---
title: 5-23 生产者消费者经典案例：BlockingQueue
---

# 5-23 生产者消费者经典案例：BlockingQueue

所谓的跟这个生产者、消费者文博士相关的这个理论知识基本差不多，我们就到位了。我觉得当然也有可能说有些方面讲的不是特别深入，我觉得讲的特别的细节，这个取决于当时我们设计这个课程的时候可能有所取舍。欢迎大家在那个我们不可能的群里面积极的提问，我们也非常欢迎大家来这里做互动，以便大家互相交换彼此对这个相同的技术问题的一些看法。前面我已经说过一句话，就说随着我们不断地互相交换彼此的这个看法，那大家都会学到新的知识，对吧？互相促进，互相提高。


讲完这些理论体系以后，那我希望通过一些实际的案例，或者有一些比较经典的这种实现来给大家加深一下印象，把理论和实际相互印证，这样相辅相成，帮助大家更好的理解这些知识。所以我们第一个在 Java 当中就有一个东西比较经典的实现，就是 broken q。 broken q 这个东西它的一个特点就是你把它分成两个词来看，很容易理解，什么东西 blocking 和 q q 大家都知道，对吧？先进先出哎。


broken 什么意思？ broken 就是等呢，就是说你就一直得等着，这两者结合在一起是到底是啥意思呢？你怎么来理解？是不是稍微还是怎么讲说跟传统的这种普通的 q 它的区别在哪儿？有些同学是不是没有之前使用过或者学习过这种的时候，对于咱们这个就不是特别理解，其实典型的这个 broken kill 就是一个非常好的 producer camera 这个模式的一个实现，你可以想象 q 里面的基本规则是怎样的？有一个往里面放，有一个从里面拿，对吧？那就是典型的生产者，消费者，对不对？你看也有容器，就是我们这个q，还有一个往里面放的线程或者程序，就是在生产者，另一个在消费者，那就是什么？就是我们的 consumer 来自然，所以这是一个非常典型的这样一个，比如说 consumer 的模式的实现在 Java 当中，那我们来看一下，就那什么情况需要用到 broken q 呢？ broken q 的作用到底在哪？其实我想了一下，就我们直接讲理论，这个可能大家听上去比较枯燥，我举一个比较经典的例子，我觉得很好理解。


唉，不知道大家有没有喜欢吃这种早餐，就中式早餐，大家有没有去买过油条？买油条的时候你看油条就是什么样，一个很大的一个锅，有可能上面有一些这种放油条的这样一些设备，那完了之后有一群排队的人来买这个油条，炸油条的老板可能有一个人在里切这个油条，或者把这个油条弄成一个什么形状，然后另外一个就把它放到油锅里面，炸好之后就卖给你。
那视线生命当中一般的人大家喜欢吃个油菜，都喜欢吃脆脆的，热热的，冷冰冰的，一块就都软着不好吃，所以它就会有一个什么现象，大家如果有仔细观察这个东西就是一个非常典型的生产者消费者的一个模式，对不对？尤其是老板就是这个生产者，那我们作为消费者，那这就是消费者这个美团老说的对不对？但是它跟一般的产品稍微有点不同，在哪里？就说前面讲过，大家都喜欢这种脆脆的，香香的，肉肉的油条，对吧？那油条如果炸出来太久的话，那可能大家就不太好卖，也不愿意吃，所以说炸油条的人这个就很考研的技术了，它就使用这种 broken q 的技术是什么意思？就是如果锅里面的油条没了，所有的都全卖光了，这 q 里面没东西了，对吧？这个消费者应该怎么样？你会blocking，你就一直会等着，就排着很长的队伍，可能越来越长，就因为国里面没有油条，就 q 里面没东西，这个时候你就等待，那有人可能等等不耐烦就走了。
那是另外一种，我们就讲这种等待，这种这种例子对不对？他是不是就等待这个时候叫消费者就在等待 q 里面出现新的东西，就是消费者在等待锅里面出现新的炸好的油条，对吧？这是一种，那另外一种，我们就从这个生产者的角度来看这个问题，那生产者那当然肯定是希望卖出越多越好，但是由于这个品质不佳或者放太久就没人买，所以他也得考量说我不能砸太多，那所以说这个时候他别举个例子朝了，他看见眼前没人了他就会怎么样？就消费者没排队了，就几乎没几个人，那锅里面这几个油菜差不多就得了，他就不会再生产了，他也会等，他就会等到新的队友排起来之后，他才开始炸油条，这样子他才会不浪费整个资源不会被浪费，这样子打造了这样一个相对微妙的平衡点。


大家听懂了这种 block q 最中文的特征就是什么啊？可以看一下，

[image](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/85a847fc-4241-4eec-9fc0-a3a7fd3ad87c/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VW6HGIOW%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T230627Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIH%2BCNIRgYh3th%2FwKR7LWhQ%2BCuu6eC1SgVjvj7%2BweI3iSAiEA3rLSoFUR5FW%2FX8RQHikpztrsW%2BIBbhm27cEXR9YesloqiAQIxv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDGjKKC09HRKzn6y%2BjSrcA7t3zPqGwgO2Z6gEBXsi3sjRC0AsaKWYHSKAevEFWeoxRWD6sjvwVg2mEDjz3rJ6G2beMLPtVF87KXWxWDs%2FICjm%2BVXVjq4deq%2FC8Rccv1qP6H3tLDzAxIt5ylW58yUkca3TyKnJB5jqyszwo5BPmw1oyfyvsKUIJ%2FPDPCxhd%2F1jHszD3GTa6Ah5ctHvsIH9Fn2lZZ5razkCa3A%2BjNCvA0eW%2FvNhxWAfvdrlBDxWx1%2FP%2BpSdoH4tnFZFIxKNqmmeZaflJjJ%2B%2B9KBRl2UcAeoGg%2FVOsmN%2BmDDGk8oNjVySIgKhhNdH2um4Mfb4tqPbaaBrpzk16sVHHFNHnqC51soZcEnCconv18DYo7eiIypptCPrIrMa%2FEDQ3ENreMtkKgqTtmlitH28aaDIQLXK3ul4pVG8MVfanSta9VtG4gM9Bt7STpqrlnjZPtuZ7pxNnN4DR88gt72k9YNEQI1%2F3JfffmcdgwtDyk9y2AXrQfLp%2F5gvj2ZaPUZ%2BPdpoSoAviBbagn0%2BzAsidmVxhh2pKdoZ81QCFDzh6gdRhhl5usNEkaMuvg7reBFuix8zTxJ1sIBf%2F%2Bf1upBM4%2Fe7PDf3NQAlhK6ryOJlACacm68QS5LWVp8koIJBsm%2BaGBMPuNIMNq6%2F9IGOqUB3Ob88kxGRADj6FHKZyAub7lLrOVWLtlGWDCcYXVW9Jg9rPTwWzUvPGlAlvVFF7ucullKrt8OyD4VE8VistPhHzkaJcEXjp8JEkibbAoK2eW64MPJzNKfap7cDaNjJMUMeR4n7ofcfpSfYgZ%2FbZv3kvmjbwj%2BnBNgG8zgotTWzyBx8JhKfzlYgi1sH2lh%2BVHsT8P79r9ocPzEFvcFeah8iSJWIy8o&X-Amz-Signature=32b38df890fba30d9001e4ea41c0b6370ce246097c08f071245b60dfef74b479&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

一个当中我们肯定有 q 加好疑问，就是这个红社区就是我们的 q 对不对？那对于线程一，就是我们的这个生产者，他就往里面放东西，放数据，放什么东西？就像甲油条那个老板，他会往里面放东西，他 push 了这个东西到这个 q 里面去， push 进这个 q 里面，就跟我们的这个消费者来消费这个东西，比如现实生活中例子就是他要去买这个油条，他要把油条重新拿走，老板就不断的往里面放油条，这个是消费者就不断的从里面去拿油条。


这是一个很普通的一个行为，他在妙就妙的这个 blocking 这个词上面， blocking 那个词就是什么，当消费者发现这个 q 里面没东西的时候，他就会一直等，他等到这个 q 里面有了这个东西以后，不管是数据还是消息还是什么东西，它会一直等到里面有东西出来，这样子它就会继续进行消费。那生产者这个也很奇妙。


如果说，比如说我们这个 q 的大小事物，这红社区域是5，这里面最多放 5 个数据，或者 5 条交集，或者 5 根油条，这 5 如果满了之后那消费者一直没来消费，那生产者就会等待，而生产者就会等到里面的数据消的到了它规定的一个值，由它才可以继续生产，就继续往里面放东西。


所以说这种模式下就是一个经典的生产者消费者模式的一个实践，而且它在这生产者的这个生产效率和消费者的消费效率，或者从资源的利用率来讲，从两端同时来看，它达到了一个很微妙的平衡，我既不会让你排队太久，我也不会生产过多起的造成一个浪费，对吧？就是这种，这是 broken q 比较奇特的，会相对于说它普通 q 的一个特色，这种 broken q 就是强调一下重点就是怎么样就生产者、消费者两者都会被阻塞，直到这个情况发生了改变。


从生产者的角度来讲，就是说必须得 q 里面没有满，他才会往里面放东西，如果 q 里面是满的，就证明消费者那边不太给力，一直没有消费完，他就不会再继续往里面放东西了，这样子不会造成浪费。从消费者的角度来讲，如果说 q 里面是空的，他一定要等到拿到了为止。所以在很多场景下面，你可以去使用这种 broken q 的技术来完成这样一个事情，那比如说就相当于说我们不要在两个系统之间要交换信息对不对？那并且要及时得到处理，那可能就会得到这样一个系统，就是说我 a 系统往 b 系统的 block q 里面放了一个消息，那不 b 系统就要复制读，一直等到读到他就开始处理。


那另外一个人就是说可能这个生产这边就 a 系统越来越多了，就他这处理的订单或处理的信息或者分配的任务越来越多了，他可能就会往那个 q 里面不停的放，直到放满为止。然后再等，等到我们的消费者这一端，把这些里面的数据、订单都处理差不多，他再继续往里面放，以此来达到一个系统性的微妙的平衡。


所以说以后大家如果要在 Java 内存级别来实现这样一个生产者消费的模式的话，这个 block queue 是一个很好的选择，大家可以去看一下这个 Java 的 block queue 相关的 SDK 和一些经典的这个例子，来了解到底怎么具体的使用，反正重点就是这。嗯，三样东西，一个是put，一个是take，还有一个是它的 broken 行为，你只要把这 3 的关系理顺了，其实你要理解整个 broken q 其实还是相对是比较好理解的。

