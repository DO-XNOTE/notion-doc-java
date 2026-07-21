---
title: 5-3 面试题深度解析-Spring Data Redis与Jedis的关系（0335）
---

# 5-3 面试题深度解析-Spring Data Redis与Jedis的关系（0335）

[image](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/6554650b-89ef-4f63-a5fd-8567a867f45a/SCR-20240814-jvgm.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666ANLN2JA%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T232148Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIDO43XEJSVX7cBP%2FocXZvIjtVQDWJv1LOMGv5iBcFFHRAiEAhAvXJT1Ou9DRhnO5CeFF1gDP5uS%2Fjj7Pv4eN0IT%2BMVcqiAQIxv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDHcImUjssAg7jkbr%2BSrcA5bgCN8m%2B9ssvzLs53mjwUXu846imkUh9rvN3iSk5lSV1ELNS349SCph7nK%2BTgDEtZmm7yctwzwzijyFuuUE939XOUKzWVdfOggBxHvOkxT1HZ30XFDRQGrFrmcpSYc%2FEk%2B7HgWId2F%2BrXD9BV1Ejrom%2BY3Ok95Kx7CXvEJ65qJ3ELH%2Bc2W%2FJc5I3nCcyApPC8UEyO7lPdijqBXVoU%2FikKp2X8CzBSMd8GuOk1M7DPs6oMqeW68mCV4rMLj%2BPj8%2Bpp5wJx9dODXzMSPvpSKeuk4VwePcVEvev1hRmOx19YFbUxFBK2HZtV8vCkHUs6Y26Cs65bYcqGJW3zOQ61i17I5%2FFkw%2FCC3OdntHfut9Mpp8gaJhCWCV%2B9nGLCsfcWg1rpj4WqrmrM5LR6%2BMQZgElZoOfuE%2Fidh6GawFtYBJ4N1WgVj2eALSKaWOSI1crpzkzEfEqpcLFJwQqzLjejm1Z1mzCvOMbthzOgQwVxSZMLiPPOR7EtbBI7QGN3fPKZnkE05a9vG39ZNC%2F7%2BhkE6%2FKvb5VMTVaeL98%2Fvj1dzzPK95xg6IZPROwpXXZtaGIpHtz7eUDWSv5qGABvoNNzSt4xARETgTElE6bDwX7VVbWSo%2BBYBxwn1upB0jX%2FRyMNq6%2F9IGOqUByiCfEkjL9FokDjtANdyn5LuqMWLyTMpUlhPesze7MAh5QsSLctDomOWAScEYY%2BVwSsHQOiPxJ%2BlMXVxOxCsRkCiWbfVEE9f0d1W9Rd2v%2B9B5i60G82n6bZjsYFIkBmInFhucukd%2BRvaJfZKaHxcFgSdqCVhnDdD9COa0v1kmV%2BuLLNdqcJZrOnb3HBfFDgbRkksFcV3p97HFhGJOmDBRjzXirQwt&X-Amz-Signature=dac640429638b601ca386fe2fa602711b7a2c89fb2cd01de8aab2eb7331e4858&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

同学们大家好，这章节我们来介绍一下我们的面试题，关于 string did Redis 与 Redis 之间的关系。对于 Redis 大家可能比较熟悉， Redis 是 Redis 的一个客户端，它基于 BL 实现的。对于Jadis，它包含几个核心的类，比如与服务进行交互，比如像 Jadis cluster，我们的 third Jadis，即 Jadis pool 和 Jadis Sentinel pool，以以及 seed Jadis 铺对这些我们首先没有去深入的介绍，那我们应该知道 Jadis 它里面包含的一些内容。


对于Jadis，它对 Redis 这些命令的封装，包括一些数据操作的命令，哨兵相关的命令，集群相关的命令。刚我们刚才介绍对应的几个客户端 Redis 对象，它封装了 Redis 服务的一个connection，其实这里面我们可以把 Redis 理解为我们的对应的JDBC，对于基于 GDB seed 协议完成了对于 Redis 也就是对于数据库的封装，这样去想象，去想， GDBC 实现了对于关于性数据库的一个读取的一个驱动的一个协议。定义 Redis 是封装了 Redis 这些命令，这样的话就是他们你可以这样去类比他们这样一个关系。对于Redis，他因为封装了 Redis 夫妻的connection，因此它只能执行 Redis 服务器相关的一些命令。


对于需要在 Redis 的 Sentinel 执行的命令，需要采用的是 status Sentinel 的对象， Redis center 对象封装了客户端与 Redis center 之间的一些链接，也就是说它通过不同的对象连接不同的服务。需要执行的比如说跟集群相关的一些操作，比如 Redis cracks 相关的命令，我们只需要使用 jettispcase 相关的一些对象。对于我们这些client，它对于 Jedis client 都是用于封装 that is 与服务器的一些链接。client，我们利用 Clacson 执行，我们发送了一些 Sensor 相关的一些命令。跟 Redis 相关的一些命令，除了向服务端发送命令以外，它还会执行一些像鉴权、链接、指定数据库等相关的一些操作。


了解完Redis，我们来再看 spring day 的Redis，其实这里面 spring day 的 Redis 跟我们 spring day 的JPA，它实现的功能是有些类似的。首先 spring day 的Redis，它是基于 spring day 的 key value 的一个抽象，完成了对于 spring day 的，也就是跟 Redis 相关的一个关系。对于 string day 的Redis，它是建立了一种规范，但是它具体跟 Redis 之间的关系还需要对应的 collection 进行完成。这里 clicks 我们可以选择 Jadis 或者是class。对于死命地的Redis，官方会倾向于我们选择Clarix。对于 Jadis 跟 clarx 之间的关系，我们可以理解为它都是一个客户端。这里面 Jadis 与 string d 的 Redis 的关系就是说其实我们 spring day 的 Redis 依赖Redis，构成了跟 Redis 客户端进行链接的操作。


spring day 的 Redis 它还完成了一些特殊的一些功能，比如说对应的斯文蒂的，对应的 Redis repose three 完成一些 KV 相关的一些操作，同时它也定义了一些注解，方便我们进行对于的实体模型跟 Redis 进行一个映射，我们知道 Java 的对象，它的特征相对来说是比较立体化的。


对于 Redis 我们更多的去认为它是一个 KV 形式的一个数据结构，当然它还支持一些哈 c 和set，z， set 等等这样一些数据结构，所以说我们跟它的这些映射关系还需要一些更多的一些注解的方式，或者说其他特征的方式进行去描述。所以说 string t 的 Redis 进行跟 Redis 操作的过程中，我们可以使用的更灵活，或者说是我们的规范性会更好一些。关于 string day 的 Redis 与 Redis 的关系，我们就先介绍到这里，同学们，我们下一章节再见。


