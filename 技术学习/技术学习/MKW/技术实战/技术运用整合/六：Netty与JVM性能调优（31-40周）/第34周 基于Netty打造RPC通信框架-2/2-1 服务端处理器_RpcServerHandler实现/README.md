---
title: 2-1 服务端处理器_RpcServerHandler实现
---

# 2-1 服务端处理器_RpcServerHandler实现

[image](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/93fef451-aea0-4dcc-910d-2ec4b9a19ca3/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466X2Y3PKT5%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T230044Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCICKSrtm804T0YhNuZ5WPGSkZex3KVhbdFIuFKvhgiYl4AiA0G%2FDc6fsjVskepdSfiRwATa6rRBgvNIHY9aHFabwUcyqIBAjG%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIM97xIdQLajb4hf8JcKtwDfMMm2d1G0tLg4V1ekRb0bwhTAjm3ZxJe%2BB6N%2B9td2Ii9G4AOgBl2mKsELCIWOcze%2BR8I6iZ0iod%2BqYWhhLhfzyRcal%2BELGd18YpNtfSkyMbBi9u0EFZlDVirfW5Q%2BasFrGK8JbZBl4piv55wvHNbvyI%2FCHMU%2FLAIfXyuOqdDIGtFb8OEOZHpJv9pnnAzztweGxQm7hqZEmmxpSu8%2F6mScWlUugq%2FN6rqdZhAeCenR4xa0YqMhoPL7qc%2FMkl6oto1UyA39rBEIg7HeeeYTaDChpqArA6HLvx7tPIq6yGChazOqepEgfcI6ARbtlUtmyq0DHE%2FG4Dgesvl5HhEztsffWi5l99%2FIoQ%2Fil1h0QjRqFHOYAcPAkBCR9ViFofpsrkV1AvKkxYIunHMcrTGYvjIFy%2BCLkdqmfl5IOxZBbs1jEPGMEDrX97Fvb7q6WCCZo0gUxEnMgs5Sm7oX8UR%2Bzt11gR0BhswX4GS2dGGNRPfNzU6ik9voDMozMpHFuzmKyeJRBIByVVXgg3NMPZFK%2FhGAEEhCAfKEzXOB1r0qNGSG3tg7EsMVDAiGaW0LwABLUoDWlOYMaUbzIB1%2BV20FLIjAAxtyKKfIjG1fGp%2BYk9n56wgsY8R%2FVGk2%2BL7jgEwgrv%2F0gY6pgGQMndkO7Kj45cRP5VZOpYdhvoGu8qrtANGZTCG9K%2FSiyy5a9FMcZFmLWMs1v9bbWeDyHJaK4s1Jmz4ZewYW96%2Bm5A1Ea36325EjPTp8%2FG7Fp8z12QqAPumZsvpp5lGUIgs8VIcuCxXXNTEbsZUbkdLfn66n7MVAucDlSRMKAg060JvxYv07GlvfX2kt9wMZxAceny0NgSDbyV%2FOuFaIdZQh7DERTkt&X-Amz-Signature=8006cf3f118d4b8726d3933f5bbd38711a6cca0fde4c24ae132a92caf04ee05d&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

节课其实我们已经讲完了 r p c server 端这节课，我们来主要来梳理一下我们的 r p c server handler，也就是我们客户端请求过来我们的服务器应该怎么去做处理。首先 RPC 搜 handler 里边提供了三个方法，是我们比较关键的。第一个就是初始化方法，就是 RPC server handler 初始化的时候，我们上节课其实也做了，无非就是把我们自己所注册的 handler map 去做一个引用，其实就已经足够了。

[image](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/df3aacdb-8e2d-4f08-bc62-44c5ae48b726/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466X2Y3PKT5%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T230044Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCICKSrtm804T0YhNuZ5WPGSkZex3KVhbdFIuFKvhgiYl4AiA0G%2FDc6fsjVskepdSfiRwATa6rRBgvNIHY9aHFabwUcyqIBAjG%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIM97xIdQLajb4hf8JcKtwDfMMm2d1G0tLg4V1ekRb0bwhTAjm3ZxJe%2BB6N%2B9td2Ii9G4AOgBl2mKsELCIWOcze%2BR8I6iZ0iod%2BqYWhhLhfzyRcal%2BELGd18YpNtfSkyMbBi9u0EFZlDVirfW5Q%2BasFrGK8JbZBl4piv55wvHNbvyI%2FCHMU%2FLAIfXyuOqdDIGtFb8OEOZHpJv9pnnAzztweGxQm7hqZEmmxpSu8%2F6mScWlUugq%2FN6rqdZhAeCenR4xa0YqMhoPL7qc%2FMkl6oto1UyA39rBEIg7HeeeYTaDChpqArA6HLvx7tPIq6yGChazOqepEgfcI6ARbtlUtmyq0DHE%2FG4Dgesvl5HhEztsffWi5l99%2FIoQ%2Fil1h0QjRqFHOYAcPAkBCR9ViFofpsrkV1AvKkxYIunHMcrTGYvjIFy%2BCLkdqmfl5IOxZBbs1jEPGMEDrX97Fvb7q6WCCZo0gUxEnMgs5Sm7oX8UR%2Bzt11gR0BhswX4GS2dGGNRPfNzU6ik9voDMozMpHFuzmKyeJRBIByVVXgg3NMPZFK%2FhGAEEhCAfKEzXOB1r0qNGSG3tg7EsMVDAiGaW0LwABLUoDWlOYMaUbzIB1%2BV20FLIjAAxtyKKfIjG1fGp%2BYk9n56wgsY8R%2FVGk2%2BL7jgEwgrv%2F0gY6pgGQMndkO7Kj45cRP5VZOpYdhvoGu8qrtANGZTCG9K%2FSiyy5a9FMcZFmLWMs1v9bbWeDyHJaK4s1Jmz4ZewYW96%2Bm5A1Ea36325EjPTp8%2FG7Fp8z12QqAPumZsvpp5lGUIgs8VIcuCxXXNTEbsZUbkdLfn66n7MVAucDlSRMKAg060JvxYv07GlvfX2kt9wMZxAceny0NgSDbyV%2FOuFaIdZQh7DERTkt&X-Amz-Signature=427d4f1d20f7a55f231f92da19ae38f0c5f6fb7d845e0c82840e882ebeb5cd24&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

第二一个方法是比较关键的，叫做 channel read 0。第三个方法就是我们抛异常的时候，我们可以去把资源去做一个释放关闭。其实这节课最核心的点就在于我们的 channel read 0 应该怎么去实现channel？ read 0 无非就是我们读取客户端的 request 请求，去解析这个 request 请求。在这里我们去得到了一个 request 请求之后，对于 handler 肯定是 worker group，就是 net 的 server 端肯定分 boost group 跟 worker group。 worker group 肯定是要异步的去做处理，而不是要阻们的 worker 线程。所以我们一定会要一个此外的 pool excuter 去异步的去提交作业，去做实际的处理。


实际处理对 handler 进行一个解析，比如我们去解析我们自己的 request 请求的class， name 等。我们去解析我们 request 里边的method，包括我们去做真正的 inwork 调用，到底是 g d k 的 invoke 还是我们的 c g library？ invoke 都可以，在这里边 g d k 就用反射去做。 c g library 里边我们可以用对应的 fast class 去做一个类似反射的这么一个调用。


接下来我们调用成功了之后，我们肯定得去把结果返回给我们的 Clang 端，我们去封装我们的响应结果。在成功的时候我们怎么去封装响应结果，以及在失败的时候我们怎么去封装响应结果。最终我们在这里面其实可以去加一些调用完成之后的一些前置后置处理器。白了我们可以去做代理相关的一些逻辑。OK，在这里老师只完成一个后置处理器，如果小伙伴们要需要，你可以去完成一个前置处理器，具体怎么去处理看你自己怎么去实现了。


好了，这个就是我们整个的 r p c server handle 的里边的一个方法。的这么一个介绍，接下来我们就进行编码就可以了。我们来打开具体的开发工具，我们把之前的都关掉。我们来看一下我们的 r p c server handler。我们最大化。其实上节课老师已经把步骤都已经放到这，我们就开始去实现就好了。


首先第一点，我们 handle 的 map 肯定是引用进来的，初始化的时候肯定要引用进来。接下来第二点就是我们肯定会有一个异常的方法，异常的方法我们在这里边可以去直接写，抛异常的时候释放资源哈。这里面一共三个方法，第一个是勾的函数是我们的 channel read 0。还有抛异常的时候，我们可以先把抛异常的时候先写出来。 wide 叫做 Excel custom，这里边肯定是一个 channel handler context，对象是一个c，t，x。还有抛异常的时候，他会给我一个throb，是一个class。OK，这个方法是我重写的事实。


小伙伴们你会发现，如果你真正的去阅读过 net 的底层代码，你会发现其实 native 里边所有的 track catch，它都是用的什么，它都没有去用exception，它用的都是slowable。其实小伙伴们我们可以随便点进去看一下哈。比如我在写代码的时候，我会把一些如何去写代码的一些细节教给小伙伴。比如我们来看一看 event loop group，就是 n i o event loop，这个是一个比较核心的类。


其实你可以看一下它里边在做 try catch 的时候，往出抛异常的时候，如果比较细心的小伙伴，你会发现它所有的异常，最外层抛出去的就是Throba，当然这个里边它还是得往外抛哈。往外 catch 基本上它是能用 throttle 的地方都会用throttle。具体上面 catch exception 它逻辑他可能是要做，这个叫做 rebuild selector，这是做什么事情？这块可能是他要去解决。


有一个GDK，有一个昆仑群的bug，就简单跟大家说一下，它是做了一个 g d k 功能群 bug 去做处理的，所以它这里边直接能 catch 住，不会出现snowball，它这里面直接就是 catch 了。 exception 往下去找你看，他基本上能去做的都是用 snowball 去 catch 住的。这个说明什么问题？说明其实我们在写代码的时候，就算是你在实际的去做业务处理的时候，我建议小伙伴能用 throba 的尽量用throba，不要用exception，因为有的时候 exception 兜不住，但是我们的 throwable 肯定能兜得住。在这里就是老师的一点经验之谈。我们去做一个注解。在这里打一个 log l 叫做server，已经抛出了我们的 exception 了，就是我们的cost。cost。什么叫exception？我们的throttle。具体的信息我这样去写，直接加上我们的 Cos 就可以了。


我们做完这件事情之后，我们把连接关闭就好了，哈，再close，OK。这就写完了。对应的抛异常的方法，重写的。异常处理关闭连接， close OK。其实我们现在来回过头来看最核心的 channel read 0。刚才我说了，我们所有 net 的 server 端，它都尽量不要阻们的 worker 线程。我们尽量都要去自己去做一个线程池去做处理。我们写一个线程池，像这种东西它都是 Java 里面最基础的东西，因为有的时候老师在面试的时候，我不会去问一些比较复杂的东西，我就问一些比较简单的线程池，它的线程池里内部的实现是怎么去实现。线程池里边它的状态里边它是用一个 Int 类型，一个 32 位的字节表示的什么？高 3 位低 29 位，它表示线程状态和key。它都是什么含义？线程池里边它的生命周期。


线程池的一些模型。它线程池里边有一个 worker 对象，小伙伴们如果知道 worker 对象里面它是实现了a， q s，就是abstract， syncodescine 那种东西。有些比较基础的内容，我还是希望小伙伴们多去看一看，具体的相关博客也好，或者是你自己去浏览一下他的源码也好。对于线程池，比如它里边有 4 种拒绝策略，系统直接拒绝，还有那种丢弃最老的，我们去扯多了哈。我的意思就是很多基础的东西，我希望小伙伴们一定要基础，要掌握得非常非常的牢靠。 6553565536 现在我们已经把线程池搞出来了，是不是把线程池搞出来之后，我们要做的事情无非就是异步的去提交我们的任务，让它不阻们的worker。线程

池就是 event loop group 那个东西不阻塞怎么去做，直接去调它的。怎么样？ execute 方法好？其实现在又一道面试题来了， execute 跟 submit 有什么区别？有些人说老师， submit 它是有返回值的，有个 future 对象，它内部使用的 future 模式， execute 是没有反馈值的。其实这只是一个最简单的逻辑。


其实你可以点到 submit 或者 execute 里边去看，你看submit，它里边也是做execute，只不过是一个 future 的模式， submit 它在出现问题的时候，它跟 excuse 是有区别的。我们去找到具体的 excuse 方法， execute 方法就是父类的方法了，哈，再往上去找 executor service 里边它会有对应的submit，它会返回 future 它的父类。我们来再往上搞，应该还是在上面。在 executor 它有 execute 方法， exsuit 是wide， exsuit 是没有返回值的。 excuse 方法，它不会往出抛异常，而我们 submit 它会抛异常。也就是你在实际真正去做处理的时候，你要注意一点， submit 方法内部异步线程出现异常的时候，它能去网速slow，但 excuse 不行，它会把异常吃掉。所以这个时候你就需要什么做好相应的详细的，这种才catch。所以是有些细节我是想一定是要跟小伙伴们说清楚的，这些都是基础。


好了，我们废话不多说，回过头来，我们去 new 一个 runnable 这么一个接口去实现出来。里边的实现我想做的这里边的逻辑。我们换成异步的了吗？好了，换成异步的怎么去解析？我们现在传过来的是request，我们要把 request 执行完了之后，再把它变成一个 response 写回去。这是我们要做的事情。首先，其实我们可以把 response 信息先定义好 RPC response， response 等于 new 一个 RPC response。接下来 response 点 set request ID。还记得吗？这是我们之前特殊的，用了很大的篇幅，重点去讲我们自己的 request ID 这个东西。因为我们要做异步回调，所以你一定要干什么？把 request ID 再重新的写回 response 里面，这是必须要做的一件事情，要不然你回调怎么办？无论是我们的 submit 还是execute，你最好在自己内部做好了。猜catch，这是必须要做的。 catch 的时候还是老师刚才说的，能用 snowball 的时候你就用snowball，不要用什么exception，万一兜不住呢？这都是一些编码和细节，小伙伴们一定要好好的去 get 到。


成功的时候我们怎么去做？我说成功的时候，我希望有 handle 这么一个方法。 handle 这个方法真正的去做实际的业务处理。把 request 传进来，它进行调用，完了之后能给我返回一个result，我就 result 去接收一下。先把模板写完response，点 response 协议，里边封装的就是一个result，直接把 result 放进去就好了。异常的时候是不是我们就相当于把 response 里边点 set throwable 扔进去就好？把 t 放回去，我们可以打一个什么？打一个log，点error。


我说 r p c server handler 在执行的时候出现异常了。 request e r r o r o 或者是slowable。把具体的信息去打印到日志里。OK，这就是我想要做的一个最简单的模板代码。把 handle 的方法再 create 出来，不要写内部的哈，我们就放到这里。这就搞定了我们的模板代码，把这都去掉。最后，如果你想要有后置处理器怎么办？你最后你执行完了之后，你是不是把东西写出去？你可以写 c t x 点 right and flash。你要写出一东西，把 response 扔出去。好后置处理器。你可以加 at listener。 net 里边很多，一定要学会。 at listener 的写法叫做 channel future listener 去加一个。如果 complete 的时候我做一些处理，你怎么做？ if future 点 is success 的时候，或者是 is done 的时候， is 什么什么什么的时候，都可以去自己做自己的一些。


我们的 after r p c hook。我这么去说能理解，我说意思，你自己可以去定义。接口在这里边，你把什么，你把 RPC hook 对象接口直接扔进来，你在内部去调一下 RPC hook 后置处理器，调一下接口，具体实现类就有了。


OK，这些后置的时候我们怎么去做，你自己可以去定义，我在这就不说了哈。前置很简单，你就在这个 run 方法之前可以做一个 before r p c hook before，我们调用之前做一些处理，调用的时候 handler 的方法做处理，调用之后做处理，就做一个切面，很简单。OK，我们现在主要来看一看什么 handle 的方法，我们应该怎么去做。 handle 的方法很简单，它主要的就是具体方法去执行。我们去解析 request 对象， request 对象里边我们就叫request，别搞太复杂。 r p c request 对象里边。我们首先string，我们是不是知道这个克拉斯name？克拉斯 name 是不是这个接口的名称？第二， get 我们的 class name 就可以了。如果有的话，因为我们请求里边还记得吗？请求里面已经有 class name 了，包括 master 的参数都会有。你通过这几个你就能做解析。


class name 有了。好了，我问你，如果我能够知道 class name，我 tenant map 它是怎么绑定的？它是interface，加上具体的实例对象，就是接口下面具体的实例对象。我是不是可以通过 handler Mac 里面取到具体实际对象，这是毋庸置疑的。直接取就可以了。直接 get key，通过可 last name 直接取到我们具体的执行器，它是一个object，我们其实叫做。如果跟 screen 整合，我在这里这样写就行了，叫做 service bin 就可以了。如果没有跟 spring 整合的，我叫做 target 或者叫 reference bin 或者Ref，这样更好一些。好了，你现在知道 Ref 对象了。 r e f。它具体的一些 class 你能不能知道？肯定知道。


第二， get class。这样你是不是真正知道这个类它具体的 class 是什么了？因为上面是一个接口，下面是一个具体时间类class。我用一个问号，我不确定它是什么东西。咱们叫做 service class，叫服务。我叫做 service reference。 service reference service class 有了。好了，现在我问你，你现在怎么去调？你可以通过 Java 里边的反射，也可以通过 CG lab 都可以。我们先把其他的也都取出来，一次性取出来，比如还是request，里面还给我们什么内容。


第二， master name， method name。我们有 string 到 method name 好了。还有什么 parameter types 好？ get parameter types，它是一个 class 的数组，这里边我们叫做 parameter type t，y，p， e 词。接下来还有一个叫做parameters。


第二， get parameter 4，它是一个 object 数组，它具体给我传过来的一些参数是什么？ parameters 我们不确定。 parameter 4 好搞定。这是这些我想要的我都能取到。我们直接通过反射去调就好了，比如g，d， k 的反就不说了。reflect。你如果都不知道，你一定要好好去学一学。


c g lab 的我们来实现一下。其实 lab 里面有一个比较关键的东西，它叫做fast，它的性能会更好一些。 fast class 就是 net 点 s f，点 c d f，他可以去create，根据我的具体的实际的东西，我的接口，这是我的接口的。下面的实现我得找到实现类，去 create 出来。它返回的是一个 fast class，我们叫做service。 fast class 我就这么去写好了，我把它接收一下，通过它去直接点 get method。 get method 我是不是要传递信息？传递什么？首先它里边 master name 是什么？这里有 master name。 OK parameter types 是什么？有拿过来。最后他把 method 给我返回。在 CG library 里边有 fast class 和 fast method，我们叫做service，真实服务的 fast method 好了，有了它之后，最后 battle 和反射去调一样的。怎么去通过反射去调 service method？点儿 inwork target 对象是谁？就是 reference speed 它这是具体的 bin 实例，它传参数是什么？ x 我们的 parameters OK，这就是一个调用，调用完了之后，这里边最终你需要 catch 往处抛一场它，它抛的你也抛也行。这里边它有一个result，这个 result 就是我们的返回值。


返回值我直接是不是直接这样就好了， c g lab 就搞定了吗？我通过反射就直接取到了吗？这个就是我们的了。 handler 方法，解析我们的 request 请求，并且去通过反射或者 CG lab 也是反射，哈，就是调用具体的本地服务，执行具体的方法。所以应该是获取具体的本地服务对象实例后，执行具体的方法。返回结果是不是有返回结果之后，我们拿着这个结果去塞进去，如果它中间调这个方法抛异常了，把 Throba 写回去给我们的可看端就可以了。


这个就是我们整体的什么对应的 r p c server handler 要做的事情。注意最核心的点。你看一下我们 channel read 0 这个方法，你要通过异步的线程池去提交作业。在真正执行的时候，到底是通过 CG library 还是通过 GDK 反射，你自己去选。回调的时候你要注意回调的结果，成功的时候应该怎么做，失败的时候应该怎么做，都应该给它塞到 response 里面，写出去就行了。这里边还有一个概念，就是后置处理器的事情，希望小伙伴们记住。OK，这节课我们就讲到这，感谢小伙伴们收看。


