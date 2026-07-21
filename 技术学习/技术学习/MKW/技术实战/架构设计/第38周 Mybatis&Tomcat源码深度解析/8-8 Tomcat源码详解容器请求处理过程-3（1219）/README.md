---
title: 8-8 Tomcat源码详解容器请求处理过程-3（1219）
---

# 8-8 Tomcat源码详解容器请求处理过程-3（1219）

接下来对于在 standard host value 里面，它会去获取 context 信息，也就是说它会在向下一步进行，我们得到 host 以后，接下来去获取 context 相关的内容，得到 context 的对象，这个三下入对象以后它也会进行判断，这里面也是如果说 next 不存在的话，也是会标明对应的404。这里面也是对异步的一些处理。


接下来我们可以看到这里你会绑定一些信息，最终我们关心的还是这个管道服继续向后流转，我们可以看到在这里面它流转 context get pipeline， get fast evoke，这个跟刚才的逻辑字形很相似，那我们直接看一下 invoke 到哪个 fellow 里面，我们看到它是一个 a sticator 的base，也就是说它里面是做一个权限验证相关的信息。
那么首先看一下这个请求里面有没有带上这个 user principle，也就是说有没有标明一下当前这个请求的主人是谁？好，那么这里面我们在请求流程过程中，对于这个权限这一部分其实并没有投入太多精力，我们还是重点看一下 pipeline 向下流转的过程，这里面它是直接获取 next 进行invoke，看一下 invoke 的操作，现在我们到哪儿？是到 stand context value，也就是我们执行到了对于 context 下面的 context value，就是我们的死单的标准的 contact value。


OK，这里面做了哪些事情？我们可以看它从 request 请求里面获取到一个 message BAT，它会去判断一下，也就是说他的请求是不是基于 Meta INFO 相关的请求，或者是 Web INFO 相关的。如果说基于这些情况的话，我们就会直接拦截，这里面我们看到这是 NODE found，也就是说我们返回的状态码是 NODE found，对应的也就是我们这里面的404。


如果说我们在访问基于我们的加 Web 协议的时候，像 Meta info 和 Web INFO 这些目录是不允许访问的，所以说它在这里面就进行了一层拦截，那么我们继续可以看到这里面获取到一个wapper，我们知道这个 wapper 跟是 Server light 的一个包装，那我们看一下这个 wapper 它包装了哪个serverlight，那么在这里面我们点开可以看一下我们能不能看到它的一些信息，这里面我们看到它对于 wapper 它包装了 THREAD class，那我们看到也就是我们的 THREAD m v c 里面的 dispowder THREAD。
也就是走到这里面的话，我发现我们已经快执行到我们的尽头了，也就是在这里面我们得到我们的王牌对象，假如 error 如果说不存在的话，它也是通过 respond 直接 send error，也就是我们的 404 的error。好，那我们继续好，那么在这里面也是对于异步信息的去处理，最终来到我们的 wapper get，我们的 pipeline get fast 进行emock。好，那么我们现在进行 emock 操作，我们看一下它会执行到哪里，这里面会执行到对应的 standard WAP value，也就是已经执行到这里了，这里面就是说对应我们包装器的一个事情，对应这里面也是 wapper 下面的 pipeline 的一个处理的过程。处理到这里面的话就应该对于 Spark 12D 去处理了，处理到这里面我们就已经对这个请求的过程中，执行到它的一个根本了，也就执行到 super let 了。可以看一下对于一个标准的 WAP value，它处理的内容是什么，这里面对于有一个 request count 的一个统计。好，我们这个并不关心。


好，那么我们看一下通过我们的 wapper 获取到我们的 context 信息，这个 context 信息它也需要去校验一下我们当前 contact 的状态是否出一个可用状态，如果不可用的话会抛出我们的服务不可用的一个状态，服务不可用在这里面对应的是我们的 503 的状态码，好，我们继续。那么当前我们的 Server 它并不是处于不可动用的状态，所以说就需要把我们的 Server land 去进行创建，看一下它是如何进行创建的。


这里面当前我们的实例还没有创建，我们看一下如果实例这会我们的实例已经有了，已经创建出来了，就把我们的 THREAD 进行一个初始化，这会儿应该去了解我们加 YY 相关的知识，我们知道对于 Serlight 它的生命周期有哪些，我们知道首先当我们弹幕开始启动的时候进行初始化，初始化能以后当我们发起请求都会调我们的对应的 do get do pose 的方法，这里面也就是得到了我们的初始化的操作。也就是说当我们第一次请求这个对应的 dispatch 时代的过程中，它需要对于 surprise 来进行一个初始化的操作逻辑，我们跟进来看一下，这里面是对于 THREAD 进行一个隐匿的操作，我们可以看到其实我们每个 THREAD 它都有对应的一个隐匿的操作，同时隐匿的操作的过程中会把我们的一些信息传入进去，这个对应的内容就是我们的一个 configure 信息。


我们跟进去到这里面我们看到会执行到我们对于 spring Web 模块下面的信息，这里面是 l t server net b 这里面我们继续，可以看到，这里面对应的是 l t thread b n 里面的 init 操作，也就是说我们在执行的过程中，对于 THREAD init 操作是在这个阶段执行的，大家看源码的过程能明白这个过程，这里面还会有一个 init thrilled being 的过程。


对于这里面对应的是 framework thrilled，这里面大家注意一下，这是因为 dispatch thrilled 它继承了这些对应的HTB，Server， LED bin 和 framework thrilled，所以说最终还是执行的是 Dispatch thrilled 这个实例的隐匿的操作。


那么这里面隐匿的操作的内容大家应该也有所了解，因为对于 spring 的知识大家是掌握的会更多一些，那么我们跳出这个初始化的过程，我们现在还回到了我们这里面 stand Warber 操作的过程，这里面我们就相当于是完成了数字化的操作。我们继续这里面也对我们的 account 进行一个自增。好，现在得到了我们这个实例，也就是 dispatch 出来的这个实例，它是已经完成初始化的过程。所以说对于我们 wapper 的 low Kit，也就是说首先把这个对象进行实例化，进行一个初始化的操作。
这个完成以后，我们接着去看一下，这里面会进行一些逻辑点，我们看一下它的底盘 Tab 是不是异步的，可以看到执行到这里面就是另一个关键操作，也就是我们可以看到它的请求的路径，也就是我们的 hello index 的，那么他要做的事情是创建我们的 filter chain。


那么 filter chain 是如何创建？我们可以看到这里面有一个 application filter factory，基于这个 factory 通过 create filter chain 的方式创建完成。创建过程中它需要传入的参数，这里面是request，一个 wrapper 和一个 throw let，这里面的 throw let 就是我们的 dispatch throw let 了。


我们看一下这个 wapper 是什么呢？ wapper 移除我们的标准的 stand one standard wapper，这是我们的请求。好，我们可以跟进来看一下它创建的过程，可以看到在这里面是通过创建的方式，我们看一下。首先是构造我们的 filter chain，我们先看一下它的请求里面是否存在 filter chain，如果说它的 request 里面不存在 filter chain 的话，在这里面我们直接通过 new 的方式构建 filter chain，同时把我们的请求，也就是说把我们的 filter chain 放到我们的请求的上下文里面去做，相当于是我们缓存了一下，同时把我们的 surlet 也放到 filter chain 里面，同时去进行异步支持的一些设置。


现在我们发现对于我们的 filter chain 里面已经包含了 Server light 相关的信息，接下来它会执行 field chain 的过程，最终执行到我们的serlight，这里面还会有一些 dispatch type 相关的操作。


大概了解了这些，那么在这里面需要开始执行我们的这是对于 filter chain add filter，也就是说 filter chain 构建完成以后，我们添加完了 Server let，同时也要把我们的 filter 添加进去，好这些内容我们就可以跳过，我们去跳出这个执行。


那么现在的话，我们已经得到了一个创建好的 filter chain，这里面我们接着去看操作，这里面对于 surlight 不等于null，同时 filter 也不等于now，它才能继续后面的操作。这里面要做的事情也就是通过 filter chain do filter 的方式去进行我们的执行，在这里面我们 filter chain 执行的话，大家就理解起来会更轻松一些。
我们可以跟一下这 filter chain 里面包含了哪些filter，那么我们先来读 filter 跟进来，这里面我们看执行的filter，这是什么呢？还是我们的 filter chain 读 feed 操作，那么我们继续，这里面是有internell，我们的 do filter，那么来到这里面呢？我们看一下 filters 里面有几个filter，这里面我们看到一共有 4 个filter，分别对应的filter，我们可以看到，从这里面去看，这里面有 filter 的class，也有 filter 的name，这是Creator，也就是我们的字符串编码的一个filter。这里面有我们的 order 的form，这里面还有一个 order request 这样一些信息。


好，那么这是几个filter，那么我们可以根据执行一下，我们其实并不关心它执行的逻辑内容了，我们只是想通过执行 filter 的逻辑来达到执行到我们对应的 dispatch share 的过程，好继续，这里面，当我们的 filter 执行完成以后，那么整个这个条件判断它就会跳出，后面它会去处理我们 Serat 相关的一个逻辑。那么我们可以看一下这里面的一些操作。对于在这里面我们看已经执行到了我们的 surprise service 的操作，其实这里面我们也应该知道，对于 thrift 生命周期执行的过程中，其实它并不是直接去执行我们 do get 和 do pose 的操作的，它其实所有的操作都是执行我们 service 对应的 service 操作。


在执行 service 操作的过程中，我们可以根据取向 service 操作，会根据它不同的请求类型，比如它是 get 请求还是 post 请求来去选择对应的是 do get 还是 do post？好，我们进入断点，我们这里面去得到了 request rebug 对象，进行 service 相关的一些内容，那么这里面我们可以看一下它其实对应的是在 HTB select，也就是我们的加号 x light， HTB 前面的 HTP sir light。


好，我们继续跟进去看。这里面我们去解析出我们的请求类型，也就是 it Mesh 的。我们这里面得到的请求类型，我们必然是get，因为我们直接从浏览器发出的请求，它在处理的过程会对于 Patr 这样的一种特殊类型，也会进行一些特殊处理。完成以后我们去执行 super 的service，看一下 super service 做了哪些操作？


do get 现在切换到我们的 do get 操作，对于我们的这个 spring 的 framework Supernet，不管是 do get 和 do post，我们看一下它处理逻辑都是一样的，都是 process request，好，我们跟进去，那么这里面是 process request，我们接着进行这里面我们看到它是一个 do service 方法。 do service 的方法现在已经切换到我们的 Dispatch slide 里面了。


执行到这里的话，大家就可以去跟我们 spring Mac 的知识呢关联起来了，也就是说我们通过请求执行弹幕开的过程是如何执行到我们对应的 control 的过程？那么执行到 dispatcher 了以后，通过我们的 request mapping 和对应的 handler Adapter 进行一些适配，最终会映射找到我们的 control 这样一个过程。那么这里面我们已经执行到了 dispatch 时代的我们在对于源码这个请求处理的过程，也就是它通过这些逻辑最终执行到我们 dispatch 失败的。对于唐木盖的处理的逻辑，我们也就大功告成了。好，关于我们唐木盖的原版详解，他请求处理的过程就先介绍到这里，同学们，我们下一章节再见。

