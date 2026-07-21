---
title: rabbitmq之homebrew安装
---

# rabbitmq之homebrew安装

[image](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/ef8cc29e-504a-4b5a-96a5-4e7290943822/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466Z77HMFFQ%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T234410Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIHFnSJO%2FAYgqaDBAd%2FxhRjb%2B7xlZWyFupP%2FhyHO%2BiAzQAiEA%2Bhpl3A32ul3Z6lqxSmb8yG58UZbCSQIPPTq00uNvAo0qiAQIxv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDKp4NXitWqOJH9FUHSrcA3i91LKVQ5JjlQIBTBeD6OEq4NPsDGO8yQnm20PmNBGvAoiV1C8XLielBb3EbT%2BaQt8R2Q7qII84r7hS4gn%2BM83X6X5coTHVsYLpAipOiksupvpbFmoPrKnnW8k8V6UjBaw4%2BxTuBzCqmND8kr2emQrUEvN7ybx%2BFrcMiIDm6khZFhaS2or8eo3QrxjmPCLppvlUrmSoEzXTQu41siV%2FK4Eaz%2FEO1%2F5Ujg3luS7uM8Yx3uI3bv6lDVm78mpaSN7RwE6IhZBRJq0cxIi5MkPmSz8FI5ckTX8VYId5AcpORr4atL2G2XMwv6qUn52f8TjHcgSDMjGMRQZfGSrpcgrEw6X3y0tA0Lt7MSILBVim1S1ImjRHGb11wXA6wcYtqf%2Bt3Vfziz7rbmYWQnmZrO33aBfptsMIV3YY1TuCep7r2q11VqOpfVrlv%2Fb%2FwMhtcHMlSDb9u5aPpH0mRjejDERljxyQDN%2Buci5nUeykL1%2BbPgy7%2B9ymXq3NZtjnqKcSfwx68MWJWTBmTtIjWg5Vxjf3t58%2FMRfAT0qYLxnX73IvYPg9kzGYZNd3r4Ky8VYoqiHu5AlIdPFms9EzinJ111EA%2BvqDtiLY1%2BbPUZn50jYeTxqoxxZmJDXqdtNCRAqfMI26%2F9IGOqUBarc2khv2c4E926H%2Fs%2F63zVKTKaj0EAfbAIdWuMoasO7yuGKHo6lC55nA2EeGNAMKsqfX3%2FEWfa0GFofnOpMrDTBV7j2wfcWZD0FTEBcSfjdLpUmWQl%2BVY6vzgY5T8p9AxtVGs95kMOyOuY3eqLJZF0sxSxzK7bEE8zmd2XxSotYxWGPz0UbfizlV9HCpx3et6TLT6m06az5vJs%2FQgj9s5L8Pp%2FjB&X-Amz-Signature=eabcb8657338c5a28391d13629dd5cda4ecdc617ce6f739afe015c37fa131cd3&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

配置文件：rabbitmq-env.conf

启动服务：rabbitmq-server

```shell
按住给过程：

# 官方推荐安装方式

brew install rabbitmq

# 配置环境变量：

# 编辑系统文件 ~/.bashrc 或者 ~/.zshrc

vim ~/.bashrc

# 文件中添加如下内容：

export PATH=$PATH:/usr/local/sbin

# :wq 保存文件后执行文件

source ~/.zshrc

# 查看版本号

# 打开RabbitMQ的sbin目录

cd /opt/homebrew/Cellar/rabbitmq/3.9.15/sbin

# 启用插件rabbitmq_management

rabbitmq-plugins enable rabbitmq_management

# 打开RabbitMQ的sbin目录

cd /opt/homebrew/Cellar/rabbitmq/3.9.15/sbin

# 启动服务()

sudo ./rabbitmq-server

# 以守护程序的方式在后台运行

./rabbitmq-server -detached

# 查询服务器状态

./rabbitmqctl status

# 关闭 RabbitMQ 节点

./rabbitmqctl stop

# 重置 RabbitMQ 节点

./rabbitmqctl reset

# 查看已声明的队列

./rabbitmqctl list_queues

# 查看交换器

./rabbitmqctl list_exchanges

# 该命令还可以附加参数，比如列出交换器的名称、类型、是否持久化、是否自动删除：

./rabbitmqctl list_exchanges name type durable auto_delete

# 查看绑定

./rabbitmqctl list_bindings
```

## **5. 访问RabbitMQ Management系统**

打开地址[http://localhost:15672](http://localhost:15672/)，默认用户名和密码都是guest。

[image](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/fffa4a9c-63cc-4d7b-bfc2-3eaebae91dda/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466Z77HMFFQ%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T234410Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIHFnSJO%2FAYgqaDBAd%2FxhRjb%2B7xlZWyFupP%2FhyHO%2BiAzQAiEA%2Bhpl3A32ul3Z6lqxSmb8yG58UZbCSQIPPTq00uNvAo0qiAQIxv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDKp4NXitWqOJH9FUHSrcA3i91LKVQ5JjlQIBTBeD6OEq4NPsDGO8yQnm20PmNBGvAoiV1C8XLielBb3EbT%2BaQt8R2Q7qII84r7hS4gn%2BM83X6X5coTHVsYLpAipOiksupvpbFmoPrKnnW8k8V6UjBaw4%2BxTuBzCqmND8kr2emQrUEvN7ybx%2BFrcMiIDm6khZFhaS2or8eo3QrxjmPCLppvlUrmSoEzXTQu41siV%2FK4Eaz%2FEO1%2F5Ujg3luS7uM8Yx3uI3bv6lDVm78mpaSN7RwE6IhZBRJq0cxIi5MkPmSz8FI5ckTX8VYId5AcpORr4atL2G2XMwv6qUn52f8TjHcgSDMjGMRQZfGSrpcgrEw6X3y0tA0Lt7MSILBVim1S1ImjRHGb11wXA6wcYtqf%2Bt3Vfziz7rbmYWQnmZrO33aBfptsMIV3YY1TuCep7r2q11VqOpfVrlv%2Fb%2FwMhtcHMlSDb9u5aPpH0mRjejDERljxyQDN%2Buci5nUeykL1%2BbPgy7%2B9ymXq3NZtjnqKcSfwx68MWJWTBmTtIjWg5Vxjf3t58%2FMRfAT0qYLxnX73IvYPg9kzGYZNd3r4Ky8VYoqiHu5AlIdPFms9EzinJ111EA%2BvqDtiLY1%2BbPUZn50jYeTxqoxxZmJDXqdtNCRAqfMI26%2F9IGOqUBarc2khv2c4E926H%2Fs%2F63zVKTKaj0EAfbAIdWuMoasO7yuGKHo6lC55nA2EeGNAMKsqfX3%2FEWfa0GFofnOpMrDTBV7j2wfcWZD0FTEBcSfjdLpUmWQl%2BVY6vzgY5T8p9AxtVGs95kMOyOuY3eqLJZF0sxSxzK7bEE8zmd2XxSotYxWGPz0UbfizlV9HCpx3et6TLT6m06az5vJs%2FQgj9s5L8Pp%2FjB&X-Amz-Signature=76730d8df9143ed3a37bf3642b7ff3ca78aa0089d1518d98b3961922f176e39a&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

rabbitmq的环境配置文件所在目录：

cd /opt/homebrew/etc/rabbitmq/


