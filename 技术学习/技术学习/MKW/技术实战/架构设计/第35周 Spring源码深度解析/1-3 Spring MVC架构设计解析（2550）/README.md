---
title: 1-3 Spring MVC架构设计解析（2550）
---

# 1-3 Spring MVC架构设计解析（2550）

[image](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/bcd8459f-d253-48b5-9c30-3d0d5c8c1913/SCR-20240803-lgza.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QUTEQBSM%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T231959Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQC53%2By%2BdzMPavLRkCDcaEg0%2BbU6r04IlH9dOC7H4jY3cwIhALv95bSiaJhAaTPifrDpIqZ2rv5BvZF6Q78zUsZDRo3JKogECMb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgwDGDc%2FLxtTgIykm9oq3AMTYbGS1byaaN1s7wzh5iX5Q75QaZA6uE%2F4rY3jPvK4Zs7NXPekYyPVDG3JH0kD%2FR2EXviM8Ie9jwYqKz6pVtV9PvWNQ4Pu6uBBcP67EHKhf431OB0ssHl4GEk5BbHV4C7IUieHCGLynnLoET2jOnoXzC4liL6iO4K26yHOVv9qU5fNo3rzXkr84lb52d7rFaN5TJIf1HxnTc0cq5IlI4MWDqABvF1YD303xk%2FGEl8l47EhUiQ6Vr%2BSEp6EOlocb%2FoI29l2qDt5eX4dAzoVVVB9Qv7%2BRSMH1d%2FmbwM0dVvXc7KgK3xAEUFQQ8R6vxF27wpnOsqUvJJ0Y%2BxQdOO%2B9%2BNqvAuyIiySkDLilnnp0lZymKCqEKp7%2Bua1n%2FDdlAVDsyinZLbJsuOBm8CG8VkM7LBqaK19vaxlh%2FmZVMb6K2XFFLaWYH%2F3Sidrz6Uj0joXKVYsjCbmfInRGk%2BIaLo3qJLvY5B5fmXEVO4tu3EXA9sWYC9D4XO7hDCuGOiYzp1XziqsXKNglt6cN25%2FWzcWKez%2F1ugLISHuEsDf%2Fh%2BPt6OQJCy4Khi%2FrDstgfRfQNgTA9ndGSXbV6iOg84HDrt5oMAvrQrKnsMboRedw%2FqDxUB51OBlRRlq9GBlGH8TRTDJuP%2FSBjqkAVOtmRquCjw3cEl8IoHkdP1t73cGkrn%2BSNW4Jf4%2FNXj4Cd74rap9yKX0Umf%2F0lmsbpoTvFRjgUpN2880zago06uF1LZYTp8Es6BeR1m0TdnlNyFCHwbJEW3eJ86AJqAPgTEtoTDqECT3N4%2B0sZ1UlT26BwjSf2xaok2acjqByxKXspxTJWq3wVQSlxng1SgTs1eiMUnNWPObQqoF7F9z3Y1pDDAU&X-Amz-Signature=aa1402f3579c41ac43ff5810e112436aa87d8324f926b3009e31e763f206ec6d&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

同学们大家好，这章节我们来学习 spring m a C 架构设计解析。 m a C 是现代 Web 应用程序中一种标准的架构模式，应用非常广泛。我们来看一下 spring framework 的架构图，来理解一下 spring MVC 所处的位置。在这里面我们可以看到，除了我们基于基础的我们的 LC 容器和 AOP 以外，上层一个是数据，一个是Web。那对于 Web 层来说，我们 Web 是作为一个基础的功能抽象。对于 Web MVC 是它具体的实现，公司提供了 Web Flex 相关的实现。相比 Web Mac 来说， Web Flex 诞生的比较晚，市场还处于一个孕育中，而 SPAM AC 它几乎是 Java Web 开发的一个标配了。


接下来我们从三方面来介绍一下 m a C 架构层面的内容。首先我们了解什么是 m a C MC 模式的主要原则是为不同的主键具有明确责任的架构。接下来带领大家深入认识 MVC 模式三个参与者之间的关系。第二，认识一下 spring ways 的核心概念，这里面会给大家介绍比如说dispatch， the write，handler，Mapping， handle Adapter 这些核心概念它在 stream AC 整个具体流程中所起的作用。


最后我们介绍一下 spring MC 的实现原理，了解一下整个 spring MC 请求说骤的过程。首先我们看什么是Mac，直观理解的话， M a C 其实就是模型 model 4 图 view 和控制器 control 了三折的组合。那么对于一个业务系统来说，模型是业务的核心，用于表示业务数据以及业务上下文中应用程序的状态，比如说用户的属性，订单状态，这些属于业务模型的内容。


试图试图是把业务数据展示的方式表示出来，它主要用于支持用户交互，支持客户端渲染 UI 样式等信息。那么现在的加后端开发提供的视图主要是 Jason 为主了。对于现在越来越复杂的前端处理逻辑， Jason 它反而变成了前端工程的模型层。现在通过各种前端框架，比如说VOE，erect，它们把数据和渲染逻辑进行了抽象分离。 lesson 是作为数据，它代表了模型层渲染的样式是对应前端的四图层，所以说具体说我们Mac，它某一个功能具体代表某一层是跟它的上下文环境是相关的。那么我们来看控制器，它主要用于处理前端用户执行超出的请求，与服务层交互更新模型信息状态，以及根据执行的结果将用户引导至适当的视图。所以说 MVC 它并不针对某个具体的实现，它只是对我们交互逻辑的一个定义。


首先我们可以看到一般情况我们通过用户发出请求，这个请求会来到控制器端，对于控制器它会根据我们请求的逻辑去路由到对应的模型操作，在这里面一般会进行我们状态的改变或数据的变化，我们通过模型改变，它会返回相应的数据，就是通过请求效应返回数据，也会到控制器程。


在控制器程它可能会有一些操作，比如说如果说需要选择特定的 4 图，那么就把特定的视图进行数据渲染返回过来，或者说还有一层它可能是需要返回 JSON 数据，在我们的后端它属于视图的一种，但是对于前端来说，它就是我们模型结构。其实还有一些事件触发机制，比如说我们模型它触发了事件变化它的状态，发生信息的时候，它可以用一种推送的方式去改变我们四组的渲染，这种方式也是我们四点驱动的另一种机制。通过这里面来看，大家已经对模型 model 4 图、 view 和 Controller 控制器已经有一些了解，接下来我们看一下 spring IMC，它对于我们架构的一些解释。


整个 spring IMC 它是运行在一个 serverless 容器里面，比如说像 Tomcat 和Jetty，它是 thrilled 容器。那么在这里面，对于我们所有的请求，它会直接打到我们对应的前端控制器。在此 MVC 里面，它的表现形式就是 dispatcher 来的，通过前端控制器进行对于我们的请求的一些包装和代理，它会执行到我们具体写的 EO Controller，我们写的 EO Controller，它就是我们前端控制器和我们数据模型层的一个引纽带，我们通过 control 去调用我们的业务模型返回我们的业务模型数据的变化。通过数据变化我们还回到我们的前端工作器，前端公磁器根据模型相关的一些视图信息获取到我们的 view template，也就是我们的视图模板，通过视图模板进行数据的渲染，我们返回给前端可展示对应的 XML 格式，但这是一个常规的逻辑，现在 three m a C 更加大众化的需求，也就是我们返回的是 json 的格式。


好，下面我们来看一下 spring m a seed 核心组件。在这里面，对于 smart message level 最重要的也就是它的前端控制器 Dispatch thats，通过 Dispatch THREAD 可以引入到对应的 Handler Mapping 和 Handler Adapt 这两个核心组件。同时在我们 handle Adapter 处理的过程中，可能对一些异常需要进行处理，这里面就是 handler exception resolver，我们需要对于业务抛出来的异常进行一些处理，返回得到对应的一些视图的响应。


接下来就看对于 handler interceptor，这就是我们 stream Mac 提供的拦截器，我们可以在整个请求的所有处理过程去介入一些我们的统一处理拦截。我们再看是 wheel resolver 和view，这里面就是视图解析器和我们的视图，我们通过视图解析器找到对应的视图与数据进行渲染，可以返回给前端进行一个视图的展示。其中中间对于数据的处理，我们很多是基于 Flash Mapper manager，也就是管理一下我们整个上下门数据的一些数据情况。这些核心组件我们可以理解为一个 spring MC 里面单独的一个知识点，但是它们之间的关系是怎样的？我们来看一下。


首先我们是基于 stream a C 核心组件加载的顺序逻辑来去解释，在整个这个过程，我们只需要通过一个加 Web configure 来去配置我们的 m a C 流程，在这里面我们需要配置的内容是什么呢？首先我们要配置一下 root configure class 和我们的 surlight configure class， root compare class，它是用来去初始化我们的一些基础数据，比如说像我们的 data source d u three 层，这里面一般包括除 Web 层以外其他的一些bin。那么对于 Server context，它为了初始化的是 MC 相关的一些内容，这里面会包括 control handler Mapping、 handler Adapter 和我们的一些视图解析成。这里面的 spram v c 设计成两个容器，一个是作为根容器或者称为父容器，另一个是成为我们的 serverless configure，对应的容器也可以理解为子容器。作为这两个容器对于我们 Web 层和非 Web 层内容做了一层简单的隔离。


首先我们父容器里面放的像我们的 data source， d o service 这一些跟 Web 无关的这些基础的业务模型，那么我们的子容器是首先子容器，它的 part 是我们的父容器，这里面它设置了跟 Web 层相关的一些主键，像 control handle Mapping 这样去做一些处理的话，其实如果说我们系统如果是在 Web 层去做一层隔离的话，我们可以看到这里面我们可以支持多个 control 层的子容器，它们可以共同相同的父容器，这样去做到了一些我们父容器资源的共用，并且能做到子容器之间的隔离。


好，接下来我们来看一下 Sperm IC 它执行的流程。这里面涉及的组件内容比较多，如果大家第一眼看到这个图的话，可能会有眼花缭乱的感觉，但其实我们仔细分析一下，其实整个思路是比较容易理明白的。首先我们对于整个 stream c 组件，它还是基于 Web configure 去初始化，整个我们注册必应容器执行完成以后，它才能去接受我们的请求，那么从这里面接收请求也是基于 h t p 方式去接收请求，对应我们 i t p 的请求，它首先会达到我们 despite script，同时在 departure THREAD 里面会对我们的 request 的信息进行包装，通过 request 里面去获取到我们对应的 handler Mapping 所需要的一些关键信息。


在 handler Mapping 里面去找到我们对应映射的内容。通过 Handler Mapping 里面我们会获取到一个 handle excuse chain，也就是我们获取到一个执行链，在这个执行链里面它会包含我们的 spring IVC，对应的拦截器以及我们的 handle Adapter。我们通过执行我们的执行链，最终执行到我们 handler Adapter 的过程。
在这里面会涉及到一些数据绑定，一些参数转换等，这些工作做完以后，它就可以执行到我们对应的handler，那么真正的 handler 也就是我们写的这个业务的 control 的方法，我们在业务 control 的方法去执行我们业务模型数据的处理，处理完成以后会返回一个对象，对象它会通过这个 return value handler，也就是我返回词的一些处理器进行处理。它通过这个 return 的 value 内容去判断我们是需要返回 4 图进行 4 图解析，还是我们通过 it message convert 进行处理。那么对于一般来说，我们如果说使用了像 add response body 这样一个注解的话，它就会直接通过 it master convert 的方式把我们的数据通常会转化成 json 返回我们的前端，那如果说这里面我们设置了我们的视图，那么它的处理会相对复杂一些。


在这里面 Handler Deepen，它会想返回成一个对应的 model noview，一个这样的对象，通过 model view，它里面包含两部分内容，一部分是model，另一部分是view。 model 就是我们对应的业务数据。 view 在这一层是一个 real 的一个表达形式，这个表达形式通常是一个字符串，也就可以理解为对应我们这个目录的一个 JSON 模板，我们的一个视图模板。


通过视图模板的一个解析器，比如说我们是framework，或者说是我们 same leaf 这样的一个视图解析器，解析到对应的视图文件，通过解析到这个 view 对象，用 view 对象和我们的数据去进行渲染，渲染完成以后去返回我们的前端，最终会得到我们正式渲染的数据。从这里面可以看到这是整个 smart VC 它在执行流程中所经历的这些步骤。其次里面还有一些更深入的一些细节，会等我们源码详解的过程中去跟一下。


通过这几点我们可以知道，对于一个 MVC 请求，它会主要分几部分，首先请求它会到 Dispatch thread，接着它通过 Dispatch thread 通过请求里面一些关键信息，比如说像 URI 和我们请求的 Mesh 的类型，它是 get 请求还是 post 的请求等等。


去 handler Mapping 里面获取到对应的 handler excuse chat，也就是我们的执行链，通过执行链里面的拦截器加载到我们 handle Adapter，最终执行到我们的Controller，通过我们 Controller 返回的值，通过 right value Handler 的判断它是需要返回视图，还是说直接通过 active master convert 转换为字符串返回给我们前端？整个这个过程也就是通过 departure try 的转一圈，把我们的数据响应给我们真正的用户，这就是 string VC 整个处理的逻辑。


通过我们前面的介绍，对于 spring AC 我们可以这样去理解，首先它最重要的就是我们的 Dispatcher Lite，基于 Dispatcher Lite，它可以构造成两个容器，一个是我们 THREAD Web application context，另一个是 root Web application context。其中我们的 Web application contact 它是依赖到我们对应 root 的 Web application context，这样我们能做到对于这些根容器里面的 service 和 repository 这些组件可以做到跨我们的子闭容器的一些共用。也就是说我们的根容器里面的内容可以被不同的我们几个 serverless 子容器里面的内容去引用，这样可以支持我们这些 Web application，也就是 serverless 成的这些指容器的一些隔离。现在我们通过一个项目模块来演示一下 smart PC 相关这些主键之间的主合关系。


好在这里面我们看一下我们这里面搭建了一个是 SPLAM AC 这样一个model，在这里面我们还是从最重要的我们 palm 文件开始，这里面我们 palm 文件里面是写的相对来说比较复杂一些，我们首先可以看到我们的依赖关系，在这里面我们首先要加入我们的加 x series API，这个依赖一定要注意一下，它的 scope 标志是provided，也就是说我们打包的时候不需要把它打到我们的包里面。


接下来是 spring Web i miss 相关的依赖， spring Web i missing，它间接地依赖了 spring Web 和 spring core 这些相关的一些内容。后面是跟 Jason 相关的，也就是我们对于返回数据 Jackson 序列化相关的意思，这里面也有 Jackson annotation 和 Jackson did band。接下来是我们的logback，也就是说打印日志输出相关的一些内容，像 Llama book 就不用再介绍了。


后面就是我们的 spring test 跟 spring IVC 相关的 test 内容，它依赖的东西比较多，这里面我们有丘比特 home Chris 以及下面的 json pass。我们可以看到我们如果说只是为了实现一个 spring 的一个 MVC 功能，我们需要引入的这些内容还是比较多的。相比我们在使用 spring boot 的时候，我们直接引入一个starter，也就是 spring boot starter WAP 来说的话，这样确实反腐了很多。


好，接下来我们看一下对我们 SPA m seed 结构，因为我们现在已经基于 Server light 3. 04. 0 的一个结构去构建，所以说对于我们现在这些 Web 工程，我们已经对 Web terminal 已经不做要求了，就目前来说，我个人和一些大厂的一些默认约定更推荐大家使用 Java Configure 的方式来配置这些 despite surlight 相关的这些 Web 组件。那么对于 spring m a C，它提供了一些抽象的方法，我们继承就可以直接实现。


我们看一下这里面我们定义的是 m a C Web application in lesser，它是继承了一个 abstract annotation configure Dispatch threader Inc center。通过这个命名我们应该知道它其实是提供了一个注册 Dispatch survive 的方法，这个方法它可以基于注解的方式去构成我们的闭音容器。在这里面它有三个抽象方法需要我们实现。这三个抽象方法分别是 get through， light Mappings，这里面也就是我们 Dispatch THREAD 所映射的路径，也 URL 我们默认是撇儿。其中还有我们的 get THREAD configure class，也就是我们对应 Web 容器相关的一些加配置，这里面我们配置了 m a C 加configure，它还同时去要求我们提供一个 root configure class，我们这里面的 root configure class 是返回跟null，这里面主要两个原因。


第一，首先我们这是一个 MV seed，一个 Demo 工程，这里面我们没有实现 DEO service 相关的内容。另一方面作为我们微服务，我们的一个模块相对是比较简单的，我们的模块里面不会有太多复杂的内容，所以说我们就推荐大家使用一个 Thurat computer class 就可以。好，这是我们这个初始化的配子。


另外我们看一下 Web Configure，对于这个 Web configure 我们这里面配置也是比较简单，在这里面我们实现了 Web MC configure 这个接口。我们看一下，在这个里面是里面提供了一些方法，在这个接口里面这些方法都有一些默认实现，我们可以有针对性地对这些实现进行覆盖，这样自定义我们 m a C 相关的一些逻辑，我们从这里面可以看一下，它里面涉及到很多东西。


这里面首先是比如说对于参数解析和 COS 的一些映射配置和formator，这是拦截器相关的配置，这还有一些资源的一些解析，里面有 written value，handler，我们的 wheel controls 相关的一些设置等等，下面这某一些设置它都是基于 three MVC 跟我们留出一些扩展的一些途径。
好，我们回头看一下，在这里面我们要一定要记着开启一下。如果我们基于注解的话，一定要把 enable m Web m a C 打开，这跟我们使用 spring boot 的方式刚好，一定要区分一下。如果我们使用 spring boot 的方式的话，那么这个 enable web YC 我们一定要把它给移除掉。因为这两种方式打开 web YC 的方式不一样，所以说它初始化的一些默认逻辑是有些区别的。


这是我们跟 m a C 相关的一些操作。首先 task 我们在容器启动的时候去加载我们的容器，去构建我们的 m a C 容器和我们的根容器，这个是去配置，去开启我们的 Web MC 以及去自定义扩展一些相关的一些配置，在这里面我们并没有去做什么自定义的一些配置，后面我们会介绍。


接下来我们看一下最重要的，也就是我们的业务Controller，对于这个 Controller 的话，我们实现也是比较简单，首先我们在这里面 Controller 通过 rest Controller 去做修饰，其实这里面可以通过 control 和 rest control 和 control 它的唯一区别，也就是我们可以从这里面看一下对于 rest control 它相当于 control response body 的组合，这样的话我们下面的方法就不需要再单独去通过 response body 去修辞了，这样决定我们在用这种方式去返回的对象的时候，它都会把我们这个 user 模型进行 json 序列化。这里面是也是相对比较简单，我们提供了一些 get by name 一个方法，这里面 name 作为参数，我们通过 name 构造出我们这个 user 对象，把 user 对象返回过去。这里面的 user 我们是一个内部的静态类，我们提供了两个属性对应的 name 和DIC。好，这是我们的country。


接下来我们看一下整个我们的项目，其中的 MVC 加和configure。对于这个 MC 加和configure，我们看到首先它标明它是 configuration 类，同时它这里面通过 add import 的方式引入了我们的 Web configure 这个类，在这里面我们定义的是 enable m a C 相关的内容。


那么接下来我们这里面是设置了一个 campaign scan，也就是我们的主键扫描的包结构，主键扫描的包结构式对应我们 m a C Web 的工程，也就是说所有在我们这个 Web 下面里面构建的这些Controller，我们通过 rest Controller 或 Controller 的方式去修辞的话，它在启动的时候就有扫描，把它作为一个 m a C control 的主键注册进来。好，这是我们这些代码的整个一个组织架构。那么我们可以看一下我们对于我们的 Demo control 方法来进行单元测试的内容。


通过单元测试大家一定要注意几点，首先我们在这里面还是使用 spring during 的configure，在这里面引入我们的 MZ 加 2 configure，也就是说相当于是我们在启动单元测试的时候，它会通过 MZ 加 2 configure 构建我们的变容器，同时我们这里面通过 Web optisin configuration，通过这个注解来表明我们当前这个单元测试是基于 Web 应用的单元测试，在这里面它会跟我们构建出 webadcase contact 相关的内容。


启动的过程中我们可以看到这里面构建了两个属性，一个是 mock m a C，另一个是 Web application context。我们知道 Web application context 就是我们 MA seed 系统对应的默认容器，那么对于在这个默认容器里面，我们有 at before its，这是我们 g unit 5 对应的一个 set up，也就是 before 处理。当我们在代言这次执行之前的话，执行我们这样一个操作，这个操作做的工作也就是通过 mock i m a C builder 构建出我们的 mock i m a C 对象。对于这个对象，它需要传入的参数，也就是 Web application context，也就是我们通过我们这个 w a C 这个 context 作为启动的容器，同时调用 builder 构建出我们的冒牌名字对象。


在这里面我们通过冒牌名对象去执行我们的 Web 方法，我们可以从这边去看到，在这里面我们是 test get by name，通过 lock run 和 lock end 去区分一下我们调研测试的执行前后，这里面我们去通过 mock m a C request builders 来去构建我们的请求。通过 get 方式请求 Demo gotten by name 去执行我们对应这个 control 所需用的方法。这里面我们需要传入的参数是parameter，对应的是 name 和Jimmy。同时我们要求我们得到的一些 media type，它属于是 application json 的类项。我们把这个请求构建完成以后，我们去执行我们的请求。


执行请求的方式是通过 mock m a C 就是 this 的 mock Mac perform，你就是通过执行我们这个请求的 builder 去获取到我们 result accents 执行完成，也就是说得到我们的一些请求的结果，这里面我们对请求结果进行一些期望值的断言。


首先我们这里面 add expect 去断言我们首先我们的状态 is OK，状态一次 OK 就表明当前状态是不是200，因为对于我们 s c v 请求，我们返回 200 认为是正常的，得到请求是 200 以后，我们再去断言请求我们的 json pass，也就是说我们返回的内容是个json，这个 json 对应的 name 属性 shift 我们的 Y6 值几米，跟我们这里面配置的内容是不是一致的。


这两个校验完成以后，把我们的信息输出来，这样就看到我们执行的一些输出效果，这是我们整个单元测试的效果，我们通过这里面去看，这里面的代码比较简洁，看起来可能会感觉比较简单，那么其实这里面需要依赖的单元测试相关的内容比较多。我们通过这里面可以看到我们在这里面写入单元测试相关的内容。下有 spring test，很有精力的，对应的丘比特的 APIM Christ 以及我们 Jason pass，这里面跟代言测试相关的依赖就有三个。


好，我们看一下，在这里面我们执行一下我们的输出，看一下执行输出的内容。好，我们启动这个方法自行，现在执行成功，我们可以看到它返回打印结果的内容。首先我们可以看到这个是绿色的，也就是说我们这两层断言都是正常通过了，也就是说这是没问题的，我们重点看一下 Pronder 的内容，这里面还是我们打印出了我们的 request 对象，和我们head，和我们下面 model view， Flash map 以及我们的 response 对象一起可以看。


首先我们的 request 对象是我们这里面构建出来的对象，它的 x masses get 它的request，URS， demo get by name 以及parameters，它支持的一个参数就是 name 机密，并且 heights 定义了一个要求， accept 是application， json 就是我们这段的配置，配置的 media type 其他的要求就没有了。这里面是 body 是空的， setting 绘画的内容也是空的。


好，我们handler， handler 指定的类型是 Demo Controller，对应的方法是我们的 Demo control 对应的 get by name 这个方法，这样我们通过我们的 URL 定位到我们的handler，这里面我们的是否异步执行是false，也就是我们不是异步执行。这里面是 resolve 的exception，跟异常解析相关的类型是null，我们这整个过程并没有抛异常。


这里面还有 model 的view，因为我们返回的json，所以说 model 的 view 它的内容都是null，也就是说没有model，没有相关的对象内容。这里面的 Flash Mapper 加相关的内容也是人脑，我们并没有去存储一些三角乳环境的属性，这我们可以看 mock LTP serverlite response 就是我们的模拟的一个想象对象，这个想要对象我们可以看到内容是首先它的 states 是200，就是它的响应请求是正确的，同时它的 error message 是null，因为它并没有发生true，所以说并没有 error message 这面hides。也就是说这里面我们添加了 application json，后面我们的 context Tab 也是 application design，它返回的 body 内容就是我们在这里面构建出来的这个 user 对象。
我们看这个 user 对象，我们构建的它是有两个属性，这两个属性分别是 name 和DESC，分别对应我们这个 body 里面的 json 的 name 和DESC，它里面的内容。首先 name 是我们作为入参传入进来的机密，它的 DSC 这里面我们默认写固定的是 this is user for demo。其他的一些内容，像 forwarder 和redirected，它都是闹的内容cookie，也并没有设置什么内容好。这样的话我们可以看到整个我们的执行完整，这是我们写的end，下面有我们对应启动的wrong。


好，这是我们 stream i m a C。一个最简洁的一个工程的一个执行的过程。关于 spring m a C。价格成本的内容，我们就先介绍到这里。到后面的话，一些源码阶段，我们再会跟大家去介绍整个 spring i m a C。执行源码跟踪的过程。同学们，我们先介绍到这里，下一节我们再见。











































