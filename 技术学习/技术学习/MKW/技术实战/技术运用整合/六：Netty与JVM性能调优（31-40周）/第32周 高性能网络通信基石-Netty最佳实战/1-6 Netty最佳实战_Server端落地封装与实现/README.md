---
title: 1-6 Netty最佳实战_Server端落地封装与实现
---

# 1-6 Netty最佳实战_Server端落地封装与实现

[image](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/ce316c51-1b13-4436-89af-f9fa09a423f9/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XH6YMKYT%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T230015Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCb1o7%2BAVDff1p6yx%2BuQOmaiAID6JIyRxVx%2F2fJKcl%2BbgIgCMyn0WUBIW3NAfxwt86RC7Mwz90ZKHsIFoU52GDZdkwqiAQIxv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDJlnHz0WrgGMKFrxNSrcAzT%2BzYLedwY57zliXoIa%2FRjkWfn8s3ka%2F6l9rFDVAY9qClPAMUhMzi1FYbMMDrZvsgL%2FgBusI%2F%2FPiTkMiAO%2BG1xwYmMbW92FQgojpcBbfCh1OVwWUNP0mBLcoS6%2FNXtZ%2FbrB%2F8R75JWajgeppcEzCFv4aB8gATbTAJfFba4skrHOaRZKkV7%2FAJo4t2sLmC%2F2DTbpN%2Be7aNJJ6iXOog%2FseC4rThTKmEykPjhj5rTz3fZrCpn4sqxiO2embUFXH9egNHlE5IXeK%2BimzbeSOrwls4T4efixi2JMinezfdCy6q7R1FysFrPHn1eXzYXM5zSloBPXxwu8i7utHAUmLtaEhB8c8MPhFFnY%2BJKJv2e%2FZNDfnxxJNXSHhhI3xZSScvTr0O3XToMRenFnsEoB1rBg4tcpMEs1O3ZQ8EuU%2FKywwJlrcp%2FCpXJLEtMAFZkwW2HRV%2FiNbqRM2YIFX3O5X6YGnSTXd9qAguoydVQfLqmrefpQxSL5soodjcnRssxa9qCa%2F5pvrSDUjQ%2FtlaNNj8Kq%2F1kKtb5g5l0Yv6lSuI1rZdQNOoy4GApai0AfbWlQlraI%2F19LbHHsXNQyQJAZ3uG8IcGaP9YfONYVhZXB6WiW2FAW3ANOVbEDnTuAN97oMMK6%2F9IGOqUBLCDjKDPfKFMYd3rCjHyYmcPAhAI41dCor4cgIO5puWxS1tohxX9tHUjYsulCjSkpmVFnYEhyl2T9IHusoQs1MlGJakfEdseDt95EVgvZcB%2BsstExYLlYK6Pjl9Ju8dKz5If7aEHUdhKrttt5sf8SelDw3kKK4vllojbfoV5WpYKaTWakPvalfqYgrELU46sO5rFCt7dkRt0KJ75gy7%2F3pBAigy%2Fp&X-Amz-Signature=8789b213957fd803ac188997d481a5d1c236039d2afade91dd3978339d0ff3bd&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

OK 小伙伴们，咱们来继续课程。上节课我们已经对于我们自己的 Nike 它的 scanner 它已经搞定了。这节课我们来看一看我们继续要学哪些内容。这节课其实我们已经把跟 spring 集成搞定了，事情就简单了。下一步骤我们比如来对 net 的 client 端跟 soul 端做一个具体的handler，以及具体的 init channel 的工作了。比如我们最开始在老师已经把 init channel 已经没有去写，包括它所实现的handler，没有去做任何的实现。接下来我们一起开始去做一下工作。


首先我们来看一看具体的。我们都知道我们现在所用的就是普通buffer，它的编解码。我们来看一看怎么去做。这块我不知道大家还记不记得我们之前讲 pro buffer 的时候已经说过了，我们通过它的 pipeline 去点 add last。首先它里边一共要加 4 个类，哈，是比较多的。第一个是要 new 一个 blue to buffer，它的 white 32 什么 set decoder，这是第一个要加的。接下来它一共要加四个，不着急，我把它先都写上，再加上我们自己的业务逻辑，可能就是 5 个了。自己的业务逻辑就是 client handler 了，在这里先把它写好。


client handler 在第二个是什么？我们对应的。你要知道我们 client 端需要接收的是服务器端的数据，所以 client 端如果接收到服务器端数据，一定要是把我们服务端的数据给它做一个处理。当然现在我们无论是客户端也好，还是服务器端也好，它本质上传输的对象都是message。所以这样我们首先对于它具体的decoder，它在解码的时候，对象我们就可以确定了。它在 Protobuffer 它的 decoder 类，我们要传递的是一个固定的。


什么是一个固定的？我们的 message build Messager 叫做 modeler 点什么点 message 点 get default incense，因为我们已经做了二次的封装了。我们在 protobuffer 的 decode 的时候，哈，一定要想到这块 message module 点 message 点 get dephoto instance okay 是我们提前要做好的。多了一个括号，把它去掉，辛苦多了一括号。来看一下。


这里边有一个小的问题，我把这两个先注释掉哈。这里边说 paper line 点 add last new 一个 pull to buffer 的decoder，这是没问题的。当然这个 message 这个类到底是在哪里？这是我们 comment 里边所定义的。这是没问题的哈。我们回过头来，它这里边为什么给我报了一个错？我们来看一下。


remove probuffer decoder，让我去删除 at last okay，我知道了，这个写的有问题，这是 spring 的，OK，换掉哈。一些。千万不要写 spring from work，这就有问题了，一定是我们 net 的哈，我们不要找错了。好把我们刚才的那句话叫做 message modular 点message，点 get default instance，这回就不报错了哈。
接下来就是跟它对应的有一个叫做 protobuffer warrant 32，有一个叫做 lens freed prepared，我不知道小伙伴们记不记得，没关系，在这里我们一起复习一下。叫做 length 打头的对 prepared 往下走。


最后一个。好，最后一个我们的encoder。我们的编码器。编码器就非常简单了，因为它编码都是基于普通 buffer 的规则，所以它不需要我要通过谁哪个对象去做编码，我们直接去传递一个 encoder 即可。注意一定是 knitted 的。哈，好搞定。


这样对应着我们客户端的，起码是客户端的 init channel 已经写完了，我们把逻辑通过 copy 直接同步到我们的另外一端，就是 server 端。因为这个过程其实都是一样的，没有任何变化的。所以在 server handler 里边直接 copy 过来，只不过在这里边改成我们的 server handler 即可。


这个步骤相信小伙伴们都应该没有太大的疑问。我们记得最开始我们去讲 probuffer 的时候，有一个request，还有一个response，对不对？它们是不同的。但是老师现在已经把整个的最上层的数据包已经定义死，都叫message。只不过在里边所传递的类型有request、response，传递的实际的数据是不同的。所以我们在最上层编解码的时候都通过它就可以。


好了，其实对于这块我们已经搞定了。接下来我们要做什么事情？接下来由于数据是通过 client 端去发送的，所以我们其实可以写一个最简单的。当然发送的逻辑很简单，我们在 connect 建立连接之后，我们已经保留了channel，我们通过拿到 channel 就可以去 out flush，比如去刷一些数据，这是可以的。比如我们刷出一些数据到我们的具体的 server 端，我们来看看 server 端应该怎么去实现。


逻辑。我们来点到 server 它内部的 server handler 里边看一下，肯定是 server handler 里去做处理的。点到 server handler 里边， OK 对于 server handler，我们来看看怎么去实现。


Server handler。我们其实实现有各种各样的方式。首先第一点，我们要明确一个对应的它 object 是什么。 object 一定是我们刚才所看到的通用的叫做 message module 了，点 message 这个类，所以你直接可以转换过来。因为我已经确定好用 message 都传输了，所以我最开始第一件事情我就可以干什么，我就可以直接拿过来，它叫做它肯定是请求 request 等于我们的message。我可以做一个强制的转换，把它转成我们。具体的。当然我也可以用全名称，因为 message 它有好多任何的开心框架，都叫message，所以你一定为了避免别出现问题，我们一定用的是对应的message。


好了，有了 request 对象之后，我们怎么去做？同学们想一想。 request 对象。我们都知道native，它是一个 reactor 模型，就是我们的 boost group，它是用来接收连接我们的 worker group，是用来做实际的处理的。其实如果你有真正的一些比如数据落库的操作，数据同步持久化的操作，尽量不要让我们的 worker 线程组去阻塞，你可以再次的去把它丢到异步的线程池里边去做一个实际的处理，这样是最好的。所以我在这里建议 request 对象，其实你都不需要做任何的处理，直接把它干什么，直接把 request 项扔到一个异步的线程池里去做处理就好了。


这是我期望跟大家说的异步的线程池。其实我们很简单，我们可以在这里边去定义，或者是我们再封装一个类去定义都无所谓。比如我们现在异步的去做一个提交，做一个处理就可以了。在这里我们直接定义一个 thread four executor，定义一个线程式，我们叫做workpool，等于 new 一个 swede pull executor，我们自己定义一个线程池就可以了。拒绝策略这里边其实我可加可不加，我是无所谓了。 OK 就只有这么几个参数，我们自己来配一下就好了。第一个 cost 我们可以写死了，比如写死了我们的 5 个 Nexus 10。 keep left 我们认为60。当然我们可以一分钟或者是 60 秒都可以，比如我们 60 秒 time unit 点 seconds OK work Queen 我们选择什么？ array blocking Queen 或者是 unblocking Queen 都可以。你有一个 array blocking Queen，我把它容量定义好，比如是4000，随便给它一个参数。


当然在实际的工作中肯定会有一个叫做拒绝策略的概念，我们可以叫做我们直接找到它具体的一个实现，看到源码哈，它里边有好多实现，我们去找到它指定的一个discard，就是带有拒绝策略的。我们 Ctrl o 找到它的这个，这里面有一个 reject handler，看它。最后我可以去传一个handler，就是它的拒绝策略。在这里我们 control t 来看一下，它里边有这么几种。



我们可以去选这种 discard proxy，我们可以直接来就 new 一个 discard proxy 就可以了，也就是我现在要做什么事情，我就直接拒绝。当然它这个类你需要去把它引进来，它是一个 static 的，所以很尴尬。我们得去找到他，他点 discount proxy 好，这样你才能去找到。


这样超过我的 4000 的限制，我最多再给你加，因为我是有间队列，我们大家一起复习一下有些队列有什么样的特性。最开始初始化有五个线程池去工作，超过五个之后都会把它放到任务队列里。如果超过任务队列的长度，有接队列 4000 怎么办？它不是直接取决，而是看一看 Max 它的 size 到底有没有剩余的线程了。 Max 肯定还有 5 个，再用 5 个之后，这回 10 个了。如果还有一个任务过来，就会直接丢弃。


我们采用这种策略，这样我们做的事情是什么？我们通过 workpool 去把它提交。 workpool 点儿 executor 或者是 submit 都可以。 submit 我们就直接 new 一个runnable，你可以直接 new 一个译名的 run 的接口。当然还有更优雅的方式，就是我们期望做什么事情，比如我再次想要一个通用的这么一个类，我可以把 request 对象。在这里我跟大家详细去讲一讲。把 request 对象扔进去之后，我肯定是对 request 对象做处理，做解析，解析完了之后干什么？把 request 对象操作完了之后，我肯定得需要 response 对象给它响应回去。因为我是服务器端，所以在这里遇到一个问题，就是我们其实要把这个东西做一层包装，也就是我们需要把 request 和一个对象一起一并带过去 context 上下文。


如果你没有上下文，你都不知道怎么去写出去，这是最核心的问题。所以在这里我们可以去在 comment 包下创建一个通用的 request 这么一个处理的线程类。因为我们 submit 的时候提交需要提交一个实现 random 接口的一个线程，或者是继承所在的类。所以在这里我们继续。比如我们在 comment 下面再建立一个咱们叫做 execute 这么一个package。我在这里创建一个类，咱们叫做 message task for request detail，简写就是 message task for request。okay，咱们实现 runnable 接口。我们把润方法搞出来。


接下来还记得吗？我们在创建对象的时候一定要扔进去两个类，两个属性。这两个属性就是我们刚才所说的这个message。第二 message 还有一个我们的context，就是我们 native 的 channel handler context 对象全局的上下文 c t x。好把两个东西接收一下，我们可以用成员变量去搞出来。我们直接用一个private，它还有一个 private 的 channel handler context。好，在这里我就直接用 list 点 message 等于message， this 点 context c t x 等于我们的 c t x。好。搞定了之后，接下来我们继续来看看怎么去做。搞定了之后，在 run 方法里面做什么事情，你异步过来，我是不是就直接可以去做这个事情了？在这里我把 handle 的代码放开，直接可以写了。好，直接就可以去做 new 一个。它过来把我们的 message 就是 request 对象以及 context 加进来。


其实我们现在关于 net 的 handler 就是 server handler。已经搞定了，写完了，剩下的事情非常简洁，剩下事情就是在这里面去处理了。这里面主要处理什么？同学们想一想，问方法里面去对我传进来 message 去做解析。怎么去解析 message 里边？首先第二get，我们都知道它里边肯定帮我们去存储了，是这类型的字符串。首先我们要做一个最简单的判断，就是它的 modular 是不是能取到。 OK string 咱们叫做modular。还有我们再看就是我们的string，c，m， d 等于message。点 get c，n，d。好，有了这两个东西不是太简单了。


我们知道我们之前把 inworker table 已经存储到了我们自己的 scanner 包下面，有一个，对吧？已经有 inworker table 了，所以我们直接调用 inworker table，可以去 get 一个 inworker 出来，直接把这两个参数传进来，是不是得到一个反射对象？起码得到一个 inworker 是我们要做调用的。


得到了 inwork 以后，很简单，我们只需要去通过 inworker 点inwork，把它具体的参数传进去。它具体参数是什么？我们调那个方法，它需要有什么样的信息？这是调哪个方法？比如 module 是我们的 user 是一个c，m， d 是一个 save params，它指代的是谁？它指代的无非就是我们在这里边具体的 save 方法里边的参数。
其实我们都知道我们能取到实际的数据体吗？可以，因为我们之前在 message 里边已经定义了数据结构体是 body bytes，所以其实我们直接可以去取出来哈，很简单取我就直接。比如我把 string 的 data 取出来等于什么？等于 message 点 get body 第二，比如 two bit Ray，把它变成一个字节数组可以吧，这是最简单的方式，变成一个字节数组base。当然这里边我叫 b y t e 中括号。好了，其实我只需要把字节数组扔进去就可以了。所以我可以认为我们 seal 方法里边只需要有字节数组，这样字节数组我就知道怎么去做了。我们要 save 的内容，说白了这就是我的参数，很简单。


好了，接下来我们调完了这个方法之后，我们要得到什么？我们得到返回值。这个方法调完了结果之后，我们给它写回到我们的客户端，是不是逻辑就已经 OK 好了，接下来调完这个方法返回什么内容，我们来想一想具体应该返回什么内容。比如它的返回值，我们可以去做一层抽象。做一层什么抽象？比如做一个通用的返回值类型，这是不是可以的？这是也没问题的。但是在这里我们首先比如我们要对实际的 server 它的内容做一个处理。好了。假设说这个modular，它里边是user，这个是一个save，我们就拿这个方法去来看好它。


走到它了之后，我们其实实际的处理很简单，因为它我们都知道就是一个 user 了。我们直接可以取到 user modular，这个是老师之前生成的点 user 点pass，这是解析序列化的一个反序列化的工作。这个是非常简单没有难度的。直接把它做一个反序列化抛异常。我们直接 catch 住抛异常了。之后我们就打印一下就可以了哈。


里边解析出来就是一个 user 对象，我们可以在这里 user user 等于。当然这个是一个 probuffer 的 model 的user。解析出来之后，这里边的数据我是不是有了，之后我们可以去比如对 user 点 get user ID，加上我们可以自己去做处理 user get 什么？ username okay 去做处理。我这里写打印 user ID 是什么，加上这里边我可以写 username 是什么。非常简单。这样已经完成了。


其实我们使用 Nike 跟 spring boot 集成其实还有一点是比较头疼的，就是因为我们的业务handler，你比如这种业务handler，它上面肯定是没有交给 spring 管理。所以你还有一个问题就是你跟你的业务集成，比如你拿到了数据之后，你现在想调数据库，你是不是得调用一个service，这个 service 怎么去搞进来？你可能只能用 application context 去点 get bin 去那种硬编码去把它搞出来，没办法用那种 out where 的方式去把它自动注入进来。因为它是不在 spring 环境下，不在 spring 容器中管理的。所以这也是有一种硬伤。


所以我们还是建议你看我加这种注解的写法是不是非常简单，它本身就是一个service，如果有具体的 DAO 接到数据小区入库操作，你是不是直接一个 auto where 的，就是自动注入相关的 service spring，并也直接把它注入进来。你在这里可以非常无缝地去使用，取到业务数据，调 d o 到层去入库，这是非常方便的一件事情。



好了，我们现在拿到手了之后，接下来其实我们要里边定义一个object，这个不太好。其实我们想定义一些返回值，比如我们现在把它返回值也做一个统一的，通用的封装。在这里老师，我想封装一个，很简单，叫做result，我们可以叫做一个结果。好了，我也想把它放到哪里，把它放到 probuffer 下面。 OK 我们写个类，叫做result，result， data 都可以，你返回去结果它实际的内容它一定是序列化的，所以在这里需要有一个泛型t。 t 一定要实现 probuffer 支持的序列化的手段，它有一个叫做generated。然后 message 在这里。


注意上面这个是 Pro BUFFER 2 支持的，我们一定要用 V3 的版本， V3 版本是 PROBUFFER 3 才支持的。 PROFILE 3 里面用的是V3， PROBUFFER 2 用的是不带 V3 的。还是有区别的。我们想要去做什么事情？比如首先返回值结果。我们来看一看返回值都有哪些内容。我们还是要打开我们自己的message，它的 Pro buffer 定义返回，它肯定有一个叫做 result type 的东西，要么是成功，要么是失败，要么是返回 error 什么的。返回值里边还有body，所以其实从返回值的角度来讲，比较关键的两个东西就是你的返回值类型到底是成功了还是失败了，以及返回的数据是什么。刚才我们已经把返回的数据已经定义好了。这个泛型必须要实现 generated message V3，必须得是这种方式才可以去做返回，要不然可以去给一个异常。


好了，现在我们来定一下具体的另外一个就是我们刚才看到文档看到这个里边，首先它叫做 result type，其实我们直接可以取出来，咱们是 message modular 点 result tap。它好直接，我们可以去给它一个 result type。实际的类型我们就可以用范畴去搞了。


实际的内容，实际的内容我们叫做content。好了，接下来比如我们给它生成对应的 GASA 方法，没什么可说的，我们就直接通过 at data 的方式去给它生成 get set 方法。接下来比如我们给它传递几个比较有意义的参数，比如返回成功和返回失败。返回成功我们搞一个比如叫做通用的方法static。返回值类型一定是它，因为我们大家已经知道了一定是它。咱们叫做 result t，这是返回值的实际类型，我们给它起个名字，叫做 success 的方法。好了，假设这里边我需要传递，如果需要传递参数，就给他一个 content t 传过来就是t，我们实际传的内容就是content。


好，我们看一看这个东西怎么去定义。我们就直接result，这里面还得加方形 result 等于 new 一个 result 泛型带过来。既然用泛型，我们就带过来。你去把它对应的属性做一个赋值。比如 result 点 result type 等于既然这个方法叫做 SUCCESS 方法，就证明它已经成功了。所以我们直接可以用它点它，定义了一些对应的数据结构。 success result type 他哈直接好。


第二你看自己就会有success，因为我们已经定义好了，这个是在数据结构里面定义的，它有success，有fail，还有这个error。好了，接下来最后把这 contents 也做一个赋值点， set 什么content，重新变量 content OK 搞定了这个事情之后，我们再把我们的 result 去返回回去， OK 返回回去。这样一个最简单的返回值，带有参数就已经 OK 了，没参数就更简单了，就不需要赋值 content 了。所以你可以再写一个重载的方法，把参数去掉，把内容去掉，直接返回好了。这是成功。
我们来说一说失败吧。失败也很简单，失败都是大同小异。我把它 copy 一份，然后把写成failer， seller 也会有，我们大写，看着舒服一些。失败肯定返回 failer 这里边。把 content 也直接带过来。 result 返回，这是失败的方法。当然我们还有一个无参的，没有结果的。 OK 搞定。我们就定义这么 4 个方法，非常简单。好了，这个 result 类就是一个通用的返回类。通用的返回结果包装通用的返回结果包装类，好，在这里边这个类给它起个名字叫做result。好。搞定完了之后，接下来不是简单了吗？我们回到 service 里边看看我们怎么去实现service，我们来看一下，实现起来也是非常简单的。我们这里边是不是直接返回他了？返回什么我们不知道，我们暂时给他一个问号，我不知道，不确定，我给他一个问号也可以。同理，这里边也是一样的，直接返回一个不确定的东西，抛异常的时候是不是就返回一个，失败就可以了，我们直接如果抛异常，在这里边返回一句打印出来也可以哈。


在这里我们直接 return 静态类result，点 fail OK 也可以传结果，如果成功，我们直接返回result，点什么success，我是不是可以返回一个？只要是实现了什么泛型，只要实现了 generated message V3 接口的，只要它的子类，就都可以去作为反馈值。


其实很简单，我们的 user 这个类，它本身实现了 generated V3，就是 message V3 接口。所以我也可以干什么？我也可以创建一个返回回去，或者是我原封不动的给你返回去，成功了就返回，是不是也可以？这是没问题的。当然 user 你得提出来哈。 OK user 等于none，这里边把它去掉好。成功的时候我就直接原封不动地把数据写回给我们的 client 端就可以了。失败的时候就返回了一个错误，这是没问题的。


OK 好了，这个逻辑其实就已经搞定了，在这里我们再多打印一句话，叫做 save OK 逗号。同样的逻辑。我在这里因为我们不是去讲具体的业务，在这里老师只是给咱们同学把整体的技术框架搭建起来，具体你如果对业务感兴趣，你可以自己去在实际的工作中去尝试一下。其实我个人觉得哈，在我们去讲课程的时候，我是觉得给你去讲实际的业务没有什么太大的意义，因为实际业务特别复杂，而且每个公司的业务都是不同，你学习的肯定是这种技术解决方案和处理方案。所以在这里我们对于业务就不是特别关注了。


在这里我还是同样把代码 copy 过来， data 也拿过来，到时候我是为了让小伙伴们知道我们走的是不同的方法，在这里边我们叫做update。OK，成功失败。好了，现在这两个类已经搞定了。接下来我们再回到我们刚才所说的 inworker 这个方法。 inworker 的方法其实现在我们已经知道了它。 inworker 调完了之后，是不是就相当于我们刚才所看到的 user service？它执行完 save 方法或者是执行完 update 的方，它的返回值肯定是这个result，我们现在可以对它继续去往下去处理了。刚才我们卡到这了， result 好走过来。 result 要做一个cascade，就要做一个强转。得到了 result 之后，我们是不是就可以根据根据什么，我们其实就可以去把它写回去，因为我们有 CTX 对象，我们直接 CTX 点 write and flash 把数据写回去就好了。


怎么去写回去？在这里边我写回什么样的结构？你是响应，你永远是写回响应的信息。所以其实在这里我们可以再次的去封装一个简单的类。我管这个类，咱们叫做 message builder，它不一定是创建写回的封装，也可以是创建响应的封装，哈，这都是可以的。总之就是一个对 message 做构建的这么一过程。要不然你自己写完了之后，你自己还得在代码里面写死了，怎么去构建的。所以在这里边我们再次去加一个工具，就加一个辅助的工具类。这工具类的名字，咱们给它起个名字，叫做 message builder。okay， message builder 它的定位就是对于创建请求和回送响应的一个数据封装类。 OK 这就是它的定位。好了，搞完了之后，我们直接来写一个。首先我们看一看刚才我们碰到这个问题，是 response 我怎么去写回去，写回去。最终你肯定要我们来看一看哈。


我 right and flash 的时候，我们要写回去什么样的对象？ right and flash 写回去的对象，这个对象是不是能够被 put buffer 直接解析的，能够被我们的 client 端跟 server 端直接能够读出来的。所以你写回去的对象一定是什么？你一定是你自己的 client 端能够识别的。说白了，你写回去对象一定是包装成这样，一定是 message model 了。点 message 一定是 message 类，包括无论是请求还是响应，一定是写出或者是写回message。我对应着我的 client 端和我的所有端才能识别。所以在这里边我们就知道了。我们最终 write and flash 刷出去的数据一定是message。我们 Pro buffer 定义好的message，这样才可以。所以我们 master builder 它的定位就是在帮我们去创建请求和响应的message。好了，我们现在先写一写。比如它既然是一个公用的工具类，所以它肯定是 static 的。我们继续往下看。它返回肯定是一个message，这个 message 就是我们的 message module。


点message，我们叫做 get response message builder 或者是 get response message。简单写好，它需要传给我们什么样的对象？
我们对应着response，我们需要知道什么？首先你的 module type，你要写回去，写回给哪个模块我都不知道，肯定不行对不对？还有 t v i p e 还有你的 command 命令是什么？以及最关注的点，最关注点你的 result type 你的返回值是什么样子的？你的返回值就是我们的 result t y p e result type。


还有实际的 data 数据，我们可以说它实现了 generated message V3 实现了的data。 OK 搞定了。只需要这么几个参数，我就帮你去构建一个message。好，我把它往下拉。这样的我们来看一看应该怎么去做。我们来写一下。肯定是通过 message builder 去创建message，所以你一定逃不开message。


点儿 new 一个builder，我们之前都已经学过了的，它就是支持链式编程。我们 new 一个 builder 之后，我们直接点儿什么点儿set。还记得吗？我们协议里边都会有 c r c code。这个 c r c code 其实我们可以写静态的，或者是直接从。从什么我们直接写死了。 c r c code 我们自己随便去定义死。这是大家的标识。我写一个 private static final 的 c r c code 等于什么？当然它是一个硬弹类型，我们找到上面的有 c r c code 的，随便给它搞过来就可以了。


NET 003 的时候我们在做编解码，应该是 002 的时候我们再去做编解码。讲解的时候会跟大家说到有一个 structure 在 message header 里，我就把它拿过来用它就好了。两边对应上都是 c s code。好了，直接把它拿过来放到这里。当然我大写 c s code。接下来我去 set 什么。首先你要 set 它的 module type，就是 set module 是什么？ OK 这里边 model 了， set module 了。然后我们传进去。还有点 set 什么 command 又是什么？ C m d。还有是不是我们要点 set result type，就是它传进来。还有你要把数据放进去， set body side body，我们拿它直接拿过来，它是可以的，这样它肯定是报错的哈。


点 build 它，不是 brand build 这个东西，它直接可以转换，直接可以用一个 copy from 方法，它有一个 beat b，y， t e string 的点，叫做 copy from。它其实性能会很高的。我们 data 点 to beta array，好直接帮我去转回来，然后点 build 方法，直接创建好，这样我们直接 return 就可以了。也就是这种封装的类。其实感觉还是比较舒服的。就直接返回我的响应数据包装，就已经搞定了。响应数据包装了。搞定了。同时还有一些比较关键的，对不对你的响应信息肯定得 set 你自己的响应的。怎么说？我们在这里有一个比较关键的点，你的 message type set master type。我们都知道了，它就是什么，它就是response，是不是就可以写死了？因为本身来讲，这就是响应的 OK 搞定完这件事情，其实我们再往下看。


对应着我response，知道了我 request 是不是也非常简单。 request 我们可以直接拿过来叫get，叫做 request message。 request message 也需要这些东西，但是它不需要响应结果，它要响应结果没有意义。或者它的响应结果你直接存一个 OK 就可以了。或者你不给它都行，我可以直接写死了。响应的结果，我们就直接可以写死它。就是success。因为我的请求，反正我不关注，或者我不加它都无所谓。把它去掉。


我的请求首先需要一个 module command，还有实际的数据。 c s code 是固定的，要改成request，其他的不变， body 这些都不变。好了，其实我们现在对应的请求也已经搞定了，不知道大家能不能理解哈。这个是对应的请求的封装，叫做 get request message 请求封装，这个就是 get response message 响应封装。Okay。响应封装。


好了，搞定完了这件事情之后，我们的工具类也有了，直接用拿过来就可以去用。好。在这里很简单，我们直接 right and flash。我们用通用的类点 get response message 就可以了。直接写出去。首先 module 的它有了结果是什么结果，你就直接从 result 里去拿就好了。我的 result 里边是什么样的结果，我就取到什么样的结果就好了，没有什么可说的。我不知道小伙伴们能不能理解老师说的意思，我们直接在这里第二 get result type，最后 data 我写回去，最后这个 data 我们把我还是把它这样去写一下，因为我的屏幕不够大，所以跟小伙伴们来看一看。 data 肯定是 result 里边它的content，它才是真正的data，因为 content 才是什么generated。


message V3 好，整个现在目前逻辑就已经搞定了。我不知道小伙伴们到现在是不是对稍微有一点感觉了，我们都是封装成通用的类。好了，其实我们可以稍事休息一下，后面我们去把后一半部分的内容。现在你看我们现在有 request 的，刚才我们看到的，我把这个都关掉。我们现在有通用的叫做 message task for 


request，其实也应该有一个 message task for response，其实也会有的，我们不用去太着急。我们现在是把前一半已经封装完了消息发过来我的 server 端去直接提交到异步的线程池。提交完了之后去做处理。他怎么去处理的，具体就是他做解析，做回调，调完了之后再给我写出去实际的内容，这个流程应该是比较清晰的。我们这节课讲到这，因为下一块我们要讲一个比较有意思的东西，我在面试的时候经常会问的一个问题，到时候希望跟小伙伴们一起分享一下。好了，这节课到这，感谢小伙伴们收看

