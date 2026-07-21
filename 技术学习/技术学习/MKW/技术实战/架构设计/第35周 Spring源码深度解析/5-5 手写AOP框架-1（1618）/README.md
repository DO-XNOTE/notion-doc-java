---
title: 5-5 手写AOP框架-1（1618）
---

# 5-5 手写AOP框架-1（1618）

[image](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/17f3a0a7-a2e8-4a4c-b36b-7a37a6fa8864/SCR-20240803-uoyi.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46677SGYOWN%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T232032Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCHMMhA8vL6QyBHNaqatmwDctkz%2FviYb%2BYROc9kU66qiQIhAMDkna2k%2Fb5iI9LP%2FxLTA4LEZ%2B3xEEUI9AelMW8Z0ZXGKogECMb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1Igw0Qz4dk%2B2HUYhBSksq3ANeLTqJ46y%2FiOGB5W9JzogtbRSP2qRJFirEonacvi1gVRva7D%2FnXrLev9gjmjxOB%2BH33qWZw35uMxv%2BAvC4zULyBUGYD%2BcxWmLQ2Xkj%2F6lROnOOen%2FzQxUzRJ5ZXy9JL9ZLsH68XTQWGgwZvhQmXFrA69T01%2BHxSQwrMRIdOzkszNitL%2B5uVa%2FbCQc%2B5Qp%2FScfMlKgDiVjii9VH%2Fw3TyJcpKbF2sHMCznOTsJMlxQFc6qBnBhooRfXaT2ZEv2ID8dq2HXbnJINU53ZTFbGLKqdbnc%2B0FaDJGNyTABiw%2BcNuyx9UGRIa0w7xs2%2FU0aLLbAha9ptV90QyAP9vKFi8RmRHVeDR4xKIsxqlG5pr6yxTo0eqt8L2beh8KifBCG5zqGveJcIR%2B8LhiKi6fZLaG%2BjIeEheVrTj0c3D2KQdk%2FOmD3tZceveo%2BtbWrhvpMdIl9Sc9hUNMkWrCZ2RvCPOMUxNgXbNrEEjkRd8EqDxg33r59OlJYL8cXqOmBBaqqXve3Pk1rYQxReZHuiZGuFbD0qsNJJsbWzUOWWwjjybG4Zk8N8Jlr6%2F2LAeMgBfj4xYISq2AejM0SXskuoNjSj9RM8m3baFFHLH4yz2DRZjlux4b%2FeLOQhsdkxuygCSPzChuP%2FSBjqkAZzbDbV9XIh7puM143lqseiSFm9i4vzqqq%2Blnq9QY0K4FnMerHSMhIHqV0Jf5GPa2Vz7Bt7d9l05fL74kMurGdelhMb42PM6YsjuquGAzSC7eUCq7VQdkpUplbDKn3QKUCc8qQzglVf7FWrKACdCHxjj%2BW0Zul6LdQKrMgiM0VyLu04F36FUQYBnUELfqRt7Wq4o2M4ywXig%2FRXjMzw7AfoTw1lY&X-Amz-Signature=fa298b6ddc7eba62f0d940ad3e1e02d55d4c1d23738f17ab1e211a4680418757&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

同学们大家好，这一章节我们来介绍 spring 造轮子手写 AOP 容器。 spring 的 AOP 框架设计是非常巧妙的，让我们通过注解就可以完成 AOP 编程。 OP 框架它是依赖核心的 bin 容器，我们这里面的手写 OP 框架也会依赖上一节写的 IOC 容器，还是维持我们照轮子的态度，在短时间内实现完整的 AOP 框架也是很不现实。我们使用开源技术也经常宣扬不重复造轮子，我们造轮子是为了让大家更好地理解 spring AOP 的实现原理。


现在我们来回顾一下 spring AOP 的实现原理。首先 string 框架它做了一件什么事情，它把我们 AOP 里面定义了一些相关的概念，在这里面向我们是我们的目标类，也就是我们需要被代理的类。我们通过advice，也就是说我们要增强什么内容，也就是说在我们的方法之前或之后，或环绕去添加一些什么内容。那么 point cut 它是指我们在哪些方法上进行一些处理？那么 advice 和 point cut 它组成了Advisor，通过 Advisor 去对于我们 AOP 过程的一个描述，我们通过它的描述生成我们一个代理类，也就是说在我们的APP，也就是我们调用方和被调用方，它们之间通过议程代理完成我们这个 AOP 原理的实现。


那么我们现在来手写 AOP 框架，对于我们来说最重要的事情是什么？我们可以看到最重要的事情就是构建这个代理类的过程，那么构建代理类的过程我们需要 device 和 point cat，从这里面我们看一下我们需要注的重点。首先我们这里面生成代理类，我们采用了 CD lab 的一个动态代理，那么构建 CD lab 动态代理它需要哪些？它首先需要 advice 通知，也就是标明一下我们如何去做这个增强。第二需要知道我们的切入点，同时还需要把我们的 talking 的目标对象来构建出来。那么现在我们开始去写我们的 AOP 框架，切换到我们项目框架，我们还是在我们 spring will 这个照轮子的这个模块里面继续写我们的AOP，这里面我们还是先从我们的 palm 门店入手，那么写 AOP 的话，我们需要依赖一些注解是什么呢？我们首先需要把我们的 aspect 接依赖带进去，那么好，我们添加上我们的依赖。


这里面注意一下，我们选择 ORGS pack 键依赖 aspect 接，它提供了一些注解，比如像 add aspect， add round， add before 等等。那么我们还需要代理，在这里面我们希望动态代理使用 c g 列，那么我们把 c 列表的大包依赖一起添加进来。


为了方便我们编程的一些工具类，我们可以添加一些工具类。这里面我们把 common text 添加进去，这里面我们选用 collection 第4个版本。好，同时我们把瓜也引入进来，瓜瓜也提供了很多比较方便使用的一些类。好，这里面我们区分一下，在这一行，我们这里面是为了 IOC 容器的一些依赖，这是我们专门针对 AOP 的一些依赖，下面我们可以理解为这是一些工具。


那么现在我们开始去创建我们 AOP 的包结构，在里面创建跟 AOP 相关的一些内容。
我们创建AUP，首先我们创建一个advice，这个 advice 它作为一个接口来标明一下我们这些类的实现，它是我们的一个 advice 的实现。那么有了 advice 实现的话，我们知道 advice 分多种，它的比如说执行之前，执行之后，或者说是环绕。那么我们现在来添加几个接口，也就是说对应的几个操作。首先我们来添加是before，对于 time 它需要继承我们的advice，因为我们现在并没有做什么实现。那么我们在，写第二个，也就是我们 off 的returning，也就是说我们执行完成之后，今天我们修改为接口好。


第三个，也就是我们的环绕通知，我们是需要一个拦截器，这是我们对通知的内容定义完成了。那么对于我们通知它的方法实现应该是什么呢？我们可以在这里面去简单细看一下。首先对于这三类通知，它的操作的参数应该都是一致的，比如说我们在这里面定义 off the returning 的话，可以在这里面写方法我们的 off the returning，它需要的参数，这里面有 return value 和 Mast 及 AR g 和我们的 talking 的对象，这是我们在执行完成之后的一个操作，那么我们在执行之前操作应该做哪些参数呢？我们这里面看一下。


对于执行之前操作的话，我们定义的内容是，首先我们要执行的 mess 的以及我们的参数以及当前的 talking 对象，这就是我们在执行之前需要注意的内容。那么这里面我们看这是一个我们的环绕同志，环绕通知我们需要使用一个类似于 method intercepts 的方式，对于环绕通知的话，我们需要注的事情也就是对于这个方法的执行，也就是invoke，那么对于 invoke 这个方法的话，它需要的参数也是 mess 的object，也就是我们的参数。


定义完 advice 接口，我们接下来定义 pend cut， pend cut 是为了说明我们在哪个类或哪个方法上进行我们的增强，所以说我们来先定义 handcat 这个接口，那么既然是对哪个类或哪个方法增强，那么我们应该写一个类似于匹配器，我们首先要匹配的话指定的类能不跟我们的朋友看到匹配上，同时我们应该也要指定一下对应的方法能不能去匹配上。


其实这样的话我们就完成我们 pet cat 的这个接口的定义，那么完成 panic 我们还要做什么事情？我们知道我们的 advice 和 point cat 它可以共同组成一个 adviser 对象，那么这个 advertiser 对象去构建我们 AOP 的一个说明，那么我们来接下来我们来创建一个 device 接口，我们创建这些接口的过程其实我们完全是参考了 spring AOP 设计的一个过程，那么如果自己在写的话，完全可以脱离 AOP 的框架去自己实现，我们在什么位置做什么争抢也是可以的。但是主要目的我们还是为了让大家对 spring 的了解更清楚一些。


那么对于 advice 它应该要提供哪些内容呢？我们在这里面首先Advisor，我们要提供我们的 Advise 类是应该是哪些，我们这里面通过 Advise 的 be a name 来去标记一下整个 Advisor 对应的best，同时我们也应该是说明一下我们的 pet card 对应的内容，在 pine card 我们怎么描述pincut？我们通过一个对应的表达式，因为我们在去标明我们这个 AOP 需要在哪，什么地方生效的时候，我们现在通常还是使用 as pet 接的一个表达式。


基于Advisor，我们一般会去构建一个 point 看打Advisor，其实这也是对应我们 spring AUP 的实现的一个逻辑，我们在这里面也是参考它的去实现。对于这个 point cut Advisor，它是继承了Advisor，同时它提供一个什么方法，它在这里面相对于Advisor，它提供一个方法，也就是说获得到我们的pandecut，也就是获得我们 pandecut 一个对象。那么这样的话，我们几个关键的接口就定义完成了。


我们现在有了 Advise Adviser 和 point cat，那么我们现在可以去构建我们的 seed live 的代理类，那么我们首先来创建一个我们的 CC lead AOP，那么这个代理内对于我们来说我们需要哪一些属性去组成？其实我们刚才也介绍了，首先它应该是由我们的目标对象，同时应该由我们 adventure 的一些组合。那么为了去获取这些 bin 是否去代理？我们应该要把 bin factor 的对象获取进来。首先在这里面定义我们的 target 对象，其实我们定义我们的 Advisor 列表，我们再把对应的 Apache 进来，好构建完这个对象处理的属性，我们去创建它的一个全类的一个构造方法。接下来对于这个 go join 它应该要做的事情是什么呢？它应该要获取一个代理对象，那么获取一个代理对象是他最正经的工作。我们先把代码框架写完，那么我们先看一下接下来实现的过程。这里面我们 CD Lib 可以生成代理类，它怎么跟我们 bin 容器的 bin 关联起来呢？我们知道我们在写 io c 容器的时候，我们写的相对比较简洁，我们只是通过我们的 class new instance 来创建这个对象，那么现在我们需要把我们原生的对象代理为我们的一个 Syllava 的代理位。


那么是现在我们需要怎么处理呢？我们可以通过我们的 be impose process 来处理，那么现在我们可以在这里面构建一个 binpose process 的实现，这里面我们可以称为AOP，那么对于这个我们知道它应该有对应的一个后处理和前处理的方法，我们先把这个类的构造方法来实现一下，对于这个类它肯定是依赖我们的 Advisor 和 being factory 难，那么所以说这两个属性应该是我们必不可少的。那么对于这两个属性，我们来先创建这个类的构造方法。


的方法创建完成，那么我们来先看一下我们整体的这些类的结构，这里面我们可以对于我们定义这些类做一个简单的一个重构，也就是对于一个包结构的重构，比如说我们的address，我们可以跟它增加一个 address 的包，这里面我们看跟 advice 相关的内容，我们这里面有advice，我们把它挪进去。这里面还有我们的 off 的 returning 和我们这里的 mess 的 intercept 和我们的 mess 的report，我们把 talent 都挪到 advice 这个包结构下面。同时我们在定义我们一个拍 hat 这样一个，包结构，那么跟 panic 的相关的内容在这里面我们首先支持 panic 的这个接口，那么这里面我们看 product advise 我们并没有判进来，因为我们这里面更倾向于给它建一个 advice 的一个包结构。现在我们把 advise 和 point advise 放到我们的 advise 这个包结构里面，这样的话看着我们的类会更整洁一些。


现在回头来我们要需要把我们的 Bing post process 跟我们的 Bing factor 去关联一下，那我们来看一下我们的 b infactory，在我们 b in factory 整个实现的过程中，我们并没有去实现 b impose process 相关的内容，所以说我们要去做关联。


首先我们需要让我们的 be in factory 支持 be impose process。好，那么首先我们来在这里面定一个 be impose process 的接口，这是一个接口，那么对于这个接口我们熟悉 spring 的同学应该是比较了解的，它接口的方法我们可以在这里面去对应。拷贝过来，我们给它提供了一个默认实现，这里面是 put pass before installation 和 up 的installation，这里面对应的一些参数。嗯，那么我们接下来要怎么做这个方法？它肯定应该要实现一下我们这个对应的接口，这样我们就可以去扩展里面相应一些相关的功能了。我们在这里面对于我们 AOP 它应该在什么阶段实现？它应该是在我们的 of the purpose， of the incentive，也就是说我们这个初始化处理完成以后，那么我们需要去覆盖我们的click，这样我们覆盖是 off 的，在这里面实现我们的功能。


那么我们在对于 AOP 去进行解析的过程中，我们就要去想，我们首先需要从 b effect 里面获取到我们那些跟 aspect 相关的一些类，只有在我们配置的表达式能覆盖到对应的类的时候，我们才需要对这个 been 来进行一个后处理的一个增强，为了更方便的描述，我们可以把这个去写一下。我们如果说是定义 AOP 的话，通常我们是这样去做的。我们先建个 u p 包，那么在这里面我们定义一个 log aspect，这样一个类，在这个类里面我们通常会加上一些注解的一些描述，在这里面我们会加上 aspect 这样一个注解。同时为了它注意我们扫描的bin，我们这里面是加上我们的 manager 的 bean 这样一个注解。基于它的话，我们通常会加上对应的描述符，比如说我们在这里面我们会使用类似于这样一个描述符描述一下我这个类它去处理的内容。好，对于它来说一个around，也就是我们的一个环绕处理的话，它是需要继承实现我们的 match 的incept。

