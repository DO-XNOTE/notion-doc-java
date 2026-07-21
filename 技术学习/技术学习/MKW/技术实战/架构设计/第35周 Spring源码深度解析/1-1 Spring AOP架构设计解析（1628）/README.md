---
title: 1-1 Spring AOP架构设计解析（1628）
---

# 1-1 Spring AOP架构设计解析（1628）

[image](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/143cc701-7b65-4b87-89a2-df4bfc67c8e5/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663OTEHJZY%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T231958Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDlW0fcnOZ7S2DAhnAi6v254TLlZSIAsEm5IBQgopCSrwIhAJoo3P%2F5tzZZviagXLXSSeVKHNXZ6Uq1Pzrsib90WSzpKogECMb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1Igz3534baYz7z%2B80mFIq3ANjfqBZN%2FN57QE0l4wCUedutDGEOAS7ImkGgKdN4V1UdRaw%2FssTLXrA%2BwkYaM9rP5D0YpvW%2B%2BwZ8sbv2636HN2UPPGX5qtabkCEQ2c182%2FQ9OgK4J9uC6stVUl9dVpfy9tI60Sm3TxCRx%2FsmO0MlNvrDu4Uns80AWz4B4hZEX7hkBFUTxsdFQJgaEIboWf3MLZVGq1cd7RWf1CFFGrCh5HKk3rUP3JKYm3kIocpbO4z7iCP8gNNcy4%2FZUzTy%2FSE2XJFDVd7M57%2ByAi%2BK3NMD7xQ%2B%2FVBkPjEdYQonapOZKVsJIpgRYtRP4MiVddyJiBvsDaRMqCh%2ByRzYnXGWOUlBkJdl8g9rB1F%2FwO%2FuQsfvZtorltZDfkUNBoXE5xcN4kRcwm1VYSKFHXgz%2B8bHsOTRt5htMhd086fRw97edBK38AhbXZkXryrvI88VwwzG9aSYbA%2BYYlTytX3YO6svu0L9pjycGYUsRwtksTNrZ%2Bgo26Pk8sJYjyy8iElpcIWUaUhvGbUGWoJYVOcDsn9F0iHZCqenE4n5hYtwm4qIUuT1J9BOxHNTgp25NigtIw5VnDGBayrcqYdJW4VvF9FSvBISo08P096DwGEK7weMGsGB81B1qr9DrntSfgaHZaHiTDPt%2F%2FSBjqkAfWl5UBpuWGeyZB2TIMxbtBDjfAwZs71uwZmG1HXJUC72dxNhqw4%2FhtwmJM0xw8yXCP7n4br4CMP%2BNR9dKfqSEgL47T8SphRzERJrDhFMnF649xzkgTBbFMVW4%2FJrYHpf1VA9eoQKHaf0wSKl4zEXa2n2hGzdzziQYPQ2N8RiUE0dm1Zy22viSE49YFer1vhQDCb%2F9VOomOo3FQAafOCR5fMSq1q&X-Amz-Signature=999d9eefb087855e5eaef0608727734dae94fd4514eff2d3b82bad759f900ed7&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

同学们大家好，这章节我们来学习 spring AOP 架构设计解析 l seed 章节，跟大家特别说明了一下 l seed 重要性，那么 AOP 的重要性如何描述？其实它仅次于 IOC 容器，对于大多数同学来说，提到 spring 特性都可以脱口而出， spring 具有 IOC 和 AOP 的特性，那么我们从 spring 的框架图里面也能看到AOP。其次也是基础的核心功能，这里面主要包括 spring AOP 模块儿以及 spring aspect 模块儿。


接下来我们去通过三个方面来介绍 AOP 架构层面的内容。首先我们要了解一下什么是AOP，第二我们要认识一下 AOP 的核心概念，在 AOP 给大家定义了几个概念，这个概念相对来说比较抽象，如果大家没有接触过相关的内容的话，可能理解起来会比较费劲。


最后跟大家介绍一下 spring OP 的实现逻辑和我们的一些代码演示。好，首先我们看什么是 AOP AUP 可以简单说就是 aspect orante 的programming，也就是面向切面编程。 AOP 它也是一种编程思想。4、面向对象编程，也就是 OOP 的一种补充。面向对象编程，将程序抽象成各个层次的对象，而面向切面编程是将程序抽象成各个切面。首先这里面我们的面向方面或面向切面编程，它都是基于 spring 的AOP，那么 spring 的 AOP 它是基于代理来实现 AOP 这样的功能，其中代理我们又可以去理解为带 Java 的动态代理和 sleep 动态代理。其次 Java 还有静态代理，但是 Java 的静态代理它并不适用于 spring 的 AOP 的功能。


对于我们的业务作用，我们可以理解 AOP 的操作可以类似于过滤器，但是它比过滤器更强大，而且应用的范围更广。因为我们在使用过滤器去做一些过滤操作的时候，我们也可以对它做一些前处理，一些后处理，它只能指定特定的场景去操作，比如说我们的 Web 对应的filter，那么它只能在拦截我们 Web 的请求，它并不能去做我们 service 或 DU 城相关的一些拦截。那么 AOP 的特性就是说，它不管你是在哪一层，只要你是一个对应的加法方法，符合我的 AOP 的条件，那么我就可以对你进行去拦截，进行一些扩展处理。


那么我们想象一下这样一种场景，我们在开发过程多模块会有一些功能的重复，比如说我们的用户模块、订单模块、支付模块，他们对于权限校验，一些事务处理，还有一些日志操作，那么对于他来说是一些重复的一些功能。那么我们通常怎么去处理这些事情呢？显然复制黏贴它不是一个好的方法。在传统的面向对象编程，我们也会将这段代码抽象成一个方法，然后在需要的地方分别调用这个方法，这样当这段代码需要修改的时候，我们只需要修改一个地方就可以。然而需求总是变化的，有一天我们新增了一个需求，需要再多出一些修改，或者说我们需要再抽象出一个新的方法，然后我们在需要的地方分别调用这个方法，又或者我们不需要这个方法了，我们还得删除掉每一处调用该方法的地方。实际上涉及到这么多地方具有相同修改问题，我们都可以通过 AOP 的来解决。 AOP 对我们最大的好处就是它可以做到对我们的签代码无侵入。那么对于 AOP 来说，它可以有几个实现的分类。要达到 AOP 的效果，保证开发者在不修改源代码的前提下，具备系统中的业务组件添加某种通用的功能。


u p 的本质是由 AOP 框架修改已有组件的多个方法的源代码， AOP 其实就是代理模式的一些典型应用。按照 AOP 框架修改源代码的机制，我们可以分为两类，首先是静态的 OOP 实现，静态 OP 实现。这里面主要是对于 AOP 植入的时机进行描述。 AOP 框架在编译阶段对程序源代码进行修改，它可以生成静态的 AOP 代理类。其实我们打包生成的对应 class 文件就已经被修改了，这个需要使用特定的编译器，比如说 aspect 接。


另一种是动态的 LP 实现，其实我们在应用场景下大多是使用动态的 LP 实现动态 AOP 实现，它可以在 AOP 框架运行阶段对动态生成代理对象。对于在内存中，我们可以使用 JDK 的动态代理或资金 Lib 的动态代理，这里面去做一些比较。相比来说我们静态 AOP 实现它会比较麻烦一些，它需要指定特定编译器，但是在运行的时候它的效率是比较高的。而动态 AOP 是在运行的时候动态的生成代列对象，所以说它对我们的性能是有一定损耗的，所以这里面我们去做一些取舍的话。其实目前来说业务上大多选择的是 spring AOP 的动态代理。接下来我们了解一下 AOP 的核心概念。首先对于 OPT 来说最重要的也就是aspect，对于 aspect 我们可以理解为它是个切面的概念，对于切面它其实就是切入点和通知组合起来，我们叫切面，这个里面可能理解起来还是比较抽象，我们可以这样想，对于横切关注点的模块化，比如上面提到的一些日志组件，我们可以认为是通知引入和切入点的组合。在 spring 中可以使用 scammer 和 aspect 接注解的方式组织实现这样一个切面。


第二我们看一下 join point，我们可以理解为此连接点，连接点就是在我们代码里面允许切入通知的位置，都可以称之为连接点。对于我们常用的，比如说方法执行前，方法执行后，或者说是抛出异常等等，这个我们都可以定义它就是一个连接点。那么对于连接点选中以后，我们就可以定义我们的通知 advice 通知，也称之为对于程序的增强，也就是说我们把原来的代码通过 AOP 的方式对我们的功能进行增强，比如说我们对原来没有权限和没有日志的模块增加了它的日志和权限模块，一方面我们可以称之为是通知的方式，另一方面我们也可以称作对我们原有代码的功能性的增强。


好，我们看下一个，也就是 point cut，也就是切入点。切入点的词相对来说比较容易理解，跟我们链接点去做比较，所有能在我们的允许切入通知的位置，我们称之为链接点。我们在链接点的基础上选择我们的切入点，也就是说我们特定了在对应的某一个方法执行前或执行后做操作，那么这个选定的方法我们就可以理解为它就是一个切入点，切入点它在spring，它支持一些 Pro 五的一些表达式和 aspect 切的一个切入点模式。 spring 默认的是用 aspect 切的一些语法，通过一些通配符的表达式去表明一下我们需要拦截的方法。


接下来我们看一下 introducted text，它可以理解为是引入的功能，它就是为类添加新的方法和属性，可以理解为它是一个动词，也就是当我们设置完我们对应的切入点，我们在执行植入的过程中为我们的类添加完新的一些功能。我们看 target object， target object 也就是我们的目标对象，被一个或多个切面所通知的对象，我们称之为 target object。可能描述比较困难，其实这个比较方便我们理解，我们在实现代理操作的时候，被代理的这个对象，我们就理解为 talk 的object。


好，接下来我们看 AOP parks AOP 的框架创建的对象用来实现切面，并且完成通知，也就是说 AOP 在对于原来的目标对象进行一层包装，进行一层代理，那么他代理完成的对象就已经支入了我们这些通知的信息，这是我们的 AOP 的代理的过程。


接下来我们看支入是将切面应用到目标类创建 AOP 代理的一个过程，那么植入它可以分为，比如我们编译器植入和类装载器植入和运行器植入。对于编译器植入它需要依赖特定的编译器，那么类装载器它是需要特定的类加载器，所以说为了避免这些麻烦， spring AOP 推荐大家是使用运行器进行植入，虽然说在运行期它可能会有一定的性能损耗，但是对我们的一些后期维护来说是相对来说是比较友好的。


接下来我们看 spring AOP 的实现原理。在这里面我们首先看到整个 spring framework 是我们最大的底色板，在 spring framework 里面它通过我们的代理和我们的 mass 和 point cut 对我们的 APP client 和我们的 talk 的鼻音做一层，拦截。在这里面我们看这是我们的目标对象，我们对目标对象构建完成以后，需要对它进行一个无侵入的功能扩展。


那么我们需要做什么事情？我们首先需要对这个 tag 的 bin 生成一个代理对象，那么这个代理对象如何生成？代理对象？首先要知道我要代理这个对象的怎么操作，比如说这个对象有多个方法，我指定要代理的哪些方法通过 pend can 的去指定，那么我代理完这个方法以后，需要对这个功能做哪些功能性的增强和通知？通过 advice 来去构建，那么通过 advice 和 point head 去表明了我们要对这个代理对象增加哪些功能？方法调用的增强，构建出我们代理对象通通过我们的 APP kind 去调用的时候，通过我们的代理对象间接的去操作我们的 target bin，就完成了我们子纯 au p 的功能的增强。


好，下面我们来看一个 AOP 的一个 aspect 的实现，通过这里面我们看到在里面对应我们定义一个log， aspect 也是非常用的业务场景，也就是说我们对我们的操作进行一个日志的记录，对于这个日志记录，首先我们通过 aspect 对它进行修饰，表明它是一个aspect，一个 au p 的一个定义。那么这里面我们还定义了 at component，标明它是一个bin，我们在扫描的过程中可以把它注册到我们的 spring 容器里面。首先这里面我们 so 需要定义我们的 point cat，这里面我们看到我们通过一个对应的表达式来标明一下我们要拦截的方法，通过 execution 我们在这里面去看到它拦截所有的我们 showcase 宾下面的这些方法，拦截这些方法完，拦截完做什么事情？这里面是around，也就是说是个包围的，我们要对它注的事情，也就是我们在执行方法之前打印一块日志，也 before 某个方法的执行，我们执行之后，也就是打压出 off 的某个方法，执行之后同时执行完成以后我们去输出一下我们这个方法调用所需要的耗时。


我们只看这个方法的实现，它相对来说是比较简单的，但是这也就是我们大多数 AOP 使用场景的一些引入。好，通过这里面大家应该能看到我们在配置完成我们这个 log aspect 之后，需要把它注入到我们容器里面，这样开启我们的AOP，那么整个这个功能模块就会生效了，我们看一下代码里面都需要做哪些思想，现在我们看这里面我们在 showcase 下面建了一个 AOP 模块。


我们还是先看一下 palm 里面的内容，在 palm 里面我们引入了 spring AOP 和 aspect 皆aware，通过这两个引入我们看即使也就把我们 AOP 的一些主要功能引入进来。在这里面我们是使用了 showcase spring IOC 里面的一些bin，我们需要重用我们的 hello Bing 和 hello context 来去演示我们这个执行的一些过程。


在这里面我们可以看到我们在这里面是定义了一个aspect，跟我们刚才 PPT 上看到的效果是一样的，这里面就不跟大家更多的去介绍，大家要记住的是我们在这里面对应的我们这个方法的名称和我们 around 进行 advice 的地址是一样的，其实我们也可以在 around 里面直接去写对应的这样的表达式，也是一样的效果。


我们构建完这个 b 音以后，我们再看这里面的 a o p 加configure，在这里面注意一下。我们首先这里面是有一个configuration，下面又 enable aspect 接 auto prox，也就是说我们去开启一下我们的动态代理，这里面我们注意一下 parks talk 的class，这里面的默认值其实是false，那么如果我们只是对于接口进行代理，它会使用 Java 的动态代理，那么这个 false 没问题。但如果说我们要对一个指定的类去进行动态代理的话，那么就会出现问题了。


所以说我们需要对于这个 box target class，我们设成 true 塞棱 true 以后我们看在这里面我们去定义一下我们的bin，这里面我们定义了一个hello，对于 hello 它的实现我们采用的是 hello context，同时我们定义了 hello bin Hallobin，它的实现是 Hallobin 实现。这里面我们再看对应，我们把 log aspect，我们这个 ao p 的一些配词也作为一个 bin 注册完，注册完它会作为容器里面一部分，在启动的过程中进行 AOP 的一些动态代理，那么我们这是我们的一些配置内容。


接下来我们对它进行一个执行的演示，我们看在这里面我们对 log entry test，这里面我们用到了 spring test 给我们提供的 spring zeunit configure，这里面我们用到的是 spring 5，它依赖到 GENIT 5 对应的一个配置方式。我们在这里面只需要引入我们的 Java configure 就可以去构造我们的容器，那么我们在启动的过程中，它通过 spring g unit 的 configure 构造出我们的容器，同时我们可以在这里面去通过自动注入，在这里面我们可以看一下我们分别去执行我们 test 的对应的 hello 和 hello 币，我们先执行我们的 say hello，我们看一下执行完成，我们看一下出处。


从这里面我们在选中 test say hello 的时候，我们可以看到这里面我们有 before say hello，我们这里面有 off say hello 同时对应的是我们的 log aspect round 方法去执行的，在 before 和 off 的之间我们执行了 hello 的 you 方法，这里面我们并没有去设置我们的 hello 对应的name，同时我们可以看到这里面还有 off 的 returning 和 off 的这样两个 AOP 的实现，这样我们可以看到对应我们再去做 u p 实现的时候，我们整个是 around 的方法，它的范围是最大的。


再看一下我们的单元测试里面，我们这里面分别依赖了hello， Bing 和 hello 这两个 bin 属性，那么对于 hello b 它是一个具体的加压类，对于 hello 它是一个接口，那么 spring AOP 在处理这些类和接口的时候，它处理的方式是不一样的。我们注入进来的这些 b 音，它都是通过 AOP 构成的代理层层的，那么对于我们这是一个普通的类，那么 AOP 它通过我们的 CD live 代理去构建成一个b。对于接口，它会使用 Java 的动态代理构成我们的b，所以说在执行过程中，大家可以打断点的方式去看一下对应 hello 和 hello 病，它真正的实现。


那么我们现在回过头来看一下，对于 Java 代理来说， a o p 的代理实现，我们默认是 java 动态代理和 c d lip 动态代理，同时我们知道还有一个 java 静态代理，它并不会作为 string AOP 代理的实现。对于 Java 动态代理和 CG Libra 动态代理，它们的优缺点大家一定要清楚。对于 Java 动态代理，它必须需要实现接口，只有接口的情况下才能使用 Java 动态代理。同时如果说针对单纯的一个具体的类是不能进行动态代理的，这是我们加大动态代理的一些局限性。那么 CD lip CD lip 的动态代理，我们可以对类进行动态代理。


其实 CD Leap 动态代理的原理只是针对你这个类，跟你构造成一个子类，将子类继承父类的方式去扩展它的功能。大家知道这里面对于 CD live 要实现子类，那么它的局限性就是这个对应的 Java 类，它不能通过 final 修饰，我们知道 final 修饰的类不能有子类，所以说通过这里面大家应该要了解 spring LP 代理的一些它的优缺点。那么关于 spring OP 架构层面，我们就先介绍到这里，同学们下一节再见。

