---
title: 1-4 Spring WebFlux架构设计解析（1358）
---

# 1-4 Spring WebFlux架构设计解析（1358）

[image](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/d2b24378-6ce3-45fa-8c6c-818d0db2057d/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RYQ6PSXP%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T232000Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDzJNS7PMhgHeC5QHFmb731SYniEQj6AjhNQYP5qjF0gwIhAKnyK5f0nza%2FhKZ%2FZRfqNtj%2BHI9QU0WwQyKmtc3jRZKSKogECMb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgzDUg441SocKU3C5ssq3AOl9oYuDcplJ5upd5r8jsR%2BdUUOr%2ByVvOfUs6epbhyi9XwpSjeZGuvZ5MZP%2F%2FvHkxgsUWusePAmfyfEpAXllz8RS2ZMwGlHUlIZPtzr0MkAFrNEF9%2FiPNZbW9X%2BEEwzrkh8eMca7BpdsQkk9Qml7gF48%2BHFHy1WZmWIcEYl2mEyxTY3YlKEOdK08dYc%2FuqSnGtTBe2HqdjREhtp5nomX9OMNsLSk0jMXaUEF5jf0SLwPjX3WLST65kn5wNQcU8klwcAkUHUkj0y2Ljj7bxTA7sqQnuVN%2BzQda%2B%2Bla1NiG%2Fp9phMNnTY%2BNFX43GGctPuCbgvEERubYKCKEX1jp4oqgHDTwWR5%2B4%2Fk4uCNY3B2t%2BJb%2BDv1XhsTZ5XZcaxhO53lKM4Tgi0ChmtYgk108Kp5oovPYfWRlsLwCBCiKejwSeJKOVJLRzi0UFgpxSqY%2BF3DPvf2pXt6CvEFK%2FMkf2PJGDfet1%2B0306UXKORSKzKTBfdzH3sjol%2F7FsNJQ3lxsRiCWaKxCryll621x3ZYm%2FLK%2FqUB1TANo6yYmsTu3L2z8GpPAWwUpsKSjYG%2BgQeWU0CNfSEaca%2BqNyvRb%2FipnxbOa3Ul2KEsRYNZH2qCBq37qIKiO%2B1Dw2mT%2B8tdHppzCEu%2F%2FSBjqkAVHWPQx1k4gt84n89gc%2FCZrh9r6lbBBqmvFKflAiNuBSzS%2Fqg73aVoe8Ozjwu1gywKhogyDTqM7srFxsovY48rwKPzllxMkFLJxbD25PURmcBZ0fSJ0FxIbka97s3QUf4pXAI2QBvly5CVghwoEYDQLs91qpn1c2%2F%2FwaUEdecOO8IOa8lpO11YQB903%2F1seZrUB2DZ6wGR%2FgGv0UnpqKANhYIiux&X-Amz-Signature=150ea0bde3cb1eb5e53e72cf8cd6deb054d204ae0c2ae863480adf17c78aab04&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

同学们大家好，这章节我们来学习 spring Web Flex 架构设计。 spring 5 case 提供了 spring MVC 和 Web Flex 这两种 Web 技术栈。此外， VC 经久不衰，大家都比较熟悉。 Web Flex 诞生不久，它主要在应用层面充分向异步和非主塞的方式去发力。向阳四异步非主塞编程相比同步，主侧编程的门槛会高很多，这不仅是对软件开发人员有较高的要求，同时它要求我们有一整套的技术栈来支持相似异步的实现。响应式编程现在逐渐成为一个热门词汇，大家也承认想要是编程是未来的趋势。


在这里面我们从三方面来介绍 Web Flex 架构层面的内容。首先我们要了解什么是 Web flags，这里面我们主要通过与 spring Web Mac 对比着来学习分析。第二节我们通过比较 spring Web Mac 与 webflags 处理过程的区别，来学习 Web Flex 的特性。最后我们通过实例演示 spring Web 工程的工程实践。


好，首先我们来看什么是webflags。 spring 的 Web Flex 它是一个异步非主侧的外部框架，它能够充分利用 CPU 的硬件资源去处理大量的并发请求。 plus 的内部，它使用一个响应字编程，也就是我们 reactive Programming，以 react 库为基础，基于异步和四件驱动，让我们在不扩充硬件资源的前提下，提升系统的吞吐量和伸缩性。
这你要注意， Web Flex 它并不能是接口的响应时间缩短，也就是说针对具体的请求，它不能让响应变快，甚至在一些场景会发现响应时间会变长。它的好处主要是提高系统的吞吐量，让我们系统的资源利用率提高。一些适用场景特别适合在一些 l 密集型的服务中，比如说像我们微服务网关这样的应用中，对于微服务网关，它只是对于数据的输入输出，一般很少有计算功能，所以说这种 l 密集型的是非常适合我们使用 Web Flex 的。那么我们再看一下 spring VC 和 Web Flex 的关系，在这里面我们看到对于 spring 提供的 spring VC 和 spring win Flex 这两个技术栈，它们的特点，对于 spring MVC 来说，它是一些简单的业务逻辑，也比较容易写入和debug。它主要依赖于像GDB，CDPA。主要这些我们是可以理解为主设的一些基础站。


对于 spring Web Flex，它主要基于函数编程，我们基于四件轮询的方式。对于它来说，像 Netty 这种特征的数据要提供一些服务的支持，当然它们之间的共性我们可以从这里面看到。 spring VC 和 spring Web Flexin，它都支持通过 control 和 request Mapping 的方式去做一些资源映射，同时它都可以去向 Tom cat 跟载体都可以提供相应的支持。这里面需要说明的是，像 Tom cat 和 Jetty 这样的 serverless 容器，它是需要依赖 serverless 3. 0 以后字词异步的方式才能提供 Web Flex 方式的支持，我们接下来看一下对于SPRAM， AC 和 Web Flex 他们的技术栈，我们这里面可以看到是主色型的和我们非主线，这里面是 serverlight 的技术栈，这里面是 active 的基础栈，同时他们支持的 Server 服务我们可以从这里面去看到。对于MVC，它主要是 serverless 容器，对于我们的 Web Flex 它可以兼容 serverless 容器，再加上我们摘体相关的内容，这里里面我们可以看到它是对于容器是版本有要求的。


sweat 3. 1，同时它支持的这些技术的原型，我们这里面可以看到对于 control request Mapping，同时 Web Flex 它也支持 control request Mapping，它支持对应的 handler 和 router function 相关的一些内容。


我们在搭建两边的服务的时候，如果说我们使用 spring boots 的话，我们可以看到 spring VC，我们需要依赖 spring boot standard wipe，我们 one Flex 它是需要依赖 string 布的 starter Web Flex 这样一个功能。


接下来我们看一下它执行的过程，其实也是我们基于 m a C 和 Web Plex 它对应的 THREAD API 和这里面 spring Web API，这里面是 negative 和 negative stream 这样一些四减流。对于 throughout API，我们可以理解为它是一个主色型的，它基于它们开的代替提供服务。对于我们 Web plus，它是基于 Ninety 或唐姆凯的chat，也就是对于版本要求高版本的一些，要通过这几方面大家去理解。


对于我们 spring VC 和 spring Wireflex，它两个最大的不同处也就是一个是同步，一个是异步。那么如果说我们对于使用开发我们 Web 程序如何选择 Wemac 或 Web Flex？首先 Web Flex 它不是 MA seed 替代方案，它们各自拥有自己适合的一些应用场景，那么我们可以聊一下如何选择。


如果说我们的应用程序它没有性能扩容方面的问题，或者说横向的扩容伸缩成本并不高，那么其实我们没必要刻意把我们的 m a C 程序修改为whatflex， m a C 程序的代码是编写比较容易于理解，并且 debug 调试也比较方便，等大家逐步的回归理性，根据业务去选择技术。大部分应用程序使用 m a C 是足够应用我们的业务场景的。
如果说我们的团队已经拥有一套非主色响应的技术栈，也铁了心需要转非主色的显象磁技术栈，那么 spring Wireflex 它作为 Controller 层的是比较适合的场景。目前的技术栈主要主题是在数据库层面，我们的交易系统常用的关系型数据库对显示的编程都不太好，不过他们也在全力适配。像 MySQL 已经提供了 r two d b seed 驱动，还等待市场的检验。像 Oracle DB two 这类比较重量级的数据库，支持 r two DBC 肯定会有一定的时间周期的。


我们的微服务体系中，我们可以单独的使用 stream IVC 或 stream Web Plex 对应的control，当然它们也可以融合在一起使用，因为这两种框架它都支持相同的基于注解的编程模型，像我们的 add control 和 add request Mapping，这在某种程度上也降低了我们使用 Web Flex 的启动门槛。


评估一个应用程序，一种简单的方式就是检查一下它的依赖关系，比如说我们有主色的刺激化API，比如说 j p 和 j d b c，或者一些网络上其他的一些 P I。那么其次 Spam VC 就是我们当前最佳的一个选择。如果我们作为客户端调用远程服务的 spam v c 程序，这样我们基本上可以无顾虑的考虑切换到响应式的 Web client，它可以直接从 smarac control 方法返回响应类型的转化成对应的 react 的对象。


对于那些延迟性比较大的接口，我们转化为可以观察到的好处是非常明显的，如我们的团队规模非常大，在向非主色式函数式声明式编程的转换过程中，学习曲线是非常陡峭的，这个大家一定要有一个心理准备。那么对于我们来说应该怎么做？就是接受 Web Flex 带来的变化，我们一定要能快速学习，快速上手，等待合适的时机我们发挥自己的作用。


好，接下来我们来看一下使用 Web Flex 的工程实践。对 Web Flex 的功能项，我们首先去介绍一下 Web Flex 的工程结构，其实这个跟 three MVC 是很相似的。其次我们看一下 control 它的方法特征以及我们的单元测试。


接下来我们看一下 spring Web Flex 的工程结构，在这里面我构建了一个 spring Flex 这样一个model，我们还是先看它的 palm 文件，在 palm 文件里面我们可以看到我们这里面是使用了 spring boot started 的 Web 依赖，这样可以减少一下我们添加依赖的复杂度。因为 Web Flex 对于大家来说大多是新的，我们通过基于 spring boot 的方式去了解它，可能会更快速的去上手。这里面像我们是 spring boot STARTER whatflex 朗姆不可，同时我们添加了我们的单元测试分布的 star test。注意一下，对单元测试的时候，对于react，我们需要添加 react test 这样一个 scope 为 test 的依赖，这是我们的依赖文件。相对来说，我们使用 smoke 的 starter 就会变得非常简洁。
接下来我们看一下这里面的application，我们的入口类也是跟普通的 stream 布的工程没有什么区别。我们在这里面整体看起来是非常简单，主要我们看一下最大的区别是什么呢？我们可以在 Web Flex configure 的话，这里面的区别是跟 through m a C 是有一些区别的。对于 spam v seed 话，我们是继承了 Web m v seed 


configuration，对于这里面我们是继承了是 Web Flex 的configure，我们是 enable Web Flex do you use my messences enable web mec。其实这里面接口的实现跟 Web x 是很相似的，这里面是配置一些跟 Web Flex 相关的一些内容，我们也是 COS 的 Mapping 颜色和 formator 和一个 resource handler 等相关的一些操作，这个总体来看跟 MA seed configure 很相似。


我们接下来去看一下我们 Demo Controller，对于这个 Controller 的话，这里面的内容就是看起来很像，但其实有一些很大的不一样。一些注解， rest control request，Mapping， m a C 和 y Plex 的支持也是一样的。


这里面唯一的区别我们可以看到，在这里面我们在执行操作的时候，我们的返回值是个Mono，对于 Mono 或者是 Flex 就是以支持 react API 里面的这些数据流的发射器。在这里面我们去构建了一个 user 对象，我们通过 Mono just，也就是说发射出一个对象出来。对于这个 Mono 它其实就支持了我们对于系统异步的操作。


那么接下来我们去看一下单元测试的效果。对于单元测试我们是依赖是有一些变化的，我们这里面是使用了我们 string 不得提供的分片儿特色的方式。这里面是 Web Flex test，当我们在启动这个单元测试的时候，它会给我们构建一个 Web 的 test calendar，我们通过这个 calendar 对应我们 Mac 工程的 mock Mac 我们可以通过它去构造我们的单元特色。在这里面我们通过 client 执行get，我们就获取到一个 get 的方法，它也可以获取 post 对应的 post 的方法。通过 get 的方法，我们去设置我们的URI，这个 u r 里面我们可以去通过障碍符的方式设置我们的参数。最终我们可以设置一些我们 accept 我们的 media type 类型。通过这里面看，跟我们的 SMB 是很相似的。完了之后我们执行exchange，我们会得到一个response，一个 SPE seed，一个对象。通过它我们去做我们的断言操作。对于断言操作，我们可以在这里面是 expand states，也就是看我们的返回向阳状态是不是 is okay，就是对应的是不是200？同时我们可以去获取到我们的body，我们的 body 信息，去通过 json pass 去校验返回的内容是否相似。


跟我们 MA seed 单元测试也是类似的，我们这里面是指定我们的 name 去执行它是否等于我们设置的机密。现在我们可以执行一下dialentist，看一下执行的效果。现在我们可以看到这个蓝色条其实就是单元测试执行。通过这样看的话，我们在做 spin Web Plex 是不是看起来很简单，其实它并不简单？这是我们在这里面给大家演示了一些最基本的一些功能。


对于我们在写我们的 Web Flex 工程的话，最重要的像 Mono 和 Flex 它们之间的概念大家是需要逐步去学习和了解。这里面对应 Flex 的一些内容大家应该知道，对于 Flex 它代表 0 到 n 个这样可以触发的一些信息源。对 Mono 它可以发送 0 到 1 个这样的一个信息源，它里面提供的功能跟我们 x Java 和我们的数据流相当中很相似，但不同的就是它们这些异步的操作的一些过程管理。其实我们还可以通过另一方面去比较一下 control 和我们这个 Wifi likes Mac 的话，我们找到最原生的这个control，我们可以看一下。


在这里面我们看到这个接口control，对于这个接口control，它提供的一个方法就是 handler request，对于这个 handler request，它提供的它的参数就是对应的 HTP Server letter request 和我们的response，它里面抛出对应的异常，那么其实这个就是最早期跟我们 Server 的 API 很接近的，它支持的输入输出对应的参数，它的输出是 model 的view，也就是我们 MVC 最早的一些概念。


那么基于 Web flags 它最根的一些节点，我们可以参考一下我们的 STP Handler，对于 STP Handler，它作为我们 CS 5. 0 以后提供了这样一个接口，我们看它的 Handler 的参数也是 let ITP request 和 Server let t p response，我们注意一下这两个是不一样的，这是 LTP Server 的request，这是 Server LED entity request 就是大家区分一下它两个参数的不一样，另外它的返回值的不一样。


返回值我们的 Controller 对应的是一个 model view，这里面我们是 model 这样一个异步的一个思想的对象，所以说对于我们 Web Flex 里面有很多一些知识点需要我们去挖掘。好，这章节我们先介绍到这里，同学们，我们下一节再见。

