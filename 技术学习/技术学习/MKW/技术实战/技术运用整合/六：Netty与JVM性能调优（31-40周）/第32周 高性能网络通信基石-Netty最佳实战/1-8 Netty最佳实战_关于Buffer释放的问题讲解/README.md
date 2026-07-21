---
title: 1-8 Netty最佳实战_关于Buffer释放的问题讲解
---

# 1-8 Netty最佳实战_关于Buffer释放的问题讲解

[image](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/7c408a3d-6a68-4636-9050-05580418ebbc/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VAVJYRSH%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T230020Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIDOMcUDtYfav6PEnu3e%2FJjOu9kREm0Ywaugwgu5vXWMHAiEAsTXSPebZDWXw%2Bav6HogXfd%2B1bByuYQBbbmIK9U2bu9IqiAQIxv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDNhQyCxnrZjIIk6DmCrcAxytdGe%2FZS7ECqUlRj%2B%2Fsax8yU3oBEBNDI8kZcfif5YTjnGQIAEsDcRva1%2FcBgb1u4kXTjNa98gy5Oyr2RhRMfAriH2qI1TJe4uGJWrIyTrFDOWOxp36Hv78Ywf4GSccBCvvT%2FmglOKcQI2rvSmOybAae7v5xh6hYMj5LBVih18OCAAl7GS%2BC46NmoAs8UfsTTCCa8G%2FqrNmMI6tnNvfgPollxE%2FRjQQAEV5uLFqm9vUWpoqMMl7H79KCnz2Ak4ShI1%2FSB5RNcV2DtR8dHKOwRP%2BwGhviFWk%2FSv%2BJ1O2j63TqtuJvcf2LKnXlv3%2FFRE%2FEMWepsV8lMepzbvOgfKPyzM%2FLvS%2FNFTpvw6Setw0UXmoicBn2HuS2qTelS8FG2JkSnTezf7KoEXZ6577SpD38CJLmXbM7HCxKnsbkusK%2Ft00YbCIRu8EcE%2BVxofZ8DrVFOFlIIViPCM%2B3Y0%2BJGa1WGMmqsVlvqFoZQGKJXqCicacVTcHjW1DuDSGpxjgF1idbEX1g%2FJrEMZM7oFquFZEE90DrrGLezv9C33ijjlKYaqENIJQRUSoymY0S%2BdEKZZ7BMCz2Hooz4JyTNJfumCsPYdlAdPbTVTGB2LCi5XOskfidUfGT11XjWNQ8IaKMLW3%2F9IGOqUBowRwzn5hxp3HTZIj5ZU0mpXRpsvYjx0CnW1UkL75oA7KqxAQz3KwMsWSnhzueRdimAVic05REh2dBYuaCfiwyrlz%2BXzJtB0O4wciWJyL2BVDmdFUpPWUP8eHdkYBSEVIOljHO1Igr3k9c5ojYhd6oI9o5AbgL90QJun8EmA3SqxC3Y0JF6hUxA9Us2WSSLLjRZzofdfBvOrJBR8babFycA2PcEz2&X-Amz-Signature=bce862797821813902569d84cc702335e1895ba1225d47f451773253d5c233bd&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

OK 小伙伴们大家好，这节课我们继续往下去讲。上节课其实我们已经把整个的服务器端到客户端的，我们的 client handler 怎么去接收已经讲完了，但是具体的这两个方法还没有去做判断实现。我们先把问题解决，到时候我们再一起详细的去分析资源释放的问题。


好了，我们看到了对应的我们的在 common 包下，它现在是处理响应的结果。在这里边直接给我拿过来的 result type 跟data，我其实可以去直接根据 result type 去做一个判断。我说简单写 result type，如果点equals，当然你肯定是要 result type，它如果是success。


第二equals，我们的 result type。我在这里可以简单的去打印一句话，老师成功是不是叫做处理 user 模块的 save 方法成功就可以了，对不对？ else 的情况下失败了，除了 success 肯定就是失败或者其他情况。我在这里写处理思路方法失败。其实这些逻辑，比如处理成功了，你肯定有对应的数据库要做一次 update 更新，处理失败，我们要也要做一个标记，让他去定时的去补偿。下面也是在 update 的方法处理成功和处理失败。


好了，我们逻辑其实就已经写完了，我们再回过头来详细的去分析一下关于 buffer 它的资源回收和释放的问题。首先我们考虑一个简单的问题，哪个简单的问题？就是我们现在无论是 client 端还是 soul 端，我们直接把关注点聚焦于 client handler 跟我们的什么跟我们的 server handler。


首先我们来看一看我们现在所使用的类都是使用叫做 channel inbound handler adapter。其实小伙伴们，可能如果你之前认真的去学习老师的图文的教程 h t t p 的client，你会发现老师在之前 h t t client 里边我并没有用刚才那个handler，我用的是什么？我用的是这个类叫做 simple channel inbound handler，对不对？ simple channel in bound handler 跟我们现在所使用的 channel amount handler 到底有什么区别？我们点进去来看一看。


首先按照 Ctrl t 看一看他们的父子关系。好，我直接搜到 simple channel inbound handler，你会发现 simple channel inbound handler 它肯定是一个比较下级的类。它的父类看见了它的父类叫做 channel inbound handler adapter 也。它们两个是一个父子关系也它是一个父类。我点进去它是一个父类对不对？它弄上层的类我就不说了哈。它的子类 n control t 我看到它的子类会有一个 simple channel。你帮我看到了，它的子类是一个 simple channel involved handler。


我们再点去 simple channel involved handle 我们来分析一下这两个handler。其实我们在我们正常写 Nike handler 处理器的时候都可以去继承，只不过一个要实现 channel read 的方法 simple channel amount handler。它要实现的也是一个 channel read 的方法。 OK 这个是 simple China 里面的handler，我们的它要实现一个 channel rate 的方法也是一样的，哈，如果没有，你看这个是没有，它都是可能是调用负累的对不对？我们看一看。我们现在用的是 channel inbound handler adapter。我们重写那个方法，肯定是 channel read 的方法。 channel read 的方法都帮我们做什么事情？它是一个，我们看一下，叫做 file channel rate c，t，x。再往下去找它具体下面的实现。这个就是得找到这里边了。这个就很复杂了，我就不领着小伙伴们一一去读了，哈。我们直接找到他所继承的那个类就好了。


叫做 channel inbound handler adapter。我们去找到 channel inbound handler adapter。好，它里边也会有一个，什么也会有一个，当然它就是更上层的了。回过头来还是回到这里，我们回头来看一下，来分析一下代码。


首先 channel inbound handler adapter，它是我们 simple channel inbound handler 的一个父类。我们来找到 READ 0 方法，你会发现 read 方法，它里边的层次结构是很深的。它调用 c t x 点 file channel read，把 message 资源对不对做了一些处理。我们点进去，你发现它就叫做 channel handler context。它是放到上下文里面的。我们去按住 Ctrl 加t，继续去，往下去找。底层实现就两个，一个叫做 Detag channel handler context，还有一个类，其肯定不能是这个类。我们再往上去找，就是这个叫做 abstract channel handler context，它去调用了什么叫做 inwork channel read。去往下走，在这里边你会看到。再往下去走，它真正的去找到了。


获取一个链表，因为我们知道 net 的它的 pipeline 事情传播机制是一个，你可以认为它是一个类似于数组。取到下一个executor，就是 event executor。说白了就是 event loop。去做一个异步的执行它。这都是做一个异步的执行。无论是他走到这里边 in event loop，还是不是 in event loop。如果不是 in event loop，它就会帮你再创建一个新的 Nike 的线程。 ninety 肯定是 fast thread local thread 的线程。继续调next，点 inwork channel reader。总之它调这个方法我们再往下看，就在下面再往下去点具体再去调 channel 了。你会看到它这里边无非就是一个链条的往下去传播具体的数据的对象。它其实就是 buffer light 里的buffer，它没有去对它进行回收，这是一个最根本的区别，也就是我们使用什么使用 channel inbound handler adapter，它最终是不会把 buffer 帮你去回收的。而它的子类 simple channel 也帮handler。我们来看一看它的 read 方法。


你看它的 channel read 方法，它是有区别的。它这里边做完了操作之后，最后是有一个叫做 release 操作。假设可以满足条件能release，它会帮你去把资源释放，比如他会帮你去把资源释放。


我们知道 Nike 里的 buffer 最简单的，从最直观的上来看，我们不从 buffer 的结构上来看。从 buffer 的类型上看， buffer 的类型最简单的就两种buffer，一种是堆外，就 direct buffer，还有一种堆内。我们 heap buffer 对不对？这是最直观的。它们有什么区别？就是黑客 buffer 是在我们 g v m 内部的，是堆内的，它其实是由 g c 管理的对吧？ g c 去可以帮我们去回收，但是我们的 direct 打法是对外内存，我们 Java GC 是没法去帮助回收对外内存的这个东西的。所以需要我们自己编码的时候，自己去做引用的释放 release 它这种就是一个引用计数法，你可以点进去它 release 方法就是做一个引入计数，比如用的了它可能就加1，释放的时候再减1，就把这一块内存。具体里面代码，有兴趣可以去看一看。可以去点一下 release 是不是release，它也是一个接口，再往下看。


你点release，你得点到很底层的一个 release 方法了。我有点慢，你得点到哪一个？它有一个非常底层的 release 方法，你往下找一找，再往下找，是一个非常底层的 release 方法，叫做 unrelease 的 bit buffer。 OK 我点一下看一下哈。sorry，不是它。反正底层它其实很多，它会帮你去以引用技术的方式做一个释放。我看一下它到底是哪个，这个层次会很深哈。我们点进去哈。我印象没错，它应该是一个叫什么什么 reference OK 在这里 reference OK 这里边有一个release，我们再点进去。它这里边有一个类，我们来看一下。这个类叫做 reference county 的 open s engine。这个类我们去点updater，点进去到这个类里边 reference count updater 类。你看它这个类真正的去做这种引用技术。


1、它其实底层就是一个 CS 操作，我们可以随便点一个，比如我们的 try final release， 0 Retry release，哪个方法都可以点进去看。最终其实就是一个我们的 compare and set 这么一个操作，它就是一个引用的释放。好了，不去关注这个事情，我们把这个点了好多哈，把没有意义的都关掉。


这是关于引流释放的事情，我们考虑一下这段代码还是回到我们的 simple channel in bond handler 对不对？它执行完了之后会帮你去释放，我们看看它怎么去做的。它在这里面最核心的类它是在 channel 瑞克的时候，它掉了一下，叫做 channel read 0。比如 channel read 0 其实是我们真正去使用的子类。 channel read 0 是我给你提供的真正让你们去可以去实现的类你。比如在最开始我们还是回到之前我们讲 HTTP 的net，基于 HTTP 的实现的时候，我们看随便点一个叫做 HTTP client test，我们点到具体的handler，你会发现哈，我们最大化。


你会发现实现了 simple channel inbound handler 的时候，你要重写的方法叫做 channel read 0，是不是 channel 日的 0 在我们这里边，他怎么去做的？他判断如果可以去执行，直接怎么去做？他做的手段，他是直接去调 channel read 0 了，把 context 跟 message 就是我们的对应的数据buffer，它直接就相当于调了这一段逻辑了。我们自己之前学 HTTP 的时候这段逻辑。好了，我现在问你个问题，如果它是异步化的，交给另外的一个线程去处理的，能理解？我说意思，当你调 channel read 的时候，假设说他执行这里面，如果是异步执行的话，这一段代码执行完了之后，紧接着就会走 finally 去把引用释放。


假设说你这个 channel read 0 里边你是异步执行的，你有什么意思？就好像我们之前对应着 client handler 或者是 server handler 一样，只不过这个不是 simple China amount handler。我们在这里面做的操作就是把当前的 message 交给了一个异步的线程，是不是我说 worker submit，然后异步的去提交去处理？我现在问你，如果你现在继承的是 simple channel inbound handler，而不是 channel inbound handler adapter，你是不是这里边执行完了这段代码之后，它就会可能当然根据实际的场景，但是总会直接执行完它之后，如果满足条件直接就会把我们的 message 去进行一个私人释放。


我问你，你在异步执行的时候，有可能你你的任务还没走完，结果你的 buffer 已经被内存被清空，被释放了，对不对？就会出现一个问题，所以我们再去使用什么？如果你在你的业务 handler 里边，你不是异步化处理，你就可以简单的使用 simple channel amount handler，它可以帮你最终去做一个 release 释放的功能。这是比较简单的一种事情。如果你是异步化，不好意思，你只能去选择它了。


channel inbound handler adapter，或者还有一种方式。这一种方式也是我们之前在讲 HTTP 的时候跟小伙伴们提了一嘴。我们最大化就是本身来讲异步。我不想阻的 worker 线程，对吧？你也可以给 handler 再加一个异步的线程池，这里面叫做 default event executor group，对不对？我可以以线程池去执行，我又再加了一个线程池去做处理，也可以这种方式去做，这也是可以。


或者你自己在 handler 里边异步处理，但是 handler 里面你异步处理的时候，你要注意，如果你想去提交异步的事情，你想把 request 这个东西想丢过去，这是不行的。或者是你 copy 一份也可以，或者是你把 request 其中的属性拿到也行。但是你不能把引用直接放进去，放进去有可能导致我们在使用 single channel amount handler 的时候，它直接把引用释放掉。所以在这里同学们你要注意的一点就是我们在使用写 handler 的时候，你要注意，对于 channel 引棒的 handler adapter 以及 simple channel 引棒的handler，他们的一些细节就是我们的 buffer 什么时机释放的问题，要不然你可能会出现异常，出现那种 reference count 引用为0，但是没找到的问题会出现那种异常的。


好了，接下来我们再来讨论一下。现在我们的做法是一个 client handler，还有一个 server handler。同学们请看我的 server handler 里边，其实它执行的是 message task for request 代码，里边并没有去对我们引用的 message 进行释放对不对？而我们的 client 代码里面，在这里面它是做了 10 发了，是不是做了一个 release 释放？这是一个什么问题？其实很简单， Nike 它其实做了优化，当你的服务器端往出写内容的时候，他会直接会手工的去帮你去把对应的message，他会帮你去做一个释放的操作，这是他比较优秀的地方。但是我如果想用的时候响应给 clan 端，它也没有再去调 c t x， d r， right and flash。所以你就需要自己去释放。我们来看一看它怎么去做到帮你去释放。


其实它是一个递归操作，我们可以点进去 right and flash 操作，我们可以点进去往下去找到 abstract channel，paper，line， right and flash message。它是不是写出去的，它会帮你做一个自动的释放操作，这个是tell。再去点 right flash。其实你就看到这块你就知道了，因为它 right 方法就是循环递归的去调。它会帮你去把实际的资源。会帮你去做一个释放。我们会看到这里边在什么情况下去做flash，所以我们就不详细的去给大家去演示了哈。


所以我们在使用 net 的时候，关于 buffer 的释放，你一定要注意一下，什么时候可以释放，什么时候我们要不能释放，要传递过去，其实就是一个同步异步的这么一件事情。在这里我们已经把关于 buffer 它的内存的释放的时机跟小伙伴讲了。好的，这个也是在实际工作中使用 net 非常需要注意到的一个问题点，希望小伙伴们能够对知识点有所了解。当然它释放的时机有很多细节，我们后面如果有机会，我会带着小伙伴把 net 的 buffer 详细的去再做一个说明。这节课我们先讲到这，感谢小伙伴们收看。

