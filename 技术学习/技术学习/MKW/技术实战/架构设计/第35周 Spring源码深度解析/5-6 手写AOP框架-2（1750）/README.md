---
title: 5-6 手写AOP框架-2（1750）
---

# 5-6 手写AOP框架-2（1750）

[image](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/c520dc47-26ea-4d27-829b-02b3e4e40b06/SCR-20240803-tgiu.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666WDW47G4%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T232033Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDSTBag7eR0niVYMMV2qPMy7KCRgdnEZIQKAUa%2BjJVxGAIgPlYGt%2BsDkbmN3BZ6f64iGMC025bIBIZUFnB5neCQapoqiAQIxv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDNJGnnPrS%2BbzVToe%2FircA5XUajiJb9o6VhUVIsMRqH2aKqVoBNIO2E7kb9A%2FCZwIRGNEz9Dj2mIM0i7mFhmD06Sh14kJoxnKVrBSoH1zEefCi1AGvuTCt4Qbd%2Bd4MVTAVpxaEBRm3%2FBhnOAb4wAUCw8bIwu4v08nL5NslTwR5tTMd6HLe6cjkPaxD8o4Aiai42eNsibDOTkcmrjnijxEQybdDTFTBIbg68xdnoUTbEFFVhS3Dn9G9bC4E8iYCKJIUDY1JIOAbbGWIj9t4x4mg5WwrP08JaZYbG0N4oikixjtue38FS%2BRdb1zxSgtaQ3m2CSioc1hACwdGBrb2nq4sdBo0TEkTdkRllYIu2SSKOBAWxxbhm5TMUQ9APAenrnZFNkW0z3xn3y%2BKdd6NiKVNt%2BcOCahA04iVim8kNtVfp%2Brgs7t39%2FbYuxJ%2FLw4av4KCPA9AOQz%2BimM2RQcblOvhzaYd58bTY8O23pmQUNnbLMNCfkI8Pn27ZZZcotQX1xCgr%2B8oIR6k9gubsuHxqPOTIY%2BB1LdTKwQFJeOwvfRkFd5TGKTtf3ky%2BXAZLEJ86Tq2R31bfchBBKehPvtQ0eRbdkjuDRxhhZbfoTVXGwDWx11%2BvSFFfESUXrsWHjdjCOt5ARjpJeflQJQgjIuMNy3%2F9IGOqUBXsM%2B01afhbiwRJaR6FcpnzfX3F35gAhrqUjjtif%2BPz3FV1N6h2WxIrchPqfsFIiaPUq%2F0YN8gwyZBBdjj83wlv1fjqhE%2FJLQly5ZE6v3VaJxJA9c5ISCJCrjPyAWfp3ykCELxnXlYCC%2BDnUVXT%2B56%2BdeoC0kH%2FZIqyJMzY%2F449wXqKJ6aUwfnkg%2B4GKNy3hWZJV7Nwk3q7q1QMb58CcPYKWWVfSl&X-Amz-Signature=2e77fc2c8d8cff892f8052e35bdc48a86ca3a570bdc6242a2ced167d9a5e942e&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

这样我们把我们这个描述符，把它放到这个方法上面，现在大家应该更容易理解，我们可以看解释一下这个方法。对于这里面，我们对于 log aspect，我们需要对于这个方法添加一些日志，那么添加的日志内容我们在哪些方法添加内容？我们是在对应的我们这个照轮子 demo 下面的这些类里面，也就是说我们在当前这个模块儿下面所有的这些，像有 create Demo model 这样一个方法，我们可以看到对于这里面我们的 DU 城有这个 create a demo model，我们的 manager 和思维层也有这个 create demo model，那么我们要做的事情，也就是说对于每一不同层次的这里面 create a demo model 去做这个拦截，那么拦截完我们做什么事情？也就是我们为了说明我们这个功能的问题，我们在这里面去简单实现一下我们的处理代码，给大家看一下我们的日志，这里面加上 SL 附件我们的业务逻辑，也就是说当它进行环绕处理的时候，它在执行之前，这是我们 mass 的invoke，就是真正执行我们的方法。


执行之前打印日志 around the before，把我们的方法名称打印出来，执行之后 around off 的也就是我们常规的一些流程，最终我们打印出执行的耗时，这是我们定义的 loss aspect。


所以说我们接下来要做的一个工作就是我们需要去解析 aspect 的，结合 at around 这样一个注解，那么在这里面我们怎么去解析？这里我们可以先定义一个类，我们在 AOP 里面定义一个我们一个 aspect 的注解的一个解析类，那么对于这个类的解析类我们应该怎么实现？对于它的解析我们首先是需要去扫描对应的一些内容，在这里面我把我的实现方式先给大家，可以直接先粘贴过来，把代码跟大家一起介绍一下，看一下，在这里面我们看，首先我们是把 being factory 和 AOP be impose process 才能进行关联起来，我们要做的事情就是进行解析。我们看这解析的过程，我们是需要把 b impact 获取到所有注释的类，那么这个类我们是方法是新加的，我们同时在 b impact 里完成这个构建，我们 reject class 是怎么获取？我们应该明白，我们首先去获取到我们 class map，我们去获取一下我们的，这样得到的内容就是我们所有的 register class，这样完成它的解析的过程。


首先去把我们整个容器里面所有加载的这些bin，我们在 string 容器里面可以理为 bin 定义文件，这里面我们就是 class class 里面我们所有区域进行遍历，我们查找它是否有 aspect 的这个注解进行修饰，如果有这个注解修饰的话，那么我们去解析这个类，比如说我找到了这个aspect，这个在这里面就对应我们的 log aspect。找到这个类以后我们要注的事件是什么呢？我们来去看你们方法里面有没有类似于around， before 或 off 的这样的一些注解，如果有这样的注解的话，我们去进行我们的 aspect 的处理。在 aspect 的处理的过程中，我们首先去获取到所有的方法，在方法里面去找是否有相关的一些 AOP 的注解，这里面我们重点去找的是around，对于before， off 的相同的道理，我们可以自己去实现在这里面实现。


如果说找到这个 notation 的话，我们可以把我们当前找到的这个注解构建一个 aspect 接 point Advisor 来实现，来完成我们的工作。那么现在我们还没有这个 apply 接 point adversion，那么我们把这个类实现一下，这个类的实现，对应的我们可以看到它是Advisor，我们应该在我们 Advisor 里面去创建我们这个类。对于 adversion 这个类，我们很明显它应该要实现porn，pointed，开了advisor，那我们把这个类的实现快速的去跟大家贴过来。对于这个类它同时需要依赖的 aspect 接point，那么我们把这个类也实现了。对于 aspect 接point，它的实现是在 point cat 里面来这里面创建几个类，现在我们已经把这个列创建完整，那么我们把其他的一些变异的问题，我们来先快速地解决一下，接下来我们来实现一下 LP 的 b impose process，那么这里面重点也就是我们的一个后处理的方法，那么在这个后处理的方法里面，在处理的过程我们肯定是需要把我们这个 aspect 加个注解解析技能把它给注释进来。在这里面我们是在它后处理的过程中去做一个判断校验，如果说当前没有初始化的话，我们把它进行初始化一下， my 痛死了，我们，在这里面我们需要传入参数，这个参数就是我们的 be impact 里，以及我们指定的当前这个对象，我们就传 this Stitch。


好下面的内容怎么去写下面的内容，我们应该要注意的事情就是需要通过我们当前的这些内容获取到我们的这些Advisor，在得到 Advisor 以后，我们去判断一下当前是否为null，如果是否为空，如果说为空的话，我们就直接把 bin 返回，如果不为空就是 AUP 的拦截，不为空的话我们需要创建我们的 AP 代理。


那么首先我们来看一下 get match Advisor 这个方法，对于这个方法的获取，我们可以看一下它的一些实现逻辑，在这里面我们这样我们可以看到它在实现的过程中是这样，它会把整个我们的 being 的 class 去获取出来，把整个找到整个类里面输入的 Mast 在 mess 里面就去判断一下它是否我们对应的朋友开的 mess bin，就进行一个匹配，这个匹配完成以后我们就可以去进行一个处理。


我们可以看这里面 get all master class，它的实现也是比较简单，也就是对我们的这个类里面的这个声明的方法，也就是获取出来这里面是否 is point cut， might be in？它实现的逻辑是怎样的？它实现的逻辑就是使用的 appeal in the cut 的实现完成。


准备看下，这个类里面它传入的参数是 panic Advisor 跟对应的being， classy 以及 mess 的方法，在这里面它是调用了 point 里面的，在这里面是 math class 以及 math match 这两个方法，如果说它只有带 math 的方子才会返回true。


接下来我们是看如何去创建这个代理类，创建代理类的过程，也就是我们涉及到了我们 CD 类的 u p 的一些操作，那么我们其实创建代理的内的工作我们可以实现的比较简洁一些。在这里面我们创建的过程也就是直接是你有一个 CWAUP progress，在这里面我们去 get 代理类就已经完成了我们这个后处理的操作。当我们通过 bin post process 来把我们的 CD live 的代理类构建完成以后，我们需要跟我们的 bin factory 构建 bin 的过程去做一个替换，那么做替换的逻辑我们是应该在对应该的 bin 的方式去做。我们看到我们在实现 LC 容器的时候，我们是通过反式的方式直接去 Nil 我们的instance，同时进行我们的依赖注入。那么在这里面我们需要注意的事情是对我们这个对应的 bin 的 object bin 进行一个包装，也就是说把我们的 bin 包装成我们的代理类，那么包装的逻辑应该怎么去处理呢？我们在这里面应该通过我们的 being post process 的逻辑来实现。我们看一下在这里面我们并没有 be impose process 的逻辑，所以说我们需要在这里面去添加一下。


首先我们来将加上我们的 being post process，大家知道在词中容易实现的过程中，它为了更好的扩展性能，这些 be input price 它都是用历史的方式进行一个循环的一遍历。我们这里面为了更简洁一些，我们只是使用一个指定的一个接口，那么我们就不再使用 list 方式。那么在这里面我们去看一下处理的过程，我们需要去做一些判断，如果说这个不等于no，那么我们需要对它进行一个后处理。


我们是 off 的insolation，把我们当前的这个 b n 对象传入进去，同时还要 b n name，这个执行完成以后，我们得到一个变量，这个变量我们的闭音对象，这个对象也就是我们获得到的代理对象。这里面我们也命名object，这样就会对它进行一个替换，这样我们可以看到那么我们这个 being post process 在什么阶段进行初始化比较好？其实我们看到在这里面我们可以让它再去构造方法的时间处理化也是可以的，这个我们可以通过构造方法的方式让它进行初始化，同时把 b impact this 作为对象传入进去。那么这样的话我们代理类与我们的 b 构造关系已经完成。那么接下来我们把我们这个代理类详细的内容来设计完成一下。


我们可以看到在这里面我们的获取代理的内容为空，那么我们现在去完成这些获取代理类的一些操作，在这里面我们去获取代理类，我们委托一个 get press 方式已完成。那么好我们这里面去一步一步来实现我们的过程。在这里面我们是获取代理类，通过概率类指定我们的 classloader 来创建我们的对象。在这里面我们用了enhancer，也就是 seed Lib Tony 构建代理的操作。


在这里面我们是使用了一个 AOP master intercept，我们是使用内部类的方式把它实现了，我们这里面把它对应的是完成，这样我们是通过构建这个 callback 使用的是 OP message，在这里面它有一个特殊的逻辑，就是说我们可以看到在这里面是 intercept 调用invoke。


在 emock 执行的过程中，我们会去看当前指定的方法它有没有advice，如果说 advice 为 null 或者是它 size 为0，那么我们就不使用代理，直接使用 match 的 invoke 就直接执行了。如果当前指定有代理的话，我们需要使用 AOPT advanced chain in emocase，也就是说一个 AOP 的一个执行链去执行，那么我们在这里面把这个类也实现完成。


这个类我们来简单看一下，对于这个 AOPT Vice， chain emocation，这里面，首先它会把当前它的 emock 方法这个 mess 有获取到，后面会进行一个签到的一个调用。这里面指定的这些属性，也就是我们代理类，我们的目标类，以及我们指定的方法和一些参数列表，以及我们的Advisor。


这里面为需要大家注意的话，我们可以看到在这里面它构建了一个人脸记录，顺引号为 i 等于0， i 等于0，它要做什么操作？如果说 i 去小于 device size，也就是说我们当前这个device，也就是说我们进行增强的列表是一个相当于是个嵌套的关系，那么它在每次获取的 at best 的过程对 i 进行加价，如果 i 当它小于 the website 的话，会进行一些处理，如果说它等于的话，那么也就是不小于的情况下它会进行一些 mess invoke。


也就是说整个这些 advise 的列执行完成以后，它会进行真正的我们方法的一些 invoke 执行，那么在这里面执行的过程，我们在这边简单去做了一些注释，我们对 advice 进行判断，如果说它是一个 before advice，那么它进行在方法执行的时候，也就是说调用 before 相关的一些操作，这里面有它是一个环绕正向。


如果对于环绕执行的话，这里面会进行 match intercepts 的操作，那么这里面切记的话，我们在这里面执行的过程中， invoke 的过程中，这里面选中的 invoke mass 是当前 AUP 的 mass chain 的 invoke 对象，同时它的参数设为 null talk 的对象就是 this 这样一个智能过程。下面是 of the returning advice 的一个操作逻辑，我们现在完成 CD lab AOPT 的代理和 AOP Advisor ten emocation 这两个类的话，我们 AOP 的这个流程应该是可以跑通了。


现在我们通过单元特色来验证一下，那么我们来基于 Syllava 这里去构建一个我们的单元词，我们看这里面，我们这些单词的逻辑，我们打开简单看一下，也是构建我们的 application context，获取到我们的 demo deal，然后我们对 demo deal 进行我们的 create demo deal 的操作，我们知道执行这个方法的时候会经过我们 AOP 的一个环绕的一个通知。那我们现在执行一下，看一下效果。


很显然我们看这里面，我们执行完以后，我们得到了 4 个b，同时我们可以看到这里面执行了 around before 和 around off 的操作。通过这样的话可以说明我们整个 au p 的实现已经正常完成了。那么我们现在把我们整个代码来回顾一下，帮助大家更好地理解。


首先在这里面是一个advice， advise 里面我们定义的是我们的前处理，后处理和环绕处理，同时这里面是我们判断看的。在 point color 里面，我们定义了我们一个对应的表达式，通过对表达式的解析，我们得到了一个 point can 的expression，它可以去处理我们 Matt class 和 math match 的相关的一些方法。


接下来我们来看一下这里面就是我们的 seed Lib 代理类，通过 seed Lib 代理类，我们去构造我们的代理对象，也就是这里面我们是基于类的代理构造完代理对象，在构造代理对象的过程中，我们首先需要通过我们的 aspect notify，也就是说我们通过这个类去解析出我们所有的使用了我们的 aspect 的结局修辞的类。也就是说我们这里面对应的这样一个 loss back 的接，也就是说我们通过了 aspect 接注解和我们的round，这些注解修饰的类会通过我们这个注解的解析器或解析到整个这个过程执行完成以后，我们需要跟我们的 being factor 进行一个绑定操作，那么绑定操作我们是基于 being pose process 作为我们的中介去做这个操作。也就是说当我们 bin 对象进行初始化完成以后，我们进行一个初始化完成的一个后处理。后处理的过程把我们的原生对象替换了 CG Lib 的一个代理对象，这是我们整个手写 a o p 框架里面涉及到的这些类。好，我们回到PPT，那么我们手写 a o p 的一些内容我们就先介绍到这里，同学们，我们下一节再见。

