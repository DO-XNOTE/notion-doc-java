---
title: 3-21 可靠性消息重试实现集成定时任务组件-1
---

# 3-21 可靠性消息重试实现集成定时任务组件-1

[image](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/22d0eb72-3cbb-4653-86a1-2d72f6210184/SCR-20240807-fdwn.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QK6V7DCN%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T225312Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCID0tlwKnqKfacm4UY5G7LprkCAyJuTAKwJuVGMaB1yf8AiAj8YZ98Pzciz4ckChKDmFNTLT4LHmjxtF7fVp3KrxqXiqIBAjG%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMjZFYvulySb8uqBqKKtwDSa3sgcUP6FSojLdU5KNC7q0oUehV3gsmvHUD8TE2yYS%2FcVT7Q%2BF3LUq5Aj755iiIi9ea7RJxp44qoezkWTO7gHEGZ9KGFrMSDn3rkvidXEbfnvTnGGHzvXIdEieU1WFY2Bd8K9TvQJlm4I8VT3MBM9ZSHRnXHSxV5zqNJUlW%2FWlUQIcazUVOgQXyPoYFBw8AFnu5gJIOhJsue5yD%2F7LcGqaQ%2FZl7aIx0%2BQeXgwN%2FVdXCLulEaAst8MRMCSjzlcL9ujtMw%2By1etMC1b86aAG%2FZ5KVWmyHdX9AxCmNrnHaLjBS3KWF5t6Qrc341iwIx8g8%2B9Nd%2FBhkDWWefF3IePcX330%2BOJDrC0%2BtMNC3I5aMycWpcL1WNolgQCEqlSzF6j5G0fBI36uJIxPVMgUbyVwbQxwZ4NfMGw1APyhDU5PWULCy2As2X740XbZpqDfd6AoIh9FvYjAIqThMmkB4zNCAZxJmGZV808%2FwckVpd76pI1B2cAiyWbwyWsWxgripzxJt7hrarlIwGaOonldSpi7abH7dDoIZ1Av0NN%2BYO1j3ltTklh4PlnR6gIhs3GeS6%2B4KMtcD6nfFzF%2FeKyrGduMTlX%2FxS6COH03Z9ipGGDgYTLq%2FsmAoQiGZqpva8%2FYwy7j%2F0gY6pgGuY6yuJScSwZoI7b7pgsrcivan%2FCy7t7HxWWHT2z%2BZg04LuAwyQKfTTI%2F3X8HEgQ1HDoKVf8UgVnRjc4fcmE7ITu%2B%2Bo2JuJGu4DE%2BmteVgs6C1U3KiTZXrI4LKOvQb%2BCDCp8SOxWFwFTKNGfW2xW1JyblEijhCAU9tBQ%2Fj%2BGPhXdDLpt2KfOfs4xTMZ0JQniJ27FuJx69zCMx2O0X6IuwkUqjWft59&X-Amz-Signature=dfc8969efa171d315b692b5b034525a3d0dd8b48bcffb171cebb51fa693e1cb6&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

[image](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/4eb83b54-81d4-4736-814d-2803c87663e5/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QK6V7DCN%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T225312Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCID0tlwKnqKfacm4UY5G7LprkCAyJuTAKwJuVGMaB1yf8AiAj8YZ98Pzciz4ckChKDmFNTLT4LHmjxtF7fVp3KrxqXiqIBAjG%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMjZFYvulySb8uqBqKKtwDSa3sgcUP6FSojLdU5KNC7q0oUehV3gsmvHUD8TE2yYS%2FcVT7Q%2BF3LUq5Aj755iiIi9ea7RJxp44qoezkWTO7gHEGZ9KGFrMSDn3rkvidXEbfnvTnGGHzvXIdEieU1WFY2Bd8K9TvQJlm4I8VT3MBM9ZSHRnXHSxV5zqNJUlW%2FWlUQIcazUVOgQXyPoYFBw8AFnu5gJIOhJsue5yD%2F7LcGqaQ%2FZl7aIx0%2BQeXgwN%2FVdXCLulEaAst8MRMCSjzlcL9ujtMw%2By1etMC1b86aAG%2FZ5KVWmyHdX9AxCmNrnHaLjBS3KWF5t6Qrc341iwIx8g8%2B9Nd%2FBhkDWWefF3IePcX330%2BOJDrC0%2BtMNC3I5aMycWpcL1WNolgQCEqlSzF6j5G0fBI36uJIxPVMgUbyVwbQxwZ4NfMGw1APyhDU5PWULCy2As2X740XbZpqDfd6AoIh9FvYjAIqThMmkB4zNCAZxJmGZV808%2FwckVpd76pI1B2cAiyWbwyWsWxgripzxJt7hrarlIwGaOonldSpi7abH7dDoIZ1Av0NN%2BYO1j3ltTklh4PlnR6gIhs3GeS6%2B4KMtcD6nfFzF%2FeKyrGduMTlX%2FxS6COH03Z9ipGGDgYTLq%2FsmAoQiGZqpva8%2FYwy7j%2F0gY6pgGuY6yuJScSwZoI7b7pgsrcivan%2FCy7t7HxWWHT2z%2BZg04LuAwyQKfTTI%2F3X8HEgQ1HDoKVf8UgVnRjc4fcmE7ITu%2B%2Bo2JuJGu4DE%2BmteVgs6C1U3KiTZXrI4LKOvQb%2BCDCp8SOxWFwFTKNGfW2xW1JyblEijhCAU9tBQ%2Fj%2BGPhXdDLpt2KfOfs4xTMZ0JQniJ27FuJx69zCMx2O0X6IuwkUqjWft59&X-Amz-Signature=1dd3af3979d75e350f1a8638d026194efb8601290f79bb4c94043717f3c66590&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

那么上一节课呢，我们已经把整个的这个 elastic job 这个基础组件已经封装好了，那么这节课我们继续来去做这个高可靠性的社会投递的 ready 和 q 这个组件。好了，那我们来简单的回忆一下我们之前对于这个 rap MQ 可靠性投递，我们都做了哪些事情。首先比较关键的一个类就是我们的这个 producer 点 broker 这个包下面有一个 producer client，那这个 producer client 这个类它其实实现了我们这个 message producer 最上层的 API 的这个接口，然后它提供了 3 个 send 方法。第一个就是说正常的 send 方法，然后根据 message 里边的这个 message type 去判断到底要发什么样的消息，要么是这个迅速消息，要么是我们 config 消息，要么就是我们的这个确认可靠性的消息。OK，然后下面两个方法老师没有去写，一个是批量发，还有一个是带一个回调函数的，OK，好在我们之前讲到了这一块，然后中途我们插入了这个 elastic job 这个知识点。


好了，我们回过头来，大家来捋一捋思路。首先我们来看这个消息它到底是怎么去发的，我们随便点进去一个，比如说点到我们的这个 confuse message，它的这个实现叫做 Rabbit broker implements。来看一下，那它呢？总是发这个客人消息，发客人消息就调这个客人的这个方法就是 send cream。然后呢去从什么呢？去从我们的这个 Rabbit template container，然后点 get template，取到具体的模板，然后调用 convert and send 方法去发出去了。那如果是可靠性消息，它可能先不是说掉坑方法，而是先把消息做一个持久化，做一个存储，那存储内容就是我们的 broker message，然后存储成功以后再去进行上的客人方法的发送。OK，那这是我们之前所讲到的知识点。


然后我们回过头来看这个 Rabbit template container，那它其实主要就是实现了一个叫做 Rabbit template，点 confirm call back 这个方法，它会重写一个 confirm 肯定方法，当消息发成功的时候去 update 一下我们的数据库，就是把我们这个叫做 message 到service，然后点 success 根据 ID 去更新一下我们具体的那个记录，把它更新成已发送。


如果说发送失败，或者是说由于一些其他情况网络闪断，导致我们没有更新成功的话，那怎么办？那接下来就需要进入一个补偿，我们回过头来看我们这个具体的数据库表结构，大家可能就知道我们之前讲的内容了，在这简单复习一下。看这个表结构，那它如果发可靠性消息成功的话，它会 insert 一条记录。然后最主要的就是这个 try count states，还有一个 next retry 是什么意思？就是说我们第一次音色成功之后，我会把这个 state 制成为0，表示说待确认的状态，就是已发送待确认，然后 next try 的时间会根据我最大容忍的这个超时间，然后通过我的定时任务会扫出来，那我们在这里设置的是什么呢？ next retry 的时间应该是设置的是 1 分钟之后，我记得之前这个值就是当前时间加上一个 1 分钟，如果你还不给我把这个状态从山顶状态更新成 3 的 OK 的状态，就会变成我们的这个0，变成 1 的话，那我就认为你有问题了，然后我就期望我有定时任务，当然后面可能就是说我们之前做的这个分布式的定时任务去把它补偿回来，让我去做一个重发的机制。


然后这样的话我们就能够实现就是可靠性的消息，土地为了防止这些中间状态导致消息不可达的这种情况，那接下来我们就开始进入这个集成，我们上几节课所讲的这个 elastic job 这个基础组件，然后把这个 producer 来封装好。那OK，那在这封装之前，其实我们上节课落了一点点小事情，就比如说我这个message， message 里边有一个字段，叫做这 4000 长度的一个 message 消息的全量信息，那这个全量信息需要做一个什么序列化？那老师怎么去序列化？我们来看老师的序列化方式，就是把这个 message 现在还没有去提到这个序列化，那也就是说我们现在存储的这个消息是一个什么消息？它有ID、有state、有 next retry，然后这个 message 它目前就是一个什么呢？就是一个普通的message。


那么正常的写法，我比如说把它转成一个 JSON 的字符串，然后让他帮我去做一个序列化，就是这里边转成一个 JSON 字符串。但是其实我们在这里我能不能把消息进行买贝斯，进行这个持久化的时候，然后我设置一个自动这个序列化的过程，这是可以的。其实我们可以观察，即使老师之前粘过的这个 mapping 里边，我们引入了一个小的这个插件，我们可以打开最大化。我们看到这里边就是比如说Y64，在我音色的一条这个 broke message 时候，对于这个 message 我做了一个处理，这个 message 我做了什么处理？叫做 type handler，等于COM，点 b f x y，点common，点 my basis，点handler，然后叫做 message Jason type handler，然后把我们具体的这个对象直接帮我去转成一个Jason，就是说我会有这么一个类。


好了，那他既然是在这个 common 包下，那我就把这个 Ctrl c 粘一下，然后呢我现在找到我们的 common 类，在这块呢我们直接新建一个package，然后分离是这个代码，我们就直接粘过来了，我就不领着小伙伴们一点点去写了。然后他可能还需要一个什么呢？还需要一个我们填进去 fast Jason convert 就是一个util，那我们来看它是在 util 包下，所以说在这里老师再加一个新的package，然后这里边叫做点斯条，然后把我们这个 fast DISN convert util 粘过来，这样的话我们这一块就没有问题了，那我们来简单来看一看这里边代码什么意思？我现在用的就是这个阿里巴巴的这个 fast Jason，基本上就将 Jason 字符串转换成实体对象，将一个字符串转换成一个 Java 的plus，然后当然肯定有将一个什么，将一个 Java 的 class 或者是一个 object 转成一个JSON，将一个 object 去 to JSON three，这是没问题的。


然后那我们主要观察一下，就是刚才我们所说的这个Mybatis，它的这么一个 JSON type handler，那它呢？其实是 Mybasis 里面给我们提供的。

这个如果说对 Mybasis 比较熟悉的小伙伴应该知道，就是有一个 my betas 里边有一个叫做 base type handler，然后你传进来什么对象，我帮你去做什么序列化。这里边就是我充分的去利用了我们的这个刚才大家看到的这个阿里巴巴的这个 fast Jason， what you tell 去做处理，因为我数据库里面存的不可能是脏话，对象存的肯定是一个字符串，然后我会把什么呢？把一个字符串去帮你转成我们自己的这个class，看见了吗？叫做message，就是我们具体的这个消息的class，就是把一个 Jason 字符串帮你转成一个 Java 的对象，然后同理肯定后面还有帮你去做其他的相关的一些转换，OK，还有就是这个 set 对不对？那我把一个 Java 的这个对象帮你去序列化成一个 Jason 的格式，然后去做一个存储，就是 set not parameter。


好了，那这个整个的这个工具类呢？我同学们课下自己去看一下，因为这个是买班次给我们提供的，所以说我们把这个小环节补上，基本上我们就可以去继续往下去走了。上几节课，我们对于这个基础组件的这个 Rabbit task 进行了一个封装，那我们现在是不是可以把这个插件引到这个我们的 Rabbit call producer 这个里边？可以把这个炸包，那我们来做一下，那这个炸包，那其实跟我们之前所学习的差不多，直接迪潘尼斯依赖。


我们之前引的是common，现在引的是什么呢？现在引的就是我们的 task 这个包了，然后保存好，对吧？现在我们的这个 producer 已经具有我们的这个 elastic job task 这功能了。然后接下来我们回忆一下，就是我们自己封装的组件怎么去集成来着。


首先第一件事情，你要有 ZK 配置，有 ZK 配置证明你要配置到 application 点 practice 这个文件里。但是同学们想一下，我这个靠producer，它本身它也是需要被别人引入进去的，我也需要做一个 auto where 的，因为它里边肯定是没有 application 加properties，只有最外边使用的那个类才会有 application 加practice。


所以说对于 ZK 的配置我们暂时不去管，还有哪些配置我们需要管呢？比如说最关键的有一个叫做 enable elastic job，是不是我可以在这个靠谱 user 里边？我先把它写好了，就我不用业务方去想了，这是 G1 或者其实这个类你也可以放到最外面，这个都可以，看你怎么去想。然后做完这件事情之后，剩下的那件事情就是我们要自己去定义一个job，然后根据你自己实际的业务逻辑，你可以去编写你自己的这个 job 就好了。那在这里我们起一个名字，比如说我们在这里起一个新的包，咱们叫做task，这个 task 包我们已经起好了，然后我们给它起一个名字。**那现在同学问知不知道我们要做什么事情？我们需要实现可靠性投递，当我们的消息如果说发送到扑克博客端给我们回送响应的时候，给我们回送响应，那个过程中如果说网络出现闪断，或者是说有些其他原因导致我们没有收到那个博客给我们的ACK，也就是说我们没有更新成功。**


**数据库里边状态就是还是三丁的状态，如果超过我们的这个 Max size，就是超过我们最大的容忍的时间了，然后我们就会做定时任务的重试，在这里我们就选择我们之前所用的这个分布式定时任务 elastic job 自己封装的这个组件，然后做重试，那我在这里给它起个名字，我们叫做 retry message。**


**那这个里面我们选择什么样的定时任务比较合适呢？是选择简单的这种定时任务，还是说选择一种其他的定时任务？其实一般来讲我们会需要做什么事情？我们会需要把状态等于 3 顶，并且超时的就超过了我的最大的容忍时间的数据先抓取出来之后，然后第二步做什么事情，再去做重试，这样去把它重新做投递。其实整个这个过程分两步，第一步怎么去抓取我们要做重试的数据，第二步怎么样把数据再重新发到 MQ 上，这是两件事情。**


当然你用 simple job 也可以，但是老师在这里因为我们精装了 3 种 job script job 我们说用的比较少，但是我们 date flow job 我们还没有跟同学们去演示，所以说在这个 demo 里用我们的这个 data flow job，跟同学们一起把这个功能去实现一下 data flow job，所以说我们自己在这里定义的一个定时任务就叫做 data flow job 了。


然后这个 data flow job 它一定要实现一个接口，就是我们当网的这个 data flow job。好，然后这里边给我们传一个t，这个 t 是什么呢？你可以认为你要抓取什么样的信息？你要抓取的信息不就是这个 broker message 嘛？然后这里边你要重写方法了，重写两个方法，第一个就是 fetch date 我要抓取什么样的数据。第二个方法就是 process date 执行，就是它会把抓取出来的这个集合返回，然后并把这个集合输送给下一个 process date 里边的一个参数，然后我们去一批一批的去处理这些数据，那说白了就是说第一件事情我们要从数据库里抓出来符合我们预期的，也就是说已经超时的就是没有被确认的消息，然后再重发回去。


当然写这个时候，首先第一步你要做一个艾特component，把它注入给super，然后接下来应该加你自己的 elastic job config 注解，对吧？因为我们已经跟我们自己的这个封装的组件集成了，所以说在这里首先第一个name，这个 name 我一般愿意去做的事情就是权限命名，这样的话我能区分说这个出现重名的情况就是名字类名一致的，那我可不可以通过包去区分？然后接下来课上表达式，课外表达式我们可以去随便去写，比如说我们除以 10 秒钟执行4，可以 10 秒钟执行次，然后是 4 个星一个问号表示任何时间 10 秒钟一次。然后接下来我们可以去做一个描述 description 可靠性投递消息补偿任务，可以，然后往下去走，比如说它override，就是是否覆盖，比如说它是否覆盖我们的这个 ESR 覆盖，还有一个 sharing to the count，这是最关键的。在这里我先写成1。

```java
package com.bfxy.rabbit.producer.task;

import com.bfxy.rabbit.producer.entity.BrokerMessage;
import com.bfxy.rabbit.task.annotation.ElasticJobConfig;
import com.dangdang.ddframe.job.api.ShardingContext;
import com.dangdang.ddframe.job.api.dataflow.DataflowJob;
import org.springframework.stereotype.Component;

import java.util.List;

/**
 * <h1></h1>
 */
@Component
@ElasticJobConfig(
        name = "com.bfxy.rabbit.producer.task.RetryRetryMessageDataflowJob",
        cron = "0/10 * * * * ?",
        description = "可靠性投递消息补偿性任务",
        overwrite = true,
        shardingTotalCount = 1

)
public class RetryRetryMessageDataflowJob implements DataflowJob<BrokerMessage> {
    /**
     * 获取待处理数据.
     *
     * @param shardingContext 分片上下文
     * @return 待处理的数据集合
     */
    @Override
    public List<BrokerMessage> fetchData(ShardingContext shardingContext) {
        return null;
    }

    /**
     * 处理数据.
     *
     * @param shardingContext 分片上下文
     * @param data            待处理数据集合
     */
    @Override
    public void processData(ShardingContext shardingContext, List<BrokerMessage> data) {

    }
}
```

有，就是老师，那这种分布式定制任务，我应该怎么去设置这个 sharing total counts 呢？我们现在作为演示，我给大家演示的时候，**我现在可能就这一张表，然后只是针对于这一张表做我们的这个定时任务做重试。就是说我们的定制任务轮询，总是轮询的这一张表，**

```java
-- 表 broker_message.broker_message 结构
CREATE TABLE IF NOT EXISTS `broker_message` (
  `message_id` varchar(128) NOT NULL,
  `message` varchar(4000),
  `try_count` int(4) DEFAULT 0,
  `status` varchar(10) DEFAULT '',
  `next_retry` timestamp NOT NULL DEFAULT '0000-00-00 00:00:00',
  `create_time` timestamp NOT NULL DEFAULT '0000-00-00 00:00:00',
  `update_time` timestamp NOT NULL DEFAULT '0000-00-00 00:00:00',
  PRIMARY KEY (`message_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
```

**但在实际工作中表不可能是一张，如果是一张的话，你对这个磁盘，就对你的这个 IO 你的性能提不上来，一共就一张表，所以说你可以搞很多张表，其实这个设计按你的想法来就可以了。我们现在其实可以说设置成一张表就满足我们的需求了，因为其实我是相当于把这个 rabate producer，这个 producer 会依赖我们具体的一个项目，相当于会被这个项目引进去，然后在这个项目的基础之上，我们去创建一个schema，创建的一张这样的表。**


比如说这这个表现在是跟着项目走的，一个项目里边可能就一张这个 schema 这张表，然后我们定时任务分片策略，其实我们设置 1 就够了，因为我们一个项目里边有一张这个 broker message 这张表就可以了。那如果后面如果你想去做一个很通用的东西，你说我这个表不跟着一个项目去走了，那你肯定要做分红分表策略了。你比如说你设置多少张表，设置几十张表或者是 100 张表，然后那你的这个 sharing total count 你自己也要去合理的去划分。比如说 100 张表可以设置 10 个分片，是不是一个分片处理卖 10 张表？OK，那这样就是起到作用了。


所以说在我们这个设计的这个过程中，因为我们的每一张表都是跟着每一个项目、每一个工程去走的，所以说在这个工程所对应的这个 DB 数据库里边，就会帮我们产生一张这个 broker message 的这种表，所以说我就没必要去再对它做 sharing 了，在数据库里加一些 where 条件，那这个就也可以去做到。好了，那在这里我就废话不多说了，我们一起来看一看这个东。

