---
title: 3-3 LoadBalancer核心内容源码解析-1（2545）
---

# 3-3 LoadBalancer核心内容源码解析-1（2545）

同学们大家好，这章节我们介绍一下 spring Claude load balance 的源码解析。上一章节我们了解了负载均衡涉及到的源码及工程，以及了解了一些负载均衡它那个自动装配的一些原理。接下来我们介绍一下 load balance 初始化的流程，其实在这里面它的初始化流程， load balance 它对应的自动装配的功能是有些类似的，但这里自动装配可能我们对它的顺序了解起来比较麻烦，那么我们要介绍它的初始化流程，那么它应该有一个顺序性的去初始。


其实对于我们来说，我们更关心的是这里面我们看似 blocking load balance client，那么如果说我们在初始化的过程中构建出 blocking 的 balance client，那么就可以理解我们这个初始化过程完成，那么我们这样的整个它初始化的过程中，我们通过倒序引导的方式，比如说我们看到了 blocking load balance client，那么它是怎么初始化？我们知道它是通 blocking load balance client auto configuration 来初始化完成。至于比如说它们之间的关系是怎么构建出来的，我们可以通过代码引用关系去找到对应的这个 block load balance 串的，它是由这个对应的一个自动装备来完成。


那么我们再去想一对于这个 block load balance client，它依赖的一个对象是什么呢？它需要依赖 load balance client factory 这样一个对，那么所以在它的初始化之前，我们应该要有一个对应的 load balance client factory 这样一个对象来完，那么这个对象它是通过这里面 load balance auto configuration 来完成的，既然它是这样一个关系，通过它来完成，那么我们就知道这两个自动装配它的顺肯定是我们首先 load balance auto configuration，然后是 blocking load balance client。
那么既然这样我们就知道了这两个自动装配的顺序，那我们先看这个制动装配顺序，它制动装配做了哪些事情？首先构造出我们的 load balance client factory，然后它是在 load balance client factory 构造的过程中，它引入了一个configuration，也就是 load balance client configuration，那么基于这个 load balance configuration 去构建出了我们当前的这里面，这是负载均衡的策略，这里面轮询的策略以及我们在构建这个 instance list supply，也就是我们的服务实例的这个列表的一个提供者。


这个服务列表提供者它通过多层的包装，这里面的包装首先是它是通 service instance list supply builder，通过这个 builder 来构，那么这个对应的 builder 它构建了哪些事？它其实做的事情也就首先它是构建基于一个 blocking discovery client，也就是基于我们的服务发现获取到我们对应的服务列表，也就是它通过我们上一章节讲的注册与发现的服务发discover， client 获取到对应服务它的一 instance 列表，这里面再通过缓存进行一层包装，这样其实当我们 blocking load balance client 真正获取这个服务实例的过程中时，首先是通过缓存，那么缓存如果说没有的话，它通过我们的服务发现去找到对应的一个服务实例的列表。


然后创立通过我们这里面对应的服务列表我们的负载均衡策略，这里面我们比如默认是轮询的负载均衡，通过这个策略随，也就是说通过顺序去选择我们对应的一个，当然我们也可以替换为一个随机的一个负载均衡的车，这样就最终得到我们通过负载均衡获取到我们这些具体实力的一个效果，那么这是我们初始化的流。


但这里面大家要注意一些，如果说我们只是初始化，并没有去发起调用，那么其实 load blanks client configuration 这部内容它是不会去装载，它只有当第一次执行的过程中，它才会去进行它的这样一个初始化的过，那么接下来我们来看这个正常执行的流程，那么其实我们了解了它的一个初始化的流程，那么对于执行流程就更容易理解一些。


这里面我们看到首先我们顺序好像是反过来了，我们首先从 block load balance client 来进行一个调用，他们我们通首先措辞去获取到我们对应的一个服务列表。那么这里面我们看它获取的过程中，其实它是间接的去调 load balance client factory，通过 load balance 看的 factory 去通过 get instance 的方获取到我们对应的一个 active load balance，其实这里面我们对应它的实现也就是我们这个轮 round Robin load balance 的一个实现，那么基于这个实现它在进行对应选择我们的实力，那么这里面就会使用 service instance list supply，那我们知道它作为一个接口底层有多种实现的包。


第一层我们要直接面对的，也就是对基于缓存 safety intense list supplier，那么它的下一层级是通过了 discover client service intent list supply，也就是一个服务发现的一个列，那么基于这个列表，它通过远程的 active discover client 远程调用获取到我们对应的服务列表，那么通过服务列表里面在依赖这里面的一个负载进行的策略，最终获取到我们的一个 service instance。


但是基于我们默认的基于 Nicos 的服务注册与发现的一个注册中心，那么我们这里面得到这个对象是一个 nicos service intense，我们可以通过这个 Nike 的 service intent 获取我们这个服务实例的一些基本信息，比如说它的 host 和它的端口号，那么这样的话整个负载均衡的流程也就执行完成了。现在我们基于源码来看一下整个执行的过程。首先如果说我们是基于 spring code common 的话，也可以去进行这样一个阅读，但通常情况下我们再去看这些自动装配的内容的时候，它们之间的顺序其实我们不太容易去把握，所以这里面我们是构建出了一负载均衡的一个模块，也就是我们的一个模块工程来去跟大家去演示一整个负载均衡，它初始化的过程以及它执行的流。


那么我们首先来看一下这个模块，嗯，对于这个模块我们看一下我们依赖的内容。这里面我们首先是依赖阿里巴 nicos discovery，也就是说它支持服务发现。另外我们这里面依赖了string，Claude，starter， load balance，我们是用到了 load balance 的一个 starter 来简便的去引入我们的内容。下面是我们引入一个常规的，像这里面 store 的 Web store，accuator，以及仍不可和我们的一些测试相关的一些内容，这是我们的一个 palm 依赖。


那么我们来看一下我们对应的 application YML，这里面我们并没有过多的特殊设置，这里面我们标明了一下 application name，也就是 ICL load balance，这里面 SCR 是对应 spring Claude load balance 的一个简称。


端口号我们可以做一个取，这里面我们配置上我们的当前 nicos 的一个服务地址，我们在使用负载监控策略去调用我们的 provider 端提供的服务的功能，我们的服务最好是有多个实例来玩，这里面我们可以看一下 nicos 我们这里面的效果。对于这个 nicos 我们现在是一个集群，现在实例数目有 4 个实例，它当然 4 个都是健康状，我们可以在这里面点开详情看一下它分别对应的端口号。好，这里面我们可以看到这里面是 80828083 到80848085，这四个是都属于一个正常的一个状态，这样我们再接着看我们的 SCR load，这是我们再看一下我们的 load balance 对应的applicate，这里面我们正常使用了 enable DISCORD client，也就是说我们的服务发现的一个机。


这里面我们并没有看到跟 load balance 相关的内容，那么这里面我们看一下现这里面倒并不是强相关，嗯，我们定义了一个 rest template， rest template 里面一个是通过了 load balance 进行修饰的，一个没有，我们这里面默认是表明它是默认是不需要 load balance，那么我们可以通过这两个不同的 RES template sling 进行一些演示。
在这里面我们看一下 Demo control，这里面我们引一个是 load balance client，也就是说我们通过对应的 load balance starter 引入来的 load band，一个是因为我们刚才知道对于 load band client 它默认的实例是什么呢？这里面只有一个 blocking load balance client，那么就是它的一个实，这样对于 rest time play 的，我们在嗯使用的过程中可以去注意，因为我们这个负载均衡它是作为客户端使用的，那么对于客户端使用的话，我们可以通过单元测试的方式去调用。那么对于服务端的话，它需要暴露端准备就是服务调用，所以说它应该要通过，最好通过 Web 启动起来。那么对于它一个负载均衡通过客户端消费的，那么我们可以直接通过单元测试来去验，那么在这里面我们看一下我们单元测试，也是用到 stream 部的 test 进行单元测试验。


这里面我们看我们首先对于我们这个 load balance 负载均衡，它需要验证的服务，它的 service ID 是对应的 nicos provided，那么跟我们这里面是对应着的，也就是我们这里面是对应 neckles provided 的，我们看这里面暴露了 4 个端口，我们可以去调用。


那么分别，我们看这里面依赖注入的是，首先 the load balance client 以及我们的是两个retemplate，对， reset template net 这是我们是支持负载均衡的，这个是不持负载均衡。那么首先我们来去验证一下我们初始化过程，嗯，这个对应的 load balance client 它是如何初始化完成的，这里面要区分两点，假如说我们只是进行初始化，但我们并没有执行 load balance clients 这个 choice 的这个服务列表的筛选，那么我们刚才提到这里面是对应它初始化的内容。在这部分内容，如果说我们不调用的话，这一部分内容它不会进行初始化，所以说只有我们在调用的选取服务实例的过程，它来进行初始化，这也可以理解为是一种懒加载的一种实现方式。好，那么我们现在可以通过单元测试的方式去验证一下。


好，那么我们现在去通过我们 test load balance 一个初始化的操作，当然初始化的同时它也会进行我们这个服务实例的一个选举。好，我们现在开始启动debug。好，我们看首先它中断的位置，当然这些断点都是我有意思的去加上去来的。如果说大家在初始化的过程中并不知道它是在基于什么方式去运行的，那怎么办？那我们可以一个比较不是太好的方法，但是它可以解决我们的问题，也就是说我们可以把所有对应我关注的这个对应的 Meta info 下面的 factory 文件，我们都可以把它可以加上断点，那我们执行的过程中看它中断到什么地方，那就可以说明它是在什么地方进行了一个就是初始化的过程，就会走到了这一点。


所以说比如这里面是 load balance auto configuration，以及我们的 load balance cat auto communication 以及 blocking load balance plant auto communication，那么好，它现在已经是中断到了 load balance auto configuration，我们看它是在这里面对应的一个制动装配的内容，所以说它初始化的过程中肯定是基于这些制动装配的路径来执行的。


好，那么第一步它在这里面是需要去创建我们的 load balance kind factory，我们在这里面跟这里面对应一下看，首先是创建我们的 load balance client fact，接下来我们来看一下它处理的事，那么我们可以跟进去，我们看一下这个构造方法它做了哪些事情。


刚才我们看它的构造方法，在这里面指定了一个它是调用 super 的方法，也就是父类的一构造方法，这里面指定了一下 load balance client configuration，我们先看一下它的这里面也就是基于 Java configuration 的方式配置了一些bin，这里面我们关心的是round， Robin NODE balance，也就是一个通过一个轮询的方式进行一负载均衡的一个策略。


那么我们还回到这里面，那我们接下来跟进去看一下，这是有 name space 和我们的 property name，这里面我们看到它是两个常量，那么我们嗯下一步跟进去，在这里面的话其实就是整个构造就完成，那么完成我们现在是这是一个初始化的过程，我们看整个这个对这个 factory 的构造完成。


那么我们接下来需要做的是什么？这里面是对于这个 client factory 进行一个 configuration 的一个设置，我们看一下这个 configuration 设置的内容是什么，这里面我们点进去这里面看一下它对于 configuration 设置的内容，是两个 list 里面两个对象，这两个对象分别是我们看到它是debug，对应的是 load balance auto configuration，我看另一个也是以 debug 的为前缀，这里面对应的是 blocking load balance kind auto configuration。


那么看到这个的话，我们跟这里面对应上，其实也就是这两个自动装配前面加上一个 debug 的一个前缀，作为我们一个默认的一个这里面配置的内容 configure 内容，那么这样的话它把它通过 name 和 client 对应的信息装配进去，这个最终会在初始化的过程中会用到，这样我们执行完成。


也就是说对于这个 load band transfactory，它是构造完成了，但是构造完成以后，我刚才提到它是一个懒家的那种法子，只有咱在第一次使用的时候才会进行真正的初始，那么它现在获取到这个 factory invoke，这已经跳到对应 being 初始化的一个过程，我们跳过去。

