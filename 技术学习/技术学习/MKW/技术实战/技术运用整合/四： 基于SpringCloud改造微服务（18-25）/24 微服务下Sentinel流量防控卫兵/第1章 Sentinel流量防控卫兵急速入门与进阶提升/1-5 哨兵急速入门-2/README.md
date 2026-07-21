---
title: 1-5 哨兵急速入门-2
---

# 1-5 哨兵急速入门-2

[image](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/f3d7e592-2cce-4990-81e0-93bd71dcb238/SCR-20240722-phzk.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666AFIKAST%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T225828Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCAKV0RaMbQ11Do4K%2BqFtQJp9956Fu596KhFPItCZ4wkwIhAIL9iQgl26w5qP6U7b16RcfxKxV9%2BW53kg4tz9DvxrGTKogECMb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgyEhg195pRpsBEz%2B%2F0q3ANqJnyF8wgZsSp6jHpfeUTqqu32AjP%2BZ9Nb40JWrg3Fc8xCcZBrdeyVkE3L9xcCRr4Ng%2BfcNO2qTsO1nCknwITfdbXLZFxknQ5CJ%2FZ7gtRj79GfvFOhYtPaCSIsUhHRweJFF%2FmsFX8AzVwEFrrJ%2B8WVauUgU11XwFcGhX%2FAlaiASAX2sdQfqyel7VSaeoTe1Iz1Al0d6vdc8LsOJcl73mYMNdXAMl8zafADy1%2BnBZMPJGCU4YxLAYymcyTyOUFiUhJTOOpQ3MavjBcRfC2OXFVMfLqfDPoUpD1jpEUaRy4nevstx7pl2lMrZ2FBLOvHE2S5aiSL4bcClt3AUXtt%2FNvhjdAAVWMpKZHXXRORE6og86RmXW1W3JsZxeKlt%2B9DwSKf1%2Fsc1BwcI33BVg69iFFO5gYizdwXH3loLlbhguX4eHiS569U05h9py2%2BipNRTiChCWW14qT319BKUFhQIlj5LqtgiEliUx12ZvptNFBsoIe0y7j8EK4Mqx8VxasKdJl7EhHpu3Fl1zx9o3s%2BkC3Poyrne2WUudDO3WkI1HCzCrfhjReijDGMV85fav6vAKXErFES37i3pbpU7QlLE%2BNtL%2FrOxTjVXH9%2F7CHkuVcp4dXBlrIlxC3H3mbsQDDbt%2F%2FSBjqkAUHpKEZ%2BPhwKe%2FNTmdsWUdxwRxtjkoYLiaTAoXNMuQYA03vYLyisI7UsL7DUQd%2FrketadlBYGBZVhn4%2BY8M37B0EJMxHf%2BqfzHIDzBuZYhon0H2Su7dPauUBU1QfroYzVINhHHA5wW81n1%2FoQC0lmJefZujnGOoDzwsb2Mk%2BF7geoAmayvF3gY%2Fj1jjFBYR6eT8fCodv4YUVkbZ5OAVSET5ycncZ&X-Amz-Signature=d6f4edc514a8e500b5312e7b7921577c3b134c845ddfc884db31f73a69c74f41&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

事情把依赖包引进来以后，接下来我们可以去写一个 demo 就叫做 hello word 写一个 hello word 的小程序，那我们把它最大化来。首先在这里老师也写一个主函数，因为官网上写的主函数我们在这里也搞一个。第一步是要引入对应的 home 就是依赖。然后第二步第二步叫做定义资源，第三步我们叫做定义规则，第四步叫做什么查看结果。第五步就是什么叫做就是 sentence dashboard 其实你把这五步完整的搞定，那才证明你真正的去了解了这个哨兵。当然我们在这里面只做前四步。


第五步等我们后面学习的时候，我们再详细说好。首先这个资源怎么去定义？现在老师按照官网的这个 demo 你看官网怎么去做的，官网写的是一个 well 循环对吧，他是写一个 well 的一个死循环，那我们可以在这里可以去做一下。在这里老师就把代码敲一下，帮小伙伴们更深入去理解。有些时候你必须要更深入的去敲代码，去对这个东西进行仔细的分析，你才能掌握这个哨兵。如果说我直接把代码 copy 过来，那你可能就没有那种感觉了。


然后在 sentence 里边有一个就是在哨兵里边有一个非常非常关键的核心类叫做 entry 这个 entry 是做什么事情的？注意，它不是我们 security entry 也不是我们 Java YouTube map 的 entry 就是我们 csp.sentinel 这个 entry 这个 entry 开始我可以定义一个空看到吧，我定义空了之后，这个 entry 是干什么的？他我告诉你外部所有的请求，比如说都进来走到这个脉函数里面，所有的请求都会要通过这个 entry 那在这里边我们必须要写一个 try catch finally 一句话。在这里我们先把这个结构写好， try catch finally 然后在安置里边。


首先在这里这是细节了。细节就是二点，一，我要做什么事情？我要定义资源，这就是定义资源什么名称，这是最关键的。什么叫定义资源名称呢？就是说你现在要做流控对不对？你要做流控怎么去做流控？你必须调 sphu 第二，什么 entry 听见了吗？ entry 里边可以添好它好多重启的方法。最简单的方式就是你可以对一个方法加 entry 当然也可以对一个普通的名字咱们叫做 hello word 都小写。也就是说现在我有一个资源，这个资源的名字叫做 hello word 好，我对这个资源 hello world 去做流控。那这个 2.2 是什么呢？ 2.2 就是说执行资源逻辑代码，什么叫做执行资源逻辑代码？也就是说我对这个资源这个资源里边，比如说他要访问数据库，比如说他在这里边他现在要访问数据库，比如说这个叫做 hello word 它是具体的资源逻辑，他要访问数据库，甚至说他要做什么，他要做访问我们的这个缓存，或者是访问我们的其他的远程调用等等，都可以反问我们的这个远程缓存。比如说 Redis 对好，当然还可以做其他事情。对不对？比如说他除了访问数据库之后，他又做了什么？在这里我再写他又做了，比如说叫做数据库持久化操作等等，数据库持久办操作。

```shell
package com.bfxy.test;

import com.alibaba.csp.sentinel.Entry;
import com.alibaba.csp.sentinel.SphU;
import org.springframework.boot.autoconfigure.SpringBootApplication;

/**
 * <h1></h1>
 */
@SpringBootApplication
public class SentinelHelloWorld {

    public static void main(String[] args) {
        // 0: 引入依赖==============>使用 Sentinel 步骤
        
        // 1: 定义资源
       while (true) {
           Entry entry  = null;
           try {
               // 2.1 定义资源名称
               entry = SphU.entry("SentinelHelloWorld");
               
               // 2.2 执行职员逻辑代码
               System.out.println("SentinelHelloWorld: 访问数据库");
               System.out.println("SentinelHelloWorld: 访问远程 redis");
               System.out.println("SentinelHelloWorld: 数据库持久化操作");
               
               Thread.sleep(20);
               
           }catch (Exception e) {
               System.out.println("要访问的资源被流控了, 执行流控逻辑");
           } finally {
               if (entry !=null) {
                   entry.exit();
               }
           }
       }
        // 2: 定义规则

        // 3: 查看结果

        // 4：控制台

    }

}
```

好了，那我现在问你整个这个资源你可以认为它就是一个方法，做了三件事情。第一件事情就是访问了数据库，比如说 select 查询第二件事情查完了之后又从缓存里查出来对不对？假设说我们有一个逻辑数据库里的跟我们的缓存里的数据要是一致的话，最终我把这条数据做一个 update 更新，或者是做一个相关的一些持久化操作，做一个音色的对吧？那这块比如说我去做一个持久化的音色操作，这三个步骤我这里边写的就都是伪代码，假设我就 select 肯定调 do 了，我在这里没调。这三个步骤它被定义到一个资源内，小伙伴们应该能理解。那比如说我在这里写一个最简单的方式，我说 sleepsleep 多久呢？我 sleep 20 毫秒表示什么呢？表示访问这些资源占用的一些耗时 20 毫秒。


然后在 catch 的时候注意我们可以去 catch 另外一种 block 我们可以 catch 更细溜溜的 exception 叫做 block exception 这个 block exception 是谁的呢？同学们想一想这个 block exception 当然你 catch 了 block exception 了，那这边你就要我直接往出抛，你直接 slow 出来，放到抛到我们的这个 man 方法。然后这个 block exception 它是做真正流控。在这里我可以写真正的流控，我可以说就是要访问的资源被流控了。然后直行流控逻辑就是这一行代码就表示这个被流控了。执行的流控逻辑是什么？好，最后 finally 的时候做什么事情，finally的时候一定要把它进行一个释放，一定要做这种。因为这个 sentinlow 它其实原生的 API 之前老师 70 多，它就是一个 Java 的客户端，对不对？你就写普通的 Java 程序即可。如果不等于空的话，那我就调用它的什么它的 next 方法去退出就好了。


OK 现在我这一段代码就写完了，小伙伴们能不能理解？也就是说我现在是 hello world 里边表示定义一个资源，这个资源里边做了三步操作，那位同学老师我可能可以做得更细粒度的，比如说每一步操作我都可以去做一个资源，什么可以呢？完全没问题。那怎么做？很简单，你要定义三次才开始。比如说这里面这是第一次，我把这个后面两个资源都注释掉，看见了吧。


OK hello world 表示访问数据库，然后我要把这个代码完全的 copy 一份，然后再写到我的主函数后面，比如这叫 entry 2 这样的。然后把这个我可能不需要反函数去做了，可能要做什么远程访问 Redis 然后这里边注意一定是变成 entry 2 了。
那如果说我现在对第三个资源我想要做 CBD 的设置，那没办法，你必须要把这个代码再 copy 一份再 copy 一份，然后再去做一个拆开 10 分钟就是这样的。可能小伙伴们会觉得复杂，但是就是只能这样去做，因为你要做到非常非常细粒度的这个流控策略。

[image](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/502d49f7-1515-4c0f-b7d1-b710319a189f/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666AFIKAST%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T225828Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCAKV0RaMbQ11Do4K%2BqFtQJp9956Fu596KhFPItCZ4wkwIhAIL9iQgl26w5qP6U7b16RcfxKxV9%2BW53kg4tz9DvxrGTKogECMb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgyEhg195pRpsBEz%2B%2F0q3ANqJnyF8wgZsSp6jHpfeUTqqu32AjP%2BZ9Nb40JWrg3Fc8xCcZBrdeyVkE3L9xcCRr4Ng%2BfcNO2qTsO1nCknwITfdbXLZFxknQ5CJ%2FZ7gtRj79GfvFOhYtPaCSIsUhHRweJFF%2FmsFX8AzVwEFrrJ%2B8WVauUgU11XwFcGhX%2FAlaiASAX2sdQfqyel7VSaeoTe1Iz1Al0d6vdc8LsOJcl73mYMNdXAMl8zafADy1%2BnBZMPJGCU4YxLAYymcyTyOUFiUhJTOOpQ3MavjBcRfC2OXFVMfLqfDPoUpD1jpEUaRy4nevstx7pl2lMrZ2FBLOvHE2S5aiSL4bcClt3AUXtt%2FNvhjdAAVWMpKZHXXRORE6og86RmXW1W3JsZxeKlt%2B9DwSKf1%2Fsc1BwcI33BVg69iFFO5gYizdwXH3loLlbhguX4eHiS569U05h9py2%2BipNRTiChCWW14qT319BKUFhQIlj5LqtgiEliUx12ZvptNFBsoIe0y7j8EK4Mqx8VxasKdJl7EhHpu3Fl1zx9o3s%2BkC3Poyrne2WUudDO3WkI1HCzCrfhjReijDGMV85fav6vAKXErFES37i3pbpU7QlLE%2BNtL%2FrOxTjVXH9%2F7CHkuVcp4dXBlrIlxC3H3mbsQDDbt%2F%2FSBjqkAUHpKEZ%2BPhwKe%2FNTmdsWUdxwRxtjkoYLiaTAoXNMuQYA03vYLyisI7UsL7DUQd%2FrketadlBYGBZVhn4%2BY8M37B0EJMxHf%2BqfzHIDzBuZYhon0H2Su7dPauUBU1QfroYzVINhHHA5wW81n1%2FoQC0lmJefZujnGOoDzwsb2Mk%2BF7geoAmayvF3gY%2Fj1jjFBYR6eT8fCodv4YUVkbZ5OAVSET5ycncZ&X-Amz-Signature=af8f41c3520a92d0920d7b275423a10f2ae69eaf3a7461459784d2f69bc76574&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

[https://sentinelguard.io/zh-cn/docs/flow-control.html](https://sentinelguard.io/zh-cn/docs/flow-control.html)


那我们暂且就认为什么呢？我们暂且就认为这三件事，欧美的定义成一个资源，我定义资源，它在真正应用程序访问到这块资源的时候，就会帮我们去做一系列的统计分析，起码是做一些统计的工作。定义资源了之后，你要对这个资源第二步要做定义亏损，对这个资源做一些限制。 OK 那这个限制应该怎么去做呢？同学们想一想，我们在这里去定义一个方法，当然这是一个主函数对吧。那我们在这个上面再定义一个方法，叫做 public static wide 我们叫做 init follow 入，其实这个代码跟官方差不多。
follow ruler 是。然后怎么去定义规则？在官网写的是这样的。首先我要有一个 Java 的普通的 list 然后我要有一个 follow ruler 这是 follow ruler 是一个对象，注意一定是我们这个 sentence 然后我们叫做 ruler 是等于 new 一个 ray 意思。然后我们要把对应的一个 ruler 给它实例化，这是必须的定义资源 ruler 等于另一个 ruler 然后对 ruler 做一些 set 的设置。


比如说我第一件事情最重要的就是应该 set 一个 resource 当然它还有一个 reference resource 我们先不考虑 reference resource 我们就 set 一个 resource 这个 resource 应该叫什么名字呢？同学们想一下，就是说这个规则是对哪个资源做的限制对吧？那这两个名字必须要一模一样，大小写都必须要一致。
就是说我这个规则是加到这个资源上面，注意小伙伴们一定要注意这一点，这个规则一定要加到某一个资源上。当然一个规则是不是可以加到多个资源上呢？没问题，规则可以放到任意多个资源上。我是不是一个资源是不是只能有一个规则呢？理论上来讲，一个资源也是可以有多个规则的。那我现在是 follow ruler 对不对？流控规则，后面我可能有一些降级的规则或者有一些什么，有另外的一些其他的，比如说热点的一些规则，黑白名单的一些规则都可以加到这个资源上。所以说它们之间本质上是一个多对多的。


但是一般来讲，在 hello world 的层面上，你可以暂时认为是一对一的关系就好。一个资源我要起码用一个规则配置。好，在这里打就是说注意我们的规则一定要绑定到对应的资源上，通过什么呢？就通过资源名称进行绑定对吧？这个我叫 hello world 那我也叫 hello worldok 然后接下来我既然是流控规则对不对？我要进行设置流控的一些规则怎么样去流控？它里边有一个静态的类叫做 ruler cost 点什么呢？ Follow qps？ Follow swiss. 同学们看一看是什么鬼？我为什么说里面大家一点点写不想 copy 呢？我们就想看一看它里面的代码对吧，你会看到它里边康特斯常量里面有什么？有 follow 泽歪德斯，还有 follow grand 也就是说我可以针对每一秒钟 QPS 去做规则的限制，我也可以针对每表中最大不允许多少个线程去做限制，这些都，我可以做一些其他的。当然这其他的就不是了。


你会看到这个 ruler cantons 它是一个什么呢？它是一个比较大的一个 cantons 对吧。我们会看到现在老师跟大家所讲的叫做流量控制的规则，它的名字叫 solo 那其实我们可以直接点到流量控制看一看。点到流量控制。好了，我们点到流量控制以后，我们看到流量控制它的名字叫做 follow control 它里边有一些属性，比如说 resource 资源名称 counts 限流的这个阈值，还有流控的类型到底是 QPS 或者是并发的线程数，这就是刚才我们通过代码看到的。然后这个叫做 limit App 我们可以对这个调用来源进行一个限制。还有这个 city G 就是说调用的关系的流控策略可以做限制。


还有在 1.6 之后新增加的这个 control 这个 behave 什么意思？流量控制效果直接拒绝或者是这种 one up 或者是匀速排队的这种方式，在 1.6 以后才真正的实现了。其实在 1.6 之前，它里边也会有这些各种各样的这个流控效果。在 1.6 之前我们使用最多的就是直接拒绝，直接拒绝就是直接跑一场。但是他后面又多了一个 one up 和这个云数排队这两个真正的才是在 1.6 之后实现的。我们现在也是用最新的版本。


OK 然后在这里边我们看到这句话，它这里边就是关于它对应的原理了，就是说这个流量的 slot 它会根据预设的规则。然后结合前面的。当然这前面有一些叫做 node select slot 还有 cluster node build slot 以及 static slot 统计出来的实时信息进行流控，也就是说什么意思，这个流控这个东西它是通过的一些具体的手段，这些手段我们就统一管它叫做 slot 槽，就是说通过一些 slot 进行一些打点，进行一些埋点，然后去统计出来的。到达这个限制之后，我就给你做一些对应的流控策略了。而这么去做好。那也就是说流控的直接表现是什么呢？看直接表现是在执行这句话的时候，我们刚才写代码叫做 sphu.entry to resource 名字的时候直接抛出的叫做 follow exception 异常。 follow exception 异常是 block exception 异常的子类。您可以捕捉 block exception 来自定义被流控之后的实际的逻辑处理一个资源可以有多条限制的规则。


然后回到我们刚才所说的流量控制有我们再找一个叫做什么呢？熔断降级，我们点到熔断降级，我们点到熔断降级，小伙伴你会发现熔断降级它是另外一种 control 它叫什么呢？它叫做 degree 处，那它所有的东西都是以 degree 的开头的，你可以看到具体的他说除了流控以外，那还有一些降级的降级也是在链路不稳定的时候。


比如说上下游依赖关系，下游服务，比如说返回的请求特别慢，或者是下游出现问题了，我们可以做一个及时的降级的策略，保障我们的应用的高可用性，它是非常重要的措施之一。由于调用关系的复杂性，调用链路中某个资源不稳定，就会导致请求发生堆积。那么 sentence 熔断降级，它会在不稳定的时候给出一个非常好的一种机制。它可以通过一些异常比例、异常数、超时时间，去做一个统一的限制，快速的去把这些不可控的请求去进行一个快速失败。它就叫做什么？ degree 的 control 就是降级策略。那它默认的行为肯定是抛出一种异常，叫做 degree 的 exception 那其实通过这一块，小伙伴们看到核心代码也差不多就是要做一个什么，做一个 entry 然后最后做一个 EST 中间这里边你看它里边只不过做了一些条件判断。


好了，那同学们看完了这个流控看完了降级还有什么？还有热点参数限流。系统自适应限流包括黑白名单控制，它其实也是一种限流。那么随便点开一个系统自适应，我们来看一看。系统自适应它叫做 system 你会看到它可能是针对于系统 Linux 这个系统负载做一个限制。当然它这里边没有对应的这个demo ，它只是让我们去看这个 demo 在这里我就返回了，我们就看一种热点规则。


热点参数我是想看到有代码的。你看热点参数什么意思？对于这某些经常访问的数据做一个流控是可以做的对吧？ OK 那你会看到这个热点参数代码都是一样的，热点参数代码都是一样的。那我们怎么去做区分呢？你看到这里边有个叫什么叫做 param follower 然后系统自适应的叫做 system for ruler 降级叫做 degree 的 ruler 我跟你说这么多，不是说要给你把这些规则现在马上就让你学会，而是什么，而是让你知道怎么样去学习。现在小伙伴们通过代码肯定知道了一点，这些规则肯定有对应的负累。


怎么说？补 lock exception 我按 control 加 T 我们看到 block exception 它的父类是 exception 它的子类是谁？它的子类有 author exception 有 degree 的 exception 有 follow exception 有 param follow exception 有 system block exception 还有一个什么 new block exception 对吧？好了，那对应着它这五个子类，这个就是安全相关的黑白名单的 degree 的降级的 exceptionfollow 流控的 exceptionparam follow 热点参数的一个 exception systemblock exception 就是系统的自适应的 exception 也就是说这个 block excep 森它是一个比较全局的比较大的一个负异常。它的子异常。


如果你具体是流空异常，你可以捕获这种 follow exception 如果你是降级异常，你可以捕获这个 degree 的 exception 对吧？ OK 那同理，我们这些具体的异常我们知道它能够分得特别细，你具体是什么样的异常，我会给你怎么去抛出。那我们的规则也是一样，我们有 follow 入了，我们点进去看一下这个 follow ruler 它父类叫做 Abase tract ruler 这个 Abase track ruler 它又 implements ruler 我们看到它整个的结构是什么呢？ f30 ruler 也有对应的五种规则。

[image](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/e925a2d8-64ac-4328-be58-db9d3b336210/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666AFIKAST%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T225828Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCAKV0RaMbQ11Do4K%2BqFtQJp9956Fu596KhFPItCZ4wkwIhAIL9iQgl26w5qP6U7b16RcfxKxV9%2BW53kg4tz9DvxrGTKogECMb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgyEhg195pRpsBEz%2B%2F0q3ANqJnyF8wgZsSp6jHpfeUTqqu32AjP%2BZ9Nb40JWrg3Fc8xCcZBrdeyVkE3L9xcCRr4Ng%2BfcNO2qTsO1nCknwITfdbXLZFxknQ5CJ%2FZ7gtRj79GfvFOhYtPaCSIsUhHRweJFF%2FmsFX8AzVwEFrrJ%2B8WVauUgU11XwFcGhX%2FAlaiASAX2sdQfqyel7VSaeoTe1Iz1Al0d6vdc8LsOJcl73mYMNdXAMl8zafADy1%2BnBZMPJGCU4YxLAYymcyTyOUFiUhJTOOpQ3MavjBcRfC2OXFVMfLqfDPoUpD1jpEUaRy4nevstx7pl2lMrZ2FBLOvHE2S5aiSL4bcClt3AUXtt%2FNvhjdAAVWMpKZHXXRORE6og86RmXW1W3JsZxeKlt%2B9DwSKf1%2Fsc1BwcI33BVg69iFFO5gYizdwXH3loLlbhguX4eHiS569U05h9py2%2BipNRTiChCWW14qT319BKUFhQIlj5LqtgiEliUx12ZvptNFBsoIe0y7j8EK4Mqx8VxasKdJl7EhHpu3Fl1zx9o3s%2BkC3Poyrne2WUudDO3WkI1HCzCrfhjReijDGMV85fav6vAKXErFES37i3pbpU7QlLE%2BNtL%2FrOxTjVXH9%2F7CHkuVcp4dXBlrIlxC3H3mbsQDDbt%2F%2FSBjqkAUHpKEZ%2BPhwKe%2FNTmdsWUdxwRxtjkoYLiaTAoXNMuQYA03vYLyisI7UsL7DUQd%2FrketadlBYGBZVhn4%2BY8M37B0EJMxHf%2BqfzHIDzBuZYhon0H2Su7dPauUBU1QfroYzVINhHHA5wW81n1%2FoQC0lmJefZujnGOoDzwsb2Mk%2BF7geoAmayvF3gY%2Fj1jjFBYR6eT8fCodv4YUVkbZ5OAVSET5ycncZ&X-Amz-Signature=a658c2c579d3e2458031ccd6e8676139a1aae8d83eed8fd5a6ee41cb91c29002&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

我们刚才只知道的是 follow ruler 对不对？这是 follow ruler 除了 follow ruler 以外，它肯定还会有降级的 ruler 就是 degree 的 ruler 有黑白名单，就是安全验证的 ruler 就是 auth 类 ruler 还有什么呢？热点参数的 ruler 就是 param ruler 还有我们的 system loser 也就是说它都是成对出现的，它都是按照五个规则，现在目前三次哨兵就支持这五种最常用的策略。


那我们知道它了以后，我们再回过头来再看这些 rule 每一个规则它都有一个叫做规则管理器的东西。我们把这个具体的一种规则你设置好了以后，比如说我现在再往下去设置，我可能我要对流控做一些限制，我就 count 是不是我给它限制成20，就每秒钟并发最大20。然后把这个规则填到这个 list 里边，就是 ruler 是点 add ruler 填到这个 list 里边。接下来做什么事情，你这个规则设置好了之后，你是不是要把这个规则放到一个地方，让我们系统识别？所以说对于 sentence 来讲，它会给你去提供一些规则管理器。


这个规则管理器有好多种，我们先用最简单的叫做 follow ruler manager 它静态类点直接 load ruler 撕，直接把这个 list 放到这里。那这样的话，你当前的这个规则就已经被我们 3 乘 4 服务加载进来了。当然由于我是慢函数，所以说你在最开始的时候一定要初始化规则，直接调用一下 init follow rules 就好了。


好，那这个里面到底做什么事情呢？它是怎么帮我们把资源管理起来的，大家可以看一看，点进去就好了。点进去你会发现它有一个 current practice.update value 那 current practice 就是什么东西？ current practice 我们看到代码它是一个什么？它是一个对象，叫做 sentence property 对吧？然后这个东西是什么东西？他做 update 是做什么动作？小伙伴们是不是有想去看一看的这个冲动？好，那我们来一起看一看。


那你其他往上看，你看到这儿了吗？叫做 map string 然后对应的是一个 list rules 然后叫做 follow rust 所有的流控规则都会帮我们去放到一个 concurrent hashmac 里面。其实你可以看到我们的这些规则，它都是持久化到内存作用。当我们的服务一旦重启，这些规则就都没了，这是三次它的一个硬伤，早期版本的运营商。
不过其实在真正的阿里内部可能都是直接做了一些文件的持久化的策略，包括一些配置的持久化策略。它开源出来之后，才提供了一些对阿波罗，对祖 caper 对我们的 nicos 包括对 Redis 的一些持久化的这个数据源的这个制定。Ok.好，我们废话不多说，我们来看一看这个东西到底是怎么去做的，它是一个对象，它里边要求泛型，就是一个 list followers 我们点进去看它是一个 interface 那具体会看到它下面的实现类对吧。 dynamic 是不是这有一个叫做 no option sentence practice 还有一个叫做dynamic ，就是动态的一些这个 sentence practice 动态的规则。这个动态的规则里边它是需要一个监听的，你看这个监听里边有什么 update valueok。


那其实同学们看到这个 update value 就知道我现在想要做的是什么事情。那我们真正 follow 入了 manager 他在真正的去加载规则的时候，他调的是刚才我们看到的那个 load 方法，就是他这个 load 方法它其实底层调用的是 current practice.update value 对吧，那我们直接可以点进去，我们点到 dynamic 是不是它其实走的就是一个新的规则。


这个新的规则为什么用泛型定义呢？因为什么？因为我们之前我是只是在这里边 load 的时候，就是在我们 follow room 的 manager 的时候，我知道它的规则是流控规则。当然这个东西它是一个最底层全局通用的。所以说我不知道它到底是 follow ruler 还是说降级的 ruler 定位入了或者是一些热点参数的 role 我不知道。
所以说我用一个泛型，那在这里小伙伴也可以看到它是一个泛型去做的，就是一个 T 然后这是一个新的 value 他会判断他说 equals 就是说你的新的跟我的旧的规则，旧的规则它被引用进来了，他在 add listen 的时候已经把这个东西是 load 进来了，然后放到这个变量里了，他们两个会比对。


如果说 equals 就是相等。当然它的一个相等判断的就是是否一致。其实你可以看到就是他们两个 old 和新的是否是我们这个 summer.long.object 的这个 equals 如果是 equals 就认为相等。如果不 ecos 直接 return 我们的force。 Ok. 好了，我们看到什么呢？如果相等，那就认为你没有变化，直接返回 force 就好了。如果不相等，那我就重新的去调用这个蕾丝，然后重新的去把这个新的规则去继续的去 update 一下。这就是最简单的。


那其实同学们你可以看到，那这个 list 到底是什么东西？我们再看一眼就知道这个 list 是一个 set 听见了吧，它是一个 connections.syncs set 就是它是一个怎么说线程安全的一个集合，就把一个线程不安全的哈希 set 进行一个包裹，变成线程安全的。


那其实通过这一块，我其实想要跟小伙伴们说的什么意思？它这些规则的更新完全没有任何请文件持久化一些动作都是基于内存的一些哈希 map 要么就是 set 对吧。所以说你要知道，当我们的服务一旦重启的时候，这些规则就都丢失了，就是起码是这些 ruler managers 就都丢失了，这就是他一个最大的问题。 OK 现在你看到就是 follow 入了 manager 我们点进去你看。


当然我们现在点到的是 follow ruler manager 我们看 degree 的你会看到有一个叫做 degree 的 rule managerdegree 的 rule manager 怎么去做的呢？差不多大同小异，它都是引用了那个 current practice 那个类都是引用了这个 current party 之类，都是使用的叫做dynamic 。 Sentinel party. 包括你可以再往下去找，除了 degree 的流控，当然还会有什么？还会有一些像我们的热点参数，包括自适应黑白名单验证，安全验证对吧，你看这就是安全验证这样做。


ulssly ruler manager 当然热点参数它单独的有一个 system 的一个包，后面我们再去找。我们先看那个系统自适应叫做 system system 里边你看它有个 system ruler manager 那 system 目录的 manager 也是一样，你往下去找就好了，你会看到它也有一个 sentinel copy 也是使用的 dynamic sentinel office 那所以我们看了这么多源码的结构，在这里可以跟小伙伴们简单做一个总结，就是说我们的三次哨兵，它里边对主流的五种流控策略做了底层的抽象和资源的封装。


对不对？比如说我们现在用的是流控的 ruler 就是对于规则而言，对于规则，我们有流控的 ruler 还有什么 degree 的 ruler 就是对于降级的入了还有对于什么？对于热点参数叫做 param follow 还有对于系统的自适应，就是我们的 system follow。



