---
title: 2-8 Spring Data ES核心源码解析（1901）
---

# 2-8 Spring Data ES核心源码解析（1901）

[image](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/1a6df51e-836b-4681-9ff3-b92019c55b42/SCR-20240814-ijii.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665YLCGGG6%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T232137Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDvMPuadOvFASMHWtZZlshRiNMZ75CgOVI%2BXtnUZ7MoJgIhAIvPjXKBZoDQQMzKDEhx4PUILW1ct0m0%2F88P9BVcXVQZKogECMb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1Igw%2FZQc06fdwA4ns4EYq3AN7i0tZX%2BBnncrTwa6M4TQ2LFjDR989nqSKFyup1McnUSz8HVlI08n%2BKl2RmMbMgtuHqtL6u1SeIZbFYthXu%2B6HznmXL4BcMPMLmiVZjHXx5w467j%2B9OWqyO7ba1LvbCTtz6Qomt9UwPGW4qTTHH8FBnm%2Fn7vHGkpvSZHMtVSOm6NqukUjYnjaANhI%2BEg4Ukxm%2FBBqpeUDJk%2B4ay%2FNN9PNSL16qbn8stNjMvVMNgjWnJCgytbRVinby3Yj%2BBild5D5on0RKFDIxIsxfChCejkjAKMkMoNlfRBTXL5j1tCNMGL3BEMM%2FJvJ4s52dd0sOzYMy5pRfjop4j8ICMJluC9JIT1USwfe4ajb325dIdF3sToelvYaSN%2FcA4eZxu0iZmLK8zhqYmK%2FA0T93wa05Iz7Vbo8L08fH%2B6s0dv%2Bymgtvxg%2F%2FhtW95bYXS4jG84Q48uAGQLbDm45N7OGDZ%2FCeiCgdVKNFMHYV2gM9O%2FLUbrme7eef6JojvjeH6rDxGpqbw45lCsI94ORuxezccM72%2FVqFYBe49iOdmMQeXOgT1u5MSDJUHjIFLFUD9uT%2F0%2Bnd2emRdp0Kt2mW%2F6qrQ7ti2%2FyloYba6sBQlKFEq93tZVJdV%2BJDZqK%2BAJoFgNjRADDxuv%2FSBjqkAbp1ihQzPgyXNClHaw%2F%2BT09DzvLlYLItowEp0nTyNkN0DfJPivnzG5p6%2F4GFIMg2n2URi2iVZbUTfbp2Iq5RqyHvOPEkZCMTMilYa9amyxT0BD9CIk8BC9a0oB1ML55wuqKlHAe9hCC3JLlpCNQCZH%2FKe3mWkFBqS33oY%2BKHAjMswj8deJq5aK2c2VB5U4b%2BDfqIUuFVtOrKHQPItizoh17vHNWw&X-Amz-Signature=f0348a77d41b588bb72e00202f3ed45f7455d3fd7414c029eebcefb259446432&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

[image](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/6076e26b-bcd6-4510-a2fa-751ea8002963/SCR-20240814-ihwg.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665YLCGGG6%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T232138Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDvMPuadOvFASMHWtZZlshRiNMZ75CgOVI%2BXtnUZ7MoJgIhAIvPjXKBZoDQQMzKDEhx4PUILW1ct0m0%2F88P9BVcXVQZKogECMb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1Igw%2FZQc06fdwA4ns4EYq3AN7i0tZX%2BBnncrTwa6M4TQ2LFjDR989nqSKFyup1McnUSz8HVlI08n%2BKl2RmMbMgtuHqtL6u1SeIZbFYthXu%2B6HznmXL4BcMPMLmiVZjHXx5w467j%2B9OWqyO7ba1LvbCTtz6Qomt9UwPGW4qTTHH8FBnm%2Fn7vHGkpvSZHMtVSOm6NqukUjYnjaANhI%2BEg4Ukxm%2FBBqpeUDJk%2B4ay%2FNN9PNSL16qbn8stNjMvVMNgjWnJCgytbRVinby3Yj%2BBild5D5on0RKFDIxIsxfChCejkjAKMkMoNlfRBTXL5j1tCNMGL3BEMM%2FJvJ4s52dd0sOzYMy5pRfjop4j8ICMJluC9JIT1USwfe4ajb325dIdF3sToelvYaSN%2FcA4eZxu0iZmLK8zhqYmK%2FA0T93wa05Iz7Vbo8L08fH%2B6s0dv%2Bymgtvxg%2F%2FhtW95bYXS4jG84Q48uAGQLbDm45N7OGDZ%2FCeiCgdVKNFMHYV2gM9O%2FLUbrme7eef6JojvjeH6rDxGpqbw45lCsI94ORuxezccM72%2FVqFYBe49iOdmMQeXOgT1u5MSDJUHjIFLFUD9uT%2F0%2Bnd2emRdp0Kt2mW%2F6qrQ7ti2%2FyloYba6sBQlKFEq93tZVJdV%2BJDZqK%2BAJoFgNjRADDxuv%2FSBjqkAbp1ihQzPgyXNClHaw%2F%2BT09DzvLlYLItowEp0nTyNkN0DfJPivnzG5p6%2F4GFIMg2n2URi2iVZbUTfbp2Iq5RqyHvOPEkZCMTMilYa9amyxT0BD9CIk8BC9a0oB1ML55wuqKlHAe9hCC3JLlpCNQCZH%2FKe3mWkFBqS33oY%2BKHAjMswj8deJq5aK2c2VB5U4b%2BDfqIUuFVtOrKHQPItizoh17vHNWw&X-Amz-Signature=7d10cc98fc627bc5b74bf5576dca24bd5c715d4a4cbb2f27e8538b5a8d865947&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

同学们大家好，这章节我们来介绍一下 spring day 的 elect search 的核心源码解析。关于 elect search，我们还是分三部分来介绍，第一部分是 spring day 的 elect search 的源码情况的一个概要结束。第二部分是我们介绍一下 spring day 的依赖search，它的一些核心的API。第三部分我们通过 spring day 的依赖 search 进行执行，跟踪一下它执行的流程。


首先我们来看一下它 spring data 依赖 search 的源码介绍， spring data 依赖 search 它的源码也是在 spring project 下面的这个目录里面，对应的 get help 模块只有一个是 string day 的依赖色子，我们现在可以切到它的 git Hub 页面去看一下，在这里我们看到对应的 spring day extra 它的源码的情况，这里面我们看它的 star 数 2. 5 k，其实这个量还是挺不错的，当然 fork 数也比较多。


所以说大家如果说在使用依赖测试的时候，通过 spring day 的依赖测试去访问，而 ES 还是比较常见的。其实对于 spring day 依赖 search 这个模块，大家更新的也比较频繁，我们可以看到它最近几天都有更新。接着看一下 spring day 依赖测试它具有哪些功能。首先我们看一下这里面的介绍，它是比如说 string day 的项目的主要目标是更轻松地构建我们使用新的这些数据库访问技术，来去访问我们的应用程序，这些技术包括我们的关系引用数据库，非关联数据库以及 map reduce。我们知道这是 spring day 的，它提供的一些包装的功能，那我们针对这里面的 spring day 的一个测试，它提供了什么事？其实 spring day 的依赖 search 它项目提供了我们与依赖 search 这个搜索引擎的一个集成。


spring day 的依赖 search 它的关键领域它是还是以PORTAL，也就是我们 POGO 这样一个中心模型，用一段设置文档来进行一个轻松的一个交互。同时我们在这里面提高推repository，那边构建一个 repository 来访问我们的数据库，这里面是有对应我们 index source 的一个情况，我们通过 report 的 CRUD 来轻松的去读写我们 e 代 source 的相关的操作。如果说我们使用原生的 e 代 source 对应的 rest API，其实操作起来还是比较复杂的，需要学习很多 ES rest API 的一些结构。


接下来看一下 spring day 的ES，它提供了哪些功能。第一项，这里面介绍的是基于 spring 的配置 ES client 的这个实例，配置 ES 开发实例，我们可以通过 spring 的方式去配置 spring 方式，这里面有支持基于 Java 的 configuration 这样注解的方式配置，或者是基于 XL 的 name space 用命名空间的方式去配置。


那么第二个我们可以看到，其实 string elecors 包装出一个 electronic reside template，看到 template 的话，我们就知道 template 去提供哪些相关的操作。我们可以向 GDBC template 进行一个类比， template 它作为一个工具类，它可以提高我们对常见 ES 超出的这些生产效率。同时它包含对于我们这些模型的一些映射，比如说我们的依赖测试，对应的索引以及我们 Java 里面的破骤进行一个影射。


第三部分就是说它提供了一些丰富的一个 object Mapping 的一些集成，我们通过 spring 的 convince service 来去完成这样的一功能。另外就是说它可以基于注解来完成这些元数据的一些映射。我们可以在 PORTAL 上加上一个 add document 的注解来完成我们这个 PORTAL 对象跟对应的 ES 值，它一个缩引的对象的一个映射。当然最重要的还是一点就是它可以自动的去实现一个 repository 的接口，通过 reposer 接口来生成一个代理，方便我们使用。


这里我们简单去介绍一下 spring day 的依赖测试它具有的一些功能。我们接下来看一下 spring day 的依赖测试它具有哪些核心的API。在这里面我们可以看到，对于核心API，它其实我们可以还是类比g， p a 或 rest 的方式去学习 spring day 的依赖测试。首先最重要的一个注解，这里面是向 enable 依赖测试repository，我们通过这个注解去开启我们依赖测试的 reposure 这种 parcel 去访问。另外对于我们，对于Java，我们的 Polo 对象或者是我们的模型对象，我们通过 at document 的这个注解标明一下它跟乙加 4 的树形的映射关系。同时我们可以通过注解 field 来进行这些每一个属性字段之间的映射的一个情况。


对于 spring day 的依赖测试，它的 reporsory 是 ES reporsory，我们看到这个命名也很容易去想一想，比如我们对应的是 GPA reporsory，这里面 answer reporsory，对于一个这个词 reporsory 我们也知道它对应的一个实现，它默认的代理实现，也就是 simple 一代测试的report。同时在进行 simple 一代测试的 report 进行一个 ES 相关的抄录的过程，它会用到，比如这里面是 index 的 operation 和 index 的operation，这个都是我们通过 spring 对 ESS 进行了一层包装，其实我们最终还是需要构建我们对应的 ESS reporsory，它的这个子接口的一个实现的代理类。构建的方式还是通过我们这里面的 fact bin，也就是一台色词 reports 的 factor bin 来构建这样对应的比例。同时我们以 spring day 的一台色子在 spring boot 的 auto configuration 也实现了自动装配的功能。这里面跟我们依赖色子相关的比较重要的两个 auto configuration，也就是依赖色子 date auto configuration 以及我们依赖色词 reporsory auto configuration。


在这里面我们可以先切到我们 string day 的 ES 它的源码里面去简单了解一下 string day，依然是源码的结构，我们现在切换到 string day 的 ES search 这种，打开源码可以看到这里面的内容还是比较多的，还是老传统。先看我们的 palm 文件，在 pool 文件里面我们可以看到对应的 spring day 依赖色子，它的 part 也是对应的 spring day 的part，说明我们归 spring date 整个 build 进行一个管理。下面我看一下它的依赖，这里面的依赖信息我们重要看一下dependence，这里面的 dependency 的内容我们看，首先它依赖了 spring context，我们 spring text 相关的这个四五相关的一个中文，这里面还涉及到 spring day 的comments。


接下来我们来看一下这里面还用到了 spring Web flags，这里面对于 spring day 的 Eli search 最重要的一点就是我们下面使用到的 spring day search， client transmits transport 以及我们的 spend e x pack in，对应的应该是下面，这里面是 exsearch rest high level 的calendar，也就是说这是我们现在使用比较多的一个calendar。下面内容我们就不用太多的关心了，那我们来简单看一下我们所有的一类。


4 指里面包里面的核心的一些类。首先我们看这里面是注解相关的一些内容，这里面注解相关内容。最重要的我们这里面涉及到自document，我们可以通过 document 建立我们 Java 对象和 ES 这个树引的一个映射关系，可以类比对应的依赖我们的 DPA 里面的 add entity 这样一个属性。这里面也有对应的一个field，也就是我们在创建一带四指这个 mapping 关系的过程中，我们通过它可以去指定我们这些类型的一些映射。下面这里面是一个 GEO point，也就是我们可以通过依赖色子存储一个位子空间这样一些信息。


接下来看一下这里面对于repository，这里面还有一个注解是我们的 enable extrs，我们看到这个注解是应该会比较熟悉，因为它基于 enable 开头，我们知道它都是通过激活某一种功能去用的。这里面还有 enable active 依赖测试， reporter 最新版本的依赖测试，它已经实现了基于 active 的方式进行显映式的去获取数据。
我们看下面这些内容，我们看到这里面是依赖测试 ENT information，就是我们去获取依赖测试 reporsory 对应实体的相关的一些信息。这里面还会涉及到我们这里面的是依赖测试reporsory。看到这个reports，我们跟对应 JP 的 reports 来进行一个类比，我们可以看到对于依赖色词report，它里面提供了一个方法，也就是色词similar，也就是说我们查找类似的，这里面是支持一个 finish 查找。这里面我们就简单介绍到这里。


接下来我们来看一下 string day 的index，它整个执行流程里面，我们先介绍一下初始化流程，对对于 string d 的依赖色词，我们使用 string Boost 方式开发的过程中，它初始化还是基于依赖塞它的 auto complication 去完成的。这里面对于 string did，依赖 search 的 auto complication 涉及到两个，一个是 us 的 date out complication，另一个是 us reporsory 的outcomplication。


对于第一个自动装会，它里面主要跟我们引入了哪些信息？我们可以看到，首先是一个 base configuration， base conversion 里面会涉及到一些convert，也就是说我们依赖测试的一些数据跟 Java 对象之间一些转换的一些工具类。


下面我们可以看到这是 rest client configuration，这个是我们直接用于跟我们的 e s 的进行交互的一个驱动client，这里面 rest client 我们基于 s c b 请求跟我们的 e s 服务建立一些关系，我们进行我们数据的一些读写。


下面这里面是 reactive rest client configuration，跟我们的 rest client configuration 是一个对应关系，通过它来构建出一个基于响应的一个 rust client。下面这里面是 electric repository 的制动装配，这里面就是跟我们 spring date electric 的内容更强相关一些，我们还会是通过类似于加载 enable electric REPORTS 的方式，把我们整个依赖色子所有实现依赖色子 report 这个接口的这些子接口进行一个代理类的构造，这个构造的过程还会用到了一个 search report configuring extends 一个扩展的类型，这些配置扩展的一些内容，主要还是去对我们的 ES reporter 的 text bin 通过这个类去构造我们的一个代理类。


构造代理类的过程中，我们知道它最终构造的代理类是基于 simple 依赖测试 repository 作为我们的一个目标对象，生成我们的代理对象，代理对象生成的过程还是跟 index repose factory 去进行一个相关联。接下来看一下整个这个初触化执行的过程。


切换到我们 showcase 下面的依赖色子模块，我们还是先看一下 pool 文件， pool 文件里面我们这里面是通过 spring boot start date 依赖色子这样一个 starter 来引入我们依赖色子相关的内容，下面的内容引入我们可以不用过多关心，还需要去特意看一下我们对于这个用户模型，这个 user 模型，这里面我们是怎么去对它进行一个注解的修辞，我们这里面重点关注的是我们这边 i document 的注解。 i document 注解说明，我们通过这个注解把我们的 user 对象跟我们依赖测试的索引库构建出这样一个映射关系。同时这里面我们定义了一个ID，作为我们整个 user 曲线它的一个唯一缩影。


接下来我们来看一下这里面特意对于这个birthday，这里面一个出生日期进行一个特别的映射，这个映射的关系我们通过 add field 这个注解映射一下，通过这个 add field 的这个注解去映们 Java 的数据类型跟依赖色的树影这个数据类型的一个对应关系？简单了解完我们这个数据模型，对于其他的内容我们并没有过多的区别，跟我们在使用 stamp data GPT 的时候很类似。


接下来看一下 spring boot 里面，它对应一段 search 的一个自动装配的类，这里面我们可以看到这是我们依赖色词的一个制动装配类，我们可以看到这里面它首先会去判断一下我们当前的上下文需要依赖的yes， its rest template，也就是我们引用了这样对应的栅包才能进行后续的操作。


这里面我们可以看到这是 elancer 的 did auto configuration，它要做的事情是首先去引入这些configure，这里面也都是在一带色词的 data configuration 下面，涉及到 base configuration， rest client configuration 以及 active rest client configuration，我们可以切进去看一下对于我们 base 的configuration，这里面主要是注了哪些信任。这里面是一边设置 customer conversion，也就是我们可以自定义一些转换器，下面我们可以看到是 simple elects 的 mapping context，构建我们一个映射的上下文对象。


接下我们看一下这是一代词的convert，就是我们作为一个转换器，下面我们看 rest client configuration，通过 rest client configuration 它来去构建我们这个疑难 search 的 rest template，也就是来构建我们对于 yes search 这个索引库的一些操作等等这些信息。


在这里面我们看到它还有一个关系，如果说我们这里面用的是 ES did auto configuration，如果说也会引入了疑难 search 的rest，看你的 auto computation 的话，我们这个应该要在这个 auto computer 之后，我们看一下对应它做的什么事。


其实这里面是主要跟我们创建出来了一代词，原生的 rest client，看看这是 rest kind of builder，我们的 rest high level 的 kind configuration，通过这些去构建出我们对于依赖测试原生的这些API，其实我们这里面是暂时还不会使用原生的API，我们只是通过依赖测试构造的 Repass 来进行我们依赖测试的一些操作。


我们看一下这里面我们关注的另一个是对应的依赖测试reporsory，这里面是有我们的 ES repose to auto configuration，我们切到这里面，我们可以看一下这里面的 reports auto configuration，它实现相对比较简洁一些。这里面更唯一关注的就是我们这里面在 import 栏我们的依赖设置 report register 一个注册器，这里面它也会校验一下我们当前的上下文。首先是需要引入了我们的一代 search report，引入相关的依赖，同时保证我们的程序依赖设置 positive bin，这个 bin 并没有去初始化，所以说我们通过这种方式进行装载，这里面我们可以看到它其实跟我们的其他的一些 reports register 是类似的。这里面是首先标明我们关注的 enable investors reporter，注解是这样，同时我们的这个 configuration 对象是依赖 enable 的 elicer 的configuration，同时我们还有一个 configure 的扩展，就是 either search reports 的 config extends，就是这是我们的启动的过程会加载的这一些内容。


其实这些加载的过程我们简单了解一下，其实更重要的就是我们执行的过程对于 spring day 的依赖测试，它执行的过程跟 spring day 的 JPA 或 spring day 的 rest 其实很类似的，通过 repository 去操作 spring day 的依赖测试。首先我们会通过找到原生代理，通过代理进行我们的执行，执行的过程中会涉及到一个拦截器链，这里面的拦截链会涉及到这四个拦截器链，最终它执行的过程会通过我们的 report query， master invoker 去间接地去引用我们依赖色词的 Pod query，就是说我们通过 query 去执行我们依赖相关的操作。这里面会用到 elecors 的operation，对于 electronic operation 它会间接的去调用我们的rest， high left planned 进行我们延时相关的一些操作。其实我们可以看到这里面在执行的过程跟其他的这些 report 插入是很类似的，这里面我们直接通过代码简单的通过 debug 的方式去了解一下整个过程。


现在切到我们的 showcase 下面的一连色子模块儿，我们这里面进行一个 debug 的执行，我们现在进行操作debug，我们可以看到这里面是我们创建 REPORTS 的一个过程，我们现在跳过这个断点，这里面我们创建 REPORTS 相关的一些 Foxer Packer factory，创建我们的代理，这里面我们可以获取到我们的代理的信息，这里面获取我们的代理的拦截器链，这里面会有一些比较特殊，这里面我们只获取到了一个代理人类。那么其实它这里面跟 DPA 它有一些区别。我们在使用 DPA repose 的过程中，直接把 7 个我们的拦截提炼都可以展示出来，这里面只有一个，其实通过它那个间接地去执行其他的难题链，最终会涉及到 4 个难题提炼的执行过程，我们可以简单跟一下，看一下这个效。


我们可以在这里面其实首先跟进去执行，我们看再进去执行，这里面我们看又获取了一个 target 对象，这个 target 对象我们去看一下，其实就是我们的 symbol elecset reporsory，基于这个 target 我们就去获取我们的 AOP 的拦截器链，我们可以看到这里面的 AOP 拦截器链涉及到三个拦截器，分别是 expose invocation interceptor 以及我们的 query cuter 的 mess interceptor。也就是这跟我们 GPA 里面 7 个的几个拦截器基本上能对应上，我们知道也是之前这几个拦截器，这里面我们重点关注的还是我们的 query executor master interceptor，可以跳过这些过程，现在我们看它已经执行到我们的 query cuter mass intercept，这里面我们看了一下它是如何执行的，这里面也是我们的 result handler，其实整个这个过程我们在 GPA 和 Sprint GP， Sprint dress 里面都经历了。


可以看到这些代码是对应的，我们的是 Sprint 的 common call 里面的内容，这里面去进入我们的 do invoker，我们继续执行 do invoker 的一个操作，可以在 doing Moker 里面，我们可以看到它获取到我们的 mess 的，也就是我们的执行的方法判断方法，这是不是一个查询方法？通过查询方法我们去获取我们 emocation 的 Meta data，会移到 Meta date，把它放到我们的 case 缓存里面，接下来我们可以看到它会通过 EMO case， Meta date， emocha 的方式进行执行。


跟进去这里面我们到 invoke 方法里面，这里面我们可以看到它是执行到我们的 repost 的 mass 的 invoke 方法里面，这里面我们还是执行 do invoke，在这里面我们看到 invocable 是一个什么样的对象，这里面我们继续跟进去，可以看到它会创建一个 query 对象，最终会通过我们的 USS 的 convert 进行 update query，这里面去看一下我们真正执行的一个过程，那这里我们可以看到最终我们会使用一个测试的 operation 来进行一些操作。


当前这个类是我们对应的 ES port query 跟我们在这里面介绍的，真正我们在 report master invoke 的过程中是通过我们的 elearces port query 已在设置 port query 下面，通过 ES operation 进行一些真正的一些逻辑操作，看到这里面它就会间接地去使用我们的 rest high level 的这个 client 进行一个操作。执行到这里，我们就先跳过我们的断点，我们现在关于这个 spring day 的依赖测试，它执行的流程我们就先介绍到这里，同学们，我们下一章节再见。

