---
title: docker 安装 mongodb
---

# docker 安装 mongodb



```markdown

## 安装了 mongodb 7.x

# 运用容器创建镜像
docker run -d --name mymondb -e MONGO_INITDB_ROOT_USERNAME=admin -e MONGO_INITDB_ROOT_PASSWORD=123456 -p 27017:27017 mongo:latest

# 创建数据库


```


