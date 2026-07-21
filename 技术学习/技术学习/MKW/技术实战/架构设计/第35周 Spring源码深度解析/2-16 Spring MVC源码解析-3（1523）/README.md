---
title: 2-16 Spring MVC源码解析-3（1523）
---

# 2-16 Spring MVC源码解析-3（1523）

[image](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/3b2b0e94-f8b9-4d6d-be65-c34db56485d3/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663UCREBGR%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T232016Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCzMVK3zA9953t18sRqlJLfil%2FtjbzzwpG%2F1%2FF46ixjFwIgaUIS1l%2F5wz7JyAfnmlhX6iU9PsLlRp5IV7UbrKVBE50qiAQIxv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDFhr2%2FhwaMyk6tJzECrcAzxiq4%2Bq3frTNVYQZb5Wp86HjFSgT5uukriKPTrovZzwWkLouDkR6RfrRhgcNfOYueYRdVZ9mBAr2ixZnJz2QqznZj1a4OcL9C28XxwpsUQGYeCykd%2BamoWgSGI%2BNeEEipp4slY9ddsyvz0gXYugvpPAfAfxsbA59SOT44dIoJxKfiJMeWb%2FVbYJFPBnG6nRp2vea%2FKxZxux4s4quIzHuyIdZIqk8DqBYOidaaYuGQ2Ucm79ARd7B913LMbBxR0HvKY6FJ1L%2BaOAqNhtThRyjXLvf3paVNOfDhCdONokMdtNSohsPV%2FEh%2B7oYp%2Fq%2BhLrfBQj%2Flbvez%2B714JFTpseLMVs5EZUQG%2BGYuZHnooGIwJ9niWMVYGGO6icLpZzvs7i6AH5RF9v%2BAEJtdlDPE3QWSbRR91M33IHCuVim8pX1PCOFy5%2BnKJKoC%2B%2BrCgipjP1ap69c6VqKImJwritRPd0L6Np1Cw44KrvP5Rbov%2ByN8F17r1MHXdxFrDXMCtA4GsiKKlmHHpgwNttWeXsKb%2BP%2Fb7mPOWYSVIvpofGgvvPPpnwssNpjbdiuRHDl8qnP2K%2BbWDNjicHjaPYL7juheagkS5BD9%2B0VvuOFuTM89U%2Bi0ZDtwlibl561qC8WskSMKG4%2F9IGOqUB9Ga5OFAQ2vF%2B5gtlZObZfj0FyAJP6D61lHh9K8sY1xbkdEMKC%2FF%2FtELTcW0HC1PsR3h0w%2BYQDqOs%2FWXVodoWpz9J7Eye320e3HRllytHImrFoJK3o7%2Ft5HROOv5O1yQsC6SOrYW0zNK9Sp6mHL8MLdSVBSqvzACM9ADAAQQ18%2BSmUtdHOEc810yquyjnftDCZ2Ih0PtpK8PBc2qRMzwvt%2FcjVTYu&X-Amz-Signature=b1b2d74d6c07107a00db146f1a1f4ac3cb5e724f6192d9380ed15786a65a58d2&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

这里面它加载的路径是，我们可以看到是这样一个路径，就是 departure THREAD property，那么它从这个路径里面去加载一下我们的配置的信息，那么我们看一下配置的信息是什么，这里面我们可以看到 dispatch throughout，它信息的内容，也就是我们通过这个k，也就是 handler Mapping 这个 k 找到对应的这些所有 handler Mapping 的实现。


这里面默认是提供了三个，比如说这是 being name， uto b name， url Handler Mapping 和 request Mapping， Handler Mapping 和一个基于函数的一个路由 Handler Mapping。通过这个方式我们可以找到对应我们需要加载的这些 handle Mapping 的实现。那么对于这个 Dispatcher THREAD 它的目录它是相对比较特殊的，它不像我们前面介绍的这些 spring factor 说对应的目录是在 Meta info 下面，它它只是直接就在对应 spring Web IC 对应的这个 basic 目录，也就是直接在根目录下面就跟我们定了一个属性文件，其实这种风格还是比较有点粗暴的。同时我们可以看到这里面其实也定义了像 handle Adapter 它的一些默认实现，这里面还有 Handler exception 解析器的一些默认实现等等。也就是说如果说假如我们没有通过 enable m a seed 方式去开启的话，它也可以去通过这种方式指定我们需要加载的这些鼻音类的实现。那么好，这是我们这里面 handle Mapping 它的一些初始化的实现，那么接下来我们来看一下 handle Adapter 初始化的方式，这里面 init handler adapter。


好，我们看一下对于这个 handle differ，我们看一下它的参数，也是一个 Pixel context，其实它的初始化方式跟 handler Mapping 是很类似的，他要做的事情也是首先通过 BN factor 里面去获取这所有的 handler Adapter 的它的一些 BN 的实现，那么把它获取完成以后，就是经过一些排序操作放到 handler depend。


如果说当前没有找到的话，它也会通过默认的策略里面去通过我们刚才看到的这个 Dispatcher THREAD 里面这个属性文件配置里面去找一下它的内容。那么如果说从这里面去看的话，整个这个初始化 handler Mapping 和 under Adapter 的内容还是相对比较简单的，其他的这些初始化类类型内容基本上也可以相同的理解，它会通过容器上下文去寻找，如果找不到的话通过配置里面加人它的默认策略，整个这个过程就是完成了 Dispatch THREAD 它的这个初始化的过程。


接下来我们来看一下这个 enable Web m a C 它做的事情是什么？对于这个注解的话，我们大家现在已经不再陌生了，那么如果说我们来可以看一下对于这个注解，它一般会通过 import select 的方式去操作我们的内容。我们来看一下这个enable，在这个 enable MSC 里面我们可以看到它，这里面是首先是 import 一个 delegating Web MC configuration，也就是这样一个代理的一个配 Web MC 一个配置类，那么我们看一下这个配置类里面出了哪些事情。


我们从这里面看的话，它这个的类里面实现的内容比较简洁，这里面主要是支持一些扩展，这里面对于 configure 的一些扩展的配置，其实主要的内容它都是在这个父类里面，也就是 Web message configuration support 在它里面去做了一些事情。


对于这个类里面我们可以重点去关注一下它，这里面首先会去定义了一些静态的一些属性配置，这里面是主要是通过上下文类路径的加载去判断一下当前取关心的这些类有没有出现。比如这里面是有加 x banner 的和，这里面是 Jackson two json， two f r 相关的一些内容，这里面 json 和 GSON Google 的 json 这项一些配置。
其实我们更关心的是这个 configuration 类，它提供了哪一些 Bing 的实现，我们可以在这里面直接去查找 add beings，我们可以查找Bing。首先我们可以看到这里面是 request Mapping， handler Mapping，也就是说这个类默认会在对应的通过我们这里面 enable Web i m seed 方式把它去注册进来。那么它同时所依赖的这些BN，比如这里面是有类型选择器和，这里面是有格子化的一些转换 resource UU UR 的一个提供器等等。那我们再向下看它提供的内容。


好，这里面还有 UR pass helper，这里面是有一些路径的一些匹配器等等，这里面我们看这是 handler Mapping，这是又一个 handler Mapping，我们可以看到这个 handler Mapping，它的内容是什么呢？这里面我们可以看一下它对应的一些实现。


对于这个 handler Mapping 它是如何构建出来的？它会通过注射器里面去 build handler Mapping，构造出 Handler Mapping。好，我们再继续向下寻找，这里面是有 be name URL handle mapping 底下的内容，这是我们的一个基于路由方法的一个 handler mapping，我们可以看到整个这些内容它是比较多的，我们看这里面它提供了很多内容。


这里面首先我们还是重点关注的是 handler Mapping，对应的是 request Mapping、 handler Mapping 和 Handler Adapt，也就是 request Mapping， handle adapt，还有我们的 handler exception resolver，也就是说这几个内容它整个在处理的过程中都是我们比较重要的对象，也就是说我们可以通过 enable WEC 的方式，它假如引入这个注解，那么我们就可以理解为这些 b 都已经跟我们初始化完成了。


整个 spram v c 初始化的过程，它分的步骤比较多，但每一步细拆下来其实还是比较容易理解的。接下来我们通过 debug 断点的方式，快速的把整个初始化的流程走一遍，让大家对于 spring MC 初始化的过程了解更清晰一些。好在这里面我已经对于 spring MC 启动的关键地方已经加上了断点，同时这里面要说明一下，因为我们在这里面去讲 SPC 用的纯原生的 spam AC，并没有用到 spin 步骤的内容，所以说我们没办法使用 main 方法去启动debug，所以在这里面我是使用了我们通过 Maven 的方式去启动。


通过 Maven 方式去启动是准备在这里面去构建了，我们添加了我们摘体的一个 Maven 插件，通过启动 Maven 插件的方式，也就是 Maven 摘体的 round 方式去启动的。在这里面看一下我们怎么启动，这里面我们注意一下，我们在这里面去配置了一个启动命令，我们可以点加号，在这里面选中 Maven 以后，在这里面去选中我们的内容，这里面可以首先在这里面要选中一下我们 working 的direct，也就是我们的项目目录，这里面是对应的 spring m v c 这个目录。同时我们在这里面输入我们的命令，这里面的命令可以我们首先是clean，也就是说我们在执行输入我们方法之前，首先要 clean 一下，保证我们的整个编译环境的清晰，这样的话在执行 Jetty run，也就是这样去启动我们的 Server light 容器，在这里面启用它同时这个名称就会给我们生成一个 showcase spring MVC 对应的 clean 在 t 状这样一个方法。


通过这个完成以后，我们可以看到在这里面我们可以点这种方式去直接运行，也可以点这种方式去debug，当然我们在这里面会填通过这种方式 debug 的方式去启动。那么好，现在我们来启动执行，看一下效果。好，这里面我们并不关心控制台底报告的效果，我们也直接把这关掉，我们只关心它执行的内容。我们看首先第一步它会到 spring thrilled contact initiation，也就是说这就是 string 给我们桥接的 THREAD 容器启动的过程，在这里面会执行这个 unstart 方法。


我们看一下在这里面我们它这里面去引入进来的这些类，这些类是什么我们可以注意的，我们还是看一下在这里面它引入的这个跟初始化相关的类是有 5 个，我们，但是我们要注意一下只有我们这个 i m a C Web application is lesson，它会真正的初始化，初始化的原因是什么呢？在这里面它会校验一下，如果说当前加载的类是个接口，或者说是抽象的类，那么它就会忽略掉，所以说这里面这几个类只有我们这个是可以正常执行的。


好，我们就先跳过，那么我们接下来进行下一步，现在我们知道它是第一步是执行的我们这样的一个类，同时它会通过它的角做了一些过滤。好，我们跳过 F9 跳过，那么接下来是到哪了？我们可以看到它在这里面是执行，到了我们这里面是我们看一下断点的位置，断点的位置是 get root configure class，这是什么原因？我们看一下对于 spram v c 构建过程中，它会拆分出我们的一个根容器和一个止容器，那么它会先初始化根容器，那么根容器的配置是 java config，那么我们先来跟出来看一下，在这里面去 create root application context，我们注意一下它还是在这个抽象的基于注解的 config departure THREAD 初始化器里面去执行的。好，我们继续执行，在这里面去构建出一个基于注解的 webadcase context 的同时，把我们指定的这个 config class 注册进去， config class 就是我们配的 java configure。


好，这样返回完成以后，我们看一下，如果说它这里面会做一些初始化，加载一些 listen 的一个操作，这个我们可以不用过度关心。好，接下来我们执行的就是 regist dispatch flight，就是我们比较关心的一个内容，在这里面它要注的事情首先会创建一下 third applicasion context，大家注意一下刚才初始化的是根容器，现在要初始化的是就是子容器了，我们看一下子容器初始化的过程，它会去调用 serlight configure class，我们看跟进来看一下，也就是在这里面我们定义的 Web config。这也就是我们定义的这个类，大家一定要注意一下，我们继续接下来就会把我们这个类 reject 到我们的contact，大家切记这里面只是 rejs 的，它也就是把这个 bin 的定义文件的注册进去，它并没有进行 refresh 刷新，也就是在这个过程整个容器里面的 bin 它还是 bin dvent 时对象，它并没有实例化成真正的 bin 出来。


接下来我们再看好，在这里面去构建 Dispatch THREAD，同时把 Dispatch THREAD 注册到我们的 THREAD context 对象里面。好，我们看在这里面需要去配置一下我们 serverless 对应的 Mapping 的路径，那么我们看一下这里面对应的 Mapping 路径。我们在这里面定义的是根目录接下来去获取思路来的filter，也就是跟我们的过滤器相关的内容。在这里面我们定义了一个过滤器，也就是我们的支付串 BI 支付机过滤器。好，继续。好，这样把我们的过滤器获取完成以后，在这里面也是通过相同的方式把这个过滤器注册进去，好，完成，那接下来我们可以去进行一些自定义的操作，当然我们并没有去做自定义相关的操作。


好，我们跳过断点到下一步，我们看刚才执行完成以后，这一步是到了 init 方法，这个 init 方法就是对应我们 dispatch let 它的父类提供的 init 方法。在这个 init 方法里面，我们需要关注的就是它在这里面其实是执行了到 init start being 的操作，我们快速到这里面去执行。看在这个 init Server net bin 操作里面，它最重要的操作就是 init Web Pixel context。


我们知道对于 fruit 容器，比如说根容器和子容器，这会它都已经创建完成，同时把 config class 已经注册完成，这里面的银器的初始化主要是构建出这个脂容器和副容器之间的关系，我们跟进去看一下，在这里面首先判断一下它们都不为闹，同时去判断一下它是支持一个 configuration 的一个容器，因为只有实现了 configurable 这种配置，它才可以去设置相关的一些操作。我们看这里面把我们的副容器设置到主容器对应的 power 的目录下面，我们接下来去进行刷新操作。


在这个刷新操作它其实就没有什么特殊的逻辑了，只是在刷新之前我们可以看一下它会 add application listener，这里面装加载的一个listener，我们可以看到这是 context refresh listener，他做的事情就是说当监听到刷新消息的时候，刷新事件的时候，它执行 framework THREAD 对应当前的 on application event，也就是说整个容器刷新完成它会执行 on application event 这样的一个功能。


那么我们去跳过断点好，那么现在它开始进行刷新操作，那么刷新的过程中要做的事情是什么呢？是需要把我们所有定义的这些必应构建出来了，那么我们看它当前是在 Web Mac configuring sport 这个，也就是我们通过 enable Web Mac 这个注解去引入的我们的 request Mapping， handler Mapping 这样一个对象，那么这就是说明我们这个开启 MC 注解已经生效了，那么我们跳过下一个，下一个就是我们的 handle Adapter 系统里接下来去执行完我们 bin 的构建，那么接下来去 on refresh 就是我们的刷新完成我们现在要做的事情就是初始化，我们 throughout 容器相关的一些内容。


好，我们现在下一步，好在这里面去执行我们的初始化策略相关的操作。现在真正到初始化的过程，这个初始化的过程相对来说就是一步正常执行，它会先通过容器里面去获取我们需要的内容，如果容器没有的话，再通过配置文件里面获取我们对应相关的内容。我们这里面我们可以这次跟到来看一下。首先它会通过我们的 b 容器里面去获取对应的这个对象，那么在这里面我们可以看到这个对象它并没有构建，那么没有构建它其实没有做什么特殊的处理，我们看还是回到 handle mapping 它里面，在这里面做的处理，它会通过变容器里面获取这些信息，同时我们可以看到它获取到了三个这样一个对应的 Handler Mapping 的b，同时把它赋值到我们当前这个 dispatter THREAD 属性 Handler Mapping 下面，那么整个公车就已经完成好。


我们跳过断点，那么整个这个过程，也就是说我们初始化策略相关的工作已经完成了，那么完成以后，其次整个 unrefresh 的操作也就完成，整个我们这个可以理解为我们启动初始化的工作现在已经完成了。好，我们跳过断点执行到这里，我们整个 spread 容器，也就是我们当前这个载体已经启动成功了，启动成功以后要做的事情就是等待我们的请求。

