---
title: 1-6 微服务的拆分规范和原则
---

# 1-6 微服务的拆分规范和原则

[image](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/ba2b43fd-7048-4edb-8593-8de329071d41/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZLGIZIOB%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T225516Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDsT15l7Z7B1B%2BJ4Cwnqf2xX6q%2B9dTc3pR8f751r0rJrgIhAKOSuU83OMHZp46MeWvVw9NL%2BUnKXWFGIEz32TpcC72rKogECMb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1Igz%2Fkn5SRmIzvDCGTOwq3APjHn8iAjrbHeOj65V8cqi%2FqUCyt4jlWJN1W8nH9G9J8ipT4EAJ4tdSi30YdOxyK%2F5oJRUj9H%2Ftg%2BCMZS2TsJ4QYCacqDWcPXGvjWlCLPWuome50p11xOLuy3PO2xzNTBcgNpfXbMlElauTozySw6MyKc4zWDwRAFKfCvXX%2FUfCp7R%2FyKOyQ7ZCOVdIltWnIkwk6gtmK38EadABzTlhK3ajuqZ4HKqFYk%2FqQCORmLtAefKESLan%2FmsyekngyJim1VLGfq3qVaMWn69TaOxG61Ug4r2w%2FHe16rP1FyVUqxHnTiPZsYN0CRwP2JN6yjI%2BIJ6Og5Tn0rf5YHKgh%2BDWNITDHkXxbNHrMj5JKExPRulk75MxTUVV%2BfIIcAGYyOVMVXAPkAPk6%2B%2FVT3pu9cW8DPM1YkfnzsgmqF22vtRD9gnvFJe4hAHW8qfFraABIlPEbnCY0KCCg%2FBzWX%2BADvG2Me5u8PSC%2FLF0Lnz1O8UjbyN6di8O8P1oLfDrHSDmP1PwfGXXNwr8PicOc3LfLWCWUfH5leh9KoydHyR9jvyYUUslO%2FiqjvZwJfar8OQe7g4cRs4IGxhEaKiTIx3iT%2FIjFWp71QI3AHYgz9XDYx2GBw7rvfShuH0HF8ZTrnf%2FADDyuv%2FSBjqkAb%2Fwm%2FYK45%2Frdnkh0uEdZSvtElSnN5XiVpOwsB%2FhNmVIBnzwzUCc0cvHSiNwxnXOvKCfsXkZWkAGvYWzHRLcvKkDcidtw%2FbjaQEr2BFJ2o7ab1LnWjGwXNlajlPY%2BUMMH8IJWunCLCyBNsgkDjgccJtzK8vu5EO24aGN%2B3d35H147pVaFrhPIvDcTrwpDTeUZ9cIra3fHIIp7hPPMa2TEcdnohAk&X-Amz-Signature=e078c81c1a973c720f08316b5ce5bbcf7e424ca8c1389d61654292500d75fb20&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

**1-5 微服务的拆分规范和原则**

前面我们了解了什么是微服务和为什么需要做微服务架构（What & Why），这一节我们就来探讨如何做微服务架构的拆分（How）

微服务拆分没有一个绝对正确的方案，服务拆分的粒度完全要根据业务场景来规划，而随着业务的发展，原先的架构方案也需要做调整。既然没有标准答案，那我们就使出“乱拳打死老师傅”的招数，想怎么拆怎么拆好了？且慢且慢，这不就成了暴力拆迁了吗，现在“扫黑除恶”正当头，我们可不能这么干。老师这里总结了几个服务拆分的心法秘籍，同学们可以照着这个路子去思考服务拆分的粒度，我行走江湖就靠着这套武功心法。

**拆迁方案**

这辈子当不成拆迁户的同学们，你们也别灰心，咱房子拆不成，微服务还是可以拆一拆的。说到拆迁，咱就得有一套方式方法，不能暴力拆迁。不妨看一看老师一般怎么规划拆迁方案

**压力模型拆分**

压力模型简单来说就是用户访问量，我们要识别出某些超高并发量的业务，尽可能把这部分业务独立拆分出来。这么做的原因非常简单，高并发业务相当于前线战场，战况非常激烈，如果我方部署兵力不够（服务器资源），而敌方攻势又过于猛烈（剁手族们疯狂的流量），万一战线失手了服务器压力抵挡不住，我们不希望让这种情况影响到其他用户场景。

我这里举两个例子：

秒杀 秒杀是一个典型的低频突发流量的场景，参加秒杀的商品的数量一般不会很多，但是在秒杀开始的时候，尤其是对爆款商品来说（比如新发布的苹果手机），会有一个很明显的突发流量

商品详情页 商品详情页毫无疑问是电商场景中并发量最大的业务，一笔成功达成的订单背后，可能会调用几十次商品详情页接口（同学们买东西都要货比三家么不是）

我在做具体规划的时候，会尽量把压力模型拆解为三个维度

1）高频高并发场景 比如商品详情页，它既是一个高频场景（时时刻刻都会发生），同时也是高并发的场景（QPS - Query per seconds极高）

2）低频突发流量场景 比如前面提到的秒杀，它并不是高频场景（偶尔发生），但是它会产生突发流量。再跟大家举一个例子，那就是“商品发布”，对新零售业务来说，当开设一个线下大型卖场以后，需要将所有库存商品一键上架，这里的商品总数是个非常庞大的数字（几十万+），瞬间就可以打出很高的QPS

3）低频流量场景 这一类多为后台运营团队的服务接口，比如商品图文编辑，添加新的优惠计算规则，上架新商品。它发生的频率比较低，而且也不会造成很高的并发量。

通常我们建议将高频高并发的场景隔离出来，单独作为一个微服务模块，典型的就是商品详情页的后台服务。对低频突发流量的场景，如果条件允许也可以剥离出来独立组成模块，如果必须和其他业务包在一个微服务下，那一定要做好流控措施（[最典型的就是削峰策略](/05f59d36344e486c9889853acfc258fe)），而且还要考虑到异常情况下的补偿机制。对于低频流量场景，我们根据业务模型切分就好了（后面会讲到）。

**业务模型拆分**

业务模型拆分的维度有很多，我们在实际项目中应该综合各个不同维度做考量。我这里主要从主链路、领域模型和用户群体三个维度来讲一下

**主链路拆分**

在电商领域“主链路”是一个很重要的业务链条，它是指用户完成下单场景所必须经过的场景。按照我们平时买买买的剁手经验，可以识别出很多核心主链路，比如商品搜索->商品详情页->购物车模块->订单结算->支付业务，这是就是一条最简单的主链路。如果这是一场战斗的话，那么主链路就是这场战斗的正面战场，我们必须力保主链路不失守。

电商领域背后还有很多隐藏的核心主链路，比如下单之前的营销优惠结算，它会影响订单的最终价格；再比如用户地址模块，它会影响下单前的配送地址选择。如果这两个模块出了问题，大部分用户恐怕都要放弃下单了。试想，双十一我们添加了一揽子购物车，结果结算的时候发现所有优惠组合都失效了，或者是无法选择配送地址，那也只好放弃了。

各位亲，这里建议将核心主链路拆分，有以下几个目的：

1）异常容错 为主链路建立层次化的降级策略（多级降级），以及合理的熔断策略，这部分我们将在Hystrix服务容错阶段的课程中详细解释

2）调配资源 主链路通常来讲都是高频场景，自然需要更多的计算资源，最主要的体现就是集群里分配的虚机数量多。举个例子，就说淘系中台业务中单品营销优惠微服务，在平日非大促阶段（非双11扩容场景）一个服务后台都有接近一万台虚机，一到了发布窗口就要通宵达旦做发布。将主链路服务单独隔离出来，这样有利于根据需要指定资源计划（比如双11阶段为每个主链路服务拟定不同的扩容计划）

3）服务隔离 主链路是主打输出的C位，把主链路与其他打辅助的业务服务隔离开来，避免边缘服务的异常情况影响到主链路。

**领域模型拆分**

领域驱动设计DDD（Domain-Driven Design 领域驱动设计）不是一个新概念，但老外们有个毛病，做什么事情特别喜欢提炼方法论，本来一个非常简单的概念，愣是被吹到神乎其神高深莫测。

其实领域模型是一个很简单的概念，抛掉繁文缛节的方法论，我们一样可以做好领域模型拆分。我举一个例子大家就明白了。阿里集团推出了一套大中台战略，将集团内部的公共领域服务从各个事业部中剥离出来，整合成了一个“集团级别”的大型中台业务。比如说IC订单系统，淘系商品服务，UMP营销优惠服务，汇金平台，用户账号系统等等。

从上面这个例子中我们可以看出，所谓领域模型，其实就是一套各司其职的服务集合。这里涉及到领域和合并和分拆。领域合并的例子就是淘系的营销优惠服务，曾经天猫和淘宝各有一套营销服务，如果不考虑底层技术，从业务层面来说它们做的事情是一样的，都属于营销优惠计算的领域范围，因此后面两条技术线整合成了一套UMP营销优惠服务。领域拆分的例子就太多了，我们做微服务规划的时候要确保各个领域之间有清晰的界限，比如商品服务，和订单服务，尽管他们之间有交集（都围绕商品主数据），但是毕竟是服务于不同领域（商品域和订单域），所以我们要将两者拆分成独立的服务。

**用户群体拆分**

根据用户群体做拆分，我们首先要了解自己的系统业务里有哪些用户，比如说电商领域，我们有2C的小卖家，也有2B的大客户，在集团内部有运营、采购、还有客服小二等等。对每个不同的用户群体来说，即便是相同的业务领域，也有该群体其独有的业务场景。

用户群体相当于一个二级域，我们建议先根据主链路和领域模型做一级域的拆分，再结合具体的业务分析，看是否需要在用户领域方向上做更细粒度的拆分。

**前后台业务分离**

同学们如果下了班当过顺丰车主的话，就会知道网约车业务不仅有一个乘客端app，也有一个司机端app。电商领域也是一样的，我们通过手淘app买买买（前台业务场景），商家通过后台的业务系统管理商品信息（后台业务场景）。在实际项目中通常也会将前台业务和后台业务做一个隔离，这也符合高频业务（前台）和低频业务（后台）的隔离策略。

**小结**

这一节跟大家介绍了微服务拆分的几个维度，在后面的章节里，我会带大家走进阿里的战略核心业务的微服务化过程，看一看这些拆分规范如何应用到具体的业务场景中。

[image](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/f074e18b-551e-4851-af65-d1f77d71bfea/Untitled_%281%29.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZLGIZIOB%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T225517Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDsT15l7Z7B1B%2BJ4Cwnqf2xX6q%2B9dTc3pR8f751r0rJrgIhAKOSuU83OMHZp46MeWvVw9NL%2BUnKXWFGIEz32TpcC72rKogECMb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1Igz%2Fkn5SRmIzvDCGTOwq3APjHn8iAjrbHeOj65V8cqi%2FqUCyt4jlWJN1W8nH9G9J8ipT4EAJ4tdSi30YdOxyK%2F5oJRUj9H%2Ftg%2BCMZS2TsJ4QYCacqDWcPXGvjWlCLPWuome50p11xOLuy3PO2xzNTBcgNpfXbMlElauTozySw6MyKc4zWDwRAFKfCvXX%2FUfCp7R%2FyKOyQ7ZCOVdIltWnIkwk6gtmK38EadABzTlhK3ajuqZ4HKqFYk%2FqQCORmLtAefKESLan%2FmsyekngyJim1VLGfq3qVaMWn69TaOxG61Ug4r2w%2FHe16rP1FyVUqxHnTiPZsYN0CRwP2JN6yjI%2BIJ6Og5Tn0rf5YHKgh%2BDWNITDHkXxbNHrMj5JKExPRulk75MxTUVV%2BfIIcAGYyOVMVXAPkAPk6%2B%2FVT3pu9cW8DPM1YkfnzsgmqF22vtRD9gnvFJe4hAHW8qfFraABIlPEbnCY0KCCg%2FBzWX%2BADvG2Me5u8PSC%2FLF0Lnz1O8UjbyN6di8O8P1oLfDrHSDmP1PwfGXXNwr8PicOc3LfLWCWUfH5leh9KoydHyR9jvyYUUslO%2FiqjvZwJfar8OQe7g4cRs4IGxhEaKiTIx3iT%2FIjFWp71QI3AHYgz9XDYx2GBw7rvfShuH0HF8ZTrnf%2FADDyuv%2FSBjqkAb%2Fwm%2FYK45%2Frdnkh0uEdZSvtElSnN5XiVpOwsB%2FhNmVIBnzwzUCc0cvHSiNwxnXOvKCfsXkZWkAGvYWzHRLcvKkDcidtw%2FbjaQEr2BFJ2o7ab1LnWjGwXNlajlPY%2BUMMH8IJWunCLCyBNsgkDjgccJtzK8vu5EO24aGN%2B3d35H147pVaFrhPIvDcTrwpDTeUZ9cIra3fHIIp7hPPMa2TEcdnohAk&X-Amz-Signature=00bc7a258fefdf9d81932c51f5b2826a9690b7f7bdd764b6dd6c8e69d94f2ebe&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)




