---
title: 2-4 用户模块- yml文件配置超时和熔断判定 
---

# 2-4 用户模块- yml文件配置超时和熔断判定 

[image](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/b244ca64-b65e-4123-b1c1-548fe2b4843a/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466S3S6LASD%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T225657Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCvUF5XOYwT3JYieaRJy3DRkW1um3nqi83NyFPNAXCSEwIhANhoTTsJz1c8PElUajueQGlAOuM%2BWFAi1gPg5oddm%2BzyKogECMb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgymvwamzHeyA8e6HC4q3AOxy2vK%2B9csa9ERyTozK9efMPDhV2kuFVbp1sVOxbflKut%2BAN0TfZRuFkx6LgfaTaNhxRfTs9z1prgFnEGlSoNwIYlUX3OTHq2mwLIszWkNjU2dzx3opfvgSar0Dr%2B1xCHYnWVRIX6GXIvLPXZ6pwakq8apOnHE2mikCaS2lohR9J4vN3iyrD7a6dBBsIrx9QnkZTL%2FP8FijQP%2F%2FenDgH3Cu6xrPo%2FPph%2BYY7TcETRV2W%2FiUW9Vk8fYXPgc0a8fym8TWzErdF79ufc3akcdh7wM9ftBSY1%2FSz7Yrbnbfuqr%2F1b4lWTmCGQDymt7R1kxPev9J76%2BIx6hH2jE7%2BfSgjyVBthVrSIc43RiEwC1cgt3DslDPmpINPAfeaMbPQCWrGZonv5KCzb7bNlhWhRsXQgqOsgLf%2BmYf6%2BtS%2F%2Fqpp8A1ouv6LCjyx1Hk656Hq77m8rfviVmFDHeTJe%2B8KbwBhxPydsdyOspi4xfdZWq8TcwewvW5T%2BLgCD2LZZHzb3pZ8d8Rn%2BeOhR6jWwifiRwrWILuRdFBlDZuCRcRlljq4AVzRcmRd1Htw3TLkT4rsoMD0kdumtYNGEdJHKPB%2FPv71TuTDwfRFAREAQNDK67dD5TpL%2BjGeRhudAZg%2BSZaTC2uP%2FSBjqkAdVn1Vmv5ndYMzeyOXEczPVdBREPhN%2BFNR1Q4Fw5NBSv%2FFPPw1gXMWE8lTeMrN8cVk5p9Arv%2FBIzHanJoYXNwCh0ViNP40gqFm0pv5fsqr6eRMS1m1N8Pe8D0VAmlYvgVl8mz1Us2vT6s3OnhjkcqT1AkDap0TUFLCosBAUY7T6jA6fsgRd9jhZaQ4QVjkVyTsHsrQUpHGuujH71pfj83Y2L23AR&X-Amz-Signature=98e683cf90d30c2fd1f77054de43183ec26c2a86aa0d06b3dce0ef9b851485f9&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

[image](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/243e98e0-daea-47b2-86d6-e1808bfdd5d9/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466S3S6LASD%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T225657Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCvUF5XOYwT3JYieaRJy3DRkW1um3nqi83NyFPNAXCSEwIhANhoTTsJz1c8PElUajueQGlAOuM%2BWFAi1gPg5oddm%2BzyKogECMb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgymvwamzHeyA8e6HC4q3AOxy2vK%2B9csa9ERyTozK9efMPDhV2kuFVbp1sVOxbflKut%2BAN0TfZRuFkx6LgfaTaNhxRfTs9z1prgFnEGlSoNwIYlUX3OTHq2mwLIszWkNjU2dzx3opfvgSar0Dr%2B1xCHYnWVRIX6GXIvLPXZ6pwakq8apOnHE2mikCaS2lohR9J4vN3iyrD7a6dBBsIrx9QnkZTL%2FP8FijQP%2F%2FenDgH3Cu6xrPo%2FPph%2BYY7TcETRV2W%2FiUW9Vk8fYXPgc0a8fym8TWzErdF79ufc3akcdh7wM9ftBSY1%2FSz7Yrbnbfuqr%2F1b4lWTmCGQDymt7R1kxPev9J76%2BIx6hH2jE7%2BfSgjyVBthVrSIc43RiEwC1cgt3DslDPmpINPAfeaMbPQCWrGZonv5KCzb7bNlhWhRsXQgqOsgLf%2BmYf6%2BtS%2F%2Fqpp8A1ouv6LCjyx1Hk656Hq77m8rfviVmFDHeTJe%2B8KbwBhxPydsdyOspi4xfdZWq8TcwewvW5T%2BLgCD2LZZHzb3pZ8d8Rn%2BeOhR6jWwifiRwrWILuRdFBlDZuCRcRlljq4AVzRcmRd1Htw3TLkT4rsoMD0kdumtYNGEdJHKPB%2FPv71TuTDwfRFAREAQNDK67dD5TpL%2BjGeRhudAZg%2BSZaTC2uP%2FSBjqkAdVn1Vmv5ndYMzeyOXEczPVdBREPhN%2BFNR1Q4Fw5NBSv%2FFPPw1gXMWE8lTeMrN8cVk5p9Arv%2FBIzHanJoYXNwCh0ViNP40gqFm0pv5fsqr6eRMS1m1N8Pe8D0VAmlYvgVl8mz1Us2vT6s3OnhjkcqT1AkDap0TUFLCosBAUY7T6jA6fsgRd9jhZaQ4QVjkVyTsHsrQUpHGuujH71pfj83Y2L23AR&X-Amz-Signature=f9a175359b5265317491a99df815de9863f4997a4a8befff152fcbb5ad38063b&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

课后，各位同学们，大家好，咱在上一节当中看到了这种非常复杂看起来非常污染代码的 high strikes command 形式的配置。那咱这一节跟大家换个口味，换一点小清新的。咱把这个配置项从 Java 代码里给它通通抽出来，放到哪放到咱的 YAML 文件当中来做一些熔断降级的配置。 OK 那我这里先找到一个 application DEV YAML 文件，它依然是选择 foodie user web 也就是用户微服务模块当中的这个配置。好，我们在这里通过 YAML 的形式把咱需要用到的熔断降级的一些属性全部都给它配置出来。好这里留大一点空开始操练起来。那第一个节点就是 high streaks 接下来是一个 command 节点。然后下面我首先要给它添加一个全局的配置，也就是 default 配置。那咱这里是对全局所有 high strikes 监管的方法来进行配置的。那后面我们还会对某个指定的方法做特殊的配置。好，那这里我们先把默认配置给它选上。那 default 节点下面我们第一个先把它的 fallback 给打开， fallback 是不是 enable 的，这个打开没打开，我给它写成 true 那在这个 default 节点下，我要加一个醒目的标识，告诉大家有的属性是默认指，也就是说它并不需要特殊指定，那写不写都行。那这里全部给他写上，是为了教学的目的，而让同学知道在这背后都有哪些属性可以操作熔断降级的开关以及它的具体参数。


OK 那接下来这个 fall back 配置完，非常简单。那下面我们接着自然要配置它的进击版，也就是熔断。你这个错误错多了，降级多了，咱就要走到熔断里面。 OK 好，熔断这里依然第一个属性，我先给它配置一个 enable 把这个熔断开。然后下面我配置这里面最关键的一个阈值，也就是你判断这个熔断是否开启的一个关键参数叫 error threat hole percentage 那我这里把这个 percentage 配置到50，也就是说你超过 50% 错误。那么开启熔断好勒，在线上环境里这个 50 可能还设置的有那么一点高，我们通常可以设置到三十四十这左右就可以了。因为当你一个服务 50% 的错误率已经是一个比较恐怖的数字了。那已经可以断定这个线上服务的健康度肯定是出了一些问题，那就要人工去介入排查。所以说我们尽量把这个值在线上环境当中，给它设置的稍微低一点，但是也不能太低。百分之三十三十五都是相对来说还比较恰当的数值。


那接下来的这个属性跟熔断也有很大的关系。前面我们也讲过叫 request volume stressfulok 那我这里把它设成 5 好了。 OK 那它这个意思就是说当五个 request 之后才进行统计。


OK 前面带同学们阅读源码的时候也读到过，它是参与熔断开关是否开启这个判断的一个条件。如果你的访问请求没有达到五个，即使你这前面的四个全部都错了，那我依然不开启熔断开关。那只有达到五个之后我才去开始计数。那接下来的属性是跟状态恢复有关了。你开启了熔断之后，我多少秒之后进入半开 sleep window in milliseconds OK 我这里给它设置大概 10 秒钟的时间。 OK 我这里备注一下，10秒之后进入半开状态。那大家还记得，控制熔断开关的还有两个参数，那这两个参数不要轻易的打开，非常的暴力，一个是 false closed 那还有一个是 false open 那这两个参数分别是代表着强制关闭以及开启熔断开关。 OK 好，咱这个熔断就先配置到这里。那接下来我们配置一个执行参数执行参数 execution 好，在下面，我们先配置这个 time out 那 time out 开公安是什么？ enable 等于 true 好，那接下来我们来配置它的隔离方案的具体参数。


OK 咱的 isolation 隔离以什么方式呢？线程的方式。 OK 除此以外其实我们这里还可以配置一些额外的参数，比如说可以指定隔离方式是线程池还是什么，还是咱前面学过的信号量。那这一个部分，同学们可以自己去从它的源码或者是文档上面去了解道理都是相通的。那我们这里如果你不指定默认，当然就是使用线程池 thread 的方式了。


那接下来两个配置都是在特定的状态下是否取消当前线程，一个是 interrupt on timeout 也就是超时的时候是否终止线程，我这里给它指定 true 那另外一个和上面的这个参数是一样的，它是 interrupt on future cancel 在取消的时候是否终止线程，那我这里也给它指定 true 好，它这两行配置和咱之前的 demo 都是完全一样的。


OK 那接下来一个比较重要啦，是一个全局默认的 time out in many seconds 这就是 high streaks 的 time out 配置。那同学们在设置的时候要和 thin 有所区分，因为咱这里是 user 服务， user 为服务里面没有对远程服务的调用。所以这里没有配置 fin 的超时时间。


如果咱在 order 这个微服务当中实现 high streaks 我们前面说过，你要注意 high streaks 的超时和 fin 超时它之间有一个相互作用以这两者中的低者作为超时的判定。那我们前面 fen 和 ribbon 这里可以设置重试对不对？那有的服务你可能设置了三次重试，但是你会发现三次重试它所能达到的最大超时时间要高于 high streaks 配置的超时时间。比如说我这里配置了 4000 毫秒。那如果你每次在份和瑞顿的重试设置的超时次数比如说是 3 次，那它的超时时间是 2000 毫秒，那 2000 乘以 3 就是 6000 毫秒。那也就是说你 high streaks 没等到你 phone 进行第三次重试，那它这里就直接走到了熔断的流程。所以这两个配置在具体的项目当中要稍微留心一下。


OK 那我这里给他 high streaks 的，默认超时时间稍微设置长一点。好了，这里就照顾一下大家电脑性能不好的同学了，给大家设置的稍微长那么一点。除了这些配置以外，通常情况下我们还会配置一个metrics 。那 metrics 下面有两个相对比较重要的子节点，一个是 rolling states 好，它这下面第一个比较重要的参数就是叫 timing millet seconds 那我这里比如设置个 2 万。


好了，那它实际上是断路时间窗口。 OK 我这里加上时间窗口统计，那 high streaks 这里只会维持这段时间内的统计结果。那除了这个属性之外，还有一个滑动窗口的计数。那我们最好配置的时候，这个滑动窗口技术要能被上面这个数整除掉，它默认的是10，那我们可以给它改成二十，三十都可以。但是最好可以让它被上面的时间窗口给它整出。这样的话，我的滑动窗口就可以在我指定的时间窗口内均匀的分布这么多个统计桶了。 OK 我这里先把它注释掉。


那当然除了这个配置以外，我们还有一个跟 rolling states 同级别的一个叫 rolling percentile 百分位计数。那它下面的属性跟咱上面的 rolling states 比较相似。那它这里同样也有一个 timing many seconds 也有这样一个统计。 OK 那除了这个以外，依然也有这个统计统的个数。


OK 那除了桶的个数之外，它还有一个桶的 size 那它名称叫 bucket sizeok 如果咱们 bucket size 设置成打个比方设置成300。好了，那意思是说在你过去的这个 2 万毫秒，也就是 20 秒内。如果你这边有 500 个请求，那我这里只记录最后 300 个，那它的默认值我记得好像是100。


OK 那如果我们不指定，其实在 high streaks 大部分的参数都会给定一个默认值。同学们在自己项目中根据自己的业务以及需求，那来制定一个符合自己的这个熔断降级的配置。好，我这里把这几个配置先给它注释掉下面这个 rolling percentok 那这里我们配置的是一个 default 也就是全局生效的属性。那如果我想对我指定的一个方法来配置，这里怎么办呢？打一个比方，我就想给刚才在前面小节里我们去定制的这个 passport controller 当中的这个 high strikes command 来进行定制，怎么办呢？很简单。我们前面不是定制了一个 command key ，对不对？那这里就派上用场了。好，我们把它复制一下，接着转头回到 application DEV 当中，往下走，往下走。


好，走到这里。那我们再与 default 全局配置节点相同的缩进行数，这边添加一个 locking feel 好，我们对 locking feel 做一些特定的配置，咱前面全局的 default 配置属性都会在下面生效。但是如果我想对某一个属性进行特殊的更改，那很简单，我只用把这个属性给它揪出来就行了。比如说我想对他的这个超时时间改一下，这十秒钟对我太长了，我这个方法短小精悍，超快猛，我想给他改一下，怎么改很简单。好，我们把这一段需要更改的属性直接给它拿过来，这个缩进控制好，把超市时间单独留下。你小子放学不要走，给我留下来。这个 1 万毫秒十秒钟，我把它稍微改一下，改成个 3 秒钟。 OK 就这么简单，那你就实现了对特定配置属性的 override 重载。好，那我们依然可以去照这个方法怎么样去覆盖其他的属性。


OK 那同学们会问了，如果我的方法上面没有声明这个 command K 怎么办呢？前面我们说过如果你没有声明这个 command K 那只要你有 hystrix command 那它会自动给你指定一个 command key 那这个 command key 的值是什么呢？我们不妨打开 high streaks command 节点来看一下。

```java
hystrix:
  command:
    # 有的属性是默认值，写不写都行
    default:
      fallback:
        enabled: true
      cicuitBreaker:
        enabled: true
        # 超过 50 % 错误，那么开启熔断
        errorThresholdPercentatge: 50
        # 5个request之后才进行统计
        requestVolumeThreshold: 5
        # 10秒后进入半开状态
        sleepWindowInMillseconds: 10000
      execution:
        timeout:
          enabled: true
        # 可以指定隔离方式是线程池还是信号量
        isolation:
          thread:
            interruptOnTimeout: true
            interruptOnFutureCancel: true
            timeoutInMillseconds: 10000
      metrics:
        rollingStats:
          # 时间窗口统计
          timeInMilliseconds: 20000
          # numBuckets: 10
#        rollingPercentile:
#          # 时间窗口统计
#          timeInMilliseconds: 20000
#          # numBuckets: 10
#          bucketSize: 300

# 对特定配置属性的 override 重载， 照这个方法去，去覆盖其他的属性
# 如果我的方法上面没有声明这个 commandKey 怎么办呢？  @HystrixCommand 那它会自动给你指定一个 commandkey 那这个 command key 的值是什么呢？默认使用方法名
    loginFail:
      execution:
        isolation:
          thread:
            interruptOnTimeout: true
            interruptOnFutureCancel: true
            timeoutInMillseconds: 10000
```


他这个注释上说了 default 指定的默认值，就是咱这个方法名默认使用方法名，所以说你这里即使没有指定 command key 那你把这个方法名在配置文件中指定出来，也是一样的效果。那有的同学们会问了，如果我方法名一模一样，那怎么办？方法名一模一样，那你肯定方法的参数签名不一样对不对？还记得咱在前面随堂 demo 当中使用过的一种方法，当使用 phone 的工具类可以怎么样呢？可以把一个方法它的签名给它打印成一段字符串，那这段字符串就可以唯一的定位到一个 high streaks 托管的方法当中。那这段方法签名就包含了类名、方法名以及它后面的这些参数的类型，你就可以把它当做是 command K 来配置进来。


OK 那如果同学们已经淡忘了这一块的知识，不妨翻过去回头看一下咱的随堂 demo 视频。 OK 同学们，那到这里，我跟大家就示范了一个 user 微服务下面的 hystrix 配置，那这里面留给大家的作业时间又到了，我们还剩下很多个其他的微服务，那这些微服务都等着同学们去大展拳脚了。所以说我们的这个微服务课程是一个给同学们留足了想象空间的课程。我们可以根据自己的理解自己的业务使用 spring cloud 当中学到了组件，将这些组件配置应用到自己的业务当中。


好，那我这里就跟大家留一个作业了这个作业是什么内容呢？叫根据业务配置 high strikes 这里还有一句鼓励语叫随意发挥。好勒。那同学们这一节就跟大家先告一段落了。那下一节里，我将带大家一起去看一下 ven 托管的这个服务配置服务的降级熔断是个什么样的流程。这里我将要跟大家介绍一些和咱前面随堂 demo 当中不一样的配置方式，以及我们在对 phone 的接口指定降级策略时候一些约定俗成的一些惯例。 OK 同学们，那我们下一节再见。


