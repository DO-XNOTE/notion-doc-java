---
title: 6-3 Sentinel核心源码解析-初始化（1833）
---

# 6-3 Sentinel核心源码解析-初始化（1833）

[image](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/c775f4be-f5b3-47de-ac6d-ab2238fa29c5/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VDX43N65%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T232116Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCNcVFUOVCQ6fmZo%2BuJnBtMBvwVouk44C1WPcDZwt8UKwIhAKhHvaDje68dzsCxpm2Th6WnD07eTLNUCGmn7o62O7vPKogECMb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgzwcjmQlYo%2FoyQYivUq3AOW1eMf%2BVDbAoWFO6FfFVEL0fQANZTbRcm3cLSUi3dI7%2FMeL8AvWqeKd%2FrXJJxi5taEPBBcg8N%2FMb2k%2FgdHpM3t3Moabxie%2FL%2FO1VhjR8LoScoWa1YOInYzJv9kn31AMlpa%2FltXG3K0YOJ3Cdkgt1jwrnPmsOdSYrS8FerVp2qj3K9pyiFX21WLZyPCOSgBZE%2FDb%2FI1vzM73mmZGQPzUKvhnjpcBSZk7eODEXosBNWAaJk%2BQC%2Bt25GedA%2Fmf6m3rmvaxmRuS24J4IITURssTQsD3HqRU4uH0wtASw8dNo1JVyxKRla0yeSKM4dJcwLU%2FR9eYM3%2ByLqcZK6Ivbw%2BcZ9JdOvvDtgDv8gidSkUhp8S%2Fo6mo5zPq5X8d4P0Obq%2Fg37YM8jSM5Ko8YUiVRkVzg5WwULT3k%2B4zFF55kRplGX4Cj6pUZbTHYlLABNZKRQZ8e0dZ%2FotgBAAMLJ65d06L2Jg87c90Lz4FRl6kwp%2F5M%2FA4FvtKmoNCltEnF8KoGBRlMX1sJpfZ4IiflNjyeNGurkU5I3vSD6q43Twn8DL1WHw223XuadZ298Lbs9KfrEujfcPj8Hzyerw8eb06%2F2P5hgv4AMfIAaegl5JQrWqvbdbRBbWoQVeBfPDj%2FmXBDClt%2F%2FSBjqkAeQTRNtyeK6EBnpP7JPekbX254BPtnWIhCze2MGqBo0I1s0AHB9gCw7DyWzPq1R5pbfRplHY%2B%2BWk%2BYiQ%2FgrUbQWdm76IeQDo9TBh4Z6z%2B%2Bk8I4DEobJzxNrHzuAyFekviU6wJ%2FUvbu5pPCcUr1rwgwmr1IT6ZJfBPwcHi%2FNe%2BjX3YYA2sSJwIpMXl%2BBsdyMbNFl0z4QllvTdMCXWFuPF1n%2F2tfbL&X-Amz-Signature=fdb5981cecc1fd731679ff7fe0fae9ae1cc7e8f8ffe5873a5b96f94b958de313&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

同学们大家好，这章节我们来介绍一下 setton 的核心源码解析， settle 的源码包含 settle 的核心内容以及 spring code，阿里巴巴里面 settle 相关的内容。这里面我们主要介绍的内容，首先是对于原生signal，它的一些启动流程，它需要注入哪些 SPI 之间的一些装载。第二个我们介绍一下 signal 它执行的流程，主要关注在存在执行过程中相关的slot，它一些执行的一些事情。


接下来我们最后去介绍一下 string Claude，阿里巴巴 says 相关的一些智通装配的内容。接下来我们来看一下原生 sentinel 启动流程，这里面我们可以看一下它启动的初始化过程，其实刚才已经有介绍，它最终还是通过 ENV 对应的 init executor 方法来进行初始化的过程。现在切到我们的代码空间，这里面我们写了一个我们演示的一个单元测试，可以在执行它在启动的过程中它进行一些加载的内容。这里面在我们演示我们启动过程之前，我们还是把 seasonal 源码结构再给大家简单过一下。在这里面我们看我们这是 check 下来的 settler 官方的这个 get header，这里面我们已经切到了对应的 1. 8. 0 这样的分支。


对于它这些模块，我们的 core 模块是我们最核心的，我们看一下核心模块里面它的包结构，下面的内容可以简单展开看一下，在这里面它都对应的是com，阿里巴巴 CSP 点 Sentinel 会有对应，像 notice and class 我们的configure。这里面其实我们比较关注的一些点，可能比如包括我们这边 init 有对应的我们的 init function，就是这里面我们定义了一个接口的接口，这里面我们是对于每一个初始化的 init function，我们还可以定义一个顺序，这个 init order 跟我们在 spring 里面装载 in 对应的个 order 对应的结构类似，也就是说我们把所有这些定义的 SBI 加载完，它可以根据 init order 进行排序，按这个顺序进行加载。


下面还要跟我们 SPI 相关的内容是有对应的 service loader util，我们看一下这里面 service loader utile，它会通过对应的 SPI 机制找到对应的 service loader，可以看到它也有一个对应的 SPI order，也就是跟我们这里面的 init order，其实我们可以理解为它是异曲同步，但是我觉得它这样去定义不同的 order 其实有点浪费。


其实我觉得他们对于不同的 SPI 的结构，可以使用相同的order，对于这相同的order，因为它的排序不一样，最终也不会产生对应的冲突。这里面还有对应的slotter， slotter 也就是我们认为在 signal core 里面相对来说比较重要的slot，它是通过这里面的是 slot chain builder 构建出来的，可以看到这里面有对应的 blocker 相关的一些slot。最重要的这里面是有flow，就是我们的流控对应的Slardar，和我们的 degree 相关的一些Slardar，这里面还有，我们可以看到这里面有 static 相关的 static SLOT，这是我们获取我们统一信息的一些SLOT。


对于 debug 的 Slardar builder chain，这个 chain builder 我们看它是实现了 Slora chain builder，其实它主要是构建出一个 process Slardar Chin，也就是说我们基于这个 Slora chain 构建我们在流控执行的一个顺序，这些我们也是都是可以支持我们自定义的。


下面我们可以看到这里面其实最外层的这个接口，也就是 SPS 这个接口，其实我们看一下它提供了哪些方法，它提供的方法都是entry，并且这个方法它对应的响应的返回值都是隐私。对应的 entry 对象，这里面也支持异步的 entry 相关的一些操作，这里面其实各种不同 entry 方法，其实我们可以看到最直接的是基于参数，还有 entry type，这里面是基于一个 string 对象，标明一下我们的资源名称，也就是我们可以通过方法名作为我们资源名称，也或者说是我们的一个具体的一个字符串。
作为我们的一个资源的名称，可以看到这里面还有是SPHO，这是一个对应的一个实现，我们可以看到同志们去看一下实现的内容，对应的 CT SPS 是它的一个直接实现，其实我们在程序里面可以看到很多Adapter，它都是基于 SPSO 或 SPSU 作为我们的实现，对于这两个它有什么区别？其实对于 SPSU 它其实实现的逻辑是比较合理的，其实这里面我们看对应的 h 方法，它会 throws blocking exception 或者是返回一个临时对象，如果说它没有发生主端限流的话，它就会返回一个移植对象，这里面记录了对应的我们当前这个资源访问的一些统一信息。


如果说我们这个资源因为它的流量达到了一定的阈值，那么它就会抛出对应的 block exception，不会返回对应的 interest 对象，这里面的 SPSO 这里面是实现的更简洁一些，我们可以看到它这里面并没有返回抑制对象，它这里面返回的是个布尔类型，同时这个方法它也不会再抛出异常，所以说这里面我们可以看到它其实也就是底层对于我们这个异常进行了一个封装。


如果说它抛异常的话，我们会把异常转换成false，这里面我们注意只有是 block exception 它会成为false，对于其他的一些结果我们都会返回 true 的形式去抛出来，所以说这也是我们看到 SPSO 和 SCIU 的它的一些区别。


其他的内容我们在这里面其实就不做过多的介绍了。这里面还有一些 UTO util 里面，这里面主要涉及到看到一个 time util，这个 time util 它是在取当前时间的时候，为了提高一下它整个执行的性能，对于时间它会把这个时间的区间理度定位到一个毫秒，如果说它就是说通过这个里面能取到一个毫秒的一个精度的一个时间，可以可以理解它这个性能应该要比直接取 system 的 control 的 time medicine 的会更好一些。


其他的我们看这里面我们就不过多介绍了，我们再看一下对应的其他的业务模块，像这里面我们看另一个重要的模块，就是我们的 settle dashboard，也就是我们的控制台，是一个完整的一个 spring 布的一个 Web 工程，可以看到它这里面有对应的 dashboard application 作为我们一个启动器去进行启动我们的程序。对应的它也有我们相关的一些 Web 资源，这里面我们看到它相关一些 Web 资源的一些信息，对于我们来说，其实这里面的细节内容我们不用过多的去参考，其实我们可以直接拿我们的控制台直接使用，我们还有基于像我们 Docker 镜像的控制台，直接启动式运行就可以。至于里面它提供了哪些操作，我们可以通过暴露的一些 Controller 知道我们的程序跟我们的客户端之间的交互的一些过程。比如这里面像我们对于一些degree，比如说我们流控的规则的控制，还有一些鉴权相关的一些内容。


控制咱就先介绍到这里，后面我们看这里面还涉及到像 class locking 和transport，这些其实跟我们相关度不是很高，比如说transport，它更多的是涉及到我们一些数据交互的过程，当然我们能理解这个过程也是没问题的，我们学习流控主要是学习它限流熔断，它对于算法和它的结构并不是过多的关心。比如说我们配置规则的过程，因为我们配置规则的话可能需要我们进行一些数据的传输，这里面我们可以为了加快我们学习的理解，像 Adapter 和demo，建议大家去花些时间去学习一下。比如像 Adapter 这里面会列出了对应的，像 Sentinel apart，其 double Adapter，这里面就是我们 certain 为了跟 double 进行集成提供的这些adapter。


那么我们这里面可以点开看一下它实现的过程，其实它实现的主要逻辑也就是我们基于 setting 的 filter 机制，也是 settle 它的 SPI 机制去实现了一个对应的filter，在执行这个 filter 的过程中，我们可以看到其实在执行的过程中它最终还是调用我们最底层的这个API，这里面我们可以理解为你看我们可以看到是 SPS entry，最终我们执行完成以后对于这个 entry 对象来进行这样一个适当的关闭，我们可以在这里面进行 entry 进行退出。其实我们这是 provider 提供的filter，这里面有对应 consumer 提供的filter，其实它关键的逻辑都是一样的，都是我们基于 SPSU entry，最终我们再进行一个结果的一个关闭。


其实这里面我们还要关注一下对应的我们的请求，是一个异步请求还是一个同步的请求，这是我们看到的 double Adapter，同时这里面有基于阿帕奇的 it client 以及我们这里面的 OK HCP。其实我们可能更关注的，比如像我们 string Web Mac 或者我们的 Web Server Lite，作为这样的服务，我们提供的 depth 它实现的过程。其实在这里面实现的过程，我们可以看到对于 Web Mac，它只是实现了一个 second 的 Web intercept，因为我们知道对于 spring 我们进行拦截，使用它对应的 intercept 可以达到相同的效果。我们可以看到这里面它其实真正实现的逻辑也是这里面去。


首先是获取 result name，通过 resource name 的话，它会涉及到一个 URL cleaner，因为如果说我们使用类似于 restful 接口的话，如果我们单纯的启用 URL 是不可以的，我们需要把这些 URL 进行归类，避免其我们类似于 rush 的URL，它会让我们的 URL 的真正的情况进行一个膨胀。


接着看，比如这里面我们再看一下 Web serverlite，这个就比较容易理解了，它其实就是一个最典型的一个 Server 的filter，那我们基于这个 spread filter，它进行对于 URL 的一些请求的一些处理，这样可以做到对于每一个 URL 定义一个资源。


当然我们可以看到这里面也有对应的 URL cleaner，也就是说我们可以对于一些 URL 进行一个汇总，通过汇总的 URL 在执行对应的s，p， h u 的entry，我们进入统计，最终我们如果说执行完成以后退出统计，把我们这个当前 entry 关闭掉这样一个过程。


其实我们看完几个 Adapter 以后，就已经大概了解这个 Adapter 它主做的工作是什么。我们了解完这些其实就知道，其实我们可以参考这些 director 去扩展我们自己接触到的新的，比如说涉及到我们需要进行流控控制的一些方法，比如说我们可以参考对应的这些Adapter，完成我们自己的一些定义的一些远程协议，或者说比如对于 MQ 消费或者说等等其他的一些情况。


那么另一个我需要跟大家去介绍的这里面extends，其实这个并不建议大家花太多的时间，因为这里面主要涉及的内容是像 notation 和一些 data 操的数据源，其实对于我们来去学习流控的原理的话，对于这些其实我们不用投入太多的精力，因为这些更多的是一个对于规则持久化的一个过程。为了方便大家学习，建议大家把 sessional Demo 这个模块里面的内容好好学习一下。其实这里面是涉及到了我们各种装配如何去使用 cycle 快速上手的一个工具，尤其是在这里面我们是 cycle Demo basic，也就是最基础的一个演练。我们可以看这里面涉及到我们的 flow 流控，我们的限流和我们的降级相关的一些Demo，我们可以把这些好好学习一下，去，对我们充分理解 settle 它的一些逻辑还是很有帮助的，我们现在回到我们的 demo 模块，这里面给大家去介绍一下我们在启动的过程中它执行了哪些逻辑。其实在这里面我们关注它启动的过程，我们可以跟一下它的源码，在这里面我们通过 simple work 来去进行它启动的，那么其实的启动的逻辑就是在这里面。


当我们在执行 entry 的时候，会涉及到 env SPS，也就是说我们看一下对应 ENV 这个方法，这个 SPS 它都属于静态的属性和静态的代码块，这里面会直接跟我们初始化完这个对象，它会去执行这些对应的代码块，这里面是一个 init extra do init，也就是说它这个执行抄论看一下 doing it 的方法，它做了哪些事情？在这里面我们切进来看到这个 doing 的，首先这里面会有一个我们可以理解是个锁，这个锁判断一下我们的程序是否初始化，或者说是否正在初始化的过程中。这里面因为它是一个初始化，是单线程，一个执行的过程，所以说我们需要用它去做一个判断，避免重复的初始化。


初始化的过程首先它会在通过 service loader utile，刚才我们也特意介绍了它去获取我们对应的 service loader，也就是找我们对应的服务，它找的内容就是我们的info，找一个这样接口实现的内容，我们可以看一下实现了这么多需要我们初始化的内容，这些初始化的内容如果说我们正常配置的话，在初始化的时候会需要把这些类都进行加载进来。
这里面找到我们的这些loader，也就是找到我们一个load，一个集合这里面如果这 load 集合，我们刚才也提到了对应这个 init for 它这个相同目录模块，下面它还有支持一个注解，这个注解式引起的 order 进行我们对于这些初始化的一些函数实现的话，一些排序。


那么我们可以看到在这里面找一个常规的在里面，比如说我们看一个对一个 command center unit form 定义的 init order 是 -1，我们在这里面接着继续，其实它得到这些 loader 以后进行一个排序，接着对于这个 loader 进行它的一个初始化的一个操作，这样初始化的过程中，其实整个这样的过程就好像是完成我们的初始化了。


真正实现初始化的逻辑，它是里面对应的一些 init function，我们可以看一下它里面默认有哪些实项，可以在这里面去把它的时间打开看一下。在我们当前的环境里面可以看到这里面相关的一些实现，具体它做的一些内容是什么呢？我们可以自己去了解一下，在这里面我们就不再一个一个的去详细的去说了，这会的话我们可以理解为对应的我们的初始化工作已经完成，我们还回到对应的 init 方法，这个行，孩子回到 SPI 侧的它使用的地方，我们可以看到我们点进来在这里面最终它执行的过程，点进去这里面我们可以看到它的SPS，它的一个实现，它的默认实现就是我们的 CTS p s。


其实执行的过程中我们最终会执行到对应这里面，在执行的过程这里面还会涉及到一些初始化的操作，我们可以看到这里面会有一个叫 look process chains，插到我们真正执行的一个链里面，处理的操作其实也是利用了 SPI 机制，最终找到我们执行链，这里面会有一层缓存。


首先我们从我们的 Chin map 里面去查找，如果说没有查找到的话，这里面会通过我们的一些 SPI 机制，可以看到这里面它的一些机制去进行一个查找的过程，我们看它是一个 new slot chain，也就是说通过 slot chain 给 provided 去创建，我们跟进来。


通过这里面我们能看到 SPI loader first intense Defield 就是已经查到对应的 Slora team builder 的一个操作，这里面它查找的内容还有一次 debug slower team builder，如果说找不着的话，它会使用这个对应一个build，我们可以看一下 Meta info service 下面的配的内容，我们可以看到它对于 slot chain builder 这里面设置的内容，也就是默认是 debug slot chain builder。所以说我们可以先打开我们的 debug 所有的tributor，看它实现的内容是什么，其实这个也就是我们在初始化的过程中去构建我们的 slot chain，也就是我们的插槽的一个链，这个插槽的链在处理的过程，首先它会创建一个 debug 的 process lot chain，同时我们通过 SPA loader 去加载这些已有的，就是说我们可以通过排序的这个 top chain，我们可以看到它对应的内容就是 process slot。其次我们只要看到对应的 SPI loader，我们就对应从 mind info service 里面找对应的这个一个接口也好，或类的名字就行，这里面对应的 process slotter 就是在这里面我们能看到它是 process sloter，里面定义了这些各种不同的slotter。


这个我们在 PPT 上面跟大家介绍到这些 lotter 的一个情况，其实我们可以看到对应每一个 lotter slotter，它都有对应的它的一个排序，我们可以看到跟几个不同的 sort 的一个 SPI order，它是 -1万，从里面再看一个，它的 slot 是 4 - 9000，这样我们看几个能总结一些归类，这是 -8000。


也就是说在 Sentino 默认定义的这个sloter，它它相当于是定了几个大的级别，每个级别之间有很大的一个跨度，这样的话它其实在这个跨度之间就允许我们在这些 slot 之间加入我们自己的slot，因为中间 1000 个数字的一个间隔足够我们去扩展我们自己的内容，这样其实我们能看到对应我们 SLOT build 的过程，也就是在这里面去构建。


其实我们从这里面构建完成以后，把 slot 装载进来，也就是默认的我们会创建这里面所有slot，构建出一个链，请求通过这个链来完成我们流控的执行过程，回到对应的 CTS PS，那么这个方法它获取到我们的 load process chain 以后，后面的执行我们可以看到它原来我们通过资源的 entry 变成我们的 chain 的entry，也就是说开始执行我们整个一个 slot 链的一个过程。


其实这个过程其实我们可以想象到它执行的过程，也就是说根据顺序把我们这个链进行一个执行，那么在这里面它执行过程就已经回归到，也就是说我们真正的我们程序执行的过程。执行到这里可以说我们在 settle 它原生的初始化的过程已经完成了，在这里我们可以看到我们在 Meta INFO service 里面，它会涉及到首先是引起的 fun 以及我们的 slogchain builder 以及 process slogder。虽然他们初始化的时机是不一样的，但这都是我们在第一次执行初始化的过程中需要我们处理的一些内容。原生 settle 的启动流程我们介绍到这里，接下来我们来看一下我们 session 的它执行的流程。

