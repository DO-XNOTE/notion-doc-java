---
title: 2-18 Spring WebFlux源码解析-1（2251）
---

# 2-18 Spring WebFlux源码解析-1（2251）

[image](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/87b2b3ff-b68e-415d-88f2-e015fe8ba5a4/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46646VO367L%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T232018Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIBwfuYSWORO%2FR2ksaNgZ7cKnHudFRGrAg7Y4O22ha9N%2FAiAKQjQA5cz5HnAP0S1d%2FyqW7FvOLHnYV8boPsYuYZ1J1yqIBAjG%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMMa3gDgTrHmvEq0prKtwDcBZgMzMXtbRPT%2F5SbYdhmRKmzSRE0oTojeaMV3EXMU%2FpR0D8oSExRLYOIodAf77sxEnRWNopZaMN8eUvR6Uppc%2FncoA38FEMvlpA%2BR8Yj8Sg1cTYFY4rFSSLcmfvGUSAECjF%2F8A88%2Brh5OoDNqnq04CFnHthYcCPKo6baU94W3oe%2FTrp9H8UABhhWoHXhQiPmet%2FoErfBgflaxpJroRbnXWAOnZMnSnZYsPW4%2BXNGPkxOY7czF%2Fqq6VBqm4ljePhbLO6o3O2I2p3h8AIM%2BwboDy3KO4Wpiufkcydc1K1sdSLcLz87j5reJ%2BHtXe1C%2F1fpu%2FGTH486%2FSm6CG5Nwoec9F8yIHF6ndjm0Efkuj%2B7O3zPUS5mingXY%2FUarlgcc%2F9TlNSiozZ0vfoG8bvg4RQRRx69UB1mxSlPG6qElIzDb8Uey6Nv%2FupDx1uNIjgEoKjRAIJUn3aK3RbLrv4tJ7t767Zzja1qEZg0VoLlXpHZ%2F%2B2la1bbSuFP2ElpvFZ35gWd%2Fv51XxAvEdZhKbOKOaDdO13BmjhPc4kEKA%2B7B9C6FtZ0rJuyHt9bm1R7BbHTdsF%2FxoJfDoflqkKJTH2j0ZnPwhPJ0Ir%2BdQVUmT%2B7MRudU2%2BExeZXdGUmpaxlzAwp7f%2F0gY6pgGmNSdT9O%2FTjYVtBO0mpvgi9rVR1uUMRE5A4HX1THcm%2FlQKeaLuTIY1tpGqOpD%2F0E4FbMidsq1H%2FtgDgM%2FdJ0R6ug42A3IMA10J9%2BU9TFAjtYxFaKnO%2BRi4hxL3x1mCmRLsiJQF3L4Diwz65yTMiHdT6m9AbwsJ1mKTWFYPRizuMpl2Wa30m5fuhcyVgpYI%2Fz7ynOGuZXstw32lDn854asHo8CXGtMB&X-Amz-Signature=dc9d69b1c5a4f06a68032fcd38f0c8af6c6cc0425594d35b52d436f8f63d02ba&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

接下来我们来看一下 spring wear Flex 它的一些启动流程，那么在这里面我们刚才介绍到对于 wear Flex，因为它诞生以后 spring boot 已经比较成熟了，整个 Web flags 的使用一般都是基于 spring boot 来使用的，所以说我们对于这个启动流程是基于 string 布的启动流程来介绍这个过程。


首先对于 wear Flex，我们去想象一下 string 布置的启动过程，我们首先是通过 spring application round 方法去启动整个 string 容器的开启的过程，那么我们要知道它还在启动的过程中会选择我们的 application context，它的实现也就是我们容器的具体实现。对于 Web Flex 这种容易系，这里面默认是 a notation configure reactive Web Server are Pixel context。我们可以看到这个容器的定义名称是比较长的，但是通过这里面的命名我们能理解它的意义。首先是基于注解的同时基于可配置的一个 negative Web Server，也就是它能把整个我们这个容器里面特征得体现出来。那么对于这个里面，我们获取到这个构造的我们的定义容器对于 Web Flex 相关的重点的操作，也就是首先我们要去注册跟 Web Flex 相关的这些 auto configuration 一些自动装配。那么对于 spring boot 里面的跟 Web Flex 相关的自动装配，这里面我主要列出来是三个。


第一个是跟 Web Server 相关的，也就是说我们在启动我们容器的时候，对于我们 Web v seed 开发，我们会启动正常的一个 time cat 的容器，或者是摘体的相关的容器。对于是 active 的 Web Server，它这里面是提供了几个可选项，这里面默认的是用的一个可集成的一个 natty 的一个 Web 服务器，同时我们可以选择一个可集成的targeted，这里面的 Tomcat 跟我们 strong lace 里面的 Tomcat 其实内置是一样的，只是它实现的方式、开启的功能是有一些区别而已。同时这里面还有像 jetty 相关的一些服务，当然这些服务它都是基于非主式的协议去实现的，这是它的 Web Server。


有了以后，剩下的就应该是 one Flex auto configuration，这里面的 auto configuration 是注册哪些内容？我们可以从这里面看到，首先它会通过 enable whatflex configuration 这种方式去开启它的注释，开启它的一些注解的解析。


那么对于 enable waterflex configuration，它继承了 delegate Web Flex configuration，这个大家应该还能记得，我们上一页提到我们的 enable one Flex 这个注解就是以待它去配子的，所以说它会定义对应的跟我们 wear Flex 相关的一些bin，这里面包括哪些bin？首先就是 request Mapping， handler Mapping， request Mapping， handle Adapter 这两个类我们应该是比较熟悉了， handle Mapping， handle Adapter 都是它一个是去处理映色关系，一个是通过映射关系找到真正的处理实现的 handler mess 的对应的方法，同时还有一些其他的像 validate 相关的一些辅助的bin。 being 的定义的名称的还是跟 spring MVC 相关的内容是非常一致的，那么同时这里面有了我们跟 three V c 相关的这些定义的bin，同时我们看还有一个词 at t b handler auto configuration，这个怎么理解？它定义的就是 Dispatcher handler 跟我们对应 THREAD 是 Dispatcher THREAD 是对应的这样一个关系。


对于 Handler HTP Handler auto configuration，它这个里面只有一个构造 in 的方法，也就是对应的 HTP Handler，我们通过 HTP Handler 它的默认实现就是 disparter handler 这样一个过程，那么在这里面我们通过 register auto configuration 完成了对于我们的一个 Web Server 的注册，同时我们跟 Web Flex 相关的这些 bin 的注册同时得到一个对应的 Dispatch handler，这样就完成了我们在 bin 注册的一个过程。


我们接下来看一下 bin 注册完成以后就需要做的一些事情，就是当我们的容器进行unrefresh，当触发 unrefresh 的时候，处理的一件事情就是 create Web Server，也就是真正的把我们的 Web Server 创建完成。


虽然我们已经在宾语容器里面定义了，但是真正的创建的是需要在这个功能去创建，在这个创建的过程中需要注的一件事情就是把我们的 Dispatcher handler，也就是 Dispatcher handler 可以理解为对应我们的 Controller 里面的业务了，跟我们的 Web Server，也就是构建出这个关系。


我们知道在 Web m a C 我们用 Server let 的方式的话，我们是通过 departure serverless 构建出跟我们派的容器或surprise，其他 surprise 容器自动判断构建出这个组合关系。对于这种非主式的业务，它的构建的关系是通过 Web Server manager 去构建出来的。通过 Web Server manager 支持的参数，这里面是 Web Server 的一个 factory 和 departure handler 作为参数构建到一个 Server manager 里面，把它们组合起来构建出 Web Server 与 Dispatch Handler 之间的关系。那么当我们整个 unrefresh 完成以后，我们会把 Web Server manager 去跟我们整个容器的它的一个生命周期绑定起来，当 unrefresh 执行完成，会执行 Web Server manager 的 stop 方法，也就是说当我们容器启动完成以后，同时我们的 Web Server 也就启动完成了。


那么对于启动完成，在这个启动的过程中还有一件事情是需要对我们 dispatter Server 的进行一个初始化，这里面对于 Dispatcher handler 初始化的它的逻辑相对来是比较简单的，跟我们 spram VC 里面的 dispater surprise 相比的话，会简洁很多。这里面主要是做三件事，一个是通过容器里面找到我们的 handle Mapping，找到 handle adapt 和找到我们 handle handler 相关的一些操作，里面的代码是相比 spring Web VC 里面的 t Spark serverlite 确实要简洁不少，那么接下来我们通过源码来跟一下整个这个启动的过程。


好，首先我们来看一下 spring Web Flex 它的官方源码，在这里面我们能看到整个在我们 Web reactive 它的根目录下面有对应的几个关键的类。首先是 Dispatch handler，我们跟我们 Dispatch THREAD 是对应的一个关系，同时它实现了 Web Handler 相关的这些接口，同时还有对应的 handle Adapter 和 handler Mapping 这样的一个比较重要的接口。我们看它的命名虽然是一致的，但是它的对应的包结构是不一样的，我们可以在这里面去除一下。


我们在查找 handler Mapping 的时候，我们其实可以找到两个 handler Mapping，这里面一个是我们的 Web active，一个是 Web Server Lite，这里面对应的模块分别是 spring Web flags 和 spring 点 Web MVC 这两个模块儿。


下面的同时这里面是 handler result 跟 handler result， handler 它也是我们在处理我们结果集里面比较重要的几个API。我们可以看到这里面是提供了各种不同的相关的操作，尤其是在 handler 里面对应的对于 handler Mapping 相关的一些抽象的一些实现，这里面有对应 resource 相关的一些区别。我们这里面对于 resource 一个转换定义的内容是放在这里面，这里面是config。


我们看一下对于这里面的 Web Flex，它最重要的就是 enable Web Flex，它作为我们整个默认对于引入的一个引导。我们可以看到这有 dedicate Web black configuration，它这里面配置了一些内容，我们可以在这里面去定义我们自己的一些扩展，电影的扩展可以通过这里面是 Web Flex configuration 它的方式去扩展。同时我们看到它继承了 Web Flex configuring support，通过 time 里面在这里面定义了各种我们需要实现的bin，比如这里面有 dispatter surflight， dispatter handler 和我们这里面是 request Mapping 对应的 handler Mapping，支持他的这些实现。


我们对于这个 string 源码内容我们先看到这里面，接下来我们来通过启动我们的 spring boot 基于的 Wifi Flex 这样一个程序，我们来看一下启动过程中，它跟 spring Web Flex 相关的一些内容都有哪些？好，我们来这里面看一下。


我们还是回到我们的 spring Flex 这个一个 Demo showcase 这种工程，它的引入的依赖是 stream 部的 Suder Web Flex，也就是bug，跟 Web Flex 相关的内容都会引入进来，同时其他的相关性不是很大，这里面是跟 test 相关的内容，这是 long book。


我们看一下整个我们程序的入口方法，就是这个 main 方法，非常简洁的，也就是一个非常典型的 spamp 的工程。这个 spin 步的工程，我们只是在引入的过程中引入了 spin 步的 start while Plex 这样一个主线，那么在它启动的过程中我们要注意的事情是什么呢？我们看我们会知道它会通过 string 布的 PK 存在，它会去扫描整个模块儿下包的内容。


对于这里面我们定义了两个类，一个是 Web flex configure，那么这个可以去做一些跟 Web flex configure 相关的一些设置，这个色值会通过写我们这个 Web Flex configure 这个类里面的这些方法进行我们的一些配置。当然我们这里面去演示它主要的核心流程，不会在这里面去做过多的其他设置，避免对我们的整个流程执行的干扰。


那么另外一个最重要的业务，也就是我们的 Demo Controller，可以看到这个 Controller 它跟我们 spring Mac 里面的 control 实现逻辑几乎是一样的，唯一区别不同就是它的返回值，这个返回值是对应那个 Mono 或者是一个Flex，这也就是说它是基于一个异步的一种处理方法。那么我们现在来启动一下我们的 Web Flex Pixel，来看一下它执行的流程。同时我会在关键的一些节点会加入断点，这样的话我们可以快速的跳转到我们比较关心的代码行列，我们可以在这里面去启动debug。


好，现在我们可以看到在这里面断点到哪儿，我们是断点到 spring application 对应的目录，它这里面就是 run 方法，也就是整个我们在启动的第一步，也就是会到 spring application 对应的 run 方法里面。这里面我们的关键点是什么呢？我们看一下 create application context，它对应的 spring 容器是什么？我们在这里面去看一下。
跟进去看一下，在这里面会通过 a Pixel contact factory 去构建它的一个容器，那么对于它来说会需要指定一个 Web application type，这个 Web application type 我们可以看一下它的值是什么，在这里面我们看到 Web application 它 type 的值，我们可以看到它是一个是reactive，对于是 reactive 类型的话，它在这里面会选择对应的容器实现它的容器实现会指向对应的active。我们看一下这是 annotation configure negative Web Server application context，也就是我们指定了这样一个容器的注解，我们在这里面想它是基于什么去判断 thrillet 还是negative？或者是其他的一个非 Web 的一个 notation config listener，它是基于这里面的 Web extension type。


对于 Webison type 它是基于什么判断？它还是基于我们当前三下文环境里面对于这个 being 的状态情况去判断的？我们继续，那么这会儿我们已经获取到了我们的 objective contact，是个初始化的对象，接下来要注的事情，它就应该去注册我们所有的这些 auto configure 相关的内容。那么我们现在直接到下一个断点，我们这里面看一下它到哪儿，它到这个 reactive Web Server，也就是跟我们的 Web 服务器相关的一个内容。


我们来看一下PPT，这里面我们获取到这个容器的类型以后，需要注的事情是注册这些 auto configuration，那么注册这里面的内容首先是 reactive Web Server 相关的内容，这里面我们可以看到它是跟 Web Server 相关的，但是我们看到它并不是 auto configuration，那么在这里面我们看一下在 spring factory 这个文件里面，在这个配置文件里面，这里面是跟 Web react 相关的。


这几个包结构下的内容都是跟 Web Flex 相关的一些内容，这里面我们看到它有多个，在这里面我们关心的是这三个是 LC handler， auto configuration 就是对应的是 Handler Dispatcher，也就是我们的 Dispatcher Handler 这样一个内容，对应的是 negative Web Server，也就是我们构建的我们的基于异步的一个 native 或 template 的服务器，还有这里面是 Web Plex 相关的一些自动装配的内容，跟我们这里面是一一对应的一个关系。这是 Web Server 和我们 Weblink 的可配置，和对应的是 disparter handler 相关的内容。


那么在这里面我们看它当前断点是到这里了，这里面的原因是什么呢？那我们看这个类呢是 reactive configuration，当前执行的是我们对于集成了 Natty 的这个服务器的一个构造的方式。对于这个集成 Natty 构造方式，它执行的原因是因为什么呢？因为在我们这里面是在这个类里面我们可以看到它因为使用了import，这里面 import 了几个跟我们集成服务相关的内容，里面有Tom，cat， JT 和 Natty 相关的这几个服务。


好，我们现在通过这里面可以看到它已经进入了我们的 reactive 的一个自动装配。那么我们先来看下一个断点，这个现在我们已经孩子带，这是另一个鼻音的内容。好，我们跳过。接下来在这里面是回到了 negative Web Server factor auto configuration，也就是我们这个自动装配的实现的理念。


那么好，我们下一步到这里面，我们可以看到它涉及到了我们的 Web Server manager 的一个组装构建，在这里面我们可以看到同时它这里面的参数是 handler 和 Web Server，可以看一下这个 Handler 类型，对这个 handler 的类型我们可以看到它就是对应的一个 Dispatcher THREAD 的一个包装，在这里面我们看到现在已经生成这个 handler 了，它里面的内容其次也就是我们经过多重的代理对应的是一个 departure handler。好，我们可以看到它在整个这里面是集成的深度还是比较深的。对于 Web Server 它需要依赖到一个 handler 对象去获取我们的 Web Server，我们可以跟进来看一下它获取的过程。在这里面我们首先会创建这样的一个 HT Server，我们可以看到这个服务，它是对应的是 net 的一个服务，所以说他创建的是一个 nice 的服务，我们可以跟进来看一下，在这里面创建 STV Server，同时基于一些配置去绑定一下我们监听的端口号相关的一些信息，我们跳出在这里面获得了 STP Server 以后，它会在这里面去构建一个 rector STP handle Adapter。那么这个适配它是构建出了跟 HT handle 的一个关联关系，构建出这个 handle Adapter，那么它作为这个 native Web Server 里面的它一个参数去构建出这个内容，这样我们得到了 Web Server。


好，我们接得到下一个断点，在这里面我们可以看到我们构建出这个 Server manager 对象以后，它会把它去再注意重包装，这个包装是基于一个 set down 的一个生命周期的一个包装，同时下面会有一个是另一个包装器，它的包装是 start stop 一个生命的周期的一个情况，这是什么意思？我们可以看一下它的一个实现，在这个里面它是实现了 small life cycle 这样一个接口，我们知道这个接口也就是在我们容器启动完成以后，会回调它的 stop 方法，结束的时候会回调它的 stop 方法。这里面当我们容器启动完成以后，会执行对应的 Web Server 的一个 manager 方法，我们可以看一下这里面操作是什么。在这里面其实在这个 start 操作是真正的执行了 Web Server 的一个 start 方法，也就是把我们这个对应的 Web 服务启动起来，也就是开始监听我们的端口，整个这步程注册完成以后，整个这个 Pre Web Server 它进入一个 end 状态。


那么好，我们接下来继续我们看下一个观点，下一个断点在这里面是对应的是 enable Web Flex configuration，这是对应的是 Web Flex auto configuration，这个对应的制动装配，那么在这个制动装配里面，它做的事情就是构造 request being handle mapping 的一些内容。好，这里面是生成widget。


下一个在这里面我们去构建 Disparter handler，它是对应的是我们的 http handler，对应的 auto configuring 去构建完成的。我们看在这一步就是整个装载完成以后，它可以开始进行我们这个 dispatch handle 的一个初始化的过程，在这里面初始化的过程我们刚才也介绍了它的初始化过程，相比 Dispatch third net 来说要简单很多，这里面其实关键的代码也就是这几个步骤。


一个首先是从我们的编译容器里面获取到 handler Mapping，同时把这个值作为一个不可变的一个包装，不可修改的一个集合包装放到 handler Mapping 这个属性上面，同时 handle Adapter 处理超过弱也是一样的，也是包装完成以后构造成放到 handle Adapter 这个属性里面，接下来这是 Handler 需要的 Handler 对于它也是做相同的处理，通过我们容器里面去获取完以后，那么就把它放到对应的我们的属性上面，整个这样一个初始化的过程就可以完成了。


那我们从这里面去看一下，对于整个这个过程处理完，也就是我们 departure handler 的一个包装，这个包装完成以后就去完成我们 start 一个启动的过程，整个我们这个容器的启动过程也就完成了。好，我们跳入下一个断点，就是这里面是对于一个初穿了一个工作条款，在这里面我们可以看到容器系统化完成以后，我们可以看到这是对应的 Web Server manager 这个类，它开始执行它的 sort 方法，这个 sort 方法执行的过程中真正的到 Web 开始启动的一个过程，我们可以跟进来看一下整个这个 net Server 启动的过程是做了哪些事情。


在这里面我们可以看到它会首先去判断一下，去构造这个 STARTER active Server 这样一个过程，在这里面是获取到 active Server 的这个属性，同时去把对应的 handler 去进行一个注册，这样的话我们可以看到它整个是Server，开始绑定我们的端口号，绑定完端口号它就开始注册启动完成。那么好，这样的话我们跳过这个断点，整个到执行到这里面，我们的这个 Web Flex 的程序是已经启动完成了。那么启动完成以后，我们来看一下我们这些自动装配的一些内容。我们可以看到在这里面我们提供了几个自动装配的一个操作，一个是 Web Flex 的一个制动创备，我们可以看它做了哪些事情。
对于这个 Web Flex auto configuration now，我们可以看到它首先去做了一个顺序下的一个构件，这里面是首先是对于 react Web Server，对于这个 Web Plex configure，它的配置是需要在这个 Web Server 配置的之后这样一个过程，同时在这个下面它构建的是一个这是 welcome page 相关的内容，这里面主要是通过这是 Web Flex configure 去配置相关的一些扩展配置信息。


另一个就是我们看到这里面有一个对应的是 enable Web Flex configuration，其实主要的这些配置信息都是通过它来去引导完成的。在它配置的过程中我们可以看到它的父类是 delegate Web Flexon configuration，那么对于它它这里面是做了一些扩展配置的一些处理，那么真正的一些 bin 的构建是在对应的 Web plus configuration 在这个 support 里面去实现的，这里面有对应，但是像 dispowder Handler 或者是 Web extended handler 相关的这一些实现，这样我们就把基于 spinput 的 Web Flex 这样的一个启动流程的介绍完成。


