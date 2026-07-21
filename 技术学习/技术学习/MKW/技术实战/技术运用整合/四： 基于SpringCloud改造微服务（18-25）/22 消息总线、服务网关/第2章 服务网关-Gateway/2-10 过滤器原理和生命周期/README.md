---
title: 2-10 过滤器原理和生命周期
---

# 2-10 过滤器原理和生命周期

[image](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/de43db4a-dfd4-4b17-97cb-6320d495c96c/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZP6CUUGH%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T225737Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQD44BApSYnCGNhKtLtLnDeDJnloUUbFxhHcFJcy6nfArwIhAI9jEkvat%2FNZyR%2BzIJOdzx91Ajb9B1DKfMdIApvFh1xwKogECMb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgxV44JBg1tLBf0ocpwq3AO%2BhjmJHWgGUc8JtKZ55cV2UIRT8ex9im7H%2B%2BaNV%2BADugEPQE0XDriydP4e%2FEnQIwORo0XhuCpGDlNDn%2FL1j4uj1XicADZ9X5ThUHvToddXZ7MFvmPC33Hh0fIUViPpaLhp%2FrK6nXdG%2BYzYBSV3Oy829RsiVO0ntOc7jnc9DmXt06Lq76Rd2KMisXMvVjMbfVH8SdPHDdE5Bjfrc1ZXoRj6ZFUuwFmdj6efUT7z1dSf5A8gyPMRgl3zIcS511OBrO6Ygr41nEyylFx75ZQCd6rDNkGdLOqsVlUyFpmFg7eAaFdVpyx%2By7D5%2FdXALn74lfP0D8wBWrWaagDc%2FTT8P0hFa8hNAyqq7dhcfaaaEKy3z6lVSIpWpnqN0M7DJxuGJsa2C6V9ktZ%2FrD2BTpe2Ht1VYjKNAsdbtlWLOd3rJ3P0nmNVdcWnbgOZxz%2FlHoKP3AkgF%2FUbJxveHepb0%2BlWWPB4VoyFIougr251whyKapogPMWkLKUZCMitT35Gq4DtJdMwq7Ut4SE7RgomGwzj8OB0XXRX75kkss%2FvrqEWLpZqgvmz3cbHGFr9iGqCUsS3rSl%2Byb8kX8be6qYS1Vn%2F9JEEYeFyM05sZGfwaDhIjDoIaNXwj%2Bzp9FX%2B0OVMbTCkt%2F%2FSBjqkAZ%2BXHP8nxwomqrCRkcpnEeDxf3FI9hzXS933p9aJVVwbKEM6NJNsc0GpKVailk8W5HuZwPFNiLvsgQE%2BwpO3mVUSN1WQq7AUnneMlnz8cuoKF8pSO6P0YXNB5l1TNmVGuhS8eQKKzcpq7n2SmUjjhFCbf%2FHoT4fbk5tDoTpK%2BOd496WVc0rqn%2FT%2B%2By06IXHIDTGO6NMLXtD1ILo5rAD8%2FURyvGfb&X-Amz-Signature=a16f10387b9460ce18401d193022e2d6fd3c51000ef1f5bae6652d7e7dc0e32f&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

**2-10 过滤器原理和生命周期**

前面我们学习了Gateway的路由和断言功能，这一节我们来了解下过滤器原理，再挑几个常用的过滤器学习一下。

**过滤器的工作模式**

所有开源框架实现过滤器的模式都是大同小异，通过一种类似职责链的方式，传统的职责链模式中的事件会传递直到有一个处理对象接手，而过滤器和传统的职责链有点不同，它更像是足球队开场握手一样，所有队员一字排开，你要从头到尾依次和所有球员握过手。

[image](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/6af6cae3-6f42-4ce9-8e85-289ac92f8cad/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZP6CUUGH%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T225737Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQD44BApSYnCGNhKtLtLnDeDJnloUUbFxhHcFJcy6nfArwIhAI9jEkvat%2FNZyR%2BzIJOdzx91Ajb9B1DKfMdIApvFh1xwKogECMb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgxV44JBg1tLBf0ocpwq3AO%2BhjmJHWgGUc8JtKZ55cV2UIRT8ex9im7H%2B%2BaNV%2BADugEPQE0XDriydP4e%2FEnQIwORo0XhuCpGDlNDn%2FL1j4uj1XicADZ9X5ThUHvToddXZ7MFvmPC33Hh0fIUViPpaLhp%2FrK6nXdG%2BYzYBSV3Oy829RsiVO0ntOc7jnc9DmXt06Lq76Rd2KMisXMvVjMbfVH8SdPHDdE5Bjfrc1ZXoRj6ZFUuwFmdj6efUT7z1dSf5A8gyPMRgl3zIcS511OBrO6Ygr41nEyylFx75ZQCd6rDNkGdLOqsVlUyFpmFg7eAaFdVpyx%2By7D5%2FdXALn74lfP0D8wBWrWaagDc%2FTT8P0hFa8hNAyqq7dhcfaaaEKy3z6lVSIpWpnqN0M7DJxuGJsa2C6V9ktZ%2FrD2BTpe2Ht1VYjKNAsdbtlWLOd3rJ3P0nmNVdcWnbgOZxz%2FlHoKP3AkgF%2FUbJxveHepb0%2BlWWPB4VoyFIougr251whyKapogPMWkLKUZCMitT35Gq4DtJdMwq7Ut4SE7RgomGwzj8OB0XXRX75kkss%2FvrqEWLpZqgvmz3cbHGFr9iGqCUsS3rSl%2Byb8kX8be6qYS1Vn%2F9JEEYeFyM05sZGfwaDhIjDoIaNXwj%2Bzp9FX%2B0OVMbTCkt%2F%2FSBjqkAZ%2BXHP8nxwomqrCRkcpnEeDxf3FI9hzXS933p9aJVVwbKEM6NJNsc0GpKVailk8W5HuZwPFNiLvsgQE%2BwpO3mVUSN1WQq7AUnneMlnz8cuoKF8pSO6P0YXNB5l1TNmVGuhS8eQKKzcpq7n2SmUjjhFCbf%2FHoT4fbk5tDoTpK%2BOd496WVc0rqn%2FT%2B%2By06IXHIDTGO6NMLXtD1ILo5rAD8%2FURyvGfb&X-Amz-Signature=c599e2a29963bb51ff1944cd3b8cc8a0054957ee4554090890213246d92782da&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

Gateway中的过滤器也是一样的模型，他们经过优先级的排列，所有网关调用请求从最高优先级的过滤器开始，一路走到头，直到被最后一个过滤器处理。

**过滤器的实现方式**

在Gateway中实现一个过滤器非常简单，只要实现GatewayFilter接口的默认方法就好了

```java
@Override

public Mono<Void> filter(ServerWebExchange exchange, GatewayFilterChain chain) {

// 随意发挥

return chain.filter(exchange);

}
```

这里面有两个关键信息：

ServerWebExchange 这是Spring封装的HTTP request-response交互协议，从中我们可以获取request和response中的各种请求参数，也可以向其中添加内容

GatewayFilterChain 它是过滤器的调用链，在方法结束的时候我们需要将exchange对象传入调用链中的下一个对象

**过滤器的执行阶段**

不同于Spring Cloud中上一代网关组件Zuul里对过滤器的Pre和Post的定义，Gateway是通过Filter中的代码来实现类似Pre和Post的效果。

Pre和Post是指代当前过滤器的执行阶段，Pre是在下一个过滤器之前被执行，Post是在过滤器执行过后再执行。我们在Gateway Filter中也可以同时定义Pre和Post执行逻辑。

**Pre类型**

我们就拿AddResponseHeaderGatewayFilterFactory举例，它可以向Response中添加Header信息：

```java
@Override

public GatewayFilter apply(NameValueConfig config) {

return (exchange, chain) -> {

exchange.getResponse().getHeaders().add(config.getName(), config.getValue());

return chain.filter(exchange);

};

}
```

这里的具体执行方法是定义在调用“chain.filter()”方法之前，也就是在转发到下级调用链路之前执行的，因此可以理解为一个Pre类型的过滤器。

**Post类型**

我们拿SetStatusGatewayFilterFactory举例，它在过滤器执行完毕之后，将制定的HTTP status返回给调用方。

```java
return chain.filter(exchange).then(Mono.fromRunnable(() -> {

// 这里是业务逻辑

}));
```

这个过滤器的主要逻辑在then方法中，then是一个回调函数，在下级调用链路都完成以后再执行，因此这类过滤器可以看做是Post Filter。

**过滤器排座次**

在Gateway中我们可以通过实现org.springframework.core.Ordered接口，来给过滤器指定执行顺序，比如下面的代码实现了Ordered接口方法，将过滤器执行顺序设置为0：

```java
@Override

public int getOrder() {

return 0;

}
```

Pre类型的过滤器来说，数字越大表示优先级越高，也就越早被执行。但对于Post类型的过滤器，则是数字越小越先被执行。

**过滤器示例**

半仙老师： 我们Gateway的组件库相当丰富，有二十多个过滤器，接下来我们挨个看一看

体育委员：拖堂了老师，能不能挑重点

半仙老师：哦，那我们随便看5个吧，剩下的过滤器作为课后作业，大家去

```java
org.springframework.cloud.gateway.filter.factory
```

包里面查看

**Header过滤器**

这个系列有很多组过滤器，AddRequestHeader和AddResponseHeader，分别向Request和Response里加入指定Header。相应的RemoveRequestHeader和RemoveResponseHeader分别做移除操作，用法也很简单：

```java
.filters(f -> f.addResponseHeader("who", "gateway-header"))
```

上面的例子会向header中添加一个who的属性，对应的值是gateway-header。

**StripPrefix过滤器**

这是个比较常用的过滤器，它的作用是去掉部分URL路径。比如我们的过滤器配置如下：

```java
.route(r -> r.path("/gateway-test/**")

.filters(f -> f.stripPrefix(1))

.uri("lb://FEIGN-SERVICE-PROVIDER/")

)
```

假如HTTP请求访问的是

```java
/gateway-test/sample/update
```

，如果没有StripPrefix过滤器，那么转发到FEIGN-SERVICE-PROVIDER服务的访问路径也是一样的。当我们添加了这个过滤器之后，Gateway就会根据“stripPrefix(1)”中的值截取URL中的路径，比如这里我们设置的是1，那么就去掉一个前缀，最终发送给后台服务的路径变成了“/sample/update”

**PrefixPath过滤器**

它和StripPrefix的作用是完全相反的，会在请求路径的前面加入前缀

```java
.route(r -> r.path("/gateway-test/**")

.filters(f -> f.prefixPath("go"))

.uri("lb://FEIGN-SERVICE-PROVIDER/")

)
```

比如说我们访问“/gateway-test/sample”的时候，上面例子中配置的过滤器就会把请求发送到“/go/gateway-test/sample”。

**RedirectTo过滤器**

它可以把收到特定状态码的请求重定向到一个指定网址：

```java
.filters(f -> f.redirect(302, "https://www.imooc.com/"))
```

上面的例子接收HTTP status code和URL两个参数，如果请求结果是404，则重定向到第二个参数指定的页面，这个功能也可以做统一异常处理，将Unauthorized或Forbidden请求重定向到登录页面。

**SaveSession过滤器**

我们知道微服务是无状态的会话，所以大多都不依赖session机制，但是如果你有分布式session的需求，比如说某些功能是基于spring-session和spring-security来实现的，那么这个过滤器或许对你有用，它在调用服务之前都会强制保存session

```java
.filters(f -> f.saveSession())
```

**小结**

这一节我们学习了Gateway组件的过滤器，接下来我们就去动手创建一个过滤器，用来实现方法计时功能。

学习Tips：在Spring Cloud的源码中可以看到大量回调函数的实现方式，自从Java 8的lambda表达式发布以来，Java的风格也逐渐偏向函数式语言。像回调这类函数语言的用法，或者lambda的stream函数操作Collection类的用法，确实在某些场景下可以减少大量代码。同学们可以多参考一些类似的例子，在工作里面用起来，让Code变得优雅也是一种实力表现。

[image](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/4a11269c-39fe-43e0-9bf2-93af4cabec63/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZP6CUUGH%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T225737Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQD44BApSYnCGNhKtLtLnDeDJnloUUbFxhHcFJcy6nfArwIhAI9jEkvat%2FNZyR%2BzIJOdzx91Ajb9B1DKfMdIApvFh1xwKogECMb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgxV44JBg1tLBf0ocpwq3AO%2BhjmJHWgGUc8JtKZ55cV2UIRT8ex9im7H%2B%2BaNV%2BADugEPQE0XDriydP4e%2FEnQIwORo0XhuCpGDlNDn%2FL1j4uj1XicADZ9X5ThUHvToddXZ7MFvmPC33Hh0fIUViPpaLhp%2FrK6nXdG%2BYzYBSV3Oy829RsiVO0ntOc7jnc9DmXt06Lq76Rd2KMisXMvVjMbfVH8SdPHDdE5Bjfrc1ZXoRj6ZFUuwFmdj6efUT7z1dSf5A8gyPMRgl3zIcS511OBrO6Ygr41nEyylFx75ZQCd6rDNkGdLOqsVlUyFpmFg7eAaFdVpyx%2By7D5%2FdXALn74lfP0D8wBWrWaagDc%2FTT8P0hFa8hNAyqq7dhcfaaaEKy3z6lVSIpWpnqN0M7DJxuGJsa2C6V9ktZ%2FrD2BTpe2Ht1VYjKNAsdbtlWLOd3rJ3P0nmNVdcWnbgOZxz%2FlHoKP3AkgF%2FUbJxveHepb0%2BlWWPB4VoyFIougr251whyKapogPMWkLKUZCMitT35Gq4DtJdMwq7Ut4SE7RgomGwzj8OB0XXRX75kkss%2FvrqEWLpZqgvmz3cbHGFr9iGqCUsS3rSl%2Byb8kX8be6qYS1Vn%2F9JEEYeFyM05sZGfwaDhIjDoIaNXwj%2Bzp9FX%2B0OVMbTCkt%2F%2FSBjqkAZ%2BXHP8nxwomqrCRkcpnEeDxf3FI9hzXS933p9aJVVwbKEM6NJNsc0GpKVailk8W5HuZwPFNiLvsgQE%2BwpO3mVUSN1WQq7AUnneMlnz8cuoKF8pSO6P0YXNB5l1TNmVGuhS8eQKKzcpq7n2SmUjjhFCbf%2FHoT4fbk5tDoTpK%2BOd496WVc0rqn%2FT%2B%2By06IXHIDTGO6NMLXtD1ILo5rAD8%2FURyvGfb&X-Amz-Signature=c8b9e18b8731b0f7d429daae29c788ad57d5edd326b4c92e6fe4bf5e57ead0d1&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)





