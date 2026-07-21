---
title: 1-2 Mybatis架构分层设计（2612）
---

# 1-2 Mybatis架构分层设计（2612）

同学们大家好，这章节我们开始学习 mybadcase 的架构分成设计。 mybadcase 作为一款优秀的持久型框架，在互联网公司广受欢迎，跟它灵活的设计是分不开的。
说到 mybadcase 的架构设计，我们这里面包含两层含义，第一层是 mybadcase 在设计过程中对于模块的一些划分。对于mybadcase，它核心也就是我们常用到的 mybadcase 这个大包。对于在跟 spring 集成的过程中，它同时提供了 my Betty spring 这样一个依赖栅。 my Betty spring 这个栅包很明显它是为了提供 my Betty 与 spring 集成的一个方案。因为我们在当前的 Java 业务开发过程中，不用 spring 的真是太少了，所以说 Myback spring 它提供了一些基于 XL 配置的方式，或者说基于注解的方式进行对于 my best 这些模块的进行扫描，简化我们跟 string 的集成。那么随着 spring boot 现在的火起来以后，同时 my bettage 也与时俱进，它同时也提供了 my betted spring boot 这样一个模块。我们知道 spring boot 更多的是一些制动装配，同时 my badcase spring boot 它提供的功能也是通过一些 auto configuration 更加简化我们的配置。


好。这是我们介绍的自 mybadcase 的这些常用模块架构分成的设计，这里面涉及到首先是 mybadcase 的核心，第二进一步是 mybyte string 与简化我们跟 string 的集成。第三我们是买 Badcase spring boot，那么我们通过这三个模块层层递进简化我们跟现在的 Java 业务开发这些框架的集成。


好，那么我们说第二个层次的含义，也就是对于 Mybyte 核心的这些设计分成，那么我们知道 Mybyte 使用起来还是比较方便的，我们通常会使用 Mapper 接口或者说 SQL session，我们这样的方式去执行我们对应的收口的查询语句。那么通过这样一种设计，那对于买 Badcase 它底层的设计其实还是有一定的复杂程度的。我们知道这里面会涉及到 x 秒的解析，我们对于 j d b seed，一些分成的代理等等，最终执行到我们的 SQL 语句，把我们 SQL 语句返回的对象集序列化成我们 Java 的 VO 对象，那么这个过程还是有很多工作要做的。


首先我们来看一下 mybadcase 这些常用的模块，在 mybadcase 它官网上我们可以看到，其实我们关注度最高的，首先也就是我们的 MYBADCASE 3，现在是对应的 get help 的地址是 MYBADCASE 杠 3 这样一个地址。那么另外我们是关注的是spring，那么这里面我们可以看到，因为整个 git help 模块，它是在 mybadcase 这个 namespace 下面，所以说对于命名上简化了一下，这里面只是spring。


其次它对应思路的炸包日是 mybetted spring，我们可以从这里面看到它的模块的名称是 mybetted spring。对于 mybettage 三这样一个模块，它对应的是 my Betas，因为我们现在 my Betas 它的版本是 3 以后的版本，因为再找一点，对于买Badcase，它的命名是 i Badcase，后面改名是 my Badcase。因为买 Badcase 3 以后，在这里面直接就对于这个 git 空间就命名为 my Badcase 3。


另一个词，我们的 spring boot STARTER，因为如果说我们只看 spring boot STARTER 这个名称很容易混淆，因为我们在学习 spring boot 的过程中，我们知道像 spring boot starter 使用的非常多，那么这里面也是因为它是在 mybetty 这个空间下面，我们命名为 spring boot STARTER，它是特指 mybadcase 与 spring boot 集成的一个STARTER。这里面它会涉及到哪些内容？这里面会涉及到像 mybadcase spring 步的 auto configuration 以及 mybadcase spring put starter，通过这个字我们在开发过程中可以引入的这个模块的名称。另外还有一个是我们在写一些代码生成器的时候会用到这里面。


Generator，那么通过 Generator 我们可以非常方便地生成一些蒸餐改查的一些对象。我们可以基于数据库，我们通过 generate 映射的过程，我们生成我们的VO，生成我们的 Mapper 文件，生成我们的对应的 Mapper 的 DU 层。操作其实也是很方便的一个过程。


接下来我们来了解一下 my Betty 这几个常见的功能模块，这是对应 mybadcase 它 Git Hub 上面的页面。这里面我们选中 repository 进行一个，根据它的点赞量进行一个倒排，我们可以看到它的排序，比如我们认为点星最高的是 my badcase，现在是 16000 多个，这个点心量还是挺不错的。


另外这里面第二受欢迎的就是Generator，那么 Generator 呢？它是 4K 的点心量，后面是我们看 string 布的 starter 和对应的spring，这里面我们就需要考虑一下对于买配置核心的它的这个，嗯，我们的 Git 会不会有库的话，它的典型量非常高。


那么另一个对于像 spring boot， STARTER 和 spring 的，它的典型量比较低的，为什么呢？其实并不是说我们对它的关注度比较小，是因为我们在使用的过程中天然使用spring，那么对应这些引入的过程，其实我们并不是那么关注了，我们可以看到对于这个 Generator 它的典型量非常高，那么它典型量比较高的原因并不是说我们在程序业务开发过程要使用它，是因为我们需要通过 Generator 去了解一下这个代码生成器的一些逻辑。我们可以切到我们的 Web 页面去看一下对应的这些情况。在这里面我们还是可以从这边看到我们对于mybadcase，整个这个目录空间下，他最关注的还是mybadcase，这里面指我们再向后看 report 其他一些重要的信息。


我们这里面也是 Generator 和我们的 spring boot STARTER 以及spring，其实因为随着 spring boot 里的兴起的话，我们其实使用 spring boot 进行依赖的功能是更多了，所以说我们可以直接引入对应的 spring boot starter，我们可以不用特意去关注对应的买 at 司令和我们这买 Badcase 核心的抓包的一些内容。好，这里面我们也同时把这些源码克隆下来，我们可以通过这些对 ID 的源码进行一个简单的一个分析的介绍。


好，这里面我们首先来看一下 mybadcase 的核心的源码情况，这里面我们可以看到对于 mybadcase 它整个模块，这里面对于 MySQL 的 palm 文件，这里面的包结构设计还是比较清晰的，我们很容易明白对于 mybadcase 它各个模块里面存在的位置，这里面我们可以看到其实虽然现在我们叫mybadcase，它里面还存放着 ibadcase 的影子，对于这些包结构并没有去做统一的一些修改，我们可以打开对应的 palm 文件。


我们去了解一下这个 mybeta 它的设计过程中的一些依赖。其实买 Badcase 在设计过程中还是比较有一些洁癖的，对于买Badcase，它的设计过程中它尽量不去依赖第三方的内容。我们从这里面可以看到，虽然说买 Badcase 它依赖了一些炸包，但是我们可以深入去了解一下。


我们会发现这些炸包我们看大多数它是为了基于当前的测试去进行引入的，也就是说我们真正的买 Beta 的核心内容，它依赖的内容非常少。首先这个 CG 内部它是一个，其他的还是非常少的。我们可以看到像对于 MySQL 的GDPC，它认为是默认提供的，比如这里面的 HR 数据库，这里面我们看也是它一个认为是测试环境使用的。当然下面我们看了这是 home logging，这是我们的一个正常需要依赖的，我们可以看到这里面是 compare 类型，也就是编译需要的，这里面还涉及到 cats exceptions 的一些扩展，这里面要看这都是跟池子相关的。


下面对于 gunit 还有我们 log for 接在这里面是一个依赖的过程，其实对于 Maget 依赖 log form 街，这也是一些历史原因，因为现在我们其实很少在心动了，直接使用 log for 接了，我们可能更多的会推荐大家使用 log back 和 log for 接第二个版本，所以说我们可以看到这里面也是它最终会通过 s l for 接， local for 接这样的方式进行一个替换，也就是用桥接的模式把 logo for 接在我们已有系统上移除出去。


这里面对于 MySQL Connector 这里面我们也是测试环境，因为 mybadcase 它作为一个关系数据库的持久层框架，它当然并不会显示的去依赖 MySQL 或者是HR。根据我们的业务情况，我们需要 MySQL 我们就引入MySQL，那么需要 HR 就引入HR，后面我们看到还有一些相关的一些炸包，这些也大都是以测试情况为主，当然它还会有一些我们可以从这里面去看到它还有一些依赖，它是一种我们可以 optional 也就是可选的形式看我们这里面对于 OGL 的一些依赖，那么 OGR 虽然它 scopes compare，但是它的这里面必要是 optional 为true，也就是说不存在这个依赖也是可以正常工作的。


同时这里面有对于 Java sister 也是这样一个逻辑，OK，对于买 badcase 它这个依赖，我们可以简单介绍一下这里面它的包结构，我们可以看到它的根的包结构是阿帕奇下面的ibadcase，那么因为我们现在虽然叫mybadcase，它因为历史是基于 ibadcase 演进过来的，这个包结构并没有进行修改。


下面我们可以看到整个包的设计过程，这里面有一些跟注解相关的一些内容，我们打开去看一下，看这些注解，其实因为我们也经常在使用 my badcase，看到这些注解应该不会陌生，比如说我们这里面会有一些隐色的相关的注解，隐私的对应的这些 value 就是我们要执行的 SQL 语句，这里面可以设置一些 DATABASE ID 相关的一些信息。


这里面有insert，我们可以看到 delete 其实是一个相同的一个道理。同时我们看它这里面还会涉及到 Mapper 这个注解，其实我们使用的是比较多的。OK，对于这些注解的话，我们不会一一去介绍，下面这是一些班顶一些绑定的一些操作的方式，其实这里面最重要的也就是我们的 Mapper problem process，也就是说其次我们在通过 Mapper 一个接口去映们对应的正常给它操作的过程中，它最终会生成一个对应 Mapper 的一个代理，我们会通过 Wifi 代理来间接的去执行 GDBC 相关的一些操作。
这里面我们看看涉及到一些缓存相关的一些内容，这里面是 builder 构建我们对象的一个过程，这是 did source 相关的一些内容，我们可以看到这里面是执行器，这里面是定义了一些异常执行器。这里面我们其实比较关心的，对于 cuter 这个接口，我们可以看它底层的一些实现，这里面有 base executor，我们的 base 批量的，我们的开嵌支持缓存的，其实我们默认用最多的还是这个 simple executor，后面是g、d、b、 c 相关的一些原生信息的一些转换，我们可以通过 circle Runner 来进行一些操作的一些执行。


好后面的内容我们就不去这样一一介绍了，当我们在介绍 my Betas 执行 SQL 的流程的过程中，会更详细的跟大家介绍里面的内容。接下来我们来看一下下面的两个模块，这里面一个是我们的 mybadcase spring，另一个是 mybadcase spring boot。我们先看 my Betty spring，在 spring boot 大火之前的话，我们通常是基于 spring 来跟 my Beta 进行集成。这里面我们看一下这个 MIT string 这个模块它提供了哪些功能。


其实首先我们也是可以看一下对应的，我们这里面 my betas 不用这个 palm 依赖的内容我们可以看到，首先对于它依赖的情况，肯定它会依赖spring，这里面我们可以看到它对于 my bench 的依赖和 spring 的依赖。这里面还涉及到 spring batch，因为 spring BAT 进行批处理的过程中，它里面涉及到一些 item reader 和 item writer，它同时都可以对于 mybadcase 进行一些读写操作。


好，我们看一下，对于我们要使用 Mybyte stream，它默认的是肯定需要我们提供 Mybyte 操作，也就是 Mybyte 这个核心炸包，同时这里面会涉及到 string context 也会作为我们默认提供的功能，这里面默认提供的功能它就是在我们的依赖的过程中不会显示进行依赖。这里面会有我们的 spring JVC 也是要求我们默认提供的，我们可以看到这是我们常见的依赖的一些内容。后面一次我们看 Derby 和 deunit 对应的 Jupiter 音阶，这都是由我们基于测试环境使用的。好，这次我们大概了解了我们的 my business string 采集的一些内容，那我们来看一下 my business 它实现了什么功能。


对于 Mapper spring 它实现的一些功能，我们可以看到这里面是有我们的 Mapper scan，我们知道 Mapper scan 是会扫描我们在对应的 mybadcase 工程里面的 Mapper 文件所在的包结构，我们这样会在执行的过程中把这些 map 的接口生成一个对应的代理的实现类，那么基于这个实现类去间接的执行我们的一些 SQL 的操作，我们再看另一个，这里面对于跟 map scan 对应的是 class pass map scan 的一个实现还有哪些？我们这里面还会有一些四五升的封装，我们可以看到对于 spring 的 manager 的tracson，我们可以看到对于 my badcase 的一个tracing，也就是这个四五的内容，我们可以看到它里面会包括一个 GDBC transaction 和 spring match 的Transex。那么我们当使用 my better string 跟 string 进行集成的过程中，我们默认的 show 就会切换成对应的 string manager 的Transex。


好，我们接下来这里面去看一下，这边还涉及到一个 supersession 的template，以及我们看这里面还有一个 supersession factor bin，我们看到以 factor bin 结尾的这些对应的类的话，我们应该知道它通常是实现了对应 spring 的 factor bin，我们通过 factor bin 里面的对应的 get object 这个方法获取到我们一个 super session factor 这个对象，我们通过 factor bin 进行一个属性的注入，最终通过 get object 得到一个这样对应的对象。


其他的我们可以再简单看一下，这里面我们看到了我们对应的badcase，因为我们这里面并没有跟大家去详细的介绍 string badcase，大家可以了解一下，对于 string badcase，它通常会涉及到对应的，我们可以称为ETL，它对于数据的抽取、转换和写入。那么这里面对应的是reader，就是我们读取，那么 write 就是我们进行写入的一个操作。


对于转换的内容通常是我们的业务逻辑需要我们质疑一下，我们可以看一下对于这个我们的 customer reader，它其实是这里面是继承了我们的是 item counting item stream， item reader，其实最终它去实现了是 item reader 这样一个接口，这里面其实还提供了一些 XR 解析相关的一些内容。


我们可以在这里面看一下这里面对应的 spring handler，这里面提供了一个叫 spring configure 的 name space handler，我们这里面去看一下，这里面是对应的 name space handler，这里面我们可以看到它在构建这个的过程中是对于 SCAN 的一个解析处理，对于 SCAN 我们可以看到它里面会包含的一些特殊的一些信息，那么这里面我们可以看到如果说我们还使用 XL 配置的话，我们可以通过 spring bin XL bin 的方式直接去配置相关的一些信息。


这里面我们可以去看一个信息，我们可以看到这里面是 application contact name space，其实它是在我们 my Beta stream 源码的 test 包下面，我们可以看到这里面如果说我们需要基于 XL 配置的话，我们可以通过 my best scan，我们 base packets 指定一下我们的 Mapper 的目录，那么就可以把这些扫描出来。通常我们现在用 XL 配置的比较少了，大多我们是直接使用我们的注解去配置。同时如果说我们使用 mybetty 这个 name speech 的话，我们一定要注意一下对于 XML 它这个 scammer 的配置，我们这里面需要指定一下对应 mybadcase 的 namespace 的一些配置，所以大家了解这一点就可以。


后面我们来看一下 my Betty spring boot。那么切到我们的对于 my Betty spring boot，我们可以看到它的 get 功能是 spring boot starter，对于它的模块名称是 my badcase，是准布的，我们可以先把它的模块收回来。我们可以看到这里面拆分了几个模块，第一个是最重要的，也就是我们的 my Betty spring boot auto contribution，也就是说我们通过这里面的自动装备来去初始化我们 my Betas 的一些配置的工作，通过预定大 a 配置的方式减少我们的一些配置工作。


那么另一个是我们的 my Betty spring boot starter，我们看到starter，我们知道它通常它里面不涉及的代码，它只是通过 palm 文件去管理其我们的这些依赖，进行直接或间接的一些医疗。其实我们现在做 Mybeta 开发使用什么步的话，我们只需要把这个对应的是 Mybeta 什么部的 seller 引用进去，那么我们其他的依赖就可以忽略掉了。


你看这里面它间接的依赖哪些依赖？这里面像 spring boot STARTER，当然它因为依赖 spring boot 环境，所以说这个是需要依赖的。这里面还涉及到 spring boot STARTER 的GVC，通常对于我们这些关系性数据库的操作都会涉及到 GDBC 协议，它里面会有默认的，我们知道 SR 的一个测试数据库。这里面接下来是我们的 mybetis string 部的 auto configure，也就是上面提供的模块儿。同时我们看还指定了我们的 my Betis 以及 my Betas spring，也就是说我们引入了 spring boot STARTER 这个对应的模块儿，那么对于 Mybest 和 Mybyte spring 这些炸包就不用我们再手工引入了，同时它也会把 spring boot 的对应的 GDBC 的 starter 和引入进来。


好，我们再看一下，下面还涉及了两个测试的模块，这里面一个是 Mybase spring boot start test，一个是 spring boot 对应的 test auto configure，因为我们知道我们使用 string 部的开发的过程中，通常会给我们带来一些友好的一些测试的体验。对于 my best 当然在这方面也不甘示弱，也跟我们提供了一些比较好的一些 test 的一些相关的一些工具，对于测试的相东西的话，一些自动装配的一些信息，这里面我们可以看到这里面是 autoconfigure my betties，我们这里面同时是 my Betty 的test。
我们应该还知道，我们其实在 stream 部的开发的过程中，我们通常会包含比如说是d，d，b， c test 或者其他的一些，对于我们可以理解为是一个 test 的分片，因为我们通常使用 string 布的 test 的过程中会把我们整个容器进行初始化，那么如果说我们对于这个测试用例的一些分片操作，这样可以大大提高我们执行单元测试的一些速度。


好，那么大家理解这一点就好，那么我们可以看一下这里面的 auto configure，因为 auto configure 是我们对于 Myback spring boot 最关心的内容，这里面其实更多的是我们定义了一些 auto config，我们可以看到这里面是 Myback auto configure，同时我们也可以想到这里面我们会有 string factory，里面会指定我们这里面 enable auto configure 所配置的value。这里面一个是 my betts language driver auto configure，另一个是 my bet is auto configuration。OK，好。


其实这里面也就是我们这两个自动装配相关的一些内容，我们现在就不展开看了。好，回到我们的PPT，对于 Mybest 各个模块的一些情况，我们先介绍到这里，下面我们来重点介绍一下 mybadcase 3 这个核心模块里面所包含的内容。其实对于 mybadcase 核心的话，我们对它的架构分成通常也会包含，对应的是首先是接口层，后面是数据处理层以及我们的框架的支撑层，在这里面的接口层也就是我们通常在做业务开发过程中跟买 Badcase 打交道使用到的东西。那么这里面接口层，我们通常现在开发，我们会通常定义一个 Mapper 接口，那么在 Mapper 接口里面会有对应的映射，对应到我们的 my Pad XML 里面去写我们对应的一些方法的查询的条件或一些参数，我们对应的方法的一些对应的SQL。


另一种是我们通过 supersession 执行一个指定的 statement ID，那么这个 statement ID 通常也是我们在 XML 里面 Mapper 文件定义的 statement ID。所以说我们通过这两种方式可以触发我们对 Mybase 的调用。那么首先在接口层，也就是我们业务层跟 Mybase 打交道，是通过接口层的 social session 进行执行 state ID，或者是通过 maker 接口进行触发我们方法，通过代理的方式执行我们底层 SQL 的一些处理。


那么另一层是我们的数据处理层，其实我们通过接口把这个调用发出去以后，看似非常简单，其实它底层进行了一些很复杂的处理。我们可以简化地说，首先它会对于这个参数进行一些处理。首先我们通过 permit handler 进行参数处理，参数进行映射，比如说涉及到一些 purpose 的处理，我们把参数如何去注入到我们对应的 SQL 的过程。另外我们这里面会通过 SQL source 对于 SQL 进行一些解析，完成对于这个 SQL 它的一些合法性进行校验。因为我们知道在 mybytes 写的过程中，我们的 XML 是支持比如说一些判断的表达式，还有一些是涉及到一些义词的一些遍历等等。其实这个 XL 里面的配置它是基于 o g l 进行一个解析的注，最终我们可以把这个支持迭代的 SQL 生成，我们真正的在 SQL 的一个静态文件。


那么生成以后，接下来我们会通过 activator 的 SQL 执行，那么 actuator 它底层的一些实现，我们知道这里面涉及到一些 bytes 和plexin，以及我们的simple。其实通常我们会执行的一个 simple 的 equator 进行我们参数的执行，那么参数执行对应执行完结果以后，我们会需要一个 result handler 进行，把我们这个 result 结果映射成我们对应的 VO 对象，那么通常这个映射的过程中，我们知道我们会通过反射的方式进行我们属性和我们对象属性的一个，也就是我们数据库的字段跟我们对象属性的一个映射，这里面其实分两种，一种是反射，另一种是我们通过 XML 指定配置。比如说我们把某个 VO 它的这个 Mapper 文件进行一个一一对应的配置，这样会减少我们这个映射的复杂度。


那么这是我们的数据处理层的一种东西，其实对于整个框架它还会有一层基础的一些支撑层，比如支撑层会涉及到比如我们 SQL 语句如何配置，测过语句配置的方式，一方面是支持在 XL 里面去配置，另一方面它还可以通过注解，在我们的接口方法上通过注解的方式去写一些简单的一些收口。


那么涉及到数据库操作的话，尤其是这个关系性数据库，我们都会对于四五进行一些管理性的操作，那么对于四五是如何管理的，这也是需要我们框架支撑去处理。另外它直接对于我们买的关系数据库的操作还是依赖了 GDBC 协议，那么底层的 GDBC 是我们对于连接词的管理，也是需要进行一些管理的，通常我们也会依赖我们的 data source 的数据库连接词进行页。同时 my patch 还提供了一些缓存的机制，可以简化使用方式，帮他提供这些对于变更频率比较低的 SQL 一些查询的效率。
好，我们接下来看一个这样一个架构图，这里面也是通过我们的是接口层和数据处理层以及记录支撑层进行一些分析，整个它画的结构跟我们刚才介绍内容是大同小异，这是这样，我们可以通过这个恰扣图让我们看起来会更详细一些。首先对于接口层，我们对于接口的调用方式会分两种，一个是基于 statement ID，另一个是基于 Mapper 接口，那么 student ID 的话，它会涉及到数据的增加、数据的删除以及数据查询、数据修改这样正常改造的接口。同时我们通过配置信息维护这些接口，也就是我们对应的 map 的 ML 这样一个配置文件。


那么基于 Mapper 接口，那么哈 Mapper 接口其实就是我们定义 Mapper 接口下面实现各种方法，通过方法映射到对应的这个 Mapper XL 里面的 NAMESPACE 的一些查询操作，其实它也是间接地使用了我们的 Steven i t 的 pass 进行调用，这事我们可以理解为是接口层的操作。


接下来我们看数据处理层，我们分四大块，首先是我们参数的映射， SQL 解析、 SQL 执行以及结果处理和映射，这里面对于参数映射，我们这里面会涉及到参数的映射配置，参数映射解析、参数的类型解析，这里面我们会通过 permit Handler 进行处理。另外 SQL 解析的话，我们可以看到它会对 SQL 语句进行配置，我们在 Mapper 里面写了 SQL 语句，是主播写的。另外对 SQL 语句解析，对 SQL 语句动态语句的一些生成。我们刚才提到，如果说我们对于 in 操作，我们会通常有一个 list 作为我们的参数，我们通过 for each 的方式把这个 list 进行拆开。另一方面我们会有一些动态语句，比如说当我们的参数里面存在 name 这个属性，那么我们 name 就会作为查验条件，如果说 name 属性不存在，那么我们就不会把 name 作为查验条件，那么这样呢？动态语句 SQL 的生成也是通过 SQL source 的方式生成的。另外在 SQL 执行的过程中，我们可以看到对于 simple executor expense executor 这种方式去执行我们 SQL 的。
一些操作。当执行 SQL 操作以后，其实它底层是 g d b seed 操作 GDPC 返回。


的结果就是一个 result set，那么我们需要对这个 resource set 进行一个结果的一些映射，那么映射的过程中它会使用到 resource set handler 这个过程。也是我们首先需要对于我们映射的方式进行一个结果映射配置，假如我们没有配置的话，我们就会进行一个反式的方式，相当一个强制的一个配置里面还会涉及到结果类型转换，因为我们对于 Java 的数据类型和对应数据库的数据类型还是有一些区别的，比如说像我们的date，我们的int，尤其我们通常会介绍 MySQL 的一些字段类型跟我们 Java 的字段类型会做一些转换，同时对于我们的数据进行拷贝，也就是说把我们查询的 request chat 转换成一个 VO 的接口，整个这些处理的过程当然我们是依赖到基础支撑层的一些操作。这里面对于 SQL 语句配置方式，它是基于 XL 还是基于注解，那么都需要我们的基础支撑者进行一些解析。


那么在我们执行 SQL 的过程中，我们会涉及到四五连接池的一些管理，那么有一些操作我们为了提供效率，我们还会存在一些缓存机制，当然比如这里面会涉及到一些测购语句的一些解析，这个解析结果如果说它跟参数无关的这些动态测购语句就会缓存起来，这样我们下次执行的时候直接就把 SQL 拿过来运用了，这样避免我们在每次执行的时候因为 SQL 余的解析占用我们大量的一些执行时长。好，那 my Badcase 的架构分成设计我们就先介绍到这里，同学们，我们下一章节再见。

