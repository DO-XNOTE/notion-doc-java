---
title: 1-18 哨兵SpringAOP注解方式应用-3
---

# 1-18 哨兵SpringAOP注解方式应用-3

[image](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/d9a0d4d3-1ea0-4672-91df-e3087c35cdde/SCR-20240722-sgwr.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TJKC3JJ7%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T225838Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIDnzsX%2FlB%2BFwkYwtC03i7M%2FwDwH7mlF9FwGlcAUXAZDSAiA8fsVCJwhudReNvORCwGR%2FzEo18KNYNXStqSa72wkCNSqIBAjG%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMuwev504HQKIH8gkmKtwDdbig6ums7ogaFXwt41RmxexLDT0NVsMGcz8FmZxZiPYq7jIeNEHEs4juqLiXMl2A%2BiNexoGfRZzL%2FxVOtGYZTiBftWDDkgKeEyZGiKhn2flT3jGa%2FGoiBTkia8i7GGj8KodlBTWxcEZOzRJqGtWfa4wigZWQTQ7jNgzVfAOdKQb%2FboVuX54tOlgfffwwZDIHOOKILM9TKCbnyTXHfGdISViuB%2Ba4LxSMZA1hENzJJ%2FyGE%2FhIFRqc6zpgeNrDUAQQYjA%2B4fUZOx6d2bpPJhfp8PbBw70%2Bsa2Mm3eTzMfWM%2BC5%2BocTLjdZCmVNi7GLU98dmrUW1tAW0zNeXYdHxYGhIyIfgZXrb%2FoqBENnu93gCc%2BUwxDUfF0HFsDFYrq0o8Bq9aWq7KcVA6f1cniebIg0H0S9ojAIvuS2aAjBEX0T%2BFAQxkg48TINSMyeOQqu7cO5hea%2BL3G1%2BUKeP3%2Bz5lk8hb05ShISG12QTBCnqWst6X8qdzoR%2FhxisiqF3%2BRZqMlr%2FOaSkX0C9PLeSe2cSYDn8CzQxCb8ZFfgU%2BjXdBz8vwRcx4gJ4vqfypem0lla%2F3lmKxJfjv%2BiIk6d8mvdECSzuRAHySRh2nolwMF52O0XxZWY8%2BY6Qy743uKXjDgwmbf%2F0gY6pgFVdBXr5qMoF5i4SdNg%2FmeTXsa37zLMLXFXOvNNrgYvuNb8GcaBmLL4bBeWudV48RA55avIHNSu4E1RJYfH4ZBhosP6Uu00WvZoDUlGbze%2BOlDlKfjB8XPMbXMiba80334cRpeJ06EUlaDN6AFYOC0oYDWZFxkx6qPP%2BmjASDpCO9wKM%2F3cP0GKQ04O1pTPyAtx9HHj8MR%2B4CHqaDxsH48raQ9QKch6&X-Amz-Signature=56659b4a62d30965fd63a324a3d2e641f36749e195a770ff30ad8409efb537ee&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

[image](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/6c41bdaf-c814-409c-9687-260eb2b3027d/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TJKC3JJ7%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T225838Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIDnzsX%2FlB%2BFwkYwtC03i7M%2FwDwH7mlF9FwGlcAUXAZDSAiA8fsVCJwhudReNvORCwGR%2FzEo18KNYNXStqSa72wkCNSqIBAjG%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMuwev504HQKIH8gkmKtwDdbig6ums7ogaFXwt41RmxexLDT0NVsMGcz8FmZxZiPYq7jIeNEHEs4juqLiXMl2A%2BiNexoGfRZzL%2FxVOtGYZTiBftWDDkgKeEyZGiKhn2flT3jGa%2FGoiBTkia8i7GGj8KodlBTWxcEZOzRJqGtWfa4wigZWQTQ7jNgzVfAOdKQb%2FboVuX54tOlgfffwwZDIHOOKILM9TKCbnyTXHfGdISViuB%2Ba4LxSMZA1hENzJJ%2FyGE%2FhIFRqc6zpgeNrDUAQQYjA%2B4fUZOx6d2bpPJhfp8PbBw70%2Bsa2Mm3eTzMfWM%2BC5%2BocTLjdZCmVNi7GLU98dmrUW1tAW0zNeXYdHxYGhIyIfgZXrb%2FoqBENnu93gCc%2BUwxDUfF0HFsDFYrq0o8Bq9aWq7KcVA6f1cniebIg0H0S9ojAIvuS2aAjBEX0T%2BFAQxkg48TINSMyeOQqu7cO5hea%2BL3G1%2BUKeP3%2Bz5lk8hb05ShISG12QTBCnqWst6X8qdzoR%2FhxisiqF3%2BRZqMlr%2FOaSkX0C9PLeSe2cSYDn8CzQxCb8ZFfgU%2BjXdBz8vwRcx4gJ4vqfypem0lla%2F3lmKxJfjv%2BiIk6d8mvdECSzuRAHySRh2nolwMF52O0XxZWY8%2BY6Qy743uKXjDgwmbf%2F0gY6pgFVdBXr5qMoF5i4SdNg%2FmeTXsa37zLMLXFXOvNNrgYvuNb8GcaBmLL4bBeWudV48RA55avIHNSu4E1RJYfH4ZBhosP6Uu00WvZoDUlGbze%2BOlDlKfjB8XPMbXMiba80334cRpeJ06EUlaDN6AFYOC0oYDWZFxkx6qPP%2BmjASDpCO9wKM%2F3cP0GKQ04O1pTPyAtx9HHj8MR%2B4CHqaDxsH48raQ9QKch6&X-Amz-Signature=6bd44c8cd9d733889c61d9c2a31bde5260152bb158d821d0e72aab3c0f927471&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

对于这个流控的这块，就是对于这个 follow follow service 这块已经讲完了。那接下来我们看一看刚才我们上节课最后说的这个 bellback 这个 fail back 其实是很有意思的，我们一起来做一个小实验，来说明一下这个 fail back 应该怎么去用。


好了。那现在我们这里边有一个 follow service 那我们再 new 一个新的 service 咱们叫做 degree service 。有了这个 degree 的 service 然后我们来看一看这它们两个函数同时存在的时候，它有什么区别。首先在这里边艾特 service 是必须要有的。然后老师把之前的 follow service 代码我粘过来，当然我要稍微改一改。 OK 现在我们它的这个权限命名这改一下对不对？这会应该叫做什么呢？应该叫做 degree 的 service 然后这个方法我们也改一下这个 degree degree OK 那这个方法它的冒号后面就是加一个 degree 的。然后其他的那这块我们叫做 degree 的 lock 看到了。然后这个我们叫做 degree 的 fail back 这有一个区别，这个大写。 Ok. 好了，基本上我们已经把代码写完了，这一块我们写正常执行 degree 的方法。这个返回比如说叫做就返回一个 degree 的表示正常的时候是这样的。然后如果抛异常的时候怎么去做呢？注意这里边 degree 的 block handler 处理的是处罚降级流控策略对不对？然后在这里边我说执行降级流控。然后这个方法是什么呢？其实我们刚才已经把注解写完了，我们把这个注解再拿过来，咱们再看一看是不是流控。什么叫做流控？其实无论是降级还是说流量控制都叫做流控，看你流控策略怎么去配。


那我们现在再写一个新的方法，这个方法我们叫做什么呢？我们叫做 degree 的 fail back 然后这个 degree 的 fail back 它跟的参数应该是什么呢？这个它只是处理抛出异常的时候进行兜底。所以说我们在这里你可以写一个 slope T 然后把这个 slogan 打印一下。然后这个就是什么触发异常时的降级策略明白了吧，那这个就是执行异常降级法。


好了，现在我们这个代码写完了，那我们来看一看怎么去做一个测试。比如说我们在这里用一个比较简单的变量 private 咱们是 atomic integer count 对于 new 一个 atomic integer 然后默认值给他一个理由，在这里面我们做一个小判断，比如说第二咱们叫做 get 或者是 increment and get 就先自增，然后再去获取自增后的结果。
如果取于 3 等于 0 的话，那我们比如说抛出一个异常，那在这里我想抛出一个 run time X 就可以了。之前我们自己去做那个手工去写的时候，就是你想去看到结果就比较费劲。但是现在就是你手工的去调价位 API 去写比较费劲。但是如果现在你用这种注解的方式，你想去看到这个效果是非常容易的。


叫做抛出业务异常，我就简单这么去写。如果说我的 count 每次都加加对不对？每次都加。如果取 3.0 的时候就抛出这个也有异常。然后如果取 3 不等于0，比如说 1247 这种，那我就直接 return 正常的逻辑就执行正常逻辑，它就会返回这个位置对吧。


当然这里边只要抛出了这个业务异常，他就会走到哪，他就会走到这里面，就是 degree 的 fell by 那什么时候流控呢？根据，你的规则处罚了，他才会到这个第 great block handler 里面。在这里我希望小伙伴们应该明白这一点。

```java
package com.bfxy.test.service;

import com.alibaba.csp.sentinel.EntryType;
import com.alibaba.csp.sentinel.annotation.SentinelResource;
import org.springframework.stereotype.Service;
import org.springframework.web.bind.annotation.RequestMapping;

import java.util.concurrent.atomic.AtomicInteger;

/**
 * <h1></h1>
 */
@Service
public class DegradeService {

    private AtomicInteger count = new AtomicInteger(0);

    @SentinelResource(
            value = "com.bfxy.test.service.DegradeService:degrade",
            entryType = EntryType.OUT,
            blockHandler = "degradeBlockHandler",
            fallback = "degradeFallback"
    )
    @RequestMapping("/degrade")
    public String degrade() {

        if (count.incrementAndGet() % 3 ==0) {
            throw  new RuntimeException("抛出业务异常");
        }

        System.out.println("--------正常执行 degrade 方法");
        return "degrade";
    }

    public String degradeBlockHandler() {
        System.out.println("-------------执行degradeBlockHandler");
        return "执行degradeBlockHandler";
    }

    public String degradeFallback(Throwable ex) {
        System.out.println("----------执行降级流控方法degradeFallback" + ex);
        return "执行降级流控方法degradeFallback";
    }
}
```


OK 那现在我们这个 service 搞定了，那我们接下来就是通过controller ，我们把 service 写一写，现在我们先 all to where 的，我们要自动去注入我们刚才所写的这个 degree 的 service 然后这个 degree 的 service 有了之后，我们把它 copy 一下，这里边叫 degree 的 test 对吧，degree的都改一下叫 degree test 这叫 degree 的 service.degree 的好代码已经写完了，那我们现在马上去来做一下小的测试。 OK 现在我们的 dashboard 其实还是起着的，所以说我直接把这个 test 启动起来就好了。我直接右键 run at 我们的 sprint bot application OK 已经启动起来了。启动起来以后，那我们接下来做的事情很简单，我们就直接点到控制台。点到控制台之后，我们首先还是要访问一下 HTTP 冒号杠杠 input host 8001。然后是 degree 的对吧，我们直接 A 访问 degree 的了，看见了吧。

[image](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/c19a3f8d-2737-40f7-aafa-f406991de678/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TJKC3JJ7%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T225838Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIDnzsX%2FlB%2BFwkYwtC03i7M%2FwDwH7mlF9FwGlcAUXAZDSAiA8fsVCJwhudReNvORCwGR%2FzEo18KNYNXStqSa72wkCNSqIBAjG%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMuwev504HQKIH8gkmKtwDdbig6ums7ogaFXwt41RmxexLDT0NVsMGcz8FmZxZiPYq7jIeNEHEs4juqLiXMl2A%2BiNexoGfRZzL%2FxVOtGYZTiBftWDDkgKeEyZGiKhn2flT3jGa%2FGoiBTkia8i7GGj8KodlBTWxcEZOzRJqGtWfa4wigZWQTQ7jNgzVfAOdKQb%2FboVuX54tOlgfffwwZDIHOOKILM9TKCbnyTXHfGdISViuB%2Ba4LxSMZA1hENzJJ%2FyGE%2FhIFRqc6zpgeNrDUAQQYjA%2B4fUZOx6d2bpPJhfp8PbBw70%2Bsa2Mm3eTzMfWM%2BC5%2BocTLjdZCmVNi7GLU98dmrUW1tAW0zNeXYdHxYGhIyIfgZXrb%2FoqBENnu93gCc%2BUwxDUfF0HFsDFYrq0o8Bq9aWq7KcVA6f1cniebIg0H0S9ojAIvuS2aAjBEX0T%2BFAQxkg48TINSMyeOQqu7cO5hea%2BL3G1%2BUKeP3%2Bz5lk8hb05ShISG12QTBCnqWst6X8qdzoR%2FhxisiqF3%2BRZqMlr%2FOaSkX0C9PLeSe2cSYDn8CzQxCb8ZFfgU%2BjXdBz8vwRcx4gJ4vqfypem0lla%2F3lmKxJfjv%2BiIk6d8mvdECSzuRAHySRh2nolwMF52O0XxZWY8%2BY6Qy743uKXjDgwmbf%2F0gY6pgFVdBXr5qMoF5i4SdNg%2FmeTXsa37zLMLXFXOvNNrgYvuNb8GcaBmLL4bBeWudV48RA55avIHNSu4E1RJYfH4ZBhosP6Uu00WvZoDUlGbze%2BOlDlKfjB8XPMbXMiba80334cRpeJ06EUlaDN6AFYOC0oYDWZFxkx6qPP%2BmjASDpCO9wKM%2F3cP0GKQ04O1pTPyAtx9HHj8MR%2B4CHqaDxsH48raQ9QKch6&X-Amz-Signature=206789006b84b3f8b3e75955f4861beb655373e3d2496d426701d4ce7cb1bfad&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

[image](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/efee48b4-40d0-4627-b1a0-7d58b7f593e2/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TJKC3JJ7%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T225838Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIDnzsX%2FlB%2BFwkYwtC03i7M%2FwDwH7mlF9FwGlcAUXAZDSAiA8fsVCJwhudReNvORCwGR%2FzEo18KNYNXStqSa72wkCNSqIBAjG%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMuwev504HQKIH8gkmKtwDdbig6ums7ogaFXwt41RmxexLDT0NVsMGcz8FmZxZiPYq7jIeNEHEs4juqLiXMl2A%2BiNexoGfRZzL%2FxVOtGYZTiBftWDDkgKeEyZGiKhn2flT3jGa%2FGoiBTkia8i7GGj8KodlBTWxcEZOzRJqGtWfa4wigZWQTQ7jNgzVfAOdKQb%2FboVuX54tOlgfffwwZDIHOOKILM9TKCbnyTXHfGdISViuB%2Ba4LxSMZA1hENzJJ%2FyGE%2FhIFRqc6zpgeNrDUAQQYjA%2B4fUZOx6d2bpPJhfp8PbBw70%2Bsa2Mm3eTzMfWM%2BC5%2BocTLjdZCmVNi7GLU98dmrUW1tAW0zNeXYdHxYGhIyIfgZXrb%2FoqBENnu93gCc%2BUwxDUfF0HFsDFYrq0o8Bq9aWq7KcVA6f1cniebIg0H0S9ojAIvuS2aAjBEX0T%2BFAQxkg48TINSMyeOQqu7cO5hea%2BL3G1%2BUKeP3%2Bz5lk8hb05ShISG12QTBCnqWst6X8qdzoR%2FhxisiqF3%2BRZqMlr%2FOaSkX0C9PLeSe2cSYDn8CzQxCb8ZFfgU%2BjXdBz8vwRcx4gJ4vqfypem0lla%2F3lmKxJfjv%2BiIk6d8mvdECSzuRAHySRh2nolwMF52O0XxZWY8%2BY6Qy743uKXjDgwmbf%2F0gY6pgFVdBXr5qMoF5i4SdNg%2FmeTXsa37zLMLXFXOvNNrgYvuNb8GcaBmLL4bBeWudV48RA55avIHNSu4E1RJYfH4ZBhosP6Uu00WvZoDUlGbze%2BOlDlKfjB8XPMbXMiba80334cRpeJ06EUlaDN6AFYOC0oYDWZFxkx6qPP%2BmjASDpCO9wKM%2F3cP0GKQ04O1pTPyAtx9HHj8MR%2B4CHqaDxsH48raQ9QKch6&X-Amz-Signature=d7d2a9ac608637f3110cb2c281706d3b4b1f89e3bfb9080ddb350b80b4cd4b30&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

首先我们这怎么是 web 的 index controller degree 的这个为什么是以 desk 做到的呢？看一下对应的代码我们刚才加了这个 degrees 因为它应该是这个名字，它应该叫 degrees service 对不对？在这里边这个是全命名的。 sorry 它叫 degree test 说的我是想要去做这个事情叫 degree 的 test 没错。


好，这回访问的 degree 的我们再来刷一下，我们要的是哪个资源？我们要的是这个资源，这个资源才是我们的 degree 的 service 的 degree 这个方法好了，那我现在给他做一个流控的策略，比如说给他做一个流控也好，降级也好都可以。比如说我们先来一个降级，降级我们设置异常数，比如说一秒钟之内，如果你触发了 10 次，就是说你的异常数一旦是一秒钟之内触发了 10 次，怎么办？就是帮你去做降级的流控。那么加上这个 OK 好了，现在我们的降级策略有了，就是对应的这个资源说每一秒钟如果异常数大于 10 次，那我就去做降级的入控。


降级的流控会处罚哪个呢？在这里我们来看一下在哪降级。如果处罚降级的流控了，那他很无喜，他会帮我们去调用对应的这个 degree 的 block 这是向处罚降级之后的进行流控的手办。但是这个什么？抛异常这种方式，就是说我们 sell back handler 它只要抛出异常的时候就会进入这个动力函数。对不对？就这块看见了吗？好，我们刚才刷了一次它可能等不等于3，我们再多刷几次，我们在这里，我在 f5 刷新，在 f5 刷新，看执行异常的降级方法看见了吗？我们再刷一次，这是第四次，再刷一次就是第五次对不对？我再刷一次，第六次看到了。执行异常的降级方法，你看我们再刷一次是第七次，再刷一次，第八次再刷一次，第九次看见了。


执行异常的研发，我不知道小伙伴们到底看没看清楚我们的操作。那也就是说我们正常逻辑是什么呢？如果取于 3 等于 0 的话会抛出异常。但是抛出这种异常跟流控一毛钱关系没有，她都会去走到抛出异常的兜底策略，就是出现异常出现问题了，就是我这个方法执行只要剖一场就会走这个 feel back 那没有说意思吗？这是一个最简单的机制，每三次你看我这里边都是，掉三次取 3 等于 0 的时候就会触发业务异常，抛出业务异常。


那处罚哪个呢？处罚异常时的降级策略，然后把这个 run time session 打印出来抛出业务异常对吧？Ok.那什么情况下会触发这种流控的？怎么降级流控的策略呢？很简单，就是刚才你配的那块，我刚才怎么配的？我还配的说一秒钟之内，如果说异常数大于 10 次，那么就会触发流控。那我们来做一下测试。这是一次两次三次，我把这个快点刷，快点刷，我看看能不能刷出来，看见了吗？执行降级流控方法，我再刷，这回他刷的都是执行降级的流控方法。同学们一起看我刷了多少次，这回他就不走。


处罚异常的时候那个 feel back 看到了，这是处罚什么了？处罚降级的流控策略。那也就是说这一回他真正去到了我们的 block handler 里。因为什么呢？因为我的流控的策略已经触发了，就是说一秒钟之内你触发了 10 次以上的异常，抛出了 10 次以上的异常，那我就走这个逻辑了能理解我说意思吗？但是说每次抛异常的时候正常进行，最好的代价我都会走 fail back 好，所以说这个小伙伴们一定要注意这个就是他们实际的区别。


我再刷一次，你看又回来了，帝国瑞的是不是再来帝国瑞的还是再来，是不是执行异常降级？再刷一次，每三次都会执行降级异常。然后我多刷几次，高一点，频率高一点以后看就执行降级了。对不对？其实你可以数一下这个业务异常一共处罚了多少次。这是一次两次，3次，4次，5次，6次 7 次 8 次 9 次 10 次对吧，已经处罚了 10 次这个异常了在 1 秒钟之内她就直接就帮你去不再去走这个抛出业务异常时的 fail back 而是直接走 block handler 就直接降级了。

[image](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/ae8efd9e-22f5-4091-856f-a9b315a803b3/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TJKC3JJ7%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T225838Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIDnzsX%2FlB%2BFwkYwtC03i7M%2FwDwH7mlF9FwGlcAUXAZDSAiA8fsVCJwhudReNvORCwGR%2FzEo18KNYNXStqSa72wkCNSqIBAjG%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMuwev504HQKIH8gkmKtwDdbig6ums7ogaFXwt41RmxexLDT0NVsMGcz8FmZxZiPYq7jIeNEHEs4juqLiXMl2A%2BiNexoGfRZzL%2FxVOtGYZTiBftWDDkgKeEyZGiKhn2flT3jGa%2FGoiBTkia8i7GGj8KodlBTWxcEZOzRJqGtWfa4wigZWQTQ7jNgzVfAOdKQb%2FboVuX54tOlgfffwwZDIHOOKILM9TKCbnyTXHfGdISViuB%2Ba4LxSMZA1hENzJJ%2FyGE%2FhIFRqc6zpgeNrDUAQQYjA%2B4fUZOx6d2bpPJhfp8PbBw70%2Bsa2Mm3eTzMfWM%2BC5%2BocTLjdZCmVNi7GLU98dmrUW1tAW0zNeXYdHxYGhIyIfgZXrb%2FoqBENnu93gCc%2BUwxDUfF0HFsDFYrq0o8Bq9aWq7KcVA6f1cniebIg0H0S9ojAIvuS2aAjBEX0T%2BFAQxkg48TINSMyeOQqu7cO5hea%2BL3G1%2BUKeP3%2Bz5lk8hb05ShISG12QTBCnqWst6X8qdzoR%2FhxisiqF3%2BRZqMlr%2FOaSkX0C9PLeSe2cSYDn8CzQxCb8ZFfgU%2BjXdBz8vwRcx4gJ4vqfypem0lla%2F3lmKxJfjv%2BiIk6d8mvdECSzuRAHySRh2nolwMF52O0XxZWY8%2BY6Qy743uKXjDgwmbf%2F0gY6pgFVdBXr5qMoF5i4SdNg%2FmeTXsa37zLMLXFXOvNNrgYvuNb8GcaBmLL4bBeWudV48RA55avIHNSu4E1RJYfH4ZBhosP6Uu00WvZoDUlGbze%2BOlDlKfjB8XPMbXMiba80334cRpeJ06EUlaDN6AFYOC0oYDWZFxkx6qPP%2BmjASDpCO9wKM%2F3cP0GKQ04O1pTPyAtx9HHj8MR%2B4CHqaDxsH48raQ9QKch6&X-Amz-Signature=17f8466cc6771db25ffd923767b72abee15d415aca01cc1cd66016aff59f66c8&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

Ok.那其实这种场景什么时候需要去用呢？比如说我们正常的访问请求的时候，一般来讲你偶尔网络闪断是正常的。那这个时候我们去做一个兜底，我们就处罚什么呢？ bellback 就可以 fell back 我们处罚一个兜底策略，比如说给他一个默认的产出值或者调一个函数都可以。但是当大流量过来的时候，那我们可能就不能够再去调用这个 feel back 了，因为你调 fire bike 全都是失败的。那干脆我给出另外一种解决方案，就是流控降级。 OK 这个跟 follow control 里边的这个 block handler 里面是一致的。所以说他们两个同时存在的时候，具体的区别就在于这。好了，我再刷一次它肯定还是正常的，再刷一次，正常的你看就逐渐降级。


好了，那这个就是区别整个它的核心的应用，希望小伙伴们一定要特殊的去注意。当然刚才你点了这么多东西，那对应的你可以看实时监控看见了吧，你可以看到他拒绝的次数在一分钟之内就到了很多次了。蓝色的表示拒绝，绿色的表示通过。当然这个整个 dashboard 控制台它是怎么去作用的？其实小伙伴们你可以去看一下中英的这个它的输出能输出在哪里呢？在我们的用户下面的logs ，然后有一个 CSP 然后我们看这是老师今天可能有好多好多，我们找这个时间最前面的就是48，看 demo test 有没有 match 对吧，看这个就好，这也是这 47 分的。


看这个就是你想要的吗？我处罚 grade 了是不是，每分钟通过多少次？然后拒绝多少次？你这里边的一些参数到底是什么意思？这都是 degree 的这个资源所对应的。这是当然这个每一个参数可能是总请求数，通过的，拒绝的，然后这个 rt 响应时间，然后其他的东西。当然你说老师这个我忘了他那个参数代表什么含义。很简单，你就去那个 demo 里面去找 demo 里边都会有对不对？就新手指南里边它里面都会有，就是对应着每一个输出的它用竖线分割的，每一个竖线分割所对应的那个值代表什么含义都有，然后你自己去对照，慢慢的结合着去学习，你基本上就没问题了。


好了，我就不领着小伙伴们再去看了。形容自然下面就在这是不是代表什么含义，这里面都有说明。就最开始 P 表示通过的请求数， S 表示 block 被阻塞的请求数，然后这个 E 就表示代表这个自定异常，然后 R T 表示平均响应时间。那这个倒数第二代表异常了呗，看一下倒数第二它就有异常了对吧，然后你看它这个在这分钟之内它这个有多少次异常，你加一下这个会处罚吗？好了，这就是关于我们注解方式去使用我们的这个三次哨兵的一个全面的讲解。好了，那么这节课我们就讲到这，感谢小伙伴们收看。


