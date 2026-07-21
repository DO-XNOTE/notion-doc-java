---
title: 2-6 架构设计-应用执行器Actuator-1（1631）
---

# 2-6 架构设计-应用执行器Actuator-1（1631）

[image](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/0519221c-731f-457f-9945-d2c13bc825e0/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZOZF7EIT%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T231955Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDmIWD8VcMMes3ljldH52hJc1hyeipnhABfi9ARHbWgaQIhAPfA0ksZdqfJvHdaYly8ZUN0XYhqDTydA4gRmjUwBajdKogECMb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1Igzmvt2Dvs1CI5sGYAQq3ANtS08W6etVNSpRMJYwW6p8Y5%2B3SJKv0HkzS0yHuPwVzTJUF6GUkpEUarj80tNXjchC0ZpFnAsmUXjhTmEj4h7RD12KtwifgcfkXt2ACmWvE5qrIoj1cbVUpIlA%2FWB9fEr6hTaMTxiLBZX9Xy5JmqIr1JCec87xMfBB5JJZHtRVkznVbQ8KwbqgrnUaBWTke2YCgyGdJF7QQ276V8EGcO%2Fbo6ViOVMF%2Ba5jGHGSnLFSRJRkQ6F%2BeXw8wP4MFvnQm5CDBWBIw1xP6dl%2FDBWFlPj0H8%2Bqv0aSdnco%2FNec88lDEMSw5IRKvG%2FRUxDdGxdygQDgbh8hfkJjuMwTfl3KlVJQQ3MtL3trhkceIKfRVw0VgPPEvOs21jyeGPEIzODajpn32Vsjcv44sOXlb9AfgUpzrUYyQlYta9EU%2F%2B05A545cGom4c1UFPkK26uOf93mGbIvdyeX9slalu1RYVAg7cJ7NFNJmLQLt7R4U3LsmFT2B3%2BOKV3spsL%2FHmNCN8V3ZdQMrFyVBHsH8x2TQywTETL4eUeTCf2THCOKYGmasmUeeF8eW%2BpeEu8X8OtTMKRInQVeu36MIPJ7ARCCRPVmeSkgGVTtFd3mhH5HMih0GtwiF7NsPyCVKFRKlTEdszDGuv%2FSBjqkAX6d2KaDuvrzrt4CegOeBCV5vivffcxKCW8HIGJS16g43FPZ8T5qX1ozso1qkSqlLrckNIDA9OEu0CH2KzycDDiQiOW0jMArDsMAla72TUIHY1Pn%2BFFu9MM%2BZlnIYYaE4lDjFX8GXmBa70StPffaU2iOG4davj25H4EUBeAxfqn0mV03NVSOZIL9jBAgZdQKi3cKNYLsfZZTg7kAVfI0hf%2FsHcMk&X-Amz-Signature=7dd4aa007a0d07557efab23dbf697b6c54d371bcec9011eaa61f66ba7d9579f4&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

[image](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/887f975e-170e-481a-9fb3-9f9f97b3a757/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZOZF7EIT%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T231955Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDmIWD8VcMMes3ljldH52hJc1hyeipnhABfi9ARHbWgaQIhAPfA0ksZdqfJvHdaYly8ZUN0XYhqDTydA4gRmjUwBajdKogECMb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1Igzmvt2Dvs1CI5sGYAQq3ANtS08W6etVNSpRMJYwW6p8Y5%2B3SJKv0HkzS0yHuPwVzTJUF6GUkpEUarj80tNXjchC0ZpFnAsmUXjhTmEj4h7RD12KtwifgcfkXt2ACmWvE5qrIoj1cbVUpIlA%2FWB9fEr6hTaMTxiLBZX9Xy5JmqIr1JCec87xMfBB5JJZHtRVkznVbQ8KwbqgrnUaBWTke2YCgyGdJF7QQ276V8EGcO%2Fbo6ViOVMF%2Ba5jGHGSnLFSRJRkQ6F%2BeXw8wP4MFvnQm5CDBWBIw1xP6dl%2FDBWFlPj0H8%2Bqv0aSdnco%2FNec88lDEMSw5IRKvG%2FRUxDdGxdygQDgbh8hfkJjuMwTfl3KlVJQQ3MtL3trhkceIKfRVw0VgPPEvOs21jyeGPEIzODajpn32Vsjcv44sOXlb9AfgUpzrUYyQlYta9EU%2F%2B05A545cGom4c1UFPkK26uOf93mGbIvdyeX9slalu1RYVAg7cJ7NFNJmLQLt7R4U3LsmFT2B3%2BOKV3spsL%2FHmNCN8V3ZdQMrFyVBHsH8x2TQywTETL4eUeTCf2THCOKYGmasmUeeF8eW%2BpeEu8X8OtTMKRInQVeu36MIPJ7ARCCRPVmeSkgGVTtFd3mhH5HMih0GtwiF7NsPyCVKFRKlTEdszDGuv%2FSBjqkAX6d2KaDuvrzrt4CegOeBCV5vivffcxKCW8HIGJS16g43FPZ8T5qX1ozso1qkSqlLrckNIDA9OEu0CH2KzycDDiQiOW0jMArDsMAla72TUIHY1Pn%2BFFu9MM%2BZlnIYYaE4lDjFX8GXmBa70StPffaU2iOG4davj25H4EUBeAxfqn0mV03NVSOZIL9jBAgZdQKi3cKNYLsfZZTg7kAVfI0hf%2FsHcMk&X-Amz-Signature=f389156595263d8d695cc60a24d5f49876a881548cab3d8717e92c50d903498e&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

同学们大家好，这一节我们来学习 spring 步的架构设计之应用执行器activator。这里我们还是通过三方面给大家介绍，首先介绍 Okuter 是什么，如何理解这个为生产环境提供监控信息的activator。第二步还是介绍 activator 公路原理。


最后进行 accuator 的一些实用实践。我们首先来看如何理解accuator。 accuator 首先它是 spring boot 提供运行时数据的一个交互规范，那么又是如何理解系统运行词数据，其实系统运行词涉及的内容很多，这里按我的个人理解划分那四类，大致覆盖应用信息、环境配置以及一些敏感操作。


这里面的信息我们在使数据的交互方式，它可以有 HT Web 的方式，也有 GMX 的方式，当然在 spring 布的一点的版本的时候，它还提供了一个 cell 操作的脚本，在 spring 布的 2. 0 把 cell 的方式去掉了，我想它去掉的主要原因应该是依赖了一些跟 cell 相关的一些栅包，其实是一些很使用场景比较低的一些依赖。


我们为了让大家更充分的理解什么是acuator，我们先看几组操作页面。首先我们看当我们启动 accuator 以后，在浏览器访问 local house 的 8080 accuator，我们能看到这样一组 U L Jason，从这里面我们可以看到它有一些像beans，cats，还有 health 健康检查，这是 info 我们的系统信息以及condition。


这里边就是自动装配相关的内容，这里面还有一些配子属性，这里面是一些我们的环境信息，我们可以指向环境的具体某一个 case 获取它的信息。内容，这里面还有日志相关的信息，这个日志我们可以动态的配置指定日志 k 的级别。同时一些敏感操作，比如像这里面可以对一些堆内存和线程的一些 dump 操作，这里面还有一些我们的监控指标等等。还有一个比较重要的就是Mapping， Mapping 也就是说当我们在使用 spring Web i v c 访问的时候，我们配置了哪些URL，可以通过这里面全部看出来。那么我们看一下基于我的分类，它是怎么去一个构建方式。首先我们看应用信息对应的 info beans mapping condition，它肯定属于应用信息，这些只在启动完成以后基本上是不会发生变化的。那么第二类我们的环境配置可能包含我们的 ENV 的环境信息，我们的 config property 就是我们的配置信息，还有 Logas 这些内容。其实环境信息应该不会发生变化，但是这里面的logger，也就是日志配置信息，我们可以动态修改，刚好这也是 Acuator 的 Endpoint 给我们提供的功能。


后面还有我们的度量指标，这里面度量指标有metrics，health，它各自的功能也像我们分别是去获取应用的各项动态的这些指标。 metrics 我们可以自己定义，自己扩展。 health 也是应用监控状态最基本的，像我们如果依赖数据库的话， health 里面会包含我们数据库的链接是否正常，如果我们依赖 Redis 的话，我们也会 check Redis 是否正常。


下面我看一些敏感操作，其实涉及到我们线上系统的操作，都应该属于敏感操作，整个这些操作应该要去做一些严格的权限隔离，比如说我们对于内存信息和我们线程状态信息，这都是很敏感的信息。当然 set down 关闭我们的系统更是比较严格，如果说把这些端露出来以后，被一些不法分子把我们的系统关闭了，想想就是挺好笑，对吧？所以说这些操作我们都应该去进行一些安全的认证，尤其是敏感操作。


当然了，其实像我们的应用信息、度量指标、环境配置这些也都是相对比较敏感的，所以说我建议大家在使用这些 accuator 的 Endpoint 的过程中，我们一定要全部进行安全校验。接下来我们看一下 accuator 的工作原理。在使用 accuter 的过程中，我们要做的首先是添加 spinput start accuator 这样一个依赖，添加完这个依赖我们的 acuator 才能去生效。那么其实默认的 acute 其实没有几个指标可以看得到，像 info 这样敏感性非常低的，它会默认开启，所以说我们需要按需开启，也就是我们在配置文件里面配置 management endpoint Web exports include，这里面我们根据自己需要哪一些端点的暴露，就写哪些端点的 ID 就可以。但是我们作为课程演示，我们可以把所有的全暴露出来，让大家去了解一个更全面的 end point。


这些开启完成以后，我们在 spring boot 这个系统启动的过程中，它会执行一个 in the point 的一个加载，这里面跟我们上一节讲的自动装配的原理是一样的，它这里面也是利用了自动装配的原理，但是这里面对于这些自动装配的命名，它大概是一个以 in the point auto configuration 作为后缀的一种方式，这样让大家看到对应的自动装配类，我们就知道它大概是做什么使用的。


当然这个约定并不是所有的实现都是参考的，那么如果说我们把 end point 通过 auto configuration 的方式注册进来以后，接下来的一件事就是我们如何把这些 in the point 暴露为我们的一些 URL 访问的。其实不担心，我们也可以想到当这个 endpoint 自动装配完成以后，我们就需要构建一个 Web Mac 的 endpoint handle Mapping。我们看到 handle Mapping 可能应该会比较熟悉，大家如果说对 spring APP Web Mac 的流程比较熟悉的话，对我们印象最深刻的应该就是 Handler Mapping 跟 Handler Adapter，其实在这里面也就是把我们这 endpoint 的 URL 映射到handmapping，每一个 handle Mapping 对应的执行路径就是我们对应的 handle Adapter。


其实这就是我们可以理解为 accuator 整个的一个工作原理，从它从加入依赖到开启配子以及制动装配的执行，以及如何把这些对应的 in the point ID 作为 URL 注册到我们的 spring webrnc 的一些执行流程上。当然在这里面我是主要讲以 Web 的方式访问的这些 in the point，当然 in the point 它还提供另一种方式，就是JMX，这个不作为我们主讲。


等整个构建启动完成以后，我们可以集成一些监控系统，把我们这些监控指标推送到对应的监控系统里面，可以看到一些漂亮的一些图形，这是我们简单看 q 一点制约工作原理的一个初步流程。那么我们接下来更详细的去看一下每一个步骤要做哪些事情。首先我们看我们要添加依赖和配置，这里面比较简单，我们添加的依赖也就是 spring boot STARTER， activator 配置我们默认是默认的，这些 endpoint 它开放的比较少，只有 info 和 hashtag 去打开了，所以说这里面我们是配置一下 management endpoint，这样我们 include 星，也就是说我们把所有的都打开。这里面如果说我们用 YML 配置的话，注意一下这个星一定要加双引号，当然我们用属性文件是行，是不需要的。


接下来我们看加载 accurate 的制动配置，我们看这里面要注意它虽然也是通过 Meta info 下面的 Sprinter factory 去加载的，但是这个文件它跟上一节讲的自动装备，它加载的文件的目录是不一样的，这个我们是在对应的 spring 步的 accuator 的 auto configuration 这个大包里面，我们上一节讲的内容其实是没有这个 accuator 的，上一节我们讲的加载这个 spring 的factory，它自带 spring boot 杠 auto contribution，没有occur，大家知道这个区别就行。


好，我们看一下这个文件的效果，从这里面我们可以看到对应的它这个文件的目录是在 stream 部的 acuator con auto configuration 这个炸包里面，并且这个文件文件的内容也不一样，这个文件内容比如说我们第一好，也就是说这个 innovauto configure 这个key，并且这个 key 里面的这些 auto configuration 它们的一些共同特点，它们都是在 acuator auto configuration 这个包下面做的一些操作。


我们接着去看这些 autoconfigurant 这些自动装配的一些操作。首先我们这里面的自动装配有一些普通的endpoint，比如说就像我们的环境信息的Endpoint，它是这样， enorment endpoint auto configuration，还有一种是一种作为配置的 in the point，这里面我们因为专注于 Web SCP 的这种方式，所以说这里面会有 Web endpoint auto configuration。


首先我们把各个 endpoint 用这种方式注入到我们的容器里面，然后我们可以通过基于 Web in the point 做一些统一的一些配置，比如说我们修改一下我们的基础路径，这些配置完成以后，我们需要把我们这所有的 in the point 注册为一个 MV seed 映射，我们就会得到一个 Web MVC Endpoint handle mapping 这样一个对象，它注册到 MVC 里面，我们就可以通过对应的 URL 访问这些 in the point。


好，我们看下一步这些自动装配的对象。首先我们看一下这个环境 end point 的自动装配，在这里面我们可以看到它的一些条件，首先是肯定是 unavailable 这个 end point，这是什么意思？也就是说在当前条件下，这个 Endpoint 它是可用的，这个可用的配置哪个？也就是 environment Endpoint，也就是说它首先通过条件判断一下这个环境端点是可用的，所以说它才会进行下面的装载。


第二呢它是 enable configuration property，这个它的操作就是说跟我们构建一个属性配置文件，这个大家应该见过好多次了，这里面 at being 就不用介绍了，它标明一个 being 的构造，这里面是 condition on mixing。


being 是指在当前环境下，容器里面没有存在我们这样一个环境端点，它在执行下面的内容，构建我们当前这个环境端点。这就是对于一个普通的 end point 自动装配的一些方式，像一些我们其他的一些beings，或者说 Mapping s 这些自动装配都是基于这样一个原理。那么这些普通的 Endpoint 装载完成以后，我们需要对我们配置的这些 Endpoint 做一些统一配置。我们看一下统一配置这个统一配置，比如说如果说对于 Web 类的，也就是说我们基于 Sep Web 访问的这些端点，我们都是通过 Web endpoint auto configuration 这样一种方式去定义的，我们称之为这是一个配置的 in the point 自动装配的对象，这里面我们可以看到它里面也是首先它的一个条件是 condition on Web application，这个比较容易理解，也就是说执行这个自动装配它需要当前是一个基于 Web 的一个环境，这里面有一个 auto configuration off 的，也就是说对于制动装备的一个排序。


对于 Web 的 Inpoint auto configuration，它要排在 inpoint auto configure 后面，这也比较容易理解，我们可以理解为它是做了一些更抽象的内容，对于 Web 是配置跟 Web 相关的一些内容，这里面是定义一个属性配置文件，这个我们就不解词了，在这里面我们看到它有一个条件就是 condition on missing b。为什么呢？因为对于这个 Web endpoint auto configuration，它的主要实现内容就是构造出一个 Web endpoint discover 这样一个对象，这个对象的目的就是在我们容器里面把所有的 Endpoint 能搜集到，这里面的所有是指外部相关的Endpoint。所以说要初始化这个对象的前提，也就是我们的上下文容器里面当前还没有构建这个b，我们可以看到这是 Web Endpoint supplier，这是discover，其实它们之间是有一个继承实现的关系。


Web Endpoint supplier 它是一个接口，这是它对应的实现。这里面我们可以理解 GDB c template 对应的操作，对应 GD b c template 里面，它这个 on missing being 用的是 g d b c operation，而这里面我们生成的对象是 g d b c template。所以说因为它们是一个接口与实现的关系，所以说可以用这种方式去执行。


我们看后面是我们的如何把这些 endpoint 注册为 MV seed 一个映射，我们看到这里面是 Web m a C endpoint measurement context configuration。这个名称比较长，我们先看一下它的注册条件。它的注册条件首先肯定是 on class，也就是 Dispatch 什么。 net 我们知道看到这个 Dispatch 什么。 net 我们就可以想到 task Web M a C 4 相关的。首先需要有这个 departure light，第二步需要肯定是 on being，也就是说我们的容易器里面必须有这两个实例，哪两个？一个是 departure 的b，一个是 Web Endpoint supplier，这个就是我们在上海页构建出来的这个b。如果说这两个 b in 存在的情况下，我们才考虑构建 Web i m a C 相关的一些自动装配。


这里面我们可以看到像 Web Endpoint supplier，它在这里面会作为一个条件去注入进来，从这里面我们可以看到它是 Web in the point supplier。同时还有一些更基础的，这里面有斯巴 light Endpoint 斯巴涅尔，还有 control Endpoint 斯巴涅尔，它要比 wipe 更具体一下。


对于 Web 来说，我们可以提供 HTV 请求，那么具体直接请求于哪种方式实现的？一种是我们基于 smart 的方式，另一种基于是 spring Web m a C control 的方式。但这里面还会有一些我们对于支持的一些 media type。就是 Endpoint 是哪种类型？不，我们现在默认都是 JSON 类型。到这里面我们能构建出这个 Web Mac endpoint Handler Mapping，也就是说我们可以从 endpoint 的初始化到它 URL 能映射到 4 种 Mac 上面。整个流程是串通了，我们可以回头再过一下。


首先我们要引入 spring boot start a q ator，然后我们配置一下需要把哪一些 in the point 的 ID 暴露出来，需要配置，配置完成以后它就会去加载我们相关 endpoint 的这些autoconfiguration，autocompilation，它这些配置文件是在一个 spring 的 factories 这个里面，它是对应的是 spring boot acuator auto configuration 的扎包。下面这个大家要清楚去哪能找到。


在这里面注册完这些 Endpoint 的自动装配以后，我们需要有一个 Web Endpoint 的自动装配去对它做一些配置性的管理，这个配置这个管理它会得到一个叫 Web Endpoint supplier 的这个对象，它可以从我们容器里面获取到所有的 Endpoint 相关的一些bin，我们基于这个 bin 呢去来注册 Web Mac 的 Inn point Handler Mapping，等我们注册完 Handler Mapping，那么它跟 strong Mac 就衔接上了，整个我们 accuator 的工作原理就是大概这样一个效果。


