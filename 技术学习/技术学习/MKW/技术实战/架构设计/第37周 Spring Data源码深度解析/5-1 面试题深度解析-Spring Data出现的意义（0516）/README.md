---
title: 5-1 面试题深度解析-Spring Data出现的意义（0516）
---

# 5-1 面试题深度解析-Spring Data出现的意义（0516）

[image](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/42ff27e7-f03c-4354-a364-c085be7ac837/SCR-20240814-jrmv.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466Q2PA2ZWP%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T232147Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQD6GTRxeU6QCJRzCpiARuDvgQj3H6vKSxChqeZpaLqBzgIgc4FWHDINGeSCq0dASAJLh1s0f0kh8EmaEVf7ZR9NVA8qiAQIxv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDLqd9%2BsLv6u3hBgeAircAwk8PlqA8wADf33aM7FwbWKHZnA0LdB6kDYI2sGgcRK6sLAHiJPbbNxe4%2BJVPJVoVPHIjGrFF1bOH1KYuoeDQxOQ9s2MU819lMSVNUi0m%2BBUnJv75%2Fi%2FNBKykqyToy85shp%2BRlEjXVIFezCrgukqgsKzyP9JGUW0uQTq%2FYCBYuhSmM0g1O8EQXmOuY6b6iYbJW5blVcgcAbIyT79SQQKIt03s01ZTp%2BcwmR54oGHkZWg5WquG9HskyfzD0gGzPVIcL1rbMvVbUB6Wtw7J79dzwQLLuJ563yfZ%2B938jexO%2BIqnU1VnVJrMjlPyA2ibCfOtMhS%2F%2FXpRrcOqFAeU7ZVDTzv%2FGUbGs2D7etixNtQZR%2BVr7RkEISAAk4VG8xSH636tDPu%2B3fDKvPdZW2lsLRqXx53%2Bnt%2BA3vAJZGlXTi5SkyTqz7xVtDEO5U4mYfpgOEbrpOh4v3NgJM3ErgJP4JMr1uborgJBpthwAgYqrW0lqejMQWxT7dFI6YxhSoRzSwkd7oMZzMztwHixkFF3hiqElolKS0RvS%2BwHyzeKuH92TlRLB%2B2BwWhUQ1u0RFtZdN8NwZB1b9insj6nqKCy8Fc5caZU3pXhORPxS6FhJCKu21BgmA0W9NqUGRy3H2HMJa7%2F9IGOqUBeV%2BzNplZO%2FvAIqpzgjQO4aHedVhTY%2F%2F1gGUAwDP7XJBhAzpwmqnKBbKIrfZR37r87wQ1xHJa%2Fg1K7hB71CHlnD2vfafsjwAymaOrzQRC9Jv7VTepJFdn6qV8iIXYGiP6QIXpO%2Fd8jpgHkS%2BI8uOUKvZg5SGcUh3kBkJzzipcfdl6hPTZnVr0srDGCnq09YfP8G%2FXiRRkt9PcGYvTBVec8bWU2ilZ&X-Amz-Signature=acbc8acabd6925f2c8176ce507c21a5321921185a01eaef8b919aa82d1e0d799&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

们，大家好，这一章节我们来介绍 spring date 的面斯题，深度解析。这里面的第一个问题，我们来讨论一下 spring date 出现的意义，我们通常是讨论某一个主键，它的意义的话大多是对于逐渐出现的背景解决的问题以及它的一些特性来去做一些说明。对于这个问题我们可以基于这三方面来去解答。首先是我们去介绍一下基于 spring 对数据访问提供一个统一的编程模型，这次 spring day 的出现最大的意义我们只是这一句话去回答的话，肯定是不够的，可以基于我们自己的理解对 spring date 进行一些延伸。二部分我们需要说明一下 spring date，它介绍一下整个 spring date 模块它的一些关键功能的一些特征。有了这些关键功能的特征，我们再介绍一下 spring day 的包含哪些模块，再把这些模块它简要的介绍一下，基本上能满足 spring day 的出现意义。


这个话题。首先，对于基于 spring 对数据访问提供统一的编程模型，我们怎么去介绍？我们知道 spring did，它的使命是为数据访问提供熟悉一致的且基于 string 的一个编程模型。同时，我们统一的编程模型，不管是对于JDBC，我们的惯性数据，还是我们的非关键选项Redis，elsets， MongoDB 等等保留这些特殊的数据存储特征的一些特性。


spring date，它能是我们的数据访问技术，不管是关系型数据库，非关键型数据库，甚至涉及到 map reduce 的框架，或者是基于云的这个数据服务变得容易。它整个基于 spring data common 包含了所有的许多项目，其中包括许多这个特定数据的项目。这里面像我们涉及到的Redis， MongoDB search，还有 NU four j 等等这些项目模块，有些是 spring date 项目组独立开发的，也有一些是社区提供的。大家知道这一项的话，知道了我们基于 spring 如何对数据的访问，提供了一个统一的编程模型。


第二个我们介绍一下 string date，它提供了一些关键的一些特性。首先我们知道通过 string date，我们把这个数据的存储进行了一层抽象，并且对于数据与我们加尔对象的映射，构建出来一个更具有特性的一个抽象的编程模型。另一方面是我们可以通过数据库，我们在进行 report re 操作的可能。我们基于方法名称派层超过动态的查询，这也就是我们一直在说的我们基于方法名称的一个查询，还有我们的命名查询。另外我们提供了一些基本属性的实现类，也就是说我们提供了一些，比如说像domain，像我们这里面的是 get ID 或者我们的pazable，以及我们对于机器auditing，营业审计相关的一些操作。另外对于透明审计，这也是死命地的出现了一些特征。


虽然我们知道对于 credit date， last update 这些， MySQL 也提供了一个这样的一个特性，当我们修改这条语句的时候，我们自动更新这个最后操作时间。当然 string date 它基于一个更高层的统一抽象，可以覆盖几乎所有其他的一些数据库来完成奥迪的操作。


另一个我们可以集成自定义的一些存储库代码，也就是说当我们的 spring date， GPA 或者说 excess 等等它默认的 report 不能满足要求的时候，我们可以自定义一个接口，基于接口的实现来完成我们自定义的一些功能。另外这些实现的过程中，我们基于加 configure 或者 Xmail 都可以轻松地配置。当然现在我们更推荐大家使用 string 布的来进行一个 enable auto configuring 自动装配的方式来完成这些功能。


其实我们还介绍到了像 spring data 对应的rest，也就是说它跟 spring city 集成，很方便的把我们 spring date 对应的这些 report 实现暴露出来，也就是说我们可以很少代码就完成了基于 string date rest 完成的正常改查的操作。


那我们看第三点，它包括的这些功能模块有哪些？对于 string date 它包含的功能模块，我们印象最深刻的应该是 spring day 的common，其次我们还有 spring day 的JPA。以 spring day 的rest，除了这几个典型特征以后，这里面还涉及到 spring date 的 JDBC 以及使用 data 我们的 key value，基于 key value 进行对于 Redis 这一类插入的更深层式的一些抽象，知道 string day 的 Redis 是基于 string k v 来实现的，另外还有涉及到像 string day 的Mongo， spring day 的一段测试，以及还有我们在课程里面没有提到，但是也是作为一个大数据存储的。像 spring date for Alpaca 的Concentra，这个使用的也是比较多的。


后面其实我们可以去 spring day 的官网去看一下，还有一些社区提供的模块，比如像 spring day 的 n u four j 以及 spring day 的 for r PAJ 的Sora，也就是一个查询的一个数据库，所以说它其实一些社区的东西还是挺多的。


其实我们介绍完这里的话，面试官应该是理解你对此中 date 呢？其实是有一些了解的，但是这里面我们并没有涉及到源码的部分，那么如果说你能基于 string day 的common，它的抽象层去更深层次的介绍，肯定也会进行加分的。关于 string date 出现的意义，我们就先介绍到这里，同学们，我们下一章节再见。


