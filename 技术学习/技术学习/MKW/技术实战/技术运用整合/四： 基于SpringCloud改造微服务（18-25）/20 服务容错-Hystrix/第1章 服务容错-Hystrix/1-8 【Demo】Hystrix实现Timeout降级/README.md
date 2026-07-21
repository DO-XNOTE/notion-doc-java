---
title: 1-8 【Demo】Hystrix实现Timeout降级 
---

# 1-8 【Demo】Hystrix实现Timeout降级 

[image](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/9f3842d3-8480-49bf-a29b-f51ab2d66347/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466W2GK547L%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T225637Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCBnUkCXfgH0CLuRcP%2BfkCWu0JsEMMPssyzZvZSqqWBjQIgGqLXvvmfzaD3w1UU09%2BMENqzyqn58akisoRZPFu8vDAqiAQIxv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDEE1yP5wVv3bpdU0eyrcAwzN1bLed6d6%2FW%2BNRhcWDk4j7VbkooV3nH7bO3nzu35hVpxeM4wXDkfIaMWmL%2FXHx%2BOKemjE%2FIoyb%2FHTENJAsiQlhsct3HYVil3owayPAhPmbsGOgtl2HoAI%2B%2FIk4ThgFsqQdFndfj9O6a1kke9KvNLoi8Upt4Yp06LWtO309mcAS1dq%2FubQq8CUwzTamZYEqWK%2Fw3QWBd%2B4qzxMvhYtw2utyZpRf91XOCKfBnnMhL%2Fc4vgziwZ8UcTgwzQaMsZWcMfLI2ZX1pa22b6bLXd02H3QF%2BnnR7WV7iGLohcymk8bbJ%2FfUKDwXM9eIJiy7UFHajZljILbz60uxvGkSCUa4ZjDbGoAQJId%2B%2FJLsWg70XGnDf2tKGjTkCb4chYtbZX64CYJyr12Ks63yLb%2FDivlzon0jsm0kwGxM3SMmtG8L5MLjuketT68K2TUh3iSOAiSNrEXS%2BLsYVc5oFVPHLiiAcBB9MAJ7hzlWKpWaEyzAWDl7ZKVV9NTHOHqYq3U6Q9Iw5Ou93eqEg0tmeP0PAD1kpcbAgQtQMmf%2F9ifdFKCKVfY6ZZL%2F8W%2FJ%2BKvo2LP3v%2BT%2BzexS%2Bk6BO0hk8gyd8TzPVvDI1nFzrsJgRO%2FAwI1i3lXTHljSh%2Fb0y8yxbBOMJ%2B6%2F9IGOqUBWJ96cUD0lpYDoHnz%2B4xZS2GQz3aWsKpTI1g9mYJE5GHEM0FFNA%2FKmNokxDOLScvXUE3jkTO3ToAXKCfIEhtvXe4xrnVmUOBe67rdPJC%2FVeLzyQnM8ixeREjqYDNhL%2FXqMUu1neOB7AMU4nfirizhQ2455fH3b6ekm8qaSJr2FraprxYjSQEZXeaBFJ%2FBIbbFTqlw01bIYjUpm0LX4ZU2pcyAw%2FJx&X-Amz-Signature=4c9f39e0be5ef52b6f70250bd656ee4fe03872f39a6cf477467aeaf057c98a7f&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

[image](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/98b2bc79-8870-4a41-adf0-eb9abb6f679e/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466W2GK547L%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T225637Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCBnUkCXfgH0CLuRcP%2BfkCWu0JsEMMPssyzZvZSqqWBjQIgGqLXvvmfzaD3w1UU09%2BMENqzyqn58akisoRZPFu8vDAqiAQIxv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDEE1yP5wVv3bpdU0eyrcAwzN1bLed6d6%2FW%2BNRhcWDk4j7VbkooV3nH7bO3nzu35hVpxeM4wXDkfIaMWmL%2FXHx%2BOKemjE%2FIoyb%2FHTENJAsiQlhsct3HYVil3owayPAhPmbsGOgtl2HoAI%2B%2FIk4ThgFsqQdFndfj9O6a1kke9KvNLoi8Upt4Yp06LWtO309mcAS1dq%2FubQq8CUwzTamZYEqWK%2Fw3QWBd%2B4qzxMvhYtw2utyZpRf91XOCKfBnnMhL%2Fc4vgziwZ8UcTgwzQaMsZWcMfLI2ZX1pa22b6bLXd02H3QF%2BnnR7WV7iGLohcymk8bbJ%2FfUKDwXM9eIJiy7UFHajZljILbz60uxvGkSCUa4ZjDbGoAQJId%2B%2FJLsWg70XGnDf2tKGjTkCb4chYtbZX64CYJyr12Ks63yLb%2FDivlzon0jsm0kwGxM3SMmtG8L5MLjuketT68K2TUh3iSOAiSNrEXS%2BLsYVc5oFVPHLiiAcBB9MAJ7hzlWKpWaEyzAWDl7ZKVV9NTHOHqYq3U6Q9Iw5Ou93eqEg0tmeP0PAD1kpcbAgQtQMmf%2F9ifdFKCKVfY6ZZL%2F8W%2FJ%2BKvo2LP3v%2BT%2BzexS%2Bk6BO0hk8gyd8TzPVvDI1nFzrsJgRO%2FAwI1i3lXTHljSh%2Fb0y8yxbBOMJ%2B6%2F9IGOqUBWJ96cUD0lpYDoHnz%2B4xZS2GQz3aWsKpTI1g9mYJE5GHEM0FFNA%2FKmNokxDOLScvXUE3jkTO3ToAXKCfIEhtvXe4xrnVmUOBe67rdPJC%2FVeLzyQnM8ixeREjqYDNhL%2FXqMUu1neOB7AMU4nfirizhQ2455fH3b6ekm8qaSJr2FraprxYjSQEZXeaBFJ%2FBIbbFTqlw01bIYjUpm0LX4ZU2pcyAw%2FJx&X-Amz-Signature=880be86fc67b595b7d944e273ef97c60b10f297f58f740dce188d6320becd94c&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

[image](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/9e2f2007-9541-4925-95b4-f9512d78b579/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466W2GK547L%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T225637Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCBnUkCXfgH0CLuRcP%2BfkCWu0JsEMMPssyzZvZSqqWBjQIgGqLXvvmfzaD3w1UU09%2BMENqzyqn58akisoRZPFu8vDAqiAQIxv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDEE1yP5wVv3bpdU0eyrcAwzN1bLed6d6%2FW%2BNRhcWDk4j7VbkooV3nH7bO3nzu35hVpxeM4wXDkfIaMWmL%2FXHx%2BOKemjE%2FIoyb%2FHTENJAsiQlhsct3HYVil3owayPAhPmbsGOgtl2HoAI%2B%2FIk4ThgFsqQdFndfj9O6a1kke9KvNLoi8Upt4Yp06LWtO309mcAS1dq%2FubQq8CUwzTamZYEqWK%2Fw3QWBd%2B4qzxMvhYtw2utyZpRf91XOCKfBnnMhL%2Fc4vgziwZ8UcTgwzQaMsZWcMfLI2ZX1pa22b6bLXd02H3QF%2BnnR7WV7iGLohcymk8bbJ%2FfUKDwXM9eIJiy7UFHajZljILbz60uxvGkSCUa4ZjDbGoAQJId%2B%2FJLsWg70XGnDf2tKGjTkCb4chYtbZX64CYJyr12Ks63yLb%2FDivlzon0jsm0kwGxM3SMmtG8L5MLjuketT68K2TUh3iSOAiSNrEXS%2BLsYVc5oFVPHLiiAcBB9MAJ7hzlWKpWaEyzAWDl7ZKVV9NTHOHqYq3U6Q9Iw5Ou93eqEg0tmeP0PAD1kpcbAgQtQMmf%2F9ifdFKCKVfY6ZZL%2F8W%2FJ%2BKvo2LP3v%2BT%2BzexS%2Bk6BO0hk8gyd8TzPVvDI1nFzrsJgRO%2FAwI1i3lXTHljSh%2Fb0y8yxbBOMJ%2B6%2F9IGOqUBWJ96cUD0lpYDoHnz%2B4xZS2GQz3aWsKpTI1g9mYJE5GHEM0FFNA%2FKmNokxDOLScvXUE3jkTO3ToAXKCfIEhtvXe4xrnVmUOBe67rdPJC%2FVeLzyQnM8ixeREjqYDNhL%2FXqMUu1neOB7AMU4nfirizhQ2455fH3b6ekm8qaSJr2FraprxYjSQEZXeaBFJ%2FBIbbFTqlw01bIYjUpm0LX4ZU2pcyAw%2FJx&X-Amz-Signature=b0366b985a3a3104a14edf1cb2ad7f7dc095531dc10d43508cb6866506fba666&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

某木客网的各位同学们，大家好，中场休息已过，我们又回到了工作岗位这一小节，我们来看一下如何对 high strikes 配置 time out 属性好。前面写分的时候，大家是不是还记得我们实现过一个超时接口，准确的说它并不是超时，而是说你告诉我跑几秒我就跑几秒，也就是这个 retry 接口它做一件什么事情呢？它会根据你传入的 time out 的时间，也就是具体的秒数。在方法中使用 thread sleep 方式挂起线程，直到当达到了你所设定的秒数以后才返回一个结果。


那么我们正巧可以利用这样的一个机制来测试我们的超时请求对不对？好，接下来咱回到哪里 controller 里，我在 controller 里创建一个方法，你看这个 controller 里创建的方法都是一些很负能量的方法。前面一个叫 fall back 咱这个方法给它起名叫 time out 好吧，好吧，不管它了，这里 time out 的路径我也依然给它设置成 time out 同时接受一个什么属性呢？接受一个 long 型的 time out 的实际描述，然后调用谁调用 my service.retry 把这个秒数传入进去。 OK 这就大功告成了吗？你看他又不领情。


hands 是个 integer 果不其然，难道这就完成了？ no no no 我们要到 fall back 逻辑里面，给这个 retry 函数动一点手脚。既然它已经超时了，我们给它返回的就叫 you are late 千万不能被女孩子说 you are late ，尤其是在约会的时候，我约会都要提前半小时去踩点。写完这个 retry 还不够，你这里调用它，它依然会等到返回结果。


因为为什么我们没有做怎么样超时配置对不对？那接下来回到 application 里面，咱给它配置几个属性，先配置一个全局的超时配置好不好？它叫什么名字，我们先给它加一个注释全局超时，它的属性名叫 high strikes.comment 再点 default.execution 这个 execution 执行的意思后面是什么？

```java
spring.application.name=hystrix-consumer
server.port=50000
spring.main.allow-bean-definition-overriding=true
eureka.client.service-url.defaultZone=http://peer1:20000/eureka

# 开启 Feign 下面的Hystrix功能
feign.hystrix.enabled=true
# 是否开启服务降级
hystrix.command.default.fallback.enabled=true

# 全局超时
hystrix.command.default.execution.timeout.enabled=true
# 超时时间
hystrix.command.default.execution.isolation.thread.timeoutInMillisecond=2000
# 超时以后终止线程
hystrix.command.default.execution.isolation.thread.interruptOnTimeout=true
# 取消的时候终止进程
hystrix.command.default.execution.isolation.thread.interruptOnFutureCancle=true



#===============Ribbon 超时的的时间配置
# 每台机器最大重试次数
feign-client.ribbon.MaxAutoRetries=2
# 可以在重试几台机器
feign-client.ribbon.MaxAutoRetriesNextServer=2
# 超时连接
feign-client.ribbon.ConnectTimeout=1000
# 业务处理超时
feign-client.ribbon.ReadTimeout=8000
# 在所有的Http Method 进行重试
feign-client.ribbon.OkToRetryOnAllOperations=true
```

 time out.enabled 给它设置为 true 同学们这里可能就体现出 YAML 和 practice 配置的不同之处了。如果它是一个 YAML 配置，相对来说你会少写很多的字。但是我个人觉得实际上 practice 似乎比 YAML 更加直观。那么一点各有利弊，大家凭个人的喜好喜欢哪一种，就配置哪一种。网上有很多小工具可以帮你把 properties 文件转成 YAML 或者把 YAML 文件转成 properties 这都不是问题。那全局配置我们打开了以后，那接下来就要配置什么？接下来就要针对这个全局配置添加一个超时的实践。


我把前面这一串字给它 copy 下来， copy paste 后面可就不一样了。叫 isolation.thread 再点 time out in mainly seconds 也就是以毫秒为单位的。那我们给它的超时时间配置成两秒好不好？ OK 配置完超时时间以后，我们还要给他配置一些什么呢？一些超时的行为。那什么行为？ OK 我们这里来看一下它的配置项，同样的把前面这一大串长字都给它 copy 下来。


haste 完事以后，后面一个属性不同喽，它叫 interruptinterrupt 什么意思呢？打断 interrupt on timeoutok 这里是个 true or false 的，指它叫什么含义呢？它就定义了超时时候的行为，超时以后怎么样暂停线程就是打断线程，终止线程。中文的表达方式好灵活。


OK 那除了这个属性以外，其实还有一个跟线程终止有关的属性，它叫什么呢？它这里叫 interrupt on future cancel 真是五花八门，什么都有。 future cancel 有什么鬼呢？那就是说顾名思义它实际上就是指取消的时候终止线程。这里两个属性分别定义了取消和超时时候当前线程的行为，就是中断。我们现在就能启动项目测试了吗？碟集，我这边还有一个小彩蛋是什么呢？大家跟我一起来看，我们到 fin consumer advanced 里面，把这串属性给它 copy 过来。这是什么鬼呢？这不是瑞笨的属性吗？没错就是瑞笨。因为咱这个 high streaks 是不是设置了一些超时规定啊？那它有可能和瑞笨设置的超持有冲突，也就是两个相互作用，谁也不服谁。这一部分的知识我现在不想剧透太多，不能说的太细。接下来有一个章节，我们专门来讨论如何对这种情况进行处理。所以这里咱就好，读书不求甚解，把瑞本的配置给他，稍微改大一点，也就是让他晚点生效。


OK 那经过这一串配置以后，大家就可以在本地把这个项目给它启动起来，然后实际的测试这个 retry 方法，看它是不是能触发我们的降级流程。 OK 那么现在把 high streaks 给它启动起来走，你我们先切换到外面的 postman 这里我调用了 5 万端口的 time out 给它传入了一个秒数，我们先来尝试一下，看这个秒数是一秒的时候会不会触发超时。好，我们现在发送一个指令，走夯住一秒返回。你看，这个端口号顺利返回了40,004，这个就是分 client 这台机器的端口号，那把这个 1 秒改成 0 秒，它应该瞬间返回。果然这里我把它改成两秒，试一下两秒，可就是我们超时判定的标线。
Oh， you are late.


我们看到了这句话代表着什么，代表着超时判定起作用了，我的逻辑进入了 fallback 里。 OK 我们回到配置页面，在这个例子中，我们配置了一个全局的变量。那么如果同学们想对每一个具体的方法在方法级别上配置变量，那怎么配置呢？小意思非常简单了。我这里教同学一个方式，我们配置方法的时候，如果想针对每一个具体的函数，也就是 service 来配置它的超时属性，可以这样配置，我把这一行配置下来。


那这不是有重复了吗？那不行，我需要把这个 service 的名字给它添加进去，添加到哪里大家应该从这里直接可以看到我要替换这个 default 对不对？我要把它替换成我的 service name 怎么来替换？同学们这样来，首先把你的类名给它打上 my service 然后打上一个井号，井号后面跟着的是你的方法的名称，我们这个名称应该是叫 retry 然后是你的方法签名。这个 retry 接受一个什么参数，我们来看一下，他接收一个 int 值。


OK 那我这个方法签名里面就可以大摇大摆的写上一个 integer 那同学说如果我的方法这个签名非常复杂，那怎么办呢？也有一个办法，方法真是无限多，我们来到闷函数里，我这里给大家写一个示例，这示例是什么呢？我们 system out 不剧透，坚持到最后。大家往后看 system out 什么东西呢？看到吗？一个 feed config K 的这个工具，这工具可神奇喽，它会给你自动生成一些签名，我们把自己的类给它塞进去。


my service.class 紧接着我们使用反射的方式把 my service 这个 class 里面对应的方法给它找到方法报上名来叫 retry 它的类型是小 int.classo 有的同学不知道这个小 int 也是直接可以点 class 的，直接跑一下这个闷方法，把这个 K 给拿到。好看，它是返回了一串 K 我们把它。复制下来之后怎么办？复制完了把它给塞回到 practice 文件里面，直接把这里替换掉。 OK 好了，那我这里，前面给它配置了 2000 超时，我想给它配置的时间更长一点，给它配置成3000，然后保存一下。保存完了回到 application 里面，把这个生成 K 的部分给它注释掉，然后打开下面正常的方法，那我们走一遍，试一试启动服务，看一看我们给这个方法级别设置的超时是不是会覆盖掉默认的超时。


好应用已经启动成功，我们转战 postman 前面我们调用两秒的时候是不是超时了？现在这个约会的女孩子，宽容了一点，给你设置三秒钟才超时，看你能不能出来。两秒钟已经不超时了耶。那三秒钟我们试一试看这个同学在三秒钟时候是不是还会超时走起？果然超时了。这个同学人送外号快三秒不行。


OK 那通过这个例子我们证明了什么？在方法级别单独设置的这个超时配置是会覆盖全局的超时配置的。那同学们可能会说了，我用这种方法签名的方式来进行超时配置，是不是显得有些臃肿，有些难看，有些别扭，有没有解答更简洁的方法？有这个方法签名可以被配置成一个 command key 但是什么是 command key 我们将放到后面的章节来进行介绍。


刚才说的是第一个彩蛋，接下来还有第二个彩蛋要跟同学说的，我们不仅可以在配置文件中配置一个超时属性，还可以在代码中配置。这么听下来我们还有两个其他途径来配置超时属性喽。没错，我们都会放在接下来的章节中一一揭晓。好，这一节的内容我们就到这里了。我总结一下这一节，包括前面的一小节，我们从头到尾体验了 for back 的流程，分别通过异常抛出的形式以及超时判定的形式将用户请求导向到了 fall back 逻辑里。同时我们还学习了两种不同的超时配置方式，分别是全局配置以及针对某一个服务进行特殊配置。不仅如此，我们还留了两个彩蛋，还有其他两种配置方式将放在稍后的账记中进行介绍。


同学们 high streaks 的第一课体验如何呢？是不是有这样一种感觉，本来听起来高深莫测的这个降级原来就是这么一回事儿。没错，实际上这后面真的没有什么很复杂的技术，玩转降级熔断真的是一件相当容易的事情。不过大家可要把这些 demo 自己从头到尾的敲一遍，这样才能把这些知识吃到肚子里面去。好，同学们，那这一节就先讲到这里了。在下面一节，我们将介绍 high streaks 中的另外一个功能叫 request catchok 同学们，下一节再见。


