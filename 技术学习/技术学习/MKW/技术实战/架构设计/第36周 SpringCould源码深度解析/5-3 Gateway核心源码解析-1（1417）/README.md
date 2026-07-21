---
title: 5-3 Gateway核心源码解析-1（1417）
---

# 5-3 Gateway核心源码解析-1（1417）

这章节我们来介绍 spring code Gateway 的核心源码解析的内容，我们主要关注 spring code Gateway 它初始化的过程，初始化是如何我们把我们定义的这些路由的相关配置信息组装起来的，另一个就是我们 Gateway 作为网关，它请求处理的过程，那么我们作为网关接收到请求，如何经过一些规则判断最终找到我们对应想要的一些服务这样一个执行的过程。


那么首先我们来看一下我们的初始化过程，那么在初始化过程，我们刚才介绍的我们初始化主要也是涉及到了我们这里面的，像 road predict handler Mapping 的初始化，那么在初始化的过程它会依赖到对应的，像我们这里面是 root depends locator 以及 root locator，还有我们这 filting Web handler 以及 simple handle Adapter 这样一个初始化的过程。


在这里面其实我们因为我们知道斯文克 KTV 它是基于 Web Flex 的方式去进行初始化的，那么肯定它会涉及到比如说 native 服务的启动这个过程，我们在这里面并没有显示的去介绍，所以说我们就隐式的假设，我们对 spring 的 Web Flex 相关的内容是有一些了解的，当然我们在前面课程讲解过，那么这里面如果说我们想更多的去了解这个过程，我们可以回到这里面我们可以看一下当我们真正的一个 KTV 启动过程中，我们可以我们启动方式也是基于 stream licated run 的方式启动，那么启动的过程它最终会执行对应的。


我们这领域是 allocation configure negative Web Server application context，那么基于 ninety 启动的过程中它是我们要知道它对应的三下文对象是这样一个对象，这样我们看它启动的过程中，其实这里面主要是 reject auto configuration 的过程中，我们所关注的一些自动装配的对象，那么这里面像 Web Flex 里面的 reactive Web Server factory auto configuration，它在自动装配处理的逻辑主要就是我们看到这里面是它有集成的对应的Natty，通过集成 Natine 去生成我们对应的服务。


这里面有 waterflex auto configuration，这里面重要的信息点就是在启动的过程中，它会把 request Mapping， handler Mapping 以及 request Mapping handle Adapter 注入到我们的容器里面，其实这个也就是说跟我们 Spark VC 所对应的它的 handler Mapping handle Adapter。那么我们这里面对于使用 Gateway 的过程中，其实这里面比较重要的一点就是说相同层级的 auto configuration，这里面是 get way auto configuration，也就是说我们在这里面去介绍的。


那么在启动我们的 get way auto configuration 的时候，它注的事情是什么呢？是初始化了，我们的 Router predicate Handler Mapping 以及我们这里面是 filtering Web Handler，那么这里面我们关注的像 simple Handler weapon，它其实并不是在 Gateway auto configuration 所初始化的，其实它是在我们的 Web Flex auto confusion 在这个成绩去初始化的一个 simple handle Adapter，只是我们在使用 Web Flex 的时候其实并没有去关心它，那么在这里面我们使用 Gateway 的过程中，我们关心的 handle Adapter 就是 simple handle Adapter，那么在这里面我们可以把它我们把也列到这里面。那么其实还有我们在 Web plus 所注重的一些东西，比如说像 HDB handler auto configuration，那么在这里面我们的 Gateway 也是需要的，比如说这里面是 dispatter handler，那么我们的请求其实也是通过 dispatch handler 去接收这些请求。然后比如说我们通过 road predicate handler Mapping 这个映射找到我们的handler，进行我们的处理的过程。


后面的一些逻辑，比如说我们这注册完成程以后，我们看监听unphrase，在执行 unphrase 的过程中，我们可以 create Web Server，把我们的这个 Web 服务构建起来，构建出 Web Server 以后，通过我们这里面是 Web Server manager 构建出 negative Web Server 的taxary，得到一个服务的构建，它这样跟我们 despite handler 的构建出关系。最终这里面是我们的 Web share manager 进行启动的过程中，就把服务启动完成。


所以说在这里面启动完成以后，这里面对应的 despite handler，它会进行一些初始化的操作，这个初始化操作主要是涉及到我们这里面是 handler Mapping， handle adapt 以及 handler result handler 相关的一些内容，那么基于这样一个初始化的流程，我们程序就已经组装起来了。那么这里面我们重点去关注还是 Gateway auto configuration 的内容，那么关注 Gateway auto configure 的内容，其实我们聚焦一下，也就是在这里面是我们关注的是像 Router PRD k 的 handler Mapping，以及我们这里面的是 filter 和 Web handler 相关的内容。那么我们切到我们的源码里面去看一下。


首先在这里面我们打开我们的也是代码模块，这里面我们去看一下我们依赖的内容，这个我们跟大家讲，我们在这简单回顾一下，这里面我们依赖的是像 spring code start Gateway，也就是我们通过启动器的方式把我们的 Gateway 引入进来，同时这里面我们看到我们用的还是 spring Claude STARTERS Alibaba NACO 的discovery，无论就是服务助手注水发现。那么基于这样的话，我们去找我们最重要的这个 auto communication，也是这里面我们的 Gateway auto communication。


Gateway auto communication 里面我们比较关心的也就是我们的 router predicate and Mapping，我们在这里可以找一下，这面我们看一下 Router predicate 这样一个 handle Mapping，我们定位到这里面，对于这个 router predicate handle Mapping，它构建的过程，它其实就是把我们注入的参数直接构建就完成了，我们可以看到它需要的参数。


这里面是 filter Web handler，即这里面是 router locate。那么其实在我们构建的过程中我们可以看先看一下它的构造方法是做了哪些事情，在构造过程中，其实我们最终能看到的也就是它把这些属性的这些参数作为属性的一个赋值。那这里面对于像 Web handler 或我们的 roadlocate 赋值以后，这里面还涉及到一个像我们的 measurement port 和我们的 measurement Pod type 的进行一些组装。这里面我们可以看到对于我们的 media port，我们可以是专门去设置它的管理的端口号，同时也可以设置一批对应的，比如说我们的 manager Pod 一个type，一个类型，这个类型我们可以从这里面看到它支持的类型的方式。


这里面首先是disable，也就是说禁用我们的管理，另外是seam，也就是跟我们的提供服务的端口是一样的，另一个是different，也就是一个不同的服务端口，那么其实它在处理的过程也就是判断一下当前我们 Server 对应的一个端口号，那么获取的端口号看端口号不等于 now 且端口号小于 0 的话，就认为它是一个disable，也就是一个不可用的状态。


后面是我们根据也是根据端口化的情况去判断它是 sim 还是 different 一个这样一个过程，那么这是我们简单来看，它是 road predicate handle mapping，其次是构造方法执行的内容，那么其实在这里面我们主要关注的还是主装的内容，这里面主要是包含像什么 role locate 和 firefilting Web handler，那么我们再回到我们的 auto configuration 里，其实在这里面做一个 bin 初始化的过程中它的依赖注入，也就是说我们关心它 filter Web hunter 它是怎么构造的。


那么我们可以在这里面去找一下 filter hand，找一下它的实现，那么在这里面我们可以看到对应的是 filter Web handler，它这里面构造 be 哪个过程，其实它构造的过程我们可以看到也是非常简洁的，这里面只是依赖了 global filter，也就是说把我们全局的这些 filter 获取到，也就是从我们 3 下文获取到以后，拿我们的全局的 3 下文的 close filter 作为我们的构造参数，就把我们的 filter work handler 构建出来了。


这里面它的 Google 参数实现的逻辑也是比较简单，只是把我们的 Gr filter 作为一个属性进行一个配置，但这里面是有一些处理的这么个处理词，把我们的 global filter 进行 load filter 做了一层处理，在这里面主要是做的事情是什么呢？也就是说它对我们可以看到这面的实现，其实在实现的过程中，主要是对我们的order，也就是我们的排序的顺序进行了一些调整。当然不能说调整，应该是对我们的 Gateway filter 进行一个 order 的一个包装，也就是说我们所有的这个 global filter，它在这里面都支持一个顺序的order。


Gateway filter 也就是支持一个序号，因为我们在执行 filter 的过程中，它肯定会有一个顺序的一个这样一个支持，这是我们在构建的 Tutor Web handler，这样看起来是它并没有涉及到太多的内容，那么其实我们看还有就是这里面的 roll locator，对 root locate，也就是说我们的路由定位器，那么对于路由定位器它处理这里面会涉及到好多路由定位器，那么我们可以在这里面去查找一下。


首先我们， road locator，我们可以看到在这里面我们首先我们可以看到这里面，这是我们比较关注的，这里面是一个 cats 的 compose 的 road locator，我们可以看到在这里面对于 road locator，它的依赖的参数是一个 list road locator，那么得到这个 list role case 它进行了两层包装。


第一层包装是我们是这是一个组合的roadlocate，也就是说我们把整个上下文里面所有这些通用的 roadlocator 的这些 being 会获取成一个list，在 list 里面包装成一个compose，一个主合的roadlocator，那么这个主合的roadlocator，它其实在外层又包装了一层 cacting road locator，这也就是我们刚才介绍的，其实我们在使用真正我们使用的roadlocate。


这里面我们看这里面标明了primary，也就是说我们使用默认的依赖注入，我们注入的就是这个 cats 的 compose 的 root locate，也就是说我们基于缓存的组合起来的这个 root locate，那么这里面我们真正用的是它，那么其实对于 road locator 它其它的一些实现的，其实我们这里面可以看一下这里面 road locator，它默认的我们这里面是 road technison road locate。也就是说我们通过我们这个常规的 road locator，它是基于我们的 root finishing，也就是我们的路由定义配置文件的 root locator，查找获取到的就是这两一个映射关系。


我们通过 root definition root locator 去获取到我们的这些路由定义信息，那包装完成以后，最终组装到这样一个使用的 primary 的一个 root locator，其实在使用的过程中我们可以看到这里面我们看到它依赖了哪些内容。


其实比较复杂的是构建这个 road definition road locator 的过程，它依赖的东西是比较多的，这里面我们可以看到它依赖的是首先 get with property，就是跟网关相关的一些属性配置，这里面还涉及到 get with filter factory unifactor，这里面还涉及到像 road predicate factory 以及我们这面 road definition locator，通过 road definition locator 还有这里面一些 configuration service 以及配置的一些服务在这里面构造出。


我们可以从这里面去看一下它的参数是非常多的，这里面除了对于像我们参数的赋值以外，我们可以看到这里面涉及到像 init factories，这里面的 factor 主要是基于这些断言的这些构建和处理，这里面还要涉及到 Gateway filter factor 的一些处理，在这里面处理的过程其实我们可以点进来去跟进来看一下，这里面在处理这个 root predict factory 的过程中，主要是我们把 factory 它进行获取它的name，判断一下 predict 在集合里面是否存在。如果说是存在的话，它会打印相应的一个警告，那么其实会做了一个替换。我们可以看到 predict put key 和 factory 把对应那个名称去进行一个替换，也就是放到我们当前的一个，这是一个 map 集合里面， map 集合，我们在从这里面去看，这里面是像 get 为 filter package，它相当于是我们直接在行级的去做了一个 for 意思的操作，它处理的内容其实跟下面这个 factory 的处理类型是一样的，也就是说把当前那个 factory 进行一次迭代，把它放到我们 get factory 的这个集合里面，也就是一个 map 里面。在这个 map 里面我们也是获取到它 name 和 factory 去做一个引用，这样的话我们这个 root definition， root locator 它也就构建完成了。


这里面是我们可以看到它是这个 Roter locator 的一个构建的过程，其实里面还涉及到了其他的一些内容，比如说我们可以看一下在这里面我们对应的是 Mint info，下面我们的 spin factory 还有哪些 auto configuration，这里面我们提到像 Gateway class pass warning，我们可以看一下它的实现的过程，在这里面实现的过程其实也就是在启动的过程中，如果说我们的 3F 环境能满足当前这个条件？我们看一下这个条件是什么？这个条件是，首先我们这里面是 condition on class，也就是说我们当前的容器里面，如果说找到了 dispatter Server net，我们知道 departure sweat 是 SPA M a C 一个比较核心的组件，那么如果说我们在上下文发现了 departure swenet，也就是我们会打印一个警告。


其实我们知道我们在使用 way 或者是 Web Flex 的过程中，它都使用了我们的Netty，那么 Netty 呢？这里面我们使用的是 Web Handler，而我们在程序里面是不应该依赖 Dispatch showletter 的。所以说如果说依赖到了 dispatch 叉 line 的，那么就说明我们的依赖过程是存在一些错误的，但是它并没有去阻断我们执行，它只是在这里面给我们打一个警告，这警告是我们看 stream MC found on class pass，也就是在我们的容器里面，我们的类路径里面找到了 Spima c 相关的一些配置。这个它是我们可以看到它跟我们的 spring Claude v 是冲突的。在如果说相同使用的话，这里面是 please remove 我们的 spring boot sort of Web dependence，也就是把我们跟 spring VC 相关的一些依赖把它移除掉。这就是说其实在 spring 它或者 spring code，它们在构建这些模块之间的这些依赖关系，以及它们的一些冲突检查。

