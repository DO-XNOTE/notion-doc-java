---
title: 2-2 RocketMQ源码解析-认识RocketMQ源码（1852）
---

# 2-2 RocketMQ源码解析-认识RocketMQ源码（1852）

[image](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/09891cc3-18d5-404d-a8d0-041eb8987575/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SFHW2TET%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T232222Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIF9a42x%2Ff0%2BUXfKLqfTYVNswAUYoFXIVqWaT09UvLibvAiAsqkcp2J%2BOeGIgDb9eNtxqvR5QTyRf2rlmfszF4U1ZPyqIBAjG%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMF23S94MoGckAULHUKtwDg2pJpOA4zHM%2BAYV1aIT1Y0rSjYIMqtRaNb4V5z2axZYA1oKO%2FCKN7RsvSG9uONicfOJGK572LET5GYIkiMlBaeOxxIx13HVXsGe4k6rFvaUvt9FNbxG5xJx4mrnXcseFbN0RlDrLzy3oSD9HiF0bIFgk%2FYWwB%2BgAYI5wCUBbkvJk39jeEGYIGeXDrrObmIfRTmt23I4EQutWdVePWdecm6VndXBrKukKBYaSxkkybDvqvbfp89dXchvrdo12pf0ChwcOcwCuGDP3Jqgkh3NH7od2yYbE3IZKJPAGRQaoVee6P%2B1QIbm8uFIGwB7cUlW8LJ6iSb09MKtvJRTVBD9acWsQfRibzUsN4TTyZarjZ9xvVDUutlCoA5kZmb6vxLSG7puxpb5FpK4gRizLsQ0%2B0I7%2F5mM5cHdYwzQWbJpBnvEE%2BRSELL3iSLHnMJTa5WxFgGJYveId3joi1aXez1MUgGxLw7%2B2q6SuwErW0J2Q7Wpgn6Oe0xHNqUcessvMFiEWypfc4Wnw7np75kqZ6h1h6NHt%2F3m4O4glx%2F0AW8994peukb1DvX%2FbHXHxUXXZO8HtBk1af4K7hiwMWWXZzdDHILc0dmzXU6RdOolKaB5Cf5dmZuwLN3razJVwV0kwyrj%2F0gY6pgERQj%2Bt6AAybIcXIiE7Jl275CX87E3NKPYZAZymdY47I97Cay2jIXAIqWMHbV68H0AJsuDi7GJ%2F2I2XI2hqfvwS0WqkRz3vKThVT2ZWzpg7SkQK706Ya0BKtisxpy9GKXr8UWdNBmG%2FKLTWKBNUzlY3jqntcGArKznTCjpC0KGHfCZMPBD2ndlz8wsFDkRu8lDoMBTXbI0POYFhcym6wGY9Osk3WWNC&X-Amz-Signature=2cd752ede85d1c72f5a508bf45e4213d26cdb88436d419598e6b7228346674a3&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

[image](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/4df44f62-7a32-4b04-bf30-2bf726efd94b/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SFHW2TET%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T232222Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIF9a42x%2Ff0%2BUXfKLqfTYVNswAUYoFXIVqWaT09UvLibvAiAsqkcp2J%2BOeGIgDb9eNtxqvR5QTyRf2rlmfszF4U1ZPyqIBAjG%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMF23S94MoGckAULHUKtwDg2pJpOA4zHM%2BAYV1aIT1Y0rSjYIMqtRaNb4V5z2axZYA1oKO%2FCKN7RsvSG9uONicfOJGK572LET5GYIkiMlBaeOxxIx13HVXsGe4k6rFvaUvt9FNbxG5xJx4mrnXcseFbN0RlDrLzy3oSD9HiF0bIFgk%2FYWwB%2BgAYI5wCUBbkvJk39jeEGYIGeXDrrObmIfRTmt23I4EQutWdVePWdecm6VndXBrKukKBYaSxkkybDvqvbfp89dXchvrdo12pf0ChwcOcwCuGDP3Jqgkh3NH7od2yYbE3IZKJPAGRQaoVee6P%2B1QIbm8uFIGwB7cUlW8LJ6iSb09MKtvJRTVBD9acWsQfRibzUsN4TTyZarjZ9xvVDUutlCoA5kZmb6vxLSG7puxpb5FpK4gRizLsQ0%2B0I7%2F5mM5cHdYwzQWbJpBnvEE%2BRSELL3iSLHnMJTa5WxFgGJYveId3joi1aXez1MUgGxLw7%2B2q6SuwErW0J2Q7Wpgn6Oe0xHNqUcessvMFiEWypfc4Wnw7np75kqZ6h1h6NHt%2F3m4O4glx%2F0AW8994peukb1DvX%2FbHXHxUXXZO8HtBk1af4K7hiwMWWXZzdDHILc0dmzXU6RdOolKaB5Cf5dmZuwLN3razJVwV0kwyrj%2F0gY6pgERQj%2Bt6AAybIcXIiE7Jl275CX87E3NKPYZAZymdY47I97Cay2jIXAIqWMHbV68H0AJsuDi7GJ%2F2I2XI2hqfvwS0WqkRz3vKThVT2ZWzpg7SkQK706Ya0BKtisxpy9GKXr8UWdNBmG%2FKLTWKBNUzlY3jqntcGArKznTCjpC0KGHfCZMPBD2ndlz8wsFDkRu8lDoMBTXbI0POYFhcym6wGY9Osk3WWNC&X-Amz-Signature=03e2f6f156f6d82869d7b06dab936a1a817e7b856153559682144ff876958d48&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

同学们大家好，这章节我们开始学习 rock MQ 核心源码解析，认识 rock MQ 源码的部分。首先我们是介绍认识源码结构，这部分我们通过官网来了解对 rock MQ 的介绍，以及通过 get him ear 了解源码结构，同时也会把代码克隆下来，基于 idea 去分析各个模块的功能。


第二部分我们是启动部署 rock MQ，那么这里面对于 rock MQ 的部署主要是为了我们单机的学习测试使用，那么这里面我们为了开发 rock MQ 部署，我们可以基于Docker，也可以基于我们官方的 release 版本进行解压进行启动，同时当然我们也可以直接基于源码进行我们启动的认证。


第三部分是我们基于我们部署的开发版的 rock MQ，来进行验证我们消息的生产和消费，接下来我们看一下我们要学习 rock MQ 都涉及到哪些源码部分。通过这里面我们看第一个，也就是我们的阿帕奇下面的 rock MQ，这是整个 rock MQ 的核心，也就是它对应的 name Server 和 BROKER Server，以及对应的 client 端，以及我们数据存储相关的内容，都是在 rock MQ 这部分，那么这是我们可以理解为 rock MQ 最核心的代码。


那么第二部分这里面我们介绍的是 rock MQ 的dashboard，那么这里面我们可以理解为它是 rock MQ 给我们用户展示的一个 UI 界面，也就是一个控制台，我们可以基于这个 UI 控制台去了解一下 rock MQ，它进行消息的主题生产，消费一个个 broker 的一些运行状态。


那么这里面我们看第三部分，这里面是对应的是 rock m q 的stream，那么 rock m 的 stream 它其实是对 rock MU 克兰德端的内容进行一个包装，这里面注意一下，它只是对克兰德的内容进行包装，它通过 spring boot 自动装配功能，让我们对 rock MQ 的使用更加方便。


这里面会给我们自动装配对应的我们的 rock MQ template，可以提 template 方便的发送消息和接收消息，这是在阿巴奇的官网，下面还有几个跟 rock MQ 相关的一些模块，这里面我们就不过多介绍了，这些模块也有对第三方语言的适配，也有一些扩展性的一些信息。


那么对于这三个模块来说，也就是三个 Git 仓库它对应的模块，我们这里面看它最重要的是我们的 rock MQ 的 name Server，以及我们的 rock MS BROKER，这两个功能模块是比较重要的。那么基于我们的 name Server 和 BROKER 它的一些依赖，比如说像一些 common 包，一些 cleaned 包，以及我们的一些 remote 远程调用相关的一些内容，那么他们会做有一些依赖。


这里面另一部分就是 rock MQ client，那么因为我们作为业务开发的同学，其实更多的情况下是跟 rock MQ client 进行打交道，那么对于 recommend client API 我们要了解清楚，这样的话我们再跟我们的 recommend Server 去执行。数据交互的过程中有些问题我们可以快速的定位。


这里面是 rock MQ spring boot，我们可以看到它其实就是我们的 rock MQ spring 这个 Git 仓库下面的内容，这里面分了几个模块， rock MQ spring boot 是存储了主要的一些业务逻辑，通常对于这个 rock MQ spring boot，它为了遵循 spring 的 boot 对应的规范，它会构建一个对应的 rock MQ spring boot STARTER。那么这个 STARTER 我们知道它只是一个基于 Maven 的一个管理的这一个模块工程，它里面并没有实现过多代码，它只是把对应的一些依赖引入进来，那么这里面我们简单介绍了一下我们需要了解到的 rock MQ 与源码相关的这些 Git 仓库，以及它里面模块的内容。


接下来我们来看一下阿帕奇 rock MQ Git 的效果。在这里面我们可以看到这里面是我们对应的 rock MQ 这样模块，这里面的模块内容非常多，我们可以看到这是我们对 get have 的一个截图，里面能展示出一些关键的信息，比如它的 store 数，或者它的 so 欢迎，整个这个 so 欢迎程度，其这个指标可以理解出来。


本身我们可以看到它的更新是非常频繁的，里面是近八天都有更新，也有刚刚有发布最新的我们的 Lark MQ 对应的 4. 2 的这样一个 release 版本，那么我们现在可以切换到我们浏览器来看一下官网的效果，这里面我们可以看到它对应的这些模块划分的非常多，具体每个模块的功能，我们可以基于待会儿 idea 的源码里面把每个模块进行展开一些介绍，这样基于 idea 对于源码结构的介绍会更方便一些。 9.


我们在这里面可以更多的去了解一下作为 rock MQ 在 GitHub 社区里面受欢迎的程度。这里面我们来切到对应的 rock m 官网的效果，这里面对于 rock MQ 它已经从这里面可以看到它是阿帕奇的一个顶级项目，那 rock MQ 它是一个统一的消息处理引擎，同时也是一个轻量级的数据处理的平台，我们看下面这几个关键特性的介绍。这里面对于低延迟，它可以在高并发压力下面能做到高于 99. 6% 的这些响应的延迟是在 1 毫秒以下，所以说这个还是相当不错的。


另外这里面对于 rock MQ 它可以进行面向金融，我们知道金融对于这个它的准确性要求非常高，所以可以看到它提供高可用的数据追踪和一些审计能力，对于金融的支持还是比较不错的。我们看到这里面它是一个产业，是可持续发展的，它可以支持万亿级的数据的稳定性保障。


下面我们可以看到它其实对于供应商是一个中立的一个态度，它这里面怎么去介绍呢？我们可以理解它就是开源中立，就是说它支持我们协议，相对来说也比较友好，我们可以直接使用对于这里面的是大数据一个友好的 big day， big day 的friendly，也就是说支持大数据的一些友好的一些支持。同时对于 rock MQ 它也有了大量的积累，尤其是在阿里巴巴内部的话，有大量的使用，尤其是像阿里云，在云上也提供了 rock MQ 的支持，所以说它的可靠性和它的一些业务积累还是很丰富的好。
那么我们回到我们的 Git Hub，我们可以看到这里面后面我们还列出了几个跟我们 rock MQ 相关的几个模块，这里面一个就是我们的 rock MQ despite，也就是我们的控制台，也就是当我们把 name Server 和 BROKER 部署访问称以后，我们可以部署我们的 rock ambug dashboard，去看到我们系统里面消息流转的一些情况。下面后面这是我们的 rock spring，刚才也跟大家介绍到了。


如果说我们为了更方便的去使用 rock mirror 发送消息的话，我们可以基于 rock mirror stream 里面提供的对应的是 rock campaign stream。不知道 STARTER 在我们的业务系统里面引入可以方便我们去使用对应的 rock mail template 的这样一个工具类。后面我们开看到对应的是 rock mail 一个扩展的一些内容，看这里面的 star 型 3. 9 k 还是相对比较高的，这里面提供了一些扩展的一些功能。


好，接下来我们看一下 rock m 的源码，这里面已经把对应 get 工程下面的 rock m q 二这个工程区域已经克隆下来了，这里面我们可以看到它各个模块儿现在正常编译启动，并没有启动正常编译它没有报错，那么这里面我们可以看到对应的我们根的palm，这里面定义了一些model，对应的 client common broker TOOLS， thought 等等许多。那么这里面我们重点去介绍哪个，一个是我们的broker，另外是我们的命名服务器，我们的 name Server，通常我们部署的功能是需要先去启动我们的 name Server 的，所以说这里面我们来看一下 name Server，对于 name Server 的话，它依赖的内容我们可以看到这里面是首先它依赖了我们的 rock Cabug client 以及 rockmbuild TOOLS，这里面是 SRVU to 也就是一些工具。


那么这里面我们可以看到这是一个可启动的模块，所以说我们打开我们的 URL 情况，我们可以看到这里面有一个 name Server start，那么这里面有对应的 main 方法。那么我们通常在启动我们的 name Server 的时候，即使是通过 cell 命令间接的去启动我们这个 main 方法，这里面会进行一些参数的解析，执行一个过程，那这是我们的 name Server，那么我们来看一下我们的BROKER， name Server 启动完成以后就应该启动 BROKER 了，那么在启动 BROKER 我们可以看到 BROKER 的依赖也近似。这里面是有 rock and common 包，我们知道 common bug 是存放一些公共基础的一些内容，这里面还有 rock MQ store。我们知道对于broker，它的实现过程要远远比我们的 name Server 实现更复杂。 name Server 我们可以理解为它只是一个注册中心，一个路由，那么这里面也不涉及到过多的数据交互，那么 BROKER 时间就会非常复杂了。


BROKER 它首先是需要去用户中心注册，需要跟我们的 producer 和我们的 consumer 都去建立链接，同时我们还需要对 broker 数据之间的一些复制备份，或者说一些主从同步等等一些思想，我们可以看到这里面有数据存储相关的内容，还有 rock MQ remoting，也就是远程处理的一些内容，同时也依赖了 rock calendar 等等这些信息。我们可以看到里面还有对应rocketfilter， a C， l 这些信息。


好，这是我们的 broker 信息，除了我们的 name Server 和broker，近次的也就是我们的 client 了。我们知道 client 是我们依赖 rock MQ client 这个大包在已有开发过程中非常多，它里面的内容主要是一些消息，客户端包含消息的生产和消费都会用到这里面的一些内容，我们可以简单去看一下，这里面我们会用的比较多的，这里面会对于producer，我们经常会用到 debug 的 MQ 的producer，这里面是我们在手工构建我们消息发送的过程中经常使用，那么这里面还有 consumer 端的内容。


这里面我们看到更多的一些例子，我们会用到是 debug 的 MQ 的 pool consumer，那我们打开看到这里面其实很明显的标志，这个 consumer 它已经不推荐使用了，这里面有描述它会在 2022 年会进行一个removed，其实时间也不长，所以说我们在新写的项目的时候就不推荐大家去使用这个 MQ pool consumer，那么这里面它提到了一个更好的实现，也就是我们 debug 的 letter pool consumer，也就是它上面的这个我们的一个实现。那么我们基于它去进行我们消息的消费。


好，这是 client 一些内容，那么后面我们来可以看一下对应的是remoting， remoting 它提供的内容主要是一些远程通信协议相关的一些代码。基于Netty，对于 rock MQ 的通信部分是由 native 去实现的，大家这个知道，对于底层的一些细节你可以去了解一下。对于 star store，它是进行一些我们的消息数据持久化，进行高可用相关的一些代码，其实这块内容的实现也是非常重要的。后面我们可以看到一些简单的像一些filter，这里面 filter 和这里面的ACL，对于 filter 我们可以理解它是做一些消息过滤相关的一些事情。


a C， l 也就是我们的防控制列表，它是做一些权限相关的一些信息，那么这里面我们先简单了解一下 rock MQ 它的一个 b 的结构，接下来我们来看一下是 rock i Mute spring，那么我们看到 spring 的代码结构会有一些莫名的倾斜，因为我们对于 spring 的缺的比较多一些。这里面我们可以看到对于我们的 rock m 和spring，它下面的一个功能模块，从这里面也能有一个一的一个对应关系，这里面我们这是对应的一个模块儿，这里面我们看到是三个模块儿，一个我们的 spring boot parent，我们的 spring boot 以及 spring boot starter。


注意一下这里面我们看了 spring boot samples，它默认没有引用进来，所以说如果说我们需要学习它里面的代码的话，我们需要在选中 palm 文件里面，这里面有一个 Maven mail，默认没有引入的话，它应该是 add Maven，你就加增加为一个面板工程，我们就可以看到这样的效果了。


如果说我们默认打开的话，这里面是没有这个点的，我们可以看到它是一个被加载的一个源码状态，那么这里面我们看它的一个model，这里面其实也是它的一个编译顺序。那么我们在基于 rock m q stream 打包的过程中，它会首先去进行 rock m build stream parent 一个处理，那么我们看一下 parent 做了哪些处理。我们看到 parent 其实相比 spring 的一些模块对 parent 定义，它通常只是一个 power 文件，把我们的 dependency manager 的信息进行管理起来，其实这里面也是我们可以看到对于 fast json，我们的 SRR for 阶这样一个门面的API，就是日志门面API，这里面有对应的 spring API contact 相关的一些内容，这是 rock IMU client 相关的信息。


通过这里面我们可以知道对于我们的 rock IMQ stream 部的parent，它其实做的事情主要也是把我们的依赖进行一个版本的管理，在里面对于各种版本的一些数据的标志，那么我们了解了point，我们接下来再看一下我们的 spring boot，那么这里面的 spring boot 呢？其实它实现的功能会比较多一些，我们看它的代码量还是比较多的，那么这里面我们看对于 spring boot 它依赖了哪些内容，这里面 spring boot 它依赖的是 spring boot 相关的信息和 spring boot auto configuration，以及 stream block communication process，也就是我们的一些配置处理的一些信息等等。


我们可以看到这里面有对应的 rock communication client，那么我们看到这个我们知道它是实现了 rock campaign client 与 string 部的集成的一些能力。那么我们再看对应的我们的STARTER，那么 STARTER 实现的内容非常简单， STARTER 它只是引入了我们的 rock MQ stream boot 以及 string boot starter，同时这里面还引入了 validation 以及一个验证的功能。


那么对于一个 string boot 相关的一个插件或者是一个主键也好，它在里面体现最多的就是它的自动装配功能，那么自动装配功能我们怎么去寻找呢？我们通常对于 resource 下面我们找到我们的factories，那么这里面我们可以看到 rock MQ auto configuration，看到这个类的话，我们找到了对于一个 spon 布的功能，它的核心的入口，那么这里面我们通常打开我们的 rock m auto configuration，我们进去看一下。


对于这个类的话，我们看到它这个制动装配类的实现，对于这个类里面它完成了哪些信息，我们可以从这里面去看一下。我们首先在启动的过程中，它会去构建我们的 debug MQ producer，那么接下来我们可以看一下这里面还有一个 debug letter pull consumer，从这里面我们可以看到对于我们的 auto configuration，它完成了我们的 rock MQ 客户端的构建。这里面的客户端主要是一个我们的消息生产器，消息消费的就是生产和消费的两个非常重要的组件。我们可以看到后面这里面我们包装出了 rock time q template，那么包装 rock m template，这里面 rock MQ template 它是我们的 rock spring 这个模块构建了一个我们的发送消息的一个工具，那么这个工具它构建的过程我们可以看到它依赖到对应的 rock MQ master convert 的消息的转换器，那么它在处理的过程中，我们可以让它也会把我们的 producer 和 consumer 分别放到我们的 template 里面的属性里面，也就是说我们的 rock and Michael template 是依赖我们的 producer 和 consumer 的。


OK，那么看到这里面我们知道对于这个 auto configation 它主要的做了哪些事情，那么其实这里面还会有一些，比如一些肯迪森条件相关的一些信息，这里面会做一些简单解析，比如说我们的 class 上下文是依赖 MQ admin 的，同时这里面的前缀 rock MQ name Server 是需要有标记的。不过这里面有一个明确 method if missing，如果说没有匹配的话，它默认值也是true，OK，下面还会有对于 method convert configuration 的一些装配的一些依赖，我们可以简单点进去看一下，这里面构建出了一个 rock MCN master convert。


好，我们回来，下面是我们一个 listener container 的 configuration 等等一些信息。好，那么关于我们这里面的 rock m q string 的内容，我们先介绍到这里面，接下来我们来去看一个，我们这里面是 rock MQ dashboard， rock dashboard 它是一个 spring 布的工程，我们可以从这里面去看到。对于我们引入了 stream application，同时这里面一个 main 方法去启动基于 APP 的启动方式，那么这个同时它也是一个包含一个前端的一个工程。那么这里面前端的代码我们可以看到它是在我们 resource static 里面会有一些样式相关的一些信息，这里面其实我们最终可以把我们这个 rock MQ dashboard，它可以打包成一个可运行业炸包，那么在可运行炸包其实它运行的过程中需要唯一指定的是什么呢？指定一下我们的 name Server，那么这里面我们需要去配置一下 name Server 的值，假如说我们没配的话，它默认是 logo house 的9876，但如果我们线上的服务部署的过程中，它可能跟我们的 dashboard 是不在同一个机器，所以说这里面还是需要指定一下我们的 IP 和对应的端口号。


那么其实这个功能它实现的逻辑是比较简单的，只是去跟我们的 name Server 进行我们数据的传输，那么去获取一下线上的一些指标信息来进行一个传输过来，那么这样的话，我们把我们的 rock MQ dashboard， rock MQ spring 以及我们的原生的 rock MQ 的源码结构跟大家做了一个简单的介绍。


现在我们回到PPT，那么我们接下来看一下我们启动部署 rock m 相关的内容。那么我们要部署一个本地可以使用的 rock m q，并且因为我们是本地开发使用，其实并不要求多高的高可用，所以说我们可以基于 release 的版本进行解压进行部署，其实也可以进行我们的源码启动部署，那么我们把 rock MQ 的源码已经下载过来了，其实我们可以直接在对应源码里面的 name Server 的 main 方法进行启动，或者 broker 的 Server 进行启动。同时也有一些简单的方法，比如我们可以基于 Docker pass 进行部署，所以说至于我们本地部署的话，这三种方案我们都可以。


但是有一点要求，其实我们源码启动部署这部分我们自己需要去完成，因为我们在进行我们的源码 debug 的过程中，是需要依赖基于源码的款式部署的。那么另一种方式，对于 Docker 部署和 release 版本部署，这个其实两种方案只要我们能实现，就可以对齐我们源码的我们的消息发送或接收的验证，这里面不做强制的要求。
但是其实因为我们在这里面部署的过程中，对于 Docker 我们还需要部署对应的 rock MQ dashboard，这里面对于 IP 和端口的设置大家一定要注意一下，否则的话，如果说基于 Docker 部署的话，我们基于我们的 rock m dashboard 在获取信息的时候可能出现一些问题，所以说如果说我们单纯使用 Redis number 进行部署的话，就会简单很多。他们的数据，尤其是 IP 和端口之间关系的，因为我们可能都在同一台机器，那么我们只是关心端口就行，对于我们的本地 IP 又比较容易处理。


