---
title: 1-4 客户端连接管理器_核心连接方法实现-2
---

# 1-4 客户端连接管理器_核心连接方法实现-2

[image](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/e8022b2b-3680-4c07-8874-b7fdfb481e0c/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667VKZD73X%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T230026Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDVZxufc0XfTfOWcFZgkSXtcxq7JDy0nLn6%2FeEcDaVjzAIhALxQx9iqymNTJo703hk6RcyBud%2Bg3ZLPymYP6AAL4%2FykKogECMb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgxfKyL2HgGQM3k7YY8q3AMpxXU%2FTvDmgg7HTrhsq8DFdDGl5mYtBa7AMP1ieMy1NptACOyiDmRExj9cyLwZNPkuluEFwkBHKJ7KsMWlKINQ2JK7KROuEdoaac5G4dacGU7gc%2B7ktSQ9AzJRg%2BZth1ZL2Gy%2FKGiQ1nCtTbeNrEIsDAp0aCsiDHJsm3WOLEv2N13UOZVcNIEVZM3EmpV1U%2FK1ZMTO%2FmRRQ7vuwLP2UY2qdmZCXoV6tY6k%2FnoWpEfRnPfJv1nxeU%2Bi21jGLTdFJWjiUHJGRapxlNa0XPJogsumKvjISP7ED%2FNFhpGmopgwyzSaXPLqTNqQjdZN6%2FmLbsOjuSrg0wc1yH7iFXpiM8Y0VMcKWmNt20yEGQprSmVxY1CbBGleeSkYXacWWyJIKRAPMSO33FubV421be7VsN9o7KIsxFIFscBtEcf1kM7KlCk%2FzFqzfibmIJad8josfHZrQ%2FPMvPeDluU2rIvfArnkG0PFtytQJW5JQfpwaP8z5%2BFzIuUon%2B3ckRLLJeamxn%2FXA5QKhAxwW4aMpUl%2FzsU2J4Rujx%2FNDuh6LmgZIKh87fIKkQkKuYLcc5BwGcScKKWo0UerTB305fvjwOn8BZaGFNMyGzeWDJ4aMQglu%2BXqqJF1nPUZFLDW3H4%2F7jCst%2F%2FSBjqkAZYfO0Q%2BWccvWo5G2WHtMqdqFUys61PyHCbTbR9R3W%2BsG9cjyZzY19qSSQ7htyt9E0Ko8fMiUz352iSOhZelfgG%2FpIu9grPmkIFMKxrbrU%2B5ebz1wtXGasUk1vU6AE6hkfPZV1uU3ZKenukuOPqFuZhVlKOVs9kOOdwD2HGBnlloR9epFnjqYFIyyRvFQ4s5rwmjkbawhY0sgKzmWy8FqnzVpLOR&X-Amz-Signature=6ca975ab442efbdf1237736afe7f416f09f19718f88221910d174ab0a66407fc&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

final unit socket 的 dress 对象是 Java 的 net 包下的，这是我们的远程的连接。我们可以另外定一个名字，叫做 remote beer。这是我们自己远程连接，等于 new 一个 i net socket address，把 i p point 传进去。 i p point 我们已经解析出来了，可以了，这个就是我们的host。哈， OK 好。


紧接着有 i net socket address 之后，我们要做什么事情？其实我们想要解析出来这个地址干什么？因为我们现在做的是一个连接管理器。连接管理器的目的就是帮我们去把已经有的连接帮我们去缓存起来。如果没有的，我们解析出来一些新的地址，我们就发起连接就好了，对不对？因为我们知道这是我们远程连接的地址，所以现在我接下来的事情就是要发起连接。第一步解析完了之后发起联系就可以了。


好了，解析出来，假设这里一个列表是两个是吧？用逗号分隔的两个我们的remote。我们是不是应该做一个存储，把这两个东西，比如我们可以用一些list，或者是用 1 set 都可以，反正就存储一下就好了。在这里我们就用一个最简单的哈希set。为什么用哈希set？因为它是不重复的。假设你给我传进来的两个地址是一模一样的，其实都是这样的是吧？我可以去做一个去重等等。
这里边存储的就是 i net socket address，我们叫做新的 all serve load site new 哈希 set 好搞定，泛型传进来，把我们解析好的 remote beer 直接扔到 set 里是不是就可以了？这样我们解析好的地址已经都存在 new all server node site 里边了。


好，其实这一部分。这是第一步。就是什么解析我们的地址，并且临时存储到我们的，它是一个哈希 set 的集合中。为什么要临时去说存储？因为后面我们要拿到。比如现在是两个地址，我们拿到两个地址，对集合里边进行 for 循环，真正的去把这两个取出来，建立一个连接。这就对了


说白了，第一步解析完了之后，第二步做的事情就是建立连接了。第二步就是调用建立连接方法，发起远程连接操作。 OK 这是第二步的事情。好了，我们看看怎么去写。很简单，我们都知道这个是哈希 set 了，我们直接用一个循环就可以了。 for 循环，它每一个循环都是一个 i net socket address 是吧？咱们叫做 server node address，它就是 set 好。在这里做什么事情？在这里。


第二步，我们得到了这个是我们想要的地址，我们直接发起连接。说白了，在这里边我们直接是不是就要发起连接就可以了？怎么发起连接？咱们回顾回看。我们想发起连接的方式。在这里。你看，我想去做一个 connect a single 异步的去发起原结，我不能是同步的，阻塞的去发，我想去做一个异步的处理模型。好了，我们怎么去做？其实我们在这里写一个方法，咱们叫做 connected a single，把谁传进去，把我们具体的地址传进去。 OK 这其实就写完了。异步的肯定是一个


create，一个 private 的思路方法哈，在这里我打个注释，这表示我们异步发起连接的方法。 OK 好了，现在我做完了一个发起连接的方法，我已经搞定了。异步发起连接到底怎么去做？同学们想一想，异步发起连接我们应该怎么去连接比较合适？这个是小伙伴们可能需要思考的问题，我们回过头来看一下。在我们发起连接的时候，我们直接就是复循环了，我们自己去重哈。通过哈希 set 所就是 at 的地址。解析完了之后，直接就这样去异步发起连接对吧？但是有可能是什么？有可能有一个问题，有些连接我们已经存在了，怎么办？我们就不去再重新发起连接了。好了，我怎么去判断连接到底是否已经包含了？这就是有一个问题，这就有问题。什么问题？连接成功之后，它对应的一个结果应该是一个什么东西？我们应该把它去缓存到一个地方。这就是一个最核心的问题。因为我们是一个叫做 r p c connect manager，是一个连接管理器，所以连接管理器里边我们肯定要有一些东西去做缓存。如果已经连接过了，我们就从缓存里拿出来继续去请求就好了。如果没有，我们再创建。所以在这里我们会有一个数据结构。在这里我们要做一个缓存。


缓存我暂且用一个 concurrent map，比如map。我们在这里。 key 是什么？ key 就是我们的一个连接地址，我们可以用字符串表示也好。或者我们直接省事，因为我们后面已经获取到了 i net socket address，它当成 key 可不可以？ value 是一个什么东西？可以是一个channel，也可以是一个client，也可以是一个具体的业务处理器。


我在这里先创建一个类，后面我们慢慢去说。我先把它写上叫做 r p c client handler。好了。咱们小伙伴们肯定都学过 Nike 足够net，你就知道 client handler 代表是什么意思。它代表的就是我们实际的 handler 业务处理器。它到底是怎么去处理的？我们一个地址对应着一个业务处理器，这是不是挺合适的？所以我给它起个名字，叫做 connected handler。


map，可以等于 new 一个 concurrent 哈希map，又一个坎凯尔纳哈希 map 哈。把这两个东西拿过来，好数据结构是非常有意思的，后面我们再详细去说。现在我们暂且把写死我们对应的一个什么。一个连接的地址对应一个实际的业务处理器，当然业务处理器是一个 clan 端的哈。好了，我们先把这个东西做一个缓存。有了这个东西之后，我们下面就可以判断了，是不是直接连，也不一定对不对。当你现在我们 for 循环出来的地址，有些地址可能是已经存在了，已经存在了，我们就不去发起链接，如果不存在，我们再发起链接。所以在这个时候我们可以做一个小的判断。


我说if，如果我们刚才所看到的 map 点Keyset，大家都知道是一个取到它里边所有的key，这个 key 肯定是所有的 i net socket address，因为我们都看到了它的 key 就是 i net socket address，对吧？所以我们它取出来set，如果包含第二 contence 这个地址，如果包含这个地址，我还需要建立连接吗？我就不需要建连接，如果不包含，我再重新的去发起连接。我们可以做这么一个功能，如果已经有了的，我就不管了，没有的我才去异步的去发起连接。我异步发起连接之后的事情怎么去做？同学们想一想，无非就是帮我去建立帧的连接，再把 map 里边的内容具体填充好。


p 我们的 i net socket address value 是谁？ value 可能就是我们刚才所看到的这个东西。我刚才简单写了一下，其实就是我们的 r p c client handler，就是真正的一个对应的业务处理器。 OK 好了，这是第二步我们要做的事情。第三步如果第二步发起连接之后，我们的第三步，比如我取到一些错误的，或者是一些我想去删除的信息，因为你是一个连接管理。 t 如果已经不存在的地址，它还存在就不太好了。我可以做一个 clear 或者是删除的这么一个工作，这是比较好的，我暂且在这里边我打个Todo，因为这块后面的事情我们一会再说，因为可能我们要想象很多东西，我们才能做第三步事情。


简单说一下第三步的事情，就是假设列表里面对不对，如果列表里不存在的连接地址，我需要从缓存中进行移除。本身来讲，假设我们在创建一个新的连接之前，我原先的 map 里面已经有一些旧的连接，我是不是应该把一些旧的连接给它干掉，到时候我们再去做这件事情。如果在我们新的列表里不存在的地址，在旧的列表里还存在，在缓存里还存在，我们要把它进行一个移除工作，这才叫一个真正的连接管理。


这是第三步我们要做的事情。紧接着我们先看一看第二步的事情，你要做什么？我们点进去，如果不包含的连接，这是一个新的连接。我们从地址上去解析的新连接，如果不包含，我们才建立一个连接。建立连接这方法我们这节课先写完。怎么去做？首先我们回看之前说我要去把这个东西通过异步的线程池去给它搞定，对吧？异步的线程池去做一个提交任务去异步的去建连接，这个太好说了对吧？所以我们来先把它写一下。首先我们在这里边先搞一个异步的线程池，在这里边我写一个 private thread pool executor，我们叫做 thread pool executor。我就直接粘过来小写，等于 new 一个 thread 或executor。当然这里边我们传几个比较关键的参数就好了，哈，我就传几个比较基本的参数。


首先它的 Cos 写死16， OK Max 路塞斯也是十六在这里边。比如我们连接超时时间是多少时间一分钟或者是十分钟都可以。六十。比如这个时间戳 time unit，我们可以给他一个second，是不是表示连接超时时间就是一分钟对吧。空闲连接时间是一分钟。接下来就是你的这个队列，我们可以随便选择一个，比如我们正常的 g d k 最常用的 array blocking key，实际的大小我们可以给他一个，比如是 1024 跟 536 这么大，6万个这么一个队列。


好了，这里边肯定是实现了 runable 接口的哈，因为这是一个任务去提交的。搞定，现在我们线程池有了，我们打开注释这个线程池的目的是什么？用于异步的提交连接请求的线程池。好，我们去拿着这个东西，到我们刚才所看到的 connect a single 方法里边，我们去把它做一下。 submit summit 肯定一个 new 一个 runnable 接口去做一个实现就可以了。在 run 方法里边，我们去写我们自己代码。怎么去做？首先 boot strap 我们先给它搞出来，因为我们现在是 clang 端，所以我们用的是 boost Chop，如果是 server 端，就是得用 server boost chop 了。这个小伙伴们应该没有疑问，等于 new 一个新的 boost shop，搞到 boost shop 之后，我们去 new 一个 boost shop 对它去做一个绑定，是不是点 group group 肯定需要一个 event loop 是吧？ event loop 我们刚才没有定义，所以现在我们直接拿过来定义。在上面我们再定义一个 event loop private 一般我们去真正使用的时候，都使用我们的 n i o event loop。当然 event loop group 它是一个上层的这么一个类。哈，咱们叫做 event loop group，等于 new 一个NIO。 event loop group 初始化我可以给它一个大小，比如4，它默认是我们的 CPU * 2 的一个大小。哈， event look group 写错了。


好了，搞定完了之后，把它绑定给我们。具体的 boost up 继续。首先来看看它的绑定，它具体的 channel 它的 channel 肯定是我们的 NIO socket channel， server 端是 NIO server socket channel，哈，这里边是 NIO socket channel。点 plus 接下来还有什么内容在这里我们这样去做。接下来它的 option 这里边我随便给他一个，比如我让他禁用 NIGO 算法，让他数据包别给我去做这种合并的操作。


the channel option 这里边我们可以写 t e c p， t e c p no niggle 是吧？新用算法我就可以写成 true 就可以了。还有一些属性，想加就加，不想加算了。搞一个 handler 出来。这个 handler 是什么？这个 handler 同学们还记得吗？你要去自己去 new 一个 initalizer channel 初始化。我们在这里可以先写一下，咱们叫做 RPC client init leather。好了，我们就先这样去写。


最后要做一个连接方法。比如我们再写一个真正的连接方法connected，把我们的 boost top 可以传进去，把我们的远程地址传进去。远程地址是谁？他他就是一个。我可以叫做 remote beer，搞定就可以了。同学们，请看这个模型，我做完了，它就是真正的去异步发起一个提交到一个线程池里了。一个任务。这是真正的连接方法。前面是一个初始化，我们先看一看 RPC client init leather，我们先把它先搞出来是吧。这个倒很简单，我们来去 finish 好了它。既然我单独去把它弄成一个类，那它肯定得去做一个继承操作。


exist 叫做 channel init leather。 channel init leather 他肯定是传的是 socket channel， socket channel 肯定是我们的 native 的，哈，他应该重写 init channel 方法这个类我就写完了对不对？这个类我先不做具体实现，因为我们看到没问题了。 connect 方法就是真正的去做连接了。我们在这里再把连接方法写一下。 private void connector 这里边传了两个参数，一个是我们的 boost type，我们可以先定义好哈。 final 我们的 whats up，这是我们自己所定义的。还有一个我们的 remote beer 在这里边，我们其实直接可以拿过来 remote beer。好了，这节课的整体的代码就写的差不多了。当然还有一些没完善的，哈，我们来一点点回顾一下。


首先我们要建立连接的时候，首先我要把这个东西按照我自己定义的规则去解析，比如按照逗号去解析，逗号解析之后，它会生成一个list，它直接调我们的 update connected server。 update connected server 是比较关键的，首先它需要解析成一个的我们的 i net socket address，把它放到一个 set 里边，用于做去重，如果有重复的可以去直接帮我们去重。解析好了之后，放好了一个哈希set。


集合以后，我们去对每一个新的 i net socket address 去发起连接，对吧？我们应该发起异步的连接，但是这个时候我应该做一下判断，因为我们去做一个连接管理器，如果已经存在的，我们就不发起连接了，因为存在了我们直接取就可以了，对吧？不存在的时候我们才去发起连接，所以在这里面会有一个缓存。


它是一个 Hashmap concurrent Hashmap，它的 key 是我们的 i net socket address， value 是我们的 r p c client handler，我们的一个地址对应的一个处理器，实际的客户是处理器，它是一个坎坷的map，没什么可说的。
再往下回过头来发起异步连接。如果不存在的，发起异步连接。具体发起异步连接的事情点过来就是我们要做异步。所以我要用一个线程池去异步的去提交一个任务，这个任务真正的去做初始化工作，再去做实际的连接操作。但是当然实际连接操作应该是我们下节课去实现的，这节课我们还没有去做。
OK 最后我们回到 update connected server。我们第三步如果列表里不存在的连接地址，列表里边我们要现在要连的地址，列表里不存在我们的缓存里，我们应该从缓存里把这些移除。假设我有 3 个IP，加端口号，有 3 个地址，但是我之前的 map 里边可能有 4 个，他们之间可能其中假设是重叠的，有一个没有用的，这次我连接的时候就有一个没用掉。我应该把这个资源给它删掉，把它移除。后面我们要做一个移除的工作，这也是我们接下来要讲的。好了，感谢小伙伴们收看这节课，我们先讲到这。

