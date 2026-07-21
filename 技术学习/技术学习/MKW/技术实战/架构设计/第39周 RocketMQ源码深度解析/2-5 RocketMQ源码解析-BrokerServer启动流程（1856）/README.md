---
title: 2-5 RocketMQ源码解析-BrokerServer启动流程（1856）
---

# 2-5 RocketMQ源码解析-BrokerServer启动流程（1856）

同学们大家好，这两点我们开始学习 rock MQ 核心源码解析 broker Server 启动流程部分，我们会通过源代码分析 Brockserver 启动的过程，看一下启动过程做了哪些事情。那么在看源码之前，我们先看一下 book Server 启动的一些大概的一些包含的一些事情。


这里面看到 book Server 启动的过程中，首先我们会执行对应的 men 方法，那么我们首先会找到 book Server 它启动的入口类 book STARTUP，那么对于 main 方法来说，这里面我们可以看到它会支持一些参数，这里面我们列出来一样，杠 C 杠 X 杠M、杠n、杠 p 这里面有一部分参数是跟 name Server 是具有一个通用性的，比如说我们上 count c 那就是我们的配置信息。杠 s 我们支持我们的 help top，杠 m 打印一些 master 信息，这里面杠 n 是指定我们的 name Server，杠 p 是打印出我们的一些信息输出。


那么对于 name Server 我们有印象，这里面是一个 name Controller，那么对于 broker Server，这里面是 broker Controller，所以说我们可以看到它这个启动入口类，它的设计还是很相似的。对于 name Server Controller，它里面配的 config 比较简，比较少一些，下面只有 name configure 和一个 Netty Server configure。那么对于 broker configure，那么这里面我们看到 4 个configure，分别是 broker CONFIGURE，我们的 native Server CONFIGURE 以及 Netty client configure 以及 message stock configure，这也比较容易理解，我们从这方面看出来 broker 在实现的过程中要比我们的 name server 更复杂一些。


接下来我们来看一下我们 starting 的过程，那么 starling 过程我们这里面还看到是 master store remoting Server 和 Paas remote Server，以及对 whats service，那我们只是列出了 4 个，其实还有很多我们在这里面没有全列出来。那么相比我们的 name Server 启动的过程中里面 star 的内容我们还有印象，它只有 remoting Server 以及我们的 feel watcher service。


那么看这方面看的话，其实 broker Server 启动过程中所需要启动的这个 service 也要比 name Server 复杂了很多，那么我们简单的了解了我们 work Server 启动里面涉及到一些内容，那我们接下来通过源码去看一下它执行的过程。


这里面我们已经定位到我们的 broker 模块里面的 broker STARTUP，那么这里面我们可以看到它是具有 men 方法可以进行启动的。那但是如果说我们在不了解源码的情况下，我们如何定位到 book start up，这里面也是基于我们的命令行的操作来去引导我们去可以顺藤模块找一下，我们假装不知道它的入口类是 BROKER servers startup，这里面我们切换到我们的 release for，那么在 resume bug 里面，我们知道我们启动 BROKER 的时候我们用的是 MQ BROKER 命令，那我们看一下博客命令里面的内容，其实我们跟到最后也能找到对应的我们启动的这个类也就是 book Server，那么可以看到这里面的 book Server 基于 run broker 点 SS 这样能进行一个执行。


那么好，那么执行我们接下来回到我们的源码，那么在源码里面我们当然可以快速的去定位到我们的 book star APP，那么我们这个找到了我们的 broker star，那么接下来我们需要看一下我们的 main 方法启动的过程，那么在这里面 main 方法启动过程我们可以先分析，首先 main 是我们的入口，那么这里面首先我们会 create broker Controller，那么创建完 book counter 以后就开始进行start，那么这样去看的话我们启动非常简单。


创建完 book 4 country，那么 start 就完成了， start 执行的过程就是我们的 country start，但其实我们看一下 create broker 喷水的过程，这个过程还是很复杂的，我们把这边搜说一下，那么我们可以看到这里面首先也是把我们的 remoting version k，也就是我们当前的 MQ 版本来进行一个设置。


接下来看一下一些配置项，如果说我们 3L 环节里面没有指定这几个发送的size，我们的 send chat 和 resell buffer size 这两个值的话，我们就设置对应的一个默认值，接下来去构建我们的 command line options，这个想起一下我们的 name Server 启动的过程中，其实这些操作很类似，他们主要是为了处理我们在执行过程命令行的一些操作。接下来我们这里面会 build comment line， build line option，这也是我们去处理过的，那么最终在这里面会处理我们的 command line。


如果说 command line 它这个对象没有获取到，那么就直接退出了，我们可以空这里面看到，现在我们构建我们的 book config，里面是 native Server configure 和我们的 native client configure。这里面我们也比较容易理解为什么 broker 需要一个 Server 和 client 端。首先对于 Server 端，我们的 broker 它需要接受我们 provider 和我们的 consumer 一些数据的请求，比如说它这里面是有对应的一个 native Server，那么对于 native client 端也容易理解，因为我们在 broke 启动的过程中，它需要向 name Server 进行注册，也可以发送自己的信号，所以说它需要一个 native kinda configure。


那么这里面理解了，我们接着看一下它的一个配置。对于我们这里面 native Server configure，我们看这里面 said listen 的port，也就是我们的设置端口号默认是10911。接下来这里面我们配置一个 message stock config。


我们知道其实对于我们 broker 处理最重要的一点就是对我们的消息进行一个存储和转发，现在主要是依赖我们的 master star configure 的信息来完成，接下来我们来看一下它会判断一下 worker show 的它的角色，那这里面如果是 Slim 的话，我们会进行一些 access master in memory Max ratio 的一个设置，这里我们可以看到它是我们的默认值减10。


接下来我们看一下对于这个 command line，它会判断一下我们在启动命令中包含是否包含这些参数。比如说我们的 c 参数，我们要配置我们的 config file，也就是对应的 broker configure 这样指定的文件，它会对于这个文件进行一个读取。这个在 name Server 的过程中也跟大家有介绍，进行一个书写，我们对这些属性以及我们的 KV 值进行一个默。


后面是我们去判断一下 rock MQ home，如果说我们的 rock MQ home 没有去设置的话，这里面会进行一个直接退出，其次我们需要设置一下我们的 MQ home 空间，接下来我们来看一下，它会去校验一下我们的 name Server，我们会获取到我们 name Server 的配置进行对于每个 name Server 进行一个，这里面进行 SOCKET address 就是我们去拼一下，你就是看能不能拼得动，如果抛异常的话它就会提示。而且这个 name Server 的地址是有问题的，所以说我们需要去配置以中 Paas 进行配，也就是我们的是 IP 转括号，我们的分号 IP 转括号，这比较容易理解，如果说这里面出问题的话，它就会直接去退出。


我们继续看这里面，我们看到它在这里面会判断一下我们的 message stock configure 的一个 broker row，也就是我们这个 broker 它的角色是什么呢？这里面我们看到这是异步 master 或者是同步的master，那不管是同步还是异步，这里面只要是master，它都会把 book ID 设置为0，这 0 里面是对应的是 master ID，我们可以在这里面看一下 master ID 对应的是0，也就是说对于我们 broker 指定 0 号作为我们的master，那么这里面如果是 slave 的话，我们可以看到 slave 它会作为一个判断。


假如说我们指定的slave，那么它的 book ID 是如果说是小于等于0，它就会判断不合法，认为这样的 book ID 是不对的，因为我们知道我们的约定是 0 是master，那么当然我们的对于 book ID 它不能小于0，所以说它应该是大于 0 的值。这里面会提示 they will book ID mark b 大于0，这里面同时我们也会退出。


接下来我们来去看一下，这里面会对于这边是 enable delicate commit log，这里面去做一个色，那么它的 book ID 默认是 -1。我们继续看后面的一些处理，这里面我们去看一下它对于这些参数解析的处理。对于 client line has option p，也就是说我们如果说用到了杠P0，那么它这里面要注的事是把我们的一些 property 信息直接打印出来，那么对于 m 的话，它也是把一些那一些信息打印出来，我们这里面的 broker configure，我们的 native server config 这些我们的 message 信息打印出来，那么这里面我们可以看到我们可以基于这些答案去验证一下。


这里面我们是有对应的我们的命令控制台，我们可以执行一下我们的 MQ broker，那么我们先用杠 h 命令，这里面我们启动去执行一下 MQ broker 杠 h 的输出内容，我们可以看到它会提示我们这里面支持杠c、杠m、杠n、杠p，那么我们接下来我们去验证一下我们的杠 m 和杠p，这里面只是打开输入内容，那么像卡片的我们指定配置文件这块，我们启动的时候 PG 引用，那么我们当然默认我们可以指定好。


那么我们这里面指定一下杠m，它会输出哪些信息？我们可以看到它这里面输出很多配置项的一些信息的内容，这里面我们可以看到 book ID 是0，说明我们是master，这里面还有一些其他的一些信息，这里面是比如说 delete when，也就是说当我们什么时候去删除数据，那么这里面是凌晨 4 点的时候进行删除。


这里面还有一个叫我们的 feel reserver 的time，也就是我们的文件的一个过去时间，这里面过去时间是 72 小时，我们再去验证一个我们的 p 命令，那么如果说我们指定的是杠 p 的话，我们可以看到它也会打印出我们的一些配置信息，这里面这样一些信息的值，我们就去看这里面 master delay live，我们可以看到它是 1 秒、 5 秒、 10 秒、 30 秒等等这样一个值。其他的也可以是我们的当前的 broker row，我们是 IM master，我们的刷盘方式是异步的刷盘方式等等这些信息。好，我们清理一下控制台，那么回到我们的源码空间，那么我们可以看到我们的杠p，杠 m 的话可以执行对应的一些操作。


接下来我们向后进行执行，在这里面的话开始创建我们的 broker configure control，那么这时我们获取 control 的方式就直接创建，那么创建了new，创建的过程中我们传入了 broker configure，我们的 net Server config 等等这些 config 信息。


其次这里面我们创建的逻辑还是比较复杂的，我们可以跟进来看一下博客，看出来创建的过程，我们可以看到这个里面的属性特别多，其实我们如果说第一眼看起来的话，会感觉眼花缭乱，其实我们快速跳过我们到它的构造方法进行执行，我们看下这里面确实有很多属性，我们可以这里面是对应的blocking。


q，这是我们的一些 configure 和一些 manager 相关的一些信息，这里面还有一些process，那么我们看这里面有很多线程词，有一点 service 里面我们可以看到 send message 和我们的 pull message 或者 reply query 等等很多跟我们现在执行相关的一，些信息，我们可以看到在这里面我们在构造方法里面传入了这几个 computer 对象，那么我们得到这个 computer 对象以后，它就会创建对应的这些 message 和我们的 process 相关的这些信息。这里面我们先不会对这每一个操作的会一一介绍。最终在执行的过程中，所有创业类对象它都会在一个特定的情况下是会用到。比如说这里面我们的send，我们对应的 pull query，我们的一个队列，你们 push 的 pull query，也就是我们获取的一个线程池的一个队列。看到这样一个信息，那我们的 book configure 里面它有一些配置信息， configure 也有一些service，还有一些限制式队列。


我回来我们接着看它继续，那么得到 control 以后，它后面会进行一个初始化的操作，那么这个初始化操作我们看整个方法它即将执行完成，也就是说它进行结束，那么这里面会对我们的 control 进行初始化，那么我们先看一下底下函数的那些事儿，如果说我们的初始化失败的话，它会直接把 control 进行一个 set up，进行一个退出。


如果说初始化成功，它里面会有一个 set on hook，这里面也是一个当我们的程序结束的时候，一个 hook 回调，里面回调的主要操作的逻辑也是把我们的 counter 执行 set down 的方式进行一个优雅关机，下面我们看到只要任意地方有抛出异常的情况，它都会直接把我们的程序进行退出。当然我们可以看到它对于异常站的话也是直接打印到了控制态，其实通常我们在做工程类的程序的时候，其实打印异常站是我们不推荐的。


好，那么接下来我们来看一下我们的conquer，这里面执行的一个初始化的操作，其实这个初始化操作还是比较复杂的，我们可以看到刚才我们又回到了 broker Controller 这初始化的功能，我们可以看到它初始化它会有不同的数据进行一个load，那么这里面我们分别是装载我们的 topic 的一个配置信息，里面是装载我们的 consume offset，也就是说我们消费的一个目标点。这里面是 subscription group，也就是我们的一些注册的我们的消费主，这里面是 consumer filter，是我们在消费过程中配置的一些过滤器，那么这里面我们看它其实返回对象就是布尔类腔，整个这个过程我们可以理解为串行的进行一个语义的操作。


如果说我们的 result 执行是成功的，那么这里面会创建一个 detail 的 message store，那么也就是我们的消息存储的一个对象。接下来我们去看这里面是有一个 book States，这里面还会去装载一些插件相关的一些信息。当我们 master star 执行正常成功的话，我们会也会进行一个 load 装载的一个过程。


如果说，嗯，我们的这里面 result 还是一个正确的结果，那么下面我们看它会去构建我们的 remoting server，其实 removing Server 就会去监听我们 Web 的请求进行一个处理。这里面也是 native Server，这里面它基于的配置就是我们的 netting Server configure 相关的一些信息去看，在这里面会指定一下我们的 listen part，哈，这里面我们可以看到，同时我们能看到一个 faster remoting Server，其实我们的 remoting Server 和 faster remote Server 其实它在做的过程中我们可以理解为都是很相似的，那么为什么它需要两个我们的 remoting Server 呢？里面简单去说一下，其实我们的 remoting Server 和 Paas remote Server，它都是接收请求去处理信息的，这里面有一点就是我们的 remoting Server 既可以去接收 producer 生产消息，也可以被我们的 consumer 进行 push 和拉取消息。但我们的 fast remoting Server 它只能被用于我们的生产消息，它不能应用于我们的消息消费。


接下来我们可以看到这里面我会创建一些线程池，我们的 send message 线程池创建的方式我们可以从里面看到，其实这些所有的操作我们都可以支持基于 computer 配置进来的。所以接下来我们去看到这是拉取消息的线程池，那我们是一个对于一个消息应答的一个线程池。接下来我们看我们这里面是创建消息查询的MQI。前两池，这里面是一个可以看到是 broker 管理的一个前两池里面对于客人端我们管理的一个前程池，接下来我们来看下面，这是我们的一个心跳的线程池，里面对于我们是对于四五消息的 end transaction accurate。接下来这是一个创建 consumer 管理的 consumer manager，接下来这是 register process，就是注册各类处理的一些 process 信息。


接下来这里面是一个定时任务，我们通过 schedule 初始化 broker 的状态统计的这些定时任务，这里面还有一个schedule，这里面它要做的事情是什么呢？我们可以看到这里面是处理的对于我们初始化 consume offset，也就是我们的偏移量的一个持久的一个 get zone，对于我们的偏移量的定时的你进行持久化到我们的硬盘上面，这里面是也是一些定时任务，我们可以看到这个定时任务是什么，对于我们的 consumer filter manager，对于我们这个初始化 consumer filter 的一个定时任务的一个管理。其实我们看下看下面这是一些对于一些定时任务的一些处理，具体它是什么我们就不再去这里面进行介绍。


其实我们可以再回头看一下我们那个 reject process，看这里面做了什么事情，去注册了一些处理器，其实这里面我们可以看到它，主要从这里面我们看到它对于像 remoting Server 和 fast remoting Server 进行了一些注册信息，这样去看的话，它注册的信息很像是一字的，那么它是通过什么去区分出 remove Server 和 faster remove 的 Server 的区别？我们可以看到在这里面对于 remuting Server，它注册了我们的 pull message process，那么但我们对应的我们的 fast remoting 它并没有去注册这个，所以说我们的 fast remoting Server 它并不能接受我们的消费者的信息的消费，这里面我们可以看到它也是在注册一些相关的一些process，那么我们对于回到我们的 reject process，那么在这里面我们在进行看到之后，这里面还会做了一些什么事情？我们拉到这个方法后面，这里面我们看到是 insole 里面有对于 45 的初始化，里面 ACL 的初始化，还有一些 RPC 的hook，这里面我们知道它是 45 相关的，这里面是 HR 相关，也就是我们的权限控制相关的这样一些信息。


那么看到这里面的话，我们知道我们对应的这个 broker Controller，它就构造完成进行一个初始化的工作，也是在这里面进行执行完整。我们回到这个方法，按大家初始化完成以后，后面我们可以看到这里面整个就执行完成了。好，那么对应我们这个方法，我们的 control 也就构造完成，进行一个初始化。


那么我们接下来回到我们的方法，这里面开始进行 star 操作，那么对于 star 操作，它也是依赖了我们的 Controller 直接 star 的请求。这个 star 操作我们可以点进来给大家去简单介绍一下，我们可以看到它里面我们可以看到对应的各种我们的服务， Meta star 服务进行启动，我们的 remoting service 启动，二次 remote Server 启动等等，我们可以看到这里面都是我们介入的这些服务，在这里面进行一个启动的操作。


在启动过程中其实这里面他也做了很多服务，当然里面有很多对应的一些性能池，这里面我们可以看到它会通过一个周期性的进行注册，也就是把自己的 broker 注册到我们的对应的 name Server 上面。好，我们再看其他的这样对应的我们的 broker store 的 manager 和 broker fast failure 的一些逻辑的一些启动。那么执行完这些的话，对于我们 broker 端的一些操作的话，它就首先创建我们的 BROKER Controller，进行我们 broker Controller 一些初始化，再进行我们的 control 进行一个 start 操作，最终在这里面的话，我们的 BROKER 启动执行也就完成了。那么我们 book Server 启动的内容我们就先介绍到这里，同学们，我们下一章节再见。

