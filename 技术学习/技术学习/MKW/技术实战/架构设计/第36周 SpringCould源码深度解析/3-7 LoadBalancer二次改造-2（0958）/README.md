---
title: 3-7 LoadBalancer二次改造-2（0958）
---

# 3-7 LoadBalancer二次改造-2（0958）

那么好，接下来我们去通过我们的调研测试，我们走一下通过 debug 跟踪一下这些关键的这些结，在这里面我们还是通过 test load balance 引起的方式进行一个执行。那么首先我们来这里面去进行debug，嗯，好，我们看第一步，在这里面执行到我们对应的这个 configuring register，也就是我们的一个注册器，那么基于这个注册器我们需要注册一下，当我通过了 load balance clients 或者说 load balance 进行修饰的这些 bin 的话，我们去这里面去执行。


那么好，那么我们现在去看一下这里面，我们看第一个是没有获取到，那么在这里面我们通过获取的 load balance，在这里面我们得到一个 client map，这个 client map 里面有三个值对应的，我们可以看一下它的内容，分别是config，也就是我们指定的我们配置的是 customer config。


另一个是我们的 name value，它对应的都是 next credit，这里应该是一互引用的关系，可以理解好，接下来看，如果说 name 不等于 null 的话，把它注入进，那么刚才我们已经看了这已经把它为注册进去，那里面的内容我们就不用再去信息的跟进了，这里面就是把它注册。


那么接下来我们跳过，我们看到下一步到哪，下一步这里面还是到这个 load balance，那么我们看一下这里面是什么呢？因为我们只是配置了一 load balance client，那么这里面对于 client s 它是谁配的？我们可以看一下，在这里面我们通过这里面的 trace 去看一下对应的一些内容，我们可以看到value，这里面对应的内容，我们看这里面能获取到它的 client 的集合，这个 client 集合是一个空的，我们这里面我们看获取到的是我们获取的是 defailed configuration，在这里面我们能得到这对应它的信息是我们可以看到 Meta date 里面的内容，这里面 Meta date 里面内容是指定的是 load plus auto configuration，这里面我们可以看到对应这个 load brands auto configuration。在这里面我们看到它，这里面使用到了，我们看一下这个类的实现 loadbands configure，这是， load balance config，那么在这里我们看一下这个bin，在这个 bin 里面是使用的 load balance plants，所以说它现在加载到这个 bin 会基于这个注解加这个 bin 它的一些配。


那么好，这里面我们看对于这 load badcase auto configuration，它的配置方式，它是获取认为是defailed，那么基于 defailed 的话，我们构造出一个b，那么这样我们它对应的name，我们可以看到它的 name 是defailed，对应上这个类的一个全路径名称它进行注册以及那么我们接下来跳舞下一步。


好，那在这里面我们看一下现在来的又是哪个bin，从这里面我们可以看到对于这个对应的 Meta date，我们看到它是 blocking load glass client a common auto configuration，那么我们在这里面我们去看一下，这里面是 block load balance client auto complication，那么在这里面看一下，这里面也是使用了 load balance client，那么同时它也是说明能找到这样一个对应的bin，同时效果一样的。我们看这也是把这个 bin 注册进去，对应的name，它是 defailed 对应的 blocking loadbus track account log application。好，那么我们接着去把它跳过，那么我们走到下一步，那么现在是这个，我们调，好，我们看现在是到了 create context 这个过程，也就是说我们创建我们这个负载均衡指定服务的一个纸的一个上下文。


那么这里面我们看到 name 的内容是什么呢？是 next provided，也就是我们当前的这个调用的服务，那么服务的名称我们基于服务名称首先创建了一个空的一个上下文对象，一个 notation config connect，一个bin，那么好，这样的话它会通过这个肯 configuration 去获取对应 neckles provided 的这个k，那么现在它肯定是可以获取到的。那么获取到以后他就把这个对应那个类，我们就会把它注册到我们 contact 里，我们可以看到对应这个类的一个结构，这里面我们看它的名称就是我们自定义的 customer load blanks configuration。好，那么我们接下来向下去继续，在这里面，它会把通过 defailed 开头的这些 b 音也注入进去，这里面我们看到它除了注册到我们定义的这个闭音以后，它还定义了一个 default config，也就我们默认的 load balance Claude configuration。


那么注册进去以后它会进行一个Refresh，把，同时把 bin 注册进去，那么在这里会进行Refresh，那么 Refresh 我们就把它执行跳过，那么好，那我们接着向下走，这样我们就获取到了对应的 service ID 为 nicos provided 这个服务的一个指容器。


那么我们通过这个止容器要做什么事呢？是啊， get bin 这个 bin 指定的type，我们可以看到这个 type 就是 react service intense load balance，那我们可以看到我们通过里面得到一个什么样的鼻音，在这里面我们看这里面指定了类型，好，最终我们得到了 load balance 的一个实例，这里面 active load balance。那么如果说在这里面做一些校验，那么接下来就相当于是我们已经获取到了对应的一些必应的实例，也就是说它最终是通过我们的 surface i 找到一个不同的子容器，通过这个不同的子容器去找我们对应的 load balance 的一个是最终的经过 load bands 的一个负载均衡的extra，获取到我们指定的这个 service intense 银行设立，那么这样的话，我们这个自定义负载均衡这个策略的一个工作原理就已经完成。


接下来我们看一下这里面是自定义 load balance 的 life cycle，那么我们先看一下这个接口，我们知道这个接口它是我们负载均衡生命周期执行的一个，首先这里面我们看它只有几一个方法。这里面首先support，判断一下当前这个请求是否支持，也就是这个负载均衡的 life circle 是否支持当前的请求。另一个是我们的 on start，也就是说我们确定这个请求开，这里面是 on start request 的，这里面标明一下我们请求执行到这里借。最后是uncomplete，也就是说我们看到在这里面我们有启动和启动请求和完成，但这里面并没有看到关于比如说失败，成功和失败的一个错误，其实这里面不管它成功和失败，它标明为完成，其实可以通过这失败的这个完成的状态去区分它是成功还是失。


那么我们来先看一下对于这个 load balance， life cycle 它能做什么事。嗯，在对于这个负载均衡的生命周期，在我们的 spring code load best 里面，它只有一个默认的实力。它默认的实例是什么呢？我们可以看一下，这里面是一个 make meter states， load balance left cycle，它做的事情主要就是对我们这些请求进行一个统，我们可以看到这里面当 on start 并没有做什么事情，这里面更关注的是 on start request，当我们请求过来的时候，他做的事情是什么？这里面我们看到它会构建一些指标，把这些统计指标构建出来，那么这里面我们可以看到它首先是 load Bison request active，也就是说活跃的请求这样一个指标，那么它会把这个指标进行记录下来，这样我们去统计我们这个负载均衡，它被调用的次数等等。


那么下面是uncomplete，对于uncomplete，它这里面关心的我们这个负载均衡，它执行成功还是失败还是取消，我们可以看到这里面对 completion context，它的 states 是一个状态，这个状态是成功失败和这样一个取消这样一个过程。


那么回到这里面，我们可以看到它会通过不同的状态记录不同的一个指标，那么在这里面我们看一下值，这里面是记录的是 load ByteDance， request discord 这样一个指标，下面是我们根据 failed 这是失败，最终后面还有我们是默认是success，那么如果说通过这种方式去记录指标的话，对于我们这个负载均衡的请求的这些结果会有一个更好的一个监控。


那么我们来看一下我们自定义这个做一个什么事情。在这里面我们制定了一个 load ballet life cycle，那么其实我们看了一下，需要根据我们的不同的业务场景来去区分我们做一些什么实现。那么在这里面我做的一个实现是非常简单的，我只是监听uncomplete，也就是它执行完成的消息，也就是执行完成的一个状态，当它执行完成以后，我去把执行完成的这个状态打印出来，具体它能是成功失败还是DISCORD。


那么这样一个结果其实当前对于我们来说不重要，我们更关注的是我们可以基于它来去嵌入的去完成这样一个工作。那么如果说大家在业务的过程中有一些更丰富的一个场景，比如说我们请求开始的时候我要做一个什么操作，那么请求完成以后再做一个什么操作，同时我去监听他成功或失败的状态，那么这样的话，我们可以通过 load balance lifecycle 这个切入点入手来去完成我们这样一个统计的一个。我们回到PPT，那么同学们，我们关于视频抽的 load balance 的二次改造的内容就先接到这里，同学们，我们下一章节再见。

