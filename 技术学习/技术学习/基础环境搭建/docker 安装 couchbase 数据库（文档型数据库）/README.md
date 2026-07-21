---
title: docker 安装 couchbase 数据库（文档型数据库）
---

# docker 安装 couchbase 数据库（文档型数据库）

```shell
1:  docker pull couchbase

2:

企业版   docker run -d --name db -p 8091-8097:8091-8097 -p 9123:9123 -p 11207:11207 -p 11210:11210 -p 11280:11280 -p 18091-18097:18091-18097 couchbase

or 

社区版

docker run -d --name db -p 8091-8097:8091-8097 -p 9123:9123 -p 11207:11207 -p 11210:11210 -p 11280:11280 -p 18091-18097:18091-18097 couchbase:community-7.2.1

3: 接下来，访问 `http://localhost:8091` 主机上以查看 Web 控制台以启动 Couchbase 服务器设置。
```

4: 官方文档 port 暴露

[https://docs.couchbase.com/server/current/install/install-ports.html](https://docs.couchbase.com/server/current/install/install-ports.html)


