---
title: 10-1 Spring Boot与内嵌Tomat改造
---

# 10-1 Spring Boot与内嵌Tomat改造

同学们大家好，这一章节我们来学习 spring boot 与内嵌 Tom 开的改造。这里面我们知道 spring boot 跟我们集成了很多第三方组件， Tom cat 也是其中一种默认的 spring boot start Web，那么引入的 Web 服务就是基于 palm cat 作为我们默认的 serverless 容器，因为 serenboot 也提供了很多可扩展的配置。


通常大多数情况我们可以基于 stream 部的给我们提供的这些配置项满足我们大多数场景的一些自定义配置。但如果说我们真的还有一些其他的一些更复杂的一些配置项，我们还有什么其他方法可以做？这里我们来看一下 stream 布的以 Tom 开的集成过程中，我们提供的一些改造的空间，对于嵌入式的 Tom 开的进行二次改造。
首先我们可以基于一些自定义的配，比如这里面是 SWA property，我们知道对于 spring boot 的过程中，我们有很多类似于以 property 做后缀的这样的一些类，这个类我们可以理解为它是我们配置文件的一个映射类。基于这个配置类我们可以想到对于这个配置类的性能，我们通过 Server 点什么什么这样的配置去完成最常用的，我们下我们可以这里面对应 Server 的port，指定一下我们这个服务的端口信息。如果说我们要专门针对 Timecat 进行配置的话，可以 Server Timecat 为前缀进行后面信息的配置，比如这里面涉及到连接词、超时间等等这些信息，都可以用这种方式配置，这里面我们可以去切换的 Server property，给大家一块去看一下。


这里面我们打开对应的这里面的 Sera property 这个类，我们可以看到它是通过了 configuration property 这个注解进行修辞，这个注解修辞我们看它指定了前缀，也就是Server，也就是说我们对于 Server property 在里面属性文件的这些属性，比如像 pot address 这些信息它都消久一个前缀，也就是我们的 Server 前缀。这里面比如像pot，我们可以通过 Server 点 pot 来进行一个配置address，我们可以指定 Server 点 address 的方式去配置。


这里面我们看到它里面还支持一些嵌套的一些 configuring properties，比如说对于Server，我们要配置一下它的 error 与报错相关的信息，我们可以通过 Server 的 error 进去，再看一下 error 这个 property 里面的一些属性，我们可以看到对应这里面是有指定pass，也就是说我们默认的爆出的路径，也就是我们的杠 error 这样一个part。
这里面还有词 include exception，就是是否包含 exception 这个属性，我们可以看到这attribute，我们如果说包含这个属性的话，那么我们可以把 exception 对象获取出来，进行一些比如说这个异常栈的一些遍历等等一些信息，这里面还会有一些其他的一些跟 error 相关的一些信息。还回到 Server party 看一下这里面还支持哪些配置？


这里面还有 SSL 操作，我们可以看到它也通过了 next configuration property，也就是说对于这个属性它也是一个嵌套的属性。我们可以看到对于跟 SSL 和安全相关的这些配置，在里面还涉及到一个 client hours 这里面等等一些信息。我们可以基于 Server 点SSL，也就是 SSL 再去配置跟 SL 相关的一些属性。


这里面像comparison，比如说对于一些想要数据的压缩在里面，一些信息也可以从这里面去进行一些配置，可以看到这些信息后面就是我们涉及到一些具体的一些服务了，可以看到这里面有 h t p 二serlight、汤姆cat、 Jetty 和 Nighty enter，这里面我们重点关注的是汤姆cat，如果说我们想对 Tom cat 的这些属性进行配置的话，我们需要进行操作是 Server 点 Tom cat，这里面也跟大家去演示 Server 点是 Tom cat，下面的去配置一下汤姆 cat 相关的一些属性。


汤姆 cat 支持哪些属性，我们可以看一下在汤姆 cat 它是作为一个内部类这样去展示的，这里面可以配置 access log，也可以配置线程，比如base， DIR 等等这些信息，像下面这些信息都是可以支持我们基于属性发词去配置的，那我们可以看到这里面像 Max connection 和 accept count 等等这些数字。我们看到这些信息以后也感觉死轮不得。


给我们提供的这些扩展其实还是很丰富的，但总是避免不了有一些需求基于默认的配置是完成不了的，这里面怎么去解释？我们可以看到对于这些属性文件，它能满足我们大多数的一些场景预警。 spring put，它在支持这些配置的过程中并没有把它们开的原声，它对应 Server exam 和 Web mail 里面的一些属性全部包含进来，所以说这里面它还提供了一些其他的一些可以支持自定义的一些扩展方式，自定义的扩展Paas，我们这里面它自定义的 customer 的一些扩展，这些包含哪些？首先对于这里面汤姆开的 Server let survelight Web Server，它是支持之定义的。


先看一下汤姆开的 Server 来的 Web Server，这里面我们来看到对于汤姆开的 Web Server effective customer，它那个这里面是去跟我们对于这个构建 Tom 开的服务的过程这个工厂去进行一些扩展的自定义。这里面我们先看一下整个这个类。


对于 Tom 开的 Web Server factor customer，它是作为构造 Tom cat 的这个 factor 的一个customer，它其实我们实现了一个 Web Server package customer，这里面只有一个方法，也就是 customer 的一些配置，其实对于这个接口，其实它里面有很多实现，可以看到这里面有 jetty 相关的，还有 natty 相关的。


这里面对于汤姆cat，因为汤姆 cat 支持 active 和 serverlight 模式，我们选用的是对于汤姆 cat Web Server packed customer 的效果。跟进来我们来看一下，看它的一些实现，在这里面它实现的过程中，其实这里面我们看它的构造参数，只是一个innovative，一个环境信息，以及我们的 server property 就是我们的配置信息。这个对象基于所有我们在 application 配的一些信息都跟 server 相关，都已经包装到 server 的 property size 里面。


我们可以看到整个这个接口只有一个方法，在执行这个方法的时候做的事情是什么？初日我们简单看几个距离，首先我们看到我们把这个 property 进行一个变量的一个指导，这里面我们得到了跟他们看的 property 相关的一些信息。这里面同时生成了一个 property Mapper，一个映射工具。


基于这个映射工具，我们可以看到 property Mapper 它做的事情。首先是from，也就是元数据是什么元素？即使 Tongue 开的 property get base DIR，这个数据也就是通过我们的 Server property 获取到的。获取到以后它会做个校验， we not now。如果它不为空的话，会把这个值设置到指定的一个操作，这里面 will not now。
设置 to 是指什么呢？ factory 点 set base directory，我们可以看到这里面有一个factory，也就是说我们 configuration time can web server factory 的一个配置对象，基于这个配置对象的相当于把我们的 base d i r 这个值设置到 set base directory，也就是说我们会出来一个映射，这样我们能看到就是我们在配置文件配置这些信息最终会映射到我们这个构建汤姆开的 Web Server 的 factory 这个对象，上面。所以说这样的话，我们配置这些信息都会注意一个映射，也就是说在这里面我们 server property 所支持的信息都会映射到 factory 上面。


我们可以看一下这里面其他的一些信息也是这样一个映射的关系，这是我们 server property 所支持的信息，我们可以理解它是通过 customer 的方式来映射到 faction 上面，如果是他不支持的信息我们怎么办？当然这里面不支持的信息也就是我们单纯去做，当前他们看到 Web Server affected customer 并没有把 Server property 里面的一些信息包含进来的信息，那么这样的话，其实我们可以既制定一些扩展信息，扩展哪些信息，我们可以自己设置一些对应的property，我们也实现 Web serve affect customer 基于它的去实现，我们去扩展我们的逻辑。也就是在这里面我们执行对于 factory 的操作，把一些属性值进行一些设置，也可以达到我们自己的一些目的，我们可以通过实现，也就是说实现 Web Server factor customer 的方式，构造我们自己的一个 Web Server factor 的对象，也就是影响这个 factor 对象的一些参数的设置，这是一种方式。另外还有一些方式是什么呢？可以在这里面简单去带大家看一下。


对 customer 还支持一些具体的一些，我们可以看到对于他们看的 connector 和他们看的 context 以及 PORTAL 的 handler 这些信息，它都是支持一些 customer 进行设置的。先来看一下汤姆克的 Connector 的 customer size，我们可以看到对于 palm cat Connector customer，它首先是一个接口，我们定义这个接口的一个规范，这样的话在它在初始化执行的过程中，会调用这些他们开的 connect customer 所有的实现执行 customer 操作，也就是会实现它们基于 connect 的一些自定义的信息。


看一下对于 string 部的默认的，它也提供了两个实现，这里面我们看到一个是comparison，也就是对于我们进行想要的内容进行压缩。另一个词 SSL 进行一些安全的一些协议的一些支持。我们先看一下 comparison 这里面实现的操作，在这里面其实我们重点关注的是什么？是这里面 customer 操作，对于这个 customer 操作，这里面我们可以看到，在这里面首先我们会获取到我们的 connect 对象， connect 的对象会从这里面获取到我们的 PORTAL Canada，也就是对我们协议的处理器，如果这个协议处理器它是默认的 ITP 11 Podcover 的话进行我们这样方式的一些处理。


如果说其他的它是 ITP to PORTAL，在里面会自行另一个处理，也就是说它会通过我们这里面对于 Connector 相关的一些信息进行一些特殊的一些属性的操作。比如说这里面对于我们正常 IT 11 这种情况，它会在这里面进行设置。首先四字，我们的协议 compreson 的是on，也就是开启的状态。接下来我们再去看它去设置一下我们的 mini size 以及我们的 MMIE type 等等，这些信息它是从哪获取的？可以看到它都是通过这里面这个属性对象，它也是通过我们的 Server party 里面获取到的，也就是我们在这个对应的 customer 这个实现类里面能做哪些事情？其实我们只要 connect 相关的这些属性，只要在这里面使用，有的一些内容我们其实都可以进行一些设置的。只要在 Connector 里面它有对应的 set 方法，我们都可以对这些 set 方法进行一些自定义的操作。


我们看到这是 Tom contact Connector 的 customer 这样的一个操作，这里面我们看一下context，可以在这里面去看一下这几个customer，它其实我们从这里面定位，我们看 embedding 的，也就是集成的 Tom cat 它里面相关的信息，那这里面还有我们 context 的customer。


context customer 它的实现逻辑也是相同的一个逻辑，我们可以看到它也是对于 context 进行一些制定扩展，这里面制定义扩展内容，也就是我们 context 对象所有它支持的一些 set 操作，只要我们能获取到这个对象，它都可以进行一些指定的一些扩展，这是我们 context 的。


这里面我们还可以看到我们的协议的 handler 处理器，可以看到这个它并没有一个默认的实现，那么我们可以看它去处理的一些事情，也是我们对于我们的 PORTAL handler 来进行一些扩展的一些设置，这里面所有的一些信息也相当于是我们在容器构建的过程中给我们指定一个回调的插入，基于这个回调操作去对于这些对象初始化的过程进行一些我们自定义的一些逻辑扩展。


大家已经看到了几个 customer 和我们的 Server party 的配置的话，其实对于基于这些情况，我们对于他们的进行二次改造的基础条件就已经具备了。那么如果说大家想基于一个相同的业务场景怎么去扩展的话，我们基于这些点呢？基本上能大概满足我们的一些需求。关于 spring boot 内嵌与弹块的改造的内容，我们就先介绍到这里，同学们，我们下一章节再见。

