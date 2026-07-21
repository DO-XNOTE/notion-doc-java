---
title: 1-2 Spring数据访问架构设计解析（2854）
---

# 1-2 Spring数据访问架构设计解析（2854）

[image](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/0890dcda-ee6d-41e0-81e3-de1023e3cf55/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663I3B4OHT%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T231959Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCbTGOFFzXHlSiCR1lqN6SQkXgQK4pXiaWCN%2Fhdliu8mwIgKN3q9vlKRB00Rq67FAHlK94n6cSHOnL7G14lWgy%2BYrgqiAQIxv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDAbKJuV%2BS1zG4h7bgSrcA3NgJVvdeFMO6n1sjRW%2F9Q6OAc%2Fw8eLnPw2icq5uoJbxdAN6j3Ea0bL62RUfKrrFz13WQEs61y3K62pQ6TPqo0UNGD92xWSDPHAOeJ7rVZS42f37qgUh3WJbnghEjxX%2Frf6aHdG6Fag%2B5idaAMA26DBbEqJxjNxuTKbl05%2FBpsbTA4rQaGOs8qyfznRZtf0R6NQxEKLFx0uyGDeGZRdF2%2BhXAJRpgT1TOYpKnI1KwQG0rEaQ2EHIwjkSAHBezRYjK%2FBih%2FDlN7WbR8mjTJiQMja3M9%2BSaMCiP3nFQ2xFqz9zIcqGKKyDRHTeXsPwpUVHpDqqEEjAtyNmKjsvYg4%2FaiaWqQDI0wqd%2ByzNRA4HI4OM1OxmCG8iszXQvRtRKL3K72fswv%2FCmYrDMW%2FYW8EecDe1wpCfsW9vL090x5GvaqBXg8bGbB7DGMTBLvj7BF6KnEPAaxkZ5%2BzLk8lxKOvEjTSVdBC3emvPRjn1LeSGX8e6WYIvWJj5%2Brdsi5k8HuEgNVYMomqVVNAY4BFgMtvrKZsoqpXtiCXf6mIJ5G%2FL%2Fo%2F3jRD5kotVLcX3Zzq24NFoim2pp7eMVykDWh4p4xDEAO8QjpaG5CasOUhMh8jZjb46LzmtYAasP8dGORKHMJS3%2F9IGOqUBG8zbA97gLulUplMg6oc%2BTCjm5NCtitBxCVAxHH31%2Bx0E9hcxiW99mt7PXyYfwvUxDEWTWhm2knT8iehP8lehzsc1IgSIngVXA%2BQSgepocJVUSiyOv13S2gs7AUzUpvoNZTC%2FFq3JBa2HKgjCn7x%2BMGlh86hHmRVQq4FBfgsY4Z%2Bh93GTtwGjJdrTM4N7RKQ%2FNTAdvkvL7PeZ6hYsStBZ9ESsk6XC&X-Amz-Signature=6c8ffeeaa0e5ac2d7101efab6a645a3f71cc0b73006dba5acc2c555cddae8019&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

同学们大家好，这一章节我们来学习 spring 数据访问层架构设计解析。通用 spring 的框架的架构图可以看到，数据访问程主要包括我们跟 spring t x，也就是我们的事物和 spring DDB c， spring OM 这一类的一些模块儿。那么从 spring 五点儿 3 开始，新加入一个也是跟数据法密集相关的模块是 r to DBC，它跟 GDBC 是对应关系的。 GDBC 我们可以理解为是一个同步的数据库访问， r to DBC 它是一个异步的区域，作为我们数据访问的一种方式。不过我们重点关注的还是 spring JDBC 和 spring TX，也就是 so 管理模块。


具体来看， spring 数据访问程架构设计解析，我们从三个方面来介绍。首先是主要介绍一下 spring GDBC 访问， spring 为访变私用原生的 GDBC 提供了 GDB c template，同时简化开发过程，提供了嵌入式数据库string，同时对数据库操作相关的异常进行了一些重新构建，即便我们使用不同的 arm 框架，表现出来的异常行为是一致的。


第二点是跟大家介绍 spring 的事物管理器， spring 抽象出的事物管理器主要是为了解决不同数据访问组件，它能使用一个一致的事物编程模型。这里面最重要的是 spring 提供的声明式事物，声明式事物是 spring AOP 的面向切面编程的一个典型的应用场景，生命式事物真的是大大简化了涉及事物应用场景的代码复杂度。
最后我们介绍一下 spring r two d b seed 数据访问，这个是 string 5. 3 以后加入的最新的一些内容，目前各大厂应用还比较少，希望大家提前了解执行的原理，抢占异步数据访问的先机。但是目前不建议应用到线上系统，我们先观察一段时间，确实稳定以后再说。


我们看一下 spring JDB seed 数据访问。首先我们看 spring JDB c，它简化了 JDBC 操作，定义了模板类的一些 template 类，比如说这里面有 GDBC template 和 name 的 GDBC template。其次，它为了提高开发效率，构建了嵌入式的数据源，一个集成的DATABASE，这个集成的 DATABASE 它是继承了 data source，另外它统一了一些底层的异常结构，比如说跟 spring date 相关的一些异常，它都是来自于 date access exception。


好，我们现在通过代码去看一下 GDP template 和我们的恰好是数据源。首先在这里面我们创建了一个 spring d b， c 这样一个模块儿，在这个模块儿里面，我们首先看一下 palm 依赖里面的内容。在这里面我们引入了 spring context， spring j d b c 和 aspect GL where，这主要是因为应用到我们的字幕式数据事务管理，这里面我们还是用的内存级的数据库H2，这里面是引入丘皮的一个它 test 类，这里面 spring test long book 和一个 text 相关的一些内容，这是日志相关的号，这是我们的依赖的内容。
那 how 我们现在先看一下，我们这里面定义了一个 Demo model，它是作为我们一个数据传输的一个对象，跟我们表示一个映色关系。这里面我们看我们定义了我们的DEO，这里面的DO，它是依赖了 GDBC template。那么我们的 GDBC template 是如何构建的？我们可以通过 GDBC Java configure 来去运行Demo。我们的 Demo model d o 它里面提供的方法我们可以看到，这里面我们提供了一个 find 方法， find all 或一个save，还有一个 update the name 的方法，这是对应的 d o 的数据操作。那么我们先看一下操作的过程和我们的数据源是如何构建出来的。对于我们的 Demo model d o 呢？它依赖了 GDV c template。 GDV c template 是如何构建出来的？可以通过我们的 g d v c 加 2 config 里面看到。在这里面我们首先是定义了一下我们的 GDB c 加configure，它是我们的 configuration 去注解的，我们这个可以理解，我们这是一个基于 Java 配置的一个 being 对象。


下面我们首先构建我们的数据源，对于我们构建数据源就是使用了我们的嵌入式数据库，这里面我们的嵌入式数据库是使用了一个 embedded DATABASE builder 去构建的，这里面我们先看它会生成一个 UNICORN name，会生成一个随机的一个布尔唯一的一个数据名称。这里面我们设置 type 类型是 HR 数据库，同时我们设置我们的脚本 encoding 是 UT 二杠八，下面是 ignore fail drops，这个什么意思？也就是我们在执行 SQL 语句的时候，对于 drop 表的一些语句失败以后，它可以去忽略掉，继续执行。这里面我们 at script，也就是我们的 SQL 脚本。怎么理解我们可以看一下。


我们在创建表的时候，一般我们会判断一下，如果这个表存在的话，去先 drop 掉。这里面如果说有有一些数据库，它可能是不支持这种 drop table if access 的，如果是存在的话去删除掉，那么如果这种情况的话，我们可能对 circle 来说直接去执行一下 drop table，那么如果失败的话，在这里面可以忽略掉继续执行我们的操作。
我们通过这种方式可以把我们这个数据库构建出来，也就是一个内存级的数据库，这是数据源构建完成了，构建完成以后我们要注的一些 4 * 4，通过我们的数据源的构建我们的 GDBC template，我们可以从这里面看一下，对于这个 GDP template 它的构造方法是支持一个 d 的source，我们可以在这里面看到对应这个 GPT template，它提供了很多方法。这里面我们可以看到它有批量操作的，有创建的、执行的等等。这里面我们在用到了它的对应的 query 方法，在这里面还回到我们的 Demo deal，我们可以看一下，在这里面我们写了一个是 find all 方法，在这个方法里面我们执行 d d b c template query。


在 query 的过程中，我们这里面是传入了 SQL 语句，在搜狗语句里面，我们需要注的事情是什么呢？我们需要传一个对应的romapper，这个 romemapper 它可以把我们的 result set 里面的这个 RS 的这个对象集，把里面的数据遍历转化成我们对应的 Demo model 对象，这样的话可以减少我们一些重复的一些操作。
可以看到在这里面我们使用了 GDBC 默认给我们提供的是 being property roadmapper，它可以把我们从数据库里面获取到的ID，names， description 和 credit date time 等等，这些跟我们的这个对象映射上，因为我们的列名和我们的属性名如果说是对应关系一一对应的话，可以直接通过反式的方式构建出来。相比我们原生写 GDB seed 话，去通过 set guide 这种方式去确认要好好一些。


这是我们的一个 query 方法，这里面是如果说有一些情况比较特殊的话，可能是需要我们去制定我们的romemapper，我们可以看一下 romemapper 的，结构，在这里面的 room Mapper，它有一个方法，这个方法就是 map row，也就是说把我们这些 reset 内容的映射过来。这里面我们可以看到此 RS 这种 number 相关的一些内容。
好，这是我们的 find out 方法，接下来我们可以看一下这里面的 save 方法，我们可以要使用 d b c template update 方法，这里面我们看一下，因为这里面我们需要去配置一个 prepared statement set，也就是说我们在执行的时候通过占位符的方式执行，也就是 paper statement。对于 paper statement 我们需要把这些值输入进来，所以说在这里面我们可以看到我们执行 insert into 这样一个 circle 语句，在这里面我们通过单元符把我们的参数传入进去，这里面我们需要知相似已知 PS set stream，把我们的第一位，二位，三位、四位分别用对应的属性名称设置进去，这样的话就可以执行我们的这个 save 的操作。


下面这是跟四五相关的内容，我们暂时先不考虑，待会儿设计事物的内容我来跟大家去介绍。后面是我们对于手工四五相关的超，这是我们跟 GDBC 相关的一些内容。但这里面还要注意一点，大家要看到其实 spend d b c 它还对我们的这些异常去做了一些整理，我们可以看到它这个 d 的access，整个我们在这里面定义的是这个 SECD access exception，它继承了 a nested runtime exception，这个异常是可以理解为是 spring 的一个根异场，这个是可以理解为 spring 跟 d b 相关的一个根异场。我们可以看一下它的一些继承结构。



首先我们可以看到从最顶级的是 object Sovo exception，下面是 runtime exception，我们可以看到嵌套的一个 runtime exception，它是来自于 spring call，我们这个第六个 size exception，它是对应的是 spring framework 的 d o，其实这个类它是在我们可以看一下它是在 spring t x 这个包下面，也就是它的四五这个包下面去管理。
其实这里面我们可以看到下面的这些异常，首先分两大类，一个词，一些是瞬时的和非顺势的，这是非顺势的，我们可以看到这里面相关的一些异常信息，这是我们的链接查找失败，这是清理失败等等这一些操作我们可以看一下瞬时的一些异常，这里面对于它进行了一些包装，这里面可以有很多对应异常的一些定义。这是当我们不管使用是 GDPC 也好，或者是 Hive net GPA 或者是 mybadcase 这样底层数据库对应的异常发生以后，它都会转化为 spring 跟我们定义的这些基础的异常。


OK，说到这里面，我们关于 spring DDB seed 相关内容，我们就先介绍到这里，接下来我们看 spring 的 45 管理器，那么 spring 的 45 管理器最重要的也就是四五管理器 transaction manager 这个接口。其次就是 spring 提供了声明式事务以及 spring 的一些编程式事务，我们会基于这三方面来去介绍 spring 45 管理器的一个内容。
首先我们看一下 spring 的 45 管理器 transexed manager 对于这个 transect manager，这也是使用 5. 3 新加的，因为原来这个四五管理器的根管理器是 platform Transex manager。 spring 为了支持 r two d b 这样一种数据访问的方式，它构建了一个 reactive transaction manager。为了保证这个 active transfer manager 和 platform trans manager 具有相同的根源，那么所以说抽象出来了纯 SEC 的manager。


我们看一下这个四五管理器里面的三个方法。这个方法是比较容易理解的。首先是 commit 和里面的rollback，这是我们在事务处理最常用的几个方法。我们的事务提交和事务回滚这里面，同时我们可以获取到这个 transaction 的它的状态。这里面我们通过 get transaction 定义 transaction definition，也就是说这是对于这个 soul 的描述，通过对 soul 的描述获取到我们这个四五的请求状态。对于这个 platform 纯 second manager，它 4 可以理解为 4 对于 JBBC 类的这些速管理器的一个根的抽象，那我们看一下它还有哪一些具体的纯 second manager 的实现的。


从这里我们可以看到在纯 segment manager 下面，它有 platform transact manager 和对应的 reactive transact manager。我们重点放到 platform transact manager 下面的这些子类词线，我们可以看到在这里面有 data source transc manager 和 DDBC transaction manager，这里面有 GTA 的 Transc manager 以及我们这里面是海版的 Transc manager。同时如果说我们如果继承 my Badcase 的话， my Badcase 下面也有一个对应的是 my Badcase Trans manager，同时也是实现了 platform transfer manager 这样一个接口，这是 spring 四五管理器的一些抽象，以及 spring 自己这些事物管理器实现的这些类继承的一个结构关系。


接下来我们看一下 string 的生命之事物，在这里面我们会优先使用注解的方式进行设名词事物的描述，同时其实 spring 它也可以基于 x nor 的方式去配置这些声明的事物，我们的重点还是基于注解的方式。首先我们需要开启声明的词物开启的方式也就是 spring 通用的规则就是 enable 什么什么什么东西，这里面开启 4 五就是 enable transection manager，也就是说它开启了我们的四五管理的方式。


基于注解的方式，我们在使用僧名词素物的注解 add transectional，也就是在我们的方法上面去加上这个注解，那么其次对这个方法就具有了我们这个生命素的功能，以及我们还有一个注解就是 so 四件监听器，就是 transition even additioner，这个监听器是什么意义？这个监听器它实现的逻辑就是如果说我们在一个有事物的方法里面进行一个事件发布，当事物回滚的话，同时如果我们正常监听的 eventlistener 四五回滚，并不能把这个四件也回滚了，那么说一说 spring 设计出了一个新的 event listener，也就是 transactional event listener 就是它是这个事件，是支持事物的，只有当我的事物正常 commit 以后，我才会把这个事件真正的发布出来。也就是说让我们 4 件的发布和四五具有相同的一个绑定关系，让它具有一定的原子性。


我们接下来去看一下声明的事物实现的一个原理，这是 spring 官方提供的这样一个文档效果，我们可以看最终我们要执行的方法是我们的 tag mess，那么如果说在 target message，它通过僧名词事物是在哪一层执行的？是在我们 trasks adviser 这一层去执行，通过这一层去构建 AOP 的代理，那么我们在 client 端调用的时候，它就通过 AOP 代理执行我们的四五的 aspect 的处理，最终让我们的 target Mesh style 也就是说具有了我们的四五的功能。同时如果说有我们需要自定义一些 AOP 的话，它其实是在我们的 Trans Advisor 和我们的 target method 之间。也就是说我们自己定义的这些 AOP 的实现，它会更贴近于我们的执行方法，能保证我们自己实现的 AOP 逻辑也可以在事物里面包含进来。


通过这样我们可以看到对于我们的生命词，事物意思是 spring AOP 的一个典型的应用场景。接下来我们去看一下 spring 的编程式事务。
如果要手工编程的方式去执行我们的事务管理的话，有两种方式，第一种方式是我们使用 spring 的 soul 管理器，就是 platform transection manager，另一种方式是使用 spring 的 soul 模板，就是 transaction template。这两种方式其实可以帮助我们去手工去做一些事物管理，但是相比我们的声明式事物的话，如果不是不得意的情况下，不推荐大家使用边长词的词，因为这样确实比较繁琐。


现在我们去通过代码去看一下跟四五相关的一些事情。首先在这里面我们需要构建我们的 45 管理器。构建 45 管理器需要做什么事情？这里面是 platform Transex manager，我们构建这个 data source 的 Transex manager，它需要的参数也就是我们的数据源。如果我们有一个对应的 GDBC data source，那么我们就可以获取创建我们的 Trans manager。为了我们四五的管理，我们在这里面构建了一些 transection template，它的参数是需要一个 transact manager，也就是我们这里面构建的这个 platform transacent manager，这样的话我们就具有了一个 45 管理器和一个 45 处理模板。我们可以看到，在这里面我们还需要去开启一下我们的 enable transex manager，也就开启一下我们基于注解的生命词。


这几点做完以后，我们现在去看一下我们的业务类，也就是我们这里面的 Demo model dog，在这里面我们可以看一下，我们在这里面通过自动注入的方式，把我们的两个事务管理的主键注入进来，在这里面注入进来以后，我们看第一个方法，也就是 find all 这里面我们使用了声明式事物。在这里面我们通过注解 at transection 的方式去标明 find all 的话，它是一个 read only 的一个事物，通过我们对于读方法标明 read only，它底层级优化会更友好一些。


我们看第二个，对于我们这种写的操作，我们比如seal，我们也 see add a transaction，同时我们这里面指定一下 the bike，也就是回滚，发生什么异常去回滚，这里面我们是指定发生 runtime exception 的时候进行回滚。在这里面我们可以看一下，我们只要通过一个简单的注解，就可以让我们这个 seal 方法去应用上它的四五功能。
那么接下来我们看一下手工去构建四五怎么去构建？如果说需要手工构建思路的话，相对来说是比较麻烦的，在这里面我们可以看到这里面是 update name，如果说我们想通过 ID 去修改 name 的话，我们需要这样一个 SQL 语句，显然它是应该需要在事务里面的，这里面我们是通过了我们的 transact manager 去开启事务。


首先我们在这里面去定义我们的通过 Trans manager 去获取到我们一个四五的一个 Trans states，这个 Trans States 是需要一个参数，这个参数就是我们这里面的 defiled transaction definition，也就是我们的一个 45 定义文件，对于这个 45 定义文件需要配置两个关键属性，一个是我们需要设置一下我们的事务名称，在这里面我们一定要做到唯一性。另一个方式是我们需要把我们这个 45 的传播的级别，也就是 45 传播行为去声明一下，选的事物传播行为是required。


如果说当前环境下已经有四五存在的话，在这里面会创建一个新的四物来去处理。首先我们获取到这个纯 second state 这样一个四物对象，接下来我们就应该做我们的业务操作，整个这里面的内容是我们的业务操作，也就是我们通过g，d，v， c template 去执行这个修改的词口语句。在这里面我们输入负入我们的值，那么这里面需要注意的事情是我们要 catch 对应的异常，如果说我们发生异常， catch 到 runtime 一个三部分要做的事是 transacent manager 进行rollback，也就是对我们的四五进行回滚。那如果说没有抛出异常正常情况的话，我们在这里面对我们的四五进行commit，也就是四五的一些提交完成，四五我们把我们的返回子 count 返回过来，这样的话我们通过手工的方式去构建，四五就完成了。


相比我们在这里面去使用一行注解去完成我们四五声明的过程，我们在这里面很显然这些代码是不是那么简洁，是相对来说比较繁琐的，像这些代码可以理解为都是一些常规的套路代码，它并没有什么技术含金量，以及我们发生异常进行 robug 和正常进行回滚这些内容其实我们是可以基于 template 进行优化的，我们接下来看下面的下面。


这里面定义的方法是 update states，也就是说修改我们的状态跟修改 name 的业务逻辑是非常相似的。这里面我们用到了纯 sexon template 区域，做我们手工事务编写，相比上面我们使用 Trans manager 的话会简洁一些。你看我们这里面 translate template 自行 excuse 方法，在这里面我们使用了 number 的表达式，这里面是它支持的参数就是 Transex dates，注意我们插入传入进来，在这里面就写我们的 EO 方法就行。


在我们的 Trans template 里面，它去做了一些区分，它区分的内容我们可以点进来，在这里面去看一下，我们重点关注这段代码，也就是 accent 字形 do in transection 去执行的时候，如果说发生异常的话，它会进行我们的因为我们的事务回滚。


如果说没有问题的话，这里面我们进行我们事务的提交，其实也就是spring，它通过模板的方式把我们这些开启事务和提交事务或回滚事务的这些常用功能进行了一个封装，这是我们对于手工去事务的方式，还有一种方式，也就是说我们刚才介绍到了对于在我们事务方法的时候，如果说我们对一个方法保存完成以后，我希望发布出一个事件来。


这里面我们定义了一个 publish event，也就是 create event，其实我们并不关心它是什么event，我们只关心的是我需要在我们四五提交以后去进行把事件发出，事务提交以后，这个发出我们需要怎么去做？在这里面我们可以看，这里面我们定义了一个四进监听，这里面有两种方式，一个是通过 at event listener 这个注解去监听我们的事件，另一个是通过 transaction event listener 比较一下这两个区别。


对于 event listener，只要触发了 publics event，那么这个监听它就会触发到。那么对于 transection event listener 它与它的区别就是只有在事务正常提交的时候，它才去监听到这样一个操作，也就是说如果说我们是对于事件的发布，也是基于四五级别的，推荐大家使用这种方式去执行我们的操作。


好，这是我们关于 GDPC 事务管理器的内容，这里面我们介绍的主要都还是基于 platform Trans manager，它对应的一些子类的一些实现。我们看一下 spring r two d b seed 数据方案方式。那么首先是什么是 r two d b c 这个命名， r two 也就是两个r，这里面主要是指 negative relational DATABASE connect activity。怎么理解？如果说我们不去细究的话，我们就可以理解为它是一个异步的 JDB seed，一个规范就可以了。其实这里面它跟 DDB seed 关系也就类似于我们 spring MVC 跟 spring Flex 的关系。


第二步我们去认识一下对于 r to DBC 它提供的一个接口规范， DATABASE client，这个 DATABASE client 跟我们对应的 Web client 是类似，可以理解为是我们读取数据操作的一个数据客户端，我们通过它去获取我们异步的一些数据请求。


接下来我们去了解一下基于 r two D b seed 一些规范，我们通过 RDB seed 方式去完成对应的CRUD，当然就是 r to DBC，它现在的应用还不是很稳定，当发布需要迭代一定的周期，这里面不作为重点，大家知道怎么去操作就可以。


接下来我们来看一下我们定义的接口，在这里面我们定义了一个是 spring r to d b seed 一个模块，这个模块里面我们可以看一下。首先 palm 依赖， palm 依赖里面我们特意注意一下，这里面我们引入的是 spring r to DBC，不再引入 GDBC 了，同时我们引入的 SR 数据库，同时我们需要引入一下 r two d b， c h r 这样一个驱动性的一个依赖包。下面其他的内容基本上是一致的，并没有什么特殊的内容。


我们看一下这里面我们的实现，这里面我们定义了一个 r to d b seed 加configuration。在这个 Java configure 里面我们做的事情是这样，我们在这里面定义了两个bin，一个是 connect factory，另一个是 DATABASE client。那么我们可以通过 HR connect factory，通过 in memory 的方式去构建一个 connect factory，这个 connect factory 我们可以理解为就是我们的 data source 数据源，跟我们的数据源是对应关系的，接下来我们通过 connection factory 作为参数构建我们的 DATABASE client， DATABASE kind 我们可以理解为对应的我们的g， d b c template，也就是说执行我们数据操作的一些 Panda 端。


那么我们完成这两个对象的构建的话，接下来看一下它们怎么使用，在这里面我们通过单元测试去描述一下这个里面的使用，在这里面我们可以看到我们在这里面通过 spring GNE 的 configure 去引入 r to d，b，c，加入 configure 就是把我们的配置引入进来，同时我们可以通过 outer where 也就是猪的方式注入我们的 collection factory 和我们的 DATABASE client。在这里面我们是也是需要去构建我们的虚拟的我们的数据库，这个内存积的数据库，在这个内存积的数据库，我们通过用这种方式执行我们的收口，把我们的表创建完成，同时初始化数据。


在这里面我们执行我们的 test query，就是执行我们查询操作，在这里面查询操作肯定还是需要我们的 SQL 语句，在这里面我们是 SQL 语句，就是一个非常普通的 slack 查询，我们可以看到在这里面我们通过 client 点circle，把 circle 作为参数传进去，我们通过 FACTS 获取代替all，我们就得到一个 Flex 一个对象获取到这个 Flex 对象它可以包含 0 到 n 个对应的数据节点，那么我们获取到这个 flag 对象，其实也就获取到了我们数据的一些引用关系。我们就可以监听对应的数据返回情况，做我们的业务逻辑。其实从这里面去看的话，只是一个异步的一个操作，实现的过程可能比较复杂，但对于我们来说，我们先做到了解它，慢慢去熟悉它，等它实际成熟的时候，我们再进行我们线上业务的应用。回到PPT，那么关于 spring 数据访问相关的内容我们就介绍到这里，同学们，我们下一章节再见。

