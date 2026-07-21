---
title: 1-2 Spring Data框架概述（1547）
---

# 1-2 Spring Data框架概述（1547）

[image](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/27ab2789-0e9d-48b2-9ad0-07972b90d86b/SCR-20240808-slpw.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RXDGHGIR%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T232125Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIETqyL0J4PQZwGVd9fgjV8epRmdENi8Yx8QS2HSp5TCmAiAGnz5ODhz3bXAOgpij0A2brLPGYlATimX48Mhxxe8ImSqIBAjG%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMotZSY3eIakylEEphKtwD4tCq4WM%2FGpyhsteLiSIEgml3E2xyqM3NS%2F7XIoxCOALy3iXug6fRXcs4UCn%2FGQVClTzZpoobpZfqSKkYS7IGkr0mSlRj7%2BsQZWmteKkg4CpodTgzPo5z4RrS7ntTLFyOOqx0L29tnEglByr3PFH07U64rrxD2iVhEE85tRoTjFFP9GVjEKo63CBfmyTa75NooKdlGS4RTn5Onrf3%2F8gXQzrJ%2FMWsukh3WN946IW3dLi39PMtt6iiPJ39IXaGKj12SX%2FIforG5kRyryTyeVxvOhp43q1t7uj7n3vvZjqBuVv9jWB8aJVji8SDYfcERM1gjrRkmkH2Wcua9FgDR2D%2BNkndpTNQeZ3Bgf70OzZX13lCVeS2t26fblkqslmzwvfvPzLBgRar4tzCBXfbz5vuOJraPESUpxn0tcr%2FAZ3Gt1Rctv%2FrF60Lv8yQlq6z2y2qiC4430fLxjtoBlMrhufepKfa2MbM4Bae1pWy19ecB81QRDbVXVkE0eythwttevmzK7r%2FfzYhcnleRO7b3I3OzXv7nJnGf8Ll%2Foexh181mztN4qmRZ4DqF%2FOWuOCK8ZWST2XHOiq%2B9WXnwoOh6IW93OE7yxEN6pRcznD825C6go0NcUIZr8GQhgN%2BLRYwq7n%2F0gY6pgHcm7b0QksmqMMZPYm2WF9ShHXnLvSMxCVQq2LxNmWKe5jnsLTxApY5Wlf63ANjF9z2JH709kdOY4JtPji6U0Lu%2BSv1HrE2MRubObqDl97QPB2wMgeLWQxlsoMPvX0a570qS1ih8CxKe%2FKFRLGHBq%2FoxTrYQv6qhBUfeFrebZ89WvuFkdLxW1CtKqIhN4M5tpSBsntda%2BDLRGmyNvgFKTZ6BkKugZwt&X-Amz-Signature=12cc74e34ded8aaf2b16586291f16faee1f771b464df25860f5a570cfb0e6456&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

同学们大家好，这章节我们介绍 spring date 的框架概述。 spring day 的框架概述我们会通过 spring day 的是什么？ spring day 的包含哪些项目模块，以及 spring date 模块的管理方式这三部分来认识一下 spring date。


首先我们来看一下 spring date 它整个一个架构的一个效果图。我们刚才已经介绍到了 spring date，它出现的目的是基于 spring 实现一套数据访问抽象的编程模型。这里面要问了，对于一套数据访问的抽象编程模型，这一套都覆盖哪些编程模型？其实这里我们最常见的也就是我们的关系型数据库，对于关系型数据库，我们通常会通使用 GDBC 买 Badcase 或者 GPA 或者海本。 net 这种方式进行我们惯性数据库的操作，这里面惯性数据库我们通常会涉及到像MySQL，Oracle， school Server， D b two 等等。我们可能在测试过程中，我们还会用到 H2 这样一个内存的关系型数据库，这是我们对应的关系型数据库。关系型数据库我们这里面基于 string date，它会通过 GPA 和 GDB seed 方式对我们进行一个包装。


除了关系型数据库，还有非关系型数据库，也就是 no SQL，那么 no 字幕它可能涉及的范围也是比较广的。这里面我们列出了像 MongoDB in u four j。当然我们这里面还会涉及到 elecserts 和Redis，这都是我们非关键数据库的一部分，那么对于 string date，它的这个抽象编程模型，我们可以看到它最顶层的抽象是一个repository，这个 repository 本身是一个接口，这个接口它标明了对应的子接口，它是一个数据库操作的reporsory，也就是一个数据存储操作的库。


对于 reporsory net 最直接的一个子类就是 CRUD 的repository，通常我们对于数据库操作无外乎也就是CRUD，也就是常说的蒸删改查，那我们基于最基本的增删改查扩展出了 pacing and sorting 的repository。 pacing 的 sorting 这里面我们比较容易理解。我们通常在做列表的过程中，我涉及到一些分页查询，对于分页查询，我们指定排序的字段以及我们 limit 对应的分页的数据，这里面我们可以基于 pacing 的 sorting report 来进行完成。


对于 CRUD report 和 pacing and sorting report，它也是我们在做数据库操作中，相对来说比较通用的一些基础的 report 操作的一些方法的集合，这里面我们可以看到具体的一些模块的实现。那我们列举了像 spring day 的JPA， spring day 的 Mongo DB，以 spring day 的 NEU 或j，它这是一个图的数据库。同时后面还有一些我们没有列取到的，比如像 spring date 的excess， string day 的Redis，这也是比较常见的。


对于 string day 的GPT，它基于我们的 pacing and sorting report 构造了自己的 GP reporsory， spring day 的 MongoDB 同样也是构建出了 Mongo repository，同时它也有对应的 Mongo template 操作的方式。


spring day 的 N u four j，它也有对应的 E u four j，对应的 reports 和 N e u four j 的template。因为 N u four j 它是一个图的数据库，这里面是 graphant 一个reporsory，这里面我们可以看到其实我们 spring day 的做的事情是什么呢？它首先构建了一层抽象，这些抽象我们基于 common 层把我们的 CRUDC responsory 和 pacing and sorting response 构建出来，通过这样来构建一些约束和规范，我们对于其他的一些数据源的访问方式去实现这种约束和规范，这样完成了我们对于各种不同数据源操作的方式，我们可以统一为 CRUD 的 report 和 pacing and sorting 的report，这样也就抽象出了我们抄录的方法。所以说我们对于 spring date 通过各个模块的实现。
DPS with the Mango DB and.


和spend，Electronics， Redis 这些不同的中间的实现，它完成了对不同的数据库的访问。像 RDMS 之后，我们的关系性数据库，我们的MongoDB，我们 Neo 化解，我们的Redis，我们 electronics 都可以通过我们对应的这一层中间层的 string date 针对某个特殊数据库的一些实现来完成。这我们大概知道了 spring date 它是做什么的，那我们看一下 spring date 它跟我们提供了哪些好处。首先就是 spring 对着它提供了一个强大的 report 和对象映射的一种抽象方式，这里面像 reports 有对应的 CRUD 的report，配置型的 sorting 就partner。那么对于一些对象映射的抽象包括哪些？比如说我们对这个配置sorting，slice，以及我们对于一些审计相关的一个模块的抽象，比如说我们的是 create by create date 等等。


接下来我们看一下 spring date，它提供了一套基于方法命名来实现动态查询的规范。这个其实创新意义挺强的，只要定一个方法的名称，就可以减少我们对于 SQL 语句的写入。比如说通常查询我们可以使用 find all，我们把整个表里面所有数据查出来，通常我们不会这样使用。另外我们可以 find by，比如 find by name，通过命名的模糊查询或like，或者说精确查询去查找一个对应的用户。我们也可以通过 find by between，比如说我们 between is 我们的年龄在 18 到 45 岁，它们之间的用户量是怎样的？这也就是我们通过命名查询的方式。


当然 spring date 定义这个命名查询方式还是非常丰富的，我们常见的这些 SQL 的操作方式都可以包含进去，比如这里面涉及到before， off 的 in 和 all 等等，都会包含进去。那么接下来我们看一下，它可以支持一些实体类，提供一些基础的公共属性。这个怎么去理解？其实我们对于通常一个对象，我们称作一个实体，或者称作一个独门，对于他来说都会有一些公共的属性。比如像ID，或者说我们的创建时间、修改时间、创建人、修改人以及当前这个订单的状态，或者说是当前整个实体的它的版本信息，Badcase，它都提供了一层默认的抽象，方便我们在做领域模型设计的过程中可以直接参考使用。还有就是对于我们的数据提供了一些透明的审计功能。


对于一些比较敏感的数据，我们对于每一次的操作记录我们都应该留档，通常我们会基于日志或者说操作记录来进行留存。那么对于一条记录，一条订单或一个文案，这个订单它是谁提交的，谁创建的，或者谁最后修改的，以及修改的时间，创建的时间和最后修改时间等等。这些事情通常我们在做业务系统的时候都是避免不了的，这也会给我们带来一些精力。


spring date GPT 或 spring day 的，它其实提供默认的一些审计功能可以通过我们适当的配置，在我们这条记录写入的时候，还有对应的我们创建时间以及创建人。当最后发生修改的时候，它有对应的修改时间和修改人。这个整个工程是不需要我们做任何开发功能的。其实这个透明的死机功能也可以称之为无需我们做太多的业务操作。


另外它还支持一些制定的 SQL 语句。我们刚才提到了基于 REPORTS 的实现，基于一些命名的查询方法都可以简化我们业务的工作量。但如果说有一些特殊情况，我们不能那样使用命名查询，或者说我们的 SQL 非常复杂的话，其实我们也可以支持的。基于 j p a 的话可以记词对应的 j p s， q r 语句，或者说是 native 语，也就是本地的 SQL 语句都可以进行执行。


另外我们在执行的过程可以通过 java config 或 x l 的方式方便集成了 spring 应用，当然这一点是毋庸置疑的，因为本身 spring date 它就是属于 spring 体系的，它跟 string 我们的应用集成的话当然是非常方便的。另外它还提供了通过 date reset 的模块与使用 MVC 可以 0 代码集成，这一点它也实现的比较巧妙。


当我们有了对应的一个reporstory，其实整个我们 Mac 到我们 service 到我们date，一个数据存储的过程可以 0 代码的实现。这里面其实也是利用了一些规范的原理，我们会把对应的 CRUD 相关的操作通过 rest 方式暴露出来，我们可以基于 STP 请求实现我们数据库的增删改查。


当然这一点大家一定要理解，有可能是我们暴露出来的这些结果是不合适的，或者说是我们不应该暴露的内容，是不是默认暴露出来了这些我们也可以基于一些配置来减少这种风险。另一点就是 spring did，它可以实验性的支持一些持久化操作，可以跨不同的存储方式。


刚才我们提到了 string date，它支持 JPA 或者 Redis 或依赖色子。当然我们在对于数据存储的过程中，可以存储在不同的存储方式，这对于 spring date 来说，因为它的这个抽象性，所以说对它来说并不是什么大的难事。接下来我们来看一下 string date 它包含了哪些项目。在这里面我们看一下 string date，首先它有对应的 string date builder，对应 build 下面它会有两个模块，一个是对应的 part 和业绩source。这里面的 part 模块是为了给其他的 Sponday 的模块提供一个标准，也就是说所有的 Sponday 的其他模块都会默认的继承对应的 string date build 下面的 partner 模块，同时 resource 提供了一些资源信息。


另外就是 string date BOM，此 BOM 我们就可以理解为我们的一些资源清单。我们在开发系统的过程中，如果涉及到依赖 spring date 的话，通常建议使用 spring date 的 BULM 文件， BULM 它可以理解为是一种依赖清单，这样我们可以减少对于一些依赖版本的控制。使用原理跟我们 spring boot 对应的依赖的 boom 的原理是一样的，它给我们规定了一些依赖的第三方的这些版本信息，避免冲突。


另一个就是我们 spring day 的comments，我们刚才提到 spring day 的comments，它定义了一些抽象，这里面像report， CRUV report 和 PZ sorting 的repository。
另外我们看一下具体的，这里面还有一个 spring day 的reset，它其实是跟 spring MVC 进行了一种整合，那么我们可以把对应的 spring day 的相关的这些 report 的信息暴露出来，我们可以直接通过 HT 的 resize 的请求，可以完成我们对于蒸山改查的一些操作。


接下来我们看具体的一些操作了，我们列出来形容 d 的electronics，什么 d 的 e line search，它其实是对 electronics 插入的一种封装，也就是说把我们 elecserts 原来我们使用是 rest client 或者是 high level rest client 操作的方式，包装成我们使用 reporsory 的方式，也就是我们像平常我们在操作关系型数据库正三改查的一种方式去操作我们的 elexsearch 以及我们的像 Sprint 的Redis。那么 Sprint Redis 操作我们通常也会使用 Redis 或者说其他的一些 Redis 客户端进行一些操作，这里面 spring date 把我们的 Redis 进行了一层包装，也可以非常方便的对于 Redis 进行基于模型的一些操作。另外这里面还涉及到像什么地的MongoDB，对于 MongoDB 我们会存储文件性的一些信息，它跟依赖设置的使用的方式有点类似。但是我们如果说涉及到更大数据量的查询，我们就是说对于搜索速度要求的话，建议大家用疑难测次。下面就是我们。


嗯，在 spring day 的里面最关注的也是 spring day 的GPA，因为我们在大多数基于 spring 的开发过程中，还是进行一些关系性数据库的一操作，所以说对于 GPA 的话，我们进行关系性数据操作是非常常见的。当然在大多数互联网公司的话，我们用 CPA 用的可能比较少一些，可能现在大家用买 Badcase 用的比较多，这里面其实有一点大家对 GPT 使用的了解程度不是很高，其实如果说大家对 string d 的GPA，尤其是 GPA 或 head 的了解比较清楚的话，我们会发现使用 GPA 是真的非常方便。也有同学会提到用 GPA 它生成的 super 可能对我们的运行效率不是很友好，但这里面还是基于我们使用的能力。如果说我们对于 stream d 的 GPA 和 Hypernet 它的实现了解比较清晰的话，我们也可以使用的这个效率上也会做得非常好。


后面的话我们还有一些没有提到，在这里面我们又只能用等等等的方式来标志了对于这里面像 spring day 的它的这些模块，它会包含官方的模块和一些社区的模块，还有一些正在孵化的模块。这里面我们把这些模块分为三部分。首先对于官方模块，首先是我们comment，这里面的 spring day 的 comments 肯定是 spring day 的官方去配置的。 comments 里面，这里面还列出了像这里面 spring day 的builder， screen day 的 BOM 以及 screen day 的rest。


为什么把这些定位公共，因为我们可以看到跟我们这些 office 相关的进行比较， small day 的GPADDBC， Redis 或什么 d 的MongoDB。跟这些比较的话，我们发现 commerce 它并没有干实际的事情，那么真正去干事的还是子诺date，GPT， b c 或 Redis 这些操作。


基于这样，我们看一下对于一些社区的，比如像什么 date 依赖色子优化界，以及我们这里面的阿帕奇的 solar 对于这些他们的区别。我们先看一下 common 这些包里面东西做了什么事情。此前我们知道斯曼迪的comments，它因为构造了这个 repose 的抽象，所以说这里面不管是 official 和我们的一些社区的这些 spring day 的模块，它肯定需要依赖comment。


另一方面，这 slow day 的 builder 出了什么事儿？其实 slow day 的 builder 定义了一个 slow day 的point，这里面像 screen day 的DPA，它们都会去依赖，也就是它的point，推荐我们去定义成 Sprint 的对应的point，这里面我们来看一下 spring 的BOM，那么 spring day 的 BOM 它的依赖于要滞后的。


其实 spring day 的 BOM 因为它的作用就是为了我们在开发的过程中定义好各个版本的依赖。也就是说当 string day 的BOM，它每次发布的时候，它会把各个模块最新的版本集成起来进行发布。这样的话我们开发过程中依赖的时候，可以依赖到对应的一个版本，能获取到我们各个模块最新的发布 release 版本。


那么子润地的 reset rest 这里面我们看也可以把它放到 common 里面，这个其实跟上面这些 common 的级别还是不一样的，其实这个 string date reset 因为它跟像 GPA Redis 它的定位不一样，在这里面也可以称之为对应的common，它这里面是把我们 spring day 的底层这些 repository 的实现包装成 spring Mac 的方式暴露出来。


所以说对于 spring day 的request，在开发过程中如果我们灵活使用起来，可以给我们带来很大的帮助，减少我们的工作量。不过这里面一定要有一点，我们一定要理解它，熟悉它，把它暴露出来的这些接口确实是我们应该暴露出来的，如果说我们把不应该暴露出来的结果暴露出，也就会造成一些信息泄露相关的风险，所以这一点大家一定要注意一下。那么接下来我们来看一下对于 string day 的模块管理，我们首先看我们各个模块，它是都会依赖 date builder 和对应的 date comments 这两个模块的。另外就是说 spring day 的管理的各个数据库的模块，它是各自的一些实现迭代，它们之间并没有什么相关的一些依赖关系。比如像依赖 s 和 Redis 对应 spring day 的elects，什么 date Redis 或 spring day 的DPA，它们之间是并行的，它们之间的开发的周期互不干扰， seed 开发进度快，它就会进行加快迭代，最终各个模块不同的 release 版本都会通过 spring date form 来进行统一发布。


也就是说我们在第三方开发的过程中，使用 string day 的 BOM 进行一个配置，我们只需要添加上我们依赖的组件，对于版本我们不用关心，因为这样我们依赖的版本都是最新的 release 版本。那么关于 spring day 的框架概述的内容我们就先介绍到这里，同学们，我们下一章节再见。

