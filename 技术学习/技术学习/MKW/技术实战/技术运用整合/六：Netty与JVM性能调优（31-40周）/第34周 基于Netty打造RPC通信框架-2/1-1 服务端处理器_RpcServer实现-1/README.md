---
title: 1-1 服务端处理器_RpcServer实现-1
---

# 1-1 服务端处理器_RpcServer实现-1

[image](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/9318b484-b833-4e5a-8048-86d849f3ca42/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664M6UJB6B%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T230036Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIG0cnIqjrRwZoIP8pmusRGw6xMGtNBHHXC%2F8XDNZjzKZAiEAmEWVeJKhoJpeszNX%2FzR%2BxeF%2BYNzyXiAr7jW8656loOoqiAQIxv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDPZz0qsqpqIf3GqHXircA%2FL4ZtUCZzYfi6oho2VjXvYfiRu%2Bmq5wcExujO5%2BHOzI8x9YGb%2FtQnUUSc9a1FVU%2FtZfVLiEUMwv9TSxeOwkboc3Hf4F98aceKDPbtio%2B%2BUFndauxc%2FXTNzJxMZzGDt%2BcNHHOMynjOGD3gYZguo1gpDZx4160t7YtaLHNtYPd8X6HNNAfe9LnVXNlQtLYEe7oMNhgobKmho8ojXsRURfEGlSjU7w4wV8OLjIQ6iaqV5sR1CdUj3i%2B25UvupRbAI4Bf7iH6Ce9H4muq8Xj%2BbEqNNqYEICZe4omWUwU0qkr%2BRgD0A3vrW1X%2B5NQ9HZXFyPVkk1LM64wAffjiRAAeeeBtEksPnD6s1OtmBa8ZQLKYjRND803AntDhjwwkr%2BvX9HVUjTDzppKjdW7hoX4i%2Ftdza7VB6iHv3MD7iYMP%2F8wb8e5VqVrwusf4PTMIn%2BmV90DyadfI3BdCkUyTAOQkq6q6BK%2FqNFnvt9vwwAWPJvY2hgTLIJCbKhxaR1zZh19Pq6nQj6xkJaIEGDJXqxgeGVor9Kmf4L2fhAdiq0BcRZx7t8z3TOuI5GwUAEvu7ivGOGNVROShcd0LSp%2F1Wep7blxWG5HH0dbBUmiRVRwtV7TXCxo4AKUH2rJkxwqZFFMMy3%2F9IGOqUBrZ3KNzZh9YDCRW5vOgcJbtEpNiC%2BPR98cY5ddffg4Ii3Jlv7BmdpPDpK52kBzzyUuc35sBqAP1R0H%2F%2BhbthMTIONnRvqcPvSXfCqO6zmhEgTfdkH096Hb45wEu6O7RzzI%2FmkrVbe8UgHEuZBuzak22p8oO%2FLzQ4R4lAvzQr3oAfV%2FNO9VjbdvI7lJzNac168b%2FCdUbdwT10yENZpsEerpwTjODOV&X-Amz-Signature=3ead49cbc3500a38ddb1a958706bd8d1c8ecc5d793b5e2d570c62700fe594267&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

简单的跟大家来回顾一下我们的 RPC client handler 里边主要这几个核心的方法。 channel read 0 就是读取数据的方法，我们把数据发送给 server 端，搜索端给我回送响应的时候， response 我们怎么去做处理对吧？

[image](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/933a3c7a-e171-48ed-8661-67a4325a2c72/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664M6UJB6B%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T230036Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIG0cnIqjrRwZoIP8pmusRGw6xMGtNBHHXC%2F8XDNZjzKZAiEAmEWVeJKhoJpeszNX%2FzR%2BxeF%2BYNzyXiAr7jW8656loOoqiAQIxv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDPZz0qsqpqIf3GqHXircA%2FL4ZtUCZzYfi6oho2VjXvYfiRu%2Bmq5wcExujO5%2BHOzI8x9YGb%2FtQnUUSc9a1FVU%2FtZfVLiEUMwv9TSxeOwkboc3Hf4F98aceKDPbtio%2B%2BUFndauxc%2FXTNzJxMZzGDt%2BcNHHOMynjOGD3gYZguo1gpDZx4160t7YtaLHNtYPd8X6HNNAfe9LnVXNlQtLYEe7oMNhgobKmho8ojXsRURfEGlSjU7w4wV8OLjIQ6iaqV5sR1CdUj3i%2B25UvupRbAI4Bf7iH6Ce9H4muq8Xj%2BbEqNNqYEICZe4omWUwU0qkr%2BRgD0A3vrW1X%2B5NQ9HZXFyPVkk1LM64wAffjiRAAeeeBtEksPnD6s1OtmBa8ZQLKYjRND803AntDhjwwkr%2BvX9HVUjTDzppKjdW7hoX4i%2Ftdza7VB6iHv3MD7iYMP%2F8wb8e5VqVrwusf4PTMIn%2BmV90DyadfI3BdCkUyTAOQkq6q6BK%2FqNFnvt9vwwAWPJvY2hgTLIJCbKhxaR1zZh19Pq6nQj6xkJaIEGDJXqxgeGVor9Kmf4L2fhAdiq0BcRZx7t8z3TOuI5GwUAEvu7ivGOGNVROShcd0LSp%2F1Wep7blxWG5HH0dbBUmiRVRwtV7TXCxo4AKUH2rJkxwqZFFMMy3%2F9IGOqUBrZ3KNzZh9YDCRW5vOgcJbtEpNiC%2BPR98cY5ddffg4Ii3Jlv7BmdpPDpK52kBzzyUuc35sBqAP1R0H%2F%2BhbthMTIONnRvqcPvSXfCqO6zmhEgTfdkH096Hb45wEu6O7RzzI%2FmkrVbe8UgHEuZBuzak22p8oO%2FLzQ4R4lAvzQr3oAfV%2FNO9VjbdvI7lJzNac168b%2FCdUbdwT10yENZpsEerpwTjODOV&X-Amz-Signature=8e548fe900ef562c43c0d4c62c1c29ffb021f4bad78ebb658179bb2468daf713&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

还有 active 通道激活的时候，当然肯定是先去做registry，再去做active。这块我要先跟小伙伴们来说清楚，因为你肯定是先注册了之后你都能够拿到具体的channel，有了 channel 之后再激活的时候，你的 channel 才能去连接具体连接哪个 server 端对吧。你连接 solo 端的时候，你才能知道我们的 remote beer 就是你远程连接的 socket 



address，你才能知道这个是我们之前大家熟悉的，其实我们已经编写完了。然后就是 init channel 以及 close 方法。这是我们之前跟大家都已经完成了，可能以内的 channel 还没有去做。当然我们后面再说。我们回过头来，简单跟大家把对应的 RPC client handler 这个代码简单梳理一下，你就知道了。


首先是registry， registry 的注册的时候，我们拿到了 channel 去缓存了，本地引用了一下。 active 的时候，我能够去通过 channel 知道我具体到底跟哪个远程的地址进行连接了，所以我能取到它的 remote address。我也本地在这重新变量引用了一下。


接下来就是核心的 channel read 的 0 方法，就是真正做处理的。其他的就是 close 方法对吧？ OK 这个代码应该没有任何问题。其实我们在这里边注意，老师在这里，在这我提前写好了。之前时间是一个object，但是现在我直接换成了一个叫做 RPC response，没问题。我不知道小伙伴们能不能理解。我们请求的时候，请求的时候我们传过去的是 r p c request 对不对？我们响应回来的时候，服务器端给我的响应肯定是 r p c response，我们肯定 channel 在 read 0 读取数据的时候，读取的对象肯定是 r p c response，这是没问题的。所以之前我们在泛型里面写的object，可以把它直接改成我们的 RPC response 了。


OK 好了，对应着我们的 RPC client handler 代码就很简单的就讲完了，因为我们其实已经实现了。接下来我们继续回看一下我们整个的流程。再往下。其实我们要做的事情就是 RPC server 服务端的编码了。 RPC 搜了服务端的编码，其实是有三个方法。第一个方法是 star 的方法，这个方法其实虽然代码量稍微多一点，但是它是最简单的。我只能说 close 跟 star 的方法是最简单的。

[image](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/ae3d037a-30cc-40bc-b57c-5834707763bb/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664M6UJB6B%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T230036Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIG0cnIqjrRwZoIP8pmusRGw6xMGtNBHHXC%2F8XDNZjzKZAiEAmEWVeJKhoJpeszNX%2FzR%2BxeF%2BYNzyXiAr7jW8656loOoqiAQIxv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDPZz0qsqpqIf3GqHXircA%2FL4ZtUCZzYfi6oho2VjXvYfiRu%2Bmq5wcExujO5%2BHOzI8x9YGb%2FtQnUUSc9a1FVU%2FtZfVLiEUMwv9TSxeOwkboc3Hf4F98aceKDPbtio%2B%2BUFndauxc%2FXTNzJxMZzGDt%2BcNHHOMynjOGD3gYZguo1gpDZx4160t7YtaLHNtYPd8X6HNNAfe9LnVXNlQtLYEe7oMNhgobKmho8ojXsRURfEGlSjU7w4wV8OLjIQ6iaqV5sR1CdUj3i%2B25UvupRbAI4Bf7iH6Ce9H4muq8Xj%2BbEqNNqYEICZe4omWUwU0qkr%2BRgD0A3vrW1X%2B5NQ9HZXFyPVkk1LM64wAffjiRAAeeeBtEksPnD6s1OtmBa8ZQLKYjRND803AntDhjwwkr%2BvX9HVUjTDzppKjdW7hoX4i%2Ftdza7VB6iHv3MD7iYMP%2F8wb8e5VqVrwusf4PTMIn%2BmV90DyadfI3BdCkUyTAOQkq6q6BK%2FqNFnvt9vwwAWPJvY2hgTLIJCbKhxaR1zZh19Pq6nQj6xkJaIEGDJXqxgeGVor9Kmf4L2fhAdiq0BcRZx7t8z3TOuI5GwUAEvu7ivGOGNVROShcd0LSp%2F1Wep7blxWG5HH0dbBUmiRVRwtV7TXCxo4AKUH2rJkxwqZFFMMy3%2F9IGOqUBrZ3KNzZh9YDCRW5vOgcJbtEpNiC%2BPR98cY5ddffg4Ii3Jlv7BmdpPDpK52kBzzyUuc35sBqAP1R0H%2F%2BhbthMTIONnRvqcPvSXfCqO6zmhEgTfdkH096Hb45wEu6O7RzzI%2FmkrVbe8UgHEuZBuzak22p8oO%2FLzQ4R4lAvzQr3oAfV%2FNO9VjbdvI7lJzNac168b%2FCdUbdwT10yENZpsEerpwTjODOV&X-Amz-Signature=7ac06c9c5b97e7c7f7f26608ea8e9402237113aa69145faaaf03bec3a3073be5&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

启动服务。启动服务需要做什么事情？是不是通过我们 net solo 端的编程模型把它启动起来就好了，让他去执行我们的 r p c server handler，真正的去执行服务端的业务执行器就好了。第二个方法是我们整个 r p c 框架里边算是比较有难度的，你可能想不明白的一个地方，很难捋清楚，但是我期望我能够讲清楚干什么事情。他做的事情叫做 register processor。注册什么内容？反正不知道我注册什么内容，我只知道我要注册的对象叫做 provider config。我就只知道我要把注册的东西，我要放到一个 map 里边。我要注册东西放到 map 里边，肯定有对应的 key 和value。 key 是什么？我说这个 key 它实际的内容就是 provider config 里边，它有一个属性，叫做接口。 value 是什么？ value 就是 provide config 里边它实际的引用逻辑程序。这个指的是什么概念？接下来就跟小伙伴们一点点说明了。最后 close 方法就很简单了，就把你 start 你启动了什么资源close，你给他释放就好了。


我们来编写我们的r、 p c server 程序。在这里我们新建一个 RPC server 的包。好，我们去 RPC server。有了 RPC server 之后，我们来一起写一写代码。首先， RPC server 其实如果需要它有一个 server 的 guess 好，因为 RPC server 我们都知道它是一个 NET 的 server 端。 NET server 端肯定得需要两个非常关键的东西，一个是 boss group，还有一个是 worker group，对吧？我们一个用于接收我们的连接的，叫做 boss group，等于 new 一个我们的 NIO event loop group。


好，还应该对应着有一个具体实际处理逻辑的，咱们叫做 worker group 好了，这两个 group 肯定是必不可少的。我们去写它的构造方法，叫 public 给我传进来的一个地址对吧？给我传进来的地址，我去做一个this，点 server address 等于 so address 就可以了。比如我调用一个 start 方法，这个 start 方法就是我们刚才看到的 start 方法。还应该有一个什么 public 的。你看我们刚才逻辑有一个 start 方法，是不是还有一个什么叫做 register processor 方法，还有一个 close 方法。我们先把这 3 个方法定义好哈。 why register pro cessor 方法？这里面传什么我们先不关注，我们先把方法写到这儿。最后一个就是 public white close 的方法。好了，现在我已经把这定义好了，接下来我们就开始实现。


首先第一个方法非常简单，就是我们 server boot sharp，这是我们的 NIO 编程模型。 server boost shop 等于 new 一个 super boost shop，这都不用说了。 super boost shop 里边去做 group 绑定两个线程组对吧？这两个线程组一个是我们的 boss group，还有一个是我们的 work group。接下来 channel 绑定的肯定是我们的 NIO server socket channel 点class。


接下来你比如它需要做一些 optional 配置对吧？比如我们在这里边 channel option 有一个比较核心的配置，它叫 so back log，我们一般我在这设置 128 或者是 1024 都可以。还有其他的一些 option 你都可以配哈。比如我们写 channel 可以配一个叫child，我没有准备去掉哈。


有同学可能说老师， so back log 是什么东西？如果熟悉 TCP 你就知道 TCP 内核里边有个概念，就是我们的 SNC 队列和 SAP 的队列对吧？ s n c 在握手建立连接的时候， s n c 第一次握手的时候会把连接放到 s n y c 队列里，给我回送什么？给我回送响应。第二次相当于回送的时候有一个加 a C k，加上 n s n c package 包给客单端收到了之后，第三次再发起握手对吧？好，这就是三次握手原理。第三次的时候，它其实本质上是从 s y n， c 的队列里边把连接取出来，放到 accept 队列里，这两个队列它的之和就等于它 BIC log 属性，我们给它设置 1024 一般就够了。


还有其他的配置项上就是一些优化的，我们先不说，先加上我们的 chair handler。 chair handle 在这里我们可以直接去 new 一个 channel in italizer 对吧？它这里面传一个我们的 socket channel，就是我们的 net socket channel。我们把具体的实现方法搞定。这里边我们要写什么内容，同学们想一下。这里边其实你就可以把之前我们克兰端里边怎么去初始化的逻辑完全 copy 过来，稍微改一下就可以了，是不是这样对吧？好，我又改什么逻辑？首先第一件事情当然逻辑前后顺序其实无所谓，但是我期望小伙伴们你要把前后顺序按照顺序写下来，这样能更好很清晰对不对？先去通过发过来数据包，我们先走什么？先走 less field base 的 frame decoder 截取出来前四个长度出来。这种东西先做一个对应辅助的一些 handler 先。肯定是 decoder 解码，解码肯定是什么对象，我们服务器端接收的是 request 对象对不对？所以这要换一下。服务器端接收的绝对是 request 对象，客户端接收的是 response 对象。服务器端写出的就是我们的Encode，编码的时候肯定是 response 一下，在这要改一下，这就 OK 了。


我们的 RPC server handler，他肯定不是 client handler， RPC solo handler。我们来写一下。在这里我们创建一下哈。创建一个class，叫做 RPC service handler solo handler。我们只需要继承什么？只需要继承一个叫做 simple channel 引爆的handler。这个范型我们写什么？肯定是 RPC 的 request 对象对不对？因为我们服务器端接收的是客户端的一个请求， channel read 0 对吧？我们叫做 r p c request，搞定对应的 r p c server handler。我们先放这儿，认为他待定，后面再去说。


回过头来，现在搞定了这个事情，接下来怎么说？接下来就是直接启动类建立连接。是不是 server address 都有了？我们直接可以去 server address 点split，我们按照冒号去分隔，找到他的 IP 端口号，是不是它会返回一个 string 数组？我们来临时的去叫一个array， string host 等于 array 数组，取第 0 个对吧？第一个就是我们的，比如是 Int 类型的 point Intake 点 pass Int 就是 array 数组的第一个元素对吧？好了，搞定了这个事情，我们知道 ip 地址了。很简单，接下来我们直接去。因为是服务器端，所以我们直接调用 slob shop 点 founding 就启动我们服务器端funding。要有一个方法，就是把 i p host 跟 point 传进去，调一下 s y n c。最后 s y n c 它要抛异常，我们往出。抛出一个 interrupted exception 在这里， r b c 搜也要抛异常，再往出抛一个 interrupted inception 就可以了。


好了，接下来绑定的方法。最后 a 新口同步 single 同步返回一个 channel future。我们可以针对于 channel future 去加一个回调的监听。可以吧，咱们叫 channel future。我先把它引进来哈。这是 Nike 的 channel future。 channel future 点 add listener，要 new 一个。什么？ new 一个 channel future，它的 listener 把它做一个实现complete。是不是？在我们搞定了这个事情之后，如果 if 它 channel future is success，表示连接成功了，是不是？第二 is success 可以打印一句话，是不是？打印一句什么话？我们可以加一个 s l f g 打印一个日志。


第二 info 就是我们的 server success bonding to 加什么？我们的连接地址就是它。 else 我们写一个不是 success 了，我们叫 fail bound into。我们去往出抛一个异常throws， throw new 一颗 section 就可以了。具体的异常信息我们可以叫做 server start bell。逗号 Cos 原因是什么？原因其实我们可以从 future 回到函数里去取得Cos。


好了，异步加一个监听应该没什么可说的。如果你想去做一个同步阻塞等待，你可以在下面去写上你自己的逻辑。比如我们有了 channel future，它这是加了个监听，是不是同步等待。我们可以加一个点 await wait。方法是不是可以去传等待多长时间。比如等待 5 秒钟 time unit 点 million seconds 是第二个。搞定了之后， await 的时候，我看一下点进去，它还会抛出一个 interrupted 的 exception 对不对？打断异常。其实我可以在这里 try catch 把刚才的代码放进去，在这里边我可以去把异常拿过来。 catch 住在这里可以去加一个error，这些都可以。
log 点 ERO 2。好，这什么，我说start。我们的 RPC 出现异常的时候，我们是 repeat RPC o corner interrupted instruction，可以吧？ interrupted 然后逗号把我们的异常信息加上去。yes，这里是e。好了，这就是一个非常简单的逻辑哈。如果 await 它真正成功的时候，我在这里，你要不嫌麻烦，你也可以再判断一下。这倒无所谓，反正同步阻塞，等着吧。


第二 is success。我们在这里的时候，我们真正的是不是？你也可以打印这句话，当然只是监听成功的时候打印这句话。我真正await。如果发现 channel future 这两个其实是异步的，这是同步的，你搞一个就行。我在这里两种都写上了哈，无所谓了。我可以写一个叫做 start RPC 是successful。可以。好，这样就可以了。我们现在整个 start 方法都已经写完了，是不是？这就是一个非常非常标准的 server 端的 net 的 n i o 程序，就是我们的 start 方法。好，接下来我们看一个更简单的 close 方法。 close 方法无非就是把我们的资源该关闭的关闭，就是 BOSS group 跟 work group 去给他杀到优雅，关掉沃克group，点 3- 6 亚关机是吧。


好了，搞定。这也搞定了。接下来我们来看一看最关键的方法。其实没多少行代码，但是它是属于最关键的。表示注册叫做 registry processor，叫做程序注册器。这个东西主要是注册什么，跟大家去详细的讨论一下。说一说这块内容。我们回过头来分析一下我们的 RPC 框架。在这里边我们首先看一下这幅图程序注册的方法。首先它需要有一个map，它这个 map 里边 key 是什么？ key 是一个接口，名称value。什么 value 是一个引用逻辑程序。首先有这么一个类，看见了吗？叫做 provider config。在这里我先把这个类先搞出来，我们再新建一个package，这叫RPC，我们叫做config。
第二 provider 好了，把它创建出来，这是一个class，咱们叫做 provider config。好， provider config 里边必然会有两个非常关键的内容，一个内容是什么？当前接口有两个比较关键的属性，一个是接口名称，还有一个是程序对象。为什么？我们来看一下引用逻辑程序哈。还有一个接口名称，因为我们在注册的时候，必须 key 是接口名称，而且是 provide config，它的 key 接口名称 value 也是 provider config 下面所有的一个引用逻辑程序。所以不管怎么说，我 provide config 类里边必须有这两个属性。好了，我现在问同学说为什么我们现在需要这么一个类，其实需要它的原因其实你可以不用它。但是后面如果小伙伴们想去说我 RPC 框架，想要跟我们的 spring 去整合的时候，你最好有这么一个 provide config 类，就比较 easy 了，比较轻松了。


在这废话不多说，我们先画一幅图，帮助小伙伴们去理解我们的 provide config 到底是一个什么东西。还有帮助小伙伴们去理解 register processor 他到底要干什么事情。


首先再新建一个流程图，这也是对应我们的 client 端程序，是我们的 server 端程序。现在我们当前要做的事情就是我们的 client 端肯定是发起一次 request 请求， request 请求发起到我们的 server 端，到 server 端哪谁去接收？当然这里我要写一下，这是我们的 client 端， client 端也相当于服务的调用方，就是我们的consumer。这边是不相当于我们的服务提供方，是我们的 server 端，也就是服务的provider。这里都毋庸置疑，对不对？肯定都没问题哈。好了，我把它字体大一点。我发起一个请求过去到 server 端。 server 端他要做什么事情，他肯定得去跟把请求解析，解析完了之后去调用对不对？我们知道 RPC 是做什么事情， RPC request 他要给我们什么样的信息？小伙伴们还记得 request 对象里边的内容吗？我们之前已经封装过我们的协议，对不对？肯定有 request ID class myself，包括 parameter types 以及 parameter 思对吧？请求里边肯定包含什么类信息？就是类名称的信息方法名称参数列表的类型，以及参数。具体实际的参数列表。

[image](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/af53507e-71d1-4742-9276-e78c501f2bb9/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664M6UJB6B%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T230036Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIG0cnIqjrRwZoIP8pmusRGw6xMGtNBHHXC%2F8XDNZjzKZAiEAmEWVeJKhoJpeszNX%2FzR%2BxeF%2BYNzyXiAr7jW8656loOoqiAQIxv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDPZz0qsqpqIf3GqHXircA%2FL4ZtUCZzYfi6oho2VjXvYfiRu%2Bmq5wcExujO5%2BHOzI8x9YGb%2FtQnUUSc9a1FVU%2FtZfVLiEUMwv9TSxeOwkboc3Hf4F98aceKDPbtio%2B%2BUFndauxc%2FXTNzJxMZzGDt%2BcNHHOMynjOGD3gYZguo1gpDZx4160t7YtaLHNtYPd8X6HNNAfe9LnVXNlQtLYEe7oMNhgobKmho8ojXsRURfEGlSjU7w4wV8OLjIQ6iaqV5sR1CdUj3i%2B25UvupRbAI4Bf7iH6Ce9H4muq8Xj%2BbEqNNqYEICZe4omWUwU0qkr%2BRgD0A3vrW1X%2B5NQ9HZXFyPVkk1LM64wAffjiRAAeeeBtEksPnD6s1OtmBa8ZQLKYjRND803AntDhjwwkr%2BvX9HVUjTDzppKjdW7hoX4i%2Ftdza7VB6iHv3MD7iYMP%2F8wb8e5VqVrwusf4PTMIn%2BmV90DyadfI3BdCkUyTAOQkq6q6BK%2FqNFnvt9vwwAWPJvY2hgTLIJCbKhxaR1zZh19Pq6nQj6xkJaIEGDJXqxgeGVor9Kmf4L2fhAdiq0BcRZx7t8z3TOuI5GwUAEvu7ivGOGNVROShcd0LSp%2F1Wep7blxWG5HH0dbBUmiRVRwtV7TXCxo4AKUH2rJkxwqZFFMMy3%2F9IGOqUBrZ3KNzZh9YDCRW5vOgcJbtEpNiC%2BPR98cY5ddffg4Ii3Jlv7BmdpPDpK52kBzzyUuc35sBqAP1R0H%2F%2BhbthMTIONnRvqcPvSXfCqO6zmhEgTfdkH096Hb45wEu6O7RzzI%2FmkrVbe8UgHEuZBuzak22p8oO%2FLzQ4R4lAvzQr3oAfV%2FNO9VjbdvI7lJzNac168b%2FCdUbdwT10yENZpsEerpwTjODOV&X-Amz-Signature=2ac600abce16f6da5743e32af3972dbc4efe796196ccd45379b870d3cdf185f3&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

我们的 RPC 是干什么事情？我们的 RPC 不就是把这些内容封装成一个 request 请求给我们的 server 端？我们的 server 端要做什么？我们 server 端其实就是这有一个执行器executor。执行器需要通过这些信息能知道什么，能知道我们要执行它。其实程序执行器要执行的一件事情是什么？无非他要做的事情就是我要知道你这个请求它到底是远程调用哪一个，远程调用执行哪一个类，下面的哪一个方法我把它最大化。


根据他给我传的这些参数，我能找到是不是应该我是一个服务的提供方，我提供了好多服务，比如我们提供了 user service 服务，我们提供了 hello service 服务等等，是吧，好多 service 服务都是我们提供的。当然我们这些服务我们肯定在 server 端来讲，我们是有具体实现的，百分之百是有具体实现的。
我暴露给什么？我暴露给 clan 端的，只是我的接口对不对？我把 user service 它的接口，以及我们的 hello service 它的接口，也就是我们后面可能会有注册中心对不对？我们再搞一个东西，是不是我们都知道学过double，就学过 RPC 框架，你肯定会知道一个 registry 这么一个轨， registry center 这么一个东西注册中心

