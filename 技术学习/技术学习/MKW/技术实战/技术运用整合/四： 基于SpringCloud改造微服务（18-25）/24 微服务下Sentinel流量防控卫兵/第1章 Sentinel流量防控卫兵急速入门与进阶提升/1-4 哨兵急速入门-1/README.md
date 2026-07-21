---
title: 1-4 哨兵急速入门-1
---

# 1-4 哨兵急速入门-1

[image](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/0e616b6f-88a1-4b2e-8361-055a2dc64fdb/SCR-20240722-pefu.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TNFF4NXD%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T225828Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIChzL%2FUh2sL2rMb0%2BzMeMDka598%2Btd1NsIrR5Rag06DDAiAl7aO0xSdOPFykvC3HC6tIkOxGNuNsDY2eyZrCPyPQSCqIBAjG%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMpID1HK7HciQKglO4KtwDYTKtlUV9lM5HeyvMuZKPjOqlF%2F3kUaO2h7bI5lsf134JYs5L0JBTNLudQNbKR5r0AiC4MJoxdndwDomtYiL3KsPXKH%2BP85MsctqGHtRoAh3r0gFYkBZkleSK6x1Oa%2BK06UvwT3j34LJd5kAVpEDeOpTYjzlHTYfnNTLrkWTN4gjkzlUBJc36Qp1ucxPqcpc1NiDlktO%2FqwktFSOa1tDF5UnCaUdCTthhwwwAB%2Fc%2FXd9iWqY%2FENfrA%2BcliArUjeT%2BrUj00Z7tjFlSiWNgJjfqrAuF6K4%2FsdVnoyjr9GUpoqteqwxtCu2TVXERdZUlX%2FhB6sr1GBShJN1vd%2BHkiL1imC6jvrDNImWODVp%2FKjxD579myxopn58%2BCzPuXhyxZ%2BoQeeD%2B2lZgpPLi%2FL8OdwNg0qW9rI1%2F9BPuJAdsF4qfQ0pNq7S%2BQ7EsQGxfa1Jh26YAYLTnsFpVZLtfH1atyxoZwX8O6PtMNrGWSD3tZqU9oNSe7uTSFb1Zn6ZLO6Q6Z1YWIMtR%2F8qrtPMtbF15zTh8hldyOLYaqxDfV9UOkOeqmPshINhgUhgdaS7zzyM%2BHZdL0aUECcOhU6iTIx%2B%2FajNFHeI73KRgRIojbnU2D%2FzjlveZQzI32T1myDx48XQwhLf%2F0gY6pgGoM%2FoQ4NpvQUTSq8QEwYRJKbFqOl9yDjhdQ3mcXuRVqL0INyTDKH47MESmD3Dt2p5xmtmCyBkdKulvV4HAlY30p7hi8z%2BtY1DG8xgci2xeWp2Vbnld74gJYjCEvrv%2BL3OVMBtF%2BYksW2YgZxO8SREX6jaxjhBrzDnB2o1OlvVNZ69XSYkg3js3CP2g0bgJR9K2SPchHD58Nw2fj4Q7ED0%2BPD09lV%2Fq&X-Amz-Signature=225698bc573fdfb180c5d4f2589543035f2bb022386ce23e4f2697fc61078b3d&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

我们来看一看这个哨兵急速入门需要哪些关键的步骤。急速入门第一件事情就是要有对应的这个泡沫依赖，第二件事情就是定义资源，那第三件事情 step 3 就是要定义规则。

[image](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/7ea33e02-513f-4f32-bf79-b6ca3eb400b2/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TNFF4NXD%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T225828Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIChzL%2FUh2sL2rMb0%2BzMeMDka598%2Btd1NsIrR5Rag06DDAiAl7aO0xSdOPFykvC3HC6tIkOxGNuNsDY2eyZrCPyPQSCqIBAjG%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMpID1HK7HciQKglO4KtwDYTKtlUV9lM5HeyvMuZKPjOqlF%2F3kUaO2h7bI5lsf134JYs5L0JBTNLudQNbKR5r0AiC4MJoxdndwDomtYiL3KsPXKH%2BP85MsctqGHtRoAh3r0gFYkBZkleSK6x1Oa%2BK06UvwT3j34LJd5kAVpEDeOpTYjzlHTYfnNTLrkWTN4gjkzlUBJc36Qp1ucxPqcpc1NiDlktO%2FqwktFSOa1tDF5UnCaUdCTthhwwwAB%2Fc%2FXd9iWqY%2FENfrA%2BcliArUjeT%2BrUj00Z7tjFlSiWNgJjfqrAuF6K4%2FsdVnoyjr9GUpoqteqwxtCu2TVXERdZUlX%2FhB6sr1GBShJN1vd%2BHkiL1imC6jvrDNImWODVp%2FKjxD579myxopn58%2BCzPuXhyxZ%2BoQeeD%2B2lZgpPLi%2FL8OdwNg0qW9rI1%2F9BPuJAdsF4qfQ0pNq7S%2BQ7EsQGxfa1Jh26YAYLTnsFpVZLtfH1atyxoZwX8O6PtMNrGWSD3tZqU9oNSe7uTSFb1Zn6ZLO6Q6Z1YWIMtR%2F8qrtPMtbF15zTh8hldyOLYaqxDfV9UOkOeqmPshINhgUhgdaS7zzyM%2BHZdL0aUECcOhU6iTIx%2B%2FajNFHeI73KRgRIojbnU2D%2FzjlveZQzI32T1myDx48XQwhLf%2F0gY6pgGoM%2FoQ4NpvQUTSq8QEwYRJKbFqOl9yDjhdQ3mcXuRVqL0INyTDKH47MESmD3Dt2p5xmtmCyBkdKulvV4HAlY30p7hi8z%2BtY1DG8xgci2xeWp2Vbnld74gJYjCEvrv%2BL3OVMBtF%2BYksW2YgZxO8SREX6jaxjhBrzDnB2o1OlvVNZ69XSYkg3js3CP2g0bgJR9K2SPchHD58Nw2fj4Q7ED0%2BPD09lV%2Fq&X-Amz-Signature=18662ddddb3b7ec0a931ab6696653a5703fa8624081836c373987ba91949c331&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

然后最后我们就通过资源定义规则，最后一步就是查看一下我们的实际的这个效果。 OK 那这个实际的效果后面我可以跟大家一点点去说，那我们按照这个四个步骤一起来进行这个实际的编码。Ok.那老师在这里已经打开了关于这个哨兵阿里巴巴的这个 sentence 它的这个 data 的一个主页。那目前这个哨兵他现在最新的 release 版本就是一点六点三，这个版本目前是我们哨兵最新的版本。那在这里老师讲跟大家一起来通过这个最新的一点六点三版本进行一个学习。

[https://sentinelguard.io/zh-cn/docs/quick-start.html](https://sentinelguard.io/zh-cn/docs/quick-start.html)


首先小伙伴们要做的事情就是从这个一点六点三的这个版本上，然后去获不出来一个分支。然后在这个基础之上我们去进行学习。那老师在这里已经把整个的这个环境准备好了，我们来看一看，现在哨兵它里边有好多好多包，看见了。但是这么多个包其实最核心的包有哪几个呢？无非就是一个铐包，还有一个这个戴斯豹的包。


其实早在一点六点零之前的版本，它没有第三方的像跟阿波罗跟这个extension 、nicos 、Redis 、 keeper 就是这些持有化规则的包，它一点六点零版本之前是没有的。后面的小伙伴们如果想去自己去持久化自己的规则，完全可以去采用它帮你去实现的这些具体的这个依赖。那当然我们后面要做的是想自己去完全的去手动的去自己去实现一下。那其实你最终要结合自己的这个实际的需求，结合自己的业务，然后去进行集成。


OK 好了，那我们废话不多说，我们先看一看它整个的这个源码包下面比较核心的就是这个 demo 这块，看它有好多好多的 demo 就供你去学习和参考。那在这里我们其实可以参考着官方文档，跟大家一起进入我们三四次的学习。那再往下拉，我们看到这里边它里边有一个叫做中文文档，我们打开这个中文档点击一下。那其实学习任何一个新的技术，你首先要掌握自己方法，你自己有一个就对应的这个套路，大家重写好了。然后他这里边最开始开篇就是说什么是哨兵，然后他做一些介绍。然后还有就是刚才就上节课 PPT 所说的这一幅图，就是它的整个的这个主要特性。然后再往下看就是克斯萨特了，先不着急看克斯萨克这边的这个文档的右侧的这个竖形。在这里我们可以先浏览一下，比如说 roadmap 就是整个哨兵，他的就是说他的一些演进的版本都需要做了什么，具体的功能从这个零点二点零版本，它支持了这个异步调用热点参数和白名单等。然后 1.4 版本开始支持了这个集群限流的这个 base 基础版，看见了吧。


那这个所谓集群限流是什么意思？后面我们再详细去说。但是我们看到正在演进到这个 1.5 版本，说支持 reactive 然后还支持 X Java React 然后 1.6 版本目前已经支持 API get way 流控了。那这个是什么意思？那其实从我的角度来讲，那之前老版本 1.4 版本他想做全局流控的时候，它采用的是集群的限制。但是那个集群流控它其实有方方面面的问题。所以说我觉得 1.6 版本，它就把集群的限制给它暂时 delay 了，延迟了不再去做开发了，只是作为一个附属功能去应用。那后面 1.6 版本开始就真正的去做到了 get way 网关。那网关其实说白了，你可以理解为它就是一个集群限流的一个升级版。因为我们所有流量的入口都需要走到这个 API get 位。


所以说从 1.6 开始，我推荐大家在实际的工作中就不要去采用这个集群了，包括其实在阿里内部基本上也没有太多的业务线去接，都是用单个节点单个服务器的流。所以说对于集群流控我们了解一下即可。后面的老师会专门花一点时间跟大家讲一讲集群限流属于什么概念。然后我们再往下看，可能后面可要支持一些什么 C 加加的一些基础功能，那这就不说了，然后这个是详细的这个 RO 脉，你学习任何技术，你看到这个官网给你这么好的一个这个文档，那你就应该看一看哪些是我想要应用的。


在实际工作中，尤其是在做技术选型的时候，你应该先看对应的这个技术的 roadmap 好了，我们回过头来看看这个里边都有哪些功能呢？我们的右侧数里边如何使用工作原理，还有这个流量控制，这很明显是很重要的一点。还有集群流控，刚才我说的网关的流控以及熔断降级，包括热点参数设置和系统的自适应以及黑白名单的控制，包括实时的这个数据的监控以及动态规则很重要。然后包括控制台、 dashboard 启动项。


在我们实际应用哨兵的时候，我们开始启动的时候要注意配置哪些规则。然后在生产环境如何去使用我们的 sentence 以及 sentence 对注解的支持，还有跟主流框架的适配。当然这个下面的技术学多语言、生态圈，包括那开源贡献这些无所谓了。那其实我们浏览下来，大体上了解了哨兵他的这个各个功能。那接下来我们就快速的进行一个入门，帮大家快速的去学习。好，我们回退回去就好了。这是最开始的一个主页面介绍，中文文档的主页面介绍，我们直接看 quick start 那我们看看怎么去使用。首先第一件事情就是要引入对应的 pom 文件，这是老师在 PPT 里说的。那我们按照这个步骤一步步跟大家呢去进行编码和学习。好在这里老师已经准备好了一个小的 demo 工程，就叫做 santa 杠 demo 杠 test 我们打开这个 test 库存，首先要把我们对应的这个依赖包引进来，那这也是必须要做的，我双击 pom 文件。然后我们把刚才这个 dependency 我把它引进来，我们现在是用的是 163 版本，就是号 163 的这个哨兵。引入它以后，我们会看到这个对应的 dependency 已经有了一个对应的 dependency 了。有了它以后我们看一看我们怎么去使用。在这里我们直接新建一个package ，叫做 com.bfx y.test 好，有了这个 test 文件，我们看一看官方是怎么去做的，我们跟着它一步步来就好了。
首先引入了这个 pom 文件之后，第二步叫做定义资源，就是接下来我们要把控制流量的这个代码，也就是 center 的 API 它说有一个叫做 SP hy.entry 然后这里边写了一个 hello world 和 entry.next 看见了，要把这两行代码包围起来即可。就是你想要进行流控代码，必须要用它的 API 的代码和把流控的代码片段包裹起来。那通过这句话我们就知道我们的哨兵它的流控规则，它的这个力度要比我们之前所知道的像那个 Google 的 goalimit 要比我们之前 cloud 里边的这个 hashtag 断路器更要力度要细。因为我们断路器一般大家都使用这种对应的注解，在方法上加一个注解。然后他就会对一个方法做一些流控的手段，做一些进程池的流控信号量的流控等等。但是你会看到你通过这一句话你就知道我们的 sentence 它的核心是什么，它是针对于某一个代码片段做什么。我们下面代码大家可以看我以这个 hello world 为开始。


最后 finally 的时候，我中间以它为开头，以它为结束。中间我的业务代码我要对这一行 system.out 做留空，就是可能这是你自己的业务。比如说你的一个方法里边可能有好多好多具体需要流通的地方，这是最细粒度的代码片段级别的流。那这里我相信小伙伴们就知道我们小明主要的做的事情。


完成这两步以后，我们做什么事情？我当然他也提供了这个注解，叫做艾特 sentinel resource 然后我们看到流控完了之后，下一件事情就要定义规则，这个规则是非常重要的。这个定义规则我们看到这个规则在创建一个 list 叫做 ruler 然后这个规则名称叫做 follow ruler 然后把 follow ruler 又 new 出来了，然后又加上了一些 set resource set yander 然后又加了什么，又加了 count 以及 add ruler 把这个 ruler 加到这个 list 中。最后用一个叫做 model ruler manager 去 load ruler 撕，把这个东西加进去，这是什么意思？这就是表示定义一个规则。


然后完成这三步以后，我们的 sentence 其实就能正常工作了。可能小伙伴们看这个就觉得我没太懂，一会我们去写代码的时候详细的跟小朋友们说，然后接下来就检查效果。在你的这个默认的路径就是在用户目录下的这个 logs CSP 下面会有一个你自己的这个 matches.lock 的叉叉，你可以看到里边对应的输出如果你有访问的话，你会看到对应的数字。那这样的输出代表什么意思，我们来详细来看一看。


就是 P 代表通过的请求的数量，然后 block 代表被阻塞的请求，看下开始是 0 的，这后面就是 1000 多个，然后 1 万多个被阻塞的请求，S代表成功的请求，成功请求多少20。那同学们你看到这一点你就知道。那我的哨兵这是 1 秒为单位的，就是 15 点 41 分 45 秒 46 秒四十七四十八四十九。例如说每一秒钟我最大允许通过的请求是多少个呢？ 20 可以了吧。看这里边有个叫做 set count 它对应着打一个注释，叫做 set limit to PS two20。 OK 也就是说现在我对这个流控做一个设置，最大每秒钟不能超过 20 个进程过去然后后面这个 E 就是抛异常的数量，然后最后这个 rt 就是表示响应时间了。当然这个响应时间可能平均响应时长和 rt 就是每秒钟的平均显示时长。


那我们看到了，那这个就是什么呢？这个就是我们的哨兵，你做流控之后，他会帮你去打出来一些相关的日志到对应的这个日志文件里，这是它对应的功能。然后其实在这里额外说一下它第五步叫做启动我们的这个控制台，也就是说什么意思，我们通过控制台可以对这些实时的资源进行一个抓取，然后控制台可以做一个展示。在这里我跟小伙伴说我们在 demo 运行完之后打出的一些什么呢？一些日志都会被控制台程序抓到自己的这个应用控台服务里面，然后通过可视化的展示重来对应的每一个服务，它的 QPS rt 等等一些对应的这个可视化的东西，这是控制台做的事情。然后后面就是一些详细的文档了。好了，我们大体上了解了这个 sentence 那我们来一起动手来写一写对应的代码。




