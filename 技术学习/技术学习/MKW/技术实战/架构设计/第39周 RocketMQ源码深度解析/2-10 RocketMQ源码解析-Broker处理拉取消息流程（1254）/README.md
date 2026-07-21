---
title: 2-10 RocketMQ源码解析-Broker处理拉取消息流程（1254）
---

# 2-10 RocketMQ源码解析-Broker处理拉取消息流程（1254）

大家好，接下来我们来介绍一下 broker 处理拉取消息请求的流程，那么我们作为一个 rock MQ，它的个 consumer 端，他在这里面去发起了我们消费的请求，那么这个发起的消费请求在我们 broker 端是会接收到这个请求，那么接收到这个请求以后我们应该怎么处理呢？也就是 broker Server 它是怎么处理的？我们来看一下。
首先它这里面处理的流程，它的入口也是我们的 native remoting Server，也就是说所有我们 client 端请求的这些请求都会打到我们的 Server 端，都会接收到这个请求，接入到这个请求以后它会进行这么来处理的流程的一个产。


Process. Messenger received. 就是说我要处理我接触到这些请求的信息，那么这里面接触请求的信息，它会根据我们请求的不同类型来去区分它是哪个 master process。我们知道对于我们发送请求的话，它是我们的 send master process，那么对于我们拉取请求的话，拉取消息的话，我们的这种 pull master process，那么在 pull my master process 以后，它会去解析我们的对应的这个请求 process request，这里面会把我们的 Pro Max request head 解析出来。


看一下我们关键的一些信息，那么这里面在解析处理的过程中，它还会去获取到我们当前这个请求 topic 处对应的这个filter，比如说里面有你说的 massive filter，它的实现会根据我们的消息是否支持重试和不重试的方式来创建两个不同的对象。通常是如果支持重试的过滤，我们是 expression for retry master filter，那么默认的是 depress massive filter，它是不只是重试的情况。那么这里面我们在过滤过程中，我们的过滤器也建好了，那么真正要操作的就是 master store，也就是我们的信息的一个存储序，去 get master 获取我们的消息进行消费，那么这个获取消费的过程中，这里面还是比较复杂的。最终我们要做的是当我们消息消费成功以后，我们这里面要对 consumer offset manager 进行一个重新的更新，那么也就是说我们的消息发生了变更，对于我们的 offset 也需要进行一个移位，那么表明我们这里面已经消费成功了。


我们来看一下 rock MQ broker 源码是怎么去处理的。那么首先我们来切到我们的 native remoting Server，这里面我们可以看到它其实处理的过程，我们看对面是按 channel handler syllable，这里面我们通过 process master receivable 里面去接听我们的处理的一个入口。那么我们区分对于我们的 request 命令的处理和 response 命令的处理，我们这里面也是对应的 response 面临的一个处理，这里面我们可以看到它是已经跳到了 native struct，这我们在介绍 prototure 的过程中也涉及到这样一个过程，这里面的处理我们可以看到它最终会执行到我们的 process 的一个执行同步或者是异步的一个 process crash 的操作，那么这里面我们它会使用到我们一个同步的操作，那么里面会切换到 protest request。


对于这里面 protest request 的实现，我们可以看到这里面我们会回到我们的 pool message，我们可以切换到了这里面的是 Pro message request 的一个操作，这里面它会也是一个重载的操作，它会执行 process request 的一个 seal 的方法，这里面我们可以看到它会去通过我们的 request 请求解码解出我们的一个 pull message 的 request header 的对象，那么这里面我们看到它里面包含的一些像我们的 consumer group，topic， Queen ID 以及我们的 Queen offset 等等这样一些信息。


OK，它基于这些信息会进行我们下 f 的一个请求，那么其实我们看法在这里面，这个方法是非常长的，我们可以看到从 92 行到 474 行，将近 300 行的一个代码，我们可以看它的出将近 400 行的代码，我们看一下的处理逻辑，所以说这些动代码读起来是比较困难的。


所以说我们自己在写代码的时候千万不要写这么长的代码，通常我们建一个方法，它代码常用的不要超过 50 行，通常 30 行作为我们的一屏的展现是相对来说比较好一些的。那么我们去看一下，我们得到这个 request head 以后，接下来的操作就是我们的一些校验性的一个操作，我们可以看到首先它会去判断一下我们当前这个是否可读，接下来我们再去做的是我们看一下它有没有进行一个 specific global configure 的一些信息，这里面看一下，我们看它会获取我们的 topic configure，那么基于 broker counter 获取到我们的 topic configure 去校验一下。如果 topic configure 如果不存在的话，这里面也是有问题的，就也就直接中断。


这里面我们可以看到它会对我们的 public configure 的一个可读性进行一个校验，其实我们看这里面大部分大段的代码都是一个校验的一个过程，那么我们这里面可以一个快速的一个跳过，那么找到我们所关心的一些内容，我们向后继续。那么在这里面我们看到相对于这里面是一个 master filter，那么 master filter 我们知道对于 rock chemical，它消费的过程是支持消息过滤，并且这个消息过滤是在服务端完成的，也就是 broker 端完成的，那么这里面它完成的方式，我们看这里面定义这个 master filter，它会去判断一下我们当前的 broker configure 这个它是否是支持retry。如果说支持 retry 的话，它会构建一个 expression for retry master filter，如果是不支持 retry 重试，那么它就会构建一个默认的 expression master filter。


得到一个这样一个 filter 以后，我们看我们所依赖的这些信息以及这些校验都已经完成了，那么接下来他要操作的就是我们的基于 Brook control 获取到我们的 message store，也就是我们信息存储器去获取我们的message，有 get message，我们可以看到这里面所支持的这些参数，我们看到它里面有 group topic 以及我们的 Queen ID，还有 offset 以及我们的 maximize number。也就获取最大的一个消息数量以及我们的一个过滤器。


得到这些信息以后，我们看一下它具体的操作。那么这里面我们去到底测的 Meta store 里面去看一下这里面存储，我们可以看到它这个方法也是比较长的，也是将近 160 行左右，所以说这么长的方法读起来我们还是关注它的一些重点的一些信息，在这里面它哪些信息比较重要的？我们首先看它会获取，在这里面先构造了一个 get met result，这种是一个空的内容，我们这里面去获取我们的对应的 consumer Queen，也就是我们的消费队列。获取消费队列这里面还跟我们 offset 相关的一些信息，进行一些初始化的一些操作。在这里面最终它会进行我们的一个消息的一个处理，像这里面它会获取我们这个 map 的 buffer 映射缓存区的一个结果。


后面这里面会对于我们的一些信息进行一个循环的一个获取我们的消息位置的一些信息，这里面对于这个 master star 内容我们简单去介绍到这里面，我们回到看我们这里面的内容。好，那么我们可以看到这里面是获取我们的 master store 的消息，那么对应我们的 get master result，我们可以看到最终这些消息处理完成以后我们要做的一件事情。这里面我们需要对于我们的信息，如果说是放了成功的话，我们把我们的释放的状态设置为success。这些处理完成以后，我们看一下最终我们的消费结果，消费完成我们需要去把 set 进行一个更新，我们可以看到在这里面我们最终会通过博客 control 获取到我们的 consumer offset Messenger，进行我们的 offset 一个提交，这里面提交也就是我们消费完成，把我们 upset 的变更提交到我们的 offset manager 管理器里面，最终里面把我们的 response 信息返回。


那么看到这里面的话，对于我们这个博客处理拉取信息的一个检验的流程也就介绍完成了，那么我们了解了博客处理拉取消息的请求，接下来我们来看一下代码隐私环节，同时我们重点看一下消费信息，这里面一部分是我们原生的 rock MQ client 消费信息，另一部分是集成 rock MQ spring boot STARTER 进行我们的消息。还有我们基于集成的 spring cloud，阿里巴巴 rock MQ 的方式进行消费。


这里面对于我们原生的方式，我们跟大家刚才已经介绍了我们原生的 consumer 消费的过程，这里面我们再简单去回顾一下，其实我们在通过原生的 rock i m client 去构造一个消费器，那么我们需要去创建一下我们的底票的 MQ push consumer，那么其实这是一个 push 的操作，其实我们还有一个对应拉取的一个 consumer 实现，那么我们可以看一下拉取的。这里面有一个叫 debug little pool consumer，我们可以基于它来去主动的去拉取的方式去获取我们的消息，那么这是一种方式。


那么这里面我们要注的关键点，我们需要注意一下，我们需要订阅我们的topic，并且指定一下我们的过滤器，同时我们需要去设置我们的监听器，也就是说我们消费的消息里面需要回调的信息是什么？最终把我们的 consumer 进行一个 star 操作好，那么我们这是对于原生的 rock appeal plander 的效果，那么我们来看一下怎么步的consumer，因为这个在讲，嗯， producer 的时候也跟大家介绍过，所以说这里面我们可以讲的会稍微快一点。


对于这里面我如果说我们基于 spring 步的 consumer 操作的话，消费信息有两种方式，一种方式我们是基于 rock M6 template，对于 rock M6 template 我们可以在里面通过 receive 指定一个实体类的方式把我们的消息消费出来。在这里面其实这里面我们看到它其实是支持一个 class 类型，同时也就是跟我们把我们的消息进行一个反序列化，这样可以获取到。


注意一下我们通过 receive 操作的话，它是一次性的，假如我们获取完就是获取当前能获取的信息，那么这个死点过去以后它就不会重复去执行，所以说我们通过 receive 操作的话，我们这里面需要通过 v 处的方式不停循环迭代的去拉取我们的信息，那么这是一种方式，我们可以看起来是相对来说比较手工的，手工的代码量还是比较多的。


其实如果说我们的业务逻辑比较确定的话，还是建议大家去使用这个 Rocketmq master listener，也就是我们基于这个监听器在对应的我们写的 consumer 里面去加上这个渐进行注写，我们实现对应的 rock MQ listener 指定它的实现，我们指定一下我们接收消息的对象，那么这里面我们指定一下 topic 和我们的 consumer group，那么就可以在程序启动的时候去把这个类注册一个监听器进行监听，那么这个过程是 rock MQ，它是跟斯伦布的集成的一种功能。我们可以从这里面看一下这个 listen 的一个操作。


通常对于这个注解的listen，它是需要我们进行在初始化的时候进行解析的，那么这里面也有对应的解析，我们看是 listen 的 container 的configuration，它会去解析我们这个注解相关的一些信息，最终把它进行一层代理，把它包装到我们的容器的上下文。这是我们对于使用部的 consumer 操作的方式，其实这里面推荐大家使用监听器的方式去完成。


那么我们再来看一下基于 spring Claude 的方式，其实是 spring Claude 阿里巴巴对于 rock Anchor 的一些包装，那么我们单纯从我们使用的代码程度来看的话，我们这里面并没有依赖跟 rock MQ 相关的一些API，所以说整个过程其实我们已经基于 spring q 的 stream 的方式把我们的 rock MQ 这个底层屏蔽起来了。


其实我们使用的都是我们纯粹单纯的一些必应的操作，比如说像这里面的consumer，我们的 consumer 是基于一个sync，我们完成了一个 consumer 的接口就可以去直接进行一个消费。那在这里面的话，我们也并没有跟 rock time 相关的一些信息，其实能看到一些信息的话是我们这里面的 application IML，在 application Yml 里面，对于 stream 下面我们 stream 是个窥探，它下面有多种实现，比如说 MQ 是一种，其次还包括像 Kafka Rubbi m q 都是以一种操作的方式。所以说我们基于 stream 的方式，我们可以做到很简单的把我们底层的 MQ 队列的实现进行一个替换。


那么当然对于 rock MQ 下面的节点的信息，它是跟 rock MQ 相关的，那么这里面我们跟 rock MQ 消费相关的一些代码就介绍完成了。同学们，那么我们关于 rock and new consumer 消费的内容我们先介绍到这里，同学们，我们下一章节再见。

