---
title: 2-9 Spring Data MongoDB核心源码解析（2215）
---

# 2-9 Spring Data MongoDB核心源码解析（2215）

[image](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/9f8a1ff2-b733-4409-82bf-57431496dd5b/SCR-20240814-imqv.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XOIN43DF%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T232141Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIFoSErecGls169NoBcuwFPbabMcSE8A98eXZpBmB37UiAiEA9%2Bork91MiDFz9fNkGr1SCPYZO%2FcOOUVhud8aY8Aj5DQqiAQIxv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDEaU9VE9DKpR7WvrPyrcAwF9jTQh1FRI5wS9ZM3pjXA%2BIDCNiNwXisOxOOukufNkL2T1unpI1bEqNdDHUv6KjiEFxfMUhnpl15Uv0Ds%2F72e2KBysihxgOTpgIq4L65NCWsf2aHwo7raLM5tmJLrMSQAbZuaHWnHEv%2BepcpfI6WZ7Vc56orBNefEJX%2FIsc1Vg1Lo16Q%2F262hIxgSr8a7WMx4LqO27%2FrphBJNUP9PmR5m86aXs0i7oVOMgI9C0FD263iOzDSQJKuDVdEWlGfIk1I%2B6TXru2%2FRLJrsv%2FWbwcfP9Zm1LHECKyXCwWkC%2B6VX1Ro46KUnZ8pFqa6t5OoAsqpKNFv3Uwq7MiwjQ3sNU%2Bv4f4aGi9kev6dlKihXgPv7idSv0tagNz43v%2BSYVuGhfGkOCjndLGLnvcTHKsvLUeebGT0%2BSATwwUZHVS0O3Iw7%2FFb8%2FSGh3ZS8cjA6a5tjkba7IEz31MXbhsLvuUr2SChRaUeIWBAfo9piKJdDTGoaQWfyrMZ8QRLHmO8YauLatvc44GGqtysWIoz0rkAGN9KiimKR%2BvzIUo8BUtDkI8NbCqANy3E58M%2FWz2hlp17NHnGqx2U8dheOziSHEPhoVsHZQCbhm6OO98QXl49OypaTw6AewNnXoNQWNvLjCMJm3%2F9IGOqUBph5U0An7GAcMLOfkiGrbsjZULzq1ltwv7IaSVj%2F%2FJssSX3EOI5evjE090PH6gsbPJP%2F9Z1VhNeRV6vpduFcMgjuRjyQScXWcpnhkv0k4U4ZBYHBmPPXH55HVGK6dx%2BIevgmFNxyPfc973xTX8esNES7F0dBMtdFq1nOJPmQCggxTkUVhZU6yw%2FV4BWtWVSsDATx9zk3tz%2BFNFP%2Bxh2Pe4CnQrpXe&X-Amz-Signature=d6164ff2df87f81ac601ee6d70bbbc66fdc6b44003235eb6fdf6d98055287e7a&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

同学们大家好，这章节我们来介绍 spring date MongoDB 的核心源码解析，对于 MongoDB 可能大多数同学使用的不多，通过我们课程的学习让大家能够快速上手应用。那么 MongoDB 的内容我们也分三部分来介绍。首先是介绍 string day 的 MongoDB 的源码介绍，这里面我们初步的去介绍一下 MongoDB 的源码内容，通过 get help 的内容和 spring 官网的文档去了解 spring day 的 MongoDB 做了什么。第二部分是 spring day 的 MongoDB 的核心API，我们会通过对于 spring day 的 MongoDB 的核心源码去了解各个 API 它的一些实现。


第三部分是我们介绍 spring day 的 MongoDB 的初始化流程，这里注意一下前面的章节，我们大多是介绍它的执行流程，在执行流程里面会划分初始化流程和运行流程，那么这里面因为它的运行流程其实跟我们的 spring day 的 JPA 或 spring day 的 Redis 其实很像。所以说这里面我们重点去介绍一下 string day 的MongoDB，它的初始化流程那么好，首先我们来去看一下 string did MongoDB 的源码介绍。对于 spring day 的 Mongo DB 的源码，这里面我们重点还是关注 spring product 下面的 spring day 的 Mongo DB。对， spring day 的 Mongo DB，它主要的核心模块也是 spring day 的 Mongo DB，当然里面还有一些其他的模块不是我们介绍的重点。另一部分跟 spring did MongoDB 相关的，也就是我们 spring boot 里面跟 MongoDB 相关的一些 auto configuration，这个里面我们也会简单去介绍一下。


那我们先看一下这里面我们看到 Sprint MongoDB 这个 get 下面页面的内容，从这里面我们看它的 star for 1. 3 k，也就是说它的关注量还是有的，跟我们的 GPA 或者说我们的 Redis 相比的话，还是有一些区别。那么我们来看一下这里面 splendid Mongodp 来简单的一些我们 GitHub 库的一些情况。对于这里面我们可以看到它的更新还是比较频繁的，我们看最近几天都是有更新的，而且它的发布的也是比较频繁。对于 spring date Mongo TB 这里面会有一些简单的介绍，它的整体目标还是基于 spring date，把我们各个不同的这些数据库通过构建统一的一个访问方式，也就是我们通过 spring day 的方式来去访问MongoDB。对于这里面我们可以去切到我们 spring 的 MongoDB 对应的官方网站，我们可以看到是 spring i o 下面的我们 spring 的 MongoDB 对应它的一些介绍页面。


首先我们可以看整体的一个概览，对于整体概览我们看到 spring didnt for Mango DV，它是整个 spring date 的一部分。如果说大家在学习的过程中对于英文可能比较吃力的话，我们可以通过浏览器进行一个整体的一个翻译，我们看这其实是很方便的一种方式，就是说对于我们这些技术文档，我们通过这些机器进行翻译，我们可以理解它大概的意思说涉及到一些文学作品，我们用机器翻译可能会丢掉了他，比如说作者的一些感情的一些色彩问题。对于技术类文档我们可以不用考虑，我们就通过机器翻译去快速的理解它的作用，其实很有帮助的。


我们可以看到对于这里面 string day 的MongoDB，它对于项目提供了 MongoDB 文档数据库的集成，这里面的文档数据库也对应的 document 的这样一个数据库。那么对于 spring date MongoDB，它的关键功能的领域还是以PORTAL，也就是我们对应的一个实体的数据模型为中心，通过 MongoDB 的 DB client 来交互，轻松的形成对于 repository 这种方式的数据库访问，其实跟我们的 ZP 的report， Redis REPORTS 和 Electronics 的 reporsory 其实很类似的。这里面的特征其实我们学习完了， GPA 和 electronic 其实很相似的。我们可以看到对于 spring been 它的一个配置，它支持用 Java 的configation，也支持对应的 XL 去构建这个 MongoDB 的client。


我们通过 MongoDB 的 client 去访问我们 Mongo 的数据库，这里面跟我们在使用 MySQL 的时候，我们通过 MySQL 的对应的 data source driver 以及我们的 data source 驱动去连接我们的数据库。同样我们会把 Mango 的 calendar 去封装成一个对应的 template 类知识，里面是 Mango 的一个template，跟我们的 GDBC template 是一样的，因为我们在知道 GDBC template 它会依赖到 t source，那么 Mongo template 它会依赖到 Mongo 的client，它可以提高我们常见的 Mongo 操作的一些生产力，包括对于文档和portal，也就是说我们模型之间的集成对象的一个映射。这里面还包括一部分的异常转换，也就是说跟通过 Mongo client 跟 MongoDB 交换过程中的一些 client 会转换成我们统一的一些异常形式。


其实这里面也应该知道，我们在 GDB seed 过程中，我们的 string day 的 GPT 也会把我们 circle exception 转化成我们的对应的 data access exception，这里面会涉及到一个我们的是非运行词异常转化成运行词异常的一个过程。因为我们把非运行词异常在编写的时候，我们需要手工的去case，或者说把异常进行抛出整个过程，其实编的代码可能会显得比较复杂一些，那我们转换成运行的异常可以进行一个统一的处理。


另外这里面会提供一些功能丰富的一些对象映射，这里面的对象映射主要还是我们通过一些注解对于映射进行了一些扩展。你看这里面它的翻译词注释，其实这就是我们对应的属性的一些注解，我们通过注解的映射元数据可以扩展这些数据的格式。另外这里面还会有一些次久化和映射的一些生命周期的事件，也就是我们进行create， save 或 update 的过程中去广播出一些事件。


其实我们还可以通过像 Mongo 的 reader 和 Mongo 的 writer 去抽象，去映射一些更底级的演，如果说我们需要更深层次的一些复写，可以基于这两个类和接口进行一些扩展。另外我们可以基于 Java 的查询标准的词性更新DSL，其实我们 DSL 用使用的非常少，这里面我们的重点还是我们通过实现 reposure 接口来自动去构造我们这个动态的代理这个死线类，基于这个死线类来完成对 MongoDB 的操作。下面是比如说像 query DSL 的集成以及 Maveridol 的集成，这时我们关注度会比较低一些。
好，这是我们简单的从这里面的概述去了解一下我们的 spring day 的MongoDB，其实我们可以通过在这里面有对应的learn，我们这里面有个参考文档，我们点击参考文档，我们可以切换到这里面的对于 spring date Mango DB 的一些文档的详细介绍，我们在这里面可以简单的过一下。这个文档还是比较齐全的，同学们在自己学习的这个过程中，也可以通过 Chrome 的一些自动翻译去快速的去浏览这个文档的内容，这样让我们快速知道 spring day 的 MongoDB 跟我们提供了哪些工作。
那么我们现在还是回到 PPT 好，我们接下来看一下 Sprint 的 MongoDB 的核心API，我们看这里面我们还是分了三部分，会涉及到注解，我们的 MongoDB 的 repository 以及我们对应 string put 提供跟 MongoDB 相关的一些内容。


首先我们看注解，这里面我们对应的是 enable Mongo repository 和 enable Mongo editing，也就是说一个是我们生成对应的我们 reposit 的这个代理类，另一个我们基于我们对应的 portal 实现的注解，我们通过我们的注解完成对于 MongoDB 操作的一个审计工作，这跟对应的 screen day 的 DP 里面的审计工程是类似的。当我们保存的时候，我们去扩展一下对应这个实体对象，它的创建时间和它的创建人，它更新的时候去更新对应的最后更新时间和最后更新人这些信息。


另外是 Mongo REPORTS，我们可以看到它其实跟我们的 GPT 和我们的一代色 report 的形成是非常相似的。这里面会有首先它的一个实体的实现类，也就是 simple Mango 的 reporsory 就是最基本的一个实现 report 里的实现类。其实我们手工定义的这些report，它默认都是基于这个 simple Mongo report，它的一个原生的对象来进行代理。对于这个 Mongo reporting 的，它依赖到 Mongo operation 和 Mongo 的 int information。对于 Mongo operations，这里面是我们对于 MongoDB 的 client 和 Mongo 的 template 进行一些包装，我们可以对 Mongo 数据进行一些读取。对于这里面 Mongo entity information 是我们通过我们的 Mongo repository 构建的这些我们的 PODO 实体类，这些 PODO 实体类会通过 Mongo int information 进行包装起来，跟我们构成一些映射关系。


对于下面我们去真的去通过 Mongo REPORTS 构建 simple Mongo report 这个 c 类的过程中，我们会使用到 Mongo REPORTS factory 和 Mongo reported factor b 去生成我们对应的这个代理的 repose 类。


好，这下面是我们的对应 spring boot 下面的相关的一些 auto comparison，这里面其实还有其他的营销跟 MongoDB 相关的扩展，我们这里面列出了比较有代表性的四个。首先我们看我们对于 Mongotb 本身，它也是一个独立部署的一个Server，像我们的 MySQL circle Server 或者是 elecserts Redis 这样是一个独立部署的，那么这里面我们也可以通过集成的方式集成一个MongoDB，方便我们去测试运行。这里面我们可以把它理解成集成的我们的关系型数据库的 HR 数据库，我们可以集成到我们的程序里面，方便我们进行我们的开发测试的一些体验。


另外是 Mongo auto configuration， Mongo auto confusion 是我们基于已有的一个 Mongo 服务来去构建我们对应的 Mongo client 相关的一些操作。下面是 Mongo date auto confusion，对于 Mongo date auto competition 就是它其实是依赖到 Mongo auto compilation，也就是依赖到对应的 Mongo 的Plexin， Mongo 的 JDBC template 就是 Mongo template 这些操作构建跟我们 spring day 的 Mongo 相关的一些信息。


最下面是 Mongo REPORTS 的autocomplication，也就是说我们通过这个 autocomparison 来构建我们定义的这些repository，它的一些实现的代理类。那么我们可以通过我们的 Sprint Mongo 源码来去看一下这些类的实现。


好，我们现在切换到我们的 Sprint Mongo 的源码，在这里面我们可以看到 point 文件，对于 porn 文件里面它还是它的 point 对应的 spring day 的point。这里面是有三个模块，其实我们重点关心的还是 spring date MongoDB，我们知道这个是进行我们的 MongoDB 模块的发布，另外这个是基于一种测试的方式，这个我们不用过多的关心，那么对于 palm 文件里面，这里面的 palm 文件我们就不过多的介绍了。


我们重点来看一下 Mongo 的repository，那么我们可以看到这里面的 Mongo reposit，它也是继承了我们的 pacing and sorting 的repository，也就是继承了我们 Sprint 的common。这里面实现扩展的一些方法，比如说这里面像 save all，我们还有一些 find all 相关的一些操作，这相当于是对 pacing and sorting 的一些扩展。
对于 Mongo reporter 它有一个默认的实现，这里面它对应的默认实现，也就是 simple Mongo reporter，我们可以切换到这里面，同时我们可以看到对应 simple Mongo reporter 它的一些源码的定位，它源码在定位到我们对应的整个是 MongoDB 这样一个包结构，下面是 repository 的 support 基于一个支持的一些类的提供。
那么在这里面我们可以看到它提供了我们的 Mongo operations 和 Mongo int 的information，从这里面我们可以看到对于 Mongo operations，它里面会包含了对应的 Mongo client 相关的一些操作，我们可以待会可以跟进去看一下。


其实对于 Mongo operation 这个接口，它默认的实现可以理解我们对应的 GDBC operation，那么它下面的实现有什么呢？它下面实现我们可以看到这里面有 Mongo template，也就是我们基于 Mongo 的操作构建一个模板类，我们去进行它的一些增删改查的操作，我们可以通过这里面去看一下它提供了哪些方法，我们可以看到这里面的 park 的 OPS 相关的这count，我们的 create collection 相关的一些操作等等，这里面提供一些聚合的一些操作。


好，我们还回到 simple Mongo reporsely，也就是说基于我们的 simple Mongo reporcy，它代理利用了 Mongo operation 和我们的 Mongo int information 它的构造的一些信息，进行我们的一些代理的操作。比如说我们在 C5 操作的过程中，最终我们去判断一下当前这个对象是不是新的对象。如果新创建的对象，它会通过 insert 方式操作，那么如果说它是旧的对象，也就是这个对象，嗯， ID 是已经存在的，那么这里面我们会使用save，也就是类似于对应的 update 相关的一些操作，那么这是我们看到的是我们的 simple Mongo repulsory。


那么这里面我们再看一下对应的，像我们如何去构造我们的对应的这个代理类，它是涉及到 Mongo REPORTS effect b，来看一下这个 simple Mongo REPORTS 如何去构建的，那么在这里面我们如果说不知道整个程序的结构，那么我们怎么去看呢？看这个 simple Mongo reposer 呢？它是被谁去创建出来的？这里面我们可以看一下它为引用，这里面能看到它涉及到是 Mongo REPORTS factory，我们点进来看一下，跟我们这里面的对应的是 Mongo REPORTER factory，我们这里面是 Mongo report factor，里面它会有涉及到 get reports base class，也就是说我们构建对应的 Mongo reposit 的过程中，它依赖的基础的 class 就是我们的 simple Mongo reposure。那么对于这里面的 simple Mongo reporter，我们可以看到我们再去跟一下。那么对于这个 Mongo reporter factory 这个类是被谁构造的？也就是这个工厂类，我们可以在这里面跟一下它的使用。


这里面我们看到是对应的 Mongo reporter factory bin，那么我们基于这个 factory bin 去构建出这个对应的factory，我们可以看到这里面是 get the factor intense，这个方法会把我们的 Mongo REPORTS factory 这个对象返回过去，也就是构建出这个bin，这样的话我们就通过一个 factory 和一个 factory bin 去构造出我们的 simple Mongo report 的实现，这就是我们可以简单介绍这些核心的API。那么底下这几个是我们跟 spring boot 相关的几个 auto computation。


这几个 auto competition 它其实并不在我们的 spring 的 MongoDB 这样一个模块儿里面，它出现了我们的 spring boot 相关的模块儿里面，这个我们是在我们介绍 spring day 的 MongoDB 初始化的流程容易介绍，那么接下来我们来去看一下 Sprint 的 MongoDB 初始化的流程，这里面初始化的流程我们就重点会介绍这几个 auto configuration，这个 embedded Mongo auto configuration 它其实跟我们生成一个嵌入的一个 Mongo 的实例，那么我们可以对这个 Mongo 进行一些读写正常改查的操作，这里面其实它重点的是生成一个 Mongo extra able，也就是一个执行的一个服务。


这里面我们可以看一下在对应的我们比较关注的是我们的这个集成的 model 和 auto communication，看它实现了一些怎样的一些Beam。对于这里面我们看它对于一些前置条件的要求是它是需要有 on class，也就是说我们对应的 Mango and setting 和 Mango STARTER。我们可以看一下这个 embedded Mongo 的 decline 的 dependency being factory post process。


其实我们在生成这对应的集成的 Mongo auto computer 的过程中，其实我们是需要生成一个对应的 Mongo Equuta，那么它需要对应的我们像 Mongo configure client 相关的一些内容，以及后面的是一些 runtime 的运行时的一些配置和我们当前的 application 的上下文。我们可以看一下在这里面我们构建了哪些 be 这样一个bin，它其实是需要依赖我们的 Mongo client，也就是需要依赖我们的 Mongo 的一个驱动driver，这里面其实是基于这个一样一个配置，它会生成一个对应的是 be infected post process，对应我们进行一些处理。


好，我们现在我们来看一下第二个，我们这里面是 Mongo auto configuration，那么对于 Mongo auto configuration，我们可以看到它里面实现什么呢？这是比较容易理解的，这里面我们构造出了mongoclient，我们通过这里面的是 mongoclient setting 的 builder customer，这是相当于是我们对于 Mongo client 的一些自定义的一些扩展，可以通过这里面去，也就是我们的一些 customer 的配置进行一些扩展配置。


下面是我们对于 Mongo client 配置的相关的一些信息，其实重点就是说我们通过 Mongo auto configuration 构造出 Mongo client，那么接下来我们来看一下这里面是 Mongo did auto configuration，我们可以看一下 Mongo did auto compreson 出了什么事情，这里面其实是一个循序渐进的过程，首先我们是有这个 Mongo 的实例，接着我们去构建出 Mongo 的client，那么现在我们来看一下 Mongo did off configuration，它其实引入了 Mongo did configuration 以及 Mongo did base factor the configuration，以及下面是 Mongo DATABASE backthree 的 dependency 的configuration，也就是跟我们的一些配置相关的一些内容。我们可以简单打开看一下，这里面我们可以看到构建它的过程是需要依赖我们当前的上下文，里面有 Mongo client 和 Mongo template，我们可以看到对应的 Mongo did 的configuration，这里面是构成了哪些？b、这里面首先是 Mongo Mapping 的context，也就是我们的映射关系在这里面去扩展起来，这里面还涉及到 Mongo customer 的conversion，也就是我们自定义的一些转换器，可以在这里面去看到。


其他的我们可以看到是 Mongo DATABASE factory 的configuration，在这里面我们构建出一个对象，也就是 Mongo DATABASE factors part，这里面它需要有什么要求？我们可以看到构建这个 Mango DATABASE fixes product 的过程是需要依赖 Mango Calendar 和我们的 Mango property。对于 mongoclider 这里面有一个要求，也就是说我们当前的容器里面只有一个唯一的 Mongo client 的一个对象。


其实跟我们在构建我们 GDP template 过程也一样，如果说我们需要通过默认的 auto competent 构建我们的 GDPC template，那么我们的 this source 只能有默认的一个，或者说我们指定一个primary，也就是指定一个主要的对应的 this source 或者一个 Mongo Grande，才能去生成我们对应的一些 Mongo DATABASE package support 相关的一些信息，那么接下来看一下是 Mongo REPORTS auto configuration，其实它整个过程也是一个循序渐进的过程，我们基于 MongoDB 实现的一些必应来构造 mongoreposit auto configuration。


那么我们来这里面去看一下 Mongo reporsory 的 auto comparison，这里面是 Mongo REPORTS auto comparison，这里面的实现也是比较简单，对于 Mongo REPORTS auto communication，它其实也就是通过 import Mongo reports 的 register 来实现了跟我们 reposure 相关的一些内容。
我们这里面可以紧紧来看一下我们比较关注的，也有比较熟悉，其实这里面我们可以看到它是一个 configuring extends，也就是一个配置的扩展，也就是 Mongo reporcy 的 configure extends 去实现了我们相关的一些信息，那么这里面还会有跟我们的一个注解，也就是我们的 enable Mongo repository 相关的一些信息，我们通过这个注解来完成。


这里面还有一些配置性的信息， enable Mongo reposer configure 信息，这个它的配置主要是表明一下，我们引入了 enable Mongo reporser，也就是开启了我们的 Mongo REPORTS 的一些配置信息。这个下面我们应该也知道它里面会有我们的 Mongo REPORTERY 的 factory 相关的一些配置的一些信息。我们可以看到这里面是 Mongo REPORTS effect b 和 Mongo REPORTS effect 和内容。


这里面我们还有一个映射的我们的document，也就是说我们跟 Mongo 映射的 document 是这样， document 一个注解，我们注意一下这个 document 的注解，我们看了它是在我们对应的 MongoDB core Mapping 的 document 下面实现，我们知道对于这个 document 可能还会跟其他的文档有一些冲突。我们如果说选document，一定要注意我们选的是对应的 string did mongo d b 这个对应模块包，下面的 document 包括 field 也是，对于 field 它也是我们指定的。在这个模块下面，我们知道对于 field 有好几个地方会涉及到了这个注解。field，我们可以在这里面去数数看一下，这里面像我们的是 MongoDB 的field，这里面有一代 search 的field，所以说我们在选用 field 的过程中，一定要区分出它是 MongoDB 的 field 还是我们的 USS 的field，不要弄混好。


看到这几个的话，我们其实就应该去了解整个我们的MongoDB，它简单的一个初始化的流程，这里面我们也是建立了我们对应的是 MongoDB 这个 showcase MongoDB 的模块。我跟大家去简单介绍一下我们是怎么去实现的这个过程首先还是看我们的 user 对象，那么基于这个 user 对象我们去实现我们的一些扩展，因为这里面我们并没有用过多的自定义的操作，切记就是说我们对于所有的 ID 需要指定一下这个ID，我们要注意它是使用的是我们的 spring did a notation 下面的ID，它不是我们的 GPA 的对应的 ID 等等一些信息，这里面我们并没有去显示的去引用我们 MongoDB 的document，但是如果我们不配置它默认会有一些扫描的应用。


这里面我们看 user repository，我们是继承了我们的 Mongo REPORTS rate，这里面对应的写是 user 和string，这里面还有我们初始化数据的操作，它跟前面的例子是很相似的，这个不过多介绍，那么对于 showcase 的 Mongo application 也是简单的慢慢方法去启动。大家可以参考其他的这些对应的 reports 去对于 MongoDB 的 reporter 进行一些运行，这里面我们就不展开运行了。好，现在我们回到我们的PPT，那么关于我们 spring day 的 MongoDB 相关的内容，我们就先介绍到这里，同学们，我们下一章节再见。

