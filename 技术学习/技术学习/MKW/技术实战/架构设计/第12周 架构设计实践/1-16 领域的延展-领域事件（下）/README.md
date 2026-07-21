---
title: 1-16 领域的延展-领域事件（下）
---

# 1-16 领域的延展-领域事件（下）

[image](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/5761839b-3108-4915-920c-04bf1cd84fac/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46656RGSD4O%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T230918Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIGHWs7LU4hBRuyxqjRQXJfKkxd%2F9%2FlfG%2Bdljmc%2B42mc2AiAt1aFKxPIp2qGmaPZW4X2rgQS0d%2FGay6AOmVnVVaJMXCqIBAjG%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMMJ1cnaguIChk7Xa7KtwDvyBvxSyOkNQT4txzsxz8utvmiXrvSujvByaMOv%2FISwC3BwqpHq6HUfnjCxKa48zu9366Bje9AXo%2BsP6hGX2DxmXgszziN2guEu%2FbnpZaMXt6Mnro9LjTGPtQQhYovxP8JeD8PptO4pM6rk1YLr54Czkxl%2F9AIRMdy48fSE1ccwEEls%2Ba2InDn68YHO%2BEfrZrSaqPg15OTOKEBBrs%2F94YazLtFHpCaNEGwdrAynSdUpy3fEezZwGypCL%2FqmWLvVU70gN0lsHMWhcnQCXmLf1kOhva%2FCpBdOZSUDitissPx3Aug0z8Cd76oejydi0RAsA7aX9S7xP%2FEdDlqWrNxe3P8x5pNXU831Wu%2BdfRQk%2FlQ1FPjKEqrVSVf4oMQcn9rJjhGH5tDh%2F8CZoonkeoonbzVymYLqX4pDCLRvCHpqYnMWK%2FSJUaW1iUVecWIZ9foedn1uiCDxLqG33GYulRmHUtXhuNgJTc1hnLldE3%2B2SpIRfkFNPL6of9Nxbh3e4yJx61iBgJD3X8I9Y5qBz7%2FwwJNOzXOgRZR0lUFOFzMNyBosRDeHqBxIugaxnLJtYk6Je4Ctwod4UF3WBpdts23bpWVatyZF%2FdARpf1k0SSb4X8%2FASmxl7Ydh4H%2FLlNQowk7j%2F0gY6pgHATWd%2BVgZtbq14aUXkVixPsz6FTUAQ0LADgvV%2FhNJ5UH15Xh8wTF27PJ%2BAFUsRZZlPOosu0vbzw58dUiW5TJLn3oEeny3AB1Aev%2BYiFmUS3MOac%2BHttbtAKFi2LCpxbDtmc1CeiEKKIWWz1kVdwgpDL%2F6u4%2BZSr68YXsPyQfQuEChHErMniP9zTPuB8TSGyaAnhbFlcI%2BU2z1x58aTGDMNbF4gYWcn&X-Amz-Signature=a6807b51dde90dfd7604070b4bc345e46d462b7d56448db1131e59fc4da6ce9a&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

[image](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/db087811-c7c3-45c5-9f54-2bda3e3ef5b3/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46656RGSD4O%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T230918Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIGHWs7LU4hBRuyxqjRQXJfKkxd%2F9%2FlfG%2Bdljmc%2B42mc2AiAt1aFKxPIp2qGmaPZW4X2rgQS0d%2FGay6AOmVnVVaJMXCqIBAjG%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMMJ1cnaguIChk7Xa7KtwDvyBvxSyOkNQT4txzsxz8utvmiXrvSujvByaMOv%2FISwC3BwqpHq6HUfnjCxKa48zu9366Bje9AXo%2BsP6hGX2DxmXgszziN2guEu%2FbnpZaMXt6Mnro9LjTGPtQQhYovxP8JeD8PptO4pM6rk1YLr54Czkxl%2F9AIRMdy48fSE1ccwEEls%2Ba2InDn68YHO%2BEfrZrSaqPg15OTOKEBBrs%2F94YazLtFHpCaNEGwdrAynSdUpy3fEezZwGypCL%2FqmWLvVU70gN0lsHMWhcnQCXmLf1kOhva%2FCpBdOZSUDitissPx3Aug0z8Cd76oejydi0RAsA7aX9S7xP%2FEdDlqWrNxe3P8x5pNXU831Wu%2BdfRQk%2FlQ1FPjKEqrVSVf4oMQcn9rJjhGH5tDh%2F8CZoonkeoonbzVymYLqX4pDCLRvCHpqYnMWK%2FSJUaW1iUVecWIZ9foedn1uiCDxLqG33GYulRmHUtXhuNgJTc1hnLldE3%2B2SpIRfkFNPL6of9Nxbh3e4yJx61iBgJD3X8I9Y5qBz7%2FwwJNOzXOgRZR0lUFOFzMNyBosRDeHqBxIugaxnLJtYk6Je4Ctwod4UF3WBpdts23bpWVatyZF%2FdARpf1k0SSb4X8%2FASmxl7Ydh4H%2FLlNQowk7j%2F0gY6pgHATWd%2BVgZtbq14aUXkVixPsz6FTUAQ0LADgvV%2FhNJ5UH15Xh8wTF27PJ%2BAFUsRZZlPOosu0vbzw58dUiW5TJLn3oEeny3AB1Aev%2BYiFmUS3MOac%2BHttbtAKFi2LCpxbDtmc1CeiEKKIWWz1kVdwgpDL%2F6u4%2BZSr68YXsPyQfQuEChHErMniP9zTPuB8TSGyaAnhbFlcI%2BU2z1x58aTGDMNbF4gYWcn&X-Amz-Signature=2983c295cc2aecf9e468ff6d4ec13758ae942392d1bd17eac95995186fbcf1f4&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

我们依然是打开我们的敏捷项目的代码，然后看一看 backlog item 这个待办任务，这个班长，对吧？那这次我们要看一看当一个待办任务被安排到一个冲刺，该人如何来进行处理。

[image](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/ea642b75-6b68-4435-be04-51e79f8724bf/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46656RGSD4O%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T230918Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIGHWs7LU4hBRuyxqjRQXJfKkxd%2F9%2FlfG%2Bdljmc%2B42mc2AiAt1aFKxPIp2qGmaPZW4X2rgQS0d%2FGay6AOmVnVVaJMXCqIBAjG%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMMJ1cnaguIChk7Xa7KtwDvyBvxSyOkNQT4txzsxz8utvmiXrvSujvByaMOv%2FISwC3BwqpHq6HUfnjCxKa48zu9366Bje9AXo%2BsP6hGX2DxmXgszziN2guEu%2FbnpZaMXt6Mnro9LjTGPtQQhYovxP8JeD8PptO4pM6rk1YLr54Czkxl%2F9AIRMdy48fSE1ccwEEls%2Ba2InDn68YHO%2BEfrZrSaqPg15OTOKEBBrs%2F94YazLtFHpCaNEGwdrAynSdUpy3fEezZwGypCL%2FqmWLvVU70gN0lsHMWhcnQCXmLf1kOhva%2FCpBdOZSUDitissPx3Aug0z8Cd76oejydi0RAsA7aX9S7xP%2FEdDlqWrNxe3P8x5pNXU831Wu%2BdfRQk%2FlQ1FPjKEqrVSVf4oMQcn9rJjhGH5tDh%2F8CZoonkeoonbzVymYLqX4pDCLRvCHpqYnMWK%2FSJUaW1iUVecWIZ9foedn1uiCDxLqG33GYulRmHUtXhuNgJTc1hnLldE3%2B2SpIRfkFNPL6of9Nxbh3e4yJx61iBgJD3X8I9Y5qBz7%2FwwJNOzXOgRZR0lUFOFzMNyBosRDeHqBxIugaxnLJtYk6Je4Ctwod4UF3WBpdts23bpWVatyZF%2FdARpf1k0SSb4X8%2FASmxl7Ydh4H%2FLlNQowk7j%2F0gY6pgHATWd%2BVgZtbq14aUXkVixPsz6FTUAQ0LADgvV%2FhNJ5UH15Xh8wTF27PJ%2BAFUsRZZlPOosu0vbzw58dUiW5TJLn3oEeny3AB1Aev%2BYiFmUS3MOac%2BHttbtAKFi2LCpxbDtmc1CeiEKKIWWz1kVdwgpDL%2F6u4%2BZSr68YXsPyQfQuEChHErMniP9zTPuB8TSGyaAnhbFlcI%2BU2z1x58aTGDMNbF4gYWcn&X-Amz-Signature=5d97d5d3012281ce6c5b9737b2cce37770e4e6069966df8ddfa5ca1c44825bba&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

那所谓冲刺如果大家不熟悉，可以看一看后续章节，我们后面有专门的 Devops 章节，还有什么项目管理章节？冲刺是敏捷项目里很常见的一个概念，**Sprint，它通常是比如说一周、两周或者一个月的时间，那每一个待办的任务都要安排在一个冲刺里面，才会有人能源来进行开发、测试和发布。**


假设一个代办任务，我们找找看它被安排到了冲刺，那这样它的这个调用方法是什么呢？我们往下滚动，就是 commit to 这个名词是什么？是一个动名结合，或者说是动副结合，动词和副词结合的一个方式来表示。我把我的一个任务安排到 commit 到了一个sprint，一个冲刺，那这样的话就会有人员来完成它，同时会在冲刺规定的时间界限内保证它能够定时定量的完成。那这整个过程其实有很多的assertion，这是我们前面说到的什么规约，基本的属性和约束，那完成这些约束以后，它会进行一个查询，这里的 evaluate status with 是一个查询，查询当前状态是不是无符合。我们能够把这个任务发布给冲刺，如果符合以后它就会把它实实在在的用 set Sprint ID 这样一个内部方法给安排给一个冲刺。


安排完了以后我们说过什么？所有的这种类似于是偏向于工厂方法的，或者是那种就公用方法都会在做完以后会推荐是发一个事件出去，看看有没有人来消费，这就是我们说的什么 new 一个事件出来，这个 new 一个事件就是我们刚刚的什么搭工，准备箭头，把剑放在弓上，就叫搭弓上箭。


好，我们第一次看到什么我们实际的领域事件的真相了，那我们看一下这个事件到底长啥样子啊？点进去。好，这就是第一个领域事件，那这个领域事件应该在这里，这就是领域事件的定义，那他这是其中的什么构造函数？他说什么？他说我其实是实现了这样一个接口，那这个接口呢？就是领域事件的一个通用接口，我点进去看一下这个 version 是很多什么很多的类里面都会有的这样一个version，那本质上领域事件最关键的是这个叫 occurred on，也就是一个世界是有什么它的时间属性，其他都可以没有，必然有它的时间属性，就是有这些时间才串联起这些事件的逻辑关系。


我们回到这个我们前面定义出来的这个事件，这个事件叫什么？叫 backlog item committed，也就是说我一个待定任务，我发布到了一个 Sprint 里面，那这样一个事件它会有什么样的内容？它必然会有具体是哪个任务的 ID 发布到哪一个 Sprint 里面，还有是哪一个租户在管理这个事情，以及发生这个事件的时间这样一些基本元素它就会什么，通过抽象的逻辑的概念具象化把它放到领域事件里面，那这个领域事件它有它的构造函数，那它的构造函数其实就是什么？把这些内部成员变量都给准备好就可以。


好，那当这个事件发布完以后，我们看一下后面会是不是什么样的操作。我们退回前面这个发布事件的过程，它会调用什么？ domain event、 publisher 这个类的一个单例，它单例里面它会有一个叫 publish 的这个方法，那这个方法是把这个事件发出去，那这个过程就是我们说的什么开弓射箭，第一步由班长把这个纸团给抛出去，我们看一下怎么抛。


publish 发出去以后整个过程是什么？是会去找一个 subscriber 的列表，所有能够接收事件的这个接收器，这个订阅方，他们会逐一来匹配一下我们这个事件和你能接受的事件是不是相关，如果是相关就由你这个订阅方来进行什么事件的处理。所以我们可以是一发多收。我们把这个件收出去以后，我们寝室里面可能有好几位寝室管理员，我们寝室王大妈、李大妈都可以接收到这个事件，然后进行相应的处理。我们就假设王大妈说到这个事件，我们看看她怎么来处理。


我们点一下这个 handle event 可以看到什么？这也是一个抽象的这个接口，那这个接口我们它的具体实现我们来看一看，有很多种不同的实践，我们假设还是在敏捷项目里面，这个实现方法是什么？是大妈拿到事件以后，什么？他会把所有的内容写到 event store，这就是我们说的什么公告栏，那一个学校通常只有一个公告栏，然后他把这个事件写到公告栏里面。


王大锤所在的班级有三个人想进行诠释的挑战，看看有没有人 3V3 篮球赛比他们更强的这个append，我们点进去看一下， event store 就是我们说的公告蓝事件存储，那这个里面有什么查询的几种方法，可以查出当前公告栏里有哪些事件是需要处理的？还有刚刚说的追加的方法，那它真正的具体实现什么，是由什么？由底层第四层来实现的，我看一下好几种，可以是什么 level d b 这种键值？对的，也可以是用 Hibernet 后台用 MySQL 来实现。我们看看假设用 MySQL 用 Hibernet 怎么实现。先把这个事件序列化，然后存成一个叫做被存着的事件，这就是 store 的event，就是一个被存着的事件，然后把它通过 Dison Hibernate 的 session factory 进行事务一致性的保存，最后返回给前端调用这个方法的。这什么具体的这个实际的调用方，那这就是一个事件的保存过程，就是把这个事件的写在了黑板上，写在我们公告栏的时候，变成一个可以用文字描述的人。


第三，我们回到校领导的一个页面，好，这是校领导页面。校领导会关注这个 event store，我这个全校唯一的公告栏，我们看一下一开始的校领导会什么。在初始化这个 event store，指明这个 event store 是用什么样的这个存储方式。那这里是 level DB，我们可以完全可以换成 hyblant DB 的存储方式。那存完了以后，我们还会指明什么？由哪一个收发师大爷来进行什么？所有事件的转发？专门会有收发处大爷把相关的这个公告栏里的事件公告给全市所有的学校，也包含他自己。


那这里选的是 Sloth MQ。如果大家对 slow s m q 不熟悉，那我建议大家用 Rabbit MQ， Rabbit MQ 在我们架构师一期的课程当中，由非常强大的什么阿沈老师单独有很多章节来聊。那我这里简单说一下， rapid MQ 其实就是一种标准消息队列，那它呢？通常会有一个exchange，这个 exchange 相当于是队列名，一旦指定好，我们这里是 n 加 PM exchange name，一旦指定好，这个 external 名称对端是吧？就是我们的消息队列的接收端，一旦有一个接收器专门去追踪这个队列，就会什么拿到相关的消息。


好，我们来看一看这个消息怎么样被发出去了。一旦这个消息队列准备好以后，这个收发师的大爷找好以后，校领导会怎么样？会通过一个定时任务轮询的方式，这也就是一个轮询的方式，不断的休息一段时间，然后死循环轮询的方式，然后调用 publish notification 这样一个具体的方法，这是个层层浸套的方法，我们用实际的这个点进去看，点到那个 try 里面去看它具体什么，最终是调用叫 notification publish 的这样一个具体的 publish 方法。


那它的实现我们看一下这样层次的调用，在我们自己写代码过程当中可以简化，那这里只是我引用一个，大家，对吧？ Involve 它的这个代码，所以相对来说看上去有点复杂，本质上大家可以简化到一次调用都可以的，我们看它的实现，具体发送消息队列有好几种，刚刚我们说了，如果我们是比较熟悉 rapid MQ，那我们就看 rapid MQ。


好，我们看一下 rapid MQ 具体来发送这个异步的消息了，它发送的过程当中它有什么追踪器？这些其实跟我们没有关系，本质是什么？ wrap MQ，一个叫 message producer 这样一个类，它是把所有的发送的这个准备工作，包含是选择通道、选择队列，全部在这里面进行完成，然后它会调用实际的这个 publish 进行发送。我们看一下 publish 发送的过程当中什么也是这个实现什么单例的序列化，然后通过 message produce 的实际的send，把这个消息给真真正正的给发出去。


我们看一下怎么发散的过程当中会什么？找到对应的这个channel，然后在这个 channel 里面调用对应的这个 exchange name，就是我们刚刚说的敏捷项目 external name，然后找到对应的q，最后把相关的配置文件和它的实际内容打包，统一调用那个非常知名的 basic publish 进行发送，那一旦发送完以后，它就是什么扔到了消息队列了。


一个消息队列是可以有多个什么消息队列的监听者，所以三个学校，敏捷项目学校，还有协作项目学校以及用户认证这三个边界上下文的项目学校都在坚挺。那谁收到了这个事件，我们看一下有一个叫 exchange listener，它时时在监听，那它监听过程当中它的关键代码就到这里了，叫什么？叫 filter 的dispatch，那这是一个什么消息队列监听器的一个本质的一个核心的监听代码，它怎么样？它收到消息以后它有多种实现方法，不同的消息队列的这个监听器，它会有不同的处理方法。


我们这里因为是哪一个监听的实践，是不是把 record item committed listener 这样一个时间？好，我们找到这个对应的监听器，这就是什么？还是我们敏捷项目的学校？还是收发师大爷？但这次可能是李大爷，他在那里监听什么？有没有消息过来？收到消息以后他看一下。


嗯，确实是来自于Angel， PM exchange name 这样的一个队列，那来自于这样队列的内容，我是需要接收的，然后我接收完以后怎么样？我把收到的消息抽取出来，通过一个这种叫 notification read 的类的方式，抽取数据完了以后读出它的什么 talent ID 来，看到什么 ID 以及 commit to Sprint ID，然后把这些 ID 封装成一个键值信息，或者叫什么 value object 值对象信息，然后再调用什么调用校领导的这个功能叫做 commit backlog item to spread。那最终什么？这个功能里面的本质其实就是获取到 tenant ID，获取到 Sprint 信息以及获取到 backlog item 信息，然后调用 Sprint 这个方法commit，把收到的这个 backlog item 信息发布给我们具体的 sprint 好，绕了一大圈怎么样？先是什么？先是由王大锤把信息扔出去，然后有什么王大妈这个什么寝室管理员写到了校园的通告栏，那最后由校领导指挥对应的这个收发师代言，把这个信息发到了全市的各个学校，那哪一个学校收的这个事件，还是这个学校的另外的李大爷收了以后，然后找到校领导。最后这是校领导指派工作，指派给谁？指派给 Sprint 这个班级来接受。


我们看一下 Sprint 这个班级的 commit 在干什么事情。前面是一些断言，我们可以跳过本质。什么本质？就是把这个收到的这个 backlog item 写到了自己的这个成员变量里面，就是也就是说我这个 sprint 我记录下来，我又追加了一个任务，这就完成什么两边的这个事务。当我们 backlog item 这个班级发生一个改变的，我要把我这个任务追加到某个sprint，最后通过一堆的这个校领导、收发师大爷还有王大妈等人发给了另外一个班级。
哪个班级？Sprint？这个是在 Sprint 班级底下， Sprint 也是一个什么，也是一个班长，或者也是一个班级，也是一个aggregate，那这个班级里面什么函数？ commit 函数，终于真真正正的是吧？让另外一个班级的内部成员变量进行了修改，这样是不是两边保持一致了？我 backlog item 认为我发布给了某个Sprint，那这个 Sprint 也认为我增加了一个 backlog item 的成员变量。


好，这里要聊一下最后一个难点，就是当一个班级里面包含另外一个班级班长的时候，我们要进行重命名，看一下这个 backlog item，其实返回的是不是这个内部成员变量，而这个内部成员变量是什么？它是一个集合，它是有很多个 backlog item，可以放在一个 Sprint 里面，但是它的类不是 backlog item 这个班长类，而是一个什么，而是一个 committed backlog 的item，这是一个重命名的班级成员类，我们点进去看一下。


好，这里要强调一下这是什么？这是班级成员entity，不是班长，这班长下面是不能管更多的班长，因为别的班长跟你不在一个聚合，不在一个班级里，但是你可以把对方班长换个面貌，本来是王大锤，你可以把它变成王小锤归在自己班级里面。那这个转换面貌的过程当中会丢弃很多数据，你可以看到这个 committed backlog item 的代码行数是多少？只有 100 多行，但是 backlog item 所有的成员变量和方法，它的行数达到多少行？我往下滚达到 600 多行。


也就是说当一个班级的班长在什么在其他班级出现的时候，他会变一个面貌，这个变一个面貌的过程当中会减少很多的相关信息，把只有这个班级所特的信息给省略掉，这也就是我们平时说的什么我们的 DL 层保持更多的信息。但是在应用和应用之间沟通的时候，是有一个叫 DTO 的概念 data transfer object，那这个 DTO 会减少一部分信息。


当什么 Sprint 这个班级拿到我们的班长的信息的时候，它保存下来，它已经是王小锤了，那这个时候他所拥有的信息就已经很少了，那通过这种方式，我们完全解耦了什么王大锤的班级跟 Sprint 的班级，这两个班级解耦了。虽然王大锤在那边化身成王小锤，成为了一个班子的成员变量，但这已经不是王大锤，也不是王大锤班子的成员。


好，聊完了这么复杂的这个领域事件，如果大家还有疑问，对中间跳来跳去感觉有点奇怪，我们完全可以在 QQ 群里面进行详细的沟通。好，回到前面的PPT，我们重新总结一下整个过程怎么样？

[image](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/757c3846-8fd2-4172-b8e0-5a570ef3cfbb/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46656RGSD4O%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T230918Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIGHWs7LU4hBRuyxqjRQXJfKkxd%2F9%2FlfG%2Bdljmc%2B42mc2AiAt1aFKxPIp2qGmaPZW4X2rgQS0d%2FGay6AOmVnVVaJMXCqIBAjG%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMMJ1cnaguIChk7Xa7KtwDvyBvxSyOkNQT4txzsxz8utvmiXrvSujvByaMOv%2FISwC3BwqpHq6HUfnjCxKa48zu9366Bje9AXo%2BsP6hGX2DxmXgszziN2guEu%2FbnpZaMXt6Mnro9LjTGPtQQhYovxP8JeD8PptO4pM6rk1YLr54Czkxl%2F9AIRMdy48fSE1ccwEEls%2Ba2InDn68YHO%2BEfrZrSaqPg15OTOKEBBrs%2F94YazLtFHpCaNEGwdrAynSdUpy3fEezZwGypCL%2FqmWLvVU70gN0lsHMWhcnQCXmLf1kOhva%2FCpBdOZSUDitissPx3Aug0z8Cd76oejydi0RAsA7aX9S7xP%2FEdDlqWrNxe3P8x5pNXU831Wu%2BdfRQk%2FlQ1FPjKEqrVSVf4oMQcn9rJjhGH5tDh%2F8CZoonkeoonbzVymYLqX4pDCLRvCHpqYnMWK%2FSJUaW1iUVecWIZ9foedn1uiCDxLqG33GYulRmHUtXhuNgJTc1hnLldE3%2B2SpIRfkFNPL6of9Nxbh3e4yJx61iBgJD3X8I9Y5qBz7%2FwwJNOzXOgRZR0lUFOFzMNyBosRDeHqBxIugaxnLJtYk6Je4Ctwod4UF3WBpdts23bpWVatyZF%2FdARpf1k0SSb4X8%2FASmxl7Ydh4H%2FLlNQowk7j%2F0gY6pgHATWd%2BVgZtbq14aUXkVixPsz6FTUAQ0LADgvV%2FhNJ5UH15Xh8wTF27PJ%2BAFUsRZZlPOosu0vbzw58dUiW5TJLn3oEeny3AB1Aev%2BYiFmUS3MOac%2BHttbtAKFi2LCpxbDtmc1CeiEKKIWWz1kVdwgpDL%2F6u4%2BZSr68YXsPyQfQuEChHErMniP9zTPuB8TSGyaAnhbFlcI%2BU2z1x58aTGDMNbF4gYWcn&X-Amz-Signature=d07b798c5a78fc2461cd20a59778623aa3e9845981b21e1a781906b35cd670fa&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

当王大锤要公告三对三篮球大赛的时候，他首先创建那个什么领域事件，然后我们把弓架在什么弓弦上，之后发出第一箭，把这个内容通过事件发布器发布出去，这就完成了我们这个 backlog item 这个聚合要干的所有事情，后面他就不是他的事情了。


然后有什么寝室的管理员王大妈把这个信息读取好以后，塞到什么我们的这个公告栏，也就是什么事件存储上，那这个事件存储保存过程当中，什么既实现了序列化，也实现了持久化。那之后会有什么校领导找到对应的什么收发师大爷选用一种方式，然后发布到消息队列里面，并指定消息队列的什么队列名、 exchange 名和 channel 名等等。那这个时候同一城市的所有学校的各个院系都开始什么通过消息队列来接收各个世界，那大家可能收的和关注的不同的消息队列，那这个时候恰巧是什么同一个敏捷项目，这个学校里面的另外一个什么收发师的大爷收到这个事件以后，又把这个信息还回给了校领导，那这个时候校领导发现这次事件应该是由什么 Sprint 这个班级来处理，所以他就让 Sprint 班级出了三位篮球巨星，然后王大锤和他的兄弟们就和 Sprint 班级的兄弟们开始什么在篮球场上干起来了。


这个时候我们的 back out item 的信息就是什么成功的注入到了Sprint，这 Sprint 里也有我们 backup log item 的ins，我们 backlog item 里面也已经挂载了什么 Sprint 的相关的 ID 信息，那这两边就联系上起来了。


好，聊完了。 domain event 领域事件这么复杂的一套流程，大家想一想，是不是所有我们聚合都要需要这样沟通啊？诶，不是，我们还有什么蓝 s 箭头，绿 s 箭头，更轻量的事件发布和接收，大家可以模仿前面的复杂过程，把消息队列去除，把这个公告栏去除，简化它的流程来实现代码的快速开发。好，下一节我们会在领域事件这样的一个知识点的基础上，聊一聊CQRS，一个经常在面试环节会跟大家聊的什么？

读和写命令和查询分离的解决方案，大家敬请期待。


