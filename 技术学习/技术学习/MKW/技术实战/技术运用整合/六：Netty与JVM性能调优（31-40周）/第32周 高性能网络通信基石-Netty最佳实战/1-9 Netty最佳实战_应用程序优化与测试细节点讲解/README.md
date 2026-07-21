---
title: 1-9 Netty最佳实战_应用程序优化与测试细节点讲解
---

# 1-9 Netty最佳实战_应用程序优化与测试细节点讲解

[image](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/3cf766b7-699e-4b51-b38d-0c44790f4190/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46675N5NRWX%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T230021Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCyP4IqtcSz00FqqNrbMgIbeplzmP79DGIqLIr%2BfZyEMgIgfTm5T2LjnZpNKZg0W0fNBc3t5uspAIsNdFUCO3fPsEwqiAQIxv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDBSyRIvV4lOtEKZI4SrcAyzdnDTT%2F89xdBEliGrhnF4CyPiSB7B9NP4%2B6H485hEfw1vixAw9z5%2FLJwRcXbHYE1jHxNngyPh3wixnrYsTPEr8oLHpiZ%2BpDtNsxlH7FnXPpkPD7fzaF4VYQJ2FQTdJtPX2JjgrlzYn2a8Wy2QZX7vDrrmNODLOPLnzIK6Y%2BrdnkYHC7Z%2B3D%2Bc4tEZ8gfLR1hfPNXdWSzhAwAXeHveu6XbNLPVtOJ7BxgYZEI9qFp6k2KsItzPNSB1BJyO1zSkJG%2FWjtFdaxvwjoiynRBK3%2FbZdxo6oAweRU3KaMhgwioWe30MmIJ4Ny%2F5koVwh%2FdR%2BTM0BdRwEJ7%2FNkvKXkZUDlCxY1EVrSWAPQ%2FwCN16yUBALziCkrUoLV2J%2FM1Rubwdd6oOnSrRlIrDkoIdgt086DQ2b2YHrrhu4NyzOP0Ws075lEUp39OInfx1uyZ0UntzJm6IAba662DoSjv9VBMiv%2FcjEcOKPFN16%2BPS1nVaGVgCqy6ETN9w3TwmgWkgcuj2d5BEsilhcfoBIhY2o6IxtVv%2F9kvRypqKWi3ckePrGJQtUGltQsuI0TG2olEum1TXuxkA2UUzomF9pN5YW%2F6UyeyWspNX7xKZAOD08IQvcyZPi3ANNsHMwnw5sxgZxMIC4%2F9IGOqUBCTEXgcZZ%2FvC3m9BgnI815YZ1daa%2BQY77dHfJyLa%2BTQbr2Lqsa%2B2cLEWO8zpYCkEgR0y%2Bh3czvCUonWoj66IyBLjR%2FLj%2BDus67LExVa8bOMohvdI7B53JN9XN6dymYYLt32y20UNbALVZJb0Rvp%2BRQ6zgOwOog94ftHMzYMjAyeFA6vKeq6a9PJ0O%2FQ2Wok9QEnqeAEnfnXwMMx%2BvWax%2B2T0ohNlV&X-Amz-Signature=70b96fd25526be36a8ad1fa899eb98df94f604a9e8585224fbe2ff895cfcac74&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

OK 小伙伴们大家好，我们继续开始上课。其实上节课我们已经把整个的 net 跟我们的 spring boot 整合的全过程，基础的代码已经实现了。接下来其实我们就要来验证一下我们的代码到底 o 不 OK 了。在这里老师也不想去把这些基本的操作再领着小伙伴们从头到尾去敲一遍了。我只是想把一些细节点跟小伙伴们来说一说，来做一个验证。


首先，当然我代码现在已经完整的实现了，它已经是可以通过的。首先我们把具体在我们真正第一次去学 Nike 集成 spring boost 的时候会遇到的一些问题，跟小伙伴们来说清楚，帮助小伙伴们去梳理一下。首先第一点，我们现在 client 端跟搜索端编码都搞定了，接下来的事情应该做什么？同学们想一想，接下来的事情你就要 clang 端主动的去发起一个请求。


我们的 client 端怎么去发起请求？在这里老师有一个类，有 client 这个类，它里边保存了一个channel。看见了。我们看到这里边最后有一个叫做 send message 的方法，它只需要传递对应的模块以及指令，加上你的数据内容，就可以去发送消息到我们的服务器端。具体模块肯定是比如user，具体的指令可能是 save 或者是 update 的方法。后面的内容是什么？后面这个内容就是你的数据信息。当然为什么我在这里去盯一个 generated message V3，而不是具体写一个 user modular 或者是一个group，因为我不知道我发送的模块到底是以什么对象，所以我用一个比较上级的父类去代表。数据发送完了之后就调用我们 message builder 点 get request message 帮我去做到生成一个 message 去传到我们的 net 网络。


中。好了，接下来我们来看一看。具体测试类我已经写完了，在 controller 里边哈 controller 里边我们同学们可以看到我有 3 个 index 测试方法，一个是 save 方法在这里诶同学们请看。我现在用的是 client 点 get instance 点 send message user 包下面的 save command 命令，把 user 通过什么 user module 点 user 点 new 一个 builder 的方式去 set 过去，一个是 ID 是 001 张 3 build 出来，然后 ID 是 002 李 4 build 出来。


如果细心的小伙伴们，你会发现，老师在之前的课程中，我们 client 端是加了一个艾特 component 注解，然后把 nate 相当于 net 的 client 端去交给 spring 去管理。艾特 component 是什么意思？同学们想一想，之前我们肯定是这样去做的，但现在我把它去掉了。为什么我去掉？首先有两点原因。第一点原因，如果你把 net 交给 spoon 管理，会产生问题。会产生什么问题？你整个的 spring 应用程序就是你的 net client，它是一个 spring boot 程序，是启动不起来的，它起码是加载了一半儿就阻塞了。为什么？因为我们知道 spring 启动容器，它的主线程是一个串行化的过程，当我们去扫描到艾特 component client 注解的时候，它肯定会执行构造方法。当然之前的构造方法里边肯定是直接去调用了。什么之前的构造方法里边直接去调用了 connect 去直接创建连接的时候，我们可以去分析一下。


创建连接的时候到最后肯定是同步阻塞的，在这里 a C 口同步阻塞也其实是在这里同步阻塞，等待连接关闭，然后去 close 释放掉。这有一个什么问题，就是当我们的主线程去加载你的 plan 的时候，在 new 出来的时候，去初始化调用同步阻塞的时候，它会把我们整个的什么整个的程序， spring boot 加载的主程序一直卡到这一个点，它就不会往下加载了，会出现这个问题。


怎么去解决？有几种方式。第一种方式很简单，我们再去创建连接的时候，我们异步的在里边去 new 一个 threat 去启动就可以了。这是第一种方式。第二种方式我们可以去做一个更好的一种方式，就是把 component 去掉。为什么去掉？本身来讲，我的 native 跟 spring boot 集成。我期望什么？我期望我的英语程序，我的 spring 容器是不需要去管理 Nike 的，让 Nike 单独自己去启动。我们要做一个解耦。我们自己的业务都不知道有 Nike 这回事，只需要做非常简单的事情，什么事情只需要帮我们去加一个注解就可以了。加我们之前所写的service，我们只需要加载注解就可以了。它就可以帮我们去通过 annotation 扫描的方式帮我们去扫描出来。扫描注入到帮我们去缓存到一个叫做 inworker table 里，我从 table 里去拿出来就好了。本身来讲，这就是跟我们写一个正常的 service 是一样的。这种方式，这是最简单的。所以我期望我们的 Nike 程序不要交给 spring 去管理，这样不太好。在这里既然不让 spring 去管理，老师在这里写一个最简单的单例，就是一个我们看到这个单例了。


OK 单例这里边在创建实例的时候，就用一个空的构造，它必须要有一个 init 的方法，就是 init 方法去帮我们去建立一个连接，当然我希望连接只能建立一次，我就需要加什么加一个 atomic 布尔类型去默认是false。当我们去创建连接之后，我把它设置成true， OK 有并发的情况下，我们需要加一把锁去控制。加一把锁。在这里我选择的就是 single nice 的锁，最简单的。好了，既然是一个单例了，我其实就可以每次去调用上的 message 去发数据就好了。所以在我们这里面，我所有方法直接去获取单例 send message 发出去。获取单例 send message 发出去。


OK 好了，首先接下来有一个问题，就是小伙伴们，我们什么时候去创建 client 端？很简单，既然是要跟 spring boot 集成，我们就用 spring boot 的方式，就是事件通知的方式。在这里我们可以去给我们的 spring boot 主程序添加一个listener。 listener 在我们 application listener read event 的时候，在我们整个 spring boot 都加载完之后，我去做一个事件通知，我去把我的什么把我的 client 端去 init 出来。 init 只能初始化一次，因为我内部去把它做了判断了，开始是false，初始化完了之后就把它设置成 true 了。再往后，即使是多线程，它因为有 sync nice 关键字，所以并发情况下也是安全的。


好了，这是最简单的，当然你用 reach lock 也可以。初始化的时候，我的应用程序加载完毕，我去调用 init 的方法。OK，这已经说了 80% 了，还差一些小的问题。比如我们在最开始慢config，在我们去 component scan 的时候，老师在这里。其实如果细心的小伙伴，你会发现我们之前是这样去做的。


第二， client 也是一个坑。为什么？因为你这样去做之后，他确实能够帮你去。sorry，我把这 content 去掉，它确实能帮你去扫描 Com 点 b f x y 点 net 下面所有的包。但是同学们，你要注意一个问题，在 common 包下有一个类，它比较特殊，它我也是采用 component 的方式，就是 net process bin scanner。它这个包是有一个艾特component，我们本身 common 这个包既是client，也是 server 的。所以小伙伴们一定要注意一点，你这样去做最好的，或者你可以更优雅的方式你。
比如你把 comment 写成一个 spring boot starter 去给它去通过配置的方式，动态的自动装配的方式去给它搞进来，这样也是可以的。我在这里只选择其中一种方式，我就把通过直接扫描全包全路径就好了。这样我们在启 spring 启动的时候也能去识别 Com 点b、f、x、 y 点心 scanner 对应的，它也会帮我去识别，这是没有问题的。


好了，客户端的变化就是这么一点，小伙伴们只要注意几个细节就好了，完整的代码到时候也会发给大家。服务器端也是一样的哈。我们之前 server 也是加上一个注解方式，交给 spring 管理 at component，现在我也变了，是不是我说他就是一个，他就不需要单立，因为他只需要拗一次就好了。当然你想拗多次也会有问题哈。所以在这里小伙伴们你要把它变成单立的就好了。


我在我们的 server 启动的时候也是加了一个事件对不对？加了一个监听 application listener ready event 的时候，我们去把声纹弄出来就可以了，就没有其他变化了。好了，接下来我们来把整体的整个的应用做一个测试。首先我们肯定是启动 net 的 server 端，哈。当然我们在这里主要想跟大家来说一下在真正工作中应该以什么样的编程方式去使用。 native 跟 spring boot 集成。其实里面有很多比较细节的东西，比如你 server 端写的代码太简单了，而且配置也没有。我觉得我课下留给小伙伴们作业，你去把我的代码去做一个优化。我讲的是一个主流的一个主要的思路，他们应该怎么去集成，怎么去做到。我刚才说的这一点就是我们图之前说的外部请求，进来告诉我对应的模块和对应的 command 命令，我就可以把数据发出去扔到让 server 端收到。 server 端处理完了之后就会给我响应，我就能收到应答。我们是要这个过程怎么去做到这种不同的请求命令，对应到不同的处理器，怎么去做到？跟我们的 net 的具体的每一个处理器，跟我们的 spring boot 也其实就是 spring 进行一个完美的集成，采用注解的方式，自己去扫描。主要这个事情。


好，我们同学们请看，我的服务器端已经启动了。当我们整个 stone boot 应用加载完毕，你会看到 started application in 3 秒多钟。整个加载完毕的时候，它会给我们推一个事件应用服务器已经启动成功了，再去启动 net 的 server 端，口号是8765。 OK 好，接下来我们继续往下去看，把我们的提案端也去启动，是通过的application。好，这个时候小伙伴们，我们来看一下服务应用已经启动之后，然后才去。sorry，我们应该换到我们具体的 client 端。 client 端你会发现我们应用程序启动之后，这样你还start。你可以注意观察看我们的 started application in 2 秒多，这样我们的 client 端star，它就不会阻们 application 主应用程序去往下去，继续去执行，继续启动。如果你把 client 放成一个component，这样你在真正的去做什么 connect 的时候，同步阻塞可能会阻们的主应用程序。


这是一个小的问题，小伙伴们一定要注意。我们来做一个测试，比如现在我去写一个 index 方法，还能访问，是不是 index 方法能访问之后就没问题。我们把对应的日志都清空。接下来我们访问一下 seal 方法。回车。 seal 方法搞定了之后，我们看到当前我们的通过，通过我们外部的请求，外部我们的相当于我们的 controller 请求发送了一条数据 001 张三，是不是我们的 server 端是不是收到了？ server 端已经收到了，是不是 C5 OK 就是 0 零 1 杠。


3、 server 端收到了之后，它会回送响应给我们的客户端，所以我们的 client 端已经收到了。叫处理 user save 方法成功。这是 user 的，我们可以换一个。比如我们 a user 的 save 方法，可以换一个 update 方法。再访问一下。好，同学们，请看我们服务器端。


首先收到了 update 的操作， 00204 给我们服务集团做完了这个操作之后，又给我们客户端回送一个响应，叫做 server 处理成功。老师演示的是什么？演示的是同一个模块 user 模块。下面不同的 come on 的 CMD 命令，它是 OK 的，小伙伴们如果感兴趣，你可以去对于什么不同的模块对应的命令做一个测试，这些都是 OK 的。


好了，到现在为止，我们整个的项目实战就已经讲完了。这个项目实战主要目的就是想跟大家分享一下，在实际的工作中，我们的spring，我们的 Nike 框架，如何跟我们的 spring boot 进行一个集成，主要是跟大家讲这个事情。当然我个人觉得这个事情其实主要是一个思路，大家一定要去细心体会，把代码从头到尾的去敲一遍，这样就最好了。


其实我们现在搞定了这个事情以后，我们现在已经实现了数据的可靠性了，白了数据的可靠性怎么去保障？我们回到我们的PPT，把它跟大家简单说一下哈，整个数据的可靠性。最开始我们的可按端把数据发出去，发出去，我们的 solo 端收到数据，这里边我要做一个幂等性，因为有可能我会多发消息，因为其实它其实同步通信。比如我开始发消息，处理完了，处理完它落库操作，给我回送响应的时候，可能响应断开了。这个时候我没有去得到 a C k 的确认，我肯定过一段时间我的数据是超时超出我预期的，我需要把它重新拉出来，再次去推送一遍。这个时候你的 solo 端一定要做好幂等性这个事情，这是非常非常重要的。当我去落库完了之后，给我 a C k，我要更新标识，这个是一个最传统的数据同步的机制，这是第一点。


第二点非常关键的是什么？我们自己的 server 端一定要做一个解耦性的异步处理。开始我数据做完密点性校验之后，直接落库就可以了。其实我可以把它落库的一些offset，其实就是 Mysql 的一些数据，你可以去记录ID。如果你是顺序，其实就是一个offset，我让他去保证一个顺序执行。当然你可以用一些数据库表结构设计，或者是一些打 tag 的方式去做异步执行任务。我肯定有一个另外的一个异步的定时执行任务器，定时器，或者我这么去做，一方面落库，落库完了之后，我去把它扔到一个异步的线程里面，异步的执行器里面去做，去做真正的实际的业务操作。


可能我数据落库了之后，我可能还要对应着有一些业务操作，或者业务操作做完了之后再更新一下数据库，这些都是可以的。或者怎么说，或者你直接搞一个定时任务，每 2 秒钟去扫一次。当然这样这两种方式，哪种方式更好一些？我个人觉得是什么，当我请求推过来以后，做完幂，等我直接落库成功以后，我要做的事情就是干什么把我们落库以后的数据同时去丢到另外一个线程池里边，去异步的去执行你自己的实际的业务逻辑。执行成功了以后，然后给我回送 a C k 响应。


执行成功了以后，其实你就不需要做任何事情了，表示执行成功了，如果执行失败了，其实如果执行成功了，因为你是异步的，你的数据落库了。以后你异步的去做实际的业务处理。落库了，比如开始落库的状态，可能是待处理的状态 0 在异步的线程池里，执行成功了，就把它从 0 改成1，表示成功。执行失败了，可能 3 次以后执行失败就变成了2，这是可以的。可能也会有一个定时任务去定期扫描业务入库里边待处理的数据，已经超时的数据，这些都是可以去做的。所以我们要保证高可靠性，还要保证高性能，尤其是我们的 server 端去在处理的时候。其实我们除了保证这两点以外，我们还有一点我们大家需要想一下，我们现在是单个的客单端和单个的搜索端。其实如果是多个的客单端和多个搜索端，我们 Nike 怎么去实现一个负载均衡？这个是很有意义的。在我们下节课的时候，老师会跟大家去讲一下。我们 Nike 做负载均衡最简单的方式就是使用我们的h、 e proxy 加上 keep live 的用 h 做一个t、 c p 级别的负载信号。当然它也可以有其他方式，比如我的 n g x 也可以去做。在这里老师给大家实际分享一些经验。到底用 n g x 还是 h a box？如果你是自己自建机房，我个人觉得你用 h a 和 n g x 倒无所谓了哈。但是如果你使用阿里云或者阿里云服务器，或者是腾讯云这些云服务，你肯定只能用什么？只能用 n g x。为什么？因为 h e proxy 需要加上 keep love 的去做一个。


怎么说虚拟 VIP 的这么一个概念？虚拟 VIP 其实阿里云肯定是不支持的，他肯定他给你买他哪个服务， IP 就是固定的，你不可能虚拟出来一个VIP，哈，这个是没法去实现的，所以他可能是支持不了 h box。OK，这一点其实是一个比较。其实是老师在很久之前哈，去使用阿里云的时候，有一个比较郁闷的问题，当时我们选择整体的技术框架都已经搞定了，结果最后就卡到不支持 h a，不支持虚拟的 VIP 漂移了，就这种问题上了。所以当时就把技术方案去换到 n g x 了。当时我们是在使用 rock m q，很早之前要看 MQ 做镜像队列集群切换，其实是做一个怎么说 HA 去做协调的HA，做这种 TCP 的多负载，这是不晓得了。所以我们在学习的过程中，我们选择 h a proxy，这是没问题的。但是如果以后工作中，可能你去选择阿里云的 s l b 或者腾讯云的c、 l b，让他去帮你去实现你这种负载均衡故障的切换也可以。


还有一点是，最好的方式是不依赖于任何第三方，我们可以去用什么，我们可以把数据信息存储到租 keeper 里面，这也是可以的。当然，如果你又加一个第三方的注册中心，你整个的个业务的逻辑就是你的实现。所以要相对来讲要复杂一些的。如果你说我的 server 端的信息跟 client 端对应的信息，我都想存储到自己的应用程序。


做keeper，你不管是阿里云服务也好，还是腾讯云，或者是自建机房，都支持你把这些信息都维护到 JK 上。首先第一点加大了 JK 的开发成本，多了一个 JK 的组件。第二点是你的心跳检测等等各方面的机制都需要做一个完善。包括你的服务上下线，你的负载均衡和你的balance，还有你的 fail over，这些你都需要自己去考虑为什么用 n g x 或者 h a，它比较方便。这些负载均衡乱码七糟的事情他都帮你做了。当然做 keeper 也可以去帮我做这件事情。后面其实小伙伴们可以去尝试着去使用 Jupiter 去做好负载均衡的事情。这个可能需要自己稍微去花点时间去写个代码。 OK 好了，我们这节课就讲到这，下节课小伙伴们再见。Ok。

