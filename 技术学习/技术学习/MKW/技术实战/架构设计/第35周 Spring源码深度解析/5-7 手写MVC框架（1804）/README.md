---
title: 5-7 手写MVC框架（1804）
---

# 5-7 手写MVC框架（1804）

[image](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/f2ebb7c3-ea88-4c75-966a-8a0bd1e6461d/SCR-20240804-bbdw.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XWGIDKKM%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T232034Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCVcpaAbC8LCbOOSRaqnEyqvfEd3CNMwPpS1LGUh2NetAIhAPomFntFFwuxWR3Wft9i7tOGt4fPG4zfqCwjQ8QW5GR%2BKogECMb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgzLZnNfLG%2B4z2yEUTQq3ANJAnMbrkHuPdSngAZyzeoOKi0IlvejemxBslQiGuqq6rElJMn9sJNk4xz5G7QIv%2Fp%2F3liON8gByfYOpF7zTPSvOhXNCpGtigxiNWmrJYFreHzIrjnItiaVfVIZBDU54cP066rbZP4aQIp6sFCgiJ5S2ztRtVJT%2FmvvcvATJv0z9BpofMHEY%2BY5Z%2FYI4WGv08I9%2FShud00ZxzgPg0bXD%2BKkTiqgV4olpXrgC2J7Wjm0yequJu%2BiIrBzuKc7YNd2DRJOJVhb6%2BGl9xrryfzqxg0vFgHkpi2K2LB%2BrFoIHQ7EVxIu2IIq081N7XvsGRI2%2FT2Dl3pH%2FaCmD07h%2B0CxTjutK%2FXNggaGiwaFHr4lcyxJWUfzPlEpJDTdNh3n0oX75yov0YTj9AAiLQDUCTANphd4bz7P8%2FU3G56hvuvWP8T0JZGbkGCc6q65CSb2CTWCkpHYlie3lG9J%2BZiWfnPCOUDelsA3qSPSueqxnkiyeLL%2Bz5trsjFMvOvY%2ByJH7X6qF1YyfOOCCwx52qTIp7gThUKh71yrJcJSeemW%2B6H7mvGqiywq0rYXJhZOiiYzFi7zs8Mp0eOyIGNv1n8R7%2BcS062lTnnb3xb4nguYnS2uUOZ8pSOJBiLcpXmiQc%2BOSDDGuv%2FSBjqkATuuOgJvNkNwuQiHA3ALOyJlAGB%2BFsv5guRaSF68oE%2F2wrNy7kLE6zYGrT96KX9S%2BcsHcmWVGjHUJjM0OSLLT05M15Oz7FkalTDH681x%2BHC8jphfCe4AlgRvHzqJ1SUBj5BSf6%2BGtyQoGaKacB8PYbmibuWv2SzAeoq8gI42fOtrPIMv8PNDViX3Bd8NGilNqcSh3Iyax6E0aYp1RV1f05ZycGky&X-Amz-Signature=cdcf4553d58c7467bd5e96d5d2076fe6cc452e52731679a778ca5da4f96c661c&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

同学们大家好，这章节我们来介绍一下 string 照轮子手写 m a C 框架，那么我们先来回顾一下 MVC 框架的执行流程，对于 spring 的 MVC 框架，它执行流程可以理解，这样，我们通过读写 Web configuration 相关的内容， request Mapping 的内容装载起来执行存放到我们的 handler Mapping 这样一个对象里面。同时当请求过来的时候，通过 handler Mapping 里面 get handler 的方式获取到 handler excusion change，解决出一个执行链，通过执行链里面最终执行我们 handle Adapter，也就执行我们 counter 对应的方法。在执行这个过程，我们会涉及到一些数据绑定和我们一些信息转换的这样一个过程。获取到这些信息内容以后，如果说我们还是使用模板相关的一些视图的话，会执行 model 能 view 进行视图的一些解析，就渲染成我们的前端。但是我们大多数情况下，我们现在都是直接返回 JSON 整个过程，像 891011 这样一个过程就基本上已经很少走到。所以说我们这次走起 MBC 框架，我们的重点是放在 despite 收 LED 和我们的 handler Mapping 以及 handler Adapter。


那么我们来看一下 SPRAM AC 这几个核心组件，我们可以回顾看到，其实在这里面我们的 handler Mapping 和 handle Adapter 是相对最重要的一个内容，我们为了整个实现的更简洁一些，我们跟 4 图相关的内容我们已经不再去实现了，同时这里面有 handle intercept，也就是我们这个拦截器功能暂时保留。


那么好，现在我们来开始手写我们的 MC 框架，还是回到 spring view 这个造轮子的这个模块。在这里面我们还是首先添加一下跟我们 MVC 相关的一些依赖。我们跟 MVC 相关哪些依赖？我们首先要添加 spread 相关的依赖，这里面我们去选择 surprise API，这里面切记要注意一下，我们需要选择一下它的scope，它是provided，如果说这个就不解释了，同时我们需要 json 序列化，我们需要把 json 相关的依赖添加进来。


defend。添加完这两个依赖的话，其实我们 MA seed 这些依赖也就够用了。我们在这里面加上注释，这是 m a C 相关的依赖。好在这里面我们创建 m seed 包，那么对于我们在写 MC 这个依赖层，我们刚才提到了我们重要的是 Dispatch slide 和 Handler Mapping 和 handle Adapter。


首先我们通过初始化的过程解析 Handler Mapping，我们需要一个 request Mapping 的注解的映射，这个 request Mapping 跟我们的 SPM 的 request Mapping 是一致的，我们就可以直接去创建指定它是一个注解，它的实现功能，我们可以快速的去把它可以实现完成，我们可以看到它是需要的运行资执行，它可以把注解放到我们的类型上和我们的方法上。对于这个注解，它在 4 MVC 里面含有许多属性，在这里面我们简化，我们只保留两个属性，一个是这个 request mapping 的URL，另一个是我们支持 ATB 请求的Mest，也就是对应的是 get 还是post。现在去介绍创建我们的 handler Mapping。 handle Mapping 我们先不实现，先把类创建完，那么接下来是我们的 handle adapt。


好，最后来创建我们的 departure shernet。在创使用 discussion surlight 的过程中，我们需要让大家去继承我们的 HTTP sir light。我们看，好，程序来说，我们应该包含两个过程，一个是我们 discussion 带的，也就是我们系统的启动过程，我们启动的过程是需要对我们的系统进行初始化，执行的过程是需要进行系统的一个处理，所以说分别把我们的初始化方法和我们的处理方法暴露出来，对于我们的。 net 来说，我们可以在这面去看到。首先我们来看一下service，对于这个方法来说，所有我们的请求都会打到 service 上面，我们可以理解为这是我们整个请求的入口。


另外还有一个我们初始化的流程怎么去描述，我们可以看到在这里面有一个引起的方法，这个 init 方法，它支持一个 Server configure 一这样一个配置对象。这样的话我们的初始化方法我们的执行方法就暴露出来了，因为我们现在是基于 surlight 3. 0，以后的话我们是不强制要求 Web 的ML。当然我们现在的工程已经没有 Web APP 这个目录，同时也不存在 Web INFO 对下面的 Web ML，所以说我们一切全部使用基于 340003. 1 或者注解的方式。


我们首先对于迪斯帕斯拉的去做一些配置，那么配置的内容是什么呢？你就看我们对于初始化的内容的要求是什么。我们在初始化的过程中，首先我们需要把这个容器对象创建出来，所以说我们可以在这里面写两个方法，一个是隐晦的context，可以把 config 的对象传入进去，那么这样创建我们的方法，这样我们这个方法创建完成。那么第二步我们的 spring 容器创建完成以后，我们需要去初始化我看到的map，初始化 handle Mapping 的过程，我们可以简洁一下，它就不需要我们其他的一些参数了，那你就可以直接把这两个方法完成。这样的话我们首先是初始化上下文容器，那么初始化上下文容器，再初始化我们的Mapping。


首先实现一下我们的 init context，实现这个 appex test，我们需要指定一个包结构，或者一个加卡皮卡类。这里面我们为了简化，我们同时通用于注解，可以直接指定一个包结构的话，就可以完成我们的内容。这里面包结构的配置我们怎么去完成？因为我们可以尽量简洁简化，我们可以把我们的配置配到我们的 init 的参数里面，我们可以从这里面去获取一下，这里面我们可以看到我们可以获取 get init parameter，这里面我们可以去定义一下我们的 base packets，那么在 base package 里面我们可以获取到一个字符串的一个类型，我们把它作为我们的参数传入，这样的话我们的 3 小时间就创建完成了。当然我们可以把创业文作为一个属性变量，我们把这个属性变量的构建出来，这是我们的第一步。


第二步我们要做的是什么？是初始化我们的 handler Mapping，要初始化我们的 handler Mapping，需要对我们的 handler 面进行一个解析，所以说这时候我们需要去做看怎么去实现它的过程。此前我们已经有出来我们的很难的买品，这里面给大家推荐，直接我们把这个作为我们的类变量。


好 handler Mapping 构建完成以后，我们就需要进行一个扫描，那么我们需要把我们变容器里面这些类全部扫描出来，这里面我们要获取到所有 bin 注册的类，那么我们可以在这里面首先获取一下 bin factory，当然我们现在这里面不能直接获取 bin factory，那么我们去里面实现把我们 be infactor 暴露出来，在这里面我们可以接着去获取通过 be infactory 获取到所有 resist 的pass。


我们现在需要对这个 reject class 进行一个遍历，便利的内容，也就是我们去扫描所有里面跟request，也就是跟我们的handler， request mapping 相关的一些内容。我们可以在这里面几个方法让它去实现 scan 的register，它的内容就是我们的一个 Bing class，我们来创建这个方法，在这里面的实现会相对比较复杂一些，我这里面直接去可以快速的把它全程在这里面。


我们对于这个方法请你进行做一个解析，在这里面我们要做的事情其实跟普通的注解解释是一样的，我们要解析，首先我们要把当前这个类里面的 request mapping 它是否存在去解析出来，同时在解析这个类里面所有的方法对应的 request mapping。


那这里面要构建一下我们的 handle adapter，因为 handle adapter 我们 handle 还没有实现。对于 handle adapt 我们需要的参数是什么呢？一个 pass 方法，现在把我们的 handle adapt 操作实现一下，这里面我们的 handle depend 还是一个空白的，对于 handle adapt 它的要求是比较简洁的，我们只是可以把它理解成我们对于一个方法的描述符。这里面我们可以使用 number 的 pass 把我们的需要的内容，我们的构造器，构建出来，这样我们的 handadapter 有了。这里面我们还有一个对应的是 build k 的方法，这样的话也就是把我们配置的这个 request mapping 构建出我们的一个映射关系。那么我们在这里面把这个我们 handle mapping 的内容我们可以逐步来实现。
首先我们这里面是通过我们的 bug 我们来构建一下。对于我们 handler Mapping，我们有时候会要了解一下我们的 k 和 value 分别对应的内容是什么？对于 handler Mapping，它的 key 是通过 request 构建完成的，它的 value 肯定也就是我们对应 control 的方法。那么其他的对于 handler mapping，它一个重要的方法就是 get handler 是需要把我们的一些内容存储起来，那么首先我们需要把我们的映射关系构建出来，这里面的 string 是我们构建出来的k，那么 handle differ 就是我们需要映射的一个方法的一个实现。


这里面我们来首先看一下 get handler 的操作，而在这里面 get handler 的操作，首先通过我们的 request 注意参数构建出我们相关的一些case，那么我们这里面去创建一下这个方法，这个方法实现的逻辑我们是怎么实现的？我是这样去设计这个事情的，其实我们在通过请求去获取这个映射的过程中，我们优先去选择这个对应方法的内容。比如说我们先获取到我们的 request URI，同时去看一下我们请求的 mess 的，如果说能全匹配 URL 和请求方法的话，我们优先获取对应的 handle Adapter。如果说我们使用 request URI 和我们的 mess 的全匹配没有获取到的话，把我们的请求 get pose 去掉，也就是说把它 mass 视为null，再去回去看能不能找到我们对应的 handle Adapter，这样我们有一个优先顺序，能做到一个极大的满足。


好，这样的话我们 handler Mapping 的内容基本上就完成了。其实还有一个如果说我们需要去解析的过程中，把我们的 handler 去注册进来的话，我们需要写一个注册的操作，这里面注册我们就简单去在这里面实现一下。注册的逻辑比较简单，我们就相当于是在 Mapping 里面去设置一个 KV 的一个过程，这是我们这个 handle mapping，那么我们现在还回到我们 despite THREAD 的实现过程去扫描的一个过程的流程，我们在启动扫描 5 handler Mapping 的过程完成以后，我们需要去实现我们的执行流程也是比较复杂的，但是我们这里面把我们执行流程最大程度的简化了，怎么说是最大程度的简化？如果执行过程最终会请求到我们的一个Ctrl，我们可以先在这里面去设计一个Ctrl，我们在这里面加上 MVC 一个包，这个 user Controller 我们可以快速的把它去实现完成。


那么我们看一下这意思，看出来这里面我们是通过 manager 的 bin 去做注解的一个修饰。同时我们这里面使用了 request mapping，嗯，定义了 pass user，在这里面我们定义了两个方法，一个是 index 方法，一个 list 方法，同时这里面都是我们 mock 的数据，可以返回去执行。我们在这里面是对 request mapping index，我们通过这个注解。


此外 Mac 的实现逻辑其实就是类上的pass，加上方法上的 pass 出一个组合，也就是我们请求的过程，它应该是杠 user 杠 intext 来完成，我们就是请求到我们这个方法，这个是我们的杠 user 杠 list 来请求我们方法，这个功能完成。把我们常规的这个 user Controller 完成以后，回到 Dispatch 12 点去实现它的一个操作，我们去实现这个 Dispatch 10 来的，因为我们现在并不关心它是 get 还是 pose 等方法，所以我们直接在 service 来去完成这个过程。


一般情况我们在 Server ID 里面写代码，现在 Server set 里面写代码很少了，但是对于早期在 Server ID 写代码的，一般我们的第一行代码，也就是要注的 4. 0 是对它做一个转换，把我们的 THREAD request 和 THREAD response 转换成我们的 h t p THREAD request response。


那么在这里面我们要去做的是什么呢？我们需要通过 handler Mapping 获取到我们的handler， handler 的参数，也就是快死的handler，这样我们会得到一个Handler，这里面我们需要去做一个校验，如果说并没有找到 handler 的话，那么也就是 handler 为now。对于这种情况，我们知道它应该就返回 404 了，就是没找到我期待的内容。 3L 404，同时我们应该去return，应该就是结束我们这次请求。


如果说我们的 handler 它不为 now 的话，我们可以通过 handler 里面去获取到我们的b，也就是我们容器里面b，在这里面我们一起做了一个引用的一个存储在这里面，同时我们再获取一下我对应 handled 的mess，OK，那么我们获取到当前对象和它的方法的话，我们现在应该要做的事情就是执行这个方法。


我们需要对它进行一次传case，我们执行完成得到返回值以后需要做什么事情？我们通常会对它进行一个序列化输出，因为我们总不能把加大对象直接渲染到页面，所以我们需要对序列化的话，我们通常会使用Jackson，也就是生成 Jackson 的判断力序列化这里面我们去构建一个 object map，我们使用它默认的 object map 实现，那么在这里面对于我们的结果进行一个序列化，这样执行完成会生成一个 json 的对象，我们把这个 JSON 对象作为我们的值渲染出去。


渲染的方式我们可以通过 response get writer，一个写物流把我们的内容写入进去，通常我们写物流写入完成以后，我们需要对它进行一个关闭，好关闭，那么这样的话我们整个这个请求的过程也完成了。好，我们现在来看一下我们这次拍摄是不是来的类，我们这里面去进行一个配置，这个配置的内容也就是我们通过注解的方式去扫描 Dispatch threader，这里面我们配置这个 surprise 对应的UL，这是我们的反斜杠，也就是这里面我们配的一个 init parameter，这里面我们定为 Web parameter，它的 k 是 name 是 base packets，它的 value 就是我们指定的 demo m a C 就是我们这个包结构，因为我们可以看到在这里面我们在初始化 context 的过程中，我们在这里面使用到了 base 派case。


其实我们还可以通过注解的方式扩展更多的一些属性，这里面我们把这个 super service 清理掉，这样的话我们就可以去启动我们的程序。现在我们怎么去启动呢？因为我们没有 spring boot，是不能直接本地系统，这里面通过 main 插件的方式去启动，在这里面我们去添加一下一个载体，没有问载体插件，这个载体插件我们这里面切记要设置一下。我们 spot packing 的方式是栅包，那么因为我们这里面默认的是栅键，所以说我们这里面需要直接配置一下，让它支持栅包的框组去启动。好，现在我们通过 Maven clean 载体状这个命令来启动我们的程序，看到这里面是启动我们的 Jetty Server 的，已经启动完成了，现在我们去访问一下我们的 local host 8080 端口看一下，在这里面我们刷新一下可以看到很快得到我们想要内容，对应的 list 页也是一样，也就是说能得到我们相应的内容。那么如果说我们访问一存在的一个地址，这里面我们看到我们会得到 S04 的一个错误，通过这样的话，我们这个 MV seed 框架，那就是已经写入完成，同时也完成了我们的一个。


对于 MVC 框架实现的是非常简洁的，如果同学们有注意到的话题可以看到其实我们在执行引入口方法的时候，我们根本就没有传入什么参数，因为我们做的这样的简化，所以说可以让我们通过三个类以就是我们 despite 12 月的 handle def 的 handle mapping 就能完成我们 MVC 框架的一个雏。形。如果同学们比较感兴趣的话，可以接着把我们通过参数解析的方式去完成我们 request 到我们 control 参数的一个转化的过程。好，我们手写 Mac 框架的过程就先介绍到这里，同学们，我们下一节再见。

