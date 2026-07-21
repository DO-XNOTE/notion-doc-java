---
title: 2-16 RabbitMQ与SpringBoot整合_消费端-1
---

# 2-16 RabbitMQ与SpringBoot整合_消费端-1

[image](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/f875fbf8-5a99-4176-a96c-39a0930d64d5/SCR-20240806-nvpt.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662RFVESFQ%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T225253Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIC8WlbZ9xfOHdnyAtvEo0ymgU6ae0P3pukpNTDySqVf1AiEA%2FybtbBYLwxdc48W4s4gEvx0WckSD0SrKvZjCMuGz4icqiAQIxv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDGe28elB6X5FiqjE4CrcA%2FCc0X4yiBZ5ywulqnBBmuwyTDaoKtLFxS43J3PJPyBtou5r64XzqoHd%2BbaQ0P0zGWHosG7vpY7Xd1i1Ucf%2FXBlvxuCtnOlY5cbNob%2BRmw8rAvw9XCSllzoaEXXj6dtDUDtrgVg0JCpceoadhTQZUgNrg262WE%2FSbaKtqrPraZcW6uGX9kHdkJnfynManPRCfTnExrpphhgtoSveBqRze5KAkKC6g8o5CLlzhwip%2ByNFqCB3MHjiEaeCAvPF1EqsvyZDq0xBam8CS4q7XgnZ2jNeKBmnHOiXP0vKGw4ymWySWTzwe1Ue%2FVXfGYILZerO0oEni0XZsOfaEF4kQnbl765Hss4UBEc6MT%2F5M74KYdD05Gvtf3qe7CKdfu07W63NsAJrBdkcG%2BqVGf9nwPmTLYf%2FJ80%2BZHkr3mnOuS6n3m%2Bw%2BGBxf8d7cQBO%2F745ED30D35bfOiMvd0jgDYhZfRw8zW3y1KFrraaVhYwvdJO1Dp%2FRb9aovDTGw0CoPirdAhp1LFnvefjyBpqWhAIV5jWknonaqPO9iVqbO02SJds7XYQCjSzPypV2KyPc6uX3oyVxbNkmfyCV0lcHqpKA8guqnWhGbch%2BdfHX2edkOy98twEDwpwTRf317sgNdQGMJ23%2F9IGOqUBd3y8q0ITsOnvX5HmhCRzeIEapNJJz6igoIdwQbxPSh8ZbiKoMq6t9H6M0AzqfnwOk7N4FCj0NehGBZ6iU6a7fv2VHeemf66cwfflvngaoLSYmdB%2FTS5vhOcKF%2F8bCXJCurk9B4NnkzRvqpiWJKjopMlbMaInOqhhUT9449atnBLbGl%2B4CjxUuf2TgOzS8qCcb4R0mz77b9jilcBfbNrCQd7mSvUJ&X-Amz-Signature=5b33e0e93fa3ad6d620014f74edfda08c4135b20856ff4a84f26e5ed4e1e7151&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

[image](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/3f35e22d-3204-4782-bd5d-00038abccc80/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662RFVESFQ%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T225253Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIC8WlbZ9xfOHdnyAtvEo0ymgU6ae0P3pukpNTDySqVf1AiEA%2FybtbBYLwxdc48W4s4gEvx0WckSD0SrKvZjCMuGz4icqiAQIxv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDGe28elB6X5FiqjE4CrcA%2FCc0X4yiBZ5ywulqnBBmuwyTDaoKtLFxS43J3PJPyBtou5r64XzqoHd%2BbaQ0P0zGWHosG7vpY7Xd1i1Ucf%2FXBlvxuCtnOlY5cbNob%2BRmw8rAvw9XCSllzoaEXXj6dtDUDtrgVg0JCpceoadhTQZUgNrg262WE%2FSbaKtqrPraZcW6uGX9kHdkJnfynManPRCfTnExrpphhgtoSveBqRze5KAkKC6g8o5CLlzhwip%2ByNFqCB3MHjiEaeCAvPF1EqsvyZDq0xBam8CS4q7XgnZ2jNeKBmnHOiXP0vKGw4ymWySWTzwe1Ue%2FVXfGYILZerO0oEni0XZsOfaEF4kQnbl765Hss4UBEc6MT%2F5M74KYdD05Gvtf3qe7CKdfu07W63NsAJrBdkcG%2BqVGf9nwPmTLYf%2FJ80%2BZHkr3mnOuS6n3m%2Bw%2BGBxf8d7cQBO%2F745ED30D35bfOiMvd0jgDYhZfRw8zW3y1KFrraaVhYwvdJO1Dp%2FRb9aovDTGw0CoPirdAhp1LFnvefjyBpqWhAIV5jWknonaqPO9iVqbO02SJds7XYQCjSzPypV2KyPc6uX3oyVxbNkmfyCV0lcHqpKA8guqnWhGbch%2BdfHX2edkOy98twEDwpwTRf317sgNdQGMJ23%2F9IGOqUBd3y8q0ITsOnvX5HmhCRzeIEapNJJz6igoIdwQbxPSh8ZbiKoMq6t9H6M0AzqfnwOk7N4FCj0NehGBZ6iU6a7fv2VHeemf66cwfflvngaoLSYmdB%2FTS5vhOcKF%2F8bCXJCurk9B4NnkzRvqpiWJKjopMlbMaInOqhhUT9449atnBLbGl%2B4CjxUuf2TgOzS8qCcb4R0mz77b9jilcBfbNrCQd7mSvUJ&X-Amz-Signature=69bdeab52e767c77b6d78b34774ec47f7128ef7f3c0b3500b09912a60dc452cd&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

[image](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/4f1d8492-523a-4d59-9944-1e34b2a49bbd/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662RFVESFQ%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T225253Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIC8WlbZ9xfOHdnyAtvEo0ymgU6ae0P3pukpNTDySqVf1AiEA%2FybtbBYLwxdc48W4s4gEvx0WckSD0SrKvZjCMuGz4icqiAQIxv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDGe28elB6X5FiqjE4CrcA%2FCc0X4yiBZ5ywulqnBBmuwyTDaoKtLFxS43J3PJPyBtou5r64XzqoHd%2BbaQ0P0zGWHosG7vpY7Xd1i1Ucf%2FXBlvxuCtnOlY5cbNob%2BRmw8rAvw9XCSllzoaEXXj6dtDUDtrgVg0JCpceoadhTQZUgNrg262WE%2FSbaKtqrPraZcW6uGX9kHdkJnfynManPRCfTnExrpphhgtoSveBqRze5KAkKC6g8o5CLlzhwip%2ByNFqCB3MHjiEaeCAvPF1EqsvyZDq0xBam8CS4q7XgnZ2jNeKBmnHOiXP0vKGw4ymWySWTzwe1Ue%2FVXfGYILZerO0oEni0XZsOfaEF4kQnbl765Hss4UBEc6MT%2F5M74KYdD05Gvtf3qe7CKdfu07W63NsAJrBdkcG%2BqVGf9nwPmTLYf%2FJ80%2BZHkr3mnOuS6n3m%2Bw%2BGBxf8d7cQBO%2F745ED30D35bfOiMvd0jgDYhZfRw8zW3y1KFrraaVhYwvdJO1Dp%2FRb9aovDTGw0CoPirdAhp1LFnvefjyBpqWhAIV5jWknonaqPO9iVqbO02SJds7XYQCjSzPypV2KyPc6uX3oyVxbNkmfyCV0lcHqpKA8guqnWhGbch%2BdfHX2edkOy98twEDwpwTRf317sgNdQGMJ23%2F9IGOqUBd3y8q0ITsOnvX5HmhCRzeIEapNJJz6igoIdwQbxPSh8ZbiKoMq6t9H6M0AzqfnwOk7N4FCj0NehGBZ6iU6a7fv2VHeemf66cwfflvngaoLSYmdB%2FTS5vhOcKF%2F8bCXJCurk9B4NnkzRvqpiWJKjopMlbMaInOqhhUT9449atnBLbGl%2B4CjxUuf2TgOzS8qCcb4R0mz77b9jilcBfbNrCQd7mSvUJ&X-Amz-Signature=f606555cd9038426fc43a318cf0f969839473be9c69be09116ad93c280060647&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

那接下来我们开始编写我们消费端的代码，其实和生产端类似，我们把这个整个的工程 Ctrl c copy 一份，然后把这个下改成我们 rapid 杠什么呀？ consumer 对应着你可以把它对应着这个包名，可以改改consumer，然后以及在这里我们不着急这个我们改成consumer。然后还有哪些？比如说对于这个 application 点 practice 里边肯定对应着关于这个publish，这些东西我就可以不要了，然后可能上面这些可能还需要我们暂时先保留一会再说，先保存一下，那对应着这个 Maven 就是 Pom 文件肯定需要改，这块肯定需要变成 Rabbit 杠consumer，然后其他的可以保持不变。


好了，那我们来回过头来看一看，对应着我们现在对于 consumer 它的配置应该如何去做？应该如何去配？我们之前有了这个 IP 端口，然后接下来对应着这些用户名密码， v host， time out，对吧？然后我们看一看那 provider 就是消息的生产者，是什么呀？是这个publish，消费者还记得吗？它叫做listener，叫做 Rabbit MQ，点listener，你看到这个 listener 里边有好多好多对应的，你可以设置的，那其实我们可以用什么呀？simple，就是简单的 acknowledge model。


默认是什么呀？可以用什么呀？就一个menu，就是手工默认是什么？默认是那个 all to，我们现在用手工签收，在这里老师打字注释表示消费者消费成功消息以后需要手工的进行签收，也就是手工的去做 ACK 操作。然后在这里我打个注释，默认为凹凸自动，然后我把这个 menu 去掉，比如说你看这里边有一个，它就是里边有两个选项，一个凹凸，一个menu。

[image](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/197f9476-8371-4836-833b-7f703940ff36/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662RFVESFQ%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T225253Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIC8WlbZ9xfOHdnyAtvEo0ymgU6ae0P3pukpNTDySqVf1AiEA%2FybtbBYLwxdc48W4s4gEvx0WckSD0SrKvZjCMuGz4icqiAQIxv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDGe28elB6X5FiqjE4CrcA%2FCc0X4yiBZ5ywulqnBBmuwyTDaoKtLFxS43J3PJPyBtou5r64XzqoHd%2BbaQ0P0zGWHosG7vpY7Xd1i1Ucf%2FXBlvxuCtnOlY5cbNob%2BRmw8rAvw9XCSllzoaEXXj6dtDUDtrgVg0JCpceoadhTQZUgNrg262WE%2FSbaKtqrPraZcW6uGX9kHdkJnfynManPRCfTnExrpphhgtoSveBqRze5KAkKC6g8o5CLlzhwip%2ByNFqCB3MHjiEaeCAvPF1EqsvyZDq0xBam8CS4q7XgnZ2jNeKBmnHOiXP0vKGw4ymWySWTzwe1Ue%2FVXfGYILZerO0oEni0XZsOfaEF4kQnbl765Hss4UBEc6MT%2F5M74KYdD05Gvtf3qe7CKdfu07W63NsAJrBdkcG%2BqVGf9nwPmTLYf%2FJ80%2BZHkr3mnOuS6n3m%2Bw%2BGBxf8d7cQBO%2F745ED30D35bfOiMvd0jgDYhZfRw8zW3y1KFrraaVhYwvdJO1Dp%2FRb9aovDTGw0CoPirdAhp1LFnvefjyBpqWhAIV5jWknonaqPO9iVqbO02SJds7XYQCjSzPypV2KyPc6uX3oyVxbNkmfyCV0lcHqpKA8guqnWhGbch%2BdfHX2edkOy98twEDwpwTRf317sgNdQGMJ23%2F9IGOqUBd3y8q0ITsOnvX5HmhCRzeIEapNJJz6igoIdwQbxPSh8ZbiKoMq6t9H6M0AzqfnwOk7N4FCj0NehGBZ6iU6a7fv2VHeemf66cwfflvngaoLSYmdB%2FTS5vhOcKF%2F8bCXJCurk9B4NnkzRvqpiWJKjopMlbMaInOqhhUT9449atnBLbGl%2B4CjxUuf2TgOzS8qCcb4R0mz77b9jilcBfbNrCQd7mSvUJ&X-Amz-Signature=41d549e8d3ea53a9d427265aa225a04370b6899dc4cd24d8b07d34cc51e08239&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

好了，那接下来我们搞定了这个事情之后，还记得吗？他有一些什么concurrently，对不对？其实都是 simple 相关的，我们点就是有一个 concurrently 线程数，是吧？我们可以哎，最大是5，这都没问题。然后 simple 这里边还有一些其他的，比如说我们这里边有一个什么不是 fetch 默认的这个批量消息的消费，是不是我们一条一条消费就写个 1 就好了？然后还有一个什么，这里边还有一个什么麦克斯坦克最大，比如说10，OK，那现在对于这个配置已经基本上配置好了，那接下来我们来看一看我们如何去编写代码了。


配置是搞定了，然后看代码，那这个我给它改成 8002 吧，之前那是8001，是吧？那这个我改成8002，那这个改成 8. 02，然后这个里边 consumer confirm 肯定不需要它，把它干掉就好了，那我们干掉，然后这个类其实还是需要的。那我们来看这个 consumer component 里边应该怎么去写代码？刚才我们叫做 Rabbit Sander，是吧？看一看叫做 Rabbit Sander，那这个就对应吧，叫 Rabbit receiver。瑞贝整个大写，叫做 Rabbit reserver 好了，然后他肯定也要把它注入到我们的这个 spring 中，就是 component 当成一个组件去做。


还记得我们之前怎么去写的吗？最大化一下很简单，就是你要对 Rabbit listener 它那个组合注解进行一系列的编码和配置，对吧？首先我们先不管3721，我们先把对应的这个监听消息的一个方法先写好，你 public y 的，咱们叫做 on message，这个名字你随便去起，无所谓， m e s c h e 然后这里面参数其实有两个。第一个比如说你就是message，是不是你这个 message 你可以去选择，就是我们的这个 spring a m q p 集成的那个 message 的message，你注意千万别选错了，别选那个 a m q p 的call，你应该选这个 promote message，这里边有范形，我们既然就是开始没规定的是object，所以说可以写个空。


然后接下来比如说你现在还要使用那个通道，就是比如说你要一个channel，这个 channel 你就可以是 Rabbit 原生的 channel 了，比如说你就写这个 Rabbit client 的 channel 就好了。然后接下来我们来看一看，比如说他也要抛一个长吧。好了，好，现在这个监听的这个方法写完了，然后你要注意有个注解叫做 Rabbit handler，对吧？ Rabbit handler 这个注解加上之后，那就证明这个是要监听的。

```java
package com.rabbit.consumer.componet;

import com.rabbitmq.client.Channel;
import org.springframework.amqp.rabbit.annotation.*;
import org.springframework.amqp.support.AmqpHeaders;
import org.springframework.messaging.Message;
import org.springframework.stereotype.Component;

/**
 * <h1></h1>
 */
@Component
public class RabbitReceive {

    /**
     *   @RabbitListener 和 @QueueBinding  和 @Queue  和  @Exchange 的组合使用
     * @param message
     * @param channel
     * @throws Exception
     */
    @RabbitListener(
            bindings = @QueueBinding(
                    value = @Queue(value = "queue-1", durable = "true"),
                    exchange = @Exchange(name = "exchange-1", durable = "true", type = "topic", ignoreDeclarationExceptions = "true"),
                                               key = "springboot.*"
            )

    )
    @RabbitHandler
    public void onMessage(Message message, Channel channel) throws Exception {
        // 1: 收到消息后进行业务端处理消费处理
        System.out.println("-------------------------------------------------");
        System.out.println(" 消费消息-----------------------" + message.getPayload());

        // 2: 处理完成之后获取 deliverTag 并进行手工 ACK 签收操作，因为我们配置文件配置的是 手工签收
        // spring.rabbitmq.listener.simple.acknowledge-mode=manual
        Long deliverTag = (Long)message.getHeaders().get(AmqpHeaders.DELIVERY_TAG);

        channel.basicAck();

    }

}
```

然后你就要开始配置 Rabbit listener，就是比较关键的 Rabbit listener，这个 Rabbit listener 它里面下面还有一个 Rabbit listener，是就是一个负数，我们先用单数，然后这里边大括号，这里边可以加一堆的配置。首先第一个就你要保定 boundings， boundings 有一个 cleaning 


bounding，这个 cleaning bounding 你要做什么？就是你要做哪一个和哪一个之间的绑定，那你肯定是我们的队列跟交换机之间有一个绑定关系。然后昆宁邦定里边我们怎么去写代码？我们来看一看，这里边你可以提示你会看到它什么，有exchange，还有什么呀？还有对应着我们看到的这个一些value，这个就是队列嘛，你看 value 这里边有个 queen q u e，所以说你开始可以写一个 value 等于什么呢？可书写叫 q u u e Queen，然后这个 queen 你可以去证明一个value，然后它的名字比如说咱们叫做 q e e 杠一，然后还有什么呀？这个 double 是否持久化？那你肯定是设成处为持久化了，所以像这种注解，它可能都是什么呀？都是以 string 类型的，它默认是什么？它 default 默认是一个空的串好了，然后 Y6 搞定了。


接下来第二个参数是不是逗号？来，我们改看一看。就是我们的 exchange 绑定，肯定是艾特 exchange 这个注解了，艾特 exchange 这个注解，这个 exchange 注解，这里面它叫name，是吧？其实你叫 value 也可以，它是新版本，可能有点变化，这 its 甚至 name name，我们可以给它起个名字叫做 e x change 杠 1 可以。然后还有什么呀？是否水笔画，对吧？第二步 apple 也是等于，我们就等于 true 字符串，然后还有什么你想一想。还有最关键的就是它的这个type，就是这个 exchange 类型，可以设置，因为我们要路由，可以设成topic。然后还有一些其他相关的，我们可以就是按括号给他回个车，让大家看得清晰一些。


还有比如说你可以直接看，就是有忽略这个 direct exception，就是声明异常，你可以如果你想忽略的话，你处还有其他的吗？看一下基本上凹凸 delete 是否是删除，然后delay， delayed 就是延迟渗透这一些附加参数，它的 means 管理员相关的不用去考虑了。好，我们暂时写到这里。然后最后现在队列跟我们的这个 x n 交换机已经作为一个绑定起来了，但是它们之间的这个路由的 routing 是什么？是不是 routing key 是什么？这是最关键的。


我们之前说 spring boot 点什么的a、b、c、 d 是不是什么都可以，对吧？因为我们回过头来看之前的生产者的发送的代码，我看到了生产者发送代码是 spring boot 点什么Rabbit，那后面这个点我们是不是可以用星去代替？所以说你可以整个规则，你说四分部的点星匹配任意的这个一个单词都可以。


好了，那这样的话我们发消息的时候肯定会被这个消息的消费者所监听，那这样的话对于我们的这个监听已经写完了，这就是一个组合配置，叫做 listener 和这个 cleaning bounding 以及 Queen 和 exchange 它们之间的一个组合使用监听。


好了，搞定这事以后，那其实我们看看里边代码怎么写在这里。比如说我先打印一行这个分割线，然后我看一看这个消息到底消没消费，是不是？那我是不是可以去做一个？这个我可以再打印一下，比如说我说消费消息，我可以加一个什么呀？我们直接把 message 取出来，它 message 里边有一个叫 get play load，直接取到消息体直接 get play 的，然后打了打印一下好了，然后接下来是不是就完事了？同学们要想一想，肯定没完事，为什么呢？因为我们在 consumer 里面我们配置了一个非常关键的东西，就是我们的这个 econology mode 等于 menu 就手工的去签收，手工签收就证明你代码，你看我这个代码消费消息证明已经消费完了。比如说你做一些数据库的操作，或者做一些幂等等一些业务操作，你消费完了之后，你要做一件事情，就是一定要去手工的ACK。


怎么去手工 ACK 就是通过后面这个channel，这个参数点什么呀？有一个看 basic ACK，这个 basic ACK 后面是否支持批量，我们默认可以写 false 就好了。这个 delivery tag 从哪来？同学们想一想， message 里边肯定没有对不对？ message 里边就是 headers 跟我们的这个 play load，那从哪？还是应该从 channel 里面去找，或者是 play log 里面没有？ channel 里面能不能有呢？是不是我们想一想 channel 里边都有什么东西？你们看到 channel 里面其实就是一些basic，什么比如说去 confirm select，还有就是比如说这个就是开启一些 select 的模式，然后对于交换机一些绑定，然后还有 close 的，还有next， publish 序号什么什么的，你会看到这些都是一些执行的方法。


而我们现在要做的事情是什么？我们现在要是获取那个 delivery tag，如果你对 red MQ 基础的 API 熟悉的话，你应该知道这个 delivery tag 应该怎么去获取。 channel 里肯定是没有的， channel 里肯定你是找不到的，那怎么办？那你一定要通过 message headers，它是通过 headers 给你传过来的，还记得吗？小伙伴们可能很有疑问，说，老师，那我这个 send message 的时候，我这个海德斯里面，难道我要自己去创建一个顶瑞 tag 吗？不需要，这个消息到达 Rabbit MQ 以后，罗克自动会帮你生成一个什么杰瑞塔克，所以说你直接就可以获取。


怎么获取很简单，在这里来看我的写法。跟 spring boot 集成，他帮你做，其实也不是他帮你做， MQP 之前就有叫 get 一个key，这个 key 我们可以写AMQP。海德斯注意叫 delay tag，直接能取到这个 delay tag，它会返回一个object，这个 object delay tag 这个东西是一个什么类型？其实你往下看，它 delivery tag 和这个东西它是一个随机的这么一个浪类型，所以说你要转一下，比如说我们叫 delay tag，然后呢？等于，然后在这里边强转成浪。为什么说是浪类型？你通过它你就知道了，因为 basic ACK 它里边 MQP 基础的 API 里面这个 delay tag 是一个浪，所以说它肯定也是一个浪，就不用说好了。


那这块是做什么事情？最后简单说一下，就是首先第一步我们就假设就是写伪代码，第一步是收到消息以后进行业务端消费处理，处理成功之后是不是获取 delay tag 并进行手工的 a C、 k 操作。为什么呀？因为我们配置文件里面配置的是什么？我们的手工签收模式，比如说你要看到这个，然后手工签收详细就是下面这一块。好了，那我相信小伙伴们应该对这块代码没有什么特别的疑问了。***然后就是之前老师说的，就是说你如果这些东西都写死在代码里，后面如果你要有改动的话就很麻烦，怎么办？我建议小伙伴你都自己去定义一个属性，这个我可以给小伙伴留一个作业，李克夏自己去试一试***。


比如说你收到的是一个订单消息，我们电商城，对吧？ Rabbit MQ，点listener，点 order 订单，然后你可以自己去定义，比如说我定义一个exchange，然后点我可以随便搞一个name，等于我们这叫做什么呀？ order 杠x，甚至这都可以。

[image](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/b5727d67-43d3-4e83-ae23-f1def1aadf73/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662RFVESFQ%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T225253Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIC8WlbZ9xfOHdnyAtvEo0ymgU6ae0P3pukpNTDySqVf1AiEA%2FybtbBYLwxdc48W4s4gEvx0WckSD0SrKvZjCMuGz4icqiAQIxv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDGe28elB6X5FiqjE4CrcA%2FCc0X4yiBZ5ywulqnBBmuwyTDaoKtLFxS43J3PJPyBtou5r64XzqoHd%2BbaQ0P0zGWHosG7vpY7Xd1i1Ucf%2FXBlvxuCtnOlY5cbNob%2BRmw8rAvw9XCSllzoaEXXj6dtDUDtrgVg0JCpceoadhTQZUgNrg262WE%2FSbaKtqrPraZcW6uGX9kHdkJnfynManPRCfTnExrpphhgtoSveBqRze5KAkKC6g8o5CLlzhwip%2ByNFqCB3MHjiEaeCAvPF1EqsvyZDq0xBam8CS4q7XgnZ2jNeKBmnHOiXP0vKGw4ymWySWTzwe1Ue%2FVXfGYILZerO0oEni0XZsOfaEF4kQnbl765Hss4UBEc6MT%2F5M74KYdD05Gvtf3qe7CKdfu07W63NsAJrBdkcG%2BqVGf9nwPmTLYf%2FJ80%2BZHkr3mnOuS6n3m%2Bw%2BGBxf8d7cQBO%2F745ED30D35bfOiMvd0jgDYhZfRw8zW3y1KFrraaVhYwvdJO1Dp%2FRb9aovDTGw0CoPirdAhp1LFnvefjyBpqWhAIV5jWknonaqPO9iVqbO02SJds7XYQCjSzPypV2KyPc6uX3oyVxbNkmfyCV0lcHqpKA8guqnWhGbch%2BdfHX2edkOy98twEDwpwTRf317sgNdQGMJ23%2F9IGOqUBd3y8q0ITsOnvX5HmhCRzeIEapNJJz6igoIdwQbxPSh8ZbiKoMq6t9H6M0AzqfnwOk7N4FCj0NehGBZ6iU6a7fv2VHeemf66cwfflvngaoLSYmdB%2FTS5vhOcKF%2F8bCXJCurk9B4NnkzRvqpiWJKjopMlbMaInOqhhUT9449atnBLbGl%2B4CjxUuf2TgOzS8qCcb4R0mz77b9jilcBfbNrCQd7mSvUJ&X-Amz-Signature=1e932c6e84d50fad3ee94ef1fa5f1359f6c9a23d05ce71ea7274364ee9939421&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

然后你比如说你加其他的，除了有他之外，是否持久化 durable Le？你可以设置成默认可以生成 19 块等于true，然后其他的 type 是什么呀？是不是 type GIP 等于我们就默认是topic，然后还有其他的吗？还有是否什么忽略那个生命异常？甚至你可以加上或者它的路由 key 是什么？路由 key 是不是 rooting key？你可以直接写成 key 等于，比如说我们叫 order 点星是不是可以这么去做？就是这些东西是你自己定义的。那你应该怎么去配啊？像这种东西你是不是可以取到这个配置文件里的东西，然后在这里你可以这样去做，比如说刚才我取到的是这个 exchange name，是它吗？我可以把它替换成 dollar 大括号，然后把这个东西放里边，这样的话它可以帮我去解析，我不知道这么说小伙伴们能不能理解，就叨了大括号的方式去解析，好，我把它还原回来。


OK，然后呢，我在这里打个注释，最好不要在代码里写死配置信息，尽量使用这种方式，也就是配置文件的方式，然后怎么去配？配完了之后怎么办？然后在代码里使用 dollar 画括号的方式进行设置，配置。好，就这样。OK，那我相信现在小伙伴们应该没有什么太多的疑问了。OK，然后呢，这个是当成一个作业哈。好了，这就是我们现在要跟大家讲的这个消费者部分代码已经编写完。



