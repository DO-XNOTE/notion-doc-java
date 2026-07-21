---
title: 5-22 设计生产者消费系统：QoS
---

# 5-22 设计生产者消费系统：QoS

认定从生产者、消费者和容器的这三个大组件，我们了解了一下生产者消费者模式的设计的重要点，这些知识帮助您理解整个设计体系当中的大部分的费用，都已经基本上讲到了，对吧？但是其实你使用这个深圳的消费者模式，在你的应用系统当中的时候，还有一个东西叫做消费保证，有些地方叫QOS， QOS 就是 quality or service，就是你这个对外提供服务的这个 quality 是怎么样的？这里有三个不同的层次，我们来看一下所谓的这个昆仑点，它讲的就是说你到底能不能收到这个东西，不管你把它叫消息也罢，还是叫数据也罢，还是现实生活中的那个例子，比如说包裹什么之类的到底能不能收得到？我对你这个收不收得到这个东西的保证就叫做QOS，就你整个对外服务的这个质量怎么样？ quota service，对吧？在这个地方第一个层次就是我们来看一下这个 at least once。


at least once 是什么意思？

[image](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/7944d60c-032e-4ebb-9372-96ff13928856/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466Z6TWIUVI%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T230627Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIG3AAZDjHYFe03ek%2BO8m2H2aJvolj4srmRW7q9jPKP5aAiAD8mBMt1OsazaotjWhws9XAURt74YYAgFVwG9Vl3CPcyqIBAjG%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMbHxLUvkM7BnYShiyKtwDiDhd3S7s%2B1Xdq69mdkxG%2BhQ0aP8ihGm752i4MPc%2Bwnz3WmDmEenLVnoGOlxHqsc03ORfdTneFchfUrphtv4QIWZNTz0wDTviLIFX%2FU4IjlRn19UiL43Mt6cZ7D%2FWbrUxagaahjJk3e7CiokN8yjqggH%2B9PjI3Mh7n3XKoOyFsXAPcZTwX5Bl4ZqzojlER7pty3wy42%2FubFLHuCMrwKuRhARUHZUeB7tdfoKWyVM%2BofG3X7MkLSLeG%2BBh0QG8mHZ5%2Bi7Pm1206m0INS6kpCkxpTNG1MsdJ6H%2BQ8ZGGwPx5HL47v7MqDkW4Rtzti5JT9W2IySSIsDcILmaWtJy4lzg1kc0Ve8x5xMdti8fcjlfGFH2U%2FwIRuqVp2Go34H%2F0GKrl7axnM5DviNJwAYjYVYQGBhKKZ3530A2Qsa2VZDFxBJE1egiRj9WdLMwpMZUs7S5bi1V2e5gxG7dnfmfkfIz8B%2BtXCrFRPUhBfWkH5zfSH8tsUT%2FnSn35IH4C1WmlIaoJOknYaovo9PB%2BZxino0XdtP3JsGNM1cTxTbkA8S56veHKUH0NqmLbyV922AjsVp%2B46hfO%2Bvx%2F1iwEGaTV474rssk3pd%2B7SowK4K050a7C2LNZrjs7mrcwjW7hz8w8rf%2F0gY6pgFK18jsaOXRBZBgDEDZxkbF1NoyDXPAYB3FbUQ9KPAkILdPU7Pk0fZNhP8tHcDm%2FI7eCCdWYIv5Y3iuo0G6803q06yanis9nYeTRmfuKWW1MkXJqqKVqElZ9ju0otyhsT6xRSCmVpBDLI%2Fd2iVgwslcwVgL2qnav0zCoqdW6oFPFexyd%2BTKRtkj%2FxPakowvTWDomwaN%2FvTxiHv%2BODmJ%2Bedr62QUyMZx&X-Amz-Signature=2e77774d58260c337840f7c9d0e9153066b86a48da04c19f26290b086948bc9f&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

就是说我这个生产者保证这个消费者这个 consumer 他至少要收到一次。这个数据单元，就是说我发过来的时候，我保证你至少会收到一次，但是你不会收不到，是你有可能收到多次，所以你要有这个心理准备。


那这句话的暗示就是这种 Qos 的这个暗示就什么意思？说白了就是你可能会收到多条消息，但是你绝对不会收不到的话就证明我违背了我对你的这个承诺，这是另外一个话题，那所以说这种情况下讲的 least once 就是你可能需要处理一下多收到的情况下应该怎么办？那如果说你从整个系统的角度来讲的话，就意味着你在这个 container 里面可能有些数据是重复的，但是因为 container 本身它是不去重的，因为他也不知道这个东西到底是不是重复的，对不对？所以你在你的这个 consumer 端，你就必须要做低 dupe 或做一些其他的这些校验或者是什么的来保证整个，从业务的角度或者系统的角度来讲，这条重复的消息它不会对整体系统造成一个很大的影响，最好是不会造成一个很大的影响，对不对？所以这点对于那种怎么讲？就是说生产者不是特别有把握这个消息到底有没有发送成功的时候，采用的比较常见就是 at least once，这个有些时候其实你比较容易理解，就相当于你自己在做系统的时候，你比如说要调一个参考服务的时候，那你说我到底调不点什么？其实我不知道，我管它呢，我多试几下，等下我多点两下就差不多这个意思。


你刷一个网页你刷一下，我刚才刷没刷啊，我有点忘了，你再点一下那个刷音按钮，是不是就是这样子的一个道理？有点像这种感觉，这样子其实说白了，只要你使用这种操作模式的production，对于你的 consumer 来讲的话，你这个地方就得防重。如果是前面举的这个上网这个人讲的人，那可能就是你得防止这个用户重复提交，那对于我们消息来讲，对于你的 consumer 人这个角度来看，你可能就得低dupe，或者是把这个系统整个做成一个 b 等的功能。所以说 at least once 重点就是我保证你至少会收到一次，但是不保证你到底收到多少次，绝对不可能是 0 次。就这三句话你连起来理解一下，你就知道这个 at least once 的含义了。


重点说白了这个环节是你要在你的 consumer 端，如果人家告诉你我的 QS 是这种 to this ones 的话，那对于你来讲，你就用来去在你的这个消费者端，你得要进行防重处理，说白了就是这样子的，就是 at least ones this ones 之后我们还有一种模式叫做 at most ones。


at most ones 是从字面上来看，这也是很容易理解的，这是我们的producer，它保证卡拉门最多收到一次，

[image](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/436f3ad0-6772-4762-84c4-b5bb0ba384b1/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466Z6TWIUVI%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T230627Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIG3AAZDjHYFe03ek%2BO8m2H2aJvolj4srmRW7q9jPKP5aAiAD8mBMt1OsazaotjWhws9XAURt74YYAgFVwG9Vl3CPcyqIBAjG%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMbHxLUvkM7BnYShiyKtwDiDhd3S7s%2B1Xdq69mdkxG%2BhQ0aP8ihGm752i4MPc%2Bwnz3WmDmEenLVnoGOlxHqsc03ORfdTneFchfUrphtv4QIWZNTz0wDTviLIFX%2FU4IjlRn19UiL43Mt6cZ7D%2FWbrUxagaahjJk3e7CiokN8yjqggH%2B9PjI3Mh7n3XKoOyFsXAPcZTwX5Bl4ZqzojlER7pty3wy42%2FubFLHuCMrwKuRhARUHZUeB7tdfoKWyVM%2BofG3X7MkLSLeG%2BBh0QG8mHZ5%2Bi7Pm1206m0INS6kpCkxpTNG1MsdJ6H%2BQ8ZGGwPx5HL47v7MqDkW4Rtzti5JT9W2IySSIsDcILmaWtJy4lzg1kc0Ve8x5xMdti8fcjlfGFH2U%2FwIRuqVp2Go34H%2F0GKrl7axnM5DviNJwAYjYVYQGBhKKZ3530A2Qsa2VZDFxBJE1egiRj9WdLMwpMZUs7S5bi1V2e5gxG7dnfmfkfIz8B%2BtXCrFRPUhBfWkH5zfSH8tsUT%2FnSn35IH4C1WmlIaoJOknYaovo9PB%2BZxino0XdtP3JsGNM1cTxTbkA8S56veHKUH0NqmLbyV922AjsVp%2B46hfO%2Bvx%2F1iwEGaTV474rssk3pd%2B7SowK4K050a7C2LNZrjs7mrcwjW7hz8w8rf%2F0gY6pgFK18jsaOXRBZBgDEDZxkbF1NoyDXPAYB3FbUQ9KPAkILdPU7Pk0fZNhP8tHcDm%2FI7eCCdWYIv5Y3iuo0G6803q06yanis9nYeTRmfuKWW1MkXJqqKVqElZ9ju0otyhsT6xRSCmVpBDLI%2Fd2iVgwslcwVgL2qnav0zCoqdW6oFPFexyd%2BTKRtkj%2FxPakowvTWDomwaN%2FvTxiHv%2BODmJ%2Bedr62QUyMZx&X-Amz-Signature=ee142df1d69816d5574de33ed72605c529729ed194b867dda26313969513cf10&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

说白了就是说你可能收不到，但是你绝对不会重说你最多收到一次，就是说如果今天好死不死没发生成功，对不起，你就收不到这份消息了，或者拿不到这个数据了。如果说咱们一切都顺利，你也顶多就收到一次，你绝对不会超过一次，就你拿数据或者收消息的话就会这样。


现在这也就特别像银行转账一样，我保证你最多转成功一次，甚至有可能不成功，对不对？如果说张三给李四转钱的时候，发现李四多收到了一笔，这个可能性不是完全没有，但是从设计机制上来讲，这银行转账就是 at most ones，对不对？他宁可说不成功，但是绝对不要发生一个重复性这样一件事情，因为可能说重复带来的后果比这个失败的后果，或者没有发成功的这个后果要更严重，这个其实也很好的。


你就是我们刚才讲一个转账这个问题嘛，对不对？那你说你这个没转成功，那大不了我再转次，如果你转多了，这个钱要回来的话，这个从法律角度来讲就很麻烦。所以这种就这样子，跟前面这个 at least month 就像这样子比，人没给你女朋友发短信，发没发成功不知道，不确定，那就发一条呗，那大不了他说起码发重了，对吧？你要说 Atmos 呢？哎，发了以后管他发没发呢，反正成功了最好，没成功无所谓，这个后果可能就很严重了，对不对？所以说不管你选用哪种QOS，对于你来讲它最重要的一点是你要适合你的业务场景跟你的当时的context，这个是很重要的一个选择的条件，供你参考的一个参考系。


从业务当中你来看整体系统的话，就是说你可能有些数据或者有些东西你可能会丢掉，这是一个可能，它这样一个事故你可以用于是丢掉，或者说你可能整体这个操作它是一个失败的，从整体的角度来看它可能是失败的，但是对于你演讲的话你就得想一想这个如果丢掉或者是错误了，你再重来一次这种情况下可不可以接受？还是说你宁可重了，他带来的后果也可以更严重一点？说白了就是这样子，前面我也举了技术方面的例子和这个现生物的例子来帮助大家理解这一点。


说白了就是说你可能生产者这边他就有点不太负责，或者他宁可承担这种失败的后果的时候，就会选择 at most once 这个对于你比如作为架构师的人，判断一下到底这个场景应该是 satellites ones 还是 utmost ones，这两种哪一种？对于你来说整体的系统的实现难度或者处理起来的这个方便程度，它有很大的区别。


发短信你发重了没关系，但是你转账转重了，这个就很麻烦，对吧？或者说你从这个比方，我们一个包裹到了快递这种来看，你发货的时候，你宁可 at most once，也不要 at least once，因为你有些货物是很贵重的。那比如说你买了一个 Tiffany 的项链送给研究朋友，那你说商家发货的时候他是选哪一种？那肯定是 utmost much，对吧？没有发成功，或者发货的过程当中出了点小问题，那没关系，我到时候再发一次呗，对吧？但如果说我不确定我发没发，我再发一个呗，这可能就有点过了，对吧？比如举个例子，你是在网上买了一个小玩具小手套，大概就三五块钱，对吧？你如果说我没收到这个，商家为了自己那个幸运，管他发没发，我再发一次，我再给他发一次，他可以承受这个，那就是 at least once，对吧？刚才讲这个珠宝的这个例子就发生了和接受方，它就是 at most ones，对于这两者而言的话，其实取决于你的业务场景。


对于这种 at most ones 还有一个可能，就是因为我们已经讲过了，你有可能会存在一个缺失的问题，这里又不比那种防虫，因为它不是第九步的第一步数据指重会过的，因为你丢了，因为你可能作为可能你根本丢了都不知道自己丢了，对吧？所以说有些时候可能就会有一些我们第三方的数据来对比验证。就你如果做的完善一点，你有完备性的系统的话，在这种情况下，如果是一个 utmost ones QS 的系统里面，你可能就要引入一些第三方的校验工具，是一个验算的这样一个过程。
通常来讲这种功能叫你的consulation，就是说你要比对一下女人以为的这样一个结果，它应该是怎么样的，和你实际的结果它是怎么样的？比对一下这二者之间的差异在哪里？那如果说举个例子好了，从你真实的系统当中就发现产生了 1000 笔数据，对吧？这是我收到的消息，而原始系统应该说，唉，不好意思，我今天发了 1300 笔，那可能中间有 300 米就丢了，对吧？所以这种 atmos 问题，这个系统里面这个引入三方校验，就是这个的 conservation 对比的功能，它是非常重要的，你设计一种系统的这一点你作为架构师一定不能缺，因为前面讲过就是说他 MOS one 是他多了，那数据总会归过来的，你是知道你是有痕迹留下的对不对？如果说是这种 at most ones 的话，这个你就完全是不知道发生过没有，对于这个考虑门状来讲的话，对吧？所以你必须得通过一些第三方式来跳出你。


consumer 则是之外的这么一个程序或者系统，当你做一次对比和校验才知道这二者之间差异在哪里。这种对你来说的话是一个系统的完备性，就功能的完备性角度来讲的话，它必不可少的。这点其实很多什么新手架构师他都没注意到这一点，因为他觉得这个丢了吗？都拿到了一些早，那你想想怎么来做这个早的过程。对啊，你每天出一个report，有这个报告给人家教，他说今天漏了 300 笔，那我们去找一下是哪 300 笔，因为这边发了这么多，这边没发出来，那时候再把嘞没有发成功的三排笔再发一下呗，然后不逐段的这样子分析出哪些丢了哪些没有丢，然后把所有的数据全部对上就好了，对吧？这就是 utmost 这种 QS 下面你系统设计的时候要注意的点，那最后来难度比较高的这样一个东西，业界把它称为 is art ones。


有 act once 什么意思？

[image](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/57d3f0f1-e38c-413b-9a25-c94bb100edca/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466Z6TWIUVI%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T230627Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIG3AAZDjHYFe03ek%2BO8m2H2aJvolj4srmRW7q9jPKP5aAiAD8mBMt1OsazaotjWhws9XAURt74YYAgFVwG9Vl3CPcyqIBAjG%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMbHxLUvkM7BnYShiyKtwDiDhd3S7s%2B1Xdq69mdkxG%2BhQ0aP8ihGm752i4MPc%2Bwnz3WmDmEenLVnoGOlxHqsc03ORfdTneFchfUrphtv4QIWZNTz0wDTviLIFX%2FU4IjlRn19UiL43Mt6cZ7D%2FWbrUxagaahjJk3e7CiokN8yjqggH%2B9PjI3Mh7n3XKoOyFsXAPcZTwX5Bl4ZqzojlER7pty3wy42%2FubFLHuCMrwKuRhARUHZUeB7tdfoKWyVM%2BofG3X7MkLSLeG%2BBh0QG8mHZ5%2Bi7Pm1206m0INS6kpCkxpTNG1MsdJ6H%2BQ8ZGGwPx5HL47v7MqDkW4Rtzti5JT9W2IySSIsDcILmaWtJy4lzg1kc0Ve8x5xMdti8fcjlfGFH2U%2FwIRuqVp2Go34H%2F0GKrl7axnM5DviNJwAYjYVYQGBhKKZ3530A2Qsa2VZDFxBJE1egiRj9WdLMwpMZUs7S5bi1V2e5gxG7dnfmfkfIz8B%2BtXCrFRPUhBfWkH5zfSH8tsUT%2FnSn35IH4C1WmlIaoJOknYaovo9PB%2BZxino0XdtP3JsGNM1cTxTbkA8S56veHKUH0NqmLbyV922AjsVp%2B46hfO%2Bvx%2F1iwEGaTV474rssk3pd%2B7SowK4K050a7C2LNZrjs7mrcwjW7hz8w8rf%2F0gY6pgFK18jsaOXRBZBgDEDZxkbF1NoyDXPAYB3FbUQ9KPAkILdPU7Pk0fZNhP8tHcDm%2FI7eCCdWYIv5Y3iuo0G6803q06yanis9nYeTRmfuKWW1MkXJqqKVqElZ9ju0otyhsT6xRSCmVpBDLI%2Fd2iVgwslcwVgL2qnav0zCoqdW6oFPFexyd%2BTKRtkj%2FxPakowvTWDomwaN%2FvTxiHv%2BODmJ%2Bedr62QUyMZx&X-Amz-Signature=2133c08c4d46ae73fa2fa0a6b5aeab0755608b9e1c88893adae42b57fdd8de46&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

也就是说不多不好，就是你要几次就几次，这个地方你要一次，那就有且仅有一次。说白了就这个意思就是说我作为一个很，比如说我保证你肯定会收到一次，而且只会收到一次，就是你不需要考虑他丢，也不需要他从这种防止或者dipe，这取决于你有多大的决心在造成这个事情。


从我个人的这个经验来讲，能真正做到一个 that ones 的系统是相当之少，总会有各种各大漏洞或者系统的问题或者硬件的问题。你要做那个case， one 是超级复杂的一个系统，所以说这现实的这个实现，或者说你在系统当中来做这种架构的人，你尽量多考虑前面两种。


get one 是一种相对来说在我个人觉得，但这只是一个相对说比较，个人的看法就是相对来说从难度，包括技术上的和这个实际操作层面来说都比较难一点，但是毕竟它是理论上是存在的，什么情况下它都只会有一份。就这个东西其实就是从技术层面回传系统层面都是非常好，但是也非常难的一件事情。比如说不管你是使用现成的中间件，比较Kafka、 IMQ 这种东西，还是你自己从头到尾要实现一个，你要做到一个 exactly once，你想想你要在整体系统分布式的环境下来保证这个东西有且仅有一次发送成功，这个其实是相当困难的。


大家稍微跟我过一下这个场景，好了，我们来这么想哈，比如说，嗯，现在我作为这个生产者，对吧？我发送了一条消息，假如说我们以消息的形态代表这个数据单元发送了一条消息，那突然这个 container 就这个中间件，懂了，那你肯定发送不成功啊？那你怎么能保证这个 R 6万次？这是不是挺难的，对不对？那就表示说当后面这个 control 在写的时候，你这个 control 还得继续往里面发，你一直到发送成功为止，对吧？我们假定现在你发出去了之后，到底发没发成功？这个到了 consumer 端那边，他接没接到这个东西都会导致你后续有没有后续的动作。


因为你有些时候你看这个 exactly once，它不是说只从你这个发出来这个角度来看，它是从发送者到消费者，就生产者在消费者之间统一的来看。比如说你发只发了一份，我稍微只稍微发，而且我处理还成功了，这个才叫应该everyone，这是最好的一种情况，对吧？另外一种就是说我确实发给你了，而且也只发了一次，但是你处理失败了，那是另外一种，对吧？刚才讲的就是什么两头都成功，而且处理也是成功，就发送成功，处理成功，这是最完美的。


次完美的就是说我确实发成功了，而且只发送了一次，而卡莱曼也接到了，但是他处理失败了，这是一种，对吧？这个稍微就有点跟你的实际业务或者实现层面的东西有些关联了。我们再来看，比如说你发送成功了，到了 container 里面，对吧？ container 如果他这个时候崩掉了，那你就怎么办？因为他有可能存成功了，有可能没存成功，你怎么知道他成没成功？是不是得有一种机制来保证？这重看真的，这角度啊，我不仅收到了，而且我还怕存起来了，虽然说我现在崩了，我恢复过来之后我还会继续向这个卡莱姆尔推送或者让卡莱姆尔读取的，所以你就不能操心再发一次了，对不对？所以你要实现这样的一个东西其实是非常困难的，相当于说你就实现了整体系统从producer， consumer 三者之间的一个原子性操作。


你可以想象一下，在一个分布式系统里面要做到一次原子型操作，这个代价可能是相当不一般的。所以说不管从理论知识史来讲，怎么达到一个分布式一致性，因为你这三者都得认为说这一条消息我是收到，却只收到一次，这是一个分布式置信问题，对吧？同时你还保证在这么个点上，它所有的 cap 当中你还得一个取舍，到底在哪个点上出了问题，应该怎么处理？所以说我就说了， exactly once 在现实系统当中你要做到的其实挺困难的，不是说现在没有，而有很多系统都号称自己可以实现 incredibly ones，但是你要真正在系统中，你达到真正的 executive ones 相当困难的，你能达到几个 9 的 exact ones 就非常不错。这一点我们就相当于一个开放性讨论。


总之一句话就是说，你更多的现实当中，你要做好的是 at most ones 或 at least ones 这种情况的应对，相对来说这两者较多一些， connect once 这种相对来说较少一些。至于说你怎么来实现这三者，或者你怎么选哪一种来？在你这个性质中来作为你要采用的一种技术方案，这个取决于你的应用场景。比如说去给你找了前面讲的这个，我要转账，这个在 a 银行和 b 银行之间，这个转账要成功的话，那当然最好是一个 at once，但是为一个 at once，你说这个要跨这么多网络，跨这么多业务范畴，这个太难了。那我们能不能做到这个就是后面的两种的一个，那我们不是又要推来部门，可能是不是 at most ones，对于我们整个体系来看是不是相对来说更合理一些？那就更好做一点。为什么呢？就说 at least once 的话，那如果我转了两笔账要回来，这个反而就困难了，你失败了，我允许你失败，你大不了让用户重新再操作一次，或者你系统层面再重新运算一次，而且银行之间肯定有一个对账的这样一个行为的。


所以说我觉得这种，比如说像银行转账的那种，个人看法，可能是不是 Atmos once 是一个比较好的选择，对吧？另外就是比如像咱们这种，嗯，两个人之间这个消息发送的这种系统，就是比较实现的这种聊天工具，聊这种推送，你发一个推送，那我觉得这种情况下大部分都会选 at least once，为什么？你推送失败的这个可能人家丢了一个消息，这个很麻烦的，对不对？但是你多推几次就人家大不了受打搅一下，对整个用户体验来讲，当然最好是成功一次，对吧？但是你说如果说这个东西我为了保证他一定能主大到我给他多推一下，这个我觉得大部分用户应该都是还是可接受的，因为作为二八原则来讲他所以这个不是特别夸张的一件事情。


而且你不管像咱们这种微信这种东西，你看有些时候你明明其实已经点开那个消息，它可能上面那个推送又会再来一次，这种情况下它肯定是 at least once，就是说我宁可多给你一点，也不少给你一点，这种情况下你就要选 at least once。所以说这里是没有一个定论的。


当然人人都希望 exactly once，但是 exactly once 的从哪个角度来讲，这个成本或者这个系统整体的复杂度都是非常高的，所以说可能你更多的是面临后两者的取舍。所以说你在你的系统中到底选哪一种，结合你的业务场景和哪一个对你来说更重要，你要做出一个选择。关于这三者，就是说 QOS 这三者之间的取舍，我很难给出你一个公式的或者定理，我只能告诉你说，在你的业务场景下，什么东西，什么东西对你来说最重要，那你就按照那种方式去选择一种 QOS 来满足你的这个业务需求。

