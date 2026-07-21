---
title: 2-2 Spring IOC容器源码解析-1（1852）
---

# 2-2 Spring IOC容器源码解析-1（1852）

[image](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/e8d35c4f-00d9-4890-89f0-b1b8a75d8825/SCR-20240803-loyj.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665CGVOGOI%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T232001Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIEAmEPh0XbLdw8FJWVcb4Q2VhzxIJb1PK5l7GEOfq9qNAiEAla8BL%2FkQgCuya3qbDDXknrLRRJSKM6QDdzB6T0jpwrUqiAQIxv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDEA%2FCxSiLi16w1%2B5HyrcA2Ic6feXl%2FhHM4aAc00oMPmEsFG4CBHjA3DNjOLQCEu5ILVVDjj%2F6LvEDlQOMWLv6DtUwExFYfgQkfxGueL%2FOvoExAkdytpA8l3Y%2F243YJ%2BCKmia5CfZPc5XCQB0PAx0nONWXcHIy52GbM8Ju%2BCOGOwGerPlk1I8XqXoCgYFJm8y0DBSEZY7XB7I7gAJYjIxOrWFlS23nsyhJxEM2cr9D5NLLsSrhgLg0F%2F%2Fsbzogm3Lfrb4wex2xqJJZzIvLiLivfhtoXtXLmsBIjzQkjE%2Fp39XVPMydkDtoGAU00c6FXL7U5gV99RYDp0y52mDe4bHxLTWmd7deAlgEMAKXA%2BeJYTj4ywbVr6j25VpRbbbl%2FeaiGyrQB1QHO6zDrv2fJh3UDuxoLpoSQmgr5IhzZexpqAcnvGfZ9b3s1CohSs8CpHiFuKdwsQd2FwFnR4zBVR3HP8mCqSPi899NEOzLdJ%2B3E3DTa2PtdZBl0GnA8kIe7FtdFxZrGHcLYbSpHzaufjR7yBc1vJH1vYUTq09uHQp3P0gJHkPmOIFj%2FgucsBEqsZ6zToG0QHFAI%2B6BrVAjNe1Oj8tQ%2BRuS8N8msnwngg1SfthQFiGsKE0cDzxGSb3ndeHNCw5RjGdkYn5JxchML%2B5%2F9IGOqUBUfdWWIYazWsmm3KhQ0F86EddqmpO%2Fr8XMcBjFjRCqAk4nQgQYU3nMCHnz72xy9U3EhOrtagFZCiz%2Fyyte1Z65JqxuY1aGi892wA2qJx6yKB88Tbk0EPos%2BcnQbCOxlf6r9JXsvhFojyq%2BwYRRgT3f2vd1YW0paG8GEOIe6imWssjgT2MxDrOFlEJ%2Fycld9Oq12cheIADJFd6Y%2BW9ktIFAM70dpcW&X-Amz-Signature=48c3e1d9499da3dfafb92767266acb5a7ef1ccb7b7f5a194780c9ebd12958765&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

同学们大家好，这章节我们一起学习 spring IOC 容器的源码解析。 IOC 容器作为 spring 框架的核心，它的代码实现是非常复杂的，我们还是划分模块，聚焦重点，通过三方面给大家进行源码解析。首先我们学习 spring LC 容器的核心类，我们重点关注孩子 be infactory 的默认实现， debug list， stable being factory 和基于注解的容器，也就是 annotation configure applicon context being infactory 的，它的子类实现非常多。接下来我们分析一下 spring LC 容器之间的关系，也就是 be infactory 它这些子类之间的关系。


最后我们介绍一下 spin LC 容器的处理流程，这也是面试经常会问到的一些考点。好，接下来我们来看一下思准 LC 容器的核心类，最核心的类也就是 be in factory， in application context 以及它们两个默认实现。对于我们 appin factory 的默认实现，也就是 default list stable， in factory 和我们这里面对于注解的一个 application contact，也就是 application configure， application context。对于这两个类，我们会通过使用这两个类去理解一下它周边相关的一些接口和一些关联类之间的一些关系。


首先我们来看一下 debug 的disable， being factory 对于这个类它实现的接口会比较多，对于这个实现类，它直接实现的接口是三个，这里面是首先是 configurable legable being factory 和 being registry。通过这两个接口要说明两个问题，第一这个接口它具有 be infective 的功能。第二个对于这个实现类，它是一个 being defined registry，也就是说它是实现了 being defined 的一个注册表的一个功能。我们再看对于它下面的一些间接的一些继承的类，这里面有 listable being factory，可以通过它的命名能体现出来，其中还有 configure being factory 也可以通过它体现出来。这里面还有一个是 Automl capable being factory，它里面描述一些对于我们 bean 一些制动猪的一些功能。下面这里面我们可以看到是 syncto bean registry，这个跟我们这个注册表的功能是类似的，这个是对于我们那个别名的注册和我们的 being definition 的一注册，这是对我们 spring 容器里面 being 实例的一个注册。


好，我们来看一下这个 defeless 病 factor 它的实现，从这里面我们可以看到它的这个继承关系也是比较复杂的，我们看到这些相对复杂的这些类结构的话，我们一定要有自己分析的思路。对于 stream 来说，我们可以分析它继承的这些类和实现的这些接口，我们通过继承类了解它能把父类这些功能继承下来，通过它实现了哪些接口，可以知道它肯定对于某个接口实现增加了这个接口规范的功能。我们可以从这里面可以看到它继承的这些类结构，也可以通过这种方式看到它实现的接口，通过这里面可以看到它接口的一些展开的效果，通过这里面我们可以看，我们首先看它继承的类，通过继承的类来看，这是一个我们支持别名的一个注册表的一个类，它下面是支持我们的默认的单例的 bin 单例的一个注册表。


下面是 factory bean 注册器的一个支持。那么对于 factor being 是我们 spring 容器提供的一个给我们提供自定义构造 being 的一种方法。接下来我们看是 abstract b infactory，其实我们对于这种命名的话，我们可能不知道它是干嘛的，我们可以点进去看一下它的实现，在这里面它依赖了我们的 be in factory 和支持 pound factory，也就是说我们看它在这个里面实现了哪些接口，这里面我们它实现了 configure being factor，也就是说它肯定是实现了这里面支持的一些方法。我们可以看到这些方法是可以 at be imposed process 和添加一些集成的一个属性解析等等。这里面还有一些获取到我们的 convincing service 等等这项一些内容，我们可以看到这个是确实我们逐个去解决时确实是比较复杂的。


下面是 abstract auto capable being factory，我们可以看到它它是之属于这样命名的，是因为它实现了 auto cap apple being factory，我们基于这个接口的实现内容，我们去分析一下它里面的，我们可以看到这里面有 apply being post process 和我们的一些 out where 相关的一些操作。这里面还有 destroy bin，也就是说跟我们自动注入对于 bin 的生命周期的处理词有一定关系，这是我们可以看到这些类的思想，我们看到对应 default list， able being pack，它还有一个子，类似 XLB impact，但是这个类已经不推荐使用了，它主要还是基于测试的环境去使用。那么我们通过这种方式去看，对于我们这个 defailed list of being factory，它实现了这些接口，可以从这里面一目了然地看出来。


通过我们可以去先了解一些简单的接口，比如这里面别名注射器，对于别名注册器，我们应该实现哪一些操作，我们可以从这里面看到。首先在这里面我们可以注册一个别名，我们针对一个name，一个 being 的 name 可以指定这个 be in name 对应的别名信息，我们当然也可以把某个别名儿移除掉。下面的方法是判断一下给电字符串儿在使用容器里面它是否是一个别名，后面我们可以根据一个别人名称获取到它所有的别名儿。我们用过这种方式去分析的话，我们可以看到因为我们的 bin factory 它实现了 alert registry 这个接口，那么所以说 bin 容器具有给 bin 赋予一个别名的一个功能，这是我们对于这个别名的注册表的一个功能。


那么下面对它下面的一个子类，也就是 being definition Gestry，也就是说我们支持一个 being 定义，也就是 being definition 的一个注册，那么注册表它可以跟我们那个别名注册是类似的，我们这里面也看去，首先判断一下这个 being dimension 是否存在，我们可以获取到这个 being definition，同时可以注册并且也可以移除。
我们再来看一些 single Bing，也就是说单类 bin 的一个注册表的实现，通过这里面我们可以看到它提供的这些方法，其实跟前面两个注册表示很类似的。首先是判断一下是否存在，我们可以获取到容器里面的单栗的bin，也可以获得一下它的数量，这里面可以获取一下整个单列 bin 的名称，这里面我们去注册的方子，也就是支持它的写的方法。


好，我们回到PPT，我们可以看一下，这是实现接口和实现率相关的内容，对应时间类也就是这一些，这样 12345 这样五个时间类，我们可以看每个时间类的时间功能，去了解一下它继承了哪些方法。接下来我们来看一下跟这个底票的list，able， be in factory 相关的这些API。我们还有印象，我们在构建这个 being factor 实例的过程中，我们是首先需要一个 being reader，这里面我们选择的是 XML being defined reader。对于 being defined reader，它原来有三个实现，这是 XML 的，这是基于Grovid，还有一个基于属性文件的，但是基于属性文件的已经不推荐使用了。


其实我们早期使用最多的也是基于 XR 的，不过现在基于 XR 方式已经不再使用了，我们是基于注解的，但是基于注解的 being decony reader 和它并不是一个体系。我们在讲 application 的实现的时候去讲基于注解的 being definition，这是 being definitely reader，我们通过 being defined reader 去解析XL，我们可以得到一个 being diminish 对象，对于 being delivery 对象，它可以构建区分出，比如这是基于注解的我们的 bin definition 还有 abstract being definition。下面它可以区分成是 root being definition 或者是 child being definition 这样一个区分。


那么我们要解析一个 being definition，我们是需要指定我们配置文件，在 spring 里面，所有的配置文件都会抽象成 resource 对象，这个 resource 对象它可以分为，比如说 file resource 和 class part resource，在这里面因为我们用到了 Claude part resource，在这里面特意指出来，其实我们在解析这些 XL 的时候，我们对于不同的配置类型我们需要不同的解析的方式。比如说我们默认的bin，我们可能会有涉及到 UTOS AOP 和我们的 cats 相关的这些涉及到 XML 的配置，那么是需要指定一下我们对应的 NAMESPACE handler，那么 NAMESPACE handler 可以通过它不同的 handler 实现去装载不同的 bin 文件的配置。


那么对于我们 name space handler，它是需要通过我们的 URL 去解析的。这里面我们通过 name space handler resolver，根据我们传入的 URL 解析的对应的 name space handler，待会儿我们去演示 spring 容器装载流程的过程中都会涉及到这些类，接下来我们看一下 noticing config application context 这个接口的实现，对于这个接口我们是可以作为基于注解的一个默认的 application context，对于它来说，它实现的接口这里面有 configurable application context 这个它实现了 application context appex context，它实现的接口也是比较多的。这里面跟大家去介绍过了这些跟环境相关的跟列表。


b factory 这里面是 message source，跟属性文件，这里面是跟我们的事件发布机制相关的，这是我们的 resource partner，也就是我们的资源路径解析器。除了我们的 configure application connect，这里面还有一个 annotation configure registry，这是另一个注册表，这个可以理解，我们是基于注解的方式去解析我们这个bin，并且把它注册进去。下面是 bin definition factory，这个刚才在 bin factory 它的实现类里面已经介绍到了。这里面还有 resource loader，也就是说我们这个默认的 Pixel context，它是依赖了我们的 resource loader。


接下来我们再看一下它的继承类，对于这个阿皮克斯克袋子，它的继承类相对来说比较少一些，这里面我们可以看到它的继承关系。首先它是继承 Generator appticase context，其实是 abstract application contact 其中很大的一部分的代码实现是基于在 abstract application context 实现的，尤其是这里面最著名的 refresh 方法就在这里面实现，其实这个 apply using context，它又继承 defailed resource loader 这样一个实现的关系。


我们看到 a notation config application context，通过这里面看到它的继承类的结构关系，这两面相对来说是比较简单的，其实像 generic application context 它并不是抽象的，它也是可直接使用的一个实现。其实我们实现它对它扩展了基于注解的功能，我们更多的一些实现都是基于 abstract Pixel contact 去实现，因为它这里面实现的类代码量和实现的功能非常多。我们可以从这里面可以看到我们最重要的这个 refresh 方法，它就是在 abstract application contact 去实现的，上面是 debug result loader，这个来说是比较简洁的，它就是说它给我们提供了一个资源装载的一个功能。


好，这是我们那个继承关系，那么我们从这里面去看它的这个实现的，从这里面可以看到它的接口的集成，就是实现的接口是相对比较复杂的，我们可以看到它实现的接口非常多，像这里面我们可以看到这些词跟 bin factory 相关的东西。因为它是 application contact，继承了 bin factory，所以说对于我们的 a notisen config application context，它也实现了所有的跟 be infect 相关的这些接口，同时这里面有它特有的一个接口，像这里面是 a notation configure registry，这是什么呢？是基于注解的方式的一些注齿容器，我们可以看到在这里面它有两个方法，一个子addressed，也就是说我们可以注册一个 class 数组，这个 class 注主我们可以理解为它是基于 spring 的注解去包装的这些类，比如说我们通过 add configuration 去搜索的类，我们可以用这种方式注册进去，那么它就会对这个 bin 里面的这些配置去进行解析。另一方面我们可以去用scan，我们指定一个packets，也就是指定一个包名，我们整个扫描包的时候，我们通过哪个路径去作为我们扫描包的一个入口，也就说这两个方式都是对于注解一个变解析的一种操作。


好，我们再看其他的，我们都是已经看过了，这里面我们看有一个 close able，我们可以对于 application 来自动去关闭这些操作，我们看这里面是有一些 case 疑问的。 publisher 就是我们可以对于进行一个事件通知的一个机制。我们 application contact 它可以发布事件，也就是执行 police event，它发布的事件内容是一个 application event 或者它的一个子类。好，我们下面这里面还有是 please even 的，是一个object，也就是我们可以发布任一个对象作为一个事件。好，我们继续看一下跟我们这个 notisen Pixel contact 相关的这些API。


在这里面我们刚才也看到这里面是有一个基于注解的 bin defense reader，也就是说对于这个实现类，它需要加载的这些宾理平台是基于注解的方式，我们去有一个注解的一个reader，同时我们还可以基于 class Buzz 去scan，也就是我们刚才看到的一个 scan 的一个目录结构，是基于它去实现的。我们可以去扫描 Java 包里面指定的包，下面去扫描所有通过 spring 注解去注解的这些bin，并把它注册到容器里面。同时这里面我们的 being definition，我们这里面是列出了 notation being innovation，并且它的两个实现子类，这里面是基于SCAN，也就是说一个是通过包结构扫描出来的，另一个是基于注解去构造出来的变体平行的实现。跟 spring 相关的注解词非常多的，这里面列了几个。


首先我看我们的 configuration 和我们的 at being，这是非常用的，还有我们的 campaign scan，也就是说我们基于包注解的方式去扫描包结构的配子方式，这里面是component，也就是我们标明一下这个类似一个 spring 的bin，当然跟 campaign 的对应的还有像 at service， at Controller 都是和它相关的。下面还有一些 profile 相关的一些注解，我们可以去区分不同的环境。


我们接下来看一下 spring LC 容器之间的关系。对于我们 b factory 和 application context 大家应该是比较熟悉了，我们知道 application context 作为接口，它实现了 bin factory 接口，或者继承了 binfactor 接口，以及跟 Bing factory 相关的这些接口的实现，那么对于容器之间，此处用的容器会非常多，我们对于容器它会通过继承或组合的方式去做到代码重用。


其实在 Java 开发的过程中，我们知道继承是 Java 默认的一个三大特性之一，但是逐渐的话，大家已经不推荐使用继承的方式了，更推荐用组合的方式，原因也比较多。首先通过继承会把我们整个类放大，也就是让类变得非常庞大，因为继承只能单继承，所以说如果我们要做一些特殊的事情的话，通过继承是没办法完成的，所以我们建议通过组合来去完成这个思想。那么我们来看一下跟继承相关的案例，当然会非常多的。我们可以看到 a notation configuring application，它与 generic application context 这两个都属于 spring 的 LC 容器，那么它们之间就是一个继承关系。


同时我们可以看到 noticing configure negative Web application context，也就是说基于这个 spring Web Flex，它们默认的一个容器实践就是它继承了我们指定的 a notation configure ability context，就是说通过继承的关系去构建出这样一个功能的一些迭代，减少我们代码的工作量，那么这是继承的案例，那么我们来看一下一个组合的案例，刚才也看到了像 generic application context，它作为我们的一个通用的一个容器，那么它跟我们的变容器之间的关系是怎样的？我们可以看到在这里面它去构建了一个属性，这个属性是 detail 的 listable b impact，这个大家应该知道了，我们知道对于这个 Episync net，它虽然是继承了或者实现了 bin factory 相关的功能，但它并没有把所有的东西都继承下来去使用，而是通过组合的方式去使用。那么涉及到容器注册或获取的方式，它都是通过代理的方式执行 be infection 里面的功能去完成的。我们看这里面 resource loader 也是这样的。虽然说我们这个 appex contact 它实现了 resource loader 的对应的接口，但它并没有直接去手工实现，它也是代理通过 resource loader 这样的方式去完成的。


那么我们来去看一下这个 general application contact 它是怎么去利用这种方式的，我们到这里面看一下这个类，我们看到这里面对应的属性，我们是detailed，disable， be impact 和 resource loader。我们看一下这个 being factory 它是怎么使用的。此前我们从这里面去看一下，这里面有一个 get being 方法，就是 get being factory 方法，这个 get being factory 方法返回这个 being package 属性，那我们看一下 get bin package 方法，它是作为一个实现，那么我看一下这个 get bin package 在哪里使用，我们去点击这里面，我们可以看到这没有 get bin，我们获取的是 get bin 的一种各种方式。


我们点开第一个进去，我们可以看到这里面对于 get being 是 bin factor 给我们提供的一个方法，当我们在执行 get Bing 的时候，我们并没有去获取 bin 相关的内容，我们是通过 get being factory 这个代理去执行 get be in，也就是说我们在获取我们 Epixin context 相关的 get being 方法的时候，它其实是通过我们代理的这个 be infactory 去实现的。通过这一层我们可以看到其实就是 spring 容器利用主和的关系，把我们的方法转嫁到另一层代理上去委托我们的实现，这样减少我们的一些代码的成本。
我们再看另一个我们的 resource loader，在这里面我们看 resource loader 它提供了一些方法，是哪些方法？我们可以看到 resource loader 里面它提供的功能是比如 get resource， get class loader，那么我们可以看到这个方法里面它也实现了这个，我们给相同的方法看一下它在什么地方去使用，我们可以看到在这里面会也有对应的 get resource 方法，我们看如果说它在执行 get resource 方法的时候，也并没有直接去获取 resource 方法，它是通过我们的判断 resource 是否存在。如果 resource loader 存在的话，它通过 resource loader 的代理的方式去执行该 resource 的操作。这样的话我们可以看到其实是 spring 通过组合的方式的一些案例。

