---
title: 2-8 架构设计-外部配置
---

# 2-8 架构设计-外部配置

[image](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/5752a368-004c-4990-a314-15e86a0886b8/SCR-20240803-kblu.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TTSPAWJD%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T231957Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCSY5CDsmpxzyuy%2BeSuTS2a5CTJzQv8uSFw%2FbnilB12ggIgXB4jLzwkhpsUyuyRqT2rR8xL%2BN1CBiDd9hOUPb5X01oqiAQIxv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDK8%2FVdYFU0vmdMeL2ircA%2F1mYY6xdyIF%2F1jzcNjMkEA8KnGnjTt9qdn%2FH3Hx5KGkBqRoLpDscW77sTxLr0qI2Fj3AAlgoGSXHtgpBK0Aerh1EXZhqWLbZFcz84gDBm5FrjKXmv6gIc0eDvF4ZwYkcbPy9kuKqQDLDPv4oThoHyKJIV3EGGg3S2UxUFCsUIhi80vYSXvJJte50xlW4%2F6qPyZVQ%2Bavtbyu4O%2BfRljGR8UZkSEOKCTtPLEM8rnUzCxY9A5EB87u0l0s4DimrTts5LVxqN%2BsOgOvBRgguqipqi5ADXDCtqOMu%2BphxHVez8BGh8PuE5ITYIYD2bOUk2s4MaRzH15wx%2FQVeFKWJ26Rolo%2BzvjLbUyIYQZ4kR1tyd9s4lNQ7CrWhH8hLtOwcU42hrKUTHLEc7BTUVjVRUKKFbEZiKkd9UE5IXmIQYKXf5%2F6260Kh31bGc1EHQMYfRHT04CN4AU4up9IJkG6I2CKbVHxkWV8GwtqrzjVH4%2F12DvQNZvjWYqcbMus4HsKIGXBCgb%2F2TWzP%2Bf3e5Kwdu4r%2F%2Fli2MjkdwS7K0mqcQJoc4R6aaekptPAUVnSY6FOcR7n2XBoy3XGGjS7Q4GvvIuJkRkNSr%2Fd2FJKf1e%2BQVCfwHW942usW9j0eos7iDgnMN63%2F9IGOqUBVkD9c8rkeE%2B6sBJeyWyUZrrJ2yDTm%2BWgo7vN3KDnyLVrhWTZBlqlBWcdyDUsCugFtjsnjdL9FGB5HmHS1ubfVLunZWSkSRxceFrK%2FbzfiT%2FPQpUueisWQ4oqJC5dX6AzbgOlHLlbVCdbYKP1ym%2FZ6IaY4zbXZGLVv7deg2qcSaNqHb509QbkaooYD4P4Yvg7RSHjjDeDvr7A8kobiVAd%2FqnhLENP&X-Amz-Signature=87856fcfc7b504926bd9065a523b2aaa5ac33ea9c38fee5db175c66e2e752b59&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

[image](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/34636188-9e0d-4a25-a550-06c85dcfaebc/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TTSPAWJD%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T231957Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCSY5CDsmpxzyuy%2BeSuTS2a5CTJzQv8uSFw%2FbnilB12ggIgXB4jLzwkhpsUyuyRqT2rR8xL%2BN1CBiDd9hOUPb5X01oqiAQIxv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDK8%2FVdYFU0vmdMeL2ircA%2F1mYY6xdyIF%2F1jzcNjMkEA8KnGnjTt9qdn%2FH3Hx5KGkBqRoLpDscW77sTxLr0qI2Fj3AAlgoGSXHtgpBK0Aerh1EXZhqWLbZFcz84gDBm5FrjKXmv6gIc0eDvF4ZwYkcbPy9kuKqQDLDPv4oThoHyKJIV3EGGg3S2UxUFCsUIhi80vYSXvJJte50xlW4%2F6qPyZVQ%2Bavtbyu4O%2BfRljGR8UZkSEOKCTtPLEM8rnUzCxY9A5EB87u0l0s4DimrTts5LVxqN%2BsOgOvBRgguqipqi5ADXDCtqOMu%2BphxHVez8BGh8PuE5ITYIYD2bOUk2s4MaRzH15wx%2FQVeFKWJ26Rolo%2BzvjLbUyIYQZ4kR1tyd9s4lNQ7CrWhH8hLtOwcU42hrKUTHLEc7BTUVjVRUKKFbEZiKkd9UE5IXmIQYKXf5%2F6260Kh31bGc1EHQMYfRHT04CN4AU4up9IJkG6I2CKbVHxkWV8GwtqrzjVH4%2F12DvQNZvjWYqcbMus4HsKIGXBCgb%2F2TWzP%2Bf3e5Kwdu4r%2F%2Fli2MjkdwS7K0mqcQJoc4R6aaekptPAUVnSY6FOcR7n2XBoy3XGGjS7Q4GvvIuJkRkNSr%2Fd2FJKf1e%2BQVCfwHW942usW9j0eos7iDgnMN63%2F9IGOqUBVkD9c8rkeE%2B6sBJeyWyUZrrJ2yDTm%2BWgo7vN3KDnyLVrhWTZBlqlBWcdyDUsCugFtjsnjdL9FGB5HmHS1ubfVLunZWSkSRxceFrK%2FbzfiT%2FPQpUueisWQ4oqJC5dX6AzbgOlHLlbVCdbYKP1ym%2FZ6IaY4zbXZGLVv7deg2qcSaNqHb509QbkaooYD4P4Yvg7RSHjjDeDvr7A8kobiVAd%2FqnhLENP&X-Amz-Signature=abfd0ef52859e299c616fe225a0080e9ab405f7c1b784a1b5fbf8a16237257e0&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

同学们大家好，这一节我们来学习 spinput 价格设计之外部配置。说到外部配置，大家可能会感觉到配置是相对比较简单的，跟我们前面介绍的启动器STARTER、智能装配 autoconfiguration 以及 aguator 比较起来没那么高大上。其实整个 spring 生态对外部配置的设计是很用心的，如果我们能深入理解这些配置的实现原理，对我们后续的系统设计会有很大的帮助。


这里我们还是通过三方面给大家介绍。首先介绍灵活的 spring 铺的外部配置，其次是我们外部配置的工作原理，最后进行外部配置的使用实现。我们先来看一下我们灵活的 string boot 外部配置，为什么说 spring boot 它比较灵活，因为 spring boot 允许多种方式扩展应用程序的配置，以便我们可以在不同的环境中使用相同的应用程式代码。这里是指我们比如说我们的开发环境、 DEV 环境和我们的测试环境，还有我们的线上环境。我们因为是同一套代码，因为不同的数据库链接，不同的 Redis 配置等等，这些配置是不一样的。所以说我们要支持各种方式的配置。这里它是可以用属性文件、 YML 文件以及环境变量、命令行参数等多种的配置方式来影响我们的程序配置。它还可以通过艾特 Y6 的注解方式，把我们的配置值注解到我们程序的变属性里面。同时 spring boot 也提供了一个非常棒的注解，也就是 at configuration property，这个属于注解，它能把具有一定规则的配置映射到一个结构化的 bin 上。这里的结构化主要是指配置的 k 与 b 的属性名称要能对应上。同时因为这么多复杂的配置， string 不得为特定的属性配置源设定了一个顺序，这个顺序它设计允许按优先级对默认值进行覆盖。属性配置源的这些顺序我们待会看一下。


这个顺序设计是非常有哲学原则的，我们看一下这些优先级顺序。这是 spring boot 对各种配置数据源的优先级排序，一共涉及到 17 项。这个数据来源于官网，我们解释一下这个配置它的意义是什么。首先我们看这里面的 1- 3，它里面的数据内容我们看都是跟我们测试相关的数据，在这里面 spring boot 它定义为跟测试相关的这些配置数源，它的测试顺序是最高的，也就是排一二三，分别对应 d v two 和 test property source 以及我们的 string 部的test。


我们想一下为什么测试的优先级排序最高，因为我们在测试环境下都需要对我们的环境做一些特殊的配置，去覆盖我们默认的这些配置。比如说我们涉及到的数据源，我们 Redis 的一些链接配置，或者说是我们其他的一些本地化变量等等，所以说它的优先级是相对最高。另一点就是我们的线上环境，因为它不涉及到测试的配置，所以说如果抛开测试环境，那么我们认为优先级最高的是什么呢？也就是我们的命令行参数了，命令行参数以及这启动过程中我们的脚本上配置的这些参数。
对于 stream boot 来说，它可能涉及到两项，一是纯粹的命令行参数，另一个就是我们称之为 stream application JSON，这个 JSON 它是配置一个环境变量，这个变量里面可以通过 JSON 格式去定义一些参数，我们也可以理解为一个启动参数。


后面也就是我们公共配置相关的一些项，这里面我们可以看到它有 serverless configure， serverless context 还有JNDA，当然我们现在使用的非常少了，以及我们可以从 Java 系统获取到的 system 对应的一些property，以及我们操作系统的一些环境变量，所以说这些公共配置顺序它低于我们命令行的输入，也低于车次。


我们在这就做深入讨，我们看第二页里面，这里面有个比较特殊的随机数，这个随机数相对来说它排的顺序还是比较高的，它是默认的高于我们这些常规的一些配置。我们想一下为什么这些随机 value 值要高于我们常规外部配置？我们这样想一个问题，我们为什么需要随机数呢？需要随机数的情况是大多是我们的常规配置满足不了，所以说基于这个原则，我们涉及到随机配置的话，它的优先级要高于我们的常规配置。


这里面我们再看常规配置里面，它涉及到四项内容，这里面分别是对应的我们的profile，对应的application，我们看这里面有 application 对应的 profile property， application profile property 这个属性文件，它可以打到我们的栅包里面，也可以放到我们栅包的配置文件外。但从这里面看，这里面写到的内容是排序更高的是 outside over your package strong，也就是说放在我们炸包之外的优先级要高于放在我们炸包之内的。同时涉及到 profile 的优先级要高于没有 profile 的。


我们知道这样一个原则，那么最后的也就是我们的 16 和 17 项，也就是说这是我们的一些默认配置，它的顺序是最低的，这个顺序大家也不需要死记硬背，通过理解这个设计原理的角度去考虑，其实总结下来就这几点，首先测次相关的配置优先级最高。第二启动参数和命令行的这些参数，正式环境下优先级是最高的。第三是应用公共系统的配置优先级低于命令行参数的优先级。另外随机配置项的顺序高于常规的配置项。常规的配置项里面涉及到两点，第一是有 profile 的配置高于没有 profile 的。


第二就是打入炸包的配置优先级低于炸包外面的最后一项，程序代码配置的默认属性优先级是最低的。我们现在对于整个配置数据源的优先级顺序理解应该是可以。接下来我们基于源代码去看一下外部配置工作的原理理解，外部配置源的抽象 property source 及几个重要的具体实现。另外通过源码分析 property source 这子类是如何构建优先级顺序的？好，我们先看一下 properties source。 property source 它作为一个抽象类，它下面有一个可枚举的 property source，我们这些具体的一些配置源都是实现了可枚举的 public source。从这里面我们可以看到我们这是命令行的 public source，这个是基于 spring application JSON 的 property source。我们还能从这里面看到这是 thrilled configure 的配置属性，这是 thrilled contact 的配置属性。


我们看一下这个可枚举的 probe source，它的结构大概是这样，其实它相对于 property source 扩展了一个方法，我们可以理解为 get property name，这个比较容易理解，我们可以就理解为就相当于是 map 盖的case，就是我们获取到所有的key，这是我们可枚举的 property source，对应的我们的 property names。


好，我们看下一个几个具体的 property source，它的顺序是如何构建的，从这里面我们可以看到这里面去判断一下我们的 debug properties 是否为空，它不为 not 并且不为空，这样的话我们会构建一个 map proty source，也就是命名为 debug 的property。我们构建完这个 property source 以后，把它放到整个 source 队列的队尾，也就是 add the last，这是我们的默认的配置实现。


那么我们看一下我们命令行的properly，从后面接着看，我们可以从这里面看到我们的 add command line properties，也就是说我们的命令行参数，命令行参数怎么处理？这里面对于命数领行参数的要求是，首先判断是支持把命令行参数配置到我们的上下文环境的，并且参数的宿主长度应该大于0，也就是存在参数，这样的话我们就会做一些操作。


首先去判断一下在当前的 source 列表里面是否存在着这样一个命令行参数的一个k，如果存在以这个命令行参数属性 name 作为 k 的对象的话，那么我们把它取出来重新做一次包装，并且把我们新的参数传入进去，对我们现在 source 里面的内容做一个替换。


如果说在这里面是不存在的话，我们就直接新建，我们这里面可以看到是 add fast 是把整个 simple command line property source 作为列表里面的第一行记录，这是我们可以看到对应的一个是排名比较靠前的我们的命令行参数，也就是启动参数，另一个排到最后的我们的默认配置。


接下来我们先来看另一个配置，从这里我们可以看到这是一个 add Jason property source，这个方法是它是怎么执行的？它是在通过一个叫 Supreme application json environment post process。我们看到 post process 的话，我们应该知道 spring 核心容器里面它有 bin 的 post process，也有 bin factor post process。其实 spring boot 它又定义了另一个 post process，也就是针对于我们的初始化环境的 post process，它的执行时间点4。


当我们的环境初始化完成以后，再做一个后处理，从这里面我们可以看到什么呢？我们的 JSON 配置相关操作，它这里面首先我们 find proxy source 这里面获取获取到一个name，这个 name 怎么获取到的？我们看这个方法，这里面它其实是获取到跟 Server net 相关的一些环境上下文信息。我们获取到 series 对应的 find fast，也就是说 Server 的这里面涉及到 Server 来的 configure 和 Server 来的context，这两个里面排名比较靠前的一个对象取出来，取出来以后在这里面去做判断。


如果说这个上下文，也就是 source 里面包含这么一个对象，那么我就把它放到这个对象之前，也就是放到我们的 series 的 configure 之前。如果说不包含的话，我就把当前这个对象添加到我们的最首位，这是我们对于外部配置的一些顺序的一些解析。


接下来 Caps 我们外部配置操作实践主要做两件事情，第一个我们使用 configuration property 制定一个配置 bin 的实现，并且它可以像我们 spring boot 里面默认配置一样，在 YML 里面去配置的时候支持自动提示。第二个就是说我们验证一下命令行参数与常规配子参数之间顺序的关系，其实这个结论我们刚才通过看源码的方式可以理解，它的顺序关系确实是这样的，但我们可以基于一些命令行的方式去验证一下。


首先我们去看一下我们的配置，这里面我们看到一个我们的 configure 模块，也就是为我们这次配置操作键所用的这个工程，我们还是先冲我们的 palm 文件可以去了解一下这个工程，这里面它跟我们前面的工程很相似，也就是说它是没有什么特殊的变化，就是依赖了我们正常的starter。这里面唯一的区别是它引入了我们的 showcase tools，这样一个也是我们对应模块儿的一个实现包。我们待会儿会去看它里面做了哪些事情。


我们现在再看一下我们的启动类，这里面的启动类里面它的操作是我们可以看到正常的 SL four 减去记录日志用的我们的 spring boot application，这是启动用的，这里面我们看到我们使用了一个 enable configuration properties，就是开启一个我们自定义的一个配置属性，那么这个配置属性 showcase TOOLS property，我们可以看到它并不是 spring 官方提供的，它是我们为课程实践而去创建的一个对应的属性配置对象。


基于它我们在这里面用到 long book，它这里面就是指可以减少我们实现 get set 的插入，这里面它用到 configuration property，在这里面我们指定的前缀是 showcase tools，这个命名刚好跟我们的工程是能对应上的，我们的工程是TOOLS，嗯，模块名称是 showcase TOOLS，所以说我们在这里面配置完成以后对它进行打包，打包完成以后我们在这里面引入。


引入完以后我们可以通过我们 application yml 里面去配置它，我们可以看到这里面有 showcase tools， ID name， states describration，跟我们这里面这些属性能一一对应上，那么我们看通过这样的话，也就是我们自定义了一个 configuration 的property，那么基于它我们可以在这里面去做一些配置实现。


这里面我对应一个是我们普通的 application YML，这里面还基于一个 application 杠，第一个也就是说支持 profile 的一个YML，我们基于这种方式可以去验证我们的属性优先级，有 profile 的是可以高于 application 的，我们可以在这里面体验一下，目前它已经支持我们的自动提示了，比如我们在这里面去选我们的dispreson，在里面可以演示，我们可以跟它命名为我们可以这样。


这是一个 DEV 环境下的，我们的描述可以看到它的自动提示，那么我们想一下自动提示是怎么实现的？其实这个自动提示比较简单，比较简单的原因是因为 stream boot 跟我们定义了好的规范，我们只要照着它的规范去操作就可以。现在我们看一下我们的 tools 这个工程，在这个 tools 工程里面我们首先是定义一个我们的bin，这个 bin 它里面只是描述出我们的 get 晒的方法就可以。在这个方法里面我们加上 add configuration property 这样一个注解，在这个注解我们指定一个前缀，我们这里面参考这个模块名称，我们前缀是showcase。点 tools 完成这个操作以后，也就是说这个 property 的必应已经定义好了。


定义好完成以后，我们需要对 tools 打包儿，我们正常情况下打包儿，它其实就是直接打出一个压缩包儿，这个打完包儿以后放进去，它是不能做到自动提示的。如果说需要自动提示，我们需要在 palm 里面引入一个依赖，这个依赖就是 spring boot configuration process，这个依赖它主要作用是整个这个过程，在编译打包的过程中，它根据这个 properties 生成对应的Metadates，这些 metadata 元数据在集成到栅包里面 idea 去引入。


识别完以后，它可以通过 Meta date 进行一些原生提示，我们可以从这里面看到我在编译打包的过程中生成的metadata，其实我们可以看到这里面是对应的是我们的men，下面是 come a mock 对应的这个包，我们这个是resource，里面是没什么内容的。这个 Meta info 它是在打包过程中自动生成的，我们看一下它的内容，从这里面我们可以看到它 name sowcase tools 是不是非常面熟，而且它的类型就是我们的 socase tools。


property 跟我们这里面是能对应上的，这是group，我们看一下properties，也就是属性，它支持哪些属性，它这些属性在这里面都有体现。我们首先 showcase 里的tools，这是描述我们的 ID name 和我们的状态，从这里面可以看到这些元数据，把我们需要配置的这些属性的能一一对应，所以说 idea 基于这些原始数据可以给我们做到一些自动提示。现在我们回到这里面去看一下，当我们如何让它生效，我们对它生效还需要开启一下 enable configuration properties，必须用这种方式引入它，才可以在这里面注入到我们并容前面一个 socase tools properties，这样一个bin，我们可以通过自动注入的方式把这对象获取到。


现在我们可以去执行一下，看一下它的效果，我们可以看到这里面我们打印出来这个 property 的内容，这里面我们看到 showcase to the property ID 是 debug ID，这里面它都是 debug 的效果， debug 的内容就是我们这个文件的配置，因为我们这里面并没有配置相关的 profile 信息或其他的一些命令行的一些注入，所以说我们可以看到是默认的这些信息。这是我们通过正常运行的方式获取到的效果，也就是说它只获取到了我们 application Yml 里面的数据。


我们看一下单元测试的效果，在单元测试里面，这里面我们看到这里面我通过声明激活了 profile dev，同时通过 test profile source 配置了我们的 showcase TOOLS ID，这里面标明是 test proty source，也就是这个注解去对应生成的。这里面我还通过 string put 的 test 构建了相同的这个k，用来说明它是 string put 的 test 构建的，基于这种方式去执行的话，我们看一下它得到的结果是怎样的。好，很快执行完成。我们看一眼结果。


首先 property ID，它是获取了我们的 test property source，这说明什么呢？说明这两个的优先级，在 test 的环境去争取的话， test 的 property source 它的优先级会更高一些。我们看 name 呢，它已经不是 debug 的 name 了，它现在是 dev name。 dev name 的原因是什么呢？因为这里面我们在 application DEV，也就是对应的我们支持 profile 的环境下面，它是有配置的，所以说它优先选 DEV 环境，而覆盖了我们的默认环境，覆盖我们的 debug name。


所以说这里面我们看到，同时我们看DSC，我们的描述也是 d visits create，因为道理是一样的，它跟 name 一样，也就是说对应的 profile 文件覆盖了我们的默认文件。我们的 states 因为没有在其他地方做配置，所以说我们追逐公司取我们底票的 states 的效果。


这里面我们可以看到通过 run 我们正常的启动类和我们单元测试类去能区分出，我们可以证明基于 profile 的优先级要比我们默认的要高一些。那接下来我们去验证一下基于命令行的操作，因为我们在 idea 的操作相对比较空间比较小一些，我在这里面通过 item 去操作一下。首先我们去执行一下正式的效果，我们基于 Mavins reboot 直接运行，我们看一下它输出的内容，我们看这里面的结果，我们可以看到它的 ID defield name， defield 它都是默认的效果。


好，那么我们去重新整理一下，我们通过命令行参数去传入一些，我们可以看到这是我原来执行过的命令，从这里面它是其实我们可以首先加说打出一个栅包去执行，但是我们为了减少这个打栅包的步骤，我们直接通过 spring 步的插件去执行 spring 步的插件它传参数的方式是这样，首先杠d，我们指定 spring 杠 boot 点 run JAM argument。也就是说我们通过这种方式去传递一些 JAM 的参数，那么参数的内容也是杠d，我们需要指定一下，我们这里面看我们是指定了 showcase TOOLS name name，它命名为 command line name，也就是说我们通过命令行传的这个名称，并且我们把 profile 把 dev 的 profile 激活起来。好，我们这样执行，看一下效果。
通过这里面我们看到结果是这样的，从这里日志里面我们能看到当前我们初始化的 profile 已经激活了 dev 这个profile，下面我们看它输出的结果，因为我们激活了 Dev 这个结果默认我们像ID，它已经成为 dev ID，这里面的其他的也都是以 DEV 前缀的。


当然因为在 DEV 环境下并没有配置states，所以说它取的是默认的提票的states，这里面 name 我们取到了，是我们的命令行参数传的 command line name，从这里面可以看到我们从命令行输入的参数的优先级要大于我们的配置的效果，我们顺序的验证就先验证到这里。回到 PPT 的内容，到这里 spring boot 架构设计解析的视频内容就结束了，这一章节开始涉及到源码的内容，大家学习起来会更辛苦，在这里谢谢大家，我们下一章节再见。


