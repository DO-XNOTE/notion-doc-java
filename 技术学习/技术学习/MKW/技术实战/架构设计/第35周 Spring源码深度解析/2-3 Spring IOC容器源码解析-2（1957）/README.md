---
title: 2-3 Spring IOC容器源码解析-2（1957）
---

# 2-3 Spring IOC容器源码解析-2（1957）

[image](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/a6f8a607-1305-40f3-a967-e0eb7ebfa157/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VQCQ4TXR%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T232002Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQD9Lr5ddrWb9qSVZ9iWC6QnjnFbfJcxmLIbdOBV%2FsankgIgJJDRNGrVzLNgGqgwhr5wY1nukbllOKpcFy36VXtxChsqiAQIxv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDDqbaDTyu4MeMQYhGircA9gyRv7Qkoj%2B9UVTcDaQZzY034DhbhUbkeaK%2F%2B%2F%2BYqaLQVqZTB7pndp3HDtDbnoEx%2Bli7XsuN2rNQAuRxn0zsSVI%2FpBT6vnBAmd0YXBMCb%2BRtvQQnL970IDW3BFWymzUUDYEl%2Bhr0F9VM2utEhcqpmGiJMMHCUqwOmKpz77FuD%2F%2B00elg7oCwKkEYVLEj4LazCC6zd6cXKpnnSgZ8wA9NdZlDkyvKpA8D0qUHjGrIiaZ5UGzUjozLqs9SRvrd1Tb%2BAS9q4s82Of7dgFeqOzCLsgW%2FgrkjxSCe96Fr9MXbVG4FCHY0W7MH93RE%2FLREShTH8FU3byahzTh0vFYH9lv7ZrMF2SgPhHEqyb%2Bs5I%2BRZ%2F6TxfotqUCkgrcFBKNqzd0BphySInsSxH1lcUvqdzEZVNQlf5mMUZ28G5QoGKudrplC2dGzz24mdQppUIq2I2%2FA%2FdzppmAHdJaVYUJM4SBwvxfaCB3UaU0k3x%2BntmJw5QGqskMsfD0Be34u%2BqRIr1J1cqxTADPeUiQivOvkIt12%2Fci303sIliYDBSyIKXcilrdHAJS%2B34EpQGnGCNbuQ5UOmM2XTWtl2czZunK22RrR4u2LLLVR%2BXb0l1TcwRIa79pzcxjalkgNI%2BIVDK%2FMPK4%2F9IGOqUBL2nN9V%2FObUYxluapD5taxAte3%2FrbhLnQkN1s6SYhEVf%2FDl3Kj5esaY4hFNlckGmr1U27al7hiTNXj5RDI8X%2BKUq%2FS6ydnpn1XNJuFmNY9xQyIxXpLEpldKOFalV9lXqRf6N%2F%2FJBxmfqSf45atWpOZkX6gVlUkktNyVKy2%2BUYxAeV8TBpS1HA3wYpDjfkR8xSL4fM1AaxU10F3j2J1hF5r8q5JCu5&X-Amz-Signature=cb783a73f2e5249fc3772cb367016f340b308adbae55baebbff28261b822f342&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

接下来我们来看一下 spell LC 容器的处理流程，这里面处理流程我们包括两个，一个是我们默认的 bin 容器 debug lisable being factory，另一个我们基于注解的容器 noticing configure， applicase and context。


额，我们可以先看一下这个默认的容器它执行的一些过程。嗯，额，在我们在演示这个默认这个 being factory 执行的过程中，大家应该还有印象，我们是创建 debug listable being factory 和我们的 XML being definition reader 和 Cospah resource 去加载 Hallobean 这个XL。整个这个过程作为一个构建组织的过程。


组织完成以后，我们通过 being depending reader 的 load being dependence 这个方法，它就会去执行我们的操作，这里面 load being dependenson 就会把我们配置文件里面定义的这 bin 装载到我们的 bin 容器里面，其实这个装载的过程它会委托一个叫 being dignity document reader 去处理这个过程。


对于这个 being defining document 它是个接口，对应它的实现时，前面加一个 debug 就是它的一个默认实现。其实它在装载的过程中，它会去判断一下我们这个 MR 对应的scammer，这个 Scammer 去解析一下，根据 UR 去判断它是我们 default name space，还是说其他指定的，比如像 AOP 的 namespace 或者其他的一些 YouTube name space 来去解决。


如果说是 beans 的话，它就是以我们默认的 debug 的 name space，它就会直接执行 parcel debug 的 element 去解决，如果说是指定，比如像 AOP 方式的配置的话，它就会通过 being depending process delegate 这样一个代理去，通过代理的方式去处理。它处理的逻辑是通过我们这个对应的 schema 获取到对应的 name space handler。对于如果说是 AOP 的话，它就会获取到一个 AOP namespace handler，用它去 press 去解析对应的XL，解析完成以后它就会通过 being definition reader UTOS 去注册我们的bin，它注册的过程其次通过这个 be independent util 代理去注册，最终还是执行的我们 debug list able being factor 对应的 register being definition。完成这个过程就是我们这个 bin 的通过 XML 解析，然后把 bin 装载到我们 bin 容器里面，但是这个装载只是装载的是 being demination，也就是说它把我们的一个 bin 的定义规则放到我们的容器里面。


其次并没有实例化我们真正的bin，那么什么时候实例化bin？对于我们 debug disable being factor 是它在 get being 的时候真正的去创建和实例化我们的bin。这个 get be in 方法，它会间接地去调用 could be in 的方法，在 could be in 的方法里面，它会执行首先是 resolver before instance，就是通过解析去做一个实例化之前的操作，这个实例化之前的操作，它会执行我们生命周期的方法，也就是 post process before instance 就是宇宙。


我们在实例化之前，我们要不要自己定义的方式去实例化？如果说我们自己定义的实例化方式，它返回有结果，它会去执行 apply being post process off 的installation。也就是说如果说我们自己创建的执行这个方法，如果说我们自己并没有去手工的去创建这个bin，那么这一段是不会执行的。接下来我们看 do create b，那么执行我们实体化之前的操作以后，就会真正的去创建b。在创建之前，我们 create b instance，它会通过一个 Instant 一个策略去创建，这里面有 CD Lib 的策略和我们 simple 一个策略 CD leave，我们知道它会生成一个对应的代理，我们 simple 就是原生的一个闭音对象，这个创建完成以后，它会对我们闭音去做一些填充。


这个填充的过程我们看首先它会执行 post process off 的instance，也就是说它会做我们实例化之后的一个后操作，我们在这个阶段也可以对我们的实例去做一些操作，接下来会 resolver outware，这个怎么解决？就是我们是对应的 set being 的一些操作，或者 set 一些属性的操作是在这一步去执行的，执行完这一步它会执行 post process property，也就是说我们的一些属性设置的后处理，在这里面会逐指向，也就是这是我们 being 填充的内容，比如包括我们 set being name 的话也是在这里面去完成的。


接下来我们看对于我们的初始化操作，这里面是实例化，这里面是出手，这是填充属性，这里面是初始化。在初始化的过程中，它首先会执行叫 invoke avoid must，这在我们的 Bing 里面我们应该还有印象，这里面是对应的。我们是我们在 Hallobin 这个方法去实现了一个 be name where 这样一个接口，它里面有一个 set be name 的方法，就在这里面去执行。好。接下来就是 post process before installation，也就是说在我的这个 b 音初始化之前去做的一些处理，这是初始化之后做的处理。在初始化之前和之后中间要做的一些事情，也就是 invoke init must，它注的事情是什么呢？也就是我们的 off 的 property site，也就是我们在构造方法执行完成以后，我们去执行的一些属性注入后的处理，其中还有我们的 invoke customer invest，这里面我们在 XR 里面配置的这些 init message 在这个步骤执行，那么执行完这一步的话，我们整个就能获取到我们对应的bin，获取到这个 bin 那么就可以去执行我们的业务操作。我们 hello b 的业务操作就是 say hello。


接下来就是通过执行完业务操作，就应该把我们整个容器去销毁，就是 destroy single terms，它会直接去调用 destroy being，在这里面会有一个执行 disposable being destroy 的方法，但是这里面会有一个 disable being adapter，通过这个 APP adapter 间接地去销毁鼻音，同时还会执行一下我们 invoke customer destroy mess 的这样一个方法。


我们先是通过脑图的方式把我们这个 being factory 这个实例，它在构建并且去加载我们的bin，并且注册到容器里面，通过创建 bin 或者执行业务方法到销毁整个过程的。先把这个架构让大家的脑海里面有一个印象，这样的话我们再去跟代码的时候会感觉稍微清晰那么一点。好，接下来我们去通过代码 debug 的方式去看一下整个这个容器进行装载，初次化容器到实例化，我们 bin 到执行完成的一个过程。好，我们还来执行我们这个对应的 be impacted test 这个方法，那么我们在适当的地方已经给大家装上断点，我们直接执行就可以。


首先我们在这里面是构造我们一个底票的 list infactory，它就是指午餐的构造方法。那么构造完成以后，在这里面我们是做了一个 add been post process，它跟我们主流程关系并不强烈，它有它其实对我们整个流程的影响不是很大。那么这里面我们看我们是构建我们的 XL bin defense reader， XL being depending reader，它这里面是需要我们把这个 been fact 作为参数传入进去的，我们在这里面跟进去看一下对于它的参数类型是 being definition registry，也就是我们的 in 定义文件的注册表。其实我们并不需要一个 being factory，我们只需要一个 being definition registry 就可以了。所以说我们可以理解到 x now being definition reader 里面，它对我们的操作只是只行了对于 being definition，一个注册或获取的一个操作。


好，接下来我们去看后面的事，我们通过 class pass resource 去构建这个资源文件，通过它构建成resource，通过 resource 我们去读解析，在这里面我们把 resource 文件作为参数，加到我们 load being definitely 的方法里面。那么我们接下来重点就在 load being definition 操作了，我们现在启动debug。好，现在我们跟进去。好，在这里面我们这些其实可以理解为一些正常的逻辑，它不是关键点，我们就可以直接跳过。好，我们跟进去，继续在这里面我们跟进去。


好，现在我们到我们的关键点，这里面是一个 do load being dependence，也就是说前面注了一些处理，只有在这里面才是真正我们处理的过程，那么我们根据你断点好点进去，在这里面我们可以看到它是通过 do load document，通过我们的资源文件获取到一个 document 的对象。也就是说我们把 XL 文件装载为一个 document 的过程，那么这个里面的内容它是普通的 XMR 操作，我们可以不用关心。


那么接下来我们看下一步，这一步是获取到我们通过 regist being definition，我们看到这个方法名称，我们知道它是一个关键的入口，也就是 task 开始注册我们的 being different 对象，我们看一下它注册的参数，就是我们的 document 对象和我们原来的 resource 对象。


那么我们先跟进去看一下它的内容，跟进去看一下，在这里面我们看到它是构建了一个叫 being demination document reader，刚才跟大家介绍过，通过我们的底票的必应 definition document reader 去装载我们的 XML 的必应属性，那么这里面是有一个 create being document reader 的一个过程，这个我们可以不用关心，它是创建了一个默认的 debuter debuted being document reader。


那么看这里面是在装载之前获取了一下当前这个注册表里面所包含的 bin depending 的 count 数，因为我们现在刚启动，它里面默认值应该是0，我们可以看到在这里面 count before 是0，我们看这里面是真正去执行我们 adjust 宾语 defentity 的操作，那么执行完成以后，它会再去获取一下当前的我们的 bin defending 的数量，去跟我们的初次值做一个差值，获取到我们这次装载的数量。


那么好，我们接下来我们 debug 跟进去，在这里面我们点进去，我们可以看到它在这里面构建一个我们 do adjust being definition，也就是在 spring 定义这个方法的过程中，一般是有正常的方法名称，前面有再加do，好像就是真正去执行的一个过程。


那么我们接下来我们跟到这个方法里面，好，很简单，在这里面我们可以看到这里面我们有一个delegate，这个 delegate 变量它是用来去解析我们的 being defending 文件的，那么首先它默认是null，我们在这里面去 create delegate。我们现在接下来跟进去，这里面是会把我们 delegate 去创建完成delegate，它对应的也是 defiled being defint pass 跟我们的，我们刚才这里面去介绍的，它是我们的一个对应的实现，那么在这里面我们首先会判断一下当前我们执行的这个对象，它是否 debug 的namespace，那么我们看一下它是怎么处理的，它是否 detail name space。


我们跟进去看一下，这里面有个方法意思， debug 的 name space，这个处理方式也是比较简单的，我们首先通过这里面去获得我们的 namespace 的一个URI，我们看一下根据 URI 的一个比对去判断。我们在这里面跟到这里面，首先我们看一下对应的 name space URI，它是我们这里面是 HDP 对应的 schema being s，我们通过它去做比较，那么默认的 BNDK 的 URI 也是这样一个值，所以说它会返回一个 true 的结果，它返回 true 我们就可以对应，也就是说它是默认的一个结果。


在这里面如果是true，它就会进行后面的一些处理，后面的处理是它会处理 profile 的一些操作，他去看一下当前的配置里面有没有 profile 相关的一些属性，对，根据 profile 属性判断是否需要处理，这里面我们暂时不用关心这个过程。


首先这里面我们看经历上面 profile 的处理，下载到我们真正的 pros being definition，也就是真正对我们比例进行解析，这个解析的过程，首先这里面有 Pre post，我们也可以看到在 strong 设计的一些一贯风格，他在做一些关键的操作之前或之后都会留出一些扩展点让我们去处理。这里面默认的 Pre 和pose，它执行都是空的操作，主要是为了我们一些扩展的调整。那么我们接下来跳过Pre，我们先执行 pass being dignation，我们跟进去。好在这里面在跟进来以后，它第一个也次驱逐判断，先判断一下 is debug name space，我们知道当前我们是使用的是默认的namespace，那么我们现在去跟进去，一步一步看它要怎么去处理。


首先通过 root 获取到我们 root 下面第一成绩的 child notice，得到这个 child notice 我们可以看到这里面我们的内容，我们去向里面去获取。首先我们看到推判断 NODE 是否是一个 element 的一个节点实现，那么我们再找对应的实现这个它就是了。在这里面也是判断，如果说我们当前的这个节点它属于 debug name space，它会通过我们的 pass debug element 这个方法去执行，如果它要不是的话，它就会执行 delegate pass cus customer limit，也就是说默认执行 debug element，如果说不是的话它就执行customer，也就是自定义的一种方式，那么当前我们是默认的是，那么我们可以在这里面跟进去看一下我们的结果。好在这里面它会去取里面的一些属性，这里面的属性去判断一下当前的类型是什么。


我们可以从这里面看到这是一个 import limit，这是毕业名的element，这是一个 being element，下面还有一些嵌套的一些 being 的element，因为我们当前我们的内容是一个 being element，它会执行到这一点，我们看好跳过它会执行到这个里面，它在这个里面作为它会解析我们的 being definition。我们根据句好，其实这里面就是真正的去解析我们 being 的一个过程了，在解析的过程中它会构建成一个叫 being dominant HOLDER，会把我们的 being domination 装载进去，通过 HOLDER 的区域获取到 Bing 抵 case 人的引用。


好，我们接下来进一步知晓。在这里面我们通过它获取到我们的 being depending HOLDER 以后，去通过 being depending rejection reader UTOS 去注册我们的拼音ignition。那么我们通过它去注册，我们看一下结果是什么样的，我们点进去，在这里面我们注意一下这个方法，它里面主要是一些静态方法。我们通过注册我们的Badcase，它的注册过程其实也是委托了我们这里面的 being defendant registry 去注册。它真正的作用是把我们对应 holder 里面的 being defending 这个对象注册的registry。好，我们自行，这里面我们可以看到这是 registry 点去注册我们的变体，现在我们可以看一下这个对象，这个对象的内容就是我们的 debug 的 list being factory，通过它执行的话就会执行到我们的默认的 being factory 实现里面。好，我们听进去。


好，现在我们可以看到现在已经回到了我们 debug listable being factory 的过程，跟我们在这里面执行的效果是一样的，我们可以看到它是通过 being definition reader UTOS 去注册，最终会调用我们 default list being factory 它的注册 Bing defendity 的操作。


好，接下来我们继续操作，我们跟进去看，这里面就是做了一个对于 bin 底部分的一个校验操作，校验没问题，它就会把它注册进去。好，这样做一些校验，那么这些工程我们就可以快速跳过。好，现在我们对于 bin depending 注册完成以后还要做一个操作，是判断一下我们这个病有没有别名，如果需要别名的话，把别名也注射进去，因为当前我们并没有给这个病指定别名，所以说这个注册它会自动跳过。好，现在我们去整个过程，它执行完成以后会触发一个事件，这里面是 send 一个 registractions event，也就是说注册完成以后触发一个事件，整个过程我们回到这里 process 并 depending 内。接下来我们继续。


好，我们可以看到这个过程执行完成，整个这个过程执行到这里面它要执行 post process mail，它里面其实也没有什么太多的内容，那么这里面要跟大家去解释的。说的一点就是我们在这里面有一个 ticket 对应的 plus customer element，因为我们当前只有一个bin，我们并不存在其他的一面。那么如果说在这里面我们需要做一些事情是，首先我们跟进来看一下，如果说是其他的情况，它会在对应的地方获取到一个 namespace handler receiver，这个操作是什么呢？它是一个解析器，解析出我们当前需要用哪个 name space 去操作，那么这个解析的过程我们可以看一下它，通过它去 resolver 我们的 NAMESPACE URL，我们跟进去看一下它的实现默认也只有一个，我们可以在这里面去看到，我们看整个这个 Reserver 的操作，它有一个 handler Mapping 去操作的，那么这里面有一个 get handler Mapping 的过程。也就是说我们去获取这个 namespace handler，它有一个映射，那么这个映射从哪儿获取到的？我们可以看到这个映射它最终其实也是通过我们对应 mind info 下面的文件去获取到的。我们可以看到在这里面有一个是 Mint info 对应的 spring handler 这样一个文件，我们通过这个文件里面获取到这些映射关系，那么我们去看一下这个映射文件。
它的 value 就是对应的 util name space handler，我们可以看一下 util name space handler，我们看一下对于这个 u to names handler 里面，它里面注册了一些可以支持解析的一些参数。比如说首先我如果我们的标签包含 contents 的话，我们会使用 contents 并 depend pass 去解决，如果说有 list set map 的话，会有对应的 list set map 对应的病例内容去解决，我们可以看到这也就是定跟我们定义了 XR 解析的一个方式。


那我们再看一下其他的，比如说我们看一下 AOP 相关的操作，对应这个 AOP 相关的 scammer AOP，它对应的 namespace 也就是 AOP name space，那么我们可以在这里面也进来看一下。对于 AOP name space 我们可以看到它会支持 configure 或者 aspect 的接 auto parks 和我们的 spring configure 的，等等这些如果说我们在使用 spring AOP 相关的一些 XL 配置的话，它会采用这里面对应的方法去进行解析。


好，我们现在还回到我们的 debug 断点难处，现在我们已经执行完我们的 pass Bing declines 了，我们接下来它整个过程就要执行完成了，我们现在跟完好，现在我们是获取到我们执行的一个 count 数，我们看一下这个 count 差值是一，我们得到了一个 count 对象，好返回进行执行完成整个过程。


我们是已经 load Bing dependence 执行完成，那么在这里面我们执行完成以后，现在我们得到的结果就是我们的 bin 容器里面已经由我们对应的 bin 的一个 bin deepness，它只是一个 bin 定义描述的一个对象，它并不是 bin 的实例，那么真正 bin 的实例是需要我们通过 get bin 的方式去获取的，也就是我们在这里面通过 debug list being taxi get being 的方式，通过 create bin 这样等等一系列的操作把我们的 bin 实例构建出来。

