---
title: 1-11 【架构思考】消息总线如何助攻其他业务场景
---

# 1-11 【架构思考】消息总线如何助攻其他业务场景

[image](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/6a7b4a1a-fbf8-4222-963b-2edec2dc2430/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466V7A6VJVC%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T225728Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCID5diQQlyL2iLaVqdAGxlQwT9DR3j0sjmSUdEago4B6%2FAiBWvrIZSaWgj0hujpnt05NRGu13he%2FxXakFu82aTBaqISqIBAjG%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMVeXRkI5Vp2covp9NKtwDbwshk3w3cbMUIfsSLewi%2FipLGR40eBJg9%2BmC9J%2FpPGArpa%2Fz%2BGtUsJDpsfXXsS9t4uOTHG5sU6CzKw%2FSsC6x5XeLg0UcYWb23qqV%2BOOcQPCdB%2FWZ1AjnmT1tyS63DJj%2BT9BYraqG3qUNxgxO%2B59y53uqaQHMwCPEVS%2BnvELtCG7t8lgNwoK7Sa8EfRqiAK07AlBiYWd66%2FP5jIZly5dfryzbQzUbju1P%2BrmQLAXy6krkxO%2FxQiUI0%2BMKqNTpvFSbBCnFqGmXFG7Zc4DLjKVj9bxeopaCzZxCT9Ewwf57N%2BdJgTrII1TRVRKALb6E5H3a9hU9pZV6m%2BRhFsTd58pMB0MCjJpPXo5iFBL8VQaCbEmPDzKTGz10Tg9S%2F5ei7z5VRqBX68PJ1QRbs3EIh0r9dxFSfdRaMccBWILU5LCEzKEr57buOPnR1fcqCwulghqWF77S0eTE2Oz4iMOPQ1MDxzQ5aDMBMXwfdvt4cWpX8gGC9FMhJgpeyzOY%2Beyy23TJFKcBSeQKRP799FBMm7piH2iaCMW4oNxT2T9zon7pGyizwymnKpkk4d9ldeVEVgUhcxUbwVLPDiIrUhgSoc7PBZunaHuuht%2BX5To5hbXWHx%2F35VVOFtlmv5DWwg8wtrj%2F0gY6pgHg68ij0%2BausSR0LnDnS%2BzMCec11JBnHkwI60yGsUYjOU8aCUr6vS4ZpnC3i0auBIC5mtPJ9paRM%2FhO3b886hINHqBNSM%2BO2xaQ%2BGJ9H2QkoqAX1puDBwMBsiOqJ1ju5vkYDZXqfefUpjZNRhJA4008HT6xlJHUh6wykz0L9ajomXoCV6CY0jxtawe6xjkRmb1Id35ZXctSRuksGY0FnQpGtPB6RU%2BR&X-Amz-Signature=b689f0e5a404cecd9daf88459d1d9ce810a75f1c24f05d5f48e79a674caacebf&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

[image](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/d99ccf01-70d1-43a7-b72d-2a4931df3534/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466V7A6VJVC%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T225728Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCID5diQQlyL2iLaVqdAGxlQwT9DR3j0sjmSUdEago4B6%2FAiBWvrIZSaWgj0hujpnt05NRGu13he%2FxXakFu82aTBaqISqIBAjG%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMVeXRkI5Vp2covp9NKtwDbwshk3w3cbMUIfsSLewi%2FipLGR40eBJg9%2BmC9J%2FpPGArpa%2Fz%2BGtUsJDpsfXXsS9t4uOTHG5sU6CzKw%2FSsC6x5XeLg0UcYWb23qqV%2BOOcQPCdB%2FWZ1AjnmT1tyS63DJj%2BT9BYraqG3qUNxgxO%2B59y53uqaQHMwCPEVS%2BnvELtCG7t8lgNwoK7Sa8EfRqiAK07AlBiYWd66%2FP5jIZly5dfryzbQzUbju1P%2BrmQLAXy6krkxO%2FxQiUI0%2BMKqNTpvFSbBCnFqGmXFG7Zc4DLjKVj9bxeopaCzZxCT9Ewwf57N%2BdJgTrII1TRVRKALb6E5H3a9hU9pZV6m%2BRhFsTd58pMB0MCjJpPXo5iFBL8VQaCbEmPDzKTGz10Tg9S%2F5ei7z5VRqBX68PJ1QRbs3EIh0r9dxFSfdRaMccBWILU5LCEzKEr57buOPnR1fcqCwulghqWF77S0eTE2Oz4iMOPQ1MDxzQ5aDMBMXwfdvt4cWpX8gGC9FMhJgpeyzOY%2Beyy23TJFKcBSeQKRP799FBMm7piH2iaCMW4oNxT2T9zon7pGyizwymnKpkk4d9ldeVEVgUhcxUbwVLPDiIrUhgSoc7PBZunaHuuht%2BX5To5hbXWHx%2F35VVOFtlmv5DWwg8wtrj%2F0gY6pgHg68ij0%2BausSR0LnDnS%2BzMCec11JBnHkwI60yGsUYjOU8aCUr6vS4ZpnC3i0auBIC5mtPJ9paRM%2FhO3b886hINHqBNSM%2BO2xaQ%2BGJ9H2QkoqAX1puDBwMBsiOqJ1ju5vkYDZXqfefUpjZNRhJA4008HT6xlJHUh6wykz0L9ajomXoCV6CY0jxtawe6xjkRmb1Id35ZXctSRuksGY0FnQpGtPB6RU%2BR&X-Amz-Signature=97c9d044df030b14b74d5db549debcbe4f754330758f4e0c0f72c34c7e4364b5&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

**Bus如何助攻其他业务场景**

前面我们学习了Bus的主要应用场景-推送配置变更，这难道是Bus的全部本领吗？就这点本事还能进Spring Cloud？

我们知道Spring Cloud的组件个个身怀十八般武艺，每个组件都有几样拿手的功能，可谓是一专多长。再看Bus，好像似乎除了推送变更啥也不会。大家有所不知，Bus是Spring Cloud的特长生，这“推送”就是它的特长。就像健美操特长都能进清华一样，Bus就靠着这一手排山倒海的推送特长，进了Spring Cloud，专门处理各种广播消息推送，不只局限在配置变更推送。

我们接下来就看看，Bus如何通过自定义事件，实现消息广播。

**发布-订阅模型**

[image](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/a262e691-840b-4c74-855f-87af237e516f/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466V7A6VJVC%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T225728Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCID5diQQlyL2iLaVqdAGxlQwT9DR3j0sjmSUdEago4B6%2FAiBWvrIZSaWgj0hujpnt05NRGu13he%2FxXakFu82aTBaqISqIBAjG%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMVeXRkI5Vp2covp9NKtwDbwshk3w3cbMUIfsSLewi%2FipLGR40eBJg9%2BmC9J%2FpPGArpa%2Fz%2BGtUsJDpsfXXsS9t4uOTHG5sU6CzKw%2FSsC6x5XeLg0UcYWb23qqV%2BOOcQPCdB%2FWZ1AjnmT1tyS63DJj%2BT9BYraqG3qUNxgxO%2B59y53uqaQHMwCPEVS%2BnvELtCG7t8lgNwoK7Sa8EfRqiAK07AlBiYWd66%2FP5jIZly5dfryzbQzUbju1P%2BrmQLAXy6krkxO%2FxQiUI0%2BMKqNTpvFSbBCnFqGmXFG7Zc4DLjKVj9bxeopaCzZxCT9Ewwf57N%2BdJgTrII1TRVRKALb6E5H3a9hU9pZV6m%2BRhFsTd58pMB0MCjJpPXo5iFBL8VQaCbEmPDzKTGz10Tg9S%2F5ei7z5VRqBX68PJ1QRbs3EIh0r9dxFSfdRaMccBWILU5LCEzKEr57buOPnR1fcqCwulghqWF77S0eTE2Oz4iMOPQ1MDxzQ5aDMBMXwfdvt4cWpX8gGC9FMhJgpeyzOY%2Beyy23TJFKcBSeQKRP799FBMm7piH2iaCMW4oNxT2T9zon7pGyizwymnKpkk4d9ldeVEVgUhcxUbwVLPDiIrUhgSoc7PBZunaHuuht%2BX5To5hbXWHx%2F35VVOFtlmv5DWwg8wtrj%2F0gY6pgHg68ij0%2BausSR0LnDnS%2BzMCec11JBnHkwI60yGsUYjOU8aCUr6vS4ZpnC3i0auBIC5mtPJ9paRM%2FhO3b886hINHqBNSM%2BO2xaQ%2BGJ9H2QkoqAX1puDBwMBsiOqJ1ju5vkYDZXqfefUpjZNRhJA4008HT6xlJHUh6wykz0L9ajomXoCV6CY0jxtawe6xjkRmb1Id35ZXctSRuksGY0FnQpGtPB6RU%2BR&X-Amz-Signature=7dfbd7b5956cad9eea32c5ddd94b5ec058f9e05c4b95e9533239cd167b955f13&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

Bus的事件推送由三个角色构成：

事件对象：Bus中定义的一个事件类，通常是一个Pojo对象，包含了消费者需要的信息

事件发布：Bus作为生产者，将事件对象通过广播的形式发布出去

事件监听：由消费者主动监听Bus的事件发布动作，当获取到事件对象后会调用处理方法进行消费

**自定义事件**

**自定义事件对象**

Bus的所有事件对象都继承自ApplicationEvent或者RemoteApplicationEvent，我们可以仿照bus-refresh功能定义的事件类RefreshRemoteApplicationEvent中的写法，定义一个MyEvent类

```java
public class MyEvent extends RemoteApplicationEvent {

public MyEvent() {

}

public MyEvent(Object body, String originService, String destinationService) {

super(body, originService, destinationService);

}

}
```

其中第一个参数可以自定义一个POJO类，大家可以根据自己的需求随意添加属性，但是要保证这个类实现了序列化/反序列化接口（implements Serializable）。

**配置自定义对象**

在创建了MyEvent之后，我们需要将它加载到Bus的上下文中，这里可以通过@Configuration和@RemoteApplicationEventScan注解将MyEvent加载进来

```java
@Configuration
@RemoteApplicationEventScan(basePackageClasses = MyEvent.class)

public class BusExtConfiguration {

}
```

**监听事件**

我们要在服务节点添加事件监听器，用来监听服务发布动作，这一步可以通过@EventListener方法级别的注解来实现（可以参考RefreshEventListener类），接收的参数就是第一步中创建的EventBody，Bus会帮我们将消息反序列化为Java类。也可以通过继承ApplicationListener接口来实现，示例如下：

```java
@Component

public class MyEventListener implements ApplicationListener<MyEvent> {

@Override

public void onApplicationEvent(MyEvent event) {

logger.info("Received MyCustomRemoteEvent - message: ");

}

}
```

**发布事件**

万事俱备之后，我们只需要一个发布事件的地方了（在消息生产者处实现），我们可以创建一个简单的Controller，然后对外提供一个POST方法，比如：

```java
@PostMapping("/bus/publish/myevent")

public boolean publishMyEvent(@RequestBody EventBody body) {

MyEvent event = new MyEvent(body, applicationContext.getId(), "");

try {

// 可以注入ApplicationEventPublisher来发送event

eventPublisher.publishEvent(event);

// 也可以直接使用

// applicationContext.publishEvent(event)

return true;

} catch (Exception e) {

log.error("failed in publishing event", e);

}

return false;

}
```

我们有两种方式发送event，一种是通过依赖注入ApplicationEventPublisher的实例来发送，现有的bus-refresh功能也是使用这种方式。另一种是直接通过ApplicationContext来发送，由于前面我们通过@RemoteApplicationEventScan注解已经将MyEvent注册为Bus的一个事件，这样ApplicationContext会把MyEvent当做一个Bus总线事件，而不是在Context范围内发布一个Regular Event。

**应用场景**

通过上面的方式我们可以将自定义事件广播到所有监听该事件的节点，让所有消费者触发事件响应。消息广播的使用场景非常多，我们随便举两个实际应用中的例子：

清空缓存：通知所有服务监听者清空某项业务的本地缓存信息，我们也可以在自定义的消息体中加业务属性，事件监听逻辑可以根据这些属性来定点清除某个特定业务对象的缓存

数据同步：子系统依赖实时的数据库记录变动触发相应的业务逻辑，我们这里就可以将数据库的binlog抓取出来，通过广播功能同步到所有监听器，起到数据同步的作用

**小结**

这一节我们学习了Bus中自定义事件的实现方式，到这里Bus章节就算告一段落了，下一章我们将去学习微服务架构中的一个重要模块-网关层Gateway。

学习Tips：有的时候看图文教程和视频会感觉知识很好理解，但是一上手写程序就要各种求助百度。没有下手练习的话，所有学习都是纸上谈兵，尤其对于实战技术来说。只要搞懂不要动手的只有一个场景，那就是面试前的知识突击。所以大家一定要多动手，把每个小Demo都自己去实现一遍，我们的课程项目也给大家留了很大的操作空间，同学们可以把每一章学到的内容应用在更多的模块中。

[image](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/76b45683-bc74-478d-9982-3f1ab0e3add5/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466V7A6VJVC%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T225728Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCID5diQQlyL2iLaVqdAGxlQwT9DR3j0sjmSUdEago4B6%2FAiBWvrIZSaWgj0hujpnt05NRGu13he%2FxXakFu82aTBaqISqIBAjG%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMVeXRkI5Vp2covp9NKtwDbwshk3w3cbMUIfsSLewi%2FipLGR40eBJg9%2BmC9J%2FpPGArpa%2Fz%2BGtUsJDpsfXXsS9t4uOTHG5sU6CzKw%2FSsC6x5XeLg0UcYWb23qqV%2BOOcQPCdB%2FWZ1AjnmT1tyS63DJj%2BT9BYraqG3qUNxgxO%2B59y53uqaQHMwCPEVS%2BnvELtCG7t8lgNwoK7Sa8EfRqiAK07AlBiYWd66%2FP5jIZly5dfryzbQzUbju1P%2BrmQLAXy6krkxO%2FxQiUI0%2BMKqNTpvFSbBCnFqGmXFG7Zc4DLjKVj9bxeopaCzZxCT9Ewwf57N%2BdJgTrII1TRVRKALb6E5H3a9hU9pZV6m%2BRhFsTd58pMB0MCjJpPXo5iFBL8VQaCbEmPDzKTGz10Tg9S%2F5ei7z5VRqBX68PJ1QRbs3EIh0r9dxFSfdRaMccBWILU5LCEzKEr57buOPnR1fcqCwulghqWF77S0eTE2Oz4iMOPQ1MDxzQ5aDMBMXwfdvt4cWpX8gGC9FMhJgpeyzOY%2Beyy23TJFKcBSeQKRP799FBMm7piH2iaCMW4oNxT2T9zon7pGyizwymnKpkk4d9ldeVEVgUhcxUbwVLPDiIrUhgSoc7PBZunaHuuht%2BX5To5hbXWHx%2F35VVOFtlmv5DWwg8wtrj%2F0gY6pgHg68ij0%2BausSR0LnDnS%2BzMCec11JBnHkwI60yGsUYjOU8aCUr6vS4ZpnC3i0auBIC5mtPJ9paRM%2FhO3b886hINHqBNSM%2BO2xaQ%2BGJ9H2QkoqAX1puDBwMBsiOqJ1ju5vkYDZXqfefUpjZNRhJA4008HT6xlJHUh6wykz0L9ajomXoCV6CY0jxtawe6xjkRmb1Id35ZXctSRuksGY0FnQpGtPB6RU%2BR&X-Amz-Signature=338874087b0ea8df763b2ba701780e1c66ce2ecd99c9cdbc9d574a7af6fd092c&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)




