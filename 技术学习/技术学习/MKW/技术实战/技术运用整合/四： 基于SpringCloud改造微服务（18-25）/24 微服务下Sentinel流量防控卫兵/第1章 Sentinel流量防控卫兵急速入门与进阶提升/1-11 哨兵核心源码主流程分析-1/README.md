---
title: 1-11 哨兵核心源码主流程分析-1
---

# 1-11 哨兵核心源码主流程分析-1

[image](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/455408b2-ff8a-4bb1-b3d7-fd71f92c4bfd/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666VJGGGK7%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T225833Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCXmJ7Y2%2BRxjBuhZifo4B8Z9Psk1IuWLrTtg10HLQdqxQIgLen%2FbqAOavy1iXOGtBmbhpmhPeY%2B0HZdYPE2Gnpx%2BREqiAQIxv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDJCrvjrgSiJgQ%2BTwQCrcA41jWTdB1JtUcftXBcQD%2BQJUfQPjdCiUZY6VKAWMnWMJDxV2RsV1yIZyatcsT%2B1rlXh2ekd5wzcaiP%2FFBg2yQXfOg5wkAxiEr97Mi3D93Voynd%2BpJvJErbvQjxAFuZZv%2FIJ0XrUKUw9UIDPfU68DYP3WA2L5%2BsZuvku14agi%2FU%2BaWifpiLvAl5eXc5%2BzNDX1quf2ukPWKzZHjuRrZo5PMMMEcAFep7t2TldKr4u3fONghrkAm7cY0DbOHOcF3Ug5bkIV5E3cad3TDfd3THC1l2%2Fj7RjNO7g%2BVKc0hxgid4RugiTguXcc6XrMAfYv27hwIxYjcYFMTumSxKkMaNslpMfxrf6Xyvs%2B1Iao5hT0iPPcObZQB%2Bb7ucxBqUZi6wsqunnOMWxk4%2F%2F0x9vkA30raRUkIC9roASHeJjo7GVUcGuRi%2FWapv1Le%2FftPCY9f3Tjwbt%2B0yn6x7V9UpGGSia9P9ME6yBZpXSZLaSU3Mpj0nPEmQCNT0hh6lhgISHr3NVsvTfiNHsq0odb%2Fq%2F2mfJjF1%2BhOdP1oH1faZ8eUyB88FF0A14N5ORc0l9VdsFRR8O0I8iW9MWbaJB%2FFIPlQ2UGen%2FwjpCDxkvUwXfZ%2BAHz4BU81Kxa6dA0LZ8t3tzpMMS6%2F9IGOqUBiTFy0zGizgvxeprslbVx%2Bbg5IfGAtGHFPnRydbAdfLuk9zImrIk84aOLObsc%2FlZoEM%2F9GtaFDhtGnu9YonwVtT08v1ljMRgv3AA5m9Da%2FFkSf%2FbPKjF91k1bOkR%2BP%2BSE0j%2FWd0m82TOVkuWCCfVc6%2FVTUtpMrlfRgFz39S83G%2BC%2BzmYwPbsnyzsuFUptsojGdtJ7osEMCqf3OI0AqCMe0fNM3PBR&X-Amz-Signature=676d8f971a2cbde82187e339fadc442dd8c4f0a08ef4079f41b7e10ca93049c1&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

大家好，那我们这节课来做什么事情？我们主要来剖析一下我们整个山体哨兵它的一个核心的主流程，对它的源码进行一个全面的分析。在这里我们首先应该回到我们最开始的这个 hello world 小程序。然后我们点到 hello world 点开之后我们其实看到了最开始这个主函数的入口一定要做一件事情，就是我们的 sphu.entry 这个方法。走到这个方法以后，他就帮我们去做流量的一个控制。然后当这个超过限制的时候，它会抛出我们的 flow exception 当然也可以用这个父类 block exception 去捕获。在 final 类的时候，你一定要去退出这个安全，也就是调用它的这个 next 方法。 

[https://github.com/alibaba/Sentinel/wiki/注解支持](https://github.com/alibaba/Sentinel/wiki/注解支持)

**OK 那我们看到这个代码你先不用着急说直接点到它具体的实现。**

**我们在学习任何源码的时候，首先第一点就起码你要会这个东西怎么去使用。**

**
第二点，你要是一定要思考，如果是这个方法或者是这个框架让我去设计，我应该怎么去做流控呢？你先应该有一个自己简单的思考，怎么说从架构的角度去分析。我想要去做哨兵流控的组件的话，如果是我该怎么去做，我该怎么去统计，我该怎么去设计，一定要有这个思考**。


有了这个前两点作为基础之后，第三点你也不要去就是盲目的去直接看到源码，看看跟我想的是否一样不一样的话，那你这样的话你会直接陷进去，我会越看感觉这个代码会越费劲。那第三点要做什么事情呢？很简单，找他的官方文档去看一下整个官方文档是怎么去设计，跟你设计的是否一样，对不对？如果跟你设计的不一样，那你可以参考一下，你看看他们怎么去把这个东西做得更好，你自己想的有哪些不足，一定要对应的要做这件事情。好了，那我们在这里直接老师给大家已经打开了，就是在我们的这个右侧数里面工作原理这块，我们来一起把这个工作原理简单的浏览一下。那 sentence 工作主流程在这里边分这几点，一个目录有一个 orwell 然后有这么几个 slot 看见了吧。有一个叫做 node select slot 它的主要的目的就是建立一个树状的结构，就是调用的链路。


然后有一个叫做 cluster builder slot 根据资源保存统计的触点，然后叫做 static slot 这是非常关键的一个 slot 了，它叫做实时的数据统计，里面可能有好多指标需要你去做统计，然后再往下才是 block slot grade slot 跟我们的 system slot 好了，这些东西是怎么回事呢？我们先看 overview 就说在我们的 sentence 里边所有的资源都对应一个资源名称，就是我们的这个 resource name 就我们写个 hello world 的时候要有个资源，然后这个资源要跟某一个规则绑定，怎么绑定起来，你要 set resource 在规则里每一次调用资源都会创建一个 entry 对象，这是什么意思？那你就看我们的代码，看我们每次去调用这个资源。


说白了，在这里边 sphu.entry 相当于都创建了一个 entry 对象，这是哨兵里边的一个非常核心的对象。你看我那外部学科每次调用一下，它其实都是创建类。 OK 然后再回过头来 NG 可以通过对主流框架的适配自动创建，也可以通过注解的方式或者是调用这个 sph UA PI 显示的创建都可以。那其实这些所有的创建最基础的都是通过 API 去创建，然后创建安全的时候，同时也会创建一系列的功能槽。


这个系列的割光草我们管它叫做 slot chan 就是一个链条一样。那它底层小伙伴们你想一想，它底层怎么实现呢？肯定是一个链表实现的对吧，面表就意味着一定是有一个前后顺序。那这些槽都有不同的职能，例如有这么多的槽，那我们看第一个叫做 node selector slot 他负责收集资源的路径，将这些资源的路径进行一个规避，然后以树状结构的形式去给它存储起来，然后用于调用路径来做一些流控的降级的一些手段。这是 node select slot 的作用，也就是说它对资源做收集的，然后给你生成一个树形，很简单。


第二一个叫做 cluster builder slush 用于存储资源的统计信息以及调用的信息的，比如说我们该资源的一些 rtqps 此外的 count 等等，这些信息将作为多维度的限流。然后降级的依据。也就说这个东西它是用来收集一些信息打点的。然后这个是最重要的叫做 statics slot 用于记录统计不同维度的 one time 指标监控信息，而这个东西才是最核心。然后再往下看，就是具有特定规则的。比如说 follow slot 就是做流控的用来做流量控制的 author 类似 lot 就是做黑名单白名单的一些验证的，用来做黑白名单的控制的。比如说 degree 的 stop 就是用来做预定义处理的预测降级规则来做熔断的。
OK 然后 system stop 是干什么的，是按照系统负载来对流量的走入口做控制的。那我们看到了我们的哨兵，在创建这个安全的时候也会创建一个 slot chat 这个死烙的 chan 大体上分这么几个，它会变成一个链条一样，帮我们去也创建出来。总体的这个框架如下，这个 slot chan 它是贯穿我们整个所有的。首先第一点有一个叫做 train node builder 然后有一个 cluster node builder 最后有一个 statics slot okay 然后 runtime statics 再往下你可以有什么可以有 system slot othly slot 然后 degrade slot 以及 follow slot 然后再往下对应的才是我们的 rules 也就是说这些 slot 创建是有一个先后顺序，创建完了之后，我们所有的 rules 如果是能匹配上某一个 slot 那它就会做限制，相当于规则，跟我们的 slot 是有一个对应关系。


然后再往下看，他说 sentence 将 slot champ builder 作为 SPI 的扩展点，那也就是说有了 SPI 它具备了扩展功能，我们是不是可以去加自己的索拉图也可以。然后你可以加自定义的 slot 然后进行编排，这样的话就可以给 sentence 加一些自定义的功能。


就是如果在实际工作中，这几个 slot 不满足你的需求。比如说我开始是一个统计的 slot 然后是一个系统保护的 slot 一个流控的 slot 包括熔断的 slotok 到时候我不满足需求，我可以在其中的某一个环节之中加上我自己的叫做 my custom slot 加好自己的 slot 实现，这都是可以的。那这就是它的一个扩展的优势，但是也有弊端。什么弊端呢？就是说它必须要走每一个 smart 因为它是一个链表的方式，它只能通过 next 这个方法去找到它下一个界面，然后去执行相应的功能，相应的统计。然后再往下就是具体的，比如说 node selector slot 它主要是负责收集资源的对吧，这些资源它是以树状的形式给我存储出来的。你看他这个 demo 是不是他说上面的这个东西有一个 context util.entry 然后这是什么？你可以认为是一个上下文，然后这个是它具体的资源。然后我对于这个 node A 我创建了一个 entry 然后如果不等于空，我说给他退出。然后最后调上下文的 context util 退出。


好这个代码什么意思呢？我们看一下他说上述代码通过这个创建一个 entries1 上下文。然后同时调用者发起了这个 App 的这个请求，就是下面这个就是我要对这个资源发起请求了。然后这个里边接着他通过这个鹌鹑请求一个 token 就是如果你执行正常就肯定不会抛异常。如果执行不正常，可能会抛这个 block exception 然后表示请求突破成功。如果没有抛的一个异常，就是突破成功。


那上述代码它如果对应着我们的这个 node select slot 它会怎么样去收集呢？我们看它会收集成这么一个形式，就是最里边是一个模式 root 然后就是你的这个 entries note 1， entries note 1 就是就它了，你可以理解就这第一行。然后再往下就是 default note ，就是我们的 note A 就是它它会形成一个树形的结构。然后资源的 ID 就是前面这一块，它是资源 ID 它也是资源 ID 这个资源的 ID 就表示我们的这个唯一的一个标识。 OK 这下面还有更复杂的生成树，你可以去看一看。然后这是它的生成的结构，你可以按照它这个官方的 demo 自己去看一下。


然后 cluster builder slot 是什么意思呢？是插槽用于构建资源的 class node 以及调用来源节点。然后他说可以去统计哪些信息呢？比如说响应信息是响应时间、 QPS 5 lock 的数量、线程数量、议程数量等，这些都会做一个调用来源信息的一个列表，来帮你去统计。那调用来源的名称，比如说是这个名称，以这个圆做一个标记。然后你通过这个命令可以去看一看我们调用者的一个情况，就是通过这个命令这个内容。


好了，我大体上跟小伙伴去浏览一下每一个 slot 它具体的功能，你看这个 TED slot 它是核心功能之一。插槽，有时候这插槽是最重要的，它是用于实时的去统计数据的。它底层采用的一种机制叫做 leap 本位你可以理解为是一个动态的滑动窗口，去实现这种秒级的支持高并发读写的这种统计分析的这么一个数组，它底层是采用 atomic reference 而为去实现的。就是我们的原子的这个数组。 OK 后面我们看代码的时候大家可以看到，然后你会看他这个什么意思。他说我现在把这个一秒钟我分成了这么几个窗口。 sample 看到分成五个窗口看就是 0 到200，200到400，400到六百，六百到八百，八百到 1000 就我分成了五个窗口。你看这里边这幅图，因为我的窗口是滑动的不断的往前走的，所以说当我的 0 到 200 这个时间跑完了之后，过期了对不对？那我这个窗口就往右边移动了一格，那就变成最低是以 200 开头。然后后面的 1000 就逐渐的加上了二百，对就变成一千二了。也就是说我所有的时间往前走，我的窗口也是不断的往前走。


然后在每一个小窗口中都会去做一些统计，比如说统计这个小窗口，它的流量 QPS 总流量是多少对吧？统计这个小窗口，它的这个选修时间， rt 等等是什么状态？它都是这样去体系，这个是它一个滑动窗口策略，也是它最核心的，所以它底层也没有采用这种令牌桶或者其他的，它是自己使用航空窗口去做的。


再往下看就是 slot 然后 degree 的 system 对吧，这些老师就不一一赘述了。好了，我们大体上已经了解了 sentence 它的一个主流程，主流程就是通过调这个 sphu.h 方法，然后他开始帮我去创建一个安全对象，这个安全对象在创建的过程中会有一个 slot chen 这个 slot chen 可能是一个链表，然后每一个列表里面的元素就是一个一个的 slot 比如说有流控的 slot 有统计的 slot 然后有这个集群的 slot 还有热点的 slot 当然最开始的时候比如包括生成数学的思考对吧，还有收集节点的都很多很多。


那我们一点点看吧。现在开始我们来进入代码分析。首先第一点我肯定要点到这个方法里边，按住 ctrl 点进去。同学们请看我已经进来到我们 sentence call 这个包下了，就这是最核心包 sentence call 然后这里边有一个 spo 还有一个 SPU 那 spo 是什么呢？同学们可以看一看 SP HO 是关于 objects 那 sphu 是什么呢？他们俩有什么区别啊？这个其实可以给小伙伴们一个小的作业，大家去研究研究。那我们现在就，看一下这个 sphu 然后他有一个 static 安全方法我们进来的。这里边你看到有一个 name 这个 name 是什么呢？这个 name 不就是我们的资源的 resource 吗？他说 name 的 unique name of the protected 然后 resource 就是说这个资源一定是全局唯一的，要不然的话会有问题。


好，然后它下面有一个参数看见了，这个叫做什么叫做 env.sph 然后点 entry 那这里边三个参数重度参数，除了第一个第二个第三个第四个都是什么意思呢？你可以点进去是不是就是 cos 你可以认为其实不差，这个是 objectok 那其实第二个参数才是比较关键的就是 entry type 但是 type H 组就两种，一种是 in 一种是 out 那什么情况下叫做 in 什么情况下是 out 在这里小伙伴们如果你看过老师之前给你发的一些那个文图的资料，你应该知道 in 就表示输入的资源。 out 就表示输出的资源。比如说我作为一个这个入口对吧，别人来访问我，那我应该叫什么？我应该叫做 in 如果我去访问别人，比如说一个请求过来到我这个服务器了，那我们做流控的时候一定要设置安全 tap 等于点 in 以这个 in 的类型去做一个输入，那进来的流量。所以说我叫 in 奥特，比如说我又访问了数据库，我又访问了其他资源，那么我可以在里边去写一个 out 就叫做舒心好了。那一般来讲我们用 in 比较多， out 其实并不是很多，这里边来看一下，我们还是点了这个点进去。当然他这个用的是就是他认为我这个那个资源是进到我这里边，就是外部的资源进到我内部资源里边。所以说我在这里用boss ，然后再点进去。


点进去之后点到 sph 这个是一个接口这个接口我们之前也看到了，我们按照 ctrl 加 T 它有一个叫做 ctsp H 点进去。然后这里边有一个 string resource wiper 这个东西就是对资源做了一层保护，主要就是你资源名称以及你的资源到底是 in 还是out ，他用一个 string source wrapper 进行一个包裹，做这个对于资源名称和类型的一个存储 laper 包裹了没什么太大作用。 OK 然后我们主要看下面这用 entry 方法，把这个 resource 和 count 以及 X 传进来。这个它是怎么做的？我们看到了这个它里边叫做 entry with poverty 就是带有优先级的这么一个事情。然后再往下看，还得继续点进去。好，点到这儿为止。同学们这个类叫什么？叫做？在铐包下的这个 sentence 的 S 叫做 ctsp h.java 这个类里边的叫做 entry with 它是整个一个代码的核心片段。我们点开来看一下，这里边都做了什么事情。

[image](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/f191b94c-ce8b-424f-a3fb-377e6bfd3f2a/basic-implementation-Sentinel.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666VJGGGK7%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T225833Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCXmJ7Y2%2BRxjBuhZifo4B8Z9Psk1IuWLrTtg10HLQdqxQIgLen%2FbqAOavy1iXOGtBmbhpmhPeY%2B0HZdYPE2Gnpx%2BREqiAQIxv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDJCrvjrgSiJgQ%2BTwQCrcA41jWTdB1JtUcftXBcQD%2BQJUfQPjdCiUZY6VKAWMnWMJDxV2RsV1yIZyatcsT%2B1rlXh2ekd5wzcaiP%2FFBg2yQXfOg5wkAxiEr97Mi3D93Voynd%2BpJvJErbvQjxAFuZZv%2FIJ0XrUKUw9UIDPfU68DYP3WA2L5%2BsZuvku14agi%2FU%2BaWifpiLvAl5eXc5%2BzNDX1quf2ukPWKzZHjuRrZo5PMMMEcAFep7t2TldKr4u3fONghrkAm7cY0DbOHOcF3Ug5bkIV5E3cad3TDfd3THC1l2%2Fj7RjNO7g%2BVKc0hxgid4RugiTguXcc6XrMAfYv27hwIxYjcYFMTumSxKkMaNslpMfxrf6Xyvs%2B1Iao5hT0iPPcObZQB%2Bb7ucxBqUZi6wsqunnOMWxk4%2F%2F0x9vkA30raRUkIC9roASHeJjo7GVUcGuRi%2FWapv1Le%2FftPCY9f3Tjwbt%2B0yn6x7V9UpGGSia9P9ME6yBZpXSZLaSU3Mpj0nPEmQCNT0hh6lhgISHr3NVsvTfiNHsq0odb%2Fq%2F2mfJjF1%2BhOdP1oH1faZ8eUyB88FF0A14N5ORc0l9VdsFRR8O0I8iW9MWbaJB%2FFIPlQ2UGen%2FwjpCDxkvUwXfZ%2BAHz4BU81Kxa6dA0LZ8t3tzpMMS6%2F9IGOqUBiTFy0zGizgvxeprslbVx%2Bbg5IfGAtGHFPnRydbAdfLuk9zImrIk84aOLObsc%2FlZoEM%2F9GtaFDhtGnu9YonwVtT08v1ljMRgv3AA5m9Da%2FFkSf%2FbPKjF91k1bOkR%2BP%2BSE0j%2FWd0m82TOVkuWCCfVc6%2FVTUtpMrlfRgFz39S83G%2BC%2BzmYwPbsnyzsuFUptsojGdtJ7osEMCqf3OI0AqCMe0fNM3PBR&X-Amz-Signature=001b6cb2b7284fc3597f7c168242d98a7752b9f6e3425d11eeb34b24830e49fc&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)





