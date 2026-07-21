---
title: 1-5 【Demo】整合Sleuth追踪调用链路
---

# 1-5 【Demo】整合Sleuth追踪调用链路

[image](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/5cd5f5cf-972b-4fd3-bb73-748f722db0bf/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665ELUCSIN%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T225757Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDwvRryA0lMlct41QjKOnRp%2Bl9iSRSsA2Rhw0gzHLkghAIhAMeQiv9OZNOeOrMnhiJYgBmStxE%2BP6ZBik60cEPVzwowKogECMb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1Igz9JHnJIrMaqnzmBnMq3ANwwW9Q0t0%2BEny2qSvkWxFzNnHSZP24UI3fm1GTsZSnFRrxZp49cpaKEq9XmQVR4lcN5VtXJpn4kJTb%2FvSfl3L9kxWT7l5SEYjoZTYULAySHjvVWoL%2FO3nexkXR8EbwYANLZ9t82NnDzuM73F67UUzP47E3MgoRgiAd2t9K9qZDJJGZ27wPW3aqq913of3SF0T9fNULJkAQnzVf1coXTDYXRDzr727Vbpy7C%2F6ViuEVGlx3f70bE2h4XMEgpADJfeTlDgFrh7xt0jCPxxbhBTOXP8SQB7Cxu%2Bl7rM8zEYkuaomO9mSCuAE3QS%2BPxj9KByPlgauMzDjmZPpP79uggYqelJj7qw3GXuYijLHPvsrpYB86rYJfCp1u5QbI%2F9ZZF6pFImwN6fiqWNR4GTEG8%2FeRSQ5rQ08n1GlEWoFesOfIDrWbmehTkh0ucAJb7ZfXkOp%2Bxm%2FX9OiGdR4OFIzFQp6berB3C17MXiPqyrX0v8HwdNL1BQU2koX2jApiTfxj4f1Uhibgp8u4JPN6tsLR1p90dPiP2OT889eLRfwQzhsVofx9ovlFHARocRrspyLc2sLTGAFCdcX2tO01YtDPk4jApUTMgYDqgrtn0b4bPwSVVu5nqDDcm%2Fn5TABRnDCOuv%2FSBjqkAYC9AaUQhRMqIQQR5Pa7ltKwZ9jCXyiPEdY3%2BuAL1mBx0p2SiYxD0Xv0n%2FejV8aePIydw3fF0hrGplEOoLKTEv342RdQl2crgLSi1pMhZOqWF6M6ciYD6QpWAXLRE59w4u%2FpDSdB8WIgAFzemDetOojfuTFlgTQ9WMpUwBje8Crn3Ycv5oIOtnaZJOp12rdgXq8QcVxGrJF6t5bMDTsox4siDRqR&X-Amz-Signature=27e07eb3cd43163b7b28dcf36d3022e84a781f5d0f0149f00fc02248a6721d91&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

各位同学们，大家好，这一小节，咱们先来做一个 slow 的急速落地，整合 slow 调用追踪链路到咱的项目当中。 OK 我们看一下这一节的主要内容。第一部分，咱们先来创建两个应用， thrust trace A 和 slow trace B 把依赖添加进去，我们让这两个应用互相玩一招，左右互搏数，它们之间互相调用。接下来咱去看 log 里面都多了什么信息，去观察一下 sloose 在 log 文件里面都做了些什么手脚。在这个过程中，我要带大家看一下 loose 中的一个秘密机关，那就是采样率。 OK 同学们抄起家伙跟我出发，编程是我快乐 996 是我的福报。
这个 solution 章节咱要创建一个全新的 director 文件夹，起名就叫 solution 接下来咱要创建两个互相调用的服务。 OK 先给它创建第一个毛酒，咱跟它起名叫 salus cheese a trace aok 把它复制一下，在后面的 module name 和前面保持一致，然后扔到哪个文件夹，扔到咱刚创建的 solution 文件夹下。这个 louis 几个字，非常容易拼错。


点击 finish 321 好，我们先来创建它的 pump 文件，这里把 dependency 加上。 OK 他这里的dependency ，大部分都可以从其他项目里面借鉴过来。同学们走，跟我一起抄作业去，咱随便挑一个项目就挑分项目。 OK 从这里面去抄哪几题啊？这个 eureka 拿到 old starter 拿到 accurator 就这三个把它给拿过来复制过来。 Ok. 除了这三个以外，还有 slow 的自己的一个 dependency 这就不能抄作业了。它是一个全新的 group ID 依然是 org spring framework.cloud OK 它的 artifact 是 spring spring 杠 cloud starter 后面跟 sloose 咱 spring 的各种组件它的命名都是相当规范的。你看这个 artifact ID 都是保持同样的队形，咱 pump 文件配置好了以后，随手给它加一个 packaging 定义成 jar 的类型。


好，接下来咱就开始创建启动类了。 OK 我们从其他项目中把启动类 copy 过来之前，先要给他创建好一个栖身之所一个文件夹，package com.imock.spring cloud OK 然后呢依然从 thing consumer advanced 这个项目里面，把这个启动类给它 copy 过来。 OK 好， copy 过来以后，咱给它改弦更章，换个名字把它叫 solution solution A 那咱不能叫 trace a application 两个 A 看起来怪怪的，叫 trace a main 吧。


main 函数点击回车。那咱接下来的所有代码部分，我们就不另外创建新的 controller 来做了，就全部放在当前的 main 函数里。大家别忘了， main 函数其实也是可以作为一个 controller 的，我们给它加一个新的绿帽子 rest the controller 再给它加一个必不可少的 sl four G 这个组件必不可少它可是咱今天的主角。


当然我不是说 lombbook 的 annotation 是主角，而是借助lombbook ，它打印出来的 log 是今天的主角。 okay 接下来我们要发起一个调用，咱没有集成 fin 就用最简单的方式通过 ribbon 的 load balancer 来做。我们这里添加一个 load balance 的注解给谁呢？还有一个 bin 给一个 rest template 类 rest template OK 这是 spring 里面的官方出品的 template 类，就给它起名叫 LB 方法，这里就直接把它 new 出来就好了。这里顺带也带大家回顾一下 ribbon 章节中学过的一种远程代码调用的方式。这种方式就有如抛掉 hibernate 等，ORM框架直接使用 GDB C 操作数据库一样，它是直接操作远程访问，原汁原味。



OK 在声明了 L B 以后，我们就接着把它给注入进来，使用 outer wire 的方法，把这个刚创建好的 rest template 给它注入进来。 rest template OK 注入好以后，这里到今天的主角了，我们声明一个 controller 的方法，把它起名就叫 trace A 好了。 OK 这里给他一个 getmapping 路径设为 Tracy 在这个方法体内，咱有两项重要的任务需要做，第一项打出一行 log 可不要小瞧这行 log 它是咱今天的男猪脚。这行 log 它打什么？内容简简单单，不多不少，就叫 trace A 就这么简单。同学们说这老师你不会糊弄我们吧，就打一个 trace A 这就是这节课的内容了，还真的没错。不过咱今天的主角可不仅仅这么简单，大家看这个sleuth ，它可是要给这行 log 加戏的，待会看它怎么来加戏。


OK 这里打印出一行 log A 之后前面说了要有 trace A 和 trace B 两个项目怎么样玩左右互脖树对不对？所以接下来咱要调用一下 trace btrace B 尽管还不存在，但是咱假定它存在，使用 get for entity 方法，我们来调用它一番。大家还记得该怎么发起调用吗？ HTTP 然后调用它的方法名 solution cheese bok 这是它的服务注册后的名称。那我们调用它后面的方法，紧跟着 trace B OK 待会儿咱要去创建一个 trace B 项目，并且给它创建一个 controller 然后它的 mapping 地址也指向 trace B OK 那接下来这里给它指定的返回值是 string.class ok.get body 好了，这就完成了，我们把代码换一行。


其实咱代码这个宽度限于这种录屏的方式，它不能太长。一般来说我们建议 120 个字符以内其实都是可以的，因为大家平时写代码的时候都是用的宽显示器对不对？像我桌面上摆了四个显示器，其中有一台专门看代码的是花了 8000 多大洋买的球面显示器，超级长。而一行代码我觉得排 1000 个字符都没问题这就是输人不能输装备，早上写代码的装备一定要好。


OK 那咱 controller 这里创建完了以后，接下来咱就要去创建配置文件了。这个配置文件我们从其他地方随便给它 copy 一份过来。那就从咱上一章中创建的 authentication service 里面，把 application.properties 拿过来。拿过来以后咱要改吧改。 spring application name 我们的项目名称叫做 sluice 杠 Tracy 它的 server port 是 62,000 开头，然后 urecar 的服务中心地址在这里， log 文件目录在这里，这三行 Redis 的配置把它删掉。 OK 接下来的 App name 我们从上面把 application name 直接拷贝下来。好，那这里这个文件就创建完了。
然后我来带大家再看一下 logback 的 stream 配置文件。其实大家即便不添加 logback sprawer slow 依然会生效。这里只是带大家看一下 slow 在 logback 日志中它具体是从哪个属性中输出的。 OK 我们看到这配置了一些核心的参数，比方说它的日志输出的位置还有日志输出的格式。然后它的输出终端我这里只配置了一个控制台输出。


Ok. 其中在日志格式这里有一点细。大家看这是一个标准的 logback 的日志输出文件格式。那么在这众多格式当中， sleuth 最终是落在哪一个点呢？同学们是落在这个里面。那如果咱把这个属性给它删除掉了，那大家就看不见死路子的身影了。 OK 我把它给留在这，你看这参数都有迷幻色彩。
5p 好样的。 OK 那咱 solution 下面的 Tracy 项目基本创建完了，这里再跟大家讲一个补充的小知识点。前面说过我们的 solution 里面有一个采样率的配置，采样率是什么含义呢？就是说尽管 soluth 会往咱的 log 日志中打标，但是打标并不代表着这行 log 文件会被采样。那么数据采样这个概念我们后面会结合 zip king 跟大家一起来讲解。


这里我先把数据采样率的配置给大家说一下，它的配置是在 application properties 里面可以配置这样一个采样率，它的名称叫做 spring sleuth.sample 这是采样的意思。点 probabilityok 它是一代表什么含义呢？就是100%。那你所有日志文件都会被 100% 的收集出来，如果想收集 80% 就是 0.8 了。


```java
spring.application.name=sleuth-traceB
server.port=62001

eureka.client.service-url.defaultZone=http://localhost:20000/eureka/

logging.file=${spring.application.name}.log

info.app.name=sleuth-traceB
info.app.description=test
# 采样率
spring.sleuth.sampler.probability=1

management.security.enabled=false
management.endpoint.health.show-details=always
management.endpoints.web.exposure.include=*
```

Ok. 那被采样收集的 log 会用作什么用处呢？那是下一小节的内容了。 OK 我们制定创建了一个 slow 的 trace A 接下来用同样的方法快速创建一个 slow trace B 好了好，我们快马加鞭的动起来，一想到快突然想到了一句诗词，虽乘奔欲风，不以其意，它的 artifact ID 是 solution B copy 一下。好，点击 321 finish 那 trace B 的 pump 文件可以直接从 trace A 这里把它 copy 下来，节省时间。


Ok. copy 完以后，这个 controller 同样的也可以把它借鉴过来。但是 trace B 里面需要稍加那么一点改动。首先依然是给它创建一个 package 叫 com.imock.spring cloud。 Okay. 把闷方法拿过来，改一个名称叫 sleustress B 接下来要演左右互搏数了啊。Ok.在 solution B 的方法中，咱要把这个路径改成 trace B 同样的 log 也要改成 trace B 了，这里就不用再调用 trace B 它自己了调用个没完了，我们就此打住好直接返回 trace B。
Ok. 那接下来依然要把这个 resources 下面的两个配置文件同样的 on trace A 中 copy 到 trace B 里，并且选中 application properties 把端口号改成62,001。同时 application name 也把 A 改到 B 好大功告成，就是这么简单。


OK 那接下来我们可以把项目启动起来，来验证它的 log 是如何来打标的。在启动项目之前，咱先把友瑞卡的注册中心给它跑了起来。 OK 那接下来我们分别跑起 trace B 和 trace A 大家跑的时候注意一下顺序，如果你先跑了 trace A 因为它这里需要调用 trace B 对不对？有可能在你跑 trace A 的时候，它首次服务发现并没有发现 trace B 因为 trace B 还没有注册，那么你可能需要等个 5 分钟之后再来调用方法，才会发起正确的远程调用。 OK 那我这里先把 trace B 给它启动起来，让 trace B 先在注册中心上把自己挂上去。


OK 在启动 trace B 的同时，我们转战到 trace A 同学们实际上从 trace B 这个启动 log 里面已经能看出那么一点点端倪了，是不是这个 log 长得有那么点不一样，前面多了三个点，这就是本节的机关所在了。好，我们把它关掉，接着把 trace 也给启动起来走，你稍等片刻，移炷香的时间，看到 spring 标签成功一半。好吃。


C 现在已经启动起来了，那我们把 lock 清空一下，把两方 log 都清空掉，然后到 postman 里调用谁呢？咱先调用 trace B 一把，再来调用 traceok 那 trace B 的端口号是62,001，我们发送一条 get 请求。


三二一走。你好，看到它已经返回了，结果 status 200 trace B 好，咱把 log 给它放大。 OK 同学们看这里。这一行当中包含了两个重要信息，一个是它，另一个是它同学们是不是看这两个信息长得一模一样。因为咱当前的方法执行完毕返回，在这整个过程中并没有调用任何其他方法，所以这两个参数是一样的。那么如果你下游还有方法需要你来调用，你会发现这两个参数发生了一些微妙的变化。那咱接下来就直接调用一下 trace A 看会发生什么事情，咱的 trace A 会在方法的内部调用 trace bok 吹 C 的端口号是62,000，我们直接发起一次调用。好，这里已经返回了。那么回到 log 文件里面 OK 先来看一下 tre C 有什么变化，我们把 log 放大。好，大家看到 trace 是整个调用链路的起点，它的第一个参数和第二个参数是完全一样的。那我们不妨把这个参数先行复制一下。


我们接下来到 trace B 看一下，trace B 接收了一个来自 trace A 的调用。那在这个调用过程中，同样它也打出了一行 log 大家看这行 log 里面第一位的参数是不是和 Tracy 一样的？没错，我把这一行打出来给大家看一下。


这是咱从 trace A 中 copy 下来的，它和 trace B 中第一个参数是完全一致的，说明这个参数是谁呢？它就是整条调用链路中的 trace ID 也就是说不管你在当前的调用链路调用了多少个下游服务，那么在这整个调用链当中，都有同样的一个 trace ID 就是它。

[image](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/2cd97f6f-12f9-46ff-b67a-3ddccdc0ef76/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665ELUCSIN%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T225757Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDwvRryA0lMlct41QjKOnRp%2Bl9iSRSsA2Rhw0gzHLkghAIhAMeQiv9OZNOeOrMnhiJYgBmStxE%2BP6ZBik60cEPVzwowKogECMb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1Igz9JHnJIrMaqnzmBnMq3ANwwW9Q0t0%2BEny2qSvkWxFzNnHSZP24UI3fm1GTsZSnFRrxZp49cpaKEq9XmQVR4lcN5VtXJpn4kJTb%2FvSfl3L9kxWT7l5SEYjoZTYULAySHjvVWoL%2FO3nexkXR8EbwYANLZ9t82NnDzuM73F67UUzP47E3MgoRgiAd2t9K9qZDJJGZ27wPW3aqq913of3SF0T9fNULJkAQnzVf1coXTDYXRDzr727Vbpy7C%2F6ViuEVGlx3f70bE2h4XMEgpADJfeTlDgFrh7xt0jCPxxbhBTOXP8SQB7Cxu%2Bl7rM8zEYkuaomO9mSCuAE3QS%2BPxj9KByPlgauMzDjmZPpP79uggYqelJj7qw3GXuYijLHPvsrpYB86rYJfCp1u5QbI%2F9ZZF6pFImwN6fiqWNR4GTEG8%2FeRSQ5rQ08n1GlEWoFesOfIDrWbmehTkh0ucAJb7ZfXkOp%2Bxm%2FX9OiGdR4OFIzFQp6berB3C17MXiPqyrX0v8HwdNL1BQU2koX2jApiTfxj4f1Uhibgp8u4JPN6tsLR1p90dPiP2OT889eLRfwQzhsVofx9ovlFHARocRrspyLc2sLTGAFCdcX2tO01YtDPk4jApUTMgYDqgrtn0b4bPwSVVu5nqDDcm%2Fn5TABRnDCOuv%2FSBjqkAYC9AaUQhRMqIQQR5Pa7ltKwZ9jCXyiPEdY3%2BuAL1mBx0p2SiYxD0Xv0n%2FejV8aePIydw3fF0hrGplEOoLKTEv342RdQl2crgLSi1pMhZOqWF6M6ciYD6QpWAXLRE59w4u%2FpDSdB8WIgAFzemDetOojfuTFlgTQ9WMpUwBje8Crn3Ycv5oIOtnaZJOp12rdgXq8QcVxGrJF6t5bMDTsox4siDRqR&X-Amz-Signature=dba3b1cc795e41d5e665b4bc7d76e68e5f932b68c56edbf34d50337a207f5fe9&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

[image](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/23645d66-2768-442f-b61e-ce5b03d8dc20/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665ELUCSIN%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T225757Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDwvRryA0lMlct41QjKOnRp%2Bl9iSRSsA2Rhw0gzHLkghAIhAMeQiv9OZNOeOrMnhiJYgBmStxE%2BP6ZBik60cEPVzwowKogECMb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1Igz9JHnJIrMaqnzmBnMq3ANwwW9Q0t0%2BEny2qSvkWxFzNnHSZP24UI3fm1GTsZSnFRrxZp49cpaKEq9XmQVR4lcN5VtXJpn4kJTb%2FvSfl3L9kxWT7l5SEYjoZTYULAySHjvVWoL%2FO3nexkXR8EbwYANLZ9t82NnDzuM73F67UUzP47E3MgoRgiAd2t9K9qZDJJGZ27wPW3aqq913of3SF0T9fNULJkAQnzVf1coXTDYXRDzr727Vbpy7C%2F6ViuEVGlx3f70bE2h4XMEgpADJfeTlDgFrh7xt0jCPxxbhBTOXP8SQB7Cxu%2Bl7rM8zEYkuaomO9mSCuAE3QS%2BPxj9KByPlgauMzDjmZPpP79uggYqelJj7qw3GXuYijLHPvsrpYB86rYJfCp1u5QbI%2F9ZZF6pFImwN6fiqWNR4GTEG8%2FeRSQ5rQ08n1GlEWoFesOfIDrWbmehTkh0ucAJb7ZfXkOp%2Bxm%2FX9OiGdR4OFIzFQp6berB3C17MXiPqyrX0v8HwdNL1BQU2koX2jApiTfxj4f1Uhibgp8u4JPN6tsLR1p90dPiP2OT889eLRfwQzhsVofx9ovlFHARocRrspyLc2sLTGAFCdcX2tO01YtDPk4jApUTMgYDqgrtn0b4bPwSVVu5nqDDcm%2Fn5TABRnDCOuv%2FSBjqkAYC9AaUQhRMqIQQR5Pa7ltKwZ9jCXyiPEdY3%2BuAL1mBx0p2SiYxD0Xv0n%2FejV8aePIydw3fF0hrGplEOoLKTEv342RdQl2crgLSi1pMhZOqWF6M6ciYD6QpWAXLRE59w4u%2FpDSdB8WIgAFzemDetOojfuTFlgTQ9WMpUwBje8Crn3Ycv5oIOtnaZJOp12rdgXq8QcVxGrJF6t5bMDTsox4siDRqR&X-Amz-Signature=878e7fdd094d0176a29a2caff68604d584135058b818ae3c6f5a9f0e9351852a&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

OK 那后面的一个参数又是谁呢？后面这个参数就是分配给当前 span 的 trace ID 了，大家可以参照前面的图文教程，再熟悉一下 sluice 中的几个数据结构和名词术语。Ok.看完了这两个参数以后，后面还跟着一个 false 对不对？ false 是什么意思，它就是采样的意思了。如果咱 false 这里显示的是 true 说明这行 log 被收集了起来，就是被采样。那么如果是false ，那说明没有被采样。同学们可能会有疑问了，咱前面不是配置了采样率为 100% 吗？是的没错，但是咱还没有配置接下来收集这些 log 的组件。


等到后面的小结，我再来跟大家展示 smooth 的好搭档 zipkin 我们可以在项目中把经过采样的 log 信息输送到 zip king 里面。 OK 那么到这里本小节的内容就结束了，我来跟大家简单回顾一下。在这个小节里，咱创建了一对左右护脖树的兄弟 trace A 和 trace B 然后使用 tre C 调用 trace B 在这个过程中有这么几个关键的点，第一，在 pump 文件中，想要把 sloose 的 dependency 给它加入进来。第二不好意思，没有。第二了，sleutha就是这么简单，你只要把它加进来，它就会在后台默默的作用。


不过同学们依然可以覆盖 logback spring 的文件来定义自己生成 log 的方式。不过这里要注意，一定要把这一行也就是 log level pattern 以及后面的 5p 给它输出进来。否则咱的 slow 的生成的这些 log 打标 trace ID 是不会打印到 log 文件当中的。
除此以外，咱还看了 sleuthed 在 log 文件中输出的 trace ID 的格式，这一节的内容就是这些了。在下一节当中，老师带大家经历一场理论升华的课程，去深入了解链路追踪中的某些原理知识点，并且来一场源码阅读。 OK 同学们，那我们下一小节再见。


