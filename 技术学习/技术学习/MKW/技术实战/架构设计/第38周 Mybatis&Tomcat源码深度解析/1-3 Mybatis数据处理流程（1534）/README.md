---
title: 1-3 Mybatis数据处理流程（1534）
---

# 1-3 Mybatis数据处理流程（1534）

同学们大家好，这章节我们来开始学习 mybadcase 的数据处理流程。在上一节架构分成设计，我们介绍了 mybadcase 的核心框架，通过包结构划分出不同的一些功能模块。我们这一节就来了解一下买 Badcase 的数据处理流程如何在这些功能模块的支持下完成的。


首先我们来看一下 Mybyte 数据处理流程，一个概括的一个情况，这里面我们可以看到，首先我们需要对于初始化配置，也就是我们配置的信息进行初始化，这里面会构建出我们的 configuration 对象，那么通过 configuring 对象来去构建我们的 SQL session factory，那么 SQL session factory 它获取的过程中其实依赖我们的配置信息，这些配置信息包括我们的 Mapper 信息我以及我们的数据源操作的信息。


其实通过 SQL session factory 我们获取到我们的这个 SQL session，那么 SQL session 就可以直接用来进行我们这个 statement ID 指定的一些 SQL 查询。那么另一种方式，我们通过Mapper，也就是说我们通过接口 Mapper 的映射。对于 Mapper 我们可以通过 SQL session get Mapper 这样一个特指的一个接口，那么生成这个接口对应的一个代理类，我们基于代理类进行我们所有的一些间接的一些操作。


其实通过我们 get Mapper 获得的对象是一个 Mapper process 的一个代理，我们基于这个代理，它其实依赖了executor，这个 executor 其实我们通常也是 simple equutor 进行执行我们收口语义的操作，在执行的过程中它会涉及到我们对应的 statement handler，也就是acuator，它在执行的过程中也是需要对应的一些处理，比如我们的 state handler 进行一些真正的比如 state handler 进行一些处理操作。


在这个过程通常我们就已经跟数据库进行交互完成了，这里面后面还会有一步是什么呢？我们从数据库获取到了我们的 reset 这样一个结果集，它会转换成我们对应的 Java 的VO。这个转化的过程其实还涉及到一个 result size 的Candler，进行我们数据的一个转化的一个过程，那么这是我们可以理解为初步的一个这样一个过程。


首先我们对于我们配置文件的初始化获取到我们的 SQL session factory，通过 SQL session factory 获取到 SQL session，我们来通过 SQL session 去得到我们的一个 Mapper 代理类，那么得到这些信息，这些我们可以理解为一个初始化的过程，那么在初始化完成以后，接下来就应该是我们数据执行处理的流程，这里面就会涉及到我们的 map broadcast 和我们的executor，通过 initiative 在执行的过程中通过我们的 Steven 的 handler 获取到数据。那么在获取到数据完成以后，进行我们返回的 research set，进行一个结果的一个映射转化。


好，那么接下来我们来看一下通过脑图来如何描述这个处理的流程，这里面我们可以看到对于我们首先是初始化配置文件，那么在初始化配置文件的时候，我们会构建一个 configuration 对象，那么对于这个 configure 对象处依赖的配置文件通常是我们的 my betas configure 对应的 XL 以及我们的 Mapper xmail 文件。那这里面我们可以通过我们的 my Betty study 里面的 my patint 模块来了解一下。我们可以看到这里面是我们的 my badcase configure 这样一个 XML 配文件，这里面我们指定了一个 Tab license 的packets，这里面我们看映射了一下我们对应的名称，我们是在 my byte domain 下面，这里面我们对应的 user 和我们的 user 进行一些映射，后面我们的 Mapper 是说明了在我们的 map configure 文件里面标明我们的 Mapper 的对应路径是什么，我们可以看到这里面是一个相对路径，其实是相对我们 mybettice configure 的目录去查找我们 user Mapper。 user Mapper 也就是说我们下面这个目录，这里面我们找到我们的 user Mapper。


通常我们相关的一些 SQL 语义操作，我们都会在这个 Mapper 里面进行一个定义，一个statement，通过 statement 去获取我们的操作，那么这里面的 statement ID 我们就可以理解是 select user by ID。同时我们要区分对于不同的一些查询的一些命名空间的区分，这里面我们看注意一个 name space，也就是假如说我们直接去 select user by ID 的话，它可能在不同的 XML 进行一些冲突，那么我们这里面 name space 来进行它一个空间的区分。


其实我们可以理解为整个这个 Steam ID，它是对应我们包机构全称我们这里面的 user mapper 点 select user by ID 这样一个全称。这里面我们指明了我们的返回类型是user，我们这个 user 因为我们在这里面已经定义了它的一个类型的一个别名，所以说我们可以直接取 user 就能对应到我们这个对应整个包结构下面 domain 的 user 这个类，所以说我们可以在里面简写这个 user 的一个类型，这个前提还是我们在包结构下面不会存在一些命名的冲突。


好，这是我们的一些初始化的配置文件。那么接下来我们需要创建我们的 SQL session factory，也就是我们如何得到我们 SQL session factory，我们可以看到这里面会涉及到一个 SQL session factory builder，我们可以从这里面去看一下这个 so Processing packet builder， circle session factor builder，我们从这里面能看到我们打开这个 super session factor builder 的第一眼，我们就看到了这个 builder 操作，我们可以看到 builder 操作它是需要一个 configuring 参数，那么构建出一个 debug circus factory 这样一个方式构建完成。


那我们看一下其他的一些方法，我们可以从这里面看一下方法列表，我们可以看到方法列表都是 builder 操作，我们可以看到多次builder，这里面其实最关键，整个 builder 最终都会调用我们这样一个操作，我们可以看到它的一些依赖。


首先我们从这里面去看，我们对于这个builder，它里面是它会传入一个reader，我们可以怎么理解？其实我们通过 social session fake 的builder，它可以直接把我们的这个 Xmail 配置文件当做一个 reader 传入进去。最终我们会通过对于 XML 进行一个解析，我们通过 XL config builder 构建生成我们对应的一个 XL 信息。这里面我们通过 x mail configure builder pass 解析，它执行的结果就是一个 configure 对象，我们得到这个 configure 对象就可以去构造我们的 SQL session factory，就是通过这里面构造出我们一个 defiled circle session factory，在这个 defiled circle session factory 我们可以看到它里面的属性，也就是我们的 configure 的属性，所以说在使用的过程中去获取到我们对应的一些 configure 相关的一些信息。


好，那么我们得到了我们的 SQL session taxi 以后要做的事情是什么呢？我们通常去获取到我们的 SQL session，也就是 SQL session 去需要获得，那么 SQL session 如果获得，我们还是切换到我们的代码里面，在这里面 SQL session 我们是通过 open session 的方式得到我们 SQL session 的对象，那么这里面我们可以简单看一下，我们这里面是open，我们的 session from data source，也就是说我们获取到这个 session 会话也就是一个 g d b c 相关的一个链接。


其实对于 SQL session 它的概念映射可以跟我们 g d b seed collection 这个映射构建出来，我们可以看到在这里面去构建的过程中，它会去指定我们现在的 Defield extra type。其他的我们看这里面是 auto commit force，写这个 level 是一个now，那我们这里面进来去看一下它执行的操作。


这里面首先是对用 extra type 这个type，我们这里面是一个 simple type，这里面我们可以看一下它里面的知识枚举，在里面默认是这个simple，其实它在获取测试 session 的过程中，它会从我们 connect 里面获取到我们的三下文信息，我们通过三角人信息，这里面会涉及到我们获取到我们 transaction factory，也就是我们的事物的创建工厂。我们通过事务创建工厂得到对应的事物，我们可以看到是 transfactor 人通过 new transfer 得到我们当前的执行的事务。那么在从我们的 configuration 里面去构造我们的accurator，那么 accurate 它依赖到我们的这个四五对象以及我们执行的一个type，最终生成也是一个 simple acute 的type。这里面我们可以看到这是我们会默认使用 simple acute 这样一个去执行器进行我们的一些操作，接下来我们可以看到它通过我们的这些信息，这里面会涉及到 IQ ator，我们的 config 伦对象以及我们的 auto commit，通过这几个属性构造出我们的 debug circus，那么 debug 的错误 session 就是我们进行操作的一个实现类。OK，那么这样的话我们就获取到了我们的 SQL session 对象。


得到 SQL session 对象以后，我们要做的事情是什么呢？其实我们刚才介绍的我们对于 statement ID 的执行，或者说 Mapper 执行，它都会直接会间接的用到我们的 SQL session 操作。现在我们已经通过 SQL session factory 的 open session 方法得到了我们的 SQL session，那么接下来我们需要进行我们的 statement ID 的执行，或者说是获取我们的 Mapper 对象，那么我们来看一下这里面 SQL session 的接口，对于搜索 session 它有哪些操作？我们可以看到这里面有 set up one，对于 set one 指定一个 statement ID，或者说是我们 set one 指定一下我们的参数 set list，其实这些就是我们常规的 g d b seed 一些查询的操作。


这里面我们看一下我们一个相对特殊的操作，这里面有一个叫 get Mapper，我们获取 get Mapper 是一个，我们可以看到它的输入是一个 class 类，那么它的对象也是对于这个指定 class 类的一个代理实现，那么对于我们这里面，我们这个实现里面是 user map，其实它会直接间接的通过 super session 的 get map 获取到我们的 user map 对应的一个实现类。这里面我们去了解一下它，其实通过这种方式就得到我们的一个 Mapper 的一个代理对象，那么这个 Mapper 代理对象其实它就是一个 Mapper process factory 构建出来的。这里面的实现过程我们就不去再细致了，我们可以简单去看一下 debug 的 SQL session 它里面怎么去实现的，这里面会通过 get Mapper 进行一些查找，这里面会涉及到一些缓存代理缓存的一些操作，如果我们的 Mapper register 有的话，我们就直接获取到了。


好，那么我们获取到我们的 Mapper 以后，就应该去执行我们的一些操作，这里面会涉及到 micromos 的，我们的通过 debug 的 SQL session 执行的过程，这里面我们可以切到 debug SQL session，看一下它一个执行的操，我们就可以简单去了解一下它处理的一个过程。我们找到 debug 的 SQL session，那么我们看到 debug SQL session 里面，我们去看一下 slack list，我们从这里面去 slack list 是最容易去理解的，我们通过一个查询的对象去执行时构语句返回它的一个结果列表。好，那么我们来跟一下我们看。首先 slack list，它是一个statement，它是不支持参数的，那么接下来它会到一个支持参数的一个方法，我们可以看到后面是一个对于一个 robug 的是debug，我们接着跟好，我们再跟下来。


那么到这里面我们可以看到其实它在执行的过程中会涉及到，我们首先通过我们的 configuration 对象获取到我们的 Mapper statement，那么 statement 这里面是我们的这个 statement 的ID，我们通过 ID 去获取 Meta statement 这样一个查询的过程。


接下来我们通过 ACQ ator 进行一个 query 的操作，我们可以看到这个 query 的操作它的参数是哪些？这里面是 map 的 statement 和我们的对于我们的parameter，我们的参数进行一个包装，以及 Robug 和我们的handler，我们可以看下这个 Handler 其实就是我们的 result handler，也就是对我们的结果集进行一些处理，其实这个过程最终会涉及我们的 accurator 进行操作，那么我们在看 icutor 里面的 query 操作的时候，我们去看一下，这里面是我们默认是 base Excel。


其次也就是通过我们的 map statement 获取到我们的 found SQL，那么通过这里面涉及到一个 case k，也就是我们通过这些参数信息构建一些我们那个缓存的k，通过缓存的 k 进行一个处理，这里面通过缓存 k 去查找。如果说当前这个缓存可以能命中缓存，那么就直接返回响应，那么如果没有命中缓存的话，再进行一些提升的一些操作，这里面我们可以看到query，它会做一些校验。首先如果当前这个 session 它已经 close 的话，所以说我们就 accurate 已经whatclosed，就是说我们去跑出一长一点点。


后面就是说我们进行一些数据的操作，这里面是首先从我们的 local heads 里面去查找当前对象是否存在，这里面去做一些调整。这里面我们可以看到如果说我们当前对象不存在，那么我们就需要 query from DATABASE，这里面有真正的会数据库的一些查询的操作。那么好，我们简单先看到这里面还回到PPT，其实通过这些过程的话，我们已经执行通过我们的 Mapper 的 process 进行我们 debug SQL session 执行的过程，它涉及到 accurate 和 map statement 相关的一些信息。好，我们看一下后面的一些处理流程，其实接下来处理的话，它会涉及到一个 statement handler，这个 Steam Handler 去执行相关的一些操作，那么我们这里面去接着去跟一下，看一下后面执行的一些操作。


我们切到 statement Handler 里面内，我们看一下 similar Handler 它的一些实现。首先我们看这是 similar handler 的一个接口，我们看一下 similar handler 有哪些实现，我们从这里面一看，首先我们可以看到是 base 的 statement handler，它是一个抽象的，下面有 creable paper statement 以及 routing statement，这里面还有 simple statement handler。其实我们在使用的过程中，默认我们会通过 routing setmhandler 进行一个路由，我们切过来看一下，在我们构造 routing setmhandler 的过程中，其实它会根据我们的 map status 里面的 statement type，我们可以看到这里面是simple，我们的 paper incredible 去构造我们真正的一个对应的 segment handler，也就是说它作为一个路由去做一层代理，那么我们最终它实现的过程也是我们这些内容。


其实我们可以通过 simple segment handler 的实现来去了解它的一些过程，我们可以看到这是 simple seed handler，这里面我们看它里面的一些方法，我们可以看到这里面是有update，这里面有query，对于 query update 我们可以去看一下，对于 query 这里面也是通过 bond circle 获取到我们的原生的circle，那么这里面我们就获取到 statement 来进行一个执行。


我们可以看一下这个 statement 就是我们的 Java SQL 的statement，也就是我们 j d b seed 概念，我们通过 j d b seed 概念去执行这个SQL。执行完成以后，我们对于通过 resort set handler 来进行这个 statement 的一些处理，我们知道执行完成以后它会得到一个什么信息，我们可以从这里面去看一下。对于 statement 执行完成以后，它会获取到一个 result set，通过我们的 result set 来进行一个映射，这样一个客人获取到我们的一些真正的一个数据信息，它会通过我们的 resort side Handler 转化成我们的一个 list 集合，那么从这里面我们可以看到，最终我们通过 Steam handler 来得到了一些我们的 resort 信息，它通过 handler query 得到我们数据的一些列表信息，又通过我们 resort handler handle recelled set 得到。我们通过 resort set 进行一个 VO 的转换，得到我们程序里面所需要的一个加 2 对象。其实我们最终的返回结果的处理就是通过 reshort handler 去获取的，这里面代码我们可以参考 de 飘的 resort handler 来实现。好。同学们，我们关于买 Badcase 数据处理的流程我们就先介绍到这里，同学们，我们下一章节再见。

