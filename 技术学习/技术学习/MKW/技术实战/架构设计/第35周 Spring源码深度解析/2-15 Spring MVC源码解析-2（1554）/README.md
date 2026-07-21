---
title: 2-15 Spring MVC源码解析-2（1554）
---

# 2-15 Spring MVC源码解析-2（1554）

[image](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/8c0cbd32-5a5e-47e4-8901-5f10919c4d3f/SCR-20240803-nvlz.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TLDQ3WIF%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T232016Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCXbhHRyM3yKXEUEu3qLkuGUBeDOlnDL0rncj126jrpHgIgKysPE42JjB8HC6z8ju%2F57YSpEpYJfZz1%2FlXeEElYUHEqiAQIxv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDDNjQOZY94GgMZ%2B1nCrcAx4O6Kbe20ya1FpKTpg%2FfqVODT1dhQJkeQfB6R6txeK2nx%2FqewqlS9V83TMp%2FWzQBFBJm6PooCkQRTuEJ%2F5kqLuEwKgUoaMEsvY9KrXa4e7oM%2BimYn4V1jltYkdWiCDhOZZjEM%2FeMPS4akCCM0hCL0bXW8ck1aFR%2FToIK16cs9f8WK%2B2mdWaV6nC%2FT4cJsvbpMnJ0Bkj51bJKBmRGXNyXe7RWmW%2Fo8QXtg0BdGh7wcVspFN8wvJ2aVArUR1Xk3O8WfWtqXWevVa2eq1PVUzu6mil9Jz4VJ21LWkmepD1rOLXLV8hFmRxPVmPIHBHNOnytf1R1wJ8pKz%2FmUMRYE0RWqwuEjHRRjLEmZ39IRD%2FjdiBBhNzi9wEtxGIMVhvf4q8qkumBgFeQx%2BZ26a7h0PnhH6NBitUnV%2BqjU5E1r3w%2FHaVtVRCcPA84JlIaWlqpOXkTbmRZcF4z1io%2B4pGwYaHaG86Z2BfocemyBK69fKf42QMHkInRQAYaZQdXUyXR4610EQqZDdPmV2Au6bymvjDVavIHJ1kACaLQJomVWHiC3kaUk9aJmHDbUZ3MWHX0qGHCBrC%2BmjQpZSWxSXqdoPjLjgRTnLESK4kk%2FuIAtQoDsVuZzYIGVnn7HqLXDWVMNm5%2F9IGOqUBFrvHg16z9iMhSIfusooTaOW8P13AI%2BLuP8rRiouZEcUSaSZqYyrSFYVelST8E4XVnfN8T2kbEZCzEFoRz8IjImY8sUP65sTFT1meuJPOlcW8%2BiJDiHloV42PoJ%2BaueYWL7ObeNt5sql69c4qiFxxpjesSZbpflBL7u6OLtSRsWrrPsmwfM0MMwrJrUNRkaYeRPblJUkDnYdNupZQknR0Qgalzc3o&X-Amz-Signature=59bcebaf1071fe70974e17650e59450efbd7433214b02203c35ff921733e1c49&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

对于 spram AC 的执行流程，我们可以分两部分，首先我们来介绍 spread Mac 的初始化流程，也就是当我们容器启动的过程中，如何把 request mapping 相关这些注解如何装载到我们的容器里面。另一部分，也就是 SPAM 的执行流程，也就是当我们请求发出以后，它是如何通过 discharge throughout 映射到我们对应的 control 对应的方法上的。


一个过程来。先看一下 three m a seed 初次化流程。对于初次化流程，这里面可以分为三个部分，首先是我们在启动的过程中，不管我们是用 Tom cat 或者Jetty，那么我们启动的过程中，我们的 Server light 容器，也就是 Tom cat，它是如何引导去初始化 spring 容器的？这里面大家要区分一下什么是 spring light 容器和 spring 容器， serverless 容器也就是对应的汤姆 cat 或摘体，那么 spring 容器它是需要在 serverless 容器里面去执行的，那么这一点我们要注意一下 serverless 容器，也就是它们开始启动的时候，它它是如何去触发 spring m a seed 初始化的。


好第二步，如果说我们整个 spring 容器启动完成以后，那么对于 dispatch share let 它是如何初始化的？ Supernet 初始化的过程中它又触发了哪些词性的变化？那么我们看第三部分，也就是说当我们容器和 disparch THREAD 都可以初始化的时候，我们就要关注一下 string 容器里面跟 Web IMC 相关的一些内容，那也就是说 enable Web m a C，它在开启我们的 spring IMA seed 过程中，它又做了哪些事情？我们可以从这三方面来去了解一下整个 stream 程序的初始化过程。


好，我们先看一下 thrift 容器如何引导 string 容器的初始化的过程。整个我们现代的 Web m c 开发的过程中，我们基于 Serverless 3. 0，我们已经不再使用 Web 点 mail 了，那么我们不需要 Web mail。整个 Server ID 容器如何引导初始化？这样的话，我们来看一下我们的 showcase 里面这个 spot Mac 这个结构，我们注意一下这个 Mac webadcase insliser，它是我们整个程序的启动的入口。


好，在这里面我们看一下这是 Mac 这个启动的入口，对于这个入口它是继承了 SPC 给我们提供的一个基于注写的一个 dispators THREAD，一个启动器，那么这启动器它做了哪些事情？我们还回到这里面看，对于这个启动器，它其实间接的继承和实现，这个叫 webadcase in sliser，它的提供是其实是spring，它跟我们去做了一个间接的兼容。


首先我们在 Serverless 3. 0 以后，它提供了一个基于类加载配置的一种方式，也就是 serverless container in sliser，它的意思是什么？如果说我们这个类是实现了这个接口，那么在容器初始化的过程中，它会加载这个接口下面的这些类的实现，我们来看一下这个类的死一些内容，这个类比较简单，其实我们看一下这个类，它对应的栅包是加 x Services a p i 4. 0 这样一个类，对于这个里面它都是 sore 的相关的一些规范。


那么这个类它只有一个方法，也就是 unstored up，也就是说当我们容器启动的过程中，它会去执行，也就是说所有实现的这个接口里面方法的 unstart up 方法，这就是我们 serverless 容器启动的时候，可以给我们注入了一种回调的一种方式。


那么对于它来说，我们看一下它的一些实现类，在这里面我们可以看到它的实现类里面这个我 spring serverless container in its Lisa，也就是说通过这个类它跟 spring 容器启动构建成了关系，同时我们可以看到还有一些其他的一些方法。 at 我们这里面有 logback 相关的一些抄准，这是 Tom cat starter 前相关内容，我们重点关注一下 spring through light container in lesser，那么也就是说跟 spring 相关的一个类。


那么对于这个启动器我们可以理解，当我们的 serverless 容器启动的过程中，它会执行到这个类，在这个类里面它会执行什么方法？我们可以看到这里面有一个 unstartup 方法，在它启动的过程中，这里面的方法它会去加载一些类，对于这些类它的一些特征是什么呢？这里面我们可以理解为这是 Web APP 的一个初始化的启动类，在这里面我们注意它里面有一个叫 handle types，这个 handle types 也是 surlight 提供的一个规范，那么所有的 handle types 在这里面去修饰的这些类型，这个类型也就是它会去加载过来。在这里面我们可以看到一个类型的集合，类型的集合它都是这样一个集合，也就是都是 webadcase in slice，也就是通过 handler types 修饰的这个类型会加载到我们的类里面。


那么对于这个 Web application initiation，它也就是我们通过这个中介，它构建出了我们的 serverless 容器和 string 容器，它们容器初始化的一个调用关系。这样的话我们可以理解为所有的我们实现了 webadcase in this letter，所有实现了这个接口的类，在我们他们开的启动的过程中都会间接地去调用指向，那么对于这个类，我们可以看到我们这里面实现的 m a C Web Picketsend，它同时实现了这个类，也就是说在执行的过程中它会调这个方法对应的 unstart up 方法。


我们可以看到因为它的继承关系比较深，它的 on start up 方法并没有直接去为我们使用。我们可以在这里面去看一下 on start up 方法，在它里面它会去调用我们这里面的一些操作内容，它这里面最重要的一点就是 reject dispatch flat。通过这里面我们应该能够理解，我们通过这种方式把我们的 dispatch throughout 跟我们的 throughout 容器联系起来了，那么我们通过这里面的 regist dispatch throughout 去构建出我们的 dispatch throughout 这个THREAD，然后把它去装载到我们的 thrift 容器里面，我们看一下这个方法的实现。


在这里我们可以看到，首先它会去通过创建我们一个 Server thrilled application context 的方式去把我们这个容器构建出来。在这里面构建容器的时候，接下来去构建一下 discussion let，我们可以先看一下构建容器的方法，那么构建容器的方法它使用到了我们这个 allotation Web Pixel context，同时它在构建这个容器的过程中，它会注册进去一个 client config class configure class，我们可以跟一下看一下它在这里面的就是我们的 macwebison 的初始化器。


这里面构建出来一个 MySQL configure，提供一个class，也就是 Web configure，我们可以看一下，在 Web configure 里面，这里面我们标明了一下，它是基于开开启了 enable Web Mac，同时根据构建了我们扫描了我们scan，也就是我们一般会在这里面定位到对应的 Web control 对应的目录下面。也就是说基于这个 Web Mac 的configure，它更专注于扫描跟我们 control 相关的一些配置，那么我们还回到这里面的配置，那么在这里面这是构建了我们的 Web Alpaca THREAD context，那么接下来这里面会创建 Dispatcher THREAD，我们看 Dispatcher THREAD 创建的方式创建就比较简单，直接把我们 thrilled APP context 作为一个参数传进去构建我们 dispatter thrilled 就可以了。


那么好，它构建出这个 dispatcher THREAD 要做的事情是什么呢？我们可以看一下，它要首先这里面会设置一些初始化器，这个我们就不用过分关心了，它会把这个 dispatch surprise 装到我们的 surprise context 对象里面，也就是装到我们的 surprise 容器里面注册进去。注册进去以后它还需要注的一件事情就是我们可以看到它去 add Mapping，添加一下这个 THREAD 映射的路径，这个映射的路径在这里面我们可以看到它也是我们自己定义实现的内容，我们这里面定义它的路径，也就是我们的杠撇，也就是最初始的默认路径。


好，那么我们回到这里面看后面还做了哪些事情，在这里面这个 Server Lite 注册完成以后，我们看一下还要去配置一下所有我们配置的filter，一会如果说我们配置 filter 的话，它从此把 filter 也注射进去，然后也可以支持我一些我们自定义的一些注射。


我们看一下这个 third filter，我们的实现是什么呢？我们的实现在这里面我们定义了一个filter，这个 filter 也就是 stream 给我们提供的字符串编码过滤器，因为我们在做 Web 开发的时候，避免一些乱码的情况的发生。


通过这里面我们可以看到我们通过这个 Web Mac 的 appliken 初始化器，它注的事情其实也就是跟我们的 serverless context 引起手建立出了一个关系，当 serverless 容器启动的时候，间接地去调用这个里面我们所提供的方法。因为我们在这里面去配置了一下我们 Web m a seed 配置是 Web configure 这个类，同时这个类标明了一下，它通过 enable web v c 注解去修饰，说明它是开启了 Web v seed 一些配置，同时它去 resist dispatch Server let 和 resist Server ladder filter，也就是把我们跟 THREAD 相关的一些内容注册进去，这就完成了我们整个容器的一些启动。


那么容器的启动完成了，接下来要做什么事情，我们就要看我们 dispatch throughout 的启动的过程。那么对于 dispatch surlet，它作为我们一个普通的surlet，那么它会遵循我们 serverless 容器的规范，把这个 Server let 装载到容器里面。它注的第一件事儿就是执行对应的 init 方法，我们看一下这个 init 方法它注了哪些思想，我们再回到 Dispatcher 来的看它的 init 方法实现的内容，在这里面对于 Dispatcher 它并没有复写 init 的方法，那么这里面我们看到它是实现的是 HTB THREAD being 的英语的方法，那么这是 spring 提供的一个间接的一个 THREAD 的实现，在这里面我们重点关注对于这个 being wrapper 去做了一层包装。


我们先并不关心它，我们关心的是它这里面是实现了 init serverless b，那么我们点进去看一下它底下的实现内容，也就是我们看这是 framework serverless 实现的内容，这里面它实现了移民的词来变，我们重点关注的是它这里面会初始化一个 Web Pixel context，初始化这个外部context，它再去初始化一个 init framework THREAD，其实它就主要内容就是这些。


我们先看一下 init Web application 它去做的事情，我们可以看一下，首先它会从我们的上下文里面去获得一个叫 root context 的内容， root contact 内容如果说存在的话，它要做的事情就是我们这里面。注意一下，在 three MVC 开发过程中，一个是 MVC 容器，一个是 root 容器，就是根容器，根容器和指容器的关系，它会在这里面去构建出这个关系。如果说这个根容器是存在的，同时我们去看一下w、 a C，也就是说这个止容器它也存在，我们就会在这里面构建一下它们的关系，这个指容器 set point 就是根容器。


这个设置完成以后要注意的事情就是这里面是refresh，我们的 weblinks contest，也就是在我们刚才它只是把这个容器创建出来，它只是把我们对应的 configure 类注册进去， reject 进去，并没有进行 refresh 刷新操作。


好，接下来我们开始进行它的刷新操作，在这里面刷新操作也比较简单，其实这里面设置完对应的内容以后，只是执行对应的 refresh 方法，那么在这里面这个 refresh 方法就是我们在 LC 容器里面讲解的，它是最复杂的一个操作，对于我们的内容进行刷新好这个刷新的过程中，其实这就是我们整个 spring 容器启动的过程。
正在启动的过程中，我们可以看到是在这里面它会执行到了一个刷新的操作，这个刷新操作也就是在刷新完成以后，它会触发一个叫刷新完成的操作，里面是 application event，我们来这里面接着去看一下，对于这里面它会有一个listener，去监听一下整个过程的完成，我们看一下它是怎么完成的知识。


我们可以看到这里面有一个 context refresh listener，也就是我们的上下文容器刷新完成以后，它去对应发出一个触发事件，触发的事件就是 context refresh 英文的，那么我们这里面 context refresh listen 就监听这个事件，当他监听到这个事件以后，他要做的事情就是调用 framework THREAD 对应的当前对象进行一个 on application event。那么我们看一下这个方法执行的什么事儿。


对于这个 on application event 它注的词情就是首先它会进行一个锁，把这个锁你锁住以后去做一个 unrefresh 操作，这个 unrefresh 操作它就会触发我们整个 Dispatch THREAD 里面的这些初始化的内容，我们可以看一下它里面的内容是什么，我们看这里面是一个空的实现，其实它是在子类实现，这里面就又回到了我们的 despite 我们的 dispatch 出来的它要注的事情就是初始化，我们的一些初始化策略我们可以看到这里面就是初始化策略注的内容，这里面注的事情会非常多。


我们可以看到首先是我们的一些多文件的一个解析器，这里面的 local receiver 和我们的 SIM 一个 handler mapping，这里面是 handle Adapter，我们一看整个这些逻辑的处理过程都通过它去初始化，每一个实现的都比较复杂。我们来顺便看一下整个通过 unapplicant event 触发到我们的一些初始化策略。


初始化策略要注意的思想就是这些内容，我们重点关注的是 handler Mapping 的初始化和 handle Adapter 的初始化。那么在这个过程我们看一下他们做了哪些事情，我们看一下 handler Mapping，对于 handler Mapping 它要做的事情是我们会从整个 be in factory 里面，我们可以看到 be in factor user 里获取一下所有 Handler Mapping 的类的死线，也就是说所有我们当前这个 bin 容器实现了 Handler Mapping 接口的类都会扫描出来，扫描出来它对应的类型也就是k，也就是我们的 b n 名称 value 对应的支持 handle Mapping 的实现。


那么确保这个 handler Mapping，也就是我们的 Mapping bins 不为空的情况下，它会进行一个排序，最终的操作是把我们的 handle Mapping 去赋值给我们当前的这个 dispatch 10 来的，这里面 Dispatcher right 对 Handler Mapping 还做了一个兼容处理。


假如说我们在刚才的我们容器里面在获取的时候，如果说没有获取到 Handler Mapping，也就是说当前如果 handler Mapping 还为 null 的话，那么它就会通过默认的一个策略去构建我们的 handler Mapping，那么它默认的策略是怎样的？它默认策略是这样，我们可以看到它也会通过当前的一个配置文件去加载它所需要的一 handler Mapping。

