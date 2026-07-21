---
title: 2-7 RocketMQ源码解析-Broker接收消息流程（2538）
---

# 2-7 RocketMQ源码解析-Broker接收消息流程（2538）

接下来我们介绍一下 broker 接收消息的过程，这里我们看我们知道 BROKER 在启动的过程中，它是基于 BROKER Controller 进行启动，启动的过程中最终 start 操作，它会启动 remoting Server 对应的starter，那么这样的话，我们对 g net 的一个服务就启动打开了，那么打开这个服务以后它就会监听我们的请求来源。


那么当我们的 producer 把消息发送过来以后，那么对应的 native Server 它就会接收到这个消息是基于我们的 post message received，它处理的过程中其实它是 native remoting Server，它是继承了 native remoting abstract，那么它在处理的过程中才依赖到了对应的 async process request，那么这里面有同学会介绍，其实我们发送有可能是发送的是同步消息，那么同步消息在这里面是不是也是 Singapore side request？其实是的，它也是基于 a single process request 在执行的过程中再进行 get 阻塞，得到它同步的消息内容。是这样一个逻辑，那么这里面处理的过程，最终它会用到了我们这里面的 send message process。


其实对于 Ninety Server 里面，它所有的这些处理逻辑都是基于我们对应的 process 来实现的。这里面它是在我们注册了对应的 send message process，它会处理在 send master protect 处理的过程中，它最终会调用我们的 master store，把我们的信息存储到对应的 lock 日志上面，这样的话这个 broker 接收的权益就完成了，那么接下来我们来看一下对于 broker 源码里面这段逻辑是怎么去实现的。


首先我们这里面看到的是 broker control，这里面我们回顾一下 start 的操作，那么 start 插入，我们可以看到这是 master start 进行start，这里面还有 remoting Server start，那么这也就是我们接收消息两个最重要的服务。


那么首先对于 real remoting Server 呢？我们可以切到我们的 Netty remoting Server，这里面有一个我们接受消息的操作process，我们可以看到这是 process message received 操作，其实这个操作的过程我们可以看到它是继承父类，我们是 netting remaining server，我们点进去它其实在我们的 native remoting of track 的这个类里面，那么在这里面处理的过程我们可以看到这是也是对我们的 command type 进行 space case 的逻辑的筛选。这里面我们是一个 request command，我们立刻请求，那么我们处理 process request command，看这里面是怎么操作，那么我们把可见区域放大一些，在这里面处理的过程，我们看啊。


首先这里面一个 rename 对象，那我们把它先折叠起来，我们可以看到得到这个 rename 对象了以后它做的事情是什么？最终会把这个 relab 它放到一个 request task，就构造那个 task 任务了，把这个 task 任务去提交出去，那么进行指向，我们可以看到这是我们整个的核心逻辑，所以说我们可以想象其实我们的处理逻辑，也就是在 relabel 这里面的内容去处理的。我们看后面就是整个已测试处理完成那么这样一个过程，如果这是我们 try catch 的内容，也就是我们 submit 的任务，那么就是处理的。


那么我们看一下这个runtime，也就是 Runnable 的这个实现，它里面的匿名类的实现内容是什么？这是我们执行润方法的过程中，这里面会有一个 do before RPC hook，也就是说执行我们的执行之前的一个回调，那么这里面我们看这还有一个 callback 方法，那么我们也把 callback 方法呢？先让它折叠起来，我们得到这样一个 callback 对象以后，我们看这里面处理的操作是什么啊？这里面操作我们看到它是如果说它是对应的是 SYNC ninety process request process，它会执行 process 的 async process request，如果它是同步的话，这里面会执行对应的 process 一个 process request，也就是它的同步操作，那么这里面我们看一下它最终会把 callback 作为一个回调的操作，所以说这个执行的过程中我们可以理解。我们暂时不关心 callback 的操作，那么我可以看一下 callback 出了什么事情， callback 住的事情，它也是就是把我们的 do after l r， p c 后，可以就是说执行完成以后做一个后处理的一个回调。这里面如果说对于CMD，它如果不是 one v 的 RP seed 话，这里面会做一些操作，比如像CTX， the red and plus，这里面对这个 Tando 的上下文进行写入并刷新。


这里面我们先把这个 callback 操作，我们先把它给搜起来，那么我们可以看到冲击里面看到它最终是执行process，它的 sync process request，或者说是我们对于 process request，那么我们先看一下这两个，我们先从 process request 进入看一下这里面进入它是 native request process，我们看一下它的一个实现类，这里面我们知道它是对应的 send message process。


那么我们可以看到对于 process 这块的，我们认为它是同步操作，其实它里面的实现也是调了我们的 async process request 也是一个异步操作，在这里面通过 get 抛词鼓动完成一个同步操作的内容，所以说我们可以直接去看一下它异步操作的内容就可以了。


那么在异步操作的内容我们可以简单看一下它的一个叫，这里面代码量相对少一些，里面也会 Swift case 校验，我们应该是走这里面的逻辑 send message request head，这里面会对我们那个请求头进行一个解析，一般如果说请求头为空的话就直接结束了。那么接下来我们对于 master context 进行一个构建，这一步我们可以看到它是在 period send message hook before，也就是在执行之前做的一些操作。


下面有我们判断这个 handle 它是批量的还是非批量的，我们最简单的请求它当然是属于异步的 send matter，它不是批量的，这里面我们跟进去看它处理的操作，这里面我们可以看到它的内容，这里面是presenter，那么在这里面我们会得到一个response，这边是 remoting command，我们已构造出一个我们这个请求的一个命令。这里面主要是回的 response command，并且对于这个对象进行一些属性的一些填充。我们回过来后面我们看这是 send message response handler，这是我们最终处理消息的一个 handler 对象。我们接下来去看一下处理的操作，这里面它构建出一个 m a seed a，我们可以看到它对于 topic ID 进行一些设置。


最后我们看其实我们关注的内容在后面，在这里面的一段内容，那么这里面最终它会调用我们的 broker Controller 得到对应的 message store，那么通过 message store 进行异步的 put messager，其实在这里面我们执行到 message store 的话，也就完成了我们的数据接收的操作，接收完成以后它就会通过 Max store 来提前 put master 上完成我们这个信息的落盘，里面最终会获取到一个 put master result。后面是对这个 put message short 的那个结果进行一些处理，那么我们看到这里面的话，我们对于这个博客接收消息的内容已基本上完成。


接下来我们来看一下我们的代码实现的部分，此前是我们的原生的 rock MQ plander 如何去实现消息的发送和接收，以及我们集成 rock MQ 基于 spring boot STARTER 方式去如何发送消息和接收消息，以及我们集成四川Claude，阿里巴巴 rocketcode 方式骑手。


那么我们现在切到我们的代码环节，这里面是我们 document study 这里面的几个模块，刚才也给大家有一个简单的介绍，那么我们来先看一下 rock MQ produce 呢？这里面已经跟大家介绍完成，但是我们还并没有执行一下，那么我们现在可以执行一下，看一下它的效果，那么我们现在去执行，我们可以看到很快这些信息发送完成，那么发送完成以后，我们通过控制台去看一下我们消息的这一个情况，从这里面我们能看到我们的集群信息，我们只有一个 broker a。


对于我们的主题信息，我们现在默认是这里面的 sowcase topic，我们也可以看一下它的一些信息，它的状态，看一下它的 topic 配置。这里面写队列，读队列都是四个是我们这是对应的消费者，那我们来看一下他的生产者，生产者就是他对应的自己，我们看一下生产的消息是 showcase topic，那么这里面我们需要传输我们的磁产主，这次我们在这里面有构建，我们是 topic name 对应的 showcase public。


那我们对应的 produce group，也就是男主是 showcase producer，那么基于这两个查询条件我们可以查一下，那么现在我们能查到对应的这个生产的 count ID，它对应的地址，这是我们可以看到它语言是Java，我们的版本是这样一个信息，那么这是我们的生产系，但是有消费信息吗？目前我们没有消费信息，这是我们的消极性，这是这不是我们刚刚执行的，我们看一下消费者，消费者现在处于一个活跃的，是现在数量是没有的，那么这样我们也可以去执行一下我们的消费的请求，我们去把消费的结果去看一下，那么这里面我们去实现了我们的消费操作。


这里面消费操作我们是用到了 debug MQ push consumer，那我们现在去执行一下，看一下消费的内容，我们可以看到在我们启动的过程中，因为对应producer，我们刚才发的消息刚才并没有接收，那我们现在我们启动 consumer 的话，现在我们看到很快我们把这些信息的接收完成。我们来看一下这里面的情况，我们看一下刷新一下。


那么现在我们可以看到一个showcase， consumer 的一个消费订阅主，那么它现在是有一个实例，当前的版本是在 8. 0，它的类型是我们看consumer，它对应的是集群方式的消费，这里面是它的一个 TPS 的一个情况。我们可以从这里面去看一下它的一些消息的一些情况，我们可以选中 let me show case the topic，把我们刚才接收的一些消息，我们可以看到它是接收消息的一些情况。


好，我们可以看到这是我们刚刚发出来的消息的一个时间点，这是我们一些信息内容，那么这样的话，我们基于原生的 rock MQ consumer 的话，我们进行消息的利用，生产和消费在这里面可以完成，同时也可以基于控制台看到这些消息处理的情况。这里面我们先对于 rock MQ，它不管是生产端和消费端，那么它的实现因为原生的 rock MQ client，所以说我们只需要引入 rock campaign planned 就可以了，那么其他的是一些辅助的开发，它跟 rock campaign for 本身没有关系，那么这是我们原生的 rock mail cleander 的使用情况。


那我们再看一下我们基于 string 布的方式，这里面我们先看一下 palm 文件， POM 文件，这里面我们并没有引入原生的 rock m cleaner，我们这里面引入的是 rock m q screen boot starter，我们记得这个 spring boot starter，它是属于 rock m q 团队是发布的。所以说这里面我们对 rock m q 注意一个前缀，通常我们 string 刚才它是 room 的 starter 作为前缀，后面即写上对应的业务，所以这里面我们看到对应 producer 它的操作。


这里面我们引入一个我们自定义的一个 rock m to showcase API，这个我们可以理解为我们消息体的一个载体，我们可以看一下它的内容，这里面我们只留了一个类，就是我们的 demo message，这里面是一个ID，一个 message 内容，其实我们在我们业务线关联的过程中，我们肯定需要定义一下我们消息的结构，也就是我们定一下消息协议。


比如说我们这里面发送这个消息，我们发送的内容它就是我们的 double master，那么 master 就是做我们消息的一个格式的协议，通常我们这个API，我们消息的生产者和消费者都可以把它引入进去，那么引入进去我们这里面构造对象发送，那么对于 consumer 他接收端的话也处理的其实也比较简单，这样的话他反序对话的对象就已经确定了，他知道应该基于哪个地方。


我们可以看到这里面直接是 on message 的方式去获取一个敲击，大家注意这里面我把这个 Meta nation 的方式注释掉了，主要是为了跟这里面去处理的方式去避免冲突。我们同时也可以基于 recommend template 的方式直接reserve，直接去接收消息。


这里面我们还是先从我们的生产消息的方式去开始。这里面我们对于基于是 spin 库的工程，所以说我们这里面是为了我们在启用完成以后就把消息发送出去。我们用到了 Timeline rain Runner， Malay Runner 的过程中，我们看这里面我们是使用到了我们的 Demo producer 去进行我们同步的消息发送。


对于我们认为 Demo production，它处理的过程是 rock time to the template， rock m template，它里面体现了很多跟 rock m 相关的一些模板方法，我们可以点进去简单看一下，这里面提供了很多我们进行消息发送里面，比如我们异步的发送，我们同步发送或者我们顺序发送等等，这些消息它都可以支持，我们可以在这里面去直接去使用。


这里面注意一下，我们发送的过程中我们需要定一下topic，也就是说我们这个主题是在这里面发送的时候同时去指定，那么基于这样的话，我们就可以把一个消息的方式去发送出去，但我们会去想，那么我们发送消息的这里面的 rock 的 MQ template 它是如何构建出来的？我们也可以想到，因为我们是 string 部的工程，那么对于 string 部的工程它都有对应的 auto configuration 自动装配的逻辑，其实 rock IMQ template 它也是基于这种方式装配的，我们可以跟进来看一下它的思想。
这里面我们切到了 rock MQ template，那么我们定位一下这个包的结构，那么这里面是我们对应的 rock MQ spring boot 这样一个大包，那么这里面我们找一下它的 auto compcuration，这里面是 auto computer 的内容，我们可以看到这里面有 rock MQ auto computation，我们打开看一下这里面的内容，这是 rock MQ configuration，它里面是依赖了，我们可以看到是 message convert configuration 以及这里面是 default 是 rock MQ transaction configuration。也就是说对于它是依赖 message 相关的，要更靠前一点。


我们看一下里面的内容，首先这里面是我们创建的是 debug 的 MQ producer，也就是我们的生产对象，它通过 auto coveration 给我们创建完成了，这里面需要我们填入的是像 name Server 和我们的 producer group，这是需要我们指定的具体里面的信息，我们可以理解为它就是一个属性的一个传递，因为它需要依赖 rock MQ property 这样一个对象，它里面都是属性的一个 KV 子。


我们可以看到它里面要求我们全 name Server access channel producer 的信息，这里面的 producer consumer 都是一个对象，它里面去支持里面具体的一些信息的一些内容。那么我们回到这里面的 detail MQ producer，那我们再看一下另一个对象，这是我们的 detail 的 little full consumer，也就是说这里面会跟我们创建一个基于拉取原理的一个 consumer 的一个对象，那么基于这个对象的话，我们可以基于 rock m q template 去进行我们的消息的消费，那么我们可以看到它后面去构造出了我们的 rock MQ 的template，它在构建的过程中依赖的对象是 rock MQ message convert，那么也就是一个信息的一个转换器。


那么其实我们可以看里面的内容，在构建 rock Lamq 的过程中，它设置了 producer 和consumer，也就是说当我们当前的这个容器里面存在指定默认名称的这个 producer 和 consumer 的时候，它就会把它直接我们直接就是 set 进来，也就是注入进来一种方式，同时把我们每次 convert 进行一个设置。


从这里面我们可以了解到其实我们的程序在启动完成以后能布的自动状态逻辑，把 rock MQ 给我们构建出来了，其实我们也可以在这里面直接引入 TQ 的 MQ producer 一次去使用。通过这里面我们看到这个 rock MQ 弹配的一个消息的一个发送。那么我们来看一下 method 我们的 consumer 的实现， consumer 它这里面逻辑是一样的，我们可以看这里面我们是通过 stream 部的 consumer application 作为启动类，我们引入了 rock enter template，这里面的消费我们也是用到了 command line runner 这样方式。当我们成语启动完成以后，我们就在一个 will true 循环里面去拉取我们的信息，我们通过 rock MQ template receive，那么在拉取信息的过程中得到信息，我们就答案输出来。这样一看，因为这个其实是一个主段的方法，如果说我们没有信息的话，它就会主设在这里面，这是一种我们消费信息的方式，那么其实对于 string boot starter，它还给我们提供了另一种方式，也就是基于注解的方式去消费。通常我们消费消息的话，这样的话其实使用起来会感觉更舒服一些。


我们基于这个 rock MQ message listener 的话，我们只要注入一下我们的topic，指定一下我们的 consumer group，那么这样的话我们就可以对消费消息进行消费，那么我们基于 on message 的方法获取到我们的 Demo message 这个对象。


大家注意一下，我们其实在 producer 的时候，我们发送的对象是一个 Demo message，那我们在这里面消费的时候，也可以直接对 Demo message 进行消费，这样的话虽然是一个异步的操作，我们都是在看起来像是在同一个 Demo master 对象进行操作。


当然它并不是同一个对象，它是通过 BROKER 在发送的过程中通过 JSON 进行序列化，存储在我们的 BROKER 上，那么接收过来以后我们搜到的也是 JSON 对象，我们只是基于 JSON 对象进行了一个反序的话， demo message 这样一个 Java 对象，它对于发送端和消费端它肯定不是同一个对象，大家注意这一点。


那么这里面跟大家去介绍了一下我们基于 rock MQ stream boot 的方式进行去如何生产和消费消息，这里面也有必要跟大家来介绍一下，就是说我们在使用 stream 布的胖子发生消息接入消息过程中，我们注意一下它的配置，其实我们可以看到这里面配置的内容。


首先是 rock MQ 这个节点，下面我们需要配置一下 name Server，这个大家也是比较容易理解的，那么作为 consumer 端的话，我们去配置一下 consumer during the group 和topic，那么为什么要配这个内容呢？刚才我们在我们的 auto configuring 对象里面也给大家刚才有所介绍，我们切到这个，我们可以在这里面看一下对应的 auto communication，我们可以看到在这里面我们构造这个 consumer 对象的过程中，这里面是需要我们去传输对应的 consumer group 和 consumer topic，那么跟我们这里面的配置就刚好是一个对应关系。


consumer group 和 consumer topic，那么只有把这两个对象创建完成，那么它才能跟我们生成对应的 consumer 对象，这是我们的 consumer 端的配，那我们看一下 producer 端的配置，那么 producer 端的配置其实也是一样，我们这里面对于 rock MQ 这个节点下面需要配置 name Server，对于 name Server 的地址，不管是 consumer 还是 provider 它都是需要的。


这里面我们同时去制定我们 producer 相关的信息，那么 producer 它设置的内容会比较少一些，它只要指定一下 group 就可以了，我们这里面对应的是 spring put producer 这样做一个group。但其实我们对于 topic 信息，我们所发送的topic，我们得到的这个 rock Anchor template，它在发送消息的时候需要我们用参数指令这个topic，所以说我们也可以在这里面配比一个 topic 作为我们默认的 topic 进行使用。


那么关于 spring put 来去构造我们消息的生产和消费，那么先了解到这里，那接下来我们再看一下我们基于 spring Claude 的方式，那么这里面其实 spring Claude pass 也就是对应的是 spring Claude stream，我们看一下我们的依赖，首先这里面是 rock and q socket API，就不去介绍了，刚才也跟大家介绍过。那我们这里面引入的跟 rock MQ 相关的内容是 spring Claude start stream rock MQ，这是 spring Claude 阿里巴巴的系列里面对 rock MQ 的一个集成，那么我们这里面在发送消息的过程中是以一种什么样的形式？我们来看一下。


那么在这里面我们看这里面的配置文件相对比较重要一些，我们看一下它在配置的过程中是 stream Claude stream，在 stream 节点下面有 rock m q，那么这里面定义了一个bander，那么在 banner 下面我们定义了一个 name Server，这样的话是对应我们那个特别的例子，我们可以看到跟 rock MQ 相关的信息只在这里面有体现，其他地方没有任何跟 rock MU 相关的信息。


那么接下来我们定义的方式bending，这里面有 source 一 hot 0，这里面是destination，我们这个可以理解为 rock MG 的topic，那么这里面我们是 showcase Chrome close topic，对应的 has contact type，这里面有点像我们 h GPT 请求过程中我们传的那个我们的内容的类型是什么？里面默认其实就是 applicating json，同时我们这里面指定义thanks，也就是说我们的对应的 source e，也就是说我们这里面的绑定的这个操作，我们要输出信息，它的操作是基于 source e 这样一个命名的 bin 来去完成的，我们这里面可以给大家看一下，我们这里面有一个是命名为 source e 的b，也就是说怎么去理解这个过程。


其实我们在启动的过程，这里面并没有通过 planned line runner 的方式进行发送消息。我们启动的过程中，其实这里面只是构造出一个 faction configure，这里面给我们提供了一个能返回 supplier 的一个b，那么基于这个它启动的过程，我们可以看对照一下这个 source 一对应我们 function competence 这里面一个b，那么它在命名的处理规则上面我们可以看到这是 source 一，它跟这里面的 listen 的 source 一是一个对应关系，也就是说它是一个函数方法的一个变，那么这里面 out 说明它是一个输出信息，就是我们消息的生产者。 0 就是我们的第一位，它一个缩影位。那么这里面告诉我们，对于我们消息的生产者是基于 SaaS 1 这个病生产出来的，它对应的 topic 是 showcase close 的topic。


那我们看一下消息的消费，那么消息消费呢？这里面也是一个相同的一个对应关系，我们也是 consumer application，里面非常简单，主要我们的消息消费是对应的我们一个 consumer 的一个b，这里面我们sync。一，那么我们看一下我们的 packing 的配置，对于这里面 stream 下面的 rock MQ，这个比较容易理解，我们配置完 name Server 就可以了，那么这里面呢？我们的bendings，这里面 sync 一跟这里面的 sync 是一个对应关系，也就是说这个 in 我们可以理解为是输入，也就是消费消息的一个过程。这里面我们指定了destination，意思是showcase， logo public，你们有必要说一下，就是说我们对于 consumer 端的话，我们的 group 一定要指定一下。


给大家介绍完这些以后，我们分别基于我们的 spring Boots 的方式和 spring Claude 的方式进行我们消息的生产和消费的一个演示。我们在 spring 部的producer，我们可以在这里面。首先我们进行启动，那么这里面启动完成以后，我们去启动我们的consumer，我们去看一下控制台的书，我们可以看对应的消息主题。


这里面我们可以看到的是 showcase boot copy，也就是说我们 spring boot 它生产的消息已经以及它的主题已经在这里面显示出来。那么我们先看一下生产对应，我们选中这里面的 showcase put 的topic，那么对应它的生产者，我们看一下生产者，我们生态者它有对应的 group spring boot producer。好，我们能获取到这样一个实例，对应我们的消息内容，我们也去选中一下我们的 so case topic。


好，我们可以看到这里面是得到了一些生产消息的一些内容，这是我们在使用 spring Boost 的方式生产和消费消息，那么我们可以演示完成，我们可以先停掉，那我们来再看一下 stream Claude 的方式，我们使用 spring Claude 方式来进行我们消息的发送，同时我们基于使用 Claude 的方式进行消息的消费。


我们通过控制台去看一下效果。我们先看一下我们的消息主题，我们刷新一下，我们再次刷新，我们看一下这里面有 SOCUS Claude topic 已经有了，那么我们来看一下对应的生产者和消费者，先看一下消费者，消费者，我们这里面有对应的 spend Claude consume 现在是一个激活的一个状态，那么这里面我们的生产者我们也是选中我们的 topic public 是我们的 showcase cloud public。


好，我们可以看到这个生产者的节点，同时我们看一下对应的消息，我们选中是 showcase close topic，我们可以看到是刚刚发送的这些与 Circus Claude topic 的消息，那么这样的话，我们基于像原生的 rock MQ 的 client 以及有 spin put 以及 spring closer 这三种方式与消息的生产和消费，就先介绍到这里。

