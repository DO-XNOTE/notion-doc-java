---
title: mysql的 yum 安装
---

# mysql的 yum 安装

[https://dev.mysql.com/doc/refman/8.0/en/linux-installation-yum-repo.html?spm=a2c6h.12873639.article-detail.8.72b91135O5IpwU](https://dev.mysql.com/doc/refman/8.0/en/linux-installation-yum-repo.html?spm=a2c6h.12873639.article-detail.8.72b91135O5IpwU)

[https://dev.mysql.com/doc/mysql-yum-repo-quick-guide/en/](https://dev.mysql.com/doc/mysql-yum-repo-quick-guide/en/)

这篇文章可以看看

[https://developer.aliyun.com/article/1055597](https://developer.aliyun.com/article/1055597)


```markdown
# mysql的 yum 安装
集群安装 198 199  200三台机器上
root 用户的密码  
199 GUOjun@12
198 GUOjun@12
```

```markdown
 ELK:  203. 204 .205 .206.
 # 单机：E:203  L:204  K:205
 # 配置：elastciserach.yml
 cluster.name: es-elasticsearch
 node.name: es-node1
 path.data: /usr/local/software/elasticsearch-7.13.0/data
 path.logs: /usr/local/software/elasticsearch-7.13.0/logs
 network.host: 0.0.0.0
 http.cors.enabled: true
 http.cors.allow-origin: "*"
 cluster.initial_master_nodes: ["es-node1"]
 
 
 # 至少需要的内存设置
 vim /etc/security/limits.conf
 * soft nofile 65535
 * hard nofile 131072
 * soft nproc 2048
 * hard nproc 4096
 # 另一个需要配置的文件
 vim /etc/sysctl.conf
 vm.max_map_count=262144
 刷新： sysctl -p
 
 useradd esuser
 chown -R esuser /usr/local/software/elasticsearch-7.13.0/
 chown -R esuser /usr/local/software/elasticsearch-7.13.0/bin
 su root
 
 
 运行”：# ./bin/elasticsearch
 # ./bin/elasticsearch -d 后台启动
 
 
 # Elasticsearch 集群 213， 214， 215
 * soft nofile 65535
 * hard nofile 131072
 * soft nproc 65535
 * hard nproc 65535
 root soft nproc 65536
 root hard nproc 65536
 root soft nofile 65536
 root hard nofile 65536
 discovery.seed_hosts: ["192.16.136.213", "192.16.136.214", "192.16.136.215"]
 
 more config/elasticsearch.yml | grep ^[^#]
 ./bin/elasticsearch
 
 ## Kibana 部署和配置
 创建用户 adduser kibuser
 chown -R  kibuser kibana-7.13.0-linux-aarch64/bin
 chown -R  kibuser kibana-7.13.0-linux-aarch64/
 
 
 find / -name "libstdc++.so*" 把ES的动态库复制到 Kibana机器上/usr/lib64
 scp /usr/local/software/elasticsearch-7.13.0/modules/x-pack-ml/platform/linux-aarch64/lib/libstdc++.so.6 root@172.16.136.205:/usr/lib64
 
 
 
 ### Logstash 启动同步mysql数据到Es   -f ：指定配置文件
  启动：   ./bin/logstash -f sync/logstash-db-sync.conf
```

## **Mycat中分库分表使用的Mysql安装的虚拟机节点**

```markdown
 ## Mysql8：200 , 201
 ## Mycat： 在Mac上 本来想要部署在202上但是没有arrch版本的
 
 1.1 查询是否安装了mysql
 rpm -qa|grep mysql
 
 1.2 卸载mysql （下面是卸载mysql的库，防止产生冲突，mysql也是类似卸载方式）
 
 rpm -e --nodeps mysql-libs-5.1.*
 卸载之后，记得：
 find / -name mysql
 删除查询出来的所有东西
 
 2 centos7安装mysql
 wget http://dev.mysql.com/get/mysql-community-release-el7-5.noarch.rpm
 #rpm -ivh mysql-community-release-el7-5.noarch.rpm
 #yum install mysql-community-server
 成功安装之后重启mysql服务
 #service mysqld restart
 初次安装mysql是root账户是没有密码的
 设置密码的方法
 #mysql -uroot
 mysql> set password for ‘root’@‘localhost’ = password('mypasswd');
 mysql> exit



# 高可用Mycat防止单点故障
# 202 安装 haproxy
yum search haproxy

install -y install haproxy.aarch


 
```

## **分库分表-Mycat和两台mysql所在节点**

```c
 ##Mysql: 200,201.202
 Mycat: mac上  /Users/guojun/workspaces/mycat2/conf
 200:使用 guojun/guojun12 登录
 201:使用 guojun/guojun12 登录
 
 
 用户做分库分表使用的数据库：
 安装在虚拟机上的mysql   172.16.136.200， 172.16.136.201
 用户名：guojun
 密码：guojun12
 
 
 创建用户使用 navicat来连接：%：表示所有的主机都可以连接
 语句： 
create user 'guojun'@'%' identified with mysql_native_password by 'guojun12'
 密码： guojun12
 用户名：guojun
 授权：grant all on *.* 'guojun'@'%';
 然后刷新： flush privileges;
 
 mycat安装在 200.201上面
```




