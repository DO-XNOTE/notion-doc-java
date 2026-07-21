---
title: 2-7 架构设计-应用执行器Actuator-2（1444）
---

# 2-7 架构设计-应用执行器Actuator-2（1444）

[image](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/5ce5f954-67fc-4609-9f61-7279c0193fc9/SCR-20240803-jwwc.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662QQZSSKR%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T231956Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIBesW5EMlw09emneELvUU92TudiM2IlZ3Z%2BEWr06j5f6AiEAzM%2F9ws5eul01C4xer5U4JOpgopfHhQl0VQsSPctTFSUqiAQIxv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDMvRv046CiRy3mhJDCrcAw7UW0UA4CpiQ6Qrti3zpjO6JG1J7w05mOMKND0Co6pPzOqOlKpxkEREljWCzpfQWLT6vJmDr7Ycs%2BB5S8N3IPW%2B0VBBL3hsa8Sy4s%2BdDw9mGjiUaLDR2E0CqKasGE2aifCuw8LP%2BXYXPWNsjMwsbx%2BJXqg3csK%2BjAG4PPsarhzmskQfxuqJRcnAF127kFZIx5ti2qLpEbo3dS6ktgTUovdJnNCt0rUxfB7rSN8nHdlMvuq07Zom%2BM4nwavQRUjM82NhU7w5Ii6OYQC1AkVF6dqNKiC9iCLCkP1KgJMaUPt6isAN0wrznroT7EwTLkWNEMubjIolPevcljmj%2B5G3wMSSj%2BLWekvniS7taUlEHdQNPQp3zc0plqSDOQuO5CVvJcrxKQy%2FiL4EJQlSWJ7%2B7skvAt8StgP%2FBZ2i9Ka6ehgokd%2BlTrutkzBcWDID41gDCI%2Foi1fLduuZOvlAxoX6Lw%2F9Lg6XDKbLthZimOtYXuKtdEaFjEfoeyCKExHfMmmLmDl18U6I43eBl29orQ6em4Yo091%2FAdmemVIqWpmqIHrD%2Fma%2B%2BWsHGZBPyZQLbdLNzt9fv1XlmlTZOeIIAP2tHOxSbAiSLV8P8nQXFHREKhyLNZHpC2VUklRWZCIQMK%2B3%2F9IGOqUB2NdDgmNRCaoob%2Fd0HpQphRZultHy%2FB4Jrvhp1ZNVgMSr5ED1C6DFJl2Eso7fKx03wlswmyg7lrbb1mn1MT7xjdGET8MKOGhLuqc0n7rdx6Gkt5450Xoc0zLYfBq0%2FD8uPfAtV4v%2BSodtKyMD9BUW8jeJVRNPnejFMqA36G%2FwWS%2F00LOAxWV%2FWNe1%2Bpu7YtlInPDNZri4fNK1g0RDfrfAWkaaFVuT&X-Amz-Signature=f187366aade5961b4c3e1fa3f53d4afa233b1752deecb76bd034f5b4456fd52f&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

[image](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/53b3ca71-a41d-4a99-98b5-808241fd91f3/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662QQZSSKR%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T231956Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIBesW5EMlw09emneELvUU92TudiM2IlZ3Z%2BEWr06j5f6AiEAzM%2F9ws5eul01C4xer5U4JOpgopfHhQl0VQsSPctTFSUqiAQIxv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDMvRv046CiRy3mhJDCrcAw7UW0UA4CpiQ6Qrti3zpjO6JG1J7w05mOMKND0Co6pPzOqOlKpxkEREljWCzpfQWLT6vJmDr7Ycs%2BB5S8N3IPW%2B0VBBL3hsa8Sy4s%2BdDw9mGjiUaLDR2E0CqKasGE2aifCuw8LP%2BXYXPWNsjMwsbx%2BJXqg3csK%2BjAG4PPsarhzmskQfxuqJRcnAF127kFZIx5ti2qLpEbo3dS6ktgTUovdJnNCt0rUxfB7rSN8nHdlMvuq07Zom%2BM4nwavQRUjM82NhU7w5Ii6OYQC1AkVF6dqNKiC9iCLCkP1KgJMaUPt6isAN0wrznroT7EwTLkWNEMubjIolPevcljmj%2B5G3wMSSj%2BLWekvniS7taUlEHdQNPQp3zc0plqSDOQuO5CVvJcrxKQy%2FiL4EJQlSWJ7%2B7skvAt8StgP%2FBZ2i9Ka6ehgokd%2BlTrutkzBcWDID41gDCI%2Foi1fLduuZOvlAxoX6Lw%2F9Lg6XDKbLthZimOtYXuKtdEaFjEfoeyCKExHfMmmLmDl18U6I43eBl29orQ6em4Yo091%2FAdmemVIqWpmqIHrD%2Fma%2B%2BWsHGZBPyZQLbdLNzt9fv1XlmlTZOeIIAP2tHOxSbAiSLV8P8nQXFHREKhyLNZHpC2VUklRWZCIQMK%2B3%2F9IGOqUB2NdDgmNRCaoob%2Fd0HpQphRZultHy%2FB4Jrvhp1ZNVgMSr5ED1C6DFJl2Eso7fKx03wlswmyg7lrbb1mn1MT7xjdGET8MKOGhLuqc0n7rdx6Gkt5450Xoc0zLYfBq0%2FD8uPfAtV4v%2BSodtKyMD9BUW8jeJVRNPnejFMqA36G%2FwWS%2F00LOAxWV%2FWNe1%2Bpu7YtlInPDNZri4fNK1g0RDfrfAWkaaFVuT&X-Amz-Signature=ca5dbb6ad1d4f1e1bacbe3a32f3c5f14a4a6a0f9f5553d18c2a450e4ee0d84cf&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

下面我们开始介绍 accuator 实用实践，我们主要包括三部分内容，首先是配置启用accurator，其次通过源码解析 acuator 的工作原理，最后我们去分析一下核心 in the point 的设计解析。好，现在我们开始看一下，通过源码去分析一下。首先在这里面我创建有 Alecutor 的一个子模块，我们看一下。首先在 palm 里面加入了我们的 string boot story cuter 这个依赖，加完这个依赖以后我们需要做的事情去在配置里面去打开我们的 endpoint Web 的一些设置，在这里面我们设置了包含所有的，接下来我们去看一，这里面是一个非常简单的一个启动类，在这个启动类里面我们定义一个 acuator application，通过 main 方法去执行，下面通过 get mapping in 四个方法。


hello，也就是说把它定义成 from m web m seed 一个方法，我们可以通过 hello 得到对应的内容，这就是整个一个简单的程序。那么执行这个程序它要做哪些事情？我们刚才已经简单分析过了，执行这个程序的过程中，跟 acuator 相关的是它需要去执行这些 acuator 相关的制动装配，那么跟 acuator 相关的制动装配，它也是在用factories，我们找一下，我们在这里面可以看一下。我们特意要选中是 stream boot occuator out configuration 的这个文件，我们可以看到这些文件，很多炸包提供了这个文件。OK，我们在这里面看一下，在这里面可以看到整个里面的内容还是比较多的，我们可以看到对应的 enable auto configuration，它的 k 是大概 100 多项，所以说对应的 value 是 100 多项还是比较多的。


接下来我们看几个 in a pointed out configuration，我们这里面看最基础的是一个beans， ins and point auto configuration，我们进来看一下，从这里面我们看到它的条件表达式也比较简单。


首先这里面只是做了一个 being in the point 是否可用的一个校验，这里面方法集的这个 bin 声明，这里面只是保证只要当前容器里面目前不存在，我们就可以去生成。看这里面它传入的参数是 configurable application context，也就是把我们整个必应的容器作为参数传进来，我们这里面构建一个 ins in the coin，我们自行看一下，我们点进来看一下，它作为参数传进来以后，从这里面我们可以看到 in the point i DS beans，也就是说我们基于 Web 的话 URL 就是beans。


我们可以看一下这个注解，这个注解它有两个参数属性，一个是 ID 默认为空，这里面还有一个是 enable by defailed，也就是说它默认是否开启，这里默认只是true，我们可以看到如果说默认这种情况，它就是开启的状态。这里面我们可以看到它有一个 read operation，也就是个读操作，这个读操作对应的 beans 方法，它构建出一个 application bins，这个对象返回我们的前端去渲染，我们可以跟一下这方法，看一下它构造出 application bins 的内容是什么。


在这里面我们可以看到它首先获取到我们的 spring boot 容器 contact 里面去做一个循环的去获取，获取的内容是什么呢？它首先去得到 context ID，从 ID 里面 ID 对应的这个容器去执行 contact bin 的一个描述性的封装，我们进去看一下它做了哪些事情，其实还是获取到它一个去 part 一个对象，最终这里面会做一个描述符的一个操作。我们看一下描述符的操作内容，其实它也就是做的一些四前式，做一个 for 循环，把我们 being factor 里面的 being dependent names 获取到去做，把每一个 bin 遍历出来，构建成一个可描述的一个必应对象。


从这里面我们可以看到它是获取到跟别名相关的，跟 scope 相关的，以及我们的 factory type 这些内容，我们可以看一下它这里面有哪些属性，也就可以看到它别名 scope type，也就是我们的 bin cost type 和resource，也就是说加转通过哪个 resource 加载的。这里面还有dependence， dependency 就是对应我们的它依赖的内容是哪些？从这里面我们可以看到 being in the point，它是有这么多一个属性，它应该对应的是一个历史的一个结构。好，我们回到这里面，那么我们现在可以去启动一下我们的系统，我们去访问一下这个 beans 的效果，在这里面我已经启动过来了，启动了Email，现在它都是默认值，它的端口是8080，这里面访问的属性是occuator。
好，我们先来访问一下，看一下效果。从这里面我们可以看到我们在执行这个过程的时候，我们看到这些内容，我们刚才看到了 beans 的 in the point，我们点进去看一下内容跟我们刚才看到的效果是否一样的。首先我们看到它里面这是一个对象，它的首先第一个 case context，我们刚才看到它对于容器的遍历，如果涉及到容器的嵌套的话会有更多的。这里面我们只有一场，它默认是application，我们点开 application 后面是ins，它这里面 partner ID 是空，并没有去设置，所以说它并没有下一层的记录，这里面我们发现它有 264 项。


我们展开我们看这里面几个内容。首先我们看到这里面跟我们自己定义相关的，我们可以搜索一下 is educator affection，我们可以看到这个 accurate application，这个 bin 是我们自己创建的，一就是我们的启动bin，我们可以看到它没有别名，它的 scope 是在容器是也就是唯一性的单离模式。它的类型也就是我们刚才定义的 cuator application。


从这里面可以看到它是通过了 spring 的 CG Lib 去做了一些增强，也就是说它并不是我们原生的 accuator application 这个类型，这说明是经过一乘带领的，我们就看 beans depoint 吧，我们从这个所有的 bins 里面可以看到我们的 bin and point，通过它我们可以看到它也没有别名，它也是一个单例的模式类型，是对应的 bins in the point。那么它的资源类型来自于哪儿？它资源类型 class pass resource，也就是说它是通过 being in the point auto configuration to class 装载进来的，确实它也是通过这个自动装备把 being in the point 声明出来的。那么它依赖哪些内容？它依赖的内容也就是我们默认的这个 Web application 的 context 对象，也就是我们容器对象。这是我们关于 beans 的一个看到的效果。


好，我们回来再看另一个我们的endpoint，从这里面我们看另一个就是我们这个Mapping， Mapping s 也是非常用的一个 in the point，我们可以从这里面看到我们所构建的这些URL，比如说在这里面我们可以看到我们通过 accuator bins 能获取到的数据，下面也有我们通过 accuator cats 就是我们的缓存数据。
我们基于这个内容我们去分析一下 Mapping in the point 它的实现。我们这里面先去查找 the mapping in the point auto config reason。好，我们到这里面可以看一下这是它的自动装配对象，我们看这里面的条件注解也相对是比较简单的。


这里面首先我们构建出一个 Mapping in point，这个 Mapping in the point 实现，它只是通过我们输入的参数 application contact 和一个 Mapping describe provider，也就是说我们的一些映射描述对象在这里面直接构建就完成了。我们看后面还有一个是跟 Server Lite Web configuration 相关的，它里面涉及到的是对应的我们 Mapping in the point，它实现的是一个 serverlite Mapping descriper provided，它的意思也就是说实现了基于 serverlite 相关的，就是我们的映射提取对象。下面也是相似的一些内容，这里面是跟 stream Web Mac 相关的一些内容。


好，我们先跟进去 Mapping end point 去看一下，到这里面我们可以看到endpoint，这里面是 ID 对应 Mapping 默认就是可使用的。从这里面我们可以看到这里面是 read operation，是一个可读的操作，也就是对应 Mapping 的方法。它的操作我们可以看到跟 beans 有些类似，这里面也会涉及到一些通过当前的 context 去获取part，直到获取到 null 为子，因为我们整个这个 application 它没有part，它会直接去执行对于 Mapping 的一个映射操作，我们可以看到从这里面它的操作，也就是我们想看到的对象就是 context 的 Mapping s，那么它是通过 Mapping s for contact 这个方法构建出来的，我们可以跟进去。


在这里面我们可以看到它是通过我们的这个 Mapping 的描述对象提供器去做了一个做循环去操作，这里面我们看它是什么对象放映到我们这个 Mapping 的字，从这里面可以看到，首先获取到 provided 的 Mapping name，从 Mapping name 里面去做这些描述对象的操作，我们把它作为对象放进来，可以在这里面它在这个操作的过程需要同时构建出这个 context mapping。


其实整个这个操作我们可以看到从这里面进去获取到它的一些描述信息，这里面有各种具体实现，这个我们就不进入了。从这里面我们可以看到它最终会构建出一个 application context Mapping 的一个对象，我们跟进去看这个对象它里面的内容是什么呢？这个我们看起来是比较简洁一些，它也就是一个map，这个 map 里面有一个 context mapping，我们再跟到这个结构里面看一下它的内容是什么，它的内容也是首先一个 map 是对应这个mapping， string 和 project 里面有 part ID，这跟我们对应的前端映射的 JSON 数据是能对应上了。


我们可以看到 Mapping 对应的首先是也是application，用的 context application 这里面是 Mapping s，跟我们这里面的 beans 的结构是很类似，我们从这里面去做个比较，是很类似的一个效果。只是在这里面它是ins，我们这里面是Mapping，它里面的内容要比 bins 多一些。我们在 is 下面就直接是所有 bin 的一个对象的集合。我们看这里面它涉及到dispatter， serverlite 和 Server Lite， filter 和 Server LETTERS。其实我们重点关注的是 Dispatcher Server Lite 里面的内容，也就是我们刚才映射的这些数据。这里面我们可以找一个我们刚才配置比较熟悉的。


一就是我们的hello，我们看我们定义的一个 get mapping，hello，从这里面可以看到它的方法对应的是 get 操作， hello 对应的 handle mass，也就是说它执行的方法就是我们对应的 acuator application 对应的 hello 方法，从这里面也可以看到它这个 handler 是这样一个操作。大概我们能从这里面去理解这个 Mapping s，它这个 in the point 所做的事情。我们看在这里面我们看到相对比较重要的是 ins 和我们认为Mapping。这里面还有一个我们在这里并没有看到的一个Endpoint，它这个 Endpoint 也就是 SAT down，也就是说优雅关机。


这个 Endpoint 大家应该还有印象，我们搜索去看一下这个 set down，这里面是也是 in the point auto configuration，我们到这里面看一下，我们打开这里面可以看到它的方式也是很类似的，我们直接去构造这个 set down， in the point 我们点进去看一下它这个里面有哪些东西，这里面大家注意一下。


在 in the point 这个注解的过程中， have 不同的地方就是它的 enable by default，它默认值是false，这说明它跟其它几个 in the point 的区别，因为 shut down 太敏感了，如果说这个操作暴露出去以后，很容易被别的外部操作进行一个关机的操作。


我们看一下它的实现操作，这里面我们看到它是一个写操作，一个 write operation，它的写操作做的事情是什么呢？我们看到如果 context 等于 null 的话，就直接抛出对应的 no context to set down，如果说是正常的话，它就直接抛出 set down message，也就是说这里面是 setting down by 就是折键。但是他返回这个操作以后，这个程序其实还并没有关闭，因为这里面提到的是优雅关机，不可能直接类似于我们 Q 杠 9 的方式去把它关掉。


这里面我们要做的事情是首先构建出一个线程，这个线程做的一个事情就是执行 set down，它即便去执行的这个过程，它还先暂停大概 500 毫秒，也就是说等程序运行 500 毫秒以后，再去执行这个容器的关闭操作。到这里面容器的关闭操作也就回到了我们 spring 容器的操作，这个我们可以点进来看一下 string 容器的操作。这里面首先在同步代码块里面去执行 do close 操作，我们看一下 do close 操作里面做了一些复杂的事件处理，既然要关闭它可能要先广播出一个关闭容器的一个事件，如果说是有一些相关的事情可以监听到这个关闭容器的时候，可以做一些清理性的操作。


做完这个操作以后，我们在这里面可以看到如果说没有 set down hook 相关的一些内容的话，我们就在这里面通过runtime， get runtime 去操作这样一些内容，执行完这个以后，其实容器就开始进行关闭了。OK，好，我们还回到我们的 in the point，从这里面可以看到关机操作，这种写操作它也是通过类似的方式去实现，但一定要注意一下它的实现的安全性。好，我们回到我们看到 acuator 的效果，关于 acuator 它的一些内容我们大概先介绍到这里，好，谢谢大家。


