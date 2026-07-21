---
title: 2-5 Mybatis重要接口及类的作用分析-执行（2333）
---

# 2-5 Mybatis重要接口及类的作用分析-执行（2333）

我们看对于 my badcase 重要的接口，这里面我们执行相关的最重要的就是我们的 icuator icutor，它是 my better 的一个执行器，是 my better 调度一个核心，附着这个 SQL 语句的生成和查询维护相关的一些事情。


那我们来看一下 my BYTE 源码里面accuator，那么我们可以看到对应的 accuator 呢？它其实是一个接口，接口里面有多个实现，我们可以从这边看一下顶层，这里面是一个 base accurator，可以看到它是一个抽象的，那么对于 base accurator 它有几个实现？这里面有我们的 BAT accurator，我们的 close accurator 以及 reuse a Creator in the simple Eurator，那么它的结构我们可以从这里面去看一下它的一个继承结构，从这里面我们可以看到的是这里面的开情 acutor 和 base acute 它是一个并列关系，其他的这几个 ACQ ATOR 它都继承了我们的 base activator。对于这里面我们其实比较容易理解的一些常用的，像我们的 simple equator，我们的 reuse equator 以及 best equator，也就对应了我们 accurate 的type。对于 captain Acra 它就会提供我们二级缓存的一个 accurate 的一个操作。在 captain acutor 里面它有一个对应的 delegate accurator，其实也是对应 basic 几个子类的一个实现。


好，那么我们可以先打开我们的 simple Creator，大家去了解一下，在这里面我们可以看到 simple Creator 它所支持的参数，我们这里面是需要 configuration 以及我们的transaction，这里面就是一个我们的配置对象，一个是我们的一个事物。我们可以看到这里面我们对于这个 sample kitten 它实现的几个方法，一个 do Flash statement，一个 do query 和一个 do update。其实对我们来说我们关注度最高的也就是一个我们的 query 和update，我们来这里面去看一下，我们先看这个 do update 操作，那么 do update 操作在这里面它注的事情是什么呢？通过我们的 map 的 statement 获取到 configuration 对象，通过 comparison 对象我们可以看到这里面是我们通过 new statement handler 这样一个方法去构造出我们一个 statement handler，那么这里面的 statement handler 在后面，我们马上就要介绍到这里面，我们看是 statement handler，这里面的 statement 还在哪儿？它是封装了 GDB seed statement 操作，同时赋值，对 GDBC statement，我们的 statement 或者 proper statement 进行一些赋值的插入，如设置参数，将 STEM 的结果转化成一个集合 list 等等这些操作。


那么在这里面我们得到的 Stadium handler，它在构造的过程，我们可以看到这里面的 new student handler，我们看 student handler 它也是个接口，那么对于它的这些实现也能从里面看到几个，一个基于一个 base dimenhandler，以及它里面几个对应的一个实现。其实 base handler 它也会对应传入相关的一些参数，这里面我们看一下 new statement handler 出了什么事情。


我们在构建 new statement handler 的过程中，我们首先是通过我们的 routing 和 statement handler， routing Steam handler 也跟大家有介绍过在我们的代码执行的过程，知道它是一个基于路由规则的一个 Steam handler 里面的 routing Steam handler，它会基于里面的路由规则，这里面我们看到它的路由规则就是我们的 statement type，那么基于不同的 statement type 得到对应的一个 statement handler 的实现。我们可以看到这里面有普通的我们的 simple statement handler 以及 prepare 的 Steam handler，以及我们的 corable Steam handler。


好，那么我们现在还回到我们的occur，这里面的关键的实现，我们在得到我们对应的 Steam handler 的过程中，我们可以看到这里面我们通过 paper Cinema Handler 进行一个处理，处理完成以后进行我们 Handler 一个 update 操作。


我们可以看一下这里面对于 paper statement Handler，他做的工作其实也是比较简单的，它是通过获取到我们真正的我们connection，这里面的 statement 和 connection 就是我们 JDBC 对应的API，也就是我们对于 GDBC 操作，首先获取到connection，那么通过 connection 获取到我们的 statement 进行我们的参数与处理完参数以后，就可以执行我们对应的一些结果集的操作。这里面我们是看到这些 statement 相关的讨论，这里面只是跟大家介绍了一下我们的这个 do query 讨论， do update 和 do current 我们可以看到它的结构其实是很相似的，我们就不再一一赘述。那么好，这是我们对应的 simple statement，那么如果说我们还对其他感兴趣的话，我们可以一一点开看一下。


这里面我们像我们是 best Acuiter，那么对于 best acutor 的话，它在去处理一些批量操作的过程中，它的性能相比我们的 simple Acutor 会好一些。同时这里面还有一个 reuse occur，那么对于 reuse accuator，它对我们这个 statement 或者是 prepare statement 进行了一个重用，这样也是为了提升我们一些效率，一些事情。好，这是我们对于 base acute 下面几个指令的一些实现，那么来看一下 base occuter 它里面的内容，作为一个抽象的 basic utter，它底下这几个实线帮我们做了一些具体的事情。
其实对于 base educator，它的包装也做了很多一些结构性的封装，我们可以看到它里面对应的一些属性，这里面有transaction。我们的 4 五 a Creator，我们这里面要看 a Creator 是一个包装器，里面有一个queen，这个 queen 去做一些 defer loader 的一些事情。我们可以看到对于 basic creator 里面一个，我们这里面是 paper 的cats，这里面命名是 local case，这个 local CACTS 就是我们通常所说的一级缓存，那么这个一级缓存它的实现方式其实就是存储在我们对应的一个海信 map 里面，对应的 k value 进行一个处理的操作。我们接下来看这是我们最常用的一个 configuration 对象。下面我们看到一些操作，这是我们构造 basic 的一些，这是个保护类型的一个构造方法，也就是说它底层的会通过实现 super 的构造方法，把对应的参数传入进来。下面我们可以看到对于 tracing 的话，我们获取的功能，它会判断一下当前这个 season 是否关闭，如果关闭的话它会抛出对应的异常，这里面是相应的一个 close 的操作。


好，这里面我们可以简单去了解一下，其实对于我们的 AQAT 操作，主要也是跟我们的GDBC， Connex 相关的一些内容，我们通过获取到 connection 字形对应的 statement 得到我们的 result 这样一个操作的过程。


好，这是我们看到的 base equator，那么另一个跟它处于平行位置的就是我们的 cats OKR，那么这里面的 catching a Creator 它处理的工作我们也有介绍，它其实就处理我们在执行过程中的二级缓存，这里面的二级缓存我们可以看到它的管理方式是基于什么管理的，这里面是有一个TCM，也就是 transaction cats manager，我们通过 TCM 进行一些缓存的一些管理，并且最终把我们的操作通过 delegate 进行一个异常的代理代理执行完成。那么我们构建这个 captain Acute 的时候，首先你需要一个 Acute 的 delegate 代理，同时我们把这个 delegate 进行一个 Acute 的一个 wapper 包装，这里面同时我们其他的这些操作，我们可以看到都是通过我们 delicate 直接进行一个代理的操作。


其实这里面我们应该要重点关注的是什么呢？是我们的 query 操作，那么因为我们 query 操作对于这个 captain acute 它主要的工作是给我们包装了缓存，所以说也就是说只有在查询的过程中，对于我们这个 category 才能起到它的作用。


我们可以看到在这里面我们在进行 query 插入的过程中，首先会基于我们这些上下游的这些参数构造出我们的 case k，作为我们对应这个 case 哈希 map 它对应的一个k，那么我们的结果放到对应的位置，从这里面我们再看一下这个 query 抄入的过程。


从这里面可以看到，首先我们会基于 TCM 这个 cacts 去 get 这个对象， get object 对应的我们的指定的 cats 和我们指定的k。这里面我们可以看到，其实对于不同的查询，也就是说如果说它不是相同的 map statement，也就是说它不同的查语句，它可能会对应不同的cats。通常这个 cats 它区分的维度也就是我们对应的 Mapper 维度，也就是说我们不同的 namespace 空间的Mapper，它有不同的cats。


我们基于这种判断，首先找到这个查询所对应的cats，那么在 case 不为 now 的情况下，我们再去看一下这个 case 是否生效，那么同时我们看一下对应的 case 里面有没有我们指定的这个key，如果说找到了我们对应的这个结果，就把结果直接返回。


如果说没有找到结果，那么我们要做的事情是通过我们 delegate 对我们的 ACQ ATOR 进行一个查询，这里面的查询可能会包括我们的一级的缓存的数据，或者是我们直接 query from DATABASE 这样的插入的方式进行获取我们的数据。获取完数据以后，同时我们把数据再放到对应 TCM 指定的 cats 里面，那么对于这样的话，我们这个 captain a cuter 它的工作就算做完了，所以说我们可以看到对于 a Creator，它分为两类，一个是我们自行 captain a Creator 的这样一个具有缓存的acutor，同时它是因为里面通过 delegate 进行一个代理，最终还是去执行我们 base a cuter 下面的具体的一些实例好。


那么 a cuter 的内容我们就跟大家先介绍到这里，这里面我们可以看到这里面有 statement Handler，那么刚才对于 Stephen Handler 也简单提了一下，那么我们来看一下 Stadium Handler，这里面我们去对应的 statement handler。


我们首先知道 statement handler 它是一个接口，对于这个接口我们可以看它做的这些事情，这里面有 bits get bound circle 和我们的 parameter handler 以及 promise 一个处理的过程， paper query，我们的等等这些 update 这些操作，其实这些操作它之所以叫我们的是 statement handler，其实也就是给我们对应的 GDB seed statement 是一个对应的一个关系，那我们可以从这里面看到这个 statement Handler 的几个实现。


这里面我们可以看到它比较特殊的一个是我们这里面是 routing Steam Handler，从这里面我们来看一下它的一个继承关系，其实跟我们刚才介绍的 a cuter type 是很类似的，这里面对于 Steam Handler 它两个一级的，一个事前类，一个 routing stead Handler，另一个是我们的 base statement Handler。那么 base statement Handler 它也是一个抽象的 statement Handler，对于它底下它有三个子类的实现，这里面有 paper 的 Steam Handler 以及 corable Steam handler，同时还有 simple 的 Steam handler，这里面我们也是重点来看一下 simple Steam Handler。


刚才我们在介绍的过程中跟大家有引入我们对应的 Steam handler，对于 Steam handler 它操作的过程，这里面我们可以看到它实现的几个关键方法，对应这里面我们的一个 BYTE 处理，这里面我们相关的 query 操作，还有 update 操作，我们重点看一下 query 和update，那么这里面对于我们的 query 操作，我们可以看到其实它操作的过程，也就是我们通过这里面的 bond SQL 获取到我们的SQL，通过 statement 直接执行我们的 SQL 套路。


那么执行完成以后，同时把我们这些结果集，我们可以看到这里面有 result side handler，通过 handle result size 的方式把我们 Steam 里面的这些查询的结果获取到，这是我们的 query 操作，这里面用到的 resort side handler，也就是我们下面要跟大家介绍的 result side handler。


我们再看上面，这里面的是一个 update 对应的操作，这里面 update 操作它的执行跟 query 操作整体上是类似的，这里面我们可以看到它首先获取到 bounder circle，那么 banner circle 获取到我们对应的这些 parameter object，也就是我们的参数对象，同时我们可以看到它对于这个从 Meta statement 里面获取到我们的 key Generator，也就是我们的生成 ID 的一种策略。


这里面我们看一大部分代码逻辑，是为了处理我们的这个 k general，我们代码生成的这个 k 的一个逻辑。具体的内容我们可以看到这里面有对应的 statement equator，对应一些执行 SQL 的一些操作。我们可以看到这里面通过 Steven 的 get update count，也就是说获取到我们影响的记录数。同时这里面会有一个 key generate 执行，这里面是 process off 的。


也就是说在我们这个更新语句执行完成以后，进行我们这个主键 k 的一个生成逻辑。那么这是我们的对于 base Steam Handler 里面实现的一些内容，那么跟对应 base SIM Handler 实现对应的我们的 roading Streamhandler，在这里面它的实现就比较简单了，最重要的也就是它的 statement handler 支持一个delegate，也就是一个代理类，那么我们代理类的执行过程，我们可以看到这些方法的实现它都是通过代理类来去实行的。


唯一的一些区别不一样了，就是我们这里面对于 routing Steam handler，它的构造方法是通过我们的 statement type 去选择我们构造指定的一个对应的 statement handler，这就是我们可以简单去理解对于我们的 Steam handler 相关的一些内容。好，那么接下来我们来看一下这里面是。
parameter handler，对于 parameter handler 和 type handler。


都是对于我们一些参数类型转换的一些适配工具，那么我们来先看我们的 permit handler， parameter handler 它是一个接口，这里面提供了两个方法，一个是 get parameter object，另一个是 set parameter。我们看一下它的实现，对于 parameter handler 比较特殊，它这里面只有一个 defailed parameter hunter 的实现。我们先看它里面提供了这些对应的一些属性，这些属性都是通过我们的构造方法传入进来的。这里面我们看一下获取我们的 get parameter object，它的实现比较简单，也就是把我们传入的这个 parameter object 参数进行直接 return 返回。


这里面关键的方法就是 set parameter，也就是把我们的参数设置到我们的 paper 的 statement 里面，其实我们看到这个参数和我们这个操作，其实我们可以想明白整个这个操作的过程，也就是把我们对于 GDB seed 操作就是设置参数的过程，其实可以理解为它的逻辑是一样的，我们可以看到这里面的一些操作。


首先这里面会通过我们的 bond circle，你获取我们的 parameter 对应的一个Mapping，那我们获取到这个Mapping，它要注的事情当然是当 Mapping 不为 now 的情况下，我们对于 Mapping 进行一个遍历，我们通过 Mapping 去获得对应的一些信息，判断一下对应它的一个模式。这里面我们看到整个这个里面所有的处理都是为了得到一个 value 词，也就是说我们需要跟 proper statement 里面 set value，我们先得到对应的这个 value 的信息，那么得到这个 value 信息，它其实获取 value 的时候，各种不同的方式去获取我们的 value 信息。


得到 value 以后，我们看这里面，我们通过 parameter Mapping 去获得了我们的 type handler，也就是说我们设置的过程中需要指定一下我们设置这个属性的一个类型是什么？我们这里面的 Tab handler 对应的一个类型，那么得到这些类型信息以后，我们可以看到它会在这里面最终进行一个 set power 的操作。


set 的过程中我们可以看到它是依赖了我们的 type handler，通过 type handle set permeter 它里面的参数，这里面是我们的 preper statement 和我们当前的一树引位子，以及我们的 value 以及我们指定的 GDB c type。那么后面的插入就涉及到了我们 type handler 对应 typehand 的操作，我们可以看到后面我们会介绍一下这里面 typehandler 它做的事情是什么呢？负责 Java 数据类型和 JDBC 数据类型之间的一些映射和转换。当然这里面我们会有一些自定义的一些 Tab Handler，我们可以看一下。


对于 Tab Handler 它的实现非常多，我们看这里面 array 和我们的base，一个 big example， big integer 和我们的 blue BAT 等等这些。我们可以看到常用的这些 Java 的类型和我们 GDBC 数据库支持的类型，它会有一个这样的一个映射关系，那么最终通过这样的一些映射关系完成我们这个数据的一个设置。


好，那么接下来我们来看一下后面是我们的 map statement，那么 map statement 我们可以理解为它其实就是一个 VO 对象，它把我们常用的这些信息都包装到一个 map statement 的对象里面。我们来吃里面去看一下，这里面的 Max statement，它就是一个实现类，我们看到它这个属性的内容特别多，其实它实现的功能好像并不是很复杂，那么在这里面我们可以看一下它的一些信息，对于一些关键的一些点，这里面首先是 resource configuration，我们对于 statement 需要标明对应的ID，也就是我们的方法的名称以及我们的 facts size 财报的这些通常我们不会去手工主动设置，通过我们默认值就行。那么对于不同的SIM，它会有对应的 SQL source，我们的配置的 SQL 以及我们的 case 信息，当然还有我们的 result map，也就是我们定义了哪些对于我们结果及转化的一些映射的一些类。


后面我们看这里面会有涉及到我们的k， generate 等等一些信息等等，这是一些常见的一些属性信息，后面会有一些 builder 相关的一些操作，这些我们不用过度的去了解这里面的一些细节。那么其实我们就知道，我们通过这个 map statement 把我们在 Mapper 文件里面构造的每一个执行方法进行了一个包装，它把这些信息序列化，我们这个 map 的 statement 里面进行我们在程序里面的流转。


我们刚才我们执行的过程中也了解到我们的 SQL sauce 和我们的 bond circle，那么来看一下我们的 SQL source，其实在这里面刚才我们有注意到这里面涉及到了我们的 SQL source 这个对象，那么 SQL source 这个对象是理解为它就是把我们的 SQL 对象进行了一个包装，那么对于 SQL source 它这个接口只有一个方法， get bond SQL，那么我们来可以看一下它的一些实现，这里面有 Dynamic SQL sauce 和我们的 prided SQL sauce。


raw SQL sauce static SSO shop，我们可以去点开去简单了解一下，这是我们的一个普通的绕 SQL source，在它执行的过程中，其实也就是我们原生的一个 SQL 的执行过程，我们获取到 circle 操作，这里面就是把我们的一个 SQL 信息获取过来。那么这里面对于 get bond circle 的实现也是通过 circle source 的一个 1 乘代理去get，帮助 circle 把我们的信息获取过来。那么我们可以看到对于我们这个 SQL source，它的操作就获取到一个 bond SQL 对象。我们可以看到下面的 bond SQL，它是表示动态生成 SQL 语义以及相关的一些参数信息。这里面我们可以简单去看一下 bond SQL，放到 SQL 我们看到它是一个实现类，这个类里面其实最重要的信息也就是我们的 SQL 语句。同时还有我们对应的 permit Mapping 作为一个参数的一个映射，其实它在处理的过程，这里面涉及到我们的 get circle。 get parameter mapping 对于 get circle 也就是原生的一个 circle 的文本，这里面 parameter meeting 就是把我们对应的这个 parameter 我们的参数映射关系传入进去。


好，就是这样一个大概的一个处理的逻辑。那么最后我们看这里面剩下一个 resort side handler，刚才我们在介绍执行的过程中也涉及到了 result set handler，对于它它是负责把 GDC 返回的 result set 结果集转化成一个对应的 list 类型的一个集合，我们来看一下这个 resource side handler，我们知道对于 resource set handler，它主要注的词性就是把我们执行完的 statement 对象取出我们的 resort chat 这个对象的结果，转换成一个 list 对象。那我们来看一下对于它一个唯一的实现，也就是 defailed result handler，我们可以看到它在构建的过程中其实也采集了很多不同的信息，这里面有 acute configuration map 的 statement 以及rollbount，也就是我们的分页参数等等一些信息。


那我们来重点来看一下它的这个对应的操作，也就是我们如何把我们的数据设置进去，我们可以看到对应的handler， resell the side，我们返回的结果是一个 list 对象，那么在这里面它那个处理的逻辑是相对比较复杂的。我们可以看到，首先它会通过我们的 first resource side 获取到我们一个 resource side 的一个wrapper，也就是一个包装器。那么这里面的实现我们可以看一下过程，就是我们通常的 GDBC 操作，通过 statement guide result set 得到一个 result set 对象，那么通过我们的一个 well 循环的方式，把我们的一个信息包装成一个 resource 的wrapper，这样的话避免我们对于 JDBC 底层的一些 API 的一些过度依赖。


好，那么我们来接着看它的一些处理操作，这里面得到一个 resource at wrapper 以后接着要做的事情，得到我们的 result map，也就是我们得到 result 对象以后，我们如何应承一个对应的加码对象，它是需要依赖我们对应的 resource map 的一个过程。


这里面我们会去校验把我们这个返回集，因为我们在设置 mybytes 对应的 Mapper 的查询 statement 查询条件的时候，会指定一个返回值的一个类型，这个类型可以是一个 Java 的type，也可以指定一个 resort map，那么我们其实在这里面就获取到对应的 result map，会进行一个映射的关系，找到对应的 resort map 进行一个映射插入。我们可以看到这里面我们在通过我们的 resort map 获取到对应的这个 resort set 的count，也就指定的一些类型进行我们一个结果的一个处理。


好，我们可以看到这里面对于 handler row value，也就是说指定每一个结果的数据，通过 resort map 进行一个处理，这里面也通过对应的我们的另一种方式，就是 result handler 进行一些处理的一些操作。好，后面的话其实也就是对于我们结果的一个赋值的一个处理，后面内容我们就不用再去详细的介绍，这里面会最终把我们得到的这个日测的结果进行一些汇总的处理，返回一个对应的一个 list 就得到了我们一个信息。那么好关于执行的这些常用的这些接口，就跟大家介绍到这里，同学们，我们下一章节再见。

