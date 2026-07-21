---
title: 5-1 Gateway架构设计-1（1403）
---

# 5-1 Gateway架构设计-1（1403）

同学们大家好，这一章节我们介绍 spring Claude Gateway 的架构设计。首先我们回顾一下业务网关 Gateway 在企业应用中的作用。现在我们企业级的复杂的微服务架构模式下，我们不应该直接把服务暴露给外网，通常会使用成为网关与外部请求进行隔离。无论我们的请求是来源于APP，我们的 PC 或者说各种客户端的小程序都要通过网关来访问后端提供的服务。那么这层网关不仅给我们带来一些安全认证，更是对前后端进行一个隔离解耦的一种方式。通常我们对于网关接口的定义，我们客户端重构或服务端的重构，只要保证协议的一致性，那么这样的操作就是相对安全的。


我们这里面是采用 spring Claude 位置作为我们 APIEO 重网关。它是 spring Claude 一个全新的项目，它是基于 spring 5. 0 和 spring put 2. 0 以及这个 product Reft 等技术开发完成的。它区域主要是为尾部提供一种简单、有效、统一的 API 路由管理的方式。这里面我们可以看一下 spring code Kate 为官方的介绍。在这里面我们可以看到对于 spring Claude Gateway，它这里面一些概要。


this project provide a library for build an API Gateway on top of spring Wattflex。
也就是说整个 spring Claude Gateway，它是基于 Web Flex 的构建完成的。那么对于 spring Claude Gateway，它的目标是提供一个简单的并且有效的一个路由方式去影响我们的API，并且它能提供我们的客户端和服务端这一层做一层横切面的一个隔离。在这个横切面我们可以做的事情，比如像安全以及我们的数据监控，并且包括一些弹性扩容的相关的内容。当然这里面我们还可以进行一些数据流控相关的操作。


那么对于 spring code Gateway 它支持的这些 future 功能，我们可以看到，首先我们看到它是build，也就构建于 spring framework 5 以及 protect react and spring boot 2. 0。也就是说，首先我们知道我们当前用的 spring code Gateway，它依赖的我们 spring 的版本和 spring boot 版本应该是要大于 5. 0 和大于 2. 0。另外它可以提供我们的路由进行一些请求，根据我们的请求的一些属性进行路由，这里面会包括我们的parameter，我们的 header 以及 cookie 等等这些信息。那么 Pre ticket 也就是一些断言和filter，它可以针对这个路由信息进行一些特殊的校验。


其实我们的路由也就是基于我们的断言信息 predict 进行一个选择，并且选择指定的路由以后，通过它的 filter 来实现它的一些功能。另外这里面可以支持一些熔断器的集成，这里面我们可以后面通过 settlement 来讲解的过程中会介绍。另外就是它可以基于 spring 库的 discover kind，也就是说它可以基于服务发现的方式，直接把我们注释在服务中心的这些服务列表直接映射出来，可以做一个简单的集成，就避免我们对于这些服务进行一个比较复杂的一个配置。另外我们可以自非常方便的自定义这些断言信息和过滤器信息。另外就是还提供像 request 点rate，LinkedIn，也就是我们的访问的一个限流的一些措施，还有一些功能，比如说像我们的路径的一些重写。当然我们在请求的过程中可以暴露给外网的路径和我们内部微服务提供的路径，可以做一层转换，这是我们简单的一个配置的过程。


那么我们现在还回到我们的PPT，那么接下来我们来看一下 Gateway 架构设计的相关内容。首先这里面我们介绍的是基于 spring Claude Gateway 对应它的版本是 3. 0. 2，这是我们当前的一个次新版本，当前最新版本是 3. 3。 0. 那么另外它对于 spring Claude Gateway 它有哪些模块？这里面我们可以看到。


首先我们这里面最重要的，也就是我们经常依赖到的，也就是 spring Claude STARTER Gateway，也就是我们的一个启动器。对于这个 start Gateway，它依赖的内容主要是 spring Claude Gateway Server，这里面我们提供了基于 Ninety 的一个暴露的一个 Web 服务，那么这里面还提供了一些支持性的信息，这里面像 Gateway 的 m a C 和 Gateway Web Flex，这样可以去就做一些我们对于我们 Web 服务的一些兼容。


那么另一个这里面是 spring code get 为dependency，它在里面构建了一些依赖的版本，这个其实我们在使用 spring boot 里面对应 dependency palm 的时候，有一个类似的一种操作，另外他还给我们提供了 spring code Gateway 的simple，也就是说给我们提供了很多的一些我们使用的示例。那么说我们在使用 spring code Gateway 的时候，可以基于这些示例快速的应用到我们的系统，那么我们可以切到源码里面去看一下，这里面我们可以看到对应的一些信息。


首先我们对应的，嗯，源码信息是在 spring code 对应的 spring code Gateway 这样一个 get 的，我们的 git 库里面当前的版本是 V3. 02，那么这里面我们可以看到它的一些结构，一般我们去了解一个项目，首先我们还是去看一下它的 palm 文件，基于 palm 文件对于它的依赖进行一些了解。其实在最根外层这个 palm 文件其实我们可以看到它其实是实现了，也就是说它的 palm 文件是point，是指定了 spring Claude builder，也就是说它归在 spring Claude 这样一个大的结构下面。


这里面我们看我们所依赖的最重要的，也就是我们的 spring Claude STARTER Gateway，看到这里面也是只有一个 palm 文件，对于这个 palm 文件里面，我们可以看到它是给我们间接依赖了，这里面是 spring code STARTER、 spring code Gateway Server 以及我们 spring boot STARTER web Flex，也就是说当我们如果说使用 spring code start get away 的过程中，那么我们就已经使用了对应的 spring boot STARTER web Flex。


那么基于现在我们通常是一些认识，我们可以认为 spring boot starter Web Flex 跟 spring boot starter web MVC 是一个互斥的，当然是我们可以通过源码的方式去解决，但是不建议大家去做这样的事情。也就是说当我们的系统，我们作为一个网关系统，依赖了我们的Gateway，同时也就依赖了 Web Flex，那么这样的话就这个系统就不建议再依赖 stream stop Web Mac 了，所以说这个大家一定要注意一下，我们可以看到后面还有对应 spring code s start load balance，也就是我们的负载均衡策略，那么对于这个 get way 对于负载均衡的依赖是可选的。因为我们可能需要负载均衡，也可能不需要，那么所以说在这里面的 Gateway 没有把这个负载均衡作为一个强依赖。
在这里面我们其实对于 spring Claude STARTER 以及这个就我们知道，作为一个对应 spring Claude 组织下面的一个模块，它肯定需要依赖对应 spring Claude 的相关的一些STARTER，那么对于这里面最重要的也就是 spring called Gateway 的Server，那么对于这个 Server 它我们看一下它的 palm 依赖，在这里面我们可以看到它依赖的一些信息，我们也是从这么个它这里面是对应的。
首先是 spring boot STARTER 以及 spring boot STARTER validation，也就是这次设计的一些 Web 相关的项目，它会进行一些校验的一些操作，这里面我们看涉及到 OS 2 这样一个校验的一个 client 端，当然我们可以看到它的依赖是一个 option 的，是一个可选的，这里面还有跟词名部的 starter accuator。
这里面我们看到这里面其实这个是有点争议的，对于我认为它目前的实现来说， Web Flex 它是一个必选的项，是不是这里面写成 Opcenter 其实会给我们造成一个误导，假如说我们直接使用 spring code get 为 Server 的话，可能还需要我们来手工去引入一下对应的 Web Plex，好在其实我们很少去使用具体的这样 spring Claude get 为 Server 这个模块，我们引入 starter 这个启动器的话，倒也不会因为这里面 optional 我们的 Web Flex 是 open 的可选，那就会丢掉。
那么其实我们从这里面可以看到，如果说我们对于 spring code together with Server，它使用了对于 Web Flex 依赖使用可选的情况，它可能后面可能会支持基于 MA seed 另一种方式，也对于我们嗯网关的一种支持，这也是有可能的，这是我们可以看到这些模块之间的关系。


对于这里面的 MVC 和 y Plex，它其实就是一个适配，这个我们就不去过多的去介绍了，我们可以再看一下对于它的 dependency 依赖，其实 dependent 依赖这个是比较容易理解的，它其实通过 depends manager 对我们依赖的这些版本进行了一个管理，这样的话我们就是做到一个版本的一个统一性。


这里面是一些simple，也就是说一些我们对于 gateway 常用的这些一些案例，我们可以看到这里面是由于一些测试的一些用例，那么我们继续看，我们这里面去看一下对于 get v 的架构设计的过程中，其实我们在启动的过程中，为什么引入这个 get v 的启动器，它就能去生效网格的效果？我们肯定知道基于 spring boot，它是由自动装配来实现的，这里面我们主要关注的自动装配的信息主要还是对应的是 spring close get away Server 下面的 spin factory 对应的一些信息，这里面我们可以从这儿看到，我这里面去做了一些组织。


这里面首先对应词 get a big class pass warning out configuration，它是什么意思？也就是说我们在使用 spring code get v 的过程中，因为引入了 Web Flex，那么所以说它就会对于我们的 class pass 上下文做个检测。假如说我们检测到了对于 Server light 或者说是 three MVC 相关的内容的话，它就会打印出警告。另外这里面最重要的就是 get away 的 auto configuration，我们可以看到对于 get way out configured，它底下引入了 80 多个b，这是它也引入 80 多个主键。


具体的一会我们来看一下对于 get away read science for g，这里面是我们可以看到它是给我们提供了一个默认的熔断器，也就是说支持限制的一个熔断器。当然我们现在是不推荐使用这个熔断器的，我们最终还会用Sentinel。另一个我们可以看到 get with no load bands client auto configuration。也就是说其实如果说我们正常业务线使用的过程中，我们肯定会使用服务的注册与发现，但我们在这里面进行一些原理的讲解的过程中，我们可以尽量简洁一些。比如说我们在讲负载均衡的时候，我们重点聚焦在负载均衡，那么我讲 Gateway 的时候，我们重点聚焦在对于 Gateway 设计的它的路由和它的断言，以及它的一些过滤器的实现上，像这里面还实现了一些像 KTV 的一个监控信息metrics，就是说这里面还会自动的提供一些自动记录这些监控信息的一个 auto configuration。


下面是 get away Redis auto communication。我们可以知道对于 get 位进行计数的过程中，我们可以通过基于 Redis 作为一个我们相对这个集中的共享存储，我们可以进行一些数据的一些记录。


接下来这里面还我们看到这里面有 get away discover and auto configuration，这里面我们可以去想象到当我们的网关去支持通过服务注册中心获取到我们所有的服务列表，进行一个映射的过程中，它就会用到了这里面。 get with discover client 一个自动装配的过程，同时这里面还提供了一些像这里面 simple URL handler Mapping，这是我们对于这里面处理的过程的一些 handler 运营侧关系。当然这里面我们看还提供的 get 为 reactive load balance client auto campaign using，也就是支持负载均衡相关的内容，这里面是跟我们安全验证相关的一些内容，我们可以从这里面去看一下对应的这个 Server 下面它的一些信息。我们现在应用非常熟悉，对于这个配置文件就是在我们的 resource Meta infra 下面的 spin factory，这里面对于我们的 enable auto configuration 自动装配相关的内容。这里面当然还有一个像 human 的 post process，也就是我们的环境的一些样的处理，这里面主要会涉及到当我们在配置我们的这些路由信息的时候，如果刷新的话，可以我们进行一些消息的一些通知，或者我们做到一个动态的刷新，这是这里面的一些我们的一些自动装配的信息。


好，那我们继续。那么对于制动装备信息里面最重要的，也就是我们的 Gateway auto configuration，这里面我也列出了一些，我们可以看到这里面的内容非常丰富，但有些我并没有去展开。好，我们看这里面，像我们这里面 root location builder，也就是说我们程序在演示我们的网关功能的时候，我们去手工指定了一些网关的一些路由映射，就是基于这个 root locate builder 来构建完成的，那么这里面还提供了像这些 property root definition load locator 它是什么意思？它就是说当我们是基于属性文件去配置这些路由信息的时候，它就会通过这个 property root definition locator 去进行解析，最终转换成我们的roadlocator。


那么这里面还涉及到一些 root definition locator，其实跟我们对于这个里面 road depending locator 跟它其实是以 on properties 它的一个具体的一个实现，当然这里面还有可能也有其他的一些实现，这里面其实就是 root locator，就是我们其实比较关注的就是我们可以通过这个 root locator 找到这些路由配置信息，这里面 root refresh listener 它是什么意思？它也就是说当我们涉及到我们对于路由配置信息的变更的时候，它可以进行一个 refresh scope 下面的这些 being 进行一个刷新。


下面这是比较重要的一点，就是 filtering Web handler，也就是其实我们在做我们这些路由处理的过程中，它都是基于 filter Web handler 进行处理的。因为我们最终获取到我们的root，构建出我们的 filter 的一个栈 filter 链在基于这个 filter 链的话进行处理。另外这里面是 Router predicate handler Mapping，我们看到 Handler Mapping 的时候，因为它跟 Spama seed Handler Mapping 有一个对应关系，所以说我们更容易去理解，其实也就是 spring Claude Gateway，它基于 spring 对应的 Web flags 扩展了一个 handler Mapping，用这个 handler Mapping 注入到我们的 Web Flex 框架里面。那么所有 Gateway 相关的一些请求，它就会通过对应的 root predicate handler Mapping 去找到我们对应的一个映射。


这里面会有一些 configuration property beings，这里面我没有展开，下面有具体的一些项，那么这里面我们可以看到比较重要的是一个 h t p header。

