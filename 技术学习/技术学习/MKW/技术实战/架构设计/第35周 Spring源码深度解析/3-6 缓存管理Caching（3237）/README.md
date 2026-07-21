---
title: 3-6 缓存管理Caching（3237）
---

# 3-6 缓存管理Caching（3237）

[image](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/d10c10a3-c2e3-45ff-9226-8d2ec7df8217/SCR-20240803-peic.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664YDHGBVU%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T232023Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIFRKowzBROkmPmY%2FyOsFkBhsTPjgvcoEagFLGto2tiS%2BAiEAgMGgktfEjwftKJfj6tCTD1P9%2BcJ4Cx%2B6IfDZO9ppx70qiAQIxv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDO%2FOZKLBjoPclX4tfSrcA5beNsTjSx3mqmX4w7hpwwVqxXNlJ3mGp7%2BWVsR4GNhM82jWi6%2BbitX41aF8mkJgblilu%2F4XrElLrHkX74B0s8OGGXZi3Xk30aOEaeIdRZ%2BuRLPMTO3mx7B8D4o5FjoWQFj%2BABCIDyRCI8653jLVD245HTJFEoBx63%2B3DLoR%2FIiHckHvFQVwBR7ACdx%2BxN1ncvrUd8AUDuDzsiSHnPuM4jHtqbCNSLPsxLB2%2BkXnK8qMUVYCQiaDo0s3zW951aHeZbtn4qsJDRa%2BBvLb2ZUZaNS3i8C7xJPZcPoZmmEl8rdrhELUVCgON992bKUO3%2BkyXv1ypou69%2B%2FRx4c7casInz93rP4TBXz9D%2FyHoT%2FAboxcLuJgAdfbvEPTFTxsT82rFGpEwHcvbLVuGI2EcqD8otRDwSxuuNziRy8CAH9r9Pz10CfZkGvqOOdy4f6G3El%2FSjjM8jJplywDq5ykUafgZcE7T9uTUpYKxVJKeMHKveZQ5wAswEk4uUu6zbKUViFEdYXgi%2B3b0k19SBjgjxDw%2F%2BAcHB%2FAYiKQNy7pFviBNhLcwFWd1QZ8kxzlBLCLLZduFYKSlfkwNMZWOq4WvzRB3a%2BthSnn4hr%2FJK%2BFCvb7o6341hcvBgB1cZQZeUqkMJq6%2F9IGOqUBtOKC8AeGFe%2BNZ3ZK%2F9w6HXEcZ6lLXYdO9mn1Ay%2Fr1R2NrsNZIJ9cKeIC1DeYKluFgXlJBLLacqCr8FTbrlzl5X0Y7KKggMhAuB%2BStHSndLcSI9BIyMyNjwQXXYIBhgd3ceWpER6EOgrzhiQjSmOLG%2Bg70Lp7eEj3D7hS4AvrYjlQhse%2B0Dt6Ruk2oWjvMd3tjiu2yz3lsYMPkrejOOuyGHd0yxrD&X-Amz-Signature=591da3b57643abdfab44ff6bd42228c4955a7a3b0a16d13da49f6d04b3c281c9&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

[image](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/b24e1092-8e7f-4605-88ed-ce13955a206d/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664YDHGBVU%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T232023Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIFRKowzBROkmPmY%2FyOsFkBhsTPjgvcoEagFLGto2tiS%2BAiEAgMGgktfEjwftKJfj6tCTD1P9%2BcJ4Cx%2B6IfDZO9ppx70qiAQIxv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDO%2FOZKLBjoPclX4tfSrcA5beNsTjSx3mqmX4w7hpwwVqxXNlJ3mGp7%2BWVsR4GNhM82jWi6%2BbitX41aF8mkJgblilu%2F4XrElLrHkX74B0s8OGGXZi3Xk30aOEaeIdRZ%2BuRLPMTO3mx7B8D4o5FjoWQFj%2BABCIDyRCI8653jLVD245HTJFEoBx63%2B3DLoR%2FIiHckHvFQVwBR7ACdx%2BxN1ncvrUd8AUDuDzsiSHnPuM4jHtqbCNSLPsxLB2%2BkXnK8qMUVYCQiaDo0s3zW951aHeZbtn4qsJDRa%2BBvLb2ZUZaNS3i8C7xJPZcPoZmmEl8rdrhELUVCgON992bKUO3%2BkyXv1ypou69%2B%2FRx4c7casInz93rP4TBXz9D%2FyHoT%2FAboxcLuJgAdfbvEPTFTxsT82rFGpEwHcvbLVuGI2EcqD8otRDwSxuuNziRy8CAH9r9Pz10CfZkGvqOOdy4f6G3El%2FSjjM8jJplywDq5ykUafgZcE7T9uTUpYKxVJKeMHKveZQ5wAswEk4uUu6zbKUViFEdYXgi%2B3b0k19SBjgjxDw%2F%2BAcHB%2FAYiKQNy7pFviBNhLcwFWd1QZ8kxzlBLCLLZduFYKSlfkwNMZWOq4WvzRB3a%2BthSnn4hr%2FJK%2BFCvb7o6341hcvBgB1cZQZeUqkMJq6%2F9IGOqUBtOKC8AeGFe%2BNZ3ZK%2F9w6HXEcZ6lLXYdO9mn1Ay%2Fr1R2NrsNZIJ9cKeIC1DeYKluFgXlJBLLacqCr8FTbrlzl5X0Y7KKggMhAuB%2BStHSndLcSI9BIyMyNjwQXXYIBhgd3ceWpER6EOgrzhiQjSmOLG%2Bg70Lp7eEj3D7hS4AvrYjlQhse%2B0Dt6Ruk2oWjvMd3tjiu2yz3lsYMPkrejOOuyGHd0yxrD&X-Amz-Signature=0f9f2628fd6c755fcaefeacaec3f702dac9ce4dab5d6f0a3ea636a9dfaeff74d&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

同学们大家好，这一章节我们介绍 string 缓存管理的设计与实现。缓存是实际工作中非常有用的一种提高性能的方法，我们会在许多场景下使用缓存来降低系统的查询响应时间。在使用 3. 1 以后，它引入了基于注解来配置使用缓存的方式stream，它本身并没有提供缓存的具体实现，它是对缓存的使用方式进行了一个抽象的包装，它可以适配多种具体的缓存实现，比如说 CON 坑的哈希 map 或者是 Cafe in cats 以及 ES cats 等等。基于注解的方式进行缓存的也是使用了 AOP 的方式实现。


我们可以方便的在需要添加缓存功能的地方，也就是配置一下cancelable，这样一个注解，它就能让这个方法完成缓存的功能，那么我们对于 spring 的缓存管理也是分三部分来介绍，首先我们去介绍一下 spring case 相关的这些注解，这里面包含 JSR 107 和我们 spring 自定义的一些注解。那么接下来孩子 spring 的 CACHE 的一些核心API，就是我们在了解完注解，了解API，最后我们来基于 spring CACHE 的运行流程进行介绍，通过我们代码示例的演示，让大家更方便的理解 spring cats 它的一些运行流程和它的一些实现机理。现在我们来看一下 spring cats 相关的一些注解，在这里我们看到 spring cat 注解的它可以区分为 spring 相关的注解和一些 JSR 107，也就是 Java 它定义的一些缓存规范。


首先我们可以看到在 spring 注解里面，传统的也就是 enable cache 去通过它来去开启我们的缓存注解，通过 cache able 在方法里面去标明这个注解，就去标记一下我们这个方法已经开启缓存，这里面有 case evict，就是说当我们需要对于缓存更新掉，也就是缓存失效掉的话，我们可以在对应的方法进行这个操作。比如说我们在查询方法上用cancelable，我们在这些 remove 方法上可以通过 category 的方式去把我们的缓存式去掉。那么对于我们的更新方法，比如 case 铺的，我们可以在修改对象的地方，我们用 cats 铺子的方式去对我们的缓存进行更新，这里面有 cacting 和 CACTS configure 的，是一些更特殊的一些缓存的一些用法。在这里我们可以看到 JSR 107 它的这个缓存的定义名称的跟 stream 的名称基本上是一致的，比如说像这里面的 cat put 是非常容易理解的，这里面的 cat evict 对于这里面是 cat remove。这 GS 107 里面提供的 cat remove all 在 spring 里面并没有提供，但是我们可以通过 cat evict 里面添加它对应的属性来完成 cat remove all 的一个效果。


现在我们来看一下 spring 源码对于 cat 的这些注解，它在实现的位置，在这里面我们可以看到对于我们 cat 相关的这些注解，比如说 cat table 和 cat configure evict， cat pool，它都是在 string context 模块里完成的，在这里面这是我们定义的这些注解的情况。


这里面比如说我们看到 enable cacting，那么对于我们这里面这些注解，可以从这里面去看到，我们看到刚才介绍的 j s r 107，它的注解在什么位置，我们可以从这里面去对应找一下，这是 case put 对于 j s 3107 它 a p i 的定义，它是在加 x cat 用的 case API 里面去实现的。里面我们看到在加 x cat 这个包对应的 allotation 目录下面有，我们看到了 cat default cat，这里面 cat put， cat remove 和 cat remove all 相关的这些注解？其实相比来说，我们使用注解的过程中，我们是使用 spin 注解还是使用 Java 它定义的这些规范的。大多数情况下，我们会推荐 Java 提供的这些规范，但是对于 spring cats 这个注解来说，可能 Java 这个规范它 cats 使用的比较少，可能大多同学会更愿意去使用 spring 定义的这些 cats 的注解的名称，具体使用哪个注解，其实这个并没有太大的区别，它都能实现我们的功能。


接下来我们来看一下 spring CACHE 它的一些核心的API，在这里面，对于我们 spring CACHE，它最重要的就是它对于 CACHE 的抽象，也就是这个 case 接口，对于这个 case 接口它有多种实现，最基本的也就是在 string context 它这个模块里面它实现了一个 concurrent map cats。大家看到这个 cache 的名称的话，大家能。
想到其实这个缓存它是利用了 concurrent hashmail 的方式去完成的这个过程。同时 spring 它还会对于一些比较好的第三方实现的这些 cats 进行了包装。


这里面比较典型的像 coffee in cats 和 ES cats，待会我们可以一块看一下，同时基于知识 cat 对象，我们通过 cat 对象去获取我们缓存的内容，那么对于 cat 对象它还需要一个 cat manager，对于这个 cats manager 我们可以去构建 cats 对象的一个过程，这里面也是跟大家去介绍重点就是说 concurrent map cats manager 和咖啡因 cat manager，当然我们这里面还有 ES cats cat manager 和 j cats cat manager。同时对于 cats 它还有一个 cats l handler，也就是说来去处理我们在使用缓存里面发生错误的一些处理方式。同时也有一个 cat receiver，它是通过我们对应的这些上下文信息去解析出我们的 cats manager，通过 cats manager 获取到 cats 这样一个对象，这就是整个 spilling cats 设计过程中用到一些内容。


当然我们在缓存对象的过程中，我们有一点是必不可少的，也就是我们的缓存的k，那么我们一般情况下我们的 value 就是我们返回的对象，那么 k 我们怎么构造呢？通常是我们这些输入的参数，当然我们也可以通过 ER 表达式的方式去注解指定我们的某些参数。


接下来我们来看一下 stream 源码里面对于这些 case cans manager 的一些实现的情况。首先在这里面我们看一下，看到这是整个这个 case 接口，它是在 ORG spring from cats 这个猫结构下，同时它的实现也是在 spring context 下面，我们可以给这里面是实现的相对是比较简洁的。我们可以看到这个 cats 接口里面，它里面提供的列方法跟 map 提供的方法是很相似的，比如我们这里面有clear，也就是把整个 cat 清空，这里面以 vacate object，这里面是指定一个对象，相当于是我们移除指定的一个对象。下面有get，也就是说我们从缓存里面获取我需要的内容。有 get update，这里面有对应三个，还要 get object，指定的 carable 或者是指定的类型等等。这里面有 get name，我们就是指定一下我们cats，这个当前缓存的名称等等这些内容。下面有invalidate，也就是跟我们上面 clear 它的功能其实是一样的，它通过 invite case 的效果跟 case 都是把我们整个缓存清空的效果。


下面有put，就是我们向缓存里面去设置内容的一个过程，这是我们看到的这个 cats 接口，它是作为一个顶级接口定义了这些方法，同时我们来看一下 cats manager，那么 cats manager 它提供的方法会更少，这里面只有两个方法，一个是 get cats 通过name，也就是指定一个 case 的名称获取到我们当前这个 case 对象。里面是我们可以获取到 cats names，也就是说我们这个当前 cats manager 里面管理的所有的 cats 名， cats 对象来全部通过 text 集合的 pass 返回过来。


在这里面我们可以看到对于 spring 默认的实现，也就是在我们这里面的 spring context 这个模块儿下面它的一个默认实现，我们可以看到这个 case manager 它默认实现的也就是这里面 concurrent map 开始manager，这个 concurrent cats manager 也是对应的在 spring context 包的实现，这个 content map 和 cats manager 对应的就是 concurrent map cats。我们可以看到这里面我们对于这个 concurrent map cats 里面定义了一个 concurrent map，这个 concurrent map 我们看一下这里面默认的构造方法，在构造方法过程的时候，它这里面传入了一个 concurrent Hashmap，也就是说它默认通过 JDK 的 concurrent Hashmap 来实现这个缓存的一个定义的过程。


当然如果说我们是需要用第三方集成的一种方式，比如说我们需要用咖啡因这样一个 cat or cat map，我们怎么去获取它？其实对于这些第三方集成的内容，它并没有在 string contact 里面，我们知道 spring contact 这个模块是非常基础的一个模块儿，如果引入非常多的第三方的话，对于整个系统的稳定性其实是有一些可以值得考虑的一些地方。那么对于一些集成第三方 string 是怎么处理的，我们可以看一下对应，我们看到这里面的 Caffeine cats，那么这个 Caffeine cats 它的实现在什么地方？我们在这里面去选中test。


在 spring contact support，也就是说对于一些第三方支持的这些实现都是放到了 spring content support 这样一个模块里面，我们可以看到在这个模块儿里面的一些外部依赖，这里面它依赖的内容，这里面像 strong being context，这就不用介绍了，我们主要是关注的是这些可选的依赖，在这些可选的依赖里面，这里面有 mail a p i 和 Cats API。


这里面我们刚才跟大家介绍的 Cats API，它这里面的依赖方式，记住这种依赖方式 optional 是一种可选的发词，当然下面是有我们的咖啡因，这里面是 ES cats 这种发词，也就是说对于这些第三方的一些集成，它是通过 spring context support，通过 optional 方式依赖进来。


假如说我们是需要使用到了这里面的卡啡因对应的依赖，那么我们需要在我们业务系统里使用的过程中，需要显示的把 Cafe in 这个依赖引入进来。当然如果说我们使用 ES cat 也是相同的道理，那么我们也是需要手动显示的去引入这个 ES 开始的实现，这里面还有像 ESL Handler 和我们的 k generate。当我们的业务非常特殊的情况下，可能会涉及到一些自定义，假如说业务没那么复杂的话，我们最多也就用到了 cat 或 cat manager。大多数情况下我们只是需要使用对应的注解就能完成我们的任务。
那么我们在工作过程使用缓存的选择方式是怎样的？这里面一般是两种情况，假如说我们是分布式系统，我们肯定需要选择分布式的缓存实现，这里面我们一般是基于 Redis 的实现。那么假如我们是需要本地缓存，那么本地缓存的话，现在我们认为效率比较高的，也就是 capping cats，这里面我们可以看到对于它在 copy in 这个 git Hub 上面，它定义了一个就是性能测试的一个效果。这里面我可以看到这是 Cafe in 的，它的并发的请求量底下有 concurrent link 的 Hashmap 和 Linkedid 的Hashmap，也就是说这两个是 JDK 官方实现的 Hashmap 的一些实现，后面是有 Grava case 的实现，以及 ES case 2 和 ES case 3 版本的一些情况。通过这个图表来看的话，整体来说如果说我们需要做本地的内存缓存的话，我们直接选或者 copy 音其实就可以了。


那么接下来我们来看一下 spring cats 它的一些运行流程，在这里面我们使用 spring cats 它的执行流程跟我们介绍的 string 45 的执行流程是很相似的，在 45 的过程中是 enable transect manager，那么对于缓存来说，我们是 enable catching，它都是通过这个注解，通过 import 对应的一个 selector 去引入对应的一些 configuration 的一些实现。在这里面它引入的实现也就是基于代理的 kids 开词型configuration。那么对于它的一个实现的过程，它这里面主要构建了三个bin，一个是一个adversion，也就是我们实现 AOP 的一个对应的描述。


另外这里面还有一个 a notation cats a present sauce，它是什么意思？其实这个对象它间接地去标明了一下我们整个这个AOP，它具要处理的这些对应的它的切入点是什么？那切入点就是我们所有通过 catable 或者case， event 等等这些注解去扫对应修饰的这些方法，是我们整个 AOP 执行的一些锚点，那么在这里面还有一个对应的 case except，通过这个我们是比较理解的，这就是我们整个 AUP 的一些拦截的操作，通过它的拦截，在这里面我们看到通过 cats in shift 拦截的 invoke 方法去执行我们对于缓存的一些处理。


我们知道对于缓存处理的过程其实比较容易理解的。首先我们在去做一些查询操作的时候，我们先从缓存里面去取一下当前对象是否在缓存里面，如果在缓存的话，我们直接把对象返回过去，假如说不在缓存里面，那么呢我们就会执行对应的我们的业务操作，一般我们可能去冲DB，我们的 MySQL 数据功能去取我们的对象，取到我们合格的对象以后，我们会把这个对象同时放到缓存里面，然后把我们整个这个对象返回给用户。那么这样的话，我们就等着在用户第二次执行的过程中去从缓存里面执行，而不用再走数据库这样一个过程，这样你就减少了我们整个执行的时间。


那么对于 spring 它这里面 intercept 它的实现也是类似的，这个 case intercept 它是继承了 case spect Sporter，通过如果它的实现里面它的关键的执行流程，也就是 excuse 的方法里面是做了一些处理，首先它会去处理一下 cat effective，也就是说它在处理的过程中会同时处理这些注解，一般它的顺序是先去处理一下具有我们相当于是缓存移处的操作。那么接下来我们从开缓存里面去查找一下我们当前的 item 是否在缓存里面，然后它会再处理一下这个 put 类型的操作，也就是说我们 case put 相关的操作。


接下来最后再去处理一次我们的 cat EFFECTS 相关的一些内容，那么接下来我们来看一下源码里面这些它的一些处理的过程。首先在这里面我们还是基于我们的 spin skill 这个模块里面去介绍我们缓存相关的内容，这里面跟大家去介绍一下，在这里面我们新加了一些内容，首先这里面我们引入了是咖啡这个缓存的一个实现，同时我们也引入了对于开启 API 这样一个接口，把这两个加号进来以后，我们去构造我们对应的缓存的一些实现类。


我们在这里面，这里面我们看这里面配置了我们的 enable catching 这样一个注解。同时我们这里面是定义了两个 cat manager，其实我们正常运行的话，我们需要一个 cat manager 就可以了。在这里面特意为了跟大家去说明一下，为什么我们在使用本地缓存的时候，我们不建议使用 contain 的highmap，它的一个实现主要的原因是因为 contain highmap 它只是一个缓存的存储，像比如说我们初始化容量，我们过去失效等等这些配置，其实 contain 含义 map 它是不支持的，所以说更推荐大家使用其他第三方的一些缓存的集成。


这里面就跟大家推荐的是 Cafe in 的 cat manager，基于 Caffeine cat manager，它可以支持很多的一些属性配置，大家可以查一下，在这里面，比如说基础的一些我们初始化的一个容量和我们最大的一些容量设置，比如说我们当前这个对象它过期失效的时间，比如说我写进去以后多久不读，那么这个缓存它就可以清理空间，减少对我们内存的占用。


这里面只是可以跟大家演搜，我们可以通过这种方式的话去配置我们 Caffin 这个 cat manager，但这里面我们并没有去设置它，我把它注释掉了，主要是因为在我们使用断点调试的过程中，它那个过去失效的时间我们需要设置的更长一些。那么现在我们来看一下这个 user service 它的实现。在 user service 实现的它是一个普通的 user service，当然它正常我们的 service 是需要调用 d o 的。在这里面我们没有去依赖数据库，我们在这里面也是通过一个 contain 的 Hashmap 作为一个 star 来去模拟我们数据库的一些操作。在这里面我们实现了蒸三改查几个相关的一些操作。


首先我们来看一下 Pre 的user，它会把 name 和 is 进行一个包装，构建成一个我们的对象放到这个 content map 里面，同时我们看一下这里面并没有跟缓存相关的内容，因为我们对于创建对象是不能跟缓存相关的。下面是我们是 remove user，假如说我们是使用到缓存的话，我们要删除这个对象的时候，同时我们需要把这个对象从我们的缓存里面也清除掉。在这里面我们对于这个删除缓存它的 key 用的是当前这个属性，也就是我们 user name 对应这个名称，这里面的 remove user 跟我们在这里面的 find user 是对应的关系。


我们在 find user 的过程中，这里面也是通过名称去查找，这里面对应的 k 也是我们的井name，也就是当我们在第一次查找这个 user 的时候，它会通过去判断一下缓存里面是否存在，如果说不存在的话，它会把当前对象从我们的存储空间里面取出来，同时它放到当前指定的这个 user 缓存里面，在这个缓存里面同时把我们对象返回过去。


只有这样我们放你当在执行我们的 remove 操作的时候，才可以对应我们这个缓存里面，把当前指定的名称把它给 remove 掉，这是我们那个简单的一对一的一个 remove 调整。同时如果说我们需要 remove all user，也就是我们把所有的用户全部清理掉，可以使用 cat evacuate 里面的一些属性，就是 all in trees，我们设置为true，也就是当我们执行这个方法的时候，我们缓存里面所有的信息都会清理掉，当然我们这里面还有一个是更新的操作，假如说我们用户的信息进行更新的话，那么更新完成以后也是需要把我们缓存的信息进行执行的。


当然这里面有两个方案，一个方案是我们可以把我们缓存的信息让它可以失效掉，那么当我们再去查询用户的时候，可以先从数据库里面取一次放到缓存里面，这样的话就相当于增加一次数据库的操作。那么我们可以在 update user 的过程中，同时把我们的缓存进行一个更新，也就是我们用到了 cat puts 的方式，当我们执行完这个 ability 的操作以后，它会把当前的这个 user view 这个返回值作为我们的参数进行一个更新，这是我们对于我们使用缓存的操作。那么现在我们来执行一下我们的单元测试，看一下整个这个执行的效果。在这里面我们通过 spring do you need to configure 引入了我们的 case scale 这样一个配置类。在这里面，首先我们要做的事情是什么？我们启动的时候，也就是 add before each 启动的时候，在我们的数据库里面创建两条记录，这 Jimmy 和Tom。


在我们执行的过程中，我们首先去执行，我们通过 Jimmy 去查找这个对象，这样的话，我们第一次去查找的过程中，它是不能从缓存里面获取到的，它应该是从数据库里面去获取，那么第二次它在执行的过程中就可以从缓存的获取到。那么我们先执行一下，看一下它执行的效果。


好，我们可以看到这是刚开始我们创建了两个对象，那么我们第一次去执行的过程中，这里面也看到了有 find user 的操作，有 find user name 等于机密，我们可以看到这是我们在 find user 过程打印的日志，那么我们在第二次执行的过程中并没有 find user 的操作，这说明我们第二次执行的过程它是通过缓存里面去执行我们的内容。那么接下来我们通过断点来跟一下我们整个系统执行的一个过程。好，我们现在来去启动，当我们启动的过程中，我们可以看到它这里面是执行到了我们的 porks cacting configuration，那么它是什么原因执行到这里面，通过这里面去跟一下看一下。


首先这里面是我们因为有 enable catching，我们通过 enable cache 可以去看到它在这里面是有一个 import 对应的 cacsing configuration selector，我们点进去来看一下这里面它对应的这里面是一个 select import 方法，默认我们使用procacy，比如代理的方式，我们看它这里面实现的什么内容，这里面注册了两个register，一个是 AOB 的一个register，一个是基于缓存代理的一个configuration。那么这样的话它就执行到了这个configuration，在这里面我们执行的过程我们可以看到它处理的内容，在这里面它定义了三个方法，一个是我们定义一个 cat adversion，也就是我们 AOPT advertiser，另外是执行我们的 cat intercept，也就是对我们方法进行拦截操作的intershapt。


那么另一个就是 cats operation sauce，那么 cats operation sauce 它住的工作是什么呢？他注的工作就是跟我们缓存相关的这些注解进行绑定，也就是标明一下我们在什么地方切入我们的AOP。我们跟进去看一下在这里面构造方法，它在执行的过程中，这里面会涉及到构建一个 notation pros notion POS，这里面是使用了一个 spring cats notion pros，我们跟进来看一下它执行了什么事情。


我们看到这里面，我们看到它是把这些注解像 cat able， cat effect， cat put， cat 同时放到当前的这个 set 里面，那么在计算的时候，也就是我们看一下当前这是不是一个候选的一个注解的时候，它就会去执行使用到这样我们可以看到它是通过这种方式去识别我们这些跟缓存相关的一些注解。


那么我们跳过这个断点，接下来执行到的是我们的一个 cat except，也就是在执行 AUP 的时候，它需要拦截的操作是怎么操作的？它是通过这里面定义的这个 intercept 去进行拦截操作的，在这里面我们定义这个跟缓存相关的操作的时候，这里面是需要我们配置一下，这里面有 error handler 和我们的 k generate 以及我们的 cat 


reslower 和 cats manager，那么我们可以跟进来也看一下它里面出了哪些事情。在这里面我们默认情况下，我们并没有去构建我们的 air Handler，那么它会怎么做？当前我们可以看到这是一个 supply 对应的 cat airhandler，它会从我们的容器里面去获取，也就是说如果获取不到怎么办？它会在这里面去指定一个 simple case 

airhandler 的一个方法，也就是说我们通过构造一个 simple cats error handler 的这样一个对象，去做我们的一个替补操作，我们可以跟进来看它是怎么完成的。那么我们点到这个里面，这里面它做的一些操作就是说我们对于这个 single supply 时，它对应一个 4 一个实例的一个提供器，这里面还提供了一个默认的，这里面它是真正的实现方式是在这里面有一个对应的 get 操作。


get 操作是首先判断一下当前这个实例不存在的话，它需要去做的是通过我们一个debug，就是最终会获取 debug 的一个值，去做一个替补的操作。那我们接下来跳过这个断点，继续刚才4，我们可以理解为我们 string 容器初始化的过程，这个初始化的过程就是把我们缓存相关的这些 AOP 的一些配置去进行一个生效的操作。
接下来我们开始进行真正我们执行的操作，那么也就是我们通过 user service 去读取我们 find user 的操作，这个过程中它会涉及到 AOP 的操作，会进行我们刚才这个 intercepts 的拦截，那么我们现在跟进去看一下我们下一步需要做什么事情。


到这里面我们可以看到它其实是被这个 cat intercept 这个方法进行了一个拦截，那么进行 emote 方法，在这里面它需要注的操作，我们可以一步一步跟进来看一下。首先会定义了一个AOP，一个 e voker，那么我们接下来看一下，在这里面去执行一个 exclude 方法，这个方法我们可以看到它的一些参数，这里面有 target 以及有 mass 的 invocation 和我们就是当前指定的这些参数，那么我们跟进去在这里面我们看一下当前的一个初始化状态，也就是我们的 cats aspect sport 它当然这个过程是已经初始化完成了，那我们进行继续这里面也会执行到一个另一个 exclude 方法。


那么我们执行进来看一下，在这里面首先判断一下是一个是否同步的方法，这个它是默认是false，我们会跳过走到这里面的，在这里面我们看到它会去首先对于早期的一些 EVICO 的方法进行一个处理，默认的话我们这里面是并没有 if go 的相关的内容，所以说这里面对应获取到的一个 set 它的值，这里面历史它的 contact 值是一个 null 值。


所以说我们在这里面它不会做什么事情，我们可以看到 context 它的内容是空的，那么我们跳出来接下来就是一个关键操作，在这里面它要注的事情是 find case item，也就是说通过我们的信息去上缓存里面去查找当前缓存里面是否存在，因为我们知道这是我们第一次去执行这个方法，缓存里面是没有的，我们可以跟一下看一下这个结果。在这里面我们跟进来看一下会去做一些处理。


首先这里面我们看到它当前是不是需要通过，首先会构建我们的这个k，构建 k 的过程中我们可以看到这个 k 是我们对应的这个参数name，这里面我们可以看到这个k，也就是对应的我们的Jimmy，它通过这个 k 去缓存里面去查找当前的这个对象，因为我们预期它是没有这个对象的，所以说它返回的对象是cats，是一个对应的一个 now 对象。


case，我们的 case 的内容是null，那么接下来我们看一下它就会返回我们一个 null 的出去。那么如果当前对象为null，接下来要做的事情是什么呢？它要对我们这个执行的一个结果进行一个处理，这个处理就是把我们当前这个cats，我们返回这个 null 的对象，它会构建了一个 put request，把这个 no result 这个对象去进行存储起来，这里面只是个临词的存储，它最终会看我们能不能从底层的业务里面获取到我们的属性，我们的真正的结果。


如果获取到结果，它会把这个 no result 进行一个替换，那么在这里面我们可以看到这里面我们需要进行真正执行我们的 invoke 的操作，那么我看一下我们在这里面操作的过程，会执行到我们的业务方法，我们快速的跟进去，这里面到我们的 find user，也就是说这第一次执行的过程中需要通过我们业务方法里面的数据库里面获取我们到我们的对象，这里面我们获取到我们的 user view，那么把 URL 给我返回过去，这里面我们可以看一下返回到这个对象以后他要做的事情是什么呢？需要把这个对象进行一个包装，这个包装成一个什么？把 written value 包装成我们一个可以进行 cats 的一个value，那么在这里面会把我们的 cats value 进行一个处理，处理成最终是我们的 collection put request，也就是说把我们这个 case value 进行，就是说搜集到我们的一个 put request 这样一个请求的一个集合里面，在这个集合里面它会进行一些处理，也就是在这里面执行 cats put request apply 方法，这个 apply 方法进行注了一个真正的一个缓存的一个设置的处理。


我们可以看里面在这里面有一个是 do 铺子的操作，这个 do put 的操作其实也就是把我们当前的 k 和 value 进行放到我们缓存的一个过程，这样的话也就完成了我们把从数据库获取到的对象放到缓存里面的一个过程，那么接下来我们进行最后一步操作，就是把有一些 cat 的 EVICT 方法再进行一次处理，这里面我们也是没有进行数据处理的，这一阶段也就是我们第一次我们通过数据库里面获取到我们的对象，然后把这个对象放到我们的缓存里面，过程就完成了。


那么接下来我们进行第二次查询，第二是查询，我们理所应当的应该是知道它要从我们的缓存里面去获取这个对象，那么我们来看一下它的执行效果，在这里面我们还是快速，我们看在这里面是。第二是查询它执行，通过我们的泛的 case item 里面去找我们的对象，那么我们的执行我们去跟进来看一下我们执行的效果，在这里面获取我们首先也是构造出我们的k，当前我们的 k 还是Jimmy，那么我们通过我们的 find in case 里面去获取我们这样的一个对象，我们在去获取的过程中我们已经得到一个 warpper 对象，这个 wiper 对象我们在进行一次拆包的处理，那么就可以作为我们使用了。


这样我们获取到我们的 cat head 它里面的对象的内容，我们可以看到它是一个 user view，那么在这里面它获取到对象，当前我们看到它是不为 now 获取完就把对象获取到，那么这样的话把整个这个对象进行一个解包，得到我们的 return value，这样的话就不再去执行我们刚才这里面看到的 invoke 操作了，那么就直接把我们的对象进行返回操作，这样的话也就真正得到了我们一个新的user。这个 user 它是通过缓存里面获取到的，那么我们整个这个过程也就是执行完成了。回过头来我们来看一下关于 string 缓存的内容，我们就先介绍到这里，同学们，我们下一节再见。

