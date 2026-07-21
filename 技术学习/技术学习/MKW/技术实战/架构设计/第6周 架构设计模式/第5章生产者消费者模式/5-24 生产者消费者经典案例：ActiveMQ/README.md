---
title: 5-24 生产者消费者经典案例：ActiveMQ
---

# 5-24 生产者消费者经典案例：ActiveMQ

一直讲到说把这个生产者消费者模式通过一种消息中间件的方式来实现起来，对吧？前面的过程中我们一直在讲这个问题，那现在我们来真正来看一下一些比较优秀的这个消息中间点的实现。首先我们来看一下一个经典的代表 x m q，其实当然后面还有一种跟 appqm q 相近的，比如像什么 rap 点 q 什么之类的，这其实都是非常接近的，有很多这种中基建开产品，唉，我们就不一一享受。这里随便的跳了一个 active q，那首先 activity q 它怎么样？它就可以实现我们之前讲的这种生产者消费者模式中的很多很多的功能，那我们下面就一一来介绍一下，大概它能实现哪些功能？嗯，如果说对这部分比较熟悉的同学，你听一听，有哪些东西是你知道的，哪一个人是不知道的，咱们这个可以探讨，对吧？嗯，如果说你不知道的，那你就认真听一下，反正这个呢，我们这里只是介绍一下，其实你也不用做什么笔记之类的，完了之后你听完这个简介以后，你自己回去还是要深入的去使用体验一下这个 activity 相关的这些功能，然后以前对这个东西真正的一个掌握，对吧？对于我们这种架构式培训学习或者自我实践是比较重要的一件事情，所以说你不要光听老师在这边讲，你自己戴着耳朵听一下就好了。

[image](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/e498c466-6cc3-43de-9655-e168e0b62d1d/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666WHDQGZH%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T230628Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIDaB5xB3qU69oEqwSvvoQxuCyvR95q7%2Bfp1%2Fot9fzr4YAiB1x863NXYXJjeXX9WP6U6guCPwYX7F%2FK2loLEzApKAsyqIBAjG%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIM1zh1HgMzhtWdrNFkKtwDIa5fEFd6ZWBQla1oeCGoc89zoMH2PFYp1%2FllHvaM3cv2PHIqVSnW%2Fo77eQ4NeC8ms8VeEDJ6V4FGKCBMBwrLoQXvA4r%2FGDNa%2Be04dye9oQkidT04xXRH%2B3JlzqtmYzp6Epf36LGdvt6pOxt%2F%2FZHF11cp6MEpJf1L3xQMLe4snOrEjFXsUWnJ4jQRBv0xS3Bezlvc5YbK4b0%2BMOjUzovlhIunNKmeRZMzir%2FhK3IY%2BntE4y697NqSLi1Ffhnf8OTHiiy6sBRxIFOdUn4HR8esIn7wsS34XgmRw71fMfRdOH7isMqjdRwbUrT1KqKq7onON3Ed%2BaP9eS8IW%2Bgomn%2BbSwKIR8jHERDMTfebNc%2FOQzC2nT3O6W3eLI6RF84Z0pv0UzTIHdERkaY1kqQPDgm4Yc%2BP5eo4M4HZuXzaGBhXxcN1f8mbwSBoMkWQ%2F7Z7b%2FmnQTjsUAV2RNybAvn%2B46iU5AAnI2h9bmiVo9B0YsVBBr9r%2F762Y3PeF%2B3%2BraUurKcwMsvRpR26jjMYi2O%2F0C1hfiSf85gaOn6FfKC4XcumK%2BWK%2FMWmA%2BekIBFrgcLNOuaUcOp4ureQB%2BD%2FVdrduuPoLP4luJq8hBWF5iNu%2F15KgHuwxbpuqDoXpeOgDbkwlbf%2F0gY6pgG7nKeqVZC8ioe72Ek%2Fcrc8b0JW93qASoVZ%2FuEevOj%2FR7Qw9z8w0bGfeTcrL6G%2F00981oxfR%2Fjr3ZRjab7gXx0c1BEH3buWoggKMpgfa%2FqZXXQ%2F0ergHIzuvDBEjjfMAdW8qScPBtqf9WQXFqKbeur5D6L2FQic%2F26yixISUfXUdWXcJ29yI7%2FhB%2F7WKOQ%2FU5d68VbBi9d8tRpsTyZD0loqjKunPiEi&X-Amz-Signature=f36013f00f844bdd40b9c0f5fb2f3aa833a1ef0a9ed0d93086223e7b0cd2dd70&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

我经常跟你讲的一件事，我们讲的时候都只是点到为止，很多地方因为它没办法把每一个点都深入下去，我重要的是分享这种思想和思考的方式，关于更细节的东西，有些东西是必须要你自己动手去探索的，就比如说叫 actomoq 这些角。首先我们知道 academic 很多功能它都是基于 GMS 规范来实现出来的，这一点其实是不是所有的这个消息中间都一定是这样子的，但是 XMQ 相对来说它是比较遵循 GMS 规范这种东西大家一定要了解。像我们其实谈到了什么 QOS 这种消息整体机制，包括我们还有常多的时候这个是基于 q 还是基于topic，就是 pop SUB 这个模式， let me q 这种基础功能都是 100% 的时间的，还有就是讲的这个数据的存储，就这个消息到这边，它在容器里面，就是咱们这个中间件里面它怎么存储的？它也提供了很多种方式的存储尝试支持，还有包括我们谈到的这个集群的问题，它这个 XMQ 它都是有支持的。


所以这些方方面面，你看是不是基本上跟我们之前就讲的时候，就你要设计一种这个生产者消费者模式的实现的时候，基本上都是比较接近的，但你说细节上，你看细节上 100% 都有很多的差异的，对吧？那我们具体来看一下。首先来讲，比如说像XMQI，它是支持这个 GMS 规范支持的比较好的关于 GMS 相关的这个协议，可是这个东西我就不详细的讲了，其实因为你只要看一下 Java 对于 JMS 的这种，然后规范的定义就可以了。相对来说比较简单一点就是如何创建连接，取得这个连接之后怎么建立一个想要的这样一个生产者或者消费者，然后再怎么发消息，怎么收消息，简单来讲就是对基础能力的一个规范。 XMQ 是相当于一个 MS 的provider，类似这样子，那所以说同时 XMQ 它提供了各种各样的连接选择，这一点是比较好，对吧？它支持http、 https 点对点的这种，什么UDP、SSL、storm、 TCPXMPP 都是支持的，这种就给了就是一些不同场景的不同的连接方式，有很多选择，这种就是我们之前在讲这个设计的时候没有详细的讲这一块，为什么这么讲？就是说因为其实现在不能场景，所以在这个业务场景主要还用在应用的这个选择范围，其实可能是相对比较宽的，你不同的场合相应该使用不同的一些方式，那可能每个实现的这个中间件的实现方式上还是有些选择性和差异性的。反正你到时候如果你要选一个中间件的时候，你就看你是在哪个场合，你选一个对你的时间比较好的这个东西就可以了。


这点你没有必要去深究这个问题，因为这个连接属于相对比较底层一点的，它并不表示说我们这个送给消费者模式的一种什么决定性因素，这个因为它是底层。从 TCP 的七层协议来看的话，对吧？我们目前在现在分成结果里面讲的这个层，一层都是隔开的连接层，就相对于下面一点，我们那个其实在上面应用层一点，所以你不要太在意这个事情。然后就是说这个 MQ 它其实是属于一个中间件，所谓的中间件你觉得怎么样？你是这个地方，其实你是完全不用考虑说你自己使用什么语言和它进行一个交互，那你可以使用另外一种语言，这个就是前面我们也讲过的这个灵活性，就是在生产者、消费者模式里面一种灵活性选择，就是说有可能这个生产者它是一种对，Python、PHP、goal，对吧？那对于你来讲，你愿意用 Java 就用Java，愿意用Scala、 Scala 用额度解释都是可以的，就说他在给你不同的平台，只要你实现了他的规范，按照他的消息格式或者连接方式的要求，你实现了这种客户端，你可以生成这一把，消费者都可以做的。


所以说这点是没有什么疑问的，对吧？还有就是说他，嗯，在讲这个，是我们这个课程前面在讲到这个数据的存储方案的时候，你讲的说，其实你是需要考量一个存储方案来保证这个消息就尽量不丢失，对吧？不可能所有的消息全部都一直放在内存里面。这个前面我们也讲过，首先 academic 它其实提供了很多这种这个持久方案的，比如说它自己的卡 RDB 这种东西，都是它提供了一款持久方案的一个解决，这个对于我们来讲前面有讲过的，就是因为你把它放在这个数据库里面也罢，还放在一个文件里面也罢，还放在什么样也罢，都是保证一个读写的一个高效率性，对吧？这个其实对于是我们比较重要的一件事情。然后对于我个人而言的话，其实最重要的一点就是集群方案。我们也看一下，在前面讲那个 container 这一层的时候，作为中间件对于集群来讲是非常重要的，因为现金这个社会，你要是没有集群的话，基本这个产品的这个竞争力还是说实话还是相对比较差一点。


唉，为什么这么讲？就是因为现在你一个单机的容量的话，其实可能能够突破的这个上限，闪容就被突破掉的，因为你动不动的话，如果一个服务可能就是几千万起掉了，然后产生了 n 多个消息。所以说你这一个单机的人，你讲这样一个单机版的这样一个中间件消息，中间件我们具体再说可能就不够看。所以一般来讲这个集群方案其实是比较倾向于是一种优先的方式，然后在 x v q 里面它提供了几种不同的这样一个集群方案，它这种一般都是使用一种 master save 的方式，有一种最简单的一个 Marshall slave 方式，它不使用任何文件系统或者数据库系统，它直接使用卡号 DB 的方式让它做文具持久化存储。
还有一个master，它只带一个 Snake master，在工作期间把消息所有的这个消息的相关的这些信息全部同步到这个 slave 里面去，如果一旦这个 master 它挂了，那 slaver 就会自动接替它的工作，并且将已经发送变为消费的这个消息保持了它这个状态。因为它所谓的状态和消息本身都是被复制过去的，所以说 master 和 snow 关系相对来说，在一个确定的 latency 就是这个岩石里面，其实它状态几乎性是一致的。


当你说啊，好巧不巧，有没有那么一点，那肯定会有的，之前我们在讲那个 best save 的时候就讲过这个，只要是有数据复制的话，任何一种数据复制方式都有可能会有 latency 的，只要在你的融入范围内都是可以的。所以说当 master 挂错， Slaves 之间能接受，对吧？那这样子就直可以直接切换一下，就像原来 Slaves 的master，然后再重置原来的这个stove，甚至马上之后这个地方开始读取，这是一种简单的一个 master stove 的这种直接模式。


还有一种就是说它是有一种类似于 JDB seed 这样一个事情，就是说，嗯，它不存在说一个 master slave 的一个事先定义，就跟前面讲的这个 master slave 不太一样，它们两个就是共享数据源的一个 broker 来构成了一个 GDB seed master state，首先抢到资源的就是相当于是一把数据库锁一样的这样一个blocker，就在这个节点他就成为了master，其他的他也会尝试拿这个东西。


如果说一旦是这一个 master 他崩溃了，那其他的 broker 抢占资源，马上肯定至少有一台可以抢到，就是拿到了把共享锁这样子它就会成为一个master，然后接替它来工作。因为它是所谓的数据都是那个 JTC 里面的，说白了就是在底层数据库里面，所以它就不存在复制问题，那直接从那里面读就可以了，所以说这也是 Adam q 这个集群的一种实现方式。


关于其他的可能就是前面有讲到过的这个 GMS 怎么去做这个生产者、消费者这种东西，大家在这方面都要去花点时间去看看SDK，还有包括它的这个控制台什么安全加密这东西大家都需要去了解一下，因为我们这个课程并不是专门讲这种消息中推荐的，有可能有别的老师会去开门开这种课程，但是大家可以去专门去定义一下这种课程。


我这个方案只是说用 activity 这种实现替代这个传统的这个现在这消费者模式的这样一个实现，让大家理解一下它是在设计上，实现上有什么特点。跟我们前面讲的这种设计模式当中，哪些点是几乎一模一样的，还是哪些点有一些小小的差异，大家自己去根据细节和你感兴趣的点做一些深入挖掘，这样子就可以和我们前面讲的理由就是相互印证，知道说哪些东西是你自己感兴趣的，哪些是你业务场景中所需要的，然后你根据这样子就至少可以掌握一个可以作为中间件的做起。以后当你遇到这个业务场景的时候，你就可以把它应用得上，对吧？

