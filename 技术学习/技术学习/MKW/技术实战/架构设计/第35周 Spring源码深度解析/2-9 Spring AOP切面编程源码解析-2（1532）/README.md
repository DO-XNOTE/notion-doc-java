---
title: 2-9 Spring AOP切面编程源码解析-2（1532）
---

# 2-9 Spring AOP切面编程源码解析-2（1532）

[image](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/46d7abe5-dd8c-4e57-899b-00b02212fcf7/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466R2LQFDTQ%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T232011Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIAC3fQVb2oQV6c1szcyQUnJ%2BgKWuIXcCuFZ0MHUnoQkyAiEAiLBueC1bb0tOUCL2CQYObQwNevZqEPzUQ5iRV4X8WKMqiAQIxv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDCUkcoNMmRLDjt39ySrcA5XlP%2Besnhc1xRs4CGHbYUJzOmYfEzOkbuwOq0oUzmUhgYrjR0FyQOvOP9y%2BiKd7b5QXaMqh4PXThmnRRkRjEPBvuTykwYsSh2TR6nUgozhMTH%2FlWzoGuFihL%2FTBupEnFQpxOybHLdKrKlHwuJ2y2APPdjIwMyQSDBklGyA3WzXsSYSvq%2B8yJUfF8bzK3tVppeGGLeXYtcLh%2BOUxnN55rXvvFCA6%2BzezEPE%2FkHVxw4bJiqDjCWEpGHjd2QWutCvnNnca9Gg%2FQEH1yv4fAvGqwQC5hLf9VsdmvkHFs27Qa5L4p72OP5WyS4gcYhGVYCL8o6tDT6chRfFCHuQYV0OgWkeVblFHSGcrvrW2p%2B2%2B%2Fkd%2FVL0S1k5gcy6Wz0UkNpvbP3guvM8U5TxiSadD5ol6gdpZwcY32OvZ887tuWkOH7hVdMe0dDxRKCenj6bPlbTTmQsYIrhDyfIfJVUBZ5gYf5Z7vQ4judchL8SmQsMlaOyYC51qP44UWS9Y1%2By5Qao2084bLFxDtf%2FCQbvgDLDP6kWlHXqCA7ts47RLwulj%2FLyGzC%2FpNDosEGrl6XOyEFaK4l7NxA%2FfHjTBlbnSQa2CJIe1khwpyfO7OiUAiLiqw5cLQciYoorieoGU2cbEMOC3%2F9IGOqUBe4IefNWM1tm9g3jPqiRjT26DxMt3dxAsUY%2FxXuQYQhFBz2uDbZ3K5%2BuGsQ5QXCKljyQogeL%2FSSZirWFoN9%2Bx%2BcS%2BHgeHlsweFZgWKT7wYbjbUIdsfxAL4YoJHysV5RZ%2FhT1tlfcEoZ4jlgSO7C0aAm0YJSByOZtJsSPGFlAA0VT5Q1MeZ%2BkmuAzC40L%2B%2FY%2FXcOVrdtbFZJNxOYXj3JJxNk4IQFDN&X-Amz-Signature=502d8c2c4929909c4c9d930af123b7a76755ca1308c6d3932fc867dd10d5dc1e&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

好，接下来我们看一下基于 Xmail 的声明式AOP。对于 x mail，我们知道stream，它构建了一些 XML 的命名空间，在这里面它会通过比如说这里面是 spin LP，XSD，或者说使命用 beans XRD 进行一个 scammer 的定义，我们通过 scammer 的定义去简化我们去配置 x 庙的方式。同时对于命名空间，它还会有一个命名空间处理器，这里面就 AOP namespace handler。我们再看一下对于这些 AOP configure 的这种配置方式，我们会有对应的配置解析器，比如说像 AOP configure，它会使用 configure 并 diagination pause，它去解析下面制定的内容。


我们来看一下具体的一个配置，在这里面我们是如果说使用 XML 来定义 a o p 的话，我们一般会引入这样一个配置，我们在这里面会指定一下我们的 name speed 空间是 schema AOP，同时指定一下 AOP 对应的XSD，也就是它的 schema 空间。我们可以看到这里面是使用了 beans 和 AOP 的命名空间，所以说这里面对应的引入了 spin beans XID 和 spring AOP 的XID。在这里面我们可以看到跟 AOP 相关的配置。这里面是首先有一个 AOPT 接 Autopress Procast tocket class 为true，也就是说我们指定默认，我们使用 CD Lib 作为我们的默认代理。同时我们看一下这里面的 AOP configure 的配置，首先在 configure 配置的过程中，我们指定里面是有 as packed 这样一个标签，它的标签下面是有一个 point cut 和 around point cut 我们知道它是一个切入点， around 它是通知的一种方式，也就是环绕通知。在 point account 里面定义了一个表达式，这个表达式指定我们会整个扫描对应的sowcase，变下面所有的方法去执行我们的动态代理，也就是执行我们 OP 的拦截。


同时这个 around around 这里面指定义 mass 的，也就是指定的方法它对应的拦截方法，我们可以看到这里面是around，对应这里面是 around advice，也就是说我们拦截的环绕通知是通过 around advice 对应的这里面的 around advice 这个方法去执行对应的 run 的方法，也就是说所有的我们这里面showcase， being 对应的这些方法，它都会被 around the bus 这里面的 around 这个方法进行拦截。希望大家能理解这个过程。


我们接下来看一下对于 x 秒的声明 c o p，我们可以抽象总结为这样，对于 AOP 的命名空间，它一般支持这样几个命名元数，一个是 APEC 接 autopacks 和 AOP 的configure，这里面是有一些区别的，比如说像 aspect 接 autoplex 和configure，我们可以理为是这个命名空间的根源数。像下面的 aspect 和 point cut 这些东西，我们可以理解为对于这个 AOP 命名空间下面的一些子元数。通过我们看到这里面的，首先用 configure 下面可以支持aspect， point cut， Advisor 这样的一些配置。在 aspect 这个标签下面还支持 point cut 和 around 质地类的一些配置。


我们接下来看基于 XML 声明 4 a O P T 的一个执行流程，它执行解析流程是这样，对于普通的 x mail 的配置文件，它都会执行到 x mail being definition reader，也就是说所有 spring 的 external 配置，它都会基于 external being depending reader 去读取加载对应它的 load being demation 的话，它会解析像 AOP pinercut around 这样的操作。当我们解析 XML 的时候，需要做一些校验，也就是说对它的命名空间去做一些校验。我们会通过这个 namespace 的 u i 去判断一下它应该取怎么样一个 name space handler 去解析。


我们在解析这个配置文件的时候，我们会发现它有对应的 schema u p 这样一个URI，所以说它会通过命名空间解析器处理器去解析这个命名空间处理器解析的过程是怎样的，也就是这个 debug 的 NAMESPACE handle 的slower，他要解析一下当前这个 AOP 这样一个命运空间所对应的 name space handler 是什么？其实它是在对应的 Meta info 下面有一个 spring 点 handlers 这样一个配置文件，跟我们那个 Sprint factories 的配置文件很类似，它也是一个 KB 的结构，在这个配置文件里面你就会指定一下对应这个 schema AOP 中的k，它对应的 value 是什么？这里面我们可以看到它对应的值是 AOP 的 name space handler。待会我们可以从代码层面去跟大家去再演示一遍，最终能得到一个这样的 AOP name space handler 方法。


对于这个 AOP name space handler 方法，它在执行启动的过程中，它会把一些解析器注册进来。这里面对于我们可以常见的像 configure 操作，我们这里面 AOP 的 configure 操作，它会使用 configure being definite propose。还有是 AOP 的 aspect 接process，它会使用 aspect auto price being depending process。


接下来我们看一下这个 AOP namespace handler 它的实现的功能，在这里面我们可以看到这个 AOP namespace handler，它继承了name， space handler，Sporter，它主要注的事情。首先这里面我们能看到它只有一个 init 方法，它应该是覆盖了这个默认的 init 方法，它注的事情就是 resist being diagnesed pros，也就是说它这里面主要是注册了一个 bin 里边的一个解析器，这个解析器通过对应 AOP 命名空间的参数据命名，比如这里面有configure，对于 configure 这样一个标签儿，它会通过 configure being dignition press 作为它指定的一个解析器。对于 aspect 接autopractice，它指定为 a Pad 接 auto progress being depending pass 作为它的解析器。那么至于这里面解析器的意义是什么呢？就是说它在启动的时候指定一下对应标签的解析器，在真正执行 pros 执行解析的过程中，它碰到 configure 这个标签，就会使用这样一个解析去操作。那么对于我们以 configure being depending pause 为例，来我们看一下它出了哪些事情。


在这里面，像 computer being depending 的PROS，它作为整个解析器处理的入口是 PROS 方法，它对应需要注的是首先自解析 Pod cut 和解析 Advisor 和我们的 pros aspect，它解析这几方面的内容。


我们看一下对于这个方法它的具体词性的过程，也就是对应 press 插入它这里面我们可以看到它是通过 DOM UTOS 去获得当前那个节点的一个 tell 的element，通过这些 element 去判断一下它的命名标签，如果说，比如说它的命名标签是 pine cut，它会通过 pass pincut pass 去解析，同时传入的对象是 element 和我们的 pause context 作为一个解析的一个上下文对象，其他的也是一样的。


advertisher 通过它的传入的参数和一些 POS 看的是一致的，是 POS adversion 和 POS aspect 都是通过这种方式去执行的。但是在注意一点，就是说基于 AOP 的解析的过程中，它首先会需要配置一下我们的 configure auto price Creator，这个操作就是说指定一下我们当前的 string 容器里面的一些 Bing post process，也就是说当满足某些条件的时候，在 get being 的过程中，我们要获取的是代理的bin，而不是原生的 bin 了。


看一下这个具体的 be impose process 它是怎么实现的。这里面是aspect，即 aware advisor or to practice creator，其实它就是一个 being post process。它这里面有两个方法是需要我们注意的，一个是实例化前处理，一个是初次化后处理。我们知道对于一个 bin 奶或者它会先实例化，那么实例化之前我们看一下。如果说实例化之前如果有 customer 定义的一个对象，那么我们需要在 before instance，也就是在私立化之前我们对它进行包装。如果它正常初始化的过程中，是需要在我们初始化去后处理 pull the process off 的 insula season，也就是说它初始化完成以后，我们判断如果它符合条件的话，我们对它进行一个包装。


我们先看一下这个初始化后处理的操作。 to swap 后处理的逻辑，也就是说当我们在执行的过程中，我们先判断一下是否符合对应的条件，这样的话我们对它进行一个包装，那么包装的过程中其实就是通过我们创建一个代理类去进行一个包装的处理。那么接下来我们看一下这个，这是我们的 post process before instance，也就是说在实例化之前的炒作。如果说我们在 spring 容器默认初始化之前，我们自己定义了一个 talk 的salt，也就是我们自定义了一种方式去初始化这个鼻音，那么这种情况下我们需要去判断特定的情况下，看它有没有进行 AOP 的代理。如果说进行 LP 代理的拦截了，那么我们在这里面需要创建我们的代理类 create price 去创建我们对的过程。通过这种方式我们知道我们前面它是首先是定义 u p，定义在什么情况加 AOP 生效，那么通过 b impose process 去创建，让我们这个 b 构建出它的 AOP 代理类，让代理类去完成这些我们通知的一些增强和扩展。


接下来我们通过代码示例来看一下基于 x Narrow 的方式如何去构建。注解，首先我们来看一下这个 AOP 的 x Narrow 的配置，通过这里面我们可以看到它对应的 AOP 的scammer，以 AOP 相关的这个命名空间下面的这些元素属性的时候，它是基于 scammer 去配置的，我们可以到里面去看一下，我们点开 spring u p 这个scammer，我们从这里面可以看到。


首先我们看它在支持的 element 是支持configure，对于 configure 下面的元素，它支持像 point cut 和 Adversion 这样一些类型，比如说还有 aspect 接等等，其实还可以支持向Procast， target class 和 expose progress。


还有一个根节点，也就是 aspect 接 auto configure 其实可以通过我们的 AOP 里面就可以看到。对于 AOP 这个命名空间的话，我们可以在第一节点就是 aspect 结合 Autopress 就是自动代理，第二节点，也就是也是一级的元素，也就是configure， configure 下面可以支持其他的强aspect，接 point cat 等这些内容。其实这些规范它是通过我们这里面的 spring AOP 的XSD，也就是说 XYR schema definition。我们了解了 spring 关于 AOP 这个命名空间的 Xmail Scammer 的定义文件的话，我们来看一下我们如何去读取这个 Xmail 配置并解析它。


在这里面我们有一个是基于 XML 的一个 a o p 的一个单元池子6，你可以看一下它是怎么执行的。首先这个单元词类它执行的内容非常简单，只是我们通过 class pass XR packaging context 把 LP 的 XL 这个配置文件装载进去，直接去获取我们这个 hello b 就完成了，那么我们可以看到在这里面的举动是非常简单的。其实我们知道当我们执行 class pass x application context 过程的话，它其实会通过 XML definition reader 去加载这个配置文件，同时去解析它的过程，我们可以去执行一下，看一下它debug，这里面我加了几个断点，可以在几个断点的地方跟大家去详细介绍。


首先在这里面我们可以看到它会通过 x l b depending reader 去装载这个配置文件，那么我们知道这一步，我们接着向后跳过这个断点进行，在这里面会通过这个 XML being depending reader 去 load being definition，也就是装载我们的并定义文件，我们可以看到这个 resource 文件，也就是我们这里面是它的描述 pass resource o p 的XL。好，我们继续通过这里面，我们继续到下一步。在这里面我们看到它现在是已经把文件加载完成以后，它需要对这个文件的进行解析，就是 pause being declining reason，它是通过 defailed being definition document reader 来完成的。在这里面是解析的过程，我们去看一下，它会判断一下我们当前的这个delegate，也就是说当前这个对象，也就是支柱的这个 element 是不是 debug 的 name space。


这个我们在讲 LC 容器的时候介绍到过这个 debug name space beans，它是我们默认的namespace，其他的比如AOP，它肯定不是我们默认的namespace，如果不是默认的 name space 的话，可以看一下，它会执行到这里面是通过 delegate plus customer element，也就是说它已经不是 detail element，就是对应的我们自定义的一个element。


当然这不是我们自定义，这是 spring AOP 自定义的，我们继续在这里面，我们看它执行到我们 pass customer element，也就是说自定义的这样这个我们跟进去看一下它执行的操作。它跟进来以后需要做的事情是什么呢？它会通过一个 read context 获取到 namespace handler reseller，也就是获取到一个命名空间的 handler 解析器，这个解析器它去 resolver 这个 name space URI，也就是说它通过这个 URI 去解析我们的 name space handle，我们通过这里面可以看到这个 name screen UR 是对应的，我们 schema AOP，那么我们通过这个 URI 找到我们的 namespace handler，那么我们 name three r n 它是如何获取到的？其实这里面它会用到了，也是 string 的配置关系，就这里面我们可以跟一下，跟大家去简单介绍一下。


在这里面解析的过程是通过 name space u r i 去获取一个 handler mapping，也就是说这里面会有一个 URI 和 name space handler 一个映射关系，这个映射关系是怎么获取到的？这个映射关系其实是通过配置获取到的，它的获取的过程，从这里面可以看到在这里面已经把这个 handler mapping 已经构造好了，这里面是对应的一个映射关系。


比如说AOP，也就是对应的是 AOP name space handler，如果是 cats 对应的是 cats name space handler，其实还有一些其他的，比如 UTOS 是 UTO name space Handler，通过这些 Scammer 和 name space Handler 一个映射关系，其实我们可以知道对于 AOPT 我们就是 AOP name Handler，那么我们这个关系是怎么构建出来的？其实这个关系我们可以从这里面看到，这里面有一个 load or prize 是指定了一个 handler mapping location，我们可以看到它是对应的内容，就是 Meta info 下面的 spring handler，它在这个配置文件里面去注了一个映射关系，我们可以看一下，在这里面我们找到 AOP 下面的 spring handlers，它定义了一个 k 和value， k 就是对应的 schema AOP 它的 value 就是 AOP 的 namespace 这样一个handler。

