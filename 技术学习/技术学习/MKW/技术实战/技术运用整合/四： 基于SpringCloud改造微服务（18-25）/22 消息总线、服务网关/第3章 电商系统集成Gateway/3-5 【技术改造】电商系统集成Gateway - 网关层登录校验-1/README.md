---
title: 3-5 【技术改造】电商系统集成Gateway - 网关层登录校验-1
---

# 3-5 【技术改造】电商系统集成Gateway - 网关层登录校验-1

[image](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/e013d0ae-1f62-414a-beb3-429767b83e9e/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666V6JJLTQ%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T225751Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDvfCQltYCaWiS%2By405BbYTBSPBu3AOK2EYBMoWt1TRrwIhAL63fNjbT%2BV1g2%2BwHq6N%2BGz2zDElAiETEMfOHt5hKg1YKogECMb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgzJzu9kQwBPgct0%2Fx0q3APyU5bcrdS6nipyiLG3DLAZcCFJcfIcJ2nDLLG0Pj7HgovGXDqlAkQa0aWWQItgld7sevJ2JK9r8%2F8HKKaUn%2FtmXvejsHaTOGGUyEdDBIj2W88rC8Iowy4F6FWbWPJaeFGhGavqBEMFF8xYiViXjb5OYXdEEpnoIqetax%2FOlny3hBH4XjA6Un97Zk%2Fzvil7vLtxANtOpmXkkCbTWNplm5JIPVByf%2FcALMVMcmHJXKQU6CBUP8mbDMXHtccFtHT2GVPgGgI%2BPgm4fSeeLrPmuuhRaxTtU9O5ornlHTX1rZLwNhLjHmCLeA3oyuUy2tT5VACzQ8EFdddwniLznw%2B5LQt7OHowamygTsIsIu%2BAyJdtnInzxTv%2FrKFoyPWxyB%2BzcLy6ShVrLTqLcDTFaPy2BRoq5JygWHXPRUZPOMk0rvYFNQUCBe5DE%2Bv3SzRW%2B5LADIctZj1r2fujyuUY5Pw4XmbbK%2FprZV1d4NwIyNEAdN7cGvfcubpPRSwNoH2G%2B0wHoaCSyz8xfVlMdCIQ3xaMX0h7MwAYuzHnyyYwZHZEskwsAFYd271X3Oo1EwE4BWcw94AymLLMDcE0NXd%2BLFYDfNAmJuM1Q56UFl%2FrJxrejPtGpANlIW0GdpNq3sDU4jDYuv%2FSBjqkAYaoHc9Rdt3mMo%2FpQKAL8385K9fuhDr4cZNw1JrvG2GQIaV%2F4O%2FBU276qjkIX1l7K20R4gomzIVEFvSE7yfLKX1zV8X%2FGPIkIN3R2%2F%2Bl56Z%2B0G011TGtOlSbyqH%2FYhYI48gXHhVJn7qaRa9fEXdcVCJQEXnjehoy2CV803jsnM9DwbRNr09z0Sie7AxGXeIn6vWMRb8tvDhKpCFpWBJiSJHfi96b&X-Amz-Signature=5e7ede21f8548eda0bbadf4699ae4b724ae2fea976a80e51542a4bfa95c2f353&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

[image](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/b0d92d4d-f423-4abf-94d0-9d8c5429a8d6/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666V6JJLTQ%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T225751Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDvfCQltYCaWiS%2By405BbYTBSPBu3AOK2EYBMoWt1TRrwIhAL63fNjbT%2BV1g2%2BwHq6N%2BGz2zDElAiETEMfOHt5hKg1YKogECMb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgzJzu9kQwBPgct0%2Fx0q3APyU5bcrdS6nipyiLG3DLAZcCFJcfIcJ2nDLLG0Pj7HgovGXDqlAkQa0aWWQItgld7sevJ2JK9r8%2F8HKKaUn%2FtmXvejsHaTOGGUyEdDBIj2W88rC8Iowy4F6FWbWPJaeFGhGavqBEMFF8xYiViXjb5OYXdEEpnoIqetax%2FOlny3hBH4XjA6Un97Zk%2Fzvil7vLtxANtOpmXkkCbTWNplm5JIPVByf%2FcALMVMcmHJXKQU6CBUP8mbDMXHtccFtHT2GVPgGgI%2BPgm4fSeeLrPmuuhRaxTtU9O5ornlHTX1rZLwNhLjHmCLeA3oyuUy2tT5VACzQ8EFdddwniLznw%2B5LQt7OHowamygTsIsIu%2BAyJdtnInzxTv%2FrKFoyPWxyB%2BzcLy6ShVrLTqLcDTFaPy2BRoq5JygWHXPRUZPOMk0rvYFNQUCBe5DE%2Bv3SzRW%2B5LADIctZj1r2fujyuUY5Pw4XmbbK%2FprZV1d4NwIyNEAdN7cGvfcubpPRSwNoH2G%2B0wHoaCSyz8xfVlMdCIQ3xaMX0h7MwAYuzHnyyYwZHZEskwsAFYd271X3Oo1EwE4BWcw94AymLLMDcE0NXd%2BLFYDfNAmJuM1Q56UFl%2FrJxrejPtGpANlIW0GdpNq3sDU4jDYuv%2FSBjqkAYaoHc9Rdt3mMo%2FpQKAL8385K9fuhDr4cZNw1JrvG2GQIaV%2F4O%2FBU276qjkIX1l7K20R4gomzIVEFvSE7yfLKX1zV8X%2FGPIkIN3R2%2F%2Bl56Z%2B0G011TGtOlSbyqH%2FYhYI48gXHhVJn7qaRa9fEXdcVCJQEXnjehoy2CV803jsnM9DwbRNr09z0Sie7AxGXeIn6vWMRb8tvDhKpCFpWBJiSJHfi96b&X-Amz-Signature=eeb09f2932a9c1712f22f4839ba282c945e51ae4610a17b4c392a7c4f3a8b917&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

hello 我们课外的各位同学们，大家好，咱在这一节当中继续改造 gateway 组件，把前面我们创建的 gwt token 的功能集成到咱的网关层这里。那在集成之前，我们先来改一下 pump 文件，这里主要是要把 foodie off API 的依赖给它加入进去。那这一个步骤和之前的随堂 demo 是一样的。我们在添加了这个福地 auth API 依赖之后，要把其中的这个 spring boot starter web 这个依赖项把它给移除出去。原因就是咱的 gateway 是基于 web flux 的，它其实并不是基于 spring boot starter 所以要把这个依赖给它剔除掉。


那咱引入了 foodie off 依赖之后，我们走到启动类这里 gateway application 咱在它这上面加入一个 enable 分 client 的注解，在这里 enable 分 clients 然后咱把这个 base package class 早包的路径给它揪出来，把其中的这个叫 auth service 的 class 给它添加进去。


那咱把这个 of service 添加进来了以后，我们就要去创建一个 filter 那在这个 filter 当中，我们在调用 auth service 完成 gwt token 的校验。我们这里在 com.imock 下面创建了一个 filter 文件夹。在这个文件夹下面把咱之前在隋唐 demo 中写过的 auth filter 给它 copy 了进来。那这里面的内容和之前的随堂 demo 都是一模一样的，没有做什么改动。咱在这个 filter 里也是调用了 off service 的 verify 方法来验证你的 token 是不是一个有效 token 那这里我们就要把这个 filter 给它放到哪，放到咱的 roots configuration 里面。


那这里我们怎么来把它给加入进来呢？很简单，咱在这个 rules 的方法入参这里，直接把 auth filter 给它引用进来，那这也是一种侏儒病的方式，非常的简单。那在引入过来之后，剩下的我们就要去甄别你当前的服务，哪些服务是需要做用户登录校验的？那这里很简单，我只要生命一个新的路由，我用最简单的配置方式这里搞一个新的路由。那它路由匹配的规则是什么呢？是需要去做登录校验的特定的一些路由规则。比如说咱这个 address 目前所有发向 address 的请求都会被路由到 foodie service 那我这里有些发向 address 的请求，我希望怎么样呢？我希望让他经过登录校验，比如说 adjust list 我想让这个请求经过登录校验怎么办？那我就在这里这样配，把这个地址拎出来，然后在后面把 filter 加上这个 filter 我们这样来加，通过你这个入参引用来把它给加进来，好，直接这样来做一步就好了。


最后我需要把它发到哪呢？ URI 把它依然发送给 foodie user service 那这里如果还有其他的跟地址有关的路径，需要做登录校验的话，那很好办，我们通通把这些路径直接复制下来 copy 到这个列表当中就可以了。那与此同时，咱的用户唯一服务这里，你看目前来说，这四个地址当中，后面两个是不是也都需要做登录校验 user info 和 center 那它都是去更改当前用户的一些信息的地方。好我们把这几个 URL 这几个 mapping 也统统加到这里面去。
那同学们是不是发现我这里对同一个地址我配置了两套不同的路由规则，这样看起来是不是有那么点丑？那么麻烦对不对其实咱在网关层里面也有很多种的方式来配置你的登录校验的规则。那我这里用了一种比较直观，但是相对，写起来比较麻烦有点丑的方法。那同学们可以试试其他姿势。


那都有哪些姿势呢？第一个就是咱在前面的视频小结里面提到的最常用的方式咱在网关层当中，在咱的 auth filter 当中，为了去校验你的 token 我们还专门发了一个请求到 auth service 里面。对不对啊？那我们这第一个最常用的方法就是前面提到过的咱不用发送一个远程请求，咱在网关层自己用 key 来验证 gwt token 的有效性，甚至说我网关层当甩手掌柜，我什么都不管。有你的服务端来去决定哪些请求需要做登录校验这样的话其实相对来说更灵活。那如果你的服务端添加了一些新的接口，它需要登录校验，那我不用在网关层里面再更改配置，我只要在你自己的服务层，你把自己的登录校验给处理好就可以了，不用麻烦我的网关层。那这也是目前业界来说应用比较广泛也是相对推荐的一种方式。在这种方式下， of service 就单纯的成了一个签发 token 的服务。

```java
package com.imooc;

import com.imooc.filter.AuthFilter;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.beans.factory.annotation.Qualifier;
import org.springframework.cloud.gateway.filter.GatewayFilter;
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


    // 千万不要忘了加Bean注解，很多同学容易遗漏，
    // 然后问老师：我的路由规则为什么没生效
    @Bean
    public RouteLocator routes(RouteLocatorBuilder builder, AuthFilter authFilter) {
        return builder.routes()
                // Auth在网关层有很多种做法，我用了种最丑的，同学们可以试试其他姿势
                // 1) 【最常用】网关层或微服务自己本地校验jwt token有效性，不向auth-service发起远程调用
                // 2) 【路由配置最简单】可以把AuthFilter注册为global filter，
                //     然后在AuthFilter里配置需要过滤的url pattern(也可以从config-server动态拉取)
                // 3) 【路由配置也简单】也可以采用interceptor的形式
                // 4) 【路由配置最丑】这就是我选的路，只是为了演示下自定义过滤器，才走了这条不归路
                // 要注意声明URL Pattern的先后顺序，一个URL可能匹配多个路由，先来后到
                //
                // FIXME
                // 1) 将其他需要登录校验的地址添加在下面，或者采用上面提到的其他方案改造登录检测过程
                // 2) 修改前端JS代码，记得把login后返回的jwt-token和refresh-token带到每个请求的header里
                // 3) 前端JS依据header中的Authorization来判断是否登录
                .route(r -> r.path("/address/list",
                                                "/address/add",    // 需要做登录校验的都可以放在这里来
                                                "/address/update",
                                                "/address/setDefault",
                                                "/address/delete")

                        .filters(f -> f.filters(authFilter))

                        .uri("lb://FOODIE-USER-SERVICE")
                )

                //  FIXME 添加好这个（作业） search 服务自己实现掉
                .route(r -> r.path("/search/**", "/index/**", "/items/search","/items/catItems")
                        .uri("lb://FOODIE-SEARCH-SERVICE")
                )
                // 配置url pattern经常会漏掉某些字符导致转发出错，同学们发现视频里提到的那个导致错误的彩蛋了吗？
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


那除了这种方式，咱还能想到其他的方式吗？如果我还继续想在网关层使用 filter 这种机制来做登录校验，我有没有一种相对来说配置简单的方式当然有了，那我们可以采用什么呢？ auth filter 给他注册成为一个 global filter 这样一来的话，我的所有请求都会默认去经过这个 global filter 的一系列过滤，我就不用在路由规则这里单独指定某某需要经过我的 filter 不用了经过 global filter 来验证。


那同学们可能会想了，我并不是想要所有的地址都经过你 global filter 做登录校验的，咱还有有些地址不需要登录校验。怎么办呢？同学们顺着往下想，非常简单。如果我们把需要验证的地址全部配到你的 global filter 里，那我是不是就知道哪些 URL pattern 是需要做登录校验的啦，这样的话咱的路由表配置起来是不是就会简单很多了？那如果我们再结合前面学到的 config 组件，还能把这一招玩出一点花头。


怎么说，我可以把你需要过滤的 UR L pattern 怎么样呢？从 config server 配置中心这里把它动态拉取。如果你有新的登录校验的接口，需要添加进这个列表当中，我只要重新刷新一下这个属性列表就可以了。对不对？那相对于咱现在配置的静态路由，那以这种方式不仅写起来简单，而且也更加的灵活。那还有没有其他的方式啊？当然有咱前面在课程里也是不是在使用 intersector 拦截器的这种形式来做登录校验，那这里依然可以采用拦截器。
老师这里为什么采用 filter 呢？其实是单纯的为了给大家演示一下在网关层添加一个 filter 的步骤方式方法。所以我这里选用了 filter 的形式，那这种形式就是最后一种配置起来最丑的老师选择的道路。那你看，为了演示自定义过滤器，那老师走上了这条不归路。不过同学们在使用这种最丑的方式配置的时候要注意一个事情，这是很容易踩的坑。


那咱们大家看到你的一个地址请求，比如说 address AD 这一个地址请求过来，它能匹配到哪几个路由？第一个，这里声明的路由是不是能匹配到？那地址完全命中。那我们再往下看，这个 URL pattern 是不是也是完全匹配的？没错，那说它可以匹配到两个路由，那究竟哪个路由才会生效呢？我们这里要注意一下。
注意 URL pattern 它的声明的先后顺序。一个 uro 如果可以匹配多个路由的时候，咱遵循先来后到，那谁在前谁就先生效。那咱的路由配置就先说到这里。那还有很多其他的路径，他需要去加到登录校验的列表当中。那这个脏活累活苦活就留给同学们自己来做了。所以老师这里加上了一个 fix me 是要去让大家做什么内容呢？那就是将其他需要登录校验的地址把它添加到下面。但是注意不是让你通通添加到这个 user service 的转发路径当中。如果你的下单地址需要一个登录校验，那你这里要重新起一个路由，把这个下单地址添加进来。


那如果大家觉得这种方式非常丑，看起来也不方便，那可以怎么样呢？尝试采用我前面提到的这其他三种方式，把咱的登录检测过程给他做一番改造。在改造好之后，同学们要留意一个坑，什么坑呢？我们来看咱的 off filter 点进去看，你看他是从哪里去获取你的登录信息的，是从他的 HTTP 的 request header 当中对不对？那所以这里我们就必须要做一个必不可少的步骤是什么呢？那就是说我需要把你登录以后返回的这个 gwt token refresh token 还有这些 user ID 把它带到每一个请求的 header 里面。那这一步怎么来做那就需要大家去修改前端的 javascript 代码。那在你登录注册过后，我们的后台微服务会在你的 htd P 的 response header 里面把这些信息给它加入进去。那你要在 G S 里面把它捕捉到。捕捉到以后，你每次去发送请求的时候，就需要咱们把这个获取到的信息加到每一个新的服务请求的 header 当中。


那这一步同学们一定要记得自己动手做一下，老师就不带大家去做了。因为前端的 javascript 代码并不是我擅长的，这个说法有点牵强，准确的说是一点都不会，所以就要劳烦同学们自己动手了。那如果你跟老师一样也一点都不会java script 怎么办呢？很简单，直接把这一行给它注释掉，让这个登录检测不要起作用了就好了。 OK 那我们这里已经改完了路由配置表。


那接下来我们去动谁呢？我们这里提到过 logging 以后我们会返回 gwt token 还有 refresh token 对不对？所以接下来我们要到 passport controller 里面把这个 gwt token 和 refresh token 给它处理。


好。好，那我们现在转粘到 user 微服务，我们这里打开 user 微服务的文件夹。然后第一步咱先去找到它的 pom 文件，再要找到 pom 文件干什么呢？我们在它的最后一行 dependency 最后一个位置，把咱的 foodie auth API 把这个依赖给它加入进来。那加入好了之后，我们就要到它的启动类里面 user application 那给它这里加上一个分 client 注解。那为什么加它呢？因为我们要在登录服务当中去调用 auth API 来生成一个 token 所以这里需要通过分接口来发起调用。那等这两个地方添加好了以后，咱就可以去改造 ctrl 来了。那改造哪个 controller 呢？当然是 passport controller 好，那我们这次改造代码从上往下撸开始，从上往下一点点做。那这第一步我首先要引入一个依赖，引入一个谁的依赖呢？ off service 给它注入进来。好，我们给它起名也叫 of service auto wire 注解给它加上。那在这之下我还要声明三个变量，哪三个变量呢？同学们看名字。第一个 private static 然后给它声明成一个 final string 不带变的叫 auth header 它的值是 authorization 那接下来第二个变量我们给它起名字叫 refresh tokenheader 它的这个 header 上面我们把它改叫 refresh 杠。


OK 那接下来的第三个，同学们应该可以猜到它是 user ID 的 header 那我们把它起名叫 IMock 杠 user ID 那这三个就是定义了我在 header 当中存储的这个值，它叫什么名字，那它们这个值是和谁对应的呢？我们来看上面，在咱的 gateway 里面，我们刚才创建的这个 off filter 里，它是怎么来验证你的登录信息的？它是从你 header 里面拿值的对不对？ auth user ID 那我们存值的时候，我们在 header 当中的名称那要跟这里保持是一致的 authorization 和 IMock user ID 好，那我们再回到 passport 里面，那我们接下来就可以去改造方法了。


改造哪一个方法呢？首先来看 login 那 login 这里我们要把生成 token 的步骤放到哪里呢？就放到这里。那为什么选择在这里呢？你看，因为前面这一步是有实现登录，它已经验证了你的用户名和密码是匹配的。那自然而然接下来这一步就要去生成一个 token 了。那我们这里先来调用谁调用 of service 调用它的 tokenize 方法。这个方法需要传入一个 user ID 我们把前一步的这个 user result 给它拿到 get ID 把 user ID 传入进去。同时我这里使用一个 of response 把它的这个返回值给它，接下来返回值，我就给它起名叫 token 好了，那紧接着下一步我要加一个 if 判断。

[image](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/b702cd14-f9ac-4ba8-b8d4-b1583610a9b9/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666V6JJLTQ%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T225750Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDvfCQltYCaWiS%2By405BbYTBSPBu3AOK2EYBMoWt1TRrwIhAL63fNjbT%2BV1g2%2BwHq6N%2BGz2zDElAiETEMfOHt5hKg1YKogECMb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgzJzu9kQwBPgct0%2Fx0q3APyU5bcrdS6nipyiLG3DLAZcCFJcfIcJ2nDLLG0Pj7HgovGXDqlAkQa0aWWQItgld7sevJ2JK9r8%2F8HKKaUn%2FtmXvejsHaTOGGUyEdDBIj2W88rC8Iowy4F6FWbWPJaeFGhGavqBEMFF8xYiViXjb5OYXdEEpnoIqetax%2FOlny3hBH4XjA6Un97Zk%2Fzvil7vLtxANtOpmXkkCbTWNplm5JIPVByf%2FcALMVMcmHJXKQU6CBUP8mbDMXHtccFtHT2GVPgGgI%2BPgm4fSeeLrPmuuhRaxTtU9O5ornlHTX1rZLwNhLjHmCLeA3oyuUy2tT5VACzQ8EFdddwniLznw%2B5LQt7OHowamygTsIsIu%2BAyJdtnInzxTv%2FrKFoyPWxyB%2BzcLy6ShVrLTqLcDTFaPy2BRoq5JygWHXPRUZPOMk0rvYFNQUCBe5DE%2Bv3SzRW%2B5LADIctZj1r2fujyuUY5Pw4XmbbK%2FprZV1d4NwIyNEAdN7cGvfcubpPRSwNoH2G%2B0wHoaCSyz8xfVlMdCIQ3xaMX0h7MwAYuzHnyyYwZHZEskwsAFYd271X3Oo1EwE4BWcw94AymLLMDcE0NXd%2BLFYDfNAmJuM1Q56UFl%2FrJxrejPtGpANlIW0GdpNq3sDU4jDYuv%2FSBjqkAYaoHc9Rdt3mMo%2FpQKAL8385K9fuhDr4cZNw1JrvG2GQIaV%2F4O%2FBU276qjkIX1l7K20R4gomzIVEFvSE7yfLKX1zV8X%2FGPIkIN3R2%2F%2Bl56Z%2B0G011TGtOlSbyqH%2FYhYI48gXHhVJn7qaRa9fEXdcVCJQEXnjehoy2CV803jsnM9DwbRNr09z0Sie7AxGXeIn6vWMRb8tvDhKpCFpWBJiSJHfi96b&X-Amz-Signature=122600b073944902c8a76adcb688d8825e97f097b4ebd631432d0d96f042e5c9&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

那同学们还记得，它这个返回值当中有一个什么呢？有一个 status code 那这个 status code 如果它怎么样呢？它不是 success 那这种情况下说明什么呢？说明我的 token 没有生成成功。所以我就要把这整个登录请求给它做失败处理。


那我们这里加一个判断，如果我的这个 token 所拿到的 code 不等于 success 那也就是等于失败怎么办？那等于失败，我就直接给他 return 一个最终返回到 UI 的一个值，这个值我从下面直接 copy 一下，也返回给他这样一个 error 但是我起的 error 的信息我就给它叫 token error 好了，那在返回之前保留一个好习惯，我们先要打一行 L 级别的日志 log 因为我们在线上的时候你排查错误，都是依赖于这些点点滴滴的 log 所以我们平时养成好习惯，碰到一些核心路径，核心判断 if 条件，别忘了在这边打一些 log 那我这个 log 就叫 token error 并且我要保留一个证据，把 UID 是哪个用户发现的 error 把它给打印出来，这里把 UID 添加到 log 里面。那我们拿到 token 之后，就接下来往下走了，我下一步需要做什么呢？那就是要将 token 添加到 header 当中。那这里我新起一个方法，我走到下面，走走滚到最底下。


好。到最底下之后，我这里声明一个 private 方法，那他什么都不返回，空手套白狼 void 给它起名就叫 add off to header 那他接收什么呢？如果我要给一个服务请求返回一个 a header 那怎么办呢？我要把它加到 HD DP server let response 里面。那它第一个参数就接收的是这样一个 response 第二个参数是谁呢？是我们刚刚生成的这个 account token 我接下来要往里面加参数了在 response stead header 第一个 header 我们把这个 off header 跑哪去了？在这 off header 给它塞进去，这里就直接从 token 里面 get token 很简单，那咱就依葫芦画瓢把这里三个请求都给它塞进去。

[image](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/e9957116-f0d7-495b-bad6-210593e8e730/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666V6JJLTQ%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T225750Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDvfCQltYCaWiS%2By405BbYTBSPBu3AOK2EYBMoWt1TRrwIhAL63fNjbT%2BV1g2%2BwHq6N%2BGz2zDElAiETEMfOHt5hKg1YKogECMb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgzJzu9kQwBPgct0%2Fx0q3APyU5bcrdS6nipyiLG3DLAZcCFJcfIcJ2nDLLG0Pj7HgovGXDqlAkQa0aWWQItgld7sevJ2JK9r8%2F8HKKaUn%2FtmXvejsHaTOGGUyEdDBIj2W88rC8Iowy4F6FWbWPJaeFGhGavqBEMFF8xYiViXjb5OYXdEEpnoIqetax%2FOlny3hBH4XjA6Un97Zk%2Fzvil7vLtxANtOpmXkkCbTWNplm5JIPVByf%2FcALMVMcmHJXKQU6CBUP8mbDMXHtccFtHT2GVPgGgI%2BPgm4fSeeLrPmuuhRaxTtU9O5ornlHTX1rZLwNhLjHmCLeA3oyuUy2tT5VACzQ8EFdddwniLznw%2B5LQt7OHowamygTsIsIu%2BAyJdtnInzxTv%2FrKFoyPWxyB%2BzcLy6ShVrLTqLcDTFaPy2BRoq5JygWHXPRUZPOMk0rvYFNQUCBe5DE%2Bv3SzRW%2B5LADIctZj1r2fujyuUY5Pw4XmbbK%2FprZV1d4NwIyNEAdN7cGvfcubpPRSwNoH2G%2B0wHoaCSyz8xfVlMdCIQ3xaMX0h7MwAYuzHnyyYwZHZEskwsAFYd271X3Oo1EwE4BWcw94AymLLMDcE0NXd%2BLFYDfNAmJuM1Q56UFl%2FrJxrejPtGpANlIW0GdpNq3sDU4jDYuv%2FSBjqkAYaoHc9Rdt3mMo%2FpQKAL8385K9fuhDr4cZNw1JrvG2GQIaV%2F4O%2FBU276qjkIX1l7K20R4gomzIVEFvSE7yfLKX1zV8X%2FGPIkIN3R2%2F%2Bl56Z%2B0G011TGtOlSbyqH%2FYhYI48gXHhVJn7qaRa9fEXdcVCJQEXnjehoy2CV803jsnM9DwbRNr09z0Sie7AxGXeIn6vWMRb8tvDhKpCFpWBJiSJHfi96b&X-Amz-Signature=64996bc99c73857a8b2f778f18c6f890a096da94e4507014919f6ea437d4715a&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)


那第二个轮到谁了？ I refresh took 那是从这个 token 对象当中 get refresh token 第三个是谁？是 UID 那就是用户的 user ID 得到。那这里老师再提醒大家一下，要记得修改前端的加 script 代码。那拿到了 authorization refresh token 还有 user ID 之后，记得把它在前端缓存下来，每次服务的时候要把这些请求参数给它带上。

[image](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/49f02b3d-1e63-4fea-bbda-eab3a0922c1d/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666V6JJLTQ%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T225751Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDvfCQltYCaWiS%2By405BbYTBSPBu3AOK2EYBMoWt1TRrwIhAL63fNjbT%2BV1g2%2BwHq6N%2BGz2zDElAiETEMfOHt5hKg1YKogECMb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgzJzu9kQwBPgct0%2Fx0q3APyU5bcrdS6nipyiLG3DLAZcCFJcfIcJ2nDLLG0Pj7HgovGXDqlAkQa0aWWQItgld7sevJ2JK9r8%2F8HKKaUn%2FtmXvejsHaTOGGUyEdDBIj2W88rC8Iowy4F6FWbWPJaeFGhGavqBEMFF8xYiViXjb5OYXdEEpnoIqetax%2FOlny3hBH4XjA6Un97Zk%2Fzvil7vLtxANtOpmXkkCbTWNplm5JIPVByf%2FcALMVMcmHJXKQU6CBUP8mbDMXHtccFtHT2GVPgGgI%2BPgm4fSeeLrPmuuhRaxTtU9O5ornlHTX1rZLwNhLjHmCLeA3oyuUy2tT5VACzQ8EFdddwniLznw%2B5LQt7OHowamygTsIsIu%2BAyJdtnInzxTv%2FrKFoyPWxyB%2BzcLy6ShVrLTqLcDTFaPy2BRoq5JygWHXPRUZPOMk0rvYFNQUCBe5DE%2Bv3SzRW%2B5LADIctZj1r2fujyuUY5Pw4XmbbK%2FprZV1d4NwIyNEAdN7cGvfcubpPRSwNoH2G%2B0wHoaCSyz8xfVlMdCIQ3xaMX0h7MwAYuzHnyyYwZHZEskwsAFYd271X3Oo1EwE4BWcw94AymLLMDcE0NXd%2BLFYDfNAmJuM1Q56UFl%2FrJxrejPtGpANlIW0GdpNq3sDU4jDYuv%2FSBjqkAYaoHc9Rdt3mMo%2FpQKAL8385K9fuhDr4cZNw1JrvG2GQIaV%2F4O%2FBU276qjkIX1l7K20R4gomzIVEFvSE7yfLKX1zV8X%2FGPIkIN3R2%2F%2Bl56Z%2B0G011TGtOlSbyqH%2FYhYI48gXHhVJn7qaRa9fEXdcVCJQEXnjehoy2CV803jsnM9DwbRNr09z0Sie7AxGXeIn6vWMRb8tvDhKpCFpWBJiSJHfi96b&X-Amz-Signature=03e261c44972e666cc8b65c4b496d00e326ebd223af17db7800a87dad6ce9b0c&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

那同学们还记得咱为什么需要一个 refresh token 吗？因为咱在生成这个 auth token 的时候，有一个过期时间还记得没有在 auth service 当中。那如果忘记的同学，我们可以快速的回顾一下 off service 那这 auth service 里面生成的 token nice 方法在这里。


gwt service 我们在生成的时候，看到这里有两个时间，一个是 now 什么时候生成的？另一个是 expire at 在什么时间过期？那因此它

这过期时间很关键。那如果你这个 token 已经过期了，那在下面的 verify 这个方法当中，那它会返回一个失败。所以我们希望让前端怎么样，让前端知道他的过期时间，做到心中有数。那他怎么才能知道过期时间非常简单，我这个 calendar 我给他生成一个叫 expiration time 这里用 calendar 的 get instance 方法。然后把它怎么样把它给加上一天的时间。


