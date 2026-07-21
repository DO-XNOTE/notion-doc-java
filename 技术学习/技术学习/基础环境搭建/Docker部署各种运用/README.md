---
title: Docker部署各种运用
---

# Docker部署各种运用


```markdown


在223,226 虚拟机节点上
用户名：admin
密码：123456

# docker run -di --restart=t balways --name=rabbitmq2 -p 5673:5672 -p 15673:15672 -v ~/rabbit2/data:/var/lib/rabbitmq  -v ~/rabbit2/conf:/etc/rabbitmq/conf.d/  -e RABBITMQ_DEFAULT_USER=admin -e RABBITMQ_DEFAULT_PASS=123456 docker.io/rabbitmq 

容器内配置文件的路径： /etc/rabbitmq/conf.d/
docker run -di --restart=always --name rabbitmq-3.11.1 -p 15672:15672 -p 5672:5672 docker.io/rabbitmq:3.11.1
docker run -di --restart=always --name rabbitmq2 -p 15673:15672 -p 5673:5672 docker.io/rabbitmq:3.11.1
进入rabbitMq容器：
docker exec -it  {rabbitmq容器id} /bin/bash
查看配置文件
cat /etc/rabbitmq/conf.d/management_agent.disable_metrics_collector.conf
将配置文件内容，true改为false：
cd  /etc/rabbitmq/conf.d/
echo management_agent.disable_metrics_collector = false > management_agent.disable_metrics_collector.conf
.退出容器：
exit
输入指令，安装插件：
docker exec -it {rabbitmq容器名称或者id} rabbitmq-plugins enable rabbitmq_management
5.重启容器：
docker restart {rabbitmq容器id}
http://ip地址:15672，这里的用户名和密码默认都是guest


# 延迟插件
docker cp rabbitmq_delayed_message_exchange-3.11.1.ez rabbitmq-3.11.1:/plugins
docker exec -it rabbitmq-3.11.1 /bin/bash 
rabbitmq-plugins list
rabbitmq-plugins enable rabbitmq_delayed_message_exchange
# 重启 rabit 容器



参数说明：
-d 后台运行容器；
–name 指定容器名；
-p 指定服务运行的端口（5672：应用访问端口；15672：控制台Web端口号）；
-v 映射目录或文件；
–hostname 主机名（RabbitMQ的一个重要注意事项是它根据所谓的 “节点名称” 存储数据，默认为主机名）；
-e 指定环境变量；（RABBITMQ_DEFAULT_VHOST：默认虚拟机名；RABBITMQ_DEFAULT_USER：默认的用户名；RABBITMQ_DEFAULT_PASS：默认用户名的密码）
ea2a13ef38ba 表示镜像的ID

# 6.Docker run 后，使用docker ps 查看在运行中也存在RabbitMQ。web界面无法访问，需要进入进行配置
进入RabbitMQ
# docker exec -it rabbitmq /bin/bash
开启web管理页面
# rabbitmq-plugins enable rabbitmq_management

# rabbitmq设置docker 运行自启动，先找到对应的rabbitmq的镜像ID

# 设置RabbitMQ自启动  docker update 容器ID --restart=always

# 重启docker

# 最后访问rabbitmq的WEB界面
  http://IP:15672/

```

## ============Docker  安装 Mysql ===================

```markdown
# 部署 mysql
# -p 3306:3306 端口映射 前面是宿主机的端口，后面是容器的端口
# -e 指定用户名的密码   （-e MYSQL_ROOT_PASSWORD 不可变）
docker run -di -p 3306:3306 --restart=always --name=avery_mysql -e MYSQL_ROOT_PASSWORD=guojun12 mysql
```

[image](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/53a19b1c-80cf-4e31-ba8d-d224798b2906/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UW3NL7VX%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T234348Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIEmto5bKXUaoT1AJ9rac8SNKzSJA8rdClcu8dWMSkYFnAiEA08sHuYqhouzv7Q43xp5qK7gCIjUjU0OwdmwghckC8RMqiAQIxv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDF4mbF6RlLyoOgBgAircA%2FITKtBJ%2BVZYMvIOtbg3U4fiVnsGDFNnNanaiwymh4hZR7q6MVxswyuUcTpCesd1qJAUa0jSDvcLJghkG9qrm0pneZ5jhZh9Zb0lH8Gs76%2FU5qetH4FKEVVQcdvIih8QjyU%2FFQp6R4sCd0Pq7Yr88Q2LIPiZGtcBH5jZzBXh3JP5LYdLlHOPEQjLLvIS8Q2UtfYuiz%2F2snrjc%2FEJv%2BgIUUChjRboZmZil0A1rb%2FZilVn%2FpLg50vNP8sYluF9gfec%2FYFsGCN%2BGuARGMwh6PTrT9qcU%2FWfjqIvvaijWfQ7vDOxykGk8sxGeNbLxZMzBpcSxM9ve%2F8fEE%2FqDTUztr6S4Dq5XuzycS6l2Uedh8Vhr1rBKG8jSOv1xbZr1WLpD2I7IOmFt7zCM43bHxbfnuoFSifLgT3OG88QJZf7BHYyxn2o2nRSbBiheIgPb5KRQy9fkIPzM6b1vbIIzDJwGjv38oYraHdBN7jhHc7GxuZ7OSR%2BtQt3JSaeKxihHSMg7qoNWonFo3WoqwS2oh0rBYVNomJO1K9dhqJbq7FcWtHTePPxK6R5bwI19nhdKhhrk6GEuYfMwDnOhf7n7d%2BQnDnz5klTk%2BTKqfObmXg8boZJFcpwAKecKi8WFO%2FvW3l7MLS3%2F9IGOqUBgZFPXZAc3MkhWtZnkpEV8nps206Kgbh05be%2FubDcv1gikBq7bRFmojGrXydNUOWM9NZFmSKVrat2M74BCqbeTIxKqCQbO2TV6ARBT1oQA2YAEAyrG03n4QqQe1LLkNmks3MATwc2i6C2dBRXBuprGePLZXFFLT7O5FTjtTMjcSOglAeTzgEWGCpIXP7H97t2%2F0s8Ue%2FGI114BDFxM5qfXoKigim5&X-Amz-Signature=a4ff2de075399f3f78f07c37de8afd814c4195fd67ab0fd58d4d287e03e5e90f&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

## ============Docker 安装 Tomcat ==================

```markdown
  100 节点
# 部署 tomcat      容器内部tomcat的目录映射：/usr/local/tomcat/webapps

## docker run -di --name=AveryTomcat -p 8880:8080 -v /usr/local/software/webapps:/usr/local/tomcat/webapps tomcat
```

[image](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/16012e9b-bd29-4b3b-a49d-a0ffb15168fc/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UW3NL7VX%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T234348Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIEmto5bKXUaoT1AJ9rac8SNKzSJA8rdClcu8dWMSkYFnAiEA08sHuYqhouzv7Q43xp5qK7gCIjUjU0OwdmwghckC8RMqiAQIxv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDF4mbF6RlLyoOgBgAircA%2FITKtBJ%2BVZYMvIOtbg3U4fiVnsGDFNnNanaiwymh4hZR7q6MVxswyuUcTpCesd1qJAUa0jSDvcLJghkG9qrm0pneZ5jhZh9Zb0lH8Gs76%2FU5qetH4FKEVVQcdvIih8QjyU%2FFQp6R4sCd0Pq7Yr88Q2LIPiZGtcBH5jZzBXh3JP5LYdLlHOPEQjLLvIS8Q2UtfYuiz%2F2snrjc%2FEJv%2BgIUUChjRboZmZil0A1rb%2FZilVn%2FpLg50vNP8sYluF9gfec%2FYFsGCN%2BGuARGMwh6PTrT9qcU%2FWfjqIvvaijWfQ7vDOxykGk8sxGeNbLxZMzBpcSxM9ve%2F8fEE%2FqDTUztr6S4Dq5XuzycS6l2Uedh8Vhr1rBKG8jSOv1xbZr1WLpD2I7IOmFt7zCM43bHxbfnuoFSifLgT3OG88QJZf7BHYyxn2o2nRSbBiheIgPb5KRQy9fkIPzM6b1vbIIzDJwGjv38oYraHdBN7jhHc7GxuZ7OSR%2BtQt3JSaeKxihHSMg7qoNWonFo3WoqwS2oh0rBYVNomJO1K9dhqJbq7FcWtHTePPxK6R5bwI19nhdKhhrk6GEuYfMwDnOhf7n7d%2BQnDnz5klTk%2BTKqfObmXg8boZJFcpwAKecKi8WFO%2FvW3l7MLS3%2F9IGOqUBgZFPXZAc3MkhWtZnkpEV8nps206Kgbh05be%2FubDcv1gikBq7bRFmojGrXydNUOWM9NZFmSKVrat2M74BCqbeTIxKqCQbO2TV6ARBT1oQA2YAEAyrG03n4QqQe1LLkNmks3MATwc2i6C2dBRXBuprGePLZXFFLT7O5FTjtTMjcSOglAeTzgEWGCpIXP7H97t2%2F0s8Ue%2FGI114BDFxM5qfXoKigim5&X-Amz-Signature=9a9a35500de3365d6979a5542eab64716da68f8308edbdce5b77eedec3ef6cf8&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

## =============Docker 安装 Nginx==================

```markdown
# 部署 Nginx  使用 CP 命令部署静态资源    100节点
# docker run -di --restart=always --name=AveryNginx -p 1000:80 -v /root/foodie-cloud/foodie-shop/:/usr/share/nginx/html nginx

# 部署项目
# docker run -di --restart=always --name=FoodieNginx -p 8080:80 -v /root/foodie-cloud/foodie-shop/:/usr/share/nginx/html nginx



没有使用-v进行目录映射，怎么上传态页面部署上去
# 先进去容器中然后看一下 目录结构
#  =================dir 命令================ 看目录结构

# 进入Nginx的容器
docker exec -it 容器id + /bin/bash
# Nginx 安装在了 etc 目录下
# cat + 配置文件可以查看内容

# 进入到 conf.d 目录下 查看default.conf
## cat default.conf
找到 root目录 在 /var/share/nginx/html 有欢迎页
把我们的静态文件所在的目录改成 html
使用 cp 命令 拷贝我们的资源到  /usr/share/nginx/html 中
退出容器使用docker cp html  到 /usr/share/nginx/html下
# docker cp html + 宿主机名称：/usr/share/nginx/html

# docker cp html AveryNginx:/usr/share/nginx/
```


## ===============Docker 部署 Redis ================

```markdown
# Docker 部署 Redis      100节点
# docker run -di --name=AveryRedis -p 6379:6379 -v ~/redis/redis.conf:/etc/redis/redis.conf -v ~/redis/data:/data redis

docker exec -it + id +/bin/bash

```

[image](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/6d362619-9db5-47a4-b058-982e7f4a698a/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UW3NL7VX%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T234348Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIEmto5bKXUaoT1AJ9rac8SNKzSJA8rdClcu8dWMSkYFnAiEA08sHuYqhouzv7Q43xp5qK7gCIjUjU0OwdmwghckC8RMqiAQIxv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDF4mbF6RlLyoOgBgAircA%2FITKtBJ%2BVZYMvIOtbg3U4fiVnsGDFNnNanaiwymh4hZR7q6MVxswyuUcTpCesd1qJAUa0jSDvcLJghkG9qrm0pneZ5jhZh9Zb0lH8Gs76%2FU5qetH4FKEVVQcdvIih8QjyU%2FFQp6R4sCd0Pq7Yr88Q2LIPiZGtcBH5jZzBXh3JP5LYdLlHOPEQjLLvIS8Q2UtfYuiz%2F2snrjc%2FEJv%2BgIUUChjRboZmZil0A1rb%2FZilVn%2FpLg50vNP8sYluF9gfec%2FYFsGCN%2BGuARGMwh6PTrT9qcU%2FWfjqIvvaijWfQ7vDOxykGk8sxGeNbLxZMzBpcSxM9ve%2F8fEE%2FqDTUztr6S4Dq5XuzycS6l2Uedh8Vhr1rBKG8jSOv1xbZr1WLpD2I7IOmFt7zCM43bHxbfnuoFSifLgT3OG88QJZf7BHYyxn2o2nRSbBiheIgPb5KRQy9fkIPzM6b1vbIIzDJwGjv38oYraHdBN7jhHc7GxuZ7OSR%2BtQt3JSaeKxihHSMg7qoNWonFo3WoqwS2oh0rBYVNomJO1K9dhqJbq7FcWtHTePPxK6R5bwI19nhdKhhrk6GEuYfMwDnOhf7n7d%2BQnDnz5klTk%2BTKqfObmXg8boZJFcpwAKecKi8WFO%2FvW3l7MLS3%2F9IGOqUBgZFPXZAc3MkhWtZnkpEV8nps206Kgbh05be%2FubDcv1gikBq7bRFmojGrXydNUOWM9NZFmSKVrat2M74BCqbeTIxKqCQbO2TV6ARBT1oQA2YAEAyrG03n4QqQe1LLkNmks3MATwc2i6C2dBRXBuprGePLZXFFLT7O5FTjtTMjcSOglAeTzgEWGCpIXP7H97t2%2F0s8Ue%2FGI114BDFxM5qfXoKigim5&X-Amz-Signature=9e89479667dc0d1d990db03d054e12f1e5544f0420aa814e1b2f206fb166f6ad&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

```markdown
# 场景1： 可以把容器变成一个镜像，也可以把镜像导出成文件进行备份，然后进行恢复成镜像
# 可以把一台服务的镜像迁移到另一台服务器上在进行恢复。这种情况还是比较常见的

# 场景2： 通过某个镜像创建了一个容器，对着个容器进行了配置上进行的修改，希望通过这个容器
# 创建另一个容器， 就可以把这个容器保存为一个镜像，基于这个镜像创建的新的容器能提高效率得到新的
# 容器，得到新的环境， 这就是容器的备份和迁移

# 比如备份 Nginx 容器成镜像
使用的命令是 commit
docker commit AveryNginx new_averynginx_mirror
# commit 创建镜像的命令
# AveryNginx 原容器
# 备份的镜像 new_averynginx_mirror

# ===============注意镜像名称不能出现大写 错误：new_AveryNginx_Mirror===================



# 基于备份的镜像 创建新的容器
docker run -di --name=XnoteNginx -p 2000:80 new_averynginx_mirror
# 1000端口被占用 2000薪的镜像端口


# 镜像的备份成tar文件
docker save -o xxx.tar new_averynginx_mirror
# -o ; 是输出的意思 output  到处到了当前的目录
# docker save -o last_new_averynginx_mirror.tar new_averynginx_mirror
```

[image](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/1699d726-2b88-4a2f-8c52-b3722b07f036/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UW3NL7VX%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T234348Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIEmto5bKXUaoT1AJ9rac8SNKzSJA8rdClcu8dWMSkYFnAiEA08sHuYqhouzv7Q43xp5qK7gCIjUjU0OwdmwghckC8RMqiAQIxv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDF4mbF6RlLyoOgBgAircA%2FITKtBJ%2BVZYMvIOtbg3U4fiVnsGDFNnNanaiwymh4hZR7q6MVxswyuUcTpCesd1qJAUa0jSDvcLJghkG9qrm0pneZ5jhZh9Zb0lH8Gs76%2FU5qetH4FKEVVQcdvIih8QjyU%2FFQp6R4sCd0Pq7Yr88Q2LIPiZGtcBH5jZzBXh3JP5LYdLlHOPEQjLLvIS8Q2UtfYuiz%2F2snrjc%2FEJv%2BgIUUChjRboZmZil0A1rb%2FZilVn%2FpLg50vNP8sYluF9gfec%2FYFsGCN%2BGuARGMwh6PTrT9qcU%2FWfjqIvvaijWfQ7vDOxykGk8sxGeNbLxZMzBpcSxM9ve%2F8fEE%2FqDTUztr6S4Dq5XuzycS6l2Uedh8Vhr1rBKG8jSOv1xbZr1WLpD2I7IOmFt7zCM43bHxbfnuoFSifLgT3OG88QJZf7BHYyxn2o2nRSbBiheIgPb5KRQy9fkIPzM6b1vbIIzDJwGjv38oYraHdBN7jhHc7GxuZ7OSR%2BtQt3JSaeKxihHSMg7qoNWonFo3WoqwS2oh0rBYVNomJO1K9dhqJbq7FcWtHTePPxK6R5bwI19nhdKhhrk6GEuYfMwDnOhf7n7d%2BQnDnz5klTk%2BTKqfObmXg8boZJFcpwAKecKi8WFO%2FvW3l7MLS3%2F9IGOqUBgZFPXZAc3MkhWtZnkpEV8nps206Kgbh05be%2FubDcv1gikBq7bRFmojGrXydNUOWM9NZFmSKVrat2M74BCqbeTIxKqCQbO2TV6ARBT1oQA2YAEAyrG03n4QqQe1LLkNmks3MATwc2i6C2dBRXBuprGePLZXFFLT7O5FTjtTMjcSOglAeTzgEWGCpIXP7H97t2%2F0s8Ue%2FGI114BDFxM5qfXoKigim5&X-Amz-Signature=78772106470bab2acd6b2aadcee5daced898eee45f25ae34fa22e7ef1828052a&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

```markdown
#  使用备份的镜像进行恢复容器
#  docker load -i last_new_averynginx_mirror.tar
#  i： 就是input输入的意思, 操作后恢复了原来进行备份的镜像，名称是 “new_averynginx_mirror”
#  而不是 last_ndockew_averynginx_mirror（文件名）同一台机器上的话再创建容器，需要删除原来的容器
# 不是同一台机器的话无所谓

```

[image](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/5f1d9939-534e-4d03-b88f-6d2e6f82b6a4/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UW3NL7VX%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T234348Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIEmto5bKXUaoT1AJ9rac8SNKzSJA8rdClcu8dWMSkYFnAiEA08sHuYqhouzv7Q43xp5qK7gCIjUjU0OwdmwghckC8RMqiAQIxv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDF4mbF6RlLyoOgBgAircA%2FITKtBJ%2BVZYMvIOtbg3U4fiVnsGDFNnNanaiwymh4hZR7q6MVxswyuUcTpCesd1qJAUa0jSDvcLJghkG9qrm0pneZ5jhZh9Zb0lH8Gs76%2FU5qetH4FKEVVQcdvIih8QjyU%2FFQp6R4sCd0Pq7Yr88Q2LIPiZGtcBH5jZzBXh3JP5LYdLlHOPEQjLLvIS8Q2UtfYuiz%2F2snrjc%2FEJv%2BgIUUChjRboZmZil0A1rb%2FZilVn%2FpLg50vNP8sYluF9gfec%2FYFsGCN%2BGuARGMwh6PTrT9qcU%2FWfjqIvvaijWfQ7vDOxykGk8sxGeNbLxZMzBpcSxM9ve%2F8fEE%2FqDTUztr6S4Dq5XuzycS6l2Uedh8Vhr1rBKG8jSOv1xbZr1WLpD2I7IOmFt7zCM43bHxbfnuoFSifLgT3OG88QJZf7BHYyxn2o2nRSbBiheIgPb5KRQy9fkIPzM6b1vbIIzDJwGjv38oYraHdBN7jhHc7GxuZ7OSR%2BtQt3JSaeKxihHSMg7qoNWonFo3WoqwS2oh0rBYVNomJO1K9dhqJbq7FcWtHTePPxK6R5bwI19nhdKhhrk6GEuYfMwDnOhf7n7d%2BQnDnz5klTk%2BTKqfObmXg8boZJFcpwAKecKi8WFO%2FvW3l7MLS3%2F9IGOqUBgZFPXZAc3MkhWtZnkpEV8nps206Kgbh05be%2FubDcv1gikBq7bRFmojGrXydNUOWM9NZFmSKVrat2M74BCqbeTIxKqCQbO2TV6ARBT1oQA2YAEAyrG03n4QqQe1LLkNmks3MATwc2i6C2dBRXBuprGePLZXFFLT7O5FTjtTMjcSOglAeTzgEWGCpIXP7H97t2%2F0s8Ue%2FGI114BDFxM5qfXoKigim5&X-Amz-Signature=1c741200393a17a2b4d7cd3ed1012a534e4b36cb5f69e44aca37a7243e0e3a32&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

[image](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/c382d1ab-3467-4a08-be0f-66072512a384/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UW3NL7VX%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T234348Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIEmto5bKXUaoT1AJ9rac8SNKzSJA8rdClcu8dWMSkYFnAiEA08sHuYqhouzv7Q43xp5qK7gCIjUjU0OwdmwghckC8RMqiAQIxv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDF4mbF6RlLyoOgBgAircA%2FITKtBJ%2BVZYMvIOtbg3U4fiVnsGDFNnNanaiwymh4hZR7q6MVxswyuUcTpCesd1qJAUa0jSDvcLJghkG9qrm0pneZ5jhZh9Zb0lH8Gs76%2FU5qetH4FKEVVQcdvIih8QjyU%2FFQp6R4sCd0Pq7Yr88Q2LIPiZGtcBH5jZzBXh3JP5LYdLlHOPEQjLLvIS8Q2UtfYuiz%2F2snrjc%2FEJv%2BgIUUChjRboZmZil0A1rb%2FZilVn%2FpLg50vNP8sYluF9gfec%2FYFsGCN%2BGuARGMwh6PTrT9qcU%2FWfjqIvvaijWfQ7vDOxykGk8sxGeNbLxZMzBpcSxM9ve%2F8fEE%2FqDTUztr6S4Dq5XuzycS6l2Uedh8Vhr1rBKG8jSOv1xbZr1WLpD2I7IOmFt7zCM43bHxbfnuoFSifLgT3OG88QJZf7BHYyxn2o2nRSbBiheIgPb5KRQy9fkIPzM6b1vbIIzDJwGjv38oYraHdBN7jhHc7GxuZ7OSR%2BtQt3JSaeKxihHSMg7qoNWonFo3WoqwS2oh0rBYVNomJO1K9dhqJbq7FcWtHTePPxK6R5bwI19nhdKhhrk6GEuYfMwDnOhf7n7d%2BQnDnz5klTk%2BTKqfObmXg8boZJFcpwAKecKi8WFO%2FvW3l7MLS3%2F9IGOqUBgZFPXZAc3MkhWtZnkpEV8nps206Kgbh05be%2FubDcv1gikBq7bRFmojGrXydNUOWM9NZFmSKVrat2M74BCqbeTIxKqCQbO2TV6ARBT1oQA2YAEAyrG03n4QqQe1LLkNmks3MATwc2i6C2dBRXBuprGePLZXFFLT7O5FTjtTMjcSOglAeTzgEWGCpIXP7H97t2%2F0s8Ue%2FGI114BDFxM5qfXoKigim5&X-Amz-Signature=8c2e07d769a9333af7d2adab1e6d5ef61264c8e33ffc57738bb93745c45e4129&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

```markdown
# 使用 Dockerfile 基于 centos7 构建 jdk8 的基础镜像

# 创建一个目录 mkdir -p /usr/local/software/dockerjdk8

# 制作Dockerfile      vim Dockerfile (必须交这个名字)
#-------------------------------------------------------真实文件去掉注释吧-----------
# 指定镜像，如果不存在则会自动下载
FROM centos:7  
# 指定创建人
MAINTAINER guojun 
# 设置当前目录
WORkDIR /usr   
# 创建一个目录    
RUN mkdir /usr/local/java 
# 添加文件到指定目录，并会自动的解压
ADD jdk-8u351-linux-aarch64.tar.gz /usr/local/java/ 


# 设置环境变量-jdk解压后的名称是jdk1.8.0_351,设置这些环境变量就是为了在任何环境下都可以执行jdk的相关命令
ENV JAVA_HOME=/usr/local/java/jdk1.8.0_351 
ENV JRE_HOME=$JAVA_HOME/jre
ENV CLASSPATH $JAVA_HOME/bin/dt.jar:$JAVA_HOME/lib/tools.jar:$JRE_HOME/lib:$CLASSPATH
ENV PATH $JAVA_HOME/bin:$PATH
#------------------------------------------------------------------

使用docker命令开始构建 Dockerfile 文件
# docker build -t='jdk1.8' .
# build: 构建 
# -t : 指定名称 起名根据自己的情况 这里我们是制作 基于centos7的jdk1.8镜像
# 空格 + 点：   空格后的 . （点）代表当前目录 
```

[image](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/7af9e8bc-72a2-409a-a46c-62575d00b229/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UW3NL7VX%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T234348Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIEmto5bKXUaoT1AJ9rac8SNKzSJA8rdClcu8dWMSkYFnAiEA08sHuYqhouzv7Q43xp5qK7gCIjUjU0OwdmwghckC8RMqiAQIxv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDF4mbF6RlLyoOgBgAircA%2FITKtBJ%2BVZYMvIOtbg3U4fiVnsGDFNnNanaiwymh4hZR7q6MVxswyuUcTpCesd1qJAUa0jSDvcLJghkG9qrm0pneZ5jhZh9Zb0lH8Gs76%2FU5qetH4FKEVVQcdvIih8QjyU%2FFQp6R4sCd0Pq7Yr88Q2LIPiZGtcBH5jZzBXh3JP5LYdLlHOPEQjLLvIS8Q2UtfYuiz%2F2snrjc%2FEJv%2BgIUUChjRboZmZil0A1rb%2FZilVn%2FpLg50vNP8sYluF9gfec%2FYFsGCN%2BGuARGMwh6PTrT9qcU%2FWfjqIvvaijWfQ7vDOxykGk8sxGeNbLxZMzBpcSxM9ve%2F8fEE%2FqDTUztr6S4Dq5XuzycS6l2Uedh8Vhr1rBKG8jSOv1xbZr1WLpD2I7IOmFt7zCM43bHxbfnuoFSifLgT3OG88QJZf7BHYyxn2o2nRSbBiheIgPb5KRQy9fkIPzM6b1vbIIzDJwGjv38oYraHdBN7jhHc7GxuZ7OSR%2BtQt3JSaeKxihHSMg7qoNWonFo3WoqwS2oh0rBYVNomJO1K9dhqJbq7FcWtHTePPxK6R5bwI19nhdKhhrk6GEuYfMwDnOhf7n7d%2BQnDnz5klTk%2BTKqfObmXg8boZJFcpwAKecKi8WFO%2FvW3l7MLS3%2F9IGOqUBgZFPXZAc3MkhWtZnkpEV8nps206Kgbh05be%2FubDcv1gikBq7bRFmojGrXydNUOWM9NZFmSKVrat2M74BCqbeTIxKqCQbO2TV6ARBT1oQA2YAEAyrG03n4QqQe1LLkNmks3MATwc2i6C2dBRXBuprGePLZXFFLT7O5FTjtTMjcSOglAeTzgEWGCpIXP7H97t2%2F0s8Ue%2FGI114BDFxM5qfXoKigim5&X-Amz-Signature=8a16d85c5b272e4ea5f3815371bab828f2bc9b1b69b0cf1fc8c0d2b08ea08e81&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

```markdown
# 使用Dockerfile文件，基于centos7构建的jdk1.8的镜像，9步完成
```

[image](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/a0678982-2bef-45a0-a065-c058f02ea9da/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UW3NL7VX%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T234348Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIEmto5bKXUaoT1AJ9rac8SNKzSJA8rdClcu8dWMSkYFnAiEA08sHuYqhouzv7Q43xp5qK7gCIjUjU0OwdmwghckC8RMqiAQIxv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDF4mbF6RlLyoOgBgAircA%2FITKtBJ%2BVZYMvIOtbg3U4fiVnsGDFNnNanaiwymh4hZR7q6MVxswyuUcTpCesd1qJAUa0jSDvcLJghkG9qrm0pneZ5jhZh9Zb0lH8Gs76%2FU5qetH4FKEVVQcdvIih8QjyU%2FFQp6R4sCd0Pq7Yr88Q2LIPiZGtcBH5jZzBXh3JP5LYdLlHOPEQjLLvIS8Q2UtfYuiz%2F2snrjc%2FEJv%2BgIUUChjRboZmZil0A1rb%2FZilVn%2FpLg50vNP8sYluF9gfec%2FYFsGCN%2BGuARGMwh6PTrT9qcU%2FWfjqIvvaijWfQ7vDOxykGk8sxGeNbLxZMzBpcSxM9ve%2F8fEE%2FqDTUztr6S4Dq5XuzycS6l2Uedh8Vhr1rBKG8jSOv1xbZr1WLpD2I7IOmFt7zCM43bHxbfnuoFSifLgT3OG88QJZf7BHYyxn2o2nRSbBiheIgPb5KRQy9fkIPzM6b1vbIIzDJwGjv38oYraHdBN7jhHc7GxuZ7OSR%2BtQt3JSaeKxihHSMg7qoNWonFo3WoqwS2oh0rBYVNomJO1K9dhqJbq7FcWtHTePPxK6R5bwI19nhdKhhrk6GEuYfMwDnOhf7n7d%2BQnDnz5klTk%2BTKqfObmXg8boZJFcpwAKecKi8WFO%2FvW3l7MLS3%2F9IGOqUBgZFPXZAc3MkhWtZnkpEV8nps206Kgbh05be%2FubDcv1gikBq7bRFmojGrXydNUOWM9NZFmSKVrat2M74BCqbeTIxKqCQbO2TV6ARBT1oQA2YAEAyrG03n4QqQe1LLkNmks3MATwc2i6C2dBRXBuprGePLZXFFLT7O5FTjtTMjcSOglAeTzgEWGCpIXP7H97t2%2F0s8Ue%2FGI114BDFxM5qfXoKigim5&X-Amz-Signature=ff94f7df356fad6a7f39b068d06627358568a42a4f635fe3d1f31273c7c6700d&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)


[image](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/b61d8962-7288-4730-9455-68d38bf4c9ca/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UW3NL7VX%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T234348Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIEmto5bKXUaoT1AJ9rac8SNKzSJA8rdClcu8dWMSkYFnAiEA08sHuYqhouzv7Q43xp5qK7gCIjUjU0OwdmwghckC8RMqiAQIxv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDF4mbF6RlLyoOgBgAircA%2FITKtBJ%2BVZYMvIOtbg3U4fiVnsGDFNnNanaiwymh4hZR7q6MVxswyuUcTpCesd1qJAUa0jSDvcLJghkG9qrm0pneZ5jhZh9Zb0lH8Gs76%2FU5qetH4FKEVVQcdvIih8QjyU%2FFQp6R4sCd0Pq7Yr88Q2LIPiZGtcBH5jZzBXh3JP5LYdLlHOPEQjLLvIS8Q2UtfYuiz%2F2snrjc%2FEJv%2BgIUUChjRboZmZil0A1rb%2FZilVn%2FpLg50vNP8sYluF9gfec%2FYFsGCN%2BGuARGMwh6PTrT9qcU%2FWfjqIvvaijWfQ7vDOxykGk8sxGeNbLxZMzBpcSxM9ve%2F8fEE%2FqDTUztr6S4Dq5XuzycS6l2Uedh8Vhr1rBKG8jSOv1xbZr1WLpD2I7IOmFt7zCM43bHxbfnuoFSifLgT3OG88QJZf7BHYyxn2o2nRSbBiheIgPb5KRQy9fkIPzM6b1vbIIzDJwGjv38oYraHdBN7jhHc7GxuZ7OSR%2BtQt3JSaeKxihHSMg7qoNWonFo3WoqwS2oh0rBYVNomJO1K9dhqJbq7FcWtHTePPxK6R5bwI19nhdKhhrk6GEuYfMwDnOhf7n7d%2BQnDnz5klTk%2BTKqfObmXg8boZJFcpwAKecKi8WFO%2FvW3l7MLS3%2F9IGOqUBgZFPXZAc3MkhWtZnkpEV8nps206Kgbh05be%2FubDcv1gikBq7bRFmojGrXydNUOWM9NZFmSKVrat2M74BCqbeTIxKqCQbO2TV6ARBT1oQA2YAEAyrG03n4QqQe1LLkNmks3MATwc2i6C2dBRXBuprGePLZXFFLT7O5FTjtTMjcSOglAeTzgEWGCpIXP7H97t2%2F0s8Ue%2FGI114BDFxM5qfXoKigim5&X-Amz-Signature=e3b76a3a5cf9145c9c26bb6abae353c21c5537c65c60fe9776e56923a29298d7&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

[image](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/9cd3c627-90c1-48ba-a255-0aafedac1ed5/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UW3NL7VX%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T234348Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIEmto5bKXUaoT1AJ9rac8SNKzSJA8rdClcu8dWMSkYFnAiEA08sHuYqhouzv7Q43xp5qK7gCIjUjU0OwdmwghckC8RMqiAQIxv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDF4mbF6RlLyoOgBgAircA%2FITKtBJ%2BVZYMvIOtbg3U4fiVnsGDFNnNanaiwymh4hZR7q6MVxswyuUcTpCesd1qJAUa0jSDvcLJghkG9qrm0pneZ5jhZh9Zb0lH8Gs76%2FU5qetH4FKEVVQcdvIih8QjyU%2FFQp6R4sCd0Pq7Yr88Q2LIPiZGtcBH5jZzBXh3JP5LYdLlHOPEQjLLvIS8Q2UtfYuiz%2F2snrjc%2FEJv%2BgIUUChjRboZmZil0A1rb%2FZilVn%2FpLg50vNP8sYluF9gfec%2FYFsGCN%2BGuARGMwh6PTrT9qcU%2FWfjqIvvaijWfQ7vDOxykGk8sxGeNbLxZMzBpcSxM9ve%2F8fEE%2FqDTUztr6S4Dq5XuzycS6l2Uedh8Vhr1rBKG8jSOv1xbZr1WLpD2I7IOmFt7zCM43bHxbfnuoFSifLgT3OG88QJZf7BHYyxn2o2nRSbBiheIgPb5KRQy9fkIPzM6b1vbIIzDJwGjv38oYraHdBN7jhHc7GxuZ7OSR%2BtQt3JSaeKxihHSMg7qoNWonFo3WoqwS2oh0rBYVNomJO1K9dhqJbq7FcWtHTePPxK6R5bwI19nhdKhhrk6GEuYfMwDnOhf7n7d%2BQnDnz5klTk%2BTKqfObmXg8boZJFcpwAKecKi8WFO%2FvW3l7MLS3%2F9IGOqUBgZFPXZAc3MkhWtZnkpEV8nps206Kgbh05be%2FubDcv1gikBq7bRFmojGrXydNUOWM9NZFmSKVrat2M74BCqbeTIxKqCQbO2TV6ARBT1oQA2YAEAyrG03n4QqQe1LLkNmks3MATwc2i6C2dBRXBuprGePLZXFFLT7O5FTjtTMjcSOglAeTzgEWGCpIXP7H97t2%2F0s8Ue%2FGI114BDFxM5qfXoKigim5&X-Amz-Signature=87a9dbf1580f4b0011aa96016eb9f87040311f2afda996011d4dde283ad00028&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

```markdown
# 拉取私有镜像 registry
# 222 部署foodie-dev的使用私服
docker run -di --restart=unless-stoped --restart=always --name=222_Avery_Registry -p 5000:5000 registry

# 231 用户部署需要的jdk1.8（centos7）容器的私服
docker run -di --restart=unless-stoped --restart=always --name=231_Avery_Registry -p 5000:5000 registry

```

[image](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/7fb99d1e-638f-4e0c-8fc5-4ca8f373cb93/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UW3NL7VX%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T234348Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIEmto5bKXUaoT1AJ9rac8SNKzSJA8rdClcu8dWMSkYFnAiEA08sHuYqhouzv7Q43xp5qK7gCIjUjU0OwdmwghckC8RMqiAQIxv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDF4mbF6RlLyoOgBgAircA%2FITKtBJ%2BVZYMvIOtbg3U4fiVnsGDFNnNanaiwymh4hZR7q6MVxswyuUcTpCesd1qJAUa0jSDvcLJghkG9qrm0pneZ5jhZh9Zb0lH8Gs76%2FU5qetH4FKEVVQcdvIih8QjyU%2FFQp6R4sCd0Pq7Yr88Q2LIPiZGtcBH5jZzBXh3JP5LYdLlHOPEQjLLvIS8Q2UtfYuiz%2F2snrjc%2FEJv%2BgIUUChjRboZmZil0A1rb%2FZilVn%2FpLg50vNP8sYluF9gfec%2FYFsGCN%2BGuARGMwh6PTrT9qcU%2FWfjqIvvaijWfQ7vDOxykGk8sxGeNbLxZMzBpcSxM9ve%2F8fEE%2FqDTUztr6S4Dq5XuzycS6l2Uedh8Vhr1rBKG8jSOv1xbZr1WLpD2I7IOmFt7zCM43bHxbfnuoFSifLgT3OG88QJZf7BHYyxn2o2nRSbBiheIgPb5KRQy9fkIPzM6b1vbIIzDJwGjv38oYraHdBN7jhHc7GxuZ7OSR%2BtQt3JSaeKxihHSMg7qoNWonFo3WoqwS2oh0rBYVNomJO1K9dhqJbq7FcWtHTePPxK6R5bwI19nhdKhhrk6GEuYfMwDnOhf7n7d%2BQnDnz5klTk%2BTKqfObmXg8boZJFcpwAKecKi8WFO%2FvW3l7MLS3%2F9IGOqUBgZFPXZAc3MkhWtZnkpEV8nps206Kgbh05be%2FubDcv1gikBq7bRFmojGrXydNUOWM9NZFmSKVrat2M74BCqbeTIxKqCQbO2TV6ARBT1oQA2YAEAyrG03n4QqQe1LLkNmks3MATwc2i6C2dBRXBuprGePLZXFFLT7O5FTjtTMjcSOglAeTzgEWGCpIXP7H97t2%2F0s8Ue%2FGI114BDFxM5qfXoKigim5&X-Amz-Signature=51a3cba2b2b3f80c479a5900dd47077184f4833046e94c173cfd1eb57a6e7732&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

```markdown
# 访问 http://172.16.136.100:5000/v2/_catalog，创建成功
# 出现内容： json输出： {"repositories":[]} 私有仓库成功
# 但是json内容是空的 -->[] : 因为我们没有上传我们的镜像，所以是空的
```

[image](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/ce4a6acf-9dfa-4cbb-ba45-05618976b528/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UW3NL7VX%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T234348Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIEmto5bKXUaoT1AJ9rac8SNKzSJA8rdClcu8dWMSkYFnAiEA08sHuYqhouzv7Q43xp5qK7gCIjUjU0OwdmwghckC8RMqiAQIxv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDF4mbF6RlLyoOgBgAircA%2FITKtBJ%2BVZYMvIOtbg3U4fiVnsGDFNnNanaiwymh4hZR7q6MVxswyuUcTpCesd1qJAUa0jSDvcLJghkG9qrm0pneZ5jhZh9Zb0lH8Gs76%2FU5qetH4FKEVVQcdvIih8QjyU%2FFQp6R4sCd0Pq7Yr88Q2LIPiZGtcBH5jZzBXh3JP5LYdLlHOPEQjLLvIS8Q2UtfYuiz%2F2snrjc%2FEJv%2BgIUUChjRboZmZil0A1rb%2FZilVn%2FpLg50vNP8sYluF9gfec%2FYFsGCN%2BGuARGMwh6PTrT9qcU%2FWfjqIvvaijWfQ7vDOxykGk8sxGeNbLxZMzBpcSxM9ve%2F8fEE%2FqDTUztr6S4Dq5XuzycS6l2Uedh8Vhr1rBKG8jSOv1xbZr1WLpD2I7IOmFt7zCM43bHxbfnuoFSifLgT3OG88QJZf7BHYyxn2o2nRSbBiheIgPb5KRQy9fkIPzM6b1vbIIzDJwGjv38oYraHdBN7jhHc7GxuZ7OSR%2BtQt3JSaeKxihHSMg7qoNWonFo3WoqwS2oh0rBYVNomJO1K9dhqJbq7FcWtHTePPxK6R5bwI19nhdKhhrk6GEuYfMwDnOhf7n7d%2BQnDnz5klTk%2BTKqfObmXg8boZJFcpwAKecKi8WFO%2FvW3l7MLS3%2F9IGOqUBgZFPXZAc3MkhWtZnkpEV8nps206Kgbh05be%2FubDcv1gikBq7bRFmojGrXydNUOWM9NZFmSKVrat2M74BCqbeTIxKqCQbO2TV6ARBT1oQA2YAEAyrG03n4QqQe1LLkNmks3MATwc2i6C2dBRXBuprGePLZXFFLT7O5FTjtTMjcSOglAeTzgEWGCpIXP7H97t2%2F0s8Ue%2FGI114BDFxM5qfXoKigim5&X-Amz-Signature=8e8a18ffd79e0b1e862246dcf4d491c3ce4aad20adc877cbd51cfcf169af4b86&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

```markdown
# 配置： 通过配置让 Docker 信任这个私有仓库地址，才可以把本地镜像文件上传到 Docker 私有仓库
配置文件所在目录
# vi /etc/docker/daemon.json
如果没有文件和目录需要自己创建 /etc/docker/daemon.json
写入内容：
#------------------------------------------------
{

 "registry-mirrors":["https://docker.mirrors.ustc.edu.cn"]

}

{
  "registry-mirrors": ["https://<my-docker-mirror-host>"]
 }
#---------------------------------------------------

# 下面的展示写错了少了些https写成了http    mirrors写成了mirror
```

[image](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/2c549363-8f13-4dd6-939e-ff8a2373965c/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UW3NL7VX%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T234348Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIEmto5bKXUaoT1AJ9rac8SNKzSJA8rdClcu8dWMSkYFnAiEA08sHuYqhouzv7Q43xp5qK7gCIjUjU0OwdmwghckC8RMqiAQIxv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDF4mbF6RlLyoOgBgAircA%2FITKtBJ%2BVZYMvIOtbg3U4fiVnsGDFNnNanaiwymh4hZR7q6MVxswyuUcTpCesd1qJAUa0jSDvcLJghkG9qrm0pneZ5jhZh9Zb0lH8Gs76%2FU5qetH4FKEVVQcdvIih8QjyU%2FFQp6R4sCd0Pq7Yr88Q2LIPiZGtcBH5jZzBXh3JP5LYdLlHOPEQjLLvIS8Q2UtfYuiz%2F2snrjc%2FEJv%2BgIUUChjRboZmZil0A1rb%2FZilVn%2FpLg50vNP8sYluF9gfec%2FYFsGCN%2BGuARGMwh6PTrT9qcU%2FWfjqIvvaijWfQ7vDOxykGk8sxGeNbLxZMzBpcSxM9ve%2F8fEE%2FqDTUztr6S4Dq5XuzycS6l2Uedh8Vhr1rBKG8jSOv1xbZr1WLpD2I7IOmFt7zCM43bHxbfnuoFSifLgT3OG88QJZf7BHYyxn2o2nRSbBiheIgPb5KRQy9fkIPzM6b1vbIIzDJwGjv38oYraHdBN7jhHc7GxuZ7OSR%2BtQt3JSaeKxihHSMg7qoNWonFo3WoqwS2oh0rBYVNomJO1K9dhqJbq7FcWtHTePPxK6R5bwI19nhdKhhrk6GEuYfMwDnOhf7n7d%2BQnDnz5klTk%2BTKqfObmXg8boZJFcpwAKecKi8WFO%2FvW3l7MLS3%2F9IGOqUBgZFPXZAc3MkhWtZnkpEV8nps206Kgbh05be%2FubDcv1gikBq7bRFmojGrXydNUOWM9NZFmSKVrat2M74BCqbeTIxKqCQbO2TV6ARBT1oQA2YAEAyrG03n4QqQe1LLkNmks3MATwc2i6C2dBRXBuprGePLZXFFLT7O5FTjtTMjcSOglAeTzgEWGCpIXP7H97t2%2F0s8Ue%2FGI114BDFxM5qfXoKigim5&X-Amz-Signature=58365ef5299ba1ceb5875cccd2db727f42f2d67d587669e9a5b2dd6fc345fff4&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

```markdown
# 添加私有仓库配置: 表示docker信任该私有仓库

"insecure-registries":["172.16.136.100:5000"] 和其他内容够好隔开
```

```markdown
# 然后重启docker服务
# systemctl restart docker



# 重启后给 镜像打上标签和加镜像的IP地址和名称
# docker tag jdk1.8 172.16.136.100:5000/jdk1.8  【jdk镜像和新的私服上的jdk镜像一样的id】
```

[image](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/341629b9-e6b2-4853-81ae-95a8c63515f3/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UW3NL7VX%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T234348Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIEmto5bKXUaoT1AJ9rac8SNKzSJA8rdClcu8dWMSkYFnAiEA08sHuYqhouzv7Q43xp5qK7gCIjUjU0OwdmwghckC8RMqiAQIxv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDF4mbF6RlLyoOgBgAircA%2FITKtBJ%2BVZYMvIOtbg3U4fiVnsGDFNnNanaiwymh4hZR7q6MVxswyuUcTpCesd1qJAUa0jSDvcLJghkG9qrm0pneZ5jhZh9Zb0lH8Gs76%2FU5qetH4FKEVVQcdvIih8QjyU%2FFQp6R4sCd0Pq7Yr88Q2LIPiZGtcBH5jZzBXh3JP5LYdLlHOPEQjLLvIS8Q2UtfYuiz%2F2snrjc%2FEJv%2BgIUUChjRboZmZil0A1rb%2FZilVn%2FpLg50vNP8sYluF9gfec%2FYFsGCN%2BGuARGMwh6PTrT9qcU%2FWfjqIvvaijWfQ7vDOxykGk8sxGeNbLxZMzBpcSxM9ve%2F8fEE%2FqDTUztr6S4Dq5XuzycS6l2Uedh8Vhr1rBKG8jSOv1xbZr1WLpD2I7IOmFt7zCM43bHxbfnuoFSifLgT3OG88QJZf7BHYyxn2o2nRSbBiheIgPb5KRQy9fkIPzM6b1vbIIzDJwGjv38oYraHdBN7jhHc7GxuZ7OSR%2BtQt3JSaeKxihHSMg7qoNWonFo3WoqwS2oh0rBYVNomJO1K9dhqJbq7FcWtHTePPxK6R5bwI19nhdKhhrk6GEuYfMwDnOhf7n7d%2BQnDnz5klTk%2BTKqfObmXg8boZJFcpwAKecKi8WFO%2FvW3l7MLS3%2F9IGOqUBgZFPXZAc3MkhWtZnkpEV8nps206Kgbh05be%2FubDcv1gikBq7bRFmojGrXydNUOWM9NZFmSKVrat2M74BCqbeTIxKqCQbO2TV6ARBT1oQA2YAEAyrG03n4QqQe1LLkNmks3MATwc2i6C2dBRXBuprGePLZXFFLT7O5FTjtTMjcSOglAeTzgEWGCpIXP7H97t2%2F0s8Ue%2FGI114BDFxM5qfXoKigim5&X-Amz-Signature=6458860627374da2e5015637ece2c3788f644ddea418fccdcf593e3959824d59&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

> 💡 重新启动私服镜像容器就可以访问了
> 💡 docker start registry ⇒ docker push 172.16.136.100:5000/jdk1.8    然后报错了
```markdown
# 将镜像push到私服上
# docker push 172.16.136.100:5000/jdk1.8，    然后报错了

#报错
#The push refers to a repository [192.168.1.161:5000/hello-world]
Get https://192.168.1.161:5000/v1/_ping: http: server gave HTTP response to HTTPS client
#原因
#docker私有仓库服务器，默认是基于https传输的，所以我们需要在客户端127.0.0.1做相关设置，不使用https传输
解决步骤
vi /etc/docker/daemon.json
将下面的代码放进去保存并退出。
#"insecure-registries":["127.0.0.1:5000"]
最终如下所示：
{
    "registry-mirrors": ["https://njrds9qc.mirror.aliyuncs.com"],
    "insecure-registries":["127.0.0.1:5000"]
}
依次执行下面两条命令，重新启动docker：
# systemctl daemon-reload
# systemctl restart docker


备注：daemon.json 此文件没有的话，可以新增此文件！！
但是如果此文件内容错误的话，可能docker 启动不了。切记！！
```

[image](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/01c18c54-9b32-4b48-8895-7970eb3e49ad/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UW3NL7VX%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T234348Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIEmto5bKXUaoT1AJ9rac8SNKzSJA8rdClcu8dWMSkYFnAiEA08sHuYqhouzv7Q43xp5qK7gCIjUjU0OwdmwghckC8RMqiAQIxv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDF4mbF6RlLyoOgBgAircA%2FITKtBJ%2BVZYMvIOtbg3U4fiVnsGDFNnNanaiwymh4hZR7q6MVxswyuUcTpCesd1qJAUa0jSDvcLJghkG9qrm0pneZ5jhZh9Zb0lH8Gs76%2FU5qetH4FKEVVQcdvIih8QjyU%2FFQp6R4sCd0Pq7Yr88Q2LIPiZGtcBH5jZzBXh3JP5LYdLlHOPEQjLLvIS8Q2UtfYuiz%2F2snrjc%2FEJv%2BgIUUChjRboZmZil0A1rb%2FZilVn%2FpLg50vNP8sYluF9gfec%2FYFsGCN%2BGuARGMwh6PTrT9qcU%2FWfjqIvvaijWfQ7vDOxykGk8sxGeNbLxZMzBpcSxM9ve%2F8fEE%2FqDTUztr6S4Dq5XuzycS6l2Uedh8Vhr1rBKG8jSOv1xbZr1WLpD2I7IOmFt7zCM43bHxbfnuoFSifLgT3OG88QJZf7BHYyxn2o2nRSbBiheIgPb5KRQy9fkIPzM6b1vbIIzDJwGjv38oYraHdBN7jhHc7GxuZ7OSR%2BtQt3JSaeKxihHSMg7qoNWonFo3WoqwS2oh0rBYVNomJO1K9dhqJbq7FcWtHTePPxK6R5bwI19nhdKhhrk6GEuYfMwDnOhf7n7d%2BQnDnz5klTk%2BTKqfObmXg8boZJFcpwAKecKi8WFO%2FvW3l7MLS3%2F9IGOqUBgZFPXZAc3MkhWtZnkpEV8nps206Kgbh05be%2FubDcv1gikBq7bRFmojGrXydNUOWM9NZFmSKVrat2M74BCqbeTIxKqCQbO2TV6ARBT1oQA2YAEAyrG03n4QqQe1LLkNmks3MATwc2i6C2dBRXBuprGePLZXFFLT7O5FTjtTMjcSOglAeTzgEWGCpIXP7H97t2%2F0s8Ue%2FGI114BDFxM5qfXoKigim5&X-Amz-Signature=5f533186a819b78fcebec833026018efb35ecce7aeedc9397e66f6f741fb46bc&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

```markdown
# 修改错误 重新上传 成功（http -> https, mirror -> mirrors）

docker push + 镜像
```

[image](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/8d9e2c12-238f-4a23-9444-18cee0aaea47/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UW3NL7VX%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T234348Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIEmto5bKXUaoT1AJ9rac8SNKzSJA8rdClcu8dWMSkYFnAiEA08sHuYqhouzv7Q43xp5qK7gCIjUjU0OwdmwghckC8RMqiAQIxv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDF4mbF6RlLyoOgBgAircA%2FITKtBJ%2BVZYMvIOtbg3U4fiVnsGDFNnNanaiwymh4hZR7q6MVxswyuUcTpCesd1qJAUa0jSDvcLJghkG9qrm0pneZ5jhZh9Zb0lH8Gs76%2FU5qetH4FKEVVQcdvIih8QjyU%2FFQp6R4sCd0Pq7Yr88Q2LIPiZGtcBH5jZzBXh3JP5LYdLlHOPEQjLLvIS8Q2UtfYuiz%2F2snrjc%2FEJv%2BgIUUChjRboZmZil0A1rb%2FZilVn%2FpLg50vNP8sYluF9gfec%2FYFsGCN%2BGuARGMwh6PTrT9qcU%2FWfjqIvvaijWfQ7vDOxykGk8sxGeNbLxZMzBpcSxM9ve%2F8fEE%2FqDTUztr6S4Dq5XuzycS6l2Uedh8Vhr1rBKG8jSOv1xbZr1WLpD2I7IOmFt7zCM43bHxbfnuoFSifLgT3OG88QJZf7BHYyxn2o2nRSbBiheIgPb5KRQy9fkIPzM6b1vbIIzDJwGjv38oYraHdBN7jhHc7GxuZ7OSR%2BtQt3JSaeKxihHSMg7qoNWonFo3WoqwS2oh0rBYVNomJO1K9dhqJbq7FcWtHTePPxK6R5bwI19nhdKhhrk6GEuYfMwDnOhf7n7d%2BQnDnz5klTk%2BTKqfObmXg8boZJFcpwAKecKi8WFO%2FvW3l7MLS3%2F9IGOqUBgZFPXZAc3MkhWtZnkpEV8nps206Kgbh05be%2FubDcv1gikBq7bRFmojGrXydNUOWM9NZFmSKVrat2M74BCqbeTIxKqCQbO2TV6ARBT1oQA2YAEAyrG03n4QqQe1LLkNmks3MATwc2i6C2dBRXBuprGePLZXFFLT7O5FTjtTMjcSOglAeTzgEWGCpIXP7H97t2%2F0s8Ue%2FGI114BDFxM5qfXoKigim5&X-Amz-Signature=e146cf93efb8d3760f94cedd42d6ba09a20ec49f66a217c2936ff068a30df735&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)




总结：

```markdown
镜像： 可以看成一个模板
容器： 可以看成是根据这个模板锁创建的容器
#可以在本机下载或者构建很多的容器，比如centos， jdk， 开发的运用程序，mysql， tomcat等等
#都可以创建成容器，这些容器可以启动，  可以把每一个容器看成是一个服务器，容器之间环境是隔离的
#可以使用容器来搭建生产环境，它的安全性是十分高的
```

[image](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/8c2739e9-e661-4c1b-8f97-68cfde1bb4cf/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UW3NL7VX%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T234348Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIEmto5bKXUaoT1AJ9rac8SNKzSJA8rdClcu8dWMSkYFnAiEA08sHuYqhouzv7Q43xp5qK7gCIjUjU0OwdmwghckC8RMqiAQIxv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDF4mbF6RlLyoOgBgAircA%2FITKtBJ%2BVZYMvIOtbg3U4fiVnsGDFNnNanaiwymh4hZR7q6MVxswyuUcTpCesd1qJAUa0jSDvcLJghkG9qrm0pneZ5jhZh9Zb0lH8Gs76%2FU5qetH4FKEVVQcdvIih8QjyU%2FFQp6R4sCd0Pq7Yr88Q2LIPiZGtcBH5jZzBXh3JP5LYdLlHOPEQjLLvIS8Q2UtfYuiz%2F2snrjc%2FEJv%2BgIUUChjRboZmZil0A1rb%2FZilVn%2FpLg50vNP8sYluF9gfec%2FYFsGCN%2BGuARGMwh6PTrT9qcU%2FWfjqIvvaijWfQ7vDOxykGk8sxGeNbLxZMzBpcSxM9ve%2F8fEE%2FqDTUztr6S4Dq5XuzycS6l2Uedh8Vhr1rBKG8jSOv1xbZr1WLpD2I7IOmFt7zCM43bHxbfnuoFSifLgT3OG88QJZf7BHYyxn2o2nRSbBiheIgPb5KRQy9fkIPzM6b1vbIIzDJwGjv38oYraHdBN7jhHc7GxuZ7OSR%2BtQt3JSaeKxihHSMg7qoNWonFo3WoqwS2oh0rBYVNomJO1K9dhqJbq7FcWtHTePPxK6R5bwI19nhdKhhrk6GEuYfMwDnOhf7n7d%2BQnDnz5klTk%2BTKqfObmXg8boZJFcpwAKecKi8WFO%2FvW3l7MLS3%2F9IGOqUBgZFPXZAc3MkhWtZnkpEV8nps206Kgbh05be%2FubDcv1gikBq7bRFmojGrXydNUOWM9NZFmSKVrat2M74BCqbeTIxKqCQbO2TV6ARBT1oQA2YAEAyrG03n4QqQe1LLkNmks3MATwc2i6C2dBRXBuprGePLZXFFLT7O5FTjtTMjcSOglAeTzgEWGCpIXP7H97t2%2F0s8Ue%2FGI114BDFxM5qfXoKigim5&X-Amz-Signature=74b6d9b43dee7a9b515db5a3ae0145f99db06921a1263df331ed12f7551ea7eb&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

[image](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/b6ade4e9-e2a5-465f-a89f-651264dc76b3/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UW3NL7VX%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T234348Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIEmto5bKXUaoT1AJ9rac8SNKzSJA8rdClcu8dWMSkYFnAiEA08sHuYqhouzv7Q43xp5qK7gCIjUjU0OwdmwghckC8RMqiAQIxv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDF4mbF6RlLyoOgBgAircA%2FITKtBJ%2BVZYMvIOtbg3U4fiVnsGDFNnNanaiwymh4hZR7q6MVxswyuUcTpCesd1qJAUa0jSDvcLJghkG9qrm0pneZ5jhZh9Zb0lH8Gs76%2FU5qetH4FKEVVQcdvIih8QjyU%2FFQp6R4sCd0Pq7Yr88Q2LIPiZGtcBH5jZzBXh3JP5LYdLlHOPEQjLLvIS8Q2UtfYuiz%2F2snrjc%2FEJv%2BgIUUChjRboZmZil0A1rb%2FZilVn%2FpLg50vNP8sYluF9gfec%2FYFsGCN%2BGuARGMwh6PTrT9qcU%2FWfjqIvvaijWfQ7vDOxykGk8sxGeNbLxZMzBpcSxM9ve%2F8fEE%2FqDTUztr6S4Dq5XuzycS6l2Uedh8Vhr1rBKG8jSOv1xbZr1WLpD2I7IOmFt7zCM43bHxbfnuoFSifLgT3OG88QJZf7BHYyxn2o2nRSbBiheIgPb5KRQy9fkIPzM6b1vbIIzDJwGjv38oYraHdBN7jhHc7GxuZ7OSR%2BtQt3JSaeKxihHSMg7qoNWonFo3WoqwS2oh0rBYVNomJO1K9dhqJbq7FcWtHTePPxK6R5bwI19nhdKhhrk6GEuYfMwDnOhf7n7d%2BQnDnz5klTk%2BTKqfObmXg8boZJFcpwAKecKi8WFO%2FvW3l7MLS3%2F9IGOqUBgZFPXZAc3MkhWtZnkpEV8nps206Kgbh05be%2FubDcv1gikBq7bRFmojGrXydNUOWM9NZFmSKVrat2M74BCqbeTIxKqCQbO2TV6ARBT1oQA2YAEAyrG03n4QqQe1LLkNmks3MATwc2i6C2dBRXBuprGePLZXFFLT7O5FTjtTMjcSOglAeTzgEWGCpIXP7H97t2%2F0s8Ue%2FGI114BDFxM5qfXoKigim5&X-Amz-Signature=fb50ea607dbcc54290aab46d139bb355a71fa07874a4bcc851ea98f02a7295aa&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

[image](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/8437c8bb-34d9-45ec-840c-24f4e8a5b83a/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UW3NL7VX%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T234348Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIEmto5bKXUaoT1AJ9rac8SNKzSJA8rdClcu8dWMSkYFnAiEA08sHuYqhouzv7Q43xp5qK7gCIjUjU0OwdmwghckC8RMqiAQIxv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDF4mbF6RlLyoOgBgAircA%2FITKtBJ%2BVZYMvIOtbg3U4fiVnsGDFNnNanaiwymh4hZR7q6MVxswyuUcTpCesd1qJAUa0jSDvcLJghkG9qrm0pneZ5jhZh9Zb0lH8Gs76%2FU5qetH4FKEVVQcdvIih8QjyU%2FFQp6R4sCd0Pq7Yr88Q2LIPiZGtcBH5jZzBXh3JP5LYdLlHOPEQjLLvIS8Q2UtfYuiz%2F2snrjc%2FEJv%2BgIUUChjRboZmZil0A1rb%2FZilVn%2FpLg50vNP8sYluF9gfec%2FYFsGCN%2BGuARGMwh6PTrT9qcU%2FWfjqIvvaijWfQ7vDOxykGk8sxGeNbLxZMzBpcSxM9ve%2F8fEE%2FqDTUztr6S4Dq5XuzycS6l2Uedh8Vhr1rBKG8jSOv1xbZr1WLpD2I7IOmFt7zCM43bHxbfnuoFSifLgT3OG88QJZf7BHYyxn2o2nRSbBiheIgPb5KRQy9fkIPzM6b1vbIIzDJwGjv38oYraHdBN7jhHc7GxuZ7OSR%2BtQt3JSaeKxihHSMg7qoNWonFo3WoqwS2oh0rBYVNomJO1K9dhqJbq7FcWtHTePPxK6R5bwI19nhdKhhrk6GEuYfMwDnOhf7n7d%2BQnDnz5klTk%2BTKqfObmXg8boZJFcpwAKecKi8WFO%2FvW3l7MLS3%2F9IGOqUBgZFPXZAc3MkhWtZnkpEV8nps206Kgbh05be%2FubDcv1gikBq7bRFmojGrXydNUOWM9NZFmSKVrat2M74BCqbeTIxKqCQbO2TV6ARBT1oQA2YAEAyrG03n4QqQe1LLkNmks3MATwc2i6C2dBRXBuprGePLZXFFLT7O5FTjtTMjcSOglAeTzgEWGCpIXP7H97t2%2F0s8Ue%2FGI114BDFxM5qfXoKigim5&X-Amz-Signature=922ff90cf54218b08861e9918b67b6150f12baa2091190cb3f2601c0d224c75a&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

[image](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/78fa9aac-564d-4e86-aded-2e202c2d2b60/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UW3NL7VX%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T234348Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIEmto5bKXUaoT1AJ9rac8SNKzSJA8rdClcu8dWMSkYFnAiEA08sHuYqhouzv7Q43xp5qK7gCIjUjU0OwdmwghckC8RMqiAQIxv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDF4mbF6RlLyoOgBgAircA%2FITKtBJ%2BVZYMvIOtbg3U4fiVnsGDFNnNanaiwymh4hZR7q6MVxswyuUcTpCesd1qJAUa0jSDvcLJghkG9qrm0pneZ5jhZh9Zb0lH8Gs76%2FU5qetH4FKEVVQcdvIih8QjyU%2FFQp6R4sCd0Pq7Yr88Q2LIPiZGtcBH5jZzBXh3JP5LYdLlHOPEQjLLvIS8Q2UtfYuiz%2F2snrjc%2FEJv%2BgIUUChjRboZmZil0A1rb%2FZilVn%2FpLg50vNP8sYluF9gfec%2FYFsGCN%2BGuARGMwh6PTrT9qcU%2FWfjqIvvaijWfQ7vDOxykGk8sxGeNbLxZMzBpcSxM9ve%2F8fEE%2FqDTUztr6S4Dq5XuzycS6l2Uedh8Vhr1rBKG8jSOv1xbZr1WLpD2I7IOmFt7zCM43bHxbfnuoFSifLgT3OG88QJZf7BHYyxn2o2nRSbBiheIgPb5KRQy9fkIPzM6b1vbIIzDJwGjv38oYraHdBN7jhHc7GxuZ7OSR%2BtQt3JSaeKxihHSMg7qoNWonFo3WoqwS2oh0rBYVNomJO1K9dhqJbq7FcWtHTePPxK6R5bwI19nhdKhhrk6GEuYfMwDnOhf7n7d%2BQnDnz5klTk%2BTKqfObmXg8boZJFcpwAKecKi8WFO%2FvW3l7MLS3%2F9IGOqUBgZFPXZAc3MkhWtZnkpEV8nps206Kgbh05be%2FubDcv1gikBq7bRFmojGrXydNUOWM9NZFmSKVrat2M74BCqbeTIxKqCQbO2TV6ARBT1oQA2YAEAyrG03n4QqQe1LLkNmks3MATwc2i6C2dBRXBuprGePLZXFFLT7O5FTjtTMjcSOglAeTzgEWGCpIXP7H97t2%2F0s8Ue%2FGI114BDFxM5qfXoKigim5&X-Amz-Signature=a55b60d96c4d18b35cdd51e8c3300063849f449e25b1042413e06601de373236&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

[image](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/c52266e4-5d8f-43fa-a4a9-358765e8ee01/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UW3NL7VX%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T234348Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIEmto5bKXUaoT1AJ9rac8SNKzSJA8rdClcu8dWMSkYFnAiEA08sHuYqhouzv7Q43xp5qK7gCIjUjU0OwdmwghckC8RMqiAQIxv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDF4mbF6RlLyoOgBgAircA%2FITKtBJ%2BVZYMvIOtbg3U4fiVnsGDFNnNanaiwymh4hZR7q6MVxswyuUcTpCesd1qJAUa0jSDvcLJghkG9qrm0pneZ5jhZh9Zb0lH8Gs76%2FU5qetH4FKEVVQcdvIih8QjyU%2FFQp6R4sCd0Pq7Yr88Q2LIPiZGtcBH5jZzBXh3JP5LYdLlHOPEQjLLvIS8Q2UtfYuiz%2F2snrjc%2FEJv%2BgIUUChjRboZmZil0A1rb%2FZilVn%2FpLg50vNP8sYluF9gfec%2FYFsGCN%2BGuARGMwh6PTrT9qcU%2FWfjqIvvaijWfQ7vDOxykGk8sxGeNbLxZMzBpcSxM9ve%2F8fEE%2FqDTUztr6S4Dq5XuzycS6l2Uedh8Vhr1rBKG8jSOv1xbZr1WLpD2I7IOmFt7zCM43bHxbfnuoFSifLgT3OG88QJZf7BHYyxn2o2nRSbBiheIgPb5KRQy9fkIPzM6b1vbIIzDJwGjv38oYraHdBN7jhHc7GxuZ7OSR%2BtQt3JSaeKxihHSMg7qoNWonFo3WoqwS2oh0rBYVNomJO1K9dhqJbq7FcWtHTePPxK6R5bwI19nhdKhhrk6GEuYfMwDnOhf7n7d%2BQnDnz5klTk%2BTKqfObmXg8boZJFcpwAKecKi8WFO%2FvW3l7MLS3%2F9IGOqUBgZFPXZAc3MkhWtZnkpEV8nps206Kgbh05be%2FubDcv1gikBq7bRFmojGrXydNUOWM9NZFmSKVrat2M74BCqbeTIxKqCQbO2TV6ARBT1oQA2YAEAyrG03n4QqQe1LLkNmks3MATwc2i6C2dBRXBuprGePLZXFFLT7O5FTjtTMjcSOglAeTzgEWGCpIXP7H97t2%2F0s8Ue%2FGI114BDFxM5qfXoKigim5&X-Amz-Signature=94620dbf2f701f999f37ec119e7cfb20975e7ffdbc4b93d237416a541dbb923a&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

[image](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/cc9b44f4-f1aa-45ba-8291-3cf304471f1a/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UW3NL7VX%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T234348Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIEmto5bKXUaoT1AJ9rac8SNKzSJA8rdClcu8dWMSkYFnAiEA08sHuYqhouzv7Q43xp5qK7gCIjUjU0OwdmwghckC8RMqiAQIxv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDF4mbF6RlLyoOgBgAircA%2FITKtBJ%2BVZYMvIOtbg3U4fiVnsGDFNnNanaiwymh4hZR7q6MVxswyuUcTpCesd1qJAUa0jSDvcLJghkG9qrm0pneZ5jhZh9Zb0lH8Gs76%2FU5qetH4FKEVVQcdvIih8QjyU%2FFQp6R4sCd0Pq7Yr88Q2LIPiZGtcBH5jZzBXh3JP5LYdLlHOPEQjLLvIS8Q2UtfYuiz%2F2snrjc%2FEJv%2BgIUUChjRboZmZil0A1rb%2FZilVn%2FpLg50vNP8sYluF9gfec%2FYFsGCN%2BGuARGMwh6PTrT9qcU%2FWfjqIvvaijWfQ7vDOxykGk8sxGeNbLxZMzBpcSxM9ve%2F8fEE%2FqDTUztr6S4Dq5XuzycS6l2Uedh8Vhr1rBKG8jSOv1xbZr1WLpD2I7IOmFt7zCM43bHxbfnuoFSifLgT3OG88QJZf7BHYyxn2o2nRSbBiheIgPb5KRQy9fkIPzM6b1vbIIzDJwGjv38oYraHdBN7jhHc7GxuZ7OSR%2BtQt3JSaeKxihHSMg7qoNWonFo3WoqwS2oh0rBYVNomJO1K9dhqJbq7FcWtHTePPxK6R5bwI19nhdKhhrk6GEuYfMwDnOhf7n7d%2BQnDnz5klTk%2BTKqfObmXg8boZJFcpwAKecKi8WFO%2FvW3l7MLS3%2F9IGOqUBgZFPXZAc3MkhWtZnkpEV8nps206Kgbh05be%2FubDcv1gikBq7bRFmojGrXydNUOWM9NZFmSKVrat2M74BCqbeTIxKqCQbO2TV6ARBT1oQA2YAEAyrG03n4QqQe1LLkNmks3MATwc2i6C2dBRXBuprGePLZXFFLT7O5FTjtTMjcSOglAeTzgEWGCpIXP7H97t2%2F0s8Ue%2FGI114BDFxM5qfXoKigim5&X-Amz-Signature=ec79f507890e3b9436c2fb20557fa64d5b30e690107527c19f0b515469c8f646&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

[image](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/e129f196-d48a-4e92-8c28-37dc1d2810ce/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UW3NL7VX%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T234348Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIEmto5bKXUaoT1AJ9rac8SNKzSJA8rdClcu8dWMSkYFnAiEA08sHuYqhouzv7Q43xp5qK7gCIjUjU0OwdmwghckC8RMqiAQIxv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDF4mbF6RlLyoOgBgAircA%2FITKtBJ%2BVZYMvIOtbg3U4fiVnsGDFNnNanaiwymh4hZR7q6MVxswyuUcTpCesd1qJAUa0jSDvcLJghkG9qrm0pneZ5jhZh9Zb0lH8Gs76%2FU5qetH4FKEVVQcdvIih8QjyU%2FFQp6R4sCd0Pq7Yr88Q2LIPiZGtcBH5jZzBXh3JP5LYdLlHOPEQjLLvIS8Q2UtfYuiz%2F2snrjc%2FEJv%2BgIUUChjRboZmZil0A1rb%2FZilVn%2FpLg50vNP8sYluF9gfec%2FYFsGCN%2BGuARGMwh6PTrT9qcU%2FWfjqIvvaijWfQ7vDOxykGk8sxGeNbLxZMzBpcSxM9ve%2F8fEE%2FqDTUztr6S4Dq5XuzycS6l2Uedh8Vhr1rBKG8jSOv1xbZr1WLpD2I7IOmFt7zCM43bHxbfnuoFSifLgT3OG88QJZf7BHYyxn2o2nRSbBiheIgPb5KRQy9fkIPzM6b1vbIIzDJwGjv38oYraHdBN7jhHc7GxuZ7OSR%2BtQt3JSaeKxihHSMg7qoNWonFo3WoqwS2oh0rBYVNomJO1K9dhqJbq7FcWtHTePPxK6R5bwI19nhdKhhrk6GEuYfMwDnOhf7n7d%2BQnDnz5klTk%2BTKqfObmXg8boZJFcpwAKecKi8WFO%2FvW3l7MLS3%2F9IGOqUBgZFPXZAc3MkhWtZnkpEV8nps206Kgbh05be%2FubDcv1gikBq7bRFmojGrXydNUOWM9NZFmSKVrat2M74BCqbeTIxKqCQbO2TV6ARBT1oQA2YAEAyrG03n4QqQe1LLkNmks3MATwc2i6C2dBRXBuprGePLZXFFLT7O5FTjtTMjcSOglAeTzgEWGCpIXP7H97t2%2F0s8Ue%2FGI114BDFxM5qfXoKigim5&X-Amz-Signature=9bf47fb0f7ed40cccd0e3161bd46bce286c669e94af329079e044c79ad586d26&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

[image](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/a62195ab-12ee-47a9-8358-5a5132e8789a/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UW3NL7VX%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T234348Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIEmto5bKXUaoT1AJ9rac8SNKzSJA8rdClcu8dWMSkYFnAiEA08sHuYqhouzv7Q43xp5qK7gCIjUjU0OwdmwghckC8RMqiAQIxv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDF4mbF6RlLyoOgBgAircA%2FITKtBJ%2BVZYMvIOtbg3U4fiVnsGDFNnNanaiwymh4hZR7q6MVxswyuUcTpCesd1qJAUa0jSDvcLJghkG9qrm0pneZ5jhZh9Zb0lH8Gs76%2FU5qetH4FKEVVQcdvIih8QjyU%2FFQp6R4sCd0Pq7Yr88Q2LIPiZGtcBH5jZzBXh3JP5LYdLlHOPEQjLLvIS8Q2UtfYuiz%2F2snrjc%2FEJv%2BgIUUChjRboZmZil0A1rb%2FZilVn%2FpLg50vNP8sYluF9gfec%2FYFsGCN%2BGuARGMwh6PTrT9qcU%2FWfjqIvvaijWfQ7vDOxykGk8sxGeNbLxZMzBpcSxM9ve%2F8fEE%2FqDTUztr6S4Dq5XuzycS6l2Uedh8Vhr1rBKG8jSOv1xbZr1WLpD2I7IOmFt7zCM43bHxbfnuoFSifLgT3OG88QJZf7BHYyxn2o2nRSbBiheIgPb5KRQy9fkIPzM6b1vbIIzDJwGjv38oYraHdBN7jhHc7GxuZ7OSR%2BtQt3JSaeKxihHSMg7qoNWonFo3WoqwS2oh0rBYVNomJO1K9dhqJbq7FcWtHTePPxK6R5bwI19nhdKhhrk6GEuYfMwDnOhf7n7d%2BQnDnz5klTk%2BTKqfObmXg8boZJFcpwAKecKi8WFO%2FvW3l7MLS3%2F9IGOqUBgZFPXZAc3MkhWtZnkpEV8nps206Kgbh05be%2FubDcv1gikBq7bRFmojGrXydNUOWM9NZFmSKVrat2M74BCqbeTIxKqCQbO2TV6ARBT1oQA2YAEAyrG03n4QqQe1LLkNmks3MATwc2i6C2dBRXBuprGePLZXFFLT7O5FTjtTMjcSOglAeTzgEWGCpIXP7H97t2%2F0s8Ue%2FGI114BDFxM5qfXoKigim5&X-Amz-Signature=10f567f0c24490f98f8cb525ed4303cd29187d66d7726dd05482f69ff97ebeb1&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

[image](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/abd5b578-e420-4b2f-b9c8-63b9e1f6081d/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UW3NL7VX%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T234348Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIEmto5bKXUaoT1AJ9rac8SNKzSJA8rdClcu8dWMSkYFnAiEA08sHuYqhouzv7Q43xp5qK7gCIjUjU0OwdmwghckC8RMqiAQIxv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDF4mbF6RlLyoOgBgAircA%2FITKtBJ%2BVZYMvIOtbg3U4fiVnsGDFNnNanaiwymh4hZR7q6MVxswyuUcTpCesd1qJAUa0jSDvcLJghkG9qrm0pneZ5jhZh9Zb0lH8Gs76%2FU5qetH4FKEVVQcdvIih8QjyU%2FFQp6R4sCd0Pq7Yr88Q2LIPiZGtcBH5jZzBXh3JP5LYdLlHOPEQjLLvIS8Q2UtfYuiz%2F2snrjc%2FEJv%2BgIUUChjRboZmZil0A1rb%2FZilVn%2FpLg50vNP8sYluF9gfec%2FYFsGCN%2BGuARGMwh6PTrT9qcU%2FWfjqIvvaijWfQ7vDOxykGk8sxGeNbLxZMzBpcSxM9ve%2F8fEE%2FqDTUztr6S4Dq5XuzycS6l2Uedh8Vhr1rBKG8jSOv1xbZr1WLpD2I7IOmFt7zCM43bHxbfnuoFSifLgT3OG88QJZf7BHYyxn2o2nRSbBiheIgPb5KRQy9fkIPzM6b1vbIIzDJwGjv38oYraHdBN7jhHc7GxuZ7OSR%2BtQt3JSaeKxihHSMg7qoNWonFo3WoqwS2oh0rBYVNomJO1K9dhqJbq7FcWtHTePPxK6R5bwI19nhdKhhrk6GEuYfMwDnOhf7n7d%2BQnDnz5klTk%2BTKqfObmXg8boZJFcpwAKecKi8WFO%2FvW3l7MLS3%2F9IGOqUBgZFPXZAc3MkhWtZnkpEV8nps206Kgbh05be%2FubDcv1gikBq7bRFmojGrXydNUOWM9NZFmSKVrat2M74BCqbeTIxKqCQbO2TV6ARBT1oQA2YAEAyrG03n4QqQe1LLkNmks3MATwc2i6C2dBRXBuprGePLZXFFLT7O5FTjtTMjcSOglAeTzgEWGCpIXP7H97t2%2F0s8Ue%2FGI114BDFxM5qfXoKigim5&X-Amz-Signature=cd319e35c724c66563653d2a11c14dad74f69e3f7af15f88e2c6a95e309f1eae&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

[image](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/9ff2deac-c1ae-498c-87dc-bab4f9a84f1f/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UW3NL7VX%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T234348Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIEmto5bKXUaoT1AJ9rac8SNKzSJA8rdClcu8dWMSkYFnAiEA08sHuYqhouzv7Q43xp5qK7gCIjUjU0OwdmwghckC8RMqiAQIxv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDF4mbF6RlLyoOgBgAircA%2FITKtBJ%2BVZYMvIOtbg3U4fiVnsGDFNnNanaiwymh4hZR7q6MVxswyuUcTpCesd1qJAUa0jSDvcLJghkG9qrm0pneZ5jhZh9Zb0lH8Gs76%2FU5qetH4FKEVVQcdvIih8QjyU%2FFQp6R4sCd0Pq7Yr88Q2LIPiZGtcBH5jZzBXh3JP5LYdLlHOPEQjLLvIS8Q2UtfYuiz%2F2snrjc%2FEJv%2BgIUUChjRboZmZil0A1rb%2FZilVn%2FpLg50vNP8sYluF9gfec%2FYFsGCN%2BGuARGMwh6PTrT9qcU%2FWfjqIvvaijWfQ7vDOxykGk8sxGeNbLxZMzBpcSxM9ve%2F8fEE%2FqDTUztr6S4Dq5XuzycS6l2Uedh8Vhr1rBKG8jSOv1xbZr1WLpD2I7IOmFt7zCM43bHxbfnuoFSifLgT3OG88QJZf7BHYyxn2o2nRSbBiheIgPb5KRQy9fkIPzM6b1vbIIzDJwGjv38oYraHdBN7jhHc7GxuZ7OSR%2BtQt3JSaeKxihHSMg7qoNWonFo3WoqwS2oh0rBYVNomJO1K9dhqJbq7FcWtHTePPxK6R5bwI19nhdKhhrk6GEuYfMwDnOhf7n7d%2BQnDnz5klTk%2BTKqfObmXg8boZJFcpwAKecKi8WFO%2FvW3l7MLS3%2F9IGOqUBgZFPXZAc3MkhWtZnkpEV8nps206Kgbh05be%2FubDcv1gikBq7bRFmojGrXydNUOWM9NZFmSKVrat2M74BCqbeTIxKqCQbO2TV6ARBT1oQA2YAEAyrG03n4QqQe1LLkNmks3MATwc2i6C2dBRXBuprGePLZXFFLT7O5FTjtTMjcSOglAeTzgEWGCpIXP7H97t2%2F0s8Ue%2FGI114BDFxM5qfXoKigim5&X-Amz-Signature=183a63078afb16b581512194ab70d8bb8d88e0d6386afc2b9aba2ad36567c191&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

[image](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/7273e689-0156-4f1c-938f-216620a765b6/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UW3NL7VX%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T234348Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIEmto5bKXUaoT1AJ9rac8SNKzSJA8rdClcu8dWMSkYFnAiEA08sHuYqhouzv7Q43xp5qK7gCIjUjU0OwdmwghckC8RMqiAQIxv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDF4mbF6RlLyoOgBgAircA%2FITKtBJ%2BVZYMvIOtbg3U4fiVnsGDFNnNanaiwymh4hZR7q6MVxswyuUcTpCesd1qJAUa0jSDvcLJghkG9qrm0pneZ5jhZh9Zb0lH8Gs76%2FU5qetH4FKEVVQcdvIih8QjyU%2FFQp6R4sCd0Pq7Yr88Q2LIPiZGtcBH5jZzBXh3JP5LYdLlHOPEQjLLvIS8Q2UtfYuiz%2F2snrjc%2FEJv%2BgIUUChjRboZmZil0A1rb%2FZilVn%2FpLg50vNP8sYluF9gfec%2FYFsGCN%2BGuARGMwh6PTrT9qcU%2FWfjqIvvaijWfQ7vDOxykGk8sxGeNbLxZMzBpcSxM9ve%2F8fEE%2FqDTUztr6S4Dq5XuzycS6l2Uedh8Vhr1rBKG8jSOv1xbZr1WLpD2I7IOmFt7zCM43bHxbfnuoFSifLgT3OG88QJZf7BHYyxn2o2nRSbBiheIgPb5KRQy9fkIPzM6b1vbIIzDJwGjv38oYraHdBN7jhHc7GxuZ7OSR%2BtQt3JSaeKxihHSMg7qoNWonFo3WoqwS2oh0rBYVNomJO1K9dhqJbq7FcWtHTePPxK6R5bwI19nhdKhhrk6GEuYfMwDnOhf7n7d%2BQnDnz5klTk%2BTKqfObmXg8boZJFcpwAKecKi8WFO%2FvW3l7MLS3%2F9IGOqUBgZFPXZAc3MkhWtZnkpEV8nps206Kgbh05be%2FubDcv1gikBq7bRFmojGrXydNUOWM9NZFmSKVrat2M74BCqbeTIxKqCQbO2TV6ARBT1oQA2YAEAyrG03n4QqQe1LLkNmks3MATwc2i6C2dBRXBuprGePLZXFFLT7O5FTjtTMjcSOglAeTzgEWGCpIXP7H97t2%2F0s8Ue%2FGI114BDFxM5qfXoKigim5&X-Amz-Signature=48d513159b4710166fa4fa2c5eac2571515d8b6f5f858d6154ab4b17f8aaeb85&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

[image](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/1a246255-c11b-40ab-80ad-15e9079d8518/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UW3NL7VX%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T234348Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIEmto5bKXUaoT1AJ9rac8SNKzSJA8rdClcu8dWMSkYFnAiEA08sHuYqhouzv7Q43xp5qK7gCIjUjU0OwdmwghckC8RMqiAQIxv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDF4mbF6RlLyoOgBgAircA%2FITKtBJ%2BVZYMvIOtbg3U4fiVnsGDFNnNanaiwymh4hZR7q6MVxswyuUcTpCesd1qJAUa0jSDvcLJghkG9qrm0pneZ5jhZh9Zb0lH8Gs76%2FU5qetH4FKEVVQcdvIih8QjyU%2FFQp6R4sCd0Pq7Yr88Q2LIPiZGtcBH5jZzBXh3JP5LYdLlHOPEQjLLvIS8Q2UtfYuiz%2F2snrjc%2FEJv%2BgIUUChjRboZmZil0A1rb%2FZilVn%2FpLg50vNP8sYluF9gfec%2FYFsGCN%2BGuARGMwh6PTrT9qcU%2FWfjqIvvaijWfQ7vDOxykGk8sxGeNbLxZMzBpcSxM9ve%2F8fEE%2FqDTUztr6S4Dq5XuzycS6l2Uedh8Vhr1rBKG8jSOv1xbZr1WLpD2I7IOmFt7zCM43bHxbfnuoFSifLgT3OG88QJZf7BHYyxn2o2nRSbBiheIgPb5KRQy9fkIPzM6b1vbIIzDJwGjv38oYraHdBN7jhHc7GxuZ7OSR%2BtQt3JSaeKxihHSMg7qoNWonFo3WoqwS2oh0rBYVNomJO1K9dhqJbq7FcWtHTePPxK6R5bwI19nhdKhhrk6GEuYfMwDnOhf7n7d%2BQnDnz5klTk%2BTKqfObmXg8boZJFcpwAKecKi8WFO%2FvW3l7MLS3%2F9IGOqUBgZFPXZAc3MkhWtZnkpEV8nps206Kgbh05be%2FubDcv1gikBq7bRFmojGrXydNUOWM9NZFmSKVrat2M74BCqbeTIxKqCQbO2TV6ARBT1oQA2YAEAyrG03n4QqQe1LLkNmks3MATwc2i6C2dBRXBuprGePLZXFFLT7O5FTjtTMjcSOglAeTzgEWGCpIXP7H97t2%2F0s8Ue%2FGI114BDFxM5qfXoKigim5&X-Amz-Signature=1463b68eeeb4f4d71d4bba5dc442d8106936f85e86db8f9f2cd88d1398769e14&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

[image](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/cf858699-67cd-46c7-97ce-3a4d89036e95/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UW3NL7VX%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T234348Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIEmto5bKXUaoT1AJ9rac8SNKzSJA8rdClcu8dWMSkYFnAiEA08sHuYqhouzv7Q43xp5qK7gCIjUjU0OwdmwghckC8RMqiAQIxv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDF4mbF6RlLyoOgBgAircA%2FITKtBJ%2BVZYMvIOtbg3U4fiVnsGDFNnNanaiwymh4hZR7q6MVxswyuUcTpCesd1qJAUa0jSDvcLJghkG9qrm0pneZ5jhZh9Zb0lH8Gs76%2FU5qetH4FKEVVQcdvIih8QjyU%2FFQp6R4sCd0Pq7Yr88Q2LIPiZGtcBH5jZzBXh3JP5LYdLlHOPEQjLLvIS8Q2UtfYuiz%2F2snrjc%2FEJv%2BgIUUChjRboZmZil0A1rb%2FZilVn%2FpLg50vNP8sYluF9gfec%2FYFsGCN%2BGuARGMwh6PTrT9qcU%2FWfjqIvvaijWfQ7vDOxykGk8sxGeNbLxZMzBpcSxM9ve%2F8fEE%2FqDTUztr6S4Dq5XuzycS6l2Uedh8Vhr1rBKG8jSOv1xbZr1WLpD2I7IOmFt7zCM43bHxbfnuoFSifLgT3OG88QJZf7BHYyxn2o2nRSbBiheIgPb5KRQy9fkIPzM6b1vbIIzDJwGjv38oYraHdBN7jhHc7GxuZ7OSR%2BtQt3JSaeKxihHSMg7qoNWonFo3WoqwS2oh0rBYVNomJO1K9dhqJbq7FcWtHTePPxK6R5bwI19nhdKhhrk6GEuYfMwDnOhf7n7d%2BQnDnz5klTk%2BTKqfObmXg8boZJFcpwAKecKi8WFO%2FvW3l7MLS3%2F9IGOqUBgZFPXZAc3MkhWtZnkpEV8nps206Kgbh05be%2FubDcv1gikBq7bRFmojGrXydNUOWM9NZFmSKVrat2M74BCqbeTIxKqCQbO2TV6ARBT1oQA2YAEAyrG03n4QqQe1LLkNmks3MATwc2i6C2dBRXBuprGePLZXFFLT7O5FTjtTMjcSOglAeTzgEWGCpIXP7H97t2%2F0s8Ue%2FGI114BDFxM5qfXoKigim5&X-Amz-Signature=e6960be8a6eec2619b83c7269777572d3e7e847918606730da494350b57e6c53&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

[image](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/e3f1a3f5-5a65-48d5-b464-b161ce40fb79/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UW3NL7VX%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T234348Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIEmto5bKXUaoT1AJ9rac8SNKzSJA8rdClcu8dWMSkYFnAiEA08sHuYqhouzv7Q43xp5qK7gCIjUjU0OwdmwghckC8RMqiAQIxv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDF4mbF6RlLyoOgBgAircA%2FITKtBJ%2BVZYMvIOtbg3U4fiVnsGDFNnNanaiwymh4hZR7q6MVxswyuUcTpCesd1qJAUa0jSDvcLJghkG9qrm0pneZ5jhZh9Zb0lH8Gs76%2FU5qetH4FKEVVQcdvIih8QjyU%2FFQp6R4sCd0Pq7Yr88Q2LIPiZGtcBH5jZzBXh3JP5LYdLlHOPEQjLLvIS8Q2UtfYuiz%2F2snrjc%2FEJv%2BgIUUChjRboZmZil0A1rb%2FZilVn%2FpLg50vNP8sYluF9gfec%2FYFsGCN%2BGuARGMwh6PTrT9qcU%2FWfjqIvvaijWfQ7vDOxykGk8sxGeNbLxZMzBpcSxM9ve%2F8fEE%2FqDTUztr6S4Dq5XuzycS6l2Uedh8Vhr1rBKG8jSOv1xbZr1WLpD2I7IOmFt7zCM43bHxbfnuoFSifLgT3OG88QJZf7BHYyxn2o2nRSbBiheIgPb5KRQy9fkIPzM6b1vbIIzDJwGjv38oYraHdBN7jhHc7GxuZ7OSR%2BtQt3JSaeKxihHSMg7qoNWonFo3WoqwS2oh0rBYVNomJO1K9dhqJbq7FcWtHTePPxK6R5bwI19nhdKhhrk6GEuYfMwDnOhf7n7d%2BQnDnz5klTk%2BTKqfObmXg8boZJFcpwAKecKi8WFO%2FvW3l7MLS3%2F9IGOqUBgZFPXZAc3MkhWtZnkpEV8nps206Kgbh05be%2FubDcv1gikBq7bRFmojGrXydNUOWM9NZFmSKVrat2M74BCqbeTIxKqCQbO2TV6ARBT1oQA2YAEAyrG03n4QqQe1LLkNmks3MATwc2i6C2dBRXBuprGePLZXFFLT7O5FTjtTMjcSOglAeTzgEWGCpIXP7H97t2%2F0s8Ue%2FGI114BDFxM5qfXoKigim5&X-Amz-Signature=2f8cf263b284f2ee03cf8f161ed2374c76a4ad3a09c98d6640124e3549eb4c55&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

[image](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/5bfdd38f-8f3d-4902-9c2d-0390090e8e4e/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UW3NL7VX%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T234348Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIEmto5bKXUaoT1AJ9rac8SNKzSJA8rdClcu8dWMSkYFnAiEA08sHuYqhouzv7Q43xp5qK7gCIjUjU0OwdmwghckC8RMqiAQIxv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDF4mbF6RlLyoOgBgAircA%2FITKtBJ%2BVZYMvIOtbg3U4fiVnsGDFNnNanaiwymh4hZR7q6MVxswyuUcTpCesd1qJAUa0jSDvcLJghkG9qrm0pneZ5jhZh9Zb0lH8Gs76%2FU5qetH4FKEVVQcdvIih8QjyU%2FFQp6R4sCd0Pq7Yr88Q2LIPiZGtcBH5jZzBXh3JP5LYdLlHOPEQjLLvIS8Q2UtfYuiz%2F2snrjc%2FEJv%2BgIUUChjRboZmZil0A1rb%2FZilVn%2FpLg50vNP8sYluF9gfec%2FYFsGCN%2BGuARGMwh6PTrT9qcU%2FWfjqIvvaijWfQ7vDOxykGk8sxGeNbLxZMzBpcSxM9ve%2F8fEE%2FqDTUztr6S4Dq5XuzycS6l2Uedh8Vhr1rBKG8jSOv1xbZr1WLpD2I7IOmFt7zCM43bHxbfnuoFSifLgT3OG88QJZf7BHYyxn2o2nRSbBiheIgPb5KRQy9fkIPzM6b1vbIIzDJwGjv38oYraHdBN7jhHc7GxuZ7OSR%2BtQt3JSaeKxihHSMg7qoNWonFo3WoqwS2oh0rBYVNomJO1K9dhqJbq7FcWtHTePPxK6R5bwI19nhdKhhrk6GEuYfMwDnOhf7n7d%2BQnDnz5klTk%2BTKqfObmXg8boZJFcpwAKecKi8WFO%2FvW3l7MLS3%2F9IGOqUBgZFPXZAc3MkhWtZnkpEV8nps206Kgbh05be%2FubDcv1gikBq7bRFmojGrXydNUOWM9NZFmSKVrat2M74BCqbeTIxKqCQbO2TV6ARBT1oQA2YAEAyrG03n4QqQe1LLkNmks3MATwc2i6C2dBRXBuprGePLZXFFLT7O5FTjtTMjcSOglAeTzgEWGCpIXP7H97t2%2F0s8Ue%2FGI114BDFxM5qfXoKigim5&X-Amz-Signature=71394bfa2a63f66cde78bb02d8ada1b114baf1b65e8bc0c719ea7a0724dc01e0&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)


