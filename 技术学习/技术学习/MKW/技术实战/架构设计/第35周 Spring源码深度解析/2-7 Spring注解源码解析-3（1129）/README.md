---
title: 2-7 Spring注解源码解析-3（1129）
---

# 2-7 Spring注解源码解析-3（1129）

[image](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/9a9f69e9-e4f6-4711-be04-a3b7ec743efa/SCR-20240803-mdwn.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466V7ONYEZR%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T232006Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIEjZQHHcL%2Bx2ajzlQqmL3d0KwXKWwpW8PE7VQA%2FxqBA5AiBiXwXjcctnMjX0XoxtxSyN3cWGb6f5qV4FUWqgj9EeJyqIBAjG%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMMs74OcoOs%2F3etjnIKtwDPyDqQkk3w1bxzp7QCGhF9mPGGDZDx0m3%2FgQ%2B%2F2wft6lC0ofJOjdOpsyBztcZgwx%2F86T111fViqNA7luV%2BzfxLzf58d5VoxCDyep%2Fa7c8UaibhOGlrOosNXamxdoxXFRE0TllWxsVq4%2FSIVgfzmDmatanskz8asSbbRO9ZfGRCgs6UffXri3%2BqhzQIm1QDlR2VVmYT0%2FrzlXAX7%2BWj03NJ1QeVTOYgNB%2F2vywPBF0c5jXgewAb5yNqLHPxTBBeX08OkVYUasouPRVWyw%2BNBnGKjLlmu7Nli0LGRd00YZmmd9L05I2DzLbU6RpB8njMktyQ3CtQBA1r%2FuSGZLKj9pgj45BgECfdqg8EZcApsfGoLnly55ifsWtH0xGge40%2Bt%2FpBDjD41bQmevP9B%2FICtuG4rR2MZ53q1P3%2BE0WRysYYizHS1r8F6UpTRNfZwDUnZdZwrQONCxkCUZUSGToZJ3lof%2Br5Nxj%2BhOpA1gapYmXTgcUMgKWveIX8z0n3PLtbZUkd8qMCCrPC2mjPzFs52OPAOZqWYG75ZfayHHqul2OfPSVPT0C6oufEOh5wRMLa5npHxeIKqfLmWCFJKcSJCDo16i1fdOrbvEGNjOxggAi2jgc13i300nwEsz2OLkw8rr%2F0gY6pgF6lBUPz4g2vq0PnO%2FvOzzU5pt0rGC%2FEz9qOk0507gHwouTaVbdtlwSnwaVC1WtxjNKZC8x4myudIcaA6EKlFOpk0aZu4G0O5BeO%2F1Tzz3Cp6fUhxNgMc6%2BnDV6h9Bv%2B8uR1ZOoQU%2FecNrlmzgzGAJcQr%2FnjgcjOLYqgK1pPjSeiYWMjqBUevIwFLyc8%2BowsiJplLhElpPOA9HNZV%2F9IdT8oxr44Ldm&X-Amz-Signature=d45cc83765d9ebde6a95de5bb4166cd0051ae7600342b174bad2ab4f7cd99048&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

我们可以看一下在这里面我们对于解析的内容，整个这里面 configuration class， post process，它的内容相对比较复杂，我们还可以通过这里面去看一下，在这里面我们 configuration Claude pose process，它通过去遍历所有这些病例森里面是否包含 add configuration 这个注解，如果包含这个注解的话，通过它去建进行一些深层值的去处理。


处理的过程主要是处理，首先是 component class 和post， property sauce 和 property sauce，这是s，这是 property sauce 以及我们的 component scans 和 component scan，这里面有 import resource 和 bin 这些注解。


处理完成以后还有我们处理一下对应的接口和我们的父类，就是继承类相关的一些处理，也就是整个 configuration Claude process 处理了这么多相关的一些注解的一些信息，等整个这些处理完成以后，它要对 bin defin 注的事情就是什么呢？需要通过我们的 configuration class being defense 的一个 reader 进行 load being defense 操作。这个 load being defending 的最终结果就是把我们当前那个 bindi 文件注册到我们的容器里面，好来跟从代码看一下这个效果。我们通过这里面 pass 解析完成以后，接下来去做一些处理，去创建一个我们的reader，这个 reader 是 configuring 卡死 being defini reader，通过这个 reader 去 load being dependence。我们跟一下，看一下我们处理的过程，在这里面我们接着跟进去这里面我们看一下，在这里面去做了两类操作，一个是我们是 load being definition from import resource load being dependent from a register。这里面还有我们的是 from import configure class 和我们的都得 being depending for being master。这几个我们都是通过不同的应用场景把我们的 being depending 进行 load 的操作。


我们在这里面看一个相对来说比喻较简单的，这里面我们是看 load being dependent for being messed，我们跟进去看一下，在这里面它要 load being dependent 需要处理的事情，是也是这里面首先需要去判断一下数字 Skype 是否为true，如果说当前的是否判断跳过，如果说这些校验都没什么问题，我们接下来处理的是我们看一下通过我们的 a notation campaign util 里面获取到我们这个 BN 注解的这些属性。


我们再看一下当前这个 BN 的状态，如果说，比如说当前，如果说他没有当前这个闭音属性的话，就会用通过断言的失败去处理掉，那么最终我们会看到他得到的一些操作，就是我们会把这个 bin 注册到我们的 bin 容器里面，注册的方式也就是我们通过这里面首先会注册一下我们的别名，注册完别名信息以后他再做一些业务的一些处理。这里面我们可以看到它会对应我们的是 Bing class 的一些设置操作。下面还有一些我们可以看到这里面的一些是否 out where？我们获取到 out where 相关的一些信息， out where 的内容，这里面还有是 init must 和 detried must 直接的信息，是否需要处理一下等等，最终我们处理的结果它会到这里面去执行。


我们的 Gestry registered being definition，我们可以看到这里面其实这个 registry 就是我们对应的 be infactory，这个 be infactory 把我们这个当前指定的我们的 BDP 的文件去注册进去。好，这个里面整个我们通过解析并且注册完成以后，我们这个后处理的这个操作就是完成了。



那么我们回过来看一下我们这里面后处理完成以后，后面还需要去 reject 并 post process，我们接下来看这里面的一些内容，好，我们看一下处理完我们的 b impact pose price，后面是我们要 regist being pose process，我们看一下这里面做的事情是什么？它也是通过我们的 post process regist delegate 去做的，我们看它这里面处理的操作是也是通过我们的 being factor 里面去获取到所有我们这个 be impose process 这些 being BDK 内文件。


这些获取完成以后，注意在这里面获取的过程其实已经把我们这个 bin 进行了实例化，获取完成以后它需要注的四项是在 being factory add being post process，也就是说我们整个这个对象在容器里面，它并不能起到这个 post process 的作用，必须把它取出来放到我们的 be impose process 这个列表里面，才可以在这里面把它放进去以后去再做一些处理。后面是对我们这些 post process 仅根据它的优先级去做一些排序，并且把它进行一些重新的组合，这些对于我们来说其实就并没有那么重要了。
我们回到我们的 refresh 方法里面，我们继续看，接下来我们应该去执行我们的 init message source，也就是初始化我们的消息的一些数据来源。我们可以看到这里面是也是通过我们 bin factor 里面去看一下当前我们的 message source bin 的是否存在，如果是存在的话，我们就会去把它去获取出来进行一些操作，这里面也需要去看一下跟我们的副 part 里面的一些信息进行一些 merge 和一些融合，最终我们可以看到在这里面去把我们当前的这些 message source 注册到我们的 bean taxi 里面，后面是 init applicase event MOS card。也就是说我们进行一下我们的一个四件广播器的一个定义。在这里面也是首先判断一下当前这个 bin 是否在容器里面已经存在了，如果在我们的 being factory 已经存在的话，那么把它获取出来，同时把它赋值给我们当前的这个属性 application event Multicast。


当然正常情况下我们的 bin factor 如果说没有设置的话，它应该是为now，就是 if 这里面它不会执行进来，它会执行到 else 的操作，这 else 成绩的话，它执行的内容就是我们通过当前的信息，我们的 be in fact 去构建一下我们一个 simple Epic event must cast，也就是说我们的一个事件触发器整个这个构建过程构建完成以后，把它复制到我们的当前属性，同时也把它注册到我们的 bin factory 里面。整个这个跟我们的阿里皮克的 event 这个广播器的工作就已经完成了。


接下来我们看后面的内容。四件广播器之后就是我们的unrefresh，这个方法其实也是给我们的子类留出一个扩展的入口，它本身在当前类里面并没有做任何实现。 on refresh 后面就是注册一下我们的listener，也就是注册我们的监听器，好，我们可以看到在这里面注册监听器的时候，也是把我们所有的当前方法里面的监听器获取过来，注册到我们那个监听器的一个广播器里面，这样一种执行的操作。同时这是我们在容器里面的设置的 please condition 的同时，我们如果说在我们 being 的容器里面，也就是说我们的 get being name for type 获取到 application listener 这样的一些 being defined 的话，它也可以去作为我们的事件监听，那么同时也是通过这种方式去把这个 bin at 进 at listener bin 里边注射进来，同时这样的话如果说有那么一些对于比较需要早期去触发的一些 applicans event 事件的，对于这些事件我们在这里面需要提前的把它进行广播出去，这是我们的事件，我们看好后面就是事前就是另一个了。


这里面就是 Phoenix be in fact initiation，也就是说执行到这个过程，我们整个跟我们容器相关的一些注册初始化的工作完成了。那么整个 bin definition 初始化完成以后要做的事情是什么呢？是需要对我们的 bin 进行实例化，这里面的实例化就是通过我们看这里面是去调用 get Bing 的操作去进行实例化的操作，在这里面会对于我们整个操作的过程去做一些组织最终会做的事情，就是 BN factory Pre instacent，就是把我们的单例的一些 BN 列私立化，但是这里面需要注意一下，对于一些lazy，也就是说懒加载的一些初始化方法，这里面并不包含进来。我们进去看一下它里面注的一些操作是什么。在这里面操作的内容也就是执行我们到 debug listable be effectively 的操作，它会通过我们这里面对于所有的方法去调用 get bin 的操作，把我们的这些实例化完成。


好到这一步，下面就是我们的 Phoenix Refresh。 finish Refresh 跟 Unrefresh 很相似，它只是标明当前是一个时间状态，这里面我们可以去对于我们的一个，子类的去复写或者一些扩展的内容。这里面我们更多关心的就是它通过 publish event 发布出一个 context refresh event，这样标明我们当前这个 Refresh 的操作已经接近尾声，好执行完这个过程我们可以理解为整个我们的 refer 操作已经完成了。后面就是我们需要对 family 里面执行的，也就是把我们的一些通用的一些 cat 空间去释放出来，最终把我们嗯 contact reference 进行结束，这样的话我们整个初始化的流程就先进行执行完成了。


回到我们这个脑图，我们再整个捋顺一下我们这个 try 代码块里面执行的内容。首先也是我们的一些 post process impact 一些处理，这也可以理解为它跟我们留出了一个回调的空间，这里面的 unrefresh 方法也是留出一个回调的方向，包括我们的 Phoenix Refresh 的操作，其实这里面它做的一些实现最关键的也就是 Publice event， contact refer event，这是几个关于时间点的操作。


对于我们整个过程来说相对比较重要的一个就是我们的 invoke being factory post process，它是对我们的 configursen class 去进行一些后处理，把我们这些里面所包含的一些鼻音的定义解析出来，把它装载到我们的容器里面。另一个比较重要的也就是我们的 Phoenix b impact installation，他注的操作就是当整个业务准备工作处理完成以后，把我们整个这里面的这些bin，也就是说这些非懒家产的 bin 进行实例化完成，也就是整个 b 容器就执行完成。其他整个这个过程里面一些细节是非常多的，大家对整个处理流程中几个关键的步骤理解清楚，这样就会对我们后面的系统架构设计提供很好的帮助。好了，我们这一节就先介绍到这里，同学们，我们下一节再见。

