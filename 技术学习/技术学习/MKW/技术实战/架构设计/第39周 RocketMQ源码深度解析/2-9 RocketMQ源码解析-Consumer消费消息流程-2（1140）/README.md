---
title: 2-9 RocketMQ源码解析-Consumer消费消息流程-2（1140）
---

# 2-9 RocketMQ源码解析-Consumer消费消息流程-2（1140）

下面对是一些信息的一些更新，我们跳过这里面，我们可以理解为对于这一部分的内容，它已经启动完成。我们回到PP，我们可以再回顾一下启动的过程，最终其实我们看到它是在 pull master service 的过程的启动完成。


我们接下来看一下我们拉取消息的过程，其实拉取消息的入口就是 pull message service，那么我们可以看到它拉取消息入口是 pull message service，为什么 pull message service 是我们拉取消息的入口？我们这里面可以先看一下这个类，其实在这里面去拉取 pull master service，一个启动的过程中，我们可以看到它基于一个running，我们可以看到它是一个 service share 的，也就是它是基于一个 run able，一个可以进行异步处理一个线程的操作，它在处理的过程。这里面的 run 方法，我们可以看到 run 方法它是一个 will true 的一个循环，也就是说它如果说没有终止的话，它都会直接执行。这里面我们可以看到它会有一个队列，这里面是 pull request Queen tick 的主吞的过程，如果说它只要能获取到一个 pull request，获取到 pull request 以后，它就会把这个 request 放到 pull message 的参数里面，执行我们的拉取信息的一个过程。看到这一点我们知道对于我们这里面的 pull Meta service，其实是有一个，我们可以理解为是一个死循环，它一直在等待我们的消息队列，我们只要获取到消息队列，我们就会进我们的消息情况进行一个拉取，所以说我们基于这个 Pro mess 作为我们的一个入口进行一个分析。


那么好我们看一下，在这里面我们如果说我们能从我们的队列里面获取到一个 Pro request 对象，那么就会执行 Pro message。当前的我们的断点已经停留到了 Pro message，我们看一下它执行的操作，在这里面我们去在执行的过程中看到它会去获取我们的 consumer 信息，这里面我们会基于 MQ client factory 去 select consumer 去找到一个可用的一个consumer。


接下来我们知道当前如果 consumer 它是基于我们 debug 的 MQ push consumer 的实现来完成的，它会基于这个 MQ 的实现的 pull message，这样的话我们去回到看一下，它会依赖我们的 debug MQ 的 post consumer MPL 进行一个，也是执行我们的 Pro message 的操作。其实在这里面执行的过程中，它会包装成一个 Pro crack，基于这个 Pro crack 执行我们的消费信息，接下来它会进行 Pro API wrap 进行一个包装，最终我们执行 poor channel 的MPL，我们的 channel 是个核心的一个操作，最终它会去依赖 m q client a p i m p l 请完成我们信息的操作。


这里面对于 m q client API 是我们可以理解为它是 consumer 的一个关键路径了，接下来它的操作是依赖到 remoting client 这里面的。 remoting client 也就涉及到。 net 的客户端，它执行一个 invoke 的操作， invoke sync 去获取我们信息的一个拉取这里面的。当我们在提交我们，尤其是 pull kernel MPL 的时候，它会把这个 pull call back 包装过来，作为一个回调方法。 call back 它的回调方法的内容。这里面我们重点关注的是unsuccess，我们拉取信息成功以后，它会执行 consumer message service 的 consumer 操作，它已经获取到信息了。 on slice 说明我们这里面 Emock sync 是获取到信息，执行完成。


这里面我们要做的事情是什么呢？是通过 consumer method concerned concurrently 的 service 进行消息的消费，我们会把一个任务，也就是包装到我们的 consumer request 里面，执行 consumer request 的这个任务的异步操作的过程中，会依赖到我们的 message listener 的concurrently，这是我们定义的监听器，就是说执行这个监听的 consumer 调用到我们自己实现的我们消费消息的逻辑。


我们从这里面去可以先了解一下这个 consumer 拉取消息的一个概貌，接下来我们去源码里面去，接着去看一下它执行的流程，在这里面我们可以看到它是获取到我们的信息，最终会执行 pull masses，接着跟下去，这里面我们跟进来，现在又回到了我们这个底票的 MQ push consumer 他做的事情我们可以看到这里面会找到一个 process Queen，如果说会判断一下这个 Queen 它是否已经 drop 掉。如果说这是也是一个校验的操作，这里面也会去判断一下它那个 timestamp 当前的时间戳会保证一下我们当前的状态是正确的。这个状态我们可以看到主要也是我们的 safe state，当前 service center 必须是running，如果是其他状态的话就会直接抛异常中断。我们可以看到还会去判断一下当前我们这个 consumer 是不是暂停状态，如果是暂停状态的话，我们看到它会进行一个延迟的一个处理，在里面延迟处理一定的时间，这里面我们可以看一下这个时间是1000，那么就是对应的一个 1 秒的操作。


接下来我们来去看一下我们的 case message， cut 以及我们的 cats 的一个消息的大小，因为我们知道这是一种虽然是铺子模式，其次也是一个客户端一个拉取的一个模式。这里面我们会去观察我们客户端消费的这个负载情况。假如说我们拉齐了大量的信息， account 数量也好，或者是 message 是两个维度，一个是消息的数量，一个是消息整体的大小，这两个的只要有一个是超标了，它这会就处个暂停状态，让你先消费，消费完了再去我们的 broker 进行拉取。


这里面进行一个逻辑的一个校验，如果说当前的 count 已经大于我们指定的一个标准了，它就会直接就去延迟再加载。下面这里面是也是基于我们的一个 case size 大小，可以就是判断一下如果说它当前积累的信息也达到了一定值，他就会去也是先终止，也就是当现在跳过，这是拉取延迟来加的。我们可以看到这里面是这个值是一个 100 大小，这个 100 是我们可以看到它是一个 100 兆，那么我们继续执行。现在我们可以看到它会判断一下这个 consumer 它是不是一个顺序消息。这里面主要是判断一下我们当前消费的跨度是不是扩大。这里面我们可以看到它现在获取到了我们的 surprise date，也就是我们监听的交期信息，当然它现在它不能为now，这里面去获取当前我们的一个丝巾戳，这里面就是我们比较关注的一个这个 pull call back，可以看一下这个 pull call back 包含了一些on，success、 however 等等的一些处理逻辑。


关注的 success 它处理的过程是最终会执行到我们构建的这个监听器，我们的 listener 这里面是我们先跳过对它的关注，那么我们这里面是接下来它要处理的方式是什么呢？可以看到后面它的一个操作，它会通过这个 pool API wrapper 进行一个 pool kernel m p l，也就是最终把我们的 pool callback 信息放到了一个 kernel IMPR 里面，因为我们现在的执行方式它不能直接去执行到这个断点里面，看一下它的实现内容，在 on success 里面我们看到这里面会有一个拉取信息的一个状态，如果是found，如果找到信息以后我们可以看到它做了什么事。


找到信息以后，这里面我们会做一个消息的处理，这里面是 consumer master service 会提交，也 submit consumer request 会提交我们这个信息，提交这个信息操作以后我们可以看一下它里面做了什么事情，对应它的实现，也就是我们的 concantly 我们的并行处理的过程。在这里面处理的逻辑小。对应的操作我们可以看到这里面它是把我们这些参数包装成一个是 consumer request，一个异步线程的去处理。


这个 consumer request 的处理的方式是什么呢？我们可以看它里面的 run 方法，在 run 方法里面它做了一些简单的校验，接下来它这里面做的事情就是我们重点关注一下它的一个核心的操作逻辑，这里面我们找到对应的 listener 进行了我们的 consumer message 的处理。


这里面其实执行 listener 到 consumer 的处理的话，我们可以看到对于这个它的一个实现，那么去消费我们的信息。那我们看一下这里面有我们的一个默认实现，这里面也就是我们的 consumer 在第一刚开始介绍代码的时候，介绍了我们在这里面实现了一个匿名类，这匿名类就完成了我们的消息的一个消费的过程。这样的话我们可以看到其实我们处理的逻辑是基于 Pro Crack，在最终我们的 consumer request 里面去完成了我们这个 listener 的一个回调监听，这里面它会最终执行到我们的 consumer master 的一个过程。那么我们现在回到我们的断点部分，这里面它执行的一些关键内容给大家介绍了，现在我们直接我们向后执行，那么我们可以看到这里面也是一些校验性的工作。我们看现在执行到这里面我们的 pull API Wrapper 进行一个对我们的 pull callback 的一个提交，去看一下它后面做了哪些操作。从这里面进入，在这里面我们可以看到它会构建出我们的 pool message request handler，也就是在构建我们这个请求的对象了。这个请求对象先把我们的 header 对象构建出来，构建为 header 对象，我们再去获取我们的 broker 地址，这里面我们得到了 broker 地址，可以看到 broker 地址，也就是我们本地的。


这里面我们开始执行我们的基于 MQ kind API 的方式进行 Pro message 的操作。这里面我们去跟一下看这里面它操作的内容，在这里面我们是通过 pull message，我们看一下这是 MQ client API 的一个操作，我们到这里面可以看到当前是我们执行的 MQ client API 的操作方式，这里面会创建，我们可以看到 remoting command，去 create 一个 request command，去创建我们一个远程的一个请求对象。这里面我们再跟一下这里面的一个处理，我们可以看到这里面创建的过程，我们是 remoting command 创建了一个对象，在这个对象我们进行一个逻辑的处理，这里面我们是异步的操作，我们看一下 pull message async 异步操作处理，因为它我们现在跳过了，我们现在因为异步处理直接执行过了。


我们可以看到这里面做的事情，在这里面做的事情其实就是我们用到了 remote client 进行一个 emote async 的一个操作，其实在这里面我们用到了 remote Calendar 的操作，我们可以看到这里面是 remote Calendar，它已经是建立了我们的 Netty 跟 Netty Calendar，跟我们的 broker Server 的一个操作，最终会执行 invoke sync 的方式去执行完我们的操作，回到我们的执行断点这里面它 return now 是因为异步操作，现在这个过程执行完成了。也就是说我们异步操作的逻辑在这里面已经构建完成。
我们现在看到在这里面我们的线程断点回到了我们的 Pro message service，在这里面我们要获取一个我们的对象，通过我们的这个主摄队列去获取。现在我们可以看到一下 pull request，它已经获取到了，现在新的一部轮请求就开始。现在我们去跳过我们的断点，看一下我们的数据消费的一个过程，我们现在把我们的这些断点都给停掉。OK，那么我们跳过了OK，可以看到现在我们的消息已经接收到了，现在把我们这些信息接收消费成功。这里面我们可以看到 consumer 拉取消息的一个过程。

