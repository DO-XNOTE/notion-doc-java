---
title: 3-2 【扩展作业提示】RPC框架以自定义注解方式与Spring整合辅助讲解
---

# 3-2 【扩展作业提示】RPC框架以自定义注解方式与Spring整合辅助讲解

[image](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/fc63a4df-2515-4722-81fb-b86bd7b66244/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XN7JB3BY%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T230049Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQC1rER7lAOgueqGaxz98TGXpRReUI6gzyKt03WbHMT6egIhAMBHWCbpZGx17y%2Fe8wiG0IA4yqcpm5WfwEvXcrQ0VONZKogECMb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgyuzakTHF9F6f1Dbi4q3AN7P5RvfXuqBR71bycbrNeIw71Ede8nwldGShBPtsOXINKHJDA9FLqgOsVh%2FOjNb0HkwpR1514bQkaBJSmKnalk7HhQurt99I%2ByfGnrC45KfyTvYRtFVX1HiAnCyoweukDrf%2BRqd3dvU7wnS5UAh0KYMYPL0zzuF8cOKFPhx%2F8cBik3rV0tcYODUXNLTd4nncdQdnoCRFWUKkRgOBBlt5AWSPYEAwM2n5Wit1RTSzyDpk9QH3%2BSZlEBiMt9vQFITJ6ftatcFj9U4cAv6Wik5neiKn0yvVZi97XwiwuetJNDXwnzcVL0Et%2F90Uw7J%2Fzi4QY%2BdJg3iZiw8H5MfFGBMEu%2B57Z1JZIR8cV7qjKIgO52Nv4cJg8nEuzKkAnnw7%2B0RPbfSV7XpQd3yZCXw7JrHKMKKV9dF%2BV0oKytrA3wW6q%2FGcm%2FrGhuIOsrmcZ5VmstLd3vFdjd5zocpQC6zjRvLckOA8bpLEUpbJ5DEEKPHhU533cRF2r1qxp3Rga2iRXpAT36am8A9VZKPu9H%2FDKzD12P47GkfzaR8U2zvEAbA7g15v0vV7NdChez7SCgOUhdhsXE6QTu6PaalIAH1XJfizrncRvBoxpCjQ1GxRU1%2BvCn%2FN6LeH0tjp9QhlAb0jDyt%2F%2FSBjqkAZbc9%2F0z%2BjjiON6Vz3m3lquSctBL9F8yOetqqjYpYcLyLgziGyYltYSeysFbWbC2x9Bg2UGI3evxPbx48oGGSkHaBw1%2BUJePGg2HnaHHz4sroKk%2FmOW7yfXbN6yDxXmUwBBJfYFlA4LNBtDLXdU1qfFAxz2AqK7o5pweVZ9FAiTVXHexCyN2DAybpAjKs%2FyzVGsuDvt307uV8A2HrSJ3%2BvHJUZr2&X-Amz-Signature=62f48088218543613a63ce2aa5d97ad8fe12fe3cf9b1a29701e429f804c2c281&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

OK，小伙伴们大家好，这节课我们就开始来说一下第二个小的扩展作业了。相当于制作中心来讲， JK 来讲可能稍微有一点难度，所以老师给咱们准备了一个相对应的代码，来降低咱们小伙伴的实现的难度。说白了，第二个作业我们想把我们自己所实现的 repeat RPC 要跟我们的 spring 进行一个集成。怎么去跟 spring 集成？其实在我们之前跟小伙伴们去讲的过程中已经说了无数次了，说了我们整个要复杂的。


这幅图其实老师已经帮你们提出来了，一个叫做 provider config，还有一个 consumer config，这两个对应的什么？这两个对应的一个比较上层的类，其实我们只需要把对应的具体的 service 实现对吧？具体把对应的 service 在注入到 spring 之前，加上我们自己的管理就可以了。相当于把 provider config，又或者是 consumer config，它的具体的一些注册信息，相关的注册内容，把它帮我去注册到 skin 中就可以了。说白了什么意思？我们的 user service，它的父类，或者是它注册之前它肯定是跟 user service，它自己的配置肯定对应着有一个 user service 的 provider config。我的 hello service implements，它对应着应该也会有一个 provider config。同理服务的调用方就是我们的 client 端，相当于 consumer 端，哈，也是一样的，它的调用的接口它也应该有一个 consumer config，对不对？它另外一个也 work service b 也应该有一个 consumer config。


其实回过头来，我们去看到我们之前写代码的时候给你的测试，你可以看到我们的 provider 要做的事情是什么。很简单，你可以认为我的 spring 再去加载 user service 具体的实例的时候，其实很简单。 user service 具体的实例我们都知道，如果你要用 spring 集成，你要做一个什么 at service？这个 at service 注解，它会帮你把实体 bin 变成一个单例的模式，然后去注入到 spring 容器中。这个小伙伴们肯定知道 at service， at component， at repository 都可以去做。
小伙伴们如果你用过double，你就知道 double 里面也需要写一个注解，也是一个 at service，只不过那个 at service 就不是 sprint 了，是我们阿里巴巴 double 的艾特service，他自己实现了一个自定义注解，把自己的类去帮我去交给 sprint 去管理了。


他为什么要自己去做注入？是不是？他为什么不是直接用 spring 的注入，而是非得用 double 的 service 去注入，不用 spring 的service。原因是什么？原因是他注入的过程之中可能还有一些自己的操作，比如什么？比如他去做自己的接口的一个 export 导出的工作。


说白了，我们应该怎么去做？小伙伴们应该去参考 double 跟 screen 整合使用注解的方式，到底是怎么去做的。也就是你需要加一个你自己的注解。你现在不要用 spring 注解。比如我们现在说我现在有一个自己的注解，我说叫做 at repeat 这么一个自己的注解，这样自己的注解就会帮我把这个类直接去注入到spring，让 spring 帮我去管理这个类。而且它也是个单例。但是在注入的过程之中可能会有几步。比如最关键的一步是什么？它帮我把 hello service 里边的 provider 生成。因为我们最终目的是干什么？是要一个provider，对应的一个接口，对应的一个实例类。这个实例类有了接口，有了它，帮我在注入的过程中生成对应的provider，帮我去注册到 server config 里面就可以了。这是 provider 需要做的事情。


同理， consumer 也是一样的， consumer 在注入的时候是不是也是写自己的一个注解？我个人觉得对于大体的实现流程，小伙伴们应该都没有什么太大问题，但是比较有难度的，可能你自己不愿意去翻一翻。其他的开源框架怎么去跟 spring 集成的。如果你知道 double 跟 seven 集成的，那你就应该明白了。在这里老师给小伙伴们写了一个单元测试。这个单元测试主要做的事情是什么？自定义注解的作用就是在 double 的时候，它在 scan 启动的时候有一个 double component scan。首先它要做的是我要扫描哪个包，下面扫描什么包对不对？扫描什么包，我给你定义好。这个包下有自己的自定义注解，比如repeat，把我自己自定义的注解都扫描出来，帮我自己去注入给 spring 这么一个事情。所以老师现在已经实现了这个事情了。一会儿我们简单就看一下代码。


我们先来看一下测试。我现在就是一个普通的 spring boot 这么一个工程，就是一个普通的 spring boot 工程。我们看到了我们引入的就是 215 包starter，加上 test 没了，我已经实现自定义注解，让他帮我去交给 spring 管理。其实小伙伴可以看test，你看到这个test，你可以理解为后面这两个包下的实现，就是我自己对于自定义注解的实现。这个老师也参考了 double 的自定义注解，它是怎么去跟 spring 集成的。我希望小伙伴们应该去好好看一看 double 怎么去跟 spring 集成的？在这里老师已经把答案给你们了，我们来演示一下。很简单。


我现在就有一个 hello service，这个 hello service 它没有去加任何 spring 的注解，对不对？我注解它也不是派生注解，它就是一个圆注解，最基本的叫做 repeat 注解。它也没有去做一个派生，它又是一个什么？艾特 reporter 或者艾特斯维斯。这是我自己自定义的一个原生注解。我自己的原声注解。我去把 hello service 去定义一下。是不是我去把 user service 去定义一下，我就可以做测试了？看见了，我做测试的代码就是这么简单。看见了吗？我说 autowear 的，直接注进来。我直接就可以用自定义注解把它注册给super，我们去 auto where 就直接注进来了。注入进来了之后，我去调用一下，看看行不行，看看能不能取到值。调用一下 hello test 和 solo test。 hello test 就是 hello test user test，具体的实现就是 user test。好了，我们把这个事情我们运行一下就好了哈。在这里我们直接采用 unit test 的方式去做一个运行。好。小伙伴们已经看到结果了，是不是他已经把具体的实例类帮我去注入给 spring 管理了？这是我自己注入的，我也打印出来了。


hello test 跟 user test 说明什么？说明我们自己的自定义注解已经生效了，对不对？我们自己在我们自己的类上加我自己的注解，交由 spend 管理。到底是怎么去实现的？我在这里简单跟大家说一下。我期望小伙伴们仔细去看一下 double 跟形成怎么去整合的。说白了它需要几步骤。
第一步骤是做一个扫描它。首先在这里边要定义一个什么，要定义一个 component scan，我要扫描哪个包下的，我自己进行注解。我在这里定义好了之后，然后它是通过这个类 component scan。它会有这么几个参数，比如扫描 value package 到底是什么 package class 其实跟 double 是一样的。注解定义好了之后会扫描它指定的就是你添的包下所有的 repay 的注解。最后帮你去注入到spring。


核心在哪儿？核心在这儿，从这儿开始看从 repeat component scan register 开始看，我们点进去看一下。最核心的方法就是在这儿叫做 private package to scan，看见了吗？它把你具体的 annotation 注解解析出来之后，然后取到它具体注解上的 3 个属性。取到之后去做一个解析。解析完了之后去返回对应的一个集合，就把每一个目录都返回成一个 set 集合，最后返回了。


哈，看见了吗？ package name class YouTube 点 package name，它最终就把你注解下面到底对应着哪些类，直接给你返回了。给你返回一个 set 集合，他自己去调 set 集合。我们看到叫做 register bin definitions 返回 set 集合，叫做 package to scan，他就去对他进行具体的扫描。当然具体扫描细节，你可以看一下上面比较关键的方法，就是叫做 root Bee definition，在这里边它又进到了。它具体怎么扫描的？它其实是进到了。


这个叫做 repeat annotation being post processor，看见了吗？这是非常核心的 bin post processor，里面做了什么事情？我的 repeat annotation being post processor，它必须要实现。这个接口是非常重要的。这个接口叫做什么？叫做 bin definition registry post processor，还有下面这几个。这个方法其实你会看到，它最重要的就是 bin post processor definition。这个是干什么？就是 bin 定义的一个 post processor 之后的一个程序执行器。这也是我们 spring 的一个切面的一个点。我们去干什么？我们第一步取到了 package to scan 之后，我们去 reserve 去解析，解析完了之后，我们去 register 就一个一个的把它解析出来的目录。我们去找到具体的一个的类，去做一个注册。点进去看一下你就知道了。点进去看一下，你看到这些都没什么可说的哈，比较简单。从这开始，这是比较关键的。


我 scanner 是干什么，它就能够帮我去扫描。指定目录下面指定的注解。我扫描的条件是什么？ include 包含什么，包含filter，包含注解的类，它都会帮我去扫描出来。最终它会调一下 do scan 方法帮我去扫描。


扫描出来了之后，我们看这里边我也有一些注释哈。首先循环获得所有的注解的类，取到它的 bin definition holder 丝，这里边 scanner 把它进去了，它获取所有的bin。 definition holders，最终找到了 definition holders，之后去循环 definition holders 最终注册的过程。这是最核心的，叫做 register service bin 对不对？他这个方法其实真正的去调注册了。我们点进去看一下。你看，其实我就可以在这个时机去做一些我自己的事情。我在注解上我能取到类上有注解，我注解上是不是我定义了什么东西，我是不是都可以取出来去做我自己的一些逻辑。我说的这一块的逻辑，其实我们自己最开始做测试的时候就硬编码的时候。还记得吗？小伙伴们，我们做硬编码的时候做什么事情？我们的 provider starter 相当于你把硬编码的这一段逻辑，你把它变成注解去通过注解去把它实例画出来就可以了。


让我们具体的每一个实例接口，还有实例对象生成一个 provider config，把 provider config 跟我们的 r p c server configuration config 去做一个绑定关系。它的绑定关系很简单，就是一个 export 方法，在这里传一个 list 列表绑定起来就可以了。其实你就可以在这里去做。最终绑定完了之后，这里边 register 你都有了。
register 大家都知道我们最核心的叫做 bin definition registry，通过他调他的 register definition bin 方法，就可以真正的去注册对不对。我的 bin name 是什么，你可以自己去定义你的 bin 是什么，我们可以写这个叫做 bin definition。


bin definition 在这里我就不想特别详细去讲，因为我们老师给你参考的是 double 怎么去跟 spring 整合的一段代码，我把它 copy 了一下，在这里简单的去做了一个演示代码，到时候也会发给小伙伴，小伙伴们可以参考它。你就要实现以注解的方式使用什么。使用我们的 r p c 的框架跟 spring 进行一个整合，你可以先实现一半。比如你先实现什么？你先实现我的 provider 跟 skin 整合，再想 consumer 跟 skin 整合，再想什么。因为上节课我们已经说了，如果你能实现 z k 去接入进来注册中心，再想加上注册中心，

[image](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/0b88c2b7-3baf-4925-a942-41675f8a5e77/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XN7JB3BY%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T230049Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQC1rER7lAOgueqGaxz98TGXpRReUI6gzyKt03WbHMT6egIhAMBHWCbpZGx17y%2Fe8wiG0IA4yqcpm5WfwEvXcrQ0VONZKogECMb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgyuzakTHF9F6f1Dbi4q3AN7P5RvfXuqBR71bycbrNeIw71Ede8nwldGShBPtsOXINKHJDA9FLqgOsVh%2FOjNb0HkwpR1514bQkaBJSmKnalk7HhQurt99I%2ByfGnrC45KfyTvYRtFVX1HiAnCyoweukDrf%2BRqd3dvU7wnS5UAh0KYMYPL0zzuF8cOKFPhx%2F8cBik3rV0tcYODUXNLTd4nncdQdnoCRFWUKkRgOBBlt5AWSPYEAwM2n5Wit1RTSzyDpk9QH3%2BSZlEBiMt9vQFITJ6ftatcFj9U4cAv6Wik5neiKn0yvVZi97XwiwuetJNDXwnzcVL0Et%2F90Uw7J%2Fzi4QY%2BdJg3iZiw8H5MfFGBMEu%2B57Z1JZIR8cV7qjKIgO52Nv4cJg8nEuzKkAnnw7%2B0RPbfSV7XpQd3yZCXw7JrHKMKKV9dF%2BV0oKytrA3wW6q%2FGcm%2FrGhuIOsrmcZ5VmstLd3vFdjd5zocpQC6zjRvLckOA8bpLEUpbJ5DEEKPHhU533cRF2r1qxp3Rga2iRXpAT36am8A9VZKPu9H%2FDKzD12P47GkfzaR8U2zvEAbA7g15v0vV7NdChez7SCgOUhdhsXE6QTu6PaalIAH1XJfizrncRvBoxpCjQ1GxRU1%2BvCn%2FN6LeH0tjp9QhlAb0jDyt%2F%2FSBjqkAZbc9%2F0z%2BjjiON6Vz3m3lquSctBL9F8yOetqqjYpYcLyLgziGyYltYSeysFbWbC2x9Bg2UGI3evxPbx48oGGSkHaBw1%2BUJePGg2HnaHHz4sroKk%2FmOW7yfXbN6yDxXmUwBBJfYFlA4LNBtDLXdU1qfFAxz2AqK7o5pweVZ9FAiTVXHexCyN2DAybpAjKs%2FyzVGsuDvt307uV8A2HrSJ3%2BvHJUZr2&X-Amz-Signature=ed49451079621f8a0bca0e1dea3264a18f069a0079a55e1bcfed9128b1901f87&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

我们应该怎么去做。我们第二个作业，这个作业也算是比较有挑战，当然挑战的难度已经降低了很多，因为老师已经把自定义注解这块怎么去做，跟小伙伴们简单的梳理了一下。讲了一下这节课，我们就讲到这，我们整体的 RPC 的课程到此就结束了，感谢小伙伴们收。


