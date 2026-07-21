---
title: 1-4 kafka与springboot整合_生产者讲解
---

# 1-4 kafka与springboot整合_生产者讲解

[image](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/df6e8f26-3b10-487a-8209-d834e5ac462e/SCR-20240807-fyjt.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46677SGYOWN%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T225322Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCHMMhA8vL6QyBHNaqatmwDctkz%2FviYb%2BYROc9kU66qiQIhAMDkna2k%2Fb5iI9LP%2FxLTA4LEZ%2B3xEEUI9AelMW8Z0ZXGKogECMb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1Igw0Qz4dk%2B2HUYhBSksq3ANeLTqJ46y%2FiOGB5W9JzogtbRSP2qRJFirEonacvi1gVRva7D%2FnXrLev9gjmjxOB%2BH33qWZw35uMxv%2BAvC4zULyBUGYD%2BcxWmLQ2Xkj%2F6lROnOOen%2FzQxUzRJ5ZXy9JL9ZLsH68XTQWGgwZvhQmXFrA69T01%2BHxSQwrMRIdOzkszNitL%2B5uVa%2FbCQc%2B5Qp%2FScfMlKgDiVjii9VH%2Fw3TyJcpKbF2sHMCznOTsJMlxQFc6qBnBhooRfXaT2ZEv2ID8dq2HXbnJINU53ZTFbGLKqdbnc%2B0FaDJGNyTABiw%2BcNuyx9UGRIa0w7xs2%2FU0aLLbAha9ptV90QyAP9vKFi8RmRHVeDR4xKIsxqlG5pr6yxTo0eqt8L2beh8KifBCG5zqGveJcIR%2B8LhiKi6fZLaG%2BjIeEheVrTj0c3D2KQdk%2FOmD3tZceveo%2BtbWrhvpMdIl9Sc9hUNMkWrCZ2RvCPOMUxNgXbNrEEjkRd8EqDxg33r59OlJYL8cXqOmBBaqqXve3Pk1rYQxReZHuiZGuFbD0qsNJJsbWzUOWWwjjybG4Zk8N8Jlr6%2F2LAeMgBfj4xYISq2AejM0SXskuoNjSj9RM8m3baFFHLH4yz2DRZjlux4b%2FeLOQhsdkxuygCSPzChuP%2FSBjqkAZzbDbV9XIh7puM143lqseiSFm9i4vzqqq%2Blnq9QY0K4FnMerHSMhIHqV0Jf5GPa2Vz7Bt7d9l05fL74kMurGdelhMb42PM6YsjuquGAzSC7eUCq7VQdkpUplbDKn3QKUCc8qQzglVf7FWrKACdCHxjj%2BW0Zul6LdQKrMgiM0VyLu04F36FUQYBnUELfqRt7Wq4o2M4ywXig%2FRXjMzw7AfoTw1lY&X-Amz-Signature=66ac755bb3ecc51f4fc295473385851133de0f1b16ac2f9e23f82cfb1be07e92&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

[image](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/7181a63d-89ec-4866-b285-924b8b4f1f00/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46677SGYOWN%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T225322Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCHMMhA8vL6QyBHNaqatmwDctkz%2FviYb%2BYROc9kU66qiQIhAMDkna2k%2Fb5iI9LP%2FxLTA4LEZ%2B3xEEUI9AelMW8Z0ZXGKogECMb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1Igw0Qz4dk%2B2HUYhBSksq3ANeLTqJ46y%2FiOGB5W9JzogtbRSP2qRJFirEonacvi1gVRva7D%2FnXrLev9gjmjxOB%2BH33qWZw35uMxv%2BAvC4zULyBUGYD%2BcxWmLQ2Xkj%2F6lROnOOen%2FzQxUzRJ5ZXy9JL9ZLsH68XTQWGgwZvhQmXFrA69T01%2BHxSQwrMRIdOzkszNitL%2B5uVa%2FbCQc%2B5Qp%2FScfMlKgDiVjii9VH%2Fw3TyJcpKbF2sHMCznOTsJMlxQFc6qBnBhooRfXaT2ZEv2ID8dq2HXbnJINU53ZTFbGLKqdbnc%2B0FaDJGNyTABiw%2BcNuyx9UGRIa0w7xs2%2FU0aLLbAha9ptV90QyAP9vKFi8RmRHVeDR4xKIsxqlG5pr6yxTo0eqt8L2beh8KifBCG5zqGveJcIR%2B8LhiKi6fZLaG%2BjIeEheVrTj0c3D2KQdk%2FOmD3tZceveo%2BtbWrhvpMdIl9Sc9hUNMkWrCZ2RvCPOMUxNgXbNrEEjkRd8EqDxg33r59OlJYL8cXqOmBBaqqXve3Pk1rYQxReZHuiZGuFbD0qsNJJsbWzUOWWwjjybG4Zk8N8Jlr6%2F2LAeMgBfj4xYISq2AejM0SXskuoNjSj9RM8m3baFFHLH4yz2DRZjlux4b%2FeLOQhsdkxuygCSPzChuP%2FSBjqkAZzbDbV9XIh7puM143lqseiSFm9i4vzqqq%2Blnq9QY0K4FnMerHSMhIHqV0Jf5GPa2Vz7Bt7d9l05fL74kMurGdelhMb42PM6YsjuquGAzSC7eUCq7VQdkpUplbDKn3QKUCc8qQzglVf7FWrKACdCHxjj%2BW0Zul6LdQKrMgiM0VyLu04F36FUQYBnUELfqRt7Wq4o2M4ywXig%2FRXjMzw7AfoTw1lY&X-Amz-Signature=31a22d597ff2f22a489a0c7beefd8ce883b7f64339d237f076e29485fca08250&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

hello 小伙伴们，大家好，那么这节课我们快速的去进入 spring boot 整合卡夫卡的一个实战。那我们来看一看整个的整合的这个步骤有哪几个。那第一个很简单，就是我们的 Maven 依赖了，对于任何的一个框架，你想去做什么 boot 级别的整合，你都需要引入一个 dependency 要么就是叉杠 starter 要么就是 spring 杠叉。 OK 然后接下来我们看一下。


那我们引完对应的配置以后，那很明显我们需要对于一些核心的配置项，一些这个 application.practice 配置项做一些配置。那无论是我们卡夫卡的生产端 produce 还是卡夫卡的消费端，也就是说 consumer 可能都需要对配置做一个这个详细的这么一个讲解，后面的老师会跟大家一步步去做。那接下来我们来看一看。


那对于 producer 这端，对于生产端，那他肯定要创建一个对象叫做什么呢？卡夫卡 template 对象。那这个我不知道小伙伴有没有印象，对于 spring boot 整合 rabbit MQ 的时候，也是有一个叫什么叫做 rabbit templateok 那卡夫卡其实也是一样的，叫做卡夫卡 template 对象。那我们来继续往下走。

[image](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/c0024484-582e-499e-b004-bd59fca0180b/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46677SGYOWN%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T225322Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCHMMhA8vL6QyBHNaqatmwDctkz%2FviYb%2BYROc9kU66qiQIhAMDkna2k%2Fb5iI9LP%2FxLTA4LEZ%2B3xEEUI9AelMW8Z0ZXGKogECMb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1Igw0Qz4dk%2B2HUYhBSksq3ANeLTqJ46y%2FiOGB5W9JzogtbRSP2qRJFirEonacvi1gVRva7D%2FnXrLev9gjmjxOB%2BH33qWZw35uMxv%2BAvC4zULyBUGYD%2BcxWmLQ2Xkj%2F6lROnOOen%2FzQxUzRJ5ZXy9JL9ZLsH68XTQWGgwZvhQmXFrA69T01%2BHxSQwrMRIdOzkszNitL%2B5uVa%2FbCQc%2B5Qp%2FScfMlKgDiVjii9VH%2Fw3TyJcpKbF2sHMCznOTsJMlxQFc6qBnBhooRfXaT2ZEv2ID8dq2HXbnJINU53ZTFbGLKqdbnc%2B0FaDJGNyTABiw%2BcNuyx9UGRIa0w7xs2%2FU0aLLbAha9ptV90QyAP9vKFi8RmRHVeDR4xKIsxqlG5pr6yxTo0eqt8L2beh8KifBCG5zqGveJcIR%2B8LhiKi6fZLaG%2BjIeEheVrTj0c3D2KQdk%2FOmD3tZceveo%2BtbWrhvpMdIl9Sc9hUNMkWrCZ2RvCPOMUxNgXbNrEEjkRd8EqDxg33r59OlJYL8cXqOmBBaqqXve3Pk1rYQxReZHuiZGuFbD0qsNJJsbWzUOWWwjjybG4Zk8N8Jlr6%2F2LAeMgBfj4xYISq2AejM0SXskuoNjSj9RM8m3baFFHLH4yz2DRZjlux4b%2FeLOQhsdkxuygCSPzChuP%2FSBjqkAZzbDbV9XIh7puM143lqseiSFm9i4vzqqq%2Blnq9QY0K4FnMerHSMhIHqV0Jf5GPa2Vz7Bt7d9l05fL74kMurGdelhMb42PM6YsjuquGAzSC7eUCq7VQdkpUplbDKn3QKUCc8qQzglVf7FWrKACdCHxjj%2BW0Zul6LdQKrMgiM0VyLu04F36FUQYBnUELfqRt7Wq4o2M4ywXig%2FRXjMzw7AfoTw1lY&X-Amz-Signature=00411257b7de52945fd7d4421fa3a4be13cf05b1d9323d854ab742546b96b778&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

那我们的消费端同学们你看到了是不是就非常熟悉，叫做艾特卡夫卡雷斯，那它是一个监听消息的一个监听器，那我可以把它放到一个方法上，你看到这个它就非常像我们之前所学的 rabbit MQ 的 rabbit listener 那其实他们是出自同一套框架，就是我们的这个 message 就是 spring mqp 或者是 spring 的这个 message 这一套框架。


好了，那既然我们已经了解了如何去做 spring boot 与卡夫卡的整合，那接下来我们就开始进入我们的实际的代码开发阶段了。好了，我们打开我们自己的这个 idea 工具，然后快速去进入这个环境的搭建。首先我们右键 new 一个普通的这个 Maven project ，然后给它起个名字 create 一个 simple project 然后起个名字叫做 tom.bfx Y 点或者加上这个名字就可以了。


然后这个 rt fact ID 我们叫做卡夫卡杠producer ，咱们起的简单一些，反正总之我们的项目都是跟这个斯科布特集成的。然后接下来我们就 finish 创建好了一个这个工程，叫做卡夫卡杠 producer 然后这个 producer 它对应着我们要对应它的一个 Maven 依赖，做一些相对应的这个设置。那在这里我们来看一看我们都需要哪些。首先在这里老师有一些比较关键的东西我就直接粘过来了，parent他的 parent 我们现在用的是二点幺点五这个瑞丽斯版本。 OK 我就直接粘过来。然后接下来它还需要哪些呢？比如说它有一些重要的 practice 配置，一些 UTF 8 字符集的配置。然后接下来比较关键的有哪些？咱们来看一看它对应的这个迈文迪坦尼斯，我们来直接快速的去写一下。


首先有 spring good starter 对应着这个 web 然后以及我们的这个 test 然后我们在这里这个 long book 就不说了，就是一些这个日志的这么一个组件。然后再往下看见了吗？我们引入的一个包叫做奥克点 spring framework.kafka spring 杠卡夫卡，对应的这个 dependence 就够了。那既然我们做完了这一步骤之后，那接下来进行真正的开发了。 OK 我们搞定了之后，我现在先不着急说我们写代码，我们先把我们对应的包先创建一下，我们叫做 com.bfx Y 点卡不卡。 Ok. 然后我们建一个因为是 spring boot 工程，所以说我们就建一个那个 application 咱们叫做application。Ok.然后我们来简单回忆一下这个 application 应该怎么去做。其实很简单，就是一个启动类，一个注解就是 spring boot application 然后在这里边写一个面函数。 OK 我们直接写那个 spring application 点乱方法，然后把我们当前的这个 application.class 放进去就可以了。好，那我们的主类就已经搞定了。


然后我们比如说我现在要做的什么事情呢？我们对应着既然有我们的 producer 那肯定有我们的 consumer 所以说我把工程 control C control V 粘一份出来，然后把它改成 consumer 然后对应着我们稍作修改，修改哪些呢？其实你只需要修改对应的这个工程名字就可以了，这边我们叫做 consumer 然后这个我们也叫做就没有了，是不是就把它就是 rt factor ID 改一下就可以了，其他的不需要变。 OK 那我们来开始快速的去进入我们自己的这个编码。


首先第一点刚才老师说了，就是说我们在去使用跟 spring boot 集成的时候，那第一件事情就应该 new 出来一个 practice 然后对应的去加一些相关的配置。所以说我们就是快速的去建一个 [application.pro](http://application.pro/)pperties 建一个对应的配置文件。


然后第一件事情是把它自己改过来，这是毋庸置疑的，我们应该用u8，然后 O playok 接下来我把它最大化，我们看一看对应着我们需要配置哪些对应的配置项。首先第一个就是我们的这个 server server 点什么呢？点比如说我们的路径，比如就是 server late 杠 contest pass 好，这个路径我们叫做杠 producer 然后比如说我们的 point server point 是多少启动端口，我们的 point 我们在这里叫8001。好了。 OK 然后接下来这两个其实是对应着无关紧要的。那接下来这些配置就是很重要了，就是我们对应着 spring boot 或者说 spring 整合卡夫卡的一些关键的一些配置项。那我们现在主要要写的是什么呢？我们现在主要写的是我们的这个 producer 端。


所以说 spring 点卡夫卡看见了吗？它其实有三个系列，第一个就是 A 大头就是 admin 然后就是 consumer 跟 producer 当然 consumer 里边还有对应的这个 listener 就是监听了，然后就 producer 然后剩下的比如说一些安全的相关的 xdream 就是 spring club stream 相关的等等，这些都会有。那我们在这里挑最关键的我们去使用。


第一个最关键的就是 boost track 杠 server 就什么意思？这个就是你对应的你自己的你的卡夫卡的集群。那我们之前领着小伙伴们去搭建的时候已经搭建过一遍了，就是老师在之前给你的文档幺九二点幺六八点幺幺点五幺，然后端口号默认是9092。 OK 这已经有了。那在这里如果小伙伴们忘记的话，那我们可以回过头来，我现在快速去打开一下我们之前老师给你提供的一个 map 档，这里边肯定会有对应的这个配置。看见了吧，我们用的是幺九二点幺六八点幺幺点五幺在这里，那我就直接顺带着把我们的这卡夫卡集群也启动起来，就是这个服务器我已经准备好了，然后这个字体我也调大一些。


Ok. 然后我们 CD 到 USR local 然后下面我们这个 CD 到卡夫卡，我们现在用的卡夫卡是二点幺二这个版本也是比较新的了。然后 CD 到 bin 目录下到 bin 目录下之后我们去执行这个命令，就是对应着我们把我们的这卡。好，启动起来之后你要观察它这个日志有没有报错，如果没有报错就证明它是 OK 的，咱们耐心等待一下。


好了，已经启动起来了之后，我们不关注他，先把这个窗口关闭，然后紧接着带我们的配置。第一个配置就是非常关键的，无论是 produce 端还是 consumer 端，都需要对这个配置进行配置一下。然后接下来就是卡夫卡的 producer 相关的配置。比如说卡夫卡 producer 有几个比较关键的，第一个就是 retrace RE 串是什么意思呢？在这里设置名就是当卡夫卡他发送消息发送失败的时候，他允不允许继续的去重试卡夫卡 producer 发送消息失败时的一个重试的次数配置。然后我们再往下看，还有一些比较关键的，比如说它的一些 P 发送。就 bench size 这个 bench size 一般来讲就是默认你可以设置它消息到达多大了，我就可以去进行一个发送。比如说我设置16384，大家是不是想起了那个 Redis 它的什么，批量发售数据的配置，16384就是 Redis slot 那个数量槽的数量。


然后比如说一个比较关键的性能优化的这个一个选项叫做什么？叫做设置卡夫卡生产者内存缓存或者说内存的缓冲区或者叫缓存区也可以缓存区的大小，这个有利于我们高性能的去做。这个 sand 其实官方推荐的大小是 32 兆，32兆，你乘一下这个数是多少？它叫做 buffer 的 memory 等于 3355432 这个其实很好记，就是335544，然后剩下的 32 兆和那 32 非常好记。那接下来有两个比较关键的配置项，在这里我就不去敲了，直接粘过来给小伙伴们看一下这两个配置项是干什么的，它主要是做这个序列化的卡夫卡消息的序列化配置。好，就这两个我们来看一看，就对应着卡夫卡的这个 key sale leather 跟这个 value sale leather 都要去做指向一个。这个明确的一个类就是 [common.co](http://common.co/) lesson 然后叫做 string co lesser 无论是对应的 key 还是 value 都需要做这么一个序列化的事情。


然后搞定完这个事情以后，**接下来我说一个卡卡里边最关键就是我们所有配置里边最关键的一个配置，这个配置它真的是能够影响你整个卡夫卡集群的，你的生产者，你的消息到底是不是可靠的，**

```shell
server.servlet.context-path=/producer
server.port=8001

# Spring 整合 kafka
spring.kafka.bootstrap-servers=192.168.13.210:9092,192.168.13.211:9092,192.168.13.212:9092
## kafak producer 发送消息失败时重试的的次数
spring.kafka.producer.retries=0
# 批量发送数据的配置
spring.kafka.producer.batch-size=16384
# 设置 kafka 生产者内存缓存区的大小(官方的建议 32MB）
spring.kafka.producer.buffer-memory=22554432
## kafka消息的序列化配置
spring.kafka.producer.key-serializer=org.apache.kafka.common.serialization.StringSerializer
spring.kafka.producer.value-serializer=org.apache.kafka.common.serialization.StringSerializer
# acks=0 ： 生产者在成功写入消息之前不会等待任何来自服务器的响应。
# acks=1 ： 只要集群的首领节点收到消息，生产者就会收到一个来自服务器成功响应。
# acks=-1: 表示分区leader必须等待消息被成功写入到所有的ISR副本(同步副本)中才认为producer请求成功。这种方案提供最高的消息持久性保证，但是理论上吞吐率也是最差的。

## 	这个是kafka生产端最重要的选项
spring.kafka.producer.acks=1
```

[image](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/e9996631-7505-40ef-bfff-07ad30c17a63/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46677SGYOWN%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T225322Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCHMMhA8vL6QyBHNaqatmwDctkz%2FviYb%2BYROc9kU66qiQIhAMDkna2k%2Fb5iI9LP%2FxLTA4LEZ%2B3xEEUI9AelMW8Z0ZXGKogECMb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1Igw0Qz4dk%2B2HUYhBSksq3ANeLTqJ46y%2FiOGB5W9JzogtbRSP2qRJFirEonacvi1gVRva7D%2FnXrLev9gjmjxOB%2BH33qWZw35uMxv%2BAvC4zULyBUGYD%2BcxWmLQ2Xkj%2F6lROnOOen%2FzQxUzRJ5ZXy9JL9ZLsH68XTQWGgwZvhQmXFrA69T01%2BHxSQwrMRIdOzkszNitL%2B5uVa%2FbCQc%2B5Qp%2FScfMlKgDiVjii9VH%2Fw3TyJcpKbF2sHMCznOTsJMlxQFc6qBnBhooRfXaT2ZEv2ID8dq2HXbnJINU53ZTFbGLKqdbnc%2B0FaDJGNyTABiw%2BcNuyx9UGRIa0w7xs2%2FU0aLLbAha9ptV90QyAP9vKFi8RmRHVeDR4xKIsxqlG5pr6yxTo0eqt8L2beh8KifBCG5zqGveJcIR%2B8LhiKi6fZLaG%2BjIeEheVrTj0c3D2KQdk%2FOmD3tZceveo%2BtbWrhvpMdIl9Sc9hUNMkWrCZ2RvCPOMUxNgXbNrEEjkRd8EqDxg33r59OlJYL8cXqOmBBaqqXve3Pk1rYQxReZHuiZGuFbD0qsNJJsbWzUOWWwjjybG4Zk8N8Jlr6%2F2LAeMgBfj4xYISq2AejM0SXskuoNjSj9RM8m3baFFHLH4yz2DRZjlux4b%2FeLOQhsdkxuygCSPzChuP%2FSBjqkAZzbDbV9XIh7puM143lqseiSFm9i4vzqqq%2Blnq9QY0K4FnMerHSMhIHqV0Jf5GPa2Vz7Bt7d9l05fL74kMurGdelhMb42PM6YsjuquGAzSC7eUCq7VQdkpUplbDKn3QKUCc8qQzglVf7FWrKACdCHxjj%2BW0Zul6LdQKrMgiM0VyLu04F36FUQYBnUELfqRt7Wq4o2M4ywXig%2FRXjMzw7AfoTw1lY&X-Amz-Signature=fefffb8bafab0c6fbfa2ed923114965e473464e54882f29e85a70a05a53251d3&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

[image](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/e933b25c-43da-43fe-a534-0973cce0ac5e/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46677SGYOWN%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T225322Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCHMMhA8vL6QyBHNaqatmwDctkz%2FviYb%2BYROc9kU66qiQIhAMDkna2k%2Fb5iI9LP%2FxLTA4LEZ%2B3xEEUI9AelMW8Z0ZXGKogECMb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1Igw0Qz4dk%2B2HUYhBSksq3ANeLTqJ46y%2FiOGB5W9JzogtbRSP2qRJFirEonacvi1gVRva7D%2FnXrLev9gjmjxOB%2BH33qWZw35uMxv%2BAvC4zULyBUGYD%2BcxWmLQ2Xkj%2F6lROnOOen%2FzQxUzRJ5ZXy9JL9ZLsH68XTQWGgwZvhQmXFrA69T01%2BHxSQwrMRIdOzkszNitL%2B5uVa%2FbCQc%2B5Qp%2FScfMlKgDiVjii9VH%2Fw3TyJcpKbF2sHMCznOTsJMlxQFc6qBnBhooRfXaT2ZEv2ID8dq2HXbnJINU53ZTFbGLKqdbnc%2B0FaDJGNyTABiw%2BcNuyx9UGRIa0w7xs2%2FU0aLLbAha9ptV90QyAP9vKFi8RmRHVeDR4xKIsxqlG5pr6yxTo0eqt8L2beh8KifBCG5zqGveJcIR%2B8LhiKi6fZLaG%2BjIeEheVrTj0c3D2KQdk%2FOmD3tZceveo%2BtbWrhvpMdIl9Sc9hUNMkWrCZ2RvCPOMUxNgXbNrEEjkRd8EqDxg33r59OlJYL8cXqOmBBaqqXve3Pk1rYQxReZHuiZGuFbD0qsNJJsbWzUOWWwjjybG4Zk8N8Jlr6%2F2LAeMgBfj4xYISq2AejM0SXskuoNjSj9RM8m3baFFHLH4yz2DRZjlux4b%2FeLOQhsdkxuygCSPzChuP%2FSBjqkAZzbDbV9XIh7puM143lqseiSFm9i4vzqqq%2Blnq9QY0K4FnMerHSMhIHqV0Jf5GPa2Vz7Bt7d9l05fL74kMurGdelhMb42PM6YsjuquGAzSC7eUCq7VQdkpUplbDKn3QKUCc8qQzglVf7FWrKACdCHxjj%2BW0Zul6LdQKrMgiM0VyLu04F36FUQYBnUELfqRt7Wq4o2M4ywXig%2FRXjMzw7AfoTw1lY&X-Amz-Signature=de7918b062e7045ac457e0b83d8f71cd651fab9b874da53f03e4f9b706b81756&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

说到底是不是100%？ OK 的。这个配置就是我一定要强调这个是卡夫卡生产端最重要的选项了，这主要干什么？其实它主要就是来去帮你配置，我们生产端肯定是要把消息发到卡夫卡的这个 broke 它主要就是来确定说你这个消息到底什么情况下，我算发送成功了，它有好几种选项。那我们先来说 0 表示什么，这个我就不重新写了，我直接把它粘过来。 AC K 等于 0 表示生产者在成功写入消息之前，不会等待任何来自服务器的响应。那比如说，0它就是不做任何的这个等待，就把消息投递过去就完了。然后我们再看等于一什么意思呢？就只要集群的首领节点收到了消息，因为我们都知道集群，卡夫卡可能有三个节点的生产者只要是收到一个来自什么来自服务器的响应，就会认为这条消息我已经投递成功了。说白了，它就是一个可靠性投递的一个配置项。通过这小伙伴们应该能理解了。


第一个是生产者在成功写入消息之前，不会等待任何来自服务器的响应。第二个就是说只要集群中有一个节点收到消息了，那么生产者就会收到一个来自服务器的成功响应。就是说我有一个，那我就给你返回了这个 ACK 了。还有一个就是负一，也可以说称之为金字奥。这表示什么？就表示分区的 leader 必须等待消息被成功的写入到了。


什么呢？我们就看所有的 isr 副本，就是所有的节点才认为 producer 是成功的，就是才认为生产消息这个请求是成功的。那这种方案它其实提供了消息的最高可靠性保障或者说持久性保障。但是理论上来讲，它的吞吐量也是最差的。什么意思？他必须要等到所有的副本就是 replicate 都收到这条消息，并且都写入成功了才会返回。那这个性能是最低的，就是等于负 1 的时候。所以说有的时候如果说你想保证卡夫雅可靠性可不可以也可以，那你就把这个配置项设置为负1，那他就是认为消息在不丢失，就不会存在任何丢失的情况。那当然其实还有一些极限情况，就是比如说那我们不妨画一个图来说明一下是一个什么概念，把我们对应的这个浏览器打开。然后在这里我去画一幅小图来说明这个意思。

[image](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/1d18671c-800f-47e6-92b6-aba0cccc4e2d/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46677SGYOWN%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T225322Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCHMMhA8vL6QyBHNaqatmwDctkz%2FviYb%2BYROc9kU66qiQIhAMDkna2k%2Fb5iI9LP%2FxLTA4LEZ%2B3xEEUI9AelMW8Z0ZXGKogECMb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1Igw0Qz4dk%2B2HUYhBSksq3ANeLTqJ46y%2FiOGB5W9JzogtbRSP2qRJFirEonacvi1gVRva7D%2FnXrLev9gjmjxOB%2BH33qWZw35uMxv%2BAvC4zULyBUGYD%2BcxWmLQ2Xkj%2F6lROnOOen%2FzQxUzRJ5ZXy9JL9ZLsH68XTQWGgwZvhQmXFrA69T01%2BHxSQwrMRIdOzkszNitL%2B5uVa%2FbCQc%2B5Qp%2FScfMlKgDiVjii9VH%2Fw3TyJcpKbF2sHMCznOTsJMlxQFc6qBnBhooRfXaT2ZEv2ID8dq2HXbnJINU53ZTFbGLKqdbnc%2B0FaDJGNyTABiw%2BcNuyx9UGRIa0w7xs2%2FU0aLLbAha9ptV90QyAP9vKFi8RmRHVeDR4xKIsxqlG5pr6yxTo0eqt8L2beh8KifBCG5zqGveJcIR%2B8LhiKi6fZLaG%2BjIeEheVrTj0c3D2KQdk%2FOmD3tZceveo%2BtbWrhvpMdIl9Sc9hUNMkWrCZ2RvCPOMUxNgXbNrEEjkRd8EqDxg33r59OlJYL8cXqOmBBaqqXve3Pk1rYQxReZHuiZGuFbD0qsNJJsbWzUOWWwjjybG4Zk8N8Jlr6%2F2LAeMgBfj4xYISq2AejM0SXskuoNjSj9RM8m3baFFHLH4yz2DRZjlux4b%2FeLOQhsdkxuygCSPzChuP%2FSBjqkAZzbDbV9XIh7puM143lqseiSFm9i4vzqqq%2Blnq9QY0K4FnMerHSMhIHqV0Jf5GPa2Vz7Bt7d9l05fL74kMurGdelhMb42PM6YsjuquGAzSC7eUCq7VQdkpUplbDKn3QKUCc8qQzglVf7FWrKACdCHxjj%2BW0Zul6LdQKrMgiM0VyLu04F36FUQYBnUELfqRt7Wq4o2M4ywXig%2FRXjMzw7AfoTw1lY&X-Amz-Signature=f9399181c2a90157e64d9351c57bcbda06d28b0bb92d6c18273b5601c8a5cb10&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

**我们之前的可靠性投递讲的是什么呢？我们之前的可靠性投递讲的是我们生产端跟这个 broke 端之间的一个关系，就是我们的生产者就是 producer to reduce 跟我们的这个 Broker 我们的这个集群，因为我们之前讲过绕开 MQ 的一个可靠性投递，大家应该能了解那个是什么意思呢？那个就是说我们的消息是一定发送到 broker 的，然后 broker 会给我回一个 ACK 这叫 send message 这叫 confirm ACK 或者是响应 ACK 就是说卡夫卡它里边设置零一负一，其实主要是针对于 Broker 自身去来说的。**

**
比如说卡夫卡设置什么呢？设置一是什么意思就表示什么呢？只要卡夫卡集群中可能这个布鲁克它不仅是一个可能是，三个节点中其中一个 broker 把消息落地了，然后我就立马了去把 ACK 返回给 producer 了。就这意思，而等于负 1 或者是等于 or 它们两个其实是一个意思，就是说开发里边三个 broke 里边所有的节点必须消息都写盘，成功之后再给你返回 ACK 成功。它只是说对于消息存储的一种状态，到底是说全量的就是我所有的副本集做一个这个存储，还是说其中写进去一个 later 之后就可以返回？那可靠性投递是不是还会存在问题，肯定会存在。**

**
比如说哪怕你写入全量的，你卡夫卡集群中有三个节点，你的消息发回去之后，你同步的去刷三个罗克内部的这个数据都落盘成功了。然后返回 ACK 的时候有没有可能再返回 ACK 的时候失败？也有可能你网络出现抖动的时候，你的 ACK 该回不来还回不来一样的。那你要怎么做呢？你还是要自己去做一个定时任务，去扫描一个中间状态。**


***但是卡夫卡它为什么要有这个设置？其实卡夫卡它这个设计思路你可以认为说 rocky MQ 有点类似于卡夫卡绕 kmq 它其实也是有这种机制的同步双写还是说异步的写还是说异步的复制，它都会有各种各样的这个写盘的策略。那在这里我不做太多的一些赘述了，主要是想跟小伙伴们说清楚这个 AC case 它其实是针对于 broker 针对于消息本身的，也不能够保障我们之前说的那个 100% 可靠性的投递，我的消息都写到所有的 broker 上了才给你返回成功。如果说给你返回不成功，那可能是我其中有一个 broker 写失败了，这样的话它对应着会有消息的一些错误的一些信息给你。***


好了，那我们理解完这个概念之后，我们回头来。那我们在这里在实际工作中的话，**一般来讲，我推荐大家就采用第一种策略，就是说我的 ACK 等于一什么意思？就是说当我的主节点只要落盘成功，那我就可以去返回给我的这个 producer 就是客户端一个 ACK 那等于负 1 的这块就是相当于限制太高了。**


**如果你设置成负1，那卡夫卡本身它就是做大数据量的一些海量日志收集，做批处理，做一些高性能的高吞吐量的一些处理的。如果说你把它设置成-1，那你就会相当于没有去用卡布卡。最牛的地方就是对于海量数据的堆积，对于海量日志处理这一块你没有去用它，你反而选择了等于负 1 的话，它的这个你比如说我的集群大，我的集群有 5 个卡夫卡节点，那你要 5 个副本全落成功，就是你的数据刷入 5 台 broker 都成功，它才会返回 ACK 那这个性能肯定是相对来讲要跟等于 1 的这个配置项要差很多很多的，至少是 5 次IO ，多少次请求就不一定了，多少次网络通信也都不一定了。**


OK 所以说在这里首先第一点先要把配置项跟小伙伴们讲清楚，说完了这个配置项以外，那接下来我们其实就可以开始写代码了。那其实卡夫卡的代码非常简单，我们在这里来创建一个包叫做 producer 然后我们来写一个类，咱们叫做卡夫卡 producer service 先把名字起好 class 我们叫做卡夫卡 producer 佘维斯。好搞定这个事情之后，首先第一步我们要加一个艾特 component 或者是 service 或者是 repository 注解都可以。在这里我选择 component 表示它一个组件。然后如果我后面有打日志的，我就可以给他来一个 slfg 这是 long book 的这么一个注解。


然后接下来我可以怎么做？我直接看我直接的写法，直接 o2l 进来，谁叫做我们 PB 上之前说了叫做卡夫卡 template 直接把它奥特威尔进来就可以用，是非常非常的方便。 key 比如说一个 string value 就是一个 object 数据，然后我们叫做卡斯卡特。Ok.然后接下来我们其实就可以去对应它，我们可以去发消息了，怎么去发消息呢？我们来看一看。


那我们在这里选择一个方法，写一个方法，咱们叫做 public wide send message message 方法。然后 send message 呢我们首先卡夫卡要发消息要从哪发，然后给他一个 topic 包括数据是什么呢？我不知道。那怎么办，给他一个 all right。Ok.那接下来我们往下看，这里边卡夫卡他的这个 template 去掉 send message 他返回一个叫做什么叫做 listening 不 future 这么一个对象。好，那我们就用这个。首先我们发送到某一个主题下某一条消息，它会返回一个 future listening 不，那我们直接用这个，我先把这个 copy 过来复制放到这里边，给他起个名字叫做future 。好，然后我去把对应的一些包都引进来，我们现在用的都是卡夫卡的，注意别引错了。


好，然后有这个 future 之后他能做什么事情啊？同学们想一想，你看到这个 future 就知道他是一个什么 future 模式，那他肯定能够去做一个 add call back 的操作。他艾特 callback 做什么？看见了吗？他可以去 new 一个叫做 listening ball search call back 那我们就 new 一个 listening able chr 科拜弄出来。然后要重写它的一个方法，重写它两个方法，我们首先把方法实现。


第一个就是 on success 还有一个就是 on failure 就是在成功的时候跟失败的时候分别可以做一些什么事情。那当然这里边的 T 我们其实可以直接知道了， T 就是里边的这一坨我就直接拿过来就好了。然后这里边其实我们都可以知道这个 T 是什么了，就是刚才我们看到的这个东西。

```java
package com.bfxy.producer;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.kafka.core.KafkaTemplate;
import org.springframework.kafka.support.SendResult;
import org.springframework.stereotype.Component;
import org.springframework.util.concurrent.ListenableFuture;
import org.springframework.util.concurrent.ListenableFutureCallback;

/**
 * <h1></h1>
 */
//@Sl4j
@Component
public class KafkaProducerService {


    @Autowired
    private KafkaTemplate<String, Object> kafkaTemplate;

    public void sendmessage(String topic, Object object) {

        ListenableFuture<SendResult<String, Object>> future = kafkaTemplate.send(topic, object);

        future.addCallback(new ListenableFutureCallback<SendResult<String, Object>>() {

            @Override
            public void onSuccess(SendResult<String, Object> result) {
                System.out.println("发送消息成功"+ result.toString());
                
            }

            @Override
            public void onFailure(Throwable ex) {
                System.out.println("发送消息失败"+ ex.getMessage());

            }
        });


    }

}
```


好，那我们来看看成功的时候，我们在这里比如说成功的时候我就打一个 log 日志就好了。我 [log.info](http://log.info/) 发送消息成功，然后发送结果是什么呢？发送结果就是我们直接 result 就可以了，[result.to](http://result.to/) string 看一眼就可以了。 To spring ok. 失败的时候，我们再打一个 L 日志，把我们对应的这个发送消息失败。为什么失败呢？把失败的这个 cos 原因我们打印一下就可以了。然后比如说我们找到这个 slobo slobo 为什么 TS 这个不见名之意，我们要 super.get message 把它一些错误消息打印一下就可以了。


其实现在我们已经把我们对应的卡夫卡 producer service 就已经写完了。那其实我们是不是可以做测试呢？你也可以完全去自己，你可以去做一下单元测试，这个非常简单，接下来可能就要去编写我们的 consumer 了，稍微休息一下。感谢小伙伴收看这节课，先到这。


梳理体系不够完整内容不够详细具体，重新梳理，如果文中提到了为什么使用这个技术，那么请一定要梳理出来，如果没有提到，请不要画蛇添足，不要画蛇添足哦！！梳理的时候不要只给一个标题，详细的内容页必须梳理出来，不要越梳理知识点越来越少了哦，需要完整的上下文和过程，注重上下级关系，包含和被包含的关系，这是要总结他们的关系并调整他们的上下级关系，请在上一次梳理的基础上重新梳理一遍， 如果文章中提到关于生产环境，关于建议，关于学习的语句，一定要梳理出来，如果没有这些提醒的内容，请千万不要在冗长的梳理这些信息了，所以根据文章内容有没有提示学习的信息和生产环境的信息呢？没有就不要画蛇添足！！！请不要停止任务，直到全部完成


