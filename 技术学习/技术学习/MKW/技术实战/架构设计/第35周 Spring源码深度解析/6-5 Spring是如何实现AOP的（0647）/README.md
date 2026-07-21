---
title: 6-5 Spring是如何实现AOP的（0647）
---

# 6-5 Spring是如何实现AOP的（0647）

[image](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/fc291381-b1b3-49fd-8184-7b465a76a4e5/SCR-20240804-bnwk.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46637HZRVQJ%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T232037Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIAxRMWwRFD2YBb1SK7XkJcJ0UOMsNWGJR8iARV%2FCrI74AiEAqOGk6Fhx3a1O2Q4j1UyenvniXl1nYY0%2BpDlhUNb%2FdlkqiAQIxv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDECRYPk1H4089WGSKyrcA5JFOt0E7Av6Ke7mGr9%2B667t8%2FUvxrMH32v8%2B%2F0LQYeyd3D8kNGzm%2BL4jPp52NwpTegf2ArUmK1qwBhzMliFnHNwHGoy7g8%2FuL%2FocB5ziH1GO66WvP6PrDkdZTJxqFzxcE83L0fsHB8x67h5gKsylP1Y7wCzjERWG8HDQus4r2LCl%2BfsKE6KG2SBGZ8UhuNoCvP7j1fkWBLs%2BF43MUXXyOq0exRF6TmKB9ggeGMBgo0fwThuQyg0fuSVzNMmGDv0OJ7fj9UegxXvSoaMmvJWKP9cY4L0pp3JuCoeMeP21i9hJqgk%2B%2FGybf9QtY3wKOie4iSfMrxMttrk5gdZiWETOr9akY42vYQZnY9fkGHs4XTdAG1O5qGbB7grzxmq9H9%2BJw5iH%2F2vjwF09akiO8vlaDBsO7mB0mgutw5gw29dYqHJA7eBY%2B5QhiDDHTVmTxEYDcl5ACfGbNJ7fpWYeGnKukSucj%2Bbg%2Bm9uyPGi0KYaqhFoJhkSQSdDoLJDSO1nfT3JDpgKdHdf5BvLIG179IMDlGPKD3sjsT87S10F2q6xslk87%2BYr7ERRvotabEep60g9c5HOMkO3IbWx%2BMhjCOUg9xPx1lqcLKkh%2BTHGP9N3KOqQh8o%2BA8UlYS8F1R1MJm3%2F9IGOqUBjK28nI131E732YlHZ10vanOLvde42BTWOuUEluz1VTkWbI0EvhIIUpxEKyrzQQllTvDpprU8kqC4jQA%2FJstoMURP846FTWczVjy1IHtfJH%2BOlIyk1Bd%2Bow20QioZc60fIKzeTV%2BgJroEkmG%2F2gC7hZ20LdgEelrSkRTXdrb6ipWCdYSztvwKxQevZt7puhyzvxV3yz8JK%2FayD0%2FEwhY7PONjTrHt&X-Amz-Signature=61b4f225a9f94403f23eebc4575437e94894c409ddd07d1b06ff63054bdae5d9&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

[image](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/584043d3-4206-465f-bbe7-72e31cf61b9d/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46637HZRVQJ%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T232037Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIAxRMWwRFD2YBb1SK7XkJcJ0UOMsNWGJR8iARV%2FCrI74AiEAqOGk6Fhx3a1O2Q4j1UyenvniXl1nYY0%2BpDlhUNb%2FdlkqiAQIxv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDECRYPk1H4089WGSKyrcA5JFOt0E7Av6Ke7mGr9%2B667t8%2FUvxrMH32v8%2B%2F0LQYeyd3D8kNGzm%2BL4jPp52NwpTegf2ArUmK1qwBhzMliFnHNwHGoy7g8%2FuL%2FocB5ziH1GO66WvP6PrDkdZTJxqFzxcE83L0fsHB8x67h5gKsylP1Y7wCzjERWG8HDQus4r2LCl%2BfsKE6KG2SBGZ8UhuNoCvP7j1fkWBLs%2BF43MUXXyOq0exRF6TmKB9ggeGMBgo0fwThuQyg0fuSVzNMmGDv0OJ7fj9UegxXvSoaMmvJWKP9cY4L0pp3JuCoeMeP21i9hJqgk%2B%2FGybf9QtY3wKOie4iSfMrxMttrk5gdZiWETOr9akY42vYQZnY9fkGHs4XTdAG1O5qGbB7grzxmq9H9%2BJw5iH%2F2vjwF09akiO8vlaDBsO7mB0mgutw5gw29dYqHJA7eBY%2B5QhiDDHTVmTxEYDcl5ACfGbNJ7fpWYeGnKukSucj%2Bbg%2Bm9uyPGi0KYaqhFoJhkSQSdDoLJDSO1nfT3JDpgKdHdf5BvLIG179IMDlGPKD3sjsT87S10F2q6xslk87%2BYr7ERRvotabEep60g9c5HOMkO3IbWx%2BMhjCOUg9xPx1lqcLKkh%2BTHGP9N3KOqQh8o%2BA8UlYS8F1R1MJm3%2F9IGOqUBjK28nI131E732YlHZ10vanOLvde42BTWOuUEluz1VTkWbI0EvhIIUpxEKyrzQQllTvDpprU8kqC4jQA%2FJstoMURP846FTWczVjy1IHtfJH%2BOlIyk1Bd%2Bow20QioZc60fIKzeTV%2BgJroEkmG%2F2gC7hZ20LdgEelrSkRTXdrb6ipWCdYSztvwKxQevZt7puhyzvxV3yz8JK%2FayD0%2FEwhY7PONjTrHt&X-Amz-Signature=319917ff0f6d5d854016475f1e526912c714703e97708b3148ff17ba8bf970cf&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

同学们大家好，这一章节我们来介绍一下 spring 面试题深度解析，那么 spring 是如何实现 AOP 的？如果说要问 spring 是如何实现AOP，那么前提就是说面试官已经知道你是已经理解 AOP 是一个什么样的概念了，那么说我们知道 AOP 关键的几个概念点，那么我们来去介绍一下 spring AOPT 如何实现的。


这里面我们先看一下 spring AOP 之间的一些实现的原理图。首先 spring 和 AOP 之间的关系以及 AOP 与我们的当前代码b， n 的关系是怎样的，我们可以这样去理解，首先我们这是我们的 talk 的宾语，就是说我们自己写的代码，我们这个代码是比如说它是一个 DO 层，那么作为 DO 层的代码，它需要被我们的设备层调用。那么在这里面 survey 层就是 D o 层对应调用的一个客户端，那么在调用的过程中，我们并没有直接去 new 出这个 D o 去调用。我们是通过 spring 委托管理的。在 stream 委托管理的过程中，我们做的事情是什么？对于 DOA 的操作，我们通常是需要事务的，我们知道我们的事务处理是不用的，声明式事务处理是通过 AOP 来实现的，那么在这个生命词事物处理的过程中，它通常是需要我们指定一层代理。


也就是说我们在 service 层调的 d o 的对象并不是真正的 d o 对象，是 spring AOP，它跟我们生成的一个代理对象，这一层 AOP 的代理它实现的功能主要是对于我们事物的包装，那么这样的话我们就理解了 spring 框架在 AOP 实现层面上做的事情。


在这里面首先我们需要指定 advice 和 point cat advice，它说明了我们需要做哪些增强。那么我们看来知道在这个场景下，我们假设它是对于我们的 d o 做了一个四五包装的增强，那么这里面有 palm cut，也就是我们指定在什么地方争抢，那么我们就理解为所有对于我们 D o 的实现，我们需要去进行拦截，进行对于我们这个 BN 的封装。


那么在这里面我们通过我们指定的 talk 的 bin 以及指定我们的 advice 增强的方式，就是对于我们事物注解的一些支持，那么在这里面我们通过这块内容和我们的目标 bin 构建成我们的一个代理bin，其实真正我们的 service 层，比如调 DO 层调的其实是我们生成的代理的一个过程，那么这样的话大家就理解了我们这个 AOP 实现的一个原理的过程，那么这是我们通常使用四物代理的方法。


另一种方式，假如说我们需要对于这个包装的病句打印日志或打印什么内容，那对于我们来改动的内容是什么？其实我们要改动的内容只是我们 advise 的内容，也就是说我们去扩展增强的一些区别。我们来看一下一段简单 AOP 的一些实现过程，在这里面你要跟面试官介绍的过程中会介绍到我如果说实现 AOP 的话，我会怎么实现？那么一般我们现在是通过声明式 u p 实现。


首先我们会定义一个对应的 aspect 类，这个类一定要切记，我们需要用 aspect 的这样一个注解去修辞，就用它来标明我们当前这个类是为了去做 AOP 的一个配置。在这个类里面通常我们会有一个pandecat，我们指定一下执行我们这个对应的表达式，也就是说我们这些方法里面去执行我们对应的一些扩展操作。当然这里面有一个默认的语义就属于一个公共的方法，这里面我们实现了我们的 point cut 的配置以后，我们还需要去配置我们的advice，对于 advice 我们通过 round 这种方式去标明一下我们扩展的内容，这里面我们会对于我们执行的方法去进行一个日志的打印，在这里面我们打印出我们执行的时间，从这里面我们可以看到这是对应的 pond cat，这是我们一个 around 类型的advice，那么它们的组合就构成了我们 AOP 的一些重要的关键点。


完成这个配置以后，我们接下来去看一下 AOP 的一些代理的实现原理，其实我们在这里面可能会被深入的去引导，问入 AOP 的代理是怎么实现的？ AOPT 的代理实现方式有两种，一个是加 r 动态代理，一个是 CD live 代理，这里面我们需要去介绍出来加动态代理和 CLM 代理它们的适用场景的区别，以及在什么时机去选择对应的不同代理的方式。


这里面我们要注意到对于加滑动态代理，它的要求就是我们这个 b 必须有对应的接口的实现，那么 CD Lib 代理动态代理它的要求就相对简单一些，它并不要求我们去实现接口，但是因为我们知道 Java 动态代理是基于接口实现，那么 CD Lib 动态代理是实现基于我们当前 bin 构建一个子类来实现，那么构建子类的条件就需要约定一下，我们当前这个 bin 它不能是 final 类型的，那么如果是 final 类型它是不能去生成我们对应的动态代理的。


介绍完这些区别以后，我们可以再基于注解对于代理的实现方式，它比如说初始化的一些流程，我们来注再介绍一下，那么就对于我们 AOP 的实现原理的方式可以跟面试官更好的介绍，那么我们可以看一下，我们来回顾一下对于注解 send COPT 的注解流程。


首先我们需要对于我们的加 configure b 需要配置一下 enable aspect 接 auto process，就是说我们首先去声明自动 aspect 的一个代理的生成，那么这里面会涉及到两个操作，一个是 import bin decline register 和我们的 aspect 接 auto perfect register，也就是说对于我们这些自动代理实现 bin 的一些注册，这里面比较重要的一点就是说通过notation，where， aspect 这些 autopractice 它要处理的事情就是这里面我们有一个对应的是 being post process 的实现，它注的事情就是进行 post process before insolation 这里面注的事情也就是说它通过 being post process 对于我们所有这些 being defensive 进行一些处理。他处理的逻辑就是去判断一下当前这个类里面有没有扫描作为 AOP 的一个词线。如果说我们扫描到了这个类需要进行 AOP 的包装，那么它需要对于这种情况下去生成我们对 0 的代理实现。那么这里面其实有一些实现的过程，它首先会去加载一下工厂里面去有 aspect 一些注释的这些bin，构建出这个 Advisor 列表，我们知道我们通过对应的 aspect 里面这个类的实现可以找到 point cat，也就是说可以找到它所有扫描的这些类，那么通过这些扫描的这些类来去指示一下我们对应哪些b，应该去构建我们的代理类。


关于这些 AOB 的实现原理，大家介绍到这里面，基本上对于 AOP 的原理已经给面试官介绍清楚了，那么这时候如果说面试官还有哪些地方更感兴趣的话，他会引导的去问，比如说在实现 AOP 的过程中，为什么在同一个类里面从 a 方法调 b 方法，那么 b 方面的 AOP 没有生效？这样的一些立体大家应该也会回答，因为它是在同样一个类内部调用，那么类内部调用并没有经过我们代理对象的实现，所以说我们一般情况下 AOP 内部调用它的 AOP 功能是不生效的。好同学们，我们这一节就先介绍到这里，我们下一节再见。


