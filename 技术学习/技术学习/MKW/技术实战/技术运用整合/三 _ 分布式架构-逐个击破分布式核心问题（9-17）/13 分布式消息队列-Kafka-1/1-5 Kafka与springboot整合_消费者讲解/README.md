---
title: 1-5 Kafka与springboot整合_消费者讲解
---

# 1-5 Kafka与springboot整合_消费者讲解

[image](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/6e88fd63-321c-4ee9-a331-681f3c74daab/SCR-20240807-gagq.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466356CD2Y6%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T225322Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDYrdy5JXDwal2XgWwVNbogizoGs74tQW9Z7%2F%2B4G0za8gIhAK2v85xgko1g0B7r5x%2FMKN50rGBPE5iGDyUSbHvijcfaKogECMb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgyPSwyecFFhSOgKFC8q3AOpoRkyo92xYBF1SiW6rqabT6YTUdABDM2xI2ay2Vf8fRn25U7XDfr0O5CgYrS2PnazR9DURfq9km0KosgpGm00kOr0bvP7ZOh75%2FWhSB2ifpkkV2MTeNnKSvLEGvn%2BSLLOThCNQHaXfz30dINxNu1LEMCaq9iwE2DzOfVE%2B1kQGsR3AnsBmTrAtk5troaVTpiy2H0tBfW6qRy%2BXvz41KbFGWx96HEGfAuIbyw1LG1geRuaVtZeRHpeSNt4utwHFmaAJLwKqxOTx%2FDgvMxNCcHIAmAQZH%2BdO2nHAN8vpT1Y3g1MwxkfyuqPj2DPlCLtj%2FIOzbA%2BLZ4OKBw6E9R%2BzW3TNtrwK%2BvQS7gNIjMjnHZW3OVBi8VZV5IKo54nujauD3Yt1WRnGg6u6n4bL2KqFFkmMsg9L9KN7SzzbyV7JA%2FY6Dpxfs33RX6LCbZt7X2lupFD8G7%2FCV%2FAZgkskw2yW7iAX9T00hW14FXvFxn7aTT5KaDKfYyOIyw1UvpafqPNBaNiTFwPm6r3LfrtFpgIm1DoVRe23duzg971cBSK%2FQztboe3cdycHNcB257BvXLxyvyk2TA%2F%2Bg%2FKmTk7sZww0XstdLfSqSWrFiiF2zJbwdjraC43nFhXCECsQeIt4jCjuP%2FSBjqkAfi4%2FyaN9a1DNrhvGAK0CMSfuyQXWUZgW%2FuReTQGpb6ufsLC8GVlVi8UX4656VThWShC6Ol52wD7RyfgHgQ0KxxVsiJwW1AUIrjUvI6tR0rS9xVYxjydTTYV%2BKuvRuYfLM2yXAYvM0F4TKOtfXYgxQ8njJNgQ6AXz9yxq5kC%2Burx5goMEUZaVhjnSaBNGg49cM83MUweBtt4TGVQBPTalbSIvo5z&X-Amz-Signature=0c32689f727d650cf98a3d25924337ad56f18d5edbf20b359e8cff40166bb8fa&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

[image](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/33c88d2a-8437-4890-b797-c07dbaba5bac/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466356CD2Y6%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T225322Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDYrdy5JXDwal2XgWwVNbogizoGs74tQW9Z7%2F%2B4G0za8gIhAK2v85xgko1g0B7r5x%2FMKN50rGBPE5iGDyUSbHvijcfaKogECMb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgyPSwyecFFhSOgKFC8q3AOpoRkyo92xYBF1SiW6rqabT6YTUdABDM2xI2ay2Vf8fRn25U7XDfr0O5CgYrS2PnazR9DURfq9km0KosgpGm00kOr0bvP7ZOh75%2FWhSB2ifpkkV2MTeNnKSvLEGvn%2BSLLOThCNQHaXfz30dINxNu1LEMCaq9iwE2DzOfVE%2B1kQGsR3AnsBmTrAtk5troaVTpiy2H0tBfW6qRy%2BXvz41KbFGWx96HEGfAuIbyw1LG1geRuaVtZeRHpeSNt4utwHFmaAJLwKqxOTx%2FDgvMxNCcHIAmAQZH%2BdO2nHAN8vpT1Y3g1MwxkfyuqPj2DPlCLtj%2FIOzbA%2BLZ4OKBw6E9R%2BzW3TNtrwK%2BvQS7gNIjMjnHZW3OVBi8VZV5IKo54nujauD3Yt1WRnGg6u6n4bL2KqFFkmMsg9L9KN7SzzbyV7JA%2FY6Dpxfs33RX6LCbZt7X2lupFD8G7%2FCV%2FAZgkskw2yW7iAX9T00hW14FXvFxn7aTT5KaDKfYyOIyw1UvpafqPNBaNiTFwPm6r3LfrtFpgIm1DoVRe23duzg971cBSK%2FQztboe3cdycHNcB257BvXLxyvyk2TA%2F%2Bg%2FKmTk7sZww0XstdLfSqSWrFiiF2zJbwdjraC43nFhXCECsQeIt4jCjuP%2FSBjqkAfi4%2FyaN9a1DNrhvGAK0CMSfuyQXWUZgW%2FuReTQGpb6ufsLC8GVlVi8UX4656VThWShC6Ol52wD7RyfgHgQ0KxxVsiJwW1AUIrjUvI6tR0rS9xVYxjydTTYV%2BKuvRuYfLM2yXAYvM0F4TKOtfXYgxQ8njJNgQ6AXz9yxq5kC%2Burx5goMEUZaVhjnSaBNGg49cM83MUweBtt4TGVQBPTalbSIvo5z&X-Amz-Signature=ecbc34f6b00e0f53af3d783195648a106f41057aa26c565002bb0c5479a36051&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

[image](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/1c4ed670-a6bf-4705-bd0a-bcbd27076249/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466356CD2Y6%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T225322Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDYrdy5JXDwal2XgWwVNbogizoGs74tQW9Z7%2F%2B4G0za8gIhAK2v85xgko1g0B7r5x%2FMKN50rGBPE5iGDyUSbHvijcfaKogECMb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgyPSwyecFFhSOgKFC8q3AOpoRkyo92xYBF1SiW6rqabT6YTUdABDM2xI2ay2Vf8fRn25U7XDfr0O5CgYrS2PnazR9DURfq9km0KosgpGm00kOr0bvP7ZOh75%2FWhSB2ifpkkV2MTeNnKSvLEGvn%2BSLLOThCNQHaXfz30dINxNu1LEMCaq9iwE2DzOfVE%2B1kQGsR3AnsBmTrAtk5troaVTpiy2H0tBfW6qRy%2BXvz41KbFGWx96HEGfAuIbyw1LG1geRuaVtZeRHpeSNt4utwHFmaAJLwKqxOTx%2FDgvMxNCcHIAmAQZH%2BdO2nHAN8vpT1Y3g1MwxkfyuqPj2DPlCLtj%2FIOzbA%2BLZ4OKBw6E9R%2BzW3TNtrwK%2BvQS7gNIjMjnHZW3OVBi8VZV5IKo54nujauD3Yt1WRnGg6u6n4bL2KqFFkmMsg9L9KN7SzzbyV7JA%2FY6Dpxfs33RX6LCbZt7X2lupFD8G7%2FCV%2FAZgkskw2yW7iAX9T00hW14FXvFxn7aTT5KaDKfYyOIyw1UvpafqPNBaNiTFwPm6r3LfrtFpgIm1DoVRe23duzg971cBSK%2FQztboe3cdycHNcB257BvXLxyvyk2TA%2F%2Bg%2FKmTk7sZww0XstdLfSqSWrFiiF2zJbwdjraC43nFhXCECsQeIt4jCjuP%2FSBjqkAfi4%2FyaN9a1DNrhvGAK0CMSfuyQXWUZgW%2FuReTQGpb6ufsLC8GVlVi8UX4656VThWShC6Ol52wD7RyfgHgQ0KxxVsiJwW1AUIrjUvI6tR0rS9xVYxjydTTYV%2BKuvRuYfLM2yXAYvM0F4TKOtfXYgxQ8njJNgQ6AXz9yxq5kC%2Burx5goMEUZaVhjnSaBNGg49cM83MUweBtt4TGVQBPTalbSIvo5z&X-Amz-Signature=544679572f1b0f73e092d73140f2e71e2cec3e0bce3106b02e2b1fe850406286&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

OK 小伙伴们。那么接下来我们继续来编写卡斯卡斯这个 consumer 也就是说服务的这个消费者。那首先我们来创建一个这个 package 咱们叫做点儿 consumer 然后在写这个 consumer 之前，我们再来创建一个我们的这个 application 点儿 practice 这个文件，我们先弄一个拜吧，什么叫做 application.properties 那么我们来看一看这个关于服务的这个消费者，他的这个 practice 应该怎么去写。那首先如果你想要的话就是 screen.sorry 就是 server server.contains pass context pass so late contact pass 我们叫做杠consumer 。然后接下来我们来说这个 server.point 是吧，points之前那是8001。那这个我就写 8002 搞定了之后，我们来看一看关键的这个 consumer 需要配置什么。



首先第一点就是一样的，无论是生产者还是消费者，你使用卡夫卡，你都得要知道它的集群地址是不是。所以说一定要有卡夫卡的它的一个集群地址，也就是说 bootstrap service 等于幺九二点幺六八点幺幺点五幺，然后等会二十九零九二。然后接下来我们看一看这个 consumer 那 consumer 我们应该怎么去配呢？首先有一个非常关键的概念，就是说它是不是需要它的签收方式应该是怎么去做？就是说就是我们的这个 consumer 就是消费端，它的这个消息的签收机制什么意思？就是我们的消费者把消息消费完了之后，他应该签收，应该选择什么呢？应该选择手工签收，简称就是说需要你去做 ACK 那这个怎么去做呢？很简单，它需要有三个配置。


第一个配置就是我们的卡夫卡。然后注意这里边就是我们的点 consumer 翻译里面看有一个什么 all to commit interval 就是这个是什么？只有自动签收的时候这个参数配置项才生效，就说你看它表示什么呢？表示说你的 all to commit 如果是 set true 的时候对不对它才生效。**那我们这个还需要配吗？其实这个你是不需要配了，因为我们在实际的工作中都是选择什么呢？都是选择手工签收，然后消息消费失败的时候，我们可以再做重试等等一些策略**。所以说我们的 consumer 它的重试的策略我们一定要选择什么呢？我们要选择第二 enable auto commit 等于什么 false 一定要等于 false 就表示我们要手工签收。这是第一步。

```java
server.servlet.context-path=/consumer
server.port=8002

spring.kafka.bootstrap-servers=192.168.13.210:9092,192.168.13.211:9092,192.168.13.212:9092
# Consumer消费端签收的机制：手工签收 ,实际工作中都是手工签收
spring.kafka.consumer.enable-auto-commit=false
spring.kafka.listener.ack-mode=manual

# 该属性指定了消费者在读取一个没有偏移量的分区或者偏移量无效的情况下该作何处理：
# latest（默认值）在偏移量无效的情况下，消费者将从最新的记录开始读取数据（在消费者启动之后生成的记录）
# earliest ：在偏移量无效的情况下，消费者将从起始位置读取分区的记录
spring.kafka.consumer.auto-offset-reset=earliest
## 序列化配置
spring.kafka.consumer.key-deserializer=org.apache.kafka.common.serialization.StringDeserializer
spring.kafka.consumer.value-deserializer=org.apache.kafka.common.serialization.StringDeserializer
# 消费者消费的并行度
spring.kafka.listener.concurrency=5
```


第二步是什么呢？第二步它有一个非常关键的配置，就是说我们具体 consumer 如果是手工签收的情况下，它有一个listener ，我们来先把这个配置项先写上，就是 spring 点卡夫卡，点这个就不是 consumer 了，而是点 listener 看这 listener 有一个叫做 ACK count 就是说最大的这个签收可以签收多少条记录，还有什么 ACK time 等等。
其实最关键的就是它有几个选项，我们看有好多选项我们选择什么 menu 就是说手工签收这个一定是非常关键的。再往下还有哪些比较关键的配置项呢？比如说卡夫卡，他对于 consumer 这块有几个，比如说消费的进度对不对？那其实如果说大家对那个 rocky MQ 了解的话， roka MQ 里边有好多好多这种消息消费的一些进度。它有一个叫做 auto offset reset 这个参数应该设置成什么呢？我们来看它有四个选项，我们一般常用的这肯定不是难了对不对？常用的是什么？常用的是这个叫做 last 跟这个 allist 那我们选哪个呢？一般来讲我们会选这个。


第一个就是 allistok 默认情况下是 last 那在这里我把这两个偏移量它的这个区别跟大家来说一说，我把这个配置直接粘过来，大家可以读一读是不是注意这个字符集我应该设置成u8，就说该属性指什么呢？指消费者在读取一个没有偏移量的分区或者说偏移量无效的情况下，应该怎么去做处理。


首先第一个就是我们的这个 last 它是默认的情况下，在偏音量无效的情况下，消费者将从最新的记录开始读取。当然肯定是在我们的这个消费者，也就是说我们的 consumer 启动之后才生成的记录。然后第二一个就是说我们的这个 Alice 它表示什么？在偏移量无效的情况下，我们的消费者将从起始位置读取分析记录。


那在这里我就选 allistok 那继续我们来看一看还有哪些比较关键的配置。那这些关键的配置无非就是序列化的配置是不是序列化配置？序列化配置大家应该都非常非常熟悉了，所以说老师在这里敲了，直接写就是对应着卡夫卡的 KV 怎么去对序列化的处理？我们来看一看都是使用这个 string 的 serializer 和这个 serializer 好了，那我们来看一看继续往下还有哪些，比如说你的消费者他的这个并行度应该怎么去设置？就是说我的线程应该起多少个？就是在监听器可以运行多少个线程数量它其实是一个线程池去做的，对不对？那我们再看 listen 这一块其实还可以配置一个东西，就是它的并行度。你看这个 concurrently 我们在这里先设置 5 试试。


好了，在这其实对应着我们的 consumer 的配置已经配置完了。那 consumer 的配置配置完了之后，接下来我们就来编写 consumer 端的代码。首先我们再起一个 class 这 class 名字叫做卡夫卡 consumer service 然后我们来加一个注解，就是我们自己的这个component 。然后如果说需要日志的话，就是加上 local G 这个注解。然后接下来我们怎么去做还记得吗？我们在最开始 PPT 上说了一样的，是不是你可以自己写一个方法，在方法上去打一个注解，叫做卡夫卡 listener 看见了吗？然后这个卡夫卡雷斯那里边有好多好多配置项，我们重点关注几个配置项。


第一个就是 group idgroup ID 什么意思？就是说你的消费者组叫什么？我们可以给他起个名字叫做 group 02 可以吧。然后他又监听哪个 topic 它里边有一个 topic 那它是一个 string 的数组。如果就一个的话，那我就写比如说我就监听 top it 02 就好了。它的配置项写完了之后，我可以自己写一个方法，这个方法叫 public void 咱们叫做 on message 你可以写一个 message 这里边都可以写哪些参数呢？其实你可以遵循它的这个 message 就是 sprint message 的这个，你可以写什么 play load 、 header 等等。但如果你不习惯的话很简单，你就这样去写。


你想一条消费，它最开始有一个 consumer record consumer record 还有 consumer record 私，我们先用这个就是单条记录消费。我们的 key 比如说是一个字符串， value 就是一个 object 然后它叫记录，我们可以写到 recall 的第二个参数。既然你选择手工 ACK 所以说你手工 ACK 你怎么去做？它里边有一个 acknowledgment 我们来 ACK acknowledge knowledgment 这里你看它有一个签收的模型，还有一个具体的接口 acknowledgment 我们来注意它是真正的去对 ACK 做设置的。


还有一个参数，这个参数叫什么呢？这个参数就是说如果说你想去获取一些对应着 consumer 的信息，也可以把这个参数拿过来。consumer ，这个 consumer 应该选这个。然后它的这个 key 和 value 都不是固定的，我们不知道，我们就用问号代替。然后我们写一个 consumer 好了，搞定。那我们这个方法就已经写完了。这个方法写完了之后，我们做什么事情如何去？就肯定是消费消息。消费消息就是它的 value 其实就是对应的那个消息内容了，这有个 value 这个 value 就是我们的实际的消息内容，在这里我可以去接收一下或者打印一下都可以。那在这里我就简单打印一下。比如说我们既然用这个 log 我们就去做一个打印。 [log.info](http://log.info/) 就是说消费端，接收消息的内容是什么呢？接收消息的内容一个大括号。然后把这个对应的内容放到这里边，就是他可以吧，打印一个日志以后，然后我要做什么事情？注意，你既然选择手工 ACK 那你必须在消费完消息之后做一个 acknowledge 的动作，这样才保证它是一个什么。手工签收必须要做一个水平吸收的机制，这样才可以，要不然的话是不行的。 OK 那其实我们对应着卡夫卡的这个 producer 以及 consumer 这块，代码已经编写完了，其实是非常简单的。那既然这样，我们接下来就要做一下测试了 test 做一下测试。那在做测试之前，老师先把这个 acknowledgment 这个 acknowledge 这句话先注释掉，就我们现在先不去做签收的动作，来看一看它是一个什么样子的。


OK 好了，那现在我们生产消费端的代码都写完了以后，我们回过头来先来看一看对应的我们的一些参数。卡夫卡里边他给我们提供了之前老师跟大家讲，说给我们提供了一些这个脚本操作，是不是我们来逐个来复习一下。在这里边我们看常用命令就好了，有创建 topic 还有查看列表。我们来先看看我们当前的卡夫卡集群里边都有哪些消息列表，在这里叫做卡夫卡杠 [topics.sh](http://topics.sh/) 然后杠杠zookeeper ，要其中连一个就好了。然后杠杠 list 看列表回车来我们看一下。


当前当然有一些历史的这个 topic 是老师之前有的。那我现在建的 topic 我们之前建的 group 是什么呢？叫 group 02，然后监听的 topic 是叫做 topic 02。 OK group 02 和 topic 02 看见了这两个。所以说其实我第一件事情要做的是什么呢？我要先把 topic 先创建出来，怎么去创建呢？在这里我们来看一看创建 topic 的它的脚本。在这里老师直接复制一下脚本，然后戴尔同学把它咱们一起阅读一下。


好叫做卡夫卡杠 [topics.ac](http://topics.ac/) 是这个脚本里边首先要连足 keeper 连完了之后要杠杠 create 就表示创建 topic 然后你的 topic 名字叫什么？ topic 名字在这里我叫做 topic 之前是 topic 1，那现在我们改成什么叫做 topic 02。然后注意后面有两个选项，第一个叫做 partition 思就什么意思，你到底这个主题下面有几个实际的 partition 那我写成两个的话，就是我们一会看的话你会看到进度，它有两个 partition 然后副本有几个呢？因为老师现在这个卡夫卡集群就一个节点，所以说我就写了一个 replication 就是一个副本。


好了，所以说就是说 topic 02 下面有两个 partition 你可以认为就是如果是对应着 rocky MQ 来讲，就是相当于 topic 下面有两个 pin 队列，这个其实卡夫卡跟 rock MQ 还是比较像的，因为它们之间对应的是我们的 rocky MQ 借鉴了卡夫卡。那这一回我再去看这个 list 大家来看一下这回这个例子里边就有一个 topic 02 了。没问题。


好了，那我们现在既然建立好了我们的指定的 topic 那接下来我们做的事情就是写一个小单元测试。比如说在 produce 下面我们创建一个 test 目录，在 test 下我们写一个 com.bfxy 点什么呢？点 Kafka 点儿 producer 点儿 test 好了，有这么一个 test 目录之后，然后我们建一个类叫做 application 这个类我们叫做 application testapplication test 4 好了，建立好了之后怎么去写一个 application test 呢？由于我们已经引入了对应的这个 test 包。所以说很简单，我们只需要做的事情就是加上这个 run with 这个注解，然后叫做 spring runner 加class ，这是第一步。


第二步就是加上 spring 的 test 注解，spring boot test 加上这个注解就可以了，非常的简单。所以说 spring boot 它帮我们简化了好多的事情，然后直接 out to where 的，谁进来直接 out where 的，我们的卡夫卡 produce service 直接奥特曼的他进来，然后复制一下，然后我们就用他去发消息就好了。在这里我们起一个方法叫做 public Y 的咱们叫做 send 这个方法。然后这里边注意它要加一个 test 注解。然后在这里我们来写代码，看看怎么去写，非常简单，那直接就叫他发消息。

```java
package com.bfxy.test;

import co.bfxy.kafka.Application;
import co.bfxy.kafka.producer.KafkaProducerService;
import org.junit.Test;
import org.junit.runner.RunWith;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.boot.test.context.SpringBootTest;
import org.springframework.test.context.junit4.SpringRunner;

/**
 * <h1></h1>
 */
@SpringBootTest(classes = Application.class)
@RunWith(SpringRunner.class)
public class ApplicationTests {

    @Autowired
    private KafkaProducerService kafkaProducerService;

    @Test
    public void send() throws Exception{
        String topic = "topic02";
        for (int i = 0; i < 10; i++) {
            kafkaProducerService.sendmessage(topic, "hello kafka " + 1);
        }
        Thread.sleep(Integer.MAX_VALUE);
    }
}
```


首先我们来创建一个 topic 主题，因为我们要发什么样的消息到哪里，那肯定是 topic 02，没什么可说的，这是我们刚才创建的是不是？然后有这个 topic 02 之后，比如说我们发送 10 次，那我就后循环 int I 的 0i 小于 10i 加写完了。好。然后我们继续调我们的这个方法，就是调我们这个 set 方法 message 首先往这一个 topic 里去扔消息，扔什么消息呢？比如说我们就扔一个字符串，叫做 hello 卡夫卡 hello 卡斯卡，然后再加上我们的 I 就好了非常简单的代码，做一个简单的测试。然后最后如果说大家想看到回调，那比如说我们在线程结束完了之后，我不让服务停掉，我可以做一个 sleep 对不对？我说 intake.max 就可以了。 max y6。然后在这里边我们往出 throws interrupter 异常。 OK 现在我们代码就已经写完了都。


那第一件事情我们需要做什么呢？首先你记得，你要注意一点什么呢？我们的列表 list 里边，我们看到是这样的，对不对？那现在我如何去看我卡斯卡的一些消息的消费进度呢？其实它有一个对应的这个脚本，我们可以把它粘过来给大家看一下来。我们看这里边就是说表示我们的卡夫卡他的 consumer groups 这么一个脚本，他能看到我们订阅的主题。好我们现在订阅什么主题了？我们订阅的 group 肯定是叫做 group 02，这个是在我们 consumer 里边已经写死了的，就是 consumer 里边我们看到这个卡夫卡 consumer service 里边 group ID 叫做 group 02。那这样的话我们现在这样直接去执行一下这脚本，它会有什么效果呢？我们来看一下执行力脚本，它会给你一个提示，说什么？ consumer group 02 doesnt exist 就不存在了。

```java
./kafka-consumer-groups.sh --bootstrap-server 192.168.13.210:9092 --describe --group group02
```

[image](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/a9fb252c-92af-4d9d-910a-774f630fef69/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466356CD2Y6%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T225322Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDYrdy5JXDwal2XgWwVNbogizoGs74tQW9Z7%2F%2B4G0za8gIhAK2v85xgko1g0B7r5x%2FMKN50rGBPE5iGDyUSbHvijcfaKogECMb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgyPSwyecFFhSOgKFC8q3AOpoRkyo92xYBF1SiW6rqabT6YTUdABDM2xI2ay2Vf8fRn25U7XDfr0O5CgYrS2PnazR9DURfq9km0KosgpGm00kOr0bvP7ZOh75%2FWhSB2ifpkkV2MTeNnKSvLEGvn%2BSLLOThCNQHaXfz30dINxNu1LEMCaq9iwE2DzOfVE%2B1kQGsR3AnsBmTrAtk5troaVTpiy2H0tBfW6qRy%2BXvz41KbFGWx96HEGfAuIbyw1LG1geRuaVtZeRHpeSNt4utwHFmaAJLwKqxOTx%2FDgvMxNCcHIAmAQZH%2BdO2nHAN8vpT1Y3g1MwxkfyuqPj2DPlCLtj%2FIOzbA%2BLZ4OKBw6E9R%2BzW3TNtrwK%2BvQS7gNIjMjnHZW3OVBi8VZV5IKo54nujauD3Yt1WRnGg6u6n4bL2KqFFkmMsg9L9KN7SzzbyV7JA%2FY6Dpxfs33RX6LCbZt7X2lupFD8G7%2FCV%2FAZgkskw2yW7iAX9T00hW14FXvFxn7aTT5KaDKfYyOIyw1UvpafqPNBaNiTFwPm6r3LfrtFpgIm1DoVRe23duzg971cBSK%2FQztboe3cdycHNcB257BvXLxyvyk2TA%2F%2Bg%2FKmTk7sZww0XstdLfSqSWrFiiF2zJbwdjraC43nFhXCECsQeIt4jCjuP%2FSBjqkAfi4%2FyaN9a1DNrhvGAK0CMSfuyQXWUZgW%2FuReTQGpb6ufsLC8GVlVi8UX4656VThWShC6Ol52wD7RyfgHgQ0KxxVsiJwW1AUIrjUvI6tR0rS9xVYxjydTTYV%2BKuvRuYfLM2yXAYvM0F4TKOtfXYgxQ8njJNgQ6AXz9yxq5kC%2Burx5goMEUZaVhjnSaBNGg49cM83MUweBtt4TGVQBPTalbSIvo5z&X-Amz-Signature=ffe13bcbdb14d760534e9fb4d86848356f2fa5d8476384e4941d478423f2e8ad&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)


那什么情况下才会存在呢？很明显就是说当我们真正的去启动了这个 consumer 的时候，他才会去帮我们去注册到 ZK 上的一些信息，就把我们订阅者的信息注册到 ZK 上才能看到。我们现在先启动一下。好我直接 spring boot 然后 start 我们的 consumer 你看启动了以后，这回它有一些对应的日志输出，你能看出来。那这一回我现在也包括我们卡夫卡自己，它内部也有一些日志。


这回我们再去敲一下这个命令，大家来看一下这个命令代表什么意思？代表着是你当前订阅的这个 group 也就是 group 02，它的一些消费进度就是 subscript describe 它的这个进度。首先我们看 topic 有两个，这是 topic 是同一个就是 topic 02 看见了。但是它 topic 下面有两个 partition 一个是第零个 partition 还有一个是第一个 partition 然后他这个里边可能我的字太大了，咱们小伙伴看着就是感觉串行了，我现在把它弄小一点，大家可以尽量的去看清楚一点，我再 clear 一下。 OK 好，我就会再瞧一下这个命令这样对齐了，你看着就舒服多了。我们看一下。


首先 topic 是不是有两个02，然后它的 partition 一个是0，一个是1。然后它的 current offset 就是当前的进度都是0。然后这是 last 就是 log and 就是当前的进度跟这个日志就是我们 commitlog 就是存储消息的实际珍视的这个 offset 是什么都是0。然后这个 LA G 表示延迟，你可以认为是延迟，就是说可能我有多少消息还没有消费。这如果说你消息出现堆积的话，这里边会有延迟。其实在老师我记得我们之前做日志收集的时候，我们有几亿条数据，就基本上我们是 64 个 partition 然后每一个 partition 可能有小两三亿个数据都没有消费。那你想想最终是多少，相当于是 100 多亿。因为我们之前有一次做升级的时候，我们自己的那个消息的这个上报采集的系统有一段时间停机了。所以说因为要做升级就具体情况可能会比较复杂。


但是我会发现什么呢？我的卡斯卡消息堆积能力特别强，几百亿的数据都完全没有问题，然后在消费它不会影响这个就卡不卡的，可能会有少部分的这个吞吐量的影响，但是不是特别大，这足以说明什么呢？我们卡夫卡消息堆积能力是相当强的，包括吞吐量也是特别的牛的，它的消费能力其实也是取决于你的 partition 的数量。


你的 partition 有几个？你对应的 consumer 它的能力就可以去做相对应做一个处理。如果说我举个例子，你的 partition 有 10 个，你的 consumer 只有两个，那这个怎么办？那这个其实相当于说它的性能肯定是有平静的。但是你反过来你的 partition 有 10 个，但是你的 consumer 有 20 个，那你有 10 个 consumer 是没有用的，因为它是对应着一对一的关系。就是我的盘 partition 跟 consumer 之间这块是一些后面老师要跟大家去讲的一些性能上优化的一些点，我们先暂时不去做过多赘述。


然后这里边后面我们看有一个这个 consumer ID 看它自己会有一个 UV ID 的这么一个串，然后它的 host 就是它的这个具体的 consumer 的地址。 OK 现在是有的，是不是？现在是有的，原因是因为什么我的 consumer 已经起来了，对不对？我 consumer 起来，所以说它是有。那比如说现在我把它停掉，我把consumer ，我停掉了。大家可以看停掉了以后，然后我再去刷一下，你会看到什么呢？你会看到最后面都是杠，表示没有任何消费者是不是？ OK 好了，我们看到现在没有任何消费者之后，我们就放心了。然后我们可以做真正的消息的发送。


好了，我们来看一看消息发送。首先我们把刚才我们写好了的这个 producer test 这个代码，我们把它运行起来，就是往这个 topic 02 里边去发消息，我们发 10 条消息来看一看，结果我为什么这里面写这个 sleep 呢？就是我想看到 ACK 的结果，我们来看一看对应着的有 info 信息。你看英文信息已经有了，它叫做发送消息成功是不是？然后 send 它会给你一些这个成功的一些返回结果。看见了吧，这里边有好多的返回结果我们看到了。那就证明这 10 条消息，我这个生产端已经发送到我们的卡夫卡 broker 上了，所以说现在我就可以把生产端的代码停掉了，因为我们已经测试通过了，然后接下来就剩下验证了。怎么去验证呢？很简单，我们就去看一看我们的这个消息的进度就好了。 OK 我们再去刷一下这个命令。


好，我们来看一下你看当前我的这个卡尔的 offset 就是当前的 offset 是几是0，为什么呢？因为我没有做任何消费是不是？那我的这个日志里面最后的这个 offset 都是5，然后延迟也是5，就证明根本就没有消费端消费。 OK 这个大家应该都能理解。那如果我的 consumer 起来之后是不是 cut offset 就会把这十条消息消费了，并且你会看到每一个 partition 它都能够均衡的去处理对应这五条消息是不是？所以说这个东西其实就是一个分区的概念partition 。 OK 那副本的概念就是比如说这个数据我可以在 1 副本，2副本，我可以有一份数据的 copy 你可以认为是主从的概念。

```java
2023-04-08 16:09:34.213  INFO 8043 --- [           main] o.a.kafka.common.utils.AppInfoParser     : Kafka version : 2.0.1
2023-04-08 16:09:34.213  INFO 8043 --- [           main] o.a.kafka.common.utils.AppInfoParser     : Kafka commitId : fa14705e51bd2ce5
2023-04-08 16:09:34.312  INFO 8043 --- [ad | producer-1] org.apache.kafka.clients.Metadata        : Cluster ID: QK8E-HuzRGuURPApyjqr6A
2023-04-08 16:09:34.499  INFO 8043 --- [ad | producer-1] c.b.kafka.producer.KafkaProducerService  : 发送消息成功SendResult [producerRecord=ProducerRecord(topic=topic02, partition=null, headers=RecordHeaders(headers = [], isReadOnly = true), key=null, value=hello kafka 1, timestamp=null), recordMetadata=topic02-0@0]
2023-04-08 16:09:34.499  INFO 8043 --- [ad | producer-1] c.b.kafka.producer.KafkaProducerService  : 发送消息成功SendResult [producerRecord=ProducerRecord(topic=topic02, partition=null, headers=RecordHeaders(headers = [], isReadOnly = true), key=null, value=hello kafka 1, timestamp=null), recordMetadata=topic02-0@1]
2023-04-08 16:09:34.499  INFO 8043 --- [ad | producer-1] c.b.kafka.producer.KafkaProducerService  : 发送消息成功SendResult [producerRecord=ProducerRecord(topic=topic02, partition=null, headers=RecordHeaders(headers = [], isReadOnly = true), key=null, value=hello kafka 1, timestamp=null), recordMetadata=topic02-0@2]
2023-04-08 16:09:34.499  INFO 8043 --- [ad | producer-1] c.b.kafka.producer.KafkaProducerService  : 发送消息成功SendResult [producerRecord=ProducerRecord(topic=topic02, partition=null, headers=RecordHeaders(headers = [], isReadOnly = true), key=null, value=hello kafka 1, timestamp=null), recordMetadata=topic02-0@3]
2023-04-08 16:09:34.499  INFO 8043 --- [ad | producer-1] c.b.kafka.producer.KafkaProducerService  : 发送消息成功SendResult [producerRecord=ProducerRecord(topic=topic02, partition=null, headers=RecordHeaders(headers = [], isReadOnly = true), key=null, value=hello kafka 1, timestamp=null), recordMetadata=topic02-0@4]
2023-04-08 16:09:34.523  INFO 8043 --- [ad | producer-1] c.b.kafka.producer.KafkaProducerService  : 发送消息成功SendResult [producerRecord=ProducerRecord(topic=topic02, partition=null, headers=RecordHeaders(headers = [], isReadOnly = true), key=null, value=hello kafka 1, timestamp=null), recordMetadata=topic02-1@0]
2023-04-08 16:09:34.523  INFO 8043 --- [ad | producer-1] c.b.kafka.producer.KafkaProducerService  : 发送消息成功SendResult [producerRecord=ProducerRecord(topic=topic02, partition=null, headers=RecordHeaders(headers = [], isReadOnly = true), key=null, value=hello kafka 1, timestamp=null), recordMetadata=topic02-1@1]
2023-04-08 16:09:34.524  INFO 8043 --- [ad | producer-1] c.b.kafka.producer.KafkaProducerService  : 发送消息成功SendResult [producerRecord=ProducerRecord(topic=topic02, partition=null, headers=RecordHeaders(headers = [], isReadOnly = true), key=null, value=hello kafka 1, timestamp=null), recordMetadata=topic02-1@2]
2023-04-08 16:09:34.524  INFO 8043 --- [ad | producer-1] c.b.kafka.producer.KafkaProducerService  : 发送消息成功SendResult [producerRecord=ProducerRecord(topic=topic02, partition=null, headers=RecordHeaders(headers = [], isReadOnly = true), key=null, value=hello kafka 1, timestamp=null), recordMetadata=topic02-1@3]
2023-04-08 16:09:34.524  INFO 8043 --- [ad | producer-1] c.b.kafka.producer.KafkaProducerService  : 发送消息成功SendResult [producerRecord=ProducerRecord(topic=topic02, partition=null, headers=RecordHeaders(headers = [], isReadOnly = true), key=null, value=hello kafka 1, timestamp=null), recordMetadata=topic02-1@4]
```

[image](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/ced654a6-830e-4e72-813e-beb31aa2db40/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466356CD2Y6%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T225322Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDYrdy5JXDwal2XgWwVNbogizoGs74tQW9Z7%2F%2B4G0za8gIhAK2v85xgko1g0B7r5x%2FMKN50rGBPE5iGDyUSbHvijcfaKogECMb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgyPSwyecFFhSOgKFC8q3AOpoRkyo92xYBF1SiW6rqabT6YTUdABDM2xI2ay2Vf8fRn25U7XDfr0O5CgYrS2PnazR9DURfq9km0KosgpGm00kOr0bvP7ZOh75%2FWhSB2ifpkkV2MTeNnKSvLEGvn%2BSLLOThCNQHaXfz30dINxNu1LEMCaq9iwE2DzOfVE%2B1kQGsR3AnsBmTrAtk5troaVTpiy2H0tBfW6qRy%2BXvz41KbFGWx96HEGfAuIbyw1LG1geRuaVtZeRHpeSNt4utwHFmaAJLwKqxOTx%2FDgvMxNCcHIAmAQZH%2BdO2nHAN8vpT1Y3g1MwxkfyuqPj2DPlCLtj%2FIOzbA%2BLZ4OKBw6E9R%2BzW3TNtrwK%2BvQS7gNIjMjnHZW3OVBi8VZV5IKo54nujauD3Yt1WRnGg6u6n4bL2KqFFkmMsg9L9KN7SzzbyV7JA%2FY6Dpxfs33RX6LCbZt7X2lupFD8G7%2FCV%2FAZgkskw2yW7iAX9T00hW14FXvFxn7aTT5KaDKfYyOIyw1UvpafqPNBaNiTFwPm6r3LfrtFpgIm1DoVRe23duzg971cBSK%2FQztboe3cdycHNcB257BvXLxyvyk2TA%2F%2Bg%2FKmTk7sZww0XstdLfSqSWrFiiF2zJbwdjraC43nFhXCECsQeIt4jCjuP%2FSBjqkAfi4%2FyaN9a1DNrhvGAK0CMSfuyQXWUZgW%2FuReTQGpb6ufsLC8GVlVi8UX4656VThWShC6Ol52wD7RyfgHgQ0KxxVsiJwW1AUIrjUvI6tR0rS9xVYxjydTTYV%2BKuvRuYfLM2yXAYvM0F4TKOtfXYgxQ8njJNgQ6AXz9yxq5kC%2Burx5goMEUZaVhjnSaBNGg49cM83MUweBtt4TGVQBPTalbSIvo5z&X-Amz-Signature=786977e0c78c93026065e751575f9e838a7ecf18e801a64e31dbaf70671ba6ea&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)


好了，那接下来我们要做的事情就是把我们的 consumer 端启动，把我们的 consumer 端启动，小伙伴们来我们去启动一下我们的这个 consumer 端的应用服务。 consumer 端启动之后，他会去对消息做处理。我们看一下。其实它已经消费完了，因为我打了这个 log 日志，就是如果 on message 进来的话，它肯定会打这个日志输出。我来看看有没有看消费消息已经有了。看见了，我们把 value 取出来了，是不是？把 y6 取出来一共是 10 条消息。 OK 那在我们的日志里边我们已经看到了这个记录了，但是它真正的消费了吗？它不一定是不是。所以说你还需要看它对应的进度，它的进度其实是很关键的。一般来讲，在实际排查问题的时候，对于进度的这个查看这条命令是非常非常重要的。你看它没有任何变化看见了吗？没有任何变化。为什么呢？因为你没有做 ACK 你没有 ACK 我的 color offset 永远都是0，就是没有做任何消费。


我的延迟永远都是这十个延迟，就是两个队列就或者是两个 partitionok 那这一点小伙伴们知道了以后，所以说你就知道签收它的这个重要性了。那我把这段代码再放开，然后我接下来再去重新做一个运行好来看一下，这回我就帮他处理完一条记录，我就做一个签收，然后回过头来我再去做这个事情。

```java
package com.bfxy.consumer;

import lombok.extern.slf4j.Slf4j;
import org.apache.kafka.clients.consumer.Consumer;
import org.apache.kafka.clients.consumer.ConsumerRecord;
import org.springframework.kafka.annotation.KafkaListener;
import org.springframework.kafka.support.Acknowledgment;
import org.springframework.stereotype.Component;

/**
 * <h1></h1>
 */
@Slf4j
@Component
public class KafkaConsumerService {

    @KafkaListener(groupId = "group02", topics = "topic02")
    public void onMessage(ConsumerRecord<String, Object> record, Acknowledgment acknowledgment, Consumer<?, ?> consumer) {
        log.info("消费端接受消息 {}" + record.value());
        // 手工签收++++++++++++++++++++++++++++++放开手工签收的代码
        acknowledgment.acknowledge();
    }

}
```


你会看到这个里边有一些 offset 更新的一些日志看见了吗？有一些 add 有一些 info 那这样的话我们再看一下消息的进度。同学们请看这回你看看的 offset 是什么，都是当前的了。然后这个 LA G 都是 0 了，就证明每一个 partition 下面没有任何消息堆积，如果有消息堆积，这个数就特别特别大。 OK 好了，这就证明没问题。没问题之后我们再做一次测试，来看一看这个效果。

[image](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/43c814e4-8116-41e7-9733-92014c9f67ab/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466356CD2Y6%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T225322Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDYrdy5JXDwal2XgWwVNbogizoGs74tQW9Z7%2F%2B4G0za8gIhAK2v85xgko1g0B7r5x%2FMKN50rGBPE5iGDyUSbHvijcfaKogECMb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgyPSwyecFFhSOgKFC8q3AOpoRkyo92xYBF1SiW6rqabT6YTUdABDM2xI2ay2Vf8fRn25U7XDfr0O5CgYrS2PnazR9DURfq9km0KosgpGm00kOr0bvP7ZOh75%2FWhSB2ifpkkV2MTeNnKSvLEGvn%2BSLLOThCNQHaXfz30dINxNu1LEMCaq9iwE2DzOfVE%2B1kQGsR3AnsBmTrAtk5troaVTpiy2H0tBfW6qRy%2BXvz41KbFGWx96HEGfAuIbyw1LG1geRuaVtZeRHpeSNt4utwHFmaAJLwKqxOTx%2FDgvMxNCcHIAmAQZH%2BdO2nHAN8vpT1Y3g1MwxkfyuqPj2DPlCLtj%2FIOzbA%2BLZ4OKBw6E9R%2BzW3TNtrwK%2BvQS7gNIjMjnHZW3OVBi8VZV5IKo54nujauD3Yt1WRnGg6u6n4bL2KqFFkmMsg9L9KN7SzzbyV7JA%2FY6Dpxfs33RX6LCbZt7X2lupFD8G7%2FCV%2FAZgkskw2yW7iAX9T00hW14FXvFxn7aTT5KaDKfYyOIyw1UvpafqPNBaNiTFwPm6r3LfrtFpgIm1DoVRe23duzg971cBSK%2FQztboe3cdycHNcB257BvXLxyvyk2TA%2F%2Bg%2FKmTk7sZww0XstdLfSqSWrFiiF2zJbwdjraC43nFhXCECsQeIt4jCjuP%2FSBjqkAfi4%2FyaN9a1DNrhvGAK0CMSfuyQXWUZgW%2FuReTQGpb6ufsLC8GVlVi8UX4656VThWShC6Ol52wD7RyfgHgQ0KxxVsiJwW1AUIrjUvI6tR0rS9xVYxjydTTYV%2BKuvRuYfLM2yXAYvM0F4TKOtfXYgxQ8njJNgQ6AXz9yxq5kC%2Burx5goMEUZaVhjnSaBNGg49cM83MUweBtt4TGVQBPTalbSIvo5z&X-Amz-Signature=8454f4465aa4219a33ba4043876fe436026046b329d0c426423632512b2d1f78&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

[image](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/cf4d338b-f4af-4a3a-b1a9-200142d956b0/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466356CD2Y6%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T225322Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDYrdy5JXDwal2XgWwVNbogizoGs74tQW9Z7%2F%2B4G0za8gIhAK2v85xgko1g0B7r5x%2FMKN50rGBPE5iGDyUSbHvijcfaKogECMb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgyPSwyecFFhSOgKFC8q3AOpoRkyo92xYBF1SiW6rqabT6YTUdABDM2xI2ay2Vf8fRn25U7XDfr0O5CgYrS2PnazR9DURfq9km0KosgpGm00kOr0bvP7ZOh75%2FWhSB2ifpkkV2MTeNnKSvLEGvn%2BSLLOThCNQHaXfz30dINxNu1LEMCaq9iwE2DzOfVE%2B1kQGsR3AnsBmTrAtk5troaVTpiy2H0tBfW6qRy%2BXvz41KbFGWx96HEGfAuIbyw1LG1geRuaVtZeRHpeSNt4utwHFmaAJLwKqxOTx%2FDgvMxNCcHIAmAQZH%2BdO2nHAN8vpT1Y3g1MwxkfyuqPj2DPlCLtj%2FIOzbA%2BLZ4OKBw6E9R%2BzW3TNtrwK%2BvQS7gNIjMjnHZW3OVBi8VZV5IKo54nujauD3Yt1WRnGg6u6n4bL2KqFFkmMsg9L9KN7SzzbyV7JA%2FY6Dpxfs33RX6LCbZt7X2lupFD8G7%2FCV%2FAZgkskw2yW7iAX9T00hW14FXvFxn7aTT5KaDKfYyOIyw1UvpafqPNBaNiTFwPm6r3LfrtFpgIm1DoVRe23duzg971cBSK%2FQztboe3cdycHNcB257BvXLxyvyk2TA%2F%2Bg%2FKmTk7sZww0XstdLfSqSWrFiiF2zJbwdjraC43nFhXCECsQeIt4jCjuP%2FSBjqkAfi4%2FyaN9a1DNrhvGAK0CMSfuyQXWUZgW%2FuReTQGpb6ufsLC8GVlVi8UX4656VThWShC6Ol52wD7RyfgHgQ0KxxVsiJwW1AUIrjUvI6tR0rS9xVYxjydTTYV%2BKuvRuYfLM2yXAYvM0F4TKOtfXYgxQ8njJNgQ6AXz9yxq5kC%2Burx5goMEUZaVhjnSaBNGg49cM83MUweBtt4TGVQBPTalbSIvo5z&X-Amz-Signature=61b3777aff2832e10113f36491a95f6a8cc69914a4df7a299fee84a35e19aa5c&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)


我们的 consumer 端启动了是不是。 consumer 端启动了之后，我把这个 producer 端我们，再运行一次，我们把它这个消息条数我设大一点，我是发 1 万条数据来观察一下。比如说 sleep 每隔别发太多了，发 1000 条，因为我想每隔 5 毫秒发一条消息。然后我们来看一看那个效果好已经启动了。启动了之后我们就来看一下。


其实小伙伴们我就想让你看一下对应的延迟的那个效果。当然它比较卡，我 1000 条消息那其实已经消费完了，因为刚才比较卡，其实我想让你看这个数，它一直在变化。但是你还没看到，因为我的现在的卡克卡就一台节点，而且它的资源有限，刚才他一次性就全把消息都发完了。


所以说看到这个效果，如果你想看这效果，你可以把这个再放慢一点，比如说放慢 50 毫秒，然后再慢慢的去对这个做处理消息发送做处理。然后你就可以观察到他这个就是刚才那个变化。我其实想让小伙伴们看到这个变化，就是它对应的这个 lag 的选项的参数变化。好了。那么其实我们对卡夫卡已经讲完了，就是对于我们的这个 spring boot 之后卡夫卡好了，那这节课我们讲到这，感谢小伙伴们收看。


