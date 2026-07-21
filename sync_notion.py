#!/usr/bin/env python3
"""Notion → GitHub Markdown 同步脚本 (GitHub Actions 版)"""
import requests, os, sys, re, time
from collections import deque

NOTION_TOKEN = os.environ.get("NOTION_TOKEN", "")
ROOT_PAGE_ID = "27475a81-2613-4b92-9415-50ae53b714c9"
OUTPUT_DIR = os.environ.get("OUTPUT_DIR", "技术学习")
HEADERS = {"Authorization": f"Bearer {NOTION_TOKEN}", "Content-Type": "application/json", "Notion-Version": "2022-06-28"}
API_COUNT = 0
RATE_LIMITER = deque()
_BLOCK_CACHE = {}  # block_id -> list[block]

def api_get(path, params=None):
    global API_COUNT
    for attempt in range(4):
        now = time.time()
        while RATE_LIMITER and now - RATE_LIMITER[0] >= 1.0:
            RATE_LIMITER.popleft()
        if len(RATE_LIMITER) >= 3:
            t = 1.0 - (now - RATE_LIMITER[0])
            if t > 0: time.sleep(t)
            now = time.time()
            while RATE_LIMITER and now - RATE_LIMITER[0] >= 1.0:
                RATE_LIMITER.popleft()
        RATE_LIMITER.append(time.time())
        API_COUNT += 1
        try:
            r = requests.get(f"https://api.notion.com/v1/{path}", headers=HEADERS, params=params, timeout=30)
        except requests.RequestException as e:
            if attempt == 3:
                print(f"  ! 网络错误放弃 {path}: {e}", flush=True)
                return None
            time.sleep(2 ** attempt)
            continue
        if r.status_code == 200:
            return r.json()
        if r.status_code == 429:
            time.sleep(float(r.headers.get("Retry-After", 1)))
            continue
        if 500 <= r.status_code < 600:
            if attempt == 3:
                print(f"  ! {r.status_code} 服务端错误放弃 {path}", flush=True)
                return None
            time.sleep(2 ** attempt)
            continue
        print(f"  ! {r.status_code} {path}: {r.text[:200]}", flush=True)
        return None
    return None

def get_children(block_id):
    if block_id in _BLOCK_CACHE:
        return _BLOCK_CACHE[block_id]
    items, cursor = [], None
    while True:
        p = {"page_size": 100}
        if cursor: p["start_cursor"] = cursor
        data = api_get(f"blocks/{block_id}/children", p)
        if not data: break
        items.extend(data.get("results", []))
        if not data.get("has_more"): break
        cursor = data.get("next_cursor")
    _BLOCK_CACHE[block_id] = items
    return items or []

def get_page_children(block_id):
    """只取 child_page 类型的 block（从缓存读取）"""
    return [b for b in get_children(block_id) if b["type"] == "child_page"]

def fmt(rich):
    out = ""
    for rt in (rich or []):
        t = rt.get("plain_text", "")
        a = rt.get("annotations", {})
        if a.get("code"): t = f"`{t}`"
        if a.get("bold"): t = f"**{t}**"
        if a.get("italic"): t = f"*{t}*"
        if a.get("strikethrough"): t = f"~~{t}~~"
        if rt.get("href"): t = f"[{t}]({rt['href']})"
        out += t
    return out

def block_md(block, depth=0):
    t = block["type"]; pfx = "  " * depth; md = ""
    rt = block.get(t, {}).get("rich_text", [])
    if t == "paragraph":
        c = fmt(rt)
        md = f"{pfx}{c}\n\n" if c.strip() else "\n"
    elif t == "heading_1": md = f"{pfx}# {fmt(rt)}\n\n"
    elif t == "heading_2": md = f"{pfx}## {fmt(rt)}\n\n"
    elif t == "heading_3": md = f"{pfx}### {fmt(rt)}\n\n"
    elif t == "bulleted_list_item": md = f"{pfx}- {fmt(rt)}\n"
    elif t == "numbered_list_item": md = f"{pfx}1. {fmt(rt)}\n"
    elif t == "to_do":
        chk = "[x]" if block["to_do"].get("checked") else "[ ]"
        md = f"{pfx}- {chk} {fmt(rt)}\n"
    elif t == "code":
        lang = block['code'].get('language', '')
        text = ''.join(x.get('plain_text', '') for x in rt)
        md = f"{pfx}```{lang}\n{text}\n```\n\n"
    elif t == "quote": md = f"{pfx}> {fmt(rt)}\n"
    elif t == "callout":
        icon = block["callout"].get("icon", {})
        emoji = icon.get("emoji", "") + " " if icon.get("type") == "emoji" else ""
        md = f"{pfx}> {emoji}{fmt(rt)}\n"
    elif t == "divider": md = f"{pfx}---\n\n"
    elif t in ("image", "video", "file", "pdf"):
        obj = block[t]; cap = fmt(obj.get("caption", []))
        url = obj.get(obj.get("type", ""), {}).get("url", "") if obj.get("type") in ("external", "file") else ""
        md = f"{pfx}[{cap or t}]({url})\n\n" if url else ""
    elif t == "bookmark":
        u = block["bookmark"].get("url", "")
        md = f"{pfx}[{u}]({u})\n\n"
    elif t == "equation": md = f"{pfx}$${block['equation'].get('expression','')}$$\n\n"
    elif t == "toggle":
        md = f"{pfx}<details><summary>{fmt(rt)}</summary>\n\n"
        if block.get("has_children"):
            for k in get_children(block["id"]):
                md += block_md(k, depth + 1)
        md += f"{pfx}</details>\n\n"
    elif t in ("synced_block", "column_list", "column"):
        if block.get("has_children"):
            for k in get_children(block["id"]):
                md += block_md(k, depth)
    return md

def render_page(page_id):
    return "".join(block_md(b) for b in get_children(page_id) if b["type"] != "child_page")

def sanitize(name):
    name = re.sub(r'[<>:"/\\|?*]', "_", name)
    return re.sub(r"\s+", " ", name).strip()[:80] or "untitled"

def get_page_title(page_id):
    data = api_get(f"pages/{page_id}")
    if not data: return "?"
    t = data.get("properties", {}).get("title", {}).get("title", [])
    return "".join(x.get("plain_text", "") for x in t) or "?"

def build_tree(page_id, depth=0, visited=None):
    if visited is None: visited = set()
    if page_id in visited: return None
    visited.add(page_id)
    title = get_page_title(page_id)
    print(f"{'  ' * depth}{title}", flush=True)
    children = []
    for b in get_page_children(page_id):
        child = build_tree(b["id"], depth + 1, visited)
        if child: children.append(child)
    return {"id": page_id, "title": title, "children": children}

def export_page(page_id, title, filepath, visited=None):
    if visited is None: visited = set()
    if page_id in visited: return
    visited.add(page_id)
    content = render_page(page_id)
    full = f"---\ntitle: {title}\n---\n\n# {title}\n\n{content}"
    os.makedirs(os.path.dirname(filepath), exist_ok=True)
    with open(filepath, "w", encoding="utf-8") as f:
        f.write(full)

def export_tree(node, parent_dir, visited=None):
    if visited is None: visited = set()
    if node["id"] in visited: return
    # 不能在此 visited.add(node["id"])：export_page 内部会自行 add，提前加会让其首行 return，导致文件永不写入
    safe = sanitize(node["title"])
    node_dir = os.path.join(parent_dir, safe)
    print(f"  {safe}", flush=True)
    export_page(node["id"], node["title"], os.path.join(node_dir, "README.md"), visited)
    for child in node.get("children", []):
        export_tree(child, node_dir, visited)

def count_pages(node):
    return 1 + sum(count_pages(ch) for ch in node.get("children", []))

def main():
    if not NOTION_TOKEN:
        print("❌ 请设置 NOTION_TOKEN 环境变量"); sys.exit(1)
    print("Notion → GitHub 同步\n", flush=True)
    print("扫描页面结构...", flush=True)
    tree = build_tree(ROOT_PAGE_ID)
    if not tree: print("❌ 失败"); sys.exit(1)
    total = count_pages(tree)
    print(f"\n根: {tree['title']} | 总页面: {total} | API: {API_COUNT}", flush=True)
    print("\n导出 Markdown...", flush=True)
    a = API_COUNT
    export_tree(tree, OUTPUT_DIR)
    print(f"\n完成! 导出 API: {API_COUNT - a} | 总计: {API_COUNT}", flush=True)
    print(f"输出: {OUTPUT_DIR}", flush=True)

if __name__ == "__main__":
    main()
