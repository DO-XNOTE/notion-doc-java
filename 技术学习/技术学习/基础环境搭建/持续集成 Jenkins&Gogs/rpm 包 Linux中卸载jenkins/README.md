---
title: rpm 包 Linux中卸载jenkins
---

# rpm 包 Linux中卸载jenkins

```markdown
# 1、rpm卸载:  rpm -e jenkins
# 2、检查是否卸载成功: rpm -ql jenkins
# 3、彻底删除残留文件： find / -iname jenkins | xargs -n 1000 rm -rf
```

