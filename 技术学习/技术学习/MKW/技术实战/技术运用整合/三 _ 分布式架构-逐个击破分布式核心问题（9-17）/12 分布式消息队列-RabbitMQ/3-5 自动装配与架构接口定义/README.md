---
title: 3-5 自动装配与架构接口定义
---

# 3-5 自动装配与架构接口定义

[image](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/cb83d466-16d1-441c-977d-e8e28f0ee938/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZM6X4Z4W%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T225300Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDeLKI%2FVedfMD5dKmjffvrlzwWilzRrFzBcqwUsus5IOQIhAKN8u0RaSx8oV11%2F8IBECGgEQ2S%2F1X67SEM3vBmPJDWIKogECMb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgwPp8j2lau7KPK8Hk0q3ANMh%2BgfgCmphAMycgvKm5aVznLYQLvb9iUrXZcj4Pw1XYHb%2FjPeIzjnfNvXWNKRBhnd%2BsBh7lWSfZzKzzJhUDLq4IehEm2px6qRFxHUtksEpE7VQl42XuxA2aX4PuukNnXgc9w8TjLpKTI4EpO6yRFiBTeOOi4RJ6KrB2T6%2FmPOfwBexWGnP64JFf1RONggtWEw82465k6l9X5qZsZO5HOkZjH4wufl1uDzrbqVat4aOSXB1yCfOf9mySTLi8yaVRyEF4ci7SHqiszpTVaatoZHLgbwhyADQPQvAMIJK6DnxWmjmpkghWzv7aSHOxCbVdL8lb%2F509u4uPRdhrj0NuRfspl0kc%2BND4k8Xu09jq0smSZKrQSci3ugKVp2a6w8ERwq16X11rsttiNp8gdX6VqC5mthLNK7xqDA54ZfaQLcXZc9AiV8B%2BAVwgYjkZh%2FPcQuU%2FDZ9Fc%2F3owduXaBGgNu%2FBawK2tPtP0KvckhQIM2y8%2BcgB%2BSu85fJxdAtUwJstNEDbxG%2BHLKkDmgBX%2Ft0W56bfbBEn8jC9tk7iaPpmzKE9uFZ5tQzEp7kT9dgHC4BvwOqB%2B3tAHsfuyPfCQ9Ph4K4N1zdQLXcE8BD%2BY3E29SMEI2KtPBZy%2FqdQuupDCNuv%2FSBjqkAbWsq%2BDRsgHDSmHlhWlt9fJ2zjSg1UP2Dam7ZMJ7m%2FrnyjFz7dj24Vi6BWv7Pue2IPLnKjUPfTNqgtTziyF12AMCaQeAVItQDzLyG1Azxg1pqZFRcLXC0Ubc9IErgnc3%2F1SrM7NC0QP%2FbbWTee5j6%2FYgP6%2FG3rY2tFI0Wh3bA4JyR10%2FUnGMbx1far1eOUII2%2FOjT2Y6D2I7evd0s4Hf8Gp%2Bqevl&X-Amz-Signature=4c994a5b89feeb8e1b20bc5742957171191bcfe48d9a64eacb7beff1a6be4e3d&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

[image](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/c1998e41-84bf-41f6-b0d9-d472fd646a5b/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZM6X4Z4W%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T225300Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDeLKI%2FVedfMD5dKmjffvrlzwWilzRrFzBcqwUsus5IOQIhAKN8u0RaSx8oV11%2F8IBECGgEQ2S%2F1X67SEM3vBmPJDWIKogECMb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgwPp8j2lau7KPK8Hk0q3ANMh%2BgfgCmphAMycgvKm5aVznLYQLvb9iUrXZcj4Pw1XYHb%2FjPeIzjnfNvXWNKRBhnd%2BsBh7lWSfZzKzzJhUDLq4IehEm2px6qRFxHUtksEpE7VQl42XuxA2aX4PuukNnXgc9w8TjLpKTI4EpO6yRFiBTeOOi4RJ6KrB2T6%2FmPOfwBexWGnP64JFf1RONggtWEw82465k6l9X5qZsZO5HOkZjH4wufl1uDzrbqVat4aOSXB1yCfOf9mySTLi8yaVRyEF4ci7SHqiszpTVaatoZHLgbwhyADQPQvAMIJK6DnxWmjmpkghWzv7aSHOxCbVdL8lb%2F509u4uPRdhrj0NuRfspl0kc%2BND4k8Xu09jq0smSZKrQSci3ugKVp2a6w8ERwq16X11rsttiNp8gdX6VqC5mthLNK7xqDA54ZfaQLcXZc9AiV8B%2BAVwgYjkZh%2FPcQuU%2FDZ9Fc%2F3owduXaBGgNu%2FBawK2tPtP0KvckhQIM2y8%2BcgB%2BSu85fJxdAtUwJstNEDbxG%2BHLKkDmgBX%2Ft0W56bfbBEn8jC9tk7iaPpmzKE9uFZ5tQzEp7kT9dgHC4BvwOqB%2B3tAHsfuyPfCQ9Ph4K4N1zdQLXcE8BD%2BY3E29SMEI2KtPBZy%2FqdQuupDCNuv%2FSBjqkAbWsq%2BDRsgHDSmHlhWlt9fJ2zjSg1UP2Dam7ZMJ7m%2FrnyjFz7dj24Vi6BWv7Pue2IPLnKjUPfTNqgtTziyF12AMCaQeAVItQDzLyG1Azxg1pqZFRcLXC0Ubc9IErgnc3%2F1SrM7NC0QP%2FbbWTee5j6%2FYgP6%2FG3rY2tFI0Wh3bA4JyR10%2FUnGMbx1far1eOUII2%2FOjT2Y6D2I7evd0s4Hf8Gp%2Bqevl&X-Amz-Signature=9f8b5bfce7e8e553dbb78c2ddcfa044667c517f3af5d2e38a13b05a41874cf6f&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

我们刚才已经把这个 API 这块封装好了，那接下来我们应该怎么去做呢？有的人说，老师，那接下来是不是就要对康门进行一个编写了？不一定说从 common 开始，暂且它肯定要有一个包，Com，点 e f x y，点rabbit，点common，先把这个包建立好，然后我们可能还有一个producer，对吧？先把这个 producer 这个包建立好， producer 好了。


那具体我们编码到底是选择 common 还是producer？那一般来讲，如果说你之前封装过或者以前写过，那你现在肯定知道哈公共出来的一些东西都有哪些内容，那你完完全全可以直接从 common 入手开始写。在这里我其实是在教小伙伴们一个这个封装基础组件的思路，那在这个时候很明显你只能定义出API，然后照着 API 去写你的代码，那你肯定要针对于主逻辑，也就是说我们生产端的这个整个封装开始入手，所以说你现在只能去写producer，在你写 producer 过程之中有一些公共的部分，你再把它抽出来，所以说我们应该先去从 producer 入手。


在这里提前说好。那除 producer 入手的话，那我们来看一看对应的这个依赖，这个依赖首先我们要加一些对应的dependency，刚才我说了，那我们的什么呢？康稳肯定是要被依赖到我们的 producer 里，所以说 common 它的一个包肯定要引进来，那在这里 group 和跟这个 artifact ID 是这样，我们都得需要在这里我把它复制一下 artifact ID 就是我们的这个Common，然后它的 version 肯定是零点一 snapshot 这个版本。


接下来我们已经把 common 类引入到了我们的 call producer 类包里面了，那接下来我们需要有哪些？首先来看一看这个副炮里边，你看他 parent 是 spring boot starter，然后这里边我这只是引了一些这个test，其实这个里边我应该多加一个，哈，在这里多加一个，比如说我把这个 starter 也引进来，可以吗？

[image](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/1e378357-f3b5-4743-9e5f-c0c74b928fba/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZM6X4Z4W%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T225300Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDeLKI%2FVedfMD5dKmjffvrlzwWilzRrFzBcqwUsus5IOQIhAKN8u0RaSx8oV11%2F8IBECGgEQ2S%2F1X67SEM3vBmPJDWIKogECMb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgwPp8j2lau7KPK8Hk0q3ANMh%2BgfgCmphAMycgvKm5aVznLYQLvb9iUrXZcj4Pw1XYHb%2FjPeIzjnfNvXWNKRBhnd%2BsBh7lWSfZzKzzJhUDLq4IehEm2px6qRFxHUtksEpE7VQl42XuxA2aX4PuukNnXgc9w8TjLpKTI4EpO6yRFiBTeOOi4RJ6KrB2T6%2FmPOfwBexWGnP64JFf1RONggtWEw82465k6l9X5qZsZO5HOkZjH4wufl1uDzrbqVat4aOSXB1yCfOf9mySTLi8yaVRyEF4ci7SHqiszpTVaatoZHLgbwhyADQPQvAMIJK6DnxWmjmpkghWzv7aSHOxCbVdL8lb%2F509u4uPRdhrj0NuRfspl0kc%2BND4k8Xu09jq0smSZKrQSci3ugKVp2a6w8ERwq16X11rsttiNp8gdX6VqC5mthLNK7xqDA54ZfaQLcXZc9AiV8B%2BAVwgYjkZh%2FPcQuU%2FDZ9Fc%2F3owduXaBGgNu%2FBawK2tPtP0KvckhQIM2y8%2BcgB%2BSu85fJxdAtUwJstNEDbxG%2BHLKkDmgBX%2Ft0W56bfbBEn8jC9tk7iaPpmzKE9uFZ5tQzEp7kT9dgHC4BvwOqB%2B3tAHsfuyPfCQ9Ph4K4N1zdQLXcE8BD%2BY3E29SMEI2KtPBZy%2FqdQuupDCNuv%2FSBjqkAbWsq%2BDRsgHDSmHlhWlt9fJ2zjSg1UP2Dam7ZMJ7m%2FrnyjFz7dj24Vi6BWv7Pue2IPLnKjUPfTNqgtTziyF12AMCaQeAVItQDzLyG1Azxg1pqZFRcLXC0Ubc9IErgnc3%2F1SrM7NC0QP%2FbbWTee5j6%2FYgP6%2FG3rY2tFI0Wh3bA4JyR10%2FUnGMbx1far1eOUII2%2FOjT2Y6D2I7evd0s4Hf8Gp%2Bqevl&X-Amz-Signature=c44794327e922dc9d1e977009c958a7bd5595f84f16d11b875e8010783fe865a&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

对， start 引进来，那就是说这个也会有 start 相关的一些内容，这个没问题， start 引进来了之后，那我们 producer 其实就不需要引 start 了，要不然你还得去再引一下starter，这样的话我们引这个 full palm，这个 starter 被我们引进来了，它天然就是一个 spring boot 的一个工程。


然后接下来还需要哪些？那现在你肯定是要做对应的这个 Rabbit MQ，所以说 rap MQ 这个包里边有一些内容，我们是不是也得需要？那关于 red MQ，其实那 common 是不是我们应该把对应的一些类放到 common 里，这样最好？所以说现在我们点到 common 里边，我们看一看对应着 common 我们应该加哪些depend？既然是公共的，首先 common 它肯定要有一个dependency，是谁？你的 API 抽象出来的这一些接口是不是应该在 common 里去体现一下？我们直接把这 3 个东西 copy 过来，然后这个是 API 引进来，也就是说我们现在是 API 被 common 引进来，因为这个 API 很单纯，它就是对外提供的一些 API 接口，然后那它不应该依赖common，而是什么康文应该里边嵌入这个API。注意这个逻辑，所以说有了它之后，我们想一想还有哪些比较关键的，比如说你的 rap MQ 奥格点 spring framework，然后点boot，然后在这里我们直接使用它的 AMQP 可以了。


spring 杠 boot 杠 starter 一般都是叫什么？什么 start a m q p 这个包已经有了，然后还有哪些？我们暂且认为他们包里面就有两个，一个是API，还有一个是MQP，那这样的话我们 producer 是不是 producer 把 common 引进来了？那也就是说它肯定具有 API 和 MQP 包了，对不对？所以说接下来我们就可以放心的去写代码了，我们就可以发信息代码了。好了，然后暂时我们什么也不需要，把所有的这个号码文件关掉，注意一下这个依赖关系。


OK，那我们看一看这个 producer 我们该怎么去写代码？那首先从最开始的角度去思考，它是一个这个producer，它这个 API 可能要引入到第三方的工程里边，它可以当成一个SDK，只不过 API 这块单独抽象出来了，就是说我们可以用这个 API 去直接调 API 就好了，我们具体下面就是 API 的实现了，那具体这个内容，这个 producer 肯定是要引到我们的这个具体第三方工程里的。


所以说在这里我们要做的事情，同学们对于这个 spring boot 它的这个自动装配应该有所了解，那我们下面用一个folder，对吧？我们就是 m e t a 杠 info 这个包，这个文件夹下我们可以创建一个类了，是这个类就是我们的 spring 第二 factory 4I yes factories 这个 screen 点factories，一般来讲我们去做自动装配的时候对不对？它可能有一个这个叫做 auto configuration，这个我相信大家对于此培训比较熟悉的，应该对 o to configure 应该是非常熟悉了，就是自动装配这个事情 o to configure，那我们可以去直接点 o to configure，然后第二 enable auto consideration，应该是这样的，然后换行，对吧？好了，他能做什么事情？他能做的事情就是它自动帮我们去装配一个类。


装配的这个类我们自己想一想，它应该是具有一个什么呀？具有一个自动装配的属性的。那我们来看一看这个应该怎么去做？比如说我现在搞一个package，除了 user 点 auto configure 可以，然后这个类，下面我们搞一个 auto configuration，什么什么什么，对吧？好，我们来一个类，咱们叫。


A rabbit producer. 对不对？然后凹凸。 Configuration. 好了，把这个类的全名就是包名，加上类名放到这个配置文件里边，点 Rabbit producer auto configuration，这就可以了，注意这是一个斜杠，千万不要写两个斜杠，那这样的话它就会帮我去自动装配这个类，就是 Rabbit producer auto configuration。


好，这个类，那我们来首先要自动装配的一个前提，就是说它必须得是一个configuration，这个注解必须要有configuration，这个注解是必须要有的，然后至于其他的就无所谓了，我们先这样去写，那这样的话就只要是 spring 1 加载加载到我们的这个 call producer，那它就会自动帮我们去读取这个 spring 点 factories 这个文件，然后去把我们这里边定义的所有的类然后都去帮我们去自动装配。他就会读这个凹凸configuration，找到这个凹凸 


configuration 了，那它里边是不是就 OK 了？小伙伴们应该能理解吧？那这样的话我们应该怎么去做呢？其实我们在这里边就可以写我们具体的一些代码了，那我们暂时呢，可能不知道我要招聘哪些内容，现在怎么办？我们先不管，我们先打个注释，这就是自动装配的一个类，做自动装配好了，把这个先关掉。


有了这个自动装配以后，那接下来我们首先要做什么事情？刚才我说了，我们有一个我们的这个API，这个包里边我定义了一个producer，还定义了一个什么呀？一个 message list，这可能是 consumer 需要做的事情，那我先暂且不管，我们就先管 producer 要做的事情。


producer 定义了一个接口，那肯定要对这个 3 个方法进行实现，由于这个 API 包它内嵌到 common 里了，而 common 又内嵌到这个 call producer 里，这个没问题的，我们来回顾一下，我的 producer 引了这个 common 包，而 common 包里边又引了这个 API 包，所以说我想去找。


我在 producer 里边，我这个泡 producer 里边我想找 API 的类，那是肯定能找到的，对吧？所以说我们就来做一个实现，比如说我现在要对这`个` message producer，也就是说 API 包里边的这 3 个接口写一个实现类。好，那很简单，我们给它起一个名字，很简单，在这里我们叫做producer。点什么呢？点broker，broker，好，有了这个 broker 之后，我们来新建一个类，咱们叫做什么呀？就叫做 producer client，对吧？那一般的 producer client 它只需要实现这个接口就可以了，就是我们刚才给小伙伴们看到的这个 message producer，这是我们自己的资产，他要实现这 3 个方法可以了，他只要实现这 3 个方法，那我们是不是就可以调用这个实例对象，然后调散的方法，然后就开始发消息？一般来讲是这样的，然后接下来我们看一看怎么去实现这 3 个方法，那实现这 3 个方法其实就会用到我们后面的内容了，那其实我们现在已经真正把一个最基础的这么一个架子搭建起来了。


后面的事情那可能就是我们针对于不同的各种各样的消息进行一个处理了，比如说如何去发批量消息，如何去发一个带有回调的消息，如何去发正常的这种 message 消息，那这样的话就是我们真正的去封装 API 的事情。这节课呢，咱们先做一个小停顿，然后下节课开始我们就真正的去分析一下我们的 COP producer 这个核心应该怎么去实现了。OK，那么这节课我们就先讲到这，谢谢小伙伴们。





```java
package com.bfxy.rabbit.producer.broker;

import com.bfxy.rabbit.api.Message;
import com.bfxy.rabbit.api.MessageProducer;
import com.bfxy.rabbit.api.SendCallback;
import com.bfxy.rabbit.api.exception.MessageRuntimeException;

import java.util.List;

/**
 * <h1></h1>
 */
public class ProducerClient implements MessageProducer {
    @Override
    public void send(Message message, SendCallback sendCallback) throws RuntimeException {

    }

    @Override
    public void send(Message message) throws MessageRuntimeException {

    }

    @Override
    public void send(List<Message> messages) throws MessageRuntimeException {

    }
}
```

```java
resource/META-INF/spring.factories

# Auto Configure  自动装配
org.springframework.boot.autoconfigure.EnableAutoConfiguration=\
com.bfxy.rabbit.producer.autoconfigure.RabbitProducerAutoconfiguration


```

```java
package com.bfxy.rabbit.producer.autoconfigure;

import org.springframework.context.annotation.Configuration;

/**
 * <h1>自动装配</h1>
 */
@Configuration
public class RabbitProducerAutoconfiguration {
}
```

