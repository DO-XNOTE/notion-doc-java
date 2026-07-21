---
title: 2-6 Spring注解源码解析-2（2410）
---

# 2-6 Spring注解源码解析-2（2410）

[image](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/b8c49242-a410-4b24-a5e5-13bce9d827b8/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XG6WBPFW%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T232004Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDPK0QgRMBweASgeJ9zBFazbWtPbuUcb85FPW%2FawS9PUwIgDDOqY8YjAEp7iDDV6mvR2wXL92rxLXs8dvnCVhvPFyIqiAQIxv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDE%2F9zDIpxuKWT2eZ7yrcA1SAO0HkH8Ugkb%2BtaBSx%2FpYTprnPA44rRUvND6CD2ruzNa9Gbjs%2BcjPff%2ByHAOZSQcn8efqiFg8%2Bd3r25I8VgMgcxFUUGvVZnegGmHVEO4uT4DUZDiZ6xYjUlkjcH9xeEUdDZr%2BP%2B%2FG976bM%2FzU8RrhfTUbZ0npRm8f2i8cIMDng6OSDluWX8TXpuFGB5uiCi0cOd0JJoR5xCoGkSs2f9HVEB9uHRKuxzS6Zjw%2BJjZJa6pN7EvdAUGdtvgmXFbwHJfHmWD31vzlkRxfSJQixM7uQSU3tWV51JJzlGEZHPcC6ZsWNLO7uw%2FA02PKRySyqWVvX2ijNTFKrm9lPkqu7xjPIktEFh2%2B6bQnsj98R%2FrVg%2F9yD2dgRHWXod9J3n1MB0nh5i0%2BVb4XkHDU2zyVdz5BeTjNQ3hG%2Fl5pvibH2%2BlWELRsNnizWo7CDcaFH41oXsCZV9V0tNX4innVfzLrLbxg863T6JJ%2FYPoOtwvA4HUTz0oIkSsRZ%2BVwzhj7efkoOweGXHJOHsN5x%2BE2vv5WgHdnNBXhVZlPRAhDJF0NndfbLXutoBxwV9DZt5rCIxxtDTo2qyhqTVdIp%2BjT2KzXc2nPeS8a5TxIAdqlQSlE9wXkESrjFx2Rd%2FWIbzx%2BjMJm6%2F9IGOqUBfwiLKRdxh%2BhHDm%2FXbT9Z7goJm3vdOIgVH%2FnRvjCgE1tcMtZkNKSfThxN4OWKyOfyAPkYia%2FQ%2FGLUlwRRKL4OacrHjLCRM3EzJlpNfiEtTtbKa29RvjMubf1pusTyVvmqnKaQxJ4ajITdd05rZf8SjXvkwEX2qb3%2BbmY42lW3ReJ5sO1QAvvbGrt%2F5aTeXHCUFrEmZTJyTx9QGqrM0m%2FO70%2FGJEQq&X-Amz-Signature=443b4672561d2c946c32f0dec953fbec9b5b9e47cb42579d3ee1dbcf79810e98&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

那么接下来如果说构造方法，把整个容器的实例构造完成以后，接下来我们要做的事情是什么呢？就是我们要注册扫描我们的 b 主旨，扫描 b 它有两种方式，其实这两个它只要正常情况下使用一个就能满足我们整个容器的构建，一般我们会通过 resist 或者说是 scanner 的 scan 方式去完成。


那么我们看一下我们的实力是通过了 register Paas 去注册，那么我们看一下这个里面所做的一些工作，在这里面我们去注册我们一个Java，我们可以看到 Java config 它是通过 configuration 这个类去修饰的，对于 configuration 这个类，它同时也使用了 competent 去做一些修辞，也就是说它间接的也是通过 competent 去修辞过的。好在这里面我们去跟进去 just 方法去执行，那么在执行的过程中，它这里面是通过 reader 去代理，去注册，我们从这边去注册 resist 病，我们进跟进去读 resist 病，在这里面我们可以看到因为它是基于注解的一个对象，那么所以说我们首先去构建一个 notation general 的BND，也就是基于注解的一个 BND 文件。


这里面我们可以看到我们这个 condition evaluate，它开始去做一些它的工作，它去来校验数的Skype，也就是说当前解析的这个 Bing dependent 文件是否要跳过，我们可以看一下它处理的逻辑是比较简单的，它处理的逻辑也就是基于我们的肯迪斯诺这样一个条件注解来判断的，对于这个条件注解，如果条件满足的话，那么我们继续自行把它装载到b，如果不满足就可以跳出了。


大家应该知道这个处理的过程，接下来我们可以看到对它的一些一些处理，我们这里面最主要的一个处理就是这里面会有它，会解析出它的 scope mandate，把它的 scope mandate 注入到我们的这个 being dependent 里面，接下来还通过我们 b n name 的generate，就是生成这个 b n 对应的名称。


接下来看这里面要处理的是什么呢？是 process common depending notify，这个我们可以看到在这里面他做的事情是哪些，他判断一下当前这个 bin 有没有像lazy，我们和其他的primary，我们的 depends on 和 role deep description 这些注解的配置，如果有这些注解的话，我们把它解析出来，把它同时同步到我们对应的 being 里面。如果说没有这些的话，它其实就相当于是跳过。


好，我们回到看一下，那么执行完这个操作以后它还会去做一些判断。这里面是有看一下我们这个参数里面对于这个限定符的操作，如果说我们在这里面传入了一些限定操作的话，会判断一下这个操作，比如说它是我们 primary 相关的限定，那么就对于我们的病 definition 设置 primary 为true，如果说 lady 的话，设置 lady need 为true。当然我们正常情况调用流程这个参数是null，所以说它这里面还是基于它整个类本身的方式去处理。


我们接下来去看一下，这里面会有一个叫 being customer 的一个操作，也就是说我们可以传入一些我们制定义的一些操作，对于它进行 customer 操作。这个里面流程我们的 being depending 的文件去做我们自定义的一些逻辑处理。做完这些处理的话，接下来我们会把我们的 being depending 文件和我们的 being name 包装成一个 being dependent HOLDER，我们在整个过程中通过 being depending HOLDER 去做一些传输的。


在这里面我们看 being dependent holder 完成以后，这里面有一个 apply scope parks model，也就是说它会通过这种方式去判断一下我们这个 bin 是是否需要通过代理的方式去完成，或者是我们代理的一些模式是什么？这里面处理完成以后，接下来就做的 4000 句子。


being dependent reader utils resist being 这个大家应该是比较清楚了，因为这个我们在嗯，上一节我们的 defailed list 都 effect 里面是看到这样方法，最终它的做法，也就是说把我们当前的这个 being depending holder 注册到我们的 registry 里面，我们可以跟进去看一下整个这个注册的过程，最终它还是注册到我们的 be impact 提供的容器里面好。这个我们可以理解为是我们通过我们这一场有 read rejects 的 pass 去主旨出问流程。这里面主要这几步，首先是构建一个 notation generic being definition，构建一个 being definitely 文件，这样在做我们的一些处理 process common depends on notation 的一些处理。


接下来去判断一下我们的生成代理的模式，整个这个完成以后，也就是我们注册到我们的 being 里面，整个这个 register being 就完成了。那接下来我们来看一下这个对于一个包扫描的方式注册的一种方式是怎样的。在我们的代言车 4 里面，我们并没有使用 SCAN 的方式，所以说我们可以直接到这个 a notation config a Pixel contact，看它的 scan 方法跟一下看它是怎么处理。


在这里面首先我们还是看到它是有一个 stop by step，也就是说记录一下它启动的一些过程，这里面是 scanner scan，我们看一下参数，也就是一个 base packet，也就是一个包名，当然它是支持传一个数组的格式，我们跟进来在这里面可以看到这里面它通过记录了一下当前那个闭音的数量，我们再进行一下读scan，最终去获取一下它们两个的差值。去标明一下这个 scan 扫描的一个包结构的个数。


核心的逻辑是在 do scan 的方法里面，我们可以点进去看一下，嗯，在这里面我们看到最主要的方法是通过它去实现了一个我们的资源逻辑的去处理，我们去找到一些候选的我们的 company 的主键，它这里面处理的逻辑主要是基于我们的文件扫描加载，通过我们对于卡斯文件里面注解的使用去扫描出来这些 Bing 抵 case 内置文件。
我们接下来可以看一下它的一些处理的过程，在这里面它会把整个我们的文件里面 class pass resolver，也就是通过我们这个前缀的一些所有的这些包结构去解析出来。整个这个解析的过程我们可以看到它是通过 class pass 性的一个前缀解析出我们所有的文件，对所有的文件进行 Meta date 的一个read，也就是把我们 Meta date 信息读取出来，判断一下它是不是我们的候选的一个辨对象，主要就是看一下它有没有去实现我们 component 的这样一个注解，如果实现的话就把它构造成一个 being definition，这里面是 scander generic being definition 去注入进来，我们以便后面的一些处理，这就是它主要的一个处理的过程。


那么我们回头来看一下接下来的业务，当我们找到这些编译 definition 的话，它还需要做一些处理，做哪些处理呢？首先我们看一下他对我们的这些获取出我们的 scope Meta date，进行一下一些比如像 scope 的一些设置，接下来去根据我们当前的这些 being depending 的内容去生成我们的 bin name，这里面去做一些判断，就是说我们要看一下这个对应的 being definition，它是如果是 abstract being definition，这个大家应该还有印象，我们默认的 XML 配的 being definition 是继承与这个 abcack 的病dimension，也就是说通过它来区分它是通过注解的一个配置的bin？还是说非注解注册的bin？我们知道我们除了注解以外，还可以支持 XML 或者 Grovy 脚本等等这种方式注册变这两种方式。也就是说如果是 XL 的，它会通过这种方式去处理的方式，也就是这里面去对于我们那些 out where 的一些方式的一些处理的一些业务操作。


如果是注解的方式，它就会执行 process common depending notation，主要也就是解析一下像这几个通用的注解，像 lady 或者说其他的 primary depend 这些东西我们看过了就不再看了。嗯，就是通过他的去看处理，接下来会去 check 一下这个当前注解的一些信息，如果说 check 没问题的话，他就会去构建出我们的 being defined HOLDER，最终的结果还是构建出 Bing deep HOLDER，通过我们 reject pass 的注册进去。


注册完成以后，中间还要去做一个对于我们的一些代理模式的一些判断处理，最终我们通过这种方式，它也是注册到我们的病因容器里面。不管是我们通过也就是注解的reject，还是我们通过注解的scanner，殊途重归，他们最终还要注册到我们容器里面。


那么好，我们可以再回看一下整个我们 scan 方法注的事情，核心也就是在都 scan 注的内容，首先找到我们候选的这些必应组件，然后构建成 noticing being definitely 这样一个定义文件，通过定义文件去注册到我们的 in 容器里面。


好，接下来我们去看一下整个我们这个最重要的方法，也就是我们的刷新方法 refresh 方法。我们首先对它一个结构进行一个抽象，前面这是一些入预处理的操作。接下来是一个 try 的一个核心流程的处理块，是 case 和finally。首先预处理是处理一些像一个属性信息和有一些校验一下一些必须的一些属性文件。这里面是获取我们的 being factory，这个获取的 being factory 也就是默认我们在这里面使用的是 detailed list of being factory 构建的一个实例。


接下来自 paper 并act，也就是对 bin pack 去做一个预处理，这里面预处理像我们涉及到嗯 e r 表达式的一个 resolver 和我们的资源的 result ID 的一个注册器。还有我们去添加一些 bin post process，这里面主要是 application context， where process 和我们这里面 application listener detail，还有注册了一些我们一些比较通用的这些上下文环境，像我们的enument，我们的环境信息和我们的 system property 和我们 system enrollment，这就是我们的一些常用的属性文件。


后面是除了 try 的核心代码块，我们可以看到如果cats，当如果发生异常的时候，我们整个容器的刷新阶段就要终止，终止的过程中我们需要把我们的 bin 销毁掉，同时进行 cancel refresh 触发一个事件，最后去 reset 我们的一些通用的一些 case 信息。


好，我们来看一下我们 refresh 代码的结构情况，在这里面我们执行Refresh，就到我们这个操作里面，我们看一下整个代码的结构。前面这些我们可以理解为是一些预处理相关的内容，真正的业务核心是在 try 里面去做了一些处理，在 try 的后面是case，如果发生异常的话，我们会整个病人的销毁，如果要去取消我们这个 refresh 操作，并且把异常再抛出去，最终我们去对于我们当前的一些环境信息去做一些清理。


那么我们可以先把串去合起来，那么这样看的话代码就相当于简洁很多，这里面我们先看一下这里面是对于一个 refresh 的一个处理，他做了哪些事情。首先这里面会记录一下当前启动的时间，并且把我们的 close 状态设为false， activity 状态设为true，这样就开始去执行我们的操作。当然如果说我们日志一般不会打开 trace 和debug，如果说打开的话会显示一下下面相关的一些信息，接下来会初始化一下我们的这些属性资源信息，执行完成以后对我们的环境信息去做一些校验，这样的话整个过程就基本上就完成了。


那么好完成以后我们再看一下我们的下面是获取我们的 being factory 操作，这个获取 bin factory 操作，它其实在这里面是直接调用了我们的 get being factory 这个盖特病Peck，它的一个默认实现。我们这里面是用的 Generator Pixel context，在这里面 bin factory 这个属性是通过构造方法去把它直接去 new 出来的。我们可以看到在这里面是通过直接 new detailed reasonable being factory 构建出这个 be infactor，这样我们可以看到对于 application context 它内部的 be infactor 就是依赖了 Defield visible，我们可以通过源码这方面去证明到这一点。


接下来我们来回到我们的 refresh 方法里面，好在这里面我们定义到 refresh 方法，这是我们获取了 Bing factor，接下来是对于我们这些 Bing factor 一些前置处理，当然这个前置处理我们可以看到他去做了我们比如说 bin 卡斯 load 的一些设置，还有我们这些是 being expression resolver，也就是我们的表达式去处理的一种方式。
这里面还有一些资源信息的处理，我们可以看到这里面有一个是 Bing post process，它是对我们 application context where 的 post 操作，也就是说当我们对于实现了 where 类的这些接口的时候，会通过这个 process 去处理。


这里面还有一个是 ignore dependency interface，也就是说整个这些依赖会要忽略的这些接口，也就是我们对于我们的 aware 类，因为我们 where 类是通过 post process 实现的，所以说这种自动注入会就在这里面的依赖去忽略掉，下面会有一些 Server dependence，这里面我们可以看到它就是说当我们的类型解析的时候对应的一些内容，比如说我们需要依赖 b factory，那么这个对象就是我们需要解析的内容。如果我们需要依赖 resource loader 的话，就把当前的 race 对象作为我们所依赖的内容，下面也是一样的效果。


后面是我们另一个 being positive products 对于 application listener 的一些操作，这是我们 load time where 的一个post。好，下面看这里面是定义了一些跟我们的一些三元环境信息的一些bin，就是我们把这些信息作为一个 bin 装载到我们容器里面，整个这个过程就已经完成了，我们还到 refresh 方法里面，接下来就应该叫串方法了，如果说发生嗯问题异常的话就开始嗯消毁我们的病，处理我们操作那么这些内容。


接下来我们就应该把重点放到我们的 try 方法里面了，那么我们还是在脑图里面去看一下我们 try 方法的内容是做了哪些事情。第二，整个这个方法 try 的一个代码体里面，首先是 post process being factory，像这些 post 操作是整个 string 容器，它给自己后续扩展留出了一些扩展点。接下来就是 invoke be impacted post process。对于我们基于注解定义的这些bin，这一段代码的操作是非常关键的，因为它这个里面是实现了 configuration class post process 一些后处理，也就是整个这个 bin 的一些解析的内容都是由通过它来完成的。


做完这一步也就是把我们的 bin 也就注册一下我们的 Bing post process，也就是通过这里面去解析的跟我们的 being pose press 相关的一些类，注册到我们对应的后处理的一些操作列表里面。接下来是 init message source 也初始化我们的一些属性信息，接下来去init，去 application event 这样一个广播对象，也就是我们其实我们就是触发信息广播的时候所用到的这些publisher。接下来是 on refresh，它主要也是表面一种当前的状态，这下面是 resist listener 和我们这一步也是比较重要的，我们可以看到这是我们整个，在这里面是我们把 bin 定义文件装载到容器里面，这一步它的操作，我们可以看到它是执行了 get bin 方法进行督盖的bin，也就是说最终我们创建 bin 操作是在这一段代码里面去完成的。


这是我们跟 detail 的 bin factory 里面的一些区别，因为它是只要在 get being 的时候就会注册，那么我们这里面是在 Refresh 阶段就去完成，后面就是执行我们整个 Phoenix Refresh，也就是执行完这个流程，就是说明我们这次测试操作已经完成了。完成的最后阶段它会 publish event 广播出一个 contact referenced event 消息，我们通过代码的结构，我们来去看一下这里面的过程。


首先这里面是 post process be effective，我们可以看到它是一个留空的状态，它也就是给对应的子类提供一个可扩展的操作，这里面是一个 stop APP step，这个我们就不再关心了，它就是记录一下我们启动的状态主要的核心逻辑。


在这里面我们的 invoke be in factory post process，它注的事情就是去扫描我们所有通过注解定义的这些bin，并且把它注册到我们的容器里面，我们跟进来看一下，在这里面最重要的也就是我们这里面 invoke being factor post process，整个这个方法执行的内容都是跟 be infective post process 后处理的内容相关，我们在这里面找到它关键的执行点，就是在这里面我们看到它通过容器里面去获取一下我们所有的 being definition registry post process。找到他以后去做了一些我们的一些排序等等的一些处理，他进行emock，在这里面去真正执行我们以后可的操作。


我们正常情况下如果说没有特殊指定的话，对于这个 being dependent registry post process，它的实现是只有一个它的指定的内容就是我们在第一步去制定了 configuration class post process，在它里面去进行我们对应的操作，这里面的操作是比较多的，我们看一下它会执行的，也就是 post process being definition Gestry。
在这里面注的 4 强处理到 process configure being declines，通过这里面我们可以看到在这里面去做了一些事情。首先他会看一下我们整个我们的 BDPT 文件里面，它跟我们的 configuration class attribute 相关的内容。如果说我们发现当前属性里面有已经不为空的话，就说明它已经扫描完了第一次执行到这里面。正常情况下这个 BDP 内的里面是没有这个属性的，所以说这个属性是null，如果是 null 的话，它就会直接下面这一句LC，它注的词情就是 configure class u 头的，去 check 一下当前的这个 configure class 是否是我们所需要正确的。正常情况下它会执行到这里面，我们会定义包装成一个 being depending HOLDER 来去执行进去。


包装完成以后，也就是说我们这个里面就已经有了当前的 BNDP 内 holder 这个对象，他要做的事情就是在这里面对于它进行一些排序，也就是对于我们所有的 configuration 这样的一些包装的类，排序完以后进行处理。


接下来关键环节就是对我们这个 being definition 进行解析，它需要解析的解析器就是这个，在这里面我们创建一个 configuration class plus，它对应这些参数传入进去构造出这个解析器。我看到它主要是解析所有的 ad configuring 对应的class，那么它解析的方式是在这个度的一个循环里面去解析，解析过程我们去跟进去看一下，好在这里面去解析这个 being depending HOLDER，在这里面解析的过程它需要去做一些判断，首先这里面看待它是一个 annotation being dimination 还是一个 abstract 的being。如果说是这里面是，它会通过不同的 BND listen 来去做一些不同的处理，最终去获取到对应的一些操作方法。


我们可以看到在这里面会执行到我们的解析方法，在解析方法里面做一层对应的包装，它会解形成 process configuration，最终的所有的抄路它会都会聚集到这个方法里去执行。在这个方法第一步也是去判断一下我们当前的条件执行器它数的skip，也就是说当前这个 config class 是不是应该去进行执行。如果说比如说 profile 或其他东西不满足的话，可以直接跳过，在这里面第一次要执行的话，它会通过 configuring class 里面去获取一下当前这个类是否存在，正常情况下它也是不存在的，如果说是存在的话，就说明它已经解析完成了。


这里面我们要做的事情是什么呢？是在这里面去真正的去做这个 process configuring class 真正的业务逻辑是在这里面，我们可以从这里面看到，在这里面我们看到当前的 campaign class，它会去判断它是否被 component 去做修辞过。


如果说被 campaign 的修辞过以后，他需要做的是处理一下这个类成员的一些信息，也就是 process member class，我们看一下它里面出了哪些字形，去获取到我们当前所有的这些 member class 去做一些正常的处理。好，我们接下来看它要处理的就是我们的 property source，对于我们属性的一些来源信息进行处理完属性信息，它会把当前的信息去放到我们的 party source 里面。


接下来是我们的 component scan，这是什么呢？去对我们主键扫描的一些内容。对于 component scan 就是它的参数，一般是我们指定的一个 package 目录。后面我们接下来需要做的事情是对我们的 import resource 去指定一下我们对应的原生的对于 BXL 的一些配置，对于 BXL 配置它需要指定的一些参数就是location，比如说我们看到 import resource，它的主要的一个参数就是 location 对应的一些内容。对于我们通过 import results 加载性的资源，它会通过对应的 XML being definite reader 去读取，这里面后面是我们通过 badcase reader 去处理出它的一些信息。


接下来我们再看对于一些 add being 这样的方式处理，通过它去获取到我们的 bin master made data，我们可以跟进来看一下，在这里面去通过注解里面去获得我们是否存在 and being 的这样一个注解，如果有的话去做对应的一些处理，这是我们的 b 音的处理。


再后面是需要处理一些接口，我们知道如果说在加 R8 以后，我们的接口可以设置一些默认的实现，那么如果说我这个类实现的这个接口有一个默认的实现，它通过这个对应的 at b n must 去修饰完成以后，我们需要也对它的这个接口去做处理。接下来是对于我们这些它继承的父类，我们的 super class 去进行处理。如果说 super class 它跟接口类似，假如说我的父类里面也有对应的艾特 BN 的修辞的话，我必须也通过这种方式去处理完成。那么执行到这里面，整个这个解析的这些分类就已经完成了。

