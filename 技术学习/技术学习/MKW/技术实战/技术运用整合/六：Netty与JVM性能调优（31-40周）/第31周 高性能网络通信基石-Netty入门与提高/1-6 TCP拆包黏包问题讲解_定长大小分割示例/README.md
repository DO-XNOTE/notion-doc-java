---
title: 1-6 TCP拆包黏包问题讲解_定长大小分割示例
---

# 1-6 TCP拆包黏包问题讲解_定长大小分割示例

[image](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/b31f6581-6203-4e80-beea-7d1586b256f4/SCR-20240925-bvom.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QYLET3HT%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T230007Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIEwQt8l5kbJdfDxUnDZfYkCQ94Vuhra5rPqJ2epvtSQsAiB%2BB3rsRHl7yglS4lj5tTGsTcZkA77P3N%2FynDfPIh9tiyqIBAjG%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMaquPkhc5CedDMGmgKtwDDOpvW6GoIQ63ct6%2Foh%2F0tAIz32nFMdgcDtI80Aoz6QfcXi6%2F%2FHVdX2E%2FYXvErZ4FkWnT6mMM6T561gZ%2BORcxXTZASoag16OiZDdxnSRaEHTuqVM8Gj5TW8OX2R%2FT%2BcIAX1XHHYaN64PVh%2FukJhxFQktc8XcLW41yMdCwHWaB6A5CsMHRAMPjwGPsBUP7UW4b%2FbTZaoiExlV4RJ%2Bkf%2B%2BOWA8PrVTlwvf7sIXGDgNgMjEGBpmpcvUjzPELFO%2FB%2BfaJkZ8jZds5XXoMKBZGS8F78Qu8SJ47ylY%2BTxOafWT72qKouJCj8w1c94L1ub0SmCX%2F8nmM1xCIf698ioWJ6T2t8NkIZe3TO2vh8%2BnRQKwmG55N6JuEb9Wsill4b9XueqxDxhULbzUMS5brrSmkZqkJxITH8XVbNelPWQ25t7wAwNenopLiIZOcgdcpmODgB4HfUerw0pMMsmPY3Imt3Xq9RaFluX7n8b9UH2juJi0e7%2FxmzvAAXGWVtSejW0HYs%2BRj0GetVT4oOSJFhUzS5yVNac9EkucHn6XKNLq1k6gk0%2BfnP3La81DQB1PApYf%2BQn3avoElf8tgBB8Gfdyr1LAXKCkBu4%2Bp49eJwqkL1xnt4oKXOa9HlAOevmXm6vMwt7%2F%2F0gY6pgGrXUSr55iJTTlGOP1Ri8LFQY%2FwRhXyybjomWs7yhPMqJ%2F43CxoaUaQGlcIR0EpXxCKxuyhXzAdu24ZA%2BOj%2BQ2%2F%2BBBbrIj5nMo58lWSMnW86fOahu0IFLvLzPGNgKY4MzLFhfr%2FfLOugBURPdDdBJ%2FRopZQxaxsvXglPtmG5Xn83Mb%2BEzOEyA1BRbauZZbQ%2BEM1CIWqMRWf17ZtueVj0ezuxkL2tuqc&X-Amz-Signature=383ac51d6558f4d14a8623ba1e3af634043b558faeff14ddd365366a711aa2be&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

[image](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/5e466ced-1dc6-4f5f-931e-fc5e1c3803b9/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QYLET3HT%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T230007Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIEwQt8l5kbJdfDxUnDZfYkCQ94Vuhra5rPqJ2epvtSQsAiB%2BB3rsRHl7yglS4lj5tTGsTcZkA77P3N%2FynDfPIh9tiyqIBAjG%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMaquPkhc5CedDMGmgKtwDDOpvW6GoIQ63ct6%2Foh%2F0tAIz32nFMdgcDtI80Aoz6QfcXi6%2F%2FHVdX2E%2FYXvErZ4FkWnT6mMM6T561gZ%2BORcxXTZASoag16OiZDdxnSRaEHTuqVM8Gj5TW8OX2R%2FT%2BcIAX1XHHYaN64PVh%2FukJhxFQktc8XcLW41yMdCwHWaB6A5CsMHRAMPjwGPsBUP7UW4b%2FbTZaoiExlV4RJ%2Bkf%2B%2BOWA8PrVTlwvf7sIXGDgNgMjEGBpmpcvUjzPELFO%2FB%2BfaJkZ8jZds5XXoMKBZGS8F78Qu8SJ47ylY%2BTxOafWT72qKouJCj8w1c94L1ub0SmCX%2F8nmM1xCIf698ioWJ6T2t8NkIZe3TO2vh8%2BnRQKwmG55N6JuEb9Wsill4b9XueqxDxhULbzUMS5brrSmkZqkJxITH8XVbNelPWQ25t7wAwNenopLiIZOcgdcpmODgB4HfUerw0pMMsmPY3Imt3Xq9RaFluX7n8b9UH2juJi0e7%2FxmzvAAXGWVtSejW0HYs%2BRj0GetVT4oOSJFhUzS5yVNac9EkucHn6XKNLq1k6gk0%2BfnP3La81DQB1PApYf%2BQn3avoElf8tgBB8Gfdyr1LAXKCkBu4%2Bp49eJwqkL1xnt4oKXOa9HlAOevmXm6vMwt7%2F%2F0gY6pgGrXUSr55iJTTlGOP1Ri8LFQY%2FwRhXyybjomWs7yhPMqJ%2F43CxoaUaQGlcIR0EpXxCKxuyhXzAdu24ZA%2BOj%2BQ2%2F%2BBBbrIj5nMo58lWSMnW86fOahu0IFLvLzPGNgKY4MzLFhfr%2FfLOugBURPdDdBJ%2FRopZQxaxsvXglPtmG5Xn83Mb%2BEzOEyA1BRbauZZbQ%2BEM1CIWqMRWf17ZtueVj0ezuxkL2tuqc&X-Amz-Signature=e7a43f95897c1d747d9c90fe4429becc27a2376d12ab79201612dd98b5b0dc16&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

OK 小伙伴们，这节课我们一起来看一看 TCP 拆包年报问题 ninety 是怎么去解决的。上节课我们说了三种方式，第一种是叫做定长，还有一种特殊的分隔符。第三种就是自定义协议栈。我们在这里用 net 的前两种方式跟大家一起来介绍一下。


t c p 拆包年包。首先老师在这里边已经有对应的代码 Com 点 b f x y 点 net 点 package e PK g 1。还有一个叫做 PK G 2。首先我们看第一个整体来讲，我们来打开 client 端简单的阅读一下。首先整个的代码其实很简单的哈，我们 client 端它起了一个 event loop group，这一个线程组其实就是用来对于消息的发送接受处理的有一个叫做 boost trap，接下来绑定group。我们现在用的是 n i o socket channel，对应着绑定一个handler。我们去 init 初始化handler，把对应的我们自己的一些 paperline 里边加一些我们自己的逻辑。当然我们最后一个 add client handler，这就是我们自己实际的逻辑。但是在这之前我们看我们加了两个东西，一个叫做 fixed length frame decoder，这里边它就是一个处理定长的消息体的一个。


怎么说，你可以认为是一个组件或者是一个实现类。这是 Nike 帮我们实现的。 OK 它我这里面写了5，就表示当我的数据包发送就发数据的时候，我只取 5 个字节，认为它是一个数据包。由于我们发的是字符串，所以我也加了一个net，里边给我们提供的叫做 string decoder。好了，最后执行我们的 handler 逻辑。接下来我们看一看。我们在这里边 b 点 connect 连接我们服务端的 IP 与端口号，最后同步的进行阻塞，等待它进行关闭。我在这里很简单，我调两次。我们拿到 channel 之后调两次 right and flash 方法。去用我们 unpull 的 lab 去 vapper 我们自己的一个 bait 字节数组，把它转成我们的缓冲，也就是 byte buffer，把它发出去。同学们，请看我第一次发的是 5 个 a 以及 5 个b。第二次又发了一下。同学们看到我现在发的是多少发的？其实一共是 7 个c，后面加上 1233 个空格。看见了，我们来看一会儿我们把程序运行起来，我们能够得到什么样的效果。


接下来看一看我们的 client handler，里边无非有几个 init 方法。 client handler，它继承我们的 channel inbound handler adapter。 OK channel inbound handler adapter 其实是一个 net 语言使用比较多的 panel 的处理的方式。当然我们其实按 control 加t，你可以看到它的整个层结构其实是比较深的。其实我们用的最多的就是adapter，以及还有一个类是它的子类。我们来找一下这个子类，后面我会讲到叫做心头打头的，我们往下找一找。
刚才我们点到的是 channel inbound handler adapter 对吧？其实它还有一个应该是非常用的一个词类，就在这儿看见了，叫做 simple channel inbound handler，里边多了一个simple，少了一个adapter。其实我们在真正去进行 native 实际的开发的时候，使用的最多的就是这两个类了。哈，这两个类叫做 simple channel inbound handler。还有刚才我们看到的这个叫做 channel inbound handler adapter，它们是一个父子关系，具体他们有什么区别，我们往后面去做实战的时候，老师再跟着小伙伴们详细的去说。


好了，我们回过头来把这两个类关掉，对应着我们有一个叫做 channel read 的方法，去把服务端给我的响应数据取到，它是一个字符串，我直接解析了，去做一个打印我客户端读到的数据是什么样子的。OK，这个代码其实是非常简单的，接下来我们看一看这个 server 端。同理，对应 server 端我们最大，对于 server 端来讲也是两个线程组，一个是 boost group，还有一个是我们的 work group，它其实就是一个 reactor 的这么一个模型了。


接下来我们去加了一些参数，比如我们的 so backlog 以及 send buffer，还有 receive buffer。发送与接收的一个缓冲区，大小重点关注看。我们在这里也是加上了一个叫做 fix 的 length frame。 decoder 也是 5 个长度也是对应的。注意我们真正的数据其实它是一个 beta buffer，通过 string decoder，其实可以把一个 buffer 去给它转成一个字符串。所以我们刚才看到的 client handler 里边直接就可以把一个 object message 转成一个string，这是通过刚才 string decoder 来的。


接下来回到我们 server handler 里面也有对应处理的一个业务代码。接下来绑定同步的去等待我们的连接关闭了，一起释放我们的 boost group，跟我们的就相当于 p group 还有 c group。Ok。好了，我们看一看具体的在我们 server 端里边， server handler 它实际的代码是什么。这个代码很简单，当我们连接激活的时候，我们的 


channel active 的时候，它会打印一句话说 server channel active。在 channel read 方法的时候，把我们客户端的数据，你看我直接能转成一个字符串，其实它就依赖于什么，它就依赖于它自己的 string decoder。
我们再看打印一句话，直接我们把 request 当成 response 做一个赋值，把 response 写回去也是使用了c，t， x 就是我们的 channel handler context 对象。它的 right and flash 方法也是把一个字符串进行，说白了也是把一个字符串转成我们的字节数组，包装成 buffer 对象写出去。 OK 这个逻辑我们搞定了。


之后，我们现在把运行一下来看一下我们想要的结果是不是跟我们所期望的是一样的。我现在肯定是先启动了我们的 server 端，因为我们的 NET 程序一般来讲都是先启server，再去对 client 端进行启动。我们右键我们 run as Java application。把我们的英语程序启动好以后，接下来这里边有一些 warning 哈，暂时不用去关注。我们把它clear。我们现在把 clan 端也启动。注意，我们把 clan 端启动的时候，它肯定会发送两次数据。在这里。你比如老师，因为它是同步的程序，所以我们可以写一个thread。点sleep，我们休眠，比如休眠 2 秒钟。


再发一次，我们来看一看执行结果肯定是我们的客栈端先往搜索端去发消息了。我们 run ads Java application。好，同学们，请看。现在你收到的结果是这样的我们的 server 端好，我们把它放到 server 端，它第一次收到了 5 个a， 5 个b， 5 个c，接下来是 2 个 c 加上 3 个空格，注意 j 也是 5 个长度对吧？因为我是 2 个 c 加 3 个空格，所以我们已经看到效果了。


这种定长的当时的发送消息，比如我们以 5 为一个数据包，假设我现在把我们的 clan 端关闭，把我们的 client 端关闭，我再次重新启动我们的 client 端。但是启动之前我们修改一下参数，比如现在我里边是有 3 个空格，我现在把空格去掉是吧？我们就发 7 个c，看看是一个什么样的效果。我们再次去启动服务。


好了，小伙伴们，你会发现当我把空格去掉的时候，我们只能读出来 5 个c，看见了后面这两个 c 压根就没有给我发送出去，无论是 server 端还是平板端都无法去收到它后面那两颗c。原因是因为你现在当前的数据包还不到 5 个字节，所以他就不会把消息推送过去，或者他解析不了。这就是我们对应的定偿方式的这种解决 TCP 拆包粘包的手段。好了，我们这节课先讲到这，感谢小伙伴们收看。

