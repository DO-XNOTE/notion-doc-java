---
title: 2-11 Spring AOP切面编程源码解析-4（1125）
---

# 2-11 Spring AOP切面编程源码解析-4（1125）

[image](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/1250d752-a7ca-4d1f-a345-1b4d8a28cc85/SCR-20240803-nilu.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XE4EU6LD%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T232012Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCon7YLWdAR%2FS%2B1qZo7O2DJkRslF48%2FW1YMySlXAkV%2FdgIgH6FTBRVNaXCRK4OVSVAHoaxt1fF1I2XmRkMXsxXGBfYqiAQIxv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDBySvxUfHZnExhDonSrcA%2Fy5vN0nx6sMGw2%2BWGaG5K8Lfpz%2BrOom2DmdTG7zXuXTUJKIxpha2pMMbUhvx2zRY1k1Mj65SD1681umU7UkC0tBTq4cOFoxt1dVEeIGOZu79%2FrsiUXPiYnLKVFU9PqqOc5%2FGwq9mqsujFDGxifXX8nMYbNqAhQZheXuRxT0vaIjzQkfiBiN4s%2FKpNi0Jv1798j9pioyRDxy6Pv2cYFXzCD6onM8viaJaO9xkWmekvkWw1Zqcejg7UbRd4nah6b0QW74rzp%2BawZjDvHGSXudWArmKwhKoBwLms%2FkfvaLDf41QfNQSzHcUcd6AsPphrwoCy3VhDhxhxBa1wpbE35tFyjkN9SDT7GTawamY%2B%2BnjDhVS2GSJcj4Z3mf28YFU2LkBp%2Bgrj7b87sczdXy9OMUJb6F0c7GxTCDkYIGnQQIO48aQzQlxaBnl4uYzNGCY7aDtUstciqKCG5jr1oELAfEP31wgXaAmdVg3t%2F3L0cf3r5O0A%2BAaMv%2Fn5o4oIqY14l6Ce%2FS%2FemqgVI72tC6HMsRrw%2FETAXGjfH1sspEw6zb4H2R127QRsk1I9hzMUh6ZoxBA2heKMHbF0sqPWJQ%2BBibRmytyrTQun5B%2BmCLYviXouIqVyLB0DtieSFkXlUCMOq3%2F9IGOqUBB37zwjsewIkCUIwk78aTHaJ1Q6H%2FpsUQwromt0wkxHMMd0zM2PdIqvuJR5Qoc2joHjMT3%2F5Xngjm0mGB%2FqktzFAUjKaA5uqVuM0DSLqRzSZYDdhRpHSoQduRoJJNsk%2F8nUWHnz04M2W0KGGsboZ8wYr6pk4sTmYnZxBNnLxsuyAyE8Y8WYqcWjIyfsGFOAiuQ0TSACLW7CcOdw7XAl0o2xrFewxS&X-Amz-Signature=18c770c9f199d6e9eb3ca4a317fd7207a5bd0380aa779609438a691ed52f744b&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

这里面我们首先来看一下 AOP 相关的注解有哪些，接着基于注解AOP，我们介绍一下 AOP 的执行流程。最后我们看一下基于注解 AOP 的一些源码分析。首先我们来看一下跟 AOP 相关的注解，在这里面我跟 AOP 常见的注解其实比较有限，我们最重要的是 enable aspect 加 auto process，这是注解开启我们的 AOP 的制动代理。接下来我们在构建 AOP 的这些实现类的时候，比如切面，我们通过 aspect 去构建这个切面类 point cat 这个注解，构建一下我们对于切入点的一些表达式，这里面 before off 的 round 就是对应我们这个advice，也就是我们这个增强的表现形式，自前自后或者一个环绕的通知的方式。


我们了解完这些注解，其实这些注解理解起来是比较简单的，我们看起来也比较容易，尤其是像 before off the round 这些注解，我们见名字义。那么好，我们看一下它的简单的一个执行流程。首先我们通过这个 enable aspect 及 auto present 去开启 AUP 的生命。时代里通过它会注册我们这里面是 aspect 接 autopress register，这个 register 其实就是一个 import being defined register，它只在 being definition load 的阶段去 register 注册。


注册的过程需要注的事情是什么呢？首先把这个 annotation aware aspect 接 auto price creator 注为一个 being post process，注册到我们的 bin 容器里面，注册到必应容器里面，它通过 post process before instance 和我们的 post process after its lesson 把我们的 being 包装成代理对象。这个跟我们 GX non 的处理过程是比较类似的，只是说整个过程我们一个是通过我们注解去开启的，应该是通过 XR 加载去开启。在这个注册完成以后，等我们 bin 在初始化的过程中，它会通过一个叫 being factory aspect 接 Advisor builder，通过这个 builder 在当前的工厂中寻找带有 aspect 接的注释的这些bin，并且构建出一个 adviser 列表去构建我们的 bin 代理。其实它这个 builder 它其实是依赖了我们这个 reflective aspect 接 the best factory，它做的事情主要是通过反色的方式去解析 aspect 接相关的这些注解，这里面的注解主要包括像 point cut， before off the round 等等这样一些注解。这些注解解析完成以后，就完成了我们整一个 bin 的定义解析的过程。那么同时在初始化的过程中，通过 post process 的方法把我们的 bin 包装起来，这是我们可以简单理解为基于注解 AOPT 方式的一些初始化的过程。


我们来看一下这个 register 它做的一些事情是什么。我们可以看到在这个 register being dignation 的话，它这里面第一句话，也就是说通过 AOP configure 误头去 reject aspect allotation or to press creator，那么它跟我们在使用 XL 去解析过程中的第一句话也是很类似的，它都是去通过 AOP 的 configure UTO 去开启我们的制动代理。
那么开启完制动代理接下来是什么呢？它就会通过我们的这些操作看一下我们当前的 enable aspect 及Autopri，它这个代理这样开启代理的属性配置，它属性配置这里面主要是解析的一个属性就是 proxy target class 是不是基于类的方式去构建我们的代理，这是整个 reject bin 提分的且执行的过程。


接下来我们通过代码四类来演示一下基于注解的AOP。好，首先我们来看一下我们这个 lock aspect，它基于注解的 u p 类，首先它是通过 aspect 接作为一个注解的修饰对应它的方法。我们这里面首先定义一个 point cat，这个 point cat 它的内容也是对应的。我们写一个表达式，这个表达式表明一下 so case been。下面的这些所有方法都会去扫描到，下面我们定义了几个advice，一个分别是 around 和我们的 off 和 off 的returning。这里面我们重点关注一下around。


在 round 我们执行的过程中，我们可以看到我们对于这个方法执行前，执行后分别打印出了日志，并且打印出了这个方法整个执行的时长，这是我们整个这个 AOP 处理的过程。看一下对应这个 AOP 它的 test 类，这里面我们用到了 spring DN need configure 它的测试方案，这里面我们首先去通过启动整个启动单元，测试的过程中它会通过我们这里面配置的 AOP 加 2 CONFIGURE，在这里面去加载我们的configuration，并且配置相关的这些bin。在配置这些相关 bin 的过程，我们这里面会执行 enable aspect。接 auto progress 就是开启我们的制动代理，这样我们点击自动代理，我们可以看一下在自动代理类上它有一个import，对应的一个叫register，它做的事情我们可以从这里面看到 rejection 的注册词性。


首先它第一步也就是通过 AOP configure utiles 注册一下 annotation or to a process creator，也就是说它注册一下这个 being post process，我们可以进去看一下，这个我们应该比较熟悉的，因为在执行 XL 的 AUP 的时候，它也会注册一个对应的一个 Autopress Creator，这里面是对应的是这个类。它其实作为一个 being pose precise，我们可以跟进来看一下，它主要提供了两个功能，第一个功能就是我们在这里面是初始化这个 being factory 的时候，它去构建出一个 aspect 接 adviser factory，这个 factory 它是通过 reflective aspect 及 Advisor factory 去构建的。它构建完成以后，我们再构建一个 aspect 及 Advisor builder，是依赖了这个 aspect 及 Advisor factory。
我们可以看到在构建这个 being factor 的 pet 接 Advisor build Adapt 过程中，通过 aspect 接 Advise EFFECTS 作为参数构建，那么对于这个builder，它处理的主要工作就是构建我们的adversion，那么在我们的 being 在初始化的过程中，它会执行这个 find candidate Advisor，也就是说获取所有候选的 Advisor 就是这个Advisor。
大家一定要理解它是我们的这个通知和我们的切入点的一个组合，也就是说 advertiser 它包含一个 advice 和一个 point cat，那么在这里面它执行的过程中会通过我们这个 builder 去 build aspect 及Advisor，这就是整个它比较起作用的地方，在这里面它会去解析对应的这些注解，并把这些注解里面解析成对应的bin，构建成一个debuser，一个列表返回过来这个就是整个这样一个操作的过程，那么我们现在可以通过启动单元测试，我们对关键这几个地方做了断顶。


我们去看一下，我们现在去执行我们 debug 操作。首先这一步是在这里面去注册我们的一个 be impose process，那么我们这一步我们跳过下面我们可以看到在这里面是初始化 init being factory，就是初始化变音的过程中，把我们这两个属性，也就是一个 adviser factory 和一个 adviser builder，把这两个属性构建出来。


我们下一步我们跳过注解，我们可以看到在这里面的是开始执行我们的一个 advisor and visitor for b，在这里面它是做了什么事情，我们可以看到这个方法是在 wapper 一个necessary，我们知道这个包装类是在我们的 being post process 里面去执行的，也就是说现在需要对我们的 b n 去做一些处理。


这里面我们看到当前的 b 音是 a o p 加configure，对这个 b 音我们其实并不关心，我们现在主要关心的还是 hello bean，我们跳过我们可以看到对于这个 bean name hello，那么这个我们可以去关注一下，通过它去执行下去，我们看一下它执行的操作。在这里面我们获取这个过程中的话，它会间接的去调用到我们这里面的是 positive Creator 里面的方法。好，我们继续在这里面，我们点击进去，我们再跟进去，好在这里面我们可以看到它已经调到我们的 notify where aspect，接 auto process creator，这里面我们看它会通过这个 builder 的方式去构建我们的这些adventure。那么我们现在去 debug 进球，我们看一下它做了哪些处理。在这里面我们可以看到它的操作是通过 a set name 去获取一下这些首先词。 cats 的 Advisor 就是因为第一步的话这个缓存肯定是没有的，我们它是获取不到内容的，这里面是获取到了三个，那么它就把它放进去了。



好，我们可以看一下这个三个 Advisor 分别是什么对象，在这里面我们会看到这三个分别是对应我们几个注解的aspector，它分别是对应了我们的 around after 和 off returning，也就是我们在这里边定义的三个Advisor，我们的 Advisor 和我们的 point cat 的一个组装的一个内容，我们跳出好在这里面我们看它已经执行完成。这样的话去获取到这个Advisor，它就可以通过 Advisor 去对我们的 bin 进行一个增强的操作，这样的话我们看它会通过获取到的 adversion 去对我们的 being 来进行代理。
这个下面 create a prexin 的内容，我们刚才在 XL 构建 AUP 的过程已经讲，我们就不跟进去了，这就说明我们通过注解的方式已经完成了我们代理的注入，我们可以跳出断点到这里面我们基于注解的 AOP 的源码分析也已经完成了，现在大家对于AOP，不管是通过 XL 或者说是注解，甚至通过proxy、 fix room 我们手工去写 AOP 的代理也都已经没问题了。那么好了，关于 AOP 的源码分析我们就先介绍到这里，同学们，我们下一节再见。

