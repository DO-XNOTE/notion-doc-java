---
title: 1-2 OSI和TCPIP模型
---

# 1-2 OSI和TCPIP模型

加起需求到落地的桥梁，构建 it 新蓝图。我是张飞扬。好，上一节我们聊了聊通信安全的概述，这一节我们来看第一个内容， OSI 和 TCP IP 模型。嗯，大家要说了，飞扬老师不是说好要生动形象的讲课吗？

[image](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/58f3e6d2-902f-47c6-b9e1-1e49bef2b06c/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TT7GW53F%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T231026Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIFZ1xOLS7A43Q4kz7Zg7iaPZ5U8vEhiCdIa4xm3BWzDGAiEA8RKtwY8F%2BFbG%2BMd7q58PPAgkerhG6rU8Lp7AJcbSbvwqiAQIxv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDFw%2BRE6L%2BtnuLNu1YircA8kaTXoj6yE0BZ0G8nagTRFoMFPOUjnfxv9h2X5Lj%2F%2FRsFnqQ9BbYMHLZ%2FL9kfEPQRuvHEt3oXGF3%2FR6SFpuSkul9RJRwYKdke%2FEd9XkC%2FKQTS76Xjrbr9TrjS3%2BR7EeDjD90a7O7QyAgImmy%2Fwkn9CkqG7OsAoBLamfpjC7KNN6bW8aBPYyFfp%2F5h9oUKIY1OK6ixph8w8t%2FRQfhc77M47%2BD0a4%2F3s7TZOAh9EcpA8MaPgjpxcdpBgmr28nSe5H3y6%2FUX7k3zO5RDyJErbYAIxhpZNnhWOpgfc3VS%2FIXFRjgKMf4v5RqBAzd9qvtqexf49ZIZ3vHQJDuYKozSzJSjn14tptrNa%2B4yvGGzV8olYDTyVIQtD4K%2BVUvnhZ66FnTontHYopXkLRUeSXlSxoh28G%2F6B9LgOvvVqS71rCCRyjgl5kHD1Z3ahiT4VRFxtCu9XMNQ2%2BFedWotlEtUjhzfxri4GpV2kSZXbct08%2BCfdzxfC1zQxI6%2BvLvWPOl0Ylz2jmYHbhdQF8afZRPu4mqucbUrRvkmjZ33cIG%2FC1%2Bd16ZZG4cfU7tq24vjk48IXpL2DDxuEjazMnZn49O3KNLOdJYJ3kexUKLRgv4USRRSZXxfowAaDXgAS7KKTPMP%2B2%2F9IGOqUBe8kjrJE3qS8iaeV3S6UEPIMSVyhAi04LDvvXnBTt1FxZbzWtmXwNafDol6HjhDR5f1AxXGTioPDd2OACqpY%2FkDeblp7SVNIKU31snCxCQr5FrWigtp9oNi2Do7JRvGz8FEo%2B6M2u%2FvgLykC0p%2BcF3aL%2BVOBdD8%2FV8Msr58Eh0e7t85EsEBPaiurdwgqaL4vMaAZA6PwQZmeGfQr%2Bk2w9sqQOnFHF&X-Amz-Signature=cca3c4412e3f3dff7026c6bcb2bb7d9d7eb7268dfef445790750f623fea9166e&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

怎么又来开始给我们科普大学里面学过的这种很枯燥的 o s i 模型了？ OSI 模型什么是所有网络通讯和安全的基础？所以我们必须来讲一讲，但是大家都是已经资深的 Java 工程师和 Java 架构师了，我们当然不能再去讲以前那套老路子。


好，付阳老师换一个思路来聊一聊跟我们平时开发，跟我们平时的测试 debug 相关的网络中到底有哪些该注意的点，好不好？这张图形还是一张老图，但是我们要说出新的思路。

[image](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/92fe76d7-36aa-43ca-b0a3-c7f825e0b409/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TT7GW53F%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T231026Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIFZ1xOLS7A43Q4kz7Zg7iaPZ5U8vEhiCdIa4xm3BWzDGAiEA8RKtwY8F%2BFbG%2BMd7q58PPAgkerhG6rU8Lp7AJcbSbvwqiAQIxv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDFw%2BRE6L%2BtnuLNu1YircA8kaTXoj6yE0BZ0G8nagTRFoMFPOUjnfxv9h2X5Lj%2F%2FRsFnqQ9BbYMHLZ%2FL9kfEPQRuvHEt3oXGF3%2FR6SFpuSkul9RJRwYKdke%2FEd9XkC%2FKQTS76Xjrbr9TrjS3%2BR7EeDjD90a7O7QyAgImmy%2Fwkn9CkqG7OsAoBLamfpjC7KNN6bW8aBPYyFfp%2F5h9oUKIY1OK6ixph8w8t%2FRQfhc77M47%2BD0a4%2F3s7TZOAh9EcpA8MaPgjpxcdpBgmr28nSe5H3y6%2FUX7k3zO5RDyJErbYAIxhpZNnhWOpgfc3VS%2FIXFRjgKMf4v5RqBAzd9qvtqexf49ZIZ3vHQJDuYKozSzJSjn14tptrNa%2B4yvGGzV8olYDTyVIQtD4K%2BVUvnhZ66FnTontHYopXkLRUeSXlSxoh28G%2F6B9LgOvvVqS71rCCRyjgl5kHD1Z3ahiT4VRFxtCu9XMNQ2%2BFedWotlEtUjhzfxri4GpV2kSZXbct08%2BCfdzxfC1zQxI6%2BvLvWPOl0Ylz2jmYHbhdQF8afZRPu4mqucbUrRvkmjZ33cIG%2FC1%2Bd16ZZG4cfU7tq24vjk48IXpL2DDxuEjazMnZn49O3KNLOdJYJ3kexUKLRgv4USRRSZXxfowAaDXgAS7KKTPMP%2B2%2F9IGOqUBe8kjrJE3qS8iaeV3S6UEPIMSVyhAi04LDvvXnBTt1FxZbzWtmXwNafDol6HjhDR5f1AxXGTioPDd2OACqpY%2FkDeblp7SVNIKU31snCxCQr5FrWigtp9oNi2Do7JRvGz8FEo%2B6M2u%2FvgLykC0p%2BcF3aL%2BVOBdD8%2FV8Msr58Eh0e7t85EsEBPaiurdwgqaL4vMaAZA6PwQZmeGfQr%2Bk2w9sqQOnFHF&X-Amz-Signature=9533af1efab001682f14e8733934c1f5656fbd2d56081f17ca63115047c49128&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

首先我拿出一支笔，左边这个 7 层大家很熟悉，是不是？这是什么？这是经典的 OSI 模型，这是一个理论模型，它的落地，特别是当前的互联网落地到哪里啊？中间那个层叫 TCP IP 模型。区别在哪里？区别就在于其实 TCP IP 只实现了 4 层下面绿颜色的物理层、链路层、网络层以及蓝颜色的传输层，这才是 TCP IP 真正实现的。


上面那三层它统一扔给了应用层，不管你是用一层实现还是三层实现，甚至于五层实现都和我没有关系，我只负责底下四层的通讯。好，这四层在 TCP IP 的世界又该如何来实现呢？物理层很简单，大家如果是看什么家里面的电视可能走的是同轴线。那如果你已经换成了电信、移动、联通的这种网络电视，那你走的是什么？以太网线？但是我们数据中心你去看一看走的是以太网线吗？不是噢，大部分都是光纤直连，甚至有的是英菲尼版的低延时的，什么高速网络通过不同的物理介质，通过不同的底层的物理层的协议能使信号最好的保持，能使延时最低，这就是物理层在做的事情。


那链路层又在干什么呢？链路层就是把不同的什么网络层映射到物理层，比如说 AIP IP 后面就会聊到在这里面有很多的安全隐患，但同时它也实现了很关键的内容，就是把 IP 地址和我们物理设备的 Mac 地址进行了映射，那除此以外，这个是不是很熟悉 802.3 协议？就是局域网内部的什么有线局域网的通信协议，那同时无线802.11，这是我们手机上面还有很多的这种什么 Wifi 设备所使用的协议。


那除此以外，这个什么载波监听，这是什么有线网络的解决冲突的主要方法？那我们在手机端呢？还有什么载播监听和冲突避免 ca c s m s c a 这些方法都来保证，是吧？局域网里面不管你是新型拓扑还是什么，还是环形拓扑，还是这种仲裁型拓扑，不管你是哪种拓扑，尽量是什么，整个拓扑结构里面，一片网络里面，它们的每个节点是可以之间进行有效、稳定、安全的互通。好在链路层之上的内容才是我们 Java 工程师、 Java 架构是最关心的。


我这里举两个例子， IP 大家都很熟悉，是不是我们大部分的通讯其实走的都是 IP 协议，但是有时候你用的不是IP，你用的是ICMP，大家还记得吗？特别是调网络的时候，你要去访问一下服务器，看看网络是不是通。你用什么命令？ pin trace root 是不是？你用这种命令其实走的是什么协议？ ICM p 协议。所以福阳老师要告诉你，这套方法在生产中心可行不通，大部分企业的生产中心是禁止这个协议的，是不允许这个协议进行互通的。


也就是说，当你去聘一台服务器的时候，你拼的结果永远是什么？Deny，那这个时候你就会找网络工程师说，嗯，我的服务器网络没有打通，或者我的防火墙没有打开，请重新帮我打开防火墙。这个思路是完全错误的，当你要测，比如像 rest API 这种什么网络连接，你要测 FTP 网络连接的时候，绝对不要用拼，不要用 trace root 去验证我们的网络，去验证我们的通信应该用什么？应该用这个传输层的验证工具来验证我们的端口。
好，那说到传输层，其实有两种方式大家应该很熟悉，一种是TCP，一种是UDP。那我给大家考一个小问题，我们慕课大家当时在看的什么是点播？但是每个月我们的什么，我们的 7 位老师也会跟大家来一些直播，点播跟直播分别走的是哪一种协议？这个小问题大家有没有想出来这是什么？是两种不同的协议，直播要求什么？实质性很强，对吧？大家在直播的过程当中可能还要扣个 1234 这种互动，这种直播，这种什么很多的弹幕要能实时的显示出来，这个时候丢一些帧是没有关系的。做什么？哪个传输层协议 UDP 最小的延时实质性最强，同时网络链路质量最差的协议。当时我们点播应该怎么样？点播应该每个字、每句话都非常清晰。所以点播都走的是 TCP 协议，你可以卡顿一下，没有关系，但是我们要求点播的每个内容都能够完整的表达到用户这里，所以 TCB 和 UDB 是不同的协议。


同样的我们要测一个 TCP 的连接，怎么测很方便？ tell net 加上 IP 地址和端口。但是如果你要测点播的功能，你还是用TCP。如果你要测直播的时候，那你要换一个名令来用什么？用 n c n c 是 network connect，简称 n c，加上 IP 地址加端口，然后加一个杠。什么杠？ u 表示你是测 u d p NC 也可以测TCP。所以作为 Java 的架构师，其实你要了解怎么样去测试网络，不要用PIN，不要用 trace root，而用 tail net 和 NC 两个命令来真真正正的验证防火墙规则以及我们的网络连通性？好聊完了传输层，大家是不是感受到了有了 TCP 的这种什么三四握手，也有了 TCP 的这种质量保证和网络重传以及 UDP 的这种快速广播，对吧？实时通讯我们基本上已经实现了底层所有数据的传输了，那应用层是不是可以五花八门随意开发了？HTTP，FTP、SMTP、邮件服务、文件服务、应用服务可以随意开发。但是我要告诉大家，我们不管是 Java 还是什么还是Python，大部分的语言都会仍然遵循OSI，通过三层上面的三层来实现真正的应用通讯。


好，那我们就举个例子，比如说我们 rest for a p i 这个 rest of API 这个协议会说什么？我们所有的通讯要求有一个方法对不对？是什么？ get post put，对吧？patch，delete，head， option 等等这些方法，还有它特定的什么 status code、返回值？所有这些规范在哪一层？在应用层，这就是 rest API 的定义，但是当应用层定义完以后是不够的。


什么所有数据传输，你传输的不是一个对象，而是什么？而是一个序列化的内容。那这个时候你要把对象序列化，你可以序列化成json，也可以序列化成XMAIL，那这个时候序列化的那部分内容就是表示层，那如何把序列化的内容进行通讯呢？你用哪个协议啊？用了 HTTP 或者是 HTTPS 来实现，同时在 HTTP 上面你实现了什么？绘画的保持，这就是绘画层，所以一个 restful API 走了，这样三层。那大家可以考虑一下，比如说我用的是谷歌的GRPC，是不是也是这样？三层顶上是 g r p seed 应用层，中间是 PORTAL buffer，那底下是及 RPC 的 RPC 连接层也是这样。


三层，那我们再换一个思路，假设我们是消息队列，比如说是卡夫卡或者是什么 rapid MQ，那上层是不是我们的什么消息队列的 broker producer 跟 message 他们的应用层之间的通信，那中间是什么？中间是消息的持久化。比如像你把消息变成了JSON，变成了XMAIL，变成了averal，变成了thrift，或者是 PORTAL buffer 等等，这些都是什么持久化、序列化的方式？它们都是表示层，那底层的绘画层又是什么呢？绘画层比如我们的 rapid MQ 就是什么 AMQP 的协议，比如我们的卡夫卡，就是卡夫卡自研的卡夫卡协议。那底下的传输层分别对应什么？分别对应，比如像 9092 这样的卡夫卡的端口，通过这样的端口来实现什么最终传输层的稳定传输，绘画层能够进行绘画的保持和连接。在表示层我们能够进行序列化，在应用层最终能实现消息的传输、 API 的调用。


好，聊完了这个网络模型，大家是不是已经深刻理解到其实我们平时的开发时时刻刻都在做网络模型，那但是网络模型又该如何落地呢？它落地成什么？落地成这样的网络设备依然以 TCP IP 的五层结构，顶层是应用层的，它不做，但是它描述出来了，那底下才是它实现的四层。

[image](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/b3ff5dfd-1920-40fb-b7bd-41575e4e0a70/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TT7GW53F%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T231026Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIFZ1xOLS7A43Q4kz7Zg7iaPZ5U8vEhiCdIa4xm3BWzDGAiEA8RKtwY8F%2BFbG%2BMd7q58PPAgkerhG6rU8Lp7AJcbSbvwqiAQIxv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDFw%2BRE6L%2BtnuLNu1YircA8kaTXoj6yE0BZ0G8nagTRFoMFPOUjnfxv9h2X5Lj%2F%2FRsFnqQ9BbYMHLZ%2FL9kfEPQRuvHEt3oXGF3%2FR6SFpuSkul9RJRwYKdke%2FEd9XkC%2FKQTS76Xjrbr9TrjS3%2BR7EeDjD90a7O7QyAgImmy%2Fwkn9CkqG7OsAoBLamfpjC7KNN6bW8aBPYyFfp%2F5h9oUKIY1OK6ixph8w8t%2FRQfhc77M47%2BD0a4%2F3s7TZOAh9EcpA8MaPgjpxcdpBgmr28nSe5H3y6%2FUX7k3zO5RDyJErbYAIxhpZNnhWOpgfc3VS%2FIXFRjgKMf4v5RqBAzd9qvtqexf49ZIZ3vHQJDuYKozSzJSjn14tptrNa%2B4yvGGzV8olYDTyVIQtD4K%2BVUvnhZ66FnTontHYopXkLRUeSXlSxoh28G%2F6B9LgOvvVqS71rCCRyjgl5kHD1Z3ahiT4VRFxtCu9XMNQ2%2BFedWotlEtUjhzfxri4GpV2kSZXbct08%2BCfdzxfC1zQxI6%2BvLvWPOl0Ylz2jmYHbhdQF8afZRPu4mqucbUrRvkmjZ33cIG%2FC1%2Bd16ZZG4cfU7tq24vjk48IXpL2DDxuEjazMnZn49O3KNLOdJYJ3kexUKLRgv4USRRSZXxfowAaDXgAS7KKTPMP%2B2%2F9IGOqUBe8kjrJE3qS8iaeV3S6UEPIMSVyhAi04LDvvXnBTt1FxZbzWtmXwNafDol6HjhDR5f1AxXGTioPDd2OACqpY%2FkDeblp7SVNIKU31snCxCQr5FrWigtp9oNi2Do7JRvGz8FEo%2B6M2u%2FvgLykC0p%2BcF3aL%2BVOBdD8%2FV8Msr58Eh0e7t85EsEBPaiurdwgqaL4vMaAZA6PwQZmeGfQr%2Bk2w9sqQOnFHF&X-Amz-Signature=c00fa26d2eabfa77e78b4c098a613caec3391e4b0448c1a3a3df8326ef3ef20d&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

我们来看一看物理层主要是通过哪种设备来实现啊？网卡或者网桥等等直连工具等等信号加强工具来实现。那链路层，链路层主要是要实现一个拓扑结构，那这个时候主要在我们的生产中心，在我们的研发中心里面用的都是交换机。那三层网络层用什么？用路由器，路由器其实是什么？是连接一片网络和另外一片网络的桥梁。


我们大部分时候在一个企业内部，我们用什么？我们用的是这种 OSPF 的这种协议，就这种协议叫什么？叫最小生成树，跟我们以前学算法里面的背包原理，什么最短路径原理差不多，是找一条最短路径，从一个什么网络区域到另外一个网络区域，从一个网络设备到另外一个网络设备。
那但是如果你们企业实现了容灾，实际上单元化，这个时候你多机房之间是走什么协议啊？走的是外部网络协议， BGP 网络边界协议，那 BGP 协议能够很好的保证什么？我的网络的路由能够准确的找到我的对端的数据中心，同时还能实现什么跨数据中心的负载均衡？很多时候我们的什么，我们的压力达到CDN，再达到负载均衡器，这个时候我们可以把它横跨在多个数据中心、多个单元里面进行通讯，这都是 PGP 的功劳。


好，再上层的传输层是什么工具？比较夸张，那就是防火墙了，我们通常有很多道防火墙部署在不同的位置来实现传输层的安全，而在传输层以上就是我们的计算机了，我们的业务的，我们的应用系统，我们的代码部署，它实现了，绘画，它实现了表达，也实现了我们的应用的沟通和交流，所有这些都通过我们的 Java 代码来实现，或者其他语言的代码。那对于这些代码的安全支持哪一层是最关键的？当然是离他最近的传输层的防火墙了。好，下一节我们就来重点聊一聊防火墙。通常防火墙在业界有一个说法，就是什么防火墙？就是我们数据中心的二郎神，那就让我们来了解一下二郎神防火墙，大家敬请期待。

