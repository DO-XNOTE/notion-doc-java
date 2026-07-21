---
title: 1-14+阿里系王牌中间件HSF
---

# 1-14+阿里系王牌中间件HSF

**1-14 阿里系王牌中间件HSF**

上一节我们看了Dubbo的源码，这一小节我们来了解下另一个阿里出品的RPC框架，那就是风靡整个集团的HSF。这里我们不谈HSF中过于细节的技术方案，主要想跟大家聊聊开源、技术选型那些事儿。

**旧账总翻不完**

在介绍HSF之前，我们先来翻一下Dubbo的旧账，聊一聊Dubbo的市场热度。

下面是应用Dubbo框架的代表公司，清一色都是鼎鼎大名的公司

[image](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/77cd0f1f-9667-4338-8a5d-2c745d2a3f7e/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663Q4RJ2GJ%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T225902Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCzZkMvZDFIVkZ9lMb1BWokB%2F%2Bhpe7oEmZSxoqM7nZ4rAIhALTOtqR10aDiHrpdrOM62GCzYBHxgIxU3iqLFt%2BtirEKKogECMb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgyGA5NXFcb5n2TnCjUq3AMC4K2Dm06jWJ6v5hAGYf5rDfIW9ThURqJnTS%2FFOGGfSuS0Ksd%2Fnw9BLXfK3j5p1FgGDvB7q3OwwUHtBnq0s4xW5WWdVcTGtxmDR%2BcSwjWt7TbifctJSoXoG5Sp5SUClVCkL6FHrs7I5Hj1ytulmtodQNpTHcSjUysXFGEZdcwxhiDKrjVkfSsIT%2FO9IrI%2FXL2Qr6u%2FrCS8e0a7ZVRZxCoa3VWcPcoq9leqprf7zACPmcdy4M07h72IZnv0IZLuyWb9jVt0rAe%2B2E2f6vkZn3VMSdymHQzRoAdJw77gM3IsQx%2B7y4N8auXhoBa7%2F8sdjsErJyZAKWdWGWq2ZOddBU23IGGeGvsTFuZ%2F1%2BMAqYPliPtv1CGfYi%2Btw4cftiKYd4QlVuOEEmpEmybn0a3YIwBe9gi0ssOZzJgLm4E7AmlTIIuwLtdhw%2BMCGPJLffJeZ14mZ8hBuw6%2FB1%2FCbKWnsx6EeicjEXJwOCzoUi%2B8PbIv4%2FloGRKdyM294VDjeWukhWLTMUKQbOh2NaVswztM1zTtV7eCKTzgogVkM7dvXfBQSX%2BDRYWZybwHHcwfdLd1Y7aAtKqnDJqhje54M5dQLfR2iZLsbnHuEAJBFa7NP3Zoh5tO2PQdGipLLSYZPDCStv%2FSBjqkAfL1sRNVmqU1hZUb00OXlPmDiwk4D4Qnjzhb596XKB6ksMT%2BehmuzOrb%2FpAlaWfSxsoysJPxL7wUpC%2BZtQnUMAzZmlGRukmh2QmoZFG5N2duNt7U4Hz6oEtHsBC6yQyFvNC3HfvkLutInpSfGAbQL%2BWlowI3JADzcV9XtDmUAJxO44fpAxNfyHak43ojEScR%2B4GIgFYvcN102dwM7ddH0KWbDoM3&X-Amz-Signature=59faf55f4a2f8dc84f4af4aaf75de99497ada9f2ea0cf92741445ffb017d2b71&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

同学们有没有看出哪里有点不对劲？这上面大部分公司都是传统企业，放眼国内，除了阿里和滴滴以外没看到一二线的互联网公司，而且据我了解有几家叫得上名的互联网公司尽管在用Dubbo，但应用范围不大，并没有在公司上下游系统全面铺开。

国内的情况大家心里有数了，然后我们放眼国外市场，算了还是不要放眼了，感觉压根没有哪家知名外企使用Dubbo的。

说里面的原因可就多了。其实大部分一二线互联网公司技术实力都比较厉害，轮子也造的不少，这类大厂大多都有自己的一套服务治理框架，或者基于开源项目做了二次开发。Dubbo的应用主要还是集中在国内市场，在国外公司的应用非常少，国外大行其道的还是Spring Cloud，以及grpc等国外大厂研发的RPC框架。

**Dubbo的接班人**

同学们不会以为阿里系的应用系统清一色都用的Dubbo吧？NoNoNo，至少我在里面工作期间还从来没有对接过使用Dubbo的业务方。真正在集团大行其道的RPC框架另有其人，那就是这一节的主角HSF（High Speed Framework），我们可以叫它“好舒服”。

说到HSF的应用范围，你可以认为是整个阿里系都在用它。HSF是由淘宝平台研发的，连包名都是”com.taobao“开头，大家不要以为它只在淘宝平台使用，HSF在整个淘系链路、天猫、集团中台服务以及各个独立事业部中已经全面铺开，用一统江湖形容绝不为过。在未来相当长的一段时间里，HSF还会是阿里系占绝对主导地位的RPC方案。

**HSF印象**

我就从个人使用HSF的经历来聊聊对这个框架的体验和感受吧。

**使用风格**

```java
<hsf:consumer

		id="product"
		
		interface="com.imooc.training.ProductService"
		
		version="1.0.0"
		
		group="testHSFGroup"

>
```

上面这段是基于HSF标签的配置文件，创建了一个Consumer。这里面定义了接口类名，版本号和group三个信息，HSF 将根据 interface + version + group 查询并订阅所需服务。

这里面的version其实是个蛮有用的字段，也会随着服务注册同步到注册中心。我经常需要和共享事业部的中台团队做对接，他们在同一时间可能会对接来自于多个业务方的需求，但是日常环境就只有一套数据库（阿里系一般只有日常和生产两套数据库，预发环境则是直接连接生产库），所有开发人员都会在本地启动服务，然后通过配置不同的version来区别不同的代码分支。

[比如营销大中台给天猫项目暴露的接口版本是1.0.1.TM](http://xn--1-kq6as6pqb792boa33d226dghf6mb1zbpy6a3nuy0cl1rosbq62ej6tpg7engjewg.0.1.tm/)，对接飞猪的是1.0.1.FZ，这样一来不同的业务方就可以在Consumer端指定一个version，HSF会保证Consumer的调用请求只会由对应版本的Producer来处理。

**技术基本面**

HSF的底层技术栈和Dubbo差别不大，也是采用Netty作为网络通信层，同时采用Hession（默认）或JDK标准序列化方式。

注册中心 不同于Eureka的服务发现方式（客户端主动获取），HSF中注册中心与服务节点建立长连接，并通过心跳检测的方式判断节点的运行状态，在某个节点变为不可用的时候，配置服务器会更新服务提供者列表（剔除不可用节点），并且主动推送到服务调用者在生产环境中不会使用一台配置服务器连接所有节点，而是会搭建多个配置服务器做负载均衡，保证变更可以尽快推送到所有节点

地址服务器 为服务提供者和服务调用者提供所有注册中心的地址，所以每台机器在向注册中心发起服务注册之前，先要访问地址服务器获取注册中心的地址

除此之外，通常HSF还会集成Diamond（配置管理）之类的中间件，因此在部署结构上，确实比开源的Dubbo组件要复杂很多。所以说，HSF的高性能和高可用，很大程度上是建立在阿里系强大的运维能力之上的，如果这套架构用在其他公司自己运维的话，未必可以玩转这套复杂玩法。

目前HSF可以通过阿里云的企业级分布式应用服务EDAS来提供接入服务，EDAS可以同时支持HSF、Dubbo和Spring Cloud三套微服务框架。借助云服务可以降低运维成本。

**久经考验**

说HSF久经考验一点不夸张，它撑起了整个淘系链路的巨大流量，也经历了双11洪峰流量的大考验。要知道即便是国外一线互联网公司的核心产品也很难有机会面对这种级别的流量冲击，毕竟双11这类中国特色的业务场景放在国外压根玩不转，因为歪果仁根本就算不清楚这么多复杂的优惠券和营销逻辑啊。

**开源路漫漫其修远兮**

淘系过去长期的实践经验已经说明了事实，在稳定性方面，HSF可谓是RPC框架的一枝独秀，可是既然HSF那么好，我何不放弃Dubbo转而使用HSF呢？很多同学可能也会感到纳闷，为什么阿里系内部都在使用HSF，而被Apache列为顶级项目的却是Dubbo呢？这就要说到开源项目的一些隐形门槛了。

首先从实现的角度来说Dubbo更加轻量级，而HSF深度融入了整个淘系链路，因此也依赖了很多阿里系开源或暂未开源的内部项目。也就是说，如果你使用HSF的话，不可避免的要拖家带口的使用一些阿里系的技术。把HSF单独抽出来做开源化也是一件不小的工程，就拿Apache的顶级项目来说，就要经过提案、孵化和毕业三个阶段

提案 这个阶段还是遵循“导师制”，就是说需要委员会的三个大魔导师联合提名，成功后Apache会组建委员会为这个项目保驾护航

孵化 孵化也不仅仅是开源项目代码这么简单，还包括开源社区的培养，布道师们要去开疆扩土，这不单是说项目写得好就可以的，还考验了项目团队或项目发起人的沟通和宣传能力

毕业 当孵化接近成熟了，并且Apache委员会的大部分导师都同意以后，项目就宣告毕业了，也就成为了Apach的正式开源项目

**Spring Cloud、Dubbo、HSF三选一？**

**HSF吐槽大会**

目前网络上关于HSF的资料少之又少，也没有详尽的文档，更谈不上构建学习体系。这就要吐槽阿里内部的文档建设工作了，集团里一众的中间件都是只管开发不管写文档的状态。开发迭代速度那是真快，就如同那脱缰的野狗一样，但是文档要么年久失修要么压根就没得可修。每次碰到问题在内网根本搜不到对应的文档，只能辗转找到负责开发的团队，或者请部门里的老法师给开个眼，非常耽误时间和精力。

Dubbo因为有Apache在开源项目孵化阶段保驾护航，所以文档化做的非常好。但那些淘系内部的各类王牌中间件就是另一番情况了，文档建设工作非常滞后。其实这也是大部分技术人员的天性，只顾闷头做出牛B的项目，顾不上写文档，所以别人还是不知道这个项目的牛B之处

如果打算使用HSF的话，强烈建议使用云平台的方式，不要自己构建整套运维体系。

**Dubbo**

比起HSF来说，Dubbo在文档建设上做的非常好，而且独立运维起来难度也不大。但是就像之前提到的，Dubbo只是一个RPC框架，只关注服务治理这个方面的东西。但是构建微服务远不止服务治理这一项内容，如果你想体验自己组装电脑的乐趣，可以用Dubbo再加上一大堆自选组件来构建你的微服务。但是如果你想直接买一个一体机，你可能更需要Spring Cloud这种全家桶。

**Spring Cloud**

和HSF以及Dubbo比较，社区支持、文档化和组件丰富程度都处于完全压倒性的优势，还想啥呢？I WANT YOU！！！

**小结**

这一小节我们了解了阿里系的主流RPC方案HSF，又聊了些开源项目的话题。大家就记着一点就好：Spring Cloud是目前微服务领域集大成者。

