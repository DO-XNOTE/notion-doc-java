---
title: 12-1 Tomcat面试题深度解析（1117）
---

# 12-1 Tomcat面试题深度解析（1117）

同学们大家好，这一章节我们来开始学习 Tom 凯的面试题的深度解析。大家在学习课程的过程中可能有一个主要的目标，就是我学习完课程是为了面试，但是同时我们面试的过程并不能依赖我们这里面的面试题的深度解析，为什么呢？其实大家更应该去把前面的这个整个工作的流程，一些源码分析的过程学习清楚，去有助于大家更好的去学习更多的东西。


这里面汤姆派的面试题深度解析，我列出了两个常考的题目，第一个也就是我们的 Web 请求，在汤姆开的过程中，请求的流程是这样的，这跟我们前面介绍的请求在汤姆开的处理的过程其实是一个道理。如果说大家把那个课程的内容学习清楚，回答这个问题就相对来说比较简单了。


第二个问题是他们开的如何去创建 THREAD 实例的，这个里面它更多的偏向于 g to e thread 规范。我们应该知道对于 Server let，它的一个生命周期是怎样的。创建 Server let 的周期，我们知道我们需要进行执行 Server let，一个init，一个初始化的操作。接收请求的过程中，它进行 dispatcher service 的操作， service 操作会进行do，get， do post， do put 等等这些操作。整个执行完成以后，当我们 targeted 关闭的时候，会执行 series 对应的 destroy 操作，这是 series 一个生命周期。


我们基于 Server 的生命周期去想汤姆派的如何去创建Server？ net 的这个实例，那也就有一些想法。那么好，接下来我们来先看一下 Web 请求在汤姆派的请求中，流程是怎样的。那么我们看介绍这个问题的话，我们来先看一下这样一个相对比较抽象的汤姆克的执行图。这里面我们来先看一下汤姆克的几个核心的主要主页，我们再回顾一下。


首先证明是Server，对于 Server 下面我们会进行一个 service 配置， service 下面我们会包括 Connector 和我们的引擎。 Connector 我们这里面会有涉及到我们的协议 handler 以及 Adapter 处理器，一个适配器。


对于PORTAL， handler 会涉及到 in the point 和我们的ACCUATOR，一个我们的线程执行器还会有我们的 acceptor 和我们的 soft process 相关的一些信息，这里面我们看回头我们看我们的一个问题，就是说 Web 请求在他们 case 中执行的流程，其实我们的请求过来以后，第一个接受感知到的是谁？是我们的acceptor，其实我们 accept 会感知到我们的请求，得到这个请求会提取对应的 socket 进行包装， SOCKET 它会包装成一个 socket process，这里面也就是说我们 connect 组件的acceptor，它会监听客户端套接字链接并获取到我们的 socket 对象，这样的话把这个 socket 对象进行包装，交给我们的线程池 accuator 进行一些处理，这样的话就开始响应我们这些任务给到 accuter 以后，它会进行 process 组件去读取我们的消息报文。也就是说 process 它会解析我们这个输入流，进行我们的解析请求头、请求体以及进行一个封装成一个对应的 request 对象，这个我们在手写我们的 Web 服务器的过程中也会体会到了。


我们首先监听我们的 socket 请求，得到以后进行注意一个处理器，这个处理器这里面我们会进行 request response，两个对象进行一个解析的包装，这个处理完成以后它会通过Adapter，也就是说 Adapter 是我们 connect 一些引擎的一个链接，一个适配这个链接会它请求会涉及到一个 map 的映射， Mapper 组件会根据请求的 UL 值和请求图的 host 值匹配会指向对应的哪一个 host 容器，哪个 contact 容器以及哪个 wrapper 的一个包装请求？其实在这里面转化的过程中，这个 Adapter 是相对比较关键的，它其实是把我们的 Connector 和我们的这些容器组件进行一个关联起来，他把生成的这个 request 对象和响应的 response 对象传递到我们的引擎容器里面，传到引擎容器里面。


后面的操作主要就是我们的 pipeline 处理了这个引擎容器的管道，开始处理它，这个管道处理包含若干个value，每个 value 它去负责一部分的处理逻辑，执行了 value 后需要执行基础的value。这里面主要是涉及到引擎，它对应的实现是比如说 stand 引擎value，它负责调用 host 复制的pipeline，这里面对应的也是host，它的 pipeline 后面 4 项 context 相关的信息， contact 容器的拐道开始处理流程也是类似的，最后会执行 wapper 容器的pipeline，这里面的 wapper 容器的 pipeline 其实它就是对应了我们 Server Lite 的实现，也就是执行到这里面的话就执行到我们通常我们在业务开发过程执行 series 的情况。


这里面跟大家简单去介绍了一下他们开始处理 Web 请求的一个过程，这个大家也可以回到前面的课程去更详细的去了解一下它这个处理的过程，以及涉及到哪些具体的一些主线。接下来我们来看一下汤姆开的如何创建 Server Lite 实例类，这里面刚才也介绍的。对于这个问题，通常我们要比较好的把 Server Lite 它的生命周期给面试官介绍到。介绍完生命周期以后，我们再去可以深入源码去看一下 Server light 这个容器基于什么方式去构造的。我们首先要知道一点，就是 serverless 代态是实例化构造的过程，是在容器启动的过程进行构造的，它在启动完成以后，它还会执行对应的 init 操作，执行之后也就是他们关闭的时候要执行 destroy 方法。
先来看一下这个 throughout 生命周期指定的那些操作。这里面我们知道，对于我们所有写的THREAD，包含 dispatch throughout，它其实都会直接或间接地继承这个 LTB Server Lite，那么我们看一下 at you surprise 它里面的情况。这里面我们看到对于surprise，这里面定义了一些 match 的类型，delete，head，get，option，post， put 还有 trace 等等一些信息。其实我们这里面使用最多的还是 get 和post，那么来看一下它里面的一些情况。


对于这个 Server light，我们可以看到它几个关键的信息，它有对应的 init 操作，这个 init 操作我们可以看到这是基于 generate serverless 里面实现的，对于 Anti Server 并没有做任何实现。另外我们来看一下对应的 destroy 操作，我们看底创业操作也是针对 series 来完成的，也就是说其实我们 series 生命周期的过程中，它有初始化，有销毁，都是基于 generate series 它执行的一个操作。


我们看一下 HTP service 做了哪些事情，这里面去看一下，这里面会有一个 service 方法，对于这个 service 方法，我们看到它其实已经获取到了对应的 request 和组织Buzz，这里面 service 操作它实现的逻辑是什么呢？其实这里面有一个对应service，我们看这里面把我们的 servertech request，它会转换成 http serverless request，那么response，也就 survey 的response，它会转化成 http survey 的 response 这样对象这里面进行一个这一个保护类型 service 进行操作，这里面操作我们可以看到它主要的操作是 r e q，也就是我们 request 获取的mess，通过 mess 的进行一个匹配到对应的方法进行对应的操作。我们可以看到如果它 message 是get，那么进行读 get 操作。在后面我们可以看到如果它是 head 操作，那么进行读 head 操作，这里面有读 post 操作等等。基于这种方式最终执行到我们对应的这个业务操作，那我们看对应 s t v c write 它的读 get 操作出了什么事情。


这里面它实现的内容也是比较简单的，通常我们在实现自己的业务逻辑的时候，需要把对应的 do get 方法进行一个复写去实现我们自己的业务逻辑，那么现在我们通过这里面我们知道了 surflight 做的事情是什么，以及它的一个简单的生命周期。接下来我们来看一下这个 survey 的实例究竟是在什么时间去创建的？创建车外来的容器，那么我们现在基于 Tom can 的去了解，那么我们就看一下 Tom can 的是如何创建车 surprise 容器的。我们在前面也介绍到对应的我们的 wapper 是跟 supply 的相关的，那么我们可以直接切换到我们对应的 standard wapper 这个value，这里面我们也可以我们可以看一下 value base，这里面对应的一个 standard wapper value，对于 standard wapper value 里面它有对应的一些执行操作，我们可以看到这里面有 invoke 操作，也就是启动的过程中我们看到这里面会有对应的获取 Server LED 相关的一些信息，我们可以看到这里面我们会通过 wapper 里面获取到我们 Server LED。可以看到这里面是一个locate，这里面可以理为是创建，那我们跟进的这个 wapper 看一下它的实验过程。


这个 wapper 也就是我们 stand wapper，它在 locate 其构造 surprise 的过程中，首先去看一下这个实例是否存在，如果说它不存在，我们可以看到它是双重机判断，如果说我们的实例它等于 null 的话，这里面会进行一个 load supply light，我们也可以从这里面跟进去看一下 load third let 出的操作是什么？ load third 操作我们可以看到它是 single third model，是不是单拎的一个模式？这里面我们看到它，这里面首先判断一下这个模式是什么意思。这个模式如果默认我们知道 Server light，它在启动的过程中它们只有一个实例，就是说它并不是线程安全的。所以说这个里面如果说我们设置的是它并不是每个线程构建一个实例，并且当前这个实例不为now，我们就把这些实例直接返回过去了。


如果是另一种情况，如果说我们判断是 single seed model，也就是说每个线程一个模型的话，这里面我们每次都会创建一个新的 instance Lite，那么接下来我们来看它的一个处理的过程，在这里面我们会依赖到一个 instance manager 进行我们的 Server 的一个构建， an instance manager，它会通过 new instance 的方式传入我们的 THREAD class 去构建我们的 THREAD 实例。这里面我们可以跟进去简单看一下他处理的方式，我们看一下它具体的一个实现。


这里面我们看到底 u 的 Instant manager，其实它的实现逻辑也相对来说比较简单的，其实也就是使用了 Java 的反射的方式，我们可以看到 class 去获取到我们默认的构造方法，再进行一个你有意思的方式把我们 THREAD 构建完成。


其实看到这里面我们大概已经清楚了我们这个 surlight 是在汤姆开的过程，我们可以看到汤姆开的过程是如何进行实例化的，那么这里面我们看到它就完成了我们实例过程，实例优化 serverless 创建完成以后，我们看到这里面会执行一个隐匿的 serverless 的操作，那么在隐匿的 Server 的操作过程中，他做的事情我们显然意见很容易去理解。


其实注的过程也就是执行我们 Server led 隐匿的操作，我们可以看到它是也是通过反射的发送去执行对于 Server 的执行，这个 mass 的 name 也就是隐匿的操作进行一个操作的一个执行，这样的话我们可以看到了对于 thrift 它初始化的方式以及初始化完成，也就是说这个实例初始化完成以后，再执行我们隐匿的 Server data，调用我们 Server 代的生命周期的 init 初始化炒作。说到这里面，对于他们 at 如何创建 server 的实例以及 series 它的生命周期的内容，也跟大家简单介绍了一下。汤姆 case 相关的内容就先跟大家介绍到这里了，同学们，我们下一章节再见。

