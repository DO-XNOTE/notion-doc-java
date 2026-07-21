---
title: 2-3 Spring Data REST核心源码解析（2338）
---

# 2-3 Spring Data REST核心源码解析（2338）

同学们大家好，这一章节我们来介绍一下 spring day 的 RESET 核心源码解析，那么我们讲解的内容呢？首先来看一下 spring day 的 RESET 一些源码介绍，我们会通过 get help 的页面去介绍一下 screen date RESET 具有哪些功能。第二我们是来介绍 screen date reset 一些核心API，这里面也就是说我们完成 screen date RESET 这个功能需要哪些比较直接我们关心的一些类和接口。


最后就是我们要是去通过源码去了解 string data reset 它的一些执行流程，这里面执行流程我们通常会包含我们的初始化流程和我们的运行执行的流程。好，我们首先来看一下 spring data reset 的源码介绍，对于 spring data reset，它的源码是主要自 spring data reset 这样一个 GID 子，那么它对应的版本是跟 spring date 整体绑定的，我们这里面也是对应的 4. 2，那么对于它下面的模块儿是其实有四个模块儿，我们比较关心的是三个模块儿，分别是 spring day 的 RESET core、 spring date reset web IMC。 5. 2.


第三个是我们的 spring did reset SL explore，它是一个 Web UI 工程，可以把我们上面 spring day 的 reside Web IMC 相关暴露的这些 request Mapping，通过这种方式展示出来，可以完成我们相应的这些正餐改查以及分页的一些查询。


看一下 spring date reset 这个源码在 get helped 情况，从这里面我们可以看到它现在像这些 water 和 star 和 fork 数，其实跟 spring boot 和 spring framework 是没办法比的，它现在是 stored 700 多个，其实还没有上千。


接下来我们来看一下它的功能模块的一些情况，在这里面我们可以看到它的更新函子比较频繁的，现在注意近似 8 天有更新。这里面我们看一下这里面有 spring day 的 reset core did， reset m a C 以及 spring 对的 reset SL extra。这是我三个自我们介绍的。同时这里面是distribution，是进行我们发版时要用到的一个模块的一些配置。这里面 string 对的 RESET touch 的话，大家可以看一下，它不是我们可以直接使用的一个功能模块，我们可以参考去学习一下它的一些单元测试的方法。这里面可以看到其实它发布非常频繁，已经 190 多支发布，同时用户量也还是挺广的。


底下我们看一下对于 spring day 的 RESET 的介绍。这是一个对于 spring day 的RESET，它跟 spring day 的 common 其实是类似，都是一个公共的模块，它主要的目标是对我们的工程提供一个固定可配置的一些前端的 UI 工程，可以通过 HTP 的方式暴露出我们这些接口。


其次， spring day 的 reset 跟 spring day 的 j p a 结合起来是最合适的。对于这里面我们看它实现了哪些功能。首先它通过暴露出我们 rest API 去实现我们的这些正态改的操作。我们同时有一个 a C l 的这样一个 media type，也就是通过 SAL 这种类型的方式暴露出来，去进行一些展示，同时把我们的这些接露出各种类型。比如像 Python 集合 item 就是我们指定的一个类型，比如说我们 get by ID，我们获取到一项就是 item 以及一些组合的一个resource，可以展现出我们的一个类型。另外它还支持分页或者是分页的一些link，也就是 link 这里面会包含比如说我们上一页的下一页以及第一页最后一页，这是我们跟分页导航相关的一些link。


另外它可以支持我们通过动态的方式去过滤我们集合的这些资源信息，也就是说我得到一个claxen，我需要把某一些，比如说没有权限的，我们可以把它过滤掉，我们可以用这种方案的自定义去扩展。同时这里面还支持我们对于查询的一些自定义的，比如说我们的 name 的 query 得到的一些信息也可以进行映射，这里面就是我们在 report 里面写的，比如说我们是 find by name，那么 find by name 也可以我们通过映射的方式映射出来我们这个查询的语句，同时它还支持一些，我们可以看到这里面 hook 就是 hook 我们这些 reset request 的相关内操作，这里面其实就是我们对于 rust 操作，比如说我们的蒸餐凯闸都会有对应的一些时间监听，我们监听会创建对应的event，我们去监听这个 event 你来实现我们对于这个超出的hook。


其实我们现在主要还是使用的 json 的格式，并且我们允许一些特殊的一些定义，也就是说对我们整个对象的进行减资。怎么理解？比如说我们用户会涉及到用户名、密码或者一些个人信息的描述，当然我们把用户对象暴露出来以后，对于密码这一项我们应该去掉，所以说这是对于我们的一些属性的减资，同时我们这里面提供了这个 SL explore 去简化我们对于我们的服务的一些测试演示，也好就是给我们提供了这样一个工具性的一个 UI 系统，同时它目前是已经支持像ZPA，MongoDB、AU、four、企业、 solar 和 concern 这么多一些数据库的存储系统。同时当然这里面也去包括我们自定义的对于这些资源的暴露的一信息。好，这就是我们可以看到对于 string 对 reset 提供这些功能都还是特别实用的，其实我们可以几乎做到配置完成以后很少的代码能完成我们整个系统的一些增删改查，其实这样还是蛮有吸引力的。
这里面有一个比较快速的一个开始的一个文字的一上，我们看我们可以这里面通常我们在实现对应的 spring date 的时候，我们会是配置对应的reporter，那个 reporture 我们可以继承对应的 CID reporter，或者说 pacing and sorting 的一个reporture。当然我们使用 spend GPT 的话，我们通常会记成GPT。这里面标明了一下，我们这里面是 repository 的 rest resource，我们指定了它的路径是people。那么对于我们默认的，我们知道我们默认如果不指定的话，它应该是对应的 passion 才对应的复数，我们应该是Pythons，所以这里面指定了一些people。同时我们可以看到它会有一些查询的操作。我指定一些特殊的路径，比如像 find by first name like，它可以把这个路径改一下，比如说 rest resource，它会对应的是 by fast name 这样一种操作。那么对于我们在配置的过程中，这里面我们可以看到它用的是 Mongo 的一个实现，这里面我们可以通过对应的是，嗯 car 我们的 LT local house 的 8080 people 色子，我们看下色子后面的这个 UL 也是 by fast name，它跟我们这里面定义的我们的 pass 路径，也就是 by pass name 对应上，也就是说它会执行这样一个方法。


通过这样我们可以知道，对于我们通过 repository 定义的这些接口的实现，可以我们通过 spring 对 recheck 一个映射关系，能可以直接映射到它的一些读写的一些操作。好，那么我们现在回到PPT，这是我们对于 spring data RESET 源码的一个简单的一个概述。接下来我们看一下 spring data reset 相关的一些核心的API。
那么对于 screen day 的reset，我们首先要知道它可以理解为是我们的一个 Web Mac 的一个工程。首先它是可以暴露一些Controller，对于我们这里面的Controller，它定义了两种注解，一个是 basepause aware Controller，另一个是 repositer reside Controller。那么对于这两个注解有什么特殊的功能，我们不用考虑，我们就理解为它是一个普通的一个 country 就行，那么它可以去映射到我们 spring data 对应的一个report，一个信息。


对于这个 Controller spin 对 reset MVC 默认实现了几个Controller，这里面的 Controller 它都是继承了 abstract repository reset Controller，那么这里面分别是 report Controller 和 repository INTI Controller 以及 REPORTER search control，还有 report property reference control 这几个 control 它分别作用是什么？对于 REPORTS control，这里面可以暴露我们整个工程相关的 reports 的一信息，类似于一些 profile 的一些相关的信息。对于 report entity 这个看出来是最重要的，其实它实现了我们对于 report 默认的这些增删改查的功能。这里面会涉及到我们通过 get 我们获取到列表后指定的某一个对象，我们通过 put 去进行对象的修改，通过 post 来进行我们的一个对象的创建，以及我们通过 delete 去删除一个对象，这里面通过 rush 的形式主要是在这里面进行一个体现。


那么对于 report 色子control，它主要是一些查询相关的一些操作，我们通过签名字义，其实我们对开发过程中查询功能非常重要，包括我们的命名查询，或者我们通过 at query 注解的方式等等。这种方式的查询都会通过 repose search 的方式，我们相当于是透传透暴露出来，从我们这样一个接口，那么下面我们可以看到这个更比较复杂。


四是 properties reference，这个就相对来说比较复杂一些，就是说我们查询一个对象，它具体的一个属性信息的方式，也就是我们的一个属性的一个引用信息的方式，可以通过它来去查找，通常这种方式会比较少一些，比如说我们首先会查一个用户，那么我们更关心这个用户他的比如说家乡例子，那么家乡例子是个对象。
那么我们可以通过user，比如说address，后面就去进行一些状的查询，后面是 prepresentation model，这是什么意思？其实我们暴露出来的这些对象，它其实需要序列化为 json 的，那么这里面在序列化json，我们通过什么样的一个对象包装我们这个模型？这里面就是我们的一个可表现的一个模型对象，那么对于这个模型对象，它里面有很多子类，其中我这里面列出来几个比较典型的，我们可以看到这里面是 class model，对于 cracked models，它还有一些子类似配子的model，也就是说我们可以支持分页的。当然 cracks 我们知道它是一个列表的集合，下面还会涉及到一些 reports search resource，其实我们这个 model 最终它会映射到一个对应的 resource 资源，这里面一个对于我们 repost search 相关的一些信息，同时像我们可以有一个 entity model 以及我们 reports link。对于 resource 这是什么意思？其实我们尤其是分页信息，它会有一些额外的一个 link 信息，比如说我们指向self，也就是。


指向我们当前这个对象的一个URL，或者如果说涉及到上一页的下一页，它会比如说。
有Pre，或者是我们想好 lost 这样一些各种不同的一些URL，这是几个？我们接着看，这里面的是 reposing event，刚才我们在 Git Hub 的页面去跟大家介绍的就是其实我们进行增删改查的操作，会有一些hook，也就是一个钩子操作，就是我们通过一些自见监听先听的自见，它都是继承于 reposure event，它里面会包括比如说 before save before Creator，涉及到 off 的 save off 的 Creator 相关的一些event。待会我们可以通过源码里面去看一下。接下来我们。


看一下是跟configuration，也就是跟配子相关的几个类，这里面会涉及到reporter， reset MVC configuration，这里面是 reset control configuration，对于 reports reset MVC，它其实就是本身我们是作为一个 MVC 工程，它实现了对 spring m a C 功能一些扩展，那么这里面肯定会有一些特殊的配置。


另外对于 RESET Controller configuring 这个就比较简单了，它其实就是把我们刚才介绍的 4 个 Controller 进行一些组装，把这个 Controller 进行并化。当然这里面跟 m a C 相关的两个对象，我们可以看到这里面会有一个 handler Mapping 和 handle Adapter。大家看到这两个对象会比较熟悉一些，因为我们在讲 spam v seed 时候，多次强调 handle Mapping 和 handle adapt 的重要性。其实对于spring，我们这里面 spring date rest，它里面的 Web v seed 实现其实也是扩展了 handler Mapping 和 Handler Adapter，它扩展的内容就是我们这里面是 reports reset handle Mapping，其实我们可以看也比较容易理解， repository 代表我们对应的资源库reset，我们通过 reset 协议的方式把我们的信息暴露出来。这里面对应的 handle Adapter 也是 reports reset handle Adapter，同时我们的 spring date retract 它也集成到 spring boot 里面了。
其实如果说我们使用 spring boot 工程的话，我们可以直接引入相关的一些starter，其实这里面会有对应的 auto configuration，我们涉及到STARTER，通常我们会联想到这个STARTER，它的一些制动装备的信息在哪里？这里面是对应的是 reports reset MVC auto configuration，大家可以去看一下这个源码，去看一下它怎么组装的，同时还会涉及到一个叫 spring date Web auto configuration，也就是说跟我们 spring date reset 相关的start，它里面涉及到两个自动装配的类，待会我们一块去带大家去看一下。


好，我们现在来切换到我们的源码里面，那里面我们首先还是看我们的 palm 文件里面的一些依赖配置，那么在这里面我们可以看到它的 part 也是 spring date part，其实就是说我们，嗯，说明 spring date reset，它也是 spring date 的一部分，也就是遵循那 spring date 构造的一些规范。


后面的就是它定义的这几个模块，我们 spend reset，call， split reset m a C 这里面是 distribution 和 SA 的explore，那么我们首先来看一下我们的 screen date，reset，call，看这里面有哪些内容好。


这里面我们可以展开去看一下，好像代码量不是很大，但其实也还是蛮丰富的，这里面会有一些注解，这些注解我们可以打开看一下，是 handler off 的create，它是什么意思？我们可以理解为它其实对于一个监听的一个注解，也就是说当我们在配置这个注解的时候，我们会监听我们的对象创建后要做的一些操作。这里面还涉及到 up 的 DELETE 以及 up 的save，当然还有 create before data 刚才我们提到的这些超出的hook，且起基于这个注解来去监听我们的一些事件，那么这里面我们可以跟这些注解相对应的，也就是这里面的一些英文的操作。


我们可以看到这个 event 是 after create event，其实这个四件定义的比较简单，这里面其实它只是继承了我们的 repost event，把它一个 source 传递过去就完成了。那么其实我们这里面的 repost event 也实现的功能比较单一，其实只是它继承了我们的 application event。


通过这里面看，其实我们这个 event 我们可以理解为它只是一个四件类型的一个标记，它里面并没有传入什么特殊的一些信息。所以对于这个 event 我们的四点监听的话，大家可以比较好的一些理解一下。对于这些 configure 里面有一些 configuration 相关的一些操作， configure 里面主要是一些配置类的信息，我们可以看到是这里面对于 Meta date configure 相关的一些信息，这里面对于我们存储了一些schema，format， partner 等等。嗯，这里面还有一些对应的一些 get set 相关的一些操作。
好，我们可以再看一下 report reset configuration，这里面的内容还是比较多的，我们可以看一下这里面的私有属性会非常多一些，我们看到这里面会涉及到一些我们查询的配置和我们的分页相关的一些信息的一些标志，也就是 Permeter 的名称。这些信息我们都可以自己去覆盖默认的配置，自定义一些配置的信息，我们接着向后去看一下，这里面还会涉及到我们的一些 Mapping 相关的一些映射的信息。


好，这个我们就不先展开一个介绍了，我们再去介绍我们初始化和执行流程的过程中，对于涉及到一些类，我们可以通过 debug 的方式去进行跟踪。好，这里面会 project teams 以及我们的一些支持性的一些类。好，这是我们可以简单说是我们 spin data reset core 里面的内容，其实 core 更相当于是做一些底层技术的实现。我们可以看一下 slow rise 的 Web Mac，这里面会有我们更多关注的一些内容。


其实在这里面我们关注比较多的就是我们刚才提到的是 repository entity Controller，那么对于这个方法就是这个control，那么这个 control 其实可以理解为我们请求的一个入口，当然我们请求更外层的入口是 departure light，因为它属于 stream AC 的一部分。对于这个 Controller 它也会通过 Dispatch THREAD 引入进来。


我们到我们 entity Controller 的过程，我们可以看到对于这个 entity Controller，它里面涉及到的一些方法，我们可以从这里面简单去看一下。我们看 get collect resource，也就是我们可以理解为是一个列表查询，这里面我们再看一下对应的我们指定的蒸 3 凯达的一些方法，这里面比如说 pose 操作，那么 pose 操作我们理解为它是一个创建的一个操作，但下面我们还可以看到这里面是option，也就获取我们当前的一些预览的一些信息就是当然 Opson 它的请求是比较特殊的，它不会获取真正的实体对象，它只是获取一些类似于描述的信息。对于这里面我们可以看到这是head，跟 option 其实有些类似。这里面是我们的 get 获取到指定的一个对象，所以这里面是put， put 是对应一个修改的操作，我们可以简单地去了解一下它里面的内容。


我们这里面还涉及到了几个其他的control，这里面是repose，reproperty， refind 就是对应的一些属性的扩展的一些信息，还会涉及到我们的一个色次，也就是我们跟查询相关的一个controller，这是我们 report 色次 control 的。其实这些 control 它都是继承了，我们这里面是 abstract reposit control，我们可以通过 command s，我们可以看一下它的一个树结构，我们通过 Ctrl s 可以看一下这样一个引用的关系。这里面是 object REPORTS RESET control，下面是它几个子类，我们简单了解好。
对于这里面我们可以看另一个这样的工程，就是我们的 spring date reset SL explore，也就是我们的一个 UI 工程。我们这个工程实现的功能比较简洁，它这里面是定义的是 SL explore，它对应的 URL 我们的一些信息，这里面还有对应 XL 一个它的一些自动装配，也就是我们构造一个 XR explore 的这样一个bin，这个 bin 其实就是 XL 的一个explore，其实我们可以理解为它就是对应的一个 control 操作。其实我们可以看到它的 Java 代码比较少，其实更多的是它是什么，它实现 Web u i，它会有一些 GS CS 资源上的一些依赖，这些依赖它是通过我们这里面现在定义一种方式，是对于 Web 账号的方式去实现的，我们可以去了解一下。


对于前端也感兴趣的，我们可以从这里去搜一下是 Web doc，我们可以看到这里面。从 Web 召 SL explore，其实我们可以理解这是我们的一个前端工程，在这个前端工程里面它的内容会更多一些，这里面会有我们的我们可以看到它的一些前端的资源信息，这里面有 GSCS 相关或者一些涉及到字体相关的一些内容。我们对于整个我们代码的框架，我们先简单介绍到这里。好，接下来我们来去看一下 string data reset 它的一些初始化的流程。其实我们使用 string data resize 的，我们也还会基于 string goes 的方式去使用，所以说我们最关心的还是 spring date reset 相关的这些 auto configuration。可以切到源码里面看一下这个 reports reset。


Mac 的 auto configuration，这是我们的 reports side m a C Autocom q，我们可以看到它这个类是在我们的 spring boot 的模块下面，在这里面我们看这里面最重要的也就是它 import 操作，这个 import 操作它引入了 report resize MVC configuration，我们可以在这里面看到这个是比较复杂的，对于这个 reposure reset i m a C configuration，它是我们这里面的是 string date reset map VC 下面的一个 configure 的一些操作信息，我们可以看到它其实它又间接地引入了 rest Controller import select，这里面是 Sprint date Jackson complicated，我们可以看到它是对应的一个 rest control 的一个引入。我们接着继续跟进去看一下，对于这个 reset control import selector，它是实现了 input selector，那么对于 input selector，我们看它引入了哪些对象，在这里面我们看一下 configure 信息，首先这里面是 add reset control configuration，我们点开这个看一下，那么看到它的话我们就开始恍然大悟。


我们可以看到这个下面里面的信息都是我们对应的 Controller 相关的内容，这里面是 repository Controller，我们这里面的是 report entity Controller，我们可以看到对应它里面的这些 Controller 信息，也就是我们比较关心的 Sprint rest 相关的几个country，也就是说这几个 control 是通过这种方式在这里面构建 bin 引入进来的。
好，这是我们的 rest control，我们退回再退到这里面。我们看另一个是 Sprint Jackson configure，这个其实就比较简单了，它这里面的 Jackson 使用的是 ZEO 的model，把这个 b 实例化了一下，并没有其他的一些操作。
那么对于这里面我们还有哪些插入？对于 repository set Mac configuration，其实它这里面还实现了，我们看到这里面是列出来的，首先是我们的 rest Controller import select，这我们看了它里面引入了我们比较重要的跟 repository 相关的，也看出来，还有这里面 slented Jackson。


另外一个这里面是 report rest handle 的mapping，其实我们比较关心的也就是我们的 handler Mapping 信息的占领于注入的，这里面还有一个叫 basepods aware handle Mapping，其实这个 base pot where handle Mapping 是对应的 reports handle Mapping 的一个父类，那么我们先看一下 reports reset handler Mapping 它在哪里？我们可以在这里面去全局查找一下这些方法的提供，我们在这里面就去搜索 handle Mapping，好，我们可以看到这里面是有对应的，我们的是 rest handler Mapping，我们可以看到上面还会有一个是对应的一个 handler Adapter。


我们重点看一下 rest handler Mapping，那么对于这里面的 rest Handler Mapping，它并不是我们直接看到的 reports 的一个 Handler Mapping，这里面是一个叫 delegate Handler Mapping，那这个名称我们也知道，它应该是对我们 report Handler Mapping 的一个包装，那么我们来看一下它这个对象的一些构造方式。那么在这里面我们可以看到它是直接 new 一个 delegate handler Mapping，同时传入一个 Mapping 和一个 press 这样两个对象。


那我们先看一下Mapping，它是一个list，这里面我们放入了两个 Mapping 对象，一个是 base Paas Mapping，一个是 reposer handler Mapping。那么我们可以看到这里面的 reposer handler Mapping，也就是我们这里面刚才提到的 repository reset handler Mapping。因为在这里面我们构建出这个Mapping，并且把它对应的一些属性我们填充一下，这里面是 GP help，我们的 application context 对象也会把它注入进去，这里面还有一个 cost configuration，还有我们的一些模式的一些解析器等等。
这个测试完成以后，我们看它这里面手工的调了一下 up 的 property set，也就是说当我们的 report 时下的 handle Mapping 对应实现的我们这个初始化接口可以在这里面也会触发去执行。另外这一个是 base Paas aware handler Mapping，我们可以在这里面点进去看一下我们的 reports reset handle Mapping，它其实是继承了 base Paas aware handle Mapping，好和我们关闭退出。看到这里我们大概知道在这里面我们去。
Repository reset and Mac configuration.


它其实例化了这些我们关键的一些必应信息，刚才我们也看到了 rest control configuration，它实现这些 control 一些信息。这里面我们对于初始化的流程我们简单先介绍到这里。

