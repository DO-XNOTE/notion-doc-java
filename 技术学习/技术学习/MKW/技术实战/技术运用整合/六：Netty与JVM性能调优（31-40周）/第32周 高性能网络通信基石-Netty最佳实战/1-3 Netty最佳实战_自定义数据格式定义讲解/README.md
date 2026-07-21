---
title: 1-3 Netty最佳实战_自定义数据格式定义讲解
---

# 1-3 Netty最佳实战_自定义数据格式定义讲解

[image](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/b1d9c932-afff-4cd4-91e8-d5c11fd153c9/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VDX43N65%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T230013Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCNcVFUOVCQ6fmZo%2BuJnBtMBvwVouk44C1WPcDZwt8UKwIhAKhHvaDje68dzsCxpm2Th6WnD07eTLNUCGmn7o62O7vPKogECMb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgzwcjmQlYo%2FoyQYivUq3AOW1eMf%2BVDbAoWFO6FfFVEL0fQANZTbRcm3cLSUi3dI7%2FMeL8AvWqeKd%2FrXJJxi5taEPBBcg8N%2FMb2k%2FgdHpM3t3Moabxie%2FL%2FO1VhjR8LoScoWa1YOInYzJv9kn31AMlpa%2FltXG3K0YOJ3Cdkgt1jwrnPmsOdSYrS8FerVp2qj3K9pyiFX21WLZyPCOSgBZE%2FDb%2FI1vzM73mmZGQPzUKvhnjpcBSZk7eODEXosBNWAaJk%2BQC%2Bt25GedA%2Fmf6m3rmvaxmRuS24J4IITURssTQsD3HqRU4uH0wtASw8dNo1JVyxKRla0yeSKM4dJcwLU%2FR9eYM3%2ByLqcZK6Ivbw%2BcZ9JdOvvDtgDv8gidSkUhp8S%2Fo6mo5zPq5X8d4P0Obq%2Fg37YM8jSM5Ko8YUiVRkVzg5WwULT3k%2B4zFF55kRplGX4Cj6pUZbTHYlLABNZKRQZ8e0dZ%2FotgBAAMLJ65d06L2Jg87c90Lz4FRl6kwp%2F5M%2FA4FvtKmoNCltEnF8KoGBRlMX1sJpfZ4IiflNjyeNGurkU5I3vSD6q43Twn8DL1WHw223XuadZ298Lbs9KfrEujfcPj8Hzyerw8eb06%2F2P5hgv4AMfIAaegl5JQrWqvbdbRBbWoQVeBfPDj%2FmXBDClt%2F%2FSBjqkAeQTRNtyeK6EBnpP7JPekbX254BPtnWIhCze2MGqBo0I1s0AHB9gCw7DyWzPq1R5pbfRplHY%2B%2BWk%2BYiQ%2FgrUbQWdm76IeQDo9TBh4Z6z%2B%2Bk8I4DEobJzxNrHzuAyFekviU6wJ%2FUvbu5pPCcUr1rwgwmr1IT6ZJfBPwcHi%2FNe%2BjX3YYA2sSJwIpMXl%2BBsdyMbNFl0z4QllvTdMCXWFuPF1n%2F2tfbL&X-Amz-Signature=7c2cad89d3a074c9f237d9ac6e9a87e2303bd9e55f5983a71f5bc4df0a911fe2&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

OK 小伙伴们，这节课我们继续来往下去讲哈。接下来我们就开始进入数据包的一个定义了。对于数据包定义，我们暂且回到我们之前的上节课的内容。对于这幅图说的是什么意思？就是我们不同的模块有新增、修改、删除，你应该对应的去到不同的模块下面指定的新增、修改、删除里边去对应的去做操作。这个时候我们来想一想我们的 pre buffer 数据结构应该怎么去定义。


首先一点，请求和响应的数据怎么去定义？在这里面我们的请求跟响应一定要区分开，请求是请求的标记，响应也应该有一个响应的标记，所以这个是必须要去做的。第二点，我们去做实际处理的时候，我们的请求去发给了 solo 端， solo 端去做实际处理的时候，它到底是成功了还是失败了？还是抛异常还是其他的情况？我们也要去做一些定义，包括我们实际的数据包格式是什么样子的。我们也应该再次的去做一个定义。最关键的一点是什么？最关键的一点就是你要对于你的模块以及对应的更新的类型也要去做一个定义。好了，有很多地方我们都需要去做细化。


接下来我们就开始对于普通 buffer 做一个格式的定义。首先我们在 common 包下建一个目录，叫做 Pro to。在 Pro to 目录下面，我们比如现在我去建一个咱们叫做 message 点 Pro to 这么一个 prebuffer 的文件。 OK 正好跟对应上了，哈，这个是 message 点，当然它叫 message 点 bat OK。好了，第一件事情就是我们要使用的是 probus 3，所以要加这么一个 s y n t a x。就这么一个注释，必须要标记它是普通三。紧接着，sorry。紧接着我们要指定一下option，就是我们之前 photographer 所定义的Java。它的 package 是什么？ package 是什么？我们来定义一下。在这里比如我想去在 common 包里面定义一个package，叫做 Com 点 BFX y 点， c o m . com m o n 点什么？比如现在我想去通用的定义一个格式common，我叫一个普通buffer，或者是其他的都可以。 Pro to buffer 对应的目录就是我文件输出的一个目录， Com 点 b f s y 点 common 点probucker。好，这就是我的目录。


搞定以后，接下来还有一个我们的 Java 的class，应该是叫做alter，我们的叫做 class name。 OK 好，在这里我们来定义一下当前我的模型。我定义的数据包的模型名字叫什么？我们可以给它简单起一个叫做 message module 可以，或者叫做咱们就下 message modular。消息的包搞定了之后，接下来我们看一看我们整个的数据格式应该怎么去定义。刚开始老师说了，对应着我们到底是请求还是响应。我要定义一种类型，在普通 buffer 里边支持枚举类型，就是enable。这个我们就叫做什么？可以叫做 message type，给它起个名字哈。咱们叫做 message type。我们比如它有两种类型，两种类型。第一种咱们管它叫做。比如我们叫做服务，我可以去多大写哈，都可以的。我叫做request，或者是叫做 service request 都可以。比如我们就简写request。注意在枚举类一定是从 0 开始的哈， raise force 等于1。好了，现在我们定义了我所有的通信哈，无非就是分请求跟响应。所以我定义好了第一层。


第二层假设我们返回值类型，我们还是要搞一个枚举类，我们叫做result。 Results check。 result type 是什么概念？我在客户端请求给服务器，服务器接收之后，他给我们的回送的响应在这里边，我说叫做success。第一种枚举都是从 0 开始的，第二个就是 failure spell her OK 要么就是成功，要么失败。


接下来除了成功失败，我们再来一种。比如我们叫做 system error，或者是 system exception 都可以。比如我们在这里定义一个比较简单的，就叫做 e x c e p t i o n。就叫做exception。就是失败的情况。可能是你内部的出现了一些异常，我把它我们叫做C440L。可以我们再给定义的 e r r o r c c i o。比如其他的一些异常，或者是我们可以定义一个什么 i know exception。这里面随便你去定义哈，只要你觉得想用的，结果可能发生的都可以有。


这两个比较关键的内容，我们定义完了之后，接下来我们定义什么？我们来去定义我们真正的数据包的结构message。注意，这回就应该用 message 了，我们也叫 m e s s a g e 这个类。好了， message 接下来我们去定义哪些内容？我们来想一想。


首先第一个我们可以去定义一个 INT64 位的浪类型的，对不对？ Java 来讲就是浪类型。我们定义一个请求的标记， c r c code 还是可以的。接下来比如请求的标记，我们只有符合标记才能通信。接下来就很简单了，就是你的 message type 到底这次通信是什么类型？是请求还是响应。对吧。你就直接这样去写，给他起个名字，我可以小写一个 message type t y p 等于2。好了，接下来你的响应类型是什么？对不对？你的 result type 是什么？这也是可以有的，所以我们直接来，咱们叫做 result cup t VIP 等于3。同学们，想一想，接下来比较关键的就是还记得我们之前这幅图。这个模块我们可以定义一个，叫做 modular type，我们可以叫做command，叫 CMD type。具体它是访问的是哪个模块，以及对应着哪个模块下面的什么操作，所以我们也需要定义。

[image](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/1212efce-c4e8-42b0-a855-397b4060255c/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VDX43N65%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T230013Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCNcVFUOVCQ6fmZo%2BuJnBtMBvwVouk44C1WPcDZwt8UKwIhAKhHvaDje68dzsCxpm2Th6WnD07eTLNUCGmn7o62O7vPKogECMb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgzwcjmQlYo%2FoyQYivUq3AOW1eMf%2BVDbAoWFO6FfFVEL0fQANZTbRcm3cLSUi3dI7%2FMeL8AvWqeKd%2FrXJJxi5taEPBBcg8N%2FMb2k%2FgdHpM3t3Moabxie%2FL%2FO1VhjR8LoScoWa1YOInYzJv9kn31AMlpa%2FltXG3K0YOJ3Cdkgt1jwrnPmsOdSYrS8FerVp2qj3K9pyiFX21WLZyPCOSgBZE%2FDb%2FI1vzM73mmZGQPzUKvhnjpcBSZk7eODEXosBNWAaJk%2BQC%2Bt25GedA%2Fmf6m3rmvaxmRuS24J4IITURssTQsD3HqRU4uH0wtASw8dNo1JVyxKRla0yeSKM4dJcwLU%2FR9eYM3%2ByLqcZK6Ivbw%2BcZ9JdOvvDtgDv8gidSkUhp8S%2Fo6mo5zPq5X8d4P0Obq%2Fg37YM8jSM5Ko8YUiVRkVzg5WwULT3k%2B4zFF55kRplGX4Cj6pUZbTHYlLABNZKRQZ8e0dZ%2FotgBAAMLJ65d06L2Jg87c90Lz4FRl6kwp%2F5M%2FA4FvtKmoNCltEnF8KoGBRlMX1sJpfZ4IiflNjyeNGurkU5I3vSD6q43Twn8DL1WHw223XuadZ298Lbs9KfrEujfcPj8Hzyerw8eb06%2F2P5hgv4AMfIAaegl5JQrWqvbdbRBbWoQVeBfPDj%2FmXBDClt%2F%2FSBjqkAeQTRNtyeK6EBnpP7JPekbX254BPtnWIhCze2MGqBo0I1s0AHB9gCw7DyWzPq1R5pbfRplHY%2B%2BWk%2BYiQ%2FgrUbQWdm76IeQDo9TBh4Z6z%2B%2Bk8I4DEobJzxNrHzuAyFekviU6wJ%2FUvbu5pPCcUr1rwgwmr1IT6ZJfBPwcHi%2FNe%2BjX3YYA2sSJwIpMXl%2BBsdyMbNFl0z4QllvTdMCXWFuPF1n%2F2tfbL&X-Amz-Signature=f82f22c8200848f6b276ea8c0786647a9faab29355e8f5d4a5590131772b4a2c&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

好在这里我们可以去换一种，比如叫 string 类型的对不对？ string 类型的modular，我们知道模块类型是什么，对不对？第四个第五个 string 类型的。什么叫做command？咱们叫做c、m、d。第六个就是 message 里边其实最核心的东西，你可以认为前面这些东西就是我们包的 header 头，就跟我们自己做资金协议是一样的，哈，这就是包头。包体是什么？我们包体我们可以去给他一个body，比如b、y、t、 e 斯就是贝斯body。


一个真正的数据存储的内容，我可能不知道是不是它，这里边可能存储的是什么？可能存储的是 user 对象对不对？刚才我们看到这幅图，它可能是 user 对象，也可能是 group 对象，对吧？ user 对象你要这里边要标记。 module 是user。 user 对象什么样的操作写好？如果是 group 对象，你在这里要标记是group。具体什么操作，写好这里边具体的传输的数据内容了。


现在我们已经把我们第一个最简单的，也不能说最简单，整个的个数据包的结构已经定义好了。数据包的结构定义好了之后，接下来我们其实可以顺带着去把。比如我们现在再去创建一个 user 和一个group，这两个类也都可以先搞定，我们一起就创建了。为了方便后面要不然也自己得创建哈。


我叫做 user 点protool。 user 点 proto 文件在这里还应该有一个叫做 group 点 Pro to 文件。Ok？ user 点 control 文件 group 点 control 文件这里面输出到哪？其实我们在这里也可以参考这两个东西，咱们先看user。首先 user 它输出，它输出也，我可以给它输出到普通 buffer 目录下是可以的。它的名字咱们就叫做 user model 了，我们之前很熟悉了，对于 user 它的格式我们就简单写一下就可以了哈。这个名字咱们叫做 user 对不对？ user 里边我们就可以给他几个核心参数，把 Int 类型的，比如它叫做 user ID。这是从 1 开始的。 string use a name 可以了。 OK 好了，这是 user 对象，已经定义完了，我们就简单的去定义两个属性就好了哈。我们要为了实现不同的模块，实现不同的操作。


好了，接下来我们把代码 copy 一下，我们点到我们的 pro two，在这里边我们叫 loop 哈。我点到我们的group，叫做group，这里边改一下，咱们叫做 group ID 叫做 group name。好了，现在我们整体的数据包结构已经定义好了之后，接下来我们可以在copy。我们可以点到具体的文件夹去生成对应的普通 buffer 的 Java 的文件。我们来一起来操作一下。


好了，现在我直接打开到我的 d 盘，我的 d v 004，咱们找到 net 的 comment 下面哈。我可以把这个东西再复制一份，两份复制 3 份对吧。首先第一个是什么叫做 user 点bat，哈。再复制一份，这个叫做什么叫做group。第二 BAT 哈。有三个执行脚本需要执行。首先我们来看一看第一个脚本，我们打开一下，看看是不是我们想要的，我一定要是以点普通 message 对不对？我文件它肯定是叫 message 对吧？一个叫message，一个叫user，一个叫做 group 点control，这是没问题的。我们现在第一个已经完成了，这是没问题哈。我们回过头来把它改一下， user 点bat。很明显这个应该叫做什么，叫做 user 点 Pro to 保存一下。还有一个我们对应的 group 点BAT，我们来改一下，叫做 group 保存好了，已经搞定了。


之后我们来分别去执行一下。首先我们执行 message 点BAT，哈，按回车，再执行 user 点BAT，按回车。如果它生成了，就证明是 OK 了，如果中间它没有生成，说明可能出异常了。好，现在我三个都已经执行完了。我们回到具体的类里边去刷新一下我们的 common 包。刷新好，小伙伴们请看，对应的 3 个 Java 的类已经出现了哈。


一个是我们的 message module 是没问题的，你看刚才我定义的内容比较多，所以它里边就有 1200 多行。你比如 group 跟user，相对而言，它定义的内容比较少，所以你会看到内容也是比较少的哈，基本上就 800 多行， 700 多行。 message 这个包还是比较大的。好了，现在我们最开始已经把我们的数据包定义好了。之后他们三者有什么关系？在这里继续给小伙伴们梳理一下。他们三者的关系是？在这里我往下来说一下。


他们进行传输数据的时候，传输的数据格式都是一样的，叫做message。 m e s s a e g e 他们传输的格式都叫message，只不过这个 message 里边有一些相对应的属性，好把它最大。他们传输的内容都叫message，小伙伴应该能看到。只不过这个里边有一个比较关键的内容，就是他传输的内容是什么。


首先有一个module，这个模块应该等于user，假设我想传 user 数据，还有一个它的 c m d，它的命令是什么？比如我们想去做一个存储方法，肯定是 save 了，对不对？接下来还记得吗？我刚才定义的一个叫做body，那个 body 它是干什么的？它是真正的去做 save user。是不是你要把 user 的一些实际的数据做一些数理化，实际的数据做一个序列化？当然实际的数据就是我们的 user module。刚才我们已经创建好了一个 user ID，一个 user name。


当然还有一些其他的，比如什么我们刚才说定义的 c r c code 无所谓，就是一个标记。比较关键的就是你的请求类型，你的通信的类型，我们叫做 message type。就是你的 message type 到底是请求还是响应，对不对？到底是 request 还是response？ r e q 或者是 r e s p，到底是请求还是响应，你要确定。比如我 client 端去向服务器端发我包，里边肯定是request，我的服务器端给我 client 端回送响应的肯定，这个类型应该是response。还有一个比较关键的就是我们的 result type。对 result type 什么意思？就是我服务器端处理的结果到底是成功还是失败？比如成功是1，失败是0。


还有一些其他的异常，我刚才说 system error 或者是其他的你自己可以随便去定义，比如它是 2 都可以的。这都是我们刚才对于数据包已经定义好了的。所以我希望小伙伴们对数据包格式的定义一定要认真的去仔细的去想一想，我为什么这样去定义数据格式以后再扩展的时候，以后如果再扩展的时候，我整体的 message 是永远不变的，格式就是这样的，它是永远不变的。我在扩展，我只需要加我自己实际的模型类就好了。比如我 user 有了之后，我再加一个什么car，或者是一些其他的东西，其他的类我都可以去，尽量去扩展， order 订单我都可以去扩展，继续扩展。因为我只需要填充好我具体的模型以及具体的命令，还有具体相对应的一个 base 字节序列化的一个贝特直接数组就可以了。


好了，我不知道小伙伴们对于 common 数据包定义是不是已经了解了，如果了解了，你可以去跟老师一起把这一块一起去实现。我希望我们在做这个项目的时候，是小伙伴们跟我们一起边听我讲你同步的去跟我一起去操作，这样你的印象会很深刻。好，这个是怎么说？这是最好的学习方式，尤其是等到我们 net 讲完了之后，我们去做一个简单的 RPC 通信的时候，里边的设计模式，包括一些设计思想，都是稍微有一点复杂的。其实我还是建议小伙伴们跟我一起来同步的去做。你听完了就开始去写代码，这是效率最高的，也是学习最好的方式。 OK 这节课讲到这，感谢小伙伴们收看。


