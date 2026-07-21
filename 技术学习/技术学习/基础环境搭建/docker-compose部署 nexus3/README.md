---
title: docker-compose部署 nexus3
---

# docker-compose部署 nexus3

直接使用安装包安装到 linux 中的 nexus

用户名名：admin

密码：guojun12

所在机器的：192.168.13.218

默认端口：8081




```markdown
#安装docker
[root@nexus ~]# yum -y install docker

#安装docker-compose
[root@nexus ~]# curl -L https://get.daocloud.io/docker/compose/releases/download/v2.4.1/docker-compose-`uname -s`-`uname -m` > /usr/local/bin/docker-compose
[root@nexus ~]# sudo chmod +x /usr/local/bin/docker-compose
[root@nexus ~]# docker-compose --version

#创建yml文件
[root@nexus ~]# cat > docker-compose.yml << EOF
version: '3'
services:
  nexus:
    image: sonatype/nexus3
    restart: always
    container_name: nexus
    environment:
      - TZ=Asia/Shanghai
    ports:
      - '8081:8081'
    volumes:
      - /data/nexus:/nexus-data
EOF

#创建目录
[root@nexus ~]# mkdir -p /data/nexus
[root@nexus ~]# chmod 777 /data/nexus

#启动服务
[root@nexus ~]# docker-compose up -d
[root@nexus ~]# docker ps -a

#访问地址： http://192.168.10.50:8081

#查看密码
[root@nexus ~]# docker exec nexus cat /nexus-data/admin-password
```

二、nexus代理、settings及pom设置方式如地址：
 

[https://www.cnblogs.com/cgy1995/archive/2022/11/08/16869302.html](https://www.cnblogs.com/cgy1995/archive/2022/11/08/16869302.html)

[https://blog.51cto.com/u_15773967/5639059](https://blog.51cto.com/u_15773967/5639059)

