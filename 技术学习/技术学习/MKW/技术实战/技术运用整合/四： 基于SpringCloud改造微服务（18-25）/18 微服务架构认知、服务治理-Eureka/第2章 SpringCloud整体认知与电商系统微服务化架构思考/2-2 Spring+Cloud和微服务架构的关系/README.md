---
title: 2-2 Spring+Cloud和微服务架构的关系
---

# 2-2 Spring+Cloud和微服务架构的关系

[image](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/10ee1d6b-e50a-44cf-a281-8592738627d1/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466X5G7XLHZ%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T225520Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIF0nV16COO%2BR%2BcnNIlkMKbTQk%2BQ8NasPVc1Qe1nHOFiiAiEAt2qDt5HysBiElpMxByOfc5PuJZvHQx79XvN2gSHbqykqiAQIxv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDDIo1ft2VyayDw%2BQhyrcAxB52OGH%2FkYB4Yi578rVJ7sspUjd5XvovyqkbuYGykGj1bI67ERf8Pw5COyXdANlDj7s2b4MYtH4MK9AMMS9F4%2F5vkqzFb0qTY0kmvm%2Fhgdjs%2FlldUgh%2Fq%2BWE5x7IUjL66NY%2FZtWxzttID5yIz8CzYuckdznmIi2xnah55dHTkAVCNdEaeW1MTCHbJauch9rIBFInG21yBbXStfR3w73rqlqwHWD1Dmov33ODjYC%2FBmWCaG%2FLgYSYtmzffg1lzR0DbetXK4xSGUNbl%2BiALFVgaxae%2Fe%2F%2FNZZvCRpuS1Z0SCqymhyATk4MecB6ZzX3iGHwKvXMfQDVJRG3%2BNQoMqHvnz0PGl%2BPxyP9K%2BH3IOuqQNvVkf4HGzIWKmMOmd0V%2BBmeyL5RcpqgTu3xmMD%2BSvxTk4I2KICnU2KRA8fyqiGMiC1DlgEowSaCMByIOjog48qKd6Vd9%2FWnLFTpbgO3qqB%2B1DfSTuzb2Wr0BHcEEcqTYHRH9oEruXEk6o3HDZiw3fYld%2B3OZ6BtO8foUEXj6%2BG8b%2Fe39DN%2Bt9aXAgICj%2FHLgUCKQT7DzypgjakP2xl8Ucrz5TBcnP%2BV9590G7PFO0Ie9yZ%2FbAmT3Xb%2FWhN0Yn%2FL5Hbqts3mxfTixa6J6Q7MMS3%2F9IGOqUBfz7bDwBvWVYK7bSjXYq8qTtlnvgyStBQNQNehJCTxN4LvhErBq50C0nUf52yqZDtxjNEkZrbcVnz0I4w3P8OrOOz7czG5Q4%2F%2FaE2cKyIpgrgmCpoNq5cL52w9TDTFyl13gvbESM%2B%2BkJjg8hT7zpCuUm9adk4rFw%2FCiypYqd2k7AoDsVelooqNutqIrxoIhrAMzYe%2F3vSx3o3vDSgAbhY1oQswuM8&X-Amz-Signature=f276ff4816770638a4c56b64d397801441a04d798420be146f7c3c57c77947c4&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

**2-2 Spring Cloud和微服务架构的关系**

前面我们谈了很多微服务的理念，不过这理论知识就像是空中楼阁，讲起来那是头头是道，可是如何将这个宏伟构想落地呢？业界开源软件数不胜数，应该选用哪些技术的组合来完成微服务改造呢？有没有一套业界的最佳实践来参考一下呢？

有！有！有！这所有的问题，都能从Spring Cloud中得到答案。

**大话Spring Cloud**

在Java悠久的历史长河中（其实也就十来年），有一个框架自诞生之初就成了Java企业级开发领域的弄潮儿，它以开放的姿态不断引领着技术改革（我们管他叫Java领域的“改革开放”），它就是久经考验的企业级开发框架，改革开放的总设计师Spring Framework

如今改革开放的春风又吹到了微服务领域，正所谓想群众之所想，急群众之所难，看到码农群众挣扎在微服务的泥沼中，这位改革开放的总设计师坐不住了，它要站出来领导广大码农阶级，坚决打赢这场脱贫攻坚战！

于是乎，一个新的史诗级框架诞生了，它吸纳开源社区各路优秀框架，打包提供了一套最佳业界实践标准的工具包，它就是当下微服务领域的圣经 - Spring Cloud

**博采众家之长**

尽管Spring Cloud是由Spring Framework直接挂牌的顶级项目，但他并不是由开源社区原生态打造的。前面提到过Spring Cloud吸纳了很多优秀框架，这些项目不光来自于开源社区，也来自于一线企业，比如Netflix和Alibaba就是两家对Spring Cloud有突出贡献的公司，这些业界大厂结合自身在高并发高可用领域积累的丰富经验，所贡献的组件也是作风硬朗能打胜仗。

可以这么说，Spring Cloud是一系列开源技术（组件）的集合，它基于Spring Boot之上，将微服务领域的基础设施简化为一个个易于部署且配置简单的组件。如服务治理、负载均衡、熔断降级、配置管理等等分布式应用中的场景，都可以借助Spring Cloud提供的组件库，通过简单的“注解+几行配置”的方式应用到自己的系统中来。

Spring Cloud各个组件来自于不同公司，在每个业务领域甚至还提供了多个可供选择的组件，所以时候它是一锅大杂烩也不为过，但是这锅烂炖它烧的好吃，各个食材（组件）之间配合的天衣无缝，呈现了这道微服务的盛宴。

**解决痛点难点**

只有你想不到，没有Spring Cloud做不到（稍微添油加醋了点）。Spring Cloud的核心组件直接来自业界的大型互联网公司，可以这么说，它们就是绝对的实力派，专注于助力各类复杂业务场景，并且这些组件在大型分布式环境中已经证明了自身的高可用和高并发能力。

目前活跃在Spring Cloud舞台的有Netflix组件库和Alibaba组件库，大家对Alibaba应该比较熟悉，但是对Netflix可能不太熟悉（不过经常看美剧的同学肯定知道Netflix），它是一家流媒体的超级巨头，全球最大的收费视频网站。这些业界巨头自身有着非常复杂的在线业务，所以Spring Cloud提供的组件都是实实在在为了解决各类业务难点痛点而生的。我这里给大家举一个例子，每年阿里的双十一，为了抗住瞬时流量爆发的场景，必须有一个足够大心脏的流控措施，那么Sentinel就是基于这个背景之下诞生的组件，如今它被纳入了Spring Cloud Alibaba组件库。

**构建生态体系**

Spring Cloud不是垒砖头一样将各类组件搅和在一起使用，而是基于一系列的抽象和改造，在原生组件的基础上抽象出了一套微服务的适配框架，让各个组件可以无缝集成，共同构建了一套生态体系。

举一个比较恰当的例子帮助大家理解，那就是推送配置变更的场景。我们表面上是使用Spring Cloud Config组件来管理配置项，但批量推送则依赖于Spring Cloud Bus组件，而Bus底层依赖Spring Cloud Stream组件，Bus在Stream之上抽象出了一层消息广播的事件驱动模型，Stream它本身也是一套对底层消息中间件的抽象，将Kafka和RabbitMQ的交互抽象成了一系列Channel模型。这几个组件之间甚至根本不用什么繁重的配置，只要把依赖项引入Pom，就开始了合体的过程。

**小结**

本节我们对Spring Cloud做了简单介绍（大吹了一番），下一节我会带大家了解一下Spring Cloud的架构体系，看看它为什么这么牛！



