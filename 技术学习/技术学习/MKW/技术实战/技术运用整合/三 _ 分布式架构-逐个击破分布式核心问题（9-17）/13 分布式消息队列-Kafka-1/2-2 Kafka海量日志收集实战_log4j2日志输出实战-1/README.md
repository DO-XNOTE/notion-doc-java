---
title: 2-2 Kafka海量日志收集实战_log4j2日志输出实战-1
---

# 2-2 Kafka海量日志收集实战_log4j2日志输出实战-1

[image](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/5dab5175-f0c8-4728-ad19-9f039afb070e/SCR-20240807-gdng.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662M5AOVC4%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T225324Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCyGa12CBy5xiMjQClGuDDN3iArSCSeniqh1hve9kUz0QIhAKEkFzmiYdU7t6JcqeZqJ6XgX%2FV3gXx5EMJh6T9PBcdlKogECMb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1Igwu%2BgmnF1MaCVCOUmAq3ANTIcvSEULQVRA9wCKeuB76O2l%2BfkyFDqdCvBGnbVoqfTaUm%2FUiz4IRrUCdjHCRGpzoYdeRGIVauS6uH6kRdSYG19trL35SWFGDjV7bq5oKvhLdzvDjQjjM8869Q6BbTHtA00iksTshiZ%2BTvQ3jOQy%2FT%2Fs2wqFSH0s3AJr6YO0A4weq4RmQckT0A4c%2Fz9FnkWcdmUkpeZ38E3W80au1%2F%2BdoGgEwrRKigfpGzjQzAI51BZMJeuVvS7r8HnQVZ0vrAkWjEqOAYGg2FSljkKI4oKpPUfY2ObcIXpSokv9zDVqIH%2FC9Nwvt6AZVsfso1dn41AIsGZ3BBVRxXP3249jKnu%2BY9PwMyTWUZEC8hLCkGJ3KWjrIQvlm0wcvVOkeVHa2q0xA6GCs%2BhKL1anTDbUCgPkAQpbqscc2hQ%2FVn0NAsgSPwkrJIn7HWsMurcG4IiQzKPjWLYcymbuXJvxCjAqtQ%2FHbgC6N9meKsGyg7qQh1oNTkOTFwCjCPcin9DqzXXm7qNxb76xrEqhGNw4joR98iHPyuI4KZonfACzKWNGA%2B4exEB5mdvkFHnpxvpKz7gBGPKw0g%2Boaiwc4GjuFyaDXBDqLAi8er%2FbFioJTW07LZqs95faLjVoWZygZB0bPGDC8uP%2FSBjqkAfWXWqy9wimFkLF0WKaHYExHUdbd3vXMgYbg%2F08Ljq0w%2BdduoZUFzFcYOYEj2OywfhD%2BMS04CBHMeNI35xFIi5gdY9dNRxpVOH9fEpBebnP0cIFnTPH2sMcenGEYaZoA0IHAp7gN9CizEUutBMdbc40w0U07BisdI90axdwmSb66eYBPXKpH90hi%2FtaUulGW%2BNGaqbzgKsW%2Fqzsj0WNs3uGbvDXE&X-Amz-Signature=2fb81e6d67f56a59b890b23fe678c74e499695787a05beb2bec4637f73c2e16c&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

[image](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/68ad4ae3-1cc3-44d9-a821-68753de549f9/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662M5AOVC4%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T225324Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCyGa12CBy5xiMjQClGuDDN3iArSCSeniqh1hve9kUz0QIhAKEkFzmiYdU7t6JcqeZqJ6XgX%2FV3gXx5EMJh6T9PBcdlKogECMb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1Igwu%2BgmnF1MaCVCOUmAq3ANTIcvSEULQVRA9wCKeuB76O2l%2BfkyFDqdCvBGnbVoqfTaUm%2FUiz4IRrUCdjHCRGpzoYdeRGIVauS6uH6kRdSYG19trL35SWFGDjV7bq5oKvhLdzvDjQjjM8869Q6BbTHtA00iksTshiZ%2BTvQ3jOQy%2FT%2Fs2wqFSH0s3AJr6YO0A4weq4RmQckT0A4c%2Fz9FnkWcdmUkpeZ38E3W80au1%2F%2BdoGgEwrRKigfpGzjQzAI51BZMJeuVvS7r8HnQVZ0vrAkWjEqOAYGg2FSljkKI4oKpPUfY2ObcIXpSokv9zDVqIH%2FC9Nwvt6AZVsfso1dn41AIsGZ3BBVRxXP3249jKnu%2BY9PwMyTWUZEC8hLCkGJ3KWjrIQvlm0wcvVOkeVHa2q0xA6GCs%2BhKL1anTDbUCgPkAQpbqscc2hQ%2FVn0NAsgSPwkrJIn7HWsMurcG4IiQzKPjWLYcymbuXJvxCjAqtQ%2FHbgC6N9meKsGyg7qQh1oNTkOTFwCjCPcin9DqzXXm7qNxb76xrEqhGNw4joR98iHPyuI4KZonfACzKWNGA%2B4exEB5mdvkFHnpxvpKz7gBGPKw0g%2Boaiwc4GjuFyaDXBDqLAi8er%2FbFioJTW07LZqs95faLjVoWZygZB0bPGDC8uP%2FSBjqkAfWXWqy9wimFkLF0WKaHYExHUdbd3vXMgYbg%2F08Ljq0w%2BdduoZUFzFcYOYEj2OywfhD%2BMS04CBHMeNI35xFIi5gdY9dNRxpVOH9fEpBebnP0cIFnTPH2sMcenGEYaZoA0IHAp7gN9CizEUutBMdbc40w0U07BisdI90axdwmSb66eYBPXKpH90hi%2FtaUulGW%2BNGaqbzgKsW%2Fqzsj0WNs3uGbvDXE&X-Amz-Signature=43d1c03e970db748bbb99983a7d87a14ae29feea271f83070d9a80c9767a41aa&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

[image](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/e7ff8aa3-da1c-4313-9332-a9bc7e7efcfc/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662M5AOVC4%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T225324Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCyGa12CBy5xiMjQClGuDDN3iArSCSeniqh1hve9kUz0QIhAKEkFzmiYdU7t6JcqeZqJ6XgX%2FV3gXx5EMJh6T9PBcdlKogECMb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1Igwu%2BgmnF1MaCVCOUmAq3ANTIcvSEULQVRA9wCKeuB76O2l%2BfkyFDqdCvBGnbVoqfTaUm%2FUiz4IRrUCdjHCRGpzoYdeRGIVauS6uH6kRdSYG19trL35SWFGDjV7bq5oKvhLdzvDjQjjM8869Q6BbTHtA00iksTshiZ%2BTvQ3jOQy%2FT%2Fs2wqFSH0s3AJr6YO0A4weq4RmQckT0A4c%2Fz9FnkWcdmUkpeZ38E3W80au1%2F%2BdoGgEwrRKigfpGzjQzAI51BZMJeuVvS7r8HnQVZ0vrAkWjEqOAYGg2FSljkKI4oKpPUfY2ObcIXpSokv9zDVqIH%2FC9Nwvt6AZVsfso1dn41AIsGZ3BBVRxXP3249jKnu%2BY9PwMyTWUZEC8hLCkGJ3KWjrIQvlm0wcvVOkeVHa2q0xA6GCs%2BhKL1anTDbUCgPkAQpbqscc2hQ%2FVn0NAsgSPwkrJIn7HWsMurcG4IiQzKPjWLYcymbuXJvxCjAqtQ%2FHbgC6N9meKsGyg7qQh1oNTkOTFwCjCPcin9DqzXXm7qNxb76xrEqhGNw4joR98iHPyuI4KZonfACzKWNGA%2B4exEB5mdvkFHnpxvpKz7gBGPKw0g%2Boaiwc4GjuFyaDXBDqLAi8er%2FbFioJTW07LZqs95faLjVoWZygZB0bPGDC8uP%2FSBjqkAfWXWqy9wimFkLF0WKaHYExHUdbd3vXMgYbg%2F08Ljq0w%2BdduoZUFzFcYOYEj2OywfhD%2BMS04CBHMeNI35xFIi5gdY9dNRxpVOH9fEpBebnP0cIFnTPH2sMcenGEYaZoA0IHAp7gN9CizEUutBMdbc40w0U07BisdI90axdwmSb66eYBPXKpH90hi%2FtaUulGW%2BNGaqbzgKsW%2Fqzsj0WNs3uGbvDXE&X-Amz-Signature=154c572e4278dc89e362a10b0ecb389437c7ede43b378008f562ef91361054d2&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

OK 小伙伴们，大家好，咱们继续。上节课我们已经把整个的这个海量日志收集的技术架构跟大家讲一下。那这节课开始，我们就一同念去对它进行一个实际的这个实战应用，把它进行一个落地。首先我们其实大家想一想，从这个日志收集到采集过滤，然后到最后把它落地到 Elasticsearch 中。最后用 kibana 展示这一套流程，那肯定是从最开始。比如说我们首先得看一看自己的应用服务，我们自己要采集的这个数据源应该怎么去做一个实际的这个实战落地对吧。接下来我们就从这个 App 我们的应用服务开始说起。那这也是我们进入这个日志输出的课程的讲解。


首先我们领着大家来熟悉一个小的组件，叫做 log4j2 , 


其实相信大家不陌生，那如果你对它比较陌生，sl4j 的话应该肯定不陌生，它是一个接口规范，它下面有好多好多不同的实现，比如说 logback 比如说 log4j 还比如说现在我们所看到的这个 log4j2 第二版本的,对应着 log4j 与 log4j2 的区别，就是说 log4j2 它底层采用了这个 LMAX公司 高效的无锁内存队列的 disruptor 框架，对这个日志收集做了一性能的一些优化调优，提升了它这个日志输出的吞吐量，从而其实也是这方面去考量了一个这个高性能目的。


当然对于这个** ****log4j****2**** **，它目前使用起来其实也是更方便。但是有一个问题就是说它在实际应用的时候，如果你自己的服务器性能不是特别好的话，它这个日收集会占用很多的这个服务器资源，比如说像CPU 、内存这都是有所损耗的。其原因本质上就是因为引入了这个 disruptor， 因为 disruptor 它本身是非常耗性能的。它首先内存是一个预加载机制，并且它是一个 RingBuffer 环形的数组，而且它底层是采用无锁的， 你可以认为是类似于这个 CAS 当然它有各种各样的无锁的策略 strategy 比如说 blocking strategy 还有这个 ill 的 city 就线程的让步的 strategy 还有等等一些，比如 timeout strategy， sleep strategy 等等很多。如果感兴趣的话，大家可以去看一看这个 disrupter 。


Log4j2 的最大优势在于它的性能。它采用了 Disruptor 来处理异步模式，Disruptor 是一个无锁的线程间通信库，它代替了 logback 和 log4j 之前的队列，使并发性能大大提升。此外，Log4j2 还可以减少垃圾收集器的压力，支持 Lambda 表达式，并且支持自动重载配置¹⁵。

源: 与必应的对话， 2023/5/7
(1) 高性能日志工具Log4j2的优点有哪些 - 编程语言 - 亿速云. [https://bing.com/search?q=Log4j2+优势](https://bing.com/search?q=Log4j2%20%E4%BC%98%E5%8A%BF).
(2) 高性能日志工具Log4j2的优点有哪些 - 编程语言 - 亿速云. [https://www.yisu.com/zixun/530456.html](https://www.yisu.com/zixun/530456.html).
(3) 日志框架选型，Logback 还是 Log4j2？ - 知乎 - 知乎专栏. [https://zhuanlan.zhihu.com/p/196630772](https://zhuanlan.zhihu.com/p/196630772).
(4) log4j2性能优势_log4j2 优点_走过程序员的路的博客-CSDN博客. [https://blog.csdn.net/lafengwnagzi/article/details/102987155](https://blog.csdn.net/lafengwnagzi/article/details/102987155).
(5) Log4j优点(配置)_码割机的博客-CSDN博客. [https://blog.csdn.net/u013019820/article/details/59126209](https://blog.csdn.net/u013019820/article/details/59126209).
(6) logback log4j log4j2 性能实测 - 程序员自我修养张振力 - 博客园. [https://www.cnblogs.com/java-zzl/p/10026563.html](https://www.cnblogs.com/java-zzl/p/10026563.html).


好了，那我们从 log4j 说起。首先第一点我们要解决的一个问题就是怎么样对它进行一个日志输出对吧？

[image](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/7d2eee09-95b8-4897-ae53-6b23d76d7f65/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662M5AOVC4%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T225324Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCyGa12CBy5xiMjQClGuDDN3iArSCSeniqh1hve9kUz0QIhAKEkFzmiYdU7t6JcqeZqJ6XgX%2FV3gXx5EMJh6T9PBcdlKogECMb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1Igwu%2BgmnF1MaCVCOUmAq3ANTIcvSEULQVRA9wCKeuB76O2l%2BfkyFDqdCvBGnbVoqfTaUm%2FUiz4IRrUCdjHCRGpzoYdeRGIVauS6uH6kRdSYG19trL35SWFGDjV7bq5oKvhLdzvDjQjjM8869Q6BbTHtA00iksTshiZ%2BTvQ3jOQy%2FT%2Fs2wqFSH0s3AJr6YO0A4weq4RmQckT0A4c%2Fz9FnkWcdmUkpeZ38E3W80au1%2F%2BdoGgEwrRKigfpGzjQzAI51BZMJeuVvS7r8HnQVZ0vrAkWjEqOAYGg2FSljkKI4oKpPUfY2ObcIXpSokv9zDVqIH%2FC9Nwvt6AZVsfso1dn41AIsGZ3BBVRxXP3249jKnu%2BY9PwMyTWUZEC8hLCkGJ3KWjrIQvlm0wcvVOkeVHa2q0xA6GCs%2BhKL1anTDbUCgPkAQpbqscc2hQ%2FVn0NAsgSPwkrJIn7HWsMurcG4IiQzKPjWLYcymbuXJvxCjAqtQ%2FHbgC6N9meKsGyg7qQh1oNTkOTFwCjCPcin9DqzXXm7qNxb76xrEqhGNw4joR98iHPyuI4KZonfACzKWNGA%2B4exEB5mdvkFHnpxvpKz7gBGPKw0g%2Boaiwc4GjuFyaDXBDqLAi8er%2FbFioJTW07LZqs95faLjVoWZygZB0bPGDC8uP%2FSBjqkAfWXWqy9wimFkLF0WKaHYExHUdbd3vXMgYbg%2F08Ljq0w%2BdduoZUFzFcYOYEj2OywfhD%2BMS04CBHMeNI35xFIi5gdY9dNRxpVOH9fEpBebnP0cIFnTPH2sMcenGEYaZoA0IHAp7gN9CizEUutBMdbc40w0U07BisdI90axdwmSb66eYBPXKpH90hi%2FtaUulGW%2BNGaqbzgKsW%2Fqzsj0WNs3uGbvDXE&X-Amz-Signature=f72eaaf0ab6a8f795b52865ac37b4932ce222c4910e2571a85a89a19b63a127b&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

 OK 那肯定我们需要用到的是一个小插件。而这个插件相信大家在实际工作中经常会用，就是 lombok 然后接下来往下去看，就是说我要怎么去对日志做一个分级，这什么意思？日志分级的意思就是说比如说我的 info 级的日志我打到哪里对不对？我的 warning 级的日志我打到哪里？还有我的 error 级别的日志我也想把它打到哪里。那这个就是一个日志分级，在实际的工作中，其实对于特别细溜的日分级没有太大的必要。后面我会跟大家去讲到，真正日志分级应该怎么去划分比较有意义。Ok.然后接下来我们再往下看。那对于日志的这个过滤，也就是说我们如何去对日志做一个过滤对吧，就是我们的日志我想需要的我才去收集它，不需要的我可能我就不去收集它了。那这个就是一个日志的  filter 日志的过滤。


然后接下来跟大家介绍一个比较关键的点，这个不能说是 log4j2 的特性了，是 sl4j 就是这个框架它有一个最核心的一个功能，就是我们的 mdc, mdc 是什么呢？你可以认为它是在日志里边的一个 Thread Local 这个变量，

只不过它这个 Theadlocal 比较特殊，它是跟着每一个线程来的。那这个 mdc 有什么作用呢？其实你可以理解为每一次请求后面我们肯定会执行某一些方法。然后在方法上，比如说在代码里边，业务代码里面我们会打一些这个 log 日志出来对吧？那这些日志它可以去都记录到一次 mdc 也就是说一次线程的局部变量里边。这个就是一个 mbc, mdc 有什么作用呢？就是说我们在打日志的时候，如果有一些特殊的变量，我们想去输出到日志里边，那我们可以把它直接 put 到 MDC 里。


mdc 大家可以理解为它是一个不可写的不可变的一个 map 当我们的这个 log4j2 ,event log4j2 这个对象就是日志对象，一旦创建好之后，它里面的内容就是完全是不可变了。然后你可以在这里边。当然其实是之前，就是我在日志收集之前，我可以去往 mdc 里边去 put 很多很多内容，当然一旦他去做收集了这个动作的时候，他就不可变了。


OK 这是关于 mdc 的一个介绍。那其实这节课我们就通过围绕着这四点，通过输出日志分级以及过滤和 mbc 跟大家去完成一个分布式日志收集海量日数及高通投量实战的第一个小环节，就是说对于日志这一块。好了，那么我们介绍完了这个主题之后，我们马上去进入我们的实战环节。

[file](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/4bf6c2eb-b922-4330-b69e-336a19014681/FastJsonConvertUtil.java?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662M5AOVC4%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T225324Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCyGa12CBy5xiMjQClGuDDN3iArSCSeniqh1hve9kUz0QIhAKEkFzmiYdU7t6JcqeZqJ6XgX%2FV3gXx5EMJh6T9PBcdlKogECMb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1Igwu%2BgmnF1MaCVCOUmAq3ANTIcvSEULQVRA9wCKeuB76O2l%2BfkyFDqdCvBGnbVoqfTaUm%2FUiz4IRrUCdjHCRGpzoYdeRGIVauS6uH6kRdSYG19trL35SWFGDjV7bq5oKvhLdzvDjQjjM8869Q6BbTHtA00iksTshiZ%2BTvQ3jOQy%2FT%2Fs2wqFSH0s3AJr6YO0A4weq4RmQckT0A4c%2Fz9FnkWcdmUkpeZ38E3W80au1%2F%2BdoGgEwrRKigfpGzjQzAI51BZMJeuVvS7r8HnQVZ0vrAkWjEqOAYGg2FSljkKI4oKpPUfY2ObcIXpSokv9zDVqIH%2FC9Nwvt6AZVsfso1dn41AIsGZ3BBVRxXP3249jKnu%2BY9PwMyTWUZEC8hLCkGJ3KWjrIQvlm0wcvVOkeVHa2q0xA6GCs%2BhKL1anTDbUCgPkAQpbqscc2hQ%2FVn0NAsgSPwkrJIn7HWsMurcG4IiQzKPjWLYcymbuXJvxCjAqtQ%2FHbgC6N9meKsGyg7qQh1oNTkOTFwCjCPcin9DqzXXm7qNxb76xrEqhGNw4joR98iHPyuI4KZonfACzKWNGA%2B4exEB5mdvkFHnpxvpKz7gBGPKw0g%2Boaiwc4GjuFyaDXBDqLAi8er%2FbFioJTW07LZqs95faLjVoWZygZB0bPGDC8uP%2FSBjqkAfWXWqy9wimFkLF0WKaHYExHUdbd3vXMgYbg%2F08Ljq0w%2BdduoZUFzFcYOYEj2OywfhD%2BMS04CBHMeNI35xFIi5gdY9dNRxpVOH9fEpBebnP0cIFnTPH2sMcenGEYaZoA0IHAp7gN9CizEUutBMdbc40w0U07BisdI90axdwmSb66eYBPXKpH90hi%2FtaUulGW%2BNGaqbzgKsW%2Fqzsj0WNs3uGbvDXE&X-Amz-Signature=763bd974cb86b414763d29ca10ae0da0847655547f6fe9273c9ba710e5032990&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

[file](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/61341d88-4951-4111-a1a3-9e973610d876/InputMDC.java?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662M5AOVC4%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T225324Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCyGa12CBy5xiMjQClGuDDN3iArSCSeniqh1hve9kUz0QIhAKEkFzmiYdU7t6JcqeZqJ6XgX%2FV3gXx5EMJh6T9PBcdlKogECMb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1Igwu%2BgmnF1MaCVCOUmAq3ANTIcvSEULQVRA9wCKeuB76O2l%2BfkyFDqdCvBGnbVoqfTaUm%2FUiz4IRrUCdjHCRGpzoYdeRGIVauS6uH6kRdSYG19trL35SWFGDjV7bq5oKvhLdzvDjQjjM8869Q6BbTHtA00iksTshiZ%2BTvQ3jOQy%2FT%2Fs2wqFSH0s3AJr6YO0A4weq4RmQckT0A4c%2Fz9FnkWcdmUkpeZ38E3W80au1%2F%2BdoGgEwrRKigfpGzjQzAI51BZMJeuVvS7r8HnQVZ0vrAkWjEqOAYGg2FSljkKI4oKpPUfY2ObcIXpSokv9zDVqIH%2FC9Nwvt6AZVsfso1dn41AIsGZ3BBVRxXP3249jKnu%2BY9PwMyTWUZEC8hLCkGJ3KWjrIQvlm0wcvVOkeVHa2q0xA6GCs%2BhKL1anTDbUCgPkAQpbqscc2hQ%2FVn0NAsgSPwkrJIn7HWsMurcG4IiQzKPjWLYcymbuXJvxCjAqtQ%2FHbgC6N9meKsGyg7qQh1oNTkOTFwCjCPcin9DqzXXm7qNxb76xrEqhGNw4joR98iHPyuI4KZonfACzKWNGA%2B4exEB5mdvkFHnpxvpKz7gBGPKw0g%2Boaiwc4GjuFyaDXBDqLAi8er%2FbFioJTW07LZqs95faLjVoWZygZB0bPGDC8uP%2FSBjqkAfWXWqy9wimFkLF0WKaHYExHUdbd3vXMgYbg%2F08Ljq0w%2BdduoZUFzFcYOYEj2OywfhD%2BMS04CBHMeNI35xFIi5gdY9dNRxpVOH9fEpBebnP0cIFnTPH2sMcenGEYaZoA0IHAp7gN9CizEUutBMdbc40w0U07BisdI90axdwmSb66eYBPXKpH90hi%2FtaUulGW%2BNGaqbzgKsW%2Fqzsj0WNs3uGbvDXE&X-Amz-Signature=8400f20a8e9dbde7fd9aeb1517d410c362a17d2b8dd22691052a721ee43858ab&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

[file](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/e01df552-a80d-46ae-b082-fe6c396135e3/NetUtil.java?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662M5AOVC4%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T225324Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCyGa12CBy5xiMjQClGuDDN3iArSCSeniqh1hve9kUz0QIhAKEkFzmiYdU7t6JcqeZqJ6XgX%2FV3gXx5EMJh6T9PBcdlKogECMb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1Igwu%2BgmnF1MaCVCOUmAq3ANTIcvSEULQVRA9wCKeuB76O2l%2BfkyFDqdCvBGnbVoqfTaUm%2FUiz4IRrUCdjHCRGpzoYdeRGIVauS6uH6kRdSYG19trL35SWFGDjV7bq5oKvhLdzvDjQjjM8869Q6BbTHtA00iksTshiZ%2BTvQ3jOQy%2FT%2Fs2wqFSH0s3AJr6YO0A4weq4RmQckT0A4c%2Fz9FnkWcdmUkpeZ38E3W80au1%2F%2BdoGgEwrRKigfpGzjQzAI51BZMJeuVvS7r8HnQVZ0vrAkWjEqOAYGg2FSljkKI4oKpPUfY2ObcIXpSokv9zDVqIH%2FC9Nwvt6AZVsfso1dn41AIsGZ3BBVRxXP3249jKnu%2BY9PwMyTWUZEC8hLCkGJ3KWjrIQvlm0wcvVOkeVHa2q0xA6GCs%2BhKL1anTDbUCgPkAQpbqscc2hQ%2FVn0NAsgSPwkrJIn7HWsMurcG4IiQzKPjWLYcymbuXJvxCjAqtQ%2FHbgC6N9meKsGyg7qQh1oNTkOTFwCjCPcin9DqzXXm7qNxb76xrEqhGNw4joR98iHPyuI4KZonfACzKWNGA%2B4exEB5mdvkFHnpxvpKz7gBGPKw0g%2Boaiwc4GjuFyaDXBDqLAi8er%2FbFioJTW07LZqs95faLjVoWZygZB0bPGDC8uP%2FSBjqkAfWXWqy9wimFkLF0WKaHYExHUdbd3vXMgYbg%2F08Ljq0w%2BdduoZUFzFcYOYEj2OywfhD%2BMS04CBHMeNI35xFIi5gdY9dNRxpVOH9fEpBebnP0cIFnTPH2sMcenGEYaZoA0IHAp7gN9CizEUutBMdbc40w0U07BisdI90axdwmSb66eYBPXKpH90hi%2FtaUulGW%2BNGaqbzgKsW%2Fqzsj0WNs3uGbvDXE&X-Amz-Signature=d92bad31a8af41dbe87f33fea1f65e94943d7bed4f29252709432fec0d6d1ddb&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)


OK 那我现在已经打开了我们这个 idea 工具。然后我在这里右键我新建一个新的 Maven project 在这里边我们由于是想去做日志收集的一个小案例，所以说在这里我们起个名字叫做 com.bfxy 这是我的 group 然后我起一个名字叫做 collector ，collector就表示收集的意思。


好了，那我们这个小项目主要要做什么事情？在这里跟大家说一下，我们把这个不相关，我们先把它 close 掉。然后这里边首先我们所应用的技术栈肯定是 spring boot 对吧既然是 spring boot 并且是 215 这个版本，那我们接下来就对它进行一个编写。那有一些固定的内容，老师就不再重复的再去写一遍了，我们直接把它 copy 过来，在这里老师已经提前准备好了我们的教学案例，所以说就耽误小伙伴们时间 copy 过来。

```java
<?xml version="1.0" encoding="UTF-8"?>
<project xmlns="http://maven.apache.org/POM/4.0.0"
         xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
         xsi:schemaLocation="http://maven.apache.org/POM/4.0.0 http://maven.apache.org/xsd/maven-4.0.0.xsd">
    <modelVersion>4.0.0</modelVersion>

    <groupId>com.bfxy</groupId>
    <artifactId>collector</artifactId>
    <version>1.0-SNAPSHOT</version>


    <parent>
        <groupId>org.springframework.boot</groupId>
        <artifactId>spring-boot-starter-parent</artifactId>
        <version>2.1.5.RELEASE</version>
    </parent>

    <properties>
        <maven.compiler.source>8</maven.compiler.source>
        <maven.compiler.target>8</maven.compiler.target>
    </properties>

    <dependencies>
        <dependency>
            <groupId>org.springframework.boot</groupId>
            <artifactId>spring-boot-starter-web</artifactId>
            <exclusions>
                <exclusion>
                    <groupId>org.springframework.boot</groupId>
                    <artifactId>spring-boot-starter-logging</artifactId>
                </exclusion>
            </exclusions>
        </dependency>

        <dependency>
            <groupId>org.springframework.boot</groupId>
            <artifactId>spring-boot-starter-test</artifactId>
        </dependency>

        <!-- log4j2 -->
        <dependency>
            <groupId>org.springframework.boot</groupId>
            <artifactId>spring-boot-starter-log4j2</artifactId>
        </dependency>

        <!-- disruptor  -->
        <dependency>
            <groupId>com.lmax</groupId>
            <artifactId>disruptor</artifactId>
            <version>3.3.4</version>
        </dependency>

        <dependency>
            <groupId>com.alibaba</groupId>
            <artifactId>fastjson</artifactId>
            <version>1.2.83</version>
        </dependency>

        <dependency>
            <groupId>org.projectlombok</groupId>
            <artifactId>lombok</artifactId>
        </dependency>
    </dependencies>


</project>
```

首先我们看到了这里，就是说我们自己的什么呢？这是我们自己的这个 215 的这个 parent boot 然后我们把对应的一些依赖 dependency 直接粘过来。然后跟大家简单的来说一下你们有哪些 dependency 好粘过来。然后我们最大化跟大家讲一下。首先第一个就是我们的 spring boot starter web 因为我们是一个 web 工程对吧，我们会用到一些什么 MC 的东西去访问。但是注意在这里面有一个特殊的强调的事情。就在这里打一个注释，就是说我们一定要去 execution 我们要排除 spring boot 默认的。那么默认的这个 start logo 它底层就是我们的 spring 那个 log back 就那个日志的插件，你把它排除出去为什么？因为只有排除出去加上我们自己的 log for G two 才行。注意你在这里看这是 long book 不用说了。


然后我把 log for G two 这个 depending 是依赖进来。接下来还有一个比较关键的就是说因为我们的 log4j2 它是强依赖于 disruptor 的，就是 com.lmax.disruptor 我现在用的是比较新的版本，叫做 3.3.4，这个版本是比较新的，你只有这两个一起去炸包引进来才好用，要不然的话它会报错。就是 class note found exception 他会说你的 disruptor not found


Ok. 最后有一个就是阿里巴巴的 fastjason 会我们去演示一下如果不加这个 Lmax disruptor 会有什么情况？那现在我对于这个麦文的 dependence 已经搞定了，那接下来我们去 update 一下我们的工程麦文 project 好了，已经搞定了之后，我们快速的去进入我们的编码阶段。在这里我去创建一个包，我们叫 com.bfxy 第二 collector 资源。然后在这里面我们的主程序主入口没什么可说的，我就不去写了，直接粘过来。然后我们来看一下打开是不是就是我们的 spring boot application 主入口。
好了，搞定完这个事情之后，我们把对应相关的一些 util 在这里粘过来，因为这些东西没有必要说再领大家重新再敲一遍。那我在这里用了两个最基础的 Util 类，那一个就是 netutil 就比如说如何去获取对应的本机的服务器的 IP 地址端口号的这个代码，你可以理解是 double 它自己底层的这么一个小的工具类，那我可以去直接拿过来，咱们直接可以用。


其实在教大家一个小的学习方法，就是你自己在封装一些 util 工具类的时候，你有没有想过我应该怎么去做？就是好的一个这个工具类封装对不对，可能你自己封装完了之后还会有一些这样那样的小 bug 所以说我建议大家去一些开源框架里边去找 common 或者是 util 包，下面去找一些人家已经帮你去做好了的 util 那些 util 不敢说 100% 没有问题，但是起码他是经历过一些时间验证的，经历过一些测试的。


所以说我还是建议什么呢？大家如果说以后想去做一些通用的工具类，比如说我们 Java 的一些反射这些类，还有这个关于网络相关， IP 地址端口相关，包括一些字符串截取等等 class annotation 相关。那你都可以去很多的开源框架里去找，比如说去 net 里找去 Dubbo 去找，去 rocketMQ 里面去找，或者去一些开源的更优秀的 Java 的开源技术站技术框架里边去找，他都会给你提供一些很好的工具类。在这里跟大家说一下这个学习方法。


然后对于这个 fast 杰森卡沃尔的util ，这个是我们阿里巴巴 fastjson 的一个通用的工具类，这个没什么可说的了。然后接下来我们就快速的去开始进行编码。那接下来我要做的事情是比如说我要再创建一个这个 package 我们叫做 web 这个 web 里边就写我们的 spring MVC 的代码，在这里我们起个名字叫做 index controllerindex controller 那这个 index controller 其实就是我们的一个外部 Mac 的入口了。那很简单。首先第一步就是我们的 rest 退出了。接下来比如说我要打日志我怎么办？我们都知道大家都学了这个 long book 了，所以说你直接加一个 slfg 就可以了。有了这么一个 slfg 的注解之后，然后我们就可以去打真正的 log 了。在这里边我先写一个非常简单的方法，叫做 public string 咱们就叫做 index 方法。这个 index 上面我就先返回一个 index 字符串 idx 好了，然后我写 request mapping 这个 request mapping 里边有一个 value value 我们就叫做 index 就好了。现在我的一个 hello world 的小程序已经写完了，这是 step 基本的一个，非常简单好了。


那现在我如何打日志呢？比如说现在我打三条日志，我们一起看我说 [log.info](http://log.info/) 是不是说我是一条 info 日志？我是一条 info 级别的日志。然后把这个东西我 copy 3 份，这里边我写 money 然后这些 L 对吧，然后我是一条 monitor 日志，我是一条 L 日志。 OK 我现在在这个 index 方法上我打了三个日志对吧，分别是不同的级别的。然后现在难道说我就可以直接去用了吗？不是的，我们现在还没有能够直接用。

[file](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/ec1349e7-655d-4ca1-a056-a62210c20cfb/application.properties?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662M5AOVC4%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T225324Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCyGa12CBy5xiMjQClGuDDN3iArSCSeniqh1hve9kUz0QIhAKEkFzmiYdU7t6JcqeZqJ6XgX%2FV3gXx5EMJh6T9PBcdlKogECMb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1Igwu%2BgmnF1MaCVCOUmAq3ANTIcvSEULQVRA9wCKeuB76O2l%2BfkyFDqdCvBGnbVoqfTaUm%2FUiz4IRrUCdjHCRGpzoYdeRGIVauS6uH6kRdSYG19trL35SWFGDjV7bq5oKvhLdzvDjQjjM8869Q6BbTHtA00iksTshiZ%2BTvQ3jOQy%2FT%2Fs2wqFSH0s3AJr6YO0A4weq4RmQckT0A4c%2Fz9FnkWcdmUkpeZ38E3W80au1%2F%2BdoGgEwrRKigfpGzjQzAI51BZMJeuVvS7r8HnQVZ0vrAkWjEqOAYGg2FSljkKI4oKpPUfY2ObcIXpSokv9zDVqIH%2FC9Nwvt6AZVsfso1dn41AIsGZ3BBVRxXP3249jKnu%2BY9PwMyTWUZEC8hLCkGJ3KWjrIQvlm0wcvVOkeVHa2q0xA6GCs%2BhKL1anTDbUCgPkAQpbqscc2hQ%2FVn0NAsgSPwkrJIn7HWsMurcG4IiQzKPjWLYcymbuXJvxCjAqtQ%2FHbgC6N9meKsGyg7qQh1oNTkOTFwCjCPcin9DqzXXm7qNxb76xrEqhGNw4joR98iHPyuI4KZonfACzKWNGA%2B4exEB5mdvkFHnpxvpKz7gBGPKw0g%2Boaiwc4GjuFyaDXBDqLAi8er%2FbFioJTW07LZqs95faLjVoWZygZB0bPGDC8uP%2FSBjqkAfWXWqy9wimFkLF0WKaHYExHUdbd3vXMgYbg%2F08Ljq0w%2BdduoZUFzFcYOYEj2OywfhD%2BMS04CBHMeNI35xFIi5gdY9dNRxpVOH9fEpBebnP0cIFnTPH2sMcenGEYaZoA0IHAp7gN9CizEUutBMdbc40w0U07BisdI90axdwmSb66eYBPXKpH90hi%2FtaUulGW%2BNGaqbzgKsW%2Fqzsj0WNs3uGbvDXE&X-Amz-Signature=1cacd99fe1dfa697c651a4930637a83924b4ce4d0e24178e7dfb9c3a76fc16a4&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

[file](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/3faacff3-f28b-4019-b7fc-e5475f52abd6/error-log-mapping.json?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662M5AOVC4%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T225324Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCyGa12CBy5xiMjQClGuDDN3iArSCSeniqh1hve9kUz0QIhAKEkFzmiYdU7t6JcqeZqJ6XgX%2FV3gXx5EMJh6T9PBcdlKogECMb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1Igwu%2BgmnF1MaCVCOUmAq3ANTIcvSEULQVRA9wCKeuB76O2l%2BfkyFDqdCvBGnbVoqfTaUm%2FUiz4IRrUCdjHCRGpzoYdeRGIVauS6uH6kRdSYG19trL35SWFGDjV7bq5oKvhLdzvDjQjjM8869Q6BbTHtA00iksTshiZ%2BTvQ3jOQy%2FT%2Fs2wqFSH0s3AJr6YO0A4weq4RmQckT0A4c%2Fz9FnkWcdmUkpeZ38E3W80au1%2F%2BdoGgEwrRKigfpGzjQzAI51BZMJeuVvS7r8HnQVZ0vrAkWjEqOAYGg2FSljkKI4oKpPUfY2ObcIXpSokv9zDVqIH%2FC9Nwvt6AZVsfso1dn41AIsGZ3BBVRxXP3249jKnu%2BY9PwMyTWUZEC8hLCkGJ3KWjrIQvlm0wcvVOkeVHa2q0xA6GCs%2BhKL1anTDbUCgPkAQpbqscc2hQ%2FVn0NAsgSPwkrJIn7HWsMurcG4IiQzKPjWLYcymbuXJvxCjAqtQ%2FHbgC6N9meKsGyg7qQh1oNTkOTFwCjCPcin9DqzXXm7qNxb76xrEqhGNw4joR98iHPyuI4KZonfACzKWNGA%2B4exEB5mdvkFHnpxvpKz7gBGPKw0g%2Boaiwc4GjuFyaDXBDqLAi8er%2FbFioJTW07LZqs95faLjVoWZygZB0bPGDC8uP%2FSBjqkAfWXWqy9wimFkLF0WKaHYExHUdbd3vXMgYbg%2F08Ljq0w%2BdduoZUFzFcYOYEj2OywfhD%2BMS04CBHMeNI35xFIi5gdY9dNRxpVOH9fEpBebnP0cIFnTPH2sMcenGEYaZoA0IHAp7gN9CizEUutBMdbc40w0U07BisdI90axdwmSb66eYBPXKpH90hi%2FtaUulGW%2BNGaqbzgKsW%2Fqzsj0WNs3uGbvDXE&X-Amz-Signature=d09cd3d0d667f29c61b8994736c5fb95a8f23d0db9e76ac567fd7f5303a4b80c&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

[file](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/0dcdc467-b542-4746-83e3-1c32182e0b9b/log4j2.xml?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662M5AOVC4%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T225324Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCyGa12CBy5xiMjQClGuDDN3iArSCSeniqh1hve9kUz0QIhAKEkFzmiYdU7t6JcqeZqJ6XgX%2FV3gXx5EMJh6T9PBcdlKogECMb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1Igwu%2BgmnF1MaCVCOUmAq3ANTIcvSEULQVRA9wCKeuB76O2l%2BfkyFDqdCvBGnbVoqfTaUm%2FUiz4IRrUCdjHCRGpzoYdeRGIVauS6uH6kRdSYG19trL35SWFGDjV7bq5oKvhLdzvDjQjjM8869Q6BbTHtA00iksTshiZ%2BTvQ3jOQy%2FT%2Fs2wqFSH0s3AJr6YO0A4weq4RmQckT0A4c%2Fz9FnkWcdmUkpeZ38E3W80au1%2F%2BdoGgEwrRKigfpGzjQzAI51BZMJeuVvS7r8HnQVZ0vrAkWjEqOAYGg2FSljkKI4oKpPUfY2ObcIXpSokv9zDVqIH%2FC9Nwvt6AZVsfso1dn41AIsGZ3BBVRxXP3249jKnu%2BY9PwMyTWUZEC8hLCkGJ3KWjrIQvlm0wcvVOkeVHa2q0xA6GCs%2BhKL1anTDbUCgPkAQpbqscc2hQ%2FVn0NAsgSPwkrJIn7HWsMurcG4IiQzKPjWLYcymbuXJvxCjAqtQ%2FHbgC6N9meKsGyg7qQh1oNTkOTFwCjCPcin9DqzXXm7qNxb76xrEqhGNw4joR98iHPyuI4KZonfACzKWNGA%2B4exEB5mdvkFHnpxvpKz7gBGPKw0g%2Boaiwc4GjuFyaDXBDqLAi8er%2FbFioJTW07LZqs95faLjVoWZygZB0bPGDC8uP%2FSBjqkAfWXWqy9wimFkLF0WKaHYExHUdbd3vXMgYbg%2F08Ljq0w%2BdduoZUFzFcYOYEj2OywfhD%2BMS04CBHMeNI35xFIi5gdY9dNRxpVOH9fEpBebnP0cIFnTPH2sMcenGEYaZoA0IHAp7gN9CizEUutBMdbc40w0U07BisdI90axdwmSb66eYBPXKpH90hi%2FtaUulGW%2BNGaqbzgKsW%2Fqzsj0WNs3uGbvDXE&X-Amz-Signature=7cf00424bc97363e0848bebac919770d15877555d77deaf4a41680199909a584&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)


我先把两个比较关键的配置文件 copy 过来。首先第一个比较关键的是什么呢？我们自己作为一个 spring boot 工程，那对应着 application.practice 一定会有。然后还有一个就是在 class pass 下，注意都是在 class pass 下。还有一个比较关键的就是我们的 logo four G two.xmail 这个名字就应该叫它 log four G two.x mail 文件。然后我们看第一个 application.promise 也是我们说的是不是就是定义了这个 root pass 还有一个这个启动的 campaign 的端口号8001，对应着一些 spring MVC 的一些默认的配置，比如说 application name 比如说 encoding 比如说一些 jackson 转换的一些东西，比如说我们说的重点，我们主要来看一看 log 复制 to 这个组件我们具体是怎么去做的。


好了，那日志的输出其实咱们同学已经会了，很简单，就是加 log sl 复制这个注解，然后打日志就好了。注意看这个对应着像日志的分级过滤都是在这个 xmail 里边的。首先我们来看一看我们这个 xmail 文件里面都有哪些配置项？首先第一个就是 purpose purpose 里边我可以定一些变量供下面的这个代码去使用，当然它是一个 xnl 的方式。然后这个 log name 什么意思？就是我们的日志输出的目录文件名称 cell name 就是我们日志输出什么样的文件，那我跟这个项目名保持一致，见名字也叫做 collector 好了，然后接下来往下看，有一个叫做 pattern 就是你的日志输出格式是什么样子。那我想按照我这种方式去打一个日志，我这种方式去打一日志。那这种方式其实我把它粘到我们的 index 这个里边大家看的可能更清晰一些，我把它就粘到这里了好，粘到这里大家可以看。首先是一个大括号，一个中括号，中括号杠 D 是不是这个表示时间？然后这个后面加大括号，表示你的时间格式什么样子的。注意我这里边是什么时间。

```java
log4j2.xml
---------------------------------------------------------------------------------------------------------------
<?xml version="1.0" encoding="UTF-8"?>
<Configuration status="INFO" schema="Log4J-V2.0.xsd" monitorInterval="600" >
    <Properties>
        <Property name="LOG_HOME">logs</Property>
        <property name="FILE_NAME">collector</property>
        <property name="patternLayout">[%d{yyyy-MM-dd'T'HH:mm:ss.SSSZZ}] [%level{length=5}] [%thread-%tid] [%logger] [%X{hostName}] [%X{ip}] [%X{applicationName}] [%F,%L,%C,%M] [%m] ## '%ex'%n</property>
    </Properties>
    <Appenders>
        <Console name="CONSOLE" target="SYSTEM_OUT">
            <PatternLayout pattern="${patternLayout}"/>
        </Console>  
        <RollingRandomAccessFile name="appAppender" fileName="${LOG_HOME}/app-${FILE_NAME}.log" filePattern="${LOG_HOME}/app-${FILE_NAME}-%d{yyyy-MM-dd}-%i.log" >
          <PatternLayout pattern="${patternLayout}" />
          <Policies>
              <TimeBasedTriggeringPolicy interval="1"/>
              <SizeBasedTriggeringPolicy size="500MB"/>
          </Policies>
          <DefaultRolloverStrategy max="20"/>         
        </RollingRandomAccessFile>
        <RollingRandomAccessFile name="errorAppender" fileName="${LOG_HOME}/error-${FILE_NAME}.log" filePattern="${LOG_HOME}/error-${FILE_NAME}-%d{yyyy-MM-dd}-%i.log" >
          <PatternLayout pattern="${patternLayout}" />
          <Filters>
              <ThresholdFilter level="warn" onMatch="ACCEPT" onMismatch="DENY"/>
          </Filters>              
          <Policies>
              <TimeBasedTriggeringPolicy interval="1"/>
              <SizeBasedTriggeringPolicy size="500MB"/>
          </Policies>
          <DefaultRolloverStrategy max="20"/>         
        </RollingRandomAccessFile>            
    </Appenders>
    <Loggers>
        <!-- 业务相关 异步logger -->
        <AsyncLogger name="com.bfxy.*" level="info" includeLocation="true">
          <AppenderRef ref="appAppender"/>
        </AsyncLogger>
        <AsyncLogger name="com.bfxy.*" level="info" includeLocation="true">
          <AppenderRef ref="errorAppender"/>
        </AsyncLogger>       
        <Root level="info">
            <Appender-Ref ref="CONSOLE"/>
            <Appender-Ref ref="appAppender"/>
            <AppenderRef ref="errorAppender"/>
        </Root>         
    </Loggers>
</Configuration>
```


udc 就是我们的这个美国那边的时间，不是我们现在的这个北京时间。 OK 为什么这么去做呢？因为其实后面你要把日志收集到 elk 上，因为 elk 的时间是这个 UGC 的时间。好，然后接下来往下看。接下来就是有一个 level 日志的级别是什么，然后是有一个叫做 thread 杠 TID 就是现成的 ID 是什么 logo 日志输出的这一些具体信息。然后看这个杠 X 开头的这三个我现在有三个杠 X 开头的，然后再往下看杠 M 这里面我又打了两个井号，是不是有一个什么有一个单引号，然后有一个杠 ex 还有个杠 N 好，这就是我现在所定义的日志格式。那其实我们按照这种日志格式去打，把日志收集到我们的这个你可以理解为先把日志通过 file bit 收集起来，然后再干什么，然后再扔到卡夫卡。


最后我们的 logstash 是要根据这个格式去解析的，所以说你的格式是至关重要的。在这里没什么可说的。三个杠 X 表示什么呢？就是说这个杠 X 表示说如果我们除了 log 复制给我们自带的一些日志输出还不够用的话，我们可以自定义一些日志输出。当然杠 X 表示自定义这个大括号里边就是你自定义的这个 P 是什么？就是你的 host name 比如说我当前的应用的主机名称、我当前应用的 IP 以及我当前这个应用它的这个 application name 我都可以通过一些方式、一些手段给它填充。好在日志里。 OK 我相信小伙伴们大体上应该能理解了，后面怎么去填充一会再说。

```java
/**
 * <h1></h1>
 */
@Slf4j
@RestController
public class IndexController {

    /**
     * [%d{yyyy-MM-dd'T'HH:mm:ss.SSSZZ}] 
     * [%level{length=5}] 
     * [%thread-%tid] 
     * [%logger] 
     * [%X{hostName}] 
     * [%X{ip}] 
     * [%X{applicationName}] 
     * [%F,%L,%C,%M] 
     * [%m] 
     * ## '%ex'%n
     * 
     * @return
     */
    @RequestMapping(value = "/index")
    public String index( ) {
        log.info("我是一条 info 日志");
        log.warn("我是一条 warn 日志");
        log.error("我是一条 error 日志");

        return "inx";
    }
}
```

然后这个杠 F 杠 L 杠 C 杠 M 是什么呢？对不对？好，相信小伙伴们都有一些疑问，你让我现在说老师，你现在说具体是什么，我也不一定能记住，但是等到日志输出的时候，我们对照看你就知道了。 OK 杠 L 可能是行号，count是这个 master 的就是方法。然后杠 M 这个就是 message 这个 message 代表的什么呢？这个杠 M 就代表里边的这个日志输出里的内容是什么？这个两个井号是我自己特殊约定的，这个单引号也是我自己特殊约定的。为什么我要这样去做？小伙伴们肯定有疑问，但是随着我们的课程逐步的深入，你就没有疑问了。

[image](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/04aa6821-42ea-45c2-855d-a180a6c9a5ff/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662M5AOVC4%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T225324Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCyGa12CBy5xiMjQClGuDDN3iArSCSeniqh1hve9kUz0QIhAKEkFzmiYdU7t6JcqeZqJ6XgX%2FV3gXx5EMJh6T9PBcdlKogECMb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1Igwu%2BgmnF1MaCVCOUmAq3ANTIcvSEULQVRA9wCKeuB76O2l%2BfkyFDqdCvBGnbVoqfTaUm%2FUiz4IRrUCdjHCRGpzoYdeRGIVauS6uH6kRdSYG19trL35SWFGDjV7bq5oKvhLdzvDjQjjM8869Q6BbTHtA00iksTshiZ%2BTvQ3jOQy%2FT%2Fs2wqFSH0s3AJr6YO0A4weq4RmQckT0A4c%2Fz9FnkWcdmUkpeZ38E3W80au1%2F%2BdoGgEwrRKigfpGzjQzAI51BZMJeuVvS7r8HnQVZ0vrAkWjEqOAYGg2FSljkKI4oKpPUfY2ObcIXpSokv9zDVqIH%2FC9Nwvt6AZVsfso1dn41AIsGZ3BBVRxXP3249jKnu%2BY9PwMyTWUZEC8hLCkGJ3KWjrIQvlm0wcvVOkeVHa2q0xA6GCs%2BhKL1anTDbUCgPkAQpbqscc2hQ%2FVn0NAsgSPwkrJIn7HWsMurcG4IiQzKPjWLYcymbuXJvxCjAqtQ%2FHbgC6N9meKsGyg7qQh1oNTkOTFwCjCPcin9DqzXXm7qNxb76xrEqhGNw4joR98iHPyuI4KZonfACzKWNGA%2B4exEB5mdvkFHnpxvpKz7gBGPKw0g%2Boaiwc4GjuFyaDXBDqLAi8er%2FbFioJTW07LZqs95faLjVoWZygZB0bPGDC8uP%2FSBjqkAfWXWqy9wimFkLF0WKaHYExHUdbd3vXMgYbg%2F08Ljq0w%2BdduoZUFzFcYOYEj2OywfhD%2BMS04CBHMeNI35xFIi5gdY9dNRxpVOH9fEpBebnP0cIFnTPH2sMcenGEYaZoA0IHAp7gN9CizEUutBMdbc40w0U07BisdI90axdwmSb66eYBPXKpH90hi%2FtaUulGW%2BNGaqbzgKsW%2Fqzsj0WNs3uGbvDXE&X-Amz-Signature=f709d092b513a498f4ea235c662d906e02960e331d79d98c5b398b36e3242bd0&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

这个 ex 有什么呢？就如果说抛异常的时候，我们应该怎么去抛异常的信息会打到这里边，这是一个战略符号，杠 N 就是换行，没什么可说的。好了，现在我们已经把我们的日志跟大家讲清楚了，大体上是这么一个格式。好了，我们继续往下去看，我的 pattern 有了。然后这里边首先我有三个，你可以理解为我有三个 append appendos 就表示这里边会装一些 appendappend 就表示输出的组件。那第一个叫做 cancel 就是输出到控制台的，它是以这个 pattern 输出的格式是这样的。然后它的 target 是 system.output 还有一个叫做 running random access file 那它我给它起个名字叫做 App a panda 然后你看他的 file name 是什么样子的？是以 dollar 符号 log 杠 home 就是我们这个 logs 为一个目录。然后下面的文件是什么呢？是 App 我写死了，看见了吗？ App 杠 cell name 我的 cell name 叫什么？我的 cell name 叫 collector 就是你的应用服务的名称对不对？那就是说他最后输出的日志文件就是 App 杠 collector 然后这个叫做 fail pattern 什么意思？就是说我在可以对它加一些时间，就是你这个日志到底是什么节点年月日，然后输出第几个对不对？ ok1 会我们看下效果。然后接下来对应的一些 pattern 还有一些策略，这些策略都是很简单，大家可以看一看多少兆的时候，500兆一个文件对吧。 Ok. 然后再往下看。


第二一个叫做 rolling random access 也是一样的。但是这里我给它起个名叫做 error 潘多。这个 error 潘多它的是以什么开头的？是以 error 杠 32 名称开头的，然后他是怎么去输出呢？也是 L 杠 file name 然后加上您的日以及第几个 log 文件。
OK 没什么可说的，这两个是我们核心的输出，一个是输出我们全量的日志，还有一个是输出我们的错误的日志。为什么这么说？因为同学们请看这里边我加了一个 filter 我加了一个 filter 就是 through 的 filter 就是允许通过的是不是它是相当于一个过滤器一样，它内置的一个组件就是说 level 是 warning 级别以上的，如果是 warning 级别以上的我才去 accept 就是 on match accept 要不然就禁用，就是说 warning 级别的我这个组件才收集 warning 级别以下的我是不收集的。你可以理解为这个过滤器非常的简单。

[image](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/548f3666-467a-4d10-a2ac-9d4a79531cb5/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662M5AOVC4%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T225324Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCyGa12CBy5xiMjQClGuDDN3iArSCSeniqh1hve9kUz0QIhAKEkFzmiYdU7t6JcqeZqJ6XgX%2FV3gXx5EMJh6T9PBcdlKogECMb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1Igwu%2BgmnF1MaCVCOUmAq3ANTIcvSEULQVRA9wCKeuB76O2l%2BfkyFDqdCvBGnbVoqfTaUm%2FUiz4IRrUCdjHCRGpzoYdeRGIVauS6uH6kRdSYG19trL35SWFGDjV7bq5oKvhLdzvDjQjjM8869Q6BbTHtA00iksTshiZ%2BTvQ3jOQy%2FT%2Fs2wqFSH0s3AJr6YO0A4weq4RmQckT0A4c%2Fz9FnkWcdmUkpeZ38E3W80au1%2F%2BdoGgEwrRKigfpGzjQzAI51BZMJeuVvS7r8HnQVZ0vrAkWjEqOAYGg2FSljkKI4oKpPUfY2ObcIXpSokv9zDVqIH%2FC9Nwvt6AZVsfso1dn41AIsGZ3BBVRxXP3249jKnu%2BY9PwMyTWUZEC8hLCkGJ3KWjrIQvlm0wcvVOkeVHa2q0xA6GCs%2BhKL1anTDbUCgPkAQpbqscc2hQ%2FVn0NAsgSPwkrJIn7HWsMurcG4IiQzKPjWLYcymbuXJvxCjAqtQ%2FHbgC6N9meKsGyg7qQh1oNTkOTFwCjCPcin9DqzXXm7qNxb76xrEqhGNw4joR98iHPyuI4KZonfACzKWNGA%2B4exEB5mdvkFHnpxvpKz7gBGPKw0g%2Boaiwc4GjuFyaDXBDqLAi8er%2FbFioJTW07LZqs95faLjVoWZygZB0bPGDC8uP%2FSBjqkAfWXWqy9wimFkLF0WKaHYExHUdbd3vXMgYbg%2F08Ljq0w%2BdduoZUFzFcYOYEj2OywfhD%2BMS04CBHMeNI35xFIi5gdY9dNRxpVOH9fEpBebnP0cIFnTPH2sMcenGEYaZoA0IHAp7gN9CizEUutBMdbc40w0U07BisdI90axdwmSb66eYBPXKpH90hi%2FtaUulGW%2BNGaqbzgKsW%2Fqzsj0WNs3uGbvDXE&X-Amz-Signature=601285e93d627dacac106539c547f1709bbc770edcb87425895a9abcaab1bcaf&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)


Ok. 好了，那其实通过这个语义咱们都知道，这里边上面一个 App abandon 它是不做任何条件限制的，就是全量的日志我都会进行收集。那下面是 warning 级别以上的日志我才进行收集。那这个就是我们自己日志的分级的策略，也就是说我有一个全量的日志，还有一个 L 的日志，只要是打 warning 级别以上，我给它输出到一个文件里边，全量的日志我也给它输出到另外一个文件里面。那也就是说我们日志收集的时候最终会有两个文件。

[image](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/9e1b19b5-16aa-4576-8b9a-6fd8d3a528ad/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662M5AOVC4%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T225324Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCyGa12CBy5xiMjQClGuDDN3iArSCSeniqh1hve9kUz0QIhAKEkFzmiYdU7t6JcqeZqJ6XgX%2FV3gXx5EMJh6T9PBcdlKogECMb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1Igwu%2BgmnF1MaCVCOUmAq3ANTIcvSEULQVRA9wCKeuB76O2l%2BfkyFDqdCvBGnbVoqfTaUm%2FUiz4IRrUCdjHCRGpzoYdeRGIVauS6uH6kRdSYG19trL35SWFGDjV7bq5oKvhLdzvDjQjjM8869Q6BbTHtA00iksTshiZ%2BTvQ3jOQy%2FT%2Fs2wqFSH0s3AJr6YO0A4weq4RmQckT0A4c%2Fz9FnkWcdmUkpeZ38E3W80au1%2F%2BdoGgEwrRKigfpGzjQzAI51BZMJeuVvS7r8HnQVZ0vrAkWjEqOAYGg2FSljkKI4oKpPUfY2ObcIXpSokv9zDVqIH%2FC9Nwvt6AZVsfso1dn41AIsGZ3BBVRxXP3249jKnu%2BY9PwMyTWUZEC8hLCkGJ3KWjrIQvlm0wcvVOkeVHa2q0xA6GCs%2BhKL1anTDbUCgPkAQpbqscc2hQ%2FVn0NAsgSPwkrJIn7HWsMurcG4IiQzKPjWLYcymbuXJvxCjAqtQ%2FHbgC6N9meKsGyg7qQh1oNTkOTFwCjCPcin9DqzXXm7qNxb76xrEqhGNw4joR98iHPyuI4KZonfACzKWNGA%2B4exEB5mdvkFHnpxvpKz7gBGPKw0g%2Boaiwc4GjuFyaDXBDqLAi8er%2FbFioJTW07LZqs95faLjVoWZygZB0bPGDC8uP%2FSBjqkAfWXWqy9wimFkLF0WKaHYExHUdbd3vXMgYbg%2F08Ljq0w%2BdduoZUFzFcYOYEj2OywfhD%2BMS04CBHMeNI35xFIi5gdY9dNRxpVOH9fEpBebnP0cIFnTPH2sMcenGEYaZoA0IHAp7gN9CizEUutBMdbc40w0U07BisdI90axdwmSb66eYBPXKpH90hi%2FtaUulGW%2BNGaqbzgKsW%2Fqzsj0WNs3uGbvDXE&X-Amz-Signature=56025b237c3e897ed1f2c35fe584bd5f482449b1e8cf46e2e9fbab7199f3a0d6&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

好了，我们看完这之后，注意再往下走。这里边就是我们 disruptor 它的一个核心就是我们的 a single log a single log 是 log four G two 里面才提供的一个组件，它底层就是使用了什么呢？使用了我们的迪萨特，大家可以去看一看，你直接去搜这个类名，它对应的是有的。



