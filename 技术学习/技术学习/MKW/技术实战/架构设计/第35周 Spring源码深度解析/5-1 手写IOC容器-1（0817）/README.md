---
title: 5-1 手写IOC容器-1（0817）
---

# 5-1 手写IOC容器-1（0817）

[image](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/db3fa9f5-7130-4b43-9eb4-a751d54339a5/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46647FD6WRO%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T232030Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIBPND%2BMS7tQ6%2FnwY5SY%2FCN3tPDrw6%2Fdc9c0Pye4NxMW%2FAiALM4xrZopn8%2FDpFxSEBDjtJ4WCwl2mo%2BDHaMIlXJLdbyqIBAjG%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMw6xAOJgaG0H3QMqoKtwDMNi%2BPEZc6IyfVkhenKjTjmMmyYXVQaUpQ6Cj42Jb1GnEptUNq7OwdtgT4hbzoPRG358FMQmSgYomiGeAolw4t70rT7GLn5zvgXaPMnvAbx9xD6vx%2FH9Qov5ceX4k4WJypmH5L5C%2BosATHiZ50auBBL1qjMPGFMpOFlR67Ox7vYy%2Fi6SECdqADhuz8H9BFatXO2nYuqVEULN1hbftxghQ2CN3as%2FRSzOqiFgrnNYy5t95Do%2BfJO3y%2FurL8t6InS7oyr5UWC0dJZINmghb3hjm0EKqu8c1w6otJ4q6CtTrp%2FOOcd049d11a%2FVCTbolCDnpXgP85WdHO9KWtsQUE%2Bjvsu1BXEv9gd2xn5tovBYUrM9zxrFki95cGzOUVtkM5sJAzrvKzgGWWxKGP0GjRseYn%2B%2FkPjSdaGeY5QgVh8mUatW%2BI%2Fz%2Bo7MU7wHL26dJem8%2Frr82x80BwMGT%2BdotkgL6kRAtNDT0GWgO3IB9WnR3y%2BCQU3cELo5vQ3KbiL2D0rtPzK%2BVEk%2BE0dtEIi01f0j7v%2BL3BOSzUUJpQcoQgj9Cnxaxl6OBU%2BHt9f%2FwY9MU1Fal4QGcRQTKiHg9WGHlTjbO3HoPM8I3eJeF4zlCFuf6iYMI5CLe8jao%2B9pOLhswgLf%2F0gY6pgHbjMDleT4d%2BrykqnA2US0NkB76RAWD2XWdwTw2yDnlTRtEWQq7rctRcfzsgGzkFvILbWDXyybKATXTwLbagrJ7SBN6rVxev%2FGxFemp%2Ba4SPX5AJralkJBwwl2zxTOli9h42ioOZrH8eyVyLOY3HR9Qe8byToCzlWeKx6YxmkiFYakmssoN50eGe9GBa4xc4cMr0f8bn3XkpaDR82HS2VdjUKliWLoR&X-Amz-Signature=e8f114803bd483c06fc07b4ca45e41bb22260491810a676f2906c943705a8d49&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

同学们大家好，这章节我们来介绍 spring 造轮子的手写 LC 容器。 spring LC 容器它的设计是非常复杂的，而且提供了很丰富的一些可扩展的一些接口，那么在短时间内我们实现完整的 IO c 容器，且其次很不现实，我们使用开源的技术也经常宣扬我们要不要重复照轮子。为为了让大家更好的去理解 LC 容器的原理，我们在这里给大家实现一个相对简洁的 LC 容器。那么在实现这个 LC 容器的过程中，我们先回忆一下 spring LC 容器的一些核心类，在这里面我们还记得最重要的也就是 being factor 与 applixin context。这里面我们可以看到我们这里面默认的容器是 de 飘的list， able being factory 以及我们使用的注解容器一般是 annotation configure， application context，那么我们在这里面搜写容器的话，我们就可以参考 bin package 和 Pixel context 这两个类去实现我们这个功能。


在我们使用我们的 LC 容器，我们现在一般是基于注解，那么我们要不要定义自己的注解？其实我们现在完全没必要定义我们的注解。我们知道 IOC 它是一个规范，我们基于规范来实现，当然 Java 它也提供了 IOC 的注解的规范。我们回顾一下我们原来介绍的 string LC，它实现了三道注解规范，分别是基于 string 自己定义的，像 add component 以及 JS 250，这里面是基于 management bean 去来去定义这个 bean 以及 GSR 330，它是通过 name 的这种方式去定义bean，其中实现了 inject 和 synct 这样的一些注解。那么我们在这里面我们可以看到只有这个 at component 它是 spring 的注解，其余的都是加 x 提供的这些规范。那么在这里面我们可以选 J S R 250 或 J S R 330 这里面的注解去实现。对于这里面我们因为使用最多的注解项，比如 resource 使用是非常多的，所以说我们可以选择 GS 250。


我们同时在这个简洁的 IOC 容器，我们实现 Mandarin p 以及 resource 这两个注解的解析，这样的话可以完成我们一个最简洁的一个 LC 容器的一个过程，我们会通过扫描一个包结构，那么扫描这些类里面哪些类使用了 manager 的 bin 这样一个注解去修辞，那么我们把它加载到我们对应的容器里面，说明它是一个被容器管理的类。
同时我们去关注一下这个容器管理的类里面哪些属性是使用了 resource 去助理修辞，使用 resource 修饰说明它进行了依赖注入，那么我们需要解析这个属性的依赖注入它对应的 bin 的是否实例化的一个过程，所以说我们通过对 manager 的 bin 和 resource 这两个注解，完成我们 Bing 的定义和依赖注入的完成。


那么我们接下来看一下整个这个我们要实现的这个容器，它启动的流程是应该怎样？我们先回顾看一下 annotation config application context 它的处理流程，我们知道我们可以手工的去通过它的默认构造方法去构建出一个对应的 application context，然后我们在这里面去注册扫描bin，同时把我们需要扫描的 bin 注册进来，我们这里面可以注册对应的 Java configure class，也可以注册一个包结构，那么我们这里面会选择在这里面是注册一个包结构，那么接下来它会进行刷新方法与repress。因为我们在注册的过程中，我们可以理解为它对于 being 的一个整理，它只是在这个过程构建出来 being defined 对象，那么只有在刷新 refresh sponsor 时候，它会通过调用 get bin 的方式把我们的这个 bin 的初始化，这样的话完成了我们 bin 的初始化，那么我们就可以从 bin 容器里面获取到我们的bin，那么我们来进行 get bin 的操作。得到 bin 的话，我们进行我们 u 方法的处理，我们当时演示的是 hello contact 的一个 say hello 的方法，通过它去执行我们的you。执行完业务以后，最后把我们这个 application connect close 进行关闭掉，这样也就完成了我们整个这个容器的一个执行流程。


那么接下来我们来去开始手写我们的 LC 框架。首先我们这里面创建一下我们一个新的模块儿，这个模块儿就是我们的 spring 创建轮子，那么好，我们下一步在这里面我们去。首先我们定义我们的名称是不用。well，好，这里面我们把 activity 先改一下，我们下一步完成在这里面构建。完成这个模块儿以后，我们接下来要做的事情就是去添加依赖。那么对于这个新的模块儿，我们已用词造轮子，那么我们要造一个简单的容器，当然我们在照容器的过程中，我们不能再去依赖我们的 spring 相关的一些内容。


那么我们在这里面去添加哪些依赖？通常我们去开发工程的时候，我们要不依赖spring，要不依赖一些对 common 的一些工具类，那么我们这里面首先把我们的 common 浪这个工具类，这是我们一般在写代码经常会用到的这样一个工具类，同时我们还有我们的 long book 是必不可少的，但在这里面我们要写日志，我们 look back，还有也就是我们在写过程的单元测试。好，这是我们一般在开发过程中必须的一些内容。那么同时我们在这里面要实现我们对应的一个注解，那么这里面注解我们是选用的对应 j s r，这里面的是 250 的注解，那么这里面我们需要依赖添加上这样一个注解，这个注解是我们这里面写一下它内容就是 im tation API，我们加上这几个注解来开始去实现我们的代码功能，同时我们也需要把我们对应的源码包里面去把我们的这个 logbug 文件去配置一下，这里面我们就参考我们 customer 里面的内容，直接对应拷贝过来就可以。


好，那么接下来我们还要做一些什么事情？我们还要做的一个事情就是首先来把我们的包结构建起来，建起来以后我们要做的就是我们一个演示的一个demo，也就是说我们需要写框架，那么我们什么代码用我们的框架，我们需要把这样一个内容去构建出来，我们先在这里面建一个空的 packet info，那么我们这里面也是参考我们 customer 里面的内容。


在这里面我们可以看到我们定义的being，就是我们写的一些 you 方法，那么在这里面我们可以先建一个模块，这个模块我们建个包，也就是Demo，那么我们把这里面的内容全部也拷贝过来，我们注意一下，拷贝过来是有一些问题的。在这里面首先我们可以看到，因为我们这里面已经不依赖 spring 了，所以说像 repository 这样的依赖我们是应该清理掉的。那么清理掉我们这里面应该怎么做呢？我们刚才写入了我们现在依赖的是我们的 GS 250 的注解，那么对于 GS 250 去修辞一个 BN 的话，它是它是这样，是 manage 的 bin 用这种方式去表示，我当前这个类被容器去说修辞，所以其他地方几个我们动静地也去处理一下，去做一个替换。


这里面的对应的outwide，我们的自动出入，我们需要改成对应的resource，我们的 Demo service，我们看 Demo service 已经去处理了，那么在这里面我们简单去修改一下，把它去。满足我们当前这个ChatGPT。同时我们在这里面不做太复杂，我们还是基于属性，我们不用做构造方法的注入。OK，我们看这里面这几个内容我们都已经修改完成。好。

