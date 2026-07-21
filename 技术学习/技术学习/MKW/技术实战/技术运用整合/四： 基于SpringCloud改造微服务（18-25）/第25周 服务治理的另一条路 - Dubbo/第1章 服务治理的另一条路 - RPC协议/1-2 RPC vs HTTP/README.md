---
title: 1-2 RPC vs HTTP
---

# 1-2 RPC vs HTTP

[image](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/0b172d98-ffc3-4c47-99e9-d0e5ad93472f/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UGAHANFS%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T225852Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIA9hn1MI7mCVPU5lw6HyRy4WyGfj7CiqeHg9bR3tZu2ZAiEAiwc11%2FgKG%2FuXs2GkaKLGW%2FL3fa94rXeP3oqHCUIjsNYqiAQIxv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDJxw9sTmRDj4ATmlSCrcAxPRVCnw0x%2F1uT2MQZdHwiB5sMJi%2Fat%2FvVOKgcseuNfmtt8kP%2F8Dt5NY%2B3yXLCH1KIZsiAhvePXbogFQe5RTJTylsPhaQncAVLIQuHHC8c52c8Dy54xEZj3N3CwZBbTgIY6kkqKAFZhRl46c1YWill4mlDVKIm55JemzY07VzdZGNrlHx%2BSx%2BhwtjTr9%2BYDhJ6xjtZyups7yr2vRyUdAd3cxfu3MRn41VLER%2FBp%2FBm2RiKo2IeXGbIJ%2FSBkyrb0DA3sqEiAsw4w01PNCs0JRwftGWVJb%2FgHPxJE18T%2FBPHidS2l4DMZvM8nabpMwCXjzbn9Pfk4nmuFdNjousnHhhQFRrOIAv%2FTICEOCHTtydkEiklAQc9HDTvkrQU8OFDJN6uLq0%2FvAj%2FCOralz6Gjj%2B0Ffkm4aL%2BFXuXWnAjO86C6jkNMSawBHTgYwIyS%2FxZm5x06n2R0PHi36HoFVGH3Beg5Wlfa3pvGZ2joPIM%2BDj3s%2FL6h4cKgVWAsk7PExMKGvoqmv43V8jwBQ%2BcGXJj1UJpo4Dmf6UcSX%2Bdsi10Dq%2BZFJDvh9kPArQveFzM%2FLX3mY1F466f08Ki5ZnbQPaD5PDrv%2BezdAu34crPsETX%2B%2BY3QjqFKcIITEi71G5%2FD5MJ23%2F9IGOqUB7a8i7jxGaz6s9Yc00Fb7YNCqjdZ7z5MCj8Mxvhx1be44RufRDnoNe%2B8JpPc5oIWeNJIurqkn4T4LplruRPcYScHKABna0YKSBy%2FxmC4J2cFi04wrOhS4Zsr7ttu7zxubXzHl84e7tfPYuYfXZZbq3p82i7uXXpgTpgZjkgFicp22N2p3cMhUlZn17ZhfbhESvgXojZQh4DRoML7dunDQJlqCCD86&X-Amz-Signature=4c9ebc97885782da10a03d7a9e0a9d34bde9f1aba9aa5f23b4569cdfa8079ebb&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

[image](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/155a9eb3-f702-4c02-b7a4-41f8985b13d2/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UGAHANFS%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T225852Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIA9hn1MI7mCVPU5lw6HyRy4WyGfj7CiqeHg9bR3tZu2ZAiEAiwc11%2FgKG%2FuXs2GkaKLGW%2FL3fa94rXeP3oqHCUIjsNYqiAQIxv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDJxw9sTmRDj4ATmlSCrcAxPRVCnw0x%2F1uT2MQZdHwiB5sMJi%2Fat%2FvVOKgcseuNfmtt8kP%2F8Dt5NY%2B3yXLCH1KIZsiAhvePXbogFQe5RTJTylsPhaQncAVLIQuHHC8c52c8Dy54xEZj3N3CwZBbTgIY6kkqKAFZhRl46c1YWill4mlDVKIm55JemzY07VzdZGNrlHx%2BSx%2BhwtjTr9%2BYDhJ6xjtZyups7yr2vRyUdAd3cxfu3MRn41VLER%2FBp%2FBm2RiKo2IeXGbIJ%2FSBkyrb0DA3sqEiAsw4w01PNCs0JRwftGWVJb%2FgHPxJE18T%2FBPHidS2l4DMZvM8nabpMwCXjzbn9Pfk4nmuFdNjousnHhhQFRrOIAv%2FTICEOCHTtydkEiklAQc9HDTvkrQU8OFDJN6uLq0%2FvAj%2FCOralz6Gjj%2B0Ffkm4aL%2BFXuXWnAjO86C6jkNMSawBHTgYwIyS%2FxZm5x06n2R0PHi36HoFVGH3Beg5Wlfa3pvGZ2joPIM%2BDj3s%2FL6h4cKgVWAsk7PExMKGvoqmv43V8jwBQ%2BcGXJj1UJpo4Dmf6UcSX%2Bdsi10Dq%2BZFJDvh9kPArQveFzM%2FLX3mY1F466f08Ki5ZnbQPaD5PDrv%2BezdAu34crPsETX%2B%2BY3QjqFKcIITEi71G5%2FD5MJ23%2F9IGOqUB7a8i7jxGaz6s9Yc00Fb7YNCqjdZ7z5MCj8Mxvhx1be44RufRDnoNe%2B8JpPc5oIWeNJIurqkn4T4LplruRPcYScHKABna0YKSBy%2FxmC4J2cFi04wrOhS4Zsr7ttu7zxubXzHl84e7tfPYuYfXZZbq3p82i7uXXpgTpgZjkgFicp22N2p3cMhUlZn17ZhfbhESvgXojZQh4DRoML7dunDQJlqCCD86&X-Amz-Signature=f8a2f6ebeeb18b255f11cd1e3e8250ca958b7bc8ecda7af839f819251d128d90&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

hello 慕课网的各位同学们，大家好，前面咱提到了 double 是一个基于 RPC 协议的框架。可能很多同学们在工作中并没有用过 RPC 也不太清楚 RPC 它的底层和 HTTP 都有什么不同。那咱这一节课程就来把这两者进行一个比较。在这两位选手进行 PK 以前，作为裁判员我们要先来认识一下 RPC 是什么？个冬，咱先来认识一下什么叫 rpcrpc 是叫远程方法调用，但是这三个字母分别是三个单词的缩写，叫 remote procedure 框就是远程方法调用的意思。不同的公司、不同的产品对 RPC 自然也有不同的实现。


那么现如今 RPC 大多是用在哪个领域呢？服务治理领域说到服务治理，大家都很熟悉了，实际上各个技术框架在服务治理领域上面真是万变不离其宗，基本上都是由一个分布式环境中的注册中心来负责新服务的注册、服务续约以及服务下线销毁等等。那在国内市场来说，目前 double 是应用最广泛的 RPC 框架。那在国外的互联网行业同样也有一个 RPC 框架叫做 grpc 它是谷歌出产的 RPC 框架。那老师现在所在的这家公司，它在微服务改造的过程中，技术选型就采用的是 grpc 的方案。那无论选择哪种 RPC 的实现方案，它都有一个共同点，就是要自定义一套 RPC 的协议规范。

[image](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/597513a4-c96d-4b47-b008-136ebf06012f/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UGAHANFS%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T225852Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIA9hn1MI7mCVPU5lw6HyRy4WyGfj7CiqeHg9bR3tZu2ZAiEAiwc11%2FgKG%2FuXs2GkaKLGW%2FL3fa94rXeP3oqHCUIjsNYqiAQIxv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDJxw9sTmRDj4ATmlSCrcAxPRVCnw0x%2F1uT2MQZdHwiB5sMJi%2Fat%2FvVOKgcseuNfmtt8kP%2F8Dt5NY%2B3yXLCH1KIZsiAhvePXbogFQe5RTJTylsPhaQncAVLIQuHHC8c52c8Dy54xEZj3N3CwZBbTgIY6kkqKAFZhRl46c1YWill4mlDVKIm55JemzY07VzdZGNrlHx%2BSx%2BhwtjTr9%2BYDhJ6xjtZyups7yr2vRyUdAd3cxfu3MRn41VLER%2FBp%2FBm2RiKo2IeXGbIJ%2FSBkyrb0DA3sqEiAsw4w01PNCs0JRwftGWVJb%2FgHPxJE18T%2FBPHidS2l4DMZvM8nabpMwCXjzbn9Pfk4nmuFdNjousnHhhQFRrOIAv%2FTICEOCHTtydkEiklAQc9HDTvkrQU8OFDJN6uLq0%2FvAj%2FCOralz6Gjj%2B0Ffkm4aL%2BFXuXWnAjO86C6jkNMSawBHTgYwIyS%2FxZm5x06n2R0PHi36HoFVGH3Beg5Wlfa3pvGZ2joPIM%2BDj3s%2FL6h4cKgVWAsk7PExMKGvoqmv43V8jwBQ%2BcGXJj1UJpo4Dmf6UcSX%2Bdsi10Dq%2BZFJDvh9kPArQveFzM%2FLX3mY1F466f08Ki5ZnbQPaD5PDrv%2BezdAu34crPsETX%2B%2BY3QjqFKcIITEi71G5%2FD5MJ23%2F9IGOqUB7a8i7jxGaz6s9Yc00Fb7YNCqjdZ7z5MCj8Mxvhx1be44RufRDnoNe%2B8JpPc5oIWeNJIurqkn4T4LplruRPcYScHKABna0YKSBy%2FxmC4J2cFi04wrOhS4Zsr7ttu7zxubXzHl84e7tfPYuYfXZZbq3p82i7uXXpgTpgZjkgFicp22N2p3cMhUlZn17ZhfbhESvgXojZQh4DRoML7dunDQJlqCCD86&X-Amz-Signature=04085bfb7e0bbe471c2b766d0e8ae0aa5e68ec3140aeff8027d55757eef2e8e3&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

这其中有两个比较重要的点，分别是方法寻址和对象的反序列化。那方法寻址为什么要把它单独拎出来呢？咱在 eurika 里面有方法寻址这一说吗？大家可以回顾一下，在 eurika 章节咱是基于的 HTTP 的调用。那我们在调用的时候，不管你是直接采用注册的 application name 加路径的形式调用，还是使用 thin client 发起调用。总之我们一定要给定一个已注册的方法名。总之我们一定要给出你需要调用的服务，它的服务名称以及它后面在 UR L 中的路径。但是对于 rp C 协议来说，我们调用其他就真的像调用本地方法一样了，咱既不用给出服务名，也不用给出路径。因此它就需要借助反射等技术获取到你当前调用的服务它的特征量，然后将它运用到自己的方法寻址逻辑上，帮你找到正确的服务提供方。那在这个过程中，你所传输的数据都会经过序列化和反序列化的过程。


那以上几点就是 RPC 框架的大概轮廓了。那接下来我们再通过一个小例子，去体味一下 rp C 和基于 rest 形式的 htd P 接口调用方法之间的不同之处。那我们就从画风这个角度来谈一下两者不同之处。什么叫做画风。那就是接口的命名风格。我们先来看一下 RPC 的画风是什么样子。咱说 RPC 是以动词命名为主的风格。那咱在命名一个方法的时候，如果是说要查询一个商品，那我们给这个方法的名称会命名成 query product 如果把画风切换到 rest 的形式的API ，那这种查询风格就变成了名词形式为主的。比如咱在定义 HTTP 接口的时候，那查询商品的 URL 是一个斜杠加 product 后面再跟他需要查询的参数。而这个动词我们就把它放到了 htd P master 的中来体现。就拿当前这个 product 的访问路径来说，如果它是 get 形式的，那它就是查询，如果是 post put ，那必然是更改。


那删除一个 product 应该怎么样啊？那就要把 HTTP master 改成 delete 这就是两者在接口风格定义上的不同画风了。所以我们讲 RPC 就是在 Java 类中写一个方法名，它更面向于执行的过程。那么 rest 形式的API ，它所面向的重点是所操作的资源，所以它的访问路径所体现出来的是它操作的这个对象。那我们接下来就登上擂台，让 RPC 和 HTTP 在四个回合中比试一番。



好，我们这里列出了 RPC 和 HTTP 两栏。那么他们第一回合，我们先从应用层的协议上来跟大家展示一下，RPC在应用层方面是自己实现的 RPC 协议，不过它底层依赖的依然是咱的 TCP 协议这点和 HTTP 是一样的，它们底层都依赖于 TCP 在稍后的章节里，我将跟大家详细剖析 double 中的 RPC 协议，它的协议组成部分都有哪些。第一回合打个照面，就这样过去了。


咱第二回合呢从编程友好度上面来说道，说道，RPC协议它配置起来相当的简洁高效。如果同学们有使用 hsf 或者 double 的经验来说，那你使用这个框架协议就相当于引用一个接口一样方便。这点非常像 spring cloud 中的 fence 所提供的编程体验。


但是 fen 这里比我们的 RPC 要麻烦很多，你不仅要用专门的 annotation 给这个 fen 指定它的服务名，还要在每个方法上面怎么样写上他的访问路径对不对？那我们再看一下 hddp 的协议，相信大家都用过 spring MVC 对吧？那定义一个访问资源的方法，那我们是不是要先定义一个 controller 然后再定义一个方法，给它指定一个路径，再指定它是 post 还是 get 相当的麻烦。更别说这里面的参数返回值这些的封装。所以咱从编程友好度的角度来说，和易用性的角度 RPC 框架似乎是略胜一筹的。那接下来咱要比拼一些硬功夫了，就是传输效率。在 RPC 协议中咱可以使用 gzip 等压缩技术，非常的简洁高效。而 HTTP 协议咱如果看过它的报文，就知道里面携带的信息非常的丰富，所以它在报文中有效信息的占比相对较少。就是说 HTTP 太婆婆妈妈太啰嗦了，而 BC 简洁高效。


那接下来咱再换一个视角，咱们把自己变身为开源软件的作者，从原作者这个角度来看，实现哪种方案会比较省事呢？我们先讲 HTTP 这底层都是线程的实现，咱只要稍微封装一下就可以了。我们只用把精力花费在这个注册中心，服务发现续约服务剔除这些功能就好了。


那 RPC 可不一样。你要自己实现 RPC 的协议，还有方法寻址等这些逻辑，这都是额外多出来的工作量，它本身的难度肯定还是要比 HTTP 协议要高出那么个层次的。但是话说回来，这个好像跟咱没什么关系。不管你实现起来有多难，只要让我们开发人员用着爽就可以了吗？那从以上几点来考虑，似乎 RPC 协议更胜一筹对不对？不管是从易用性来说，还是从通信的效率来说，它都要比 HTTP 的方案稍微高效一点。问题来了，既然 RPC 有这么多的优点，那为何前面还让我们学 spring cloud 还有尤瑞卡呢？直接用 double 不就一了百了了吗？其实 RPC 再好，就是一个服务治理框架，你有网关层 gateway 吗？你有分布式配置中心吗？你有 bus 推送服务吗？你有 solution 追踪链吗？你有 sentinel 限流哨兵吗？你有日本的负载均衡吗？负载均衡好像 double 还真的有。


那除了这个以外，大部分咱 spring cloud 提供的全家桶组件的功能， RPC 框架里好像都没有。所以说，如果你的目标是搭建一套微服务应用的全链路系统。那么选择 spring cloud 绝对是首选。那如果你已经有了一个成熟应用，只不过想替换一个服务治理框架的解决方案，那考虑 double 也是一个不错的选择。 OK 同学们，那这一节的内容到这里就结束了，我们在接下来的小节将深入 double 跟大家介绍 double 的架构设计以及核心功能。 OK 同学们，那我们下一小节再见。





