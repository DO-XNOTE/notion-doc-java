---
title: 2-8 Spring AOP切面编程源码解析-1（1612）
---

# 2-8 Spring AOP切面编程源码解析-1（1612）

[image](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/1bd64cb6-121f-4d95-bd1a-6b997686c588/SCR-20240803-mmdg.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666UQBTRZO%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T232009Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDNolmiPSoI%2FqmO5xomfSoKMBo88OuSOvgXkfWqrg%2BqhgIhAMpYe9nfohJwTjmc8cbmqzttSmFwBLglmGsjjvFawwaRKogECMb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgxW4CulAf6qrQfalgEq3AP1B%2FYqtiX2zpkxbUaWN7JP%2F1FPrCKfFFMpUQ%2FjybCLGyGq7y4eNKAkE16GB1ox3AqelquQ7BwjUDHa3J9%2B0DBXDDobXVSYzE4RqP0Q9oUm0UxQckh4mNqN7D2e%2Fh9NlHuKr%2BbcI3L5Itdm%2FGkX0fc2HO8%2BYBU7GFkwwG4L%2BXmrLPYAS35I4GGoTCyu3bVhqWgO80EpXx8vK2PU4cNkk0XgoR00EDRRnP56639DMe6qoq6vFM%2BIokc11pl64lN4SiShJQMq53j1pvdtxwjCdQQYUHmmOUBWFLDgUS%2BMC81c%2BOHjJ915ruW4OvYxCDCu6aPbidSsiwJXxDODLsNCUfuqGt7JqX6st2OWntBKClumJu0KBMYknOvmAz4tsbqcvETcrdtk%2Bw%2BaRKY6bBNBhG4JJXf2IdbDw1G7ABGN16uftCziLx%2FSxh6nI894zxluj6pSsGIjlmyTcVvp8OAXwkRjc5OmeT9xqiaDGClIKQDxm%2BY9cvHG7%2B9Oj5E59T814289PZ9s5zOPnv7gDAVbuhcQa8pXXKKAo7COc8S4HShA6FfZyqD%2BAkvh9faVGy4dfW8Rd0nOPzDlVZvgzwMs9ZU9%2BBRDSQ%2BOXN9%2FobdoCsha4LKHukdltbx8tHrlkjCEt%2F%2FSBjqkAeuzhQi1y0P43ofssH%2B6w3wrctjtDgtdSWm4gSgtj5IBaFv1hMes3TrbuKcNjIGmNl0TJbwwdf8aQupsFPGqzvQb3J%2B2DaWKrplhryEa026yIulfh5BUw5l1cJxgkLrgyQXDw2b9USeqPFMD0tXWRVKlydrBIBHSonMkr8RXgBO%2BObPycnZt88cZTJBtkLBWhAXC2HM1Uh4n5MNPCnZXHPmkb7WF&X-Amz-Signature=26b871600ec640c8812a5487c5e1d4d2f4e815306d4f7d9a8d3ab15f99372e40&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

同学们大家好，这一章节我们学习 spring AOP 切面编程的源码解析。通过前面的 AOP 架构设计章节，我们已经了解了 spring AOP 的几个核心概念，比如说通知切入点、代理对象这些概念。这一节我们通过撤词案例来分析一下 AOP 的源码实现。这里面我们通过三个小节来学习 AOP 切面编程的源码。首先我们学习 spring AOP 的核心API，我们主要通过学习 prockets factory 来手工完成 AOP 代理的实现，手工实现的过程，让大家更清晰的理解 advice 和 point cat 等抽象概念。然后我们学习一下声明式的 AOP 实现原理，声明式的 AOP 可以支持 x now 和注解两种方式，我们会分别介绍基于 XL 的声明式 AOP 会带领大家更详细的理解 spring 加载 x 庙的配词过程，理解 spring 电影 XL 的命名空间机制。


基于注解的生命 c o p 是现在使用比较广泛的，我们学习 AOP 如何利用 a o seed 扩展机制完成 A o p 功能的植入。我们先来看一下 spring AOP 的核心API，很多同学工作多年在项目中使用到AOP，却很少关心 AOP 的底层实现，甚至不知道有 proxy factory 的存在，这也可以说是死不用。优秀的非侵入设计带来的便利性，让大家不用关心底层的实现。


我们来分析此中的源码，就从底层入手，让大家理解 AOP 的实现原理，我们知道在构建 AOP 的过程中，我们首先要知道我们要使用 AOP 做什么事情，也就是说通知，也就是我们对系统进行拦截以后，我们的增强扩展是什么内容？另一方面是我们需要在什么地方去做这些通知，也就是 point cut，也就是我们的切入点是什么？在 spring AOP 里面，他把 advise 和 point cat 进行组装，构建一个 adviser 对象，这个对象可以理解为是切入点和通知的一个组合，它基于这个组合去对我们的源码类进行扫描，去进行一些拦截。


那么我们来先看一下跟 Procast factory 相关的这些类，在这里面我们首先可以看到这里面是区分有通知切入点和切入点加通知定义的Advisor，以及我们定义的一个 Advise 的，就是切入点加通知，加上我们的目标对象，通过这三点生成我们的代理对象，我们称为 Advise 的。接下来就是我们真正构建我们的代理对象使用的 LP profile factory。在这里面我们会通过我们不同的实现采用 CD Lib 代理和我们的 GDK 动态代理。在我们的通知过程中，我们这里面有 before advice、 off 的 advice 以及我们的一个拦截器，在这里面，像。
off 的advice，它有Sobel。


advice 和 off 的 returning advice，这两个分别对应的就是我们在执行完成以后是抛出异常或者是正常结束。对于 before 的 best 最常用的也就是 match 的 before 的 best 运营这些接口，它有各种不同的时间类，待会我们会通过这些去演示一下如何使用。


对于 point cat 类目，对，其实就是对我们的类去做一些过滤，同时对我们的方法名做麦子，也就是说我们能扫描对应到的我们的 class 以及我们的方法名能匹配到，也就是可以作为我们那个 point can 的一个切入点。下面是 point Advisor，是 spring 为了使用方便对我们做了一个抽象，它的实现类一般是 debug point cat Advisor 去做一个组合。


好，我们接下来看一个相对比较简单的一个 proxfactory 的使用，在这里我们可以看到我们首先构建我们的Hallobin，这个对象在使用 Hallobin 的过程中，我们先创建 proxv factory，通过 profactory 名设置我们的target，也就是我们的 Hallobin 作为我们的一个目标对象，然后添加advice。这里面的 advice 我们使用的是一个 mass 的 interceptor 的一个拦截，也就是我们的方法拦截的一个自定义的实现。通过添加device，然后我们从 perpacks 去 get perpacks，也就是我们从一个代理工厂获取到我们的代理类，那么基于这个代理类，我们执行我们的 say hello，它就会进行我们的一些拦截操作，也就完成了我们整个 AOP 的过程。


那么在这个过程中，我们要可以看到我们 Procast get class 它的类，它并不是我们原生的 Halo Bee，它是使用我们做了一项代理，我们接下来去通过代码演示看一下这个过程。在这里面我们先执行我们的运行操作，我们可以看到首先是通过构造方法生成我们的对象，在这里面我们获取到了我们的代理类，我们可以看到代理类是一个通过 CD lip 增强了的一个代理类，它并不是我们原生的 hello bin。那么执行完成以后，我们看一下我们在执行我们的业务方法的时候，这里面会执行一个 say hello，一个 before 一个操作。也就是说在我们执行我们真正的业务方法 say hello 之前。


它会调用了一下我们争前的业务类，我们可以细致的分析一下这个方法。首先在这里面我们为这个 proxy factory 构建了一个advice，这个 advice 我们可以点进来看一下，它是 customer must be for advice，这个 advice 它实现了 must be for advice 这个接口。在这里面我们在方法执行之前，我们去做了一个操作，这就也就是说打印一个before，就仅仅这样一个操作。那回到这里面，我们看我们在设置 target 的时候，我们把我们 new 出来的 hello being 去设置进去，为我们的代理的目标对象。在这里面我们特意做个实验，我们可以看到刚才生成的这个proxy，它是基于 CD live 生成的，那其实我们知道 spring ao p 在创建代理类的时候，它可以通过 CD live，也可以通过动态代理。我们知道 hello bin 这里面我们是实现了一个 hello 接口，但是在这里面它默认获取到的是一个 CG Lib 的接口。那么如果说我们是想需要通过加入动态代理的话，我们可以在这里面去指定一下它的INTERFACE，这里面 4 指 hello INTERFACE 这样一个接口，这样的话我们在获取这个代理的时候，获取到的就是我们的 Java 动态代理。来，这样我们可以再执行一下，看一下效果。


考勤，我们可以看到执行的这个proxy，它是 com sound，它就是 Java 默认实现的动态代理。通过这样可以看到，如果说我们是需要通过 Java 动态代理或 city lab 代化，就是看我们字有没有默认使用我们的接口，这是一种判断的方式。另一方面我们也要知道 CB live 代理，它是对我们的 Hallobin 构建了一个子类，所以说 Hallobin 一定不能是 final 类型的。


这里面我们可以看一下这个对应的advice，我们这里面用的是 master before advice，我们可以看一下这个advice，它的一个树状结构，我们可以跟进来，它的最顶级的结构就是advice，我们可以看一下它的这个继承体系，在这里面 advice 它这里面有一个intercept，就是我们方法拦截可以使用它。我们另一个测试力可以用 must intercept，这里面还有 before advise，这里面是 off 的advice，对于 before advice 下面有 must be for advice，还有它的一些子实现，这是我们制定的实现，这是 object 接 must debug advise，这是 spring 给我们提供的实现。另外对于 off 的advice，它可以在区分 scope advice 和。我们这里面是 after return of the advice，这就是我们介绍的。执行后的话，它可以分两种情况，一种是正常完成，一种是抛出异常。在这里面我们可以看我们另一个测试用例，我们另一个词用例，我们是执行的，是我们的方法单阶，在这里我们可以看到这里面我们定义的是一个 advice 是 cost must intercept，也就是说我们定义的方法拦截，对于方法拦截来说，我们可以理解为它是做前后处理，也就是我们经常会用于 around 的情况。


对于 around 的情况，我们使用 must intercept 去做这个事情，我们可以看到在这里面的词线的 match 的 insect 接口，它对应的方法也就是我们的 invoke 方法，它的参数是一个 master invocation，这个 invocation 我们可以看一下它里面能获取到哪些信息，这里面我们可以从这里面看到它能获取到的信息。这里面有对应的argument，也就是参数 mest 和相关的一些静态的一些信息，这里面是当前对象和一个process，就是执行的过程。


好，我们回到这个方法，那么在这里面我们执行一下我们这个测试用例，对于这个测试用例来说也是比较简单的，我们可以执行一下，看一下它的效果。好，这样执行完成以后，我们可以看到它是在执行我们的业务方法 say hello 的时候，执行一个 before 和我们 off 的。 before 和 off 的都是我们在这个方法拦截里面去实现的内容，这里面 before 和 off 的整个这个过程执行完成。那么我们可以看到在这里面我们虽然是手工实现了 AUP 的功能，但是我们可以看到我们有一个 process factory，我们有一个 target 对象，也就是说我们的 hello bin，这就是我们的目标对象，我们还有 advice 争抢，但是我们这会儿可以注意到我们可能缺少了一个条件，也就是我们的 point cut。我们的切入点好像并没有明确的指出来，这里面需要跟大家说的就是我们在手工定义 Procast factory 的时候，我们指定了 pocket 的对象和我们的advice，那么它的默认的切入点就是整个这个 hellobin 的输入方法，我们可以在这里面去执行一下，我们甚至执行这个对应的 to string 方法，它也会执行相应的操作。


我们可以看到在这里面我们执行一下 to spend 方法，执行 to string 方法的时候，它也会执行一个 before 和 off 的相关的一些超准，这里面是 before to string 和 off 的 to string。从这里面我们可以看到，其实也就是说我们在走工具指定的 advice 默认它会把我们所有这个对应代理类，也就是说我们的目标类它所有的方法都会进行一层代理。那么如果说我们想针对性的去把某些方法去做代理的话，我们就需要指定我们的 point cut 了，那么在这里面我们还有一个可以指定 point color 的方法，在这里面我们可以看一下结构也是一样的，我们在这里面构造hallobin，构造 project factory，我们设置target，在这里面有一个区别。


我们首先在这里面定义了一个advice，这个 advise 也是我们的 customer mass 的intercept，也就是我们的方法拦截。在我们 advise 基础上，我们又定义了一个 point cut，这个 point cut 也是我们自定义的一个 point cut，我们可以先不管它的词下内容，我们通过 advice 和 point cut 构造出一个 default point cut a version，这个 a version 怎么理解，我们就可以理解为它就是 point cut 和 advice 组装的一个对象。


组装完成以后，我们把这个 adviser 添加到我们 positive factory，这样的话它执行它就会有针对性地去执行我们所拦截的方法。我们看一下这个 point cat 它的实现结构，我们可以看到在这里面，对于这个 palm cut，它有两个方法需要我们实现，一个是实现我们的match，也就是我们对于方法的一个确认，另一个是我们获得我们的 get cost filter。


在这里面我们看一下我们对于 COS filter，它作为两个方式的过滤，一个是过滤我们的类，一个是过滤我们的方法。对于我们的类的过滤，我们这里面定义了一个匿名的实现，这个匿名类词线，我们看这里面我们实现的内容是我们 return class equals Halloween，也就是说如果我们当前这个 bean 它是Halloween，那么我对它进行过滤，也就是说命中。


那么首先命中classfilter，其次还有一个特点，就是说我还需要命中它的方法，它的方法是什么呢？它的方法名要以 call say hello，也就是说它必须是 c hello 这个方法我才能去进行拦截，除了 c hello 以外的方法我不拦截，所以说在这里面我们针对刚才的测试，我们在执行 c hello 的时候，它应该会执行我们的 AOP 拦截，执行 two string 方法的时候，它就应该不会再执行我们的拦截方法了。那么现在我们可以执行一下，看一下效果。


中间我们看一下这个 AOPT 拦截，我们现在看到 AOPT 的拦截只是拦截了 c hello 方法，它并没有在这里面拦截 to string 方法，这说明我们这个 pandecut 它现在是生效的一个状态。好，我们这样的话可以用指定 pincut 的方式去拦截指定的类和指定的方法。


那么我们来再看一下这个 porx factory，它去获得我们的代理类的过程中发生了什么事情，我们可以跟进来。在这里面我们点击一下 get perfect，我们看一下它做的一个什么事情，在这里面我们可以看一下 perfect factory，它里面的方法是很多，你像这里面是属于我们继承负类的方法，我们可以再看一下，这样的话就是单纯我们看 proxy factory，它的方法就是除了 proxfactor 的构造方法，就是 get proxy 的方法。这里面 get proxy 提供了几个不同的参数的传递。


这里面我们看一下我们这个无参的 get perfect，在这里面它执行的过程，首先它会去执行 Pre LP Propass，我们看一下它执行的操作是什么呢？在这里面它会得到一个 AOP process 这样一个类，通过这个类再去创建获取我们的 get provide，也就是说真正 get process 的操作是委托给我们 create LP 的具体操作来执行的，我们看一下对于这个方法，它是一个接口，也就是 LP perfects，这里面我们看一下它具体的实现，这里面我们可以看一个是 CD Lib 的一个实现，一个是 JDK 动态代理的实现。这样的话我们知道其实就是在这里面去区分了我们 CD lab 和动态代理的实验。


那么我们可以看一下对于这个方法，我们 create OP proxy，它在什么情况下去获得了JDK，什么情况用的是 seed lip，这样我们跟进去看一下，这里面我们看一下获得这个方法，也就是这里面有一个 debug AOP profess factory，在这里面是 create AOP 代理。


那么基于这个方法我们可以看一下它助了怎么操作，首先我们可以从这里面看到它在里面去注了判断，如果说是满足一定条件是 JDK 的动态代理，其他情况下是基于一个 CG lip 的一个动态代理。这里面是什么我们可以看到，首先是 target class 意思 interface 或者我们的 pockets 意思是一个代理类，那么它就会采用我们的 JDK 的动态代理，其他情况下会使用 CD Lib 的动态代理。另一方面就是我们看在这里面还有一个判断条件。


当不满足指定的这几个条件的时候，它直接就会采用 GDK 的动态代理，我们可以跟进来看一下 GDK 的动态代理和我们 CD live 动态代理的区别，在这里面，对于一个 DDK 的动态代理，它的参数也就是 advise 的support，也就是我们定义的我们的 advice 和 point cut 它的一些组合的一个对象。在这里面它可以就是直接获得 get process 的构造方法，也就是我们获取代理的方式。传入对象 class loader，在这里面是通过 Procast new proxy instance 指定一下 class loader 和指定一下我们的interface，传入当前对象就构造出我们的当前的一个代理对象。


我们再看 CD Lim 的动态代理，这里面 CD lab 的动态代理，它的实现方式也是一样，通过午餐的 get progress 去间接的调用 get price，指定一下我们的 class loader 为参数，在这里面的调用过程是相对来说比较复杂的，这个过程可以大家不用太细致的了解。


大家知道我们真正的我们的代理类的构建过程是通过 profile factory，它间接的去使用我们的 CG label 或动态代理去完成就可以了。好，回到我们的 PPT 这里面我们去了解了一下通过 perfect three 构建代理对象的方法，同时我们也知道我们可以不依赖 string 容器，是使用prohibit。
tractor 的方式构建一个指定的一个 target 对象的代理对象，然后通过这个代理对象执行我们的一些 AOP 的一些拦截操作。

