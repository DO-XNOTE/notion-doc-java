---
title: 6-2 Spring框架IOC容器的启动过程（0942）
---

# 6-2 Spring框架IOC容器的启动过程（0942）

[image](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/fabd4e2b-1974-40e9-9177-62d09c602424/SCR-20240804-beui.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SIOPZF47%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T232035Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIEuUQkTM3jiHXvFlpf6tLGTWkWsw8iasRuKbhwgU2XihAiBgvLoBqlpP9RRklbKxwvjbQ38%2FYp%2FLwQyK8RguQPaSPSqIBAjG%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMpTN4iTOfM%2BPnXa5kKtwDdlKVXcCG6t4NIifzWMlz0y5p3W0PoWYkVR1zkfzHafxkJkMrRcV3I7sXN0UQKIgTR%2B1wmDojzxKQyV2vPQUXcUp6X1cUPBzLH7sQULbuLbM1sTSetznFopLSj4F4kIVpa43eIeWpSM%2BAURrPyGSu%2BDHtZT0YyqGVUapMBGmCQ8CsN19M7RAA7x9r2ncor%2B65ldLFM1vEs%2FLeVISiFQQ6R4j5WPdhsdZsnjxWCeUo0juD07PqbpwGEJ7gLknXxoFZsGoJjP7IJd19nbIIhodQy%2FveiY9sEISOYfHV1PSZKTExyQRsuq5OCMJulczGa2vClpL%2FrPm092NybOThXnmuBa%2Bwp37K6qHzZwE%2F4ZpRJw07Q4AptkXPTA7wTtP4HonSxlJ%2FhzvSvFJ3auV1HoyzzMs9oQ%2BHqcHyZVP0mrylQ8SjWJbVkHkqLNgYfyNBWHhxQFo7VtbhkFfUtaF91i11Ay9ENVZhnIcI1Ku%2BhQ3hu11FTT6OYcB1xkGV0fKtHdgxTB%2BErr6u%2FINYLWdJjR5YwnKsMPbXkyUdXVD6vJa81kr3u7D2haLWTuAOn2hd8hbjj8kxoLm1Jz7OnKfRzCBsMIH07iogSg9fmX2zV9gxRe21adgu2OFg4WHIjgwwsLr%2F0gY6pgHXJNIPhFUis0FV1nf3iehRvVcw1q%2BCXAAAV7jKMKBZH2mZ6YsZw9jF3K0XultP2XzOX0oKliN7R4kkJ34abB5jeKALgkr%2F7Xnj61VfwXIKtdYaIMTmc%2BG%2B5IdF%2B05WamavirmL1lF8WNne7NyKJjpBpTwxUuw%2F3FzMvxDpBruqymAhh6hMFgEURxj%2FNnhoX%2BKivqFIE3j6DpeGLS4qPz6akmmGHobr&X-Amz-Signature=1d15045d7955af06d6895cc221ea68beb368b1dd08709b1e42ff5848a5dff906&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

同学们大家好，这一章节我们来介绍一下 spring 面丝体的深度解析 spring 框架 LC 容器的启动过程。通常我们看到这个问题的话，大多是需要我们解析一下 spring 的 LC 原理。那我们来看首先我们的 spring LC 容器它的工作特征是怎样的？通常我们写完业务逻辑以后，我们会通过我们的 spring io c 容器进行包装，也就是我们的一个 application context 实例去进行业务逻辑的包装。对于这业务逻辑包装过程中它通常会依赖一些元数据的配置，通常我们可以是XML，也可以是加 config 的文件。
那么 spring s 人去通过我们元数据配置以及我们业务逻辑代码的实现的这些特征去构建出一个完整的 Java 应用，程序，那么这就是我们 spring LC 容器它执行的一个过程，那么在执行过程中，我们进行 spring LC 容器启动过程的介绍，那也是相对比较简单的，因为我们都已经学过了这些内容。


首先我们来看一下核心容器，也就是我们的 bin 容器处理的过程，那么构建变容器的话，也就是我们默认的 de 飘的 listable infactory，那么我们知道在构建这个实际的变容器的过程中，我们需要首先去构建我们这个 default list being factory，那么构建完成以后我们还依赖一个对于 x mal 的话，我们是 x mal being depending reader，也就是说我们一个 bin defin 文件的一个读写器，那么对于它读的内容也就是一个资源文件。这个资源文件是通过 claspat resource 包装的一个 hello bin XL，也就是我们的配置文件会通过 Passport reset 包装，一起通过 XML being defined reader 读取进来，它读取读成完成以后，会通过 load being defined 的方法把我们整个 external 配置的内容加载到我们的 be infactory 里面。


其实加载的过程是比较复杂的，在里面加载过程中对于 XML 的话，最重要的也就是对于 XML 的解析，那么解析的过程中我们会碰到不同的 string 定义的一些namespace，比如像 MC 开头的或 AOP 作为开头的等等，它都会通过 name space handler 的方式去找到对应的解析器去解析，解析完成以后把我们这些解析的 bin 来读，我们注册到我们的 bin impact 里面。这里面我们可以看到是通过 register being defending 的方式注册到我们的 be in 容器里面，那么对于这个病体分类注册到容器里面。


接下来要注的事情，当我们注意一下，这会我们的 bin 并没有创建，只是把我们的 bin 的定义文件创建完成了，以及它的依赖关系也构建完成了。现在我们要注的是当我们要使用这个 bin 的时候，我们通过 get bin 这个方法，通过 get bin 去调用，调用的过程会首先判断一下这个 bin 是否存在，如果 bin 已经存在了，那么获取到缓存里面的bin，如果 bin 是第一次调用，那么它当然是不存在的。过程中它会通过 create bin 的 pass 去把整个 bin 构建过程。


在这里面创建 bin 的过程中其实是比较复杂的，它需要把这些 bin 之间的依赖注入的关系，以及一些前处理后处理的执行逻辑都执行生成。包括对于像 init mess 的和我们的 destroy method，这个一些构建的逻辑都需要构建完成。


执行完这一步的话，就是我们这个 Bing 实例已经构建完成了，我们可以通过去获取到这个 bin 进行 bin 的一些业务操作。这仅这样的话，我们整个 bin 容器的启动过程就完成了，这是我们最底层核心的这个 be infactor 的构建完成。


那么对于我们在业务开发通常用的 application context，我们是这样一个逻辑，这也跟大家介绍过了，我们再回顾一下，因为我们通常我们现代座驾开发主要是基于notification，也就是注解的一个 configure applicant context 去构建我们的 bin 容器对象。对于它的处理过程，我们通常会需要通过默认构造方法构建出这个 Pixel 跟它的对象。


那么呢，接下来我们需要去注册一下我们的扫描bin，注册扫描 bin 分两种情况，一种是注册一个加 configure 类或者一个，另一个是指定一个 base packets，就是我们包名，那么发这个注册完成以后它就会进行那个 being definitely 的解析，完成以后通过我们刷新这个 refresh 方法的时候把整个 being 的初始化完成。这里面要注意一下就是我们通过刷新 refresh 方法。其次里面有一点就是相当于我们在 b factor 里面通过 get being 的方式去创建这个 bin 的过程。好到这步刷新完我们的方法以后，对于及注解的 applicon contact 它就已经初始化完成了。后面就是我们业务逻辑处理的一些部分，那我们来看一下更细节的一些方法。


首先在进行默认构造方法生成的过程中，它要做哪些事情？它会构建一个 notation being 的 depending reader，我们想跟我们刚才在处理 being factory 的过程中，它里面用的是 XL 的 bin definition，我们这里面是基于注解的 bin definition，它多次为了对我们这些注解进行一些我们的 bin 定义文件进行解析，这是我们刚来自ML，现在我们是注解。那么在解析的过程中，它会把一些类似于 being post process 注册进来。这里面我们会看到这里面比较重要的几个，像configuration， class process 以及我们这里面的Autoware， annotation 以及 common 等等这些一些 be impose process，那么这是我们的 defending reader。


接下来还有一个叫 class Paas being depending scanner，这个比较容易理解，一个是我们的定义的一个读写器，这里面是一个扫描器，也就是这个扫描器，它是基于一个包结构的扫描器，通常它会通过一个 notation type filter 来去构建这些关系。这里面主要是扫描三种类型的注解，一个是 spring 原生的注解，像这里面 add component 以及 JSR 250 的 managed bean 以及 JSR 320 的 name 的这几种类型的注解。


好，这是我们构造方法执行的逻辑，那么接下来我们来看一下它扫描的逻辑，也跟我们刚才是对应的，一个是注册我们的 Java 卡片，另一个是我们扫描包的结构，这里面处理的逻辑其实我们就不再去细讲了，这个大家可以翻过来前面介绍的这些内容去详细的去理解。


好，接下来就应该是我们执行 refresh 方法，那么对于 application context，它 refer 方法处理的工作是比较多的，这里面的我们在这里面还是粗略的回顾一下，大家可以回到对应的章节去讲讲它里面详细的一些内容。这里面主要是我们要介绍的是我们要把我们构建底票的list， being factory 的过程说出来，这样能体会出我们的 application contact 以及我们 bin factory 它们之间的构建关系。同时这里面是预处理我们的 bin factory 要注意哪些事儿，这里面我们看到它会需要把我们的 Bing poster process 注册进来，同时还跟一些我们 bin 里面注册的一些单例，这里面像环境变量以及我们系统的一些属性文件，我们系统的一些环境信息等等等，这些完成以后它就这是我们真正的一些比较重要的逻辑，那么下面会有一些其他的比如 case 里面的内容就是我们对应的。


如果说初始化失败的情况怎么办？失败完成以后我们还需要进行一个 control 的一个取消操作，以及对于我们的一些 common case，一些reset。那么真正成功的逻辑是在 try 里面的内容，那么我们看一下 try 里面的内容是什么？在 try 里面要执行的过程我们首先是 post process being factory，也就是说我们在对于 being factory 构建的一些默认的一些逻辑，不过这里面我们可以看到源码里面它是一个嗯空的代码块儿，可以通过它这些子类的继承来实现。


接下来去进行的是 invoke be infactor post process，这里面就是说到对于我们的 being post process 和我们的 fact being factory post process，它里面处理的一个时间节点是这样，在这个步骤，接下来它处理完这个 be effective positive process，它需要去注册我们的 bean post process，把 bean post provide 注册完成以后会进行一些像 message source，一些初始化，以及我们的四件广播器的初始化。这期完成以后，那做出一个 unrefresh 一个通知，这里面也是一个默认的一个底票的，一个空的一个代码块。


接下来去注册我们的监听器，在这里面有一个最重要的一点，就是说 Phoenix being faced in place，这是什么意思？就是说当我们前面这些内容处理完成以后，我们需要做的一件事情是把我们的闭隐的实例化，那么因为我们在前面它注册完成以后，是把我们的闭隐定义文件完成了，那么闭音定义文件完成以后，我们需要手动的在 be effect 中需要手动离开了bin，那么在 article context 里面，它在初始化的 refresh 的逻辑里面，通过循环遍历 be infect 里面的 bin 定义文件，通过 get bin 的方式去通过 create bin 把我们的整个容器构建出来。这也就是说当我们的 refresh 方法执行完成以后，我们 Bing 容器里面的实例都是可用的状态了。


当这些实例构建完成以后，接下来就是我们的 Phoenix Refresh，也就是说等我们整个 Refresh 的最后一步，我们可以看到它最后做的也是对于我们的缓存的一些清理，一些资源清理，以及我们对于生命周期处理的步骤。最后会广播出一个事件，也就是我们 context fresh 的event，也就是说我们这个刷新完成了。那么介绍完这些的话，对于我们 spring 这个容器的一些启动流程，基本上能可以描述的比较清楚了，对于这样的面试官对于我们这样的介绍也能达到他的一些预期。好，那么这一节我们就先介绍到这里，同学们，我们下一节再见。

