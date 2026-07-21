---
title: 3-1 LoadBalancer架构设计-1（1128）
---

# 3-1 LoadBalancer架构设计-1（1128）

消费同学们，大家这一章节我们介绍 spring Claude load balance 架构设计。首先我们回顾一下负载均衡的工作原理，之所以需要负载均衡的存在，是因为在微服务集群中存在着复杂的系统调用关系。消费者在通过注册中心获取到服务列表中，我们要选择一个示例进行一个请求执行，那么这个选择其中一个实例的过程就是负载均衡的逻，具体我们通过什么样的一种策略来选择，这是负载均衡的算法，最常用的基于客户端的算法，像轮询哈希，当然随机选择也是一种算。


那么在这里我们要注意，我们这里面的负载均衡只是关心消费方，他在获取这个服务列表里面选择一个的过，那么至于消费方这个服务里边，它是通过注册中心获取的，或者是通过其他方式获取的并不关。所以说我们对于这个负载均衡的架构设计，我们聚焦在消费方获取这个具体实例的一个过程。


现在 spring Claude 的负载均衡的默认实现已经不再依赖RE，那么 skin Claude 团队自己完成了一套负载均衡的实现，它是基于 spring code load balance 完成。这里面我们看一下 spring code load balance 它的源码所在。 spring code load balance 它的源码是也是作为 spring Claude 对应下面的 spring Claude comments 下面的一个模块来完成。那么 spring code Commerce 大家可能会比较陌生，这里面跟大家简单介绍它下面的模块比较多，对我们关心的 load balance 来说的话，它比较重要的模块，这里面 spring Claude comments 和 spring Claude context，这里面有我们重点关注的 spring Claude load balance。原来的 spring Claude load balance 是一个单独的一个 gate 功，那么后来它已经合并到了 spring code common，在这里面它们之间的一些依赖关系。


spring code load balance，它依赖 spring code comments 和 spring code context，我们可以看到comments，它里面是定义了一斯文库的，说一代这些主键的抽象，这里面比如像我们的服务注册一发现我们的负载均衡，以及对于我们的一些熔断器等等这样的一些具体的就是一些抽象的一些概，对于 string code load balance，它实现对应 spring code comments 里面负载均衡的实现。


那么这里面的 spring code context，它是扩展了一下对于 spring code 里面常用的一些上下文的一些信息，那么除了这三个模块，其次它还有一些其他的模，那么对于 spring Claude comments，它下面还有，这里面 spring code comments dependence，这里面我们刚才介绍的 comments context 和 load Belle。同时它还有像 spring Claude starter，bootstrap，这里面还有 spring Claude starter， load balance 这些内，那么我们可以把源码下载下来，在我们本地看一下它的源码结构，在这里面 spring code comments 下面，这里面是我们关心的 spring code comments 以及 spring code comments dependence、 context 以及这里面是一些字词集成的测试的一些辅助。


那么最重要的就是我们这里面的 Spencode load balance，同时 Spencode load balance 为了简化使用，这里面集成了像 Spencode STARTER load balance，通常我们使用的时候就是引入 spring code starter load balance，就是相当于是间接地引入了 load balance 和对应的 common context 架构的内，这里面还有像 stored 的 SOP 和 test 都是一些辅助的一些功能。那么在这里面我们可以简单的去看一下对于 load balance，它的 palm 文件里我们可以看到第一眼看到这里面它依赖了 spring Claude comments 和 spring code context 的内，下面还有一些像一些校验，这是 acuator 相关的，那么对于这里面我们依赖的comments，它下面的结构也是相对比较简单一些。在这里面我可以看到对应的 Claude 端下面，它下面几个模块我们看起来是比较有一些共鸣的。这里面像我们的熔断器，我们的服务发，这里面的服务负载均衡，这里面我们的服务注册等等这些内，像，这个里面是一些更通用的一些信息。


对于我们注意 ITP 客户端构建的一种方，这里面还有涉及到一些PVC，这里面我们看它是 react 的一种方式的一些包装，这里面跟安全相关的一些内容，还有一些常用的一些工具类。像 configuration 里面，这里面会有一制动装配相关的一些内容，包括我们一些配置的一些信，那么对于我们唱 load balance 相关的内容，我们可以在这里面简打开 load balance 相关的内，这里面像最重要的我们会有一个 load balance 的一个注解，那么我们对 reset template 加上这个注解，它就可以积负载均衡来完成。那我们还通过这两个模块，比如我们这里面 spring code comments 跟对应的 spring code， load balance 它们之间的关系来看一下。


我们看对于 spring code comments 里面它可以定义一些抽象，比如这里面对 load balance 的client，那么这里面作为这个接口，那么它的实现在什么位置？我们看一下它的一些实现，在这里面实现，我们看这里面有 blocking load balance client，那么我们贴到这个对应的类里面，我们看这是我们一个具体的一主设的负载均衡的一个 kind 实，那么这个它的实现位置是在哪呢？在 spin code look balance，这也就是印证了我们的说法，就是对于 speak comments，它在这里面定义了一些规范，比如在 client 里面定义的这相关的一些规范，这是负载均衡相关的一些规范。那么对 swimcode load balance，对这个规范进行一些它自己的一些实现。


好，那这是我们来看到这个 spring code comments 跟 spring code load balance 之间的关，那么接下来我们继续看一下，不管是我们使用的 spring code comments，还有我们 spring code load balance，那么我们要依赖 spring Claude load balance，也就是它实现的负载金，我们只需要引入 spring code STARTER load balance 就可以完成。


那么依赖完这个 STARTER 模块以后，它对应的这些自动装配的信息有哪些？在这里面我们关心两个地方，一个是对应 spring code comments Meta info 下面的 spring factory，它有哪些内容？另一部分是对应的我们看 spring code load balance my info 下面的 spring pack。也就是说我们在使用到 spring code load balance，我们需要关心这两个炸包下面的自动装配的。那么我们首先来看一下 spring code comments 下面有哪些。


对于 spring code comments 下面有几个自动装配，也就是 auto configuration 的实现，这里面首先 load balance auto configurate，这里面我们特意加了一个Claude，也就是带在包结构里面有client，这就这个 load blanks out configuration，它属于Frank，同时还有一个同名的它属于 load balance。


所以这个大家要注意对于这个 load balance auto communication，它里面实现了哪些being，其实基于这个自动装配，它构造出来 rest template， load balance request transfer，也就是对一个请求的一个转，这里面还有 reset template customer，也就是说我们需要对 reset template 进行一些自定义的一些超。


这里面还涉及到我们 load balance 的intercept，也就是说一个拦截我们在做 reset template 请求的过程，通过拦截器把我们这个负载均衡的策略包含进去，这里面还有 load balance request，通过这种方式构建一个request，那么下面还有一个 reactor load balance client auto configurate，那么这种它实现的内容是基于 record 方式，就是也就是响应式的方式构建了一些filter，一些产方法的一些过滤器。那么还有就是我们这里 async load balance auto configure，这里面就是对应的，这里面是 reset template，跟这里面是 think reset template，其实我们重点关注 RESET template 的实现的过程，那么对于它的工作原理我们就都比较清楚了。


同时这里面还有一个 load balance being post process auto configure，我们看到这个 being post process，我们通常知道它是注意后处理的超这里面做的事情，我们看到这里面爱的 load balance 的，也就是说当我们在为这个注解去做一些解析的过程中，我们用到了 being post process，也就是我们通过 load balance Web client builder being post process 他做的事情是什么呢？也就是所有我们在 Web client builder 的这个对象上，使用 add load balance 修饰的这些方法，或者一些 bin 的d，那么它都会通过 bin post process 完成进行一后置的包装，通过这个包装让 Web 刊的 builder 完成了它实现这个负载均衡的功能。


好，接下来我们看一下 spring code load balance 下面对应的，这里面对应的也是我们看 load balance auto config 跟上面是一个同名的类，只是它对应的包结构是configure，下面或者它的模块也不一。那对于 load balance auto configuration 它住了一个什么呢？它这里面构筑 load balance row configure 这样一个bean，还有是 load balance client factory，这个是最重要，它通过 load balance client factory 的构建间接地引入 load balance client configuration，也就是基于这个注，去实现了的后面的一系列的一些必应的触手。


那么对于这里面我们可以看到 load balance kind configuration 它做了哪些事情？它构建出来两个最重要的bin，一个是我们是 round Rubin， load balance 就是这是一个轮询的一个负载均衡的一个策略。另外这里面提供了是 service instance list supply，也就是说这是一个具体的我们的服务实例的一个服务列表的一个提供器，那我们基于它的一个承叠的包装完成我们这个服务列表的获取。接下来我们看这里面。
Blocking load balance, client auto configuration.


也就是这是我们在使用过程中直接用到的一个负载均衡，一个 Claude 多，它是一个主摄性的，通过命名可以看。那么对于它这个自动装配的 auto configuration 里面包含了哪些病？这里面有 blocking load balance client，也就是说它是最直接的这样一负载均衡的客户端。同时它这里面会根据不同的策略会构建基于一个支持重试的一个 blocking load balance retry factory，这里面还有涉及到一些transform，也对于一些 cookie 的一些转化。


后面这里面是 load balance case auto configurate，也就是说我们在负载均衡来获取列表的过程，其实它是支持缓存的，那么支持缓存的话，它就避免我们每一次请求的过程中都要通过注册中心拉取一下我们的服务列表，也就是说对于一个性能效率的一个提高。


其实这里面对于 load balance cat manager，它有两类实现，一个是基于咖啡这样一个缓存工具，另一个它是基于 concurrent Hashmap 实现。接下来这里面还有一个 auto configure，这里面是 load balance States，就是基于统计的。那么我们基于这个 auto configuration，它实现了那 Michael meter state load balance life cycle，也就是它会负载均衡，它执行的生命周期去监听我们这些请求它的成功和失败。那么这样的话可以通过 spring boot 对应的acuator，它提供的 endpoint 暴露出来，那么我们可以基于一些监控报表获取到这些数。

