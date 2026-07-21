---
title: 6-6 Spring MVC的请求流程（0737）
---

# 6-6 Spring MVC的请求流程（0737）

[image](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/22565ac0-8cd2-45bb-a880-0675fa420abf/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664Z2RPWVP%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T232037Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDPlqjDR94ll7PgE0j65nsTvx%2BtafkmytDHhIFo1XGflgIgU0Y3PHKHK6kRMGg%2BD0%2F4IVnbg4Is7umK3Jo3%2F7r2Si0qiAQIxv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDAhT%2FAWIyOBApDhdpCrcAwQHteogp2BKSq1OOqi8duNhvsC0scIJSo%2Fkqbkfh37qhcLROlMVBI266Zpf%2BZDKEA4%2FKwEz5qi6drNOO%2BuFOSQc8gCBzxa1Bf821QwXSZgmGZR6ydRDwkcoCwr%2FK2zVaxTgiLdv6DMVSH5HegO0e0Dppc3wb0ztqECzYsR8IRYNk28KC6ubgLr2%2BIS5jyw%2F0cgtA1BsqP2ydft3HaAt1V3hw7LQpcv1EHltZDxO%2BQRt%2Bl5OSz5XsFaNREukARDSRbL%2Fw0%2FlOJC%2FUn%2B2Vekxuim4YJyI0FdN4aZfudVbgqaT6xxEL3De1l%2FnFLHxc63nq13GQPIYAuIBUmUk0eL7RUBNao5cziKyeCuC0aJOLREKh%2BBzvVP9UQ%2F4d8RK4pX4ysKihg0lJwIy3F%2FwnwBgzBvWjif%2FIbPG8gEKGGvknh%2FqaTNlOSI6cUm9tK52JDfoGRGsF5IMhnonmddQWJdg%2FHNfCu4WwOCmgyI6GWY4ObQQuOnxW66bXTveGCH3jsIumm%2BwazEEZtmRtWG%2BmSnlpHPT%2B754MdT1Nrm8Y06VWgTv%2BmVh%2BbyTWV%2BpkBE2esoeZvvu9VaiAKPJHrv18Q1yHtg8uA2oTeXUxmlKmUQWnTQJBOHiTDOP%2F9cF7l%2BtMPG6%2F9IGOqUBtVnSLMcmz6Cdw1NCfZw4iHYyi0G%2Bc%2BMKQ52r3xNkrccgMxzcrIm8Yr8TyMTUDSZiFlpaFJZ3FDyNKOr97d8StRxYNFJ8cm5LJX3mzIZ%2BwWX%2BpWhJZtafo%2F5g5TCK2%2FG02CBp8R4lIoWH9b2mN4cUNeZwsLDeWZmSO%2BHjiq6Vo%2FEKRbs0H0yvqrIuCC1VeFWkY9FW%2B0c0nRO5AHkHnOPjFMkVg5vH&X-Amz-Signature=4059763a13703c0465a3fc4ea04d841dd27a29298347f9385802a493430ae3b8&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

[image](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/c60e6f39-a999-4c95-b6e9-6b0da9afc1f1/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664Z2RPWVP%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T232037Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDPlqjDR94ll7PgE0j65nsTvx%2BtafkmytDHhIFo1XGflgIgU0Y3PHKHK6kRMGg%2BD0%2F4IVnbg4Is7umK3Jo3%2F7r2Si0qiAQIxv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDAhT%2FAWIyOBApDhdpCrcAwQHteogp2BKSq1OOqi8duNhvsC0scIJSo%2Fkqbkfh37qhcLROlMVBI266Zpf%2BZDKEA4%2FKwEz5qi6drNOO%2BuFOSQc8gCBzxa1Bf821QwXSZgmGZR6ydRDwkcoCwr%2FK2zVaxTgiLdv6DMVSH5HegO0e0Dppc3wb0ztqECzYsR8IRYNk28KC6ubgLr2%2BIS5jyw%2F0cgtA1BsqP2ydft3HaAt1V3hw7LQpcv1EHltZDxO%2BQRt%2Bl5OSz5XsFaNREukARDSRbL%2Fw0%2FlOJC%2FUn%2B2Vekxuim4YJyI0FdN4aZfudVbgqaT6xxEL3De1l%2FnFLHxc63nq13GQPIYAuIBUmUk0eL7RUBNao5cziKyeCuC0aJOLREKh%2BBzvVP9UQ%2F4d8RK4pX4ysKihg0lJwIy3F%2FwnwBgzBvWjif%2FIbPG8gEKGGvknh%2FqaTNlOSI6cUm9tK52JDfoGRGsF5IMhnonmddQWJdg%2FHNfCu4WwOCmgyI6GWY4ObQQuOnxW66bXTveGCH3jsIumm%2BwazEEZtmRtWG%2BmSnlpHPT%2B754MdT1Nrm8Y06VWgTv%2BmVh%2BbyTWV%2BpkBE2esoeZvvu9VaiAKPJHrv18Q1yHtg8uA2oTeXUxmlKmUQWnTQJBOHiTDOP%2F9cF7l%2BtMPG6%2F9IGOqUBtVnSLMcmz6Cdw1NCfZw4iHYyi0G%2Bc%2BMKQ52r3xNkrccgMxzcrIm8Yr8TyMTUDSZiFlpaFJZ3FDyNKOr97d8StRxYNFJ8cm5LJX3mzIZ%2BwWX%2BpWhJZtafo%2F5g5TCK2%2FG02CBp8R4lIoWH9b2mN4cUNeZwsLDeWZmSO%2BHjiq6Vo%2FEKRbs0H0yvqrIuCC1VeFWkY9FW%2B0c0nRO5AHkHnOPjFMkVg5vH&X-Amz-Signature=4bde7336c4d93c6bbb15c37ca10527301f8732ff25350ea5faca5e0fc275149d&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

同学们大家好，这一章节我们来介绍 string 面试题深度解析之 spring m a seed 请求流程。大家知道对于我们在做加 Web 开发过程中， spring Mac 的过程是非常重要的，因为我们对外提供 LTP 的接露主要还是基于 stream MS 的方式去提供。通常面试官可能会让你介绍一下 SMMS 的请求流程，甚至有面试官他会这样去问，能不能给我介绍一下，我们通过浏览器打出 url 请求到对应 three m v c 提供的 control 这个过程，那么这个可能就已经比本身操作 stream m v seed 知识，它可能会需要你再介绍一下关于网络以及浏览器去解析这样一个过程，那么在这里面我们重点去解释关于 spram AC 的请求流程，那么我们回头来看一下我们smart、 m a C 这些核心主键的一些执行流程。


其次我们在介绍的过程中，我们一定要注意，像 Dispatch Threader，一定要提到 Dispatch Threader 里面它有对应的 handler Mapping， handle Adapter 以及我们这些司徒解析，这几大块不能丢，也就是说我们整个流程是需要这几大块支持的。


在介绍这几大块执行的过程中，我们可以把这些细节适当的去挖得更深一些，比如说我们在请求的过程中，这里面 handler Mapping，那么在 handler Mapping 获取对应值的时候，那么这 Mapping 对应的 key 和 value 我们怎么解释呢？那首先我们对于 Mapping 的 key 是通过我们的请求包装起来的，大家切记我们不要说通过 request get URL 这个 URL 去获取的，我们知道这个 handler Mapping 它映射关系里面可能还会包含对应的我们的 activity master，也就是我们是 get 请求还是 post 请求，以及我们的 media type 信息，我们是接收 JSON 还是接收 XML 或 XML 等等，这都是我们 handler Mapping 的一些参数。那么以及我们对应的value，那 value 我们知道我们通过 Handler Mapping 可以得到一个对应的 Handler experience time，也就是说我们会得到 Handler 的一个执行栈，那么如果说我们没有想起这个 handler 的执行站，那么我如果说我们能说出来对于是一个 Handler Adapter，或者说我们说出来是我们对于 control 的方法的包装，这都可以去解释接受。


那么对于 handle Adapter，我们知道 handle Adapter 就是我们对于 counter 方法的一个包装，那么我们要知道 handle Adapter 它是如何去调用我们对于 control 的方法，我们这样可以理解出来这是我们里面会涉及到了一些反射的操作，去把我们的信息取出来。


那么这里面还有一点就是说我们如何把请求里面的参数转化为我们对应这个 counter 方法的这些请求参数，这个因词关系大家也知道它是利用了我们这里面的对应 it master convert 以及我们的 did 绑定，还有我们这里面可以提到我们的一个参数转化器，参数转化器可以把我们 request 的请求里面的内容转化为我们对应这个方法里面所有的这些参数列表。


那么完成这一步的话，后面其实对于我们视图层的解析的话，我认为其实是不重要，因为视图解析，首先我们现在前后端分离已经很少用后端视图了，其实我们能在这里面把我们的 JSON 序列化的过程中介绍好，其次也就足够了，这是我们大块的内容。如果说有必要的话，我们可以把我们整个跟 discussion Server let 相关的一些核心的一些细节可以介绍一下。首先我们来回顾一下对于 departure THREAD 它初始化的过程，那么当然它并不在我们的执行的过程，也就是说我们请求的过程并不包含初始化，初始化一定在请求之前完成的。那么我们在初始化的过程，我们可以看到对应 dispatch Server net 里面它的 init 方法，它首先会 init servernet being 我们 init Web application context，同时去配置和refresh，就是 config and refresh 我们的 Web apps context。也就是说我们在这里面把 Web Applix context 初始化完成以后，就应该构建我们这个必应容器了。


是构建完 bin 容器以后，它会跟我们这个 Server light context 进行绑定，这样的话会触发一个 application event 这样的操作。在这个过程它会有一个策略的一些初始化，这里面是初始化跟 spram c 相关的一些东西，我们可以看到最重要的也就是init， handler Mapping 以及 handle adapters，还有这里面有 handler exception 与slower。


也就是说我们在 MC 请求过程中发生异常以后，我们这么去处理其他的一些，比如像这些视图解析器以及等等内容，我认为这个其实并不是我们考察的重点，那么这是我们整个 dispatch 识别的初始化的一个过程，那么初始化完成以后真正重要的也就是该接收我们识别 MV seed 请求。


那么在接收我们 MVC 请求的过程中，它的首先的入口也是我们的 d start flight，我们不管它是 get post 或 put delete 这些请求，它都会打到我们对应的 do service 方法，在我们的 do service 方法去进行我们的一些请求，那么首先对于 dispatch try，它会把整个得到的请求，它会把我们关键的这些请求信息去包装起来以后，首先这里面会 police 一个 request handler event，也就是构造这个事件就是把这个事件广播出去。在 do service 里面的话，它会把我们请求里面 trip 的信息进行一个镜像的一个保存，也就是说构建我们一个 Snapshot 的版本，那么当它 Snapmate 处理完成以后，再对这个 Cinema shot 版本进行一个恢复。


在这里面 do dispatcher 也就是我们一个处理的过程，在这个处理的过程中，它首先去进行 get handler，也就是通过我们的 handler mapping 里面去获取到我们的handler，这里面得到的是 handler extra chain，就是我们的执行链，通过这个执行链在找到我们具体的 handle Adapter。


那么在执行 handle Adapter 的过程中，它首先会有一些拦截器 Handler intercept，它会有一个handler，也就是在我们执行 handler 之前，我们可以去构建的一些事项，以及我们真正 handler 去执行我们 control 对应的方法，以及我们的一些后处理，就是我们的 Handler intercept 对应的 apply post handler，也就是我们的 handler 执行完成以后要做什么事情。同时还有一个对应的我们需要 process departure result，就是说对我们的这些处理的一些信息进行一个结果的渲染和分发，那么后面就是我们看 handadapter 来处理的过程。


对于我们 handle Adapter，通常我们的一个实现就是 request mapping， handle Adapter 推它的实现是基于我们 request mapping 这个注解去构建出来的 handler difter，它在 handler 执行的过程中会构建出一个叫 handler Mast，这个 handler Mast 也就是对我们 control 里面的方法的一个包装。在这个 handle mess，它有一个词线，也就是我们在里面的 handler invoke handle mess 的，这里面在执行的过程中，通过 invoke for request 这样一个过程的最终会执行到我们对应的方法。


其实对于我们平常会返回 json 对象序列化的方式，这里面会用到 HTTP message converts 的实现，对于 htmsh 的 convert 这种，它有多种实现，其实我们最关注的也就是 Mapping Jackson to active method convert，也就是可以把我们一个对象转换成一个 json 的一个序列化过程，这个就是我们 spam VC 一个执行的流程。如果说能把这些介绍清楚的话，面试官应该是很满意了。


