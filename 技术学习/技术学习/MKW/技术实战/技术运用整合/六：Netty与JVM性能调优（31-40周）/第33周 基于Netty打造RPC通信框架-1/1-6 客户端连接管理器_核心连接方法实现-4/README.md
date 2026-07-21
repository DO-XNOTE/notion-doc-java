---
title: 1-6 客户端连接管理器_核心连接方法实现-4
---

# 1-6 客户端连接管理器_核心连接方法实现-4

[image](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/b2d95740-e69e-4298-973a-ebedc8108c4f/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46623EKT66I%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T230030Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIGEunowe5h927W3N%2Bg7W0lIWrUwuAuclNlp4Xrm0HwvcAiBut1znoR0%2BulmP1Ku3pTna9x8Xb0qJt3Fug%2FqnEp2EeiqIBAjG%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMgWR3B4fEy4Wti5E1KtwDAN0iVbZ3O2qWe0VgRLzd0z8%2FuzB0yFFAokNtP9sp7yUP2gcFZCkoiAOCaCABpkfhPnWEvs8w3jJ%2FEqfMNF8wvYthOywGxZ9PNiDdz5hFjrlLP5UfhBzJEE67qw7ARLGzBK61P6n846BQGPzRri7AhcF9jc5XMIBInBEuo4ZT9myLRTuQIsS7OxWEpPxN76FMnn%2B6aHs%2FYtHCBF%2BQF6GfBQsL7uLG%2Fz1RLWWVMfYKqKlOwT0ePxskKSO3ugVpXq5yuNVaLE5oZsk1pvpvU2a3C5OD5Ql8dbahOsFMEguJW%2B1XMcRgvaLYgjXpxewA39yA2oLDFS1AtOsHMjaAXMaldwoAa1J64gOpAWp4%2FArIIMeeKKmFq2w9j%2FbVvYNAEGLSGPmOQm2NIfUAGFhjtUm4LXM%2FqKqjSr%2BMZbHxXfO4z5UWnWdDdncLHv2ZDL6moRuerHkqZGT%2B0dslnHSHcLmm%2Fe4CLV2S8DVyDcXB7H8rz%2BnYfIpmXzh%2Brb76IZzUrMeAyud64XaH%2F0QNgnc%2BFl5qKI4akYUHuGm8tJb9R8i4EI5h2AN7t7Z%2FUVf0CIGMhBMRUW%2F%2BmcHMVhIL%2FunvSUNeb33tON6s8jAkQs2tUxcAtJzNIO427nnV9Xm5GUww2rr%2F0gY6pgFGMUNMRvfC%2B37IYMdMjRhCFcDlUK9D0h7Eh3dqpLHLRvAtDEGRo3RladYJSYYSt5zCv4LomhMibfRYqlS3pbEN32u6AN4%2BEzEMrkQAb0B3i%2FWWUF6iBIPCYjDqQPd%2FmR6%2BKsR5WVyWqVGQ6DWaUsqmO6rpIJGeqyRqhzUXDWz5voEhe2xhqWB0RfEMaWJ0nCWrZ7KMIeXYTJI6etSfziFuuv3MWpLg&X-Amz-Signature=82cb27b244e682a9b4050dcd3a19044fe5d06e0dd1812297fdd381689b98d780&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

所以在 clear 的时候我们就好办了。我们直接就可以第二get。当然还没有去实现 get remote beer 的方法，不，直接可以去写一个 get remote there 的这个方法。当然我去创建出来，哈，直接 return 就好了。 this 点 remote beer，它会有一个返回值，哈，我直接 return 它，返回的就是 second address。好。有了它之后，我们每一个 handler 我们要清除清除。


首先我们要知道它的 remote beer 是什么。人们的 beer 我能拿到了，那就是一个 socket address。我们用一个 remote beer 去接收一下，拿到了它就好办了。我们就直接从什么从我们的 map 里边，因为它就是key。我们看上面 map 叫 i net socket address，当然这个叫 i net socket address，是不是你可以也做一下对应，或者是怎么样都可以？其实 i net socket address 跟 socket address 你可以认为差不多，它直接可以帮我们去做一个转换。我们回到有了 remote beer，我们其实从我们刚才 map 中它 connected handle map，有了 key 了之后，我们就可以删掉 value 了。其实后面的事情就很简单了，我们就直接点 get 这个key，就是我们和 bear 这样，缓存的。
取到了具体缓存的handler，我们就可以把它干掉了。在这里面我们可以用一个叫做RPC， RBC handler，我们取到了，其实我们可以直接接收一下，也可以。在这里， i p c handler 我们就叫做 handler 了，这个 handler 是什么？这个 handler 就是我们真正缓存的handler，我们直接就想要把它缓存的 handler 删除，这是缓存的handler，我们怎么去把它？比如连接给它关掉。 handler 里面它应该有对应的 close 方法，就可以去释放连接。其实在这里我们直接调一下 close 就可以了。这 close 方法没有我们重新写一下 create method 好，说白了还是他。


r p c client handler 里边我们要调一个 close 方法，把我们真正的所有的资源做一个释放。有了 channel 点，我们有一个叫做right。 and 在使用 net 的时候，它有一个特性，可以有一个叫做 apple 的这么一个工具类，可以去调一个叫做 empty buffer 的这么一个东西，点 add listener channel future listener please。
你可以认为这是一个处罚事件，我们的 channel 可以主动的去发一个 empty buffer 一空的buffer，这个空的 buffer 发出去之后，我就可以被我们的 channel future listener 点close。就是这个事件所监听到，直接就会帮我们把整个的 channel 给它关闭掉。这是 Nike 提供的一种机制。老师在这里详细的说一下。


Nike 提供了一种主动关闭连接的方法，发送一个叫做 empty buffer，这样我们的 channel future 的 close 事件就会监听到并关闭连接，关闭我们的通道。好，这是一个他给我们提供的一种机制，只要是做了这件事情，连接就关掉了。好了，有了这个事情就简单了。我们调这 close 方法，是不是他会帮我们发一个空的，叫做 m t buffer 的一件事情，他就会把真正的连接去关闭掉了。当然前提是你从这里边能取出来，你如果取出来，你就没办法关闭了。


紧接着我们要做的事情是什么？我们紧急的事情，我们资源都已经释放了，我们就直接可以从它的 map 中把它移除。如果你想做的严谨一点，如果你真正取出来handler，它不等于空的情况下，我们去做真正的资源释放。取出来之后我们再去调 remove 方法。 map 我们可以根据 p 去直接做remove，或者你直接去 remove 一个对象都可以，我们直接删除，直接从 map 里面把它真正移除了。如果它不等于空，先把资源释放，然后删除map。OK，接下来是不是把它直接 clear 就可以了？调 clear 方法清除的工作就稍微有点绕。因为什么？因为有些资源你不释放不行。你先自我循环list，这个 list 是对应的所有的 RPC client handler。 RPC client handler 之后，你要通过它去删除map，你只能去通过引用。通过 remote beer，因为 remote beer 是我们 map 集合里的key，就是 i net socket address。得找到key。怎么去把 key 放到引用里，你就只能对它进行什么引用的。这么一个方式就是在我们通道注册和激活的时候，我们注册的时候找到China，激活的时候通过 channel 知道它的远程连接地址，把它去保持一下引用。这样对应着我们的每一个RPC。 client handler 里面都保持了远程的地址的引用了。


socket address 引用了。我们知道了这个引用了之后，我们直接从取出来。引用之后引用的 key 肯定对应的就是 map 里能 get 出来。 get 出来之后找到 handler 里边把 handler 它对应的资源去 close 掉。如果不等空，因为 close 方法有些虽然连接超时，连接失败，很多原因，比如可能不通，或者是怎么其他的情况。我们应该把对应的资源释放，调一下 close 方法，给他再次发一个什么？发一个 empty buffer，让他 empty buffer 能够触发 channel future listener 的 close 事件，把我们连接具体的通道给它干掉。给它干掉之后，这样资源就真正释放了。以后再从 map 里面去把 remote build 给它删掉。最终再把我们整个的 connected handler list 也都删除。相当于先删除所有的map，就是所有的 connected handler map 中的数据，然后再删除我们 connected handler list 中的数据，再清空。但是中间你要知道，你要删除 map 的数据之前你一定要做的事情，你先把资源释放，要不然你真正的网络连接资源没有去清空。你只是把什么，你只是相当于把对应的里面存储的缓存删了。实际上它 RPC client hello，它资源还有的没释放这个问题。所以小伙伴们注意一下 clear 方法应该怎么去做。


好了，我们现在回过头来看一下具体的 connect a single 方法。就是创建。创建完了之后，真正调用连接的时候，这是发起连接，先给他一个监听做什么事情。 clear 把资源都释放了之后，然后再重新连接，再重新调用 connect 方法，再帮我去重新做一个连接，每 3 秒钟去连一次。这是失败的时候，要把资源都释放，发起重连。


还有一件事情，在成功的时候我们应该怎么去做？同学们想一想成功的时候我们要怎么去做。来我们回看一下之前的对应的图。连接成功的时候，首先你要把资源干什么？添加到缓存里？说白了，你自己现在不是做一个什么叫做 connected manager，就是一个连接管理器。是不是你应该把所有的资源就是删除的 map 也要加到 list 里？好，这两个地方我们都需要去做，所以这个是我们在连接成功的时候要做的事情。所以我们直接拿到 China future，不需要去点 channel 点 close future 了，因为这是关闭的时候的一个监听。如果连接成功的时候，我们直接 at 一个普通的 listener 就可以了。我们还是这样去做，你有一个 channel future， listener 就是一个回调，在 channel future 的时候，它 operation complete 它。 future 有一个什么，有一个返回的结果。我们说他如果 is success，证明他已经建立连接成功了，返回成功了。我们可以打一个日志说 successfully connect 这是真正连接成功的。 to remove 它 server 真正的去跟远程连接成功。远程连接的地址 beer 是什么？就是我们的罗摩托比尔。我们直接加上对莫特贝尔在哪里？在这里。Ok。好了，这是连接成功的时候，我们已经知道了我们要做的事情。既然是连接成功，那就证明我们之前的那一部初始化工作都已经做成功了。我们直接把连接成功里面所有的资源放到我们缓存里。


同学们，你想一想，在这之前，在我们异步提交的时候，这里边是不是加了一个handler？ handler 是不是去 new 出来一个 r p c client initalizer？同学们，想一想，这个 r p c client initializer 里边我要去添加的内容有哪些？ init channel 可能会有一些编解码的 handler 业务处理器最终必然会有哪个？必然会有我们刚才一直跟大家说的 r p c client handler。


RPC client handler 才是实际的业务处理器，如果你初始化的时候你不把它加进来肯定不行的。实际的业务处理器这个是必须要加进来的。好了，具体怎么去加，我们后面再去说。但是我们现在应该明白，哈，这里面肯定会有它。好了，既然会有它，我是不是可以从我们初始化的时候去？在 handler 里面已经 new 出来。 RPC client init laser 在 RPC client init laser 里边，在 paperline 里边，我们肯定要加对应的编解码的handler，也肯定要加我们实际的业务处理器的handler，也就是 r p c client handler，证明连接肯定是有 RPC client handler。这肯定是没问题的。我们在干什么？我们在连接成功的时候，我们只需要做一件事情，我们找到连接成功所对应的 client handler，把 client handler 加到缓存里就可以了。


怎么去找你？既然连接成功了之后，那你这个 future 就点channel，再点pipeline，找到 pipeline 之后，你是不是就能调用 pipeline 去把你想要的 pipeline 中的他的 client handler 去找出来？对应的业务处理器到底是编解码的还是你自己的？说白了，我们在这加盟的，我找到配方案了，我就能找到具体的编解码的，还是实际业务处理器的handler。我们现在用的不就是需要实际业务处理器的 handle 了吗？所以他点class。是不是这一步操作就把我们 RPC 克兰的 hello 找出来了。成功的时候我们只需要做一件事情，把这些内容都加到缓存里，我们叫爱的 handler 都加到我们的管理器，就是 RPC connect manager 所对应的缓存里就可以了。直接调这个方法添加到缓存里就好了。缓存应该怎么去写？我们接下来看一看哈。


当然这个不要是讲内部方法，我们写到这里，这个方法的目的就是它是 add handler 的目的就是添加我们的 RPC client handler 到指定的缓存中，因为我们是一个连接管理器，添加到哪个指定缓存中？我们这里面所声明的缓存就两个，一个就是我们的map，就是我们的 connected handler map。还有一个就是这个list，就是所有连接成功的地址，所对应的任务执行器列表都应该存到 list 里。所以我们要添加的东西就是把新的 handler 加到 map 中，以及再加到我们刚才看到 connected handler list 中，即可。以及中。加到这两个中很简单，我们来加一下。首先假设我们先加绿色中，当然先加绿色，加 map 倒无所谓了，直接点艾特就可以了。因为我们对应的 connected handler list，它里边的泛型就是我们的 RPC collect handler，实际的业务处理器？它是一个实际业务处理器列表，再回过头来怎么去加到 map 中？更简单了，我们直接去调它点 put 方法 t 怎么去取handler，你都能找到 handler 点 get 什么？ Get channel？ get channel 还没有，但是我有一个什么 get remote beer。


其实取到的不就是我们自己的远程的地址？我们直接取到远程地址，它有一个 socket address，就是 socket address。其实你要强转也可以。比如你定义的是一个 i net socket address，这里边它返回的是一个 socket 的dress。如果我们 map 里边存的是一个 i net socket dress，也可以旋转一下就可以了。我们叫做 remote and address，直接就可以去做一个强转就可以了。强转一下，把 key 放进去， value 是谁？ value 就是他。当前的handler。这两件事情就已经做完了。爱的 handler 里面就把我们对应的新的业务处理器加到 list 中，并且也加到 map 中了。 OK 最后还有一步叫什么？同学们来回看老师之前的逻辑哈。


这里边最后一步还要做一个叫做 single no available handler。这什么意思？唤醒可用的业务执行器。我们在这里去先写叫做 signal available，然后 handler 这个方法唤醒可用的业务执行器。可能我们刚开始启动的时候没有可用的业务执行器，没有任何的实际的 RPC club handler，这个时候我们就应该阻塞。


当我们新添加了之后，我们就应该唤醒了。我不知道同学们理不理解这意思。我们举一个更形象的例子，就是我们的队列一样，假设队列里边没有元素了，就是 0 个元素。我们调队列的 take 或者是获取元素的方法肯定是阻塞着的。什么时候去调了一个 put 方法，往里面去扔了一条具体的数据，这条具体的数据你对应着另外 take 线程是不是应该去做一个唤醒操作。所以当我们去真正的去往里去加一个新的地址和一个新的 handler 的时候，我们应该唤醒另外的一个线程，让他去通知，告诉他什么我已经有一个新的连接接入了。所以在这里边我们先把代码先简单的去写一下，后面我们再详细的去具体分。

