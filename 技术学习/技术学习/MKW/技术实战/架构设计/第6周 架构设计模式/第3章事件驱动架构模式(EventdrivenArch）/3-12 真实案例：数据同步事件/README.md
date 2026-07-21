---
title: 3-12 真实案例：数据同步事件
---

# 3-12 真实案例：数据同步事件

不知道慕克网的同学们有没有关注这些比较流行的技术话题，我相信是应该的，否则你也不会来参加这个课程，对吧？最近这些年微服务架构还是越来越流行，如果你有亲手去从头到脚的参与微服务架构的设计、开发，实时上线，我不知道大家有没有经历过这样一个过程，你们在做这个事情的时候，最初你们可能会正常情况下，公司里面就是先对这个微服务的这样一个我们叫 bonded context 划分，其实简单来说就是一个领域的边界，就是说你要做微服务化首先要改造的就是这个系统的划分。


说白了就是说原来大家都是一个大一统的，这么一个袜或者一个架跑起来所有的功能，大一统就是靠这个极其牛逼顶着对不对？现在微服化讲究的是什么？分而治之，各自有各自的领域，我们自己要把自己这摊子事儿管好，同时不能去管别人的事情，就这么个意思，大概对吧？你只要有了这个 bounded context，那就知道哪些东西就是哪些数据，哪些功能是属于你的，哪些东西不是你的东西你不能touch，那现在这个问题就来了，对吧？举一个简单的业务场景，就是原来比如说我是一个订单管理系统，我要查找这个用户的信息，诶，原来很简单啊， selecting from users table so easy。


那现在你还能怎么做吗？当然是不能，对吧？因为 user 已经不是你的 domain 了，你的 domain 是跟订单相关的， user 要加 user domain 的，你要拿 user 的信息，要么就是聊调用一个 API 去拿到这个 UR 的信息，很擅长，对吧？但是你要调用一个 UR 的API，有没有想过有什么问题？首先你要调这个 API 就意味着对外界形成了一个依赖，而且这个依赖是一个强依赖，对吧？第二，一旦是有一个调用，就是一个集成点，只要有了集成点， potential 的这个风险就是非常高的，但失败的几率就比你自己在内存上做调用肯定要高很多。


那怎么来规避这些问题？特别是分布式环境下面？所以说很多人后面就想了很多办法，有一个方案叫做 unit source。 unit source 是什么意思？就相当于说大家都在同一个公司里面，虽然我们分家了，但是我还是要告诉，这就有点像什么。所以说你成家了，和爸爸妈妈分开住了，但是里面互相有什么事，还是互相打个电话通知一下，对吧？对应到我们这个系统设计上也就是这样子的，就是说原来我们大家是一家，但是毕竟我们还是为同一家公司服务嘛，对吧？不是什么仇人相见，说完以后不能见面的，那肯定不是真正。


所以说我有什么事儿我就告诉你一声儿，然后你拿到知道我的最新的消息，然后你愿意做什么样的事情？ take 什么的action，那是你的事情，我是不管，我只通知你说这样子。但是我反正是通知到你了，对不对？你愿意去就去，不愿意去就不去，就是这么个意思，就是 event source 就给了很多人的启发。一个什么启发？就说在微服务架构下面这个数据，我老是把它印证去扣API，我总觉得这个不安全。这个不安全不是指的那个 security 上的那个不安全，指的是说我觉得对我这个 fading point 诶，不安全，老师觉得可能会失败。那我就这样子，我就把调用远程的一篇作为一个备选项，我把你的数据给同步过来，作为我的主选项。这样子你看思路是不是又反过来了？这个行为 source 这个思路其实很有意思的，是吧？你告诉我你变化了？这个变化是很多含义的，不是真的只是 update 一件事情叫变化，从 0 到 1 新增了一条数据，它也是一个变化，那就是相当于说你有什么数据变化，那你就告诉我，对吧？

[image](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/a6821743-ebe4-4f7b-a37c-1a9e29cfe3f0/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665NPH7MVQ%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T230556Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCICFiCd2IFDKKuHZwtCbZnjQ8wxY4MTm40MRw8RfSo7%2FtAiBbzheeYxsQbMxzoYtZerRXZDPW84FnBagPCzLf%2FfIU1iqIBAjG%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIM%2F453AMf9kDV8DHdAKtwDxL6qiA35yqtdKpmW8quJdcznNdisc9BREp2sjA%2B0%2Bq8weiaXrmMXzjIR74B0o2h%2FRkWvHqDqzEJYtoi9jZzeWXcWFfWxBu1STo%2BZ7YqePeJy9efTu%2F%2FX87KTiRUkXYkB9mUV6sc5y4xoluTz2iriEY2Ie%2B%2BAGIDcpWGjqJ6foZUg0QR%2BU%2B5r4j55%2FjMYA%2B00oVkjwsS4Ec9CyzS7cX4mce9ZD4wOYXIVvXM73W6%2FMG8Ju2izKSho4oz8ICpZ8obwqLPqMrpCnkX9UEJYt4WvyBMPKzUnxt1B%2BqT4HWowau0qPCjLxEi4IPVenrteQsbsmyUyp6EgIJJsyvrA9feX9tTafSodBbAl1fDxcectvJocSde6kS170IWVRzzEsWj5qaUYbQn5F7xZFREGRjZTM7oe%2BROy9rkogW1%2BIKM3b3vxAarhU%2FM7MBsvPvXg%2BMHioq8Lv%2Fig4gad1eTkUpw5WMUjksHy%2BI7m0ww627BLNbSjUq1H4cZCcR8t%2BKAUuBja%2BJJvsHgzBZkTfB%2Bv3OD7pXAKUF%2BPoSFbMlas6XANtqdT8nUuuT%2FNxMZ%2B%2B34epjzUrAw4q2c1wjkzF5YMx%2FscW7es9AWDY5th1NSUMKHzYRC5H6EfS3Vl0TSixw8wnrr%2F0gY6pgHnp%2FK3sgxN10TcBkL8ODxQqvxlcR7B%2Fa8KwmdKT2tEIj9ofIgvNtBe7my0REBsyxKmmnla1%2FibuFiGHFHW2Ee7GjDjOQi7Obe0mmk1ehBVhNJo%2B1kYrKI4RegGl%2B8zlpzY%2Fa96XP7kOZ1gMsF7JV4tiJpi0HHUzmZ5MyJI1eCSnXQ8nW%2F2n9JTdo15VVZtTrLU7yO5cKiw%2FpycStGNwGdcAeFKLvth&X-Amz-Signature=f16691ae4784f9327e2adc4298aa6287bb8a4f9cc89dc0236356022b09211953&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

那我们来看一下这个场景，就是用户他做了些操作，在我们的网站上面，不管什么网站，这只是一个代称，它在网站上做了一个操作，自然而然就对我们的数据库造成一些影响。
这个数据库的影响那可能是方方面面的，在这个分布式和这个微服务化以后，整个系统它就不光是一个 DATABASE 了，它是 under DATABASE，甚至这个 DATABASE 都是异构的，有的是 Mongo DB，有的是Redis，有的是 ration DATABASE、MySQL、Oracle，这都是有可能的，对吧？之间也没办法再进行直接查询了，也不允许他们做，你也访不了，因为大家都不知道所在地方，可能网速不通，那所以说怎么办呢？前面讲过，除了掉 API 之外，那我们还有一个办法，就是说我把你的变化我给存起来，因为我们大多数在实现了这个 Micro service 的时候，同时会想到跟配套的这个 winter source 这种方法来配合使用，就是什么我有事儿就发生广播，就相当于说举个绿草了。


前面讲到了一个例子， you are 这个 data 就是，而且用户相关的信息，他决定说我要产生的方案，就说我任何一个信息的变更， user 的但是非敏感信息，可以公开的信息，基本就跟你 API 能够的信息差不多的全部要做广播，当然他不会把这个 password 给广播出去，没那么傻对吧？他就把 user 信息全部广播一遍在系统内部，当然是再强调一次，系统内部仅限于系统内部，他把这个消息就广播出去，这个消息广播出去之后怎么办就看你看着办，你爱咋办咋办，是不是听着这个话你爱咋办咋办？而且也没人管你？好像你的业务逻辑也比较简，我可能就是只要 capture 这个变化把它乘起来就可以，这是不是就跟我们事件系统架构里面的那个 blocker 模式很容易套上？为什么这么说？你想，因为 source 它的源是一个event，总归是有事件会发生，刺激到我们的整个系统的培训者的变化，然后你拿到了这个数据，你要做啥？做啥？这好像就是 single start finish，而且相对来说逻辑比较简单一点，对吧？再看这个 org 里面，就这个网站里面，它有无数个仔细的，有无数个microservice，那是不是你说我要把这个消息拿不出来协调起来做一件事情？肯定有这种东西，但是我们在这很大的这个数据层部里面，它肯定不也有这个问题。比如我对什么兴趣，我对什么感兴趣，我就拿什么数据。


至于说我对别的感兴趣，跟你没关系，你要拿什么数据，那是你的事情，我也不会支持你，因为我们之间没有依赖关系，我也不知道对你一无所知。那这个时候你看，就直接套用一箱我们的这个 broker 模式，我感觉是恰到好处，不知道大家是不是这么想哈，反正大家就比对一下吧。


模式反正都是套用适合的场景，哎，没有特别大的副作用，你就往上套，套上去了。这就对了，证明你的思路是对的，只要你套上去之后发现优点大，还缺一点，那就 OK 的，对吧？那前面讲到了 DB 的变化，广播出去，到我们一个共通的这样一个 data sync，就是我们 data source 的这个 unit bus 里面去，也就是说所有的 data change 都会放到这个里面，然后，哎，各个 domain 你 a b c、 d e 不起。whatever，你愿意来读这个消息，又来读，不愿意读那就是你的事情。


总之我给你多了一个选择，现在你要读这个消息，你看这个图是不是基本上就跟我们的这个 broker 非常非常接近，对吧？原始的这个 DATABASE 上面的数据发生了一个变化，然后直接传到了我们的这个 unit bus，相当于我们的 broker 上完了之后，各个 domain 就是我们的一个channel，或者说我直接认为它一个 process 就好了，对吧？那你愿意读的这个消息你就直接去读，那读的时候怎么处理，那是你的事情，你现在不读那也没关系，我也不care，因为这个里面就没有强耦合， procedure 之间它也是没有任何依赖关系的，也是生产耦合，对不对？所以说在这个地方就是形成这样一个模式，数据同步的消息发出去了，他会把自己的可功能性全部放在这个信息里面去，然后你愿意读你就读，你愿意存就存，否则你就把它当成一个通知，听一下就过了，也不用care，直接 skip 掉没问题。


这反过头这种设计架构呢？诶，影响就在于说我拿到这个消息，并且我持续化成功了以后，我就优先读本地，直接自己读自己。而且我知道这个 single 做 true 是来自于你的，对吧？我知道这个权威的源头是来自于你的，而我相信这个数据变化是及时的，当然这就是价格使用的一个 trade off，就是一个平衡性。那我为了这个性能，或者我的这个响应时间，或者我的escalate，我愿意牺牲你一部分的数据一致性，这 OK 的，那我就直接读本地，实在是读不到，我要在 fairy 或者 fail over 把它 fail over 到扩展成一片，达到最新的数值。这也是一个四个方式和一种设计方法，这种方法反正见智，技术难度上说句实话还是挺高的。


因为这个里面牵涉到一个分布式一致性问题，也就是说那个原始数据变化有多快？你本地存储的副本是不是有那么快？这个是有很大的一个问题的，对吧？那我们理想状况这里讲的只是一个探讨，开放式探讨说这种方法行不行，我不能说一定行，或者一定不行，取你的场景和你的公司的技术栈，甚至你的开发人员的能力，你能不能把这个事情搞定？我个人觉得是能搞定他，那是非常好的一件事情，因为这样子的话，无人对你，还是对被调用的就被依赖的那个接口，包括那个 domain 的系统，那都是非常好的东西，为他减轻了压力对不对？他又不管你怎么去，他只管自己是不是很稳定。


因为你如果说外面有几十个人，每秒钟请求几百万次，人家直接就压死了，现在一下有几万次请求 product 还降成几百次，哪怕降低这么多，那是百分之多少，对不对？非常好的一件事情，对双方都是有利的，唯一的问题可能是你要容忍一定的这个不一致性，这就取决于你的那业务场景和技术能力了。


还是那句话，你能够搞定这两件事情，这个我们在硕士的模式用起来是非常好的，建议大家思考一下这个同，我和我们的这个模式就是这个叫市井驱动架构模式，其实 broker 模式一起来思考讲的这个人的 source 这个模式，这两者结合在一起来形成了这样一个方案。这种方案好与不好，它的优点和缺点还是比较明确，很明显我相信大家都能够看出来。你自己这个比对，或者你跟你们公司里面的这个微服务架构，想一想有没有这种场景，有没有这种用法，我觉得你会收获更多。永远记住独立思考，把当前的问题难度提高， go deep 才是你不赚取的进步的最好的一个技巧。

