---
title: 2-12 Spring数据访问源码解析-1（2036）
---

# 2-12 Spring数据访问源码解析-1（2036）

[image](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/1edc7d97-5c33-46d3-9440-b1dc7cfeca3b/SCR-20240803-nmpd.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662T6M64RV%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T232013Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCcnXuNyv1XLFoh1gOWp%2B6giD1dWCmleVO5DbuC%2BlBpgQIhAMco%2BWD8Z7nZly%2BqGu3EYjhOZ%2FXU5ZPA4UAKlzE1nY4fKogECMb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1Igzc3lAtZm7%2BAFKm0eAq3AN3iRhiMdFCYeJqM43VsXmFFCgtsXY%2F7HhoYOsvL5xSdpQn%2BZFav305zzvZtOarofjxGqarOODdaoeFFjCmnAfbox2OjMWQ3ER1T8vQrWdd39V5mOUui3Ep0CSVLEMquemMqRxVFIOXNsQXqnIUlHHUY0M39NNGhbc1a5d5f6%2BQpdk%2BH2O5fcCrRUs1Lw4sPQhkaAD%2BQa%2BjoIK8A0CUHmMiIzC1t0NJ4GnSsGH90b%2Fa%2FMC1wQNeauGhRywyy6x1i6OKvYT7DuTK3RMDqYD85sJ7IG7Kwx8Buxo1MlaG3%2Fjyh7jo0%2FcJtz4M4GjjGcV%2B46OCw3urlp7WXhrfVvDCPtjgGTin21gICpV4HIin%2FUDJyj1WaV34JLPIIcaOvSQaqzAu0J1G2t6JlaQcwfjcW0hlcDdUukbBtTlWTt53vK2L7jHVP8DUce%2FG5wmPmVSxtbRHbk2S%2BJRslnS2DV%2F%2B2Q8HhtQBAF4YF7JmXhXnPI1ytfJdqc1%2ByLIMIEiuFxaHUlQYAHxYp5w2uWx%2BhxAtCIetq5BDrSFt%2FvciGaPA2Wc3OH5k362HlV54AI67J3UDPnZDBiTjUZSL3%2Bgf5Y5uJ7zQMKIpue3L9u46ezdl5A%2F%2BigQBdmaCPOq8Kg%2BsSjCjuP%2FSBjqkAeFoxbKahED%2BRcJ6H8Va3bEveyQXQl3hj%2BGlzyxvIs7UfXTEtTlS9CyIXbcLwE%2BrSJSV1Ev5QXlS9mJr5MerNr76P1i9R1V%2FJEqk8AVTfvfCgSm0HHIBP1vHQEUzKa7nnWTwI6CvIcmtrBxagZozu9LbZOcJNcr%2FLxFtBP9BOOuGLTBhTcO5Okl%2Fs7hkY6apM%2BpBk4Pir8PB%2BhFdzO9UqYIg62LR&X-Amz-Signature=d275b0de779d8899e31634badb62bc714f6cad30d5650286e028c3a15a101a63&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

同学们大家好，这一章节是 spring 数据库访问源码解析。 spring 核心框架做的数据层面的工作，主要是对原生的 JDBC 和事物进行了封装，方便 spring 对各种不同的 OM 框架的集成方式抽象。我们这里面分三部分介绍数据库访问相关的源码内容。第一部分是 spring JDPC 核心 API 的介绍，这里面还是回顾一下我们的 GDPC template 相关的一些内容。第二部分是 spring 的声明，是事物的执行流程，对于 spring 的 semins 四五，它也包含 XL 的方式和注解的方式，我们这里面会重点介绍注解的方式。


第三部分是介绍基于 spring 数据访问的扩展，这里面会主要介绍一下 h r 数据库的一些特性和自主机数据源给我们提供的一些功能？扩展好，接下来我们先看一下 spring j d v seed 核心API，在这里面我们可以看到，对于 GDB c 层面的核心API，我们主要分三部分，第一是 data source，第二是 DDB 的operation，也就是 GDB c template 相关的内容。第三部分是 name 的 permeter GDBC operation，也就是 spring 给我们提供了一个基于命名参数的 GDPC operation，它其实跟我们对应的 GDP template 是很类似的。


对于 data source 来说， spring 首先提供了一个潜入式的DATABASE，或者也可以理解为可以集成到我们应用里面的DATABASE。对于这里面，我们主要用的比较多的还是 HR 数据库，也就是说内存级的可潜入集成的一个数据库。对于这里面的数据源，数据源连接词，我们推荐用德鲁伊的 data source，也就是阿里出的一个 did 页。
德鲁伊 data source 它主要的特征主要是它可以给我们提供比较好的一些监控的数据。对于我们这些潜入式的数据库，我们提供了一些可以支持配置的一个操作。这里面主要是 embedded DATABASE configure，我们可以基于这个接口，它提供了 SPI 的功能，实现去配置我们自己的内容。但有一点就是说我们这个强势的这个数据库，它主要还是用于我们开发过程的功能，测试线上一般是不出现使用的，我在这里面着重强调这个兼容式的数据库，主要是因为它在开发阶段给我们带来很高的效率。


好，这是我们 GDBC 相关的一些核心的API。那么我们可以通过 spring 的源码来看一下对于跟数据库相关的这些模块的包结构和它们核心的一些类。对于 spring 框架来说，它跟数据库相关的内容主要是有 spring JDBC 和 spring OM，还有我们这里面的 spring 的TX，也就是我们的四五管理，这里面还有 spring 5 提供的 r two DBC，这个我们就不作为重点去介绍了，后面等它的热度起来以后，我们再去介绍这段你的内容。


对于这些内容我们可以看一下它的依赖关系。在这里面我们首先看我们的g、d、b、c，看这里面g、d、b、 c 里面它依赖了我们的 spring bin， spring core 和 spring TX spring context，也就是说 GDBC 是依赖了 45 相关的这个模块，那么我们看一下这种 45 模块，对于这个色物模块来说，它依赖的内容主要有 spring beans core，最重要的就是 spring AOP，也就是我们四五相关的内容主要是依赖 spring AOP 实现的，也就是说 spring 实现的事物这个功能也就是 AOP 的一个最大用户。


我们简单看一下这个 spring 事务工程，它的源码结构，在这里面我们打开包结构可以看到，首先它根目里面对应的是 DOGC 和transaction，这里面我们关心首先看DODO，我们可以理解为数据访问层的一些通用操作，在这里面我们可以看到在 DO 下面这些类主要是一些异常类，也就是spring，它在这里面对于一些数据库相关的异常都进行了一个封装。这在这里面这个 did access 就是整个异常的一个根类，我们可以从这里面看一下它的异常的一个结构，这个我们可以看到它整个作为一个异常的封装的集成。


通过这里面我们可以知道整个我们数据库访问程相关的异常都会在这一层的包装，比如说 my badcase 的异常，和g，d，b、 c 相关的一些异常都会通过这种方式转换成一个运行词异常。本来我们g，d，b， c 底层的是一些 i o exception，它是非运行词异常，在这里面 spring 把异常进行包装以后，可以让我们代码写起来更优雅一些，避免了那么多 try catch 的操作。这里面还有一个 notation 包，这个 notation 包做了什么事情，它在这里面我们可以看到它主要是处理这个 repository 注解，也就是说通过 repository 这个注解进行修辞的这些类，它都会对这些异常进行默认一个转换的过程，这是我们看到第一位相关的内容。


那么接下来我们看一下Transex，这里面它也有一个注解board，在这里面我们可以看到这是 enable Transex management，就是我们认为比较重要的，就是打开我们的基于注解的速管理的一个功能。第二个注解就是transactional，这个是我们在使用过程中使用比较多的，也就是说我们使用声明式注解的时候，把这个注解放到我们对应的方法名上面，进行一些相应的配置，就可以去生效我们的 send 事务。下面是跟一些我们看在文章的关注下，这里面在 event 这个包下面有一个 transection event list，这个注解我们也会去讲一下，也就是介绍一下 spring 是如何做到在我们的事务里面去发布的这些事件，如何保证它是只有在四件，也就是说我们事务 commit 以后再进行真正的发布这个事件，或者说是让我们的监听搜到这个真正式 commit 以后的事件，这是我们对应的这个四五相关的这报备结果。


我们看一下 GDP seed 内容，对于 GDP seed 内容是大家可能会认为比较简单，但是我们确实在生活工作过程中用的也比较少，因为我们现在的数据库查处主要还是基于 my case，原生写 DDBC 已经很少了。另一部分或者说是在一些企业级的项目可能会用到 Hive net 和GPT。


对于 GDBC 我们简单介绍一下它实现的这些功能，在这里面我们可以看到，首先它是基于配置的方式，我们可以看到在这里面有一个 GDBC name space handler，也就是说 GDBC 我们可以参考 AOP 的那个 name space handler，也就是它可以基于我们的 XL 配置，通过这种方式去简化我们的一些配置方式。


下面是跟 GPT call 核心相关的内容，这里面我们看到它有 GDPC template，也就是我理解对于这个 GDBC 这个模块来说， GDP template 可以理解为是最重要的一个操作，我们可以通过它去方便我们 GDB seed 一些操作。


下面我们可以看到跟 GDB c template 对应的，也就是 road Mapper，我们所有提出的这些 result 可以通过 roommapper 这个接口进行一个转换。对于 roomaper 它有一个默认实现，这个默认实现就是 being property roommapper，它注的事情是通过我们表的列和我们的属性的名称去做一个映射关系，如果说它是可以匹配过来的话，我们可以通过反式的方式减少我们的一些代码写入，这是我们还有对应 data source 呢，这里面有一个集成的数据源配置，这个我们在这里面不去重点介绍它了，我们可以看到这里面对应的这个可潜入的 DATABASE 它底下提供的这些实现。这里面实现的是有多种实现，这是我们 spring DDBC。


其次还有一个就是 spring OM，对于 spring OIM 的话，这个可能看我们的基础选型，如果我们选 mybadcase 的话，我们可能对于这个 spring OIM 根本不关心，因为这里面主要是提供了对于韩 net 5 和 GPT 的一些支持。


my Betas stream 本身没有提供基于 Mybest 集成，因为 my Betas 自己提供了一个叫 my Betas stream 模块，用来更好的集成，包括对于 my Betty， spring 提供了 yes STARTER 功能，也是可以方便我们继承 spring boot 方式去使用。


从这里面可以简单看一下像 spring d b c， spring TX， spring OM 它的这些源码模块的一些内容，对于 r two DBC 我们在这里面就不做过多的介绍。好，我们接下来回到PPT，看一下跟我们 spring sumance 事物执行流程相关的内容。对于 string 的生本式事物，可以支持两种方式，一种方式是注解，另一种方式是XL。对于注解，我们可以刚才在源码里面看到这三个注解，就是 enable 纯 section management，就是这个出现是开启我们的生命次数，而 transcenter 就是我们在对应需要的方法加上这个注解，它就可以生效我们的生命是四五。


那么这个 try section even listener 就是它可以监听我们发布的事件中，只有在我们指定事务相关的事件的时候，它可以监听到这些，比如说我们事务提交、事务回滚或事务完成等等这几个事件。对于 x nonsense 45，它也提供了类似于 AOP 的命名空间，方便我们使用。比如像 TX notation driven，它跟我们这里面是类似的，也就是说它都是打开基于注解方式的一些声明式事物的驱动。下面是advice，也就是对我们比较理解的对于 AOP 的一些配置操作，这里面会重点去介绍一下注解是生命相关的事物，好，对于我们生命是事物，里面事物可能有一些知识点，可以跟大家介绍一下。首先是事物的隔离级别，对于我们在使用不管是 MySQL 也好， SQL 和Oracle， 45 的隔离级别的，它都支持一些配置或者我们传输的一些定义。对于 45 的隔离级别， spring 这里面分为五种，其实也就是四种，这个 debug 它会依赖于我们所依赖底层的数据库去介绍，那么我们看一下下面这四种它的结构。


首先我们看是 read on compt 的，也就是说我们是独未提交，这种情况一般业务生产线上是不会使用的，假如我这个数可以看到其他线程未提交的这些信息，这就是非常严重的章读事件。另一方面我们就是 read competit，也就是我们读已提交，对于读已提交这种情况，其实大多数情况是可以接受的。


另一种方式是可重复读，其实在 MySQL 它默认选的 15 个类级别就是可重复读，比可重复读更严格的一层级就是序列化，序列化它就是严格我们的每一个线程是串行序执行，保证我们的这些数据可见性是绝对安全的。其实对于这种可序列化的这种情况下，我们大多情况下是不会选择这种方式，因为它的效率会非常低。


那我们接着看一下对于 45 的一个传播机制， 45 传播机制这个可以理解为它是 spring 给我们定义的一个概念，它跟数据库并没有什么直接的关系，对于这几个船，我们看这是四五传播机制，有 7 种传播机制，我可以跟大家简单介绍一下。首先第一个是required， require 就是比较常用的一个四五传播行为，如果当前没有四五，那么就新建一个四五，如果已经存在一个四五，那就加入了这个四五中，这是相对合理和比较经济的。也就是说我当前执行是需要四五的，假如说整个流程是抵在四五过程中的话，我不会创建新的，那么我就用你已有的一个四五就行。


第二个是supported， supported 就是它是支，是事物的，对于这种情况，当前方法它必须要四五的上下文的，但是如果存在当前四五的话，这个方法就在四五中运行。第三种是Medatory，他表示这个方法必须在四五中运行，如果当前四五不存在，就会抛出一个异常，它并不会主动开启一个四五。下面这个 request new 是比较容易理解的，也就是说它执行的过程中，它必须运行在自己指定的一个新的事物里面，一个新的事物被启动。如果存在当前的事务，在该方法执行期间，当前事物会被挂起。第有个是 not supported，这个也是比较极端的，也就是说表词方法它不应该运行在四五中，如果存在四五，方法在运行，就会被挂起，抛出异常。第六是never，never，也就是说当前方法不应该在事物的上下文中，也就是在运行的过程中，它会抛出异常，这种情况其实死用的会比较少一些。第七个是一个嵌套情况，他就是说如果当前已经存在一个事物，那么该方法就在签到的事物中运行，签到的事物可以独立当前事物进行单独的提交或回滚。如果当前事物不存在，其行为跟 Require 是类似的。这是我们介绍的这七种的事物传播机制。我们了解这些事物传播机制以后，我们来看一下生命式事物的执行流程。


对于生命式事物，我们首先要做的事情是通过 enable transact management 把我们整个事物开启，它做的事情是什么呢？它会通过我们这里面有一个 import selector，大家现在已经对 import selector 已经比较了解了，通过它会引入 string a 配置文件，对于这里面比较重要的 string 配置文件就是 transact management configuring selector，它做的事情是什么？它引入了几个对应的跟四五相关的一些配置。首先它引入的一个叫 auto pass rejects，这个大家理解，这是我们开启制动的 AOP 4，它的一个register。第二个是跟事物相关的part，就是基于代理的事物的一个管理的配置，它住的事情是什么呢？我们可以理解为它其实住的事情就是把我们 AOP 所需要的这些条件组装起来了。比如说 advice point cat，它构建出对应的 Advisor 可以够获取，我们 b 的过程中判断它是不是应该通过代理去获取。通过这里面我们可以看到它，首先这里面有一个 transaction intercept，其实这个也是我们整个在执行 a O P 45 的过程中最重要的一点，也就是它是拦截器通过它去开启45，完成以后对 45 进行提交或对 45 进行回滚。


这里面是 a notation transaction attribute source，它是做什么事情？它的工作主要是对我们使用注解的生命词事物作为一个属性的描述。这两个一个 interceptor 和我们的 attribute source，它两个作为属性构建到我们的 being factor transact attribute Advisor，我们看到 Advisor 我们应该知道它就是我们 AOP 构建的一个对象。可以说明首先是我们执行的操作是通过这个拦截器去执行我们的操作，那么在什么地方执行就是通过我们注解，在什么地方加注解，我们就要怎么样执行下面这个类，它是 transaction event listener factory，它主要注的就是我们如何处理这些事件，是在跟事物相关的这些事件。


通过源码来看一下，对于我们需要用生命式事物的写法，在这里我们可以看到这是一个带 demo d o test 这样一个单元测试。对于这个 demo d o 我们可以在这里面看到，我们看 find 2 或我们的C5，它都使用了纯 sex 进行修饰。对于我们读的操作，比如说 find 操作，我们是可以标记为 read only true，说明它在四五处理上会更好一些。


对于我们写方法，比如我们 seal 方法和我们这里面的 update name 方法都有了纯signal，它进行修辞，同时我们可以基于它去做一些相关的配置，从这里面我们可以看到对于这个注解，我们可以在这里面看一下它支持哪些属性，对于这里面属性它支持的是比较多的，我们可以看一下。


首先这里面是隔离级别，这里面是比如说哪些异常不进行，我们robug，这里面是它的四物传播属性，是否是 read only，这是几个比较重要的。这里面对于45，它还有 time out 相关的一些操作，比如说我们对于 45 超时间，如果说超过这个时间我们 45 就直接回滚，这里面我们同时可以指定 Transit manager，也就是我们的 45 管理器。一般情况这个我们不需要单独去配置，这是我们在写我们的数据库操作的时候，我们的四五休息此次需要这样去注解修辞一下就可以完成。同时我们还需要做的一件事情就是把我们的基于注解的错误开启一下，开启的操作也就是基于 enable Trans manager，把这个主角放上去就可以完成。


这两点的话，我们再去执行单元测试的过程中，我们看这边指定 GDP 加卡贝克，那么他要做的事情就是通过这里面找到我们 enable transact management，它里面注的词情就是我们可以看到这里面有个selector，也就是通过它也就是加上这个注解，它就会执行这个类里面的一些内容。


点进去看一下对于这个类里面它做的事情，也就是我们可以看这里面 slack import 做的一个最重要的事情，这里面它有 advice model，它是通过哪种模式的？是普通的动态代理还是 aspect 放街？那么对于我们这里面正常我们使用perfect，我们可以通过这种模式去跟一下，看我们的程序的执行过程。我们想用动态代理模式的话，它这里面会引入两个叫configure，一个是 auto Broadcast registry，这个是在 AOP 里面我们介绍过，它就是开启自动代理的一个功能。


另一个是跟我们四五相关的，也就是说对于我们四五管理器的一个配置，我们可以重点关注一下这个类，在这个类里面我们可以看到它注的事情，这里面首先用 configuration 修辞，它是个配置类，这里面我们重点看这是一个Advisor，它是构建一个 Advisor 去描述一下我们对于哪些方法进行四五管理，并和哪些类型进行四五管理。同时对于这个 attribute source 的version，它需要两个参数，参数分别是对应的一个是 transaction 的 attribute source，这个也就是说明通过我们的注解修辞的这些类。另一种方式是 transaction intercepted，也就是这是我们真正处理的我们的advice，也就是对于 45 拦截的操作，他们通过这两个对象构造出我们的advice，把这放到整个我们的 bin 里面，就可以去应用我们的45，通过 AOP 去完成我们的事物管理。


下面这个 b 就是 transact attribute source，看一下它是怎么实现的。在这里面是首先它是基于 allotation transact tribute source，在这个方法里面，这个类里面它有一个操作，也就是说它看在构造方法里面去判断一下当前以哪种方式去解析我们的注解。默认情况下我们是基于 spring transactional tation plus，我们点进来看一下它是怎么操作的，它的一些候选方法的判断，也就是它会判断我们的 transactional 这个注解，也就是说所有基于这个注解的话，它都会作为我们四五管理的第一个切入点。
好，从这模块我们回过来再看一下，那么我们看了这个 notation source，这就是我们的 check intercept，它是最重要的，待会我们去 debug 过程的话，整个主要的工作流程就在这个里面去完成的。这里面我们可以给大家看一下这里面对应的 invoke 方法，在 invoke 方法里面它做了很多词巧，这里面它通过这里面去 invoke with transection，在这里面首先它会去获取到对应的 attract source 和我们的 transegment manager。


我们的 45 管理器，通过 45 管理器去判断一下是否需要开启45，如果需要开启45，等把 45 开启以后进行执行，执行完成以后，如果说有色否相当于抛出相应的异常的话，才去判断一下是否需要对于 45 进行中断后回滚。另一种方式是对于我们的 45 进行 clean transfer info，到最后的话对我们的 45 进行提交相关的一些操作，这主要是在这个 transex intercept 的工作功能完成的。好，我们回到这个配子类，这些配子类里面我们看到还有一个比较重要的，也就是我们的跟 listen 的配置相关的，它是在我们这个父类里面去实现的。我们可以看到在这里面有一个跟，这里面 transect event listener factory。对于这个它就是当我们在事务里面去发布事件的时候，也就是发布event，通过它去判断，只有我们事务提交或者指定事务的某个状态的时候，它才去接收这个事件。


这是整个我们这个四五，它启动各种初始化的一些过程。我们来回头看一下这个单元测试类，如果说我们在执行这个 save 方法的时候，它在执行 save 的过程中，它就相当于是去执行我们事务的流程，对于事物的执行流程，我们可以在 PPT 来接着去看一下。

