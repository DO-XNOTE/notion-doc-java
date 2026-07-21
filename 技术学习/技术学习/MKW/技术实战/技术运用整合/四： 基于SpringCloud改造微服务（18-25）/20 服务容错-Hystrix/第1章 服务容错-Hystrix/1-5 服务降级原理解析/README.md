---
title: 1-5 服务降级原理解析
---

# 1-5 服务降级原理解析

[image](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/ee66119e-da72-48e6-803d-4d22c010269d/SCR-20240718-rzem.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466S2IXKWRP%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T225635Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDbIhM%2BWGRlD4RUvn4B7y7nVSYacJ%2Ffj9ZauM9kvd%2B4NwIhANU6fhNh10HFCclipiJsDYaPdxo512HmGFRX9ju%2Bl1szKogECMb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1Igwep3D%2Bd9HQqXtCBhkq3AOBOQQEXLZRB9ve8BSlOWu7NRFOcGN2QT8H7O%2F238asMaRveDWErJSiqisuEXKrsCzU3CNrj4kngBqhzcG3BMZfT8MOxuV7NHSEU3BQ2YBTGbCdSPwNxhVg8FEFiVS69aRjfy9%2FFU8B%2B6ei7osWX65p5WdEyFyWjAJ8TRSLd0deg7k3lkqdiNnH8uHs%2B5rc%2FohZeg2hzSOB0H7N71Fpdu38T31%2Fe9PnspAqPaYxEZFSFfUZ1%2FKmw5JSLp3E3r3b6yL%2BT9l5A0RNQAw7DfARX2XVqev1pY%2B3nQQ6ujriMWTbqFzC%2FzIkgIuZhkU3wRNrJ7EO3s9StF3UL85oWbqpN0CtW8VboXye3FcAgRPfNQFZyNGUkWPq41D90a%2FAIRNvtaZNxBb0FrvE98Vxhze6GIL3Kei0IYKfnlG019EOZgTF9XAMLeyhtfQhMfb0Kyfpe219D9hu6GKotgNmTW9nU0NSGvkUbWqW0CMukj9ioL5YoAUm9hfjs7iynCwrm%2B6KrJM2s9po%2F0bwyus8dOBGACrMp5ebGPbaEmJGsiadbkia1SWDv6haDylO7LnWW5WHpm%2F9FyzmyySE5mp7ipQiGq%2Bgi1HrXaVWigtghH4vEce59pZ79F99u9%2FxapB5wjCzuv%2FSBjqkAQ%2BZr%2Bi8SHMboZDcgbTHuVbmqugn%2BTID4CvdVisJH74sJPN0MMko8TTSzkVKWJeqFvvvq3Q1MK%2FRnx6lX5wByWifxRojVm5vpCc%2FIegEUKbFk2lRp29Fck7T5zsTZ3F3FR6yMeri8x06YVaMvYlBMnstel82A7x6tVP19zbKZU3wXedx0Qb3H8x%2F7%2FeqMaBGZSk%2BmMlnIbdwkkFz0jp87Nw8ESsf&X-Amz-Signature=70c114f5b70962f692cb862578ef7e992089ef82d846c828ba2748e75f909289&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

[image](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/e7a9685a-8676-4ac0-942f-8ae1217a2c86/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466S2IXKWRP%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T225635Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDbIhM%2BWGRlD4RUvn4B7y7nVSYacJ%2Ffj9ZauM9kvd%2B4NwIhANU6fhNh10HFCclipiJsDYaPdxo512HmGFRX9ju%2Bl1szKogECMb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1Igwep3D%2Bd9HQqXtCBhkq3AOBOQQEXLZRB9ve8BSlOWu7NRFOcGN2QT8H7O%2F238asMaRveDWErJSiqisuEXKrsCzU3CNrj4kngBqhzcG3BMZfT8MOxuV7NHSEU3BQ2YBTGbCdSPwNxhVg8FEFiVS69aRjfy9%2FFU8B%2B6ei7osWX65p5WdEyFyWjAJ8TRSLd0deg7k3lkqdiNnH8uHs%2B5rc%2FohZeg2hzSOB0H7N71Fpdu38T31%2Fe9PnspAqPaYxEZFSFfUZ1%2FKmw5JSLp3E3r3b6yL%2BT9l5A0RNQAw7DfARX2XVqev1pY%2B3nQQ6ujriMWTbqFzC%2FzIkgIuZhkU3wRNrJ7EO3s9StF3UL85oWbqpN0CtW8VboXye3FcAgRPfNQFZyNGUkWPq41D90a%2FAIRNvtaZNxBb0FrvE98Vxhze6GIL3Kei0IYKfnlG019EOZgTF9XAMLeyhtfQhMfb0Kyfpe219D9hu6GKotgNmTW9nU0NSGvkUbWqW0CMukj9ioL5YoAUm9hfjs7iynCwrm%2B6KrJM2s9po%2F0bwyus8dOBGACrMp5ebGPbaEmJGsiadbkia1SWDv6haDylO7LnWW5WHpm%2F9FyzmyySE5mp7ipQiGq%2Bgi1HrXaVWigtghH4vEce59pZ79F99u9%2FxapB5wjCzuv%2FSBjqkAQ%2BZr%2Bi8SHMboZDcgbTHuVbmqugn%2BTID4CvdVisJH74sJPN0MMko8TTSzkVKWJeqFvvvq3Q1MK%2FRnx6lX5wByWifxRojVm5vpCc%2FIegEUKbFk2lRp29Fck7T5zsTZ3F3FR6yMeri8x06YVaMvYlBMnstel82A7x6tVP19zbKZU3wXedx0Qb3H8x%2F7%2FeqMaBGZSk%2BmMlnIbdwkkFz0jp87Nw8ESsf&X-Amz-Signature=97e99207bcd3e9bbf85a0e25441fe4498dc1aa95b88f39136fb67997e6137688&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

**1-5    服务降级原理解析**
前面的小节里我们学习了  Hystrix  的核心功能，今天我们拿一个最常用的功能来展开，那就是“服务降级”。作为 SpringCloud 中的执法部门-六扇门，Hystrix 监管着服务的一举一动，不管是超时还是异常抛出，但凡有违法乱纪的现象发生，就会被强制放到 fallback 里进行改造。可是，每个应用都有一长串的服务，那全部都交给 Hystrix 这能管得过来吗？Hystrix 可不是所有服务都监督，毕竟六扇门人力有限，他们只盯梢一些关键人物，给每个关键人物指派一个锦衣卫，但凡有异常发生，立即动手。接下来，我们就来看看六扇门的锦衣卫是如何秉公执法的。
盯梢名单-@HystrixCommand  

现在流行苍蝇老虎一起打，可我们六扇门不在乎小苍蝇，只盯大老虎。对那些一旦发生异常，影响特别恶劣，但是还有补救措施的，我们就安排一个锦衣卫贴身监视。


```java
@HystrixCommand(fallbackMethod = "putInPrison")
public String bigTiger() {
		throw RuntimeException("Eat People");
}
```


上面就是我们的贴身锦衣卫@HystrixCommand 注解，直接管在大老虎（具体  Method方法）的头上，没有指派锦衣卫的方法就可以放飞自我了，Hystrix  不会管你的。@HystrixCommand 注解中指定了一个  fallbackMethod，这里就是大老虎进行改造的地方，也就是降级逻辑所在的方法名。注意，降级方法的方法签名（参数列表）要和原方法保持一致，也就是说，如果原方法声明了一个参数  String，那么降级方法也要声明同样的参数，Hystrix  会原封不动的把当前参数传递给降级方法。
当  Hystrix  和  Feign  共同使用的时候，还有一种配置方式，那就是在  FeignClient  注解中指定一个  class，在这个  class  里可以处理  Feign  接口中声明的所有方法的降级需求。

```java
@FeignClient(name = "feign-service-provider", fallback = Fallback.class)
public interface MyHelloService extends HelloService {

}
```

在稍后稍后小节中，我们将把上述两个方案同时应用到  demo  中。

**锦衣卫工作流程-异常捕捉**

如果同学直接去阅读  Hystrix  服务降级的源码，相信有很有效的直接劝退的作用。Hystrix的源码大量基于  RxJava，在实现上比较接近函数式语言的风格，运用了大量的异步回调函数和事件驱动，层层嵌套十分崩溃，这对有  JavaScript  或其他函数语言经验的同学会容易理解一些（我估计  Hystrix  研发团队一定有资深  JavaScript  背景的研发人员）。如果大家平时阅读源码的经验不多，想弄明白这里面的道道可以说非常的难。老师  2  年前完整阅读过  Hystrix  代码，今天回过头再看的时候，也仔细  debug  了好一会儿才把异常捕捉的底层实现摸清。老师在源码阅读环节也会带大家从头到尾  debug  一把，跳过繁文缛节，只看最核心的部分。尽管  Hystrix  是一个久经考验的开源项目，但坦白的说，我对  Hystrix的代码结构和可维护性保持谨慎悲观的态度。为了避免直接劝退，这里的流程图以业务流为主，不涉及具体类名和方法名。不过我鼓励同学们自己去研究一下代码，这样有不懂的地方，就可以带着问题去看代码讲解视频：

[image](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/a8ef487f-dfbe-4505-9f3e-a02c77a577dd/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466S2IXKWRP%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T225635Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDbIhM%2BWGRlD4RUvn4B7y7nVSYacJ%2Ffj9ZauM9kvd%2B4NwIhANU6fhNh10HFCclipiJsDYaPdxo512HmGFRX9ju%2Bl1szKogECMb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1Igwep3D%2Bd9HQqXtCBhkq3AOBOQQEXLZRB9ve8BSlOWu7NRFOcGN2QT8H7O%2F238asMaRveDWErJSiqisuEXKrsCzU3CNrj4kngBqhzcG3BMZfT8MOxuV7NHSEU3BQ2YBTGbCdSPwNxhVg8FEFiVS69aRjfy9%2FFU8B%2B6ei7osWX65p5WdEyFyWjAJ8TRSLd0deg7k3lkqdiNnH8uHs%2B5rc%2FohZeg2hzSOB0H7N71Fpdu38T31%2Fe9PnspAqPaYxEZFSFfUZ1%2FKmw5JSLp3E3r3b6yL%2BT9l5A0RNQAw7DfARX2XVqev1pY%2B3nQQ6ujriMWTbqFzC%2FzIkgIuZhkU3wRNrJ7EO3s9StF3UL85oWbqpN0CtW8VboXye3FcAgRPfNQFZyNGUkWPq41D90a%2FAIRNvtaZNxBb0FrvE98Vxhze6GIL3Kei0IYKfnlG019EOZgTF9XAMLeyhtfQhMfb0Kyfpe219D9hu6GKotgNmTW9nU0NSGvkUbWqW0CMukj9ioL5YoAUm9hfjs7iynCwrm%2B6KrJM2s9po%2F0bwyus8dOBGACrMp5ebGPbaEmJGsiadbkia1SWDv6haDylO7LnWW5WHpm%2F9FyzmyySE5mp7ipQiGq%2Bgi1HrXaVWigtghH4vEce59pZ79F99u9%2FxapB5wjCzuv%2FSBjqkAQ%2BZr%2Bi8SHMboZDcgbTHuVbmqugn%2BTID4CvdVisJH74sJPN0MMko8TTSzkVKWJeqFvvvq3Q1MK%2FRnx6lX5wByWifxRojVm5vpCc%2FIegEUKbFk2lRp29Fck7T5zsTZ3F3FR6yMeri8x06YVaMvYlBMnstel82A7x6tVP19zbKZU3wXedx0Qb3H8x%2F7%2FeqMaBGZSk%2BmMlnIbdwkkFz0jp87Nw8ESsf&X-Amz-Signature=ec864559fab9e4915072a5b86e9d17b379bbada773afeac60d6355d8bf68ec89&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

@HystrixCommand: 安插在方法上的锦衣卫，标识此方法由  Hystrix  监管

AspectJ：运用  Spring  的切面能力，给带有@HystrixCommand 注解的方法配置了切面点，在方法调用的时候，将首先执行切面逻辑。大家可以借这个机会，顺带复习一下  Spring 的  AOP  切面编程（最好能够通过一个简单的小任务加深理解，比如自己定义一个注解，并且给这个注解配置切面完成一个简单逻辑，比如：将带有自定义注解的方法的执行时间打印到 log 中）

Request Cache：（下一节会讲到  RequestCache 策略）如果处于开启状态，则尝试用  CacheKey  从本地缓存中获取数据，也就不用发起方法调用了如果处于关闭状态，就继续往下走到最烧脑的部分，Observer


注册Observer：Observer 是观察者模式（在 RxJava 中又叫 Observable），但这里只是一个幌子，这个 Observer 背后运用 RxJava 注册了一堆异步回调函数，当方法正常执行、异常抛出、结束或其他状态的时候，将会触发对应的回调函数进行处理，而且回调函数里面还会嵌套回调函数。（Hystrix 开发团队是不是有个很怕失业的程序员？写这么复杂是要别人没法接手吗？）


发起调用：在发起调用之前，将会检查熔断状态，如果断路器当前处于开启的状态，那么将直接走向 fallback 流程。如果断路器处于关闭，则发起真正的调用

异常，又见异常：前面你来我往这么久，就是等方法调用抛异常。异常触发了步骤 4 中注册的回调函数，然后直接转给了降级方法


小结
这一节带大家了解了  Hystrix  的降级业务流程，下一节我们就来点轻松的话题，看看这帮六扇门的锦衣卫们，对这些进了  fallback  的家伙都有什么严刑逼供（降级）手段。
学习Tips：

我鼓励同学们自己深入研究  Hystrix  代码，相比前面几个组件来说  Hystrix  的代码阅读难度有大幅提升。有人说学习应该先易后难，老师自己比较喜欢先难后易，这个感觉就像学钢琴，如果直接从  10  级谱子开始弹，虽然初期非常艰难，但一旦学会之后，前面9级8级这些谱子就不在话下了。当然了，好的学习方法首先得要适合自己，不管从难到易还是从易到难，适合自己就是最好的。在学习过程中，解决越困难的问题，你就会积累越多的自信心，不畏难且迎难而上，也是我们技术人员的工作态度。

[image](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/fe796499-7c86-451e-9ac4-feb858f8e3bb/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466S2IXKWRP%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T225635Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDbIhM%2BWGRlD4RUvn4B7y7nVSYacJ%2Ffj9ZauM9kvd%2B4NwIhANU6fhNh10HFCclipiJsDYaPdxo512HmGFRX9ju%2Bl1szKogECMb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1Igwep3D%2Bd9HQqXtCBhkq3AOBOQQEXLZRB9ve8BSlOWu7NRFOcGN2QT8H7O%2F238asMaRveDWErJSiqisuEXKrsCzU3CNrj4kngBqhzcG3BMZfT8MOxuV7NHSEU3BQ2YBTGbCdSPwNxhVg8FEFiVS69aRjfy9%2FFU8B%2B6ei7osWX65p5WdEyFyWjAJ8TRSLd0deg7k3lkqdiNnH8uHs%2B5rc%2FohZeg2hzSOB0H7N71Fpdu38T31%2Fe9PnspAqPaYxEZFSFfUZ1%2FKmw5JSLp3E3r3b6yL%2BT9l5A0RNQAw7DfARX2XVqev1pY%2B3nQQ6ujriMWTbqFzC%2FzIkgIuZhkU3wRNrJ7EO3s9StF3UL85oWbqpN0CtW8VboXye3FcAgRPfNQFZyNGUkWPq41D90a%2FAIRNvtaZNxBb0FrvE98Vxhze6GIL3Kei0IYKfnlG019EOZgTF9XAMLeyhtfQhMfb0Kyfpe219D9hu6GKotgNmTW9nU0NSGvkUbWqW0CMukj9ioL5YoAUm9hfjs7iynCwrm%2B6KrJM2s9po%2F0bwyus8dOBGACrMp5ebGPbaEmJGsiadbkia1SWDv6haDylO7LnWW5WHpm%2F9FyzmyySE5mp7ipQiGq%2Bgi1HrXaVWigtghH4vEce59pZ79F99u9%2FxapB5wjCzuv%2FSBjqkAQ%2BZr%2Bi8SHMboZDcgbTHuVbmqugn%2BTID4CvdVisJH74sJPN0MMko8TTSzkVKWJeqFvvvq3Q1MK%2FRnx6lX5wByWifxRojVm5vpCc%2FIegEUKbFk2lRp29Fck7T5zsTZ3F3FR6yMeri8x06YVaMvYlBMnstel82A7x6tVP19zbKZU3wXedx0Qb3H8x%2F7%2FeqMaBGZSk%2BmMlnIbdwkkFz0jp87Nw8ESsf&X-Amz-Signature=66aaa39e9451b8e7e8dd0b537a80263bdc8f5cde0ab87604ca8aa1cffbe3af03&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)





