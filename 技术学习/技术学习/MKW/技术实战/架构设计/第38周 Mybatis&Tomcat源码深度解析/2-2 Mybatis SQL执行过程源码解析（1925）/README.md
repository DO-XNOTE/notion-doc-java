---
title: 2-2 Mybatis SQL执行过程源码解析（1925）
---

# 2-2 Mybatis SQL执行过程源码解析（1925）

同学们大家好，这章节我们开始学习买 Badcase 的 SQL 执行过程的源码解析。上一节我们介绍了配置文件解析的过程，通过配置文件初始化最终完成我们 SQL session factory。那么这一章节我们专注于 SQL 执行的过程。我们知道对于买 badcase SQL 执行的过程可以分两部分，一部分我们通过 Mapper 接口生成 Mapper 代理类进行我们方法的执行。另一个方式就是我们可以直接使用原生的 SQL session 来执行我们对应的正三改查操作。那么不管是我们通过 Mapper 接口还是原生的 SQL session，最终执行的过程都是通过 SQL session 进行数据的执行。


好，那么我们来从这里面去看一下对于我们通过接口和 SQL session，它最终是如何汇聚到一起的？首先我们在通过接口调用的时候，现在也是通常推荐大家的方式，我们通过声明一个接口，这个接口可以通过我们的查询注解或者是对应的 map XML 文件执行我们相关的操作。这里面对于 Mapper 的接口最终会生成一个代理对象，那个代理对象就是通过 Mapper process 生成的，这里面它会通过里面的 Mapper must invocation 进行执行，执行的过程会依赖 Mapper Mast 最终推执行到我们的 SQL session，通过 SQL session 来进行我们操作的一些处理，其实归根结底我们的 Mapper process 最终执行还是对应 SQL system 相关的映射的。 DELETE update select，也就是我们常规说的蒸三改差，我们通过 Mapper process 执行到 super session，这部分理解完以后我们就可以专注的去了解 SQL session 它执行的过程。


其实在我们通过 SQL session 执行的过程，默认会通过我们的底票的 SQL session 来进行执行，那么在底票的 SQL session 执行的过程中，我们会生成一个 map 的statement，那么 Mapper statement 我们可以理解为是上下文参数的一个组合的 VO 对象，真正执行的过程还是通过 IQ Ator 传入我们 Mac statement 这个 a 参数进行一个插入的执行。


执行的过程对于它的实现，我们通常会用的是 simple AQ a 特，其实在 simple AQ 的执行之前，还会涉及到一层开始 iq 一的，也就是我们执行的时候，如果对我们缓存进行一个封装，其实在执行的过程中最终还是把我们执行的操作委托给我们的 statement handler 进行一个执行的操作。这里面会涉及到一个 routing statement Handler 的路由映射通这个路由的 statement Handler，根据我们查询的不同类型去选择具体的一些handler。这里面我们演示一个基于 simple seed man 的 handler 执行的一个过程。其实在 simple seed man handle 它真正执行的过程，它会涉及到首先是对参数进行一个处理，执行完成以后对结果我们的 result handler 进行一个处理，这样一个处理的过程，假如说我们涉及到一些制定义的一个type，一些类型的转换，我们还会涉及到 type hunter。这里面主要是我们可能会把一些枚举，也就是说通常我们对于枚举的一个映射关系，我们存储数据库的话，枚举对应的一些 V6 子，我们反序的话，从数据库获取过去以后，会把这个 value 值转化成对象。


一个枚举的过程或涉及到一个 type handler，现在我们可以通过这个 my badcase 的 study 项目感受一下我们这个收口语句执行的一个过程。这里面我们来看一下我们的 user Mapper test 这样一个单元测试类，这里面我们也是用到了买 badcase test 作为我们分片的一个测试构建器，那么好，现在我们可以去通过 debug 的方式执行我们的操作。


好，我们看现在暂停的断点，这里面的断点是我们的 SL config builder，也就是说我们初始化执行的过程，我们可以看到它里面去初始化这些买白色 config 相关的信息，那么我们跳过这个断点，这是来到另一个断点，也是我们的 x mal map builder 去讨论。也就是说我们刚才是主要解析我们的 my better configure 这个对应的 XL Mapper builder，它是来解析我们的 Mapper 文件的，那么我们可以看到它会获取 Mapper 相关的这个元素以及一些信息，我们可以看到获得 Mapper 信息，那么我们现在这个断点我们也跳过，现在执行到我们的 user Mapper test 下面的这个执行，我们的调研测试字段点。


现在我们可以看一下我们的 user Mapper 这个对象，因为我们知道我们这里面的 user Mapper 它是个接口，那么在这里面我们能执行肯定是已经被实例化，这里面我们可以看到对应 user Mapper 这个实例化，它的实例的类，也就是我们的 Mapper proc case，也就是我们它是一个 Mapper 的一个代理内的实现。


我们接下来是跟进断掉，看一下它是如何执行的。那么在这里面我们看它，首先我们看到它会执行 cats invoke，生成一个 cat invoke 的对象，我们可以看一下这个 cat invoke 对象是如何生成的，这里面我们跟断点进去，在这里我们通过 cat invoke 执行的 math 的进行一些构造，它最终会执行到我们对应的 defend mass 的 input 的构造，一步一步执行。


在这里面我们可以看到它在执行是同 map mess 的进行一个执行，它其实构建了一个 plan 的 mess 的invoke，也就是说我们一个相对来说比较朴树的方法的一个执行器，这个方法执行器里面这里面用到了 map Max 的，我们看一下 map Max 的做了哪些事情。 must 里面它有一个Claude，同时还有一个 math 的 command 对应的是 circle command，而 math 对应我们的 math 的signature，也就是我们的方法的签名。


我们现在执行跟进去看一下做哪些操作，这里面我们通过我 SQL command 去判断一下它的类型。对于 SQL command 我们可以看到这里面的类型执行的 select user by ID，同时我们可以判断它的命令类型是以select，它可以执行到我们对应的 select 的 case 路径。


好，我们跟进来。对于 select 类型的话，我们会考虑它的返回值进行一些特殊的处理，我们因为返回的是一个唯一的对象，这里面暂时它都没有匹配到，那么我们看这里面是进行一个 else 相关的一些处理，这里面的处理侧将会把我们的一些参数进行对象的一个转换。


好，我们现在下一步可以看到我们的 prometer 是一个 long 类型的 54 的一个数字里面并没有做什么变化，这里面我们看它开始现在已经执行到我们的 SQL session select one，因为我们返回一个对象，所以说这会儿我们可以看到它已经跟我们这里面的 SQL session 执行的对应关联到一起。通过 map procase，它经过一轮的执行，最终还是通过我们的 SQL setting 进行一些后续的操作。好，我们可以看到它在执行的过程。这个 command get name 它的内容是什么？看一下我们的command，它的 name 其实也就是对应的 statement ID，这个 statement ID 的它的主城市首先是对应的 name space，我们的 user map 的一个全路径，加上对应的这个方法名，我们的是 select user by ID 的操作。好，那么我们现在跟进去我们后面的一些操作，现在跟进去我们点 sec 的 one 进来。


好，这里面我们可以看到它其实对应的这个 Supersession 也是一个代理，它当前的实现了一次 Supersession template，我们现在不纠结它最终底层也是代理，我们跟着看一下它底层代理的内容，这个 SQL session proxy，它的代理内容也就是我们的 defailed supersession。


其实这里面的实现逻辑还是会最终找到我们的 defailed supersession，这里面我们看到它会获取到一个 SQL session 的一个过程执行，最终我们可以看到得到的这个 SQL session 的对象，它是我们的 defer 的 SQL session，现在我们开始实行 master invoke 编进去，现在到这里面我们已经执行到 debug 搜索session，从这里面我们可以看到我们这执行的过程， SQL session 默认，我们先找到是 debug 的 SQL session，现在我们看进行一个 select 的查询，那么我们跟进去看它里面的操作。嗯，这里面我们注意一下，现在的参数是statement，也就是我们查询对应的 name space，加上我们的查询 ID 以及我们的这些参数。


好，我们跟进去继续，我们再继续，可以看到在这里面它已经有一些特殊的信息了，在执行的过程中，我们通过 configuration 传入参数是我们的statement，获取到了我们的一个 map 的statement，也就是说经过映射的一个statement，现在我们开始进行我们的一个查询，查询的真正执行操作。我们可以看到这里是 IQ ator，也就是说它委托 IQ ator 进行我们一个 query 的操作，这里面的参数也就是我们的 map 的statement，这里面还会对我们的这些参数进行 text 类型的一个包装，同时传入像 Robot 和 handler 相关的一些操作。注意一下这里面的 handler 就是我们的 result handler，最终我们获取的结果通过 handler 来进行一个处理。


好，我们接下来去关注的信息是什么呢？我们看一下这个 map segment 是如何构造的，我们可以跟进来看一下这里面，我们看到它其实就是利用一个缓存的方式进行一个获取的过程。好，我们通过这里面去获取对应的一个 map SIM 的这样一个对象，那么我们接下来看一下这里面 IQ ter，我们先看一下 IQ ter 的它的对象实现是什么啊？可以看到第一种，我们看到的它是一个开启型的 IQ Ator，也就是说这个执行是支持缓存的，如果说它有缓存信息的话，可能他就不会直接再通过 DB 里面去查询，直接把我们的结果返回来。好，我们现在跟进去。好，这里面我们进到query，我们可以看到它在执行的过程，它会获取到我们的 bond SQL，那么同时去构建我们一个 KiteX k，好，我们一步一步进行执行。


那么具体这个 case k 是如何生成？我们可以看一下这里面生成的一些逻辑，它最终还是调嗯， delegate 底层的一些生成逻辑，我们再跟一下这里面就到哪，这是到我们我们可以看到它是在 base accuator 当前这个对象，它其实是 simple accuator 生成 case 的对象，我们看它会把我们先看一下生成的 case 可以跟哪些元素相关。首先是我们的 map statement ID 和我们的 offset limit 和我们的SQL，这些是我们通常查询的关键的一些属性，如果说这些属性没变的话，我们可以理解为这个 SQL 是没有变的，所以说它根据这些参数生成我们的一个 case key。好，那么我们现在跳过我们快速的得到这样一个 case k，OK，那么我们现在得到 case k 以后，我们看下一步我们 query 的过程。这里面既然我们有一个case，那么先我们去校验是否有缓存，如果说缓存不等于no，会进行缓存相关的调试，当然我们这里面第一次执行肯定是没有缓存的。好，这里面我们开始进行 delegate 的一个 query 跟进来，我们可以看到现在我们其实我们还是四代 base ACQ ATOR 执行，其实我们的实现类似 simple acute OK，我们可以看到在这里面执行的过程中，它首先会初始一块 air context 的，如果说有异常的话，我们会把一些异常信息放到 air context 里面，把我们的详细信息返回过来。


首先我们判断一下当前这个 IQA 的是否关闭了，如果是关闭状态的话就会抛异常了。我们看一下，在这里面我们会做一些判断，如果我们的 result handler，它如果等于null，那么它就会通过我们的 local cats 来获取我们的本地的一个缓存信息。好，因为我们最终没有获取到 logo hits，所以说我们现在要需要通过 query from DATABASE，也就是从 DB 里面去查询数据，在这里面它执行的过程，首先会把这个执行的过程放到我们那个 local cats。好，我们在这里面是真正的执行的操作，我们是 do query， do query 的过程中我们可以看到这里面也是用到了我们的configuration。


获取到 configuring 主要做什么事情？主要是构建我们的 statement handler，我们可以看一下最终我们构建 statement handler 是通过我们的 configuration 对象构建的，这里面构建的过程我可以跟进去看一下这里面相关的一些参数。


首先我们是直接通过 routing stream 的 handler 构建出来一个handler，我们看一下这个 routing stream handler 是如何构建的。继续跟进去，在它的构造方法里面，其实是判断了 map statement 它的一个 statement type，根据这个类型去生成对应的我们的 statement handler，可以看到当前是一个 proper 的 statement handler，也就说我们是一个预处理的 statement 的一个处理的过程。好，那么我们得到了这个 purpose handler，我们回到执行的过程，在这里面还做了一些事情，可以看一下，这里面能看到是 intercept chain，也就是我们的拦截器的链。其实在这里这些拦截器的链我们当前的 Steam 的 Handler 放进去，我们就开始进行一些执行。好，我们现在得到了一个Handler， Handler 我们的对象类型是 paper statement Handler，我们知道在 statement 和 purpose statement，在 JDBC 协议里面， purpose statement 可以避免我们常规的一些 circle 注入的问题。我们得到这些信息以后，现在开始进行 purpose 店面的一些处理。


走到这一步的话，如果是熟悉 GDBC 的同学的话，在那里面看到已经相当比较熟悉了。首先我们可以看到获取到一个 connect 对象，这个 connect 对象就是我们 GDB c 协议的connect，当前的 GDB connect 是基于 H2 的 memory 的，得到的一个 connect 链接，看到得到 connect 链接以后，现在推 handle 进行一个预处理，看一下预处理做了哪些事情。这里面预处理它因为当前是一个 delegate 对象，最终还是执行到 delegate 去看，这里面对于我们 statement 进行特殊的处理，这里面我们看主要设置了一下 timeout 和我们 fat size，也就是说我们查询的一个数量。


好，下面对于我们的参数进行一些与处理，我们看看一下是对 parameter 的一些处理，我们的 parameter 跟进去看一下，可以看到对于参数的处理，我们是 parameter handler，好，这里面我们就可以看到其实我们的 statement 在执行之前会把我们的参数进行一些预处理。那么我们可以看到在我们 statement handle 执行的过程中，其实还没有执行完，我们就会涉及到一个 permeter handler，通过 debug 的 permit handler 来检测出的一些对于参数的预处理，可以跟进去看一下它是做了哪些预处理，这里面我们可以看到是 set parameter，这里面也是首先是 air context 去验证一下有没有什么特殊的处。


好，我们看一下，这里面首先对于 parameter mapping 进行一些迭代的处理，可以看一下这里面获取到我们的结果， Premiere get 进行处理，其实这些不是我们过多关心的，我们其实更多的去看一下最终它处理的逻辑是我们通过可以看到这里面是 type handler 进行一个参数的处理。


其实也就是类似于我们在做g、d、b、 c 操作的时候，把我们的参数设置到我们的 statement 上面，这里面是 proper statement 进行处理，可以看到它这里面做了哪些操作。如果是 parameter 等于 null 的话是PS，也就是 set null，还有 purpose name set now，正常情况下我们会 set now 的prometer。再跟进去看一下里面的一些操作，这里面各种类型的一些数据的设置。


好，我们大概了解这样一个过程，我们现在后面内容我们就不再跟进继续看了，我们现在是跳过好，现在执行了我们的参数的一些预处理，得到了我们的 statement 对象，我们 swim 的预处理的操作就完成了，现在开始执行我们的 query 操作。跟进去我们看一下 query 操作好，最终我们开始抄入的内容，其实也就是我们 preparment Stadium 的 ACQ ATOR，其实最终还是我们的买卖是调用 TTBC 的协议执行我们的操作。


执行完成以后，现在我们的数据获取到了，得到一个 recelled set 这样一个数据集，我们需要对它进行一个转换，这个转换的过程就用到了 result set handler 进行我们的数据结果集的转换。现在我们可以看到它已经执行到我们的 result side handler 进行执行，这里面我们看一下跟一下，看一下它执行的一个过程。


我们看到首先通过 statement 得到一个 result 赛的包装器，基于这个包装器获取到我们的 resource 赛的map，最终把我们这些 resource 赛的对应的字段跟我们的 value 的对象映射起来，因为我们这里面是一个优势对象，最终它会映射成功。这里面我们可以看到我们得到的 result side，它应该是一条记录好我们结果获取完成。其实执行完成以后需要把 GDBC 相关的这些对象链接 statement 进行关闭，同时 resource set 也应该进行关闭好我们的 do query 执行完成。


现在把 local case 的一些信息，我们看来这里面铺子的信息把它给清除掉，现在对于 local case，把我们当前查询的内容跟我们的 k 关联起来，也就是放到缓存里面，以备下次使用的时候可以直接读缓存。OK，看到现在的话，我们整个执行过程基本上执行完成，现在我们已经获取到了我们的结果对象，因为我们最终是 select one，那么 step one 的执行的过程中会把我们的历史的对象转换成一个对象。但这里面一定要注意一下，假如说我们查询的结果通过 select one 查询的结果大于一条，那么它就会抛异常，现在我们得到我们的 resort 结果。


好，现在到了我们的单元测试，那么我们进行一个打印的操作，把我们的结果输出来，这样的话我们整个查询的执行过程就给大家介绍完成了，其实这个执行的过程中还涉及到一些其他的钞票，我们如果说通过注解 SQL 执行的操作会不会有什么区别？其实整个流程是大同小异，我们基本上都是通过这样几个关键的对象把我们的数据获取到。


好，我们现在结束单元测试，那么回到PPT，通过这样我跟大家去介绍 SQL 执行的过程。我们知道买 Badcase 的 SQL 执行过程，其实它最终还是通过我们的 SQL session 进行执行的，执行的过程中它通常会用到我们的 detail 的 super session 进行真正的一些业务的操作和执行。在执行的过程会构建出我们的 iPad statement，这个构建其实也是通过缓存里面获取到的这上下文的信息。执行的过程会通过 IQ ator 进行一个执行，将最终会使用 statement handler 来进行一个代理的去操作。 statement handler 处理的过程，这里面会涉及到 routing 的 statement handler 以及我们的 simple statement handler。其实最终在执行的过程中，我们会涉及到 prepare 的 student handler，也就是预处理的 student handler，这里面处理的过程也会涉及到我们参数的处理和结果集的处理。整个我们 SQL 的执行流程大概是这样一个过程。我们这一章节的内容就先介绍到这里，同学们下一章节再见。

