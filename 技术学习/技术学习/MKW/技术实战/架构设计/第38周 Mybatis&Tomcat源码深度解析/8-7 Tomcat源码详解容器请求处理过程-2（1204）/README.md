---
title: 8-7 Tomcat源码详解容器请求处理过程-2（1204）
---

# 8-7 Tomcat源码详解容器请求处理过程-2（1204）

好，其实这里面会有一个线程启动，可以看到这里面是我们 start accept THREAD，我们可以跟进来去看一下，这里面我们会创建一个accept，这里面我们注意到其实在这里面我们的 accept 的请求的接收的过程就在这一部分，那么我们可以看到对应的每一个涉及到线程的话，这里面都会指定一个线程名称。所以说我们在这里面 debug 的过程中，可以从线程名称去判断一下当前执行的这个请求的线程，它是处于在哪一个工作的步骤里面。


k，好，那么我们现在跳过断点，跳过完断点以后，我们可以看到整个程序已经启动完成，启动完成以后我们这里面的程序就等待接收请求，现在我们通过浏览器去发出一个请求，在这里面我们可以看到对应的 hello index 这个请求其实它并没有什么特殊。


那我们出发出请求以后，我们看程序已经到了我们的执行断点，我们可以看到现在是在什么位置，是在我们的 NLN 的point，对应的 NLN 的point，我们可以看到这段断点，它执行的过程是什么呢？是我们这个轮询器，也就是说我们基于轮询器执行的过程中，我们看这里面一个我要处理的一个循环，去监听我们请求的变化。
我们现在通过发出请求，你就已经到这里面在人群进行接受，那么我们现在去开始处理的过程，那么现在的话它会首先我们可以看到包装的对象，这里面我们首先对应一个 selection select k，同时我们这有个 SOCKET Wiper，这个 SOCKET Wiper 是 NIO SOCKET Wiper 的一个包装好，我们现在去，嗯，直线跟进去。那么在这里面会处理我们的这个请求的。k，好，我们注意一下，看一下，这里面会去做一些判断，比如说我们的 sow SOCK 的kid，它的一些 readable 和 readable 是否可读可解的一个情况。


在这里面我们得到一个叫 socket process base，其实这个 socket Bay base 的话，我们可以获取到它的真正的实现，它真正的实现其实我们这里面是 a SOCK 的process， a SOCKET process 它构建的过程，我们这里面有 socked wapper 和一个event，这里面的 event 是对应的 SOCKET event，也就是 open read。


那么这个 SOCK 的 process 我们可以看到它其实是 NLN 的 point 里面的一个内部类，那么这个内部类它其实继承了我们的 SOCK 的 process base 的抽象的一个抽象类，那么我们现在重置，我们继续我们执行，这里面创建我们的 SOCKET process 操作，这里面我们可以看到现在去获取我们的accuator，那么现在我们也就是在执行的过程中创建出一个 SOCK 的process，获取到我们的accuator，那么在这里面进行执行。


这里面会有一些判断，你看如果说它没有获取到这个 IQ Ator，它会使用当前线程直接执行，也就是说如果说我没有使用线程池的话，那么强，类似我们也可以接受请求，只是接收请求它会 BL 一个主端的一个状态，我们只能接受一个请求。那么这里面也就是对应的，我们首先去通过 accepter 构建出我们的一个 socket 的process，那么这里面通过 socket process 执行 acuator 进行一个执行的操作，在这里面我们把断点执行过去，那么执行过去，我们看现在已经到了我们新能池执行的过程，这里面构建出我们的command，我们可以看到这个 Relab 的这个 command 内容是就是我们的 soft process，我们跳过好这里面我们可以看到它执行到了对于 socket process base，那么这里面是进行它的 run 方法，也就是说进行运行。


我们看一下这里面是主 run 方法，其实是我们这里面对应的 NLN 的point，下面也就是说这个 SOCK 的process，它执行的操作，这里面首先会得到这个 NLN 的point，这个 Polar 进行一些判断，如果说它不等于null，等于 now 的话，它就直接 close 掉了。


不等于 now 的话，再进行后面的一些操作，这些我们的一些信息我们可以看到这里面在执行的过程中，我们首先判断这个event，通过这个 event 去获取我们不同的一个 handler event，它不等于null，这里面我们看一下获得的 handler 信息是什么，这里面我们可以跟一下，我们去获得到 handler 进行一个 process 的处理，我们跟到这个 Handler 下面我们可以看到这个 Handler 内容。


其实它是一个 connection Handler，这里面的 Handler 对应的那个协议 Handler 它不是一个对象，这里面大家区分一下，那么好我们开始进行我们的 process 处理，这里面就执行到我们的 process 会涉及到协议的一些操作，好，我们继续好，这里面会获取到我们的socket，同时我也会去获取到我们的Processor。


获取到 Processor 进行一些处理，我们可以看到在这里面我们去获取到一些process，这里面现在 process 为null，我们是如何去创建这process？从一个 recycle 可重用的 process 获取一个对象，那么现在我们对象如果说 Processor 文档，最终我们会通过我们支持的协议的对应信息去创建这个Processor。


看一下我们当前 get 嗯， PORTAL 得到的信息是什么呢？我们 power 可以看到它是 HTP 11 NIO PORTAL，也就是说我们是 NIO 的协议，对应 NL 的协议，我们可以这里面对应的 AL 的协议。我们在获取协议的过程，我们再去创建 create Processor，也就是创建我们这个协议的处理器，对于它这个协议的处理器，我们可以看到它其实直接就是通过 new 创建出来的，这里面同时投入一个Adapter，也就是我们可以看到这里面对应一个 defter 操作。这里面我们构建出了对应 HTP 11 的 Processor 信息，那么我们得到了这个处理器，把它向上传递，得到这个处理器以后开始进行对于处理器的一些注册。


好，我们接着进行处理，那么在这里面会进行一个 process 处理的操作，我们跟进去在这里面处理的过程我们可以简单去看一下，这里面我们看到它处理的逻辑都是会涉及到一个度，对应的一个 do will 的一个操作，判断这个状态进行一逻辑的一个循环，那么这里面我们可以看到它是在判断一些状态。


首先我们对于 open read，当前我们的状态是 open read 现在已经命中，现在即通过 service 去处理我们的 SOCKET wrapper，我们跟进来看一下，这里面我们通过 request 获取到我们的 request 信息，进行我们对 process 的一个 service 的处理，其实它最终会调用到 Adapter 进行一个适配的操作。


我们可以看在，我们最终其实执行关心的是在这个部分，在这里面我们可以看到在当前这个 process 里面去获取我们的defter，通过 defter 进行 service 的一处理，这个 defter 实现就是这里面我们指定的考虑dipter。


好，那么我们现在进行 safety 的操作，那么 space 操作，我们知道对于这个depth，它是我们的 connect 连接器和容器之间的一个适配，我们进行点service，可以看到它会做什么处理。好，我们跟进去这里面我们点service，看到在这里面我们可以通过 request 对象和 response 对象获取到我们的 request 和 response 这样一个对象。注意一下这里面的 request 它类名是一样的，但是它的包结构对应的是不一样的，这里面是我们可以看到对应的信息以及 request 它本身，这里面字对应的是 Connector 下面的内容。


好，那么我们继续在这里面我们都是通过如果说我们当前的 request 信息为 null 的话，在里面通过 client 来创建我们的 request 信息。我们继续这里面我们可以看到对于 query string 的 Creator 进行一些处理。


对于这里面我们比较关心的是什么呢？主要是我们的 Connector 相关的一些操作，在这里面我们通过 Connector 进行一个 get service，在 get cleaner 以及在 pipeline 我们可以看到 get fast 进行以 invoke 操作。


通过这里面我们可以看到其实是在我们这个 Adapter 操作里面，也是通过Connector，通过我们的 Connector 这个对象找到我们的service，我们可以看到通过 service 再找到我们的container，通过 service 再找到这个引擎，也就是说我们通过 Connector 和我们的容器，它具有共同的负依赖，也就是 code service。我们通过 Connector 找到它的service，再找到引擎这样一个过程，找到这个 Connector 引擎以后，再通过它的管道操作符，那么管道操作我们知道它是一个序列的，也就是说我们找到第一个结果，进行一个 Emock 操作，这里面我们看到它整个这一行记录经过多次操作进行一些处理的操作。


这里面我们其实最终要关心的是我们的 invoke 方法，所以说在这里面我们可以直接点到 invoke 方法进行执行。同时我们可以看到对于 get service 的 get container 是比较明确的， get pipeline 它和 get fast 它的区别是什么？我们可以切换到我们的 get pipeline 里面看一下得到的信息，那么这里面的 pipeline 它的实现是一个 standard pipeline，对于这个 pipeline 里面的内容，我们可以简单去看一下它的 basic container 的一些信息，包括它的一些状态的信息，那么这样我们得到这个 pipeline 以后，接下来我们再执行是 get fast，对于 pipeline 它会执行 fast 的操作。


首先它会判断一下，如果 fast 不等于 null 的话，去 return fast，当然当前我们的 fast 是不存在的，并没有指定一个fast，那么它就直接把 basic 进行一个返回，也就是我们的basic，也就是 stand engine 的value。


好，那么我们继续，我们得到这个 value 对象以后，我们就进行 emock 操作。好，那么我们 emock 操作这里面我们可以看到它是在 stand 引擎的 value 操作，其实这里面他做的事情它就会涉及到，也是一些依赖链的一个传输，我们可以看到它这里面注的判断是首先去获取这个请求的host，如果说这个 host 等于 null 的话，这里面直接就是设置 response 为air， send air 它的状态码是404，也就是 404 之后当前你指定的 host 不存在。这里面还要对于一些是否支持异步的一些设置。


处理完成以后，这些 host 相关的操作就执行完了，接下来他会把这个管道向下传递，向下传递可以传递到哪里？可以通过invoke，我们可以看一下这个invoke，我们点击进去就看一下它已经到对应的哪个管道服，那么我们看一下这里面我们执行的这是一个 error report value，我们可以看一下对于 host 的城市里面，它里面 problem 它可以支持多种，或者是这里面它对应的是一个 error report Melon，我们可以看到它执行完成以后它会执行next，但我们可以看到它并没有说先执行 air report value。它是执行完这些逻辑以后再去执行跟 air report 相关的信息。也就是说你在执行过程中报错了，我们最终会在 air report volume 进行一个碰撞捕获，这里面会进行异常信息的一些处理，先看它的 get next，再进行value，再进行evoke。


看一下引入口的操作，当前是已经到了我们的 standard host available，也就是说这是我们的 standard host value。当前这个我们可以理解为它是一个 air report 的一个报告的value。那么这里面我们可以扩展一些不同的外漏税热，利用叉叉去进行一个子次。

