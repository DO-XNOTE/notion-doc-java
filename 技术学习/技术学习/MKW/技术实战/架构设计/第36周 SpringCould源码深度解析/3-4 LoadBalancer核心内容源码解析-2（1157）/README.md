---
title: 3-4 LoadBalancer核心内容源码解析-2（1157）
---

# 3-4 LoadBalancer核心内容源码解析-2（1157）

好，接下来我们看现在是到了 blocking load balance client 的一这样一个 b 构造方，这是在构造我们这个最终使用的这个负载均衡的一个客户端，那么它使需要的参数是一个是我们刚才构造完成的 load balance client factory，另一个是我们的一个 load balance。


那么对于 load balance property 我们可以进去看一下它这里面实现有哪些可配置的参数，这里面比如是塞尔 Tech s int 以及一些retry，我们这里面是否是绘画年字的等等这些一些标记，就是基于这些我们都可以进行一些属性的一些配好，那么我们现在跟进去这个构造方法的执行。好在这里面它也是最简单的一个构造，也就是把两个参数进行了一个赋值，那么这个，嗯， load balance trend 它已经完成了。


好，我们这现在也跳出去，我们现在的程序执行到了对应的 broken load balance client 的choice，也就是它开始执行我们的方法，比如现在已经执行到哪，已经执行到 load balance client 去选择我们对应服务的一个服务。也就是说其实我们执行到这里面的话，我们看其实对于 string 容器的初始化工作已经完成了，但是我们现在去获取一个实例，我们再看一下 load band client，它具体里面难加的，需要实例化的一些内容。好，我们还是跟到对应的位。对于这个 load band 看的factory，它首先要获取一个对应的实例，也就是获得一个 load balance client 的一个实，那么对于这个实例，我们这里面对应的是 reactive load balance，那么我们看一下它通过 service ID 作为一个 k 去获取，我们跟进去看一下，这么我们接着继续跟进去。


在这里面我们看到他会拿这个服务ID，也就是我们的 NICOS Pro ID 去获取一个对象，这个对象就是 notation configure application context，也就是它会通过一个服务名称获取到一个 string 容器，作为一个 string 容器进获取我们对应关注的内容，那么我们看一下这个 string 容器，它跟我们当前容器的关系的string，我们跟进去看一下。


首先会做一个这样的一个校验，我们看一下对应的这个contains，它是一个什么？它是一个map，这个 map 对应的 case name，它的 value 是一个 noticing configure application contact。也就是说在我们整个 spring 容器里面还有一个contains，它关联到了一些纸的 string 容器，这就是我们看到其实容器里面还会根据我们液嗯，在容器的需要包装了其他多个 stream 容器。好，那么我们现在去看第一次我们在请求的过程，其实这个容器列表是没有的，因为它还没有做到真正的初始化。好，我们看它如果没有的话，那么接下来我们怎么办？我们会把这个 name 放进去，放到contact，同时 create contact，也就是创建这个context，就是创建我们这个一个纸的一个 spring 容器，那么我们重点看一下这个创建的过程，好在这里面探卷的过程首先是通过构造方法创建，那么然后它会通过我们刚才配置的相关的一些信息进行一个初始。这里面我们看它重点处理的是这里面我们看一下 context regist，也就是说这 spring 容器上下文它需要注嗯，几个 configuration 对应的。


b。这里面一个是 property placeholder auto configuration，也就是我们这个属性占位的一个解析，另一个是我看是一个 de config type，这个 debug config type 是怎么来的？我们需要去回想一下这个 debug 的 config type 跟我们刚才在这里面去使用的时候，我们看是在这里面去构造的过程，我们把 load balance client configuration 作为参数传过去，它在设置的过程中对应的也就是 debug 的 config type。现在我们知道了，也就是说我们刚才提到的这个对应的类，在这个时机进行执行的好，那么我们执行完registry，它其实就会进行一些初始化的操作。好，我们接下来去看，接下来我们它只是注册的过程中，在后面执行 Refresh 的时候，才会真正的去实例化这些b，这里面会对于我们的一些 3L 环境的一些信息进行一些包装。


好，我们接下来看一下，如果说当前它的 point 它不为 null 的话，我们在这里面去把它 context 进行重新的一个传输，并且它的 cross loader 也作为一父类的侵权一个引用过来，好，那么在这里面它会进行这个 bin 的一个刷新。


real contact refresh 就开始对 bin 进行一个实例化，那么这样实例化的过程中的话，我们就会执行到对应的一个配置的一些信息项，我们看我们执行配，那么这会他已经到了 load balance client configuration，也就是说刚才我们关注的我们在这里面关注的这个 load balance client configuration，使他在第一次执行获取这个服务实例的过程中才进行一些初始化。


那么好，那么现在初始化的过程我们看一下它，首先我们这里面是通过 surface instance list supplier builder，它构建一个 builder 对于这个 build 对象做几件事，首先是我们是 blocking discover client，另一个是 with catching，也就是说它首先是基于我们的服务发现获取服务列表。另一步是通基于缓存进行一层包装，避免我们的一些资源浪费，这样的话就构建出了这 service intense list supply，那么我们跟进去看一下这两步处理的事情。对于 builder 来说它是比较简单的，它就构建了一个build，对，我们退出，我们接下来看一下，这里面是我们看 with blocking discovery，那么我们现在跟到这个方法里面看一下。


好，这里面我们点击进来，这里面我们看它是执行 with blocking discover client 这块要做的事情是什么？其实它对应获取到的是 service instance list from build，那么这里面是构建出来一个 base Creator，他著的事情，我们看这是个 Lumbo 的表达式，他做的事情是在这里面通过我们的 spring 容器里面获取到我们的服务发现的client，那么得到服务发现 client 以后，在这里面包装一下是成为我们 discover client service intense list supply。


那么我们可以跟进来看一下他做的事是什么，这里面我们可以看到他最终做的事情是通过d，这里面对应的 discover client 支持delegate，获取到我们的 get instance 一个服务列表，获取到我们对应的列表，获取到列表以后包装成一个 service list 就完成它的任务了。


好，那么我们这是这一步，那么接下来还有一步，我们看一下它要是 with category，就是说它要进行一些缓存的包装，那么缓存的包装我们看我们关注点也是在这一部分内容，这里面我们看到它通过我们的 spring 容器获取到一个 load balance cat manager，那么这个 load balance cat manager 我们看一下作为这个接口，它下面有两个实现，一个是基于 Cafe in 的对应的一个 cat manager，另一个是 debug load balance cat manager。因为我们在这里面并没有引入 Cafe in，所以说它默认 debug load balance，那么在这里面我们可以看到对于它的一个缓存实现是基于 concurrent Hashmap 来实现的。


好，具体这些缓存这是不是我们的重点？那么我回过来，我们接着来看到这里面，这是进行一个build，一个过，那么这样最终会得到我们一个 service intense list supplier，那么我们这个初始化的过程就完成了，那么我们执行跳过去。靠，好，我们进行 F9 跳过去。好，这是我们在获取的对应的我们 service instance 实例的一个过程，把这个断点取消掉。


现在我们看这里面现在到了我们的嗯， react load blanks 这样一个过程，在这里面我们获取到对应的我们的 load balance，看的factory，那么现在去通过这个构造我们的负载均衡策略，那么负载均衡策略这里面我们默尔使用的是一个轮询的负载均衡策略。


好，我们继续，那么我们看一下这个负载均衡策略，它具体的一些实现看，我们看这里面它是怎么去实现这个负载均衡策略的，这里面我们看自动它这选择的一些服务，最终它会通过 process intents response 去处理。这里我们看在整个是 get instance response 的过程，我们看这个方法，在这里面有一个就是当前一个计数器，它每次之前就会进行制自争的过程中，它进行一个轮询的选择，是根据自争这个值跟我们这个服务实例进行一个取余，当前是得到了对应的索引位置，那么获取到这个实例通过一个 detailed response 返回过来。


好，那么我们接着去之前我们跳过我们这个当前，现在我们可以看到它是通过我们的 supplier 在进行我们的这个选择的一个过程。好，我们在这里面通过 supply 它真正去获取到我们对应的这个时。好，这里面我们看到通过 get Instant response，我们得到一个 CVC service instead，我们继续这样，我们现在返回到我们这个，我们可以看到在这里面我们包装的这个底票的 response 这个实例。这实例的类型是 macos service intense，也就是我们基于 neckled 获得到了一个服务实例。好，得到这个实例，我们把结果返回过来。


好，现在来执行完成。那我们看一下我们得到的这个实例是什么呢？我们的实例是 safety intense，它是我们的 19216810. 227，对应的是8085。得到这样一个实例，那么我们看一下，最终我们获取到这样一个服务实例，这样我们这个初始化以及我们在执行的过程就已经执行完成了。


哦，我们当前的负载圈出来是轮询，那么我如何验证这个轮询是否真的是轮询呢？那么下面我这里面还有一个，是啊，验证这个负载均衡的一个客户端，那么这里面我们做了 for 循环，就是循环 10 次。那么我们现在这样快速执行一下，我们看一下它的，通过对它的结果的一个分析，我们来验证一下这个轮询的效果。好，他现在已经执行完成，我们现在看一下他的结果，这里面我们得到的结果是这样对应的，我们看 848283858423 这样一个，只要这个列表的顺序变化了，就是确定了。那么我们现在就是一个轮询的过程，比如说我们 4235 这样一个过程，可以证明它是一个轮询的一个效果。其实这个验证的意义其实并不是很大，只是说明我们做一个客户，做负载均衡策略，它是一个严谨的一个过程。好，那么回到我们的PPT，那么我们在这里面跟大家介绍了 load balance 核心源码解析，主要是它一个初始化的流程以及它执行的一个流程。那么我们对于核心源码解析的内容我们先介绍到这里，同学们，我们下一节再见。

