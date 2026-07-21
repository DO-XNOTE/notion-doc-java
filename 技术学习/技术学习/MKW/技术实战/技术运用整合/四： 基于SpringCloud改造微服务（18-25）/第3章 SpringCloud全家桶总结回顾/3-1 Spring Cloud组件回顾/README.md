---
title: 3-1 Spring Cloud组件回顾
---

# 3-1 Spring Cloud组件回顾

[image](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/adb3eebe-4891-4270-8b85-66f0190c4e79/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466THCYQB3N%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T225905Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIEkWBrQ%2BMB3d3QHLur7ir4XNM2i%2B7%2Fuh1mTCihncFVhGAiEAm8XFghD755sB5dvceXuT122p%2F2HeM4TakfgXWHB%2BgvgqiAQIxv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDEiuMExJ0VGBhrC8%2FircA2WlW5koWDEgKjDaLOHtjey4%2F9MVmXyOxFE%2Bcku3TF%2FRAhIUb%2FvOJ1VdW%2B23uExPycKccbxNcF2Tljjvqqr2S0NYklaONDY0Zznxm7uq67r7YOP9JuSZdVNJBKXRY3sDsY4tQNDDdPtLzVgdlzstNhxhXORKnXTO%2BwXnGb0irMAmP1FlY%2BSBdjXWJDpMqJ6NISOg0xbUyZ5Bmu1XXoeoVNFphC01nvxjGdgm%2Ffgs0d56vl6UkzN2DKVBSgOs%2FqTxBXOnjK0EzLMguqF6le%2FQ0r59YyzT1N4rH%2BioBM01iDvFk5xP8BcYwVCkqosbv3p97GKx1rVYjZCZ1vKdyXImF8%2Bxs9EwvD7KUnuYIZGd4CejJJyDxfuVJmmffhohr1pGWM4Lot%2FPBQrGrIgQkgQjjea6tHxuCJ2y9TX%2BcdBUTTiWWIh88BxfE3jG%2FliYWR6yqs7OObHaV3cNCTdVG690G0hhitNinLUMXpTgfX4iD70bOnUzxrV1sLEwHWi0gu2aYlyPtBCwkwYkzePS15gKSmiXf8mCFUwBF4rK1SdYkGZMq3fDw%2FOVVcrbs9RCgTP3RYhMAtrN3YnMNJbxWey%2BRNjw54BHNwp2k1gGlW81SDfpcY0Iwtd9coAs%2BajkMMe6%2F9IGOqUBGOcjFDZbngQfE4zeaBhwC5zS8ODE9fnpkQDNHIuw9MiOljyMNq3oY0vJ8WaehRQqSkFQktCfg7S6HTgzrAzUCa9MkJXbqTOgPynoXN3uzTrIBUK6R55V5NWICSijy5r0ne0US9RQeXlTODbvqxO82i8ZB3bQYe9nNSm6CVAdFRdj2AGZsx9uEQSqaejdePkEEXuyXMB3FNGu62a4JMySn6XPOCEx&X-Amz-Signature=932d3c383a263d10f5f4c41e26c430ea69ebd39564e3ccef1ad1ec2bff0ed7de&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

[image](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/bf256451-f63d-4741-841b-67bd98fb1dc4/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466THCYQB3N%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T225905Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIEkWBrQ%2BMB3d3QHLur7ir4XNM2i%2B7%2Fuh1mTCihncFVhGAiEAm8XFghD755sB5dvceXuT122p%2F2HeM4TakfgXWHB%2BgvgqiAQIxv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDEiuMExJ0VGBhrC8%2FircA2WlW5koWDEgKjDaLOHtjey4%2F9MVmXyOxFE%2Bcku3TF%2FRAhIUb%2FvOJ1VdW%2B23uExPycKccbxNcF2Tljjvqqr2S0NYklaONDY0Zznxm7uq67r7YOP9JuSZdVNJBKXRY3sDsY4tQNDDdPtLzVgdlzstNhxhXORKnXTO%2BwXnGb0irMAmP1FlY%2BSBdjXWJDpMqJ6NISOg0xbUyZ5Bmu1XXoeoVNFphC01nvxjGdgm%2Ffgs0d56vl6UkzN2DKVBSgOs%2FqTxBXOnjK0EzLMguqF6le%2FQ0r59YyzT1N4rH%2BioBM01iDvFk5xP8BcYwVCkqosbv3p97GKx1rVYjZCZ1vKdyXImF8%2Bxs9EwvD7KUnuYIZGd4CejJJyDxfuVJmmffhohr1pGWM4Lot%2FPBQrGrIgQkgQjjea6tHxuCJ2y9TX%2BcdBUTTiWWIh88BxfE3jG%2FliYWR6yqs7OObHaV3cNCTdVG690G0hhitNinLUMXpTgfX4iD70bOnUzxrV1sLEwHWi0gu2aYlyPtBCwkwYkzePS15gKSmiXf8mCFUwBF4rK1SdYkGZMq3fDw%2FOVVcrbs9RCgTP3RYhMAtrN3YnMNJbxWey%2BRNjw54BHNwp2k1gGlW81SDfpcY0Iwtd9coAs%2BajkMMe6%2F9IGOqUBGOcjFDZbngQfE4zeaBhwC5zS8ODE9fnpkQDNHIuw9MiOljyMNq3oY0vJ8WaehRQqSkFQktCfg7S6HTgzrAzUCa9MkJXbqTOgPynoXN3uzTrIBUK6R55V5NWICSijy5r0ne0US9RQeXlTODbvqxO82i8ZB3bQYe9nNSm6CVAdFRdj2AGZsx9uEQSqaejdePkEEXuyXMB3FNGu62a4JMySn6XPOCEx&X-Amz-Signature=1f0d13cf06b04227960ac082da52473dcae70ab9b17f61b486b8baae981b6856&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

的各位同学们，大家好，经过前面几个星期大家非常努力的奋战，我们 spring cloud 的部分就要告一段落了。那么接下来我来带大家一起去回顾一下我们在这个章节当中学过的所有 spring cloud 的总结。同学们不用紧张，这是期末总结，不是期末考试。不过大家可要记得在结束课程之前，把前面欠下的作业全部补上交。那我们就从咱学习的第一个 spring cloud 组件 eureka 开始这段回忆。


如果说微服务架构是一个摩天大楼的话，那么这服务治理就是这座大楼的地基。咱 EU 瑞 CA 提供了非常丰富的服务治理功能，有服务注册，它的服务注册是通过 enable discovery client 这个注解来发起的。那接下来还有服务发现是客户端主动到注册中心拉取服务列表。接下来还有心跳检测，心跳包也是由客户端主动发起发送给注册中心，更新自己的服务状态，建立在心跳检测机制之上的，还有服务续约功能。**这里服务续约我要强调一个知识点，那就是咱里面提到的 dirty time 如果 dirty time check 没有通过的话，它会重新发起服务注册。**


除了服务续约以外，还有一个功能也是建立在心跳检测的。同学们还记得吗？叫服务剔除对不对，那服务剔除还有一对冤家路窄的功能叫服务自保。他们俩之间是有你没我有我没，你只能有一个在起作用。最后一个是服务下线，它是由客户端主动发起下线请求到服务注册中心。 OK 那 eureka 我们知道它是基于什么 HTTP 的服务治理方案。在稍后的章节，我们还将跟大家介绍一种不同的路线，那就是 double 的 RPC 我们微服务架构的组件都要讲究一个高可用性。我们在相关的课程里也提到了有瑞卡如何通过多注册中心互备份，实现它的高可用化改造。


接下来有瑞卡后面我们学习了负载均衡组件 ribbon 那 ribbon 有十八般武艺，它有一套非常丰富的负载均衡策略库里面内置了很多种负载均衡策略可以供我们选择。那在相关的课程里，我们还介绍了它的 iping 机制以及 ribbon 所采用的 error 扩展机制。并且通过扩展一个 error 接口，我们实现了自定义的负载均衡策略。


那 ribbon 中还有几个比较关键的知识点，比如它的超时判定的配置，还有它的重试。[**关于重试，我们这里必须要强调如果你的接口没有实现幂等性，那么要慎重使用重试功能**](/af163c3df3fd462c8771f251e9ec6887)。除此以外，[**我们还在图文教程里面探讨了如何根据不同的业务场景选择合适的负载均衡策略**](/8ffe4f9464a6458db1b67a88625af26e)**。**[**我们这里引入了两个模型概念一个是连接数敏感模型**](/8ffe4f9464a6458db1b67a88625af26e)[。](/8ffe4f9464a6458db1b67a88625af26e)

[另一个是 rt - response time 敏感模型](/8ffe4f9464a6458db1b67a88625af26e)。忘掉的同学们可以翻过去回顾一下当时的图文章节。在 ribbon 后面，我们学习了一款简化服务间调用的组件，叫 fin 它的使用风格非常小清新，是本地接口 style 形式的方法调用。这里面两个比较核心的概念分别是 fincontract 和动态代理机制。不知道同学们有没有按照老师上课时提到的要求，从头到尾通过 debug 走一遍份的流程，如果还没有尝试的同学，不妨去抽空体验一下。


那 fin 这个组件还有非常厉害的左膀右臂啊左青龙右白虎，它集成了 ribbon 用来提供负载均衡的特性，并且也集成了 high stricks 用来做服务间的容错降级。紧接着分之后，我们学习了一个重量级的组件，它的内容非常多是 high strikeshigh strikes 有三板斧。第一板斧就是这最常见的降级功能，它是通过指定一个 fallback 函数实现降级的流程。我们在业务代码中也跟大家展示了多级降级，就是多个 fallback 串联起反应。有关降级这里面还有一个比较特殊的功能，那就是 request catch 其实与其说是降级，不如说它是一种性能提升的手段。


接下来的第二个板斧就是熔断，熔断是建立在降级之上的一招雷霆手段这里面涉及到两个比较重要的知识点，分别是触发判定，就是说在什么情况下方法才会触发熔断，以及这里面还涉及到的三种熔断状态的转换，就是熔断开关的 open 状态、 close 状态和 health open 状态，它们之间是如何来互相转换的。那第三板斧就是线程隔离。我们在课程中介绍了两种不同的隔离方案，分别是线程池以及基于信号量的隔离方案。


在 high streaks 章节，除了技术部分以外，我们还拓展了主链路规划的剧情。我们通过阿里系的一个简单的用户从搜索到最终下单的场景，跟大家梳理了主链路规划当中需要考虑的种种问题。在课程中我们还介绍了 high streaks 的两个好搭档，分别是 turbine 以及 high streaks dashboardturbine 是用来聚集不同服务器之间的服务调用状态，而 dashboard 是一个可视化的页面，将这些服务状态体现在 web 页面上。


在 high streaks 后面，我们来到了 config 组件。 config 组件最重要的一个特性就是管理配置项，那它可以把配置项存在代码仓库里或者是数据库或者是本地的文件当中。我们有三个非常重要的属性，它们决定了你的应用会拉取哪一个配置文件。这三个属性分别是 application name 还有 profile A 级 label 构建在配置项管理之上，还有一个动态刷新的机制。


在课程中我们还介绍了如何通过 config 组件的加解密特性对配置属性进行加密，然后存放在相应的代码仓库里，并且在拉取配置文件的时候进行解密操作。配置中心作为一个独立组件，它也要具备高可用化的特性。那在课程当中，我们开启了多个配置中心，并且将它们都注册到了 eureka 注册中心中。所有的应用节点，通过 eureka 的服务发现机制来拉取相应的配置文件。接下来的一个章节我们介绍了 config 的一个好搭档，那就是老司机 bus 消息总线。它的主要应用场景就是和 config 一起搭配使用，构造一个基于总线架构的配置中心，将配置变更推送到整个集群中的服务节点上。其实 bus 能做的远远不只是当 config 的小弟，他也可以自己去自定义一个事件，实现广播场景。当我们的项目集成了 bus 组件以后， bus 它会很自觉地将自己的消息推送的端点注册到 activator 上。那我们在课程当中也相应的学习了 bus refresh 它的底层机制是如何来运作的？ OK 在 bus 以后，我们又介绍了一个独立的微服务组件，它是 gateway 网关。


gateway 也有三板斧。第一板斧是 root 它的路由规则的集合，我们在 gateway 的网关层当中可以配置多个 root 那你的用户请求匹配上了哪一个路由规则呢？那它就会使用相应的 root 转发到对应的服务器当中。那 root 背后一个最关键的属性叫 URI 它是你的应用请求最终将要访问的目标地址。
第二把板斧就是 predicate 其中咱最常用的是路径的断页。那除此以外，我们还有基于 header 基于 requestparameter 甚至 cookie 等等很多很多种不同的 predicate 最后一把板斧就是 filter 过滤器。当然了， gateway 已经给我们提供了丰富的过滤器，用来处理 headerrequestparameterresponse parameter 等等。不过我们也可以实现自定义的过滤器来满足我们的特殊需求。


除了这三板斧以外， gateway 还有很多其他的功能，比如它也兼具负载均衡的特性，并且可以和 hashtag 搭配使用来执行网关层的降级。而且 gateway 还内置了对于 Redis 的知识，我们可以在网关层当中结合 Redis 来实现限流。在咱的课程当中还自定义了一套 filter 实现了用户权限的鉴定。


那排在 gateway 后面的一个组件，我们学习了 sleuth 它是专门用来做调用链追踪的组件。其中比较重要的一个知识点是它的数据结构。这里分别有 trace 它是在整个调用链路中保持了一个唯一的 trace ID 的结构。除了 trace 以外还有 span span 是标识了一个基本的工作单元。当然在工作单元内还有一些事件，那它是通过 annotation 来标示的。 sleuth 的实现原理其实非常简单粗暴了，它是通过 adapter 机制为每种不同的调用方式实现了自己的适配器，并且在上下游调用链路中传递 trace 信息。咱们的 slows 是一个人员超好的组件，它有很多的好搭档，比如说 zip king 还有 elk elastic search logstash 和 kibana 三兄弟。通过这五小强合力，我们就可以玩转调用链路，追踪的所有的用户场景。那在 smooth 的后面，我们学习了 stream 组件，stream是用来做消息驱动的中间层和咱的底层消息中间件进行交互的。记住它，我们可以轻松实现发布订阅模型。这里面我们跟大家 demo 了广播场景以及如何利用 rabmq 的延迟。消息 stream 还有两个非常重要的特性，分别是消费组和消息分区。通过消费组配置，我们可以让组内的服务节点轮流的消费消息。通过消费分区，我们可以把具有相同特征的消息定向的发配到对应的分区当中。那除此以外，我们还学习了很多的异常重试的策略，比如说原地打转的单机 retry 以及 enqueue 也就是把异常的消息重新发回到 queue 让服务器啊重新消费。我们还对那些顽固异常做了终极手段，那就是借助 rabi MQ 的死信队列，将这些怎么也修不好的请求直接发配到死信队列中，等待人工介入。


最后我们还可以借助自定义的 fall back 逻辑，将消费失败的消息导向到降级流程当中。 spring cloud 中所有学过的组件我们已经回顾完了。接下来老师有几句额外的话送给同学们啊，我们学了这么多知识啊，一定要多多实践去练习。正所谓纸上得来终觉浅，觉知此事要躬行，这个躬是躬下身子的躬。同学们也就是说要让大家通过实践把学到的知识巩固下来。所以技术人员要始终贯彻这么一个思想。


Talk is cheap， show me the code
在实践的过程中，我们要秉承尽信书不如无书，所有学到的知识一定要能活学活用，不同组件的不同功能搭配可以产生很多的化学反应。就像我们打英雄联盟或者 Dota 不同英雄的技能组合，那会产生意想不到的效果。这些都要通过我们在实践中多摸索，多积累经验。


同学们在实践的过程中一定也会碰到很多稀奇古怪的问题，比如我的环境怎么起不来了？咦这里怎么跟老师教的不一样这个功能为什么不起作用？正所谓 no pen no gen 我们只有不断地去解决各种各样的问题，这样才能积累经验值。这就像一个打怪升级的过程。你解决的问题越多，打的小怪越多，经验值涨得越快，你自己的等级才越高。这样你的老大才放心，让你去解决大问题，解决大 boss 那在最后我要嘱咐同学一句，碰到困难，碰到任何项目中的疑点难点，我们一定要主动承担。这其实是在职场中一个很积极的态度转变，与其主动等着别人把任务分给你，和你自己，主动站出来承担这个责任，这对你的个人成长是绝对截然不同的两个效果。我们不光要技术拿得出，手活好，同样也要有这份责任心主动承担。在最后，希望同学们把学到的 spring cloud 的知识勤加修炼，终有一日将会神功大成。祝同学们有朝一日可以大鹏一日同风起，扶摇直上九万里。同学们，我们下一节课程再见。




