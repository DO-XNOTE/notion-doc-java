---
title: 5-27 生产者消费者经典案例：Spring Events
---

# 5-27 生产者消费者经典案例：Spring Events

讲一下另外一种这个现在在消费者 MOS 的使用方式，可能这个例子相对来说比较细节一点，具体一些。当然大家平时在这个工作场景当中使用 spring 的时候，这是假听，特别是在 spring 的框架下面。这个例子是你在使用 spring 的时候讲在这样一个 context 之下，你有没有这种需求？比如说你现在在写一段代码，这个代码它可能是做了某件事情，然后做完这件事情的时候可能会影响很多下游，觉得它这个改变你做出来之后很多地方都会受到影响，理论上他们都应该做出相应的反应，然后根据这个收到的这个变化，他要做出自己不同的一个逻辑处理的这样一个情况。


就这种场景简单一点的做法，实话实说，简单直接一点，你把所有的这个相关的这个地方做成一个，并注入到你现在做变化的这个 b 里面，然后你一一调用他们相应的方法就可以了，对吧？这种做法说行不行？能不能用？那毫无疑问肯定是能用的，这个有啥不能用的？这个没有说不能用的，但是这样好不好你是自己想一想的，所以这个地方我们得问的是不是能不能，而是好不好？那有什么方法可以把这个问题变得更优雅一些，而且更灵活一些？不要这么重度耦合，因为我们已经讲过了，如果说你在系统当中是一种这种直接注入的话，这个都是一个很严重的组耦合，对吧？这是个直接的一代关系，所以这个是重度耦合，那我们能不能把这个弧度降低一点？第二是能不能这个东西变得更灵活一些？那比如说，那原来有 5 个啊，这个相应的病，它可能关注这个状态的变化，那现在比如说另外有两个它也要，那你原来改程序是不是还得把它一个调变？还有什么主动各种阐述他这样的东西可能不太一样，这方面是不是就不太灵活，也不太好？那有的时候有什么办法？这个地方其实 spring 框架里面提供一个 spring event 的这样一个东西，其实它也是一种咱们的这个 closer consumer 或者 pop sub 的这样一个机制的实现。简单来说它也是比较简单的。


首先来讲你就是这个程序定义一个event，

[image](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/aaff1124-db56-4a8b-b898-b0a610efa8eb/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46634ZNWQWJ%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T230630Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQC7Il7p%2BeJGy98eNNsPhYzmQ3kchsVjSX08RpsPpY3QjwIhAJiZ5veEyn0ahQ425O54D07pO5WTBthJK4IYySRHzAzhKogECMb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1Igw27xR7HYOF4OodXicq3ANXZltFld%2B5Ofih94zlxVfxqe8R4hnf6YVquBNAdskbJ0PxlrZNZkHvNaYgQuNAtaDqPDegWAdhNj2L7YMWy1BMhdQ1Erde94y39KYxADn2GxGuR7uLeMhuSp4Q2kRBSN2XqKN0ZKvGmrG5ecIxlGCD8Yyk8%2FYotEPJbv4Uo5%2FuQpHIV%2BzUVEpyWh1aqbURwcsvsu%2BOv4R3LcqvaXtQyW3F3QiP%2FGZldZySdxNX6xUknSF%2BhpA9A2HAsGV8cY0wYs%2F6o5rSMXOQB537e5VOoO5i66zYVnEoh7IEf9b%2F5AvxudLB7%2FhLDCDxsXjWJUDOXos5hmynZsq8loX8b6ICQwdftTMVT%2F8xjuAlk8TAZ8jsQBr6Ip32nZhJa4Gl4sYeKPyOIqNeb8f78mF1wWIecD%2Fahkv%2B9laQ2qCRtBZW0T5WmM6r8%2BXAADDl%2BLd0%2F5WjiLkFRrr%2Buscvi3eThmyIFG4FNIN5t5%2FqplYGtkWfBxfp%2FuaUYcKiRJnxPtn9F58rW15vpWtfx58TgORY4GxHPsKPhOccMd%2BQH%2BGxL1vMMIO5gy6JBb0R%2FZ38CUmK3fPoDAoxshlD2c0h28BZyqGQZN35c3xddMTfykzVyG%2B8euFeds9UzNCfPrP07QGCQDCjuP%2FSBjqkAbk6WiBC5k5%2B9%2BcY066bU7gZstzXmjcGoJ7MrhX51QoYapqM8DA%2BV2BbbNpZVfDyaF%2BJdQRLLPXjUpdaGhfv2JC4nVFYAhy5iZJ5ArwQ%2BiEf5i3LtsLGq1PjcGJQAnV87TXIAU%2Bozj9TChizA1NCgse5j%2BZrcVGLtJYeTxsJs%2BCa%2BTYUDQfyYkw9jcqeJo1wZYsnXtNS2xu7pMpZBbjssK8OhUGz&X-Amz-Signature=5a1e55ff31de5b7d3efd39720e978f9119aa4e3467b6f2b0718c48635c525473&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

这个你随便怎么构？随便构思这样一个event，定义这样一个类，然后你随便把它定义出一个数据结构，然后你再定义一个listener，这个 listener 就是我们的consumer，说白了就是这consumer，它就是关注于这个event，你只按照我们写的这种方式定义一个 annotation 叫 event listen 这么一个东西，然后把这个 event 注入进去，对不对？那最后你怎么把这个生产者和消费者关联起来？相对来说也比较简单。


在 spring 这个框架里面，它提供了一个叫做 application eventually publisher 这么一个东西，说白了它就可以把某些事件通过这个 event publisher 就是在 application 层面，就整个应用层面只需要对这个 event 感兴趣的都会收到这两个消息，会受到这个事件。


所以你前面讲的那个就是说做出来一些系统的状态改变，在这个地方就作为触发，这个 publisher 就是作为这个生成者的地方，通过这个 publisher 把这个消息广播出去，所有对这个东西就这个事件感兴趣的，都可以创建一个 listener 进行自己的业务逻辑处理，这样子你来想一想对不对？当你做出任何改变，你只要调一个结果，就是 application publisher 的 publish 问题方法，然后把这个问题传进去就可以了。然后不管有多少个地方对你这个是change，就这个状态的改变或者是什么事情感兴趣，他只要监听这一个事件就可以了，这因为这是一个广播消息的这样一个机制，然后完了之后你想想这样子的这个系统的灵活度大大的变化。首先来讲的话，这个 consumer 跟 producer 是彻底的分离的，这不存在强耦合这样一个关系。诶，原来最简单的原始是就是直接把这些所有对这个东西感兴趣的全外注入到这个生产者的这个范围，现在显然不需要了，因为他们通过这个 event 的机制，就是框架里面这个 event 机制把它解耦了。


第二点就是你现在要加多少个这个对他感兴趣的都很方便，不需要改。原始的这个出处档就是 consumer 的一端的东西，基本上你不用改，你只有一个方法，就是你自己去实现一个listener，然后来监听这个事件，后面拿到事件之后你怎么做它取决于你，你逻辑它也不干涉你。


我对外广播的时候觉得作为 consumers pollution，我是不关心那个 consumer 是怎么样的，我只管生产出的这个event，然后把你发布出来，然后你作为concern，你爱加多少个？爱怎么消费怎么消费，对不对？这完全符合我们之前在讲这个生产者消费者模式的这个特性，这个特征值对不对？各自独立变化对不对？其一，其二这个 or 是很松的，饱和度是很低的，而且灵活度非常高，就是你要增加一个listener，就是所谓的这个科很easy，你加一个就可以了，对吧？然后他们之间这个依赖关系也发生了变化，他只监听这个event，不再关心原始的出处在哪里了，这样还从某种程度上可能达到一种复用。


比如说有另外一个地方作为一个类似的这样一个变化，类似的变化它只要把这个消息发出来，唉，完了之后，只要对这种消息感兴趣的这个consumer，也就是我们这里所谓的listener，他只要 listener 这个有问题就可以做相同的处理，对不对？那所以说这两边的独自变化都是非常可以，对不对？那所以这种情况下就比原始的那种猪肉在一个挨个的掉，对，不知道高到哪里去了，对不对？所以说大家可以体会这个 spring 其实还有很多类似于这样子的一个，这段时间我这里是挑一个最简单的来给大家讲解一下， spring 里面有很多种 event 机制，你可以理成各种各的event，比如说举个例子好了，在 spring 当中它不是有产生性管理，对吧？而且这边的前后它可以把所有的这个有问题都可以弹出来，在你的这个整个 context 里面传递，你这对这东西感兴趣你都可以做。比如说在这个 commit 之前， commit 之后 transition begin， transition 结束， robug 的时候， explain 的时候你全都可以捕捉得到，做出对应的处理，所以这个是非常优雅的一种设计。这种事件广播性质的这样一个系统设计，就是我们的这个 pleasure consumer 的这样模式的一个经典实现。


在 spring 当中非常非常多，大家对这个 spring 的领取感觉也可以查一下相关的，这个 spring 的方法很大，然后以后你在移动的情况下，你就知道怎么处理，是不是可以更优雅一些，把这个异步化灵活性也提高了，而且没有强依赖了。所以说这种东西你了解的越多，对于你在实际应用当中的好处就越大。


你不要小看这一个模式，它好像听上去就那么几句话来描述这个东西，其实它的应用场景是千变化，你除了看我这里讲这个 spring 的这个 event 这个机制，这个地方找的比较细节一点，这个例子你其实也要思考一下，你以后在设计的时候，如果有相同的这样一个系统需求，你会怎么能实现？会不会像 spring 这种方式来处理，如果你要做的话，你是怎么做？唉，这个才是启发你的地方。


我讲这个例子，那个你不要觉得这个好像很简单，或者说这个是不太细节，因为咱们是架构式课程，其实不是这个意思。我今天讲到，不管我是跟你讲这种比较虚的，比较抽象的东西，还是通过例子来讲，其实都是一个模拟，希望你明白背后的本质，你也只有通过理解那种本质，然后再把那个本质不断的应用到具体的案例当中，甚至不断的从实到虚，从虚到实，你才能够来完完整整的掌握这个知识。这一点我希望大家好好的体会一下我刚才讲的一句话的意思。通过 spring 中有问题的这个传播的方法，能给你在设计系统中带来哪些启示？大家把这个作为一个思考，你好好思考一下。

