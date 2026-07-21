---
title: 4-2 OpenFeign核心源码解析-1（1506）
---

# 4-2 OpenFeign核心源码解析-1（1506）

同学们大家好，这一章节我们来介绍一下 spring Claude open phone 的源码解析。那我们在介绍 open phone 的过程中，我们也是分两部分，一部分我们介绍它初始化的过程，另一部分我们介绍它执行的过程。那么初始化的过程我们还回头看一下，其实对于 open phone 的话，它初始化的入口我们可以理解为它是这个注解 enable phone client，那么它基于这个 enable pen client 开启我们这个 fin kind，一个 register 以及一个注册的一个过程。整个其实在 fend 看 reject 的过程其实有调用后面的方法。


那么接下来我们通过源码来去分析一下整个这个执行的过程，那么在这里面我们还切到我们的工程模块，在这里面我们看到对应我们的系统入口，那么我们程序的入口是对应的 neckles open phone Demo application。那么在这里面我们执行的过程中，首先我们看到它这里面有对应的 enable phone clients，这里面同时对于它依赖的其他的，像 enable discover client 和，其实这个并不是必须的。那么如果说我们不使用服务发现的话，我们直接配置 URL 也是没问题的，那么基于这个 enable phone client，它会做的事情是什么？它其实要做的事情就是需要去扫描我们整个容器里面使用了 enable client 这样一种操作，那么在这里面对于我们 enable cleaner，它这里面定义的是name，也就是 next provided 这里面的 name 的意思，其实它跟 service ID 是类似的，那么我们通过这里面注册一个 service ID，同时在我们这里面也涉及了我们的服务注册与发现，那么也就是它会通过我们的服务注册中心里面查找这个 service ID 对应的我们的服务的名称。


那么找到对应的资源列表，获取到我们的服务器的列表以后，通过最终的负载均衡的策略，找到我们对应的我们的服务端的一些URL，这样执行我们的数据。那么接下来我们来看一下你那部分 client 它执行的过程。首先我们知道，当我们在执行 spring bool application 启动的过程中，它最终会去解析这些注解，比如说像 spring boot Pickagson，它会解析这些自动装配的内容，那么像 enable discovery client，它会自动去进行注册 Python 相关的内容，那么这里面 enable 份 client 它就会去做一些解析我们的 enable 这个 fun cleaner 的构建的过程，那么我们可以跟进来看一下。


在这里面，对于这个 enable fun cleaner，它这里面有一个import，一个register，在它以 Pod 的过程，它其实相当于是就进入进行一个解释执行，那么解释它执行的过程中我们看到它是实现了 import being defendant register，还有后面像是 source load aware 以及我们的三角标环境变量的一个 aware 的操作。


那么在这里面的话主要的是执行这个对应的操作，在这里面我们可以看到它执行的方法，也就是这里面是实现的是 register bin definition，就是在注册 bin 的一个过程，这里面其实有两个方法，这两个方法我们可以从这边看，它们的区别是有一个是指定了一个 b name Generator，也就是在生成 b name 的时候给一个指定的方法。但其实对于这个我们实现的过程中，它其实只是调一个默认实现，也就是相当于是直接依赖了我们的 adjust bin DP 的应用操作，所以我们还是回到这里面，其实我们只关心这一个方法就可以了。


其实在执行这个方法的过程，首先是需要去我们看到这里面是 resist defailed configuration，这样我们点击进来跟进来，在这里面去首先去注册我们默认的这些配置，那么其次在我们做 open FIN 的时候，它有一些默认的一个 defer 的配置，还有可以指定的我们针对某个 service 名称的一些配置。那么在这里面我们可以看到它执行的过程。


首先我们从 Meta date 里面去获取我们的 notice attributors，这里面它通过看一下我们 Meta date 里面是否有 enable 在 client 这样一个注解，那么当然它因为通过这里面去发起的，所以说肯定这个注解是可以找到的。


找到这个注解以后，这里面它会对于它的内容转化成一个map，这里面比如说就是其实它的内容就是对于这个底份的分刊的这些属性的一个 map 映射，这样他接下来去处理的事情是什么呢？先判断一下它不等于now，那么接下来看这个属性对象里面，它是不是包含 debug 的 configuration 通常是包含的，那么只包含这个 k 就可以，那么它里面的内容是需要我们重新去注册的，那么在这里面我们得到它的信息以后，在这里面去再去校验 match day 的相关的信息，那么这里面它通常会执行 debug 相关的一些配置。


接下来就去进行我们对于 resist trend configuration 的注册，我们看在这个注册的过程中，它最终会构建出一个 being dependent builder，这个 Bing defending builder 它是通过我们这里面看到是分 client specification 及这样一个对象构建的，那么这个对象其实我们在 load balance 的时候，也有一个类似的一个这样的一个对象，它其实也就是对我们这些配置项的一个描述，同时它也是实现了 name 的 context factory。这就是说我们在配置一些特殊的配置信息的时候，基于它去一些去配置实现。
这里面我们看其实在构建的过程中它传入了两个参数，这两个参数都是基于构造方法传入的，第一个参数是name，第二个参数是configuration，也就是说它通过我们的 name 和 configuration 对应的信息去构建这个对象。那么在这里面我们可以看到在构建这个对象的时候，它一个默认的构造方法，这不是默认，这是默认构造方法，这是有参数的构造方法，分别是 name 和一个configurance，一个指定类的数组。这样它其实是使用了第二个构造方法来构造我们这个 bin 构造完成以后，它就把这个 bin definition 注册到我们的 register 里面，也就注册到我们的注册中心。其实这个主人引擎可以理解为我们这个 bin 容器的上下文环境，也就是 bin 容器的一个register，这里面我们会定义一个名称，我们指定的这个 bin definition，这样的话它这个就我们就相当于是执行完成了。


那么我们接着回到我们的方法，可以看到这里面，接着再向上而回到，好在这里面我们看这是我们注册完我们默认的这些配置项以后，我们接下来需要 regist 分client，这就是说其实一个是指定我们一个公共的一个 configure prepage，另一个是指定我们分 client 一个特殊的配置。那么在这里面配置的过程中，我们看它是在获取的过程中，首先去得到我们对应的一个 enable 分 client 词相关的一些信息，它看这个属性里面可以从这个属性里面去查找是否有client。也就是说我们在配置这个注解的时候，我们有没有去指定一下 client 信息，也就是说如果有指定 client 信息的话，它其实在这里面解析的过程中，会对这些 client 进行一个专门的一个加载，也就是会把特定的 client 去注入到我们的reject，也就是我们的 bin 容器上下文里面，那么如果说假如说我们的 client 是为 null 或者是 client lines 为0，也就是说它并没有指定client，那么它要做的事情就基于 resource loader 去进行一个注解的一个类型的一个筛选。


这里面我们首先构造出一个scanner，也就是一个扫描器，这个扫描器基于我们的资源 resource loader 去扫描，并且它进行一个注解的一个过滤，那么这个 notisen type filter 是指定分client，也就是说我只扫描通过了份 client 进行修饰的这些类，那么就是说它会把这样的相关的一些 b 就是扫描出来。


那么对于这里面的话，对于我们扫描的内容其实也就是我们的 e code service，因为它的这个在定义闭应的过程中使用了份刊的这样一个注解，那么这样的话它会把我们定义的这些我们可以理解为是一个接口规范，或者泛 client 一个定义的接口规范，那么扫描到以后它会进行一些解析，最终是通过指定这个胞结构里面去解析有反刊的注解的这些病。


这里面我们看另一个条件，如果说我们的 Claude 已经指定了我们的 kind 类，那么它就会通过我们的 notation gender being dimension，就是把这个类去装载进来，把它构建起来。那么后面我们看它会对于所有的这些候选的这些注解对象进行一个处理，我们在处理的过程中我们看它会进行一些首先这个对应的候选的 campaign being definition，它属于 notation being definition，那么对于这个比例面解析的过程中，我们可以看到最终它会通过我们去获取泛刊的这个注解的信息，把泛刊的它注解的信息获取到，找到对应的name，并且这个 name client name 进行一些注册。


那么在注册的过程中，我们可以看到它注册主要是关键的几个点，这里面一个是名称，另一位他会找 configuration 这个对象，那么通常情况下，如果说我们指定了特定的 can configuration，那么对于这个 fine client 它会用特定的configuration，如果说没有指定的话，或者说它或者是 null 它就会使用默认的。那么在这里面我们注册完我们的 client configuration，同时它会迭代注册 resist fine client，也就是说我们 fine client 一些信息。那么在这里面我们去看一下对于这个 configuration 它的类的内容，其实也就是说我们可以在这里面去定义我们自己的一些配置信息，可以这里面配置的线配置项还是比较多的。


对于这里面的 value 和name，其实我们可以理解为它是等价的，我们不管是配 value 还是 pay name，最终在这里面获取到的信息都是对应的 kind name，我们看一下 client name 的实现，在 client name 实现这里面看，首先它会去看看的，首先不会now，它会从这个里面去找对应的value。如果 value 它首先是 context 的，假如 context 有值的话，它会去看一下 value 的值，如果说 value 获取到的话，它会把用 value 把 contact 的内容替换掉，因为最终它相当于是我们处理的过程中会有一个优先级。


我们看这里面处理的过程，首先它会去取 context ID，如果 context ID 它如果说为null，那么再去看value，那么如果说整个它就再去看name，只有看 service ID。如果说最终我们去判断 value 的值不为空的情况下， high Tech 也就是有存在一个对应的文案，那么我们就把这个对应的名称就返回过去，我们获取到了 client name。假如说如果说都没有的话，这里面会抛出个 u state exception，也就是说当前这个配置状态是有问题的这样一个过程，这是我们获取 kind name 的过程，那么最终得到这个 name 以后，它才会进行我们这些信息的注册。注册的过程跟刚才的处理逻辑是比较类似，我们看这里面这个注册的过程，我们刚才已经看到，那么我们返回，那接下来我们看注册 resist fine client，也就是对应下面的方法。


在这个执行的过程中有几个关键点，这里面我们看到最关键的点就是我们最终在执行的过程中，我们获取到这个粪刊的 fact bin，其实在注册这个 bin 的过程中，也就是我们最终其实得到我们生成粪刊的一个代理的过程，我们在这里面去看一下这个粪刊的 fact bin，它一些情况，我们可以看到它是实现了泛 factory bin 这样一个接口，那么最终我们可以通过对 get objects 的方式得到对应的一个类。这里我们看它是涉及到我们在 set being factory 里面有 be in fact 这样对象，这里面主要是我们关心的是个type，那么比如说对于这个 fact being 它的 type 是什么？那么如何在 get object 的时候能得到对应的一个什么类型？那么这个 Tab 的类型其实就是我们可以理解为我们在定义这个接口的时候，接口的全路径，那么基于这个接口的全路径，我们去构建出这个 fine client fact b，那么在这个对象定义完成以后，这里面最终化处理的事情是什么？我们可以看到其实这个定义它构建方法，其实我们应该通过它的 get object 方法去跟进来，这里面我们是 get apply 的方法，这个方法其实就相当于是获取到我们 factory bin，构建 bin 的过程，它通过 get target 这样一个目标对象，通过目标对象我们这里面去执行。


我们看首先它会通过 be impact 里面去获得对应的这个 FIN context，那么我们在初始化的过程中并没有涉及到 FIN context，那么 FIN context 它是怎么来的？其实 phone context 它是通过我们的 auto contribution，我们自动装配也完成的，自动装配的内容我们在这里面一次有跟大家去介绍，那么我们来可以看一下它自动装配的内容，我们找到对应的信息，这里面 Meta info 对应自动装配的内容，我们可以看到这里面有 FIN auto configuration，那么我们重点关注这个，在这里面我们看到它是有一个构造出一个bin，这个 bin 就是 FIN context。


那么 FIN context 它做的事情就是把我们这些自定义的这些configurations，这里面对应的 FIN client specification，这样注册到 fine context，我们从这里面去获取我们比较关心的内容，也就是对应的 find out configuration，那么还回到我们的这个状态的过程，其实我们看这里面获取到这个 FIN connect 对象以后，我们看通过 FIN 这个方法构建出一个 FIN builder，那么看它里面注的是什么事情？其实在这里面其实也是通过我们的 context 对象里面去找到一些相关的一些信息，就是说我们在构建分 builder 的一些所常用的一些内容。这里面比如说我们看有它的日志记录器，我们的 encoder 和decoder，以及相关的一些对象，也就是我们这些信息它都是从当前一些指定的费用 context 里面获取的。


那么我可以看一下这个里面获取的过程，它首先还是通过这个 context 对象去找里面具体的一个 instance 实现，可以根据你看一下看这个分 context 它是怎么处理的，它在 get instance 的过程中首先指定 context ID，其实我们就相当于是在 name 里面，它通过 get context，也就是说我们在这个里面找到一个对应的我们的一个 spring Bing 的一个上下文，一个 bin 容器的上下文。


那么从这里面其实我们看在这里面处理的过程跟我们在 load balance 处理这些特殊配置也是一样的，其实因为它们是继承了相同的 name 的 contact factory，也就是说从这样一个对应的子容器的 map 里面获取到对应的信息。


好，那么我们回来接着向往回走，我们看，这样我们就在这里面构建范的内容，我们就可以简单去了解到这里，其实我们在构建的过程中也可以去做一些自定义相关的一些操作，我们可以看到这题 apply build customers，也就是说我们有一些自定义相关的一些信息的话，我们可以通过自定义对应 build 的内容，我们可以看到这里面去获得份 build customer。


那么我们在注册这个 bin 的过程中，它会在执行的过程通过我们上下文信息里面获取到对应的内容，进行它一个处理。对于说也就是说在实现它的过程，我们看到进行 customer 相关的一些实现，就能得到通过猪的方式进行这个 builder 的一些特殊化的处理。

