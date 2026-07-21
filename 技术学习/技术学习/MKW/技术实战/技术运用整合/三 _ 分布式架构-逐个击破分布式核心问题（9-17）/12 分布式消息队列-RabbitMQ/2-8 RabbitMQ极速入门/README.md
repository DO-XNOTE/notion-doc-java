---
title: 2-8 RabbitMQ极速入门
---

# 2-8 RabbitMQ极速入门

[image](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/7e5c95b0-16d7-43b1-aa61-f2cefeb16e7c/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466Y54XLIU5%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T225245Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIGcewSVOwCWENET6%2F1cik018aIKuBMWRPxsVC7FDdzB5AiEAoEvNUcXiSSzJ63o1dV2bJzzHKFkW7fcH8rCxYap3%2FeoqiAQIxv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDEpU763EhlXSJiMgYyrcA%2Bkg05dSogYjDDaMMcjUerVinAwrpaq9P%2FxBH3yp71gHIemT8k5nRfg4zLTenwnD0hi69LEZdeuE9rBbxFQ94Q6paSIHvO0DQOO6AyXtSk8xhEyBhimJP4tuTabl%2BLioUR9%2BVwlwSpm3vo%2BjlVTAqxijj33zMpW4I0Aiorpxw5Dt3KvFJq%2BAZn5xo9j8TSJvGyFDqD%2BehVb8GAX9zrPAoxgPkJxQbD8xjjFbrGdsrLKXnzWSxgAZIqUoxr726WU4LUWvk9MVtqGhLpV%2BBjhWUkK2P8FQwHxIsw10Pt13EhMcS%2BvcUrSotxrbJh5ikSk0dbU521JISKdH5IhrVb7VjowGJWOkLAcXyJdMSmBTileUR8TfeV7jC6zn8bsFqoAPAilz%2BAXkT3EwpBJrevjlElX%2BqoY3UbXhmQfY%2FvfW2T1wjsuAAIXTfnd25DXF5q6mGwhrmhSiUVNnYq4f0zi0H95eIocOLOnfr0GbhugnJz3UN%2Bw9sZ5CbvgjQIpqKR1jnjikzfAv%2BeQ1MeX%2Fk9sj5sH0MfnnW0PFpSWVhwaxNZThdDKlDFrK%2BQ1BSruJOXNpI9Z38A1oewHPu96D2%2FNlCKyf5PJ5jv%2BCcG5uT7EgpXIIFtpsBiEEnj0OTg7oMLa6%2F9IGOqUB6COQQNAEqVcGsf60mJU%2F%2BsP1uBNee9Jz6XTqaV1jiEOwMyaF1qI3z3vca%2FYh5XmluNarF7bw5tSvWVVYyJ4EhpNTDCgXxTRfiar6LkEIujg2PUOgNUn24Igi0EtyCjtF%2FYRjZiFOnLg4r0zpNUsPqq99umtjpfmLu%2FaDD1FXxJRXJqeIED%2BBPVLYbufKhQUEvR9wyKj8Vwgrg4tUXuY0YaDtcYCP&X-Amz-Signature=ccac7b12f8afadceab32e66d4e9ad11fc2eaf6325382796944a771b9f8622fc3&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

```javascript
2-8附：RabbitMQ急速入门
急速安装RabbitMQ
Hi，小伙伴们，现在我们就快速地准备一台2G以上内存的Linux虚拟机。开始RabitMQ环境的搭建，然后和我一起体验RabbitMQ之旅吧～首先我们明确一下安下：
·准备一台Linux虚拟机，老师的机器是Linux7（CentOS7）；配置最好再2G内存以上哦，然后使用Xshell登录上去即可，注意准备工作非常重要哦。首先虚拟机是否能够和本机Ping通，检查虚拟机和本机的网络、防火墙等基础设施。
·进入安装：
#1.首先在Linux上进行一些软件的准备工作，yum下来一些基础的软件包
yum install build-essential openssl openssl-devel unixODBC unixODBC-devel make gcc gcc-c++ kernel-devel #2.下载RabbitMQ所需软件包（本神在这里使用的是RabbitMQ3.6.5稳定版本）
wgetwww.rabbitmq.com/releases/erlang/erlang-18.3-1.el7.centos.x86_64.rpm wget http: //repo. iotti. biz/CentoS/7/x86_64/socat-1.7. 3. 2-5. e17. lux. x8664. rpm
wgetwww.rabbitmq.com/releases/rabbitmq-server/v3.6.5/rabbitmq-server-3.6.5-1.noarch.rpm #3.安装服务命令
rpm -ivh erlang-18.3-1. el7. centos. x86_64. rpm rpm -ivh  socat-1. 7. 3. 2-5. el7. lux. x86_64. rpm
rpm -ivh rabbitmg-server-3. 6. 5-1. noarch. rpm #4.修改用户登录与连接心跳检测，注意修改
vim /usr/lib/rabbitmg/lib/rabbitmg server-3. 6.5/ebin/rabbit. app 修改点1：loopback_users 中的<<"guest">,只保留guest(用于用户登录) 修改点2：heartbeat为10（用于心跳连接）
#5.安装管理插件
##5.1首先启动服务（后面包含了停止、查看状态以及重启的命令）/etc/init. d/rabbitmq-server start stop I status restart
##5.2查看服务有没有启动：lsof—i：5672（5672是Rabbit的默认端口）rabbitmq-plugins enable rabbitmq_management
##5.3可查看管理端口有没有启动：
lsof -i:15672 或者 netstat -tnlp grep 15672
##6.一切OK我们访问地址，输入用户名密码均为guest：##http://你的ip地址：15672/
#7.如果一切顺利，那么到此为止，我们的环境已经安装完啦急速入门，Hello World
学习任何一个新的技术，都要从Hello World的开始，本神觉得任何一门技术，就好像我们在学生时代所学习的每门学科一样，那么最重要的就是Hello World一废话少絮，我们开始！
·首先第一步准备打开IDEA（或者Eclipse）开发工具，新建一个maven工程，引入对应的依赖包（pom.xml）<dependency>
KgroupId>com. rabbitmq</groupId> KartifactId)amqp-client</artifactId> <version)3.6. 5</version)
</dependency> 

```

[image](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/01c19a1e-5440-48b4-827a-e879e68c9b8e/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466Y54XLIU5%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T225245Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIGcewSVOwCWENET6%2F1cik018aIKuBMWRPxsVC7FDdzB5AiEAoEvNUcXiSSzJ63o1dV2bJzzHKFkW7fcH8rCxYap3%2FeoqiAQIxv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDEpU763EhlXSJiMgYyrcA%2Bkg05dSogYjDDaMMcjUerVinAwrpaq9P%2FxBH3yp71gHIemT8k5nRfg4zLTenwnD0hi69LEZdeuE9rBbxFQ94Q6paSIHvO0DQOO6AyXtSk8xhEyBhimJP4tuTabl%2BLioUR9%2BVwlwSpm3vo%2BjlVTAqxijj33zMpW4I0Aiorpxw5Dt3KvFJq%2BAZn5xo9j8TSJvGyFDqD%2BehVb8GAX9zrPAoxgPkJxQbD8xjjFbrGdsrLKXnzWSxgAZIqUoxr726WU4LUWvk9MVtqGhLpV%2BBjhWUkK2P8FQwHxIsw10Pt13EhMcS%2BvcUrSotxrbJh5ikSk0dbU521JISKdH5IhrVb7VjowGJWOkLAcXyJdMSmBTileUR8TfeV7jC6zn8bsFqoAPAilz%2BAXkT3EwpBJrevjlElX%2BqoY3UbXhmQfY%2FvfW2T1wjsuAAIXTfnd25DXF5q6mGwhrmhSiUVNnYq4f0zi0H95eIocOLOnfr0GbhugnJz3UN%2Bw9sZ5CbvgjQIpqKR1jnjikzfAv%2BeQ1MeX%2Fk9sj5sH0MfnnW0PFpSWVhwaxNZThdDKlDFrK%2BQ1BSruJOXNpI9Z38A1oewHPu96D2%2FNlCKyf5PJ5jv%2BCcG5uT7EgpXIIFtpsBiEEnj0OTg7oMLa6%2F9IGOqUB6COQQNAEqVcGsf60mJU%2F%2BsP1uBNee9Jz6XTqaV1jiEOwMyaF1qI3z3vca%2FYh5XmluNarF7bw5tSvWVVYyJ4EhpNTDCgXxTRfiar6LkEIujg2PUOgNUn24Igi0EtyCjtF%2FYRjZiFOnLg4r0zpNUsPqq99umtjpfmLu%2FaDD1FXxJRXJqeIED%2BBPVLYbufKhQUEvR9wyKj8Vwgrg4tUXuY0YaDtcYCP&X-Amz-Signature=8bc6eb91ead575d323a10dbab4bc121996e8b18f639bef08c1aae5bb5f001952&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)


