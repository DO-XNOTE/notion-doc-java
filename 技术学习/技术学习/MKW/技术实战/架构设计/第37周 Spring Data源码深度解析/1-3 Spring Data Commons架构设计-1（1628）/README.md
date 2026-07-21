---
title: 1-3 Spring Data Commons架构设计-1（1628）
---

# 1-3 Spring Data Commons架构设计-1（1628）

[image](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/22c179b1-e29a-420a-8882-f0a9ea73e6dc/SCR-20240814-hlyx.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YSMRQKCT%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T232131Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDo3A981OA3BUefL7rDkh6VeUTAPVLmoLvn6vur5F53LwIgTApbUzVzrvmxvhnL0%2FqpfAdcu%2Fhy%2BBzabpBhRM359UcqiAQIxv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDLF6kmbym1XNHiJp4SrcA2OZzs4EFUA4%2BVmtCJTQq6Ip4mefaxh4w0Hyk%2BX1auRkh82Gmtyd4bEimTEWx%2BN%2BXZU5ecEKM13TWeozN6e0IKL5O6wmBLv10A2w1o%2F9JkK9wGSdTYVWMEZUNPJik8v96irXVgRw%2BwNJEkhbZvPvmj6ucs46wKhFNY%2BQHbaY5Y%2BJqkBFmUOuGia7RPK2cNR2UoRyku9dAa8zqS2MV8DFkB99q4%2FkO0g7xqNq98QMQ%2BTYF6goKuX1D5Sqh2rOedK%2F19HAeuGO%2F8frrsVjkqcJMd%2F9dg531pF%2BkoZ7Np7aOcKyMVja1KMmGHlj1g%2FltXrgx5%2B2o7Tz2KEp%2FaytYuhalzZKb9%2FvCSwYx857bgAwRuhyUdlWA8a%2Bv1FmXzAtMabaeepyKM2kFrBGbyVYEUocM3qtEnzz%2Bw4kK6UD6geEhZE6bMXE7gEkUWIyQAU7orfdv56UH7gvHrl8%2FqP2hOa8GfesXWvNeMWU9fAyTU8%2FZcLVA8VvnpD57offs%2FAkaWCeSh0iAmYNT6zi9BompyoGeNUxGFU14tL7RscPj1gq3k5CLAcxqKO9mG%2FsZuneezIDtlhno9f9008jZ1Di9l0DH8rZ3MRJvXB6oNS9DVba3OVVTsH1IIhIekYv8tAVMLW4%2F9IGOqUBZY261m9vI2Ig%2BA7UVPliEFxim0hvoxJnCiwCuh9jhPGlraqyfpzNqRvEhxSl4v%2Fg0V0pdkxywjfuwspqNsujrYTCkgZ8FhYuxc%2BlVT0vxpFg3AnMkhEsIGtCbmLG9ufKpstoBWoanSlUHBmmjIuMIjIXuW%2FrwcGSqz5Ku7YyQlKA13SDhnXCibh%2FIya6DNHN28wjt94iQNMhs8MTZH8mAqU5C1Jo&X-Amz-Signature=42d9030e4f7060a26a8f3c63fdf20d12924a7d3f9969648c855131a8552cbd03&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

同学们大家好，这一讲解我们学习 spring day 的 comments 架构设计，我们分三部分介绍，首先是 comments 模块介绍，这里面的 comments 模块是包括 spring date builder、 spring date comments、 spring date rest 以及 spring date bomb。这里面的 comments 是代表了我们 spring day 的模块里面相对通用的几个模块。另外我们需要认识 comments 的源码，这里面的 comments 我们更多的是针对 spring day 的comments，它默认的源码，以及我们是通过 spring date JPA 来一个案例演示。


首先我们来看一下 comments 的模块儿介绍，对于 spring date 模块儿里面的 common 模块儿，我们这里面可以看到它会涉及到 spring date comments、 spring date built 以及 spring day 的 BOM spring day 的 rest 这里面我们为了把整个模块能串起来的话，我们这里面还带上了 spring day 的 GPA 这几个模块，它们之间的关系是怎样的？首先我们重点要复用到 spring day 的builder， spring date builder 它是构建了我们整个 spring date 的point，基于point，那么它定义了这些依赖的一些管理依赖的版本。所有的这些其他的模块都是基于 spring date point 去验生，也就是说包括 spring date comments spring date rest 和 spring GPT，它都会在POM，也就说 Maven 的 palm 管理的过程中，它的 point 都是指向了对应的 spring date build 下面的一个 point 模块，这里面我们看对于 Commerce 跟 GPT 的关系，我们比较容易理解。 spring day 的Commerce，它定义了我们这些数据超出的抽象，这里面最典型的是repository， CRUD repose，或者是翻译者和 pacing and sorting 的repository。


Sprint d 的GPA，它基于 report 定义的，这自定义的实现，通过 GPA report 以及对应 GPA 相关的一些查询，实现完成了我们基于 JPA 的一些数据操作。这里面还有 spring day 的rest，它其实是把我们这些后端数据库操作相关的内容暴露成MV， seed 方式可以直接请求，这样的话我们就把整个应用，也就是说我们通过 STP 请求到我们的数据库，对数据库进行基于 rush 的风格的蒸删改查好，这是我们的源码结构。


这里面我们可以看到对于模块之间他们的版本其实不一样的。比如说对应的 spring day 的comments，这是 2. 5. 22. 2，这里面我们可以看到 spring date rest 是 3. 5. 2，其实我们还依赖其他的一些各个 spring date 下面的模块，它们版本可能也是不一样，这是怎么管理呢？ 5.


它就通过 spring day 的BOM，也就是 spring day 的BOM，它作为我们的一个列表清单，这个列表清单里面它会管理各个模块的版本信息，待会我们一块通过源码去看一下。


对应，这里面这是我们各个 common 模块它对应的源码的地址，其实它对应的模块我们可以从这里面可以看到对应，我们这里面的是 spring date，我们更关心的是 spend date point 以及我们 s spend date comments，也就是对应的 spring date Commerce 的源码 spring date bomb，也就是我们 spring date BUM 这样一个 date 地址。这里面我们看到是 spring day 的rest，这里面我们更关注的是 spring date rest web m a C 以及 spring date JPA，是对应的 spring date JPA，这里我们看到 screen day 的 g GPT，它并不属于 common 模块儿，放在这里只是给大家一个衬托，我们区分清楚 commerce 模块儿跟我们正常业务模块儿的区别。


但我们要是做正常的数据库的 CRU seed 操作，我们必须依赖对应的一些实现模块，也就是我们典型的这些数据库操作模块，包括 string day 的 GPA 或 string day 的Redis， string 对的 Mongo 或 string 依赖的色子，都是我们操作的一些典型的数据库操作模块。我们现在看一下 Commerce 模块，它定义了哪些相对核心的一些概念。在这里面，对于我们的数据操作模块的repository，这里面最典型的reports，我们看这里面是 CRUD 的 report 和 pacing and sorting 的reporsory。我们知道这是一个正餐改查的我们的操作库，另外一个是支持分页和列表查询的一个分页库，这里面的 report 跟我们常规在开发过程中设计的 d o 是有些类似的，其实我们可以对应的什么什么 d o，我们跟这里面 report 也可以做到一个映射的关系。对于 reporter 里面，它还提供了想要 4 编程的一些report，这里面像 eractive 的 CRUV reposary，同时是对 RX Java 也做了支持，这里面其实它支持了 RX Java 的 123 都支持进来。因为 x 加法一我们现在用的比较少了，所以这里面只列出了 x 加法 2 和 x 加法3，这是我们的reports，也就是可以理为数据操作库。


另外我们在堵门层，也就在领域层的话，这里面定义了一些约定，或者定义了一些必应的规则，比如说这里面配置 pitiable 和 RD 的able， slice 和salt，这里面我们看对于我们通常 testing and sorting 的reports，我们获取到的一些对象，也就是我们一个分析的对象。对于分页的对象，我们还支持一些审议，对于我们数据库操作会支持一些审计操作。我们对应的是 RD able 的一样一个模型的接口，这里面会涉及到我们的创建时间，修改时间，创建人和修改人等等。


这个 slice 我们可以理解为查询的分片，我们如果说对于分页查询要求没那么高，我们更需要对应的一个列表，我们可以基于 slice 的 Intra 的查询。 sort 就是我们支持排序的各自的一些参数。另外我们看一下它还提供了一些比较关键的注解，这里面的注解我们看最重要的，这里面是 i 的ID，这里面我们要知道这是 string date Commerce，他电影的注解，这些注解跟其他模块的注解其实并没有什么太多关系。如果大家了解 hapnet 的话，我们知道 hapnet 也有对应的一个Sid，这两个是有一些区别的，嗯，同时还有一些其他的像注解，像这里面是 last modify 这个注解的说明，对于我们的一些模型上，它用来说明我们最后修改人，这里面是最后修改时间，这是创建人，这里面是创建修改时间，这也就是创建时间。


这里面我们可以看到还有一个version，我们可以理解为是我模型修改的一个乐观锁，我们在数据操作的过程中，如果修改的时候，我们需要去判断一下我当前获取的对象是不是最新的对象，如果说不是最新的对象，我们修改的时候进行报错，进行乐观手，我们重新查询到最新的对象再进行修改。这是我们基于 version 实现乐观数的一个效果。


好，这里面我们能看到了这些各个模块的介绍，那么我们先简单去看一下刚才提到的这些模块。好，我们先看一下这里面的是 spring day 的builder，对于 spring date builder，那么其实这里面我们看到里面有两个子模块，我们首先点开我们的 palm 模块，这里面定义的这两个子模块一个是result，一个point。这里面其实我们重点关注的是 power 的模块儿， power 的模块儿，我们看 spring date point，它里面只有一个 power 文件，这 power 文件去规定了所有其他的 spring date 模块儿所依赖的第三方依赖的一些版本儿。我们在这里面看到这里面我们对于它的模块名称，也就是 string did point，那么它的 point 是 string the builder，也就是对应的一个 root string did builder。


对于下面我们看一下这里面定义的一些内容，这这里面会定义的一些 property 属性，简单看一下我们很容易理解，比如说这里面的是我们的 commerce io 的版本，我们的瓜瓜的版本以及 Jackson 的版本和其他招的 day 招的 time 这样的一些。这里面还有 unit Kotlin 以及 Lockback Lombbook，这里面query， DSL 等等，这里面包括x， Java 的 123 的各个版本。通过这里面我们可以看到其实在 spring day 的point，它其实是定义了我们这些外部依赖的这些版本。那么好，我们基于这些版本我们可以理解它其实是在我们的 dependence manager 里面进行一些管理。到这里面我们看到 depends management 里面对应的我们这里面的一些 Rector BOM 相关的信息，这里面是 string framework bomb，可以看到这个BOM，也就是说它对于依赖的一个总结。下面我们看涉及到 Kotlin 这样的一些依赖包等等，也就是说我们在 spring day 的 point 里面去定义了这些外部依赖的一些版本信息。


看到了 spring day 的builder，那么接下来我们看一下这里面的是 spring day 的common，对于 spring day 的 common 的话，这就是我们常规的一个炸包，我们看这里面对应它的SRT，下面是有对应的 Java 代码和 Kotlin 相关的一些代码，那么这里面我们可以看到它还有对应的 test 的代码。


对于这里面我们重点关注的对于 spring day 的comments，它的 point 是 spring day 的 point 在里面对应依赖的版本，这里面它也会扩展到一些自己所特有的依赖的版本，我们可以看到它依赖的像 spring core， spring beings，因为在我们在这里面是继承 point 的 spring date， point 已经把这些版本信息包含进来了，所以我们只需要把我们的依赖引入进去就可以，不需要再去强制的指定版本信息，这是我们看到的模块。当然对于 spring day 的comments，它定义的内容也是比较重要的，待会去详细看一下 spring comment 这个 bottom 的内容。


接下来我们看一下 spring the comments 它的一个具体实现，也就是这里面是 screen day 的 comments 的对应的 string day 的 JPA 对应 spring day 的JP，这里面我们看到它是使用的point，也是 spring day 的 point 在这里面对应的它的内容。我们看这里面定义它依赖，因为我们知道 stream d 的GPT，它底层的实现是基于 Hypernet 实现的，这里面会有对应的 spring OM 和 spring Hypernet 相关的实现的一些内容。


通过 spring day 的GPA，我们可以进行我们对于关系性数据库的一些增删改查。这些数据它只是局限于对应的reports，也就是 DAU 层。他如果说把这些 DO 的服务暴露给我们外网，就是通过我们 ITP 请求去访问到，这里面会涉及到 spring day 的rest，这里面我们看到 spring day 的 rest 下面有几个模块，这里面首先是 spend rest call 和 spend rest Web Mac，它去定义了几个基于 repository 相关的Controller，可以实现对于 reports 它一些增删改查以及它的特殊的一些查询的匹配。同时它还提供了一个UI，也就是这里面的是 rest s l x player，它会定义了一个通用UI，我们可以直接对于我们 repose 暴露的这些接口进行一些蒸删改查。这里面是基于 rust 规范，就说我们是 post put 相关的一些操作，这是我们 spring day 的 rest 的这个代码的一个情况，那么后面我们可以看到最终对应的是 Sprint 的BOM，那么我们看一下 Sprint 的 BOM 是怎么实现的。


对于 Sprint 的BOM，下面有一个模块叫 Sprint BOM，它并没有直接用我们最外层的成报的，这里面定义的是 Sprint bomb point，最下面是 Sprint 的BOM，也就是说其实我们依赖的内容实施我们对应的 Sprint bomb，这个 Sprint 的 BOM 下面我们看它定义的一些依赖，也就是这里面定义的一些依赖规则。比如说这里面是 dependency manager，应该是基于字典排序。首先是 spend Accenture，这里面我们的版本是 3. 2，这里面是 spend comments 是 2. 2. 5. 2，我们可以看到 spin day 的模块下面各个版本它的版本号可能是不一致的，这里面是 cost base 是 4. 2，这里面 index search 也是 4. 2. 2。 2. 还有一些 ZU 以及GDBC。


好，我们这里面是 really single，这个是跟 GDBC 其实是在相同的一个模块。下面，后面是我们的 GPA Mongo DB 应用或解释一个图的一个数据库，这里面我们注意还有一个 r to d b c，也就是说你就基于 active 的一个关系性数据误差的，因为这个现在大多，尤其是 MySQL 现在应用还不是很广泛，所以说这个用的是比较少。
下面有 Redis 和这里面是 spring day 的 rest Web Mac 相关的内容，这里面是我们刚才提到的基于我们 spring day 的 rest Mac 提供的一个UI，待会跟大家去演示一下。好，大概也就是这样一些内容。我们现在回到PPT，那么接下来我们介绍一下 commerce 源码，对于这里面的 commerce 源码，我们就重点的去看一下 string 对的comments，它这个源码里面涉及到我们比较关注的一些内容，这里面打开我们 spring day 的comments，我们可以刚才我们的 palm 的这些规则我们简单介绍了一下，现在我们去打开这些包结构我们可以简单地去过一下。


首先这里面我们看到它的annotation，也就是我们的一些注解，在这里面的注解我们可以看到刚才提到的是ID，我们的 create by 和我们的 create date，也就是我们创建时间和创建的日期。我们的创建人，这里面我们标记对应的一些创建人。


下面我们看这里面是我们的最后修改时间和最后修改人，这里面还涉及到我们的刚才提到一些乐观锁等等，这是我们常见的一些注解的情况。这里面是我们看 RD 填，也就是说跟审计相关的一些信息，审计相关的信息会当我们程序执行的时候，如果说我们程序配置了对应的 create by 和 create date，以及 last modify 和 loss modify date，它在执行的过程中会把当前的一些 3L 信息注入进去，比如当前的修改时间，当前修改人他可以通过跟 spring secret 相结合获取到我们当前 3L 的登录人的一些情况。


我们再看这里面的是一些读梦相关的一些信息，我们可以看到是 auto table 这样一个接口，我们可以看到基于这个接口我们能获取到当前的创建人和我们准备是设置创建人，我们就要获取到当前的创建时间等等一些信息。我们再看一下是 Audit aware，我们可以看到它可以基于通过实现这个接口获取到我们当前的这个Audit，也就是我们获取当前登录人信息的一个相关信息。我们可以看到是对应的配置，我们获取到一个配置对象信息，配置信息它是继承了slice，它获取的内容是什么？它可以获取到我们 get number 和 get size，也就是说对于 slice 它比 page 更抽象异常，我们可以获取到对应的一些 list 列表信息。


看一下对应的配置信息，这里面我们可以包装成一个配置对象，这里面我们获取到 total 配置分页。那么我们有没有去想过对于这个配置和 slice 它的一些区别是什么呢？其实它的区别就是对于 slice 的话，只会关注我们的行数是多少，或者说我们总共获取的 size 内容是多少，并不关心它的总数，也就是 total 配置或 total element。
并不关心这个记录的总数，因为通常我们在关系型数据库查总数的时候，其实这个性能消耗还是比较大的，甚至我们在执行 count 这个 SQL 语句的时候，甚至比进行我们列表查询的数据花的时间还要多。所以说这个时候如果说我们返回 slice 的话，我们不会去进行 total 配置的查询，这样的性能会好一些。


我们看这里面还有对应的 page able 相关跟我们定义的规则，还有对应的一些实现，比如说我们的配置MPL，对应的实现以及我们的配置request，下面我们看这里面还定义了一个 range 对象，我们可以定义一个范围，一个概念。好，这是我们看的 domain 相关的一些内容，这里面还有比较关心的，也就是repository。在 reposure 里面我们看到这里面是我们提到好多次的repository，以及它 reports 的实现，对应的 CRUD reports 以及我们的 pacing and sorting 的 repository 这样一个，其实对于这些 repository 它有各种不同的实现的一些支持。


相比较的，我们再切到 string day 的 GPT 的原貌可以看一下 string day 的 GPT 里面，我们可以看到是最主要的，我们要关心的是GPT，那么 GP reports 它是继承了 pacing and sorting 的repository，这跟我们刚才提到的它们对应的一些抽象的关联起来，那么基于 GP reporter 它底下还有对应的一些实现。我们可以看到它这里面是基于 RT label，也就是说我们支持一些审计的posery。


其实我们应该注意到这些像 reposry 它的一些子接口，它并不是在我们 string 的 GPA 的核心，也就是我们发布的源码里面，它是对应的simple，也是可以理解为样例。我们可以切进来看一下，其实这个一些 report 的样例，它是属于一个 test 包，支持我们实现功能的一些演示的一些功能。好，这样的话可以大概了解我们自 sprint 的comments，它的嗯，源码工程的一些特点。接下来我们回到PPT。

