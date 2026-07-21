---
title: 3-32 【技术改造】电商系统集成Eureka - 订单中心-3 
---

# 3-32 【技术改造】电商系统集成Eureka - 订单中心-3 

[image](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/ce89a9de-0293-499d-90f7-139dcc2e3b84/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VZTRBEKM%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T225559Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIHAtbCp61Hqqu7tOd%2FpIUHLntWxDXV0C9PeHiBrawz33AiEAjpy1rHuuXVihDXJR2VS%2F3HNQrSU10StcWD6l5CyHVmQqiAQIxv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDNQyA5B3lJX%2FTEY63SrcAzipiNMDzKwLR7zN5NwjC2xJkU2DF%2FmtLMuvHU0vmr7cnfYKuXKorUd0YAp5r0feQCDX8XF10o4xF7%2BIZkMxOivrr4JZGyghgBIQn%2FkNU3c0LFrNrcl0xwGtYnjaFCBYmJEQ1QlUMVQgH95TtltdEije5gD8sVPfvYJr8cfpSh6vwRiV7u0KzcpcRHuTLLuu%2BJ5AoZkznOylVq0Bsqv%2BM4YQOxuk9yxW%2F9T5lcloe0N4QnCoe0sLSTMKnGjeLdst0SYeTnqMf0ph9GcsT9UGZDA9mJ%2BBJjvtZG1HLhc2xyy3L2mT9gIKeKYi0UEk%2BpqkuYyfJnmwr3kFVvFiIH5Rrlql%2Bj0sfj5R91TnpScT4vS5FCWoKm3QtMfpuuViWJCIH3kjOaGrqiE%2BScxMQmThB6k%2FkkC%2B4a%2FkmI%2FdytUYIv8kodnUMkUuLb3GUkXtkQ7TTK%2F9akTrinBBFpjQHMZZ3qIUDhNrLZqc%2BesERePbsrtM4CXgg122327Id4IU7KH%2F7VpQvTCoBt1myfa4dVQZRG5U7ZQDkrpFFbDUxHx6VgB4Bt9F2D33qczkGh83yoMHYOaLjd2cZmW23tV70XHTt2IVwy6Rur%2FJnd7qMK2T3kNdXb%2FJxpjiP32Oc2UNMMa6%2F9IGOqUBbZ5z8LKHcg%2BHN1r0ya7LNFYL39VaQaD1pbxpP2edtMfH3l9c7oGTlhVshO2qRY344HNw3UAleQeRWCyPpbBLcXbxPAWgQ8shpjNdAK814WTCbnJNz45BfXy1%2FjdqxEZ2zdTb5kp4R6ldJFaqOfkon74ONtMhST2tCWb%2FcFRVhqS2hLpmX%2BI9uzRK9bwSUtSw6JmuKEIWNbILw4wCTypoXYjsvWIm&X-Amz-Signature=53c76e06daa0a20eba4027e4b00a294fce889dfe130c0a351d8243d145e47f7d&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

[image](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/72967571-eaee-48ee-be46-326b48a94a6d/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VZTRBEKM%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T225559Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIHAtbCp61Hqqu7tOd%2FpIUHLntWxDXV0C9PeHiBrawz33AiEAjpy1rHuuXVihDXJR2VS%2F3HNQrSU10StcWD6l5CyHVmQqiAQIxv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDNQyA5B3lJX%2FTEY63SrcAzipiNMDzKwLR7zN5NwjC2xJkU2DF%2FmtLMuvHU0vmr7cnfYKuXKorUd0YAp5r0feQCDX8XF10o4xF7%2BIZkMxOivrr4JZGyghgBIQn%2FkNU3c0LFrNrcl0xwGtYnjaFCBYmJEQ1QlUMVQgH95TtltdEije5gD8sVPfvYJr8cfpSh6vwRiV7u0KzcpcRHuTLLuu%2BJ5AoZkznOylVq0Bsqv%2BM4YQOxuk9yxW%2F9T5lcloe0N4QnCoe0sLSTMKnGjeLdst0SYeTnqMf0ph9GcsT9UGZDA9mJ%2BBJjvtZG1HLhc2xyy3L2mT9gIKeKYi0UEk%2BpqkuYyfJnmwr3kFVvFiIH5Rrlql%2Bj0sfj5R91TnpScT4vS5FCWoKm3QtMfpuuViWJCIH3kjOaGrqiE%2BScxMQmThB6k%2FkkC%2B4a%2FkmI%2FdytUYIv8kodnUMkUuLb3GUkXtkQ7TTK%2F9akTrinBBFpjQHMZZ3qIUDhNrLZqc%2BesERePbsrtM4CXgg122327Id4IU7KH%2F7VpQvTCoBt1myfa4dVQZRG5U7ZQDkrpFFbDUxHx6VgB4Bt9F2D33qczkGh83yoMHYOaLjd2cZmW23tV70XHTt2IVwy6Rur%2FJnd7qMK2T3kNdXb%2FJxpjiP32Oc2UNMMa6%2F9IGOqUBbZ5z8LKHcg%2BHN1r0ya7LNFYL39VaQaD1pbxpP2edtMfH3l9c7oGTlhVshO2qRY344HNw3UAleQeRWCyPpbBLcXbxPAWgQ8shpjNdAK814WTCbnJNz45BfXy1%2FjdqxEZ2zdTb5kp4R6ldJFaqOfkon74ONtMhST2tCWb%2FcFRVhqS2hLpmX%2BI9uzRK9bwSUtSw6JmuKEIWNbILw4wCTypoXYjsvWIm&X-Amz-Signature=982c970ef4cb5dbc8289bbef6d72a93741306c69e75da008172d13d8a98086df&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

这里第一步先加一个施工标师叫 fix me 等待份章节再来简化。好，这里施工标识在这里打一个下面这里打一个。那同学们不要说老师写烂代码，是因为咱还没有学到后面的黑科技，那这里只能用比较繁琐的方式来做了，那接下来就要对这个服务进行一个改造了，咱现在要调用的是 address service 里面的 query user address 那好办，我们怎么做啊？咱把刚刚写过的这段代码给它 copy 过来。

[image](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/265da9f6-4644-4edf-90da-32b987a15260/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VZTRBEKM%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T225559Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIHAtbCp61Hqqu7tOd%2FpIUHLntWxDXV0C9PeHiBrawz33AiEAjpy1rHuuXVihDXJR2VS%2F3HNQrSU10StcWD6l5CyHVmQqiAQIxv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDNQyA5B3lJX%2FTEY63SrcAzipiNMDzKwLR7zN5NwjC2xJkU2DF%2FmtLMuvHU0vmr7cnfYKuXKorUd0YAp5r0feQCDX8XF10o4xF7%2BIZkMxOivrr4JZGyghgBIQn%2FkNU3c0LFrNrcl0xwGtYnjaFCBYmJEQ1QlUMVQgH95TtltdEije5gD8sVPfvYJr8cfpSh6vwRiV7u0KzcpcRHuTLLuu%2BJ5AoZkznOylVq0Bsqv%2BM4YQOxuk9yxW%2F9T5lcloe0N4QnCoe0sLSTMKnGjeLdst0SYeTnqMf0ph9GcsT9UGZDA9mJ%2BBJjvtZG1HLhc2xyy3L2mT9gIKeKYi0UEk%2BpqkuYyfJnmwr3kFVvFiIH5Rrlql%2Bj0sfj5R91TnpScT4vS5FCWoKm3QtMfpuuViWJCIH3kjOaGrqiE%2BScxMQmThB6k%2FkkC%2B4a%2FkmI%2FdytUYIv8kodnUMkUuLb3GUkXtkQ7TTK%2F9akTrinBBFpjQHMZZ3qIUDhNrLZqc%2BesERePbsrtM4CXgg122327Id4IU7KH%2F7VpQvTCoBt1myfa4dVQZRG5U7ZQDkrpFFbDUxHx6VgB4Bt9F2D33qczkGh83yoMHYOaLjd2cZmW23tV70XHTt2IVwy6Rur%2FJnd7qMK2T3kNdXb%2FJxpjiP32Oc2UNMMa6%2F9IGOqUBbZ5z8LKHcg%2BHN1r0ya7LNFYL39VaQaD1pbxpP2edtMfH3l9c7oGTlhVshO2qRY344HNw3UAleQeRWCyPpbBLcXbxPAWgQ8shpjNdAK814WTCbnJNz45BfXy1%2FjdqxEZ2zdTb5kp4R6ldJFaqOfkon74ONtMhST2tCWb%2FcFRVhqS2hLpmX%2BI9uzRK9bwSUtSw6JmuKEIWNbILw4wCTypoXYjsvWIm&X-Amz-Signature=1ef74dd05c09129f01ebc144aa457f28c6453b6838690c765418590be7b4498d&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

这段代码首先第一步这里是做什么？去用 client 拿到一个 foodie user service 好，拿到之后怎么办，我们这里要发起一个 address service 里面的调用，调用谁呢？ Query user address. 我们先来看一下这个服务，它 query user address 它的特征变量是什么？那它这里的路径是 query hs 然后有两个参数，那我们记下来了，先把 hsapi 给他这里 copy 过去。接着回来我们把这个 method 上面的 get mapping 也给它 copy 过去。那剩下的这个参数怎么办呢？参数好办，是丑了一点，但是没办法，user ID 等于我们要把它拼起来，除了 user ID 还有一个 address ID address ID 等于也是一个星。这里我们要把这两个参数怎么样给它传递进去。 a user ID 和这个 hsid 都把它放在这里，然后咱就用 rest template 发起调用了咱这个请求需要调用的 query user hs 是一个 get 请求，所以我们就调用 get for for object 好，我们这里把 URL 给传入进去，然后这个类型它返回的类型是 user address 那这里我们把上面一行注释掉，然后把这个赋值语句给它 copy 过来，这一下这一片红色就已经解决了，对不对啊？那我们把这个给他 copy 一下，接着去解救下面的这么几个方法。


同学们看到这里有几个一二三四有这么四个方法，他们都在等待着谁来解救，不是，我同学们他们都在等待着你来解救了。那老师前面已经给出了例子，那我们这里就让同学们怎么样，自己去把这些方法给他解救出来。我这里给出一个示范，剩下的服务就要同学们自己来动手了。我这先把这个作业给他打上，这个作业标识叫同学们自己改造。那下面加搭一个施工标识，这个也是让同学们自己改造。我先把这里给他注释掉，然后再给他一个负空，就是空值的语句，同样的这里也是给它复空。然后我这里去做第一个例子，我给它闪开一条空，我要大显身手了。


那咱把上面这里刚刚写好的这一段给它 copy 一下走，来到下面这个 instance 给它名字起叫 item instanceitem API 它的 client choose 这里改成 item 然后这个 URL 我们直接在这上面原封不动地改，怎么改？我们首先看和前面一样的步骤，item service 里面这个 query item spec by ID 它的路径是什么？它在 item API 下面 query query expect by ID 它在哪里？好在这它的路径叫 single item spec 我们这里回退回来，把这个 uro 替换掉，改成 single item spec 然后它有参数没有有它的参数是谁？这里 spect ID 等于后面加一个百分号 S 然后传入的参数我们要把 items spec 的 ID 传入进去。好嘞，那后面它同样的也是一个 get 请求 get for object 但它的返回值是谁？是 itemspect 同样的我们这里接收返回值的时候也要这样接收，把上面这一行注释掉。


最后一步不要忘了这个 service instance item API 它需要把这两个给它替换掉，不然的话你这个服务就发到哪里了？发到前面咱指定的这个 user service 码，那它会报错的。做完这一番改动之后，世界瞬间就清净了。那老师的世界清净了，同学们的世界会比较忙。为怎么说这里作业，同学们你不做好作业，这个服务接口是调不通的。有同学说我不想做作业好麻烦怎么办，老师给你们指条明路，等下一周我们学习到份章节以后，这些代码同学们看，咱新写的这些非常麻烦的代码统统不用了。


回到怎么样方式回到最开始的这种调用方式是不是很神奇啊？通过咱的 phone 组件，不需要引入任何 item service 的实现类，我只要引入 item service 的接口，咱就能怎么样呢？实现方法的调用好勒。那这两条路都给同学指出来，勤快的同学们可以在这里做作业。


那懒的同学们，就等下一周学习到份之后，我们再来改造这个 order service 那咱这个 order service 已经全部改造完成了，接下来我们去创建最后一个 module 是谁呢？那就是 order controller 我们给它起名 foodie 杠 order 杠 web 专门来放 controller next 路径不要乱，依然是 domain order finish321 走它有哪些依赖项需要加入进来呢？ 321 走我们这里看到，咱的 build 节点 main class 还没创建，但是先给它指定出来了。接着往上看都是很通用的 dependency 引入了 order service 后面是 web component 以及 eurika 的依赖。


好，我们接下来从头开始创建，在 Java 里面创建一个 package com.imock.order 在这个里面咱先把它的启动类给它传递进来，启动类给它复制过来，我们从 item application 直接 copy 一份，给它改名叫 order application 在这里有这么几个地方需要改的一个是 mapper scan 对不对？我们改成 order 除此以外，我们还有一个地方要改是哪里。别忘了咱在之前 forty DEV 里面有一个 enable scheduling 我们把它给它打开。


那接下来我们就可以去创建 controller 了，我们把这个 package 给它打上 controller 这里有哪些 controller 呢？我们去 foodie DEV 当中 copy 代码。好同学们可以看到，我这里已经把这三个 controller 给它揪过来了，分别是 order controller 以及 center 这个目录下面的 my comments controller 和 my orders controller 那我们接下来一个给它改造一下啊。


啊好先到这里，我们把这一个类主要是一些路径的问题。好，我们 321 走这里路径改完了，那咱接下来看还有哪里报错这里 create ordercreate order 怎么报错了？因为咱改了 create order 的接口签名对不对？你看他现在接口签名接收的是 place order BO 这个好办。好，我们这里直接创建出一个 BO 好了怎么创建？直接 new submit order 传入进去， shop card list 传入进去，接着把 order BO 传递给这个科瑞的 order 方法，这就完成了。


那咱接下来往下看，你看这有个变量标红了，为什么？我们点进去看，你看它不是一个 public 的访问变量，所以这里访问不到，我们把它改一下就好了。 base controller 的支付的 callback 接口，那把它这里给它改成 public 那么接下来往后看。还有，这另外一个 payment URL 也要把它改成 public 这两处改好之后这个类就清净了。
那我们接下来看剩下的两个类都是同样的方式，我们到 my orders 里面看一下，把这些上面的路径都给他改好，这应该是 order 下面的，然后这个对象引入进来。那像这里 my order service 这个方法我们要怎么样呢？因为 base controller 里面已经没有 my order service 了，它离到了订单中心，所以我们这里同样的，在这个方法里面要把这个注释给它打开，把 my order service 给它引入进来，那这里就没有几个红叉了。那咱接下来看这里， check user order 这个方法我们同样的也要通过 my order service 进行调用。再往下看，这里也是一样的，经过这么一改，就还剩这最后一个类了。 My comments. 看出来，咱首先把上面的路径全给它改好，一二三走上面，这里改好了以后，我们来看剩下的报错的这几个虾兵蟹将，咱三下五除二，把它搞定。


Check user order. 咱这是要引入谁 out where 的一个友军进来是 my order service 把他给拉进来就对了。好在上面补全它，这里也补全它，这里也，这里不能补全它了你看 my comments service 这个类里面已经没有 query my comments 这个服务了。所以我们这里要用前面学过的方法怎么样呢？把这里先变出 load balancer 和 rest template 全部都加进来走，你加进来了。


加进来以后，下面这里咱要改造了，怎么来改和前面一样的方式接下来我要变身了，我要加入一段非常丑的代码。在这里，你要问他有多丑，那要多丑有多丑，所以我得列一个牌子。前方施工，学完 thin 再来改造。那我开始了一二三走，你一大长串。首先这里拿到一个 instance foodie item service the instance 然后接下来接下来这里是调用 item comments API 的访问路径，然后把必要的参数塞进去之后发起一个访问。那这个访问是 get 形式的，同学们再忍那么几天，学完分之后咱就能把代码风格再给改回到小清新式了。那好，看起来咱所有代码的事儿都已经摆平了，那接下来就要去摆平配置文件。


配置文件最简单了，我们从前面的商品中心里面直接把这些配置文件给它 copy 一份，拿过来改哪些内容呢？第一个内容当然是咱自报家门 application YAML 里面的 application name 了，不叫 fooded order service 再往下还有一个关键的地方，mapper ，咱这个 item 要把它改成 order 好，这里就改好了。那咱接下来到 DEV 里面，这个 DEV 里面的 server port 咱们排到几了，item是1， user 是2，那咱的 order 就给它改成3。


这里改完以后，下面这个数据库同学们最好也把它改成独立的数据库。然后把相应的表在这个 schema 当中重建一下，最好结合前面学过的分库分表去 IP 把这里都给应用上配一下。那我这个 Redis 改成我本地的 local host ，然后 passport 给它去掉。那同学们自己记得，改回你自己本地的方式。


到这里，咱的订单中心已经改造完成了，小伙伴们要测试的话怎么做呢？首先咱要确保把 registry center 给它启动起来，也就是注册中心。接下来在启动订单中心之前，咱先把商品中心 item 和 user 用户中心给它分别启动起来，然后再启动订单中心，否则你先启动订单中心的话。那么他第一次在尝试做服务发现的时候，是发现不了 item 和 user 的实例的。那这时候你从订单中心发起访问到 user 或者 item 服务的时候，他将会给你报出一个 no instance 的错误，直到他去尝试下一次服务发现的时候，拉取到了 item 和 user 的实例。


那到这里，咱 eureka 的商针改造环节就告一段落了。同学们看到这里，代码只改造了 item order 和 user 三个微服务，剩下一个 cart 购物车的服务以及 search 主搜服务。那这两个服务就留给同学们课后动手了。细心的同学可能会回想起来，咱还有一个服务叫什么叫 off 做用户鉴权的一个模块服务。那这个服务稍安勿躁，他在后面的 gateway 章节才会跟大家去见面。届时我们就通过 auth 服务以及搭配网关层 gateway 提供统一的用户登录状态检测。那到这里，整个有瑞卡阶段的课程就告一段落了。同学们是不是觉得微服务学起来就是像老师说的这么简单轻松。好，那剩下的课后作业就交给大家去完成了。同学们，我们下一周在瑞本和份章节中再见。


