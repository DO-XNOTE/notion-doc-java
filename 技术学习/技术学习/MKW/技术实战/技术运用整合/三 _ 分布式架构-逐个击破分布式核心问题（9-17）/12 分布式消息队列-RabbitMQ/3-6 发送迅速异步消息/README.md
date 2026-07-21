---
title: 3-6 发送迅速异步消息
---

# 3-6 发送迅速异步消息

[image](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/ad263345-6a28-4465-a9e0-bc2873cca70d/SCR-20240806-qzdp.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666JSGJMRQ%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T225300Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIAX4tR%2BO0RROb%2B5gkFTULvl05gUc4C1tTczo1mMTez0uAiEAg%2BRqlYaedxtuHHfBL%2BUldYkhgBG8%2F3TsWrKCOLOiYvAqiAQIxv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDIV6T0Ih4xkNa008%2ByrcA72bwr2E2MrVA9auaaTn3bySudSUxL8tD2lAVBjKIqqW6Pew7ZCYNCCaD3jdy85yM6m0Aj6XUdN4C%2F5BlBJBdCz%2FMws9S8uDDLPyuiwk7H0Zw6AeSVXTGoxApSEkN27MSqctvnYRqiUOxzCkCV2jQcXBUPkQ6zmtTcy9Y4r0vBH%2FKOuSC%2FDF5cxjwxVNfVgcmRkIBx12nnRZChRsk1xCMcYOFhjolOC%2FgNjq1BsvwpSzVF8Tq5H6hE%2FrlOoaAo4RA2RDt7yo5X83jLIWRgz76zihZVz9FH%2FvxGxBrmHLa%2B%2BMVrNIxoG7DKfauSJF6ykqd6ILWBGzpuV1HTL45cMXluCgmcGMez5SUTh%2BxbeKqBGFeVJr%2FHMDNPHGQdVqGcqyejfGZBfPgkns5vS5nk8UnkrtfN%2BxlizTlPL8zmGDsnEh424k84LVAkTGewdcRYE6B8ey41Wew8SrgMxaMwgn6qVZJ67EnS3k5OwsOQU35rlkt4V%2Fd5013h%2FFltd%2B56hN6zl9JZW2Rf95BDUBxusaL%2FhLhhiFWwNuB9PthYNZDo66dA4lmvCh59Xv9hsxKEMfKaWrtA19beHGhaClXkGS4gi9MAHEKw0wbsEMNSbH1XvYoLPZO8Xn6M0EpT7TMMS6%2F9IGOqUBYZ7Wps4by2ZT%2F1VlpVOyMeVsnn3TCegmiNVAjN01SwE5YE3VHv2zC42RULYrg66edCfm7fK%2BOzizPG2q3T%2B039WXTXJmmkZ3OvODsxCFB%2FU%2FeTwZOvo%2BP7%2F7V88L70fTp2XiCcGjB7BzB3CBfGpM2q9iB2re%2FgPdJQhdp1YMTkHqC42UbDWn8GS9hR%2Fs20Rw%2BRNOzpnXnFBhy6Ep8tITH6MDMlSy&X-Amz-Signature=d5c62a02ab8f6e6197a2fb65dfc3721bf2d7f59ea6a8cb841e14774a331b0731&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

[image](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/a9b88fb0-b0d2-47d6-8585-f7f6e01e6e08/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666JSGJMRQ%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T225300Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIAX4tR%2BO0RROb%2B5gkFTULvl05gUc4C1tTczo1mMTez0uAiEAg%2BRqlYaedxtuHHfBL%2BUldYkhgBG8%2F3TsWrKCOLOiYvAqiAQIxv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDIV6T0Ih4xkNa008%2ByrcA72bwr2E2MrVA9auaaTn3bySudSUxL8tD2lAVBjKIqqW6Pew7ZCYNCCaD3jdy85yM6m0Aj6XUdN4C%2F5BlBJBdCz%2FMws9S8uDDLPyuiwk7H0Zw6AeSVXTGoxApSEkN27MSqctvnYRqiUOxzCkCV2jQcXBUPkQ6zmtTcy9Y4r0vBH%2FKOuSC%2FDF5cxjwxVNfVgcmRkIBx12nnRZChRsk1xCMcYOFhjolOC%2FgNjq1BsvwpSzVF8Tq5H6hE%2FrlOoaAo4RA2RDt7yo5X83jLIWRgz76zihZVz9FH%2FvxGxBrmHLa%2B%2BMVrNIxoG7DKfauSJF6ykqd6ILWBGzpuV1HTL45cMXluCgmcGMez5SUTh%2BxbeKqBGFeVJr%2FHMDNPHGQdVqGcqyejfGZBfPgkns5vS5nk8UnkrtfN%2BxlizTlPL8zmGDsnEh424k84LVAkTGewdcRYE6B8ey41Wew8SrgMxaMwgn6qVZJ67EnS3k5OwsOQU35rlkt4V%2Fd5013h%2FFltd%2B56hN6zl9JZW2Rf95BDUBxusaL%2FhLhhiFWwNuB9PthYNZDo66dA4lmvCh59Xv9hsxKEMfKaWrtA19beHGhaClXkGS4gi9MAHEKw0wbsEMNSbH1XvYoLPZO8Xn6M0EpT7TMMS6%2F9IGOqUBYZ7Wps4by2ZT%2F1VlpVOyMeVsnn3TCegmiNVAjN01SwE5YE3VHv2zC42RULYrg66edCfm7fK%2BOzizPG2q3T%2B039WXTXJmmkZ3OvODsxCFB%2FU%2FeTwZOvo%2BP7%2F7V88L70fTp2XiCcGjB7BzB3CBfGpM2q9iB2re%2FgPdJQhdp1YMTkHqC42UbDWn8GS9hR%2Fs20Rw%2BRNOzpnXnFBhy6Ep8tITH6MDMlSy&X-Amz-Signature=acafed617e3d84d11bbb9a026f5da3425554c027a4ecf73fb20d8b0108e6e32c&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

那上节课呢？我们已经知道了，我们有一个这个 producer client，它实现了这个 message producer 接口，然后把这三个 send 方法都已经实现了，一个是带回调函数的，还有一个是没有回调函数的，然后还有一个是干什么？就是一个 send message 4，就是一个批量发送，那真正发送应该怎么去做？包括我们应该怎么去着手往下思考？这个我相信是小伙伴们比较关注的一个内容，如果说小伙伴对于这个扎特这种写法就比较别扭，那其实很简单，那你可以干什么？你可以直接在 configuration 上加一个 component scan，加一个扫描的这么一个注解，然后就按照你想的方式去写就好了。比如说我举个例子，在这里我写一个 component scan 去扫描。扫描什么包啊？就扫描我们自己的这个包哈，比如说就是 Com 点 b f x y，点rabbit，点 producer 点行就可以了，是不是我现在就认为它是一个普通的 spring board 工程，然后我去写就好了。


这样的话你的思路是不是就有了？你比如说这个client，那这 client 我要怎么去写？首先我是不是把它给它交给 spring 管理？所以说一般来讲我都这样去写就好了。导入一个 component 注解，对吧？就搞定了。然后干什么呢？接下来这个 produce client 里边是不是需要有一些其他的依赖呢？他怎么去发消息啊？给我提供的是这个 send 方法，对不对？就是一个 send 方法，而我们可能有各种各样的发送消息的这种机制。比如说回过头来看，我们 API 里边，我们 message type 里边有什么等于 0 的，等于 1 的以及等于 2 的，就是发普通的迅速消息，然后呢？还有什么确认消息以及可靠性的消息，每一种消息你应该怎么去发？那这个都不一定。所以说你单纯说老师我从这个 producer client 去发消息，那这个不太好。这个 message 有了，我们应该知道这个 message 的类型，然后再去写。因为我们的消息类型有这三种，所以说我得根据不同的类型去写不同的发消息的这个业务逻辑才可以。


这个component，比如说把它注入到 spring 馆里了，当然后面我们肯定不是用这种写法，一般我们写 starter 都不会说 at component 这么去写，这样写太 low 了。一般我们会在初始化的时候先处理好，那这个如果你不会，我们先按照这种思路，然后慢慢的再去转变过来就好了。先不管其他的 call back 这个我们就先把它放到最后，因为这个可能稍微复杂一点，我们就先管这个。


第一个最简单的 send message，那这个应该怎么去写呢？这个我想注释 producer client 就是说发送消息的实际实现类，一定要实现这个 message 普格斯这个接口，那我怎么去发消息啊？同学们想一想，发消息的时候，比如说首先我去做一个 check 它的topic，如果是空的话，那其实我们就抛个异常对不对？这是不是可以还有一个 Pro call 的这个 condition 条件的这么一个司法？这个是 Google 的，对不对？ Google common 的一个包含就可以去做一个check，比如说arguments，如果不符合我们的要求，它里边会抛一墙的。


比如说我在这里随便找一个，咱们叫做 check not，然后就把 message 放进去 m e s a g e 点，比如说一般来讲我们的 topic 的部分属于UNA，我们就这样去写好，那这个里面怎么去实现，怎么看一眼？如果说这个 reference t 等于none，那就直接往出 slow low point exception，OK，所以说很多时候我们可以用第三方的一些比较不错的包做一些 check 检查，就没必要自己去写等于空，然后自己再往出抛 no point exception，你看代码非常简单。


OK，好了，那如果说这个 topic 不为空，那是不是我们的逻辑就可以继续往下走了？也就是说老师，那我在创建 message 的时候，我们一般不就是用那个 message builder 嘛，对不对？之前讲了 topic 等于工作时已经 throw 这个 runtime acception 了，对吧？为什么我们在这里还要做check？ message builder 只是一种构造的方式，可能别人不用 message builder，可能他就是习惯了就用一个 message 是不也可以？这个说白了就是一个 helper 辅助类而已。


所以说我们在这里该 check 还是一定要做check，然后我们想一想，我们是不是要根据不同的消息类型？比如说我们先把 message type 取出来， message type 如果等于 message 点 get message type，我们取到了这个 message type，是不是应该做一个判断？比如说在这里我们去做个 switch 判断 message type，如果 message type 等于什么？比如说在这里它等于迅速的让我们做什么事情，对不对？然后在这里我们继续往下去写，一共三种了，还有一种是什么confums，还有一种是叫做rate，根据不同的消息类型我应该做不同的处理，那具体怎么去处理？假设说我应该再衍生出来一个类，那我应该怎么去实现？现在可能想不出来，但是我们是不是可以先做一层抽象？这个事情其实是非常非常重要的，我们来想想这个东西我们应该怎么去抽象。我现在举个例子，发迅速消息还好， config 消息也还好，发这个这种可靠性投递的消息可能要真正的去跟我们的数据库相结合了，具体对于可靠性投递我们后面再说。那我们现在肯定有一个实体帮我们去发这 3 种，看看能不能抽象出来。比如说我现在就开始抽象，我在布鲁克里边做一个接口 interface part，比如说叫做Rabbit， Rabbit Broker。好，这个接口我们先定义一下，它是一个interface，这个我说具体发送消息的接口，不同种类型消息的接口，我们来看一看我都有哪些种类型消息。


首先我在这里边就返回之外的就可以了，比如说 y 的第一种就是repeat，这叫是迅速消息，我们自己的 message 好，这是第一种。然后还有什么 confirm 是不是？还有就是可靠性的 3 对吧？那 3 对吧？如果说批量消息也是一种的话，其实我们可以再写上 send message。


上层 message 是一般我们需要一个 list 列表，在这里我先不写，因为这个我不确定我应该怎么去写，所以说我们先把这个接口定义好，有了这个接口，那我们是不是有对应的这个接口的实现类，应该怎么去做这个broke？我是不是应该在这里边根据不同的消息类型，然后去看看实际怎么去发送？按照我们正常的逻辑，我们应该这样去写 auto where 的，我们自动装配进来对不对？然后具体调这个接口的这种迅速的 send 是不是就可以了，对吧？然后这种 config confime 就可以了，然后这种是不是调这个就可以了，对吧？这是我们的一个想法，针对不同的消息，根据消息类型，我们应该进行具体的这个发送。逻辑嘛。


好了，有了擦了之后，接下来就好写了，那我们来看一看吧，现在我们代码已经写死了，就是这个 broker 已经知道了，那这个 broker 的实现不还简单吗？我们直接写一个类，咱们叫做 Rabbit broker implements，可以，它只有帮我去实现这个接口里的 3 个方法，你是不是也把它变成一个 component 就行了？这个 component 被 spring 管理了，那么接下来我们看一看这个布鲁克应该怎么去写啦？那首先呢，我们看一看迅速消息应该怎么去写？迅速消息很简单，就是说我发这个消息我也不需要考虑太多，我就希望他马上把我发出去。我说迅速消息不管怎么样，我得 set 我们的 message type 等于什么呀？ repeat 这种类型。然后我们比如说内部搞一个 private 的方法，就叫做 send Kerm。发送消息的核心方法，我们叫做 send Kerr。好了， send Kern，我们直接把这个 message 传进去，直接把这个 message 传出去好，然后他让我去盯一下，我们把它认出来。


发送消息的核心方法后面可能我们很多发消息都需要依赖于这个三个客，它是不对外暴露的发送消息的核心方法，然后在这里这个发送消息的核心方法我们应该怎么去做？在这里边发消息的逻辑，我们使用 spring boot 去发消息，一般我们怎么去做？一般的情况下我们都会用什么呀？都会用一个 rabbit template。


还记得了，回过头来把之前老师讲的那个 producer 这个代码打开，我们来看一看。那我们之前去写发送消息逻辑的时候，是不是直接注入一个 Rabbit template 就可以了？那在这里你也可以这样去用啊，对吧？比如说它既然是交给 spring 管理，那我完全可以这样去写嘛。我们先不管这个 rap template 我配好，那我先看看怎么去用它。比如说这个 rap template，我想去用它 send curl，就是直接调它的 convert and send 就可以了。那我们现在来写一写吧， Rabbit template 有了它，然后点 convert and send message，当然在这里边有好多参数的，我们是不是可以选一个就是比较多的参数的，这个就比较多。


第一个是exchange，然后 routine key 是不是也可以有？还有 object 就具体消息的内容了，对不对？最后一个参数就是 calculation date，就是我们自己的这个消息的唯一的这个主键就是 rain time q 的定义。那我们照着这个逻辑来写一写这个exchange，是不是我们直接在定义 Rabbit template 的时候，我们是不是可以去给它取出来？比如说 Rabbit template 点 get routing key，还有 get 什么呀？ exchange 直接就看到了，我是不是直接可以取出来这个 get exchange 或者这个 message 里边？我们最开始定义的时候，它是不是有个topic，对不对？那这个 topic 是不是就相当于一个限制？所以不管怎么样你都可以去，因为我们后面肯定不这样去写，暂时写死了。


x change 先这么写死了，然后 routing key 肯定是从这个 message 里取出来的。 get routing key 我先都这样去写，首先这个 routing key 先有它，然后 string 我们有了这个topic，然后就是 message 加 get 了topic，对吧？好，有了这两个，然后这个具体是什么呀？具体就是 message 把 message 扔进去，然后这个 calculation date 就把它弄出来，是不是我们直接 calculation date，直接用我们的这个 spring 的 AMQP 的这个就好了？所以又一个什么 coloration date，然后这个 ID 是什么呢？ ID 是不是你之前已经定义好了的？来我们来看一看你的 message 里边是不是就已经有 message ID 了，对吧？这是我之前已经包装好的，所以说完全我可以做一件什么事情，比如说我把它这个 format 一下string，然后点 format 我卖的它的格式，比如说是一个百分号 s 的占位，比如说用井号分隔，再来个 2% s，就我用井号分隔两个占位的，第一个占位的我们就取出来一个 message 就好了。 message 第二 get message ID，第二一个占位子，比如说我们用一个当前的时间戳system。

The current time in this still do not.


好，现在我就写完了，同学们看到这个 call 流 listen date 怎么去做的？来，我把它这个 new 的过程分成两个步骤，这样大家看着就清晰了。就是说我用一个井号作为一个分隔，然后百分号 s 就一个占位符，就是 message ID，加上井号以及当前的时间戳，以它两个字符串，以井号拼接成为一个唯一的ID。最后把这个 calculation data 放到这里是不就可以了？那具体这个 exchange 就是这个topic，没什么可说的。


好了，那这样的话我就已经分发完了，这个 send message curd 就是核心发消息的，这个方法我已经搞定了。然后最多撑死我打一下日志，比如说我在这里加一个 s f， o g 打个日志，我说 log 第二 info 发完消息了吗？我就说 send to Rabbit，然后逗号 message ID 是什么？我就直接取出来了，从 message 点 get message ID，这个打逗号 message ID 好了，就是我打个这个日志就好了，已经搞定了。


好，然后这个是什么方法？是 Rabbit broker implements 这个类似的 send current 这个方法。一般来讲我们用井号作为一个输出后果，对不对？这样比较正规，就是井号开始，井号结束就表示它是哪一个类的，什么方法，然后执行什么逻辑，发消息的 ID 是什么，对吧？好，其实现在我就写完了，这就是核心，发送消息，用我们迅速消息就直接把它扔到MQ，我也不需要什么Excel，什么也不需要就可以了。


那其实接下来同学们你是不是要考虑一个问题，就是说我怎么去做一个异步化的过程？就是说我这个消息我不想这么同步的去阻塞。本身来讲它这个 convert 和 send 它确实是一个异步化，但是你在这里边你又生成了 coloration ID，又做了这些配置，感觉性能是不是也会有一点这个慢？所以说你最好的方式，你比如说把它放到一个异步的队列，让这个克制方法就是性能更加的高，可不可以？其实也可以在这里比如说我们用一个线程池是不是可以？那我们在这里我先弄出来一个一个class，比如说我们叫做 a single 异步s，y，c，然后去我给他起个名字叫做 a C q e a s e basp，他做的事情是什么呢？它这里边就是一个线程池了，我们定一下线程池基本的一些属性，比如说线程池它的 thread size 是多少？ thread size 是我 run time 的 avariable processor。


有了这一个属性之后，我们可能还会有，比如说队列的大小，是不是这个一般也是我们需要关注的，比如说 QE 杠等于，比如说 1000 和1万，也随便给他一个。有了这两个属性之后，我们再来一个private，然后static，我们搞一个 executor service，我们叫做 Thunder i think，等于什么呀？ new 一个自定义形式，什么 thread for executor，对吧？这里边有一堆参数， cost 是多少cost？我们就是这个 Max 就乘以 2 好 Max 或者你想怎么去加就怎么去加，无所谓了。或者是我们就写死了 Max people live 的和我们说60L，这里边时间戳 time unit 点second，然后 work in， work in 是什么？以及它其实还有一些什么拒绝策略那些东西，我们就一起都来写一写。顺便回顾一下我们的线程池哈。


work king 我们就用 early block Queen，用一个 array locker，然后这个开口就是容量嘛，容量的话其实无所谓了，你就写 pin SARS 对不对？你在这里已经定义好了，唉sorry，我们就写 pin SARS 搞定了之后还有哪些参数？比如说他当前的这个什么 thread factory 是什么？我们就用一个 thread factory，比如说打个逗号，这里边我打个括号，现在是奥瑞布 locking king 多了一个多雷括号，就这个嘛，这是对应的利用一个这个工厂多余的。

```java
package com.bfxy.rabbit.producer.broker;

import lombok.extern.slf4j.Slf4j;

import java.util.concurrent.*;

/**
 * <h1></h1>
 */
@Slf4j
public class AsyncBaseQueue {

    private static final int THREAD_SIZE = Runtime.getRuntime().availableProcessors();

    private static final int QUEUE_SIZE = 10000;

    private static ExecutorService senderAsync = new ThreadPoolExecutor(
            THREAD_SIZE,
            THREAD_SIZE,
            60L,
            TimeUnit.SECONDS,
            new ArrayBlockingQueue<Runnable>(QUEUE_SIZE),
            new ThreadFactory() {

                @Override
                public Thread newThread(Runnable r) {
                    Thread t = new Thread(r);
                    t.setName("rabbitmq_client_async_sender");
                    return t;
                }
            },
            new RejectedExecutionHandler() {
                @Override
                public void rejectedExecution(Runnable r, ThreadPoolExecutor executor) {
                    log.error("async sender is error rejected, runnable: {}, executor {}", r, executor);
                }
            }
    );

    public static void submit(Runnable runnable) {
        senderAsync.submit(runnable);

    }
}
```

好了，这就可以了。然后我们看看这个怎么去写，比如说另一个 thread 我们怎么去写它？有一个 thread 我们就把它弄出来，比如说 t 等于 new 一个thread，把这个 r 放进去，然后返回好，然后这个东西干什么？比如说我们给它起个名字，是这个比较关键的一点，可以去设置这个现成的名字，我们叫做 Rabbit m q。然后杠什么呢？比如说我们现在叫 client 杠 a single sander，然后这就是它的这个名字，这个是发送的这么一个线程，是在做事情好了，然后接下来比如说还有一个拒绝策略，你有一个 rejection 的 excuse color 好了，那这样的话这个拒绝的话我们就打一个 l log 就好了。

[image](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/a837393f-fdf0-4e26-8121-fca1ffec563c/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666JSGJMRQ%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T225301Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIAX4tR%2BO0RROb%2B5gkFTULvl05gUc4C1tTczo1mMTez0uAiEAg%2BRqlYaedxtuHHfBL%2BUldYkhgBG8%2F3TsWrKCOLOiYvAqiAQIxv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDIV6T0Ih4xkNa008%2ByrcA72bwr2E2MrVA9auaaTn3bySudSUxL8tD2lAVBjKIqqW6Pew7ZCYNCCaD3jdy85yM6m0Aj6XUdN4C%2F5BlBJBdCz%2FMws9S8uDDLPyuiwk7H0Zw6AeSVXTGoxApSEkN27MSqctvnYRqiUOxzCkCV2jQcXBUPkQ6zmtTcy9Y4r0vBH%2FKOuSC%2FDF5cxjwxVNfVgcmRkIBx12nnRZChRsk1xCMcYOFhjolOC%2FgNjq1BsvwpSzVF8Tq5H6hE%2FrlOoaAo4RA2RDt7yo5X83jLIWRgz76zihZVz9FH%2FvxGxBrmHLa%2B%2BMVrNIxoG7DKfauSJF6ykqd6ILWBGzpuV1HTL45cMXluCgmcGMez5SUTh%2BxbeKqBGFeVJr%2FHMDNPHGQdVqGcqyejfGZBfPgkns5vS5nk8UnkrtfN%2BxlizTlPL8zmGDsnEh424k84LVAkTGewdcRYE6B8ey41Wew8SrgMxaMwgn6qVZJ67EnS3k5OwsOQU35rlkt4V%2Fd5013h%2FFltd%2B56hN6zl9JZW2Rf95BDUBxusaL%2FhLhhiFWwNuB9PthYNZDo66dA4lmvCh59Xv9hsxKEMfKaWrtA19beHGhaClXkGS4gi9MAHEKw0wbsEMNSbH1XvYoLPZO8Xn6M0EpT7TMMS6%2F9IGOqUBYZ7Wps4by2ZT%2F1VlpVOyMeVsnn3TCegmiNVAjN01SwE5YE3VHv2zC42RULYrg66edCfm7fK%2BOzizPG2q3T%2B039WXTXJmmkZ3OvODsxCFB%2FU%2FeTwZOvo%2BP7%2F7V88L70fTp2XiCcGjB7BzB3CBfGpM2q9iB2re%2FgPdJQhdp1YMTkHqC42UbDWn8GS9hR%2Fs20Rw%2BRNOzpnXnFBhy6Ep8tITH6MDMlSy&X-Amz-Signature=42df15778aaaa112fb5f4058ffe28eddd9eac40923928d852b6233f22e09da9f&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

在这里边我们 s l o g 拒绝的话，我们其实 log 点 e r o r log，就是说 a single sand is error rejected，然后我们打印出来它的这个线程池的线程是什么就好了，叫做 runnable 以及 executor 就被拒绝了，可能是我们这个满了，我们的容量达到上限了，或者是被我们的这个拒绝了，我们自己写拒绝策略这么一个事儿打印一下。


好，那这个就是我们整体的这个 a think，它的这个一些类主要就是一个executor，然后我们就来一个方法，这都是 private 的，来一个公共的。比如说来一个 public 的方法去做一个提交 the public static wide，我们叫做submit。对，方法反正就是给我放一个 runner 接口的 runner 过来，然后我去帮你去提交一个任务，对不对？就是我们这个 send a single 要他的 submit 嘛？好，我们的这个 runable fun 就好了，搞定。那这样的话我们这个异步提交的这个 base q 已经写完了。


回过头来，那我们现在要做的事情就是我们在真正发迅速消息的时候，是不是就可以依赖于他？那我们再回到这个client，或者说回到这个 broke client 还不够，我们还往下去点，回到这个broker，点击broker，点到它具体的实现。然后在 send 客人的时候，是不是我们就可以加上这个东西了？因为我刚才已经封装了一下了，在这里边我们就可以用这个点 submit 一个 run 接口的内容啊，我们也叫runnable，然后一个尖括号，一个大括号就搞定了，我们把这个里边的内容完全的去写到这里边，这个 runnamo 像少了一个这玩意儿，对吧？ learning 接口，然后就是异步去提交好了，我们现在已经实现了第一件事情，真正的发送不同类型的消息，实现类，然后它也实现了迅速发消息。


怎么去做？其实核心调这个 send 客人方法，用一个异步队列去做的，这样的话这个性能会很高，使用异步线程池进行发送消息，这样的话它的性能会非常高。哈，好了，那其实呢，我们第一块发迅速消息已经跟大家讲完了，我不知道小伙伴们对于这个发迅速消息，OK，这节课我们就先讲到这，感谢小伙伴们收看。



