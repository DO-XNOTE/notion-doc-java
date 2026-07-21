---
title: 5-1 RocketMQ面试题-介绍一下MQ 在业务中比较实用的场景（0643）
---

# 5-1 RocketMQ面试题-介绍一下MQ 在业务中比较实用的场景（0643）

[image](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/478fdad9-7903-44b5-b6c5-6e1b4f6e81f6/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663PCW5YYV%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T232233Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCICGWeTGA1oXxqo1Hx8o01KM02oTkiUL0cU6sfjTN1geTAiAS2MNC6ycdHPTy9jmWaxN6SZhry8emgMgFSa5%2FeaYQ4SqIBAjH%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMVJ3YaZ9%2BqyFmKPIDKtwDamR83VzbtD4jSeEf4hkBkHZzIflkmpVZZf%2BoxRCuE6SzjeE%2FzxTKYVATBlc%2BelK36VeWHghSg2Tkn3vmS3pvBBo7MwD5SGpTGpdtvc5Y3S8KifErZUx%2FZLO4ndFNP45mnP5F%2FdPnbdNucAyMZdaWDoH9Nu8Js63lPIql7nQaMDyL5FY21RRr5cqAuV12Gi2n9xsva430jflEOnUIW%2B1C6HF8xbm%2Ffkv%2BxJfXSx%2FbGyJLe0RnMZxQfHITr9xnz59KxPnqXMx5hGS%2F%2Fwzt49EIm7LtzunFV%2BNR7ukfCSNEUp3CjO3%2FgskNbAIIjrsMOQjFz5mJxB4%2FjZyXngFnPsWU6rVYcMWy6YnPbsld8iEyP0iMsaaiNRCzDTDSe6Oh7Q2XDAA8lVN8rZCyBxMX22z%2F42f2IO9igsjZs0MOepId3UdeCLUQg3ooHYj%2BwiVQulNz0FicmgjyQoQ%2B3cyHYK1f45nA235gaQCR63hgHNSNUBC5h3ga2RlpTIPkLTv9G3mLIKnVHQhWOk2jn9jHVAkJa94Kw9XQpWoBBXwyWk10TDK1yiKlrtwAvIpmKo%2BxO1ERAVsn3JmRppthdfIGBw1%2FynVuwrCAx2vtHSWrdwPyRDAOpIkCmYkkONIVrIow%2Fdj%2F0gY6pgE2a%2BWnHBE7%2FwLJDN7lt7auHwFxaoadfhK7wP0NF%2Bx8ZNNRuByYdB04BxbGehisomrGBD8XuE7LWSgykSNBPTWUSldra7K9KbHs3lQUC5XIYlm%2FeQfL2BLfaOEb5eQPRt2Q08dDZya5m%2BX8jZjfphsKgVzt9IIygqwYjiPWYqjIKbGeuXNf7HoRKwtQZOiwVOXB3nUrTBSlcN3mvIG54FZSY4imVfjE&X-Amz-Signature=a95b7a1b18b279f37567a8de3ff0bd1021da1b78db5d69872ed273bfee7837b9&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

们，大家好，嗯，现在我们来介绍一下 rock MQ 面试题部分，通常对于 MQ 的面试题经常会被问到，介绍一下 MQ 在业务中比较实用的一些场景，其实这里面的 MQ 并不特定指哪一类MQ，比如说 rock MQ、 TMQ 或卡夫卡它都属于MQ。


那么这里面我们怎么回答？我们可以先分几个步骤，第一，我们去介绍一下 MQ 是什么啊，以及 MQ 的特点，再去基于 MQ 的特点来介绍一下业务中我们可以适比较适合用 MQ 一些场景，比如说对 MQ 简介， MQ 它是一个 message 块，也是一个消息队列，它是指我们把一些消息保存在一个容器里面。具体的定义，这里面它跟类似于数据库缓存，用来保存数据，当然与数据库缓存的产品比较，它有一些自己的特点，这些特点比如说先进先出，如果说不能先进先出它就不是队列了。


消息队列的顺序在入队的时候就基本上已经确认了，一般不需要人工干预。当然也有一些消息队列，它支持一个优先级队列，那么这是另一种说另一个话题了。另外它支持发布订阅，那么发布订阅是一个比较高效的一个处理方式，如果说不发生阻塞的话，基本上可以理解为是个同步的操作。


当然 MQ 我们也介绍它可以支持一些，比如定时的消息，我故意我们设置一些颜色事件，那么还有它支持一些持久化，通常对于我们处理消息的这些中间件，它都是可以把我们的消息进行落盘处理的，也就是说如果说特定场景的宕机，它不会丢失数据。另外它也是支持分布式的，在这种大流量、大数据的使用场景下，只支持单体应用的服务软件，基本上可用性是比较低的。我们支持分布式部署，还能做到一个横向的扩容，这是我们 MQ 里面它的一些特点。我们了解了 MQ 它的一些特性以后，我们来再看一下它的应用场景。


首先我们 MQ 它是一个异步处理，另外就是说它通过异步处理可以做到一个系统的解耦，另外 MQ 它可以做成一个缓冲，对于一个 MQ 我们可以进行一些流量的消锋，等于对于 MQ 它的一个特征，它可以处理一些比较大的一些数据量，比如说像 Kafka 对于日志的预处理，还有一些消息的通讯，我们发送消息的话我们理解为是个近 40 的操作，一些消息通讯可以点对点的一个发布。


那么基于这几点的话，我们对于我们先来说异步处理，异步处理的场景比较多，比如说我们订单交易完成以后，通常我们会对这个用户进行一个积分的增加，那么我们交易完成是我们的主逻辑，增加积分可以理解是一个相对边缘的辅助逻辑。那么如果说我们交易完成以后，比如说我们是生单、支付等等这些操作完成以后，那么订单变成完成，那么订单变成完成以后，我们去可以发个消息出去，那么对于我们的积分系统接收到这个订单支付完成订单完成的消息以后，可以对这个用户的积分根据订单的金额进行一些增加。那么京东其实也就是这样一个逻辑。


所以说我们可以看到订单交易和积分增加它并不是一个完全实施的一个过程，其实它不要求实施，但只要它能做到一个，我们可以理解为一个追踪一致性，也就是最终能把这个积分加上去，用户就没有投诉就可以接受了，这是我们可以理解为一个异步处理。同时这样也是做到了我们的交易系统和我们的积分系统进行解耦，那么交易系统和积分系统它的变更是基于消息进行驱动的这样一个过程。


嗯，另外对于比如说流量削峰的话，怎么去理解？假如说我们的，尤其是秒杀系统，对于秒杀系统的话，它的一个业务特点就是会在很短的时间内带来很大的流量，那么这种情况下，我们在设计我们的交易系统的时候，如果说让我们的系统直接承受这么大流量是需要一个很高的成本的，那么这个成本它是也可以理解为在短暂的一瞬间去使用，其实是比较不划算的。


那么我们可以把秒杀过来的这些请求都收集起来，我们放到消息队列里面，那么消息队列通常来说作为一个分布式的中间件，它很容易承载比较大的一个请求，因为它的处理过程这是无业务逻辑的，所以说它可以接受很大的请求，那么我们的业务系统呢？秒杀系统可以消费 MQ 的信息，那么进行一个处理，那么比如说我秒杀的时候 100 个商品，那么在很短的时间内直接上来上万的请求，那么我就相当于是我们可以基于一定的顺序把前 100 个消费完，那么这样的话，我们认为它可以理解为秒杀成功就抢到了对应的商品。


那么后面的业务处理，当我们在我们的秒杀系统处理完前 100 个以后，后面的东西，那么商品已经没有了，后面可以给用户一个提示，当前商品已售空等等这样一种钞，这也是解决了我们一个流量削峰的一种方式。还有对于日志处理，日志处理也比较容易理解，通常我们的系统我们会基于 Docker 的方式去部署系统，我们的日志对于磁盘是不敏感的，所以说我们的日志落盘以后，很快就基于 rock M6 的方式同步出去，同步到我们的一个日志中心，通常是 IDIS 的这种分布式的日志存储空间。那么基于这种方式的话，对于卡夫卡它去存储我们的消息进行一个异步的处理，也跟我们提供了一个很好的帮助。


另外对于消息通信的话，这种点对点的订阅发布，或者说是我们的广播模式，或者说是集群模式，其实这里面也是一个比较有用的一个场景。恶来说，其实我们在已有开发过程使用 MQ 最大的一个方式还是因为我们需要做系统解耦，那么 g n， g m q 作为系统解耦，我们订阅我们关心的数据，这是我们通常使用比较多的，那么其实对于流量削峰这种情况，可能我们使用流控软件，流控组件会更方便一些。


通常介绍完这些内容的话，对于面试官一般会能得到肯定的答复。这里面大家记住我们如果对于一个抽象的概念，比如说 MQ 或者其他的一个什么概念，我们一定要对它简单做个介绍，来介绍它的特点，基于介绍和特点来去分析它的一个具体的问题。比如这里面我们是实用的场景，那么我们分析的具体的使用场景，所以说我们可以简单几句话，也就是说它可以支持异步处理，使用异步处理的场景系统解耦，那么进行业务解耦的时候也比较方便。流量交锋、日志处理和我们的消息通信，那么这就是我们 MQ 在业务中比较实用的场景。


