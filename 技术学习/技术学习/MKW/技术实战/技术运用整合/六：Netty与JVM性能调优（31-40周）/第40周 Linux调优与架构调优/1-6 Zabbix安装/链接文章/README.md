---
title: 链接文章
---

# 链接文章

**zabbixdocker里的mysql_docker+zabbix，使用docker搭建zabbix服务**

[image](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/52e56350-a409-4d38-a3ff-2148c380ec4e/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667UOQFDCL%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T230244Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIEJBuP04eVbb0GzBsjaaM3w1KpBPaUqFysXR%2Fl%2FF%2FMFfAiAUdfCqtKiv9dI572ajm3ideyF1paUfFA11C48CpEh90SqIBAjG%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIM8j0ReRb9bQexWvE9KtwD3%2FUbLhSlwGDZTqEDlS%2Fqxy4slfboyUJpddx4AsjO5c4rKTS8AG0K67PINR9PvBlnQt18z2dZ7YkYgFS9YQ1Zc2COkvUpJTI%2BCKkQ5lLgbXg2ZrDCel7JQDS0wTPEM7S1cFn%2BtTm5DQjuViYUKVbo4nW8MGC1%2BVSwG4eSt3c%2FKxzhX1YxOyGHAls9HdsW9heSMgNXdxDaDKtGc%2FfWojM%2FiRcR7lKccXT2%2BFmxKI3NhA4P0ZfmIJXcdva1jAZKV4qCP3rFr3qHhsSspoB8NvNN%2BezRlbx%2BStE2vMdfkId%2BPK2%2F0MyhLY6Y3i%2F0erbvqxU5RekgVFLKRa6824iSCA88wuZD9KLZO5zrFPTW2FLZGcXvD7sx5MDx610TifNzWQ1u1MzXP%2BBxWvLPLmAuUgwIu88gI9XSCxhchyNQc7VEMMTQyFH0FIRSBrP5HfTCf7tr8EeCeToc09vQ5d9djR8r15qc%2F1KJBYnnO8%2F3MgfdH1TPoQIXQFalAtxPXn1CPrpew4vXKhakqPiHOkhBHSBHI4mmafzU669ICaiIBA8UrIdvAhINuPm0ZAh66Y2J5MbYWaKQstAY4rms%2Bo6MJhpaJqH13j6OjiI0SvnCtveseBxOloDn67hLxVOhwCcw8Lf%2F0gY6pgFphucyaBD2o4CDa0SIZ8fp%2FJHPsjxuOfu3VNCPGC5weGmNGBSKqGDA%2B%2BUYulFlep4s3YtQDpswo1Dapyw%2BEn1vgY34NE53SryNlz5KYHTOc3T6Ibzk8yM1BYGdhoIX97%2BUCHrup1hHBHOzMgF%2FdHyersCXXElQs%2BlvlNdbnnfhl4dTegyHTCA3%2FpKkWfM3dfx7Qgnw7lpxx29JV11A7%2FC0GIviP%2FKl&X-Amz-Signature=31af7380b6542dd764de7861da8b2c3004ffa53fe28029fa3edc6b5eb7dbe7c8&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)


```javascript
1. 下载zabbix-server镜像，zabbix-server镜像分两种，支持MySQL数据库zabbix-server-mysql，支持支持PostgreSQL数据库zabbix/zabbix-server-pgsql。下面安装的是支持MySQL数据库的Server镜像。

打开zabbix-server-mysql的docker hub，大家会发现，zabbix-server-mysql有下面这些版本

Zabbix server 3.0 (tags: alpine-3.0-latest, ubuntu-3.0-latest, centos-3.0-latest)

Zabbix server 3.0.* (tags: alpine-3.0.*, ubuntu-3.0.*, centos-3.0.*)

Zabbix server 3.2 (tags: alpine-3.2-latest, ubuntu-3.2-latest, centos-3.2-latest)

Zabbix server 3.2.* (tags: alpine-3.2.*, ubuntu-3.2.*, centos-3.2.*)

Zabbix server 3.4 (tags: alpine-3.4-latest, ubuntu-3.4-latest, centos-3.4-latest, alpine-latest, ubuntu-latest, centos-latest, latest)

Zabbix server 3.4.* (tags: alpine-3.4.*, ubuntu-3.4.*, centos-3.4.*)

Zabbix server 4.0 (tags: alpine-trunk, ubuntu-trunk)

因为我的服务器是centos7版本，所以选择的是centos-latest版本。还有后面如果想自己重做镜像的话，选择centos版本，用着会更简单一点。在linux终端使用

docker pull zabbix/zabbix-server-mysql:centos-latest

下载zabbix-server的镜像。再通过

docker image ls

查看下载的镜像。如下图：
```

[image](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/eb088410-c7f5-4c16-87b4-6c8fcf7aebb0/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667UOQFDCL%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T230244Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIEJBuP04eVbb0GzBsjaaM3w1KpBPaUqFysXR%2Fl%2FF%2FMFfAiAUdfCqtKiv9dI572ajm3ideyF1paUfFA11C48CpEh90SqIBAjG%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIM8j0ReRb9bQexWvE9KtwD3%2FUbLhSlwGDZTqEDlS%2Fqxy4slfboyUJpddx4AsjO5c4rKTS8AG0K67PINR9PvBlnQt18z2dZ7YkYgFS9YQ1Zc2COkvUpJTI%2BCKkQ5lLgbXg2ZrDCel7JQDS0wTPEM7S1cFn%2BtTm5DQjuViYUKVbo4nW8MGC1%2BVSwG4eSt3c%2FKxzhX1YxOyGHAls9HdsW9heSMgNXdxDaDKtGc%2FfWojM%2FiRcR7lKccXT2%2BFmxKI3NhA4P0ZfmIJXcdva1jAZKV4qCP3rFr3qHhsSspoB8NvNN%2BezRlbx%2BStE2vMdfkId%2BPK2%2F0MyhLY6Y3i%2F0erbvqxU5RekgVFLKRa6824iSCA88wuZD9KLZO5zrFPTW2FLZGcXvD7sx5MDx610TifNzWQ1u1MzXP%2BBxWvLPLmAuUgwIu88gI9XSCxhchyNQc7VEMMTQyFH0FIRSBrP5HfTCf7tr8EeCeToc09vQ5d9djR8r15qc%2F1KJBYnnO8%2F3MgfdH1TPoQIXQFalAtxPXn1CPrpew4vXKhakqPiHOkhBHSBHI4mmafzU669ICaiIBA8UrIdvAhINuPm0ZAh66Y2J5MbYWaKQstAY4rms%2Bo6MJhpaJqH13j6OjiI0SvnCtveseBxOloDn67hLxVOhwCcw8Lf%2F0gY6pgFphucyaBD2o4CDa0SIZ8fp%2FJHPsjxuOfu3VNCPGC5weGmNGBSKqGDA%2B%2BUYulFlep4s3YtQDpswo1Dapyw%2BEn1vgY34NE53SryNlz5KYHTOc3T6Ibzk8yM1BYGdhoIX97%2BUCHrup1hHBHOzMgF%2FdHyersCXXElQs%2BlvlNdbnnfhl4dTegyHTCA3%2FpKkWfM3dfx7Qgnw7lpxx29JV11A7%2FC0GIviP%2FKl&X-Amz-Signature=eed7276ec1479304893da6dfcbe6dcddba7e87474b457a8364fed408d196960b&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

```plain text
3. 下载Zabbix web镜像，这里使用的是基于Nginx web服务器及支持MySQL数据库的Zabbix web接口zabbix/zabbix-web-nginx-mysql。这里是用的是latest版本，在linux终端使用
docker pull zabbix/zabbix-web-nginx-mysql:latest
下载web镜像。再通过
docker image ls
查看下载的镜像。如下图：
```

[image](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/23ea48a9-e9ea-4797-a4a3-593d187fab71/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667UOQFDCL%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T230244Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIEJBuP04eVbb0GzBsjaaM3w1KpBPaUqFysXR%2Fl%2FF%2FMFfAiAUdfCqtKiv9dI572ajm3ideyF1paUfFA11C48CpEh90SqIBAjG%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIM8j0ReRb9bQexWvE9KtwD3%2FUbLhSlwGDZTqEDlS%2Fqxy4slfboyUJpddx4AsjO5c4rKTS8AG0K67PINR9PvBlnQt18z2dZ7YkYgFS9YQ1Zc2COkvUpJTI%2BCKkQ5lLgbXg2ZrDCel7JQDS0wTPEM7S1cFn%2BtTm5DQjuViYUKVbo4nW8MGC1%2BVSwG4eSt3c%2FKxzhX1YxOyGHAls9HdsW9heSMgNXdxDaDKtGc%2FfWojM%2FiRcR7lKccXT2%2BFmxKI3NhA4P0ZfmIJXcdva1jAZKV4qCP3rFr3qHhsSspoB8NvNN%2BezRlbx%2BStE2vMdfkId%2BPK2%2F0MyhLY6Y3i%2F0erbvqxU5RekgVFLKRa6824iSCA88wuZD9KLZO5zrFPTW2FLZGcXvD7sx5MDx610TifNzWQ1u1MzXP%2BBxWvLPLmAuUgwIu88gI9XSCxhchyNQc7VEMMTQyFH0FIRSBrP5HfTCf7tr8EeCeToc09vQ5d9djR8r15qc%2F1KJBYnnO8%2F3MgfdH1TPoQIXQFalAtxPXn1CPrpew4vXKhakqPiHOkhBHSBHI4mmafzU669ICaiIBA8UrIdvAhINuPm0ZAh66Y2J5MbYWaKQstAY4rms%2Bo6MJhpaJqH13j6OjiI0SvnCtveseBxOloDn67hLxVOhwCcw8Lf%2F0gY6pgFphucyaBD2o4CDa0SIZ8fp%2FJHPsjxuOfu3VNCPGC5weGmNGBSKqGDA%2B%2BUYulFlep4s3YtQDpswo1Dapyw%2BEn1vgY34NE53SryNlz5KYHTOc3T6Ibzk8yM1BYGdhoIX97%2BUCHrup1hHBHOzMgF%2FdHyersCXXElQs%2BlvlNdbnnfhl4dTegyHTCA3%2FpKkWfM3dfx7Qgnw7lpxx29JV11A7%2FC0GIviP%2FKl&X-Amz-Signature=6536d98e5e32003db45c5638b42d16d66a184423c307e59aed2b184a5d4321f0&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

```javascript
4. 下载zabbix-java-gateway镜像， Zabbix本身不支持直接监控Java，而是使用zabbix-java-gateway监控jvm/tomcat性能。这里我们使用latest版本，在linux终端使用

docker pull zabbix/zabbix-java-gateway:latest

下载zabbix-java-gateway镜像。再通过

docker image ls

查看下载的镜像。如下图：
```

[image](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/57588ed0-7eef-4cf6-9fdc-e9b5e2c9cf9e/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667UOQFDCL%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T230244Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIEJBuP04eVbb0GzBsjaaM3w1KpBPaUqFysXR%2Fl%2FF%2FMFfAiAUdfCqtKiv9dI572ajm3ideyF1paUfFA11C48CpEh90SqIBAjG%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIM8j0ReRb9bQexWvE9KtwD3%2FUbLhSlwGDZTqEDlS%2Fqxy4slfboyUJpddx4AsjO5c4rKTS8AG0K67PINR9PvBlnQt18z2dZ7YkYgFS9YQ1Zc2COkvUpJTI%2BCKkQ5lLgbXg2ZrDCel7JQDS0wTPEM7S1cFn%2BtTm5DQjuViYUKVbo4nW8MGC1%2BVSwG4eSt3c%2FKxzhX1YxOyGHAls9HdsW9heSMgNXdxDaDKtGc%2FfWojM%2FiRcR7lKccXT2%2BFmxKI3NhA4P0ZfmIJXcdva1jAZKV4qCP3rFr3qHhsSspoB8NvNN%2BezRlbx%2BStE2vMdfkId%2BPK2%2F0MyhLY6Y3i%2F0erbvqxU5RekgVFLKRa6824iSCA88wuZD9KLZO5zrFPTW2FLZGcXvD7sx5MDx610TifNzWQ1u1MzXP%2BBxWvLPLmAuUgwIu88gI9XSCxhchyNQc7VEMMTQyFH0FIRSBrP5HfTCf7tr8EeCeToc09vQ5d9djR8r15qc%2F1KJBYnnO8%2F3MgfdH1TPoQIXQFalAtxPXn1CPrpew4vXKhakqPiHOkhBHSBHI4mmafzU669ICaiIBA8UrIdvAhINuPm0ZAh66Y2J5MbYWaKQstAY4rms%2Bo6MJhpaJqH13j6OjiI0SvnCtveseBxOloDn67hLxVOhwCcw8Lf%2F0gY6pgFphucyaBD2o4CDa0SIZ8fp%2FJHPsjxuOfu3VNCPGC5weGmNGBSKqGDA%2B%2BUYulFlep4s3YtQDpswo1Dapyw%2BEn1vgY34NE53SryNlz5KYHTOc3T6Ibzk8yM1BYGdhoIX97%2BUCHrup1hHBHOzMgF%2FdHyersCXXElQs%2BlvlNdbnnfhl4dTegyHTCA3%2FpKkWfM3dfx7Qgnw7lpxx29JV11A7%2FC0GIviP%2FKl&X-Amz-Signature=bddb315bef7d863153396dcec4b16075f89643e5cc43105d937932a04886cf25&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

### 镜像运行

```java
镜像运行

1.  启动zabbix等镜像之前，需要先创建一个新的 Docker 网络。需要将后面的zabbix-server、mysql、web等容器都加入到此网络中，方便互相访问。在终端使用下面命令创建。

docker network create -d bridge zabbix_net

创建后，可以查看是否创建成功。

docker network ls



2. 运行mysql 镜像，创建mysql容器。

docker run -dit -p 3306:3306 --name zabbix-mysql --network zabbix_net --restart always -v /etc/localtime:/etc/localtime -e MYSQL_DATABASE="zabbix" -e MYSQL_USER="zabbix" -e MYSQL_PASSWORD="zabbix_pwd" -e MYSQL_ROOT_PASSWORD="root_pwd" mysql:5.7

其中-p 是将容器中的3306端口映射到服务器的3306端口，

--network zabbix_net是将容器加入到zabbix_net网络中，

-v /etc/localtime:/etc/localtime是同步服务器和容器内部的时区，

--restart always设置自启动，

-e MYSQL_DATABASE="zabbix"，创建环境变量。

--name zabbix-mysql，给容器命名。

3. 运行zabbix-java-gateway镜像，创建zabbix-java-gateway容器。

docker run -v /etc/localtime:/etc/localtime -dit --restart=always --name=zabbix-java-gateway --network zabbix_net zabbix/zabbix-java-gateway:latest

4. 运行zabbix-server-mysql镜像，创建zabbix-server-mysql容器。

首先创建数据卷zabbix-server-vol，通过命令

docker volume create zabbix-server-vol

启动zabbix-server-mysql容器。

docker run -dit -p 10051:10051 --mount source=zabbix-server-vol,target=/etc/zabbix -v /etc/localtime:/etc/localtime -v /usr/lib/zabbix/alertscripts:/usr/lib/zabbix/alertscripts --name=zabbix-server-mysql --restart=always --network zabbix_net -e DB_SERVER_HOST="zabbix-mysql" -e MYSQL_DATABASE="zabbix" -e MYSQL_USER="zabbix" -e MYSQL_PASSWORD="zabbix_pwd" -e MYSQL_ROOT_PASSWORD="root_pwd" -e ZBX_JAVAGATEWAY="zabbix-java-gateway" zabbix/zabbix-server-mysql:centos-latest

5. 运行zabbix-web-nginx-mysql镜像，创建zabbix-web-nginx-mysql容器。

docker run -dit -p 80:80 -v /etc/localtime:/etc/localtime --name zabbix-web-nginx-mysql --restart=always --network zabbix_net -e DB_SERVER_HOST="zabbix-mysql" -e MYSQL_DATABASE="zabbix" -e MYSQL_USER="zabbix" -e MYSQL_PASSWORD="zabbix_pwd" -e MYSQL_ROOT_PASSWORD="root_pwd" -e ZBX_SERVER_HOST="zabbix-server-mysql" zabbix/zabbix-web-nginx-mysql:latest

zabbix所需容器已经全部启动，可以通docker ps 查看容器状态，如下图：
```

[image](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/f7221ad0-8e1b-41fe-a3f3-face85b306c9/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667UOQFDCL%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T230244Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIEJBuP04eVbb0GzBsjaaM3w1KpBPaUqFysXR%2Fl%2FF%2FMFfAiAUdfCqtKiv9dI572ajm3ideyF1paUfFA11C48CpEh90SqIBAjG%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIM8j0ReRb9bQexWvE9KtwD3%2FUbLhSlwGDZTqEDlS%2Fqxy4slfboyUJpddx4AsjO5c4rKTS8AG0K67PINR9PvBlnQt18z2dZ7YkYgFS9YQ1Zc2COkvUpJTI%2BCKkQ5lLgbXg2ZrDCel7JQDS0wTPEM7S1cFn%2BtTm5DQjuViYUKVbo4nW8MGC1%2BVSwG4eSt3c%2FKxzhX1YxOyGHAls9HdsW9heSMgNXdxDaDKtGc%2FfWojM%2FiRcR7lKccXT2%2BFmxKI3NhA4P0ZfmIJXcdva1jAZKV4qCP3rFr3qHhsSspoB8NvNN%2BezRlbx%2BStE2vMdfkId%2BPK2%2F0MyhLY6Y3i%2F0erbvqxU5RekgVFLKRa6824iSCA88wuZD9KLZO5zrFPTW2FLZGcXvD7sx5MDx610TifNzWQ1u1MzXP%2BBxWvLPLmAuUgwIu88gI9XSCxhchyNQc7VEMMTQyFH0FIRSBrP5HfTCf7tr8EeCeToc09vQ5d9djR8r15qc%2F1KJBYnnO8%2F3MgfdH1TPoQIXQFalAtxPXn1CPrpew4vXKhakqPiHOkhBHSBHI4mmafzU669ICaiIBA8UrIdvAhINuPm0ZAh66Y2J5MbYWaKQstAY4rms%2Bo6MJhpaJqH13j6OjiI0SvnCtveseBxOloDn67hLxVOhwCcw8Lf%2F0gY6pgFphucyaBD2o4CDa0SIZ8fp%2FJHPsjxuOfu3VNCPGC5weGmNGBSKqGDA%2B%2BUYulFlep4s3YtQDpswo1Dapyw%2BEn1vgY34NE53SryNlz5KYHTOc3T6Ibzk8yM1BYGdhoIX97%2BUCHrup1hHBHOzMgF%2FdHyersCXXElQs%2BlvlNdbnnfhl4dTegyHTCA3%2FpKkWfM3dfx7Qgnw7lpxx29JV11A7%2FC0GIviP%2FKl&X-Amz-Signature=66b40a2d1acaae68845528d124d2be9c6714d7917cedc60eb9e088cafb544999&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

```java

6. 在浏览器中输入http://IP/zabbix，打开zabbix首页，其中用户名密码分别是admin/zabbix。

出现下面页面，zabbix搭建成功。是不是比自己创建数据库，搭建zabbix-server简单很多。
```

[image](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/6c084694-9569-4731-9342-c20f58b07e76/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667UOQFDCL%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T230244Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIEJBuP04eVbb0GzBsjaaM3w1KpBPaUqFysXR%2Fl%2FF%2FMFfAiAUdfCqtKiv9dI572ajm3ideyF1paUfFA11C48CpEh90SqIBAjG%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIM8j0ReRb9bQexWvE9KtwD3%2FUbLhSlwGDZTqEDlS%2Fqxy4slfboyUJpddx4AsjO5c4rKTS8AG0K67PINR9PvBlnQt18z2dZ7YkYgFS9YQ1Zc2COkvUpJTI%2BCKkQ5lLgbXg2ZrDCel7JQDS0wTPEM7S1cFn%2BtTm5DQjuViYUKVbo4nW8MGC1%2BVSwG4eSt3c%2FKxzhX1YxOyGHAls9HdsW9heSMgNXdxDaDKtGc%2FfWojM%2FiRcR7lKccXT2%2BFmxKI3NhA4P0ZfmIJXcdva1jAZKV4qCP3rFr3qHhsSspoB8NvNN%2BezRlbx%2BStE2vMdfkId%2BPK2%2F0MyhLY6Y3i%2F0erbvqxU5RekgVFLKRa6824iSCA88wuZD9KLZO5zrFPTW2FLZGcXvD7sx5MDx610TifNzWQ1u1MzXP%2BBxWvLPLmAuUgwIu88gI9XSCxhchyNQc7VEMMTQyFH0FIRSBrP5HfTCf7tr8EeCeToc09vQ5d9djR8r15qc%2F1KJBYnnO8%2F3MgfdH1TPoQIXQFalAtxPXn1CPrpew4vXKhakqPiHOkhBHSBHI4mmafzU669ICaiIBA8UrIdvAhINuPm0ZAh66Y2J5MbYWaKQstAY4rms%2Bo6MJhpaJqH13j6OjiI0SvnCtveseBxOloDn67hLxVOhwCcw8Lf%2F0gY6pgFphucyaBD2o4CDa0SIZ8fp%2FJHPsjxuOfu3VNCPGC5weGmNGBSKqGDA%2B%2BUYulFlep4s3YtQDpswo1Dapyw%2BEn1vgY34NE53SryNlz5KYHTOc3T6Ibzk8yM1BYGdhoIX97%2BUCHrup1hHBHOzMgF%2FdHyersCXXElQs%2BlvlNdbnnfhl4dTegyHTCA3%2FpKkWfM3dfx7Qgnw7lpxx29JV11A7%2FC0GIviP%2FKl&X-Amz-Signature=042821b0c5921925ca0e43777499505fc90e5ef15cfe686dd28986a95b491f59&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)


