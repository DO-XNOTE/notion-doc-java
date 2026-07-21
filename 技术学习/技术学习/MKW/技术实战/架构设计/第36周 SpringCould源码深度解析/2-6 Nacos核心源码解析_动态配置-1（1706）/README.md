---
title: 2-6 Nacos核心源码解析_动态配置-1（1706）
---

# 2-6 Nacos核心源码解析_动态配置-1（1706）

同学们大家好，我们接着介绍一下 NICOS 的源码，这里面我们主要介绍 NICOS 的动态配置源码解析。对于 NICOS 的动态配置，我们也是分为 Nike 的客户端的处理和 Nike 的服务端的处理。在 Nike 的客户端里面，我们使用的方式还是依赖 spring Claude、阿里巴巴对应的 nicos 的一个 STARTER 配置，通过 STARTER 配置，我们这里面是肯定要有它对应的自动装配的功能，通过它的自动装配这些 auto configuration 来来启动我们配置项的一些加载。


这里面的配置项加载主要是我们通过远程的 negos 服务端加载到了我们的一些关心的一些配置项。我们配置项加载完成以后，这里面需要我们是动态监听，因为我们对于服务端配置的变更，客户端如何感知到并进行一定词的一个刷新。首先我们要动态监听到我们的配置中的改变，同时对于我们使用了 press scope 这样的一种状态的话，当我们配的我们的一些属性，它可以做到一个动态的一个刷新的一样过程，这是我们客户端相关的一些内容，对应的自动装配置加载我们的动态监听和定域刷新。
这几个知识点对于我们 NECOS 服务端相对来说比较简单一些。对于 NECOS 服务端，它也有对应的 config Controller，提供我们获取配置的服务，同时提供一些动态监听服务的操作。这里面的不管是我们动态监听还是获取配置的过程，它主要涉及的一些长轮询的一种操作，看一下动态配置 NICOS 客户端自动装配的内容，其实我们通常关心对应的装配内容，我们会关心 spring Claude start，阿里巴巴 nicos config 对应它下面的 spring 的 factor 里面的一些自动装配的信息，在这里面我们可以去看一下对应的这个配置文件。


对于我们 spring code start，阿里巴巴 nicos configure 有一个是 bootstrap configuration 这样一个装配内容，我们在其词学习 spring boot 的过程中，只关注的像这里面对应的 spring promote put auto configure， enable auto configure 以及错误收集或者 property source loader 相关的一些内容。


对于 spring framework Claude boot strap 下面的这个 boot strap config reason 这个 k 其实我们并没有涉及到，其实它并不是 spring boot 默认的自动装配的一个内容，但是因为我们在使用 negos 的时候，它需要 negos configure，不是 shop configuration，它只用这种方式装配的，我们必须要了解一下它的原理是怎样的。


回到这里面，其实对于这种的一种装备方式，它并不是 spring put 默认的装备方式，它是 spring Claude context 实现了一种新的一种装配方式。其实这种装备方式的逻辑是 Boost drop application listener，它作为一个监听器，监听到 application 英文的 preper 的这个event，也就是说当我们这个环境信息在执行之前，就是说预处理之前我执行的一些操作，这个刚好跟我们 nicos 动态配置它的一些处理的这个时间点是对应上的。也就是说我们在解析 NICOS 远程的数据的过程中，它应该是在我们这个环境信息处理完之前去做的，也就是说在系统初始化之前去做的这些事情。


这里面我们，嗯，待会通过源码去看一下怎么通过这边 Claude context 这里面的 Boost listener，通过各种逻辑的关联关联到我们对应的 nicos configuration，不是 trouble configuration 这样一个配置的信息，我们在这里面只关注对应的是阿里巴巴 nicos config 下面的这些自动装配信息。


对于 nicos configure boot trouble config reason，它下面构建了几个b，对于简单比较容易理解的，像 nicos configure property，也就是我们跟配置相关的一些属性设置，这里面还有 nicos config manager，可以理解为它是对于 nicos 客户端和服务端之间的一个包装。


其实这里面最重要的一个信息就是 nicos property source locate，这其次是什么意思？也就是说我们通过 macos property source locate 进行配置文件的定位，通过配置文件定位器获取到配置文件的内容，那么这里面有 necos configure auto configuration，对于这个自动装配的对象，它处理的信息跟这里面是有一些大同小异的。
这里面像 Nicos computer property 跟它是相关的。还有 Nicos Refresh history，也就是说 Gecko s 动态刷新的一些历史记录，这里面还有 necos configure manager 跟这边对应的，其实这里面还有一个 nicos contact repress，也就是说当我们在配置这些依赖的配置的时候，它进行刷新的时候，我们怎么处理？这是我们自动装配相关的一些内容。接下来我们看一下配置加载的时候涉及到一些情况。


对于 nicos 配置加载，我们知道它配置加载的是一些远程 nicos 服务的配置文件，其实它是需要我们使用到 nicos property source locate 进行首先 Loki 的定位，它在定位的过程中其实依赖到叫这里面是 config service，对于 config service 它进行我们数据加载的过程，其实它是逐步的一个调用的过程，它通过 nicos property source builder 构建出这个对象进行，像我们通过 Loki load application configuration load 在它执行的过程中它会调用 load nicos date 一 person 的。接着它真正去调用 nicos property sauce，也就是通过加载的方式加载到真正的原始的一些数据。这里面我们看到 nicos properly source builder 它做的事情，其实首先它要构建出 property 对象，在这里面即将 load necks date 进行一个数据的加载。这里面最终我们会使用到 nicos configure service，通过 nicos configure service 它的 get configure 去获取到我们的一些数据，最终我们其实 get campaign 的数据操作，它还是委托我们这里面的 kind work 去进行一些数据操作。


对于这里面我们看到 client worker，它通过 get Server configure，最终在这里面会执行 agent HDP，进行一个 HDP 请求，其实 IP 请求它发的url，也就是这里面的 v c s configures，其实跟我们刚前面讲到的我们的服务注册 naming 是一个对应的关系，那是服务注册，这里面是动态配置，通过这样一个 URL 去访问到我们服务端的一些内容，这是我们的配置加载。


接下来我们看一下，这里面是动态监听和订阅刷新，这里面的动态监听和订阅发音听起来好像是一致的一个意思，这里面就是定位上是有一些区别的，比如动态监听，这里面更多的是关注于我们程序跟 Nicos 的交互，比如我们 Nike 的 config service 它要做的思想，这里面最重要的是 kind Walker 及这个长轮询的一个 reinable 这样一个实现。最终其实这个看到 worker 它会定期的去执行一个 check update。 config SPR，也就是我们的 string 的缩写，在这里面我们动态的去更新。


这个更新的过程其实就是访问了我们服务端的一个 Controller 的一个请求，对应的是这里面是 config listener，我们基于这个请求通过服务端的一些数据交换去感知我们这个配置的变化。这是动态监听，它主要用来去跟 NICOS 服务端进行交互，触发我们服务的一些变更。


当我们发现我们的配置变更以后，我们要做什么事？这里面要看订阅刷新，更多的是关注我们 Nicos 的配置变化，如何把这个变化感知到我们 spring Bing 的配置项里面？其实这里面涉及到一个 nicos contact refresh，也就是说它是一个主要是用来进行我们的一个 context 上下文刷新的一个工具。基于它的刷新它是怎么去做的？最终它会通过 refresh event listener，也就是说我们需要一些刷新的一个四件监听器，监听这个 refresh event。得到这个 restart event 以后的它最终会调用 context refresh 进行一个 refresh 操作。


这个 refresh 刷新的操作通常是它只关注哪些在这里面是 refresh scope 修饰的这些bin，它会进行一个刷新。那么如果说我们没有对应的 refresh scope 这种修饰的这个bin，它不会感知到这个 nicos 的动态刷新，就是这样一个逻辑。


接下来我们看一下这里面的服务端相关的操作，对于服务管相关的操作关注比较简单，对于不管是获取配置还是动态监听，对应的都是 config control 下面的方法，像这里面获取配置的话，它对应的是 config Controller，下面的是 get config，最终它会通过 config Server light in near 进行 do get config 的操作。这个动态监听也是通过 config Server light 音乐进行一个 do pouring compete，也就是做一个长轮训的一个配置的相关的操作。


这是我们首先对于 macos 的动态配置进行简单的流程的一个概述，接下来我们通过源码去了解一下整个 NICOS 动态配置的它一些流程的源码，实现切到自动装配的逻辑，我们看一下这个自动装配逻辑是如何实现的。切换到对应的源码，这里面是 spring Claude start，阿里巴巴 nicos config，我们切换到这个对应的 spring factory 的文件，看到这里面的 Boost trouble configuration，我们知道它这个并不是 spring boot 默认的一个加载的对象，它对应的这个 next compare boot configuration 它是如何加载上来的？所以说我们需要根据它的一些路线去找一下它的一些点，也就是说按图索骥。


在这里面我们先看一下不是刷宝 configuration 这个类，它是出在什么地方，我们看到其实找不到以后，我们发现它是个注解，那这个注解只是说明了一下，可以看到这里面在标明了这个接口，它在 spring FEX 里面去一个配置。通过这些的话，我们可以看到 string Claude context 的这样一个炸包下面，既然它在这个炸包下面，我们看一下它的 spring factory 里面有哪些内容。


对应的在 spring factory 里面也有这样的一个配置， string 的 spring framework Claude boot strap configuration，其实我们可以看到其实这个生效的这个配置应该是在我们的 spring Claude contact 完成的。


我们通过根代码的话，其实发现一点就是这里面的是 spring formal contact application，对这个 listener 这里面定义了一个叫 bootstrap application listener，那么我们看一下 bootstrap application 他做了哪些事情，其实在这里面他做的事情比较多，其实我们需要关注一下，我们聚焦点在这里面是有一个最重要的方法，就是说他按 application event，也就是说他监听一个 application 的事件。


那么这个事件我们可以看到它，其实也就是说当我们的环境信息在初始化完成之前进行一个事件，也就是说预处理的一个事件，在这个预处理的事件过程中，它其实实现了一些操作，这里面你看它会找到一些初始化器，通过这些初始化器来进行一个数据化的初始化操作。除了这些初始化器的话，这里面还有一个操作，我们看一下这个是不 strap service context 的，那么我们看一下它这里面做了什么事情，在这里面做的事情跟到最后这里面有一个比较关键的点，其实这里面就是说它通过对应的一些信息进行一个 build 的操作。我们可以看到在这里面通过 builder 的时候，它传入一个 source 的source，就是 Boost rub import select configuration。
看到这个 import selector 的话，其实应该有一些印象，其实它是通过这种方式去引入了新的一些配置，那我们切进来看一下它的配置的内容，通过这个 Boost trouble import select configuration，它引入了一个import，对应的也就是 Boost trouble import select。


我们跟进去看一下它处理的内容，在这里面对于 select importers 它做的一些处理是怎样的？它是这里面使用到了 spring factory loader，通过加载我们的 factory names，对应的是 Boost shop configuration，那么我们看到这段代码的时候，对于这个 k 的一些配置应该有已经理解了，其实它是通过这种方式去构建了一种新的一个加载的规范，也就是说 swing Claude context，它构建了一种新的加载规范，就是 Boost drop configuration，通过这种方式也可以加载到我们的上下文里面。看到这一点我们应该会很理解了，对于这里面是它配置的 nicos configure boot strap，它也会在适当的时机去加载进去。


加载完成以后接下来要做的事情是什么呢？我们可以看到它加载完成以后真正要生效的事情其实是对应的 nicos pop source locator，它进行我们的 locate 的一些查找，它其实处理的逻辑是在这个里面，我们可以看到这里面有个 property source boot shop configuration，它是在哪个类里面？它是在我们这个配置，通过 Boost shop configuration，它配置 property source Boost shop configuration。


那么我们看一下它的实现，在它这个实现的过程中，它是实现了 application context Instant ride，也就是说它是一个初始化器，初始化器的话它肯定会执行这个初始化操作，在这个初始化操作的过程中，我们可以看到他获取到了所有的这些 property source locator，也就是说他把所有的这些属性源文件的定位器都做成一个集合，进行一个批量迭代的去处理其实最重要的就是在这里面 locator 进行 locate 的时候会获取一些信息。


这里面我们应该有一些感觉，因为我在这边定义了一个 nicos property source locator，它是通过 nicos boot travel configuration 定义出了这个bin，这个时间它已经定义完成了，所以说它其实在这里面去执行的过程中也能获取到，最终它其实在这里面去进行 locate 的locate，我们这里面可以去获取到它对应的一个实现，这样也就是能找到了。


我们看这是 Nicos property source locator，通过它的 locate 操作的话，真正的去执行我们 nicos 的动态配置跟 nicos 服务之间的一些交互的关系，通过 nicos config manager 它获取到 config service，它会逐步的去通过最终对应的，这里面是 property source builder，通过 builder 的操作最终获取到我们对应的操作。


我们这里面看到这是 builder 对应 builder 的内容，重点关注这里面的操作，这里面有几种方式，它首先是加载这个共享的配置文件，加载一些扩展的一些配置文件，我们关注它，这里面 load application configuration，这我们看它实现的内容是什么？我们点进去看一下它实现的内容，其实我们看关注几个重点，这里面是 load necks data in percent，如果说我们在加载的过程中，我们看一下它去出了哪些事情，跟进去看一下在这里面加载的过程中，其实它会通过我们获取到 did group ID 进行一个 k 的一些定位去处理的过程中，这里面我们看那这是 load nicos party source。那么我跟进来看一下，这里面就去一个加载的过程，应该重点超车就是我们超屁 source builder，它的 builder 的过程。跟进来看一下， builder 超出的过程中，我们可以看到它是通过 load necks date 进行一个数据的加载。


跟进来在这里面看一下数据加载的过程，在数据加载的过程，我们可以看到它，它是通过依赖了 config service get config 的操作去进行我们的远程数据的加载。那对于 config service，我们再跟进去看一下它的处理，这里面 config service，我们得到 nicos config service 的一个实现，这里面是 config get config in near。在这里面我们可以看到首先它会加载本地的配置，如果本地配置不存在的话，它会接着去通过 worker 去 get server config 的方式去操作。


我们可以看到这个 worker 它是对应的 client worker，它进行监听的一个处理。我们通过这个 get Server configure，我们可以看到它通过 client worker 去获取具体的一些配置信息。那在这里面我们看到定义了一个 http reset recell 的，也就是说它的一个请求的一个结果，对这个请求结果它会进行inforce。


在这里面首先是构造了Prometer，把我们的 data ID group ID，如果说涉及到多租户的话，这里面会还有对应的 tent ID，有 tent 一个租户的一个标记，通过这个 agent 它就是对应的我们的是 LCP agent，通过 HTP agent 去发出一个 ITP 请求，是那 SP guide 请求，对应的 UL 就是我们的 configure the Controller 对应的plus。这里面我们可以看到它其实对应的是v， c s 加上 configurs 这样一个配置。


其实通过这样一个 HP 请求，向我们的服务端发起请求，得到一个对应的结果集，得到结果集以后，对结果集进行一个反序的话，它构建成我们一个属性文件，整个这样的一个处理逻辑就已经完成了。这样 tell 最终能达到通过 nicos property source locate 获取到我们对应的数据的一个过程。

