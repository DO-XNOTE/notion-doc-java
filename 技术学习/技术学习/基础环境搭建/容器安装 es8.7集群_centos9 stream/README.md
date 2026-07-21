---
title: 容器安装 es8.7集群_centos9 stream
---

# 容器安装 es8.7集群_centos9 stream

参考文档：

https://maxqiu.com/article/detail/150

[https://github.com/gm19900510/docker-es-cluster](https://github.com/gm19900510/docker-es-cluster)

```yaml
##参考文档： https://maxqiu.com/article/detail/150
#系统配置
修改 sysctl.conf
编辑配置文件

vim /etc/sysctl.conf
添加如下设置

vm.max_map_count = 262144
保存后执行以下命令立即生效


sysctl -p
检查 ulimits 的 nofile 和 nproc
运行一个测试容器（运行时会拉取 centos 镜像，请耐心等待），输出默认值


docker run --rm centos:7 /bin/bash -c 'ulimit -Hn && ulimit -Sn && ulimit -Hu && ulimit -Su'
默认情况下，会输出如下内容

前两位代表：最多可开启的文件数，最小要求65536
后两位代表：进程开启多少个线程，最小要求4096，unlimited 代表不受限制
65536
65536
unlimited
unlimited
若出现被限制的值，则需要在执行 docker run 时添加如下参数

--ulimit nofile=65536:65536 --ulimit nproc=4096:4096
禁用 swap 分区
若已关闭则忽略

方案1：关闭宿主机的 swap （推荐）
临时关闭
swapoff -a
永久关闭
#编辑配置文件
vim /etc/fstab
# 在/etc/fstab中swap分区这行前加 #
# /dev/mapper/centos-swap swap swap defaults 0 0
方案2：关闭容器的 swap
在执行 docker run 时添加如下参数

-e "bootstrap.memory_lock=true" --ulimit memlock=-1:-1
```

**Centos Stream 9 安装Docker 23.0.2 社区版安装**

```yaml
# CentOS Stream 9安装Docker 23.0.2社区版的步骤如下：


更新系统：
sql复制代码 sudo dnf update -y


添加Docker存储库的GPG密钥：
 sudo rpm --import https://download.docker.com/linux/centos/gpg



添加Docker存储库：
复制代码 sudo dnf config-manager --add-repo https://download.docker.com/linux/centos/docker-ce.repo



安装Docker Engine社区版：
lua复制代码  sudo dnf install docker-ce-23.0.2 docker-ce-cli-23.0.2 containerd.io -y



启动Docker服务：
sql复制代码 sudo systemctl start docker



设置Docker开机自启动：
bash复制代码 sudo systemctl enable docker



验证Docker安装：
复制代码 docker version

# 环境
vi /etc/security/limits.conf
* soft nofile 65536
* hard nofile 65536


vi /etc/sysctl.conf
vm.max_map_count = 262144
```

```yaml
docker network create dev
# // 运行临时容器
docker run -d --name es1 --net dev -e "discovery.type=single-node" -p 9200:9200 -p 9300:9300  elasticsearch:8.7.1


#// copy文件并修改（现创建要映射的目录）
docker cp es1:/usr/share/elasticsearch/config/ /work/elasticsearch/config

docker cp elasticsearch:/usr/share/elasticsearch/config /data/elasticsearch
docker cp elasticsearch:/usr/share/elasticsearch/logs /data/elasticsearch
docker cp elasticsearch:/usr/share/elasticsearch/data /data/elasticsearch
docker cp elasticsearch:/usr/share/elasticsearch/plugins /data/elasticsearch
#// 修改配置文件（开发测试-关闭安全策略）
vim elasticsearch.yml  (集群配置)

network.host: 0.0.0.0
http.cors.allow-origin: "*"
http.cors.enabled: truex
cluster.name: es-cluster
node.name: node1
http.port: 9200
transport.port: 9300
discovery.seed_hosts: ["192.168.13.101:9300","192.168.13.102:9300","192.168.13.103:9300"] 
cluster.initial_master_nodes: ["node1","node2","node3"] 

#// 重置密码(如果没有把安全策略关闭，又是后台运行的user是elastic)
docker exec -it es1 /usr/share/elasticsearch/bin/elasticsearch-reset-password -u elastic
#// 关闭临时容器-并删除
docker stop es1
docker rm es1
docker ps -a
docker ps

// 创建目录并给所有的目录权限
sudo chmod -R 777 /work/elasticsearch/*

#// 重新运行并挂在目录
docker run -d --name node1 --net dev \
-v /work/elasticsearch/config:/usr/share/elasticsearch/config \
-p 9200:9200 -p 9300:9300 \
elasticsearch:8.7.1

docker run -it --name node1 --net dev \
-v /work/elasticsearch/config:/usr/share/elasticsearch/config \
-p 9200:9200 -p 9300:9300 \
elasticsearch:8.7.1

docker run -d --name  node2 --net dev \
-v /work/elasticsearch/config:/usr/share/elasticsearch/config \
-p 9200:9200 -p 9300:9300 \
elasticsearch:8.7.1

docker run -d --name node3 --net dev  \
-v /work/elasticsearch/config:/usr/share/elasticsearch/config \
-p 9200:9200 -p 9300:9300 \
elasticsearch:8.7.1

# // 查看出错的容器
docker logs <容器id/名称>

# // 删除上面的出错容器
docker stop node1
docker rm node1

# // 如果能成功，把配置发送到其他节点，并修啊节点名称（其他节点授权目录权限 sudo chmod -R 777 /work/elasticsearch/*）
scp -r config/* root@192.168.13.102:/work/elasticsearch/config/
scp -r config/* root@192.168.13.103:/work/elasticsearch/config/
vim config/elasticsearch.yml 修改对应的名称

## 一、docker启动命令少了 --restart=always
1、Docker 命令修改
docker container update --restart=always 容器名字

```

```markdown
# (开发学习-不要安全验证)整体思路--->现安装单机---->拷贝配置文件到宿主机---->关闭安全验证，配置可以跨域---->重新部署三台es


# 需要使用的工具
1：在容器内部安装 vim 
1.1 进入容器  docker exec -it -u root <容器名称或者id> /bin/bash(以root的身份进入容器内部)
1.2 更新 apt-get update 
  1.2.1 下载vim工具 apt-get install vim -y
1.3 
1.2 进入 /usr/share/elasticsearch/config 拷贝config下所有的文件到宿主机



# 安装kiban

1. 运行临时容器#
docker run -d --name kibana -p 5601:5601 kibana:7.17.1
2. 创建本地挂载文件#
mkdir -p /data/kibana/config
docker cp kibana:/usr/share/kibana/config /data/kibana/
在本地就能看到拷贝出来的kibana.yml文件，
vim /data/kibana/config/kibana.yml
修改配置为
server.host: "0"
server.shutdownTimeout: "5s"
elasticsearch.hosts: [ "http://localhost:9100" ] # 记得修改ip
monitoring.ui.container.elasticsearch.enabled: true
i18n.locale: "zh-CN"
3. 停掉临时容器并重新启动#
停掉旧的
docker stop kibana
docker rm kibana
重新启动挂载了地址的新的容器
docker run -d --name kibana -p 5601:5601 -v /data/kibana/config:/usr/share/kibana/config kibana:7.17.1
# 参考 https://www.cnblogs.com/baoshu/p/16128127.html
docker cp kibana:/usr/share/kibana/plugin /data/kibana/
docker cp kibana:/usr/share/kibana/config /data/kibana/
docker cp kibana:/usr/share/kibana/data /data/kibana/
 
```

[https://www.cnblogs.com/baoshu/p/16128127.html](https://www.cnblogs.com/baoshu/p/16128127.html)

参考文档

使用 vscode修改配置是最方便的，把vscode的服务文件上传

` scp -r .vscode-server  root@192.168.13.101:~`

如果还是连接不上，把本机的.ssh文件中的 know文件中目标目标连接记录删除重新连接

[image](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/eca4e877-beb9-4e6f-96a5-be664e84d155/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662Q5NR57N%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T234351Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIH26Si5pxgXXZNE%2FOe9drywjk7AeNJNUikzUcYd3%2FB9HAiEAvf92xH0WkavtyA1MCUc8ymEx7MAtd6D%2FeoEy3FRllhIqiAQIxv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDGuUm%2BBehoBHcaLoNircA%2B3Xzc1mWN%2F7hTcfyWmNdYJ48lgBxg5uoue09iexFBy3qv02hga6ZZpX%2B1O24n44EtvsBD37FmwXg0dUml2X9vNGGlO7MPF%2BSYVbUAHtia0thShHlYBOYcH%2BgdqcfC%2FmtaYcEURR1NW4MGmfezKGUOfMIMXwnHZ3ZjzcG8pO2l2Hbr3OEzRF9WzqHx1%2FzEYJ0fbzp8HQP2JuTOjpNGqNRuW%2BpeJy3%2FsVyHGq%2FmxXMo0k1G1jIvpOQM2LHtMNRU47tIEwB%2Fk5BzZxulQaM%2Boo05umUj%2FisJDq%2BiCl8KnCFMtI5KtpPt8QdO6oPR7%2BRIpyGcRkhgP54D0TizHOmclV7NK%2B1L5d6VuRR12vAtLBeQCIg9CEu%2BGZXyg8YRCDvSM16o8%2Bk8VuuEUyV%2FtaNPCndX2a1jTjMSbH1xeN8aGOsMwzaj0t0izSKUuqApHiUdMRYClNaswuozPMJD3lJTDd%2BH9EDt7EcOZhXmEOvyeaX37oriXHJsRhI3jT%2BD%2FFcX1hN3u7GAzdg%2BMhHLdD6huLinIWymVT%2Fx%2Ft6qt4gstwZ%2FAhzXWr8NWLY4nb6nAYWq8ORE1cxcbg9N7woTZli0myR1KDrpxJjsz28sr%2FUnXUhm8FK1CdiKr8VHOcTdO0MIK7%2F9IGOqUB%2BmGdsluhuuvt908cznJP3YKAsl%2BG6nnCYRGPD66y2C7b5QRwtVnW%2BB8Bh%2FjY%2FzJk0I7xN1zlAOIviQwn2VkFQxcjIlfBQQ%2FyrYKgo39p7NEPqx37M6wXuyHVTN5Fk9sFnQYYlUcZl3oHzd2Ol7nsCLPAa2bgk6da%2BZ%2Bovxtw%2FLGYIYXmvAEYtw3j7LvvNf7J%2FvENULPryXyDFo6BKc0ZWN7vjGhk&X-Amz-Signature=54428026a99098067161d9eebdf3640fd82fbfb2c9a71ca15dbc8c0cc4dadb15&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

[image](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/d70028af-0777-4738-b0c2-e2dc21b41ee7/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662Q5NR57N%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T234351Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIH26Si5pxgXXZNE%2FOe9drywjk7AeNJNUikzUcYd3%2FB9HAiEAvf92xH0WkavtyA1MCUc8ymEx7MAtd6D%2FeoEy3FRllhIqiAQIxv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDGuUm%2BBehoBHcaLoNircA%2B3Xzc1mWN%2F7hTcfyWmNdYJ48lgBxg5uoue09iexFBy3qv02hga6ZZpX%2B1O24n44EtvsBD37FmwXg0dUml2X9vNGGlO7MPF%2BSYVbUAHtia0thShHlYBOYcH%2BgdqcfC%2FmtaYcEURR1NW4MGmfezKGUOfMIMXwnHZ3ZjzcG8pO2l2Hbr3OEzRF9WzqHx1%2FzEYJ0fbzp8HQP2JuTOjpNGqNRuW%2BpeJy3%2FsVyHGq%2FmxXMo0k1G1jIvpOQM2LHtMNRU47tIEwB%2Fk5BzZxulQaM%2Boo05umUj%2FisJDq%2BiCl8KnCFMtI5KtpPt8QdO6oPR7%2BRIpyGcRkhgP54D0TizHOmclV7NK%2B1L5d6VuRR12vAtLBeQCIg9CEu%2BGZXyg8YRCDvSM16o8%2Bk8VuuEUyV%2FtaNPCndX2a1jTjMSbH1xeN8aGOsMwzaj0t0izSKUuqApHiUdMRYClNaswuozPMJD3lJTDd%2BH9EDt7EcOZhXmEOvyeaX37oriXHJsRhI3jT%2BD%2FFcX1hN3u7GAzdg%2BMhHLdD6huLinIWymVT%2Fx%2Ft6qt4gstwZ%2FAhzXWr8NWLY4nb6nAYWq8ORE1cxcbg9N7woTZli0myR1KDrpxJjsz28sr%2FUnXUhm8FK1CdiKr8VHOcTdO0MIK7%2F9IGOqUB%2BmGdsluhuuvt908cznJP3YKAsl%2BG6nnCYRGPD66y2C7b5QRwtVnW%2BB8Bh%2FjY%2FzJk0I7xN1zlAOIviQwn2VkFQxcjIlfBQQ%2FyrYKgo39p7NEPqx37M6wXuyHVTN5Fk9sFnQYYlUcZl3oHzd2Ol7nsCLPAa2bgk6da%2BZ%2Bovxtw%2FLGYIYXmvAEYtw3j7LvvNf7J%2FvENULPryXyDFo6BKc0ZWN7vjGhk&X-Amz-Signature=ceb0e92be2701ca8248af0cd2c81a932f92909cdf29278173478a6f8ca3a1806&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

```markdown
# 系统配置

vim /etc/security/limits.conf


 62 # 官网建议生产环境需要设置bootstrap.memory_lock: true；
 63 # 若设置为true 需要在/etc/security/limits.conf添加如下内容：
 64 elasticsearch soft memlock unlimited
 65 elasticsearch hard memlock unlimited
 66 
 67 
 68 * soft nofile 65536
 69 * hard nofile 131072
 70 * soft nproc 4096
 71 * hard nproc 4096

解决：切换到root用户，进入limits.d目录下修改配置文件。
vi /etc/security/limits.d/90-nproc.conf 
修改如下内容：
* soft nproc 1024
#修改为
* soft nproc 2048



vi /etc/sysctl.conf 
添加下面配置：
vm.max_map_count=655360
并执行命令：
sysctl -p
```


