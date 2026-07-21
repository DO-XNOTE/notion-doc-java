---
title: 3-2 LoadBalancer架构设计-2（1109）
---

# 3-2 LoadBalancer架构设计-2（1109）

那么这样的话，我们看到了这些初锐的这样一个结构，那么我们可以切到源码里面去看一下它们之间的这些关系。那么在这里面我们可以看到对应的我们的 spring code comments 它的这些配置信息。在 string factory 这里面我们可以看到它里面跟 enable auto configuring 相关的信息非常多，但我们这次只关注跟负载均衡相关的一些内容。


这里面我们看到 load balance auto configuration，这里面也有 load balance being post process auto configuration，我们可以先看一下这个。好，在这里面我们看到这是 load balance auto configuration 它的一个实现，这是我们刚才提到它是有重名的。注意一下这里面我们关心的是什么？我们关心的 spring code com 对应的这样一个内容，另一个是支持 spring code load balance。我们现在关心的是 common 下面的，所以我们点到这里面，这就是我们对应的。


对于这里面我们可以看到它这个 bin 的定义，这里面是一个 reset template 的一个集合，我们看到它这里面通过 load balance 进行修饰，也就是说它的意义是什么？它会把整个我们容器里面 reset template 这个 bin 搜集到这里面，进行一些初始化的适配，那么这里面有 add load balance 的一个修饰，那么说它这里搜集的集合也是包含了 add load balance 的一个修饰的，这样才能会影映射到待会我们会具体的细节我们没讲，接下来这个 bin 是 small 的 installzing single，这个 bin 它的意义是什么呢？我们可以看到它是一个接，那么这个 b 也就是当我们的实例初始化完成以后，它调用这个回调，也就是对于我们这些 b 做一些特殊的处理。


其实在这里面它的实际意义也就是把我们的 reset template 进行一个 RESET customer 的一个注册的一个修饰，也就是其实它的逻辑，也就是把我们所有这里面通过 add load balance 的进行修饰的这个注解的这个 RESET template 进行一些拦截，它这里面主要涉及的拦截策略就是把我们的负载均衡策略映射进去，那么其实它底下会映射到这里面一些，这里面有一个负载均衡的 intercept 一个拦截器，这里面是 reset template CO，那么它基于这个 customer 它实现的制定义的操作。也就是说对于 reset template 它添加一个拦截器，这个拦截器的内容就是基于负载均衡的拦截器，那么在这里面我们看一下它这个负载均衡拦截器的是，这跟进去的话可以看到它最终进行拦截的一些操，待会回头我们会具体详细的去介绍一下。


这是我们在看到对应的，我们看的是 spring code common 下面这个 load balance auto configure 的一个实现，其他的我们后面我们详细的再去细节地去，那我们再来切换到我们的 spring code load balance，看这个下面会有哪些比较典型的，我们的一些自动装配的一些类，那么在这里面我们可以看到这里面也是基于 enable auto configuration，这里面有 load balance auto configuration 和 blocking load balance client auto configuration，还有一些基于缓存的 load balance cats 等等。这里面 load balance 一些统计信息的包装。


那么我们先看一下这个里面他做了哪些事情，这里面注意一下我们现在应该是切换到对应的 string code load balance 这个模块下的配置，在这里面我们看到这里面是一个是 load balance room configure，也就是分区的一个配，这是我们最关注的是 load balance client factory，那就是其实我们在构建 loadback client 的过程中，是需要一个 loadback factory 去获取我们的一些信息，那么在这里面对于在构建 load best client factory 的过程中我们可以跟进去看。


在这里面我们指定了一个 load balance trend configuration，也就是它的一些配，其实这个配置它可以理解为是一个 Java 的 configuration 类，这里面构建了一些bin，我们可以切进来看，我们看到这里面是基于 configuration 去实现的。


首先是这里面看基于这个 load balance client configuration，它是依赖到我们的 discovery enable，也就是说我们需要把我们的服务注册与发现的，在这里面它定义的是一个 react load balance，那么它的具体实现是基于我们这里面 road Robin load balance，也就是一个基于一个轮询的一个负载均衡的一个实现，那么其实在构建这个基于轮询的负载均衡的实现的过程中，它还是需要依赖到我们的服务发现的列表的一些信，那我们看一下对于这些它是怎么去完成的？在下面我们看这里面 spring Claude load balance configurations，这里面是debug，那么如果说 debug 我们不配置的话，它是默认匹配的，它这里面实现的是内容，是怎么实现？这里面是我们是 service instance list supplier 一个build，对，那么基于这个 build 对象它完成了几件？首先 with discovery Claude，也就是说它基于服务发现的一个客户端。另外它 with 开启，也就是它是支持缓存的，也就是说我们在定义这个服务实例的一个列表提供器的过程中，它基于两条策略，一个是我们这里面是获取我们的服务发现的客户端，另一个是它基于缓存，其实我们可以跟进来看一下在这里面他做了哪些事情。


为此 discovery client 它实现的内容是，当我们在创建这个 base Creator 的过程中，我们看一下它配是创建的过程是怎样。它首先是通过我们的上下文获取一个 reactive discover client，这个我们再去了解我们的服务注册与发现的过程中，我们知道当我们打开了 discover client 的过程中，我们也可以获取到这样一个必应对象，那我们基于这个 descriplan 的可以获取到我们的一个列表，那么基于我们的请求列表就是我们的服务列表去选择我们具体的一些信息，那么这是我们这里面是 with discover client 它实现的工。


另一个我们可以看到它是 with cats，我们这里面去选择一下，基于缓存的，那么每次开启他做的事情是什么？它也是通过我们的 bin 容器的上下文里面获取到一个 load balance cat manager，也就是获取到一个缓冲管理器，那么基于负载均衡的缓存管理器进行一层包装，那么就是它是通过开庭 service instance list 再进行一次包装，也就是说其实把 delegate 就传进去，也就是整个这个提供器就是这个 service intense 的 list supplier builder，它在构建它的过程中构建了多层的代理包装，比如说最外层我们是需要通过我们的服务发现获取到我们的服务发现的列，中间再包一层我们的缓存，那么再完成是给我们用户使用的 search intense list brand build。大家了解这个过程就可以。


我们看的对于 spring Claude load balance 一个简单的一个介绍，那么对于这里面我们看可以再去跟一下哪个这里面对于 blocking load balance client 他做的一些什么事情。对于这个里面我们看到这里面，是啊定义了我们最直接使用的也就是我们的是 load balance client，通常我们在做业务操作过程中所依赖的对象也就是 load balance client，那么至于这个死，嗯， Claude load balance 这个它有一个唯一的实现，也就是 blocking load balance client 基于这个实现就是也是我们的默认实，我们通过它它需要的一个参数也就是 load balance client。


这个 load balance client factory 大家应该还有一点点印象，我们是在这里面构建出了这个 load balance 的 client factory，那么在这里面它做一个参数注入使用，也就可以去进行我们的对象的一些获取。下面会有一些如果说我们是支持重试的话，它会有一些跟重试相关的一些内容。


好，那么我们回到这里，对于自动装配的内容我们就先介绍这一些，那么接下来我们看一下它有哪些核心的API，在这里面我们重点关注一下，对我们使用最多的是 load balance client，我们基于它去进行我们的一些负载均衡的选择，但是 load balance client 它继承了这 service instance choser，也就是一个我们的服务列表，一个选择服务实例的一个选择器。基于它去完成我们具体的一个服务的选择，那么 load balance client 进行一个请求的一个执行，那么同时跟 load balance client 对应的这里面它依赖的是activity， load balance 就是它具体的一个实现，同时它也实现对truth，也就是说选择我们具体实例的一个方法。


同时我们应该更关心这个当然是注解，它不是API，但是我们相对使用比较多，也是比较重要的，也是支持 load balance 的这样一个注解，它通常会运用到 reset template 或 Web client builder 上面去进行修辞，表明这个客户端的它可以支持负载均衡。那么另一个是我们对 load balance 的 client 端进行设置的时候，可以用到 load balance client 这样一个注解进行一个全局的设，这是一个核心的AP。那么接下来我们来看一下对于这个 load balance client 端它的一包装的情况。


首先我们看我们直接依赖的是 blocking load balance client，那么对于 blocking load balance client 它又提供了哪些？它里面它依赖到一个 load balance client factory，那么对于 load balance 出来的category，它底下就是我们可以通过 load balance client factor 里面获取不同的服务，比如说我们 nicos provider 我们可以指定，比如 service 一，这个里面可以 react load balance，那么基于 react load balance 它具体的 service intense list supply，最终我们是通过 service instance list supplier 提供出我们具体的实例列表。


那么这个实例列表里面在 react load balance 基于它的一个算法实，获取到一个具体的一个实，那么这里面可以是同时是支持多个实例的。比如说我们的服务一，服务二我们都可以通过这种方式去进行一个理，也就是说在整个包装的过程中，对于我们一个应用，我们只需要关心 block balance China 就可以了。具体这些它是怎么构建起来，我们其在做应用开发过程是不需要理解的。当然我们现在基于源码的一个深入解析，当然我就在这里面告诉大家他们之间的关系的点，待会我们再通过源码之间调用链的一个追踪，让大家了解的更细致一些。好，那么关于这个 load balance 的架构设计的内容我们先介绍到这里，接下来我们会进行一些核心源码解析内容的讲解。

