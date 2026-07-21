---
title: 3-2 【技术改造】电商系统集成Gateway - 配置网关层Redis限流
---

# 3-2 【技术改造】电商系统集成Gateway - 配置网关层Redis限流

[image](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/e88334f0-452c-42af-b941-bfb4bbb79b4d/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466Q474F7ST%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T225747Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCs1jm3VqPAw3VWoQCSjcxukeKjJSyw0cBFJs7Mk122JwIhAP%2FpM3KyUAEfKhxjNHA7%2FbMDc5JYnQgPB%2Fg7FJngTmGkKogECMb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgwdCU3BtNVVakVtlOIq3AOGG87yeqlucJpB0UZnHTThI3Wp8FgXiNkR6beoTJV4zoRgcl6BtFtwFaHGxqG1lwa7qUEj8MdPZxqjnGpB5otkgFIZNow3P3zjcDZ89uQitBTiWL7SlEIRFf9%2F5Wm40Aoe6anLQC7KAkATnsQTPkmmbHPXsLAMrjJ70MkWsJ5pLULSpfWPmX8krAoM3EVn5vAAybhzs4929WZeqDFOWr5mgJjb%2FR4kfEpIoeiuEmYMkex29IFADSsO4uZ3f9kya9DwT62UajSHkVJZ7Wm7G9teucwkFRxwngsaCk8IWmnmdQwTTp8dEhJRkkr3umtQsYhW8m3%2FmHWXyPGOSGOY9rv4j4DW7XFDagUD5FpVppBIKhmy60P%2FrSvSfdSxFiltQ1Nu2OgsWNMRzPCUQ11skIVAtrf%2FcVT5dhuHB2Mbr3y3vk6%2BmJwEqYYlViYolyPOZ5aBEUg%2B6IIhTa%2FKZjJ8fqHYIR0E5qw3gqQeFxfmkemBJ1XHPpGDND4UvMBhZvc2flpaCVe4ru3lpRpYxnGGgHGsLByFdOrdTpXIErkER0MGZB4YwXY4ysoH2O7PF1rJ5b6OU2JT43olpnYFFgF6zYlslKl3L%2FMZI0w1lZaeIFD2sJqyM8cnN4SAkbYR4jCWu%2F%2FSBjqkAfDxGKxGjfOEXTP5NYh9kUosGOxjOIfNP5iSidG3JJ6G3uLr%2FJDMOXavM%2BUvjOcfi%2BYDy%2BnW6kgxiUAS1cPuOlkysuzCFIzS9vYR7SHiO8I3Zt0qsOMQSNbvh6aoCbn1g0XJf%2BgzLPc1Cz6WUYeY3j5KsBkQvPsbCGD6UEXwXISwbkBzthqyTe6dvWV%2FSUBgfBK6%2B2CJ7ThX5Uo1KW%2FuGAL8SiOT&X-Amz-Signature=d60176a3ce9b7cb2fed50158e4e090ea191a23b24c22632bff8ab7f2ea1d084e&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

[image](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/3dcf7ca0-b06f-42fb-8752-42d03b8e8470/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466Q474F7ST%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T225747Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCs1jm3VqPAw3VWoQCSjcxukeKjJSyw0cBFJs7Mk122JwIhAP%2FpM3KyUAEfKhxjNHA7%2FbMDc5JYnQgPB%2Fg7FJngTmGkKogECMb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgwdCU3BtNVVakVtlOIq3AOGG87yeqlucJpB0UZnHTThI3Wp8FgXiNkR6beoTJV4zoRgcl6BtFtwFaHGxqG1lwa7qUEj8MdPZxqjnGpB5otkgFIZNow3P3zjcDZ89uQitBTiWL7SlEIRFf9%2F5Wm40Aoe6anLQC7KAkATnsQTPkmmbHPXsLAMrjJ70MkWsJ5pLULSpfWPmX8krAoM3EVn5vAAybhzs4929WZeqDFOWr5mgJjb%2FR4kfEpIoeiuEmYMkex29IFADSsO4uZ3f9kya9DwT62UajSHkVJZ7Wm7G9teucwkFRxwngsaCk8IWmnmdQwTTp8dEhJRkkr3umtQsYhW8m3%2FmHWXyPGOSGOY9rv4j4DW7XFDagUD5FpVppBIKhmy60P%2FrSvSfdSxFiltQ1Nu2OgsWNMRzPCUQ11skIVAtrf%2FcVT5dhuHB2Mbr3y3vk6%2BmJwEqYYlViYolyPOZ5aBEUg%2B6IIhTa%2FKZjJ8fqHYIR0E5qw3gqQeFxfmkemBJ1XHPpGDND4UvMBhZvc2flpaCVe4ru3lpRpYxnGGgHGsLByFdOrdTpXIErkER0MGZB4YwXY4ysoH2O7PF1rJ5b6OU2JT43olpnYFFgF6zYlslKl3L%2FMZI0w1lZaeIFD2sJqyM8cnN4SAkbYR4jCWu%2F%2FSBjqkAfDxGKxGjfOEXTP5NYh9kUosGOxjOIfNP5iSidG3JJ6G3uLr%2FJDMOXavM%2BUvjOcfi%2BYDy%2BnW6kgxiUAS1cPuOlkysuzCFIzS9vYR7SHiO8I3Zt0qsOMQSNbvh6aoCbn1g0XJf%2BgzLPc1Cz6WUYeY3j5KsBkQvPsbCGD6UEXwXISwbkBzthqyTe6dvWV%2FSUBgfBK6%2B2CJ7ThX5Uo1KW%2FuGAL8SiOT&X-Amz-Signature=ef726c4fd8c7402ee9434b557215569709639f5b53df5f3f294babf1449ea53f&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

[image](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/66b553c6-9237-43e4-a01b-c86ae7157cb1/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466Q474F7ST%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T225747Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCs1jm3VqPAw3VWoQCSjcxukeKjJSyw0cBFJs7Mk122JwIhAP%2FpM3KyUAEfKhxjNHA7%2FbMDc5JYnQgPB%2Fg7FJngTmGkKogECMb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgwdCU3BtNVVakVtlOIq3AOGG87yeqlucJpB0UZnHTThI3Wp8FgXiNkR6beoTJV4zoRgcl6BtFtwFaHGxqG1lwa7qUEj8MdPZxqjnGpB5otkgFIZNow3P3zjcDZ89uQitBTiWL7SlEIRFf9%2F5Wm40Aoe6anLQC7KAkATnsQTPkmmbHPXsLAMrjJ70MkWsJ5pLULSpfWPmX8krAoM3EVn5vAAybhzs4929WZeqDFOWr5mgJjb%2FR4kfEpIoeiuEmYMkex29IFADSsO4uZ3f9kya9DwT62UajSHkVJZ7Wm7G9teucwkFRxwngsaCk8IWmnmdQwTTp8dEhJRkkr3umtQsYhW8m3%2FmHWXyPGOSGOY9rv4j4DW7XFDagUD5FpVppBIKhmy60P%2FrSvSfdSxFiltQ1Nu2OgsWNMRzPCUQ11skIVAtrf%2FcVT5dhuHB2Mbr3y3vk6%2BmJwEqYYlViYolyPOZ5aBEUg%2B6IIhTa%2FKZjJ8fqHYIR0E5qw3gqQeFxfmkemBJ1XHPpGDND4UvMBhZvc2flpaCVe4ru3lpRpYxnGGgHGsLByFdOrdTpXIErkER0MGZB4YwXY4ysoH2O7PF1rJ5b6OU2JT43olpnYFFgF6zYlslKl3L%2FMZI0w1lZaeIFD2sJqyM8cnN4SAkbYR4jCWu%2F%2FSBjqkAfDxGKxGjfOEXTP5NYh9kUosGOxjOIfNP5iSidG3JJ6G3uLr%2FJDMOXavM%2BUvjOcfi%2BYDy%2BnW6kgxiUAS1cPuOlkysuzCFIzS9vYR7SHiO8I3Zt0qsOMQSNbvh6aoCbn1g0XJf%2BgzLPc1Cz6WUYeY3j5KsBkQvPsbCGD6UEXwXISwbkBzthqyTe6dvWV%2FSUBgfBK6%2B2CJ7ThX5Uo1KW%2FuGAL8SiOT&X-Amz-Signature=bc5cf7d921b98cfb77e71a56cdc8540f209722b3ee787ac0ad29f9d59f2a72ae&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

hello 慕课网的各位同学们，大家好，那咱这一节就继续推进深化咱商城项目的改造。好，我们在前面的图文小结当中是不是学习过了？咱如何在网关层给的位置里配置限流的规则？想在 gateway 当中的限流，我们也是利用 Redis 和 Lua 脚本来实现的。


那之前在图文教程里，我们的配置方式是在咱的 YAML 文件当中配置了一个路由规则，然后配置了一个 filter 在 filter 当中我们给定了限流的某些参数。那我们这里就从视频小结里面带着大家把这个流程熟悉一下。不过为了和图文教程互补，我们在这一小节当中用个不同的方式，咱不在 YAML 当中配置了，我们用 Java 的形式把这个限流给它配置进来。那既然说到限流配置，那咱总得有一个配置的地方对不对？我们这里创建一个 Java 类，那给它起名字就把它起叫 Redis limiter configuration 这个意思就是 Redis 的限流的意思。好我们点击创建。那在这个配置类上面，我们先给它加上一个什么注解呢？那就是所有配置项都会加上的 configuration 这个注解。那咱前面在图文教程当中学过，咱注解的有两个比较核心的要素。第一个要素是什么呢？ ID 通常我们也叫 key 它是什么 key 它是代表着你当前这个 request 的一个特征量。比如说你这里是基于 IP 地址限流的，那你所有进来的 request 不管它是访问哪个请求，那它这里都会带上一个什么，带上一个以 IPD 址为 K 的一个参数。那利用这个参数到 Redis 当中去查找对应的 IP 地址它当前的流量数据。


那如果你想以方法的名称作为限流，那同样的这个K ，那就应该是方法的名称，所以它会根据咱具体业务的不同来使用不同的 K 那我们在 Java 当中怎么来声明一个 key 呢？打个比方，我这里声明一个 host address 的 key 怎么声明一个方法加法方法，然后它返回一个 key resolver 这个 key resolver 就是一个具体的业务逻辑，它用来去定位你一个方法请求的 key 咱给它的方法名就叫做 remote address key resolver 好了，那接下来我 return 一个谁呢？ return 这样的一段逻辑，mono just just 什么呢？这里的逻辑就是具体返回你的 key 的地方。那这里怎么返回 key 那我把这个 exchange 主体拿到我们调用它的 get request 方法。好，你看到这个 get request 返回的类型，server HTTP request 对不对？那这里的步骤和咱前面的 demo 教学视频是一样的。那再往后走，我要 get remote address 那在这之后我还要再 get 一个address ，你跟查户口一样，我要查到底，把你的所有地址都给拿到。那最后终于到了他最后一个 ijs 我把这里换一行，太多了。


OK 那这最后一个是谁是 get host address 那通过这样一段逻辑，我们就可以把用户访问请求当中的 host address 来作为限流的一个 key 那我们给这个方法声明一个 bin 在声明完病之后，我们还要声明一个比较重要的属性 primary 那这里为什么我们要定义一个 primary 呢？因为早在真正的项目当中，肯定不只会声明一个 key resolver 那你会为具体不同的业务指定不同的 resolver 比如说你的用户模块，你想以 IP 地址限流，那你的商品模块，你想以用户的登录名称限流，你这每一个限流规则都需要生命成一个不同的 key resolver 所以这里在上下文当中你会出现很多个 key resolver 我们这里给其中的一个 key 加上 primary 这一个注解是为了避免我们的 gateway 框架在自动装配的过程中如果它引用了 key resolver 那我们这里定义了多个 resolver 那他不知道该是用哪一个，所以我们以防万一在这边加一个 primary 那我们自己的业务层当定义了多个 key resolver 的时候，我们可以很轻松地使用谁使用 autowire 的加这个注解 qualifier 来指定我想对某个具体业务使用哪一个不同的 key resolver 那么这里 K resolver 定义好之后，接下来我来定义一个谁呢？


那就是咱限流的这个主角是 Redis read limiterokay 那我给这个方法也同样的，就叫起名叫 Redis limiter 那它声明起来就简单多了我用最简单的方式我直接 return 一个 new Redis rate limiter 同学们看到它这里面有很多的构造参数，那有复杂的有简单的。比方说你上面你可以指定一个 Redis template 那你也可以指定你想用的限流的脚本在这里。


script Redis script 我们可以怎么样呢？手写一个 Lua 脚本，那使用自己的路外脚本来做这个限流的规则。那咱这里就一切从简，我们用这个最简单的构造器。


那两个参数的构造器，这两个参数分别是什么含义呢？那第一个参数它的意思是我的限流桶的速率，比方说我每秒给你发三个令牌，或者每秒给你发 5 个令牌。那这是第一个限流速率。那下面的第二个参数，default default 谁？ default 你桶的数量，

[image](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/de9233bb-53ae-481a-826f-5cd5f5e1eb18/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466Q474F7ST%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T225746Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCs1jm3VqPAw3VWoQCSjcxukeKjJSyw0cBFJs7Mk122JwIhAP%2FpM3KyUAEfKhxjNHA7%2FbMDc5JYnQgPB%2Fg7FJngTmGkKogECMb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgwdCU3BtNVVakVtlOIq3AOGG87yeqlucJpB0UZnHTThI3Wp8FgXiNkR6beoTJV4zoRgcl6BtFtwFaHGxqG1lwa7qUEj8MdPZxqjnGpB5otkgFIZNow3P3zjcDZ89uQitBTiWL7SlEIRFf9%2F5Wm40Aoe6anLQC7KAkATnsQTPkmmbHPXsLAMrjJ70MkWsJ5pLULSpfWPmX8krAoM3EVn5vAAybhzs4929WZeqDFOWr5mgJjb%2FR4kfEpIoeiuEmYMkex29IFADSsO4uZ3f9kya9DwT62UajSHkVJZ7Wm7G9teucwkFRxwngsaCk8IWmnmdQwTTp8dEhJRkkr3umtQsYhW8m3%2FmHWXyPGOSGOY9rv4j4DW7XFDagUD5FpVppBIKhmy60P%2FrSvSfdSxFiltQ1Nu2OgsWNMRzPCUQ11skIVAtrf%2FcVT5dhuHB2Mbr3y3vk6%2BmJwEqYYlViYolyPOZ5aBEUg%2B6IIhTa%2FKZjJ8fqHYIR0E5qw3gqQeFxfmkemBJ1XHPpGDND4UvMBhZvc2flpaCVe4ru3lpRpYxnGGgHGsLByFdOrdTpXIErkER0MGZB4YwXY4ysoH2O7PF1rJ5b6OU2JT43olpnYFFgF6zYlslKl3L%2FMZI0w1lZaeIFD2sJqyM8cnN4SAkbYR4jCWu%2F%2FSBjqkAfDxGKxGjfOEXTP5NYh9kUosGOxjOIfNP5iSidG3JJ6G3uLr%2FJDMOXavM%2BUvjOcfi%2BYDy%2BnW6kgxiUAS1cPuOlkysuzCFIzS9vYR7SHiO8I3Zt0qsOMQSNbvh6aoCbn1g0XJf%2BgzLPc1Cz6WUYeY3j5KsBkQvPsbCGD6UEXwXISwbkBzthqyTe6dvWV%2FSUBgfBK6%2B2CJ7ThX5Uo1KW%2FuGAL8SiOT&X-Amz-Signature=1bb5c03f72aa03559cd90674d7e5b6924b5c944b7e9d7abc20c38d0417f76c4c&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

这个令牌桶它的容量是有多大？那这是两个参数。好，我们这里给它随便指定一个。好了，咱给它指定。好，每秒钟 10 个令牌。然后你的这个桶子它有 20 个的容量，我们这里给它同样的加上一个并注解。那同学们会想，如果我想给不同的服务指定不同的限流规则，怎么办？非常好办。那咱这里可以假设这一个 Redis rate limiter 是给谁的呢？是给咱用户微服务指定的限流规则。好，我把这个 bin 加上一个名称，一个别名 ID 叫 Redis limiter user 证明它是给谁呢？

```java
package com.imooc;

import org.springframework.cloud.gateway.filter.ratelimit.KeyResolver;
import org.springframework.cloud.gateway.filter.ratelimit.RedisRateLimiter;
import org.springframework.context.annotation.Bean;
import org.springframework.context.annotation.Configuration;
import org.springframework.context.annotation.Primary;
import reactor.core.publisher.Mono;

/**
 * <h1></h1>
 */
@Configuration
public class RedisLimiterConfiguration {

    // HostAddressKey
    @Bean
    @Primary  // 以 IP地址限流
    public KeyResolver remoteAddKeyResolver() {
        return exchange -> Mono.just(
                exchange.getRequest()
                            .getRemoteAddress()
                            .getAddress()
                            .getHostAddress()
        );
    }

    @Bean("redisLimiterUser")
    @Primary
    public RedisRateLimiter redisLimiterUser() {
        return new RedisRateLimiter(10, 20);
    }

    @Bean("redisLimiterItem")
    @Primary
    public RedisRateLimiter redisLimiterItem() {
        return new RedisRateLimiter(20, 50);
    }
}
```

给用户为服务使用的。那接下来我再 copy 一个新的 Redis rate limiter 然后这里给它改成商品证明，我当前这个 limiter 是给商品服务来使用的，同样的它的这个 bin 我们给一个不同的名称叫 item 那咱商品调用多还是用户调用的多呢？好像是商品对吧？那我给它的限流给它改大一点。好了，我这边给它改成20，那它的令牌桶我改成50。


然后这里同样的我要指定一个 primary 为什么要指定 primary 呢？和前面的 key resolver 一样咱的 gateway 在加载的时候有一个自动装配的过程。那在这个自动装配车间当中有这样的一个类，它是使用的 gateway auto configuration 好，我们进来。那看到这一行在这里声明了一个 bin 那自动装配过程中这个 bin 他会去拿到你的 rate limiter 和 key resolver 那这里他期望的是什么呢？我只有一个实例。不过咱如果在应用当中声明了两个实例，像这里一个给 user 用，一个给 item 用。那这个 auto configuration 自动装配过程，抓瞎了，他不知道该用哪一个怎么办呢？那只好去启动的时候报错了对不对？所以我们这里给他指定一个 primary 就是告诉他你我选我 OK 把它作为一个默认的 Redis limit 好勒。那咱这里声明好了，这个 configuration 类。


接下来我们去做一个配置，我们找到 application YAML 那在这个里面，我们要声明 Redis 的配置，既然咱使用 Redis 限流，那我们自然要把这个 Redis 的连接串给它配置过来。好，我这里就使用最简单的单机版的单体的 Redis 来做连接，它这里在 spring 这一个 tag 下面添加一个 Redis 节点，在这里我指定 host host 是谁？ Local host. 然后它的端口我这里用的是默认的 6379 database 0。
那除了这个配置以外，我这里再给它加一个允许并重在 all of bin 加 finish overriding 好嘞，那我们使用 green witch 版的 spring cloud 经常会因为病重载导致的启动错误所以我个人比较习惯在每一个项目当中直接声明了这一句，一了百了解决所有烦恼。

```java
# 可以集成在 config-server进行配置

spring:
  application:
    name: platform-gateway
  redis:
    host: 172.16.136.222
    port: 6379
    database: 10
  main:
    allow-bean-definition-overriding: true
  cloud:
    gateway:
      locator:
        enabled: false
        lower-case-service-id: true
#        routes:   在代码中去配置路由吧

server:
  port: 20004

eureka:
  client:
    fetch-registry: false
    register-with-eureka: false
    service-url:
      defalultZone:  http://localhost:20000/eureka


# 开启所有 actuator-endpoint
management:
  endpoint:
    health:
      show-details: always
  endpoints:
    web:
      exposure:
        include: "*"
  security:
    enabled: false
```


好，那我们配置也改完了，然后 Redis 的这个限流的 key resolver 还有 Redis 的限流器也都声明了。那接下来我们就要到这个 roots configuration 里面，来把刚才配置好的这个限流器集成到我们的路由规则当中。


那我首先直接一个 private 变量把咱的 key resolver 给它拿过来。好，就起的名字叫 host name resolver 那这里 out wire 的进来。那因为我们这里只声明了一个 key resolver ，所以我们这里不用指定什么 qualifier 这样的注解。


但是下面的这个注解我们就要去指定使用哪一个 Redis 限流器了，因为咱刚才是不是配置了两个，一个给 user 一个给 item 好，那接下来在这里我们同样的声明一个 private 变量，它的类型， rate limiter 后面它的变量名也是 rate limiter 这里同样给它一个 out wire 的。但是在这下面我们要给它加一个 qualifier 这个注解我们用来指定去加载哪一个bin 。


好我们走到这个 Redis limiter configuration 这里，看看咱给 U user 服务指定的这个 bin 的名称叫 Redis limiter user 好我们把这个方法名给它 copy 下来，然后回来把它 copy 到这里去。好，那我们这里注入的就是一个给用户微服务模块创建的这样一个 Redis limit 好，那我们接下来就去找到用户模块在哪里，用户模块。好在这里，那我在他的 URI 返回之前我给他加一个 filters 说他叫filters ，但是我这里只打算给他加一个过滤器，那就是 request rate limiter 好，就加这个过滤器。好，我们把它打出来。那同学们如果想添加其他过滤器怎么办呢？非常简单，你在这个 F 后面打一个点，你可以看到。


哇这里面好多的过滤器，就是前面咱们的图文教程里面列出的那些比较重要的过滤器全在这里面。那这也是我比较喜欢使用 Java 这种配置方式的原因了，你这样选起来非常的直观，可读性也会更高。那咱添加了这个 request rate limit 之后，我们要给它指定属性了对不对？它的属性我这里给它声明一个 C 为什么叫 C 呢？这可不是 abc 乱起的，看它的这里面的参数叫 config consumer ，我这里就蓝省市了，给它声明一个 C 好了，那这个 C 我要指定两样东西，第一样东西是它的 key resolver 来自哪里？来自咱刚才把它给 out wired 进来的这个 host name resolver 好走，你进去。
第二个自然就是咱的 rate limiter 来自谁呢？来自咱这里声明的 rate limit 好，我把这个名称给它写得更可读性一点，后面加个 user 而证明它是给用户为服务来指定的限流规则，把它加上去。那同学们配完这两项，就可以去把这个项目启动起来，看一下限流是否起作用了。

```java
package com.imooc;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.beans.factory.annotation.Qualifier;
import org.springframework.cloud.gateway.filter.ratelimit.KeyResolver;
import org.springframework.cloud.gateway.filter.ratelimit.RedisRateLimiter;
import org.springframework.cloud.gateway.route.RouteLocator;
import org.springframework.cloud.gateway.route.builder.RouteLocatorBuilder;
import org.springframework.context.annotation.Bean;
import org.springframework.context.annotation.Configuration;
import org.springframework.http.HttpStatus;

/**
 * <h1></h1>
 */
@Configuration
public class RoutesConfiguration {

    @Autowired
    private KeyResolver hostNameResolver;

    @Autowired
    @Qualifier("redisLimiterUser")
    private RedisRateLimiter redisRateLimiter;


    @Bean
    public RouteLocator routes(RouteLocatorBuilder builder) {
        return builder.routes()
                //  FIXME 添加好这个（作业） search 服务自己实现掉
                .route(r -> r.path("/search/**", "/index/**", "/items/search","/items/catItems")
                        .uri("lb://FOODIE-SEARCH-SERVICE")
                )

                .route(r -> r.path("/address/**", "/password/**", "/userInfo/**", "/center/**")
                        .filters(f -> f.requestRateLimiter( c -> {
                                  c.setKeyResolver(hostNameResolver);
                                  c.setRateLimiter(redisRateLimiter);
                                  c.setStatusCode(HttpStatus.BAD_GATEWAY);
                                }
                        ))
                        .uri("lb://FOODIE-USER-SERVICE")
                )

                .route(r -> r.path("/items/**")
                        .uri("lb://FOODIE-ITEM-SERVICE")
                )

                .route(r -> r.path("/shopcart/**")
                        .uri("lb://FOODIE-CART-SERVICE")
                )

                .route(r -> r.path("/orders/**", "/myorders/**", "/mycomments/**")
                        .uri("lb://FOODIE-ORDER-SERVICE")
                )

                .build();
    }

}
```


那为了让限流的这个药效更明显，我们回到 configuration 这里，把配置项中的 Redis limited user 把它的限流给它缩小一点。让它每秒钟可以放行一个令牌，它的筒子可以最多放两个令牌。 OK 我们保存一下，然后直接开启它的慢方法。


那在启动完之后，到 postman 里去调用一把它的用户微服务，这里已经显示 started 那同学们记得，在启动咱 gateway 之前，我们为了验证用户微服务模块，还要去启动前置的几个微服务，分别是谁呢？尤维卡注册中心必不可少的。对不对？还有，咱的用户微服务是不是还调用了配置中心，所以 config 组件一定要把它启动起来。那这几个是咱需要启动的微服务部分。
那中间件这里我们记得，要把 Redis 启动起来，同学们千万要记得很多同学这一步可能会忘了几栋Redis ，那发现这个 request 一直在那 loading loading 怎么转还是转不出来呢？别忘了把 Redis 提东西了。那现在我们看到已经显示 started 了，所以我们转站到 postman 这里，我尝试向咱的 gateway 里面发送一个 address 杠 list 这样一个请求，它最终会转发到哪里呢？用户微服务模块对不对？好？我们这里点击 send 一个请求很快返回了，再点击 send 还是返回了，每秒钟访问一个，完全没有任何问题。那我们加快速度开始走起。


同学们看到这里，那是不是很多请求都被拦住了，那它这里显示什么呢？而显示 status 是429。那它的含义是 too many request 说明你的这个 request 发的太多太平了。那如果同学们想要定制一个 status 我不想要409。我想换一个怎么说，那我们回到咱的这个 gateway 代码当中，这里它还有一个配置参数，我们可以指定一个 set 谁呢？ Set status code. 那这个 status code 就是 HT DP status 里面的一个我们可以给它起名叫什么呢？ Bed gateway. 然后再把我们的 gateway 这里给它重新启动一下。

```java
package com.imooc;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.beans.factory.annotation.Qualifier;
import org.springframework.cloud.gateway.filter.ratelimit.KeyResolver;
import org.springframework.cloud.gateway.filter.ratelimit.RedisRateLimiter;
import org.springframework.cloud.gateway.route.RouteLocator;
import org.springframework.cloud.gateway.route.builder.RouteLocatorBuilder;
import org.springframework.context.annotation.Bean;
import org.springframework.context.annotation.Configuration;
import org.springframework.http.HttpStatus;

/**
 * <h1></h1>
 */
@Configuration
public class RoutesConfiguration {

    @Autowired
    private KeyResolver hostNameResolver;

    @Autowired
    @Qualifier("redisLimiterUser")
    private RedisRateLimiter redisRateLimiter;


    @Bean
    public RouteLocator routes(RouteLocatorBuilder builder) {
        return builder.routes()
                //  FIXME 添加好这个（作业） search 服务自己实现掉
                .route(r -> r.path("/search/**", "/index/**", "/items/search","/items/catItems")
                        .uri("lb://FOODIE-SEARCH-SERVICE")
                )

                .route(r -> r.path("/address/**", "/password/**", "/userInfo/**", "/center/**")
                        .filters(f -> f.requestRateLimiter( c -> {
                                  c.setKeyResolver(hostNameResolver);
                                  c.setRateLimiter(redisRateLimiter);
                                  c.setStatusCode(HttpStatus.BAD_GATEWAY);
                                }
                        ))
                        .uri("lb://FOODIE-USER-SERVICE")
                )

                .route(r -> r.path("/items/**")
                        .uri("lb://FOODIE-ITEM-SERVICE")
                )

                .route(r -> r.path("/shopcart/**")
                        .uri("lb://FOODIE-CART-SERVICE")
                )

                .route(r -> r.path("/orders/**", "/myorders/**", "/mycomments/**")
                        .uri("lb://FOODIE-ORDER-SERVICE")
                )

                .build();
    }

}
```


好，这里稍等片刻钟，他这边已经启动好了。好，我们回到波斯曼当中，再尝试发送同样的请求，点击快一点走。你好，我们看到他的 status 是不是已经发生了变化这里变成了谁 502 bad gatewayok 那到这里，咱这一小节的内容就告一段落了。


我们在这一小节当中带同学们通过 Java 配置文件的方式把 gateway 做了一个简单的限流配置。那我们只是配置了这个用户微服务模块，那剩下的几个微服务模块，同学们就自己随意发挥了，去找你认为最需要用限流进行保护的资源路径，然后为它配置一个自定义的限流规则。那这个限流规则它包含两部分，一个 host name resolver 还有一个 rate limiter userok 那这一节的内容就到这里结束了，不过老师想给同学们留一个作业，这个作业有点难。那这个作业的名称叫做 copy 不走样。



那 copy 谁呢？就是 copy 咱前面在用的这个 Redis rate limiter 那怎么个 copy 法，我们 copy 的是它的功能，也就是说我这里不想使用 Redis 作为限流，我想提供一种更加轻量级的限流方案。比方说什么呢？ in memory 内存级别的限流，构建一个 gvm 内存里的一个限流器。我们可以去参照 Redis rate limiter 里面的这些业务逻辑，看它是怎么来实现限流。这里面还包括一些非常细小的细节，比如说你看，它这里运用了很多 case 锁，你看 compare install 那我们通过去精读这个 Redis rate limit 的代码，然后搞懂它这里面是怎么来实现的。

[image](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/b91786bd-bd3d-4fab-aa2c-add9e6851534/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466Q474F7ST%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T225747Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCs1jm3VqPAw3VWoQCSjcxukeKjJSyw0cBFJs7Mk122JwIhAP%2FpM3KyUAEfKhxjNHA7%2FbMDc5JYnQgPB%2Fg7FJngTmGkKogECMb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgwdCU3BtNVVakVtlOIq3AOGG87yeqlucJpB0UZnHTThI3Wp8FgXiNkR6beoTJV4zoRgcl6BtFtwFaHGxqG1lwa7qUEj8MdPZxqjnGpB5otkgFIZNow3P3zjcDZ89uQitBTiWL7SlEIRFf9%2F5Wm40Aoe6anLQC7KAkATnsQTPkmmbHPXsLAMrjJ70MkWsJ5pLULSpfWPmX8krAoM3EVn5vAAybhzs4929WZeqDFOWr5mgJjb%2FR4kfEpIoeiuEmYMkex29IFADSsO4uZ3f9kya9DwT62UajSHkVJZ7Wm7G9teucwkFRxwngsaCk8IWmnmdQwTTp8dEhJRkkr3umtQsYhW8m3%2FmHWXyPGOSGOY9rv4j4DW7XFDagUD5FpVppBIKhmy60P%2FrSvSfdSxFiltQ1Nu2OgsWNMRzPCUQ11skIVAtrf%2FcVT5dhuHB2Mbr3y3vk6%2BmJwEqYYlViYolyPOZ5aBEUg%2B6IIhTa%2FKZjJ8fqHYIR0E5qw3gqQeFxfmkemBJ1XHPpGDND4UvMBhZvc2flpaCVe4ru3lpRpYxnGGgHGsLByFdOrdTpXIErkER0MGZB4YwXY4ysoH2O7PF1rJ5b6OU2JT43olpnYFFgF6zYlslKl3L%2FMZI0w1lZaeIFD2sJqyM8cnN4SAkbYR4jCWu%2F%2FSBjqkAfDxGKxGjfOEXTP5NYh9kUosGOxjOIfNP5iSidG3JJ6G3uLr%2FJDMOXavM%2BUvjOcfi%2BYDy%2BnW6kgxiUAS1cPuOlkysuzCFIzS9vYR7SHiO8I3Zt0qsOMQSNbvh6aoCbn1g0XJf%2BgzLPc1Cz6WUYeY3j5KsBkQvPsbCGD6UEXwXISwbkBzthqyTe6dvWV%2FSUBgfBK6%2B2CJ7ThX5Uo1KW%2FuGAL8SiOT&X-Amz-Signature=24bde6bc1d3b9785c25004dbd9d2da60e7984ed86bdc98bdd14c97970412bc36&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

那最后一步就是把这里面的代码还有这里面的业务流程转化为自己的一个限流工具类。那这个作业应该是前面老师出的所有作业当中，对同学们相对挑战会稍微大那么一点的，相信同学们，在这之中将体会到定制开源软件的乐趣。 OK 同学们，那这一小节就到此结束了，我们下一小节继续为网关层添砖加瓦。同学们，我们下一小节再见。




