---
title: 5-4 Gateway核心源码解析-2（1432）
---

# 5-4 Gateway核心源码解析-2（1432）

还是住了不少功夫的，如果说我们真的不小心把 spring boot start Web 或者说 spring MVC 这样一个模块引入进去以后，它就会有这样一个提示，那么这里面还有其他的一些像支持一些熔断器的 auto configuration 及我们这里面的一些监控相关的一些信息，以及 get 为 Redis auto configuration 等等这些内容。


这里面还有另一个比较重要的，就是 get away discover kind auto communication，这就是说我们通过我们的注册中心服拉取我们的这些服务发现的配置，进行我们网关的一些映射，知道了我们的自动装配这些启动的过程，那么我们可以通过 debug Paas 去启动一下，对于我们这些关键的这些组件的初始化，我们可会有相应的一些断点，我们可以关注一下。


那么现在我们可以通过 debug 的方式去启动，我们现在去执行启动许诺过程会涉及到一些初始化的按钮，我们可以快速的去浏览一下，我们知道它一个启动的过程是怎样的。好，这里面我们去，我们看这里面是我们在初始化我们的 root locator 的时候去执行的 root being dependent load locator，去这样一个初始化的过程。好，我们其实我们里面的代码我们可以简单的去看一下这样一个构造方法来执行的过程，我们就不会去细致地去一行debug，我们去跳过这个断点，我们去看下一个，在这里面我们可以看到它执行的是构建这个 primary root locator 的一个过程，这里面首先通过我们的 compose 的 root locate 进行一层包装，然后带动 case locate 包。我们也可以在这里面去看一下我们当前的 root locate 它得到了哪一些？b，我们可以看到它得到的两个病因，一个是 root definition local root locator，也就是我们刚才上面这个对象去构建的。


另一个我们可以看到它是 road locator builder，那么 road locate builder 它的内容我们看它是基于 number 的表达 4 去获得的这样一个bin，其实它的内容也就是我们其实在我们程序里面去设置的内容，也是我们在这里面我们，我们应该有印象，我们在这里面是通过 customer road locator 去构造的我们一个 road locator，那么它其实在使用的过程中是使用的，像 road locator builder，我们可以看到像如果 location 的 builder 去构建出来的这个我们定义的这个路由信息。


这样的话我们整个程序的上下文里面原生的，或者说是我们原生的这些 road locator 是两个对象，一个是基于 road locator builder 构建的，另一个就是 road definition road locator 只有这样的方式好，我们可以看到在这里面最终构建我们的以及 catch 的，所以说看到这里面我们去想一下，其实如果说我们在构建程序的时候，对于这里面这个必应的构建，我们应不应该去配置 ad primary？如果说配上这个 ad primary 的话，可能我们得到的预期就不一样，因为如果说我们在这里面配上 ad primary 的话，我们就相当于是把这个进行了一个复写，那么进行一个复写以后，这个对应的 roadlocator 它就不会再进行初始化了，或者是对相同一个 roadlocator being 进行 primary 的话，会造成一些冲突。


好，我们继续跳过当前的论点，我们看到这里面，我们看他开始去构造了我们的 road predicate handler Mapping 了。其实我们得到这个 road handler Mapping 以后，就整个我们的 Web Flex，它的一个容器，也就是它这个 handler Mapping 的主装就算完成了。这样的话我们其实就是我们可以简单的理解了一下这个启动自动装配的一个过程，那么接下来的就涉及到一些注册的内容，这就不再是我们所关心的一些内容了。


好，那么我们现在其实还回到我们的PPT，看到我们初始化的流程，其实最终是当我们把 road practical 的 handler Mapping 构建完成，就整个初始化流程就执行完了。只是我们在构建它的过程中所依赖的这些 road definite locator 和我们的其他的一项相关的一些信息，它会有一个初始化的一个过程。


我们来看一下 Gateway 它执行的流程，其实在 git 位执行的过程中，我们在这里面介绍的它首先还是通过我们的 root practice handler Mapping 作为我们整个 Gateway 的入口，那么在这里面我们最终还是通过像 lookup root，也就是通过查找我们的路由信息，这里面通过 road locator 去间接的我们通过我们的基于我们的 captain road locator，到我们的主合 road locator，再到我们具体的我们可以是 road declining road locator，或者说是基于 road locator builder 构建的这些 locator 来进行一些我们这些路由信息的一些组装。


那么其实在这里面进行路由信息的组装，我们最终可以获得到的一个对象就是我们的 filtering Web handler，那么基于 Web filting Web handler，它会在我们的 simple handler Adapter 里面进行执行，最终它的执行，也就是说间接的去调用 filter Web handler 里面的 handler 方法，最终是其实执行我们 Gateway 提供的每一个对应的路由它这些filter，那么执行 filter 的过程就是把我们的 filter 构建成一个组装的 filter 链，那么去进行一页执行。


那么对于 filter 链来执行的过程中，我们还是关注的我们这里面的是 global 的filter，也就是全局的 filter 以及我们当前路由对应的filter，那么这时候我们可以理解为我们整个 Gateway 的请求功能执行的流程，那么如果说我们在放大了整个我们基于 waterflex 的一个工程来看我们在执行的流程，我们可以在冲这边去对应看一下，在这里面我们看它请求的过程中最终其实是通过我们对应的 h t p Handler，这里面会涉及到像 react HTP Handler 一个 Adapter 最终和我们的 Server light ENTP handle Adapter 一个映射，它最终会请求执行到 Web HTTP Web handler 的Adapter。


那在这里面会有一个转换，它会把我们的 HTTP handler 转换成一个 Web handler，那么转换成 Web handler 一个过程其实就会被我们的 Dispatcher Handler 进行捕获，也就是说我们可以理解为所有的 Web Plex 的请求，它都会请求到我们的 Dispatcher handler，那这里面其实它处理的过程就首先它最重要的话就是 Handler 方法才会获取到我们 get Handler 对象，那么这里面我们去需要做一些区分的是，其实这里面就会涉及到我们对应的 handler Mapping，那么如果说我们在默认的 Web Flex 的服务的话，它用的是对应的 debug 的 request Mapping 的 handler Mapping。


那么如果说我们涉及到我们网关的话，用到的 Mapping 也就是这里面我们的 road predicate handler Mapping，其实也就是说我们在插到 Handler 的时候，它是从哪个对应的映射里面找到我们的Handler，那么其实找到 handler 以后，它执行的逻辑其实是一样的，这里面就是 invoke handler 在 handle resolve 的这个，其实执行完这个过程我们这个 get v 的请求已经执行完成了，但其实这里面会有一些区别。也就是说如果说我们正常的 Web Flex 请求，它会通过我们的 request Mapping handler Adapter 进行处理，这里面会涉及到 Emock handle， master handle， rest handle 相关的一些处理，最终我们把数据通过 SCP master writer 我们渲染出去，那么这里面是 get v 的情况，对于 get v 的情况的话，它会得到我们的是一个 filtering Web hunter 这样一个它。 get hunter 会得到这样一个对象，那么基于这个对象它是一个全局，我们可以理解为是容器里面唯一的一个bin，那么基于这个b，它会通过 simple handle depth 进行执行，那么真正执行的过程其实也就回到了我们刚才提到的，这里面会执行我们 gateway 的一个filter，那么就是这样一个执行的过程。那么现在我们可以切到源码里面，我们去通过源码来分析一下整个执行的一个流程。


首先在这里面我们先看一下我们这里面定义的这个 road locator，也就是我们在这里面去定义了几个路由。首先比如如果我们访问 provided 这里面只定义的一个ID，那么我们访问的路径是以 provided 作为我们的请求的前缀，那么他要处理的事情就会把这个请求进行转发到我们这里面的，嗯， local my local 8081 也就是说如果说我们以 provider 作为我们的请求前缀，会映射到这样一个请求我们的弟子，那么如果是基于 consumer 的话，我们会检映射到 8091 这里面。


open fan 是 8092 这样一个映射的一个过程，那么如果说我们再去想一下它真正执行的过程，我们怎么去作为我们整个请求的一个切入点，其实我们可以看到如果说我们基于这里面去看的话，其实它在执行的过程中我们会涉及到我们的 road predict handler Mapping 的一些，这里面就会涉及到 lookup router，那么我们可以在这里面也还切换到我们这个类的实现里面。


filter predicator handle Mapping，那么我们可以看到在这里面它会肯定会执行到我们的 look up 的router，那么如果说我们在基于这个逻辑去看的话，其实我们的所有请求它都会执行 Dispatcher handler，那么我们也可以在这里面去切换到我们的把我们的dispatcher， Handler 把它打开，那么在这里面我们可以看到对于 despite Handler 它也会进行执行到这里面，对于 discussion Handler，我们应该知道它执行的是我们的 handler 方法。


那么在 Handler 方法执行的过程中，它会通过 handler Mapping 去查找我们相关的一些信息，我们可以看到通过 Handler Mapping 去找对应的Handler，因为 Handler Mapping 也会有多个的实现，那么它基于某一个去支持能找到对象的话，来进行后面的你 Vocal Handler 方法操作，因为我们基于这种 react 方式的编码。
其实 debug 其实不是很方便的，我们只是更多的关注到我们，比如说我们程序运行到这里面，它进行一个选择的逻辑是怎样的，这样也会更方便我们去查找，这样我们通过 dispatter Handler，会通过 Handler Mapping 里面找到我们这里面 road predict Handler Mapping，那么它在执行的过程我们看其实这里面它只是跟我们返回出了一个对应的一个 Handler 对象。


这个 handler 对象其实也就是我们刚才提到的一直在说的是filtering，在我们你的 Web handler，那我们其实注意我们再去查找这个 filter Web handler 的时候，这里面是一个是在我们的 get way 对应的包下面，还有其实还有一个是在对应的 spring Web 包下面也有一个这样一个 filter Web handler，一定要注意一下，我们要去找我们网关这个 handler 里面对象，其实在这里面我们它一个处理的对象也就是handler，那么真正我们处理的逻辑是 filtering vivo hunter 它里面处理的逻辑其实它在处理的过程中，其实我们可以看到它获取到我们指定当前的一个 router 的 get filter。也就是说我们当前我们的路由获取到我们的 filter 信息，那么同时获取到我们的 global filter 来进行一个一些组装，得到我们的 filter Gateway，一个 filter chain 的一个执行的过程。


那么其实构建完这个 filter Gateway， filter chain，它会进行一个 filter 的一个操作，我们可以看到它其实这是一个链的一个构栈的过程，它比如说它在执行的过程中，它会得到我们记一下这个当前 field 的 index 的，如果你看它的小于 filter size 的话，它每次执行它会去通过 filters 找到这个 Gateway filter，那么进行下一个站的一个迭代。


那么下一个真正迭代我们可以看到它构建这个 debutor git request chain 的时候，首先把当前对象作为我们那一个参数传入进去，同时把我们这个 index 我们的 string 值加一，也就是说我们的 filter 链的向后移步进行，再进行一个 filter 的一个处理，这样的话也就是把我们整个 filter 的过程进行一个一个串联起来，其实我们在这个处理的过程中，其实也就整个可以理解为我们的 filter 处理的一个核心的一个逻辑。


但真正的我们 filter 在做了什么事情，应该是我们具体的 filter 里面去做，那么现在我们可以去做一个请求执行，我们看一下它执行的过程，我们在这里面也是关键的地方，我们加入了断点，那么对于这些有断点的地方，我们可以重点关注一下当前在执行的这个过程，我们程序的一些想了一些情况。


好，那么我们在这里面去，我们看我们这样执行，我们是基于8020，我们进行provided，通过 ECOAP name 这样的话我们可以切换到我们映射的对应的一个路径，那么就从这里面看，我们是请求到 provided 这样一个路径下面会映射到这样一个 URL 下面。那么我们现在去请求我们通过我们的 debug 断点来去关注，我们看这里面。首先当我们请求的过程中，这里面是 react ITB handler Adapter，这就是我们最外层的一个接受请求，得到了这样一个请求，那么我们现在可以直接跳过，因为这里面更深的城市我们不用过度的关心，那么在这里面我们可以看到它已经切换到 dispatter handler 了。


那么在 discussion handler 这一层，我们可以从这里面看，其实已经在这里面去我们要注的事是 get handler，那么在 handler 的形容 get handler 就得到我们当前处理的Handler，那么该的 Handler 的过程其实通过我们的 handler Mapping 获取到的，那么在这里面我们看一下 Handler Mapping 的对象有哪些，我们可以看到在 Handler Mapping 默认有 6 个 Handler Mapping，那其实我们关注的我们其实这里面是比如说是 Web Flex Endpoint Handler Mapping，也就是暴露到外边的端点是通过它来完成的，这是 counter and handler Mapping。


其实这些不是我们过多关心的，其实对于 Web Flex 它最重要的是 request Mapping handler Mapping，那么这里面因为我们是基于 Gateway 的逻辑去处理的，所以我们这里面更关心的是我们这个是 root predict handler Mapping，那么其实它在获取这些我们的路由信息的时候，它最终会通过映射到 root particular handler Mapping 这样一个对象进行执行。


那么在这里面我们看啊，首先它执行的逻辑，如果说 handle mapping 等于 null 的话，就直接去那个 404 NODE bot 也就找不到，没找到对应的对象，那么其实我们这里逻辑肯定是能获取到对应的信息的，那么这里面它就是通过 Handler Mapping 的一些遍历，最终进行一些逻辑的一些计算去找我们对应。


通过 exchange 作为我们的参数对象，去找我们相应的Handler，那么在这里面去找到 Handler 以后，进行一个 Inbook Handler 的处理，那我们可以在 invoke handler，在这里面也有对应的相应的断点，那我们可以看到它处理的结果。那么我们在断点下面自行跳过，现在去真正去获取一个 guide handler 的一个过程。

