---
title: 6-4 BeanFactory和ApplicationContext的关系详解（0455）
---

# 6-4 BeanFactory和ApplicationContext的关系详解（0455）

[image](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/fa5df62d-501d-45a6-857b-f61546583926/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SCWIUEQ6%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T232036Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCe3X%2B4n43WywQUIxA%2BtJORu4Z1M2KBEjsYKPxbA04DOAIhAMdfZfRixGcnVZ0wpSs0mAJFBU7oiEEcykWAS1oJNtLpKogECMb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgzqyX%2FYXYfK%2BM08A%2B0q3ANDoIrJu2jCt0rjlWvN79bcVumVPMl2kKNrn6ZOGaBXjv7YiYyBBRASHwDasU16oYLXS4yVLMF4RmM5pFMclpThOcf25mGNtHC74zO8WT90oDeNyO2VES57Ofk%2Fq3iYhkgIP8Z7CofbJlxe%2BcTfgMV8vig7PhEPM6HDsAqSM5LWqRVV%2F3eX6YqGu7t397sdh5I6PSszqXBjoNnHKPMXLebkdQZfWhgZ3U5%2Byu2YH9V0piePMuk1j3r%2FR9DAyWsZffoos4IRnO4Alk4IklbuFLG17L7VuLRIl5Mnv6WkRHDCLcg6z3eyhW%2F6xBcFhn%2BbLPjF%2FlrGZDd29tOiuNJEhLfoHU%2BtC2zCtYFN7f1%2BBxq3z%2FuuRi3P6sCkjp0xviXvr%2Bf068zdIxisCoLHHh1eQwouQUwAQ7YsJqJNTW%2B2GzYEjNe4RzBM%2FZpCf0Fwgioz28xOwNOpGTruKt%2B1kIQ1Fageoz3W7r6tIz37j019zyvoX1PQsU5%2BZw1uCyR0MrR0ExXoFgeudEjd82n5ty7QSZGhUtsH%2FHeuQ0gDRHsRm8gktnXmfA7c5AX9gJIbzHYKSaUY6CBwI2XpzXoohLCu1%2BNDJIE8%2BvDIt7PGhP2lveJwqOoDrs2UWCwms2ldiTCjuP%2FSBjqkAQ4htCWEpLsghie3QqbIvX70DQWu6T%2FDGnHrc%2B0lA7lKqDWgFTw6m7MOtMyAt%2B6rfUhLaqpz53l%2BhXfmxM6Q6tvixGuSESKwnGyQvaRyEaItlgA9ug66usg5AcxIDtL%2FEItLaOZ8aKlkSqH56vzuiUSmRRRuNHRabV0%2BDg91HZHBGnn%2F4Z%2FhYG3DQm540f9UYcdzLN5vXsbDHiEEPTDfDBlcoOW1&X-Amz-Signature=b1690bd2303c7d60d756ec3cb6ce207366b453e50653b2e928228823df5e72d1&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

[image](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/80020b97-5628-4640-9c8a-7c8eb946e992/SCR-20240804-btnj.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SCWIUEQ6%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T232036Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCe3X%2B4n43WywQUIxA%2BtJORu4Z1M2KBEjsYKPxbA04DOAIhAMdfZfRixGcnVZ0wpSs0mAJFBU7oiEEcykWAS1oJNtLpKogECMb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgzqyX%2FYXYfK%2BM08A%2B0q3ANDoIrJu2jCt0rjlWvN79bcVumVPMl2kKNrn6ZOGaBXjv7YiYyBBRASHwDasU16oYLXS4yVLMF4RmM5pFMclpThOcf25mGNtHC74zO8WT90oDeNyO2VES57Ofk%2Fq3iYhkgIP8Z7CofbJlxe%2BcTfgMV8vig7PhEPM6HDsAqSM5LWqRVV%2F3eX6YqGu7t397sdh5I6PSszqXBjoNnHKPMXLebkdQZfWhgZ3U5%2Byu2YH9V0piePMuk1j3r%2FR9DAyWsZffoos4IRnO4Alk4IklbuFLG17L7VuLRIl5Mnv6WkRHDCLcg6z3eyhW%2F6xBcFhn%2BbLPjF%2FlrGZDd29tOiuNJEhLfoHU%2BtC2zCtYFN7f1%2BBxq3z%2FuuRi3P6sCkjp0xviXvr%2Bf068zdIxisCoLHHh1eQwouQUwAQ7YsJqJNTW%2B2GzYEjNe4RzBM%2FZpCf0Fwgioz28xOwNOpGTruKt%2B1kIQ1Fageoz3W7r6tIz37j019zyvoX1PQsU5%2BZw1uCyR0MrR0ExXoFgeudEjd82n5ty7QSZGhUtsH%2FHeuQ0gDRHsRm8gktnXmfA7c5AX9gJIbzHYKSaUY6CBwI2XpzXoohLCu1%2BNDJIE8%2BvDIt7PGhP2lveJwqOoDrs2UWCwms2ldiTCjuP%2FSBjqkAQ4htCWEpLsghie3QqbIvX70DQWu6T%2FDGnHrc%2B0lA7lKqDWgFTw6m7MOtMyAt%2B6rfUhLaqpz53l%2BhXfmxM6Q6tvixGuSESKwnGyQvaRyEaItlgA9ug66usg5AcxIDtL%2FEItLaOZ8aKlkSqH56vzuiUSmRRRuNHRabV0%2BDg91HZHBGnn%2F4Z%2FhYG3DQm540f9UYcdzLN5vXsbDHiEEPTDfDBlcoOW1&X-Amz-Signature=38b35902a4ad5aa44e102b77898acea73b393dcb4c465a454249ebb31d507f5c&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

同学们大家好，这一章节我们来去介绍 SPU 面试题深度解析。这里面的问题就是 bin factory 和 applicting context 的关系。那么大家知道 bin factory 和 applicting context 它都是始终容器里面比较高级一点的一些接口，向 bin fact 里面提供了一些基础的一些 get bin 的操作application，它提供了一些更复杂的一些我们容器管理的一些功能，像我们的事件，我们的属性注入等等这些。


那么关于 b factory 和 picking 的它们关系，我们怎么来介绍？我们来首先来了解一下 b infactory，首先 b infactory 对于 spring 来说，它是 LC 容器最高层的一个抽象，也就是说我们 b factory 整个 spring 容器里面它的这个顶级的一个抽象接口，那么 applicase context 它也继承了 bin factory，那么它提供了各种获取 bin 的一些方法，其实它只有一个默认实现，这个默认实现也就是 defailed listable being factory。真正的在我们使用容器构建的过程中，所有的容器都是 debug listable being factory，它去做我们这个容器的储存的。


那我们来看一下这个 b factory 它类的实现。我们回顾一下这里面其实最重要的，也就是说我们根据各种不同的参数去获取我们 bin 的一些情况，这里面我们根据一些类型，我们类型和对象的指定对象以及我们的一些名称。下面我们可以根据 Tab 去获取到我们指定的一些类，也就是说我们根据这个 bin 的名称获取到我们这个 bin 的类的实例。


那么我们来看一下这个 bin package 它的一些验生接口和一些实现。那我们可以看到这里面验生出来的 configurable being factory 以及这里面 application context，我们可以看到 Applican context 在与 be infactor 这两个接口之间的这些继承关系。这里面有 outliable capable being factory 以及 leasable being factory 这些接口的一些事件的过程。对于 being factory 的，也就是说它默认的实现就是 debug 的 listable being factory，这是我们可用的一个factory。


接下来我们看一下 application context，那么 application context 它实现了 bin factor 的所有方法，实现了 be infective 出的方法，这个实现的意义怎么理解？它跟那个底票的 list will be infect 实现还是不一样的，它默认的这个 be in fact 实现，它肯定是通过我们的方式实现了这些功能。那么对于 a pacing context，它的实现的过程，它其实通过 detail 的 list able be effectively 的代理的方式去实现了。接下来就是 a picking contact，它那个功能更加齐全，它支持一些后处理与一些事件机制。常用的一些实现就是基于注解的 configuration applixin context。其实我们可以说 application context，它是在 be infect 的基础上聚合了更多功能的一些扩展。


那么来看一下，在这里面我们可以看到 applicon context 接口，它跟这里面各种不同的 impact 之间是有一些关系的。这里面比如说对于它像 resource loader without pattern is slower 和我们的一些 application event police，也就是说这就是application，它相对于我们 being factory 扩展出来的这些接口，也就是说扩展出来这些功能。
那我们来看一下 Applicon context 它的一些实现，这里面常用的一些实现，我们可以看到它是 generic XML applixin context，这里面有我们 file system application context 以及 cos pass XML application context。其实我们在使用更多的也就是基于注解的 annotation configure applicon context 这样一个实现的内容。


好，接下来我们来看一下在 spring 官方里面，它对 be effective 与 applicon contact 一些定义？在这里面我们看到 being factory，它这里面的意思项也就只有一项，而 Python context 它满足所有的这些项。对于 being factory，它只是实现了我们这个 being 死裂化的和一些注入的一些规范。那么这里面关于生命周期的一些管理，以及我们自动注入 being post process 这些功能它是没有的。同时像自动注入 being faculty post process Pixel connect，它也实现了intact，它没有这样的功能。接下来像这里面有像 message source 的一些默认的转换及访问等等这样一些过程。下面有我们关于 application event Publisi，也就是说我们事件发布机制的一些完成，也就是这些相对于，也就是 application context 相对于 be effective 扩展的这些功能。


其实在这里面我们要区分 be effective 与 application context 的功能，我们选取哪个正常的我们生产环境使用，我们都会使用 Applicon context 的基于 application context 它的具体的实现，它内部一般都会包含我们的一个 be infactor 的实现，也就是对应的底票的 list able being package。其他的一种情况就是说我们单独使用 de 飘的 list able being package，只是我们在去深入研究这个 IO c 容器的实现过程中，我们更关注大多数我们生产环境下，我们只关注是 Applicon context 实现也就足够了。好，那么关于 bin pattern 与 application context 它们之间的一些区别与联系，我们就先介绍到这里，同学们，我们下一小节再见。


