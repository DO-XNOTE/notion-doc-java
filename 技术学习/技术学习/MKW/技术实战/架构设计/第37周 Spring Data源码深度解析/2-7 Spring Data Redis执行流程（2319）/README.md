---
title: 2-7 Spring Data Redis执行流程（2319）
---

# 2-7 Spring Data Redis执行流程（2319）

[image](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/5c6ab67b-afb5-481c-ab25-31d0a1df237e/SCR-20240814-ifnv.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UZYSWWG2%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T232137Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDXcRk%2BxnjxdsAURqAO8dMjDhkapNX7pKE%2BowkBbWvq%2FwIgI2DWJaGXLROrHVV3DhzdjyEy4K8Tj647B4qRV2I3V2QqiAQIxv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDNzZXC%2BP2lfZXD2LvyrcA6JyPtene8hYox2ceP5yJPTyaxJiC7W%2BMhFTEqejuH8bnNadF6PwNH0Wf7TYnTm0za0bxmkGUbSoTksD19xJhC8BEarCOnJ%2BLn4yoaXr8jaIneVAFDgf7EpTjBXrZHRm3zEaMrsC8gp2i%2Fgy4eNt%2BPeZRP1I4VvnII%2FOueuFUJzX9IAp800rKwYV8w9dDhpXP2PL%2B00bXQCoY1aa0xI%2BvUs8zHh2BesL4zyzGaDYR22VBqFJqP%2BwwI%2FMgq5qYDmO5%2BHMIY6J1CWe59xm%2BEdE%2FkJTkVUnqHgckvBOIlsuOi178YXUa8Cex2JtBneugyU9tibd0%2BTW3G%2FSUZGRZYgxozzMGOEy5QaCHRHD7Cseiz52g6rIXVKIE1c%2B5QaJyi2%2Bra7MAt%2FJ0LSIGpcWY4NVi4hnoOWMxqg5FVKfXBxxdvrWBKHCst3YYvAVTMviuCdWyHQUzr%2F57rksrqEu3QPrATkWOvt36obTmXFZY5opxAQKWUMvG5vsXVDNiZGYA%2BcpMEjUfGD8snOXKYQ8gePj%2FBFhWV3VCmVUyvNx1gx7Q7W8d90g5AD2Nppihci3pWAYxll0zVlXhDPQXXtNClSj8ocqWgF2wXAcUqSYi9GVPVwx71UBDRWLOMODEh%2BOMPy3%2F9IGOqUB24G5MvRsn8XOo3yu2aTrDqsaCzX1YrOyKn7%2BpHXLWFJ0PtlYkESrhPFEBYftUFd4MjSfDaL%2Bp6ZEjWZGwzl39RLXE%2BMS8ExcoReS1Z2%2Fy%2B878cB3V9zXTlsTCvaaNr29U0xhLa02gS8qLC6wuQXgZf7JTkAI5pRYsbmJfGPHjn5n9QxJw3HtXuLZoTHE%2FPvXcPMqBBf5a%2F%2Fglz5N8I9bOcGiuYov&X-Amz-Signature=f92f68971eb6761838445072f9feb33f4095b589668296af5fd26d950e8ac1a9&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

[image](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/99012898-2d6e-4180-8d6e-dab45b3c3751/SCR-20240814-idxz.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UZYSWWG2%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T232137Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDXcRk%2BxnjxdsAURqAO8dMjDhkapNX7pKE%2BowkBbWvq%2FwIgI2DWJaGXLROrHVV3DhzdjyEy4K8Tj647B4qRV2I3V2QqiAQIxv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDNzZXC%2BP2lfZXD2LvyrcA6JyPtene8hYox2ceP5yJPTyaxJiC7W%2BMhFTEqejuH8bnNadF6PwNH0Wf7TYnTm0za0bxmkGUbSoTksD19xJhC8BEarCOnJ%2BLn4yoaXr8jaIneVAFDgf7EpTjBXrZHRm3zEaMrsC8gp2i%2Fgy4eNt%2BPeZRP1I4VvnII%2FOueuFUJzX9IAp800rKwYV8w9dDhpXP2PL%2B00bXQCoY1aa0xI%2BvUs8zHh2BesL4zyzGaDYR22VBqFJqP%2BwwI%2FMgq5qYDmO5%2BHMIY6J1CWe59xm%2BEdE%2FkJTkVUnqHgckvBOIlsuOi178YXUa8Cex2JtBneugyU9tibd0%2BTW3G%2FSUZGRZYgxozzMGOEy5QaCHRHD7Cseiz52g6rIXVKIE1c%2B5QaJyi2%2Bra7MAt%2FJ0LSIGpcWY4NVi4hnoOWMxqg5FVKfXBxxdvrWBKHCst3YYvAVTMviuCdWyHQUzr%2F57rksrqEu3QPrATkWOvt36obTmXFZY5opxAQKWUMvG5vsXVDNiZGYA%2BcpMEjUfGD8snOXKYQ8gePj%2FBFhWV3VCmVUyvNx1gx7Q7W8d90g5AD2Nppihci3pWAYxll0zVlXhDPQXXtNClSj8ocqWgF2wXAcUqSYi9GVPVwx71UBDRWLOMODEh%2BOMPy3%2F9IGOqUB24G5MvRsn8XOo3yu2aTrDqsaCzX1YrOyKn7%2BpHXLWFJ0PtlYkESrhPFEBYftUFd4MjSfDaL%2Bp6ZEjWZGwzl39RLXE%2BMS8ExcoReS1Z2%2Fy%2B878cB3V9zXTlsTCvaaNr29U0xhLa02gS8qLC6wuQXgZf7JTkAI5pRYsbmJfGPHjn5n9QxJw3HtXuLZoTHE%2FPvXcPMqBBf5a%2F%2Fglz5N8I9bOcGiuYov&X-Amz-Signature=7b0590e421e70d0d1dadaae78645a0fc594693cea9ca6cb1d2126a55741cd742&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

那么接下来去看一下 spring day 的 Redis 的一些初始化流程，这里面我们介绍 spring day 的 Redis 的初始化流程，我们还是基于 spring put 的工程去构建。对于这里面，首先我们更关注的是 Redis 的 auto configuration，这里面有两个autocommon，一个是 Redis auto configure，另一个是 Redis 的 reports rate auto configuration。


对于 Redis 的 auto configuration，它其实做了两件事，一个是构建我们的 Redis connection，这里面 Redis connection 它依赖到对于 connection configuration，我们基于一些配置去初始化我们的 Redis connection，这里面会涉及一个是 LETTERS 和 Jadis 这两个配置情况信息，同时我们基于这两个配置信息去构造我们的 Redis template，还有我们的一个 string Redis template，因为我们知道 string Redis template 是 Redis template 一个，我们可以理为特殊化，也就是本身 Redis template 它是基于 object 作为 KV 的 string Redis 我们基于 string 作为一个 KV 的存储方式。


那么对于 Redis repository 的 auto competition，它实现的内容其实就参考了我们对应的 enable Redis reported 这个注解实现的功能来实现的。它主要是我们引入了通过 import 引入了 Redis report register，那么基于这个 Redis report rejection 引入对应的 Redis report configuration extension，也就是我们基于 Redis 的 report 配置的一些扩展信息，对于这里面的信息，我们主要关注它引入了对应的是 Redis repository factor being，对于 factor being 和对应的 factory 它都会包含进来。
我们知道对于 Redis report factory 它是继承了对应的是 report factory support，其实这里面还涉及到我们的 KV 相关的一些信息。对于我们通过 reposite 注意中生成我们的相关的代理，它这个代理的 topic 也就是我们的 simple key value 的repository。


这里面我们看一下对于 Redis report configuration extension 它里面做了哪些事，其实它这里面主要是定义了我们相关的一些底层的我们 Redis k v 相关的一些操作，这里面我们通过 Redis k v 的 template 来去实现，其实这里面也就是对应的是 Redis 的 operation 相关的一些实现，同时它也定义了 register KV 的Adapter，基于 Redis KV 的 Adapter 跟我们的对应的KV，我们的 map KV Adapter 进行一个关联，我们可以做一个对应的一个替换。那么我们可以基于我们的 showcase 的代码来去验证一下整个这个初始化的流程。现在切换到我们 sowcase ready 的这个工程模块，那么这里面呢？我们对于这个工程模块的结构跟我们前面看到的对于SOCASE， GPS 类似的，但是这里面有一些区别，我可能大家会简单介绍一下。


首先会拿 palm 文件，对于 palm 文件我们的依赖区别肯定是有的，首先看我们这里面引入依赖是使用 spring put started 的 did Redis 作为我们 spring did Redis 应该以依赖，那么对于 Redis 它的驱动，我们这里面选的是 Lettuce 的 call 对应Lettuce，而我们没有选嗯，Janice。当然这里面我们换成 Janice 所有的功能其实是没有什么区别的。


接下来我们看一下底下的一些依赖，我们就不用过多的叙述了，它都是一些常规的依赖，像我们的 starter Web 和 sort accuator。那么我们来看一下我们对应的关键的区别，就是我们这个 user 对象，那么对于这个 user 对象，我们注意一下，对于 spring day 的 GPT 里面，我们会用 at entity 进行修辞，这里面我们看这里面。
对于Redis，我们使用的是Redis，哈希，这里面我们指定了一下我们的名称，这里面的名称其实我们可以看到Redis，哈希它其实是依赖了我们的 k space，对于我们的名称的内容其实可以对应到我们的 k space 里面的value，其实这样有一个阴阳这样一个对应关系。


还有一点就是我们这里面的ID，这里面 ID 我们注意一下，我们 ID 引入的是我们的 spring date 对应的 notice ID，以及后面还有我们如果说是需要我们做查询条件的话，这里面像name，我们通过 index 的来进行一个修辞，这个 index 的这个注解也是来源于我们的 spend Redis 这样一个下面的 index 的，它并不像我们 spring data DPA 里面那是关系型数据库，我们可以直接通过命名查询去查找我们任意的属性。那么对于我们 Redis 的话，如果说需要进行查询，我们必须在这里面加上对应的索引，那么页面 Redis 只有建了索引，它才能作为一个条件进行我们的直接查询。


那么其实主要的区别还是就是在我们 user 模型的修饰上面，其他的我们可以理解为基本上是一样的，我们可以看到这里面有我们数据库的初始化，这个初始化的内容其实也是相似的，只是我们做了一个改进，当我们发现我们的 report 任务库里面有数据的话，我们对于我们数据库的内容进行一个删除操作，我们 delete all 同时再进行一个嗯操作。这里面对于 g p a 的话，我们使用通常使用 MySQL 或HR，它会有自增 ID 的一个计算逻辑，那么对于Redis，它也可以自己去填充ID。当然我们为了让这个 ID 更具有一个可预见性，我们这里面的 ID 也是手工指定了，指定完这个ID，我们可以拿 ID 作为我们的查验条件进行一个查找。


好，这是我们可以看到的一些区别的一些东西。对于我们的 user repository，这里面的区别主要是我们继承了我们的 k value 的reposure，其他的并没有什么过多的区别。现在我们知道了这个 Redis 它的工程结构，那么现在我们来去了解一下它启动的过程，那么启动过程我们基于 spring boot 启动，所以说我们更多的先关注一下 Redis auto communication 出了哪些事情，我们再看一下 Redis REPORTS auto complication 出了哪些思想。


好，那么这里面我们来去看一。首先我们来看一下这是我们的 Redis auto configuration，对于 Redis auto configuration，我们看一下这里面的配置信息，首先它是需要依赖一个 on class 的条件，就是说我们当前程序上下文是包含我们的 Redis operation，那我们看一下 Redis operation，它是在对应的是 string day 的Redis，也就是说当我们程序里面只有依赖了我们的 string did Redis，那么这个 auto competition 它才有可能去生效。同时它也依赖了我们这里面的一个属性配置，这里面的属性配置是 Redis property。


对于 Redis property，我们可以看到它里面定义了一些跟 Redis 创建链接的一些信息，它对应的前缀是 spring Redis，我们可以看到这里面URL，我们这里面有host，我们的 username 等等，password，我们的端口号等等是否 SSL 等等这些信息。


好，那么我们还回到我们的 auto configuration 这里面，我们看到它里面是通过 import 引入了两个 connection 的configuration，这里面一个是我们的 lattice 和我们的jetis，这里面它其实实现逻辑是一样的，就是说我们可以看到对应，嗯，如果说我们程序里面依赖了我们的 lets 的话，它会优先使用 let us 作为我们对于我们的 collect resource 的一些创建的一些默认的驱动。这里面我们看到它是构建我们的 letters 的 connect factory，构建成功，通过这个 factory 去构建我们对应的我们 Redis 的一些连接器。好，这是我们可以看到这是对应的是 let us 的情况，那么我们看一下 Janice 的情况，其实是类似的，它也是看一下我们当前有没有引入对应 Janice 的依赖，那么引入了这个意思，依赖它去尝试使用我们的 Jettis connect factor 去创建。


其实对于我们 Redis auto configuration 以来，它通过不管是 LETTERS 还是Redis，只要它创建了我们的 Redis connect factory，那么如果说有了 Redis connect factory，它会基于 Redis client factory 构建我们的 Redis template，我们可以看到这个 Redis template 它对应的 KV 都是 object 的对象，那么我们知道 Java 的 object 对象如果存储到 Redis 里面，这个过程都是需要一个进行序列化的过程，那么其实我们可能通常我们是使用 string 注意我们的 KV 去存储。那么这里面我们更建议大家去使用 string Redis template 进行我们相关的一些数据库存储的一些操作，那么这里面也跟我们构造出了我们的 string Redis template，这是我们的 Redis auto communication 它注的事情，它主要是创建出了 Redis template，我们可以用它进行我们 Redis 相关的一些操作，那么接下来我们看一下 Redis 的 reports auto configuration，那么这里面我们可以看到它也是对于 unclass 的一个校验。


首先它是需要依赖我们的 enable Redis repository 这个注解，那么引入这个注解说明我们对应的 string did Redis 这个就是引入进来了。同时它还需要要求我们当前的上下文是具有 Redis connection taxi，也就是说我们当前这个 Redis 的链接器它已经建立起来了。同时我们看到后面它还会有一个排序，比如 auto communication oft，也就是说这个 auto confusion 它在执行的过程一定要在 Redis auto configure 之后，为什么呢？因为我们首先它是需要依赖 Redis connection package 和bin，同时它在执行的过程它还要依赖我们的 Redis template 相关的信息。


其实这里面它最核心的事情是什么？也就是我们的 import Redis report rejects，这个我们刚才也给大家去介绍过了，在这里面最重要的一点就是我们的 Redis report configuring extends，他去跟我们构建我们需要的这些类似于 Redis Adapter 等一些信息。这里面还涉及到我们的 enable repository，也就是说明我们去启动我们的 Redis 的这些 reposure 的一些操作，也就是对我们的 repass 的接口进行代理构造中对应的代理。那么我们这个启动的过程在这里面会我们可以看到 Redis report configuration，它也继承了 KV 对应的这个配置扩展器，这里面会有一些跟我们 Redis 相关的一些 bin 定义文件的一些注册。


好，这是我们可以从这里面去了解一下我们整个这个启动的过程，那么其实最终它在启动的过程，它还会依赖到我们这里面的 Redis report effect bin，那么基于 Redis REPORTS effect bin 构建我们的 Redis 的操作，我们简单了解了这个我们的制动装配它注的工作，那么接下来我们可以通过单元测试我们来启动一下，我们看一下它制动装配的一个过程。那么这里面我们的 user report retest 它实际的过程也是类似的，我们这里面通过 debug 的方式进行启动。


好，首先我们可以看到这里面会我们定位到了 Redis report configuring extends，这里面比较关键的一点就是我们看到是通过 be independent builder，它进行一个 root being defined 一些构造，它构造的内容就是我们的 Redis key value 的template，其实这就是我们最原生的跟，我们数据库跟，也就是跟 Redis 操作的一个template。这个可以参考一下 GDPC template 它注的功能，我们就大概理解这样一个它的一些定位。好，那么我们现在跳过这个断点，我们看下一步它到哪里，这里面我们看到也是在我们的 configuration extends 这里面，我们看它去获取我们这个注解的标记，也就是我们的 Redis 哈希，那么我们跳过我们下一个在这里面它是我们对于是 report factory support 的一个构建，其实我们可以看到当前这个类，我们可以看到 4 现在是定位到 key value reports factor bin，其实真正执行的是它的子类，它的子类就是我们的 Redis report factory bin。这里面创建这个 report factor 的过程，我们可以构建出它是 report factory support，其实我们这里面的是 Redis report factor bin，其实是这个 factor support 的一个子类。其次也就是返回了我们对应的这个 factor bin。


好，我们继续，这是我们看返回我们对应的 Redis report factory，这里面是 Redis report factory 构造出来这样一个内容，它里面传入的对象是涉及到我们的 key value 的operations，这里面的 operations 和我们的 query Creator，也就是构建我们的查询对象的一个构造器，这里面以及我们的 report requiry type 一些类型。好，那么我们继续跳过这个，现在我们可以看到它是来到了 report factor report 这里面是 get repository，那么 get report 这个过程就是通过我们已知的这些条件来来构造我们这个代理类的实现。


在这里面我们可以简单跟一下看一下，首先他会去判断一下我们的 report INTERFACE，那不能为空，那么当前这个 INTERFACE 就是我们的 user report 以及相关的这些 Freezman 的信息。好，我们继续。对于这些 start APP，我们在介绍 spring framework 的过程中也介绍它，其实我们是在记录一下我们应用程序启动的一些过程，我们可以简单去看一下，我们在这里面首先是 on event，也就是说发出一个event，一个我们看这里面的注解描述是 spring day 的 report init，也就是说我们的 report 信息正在启动，它启动了标记。这里面是 repositer interface reporter interface，也就是我们的 user reports，也就是说它会把这些注意一个指标信息记录在我们的一些 metrics 里面，我们可以通过一些系统去获取到这些 metric 信息，了解我们系统启动的过程。好，那么这里面我们看它进行一些 Tiger n 修辞，也就是我们信息的一些嗯，标记。


另外这里面又是一个 store 的 step 的一个 event 事件，这里面是 spring state 的 reports metadate，也就是说我们初始化成 Meta date 一些相关的信息。好，下面我们获取到对应的 Meta date，这里面我们看到对应这个 start a step 它就结束了，也就是我们 Meta date 获取与完成。


我们看接下来是一个 composition 的一个step，就是一个组装的一个过程，这里面我们可以看到也是打上这个 k 的标记，记录一下我们处理的一些信息，它也是对于 user repose 一个操作，这个我们接着跳过。好，那么我们现在是可以看到真正我们去处理的过程，我们直接过来了，这里面我们看到它是在构建一个 simple key video 的一个reposure，它里面对应的参数一个是 int information，另一个是 k value 的operation。 q value operation 它的一个实现，也就是我们的 Redis template，也就是 Redis k v 的template，我们可以从这里面看到对应的 operation 是 Redis carry term 的一个实现。


好，我们继续。好，现在我们到了 Bing auto 的一个实现，现在我们可以看到这里面是通过构造方法去构造出我们的代理的实现类。好，我们跳过。好，现在我们获取到了我们的一个 report 的一个代理类，那么这个代理类也就是我们对应的，我们可以刚才是跟进到对应的实现这个 talk 的就是我们的 simple key value 的 policy 的一个实现，那么这个代理类构建完成以后，我们现在这个被代理的这个原生对象构建完成以后，我们需要创建我们一个代理。那么这个代理是使用 AOP 的代理进行一些包装，这里面的包装我们定义了几个advice，那么我们待会可以看在执行的过程中了解一下真正执行涉及到哪些advice。


好，现在我们可以看到整个这个代理类已经构建完成了，那么我们这个代理类构建完成以后，接下来是一些 protect factory， protected factory 我们大概知道它是对于我们输出内容的一个减资，我们对于不关心的这些相关的信息可以把它减资掉。


好，现在我们这个 repose 代理对象已经得到了，那么我们这会儿就是已经得到了我们相关的信息，现在我们跳出断点，那么跳漏断点现在就已经到了我们执行的阶段，那么我们先跳过，待会我们先看一下执行涉及到的一些API，以后我们来再通过 debug 的方子跟一下执行的效果。


那么 spring did Redis 的初始化流程我们先介绍到这里，接下来我们来看一下 spring Redis 它的一些执行流程。对于执行流程我们这会儿已经得到了我们 repastary 的这个代理类，那么对应它带零点，我们知道它原生的对象，也就是我们的 simple k value 的repository，我们基于 JDK 的动态代理来进行我们的代理实现。同时在代理的过程其实它也会涉及到我们 AOP 的拦截， AOP 拦截里面这里面我们关注的是三个interceptor，这里面首先是 expose invocation interceptor，这个我们跟 JPA 应该有一些似曾相似的感觉，其实 spring day 的 Redis 它这个代理内相比 spring day 的JPA，它这个 intercept 少了几个。


现在比较重点的就主要是三个，我们这边是 query executor match 的 intercept 以及我们的 implement must inclusion except。其实我们重点还是关注的 query except must intercept，于这里面我们最终还会涉及到我们的 reposit 的 match 的invoke，那么在 GPT 里面也会有这样一个对象，只是这个对象 reposit master invoke 它的实现是有些区别的，比如说对于我们底层实现的这个invocable，对于 invocable 它的实现，对于 spring day 的 GPA 它是对应的是 DPA Pod tree query。


那么对于我们这里面 spring day 的Redis，它是 key value 的 Pod tree query，对于 key value point tree 块，它底层使用了我们的 key value operation 进行我们 Redis 相关的一些实体的一些操作。那么现在我们接下来通过 debug 跟一下，看一下效果，那么在这里面我们通过跟进去，我们 F7 跟进来，在这里面我们到了我们的代理类进行执行。


此前我们来看一下我们的 talking 的对象，我们的，可以看到我们获取到的 talking 的对象是对应的，我们可以看到是 symbol k value 的repository，接下来我们获取到我们 AOP 的这个链拦截气链，对于这个拦截气链我们可以看到对应这个连接气链，它里面的元素是有三个，这个分别是 expose invocation intercept 和我们的 query executor mass 的intercept。还有这里面对应的也是一个可实现的一个方法的 execution intercept，那我们继续我们进入。好，在这里面它会到我们对应这个 invoking 的执行，我们再跟进去。好，现在是到了我们的 expose invocase Intershaft，称呼我们在执行 GPT 的过程中也要执行这个Intershaft，它其实也就是把我们的 old invitation 跟我们当前的 master indication 做一个替换。好，继续我们进入。好，现在到我们比较关键的是我们的 query excluder method intershaft，在这里面我们还是根据我们的 Mast 方法去获取到我们对应的 execution Adapter，在这里面获取，我们可以看到这里面是一个嗯嵌套的调用，最终会执行到我们的 do invoke 方法，我们在这里面点 do invoke 方法进入这里面获取到我们的 mess 方法。


在这里面我们去看判断一下我们当前 mess 是否是一个嗯 query 方法，当然我们这是一个 query 方法，会见在这里面去获取我们这个方法对应的 reports mass 的invoker，也就是我们的调用的这个执行器，在这里面我们可以看到它会构建我们的 Meta date 信息， Meta 信息在 case 里面不存在，那么我们构建处理源把它放到 case 里面，以备我们下次使用的时候提高我们的执行效率。


现在我们看通过我们的 invoke case metadate 进行我们的 invoke 执行，我们也跟进去，跟到 invoke 我们可以看到这里面我们会选择是读 invoke 的方式进行执行，那现在我们到这里面，我们获取到 invoke 的相关的一些信息，我们可以看到这里面是 invocable 去进行invoke，同时这些我们的AUX，我们的一些参数信息也就传入进来我们进行执行。


好，我们现在没有好，我们跳出这个，现在我们到了我们执行的这个过程来执行过程的过程，我们可以看到这里面我们首先是一个构造，我们的 parameter access，也就是我们的一些参数的访问器，这里面构建我们的 query 对象，我们的 key value 的 query 对象。通过我们的 query 对象进行一个如果说需要我们进行我们的属性的一个 protection 进行裁剪的话，我们进行裁剪，不需要的话我们就直接执行。这里面我们开始对于我们的 process result do exult，我们进行我们真正的一个处理，我们现在跟进去 do exult，那么这里面我们看到如果说它会对当前这个 query mass 的进行一判断，它是 pets query，或者是它是 slice query，那么进行我们下面的操作，我们这个是嗯 find by name 它嗯应该不属于这样，它并没有一些分析者相关的一些参数。


那么首先再看一下它是不是一个 collection query，因为我们返回的是个list，所以说它属于一个属于我们的 collection query，它属于执行到这里面，那么在这儿我们可以看到它会依赖我们的 key value operation 进行我们的一些真正的一些处理，那么其下面的一些内容它就归到我们的 key value a person，我们可以简单跟一下，看一下它的过程。


在这里面会进行我们执行的操作，现在结果执行完成，我们可以看到我们已经回到得到我们的 result 对象，这个 result 实际上是一个 user 对象，我们的 user ID 是 0 相关的一些信息。好，那么到这里面我们这个结果就已经执行完成了，执行完成以后它会进行一些嗯事件的广播，如果说我们有哪些相关的一些监听信息的话，可以去监听对应的一些信息。好，我们 result 结果返回出来，那么整个我们这个过程就已经执行完成，我们现在跳过亮点执行完成。


好，那么这里面我跟带大家去了解了一下我们此轮队的Redis，它执行的一个过程。其实我们主要还是了解一下我们对于reposry，它原生的这个代理类，也就是它原生的 topic 是 simple key value reposary，它整个过程还是通过我们这几个 AUP 的拦截器 interceptor 进行我们的拦截，进行我们一些扩展的一些处理，最终它会通过我们的 k value PORTAL tree query 依赖我们的 key value operations 进行对 Redis 相关的一些操作，那么我们关于 spring date Redis 的一些源码的介绍就先介绍到这里，同学我们下一章节再见。

