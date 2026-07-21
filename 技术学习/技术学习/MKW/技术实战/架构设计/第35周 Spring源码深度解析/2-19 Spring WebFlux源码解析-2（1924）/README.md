---
title: 2-19 Spring WebFlux源码解析-2（1924）
---

# 2-19 Spring WebFlux源码解析-2（1924）

[image](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/ec19b01e-51b5-4a9a-94c4-565e13ca6e58/SCR-20240803-oghu.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UGKOJJRB%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T232019Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIAeQXcVYdqPkQu%2BsQY%2B1rJ0R25fMCPkE2Ni8Wu0OCSyPAiEAo3QEt0bpY2IqI2MA1e462xUJsSxcmJFdfF3GJFpFo50qiAQIxv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDBpaXVgSNSto%2BvvxzCrcAxC%2FE%2BERdsaeNoPCq%2FGLekbchFEZypPAXlI0egGGvm4O26QDL%2FBiD8EZfGTtNTX3qY3jPDvWonP0wfedr15Ry38TPELpne1N%2FR10TiEZkTU1zmKyxAu%2BRChd2Wm42KjrxygaqIbSgfq2pIg70juk9F6g08GX9qMIZxGiFo2CzpfTib0%2BiXoUU1Syh9Ij0oE7soD6naJ8%2Fr%2Fx1BXiikTADQD4n%2BHeyfxQ43fx2dmY0oRj8Bc5i%2FlKyoLU1Ojadl1lnZGE%2FhmyegX0wn%2FVEEnHTj%2B%2FwdnzZlYpevwqSvG%2BENWnCQi1IfBID9ZEJt5Yrmp5KTQAcpTIeX%2BIRwdEGtKbFkjbmY15AO0iISHKI3E1YNB%2FF5ZXgKT1vHsRblwT5utBwKCKAZhmmJlqyw8hFz7acqfYS7fvSEDWxEUZ63anta%2B9TNmVQfMjqi1u5ZQA8Xo401wrhEZPX0Pbe20LPG9b9g2VSjmQAiWE3U2RuD%2BQCmAU1WT26yzNcSSDsX%2FXTgabrM9K54HwIRMqDtL7L2km%2BosKuUrKThWF5bwQ2nPXMm2mCOaMIGKIFLXo3qxNn%2Fb%2FmZEyX5mDHkuSHTU%2FOZzPDRfS35YFwFbPuIUTXtj4pqOjKQ8uTpsPinJSCZEhMMK3%2F9IGOqUBMe6Dre9MIIpp9m8pdDLfcmcQ04KK5YOTFL6k6IZGOolDc%2FQZ7v73BAE%2FBDoEvHev5cHPV0aCo4ctJscfZX%2FRP%2FI1MqaiRNWERQZABGwF9HUn0e%2B5O5HFvFGXLQ0FqM0bU65FzRpa%2Bps9aXxQwfBb6TeyOuxNPXKIm67Z98swnWK5qx6Qe9%2B0%2BmOO2HFawRG6WPTAk06pWjnT8A%2FK6llpB0HvSLiQ&X-Amz-Signature=ae2f8f844a6fd071d289bc720084119d23a6cab383de747b902a8cb1151a7d01&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

接下来我们来看一下 Wolflex 它的请求流程。我们在讲它的架构原理的过程中，我们介绍到整个 spring Wiveflex，它的请求率分大概是这样，首先我们请求它会通过我们的直接打到我们的 Server 上， Server 会对应的 active Adapter 去做一个适配处理，对应到我们的 string Web Plex，它的核心的一个 handle 控制器上，最终的到我们的 Controller 接入了。


通过 Controller 去也是通过 Flex 异步的方式去获取数据的一个相关信息，那么我们在这里面去找一个对应关系，首先这里面的 Server 跟我们程序对应的，也就是 net Server，这里面的 negative Adapter 也就对应了我们一个 Web handler 的一个转换的一个过程里面的 spring Web Flex，这一层的包括我们可以理解为对应的我们是 discharge handler 去处理的内容，这个里面也可以理解为我们的核心的一个控制器patterhandler，它通过 Mapping 映射找到 Adapter 包装，这个 Adapter 包装就对应的 control 里面的一个方法。那么我们获取到这一步的话，整个是 Web Flex，它的核心内容就执行完成。那么我们来看一下基于它的一些核心 a 撇的方式，去看一下它整个执行的过程。


首先在这里面我们所有的请求过来以后，都会对应到我们的一个 Web 服务的一个适配上面，也就相对于说我们如果说是普通的 Tom cat 服务的话，我们请求过来以后都会打到对应的一个 survelight 上面，对于 survey VC 对应的是 despite survey 的。对于我们的 spring Web flags 请求，它也会打到 at b handler 上面，通过这个 ITV Handler，它会去进行一个相关的处理，这里面会有一些区别。如果是 Natty 的话，它会直接请求到 negative active handle Adapter 这样一个类里面 play 的方法对应。如果说是 surlet 的 s p handler，比如这里面有 jetty 或者汤姆 cat 的话，它会请求直接打到 threader t p handler Adapter 上面。


这个我们就可以理解为我们 active surreder 的 service 的方法，它的原理是可以这样去理解的，那么我们得到这个 Activhandler 对应的操作以后，它要做的事情是什么呢？是需要做一个请求的替换，我们需要把 ITP Handler 替换为 Web Handler，对应我们替换的方法，它是通过这个 at TCP Web Handler 第一个 d Adapter 一个适配器去做的，我们转化为这个 Web Handler，也就是我们 Dispatcher hunter 的一个实现。


对于这个 disarch handler 它处理的操作，我们对比着 discuss THREAD 它的一个做的内容，其实也是首先是根据我们的请求信息，比如说我们的对应的 URL media type 相关的一些信息获取到我们对应的handler，获取到 handler 以后，对应的 handler 去执行一些 invoke handler，我们执行 invoke handler 需要做的一个事情，对于 invoke 之前会把我们整个操作的去包装成一个 invocable handler master，这个跟我们 SPU m a C 里面也有一个同名的一个类，它们只是名字相同，它们实现的方法还是有些区别的。对于它的一些处理的话，也就是首先要注的事情，也就是对于参数解析，把我们携带的这个参数经过解析转换映射成跟我们对应 control 的方法里面的参数是一致的。


注成一字以后，我们就开始执行这个对应 mess 的一个 invoke 方法，也就是通过反式的方式调用我们 control 的一个具体的方法，这个方法执行完成以后，它会生成一个 handle result 对象，对于这个 handle result 的对象我们是不能直接去返回的，我们需要对这个 handle result 对象来进行转换。跟我们 spram a C 里面对应的 return value 的一个 handler 是对应着的，它也就是说把我们的返回值去做一些处理，它处理的方式也是根据不同的 handle result handle 的实现。这里面比如说指定的四个词线有 service sponse result handler，也就是返回此次 service response 的，它会通过这个 handler 去处理。那么如果说是通过我们的注解 response body 修辞的话，它会通过这种方式，或者是我们会返回一个 response int 这样一个对象，它会通过这样一个对应的 result handler 去处理。


处理完成以后最终的输出到我们的前台效果，也就是通过我们的响应头响应出去，这里面会涉及到对应的 active message writer 这样一个对应的一个写入器，它会写入到我们的响应信息里面，这样的话就会完成了我们整个流程的转换。那么在这里面执行的过程中，其实还有一部分是我们可能并没有注意到关注的一个点，也就是我们的 handler Mapping。


handler Mapping 的处理过程其实跟在我们这里面去处理，这个在 handler 的过程是通过 Handler Mapping 去完成的，因为整个这个代码它是基于流式的方式去处理的，它的那个结构性的话看起来也是比较清晰的，但是可能有一些细节我们在 debug 断点的过程中并不是那么明显，那么我们在这里面看到完它整个一个执行流程以后，那么我们通过请求来去观察一下整个 debug 执行的一个过程。


我们现在切到源码，那么现在我们呢来发起请求，我们看发起请求断点进来以后，我们可以看到它就到了，对应的是 react ATV Handler Adapter，我们通过这里面去看到跟我们这里面是 ITU handler，对应的是 active Rector。 ITP handle 代表音就是我们记忆是 negative Server。那么在这里面我们看一下这个 apply 方法它做了一个什么事情，我们看首先它会把我们原生的这些 HTP Server letter request 和 LCP Server letter response 进行一个包装，包装成对应的是 Raptor activity， Server request 和对应的 Server activity response，包装完成以后，它会委托 activity hunter 这个方法去进行一个 handler 的处理，我们跟一下看一下这个 handler 的内容是什么。


对于这个 handler 我们可以看到它是一个 delegate initilesson 的 active handle 的一个包装，那么我们可以看一下它里面住了一个什么事儿，我们可以在 debug 跟进去，在这里面我们切切注意一下它在 debug 进入的时候比较一定小心一小，我们这里面选中 handler 点击进去，在 Handler 进去以后，我们可以看到它有一个delegate，这个 delegate 就是对应的是 HTTP Web Handler Adapter。


那么我们刚才介绍到基于这个 HTTP Web Handler Adapter 去做了一个转换，它这个转化的内容也就是把我们的这个对应的是 h t b，也就是说我们的 h t p Handler 通过它转化成我们的 Web handler，那么它这个转化的过程下一步就可以转换成 Web handler 的过程。那么我们先来跟进去，这步跟进去我们看一下它转换过程是怎么完成的。


在这里面它要做的一件事情就是首先是把我们的 request 和 respond 对象进行一个包装，通过 create exchange 的方式包装成我们的 Server Web exchange，那么我们看一下它是如何完成这个包装的过程的。


我们点 debug 进去，在这里面的话，它会通过 debug 的一个 Server Web exchange 它的操作进行一个处理，这里面构建了很多参数的一些内容调出，在这里面进行包装，完成以后要做的一些事情，我们可以看到它根据情况是否要打印一下 debug 日志，那么在这里面去接会再用我们的一个 delegate 去进行真正的 handler 处理。
那么这个 delegate 是什么对象？我们可以看一下，在这里面我们根据看一下这 get delegate 这个delegate，它这里首先是 the seven handler Web handler，也就是说要判断一下是不是有异常相关的处理的内容，那么我们不必纠结，我们进去看这个 header 的处理，那么我们点进去在这个 handler 层的处理的过程中，它会去执行 super handler 的操作，那么我们看一下在这里面它处理的一些内容，我们跟进去看一下，在这里面会用到一个delegate。


这里面我们看到这个 delegate 是个 filter Web Handler，在这里面是我们的 handler Adapter 来去做一个对应的一个处理，这里面我们用到了一个过滤器，一个 filter 的处理方法，我们继续 debug 进去，看到这里面是一个执行链，这个链它的实现也就是 debug Web filter，也就是我们在执行的过程中，它首先会通过这个执行链去包装一下我们当前这个请求过程中是不是有异常的一些处理消息。


如果有异常处理消息的话，就直接执行一个异常处理的一个操作了，如果没有的话它会进行后面的一些处理，那么我们接下来再跟进去看一下它会做什么处理，在这里面我们可以看到它这里面到了我们的是 default filter chain，我们这里面会进行一个发词的处理，那么这里面我们会定位到这一行，我们的 Inbook filter 是这里面要注的事情是看一下当前的 trend FILTER 里面是否为存在。


如果说 pend filter 不等于null，且当前的这个过滤器列儿是也不等于null，这样的话会执行第一个方法就是 invoke filter，如果说这里面条件不满足的话，它会执行 handler 对应的handler，那么我们看一下它执行的条件判断，我们看一下当前这个值它SNO，我们接着下一步在这里面它会去选择执行对应的handle，我们跟进去我们看一下当前这个 handler 对象，它已经是切换到我们的 disparter handler 了。


在 dispater handler 它的处理请求就是可以理解为 y Flex 的一个比较重点的请求了，它执行到这一步就开始跟我们业务方法相关了，那么我们 debug 跟进去，在这里面我们会看到它是到了对应的 disparter handler 这个方法对应的 handler 方法。


在这个 handler 方法里面，首先去判断一下 handler Mapping 是否为null，如果 handler Mapping 如果等于 null 的话，那么直接就 not found， error 就失败处理跳出了我们。因为在初始化的过程中， handler Mappings 构建完成了，所以说这个当然一般不会为now，那么在这里面它会通过 Flex 的方式去做一个遍历的操作，是首先遍历 handler Mapping，把 handler Mapping 获取出来去执行通过 Mapping 去 get handler 的过程，在这里面我们看一下我们在 debug 跟进去看一下它对应的那种，我们是执行 Mapping handler，那么在这里面我们看根据你看的效果。


在这里面我们进来以后，我们能看到当前进的 Mapping 是 abstract handler Mapping 的实现，那么这个实现的真正实现的内容，我们可以看到它是一个 router function Mapping，也就是说它是一个路由的一个过滤，那么因为我们在这里面并没有定义，所以说它这里面并不会获取到真正的一个handler。


我们继续跟进去，我们可以看到这里面当前到的这个 handler Mapping 对象是，我们可以看到它是 request Mapping， handler Mapping 也就是我们这个 abstract Handler Mapping 的实现，也就是真正我们所需要的这个基于注解的 request mapping 的一个实现。这样的话我们应该有预期可以获取到我们对应的这个方法。
我们可以看到我们当前的 result 方法，其实获取到了一个这里面去处理的结果，我们先来继续看它是如何去处理。首先获取到我们的 request 的操作，在 request 操作里面去做一些逻辑的判断，它比如 COS 的一些判断，还有一些prevent，一些 request 请求的一些判断。我们继续现在我们可以看到它获取到了对应的handler，这个 handler 内容我们可以从这里面去看到对应handler，也就是我们的 Demo Controller 对应的 get by name 这样一个方法。那么获取到这个方法以后，我们看一下它要做哪些处理。


我们跳出在这里面，我们看它是获取到了 handler 中 handler 里面去获取到我们的 handle result，这里面它处理的过程也是一个循环的操作。在这里面 handle difters 我们可以看到它有 4 项，在这里面我们更关注的应该是 request mapping handle adapt 对应的时间的操作，那么我们可以快速地去执行一下。


在这里面我们看到对应当前的这个 handle Adapter，也就是我们的 request mapping handler，那么它开始进行我们真正的业务的 handler 操作，那么我们执行到这一步，我们可以看到它去通过我们这个当前的 handler 对象，我们当前这个 handler 对象是一个 handler mess 的一个对象，那么我们看 handle message 对象它要做的是处理是什么？它会通过这个 Mesh 的 receiver 去解析这个 handler method，解析到为一个 invoke invocable handler method 基于这个 include handmethod，它会进行一些处理，那么我们现在执行操作，这里面会有一个初始化的一个操作，初始化会把这些 handle master 和一些绑定的一些上下文对象以及我们的 exchange 作为参数传入进去，然后去进行一个 invoke able master， invoke 就是这个方法就会触发我们的对应的一些参数的执行，那么我们跟进来看一下，在这里面我们跟进来点 invoke 进来。
在这里面我们可以看到这个对应的 invoke handler meshed 的 invoke 方法，它要做的一个事情，这里面我们可以看到它也是通过我们这些流失处理，在这里流失处里面，首先它会通过 get method argument values，就是说获取到我们当前这个请求里面所有的参数。获取到参数以后进行一个 fat map 的转换，那么我们看一下它这个获取参数的过程是怎么获取的，我们可以 debug 跟进的。


在获取参数的过程，首先会获取到 matched parameter 以及描述对象，那么通过描述对象去循环的通过这些输入的 method parameter 去解析解析并初始化这些对应的一些参数信息，把参数信息执行完成以后，它就会构造出一个对应的参数对象，那么我们现在执行完成的过程，我们就跳出这个过程，我们跳出在这里面我们看如果说 get mass argument value 获取到正常的值以后，执行 flat map 操作，在这里面我们已经得到了它的对应的参数。我们可以看到这个参数里面，这是我们带的参数，也就是我们请求的值是一个 test 的值，那么在这里面会去进行 Mesh 的invoke，我们这里面同时去指定一下获取到单件 get bin 和我们的参数信息，那么开始进行我们的 evoke 操作，我们跟进去，在这里面我们去执行，现在已经到了我们的业务方法，在这里面我们可以看到执行的业务方法的话，也就是我们就比较清晰了。


那么我们开始跳过，现在我们可以看到执行完以后，我们即得到了一个result，我们 result 对象是什么呢？是一个handler， result 对应的类型是什么呢？它对应类型就是我们这里面指定 result type，就是我们的 Demo Controller 对应的 user 下面这样一个类型，那么其实它的 return value 的内容是一个，我们可以看到这是一个 Mono 炸死的，也就是我们一个对象，它发处罚一个对象。


接下来我们要注的事情是通过这个 monodize 去获取一下我们 reset handler，我们看一下我们能得到一个什么样的 research handler，我们跟进来，我们从点这个进来去看一下，我们看当前是否支持我们找对应的racer。我们可以看到通过这样的操作的话，我们获取到的 result handler 是一个 response body result Handler 为什么获取到这样一个handler，我们可以回到我们的对应的 handler 方法里面，这个方法其实是通过 sponsbody 修辞一个方法，那我们得到这个 result handler 以后，它开始进行我们的 handle result 操作，那么进行 handle result 操作，它其实处理的过程也就是相当于把我们的这些信息写入进去，我们可以得到一个body，这个 body has more than just。同时去获取一下 measure permeter 的一些处理，进行我们的这些信息的写入，也就是写到我们的 response 对象里面，这里面我们接着简单跟一下，在这里面我们可以看到它的一个处理的过程，处理过程在这里面它会通过我们看一下，这里面我们可以看到它是去遍历这个 activity master writer，通过找到合适的 activity master writer 那么进行写入。


我们现在已经切入进来，我们可以看一下它这个 writer 内容是什么，当前对应的这个 writer 是一个，我们可以看到它是 encode activation 的writer，那么这样的话接下来就执行我们的一个数据写入的操作，那么我们数据写入操作完成以后，那么整个这个显然就返回出去了，我们整个这个执行流程就完成，现在我们就执行流程进行完成。


那么回到我们的流程可以看到整个这个过程，也就是我们通过我们正常的 HTP 请求获取到对应的 ITP handler，通过 at TTP Web handle Adapter 去转化，把 ITP Handler 转换成 Web Handler。接下来流程就会通过 Dispatcher Handler 去进行处理，它处理的过程跟我们 stream Mac 处理的流程是很相似的，是通过 Handler Mapping 找到 Handler 去进行 invoke handler。在 invoke 的过程中首先只需要通过参数解析出我们这个方法去支持的这些参数，然后调用反射的方式去进行 invoke 执行的结果，我们通过 handle result 去包装起来这个结果最终会通过 handle result handler 这种方式去处理这个结果。在处理结果的过程中，它会借助 HCP master write 这样一个写入器，把它写入到我们的响应题里面，那么整个这个请求流程就执行完成了。关于 spring wireflags 这个源码解析的内容，我们就先介绍到这里，同学们，我们下一节再见。

