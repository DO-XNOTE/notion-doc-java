---
title: 1-7+Dubbo协议解析过程
---

# 1-7+Dubbo协议解析过程

[image](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/ddd31026-dd11-427c-bbc9-4453f7b3c691/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RHX6VJEV%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T225856Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDGqYhwCmuFikK8fWP%2Fhrh0HzEJD8Ru5khE7JvzXuyNuQIhAKrBp%2BV4Xz7jcl0YPer9tdF59%2BTNPEmhLPVAq59Tj5cMKogECMb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1Igw4cify3P3qntrryW8q3AMJYTOYRiZD5YyiP0tOMTerez4qyzOOnNKX3IWDgv07ZBvHMcUR1eQne22UOSNKfrP4Jgw%2B%2BZsi4F%2FtgaF0yLbM9NN1UyJfKS2RRLwfN0ht8nscp67Cq7yd%2Ben5A8x9m6jJ%2FDhuYY%2BPK5AgOBAZmcNwQVxIoNN3NpGYvXj7DAkBLiTqnblrgYqL3o3Hl%2BApI9m3TrWNrIQ1DKSDN8iaC%2FdZQt24OlQzQsrlSy3b6xCkWnVSkQJjYnDUoDAwvM9dL1GCBx3fay5MVJA7OTPdQs1yL4otvw5AcvrA34UHps7BHKvux%2F1U%2BAcqsyWuOrs%2FvKCbAUXgA0jCigfMUF2o3XO%2FLNqbPTBmfbsy08K4NPyQfAFyxXEkzG9zzthNxyZLsFZa0FbkC%2BqhkDBDymjMdUTsWaGNya5RNtbGr8tr5aomQACP1DGwLOeGBENgjRblKcvhud1PM%2B2MJG8%2FpfJI6peTqKZ5e6nGE8yuoUlexFr%2FXBQS3jPpMVGvlaUTSDoKPeWwyAdSJk5DAMw4sCDYNDR4YdM2Lym2mIzi8TCSDjywILGe1ZNZLQLLUKOfVEUOWUNFk2XbOnEPHEXTwHgxPUDNbABTkbTj3E0MLQwohatB2FQJYH5XTJJghhYxkTCGu%2F%2FSBjqkAaKYGfduQx56tdrC9TLQxvQalFSOFG%2FzDtTS1eYMcjq%2B3fe4AFlKluzMSRda%2FiBaWxU%2FnSSBX5RRuSCPQODdnkUbipMV6%2BcZ0M5MvU5Fr5lb1uk%2BbVzLmEGlSZPUmBgyxLtS1ZsvcIh8lwww%2B9qtXh45VUrsLEgXkikiQmkoBFYtI%2B6TOm3JGuSyTGTNuTm8JPzZEPZFSDhRQ5CTnZZ1veyFp5eU&X-Amz-Signature=1745d854ae3bc0c2db2382da434380754912600aeabdc41342bff5d05e0b2409&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

前面我们了解了Dubbo的Cluster组件，这一节让我们学习Dubbo的一个重要环节Protocal。

**Dubbo有哪些底层协议**

同学们以为Dubbo只有一个RPC协议吗？非也，既然是阿里巴巴出品的开源项目，那自然秉承了“包罗万象”的一贯传统。Dubbo的底层有支持多达9种通信协议，并且他们都有各自的适用场景。我们快速的一扫而过：

Dubbo本尊 这也是官方首推的底层通信协议，稍后的章节我们再深入介绍

RMI Java界的老法师可能会对RMI比较熟悉，没错，这个就是JDK中“java.rmi”包下的实现，底层采用阻塞式（同步传输）的短连接+JDK中标准的二进制序列化。适用场景 参数数据包大小不一，服务提供者和服务消费者的个数相近

Hessian 用于集成Hessian的服务，基于HTTP短连接，采用Servlet向外暴露服务适用场景 参数数据包较大，服务提供者的数量远多于消费者数量

HTTP 最简单的基于HTTP表单的协议适用场景 可以使用浏览器直接查看，适用于需要同时给后台应用程序以及浏览器提供服务的场景（很多其他协议无法通过浏览器直接发起调用）

WebService 基于大名鼎鼎的Apache CXF，使用基于SOAP的序列化技术适用场景 比如公司内部的系统是由多种不同语言构成的，那么这个场景就比较适合采用WebService协议，WebService通常使用在系统集成和跨语言调用场景中

REST 基于标准的Java REST API（JAX-RS 2.0）实现的REST风格调用，Dubbo花了大力气在这部分的实现上面，它的使用风格和原生Spring MVC类似。但它不是今天的主角，同学们如果感兴趣的话可以自己花点时间去阅读REST协议的源码

杂七杂八的协议 Dubbo还支持基于Thrift，Memcached和Redis的协议，不过相信大家在职业生涯中应该是用不到的

**主角登场-Dubbo协议**

**Dubbo协议的特性和性能**

我们先来看一看Dubbo协议的特性：

在官方的测试报告中，由于Dubbo将底层的通信框架从mina换成了Netty，大大提升了稳定性，主要体现在JVM Old区对象的数量减少了很多，因此Full GC的触发频率大幅减少。

插播一条广告 上面提到了JVM，所以这里多说两句。JVM的知识历来都是面试中的常见问题，大家在面试前不能光靠背题目来应付，面对有经验的面试官来说（比如我，骄傲脸.jpg）几句话就能被问出来。这里建议大家手把手去做一些JVM调优的测试，构造一些极端场景，再用批量测试数据数据跑一遍，看看这些参数的微妙作用，再把JVM的dump文件拿出来跑出分析结果。到这一步你基本就能吊打80%的面试官了。学知识光看书是没用的，必须动手去做。

**Dubbo协议的适用场景**

尺有所短寸有所长，Dubbo并不是万能药，我们在使用它之前务必要知道它的适用场景：

适用场景 传入传出参数数据包较小（建议小于100K），但是并发量高的场景。简单来说就是短平快，QPS/TPS高但是数据量小的情况

不适场景 尽量不要用Dubbo协议传输大数据包（比如大文件、视频、超大字符串等），这类场景建议使用上面介绍过的其他协议栈

Dubbo协议的调用流程

接下来我们通过一幅图，看一下Dubbo协议的工作流程

这次我们换个姿势，采用从中间向两边展开的方式解读这个协议工作流程

**Transporter**

大家注意看图片底部最中间的Transporter，这个是底层网络传输组件，目前Dubbo支持Mina和Netty。大家可能对Netty比较熟悉，但并没有接触过Mina。在Dubbo的2.0版本以后已经从Mina全面替换为Netty，基于Netty的传输层在稳定性和性能上都要更好一些。

**Header & Body**

接下来我们看图中的绿色部分，就是Header和Body，这部分是Dubbo定义的私有RPC协议中的数据格式部分，它是一个变长协议，由定长的Header和不定长的Body组成。

Header

上面是Header的结构，图片中的数字代表Header中Bit位置，下面的文字表示这段字节所携带的信息，Header总长度为16字节。其中Magic High=0xda，Magic Low=0xbb，标识了这是个Dubbo协议。

后面紧跟着16-23比特位带有两个信息：当前请求的类型以及序列化的方式。其中高四位表示当前请求的Request flag（有三种类型：REQUEST, TWOWAY和EVENT），低四位表示序列化的方式，Dubbo有四种序列化方式，分别对应Dubbo，FastJson，Hessian2和Java原生序列化。接下来24-31位是响应报文才有的信息，作为Request报文并不包含这部分信息。其中定义了详情请求的状态，比如OK，BAD_RESPONSE，SERVER_TIMEOUT。注意这些Status Code可不是HTTP Status，而是Dubbo自定义的状态。最后两个部分分别对应Request ID（唯一请求ID）和经过序列化后的Body内容的长度。

Body

这部分是Dubbo协议中不定长的部分，在传输之前会经过序列化处理，对于一个请求包来说，主要包含三部分的信息：

协议版本 Dubbo当前的版本

寻址信息 目标服务的名称，服务版本，方法名，方法签名类型

数据 方法参数值，附件形式的数据等

**Client，Server和ThreadPool**

Client对应调用发起方，Server对应服务提供方。

Client 在发起调用之前会将整个消息进行序列化，组装成上面的Header+Body的变长协议格式

Server 根据Header里标识的序列化方式，对Body中的内容进行反序列化

ThreadPool 响应服务调用请求的线程池，可以选择配置Fixed或Cached Thread Pool

**Dispatcher线程派发模型**

Dispatcher用来创建具有线程派发能力的ChannelHandler，将来访Request派发到线程池或当前IO线程。我们可以给Dispatcher配置5种派发策略

**协议的约束**

既然Dubbo协议应用了序列化和反序列化技术，那么对我们数据传输有几个约束条件：

Serializable 参数和返回值必须实现Serializable接口，否则在调用的时候会抛出无法序列化/反序列化的异常

使用JDK原生类 比如Map、Date、List、Number等一系列接口，我们不能在返回值和参数中使用自己创建的实现类，只能使用JDK原生的接口实现类。

**服务的同步和异步调用**

Dubbo支持同步和异步两种调用方式，整个链路流程非常复杂，我们只抓重点看下两个调用模式的不同

异步调用 异步调用还可细分为“有返回值”的异步调用和“无返回值”的异步调用。所谓“无返回值”异步调用是指服务消费方只管调用，但不关心调用结果，此时 Dubbo 会直接返回一个空的 RpcResult。若要使用异步特性，需要服务消费方手动进行配置。

同步调用 这是默认情况下Dubbo所采用的调用方式，调用方等待服务提供者返回处理结果

**小结**

这一小节我们了解了Dubbo协议的工作流程，下一小节我带大家去搭建一个服务消费者，完成整个Dubbo的调用链路。

注：本节内容参考了Apache Dubbo官方网站，配图来自Apache公开文档




