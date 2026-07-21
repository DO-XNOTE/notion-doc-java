---
title: 1-6 Bus的接入方式+RabbitMQ+&+Kafka
---

# 1-6 Bus的接入方式+RabbitMQ+&+Kafka

[image](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/ad43cc16-bf9d-4881-9a93-139bc403d5f4/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SXGLXAT4%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T225724Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDUGza3pYY3GJe6rzJwPc5NoRv1w7FpLhO0v43ScEOOCgIhAJsljwH%2FHps9t0Hr1en5B8gVxnFGpImscRt%2FiqOf2YTqKogECMb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1Igzj35XpKnw%2FHkov4bEq3ANoIHaUDrjegcW2W7dzmm21uO%2FJZhaYTrD%2B%2BWjB38boF%2BDe2qOEj4ciYRWfybcjHc%2BabYLWaLbUaxZzx8BhouA5lNJLUFbZXR8NJUAhU3BrKFVk6Pe2VUu%2Biyok5841MhYkhRxQXM5hkeqS0PEbc3DdLD3a9gnVDy9c7FLydS9p5MYS%2BmULR6Gzrplu2a1HVgSmKR6XHJTfu4lk4uPRdOFSRPEUuFJYuHSBLTz57%2Bl%2BJzq5illMMYV12k9m4BmwjlSWLFOl4AP2vPvVdqXS2KIvzP3jnRv9V88hh92OEhqZMNCzC6IrkuqM2Sf9c1OOrvvKG7tZ3XhsQNswf0a%2FWioGQsDsVjGX4oh%2FhhPfd8oXdjkpdL12PBt4M7vzhfwBrPptkN909cmNB49nkg0D6nEx2dEczugwFItMy3yQFpsO%2F1%2FUAN5kSJlMrf5g2vBk6tehMwpJV9Eo2c3II1T2ESbIeuUzwg8CBvR0durX4v180ih97q8hUU62sL3SWkGq7AgBEamRFkKIYkzF3X91DqiOBtw9EiLLVCVy3mz80igYqarcWyznc7%2Fr7WEncAajUsZdSAmltI9nzbRN4m%2FQUnCiX%2FgC%2F%2BdEc2CR4Lnn1ZGUiYZVXiQrMaCUzffCnTChuP%2FSBjqkAUpQdjubcTtTPmtkl5JyHrayqTDCl1KUxKIgWswFLnQEHAz0gH0V7D5IoSVHNxOOzZJKwiwCmBwGPzZ0lR02FQjNeFmvJHDwGMZ2YFZgqkeh0jpXaQONpEG2F6gdx%2Bua%2FBFRXBoQnoI4aXZ284nem5ca%2B0PgOJYN%2BahUGOfQSnlkViLSviHtr%2FBCHIa6Vqn5S9EkI5zoPPo7QMTrdUaYRyeDTlYX&X-Amz-Signature=54f3d66078b5f9f05fe67c9afff52a78f32c17f209f9e4596201e386f44de07d&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

**1-6 Bus的接入方式 RabbitMQ & Kafka**

前面我们了解了Bus的工作方式，在动手改造配置中心之前，我们先来了解一下Bus有哪些接入方式。

Spring的组件一向是以一种插件式的方式提供功能，将组件自身和我们项目中的业务代码隔离，使得我们更换组件的成本可以降到最低。Spring Cloud Bus也不例外，它的底层消息组件非常容易替换，替换过程不需要对业务代码引入任何变更。Bus就像一道隔离了底层消息组件和业务应用的中间层，比如我们从RabbitMQ切换为Kafka的时候，只需要做两件事就好了：

在项目pom中替换依赖组件更改配置文件里的连接信息

接下来我们就看一下RabbitMQ和Kafka两种消息组件如何接入Bus

**接入RabbitMQ**

RabbitMQ是实现了AMQP（Advanced Message Queue Protocal）的开源消息代理软件，也是大家平时项目中应用最广泛的消息分发组件之一。同学们在分布式章节应该已经深入了解了消息队列的使用，这里我们就不再赘述了。

接入RabbitMQ的方式很简单，我们只要在项目中引入以下依赖：

```java
<dependency>
      <groupId>org.springframework.cloud</groupId>**
      <artifactId>spring-cloud-starter-bus-amqp</artifactId>**
</dependency>
```

点进去查看这个依赖的pom，你会发现它依赖了spring-cloud-starter-stream-rabbit，也就是说Stream组件才是真正被用来发送广播消息到RabbitMQ的，Bus这里只是帮我们封装了整个消息的发布和监听动作。接下来我们看下项目中所需的具体配置：

```java
spring:
  rabbitmq:
  host: localhost
  port: 5672
  username: guest
  password: guest
```

上面配置分别指定了RabbitMQ的地址、端口、用户名和密码，以上均采用RabbitMQ中的默认配置。

**接入Kafka**

要使用Kafka来实现消息代理，只需要把上一步中引入的spring-cloud-starter-bus-amqp依赖替换成spring-cloud-starter-bus-kafka依赖

```java
<dependency>
			<groupId>org.springframework.cloud</groupId>
			<artifactId>spring-cloud-starter-bus-kafka</artifactId>
</dependency>
```

如果大家的Kafka和ZooKeeper都运行在本地，并且采用了默认配置，那么不需要做任何额外的配置，就可以直接使用。但是在生产环境中往往Kafka和ZooKeeper会部署在不同的环境，所以就需要做一些额外配置：

```java
spring.cloud.stream.kafka.binder.brokers
spring.cloud.stream.kafka.binder.defaultBrokerPort
spring.cloud.stream.kafka.binder.zkNodes
spring.cloud.stream.kafka.binder.defaultZkPort
```

**小结**

这一节我们了解了Bus的接入方式，下一小节我们趁热打铁，把分布式配置中心改为总线式架构。

学习Tips：大家知道Spring Cloud的组件都是通过一个注解开启功能，可是Bus既没有添加额外注解，而且除了消息组件的连接配置以外也没什么特殊配置，那么它是如何与actuator/bus-refresh的刷新功能关联上的呢？前面我们经过了很多源码阅读练习，也积累了一些经验。这里就给大家布置一个小任务，尝试摸清bus-refresh是如何工作的，我先提供一个线索，大家可以先找到bus-refresh的入口Controller类，然后顺藤摸瓜就好了。



[image](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/b7f26ef2-a278-429d-9779-7b0e9111d59d/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SXGLXAT4%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T225724Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDUGza3pYY3GJe6rzJwPc5NoRv1w7FpLhO0v43ScEOOCgIhAJsljwH%2FHps9t0Hr1en5B8gVxnFGpImscRt%2FiqOf2YTqKogECMb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1Igzj35XpKnw%2FHkov4bEq3ANoIHaUDrjegcW2W7dzmm21uO%2FJZhaYTrD%2B%2BWjB38boF%2BDe2qOEj4ciYRWfybcjHc%2BabYLWaLbUaxZzx8BhouA5lNJLUFbZXR8NJUAhU3BrKFVk6Pe2VUu%2Biyok5841MhYkhRxQXM5hkeqS0PEbc3DdLD3a9gnVDy9c7FLydS9p5MYS%2BmULR6Gzrplu2a1HVgSmKR6XHJTfu4lk4uPRdOFSRPEUuFJYuHSBLTz57%2Bl%2BJzq5illMMYV12k9m4BmwjlSWLFOl4AP2vPvVdqXS2KIvzP3jnRv9V88hh92OEhqZMNCzC6IrkuqM2Sf9c1OOrvvKG7tZ3XhsQNswf0a%2FWioGQsDsVjGX4oh%2FhhPfd8oXdjkpdL12PBt4M7vzhfwBrPptkN909cmNB49nkg0D6nEx2dEczugwFItMy3yQFpsO%2F1%2FUAN5kSJlMrf5g2vBk6tehMwpJV9Eo2c3II1T2ESbIeuUzwg8CBvR0durX4v180ih97q8hUU62sL3SWkGq7AgBEamRFkKIYkzF3X91DqiOBtw9EiLLVCVy3mz80igYqarcWyznc7%2Fr7WEncAajUsZdSAmltI9nzbRN4m%2FQUnCiX%2FgC%2F%2BdEc2CR4Lnn1ZGUiYZVXiQrMaCUzffCnTChuP%2FSBjqkAUpQdjubcTtTPmtkl5JyHrayqTDCl1KUxKIgWswFLnQEHAz0gH0V7D5IoSVHNxOOzZJKwiwCmBwGPzZ0lR02FQjNeFmvJHDwGMZ2YFZgqkeh0jpXaQONpEG2F6gdx%2Bua%2FBFRXBoQnoI4aXZ284nem5ca%2B0PgOJYN%2BahUGOfQSnlkViLSviHtr%2FBCHIa6Vqn5S9EkI5zoPPo7QMTrdUaYRyeDTlYX&X-Amz-Signature=b06106d468221430d23eb13a9e34f27914eac087afe90b7ba764a655ce1bc095&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)




