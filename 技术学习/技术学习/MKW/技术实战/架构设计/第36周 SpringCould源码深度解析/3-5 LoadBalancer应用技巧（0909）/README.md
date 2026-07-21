---
title: 3-5 LoadBalancer应用技巧（0909）
---

# 3-5 LoadBalancer应用技巧（0909）

我们对同学们，大家这章节给大家介绍一下 spring Claude load balance 的一些应用技巧，那么首先我们来看一下关于我们的 rest template，那么我们在使用 rest template 的时候，我们使用上对应的 load balance 的这个注解，那么我们就可以让 rest template 让它支持一负载均衡，那么我们有没有想过这种操作是怎么完成的？为什么我们再加上 load balance，它就能让 rest 他们的达到一个这样复转均衡的效，这样我们可以去深入的去了解一下它是怎么去实。


首先我们来看一下这个 rest template 构建的过，在 spring Claude load balance 里面它做了一些工作，首先我们对一个 reset template 它是做了这样一个处理，对于我们瑞斯template，如果说它使用了 load balance 的作为注解的修饰，它在自动装配的过程中通过 rest template cost 去自己定义一个什么呢？它通过 rest template 执行的过程加一层拦截器，也就是 load balance intercept，这个拦截器做的工作，也就是说在执行之前通过 load balance 卡尔的获取一下我们负载均衡的列表，那么其实这里面它会对于我们如此他们这个执行过程的 URL 进行解析，把对应的 host 获取出来，通我们负载均衡的获取策略，根据这个 safest ID 去找对应一指定的 host 和对应的端口，那么这样的话它就可以达到了一个负载均衡的效果。


那么现在我们来可以看一下源码，它是这个怎样执行的过程好，还是切换到我们的负载均衡的这个演示model。在这里面我们可以看到我们这定义了两个 reset template，一个是基于负载均衡的方式，一个是不只是负载均那么好，那么我们现在去看一下它执行的，在这里面我们先把代码简单过一下。


对于这里面的 load balance auto configure，我们可以看到在我们在启动的过程中，它首先这里面会构建一 rest template customer，也就是通过它这个自定义的一个配置去执行一些超，我们看一下它的实现，它的实现也就是在这里面它定义也就是在我们 rest template 里面设计一些拦截器，这个拦截器的内容是 load balance intercept，那么我们看一下 load balance intercepts 它是怎么构建出来的，也就是上面这里面有定义 load balance intercepts 的过。


那么对于这个 load balance intersep 的这个拦截器，它做的事情是什么呢？我们可以跟进去看一下，在这里面它进行在拦截器操作的过程中，也就是在真正的执行之前，那么执行之前它做的事情就是我们看这里面是首先获取到我们的请求，那么根据我们的 URI 获取到对应的host，那么先判断一下这个 service name 是否存在，如果说是它是一个纯栈，那么我们直接执行 load balance 的 execute 就是让它给自在。


这里面我们看它注了一层替换，也就是说把原来的host，也就是我们的 request 对应的URI，它替换成了 service name，那么通过 load balance 的方式进行执行，那么后面执行的过程就跟我们原生的用 load balance 进行负载均衡的操作就没什么区别了。


只是在这里面我们通过 rest 对应的这个 request 请求，我们构造成了一个对应我们的loadbison，一个请求注入了一层包装，那后面的逻辑就是类似的，那我们看那这个拦截器它最终是怎么去执行到的？我们还回到我们的 load balance auto configure，我们看到在这里面它通过 rest template customer，那么进行这个罗德拜斯它这个拦截器的一个注册，那么我们看一下这个 customer 是什么时间去执行的，看这里面是 smart ins， lesson single，那么它这里面做的事情是什么呢？我们仔细看这里面，也就是说它首先会把我们这个 reset time 的 customer 一个自定义器，它去进行一个遍历，那么对于所有的 customer 进行一个处理，它首先是对 reset template 这个列表进行一个遍历的去进行一个 customer 处，这里面我们看一下对于这个 research template，它这个列表是怎么获取到这个列表是获取当前这个对象里面的这个属性。


rest template 就是说它获取的是 rest template，这里面我们看到这里面是用的是 out where 有制动，它把整可以理解为是整个容器里面的 research template 进行注入，进来，注入成一个链，当然我们看到这里面会有一个修辞符，这里面 at load balance 的，但它是什么意思？我们可以想，当我们在这里面能搜集到的这个 rest template 列表，那么它就可以把我理解为是我们这个拦截器跟它驻车厂。


那么我们需要关注的是这个 rest time list，对于他来说，我们可以看到我们这里面的一个配置，那么我们有 rest template 和这两个 research template，一个是有 ad load balance 的，一个是没有的，那么它在这里面的一个注册的方式有什么区别？我们可以看到这个 ad load balance，它的这个注解的一个元数据，我们可以看到上面，我们就不关心了，这是target，它可以在我们的属性和我们的 parmeter 和 mast 都可以去死，那关键是我们看到这里面的qualify，那么它是什么意思？我们可以理解为它是一个对于我们闭眼注入一个修辞，也就是说它一个限定符，那么说这个限定符我的逻辑我们可以理解为只有我们在 rest template 定义这个闭幕的过程中，使用了 ad load balance，那么它才可以注入到这里面。所以说在这里面对于这个自动注入的过程中，我们这里面虽然定义了两个 reset template，那么只有它能注入进来，而它是注入不进来的。如果说它能注入进来，所以说在这里面一些执行的过程中，也就是只有能注入进来基于 at load balance 的这样一个 reset template，它才可以把这个拦截器加载进去，所以说这样也就是说只有我们能注入了我们这个拦截器，那么它的负载均效能才能升。


那所以说我们可以看只有在我们定义的过程中，使用了 ad load balance 的，那么这个 rest template 它才能生效它的负载均衡的撤，这是我们能理解了为什么我们配上这个注解，它就可以支持负载均衡，那么我们现在去执行一下，我们看一下执行负载均衡的效果它是怎样的。


好，那么我们现在我们执行这个单元测试。好，我们现在 debug 执行。好，我们看执行的过程中先执行它一个初始化的过这里面，首先我们看这里面是构造我们这个负载均衡的拦截器，那么我们跳过，好，接下来我们到了通过这个 rest template customer 定义如何把这个负载均衡的拦截器注入到我们的 rest template 上面。我们继续跳过，那么现在我们是通过 smart initiation single 进行把这个注入的执行完成，它其实也就是在我们当程序我们的 BN 初始化完成以后进行的一个后处理。好，现在到我们的方法，也就是说这个初始化过程已经完成了，接下来执行我们负载均衡的一个操作。


那么我们看呀，首先它，嗯会执行 get object，我们看一下我们这个URL，我们 URL 是基于 service ID 去注册，那么我们跟进去，我们看这里面我们的对应的 URL 是 SP nicos provide 对应，我们其实最终会把这个负载均衡，我们 service ID 换成对应的 IP 和URL。


好，我们继续跟进去，在这里面我们进去好执行，我们看这里面我们得到了一个 URI expand，这里面我们看到它的内容，我们接着跟进去，好。在这里面进行 request 操作。其实整个过程它还是一直跟进来，我们看直到我们在执行这个的过程，它获取到构建出一个我们一个拦截器的一个链，基于这个拦截器链来进行一个处理，我们继续跟进来。好在这里面我们可以看到我们基于拦截器链来进行一个一个获取。好，我们在这里面看这现在我们得到了我们的拦截器，这个拦截器，那么这个拦截器是什么呢？我们看这个拦截器就是我们的负载均衡的拦截器，我们跟进去看一下，在这里面它通过我们的请求对象获取到URI，那么通过 URI 的 host 得到这个 service name，那么然后基于这个 service name 进行我们 load balance 的一些处理，那么这样它执行的过程就是跟我们刚才介绍的 load balance 去执行负载均衡策略是一样，那么我们跳过断点，现在执行完成。


好，现在我们执行完成，我们看能获取到我们正常的一个输出的一个结果。好，那么回到我们的PPT，这是我们的介绍，我们的 rest template 和 load balance 的相关的一些内容。

