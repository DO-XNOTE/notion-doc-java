---
title: 2-1 本章概述（0409）
---

# 2-1 本章概述（0409）

同学们大家好，这章节我们开始学习 Rocketmq 的核心源码解析，那对于源码解析，我们首先来认识一下 Rocketmq 源码，那么我们会通过官网来了解 rock MQ 的门户介绍，并且通过 get help 医疗的介绍了解源码结构。同时我们会把代码克隆下来，通过介绍 rock MQ 源码的各个模块，让大家更直观的了解它的一些实现细节。同时在这一部分我们会部署一个单机版的 rock MQ，用于代码学习和开发的一个验证。


接下来我们会介绍一下 rock MQ 源码解析的 name Server 的启动流程，以及我们这里面的 broker 启动的流程。其实我们知道对于我们 Server 端的部署，主要是 name Server 和我们的 BROKER Server 这两部分的启动过程，其实我们能了解一下对于它的一些工作原理了解是非常有帮助的。那么这里面对于 name Server 和 broker 的启动疗程了解清楚以后，我们要做的是什么呢？我们要去了解一下我们消息发送的流程。


消息发送我们通过producer，也就是我们的 rock Mute client 端基于 producer 来发送我们消息。在业务方使用 rock i m q 的 Clenan 端，不管是发消息还是我们消费消息，都通过我们层层的包装，让我们对消息的处理越来越方便。


我们可以使用 rock MQ 原生的 Claude 端构建对应的 producer 发消息，我们也可以使用 rock and 跟 spring 集成的对应的我们的 rock MQ spring boot，它的方式发送消息，那么我们可以基于 rock MQ 的 starter 自动构建对应的消息爬虫器，也有对应的 rock MQ 的template，我们可以进行消息的发送和接收。
通过 spring boot 对我们 rock MQ 的包装，它会依赖对应的 spring message 这样一个模块，对于我们的 Messenger 进行一个抽象包装，可以基于对应的 rock Anchor template 对应消息的发送和消费。


其实这样使用已经很方便了，但随着 spring Claude 的兴起的话，我们知道我们会把消息的发送的包装成一 stream 流，那么这里面对于 spring Claude，阿里巴巴其实也对 rock MQ 进行了包装，那么使用 spring Claude 阿里巴巴 rock MQ 的集成，我们可以更加方便地对消息进行一个发送和消费。


我们知道不管是 stream message 的包装，还是我们基于 spring code stream 的包装，它们做的主要目的就是屏蔽底层，也就是不同MQ，它的实现逻辑与一些公共的功能抽象出来，可以做到对底层的具体实现进行替换的时候，对于已有无感。


所以说不管是 spring message 还是 spring code stream 这一点的话，它需要丢掉一些我们具体一些 MQ 实现的一些特性，比如说对于 spring boot 对于 rock MQ 的包装，虽然 rock MQ 实现了对应的template，假如说我们使用默认的对应的 MQ 的这个 operation 操作的话，它只能发送我们普通的消息，那么对于我们的异步消息 one way 消息的话，这种情况下词其实是发送不了的。


所以说如果说我们想使用 rock MQ 它各种特性，那么我们可能还是需要依赖对应 Rockmq 它内部的实现的API，这样的话我们一边使用对应 spring boot 或 spring Claude 给我们包装带来的优势，或者我一些便利，那么同时我们也应该了解 rock MQ 它自己 API 实现的一些特征功能。


通过这里面我们一起来去想，我们是应该使用 spring wood 或 spring close stream 的包装，还是说我们用原生的 rock MQ，这里面其实并不冲突，那么有看我们对于这个 MQ 它业务场景的需要。如果说我们并不需要 rock m q 这些它独特的一些特性，那我们使用 spring put 包装或者说 spring Claude stream 的包装就可以。假如说我们用到了 rock m q，它里面独特的一些特性，需要做一些更多的定制，那我们就需要依赖对应的 rock camera 给我们体现的 API 的一个实现好了。 rock MU 核心源码解析本章概述的内容我们先介绍这里，接下来我们去学习认识 Rocketmq 的核心源码。

