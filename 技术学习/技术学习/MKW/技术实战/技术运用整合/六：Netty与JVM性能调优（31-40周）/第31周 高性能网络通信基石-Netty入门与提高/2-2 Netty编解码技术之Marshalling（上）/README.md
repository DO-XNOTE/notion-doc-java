---
title: 2-2 Netty编解码技术之Marshalling（上）
---

# 2-2 Netty编解码技术之Marshalling（上）

[image](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/4f3ae476-2159-4c06-9e9e-7eab8850c3c9/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665AXUELPE%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T230008Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCeiL8JXn9YJgwbh9F7gzL7U8UDHPfkgjXTTlFE9IJTZwIhAIcosaTXt9UmWaNFwEUAGKWvY1tSAc8fcoiXV6jR3EqiKogECMb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1Igxe31k6h5ZUQJAExwIq3APiy6U%2F6i6CSg9scSzWXyirjtq%2Fntulq9U2YLXwsZ0Y0hdz%2FIXTRSpnckpJHvX3SYDfLQr8431ADJy7ZtC0ZNtT9kx8pAjXUkQTxCeP7kgxGlKH0Kdf8cApsDOeYubanbxPUPo2kI8hmm7CoP14cIPQvD0X4l5hpXneGg%2Brd3OdVVT0FfEVy5h%2BG9H%2FEmJfx0a4poNB%2FvaIdofplDcJYJIgV05eG%2FHOH9rXX9iklD8XlceCwGQuBhFZoWQEtzYNaW2ttZtlJrd0M00TCp5UbtZ1thh%2BpGdLjm5K2utRsZGTnTe5%2BsZoii%2BigKR5WE%2FUHpPR76bazWLHohiSsOJMZf9IYKntGW%2BVVWKeF7JCEVqQW264gc%2FZ9TvGWnkVzfotC4gKAPTuf6fZeLyF1dLviW7De4bMMVgVHKK8kxXW8dDfZqRGevFeIMJAOunEfJ%2BA7ZRITOGHEmyRyVDyjv3wpqjpY50gMfC7%2F9HDgp6puSbIGY%2BPIG1bA2jcntUZhCDy%2FdsllZjqgY%2F8mir42n2pssFJW77juaweOMt%2BRar%2FSKRVDg8syjL21NGlgk5fA77pitE%2Bx7wn%2FAfVY3klv0CW3mXDw3RDPpJSK%2FbPOG2WD9QuDCZ4qPwOqFGd%2Fnu9YjCkt%2F%2FSBjqkAUxpnCTCvCU7rNO%2FSlOi%2Fh3ECyWfW9%2FEJo3wI%2FcmcvlPApRsw4WgH1T66Vat7qrKZBszdBhy3ZL%2FVelwW%2F82JoiXlHLwy9E3pb1LywjyCxRCve4SYfnVOtaqRT8vRodUo2laJWlghmxalBj6UkJvfmqKpmncbWMaPcxAG9tJsWLGlhY3XpgeHKqk4gGEuLQihcrcgeQPA%2BFvkTDo6DOFiCqTc6l2&X-Amz-Signature=59a8dbe9e4d9d01a2277fb17e275e9f62e5ab02eb8c63ec958275faba22c39b0&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

[image](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/dee2a02c-3e31-4322-89f4-51878150f1c1/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665AXUELPE%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T230008Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCeiL8JXn9YJgwbh9F7gzL7U8UDHPfkgjXTTlFE9IJTZwIhAIcosaTXt9UmWaNFwEUAGKWvY1tSAc8fcoiXV6jR3EqiKogECMb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1Igxe31k6h5ZUQJAExwIq3APiy6U%2F6i6CSg9scSzWXyirjtq%2Fntulq9U2YLXwsZ0Y0hdz%2FIXTRSpnckpJHvX3SYDfLQr8431ADJy7ZtC0ZNtT9kx8pAjXUkQTxCeP7kgxGlKH0Kdf8cApsDOeYubanbxPUPo2kI8hmm7CoP14cIPQvD0X4l5hpXneGg%2Brd3OdVVT0FfEVy5h%2BG9H%2FEmJfx0a4poNB%2FvaIdofplDcJYJIgV05eG%2FHOH9rXX9iklD8XlceCwGQuBhFZoWQEtzYNaW2ttZtlJrd0M00TCp5UbtZ1thh%2BpGdLjm5K2utRsZGTnTe5%2BsZoii%2BigKR5WE%2FUHpPR76bazWLHohiSsOJMZf9IYKntGW%2BVVWKeF7JCEVqQW264gc%2FZ9TvGWnkVzfotC4gKAPTuf6fZeLyF1dLviW7De4bMMVgVHKK8kxXW8dDfZqRGevFeIMJAOunEfJ%2BA7ZRITOGHEmyRyVDyjv3wpqjpY50gMfC7%2F9HDgp6puSbIGY%2BPIG1bA2jcntUZhCDy%2FdsllZjqgY%2F8mir42n2pssFJW77juaweOMt%2BRar%2FSKRVDg8syjL21NGlgk5fA77pitE%2Bx7wn%2FAfVY3klv0CW3mXDw3RDPpJSK%2FbPOG2WD9QuDCZ4qPwOqFGd%2Fnu9YjCkt%2F%2FSBjqkAUxpnCTCvCU7rNO%2FSlOi%2Fh3ECyWfW9%2FEJo3wI%2FcmcvlPApRsw4WgH1T66Vat7qrKZBszdBhy3ZL%2FVelwW%2F82JoiXlHLwy9E3pb1LywjyCxRCve4SYfnVOtaqRT8vRodUo2laJWlghmxalBj6UkJvfmqKpmncbWMaPcxAG9tJsWLGlhY3XpgeHKqk4gGEuLQihcrcgeQPA%2BFvkTDo6DOFiCqTc6l2&X-Amz-Signature=e7b38aa2e517541a66828224788dc680a55e2dbddbace12273e006bf19fa552d&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

OK 小伙伴们大家好，这节课我们开始进入 net 的编解码技术。首先我们来学习这 BOSS 的玛莎琳应该怎么去实际的应用。首先我们要使用 g boss 的玛莎令，所以我们在 Pom 包下，我们应该引入对应的它的依赖包。在这里老师用的是 1. 3 点x，就是比较老的包哈，所以大家也可以用比较新的，也可以没有什么问题。

[image](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/899e3717-3ced-4758-9289-776d573f5f2e/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665AXUELPE%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T230008Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCeiL8JXn9YJgwbh9F7gzL7U8UDHPfkgjXTTlFE9IJTZwIhAIcosaTXt9UmWaNFwEUAGKWvY1tSAc8fcoiXV6jR3EqiKogECMb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1Igxe31k6h5ZUQJAExwIq3APiy6U%2F6i6CSg9scSzWXyirjtq%2Fntulq9U2YLXwsZ0Y0hdz%2FIXTRSpnckpJHvX3SYDfLQr8431ADJy7ZtC0ZNtT9kx8pAjXUkQTxCeP7kgxGlKH0Kdf8cApsDOeYubanbxPUPo2kI8hmm7CoP14cIPQvD0X4l5hpXneGg%2Brd3OdVVT0FfEVy5h%2BG9H%2FEmJfx0a4poNB%2FvaIdofplDcJYJIgV05eG%2FHOH9rXX9iklD8XlceCwGQuBhFZoWQEtzYNaW2ttZtlJrd0M00TCp5UbtZ1thh%2BpGdLjm5K2utRsZGTnTe5%2BsZoii%2BigKR5WE%2FUHpPR76bazWLHohiSsOJMZf9IYKntGW%2BVVWKeF7JCEVqQW264gc%2FZ9TvGWnkVzfotC4gKAPTuf6fZeLyF1dLviW7De4bMMVgVHKK8kxXW8dDfZqRGevFeIMJAOunEfJ%2BA7ZRITOGHEmyRyVDyjv3wpqjpY50gMfC7%2F9HDgp6puSbIGY%2BPIG1bA2jcntUZhCDy%2FdsllZjqgY%2F8mir42n2pssFJW77juaweOMt%2BRar%2FSKRVDg8syjL21NGlgk5fA77pitE%2Bx7wn%2FAfVY3klv0CW3mXDw3RDPpJSK%2FbPOG2WD9QuDCZ4qPwOqFGd%2Fnu9YjCkt%2F%2FSBjqkAUxpnCTCvCU7rNO%2FSlOi%2Fh3ECyWfW9%2FEJo3wI%2FcmcvlPApRsw4WgH1T66Vat7qrKZBszdBhy3ZL%2FVelwW%2F82JoiXlHLwy9E3pb1LywjyCxRCve4SYfnVOtaqRT8vRodUo2laJWlghmxalBj6UkJvfmqKpmncbWMaPcxAG9tJsWLGlhY3XpgeHKqk4gGEuLQihcrcgeQPA%2BFvkTDo6DOFiCqTc6l2&X-Amz-Signature=f8f940e84c686a686d3bd446c310418be5a7e5604813ae9bcef9523800980e9d&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

g boss 的marshling。 OK 引完了包之后，我们其实就可以进行真正的编码了哈。在这里老师花一点时间，我们一起从 0 开始把整个的 marshmalning 框架，其实也帮助小伙伴们。对于 Netty 不是很熟的小伙伴们来梳理一下，从头到尾进行一个编码。好了，首先我们新建一个package，叫做 come 点 B F X Y，第二， ninety 第二，我们的 marshling OK 我们再进入编码。


首先我们来想一想我们现在要做什么事情。我们现在要做这种数据的一个传输，说白了用到 g boss 玛莎令，让他帮我们去做一个序列化的这么一件事情。我们现在首先应该想一下我们数据都要传输。什么样的对象，我们其实可以去自己去定义一下。好了，我们在这里比如当我的 client 端发出去的时候，我定义一个 Java 的对象，因为为什么说我们要定义一个 Java 的对象？因为其实 boss selling 其实是对 Java 的。这种 object 的支持是非常好的。我们可以简单写一个叫做 request date， request data okay。对于 request data，我们 client 端发送数据的时候，我们采用数据包。假设我们 server 端往回响应给克兰端的时候，我们可以具体写一个叫做 response data OK 所以在这里我也把 response 这个类也定义出来。


Data。好了，我们发送以及回送响应都有了。接下来我们要做什么事情？首先你想要用 g BOSS 的玛莎铃，除了引包之外还不够，还需要加入它的一个叫做 code c factory。说白了，对应的我们的这种序列化无非就是 encoder 和 decoder 的过程。所以在这里老师把之前写好了的这种模板形式的这种叫做 Marshall in code see factory。直接粘过来就好了哈，我们修改一下包名，直接粘过来好了。这个类是老师之前写的，比较早了，我们一起来看一看这是在做什么事情。


首先它是一个 final class，既是官网的demo，我们可以看一下。 final class 叫做 mastarling code c factory。这里边主要有两个静态的类，一个是用于 decoder 解码，还有一个是用于 encoder 编码的。具体编解码的逻辑是什么？我们来看一看。


首先从它的解码开始。首先它第一个要通过玛莎琳工具类它的方法去获取 marshling 实例对象，对吧？因为你要用它，所以你要把它 new 出来，就是marshling。点 get provided marshling factory。这里边都是固定的，要传 serializable 序列化的它。返回一个 factory 之后，第二件事情就是创建它的configuration。我们把它 new 出来，给它 set 第五个版本就可以了。


接下来安玛沙令。这安玛沙令 provider 这是干什么？是根据我们的 factory 和 config 去创建一个服务的提供者，可以去理解。它就用于帮我们做解码的provider，叫 default m macarling provider。在这里边把 factory 跟 config 都装进去。


最后一步骤，有了 provider 以后，我们去创建它的decoder，也就是它的解码器OK。解码器很明显就直接 new 一个 marshling decoder 传进去我们的provider。后面两个参数就是我们在序列化的时候最大的序列化的字节是多大。在这里老师写了 1024 乘以1024， OK 也就是 1 兆。我们返回我们的解码器对象，就是我们的decoder。接下来看我们的 build Mar 夏令encoder。我们的编码器也是同样的道理，直接通过什么，通过我们的 factory 以及 config 去把我们的 default Mar 夏令 provider 去实例化出来，然后传进去这两个参数。用我们的 provider 对象直接 new 一个 macarling encoder，把 provider 放进去。最后返回我们的 macarling encoder，就是编解码器对象都创建出来就可以了。


我们有了编解码器对象，其实很简单，跟我们之前去学习分隔符解决 TCP 拆包联包问题一样，我们把对应的地方去放编解码对象就可以了，在我们的 channel init channel 里边。好了，基本上我们搞定这件事情之后，接下来还别忘了我们的数据传输对象。虽然你现在不用 Java 的这种序列化的方式，但是 g boss 玛莎铃，它必须你要去实现你自己要传输的 Java 对象。一定要实现 Siri elizable 接口，这是规定死的。所以我们一定千万要记得两个类都需要实现 Siri elizable 接口。


有了 Siri 莱斯不接口之后，接下来我们进行实际的填写。比如我编码，我请求过去的时候，哈，在这里老师打注释，我们请求过去的时候，请求过去的时候，我们请求对象。我们直接可以这样去写请求对象就是我们的 request data 都有哪些属性，比如最简单的我们一个一个去列出来。比如最简单的就是我们的 private string ID，可以吧，我们的 private stream，我们的 name 可以。比如我的请求消息是什么，对不对？我们的 private string，咱们给它起一个名字，也是 string 的哈，叫做 request message。
好，可以。比如我想去传一些，现在我们看到的就是一些普通的类型的对象。比如我们想传一个数组，传一个字节数组。比如我有一个文件，或者有一张图片，想去在网络上传输，我们可以去写一个叫做附件attachment。好了，现在是有一个附件也想上去传，所以搞一个attachment。出来。这 4 个属性就是我们客户端发给服务器端的内容了。


OK 最后一定要实现对应的 gas 赛方法。在这里李老师直接是好了，我们继续。刚才我按快捷键，它有一个冲突，跟我的企业微信。好了，接下来我已经把对应的概赛方法都生成完了。这是我们 request data，对应着我们也可以有 response data。当然这里边有一个序列化，我们生成一个 January 一个default，它的 Serolevel version UID 就好了，无所谓。接下来我们继续来看一看对应的响应信息。我们来添一些响应信息都有哪些内容，我们可以随便去写几个简单的哈，比如它同理也有 ID 和name，我们来加上private，我们的 stream ID， private 我们的 string name，对吧？可以，以及我们的private。在这里面我们叫做 response body，或者叫 response message，哈， response message 我们对应着把它也生成 get set 方法。当然这是一个 string 类型的，好搞定。紧接着我们也是千万不要忘了，哈。当然这个可有可无了，就为了他不给我们去有警告的提示。 OK 现在我们已经把对应的请求跟响应的数据已经搞定了。接下来事情很简单了，无外乎我们的 Nike 的这种编程模型。


net 编程模型。我建议大家，其实在刚开始的时候，你应该从服务端，也就是 server 端开始去写代码。为什么这么说？因为 server 端它可能怎么说，跟我们最开始写原生的 IO socket 的时候，也是先从服务端去编码，再去写 client 端。哈， OK 好，我们现在先去从服务端开始写，我们就叫一个简单的server，这个过程其实就是对于一些 Nike 不太熟悉的小伙伴一个巩固加深的过程。所以我期望其实你可以跟老师一起去敲代码。


首先我们要有两个 event loop group，对吧？在这里其实有同学说老师， event loop group 是什么东西？它你可以认为是两个线程组，我们在这里叫做 b group both group，等于 new NIO event loop group。好。一般来讲，我们 boost group 我们都可以设置成1，表示什么？因为我们其实 Nike 它是一个 reactor version，就是我们的 boost group，其实就一个就可以了。我的 worker group，它其实有很多。当然我们如果不去写，它默认就是我们的workgroup，默认是我们的当前的 runtime 点。 arrival 就是我们的CPU。当前服务器电脑的是一个CPU，合数乘以2。有兴趣可以看一看它底层的代码。这个东西 Nike 底层代码其实不是很难，它其实很简单。我们来看一下当前简单跟一下，因为我们毕竟不是一个源码课程，是一个实战类相关的一些课程。我们点进去这里边它调 diss 0，什么意思？就是你不给我传参数，我默认是 0 点到 this thread 嘶，肯定是 0 个。再往下点之后，它其实调用链是比较长的，这里边有一个this，哈。这里边有一个executor。这个 executor 就是一个线程池。可以这么去理解。


后面还有一个参数叫做 selector provider，哈，这是什么意思？其实我们的 selector 选择器，它的 provider 什么意思？就提供者选择器的提供者。说白了你可以这么去理解，调用 provider 方法就是它能够把选择器的提供者去实例化出来。你可以这么去理解这个有什么用？其实是在我们做 n l event loop，在做初始化的时候，会去用到我们的provider，会去用到我们的selector。


其实说白了是一个 NIO 的模型，我们不断的去轮询，注册到我们线程上的一些 IO 的操作事件，对吧？所以它就是一个提供者，它是一个单例模式。有了提供者之后，我通过提供者可以去 open selector 打开一个的selector，登录复用器。在这里边代码其实没必要领着小伙伴们看了，点进去大概看一眼也可以。我们会看到它里边是加锁的方式。 if 如果 provider 等于空，不等于空，直接返回，也就是肯定是一个单例的方式了。如果等于空，它通过几种机制去帮我去把它创建出来。比如叫做 load provider from practice。
从系统参数系统变量上，如果你配了，我可以帮你返回，对吧？这个是不是它就是 Java 点 n a o，点channel，点 s p i，点 selector provider。你如果配了这个参数，它可以去帮你去 class loader，帮你去 new instance，这很简单对吧？如果你说诶，你没有，但是你说你 as server as service 方式，这种方式其实也是 s p i 了，我们点进去看一下这种一个 select provider，你会看到什么？你看到 service loader，它就是一个 s p i 对吧？只要我实现接口下面的实现类，它会帮我去遍历出来。编制出来说无限去遍历还是next，只要有 next 直接返回true。 OK 这是 s p i 的方式。这种方式可能就是比较底层了，是 send 点 n i o 点 c h 加default， select provider 加 create 就是它。


其实 create 方法我印象没错，它其实也有很多不同的实现，比如这个是太底层了哈。这个里边它应该是根据不同的操作系统。如果你是 windows 操作系统，可能会有一个叫做 windows selector。我 control T1 下，当然我在这里我点不到哈。如果你是 Linux 对应的，会有 Linux 所对应的selector，就是根据不同的操作系统返回provider，这个 provider 就是我们的 selector 它的提供者。去说回过头来，顺带着就领着大家看一眼。你自己在学习的时候也应该经常的去翻翻源码来看一看。


再往下走还是点this，这里边又多了一个 default selector city factory，哈。一个策略就是我们的 selector 它的策略工厂。你还要往里点。到这儿叫做 n i o event loop group，它会调父类，它的父类是谁？就是 n i o event loop group 它的父类。我们点进去，它的父类叫做 multi thread event loop group。在这里边你就能看到具体的逻辑了，它说如果 n thread 等于0，我就直接变成叫做 default event loop thread default。你可以看到它在静态初始化代码块的时候，它对它进行一个赋值，就是当前我们的什么我们的 net runtime 点 arrival processor 乘2，对吧也。这是默认的一个结果集，默认的一个结果。但如果这也是为什么我们正常你看到代码，一般来讲它 boost group 都会写一对。不对，我们的 work group 它可以不写哈，默认我们的 CPU 合数乘2。 OK 这很简单哈，没什么可说的。


再往下看。其实如果感兴趣的小伙伴，你可以去再往下去跟1，跟他的代码对吧？他做完这个事情之后，比如我们刚才跟到了这里，是不是你可以再去跟super，再往下点是不是诶，这又一个类叫做 munity slide executor group。再往里边点看一看到逻辑。你看这个逻辑是干什么逻辑？你可以理解为它在真正的去初始化我们的 n i o event loop group 的模型，其实就是在初始化我们的 reactor 模型。当然还没有去运行reactor。 OK 简单来看一看。这里边有一个children，哈，这个 children 它就是一个 event executor。
event executor 是一个比较上层的接口，我们可以看到 children 它定义的是一个 event executor，一个数组，也就是其实我们的这种 group 就是 NIO event group，它其实是一个数组的这种模式，哈，你可以看到它是最上层的 event group。再往下有各种各样的实现，比如 EPOL 的这种 event group，还有我们经常会用到的这种 n i o event loop，对不对？各种各样的 event loop。 Event loop。它其实还有一个上级类叫做 single thread event loop，这个是一个比较核心的。再往上看，还有一个叫做 single thread event executor， OK 再往上看，还有一个叫做 abstract scheduler scheduler event executor。说白了什么意思？我们的 event group，其实它可能是一个带有丢失任务性质的一种叫做 event loop，对不对？带有定时任务性质的一种叫做事件的executor。
其实我们在去学习的时候，尤其是在去读源码边学习边读源码端边了解它的时候，你一定要尝试着自己去跟一跟代码，尤其你要尝试着去看一看它的整体的层次、结构和设计，这样后面你再去学习还是使用还是读源码，都会非常非常有帮助。 OK 我们废话不多说哈。我回过头来你看这里边无非就是什么。这里面做一个非法的参数的校验，如果 executor 等于空，它 new 出来一个叫做 thread pre task executor，它 new 出来了一个executor。这个 executor 说白了就是我们真正 event loop 要做的线程池的里面的线程的一个东西了。他去初始化， children four 循环着去 new child 初始化。在这里边有一个叫做什么叫做 trucer factory，点 new trucer 就是一个线程选择器。说白了，我们当前一个线程过来，我们 event loop group，我们让谁去对线程进行一个一对一绑定。监听的就是让哪个线程去对去服务于你接入过来的请求。就是这么一个意思。性能显示器它好像有两种实现，一种是这种，你可以看一下它有两种实现，一种是。


Power of 2 event executor truth.
还有一种是 generate event executor chooser 什么意思？ power of two 就是 2 的幂的这么一个算法。很简单，它就是为了去做一个取余的操作，单个语的操作，这样有助于提升我们计算机去做语操作的时候，性能会非常好。如果不是取语操作的时候，它可能就是正常的这种 index 去取模的方式了。这些代码都比较简单，老师在这里就不详细去说了。我们其实还是回来我们是一个实战的课程，所以我们快速的去往下写代码。


接下来我们要做什么？我们现在是服务器端，服务器端肯定会有一个叫做 server boost trap 对不对？ server boost trap 是各类找到 server boost trap，我们叫做 s b。OK，我们 new 出来 server boost trap，我们有了 boost trap。这个 boost trap 是干什么？它说白了你可以理解为是一个链式调用的这么一个组织。它其实你可以认为是一个 builder 建造者模式，可以点进去，比较类似于builder。它继承自 abstract bootstrap。当然 abstract bookstrap。


无论是我们的 boost trap 还是 server boost trap，都是有一个父类的。这个父类又做了什么？其实小伙伴们你可以去关注一下代码就好了，你看到它这里边都是这种链式编程 return this 对吧？最后调完了之后，最后一步其实就是调我们的 check handler，就不往下去看了哈。小伙伴们感兴趣可以看一看。


我们在这里快速回到代码。有了 server boost trap 之后，我们用 server boost top 去点group。首先第一个 group 是非常关键的，它的主要的目的就是把我们的 boss event loop group 和我们的 worker 去做一个配置。做这个配置其实已经形成了一个 reactor 这么一种父子线程组的一个关系。然后就是我们的channel，现在我们用的 channel 肯定是 NIO server socket channel 对吧？第二 class 紧接着，其实它套路都是一样的， option 配置一些选项。比如在这里我们配一下日志，他 net 有一个日志的logger，我们叫做option。我们点日志不是 option 里的，我们配一个比较关键的属性，叫做 so backlog。这也是我们真正的比较底层的一个概念了，你的 TCP 真正建立握手进行s， y n c 队列跟 accept 队列之和就等于 so backlog。当你的一瞬间接收的请求排队列的大小这个数。
其实我们讲到这儿了之后，我们暂时先停一下。关于是不是它底层采用什么机制？其实你看到这个类，它能把这个类去映射成一个对象。它这块儿肯定是一个反射的方式。你看叫做 reflective channel factory，是不是根据你传进来的class，我通过反射去给 new 出来调用 channel factory，这里面就是一个反射的逻辑。其实你可以点进去看一看，对吧？ this are class 返回的就是我们的class。
我们再往下看，继续往下说 option 加一个handler，它应该是加我们的，叫做chair。因为我们是 server 端，所以我们要加一个 chair handler。在 chair handler 里面，我们去 new 出来。我们很经典的类就是我们的 channel init leather。我可能现在写代码比较慢，因为什么原因？是因为老师换电脑了，所以键盘还是不太熟悉哈，所以超代码稍微有一点慢。小伙伴们体谅。我们现在用的是我们的正常的 native channel，把它的该实现的方法实现结束。新的笔记本可能打字起来比较费劲，因为它的建成非常短。


Ok， s c。第二渠道 pipeline 其实就是我们的一个怎么说管道，或者是它可以去加一堆的，比如 add last，它底层是一种这种双线链表。 at last 我们都要加什么东西？首先我们肯定要加自己的服务，我们 new 一个 server handler 出来，这肯定是可以的对不对？加我们自己的一个 server handler。 OK 搞定了这件事情之后，我们把它去 create 出来。 create 出来我们的 server handler，我们就放到玛莎琳下面就可以了。我们去finish，有了它，你看它帮你去implements。这个类就是非常非常的上层。所以我们只需要使用那种叫做继承的方式就可以了。我们暂时不需要这些东西，我们只需要继承一个类。


exist 我们的 channel inbound inbound 是我们对应的读入的意思。 adapter 还有什么outbound？哈，我们只需要关注一个方法就可以了，叫做 public void channel read。这个方法里边有两个参数对吧？第一个参数就是我们的c，t，x，就是我们的 channel handler context 对象，都是非常熟悉的 channel handler context 对象c，t，x。


还有一个就是我们实际的 buffer message，我们可以用 object 去定义一下，它默认其实是往出 throw exception 的。哈，诶，不是。你看有一个叫做 over wraps 对不对，就证明我们这个方法写对了。好，没有问题。


OK 现在我们自己定义的 server handler 已经搞定了，接下来干什么？回过头来，我们刚才其实已经对于 g boss 玛莎令 factory 工厂已经搞定了，无非就是调用它的 encode 跟 decode 方法添加到我们的 paper line 上。注意你一定要添加到你的实际的业务方法之前才可以哈。你要放到之后可能就解析不了了。所以因为它是一个链式的。你可以认为它就是一个责任链的模式。后面有兴趣我们可以看一看。所以你一定要按照顺序去add，因为它是一个责任链模式哈。我们 machanlings could see factory 点decoder，是不是 build decoder 加完了之后，我们再来一个 encoder 就好了。


搞定。最后是实现我们自己的什么？实现我们自己的业务逻辑 handler 好了，就这么一个非常简单的事情。现在我们整个模型基本上写完了。我们直接干什么？我们直接调用我们自己的 serve a boost shop，让他去对端口进行绑定。什么？比如绑定一个8765，绑定一个端口进行同步的一个 single 阻塞，对吧？它最终会返回一个。当然它会抛异常。我们在这里就直接往出 throws 可以了，因为是一个 demo 级别的小应用。绑定完了之后，它会调用 single s y n c 方法，它会给我返回一个 channel future。我们通过 channel future，其实拿到 channel future 就可以去对它去发真正的消息了，就可以去做了。当然这是我们 sorrow 端的 channel future，它不需要发消息，对吧？好，最后我们来同步的去阻塞它。


第二 channel 获取到 channel 之后，然后第二 close future，第二同步去监听连接关闭。关闭之后，我们把我们两个资源都去 shut down 释放掉。优雅的释放。哈，我们的第二个资源，优雅的释放 12 道。


好了，我们的代码就写完了。有同学说老师这个绑定其实就相当于一个契机。我不知道小伙伴们能不能理解。老师的意思，就是我们的代码开始去做初始化的逻辑对不对？我们的 event loop group，它是一个非常核心的概念。 server boost trap 就是我们的 abstract boost trap，也是一个非常核心的概念，以及它的一些配置项。我们通过这种责任链这种方式，去把可以认为是一种双向链表的方式，把我们自己的业务处理都加到我们的 Paperline 上。你可以这么去理解，这些其实都是一个初始化准备的工作，什么时候我们的应用程序真正起来了起来，肯定绑定的方法才真正是把我们应用程序起来了。所以小伙伴们，你一定要去好好去研究一下我们 Nike 整个的这几个比较关键的步骤。在这里老师也简单跟大家来带带着。


读一读绑定里边的代码，到底它是做什么事情。我们点击绑定哈，你会发现它会进入 abstract boost trap 类里边调绑定方法。绑定方法里边传一个 a net socket address，就是我们真正的把我们的 Java 的点 net 包下的 socket address 这个类就搞出来了。端口号传出来，这没什么可说的对吧。绑定这里边去做validate，如果没问题，你的地址没问题，或者对应的验证都通过了。他会调度 bound 的方法。杜邦的方法，他把我们的 i net socket throw address 对象传进来了。 do 棒的方法里边他都做了什么事情？其实代码就比较长了，简单解释一下。他最开始做的事情就是 init 初始化和注册。说白了，把你自己的一个端口，你给我传过来的 8765 端口，以及它的一些信息都做一个初始化和一个注册给谁注册给我们的模型。你可以认为注册给我们的整个的 react 模型，或者注册给我们的 event loop 献丑。接下来它会返回一个 channel future，去返回一个channel，它会判断当前的 register future 我们的注册结果到底是成功还是失败？


如果 is done 表示成功，如果成功，它其实就会调一个 do bound 0，如果没成功，他怎么去做的？没成功，它采用的是 add listening 的方式，就是异步的去回调，直到成功为止。成功再去调一下杜邦的灵方法，也就是其实我们真正的核心，其实最核心的就是 do 棒的联合方法，真正的去做我们的地址的注册，因为你看到把 local address 对象也传进去了哈，就是不管成没成功，它都会做一个等待，直到它超时或者出现异常的时候，它会才会 set 我们的filler。就是注册失败对吧？接下来我们把整个代码聚焦到 do 棒的 0 来简单看一看。


do 棒的 0 方法里边很简单，它就是调我们的 channel 点 event loop，点executor。把一个 runnable 接口，说白了，其实它提交一个任务对不对？ event loop 点 executor 它是什么？我们其实可以 control t 来看一看真正它。其实我现在 channel 点 event loop，它返回的是一个 net 原生的，叫做 event loop 对象，通过这个对象调用的 execute 方法去执行异步提交一个任务。这个任务做什么事情？你看 channel 点绑定，在这里我就不说了。在 channel 点绑定才是真正的去 abstract 绑定，对 pipeline 去绑定真正的数据了。这里边就是真正的做绑定的事情了。 OK 最后结束的时候，当我们失败的时候，我就把它 close 掉。其实对于这块就挺有意思了。刚才我说它是一个 event loop 对象，它真正的去调 excuse 的方法去执行。这个到底是一个什么东西？其实你按 Ctrl t，其实你能点到那个类。这个类比较核心的，它有 3 个，一个叫做嵌入式的 event loop，还有一个是 global event loop，还有一个是叫做 single thread event executor。其实它真正默认调的就是 single thread event executor execute 方法。它做的事情判断什么？判断当前你加进来的是不是在我的线程内的，如果是怎么办？我去添加task。如果不是，我重新去启动一个新的线程，再添加task，做一些其他的事情。


再往下简单跟一跟 start 方法，就是真正的是起线程了，因为我真正的一个连接过来，你肯定对应着要起一个线程去做这个事情。它这里边用的是 c a s 对不对？你看 compare and site，就是 c a s 的操作，去启动一个标准的线程。 do start to start 方法。里边这是一个断言，等于空在这里边。你看，这就是一个executor。


点executor。简单来说，这里边真正做的事情就是我们的。 OK 这是finally。如果注册失败的时候，他做一些兜底的事情。其实最核心的逻辑就是 single thread event executor。点 run 方法润航法。真正的去处理 IO 模型了。这个 isuter 是什么东西？其实你可以点去看一下isotor，它其实就是我们的 single thread event executor，或者就是我们的 n i o event loop，它会有 execute 方法，我们来看一看。


我们的叫做 single thread event executor，哈，点过去， OK 在这里，他应该是哈executor。它应该实际上是一个什么对象？它应该是对象，它是调这个对象，把 command 传进去，调用factory，点 new 一个thread，然后去start。


为什么这么说？还记得我们最开始的时候 executor 对象，其实我们看见过，在哪看见过？在创建我们的 n i o event loop 的时候，其实你可以点进去看一下，我们其实用到了这个东西 this super。再点进去，再跟下去，应该是在这个对象看见了，叫做 thread pre task executor 这个对象是不是？你看调用的 extra 方法去提交任务，让线程执行？说白了其实就是一个提交任务的线程执行器，叫做 thread pretask executor。okay，对应的往回点一下哈，刚才我们看到的 executor 就是刚才线程执行器，就是我们的 thread pre task executor 调 extra 方法，真正的去把任务提交进去。


提交进去它调的是 single thread event executor 点 run 方法，这个 run 方法就是我们的。你看这个类就简单了，我们用的是 event loop。 i o event loop 所以润航法，它真正执行的就是 n i o event loop 的润航法。


这个润航法到这儿其实小伙伴们你就看逻辑就很清晰了，到这就真正的是无限复用循环去监听标识位对不对？ select wake up 唤醒肯定是做这种监听操作。 select 操作。再往下看，就是做真正的 process select key 操作，做执行任务的操作。这个就是真正的去执行我们的 react 模型的一系列的事情了。


OK 好了，再往下我就不说了。大体上我们整个的 server 端，它启动的一个简要的核心的过程就是这样的。哈，希望小伙伴们对于有一点点了解就好。其实随着你不断的去学习，不断的去深入研究net，后面我希望的小伙伴们应该是好好去看一看 NET 的一些相关底层代码，它的一些设计，一些思想，还是非常不错的。 OK 我们这节课先讲到这儿，下节课我们继续往下去讲，感谢小伙伴们。


