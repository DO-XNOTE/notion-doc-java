---
title: 2-3 用户模块- 基于HystrixCommand注解配置降级和线程池 
---

# 2-3 用户模块- 基于HystrixCommand注解配置降级和线程池 

[image](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/167d4765-3222-4d0e-b1e6-93bf1087f371/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UE3J2JRJ%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T225656Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCICaWRJawQEF4xe9MSKB7gcGs9UcAaawb2FTYuIBzh%2BuDAiEApahm6bfjuJF1hcTM3qKeXmfQyY5icpGTs6EU4IaDOkgqiAQIxv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDOh5eZz8gvqcJ5pAiSrcA7XKh8Vij52o5SegLcGGCn9%2FjNQSzGnaE6BKix0wOJ7UH2M9XZXEhyxUOH52NO3T6kYiBBKLtAeDzz96I27JGgWg6%2BvGvhM3dtgXnF%2FXZcpYGn3J7324DvUXz2NTnCznEUuxLtAUvU4qiWTwhh8tXZhYTdGW0Qz0T9HD9qLHmgAatSLgUPYLFAPU37QYzAlB7AmANsha2nSLP7N%2B7LupQXrS0oRe7JSasRqVZ9M65qJ1arBP2hPoa6n3m2znF0muKn%2BztgDcCBbGPm3ySx5Lj7n2OrcFq3jrN296ST4ad7NBXjjCpXu7LcrG7LzHVzbkLZD7YdgwU8ORH1a122wHn1RZhExNKDanbpotce0Lpzkz0fgjzDa097sRCNlbQqE9UUE6sHx5xLvu1TR4el%2BKB9tRuGv4m6YG6AwqxyDn%2FEz3lbjnURx%2BVx38vmj5Un%2Bqi4x%2FOqrif1b1nE6jC97Hes6qcT2qHgrgW%2BgEGprAzuZbrzvoMbkRJUUSaytMhn0OGQcEmkSAqGYVHKjFLnZZ55ACUL6S%2FmvC1TeI50pzpmXhGGco3VuuIQ9BufYDRqBz4WQcQKggEJyxuZgV8qeyc5R2UJKK8H%2BTjiAdeJwf63zbK3TVGOEqo1EAUuYmMLe4%2F9IGOqUBFuSn9kfkFef4CM%2BKn%2BVZczmH1w3Or3y3yaHxP77wifOklGoX5zuBCU2D7w%2FaTxLHLJCB%2FGsK2g4k1YMeRwWoVm7H1sdDi04i%2B87oqegyU4Zn0doz5kvnZ%2BuweqjwVUqf2HVbjiv7BaW7WHZZPKhStsO79jacjb7kjz%2F%2BW6uocUCsuuYREaodXJkI%2Bctc9recbIdBPdRdlMFxb5IKgbU4KC1JPlVa&X-Amz-Signature=99f84342f795cdec6ded7a015beeb35e4b364c5cd56b13d6a9d76a79005170f8&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

[image](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/8a78b4df-a272-408c-8e39-fb9c23663169/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UE3J2JRJ%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T225656Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCICaWRJawQEF4xe9MSKB7gcGs9UcAaawb2FTYuIBzh%2BuDAiEApahm6bfjuJF1hcTM3qKeXmfQyY5icpGTs6EU4IaDOkgqiAQIxv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDOh5eZz8gvqcJ5pAiSrcA7XKh8Vij52o5SegLcGGCn9%2FjNQSzGnaE6BKix0wOJ7UH2M9XZXEhyxUOH52NO3T6kYiBBKLtAeDzz96I27JGgWg6%2BvGvhM3dtgXnF%2FXZcpYGn3J7324DvUXz2NTnCznEUuxLtAUvU4qiWTwhh8tXZhYTdGW0Qz0T9HD9qLHmgAatSLgUPYLFAPU37QYzAlB7AmANsha2nSLP7N%2B7LupQXrS0oRe7JSasRqVZ9M65qJ1arBP2hPoa6n3m2znF0muKn%2BztgDcCBbGPm3ySx5Lj7n2OrcFq3jrN296ST4ad7NBXjjCpXu7LcrG7LzHVzbkLZD7YdgwU8ORH1a122wHn1RZhExNKDanbpotce0Lpzkz0fgjzDa097sRCNlbQqE9UUE6sHx5xLvu1TR4el%2BKB9tRuGv4m6YG6AwqxyDn%2FEz3lbjnURx%2BVx38vmj5Un%2Bqi4x%2FOqrif1b1nE6jC97Hes6qcT2qHgrgW%2BgEGprAzuZbrzvoMbkRJUUSaytMhn0OGQcEmkSAqGYVHKjFLnZZ55ACUL6S%2FmvC1TeI50pzpmXhGGco3VuuIQ9BufYDRqBz4WQcQKggEJyxuZgV8qeyc5R2UJKK8H%2BTjiAdeJwf63zbK3TVGOEqo1EAUuYmMLe4%2F9IGOqUBFuSn9kfkFef4CM%2BKn%2BVZczmH1w3Or3y3yaHxP77wifOklGoX5zuBCU2D7w%2FaTxLHLJCB%2FGsK2g4k1YMeRwWoVm7H1sdDi04i%2B87oqegyU4Zn0doz5kvnZ%2BuweqjwVUqf2HVbjiv7BaW7WHZZPKhStsO79jacjb7kjz%2F%2BW6uocUCsuuYREaodXJkI%2Bctc9recbIdBPdRdlMFxb5IKgbU4KC1JPlVa&X-Amz-Signature=2836893823b6040bfd29db4a887f13aa78ff725c31b9ce3cb94a68b9ff38e6f2&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

慕课网的各位小伙伴们，大家好，这一节里我们就要把 high streaks 应用到咱的业务流程里面。我们先挑选一个微服务，就拿 user 微服务来开始动刀子。那我们如果要开启hystrix ，这里必不可少的一步，先是要找到它的 user application 这个方法，我们这里要在这上面添加一个注解。


什么注解呢？Enable. enable 谁呢？ enable 这个 circuit breaker 熔断降级。 OK 把这个注解添加进去之后，我们去找到一个 controller 随便拿一个 controller 来开始动手就拿它好了。 passport controller 同学们可能会有一点疑问，咱的这个 user 这个微服务它处于一个上游服务，它并没有调用其他的微服务。那这种情况下 high strikes 可以起作用吗？当然是可以的。同学们可能经过前面分章节的学习，会有一点思维定式，认为我们 high streaks 只能应用在方法间调用其实不然，比方说我这里一个 controller passport controller 这里有登录、用户注册等等这些服务，那只要符合 spring a op 切点的这些方法，我都可以给它加上 high strikes comment 这个注解。


OK 那我们这里就先拿这个 log in 来动一个刀子用户登录是一个网站系统当中最容易做降级的部分了，它的流程非常简单，一般都是静默降级。在大家都用过 12306 买火车票。对不对？你登录不上去的时候，它会告诉你是验证码不对。其实根本不是验证码不对，而是说在高峰流量的时候，后台服务直接拒绝了你的请求。 OK 那我们这里就可以用 hystrix comment 来模拟一下这个情况，顺带再跟大家讲一下 hystrix command 中的几个主要的配置项。


OK 那我们这就开始了。那首先我们最重要的一个配置项，虽然很多情况下同学们并不用，但是这个配置项在后台的业务流程中还是很重要的。叫 command key 那 command key 我们这里给它指定叫什么叫 log in 好了，就把它起名叫 log in 那它是什么含义呢？首先我们去明确一下，它是一个全局唯一的标识服务。 OK 那这个标识服务如果你不指定的话，它的默认是谁呢？默认就是函数名称。 OK 咱的这个函数名称 login 那它这里的值默认就是 login 了。 OK 那我们给它起个不一样的志好来叫 login feel 当你指定了这个全局唯一的标识服务之后，那咱可以在项目的 YAML 文件当中通过这个 key 找到咱配置的这个 high streaks commandok 那这个 key 配置完了，那接下来我们配置另一个 key 跟分组有关的 group keyok 我把这个逗号打上好。


group key 那 group K 我们这里给它指定就叫 password 好了。 OK 那它又是什么含义呢？它是指一个全局服务分组。这个含义我们可以给不同的 high strikes command 指定同一个 group key 那这样的话它就属于同一个分组了。对不对？那它通常用在什么地方呢？那它会用于比如说组织仪表盘，大家前面都看过 dashboard 这些仪表盘操作，还有一些统计信息。那做一个分组。那当你不指定 group key 的时候， high strikes 会为它默认指定一个值，那它的默认值是谁呢？是类名，就是你当前这个类的名称，咱这个叫 passport controller 好，那它这里就会给你默认一个类名。那除了这两个以外，我们这里添加一个最关键的属性。


前面大家在 demo 环节当中也已经有做过，这个属性是 fall back method 好我们这里给它起一个名字就叫 login feel 那 login feel 这一个属性它是指向谁，指向你当前这个类的一个方法，所以说你要放在同一个类里面，那这个方法它的可见度是 public 或者 private 都可以，因为它毕竟在同一个类里面的。所以咱们定义成 public private 其实都是可以的。 OK 都可以。好。那接下来再跟大家说哪个属性，跟说一下这个。


好了，ignore except OK exceptions 那它后面是叫 exception S 说明这里可以配置一个集合对不对？那它是什么含义呢？它这里是配置一些例外的情况，什么叫例外情况？也就是说列表中的 exception 怎么样不会触发降级。


OK 那我们这里可以找一些非常特殊的exception ，比如说 illegal arguments 好了，那这里的 exception 实际上是根据大家自己的具体业务来自己配置的。那所以我暂时把它给注释掉。同学们如果需要去配置的话，那记得找到这样一个 ignore exceptions 这样一个配置项。 OK 那接下来我要配置一个跟线程有关的属性了，准确的说是一堆属性。 OK 在前面都学过 high strikes 的线程池，信号量等等。那我们这里通过 hystrix command 也可以配置线程相关的参数。那比方说我这里就跟大家先配置一个什么线程组。


好了。 OK 这个线程组名称叫什么呢？ Thread pool key. OK 我这里给它起名叫 thread to A 什么含义呢？它这个线程组可以有多个服务，可以共用一个线程组。那好，咱这个线程组定义好了以后，那自然要去定义线程组的一些属性了，它的属性的这个 key 叫做 thread pull properties 好，这个 properties 里面就包罗万象了，非常非常多。那同学们感兴趣的话可以去找官方的文档来学习一下 thread pool 中的属性都有哪些？那我这里挑选几个比较有代表性的属性跟大家去过一下。


好了。 OK 那咱这每一个属性在 high strikes command 当中是怎么来引入呢？我们这里要借助于 high strikes a property 把 property 引入进来。那我这里给他指定一个谁指定一个 name 这个 name 就是我接下来要指定的属性名称。比如说这一个 call size 那看这个名称就知道非常重要。对不对？ call 核心人物。那它是什么个含义呢？很简单，顾名思义，核心线程数。 OK 那除了核心线程数以外，自然有非核心的线程数，对不对？你从它这个名字就能看出来了。


那接下来给大家介绍一个两面派的属性。为什么叫它两面派？我们来看它也是这个线程隔离中一个比较重要的参数这个 property 的名称叫做什么呢？它叫做 max Q size 最大的 Q 的长度。那我们这里给它写个 40 毫嘞。那它为什么说是两面派呢？因为它是一个条件判断的东西。


那如果你这个 cue the size ，我们说它大于 0 的时候和小于 0 的时候默认负1，在这两个情况下它的行为是不一致的。 OK 那它哪些行为不一致啊？它的实现方式是不一致的。那大于零的时候它这里是什么来实现呢？ linked blocking queue 那这是一个很常见的数据结构，大家应该都比较熟悉了，那面试里面的看 current 包下的这些类都是经常会被问到的。所以我这里也建议同学们看到一个小的知识点，比方说 high streaks 咱从一个知识点把它深入进去，咱通过表象深入到本质这一个属性。咱知道用法了之后，我们再深入到底层，看一下它怎么实现的，顺带把它的实现类也给它看一下，这样顺藤摸瓜，你就能从一个现象到本质，从头到尾全部拎清楚，非常清晰。


OK 那我们接着回来，说到这个 link 的 blocking Q 那它就是等待，请求等待的队列。那在说到这个默认负 1 默认负 1 的时候，它是用的谁 synchronous Q 那看的名称大家有可能没有用过，可能大部分同学看起来还比较陌生，或者是只在什么面试宝典中用过它对不对？那我们其实在很多开源项目中都可以见到他的身影。那它是什么呢？它也是一个阻塞队列，我们先明确依然是阻塞队列。但是这个阻塞它有一个特性叫什么呢？它不存储元素。那什么叫做不存储元素呢？我这里建议同学不要听老师瞎掰，我们直接去怎么样呢？建议读编码是源码，是我们学习一项技术最全面最能加深记忆的方式。如果你通过这个课程，老师告诉你一下这个类是什么作用，那它的底层机制是什么？你很快就会忘了。但是你如果把这个类我们直接点到 GD K 里，很简单的直接给他打几个断点，从头到尾这样 debug 一番，看看他的初始化使用流程都是怎么样的。那你对他这个记忆就会非常的深刻。


OK 那老师为什么也建议大家去读一下这个类的源码，因为它这里面牵扯到很多什么操作呢？ CAS 操作我们可以学到 CAS 操作在 gdk 核心类当中的具体应用。 OK 那我们接着往下讲，咱看了两个属性之后，我们来给大家说一个 maexcusize 的姐妹篇。什么叫姐妹篇呢？就是这两个属性是相互关系的。那它叫什么名字呢？叫 Q size rejection 这里注意名称不要拼错了 rejection threshold OK 我这里给他随便写就写个 15 了。那它是什么含义？他为什么跟前面一个称作姐妹篇呢？因为他在这一个属性 max Q says 等于负 1 的时候。

```java
/**
     * 这个降级的配置 导致代码看上去好像有点乱，也可以转移到 yml文件中去配置
     * @param userBO
     * @param request
     * @param response
     * @return
     * @throws Exception
     */
    @ApiOperation(value = "用户登录", notes = "用户登录", httpMethod = "POST")
    @PostMapping("/login")
    @HystrixCommand(
            commandKey = "loginFail", // 全局唯一的标识符， 默认是函数名称
            groupKey = "password", // 全局服务分组， 用于组织仪表盘，统计信息。默认是类名
            fallbackMethod = "loginFail", // 同一个类里面， public/ private 都可以
            // 在列表中的exception， 不会触发降级
//            ignoreExceptions = {IllegalAccessException.class},
            // 现成相关的线程池
            // 线程组,可以公用一个线程组
            threadPoolKey = "threadPoolA",
            threadPoolProperties = {
                    // 核心线程数
                    @HystrixProperty(name = "coreSize", value = "20"),
                    // size > 0, LinkedBlockingQueue -> 请求等待队列
                    // 默认 -1，SynchrounousQueue -> 不存在元素的阻塞队列（建议学习远吗， 学习CAS运用）
                    @HystrixProperty(name = "maxQueueSize", value = "40"),
                    // 在 maxQueueSize 的时候无效，队列没有达到 maxQueueSize 依然拒接
                    @HystrixProperty(name = "queueSizeRejectionThreshold", value = "15"),
                    // （线程池）统计窗口持续时间
                    @HystrixProperty(name = "metrics.rollingStats.timeInMilliseconds", value = "1024"),
                    // （线程池）统计窗口内桶的数量
                    @HystrixProperty(name = "metrics.rollingStats.numBuckets", value = "18")
            }
//            ,
//            commandProperties = {
//                    // TODO 熔断降级相关属性，也可以配置在这里
//            }
    )
    public IMOOCJSONResult login(@RequestBody UserBO userBO, HttpServletRequest request, HttpServletResponse response) throws Exception {
        String username = userBO.getUsername();
        String password = userBO.getPassword();

        // 0: 判断用户名和密码是否是空
        if (StringUtils.isBlank(username) || StringUtils.isBlank(password)) {
            return IMOOCJSONResult.errorMsg("用户名或者密码不能为空");
        }

        // 1: 实现登录
        Users userResult = userService.queryUserForLogin(username, MD5Utils.getMD5Str(password));

        if (userResult == null) {
            return IMOOCJSONResult.errorMsg("用户名或者密码不正确");
        }

        userResult = setNullProperties(userResult);

        CookieUtils.setCookie(request, response, "user", JsonUtils.objectToJson(userResult), true);
        // TODO  生成用户TOKEN,存入到redis会话
        // TODO  同步购物车数据
        return IMOOCJSONResult.ok(userResult);
    }

    /** 降级方法
     * */
    public IMOOCJSONResult loginFail(@RequestBody UserBO userBO, HttpServletRequest request, HttpServletResponse response) throws Exception {
        return IMOOCJSONResult.errorMsg("验证码输错了， 模仿12306");
    }
```

怎么样呢？无效其实这很好理解了，你队列的最大值是通过一个无缓冲的不存储元素的阻塞队列来实现的。那你自然没有这个队列长度了。所以这个字段的意思是当你前面这个值设置了大于 0 的时候。那我这里的具体给定的这个 Q size ，rejection threat hold 可以在队列没有达到谁达到你 max Q size 指定的这个长度的时候依然拒绝。所以下面这个属性比上面这个属性看起来更狠那么一点，拒绝你给你发张好人卡，走到熔断降级流程当中去。


那我们接着往下看，接下来的属性就跟统计有关。比方说我接下来介绍的是一个 matrix.rolling state 再一个点 timing milliseconds 那你看milliseconds ，那就是毫秒的意思，我这里给它指定个值叫1024。好啦，大家都很熟悉啦。 1024 它是什么含义呢？它跟线程池有关。 OK 它是指统计窗口持续时间。 OK 这个统计窗口是指谁呢？括号线程池，因为它是配置在哪，配置在咱 thread pool 下面的，那自然是跟线程池有关系的。 OK 我们把它再复制一下。


前面说到有两个 metrics 统计相关的属性，那上面的是一个下面的这一个，我们把它的最后的这个单词给它改一下，它不是 time in many seconds 了，它是 number buckets 好，这个 number buckets 就是桶的数量，我们把它改成1024，是个 18 进的话题，我们把它改成18。那它的含义是指窗口内桶子的数量。 OK 所以把这两个连起来，就是你一段指定时间内我设置一个统计窗口，然后在这个统计窗口内我均分多少个桶？ OK 非常简单。


那咱这里配置属性不光有 threadpoolproperties 还有什么呢？还有一个也是跟 properties 有关的，它是咱熔断降级的 practice 都可以在这里面配叫 command practice 那么这里其实加一个 todo 跟大家说一下，熔断降级相关属性怎么样，也可以放在这里。


那待会我们会到配置文件当中跟大家展示一下怎么来配置这个 command problems 好，我这里先把它给注释掉。那我们这一节就暂且先不配置容端降级相关的属性。那在下一节当中，我们在配置文件中再来配置这些属性。不过同学们记住，熔断降级相关属性我既可以在配置文件当中，也可以把它下放到哪里，下放到 hystrix command 当中来进行配置，非常的灵活。


好，那咱这个标签注解已经配置完了吗？似乎还没有，咱这里这个 fall back method 是不是还没有写呢？对不对？好，我们把它复制一下，咱这个名称叫 login feel 把这一个方法的名称全部给它拿过来 copy 一下，走到这里把它粘贴过来。咱要配置一个一模一样的方法。什么一模一样叫签名一模一样，但是它的方法名不一样，咱前面叫什么它的 fallback 方法叫 login feelokay 那好，


我这里也把它改叫 login feel 那方法的这个签名有什么参数？依然放什么参数，不过像这里可以多一个参数是谁呢？同学们这里看 through throwable okay 因为咱到了这个降级流程当中，肯定是犯了什么事儿对不对？要么什么 exception 要么超时那他可能会有一个 throwable 的这个错误抛出来。那你在这个 fall back 方法当中，可以去接收这个错误来做一些 log 打印或者去分析，看它的错误类型等等都可以。


好，咱这个方法可见度，其实 public private 都是可以的，我们把它设置成 private 那这个流程非常非常的简单，咱就模仿谁模仿12306。好了，你登录失败了，我告诉你是验证码错误。咱偷梁换柱，做一个非常非常简单的降级流程。 OK 这里我给它返回一个什么呢？返回一个 error message 说你验证码输错了。好，但是咱是没有在电商项目当中集成验证码了。对不对咱这个撒谎也不能乱撒，所以我们做一个解释，咱是什么呢？模仿12306。咱不是自己瞎吹牛，咱是模仿12306。


好了，这个锅甩给了 12306 以后，咱的这个 comment 配置就已经完成了。同学们看起来这个洋洋洒洒是不是有那么点多啊？确实是的，你如果通过 high streaks command 在代码当中来配置，那其实看上去是有那么一点乱的。所以大部分情况下我们可能更倾向于在配置文件当中进行配置。


OK 那这里跟大家就展示了一个 hystrix command 在 Java 类当中的配置方式。同学们可以仿照老师这节讲的这个内容，在其他你看着不顺眼的方法当中给它加上去。比如说咱在上面的这个用户注册方法上，那同学们也可以在这边加一些 Hystrix 注解，去完成自己需要定制的熔断降级流程。这里拿 user 微服务只是跟大家抛砖引玉，咱这个 domain 包下面还有很多其他微服务的都等着同学们利用咱前面学到的知识，充分发挥主观想象力、主观能动性以及主人翁的意识，随心所欲的给各种方法添加熔断、降级线程、隔离信号量等等各种各样的手段。好勒。同学们，那这一节通过注解来配置 hi strikes 已经跟大家 demo 到这了。那咱下一节当中，再通过配置文件跟大家去把 high strikes 集成到我们的这个微服务项目当中。 OK 同学们，那我们下一节再见。

