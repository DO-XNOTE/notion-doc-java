---
title: 2-19 【Demo】消息驱动中的降级和接口升版
---

# 2-19 【Demo】消息驱动中的降级和接口升版

[image](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/7061c558-6252-4d92-b39f-0d4cb515c38f/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663GXRW277%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T225822Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIDYnQt%2BI2ZiBubGvyY3Yc71vX6BAWGs%2BN8kSC1ufQ%2FNHAiBoyjpqrrQhoL4iukcnv%2B%2BS5Ro7AFSV%2FSddmQOat1H2NSqIBAjG%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMlZqbso2lJkJGHwQFKtwD9uledLI0V31PIAXdRMfBkscOXbq9ZuwIwA%2FgaMehT20q2f807K%2FknW0yYbbW5bI1HwQvutSlJjK9XS5QPaEKxe%2FQjSGQwYqargY9W9AvNFVMF5bFwWuNI0%2BQ6ClpDyKVHT%2BnbI24641ZBtB26oHTWoyrMtm%2FrDam32W4lh628enZ%2FlUEn%2FVBKCIWIbvIqMEaN11voPy%2F%2F9nRKSZ3vC9rqLXaw3dJfPZ45j3uCDBVRUP07tuKqUqr%2FVVnn%2B%2B%2B6GU%2FJEQqxKjiziomQYtYa7MI2q6sKCpzFh1XZkVMXV5rVODhwZeFZX3N9ZTTRHMkSxr1l%2FLnYafF4EQmRsEE9TBkoGtXuybPDAMcf6mUkm8sbd6NxvuMWPAiFTAhFj9WVGKnPoMTTnpoQWbJpcO%2BY6A3TWNZiMK4lCRaTvg4wKGvgyi0hINkkqMXt%2BBAPhdPPYoUWYoGPJXsD8pgH%2FYGL4MejwMzuKdNPSaX8IeP0IH0y%2B9%2F7ZLZXpg32YOXRaML4Xq6kEVKnGGcSPBtwaBwCcpxxam86tkwc66NWHEvGUdA856T%2BZyu1g6u1Wyssx3RBv0%2BKFi4gCSbKtelz%2BGEOKAW0OR%2F2c%2BdxskIJ9bqdJJt2%2B7DV8Ox6dnvHNrFrQMwk7j%2F0gY6pgH6p5lMwfTfFyHBBBdAqfBhyFedrWbxR8MlBqXrcKlHYxkNSvWRrmHXajGqRs2r2yo6IBQWtgTgDYd2cL8VfpxdAuZTVXtI0PD5PHOeWCwTz0k7t3pPn6%2B6wwy%2BrU916jGFcFvI1F1vRDNsDc2dVOxnyyL6JYGFW%2FDeMrxXBr3RbqwqYlf3ntNg8q5pTr1HjYCd2e1qljYwLsP0RouGCm2j%2BWTbuXuA&X-Amz-Signature=f09f2de9de36b58cc065456a02613f54cf29f139e34f526b350f326b3b1f356d&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

[image](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/dbedfe6d-83e9-4ec4-92d6-c37f37efa031/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663GXRW277%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T225822Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIDYnQt%2BI2ZiBubGvyY3Yc71vX6BAWGs%2BN8kSC1ufQ%2FNHAiBoyjpqrrQhoL4iukcnv%2B%2BS5Ro7AFSV%2FSddmQOat1H2NSqIBAjG%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMlZqbso2lJkJGHwQFKtwD9uledLI0V31PIAXdRMfBkscOXbq9ZuwIwA%2FgaMehT20q2f807K%2FknW0yYbbW5bI1HwQvutSlJjK9XS5QPaEKxe%2FQjSGQwYqargY9W9AvNFVMF5bFwWuNI0%2BQ6ClpDyKVHT%2BnbI24641ZBtB26oHTWoyrMtm%2FrDam32W4lh628enZ%2FlUEn%2FVBKCIWIbvIqMEaN11voPy%2F%2F9nRKSZ3vC9rqLXaw3dJfPZ45j3uCDBVRUP07tuKqUqr%2FVVnn%2B%2B%2B6GU%2FJEQqxKjiziomQYtYa7MI2q6sKCpzFh1XZkVMXV5rVODhwZeFZX3N9ZTTRHMkSxr1l%2FLnYafF4EQmRsEE9TBkoGtXuybPDAMcf6mUkm8sbd6NxvuMWPAiFTAhFj9WVGKnPoMTTnpoQWbJpcO%2BY6A3TWNZiMK4lCRaTvg4wKGvgyi0hINkkqMXt%2BBAPhdPPYoUWYoGPJXsD8pgH%2FYGL4MejwMzuKdNPSaX8IeP0IH0y%2B9%2F7ZLZXpg32YOXRaML4Xq6kEVKnGGcSPBtwaBwCcpxxam86tkwc66NWHEvGUdA856T%2BZyu1g6u1Wyssx3RBv0%2BKFi4gCSbKtelz%2BGEOKAW0OR%2F2c%2BdxskIJ9bqdJJt2%2B7DV8Ox6dnvHNrFrQMwk7j%2F0gY6pgH6p5lMwfTfFyHBBBdAqfBhyFedrWbxR8MlBqXrcKlHYxkNSvWRrmHXajGqRs2r2yo6IBQWtgTgDYd2cL8VfpxdAuZTVXtI0PD5PHOeWCwTz0k7t3pPn6%2B6wwy%2BrU916jGFcFvI1F1vRDNsDc2dVOxnyyL6JYGFW%2FDeMrxXBr3RbqwqYlf3ntNg8q5pTr1HjYCd2e1qljYwLsP0RouGCm2j%2BWTbuXuA&X-Amz-Signature=0a65e25f13624e20b1a528dd198848ffd8184581d187d3b08c11b03157f8527f&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

[image](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/f49f4d9d-93ca-466f-a00d-4a4aabb186c8/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663GXRW277%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T225822Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIDYnQt%2BI2ZiBubGvyY3Yc71vX6BAWGs%2BN8kSC1ufQ%2FNHAiBoyjpqrrQhoL4iukcnv%2B%2BS5Ro7AFSV%2FSddmQOat1H2NSqIBAjG%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMlZqbso2lJkJGHwQFKtwD9uledLI0V31PIAXdRMfBkscOXbq9ZuwIwA%2FgaMehT20q2f807K%2FknW0yYbbW5bI1HwQvutSlJjK9XS5QPaEKxe%2FQjSGQwYqargY9W9AvNFVMF5bFwWuNI0%2BQ6ClpDyKVHT%2BnbI24641ZBtB26oHTWoyrMtm%2FrDam32W4lh628enZ%2FlUEn%2FVBKCIWIbvIqMEaN11voPy%2F%2F9nRKSZ3vC9rqLXaw3dJfPZ45j3uCDBVRUP07tuKqUqr%2FVVnn%2B%2B%2B6GU%2FJEQqxKjiziomQYtYa7MI2q6sKCpzFh1XZkVMXV5rVODhwZeFZX3N9ZTTRHMkSxr1l%2FLnYafF4EQmRsEE9TBkoGtXuybPDAMcf6mUkm8sbd6NxvuMWPAiFTAhFj9WVGKnPoMTTnpoQWbJpcO%2BY6A3TWNZiMK4lCRaTvg4wKGvgyi0hINkkqMXt%2BBAPhdPPYoUWYoGPJXsD8pgH%2FYGL4MejwMzuKdNPSaX8IeP0IH0y%2B9%2F7ZLZXpg32YOXRaML4Xq6kEVKnGGcSPBtwaBwCcpxxam86tkwc66NWHEvGUdA856T%2BZyu1g6u1Wyssx3RBv0%2BKFi4gCSbKtelz%2BGEOKAW0OR%2F2c%2BdxskIJ9bqdJJt2%2B7DV8Ox6dnvHNrFrQMwk7j%2F0gY6pgH6p5lMwfTfFyHBBBdAqfBhyFedrWbxR8MlBqXrcKlHYxkNSvWRrmHXajGqRs2r2yo6IBQWtgTgDYd2cL8VfpxdAuZTVXtI0PD5PHOeWCwTz0k7t3pPn6%2B6wwy%2BrU916jGFcFvI1F1vRDNsDc2dVOxnyyL6JYGFW%2FDeMrxXBr3RbqwqYlf3ntNg8q5pTr1HjYCd2e1qljYwLsP0RouGCm2j%2BWTbuXuA&X-Amz-Signature=827b6d7fe5b024f8197cae93f5001ba5136b86dadbad73c58c9d00fbf1221c03&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

慕课网的各位同学们，大家好，这一小节是咱整个 stream 章节中有关于异常处理的最后一个知识点了，我来带大家一起自定义一个异常处理的逻辑。咱先来一起看一下本节的主要内容总共分为两个部分。第一部分我们借助 spring integration 组件来实现 fall back 逻辑。大家没看错，这个 fall back 就是指降级逻辑。只不过咱这里的降级并不像 high streaks 一样运用在接口调用上，这里咱是应用在了消息的消费者上面。

[image](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/47499c1e-35ef-4fd4-a061-9cea6409503a/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663GXRW277%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T225822Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIDYnQt%2BI2ZiBubGvyY3Yc71vX6BAWGs%2BN8kSC1ufQ%2FNHAiBoyjpqrrQhoL4iukcnv%2B%2BS5Ro7AFSV%2FSddmQOat1H2NSqIBAjG%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMlZqbso2lJkJGHwQFKtwD9uledLI0V31PIAXdRMfBkscOXbq9ZuwIwA%2FgaMehT20q2f807K%2FknW0yYbbW5bI1HwQvutSlJjK9XS5QPaEKxe%2FQjSGQwYqargY9W9AvNFVMF5bFwWuNI0%2BQ6ClpDyKVHT%2BnbI24641ZBtB26oHTWoyrMtm%2FrDam32W4lh628enZ%2FlUEn%2FVBKCIWIbvIqMEaN11voPy%2F%2F9nRKSZ3vC9rqLXaw3dJfPZ45j3uCDBVRUP07tuKqUqr%2FVVnn%2B%2B%2B6GU%2FJEQqxKjiziomQYtYa7MI2q6sKCpzFh1XZkVMXV5rVODhwZeFZX3N9ZTTRHMkSxr1l%2FLnYafF4EQmRsEE9TBkoGtXuybPDAMcf6mUkm8sbd6NxvuMWPAiFTAhFj9WVGKnPoMTTnpoQWbJpcO%2BY6A3TWNZiMK4lCRaTvg4wKGvgyi0hINkkqMXt%2BBAPhdPPYoUWYoGPJXsD8pgH%2FYGL4MejwMzuKdNPSaX8IeP0IH0y%2B9%2F7ZLZXpg32YOXRaML4Xq6kEVKnGGcSPBtwaBwCcpxxam86tkwc66NWHEvGUdA856T%2BZyu1g6u1Wyssx3RBv0%2BKFi4gCSbKtelz%2BGEOKAW0OR%2F2c%2BdxskIJ9bqdJJt2%2B7DV8Ox6dnvHNrFrQMwk7j%2F0gY6pgH6p5lMwfTfFyHBBBdAqfBhyFedrWbxR8MlBqXrcKlHYxkNSvWRrmHXajGqRs2r2yo6IBQWtgTgDYd2cL8VfpxdAuZTVXtI0PD5PHOeWCwTz0k7t3pPn6%2B6wwy%2BrU916jGFcFvI1F1vRDNsDc2dVOxnyyL6JYGFW%2FDeMrxXBr3RbqwqYlf3ntNg8q5pTr1HjYCd2e1qljYwLsP0RouGCm2j%2BWTbuXuA&X-Amz-Signature=aecc3c555afb815c5b3bb8f33dadd8081657e6561254782b32f317bcafd6d0f1&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

那接下来的一个部分，我们来看一下 consumer 升级的玩法。我们平时在开发接口的时候，尤其像电商领域这种变化非常非常频繁的场景。那由于业务玩法的变化，接口需要升级，通常我们可以在原接口的基础上提供向前向后兼容，或者可以开发一个新的接口。咱在大型应用的代码里面经常会看到一个接口，后面跟着一个版本号 v1v2 v3 对吧，那就是不断升版的结果。那对于消息驱动的业务逻辑，也有这样一个需求，咱这里就跟大家介绍一个最普通最通用的玩法，咱来了解一下如何让生产者和消费者之间共同协作。根据上游应用的指示，在消费者当中采用不同的业务处理方案。


OK 同学们，最后一节，大家打起精神，我们开赴 intelligi 编程使我快乐。 996 是我的福报，咱在 stream 章节最后一次享受福报的机会来啦。好，这里重新创建一个新的 topic 把它叫做 fall back topic 又到了那个熟悉的剧情啦。对不对想要改 input output 的名字，把它改为 fallback consumer 和 fallback producer 改完以后，转站到 controller 里面，我们在 controller 上面先把它们引入进来。我们在这一节当中，不光要讲 fallback 还要讲如何对 consumer 进行升版。那这里也牵扯到 producer 也就是 controller 中的改动。所以我们把这两个 demo 就混合在一块儿来讲了。


这里先把刚才创建的 topic 给它引入进来，它的变量名称叫 fallback topic producerok 把它复制一下走到下面。然后在这个死信队列测试这里也把它 copy 一下，剧情还是那么的相似，咱从上到下改代码。首先这里注释是 fallback 加升版版本的版，那它的 UR L 我们把它改成叫 fallback 方法名也是 send message to fall backok 这里方法参数我要改动一个地方。我们这里指定一个新的 request param 叫什么呢？给它起名叫 version 这个 version 待会儿怎么用？咱马上就揭晓了它的值，是一个 string 类型的。 Version. OK 接下来咱在发送方法的地方把这个 producer 替换成咱刚刚创建的 fallback producer 然后还有一个改动这里。


在 send message 的时候，我们要对这个 message 动一点，手脚怎么动？咱假设现在是一个电商场景，我们要调用一个接口，下单接口叫 place order 那不同的手机 App 可能调用的接口的版本是不同的。比如说我的老版本，它调用的接口可能是叫 place order V one 也就是初始版本。那升级过后的 App 有可能是调用 please order way to 那在调用的时候，我可以决定去走哪个调用逻辑对不对？那把这种接口调用的方案类比到我们的消息驱动场景中来，万变不离其宗。


我们在调用下游方法，也就是说我们在生成这条 message 的时候，一定要指定好接下来要调用哪个版本。这里有两个方案，我们可以把这个 message 发送到不同的 Q 比如 Q one 你要是新的业务逻辑，你可能把它发到 Q two 这是一种方法。还有一种更简单的方法，它不需要你上游代码做过多的改动，只用怎么样只用传递一个信息到下游就好了。
什么信息我们这里来看，我希望对代码的冲击越小越好，也就是说它的 payload 尽量保持不变。那么这个参数我们把它放到哪里呢？放到 header 当中。 OK 那给 header 加一个新的变量叫 version 那这个 version 的内容就是咱从前端页面传入过来的。好，我们给它加一个默认的值。好了，default value 等于1.0。 OK 那我们把注释给清空掉。


好。 controller 定义好了以后，我们接下来到 consumer 里面定义一番 consumer 这里也从上到下定义 topic 这里我们把刚才创建的 fallback topic 给它加进来，加好以后往下走，往下滚到最下面把死信队列这里 copy 一下，另起一行。然后从注释从上到下开始改起。这里注释是叫 fallback 加升升级版本，它的 streamlistener 的 topic 这里要记得把它变成 fallback 那进到 fallback 降级的都不是什么好家伙，咱给它改名叫 goodbye bad guy 好嘞，那接下来在接收消息的这里，我们有一点要改动了，怎么改？我们添加一个新的注解叫做 header 好，大家看 header 是来自于哪，这里有两个 header 我们把它添加。


第一个 header 是来自于 messaging 的这个 header 接收什么参数呢？它就接收咱上游传下来的 version 然后类型依然是 string 类型，咱接收完 header 以后，咱就要把 header 应用在下面的逻辑当中了。那首先给它打一行 log 这个叫 fall back 一句问候，而又 K 后面 OK 不 OK 就看你的 version 了，我们这样来定义一段稀奇古怪的逻辑。如果你的 version 是 1.0 这样的话怎么办？我就把你放过去。意思就是说你没有出错，可以安然无恙的通行。那假设你不是1.0，你是其他的版本，你是2.0，我们这里再给它加一个 2.0 的判断逻辑。


其实同学们如果这里有工具类，咱可以引入 Google 的工具类或者阿帕奇的工具类，可以对比较字符串的时候使用 string utils 比较。那咱这里没有引入 dependency 就直接采用这种方式来简单化了。如果你是 2.0 怎么办呢？那就给你添加一行 log on supported version 就说你目前这个版本还不支持，2.0的版本还没有开发完，不支持。那剩下的版本怎么样？剩下的版本发善心了，也给你放行过去了。但是在放行之前，我把你的版本号给它打印出来， version 等于这里给它打印。


Ok. 那通过这种方式，我们就可以针对不同的版本走不同的业务逻辑。其实在咱的生产环境里面这种场景也非常的常见。因为在互联网公司，大家知道开发模式叫什么叫操快猛，就是怎么快怎么来，你只要让这个应用可以用就可以。所以我们在选择方案的时候，就选那种在最短时间内可以迅速落地的方案。那与其在新创建一对消费者生产者一个新的 topic 那咱现在选择的这种方案通过 version 来区别应用逻辑是不是最简单高效省时省力的？ OK 那咱的版本升级讲完了，那 fall back 还没有讲对不对？先别急，我们先去更改一下配置文件。好，走到 application.progress 文件里面收集小说版，咱把上面的这行配置给它 copy 过来，死信队列的配置从上到下开始改了，这个注释是指降级流程 fall back 配置。那好，这里我们把它的 consumer 和 producer 都改成 fallback consumer fallback producer 重试次数这里保持不变还是两次。然后给它添加一个 group 咱的 group 的名称就叫 fallback group 好了。


OK 那配置文件也改好了，接下来咱可以去修改 fallback 逻辑了，我们走到 consumer 里看一看 fallback 逻辑怎么改，跟大家讲最简单最经济高效省事的方法。以后大家在互联网公司被这个 996 倒排气逼得喘不过气的时候，还就用这种方法就对了。说实在的，在阿里还真的从来没做过一个让开发估算工期的项目，都是业务部门说一个日期，我某年某月某日之前就要剩下的事儿他可不管了，只要你把这个功能做出来就行。所以大家都被这种倒排气逼的是神烦。那帮产品 PD 妹子真的是太要了。


我们给这个方法起名就叫 fallback okay 那它接收什么参数呢？接收一个 message 这个 message 是什么类型呢？我们把它引入进来，它是 stream 下面的这个 message 好，加入进来以后给它加一个问号泛型，它就叫 message 好了，我们开始写里面的逻辑了，从这个 message 里面咱不光可以 get 到 payload 也可以拿到谁也可以拿到 headers 这就是咱需要的所有内容了。然后在这里我们业务逻辑就不多写了，只是为了跟大家展示一下 fallback 的流程。所以我们这里的 info 信息就是 info log fallback entered 进入了 fallback 流程。


那这两个方法怎么关联起来？接下来就要 call spring 的 integration 组件大显身手了，咱加入这样一个注解叫 service activatorok 那这个注解是 spring integration 下面的一个annotation ，大家应该在项目中也用过非常常见的一个。那这里什么呢？指定一个 input channel 它这里是一个信道的名称。信道名称怎么填？同学们，我们到配置文件里面看一下，咱们看一下当前我们项目启动的这个信道名称是什么格式。好，我们这里信道名称应该用谁呢？咱不是把它重定向到了 fall back topic 了吗？那所以我们的 input channel 应该起名的流程是这样的，首先是 fall back 杠 topic 后面你如果配了 group 的话，这里要把你的 group 给添加进去，咱是 fallback group 那既然都是降级逻辑了，它的 input channel 总归有一些特殊的标记，就叫 Iris 好嘞，咱把这一行复制过来，粘贴到刚才的 consumer 里面。好，这里的降级逻辑就已经搞定了。当咱的业务请求抛出异常并且重试次数达到上限了以后，那么它就会被转到 fall back 逻辑里面。 OK 我们现在把方法给它启动起来，验证一下结果，打开 stream application 直接把它跑起来，稍等半炷香的时间。


好，项目已经启动好了，接下来咱转战 postman 前面讲到，在 1.0 版本的时候，它的所有的业务逻辑都是正常返回的。那我们这里给它指定一个新的参数叫 version 1.0。 OK 把它发到哪个地址呢？发到 fallback 这个函数里面，我们点击发送了走。


你 OK 回头看一下后台的 log 同学们在这里已经看到了最后两行 log 说明这条方法已经被消费成功了，那咱把 log 清空掉，如果你不是 version 2.0 都不会踩到坑里的。咱不信试一下 version 3.0 传过去，依然被消费成功了。


那接下来咱要试一下 version 2.0 了，我们把 log 清空 2.0 可就要掉到沟里去了，我们添加成2.0，然后再发一个 sand 好，回到后面看一下。它第一次调用显示了 unsupported version 说明你第一次调用失败了，紧接着它发起了一次重试，然后又失败了。失败以后，这一行 log 就转入到了 fallback 里面。


OK 同学们，那这最后一个处理异常的招数你 get 到了吗？本节的课程内容到这里就结束了，我来跟大家稍微总结一下。在这个课程中我们学习了两个知识点。第一个是消息驱动业务流程中的升版，它和 App 接口的升版实际上概念上是一样的。这里通过在 header 里面加入一个 version 信息，使用了最简洁高效的申办手段，将当前的消息在 consumer 中采用不同的业务流程把它处理掉。


那第二个知识点就是咱的 fallback 流程了。我们这里在方法的最下面添加了一个 fallback 函数，这个 fallback 函数的关键是通过 spring integration 组件指定了一个输入的信道。那这个输入信道的命名格式就是你指定的消息队列名称，咱这里是 feedback topic 如果配置了group ，这里要把 group ID 也给添加进去，最后再加一个点 errors 好，那本节的内容到这里全部结束。在下一节当中，咱对这几种异常处理的策略进行一个简单的回顾和总结思考一下。在不同的业务场景中，我们如何选择合适的异常处理策略？ OK 同学们，那我们下节课程再见。




