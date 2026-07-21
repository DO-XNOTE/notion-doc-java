---
title: 1-9 【源码品读】负载均衡策略解析-1
---

# 1-9 【源码品读】负载均衡策略解析-1

[image](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/40d3ce5e-be34-45d0-b7c5-c5138b1f5a79/SCR-20240718-emev.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TR7UR6KG%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T225609Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIDvG8xkydS3p2CgTjFzl4lOievMDE6ywc8qRbfZNvlTgAiEA%2FtT%2BC%2B72JckGrAa4%2BTkJPBUrRy6YInQV4PZx4U302QYqiAQIxv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDJG%2FaSbBhjvvw9n01ircA20O0GWNdjjzI6SkB4EKAu%2FS7BgrIaFigkeGj0nkJ84LBE7KQoFib2eHo1vYK8JIQeCHnr0vd%2BdTphUjjMyNvEhdPQFQPn64ld7zfSgtDQWuNmBXCHAb%2FKAxgW9iE8t3SWNNyxfVeJDdh67fa5SCrqjza3kB4qBknrHUt88A2pEjOXl2tbv0OJx2zy4xvSfg3TGmSpmbLcGiXdElSggRZt%2BLwk3awiRgpvffuNKYnk1XjbtF2AQsd8w%2F7x%2BcrQ1kzbmcVd29ksV3QpgmgCwt13QS%2FUsMDsQKbPjHHCWZyQMi9%2FPu2wNoOSih8RRBa4rSBO%2BF%2BFJp%2BSkuncUvEellziHr56%2F8JUTEyO1Nbc%2FgC%2FbpjgvWfEfQ7fP2sq5VmhnrnWevA%2BOciYjBAzWo%2FmS3ISXd2B0cEZs2cylfqbKgVtjdI0izsz38zfp3uW%2FlVKnt2bv6M4Fz9R3S03I4eAUPEXwrgqvOqSGNezdsTPBb6M53%2FcQaTyKEbuHoQRgxd%2F%2FuSFSnSFiLuzZRs4IkIh%2Fg5t8sA5t5XyUxqkI7ytYnxP6uiJGAvR1nxeXoxcZM52Xh0N0dyM8f28jaiA1WvqABrF4fVJoK38DfUR3PVS86VyvKfptHGPvZL1pbRibrMLW4%2F9IGOqUBoKjF6jgIbHM1O3FTIh5o1rSg4FRaMu8ZNbkTVeMHKApqJpMm9tqnLoXMyOsA5A%2F4XBKEr4GiT4h6vqr8%2BKpYnKC1yf9y%2F7PFvIBIgbHWl6XwBjtjTwrHU23OvecycfBQMQXY7PhkSADKSPopnak7c3Lpl4%2FIoo6YEy%2BKJVRcFA%2FMFDTvdHsJgDGEZPjr1gCPNfID8qXD%2BUksOoPfzl3c5Pk2LqPD&X-Amz-Signature=5a563ebdd33cc28dd76e84d7a1595d36141ad87c3cfc5b60687504e4de813f49&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

[image](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/9b547570-ec61-4d90-8a00-568bb04f0ed4/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TR7UR6KG%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T225609Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIDvG8xkydS3p2CgTjFzl4lOievMDE6ywc8qRbfZNvlTgAiEA%2FtT%2BC%2B72JckGrAa4%2BTkJPBUrRy6YInQV4PZx4U302QYqiAQIxv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDJG%2FaSbBhjvvw9n01ircA20O0GWNdjjzI6SkB4EKAu%2FS7BgrIaFigkeGj0nkJ84LBE7KQoFib2eHo1vYK8JIQeCHnr0vd%2BdTphUjjMyNvEhdPQFQPn64ld7zfSgtDQWuNmBXCHAb%2FKAxgW9iE8t3SWNNyxfVeJDdh67fa5SCrqjza3kB4qBknrHUt88A2pEjOXl2tbv0OJx2zy4xvSfg3TGmSpmbLcGiXdElSggRZt%2BLwk3awiRgpvffuNKYnk1XjbtF2AQsd8w%2F7x%2BcrQ1kzbmcVd29ksV3QpgmgCwt13QS%2FUsMDsQKbPjHHCWZyQMi9%2FPu2wNoOSih8RRBa4rSBO%2BF%2BFJp%2BSkuncUvEellziHr56%2F8JUTEyO1Nbc%2FgC%2FbpjgvWfEfQ7fP2sq5VmhnrnWevA%2BOciYjBAzWo%2FmS3ISXd2B0cEZs2cylfqbKgVtjdI0izsz38zfp3uW%2FlVKnt2bv6M4Fz9R3S03I4eAUPEXwrgqvOqSGNezdsTPBb6M53%2FcQaTyKEbuHoQRgxd%2F%2FuSFSnSFiLuzZRs4IkIh%2Fg5t8sA5t5XyUxqkI7ytYnxP6uiJGAvR1nxeXoxcZM52Xh0N0dyM8f28jaiA1WvqABrF4fVJoK38DfUR3PVS86VyvKfptHGPvZL1pbRibrMLW4%2F9IGOqUBoKjF6jgIbHM1O3FTIh5o1rSg4FRaMu8ZNbkTVeMHKApqJpMm9tqnLoXMyOsA5A%2F4XBKEr4GiT4h6vqr8%2BKpYnKC1yf9y%2F7PFvIBIgbHWl6XwBjtjTwrHU23OvecycfBQMQXY7PhkSADKSPopnak7c3Lpl4%2FIoo6YEy%2BKJVRcFA%2FMFDTvdHsJgDGEZPjr1gCPNfID8qXD%2BUksOoPfzl3c5Pk2LqPD&X-Amz-Signature=44a859b85c27ea473e3abb628bb1364c98f42cef785bfbde2299c56d42d567e7&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

喽，慕课网的各位同学们大家好，这次又到了我们源码阅读的环节了。那这一节我来带大家看一下负载均衡策略在源码级别是如何来实现的。那这一节主要内容都有哪些呢？第一部分我带大家熟悉一下七种负载均衡策略。相信大家在前面的图文章节中已经对瑞本提供的这些默认的负载均衡策略它是怎么运行的？它在流程图的状态流转都有哪些这些知识已经有所熟悉了。

[image](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/b747b5ec-3342-48cb-8c3f-1fafa22e93d1/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TR7UR6KG%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T225609Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIDvG8xkydS3p2CgTjFzl4lOievMDE6ywc8qRbfZNvlTgAiEA%2FtT%2BC%2B72JckGrAa4%2BTkJPBUrRy6YInQV4PZx4U302QYqiAQIxv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDJG%2FaSbBhjvvw9n01ircA20O0GWNdjjzI6SkB4EKAu%2FS7BgrIaFigkeGj0nkJ84LBE7KQoFib2eHo1vYK8JIQeCHnr0vd%2BdTphUjjMyNvEhdPQFQPn64ld7zfSgtDQWuNmBXCHAb%2FKAxgW9iE8t3SWNNyxfVeJDdh67fa5SCrqjza3kB4qBknrHUt88A2pEjOXl2tbv0OJx2zy4xvSfg3TGmSpmbLcGiXdElSggRZt%2BLwk3awiRgpvffuNKYnk1XjbtF2AQsd8w%2F7x%2BcrQ1kzbmcVd29ksV3QpgmgCwt13QS%2FUsMDsQKbPjHHCWZyQMi9%2FPu2wNoOSih8RRBa4rSBO%2BF%2BFJp%2BSkuncUvEellziHr56%2F8JUTEyO1Nbc%2FgC%2FbpjgvWfEfQ7fP2sq5VmhnrnWevA%2BOciYjBAzWo%2FmS3ISXd2B0cEZs2cylfqbKgVtjdI0izsz38zfp3uW%2FlVKnt2bv6M4Fz9R3S03I4eAUPEXwrgqvOqSGNezdsTPBb6M53%2FcQaTyKEbuHoQRgxd%2F%2FuSFSnSFiLuzZRs4IkIh%2Fg5t8sA5t5XyUxqkI7ytYnxP6uiJGAvR1nxeXoxcZM52Xh0N0dyM8f28jaiA1WvqABrF4fVJoK38DfUR3PVS86VyvKfptHGPvZL1pbRibrMLW4%2F9IGOqUBoKjF6jgIbHM1O3FTIh5o1rSg4FRaMu8ZNbkTVeMHKApqJpMm9tqnLoXMyOsA5A%2F4XBKEr4GiT4h6vqr8%2BKpYnKC1yf9y%2F7PFvIBIgbHWl6XwBjtjTwrHU23OvecycfBQMQXY7PhkSADKSPopnak7c3Lpl4%2FIoo6YEy%2BKJVRcFA%2FMFDTvdHsJgDGEZPjr1gCPNfID8qXD%2BUksOoPfzl3c5Pk2LqPD&X-Amz-Signature=c82768bb82b278f07347eb28f03ff507e9d72f35e56f2d07763ea1affaa5815a&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

那么这里我们就挑几种非常常见的负载均衡策略看一看它在源码层面是如何来实现的。那接下来第二部分是复习一下自旋锁的使用方式。自旋锁这个东西听起来非常高大上，非常神秘对不对？但是它实际上是一个实现起来非常简单的方式。那它解释面试中经常会被问到的问题，比如像 synchronize 中哪些步骤会用上的自旋锁这种机制。 OK 那这里我们就带大家看一下自旋锁在 ribbon 的负载均衡策略中都有哪些应用。



最后一个部分我们来看一下什么是防御性编程？那大家应该不是第一次听到防御性变成这个名词了，对不对？我们说防火防盗防师兄，那这个防御性编程它是防谁呢？我们不防去瑞本的代码里一探究竟。好，那接下来我们就抄起家伙准备开工吧。每天 coding 1 小时，健康工作 50 年。你不用 coding 你看人 coding 也可以，健康工作 50 年。那我们这里就到了 raben 的源代码处。大家看到这个包字小，我给大家念一下 ribbon load balancer 这个包下，全都是它的负载均衡策略基于负载均衡的框架。那我们第一个负载均衡策略来看谁呢？话说做题要怎么样从简到易，对不对？就来看一下这个最简单最随性洒脱不拘一格的 random roll 随意而为，好收起小桌板。这就是它的源代码了非常少，但是你看这个书写个相当工整，赏心悦目，而且每一行相对注释都非常完全，这个才是怎么样心目中的开源项目。


源码应该有的风格。但是 ribbon 因为功能比较简单，大家如果往后看像比如 high streaks 的源码 oil 那就头大了。我们后面有了头疼了。先来从简单的看起。大家来看它的核心的源码都在 choose 这个方法里对不对？那它是谁来调用这个 choose 的？我们往下翻。看到这有个 overrider 的 choose 方法，那外面的服务外面的组件，比方说 resttemplate 或者是我们后面将要学到的 gateway hystrix 那这里都会应用 ribbon 的 choose 方法来选择一个具体的服务器。


好，我们这里先来跟进去看一下。那 choose 方法有两个参数，一个是 load balance 另外一个是 object 是一个 key 那在这个 random row 里面大家可以看到这个 key 实际上是没有使用的，没有相应的引用，那我们就先忽略它了。


OK 从第一行开始看起，那如果我传入的 load balancer 是空，那么自然而然的我没有机器返回，对不对？直接返回空。那接下来这里有一个 while 循环，那如果这个 server 是空，我要持续的找到一个可用的服务器。那在第一步大家看到这里有一个很奇怪的 thread interrupted 这是什么含义呢？为什么它这里会用到thread 。我们向后来看一下，这里大家先看，如果这个线程被暂停了对不对？被中断，那么它将返回一个空，那什么情况下会中断？往后看，这里定义了两个 list 一个叫 uplist 一个叫 all list 这两个 list 有什么区别呢？ all list 就是 load balancer 中获取到的所有服务器，不管他死活死的活的，全部都暴汗，这是一个拳击拉壮钉全拉出来了。


那 up list 顾名思义，你的 server 是 up 状态的，也就是它是可运行状态的正儿，没有任何异常还在持续运行。那它是 up list 那接下来我们这里有一个 server countserver count 取哪个值呢？取 all list 的 size 值，也就是目前所有机器的数量。


那如果 server count 是0，那代表什么含义？代表目前没有注册对应的节点，在服务中心上一个节点没获取，那所以它返回一个空往后这里就相当于是 random road 相对核心一点的部分了。它怎么样？它把这个当前所有机器的最大数量传入到一个 choose random int 的方法中，拿到一个下标。那这个 choose red mint 是什么呢？我们看一下。这里看到它使用了一个 thread local random 那这个类应该大家在编程的时候也会用到过。那它怎么样呢？它拿到当前 thread 中传入了一个 server 


count 那它返回一个什么值呢？它返回 0 到这个 server count 中间的任意一个值，那它是随机的。
那这里我再跟大家牵扯一个小的知识点，大家知道 Java 中这个随机是真随机还是伪随机吗？大家知道什么叫真随机数吗？ OK 我这样跟大家说，我们做 Java 时候，不管是用 random 类还是 thread local random 之类的类，那你总要在生成随机数之前传入一个种子数据对不对？我们说，实际上 Java 中的所有数字它都并不是真随机数，也就是在所有输入都一定的情况下，不管你把什么样的种子数据插入进去，它可以是当前的时间或者是当前的时间戳中的后几位，不管你让它再具有可变化的性质，它都是可以预测结果的。


那什么是真随机数呢？真随机数它往往有的时候要掺杂一些你不可预测的东西来作为一个种子生成数据。比如说怎么样，比如说你当前 CPU 的温度，那它是你不可预测的。所以有些时候真随机数往往会通过一些硬件来生成。那这个硬件有一些感应器或者是温度感受器或者是噪声感受器，它会采集甚至环境中当前的噪声来作为随机数的种子，产生一个真随机数。


OK 那我这里稍微拓展了一点，那大家再回到主线上来。记住这个 choose red mint 是返回一个 0 到 server count 中的其中一个随机的值。那它作为 index 怎么样从 up list 中获得这个 indexok 那它的 server 有可能为空，那为什么会有为空呢？大家明白这个含义吗？你看它下面有一个注解。


the only time this should happen is if the server list were somehow trimmed 就是说发生这个条件的因素是这个 server list 正在被修正。 OK 那如果发生了这种情况，我怎么样？我是不是要重新再选择一台 server 呢？大家看这里他做了一个什么事 thread yelled 这个一个 yelled 方法，大家可能平时没太见过，它是为什么呢？ yelled 相当于一种退让的意思。


比方说我作为美国总统对不对？经常需要在国会发言。那反对派有的时候故意占用国会发言时间，不让总统发言。那这时候下面我这党派的成员就会去上去发言。在他获得发言的权利之后，他会说这样一句话， I will yield to the president of United States of america 什么意思啊？就说他把自己的发言机会让给了自己的总统上去发言。


Ok.那这个 yelled 实际上意思是类似的，他将自己当前的县城可以出让出去，让其他线程来继续分摊这个资源，也就是分摊 CPU 的资源，让 CPU 也可以切到其他同级的线程上去运行。那既然这里牵扯到了一个线程的退让，所以它的上面我们再回到最上面看到吗？这最上面有一个 if 条件，判断线程是不是被中断。那我们说这其实是一种防御性编程的体现。为什么他考虑到了所有的异常情况，他认为所有的输出所有的外部环境都是不安全的。我们说这个就是防御性编程的前提。他即使我们保证传入过来的 LB 一定是有值的。那么我们也不妨在这边加一个 if 把它作为空值来判断，那这就是假定所有的输入都是不安全。


所以我们很多有经验的程序员，他即使当前状态下他知道你的传入参数不可能为空，但是他依然会这样写一句，为什么？因为未来是可变的，你不能预知未来有很多变数，有可能其他调用方来调用，你的时候就会传入一个空值。所以我们经常在写代码的时候，强调大家要使用防御性编程，那就是这样一个道理，避免未来的异常发生。


OK 我们这里再回到起点。如果 server 为空，我把线程可以作为出让，并且 continue 进行下一次循环。那如果 server 不为空，我们这里加一个判断， server is aliveserver 如果现在是存活的，也就是可用的，那么我们直接把这个 server 腾回去，如果不可用怎么办呢？不可用就把这个 server 制成空。


那下一次 for 循环会再循环到一个新的 server 上。在设置成空以后，这边也会使用一个 thread yield 跟上面保持一致也就是说这个方法大家记住，在每次 while 循环进入下一个循环的时候，都会用线程出让这样一种方式。 OK 那这就是 random road 的核心非常简单，对不对？无非是有一些特殊的扩展知识，比如 thread yield 以及它的真随机数尾随机数好，那这个看完了，接下来我们看哪一个 row round rubbing row 好，这个我们进来。


那这个 role 为什么中间有个叫 robin 的单词呢？


这就搞不清楚了，太阳子这个 author 列表里面也没有一个叫 robin 的人。我们不管他了进入主线，那它的 choose 方法大部分跟前面的 random row 是相同的。第一步，如果 load balancer 是空，那我同样的也返回，空什么都不做。


接下来一个 while 循环，那这个 while 循环跟前面的 random row 有个不同之处是什么呢？它这边有一个计数器，如果你重试了多少次，你重试了 10 次依然没有结果返回，那么它就不会再继续重试下去了。那这里会打一行什么？打一行 log no available a live service 那就是你重试了 10 次依然没有找到一个可用的服务器。 OK 那就它返回一个空了。那反观我们的 random row ，我们现在切到了 random row 这个 while 循环没有做次数限制，那它如果说重试到所有的节点都试完了，它依然没有合适的。怎么办？继续重试，它的永无止境。 endless 好，那我们现在切回到 round robin row 继续往下看。


这两个 list 跟前面 random row 的 list 一样，一个是所有服务的列表，一个是目前来说 reachable 的 server 列表。 reachable 的 server 列表实际上就是 up serverok 那同样的这两个 count 是对应上面两个 list 的大小，你这里的 if 条件。如果你的 server count 和 up count 都是0，那么代表着你当前没有可用的服务器。对不对？那就返回一个空。接下来这个 index 看到这一个 next server index 就是选择哪个下标的服务器了。那这里我们看一下它有一些特殊处理。点进去好，看到这个 for 循环吗？两眼一摸黑，两个冒号，这什么？这就是自旋所。同学们，自旋所是不是一个听起来很高大上，但实际上很 low 很容易理解的一个使用方式？那它不仅有 for 循环使用方式还有一种什么？ while 循环， while true 让它永远在这自旋。那它在自旋的过程中肯定需要有个退出条件，推出条件就是放在这个业务逻辑里面。那大家其实可以看到，这种自旋锁的应用在 ribbon 以及很多开源项目中都非常非常多。


OK 那我们这里看这个 current 是什么？是一个 next server 的 counter 这个 counter 是一个 atomic integer 一个线程安全的 int 类型的数字。好，那我从这个数字里面 get 到一个 current 这个 current 是什么呢？就是我上一次访问到的机器对不对？它的下标。


那这里 next 怎么算呢？ current 加一取模，看到吗？ current 加一取模，那这个模是什么？我们来传到外层看一看膜就是 server count 那比方说你这个现在有 100 台 server 那你上一次已经轮询到了第 90 台，那么这里就是第 90 台加上 1 取一个摩 100 的摩，那它的 next 就是91，非常简单，它这里为什么不直接把 current 加 1 返回回去，而还要取一个模，这是为什么呢？大家有没有考虑到？因为这个 server 的 list 它可能会发生大小的变化，对不对？有可能你上一次访问到了第 100 台机器，那你现在这次再进来的时候，这第 100 台机器突然挂掉了，那它从它的 server 列表中被移除出去了，它只有 99 台了。所以我们不能单纯的把它加一赋给 next 而是要做一个取模的操作。


OK 那剩下一步是什么？ compare and set 大家知道 compare and swap 是开词操作，那 compare and set 实际上 compare and set 跟 compare swap 没有区别，这都是 cast 操作。


什么是 case 呢？那大家应该都非常熟悉了，这个也是面试中的热点问题，也就是说它比对你当前的想要替换的值是不是这个 current 的值？如果是 current 把它替换成 next 那如果不是 current 怎么办呢？那这个 if 条件就返回一个 false 接下来继续 for 循环，继续自旋对不对？所以说这个自旋加 swapcompare 操作是一个非常非常常见的消耗资源很少的线程同步方式。


okay 那我们看 compare and swap 点进去，它是用的什么用的非常出名的 unsafe some mask 包下的一个类用的它的 compare 的 swap 操作。那再点进去，你们会发现这个方法实际上是一个 native 修饰的方法，它已经不在 Java 层面了，它是由操作系统层面实现的一个方法，底层的函数。
OK 那实际上大家总会觉得compare ，我先比较，然后再 swap 那这两步应该是分两个操作，它在操作系统层面怎么保证原子性呢？实际上在系统函数里面，这个 compare swap 就是一个操作，一个原子性操作，所以它能保证你的整个操作是一个原子性的。


那我们这里看到了自旋锁加 case 操作的应用，那么返回到上一层，那这里获得了什么？获得了 next server index 那获得 next server index 之后，就把这个 server 从所有机器列表中把它给拿掉，拿到了之后判断它是不是空。如果是空，这里依然用了线程让步并且重试，那重试 10 次，如果还为空，那就返回空了。 OK 那假设它不为空，那这里条件就是你的 server 如果是正常的，并且 ready to serve my request 这个情况下把你返回，否则的话这里把你置为空。


那么这里在最后一步条件跟前面的 random row 不同的是，它没有做线程的让步，因为它这个有时间次数的限制，它 10 次就完全的退出来了，所以它并不会过长的占用线程，而 random row 它为什么需要做线程让步呢？大家现在这里明白了吗？因为它没有退出条件对不对？它这个退出条件为空，它只有 server 是否为空才作为一个退出条件。


所以说它有可能会持续不断的一直在这 running 那它消耗的是什么？是线程资源？我们不可能让这个当前的 rubbing row 一直占用着整个线程。所以它在每次做下一个循环的时候要做线程的让步。而 robbing row 不同，你总共最多也就用 10 次。那所以我在每次这里循环的时候就不需要再做线程让步了。对不对？ OK 那接着往下前面我们已经讲到了，如果做了 10 次依然没有返回，那么就直接返回一个空 round robin row 到这里就要结束了。


那我这里再给大家提一个小问题，同学们可能有所不知， round rubbing row 有一个天然的天坑。为什么呢？你看这个 increment and get module 这个方法，当前服务器自增加 1 作为下次服务器访问的那个 index 这里有什么坑呢？我们来看这个计数器它就是关键所在。


这个计数器在 round rubbing row 初始化的方法中给它赋了一个什么值？ 0 对不对？那假设我们集群中有 4000 台服务器，这 4000 台服务器不巧在同一时间全部重启了，并且他们都应用了 round robin root 那这个在 4000 台服务器当中，它的计数器的初始值谁？都是0。


那假如我们在上一层，我们返回到上一层这里 server 列表也是按照统一的顺序排序的。也就是在说这 4000 台服务器中，每台服务器拿到的 server 列表都是按照同一个顺序排序的。那么当请求到达每台机器的时候，他们怎么访问？他们肯定是从第零台机器依次往后第一台，第二台第三台这样访问下去。那也就是说所有的请求可能在相对密集的时间内都会落到第零台机器，然后接着第一台机器，接着第二台机器。那这样的话，负载均衡岂不是会给机器带来更大的压力吗？那大家知道 round 


robin road 里面怎么解决的这个问题吗？这就是留给大家课后思考的小问题，大家可以想一想，如果交给你来你怎么解决，或者说 ribbon 它怎么解决？ OK 那这一节我们学了这两个row ，大家心里觉得哪一个 row 应用起来更加合适呢？ on the robin road 对不对？一来它效率可能比较高一些，因为它的 while 有个退出条件，不会长时间占用资源。二来它的访问比较平滑，一个往后移动，不像 random row 但随意而为随意访问节点，它的负载均衡可能并不是非常可控可预测的。


OK 所以我们在项目中默认使用的大部分都是 round robinroll 对不对？那这一节的内容先讲到这里，下一节我带大家看两个更加复杂一点的 role 好，下一节我们再见。

[image](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/23063fee-e0ff-467d-8b4f-3d6b00633c60/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TR7UR6KG%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T225610Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIDvG8xkydS3p2CgTjFzl4lOievMDE6ywc8qRbfZNvlTgAiEA%2FtT%2BC%2B72JckGrAa4%2BTkJPBUrRy6YInQV4PZx4U302QYqiAQIxv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDJG%2FaSbBhjvvw9n01ircA20O0GWNdjjzI6SkB4EKAu%2FS7BgrIaFigkeGj0nkJ84LBE7KQoFib2eHo1vYK8JIQeCHnr0vd%2BdTphUjjMyNvEhdPQFQPn64ld7zfSgtDQWuNmBXCHAb%2FKAxgW9iE8t3SWNNyxfVeJDdh67fa5SCrqjza3kB4qBknrHUt88A2pEjOXl2tbv0OJx2zy4xvSfg3TGmSpmbLcGiXdElSggRZt%2BLwk3awiRgpvffuNKYnk1XjbtF2AQsd8w%2F7x%2BcrQ1kzbmcVd29ksV3QpgmgCwt13QS%2FUsMDsQKbPjHHCWZyQMi9%2FPu2wNoOSih8RRBa4rSBO%2BF%2BFJp%2BSkuncUvEellziHr56%2F8JUTEyO1Nbc%2FgC%2FbpjgvWfEfQ7fP2sq5VmhnrnWevA%2BOciYjBAzWo%2FmS3ISXd2B0cEZs2cylfqbKgVtjdI0izsz38zfp3uW%2FlVKnt2bv6M4Fz9R3S03I4eAUPEXwrgqvOqSGNezdsTPBb6M53%2FcQaTyKEbuHoQRgxd%2F%2FuSFSnSFiLuzZRs4IkIh%2Fg5t8sA5t5XyUxqkI7ytYnxP6uiJGAvR1nxeXoxcZM52Xh0N0dyM8f28jaiA1WvqABrF4fVJoK38DfUR3PVS86VyvKfptHGPvZL1pbRibrMLW4%2F9IGOqUBoKjF6jgIbHM1O3FTIh5o1rSg4FRaMu8ZNbkTVeMHKApqJpMm9tqnLoXMyOsA5A%2F4XBKEr4GiT4h6vqr8%2BKpYnKC1yf9y%2F7PFvIBIgbHWl6XwBjtjTwrHU23OvecycfBQMQXY7PhkSADKSPopnak7c3Lpl4%2FIoo6YEy%2BKJVRcFA%2FMFDTvdHsJgDGEZPjr1gCPNfID8qXD%2BUksOoPfzl3c5Pk2LqPD&X-Amz-Signature=09147af378cdadb5fc73a701f8a682800b5c10806af7e8a7af16c422b1df1c96&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

[image](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/0b6b8b2d-7122-4507-8aa2-30b6b893ce77/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TR7UR6KG%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T225610Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIDvG8xkydS3p2CgTjFzl4lOievMDE6ywc8qRbfZNvlTgAiEA%2FtT%2BC%2B72JckGrAa4%2BTkJPBUrRy6YInQV4PZx4U302QYqiAQIxv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDJG%2FaSbBhjvvw9n01ircA20O0GWNdjjzI6SkB4EKAu%2FS7BgrIaFigkeGj0nkJ84LBE7KQoFib2eHo1vYK8JIQeCHnr0vd%2BdTphUjjMyNvEhdPQFQPn64ld7zfSgtDQWuNmBXCHAb%2FKAxgW9iE8t3SWNNyxfVeJDdh67fa5SCrqjza3kB4qBknrHUt88A2pEjOXl2tbv0OJx2zy4xvSfg3TGmSpmbLcGiXdElSggRZt%2BLwk3awiRgpvffuNKYnk1XjbtF2AQsd8w%2F7x%2BcrQ1kzbmcVd29ksV3QpgmgCwt13QS%2FUsMDsQKbPjHHCWZyQMi9%2FPu2wNoOSih8RRBa4rSBO%2BF%2BFJp%2BSkuncUvEellziHr56%2F8JUTEyO1Nbc%2FgC%2FbpjgvWfEfQ7fP2sq5VmhnrnWevA%2BOciYjBAzWo%2FmS3ISXd2B0cEZs2cylfqbKgVtjdI0izsz38zfp3uW%2FlVKnt2bv6M4Fz9R3S03I4eAUPEXwrgqvOqSGNezdsTPBb6M53%2FcQaTyKEbuHoQRgxd%2F%2FuSFSnSFiLuzZRs4IkIh%2Fg5t8sA5t5XyUxqkI7ytYnxP6uiJGAvR1nxeXoxcZM52Xh0N0dyM8f28jaiA1WvqABrF4fVJoK38DfUR3PVS86VyvKfptHGPvZL1pbRibrMLW4%2F9IGOqUBoKjF6jgIbHM1O3FTIh5o1rSg4FRaMu8ZNbkTVeMHKApqJpMm9tqnLoXMyOsA5A%2F4XBKEr4GiT4h6vqr8%2BKpYnKC1yf9y%2F7PFvIBIgbHWl6XwBjtjTwrHU23OvecycfBQMQXY7PhkSADKSPopnak7c3Lpl4%2FIoo6YEy%2BKJVRcFA%2FMFDTvdHsJgDGEZPjr1gCPNfID8qXD%2BUksOoPfzl3c5Pk2LqPD&X-Amz-Signature=53f61276811ccb46e04586faf03f898b04225b4f3b4a51b2fb766f656a81550d&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

# ======RetryRule

[image](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/1ad814c4-c1f6-4bc0-a775-b531dd87b811/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TR7UR6KG%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T225610Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIDvG8xkydS3p2CgTjFzl4lOievMDE6ywc8qRbfZNvlTgAiEA%2FtT%2BC%2B72JckGrAa4%2BTkJPBUrRy6YInQV4PZx4U302QYqiAQIxv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDJG%2FaSbBhjvvw9n01ircA20O0GWNdjjzI6SkB4EKAu%2FS7BgrIaFigkeGj0nkJ84LBE7KQoFib2eHo1vYK8JIQeCHnr0vd%2BdTphUjjMyNvEhdPQFQPn64ld7zfSgtDQWuNmBXCHAb%2FKAxgW9iE8t3SWNNyxfVeJDdh67fa5SCrqjza3kB4qBknrHUt88A2pEjOXl2tbv0OJx2zy4xvSfg3TGmSpmbLcGiXdElSggRZt%2BLwk3awiRgpvffuNKYnk1XjbtF2AQsd8w%2F7x%2BcrQ1kzbmcVd29ksV3QpgmgCwt13QS%2FUsMDsQKbPjHHCWZyQMi9%2FPu2wNoOSih8RRBa4rSBO%2BF%2BFJp%2BSkuncUvEellziHr56%2F8JUTEyO1Nbc%2FgC%2FbpjgvWfEfQ7fP2sq5VmhnrnWevA%2BOciYjBAzWo%2FmS3ISXd2B0cEZs2cylfqbKgVtjdI0izsz38zfp3uW%2FlVKnt2bv6M4Fz9R3S03I4eAUPEXwrgqvOqSGNezdsTPBb6M53%2FcQaTyKEbuHoQRgxd%2F%2FuSFSnSFiLuzZRs4IkIh%2Fg5t8sA5t5XyUxqkI7ytYnxP6uiJGAvR1nxeXoxcZM52Xh0N0dyM8f28jaiA1WvqABrF4fVJoK38DfUR3PVS86VyvKfptHGPvZL1pbRibrMLW4%2F9IGOqUBoKjF6jgIbHM1O3FTIh5o1rSg4FRaMu8ZNbkTVeMHKApqJpMm9tqnLoXMyOsA5A%2F4XBKEr4GiT4h6vqr8%2BKpYnKC1yf9y%2F7PFvIBIgbHWl6XwBjtjTwrHU23OvecycfBQMQXY7PhkSADKSPopnak7c3Lpl4%2FIoo6YEy%2BKJVRcFA%2FMFDTvdHsJgDGEZPjr1gCPNfID8qXD%2BUksOoPfzl3c5Pk2LqPD&X-Amz-Signature=5e1d53effbc73e57b13b810407a500b88b27571e607738a45bea6b815a8ea9fe&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



