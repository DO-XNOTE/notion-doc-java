---
title: 2-5 【Demo】Guava RateLimiter客户端限流（阻塞模式）
---

# 2-5 【Demo】Guava RateLimiter客户端限流（阻塞模式）

[image](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/17b31c8b-7201-4768-a67f-969199381a5b/SCR-20240808-hnnu.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466Z5EGJPF4%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T225456Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIDmkbBoJ6JgLPIxAXhK3cCWy8FcWfpI2Ny2oJ%2Fq%2F%2B8aKAiEA4bIs6eL5O0NXwRKH7xzfgB2w8iYsFzeMNlq9yzLvim8qiAQIxv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDC8DQd3iB41rTIgryircAzqhPy0O5kTPhoC1eRc5fxwmJ0%2BgNdSyGwGZNxb3VIAcvQZsSbgWEx6RT1IMuYFxqwhZ5M1jNoIaSEDP65uaQDqB1pvrGEpZ%2FToYzUVuBCpdWtJv8Ve%2FlYHjgxb6DFqhGyeOK2031%2Bvq1imWrIqfh7aP4UkNMy3fTdysJbjaLx49GkbZ2rbIIgYPg1LbbTul7VbXhakiokmutekvzbhZ056Y6pADn5ZofQupDIDyhLW0SIwwJjh7CwGoisXWULXRG%2F%2B%2Flft6TEcsEv%2FNwhYorloYxNE%2Bprs3p6uHXXDFV%2FUIJi3S0CbuRrGl810iEU0ApBgrXv9%2Fs0%2BPCfP2kVRJnFzu5ziEjLP8qNwrl6TZche8ngG8j85agGyST6rQorqF2H9LsM1gEGhUQc1t9gmeDN28tgtPBEaC88cTQ9Z9mCDxgtbPJwmKw99fpAKmduyp4AIRxUz986K%2B1rgRR48HJN4t5YIsVo%2BJhE4iBOfaK17eBNoVVrXymplMOkabZ0EU6boucFZrBvX%2F6rLA88HSQy1cSy%2BU4mQauDQXdMsfNPnp3ELz1hd0V%2BAVRvSWcrvtFfIeyOQ8RY17gBt9p%2BX13%2BvaRZPb2Whxcx1yI2RuxwJta%2FnuTyRbU173fCB8MKC3%2F9IGOqUBT8J6msjffHGQy2pKwYlT%2FZG83%2F8GFWeQVpu6MxOKjnlxDZiSVsCVkYpnRGlNWeCSlxyb%2Fl%2FAHyjWezArRgK2jD7WMznDKrdKbZOGY%2BQ7wHPotdzq%2BTZfwTSl39CKVivihFdBsijRQTpw5I5i%2FhKAfgkTW5dCJSKRENZWlRwsgBtCQ8kG2xUtToJLODUI0qaqqOQ8JG5Q315%2Fj7ym3WiF9r8qDKh7&X-Amz-Signature=69b7e4a9fd3af630d6ccf3cd1619be22efe2823e8309924bf5a140f97c58dae7&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

[image](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/549f67b4-2352-4dc8-a8c1-5194b33e31e8/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466Z5EGJPF4%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T225456Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIDmkbBoJ6JgLPIxAXhK3cCWy8FcWfpI2Ny2oJ%2Fq%2F%2B8aKAiEA4bIs6eL5O0NXwRKH7xzfgB2w8iYsFzeMNlq9yzLvim8qiAQIxv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDC8DQd3iB41rTIgryircAzqhPy0O5kTPhoC1eRc5fxwmJ0%2BgNdSyGwGZNxb3VIAcvQZsSbgWEx6RT1IMuYFxqwhZ5M1jNoIaSEDP65uaQDqB1pvrGEpZ%2FToYzUVuBCpdWtJv8Ve%2FlYHjgxb6DFqhGyeOK2031%2Bvq1imWrIqfh7aP4UkNMy3fTdysJbjaLx49GkbZ2rbIIgYPg1LbbTul7VbXhakiokmutekvzbhZ056Y6pADn5ZofQupDIDyhLW0SIwwJjh7CwGoisXWULXRG%2F%2B%2Flft6TEcsEv%2FNwhYorloYxNE%2Bprs3p6uHXXDFV%2FUIJi3S0CbuRrGl810iEU0ApBgrXv9%2Fs0%2BPCfP2kVRJnFzu5ziEjLP8qNwrl6TZche8ngG8j85agGyST6rQorqF2H9LsM1gEGhUQc1t9gmeDN28tgtPBEaC88cTQ9Z9mCDxgtbPJwmKw99fpAKmduyp4AIRxUz986K%2B1rgRR48HJN4t5YIsVo%2BJhE4iBOfaK17eBNoVVrXymplMOkabZ0EU6boucFZrBvX%2F6rLA88HSQy1cSy%2BU4mQauDQXdMsfNPnp3ELz1hd0V%2BAVRvSWcrvtFfIeyOQ8RY17gBt9p%2BX13%2BvaRZPb2Whxcx1yI2RuxwJta%2FnuTyRbU173fCB8MKC3%2F9IGOqUBT8J6msjffHGQy2pKwYlT%2FZG83%2F8GFWeQVpu6MxOKjnlxDZiSVsCVkYpnRGlNWeCSlxyb%2Fl%2FAHyjWezArRgK2jD7WMznDKrdKbZOGY%2BQ7wHPotdzq%2BTZfwTSl39CKVivihFdBsijRQTpw5I5i%2FhKAfgkTW5dCJSKRENZWlRwsgBtCQ8kG2xUtToJLODUI0qaqqOQ8JG5Q315%2Fj7ym3WiF9r8qDKh7&X-Amz-Signature=d4d6abf43167d4434991377eac3e0345214d569f03e226415a00300cef9fb11c&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

[image](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/3a7e8e20-e6ac-4a60-9b30-f1223f2d3c33/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466Z5EGJPF4%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T225456Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIDmkbBoJ6JgLPIxAXhK3cCWy8FcWfpI2Ny2oJ%2Fq%2F%2B8aKAiEA4bIs6eL5O0NXwRKH7xzfgB2w8iYsFzeMNlq9yzLvim8qiAQIxv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDC8DQd3iB41rTIgryircAzqhPy0O5kTPhoC1eRc5fxwmJ0%2BgNdSyGwGZNxb3VIAcvQZsSbgWEx6RT1IMuYFxqwhZ5M1jNoIaSEDP65uaQDqB1pvrGEpZ%2FToYzUVuBCpdWtJv8Ve%2FlYHjgxb6DFqhGyeOK2031%2Bvq1imWrIqfh7aP4UkNMy3fTdysJbjaLx49GkbZ2rbIIgYPg1LbbTul7VbXhakiokmutekvzbhZ056Y6pADn5ZofQupDIDyhLW0SIwwJjh7CwGoisXWULXRG%2F%2B%2Flft6TEcsEv%2FNwhYorloYxNE%2Bprs3p6uHXXDFV%2FUIJi3S0CbuRrGl810iEU0ApBgrXv9%2Fs0%2BPCfP2kVRJnFzu5ziEjLP8qNwrl6TZche8ngG8j85agGyST6rQorqF2H9LsM1gEGhUQc1t9gmeDN28tgtPBEaC88cTQ9Z9mCDxgtbPJwmKw99fpAKmduyp4AIRxUz986K%2B1rgRR48HJN4t5YIsVo%2BJhE4iBOfaK17eBNoVVrXymplMOkabZ0EU6boucFZrBvX%2F6rLA88HSQy1cSy%2BU4mQauDQXdMsfNPnp3ELz1hd0V%2BAVRvSWcrvtFfIeyOQ8RY17gBt9p%2BX13%2BvaRZPb2Whxcx1yI2RuxwJta%2FnuTyRbU173fCB8MKC3%2F9IGOqUBT8J6msjffHGQy2pKwYlT%2FZG83%2F8GFWeQVpu6MxOKjnlxDZiSVsCVkYpnRGlNWeCSlxyb%2Fl%2FAHyjWezArRgK2jD7WMznDKrdKbZOGY%2BQ7wHPotdzq%2BTZfwTSl39CKVivihFdBsijRQTpw5I5i%2FhKAfgkTW5dCJSKRENZWlRwsgBtCQ8kG2xUtToJLODUI0qaqqOQ8JG5Q315%2Fj7ym3WiF9r8qDKh7&X-Amz-Signature=399af0e04d6bf51bb86d8c6d28f033949c71425b8e2c08d7044593b439ceaeb8&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

过往的各位同学们，大家好，这一节咱来到了分布式限流中第一个需要动手操作的环节了。俗话说万事开头难，但是我们非要反着来在一开始做一个简单的 case 咱这一节将使用谷歌开发的 gravaa 工具箱，其中的 read limit 客户端限流类给大家，提供一个简单的轻量级的客户端限流方案。


那咱先来看一下本节的主要内容都有哪些。第一部分，咱创建一个 read limiter 子项目，这是一个独立的 module 然后引入咱需要的依赖项进去。

[image](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/825db758-28e5-409a-9f76-196044816aec/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466Z5EGJPF4%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T225456Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIDmkbBoJ6JgLPIxAXhK3cCWy8FcWfpI2Ny2oJ%2Fq%2F%2B8aKAiEA4bIs6eL5O0NXwRKH7xzfgB2w8iYsFzeMNlq9yzLvim8qiAQIxv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDC8DQd3iB41rTIgryircAzqhPy0O5kTPhoC1eRc5fxwmJ0%2BgNdSyGwGZNxb3VIAcvQZsSbgWEx6RT1IMuYFxqwhZ5M1jNoIaSEDP65uaQDqB1pvrGEpZ%2FToYzUVuBCpdWtJv8Ve%2FlYHjgxb6DFqhGyeOK2031%2Bvq1imWrIqfh7aP4UkNMy3fTdysJbjaLx49GkbZ2rbIIgYPg1LbbTul7VbXhakiokmutekvzbhZ056Y6pADn5ZofQupDIDyhLW0SIwwJjh7CwGoisXWULXRG%2F%2B%2Flft6TEcsEv%2FNwhYorloYxNE%2Bprs3p6uHXXDFV%2FUIJi3S0CbuRrGl810iEU0ApBgrXv9%2Fs0%2BPCfP2kVRJnFzu5ziEjLP8qNwrl6TZche8ngG8j85agGyST6rQorqF2H9LsM1gEGhUQc1t9gmeDN28tgtPBEaC88cTQ9Z9mCDxgtbPJwmKw99fpAKmduyp4AIRxUz986K%2B1rgRR48HJN4t5YIsVo%2BJhE4iBOfaK17eBNoVVrXymplMOkabZ0EU6boucFZrBvX%2F6rLA88HSQy1cSy%2BU4mQauDQXdMsfNPnp3ELz1hd0V%2BAVRvSWcrvtFfIeyOQ8RY17gBt9p%2BX13%2BvaRZPb2Whxcx1yI2RuxwJta%2FnuTyRbU173fCB8MKC3%2F9IGOqUBT8J6msjffHGQy2pKwYlT%2FZG83%2F8GFWeQVpu6MxOKjnlxDZiSVsCVkYpnRGlNWeCSlxyb%2Fl%2FAHyjWezArRgK2jD7WMznDKrdKbZOGY%2BQ7wHPotdzq%2BTZfwTSl39CKVivihFdBsijRQTpw5I5i%2FhKAfgkTW5dCJSKRENZWlRwsgBtCQ8kG2xUtToJLODUI0qaqqOQ8JG5Q315%2Fj7ym3WiF9r8qDKh7&X-Amz-Signature=f74376776666237acd87b23c78de149a177e40a6a537a0587e0a67b2f71c28b8&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

紧接着咱来领教一下如何在 grama 当中创建一个非阻塞的限流方案。非阻塞是什么意思比如说你现在有一个请求进来了，但是他拿不到令牌怎么办呢？干等着妈。


No！No！No.我们的做法是出门只走右转不送，当即返回失败。那除了非阻塞式的限流方案以外，同学们一定想到了它还有同步阻塞式的限流方案对吧？这时候的用户请求会怎么样呢？假如被处于限流状态，他会在那里干等着，直到限流状态解除以后才会放行。这节的内容既轻巧又简单。同学们准备好的话，跟我到银泰迪这里，咱开拔每天 coding 1 小时，健康工作 50 年。同学我们这里准备要开工了，我想同学们看到我的影泰力，这一定很纳闷，因为这里怎么排排坐排了这么多从来没见过的名词和项目。大家不要心急，这是你们在后面一个章节微服务将要学到的内容。老师可是从远程穿越过来的，在录分布式章节的时候，已经把后面一个章节所有的教学 demo 全部给搞定了，此处应该有掌声才对。
好，那我们二话不说开始本节的demo 。这里我们对着顶层项目创建一个新的 module 顶层项目咱可以从 github 中的代码上面拉取下来。我们的分布式最后一个章节的代码和下面的微服务章节代码是放到一块的，大家参考一下就好，我们这里创建一个新的 module 然后给它起名字叫什么呢？就叫 rate 杠 limitok 点击 next 这个项目的 moto name 和前面保持一致。 rate 杠 limit 然后就创建在咱的 spring cloud demo 这个大项目，下面点击 finish 321 palm 出来。


好嘞，咱这里看到它继承了一个 parent palm parent palm 是我在 github 中已经创建好的，大家到时候拉下来就可以。我们的 parent pom 里面只是指定了很简单的内容，比如说它这边有两个 dependency management 分别指定了咱需要用到的 spring boot 还有 spring cloud 的版本。那咱在这一节当中只会用到下面的这个上面的 spring cloud 咱下一节再说。并且它在下面引入了一个咱需要用到的工具类是什么呢？是轮 book 这个组件大家应该都比较熟悉了，前面的项目中也有用到。 OK 那我们的 rate limit 中的 palm 就继承自这个 spring cloud demo 的 palm 文件，咱接下来要往这里面添加一些 dependency 都有哪些地盘？纳斯呢？好，我们来从头开始，江湖好汉排座次。


那这第一个 dependency 当然要老大哥上了，叫 org spring framer 后面跟谁 boot spring framework spring boot 当中的哪一个类呢？它的 artifact 是 spring boot 然后后面跟着 starter web 因为接下来咱要 demo 的内容是基于 sprint boot 搭建的应用，所以这里要把它的引用首先拉进来。
大哥好了，二哥上二哥是哪位报上名来。好，这里二哥我们来引入一个当之舞会的黄金配角，这个黄金配角在其他章节中是配角，但是在咱这一章当中算是一个主角了。它就是咱前面提到的谷歌的工具包，它的 group ID 是 come.google.graph OK artifactid 这里我们把它打上就叫 gravaa 它的版本是什么？咱这里给它指定是幺八点零，大家也可以使用最新的版本因为老师这个人比较喜欢18，要发，所以咱这里就用幺八点零讨个好彩头。


咱接下来就要创建 Java 类了，在创建 Java 类以前，我们先要把包名给打上去，包名打谁好呢？我们这里就要感谢本章课程的独家冠名赞助商 I mock 所以这个包名就给它冠名成 come.i mock.spring cloud 。因为我们后面的章节都叫 spring cloud 所以这里也就保持队形了，叫 spring cloud 好，接下来我们给这个项目创建一个启动类，因为本章的内容是限流，所以这个启动类的名称就把它叫做 read limiter 然后后面跟 application 好勒，这个类创建好了以后，我们要打出一串行云流水的输出。
那创建一个 man 方法， public static void man 这个慢方法中，怎样把这个项目启动起来？怎么启动啊？ new spring application 咱用它的 builder 把这个项目给 build 起来。 a builder 当中传入当前的类的 class 好在后面另起一行，我们以 web 形式来把它启动起来，那它传入的参数启动类型是 web application 中的 servlet 类型，接下来直接把它跑起来。好了，这里把 arguments 参数参给它传入进去。


那闷方法好了以后，咱可少不了一个关键的注解，我们往这个类的头上戴一顶绿帽子，叫 spring boot application 那加上这个注解以后，当前项目就可以以 sprint boot 的方式来启动了。我们接下来就可以去创建配置文件，咱先把准备工作给它准备好，这样就能安心的码代码了。这个配置文件我们给它起名叫 application.properties 大家如果喜欢 YAML 格式的也可以用YAML ，老年人一般比较喜欢property ，年轻人都喜欢 YAML 好，这里的配置文件属性咱先给它定义。
第一个，自报家门 [spring.application.name](http://spring.application.name/) 它的 name 叫什么叫 rate limiter 是当前的项目名称，接下来要给它指定一个端口号来，老师最讨厌使用什么 8081 了，这里给它起叫10086。好勒，就是这么简单，这里暂时不需要其他配置，等后面的时候咱学到 Redis 限流，那还要在这里配置 Redis 的连接串，我们现在就只用配置这两个属性就好了。


那接下来咱可以去创建一个 controller 了，这样我们就可以在外部的 postman 里发起调用，来验证我们的限流逻辑了。我们给这个 controller 起名就叫controller 。好，定义完controller ，咱接下来给上面添加一个方法的 annotation 叫 rest controller 然后再给他添加一个 sl four G 这是龙 book 的一个 log 组件，方便我们打印一些 logok 那接下来主角要登场了。咱这里给他添加一个新的类叫 rate limit 这个类的名称，我们也把它起名叫 rate limit 那怎么样声明是 new 吗？ No no，no.我们使用 rate limit 的一个 create 方法。好， create 里面的参数是什么呢？我们给它添加一个2.0。 2.0 是什么意思呢？就是说我的这个限流组件允许每秒钟发放两个通行证。这样一说大家是不是就明白了如果你的请求过来，每个请求消耗一张通行证，那么这样的话你每秒钟就可以有两个请求过来消费。我们不妨点击 create 进去看一眼。


实际上 rate limiter 不仅只提供了这一个 create 方法，它在下面还有其他的不同的方法签名。比方说这里这个 create 方法它还有一个很奇怪的变量叫 warm up period 这就是预热模型了，这是接下来要讲的内容。我们这里先不纠结，返回。


Ok. 那在正式开始写 control 的方法之前，我们不妨再点进去看一下 rate limit 这个类里面又卖的什么药呢？你看这里有一个注解大红注解高高挂，看到这个注解我就觉得很安全。这个注解是 thread safe 线程安全。但是在这么安全的一个注解下面，好像有一个那么不安全的注解，它叫 beta 什么意思呢？就是说当前的这个组件还是一个 beta 版测试版，有可能只是说有可能会有那么一点点潜在的问题。不过大家尽可放心，因为这毕竟是，谷歌出品必属精品，它既然放出来让大家使用了，我们姑且放心使用就好。 OK 我们返回回来。


那这个 limit 已经声明好了以后，我们接下来要去定义第一个 case 这个 case 叫什么呢？它就叫非阻塞限流。 OK 那我们给这个方法起个名字叫 try acquire 尝试获取通行证。那为什么咱不直接叫acquire ，因为我们没有这么自信，所以说需要先尝试获取，它有可能会被我们的 limit 给拒绝。
那这里我们要接受一个参数是什么呢？ integer 类型的 count 这个 count 是什么含义？我们马上就知晓了。在方法体中，我们先不着急写自己的业务逻辑，我们先要问一问这个limit ，当前有没有通行证给我，没有我就走了。那怎么问调用它的 try acquire 方法。这个方法它有一个默认的实现，就是说你不传入任何参数，那它默认当前的请求获取一张通行证。如果你想让当前的请求消耗多张通行证令牌的话怎么办呢？这里就用到了咱传入的 count 我们把 count 传入进去。如果你当前的请求每秒钟消耗一个令牌，那么这里就可以每秒钟让你通行两个请求。但是如果你每秒钟要消耗两个令牌，那么我每秒钟只会让你通行一个。 OK 那好这里如果这个方法返回 true 那么证实你现在是可以处于放行状态的。那我要恭喜你了，这里打一行 log success 你被允许通过了。然后我们还要在后面打印出一个 rate 当前的速率，速率从哪里拿呢？从 limiter 里面拿。 Get rid. OK 这时候直接返回一个喜报叫 success 恭喜。


那如果你当前没有获取到令牌而又很遗憾，因为它是非阻塞限流，它不必在那等着。你能不能获取这个令牌、能不能获取通行证，这是当场就能知道的。所以当你很遗憾的被告知请出门，只走右转不送，那你只好默然离开。在离开之前说一句话好了。很遗憾。 feel 抱怨一句，然后打印出同样的 rate 这个 rate 咱从上面 copy 一下，把它 paste 下来，然后返回一个 feel 告诉领导。没有办成事，非常遗憾。好，咱给这个方法定义好了之后要加一个 get mapping 它的 UR L 是谁呢？我想一下就把它定义成 try acquire 好了，好快刀斩。那麻咱第一个方法就已经定义成功了，我们不妨把它启动起来试一下。


我想有的聪明的同学，这里可能看出了一个小问题，什么问题咱这里不是定义了每秒钟返回两个令牌通行证吗？那假如你在传入 count 的时候传入了撒，我想一次拿撒，那你每秒钟才给我两个，你想拿仨怎么办呢？待会儿我们测试一下就知道了。好，咱的项目启动得非常快，因为没有加入任何其他的组件，我们把 log 清空一下而转战到 postman 这里。 postman 向 10086 端口的 try acquire 方法发起了调用，我们把 count 先指定成1。好，接下来可以点击 send 了。我们这里一通乱点能快有多快？来准备开始爬爬。唉呀一阵啪以后，我们回到 intelligi 里面看一下 log 我们把它稍微放大那么一点。 OK 我们来这里看一下。两行成功的 log 之间大概相差多长时间？看这一个成功的 log 它是 44 秒 769 接下来一个是 45 秒269，这之间大概相差多少？相差了0.5。大家如果看看其他的log ，也差不多是这种情况，两个之间相差接近 0.5 左右。
那这说明了一个什么情况？同学们能猜出来吗？如果你当前分配了两个令牌，它其实是会匀速的在当前秒钟发放出去。也就是说你可能在这一秒刚开始的时候发放一个令牌，在 0.5 秒的时候又发放一个令牌。那假设你这里发放 10 个，那依然是匀速发放的。


不过这里好像有那么点蹊跷什么呢？同学们看这里吗？在一开始极短的时间内，他突然间放行了四个请求，但是在下面，他每秒钟只能放行两个请求了。这是？为什么一开始他能放行四个？好像限流措施难道失效了吗？ No no no.这里就要牵扯到后面的预热模型等等之间的逻辑了，我们在后面的章节里会跟大家详细说明的。 OK 那咱把 log 清空再做一个测试。什么测试呢？咱把 count 改成 2 来再来一阵啪啪调用准备走。唉呀一阵啪啪又结束了，咱回到 log 里看一下。 OK 我们看两个成功请求之间相差的秒数，将一次拿走了你两个通行证，而所以你每秒钟应该只能放行一个。好，这个成功的请求是在 33 秒放行的，下一个是在 34 秒238，这之间的间隔近似一秒钟。那后面三四点二三八跟下一个是三五点三五三也是近似一秒钟。所以正是咱的这个限流器完全运作正常。不过我们再往上滚。发现在开始访问的时候又出现了前面那种奇怪的情况，为什么在刚开始的时候，他能在一秒钟之内突然放行两个请求呢？看起来不合理。这个存在即合理。当我们揭示了它里面的底层机制以后，同学们就不会觉得它奇怪了，什么时候揭示，反正不是现在后面我们会找机会跟大家说的。好，我们把 log 清空，再来测试一个情况，你看我们现在变身成了测试人员，专门给开发来找茬，在那 count 是2，我们把它设置成 4 号了。


好，再来一阵啪。其实 postman 有一个批量发送的功能，大家不用这么累的点击按钮。但是我觉得自己发送请求比较带感，就像手工面条永远比机器面条好吃。对不对好，我们再来，准备好开始。一阵狂点之后走到 entirely J 里面。我这里每秒钟消耗几个请求？消耗 4 个令牌。 OK 那你每秒钟产生几个令牌？只产生两个。那怎么办？这种情况下，我们看一下它两行 success 请求之间的间隔。这个请求 success 它是在 20 秒点 4 这个时间产生的。那下一个 success 在哪里？我们找一找。还找不见了。在这里下一秒是在 22 秒500，这之间相差了多少？相差了两秒钟。对不对啊？那这代表着什么含义呢？就是说如果你当前只能发放两个通行证，但是我要 4 个。 OK 那我可以让你先通行，只不过我要在自己的小本本上面怎么样记下来。你欠了我两个，那这两个什么时候还呢？等我下一秒新的通行证发放下来之后，我先优先偿还上一波你的欠债，然后再来去服务新的请求。所以他这里你会发现每隔两秒钟才会成功一次，因为两秒钟你才会产生四个令牌，才能满足一次调用。好。不过这个奇怪的情况又出现了，同学们看这两句好像在一秒钟的时间内，我就放行了两个需要四张令牌才能放行的请求。这是什么原因呢？同学们，我觉得你们现在已经非常非常纠结了，很迫切渴望想知道这个东西。我偏要跳跃到大家的问候，等后面张杰再跟大家说这里我们怎么来理解这种情况，大家可以把它当成什么呢？新用户优惠。


第一次调用的时候，我把你当做新用户好吧，送你一次免费大保健，但是当你后面再调用的时候，我就要给你记账了。你欠我的，我可要记在自己的小本子上面，等后面是要你还的。 OK 那这里就是我们测试的简单的非阻塞限流的情况了。不过假设我的应用有这样一种需求什么需求？也就是说我不是那么着急，那么迫切的就要知道当前你能不能服务。我想知道的是在未来的一秒钟甚至未来的两秒钟，你有没有可能存够足够的通行证让我访问呢？如果在未来两秒钟你可以让我达到访问的这个要求，那我愿意等这两秒，如果不行，那我也只好走了。那这种介于非阻塞和阻塞之间的请求怎么办？也就是定时阻塞。我们这样办，先给他打一个叫限定时间的非阻塞限流，看这个描述的相当精确。


那怎么办呢？我们开始录代码了，我们只要把上面的这个方法把它 copy 一下，然后 paste 到下面，在这个基础上改。把这个 try acquire 给它改成 with the timeout 就是带有 time out 的尝试获取令牌的动作。然后它这上面的 get mapping 这里面也把 time out 给它加上去 with time outok 那这里他冒的咱是不是要传进来，那这个方法签名也要变喽，不光是 count 还有一个 integer 类型的 timeout 同学们在传入参数的时候，咱就不用使坏传个 0 什么负 1 的，咱就都把它传成正数。
好了。 OK 那在下面 try acquire 这里咱怎么做呢？很简单，把滩帽子传入进去，传入完了还不够，我们还要怎么样。告诉他这个 time out 的时间单位。这里我们可以直接调用 time unit 它是哪里面的类呢？这个 time unit 是 concurrent Java concurrent 包下面的类。咱前面传入的应该是按秒。那这里就是 time unit.seconds。 Okay. 好，我们把这个项目给它关停掉，然后重新启动一把稍等半炷香的时间，咱们有组件加载得非常快。


这里已经启动成功了，那我们把这个方法的路径给它 copy 一下，也就是说我们到 postman 里找一个这个方法 try a choir 怎么调用呢？我这里把它设置成 2 count 是2，胎冒的是几呢？我胎冒的设置成零，那如果胎冒是零，说明当前的胎冒了基本上是没有生效的。对不对？不是说基本上它就是没有生效的。好，我们这里看到它实际上返回的速度也非常快，那它还是一个非阻塞的限流，因为它的等待时间是零，并没有这种让你挂起多少秒的操作。


OK 那接下来我把 log 给清空掉，我们再换一个姿势来调用。咱的 count 还是2，然后把 time out 设置成几呢？我们把它设置成2。好了，OK我们再发起调用。如果它的它冒生效的话，那咱发起的调用应该会在页面上夯住一段时间。我们来开始。同学们看到没有在 postman 里这个请求，被夯住了一段时间大概一秒钟。 OK 那我们到后台看一下，哇全是成功没有失败。因为为什么？还因为咱在 postman 里夯住的 loading 那段阶段是没法发起第二个请求的。如果那段阶段还能发起请求，这里是会看到失败的。 OK 那咱们每个请求之间的间隔大概是一秒钟。那我们这个 time out 其实时间太短了，我们把它设置长一点，让这个 time out 表现得更那么明显一点。好吧，这里把 count 设置成10， time out 设置成几。


五好，我们点击 send 你看 123 这里大概很快就返回了。因为为什么呢？咱设置的每次拿取的令牌是10？他冒的是5。那咱们每秒产生的新令牌是几？是2，说明在 5 秒钟之内我最多可以产生几个令牌。 2 乘 5 等于10。对不对？也就是说当前你的令牌产生速度一定能满足你这个请求所需要获取的令牌数在约定的探报时间范围内。那假如我把这个时间配置的太离谱，比如我现在想获取多少个 100 个令牌，那你 5 秒钟能不能返回这么多呢？绝对不能。 OK 那我们试一下这个请求会不会调用成功。


按照新客户优惠逻辑，第一次会成功的对不对？好，接下来第二次点击看到吗？他这立马返回了失败，他并没有夯住 5 秒钟再返回失败，而是立即失败了。我们说这叫 fast feel 为什么呢？因为你无论如何，你在 5 秒钟之内绝对产生不了 100 个令牌，它一定是会失败的。所以说这个 read demeter 它有这样的一个机制，在你要求的令牌数远大于在规定时间内我可以产生的令牌数的时候，我会直接让你返回失败。其实这是一个很好的性能优化的点。


OK 同学们，那这一节中跟大家 demo 的非阻塞限流的两个例子就到这里了，看来我已经拖堂了，咱剩下的阻塞的例子我们放在下一小节跟大家讲，然后讲完之后再带大家回顾一下这一章中学到的 rate limit 简易版限流的知识点。 OK 同学们，那我们下一小节再见。



