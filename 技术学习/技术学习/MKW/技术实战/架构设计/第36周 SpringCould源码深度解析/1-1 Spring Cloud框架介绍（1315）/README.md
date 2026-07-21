---
title: 1-1 Spring Cloud框架介绍（1315）
---

# 1-1 Spring Cloud框架介绍（1315）

同学们大家好，这章节是 spring Claude 的框架介绍，我们的课程通过三部分来快速了解一下 spring Claude。首先是 spring Claude 是什么？第二， spring code 又包含哪些项目？第三， spring code 它以 spring boot 以及 spring 阿里巴巴相关版本的一些依赖。


首先我们来看一下 spring code 是什么？一句话， spring code 它是一系列框架的有序集合，其实它利用了 spring boot 的开发便利性，巧妙地简化了分布式基础设施的开发。比如说 spring Claude 里面包括的服务注册与发现、配置中心、消息总线、负载均衡、限流熔断、数据监控等等，都可以用 spring boot 的开发方式做到一键启动和部署。


spring 它本身并没有重复造轮子，它只是将目前各家开发比较成熟，我经得起实践经验考验的服务框架组合起来。比如将早期 spring 它集合的是奈飞，现在 spring 与阿里巴巴集成的 spring Claude，阿里巴巴它都是基于 spring boot 的风格封装为 start 的方式，方便我们快速使用，同时屏蔽掉了一些复杂的配置。


这样也得出来， spring Claude 是为开发者提供了在分布式系统中快速构建应用的工具。我们使用 spring Claude 可以快速的构建应用启动服务，同时能够方便和各大云平台的资源进行对接。比如说国内影响力比较大的有阿里云，国外有亚马逊云。大家要注意的是，即便有 spring Claude 可以帮助我们快速的构建分布式应用。


一定不能忽视的是，分布式系统的复杂程度要比单机系统大得多。我们需要知道，涉及大量跨服务的 RPC 调用是极其复杂的，同时会给开发和运维带来很大的工作量。对于大多数公司或业务，它没有达到一定程度，不要轻易做过度的服务拆分。当然，我们可以设计双耦合的系统，划分合理的模块和包结构。当业务量逐步成长起来的时候，再进行微服务拆分，也不会有太大的工作量。


第三， spring code 它是一个很年轻活泼的微服务框架。为什么用年轻活泼 spring code，它在 2016 年才推出 1. 0 的 release 版本，在版本更迭的过程中，有些 API 也发生了变化，早期依赖支撑的这些组件由于各种原因进行了替换，大版本升级也会带来各种不兼容。


虽然 spring Claude 比较年轻，还存在一些问题，但是这些不耽误 spring Claude 成为 Java 领域最成功的分布式框架。主要是 spring Claude，它提供了一个全套的分布式系统的解决方案。接下来我们看一下 spring Claude 包含哪些项目。首先我们来看一下 spring Claude 官方的架构图， spin closer 的构建，微负的思路也如图所示。它所有的这些外部请求，无论是移动端的和 PC 端的，它都会把请求到我们的网关 Gateway 上面。网关主要是进行流量的路由和用户鉴权等公共操作。


网关它基于路由配置，把对应的请求转发到对应的这些服务集群上，那么转发到具体的集群的哪个实例？它首先是需要通过注册中心获取到我们对应的这个服务的这些实例列表，那么然后基于负载均衡的机制对应到具体实例，在微服务的节点之间调用，它都属于一个远程的 RPC 调用，比如说微服务之间或者网关到微服务之间，它都属于一个远程的 RPC 请求。那么 RPC 请求在 spring 中是基于 open 份来实现的，同时阿里的 double 也是国内比较优秀的 RPC 框架，在 RPC 请求问题定位及时排查是非常困难和耗时的。


spring code 提供了分布式的一个tracing，也就是说我们的请求链路的跟踪，它可以把每个请求通过一个唯一的标字串起来，方便我们来分析每一次请求肘部的一些路径节点，以及每个节点处理的一些时间消耗。那么既然有了时间消耗，微服务集群的最大的风险就是节点之间的依赖。由于流量突征或下滑，服务不稳定，引起服务的可用性下降，从而导致一些系统雪崩。这方面 spring Claude，它通过限流和熔断的策略来保护每个应用的一些实力节点。通过这样的串下来的话，我们可以看到 spring 的这些微服务集群盈亏会包括，首先是 API 网关，同时就包括服务的注册与发现以及分布式的一些配置。后面是我们的网关与节点，以及微服务节点与节点之间的这些远程服务的 RPC 调用，还有这里面的链路追踪以及追踪服务之间为了保护自己的节点进行的一些限流或熔断。


好，接下来我们来看一下 spring code，它具体这些项目的包含逻辑。首先我们可以看到 spring code 本身作为一个大模块，它集成了很多模块的组合。首先我们来看一下服务注册一发现，基于服务注册一发现它有多种可选项。首先这里面我们推荐的是阿里巴巴nicos，其实还有奈飞提供的 urack 以及阿巴奇的Rooper，它都可以用来去做服务注册与发现。这里面要说一下，像 double 沼气是使用 Alpaca 的 keeper 作为默认的主体与发现，那么 spring code 的第一开始它是使用的是奶菲的irocket，现在是 spring 的，阿里巴巴的 Nicos 就更在国内是占据一些上风的。


好，接下来我们来看一下分布式配置，也是像 spring Claude 比较支持的是阿里巴德 Nicos 以及 spring 自己的 spring Claude configure，同时基于分布子配置，其实市场上还有携程的阿波罗也是比较受欢迎的。


接下来我们看一下 API 网关， API 网关的可选项不多，最早期是 spring Claude 使用 knife 的注作为默认的网关，现在由于 rule 的停更等等一些原因的，现在 spring 自己开始去做自己的 spring Claude Gateway 这个网关项目。


接下来我们看一下限流熔断器，早期使用的是奈飞的 his tricks，那么现在也是因为一些停更的原因，现在在国内的阿里巴德 Statue 现在是使用人越来越广泛。接着我们看一下服务调用。对于服务调用，在 spring Claude 里面，它主要让基于 HTB 的方式进行调用，所以说这里面最多的是使用的是 open 份，同时也支持 rest template，这是 spring 本身提供的 HTV 的一个 client 端，同时基于 double 的服务 RPC 调用也是使用非常广泛的，但是它默认的并没有跟斯门科特做一个友好的集成。
接下来我们看一下负载均衡。负载均衡其实也是现在 spring Claude 的 load blanks 逐步要替换到原来集成的 knife 的Ruby。消息总线写次 spring Claude，它对于各种消息组件进行一些封装，包括像Kafka， Rabbit MQ 和 doc MQ 的进行一个封装，但是我们用的话都是基于 spin code blade spin code bus 去使用，我们并不关心具体这些消息的实现。还有就是链路追踪，这个我们一般默认就推荐用 spring Claude，萨料斯去做就行。当然它还有其他的一些 spring code 组件，包括像一次性token，全局锁， leader 选举分布， session 集群状态等等，这些服务我们就不业绩介绍了。


下来我们看一下基本 code 在 Git Hub 上这些代码的一些情况。其实我们注意到像 spring Claude，它跟 spring product 并没有在一个 git Hub 上面，这里面 spring Claude 单独去开了一个 git Hub 空间，我们可以切到 git Hub 上去看一下，在这里我们可以看到它是在对应的是 get Hub，在里面是 spring code 这个目录下面，我们可以看到它里面的模块是比较多的。一般这些模块的命名是基于 spring code 作为前缀，进行像knife， get away configure 这样模块的一些设置。但是如果说相比较的话，这些模块他们的这些关注度跟 spring boot 和 spring framework 当然不是一个数量级的。


对于这些项目的话，它可以分为两类，一类是 spring cloud 对于一些成熟框架的一些封装，比如像这里面的 spring q 的奈飞，它是把奈飞公司的一些开源的主键进行了一些封装，也包括像 spring 的阿里巴巴。当然 spring 阿里巴巴的 Git Hub 的目录是在 SP 阿里巴巴的组织下面，它并没有在这里面。


第二点是有一部分的是 spring 本身它自己开发的一些功能模块，这里面包括像 spring Claude 的Gateway，还有下面的 spring code configure 以及 spring code load plus，这些都是 spring 的他自己去实现的。这些模块对于我们想快速开发这些实践微服的开发者来说，通常基于我们这些模块是完成足够了。


我们的课程会推荐大家使用 spring Claude 阿里巴巴的组件，大家可以切到 spring Claude 官网上，在这里面是对应的project，我们可以选择对应 spring Claude，从这里面我们可以看到也是这些 spring Claude 相关的一些模块，我们可以看到这里面有 spring 阿里巴巴和亚马逊相关的一些服务的组合，这是各个模块都有对应的一些文档，大家可以感兴趣去看一下。这里面我们可以选择学习的方式进行对应，版本以及我们有一些案例你都可以参考去学习。那么嗯，我们切回到 PPT 我们看一下，从这里面可以看到我们其次对应 spring Claude 的它包含的这些项目，比如说像这里面有 spring Claude builder，其实它是用来构建整个 spring 模块的一种方式。这里面像 sprinkle 的bus，我们的是短路器configure，这里面 Sprint common 这些模块都是相对来说是孩子比较重要的，希望大家可以把 GitHub 上的代码克隆下来，大家去分析一下。


好，接下来我们看一下 spring code 阿里巴巴相关的一些内容。 spring code 阿里巴巴是由阿里巴巴团队去适配了一下 spring Claude 的一些接口和规范，那么去推出了 spring code 阿里巴巴的这一套使用方案。 spring code 阿里巴巴它目前的热度是非常高的，在 Git Hub 上它的 stop 和 fork 数甚至比 spring code 本身都要高，我们可以在 Git Hub 上看一下。


在这里面 spring code 阿里巴巴它是隶属于阿里巴巴的组织，下面它提供了哪些功能？我们可以看一下下面的 read me，这里面当然也有众人文档，它其实主要是包括像 settle 这样一个流控组件，它可以提供限流和熔断的一些功能。还有nicos，这个 nicos 它使用就比较广泛了，它主要可以用来去做注水发现，同时它还可以进行一些我们的分布式配置。下面的 rocksmq 就是我们几个分布式的一个 MQ 消息体系。下面还有double，也就是阿里早期推出的一个 RPC 框架，现在它的热度也越来越高，在国内使用 double 的公司还是非常多的。下面 SATA 也是阿里巴巴的开发开源出来的一套分布式 soul 的一些解决方案，现在的关注度也非常高。


好，我们回到PPT，我们了解完了 spring code 以及 spring code 阿里巴巴，看一下他们这些版本及源码的一些关系。首先我们要知道有一点是，首先 string Claude swing code 它本身是依赖 spinboot 的，同时 spring code 阿里巴巴它又依赖到 spring Claude。这里面的问题就是 spring code 我们用最新的 spring code 版本看到的它依赖的 spring boot 版本不是最新的。同时我们看到 spring code 阿里巴巴它最新的版本，它依赖的 spring code 版本也不是最新的。所以说在这里面我们基于这个依赖关系的话，我们优先去选 spring code 阿里巴巴的最新版本。


spring code 阿里巴巴当前的最新版本是 2. 5 release 版本，它依赖的 spring boot 版本是 2. 2. 1，同此它依赖的 spring clude 版本是 h 版本。 3. 在这里面 A4 版本它通过 S R 1 到S20，我们选用的是 S R 9 这样一个版本。那么来看一下我们思文科的课程最终的一些版本选择。首先这里面我们选用 spring code 阿里巴巴的当前最新版本是 2. 5 Redis。同时对于 spring code 阿里巴巴，它依赖的 spring Claude builder 的版本是 2. 1，这个 2. 3. 1 这个版本对应的 spring Claude，我们常规的这个发布列车，它的版本是 s 版本的S29。 3.


同时对于这个版本，他们依赖的使用部的版本是我们的课程默认就基于这样一个版本去进行使用。同时大家应该注意到，其实在 stream Claude 它后期的版本，版本的命名已经发生了一些变化。我们知道早期的这些基于字母的这种方式是基于伦敦的地铁进行a，b，c，d，e，f，g， h 的这种更迭。后面的话， code 它会基于年份进行一个版本的更迭。


spring code 它现在最新的版本是 2020 杠 0. 1 这样一个版本，同时也是对应的 spring Claude i 版本，也就是 s 的下一个版本 spring Claude。阿里巴巴它也会追随 spring Claude 这样版本命名的策略，它也会采用 2020 杠 0 这样一个版本。同时我们可以看到在 spring code Git Hub 的代码上已经有了 2020 这样一个分字。关于 spring code，我们一个初步的一个入门介绍，我们就先介绍到这里，同学们，我们下一节再见。


