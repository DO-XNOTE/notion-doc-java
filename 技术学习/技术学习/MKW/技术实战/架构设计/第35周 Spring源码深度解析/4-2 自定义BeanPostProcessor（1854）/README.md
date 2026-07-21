---
title: 4-2 自定义BeanPostProcessor（1854）
---

# 4-2 自定义BeanPostProcessor（1854）

[image](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/7743919b-1161-4849-ac21-7a1f31a9fa96/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664MDIFBJU%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T232025Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIGdOa2oxhOuzOoj8CZlFFlXP2WW6xEdoAq7cKRmElzXmAiEAijX6KoouGVQVd3vKxVuDbzbLJN2xgCwVT2K9Gqz%2BH%2FsqiAQIxv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDKRDxg2m3qLiZIZBDSrcA2wWmZU59aElqBSio7gJXOmPkyIqmu1L3rkGIoeVsz2jaSH1rE0pOUbDGvYo%2FCRGym1vDPl7uwoVOffQtAg48%2FFKL8lLyyWaiFeSwl8p8mntHhewT4XpFE4evbgtGyL7%2B1DQ%2FUDkgjteNyT%2FRvkezl5ixmDaKyczElx60fHjwAW%2BAXDAerKOIdJ%2BrR5HTdlaTegc77NJB%2FXtEbDsglhXT6h8wY%2BVjhvUKHKh8Mfnpdjhvj55vaM4qhhHChYH9558ireTvkQ5YVUIl3NuezGtcmQo6pNPz6ljMh7fEkRQLv7ZR0MDInD6ki1rU5iSSNYOaE%2BLvNcaOxPXMWqTQptoe%2BKmxB0kBZEURpfdlAd0FzDPoE3fuveFLprdO4aNsFeSsYm5ENUWoNzewlUaydXk7gumaDOo6PvTy8f6z61WgpCFOhxwSYH6l%2BUxIvxAq2%2F%2FVVoPeZU9ej566PXv1RxQCZJPcV3yVCqN8PK%2B35trP77HgVxf1y7f5QLFoO%2Bv%2BTvUU7szcmAUkxX26aO0CEx7JJtzCBwGD0ziLYsRVHlPz6GX8OQIvQULWEDVrXAz6fZblrIrO4n8Eo9jLy5YPfjWJrFEsDKukHfke5q%2Bg3%2Fk4jjYfS5gBxS5x%2BCLqdl0MMm4%2F9IGOqUBUbCfoBax5MhQYF5%2BL6sHIKjNYyyIG8iNr3%2FPcH8KSMyKw2exy35LseTcj4IcDS34jAkh%2BSlDj5t1FWWmziyNiWoc0shTkUJXSjrw0DxWTpQbtRLc4jdMMPs6fBF5F%2BHiawXM8j8WNq2e1G50jC%2FT5CeYT%2FjmESPjAwXgp5vuy1zKhQJhcN560qzjUkv3BZqLUxuRLQ76HdoRqswhnzcGS3z45Tum&X-Amz-Signature=e1b8b602fa98de5cf655da1e78987bca13ca823a81705234e7c7e10e63cf0ecf&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

[image](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/e5428dac-ca25-44d7-9012-88b1de2ae1db/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664MDIFBJU%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T232025Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIGdOa2oxhOuzOoj8CZlFFlXP2WW6xEdoAq7cKRmElzXmAiEAijX6KoouGVQVd3vKxVuDbzbLJN2xgCwVT2K9Gqz%2BH%2FsqiAQIxv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDKRDxg2m3qLiZIZBDSrcA2wWmZU59aElqBSio7gJXOmPkyIqmu1L3rkGIoeVsz2jaSH1rE0pOUbDGvYo%2FCRGym1vDPl7uwoVOffQtAg48%2FFKL8lLyyWaiFeSwl8p8mntHhewT4XpFE4evbgtGyL7%2B1DQ%2FUDkgjteNyT%2FRvkezl5ixmDaKyczElx60fHjwAW%2BAXDAerKOIdJ%2BrR5HTdlaTegc77NJB%2FXtEbDsglhXT6h8wY%2BVjhvUKHKh8Mfnpdjhvj55vaM4qhhHChYH9558ireTvkQ5YVUIl3NuezGtcmQo6pNPz6ljMh7fEkRQLv7ZR0MDInD6ki1rU5iSSNYOaE%2BLvNcaOxPXMWqTQptoe%2BKmxB0kBZEURpfdlAd0FzDPoE3fuveFLprdO4aNsFeSsYm5ENUWoNzewlUaydXk7gumaDOo6PvTy8f6z61WgpCFOhxwSYH6l%2BUxIvxAq2%2F%2FVVoPeZU9ej566PXv1RxQCZJPcV3yVCqN8PK%2B35trP77HgVxf1y7f5QLFoO%2Bv%2BTvUU7szcmAUkxX26aO0CEx7JJtzCBwGD0ziLYsRVHlPz6GX8OQIvQULWEDVrXAz6fZblrIrO4n8Eo9jLy5YPfjWJrFEsDKukHfke5q%2Bg3%2Fk4jjYfS5gBxS5x%2BCLqdl0MMm4%2F9IGOqUBUbCfoBax5MhQYF5%2BL6sHIKjNYyyIG8iNr3%2FPcH8KSMyKw2exy35LseTcj4IcDS34jAkh%2BSlDj5t1FWWmziyNiWoc0shTkUJXSjrw0DxWTpQbtRLc4jdMMPs6fBF5F%2BHiawXM8j8WNq2e1G50jC%2FT5CeYT%2FjmESPjAwXgp5vuy1zKhQJhcN560qzjUkv3BZqLUxuRLQ76HdoRqswhnzcGS3z45Tum&X-Amz-Signature=1e534793f5934d4288f34c9f8418f70c7ba76d7184fbf6d99002645ab17ed33e&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

[image](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/59e6dcd1-5875-4deb-9495-252980818a41/SCR-20240803-rvss.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664MDIFBJU%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T232025Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIGdOa2oxhOuzOoj8CZlFFlXP2WW6xEdoAq7cKRmElzXmAiEAijX6KoouGVQVd3vKxVuDbzbLJN2xgCwVT2K9Gqz%2BH%2FsqiAQIxv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDKRDxg2m3qLiZIZBDSrcA2wWmZU59aElqBSio7gJXOmPkyIqmu1L3rkGIoeVsz2jaSH1rE0pOUbDGvYo%2FCRGym1vDPl7uwoVOffQtAg48%2FFKL8lLyyWaiFeSwl8p8mntHhewT4XpFE4evbgtGyL7%2B1DQ%2FUDkgjteNyT%2FRvkezl5ixmDaKyczElx60fHjwAW%2BAXDAerKOIdJ%2BrR5HTdlaTegc77NJB%2FXtEbDsglhXT6h8wY%2BVjhvUKHKh8Mfnpdjhvj55vaM4qhhHChYH9558ireTvkQ5YVUIl3NuezGtcmQo6pNPz6ljMh7fEkRQLv7ZR0MDInD6ki1rU5iSSNYOaE%2BLvNcaOxPXMWqTQptoe%2BKmxB0kBZEURpfdlAd0FzDPoE3fuveFLprdO4aNsFeSsYm5ENUWoNzewlUaydXk7gumaDOo6PvTy8f6z61WgpCFOhxwSYH6l%2BUxIvxAq2%2F%2FVVoPeZU9ej566PXv1RxQCZJPcV3yVCqN8PK%2B35trP77HgVxf1y7f5QLFoO%2Bv%2BTvUU7szcmAUkxX26aO0CEx7JJtzCBwGD0ziLYsRVHlPz6GX8OQIvQULWEDVrXAz6fZblrIrO4n8Eo9jLy5YPfjWJrFEsDKukHfke5q%2Bg3%2Fk4jjYfS5gBxS5x%2BCLqdl0MMm4%2F9IGOqUBUbCfoBax5MhQYF5%2BL6sHIKjNYyyIG8iNr3%2FPcH8KSMyKw2exy35LseTcj4IcDS34jAkh%2BSlDj5t1FWWmziyNiWoc0shTkUJXSjrw0DxWTpQbtRLc4jdMMPs6fBF5F%2BHiawXM8j8WNq2e1G50jC%2FT5CeYT%2FjmESPjAwXgp5vuy1zKhQJhcN560qzjUkv3BZqLUxuRLQ76HdoRqswhnzcGS3z45Tum&X-Amz-Signature=58a9e2e0161c296b85b80c0059aaee0b8dae7172923985acb2efab9709320585&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

同学们大家好，这一节我们来介绍一下 spin 二次改造中的自定义 Bing post process。我们在开始之前先回顾一下 Bing post process 这个后处理器的一些工作过程。首先 bin pose process，它是在容器初始化 Bing 的过程中提供了一些干预性的一个扩展，它提供了两个方法，分别是一个 post process before in its lesson 以及我们的 post process up 的installation，也就是我们在 being 在构建之前，也就是初始化，也就是 new 这个 being 之前和之后做一些事情。同时我们可以在基于 before in s lesson 去用我们的方式去创建这个bin，这样的话它就不会使用 spring 容器默认的这个 bin 去初始化，那么对于 post process off 的installation，也就是当我们整个这个 Bing 的初始化完成我们的一些后处理，我们可以基于在 spring 容器对我们这个 bin 的初始化的过程，再做一些我们自己的一些扩展。


那么好，我们现在去构建一个我们的这个工程，来去跟大家演示一下并 pose process 的处理过程。现在到我们的工程模块里面，我们准备在 showcase 下面创建一个我们的 spring customer，这个模块用来去做我们的二次改造的相关的内容，在这里面我们去插件模块。好，我们下一步在这里面我们看一下，我们是这里面是选中的 study showcase，首先我们在这里面对我们的这个包的模块名称进行命名， spring custom，同时对 r tip ID 我们进行一个简单的一个结构的改造，我们在这里面 showcase 跟我们这里面的模块做的保持一致。


好，那么我们现在点击完成。好，现在我们创建完成以后，我们打开这个模块简单看一下，在这里面是一个空白的模块，我们并没有什么依赖，那么我们先把我们的一些常用的依赖添加进去，那么常用的依赖我们这里面选择哪些？在这里面我已经定义好了一些，把它直接给我们去拷贝过来。跟这里面跟大家简单说一下，这里面也就是首先我们的 spring context，因为它默认去依赖了 spring core 和 spring beings，这里面我们是需要做一些测试工作，是 spring test 以及只有你的丘比特。这里面我们定义引入了通过 spring boot STARTER，引入了 E N 4 相关的内容，还有我们经常用到的 long book 这些我们的依赖。


添加完成以后，现在我们需要做的事情就是创建我们的包结构。那么在创建我们包结构的过程中，我们要做的思想是先把我们的，我们通过创建类的方式把这个包结构创建完成好，这样我们得到这样一个模块儿，那么在这里面我们去构建一个 being 的目录，在这个 being 目录里面我们定义一些我们常规的一些业务开发需要用到的一些bin。


在这里面我们可以首先来定义一个 demo model，通常这个 Demo model 里面我们会用 long book 的 at date 这个注解去修辞，并且我们跟它指定一下一个常用的属性，这里面我们会指定一下 ID 和对应一个name，这里面根据一些警告我们去解决一下它这个黄石的警告。


那么对于这一个最基础的model，我们来可以构造一下它相对应的一个DAU，这里面我们去构建 model d o， Demo deal，对于这里面我们现在并没有使用到接口，那么对于 Demo deal 通常我们是会需要去进行一个数据的正常改查，因为我们这里面其实作为颜色我们并没有去做真正的数据库的操作，那我们还是以一个 concurrent Hashmap 作为我们数据的存储方式，好，我们这里面去声明一下。


引入好，这样的话我们以这个 contain high mail 作为我们数据存储的一种方式。那么接下来我们给这个 Demo DO 构建一个最简单的方法，也就是给这个方法提供一个创建的一个操作，那么我们这里面去写一下这个创建的，对于这个创建 Demo model 操作，它肯定是需要一个 Demo model 类型的一个参数，那么这里面我们把这个对象存储到 Hashmap 里面也就完成了。那么这里面我们还是通过 model 点 get name 作为它的key， model 对象作为它的value。同时因为我们在正常把我们的 model 放到我们的行业版本里面会有一个返回值，那么我们这样正常返回过去，这样也就完成了我们最基础的一个 Demo model，我们的 Demo 的 d o。


接下来我们来写是创建我们的一个 Demo 的一个service，好，对于 Demo service 的话，它的方法我们也是在这里面提供相同的一个 create model，因为我们对 Demo service 它是需要依赖对应的我们的 d o 的，我们在这里面去依赖。注入一下。


好，我们正常可以通过 add all swear 把这个写进去，这里面我们的操作就应该是通过 demo DU 点 create 我们的，从这样看的话，我们这样最简洁的一个对应的 Demo 的 d o service 就完成了，那么我们在这个基础上去做我们的 impose process 的操作，那么我们要做一个什么事情？我们可以这样去想，对于我们在这里面写的这些 bin 的话，像 demo d o 和 demo service 都是我们自定义的这些bin，我想对我这些自定义的 bin 来做一个扩展模块的一个名称，比如说我们给它指定一个名称，在这里面我们可以通过这种方式我跟大家去介绍一下这个需求的，对于这个需求的话它就我们可以先定个接口，对于这个接口我们可以理解为是这个模块儿名称。


那么我对于所有我们自己实现的这个接口儿，让它实现这个接口儿，同时可以跟它进行一个统一的一个模块儿名称的设置好，我们在这里面对于它我们可以定义一下对应的 get set 方法，这样我们就定义了这样一个接口，对于这个接口我们让所有的 d o 和 service 来实现这个接口，我们看一下实现完的，在这里面实现完接口对应，我们需要实现这两个方法。


我们看，首先我们需要去get，我们这里我们可以返回 return race，我们并没有在这里面创建这个属性，那么我们让它去自动把使用性创建完成属性以后，我们在这个set，这里面我们需要去定义一个我们的参数，这里面我们讲了色子。好，这样我们这个操作就完成了。那么同样的我们的 service 也要做相同的操作，我们可以在这里面把对应的内容我们复制过来，复制完成以后我们这里面也是让它实现这个model。好，这样的话我们这两个 DAU 和 service 就同时实现了 model name able 的这种操作。


那么我们想在不同的模块，我要对这个 model name 设置一个相同的名称，也就是说我们这个模块作为公用模块，它在不同的系统会需要设置不同的模块名称，那么我们可以做一个这样的事情，那么这个事情我们就通过我们的 bin post process 来完成。


那么现在我们在这里面是设置一个 configure 的一个包结构，在 configure 包结构里面去创建我们自定义的 bin process，我们起名称我们可以就 cost custom b，那么对于这个 Bing post process，我们知道它应该去实现， being pose process，在这里面我们可以看到对于 being pose process 这个接口，它现在是默认有两个。


对于这个方法已经有实现，我们如果说实现的话它并没有报错，那么对于我们来说，我们肯定是需要对它进行一些实现的，那么我们要做的事情，我们可以在这里面去覆盖它的默认方法，我们选中这两个方法。对于 post process before installation，也就是说我们正常的话，我们应该把它输入的这个值去返回过去，我们不管这个值有没有，我们都需要把它直接返回过去。对于 post process 的information，我们也是需要把它默认值作为 return 的条件返回过去，那么对于这样一个空的一个 been pose process 已经完成了，那么如果说我们要做我们自己的业务的话，我们需要去做一些判断，去做一些操作，比如说在这里面我们要判断如果说它是某个指定的类型我们去创建的方法。比如说我们可以这样，对于这种情况下，我们通过在 before installson，在初始化之前进行一个我们自己创建的一个 demo d o 的操作，就把我们使用默认创建这个对象的方法给覆盖掉了。


这样我们去做一个举例，那么我们更重要的事情是需要在这里面去完成，也就是说在 PROS off 的instance，也就是在它的后处理的过程中，我们去做一个操作，操作的逻辑是怎样的？我跟大家去写一下，看一下只要它实现了 model name able 这个接口，那么我们就在这里面给这个对应的 bin 设置 model name 这个名称，设置一个指定的一个值，可以看一下，我跟大家设置一个名称，这个名称我们可以去制定一下，只要保证它是我们对应的值就行，我们可以在这里面去写一下是不用custom。
好，那么这样的话我们这个后处理呢就完成了，现在我们需要去做一个验证一下，我们得到的 bin 对应的这个 model name able，对应它的 bin 的后处理的值是不是都已经设置完成了？行，我们在这里面去通过它去创建一个test。好，我们现在用 DN IT 5 的方式。好，现在我们在这里面写我们的代言战士。
好，在这里面我们需要这里面去做一个注解的config，因为我们要基于注解的方式去完成。


大家注意一下，这里面我们并没有直接去指定给定注解的名称，那么这里面我们的对应的加 configure 的配置，我们可以在这里面写一个内部类的方式去实现。
这里面我们把我们对应的声明这个 customer being put a process，在这里面用个 being 的方式去注入进来，这是我们常规注入 be in a pass，我们直接 return 一个 new 一个 customer purpose，这样我们就注入完成了。那么同时在这里面我们通过 context 点 regist configure， b 把这个类注入进来，我们再对我们这个 name 进行一个 refresh 就完成了。


那么这样完成以后，我们现在要注意的事情是什么呢？我们需要从容器里面获取到我们对应的这些 model beings，那么我们看一下它返回的内容，是不是我们再判断下的 model name 是不是我们所需要的。我们这里面是 get be name for type。


我们这样做的意思就是把我们所有的 model name able 的这样 the bin 的名称获取到，获取完名称以后，我们取出一个遍历，我们通过名称去获取一下它对应的这个遍，这里面我们选的是这里面的词是该的 b 指定类型，这样呢我们就得到这个bin，那么得到了bin，我们要做的事情是什么呢？我们验证一下这个对应的 model 的 bin name 是不是我们在这里面设置的刚才设置的那个名称。好，我们现在我们可以 log 打印一下。好，我们在这里面去，让助理声明一下我们的日志，这里面我们使用 long book 的方式去说明，是非常方便的。这里面我们去输入，首先是 be name，接着我们再把对应的 being model name，打印数出来。好，我们看这里面是 being 点儿 get class，点儿 get simple name，这样得到一个较短的名称，我们在执行 bin 的 guide model。


接下来我们可以拷贝一个 logback 的配置文件，规范一下我们日志的输出。好，okay。好，我们再切换到我们的测试类，看还有没有其他问题。这里面的 configure 应该是一个静态的，同时如果这样我们初始化的话，我们已经把 custom being post process 方案进来了，那么我们需要对于我们这里面的 demo deal 和 Demo service 去做一些处理。这里面是加上我们对应的初解，我们可以去看一下里面我们 at repository，这里面的 d demo， d o 是对应的 at service，这是我们常规的一些操作。好，那么现在我们去执行一下我们这单元测试，看一下它的结果。


好，现在我们看到这样，我们现在得到了两个跟 model name able 相关接口相关的必应，一个是 Demo DU，一个是 Demo service，同时它们的 model name 都设置为我们的 spring cost model，这样说明我们这个 Bing post process 其次已经执行完成了。但是有一点要注意的是，如果我们通过注解的方式，用这种方式去注解这个 being pose process，那么它有一些 bin 是不能生效的，比如说当前这个 configure bin，如果当前这个 configure bin 也是实现了 model name able 的话，那么它就不可能把这个 model name 放进来。那么我们可以去做一些验证，我们验证一下这里面，我们同时也让这个 config being 去实现这个 model namable，同时我们把这里面的一些配置可以快速拷贝重用，这里面要跟大家说明的问题是什么呢？就是说当前我们这个 bin post process，它属于这个 configure bin，那么在它的构造的过程中必须 configure bin 先实例化完成。所以说我们用这种方式去执行的话，对应这个 configure being 的，它是不可能去执行到 customer being poster 对应的一些方法。那么我们现在去看一下这个执行的结果，我们现在再执行一下单元测试。


好，现在我们可以看到我们现在得到了 3 个b，当然是 d o service 和我们这里面的是配置的 config b，那么我们看一下对应的 model name，那么对于这个b，它的 model name 是now，其他的 model name 是 string cost models。我们可以看到问题，也就是说通过注解的方式对应的当前数组的这个 config bin，它是不可能执行到我们对应的 bin post 方法的。那么如果说我们想执行这个方法怎么办？我们可以这样做，我们在这里面把这个 custom being positive 注释掉，那么我们不再使用注解的方式注入这个 being possible test。那么我们通过哪种方式？我们通过 API 的方式，在这里面，我们如果说需要注册这个 being positive，我们需要通过 context add 我们的 p n taxary，我们看一下得到这个 being factor，这个对象是什么？这个 being factor 的对象是 configurable listable being factory。它可以做一件事儿是什么呢？也就是我们这里面是 ID be imposed，那么在这里面我们是只要 new 这个对象就行了，把对象 new 完成，那么我们现在去执行一下，看现在的效果。


好，现在我们看啊，最起码还是 3 个b，那我们重点看一下这个 b 对应的它的 model name， string cost model 它已经打印出来了。这说明我们通过这种方式的话，其实能解决当前，比如说我们宿主这个注解 bin 它这个post，也就是 bin post process 不生效的问题。好，那我们自定义 Bing post process 的内容就先介绍到这里，同学们，我们下一节再见。


