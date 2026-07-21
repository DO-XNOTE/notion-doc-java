---
title: 1-1 对象池详解
---

# 1-1 对象池详解

[image](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/834e4d9f-7535-4dc6-8295-81eb6ea946c2/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663AXYZQBU%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T230106Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCICtpHjqCnmPN2EfbvnMRsKajfenuHSivnhzkBBdksr1jAiEA8XIS6l%2Bj7saUbpxt4tVAm%2FmOfYN8o8FoUeEnUGKXr88qiAQIxv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDCnKZ3DjRTiwVA8hiCrcAwe5dgh5Nx%2BybskS13Z1LzqkzVg2ttPpV6jwTpnJUD6QulfEySo4d6lPVAqSnr7E9uSfbGnbB2w3PRQC2g080y4tgfDZiwyQjD%2FnXkQs0Ey96a5mBzubprOUR16rFku5YA2gN3BttN4w055H5pAA4B65Nui3gKi1l4BxN59Mm5yl4at2jpx8A2BC4T9Si3z%2FBmbY8VjvTG3c3alQ%2BVobZhrHIn4vNM8cSN0NolY%2BCurPb%2FJMu3oCDDLefLQgipZX9cZJYYxmmK28gGHTFst0GXZHg4SilkxQIRpWDa1dNL0Emw9erixdXJOkBt0xqjhW%2FB3UJ4%2FPmJ96yzXx3AH2jA3dVnNBaWyesW%2FYtfJO2sGMPUTRAUyUjYLNmillD82rrYwqoczLI27gMnsXQMr7oQ0jcp%2BSK9KBqXX3Bf%2FoDFNeXDCh7KrvsAcGKb7itaA%2B6fQu7GazWGbGr43cTMVty9OPxdpKSuM5W5IGhvVxuV%2B%2F%2Ftxe3aqNv4dE21aQ3X742dDldWlHIPWQD%2FeBTMQ6lcj4TsFe0VaElkKfrIy3xGJkjJli3UqaxteIhXfB8xcrYdruaF0%2Flhl5xlGog1cfI8qqh5bDF3Cy4Pz50C534ncjq5q%2FL%2BzRIcV5EqceMMu3%2F9IGOqUB5wb97EEyxc3xmjVNjZeAQc%2FuNtz2QNaaBCCbHmNtn4fkdH6uaQNMebCobBad8lYHPEkBoHaV8XnLMh8%2Fm2NzR6GeH%2BXjsbdNa94P%2FTR2Wh7o6At6ZPFbycjwu8AV1ZvXOR72ZoXdKhWRJiaApopxO9ndllJPyWLEsEJxYNVrzFkr%2FFc3Bz13rIEuazsolWvKdyM%2BXPtebjcRnAK9JrzMz2O4q7w%2F&X-Amz-Signature=979e0729ad1f0bcb75f56ce2c70b59e7570908499cfd85e828302da57ec83783&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

[image](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/2c5a88f1-db10-4dc5-bc0f-9b5bf4332c7e/SCR-20240727-tzjs.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663AXYZQBU%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T230106Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCICtpHjqCnmPN2EfbvnMRsKajfenuHSivnhzkBBdksr1jAiEA8XIS6l%2Bj7saUbpxt4tVAm%2FmOfYN8o8FoUeEnUGKXr88qiAQIxv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDCnKZ3DjRTiwVA8hiCrcAwe5dgh5Nx%2BybskS13Z1LzqkzVg2ttPpV6jwTpnJUD6QulfEySo4d6lPVAqSnr7E9uSfbGnbB2w3PRQC2g080y4tgfDZiwyQjD%2FnXkQs0Ey96a5mBzubprOUR16rFku5YA2gN3BttN4w055H5pAA4B65Nui3gKi1l4BxN59Mm5yl4at2jpx8A2BC4T9Si3z%2FBmbY8VjvTG3c3alQ%2BVobZhrHIn4vNM8cSN0NolY%2BCurPb%2FJMu3oCDDLefLQgipZX9cZJYYxmmK28gGHTFst0GXZHg4SilkxQIRpWDa1dNL0Emw9erixdXJOkBt0xqjhW%2FB3UJ4%2FPmJ96yzXx3AH2jA3dVnNBaWyesW%2FYtfJO2sGMPUTRAUyUjYLNmillD82rrYwqoczLI27gMnsXQMr7oQ0jcp%2BSK9KBqXX3Bf%2FoDFNeXDCh7KrvsAcGKb7itaA%2B6fQu7GazWGbGr43cTMVty9OPxdpKSuM5W5IGhvVxuV%2B%2F%2Ftxe3aqNv4dE21aQ3X742dDldWlHIPWQD%2FeBTMQ6lcj4TsFe0VaElkKfrIy3xGJkjJli3UqaxteIhXfB8xcrYdruaF0%2Flhl5xlGog1cfI8qqh5bDF3Cy4Pz50C534ncjq5q%2FL%2BzRIcV5EqceMMu3%2F9IGOqUB5wb97EEyxc3xmjVNjZeAQc%2FuNtz2QNaaBCCbHmNtn4fkdH6uaQNMebCobBad8lYHPEkBoHaV8XnLMh8%2Fm2NzR6GeH%2BXjsbdNa94P%2FTR2Wh7o6At6ZPFbycjwu8AV1ZvXOR72ZoXdKhWRJiaApopxO9ndllJPyWLEsEJxYNVrzFkr%2FFc3Bz13rIEuazsolWvKdyM%2BXPtebjcRnAK9JrzMz2O4q7w%2F&X-Amz-Signature=4d27c356d58b1ecacdf5640040e55380d91745eae02bc980606d1be70b05a1c0&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

[image](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/0d30dff3-563c-4369-8874-d212fe67cdb9/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663AXYZQBU%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T230106Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCICtpHjqCnmPN2EfbvnMRsKajfenuHSivnhzkBBdksr1jAiEA8XIS6l%2Bj7saUbpxt4tVAm%2FmOfYN8o8FoUeEnUGKXr88qiAQIxv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDCnKZ3DjRTiwVA8hiCrcAwe5dgh5Nx%2BybskS13Z1LzqkzVg2ttPpV6jwTpnJUD6QulfEySo4d6lPVAqSnr7E9uSfbGnbB2w3PRQC2g080y4tgfDZiwyQjD%2FnXkQs0Ey96a5mBzubprOUR16rFku5YA2gN3BttN4w055H5pAA4B65Nui3gKi1l4BxN59Mm5yl4at2jpx8A2BC4T9Si3z%2FBmbY8VjvTG3c3alQ%2BVobZhrHIn4vNM8cSN0NolY%2BCurPb%2FJMu3oCDDLefLQgipZX9cZJYYxmmK28gGHTFst0GXZHg4SilkxQIRpWDa1dNL0Emw9erixdXJOkBt0xqjhW%2FB3UJ4%2FPmJ96yzXx3AH2jA3dVnNBaWyesW%2FYtfJO2sGMPUTRAUyUjYLNmillD82rrYwqoczLI27gMnsXQMr7oQ0jcp%2BSK9KBqXX3Bf%2FoDFNeXDCh7KrvsAcGKb7itaA%2B6fQu7GazWGbGr43cTMVty9OPxdpKSuM5W5IGhvVxuV%2B%2F%2Ftxe3aqNv4dE21aQ3X742dDldWlHIPWQD%2FeBTMQ6lcj4TsFe0VaElkKfrIy3xGJkjJli3UqaxteIhXfB8xcrYdruaF0%2Flhl5xlGog1cfI8qqh5bDF3Cy4Pz50C534ncjq5q%2FL%2BzRIcV5EqceMMu3%2F9IGOqUB5wb97EEyxc3xmjVNjZeAQc%2FuNtz2QNaaBCCbHmNtn4fkdH6uaQNMebCobBad8lYHPEkBoHaV8XnLMh8%2Fm2NzR6GeH%2BXjsbdNa94P%2FTR2Wh7o6At6ZPFbycjwu8AV1ZvXOR72ZoXdKhWRJiaApopxO9ndllJPyWLEsEJxYNVrzFkr%2FFc3Bz13rIEuazsolWvKdyM%2BXPtebjcRnAK9JrzMz2O4q7w%2F&X-Amz-Signature=7ac2b7cb8ae695d98d2a54b3a26d06dea50249578c3934e88c8ebb86badfc94c&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

大家好，我是大木。石化技术是性能调优的重要措施。石化的思想是把对象放到池子里面，但要使用的时候从池子里面拿对象用完了之后再放回到池子里面去，这样可以降低资源分配以及释放的开销，从而提升性能。在实际项目中，其实我们每天都在使用池化技术。比方对象池通过复用对象，从而减少创建对象以及垃圾回收的开销。线程池通过复用线程，从而提升性能。连接池通过复用连接，从而提升性能。

[image](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/381f2a99-a990-4257-9559-8604c956eb2a/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663AXYZQBU%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T230106Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCICtpHjqCnmPN2EfbvnMRsKajfenuHSivnhzkBBdksr1jAiEA8XIS6l%2Bj7saUbpxt4tVAm%2FmOfYN8o8FoUeEnUGKXr88qiAQIxv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDCnKZ3DjRTiwVA8hiCrcAwe5dgh5Nx%2BybskS13Z1LzqkzVg2ttPpV6jwTpnJUD6QulfEySo4d6lPVAqSnr7E9uSfbGnbB2w3PRQC2g080y4tgfDZiwyQjD%2FnXkQs0Ey96a5mBzubprOUR16rFku5YA2gN3BttN4w055H5pAA4B65Nui3gKi1l4BxN59Mm5yl4at2jpx8A2BC4T9Si3z%2FBmbY8VjvTG3c3alQ%2BVobZhrHIn4vNM8cSN0NolY%2BCurPb%2FJMu3oCDDLefLQgipZX9cZJYYxmmK28gGHTFst0GXZHg4SilkxQIRpWDa1dNL0Emw9erixdXJOkBt0xqjhW%2FB3UJ4%2FPmJ96yzXx3AH2jA3dVnNBaWyesW%2FYtfJO2sGMPUTRAUyUjYLNmillD82rrYwqoczLI27gMnsXQMr7oQ0jcp%2BSK9KBqXX3Bf%2FoDFNeXDCh7KrvsAcGKb7itaA%2B6fQu7GazWGbGr43cTMVty9OPxdpKSuM5W5IGhvVxuV%2B%2F%2Ftxe3aqNv4dE21aQ3X742dDldWlHIPWQD%2FeBTMQ6lcj4TsFe0VaElkKfrIy3xGJkjJli3UqaxteIhXfB8xcrYdruaF0%2Flhl5xlGog1cfI8qqh5bDF3Cy4Pz50C534ncjq5q%2FL%2BzRIcV5EqceMMu3%2F9IGOqUB5wb97EEyxc3xmjVNjZeAQc%2FuNtz2QNaaBCCbHmNtn4fkdH6uaQNMebCobBad8lYHPEkBoHaV8XnLMh8%2Fm2NzR6GeH%2BXjsbdNa94P%2FTR2Wh7o6At6ZPFbycjwu8AV1ZvXOR72ZoXdKhWRJiaApopxO9ndllJPyWLEsEJxYNVrzFkr%2FFc3Bz13rIEuazsolWvKdyM%2BXPtebjcRnAK9JrzMz2O4q7w%2F&X-Amz-Signature=e002d1e9eff281ca641b1cc299b324a7d097860191430b1d596cb6b5620a6a80&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

这一节我们来详细探讨对象池。对象池适用于维护一些很大，创建很慢的对象。对象池也有缺点，首先它有一定的学习成本，第二，它增加了代码的复杂度，所以也不能滥用。下面先来看一个我实现的对象池。这段代码比较简单，首先弄了两个 set active set 存储活跃的对象， Idle set 存储空闲的对象。核心的方法也只有两个，一个叫 borrow object，用来从对象池里面获取对象。第二是 return object，用了在使用完对象之后，把对象归还给对象池。


先来分析 borrow object，我们首先会看是不是有空闲的对象，如果有，就直接复用空闲对象了。如果没有空闲对象，会判断当前对象池的大小是不是超标了。如果超标，就使用 wait 方法阻塞当前线程，直到下面 lock 点notify。被调用之后，阻塞的线程才会被唤起，它会进行递归。再次尝试获取对象。如果对象池没有超标的话，那么就用反射调用对象类里面的盈利的方法。也就是这里 money 类里面的 init 方法。初始化对象好。


 return object 的方法就更简单了，它用来归还对象。把对象从 active set 里面删掉，并且放到 Idle set 里面去。好在这里我提供了一个测试。大致上是这样的场景假设 money 这个类非常的大，创建的非常的慢。在 init 方法里面，我用 thread 点 sleep 模拟了创建慢的过程了。我们弄了 10 个线程去操作对象池里面的money。对象还弄了一个线程类。在线程类里面，我们频繁的从对象池借用money，使用 money 用完之后归还money。执行一下看看。



从日志可以发现，我们几乎每次都是复用了原有的对象，这样可以节省很多 new 对象的时间，并且也可以在一定程度上节约内存。所谓的对象池。不过这个对象池的实现还是比较蹩脚的，首先性能比较差，各种 synchronized 还有递归对吧。第二，这里的对象复用机制其实并没有真正实现，而是拿到一个对象直接认为可用了。这段代码主要是用来帮助大家理解对象池的核心的。实际项目中使用对象池，一般都会借助一些对象池框架。这里介绍一款业界非常流行的对象池框架，叫做 comments pull two。这是一个由阿帕奇基金会开源的框架，专门用来创建对象池。它的官网在这里， GitHub 地址在这里，感兴趣的同学可以看一下。


comments pool two 提供了两类对象池。第一类叫做 object pool，这个命名真形象对吧？ object pull 是一个接口，它有这么多的实现类，我们把每个实现类的作用和特性都总结出来了，同学们可以看一下。其中最重要功能最强，使用最广泛的是 generic object pool。这个对象池非常的强大，也比较的通用，而且封装的比较完备。 object put 核心 API 我也做了一个总结，这些 API 也非常的通俗，从名称就可以看出来含义了。同学们可以留一个印象，一会儿在实战的时候会用到。


第二类对象池是 key 的 object pull。这种对象池和刚刚的 object pull 的区别在于，它是通过 key 去找对象的。从设计上来说， key 的 object pull 和 object pull 没有区别。它有这几个实现类。使用最广的是几年入个 key 的 object pool。好，下面我们着重探讨。 object pool 来写代码。首先为项目添加 common two 的依赖。


import 一下，我们把代码写在我这里。事件创好的 comments pull 包里面依然围绕创建 money 对象慢的场景展开。首先把 bunny 类 copy 过来，粘贴，改成publicly，打包，创建一个类，叫做 comments pull to test， p s v m 创建变方法。我们使用几年 record object poor new， generic object pool。泛型的。


写money， new 的时候，我们发现有三个构造方法，有一个参数的，两个参数的以及三个参数的。其中一个参数的构造方法用来创建一个默认配置的对象池。两个参数的以及三个参数的构造方法可以传入配置。后面我们再来详细探讨配置的那些事儿。这里我们就用一个参数的了，它需要传入一个 poor 的 object factory。


pulled object factory 是用来创建对象的，其实用到了设计模式里面的工厂模式，对吧，大家应该都很熟悉的。目前 pulled object factory 有两个实现类，一个叫 base pulled object factory，它是一个抽象类，我们可以基于这个抽象类扩展成自己的 pulled object factory。第二是 synchronized pulled object factory，它是一个内部类，它用来代理一个其他的 pulled object factory。把 pulled object factory 包装成一个线程同步的类。一般来说， poor 的 object factory 都是需要我们自己根据业务去实现的。这里我们创建一个， come on money pull the object factory，让它实现。 pull the object factory 泛型写money， after enter 打包。当然了，这里也可以继承被子。


pulled object factory up center 实现方法可以看到 factory 类里面有很多的方法需要实现，我在这张表格里面做了详细的总结。这些 API 也是比较通俗易懂的来实现方法。 make a object 用来创建对象。这个方法返回 pulled object。大家想为什么这里返回的是 pulled object 而不是 money 呢？这也是 comes pull to 设计巧妙之处。 pull 的 object 可以对原始的对象，也就是这里的 money 进行包装，从而让 money 被对象池管理。目前的 poor 的 object 有两个实现类 default pull the object，可以包装原始对象，实现监控以及状态跟踪等等。


pull 的 soft reference 进一步的封装了 default pulled object，可以和 soft reference object 的 pool 配合使用。基于软链接的对象池。实际项目中 99% 的场景下用这两个类已经足够了。如果觉得不够用，可以继承这两个类进行扩展。值得一提的是， comments pull to 为 pulled object 定义了若干种的状态。有这么多，看着比较容易蒙，我从网上找了一张图帮助大家理解，继续写代码。这里我们使用 default poor 的 object 就可以了。


ceremony 用money，类型是 u s d 美金，又一个 big decimal 1 美金。由于 money 的创建非常慢，所以我们也使用 thread 点儿sleep，睡个 100 毫秒，模拟非常慢的场景。这样 make object 就编写完成了。为了比较好的跟踪对象的状态，我们打个日志。Logger。 log factory get a longer。
看一下。日志叫做 make object。State。object，点儿 get a state 就可以打印对象的状态了。 return object 其他的方法我们也打印下日志。
validates 返回true。单日志。


目前我们先只实现一个 make object，其他的方法暂时不实现，因为这个例子比较的简单，大家还看不出每个方法的实际用途，在下一节就会有比较深刻的理解了。现在我们就可以在这里传入，我们的 full object factory option enter。对象池创建好了，我们就可以对照 PPT 里面的核心 API 去操作对象池了。比如， borrow objects 就可以拿到对象了。拿到对象之后，你可以使用对吧，比如我重设一个值，变成了人民币，贬值了对吧？再把对象 return 回去运行一下试试看，这样就可以看出对象的状态是怎么样迁移的。


好，回到 PPT 简单总结一下。 comments pull two 还是比较简单的，它有几个组件。 object pull 是对象池的抽象，最核心的类是 generic object pull 以及 generic key 的 object pull。第二个组件是factory，它可以创建以及管理 poor 的object，一般需要自己扩展 poor 的 object factory。第三是 pulled object，它可以包装原有的对象传，让对象被对象池管理。一般我们会使用 default pull 的object。只要掌握这 3 点， comments pull to 就没有什么问题了。哪怕遇到问题也不用怕，只要从你所使用的 object 的破对象调用的方法开始追踪源码，比如 command option b，继续 command option b 就会看到业务逻辑了。


comments pull to 的代码写的是比较简单的，分析起来也不难。这里我们只探讨了 generical object 的pull。对于 kid object pull 这种类型的对象池，同学们也可以测试玩一玩。 API 基本上都是一样的，只是多了一个 key 的参数而已。好，这节课就到这里，谢谢大家。





