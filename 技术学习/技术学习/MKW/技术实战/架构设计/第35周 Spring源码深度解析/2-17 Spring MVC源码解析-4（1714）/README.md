---
title: 2-17 Spring MVC源码解析-4（1714）
---

# 2-17 Spring MVC源码解析-4（1714）

[image](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/dacdeee6-424c-4fec-8653-e1c7a0d4d5d3/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XZWQT6QA%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T232017Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIDipOS1%2FcLxlIWYe3e1Y6u0Cs5rk2p5uJSiY2zIL%2BkRGAiEAsv1uPh3gzJB8TZIAxSXzihynKVOUUpw6w49ru1BpAioqiAQIxv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDML1vLjVRLdbR8lqICrcA6eP%2B5rxJu7PT3r0tlgq4nn0WWMFG8clYz0anY%2FyKc3ZwsbFk6NzBRr4KBx%2B4Gpw0QnZYQgnEn2%2F8hp6OZf9Q6Li0pKNgdni50NKlvQGSAoKLNYGp2GoEnbTwvvOU%2BHe%2BqjHNwCBOG6pdDX2diZoekFa0tvrw%2FqOhE%2FefOJKU4FPhvi2RSo%2F%2Bi%2BSFwnnHxQL%2FNaObPjrHm2P6nDhUDj3sHQhFd0xNhou%2B3h1%2BIgLYE9iS3QtulEUA8ulVP8iq2i46F%2F2eElCKZb%2B7r%2FfrhTQ1RZhAXlODxtAFAiOcmFQhSzat%2FqVRDq9lG%2Fc0rWzUOLHvA36reu9%2FxujmtwHWjy%2BQlxqcmr%2F0FuRC9I2V7lQ3uUCJlU%2FXPahrnQ%2B8CmSFDDaUnmqu%2BtHSOpJQEAnWFhImCVVr3dc4PGRYRASu9%2B5Lkd%2FUZv%2B73hpSD%2BH9Zn8TUgF5%2BOLKd1Td8gYO0LNWagR8%2FDudmJvuhevBSjzE6nHwSQZ4KeDKPg3edDQBF9RcRDJjThtmNkVxOdOU1g0kdRN8BJA6kqotht%2F7MilEkrI%2BSwkLUWrNVU2FbRvfMTWTCjrJ57mgljj1JlmJoScZBBcMwt1680ns7f63VtOApqcwmdhYV1Sk7RIGeHVL2iwMKO4%2F9IGOqUBs5Hz4z3rgacsZh%2F9GQluflrQRgFNcAr1ZnrrzRvbC8DaEgr24bSAqu6yrIEa9F0S13%2FRmprUCQXX4J1KTd6BvtCmN43fUaglLPv4ohPh%2F1AJc0nbVPd0NNmjn7BRHBH1Wdor4%2B3GdleQZu0stQyvpx17oQFeTy52tZqchmf1Aq7OYG7Vl0R739%2FL3jj4S74aIJC7HoVn4iitiElJnFANgCUCUMi%2F&X-Amz-Signature=fe0d109a34f2cda3baa03e8aba254f621c51519917a77fe143ade7b091a45c17&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

这个什么 MVC 执行请求的一些流程？好，我们来看一下 MV seed 请求执行流程。在请求执行流程的时候，我们首先会去进行 discussion THREAD 接收请求的一些预处理，同时来进行 Handler Mapping 去获取一下 Handler Adapter 的信息。最后我们基于 handle Adapter 对于它的一个包装成 Serlight invocable handler Mast 去执行真正的请求的方法。也就是说我们可以大致的去分三个步骤，通过 departure 出来的预处理到通过 Handler Mapping 获取到我们对应的 Handler Adapter 里面，去找到真正的 Handler mess 的一个包装方法，通过这个包装方法的反色去执行我们的 invoke 方法。


好，来我们看一下这个 spring Mac 的执行流程，这里面 m a C 请求的执行流程，它大致是整个我们 spring m a C，它的入口就是 despite Thurat，对于我们的请求，它可能不关心你具体是什么请这里面比如说 do get，读post、读put、读delete，它都会接收到。


接收到完成以后，对于 departure THREAD 接收到这些请求，它做的统一处理，也就是进入到 process request 的方法，也就是说把我所有的请求去统一起来。这个方法里面它要做的事情是间接的去调用了 do service 方法，通过 do service 直接调 do discussion 方法。对于这里面 process request 和读 service 方法，它都做了一些统一的处理，在这里面我们可以看到对于 process request 方法，它会对于我们请求的一些上下文信息去保存起来，这里面的保存方式它其实是放到了所有的 local 里面。当执行完 do space 方法，它会切记去把我们这些上下文信息，再清理掉一些reset，或者说重置一下。当执行完这个以后，它会去 publish 一个 request handler event，也就是说它就会广播出一个事件，如果说谁关心这个过程的话，可以监听这个事件去做一些特殊的处理。


那么这是 process request project where，它下面是 do service，其实 do service 也是注了一些类似于这样一个统一处理，但是它处理的内容是局限在 request 对应的attribute，也就是说我们的请求属性上的一些内容，它首先会把我们这些所有请求的参数进行一个包装，去判断一下我们在执行 MC 之前，它的 request 对应的 attribute 里面的内容是什么。执行完 do dispatchers right，他就会把我们这些 tribute 信息重新restore，也就是重置一下，也是类似于重置真正的一些业务操作，就在 do dispatcher， Dispatcher 说他著的内容是首先去获得一下 get handler，这个 get handler 得到的内容是一个 handler excuse？也就是 handler 的一个执行链，这个执行链里面去包含我们真正的 Handler Adapter 和我们的拦截器的一个组合，那么我们通过这个执行链去获取到 handle Adapter，对于在这里面获取到的这个 handle Adapter，它就开始执行它的一些业务操作。


一些预处理首先会执行对于我们拦截器的 pray handler，也就是在 handler 执行之前的一些预处理。执行完 Pre handler 的话，就开始执行我们的 handler type 对应的handler，其实这个操作的过程就是会间接的去执行到我们 control 对应的方法。这个操作执行完成以后，因为这里面比较复杂，我们接下来后面还有一页去介绍一下 handle 的处理过程。这个处理完成以后，他就开始执行对应的 apply post handler，也就是这是 Pre post，是对应的一个关系，也就是说这是前处理，这是后处理。它做这些后处理的套路也就是包含一些内容，比如说我们自己实现的一些逻辑，假如说这里面是 Pre handler，它如果返回一个 false 的话，就没有这个执行 handler 的过程了。


这个大家知道拦截器的执行业务流程，执行完这个 post handler 以后，应该就要去处理这个 dispatter resource，也就是说真正的去处理我们这个 control 的返回内容的这个结果集的一些处理。但是这里面处理的话，我们可以看到如果说它pros，它可能是如果抛异常了，通过异常的处理其他情况，它需要render。如果说返回了 model 的view，它就会对 model 的 view 里面的 view 解析出来，进行我们的一些数据的渲染。


如果说我们返回的是 json 的话，整个这个过程是执行不到的，这里面是 render 完成以后，我们最终会有一个 handle in the chat，也就是我们的拦截器有一个 off 的completion，也就是说整个我们拦截器执行完成以后去做的一个回调，这是我们可以看到整个 Mac 请求流程执行的比较大块的一个内容。


那么我们看一下对于这个 handler 里面他要做的事情是什么呢？对于这个 Handler Adapter，他在做 Handler 之前，其实这里面我们重点关注的是基于 request Mapping handle Adapter 的实现，如果其他的一些 handle Adapter 实现，它的逻辑可能是不一样的，因为我们基于注解的 handler Demo 主要是 request Mapping Handler Adapter，我们所有的这里面讲的内容主要是基于这个 s 线，那么胎儿住的事情通过 handler 方法去调用 handler international 一个内部的实现，最终是通过 invoke handler mess 的 pass 去执行。那么这个 invoke handler mess 的就会回归到我们刚才介绍的 Sernet invocable handler method，也就是我们通过这个 handle method 的包装去执行在执行的过程中他会做的事情。


我们可以从这里面看到通过 invoke and handler 去做的事是，首先它这里面会做的一些操作是 invoke for request，它会通过一个 handler mess 的 argument resolve，也就是它去解析我们的参数，解析完参数以后进行 do invoke 执行完 invoke 以后会 handler written value，也就是说 doing voke 它会返回值，它的响应值会通过我们的 model and view mass 的 return value handler 去进行处理。那么在这里面这个 handle value 它主要的一些处理逻辑。这里面更关心的也就是 request response body mass the purpose，也就是如果说我们通过的是 response body 这样注解修辞了，它会通过这种方式去对我们的 return value 进行处理，这个处理完成以后，它不会返回 model 的view，它处理的逻辑就是通过 it message convert 进行一些我们数据的渲染。


一般的流程是通过 it master convert 它的一个实现，也就是 Mapping Jackson two item master convert 进行处理，并且把它得到的对象渲染到 response 对象里面，通过 red stream 的方式把我们这些数据流渲染出去，这可以理解为我们整个 4 转 MVC 执行的这个流程的一个简化版。接下来我们通过源码去分析一下它执行的过程。
好，我们看这里面我们已经通过请求把断点打到我们对应的这个读 get 方法，也就是说我们刷新的一个 get 请求，我们可以看到通过 STB 和 local house 的 8080 这样一个demo， get by name 这样一个操作进入到我们的 departure service 请求。好，这样的话它现在我们要注的就是通过 process request 的方法去执行。通过读 get 方式到我们的 process request 方法，我们先来跟进去，在这里面我们可以看到 process request 的方法，他去做的一些事情，这里面我们看到它是获取的一些 local context 的，它这里面获取的方法我们可以跟进来看一下。这里面主要是通过一个对应的 THREAD local 的实现，从 get 的方法去构造。好其他的，我们就几个实现的类似相关的，我们就跳过。在这里面我们看现在是需要隐匿的 contact HOLDER，也就是说把我们请求相关的一些塞下文状态去保存起来。


好，接下来我们看 do service 的操作， do service 操作首先他会去打印一些日志信息，这个我们先不关心，我们看接下来他会去做一些跟 attribute 相关的一些内容，首先他会把跟我们 three VC 三亚文相关的一些信息保存到这个 request 的对应的 tribute 的这个属性里面，同时它在执行完成以后会再清理掉。好，我们看这里面设置一些信息，接下来应该去执行 do dispatch throughout，那么 do discussion，我们看一下他处理的事情，在这里面就开始去做我们真正的一些业务处理了。我们现在在这里面去首先判断它的是不是文件上传的相关的一些操作。好在这里面我们可以看到它去开始获得我们的 get handler，看一下这个 Mapper handler 它的类型，这里面对的类型是 handler execution chain，也就是我们的执行链，我们通过这里面的 request 获取到我们的执行链，那么我们看一下它获取的过程是怎么获取的，在这里面它获取的过程是通过 handler Mapping 去循环找对应匹配的内容，可以看一下在这里面它获取到第一帧获取到就把当前的这个 handler Excel 称返回出来。


接下来去看一下，如果说我们这个 map handler，它如果等于 null 的话，就会返回类似于 404 的一个超准，当然我们这里面已经获取到了，它是正常执行，在这里面它会通过这里面的 map handler 获取到我们真正的 handle 的操作。


我们看一下它执行的过程，在这里面也就是通过 handle type 的做一个类似于我们的是否支持一个校验，如果支持的话把它返回过来，也是返回到这里面，我们再看它会经过判断一下我们请求的方法类型，这里面如果是对于特殊的方法做一些处理，比如说 get head 的话，去判断直接返回它对应的，比如说它的一些最后修改时间就可以。


好，我们现在它应该要注的其实就是 play Pre handler，也就是需要对我们这些拦截器的一个前处理。对于拦截器的前处理的话，如果说他前处理的结果是失败的，也就是false，那么它就直接 return 整个后面的流程不执行了。我们具体的执行过程我们可以看一下，它在这里面其实还是调用了我们构建的是拦截器这个拦截器链，但是我们并没有主动去创建这个拦截链，这是它系统默认提供的两个，那么我们直接跳过就行。好，它返回结果是true，那么 true 的话它会直接还会执行对应的 SA 的 handle Adapter，我们可以看到这里面真正的去执行了，我去执行我们的handler，那么我们跟进去看一下，这也是我们比较关心的内容。


在这个 handler 我们还是接着跟进去，我们可以看到他现在要做的事情，还是一些代理的操作，我们还是接着方法去跟进去。我们可以看到在这里面的话，它就是代码的逻辑相对来说就比较复杂了，我们可以看到在这里面当前我们是在 request Mapping， handler adapt 这个类里面去执行的，在执行它的过程中，我们看在这里面要构建出一个 thrift invocable handle mess 的，跟我们这里面讲的内容是对应上来，首先它是在对应我们的 request mapping handler Adapter 里面去执行，同时构建出这样一个 handle mess 的。


接下来他构建出这个 handler Mesh 的以后，他去判断一下我们当前的这个参数解析器，如果不为 now 的话，把参数解析器设置进来，同时把我们的 return value handler，把我们的返回值的处理器，也就是如果不文档也设计进来，这样的话接下来去设置，比如说一个数数据绑定器。


好，这里面还有一些参数命名的一些发现的相关的一些内容。好，我们接着进行考，这是相关的一些属性内容，我们接下来看到它在里面去真正的执行 Emock and handler，那么我们跟进来看一下，它在执行的时候，我们接着去跟进来 Emock for request 这里面我们看到它会通过我们的请求和我们判断一些参数信息，它会解析出我们的参数出来。在这里面因为我们这个操作它没有参数，所以说其实我们就不关心它解析的内容是什么了。


好，接下来我们再继续跟进去，这是执行我们的 do invoke 方法，好获取相关的一些操作，我们看在这里面去设置一下它的可读性，我们到这里面就是真正的去执行我们的超准，那么我们点进去就会到我们 control 的方法里面了。还有一层，这个层次还是比较深的，是在这一层我们去点进去，好执行我们的回调方法。


好，终于到了我们写的 control 的方法里面，在这里面我们的参数 test 已经获取到了执行我们的操作，那么我们返回的内容是什么呢？我们返回的内容是一个 user 对象，但是我们这里面用的是 rest control，其实相当于是我们这里面已经被 response body 羞涩过来，所以说我们这个 model 它最后会渲染为 Jason 的boss，去渲染到我们的响应对象里面。


好，这样我们得到了 return value 返回值，现在去对我们这个想要的状态去做一个设置，我们当前的状态为null，它就会返回位，也就是说并没有去对状态去做什么处理。如果说它状态已经有返回内容的话，这里面就会有一个错误的结果，这里面去看那一下我们当前的 response 状态的一些校验，现在是对我们这些返回值去进行处理，对返回值的一些处理是相对比较特殊的，这里面的逻辑也比较复杂，我们可以跟进来看一下。他首先去会选择一下我们当前这个对象是支持的这些反馈值的想象内容。这里面获取到的一个 handler 就是 request response body match the process，也就是说它去因为基于 response body 去修辞了，所以用这种方式去处理它的处理方式。


我们可以看一下通过 handler return value 注的一些操作是什么呢？这里面会创建 input message 和 output message，最终是通过一些转化的方式把它写入进去，我们可以看一下它是 write with master convert，也就是说把我们的信息通过 active message 的方式去转化出去，这里面就开始去把我们这些信息通过 input message 写入到我们的 output message，你可以看到这里面是我们的 output message，其实构建出来是一个 THREAD Server 的 it response 对象，这个 response 对象它就可以直接去把内容我们渲染出去。


好，我们进入下个节点，在这里面我们可以看到这个 generic convert，它是一个什么对象？这里面的 generic convert 它其实就是 Mapping Jackson two active master convert，也就是这样一个消息，一个转换器把我们的数据转换出去了，那么好，这样的话我们就执行，他就去完成了我们数据的一些写入。


好，我们跳过这里面去真正的去执行我们数据的操作，去把我们的当前这个对象，我们可以看到是 action two s master convert 去写入到我们的渲染，我们的响应请求里面，我们看一下现在的话，整个执行完成它会去获取一下我们的 model 的view。


当然我们知道因为当前使用的是 Jason 渲染的方式，所以说这个 model 的 view 他返回的内容是一个now，那么我们接下来看一下这里面返回以处理完成以后，我们看一下他会去处理一下 departure result 相关的内容，在这里面我们会判断他如果说返回的内容，如果说有异常的话，去做一些异常的一些处理，如果说没有异常，那么我们去接下来看一下他要做的事情是判断一下我们的 model view 是否存在。


那么 model 的 view 我们当前也是不存在的，如果是存在的话，它会调用 render 去渲染，如果不存在也就跳转出去。好，接下来它最后会去判断一下 map handler 的是否存在，当然这个是存在的，我们会执行一下拦截器的后处理，也就是说我们执行完成的一些操作，这里面是通过连接器去做 of the completion 相关的一些操作。好，这样的话整个我们的请求就已经执行完成了，接下来要做的事情就相当于是回退到我们的执行调用链里面去，把我们这些因为 SPRAM AC 去修改的这些赛尔变量，它进行重新的一些恢复好，我们可以看到这里面是执行，指 set contact holder 把一些请求去重新处理一下，同时我们记录一些 resort 信息，这里面广播出去。


我们的 request handler event 跟我们这里面的请求内容是对应着的，它是执行完成以后，同时把我们的信息在这里面。 publish request handler event 就是把我们那个请求的事件的广播出去。好，我们继续在这里面，我们可以看到它已经回到了读 get 方法，整个我们的执行流程也就执行完成了。这样的话我们整个 spring Mac 的执行流程就介绍完成了。大家通过这个课程的学习，相信对于 spring Mac 的初始化过程和它的请求执行流程都应该是比较清晰了，也希望大家通过在关键点添加断点的方式，通过断点 debug 的方式去了解一下源码的执行过程，这样会更有利于大家对于这个执行过程的理解。好，今天的课程就先介绍到这里，谢谢大家。

