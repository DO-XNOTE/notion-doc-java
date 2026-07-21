---
title: docker安装ELK 
---

# docker安装ELK 

```java
单独安装

01 安装必要的依赖
	sudo yum install -y yum-utils \
device-mapper-persistent-data \
lvm2


02 设置docker仓库
	sudo yum-config-manager --add-repo http://mirrors.aliyun.com/docker-ce/linux/centos/docker-ce.repo
	

【设置要设置一下阿里云镜像加速器】
sudo mkdir -p /etc/docker
sudo tee /etc/docker/daemon.json <<-'EOF'
{
 "registry-mirrors": ["https://orptaaqe.mirror.aliyun.com"]
}
EOF
换成这个： "registry-mirrors": ["https://orptaaqe.mirror.aliyun.com"]


sudo systemctl daemon-reload

03 安装docker

yum install -y docker-ce-18.09.0 docker-ce-cli-18.09.0 containerd.io


04 启动docker
	sudo systemctl start docker && sudo systemctl enable docker


------------------------docker pull elasticsearch:7.17.6-----------------------
docker pull kibana:7.17.6
docker pull logstash:7.17.6
mkdir -p /data/elk/es/{config,data,logs}
chmod -R 777 /data/elk/es
chmod -R 777 /data/elk/es/config
chmod -R 777 /data/elk/es/data
chmod -R 777 /data/elk/es/logs
# 报错挂载目录没权限
"Caused by: java.nio.file.AccessDeniedException: /usr/share/elasticsearch/data/nodes",

cd /data/elk/es/config
touch elasticsearch.yml
-----------------------配置内容----------------------------------
cluster.name: "my-es"
network.host: 0.0.0.0
http.port: 9200

[root@elasticsearch home]# curl http://localhost:9200
{
  "name" : "0adf1765ac08",
  "cluster_name" : "my-es",
  "cluster_uuid" : "MpKqrEKySnSdwux0m7AlEA",
  "version" : {
    "number" : "7.7.1",
    "build_flavor" : "default",
    "build_type" : "docker",
    "build_hash" : "ad56dce891c901a492bb1ee393f12dfff473a423",
    "build_date" : "2020-05-28T16:30:01.040088Z",
    "build_snapshot" : false,
    "lucene_version" : "8.5.1",
    "minimum_wire_compatibility_version" : "6.8.0",
    "minimum_index_compatibility_version" : "6.0.0-beta1"
  },
  "tagline" : "You Know, for Search"
}

1、vim /etc/sysctl.conf (需要是root账户)
文件最后添加一行: vm.max_map_count=262144
2、sysctl -p 重启生效

docker run -di -p 9200:9200 -p 9300:9300 --name es -e ES_JAVA_OPTS="-Xms1g -Xmx1g" -e "discovery.type=single-node" --restart=always -v /data/elk/es/config/elasticsearch.yml:/usr/share/elasticsearch/config/elasticsearch.yml -v /data/elk/es/data:/usr/share/elasticsearch/data -v /data/elk/es/logs:/usr/share/elasticsearch/logs elasticsearch:7.17.6

-------------------docker pull kibana:7.17.6-----------------------

获取 es 的 ip 地址
docker inspect --format '{{ .NetworkSettings.IPAddress }}' es   172.17.0.2


3、新建配置文件
用于docker文件映射。所使用目录需对应新增。（172.17.0.2改成自己的）

# vi /data/elk/kibana/kibana.yml
mkdir -p /data/elk/kibana/
vi kibana.yml
#Default Kibana configuration for docker target
server.name: kibana
server.host: "0"
elasticsearch.hosts: ["http://172.17.0.2:9200"]
xpack.monitoring.ui.container.elasticsearch.enabled: true
i18n.locale: “zh-CN”

docker run -di --restart=always --log-driver json-file --log-opt max-size=100m --log-opt max-file=2 --name kibana -p 5601:5601 -v /data/elk/kibana/kibana.yml:/usr/share/kibana/config/kibana.yml kibana:7.17.6

-------------------------------docker pull logstash:7.17.6---------------------------
mkdir -p /data/elk/logstash/
cd /data/elk/logstash/
vi logstash.yml

http.host: "0.0.0.0"
xpack.monitoring.elasticsearch.hosts: [ "http://172.17.0.2:9200" ]
xpack.monitoring.elasticsearch.username: elastic
xpack.monitoring.elasticsearch.password: guojun12
#path.config: /data/elk/logstash/conf.d/*.conf
path.config: /data/docker/logstash/conf.d/*.conf
path.logs: /var/log/logstash



mkdir -p /data/elk/logstash/conf.d
vi syslog.conf

input {
    tcp {
        port => 5044
        codec => json_lines
    }
}
output{
    elasticsearch {
		  hosts => ["172.16.136.205:9200"]  # 定义es服务器的ip
      index => "system-syslog-%{+YYYY.MM}" # 定义索引
    }
}


4、编辑本地rsyslog配置增加：
（192.168.200.94改成自己的）
vi /etc/rsyslog.conf #增加一行（外网地址）
*.* @@172.16.136.205:5044


systemctl restart rsyslog

docker run -di --restart=always --log-driver json-file --log-opt max-size=100m --log-opt max-file=2 -p 5044:5044 --name logstash -v /data/elk/logstash/logstash.yml:/usr/share/logstash/config/logstash.yml -v /data/elk/logstash/conf.d/:/data/docker/logstash/conf.d/ logstash:7.17.6


测试es接收logstash数据
curl http://localhost:9200/_cat/indices?v
health status index                    uuid                   pri rep docs.count docs.deleted store.size pri.store.size
green  open   .apm-custom-link         WBgbpphkQCS73sfjjIG0-Q   1   0          0            0       208b           208b
green  open   .kibana_task_manager_1   xmBASGi9QheR-r8hG2XLZA   1   0          5            0       28kb           28kb
green  open   .apm-agent-configuration MsvsgveHSCOhBQRCgTnsRg   1   0          0            0       208b           208b
yellow open   system-syslog-2022.02    1Vcjw7Q-TTqVscpknyK7HA   1   1          6            0     20.7kb         20.7kb
green  open   .kibana_1                vJ-B5wakRSmOrwM6ri-xgw   1   0         84            2      115kb          115kb




------------------------------------------------------------------









# kafka需要的 zk   latest
docker run -di -p 2181:2181 -p 2888:2888 -p 3888:3888 --privileed=true --restart=always --name=zkNode-1 -v /data/elk/zookeeper/conf:/conf -v /data/elk/zookeeper/data:/data -v /data/elk/zookeeper/datalog:/datalog zookeeper

### 有问题
修改自己的zookeeper主机地址
docker run  -d --name kafka -p 9092:9092 -e KAFKA_BROKER_ID=0 -e KAFKA_ZOOKEEPER_CONNECT=172.16.136.203:2181 -e KAFKA_ADVERTISED_LISTENERS=PLAINTEXT://172.16.136.203:9092 -e KAFKA_LISTENERS=PLAINTEXT://0.0.0.0:9092 -e ALLOW_PLAINTEXT_LISTENER=yes -t bitnami/kafka

#docker 启动参数说明: -d:后台启动,--restart=always:如果挂了总是会重启,--name:设置容器名
#-p: 设置宿主机与容器之间的端口映射,例如:9902:9092,表示将容器中9092端口映射到宿主机的9902端口,当有请求访问宿主机的9902端口时,会被转发到容器内部的9092端口.
#-v:设置宿主机与容器之间的路径或文件映射,例如:/home/kafka/logs:/opt/kafka/logs,表示将容器内部的路径/opt/kafka/logs目录映射到宿主机的/home/kafka/logs目录,可以方便的从宿主机/home/kafka/logs/就能访问到容器内的目录,一般数据文件夹,配置文件均可如此配置,便于管理和数据持久化
#-e 设置环境变量参数,例如-e KAFKA_BROKER_ID=1,表示将该环境变量设置到容器的环境变量中,容器在启动时会读取该环境变量,并替换掉容器中配置文件的对应默认配置(server.properties文件中的 broker.id=1)
# kafka:latest 表示使用docker镜像名称为kafka,并且版本为latest的镜像来启动
docker run -d --restart=unless-stopped --name kafka -p 9092:9092 -v /data/elk/kafka/logs:/opt/kafka/logs -v /data/elk/kafka/data:/kafka/kafka-logs -v /data/elk/kafka/conf:/opt/kafka/config -e KAFKA_BROKER_ID=1 -e KAFKA_LOG_DIRS="/kafka/kafka-logs" -e KAFKA_ZOOKEEPER_CONNECT=10.84.77.10:2181 -e KAFKA_DEFAULT_REPLICATION_FACTOR=1 -e KAFKA_LOG_RETENTION_HOURS=72 -e KAFKA_ADVERTISED_LISTENERS=PLAINTEXT://10.84.77.10:9092 -e ALLOW_PLAINTEXT_LISTENER=yes -e KAFKA_LISTENERS=PLAINTEXT://0.0.0.0:9092 -t bitnami/kafka


```

```javascript
1. 下载镜像（时间很久，耐心要足）：
docker pull sebp/elk

2. 创建Docker容器（只用在第一次使用的时候才创建）
docker run -p 5601:5601 -p 9200:9200 -p 5044:5044 -e ES_MIN_MEM=128m  -e ES_MAX_MEM=1024m -it --name elk sebp/elk


3. 进入docker容器：
docker exec -it elk /bin/bash

4. 修改配置文件
配置文件的位置：/etc/logstash/conf.d/02-beats-input.conf
将其中的内容都删掉，替换成下面的配置
input {
    tcp {
        port => 5044
        codec => json_lines

    }
}
output{
    elasticsearch {
    hosts => ["localhost:9200"]

    }
}

5.	重启docker容器（大概等5-10分钟，等待服务重启）
docker restart elk

6. 访问Kibana
http://localhost:5601/
```






