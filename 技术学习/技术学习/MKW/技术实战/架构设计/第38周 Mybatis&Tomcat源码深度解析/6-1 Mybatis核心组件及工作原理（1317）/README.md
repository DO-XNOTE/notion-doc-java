---
title: 6-1 Mybatis核心组件及工作原理（1317）
---

# 6-1 Mybatis核心组件及工作原理（1317）

同学们大家好，这章节我们来开始学习买 Badcase 的面试题深度解析部分。 my Badcase 的面试题通常集中在核心组件和工作原理，那么回答买白色的核心主键有什么？买白色的工作原理是怎样的？我们简单的就把它拆分成两部分，先回答 my best 常用主键，比如说收入 session 这些使用频率比较高的，或者 session factory，那么对于我们构建 session factory 的方法，那么第二我们就来去学习一下 my best 组件级工作原理，这些在前面也都跟大家介绍过，那么我们来为了回答这个问题，我们再来回顾一下。


首先我们来看这张图，对于 my badcase 来说，它宏观的结构，我们可以把它区分成像这里面接口层、数据处理层以及基础支撑层，那么对于接口层，也就是我们作为一个对 mybyte 的使用方，我们其实作为 client 端去调用 mybytes 去执行。那么对于我们经常使用的接口，对于这里面有数据库的增加删除，我们数据查询以及修改，也就是这里面我们是通过了 my badcase 的 SQL session，已经对应它的一个增删改查操作。


当然我们可以通过 super session 获取到我们对应的一个Mapper，也就是通过生成代理的方式得到一个 Mapper 对象，那么 Mapper 的代理类进行我们数据正常改造和操作。在这个过程其实我们知道这个 map 的代理立项，它在操作过程最终还是会依赖 SQL session 它的一些 API 进行信息的一些维护好，这是接口层，那么接口层我们再看一下数据处理层，那么数据处理层的通用方法，也就是我们通过接口层调用对应的增删改查方法，我们会映射到对应的 statement ID 执行我们相关的搜索操作。
在操作的这个过程中，我们会涉及到参数映射、 SQL 解析、 SQL 执行以及结果处理和映射。对于参数映射的过程中，我们会使用到 permit handler 这样一个核心的组件。对于 prime 的handler，它能做的事情像我们参数隐私的配置，参数隐私解析以及对应参数类型的一些解析。解析完成这些参数会对于我们的 SQL 进行解析，在 SQL 里面，这里面会像我们通常的 SQL 以及会配置，在 XL 里面，我们首先需要对 MVR 进行解析，生成我们 SQL 语句的配置，把 SQL 语句的配置解析完成以后，我们对于 SQL 语句进行解析的内容。这里面解析是对于买 badcase 支持一些动态的 SQL 语句，比如说我们支持 for each，支持 if test 等等这些操作，那么我们对这些动态语句基于我们的参数进行解析，生成我们真正的SQL，那么这里面会使用到我们的 SQL source 这样一个对象，也就是我们的 SQL 原始的信息。我们解析出真正的 SQL 信息，就需要进行我们的 SQL 执行，或者执行的逻辑通常会依赖到我们的 IQ Ator。


在 my badcase 里面， IQ Ator 真正处理的执行者，它会分为三种，这里面我们列出来像 simple Q1，点 BYTE OKR Extreator。通常我们来执行的过程都使用的是 simple acute。在某些情况下，我们为了提升效率，对于一些批量操作，我们可以采用 best Creator。那么在使用这些具体的执行 IQ 的之前，我们会有一层 cat a Q2 进行一层代理，我们基于 cat a Q2 的这层代理去完成我们这些缓存的一些实现。那么 SQL 执行的过程中，我们获取到对应的 statement 执行，生成 resells set。那么 resort set 是如何转化为我们的 Java 避孕对象的？这里面的处理就涉及到 result side handler，那么对于 result side handler，他做的事情主要就是对于我们的结果映射的配置进行解析，把配置进行转化，转化完以进行一个数据的拷贝。这里面我们通常会在 XL 配置的过程中使用 resort set 或 resort map 等等进行一个映射。那假如说我们没有配置上的 map 的话，我们也可以直接指定一个 Java 的类型，一个type，那么买 BYTE 在执行的过程中，它会把我们 SQL 执行生成的字段信息跟我们对应指定的价，并进行一个反射的映射，我们通过字段和属性的一一映射完成对于数据的转化，那么这样的话就完成我们整个数据处理的过程，这里面我们看涉及到主要的这些组件。


这里面有 Permeter handler，我们的 SQL source IQ Ator 以及 sort handler，它分别实现了对于参数的映射、 SQL 解析、 SQL 执行以及我们结果处理和映射。那么这里面完成这些操作有一个前提，也就是说我们的一些基础支撑，我们的基础支撑是完成如何对于 XL 的配置解析，以及对于注解的解析，以及事务管理、连接磁管理以及缓存的机制。通过这些基础支撑跟我们数据处理的逻辑这样完成对于我们一个 kind 层接口的暴露。


所以说我们在真正使用 mybyte 的过程中，我们好像关心的只有接口层的一些API，这里面涉及到supersession，或者说我们 get Mapper 得到了 Mapper 对象，那么我们基于这些信息完成对于 my badcase 正餐改查的操作。其实对于底层的这些依赖，对于我们是做了一层屏蔽，那么我们在学习源码的过程，当然需要把底层的依赖分析清楚。


下面回顾了买 Badcase 的宏观的一个基础架构，这里面的接口层、数据处理层以及基础支撑层，包括它在执行的过程中一些关键的操作。那么接下来我们再基于它这些核心的一些组件，我们来去熟悉一下它的一个工作的处理流程。那么在这里面我们来还是看到整个处理过程所涉及的内容。这里面首先会初始化我们的配置文件，创建 SQL session factory，获取到 SQL session，获取map，通过我们的 map 的代理对象进行 IQ 的执行。再接下来是我们处理数据的炒作的请求，这里面是 statement handler，那么在这里面处理的过程就涉及到了 JDBC 原生的一些操作，最终返回的结果，进行我们的结果的处理。


那么我们大概了解这主要的几个步骤，我们来详细看一下执行的过程。首先初始化配置文件，我们这里面会创建一个 configuration 对象，这个 configuration 对象它操作的内容主要是对于我们的 badcase config x 面进行解析，解析买卖的咖啡盖里面的这些通用的配置，这里面涉及到我们的 setting 配置，我们的排给音，我们的别名等等好，或者是甚至包括我们的 data source 数据源。但因为现在我们买 Badcase 通常是基于 spring 共同使用，那么关于数据源的操作，它会委托给 spring b 来去处理。
那么接下来大家处理完买 BYTE config 里面，这里面会指定我们的买 map 的 XL 目录，那么接着去执行我们对应的 apple 的XML。 map 的 ML 里面是记录着我们各种的不同对应 Mapper 信息的一些 SQL 执行，这里面我们通过 Mapper 的命名区分成 name space，在不同的 name space 里面进行我们的select，update，delete， insert 的操作，指定对应的 statement ID 进行一个 SQL 的唯一标记。


那么在这里面初始化完这些配置以后，我们就要创建我们的 SQL session factory。这个创建 SQL session factor 的过程首先是依赖我们的configuration，这里面我们会有一个 SQL session factor builder，我们基于 SQL session factor builder，通过 configuration 作为参数，就能生成我们对应的一个 SQL session factor 的对象。对于 SQL session factor 的对象获取到以后，我们接下来做的就是获取我们的 SQL session，这里面我们通过 open session 的方式得到一个 SQL session 对象。
其实我们看到 open session 其实跟我们盖的 collection 其实有些类似，通常我们可以把我们的 GDBC 的 collect 链接跟我们的 SQL session 进行一个映射的一个对比，这样我们得到 SQL session 对象，也就获取到了操作数据库的一个handler，也就是说我们可以通过搜索 session 完成对数据库操作的调用。那么这里面我们可以看到 SQL session 的过程中，它会通过 SQL session factory 调用 open session 的方式获取。


这里面会涉及到哪些信息？首先是事务 GDBC 操作，通常我们会涉及到事物，这里面事物有GDB，seed，纯 sex 以及通过 spring 管理的这个transex。这里面是我们知道我们在使用 spring 的过程中，它提供了一层对于四五的抽象，纯这个 45 的抽象，它包装了对，包括像哈巴 net g，d，b， c 买白太子这些 45 的处理方式统一使用纯的方式进行处理。


那么在有素的管理以及我们的 IQ Ator 真正的执行者这里面，我们只列出了我们的 simple ACUTE，刚才也介绍到了对于ACUTE，它的实现还涉及到了 best acute 和 resume ACQ 执行的过程中。其实我们这里面会涉及到一个 SQL session，一个默认的实现，也就是我们的 debug 的 SQL session。对于 SQL session 这个接口，其实它实现了多个实现，但最终执行的过程都会依赖到我们的 debug 的 SQL system。比如说我们这里面会用到了 SQL template，那么 SQL template 它是对于 SQL session 的一个实现， SQL template 实现依赖了 SQL session 的代理，最终还是执行了 debug SQL session，我们得到 SQL session。在我们现在买 BYTE 的工作过程中，我们通常直接使用 SQL session 操作我们 statement ID 的方式也是比较少，我们大多会定一个接口叫对应的一个什么Mapper，我们基于这个接口生成一个代理类去进行执行。那么我们用 SQL session 现在最大的工作就是 get Mapper，当然这个过程很少需要我们手工去执行了，因为像 my best 提供的 my best 跟spring，Mybest， spring boot 相结合的这些插件的过程中，就替我们自动完成了这个过程。


所以说我们在使用 Mybyte 的过程中，大多是只需要调用我们 Mapper 成这个 map 的接口，那么基于这个 Mapper 的 b 呢？完成我们数据库的操作，这里面我们通过 super session 的 get Mapper 操作，得到一个 Mapper 的一个代理类，其实这个代理类的创建过程是通过我们这里面 map 的 Prox factory 去构建的，我们可以看到整个生产生成的过程，他们通常用到了好多跟 factory 相关的这些后缀，这里面像 supersession factory，这里面 Mapper pockets factory 等等。


对于 map 的protofactory，它执行的过程，其实首先它会依赖到我们的 ACQ ATOR 在 map 的must，也就是说整个一个代理类，它需要把我们执行的这个方法进行一个抽象包装，抽象包装的方式就是抽象包装成一个 map 的Max，也就是说执行的这个方法是被我们的 map 进行一个包装的过程。


最终我们在之前底票的资扣 session 的过程中，我们通过 map mask 获取到一些信息，比如说这信息对应的 statement ID 和它的一些参数，以及它执行返回值的内容。那么这样的话基于最终还是基于我们的底配的测过 session 得到我们相关的一些信息，那么现在我们执行到了我们的 map Prox，那接下来就看一下我们真正一个处理的过程。


真正处理的过程这里面依赖到 statement handler，它最直接的实验也就是 simple studio handler，它处理的过程会涉及到我们的一个 zoating schema handle，也就是我们的一个路由处理，在路由处理的过程中，它会根据我们对应的 type 会区分成我们。这里面是 simple 斯特曼 handler 和 paper statement handler 以及 corable Steam handler。最终的过程还是对我们的一个 statement 进行一个执行，这里面我们特意指出了对于我们的插件的使用，我们会在 intercept team 里面把我们的 plugin 进行一个应用，最终来处理，像 proper handman 的最终执行，我们 handler 边query，那么得到我们的处理结果以后再进行 result handler 的一个调用，也就是说执行完得到 resource set。


我们把 resource set 进行一个包装，也就是把 Resso 通过 resort handler 把我们的 resource set 转化为我们在买 badcase 定义的过程中，返回值一个对应的 Po go 的类型，那么介绍完这些的话，对于买牌子的核心主见解，基于工作原理给大家带来一个新的回顾，希望大家能更深入的去了解 my Badcase 的核心组件以及它的一个工作原理。好，那么 my Badcase 核心组件及工作原理的内容我们先介绍到这里。

