---
title: 2-4 Mybatis重要接口及类的作用分析（2643）
---

# 2-4 Mybatis重要接口及类的作用分析（2643）

同学们大家好，这章节我们来学习一下 my Badcase 的重要接口，以及这些类对它的作用进行一个分析。首先我们来看一下我们重点关注的这些接口和类都是哪一些，我们从这里面去看，也是做两个分类。首先我们来看一下初始化构建相关的这些重要的接口和类。这里面我们首先看到的是 SQL session factory builder，那么 builder 它这是根据它的命名，我们可以知道它是个类，它是一个构建器，这个构造器主要是为了构造出我们的 circle session factory，那么 circle session factory 和我们这里面的 circle session 是 mybadcase 里面最重要的两个接口。对于 social session factory 它有对应的debug， social session factory 的实现后面我们可以看到这里面是 external configure builder 以及configuration，那么这里面它也是一个对应的构造关系，我们通过 XML 的 configure builder 来构建出我们的 configuration 对象。


对于 configuration 对象，它是整个我们配子类的一个合集，也就是说我们整个跟 my badcase 相关的配置，它都会解析到 configuration 这个对象里面。这样的话我们通过 configuration 构建出我们的 solution factory，也就把我们的配置能作用生效。


最后我们可以通过这里面的 solo session factory，我们跟我们的 solo session，我们可以根据它这个接口命名来可以理解，对应的一个 factory 就是构建这个 SQL session 对象的，那这里面我们简单理解了这几个类之间的关系，那么我们来逐步的去看一下我们每一个接口或类在买 Badcase 实现过程中，它都起了什么作用？这个接口有什么方法？这个方法它在什么地方被用到，我们一块来去学习一下。


好，首先我们来看一下 SQL session 的 factor builder，我们切换到 SQL session builder 这个类，对于这个 SQL session factor builder 它的这些方法，我们可以看到这里面是一些 build 类型的方法，我们可以看到对于这些 build 类的方法，它传入的参数我们可以看到可以是一个 configuration 对象，可以是个 input stream，也可以是一个 input stream 加上一个property。这里面还要是 input stream 和string，也就是它基于这样几个 builder 方法去构造我们的 SQL session factory，那么这里面我们可以通过这些方法简单去理解，最终它都会走到我们同样一个方法里面，也就是我们的这个 build 方法。


那么在这个 build 方法里面，我们可以看到它的参数是首先是一个reader，那么这个 reader 其实可以读取我们对应的配置文件，这里面还有我们的三亚文环境信息以标记以及一些property，也就是一些属性信息。那么通过它来的构调出我们的 social session factory，这个 social session builder 它构建的过程其实是依赖了我们这里面的 xmail configure builder，我们 xmail configure builder 的内容我们待会再深入进去理解。好，那么现在我们可以看一下对于 SQL session factor builder，它是在什么地方用到了，我们可以按住我们的 control 键或 command 键去点开看一下。


这里面我们可以看到对于这个 SQL session factor builder，它被两个类用了，一个是我们的 SQL session factory bin，另一个是 SQL session manager，我们现在都是基于 spring 跟 mybadcase 进行整合的一个开发，所以说对于我们通过 spring 来构建这个对象的时候，我们可以看到这是一个 circle session factor bin，也就是我们通过这个 bin 来去构建我们的 circle session factory。那么我们可以看到它都是跟 circle session factory 相关的，一个是 circle sentence factory builder，一个是 circle sentence factory bin，我们先来看一下这个 sociefactor being 它出了什么事情，对于在这里面我们看到它引入了 supersession factory，我们可以快速定位它在什么地方用到了，我们可以看到在这里面它有涉及到了我们 SQL fact builder 的一个色字。那么在这里面我们看一下对应 SQL 30 fact being 在什么地方使用。


好，我们看一下这个属性在这个类里的使用，这里面有三个地方引用的。第一个我们可以看到这里面是对于我们这个 circle specific builder 这个属性进行一个色值，也就是说我们支持一个自定义的 SQL session builder 传入进来，这是一种方式，那我们看另一种方式里面是一个我们的参数的校验，参数校验的内容我们可以看是在哪儿，是在 after property set。我们知道基于 spring 的生命周期，我们在整个 bin 初始化，我们的属性设置完成以后，它会执行 of the property side。那么在这里面我们会校验一下当前的 social satisfaction builder 是否存在，如果说不存在的话，它会报错提醒，这是一种方式，我们可以看到另一个地方，调用的地方就是我们真正关心的。我们可以看到在这里面是 SQL session factory builder，它调用了 builder 操作，那么在这里面通过 build 操作来构建出我们的 SQL session factory。
我们来看一下这个操作是在什么位置执行的，我们可以看到它是对应这个方法的名称，这里面也就是我们的 builder circle specific factory，也就是说我们在通过 builder circle satisfactory 的过程中获取到 circle specific factor 对象，最终它是通过了我们这里面的搜索 session builder 的方式去构造。


我们可以看到这里面的代码量很长，其实前面都是为了构造我们的参数，也就是我们的 configuration 参数。对于我们这个 super session factor builder，它是支持一个 configuration 参数，那么在这里面前面都是我们构造对应的 configuring builder，也就是我们的 configuration 参数的一个过程。


所以说整个我们在这里面 SQL session factor being 里面很大的代码量是为了构造我们的这个配置对象，那么我们的配字阵因为 spring 支持一些灵活的配置，如果我们单纯使用 my badcase，它的配置通常是我们的 property 对应的 XML 配置和我们的 Mapper 配置。那么如果说我们基于 spring 的话，还有一些上下文环境信息可以通过各种方式进行。我们一个特殊的配置好，这样我们可以看到了对于我们的 solo specific builder 在我们这个对应的 solution factor 变的一些实现方式。那么好，我们来回到我们的所有参与方的builder，我们看一下它的另一个定义的方式，我们可以看到它另一个方式，也就是我们这里面的 SQL size manager。


那么对于这个 SQL size manager 对于大多数同学来说是比较陌生的，我们现在使用买 Badcase 开发很少单纯使用买 Badcase 我们大多是跟 string 集成的，我们使用的是 sogoscience package bin 这种方式。假如说我们真的我们不需要使用spring，当然这种场合很少，那我们可以通过 super cess manager 的方式来构建我们的 session factory，这里面我们可以看到通过它的引用方式对应传入的这些参数也是一样的。


首先我们可以看到这里面是个静态方法，我们通过 SQL size manager 你构建我们的实例，构建实例它说的参数是个对应的reader，其实这个 reader 也就是说把我们对应的配置文件作为一个文件读取器去获取出来，进行我们的一个构造，其实我们可以看到对应在这里面构建出 SQL sense manager 以后，它要还要做的事情是什么呢？我们看这里面有哪些方法，那么我们看一下整个方法结构，我们会看到对于我们这个 SQL session manager 的话，这里面有一些像commit，也就是我们事务的提交，这里面还有 delete 相关的操作，当然还有我们的 insert 等等。


我们可以看到这些的话，我们会有些奇怪，那么我们对于 super size manager 的话，它会有一些增删改查的操作，这里面我们可以看到 insert 的时候，它其实是支持我们传入一个statement，那么 statement 就对应我们在构建我们这个 Mapper 文件里面的 circle 片段，也就是说我们指定一个方法，那么方法通过 Steam 的指定一个名称来执行对应的circle。也就是说我们的 SQL sense manager 可以进行我们数据库的增删改查的操作。


那么另一个我们去看一下我们执行 SQL 增删改查的操作。为什么我们要用到 SQL size manager？我们通常来说我们会认为它应该是 SQL session 去进行我们正常展开的操作，所以说我们这里面可以我们到最上面，我们看一下我们这个 solution manager 的定义，那么 SQL session manager 它实现了两个接口，一个是 SQL factor，另一个是 SQL session，那么我们看到它实现了 SQL session 的话，我们就理解了，因为本身我们对于增删改查的操作通常我们是使用 SQL session 来完成的。


现在对于 SQL session manager 的话，它其实是对我们 SQL session 的一层包装，但同时 Soho size manager 又继承了我们 SQL satisfactory。但这种情况的话，我们可以看到 mybadcase 在实现的过程中，它是为了简化我们使用，同时构造出一个实现类的实现了，既实现了 SQL session factor，又实现了 SQL session，但这样的话其实也给我们带来了一些混乱。所以说我们现在其实单纯使用mybadcase，使用 superscience manager 去执行的这种情况是很少的。同时我们可以看到它这里面是构建我们 super size manager 的过程，其实它是一种静态方法的构建，通常我们在 spring 容器管理的过程中，我们很少使用静态方法去构造一些内容，那么在这里面我们通过 new instance 构建 circle session manager 的过程，其实这里面也是它其实只是间接地使用了 circle session back to builder 的功能进行builder，那么这里面也是把对应的 reader 参数，也就是我们可以理解为透传上我们对应的搜狗 session fact builder，构建出我们的 session fact 的对象就完成这个插入了。


其实我们可以看最终我们的 SQL size manager 它的这个构造参数，虽然这是个私有的，它构造的过程是所依赖的对象也就是我们的 SQL science factory，那么得到 SQL science factory 的时候，我们可以看到它首先对于我们 SQL session factory 的这个属性进行赋值，另一方面它生成一个 SQL session 的一个代理，那么这个代理我们是即 Java 的动态代理，生成这样一个代理实现它的正常改查都是通过这个 supersession 代理来完成的。


好，那么关于这个 supersession factor builder 的内容，我们先介绍这里，大家知道它是做什么的，也在什么地方使用，就可以达到我们的一个目的。好，接下来我们来看一下 SQL session factory，那么对于 SQL session factory 大家已经比较熟悉了，我们可以简单快速的去了解一下，这里面我们通过 SQL session factor builder 是构建一个 SQL session factor 的对象，那我们可以看一下，对于这个 SQL session factor 这个接口它定义了一些超转。


首先我们可以看一下它的 open session 方法，这里面主要的方法也就是 open session，它通过各种不同的参数去构建我们这个 SQL session。我们可以看到首先它支持参数，这里面是我们的 auto commit，什么意思？我们可以来是否自动提交？下面是我们的connection，就是我们通过传入一个 connection 构建一个错误session。
后面面我们可以看到这里面是我们的事物隔离级别。我们应该知道不管是 spring 对于 45 的管理，还是买 Badcase 对于 45 管理，它其实这个四五颗类级别都是依赖我们底层关系型数据库的事物隔离级别。这里面我们可以看到我们是 read competed， read uncompeted，我们这里面是可重复读，这里面是序列化。那么对于这四种四物隔离级别的话，通常在面试的时候经常会问到，这里面我们需要了解各个四五隔离级别它的一些特征是什么。我们看一下这是我们的 activator type，也就是 mybetted 执行的类型，这个是一个枚举类型，我们可以看到这里面是支持三种我们的 simple reels 和 bits 这样几种方式。下面我们可以也就是对于我们上面这几种方式的一个组合。


好，这是我们大概了解我们 SQL satisfactory，它定义这个规范支持的一些参数，我们可以看一下它的默认的实现有哪些。从这里面我们可以看到对于 solution sense factor 有两个实现类，一个是我们刚才介绍到的 solution manager，另一个就是 debug 的 SQL science factory。其实我们所使用的 SQL science factory 的实现基本上都是基于 debug SQL science factory 来完成的。对于 defeat 所有satisfactory，我们 care 它是在我们的 my badcase 的 season debug 这个包下面，也就是我们这些关键接口的一个默认实现。


对于我们 debug 的 SQL satisfaction，它构建的过程它是需要一个 configuration 对象，那么我们可以看到它拥有这个 configuration 对象以后，才可以去创建这样一个实例。到这个实例我们最基本的操作就是 open session，也就是我们获取一个搜索 session 的实现。在这里面我们可以看一下一个 open session 它的实现的过程，我们看到它这里面都会调用到 open session from data source。这里面我们可以知道 supersession 其实是我们 g d b c 一个 k text 的一个包装，所以说我们如果说打开这块 session 的话，我们一个前提是需要通过我们的数据源，那么基于数据源我们可以看它做了哪些操作。在这里面这个在我们讲解我们 mybetty 执行流程的过程中，跟大家介绍到我们基于这些参数创建出我们 SQL 参数对象，这里面我们可以看到它也跟四五相关的内容。


通过我们创建一个新的事务管理器，这里面是我们的accuator，也就是我们的执行器得到我们的一个执行器，那么我们看到创建 accuator 的时候，它是使用了我们的 transaction 四五和我们的 x 的对应的一个执行type，那么通过我们这样的话得到我们的activator，我们知道涉及到 g d b c 相关操作的话，通常会需要一个事务的管理。我们通过 accurator 和我们 auto committer，也就是我们配的 4 伏自动提交这样的参数，也就是我们原生的最复杂的 communion 对象去构建我们的 debug SQL session 的话，就把我们这个搜索 session factory 构建完成了。


其实我们可以看到这里面对于搜索 session factory 它本身的实现看起来好像会比较简单一些，其实这里面它只是对我们的一个 g d b seed 一个包装，我们把我们的链接包装成我们对应的一个 SQL session。好，那么我们回来接着看。我们这里面是我们的 XML configure builder，我们可以看到通过命名我们也知道 xmail configure builder 是构建我们 configuration 对象的。在初始化的过程，我们是通过 super satisfaction factor builder 去传入对应的reader，这个 reader 最终它是给了我们的 x mail configure builder，通过 x mail configure builder 进行一些复杂的解析，得到我们的 configuration 对象。那么我们来现在来看一下 XML configure builder 它所操作功能，那这里面我们还可以通过我们的 Supersense package builder 来去构造。在这里面我们可以看到对于 circle session impact builder 的过程，我们会把对应的reader，也就是我们的上下文信息和property，我们都会传入我们的 XML configure builder，那么这就是我们说刚才讨论的 external config builder，那么对于它的话，它在构造的过程中会把这些参数再去进行一层碰撞代理传入我们的 XPOS process。


也就是说对于我们一个 x 苗，一个解析器，我们这里面的 external configure builder，它其实最重要的方法我们可以看到就是这里面的pass，也就是我们的解析方法，那么它通过 pass 解析得到我们 configuration 这个对象，那么整个这个过程都是一个解析的一个过程。


其实这里面的几个关键操作我们可以看到这里面，首先是我们通过 pass 进行获取到我们的 evil NODE，就是获取到我们 configuring 信息的一些内容。我们知道对于我们在配置信息的过程中，我们可以看一下 my best configuration，它所有的配置都在这个节点下面，也就是 configuration 节点下面，所以说因为它都在 configuring 节点下面，所以说这里面解析的过程中，首先它会获取到 configuring 这个节点下面这里面再进行一些真正的解析，那么我们来看一下解析，在这个解析的过程中它这里面可以看到它有一个防并发的操作，如果说已经带解析的话它就会直接抛出异常。


我们可以看到这里面解析的内容还是比较复杂的，它会把我们买 Badcase configure 里面所有的这些节点进行逐个的去解析。我们可以看到对于我们买 Badcase Configure 里面所支持的这些属性，像setting， taballines 和我们的Mapper，我们可以看到这里面是 property setting 和我们的 tablets Plug in，我们还没介绍，到后面我们会介绍，这里面还会涉及到一些散牙文信息，我们的 DATABASE ID provided tap， handler Maps，那么这些都会逐步的去进行一个解析的过程。


所以说对于我们通过 XML 配置去做一些配置变化的过程中，是不是都会避免不了这样一个解析器，那么由于在 string 它的推崇下，逐渐的去弱化 XL 推崇用注解的方式进行一些解析，其实 my batch 它在注解上也做了一些不少的工作，这里面我们可以看到对于 x mail builder， configure builder 所做的一些字讲，其实就是获取到我们的 Xmail 配置文件，进行逐个元数挨个解析，把这些 XL 反序列化成我们的一个加法对象。


这里面的加法对象就是configuration，那么得到这个 configuration 以后，对于 x 庙 configure builder，他的工作那么也就完成了。那么这里面我们得到了 Xmail configure builder，通过构建出我们的 configuring 对象，现在我们来可以看一下 configuring 对象，它本身的内容非常多，但是它并不复杂，在业务上它其实我们可以对它简单的一些理解，我们可以看到 configurity 下它可以理解为就是一个POGO，那么这个 POGO 里面是放了很多一些 KV 的属性，我们基于这些 KV 的属性把我们 XML 配置的信息映射到我们的 config 润对象里面。这样我们来构建 circle satisfaction factor 的时候，把我们的各个配置进行一个生效。这里面我们可以看到我们的 configure 对象，这是我们的 3 + 2 环境信息。


下面我们的各种的参数配置信息，我们看了这里面是 log m p l，就是我们在配置的过程中可以打印我们的搜狗参数和我们执行的搜狗语句等等，我们可以看到这里面很多很多的一些配置，具体这些配置的内容我们就不去一去细说了，这里面我们看到对应的 extra type，也就是我们的 x type 是一个simple，我们看这里面的东西很多很多，如果大家对哪个参数配置比较关心的话，可以在这里面有针对性地去了解一下这参数的一些配置信息。
OK 了，这里面有cats，当我们涉及到缓存的时候，会有一些 cats 信息，还有我们的 result map，也就是说我们在 Mapper 里面配的 result map，它都会在这里面进行一个汇总。这里面还有我们的 k Generator，也就是我们的主键生成器等等很多这样一些信息。


那么上面是属性信息，我们可以看到它也都是 final 类型的。下面就是对于这些属性信息的一些注册的方式和或者我们蒸餐改查的一些操作，这里面我们可以看到对于买Badcase，它注册了很多一些别名，这里面比如GDBC，我们对应的是GDBC，train， section factory 等等。


这里面还有一些像我们这里面对于缓存的处理策略，这里面 FFO 你就先进先出LRU，我们的还有soft，很 weak 等等，我们可以看到它定义了很多。还有这里面对于我们的日志管理器，这里面有 s l，four， j 和我们的 common log，一节log， four 减log， forty two，还有我们的 s d 就是我们的标准输出器，我们通过我们的标准输出器输出我们打印出来的 SQL 和我们的一些参数返回值等等一些信息。


这里面是定义了一些别名，那么好通过这些我们可以简单了解一下我们的 configuration 里面它做了一些哪些事情，也就是说我们所有为通过配字可以解决的问题，我们都可以在 configuration 里面找到它对应的一个表达，那么我们了解了configuration，也了解了 SQL session factor，那么接下来我们来看一下 SQL session。那么在这里面，对于我们来说， SQL session 是通常我们在做 mybadcase 操作的时候，跟我们接触最多的一个接口。其实我们如果说使用 Mapper 的话，其实 Mapper 把 social session 进一层包装，我们甚至连 social session 的感知都感知不到，我们使用 Mapper 的过程只会关注到我们业务定义的这些 Mapper 的接口，那么看一下 SQL session 它做了哪些事情？这里面我们了解 SQL session，我们可以先看一下 SQL session factory，通过测试 Packder open session 的方法，得到我们这样一个 so group session 的一个接口。我们看 SQL session 它是继承了closeable，也就是我们这是一个 i o 操作的理由，它说通常都会具备的，也就是具有一个 close 功能。我们可以了解到我们 super session 其实对于一个 collection 的包装，我们一个链接是可以关闭的，所以说它是支持 close ball。


我们可以看一下 circle session 它有哪些方法，我们把它的这个方法结构调出来，从这里面我可以提供的方法是很多的，对于通常这里面我们对于事务的管理，这 commit 还要对于缓存的清除， delete 和我们这里面 Flash statement 就是刷新我们请求执行。下面是我们的一些正常改查，就是 insert rollback， rollback 跟 commit 是对应的，一个对于我们事务的提交和事务的回滚。


下面对于我们常规的一些查询操作，我们这边是 select 的操作，下面有 select list 就是我们获取到一个列表，还有我们对于 select map，假如说我们没有对于这个对象进行一个 resort map 映射的话，我们可以直接把信息查返回出一个 map 出来。


当然我们查询的过程还是基于Robuz，也就是进行一个分页的操作。大家注意一下对于 my Betty 人默认的 robug 它的分页操作，它其实是一个内存分页，也就是说它的分页的信息不会传递给数据库，所以说我们知道对于这种内存分页，它的性能和效率是比较低的。通常我们会必须使用类似于我们 MySQL 的一些分页查询，我们通过 MySQL 的 limit 操作去指定我们返回的数据量。好，这样我们可以看到对于 super session，它其实也就是提供了一些对于我们数据库相关操作的一些封装。那么我们来看一下 supersession 它的一个默认实现，对于 Supersession 它的思想，我们可以看到这里面有 defer 的 Supersession 和 supersession manager 以及 Supersession template。


那么对于我们 supersession manager 刚才已经跟大家介绍了，我们看一下搜索 session template，我们可能看到 template 我们会比较有一些似曾相似的感觉，我们了解的 GDB c， template 等等一些模板化操作，其实对于模板化操作，它最终还是会用到了我们抵费的搜索三四分。


我们先看一下我们 SQL session template 模板化操作它做了哪些事情。对于模板化操作，我们它实现了 SQL session，我们可以看到它在构建的过程中，它是需要一个sociosentfactory，那么通过 circle session factory 构建我们相关的一些信息，这里面最终会执行得到我们的一个 supersession 对象，我们可以看到在这里面我们进行的过程中，首先我们的 circumstances factory，我们的 accurate type，我们这里面 exception 的 translate 也就是我们的异常处理器。也就是说我们可以看到这是 org my Beta spring 包下面的 SQL33W 的，所以说通常我们在跟 spring 打交道的时候， spring 会把底层，也就是说 my Betty 是相对于 spring 是一个底层，它底层的一些 IO 超出的 exception 进行包装，所以说它用了我们的一个异常转换器。


这里面我们可以看到它会生成一个 circle session prox，也就是说也是通过我们一个 GDBC 动态代理的方式生成我们一个 supersession 的一个代理实现，这里面通过代理实现来完成我们的操作。好，那么这样的话我们就能获取到我们一个 SQL session 的一个相关操作，那么我们来看一下它的一个常规的正常改造成儿，比如我们看对应的select，我们可以看到这里面 slack list 它做了哪些操作？我们看它 slack list，其实它的操作就是使用了 SQL segment proxy，也就是我们代理实现直接调用了 slack 的list，最终它还会用到我们这里面对应的一个实现，也就是我们的 debug SQL session，最终真正干活儿的工作还是 debug SQL session。


现在我们切换了 debug 的 SQL session，我们可以整体来看一下这个类的结构，它是直接实现了 SQL session，我们看到它也是在 ibadcase session defield 这个包下面，也就是这个包下面通常是我们对于一些内容的一些实现，刚才我们看到像对于 debug 的 SQL session，我们可以看一个是 debug 的 SQL session，一个是 debug session faction 作为我们的一个默认实现好，那么这里面我们看到一些常规的一些属性configuration，我们的 accurator 以及我们是否自动提交事务。好，那么我们看一个具体的一个 select list 方法。好，那么在 slack 的 list 它也是多个方法的一个重展，我们跟进来，那么到这里面是执行到了我们真正的 slide 意思的操作，操作的流程，我们在 my badcase 执行流程的关键方法里面，我们给大家介绍到我们通过 configuration 获取到我们的 map statement，那么通过 statement 执行，通过 icuter 进行执行我们具体的一些信息。对于我们的 SQL session，主要它其实也就是在它这个工作执行完成以后，把它的下一棒交给了我们的 IQ ator，通过 IQ 特进行我们相关的一些 query 操作，去跟数据库进行一个打交道的一个过程。


好，那么这里面我们跟大家去介绍了 supersession 相关的一些内容，那么这是我们的初始化构建相关的一些关键的接口。那接下来我们来看一下跟我们执行相关的一些接口。

