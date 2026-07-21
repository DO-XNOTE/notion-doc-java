---
title: 3-2 RocketMQ应用技巧解析-通信机制（2004）
---

# 3-2 RocketMQ应用技巧解析-通信机制（2004）

同学们大家好，这章节我们开始学习 rock MQ 的应用技巧，解析通信机制的部分。那么对于 rock MQ 的通信机制，我们这里面也是分三部分来给大家介绍。首先第一部分，我们来介绍一下 rock MQ 在整个集群过程中，我们数据流转的形式是怎样的。第二部分是我们介绍一下对于 rock MQ 核心源码里面的 remoting 模块，其实 remoting 模块我们可以理解为它是个远程通讯的一个模块，这里面定义了远程通讯的一些规范和实现。


第三部分，我们来介绍一下， net remoting Server 它是如何基于 react 实现了多线程的设计。那么好，我们先看一下 rock MQ 数据的流转，那么这里面呢？这个图对我们来说是比较熟悉了，我们可以看到对于 rock MQ 这样一个博客集群，以及它的 name Server 集群，以及这里面的 producer 和我们的consumer，它都是以集群的方式去存在的。对于一个 rock MQ，它的实现过程，它的数据会实现哪些流转的方式我们知道。


首先当我们启动的过程，我们会启动 name 12，那么启动 name 12 的时候，它可以理解为没有过多的数据交互，因为每一个 name Server 它都是一个独立的个体，那么 name Server 启动完成以后，我们会启动我们的broker，那么在启动博客的过程中，它会向这几个 name Server 节点都会去注册，那么这个注册的过程就涉及到了数据交互，这里面数据交互都是采用 net 作为底层实现来完成的。


那么这是一种方式，我们的 broker 要跟我们的内部 server 进行一个数据交互，这里面包括它的注册以及它的一个对应的 topic 的一些注册信息。那么这里面我们可以看到对应的博客 master 和博客slave，那么对于我们主重之间它也会有数据交互，那么这里面我们在做高可用的过程中涉及到它的 HA 模块，那么我们了解到 broker 之间也是有数据交互的，这里面主重的数据交互。


对于博客2，我们的 master 2 和 slave 2 也是同样的道理，他们也会涉及到数据的交互，那么这是我们集群本身它 name Server 和 broker 之间的一个数据的交互的过程，那么现在我们来看一下客户端，这里面我们看到对于我们的 producer product，首先它会跟我们的 name Server 进行交互， producer 它会通过我们的 name Server 集群里面随机选取一个节点，把我们相关的路由信息以及住址的博客信息拉取回来。在这里面根据我们对应的我们的 topic 信息发送去选择对应的broker。那么这里面我们看到首先我们的 position 是需要跟内部设备进行交互，这里面也属于远程交互。


第二就是我们其实 MQ 流转里面最重要的一条，也就是说我们 producer 选中对应的broker，也就是说把我们的信息，我们的消息流水推送到博客信息，那么这是其实我们最主要的数据流转，也就是数据量最大的一种场景。那么我们的数据流转到博客以后，这里面的 consumer 都会监听博客信息的变化，那么他感知到信息的变化以后，我们进行拉取或推送的方式，把博客里面的活跃信息拉取到 consumer 进行一个销毁。那么这里面消费的过程也是需要一个跟 name Server 的交互的过程，它需要先从 name Server 里面拉取到这些对应的路由和 topic 信息，以及 broker 里面注册的一些信息，那么基于这些信息去找到我们对应的 consumer 需要去哪个 broker 去消费信息的过程，那么这样的话我们就看到其实我们整个 rock MQ 集群的过程中，涉及到数据交互的流程非常多，我们可以看到这里面密密麻麻的线条都是它进行交互的一个过程。


所以说我们可以看到对于 rock MQ 里面数据的远程传输是非常重要的，里面我们了解了 rock MQ 集群它数据流转的一些线条和方向，那么接下来我们来看一下 remoting 模块，这里面我们简单介列出来。对于通信机制，这里面最重要的就是 rock 的 remoting 模块，对于 rock 的 remoting 模块里面，它里面有几个接口和实现对应的接口，这里面是 remoting service，可以理解为我们操作的一个根接口，那么它下面有对应的 remoting client 和 remoting Server，这两个也是分别对应的分别的接口规范，那么对于这两个接口规范他们都有基于。 net 的实现，也就是对应的。


net remoting client 和。 net remoting Server 这里面对于 net remoting Server 它的实现的是非常值得我们去深入研究的，那么这里面也就是说我们涉及到 client 端和 Server 端进行数据传输的过程中，它的数据载体是什么？它的数据载体主要也就是个 remoting command，这个 remoting command 我们可以理解，我们对应 HTP 协议里面我们会有 request 和response，那么我们基于 net 实现的这个协议，它的输入和输出都是对应的 remoting count，那么 remoting command 这里面我们看它有对应的 code language， ver 森、 remark 和 customer head 以及body。这里面其实传输最重要的内容是body，那么其他的这些信息都是对于我们这个请求的一些标志性信息。其实像这里面指定的 code 码 language 以及版本信息，还有一个 customer head，它会根据不同的数据传输类型定义不同的head。


那么这样我们大概了解了这个 remoting 它里面包含的一些内容。一个初略的介绍，那么我们接下来切到源码里面去，让大家更深入的了解 remoting 模块。这里面我们看到 remote 模块里面的代码量其实并不大，我们可以看到这里面定义了一些接口规范，这里面注解 common 以及定义了一些 exception 对于。 net 下面包下面的一些实现的代码量，我们可以看到类的模块是比较多一些其他的，这里面定的 PORTAL 以及我们的协议。那么这样看的话， remoting 模块它的代码量不大，但是我们可以看一下它的 palm 文件它依赖了哪一些？第三方依赖这里面我们看到 fast json，因为我们在传输的过程中是用到了 json 去做系列化，那么 fast Jason 和我们 on 都属于阿里，阿里它肯定会更多的以推荐自家的 JSON 序列化的方式。 fast JSON，那么它依赖的内容这里面有。 net all 也就是说我们涉及到远程传输是依赖到。
net 的一些内容，那么这里面的 rock do， rock MQ 的 login 我们就不用过多去介绍了，其实它也是为了减少我们底层，这是替换的麻烦，所以说这里面定义了一个 rock MQ locking 的一个门面，具体它的实现还是基于 log for 街或 log back 当时去实现的。


那么这里面我们看到了 remoting 它的一个模块情况，那么我们也可以去看一下，对于这个remoting，它是属于一个基础模块，那么基础模块都在哪些模块里面有用到了remoting？ rock 的 MQ rock MQ MO remoting 我们可以看一下，这里面我们可以看到是ACL，这里面是博客有用到，这里面 common 也有用到，我们可以看到这里面对应的 store 也会有用到Server， YouTube 都会用到我们对应的这个 remoting 包，那么这里面我们可以简单看一下这里面的介绍。


这里面对于文档里面有介绍是 rock MQ remoting，这个模块是 rock MQ 消息中负责网络通信的模块，它几乎被所有需要的网络模块通信都需要它。这里面涉及到rock，没有Claude， rock broker， rock my name Server 等等等。所以我们可以看到这里面的 common 模块。我们知道 common 模块属于基础模块，通常会被第其他的模块的依赖，我们可以看到即便是 common 模块，它也依赖了我们的 rock MQ 的 remoting 足以说明我们的 remoting 模块它的基础性甚至要比 common 还要强一些。
那么这里面对于 remoting 它这些模块的类，我们可以简单来去看一下，通常我们学习了解一个模块，我们更多的先看一下它的接口，它定义了哪些接口，我们可以看到这里面有channel， event listener，我们这里面有 command customer head，这里面 invoke callback，这里面 remote client、 remote Server 和我们的 remoting service。那么刚才我们有介绍 remoting service，我们可以从这里面看一下它的继承数结构。


那么对于一个 remoding service，我们从这里面看到它下面有两个接口的子实线，里面有两个接口，一个是 remoting client，一个是 remoting Server。对于 remoting client，它这里面有。


net remoting client 作为它的实现，对于 remoting Server，它有对应的。 net remoting Server 作为它的实现，其实我们从这里面去分析一下整个我们系统的调用的入口，也就是我们的对应的。 net remoting client 和。 net remoting Server 就是我们整个的核心，那么我们来再看一下对于我们的 remoting client，我们先以 Claude client 作为我们的入手点，那么我们可以看一下 kind 里面有哪些方法，我们这里面看一个invoke，我们可以看到这里面有 invoke 是 a sync 和我们的 think 处理以及 one way，那么这里面其实更容易理解的是我们那个同步调用，那么其次是异步调用。


那么最后对于弯位，那么关卫我们可以看一下，分别看一下对于像我们的同步调用，这里面是对应的是我们的返回值，是 remoting plan 的，我们对应的是 Emock think 的话，它是外语的类型，那么汪卫也是话语的类型。我们重点看一下这里面的 invoke think 它的一个实现，那么在这里面实现我们可以看到它关键的参数，这里面的 request 对象是一个 remoting command，那么它得到的响应内容这里面也是 remoting command，正如我们在这里面介绍的我们的 remoting command，通常这个 command 命令模式的方法使用，它既是一个输入对象，也就是一个 request 请求的输入，它同时也是一个响应我们对应的输出的一个参数的包装。那么这里面我们刚才介绍了最重要的，我们的数据传输是基于包体的方式，那么在这里面我们可以通过对应 net remoting class 的这个请求方法去了解一下我们数据传输的一些方式。
OK，那么这里面我们简单了解了一下对于我们这几个关键的接口以及它的传输的方式，那么我们可以从这里面切到 remoting command，看一下它里面的内容。我们在这里面有介绍，它有 code language，verse， remark 和body。那么在这里面是怎么体现的？我们可以看到这个类比我们刚才预想的要复杂一些。对于 remote Claude 里面，它有很多Pixel，final，string，以一些静态常量，这里面还有一些私有化的一些 final 类型的属性。最终我们更关注的是什么？我们关注的是这里面的一些常规的一些类的属性，这里面像 code language 以及 ver 森，这里面还有flag， remock 以及一些扩展的field，这是 customer cosmohead。同时这里面还有一个 slab type，也就是说我们序流化的类型是什么？这里面默认是Jason，同时这个 body 一个二进制的body，是我们存储信息的一个主要的一个内容。


OK，那么这里面我们大概了解了 remoting command 里面的数据结构，那么我们接下来看一下，这里面我们看一下这个类图，这个类图也非常容易理解，跟我们在这里面去看到的类的结构也是一个相同的一个对应关系，这里面 remoting service 对应我们的对应 revenue service，它下面的两个对应的接口，一个是 remoting Server 和一个 remoting client，以及这两个接口它的实现OK。


那么这两个接口分别对应的是 net remote Server 的实现以及 net remoting client 的实现，那么这两个类的实现，它们同时又具有一个公共的父类，那么这个父类是 Netty remoting object，也就是说基于 Netty 实现 remoting 的一个抽象类，那么这样的话其实就减少了这两个类里面重复的一些代码，我们提取出来，提取出一个负类来。这里面我们也可以比较容易的看到这些类之间的关系。


对于 remoting Server 它定义的比较抽象程度比较高，它这里面只有对应的启动start，因为我们的停止 set down 以及我们注册一些 RPC hook，也就注册一些回调的一些业务逻辑。那么对于 remoting Server，我们可以看到这里面注释了一些process。大家还注意到我们其实在接收数据或者是消费数据的时候，都会涉及到process，里面有对应的 send message process 以及我们 pool message process 都是在这里面，我们通过注入的方式注射进去的。同时这里面我们还可以获取 get process pair，就是我们要获取到一个一对，这个对的内容分别是， net request process 和对应的 ACUTE service，也就是说我们要获取一个指定的 request process，还有它对应的一个处理它的一个线程池，基于这个线程池进行对它进行消费处理。


OK，下面这三个对应的是分别是我们处理消息的几个不同，一个是 think 是同步的异步的，这里面 one v 的方式跟我们对应的 remoting kind 的操作也是一个对应的关系。对于这个Claude，它有一个跟我们的 Server address 进行操作的操作，一个是更新我们的 name Server 的例子，这里面去获取我们的内部策略的地址，同时这里面也有对于 invoke think 我们的同步异步官微的处理方式，OK，那么这样的话我们可以看到了它这个接口里面分别具有的一些公共的一些方法，那么对应这是他们实现的内容。


其实这里面对于 net remote Server，它的实现逻辑相对来说更受到关注一些，因为在处理的过程中，它用到了我们的 react 模式的多线程设计，所以在源码学习过程中，这个 net remoting Server 也更多的容易受到关注。


那么接下来我们来看一下它的 REC 的多线程设计，那么这里面这是一个相对来说比较抽象的一个图，这里面密密麻麻写的内容非常多，我们怎么去看？我们首先看这里面，这是 net remoting Server，那么基于 net remoting Server，它在这个类里面有一个属性，我们的属性是 process table，也就是说我们所有处理的这些process，它都基于一个 table 方式。这里面其实就对应的一个map，基于一个 map 方式，把我们的 request code 对应一个 int 类型的 request code 以及一个 process pair，这个 process pair 刚才我们有印象， process pair 是对应的 request process 以及他们对应的线程值的一个组合，我们可以在这里面对应着我们的源码来跟大家去介绍，这里面我们可以切到我们的。


net remoding Server 在这里面处理的过程，我们去看一下我们的pool，这里面的 pool table 我们可以看到这里面对应的属性是 process table，这里面我们可以看到 protect table，它是一个保护类件。首先这个 protect table 它是位于我们可以看到是 netting remoting protract，也就是我们对于 remoting client 和 remoting Server 都共同继承的这个abstract，抽象的。 net remoting，所以说我们可以看到对于这个 process table，它是在 client 端和 Server 端都是需要的。那么在这里我们可以看一下这个类的结构。首先它是一个哈希 map 的类型，也就是说我们一个 map 对应的 KV 建值，对它的 k 就是对于一个 int 类型的一个 request code，那么它的 value 类型我们可以看到它是pair，这是一个对一个数据，对这里面它的k，它这里面不能称为 k 了。他们第一个项数据和第二项数据分别是 net request process 以及是我们的 request process 一个实现。另外是针对这 process 的 x 设的设备词，也就是对应的一个我们的线程池，我们可以看一下 per 它的对应的参数，这里面或我们可以或者是 OBJECT 一， OBJECT 2，也就是我一个数据一和数据 2 的类型，我们可以看到对于命名是 object 的话，这个命名其实还是挺挺不讲究的。


OK，那么我们接下来看，这是我们看到了 process table，那么接下来他要处理的话，我们这里面会有对应的 process request，这里面是 process request 和 process response，那么也就是说处理我们的请求数据和我们的 response 数据，当然这里面还会有我们接收数据的请求。


那么在我们这里面 remoting track 里面大家还有印象，我们有了解，这里面是啊request，这里面receive，这里面我们可以看到是 process message receive，也就是说我们要处理我们接收到的这些消息，这里面处理的过程中，这里面会涉及到会判断一下我们 command 类型去处理是 request command 还是就 sponse command。应该还有一些印象，所以说这里面会分别去处理。那么在这里面我们可以看到这里面会涉及到了几个线程池，这里面分别对应的是我们的。 net react master，也就是我们主的 REC master 以及这里面是。 net react pool native work 和我们的 remoting work，这里面我们可以这样去理解，对于我们的主线程，它是我们对应的，是因为 look group boss，他负责监听我们 TCP 的网络请求，建立好链接，创建我们对应的 SOCKET channel 并注册到 select 两面。其实对于 rock MQ，它的源码会根据我们当前的 OS 类型选择是 NL 还是一个 EP 的方式，然后其实是在我们的。 net remote Server 构造的时候就已经得出结论了，我们可以看一下源码的部分，这是我们可以看到它是对应的我们。


net remoting Server 的构造方法，在它构造方法执行的过程中，我们这里面有一个判断条件，这里面判断的是 user 一铺，也就是说如果是为 true 的话，这里面我们直接创建一个 EPO event loop group，那么如果说它是 false 的话，这里面是会创建一个 NIO 的 event loop group。


那么这里面我们来看一下这个 user 衣铺，它的条件判断是什么，这里面很容易去看出来。首先我们看一下 remoting UTO，当前我们是一个 Linux 环境，并且它是我们的 Server config，也就是我们的配置过程中是 user epoll 的作为 native selector，并且当前的 epoll 它是可用的，基于这几个条件来去判断，其实对于我们来，通常我们只关注的它是操作系统OK，那么这里面我们还切到这里面我们可以看到对应创建的是一个 e 铺 event Loop group。那么这样嘛，它会创建性能池的个数，默认是一个OK，嗯，接下来我们了解完这些情况以后，我们来看一下它真正处理的一个 channel pipeline，这里面我们可以看到它一个是对应是hat，一个是tail，我们可以看到这是头，这是尾。


类似于一个链表，双向链表的一个处理的过程。首先我们通过head，这里面会涉及到 Nike Encode，这里面。接下来 Nike d code 也比较容易理解，所以涉及到对于。通过。 net 它的一个编码和解码操作，这里面我们可以看有一个 idol state handler，对于一个空闲情况的一个处理。接下来这里面会涉及到。 net connect manager handler 以及最终是我们的。 net Server handler 这样一个处理的过程。其实在处理的过程最终还是使用了对应我们 request process 进行我们处理的一个逻辑。看我们 record 多线程设计，我们基于这个相对比较复杂的一个运行图，以及我们对应的是。 net remoting Server 的源码跟大家做了一个相对简要的一个介绍，那么在这里面我们关于 rock FQ 通讯机制的内容就先介绍到这里，同学们，我们下一章节再见。

