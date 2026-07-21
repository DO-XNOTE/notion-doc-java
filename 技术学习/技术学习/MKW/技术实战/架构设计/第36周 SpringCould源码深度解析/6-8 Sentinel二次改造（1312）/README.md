---
title: 6-8 Sentinel二次改造（1312）
---

# 6-8 Sentinel二次改造（1312）

同学们大家好，这一章节我们来介绍 settle 二次改造。 settle 的核心提供了支持扩展的 SPI 机制，这里包括SLOT， chain builder 和slot。那么对于单纯的扩展slot，通常不需要对 Slora chain builder 进行二次改造，比如说像热点参数限流的 slot 和网关 Gateway 相关的slot，都是通过 SPA 机制能扩展的。


那么大家有没有想过另一个场景，我们 settle 它的 Slardar 太多了，我想简化一下移除，即构我不需要的Slardar。这种情况大概率就需要我们修改 slot chain builder 的改造了。那么我们对于 Sentinel 二次改造，我们的选题是对 sort chain builder 进行首先深度分析，对于 sort chain builder 的分析完成以后，我们在对于它进行改造，那么我们可以通过自定义所有的 chain builder 方式来替换默认的 sort chain builder，也就是我们的 debug 所有的 chain builder。


那么在这里面我们改造的目的是什么呢？我们的改造的目的是可以对整个我们的 slogan 的列进行一个重新的排序，当然它是支持排序的，那么我们有没有必要去做排序？其实我们通常是没有必要做排序的。另一种方式就是说我们对于 Sentinel 默认的这些 Slotan 可能存在一些需要改造的空间，那么我们要改造的过程中，我们可能需要把 settle 默认的 slot 替换成我们自定义的slot，那么这个过程就需要我们通过自定义 slot chain builder 来完成了，那么另外一个同学说，那么我们直接扩展 slot 不行吗？当然也可以，扩展 slot 的话会让我们整个 sorter chain 的链的比较长，这样当然我们的 sorter 的 chain 越长，对我们性能消耗会越大。


所以说我们通过自定义 Slora chain builder 构造我们自己的 Slora chain，我们可以定义出一个精简化的这个 Slora chain，这样的话可以满足我们个性化的一些业务场景。那么我们来看一下 slogchain builder 的一些分析的情况，我们还是先看一下，对于在 settlement 核心的一个工作流程上，我们可以看到它是通过 slower chain builder 构建出整个 solid chain，那么整个过程它会涉及到几个slot？那么如果说我们想一下对于三种它的 SPI 机制，如果说它对 slot 扩展的话，它在扩展的过程中定义一个slot，那么通过 SPI 对应的 Meta info service 下面去定义一个对应的 process slot，那么它可以加载上来。


那么对于 sorter chain builder，我们知道在整个流程中它只需要一个 slot chain builder，它可能构建的对象是只有一次。那么如果说我们定义一个对应的 slot chain builder，那么它能构造出我们自定义的 slogan builder 吗？或者说它自定义的逻辑是怎样的？也就是说对于 slot 的话，我们相当于是可以扩展，我们制定一个根据它那个 order 的排序，我们是插入在 system slot 前面或者后面，这样对于我们做一个区分，那么我们看一下唯一的 slot chain builder 它是怎么去实现的，那么我们看 slot chain builder。


我们来先切到代码里面，我们从这里面去看一下，我们看一下是 c t s p s。对于这样一个类，它里面会涉及到我们获取对应的 slogan chain 的一个过程，我们可以看到这里面是对应的是 look process chain。在前面章节我们跟大家介绍了这个方法，现在我们回头更深入的去具体了解一下它。


在获取这个我们对应的 slogan chain 的过程，我们可以看到其实这个 slogchain 它是通过 process slogan chain 来表现的，对于这个 process slogan chain，它的表现形式，其实它也是一个对应的 process slot，它只是支持构成了一个 Flora chain 的一个效果。


那么在这里面我们看一下这个 chain 链是怎么去构造出来的，此前它会从缓存里面去获取，那么当然我们在初始化启动的过程中，缓存里面肯定是没有的，最终我们是从哪儿获取的？这里面是有 Slardar team provider，那么对于 slot team build broader，这里面是一个 new Slardar team，我们看到 new 的话，我们知道它是一个创建实例化的过程，我们这里面可以跟进去看一下。


在这里面创建这个 search and builder 的过程中，我们看首先它会去获取这个对应的 search and builder，如果说 slot turn builder 已经确认了，那么可以直接调用builder，那么如果说 slora turn 为null，它为 null 的话，它可以这里面会通过 SPI loader，也就是我们定义 SPI 机制，它去加载这个 assault in builder 这样一个过程。
那么过程这里面我们看到它会指定是 load first intense default，也就是它加载第一个实例，或者说是一个默，如果没有的话就加载默认的，那么对于默认的话，这里面就是 debug 所有的computer，因为我们要替换，所以说我们肯定不希望是默认的，那么我们怎么替换？看这个方法它实现的逻辑，它是这里面是 load first 的instance，那么只加载第一个，我们可以看一下这里面的逻辑是怎么实现的，其实我们最终会涉及到里面一个 SPI service 的加载机制，在这里面我们加载的过程可以加载到对应的一个safeloader，那么加载到 surface loader，我们可以看到 safeloader 它其实实现了是一个迭代器，比如说是一个 at table，它是个迭代器，也就是迭代器它可能会加载多个。


那么加载多个的情况下我们怎么去区分呢？我们看方法名是 load first， instance or defeat，这个怎么去理解？我们看到家长整个对它进行一个迭代的过程，那么这个迭代遍历的过程它做了一个什么事？我们可以看到它在遍历这个实例的过程中，会拿实例对应的 class 跟我们 defailed class 进行一个比较，如果说它不是相同的，那么它返回大家理解了吗？也就是说它在查找这个迭代器的时候，整个迭代器找的是第一个跟我们这个给定默认的 class 不是相同的，也就是说我们默认的是一个 default sort chain builder，那么跟它一样的话我就会忽略，那么找到不一样的话我就直接返回，也就是只能找到第一个跟它不一样的一个quota，那么如果说没找着的话，他就通过我们 DQ 的 class 创建一个实例，所以说大家应该理解了。


如果说我们在创建我们的 SPI 机制的过程中，其实这里面就完成了我们 SPI 机制的一个构建，那么这里面我们可以再回来看一下对应的一些实例的情况，在这里面我们首先去找我们 debug 的 slot computer，那么这里面它的源码会在哪里面去实现？对于这里面我们可以看到会找到对应的一个 slogan builder，那么在 slot term builder 里面，它会获取到 debug 的 slot term builder，那么我们自己要构造我们的 slot term builder，我们需要怎么做？我们需要定义我们的 Meta info 对应的service，下面也定义我们对应的 com 阿里巴巴 CSP settle sort chain 的 sort of builder。那么我们通过这样构建盘这个文件以后，它会通过我们的 SPI 机制去查找对应所有的这个 slot builder 文件，那么找到所有的这样的定义的这个 sorting builder，那么找到以后它会根据一个顺序获取到第一个，那么所以说这里面就我们应该要注意到一点，这里面第一个也就是说其实如果说我们定义了多个 store ten builder 的话，其实我们得到的结果是不确定的。


所以说我们在定义 store Chen builder 的时候，我们一定要有一个统一的一个约束，我们不能随便自定义这个 slow Chen builder，那么我们看一下我们自定义 slow 的 tender 我们怎么去操作呢？在这里面我们对于 settle 的工程里面，我们首先这里面在 settle 包下面建了一个configure，就 configure 我们定义的是 customer slogan builder，那么我们先不管它里面实现的内容是什么，那么我们如果说想让这个 source builder 生效，那么我们首先需要在我们的 resource 目录里面是创建我们对应的 Meta info，也就是 SPI 规范下面的目录，它对应的目录是 Meta info service。


在这里面我们定义了一个是对应的 slot and builder 这样一个文件，那么这个文件里面我们指定了一下，是我们对应的构建的是 customer slot computer，那么在这里面跟我们的名称对应上，那么在启动加载的过程中，它就会获取到对应的配置文件，找到我们这里面的这个类的全名称，也就是 customer slot team builder。
那么在构建的过程中会通过它去调用我们对应的 build 方法build，构建出我们的 process slower chain，也就是说构建出我们真正的这个我们的执行链，那么在这个执行链里面我们可以去构造我们这个链的一个结构，那么我们知道它默认链的结构其实是对应的也是基于 SPI 机制配置的，这个我们这里面可以看到配置的这些slot，那么它默认的是基于这个 process slot 这个 SPI 机制去加载，也就是加载了这些我们的一些 slot 文件。


那么对于我们自己要是去自定义这个 chain builder 呢？我们可以构建我们自己所需要的slot，那么比如看这里面我们是通过手工的构建出一个 debug 的 process slot chain，那么我们手工的去把这些我们关注的这些 slot 一个一个装载进去，那么我们可以看到这里面比我们默认的是少了几个slot，比如像这里面的 system slot，那我们这里面是基于编程的方子构建slot，我们也可以非常轻松的创建一个我们自定义的slot。


当然这里面要注意一下，如果说我们在这里面手工的去创建，通过编程的方式构建我们的 process slot chain，那么在这里面我们已经改变了 store chain 的它默认的 SPI 机制。那么如果说我们在这里面改变完成以后，那么对于用户还是通过我们这样遵循 SPI 机制构建的 process sorter，它还能不能加载进来？现在是不能了，所以说我们要知道我们这里面的改动已经改变了 settle 默认的一些表现，所以说大家一定要注意一下我们是如何实现的。


如果说大家对于构建策略，我们还是想遵循一下对应的 process slot 的一些规范，那我们可以在这里面还是使用它默认的 build slot chain 的一个过程，我们还是这里面通过 SPI 机制去加载对应的 process slot，这样我们可以加载到我们基于 SPI 机制扩展的slot，我们也可以基于 SPI 机制扩展的 slot 进行一个二次的一个后处理，那么基于这个后处理的话，我们既遵循了 SPI 的规则，也能去扩展我们自定义的一些逻辑，这样也其实是挺好的一个实现。那么我们这里面去看到我们完成了这个，我们这里面是 customer slot term builder 里的构建，并且基于编程的方式完成了这个链的构建，同时也自定义了我们一个 customer sorter。


我们看一下我们定义这个最简单的一个 custom sorter，对于这个 custom shorter，我们是让它继承了 abstract link 的 process sorter，对于second，它大多数的这些 sloter 都是继承了 abstract linked process sloter，我们可以跟进来看一下，在这里面我们看一下它的一些脂类，从这里面我们可以看到这是我们的 custom sorter，这是比如 grade slot，也就是降级的这是我们流控的 slot 等等跟日志相关的slot。这里面还有热点参数相关的slot，那么在这里面我们可以看到我们现在重写了我们的一个 slot term builder，并且我们自定义了一个 custom sorter，当然这里面我们并没有做什么实现那么好，那么我现在去通过单元测试，我们 debug 一下，看一下我们制定的 customer sort chain builder 是不是真正生效了。


那我们现在这里面执行一下，我们现在通过 debug 我们，我们可以看到现在它已经执行到，我们对应的是 speed loader，在这里面我们看一下它执行的情况，此前它第一步是通过我们 service loader member k 里面获取，当然获取不到的，那么这里面接下来它通过 service loader user 去 get service loader，那么这样我们 get 到我们可以看到我们会通过 service loader 得到一个对象，那么我们看这个对象当前它是一个 token service 这个我们可以跳过，但这不是我们关心的。


那么接下来是到 look process chain，也就是这是我们真正获取这个 solid chain 的过程，那么我们切进断点，那么在这里面我们是通过 slot chain provided 去 new slot chain 构造，这里面会，这是我们真正要关心的内容。


首先我们看一下它，现在它获取 service loader 的时候没找到我们的结果，那么这里面我们通过 service loader UTO 从我们的 get service loader 里面去找我们对应的这个builder，那么我们看一下现在我们获取到一个 service loader，那我们看一下这个 service loader，这个 service loader 它是一个 task 迭代器，我们看它执行的结果，现在到这个 service loader 来进行一个迭代。


那么现在我们看一下当前的instance，这个 instance 它是一个 customers lot of chain builder，那么也就是说这是我们构建自定义的，它跟 debug class 对应的这个类，这是我们这里面是 debug slot tribute，它不是同一个对象，比如说这个值成立，那么我们就会把当前的 instance 对象的返回，这会就我们就不再使用 debug class new 的 instance 了。


那我们返回以后，我们可以看到这里面我们构建出这个 slot chain builder，那么在这里面 slot chain builder 它如果是等于 null 的话，使用默认的，那么单填不等于null，那么现在我们需要去使用我们默认的我们这样一个我们自定义的这个 slogan builder，那么现在是进行一个 build 操作，那么 build 操作我们跟进来，现在执行我们自定义的我们的 customer solution build customer 我们可以看到这里面我们是定义的是process、 load ten，那么这里面是我们自定义的这些slot。


那么这样的话我们可以看到我们通过在这里面是自定义我们自己的 solution build 现在已经生效了，那么接下来它执行的流程，也就是说我们只需要在我们对应的这个 build customer 里面实现我们自己主装的 slot 这些链的逻辑就可以了，那么现在我们去把我们的程序执行完成，那么我们现在回到我们的GPT，那么在这里面的话，我们可以通过我们自定义的 slogan building 来完成我们对整个链的一些自定义的一些顺序的一些编辑。那么我们对于 search and builder，那么我们先介绍到这里面。

