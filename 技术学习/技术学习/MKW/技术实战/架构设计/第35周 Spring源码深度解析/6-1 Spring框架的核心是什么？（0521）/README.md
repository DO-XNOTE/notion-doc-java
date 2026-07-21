---
title: 6-1 Spring框架的核心是什么？（0521）
---

# 6-1 Spring框架的核心是什么？（0521）

[image](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/e2b1f9a7-454c-4616-9cc1-5c3b874b9dc3/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UJDAFMMW%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T232034Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDhsHFQHOiEXHREhr41JubdL8%2BiphPuelUxDXWKuc2kmAIhAJREZnRTJdit3rqX5%2FApSViFt%2FftcJ%2FKw1Mz3Fqr9lHGKogECMb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgzxiiEFHlmAGyErW18q3ANkByrTRk9kxE9ZpiVd2viKSCFI4kjITk8E1%2FoSOH%2BXjgQUGmGy0LptNYLq0a0yDhKs08NaKwyoTZtuL16Ctjf7XMZPPGMFBGD%2Bd3FUvnnfTI%2FEEanfsO16NeMzk5v2e51wgaDnVrC%2BSFsRK5%2FvqFGyAJxSRZ0OYGGy6ShQoO9i9ilaAkR03%2B%2BPsxLcG3NJQEn98odMQlareFoJnlMiycWmdMGu0Qz%2BIoDB2dj5%2BA0S%2BI8xYpfwZYq%2FspDl5N2uk%2BZI7g6xu%2BRL3UF9m45W%2FVNrohi0AS830nKKiJwIYgjUS09rKJ1cIR9l%2F4lOA8cLGON7Fg4ROTGCLlI6AI53ysYnON3Rc1Q2C2tDbUUxY9lHkiTysgX5OSPda6JNT0MqpxvgM4AgnQpnXo%2Bt%2Bz%2FxUYyEE2tBJSh4f9Ahp%2Bp6fGGLlLgbEtVy2r4a3C9AxLDCPpYK9Gf6XEVi08VVjG%2BtezXrozCJz92ZTBKQhR1bNwvAJtcCpDa9cS72ydZolHB1nkIEpeZ8C0BtAT4j3zfobrU2Ok6pjyxocAipwDr%2BZJu7%2FSoJKvlyQDHSGik4x0mbED411gsKaJhRkBOlMsbhEXPll3O7D9AdmchFE3sBq93TkDju5x6lMliZnifVYTCLuP%2FSBjqkASnetTc11TpWqfJ6wMJyM2pRHb18Nx8zzv26HqbdA9mQFWHAhyyeR3Gg3FZYAAygWx0zllEhNYf%2F%2FQsDOzDUdy8QNNll%2FTKHT0xsHg9eQmBuNVeBA2TXof%2B3yrZGnHYR7Pdw%2FUQhIyhZnL%2FiDkWkTS6bK0MD6oixn27Try2vgHBoG%2FNsxblFiaPwkQ07USAO0g7cQk5Rp9MTRxmlUmJoZkFE7u6y&X-Amz-Signature=b85b8eb1ef4ca8dc2be361bb8ae0d315d5ccaed5a2f0485f3d4822e1a7f9dace&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

同学们大家好，这章节我们来介绍 spring 的面试题深度解析，就是 spring 框架的核心是什么。这是 spring 问题的一个高频的中奖题目，回答这个问题基本不会冷场，有过开发经验的同学都可以巴拉巴拉说很多，这也是 spring 系列问题引入的一个铺垫问题。


那么在这里面我们要对这个问题进行一个条理化分析，面对 spring 框架的核心，我们应该如何回答？它既能展示自己对 spring 框架深入的了解，也能通过这种技术的了解去打动面试官。首先我们要对 spring 框架有哪些模块做一个简单的介绍，体现出我们对 spring 框架的整体理解，然后介绍一下各个模块之间的依赖关系，通过模块儿之间的依赖关系可以分析出每个模块儿依赖最多的是什么，这样我们就可以得出 spring 的核心框架，也就是 spring 的 IOC 容器。顺便的引申一下 string 的发展历史，体现出自己对技术八卦的热爱，给面试官树立起你对这种技术框架专研的能力。


那么我们来首先回顾一下 spin 框架的核心模块，在这里我们可以看到这个 spring framework 整体的它的基本框架，它是由 spring 的 LC 容器， spring LC 容器涉及到哪些模块？它 spring LC 容器最重要的就是 spring beans，那么 spring beans 它是依赖的 spring core，那么基于 spring bean 和 spring core，它就可以构建出我们整个 spring 的核心容器，那么我们知道 spring 的核心容器它只是实现了 Bing 的构建和 Bing 的注册。


那么如果说我们希望基于注解，或者说等等，像四件驱动等等这些事件的话，我们就需要一个 context 模块，在这里面 context 模块它跟我们构建出来 application context 这个对象，它里面有对应 XR 的实现和我们注解的实现。


基于这些就是我们更丰富了我们的 spring 容器里面的一些功能，那么这是 spring 的容器功能，那么在上面我们知道我们还有 spring 的 AOP 功能， spring AOP 功能它通过代理的方式构建出一个新的对象来满足一下我们。对于这些模块统一入口的野封装，我们通常会在权限和日志的上面使用 AOP 的功能去实现。


在 spring AOP 上面是我们的 spring 对于数据抄入的一些封装，这里面它对 GDBC 和对于 IM 两种方式进行了封装。同时在这里面 spring 做的最大的一个事情是对于我们各种数据访问的这些组件进行了事务的抽象，这里面事物抽象包括GDB，seed， transact manager 和 OM 对应的 transc manager。同时像 mybatting 这种第三方主键接入的过程中，它也通过实现了 transegment manager 的方式去来完成 45 的管理。


那么这里面的 transegment manager 45 管理，我们可以基于这样一个注解进行森明词注解，其实这个森明词注解它是利用了 AUP 的能力来实现这个功能的我们查看这一块跟 spring Web 相关的内容， spring Web 相关的内容最重要的就是 spring Web i m a C。那么同时在 spring 5. 0 以后，我们开发了新的一个 spring Web flags，支持异步的方式去请求这些网络的一些数据。那么在 Web Mac 和 Web Flex，他们同时依赖了 string Web 模块，对于这些 Web 请求的一些封装做了一些统一的一些处理。通过这里面我们可以看到对于这些大的模块，有 spring day 的 spring Web Mac 以及AOP，这里面是我们的核心容器以及作为整个基础的我们的单元测试组件，那么我们可以看到 AOP 依赖了我们的核心容器。


5，它同时又依赖了LP，那么间接的也会依赖到我们的核心容器。这里面的 Web IC 和 y Flex，它们在构建所有必应组件的过程中都会依赖到我们的核心容器。从这里面去看的话， spring 框架的核心是什么呢？它就是我们的 LC 容器，那么 LC 容器里面会涉及到哪些模块儿？我们可以去介绍。


像 spring beans， spring cores， spring context，这里面还有一个模块儿就是expression，也就是我们构建 SPRER 表达式的这个实现模块儿，它可以在我们在定义我们的属性文件或我们注解依赖的过程中使用，通过表达式来表达我们的一个文本字符串的内容。


通过这样的去解释的话，我们可以看到整个我们 string 框架里面包含了这些内容，当然如果说大家可以去引申一下，像 string Boost 内容也会对整个问题是加分的，所以说当回答这个问题的时候，我们不要简单的去说一句始终的核心就是 LC 容器，那么没有了。


那么其实面试官对于这个问题来说，它并不是说想知道，你对于这个的总结就是一个 spring LC 容器，它更想知道的是你对整个 spring 框架这些各个模块的了解，通常你对这个模块的介绍越详细，那么面试官他对你的认可度会越高。很多面试官喜欢听候选人滔滔不绝地讲述自己的理解，也有一些面词观它会意识到你对这块内容了解比较好，会跟你进行一个更深入的交流，这也是加分项。那么有一点要注意的是，回答问题千万不要一问一答，这样会很被动，面试官说了很长一段话，你就一句 yes or no，这样是不对的，你要能适当的去引导面试官的思路，在你最熟悉的领域去多做一些交流。好了，这一节我们先介绍到这里，同学们，我们下一节再见。

