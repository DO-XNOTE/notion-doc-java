---
title: 5-2 Gateway架构设计-2（1757）
---

# 5-2 Gateway架构设计-2（1757）

beans 以及我们的 global field beans，其实这个是非常重要的，因为我们在 Gateway 网关请求的过程中，所有的这 global filter 它都会去生效。另外这里面还有 predicted factory beans，我们可以看到这个内容非常多，也就是说我们支持这个断言的这些 factory being，它是实现非常多。


这里面还有我们对于 get away filter factory beings，也就是我们定义了一些默认的一个 filter 的一实现，就是说 string code get way，它给了我们很多比如断言的实现和我们的 filter 实现，我们在配置我们的路由的时候，可以基于这些去来进行一些实现，会检测简化我们的一些实现的一些难度。其实这里面是还有 Natty configuration，也就是说在我们虽然网关使用了，底层使用了Netty，这里面还给我们扩展了一些。


net 相关的一些配置相关的信息。这里面比较重要的，也就是说真正我们向外发出 HCP 请求，也就是说我们发出代理请求的时候，在这里面一完成。这里面还有像 Gateway occur confusion，这个是比较容易理解的，就说我们在 Gateway 向外暴露一些 endpoint 过程中，是基于它这里面去定义的。好，这是比如一些 token 相关的一些认证相关的一些信息，那我们可以在这里面我们跟到这个 get auto configure 里面去看一下，我们可以看到这个类它其实还是比较复杂的，我们看一下它的一些信息。这首先这些它的内容比较多，它定义了很多beans，这里面像Adapter，chats，bot， global filter 以及 add request head 等等，这样我们现在看到它因为是基于字母排序的，所以 a 在前面。


这里面还有一些像 off 的时候的 predicted practice 以及 before 等等，这些可能大家的感知度还不是那么强，我们看它底下还构建了一些纸类去构建，这里面我们看到有 get away， a creator configuration 以及 native configuration 以及等等这些 token really configuration，其实我们看到这里面的内容的时候可以在里面，嗯，去过一下，其实它里面还做了一些分类，这个分类我们从这里面看。


首先我们向这里面走一下，这里面这是我们比较重要的，像 root locator，这里面这个 root locator 它是基于 catch 型 root locator，也就是说其实我们在网关执行的过程中，它不是每一次都会去把我们整个 root locate 去遍历一遍，它是通过一个缓存缓存的 pass 去缓存起来，我们可以从缓存更高效地去找到对应的router。


这里面像是 root refresh listener 就是我们刷新的一个过程， filtering Web handler，也就是说这是我们在其实通过我们对应的 Mapping 去找 handler 的过程，我们找到的对象都是这样一个固定的对象获取到的 filter Web handler，它可以获取到我们对应的路由，通过路由里面能找到这个路由相关的这些 filter 以及我们的 global filter 组装起来，去进行我们一些相关的一些处理。后面这里面是像 router predict handler Mapping，这是我们最重要的，它是通过这个 handler Mapping 找到对应的内容的。好，我们可以看到这里面是对应的像一些共性的一些信息，比如 configure property，对应一些属性的一些配置，这里面有 ITP handler filter。我们看这里面是我们这里面定义的一些 global filter，这里面像 badcase cats 以及 remove cats 等等，这里面像 road to request URL 这样一个转换的一个 filter 等等。这其实这些 filter 它在执行的过程中都会根据当前的场景进行判断是否生效。


看这里面 forward routing 和 forward pass 等等，这里面还要像Websocket，假如说我们像 Websocket routing filter，假如说我们在配置路由的过程中用到了 Websocket 的协议，那么它会经过 Mobile SOCKET 相关的 filter 中转。


这里面会有一些像我们一些断言的 factory 的构建的一个过程，这里面像 off 的 Router 和 before Router，以及像 between 等等一些操作。这里面有跟 cookie head 些，也就是 head 相关的一些信息。对面 host 好，我们就简单先了解一下我们这个 get away auto configure 里面的一些内容。


接下来我们来看一下 get way 的一些核心概念，对于像 spring code 概念位，它最重要的概念也就是路由，这里面像路由，其实在路由里面它会定义一些属性，其实这个 Router 它会通过一个 Router DISN，也就是 Router 定义的一个类去包装过来的，转换过来的。对于一个router，它里面包含像ID， URL 和我们的order，一个排序的一个顺序等等。这样另外还有几个比较重要，像这里面predicate，也就是一些断言的信息，以及我们 get the filter。


这个 predict 断言信息是通常我们的请求参数里面一些带来的信息去进行一些匹配，匹配到我们对应的一个router，也就对应到我们那个路由。另外这里面是 Gateway filter， get filter 它做的事情主要是判断一下我们当前这个路由处理的一个逻辑是怎样的。我们有默认的 global filter 以及我们对这个 router 定义的这些 filter 都可以处理，当然对于 router 里面相关的一些 mint 字的信息也是包含进来的，那么这里面我们对于 predicate 和 filter 也是比较重要的，我们可以一会展开来说一下。


对于 predicate 的话，我们可以看到，首先 predict 它自己是本身包含一些操作的，比如像 and negative 以及 not all，这是一些逻辑的一些组合。其实对于 predict 它也是由一个 predict definition 来构建完成的。对于这个 predict definition，它里面通常有 name 和art，也就是说有先有一个这个 predict 的名称，再加上它的一些参数信息。
通常对于我们 Gateway 里面我们用的是 single predicate，对于这里面官方也就是 spring code Gateway 也提供了一些默认的 Router predicate factory，这里面我们可以通过前缀命名，通常比如说这里面是 pose road particular factory 以及 host road project factor，刚才我们在这里面我们可以看到，也能看到这里面是 header host 等等这样一个效果。那么我们通过这个命名也就可以简单的理解到这个 PRD k 的它注的作用是什么。比如说像 POS 一个路径，我们基于路径去判断一下跟我们的路由信息能不能匹配。host，也就是我们的域名以及我们的 must 有我们请求的方法，比如说guide，还 post 或者其他等等。


当然 head 里面会储存一些信息，包括我们的一些校验信息，或者一些隐藏的相对隐私的一些信息。 query 就是我们常用的一些参数。 cookie 我们用的是比较多的，我们一些认证的session、会话 ID 等等，可能会放到 cookie 里面，这里面像 OPT before between，这是我们的一些计算逻辑，我们可以理解为它，比如说它会跟某个数字或时间进行一些比较。这里面 remote a d i，这就是我们的 IP 信息相关的一些内容，这是我们可以看到是 predict 相关的一些内容。


那么接下来我们来看一下filter，其实 filter 其实里面东西是非常复杂的，我们这里面并不能把整个 filter 全部的内容列出来，这里面我们需要关注的也就是整个 filter 的构建，它也是基于 filter definition 构建出来的。


filter definition 也是包含我们的 name 和我们的一些参数信息，通常 filter 我们可以包含为 Gateway FILTER 和 global FILTER，那么对于不管是 Gateway FILTER 还是 global FILTER，它在整个我们请求的逻辑处理的过程中是并没有什么区别的，他们的顺序也是基于他们 order 顺序进行一个排序，其实这里面对于这些 filter 也提供了很多，像这里面 get away filter factory 提供了很多这里面比如像我们这也是一个前缀的一个截取，比如说 add request header 它是什么意思？也就是说当我执行到这个 filter 的时候，我把一些请求的信息添加到这个 header 里面，这里面比如说 map request heal map request，这就是说当如果说我的上下而信数据接口发生变化的过程中，我可以对 header 的这些 k 和 value 进行一个参数的映射，主要做这些，下面这个也比较容易理解，它就是说我们可以在请求里面添加一些参数 a parameter，或者说在响应里面添加一些 header 相关的一些信息。这就是我们 filter 处理的一些内容。那么接下来我们来去介绍一下我们 get way 这个流程初始化的过程。


其实我们知道我们的 spring code Gateway 它是依赖了 spring 对应的webflags，那么所以说对于这个 Gateway 初始化的过程，它是依赖的我们的 Web Flex 初始化的过程，如果说大家对于 Web Flex 的初始化过程还不是很熟悉的话，我们可以回到我们的介绍 Web Flex 章节的内容，去了解一下它初始化的过程。像 Web Flex 它初始化的过程跟我们 SPM v c 初始化的过程也可以进行比较的去学习。


这里面我们重点去了解 Gateway 相关的信息，这里面我们首先它会去构造我们对应的 router predicate handler Mapping，也就是我们所有的请求，也就是我们在请求过来以后，我们对应我们的 request 信息做一个k，去通过这样一个 Mapping 里面去获取我们相关的一些handler，那么对于他去获得 handler 的过程中，他获得所有的 handler 都是 filter Web handler，那么基于我们 filter handler 再通过 simple handle Adapter 进行执行，那么就去可以执行到我们一些 filter 相关的一些信息。


那么所以说在构建这个 router predicate handler Mapping 的过程中，它需要哪些信息？你看这里面首先对于 filter Web handler 它是需要的，那么这里面对于 filter Web handler 它里面还依赖了 global filter，那么这里面如果说我们进行路由定位，那么它会需要到 router locator，也就是通过一些路由定位信息，那么这里面我们可以看到它定位信息会包含像我们的 road particular factory 以及 get way filter factory，也就是对于这个 road factory 里面，它里面涉及一些我们像路由的一个定义信息的一些查找，以及我们的 predicate 相关的一些信息，以及我们的 gateway 以及 filter 就相当于是我们的路径相关信息。对于这里面它会派定一些我们配的一些属性相关性，包括一些上下文信息，那么基于这些信息构建出我们的这个 handler Mapping。


我们构建完 handler Mapping 以后，那么我们看一下具体的，比如像我们的 root depends locate 它是怎么操作的，其实它主要的功能就是我们查找一下我们在配置所有的这些路由的一些定义信息，那么把它给相当于是组装在我们的 handle mapping。那么对于这些路由定义信息，它有包括多种方式，这里面像其实最主要的就我们 property route definitely locate，也就是首先是基于我们的属性文件配置的一些路由定义信息。另一种方式我们看这是 discover client，也就是我们通过注释中心获取到这些我们注释中心对应的这些路由信息。


那么另一种方法我们可以看到这里面像这是一个组合的，也就是说我们不管是我们是通过注册重新获取的，或者我们竖向解析的这些路由配置信息，都会组装成这样一个组合的一个 load depending locator。最终我们对于组合，我们为了它的执行效率，我们还会有一层缓存。


基于 CACHE 的一个组合，其实我们可以理解为最终成为执行的时候，首先是调用 CACHE 的定调用组合的，通过组合里面去看，里面的是辅助的预发现以及我们的 property source，就是我们的是配置文件的一个定义的这些主要信息，那么我们所支持的得到了我们的路由定义的 locator load definition locator 就是查找我们的路由定义信息，那么基于路由定义信息我们可以获取到我们对应的 Roter locator。


那么这里面我们看对于以一个对应关系，这么一次基于缓存的和基于一个组合的，后面就是我们的 filter Web handler，对于我们也知道 filtering Web handler，它实现了 Web handler 接口，那么就是它可以通过 handler Mapping 找到这样一个对象，基于一个 handle Adapter 基于用处理其实这个对应的 handle Adapter，在这里面我们使用到了是 single handle Adapter，它进行一个简易的一个处理。


其实在 simple handle Adapter 处理的过程，其实这个过程组装完成以后，初始化的工作就执行完了，那么我们找到handadapter，我们的 Web handler 通过 handle Adapter 执行的过程，就是我们相当于请求处理的过程。那么下面我们来看一下请求处理的一个过程，通过 spring Claude guide 为官方的这张图宏观的去了解一下，其实也是一个回顾，因为这个图大家也都比较熟悉了，也跟大家介绍过。


首先我们作为一个 Web 服务端，作为一个 get way 的client，去请求 get way 的过程中是这样，当请求 spring 库的 get way 的过程，首先我们会去找 get 为对应的 handler Mapping，也就是我们刚才介绍的 handler Mapping 中 handler Mapping，因为我们在初始化的过程已经把这些路由定义信息组装到我们的 handler Mapping 了，我们可以通过 handler Mapping 它里面的这些断言信息的一些判断，找到对应的我们的一个Router。


其实这里面还并没有找到Router，因为这会儿我们找到输的都是一个统一的 filtering 的 Web handler，那么机制 Web hunter 进行去组装，通过 hunter 他去找具体的一些Router，也有具体的路由通过路由信息找到这个路由特有的 filter 以及这些 global filter 进行一个主包，主包完成以后，剩下的就相当于是我们要去走 filter 进行处理了。


那么这 filter 处理的过程中其实有一个会对应的，比如说我们不管是 ENTB 协议，还是比如说我们的 Web SOCKET 协议，或者一些其他的协议，都涉及到一些外部调用，这些外部调用它都会对我们的外部调用进行一个包装，比如说我们是 ITEP 的调用 Web SOCKET 的一个调用，也或者我们是基于 load balance 协议、 LB 协议进行调用，它都会进行组装，最终会调用到我们外部的这些服务。


在这里面我们看到是这里面是基于成代理的服务最终的请求逻辑，也就是通过 get weekend 进行请求，这里面经过 handler mapping 到我们的 Web handler 以及我们各城 filter 组装执行完成以后，响应回去，把我们的数据返回过去。那我们看基于这些源码级的这些主线，我们来去看一下，这里面我们看一下我们执行流程所涉及到的一些过程。


首先其实我们请求过来以后进行执行的过程，他会首先找到我们对应的 Router practice handle Mapping，其实我们知道对于 Web Flex 里面它会定义了多个 handler Mapping，那么我们的请求可以通过我们的 handle Mapping 去找到对应的一个映射，那么找到对应映射以后，它会通过调用 get handler 对应的 handler internal，以及这里面最终是 lookup router，也就是找我们真正的 root 信息，这个找 root 信息的过程中其实就是依赖到我们的 root locator 去找，也就是 root locator 它去查找的过程。我们可以看到这里面是这些对于 root locate 的一个包装。首先我们直接调用引用的是开启型 root locate，它基于缓存的率查找，它底层会调用多层的一些代理。比如说首先是一个主合的 root locator，那么主合的 rocator 里面它会依赖到我们的 root definition root locator，以及我们这里面是 road locator builder，也就是我们基于 road locate builder 可以自己定义一些信息，就是我们在程序里面去定义这些路由映射的时候，去基于这个 locate builder 去定义的。


那么这里面其实我们更关注的信息，我们基于像 root definition， root locator 定义查找的过程中，它其实也是一个对应的关系，它这里面我们刚才介绍了像这里面基于属性配置的，基于服务发现配置的这样一种我们的路由定义信息的查找。


其实这里面我们在获取的过程中，我们获取的对象也就是我们的 filter Web handler，得到这个 filter Web handler 这样一个 handler 信息，它会通过这里面的 simple handler data 进行执行。


其实这个 simple handle Adapton 它处理的也比较简单，它只是拿到对应的 Web handler 进行一个 Handler 处理，就是调用它的方法就行了，其实就是一层适配调handler，真正调 handler 方法的过程，其实这里面实现的是怎么说是比较巧妙？在这里面我们定义了所有 filter 的一些过滤页操作，这里面它会构建出一个 debug get v filter chain，也就是说构建出一个 filter 链，基于这个 filter 的一个链来去进行一个链式的去调用。


这里面其实它组装这个 filter 链的时候，它会用到了这些 get v filter，这里面包含我们针对这个路由本身特有的，以及我们这些全局的这些 Gateway filter。那我们看一下这 Gateway filter，我们可以简单看到这个 Gateway filter 里面，这里面我们涉及到两部分，一部分会通过 root 点 get filters 去获取到跟当前的这个路由紧密相关的，也就是基于住路由配置的filter，另外就是我们 global filter 去定义的，那其实我们在配置的过程中，我们在执行的过程如果去跟一下 debug 代码，我们会发现我们通常会依赖到这些filter。


像这些 filter 其实我们比较关注的是哪个？我们作为一个网关最重要的功能是接收请求，匹配到对应的路由，那么这个路由做的过程就是我们把数据向下游发起，得到数据以后再想要回来，那么在这里面真正去进行我们数据请求，也就是 LP 请求的操作，其实在这里面是基于 native routing filter 去完成的。


基于 natty routing filter，它这里面依赖到我们的 STP client Connector，也就是它会构建一个 STP 的一个client，基于 g client 进行一些处理，那么如果说我们基于的是我们的 Websocket 协议，那么可能会我们就会用到 Websocket routine filter，那么 HT 协议或者 HPS 协议的话都是 native routine filter。这里面其实每一个 filter 都有它的一些作用，它处理的过程如果说涉及到需要它处理的话，它就会生效进行一些处理。其实像我们这个 Web socket routing filter 和 Nike 都听filter，可以理解为它这两个不会同时生效，一个请求链路里面也通常会只有一个请求会生效。比如其实我们刚才说到 STB 和 SPS 协议的走 native filter，如果是 WS 协议的，我们就走个 block 就请filter，那么这是我们在介绍了一下我们整个 spring Claude get way，它这些源码的结构，以及这里面核心的一些组件，以及我们这个 spring code v 它启动的流程和它执行的流程的一个过程。那么关于 spring code get v 的架构设计内容，我们先介绍到这里，同学们，我们下一节再见。

