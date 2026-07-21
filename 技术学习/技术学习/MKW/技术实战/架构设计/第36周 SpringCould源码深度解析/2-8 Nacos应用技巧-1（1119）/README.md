---
title: 2-8 Nacos应用技巧-1（1119）
---

# 2-8 Nacos应用技巧-1（1119）

同学们大家好，这章节我们介绍一下 NICOS 的应用技巧。前面我们介绍了 NICOS 架构设计以及使用 spring Claude。阿里巴巴集成 NICOS 的使用场景，了解了 NICOS 与 spring Claude 集成的服务注册与发现及动态配置的原理。那么对于不使用 spring Claude 场景，我们应该如何集成 Nicos 呢？今天给大家介绍一下更单纯的使用 spring 和 spring boot 这两个场景对 Nicos 集成的使用方式。第一部分我们会介绍一下集成 Nicos spring，第二部分是集成 Nicos spring boot 以及第三部分我们还是基于 spring code 来完成了 Nicos 动态配置的实例。我们来首先看一下如何集成 Nike spring，那么对于集成 Nike 的 spring 就是我们在程序开发过程中没有用到 spring boot，也没有用到 spring Claude。那我们单纯使用 spring 项目的话几种方式，在这里面 NICOS 它提供了一个叫 Nike spring product 这样一个项目，那么这个项目我们可以看到它本身它并没有在阿里巴巴这个 group 下面，它是单纯的一个 next group，那么基于 next group 它会做一些 next 周边的一些事情。那么接下来对于这个 next group，它对应的一个栅包，我们可以理解为 next spring contact 这样一个栅包，它也基于 Maven 的 bus 进行发布。


那么另一个我们要看一下我们的一个 Demo 实现，也是基于我们的 yes 模块 Nike spring 这个模块去演示如何继承 Nike spring product 的，那么我们首先来看一下这个 Nike spring product，它所处的位置在这里面，在 get help 上它有一个 next group，我们看 next group 里面都有哪些东西。这里面有 Nike single，也就是说它会把 Nike 和 AK 它们之间的一些数据进行一个同步，也就是说我们都是作为配置中心。那么为了更好的推广 nicos 的话，我可以把你 ZK 的这些元数据同步到nicos，也可以把 UROC 上面这些元数据同步到nicos，这样减少大家迁移的一个成本。


这里面有 nicos K 8 s，还有跟 nicos SDK 的 CSA 这一个客户端，这里面有跟 go 语言的客户端，这还有我们用到的 nicos Docker，它基于 Docker 实现的一个包装，我们可以直接把它 check 下来，直接启动我们的这个 nicos 服务。


下面我们可以看到这里面有 nicos spring boot product，还有后面的我们的是 Nike stream product，中间我们还看到跟 Nicos SDK、 NODE js 和 SDK 的 C + +，显然语言相关的内容。


有一点我们要看到其实这些我们这些我们可以理解为 Nicos group，它一些周边的这些服务，这些点它的热度肯定不如 spring Claude、阿里巴巴和 Nicos 本身我们可以看到 Nike spring product，它的标签只有 600 多个，对于 Nike spring boot product 它只有 500 多个，这还是整个在这个 group 下面标新量最高的。


那么我们先来看一下我们关注的 next stream product，它里面实现了哪些东西？对于 next stream protect，它里面是几个模块，一个是最主要的，也就是我们用的是 next spring context，这里面还有一个 neck spring simple，也就是一个样例，那么我们可以基于这些案例去学习一下怎么去使用。


那么对于这里面有个问题，因为它早期Nicos，它为了支持更早期的 spring 版本，这里面依赖的 spring 的版本是比较低的，这里面我们可以看到它依赖的 spring 的版本仅仅是 3. 18，所以说这个版本确实是比较低的，因为我们现在在开发过程中主流都已经用上 spring 4 甚至 spring 5 这样一个版本，因为我们在这样一个过程，在使用这个案例的时候有部分可能在启动的过程会有一些问题，这个大家根据报错简单排除一下基本上都能解决问题。 2.


那么对于这里面实现的内容，我们可以打开看一下这个 Nike spring context，我们看到它的时候其实还有一些很多四层相似一些面熟的一些东西。首先这里面我们可以看到它是有一些对注解的一些处理的一些插入，这里面还有我们看这里面有context，这里面对于注解的定义，这里面是 enable negos，这里面还有我们的跟 configure 相关的，跟我们的服务注册与发现相关的一些配置，这里面还有 config XL，我们看这里面是甚至定义了一个 nicos name space Handler。
我们看到这个对应的 name space Handler，我们应该明白对于它是支持基于 Xmail 的一种解析的方式。其实我们可以基于 Xmail 的方式去配置 nicos 相关的一些信息，这里面是对于 notation driving 和 global property 和我们的 property source 相当于一些配置信息。


在这些我们就不再演示了，我们还是基于注解的方式给大家去演示，只是告诉大家基于这个 nicos string 的这个项目，它实现了很多功能，这里面还要跟四件相关的一些内容等等，这是整个这个项目的一个大概一个结构，我们看这里面一个情况，接下来我们看如何去使用这个 Gecko 子分 context 来完成我们对于跟 Gecko 的一个集成。那么好在这里面我们还是切回到我们的 spring code study。在这里面我们构建了一个工程是 Nicos spring，虽然说我们这个 Nike spring 这个工程它支持我们在不使用 string 布的，也就是纯原生 string 的基础上去完成它的集成。当然我们也可以去 string 布置的工程依赖它来看到它产生的一个效果。那么首先对于这里面我们是需要引入对应的 nicos string context 的，因为这个本身 Nike string context 它的版本更新是比较慢的，我们就选用它最新的版本就可以了。


底下的这些内容也就是我们常规的依赖这里面 long book 和我们的 stream start test 和 stream book start Web 一个Web，工程，那么我们看一下这里面我们写了哪些东西，在这里比较简单。


首先我们看对于我们这个 nicos stream application，它一个入口类，那么我们这里面跟我们对应的 nicos configure 它的实现内容是一致的，也就是说这里面我们只是在启动的过程中打印了一下我们关注的在 neckles 配置的一个属性，那么其他的还有什么呢？我们看这是 necks Controller，那么我们基于 control 我们来实现了一个 configure 的一个URL，一个mapping，那么基于 configure 我们获取到对应的这个属性的配置，也就是说这个属性配置 username 它是通过 nicos value，也就是说我们 nicos value 就是远程获取到的一个配置项，那么在配置这个 next value 的过程中，我们这里面还设置了一个字词自动刷新，也就是说当我们的远程配置更新以后，这个值也会发生变化。


那么这样一个过程，那么我们再看一下最关键的，这里面 negos configuration，对于 next spring 这个项目，这里面的配置是最重要的，我们可以看到，首先上面是我们 long book 的一个日志配置 S2 for 接日志，另一个是 at configuration，我们标明一下这个类下面都是我们配置对应的一些d。


那么接下来我们看我们还配置的是 enable nicos configure，也就是说我们首先开启了 nicos 的一个动态配置，在这里面我们配置的一个内容，我们是在 global property 里面设计了一个设置的是 nicos property，也就是跟 nicos 相关的一些全局的一些配置。这里面我们因为其他都是默认值，所以说我们只需要设置了用 Server ID，也就是说我们 nicos 服务的地址在这里面还是我们 nicos i m local 888。那么另一个就是我们设置了一下我们开启 in nicos，并且 nicos 的地址。


接下来我们需要配置一下我们监听的 Nike 的这个属性配置文件是什么，这里面我们定义了一个 data IDS my user，并且也让它开启自动刷新。这里面我们跟我们使用 spring code 集成的效果去一个比较，我们在使用 spring Claude 及集成的过程中，这里面我们需要配置对应的是 Boost strap property，那么我们使用直接使用 next spring 的话，我们这里面是在通过 enable next config 来配置了一下我们这个 nicos 的服务地址，同时我们是通过 nicos protostore 来配置一下我们监听的 data ID，对应了我们的配置文件。


好，我们看一下这里面我们的阿飞克森 YML 里面，这里面配置比较简单，这就纯粹的我们跟 strong 布的相关的一些配置。好，那么我们现在已经程序已经启动了，启动完成以后我们可以去访问一下，那么我们这里面对应段口号是8011，我们看8011，并且我们的 UIR 是configure，那么我们在这里面去访问一下试试。好，我们看现在我们得到的是对应的 GMV C4，我们一个改进的过，那我们看一下当前这个值的效果，我们可以点编辑，现在它有一个更新的一个过程。好，现在我们看到 user names 对应的是 GMC 4，那我们可以对它进行一个修改。我们如果说把它改成C5，我们再看一下这里面它更新的一个变更，那么我们点击发布。那这里面我们来看一下我们的日志的一些输出，我们发现当前是 on change string，它有一些变化了。好，那么回到我们这里面的这个请求，我们看一下这里面的它也已经发生变化了，这说明我们通过单纯的 spring product 来进行集成，也是集成的，没有问题。


那么这里面我们看到在对于我们这里面的配置，我们使用的了是 nicos config listener，这是什么意思？就是说我们基于一个注解去监听我们这个配置的变化，我们关心的内容是我们的 my user，当我们的内容发生变化的时候，我们输入这个 on change string，那么当它进行执行的时候，我们看到 on change string 这样一个内容，那么它输出的内容是什么呢？就是我们发生变更的这个 KV 的值，这里面就是对应的 user name GMV C5，也就是它发生变化了。


我们从这里面可以看到，如果说我们不使用 spring code，和我们单纯使用 spring 相关的工程的话，我们也能做到去监听配置的变化，能做到这个配置项来进行一个实时的更新。如果说我们需要关注某个变化去做一些处理的话，我们可以通过 nicos config listen 的方式去完成。要注意的是我们跟 nicos 相关的这些注解也好，这些操作也好，它的命名都是基于 nicos 这种方子去命名的，所以说我们基于 spring Claude 来做的过程中，这些命名它不推荐我们的 spring Claude 里面使用的，所以说当然我们可以用这种方式去完成我们的业务，但是跟 spring Claude 集成的时候，我们尽量不要用针对某一个具体的一个实现。


我们通常还是基于我们的整个环境的一个变化，比如说我们的involvement，一个 change 的一个事件来监听这个过程，这是我们的一些动态配置。那如果说我们涉及到一些动态，我们的服务发现的话，我们可以看到这里面也有一个叫 naming service，那么基于 naming service 的话，它可以获取到指定的一个 service name 的所有的一些实例，我们可以看到这一些实例的一些信息。那么在这里面我就不太跟大家一演示 naming service 来，因为这里面它是使用一个 neckles injected，也就是说 next 一个注入的注解去完成的。但是因为我们在 string 的版本比较高，它这个注入是有一些问题的，告诉大家有这样一种方案我们可以可以使用，但大多情况下我们还是基于 spring Claude 来完成就可以了。关于使用 nicos 不用这个项目集成我们的 nicos client 端，我们就先介绍到这里。

