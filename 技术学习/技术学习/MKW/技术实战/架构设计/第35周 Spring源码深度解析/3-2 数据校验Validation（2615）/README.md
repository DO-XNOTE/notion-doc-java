---
title: 3-2 数据校验Validation（2615）
---

# 3-2 数据校验Validation（2615）

[image](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/3d6a1abe-91ca-42c0-9695-3345d1d84e7f/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UHQ7LQF6%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T232020Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIBXp%2BnnK0Puob2Jfa9MS09gNYsNXUXAFt7NJdxz7oyltAiBK3LvB0sCu473ljSkzTcYcfqH3mbDPT2Q1qaHX6HACKiqIBAjG%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMXzD94sKWB4PQvw24KtwDiMvR4vzE5Z8hJwqs9Di67KYOvMp8CyCJSDOg8Uo79jlJlrq8Lkj4Y51KWQos%2FCndaQc06KHGHTCvYbj3vhj8xkVe%2BMZ5NppZQILfpm9DbAVDZdQi9vSsf7I7j21Syo0j2VNa7CHnCclmBRu986qR0dlUbrDIYVMs3rHuDozVkTTPu4cwVyNadHI8v2QITgzynNaex10r02rpKZ8KfNtzXk1xMPS4HtLvo22KejrpqeEzprnLkkB%2FhfWQ6jRjoLxZWT0RAsraubGeJAjw701YNG8JvBxdYenyk0NENhi61oWVDmZooI6A41D0dUV6QN55bH20KNYLGz1yB2XFCcmLwa0D4uJvOJOU8A8y%2Ba%2BhJD85Yk89H2bJ9YebpIL16pWUI83FPX2tMFem4NqD7GwAdE3G%2B3MsuiytwYxOyd%2BgaWJXtSXYoz4z0LhpzMPhJXj%2BWf4tpEoNJVrsAa6t6CRtRKnMFgqGz256V1It%2BEN0vGDnQh91vzzoTdxW78tzdiTnUmfSBunkIVJKDpJcJL2jA5K%2BkeZE1qz8l539MJeKhcEglGtd3igHEBXeNDMnKUsZa6dx%2FyP9otk%2FNnPYg0RI%2BLEBuRXjVUNc53qAZ9O8RLMnVExEP%2Bv%2B6wFX%2B4cw6bn%2F0gY6pgEWq%2FwR9QIqScAMwHq%2BbqdmFQLmrobR6TD%2B2RmFA%2BLaVBuNxFlDr6fxMRZQxuA%2BoG01D8wnDOuRQHldoXJKpdi4hz3mCmuD4sqoceft520tfMvlcGo8DqXEudcv0lR4ZFxTaP9z419mAkWaz8pY1lsWB2Q4%2FFD7WcwwH7ITZHFoi3s771W03PZHrDaBiDQ%2Fu9HKpEYg96o4lo1bv76solLufc%2Fx18tU&X-Amz-Signature=f9ae64deaaedd19a2c9e6316c7c07e797063c296f0c8a97ca5402816a2cb43f7&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

同学们大家好，这一章节我们来介绍 spring 的数据校验。 Validason 在 Java 领域做数据校验的规范是 j s r 303， J s 到303，它定义了基于注解描述的数据校验规则，包括我们常用的，比如说输入长度、字符串不为now、数值大小范围、邮件格式等等。那么基于这个 JSR 303 还不能提供了一套它标准的实现，也就是说它可以实现基于这些注解的一些校验的逻辑。


那么在这里面我们去介绍 spring 的数据校验。我们来分三部分，首先我们来介绍一下 spring viteason 相关的一些核心API，这里面的核心 API 包括 D S R 303 的规范和 Hypertime 的viteadata，以及 spring validation 相关的一些API，那么第二我们继续介绍一下在 spring 框架过程中使用 validation 使用数据校验的一些场景。


最后我们还是基于我们代码进行 spring validation 的一些使用实践。首先我们来看一下 spring validation 的核心API，从这里我们来看一下跟 spring validation 相关的这些API。首先是 J S R 303 的规范， JS R33 规范，它首先是定义了一主跟我们这些校验相关的一些注解，我们可以从这里面来看一下这些注解的内容。


通过注解这里面首先它有一个 at Vlady 的这样一个开关，我们也就是说它标记一下我们对应的操作是需要通过校验逻辑的，那么校验逻辑我们常用的这里面有像 not blank 不为空，这里面 not unpatty，跟我们在使用一些 UTL 校验 string 植物串的操作逻辑是一致的，我们可以做到介名词义，这里面是 not now，底下是 at null，如果是 null 还有一些跟size。比如说我们输入这个字符串长度大小，这里面有 Max 和min，包含我们对于一个数值类型的它的最大值，最小值的一些设置。


下面我们可以看到它是跟我们这些数值相关的一些内容，这里面有负数和正数包括 0 或不包括 0 的情况，底下里面有跟 Email 相关的还有一些pattern，也就是说我们可以支持一个表达式的方式去校验我们这个输入的内容是不是我们合法的一个输入？当然对于在 data 303 里面提供的，还有其他的一些很多的一些注解，这里面我们就不一一列出来其介绍了。


通过这里面我们可以知道我们现在可以做到对于一个 PORTAL 或者一个VO，它一个属性的注入，也就是属性的校验，可以通过注解的方式去加上我们的描述，那么在使用框架的过程中就可以自动生成校验的逻辑，这是一些我们常用的这些注解，那么在这些注解它是如何生效的？在 GSR 363 规范定义完这些注解以后，它并没有去定义这些具体逻辑实现，那么它具体的实现是通过 Hive net validated 去实现的，这样它里面的这些对应关系，比如说在 G 2303 规范里面，它定了一个叫 relticent provided，也就是说这个校验的提供者是谁。


那么 Hive net validator 它就实现了一个 Hive net validation 对应的 provide it，也就是说 GSR 303，它通过 SPI 的方式去寻找对应的这个 priority 的实现。我们如果引入 havennet valid 大包的话，它就可以找到这个对应的实现，可以把整个它的这些处理逻辑生效。就是我们在使用的过程中就可以使用 happening ability 的它的实现来校验我们的这些 validation 逻辑。那么在这里面我们可以看到对应 GS 303 规范里面有 validata 的有factory，那么 Hypanana 也有它的 Hyperena ability 的factory，也就是说当我们在实现一个规范的过程中，我们其实基于它的业务逻辑实现我们的业务代码就可以。同时 Hive net 它在 GSR 303 规范这些约束注解的基础上，又扩展了一些自己的注解。当然这些注解的先后顺序，比如说有一些它是 happening 的先定义的这些注解。那么在大家使用越来越广泛，越来越受欢迎的时候， DSR 303 规范随着它的也是版本更新，它可能会把 happy time 里面的这些约束移动到它这里面。


其实就是说我们实践先行规范之后，我们可以把实践中受欢迎的这些注解挪到我们对应的规范里面，那么这里面我们 spring validation 跟它们的关系是怎样的？其实如果说我们不考虑 spring 它的特殊性的话，我们完全可以基于 GL 303 规范和 having a video 的实现这两个来完成我们对于这些输入输出的一些校验。在 spring 这里面它会做了一个 spring village Adapter，大家可以看到 spring 其实它做的更多的不是说我去实现什么功能，我更多的是对于已有的这些轮子进行整合，它不再去制造轮子其实是一个成本非常高的事情。


那么对于我们在 string validis 它里面提供了一些对应的 at validate 注解， ideally 的注解跟我们刚才加 3. 3 里面 at valid 它的可以理解为是一个对应生效的一个关系，也就是对应是一致的。那么对于它同时也提供了一个 validator 一个接口，这个 validator 接口跟 GSR 303 validator 的接口是不一致的，对于这个接口我们可以理解为它进行我们的一个校验的操作。对于 spring validator，它可以去扩展我们具体校验的一些实现，同时这里面还有一个 local validation factor bin，去可以构建我们本地的一个可以进行 validator 一个校验器。


好，这是我们在介绍 string validata 之前的话，这几个关系大家一定要明白，也就是 JS 303 规范，它就是定义了一个校验逻辑的规范，那么 Handler validata 它是一个具体的一个校验逻辑的实践。我们的 spring validis，它是对于整个规范和实现做了一层包装，方便我们在已有处理中去使用。


好，这个已经跟大家介绍过了，那么我们下一步如果说我们使用 validitizen 的话，我们需要做哪些操作？我们在构建我们的项目的过程中，我们一定要增加对应的。首先是 havennet validator，对于 havennet validator，它是依赖了我们这里面是 validation API，那么 validation API 就是我们的 g S R 303 这个规范它们的依赖关系词构建完成的。所以说我们引入 Hemini 的validator，其实它也就间接地引入了。


确实有一点需要注意的话，像这个 ER 表达式，它的依赖是需要我们手工引入的，那么因为在这个 er 表的是它依赖在 Hamline 的 validata 里面，它用的是 provided 的一个形式，也就是说我默认你在使用 validator 这种场景的环境下，对一而表达式是必须提供的。


如果说我们没有被其他应用间接依赖金融的话，我们需要手工加入来，因为如果说不加入的话，我们在使用 Spiami seed 一些 v list 校验的过程中，可能会出现莫名其妙的，我们的校验功能并没生效，但是我们根本看不到什么错误，去排查起来是比较麻烦的。


好，接下来我们来看一下 smilation 的一些使用场景。那么我们刚才也介绍到了对于 validation 的最常用的属性参与，也就是我们程序的入口，也就是 spend VC 它输入参数的一些校验。那么在这里面，我们通过在 conquer 上去进行我们的参数校验是比较合理的。


第二步是对于我们 spring 管理的一些 bin 方法执行参数的校验，对于 MVC 来说，它有一套自己的实现的 VDN 校验的逻辑，对于如果说其他的像我们自定义的这些service，那么它的参数逻辑其实并没有去执行，那么如果说我们想进行对于 spring 管理的比如像 service 或 do 层的方法参数的校验的话，我们可以使用这个 editing 区来完成。


另一个也就是当我们使命中去初始化的过程去验证 bin 的属性，当我们程序启动的时候去组装我们的bin，那么 bin 里面这些属性也许也有一些我们定义的一些规则，假如说这些规则不满足的话，我们 spring 容器启动的过程就会被中断，那么首先我们来看一下 spring MVC 输入参数校验的逻辑，在这里面我们可以看到这是我们最常规的一个 control 里面写的一个方法。


当我们执行 create user 的过程中，它会对我们这个 user 参数进行解析，也就是把我们请求里面所带的参数，或者说我们 request body 里面的内容去解析我们这个 user 对象。那么我们可以看到这个 user 对象我们在定义的时候，它用到了我们的 vdation 的一些注解，比如说access，我们判断一下这个name，也就是它作为一个普通的一个参数，它限制我们最小的必须是三个以上，注意大 18 个也就是对一个名称的限制。


假如说我们在输入的过程中它是不满足的话，那么在它执行的过程中就会抛出异常，这是我们对常规的使用 m a C 输入参数校验的一些操作。好，我们接下来看另一种方式，也就是我们在 user service 的过程中，我们需要调用我们的方法校验，那么这跟 m a C 相关有什么区别？我们知道在 MC 里面，我们这些参数并不是我们手工输入的，是我们在前端我们提交的这些 request 请求里面的属性去解析出来的。


所以说这个解析的过程中是由 spring Mac 它的参数解析的逻辑完成的，并且它完成一个数据绑定，那么在这个数据绑定的过程中，它就可以根据我们的业务场景是否去进行校验，所以说这个过程可以由 spring c 来去实现，因为它是 spring a C 去对参数的一些主状。


那么对于 service 层的话， service 层它一般是我们的业务逻辑的一些调用，比如说我们 control 层与调 service 上去 create user，当然那我们一般情况下在入口就会去校验我们这些参数。假如说如果说有一些其他入口的校验，比如说像 double 或其他一些场景校验，他并没有去做这些校验，那么我们怎么办？我们可以在这个 service 方法里面去进行参数的一些校验逻辑。


在这个校验逻辑过程中， spring 的 validation 是怎么生效的？它是需要通过 AOP 的方式，也就是说我在进行这个 user service create user 调用的时候，进行一层 AOP 的包装，那么包装的时候我首先去解析你参数里面这些注解，我去判断你的这些校验逻辑是否生效。如果说校验逻辑校验通过，那么我进行我代理的执行，如果校验失败的话，我直接就抛出异常去中断这个过程，那么这是 spring 管理的闭隐方法执行参数的校验。


那么接下来我们来看一下这个可能使用的是会比较少一些，也就是说在 string 容器初始化的过程验证宾的属性，比如说我们在这里面定义了一个 user vo，这个 user vo 它定义了一些校验逻辑，比如说也是它的最大值、最小值，以及它不能为now，在这里面我们如果说不管是通过 XML 或者通过 Java 注解的方式去定义这个 user vo，那么我们来这里面定义 user vo 的时候，我们可以看到定一个name，我们的长度是GI，也就是说它是两位。那么它不满足这个条件，在整个程序启动的过程中，它就会中断。这样就去验证一下我们的配置的一些不合理的一些情况，也就是快速失败的逻辑。


这是我们介绍了几种我们 spring 初始化场景过程的一些validations，一些应用场景，那么我们接下来看一下 string validation 它的一些使用时间。在这里我们孩子看到我们的 spring skill 这个项目模块儿，在这个模块儿里面我们相比上一节我们添加了几个 e i，这里面是海 meline 的 validator 和我们的 validation API 以及 EL 这个依赖。那么这个完成以后我们来去看一下。


首先我们来去验证一下我们在容器初始化的时候，对于我们的 being 的一些校验，那么在这里面我们定义了一个 religion skill 的一个test，在这里面去调研它的时候，我们可以看到这里面的实现。我们在这里面去定义了一个configuration，我们通过 test being init validation 的这样校验去验证。那么在这里面我们可以看到我们通过 notisen config application context 这个变容器去初始化我们的容器。


在初始化的过程中我们去做了两件事情，我们首先去初始化了 validation scale 和我们的对应的 configure 这个配置，在这里面我们启动的时候它会抛出对应的异常，这个异常也就是 being Christine exception，那么它抛出的原因是什么呢？是因为在这里面的 user view，它这里面的校验逻辑和我们的要求和它配置的东西是不匹配的，那么我们想一下它是如何做到这些逻辑的校验的？我们可以想象它在去构建 bin 的时候会做一些什么操作，因为 spin 容器给我们提供了很多后处理的操作，这样我们可以很容易去想到，其实 spring 框架可以通过后处理的方式去完成这个功能的校验，那么我们可以看到在这 visiting skill 在这里面它确实是这样去做的，这样的话它既通过构建一个，这么我们看到是 being validated post process 这样一个后处理的一些主键去进行一些操作。也就是说当我们的容器在初始化的过程中去判断一下我们输入的这些参数是否合法，如果说是合法，那么通过校验如果不合法的话就起相当于中断我们的请求。


这里面我们可以看一下 being validation post process 它做了哪些事情。在这里我们首先看到它里面有一个validator，一个对象，通过这个 validator 来去进行我们数据的一些校验，我们可以看到在这里面会有一个 of the property side，我们知道当整个这个对象我们初始化完成以后，它会把 validata 这个属性的构造完成，它构造的方式也就是最普通的方式 validation build debug validata factory，通过这个 factory get validator 得到这样一个 visitor 对象。那么得到这个对象以后它会再去做一些处理。
我们可以看到这里面有两种处理方式，一个是 post process before，一个是 post process off 的。也就是说我们至于是在初始化之前去做数据校验，还是初始化之后去做校验，我们可以通过我们的一些参数去进行配，也就是通过这个参数去配置，不管这参数是 true 和false，它最终都会执行到 do 为data。我们看一下 do with this 它的实现效果。


这个方法里面最重要的也就是我们通过 validator 去校验我们的这个 bin 的属性是否是合法的，通过校验的结果我们可以看到它是一个违反约束的一个 set 列表，通过它我们去判断如果说对于这个结果集不为 now 的话，也就是说一定有违反我们结果的内容，那么这样的话就会抛出一个 exception 去中断我们容器初始化的过程，这时候我们可以看到它是这个对于初始化的一个校验逻辑，那么我们在这里面去可以执行一下，看一下这个执行的效果。


好，现在我们看执行完成，我们再简单说一下这个单元测速用例，在这里面我们可以看到我们断言在执行这段操作的时候，它一定会抛出一个异常，这个异常内容也就是 exception 这个异常，如果满足这个要求的话，那么我们这个断言的执行成功。如果说没有抛出异常，那么我们这个断言就是失败的。所以说我们可以看到在 Dunit 他去做这种测试的话，也是比较给力的。


好，当我们执行完成以后，我们得到这个exception，我们进程 exception 一些简单信息的一个输出。我们可以看到我们在定义的过程中构建这个 being 这个 user 的过程中是失败了。失败的原因是什么呢？这里面是，它是在初始化的时候去这里面是抛出了一个异常，它的是 Bing 的状态是错误的， true 的原因是 name 的 lens 应该是大于等于 3 或小于等于 18 或者 is 的，也应该满足一定的要求，那么去满足我们的过程。


好，这样我们可以看到在这种情况下，它的断言能证明出我们通过这种方式，它会导致我们的程序启动失败。那么我们接下来看一下第二个，也就对于普通参数的校验，我们可以看到在这里面我们去使用 user service，在 user service 里面我们定义了一个 create user 方法，我们需要对于这些参数的输入参数值进行一些校验。如果说是使用 three MV seed 话，那些参数是由 SMV seed 参数解析器解析出来的，我们可以通过在那里去做一些校验。那么如果说我们一个普通的一个方法去进行做校验的话，就需要使用到了我们 AOP 的一些拦截，那么在这里面我们怎么做？我们看在这里面去定义的过程中，我们的 Vloodin scale，它这里面也做了一件事情，他住的也就是我们的 master visit post process，这个是怎么理解？其实也就是在我们执行方法的时候去进行我们校验的一些后处理。我们可以看一下它的实现逻辑，在这里面它注的实现比较简单，它这里面定义了一个validity，一个注解，同时定义了我们这个validator，也就是我们的验证器。


在这里面其实最后我们可以看到也是 of the protoset，也就是说在这个电台完成以后，他要做的事情是构建一个 AOP 的pondcat，它通过后处理的方式去构造我们 AOP 的实现，在 OPT 的实现里面，这里面是也是基于注解的一个 point cut，这个注解就是我们刚才这里面看到的是validata，它里面处理的事情是什么呢？它会做的操作就是 create master validation，通过 master validation accept，也就是这一个方法拦截去做我们的一些校验的逻辑。


我们可以跟到这里面去看一下，在执行 invoke 方法的时候，它去发现我们当前这个 validation 相关的一些操作，这里面它可以去基于 group 的方式去主旨，最终他要做的事情也是通过 Validator 去执行我们 VDATA 的操作。我们可以看到在这里面去执行 visitor parameter，它的一些参数的一些校验，也就是大概这样通过 u p 的方式去进行我们参数的一个拦截的一个校验。好，我们现在回到这里面，那么现在我们可以也是执行一下这个操作的内容，我们看一下执行的效果。


好，我们可以看到它也是执行中在调用 create user 方法的时候抛出异常，需要注意的唯一的区别是这里面抛出的异常是加 x mediation 它对应的一个异常，它不是 SPU 包装后的异常，那么这个大家明白就可以。这是我们介绍的这种两种场景，另一种场景是我们在使用 spam v seed 时候它校验的逻辑场景，我们切到 spring Mac 这个模块里面去看一下这个过程，同时在 spring Mac 这个模块里面我们也对这个工程做了一些改进，主要改进也是 Q2 加入了我们相关的一些内容，这里面是 Hive net validator，也就是 Hive El，同时那个是 validation API 是通过它是间接依赖的。那么完成这些的话，我们去可以去进行我们参数的校验。


我们来看一下这个 Demo Controller，我们对它加入了一个 VT 的，也就是校验的操作。首先这是在这里面，我们是 create user，创建用户的过程中，我们是可以去执行 add validate，也就是对这个 user 的输入的内容去进行校验。对，对于这个优势我们也对它进行了一些适当改造，也就是说对于这个 name 去做了一下它的校验逻辑的一些约束，也就是它的 size 也是 mean in sandmonks in SPA，同时这样一些操作，那么我们在对它进行操作的过程中，我们去可以在这里面去看一下。


在这里面我们可以执行 test crude user，我们去看一下它执行的结果是怎样的。在这里面我们可以先执行一下，看一下这个结果，让大家去有一些理解。我们看执行完成以后，它也是执行的失败，失败的原因也就是 reject 的原因， name 的 value 是JI，它不满足我们的条件，这样的话是执行失败了。我们可以看到其实虽然失败，但它并没有去抛出异常，我们同时也没有使用异常的断言，这个原因是什么呢？这个原因是因为我们在 Demo Controller 里面，我们这里面定义了一个全局的一个 exception handler，一个全局的异常捕获器，也就是说当我们执行这个方法的时候，它并没有执行这里面的逻辑，它是执行到了这个 exception 这个逻辑。


在这里面我们可以看到我们把这个异常的信息做了一个包装，也就是 extend me message 去做了一个打印，同时我们返回的 HTB 的状态码也是OK，也就是 200 这样一个情况。那么我们在想其实在这个过程中，它是在什么阶段去进行我们这个 VDD 的内容的校验？其实我们可以看到我们应该知道对于这个优势的对象的数据解析，它是通过一个参数解析器来完成的，那么我们可以断点跟到这个地方进行，看一下它执行的结果是在什么地方去做的校验。那么好，我们现在去通过 debug 的方式去执行好。


其实执行的过程我们可以看到在这里面我们定位到这样一个类，这个类似个 model tribute mass 的process，就是我们知道它是对我们参数模型的属性去进行构造的一个方法的拦截处理。对于这个类我们可以看到这个类它是实现了 Handler master argument receiver，也就是说它其实就是对于我们参数进行解析的一个参数解析器，那么在这个参数解析器执行的过程中，它当在这面执行到这里面这个超出的内容，我们可以看到定位的这个方法是什么，这个方法是 resolver argument，也就是解析我们的参数。


在解析参数的过程中，前面这些内容我们就可以忽略。在这个解析的过程中，它是获取到以后，这里面判断一下是否需要校验，那么是否需要校验它做的事情是什么？我们可以跟进去看一下，在这里面去通过我们的 parameter 去获得对应的这些注解，在这些注解里面是发现有没有跟 validation 相关的内容，那么我们可以跟进来看一下，在这里面我们看他做的事情是什么呢？也就是去获取跟 validated 相关的这些注解，也或者是通过 v a LID 开头就是以这个作为前缀的这些注解，也就是这样把两个注解都包含进来了，如果说有这两个注解的话，那么它就满足了我们这个需要校验的条件，那么去会进行校验，我们可以看到这里面是获取到了一个值，获取完成以后它会进行我们的数据绑定的一个 vddate 去进行校验。那么我们可以看一下它进行校验的逻辑是什么。在这里面进行校验的过程中，首先去 get 一个 bending result，获取这个对象，在这里面去构建这个对象的过程中去进行校验，那么校验我们可以看到在这里面它是有两个条件。


在校验的过程中，首先是当前的这个东西是不为闹，另一方面是它的 validator 是实现了 small 的validator，我们继续看一下它这个条件并不满足，那么现在进行一个 validata 的操作，那么我们可以看到这个 validator 操作，其实也就是最终执行到了我们的 validator 对于数据的校验，这个具体的过程我们可以跳过。


那么我们看一下执行完成出来以后，我们在这里面看到的是我们知道它是有了一个 bending recell 的一个结果，并且它其实也是有一个 error 值的，那么如果有 error 值，是不是一定会抛出这个 binding exception 异常？不一定，我们要看一下它是不是满足这个条件，这个怎么去理解呢？也就是说如果说我们当前这个Controller，我们回到这个control，如果 control 只有一个 VV 的方法，那么这种情况下是需要抛出异常的，那什么情况下会不抛异常呢？我们去这里面，如果说我们对应的这个方法同时有一个 bending result，这样一个组装的一个属性，一个参数，那么它就会把这些信息带到这个 error 里面，再到这里面它就不会抛出这个异常。这样的话我们可以在业务处理的过程中，根据这个里面的 error 的内容进行我们的业务处理，那么它就不跑异常了。


如果说是这种情况的话，它并没有一个 error 的参数，那么它没有什么位置去表现我们这个异常的信息，所以说在这个情况下它就会抛出异常。好在这种情况我们可以看到在这里面它会去执行我们异常的一个抛出，也就是说我们数据绑定的异常好。说到这里面的话，大家对于这个 spring v seed 这个异常校验的话，应该也大概了解清楚。好的，关于 spring 的一些数据校验的内容我们就先介绍到这里，同学们，我们下一节再见。

