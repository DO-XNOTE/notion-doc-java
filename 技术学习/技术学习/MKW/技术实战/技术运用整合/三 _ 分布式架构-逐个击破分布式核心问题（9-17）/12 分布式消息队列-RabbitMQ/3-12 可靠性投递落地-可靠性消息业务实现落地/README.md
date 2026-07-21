---
title: 3-12 可靠性投递落地-可靠性消息业务实现落地
---

# 3-12 可靠性投递落地-可靠性消息业务实现落地

[image](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/6ec96d5d-be5a-4bab-b62b-51d63125cf6d/SCR-20240806-rzsa.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YWWRE2ZG%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T225305Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCT8OZCdI3hNjzzxCQu1mGk2Y%2FlA3KM8CY8HojBxjSQvwIgXtT8GCGtoj5XRPAkRPBWvjHRwK2chUW1JKvQGqwToXkqiAQIxv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDHRGJXs%2BJWJvCShbCyrcA2qCAZwm2madlL6SZvX%2FHkkyfsKYRXBnDzrVW7D%2F8psqvc3W6ALptXcJkNoJ6Btfj49%2F6v5nMloLfWV2q%2FupQGeEA7ulqZX%2BzwVBMxpOztPuLShPtQR9eFgGjA%2FmH7kLNzENSnFlBn%2BUs4TFmWw6fp6bemaV2GxbhCUCVP0%2BdKcaOExoRVK3ddU8RJWCdbp0SaJHUbLWmC3UIyQGh5CYmJWYeU3zKscr7T8yW5Jfg4jCt6%2BZF6JP9%2BITs%2BGX00Msxy4y6c8uG%2FCRpco%2FaC%2F3A8ZpBiEtIut9KYQMxfPjTOGNd2%2Fc66%2FGzz%2B9uO19d7LaTBtWPA9L59nT39SMDl87GT%2Fc4OSKD9JXZtWJHQZLObD6gmw6uvZSRPJVp0HmgFYzY3k1ggae5FdN80nfdytspH1b%2F7Xcw%2FiQE4Qt%2BLtp%2BB4DtXZy0Z4vXbWlr%2BqjQ9Q%2FkxiEa0jL%2FpI5iYLRFGRzPiV7Hn%2B30dp2F89ggsSsD%2BxnsHLYcoSn2nxrNskLlXvWtjWfXbnXdsJFEq82OV5qfBxEvc102x5lRNUnXxAyHjf1Fjt2pSPnoByfdjQ9ypq6waVt2k4S9IwPvwXEro4oBv5JP9CUFRDINSUDidhTaTq9zEC0TLOo9U8%2FgCsYMK63%2F9IGOqUBJT7GNb4zMiaic3%2FFvr2KU8G3DhNE5EZlfmOML4wd9C73viPu3uJycFfVHygAlFCxsXhI8Ka8oimJ725o7%2Brwku4w%2FedKGylEbLYPeDK8NrUh0Tne815ZlRNS%2FQo%2Fn%2FJCCm2E58suLCFGj5oehYtPARC0qj3GtjTcYma009q54lpmwReuPl2VjsbntwVVqFcupq48Q4%2FX3DY4tRbnoEqFYqN9zs9R&X-Amz-Signature=c5867d905c769c684749283e14757e6c242d3dba19fb27e1407d1b726fcc3d0a&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

[image](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/1f0d5ea6-6a16-4648-aa08-b3bc5878ca0d/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YWWRE2ZG%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T225305Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCT8OZCdI3hNjzzxCQu1mGk2Y%2FlA3KM8CY8HojBxjSQvwIgXtT8GCGtoj5XRPAkRPBWvjHRwK2chUW1JKvQGqwToXkqiAQIxv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDHRGJXs%2BJWJvCShbCyrcA2qCAZwm2madlL6SZvX%2FHkkyfsKYRXBnDzrVW7D%2F8psqvc3W6ALptXcJkNoJ6Btfj49%2F6v5nMloLfWV2q%2FupQGeEA7ulqZX%2BzwVBMxpOztPuLShPtQR9eFgGjA%2FmH7kLNzENSnFlBn%2BUs4TFmWw6fp6bemaV2GxbhCUCVP0%2BdKcaOExoRVK3ddU8RJWCdbp0SaJHUbLWmC3UIyQGh5CYmJWYeU3zKscr7T8yW5Jfg4jCt6%2BZF6JP9%2BITs%2BGX00Msxy4y6c8uG%2FCRpco%2FaC%2F3A8ZpBiEtIut9KYQMxfPjTOGNd2%2Fc66%2FGzz%2B9uO19d7LaTBtWPA9L59nT39SMDl87GT%2Fc4OSKD9JXZtWJHQZLObD6gmw6uvZSRPJVp0HmgFYzY3k1ggae5FdN80nfdytspH1b%2F7Xcw%2FiQE4Qt%2BLtp%2BB4DtXZy0Z4vXbWlr%2BqjQ9Q%2FkxiEa0jL%2FpI5iYLRFGRzPiV7Hn%2B30dp2F89ggsSsD%2BxnsHLYcoSn2nxrNskLlXvWtjWfXbnXdsJFEq82OV5qfBxEvc102x5lRNUnXxAyHjf1Fjt2pSPnoByfdjQ9ypq6waVt2k4S9IwPvwXEro4oBv5JP9CUFRDINSUDidhTaTq9zEC0TLOo9U8%2FgCsYMK63%2F9IGOqUBJT7GNb4zMiaic3%2FFvr2KU8G3DhNE5EZlfmOML4wd9C73viPu3uJycFfVHygAlFCxsXhI8Ka8oimJ725o7%2Brwku4w%2FedKGylEbLYPeDK8NrUh0Tne815ZlRNS%2FQo%2Fn%2FJCCm2E58suLCFGj5oehYtPARC0qj3GtjTcYma009q54lpmwReuPl2VjsbntwVVqFcupq48Q4%2FX3DY4tRbnoEqFYqN9zs9R&X-Amz-Signature=34fce54a8da9e2c634c362419a67eea441a48b8192b0087762268a545402684b&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

这节课我们继续，我们来讲什么呢？就是讲可靠性投递的核心业务逻辑的实现，那这儿呢？我们就跟着小伙伴们一点点编码去做就好了。首先我们来看到核心，找到我们的这个 produce client，打开，然后我们来看 produce client 我们要做什么事情。那既然是可靠性投递，比如说用到这个一个叫做 Rabbit broker，它具体的实现根据发迅速消息，发 confime 消息以及发可靠性消息，是不是就是我们的 Rabbit broker？真正的可靠性消息应该怎么去做？现在我们的可靠性投递就要依赖数据库表了，就是我们说我们在把消息投递的过程中，我们要把这个消息的记录要放到具体的表中，所以说我们看看怎么去做，首先需要点进去领到他具体的实现， rabbit broker implements，我们之前已经领着小伙伴写了一个 can 对不对？然后写了config，然后接下来就是这个了，就是他看看怎么去，徒弟我把它放到最上面，这样的话小伙伴们看着应该更爽一些。


下面的事情我们先不管了，总之这个可靠性投递最终是要干什么？最终也要做这个就是三德克，三德克人相当于把消息直接是扔到 MQ 里了，那在这之前我们要做一个可靠性的事情，那其实通过之前的 PPT 老师也跟同学们讲了，就是我们先要做一个入库操作，对吧？怎么去做这个入库操作呢？那既然是要跟数据库打交道，那我们之前已经写好了的这个 map 是不是得用上了？所以说在这里我们要做的事情是先搞一个 service 出来，这个 service 的目的就是为了做实际的存储的，我们叫做service。那这个 service 我们给它起个名字叫做 messages store service。可以，当然在这里我就不去写什么呢？我就不去写那个接口了，我们直接就把它当成一个这个接口的实现就好了。

```java
package com.bfxy.rabbit.producer.service;

import com.bfxy.rabbit.producer.constant.BrokerMessageStatus;
import com.bfxy.rabbit.producer.entity.BrokerMessage;
import com.bfxy.rabbit.producer.mapper.BrokerMessageMapper;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;

import java.util.Date;

/**
 * <h1></h1>
 */
@Service
public class MessageStoreService {

    @Autowired
    private BrokerMessageMapper brokerMessageMapper;

    public int insert(BrokerMessage brokerMessage) {
        return this.brokerMessageMapper.insert(brokerMessage);
    }

    public void success(String messageId) {
        this.brokerMessageMapper.changeBrokerMessageStatus(messageId, BrokerMessageStatus.SEND_OK.getCode(), new Date());
    }

}
```

message store service。好， message store service，我不写接口了，那就直接写艾特service，对不对？好。然后首先第一件事情就是 auto where，对不对？我们把我们之前的那个 map private，我们的叫做 broker message Mapper 给它注入进来。好，因为我要对数据库操作。那我们之前已经有了这个，对吧？我把它注入进来，这是肯定的。


好了，接下来我们继续往下看应该怎么去做，它里边都有哪些方法？我们来想一想。首先我其他的方法我不知道，但，但是起码有一个音色的方法，对吧？就是当我们去发送一条消息之前，我希望一条发送消息的这个备份一个副本先落地，然后再发消息。根据肯飞，我们回来的时候把状态找到，然后去做一个修改。我们至少有一个 public 返回值是Int，我们叫一个 insert 的方法， insert broker message 就好了，我们至少要做这么一件事情，就是 return this 点。

Book message method insert record.


record 就是我们的 broker message，OK，做完了这件事情了，好，有这个累了之后就好办了，我们再回去，回到我们核心的这个 rapid broker 的实现就在这。那怎么办？首先你要把它入进来，是不是 all to where private？它是不是把 service 搞进来？那我们在发真正的可靠性消息之前，我们要做一次落地，对不对？那在这我们来一起想一想这个代码应该怎么去写。


首先呢，我们肯定要把 broker message 弄出来和message，我们也叫 broker message，等于 new 一个 broker message 出来，然后对它去设置相关的一些它必须要有的信息有哪些？点 set 最关键的是 message ID，那 message ID 是不是通过 message 能够获取 message ID，然后 broker message 点 set 什么呢？比如说它的状态，那状态有哪几种？比如说老师你不是定义了吗？ 0 表示什么呢？ 0 表示已发送，待确认，对吧？但是你不能这样去写，你要写的好一点的话，那我们比如说再建立一个包，这个包其实你放到哪里都可以，你比如说你把它放到 common 里也行。其实如果是 producer 发送状态的话，那我们把它放到 common 里，这也无所谓。OK，那在这里我再建一个package，咱们叫做什么呢？叫做constant。

```java
package com.bfxy.rabbit.producer.constant;

/**
 * <h1></h1>
 */
public enum BrokerMessageStatus {

    SENDING("0"),
    SEND_OK("1"),
    SEND_FAIL("2");

    private String code;

    BrokerMessageStatus(String code) {
        this.code = code;
    }

    public String getCode() {
        return code;
    }

    public void setCode(String code) {
        this.code = code;
    }
}
```

第二， constant 这么一个包在这里首先我要定义一个状态了，这个状态可以是枚举值，对不对？我们叫做 broke message States 可以定一个枚举类叫做 broker message，然后 stays 好，它有哪些？比如说有一个 3 顶的一个枚举值，它是0，对吧？表示消息发出去了，待确认。

[image](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/28009653-b7d6-4a15-92cb-97d0d8246f62/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YWWRE2ZG%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T225305Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCT8OZCdI3hNjzzxCQu1mGk2Y%2FlA3KM8CY8HojBxjSQvwIgXtT8GCGtoj5XRPAkRPBWvjHRwK2chUW1JKvQGqwToXkqiAQIxv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDHRGJXs%2BJWJvCShbCyrcA2qCAZwm2madlL6SZvX%2FHkkyfsKYRXBnDzrVW7D%2F8psqvc3W6ALptXcJkNoJ6Btfj49%2F6v5nMloLfWV2q%2FupQGeEA7ulqZX%2BzwVBMxpOztPuLShPtQR9eFgGjA%2FmH7kLNzENSnFlBn%2BUs4TFmWw6fp6bemaV2GxbhCUCVP0%2BdKcaOExoRVK3ddU8RJWCdbp0SaJHUbLWmC3UIyQGh5CYmJWYeU3zKscr7T8yW5Jfg4jCt6%2BZF6JP9%2BITs%2BGX00Msxy4y6c8uG%2FCRpco%2FaC%2F3A8ZpBiEtIut9KYQMxfPjTOGNd2%2Fc66%2FGzz%2B9uO19d7LaTBtWPA9L59nT39SMDl87GT%2Fc4OSKD9JXZtWJHQZLObD6gmw6uvZSRPJVp0HmgFYzY3k1ggae5FdN80nfdytspH1b%2F7Xcw%2FiQE4Qt%2BLtp%2BB4DtXZy0Z4vXbWlr%2BqjQ9Q%2FkxiEa0jL%2FpI5iYLRFGRzPiV7Hn%2B30dp2F89ggsSsD%2BxnsHLYcoSn2nxrNskLlXvWtjWfXbnXdsJFEq82OV5qfBxEvc102x5lRNUnXxAyHjf1Fjt2pSPnoByfdjQ9ypq6waVt2k4S9IwPvwXEro4oBv5JP9CUFRDINSUDidhTaTq9zEC0TLOo9U8%2FgCsYMK63%2F9IGOqUBJT7GNb4zMiaic3%2FFvr2KU8G3DhNE5EZlfmOML4wd9C73viPu3uJycFfVHygAlFCxsXhI8Ka8oimJ725o7%2Brwku4w%2FedKGylEbLYPeDK8NrUh0Tne815ZlRNS%2FQo%2Fn%2FJCCm2E58suLCFGj5oehYtPARC0qj3GtjTcYma009q54lpmwReuPl2VjsbntwVVqFcupq48Q4%2FX3DY4tRbnoEqFYqN9zs9R&X-Amz-Signature=882150b7d20092824d0d1d76c44bc2755d94d831aeaa182cb8d1786639b2c939&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

还有一个是三顶杠OK，表示发送成功了，对不对？我也确认了，就是我得到这个 broke 给我的 ACK 了，然后还有一个是 3 丁file，就是发送失败，那这个时候是2。然后比如说我们定义它的 code 码 private string code，然后接下来有一个 private 的这个构造方法传进去我们的这个 string code，这里边就是 this 点 code 等于 code 好，然后我们最好再来一个 get code 的方法。


嗯，三十四二，这个是一字串好， public stream get cold 写完了，然后直接 return 再写 code 是不是好？这个类就写完了，它就是来标记我们的这个消息的发送状态了，有了它之后我们再回过头来，那这个是不是就好办了？这个我们直接默认的就是什么 30 点 get code 就相当于什么呢？默认当我们入库了之后，那这个状态就是处于已发送，待确认。然后接下来同学们想一想，我记得说有三个非常关键的，一个是state，还有一个是什么 next retry，还有一个叫做 try count。首先我们思考一下这个 try count 这个东西叫表示重试的次数，我们数据库里肯定是有这个结构的，再看看我们来看一下数据库schema，打开他肯定有 try come 这个字段，但是我们需不需要设置我们第一次发送的时候，其实是不算重试的，这一点小伙伴们要知道，等到我第一次发送失败了以后，在第二次的时候才算重试一次。


所以说当我们刚发的时候，这个 try count 它默认是0，是不需要改的。那其实我们的这个broker，它的这个 entity 实体已经定义了，它的这个 try count 默认就是0，第一次的时候是不需要变的，所以说 try count 在最开始发送的时候不需要进行设置，然后 try count 和 states 这两个参数我们搞定了。


还有一个最关键的就是我们的 next retry，当我们去做重试的时候，我们认为当你已经超过了多长时间，我才会帮你去做同事，那肯定是当前时间加上一个你最大容忍的一个时间，那当前时间呢？我们可以 new date，对不对？我们把这个放到这块，我说 date 等于 new 一个date，然后怎么去做？说当前时间加上多久？那是不是也可以做一个定义？比如说我们之前定义了这个 broker message state，现在我们再定义一个叫做 broker message Cos，就是一个常量，这里边都存储一些常量，所以常量我就用一个 interface 表示了，我们叫做cost，这里边我们有一个 time out 时间，比如说我们默认超时间是 1 秒钟，我叫 time out 等于1。


可以，这就是我们定义的一些常量，常量信息，这个不一定是 1 秒，可以是 1 分钟或者是 1 小时，我现在设置1，那其实我想做的我也不想说，把它这个最大容忍的时间设的太长，因为咱们测试嘛，要设 1 小时的话，你得等 1 小时才能看到结果。所以说在彻底我就设置为 1 分钟。


如果说当前时间加上 1 分钟，你这个消息的状态还是等于三定状态的，那证明你这条数据有问题。因为理论上来讲，你消息发完了，古洛克给我返回ACK，我就应该把这个状态从 0 改成 1 了，也就变成 3 的 OK 的状态了，或者是 3 的 fail 的状态了，不可能一直是三定状态。


那在这里我们是不是就可以做一下，比如说我们日期加 1 分钟，就是我们用 date util 吧， date util 点 at minutes， add minis 就表示时间 1 分钟，那当前时间是no，然后再加上我们的这个一分钟，那这一分钟是什么呢？这一分钟不就是你自己的这个 broker message constant 假太冒是吧？对不对？因为它就是一个变量，它就是一个1，然后具体你爱的分钟就是一分钟。


比如说我们最开始发送的时候，我们就已经要把下一次如果一旦它发失败，或者是一旦 broke 应答的时候出现网络闪断这种情况，我们一定要预计到，所以说我们一定要说下一次 RE 串时间就是我最大容忍的当前时间加上一个 1 分钟，OK，然后接下来还有哪些比较关键的？就是比如说当前的这个 great time 就是 null 就可以了。第二 set great time 就是null，然后还有 update time，那这个 update time 第一次也是null。


还有一个比较关键的就是我们 set 有一个全量的信息，还记得就是说我会保存这个消息的全量信息，那我就把 message 保存进去，见了吗？ set message 嘛，把全量信息保存起来就好了。然后我当前的这个 broker message 这个对象已经搞定了，接下来我就用 service 去做一个 insert 就好了，对不对？就是insert，反正在发确认消息可靠性消息的时候，我先把这个对象入库了。


入完库之后，接下来我做的是发送，发送很简单，我去调一下那个散的客人方法发就好了，就搞定了。就第一步分为两步，第一步是把数据库的消息发送日志先记录好对不对？然后第二步才去执行真正的发送消息逻辑。OK，那在这里其实确认消息是不是我们也应该做一件事情，因为其他我们都做了。你比如说发迅速消息的时候，我们首先设置了type，对不对？等于迅速的，然后发 confirm 的时候也是设置等于 confirm 的，那发那个可靠性，其实为了确保万无一失，你也要这么去做。在发之前我去做这个事情，当然这个就是怕万一有问题，我可以把它做这个事情，并且其实有的时候你发现这个 message 你完全可以设置成 final 的，因为你不需要做修改。


OK，好了，这就是我们真正的发消息的逻辑，就是发消息之前我先把它入库，然后去发送，然后接下来小伙伴们想一个问题，那我更新的时候我怎么去更新它的状态？我之前说了，我们做完发送消息之后会把消息投递给伯克，伯克会给我一个ACK，给我 ACK 的时候我再去更新一下这条消息的space，把 sending 状态改成 send OK，或者是 send file，对不对？那也就是说在 confirm 的时候我们需要再做一些事情，那想一想是在哪里？那其实就是跟我们之前的 confirm 是也是一致的。


confirm 消息做法是什么样子的？我们找到 container 以后，我们找到最后面的内容了，找到 container 之后，他肯定是实现了 callback 方法，说白了可靠性也是依赖于config，只不过比他多了一个入库操作，我们来看找到下面 confirm 对不对？那其实当我们 message ID 能取到，是不是 message 肯定能取到？我们根据这个 message ID 发的时候会有，为什么呢？其实就是在这儿我们做完了入库之后，发克人消息的时候，已经生成了一个 coloration date，这个是跟 confirm 逻辑是一样的，不管是什么样的消息，总会有一个唯一ID，然后加上当前时间戳，然后去再发送跟忘了S3。那既然有它，是不是我们可以去根据它去更新我们数据库里的那个记录？因为我们这个 broker message 它的主键是贴上去的，所以说根据主键回来的时候能去找到具体的记录，然后去更新一下 SIS 就可以了。那我们来看一看这个怎么做吧。


那我们先按照正常逻辑去洗，比如说如果一旦 confirm 回来 ACK 了，那这个 ACK 如果是怵的话怎么办？它是component，所以说是不是它也得需要用到 autowear 的我们的service，因为我们要对数据库进行操作了。 private message 到 service 有了它之后，我期望 ACK 如果是成功的话，我希望调它的一个更新的方法，比如说我们就叫做success，然后把我们具体的这个 message ID 传进来就好。这就是什么呀？当我们的这个 broker 返回 ACK 成功时，我们要做的事情就是更新一下我们的日志表里对应的消息发送状态为 send 杠，OK，是不是？它一开始是三定状态，我们把它变成 send OK 就可以了。那这很简单，我们直接去把它生成，我们直接 create method，直接就是做一个 update 操作。


第二， change broker message state 直接相当于修改消息的状态。注意看我的写法哈，这个状态有 3 个值哈，这个是我提前写好了的，因为我怕这个浪费小伙伴的时间。然后这个状态应该是什么呀？应该就是 broker message 它的这个 states 对不对？ broker message states，点 send OK，点code，然后当前时间就是 data 好，这就发完了，这就是一个 success 方法。


好了，那这个就是说当我们 ACK 成功的时候，我们一定要回来把我们的状态更新成 send OK 的就行了。那同理，有 send OK 的，是不是应该也会有 send file 的，对不对？所以说这个代码我就再加一个，我一并都写了，是不是我们直接叫做feller，也是根据ID，只不过把它状态改成 send fail 就完了。现在这 3 个方法已经搞定了。

```java
package com.bfxy.rabbit.producer.service;

import com.bfxy.rabbit.producer.constant.BrokerMessageStatus;
import com.bfxy.rabbit.producer.entity.BrokerMessage;
import com.bfxy.rabbit.producer.mapper.BrokerMessageMapper;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;

import java.util.Date;

/**
 * <h1></h1>
 */
@Service
public class MessageStoreService {

    @Autowired
    private BrokerMessageMapper brokerMessageMapper;

    public int insert(BrokerMessage brokerMessage) {
        return this.brokerMessageMapper.insert(brokerMessage);
    }

    public void success(String messageId) {
        this.brokerMessageMapper.changeBrokerMessageStatus(messageId, BrokerMessageStatus.SEND_OK.getCode(), new Date());
    }


    public void failure(String messageId) {
        this.brokerMessageMapper.changeBrokerMessageStatus(messageId, BrokerMessageStatus.SEND_FAIL.getCode(), new Date());
    }

}
```

当我们什么时候说 send fail 呢？这个可能是后面的事情，先不用关注好这一块的逻辑我们已经写完了，也就是说当我们确认消息的这个实际的这个业务逻辑就是先入库，然后发消息，等待 confirm 成功，就 ACK confirm 失败，那怎么办？ concern 失败这里面我还没写，其实我可以根据它的这个发送的结果，假设说 MQ 满了的话，那我肯定要做就是满了的事情，满了事情你再重试也白扯，对不对？因为 MQ 已经满了嘛，所以说如果是满了的情况下的话，那我们其实在这里具体的这个 file 哈，你其实还可以改一改其他的逻辑，就是说当我们 confime 的时候，如果返回的失败的结果是不一样的，假如说这块 container 它返回的这个失败，它的这个 Cos 原因是由于我们的这个布鲁克。比如说磁盘满了的话，那这个时候你再重试都白扯，对不对？所以说呢，你是不是应该说这个时候如果是fail，那最终就是 fail 了。

[image](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/a5211427-81c8-4f73-81a4-4b01e395e606/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YWWRE2ZG%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T225305Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCT8OZCdI3hNjzzxCQu1mGk2Y%2FlA3KM8CY8HojBxjSQvwIgXtT8GCGtoj5XRPAkRPBWvjHRwK2chUW1JKvQGqwToXkqiAQIxv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDHRGJXs%2BJWJvCShbCyrcA2qCAZwm2madlL6SZvX%2FHkkyfsKYRXBnDzrVW7D%2F8psqvc3W6ALptXcJkNoJ6Btfj49%2F6v5nMloLfWV2q%2FupQGeEA7ulqZX%2BzwVBMxpOztPuLShPtQR9eFgGjA%2FmH7kLNzENSnFlBn%2BUs4TFmWw6fp6bemaV2GxbhCUCVP0%2BdKcaOExoRVK3ddU8RJWCdbp0SaJHUbLWmC3UIyQGh5CYmJWYeU3zKscr7T8yW5Jfg4jCt6%2BZF6JP9%2BITs%2BGX00Msxy4y6c8uG%2FCRpco%2FaC%2F3A8ZpBiEtIut9KYQMxfPjTOGNd2%2Fc66%2FGzz%2B9uO19d7LaTBtWPA9L59nT39SMDl87GT%2Fc4OSKD9JXZtWJHQZLObD6gmw6uvZSRPJVp0HmgFYzY3k1ggae5FdN80nfdytspH1b%2F7Xcw%2FiQE4Qt%2BLtp%2BB4DtXZy0Z4vXbWlr%2BqjQ9Q%2FkxiEa0jL%2FpI5iYLRFGRzPiV7Hn%2B30dp2F89ggsSsD%2BxnsHLYcoSn2nxrNskLlXvWtjWfXbnXdsJFEq82OV5qfBxEvc102x5lRNUnXxAyHjf1Fjt2pSPnoByfdjQ9ypq6waVt2k4S9IwPvwXEro4oBv5JP9CUFRDINSUDidhTaTq9zEC0TLOo9U8%2FgCsYMK63%2F9IGOqUBJT7GNb4zMiaic3%2FFvr2KU8G3DhNE5EZlfmOML4wd9C73viPu3uJycFfVHygAlFCxsXhI8Ka8oimJ725o7%2Brwku4w%2FedKGylEbLYPeDK8NrUh0Tne815ZlRNS%2FQo%2Fn%2FJCCm2E58suLCFGj5oehYtPARC0qj3GtjTcYma009q54lpmwReuPl2VjsbntwVVqFcupq48Q4%2FX3DY4tRbnoEqFYqN9zs9R&X-Amz-Signature=333fba01f4c28b4377abfa083965c8edb88b1971e6c34d1ed7d6cc0201abc5b6&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

但是还有一种情况，如果说不是说磁盘满了使我们达到预警了，比如说他的这个写不进去了，他的 system busy 了，比如说他自己 OS 级别的，他的这个配置 catch busy 了，对不对？他在写的时候当前是比较繁忙的，他是希望你再过一段时间，等到低峰的时候再写，那这个时候其实我们还可以重试的。

所以说就是根据具体逻辑，你可以再定义一个状态，虽然说fail，但是叫做 a moment，你可以这样去写，就是说你再等一等，可以给他一个状态散。就是当有一些情况下的时候，我们可以去给他定义一些更契合于我们自己业务的一些状态。比如说遇到这种情况下，我们可能不是说 1 分钟了，我们可能 10 分钟，或者是后面半小时之后我们再补偿一下，就这个是根据具体业务需求自己灵活去处理的事情了，唉，写错了，好像 m o m o n t a moment，对吧？ 

[image](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/e93f08bd-3b2a-43de-bd7d-2cd8dcf6f898/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YWWRE2ZG%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T225305Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCT8OZCdI3hNjzzxCQu1mGk2Y%2FlA3KM8CY8HojBxjSQvwIgXtT8GCGtoj5XRPAkRPBWvjHRwK2chUW1JKvQGqwToXkqiAQIxv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDHRGJXs%2BJWJvCShbCyrcA2qCAZwm2madlL6SZvX%2FHkkyfsKYRXBnDzrVW7D%2F8psqvc3W6ALptXcJkNoJ6Btfj49%2F6v5nMloLfWV2q%2FupQGeEA7ulqZX%2BzwVBMxpOztPuLShPtQR9eFgGjA%2FmH7kLNzENSnFlBn%2BUs4TFmWw6fp6bemaV2GxbhCUCVP0%2BdKcaOExoRVK3ddU8RJWCdbp0SaJHUbLWmC3UIyQGh5CYmJWYeU3zKscr7T8yW5Jfg4jCt6%2BZF6JP9%2BITs%2BGX00Msxy4y6c8uG%2FCRpco%2FaC%2F3A8ZpBiEtIut9KYQMxfPjTOGNd2%2Fc66%2FGzz%2B9uO19d7LaTBtWPA9L59nT39SMDl87GT%2Fc4OSKD9JXZtWJHQZLObD6gmw6uvZSRPJVp0HmgFYzY3k1ggae5FdN80nfdytspH1b%2F7Xcw%2FiQE4Qt%2BLtp%2BB4DtXZy0Z4vXbWlr%2BqjQ9Q%2FkxiEa0jL%2FpI5iYLRFGRzPiV7Hn%2B30dp2F89ggsSsD%2BxnsHLYcoSn2nxrNskLlXvWtjWfXbnXdsJFEq82OV5qfBxEvc102x5lRNUnXxAyHjf1Fjt2pSPnoByfdjQ9ypq6waVt2k4S9IwPvwXEro4oBv5JP9CUFRDINSUDidhTaTq9zEC0TLOo9U8%2FgCsYMK63%2F9IGOqUBJT7GNb4zMiaic3%2FFvr2KU8G3DhNE5EZlfmOML4wd9C73viPu3uJycFfVHygAlFCxsXhI8Ka8oimJ725o7%2Brwku4w%2FedKGylEbLYPeDK8NrUh0Tne815ZlRNS%2FQo%2Fn%2FJCCm2E58suLCFGj5oehYtPARC0qj3GtjTcYma009q54lpmwReuPl2VjsbntwVVqFcupq48Q4%2FX3DY4tRbnoEqFYqN9zs9R&X-Amz-Signature=692cc326925858c14f4db5bc9f4c2135ffc33207065a67942d469da24cab9910&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

wait a moment 好了，那么关于可靠性的这个逻辑就已经搞定了。


那其实还有一大部分逻辑是什么呢？就是关于补偿这事，假设说我们的这个网络真的闪断了，我没有收到任何的消息，就是相当于我们的 container 这个 config 的方法，这块压根就没有收到任何的这个 ack，那他肯定更新不了，然后比如说他收到了，但是抽的全是file，投射好几次全是file。那我们是不是在 iOS 的时候也应该做些处理？这后面的逻辑就需要用到我们的这个定时任务，然后在这里我们会讲一下当能网的这个 elected job，就是分布式定时任务。OK，这节课我们先讲到这下节开始我们去针对这个定时任务来进行详细的讲解。首先跟小伙伴们把定时任务整体是干什么的，以及到底怎么去用，先讲解明白，然后再去集成到我们的这个可靠性投递的这个基础组件里面。那这节课先到这感谢小伙伴们收看。


