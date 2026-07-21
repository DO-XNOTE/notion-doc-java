---
title: 1-3 kafka 入门和核心 API 解析
---

# 1-3 kafka 入门和核心 API 解析

[image](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/261775b4-64d2-4eba-82c7-4f4f405b6d4f/SCR-20240807-ftgk.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WOU56U75%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T225321Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIAkVQ6BsilR0lFy2IDPGcKTPoWOs4sBkYnHjW4NWJ9DDAiEAuDZ4Tx5NDX4GLl37aDscZsiIRu8Fw5Wexxzi6SVm6gcqiAQIxv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDP8QNRj0KYdGUtts4ircA%2BjMlwwmaMMBSmuoArBvWEk259L%2BjJQv4jj%2Bkm%2FjmC53gsnSN9Kr%2Frh6%2B5xpW527bd3F6OiBplPZLS2%2B4yWASdqMQVmoIF0kWiCFyL4nVga59VcnHKIfuNBDEehOb0buZjFAQVcd9dx3z2dt8A4EjlKlpSCRbur5BhrLmZwywdmoiop5z9wqam7DDbFrOBsSxFJIQ7QO6dB3qvUeI0wcy7OghbjVrd1i1HbcRb%2BqM7nSSsCO8Y7wouyCqjPk5N4qBenXHzd%2BrbUQ2nJtg2dNwvUJcT5PBYSY02e6eRvoPDT1CbUFeAF4q31Kkq36zP8nNSHY3qy1vwp8IewFIyQyvS37Y5YT6rU2jfzRPtW1gdm43xfO9cj5%2BJ8Xti54Kg70zkZq3t8z0SvjGBpCI4xjE4w5%2FFKFPWxOGoqfsf%2B%2FBIXV5gQ%2BanD1d0LN%2Bms2Fo%2Fy9kWUGXJY%2BoZ0rQw9zRnPxuT6nUo8qluNRM9YL92zQFjxBMOpmByJrIrYLooWYuLilXOufWKil47NszehYgb5pAx6RWjaNv%2FFoB%2FkFVUiRJwjYgFBKexL8tqfQjt9bGCAr2pszPVhhqzp5d20hKo1Nsmk%2FJiVXvhOjwJO7jm9mc1zLocEPBUfcRy9tascMN27%2F9IGOqUBbARLBoXUuBmB82nG6bW8fSgYe6%2FtAWDX9lJwyyPNLZ3CEVfPVaqHtCw5OUtqoNfl7agOfKX9HhYd4kLxEd%2BbGmUsv9IuOnsIz1%2F%2Fv30OAnf26HyqWRaV%2FowLncPnYoqsnLarQMgOHuu5N0BUlUlMZV6aDt%2F2ode5oikH0hfNDkOuLqoI0hPg8Z2x2%2FI2ZAcMitz3fTddl1RFX5ZtZ4f%2BIcqiIfv6&X-Amz-Signature=62e2e0aa0c47032885533257d4ce5afe0fa9a3cf44d3c446528357abb3e3b7ab&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

```java
## 解压命令：
tar -zxvf kafka_2.12-2.1.0.tgz -C /usr/local/ 
## 改名命令：
mv kafka_2.12-2.1.0/ kafka_2.12
## 进入解压后的目录，修改server.properties文件： 
vim /usr/local/kafka_2.12/config/server.properties 
## 修改配置：
broker.id=0 
port=9092
host.name=192.168.11.51
advertised.host.name=192.168.11.51
log.dirs=/usr/local/kafka_2.12/kafka-logs 
num.partitions=2
zookeeper.connect=192.168.11.111:2181,192.168.11.112:2181,192.168.11.113:2181 
## 建立日志文件夹：
mkdir /usr/local/kafka_2.12/kafka-logs 
##启动kafka：
/usr/local/kafka_2.12/bin/kafka-server-start.sh /usr/local/kafka_2.12/config/server.properties &
```

[image](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/c47dff2d-0f82-435c-a99e-f874c7d1a035/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WOU56U75%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T225321Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIAkVQ6BsilR0lFy2IDPGcKTPoWOs4sBkYnHjW4NWJ9DDAiEAuDZ4Tx5NDX4GLl37aDscZsiIRu8Fw5Wexxzi6SVm6gcqiAQIxv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDP8QNRj0KYdGUtts4ircA%2BjMlwwmaMMBSmuoArBvWEk259L%2BjJQv4jj%2Bkm%2FjmC53gsnSN9Kr%2Frh6%2B5xpW527bd3F6OiBplPZLS2%2B4yWASdqMQVmoIF0kWiCFyL4nVga59VcnHKIfuNBDEehOb0buZjFAQVcd9dx3z2dt8A4EjlKlpSCRbur5BhrLmZwywdmoiop5z9wqam7DDbFrOBsSxFJIQ7QO6dB3qvUeI0wcy7OghbjVrd1i1HbcRb%2BqM7nSSsCO8Y7wouyCqjPk5N4qBenXHzd%2BrbUQ2nJtg2dNwvUJcT5PBYSY02e6eRvoPDT1CbUFeAF4q31Kkq36zP8nNSHY3qy1vwp8IewFIyQyvS37Y5YT6rU2jfzRPtW1gdm43xfO9cj5%2BJ8Xti54Kg70zkZq3t8z0SvjGBpCI4xjE4w5%2FFKFPWxOGoqfsf%2B%2FBIXV5gQ%2BanD1d0LN%2Bms2Fo%2Fy9kWUGXJY%2BoZ0rQw9zRnPxuT6nUo8qluNRM9YL92zQFjxBMOpmByJrIrYLooWYuLilXOufWKil47NszehYgb5pAx6RWjaNv%2FFoB%2FkFVUiRJwjYgFBKexL8tqfQjt9bGCAr2pszPVhhqzp5d20hKo1Nsmk%2FJiVXvhOjwJO7jm9mc1zLocEPBUfcRy9tascMN27%2F9IGOqUBbARLBoXUuBmB82nG6bW8fSgYe6%2FtAWDX9lJwyyPNLZ3CEVfPVaqHtCw5OUtqoNfl7agOfKX9HhYd4kLxEd%2BbGmUsv9IuOnsIz1%2F%2Fv30OAnf26HyqWRaV%2FowLncPnYoqsnLarQMgOHuu5N0BUlUlMZV6aDt%2F2ode5oikH0hfNDkOuLqoI0hPg8Z2x2%2FI2ZAcMitz3fTddl1RFX5ZtZ4f%2BIcqiIfv6&X-Amz-Signature=1366723f99d6b785dccabb57fbd6c8b0e8cce4bd1eb7df8fca4942ef11b0c0ad&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

```java
## 简单操作：
#（1）创建topic主题命令：（创建名为test的topic， 1个分区分别存放数据，数据备份总共1份）
kafka-topics.sh --zookeeper 192.168.11.111:2181 --create --topic topic1 --partitions 1  --replication-f 
## --zookeeper 为zk服务列表
## --create 命令后 --topic 为创建topic 并指定 topic name 
## --partitions 为指定分区数量
## --replication-factor 为指定副本集数量 
#（2）查看topic列表命令：
kafka-topics.sh --zookeeper 192.168.11.111:2181 --list
#（3）kafka命令发送数据：（然后我们就可以编写数据发送出去了）
kafka-console-producer.sh --broker-list 192.168.11.51:9092 --topic topic1 
#（4）kafka命令接受数据：（然后我们就可以看到消费的信息了）
kafka-console-consumer.sh --bootstrap-server 192.168.11.51:9092 --topic topic1 --from-beginning 
#（5）删除topic命令：
kafka-topics.sh --zookeeper 192.168.11.111:2181 --delete --topic topic1
#（6）kafka查看消费进度：（当我们需要查看一个消费者组的消费进度时，则使用下面的命令）
```

