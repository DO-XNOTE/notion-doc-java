---
title: 3-1 【拓展作业提示】注册中心集成功能讲解
---

# 3-1 【拓展作业提示】注册中心集成功能讲解

[image](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/b427ea50-ba9a-4f5e-9a1d-d7f329968573/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WTWWBXQM%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T230048Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDfzEzOt%2FeJzN8wRAtiKcYl5SD0LwPW4riYxE%2FE6hCL%2BgIgNtZjDoHbRhWBUyEO5gI4zTU74sb9jxdTPwx7uBE2mHgqiAQIxv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDPSNrTxpNO31a4CvAyrcA2HNdQCHDt70pb764NxnhQBt%2FZuN7nfVwviKYLiH2zySrcpWP4WLpgQODobAaZidWZYP8jTbYSAhyudARLmf4xFdDbvLd6%2BnNlkfKiEaHU8bM9uauvitYZv%2BpmRJzy2HHCZtJmco7Zj9xc1Gqw%2FQfTquuTz59VWNXYozx0Ohwmat2xQVY9Q42e8XuUUV0dhLXpykILsUQSw1akCAQ2Oh6cpie24luhsbaGuk%2FGXnCmB2RwxcyEVeeEBEJ5GCNXUmxrCqcwrYMlk13OmVHjQKKrUvQJA85W7zuFOh4teozZHrKzmCfwwbsVxcxJ6Xq6v3ZGLH7etb%2FrD6FJtC1Z%2F0ixoHqmiBTEHp63%2B1%2FR3Op8D3kMDwmn7423KVaHL8mbNyv5%2FoLuYmt0RbSl32Yd1cp0S18ULjg9GjW%2FUTF3HBbZURL5KCy7Pn%2F3ZK3fNg37U99Q0vkWisFpihbHTLBQGtoQfVHE%2BdTtca775wL2KBcPR5Qnk%2FdJjlpH%2FgTLGfwa7wP6N1e4pgS29y5XzKbKSVYD3fGZie8R9vxmFMIXjRfZvfOsFac7WRTBVAQjlVLAiULbuQurUjhESsd%2FbeRU9B2OnnwK2l5mn7DCgBFHOw3s%2B1x2Gu6WAcPUSeW%2BYXMNq3%2F9IGOqUBUtcaRSe26nQA1dly4n1kLNoM4504Vz6y0MO1VKGobVv2Wz%2BPCvPqEcQgZa2QmRvx2CsdHOQzK3JVp2Q55K0spcvLGUXefUgLmdAGoljXFYrsO8i9ilE%2F6xRQRTj8awIpXjcGVGM8t7Va2uvy8GZi02lI58aAfCcMvEXGtS%2B1c6KhKm235Z%2FRNsbEvQCnXBgbBoxMbUwP6f0c6m7oPVYZ8v2K54s%2F&X-Amz-Signature=be39259675d5f652b8eea86de573c9009a853e1de819549219853846f3f17b51&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

hello，小伙伴们大家好，从这节课开始，其实我们整个的 RPC 框架已经结束了，但是其实由于我们是一个架构的课程，也是一个比较有意思有深度的课程，希望小伙伴们能够去。不仅仅是听老师去讲，小伙伴们自己本身应该学会思考，去自己去完成一些相对应的相关的扩展。


我在这里有两个小的作业。第一个作业就是我们要对我们整个的 r p c 框架把信息去注册到我们的注册中心，可以是zookeeper，也可以是Redis，或者是其他的对应的一些像 Kacos 等等都可以。第二个作业就是我们要跟我们的 spring 进行一个整合。在这里我期望给小伙伴们一些思路，后面的课程如果有机会，我也会把自己学实现。当然我希望小伙伴们，你自己首先必须要去想，去尝试，去做，希望你也能把这块做好。


OK，我们先说第一个小的作业，就是我们怎么去跟我们的注册中心去进行一个整合。注册中心说白了，在我们的 client 跟我们的 server 端以外，我们又加了一个新的东西，就是我们的 two capture。在这里我以 zokeeper 为例，我们在什么时间节点去把它注册到zookeeper？如果非常认真，你应该知道 RPC solar config，它在启动的时候我们有一个exporter。这个方法我们之前当然老师都打注释了。


我们首先启动服务端去干什么。这里边的注册是相当于把所有的 provider config 去注册到我们的 r p c server 上。紧接着如果你有 z k 是不是？你可以去把所有的你的服务提供的列表是不是？在这里。把所有服务提供的列表注册到什么 ZK 上？具体 provider 你肯定知道，它具体的interface，它的什么，它的父类会有一个interface，它的接口名称你知道了对不对？还有还有一点就是它的具体的引用对象你也知道了。当然引用对象我们可能不需要，所以我们只需要接口名称，因为对应着我们的 client 端就是服务的调用方，只需要知道接口名称就可以了。都把它注册到什么上，都把它注册到 z k 上即可。


当然我们现在 r p server 只是一个节点，如果有 10 个节点，其实你应该组织一个目录树。我不知道大家有没有看过 double z k 对应的目录树，它是怎么样的？它是这样的，它最上层。哈，我在这里画一下，它最上层。如果你是它最上层，肯定是有一个double。紧接着它下一级。什么？下一句是你的interface，比如come，点 b f x y，点service，点 hello service。它就是一个这样的信息。


在下面它目录树，下面有什么？在下面下一级的目录树，它有什么？它有服务的 provider 提供方，是一个目录树。还有一个叫做服务的consumers，就是服务的调用方。它是这么一个结构，它的服务的 providers 就是一个的。你可以理解为最简单的就是一个的 i p 加上point，它可能有多个 IP 加上point，这可能是其中的一个节点，比如幺九二点，幺六八点，幺幺点 101 可能是102，端口号可能是 8765 可能是这样的。哈，这个就是double。它我是挑比较简单的去跟大家说。


相当于我们在 export 的时候启动完了之后，接下来应该把自己的本季的 ip 地址，包括自己的服务的信息，我都应该给它注册到 Zoom 上，形成这么一个数。这是我们的服务的提供方，就是我们去暴露的过程。好了，现在我们已经说完了怎么去注册了，我期望小伙伴们应该对 ZK 比较熟悉了。对应的服务的调用方就是 consumer 端，它也是一样的。是不是我到底哪个模块是引用了它？到底启没启动？我肯定也是 IP 端口，然后加上 i p 端口等等，我到底有多少个consumer？肯定也是这样的。只不过有一点比较复杂的是什么？我们在我们服务的调用方，相当于调用方式是谁？是我们的 consumer 在启动的时候，因为我们之前的 API 在启动的时候，我们是直接想当然的哈，知道了它的 IP 端口，它的超时时间。


像这些信息，其实你都可以放到我的 provider 里边，都可以放到 provider 里面，在注册的时候统一去给它暴露到 ZK 上，包括这个地址，包括它的方法。它的这些东西。其实我们还有一点比较关键的，就是关于负载均衡的事情，关于 fire over 失败转移重试的事情，我们刚才看到了，这里边是可能会有多个地址，可能有多个服务，多个服务都是对应的 hello service 的服务的提供者。你到时候肯定得去把这些东西去做一个缓存，去缓存到本地的 map 中，或者是什么样子的对不对？你 consumer 在调用的时候，你这比如做一个简单的 balance 策略，去选择其中的一个服务，去发起 RPC 调用，这是这么一过程。


其实我个人觉得加上 zookeeper 这个东西其实是非常简单的，我相信小伙伴们从架构学到应该也是有能力去完成工作的。后面如果小伙伴们实在是完成不了，老师后面也会给大家去实简单实现一下，我相信小伙伴们一定能把作业完成。OK，这个就是我们的第一个作业。这节课我们就先讲到这，感谢小伙伴们收。

