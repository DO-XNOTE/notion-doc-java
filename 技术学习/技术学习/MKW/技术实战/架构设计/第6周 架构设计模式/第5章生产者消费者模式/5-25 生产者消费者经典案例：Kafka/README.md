---
title: 5-25 生产者消费者经典案例：Kafka
---

# 5-25 生产者消费者经典案例：Kafka

了解了这个 activeMQ 作代表的这种传统的，相对来说它实现了这个协议规范，是 GMQ 的， AGMQ 的这种一个 MQ 的，那其实近几年大家冒出来的比较厉害的这种消息，中间就属于 Kafka 的天下了。为什么这么讲？因为 Kafka 的这个设计思路，包括这段应用场景，其实跟 MQ 有些地方是相似的，有些地方是不相似的。比如说 x m q 的话，它是既支持这个q，也支持这种topic，也是 Capsule 这种都是支持的，对吧？

[image](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/d3599965-d09b-438f-acab-c6c2a3cb62ce/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466Z3WRPX7M%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T230629Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCPd9sQ8MqlUMt5gVnybl8w6tHWYnqrBDB7bwpKaxkw6gIhAK2AcdJgbxrhGR6HMRSxJMXgDUBqdG7X%2FwdXluLHVB80KogECMb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgwSyMUBD2UrddOLee4q3ANG2xMyoTIk0vacj1dwNEmrSHk23FYR1cZztcTCFv%2BJECZIZP5TIp2iGplXoXbm874RT9yrIAPEz4d%2BWYb5SQmAWasq8y5teAF%2FDQNn21vYvw2tor2%2BnpkL4X0VzdzCVHGFnbzWBwcdRwwBrgAyHhxY8yQNw0AP7cggS3X7bif3WLqfUMudLDU%2BQ4CWt9hHG4sfo69OhDyA5JNabt5j0sJ%2FLj8QAUV6XrcigdrIWiaYl6jBi87flibBE01HCre53DeswPntZFchpR%2Bh681%2FQNKPephFMJQ3lO7pGfl7hsFa8v2f4vrnBkU86iAufb5%2Bi7JS0osso3VVCx8WHf7pdn64j3m%2FOwbhTf0biFy2SbI6DHGrtbyptdWnN9ltWKBOTZk4sseaZs4VJZGk9c3iSXwFR%2BsSNQbGfIiMGcnuiKWC1XH0miVgqI77amPvDgMnF9dOJPJ%2FSc%2BiGFvwjW0Tf7N1hMF%2BTELfFVTPoH5rhFz6s8BY3ogfSR7y9kSPSZeLUS9pophCj8ynIdZpYIuLSQYKILXEQVW5hH7YMigICd4LFQXejrbSOR%2FwD4D1yFxQkFh6f82lJ%2Fo9u4yAa8Gy9MZL5RMLZAxr6rGQdn%2F3RLjsMlp9%2FXoPTjWpOkpqcjDruf%2FSBjqkAXZ54%2BtXhw3C0oGLbn%2FFNu1%2FuiGU2tiv96hSgaWOVPSEmRRA8IDNaIWuJkocmoJ7GQdSWGTI7VYJ8wXpZ55opbvHTk4NkZz69xd%2BBj9cJw5XTU7XhRoI1lueft3lGq5PVpp0KtXNbxS0dapkzctuJ2DOxusa7ClzwbW2MphNmxOfg%2FrBeaEzTHusMlzwwYSQPWxOrrj3w%2FHzEw2PZVioKFq0pxUI&X-Amz-Signature=1dfc0ecec3a66a2244005b23a71688a072bae3b3ce8101c9927bafc200f6c5e2&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

但是在 Kafka 里面，它其实不支持这种 q 这种模式的，它只支持这种基于 topic 的这样一个主持方式。


那为什么这样子thats？因为它的设计思路或者它整体架构它就是为这个场景而生的。首先来讲的话，这个 Kafka 它最重要的一点，它生来设计成就是分布式的，就是天生它就是为了支持集群而来的。而其实像 active MQ 这种东西的，它最初的更多的提供的是单机版，然后这个 classer 集群这种功能它是后来慢慢衍生出来的，进化出来的。不是说他不好，就是他就说设计的思路和理念，就跟现在这个 Kafka 的设计思路理念是不太一样的，所以说 Kafka 近些年来能够风靡应用市场，作为中消元硬件也是有道理的。


为什么这么说？因为它的设计思路的不同使得它这个高吞吐力消费场景比较好，而且它整个天然是有集群功能，就是你只要是安装了这个Kafka，你把它当成要把它做成一个单机版玩，其实反而挺困难的。如果没有记错的话，之前比较早一点的，老一点的就好像是 0. 9 以前的这个 Kafka 版本。嗯，下载下来之后你还可以用它自带的这个 rookeeper 和这个Kafka，还可以搞一个单机版，很早之间的版本了，现在就你想下来之后你想遵守一个单机版好像其实也挺烦的，现在基本上就不支持，你必须得好像资金在自己机上玩的，你也得搞一个所谓的这样一个机器人才能玩得起来。


为什么呢？那就要从这个开发设计思路来讲，我一直在讲这个问题，因为这是 Kafka 它最初的，你现在感觉它像个效率，中间其实它最初的把自己的定位是一个 log 的community，就是说它是把这个 log 给存储起来，你可以用于说所有的事件的这个动态、什么东西的一个变化，就不停地把这个 log 往一个地方写，然后把这个跟踪的轨迹或者它的活动的这个范围什么之类的全都给它记录下来。


简单来说，任何一个实例的变化的记录，或者你消息是什么日志什么之类的，你都可以给它记录下来。它这设计目的是这样子，就是你可以把它是一个 log 的这样一个存储围控器，但是后面其实发现它这个东西，这个日志怎么放进去转要消费，就感觉跟这个生产者、消费者模式是非常接近，也就跟我们传统的这个消息流程件比较接近，我们要重复前面说的句话，其实它设计之初的思路就跟传统的消息软件不太一样，它设计的时候就是把自己做成一个分布式的设计。


它牛顿牛在哪里？首先来讲 Kafka 的这个集群就是 Kafka 的cluster，它是跟这个 rookeeper 这个集群两个是配套的，就是你要单装个Kafka，所谓的单装 Kafka 就是你只拿一个Kafka，你是根本跑不起来的，它必须得跟 zookeeper 这个集群两个来在一起运行才可以，而且更古早一些的版本的这个 Kafka 的这个SDK，你还必须得先跟 zookeeper 打交道才能再访问Kafka。这个原因是什么？原因是因为 Kafka 的相关的所有的一个节点，假设 the BROKER 信息全是存在这个 zookeeper 里面的，你原来是无法直接跟他通信的。后面这个 SDK 改了，就如 keeper 就藏在背后去了，就让你感觉不到 keeper 的存在，但其实你是离不开它的，这点大家一定要跟传统的认同来改，区隔一下，这个地方我就不详细讲如 keeper 它当时是干嘛的了，大家大概了解一下。


你可以简单的认为在这个地方 Rocket 就是来管理 Kafka 集群的各种信息和状态的，简单来说就是这样一个OK， Kafka 这个集群挺有特色的。首先来讲，我们前面已经讲过了， Kafka 它是不支持 q 这种模式的，就是传统的我们讲的这种点对点的所谓的 p to p 的东西，对吧？它所有的这个日志一般叫日志，也把它叫小写。它的存储方式都是按照 topic 来组织的，当每一个 topic 它会分成在不同的存储，这就是我们想到的另外一种这个集群的模式，就是partition。


首先一个 topic 它会被分成很多个partition，不同的 partition 会存在 Afka 集成入到不同的 BROKER 里面，但在每一个 BROKER 里面，它都会存储一个 partition 的部分，就是一个 topic 会分成很多个partition，然后这个 partition 分配在某一个 blocker 上面，然后某一个 block 就是某一个 block 里面的那个partition，它可能是这一个 partition 的一个master，其他两个都是 Snake 就是这个意思，大家理一下。


首先 topic 它是被分成不同的partition，就是说所有的消息都被按照这个 topic 的形式来进行组织，组织完成就在每一个 topic 它存储的时候，它也不就是实时词，是要把自己存在一个地方，而是把它分成了不同的这个partition，然后每一个 partition 它都有自己的组合重，这样子从很多个方面保证了这个东西的高可能。


所以说当你一个东西切分成不同的把地性，然后每一个把地形又有组合重，那是不是很不容易挂？而前面讲的这些所谓的什么怎么分配？broker，包括咱们 master slave 呀，还有你这个 party 信息， topic 的信息，这些都是存在 rookeeper 里面的，所以说其实你要访问这个 Kafka 的这个 broker 的，其实事先其实已经访问过一次这个 rookiber 了，只不过你通过 SDK 去放的时候你是感觉不到这一件事情的。但如果你用命令行的话，其实你死。


理论上你应该先去问一下 Zokeeper 现在有哪些Brocker，哪个上面它信存在哪里的，这些信息都在做 keep 上，你要先去创业拿到。所以这一个特点就是造成了 Kafka 这样一个比较特殊的高存储性和高存储性，就是说当你容量不够的时候，我直接扩 partition 就好了，对吧？我再加 blocker 把 team 再分一分，这样子这个 topic 下面可存储的消息就越来越多了，所以它的扩展性是非常非常好的，而且你想想它这种扩展方式之后，那整个系统的 support 是不是也上去了？所以它这个写恶性除了跟这个扩张性有一定的关系。


对，还有就是 Kafka 本身的这个存储的方式。诶，跟前面讲的 MQ 的这种方式不太一样， Kafka 里面它存储文件的时候，它是把它分成了不同的segment，然后完了之后它是把文件会按照一定的大小，就是同一个消息，就是同一个 topic 里面它会把它的按照大小来不停地分片，就再分一次。


这样子分了之后变成读取的时候，它是有 index 来帮助你去寻找这个位置，这个消息到底在哪里，类似于这样一种方式，而这个细节这个东西大家可以自己去查找一下 Kafka 的这些相关的文章，包括在官方文档里面，来看一下它到底怎么样蠢。没有文件的你就只知道它跟传统这个 MQ 的存储方式是不太一样的，而且它的这个 topic 的这个存储方式也跟传统的这个 MQ 是不一样。虽然大家都把它当成一个消息中间件，那这理论上它并不是个消息中间件，我已经讲了好几遍，那除了这个，我们讲到的这个 topic 本身的这个存储方式可能跟传统的不一样，而且消费方式也不太一样。


首先它的这个 consumer 不是按照一个 consumer 的形式来支撑的，它这边所有的这个消息它都是按照一个什么 group 的形式来的，所以说它虽然是一个 PUB SUB 模式，但是它跟原来我们这 MQ 的这种 PUB SUB 模式不太一样。怎么这么说呢？就是当在一个 Kafka 的这个 consumer group 里面有多个 consumer 的时候，它其实是把每一个 consumer 分配到这个 topic 上的某一个 part team 上面来。


怎么解释？再细说一下，我们前面已经讲过了，每一个 topic 它会被划分成若干个 partition 来进行存储，对吧？每个 partition 由自己的主充结构什么之类的，这前面都已经讲过了。那这样子，当你有任何一个 consumer group 进来的时候，跟这个局限打交道，当然首先是跟 ROOKIE 打交道，拿到了这个 topic 他所有的这个 partition 的信息之后，这里它就有一个配对的过程。什么意思？就是说这个 consumer group 里面有几个consumer，然后我这个 topic 有多少个partition，然后它就会把它配对。所以最好的情况下可能就是把 teaching 的数量和你的这个 consumer 的数量是一一对应的。是最好比如说你说 consumer 多于you，那可能其实它就是这么说，就嫌弃在那里了，就嫌那对吧？没什么用。


那如果说 consumer 太少，那 partition 太多，那就会存在什么？一个 consumer 要应付多个partition，那如果一旦这个 consumer 有问题，那这个可能就会造成一些 reach 外的这样一个后果，对吧？所以最好的方式就是 tartine 的数量给你的这个consumer，就这个 group 里面 consumer 是一一相等的。


另外一个就是说它的困难不太一样是什么？就说它这个 consumer 里面，每一个 consumer 到 partition 上面，它的读取方式，它也是通过这种自己拉的方式，MQ，之前讲的这种 MQ x m q 里面都是推的方式，就是 server 往上推居多。然后在这个 Calica 里面其实都是以拉的方式为主，就是你是用 long pulling，为什么这样子？其实就是因为你使用这种可能的 group 的概念，每一个 consumer 它自己对应的这个东西在 cover 的术语里面叫offset，就说每一个 consumer 在一个 part 性上，它的 offset 那是不一样的，而且是字节维护的。


当然了这些信息都是存在这个 zokeeper 上面的，所以说是一个 group 里面的这么多个 consumer 被一个的 offset 是不一样的，就他自己读到哪里他不知道的，而且他要自己来维护这个 offset 的信息，就什么意思？就说我现在比较读过一条了，我要 commit 一次，告诉你我从一读到了2，下次你给我发 3 这个过来，就是这么个意思，所以说它跟传统的这种东西也不太一样，其实传统的这种 MQ 的形式来讲，它一般来讲你是不需要自己去维护这个东西，你只要发一个 acknowledge 到我们的那个 server 上面就写佣金上面就可以了。在这一点你却要维护你这个offset，就是你自己读到哪里你得自己知道。


为什么这么说呢？是比如说相同的一个topic，不同的可能的group，它其实在什么东西都是不一样的，你看上去才是读，它不是像原来那种传统的 PUB SUB，你每个收到的信息都是一样的。那这个人虽然是帕布萨，或者是虽然是topic，但是它的形式是非常不同的，就是你要自己维护你自己在哪里，你就说白了这个地方还是相当于说你一个consumer，它是独占了这一个，它提醒的这个 parting 和这 convert 之间的关系就像有点像，我只说有点像，这么说不是完全正确的，就有点像那种 q 的那种模式。在它发过来的时候，它是发到这一个 topic 上的，但是 topic 分成多个partition，每一个 partition 对你一个 consumer 来讲，它就有点像一个 q 这种感觉，这个比喻不是十分恰当，但是有助于你去理解这件事情。


所以这里就可以第几件项对应 consumer 来讲，它是对应到 partition 上面去的，这里有个 offset 的维护的问题，这些信息都是存在这个 zokeeper 上面去，所以就是这一切都让这个 Kafka 的实现方式，包括设计理念都跟传统的这个 MQ 的方式其实是非常非常不同的。


这里我们不会深入去讲的一个细节，或者怎么去讲这个卡的一个抗战producer，还有 conuma 怎么去实现，相对来说其实也不是特别神秘，大家去找一下对应的文档，官方文档，还有个 Java 提供的 SDK 来看一下就会有个初步的印象了解，我这里想要讲的主要是什么？ Kafka 这种实现机制和 MQ 这种实现机制其实相差特别大，你要根据自己的需要来选择一种到底哪个适合你，对吧？还有就是他们各个特征，哪些情况比较吸引你，比如说我这个消息流量特别高，那我个人觉得显然就应该选Kafka，因为它天生就是分布式的，而且很容易扩展。


相对来说传统的 MQ 的这种集训模式的方式是比它要落后一些的，这一点大家也心里一定要清楚，对吧？因为看法设计之初，它就是为了扩展各种分布式而来的，刚才我只是举个例子，还有包括其实像Kafka，你要维护这个集群也是挺困难的，因为它是既要有一个keeper， Kafka 来这两个均都要维护，所以做起来相对来说也比较复杂一点。


这里我就不深入写去讲解这个 Kafka 到底怎么回事，大家从心体上有个概念就差不多。这里展示的这幅图是非常好的反映了这个 compa 这个经典结构，所以大家好好去找一下官方文档，最好是自己能够在本地搭建一套这个开发的这个集群环境来使用，一样体验一下这个开发的感受是怎么样的，它跟传动这个 MQ 它到底有什么样的区别？只有当你去试过你才知道这个区别在哪里。这种组件适不适合你当前的系统或者未来你在某一个场景下，你发现你需要某些特征，是不是只有 Kafka 想提供给你？这一点，你自己要去看看文档，动手试验一下。

