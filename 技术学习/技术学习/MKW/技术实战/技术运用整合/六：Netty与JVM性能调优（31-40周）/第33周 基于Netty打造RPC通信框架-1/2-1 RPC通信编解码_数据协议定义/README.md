---
title: 2-1 RPC通信编解码_数据协议定义
---

# 2-1 RPC通信编解码_数据协议定义

[image](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/bd1e3943-f5d2-4ce6-bd7d-ed1ccf32e372/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SKHMWRHZ%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T230034Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCICTeUrdbcajI1VEOyiJklJACn6Bc3lP%2Be%2BHv80nvqoCBAiEA0h2%2BI7KPPBdo1U2Hp40N%2B2o7XfujFZ2viu31yFhk2HQqiAQIxv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDDwGVzzGDhRJ7RzggyrcA9VUxU5%2BxBhtIq6zwiwKwwqfUUe0CBe3%2FCGKjKP2%2F%2BEcrSD7WYSjBkhJMkPrbp1Uor6s8yxzxx5OQJl71Lq1XrnSzcLQpObg95cM0Ce%2F6QEkQ7A0vkWzLiXg9K7aTnBU0Hz22cIfXgzQUsBLjdmjgg%2FwS9zIEsLEbAbzfc46ibrkfwff5KY3QEak16fvDjcUZxDQCsMEBZ%2F3JGpQ3BNZh50v7dkgNTAN6npNPJHb4%2BFjbODvg48%2BPI7C5HAlW7rRJmMZViG9rz6Deta4lmSrR4N5m%2BlfAQIE3ne8ryikYR5XTxMPpqUYNtKOvrD%2BAKnsy6Sc1IFjHOF19AHtUadi7HQnOXCAv4qE%2BD4u%2BImKOoWG9TGmUT0ig45kmyflp27NhPlvE3Ws8d%2F4yf9pl4UD16fdlRAxBlUBID0E8xL9vrPg60FIOeN1rB46ZdenZzYEN2GL8uVByG8ad%2BjrxWQvyGk%2F%2BYxPWdrHOl60oHudfvP8wrw8g2bqVqBiYsNIqs3rAPjhTtHBz9N%2BYqsJp%2BfAwsaio5vQttmUS1RsAvBS5sUol6NWhFJ%2Fv4DPd2PAaYJW7xbup5EkZ%2B9oZKZfP4gIvKmL9hpKBKdbFnptT86OLerOg9%2BReJfhRrO2FtfvMPC4%2F9IGOqUBWm0GrqoVPsDMwr6zUvZGMTJzyJAB048R5OAuXtoZHGEeBomwgNTTBMqtkFE0Ck6kQiDuZbBc8TU3Z2ZCvj2b8HL1u801O08QsLJTFzNg1CWWGpu6hjdNXERP3wqYXWVIBQ9BGgBd3ND%2FtLw%2F6wtatTcA5iDoOoSRKbgVCU%2BXr%2F5xnRiuVcCHR1oObACC%2BouWw19Qqfm%2FeK3Ia%2FabJzLVnhE7m96Y&X-Amz-Signature=a65bddfe60ddda8aceba55da30cb6d4bf2e3e3215536fd67c273be51bcf8bbcf&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

接下来我们继续往下去讲上节课。其实我们已经针对于我们整个的 RPC client 已经搞定了，它就是一个外壳。当然 RPC client 端它实际的初始化的过程中，其实是我们的连接管理器去做的。我们连接管理器都做了什么事情？在这里我们来回看一下代码，我们来看一下我们具体我来最大化一下哈。


实际上我们建立连接的时候，是通过一个地址去调用它的 connect 方法，也就是连接管理器的。我们点进去连接管理器，我会发现在这里边我们去调用了 update connect server 这个类，在最核心的地方我们去调用了，发起了一个异步的 connect 对吧？点进去异步的connect，它是通过线程池去做的，它提交的时候，首先初始化了我们的 boost trap 类，去绑定我们的 event loop group，接下来去绑定channel，哈，表示是一个客户端的 NIO socket channel。接下来去添加option，以及去对它的 r p c client initalizer 做一个初始化。当然最后的时候去发起真正的连接。其实我们在之前的课程中已经把所有的步骤都已经写完了。后面真正连接的过程，但是我们还没有去对 RPC client in it leather 做一个实际的处理。我们点进去，我们在这里面，在之前老师只是打了两个注释。在初始化我们的 

[image](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/f6312586-2db7-49e0-bb82-7a9076315bb7/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SKHMWRHZ%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T230034Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCICTeUrdbcajI1VEOyiJklJACn6Bc3lP%2Be%2BHv80nvqoCBAiEA0h2%2BI7KPPBdo1U2Hp40N%2B2o7XfujFZ2viu31yFhk2HQqiAQIxv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDDwGVzzGDhRJ7RzggyrcA9VUxU5%2BxBhtIq6zwiwKwwqfUUe0CBe3%2FCGKjKP2%2F%2BEcrSD7WYSjBkhJMkPrbp1Uor6s8yxzxx5OQJl71Lq1XrnSzcLQpObg95cM0Ce%2F6QEkQ7A0vkWzLiXg9K7aTnBU0Hz22cIfXgzQUsBLjdmjgg%2FwS9zIEsLEbAbzfc46ibrkfwff5KY3QEak16fvDjcUZxDQCsMEBZ%2F3JGpQ3BNZh50v7dkgNTAN6npNPJHb4%2BFjbODvg48%2BPI7C5HAlW7rRJmMZViG9rz6Deta4lmSrR4N5m%2BlfAQIE3ne8ryikYR5XTxMPpqUYNtKOvrD%2BAKnsy6Sc1IFjHOF19AHtUadi7HQnOXCAv4qE%2BD4u%2BImKOoWG9TGmUT0ig45kmyflp27NhPlvE3Ws8d%2F4yf9pl4UD16fdlRAxBlUBID0E8xL9vrPg60FIOeN1rB46ZdenZzYEN2GL8uVByG8ad%2BjrxWQvyGk%2F%2BYxPWdrHOl60oHudfvP8wrw8g2bqVqBiYsNIqs3rAPjhTtHBz9N%2BYqsJp%2BfAwsaio5vQttmUS1RsAvBS5sUol6NWhFJ%2Fv4DPd2PAaYJW7xbup5EkZ%2B9oZKZfP4gIvKmL9hpKBKdbFnptT86OLerOg9%2BReJfhRrO2FtfvMPC4%2F9IGOqUBWm0GrqoVPsDMwr6zUvZGMTJzyJAB048R5OAuXtoZHGEeBomwgNTTBMqtkFE0Ck6kQiDuZbBc8TU3Z2ZCvj2b8HL1u801O08QsLJTFzNg1CWWGpu6hjdNXERP3wqYXWVIBQ9BGgBd3ND%2FtLw%2F6wtatTcA5iDoOoSRKbgVCU%2BXr%2F5xnRiuVcCHR1oObACC%2BouWw19Qqfm%2FeK3Ia%2FabJzLVnhE7m96Y&X-Amz-Signature=ed8496ac1996817787a75cd3468df2421519fb6f8ac4ce28ec09ee4793cf33b5&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

channel 的时候，我们要加一些实际的业务处理器，比如做实际编解码的，做实际业务处理的，对吧？我们这节课就来做对应的我们自己 RPC 的编解码，做一个 code c 的处理。对于编解码其实也是最核心中的核心了。我们一点点开始去说明。
首先我们来看一下我们整个的 RPC 框架的一个架构。之前的课程中已经完成了两部分了。 r p c client call 我们已经完成了 r p c connect manager，是不是以及 r p c client，它具体的一个空壳已经搞定了。
接下来的事情我们要做什么？我们要做 code c 编解码，也就是我们整个绿色的这一部分。首先我们来看一看是传统的 RPC 框架都会有什么，都会有 encode 跟 decode 的操作。当然 encode decode 它是做一个编码和解码过程，最核心的就是你的协议到底应该怎么去定义。我们在这里你应该非常清楚你的 RPC request 和 r p c response，像这个其实就是我们具体的协议了哈。


最后我们想去基于我们叫做 p to Shaffer 这个框架，它也是 p to buffer 的一个 Java 的客户端，去做一个封装。这节课就来看一看我们具体的 code c 编解码了哈。首先我们要做这一块东西，我们先了解一下应该怎么去实现。回过头来我们来看另外一幅图。再往下我们来看一个这幅图叫做 r p c a client initializer 初始化的过程。我们要做什么事情？首先我们应该就通过pipeline，就是 init channel 这个方法去拿到 pipeline 对吧？初始化的 pipeline 去自己去定义自己的编解码的。初始化的工作，就相当于往里边去 at last 加自己的 handler 编解码，最终再把自己的业务的handler，就是 RPC client handler 也加进去，这个是毋庸置疑的。


最后我们来看我们自定义的编解码应该做什么事情。比如你的具体的协议是什么？就是你的 r p c request 跟 r p c response。也就是对应着我们架构设计里边的 r p c request 跟 r p c response。你应该定义一下在编解码的时候应该怎么去做处理对不对？也就是你的 r p c encode 跟 decode 应该怎么去做？接下来儿有一个叫做 a less field，叫做 base 的 frame decoder，这是干什么事情的？说白了，我相信学过 Natty 的就是对 native 非常了解的小伙伴应该很清楚，它。

[image](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/a7a77301-4459-4766-b9e7-92c7db3b3062/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SKHMWRHZ%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T230034Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCICTeUrdbcajI1VEOyiJklJACn6Bc3lP%2Be%2BHv80nvqoCBAiEA0h2%2BI7KPPBdo1U2Hp40N%2B2o7XfujFZ2viu31yFhk2HQqiAQIxv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDDwGVzzGDhRJ7RzggyrcA9VUxU5%2BxBhtIq6zwiwKwwqfUUe0CBe3%2FCGKjKP2%2F%2BEcrSD7WYSjBkhJMkPrbp1Uor6s8yxzxx5OQJl71Lq1XrnSzcLQpObg95cM0Ce%2F6QEkQ7A0vkWzLiXg9K7aTnBU0Hz22cIfXgzQUsBLjdmjgg%2FwS9zIEsLEbAbzfc46ibrkfwff5KY3QEak16fvDjcUZxDQCsMEBZ%2F3JGpQ3BNZh50v7dkgNTAN6npNPJHb4%2BFjbODvg48%2BPI7C5HAlW7rRJmMZViG9rz6Deta4lmSrR4N5m%2BlfAQIE3ne8ryikYR5XTxMPpqUYNtKOvrD%2BAKnsy6Sc1IFjHOF19AHtUadi7HQnOXCAv4qE%2BD4u%2BImKOoWG9TGmUT0ig45kmyflp27NhPlvE3Ws8d%2F4yf9pl4UD16fdlRAxBlUBID0E8xL9vrPg60FIOeN1rB46ZdenZzYEN2GL8uVByG8ad%2BjrxWQvyGk%2F%2BYxPWdrHOl60oHudfvP8wrw8g2bqVqBiYsNIqs3rAPjhTtHBz9N%2BYqsJp%2BfAwsaio5vQttmUS1RsAvBS5sUol6NWhFJ%2Fv4DPd2PAaYJW7xbup5EkZ%2B9oZKZfP4gIvKmL9hpKBKdbFnptT86OLerOg9%2BReJfhRrO2FtfvMPC4%2F9IGOqUBWm0GrqoVPsDMwr6zUvZGMTJzyJAB048R5OAuXtoZHGEeBomwgNTTBMqtkFE0Ck6kQiDuZbBc8TU3Z2ZCvj2b8HL1u801O08QsLJTFzNg1CWWGpu6hjdNXERP3wqYXWVIBQ9BGgBd3ND%2FtLw%2F6wtatTcA5iDoOoSRKbgVCU%2BXr%2F5xnRiuVcCHR1oObACC%2BouWw19Qqfm%2FeK3Ia%2FabJzLVnhE7m96Y&X-Amz-Signature=448fac47b4327c20d37cc446043893bf949a907dcc5dd46dae0c446eb772a4dc&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

其实做一个你实际数据包解析的，后面我们会去讲。最后我们在编解码过程中我们去使用了什么？使用了我们的普通 shuffer 这种编解码器去做的。 OK 这个就是我们整个我们的 r p c client initalizer 的一个全流程。我们来按照这个步骤一点一点的去进行编码。首先初始化蝙蝠烂，然后去做编解码器的一个初始化工作，最后去加上我们的业务 handler 就可以了。 OK 我们来打开我们具体的代码，对应着我们现在第一步应该去做的事情就是把 paper line 拿到。我们通过 c h 就是我们的 socket channel 去拿到我们对应的pipeline。拿到 pipeline 之后，它的定义就是我们的channel， pipeline 我们叫CP，等于它。接下来我们去对 CP 去添加一系列的操作，比如这里边我们 CP 点 add last。我们要自己要定义我们的编码器，要定义我们的解码器，还要定义我们的实际的业务处理器，就是我们的 RPC client handler。可能要加一些其他的东西。在这里我打开注释。好，我们来看一看。我们现在就来把我们的协议定一下，我们的协议怎么去定义。在这里可以看我们的协议肯定是我们自己所定义的RPC， request 和 response 对象，我们到底应该怎么去传 request 对象跟 response 对象？其实说白了，从 r p c 的角度来讲，比如大家比较熟悉double，我们应该怎么去定义它？在这里我们一起来看一下我们的协议。


首先我们肯定会有两个类，一个叫做 RPC request，还有一个 RPC response。当然在这里面我们去创建一个新的包，我们在这里就不再是 client 了，而是我们的 code c 对不对？ code c 这个包把 request 放下去哈。
还有一个对应的我们的 response r p c response。好了，无论是 r p c request 还是response，你首先第一点，你要做远程的序列化，你就应该实现 Java 的 Siri last more 接口，对吧？你自己都应该有一个定义，一个 default ID，不用我说，大家都知道。好，这里边比如有一些属性，我都用 long book 的 data 去听一下哈。无论是我的 request 还是response，都应该有这么。最开始的一件事情要做 serializable gecko。我们把 ID 拿出来，我们要定义一个data。搞定了这件事情之后，我们来看一看。


大家来一起想一想我们的请求方都需要哪些参数。比如请求方，我需要知道我的请求 ID 是什么。每一次请求，我希望有一个自己的ID，我们可以定义一下，叫做 request ID。 request ID 是干什么事情？同学们想一想我当前这次请求，我要知道我这次请求有个独立的 ID 有什么用。当我们去做同步的时候，可能没有什么太大用处，但是在我们去做异步的 RPC 要用的时候，我们在本地把这次请求应该做一次存储，比如存到我们的一个 map 中，它肯定是一个 future 模式。
我要 request ID 有什么用？我把 request ID 带到我们的响应方，就是我们的实际的服务的实际处理方哈，乌克兰端肯定是调用方。在处理方的时候，我们带上 request 请求，处理完了之后，他给我回送响应的时候，我们应该通过 request ID 去找到我们实际的处理的缓存，这个时候 request ID 就有意义了。如果小伙伴们没明白，我简单来说，我在发请求的时候，我带上 request ID 给我们的享用方就是我们的response。说白了，我们的调用方 server 端实际处理的时候，处理完了之后，他应该也把 request ID 也应该再 set 回去，再回来。回来的时候我们通过 request ID 去拿到对应的 future 对象，就能找到我们 call back 对应的一个实际的处理了。所以在异步的时候是非常有意义的。


如果小伙伴们你了解过double，或者了解过其他的 RPC 框架，像 Sofa boot 或者是你的 Rockmq 底层的 removing 框架，它里边对于异步的操作都是采用了这种 ID 回调的方式。如果小伙伴们还不明白，我们在这里给小伙伴们画一个图，让小伙伴们彻底去了解异步调用应该怎么去使用。


其实我们整个的 RPC 框架比较核心的点，稍微有一点复杂的异步调用。因为异步调用涉及到什么？涉及到我们的 future 的模型。好，现在我画的东西是表示我们的 request 请求，这一边就是我们的 response 哈。说白了，我们的 net 的 client 端就是我 RPC 的 client 端跟我们 RPC 的 solo 端，我把它最大化一下，里边我都是让他去上下哈。 client 端 soul 端。一般来讲是我们的 client 端是不是主动的去发起一次请求。假设我用原型表示哈，我发起一次 request 请求，这个 request 请求我带上一个东西，叫做 request ID 好，我把它最大化一下。


这个就是一个 request 请求哈。这里面有一个 request ID，他去真正的去发起一次调用。假设他真正的去发起一次调用， request 请求发过去了，我们对应我们的 server 端是不是应该处理 request 请求？这是实际的 executor 执行器，它可能是利用线程池去异步去执行的对吧。当我 client 端去把数据发过去之后，就异步的去执行，执行完了之后，如果是同步就无所谓了。但是如果是异步，小伙伴想一想，因为我把请求发出去之后，这是我自己组织的数据包，数据包发过去以后，当前我线程其实就已经结束了。


线程结束了之后，异步的去执行，执行完了之后，他去给我返回一个结果。当然这里边叫做什么，叫做请求数据包， OK 叫做 request 数据包，叫做 response 数据包。这样小伙伴应该能看懂哈，这个就是实际的响应的数据包哈。当我响应回来的时候，我怎么去能够找到对应的？接下来响应应该是由谁去处理，这个就是一个问题。所以这个问题很简单。我请求的时候，我自己生成一个 request ID，我把对应的它是一个 future 模型，就是一个future，你可以认为个就是一个回调的这么一个模型。我需要把 request i d 所对应的回调的实际处理函数给它封装到一个table，这个 table 可能是一个 map 或者是一个集合容器中，把我后面要执行的东西 put 到一个容器中，这个 key 就是 request ID。我在发之前，我先把执行的后半部分响应的逻辑给它放到 table 中，肯定是 request ID 为 key 的一个集合哈。好了，就是这么一个过程， table 我们把它换一个颜色哈。


我在执行的时候，我带过去 request ID 了。是不是 request ID 在我们执行 server 端真正处理的时候，处理完了之后，在 response 的时候，你也应该干什么？也应该把这次 request ID 也塞到数据包里给我响应。回我们的 client 端。在我们克兰端真正去接收响应的时候，克兰端要做的事情就非常简单了。这是接生响应的另外的一个线程，可能又是一个异步的线程池，接收响应的时候，直接找到 request ID，所对应的 table 就是这个 request ID，它是key。 value 是什么？我们的实际接收响应的处理函数。为什么为value？其实这是一个经典的 future 模型。哈，这个东西是什么？这个是响应结果处理器好请求过来的时候，它是带上 request ID 的响应结果。我们通过 key 拿到实际的value，这个 value 拿过来之后直接执行就好了。这就是异步的 future 模型。


异步的 future 模型最主要的点是在于什么？是在于发请求跟我回送的响应，它们是异步的，起码是两个线程，不是同步阻塞的。同步阻塞是什么意思？我请求过来了，执行，执行完了结果之后，回过来的时候，你的程序才能继续往下走。异步的过程。我把这个请求包丢给你，我就不管了，你给我响应的时候，我响应结果了，我才去处理这么一个过程。其实很多开源框架都是采用这种机制，包括 double 里边，它也是采用 future 模式，包括Rockmq，包括沙发部存，包括一些其他的开源的框架都是采用这种思路去做的。


所以对于我们自己的协议的定义， RPC 协议，你最关键的就是 request ID，做异步的时候是必须要的，这是一个非常关键的概念。好了，我们了解了它之后，我们继续往下去定义。有了 request ID 以后，首先我们做RPC，我们知道我们最开始简单的已经知道 RPC 是不是我们用 Java 的方法去调。所以你最关键的 class 内部必须得有。还有什么？你调的方法是什么？ method name 也必须要有你的method。紧接着还有一些比较关键的属性，比如你具体的类型是什么？你的参数类型到底有哪些类型？这是不是你得给我你的 parameter types，你其实是一个数组parameter。还有你具体调用的时候，因为我现在是一个 client 端。 client 端说白了是什么？ client 端你可以理解为服务的消费方，就是consumer。如果你对 double 熟悉的服务的生产端就是。说白了就是提供方。 server 就是服务的什么的 provider 对吧？就是服务的provider。


我的 consumer 是不是我得去远程的去调我的 provider 所提供的一些接口？我肯定得知道接口的类包括接口的方法名称，类名包括它的参数的类型，以及我到底调它的时候传什么样的参数，我的参数值是什么，对吧？所以这些都是毋庸置疑的参数类型。


具体的，实际的调用的时候传递的参数是什么？你的 object 内容，你的 parents 的参数是什么？这些都必须要有 OK 这样我们整个的协议才能算定义 OK 好了，现在我已经把请求的协议定义好了，接下来我们再想一想我们想象的协议应该是什么？响应的协议。


这根也非常简单，我们来想一下响应的协议无非首先第一点，最关键的是什么？你肯定要有 request ID 是不是？其实你也可以把它当成什么 response ID 也可以。当然 request ID 就是我们客户端发请求师给我带过来，回送响声的时候也得带上它，因为我要去执行后面的逻辑。


还有一个最终执行的结果是一个什么东西？我可以用一个 object 去表示一下对不对。它给我返回的到底是一个字符串还是一个数组，还是一个什么？其他的东西我不确定，所以我叫一个object。 OK 这是对应的响应结果。当出现异常的时候，如果你了解double，你就知道了解double。 double 里边如果出现异常，给你返回。给你一个什么？给你一个比较大的 slope 对象，我们也带过来。 slope 我们也带过来好了。


当然 double 里边可能还有一些像影视传参的东西，比如像 attachment 对吧？它是通过什么的？通过这种 RPC context context 里边去传递的一些这种attachment，一些隐私的参数，我们在这就不去说再加上一些隐私全参的东西了。


OK，好了，我们暂且去定义我们的响应信息。这么几种，一个结果，还有对应的 request ID。如果抛异常的时候肯定不是结果了，肯定返回的是一个异常信息。 throttle OK，这就是我们的响应。 r p c response 这是我们的响应的协议，已经定义好了，这是请求的协议。 r p c request 好了，我们这节课主要就是把我们的协议来定义。好，感谢小伙伴们收看这节课。

