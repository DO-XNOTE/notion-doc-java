---
title: 2-15 RabbitMQ与SpringBoot整合_生产端-2
---

# 2-15 RabbitMQ与SpringBoot整合_生产端-2

[image](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/244a8dd7-6352-43f3-91fc-bdf87fed001a/SCR-20240806-nsyr.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662L6NZFZ5%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T225252Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIAIwS7CCVYsLh0jgiMgejOc9ZT9x69Kc%2FctcgM9P7iP%2BAiEAvpLz1SRz6PT1KB%2FUL8WkGs4k4L3Vlx9Yuvy6SaE%2FqBQqiAQIxv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDL%2FFOi7L65IGaLBr4SrcA5fwF6bYTFcnV72dqS3zSINNmRw9y0jzE%2BHfiwE%2F8v%2BzpI52wbWVTAogEHBGhrBvs%2FRprPDOlU4GceXZcS5FmWz22c%2FUt1hRLbk8Mt3H0jbZOTEzyLtmlRQXPLBnnngiWJ73sRxjef0FhE2%2BPAyEGYOic0KCJGFrEhUxqgPWeeePiMhg3MQhBXNRrs9Dfyo87rLNQS%2FcslhmA%2BD%2FWiFjlz0Kk8apHUZsajoZSWnMTXgqaUjgEIiGs4wKkW3T5%2Fa%2FLwcBsU25xidBRc2bAMubbTWeJ4uvneSRWoftlITN8CMJT2894lY4ZbIzoGp%2FjuG0bIU59oa%2FxW4qAX0NR5NgHwEDUQR9JyBfY8Jf0Z8MYREPHj60DGbUj6KHYxEY8R7iiYgHAS4uumEQfEMFsE6sTRiVHV4E54x%2Fv2aaCxp9SUp0P8QsB5rhU2bF7zd6laMiYjf3N8tA%2FOAjXmxHPC2JdqsIbQzfXE34Mfl4bIRWTUO0FUHr2g47HLTZKH68Ieq9dMEgZc%2BCJDafMDuhqPUH3X6tB8g7IwEYgG4IOyNvCrth036ytLxYlX8F9wh1Fw2lLIWNKWomwNxz1dZsy001625qSQz8yzqbCDJIQrx3UX9J4foivK2RFDNtedsNMMK6%2F9IGOqUBvOeYHnC3R6GGbJUCgMna8BQYcqZaxv%2FhvvZzMgW0li98kgB0oL5EoNnE8dI8woN7znUfDO815dUS0b8iBckrEL3LyaznyNMMVjRD8VKDhqozn%2BmRzUo2c1%2FZtSWxRAi5aWQTtubASLsVddDGuH04GLhxD0%2F9CHbkryCNMxbheEowxuRQ38TjIWHLUyP7foI5dLywhQo1yB9KLs2sKO8KEWTQU%2Fno&X-Amz-Signature=1c94ede98cf28050b66937cdd5f6b606d09736412034e0b38c06859db0b4c200&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

[image](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/df13cb03-3ed6-413d-ae78-6b6f5fe8d0f2/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662L6NZFZ5%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T225252Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIAIwS7CCVYsLh0jgiMgejOc9ZT9x69Kc%2FctcgM9P7iP%2BAiEAvpLz1SRz6PT1KB%2FUL8WkGs4k4L3Vlx9Yuvy6SaE%2FqBQqiAQIxv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDL%2FFOi7L65IGaLBr4SrcA5fwF6bYTFcnV72dqS3zSINNmRw9y0jzE%2BHfiwE%2F8v%2BzpI52wbWVTAogEHBGhrBvs%2FRprPDOlU4GceXZcS5FmWz22c%2FUt1hRLbk8Mt3H0jbZOTEzyLtmlRQXPLBnnngiWJ73sRxjef0FhE2%2BPAyEGYOic0KCJGFrEhUxqgPWeeePiMhg3MQhBXNRrs9Dfyo87rLNQS%2FcslhmA%2BD%2FWiFjlz0Kk8apHUZsajoZSWnMTXgqaUjgEIiGs4wKkW3T5%2Fa%2FLwcBsU25xidBRc2bAMubbTWeJ4uvneSRWoftlITN8CMJT2894lY4ZbIzoGp%2FjuG0bIU59oa%2FxW4qAX0NR5NgHwEDUQR9JyBfY8Jf0Z8MYREPHj60DGbUj6KHYxEY8R7iiYgHAS4uumEQfEMFsE6sTRiVHV4E54x%2Fv2aaCxp9SUp0P8QsB5rhU2bF7zd6laMiYjf3N8tA%2FOAjXmxHPC2JdqsIbQzfXE34Mfl4bIRWTUO0FUHr2g47HLTZKH68Ieq9dMEgZc%2BCJDafMDuhqPUH3X6tB8g7IwEYgG4IOyNvCrth036ytLxYlX8F9wh1Fw2lLIWNKWomwNxz1dZsy001625qSQz8yzqbCDJIQrx3UX9J4foivK2RFDNtedsNMMK6%2F9IGOqUBvOeYHnC3R6GGbJUCgMna8BQYcqZaxv%2FhvvZzMgW0li98kgB0oL5EoNnE8dI8woN7znUfDO815dUS0b8iBckrEL3LyaznyNMMVjRD8VKDhqozn%2BmRzUo2c1%2FZtSWxRAi5aWQTtubASLsVddDGuH04GLhxD0%2F9CHbkryCNMxbheEowxuRQ38TjIWHLUyP7foI5dLywhQo1yB9KLs2sKO8KEWTQU%2Fno&X-Amz-Signature=6988a6c7c139c29d454f0eb85c8ec3248bbc07969c52f5daf9957c8f6903a813&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

接下来我们就进入编码，那我们可以来一个对应的一个新的包，咱们叫做 producer 点component，可不可以就是组件。OK，那 producer 的 component 这个组件我们建立一个类，这个类就用于我们去写 Rabbit MQ 的一些代码，比如说我们叫做 Rabbit MQ 的 sender 发送者，可不可以？没问题。然后我们直接注入就行了，直接把它注入到我们的这个 spring 中，因为它是一个什么呀？它是一个跟 rap MQ 跟我们的这个 spring boot 已经集成了的。那注意怎么去写呢？直接 out to where 的，我们的 Rabbit 直接可以去把 Rabbit template 注入进来，因为他已经帮你去输入化好了的。


OK， Rabbit template 有了之后，我们通过 Rabbit template 就可以去发送消息，那在这里呢？我说我现在想去发送一个什么啊？刚才我配置里配的是一个什么？一种叫做confirm，是不是确认消息？确认消息，大家回忆一下，对于 Rabbit MQ 的确认消息，你需要写一个这个回调的这么一个监听，那这个监听就是我们对应着生产者把消息发出去之后，然后发给布鲁克，布鲁克收到了这条消息以后，然后给我们回送一个 config 应答。那我们根据应答的状态到底是成功还是失败，来确认这条消息是否真的去发放成功了。


好了，那既然是这样的话，那你需要有一个listener，那这个 listener 呢？跟我们的这个 spring boot，跟我们的这个 Rabbit 去整合的时候已经给我们提供了，我们直接可以去在代码里进行这样去写，比如说我定义一个 final 的，注意看我的写法，它叫做 confirm call back，注意在这里你应该选择我们的这个，下面这个叫做 spring smoke a m q p 然后 Rabbit card template。是这个OK，然后我们给起个名字，等于另一个什么呢？用一个 Rabbit template Rabbit template 这个类，然后点 confirm callback，你看这里面有什么，下面这就是 return callback，这就是一个 confirm callback，我们来重写它的一个 confirm 方法就可以了，听见了吗？好了，注意这里边老师打个注释，这里就是确认消息的回调监听接口，对吧？然后用于确认消息是否被 broker 所收到，好了，你只需要重写这个 confirm 方法就可以了。


这个 confirm 方法里边有两个比较关键的这个参数。第一个叫做 calculation date，那这个 calculation date 是干什么的？对于这个 coloration date，在这里我要说一下，对于这个 coloration date，一般来讲它就是作为一个唯一的标识。为什么这么说？比如说你生产者你发了一条消息，你发到 MQ 了，那 MQ 给你回送 ACK 的时候，是不是你怎么知道说这条消息被确认了呢？是不是你们之间得通过一个统一的标记来确认这事儿？所以说这个 calculation date 一般来讲你可以去做唯一的标识，当然你也可以做自己一些特殊化的处理都可以的。然后接下来第二个参数叫做布尔类型的ACK，那这个就是我们的 broke 是否落盘成功，就是消息是否到达 broke 了。可以这么理解，如果是 true 的话那就成功，如果是 false 的话就失败了，对吧？这没什么可说的，那接下来就是失败，它会给你一个这个 Cos 的原因，它会给你一个这个对应的这个失败的一些异常信息，会给你回送。


好了，那基本上这就是这个回调接口，我们已经写完了。那对于这个回调接口呢？我们暂时你先不用去管哈他需要做什么事情，总之这个对象就是回调接口的这个对象我们搞定了，那接下来我们要做什么事情，我们就来写具体的发送消息的方法好了，那如何去发送消息？因为它是一个component，它肯定是被别人去注入 out where 进去，然后去调用它的一个方法，比如说调用它的一个简单的 send 方法，对吧？所以说我们就可以去做 public void，然后stand，然后这个 send 什么呢？我们可以 send 一个 object message，这都可以的。然后给他传一个map，这个 map 我们可以这样去定义，叫做 proper case，然后这里边 throws 我们的 e x， e p t o n exception。


好，我现在定义了一个真正对外发送消息的一个方法。发送消息的方法，然后第一个就是具体的消息内容，然后额外的附加属性好了，我就可以这样去定义好，然后我们看看怎么去写吧。


对于这个 spring boot 整合 write MQ，它里边有一个 message headers，这个 message headers 用来干什么的？注意这个 message headers 一定你别选错了，别选这个 COM 点send，你应该选一个 spring 的，OK，这个里边它主要是对它的这个额外的属性附加的属性进行一个封装。在之前我们学 rap MQ 基础 API 的时候，应该也见过这种东西，比如说一些过期时间，还有一些优先级都可以存到这个 practice 里。但是在我们所用 boot 整合的时候，那你就得按照 AMQP 的规则了，它是这些附加的属性封装到了这个 message 海德斯里边。这个海德斯里，那我们来看一下，在这里边就是 new 一个 message hiders，然后把我们的这个 practice 给直接扔进去就好了。然后接下来那我们如何去创建一个message？这里面抛一个错，看一看 is not defined，我看一下他这个map，他就选错了，我们选 COM 点 send 点 Java FX，是不是？这是我的问题，来看一下这个map，看这个肯定不对哈，然后这个 map 我们应该选什么呀？ Java util 的，对吧？好了，搞定了之后，我把它这个往上移一移哈，我们再来看这个headers，我们已经有了。


然后接下来我们是不是要构造一条消息，然后争取把这个消息发出去就可以了，对吧？那怎么去构造消息呢？还是一样的 spring MQP 呢？它本身给我们提供了这个消息的这个构造器，我们可以用 message builder m e s message builder 注意我们用什么呀？ spring 的 a m q p 的或者是这个 support 都可以，你看上面用的是哪个？上面用的是我们的这个messaging，那我们这个也用这个 messages 也可以了。然后这里边其实 message builder 可以直接点 create 一个 message critic message，你看它两个参数，第一个是 play load，就是你的实际的内容消息的实体，它是一个 t 范型，我们直接放到这里就可以了。


然后 message headers 就是我们的 message headers，OK，好了，创建好了以后它肯定会返回值，是因为它是一个构造者模式，我们该点进去代码，你看这个 message 是不是注意这个message？其实我跟你说，在你写 message 的时候，其实有好多叫 message 的 MSG 配置，你说你到底选哪个，你自己都不知道对不对？没关系，你直接到这里边去看是不是message，然后 message 就可以了，这肯定就保证不会出错了，就这个message。然后这里边需要有一个泛型，就是如果你这里边带泛型的话你就写上，如果不带的话你就写个问号，这种可以，对吧？OK，或者你不写，这也可以所谓。


然后接下来我们来看一看，接下来这个消息已经构造好了，对吧？消息构造好了之后，我们是不是就利用我们的 template 帮我们去把消息发出去，那在发出去之前你要做什么事情？你要注意我们现在用的是什么呀？用的是 confuse config 模式，需要做什么？需要做一个 listener 监听，所以说在我们发消息之前就是直接 list 点 rabbit template。点什么呀？点 set confuse callback， confirm call back 有没有？已经有，就是我们上面声明了这个 final 的 confirm callback 这个对象，对吧？然后搞定了这个事情之后，我们可以做什么事？我们可以真正的去把消息发出去，比如说 Rabbit template，然后点 convert and sand。

```java
package com.bfxy.rabbit.producer.componet;

import org.springframework.amqp.AmqpException;
import org.springframework.amqp.core.MessagePostProcessor;
import org.springframework.amqp.rabbit.connection.CorrelationData;
import org.springframework.amqp.rabbit.core.RabbitTemplate;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.messaging.Message;
import org.springframework.messaging.MessageHeaders;
import org.springframework.messaging.support.MessageBuilder;
import org.springframework.stereotype.Component;

import java.util.Map;
import java.util.UUID;

/**
 * <h1></h1>
 */
@Component
public class RabbitSender {

    @Autowired
    private RabbitTemplate rabbitTemplate;

    //    @RabbitListener
    private RabbitTemplate.ConfirmCallback confirmCallback = new RabbitTemplate.ConfirmCallback() {

        /**
         *
         * @param correlationData 作为唯一标识
         * @param ack 是否落盘成功
         * @param cause 失败的一些异常消息
         */
        @Override
        public void confirm(CorrelationData correlationData, boolean ack, String cause) {

        }
    };

    public void send(Object message, Map<String, Object> properties) throws Exception {

        MessageHeaders mhs = new MessageHeaders(properties);

        Message<?> msg = MessageBuilder.createMessage(message, mhs);

        rabbitTemplate.setConfirmCallback(confirmCallback);

        // 指定业务单位唯一 ID
        CorrelationData correlationData = new CorrelationData(UUID.randomUUID().toString().trim());

        MessagePostProcessor mpp = new MessagePostProcessor() {
            @Override
            public org.springframework.amqp.core.Message postProcessMessage(org.springframework.amqp.core.Message message) throws AmqpException {
                System.out.println("post to do: " + message);
                return message;
            }
        };

        rabbitTemplate.convertAndSend(
                 "exchange-1",
                "springboot.rabbit",
                             msg,
                             correlationData
        );
    }
}
```

注意在这里里面有好多好多这种重载的方法，这种重载的方法我们尽量选一个最多的，然后跟大家把这些东西相关的一些你需要注意的一些东西要跟大家说一下，然后你比如说我现在你看到这个是不是很多？第一个要你填什么呀？exchange，就是你具体的 exchange 是什么？我们可以去添这个 exchange 杠 1 可以，然后 routing key 就是你的路由的 key 是什么？我们可以说 spring boot 点 a d， c 可不可以？或者是 spring boot 点Rabbit，这都是可以的。然后 message 就是你具体的消息，就我们现在已经封装好了的这个 message 直接可以放到这里好了，然后我们来换行。


接下来叫做什么呀？还有一个叫做 message post processor。什么意思？当我们消息发送完之后，我可以做一个回调函数，这个里边我们可以做一个回调，注意你要用这个message，然后把它 new 出来，当然它是一个接口，你要里边把它实现之后要重写一个方法，就是看叫做 post message 就是你做完了这件事情你可以做什么？我们其实也可以实现最后一个叫做calculation， calculation 的目的是什么？它就是用来做一个唯一的标记，那这个唯一的标记呢？其实你应该提前把它设置好，比如说我现在在这里直接把这个 calculation date，我们叫CD，等于 new 1 coloniation，看它就是new，然后这里面就是可以传一个唯一的ID，唯一的 ID 你就可以去搞一个什么UUID，这是可以的。


第二， random to spring，就搞一个这个UID，然后把这个population，当然我就用这个群称好放进去了，这样的话是不是就搞定了？它有一个报错，他说第四个参数是一个 calculation date，这里边我看一下，可能我们范形不对。


string，然后有一个 final object，接下来有一个什么呀？叫做final，我们的这个 post processor，然后是我们的这个它叫做 Aug spring from work，点AMQP，点rabbit，点connection，第二 calculation date，对吧？OK，那我们看看我们这个是不是， connection currently，对，这没问题，我们还给我一个提示，我们比如说我们 remove 一个，OK，我们这个我们你不能那么去用，你可以去先把它弄出来之后，然后你这样去回调。有些问题我们先不用它。好，我们先这样。唉，你看这样是没问题的，但是这个后面有个小报错啊，少了一个分号，OK，好了，这样的话你就是指定了什么呀？业务唯一的 ID 可以了，那么现在没问题之后，我们再回过头来看一看，就是刚才那块有什么问题，为什么我指定一个 post processor，它会给我们提示错误，然后对应着这个东西？我其实来直接写一写 message post processor，然后我们看一下，然后咱们叫做MPP，等于你有一个 message post processor，OK，因为这个方法，然后我刚才是把这个 MPP 放到这里边，他报错了对不对？来，看好，他确实报错了，看他提示什么，他说的 master 的 convert and send 什么什么什么 arguments not a playable 就是不可用的，那是不是我们这个参数传错了？我们来看一看。


注意你要怎么去看这种问题，你要点进去，然后去看对应核对具体的参数。你看这个 message post processor 这个东西，它属于奥克点，我们的 spring from work AMQP call，看看这，这是 call 报下的 message post processor。


然后我们来看看我们自己的，是不是我们自己呢？是，唉，不是我们自己是message，是不是他这个是 message 吗？我们来看一看这个 post processor，我们看它是 AMQP . com，我们自己给错类了，我们自己给的是 message . com，对不对？所以说那这个是不对的，这是不对的，我们应该重新回过头来，然后用什么呀？ AMQP 这个号，我们把上面的那个 message 给它就给去掉，我们叫做 message post processor，你看只有两个，你到底用哪个？是不是你应该用这个 MQP 的MPP，然后等于又一个这个 message post process，OK，好了，这回你看他就不报错了，对不对？然后他会给你一个message，你可以对 message 进行一个什么呀？后续的一个处理，是不是我们直接把这个 message 打印就可以了？是不是我们直接 return message，然后在这里去打印一下，打印一下 host Todo，然后再加上一个message，可以，这完全没问题，就打印一下了。


OK，OK，那现在其实我们已经算把我们整个的这个生产端的代码已经写完了，是不是生产端其实非常简单，就是一个 rabbit listener，然后其实后面你可以写对应的这个单元测试了，然后就可以测试这段代码到底能不能把消息发到 broker 了。好了，那么这节课我们就已经把生产的代码暂时写完了，测试我们后面再写，我们下节课就开始对消费端来做一些代码的编写了，感谢小伙伴们。




