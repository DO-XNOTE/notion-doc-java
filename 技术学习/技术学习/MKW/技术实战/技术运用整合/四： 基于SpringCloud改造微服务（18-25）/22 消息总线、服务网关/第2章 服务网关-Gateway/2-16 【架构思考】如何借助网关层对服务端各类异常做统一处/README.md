---
title: 2-16 【架构思考】如何借助网关层对服务端各类异常做统一处
---

# 2-16 【架构思考】如何借助网关层对服务端各类异常做统一处

[image](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/cdf7b6b8-e68d-44b3-9fa2-4b6477451597/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VRPM5EUL%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T225742Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCTHklEgm6U482WF3x083CBKOTdYKEW%2FdpuiXDHjcyRIwIgEEWeyq8D13yTVydtg9qrKDsDdlwrXuuuPvvapz%2FMjH4qiAQIxv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDIYCeAGJfk79YVmpFyrcAwafbhi%2B9v1WefIo%2BOBEfChhDNjmv2Krh9wzKld3%2Fn5FElZMV71QCeng0PKfQlToP8Ikvi2jHqXmb5%2FJB5DcssY%2FDRrf1tf1WS8LV4wUVHtPCnwY5gGawCpI3XJMV2nj%2FUydu3KKeLfHZxxgsmbtzD%2B%2BToCT3dtyKmeP5dAI2bW%2FqVtX0hLIdGzMpU5%2BwqKp3VlU5xZurYPq6gyC6gcz%2BysMfACtxpfVg%2BM9MbuxWmUvG8ZtKodkgaGGSzCqaf9M29tyAw3I6vLBEx5o2mjyUh17Q5ggm2AkHP2NOmF2Xlug6DgO4fqnMoy9vTCIt7vAY3LDIX9EWCB2a6Qxj%2BSKzZG%2BVsCDEwJJgky7yDirDoVktfdGJ5ny6POz30pTPihDdddBIPP%2FL93C7lXqgw7Koda%2F0g%2B4tmikWNN7sSAHdWAE%2BZ80llRjDtFoFKA3I7Aa2ghD0YF608ht%2FJKKKNsIeiBnbMk3%2BOl%2FxamurD9eSXUAhRpKkUUvWKD8rQGTvibl67rn9usmY%2FY%2B6%2BsxEaaRzMBPmORbus4YpHInWW%2FhuB0dJ3q%2FUUECW8jPwcgqq%2BvkG6hAxyIFBOeVL30WGTVKm2DoKF5aETIFyP4yBlRITERlnDvUZl6vhWSnDROwMJa4%2F9IGOqUBQJzcelVNnx6auBVPOYjx0TmZd1b51lddqMmrF4j%2BqQJDN2tw%2F49HIH%2BSP45WUK2kU8IiUKkbCPyrCPcXojIMPx9iwZy6bbkPhDSOdOsl7aXnVFnQjky9bT8jfZVm9CoSAq0C4mxqrQMww0CwIskhzmI2l5HQElAZv9LB8EY6%2F1ta%2BrvuV87Wi75Butomfzt%2FS9cTeO45E0zUI2Bq0GlHxFMGbKPq&X-Amz-Signature=e1c329b205dbfdbad1af021fee8a54601706591edfcc1bca6cc689c352840795&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

**2-16 【架构思考】如何借助网关层对服务端各类异常做统一处理**

前面我们在网关层搭建了一套基于JWT的用户鉴权服务，这一小节我们来探讨一下如何在网关层做统一异常处理。

**异常的种类**

网关层的异常分为以下两种：

调用请求异常 通常由调用请求直接抛出的异常，比如在订单服务中直接报错

```java
throw new RuntimeException("error")
```

网关层异常 由网关层触发的异常，比如Gateway通过服务发现找不到可用节点，或者任何网关层内部的问题。这部分异常通常是在实际调用请求发起之前发生的。

在以上两种问题中，我认为网关层只应该关注第二个点，也就是自身异常。在实际应用中我们应该尽量保持网关层的“纯洁性”并且做好职责划分，Gateway只要做好路由的事情，不要牵扯到具体业务层的事儿，最好也不要替调用请求的异常操心。对于业务调用中的异常情况，如果需要采用统一格式封装调用异常，那就交给每个具体服务去定义结构，让各自业务方和前端页面协调好异常消息的结构。

但是在实际项目中，不能保证每个接口都实现了异常封装，如果想给前台页面一个统一风格的JSON格式异常结构，那就需要让Gateway做一些分外的事儿，比如拦截Response并修改返回值。（我还是强烈建议让服务端自己定义异常结构，因为Gateway本身不应该对这些异常做额外封装只是原封不动的返回）

Gateway已经将网关层直接抛出的异常（没有调用远程服务之前的异常）做了结构化封装，对于POST的调用来说其本身也会返回结构化的异常信息，但是对于GET接口的异常来说，则是直接返回一个HTML页面，前端根本无法抓取具体的异常信息。所以我们今天就主要聚焦在如何处理调用请求异常。

**服务调用异常**

我们定义一个主动抛出异常的GET接口，然后通过网关层发起调用，会发现默认返回了HTML的异常页面。

当我们使用常规的全局异常处理方式会发现根本不起作用，这是为什么呢？因为我们目前使用的Greenwich版本底层是基于WebFlux来实现的，并不是Pure Servlet应用，因此常规的手段在这里不起作用。那么接下来，我就带大家通过添加一个过滤器，来处理异常调用，并且将返回值改为JSON格式。

**改造客户端异常**

我们先来看一看Gateway网关层异常情况下的返回数据

```java
{

"timestamp": "2019-10-26T15:13:29.870+0000",

"path": "/gateway/error",

"status": 500,

"error": "Internal Server Error",

"message": "Unable to find instance for FEIGN-SERVICE-PROVIDER"

}
```

看起来干净整洁，那我们是否可以在网关层对服务端返回的异常做一番改造，也呈现类似的效果呢？接下来，我们就运用最开始Eureka章节中学到的装饰器编程模式+代理模式，给Gateway加一层特效，改变ResponseBody中的数据结构，顺带也体验一下如何将编程模式运用到实际需求中。

**代理模式 - BodyHackerFunction接口**

在最开始我们先定义一个代理模式的接口

```java
package com.imooc.training;

import org.reactivestreams.Publisher;

import org.springframework.core.io.buffer.DataBuffer;

import org.springframework.http.server.reactive.ServerHttpResponse;

import reactor.core.publisher.Mono;

import java.util.function.BiFunction;

public interface BodyHackerFunction extends

BiFunction<ServerHttpResponse, Publisher<? extends DataBuffer>, Mono<Void>> {

}
```

这里引入代理模式是为了将装饰器和具体业务代理逻辑拆分开来，在装饰器中只需要依赖一个代理接口，而不需要和具体的代理逻辑绑定起来。

**装饰器模式 - BodyHackerDecrator**

接下来我们定义一个装饰器类，这个装饰器继承自ServerHttpResponseDecorator类，我们这里就用装饰器模式给Response Body的构造过程加上一层特效。

```java
package com.imooc.training;

import org.reactivestreams.Publisher;

import org.springframework.core.io.buffer.DataBuffer;

import org.springframework.http.server.reactive.ServerHttpResponse;

import org.springframework.http.server.reactive.ServerHttpResponseDecorator;

import reactor.core.publisher.Mono;

public class BodyHackerHttpResponseDecorator extends ServerHttpResponseDecorator {

/**

- 负责具体写入Body内容的代理类
- /

private BodyHackerFunction delegate = null;

public BodyHackerHttpResponseDecorator(BodyHackerFunction bodyHandler, ServerHttpResponse delegate) {

super(delegate);

this.delegate = bodyHandler;

}

@Override

public Mono<Void> writeWith(Publisher<? extends DataBuffer> body) {

return delegate.apply(getDelegate(), body);

}

}
```

这个装饰器的构造方法接收一个BodyHancker代理类，其中的关键方法writeWith就是用来向Response Body中写入内容的。这里我们覆盖了该方法，使用代理类来托管方法的执行，而在整个装饰器类中看不到一点业务逻辑，这就是我们常说的单一职责。

**创建Filter**

```java
@Component

@Slf4j

public class ErrorFilter implements GatewayFilter, Ordered {

@Override

public Mono<Void> filter(ServerWebExchange exchange, GatewayFilterChain chain) {

final ServerHttpRequest request = exchange.getRequest();

BodyHackerFunction delegate = // TODO 这里定义写入Body的逻辑

// 将装饰器当做Response返回

BodyHackerHttpResponseDecorator responseDecorator =

new BodyHackerHttpResponseDecorator(delegate, exchange.getResponse());

return chain.filter(exchange.mutate().response(responseDecorator).build());

}

@Override

public int getOrder() {

// WRITE_RESPONSE_FILTER的执行顺序是-1，我们的Hacker在它之前执行

return -2;

}

}
```

在这个Filter中，我们定义了一个装饰器类BodyHackerHttpResponseDecorator，同时声明了一个匿名内部类(代码TODO部分)，实现了BodyHackerFunction代理类的Body替换逻辑，并且将这个代理类传入了装饰器。这个装饰器将直接参与构造Response Body。

我们还覆盖了getOrder方法，是为了确保我们的filter在默认的Response构造器之前执行。

**改造Response Body**

这里就是上一步中标注TODO的部分

```java
BodyHackerFunction delegate = (resp, body) -> Flux.from(body)

.flatMap(orgBody -> {

// 原始的response body

byte[] orgContent = new byte[orgBody.readableByteCount()];

orgBody.read(orgContent);

String content = new String(orgContent);

log.info("original content {}", content);

// 如果500错误，则替换

if (resp.getStatusCode().value() == 500) {

content = String.format("{\"status\": %d,\"path\":\"%s\"}",

resp.getStatusCode().value(),

request.getPath().value());

}

// 告知客户端Body的长度，如果不设置的话客户端会一直处于等待状态不结束

HttpHeaders headers = resp.getHeaders();

headers.setContentLength(content.length());

return resp.writeWith(Flux.just(content)

.map(bx -> resp.bufferFactory().wrap(bx.getBytes())));

}).then();
```

我们对500的HTTP Status做了特殊定制，使用我们自己的JSON内容替换了原始内容，同学们可以根据需要向JSON中加入其它参数。对于其他非500 Status的Response来说，我们还是返回初始的Body。

这里有个需要注意的地方就是记得在header中设置content-length，让客户端知道Response中内容的长度，否则的话客户端会认为传输未结束，一直等在那里。

**使用Filter**

上面步骤都完成以后，接着我们就可以将这个filter应用在指定的路由规则中，或者定义成global filter，对所有路由规则生效。经过这次的改造，远程服务抛出的异常也在网关层做了统一处理，从HTML页面转为了JSON格式的数据。

**小结**

这一节我们学习了网关层的统一异常处理，顺带体验了一把设计模式在具体项目中的应用，下一节我们就来了解网关层的另一个功能-限流。

学习Tips：设计模式是程序员的一项内功，有时候读开源项目源码的时候被绕来绕去的逻辑搞蒙了，这时候不妨看看这些类的名称，你就很容易知道他们是应用了哪些设计模式（比如xxxDecorator肯定应用了装饰器模式，xxxTemplate就是模板模式），这样也就很方便搞清楚代码之间的组合关系。而且某几种设计模式经常被搭配在一起使用，这些都是需要在实践中慢慢积累的经验。

[image](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/e46d0319-7bed-4a6d-b9a4-7ed380323842/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VRPM5EUL%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T225742Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCTHklEgm6U482WF3x083CBKOTdYKEW%2FdpuiXDHjcyRIwIgEEWeyq8D13yTVydtg9qrKDsDdlwrXuuuPvvapz%2FMjH4qiAQIxv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDIYCeAGJfk79YVmpFyrcAwafbhi%2B9v1WefIo%2BOBEfChhDNjmv2Krh9wzKld3%2Fn5FElZMV71QCeng0PKfQlToP8Ikvi2jHqXmb5%2FJB5DcssY%2FDRrf1tf1WS8LV4wUVHtPCnwY5gGawCpI3XJMV2nj%2FUydu3KKeLfHZxxgsmbtzD%2B%2BToCT3dtyKmeP5dAI2bW%2FqVtX0hLIdGzMpU5%2BwqKp3VlU5xZurYPq6gyC6gcz%2BysMfACtxpfVg%2BM9MbuxWmUvG8ZtKodkgaGGSzCqaf9M29tyAw3I6vLBEx5o2mjyUh17Q5ggm2AkHP2NOmF2Xlug6DgO4fqnMoy9vTCIt7vAY3LDIX9EWCB2a6Qxj%2BSKzZG%2BVsCDEwJJgky7yDirDoVktfdGJ5ny6POz30pTPihDdddBIPP%2FL93C7lXqgw7Koda%2F0g%2B4tmikWNN7sSAHdWAE%2BZ80llRjDtFoFKA3I7Aa2ghD0YF608ht%2FJKKKNsIeiBnbMk3%2BOl%2FxamurD9eSXUAhRpKkUUvWKD8rQGTvibl67rn9usmY%2FY%2B6%2BsxEaaRzMBPmORbus4YpHInWW%2FhuB0dJ3q%2FUUECW8jPwcgqq%2BvkG6hAxyIFBOeVL30WGTVKm2DoKF5aETIFyP4yBlRITERlnDvUZl6vhWSnDROwMJa4%2F9IGOqUBQJzcelVNnx6auBVPOYjx0TmZd1b51lddqMmrF4j%2BqQJDN2tw%2F49HIH%2BSP45WUK2kU8IiUKkbCPyrCPcXojIMPx9iwZy6bbkPhDSOdOsl7aXnVFnQjky9bT8jfZVm9CoSAq0C4mxqrQMww0CwIskhzmI2l5HQElAZv9LB8EY6%2F1ta%2BrvuV87Wi75Butomfzt%2FS9cTeO45E0zUI2Bq0GlHxFMGbKPq&X-Amz-Signature=3ac02b2d0406ef09b56fc146d1a000c7424426585532b53f24f67a17e818671d&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



