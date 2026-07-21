---
title: 2-3  第二代网关组件Gateway介绍
---

# 2-3  第二代网关组件Gateway介绍

[image](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/5b213c9d-10c4-4a27-9220-4fa70c2dee53/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664NFUFNYD%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T225732Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCk9ixlobRwGL%2FmoYdYACrsp2VE55M0TmhsrmLTJTD%2F4wIgEab%2BqKz4popthZILvZ%2B2nLpErFuDyXcajQLHLnBEpc8qiAQIxv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDHjfGEE5otcUvuHvgCrcA%2Fby%2Bndtcw%2Bby3sBASayf6F%2BIOnKTmhlcGYEZXxRqAqfN1o6PSqYgjAR8n8tH1r2TA90jBjmyAulS%2BVa9fqUqaZYRt7JtGUEaSwfSsHSzwEfbb2Vyxe0mnFEc7oyAolfdoFe%2Fbxk%2BtESlhaxMqFvb%2FmLix%2Fw%2FpXGl%2FO4AN9RpsfL4QMiiTndgt9nRYW61NLlYEf8iP6Bdg6QAzFTiR2Vm%2BfHHlhvSR7mWr%2BCQeLny3ZQHh4pTROEiOZPskqD0fnLSdQdcaVAPV2jKJM%2F%2BStvMfwRrEK9hO9MNTiwLL9adayU0gJnGfXMGzQxTvEJPAjcgbu8iYsWtveMfePFPA%2F%2B33O8iNncWY63%2BXBnqt%2BDOVQeimt%2BStY%2BEzS1Jh4SexmgP4W%2BJoDmCVp%2Bv4agyT2ikCvToGomeY7R2%2Ft43G9Io9LGn%2Bjs6LCDp2KSTNdyAAsH%2BC7%2BhZ0ROEo0BKa3kk9m1WdBjhkoChXIQJfzbh0SEbh9hAzeZKPdG5TLE7y4ujoPTlNegWezMEPMBmqdOHuEIw04mcrKbMHy0Tjx4Rv9gid4TJlAKGr3sjsHishffN8KhtcbgA9sT2MU2%2Fgx%2B6GOoSQzEqQp4yGCwyWeYreBtbi9HEO4CkQswTjkHyZ1MNe6%2F9IGOqUBHZ6IOjRESrblTFqUOlM1yMHyBmjrs%2BxphbPiQ62cWJeB9SV%2BBM474092Oxc5fgsUH1a%2BRQ8pYe7qzwTJfBZfAcw%2FfmzjNsRft%2Fv82PqPDQo68H9IABmkCBAxgjE72SsT7xbwZdpOMHdzT3v0ojqyAeL%2B5KZXEJrwbEPzO97z1FyY2gazf0tAmb%2F4fnhRiDvLxhJaqw%2F8jNw9p%2FWzbc7yspjo%2BTHl&X-Amz-Signature=ef423f83cc8e4d242d1ab2a0f91c0f070f41f365405439857362f7c59ba2664c&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

[image](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/1108f250-0812-4a3a-9437-1eb47b294bae/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664NFUFNYD%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T225732Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCk9ixlobRwGL%2FmoYdYACrsp2VE55M0TmhsrmLTJTD%2F4wIgEab%2BqKz4popthZILvZ%2B2nLpErFuDyXcajQLHLnBEpc8qiAQIxv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDHjfGEE5otcUvuHvgCrcA%2Fby%2Bndtcw%2Bby3sBASayf6F%2BIOnKTmhlcGYEZXxRqAqfN1o6PSqYgjAR8n8tH1r2TA90jBjmyAulS%2BVa9fqUqaZYRt7JtGUEaSwfSsHSzwEfbb2Vyxe0mnFEc7oyAolfdoFe%2Fbxk%2BtESlhaxMqFvb%2FmLix%2Fw%2FpXGl%2FO4AN9RpsfL4QMiiTndgt9nRYW61NLlYEf8iP6Bdg6QAzFTiR2Vm%2BfHHlhvSR7mWr%2BCQeLny3ZQHh4pTROEiOZPskqD0fnLSdQdcaVAPV2jKJM%2F%2BStvMfwRrEK9hO9MNTiwLL9adayU0gJnGfXMGzQxTvEJPAjcgbu8iYsWtveMfePFPA%2F%2B33O8iNncWY63%2BXBnqt%2BDOVQeimt%2BStY%2BEzS1Jh4SexmgP4W%2BJoDmCVp%2Bv4agyT2ikCvToGomeY7R2%2Ft43G9Io9LGn%2Bjs6LCDp2KSTNdyAAsH%2BC7%2BhZ0ROEo0BKa3kk9m1WdBjhkoChXIQJfzbh0SEbh9hAzeZKPdG5TLE7y4ujoPTlNegWezMEPMBmqdOHuEIw04mcrKbMHy0Tjx4Rv9gid4TJlAKGr3sjsHishffN8KhtcbgA9sT2MU2%2Fgx%2B6GOoSQzEqQp4yGCwyWeYreBtbi9HEO4CkQswTjkHyZ1MNe6%2F9IGOqUBHZ6IOjRESrblTFqUOlM1yMHyBmjrs%2BxphbPiQ62cWJeB9SV%2BBM474092Oxc5fgsUH1a%2BRQ8pYe7qzwTJfBZfAcw%2FfmzjNsRft%2Fv82PqPDQo68H9IABmkCBAxgjE72SsT7xbwZdpOMHdzT3v0ojqyAeL%2B5KZXEJrwbEPzO97z1FyY2gazf0tAmb%2F4fnhRiDvLxhJaqw%2F8jNw9p%2FWzbc7yspjo%2BTHl&X-Amz-Signature=7de0039a1ad2bd2ab48a220608457c5ef5bf3525d66e20c5d832535886c48f8e&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

hello 慕课网的各位同学们，大家好，在这节当中，我们就跟 spring cloud 中第二代的网关组件 gateway 打一个照面。那我这里为什么要强调第二代网关呢？因为他跟第一代网关 zoo 有一段不得不说的恩怨清仇，究竟是情杀还是仇杀？请收看今晚八点半网关组件 zoo 的不归路。


这个故事的起因，咱先从 gateway 来说起。在深入 gateway 以前，咱要先来看一看这个网二代他身上都有什么标签。我这里总共列出了三个标签，第一个 I 非常熟悉的图标 spring 那网二代 gateway 是目前 spring cloud 官方主推的服务网关组件直接挂牌在 spring cloud 下面更正瞄候。所以对于新的 spring cloud 的应用来说，咱就不必纠结是使用 zoom 还是 gateway 了。选 gateway 没错的，那官方主推也只能说明你出身。好，你可要有点本事我们才能用你。那可不， gateway 也是有那么两把刷子的。为什么呢？因为它的底层是基于 net 构建的，大家对 net 应该都非常熟悉了吧，它是一个高性能的网络通信组件，在网络通信消息传输这个领域不仅又猛又持久，并且快字当头，效率非常非常高。

[image](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/285b0717-6bf2-4707-adfc-26aadb9826d7/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664NFUFNYD%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T225732Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCk9ixlobRwGL%2FmoYdYACrsp2VE55M0TmhsrmLTJTD%2F4wIgEab%2BqKz4popthZILvZ%2B2nLpErFuDyXcajQLHLnBEpc8qiAQIxv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDHjfGEE5otcUvuHvgCrcA%2Fby%2Bndtcw%2Bby3sBASayf6F%2BIOnKTmhlcGYEZXxRqAqfN1o6PSqYgjAR8n8tH1r2TA90jBjmyAulS%2BVa9fqUqaZYRt7JtGUEaSwfSsHSzwEfbb2Vyxe0mnFEc7oyAolfdoFe%2Fbxk%2BtESlhaxMqFvb%2FmLix%2Fw%2FpXGl%2FO4AN9RpsfL4QMiiTndgt9nRYW61NLlYEf8iP6Bdg6QAzFTiR2Vm%2BfHHlhvSR7mWr%2BCQeLny3ZQHh4pTROEiOZPskqD0fnLSdQdcaVAPV2jKJM%2F%2BStvMfwRrEK9hO9MNTiwLL9adayU0gJnGfXMGzQxTvEJPAjcgbu8iYsWtveMfePFPA%2F%2B33O8iNncWY63%2BXBnqt%2BDOVQeimt%2BStY%2BEzS1Jh4SexmgP4W%2BJoDmCVp%2Bv4agyT2ikCvToGomeY7R2%2Ft43G9Io9LGn%2Bjs6LCDp2KSTNdyAAsH%2BC7%2BhZ0ROEo0BKa3kk9m1WdBjhkoChXIQJfzbh0SEbh9hAzeZKPdG5TLE7y4ujoPTlNegWezMEPMBmqdOHuEIw04mcrKbMHy0Tjx4Rv9gid4TJlAKGr3sjsHishffN8KhtcbgA9sT2MU2%2Fgx%2B6GOoSQzEqQp4yGCwyWeYreBtbi9HEO4CkQswTjkHyZ1MNe6%2F9IGOqUBHZ6IOjRESrblTFqUOlM1yMHyBmjrs%2BxphbPiQ62cWJeB9SV%2BBM474092Oxc5fgsUH1a%2BRQ8pYe7qzwTJfBZfAcw%2FfmzjNsRft%2Fv82PqPDQo68H9IABmkCBAxgjE72SsT7xbwZdpOMHdzT3v0ojqyAeL%2B5KZXEJrwbEPzO97z1FyY2gazf0tAmb%2F4fnhRiDvLxhJaqw%2F8jNw9p%2FWzbc7yspjo%2BTHl&X-Amz-Signature=7b4412ee9b7f4ce9ad4ce0b6426c7a9e9c5e4d8dbe30c56c6b367ee1c68d8b62&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

OK 那咱看他的第三个标签是 Netflix 哟怎么打上一个叉了，这就要牵扯出 spring cloud 和 Netflix 之间的一些小恩怨了。咱第一代网关组件邹其实是基于 Netflix 公司的，所以它的开发、维护、升级以及加新功能基本上都依托于 Netflix 公司的开发团队。但是 get way 可不同，就像前面说的，它是直接挂牌于 spring cloud 下面的。也就是说它的主要研发力量是来自于 spring cloud 的开源贡献者，同时也有非常活跃的社区做支持。那为何 spring cloud 抛弃 Netflix 公司研发的 zoom 而选择自己研发一个。


Gateway.不急，这个故事咱稍后再说，不过偷偷跟大家说一下，还不是因为 Netflix 公司不靠谱。 OK 咱给 gateway 说了这么多好话，其实总结起来就八个字，根正苗红，能打胜仗。那咱要看看喽， gateway 都能去打哪些仗？我们这一页就一起看一看 gateway 通常都可以被用作哪些业务场景好。
第一个场景叫路由寻址。

[image](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/574c75ea-e2fa-4300-927e-9da17e6f6982/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664NFUFNYD%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T225732Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCk9ixlobRwGL%2FmoYdYACrsp2VE55M0TmhsrmLTJTD%2F4wIgEab%2BqKz4popthZILvZ%2B2nLpErFuDyXcajQLHLnBEpc8qiAQIxv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDHjfGEE5otcUvuHvgCrcA%2Fby%2Bndtcw%2Bby3sBASayf6F%2BIOnKTmhlcGYEZXxRqAqfN1o6PSqYgjAR8n8tH1r2TA90jBjmyAulS%2BVa9fqUqaZYRt7JtGUEaSwfSsHSzwEfbb2Vyxe0mnFEc7oyAolfdoFe%2Fbxk%2BtESlhaxMqFvb%2FmLix%2Fw%2FpXGl%2FO4AN9RpsfL4QMiiTndgt9nRYW61NLlYEf8iP6Bdg6QAzFTiR2Vm%2BfHHlhvSR7mWr%2BCQeLny3ZQHh4pTROEiOZPskqD0fnLSdQdcaVAPV2jKJM%2F%2BStvMfwRrEK9hO9MNTiwLL9adayU0gJnGfXMGzQxTvEJPAjcgbu8iYsWtveMfePFPA%2F%2B33O8iNncWY63%2BXBnqt%2BDOVQeimt%2BStY%2BEzS1Jh4SexmgP4W%2BJoDmCVp%2Bv4agyT2ikCvToGomeY7R2%2Ft43G9Io9LGn%2Bjs6LCDp2KSTNdyAAsH%2BC7%2BhZ0ROEo0BKa3kk9m1WdBjhkoChXIQJfzbh0SEbh9hAzeZKPdG5TLE7y4ujoPTlNegWezMEPMBmqdOHuEIw04mcrKbMHy0Tjx4Rv9gid4TJlAKGr3sjsHishffN8KhtcbgA9sT2MU2%2Fgx%2B6GOoSQzEqQp4yGCwyWeYreBtbi9HEO4CkQswTjkHyZ1MNe6%2F9IGOqUBHZ6IOjRESrblTFqUOlM1yMHyBmjrs%2BxphbPiQ62cWJeB9SV%2BBM474092Oxc5fgsUH1a%2BRQ8pYe7qzwTJfBZfAcw%2FfmzjNsRft%2Fv82PqPDQo68H9IABmkCBAxgjE72SsT7xbwZdpOMHdzT3v0ojqyAeL%2B5KZXEJrwbEPzO97z1FyY2gazf0tAmb%2F4fnhRiDvLxhJaqw%2F8jNw9p%2FWzbc7yspjo%2BTHl&X-Amz-Signature=f7984768f2352d98133f8246950976b2991f3e1a407a9c4fb5e3e5c5f6efbc3c&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

不过这并不是一个特殊技能了，所有的网关层组件其实都会的，你会我会大家会路由寻址可是网关层组件的主流业务。那么这里就是根据用户来访的请求路径，把它转化成一个内部服务的路径，把用户请求导向到后台正确的服务。那么基于路由寻址以上，我还需要一个功能叫负载均衡。为什么呢？比如说咱后面要调用商品详情页，那一个详情页后面可是连接着几千上万台机器尽管我通过路由寻址功能知道了用户的来访请求，应该被导向商品详情页服务，但是该倒下哪一台呢？这里就必须借助负载均衡策略来指定服务器。


同学们知道是 spring cloud 中哪一个组件给 gateway 提供的负载信号吗？不用我多说，大家应该心里已经有答案了瑞本对不对？ OK 那我们说负载均衡实际上是构建在路由寻址上的一个附加功能。那么除了这两个功能以外，我还有哪些应用场景呢？当然了，限流咱 gateway 作为整个用户调用链路的最上游，它是用户来访请求抵达系统的第一站。所以如果我想对后台服务进行限流在哪里是最合适的？在 gateway 也就是请求发起的第一站，这里来把它限流掉，是不是一种最节省成本的方式因为这个用户请求在网关层就会被丢弃掉了。不像其他客户端限流的方式，还要把这个服务请求下放到具体的接口层，然后再来做限流。所以说网关层做限流效率是非常非常高的。


那除了这三个功能以外，咱还有一个很通用的功能叫什么鉴权，说白了就是权限验证了。其实现在有很多种开源的权限验证方案， gwt 当然是其中的一种机制，还有其他几个大家耳熟能详的名词，比如 OAUTH 还有后面的 OAUTH 2.0，包括 tfa 等等，它都是用户权限鉴定的一种方式。
那么在本章，咱就基于 gwt 技术构建一个最简单的鉴权服务，集成到 gateway 网关组件里面来。那这四个小方框就是主要的业务场景。其中主线任务是谁，也就是 gateway 组建主营业务也是它最重要的业务。那当然是陆游寻址了，对不对？要你 gateway 过来就是来办这件事的。 OK 咱到现在对 gateway 已经做了一些简单的了解。接下来咱就把这个网二代 gateway 和一代目网关 zoo 一起拿出来做一个比较，看看这两个网关层组件技术各自都有什么优点、缺点以及不同之处。


OK 那我们就开始擂台赛的第一回合 gateway 迎战 zoo 我们看到 zoo 这里出场了两位选手，分别是 zoo 1.0 以及 zoo 2.0 版本。那两个 zoo 打一个 gateway 这两个打一个好像看起来不公平。


没准，你这两个还打不过人家一个。咱第一回合先过个招，我们先从靠谱性这一个角度来跟大家分析分析。啊 gateway 自然不用说根正苗红，能打胜仗，它是直接挂牌于 spring cloud 下面由官方支持的 spring cloud 旗舰店出品口碑好，质量靠得住，售后服务也到位。
那么 zoo 在 1.0 时代是曾经靠，不过为什么他可曾经是 spring cloud 中网关组件里的开山始祖，为什么这么说？因为没有其他网关组件的，大家只能用它了。不过 zoo 也是做了一番开天辟地的努力，当然也用实践证明了确实是一款很优秀的组件。但是时代在进步，旧的不去，新的不来，我们总要做一些技术上的改进。这不 zoom 2 点 0 立马就呼之欲出，但是他一直卡在了呼之欲出的这个环节，就是没有出来，愣是硬生生的把自己打造成了专业放鸽子的鸽子王，最后搞的是 spring cloud 的官方也耐不住性子了，索性一不做二不休，直接推出了 gateway 作为自己的第二代网关组件。


大家这下清楚 gateway 的由来了吧。那这首次过招， gateway 就先赢了半招。那咱接下来过第二招了。这可是一招狠招，咱要比 gateway 网关组件的一个核心指标性能。那么 gateway 自然不用多说，它使用了又猛又 19 块字当头的 net 作为底层的组件。


与此同时，千呼万唤使出来的 zoom 2.0 也使用了 net 与之相对的， zoom 1.0 在这一个方面上表现的就有点那么不尽人意，他这里采用的还是一个同步阻塞的模型，因此性能相对会较慢一些。因为 zoom 一点 0 面试的时间较早，所以群众基础也比较广泛。那可能现在很多的 spring cloud 应用也是架构在 1.0 以上的。但是对于新的应用来说，我们能选择 gateway 或者 zoom 2.0 的，那就尽量不要再用 zoom 1.0 了。 OK 那咱在这第二个过招上， gateway 和 zoom 2.0 都略胜半招。

[image](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/0b81ebae-cc8e-484c-b5eb-3677a43fac23/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664NFUFNYD%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T225732Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCk9ixlobRwGL%2FmoYdYACrsp2VE55M0TmhsrmLTJTD%2F4wIgEab%2BqKz4popthZILvZ%2B2nLpErFuDyXcajQLHLnBEpc8qiAQIxv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDHjfGEE5otcUvuHvgCrcA%2Fby%2Bndtcw%2Bby3sBASayf6F%2BIOnKTmhlcGYEZXxRqAqfN1o6PSqYgjAR8n8tH1r2TA90jBjmyAulS%2BVa9fqUqaZYRt7JtGUEaSwfSsHSzwEfbb2Vyxe0mnFEc7oyAolfdoFe%2Fbxk%2BtESlhaxMqFvb%2FmLix%2Fw%2FpXGl%2FO4AN9RpsfL4QMiiTndgt9nRYW61NLlYEf8iP6Bdg6QAzFTiR2Vm%2BfHHlhvSR7mWr%2BCQeLny3ZQHh4pTROEiOZPskqD0fnLSdQdcaVAPV2jKJM%2F%2BStvMfwRrEK9hO9MNTiwLL9adayU0gJnGfXMGzQxTvEJPAjcgbu8iYsWtveMfePFPA%2F%2B33O8iNncWY63%2BXBnqt%2BDOVQeimt%2BStY%2BEzS1Jh4SexmgP4W%2BJoDmCVp%2Bv4agyT2ikCvToGomeY7R2%2Ft43G9Io9LGn%2Bjs6LCDp2KSTNdyAAsH%2BC7%2BhZ0ROEo0BKa3kk9m1WdBjhkoChXIQJfzbh0SEbh9hAzeZKPdG5TLE7y4ujoPTlNegWezMEPMBmqdOHuEIw04mcrKbMHy0Tjx4Rv9gid4TJlAKGr3sjsHishffN8KhtcbgA9sT2MU2%2Fgx%2B6GOoSQzEqQp4yGCwyWeYreBtbi9HEO4CkQswTjkHyZ1MNe6%2F9IGOqUBHZ6IOjRESrblTFqUOlM1yMHyBmjrs%2BxphbPiQ62cWJeB9SV%2BBM474092Oxc5fgsUH1a%2BRQ8pYe7qzwTJfBZfAcw%2FfmzjNsRft%2Fv82PqPDQo68H9IABmkCBAxgjE72SsT7xbwZdpOMHdzT3v0ojqyAeL%2B5KZXEJrwbEPzO97z1FyY2gazf0tAmb%2F4fnhRiDvLxhJaqw%2F8jNw9p%2FWzbc7yspjo%2BTHl&X-Amz-Signature=58bf79763e6395e50fcd53d2dab85c7a4a201fb3fea87578efefc19ded4e2d0a&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

接下来咱过第三招也是一个很重要的性能指标，叫RPS 、 request per second 和 QPS 其实就是一个概念了。在这里我引用了 spring cloud 官方出品的 report 还有民间的一些测试报告。那么在这三个组件当中， gateway 独领风骚，它每秒可以处理大于 32,000 个 requestzoo 1.0 它大概是在 2 万个左右徘徊。 zoo 2.0 相对 1.0 来说有一个比较大的性能提升，把这个上限拓展到了 25,000 左右。但是和 gateway 的 32,000 比还是有很长的距离需要追赶。所以这一招一出， gateway 组件已经是胜券在握。那我们接下来看这第一回合的最后一招。


我们把 spring cloud 寄出来， gateway 是 spring cloud 自己出品的组件，那自然和 spring cloud 已经完美整合起来了。咱们这里说的整合是完全整合到了 spring cloud 官方出品的开源组件库里。那 Zoe 1.0 作为开山始祖也是在 spring cloud 中的一部分。可是 zoo 2.0 因为这个放鸽子行为鸽了 spring cloud 太长的时间，所以只好被 sprint cloud 无情的抛弃了。


不过我们也是可以在 spring cloud 应用中使用做 2.0 的，大家可以看作它是 spring cloud 在外面养了一个小妾，并没有登堂入室，像 gateway zoo 一样光明正大的出入 spring cloud 好，第一回合我们看下来，在这 12344 招上， gateway 都是当之无愧的胜者。
那么我们接下来再来看第二回合，看看 zoo 是不是能扳回颓势。那么接下来咱来到，第二回合只用三招决胜负。

[image](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/269864f0-3e14-4504-b03a-260e5207ac4d/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664NFUFNYD%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T225732Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCk9ixlobRwGL%2FmoYdYACrsp2VE55M0TmhsrmLTJTD%2F4wIgEab%2BqKz4popthZILvZ%2B2nLpErFuDyXcajQLHLnBEpc8qiAQIxv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDHjfGEE5otcUvuHvgCrcA%2Fby%2Bndtcw%2Bby3sBASayf6F%2BIOnKTmhlcGYEZXxRqAqfN1o6PSqYgjAR8n8tH1r2TA90jBjmyAulS%2BVa9fqUqaZYRt7JtGUEaSwfSsHSzwEfbb2Vyxe0mnFEc7oyAolfdoFe%2Fbxk%2BtESlhaxMqFvb%2FmLix%2Fw%2FpXGl%2FO4AN9RpsfL4QMiiTndgt9nRYW61NLlYEf8iP6Bdg6QAzFTiR2Vm%2BfHHlhvSR7mWr%2BCQeLny3ZQHh4pTROEiOZPskqD0fnLSdQdcaVAPV2jKJM%2F%2BStvMfwRrEK9hO9MNTiwLL9adayU0gJnGfXMGzQxTvEJPAjcgbu8iYsWtveMfePFPA%2F%2B33O8iNncWY63%2BXBnqt%2BDOVQeimt%2BStY%2BEzS1Jh4SexmgP4W%2BJoDmCVp%2Bv4agyT2ikCvToGomeY7R2%2Ft43G9Io9LGn%2Bjs6LCDp2KSTNdyAAsH%2BC7%2BhZ0ROEo0BKa3kk9m1WdBjhkoChXIQJfzbh0SEbh9hAzeZKPdG5TLE7y4ujoPTlNegWezMEPMBmqdOHuEIw04mcrKbMHy0Tjx4Rv9gid4TJlAKGr3sjsHishffN8KhtcbgA9sT2MU2%2Fgx%2B6GOoSQzEqQp4yGCwyWeYreBtbi9HEO4CkQswTjkHyZ1MNe6%2F9IGOqUBHZ6IOjRESrblTFqUOlM1yMHyBmjrs%2BxphbPiQ62cWJeB9SV%2BBM474092Oxc5fgsUH1a%2BRQ8pYe7qzwTJfBZfAcw%2FfmzjNsRft%2Fv82PqPDQo68H9IABmkCBAxgjE72SsT7xbwZdpOMHdzT3v0ojqyAeL%2B5KZXEJrwbEPzO97z1FyY2gazf0tAmb%2F4fnhRiDvLxhJaqw%2F8jNw9p%2FWzbc7yspjo%2BTHl&X-Amz-Signature=c926e270058c700811dccdd71b7c551d820616c9cda7110f8387ea9aa0d9a0ba&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

接下来咱过第一招，这一招里咱以长连接论胜负。长连接是咱在通信框架包括 net 等等这些组件中非常常见的一种特性。那么 gateway 做得很好，它支持长连接， zoom 2.0 也不甘落后，同样也是支持长连接的 zoom 1.0，那就掉链子了。长连接是什么？没听说过要不起过，所以他压根就不支持。那在这一回合中，不出意外的又是 gateway 额度 2.0 获得了胜利，那只剩下两回合了，咱看看 Zoe 1.0 有没有机会搬回颓势。


第二招，再从开发的角度来看一下看什么内容呢？那就是编程体验，简单的说它就是上手的难度。从这一个角度来说， gateway 以及入 2.0 的编程模型虽然看起来更加灵活，扩展点也比较丰富，那么有好变而有坏。那么灵活性带来的那么一小点点的代价，就是从编程体验上来说，它的上手程度要稍微难。那么一些 Zoe 1.0 的编程模型相对非常的简单，而且扩展性也就是一个 filter 走天下，所以更加容易简单上手，快速开发。


其实编程体验也并不能说是技术选型的一个重要考量因素。因为对我们技术人员来说，好像还没有听说因为某个组件它太难学习而导致在生产环境上无法应用。对不对，快速学习复杂组件也是一种必备的能力。所以难不怕？只要它够稳定够灵活，然后它的特性足以支撑咱的业务，我们就可以用它再说了，就算你后台代码写得再难，还能难过 high streaks 这个九曲十八弯是跳来跳去的代码实现吗？所以尽管 Zoe 1.0 在这一项过招上面小胜半招，但是好像没有扳回太多优势。


咱看看最后一招这招大招杀招是从哪个维度来考量的？它是从调试和链路追踪的维度来看的。因为咱 gateway 和 zoom 2.0 它的底层是谁？是用的 net 它有很多的异步调用对不对？所以它在链路追踪和我们 debug 之类的调试可能会增加那么一点难度，入 1.0 就不一样了，它完全是一个同步模型，所以在这方面完全是无压力的。不过一句老话说了，叫便宜无好货，好货不便宜，咱们学习一些功能更丰富的组件，自然来说学习成本就会略难那么一些。所以在这一回合，尽管作为 1.0 又小胜了半招，但是从整场比试来看，这最后两招都不是关键的节点。


所以从前面第一回合和第二回合的大 b5 来看，如果让大家选择一个将要在生产环境上使用的网关层组件，每个准话该用哪个？您瞧好了，用 get away 不是 get 是 get away 千万不要用get 。所以在本章的 demo 和后面的电商环节，咱都使用 gateway 来搭建我们的应用。


好讲到这，本节的内容就到这里结束了，那我来跟大家回顾一下。在这一节的开始，我们看了一下王二代 gateway 的特性也就是它的标签。然后我们去了解了 gateway 可以做的功能点，做的业务都有哪些。在后面我们通过两回合的比试，将 gateway 与 zoom 1.0 还有 zoom 2.0 做了一个综合的比较。那么在这三者中决出了冠亚季军，反正大家都有奖牌。那最后得出的结论就是 gateway 才是真正的王者。 OK 到这里本小节就结束了，在接下来的小节里，我们将用图文教程带大家了解一下 gateway 的体系架构，然后用最快的方法跟大家一起动手搭建一个快速落地的 gateway 小 demo 那同学们，我们下一节视频课程再见。



