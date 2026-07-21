---
title: 2-1 Spring Data JPA核心源码解析-1（1904）
---

# 2-1 Spring Data JPA核心源码解析-1（1904）

[image](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/1ead9b86-9f3b-406b-ba49-d65e3cddc837/SCR-20240814-hpfz.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TFHUAZJD%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T232133Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIGauk9vko323eh8c3LRF0CGBl3VgMKOaBn9siADxE8ujAiEA%2FJYFefBtIAUj50EIRqpFps2c9FNQQ2TWSwUR1GO%2BppcqiAQIxv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDLy8EC9lkr00EBFEzircA%2FO8U%2FGHkxJ1e0BZcj1SqV7XKiDna7jUFvV4JSxreaYAMUWLA7Q4PGf7SR9r9fdpl8%2Flxgc04uQJULdeUBmkLdveY9G6JVWsKVB5xqaJrRffX8YavImEvnQCjSXvK1f4fFwWhQeP08GIiKn%2BKFdMSXzVEvfzTcizLD0MHdY2Ker1BTUNZkWrt%2BsP0R%2BSiclta334FBP3BGOSoJDVimgoFaV9%2B6PLN9mh1wP4AWS8mlqP4X7DIl0KSxGT3Uc0xFfnFDJriak95VlO3k3lM5%2FPz2HPbxli1Bnp1pX8jL4f7nRKAee41h%2Fx2Yjo15NLUrSW5BHTM2HMG5m%2F0c2zN1xSouB08AqwiDM5BZuAyRPhQCoGm2JX60Y42t%2BHkcMZWrZ2saVkJPQYzbhOA45zDaMQ%2Fi7w9j6li9cZoHgVPQitluwktd0T72qQvEtszJOy7vWtYCwisiNoBFS8IjYXRRpn6QIxwuvldsMMC%2B1J4dS2hox2ekUeF6e7bm3sS8YgAht35lqwtWG99c%2BA%2Fs6drXr5huNub573CdnkiHYDj7sMzlFv0v6KuwJv118FxPTU4m%2FAnJpnrxR1j2Jh7nqZdR5MhT%2FUmMmwaUVn3IMhiQiPTJ3jWYvsa2G4QhjPTdLbMMy3%2F9IGOqUBaHJ%2FnDG7K7aDzR%2BV49ZAVaorFi0RlijT9H7Gv4yHo1mjHK6H5MsGneiupSv0LKVDhE%2Fa1n0eZIgF%2Fo0TbYJv1zknI2Q9F4%2BYvkYyUp6JTWc83N6nRNGSpJpXy%2BqmingBArOhlMB8S%2BuCSGvavj3gIgCJzvp9RoPQHwWj2HpvZEG%2BlsSsZJKu%2BQGcr29mUoEOkYwq3bG2pTRJisT8XV2spvnaUCxT&X-Amz-Signature=0a63ddc955a2b3d3605b1023a7d3ea62783dc9225a4aeaadef93fc37b77da79f&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

同学们大家好，这章节我们来介绍 spring day 的 JPA 的核心源码解析。那么说到 JPA 呢？我们先简单解释一下什么是 JPAJ API，也就是 Java persons 的API，也就是说 Java 做持久化的API，它是在 sun 官方在 JDK 5. 0 以后提出了一个 Java 持久化规范，也就是 GSR 338 这些接口，它所在的包对应的是加 x 的persons。


那么 GP 的出现主要是为了简化词 90 开发以及整合 OM 框架，结束 Hive net、Toplink、 GDO 等奥姆框架各自为应的一些局面。GPA，它是在吸收现有奥姆框架的基础上发展而来的，易于使用，伸缩性也比较强，就是我们常见的hypeline，它是 GPT 的一个实现，但是其功能是 GPT 的超级，也就是happiness，它实现的功能要比 GPI 更多。当然因为 GPI 是规范，所以说我们现在使用 GPI 比使用 Hipna 的更稳定，那么 GPI MI 之间的关系可以简单的理解为 GPS 标准接口 Hypernet 去实现。这样去理解的话，可能大家会有一些疑惑，其实我们应该知道 Hypernet 出现要比 JPA 更早，其实事实上是 Hypernet 在 OM 框架的定义上成为了一种约定和规范，也就是得到大家认可以后才定义了 GPT 的规范。或者说也有人说到，其实 GPT 在定义规范的时候，很多 HIPNET 当时的参与者参与了 GPT 规范的定义，所以说我们可以理解为Hypernet，它这个技术实现也促进了 GPA 的构建。


对于GPA，它下面涉及到三方面的一些技术，对于首先是 ORM 的映射元数据，它其实是指我们的数据库表结构与我们加 r 对象属性之间的一些对应关系，也就是通常我们可以理解为一个关系型数据库，每一张表它对应一个对象表里面的属性和字段对应了我们一个对象的属性。


那么这里面我们对于源数据的描述，它可以是 x 描述的方式，也可以是注解的方式，那么现在大家使用注解会比较多一些，所以说现在我们对于 GPA 这些对象一些元数据的描述，我们通常也会采用注解的方式。另一个就是API， API 是指我们通过 GPA 操作我们慈禧翠样进行数据化、持久化操作的一些API。那么这里面的持久化操作 API 主要是指我们的CRUD，我们对应的正餐改查。


另外一种就是查询语言，我们通过面向对象而非面向数据库的查询语言，我们这里面称之为GPQL。那么对于 Hive net 它称为 s q l，这都是对应的一个查询语句，其实跟我们的 SQL 其实是类似的，其实整个 g p q l 还是 Hive net 对应的 h q l，它最终都会转化成我们对应的 g d b seed SQL 语句，整个我们采用 g p q r 或者说 Hirender s q r，它主要是为了避免我们的程序与对应的数据库的 SQL 紧密耦合。也就是说我们知道对于不管是MySQL，还有 d b two Oracle，或者说是 SQL Server，它们都对于除了支持 SQL 标准外，以后还有一些它自己本来的一些特征。比如说我们对于分页来说，像MySQL， SQL Server，Oracle，它都有不同的方式进行分页。那么如果说我们基于海本 net 的 SQ2 语句，或者 j p 的 j p Q2 语句，那我们可以用相同的一套分页的逻辑去适配不同的我们对应的本地化的查询语言。这就是我们对于 GPA 我们几个关键的一些要素。


spring day 的GPA，它是 spring 基于 arm 框架和 JPA 规范，在这些基础上封装了一套 GPT 的应用框架，它可以使开发者用比较简单的代码去实现对数据库的一些访问操作，也提供了一些 CRUD 在内的一些插入操作，非常易于扩展，学习成本也比较低。那么我们首先来对于 spring day 的 JPA 核心源码解析的内容，我们会分三部分介绍，首先我们是介绍 spring day 的 JP 的源码介绍，我们去 get help 上去看一下对应 string 堆的 GPA 源码的结构。


第二，我们去介绍一下 string 堆的 GPA 的一些核心API，那么我们使用 string 堆的API，那么整个它用到了哪些关键的类，关键的接口？第三部分我们就是对于 spring day 的 JPA 它的一些执行流程的一个介绍，那么首先我们来看一下 spring day 的 JP 的源码，那么刚才也介绍到了对于 string day 的 GPA 的源码是在对应的 git help string product 下面的 string day 的GPA，这是对应的一个 end git 工程例子，那么对应的模块它只有一个是 string day 的GPA，那么在我们介绍 spring date JPA 课程的过程中，还会涉及到一部分源码，也就是对应的模块是 spring boot start date JPA，那么这个模块它是在 spring boot 模块下面。


这个大家可以再看一下 string 部的源码，找一下这个我们一个模块，当然这个模块它是一个starter，这个 starter 里面它只会包含了对应的 palm 文件，对于我们的gradle，也就是我们 gradle 对应的一个配置文件。


那么现在我们来看一下 string day 的 GPT 的源码，那么在这里面我们去打开了，这是 string day 的 GPA 的工程源码，在这里面我们先看一下它对应的 palm 文件，那么对应这里面的 palm 文件，我们看对于 spring date GPA，它是 spring date 的一部分，它也需要遵循对应的 sprint 的规范，也就是我们看这里面的point，它对应的 point 使用的是 spring date point，也就是对应的 framework 下面 date builder 的 group 下面。


那么我们看一下它的依赖，对于这里面的依赖的内容，我们从这里面去看，首先这里面是 spring day 的common，这是因为它是 spring day 的一部分，这里面还依赖了 spring 的OIM，这里面有 spring contact 和 spring AOP，这里面 spring TX，也就是跟soul，像 spring 的 soul 管理器相关的内容。那么这里面就对应的一些常规的依赖了。


那么好，我们所关注的一些依赖是在哪？是在对应的 spring YM 里面，我们可以从这里面去看一下。对应一个树结构，我们看到这里面有对应的 have net，我们 have net CO 和 havennet common 的 annotation 等等一些内容，这里面还涉及到对应的加x，annotation， API 等等，这是我们看到的一些这些依赖，那么我们了解完这些依赖以后，我们这里面去看一下对应的源码。在这里面我们去看对应。


首先整个 string GPT 的 start 包是在 d 的 GPT 下面，在这里面我们可以关注到几个比较关键的点，这里面涉及到 convert 一些数据转换，嗯， domain 这次跟我们 spring data DP 绑定相关的一些内容。


这里面我们再看一下我们的Mapping，那么 Mapping 这里面涉及到一些映射关系相关的一些信息，这里面的是protection，也就是我们需要做一些数据映射的一些过程，这里面我们重点去看哪些，就是reporstery，那么在这里面我们知道这里面有我们会介绍它 reports 的一些实例转化的一个过程，这里面会有 GPA 的 requester being 和我们这里面是 enable GPA reposter。


其实对于GPA，我们在使用 string 的 GPT 的过程中，其实这个 enable GP reporter 是我们一个启动器，那么当我们 string 容器执行的过程中，它扫描到这个注解，那么就会进行这些 rejects 的初始化，把我们整个 string 对的这批这个初始化的过程就激活起来。这样就可以我们使用命名查询的方式去执行我们数据库的增删改查。
这里面我们可以看到它还会有一个 GP 的 auditing 的一个register，也就是它会去做一些审计性的操作，会把我们当前的操作人，当前的操作时间都会进行一个更新，这里面会有一些跟它对应的相关的一些处理的信息，这里面我们看到还有对应的一些 query 相关的一些内容，这里面我们可以看到对应的是 abstract GPT query 和 abstract string base GPT query 等等。这些内容其实我们用的比较少。


大家可以了解一下它这里面对应的一些类结构是怎么回事。我们更关注的是对应的这是我们是GPT。
对于 GPT 我们可以看一下，我们知道 GPT 它是继承了 pacing and sorting 的reporsory，但是我们再向后看，这里面还涉及到一个 query by example 的extrator，也就是说其实我们的 GPT 它实现了两个接口，这两个接口一个是来自于common，另一个是来自于 spring date GPT 这个模块。下面 repeating and sorting 的 reporter 我们大概已经了解，它就是实现了整删改查和一些分析的操作。那么这个对于 query by example，它是基于另外一种查询语句，我们可以看到对应的这个接口，这个接口我们可以通过方法命名，我们知道它是一些读的查询方法，比如 find one， find all。对于这里面它需要传一个example，一个对象基于这个example，其实这个 example 也就是把我们 where 的这些条件的序列化成一个对象，通过这个对象的时候，把我们的一些查询语句传输过去。


find 2 FIND 2 这里面还有对应 find 2 支持一个排序的操作，当然我们可以看到这里面对于 find 2 支持我们一个分页的操作，其实跟我们对于 hidden 的 sorting 里面对应的查询条件是类似的，只是我们这里面是支持一个example，一个参数，这里面是我们 count 和是否存在这样一个对应的这几个方法。接下来我们来看一下另一个。
相关的，就是我们的 GPA species e Cuz，其实我们可以看到这里面跟我们刚才看到的这个对应的 query by example 其实很类似。
只是它们的参数是不一样的。


对于 GPA specification 的ECR，它对应的查询参数也是specification，那么对于 query by example 的exector，它对应的参数是一个example，随着这就是它们的一些区别，其实这些接口最终它会在执行我们查询的过程中会使用到。


那么其实这里面我们接着看另外一个比较重要的一点，对于我们这里面会看到一个 simple GPA departure，那么对于这个 GPA simple GPT request 是我们要知道在我们写使用 GPA 的过程，我们只是使用一个接口，那么接口里面通过命名查找来去定义我们的一些正确考察的方法。其次对于我们所有的这些接口，注重它都会转换成一个代理的一个实体类，那么基于我们生成的这个代理类去进行我们正常改造操作，其实这个代理类都依赖了我们这里面的 simple DP reporter，我们可以看到 simple DP reporter 它是实现了一个 DP reporsory implementation，那么点开它的话，我们看到它又间接地继承了我们的 GPT 和 GPA specification 的 e Suiter。这会大家可以明白一些原理了。


其实我们最终对于 DP reporsory，它继承的 pacing and sorting report 也好，或者说是 query by example extrator 也好，其实最终它都会通过我们的 simple by，再也就是 simple JPA reporter 来进行我们的执行。


对于这里面 simple JPA reporter 里面我们可以看到它是依赖到我们的 GPA 核心的类，就是 int d manager，也就是我们的一个实体管理器，我们通过这个 4D 管理器对数据库进行增删改查。那么这里面还有一个 GPA int 的information，其实这里面是定义了我们 GPA 实体的一些信息，我们可以点开简单看一下，这里面会有一些签名儿类的一些方法。我们看到它对于 GPT information，它继承了我们的一个 int information，同时还要对应的 GPT 的metadate，我们可以在这里面点进来看一下。
对于 int 以后 mission 里面会包含当前这个对象 is new，我们可以 get ID，通过对象获取到对象的一些 aid 信息。这里面对于 ID 是一个必选的一个 require ID 的一个是默认实现。当然我们可以看到它还继承了我们的 entity metadate，也就是我们实体的一些元数据信息。对于 Internet lead，它。
只有一个方法 get 叫type。


也就是我们这个管理实体类型的类型是什么？我们再回到这里面，对于 GPT information，我们这里面还涉及到一个 GPA 的 entity Meta date，我们可以点开看。这里面，对于 GPT 的 e t Meta date，它继承了我们的一个实体的 internet date，这里面我们可以获取到这个 get entity name，也就是说我们获取到这一批管理的一个实例的名称是什么？好，这里面我们大概简单认识了一下关于 string d 的GPT，它的一个实现的过程。


回到我们的PPT，那么接下来我们看一下子润迪的 GPT 的一些核心的API，那么对于核心API，我们这里面去简单说一下。这里面首先包括我这边分了三类，其实一共是两类，这里面像 repository 和 ID 厅，也就是一个是用于我们这些reporter，也就是我们的 DAU 的一些构建的一个过程。另外就是说我们基于 GPA 进行一些审计的一些操作，当然这个 editing 它也是基于 PORTAL 来完成的。另一方面是我们基于 string boot 的一个 auto configuration，也就是 GPA reported auto configuration。我们看到这个配置，我们知道使用对应的 spring boot starter data GPA 的过程中，启动的过程会依赖到这个自动装配，那么其实这个自动装配它的实现最终也会默认依赖到我们上面这些内容。


好，那么我们先来看一下 repository 相关的内容，对于 repository 相关的内容，我们这里面会涉及到 GPA repository，那么其实如果说如何去解析 GPA repository，这里面会涉及依赖到一个注解，这里面叫 enable GPT，那么基于这个注解我们知道对于这个注解它需要去装载一些加载器，也就是说我们基于注解的去解析，当我们这闭隐初始化的过程中初始化一些信息。这里面主要初始化的内容也就是对应的 GPT 的register，其实在通过 GPA report register，也就是说这个注册器注册的过程中，一个比较关键的对象，也就是 GPA report configure extends，其实看到这个我们可以见名字义，也就是 GPT 的一个config，一些配置信息的一些扩展，那么基于配置信息的扩展去把我们 GPT 的信息解析出来。


那么对于这里面的 GPA report，我们可以知道刚才也介绍了一些，首先它是需要它继承了 PACING and sorting 的 report 以及 query by example，etc，那么其实 GPA reporting 它有一个对应的子的接口，子接口也就是对应的 GPA report implemation，也就是说对应的一个实现的一个接口，那么对于它的接口的一些默认实现一个就是 simple GPT 的reporter。对于这个 report 它是一个实现类，这个非常重要，大家去打开看一下，刚才也介绍它的一些实现的一个过程。


下面对于 simple GPT reports 跟相关的一些 GPA specification 的extrator，也就是他们对于这个接口与这个接口他们查询的方法是很类似的，只是不同的参数，这里面还会涉及到我们定义的这个 customer 类的 GPA positive，那么它这个接口如何去实现增删改查？我们知道它是基于一个代理类来实现的，那么这个代理类它的根本实现它会涉及到了 simple GPT reposit，那么这里面我们在构建这个代理类的过程中会用到 GPT factory being，我们看到 factory bin 作为后缀，我们知道可以通过这个 bin 来构造我一个新的，通过 factory bin 构造一个新的bin，这个 bin 也就是通常我们在写我们的 GPA report 的过程中对应的一个实现了它的一个子类，那么 GPA report factory bin 跟它相关的是 GPA report factory，那么通过它来去构造一个 report factory。通过 report factory 来构造我们对应这个 report 的一个代理实现。这里面会涉及到我们 simple GPT reporter，跟这里面是一个对应关系。


对于 simple GPT reporter，它会涉及到 DPA entity information，刚才我们介绍了，这里面还涉及到一个 entity manager，这里面还涉及到一个 presence 的一个provided，但这就是我们构造 reposer 一些核心的一些关键。其实对于我们来说，我们只要关注 GPT 它对应的类就可以满足我们常规的一些开发工作了。接下来我们看一下 ID 听跟审计相关的内容。


如果说我们需要使用 string data GPT 开启审计，我们需要加上 add enable gdating 这样一个注解，那么同时我们还需要去对于一个 editing 的 entity listener 进行一个实例化，那么这样的话，也就是说当我开启我们的审计操作的时候，对于 editing intedlistener，它监听掉对应的一些我们的 save 和我们 update 方法的时候，我们去修改对应这个实体。里面通过几个注解修饰的一些操作，比如说我们的 create by 以及 create date 和我们的 modify by 和 motivate date，就是也就是它说明了我们的创建人和创建时间，以及最后修改人和最后修改时间进行这几个属性的更改。


当然这里面还涉及到一个乐观说，也叫 Adversion 一个版本的信息，这里面我们不需要展开去介绍了，对于我们的 string boot 对应的 GPT auto configuration，我们在案例演示的过程中可以跟大家去演示一下它是怎么去操作的。


那我们了解了 string d 的 GPT 的这些核心API，接下来我们看一下 string d 的 GPT 的执行流程，那么在这里面我们看到这个图，其实 spin date GPT 的执行流程，它也会分初始化的过程和执行的过程，那么对于初始化的过程，我们看对于它会通过 spring day 的common，我们 spring day 的 DPA 和对应的 DPA reporter 以及 data source 来构建出整个这个 CID 操作的过程。


那么其实在执行的过程中，我们对于我们自定义的 partner reportery，如果它执行的是 GPT 原生的，也就是我们 ZK repulsory，它提供的这些方法，比如说DELETE，find，one， save 等等这些抄录它最终会执行到我们的一些实现代理类，也就是我们的 simple GPT reporter。


对于 simple GPT report 里面提供的一些默认的实现就是DELETE， find all，find，one，save，那么如果说它使用了我们 string day 的 GPT 相关的特性，也就是我们的命名查询，比如说这里面我们是 find by name，它最终会生成的 SQL 语句类似于 select 指定的我们的一些属性，比如我们这里面是 select 星，那么 from 我们指定的 passion 这个表，那么它的查询条件就是 where 对应的 name 就是属性 name 等于指定的我们对应的参数。这里面会涉及到我们的一个命名查找。那么对于这里面我们去先去了解一下我们程序启动的逻辑是怎样的，我们再去介绍我们是程序执行的逻辑，接下来我们来看一下 spin d 的 GPT 的初始化流程。

