---
title: 2-5 订单模块- Feign接口降级配置-1 
---

# 2-5 订单模块- Feign接口降级配置-1 

[image](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/dc833816-449c-424e-ab2f-4bed454a28ef/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZGD7GKB5%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T225658Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIAgczk37%2Fd5HJpwVVsz20vysWq9ZBVajkSn87GvJpcqiAiEA60kN0HKexPTj0hlXIybP%2Fb%2FO4XZ0d4RidRIv156KEsQqiAQIxv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDKiRUhf%2BCxNyGyoVyCrcAwIAvupiCmNVTiUCOVayk1ccPzawV%2B5yhVazr6aeAsX6KVfTJUSAH0Ng9fYVBdZq3RrDRJAI3vwRQq%2Be5CEqM25sqYchF0ZKPXeGUxm0bLIG1lfl1Lv1gSLGuGV3GtQWyjGiunj%2FvfFA7mHKQliRbgMnRIUHGVeHasCB0%2B4fyHUYi%2FdhSJtrLlTG52%2F8PRX2qX1mhsL%2BpyDCoNnEAZMKYVVABJVmQj41jQfvbI713e1cJGK6%2Fn%2F%2FXqFnen3SMhrUjOxnaV2VazbS77z%2Bdhms8nd1duYXbGjvG7B3trD%2BQ8l%2Bb4%2BVVYgj4d2Z%2FyidEJW0Y9MIUuiovHMpP%2BogLfRvg%2FDV87gJyo6BCejCm91Gcy5A7XGAjT6gmthJ5rqdbZBhtgRMR3o2pLDtjofJvHWG5ebDy7vfm%2F0hiFvsh8IYeACVwSyWcPklKKifztlj0y%2FrvZfDBBgC1YcY7TwvhyLdCTMJNYUrNBOPzU3i6wI67qR7jfrN8KITsjhJZlHxKFGSU77ZuGeLxcVq5JUraYyG08lGY4MESGoRaHq65CbO5o7RnuKzUSDDENmW%2B%2FsG5KqiR10B7T9ToYTW5uV%2BihuoK18OkJYEQZtgAyC4s5BzNAo2kKQGNjHWtWGPVj%2FwML%2B7%2F9IGOqUBvNZe0fZFyX4My7MYdhoOFaJ%2FKWOSx6iS4vvsoINGmwTuMxkRNSaEsB2RYfXSiYinbj52w%2FXa8%2BXwURVgq3CQ2gbV4F7SSOhgM2SsDsJEvrArpef3BlKzeekhXpQOqXYSJ3Znp4Abp3%2B7uPlK45QiLP0ggGSDkDLOf9uL6EyHHCH%2BB56hLM6juVDv0jg3TV38kZ%2FT1ajUZcEYpeKy6mAVi8mDWAZ2&X-Amz-Signature=4cd8ee043996198cd3ee005803a374c0b9bda1afb4650b0843e6e9aa19f2ca1c&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

[image](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/eff3fb5e-1aee-4ee7-ad95-56f1a43310f5/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZGD7GKB5%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T225658Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIAgczk37%2Fd5HJpwVVsz20vysWq9ZBVajkSn87GvJpcqiAiEA60kN0HKexPTj0hlXIybP%2Fb%2FO4XZ0d4RidRIv156KEsQqiAQIxv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDKiRUhf%2BCxNyGyoVyCrcAwIAvupiCmNVTiUCOVayk1ccPzawV%2B5yhVazr6aeAsX6KVfTJUSAH0Ng9fYVBdZq3RrDRJAI3vwRQq%2Be5CEqM25sqYchF0ZKPXeGUxm0bLIG1lfl1Lv1gSLGuGV3GtQWyjGiunj%2FvfFA7mHKQliRbgMnRIUHGVeHasCB0%2B4fyHUYi%2FdhSJtrLlTG52%2F8PRX2qX1mhsL%2BpyDCoNnEAZMKYVVABJVmQj41jQfvbI713e1cJGK6%2Fn%2F%2FXqFnen3SMhrUjOxnaV2VazbS77z%2Bdhms8nd1duYXbGjvG7B3trD%2BQ8l%2Bb4%2BVVYgj4d2Z%2FyidEJW0Y9MIUuiovHMpP%2BogLfRvg%2FDV87gJyo6BCejCm91Gcy5A7XGAjT6gmthJ5rqdbZBhtgRMR3o2pLDtjofJvHWG5ebDy7vfm%2F0hiFvsh8IYeACVwSyWcPklKKifztlj0y%2FrvZfDBBgC1YcY7TwvhyLdCTMJNYUrNBOPzU3i6wI67qR7jfrN8KITsjhJZlHxKFGSU77ZuGeLxcVq5JUraYyG08lGY4MESGoRaHq65CbO5o7RnuKzUSDDENmW%2B%2FsG5KqiR10B7T9ToYTW5uV%2BihuoK18OkJYEQZtgAyC4s5BzNAo2kKQGNjHWtWGPVj%2FwML%2B7%2F9IGOqUBvNZe0fZFyX4My7MYdhoOFaJ%2FKWOSx6iS4vvsoINGmwTuMxkRNSaEsB2RYfXSiYinbj52w%2FXa8%2BXwURVgq3CQ2gbV4F7SSOhgM2SsDsJEvrArpef3BlKzeekhXpQOqXYSJ3Znp4Abp3%2B7uPlK45QiLP0ggGSDkDLOf9uL6EyHHCH%2BB56hLM6juVDv0jg3TV38kZ%2FT1ajUZcEYpeKy6mAVi8mDWAZ2&X-Amz-Signature=2982c62d546fd125e5522546c4d850981dbddc8bb8180e9b7904b5d6892f3938&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

hello 我们客网的各位同学们，大家好，咱这一节将要对分接口形式的调用方式来做服务降级的配置。 OK 那我们去挑选 user 模块，咱先把 user 模块当中我们之前已经配置好的这个熔断降级 high streaks 的默认属性，把它 copy 一下。好， copy 到这里，咱下面这个 login file 不用copy ，因为它是 user 模块特有的一个服务，咱只要把上面的这个默认属性 copy 一下。 OK 那到哪里呢？当然是到咱的订单中心了，因为我们这几个微服务当中，只有订单中心，这里需要用到咱们的份接口来调用其他的两个微服务。 OK 那我们把它 copy 过来以后，我们这里再跟大家开启另外一个配置。这个配置是在份节点下面的。我们份下面有一个专门的 high streaks 配置，因为 fen 它不光集成了 ribbon 它也集成了 hystrix 的功能。所以我们这里有一个 hystrix enabledok 那可以通过这里控制粪接口上的降级是否开启或者是关闭。 OK 那这一段配置都配置好了之后，我们就可以去来写降级熔断的代码了。


OK 那我们这里去挑选哪个服务呢？我们就挑选一个简单的做一个示范。我们看到咱这个 controller 中有一个叫 my comments controller 你看它这里调用了 item comments service 那这个 service 我们点进去看一下它在哪里，它是在商品中心的微服务模型当中。这里提供出了一个粪接口，是商品中心暴露出来的。好我们将要对它指定一些降级熔断的策略。那这第一个问题就来了，我如果要对缝接口上面指定一个降级的类，前面我们学过是怎么处理呢？在 fen client 上面，我们可以直接指定一个 fallback 这个 fallback 是一个 class 那同学们思考这样一个问题，我这个 fallback class 是加在这个 item comments service 上？还是说我要在订单中心上新建一个 service 来继承自这个 item comment service 然后再指定它的降级类这个问题**其实在业界实际的操作当中，有一套相对来说约定速成的规范是这样的**。


**通常来讲一个微服务，那它需要暴露给别的上下游微服务进行调用，它要声明一套接口层对不对？就像咱这里商品中心这里声明了一个 item comments service 它是由我商品研发团队声明出来供其他微服务方调用的。所以说如果我作为商品研发中心团队来说，我如果想对我自己的服务定制特定的降级逻辑，通常来讲我会怎么做呢？我当然是会在我具体的 service 或者是 controller 里面，我在咱服务的内部就已经通过 hystrix comment 来已经指定好了。**


那我这个降级并不需要去暴露给别的上下游服务，也就是说上下游服务他根本不知道我在这个服务背后做了哪些降级流程，他只管调用你的服务。然后你的服务如果发现不超时或者出现异常，那你把降级后的结果再返回给我。Ok.这个我们叫做微服务内部的降级。

[image](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/c79d5ba7-40a3-49e1-a1d7-c95f93bf74fe/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZGD7GKB5%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T225658Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIAgczk37%2Fd5HJpwVVsz20vysWq9ZBVajkSn87GvJpcqiAiEA60kN0HKexPTj0hlXIybP%2Fb%2FO4XZ0d4RidRIv156KEsQqiAQIxv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDKiRUhf%2BCxNyGyoVyCrcAwIAvupiCmNVTiUCOVayk1ccPzawV%2B5yhVazr6aeAsX6KVfTJUSAH0Ng9fYVBdZq3RrDRJAI3vwRQq%2Be5CEqM25sqYchF0ZKPXeGUxm0bLIG1lfl1Lv1gSLGuGV3GtQWyjGiunj%2FvfFA7mHKQliRbgMnRIUHGVeHasCB0%2B4fyHUYi%2FdhSJtrLlTG52%2F8PRX2qX1mhsL%2BpyDCoNnEAZMKYVVABJVmQj41jQfvbI713e1cJGK6%2Fn%2F%2FXqFnen3SMhrUjOxnaV2VazbS77z%2Bdhms8nd1duYXbGjvG7B3trD%2BQ8l%2Bb4%2BVVYgj4d2Z%2FyidEJW0Y9MIUuiovHMpP%2BogLfRvg%2FDV87gJyo6BCejCm91Gcy5A7XGAjT6gmthJ5rqdbZBhtgRMR3o2pLDtjofJvHWG5ebDy7vfm%2F0hiFvsh8IYeACVwSyWcPklKKifztlj0y%2FrvZfDBBgC1YcY7TwvhyLdCTMJNYUrNBOPzU3i6wI67qR7jfrN8KITsjhJZlHxKFGSU77ZuGeLxcVq5JUraYyG08lGY4MESGoRaHq65CbO5o7RnuKzUSDDENmW%2B%2FsG5KqiR10B7T9ToYTW5uV%2BihuoK18OkJYEQZtgAyC4s5BzNAo2kKQGNjHWtWGPVj%2FwML%2B7%2F9IGOqUBvNZe0fZFyX4My7MYdhoOFaJ%2FKWOSx6iS4vvsoINGmwTuMxkRNSaEsB2RYfXSiYinbj52w%2FXa8%2BXwURVgq3CQ2gbV4F7SSOhgM2SsDsJEvrArpef3BlKzeekhXpQOqXYSJ3Znp4Abp3%2B7uPlK45QiLP0ggGSDkDLOf9uL6EyHHCH%2BB56hLM6juVDv0jg3TV38kZ%2FT1ajUZcEYpeKy6mAVi8mDWAZ2&X-Amz-Signature=a230c68278f49cd77d33c9fe4f754fb990056d83eb905b3310643395b143e40f&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

```java
/**
 * <h1>内部的降级（商品中心）放到item-service里面实现</h1>
 * 降级方案（订单中心，调用商品中心服务）由订单中心定义降级逻辑
 */
@FeignClient(value = "foodie-item-service")
@RequestMapping("item-comments-api")
public interface ItemCommentService {

    /**
     * 查询我的评论
     * @param userId
     * @param page
     * @param pageSize
     * @return
     */
    @GetMapping("myComments")
    public PagedGridResult queryMyComment(@RequestParam(value = "userId") String userId, @RequestParam(value = "page", required = false) Integer page, @RequestParam(value = "page", required = false) Integer pageSize);

    @PostMapping("saveComments")
    public void saveComments(Map<String, Object> map);
}
```

那作为调用方来说我也想指定特殊的降级服务。那怎么办呢？假如我这个订单中心调用你的商品服务，那我也想对你的某个特定接口指定降级流程。那我这里想指定的降级策略是在我订单中心这段控制的，它不属于你的商品域，所以理所应当的我们不要修改这个商品域暴露出来的接口。那这种情况下，我们应该在咱的订单中心里面单独声明一套份接口来指定它的降级流程。所以总结出来就是这样一句话，叫内部的降级。也就是说比如说咱的商品中心，咱在商品中心领域内的降级放到咱自己的 item service 里面来实现。


Ok.那对于调用方想要指定的降级，就是咱今天将要讨论的例子，叫订单中心，订单中心怎么样调用商品中心的服务？那这种情况下调用方由订单中心来定义它的降级逻辑。 OK 那所以这就是一个**职责划分，我的就是我的你的，那你自己来搞定**。好，那这里我们已经划分好了界限。那接下来我们要在咱的 order service 里面，去对咱的上游服务来做一个降级流程。


Ok.那我们看到这个在 web controller 里面 my comments 这里调用了 item comments service 好，我们就对它来进行一个降级。那接下来我又在 foodie order service 当中创建一个包。那这个包的路径，同学们看到叫 come.imock.order 那还是订单域的东西，它是放在 order 下面后面跟 fall back 再跟上 item service 好，从这个包名我们就可以看出它是一个订单领域下专门用来指定降级策略的这样一个文件夹路径，从逻辑上也可以很清晰地表达出我对这个商品中心服务的降级是放在咱订单域这边来实现的，也就是说是由调用方来决定的降级逻辑。 OK 咱把这个 package 给它创建出来。Ok.那然后咱在这个下面紧接着创建一个 interface 好，这个 interface 咱给它起名叫 item comments 后面叫 thin client 好，点击。


OK 好，那这个类创建好了之后，我们继承自谁呢？我们这个接口要继承自 item comments service 好，咱把它加进来，然后顺带的在这上边指定一个分 client 那咱的这个分 client 它调用的是谁呢？ foodie item service 对不对？好？那接下来我们看一下，咱订单领域当中有几个类调用了 item comments service 我们要把它替换成咱新创建的这个 item comments thin client 好，我们先到这个 service 里面先来找这个 my comments service 里面看这里，我们把这个注释注释掉，接下来替换成谁偷懒换柱替换成咱刚才创建的这个服务名字不变，这个名字我们依然把它叫做 item comments service 好，把它引入进来 out wide 给它加上。


OK 那这里改完之后，咱还有一个 controller 叫 my comments controller 那在这里面还有一个地方，这里我们依然的同样的方式把它替换成咱刚才创建的这个类 fen client 替换好之后，我们这里要带大家来趟一个坑，我们不妨直接启动一下当前的服务，同学们猜一猜它会报什么样的错误。
我们在启动之前，把咱刚才新添加的这个 package 给它加到扫包路径当中。这个 package 名称叫什么来着？叫 come.imock 点谁呢？点 order order 下面的 fall back 下面的 item service OK 那把这个扫包路径加上之后，咱就可以把这个新添加的分接口给它加载起来了。那我们先来启动一下，同学们看一下这里会有什么错误。这是很多同学第一次在使用分接口配置 hashtags 降级流程当中需要过的第一道坎。你看这个 log 看起来很正常，走着走着它就瘸了。你看瘸了，我们来放大看一下。一个很稀疏平常的错误。他这里面说什么呢？那女孩对，我说。好，我们看。


好，找到最后一个 cosplay 这里异常，我们去做 troubleshooting 的时候，通常从最后一个报错异常开始向上找好这个异常，我们找到它的最后一个报错的地方，看它这里说了什么。你看 ambitions mapping 你一看到这个你就知道了非常常见的一个错误。咱平时在做 spring MVC 或者是 spring boot 的时候，经常会碰到。 Ambitious mapping. 它并不是 spring cloud 当中一个特定的错误，而是将 spring boot spring MVC 等 web 应用当中经常会看到的错误。它的意思是说，你的这个 item comments service 和咱下面指定的这个 item comments think client 这里面有相同的 HTTP 的访问路径。

[image](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/3661d0a6-78ce-4ce5-8f57-d7a9e5cb15e4/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZGD7GKB5%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T225658Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIAgczk37%2Fd5HJpwVVsz20vysWq9ZBVajkSn87GvJpcqiAiEA60kN0HKexPTj0hlXIybP%2Fb%2FO4XZ0d4RidRIv156KEsQqiAQIxv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDKiRUhf%2BCxNyGyoVyCrcAwIAvupiCmNVTiUCOVayk1ccPzawV%2B5yhVazr6aeAsX6KVfTJUSAH0Ng9fYVBdZq3RrDRJAI3vwRQq%2Be5CEqM25sqYchF0ZKPXeGUxm0bLIG1lfl1Lv1gSLGuGV3GtQWyjGiunj%2FvfFA7mHKQliRbgMnRIUHGVeHasCB0%2B4fyHUYi%2FdhSJtrLlTG52%2F8PRX2qX1mhsL%2BpyDCoNnEAZMKYVVABJVmQj41jQfvbI713e1cJGK6%2Fn%2F%2FXqFnen3SMhrUjOxnaV2VazbS77z%2Bdhms8nd1duYXbGjvG7B3trD%2BQ8l%2Bb4%2BVVYgj4d2Z%2FyidEJW0Y9MIUuiovHMpP%2BogLfRvg%2FDV87gJyo6BCejCm91Gcy5A7XGAjT6gmthJ5rqdbZBhtgRMR3o2pLDtjofJvHWG5ebDy7vfm%2F0hiFvsh8IYeACVwSyWcPklKKifztlj0y%2FrvZfDBBgC1YcY7TwvhyLdCTMJNYUrNBOPzU3i6wI67qR7jfrN8KITsjhJZlHxKFGSU77ZuGeLxcVq5JUraYyG08lGY4MESGoRaHq65CbO5o7RnuKzUSDDENmW%2B%2FsG5KqiR10B7T9ToYTW5uV%2BihuoK18OkJYEQZtgAyC4s5BzNAo2kKQGNjHWtWGPVj%2FwML%2B7%2F9IGOqUBvNZe0fZFyX4My7MYdhoOFaJ%2FKWOSx6iS4vvsoINGmwTuMxkRNSaEsB2RYfXSiYinbj52w%2FXa8%2BXwURVgq3CQ2gbV4F7SSOhgM2SsDsJEvrArpef3BlKzeekhXpQOqXYSJ3Znp4Abp3%2B7uPlK45QiLP0ggGSDkDLOf9uL6EyHHCH%2BB56hLM6juVDv0jg3TV38kZ%2FT1ajUZcEYpeKy6mAVi8mDWAZ2&X-Amz-Signature=cc601b4e88acedc70dac7f7f70935a8da9ab4c63700781f7b56a93328a4ca350&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

什么个意思？来同学们看一下。我们收起小桌板，你看这个 item comments service 里面，咱为了使调用方和服务提供者配置起来方便，我们是不是在这个接口层加入了 request mapping 然后每一个方法上面 post get 这些都已经给它指定好了。对不对？那这就形成了一个 HT DP 的访问路径。那当我们在刚才创建的这个 item comments think 的时候，咱继承自了这个 item comments service 所以我们这个接口也自然而然的继承了这个原生接口上面这些 request mapping 这些 annotation 还有方法上的 mapping 路径。因此一个同样的方法，比如 save comments 它同时存在的两套接口中，并且这两套接口中给我配置的 request mapping 访问路径 post mapping 都是一样的。那在这种情况下，那 spring boot 它不干了，那 spring boot 它在加载整个上下文的时候，它发现你的这个方法已经在其中某个接口里面实现了。那么这样的话，你在同时加载两个接口的时候，它加载了两个同样访问路径的方法，那就会给你报出 ambitions mapping okay 那通常来讲这个情况我们怎么来办？那半仙老师这里就给同学三枚锦囊妙记，这每一个锦囊里面都有一个解决的办法，一个问题条条大路通罗马，它有很多种方式可以把它搞定掉。同学们只要挑选一个自己得心应手，看着顺眼，用着舒服的方式来解决就行了。当然了，这每一个方式之间也有优点缺点，那老师这里就跟大家去来展示一下。


好，那我们就从发现问题，寻找根本的引起问题的原因，再到解决问题这个思路来出发。我先把刚才的问题给他在这边注释下来。这段很长的注释就是叙述了刚才我们发现的问题，也就是说两个接口同时被加载到上下文当中。但是他们定义了对同样方法相同访问路径的两个实例，所以它会引发 

[image](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/676239fd-eb60-4271-bf53-f3813a66cbc4/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZGD7GKB5%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T225658Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIAgczk37%2Fd5HJpwVVsz20vysWq9ZBVajkSn87GvJpcqiAiEA60kN0HKexPTj0hlXIybP%2Fb%2FO4XZ0d4RidRIv156KEsQqiAQIxv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDKiRUhf%2BCxNyGyoVyCrcAwIAvupiCmNVTiUCOVayk1ccPzawV%2B5yhVazr6aeAsX6KVfTJUSAH0Ng9fYVBdZq3RrDRJAI3vwRQq%2Be5CEqM25sqYchF0ZKPXeGUxm0bLIG1lfl1Lv1gSLGuGV3GtQWyjGiunj%2FvfFA7mHKQliRbgMnRIUHGVeHasCB0%2B4fyHUYi%2FdhSJtrLlTG52%2F8PRX2qX1mhsL%2BpyDCoNnEAZMKYVVABJVmQj41jQfvbI713e1cJGK6%2Fn%2F%2FXqFnen3SMhrUjOxnaV2VazbS77z%2Bdhms8nd1duYXbGjvG7B3trD%2BQ8l%2Bb4%2BVVYgj4d2Z%2FyidEJW0Y9MIUuiovHMpP%2BogLfRvg%2FDV87gJyo6BCejCm91Gcy5A7XGAjT6gmthJ5rqdbZBhtgRMR3o2pLDtjofJvHWG5ebDy7vfm%2F0hiFvsh8IYeACVwSyWcPklKKifztlj0y%2FrvZfDBBgC1YcY7TwvhyLdCTMJNYUrNBOPzU3i6wI67qR7jfrN8KITsjhJZlHxKFGSU77ZuGeLxcVq5JUraYyG08lGY4MESGoRaHq65CbO5o7RnuKzUSDDENmW%2B%2FsG5KqiR10B7T9ToYTW5uV%2BihuoK18OkJYEQZtgAyC4s5BzNAo2kKQGNjHWtWGPVj%2FwML%2B7%2F9IGOqUBvNZe0fZFyX4My7MYdhoOFaJ%2FKWOSx6iS4vvsoINGmwTuMxkRNSaEsB2RYfXSiYinbj52w%2FXa8%2BXwURVgq3CQ2gbV4F7SSOhgM2SsDsJEvrArpef3BlKzeekhXpQOqXYSJ3Znp4Abp3%2B7uPlK45QiLP0ggGSDkDLOf9uL6EyHHCH%2BB56hLM6juVDv0jg3TV38kZ%2FT1ajUZcEYpeKy6mAVi8mDWAZ2&X-Amz-Signature=2e735b3e20647cf4bf09c802cba2c92e5848038c2d42d4c4f4156a4976818fca&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

ambitions mapping 的错误。那么这个解决思路其实非常非常的简单。那就是在 spring 的上下文当中，我们尽量避免去同时加载两个访问路径相同的方法。顺着这个思路我们往下来想，如果你非要加载这两个类，那么这里面的方法的访问路径你能不能改不能改的，因为你一改了，那我们的分接口去寻址的时候，那就会发错路径，导致这个方法得到 404 not found 那既然我们不能硬改访问路径，那怎么办呢？这里的解法非常的多，它有大概这么三个解决方案，我跟同学们挨个去大致的描述一下。
第一个方案就是说我们在项目启动的时候不是要扫包吗？问接口要扫运行包，那这个时候咱不要把原始的分接口扫描进来就行了，只要把咱新建的这个 item comments 分 client 扫描进来，那就可以


了。这样的话咱在整个 spring 上下文当中就不会存在重复的现象了。 OK 那具体怎么来做非常的简单。我们只要把启动类上面 enable 分 clients 里面的注解，通过 clients 这个属性来指定你需要加载的对象，指定你需要加的接口，而不是通过扫包的这种方式配置就迎刃而解了。


那我们去看一下怎么来做，我们转战到 order application 好，你看，咱这里是用的 base packages 好，我们把这种方式给它摒弃掉，换成谁换成一个新的注释方式叫 clients 那咱的 clients 里面都有哪些内容呢？很简单，咱先把前面咱创建的 item comments 分 client 给它加载进来。


那接下来这个要不要加进来呢？ item comments service 咱不要把它给带进来，咱把其它的服务需要用到的通给它用这种方式给它加进来。比如还有 user service 也要用到的还有什么 address address serviceok 那通过这种方式，你用到什么类我才把它添加到 thin clients 的上下文当中，这样的话就可以避免重复了，对不对啊？那这种方式有显而易见的优点和缺点。比如说它的优点就是服务提供者和服务调用者我不需要额外的配置，咱只需要在启动类的时候，把这些需要加载进来的类给它列出来就可以了。那缺点自然而显而易见，你启动的时候是不是会麻烦一点，以前只用配个扫班路径就可以了。那你现在要把这个路径下的所有类给它加进来，那看起来是麻烦的一点。不过在实际使用过程中，咱其实也没有那么多的类需要加载进来。所以我个人比较喜欢这种方式的解决方案。 OK 那咱看一下还有没有其他的解决方案呢？那当然有了，咱说过三个锦囊妙记。

```java
import com.imooc.item.service.ItemCommentService;
import com.imooc.order.fallback.itemservice.ItemCommentsFeignClient;
import com.imooc.user.service.AddressService;
import com.imooc.user.service.UserService;
import org.springframework.boot.WebApplicationType;
import org.springframework.boot.autoconfigure.SpringBootApplication;
import org.springframework.boot.builder.SpringApplicationBuilder;
import org.springframework.cloud.client.discovery.EnableDiscoveryClient;
import org.springframework.cloud.openfeign.EnableFeignClients;
import org.springframework.context.annotation.ComponentScan;
import org.springframework.scheduling.annotation.EnableScheduling;
import tk.mybatis.spring.annotation.MapperScan;

/**
 * <h1></h1>
 */
@SpringBootApplication
// 扫描mybatis 通用 mapper 所在的包
@MapperScan(basePackages = "com.imooc.order.mapper")
// 扫描所有包以及组件包
@ComponentScan(basePackages = {"com.imooc", "org.n3r.idworker"})
@EnableDiscoveryClient
@EnableScheduling
@EnableFeignClients(

            clients = {
                    ItemCommentsFeignClient.class,
                    ItemService.class,
                    UserService.class,
                    AddressService.class
            }

//        basePackages = {
//        "com.imooc.user.service",
//        "com.imooc.item.service",
//        "com.imooc.order.fallback.itemservice",
//}
)
public class OrderApplication {
    public static void main(String[] args) {
        new SpringApplicationBuilder(OrderApplication.class)
                .web(WebApplicationType.SERVLET)
                .run(args);
    }
}
```



第二个是什么呢？第二个方式就是说原始的这个分解口咱不要定义 request mapping 注解。 OK 那从这里给它删除掉。那删除掉之后我们要把它放在哪儿呢？那当然是它的服务提供者和服务调用者，那都需要在自己头上加上这个注解了。所以这种配置方式它的优点和缺点也是显而易见的。优点是我启动的时候直接扫包是不是就可以了？不用像前面一个方案一样指定加载一大串的接口。那缺点就是说你的服务提供者需要额外配置路径访问的注解。


当前我们看它的服务提供者上面是没有 request mapping 的每一个方法上面也没有对应的 post mapping get mapping 那是因为通通都从 item comments 当中继承过来了，通过实现接口的方式把它给继承过来。那如果你把这个 mapping 全都移除掉了，那你的服务提供者首先需要配置这些注解。并且在任何情况下作为服务调用者来说，即使咱不需要去重新定义一个分接口来指定 fall back 类，那么你依然要在服务调用者这里声明一个独立的接口。为什么呢？这里正是需要在这个独立接口中声明这些 request mapping 即 post mapping get mapping 这些路径信息。


为何前面一个配置方式比起来，我个人觉得这种方式似乎稍显麻烦一点。其实很多同学在自己项目当中或者有些公司也非常喜欢在每一个服务调用者这里声明一个独立的分接口。那当然这种方式也是可以的，具体要结合自己公司规范。那咱没有一个非黑即白的标准答案，同学们根据自己的个人喜好还有公司的要求来自由选择就可以了。

[image](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/a28d3019-e265-408e-9c65-308dc9e263c0/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZGD7GKB5%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T225658Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIAgczk37%2Fd5HJpwVVsz20vysWq9ZBVajkSn87GvJpcqiAiEA60kN0HKexPTj0hlXIybP%2Fb%2FO4XZ0d4RidRIv156KEsQqiAQIxv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDKiRUhf%2BCxNyGyoVyCrcAwIAvupiCmNVTiUCOVayk1ccPzawV%2B5yhVazr6aeAsX6KVfTJUSAH0Ng9fYVBdZq3RrDRJAI3vwRQq%2Be5CEqM25sqYchF0ZKPXeGUxm0bLIG1lfl1Lv1gSLGuGV3GtQWyjGiunj%2FvfFA7mHKQliRbgMnRIUHGVeHasCB0%2B4fyHUYi%2FdhSJtrLlTG52%2F8PRX2qX1mhsL%2BpyDCoNnEAZMKYVVABJVmQj41jQfvbI713e1cJGK6%2Fn%2F%2FXqFnen3SMhrUjOxnaV2VazbS77z%2Bdhms8nd1duYXbGjvG7B3trD%2BQ8l%2Bb4%2BVVYgj4d2Z%2FyidEJW0Y9MIUuiovHMpP%2BogLfRvg%2FDV87gJyo6BCejCm91Gcy5A7XGAjT6gmthJ5rqdbZBhtgRMR3o2pLDtjofJvHWG5ebDy7vfm%2F0hiFvsh8IYeACVwSyWcPklKKifztlj0y%2FrvZfDBBgC1YcY7TwvhyLdCTMJNYUrNBOPzU3i6wI67qR7jfrN8KITsjhJZlHxKFGSU77ZuGeLxcVq5JUraYyG08lGY4MESGoRaHq65CbO5o7RnuKzUSDDENmW%2B%2FsG5KqiR10B7T9ToYTW5uV%2BihuoK18OkJYEQZtgAyC4s5BzNAo2kKQGNjHWtWGPVj%2FwML%2B7%2F9IGOqUBvNZe0fZFyX4My7MYdhoOFaJ%2FKWOSx6iS4vvsoINGmwTuMxkRNSaEsB2RYfXSiYinbj52w%2FXa8%2BXwURVgq3CQ2gbV4F7SSOhgM2SsDsJEvrArpef3BlKzeekhXpQOqXYSJ3Znp4Abp3%2B7uPlK45QiLP0ggGSDkDLOf9uL6EyHHCH%2BB56hLM6juVDv0jg3TV38kZ%2FT1ajUZcEYpeKy6mAVi8mDWAZ2&X-Amz-Signature=1b7e6ad984cd89b3faa87cdc26a539b8a99cf55e55f8afd5e96c73ee5efa7390&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)


OK 那我们再说最后一个锦囊妙记是什么呢？这个锦囊妙记更狠了，它说原始的这个分接口，咱不用指定分 client 注解。好嘞，那你把这个分 clients 直接给它就拿掉了。那这样的话它的优点和缺点，同学们这一拍脑袋就能想出来了。优点吗？自然有两个。那第一个是说你启动的时候，咱也通过扫包来扫描份注解就可以了。那因为你这个服务 item service 里面，它没有定义分 class 注解，所以你扫包能不能把它扫加载到上下文中呢？不能。同学们所以这里在启动的时候配置相对简单一些，并且相对于第二种的解决方案，咱在服务提供者这一个层面，不用额外的配置。为什么？因为咱的这些 request mapping 还依然的放在了这个接口层这里，所以服务提供者依然可以继承咱们在接口层这里定义的这些 mapping 那这种方式也有一个显而易见的缺点。


那和第二种方案的缺点 B 是一样的，就是在任何情况下，我需要在服务调用者这里增加一个额外的分 client 接口，并且在这个接口上面盖上一顶大帽子，分 client 那这三个方案各有利弊，所以同学们按照个人喜好来选就行。那我自然是比较喜欢第一种解决方案。对不啦，因为毕竟老师是个懒人，听好是懒人不是烂人。那这第一种解决方案，咱们在这里已经配置好了一半，这四个 client 都已经洋洋洒洒地列在这里了。

[image](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/bd8f16ed-1754-492a-89f4-f506485feb73/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZGD7GKB5%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T225658Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIAgczk37%2Fd5HJpwVVsz20vysWq9ZBVajkSn87GvJpcqiAiEA60kN0HKexPTj0hlXIybP%2Fb%2FO4XZ0d4RidRIv156KEsQqiAQIxv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDKiRUhf%2BCxNyGyoVyCrcAwIAvupiCmNVTiUCOVayk1ccPzawV%2B5yhVazr6aeAsX6KVfTJUSAH0Ng9fYVBdZq3RrDRJAI3vwRQq%2Be5CEqM25sqYchF0ZKPXeGUxm0bLIG1lfl1Lv1gSLGuGV3GtQWyjGiunj%2FvfFA7mHKQliRbgMnRIUHGVeHasCB0%2B4fyHUYi%2FdhSJtrLlTG52%2F8PRX2qX1mhsL%2BpyDCoNnEAZMKYVVABJVmQj41jQfvbI713e1cJGK6%2Fn%2F%2FXqFnen3SMhrUjOxnaV2VazbS77z%2Bdhms8nd1duYXbGjvG7B3trD%2BQ8l%2Bb4%2BVVYgj4d2Z%2FyidEJW0Y9MIUuiovHMpP%2BogLfRvg%2FDV87gJyo6BCejCm91Gcy5A7XGAjT6gmthJ5rqdbZBhtgRMR3o2pLDtjofJvHWG5ebDy7vfm%2F0hiFvsh8IYeACVwSyWcPklKKifztlj0y%2FrvZfDBBgC1YcY7TwvhyLdCTMJNYUrNBOPzU3i6wI67qR7jfrN8KITsjhJZlHxKFGSU77ZuGeLxcVq5JUraYyG08lGY4MESGoRaHq65CbO5o7RnuKzUSDDENmW%2B%2FsG5KqiR10B7T9ToYTW5uV%2BihuoK18OkJYEQZtgAyC4s5BzNAo2kKQGNjHWtWGPVj%2FwML%2B7%2F9IGOqUBvNZe0fZFyX4My7MYdhoOFaJ%2FKWOSx6iS4vvsoINGmwTuMxkRNSaEsB2RYfXSiYinbj52w%2FXa8%2BXwURVgq3CQ2gbV4F7SSOhgM2SsDsJEvrArpef3BlKzeekhXpQOqXYSJ3Znp4Abp3%2B7uPlK45QiLP0ggGSDkDLOf9uL6EyHHCH%2BB56hLM6juVDv0jg3TV38kZ%2FT1ajUZcEYpeKy6mAVi8mDWAZ2&X-Amz-Signature=839d4cac143d917c9a72c5ebe3181a1f938607d1682ca6eee338aae7dd89327a&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

其中这个 item comments service 怎么浑水摸鱼又进去了，咱们把它去掉，可不要让它混进去了，这样的话启动依然会报 ambitions mapping 这个错误的。 OK 那咱这一节就先告一段落了。在下一节当中，我将要通过第一种方案继续往下走，带同学们把这个分接口的降级服务给它配置好。好同学们，那我们下一小节再见。


