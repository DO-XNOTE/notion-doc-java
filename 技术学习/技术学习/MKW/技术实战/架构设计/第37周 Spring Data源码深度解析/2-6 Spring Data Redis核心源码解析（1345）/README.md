---
title: 2-6 Spring Data Redis核心源码解析（1345）
---

# 2-6 Spring Data Redis核心源码解析（1345）

[image](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/54845111-28c3-49ff-857a-fd723838eb53/SCR-20240814-hzce.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QHNTIS3A%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T232136Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIAVEpTUDfluImuIBYTS5GbNKQYAjq6SQxJC%2BjH2Dxk9sAiB8lqldzmvMQBCJ%2FQepIgcmF1yovVg1M9xHNPwbX5b1HCqIBAjG%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMBujTzhAeKCVqOyuwKtwDabOfrtV3955ieBTe%2FlyKCrlvK8zuGGTrhDBp4Mh3jiInPtVZ5%2FNgFxAyYW2O%2Bn7uTtNm4OlSVRPpFGstkOA99RR1R4nFI0CXHocKdfFc9nd6H2pmu6kSPtb%2FwAkvD1xA8UPpO%2F%2BIux0Mvgm8gN3wk1flw0Aq4%2FLovvhjq8%2FM6eDk72unlnIfLNc1I81XJdn%2BajmuEW3fWBXp2kRleZTdbHQiqVeKos%2FuddPbYpayIlifx1Aas5m%2BDGTjjxL4kn%2BWe8Xsz43qmV%2FjcZMlkUqaRYv6ms4310wg0WSFVh%2FjXjCrmr%2FGWQgX%2FIRvQhFVhga%2FiJ6ihqJsSo7p2kukSvtefY6wTjKCl%2BSkfkC%2F0tPOua8%2FAk6CYvDfe4WM5bcJfBf4iPJcoTGBEu%2BxkYYgW4wdsEaVKy1c7cos%2BZosEi%2BDGsxl2%2B73bjk%2FnnJgcLNQHh92VCVzKOZJKl5%2FZ%2BB2muDsyvDnn3zWX9XzitDY7%2FZYQf9Z1ov049JAA0VHaDxzGRtsA8AFmzY8NHF2w5nM4FE3GCPs51QAOlHbQpkKiEIhQD3ct6ZhNaql%2Fxy8DZ7LiXiwPSJAW%2FiKfA66nbqUTDA1lG3rJogbJWmBOmUyhVIqYOdwCD%2FLLI9j3%2BZtmRwwq7n%2F0gY6pgFGrQHoeK6%2BoimNhG2%2BQDGWzuLPjUpoz7n2JqrNjTuPa0G%2BYDMzOl7bvL2dl4BwHQpQTVZ0cKnixUn7iXTDBCZquMT1ZnaN8nKiz4q2Uvpv6MJl2NBzMaLLy7wp36%2BG1AyXKWrifUjEYDhXCrkY0T8mRXSVFfJJA6jHIeSX2ZNdxrPCwynpEcT8fQLxXQ4Bn9TRtU6FlWizYNrDMPv7I1EuNqJeMisr&X-Amz-Signature=d1f08f460d010bb130c40c73c0fc9f72693d1df147a7420086b7ec9365380488&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

同学们大家好，这一章节我们来介绍 spring day 的 Redis 的核心源码解析。对于 spring day 的Redis，我们还是分三部分来介绍。首先是介绍 spring day 的 Redis 的源码介绍，我们也是通过 GitHub 去了解一下 spring day 的Redis。那么第二部分我们介绍一下 spring day 的 Redis 一些核心API，当然对于 spring day 的 Redis 核心 API 跟 spring day 的 j p a 它的核心 API 之间还是有一些区别的。


第三部分我们来介绍一下 spring day 的 Redis 它的一些执行流程。那么首先我们来看一下 spring day 的 Redis 涉及到哪些部分。对于 spring day 的Redis，它本身就是我们对应的 spring put 下面的 stream date Redis 这个 get lab 的一个工程，那么对于这个 gate 的工程，其实对于 spring day 的系列，它还依赖了我们这里面的是一个 spring day 的KV，我们知道 Redis 我们只通常会用做缓存，那么对于缓存的话我们更像一次一个 KV 的一个数据结构，那么这里面 Redis 依赖了 string day 的KV。这里面是我们也要介绍一下 string 的 KV 的情况。


接下来对于这两个 git 工程的设计的模块，我们主要还是 spin did Redis 和 spin did Redis K V 6，那么这里面还会介绍到我们在 spring put 里面会用到的 in starter，这里面是 spring boot starter did Redis，那么我们在开发过程中还是使用基于 stream 步骤的开发，就是引入 spring put starter did Redis 来去方便我们的开发。那么现在我们来看一下 spring did Redis 它的 Git Hub 上的工程。好在这里面我们可以看到这是 screen did Redis，对于相比于 spring day 的 JPA 和其他的一些模块，我们可以看到 spring day ready，它的 store 数还是相对比较多的，已经 1300 多，同时它的 fork 数和 Watts 数相对也是比较可观的。


那么这里面我们来看一下 spend date Redis，这里面它只有一个模块，也就是我们默认的 spin date Redis，这个模块里面并没有更多的指模块，对于这里面我们看一下 spin date Redis 提供了哪些功能。首先 string day 的Redis，它的目标也就是满足我们 spring day 的工程，让我们整个数据访问更简洁，更简单。那么对于它提供了哪一些future，我们可以看一下这些功能。首先词名 did Redis，它提供了一些我们开始底层的一些抽象。对于我们数据库的链接，它提供了像对于 Redis 的驱动，像 letter 和 Redis 这两个驱动都是支持的，我们可以二选一，那么现在我们还是更倾向于大家选 letter 式。


如果说我们需要一些 Redis 特殊的功能的话，比如Redis，它可能对于本身的 Redis 的驱动实现的功能更丰富一些，但是还是鉴于jadis，它的性能会稍微相对弱一些。现在我们主要是主流的还是优先选letters。同时它还提供了一些底层异常的一些包装，它会把原生的一些 Redis 相关的异常包装成 spring did access exception，这样方便我们统一处理。同时它还提供了一个Redis，一个template。我们知道 GDBC template 我们经常使用，对于 Redis template，它类似于 DDBC template，对我们常用的这些操作进行了一些封装。


好，这里面对于 Redis 的 signal 和 Redis class，它也是支持的，比如说我们的哨兵模式和我们 Redis 的集群模式，士兵的 Redis 都可以底座底层的一些支持，同时也提供了像 reactive API。对于 active API，它只能用在 letter drivers，如果我们选 Jadis 的话，是不支持这种方式的。同时比如说对于j，d， k 的string， json 和 spring object，包括 XL 一些 Mapping 的一些映射，我们支持一些序流化和反序流化的这样一种操作。同时我们可以看到对于我们的一些计数器，也提供了一些原生的一些支持。


后面的这些我们可以看到，其实我们关注的是最后一部分，它其实提供了自动的对于 report 的一个实现。对于 report 接口，它可以类似于像参考 GPT repost 功能进行了一个实现。当然我们知道 GPT 它属于关系型数据库，那么 Redis 它属于我们可以理解为是非关系型的数据库，它是个 no SQL，那么对于这里面主要还是基于 KV 的方式，那么对于 KV 的方式 string date Redis 我们可以理解为它是 KV 的一个具体实现，其实 string date 也还提供了一个 KV 的一个工程模块包，那么对于这个 KV 我们可以理解为它相对于 Redis 进行了一层抽象，这里面可以提供一些 KV 的操作。


我们可以看到对于这个 screen day 的KV，大家对它的印象还是比较少的，因为我们大多是直接在用Redis，那么这里面我们可以看一下它提供哪些功能，其实对于 string z 的KV，它的整个架构主要是为了对于在顶层上对于 KV 的这些 report 操作的一些实现，同时它也提供了一些动态的 SPL 的一些查询条件，同时它也支持我们一些自定义的一些 repose 一个coder。


在这里面我们可以简单看一下使用我们 Sprint 的 KV 实现的过程。如果说我们使用什么对 KV 使用的方式，其实跟我们在使用 GPT 的方式很类似。比如我们这里面是 person reporsory，我们在使用的过程中继承了 CIUD 的reporsory，这是我们定义的 repository 方法。那我们看一下我们的这是一个 my service，就是 service 的依赖repository，其实我们最终应该关注的是我们的一个实体，我们的president，那么对于 person 的话，这里面我们看到对于我们在使用 GPA 的时候，我们会这里面使用 add entity 或 add table 去进行修辞。


我们知道它是一个实体对象，那么对于 KV 的话，这里面使用的 k space 就是说这是一个命名控件，我们知道 KV 的命名控件，同时这里面的ID，这个 ID 它跟海伯纳的ID， GPT 的 ID 是不一致的，它是始终 day 的自己封装的ID。这 ID 表明 uid 作为这个 person 对象，它的一个唯一的ID，其实在启动的过程，这里面会使用到了 enable map reporter，它就会生成这样一个repository。


请支持我们的这些证删改查，但这里面一定要注意一下对于默认的 string date、 k v 它的实现，它底层的实现是用的 content Hashmap 去做我们 KV 的一些存储，当然我们现在的分布式系统操作肯定在内存级的 concern 的海信脉络，显然无法满足我们的需求。


所以说我们现在大多还是直接在使用 string day 的Redis，那么使用 string day 的 Redis 的操作的过程中，其实它也是对我们这个 KV 的一个实现，就是 KV 是更抽象的接口，我们使命对的 Redis 是基于 KV 的实现，那么基于 KV 的实现的话，其实我们刚才提到 KV 的功能 Redis 它都是具备的。


其实这里面我们更重要的一点是，我们在定义这个对象的过程中，我们可以直接把我们的数据存储在我们的 Redis 里面，但这里面我们需要去把我们底层的链接器构建出来。我们这里面比较抽象的是 Redis connection factory，对于 Redis 的连接器的这个工厂，它有两个默认的实现，这里面是 LETTERS 和 Jadis 对应的一个 connection 的factory。


好，那么对于这个 git help，我们的页面的内容就先简单介绍到这里，我们还是回到我们的PPT，接下来我们来去介绍一下 string day 的 Redis 的一些核心的API，这里面定义的这些 API 我们并没有去区分它是对应的是 KV 还是 spring day 的Redis，我们知道在使用 spring day 的 Redis 的过程中会用到这些相关的一些内容。首先这里面对于一些注解我们要关注一下，这里面注解是用的是 add enable Redis 的repository，另外还涉及到一个 Redis 哈希和 index 的，那么这三个注解分别是在我们使用 spend Redis 需要关注的。


其实我们使用 stream 铺的开发的过程中，其实对这个 enable 相关的这些注解，其实我们就可以不用过多的去关注，因为基于 spring boot 它的自动装配原理，我们可以自动的把 enable Redis reports 加载进来。


对于 Redis 哈希，我们可以跟刚才理解对应的 k space 这个注解是类似的，也可以跟我们艾特 entity 这个注解去进行相比较，也就是说我们对于 Redis 一个实体，我们通过 Redis 哈希来进行修色，标明我们这个对象可以通过 Redis 的哈希的这些数据结构存储在我们的 Redis 系统里面，那么同时对应的 ad index 它其实是对我们指定的属性来进行索引。


我们知道对于哈希我们只用 ID 作为我们唯一的 k 键，那么如果说我们需要查找属性，通过属性查找的话，我们必须对这个属性重新对子定义一些索引，创建我们的索引，那么这是我们注解相关的一些内容，其实我们开发过程中对于这两个注解是一定要万分关注的。


另外就是我们的repastry，那么在我们 repastry 其实跟我们在 spring day 的GPA， spring date， common 的过程都介绍到 repastry 或者 CIUD 的repasory，那么对于 spring date 的话，这里面也有对应的一些repastry，其实它这里面的 repastry 主要是对应的是 value 的repastry。


UKV repasory，对于 KV request，它的构建的过程，它会涉及到 KV request factory 和 KV request factory being，那么这是我们对于 spring day 的 KV 的关键的这些reposure。那么对于Redis，它分别有对应的 Redis report effect 和 Redis repeat effect mean 的一个实现，其实它们对于 Redis 的实现，最终它会基于一个 simple k v 的repasory，也就是说这几个是我们的 k value 的report，它是接口，那么这两个是一个 factory 的工厂类，那么 factory being 是构建这个 factory 工厂类的一个bin，那么它们最终构造的这个 repository 它的代理实现是基于 simple key value repository 来实现的。底下这两个是跟我们的 spring put 启动相关的两个 auto configuration 自动装配。第一个是 Redis auto configuration， Redis auto confusion 它主要是把我们相关的这些 Redis connection 链接构建起来。


那么第二个是 Redis repository auto communication，我们可以看到repository，它主要就是为了去构建我们对应的 key value 的repository，这样一个对应的一个代理实现。好，那么现在我们可以到 spring did Redis 的源码去通过功能源码来看一下这个结构，首先我们可以 check 下来对应的 spring day 的 Redis 的源码，我们去打开它 top 文件，那么在 point 文件里面我们可以看到对应 spring day 的 Redis 这个工程模块，它其实它对应的 point 也是 spring day 的point，我们知道它是整个 spring day 的体系的一部分，我们可以看到下面它的一些依赖，这里面对于一些依赖的版本做了一些封装。


我们可以看到它的依赖。首先是 spring day 的 key value，也就是说我们在使用 spring day 的 GPT 的时候，它的直接依赖是 spring day 的common，那么对于我们在使用 spring day 的 Redis 的时候，它的直接依然是 spring day 的KV，那么下面是跟 spring day 的 TS 45 RXM 进行一些序列化相关的一些内容，这里面 AOP 会做一些代理。这里面是 spring context support 底下也就是我们的 Redis 相关的一些驱动，对于 Redis 驱动现在常见的也就是 Redis 和 Redis 这两个驱动，如果说我们追求功能完整的话，我们可以选 Redis 和我们追求更高的性能，我们建议大家使用LETTERS，下面会涉及到一些 natty 相关的一些配置，这里面是 react core 相关的一些配置，下面对于我们就不用过多的去关心。


好，那么这是我们看到的我们的 spring 对于 spring did， Redis 的 palm 的一些意态的一些情况，那么这里面对于我们核心的比较关注的一些类有哪些？我们可以简单看一下。


首先我们看一下这个 spring day 的 Redis 的 report refactory，也就是我们基于 Redis 的 report factory 来构建我们对应的跟 Redis 相关的report。在词线内这里面也能看到对于 Redis report factory，它继承了 key value 的 reports factory，同时我们可以看到这里面也有 Redis report factory b，那么对于 Redis 的 report factor b，它也是同样继承了 key value 的 reports effect，这就是我们能看到对应 Sprint did Redis 跟 Sprint KV 相关的一些关系，我们可以在这里面去找一下我们的这个注解。


我们的 enable Redis reporsory，那么对于 enable Redis 的 reposure 这个注解，它里面的属性扩展属性还是很多的，我们可以从这里面去看一下，里面有很多东西，这里面是比如说 Redis template 一个引用，我们的对于reports， being class 等等这些信息还是挺多的，其实需要我们特意改造的内容并不是很多。其实我们更多的关注于基于这个 enable 的 reready repose，它启动的过程中需要import，也就是触发我们 Redis repose 的 register 去启动就可以。


对于它这个依赖的引用，我们可以看到其实 Redis report reduster 它会注册一些我们常见的一些bin，对于我们可以看到它其实是继承了 repository 的 bin definition that support 一个支持性的，对于这里面并没有实现过多内容，这里面关注的就是我们的 reports configure excuse，其实 extension 对于它来说去配置了我们比较关心的一些注册的一些依赖，我们可以到这里面去看一下对于它的一个实现。这里面我们关注的是 Redis report configuration extension，在这里面它里面会涉及到我们的对应的 Redis 的一些 Redis template，我们是可以搜一下，我们可以看到这里面我们涉及了对于 create Redis convert definition，我们的 KV Adapter，我们的 Mapping context 以及我们的 Redis reference 引用的相关的一些信息。其实这里面比较重要的会涉及到我们的 Redis KV 的Adapter，那么基于 Adapter 我们可以看到它是构建了我们这里面的 string being 的一个定义文件， spring brain 的definition，这里面我们把 Redis 的 key value 的 Adapter 注册进去，进行我们新人移植。


这边还涉及到我们一个注解，这是 Redis 哈希，比如说 get identifant a noticing，就是说我们具有一个明确的一个类型，区分的一个类型，这里面就是Redis。希待会儿我们在演示我们基于 Redis 这个 showcase 工程的时候，就可以看一下它是怎么去使用的。那么好，这就是我们简单的对于 string 对的 Redis 的源码就先介绍到这里。

