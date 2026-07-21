---
title: 2-2 客户端异步请求代理实现_RpcFuture回调模型实现
---

# 2-2 客户端异步请求代理实现_RpcFuture回调模型实现

[image](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/c70d0e4a-28b6-4f70-9d4e-4b4b76158f9e/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SXGLXAT4%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T230044Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDUGza3pYY3GJe6rzJwPc5NoRv1w7FpLhO0v43ScEOOCgIhAJsljwH%2FHps9t0Hr1en5B8gVxnFGpImscRt%2FiqOf2YTqKogECMb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1Igzj35XpKnw%2FHkov4bEq3ANoIHaUDrjegcW2W7dzmm21uO%2FJZhaYTrD%2B%2BWjB38boF%2BDe2qOEj4ciYRWfybcjHc%2BabYLWaLbUaxZzx8BhouA5lNJLUFbZXR8NJUAhU3BrKFVk6Pe2VUu%2Biyok5841MhYkhRxQXM5hkeqS0PEbc3DdLD3a9gnVDy9c7FLydS9p5MYS%2BmULR6Gzrplu2a1HVgSmKR6XHJTfu4lk4uPRdOFSRPEUuFJYuHSBLTz57%2Bl%2BJzq5illMMYV12k9m4BmwjlSWLFOl4AP2vPvVdqXS2KIvzP3jnRv9V88hh92OEhqZMNCzC6IrkuqM2Sf9c1OOrvvKG7tZ3XhsQNswf0a%2FWioGQsDsVjGX4oh%2FhhPfd8oXdjkpdL12PBt4M7vzhfwBrPptkN909cmNB49nkg0D6nEx2dEczugwFItMy3yQFpsO%2F1%2FUAN5kSJlMrf5g2vBk6tehMwpJV9Eo2c3II1T2ESbIeuUzwg8CBvR0durX4v180ih97q8hUU62sL3SWkGq7AgBEamRFkKIYkzF3X91DqiOBtw9EiLLVCVy3mz80igYqarcWyznc7%2Fr7WEncAajUsZdSAmltI9nzbRN4m%2FQUnCiX%2FgC%2F%2BdEc2CR4Lnn1ZGUiYZVXiQrMaCUzffCnTChuP%2FSBjqkAUpQdjubcTtTPmtkl5JyHrayqTDCl1KUxKIgWswFLnQEHAz0gH0V7D5IoSVHNxOOzZJKwiwCmBwGPzZ0lR02FQjNeFmvJHDwGMZ2YFZgqkeh0jpXaQONpEG2F6gdx%2Bua%2FBFRXBoQnoI4aXZ284nem5ca%2B0PgOJYN%2BahUGOfQSnlkViLSviHtr%2FBCHIa6Vqn5S9EkI5zoPPo7QMTrdUaYRyeDTlYX&X-Amz-Signature=36dc668111261a3636bca63d494c5879bf1912f0da332e772747e724cbcfd482&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

hello，小伙伴们大家好，这节课我们继续往下去讲。上节课其实我们已经对于 RPC silver handler 整体的过程已经搞定了哈。接下来我们要做的事情是什么？我们的 RPC server 端搞定了之后，最关键的一点就是我们的 RPC client 端， RPC client 端我怎么去发请求？最关键的一个类就是我们的 RPC client handler 对吧？ RPC 可量的 handler 要做的事情，我们同学们首先看第一个上面的一个直线的线性的流程。我们看首先 RPC 搜handler，里边提供一个方法，叫做 send request。 send request 它主要是异步的去发送请求的一个方法。在这里我要强调为什么它是异步的去发。我们都知道我们想要去写同步的发送，其实很简单，我们一些同步的请求过去，我们的请求会阻塞到我们当前线程里去调用。另外一端就是 remote 端， remote server 去做一些执行的逻辑，执行完了之后，把返回结果返回给我，我再继续主，我等待线程继续才能往下去走。


这是一个阻塞式的请求。现在我们想要做的是一个非阻塞异步式的，也就是我们的请求跟响应这块。我现在想把它断开，变成两个线程去做。我不知道小伙伴们能不能理解这个意思。你想变成两个线程去做，你必须要去拆开，这是第一点，第二点，你必须要第一个请求。线程发回去之后，我就不管了，我不阻塞，我可以去走其他的逻辑响应我们的 solo 执行完了之后，他再回来响应的时候，他是不是得找到之前请求的所在的对象去做后续处理？所以它比较关键的一点就是会应用到我们的 future 模式哈，这个也是我们做异步回调非常关键的一个概念哈。所以小伙伴们请看 send request 方法。


它首先一步发请求第一件事情做了什么？将请求封城封装成一个 future 模型，等待异步回调做处理。所以这有一个非常关键的概念，就是我们要做一个 future 模式哈。我们后面会定义一个 future 类。接下来我干什么？将 future 对象放到我们的一个叫做 pending RPC table 中，

[image](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/39fb73dc-a06b-4b95-a439-c0a701105ee2/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SXGLXAT4%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T230044Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDUGza3pYY3GJe6rzJwPc5NoRv1w7FpLhO0v43ScEOOCgIhAJsljwH%2FHps9t0Hr1en5B8gVxnFGpImscRt%2FiqOf2YTqKogECMb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1Igzj35XpKnw%2FHkov4bEq3ANoIHaUDrjegcW2W7dzmm21uO%2FJZhaYTrD%2B%2BWjB38boF%2BDe2qOEj4ciYRWfybcjHc%2BabYLWaLbUaxZzx8BhouA5lNJLUFbZXR8NJUAhU3BrKFVk6Pe2VUu%2Biyok5841MhYkhRxQXM5hkeqS0PEbc3DdLD3a9gnVDy9c7FLydS9p5MYS%2BmULR6Gzrplu2a1HVgSmKR6XHJTfu4lk4uPRdOFSRPEUuFJYuHSBLTz57%2Bl%2BJzq5illMMYV12k9m4BmwjlSWLFOl4AP2vPvVdqXS2KIvzP3jnRv9V88hh92OEhqZMNCzC6IrkuqM2Sf9c1OOrvvKG7tZ3XhsQNswf0a%2FWioGQsDsVjGX4oh%2FhhPfd8oXdjkpdL12PBt4M7vzhfwBrPptkN909cmNB49nkg0D6nEx2dEczugwFItMy3yQFpsO%2F1%2FUAN5kSJlMrf5g2vBk6tehMwpJV9Eo2c3II1T2ESbIeuUzwg8CBvR0durX4v180ih97q8hUU62sL3SWkGq7AgBEamRFkKIYkzF3X91DqiOBtw9EiLLVCVy3mz80igYqarcWyznc7%2Fr7WEncAajUsZdSAmltI9nzbRN4m%2FQUnCiX%2FgC%2F%2BdEc2CR4Lnn1ZGUiYZVXiQrMaCUzffCnTChuP%2FSBjqkAUpQdjubcTtTPmtkl5JyHrayqTDCl1KUxKIgWswFLnQEHAz0gH0V7D5IoSVHNxOOzZJKwiwCmBwGPzZ0lR02FQjNeFmvJHDwGMZ2YFZgqkeh0jpXaQONpEG2F6gdx%2Bua%2FBFRXBoQnoI4aXZ284nem5ca%2B0PgOJYN%2BahUGOfQSnlkViLSviHtr%2FBCHIa6Vqn5S9EkI5zoPPo7QMTrdUaYRyeDTlYX&X-Amz-Signature=734dd24f0e8d4d4b15488e2bf29ae1c19e029e5195f6d210123b37b525f3b74f&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

或者叫做 pending RPC response table。其实语义上很清晰了，我等待 RPC 的响应回调的一个 table 容器，等待去做回调处理这么一个过程。紧接着这两件事情做完了之后，我的请求不阻塞，直接去 right and flash 异步的去把我的请求写出去。这样我们的请求的逻辑就可以了。我想象什么时候给我响应，我不管，反正给我响应的时候，我能够从容器里边找到对应的 future 对象，拿出来做一个真正的 call back 执行就可以了。

[image](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/4879d293-d32f-472a-a5f6-a86f24052061/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SXGLXAT4%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T230044Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDUGza3pYY3GJe6rzJwPc5NoRv1w7FpLhO0v43ScEOOCgIhAJsljwH%2FHps9t0Hr1en5B8gVxnFGpImscRt%2FiqOf2YTqKogECMb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1Igzj35XpKnw%2FHkov4bEq3ANoIHaUDrjegcW2W7dzmm21uO%2FJZhaYTrD%2B%2BWjB38boF%2BDe2qOEj4ciYRWfybcjHc%2BabYLWaLbUaxZzx8BhouA5lNJLUFbZXR8NJUAhU3BrKFVk6Pe2VUu%2Biyok5841MhYkhRxQXM5hkeqS0PEbc3DdLD3a9gnVDy9c7FLydS9p5MYS%2BmULR6Gzrplu2a1HVgSmKR6XHJTfu4lk4uPRdOFSRPEUuFJYuHSBLTz57%2Bl%2BJzq5illMMYV12k9m4BmwjlSWLFOl4AP2vPvVdqXS2KIvzP3jnRv9V88hh92OEhqZMNCzC6IrkuqM2Sf9c1OOrvvKG7tZ3XhsQNswf0a%2FWioGQsDsVjGX4oh%2FhhPfd8oXdjkpdL12PBt4M7vzhfwBrPptkN909cmNB49nkg0D6nEx2dEczugwFItMy3yQFpsO%2F1%2FUAN5kSJlMrf5g2vBk6tehMwpJV9Eo2c3II1T2ESbIeuUzwg8CBvR0durX4v180ih97q8hUU62sL3SWkGq7AgBEamRFkKIYkzF3X91DqiOBtw9EiLLVCVy3mz80igYqarcWyznc7%2Fr7WEncAajUsZdSAmltI9nzbRN4m%2FQUnCiX%2FgC%2F%2BdEc2CR4Lnn1ZGUiYZVXiQrMaCUzffCnTChuP%2FSBjqkAUpQdjubcTtTPmtkl5JyHrayqTDCl1KUxKIgWswFLnQEHAz0gH0V7D5IoSVHNxOOzZJKwiwCmBwGPzZ0lR02FQjNeFmvJHDwGMZ2YFZgqkeh0jpXaQONpEG2F6gdx%2Bua%2FBFRXBoQnoI4aXZ284nem5ca%2B0PgOJYN%2BahUGOfQSnlkViLSviHtr%2FBCHIa6Vqn5S9EkI5zoPPo7QMTrdUaYRyeDTlYX&X-Amz-Signature=6ea13afcf129eebd31fbf96d6e21544032f0e488d8a96ef944edc21df9d1a9bb&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

这个逻辑其实很简单，因为我们都知道有一个非常关键的概念，就是我们在请求的时候， RPC request 的时候，会有一个 request ID 会带到我们的 server 端。我们响应的时候，同学们也知道，响应的时候我会把 RPC request ID 就是我们的 request ID，给它放到 response table 里，放到 RPC response 里，对吧？所以在响应的时候，我们响应数据回来的时候，我们就可以通过响应带的之前的 request ID 从 table 中找到 future 对象，拿出来去做一个执行就可以了哈。


好了，我不知道小伙伴们能不能理解我现在所要做的异步封装的一个思路。好了，这个是一个线性的流程，往下看。其实我要实现这件事情，我要需要依赖自己，需要做一些东西。比如我会有一个 RPC call back 接口，对吧？我等待 future 给我响应的时候，我要去做 call back 回调，比如成功的时候，失败的时候，我怎么去做处理。所以要提供一个比较上级的接口，接下来最关键的就是我们怎么去对 RPC future 做一个封装，它是一个异步处理的模型。


RPC future 最关键的里边有三个方法，第一个叫做 then 方法，就是处理方法，第二个就是阻塞式的这种开关。 a QS，也就是 abstract queen 的signonizer，就是我们 Java GUC 的 a k s 类。我们可以基于 a k s 去做一个扩展是吧？接下来我们可以at，可以去加多个回调函数去，可以去一起去执行，这些都是可以的。代方法做的事情很简单，我的响应过来了。代方法我们应该放到什么地方去执行？小伙伴们想一想，是不是等到我们的 RPC and handle 它的 channel 率的 0 方法，它给我回送响应结果的时候，我就可以去调代方法了，对不对？代方法处理的时候，无非去调一下 ingwork call back。就是把所有的回调取出来，依次去执行，执行完了之后回调的结果。如果是成功，我去做相应的处理，如果失败，我去做另外的失败的相应的处理就可以了。好了，这就是我们整个的我们现在要做的一个回调的这么一个编程的思路。


接下来我们就开始一点点编码。首先第一步要记得我们要在 RPC client handler 里面去做处理，发送一个异步请求，封装我们的 future 模型，去把 future 对象模型对象扔到 table 里，直接发出去请求哈，快速的去实现。在这里边老师已经打开了我们的 RPC client handler。

[image](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/2f0789f4-fbec-411b-98a4-a5ca2d868804/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SXGLXAT4%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T230044Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDUGza3pYY3GJe6rzJwPc5NoRv1w7FpLhO0v43ScEOOCgIhAJsljwH%2FHps9t0Hr1en5B8gVxnFGpImscRt%2FiqOf2YTqKogECMb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1Igzj35XpKnw%2FHkov4bEq3ANoIHaUDrjegcW2W7dzmm21uO%2FJZhaYTrD%2B%2BWjB38boF%2BDe2qOEj4ciYRWfybcjHc%2BabYLWaLbUaxZzx8BhouA5lNJLUFbZXR8NJUAhU3BrKFVk6Pe2VUu%2Biyok5841MhYkhRxQXM5hkeqS0PEbc3DdLD3a9gnVDy9c7FLydS9p5MYS%2BmULR6Gzrplu2a1HVgSmKR6XHJTfu4lk4uPRdOFSRPEUuFJYuHSBLTz57%2Bl%2BJzq5illMMYV12k9m4BmwjlSWLFOl4AP2vPvVdqXS2KIvzP3jnRv9V88hh92OEhqZMNCzC6IrkuqM2Sf9c1OOrvvKG7tZ3XhsQNswf0a%2FWioGQsDsVjGX4oh%2FhhPfd8oXdjkpdL12PBt4M7vzhfwBrPptkN909cmNB49nkg0D6nEx2dEczugwFItMy3yQFpsO%2F1%2FUAN5kSJlMrf5g2vBk6tehMwpJV9Eo2c3II1T2ESbIeuUzwg8CBvR0durX4v180ih97q8hUU62sL3SWkGq7AgBEamRFkKIYkzF3X91DqiOBtw9EiLLVCVy3mz80igYqarcWyznc7%2Fr7WEncAajUsZdSAmltI9nzbRN4m%2FQUnCiX%2FgC%2F%2BdEc2CR4Lnn1ZGUiYZVXiQrMaCUzffCnTChuP%2FSBjqkAUpQdjubcTtTPmtkl5JyHrayqTDCl1KUxKIgWswFLnQEHAz0gH0V7D5IoSVHNxOOzZJKwiwCmBwGPzZ0lR02FQjNeFmvJHDwGMZ2YFZgqkeh0jpXaQONpEG2F6gdx%2Bua%2FBFRXBoQnoI4aXZ284nem5ca%2B0PgOJYN%2BahUGOfQSnlkViLSviHtr%2FBCHIa6Vqn5S9EkI5zoPPo7QMTrdUaYRyeDTlYX&X-Amz-Signature=44c69029c7afb0cef7d15ecec1d8b6e38fbfeaede424c05874e8702f8af7c2f6&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

在 RPC client handler 里边，我们直接可以去写一个方法对不对？叫做public，它的返回肯定是一个什么 RPC 的future，我们其实就是 future 模型对象，我们需要用了。我现在直接先把空壳先搞出来，先不去写 RPC future。具体的实现你先不用去关注哈。 RPC future 对象有了之后，我们现在响应的结果肯定是 RPC 请求，最终它的结果肯定是 RPC future。我们写一个叫做 sand request 方法。 sand request 方法肯定是给我传递的参数，我们请求肯定是需要 RPC request，对不对？这是毋庸置疑的。我们 RPC request 对象肯定是要有的哈，我去把它发出去。我说现在这是什么？这是异步异步发送请求的方法。异步发送请求第一件事情是做什么？第一件事情就是你要把请求的信息给它封装到我们的RPC，封装到我们刚才所实现的 future 里边。所以第一步最简单的就是我要把 RPC future new 出来，对不对？ RPC future new 出来等于 new 一个 RPC future。 RPC Vu 是必须里边要有什么，要有 request 对不对？是我要保存一下我的request，这样我才能知道我 request 到底是什么内容。所以它的构造方法里边你必然会有 RPC request 对象。所以在这里我们可以先把这个东西写出来哈。


我们帕布雷克 public r p c re a sorry r p c future 这里边会有一个 r p c request 对象request，我们可以去把它引进来，我可以用一个成员变量去给它保存一下。是不是我说 private RPC request 好了，这里边就是 this 点 request 等于 request 就可以了。
其实同学们，你想想还有什么对象，比如它的响应对象是不是也得需要有？是不是？因为毕竟我们是一个就是 future 模型，所以 RPC 瑞斯棒死对象，也是需要有的。哈 response 具体 response 什么时候用，我们一会再说哈。我们先把这个东西先放到这哈。接下来我们看一下对应的瑞 RPC future，我们已经把它实例化出来了。第二件事情，我要把它放到一个 table 里，哈，放到 table 里的目的是什么？目的是为了我们后面响应结果给我回来，回送的时候，我们能够从 table 里找到对应的 IP future 去做执行，对吧？如果你找不到 IP filter 肯定就不对了。所以在这里我们要定义一个类，定义一个模型。我们的 RPC table。你可以认为这个东西我们可以去给它起个名字。我们在这里private，我们叫做一个map，它肯定是坎哈的 map 哈，它的 key 就是我们的string。这个 string 是什么？说白了就是request， i d 是不是value？就是我们的 r p c future 了。
p c future 哈我们叫做什么？刚才我流程图里已经写了叫做 pending RPC table，或者叫做 pending RPC response table，等于 new concurrent。哈希 map 好了，另外一个坎哈任。哈希 map 好了。有了这一个缓冲，这个东西就是作为一个缓冲的。哈我请求过去之后，我封装好了。之后我直接把什么？我直接把 future 对象扔到我的 pending RPC table 中，直接点 put 就可以了。 key 是什么？ key 肯定就是 request ID，所以我们就从 request 点 get request ID 取到value。就是我们 up is future。只要做完这两件事情，我们的异步的 future 模型就已经大功告成了。
最后就给它写出去就好了是吧？写出去很简单，我们有 channel 对吧？有channel，你 channel right， flash 就可以了。是不是 channel 点right？ and flash 我们的请求对象，这就可以了，对吧？这样最终我去 return 返回什么？返回 RPC future 对象？我不知道小伙伴们能不能理解代码的含义，说白了，代码的含义在说明一个什么问题？在说明我在发送请求的时候，我要先把请求封装成一个 future 模型，把请求返回去。你想想别人去调我的 send request 的时候，是不是就可以利用 future 模型发完了之后，调一下它的点 get 方法去等待，是不是就可以去异步的去等待这种回送的结果了？它可以支持这种怎么说两个线程了哈。好了，如果你不掉 get 他可能你要。
其实我们后面再详细的说，后面我们再写代码的时候，小伙伴们可能就更清晰了，现在你先去记哈，在这之前你知道。至于为什么我要返回future，可能小伙伴们可能有一点不理解，哈，没关系，我们后面再说。现在我做完第一件事情之后，就相当于我们回看一下哈，相当于我们的过程已经搞定了。接下来就是下面这一块了。


我要怎么去实现 RPC future？

还有 RPC call back，以及它里边的一些方法应该怎么去做哈。我们首先先把 RPC call back 先把它搞出来对吧？肯定是有一个回调函数的。 RPC call back 主要的目的就是当我们响应给我的时候，我怎么去做回调处理。我在这里写一个 interface 哈，叫做RPC， call back。好， RPC call back 里边就两个方法，我可以去叫做 success 对不对？ success 返回成功的时候给我一个结果，比如给我一个result，我不知道它是什么类型的，所以我就是 object 就可以了。还有一个，当我失败的时候，我可以返回一个 failure 对不对？失败的时候比如给我返回一个throttle，就是我抛一个异常可以，或者叫做Cos。
做完了这个事情，我们来继续往下看。现在回调函数也有了，接下来同学们想一想接下来我需要做什么事情。我现在把请求发出去了。请求发出去了之后，我是把我们的具体的后半部分的逻辑处理直接放到 future 里边了。


future 又加到 table 里了，什么时候给我回送响应？是不是小伙伴们就有点疑问了，响应肯定是在哪里去做的？肯定是在 channel read 0，就是我们 client 端 channel read 0 的时候。如果进到这个方法里证明给我回送响应了，对吧？回送响应的时候我要做什么事情？同学们想一想，第一步是不是你要先把干什么？你响应的是 RPC response， RPC response 里边肯定会有什么？肯定会有 request ID，我不知道小伙伴们能不能理解哈，这个应该大家都明白，肯定会有 request ID，因为我去做实际的response，就是服务端做处理的时候第一件事情对不对？第一件事情就是把 request ID 设置到了我们的 response 里边，就是 RPC response 里边，不信我们可以简单看一下对吧？你看我在这是response，sorry，这是我们 RP server handler 里面做的事情，他第一件事情 new 出来了 response 对象之后，就是把 response 对象他的里边的一个 request ID 属性设置了。这个就是我们请求过去的 request ID，我们响应也给它塞进去，看见了，最终经过实际的处理把它写出去这么一个过程。


好了，我们小伙伴们应该很明显知道这里边肯定是有 request ID 的。怎么去做？是不是我们很简单，因为你已经把 future 对象放到 table 里了，所以你直接从 table 里取就好了。你从 table 里点 get 我们的 request ID，是不是就能拿到 future 对象，是不是它就会有一个 RPC 的 future 对象就OK？ RPC future。


好了，现在有一个问题，如果 RPC future 它不等于空，我们可以加一个判断，如果它不等于空，是不是证明它确实是有实际的内容，或者是等待什么？等待我们对应的那半我们的请求过去了，还没有响应。所以它不等于空，不等于空，我们要做什么事情？其实接下来响应结果给我了，我们是不是直接做回调就可以了？说白了，我们直接就去调一下 RPC 点蛋方法，把响应传过去，具体响应怎么去处理，就是这个蛋方法内部做的事情了。也就是我们回看一下，响应给我，我直接调代方法去做实际的处理就可以了，对吧？好了，这么一个事情非常简单，这个代方法我们先把它去创建出来哈。当然在弹方法之前我看一下哈叫做什么？ RPC response 哈。OK，这个代方法我先把它直接去 create 出来哈。好了，具体代方法做什么我们先不管哈。假设直接做处理了。你之前原来的 table 里的我们 pending RPC table 里的 future 其实就可以不用了，对吧？所以你直接可以移除，你直接可以 remove 就可以了。


把我们当前的，通过 request ID 把当前的这个 q v 键值对，就是 request ID 所对应的 RPC future。我们在这里已经拿出来了，把它删除掉对不对？当然引用还在吗？然后， RPC future 引用还在哈，我们去调代方法去把响应传过去，其实就是这么一个简单的过程。这块我们已经实际的把我们 RPC client 端的编码已经写完了。剩下的事情是什么？剩下的事情就是我们怎么去做 RPC future 的封装了。接下来我们一起来看一看 RPC future 我们怎么去做实际的封装。


首先我们来回顾一下代方法，这个代方法是刚才我们加进来的。哈，代方法要做什么事情？我们说了瑞斯 BOSS 对象我是不可，在这里边已经声明纯变量，所以我们可以做一个引用，直接我们可以response，等于我们的response。我就这么简单去写好。现在引用都有了，弹方法做的事情是，实际的回调处理，具体实际的回调处理应该怎么去做？肯定是一个什么过程？肯定是一个这种你可以认为是一个阻塞的过程，哈，一个阻塞的过程。


其实我们可以在这里边我们可以加一些额外的比较关键的属性，比如当我们我举个例子，比如当我们创建的时候，其实我们可以给他一个时间，执行完成之后我们也可以给他一个时间。一些额外的边角表的东西，我们可以先写上哈。比如当 future 模型创建的时候，放入 table 的那一刻。说白了，创建的时候我们可以有一个 start time，这完全是可以有的哈。比如 long 类型的 start time，这是一些属性，我可以给他 start time 就可以去说this，点 start time 就等于我们 system 点什么？点 current minutes，哈，就是一个起始时间。OK，这是可以的。这个蛋方法。同学们想一想实际的回调处理，我要怎么样才能去通知他说我可以去做实际的处理了。小伙伴们，你要想一想这块，如果你想不明白，其实我们可以简单来简化一下它。你要结合着上下文来看我们的 RPC client handler，它其实在最后是不是还是返回了一个 RPC future 对象？我在 send 之后，其实我返回的 RPC 对象。一般来讲，我们传统的 future 模型大家都知道，我会调一下点 get 方法去等待，是不是去阻塞，去等待结果，什么时候结果有了，我 get 方法里面就有返回值了。所以也是一样的。哈，我们调 get 方法的时候，他说白了就是一个阻塞。当我们我调 get 方法是阻塞，是不是我调蛋方法的时候，说白了非阻塞就可以去让它去执行了。它们两个之间会有一个锁的概念，对不对？一个互斥的概念。所以在这里我们要跟小伙伴们来说清楚一点。


在这里我们需要一个比较关键的东西，它，你可以认为它是一个什么？它是一个 future 模型。我们当前的这个类，它一定要我们实现我们自己的。我们 Java 的 GUC 下的一个future，其实我们可以来写一写，哈，其实很好理解它既然是一个future，它肯定是一个 future 模型。我们要不要是 net 的，哈，我们要 Java 的future，我们传一个 object 进来，因为我不确定它结果是什么，是不是我只能是给它一个object。 future 模型。它要实现好多个方法。我们 implements 一下，你看它要实现这么多方法。从当然，从这个蛋之后，哈，我们来看它要实现这么几个。首先第一个是cancel，是不是取消，还有个 is cancel 的，还有一个是 is done，还有两个 get 方法。这两个 get 方法是干什么？是不是？说白了，当我们去发送请求之后，我们的 r p c handler client r p c client handler 调 send re request 的时候，是不是返回future？我们是不是可以去调 future 里的点get，实现一个同步的等待，对吧？这是肯定的。get。


说白了，我们接下来要去重写的这 2 个方法，对吧？我们先不去考虑太多，我们先去关注这个事情。这个 get 是一个阻塞的概念，什么时候我们能拿到结果，肯定是对应着，但方法处罚了之后，我们能拿到结果。所以对于 get 和弹方法之间，他们应该有一个这种互斥，就是一个类似互斥的这么一个角色。这个角色我们在这里先把它封装一下。在这里老师使用一个比较简单的。当然这个也不算简单，可能小伙伴们没接触过太多。我说我自己写一个 sink 同步的一把锁，哈，这把锁我自己去继承。我是不是可以自己继承？比如我继承 abase tract abstract queen 的 single neither，我自己去随便去定义。我只要去继承了AQS，我就拥有了 a k s 里边的核心的内容，比如它的 state 共享变量，比如它的同步队列。对吧？我去重写它几个方法。重写几个方法。其实我就自己随便去定义一个标记就可以了。我自己定义哪些标记，同学们想一想，我就定义什么时候阻塞，什么时候释放就可以了。释放的时候肯定是在弹的时候，我就释放阻塞了。什么时候阻塞调 get 方法第一开始的时候，我要我就做一个阻塞就可以了。所以现在你自己定义的这把锁，你只需要去标记阻塞跟释放的时机就可以了。我现在就随便去定义几个变量。


我说 private final 的 Int 类型的 then 表示完成，我给它设置成一等待，是不是等待我们就给他一个 Int 类型，你叫 wait 也好，叫做 pending 也好，都可以，我们叫做 pending 对不对？就等待，如果等于 0 的时候，就表示是一个等待的过程，可不可以？这是我自己定义的这把锁的两个标记。我也不是完全的按照我们的 a k s 里边的 state 东西去做的。


我只需要实现两个方法，一个叫做 try required，一个叫做 try release 的就可以了，对吧？小伙伴们应该对 AQS 比较熟悉的，你应该知道protected，因为具体我这是我的父类，肯定有具体的接口，我应该是做具体的实现，比如 try require，这里边还记得吗？要给我一个request，就是一个许可的号。


瑞克尔斯是什么对不对？你获得许怎么去获得许可？最后返回一个到底能不能拿到许可？你看它这里边有一个重载的方法Overrest，所以这个是一个上层的接口，我们什么情况下算是它能够获取许可？如果当前的 get state 大家应该不陌生，哈，如果当前 get state 等于蛋的话，是不是就是获取许可？我不知道小伙伴们能不能理解，如果是等于蛋，我不管这个蛋它是 1 还是 2 还是几，反正这是我自己定义的标识。我们看自己这代码，你不需要看实际的太复杂的东西。
当然 state 写错了哈，有一个 t 好了，如果它等于蛋的时候，是不是就是获取许可？因为等于蛋的时候证明已经完成了，我的标记已经释放了，这才是等待。等待的时候肯定是拿不到许可的，所以这就返回 true 了。这边就是force，可以吧，这是一个最简单的。当然， get states 是我们abstract。
Synchronized obstruct queen synchronizer.


里边的方法哈，它就是一个什么，我们点进去，它就是一个state，这个 state 就是一个 wallet 所声明的所修饰的一个这种共享的变量，对吧。好了，获取许可的时候肯定是 state 值等于氮的时候，因为我们自己声明的哈。当然 AQS 0 和 1 那个东西，你就是本身来讲 AQS 内部的state，它等于 0 = 1，你不需要关注，你认为就没有了。你就按我这个为准。我说等于但的时候有许可，等于 pending 的时候没有许可就是等待。这就可以了。然后踹release，踹request，大家都知道了，踹 release 很简单了，是不是 protected 布置类型的charges，对 list 对吧？也是给我来一个release，是可以吧。吃这个方法就表示我要干什么？我要去，我要去释放许可，对吧？我要去释放许可，我在什么时机去释放？我又是不是写错了？ try release？没错。OK，我先给它返回值，先直接写好if。


如果我们 get state，它如果等于pending，等于 pending 是什么？它是等待的过程对不对？等于 pending 的时候属于等待的过程。我们可以用一个简单的一个CS，我们去做一个处理。比如在我们的 abstract think 里边，有一个 CS 的操作叫做 compare and set States，对不对？ compare 比较并交换比较，并去设置set，这是对 space 的一个设置。


我期望的还有真正更新的。我期望你是 pending 的状态对不对？我要释放吗？我期望你是 pending 的状态，并且我真正释放的时候你是 done 的状态，对吧？这才能真正去把所释放了。好。最终如果释放，如果 c s 成功了，就 return 处对不对？就真正释放成功。如果没释放成功，那就返回 first 就可以了。
好，这个方法它也我也是重写了一下 AQS 的踹release。为什么我会重写这两个方法？因为原先 states 值跟我现在所声明的语义是不同的。我现在认为等于1，这个是 done 的状态，等于 0 是 pending 的状态。所以我要根据我自己的上下文去修改一下我的 try 瑞克尔跟 try 瑞丽斯这两个方法。


好了，接下来就简单了是不是？接下来比如这里边我给他一个其他的方法，比如 e 子弹的方法，到底释没释放，就是一些简单的判断。我说 public 布尔类型 is then 到底是没，到底可不可用释没释放直接 return 什么？这里边不需要我去比较，直接通过 get states 等于蛋去比较了，如果等于蛋就代表是 OK 的，确实是这种蛋的状态对吧。


好了，现在我整体的 a k s 就自己去写的这把锁已经写完了。这就是一个最简单的自己定义的一把锁。我自己定义的这把锁，其实我可以去做一些什么，我可以去做一些把上面能实现的东西，我可以尽量实现一下，比如伊斯弹是不是这个伊斯弹，我是不是直接可以调用我的自己定义的这把锁的伊斯弹方法。我们自己定义的这把锁我们在什么时候初始化？其实你可以去在构造的时候把它拗出来就可以了。这是最简单的。比如在创建 RPC future 的时候，我是不是就可以直接弄出来？我在这里可以有一个变量哈，叫做 s y n c，就是我们自己内部的 s y n c 这把锁。加一个引用。这里边在创建的时候，创建 r p c future 的时候，我直接就是搞出来， diss 点它等于 new 一个 SNC 好，是不是就可以了，对吧？


我们有了这个引用，在创建的时候肯定是拗出来一个实例了。接下来我想去加东西不就简单了吗？这里边cancel。我可能不太知道哈， cancel 到底是什么时机，我可能不太清楚，我如果实现不了的，我可以去给他直接抛出一个异常可不可以？比如 new 一个叫做 in supported。有一个比较关键的是不是 exception 叫做不支持当前操作的。其实 AQS 里边好多这种概念哈，就不支持当前操作，我们可以点进去。 a k s 里边，它是一个抽象的，我们可以去 Ctrl 来看一看这里边比如 cancel require 的，这是有实现的哈，它里边肯定有一些没有实现的方法，他自己都是直接抛了一个异常。我不知道。


小伙伴们，如果你看过 AQS 的代码，你应该知道了哈，我们往下去找一找，你看他有好多都是什么 try list？我这个 fact 他不支持，我就直接 new 一个异常，我们也可以这么干。我们不想给他去写的方法，我们直接去往出抛一个异常就好了。是不是我们直接 through new and supported op operation exception？OK？我们 cancel 可以不用。什么意思？ cancel 这些我都没听过，是不是我就直接往出抛异常？反正你调我方法我就跑一成就完了。哈，对吧。因为我不知道该怎么去做。 e 字段方法到底是可以的，是不是因为 e 字段方法我们肯定是需要的。 easy 弹方法，我们只需要判断我们之前所看到的 single is 弹就可以了。成员变量 SNC 点 is 弹对吧？这个是我们可以实现的，关键的。下面这两个方法就是get。


哈，这两个 get 方法是不是很关键？这两个 get 方法是很关键的，比如我们什么时候去调用get？同学们想一想，还是你要结合着上下文语义。当我们把请求发出去之后，我最终是异步的写出去了。我不等待，但是我会返回一个 future 对象，这个 future 对象会直接返回到整体的上下文中。


future。它里边会有两个 get 方法，对吧？有两个 get 方法是干什么？我想去获取许可吗？对不对？我获取许可，我怎么去才能让他去获取把许可？小伙伴们在这里很简单，我们就通过我们刚才自己定义的这把锁，如果require，如果我说等于- 1 的情况下，这就相当于我想去做许可的获取了哈。在这里我写一个简单代码哈。


我说 this 点 response 如果不等于我去做什么事情，我去直接 return 是不是？ return 什么？return？ this 点 response 点 get result。因为这个 result 才是我真正想要的，什么才是我真正想要的数据对不对？因为 get 方法大家应该你应该知道我 get 方法不就是我。上下文语义中，我发送完了 request 请求之后，我想去获得 RPC future 调它的 get 方法就想去得到结果。


调 get 方法如果有结果不是，我们是不是就可以把这个结果直接返回回去了，对不对？如果等于空，简单写一个else，直接返回空就完了是不是？或者你不写也行？哈，如果有多行， L4 的你如果有多行，你要加一括号包裹起来。这就是一个最简单的操作，下面还有一个get，带一个超时时间，我同步能等多久，对不对？这个也很简单，同步能等多久？它要比上面一直阻塞着 get 对不对？什么时候有了值，我什么时候会干什么，我就拿到许可了。之后有值了，之后我返回，结果没有就算了。


这里边是它有一个阻塞s，y，n， c 点我们踹 require 的，有一个叫做纳nos。我要等待多久？哈，我等待多久。如果我添一个- 1 是不是？时间戳，我可以去自己去定义一下，因为我们之前我想一想，哈，这个时间，我们这个时间在这里是吧？这个时间我们已经有了。比如我说我 get 我等待 10 分钟，或者这部分或者等待 10 秒钟。你应该直接传进来这 10 秒钟就可以了，是不是？所以我们就直接用 unit 点 to knuckles to Nannos，把 time out 时间去穿过去。当然它会有一个踹 require 的纳扣斯。这么一个实际等待的过程。看看他到底能不能拿到许可。他会返回一个布尔类型是否成功。


success 如果成功，我们去做这个事情。如果失败，我们抛一成就好了。是不是？那就写判断。如果这块是表示成功拿到许可的，我做的事情就很简单。我说 DS 点 response 如果不等于空的情况下，我们去把结果返回去对不对？我们 return this 点 response 点 get result 对吧？ else 的情况下，水天空。好。


接下来下面这是 success 的情况下，如果非success，同学们想一想，非 success 我们直接就抛异常了就可以了。是不是？我们直接 throw new 一个 run time exception runtime exception 直接抛一个异常，不是抛异常。我们可以写什么？ time out， time out exception 我们 request ID 是什么？我可以给它加上 request ID 我们当前我们可以取到 diss 点 request 点 get request ID，我们还可以加上一些其他的，比如当前的类名称是不是 class name 是什么？很简单就是 this 点 request 点 get class name。当前的方法是什么对吧？方法也可以有，逗号方法就是method， name 是吧？加上this，点request，点 get method。


好了。基本上把我想要输出的都输出一遍来，给他一个比较完善的异常告警。反正总值超时了，我把它来。来分一下哈。好，就是这样。就这样，不要搞太复杂哈。在我们抛异常的时候，我们直接就去往出死肉，就不需要去写瑞特了哈。好了，我们当前 get 方法其实就已经写完了哈。我们看到了我们的future。两个 get 方法，反正就是获取许可对不对？sorry，反正就是获取许可。根据判断到底成功与否，成功不等于空，是不是就把这个结果返回去就行了。这是 get 方法等待的什么时候会做释放，做释放就在关键在于蛋。所以其实最核心的还是在这个蛋应该怎么去写。很简单，你去获取许可，但释放就好了。如果我们去做释放，我们可以写一下。我们可以写怎么写 s y n c 点。 release 之前是-1，现在我写个 1 就好了，对吧？ release 的时候它释放，它返回。sorry，不是这个意思。蛋哈，是我们刚才那个蛋。方法在这里。但 release 到底释没释放成功，我可以有一个布尔类型，对不对？布尔类型我说success。如果是释放成功的时候，我就可以继续往下去走。是不是？如果程序释放成功了，我要继续去执行一个逻辑？那个逻辑叫什么？我们可以看一看，回看一下。但处理方法如果能处理，就会调一个叫做尹沃克 callback 斯，就是执行所有的回调对吧？好了，我们可以写一个方法叫做尹沃克。


什么尹沃克哈 call back 4 这个方法为什么会有一个叫做 call back 斯？因为其实我们可能有多个回调，我们可以加多个回调函数，这都是可以的。来，我创建一个 emock call x 方法哈。好，我执行完了之后，调用完了之后，我想判断一下是吧？我想判断一下，比如我们当前我当前时间减去开始时间，如果大于我的个响应的允许不允许的，或者是响应的一个上限，我可以也可以抛一个异常。我不知道小伙伴们能不能理解我说意思哈。假设我们在 RPC future 的时候开始创建的时候，我们是有一个 start time 对不对？好了，但这个请求回来的时候，他在这里做执行。执行完了之后，我是不是在这里可以记录一个 and time 对不对？ and time 是怎么去定义的？同学们是不是？比如我写一个long，咱们叫做response，或者叫做 and time 对不对？如它肯定是等于当前的system。


第二，它减去 start time 对吧？把一个开始和一个结束的时间都记录一下。在这里 start time，减去 4 大time。好了。 and time 中间的。说白了，这个是最终的。我这不能叫 and time 了哈。我叫什么time？叫做耗时的时间，叫做 cost time，可以吧。因为这个是结束。我真正所有的都调完了再走，再获取当天时间，肯定是结束时间对不对？结束时间减去起水时间，就等于中间我回调请求从我发的那一刻开始，对不对？发的那刻开始在哪？不就是在这里吗？在我上的 request 时候，我去 new 出来 RPC fuller 对象的时候，我去记录一下当前的开始时间，我回调的时候都执行完了，这是不是也记录一下结束时间，结束时间减去开始时间，就是中间的cost。就是整体 r p c 调用的耗时间对吧？我们记录耗时，我们可以做什么事情？比如我，我们再给他一个阈值，再给他什么值？比如我在这写死了。我觉得这个东西是一个比较关键的点。其实正常我们经常会有这么一个控制，咱们叫做cost，我们就叫做time。


the time throws。单词就是我整体的阈值。我认为我整体的请求阈值是多长时间，我可以写死了。 private final 浪可以写static，哈，整体执行的一个耗时的阈值，比如是5000，我们的 5 秒钟，哈，如果整体耗时大于 5 秒，我们是不是可以给他一个比如警告是不是你当前请求太耗时，时间太长了对吧？我们就可以。如果当前 cost 它小它大，对不对？能不能理解我说意思，我们阈值是 5 秒，你现在回来的比 5 秒还大，证明你的耗时时间太长了，我可以给他一个告警是不是？我说第二warning，当然我们没有 log 哈，我们把 SFG 加上，lot，点 warning 是不是？warning？我们可以给他一个告警，说 the r p c response time is too slow，可以吧。
request ID 是什么？写上去对不对？后面比如它的方法是什么？当然这是 warning 哈，你可以把它写全了吗？ request ID 是什么？加上 this 点 request 点 get request ID 其他的就不写了哈。我在这里简写除了有 request ID 之外，还有什么它的类名，还有它具体执行哪个方法都可以加上它整体的耗时多久，是不是他说 cost time 是多久，我们就加上你最终减完了耗时，对吧？OK，这样就可以了，算是一个比较完善的一个什么个 RPC future 了哈，它也有告警的提醒。


接下来我们看一下后面的就是我们的这个 inwork callback 斯。为什么我叫做 inwork callback 斯？原因是因为什么？原因是因为我期望在回调函数的时候我可以加多个回调，就不一定我只回调一次，或者是不一定我只是响应结果给我，我只做一次回调。我可能做多次的时候要保证一个什么？要保证一个顺序，所以我用一种数据结构 list 是最好的。因为先你list，它是有顺序的，对吧？所以在这里面我搞一个list，叫做 r r p c callback。好，我们叫做等待回调的一个list，对不对？我可以叫 pending 什么 call backs，可以吧。等于 new 一个 array list。这就写完了。好了，这是等待回调的是不是等待回调的这么一个集合？当然我们后面肯定会把它加上哈。我们先不管它，我们先假设 list 集合里边有内容，很简单，我们直接在 in work call back，我们直接复循环这个这个容器就可以了。我们可以做什么事情？他 for 循环，他对不对？ r p c callback，然后写 call back 风循环。当然其实你这里面最好是加一个 final 的哈，因为回调函数是不可变的。最好是这样去做，真正的去执行。我们可以写一个 run call back，是不是？ call back，诶，真正的去执行，把具体的一个 call back 传进去，它就真正的去执行了哈。
我们再创建一个方法，就是 run call back 方法。当然这个里边其实最好，你应该去加一把锁。为什么要加锁？因为你是多个函数，执行的时候我就怕线程安全问题，所以你最好加一把。一个乘入锁是最好的。我们在这里面再加上一把宠物锁。注意这个锁是跟锁，是判断 future 模型用的。我现在加的宠物锁是执行 call back，它要保持一个原子性的。哈，他们两个不是一样的，我们叫做lock，或者叫做 call back lock，哈，等于 reach and lock。好了，我们有了它之后，在执行之前是不是我们可以去做一个加锁动作？ final 的时候可以去做一个释放锁的动作。我说lock，点 lock try finally 在 finally 的时候，我们去做一个释放，点 unlock 对吧？把中间代码片段移到 try final 类里边。


好，最终这就是什么依次，依次执行回调函数处理，对不对？这个是 run call back，才是真正的处理回调函数。怎么去处理？回调函数怎么去处理？同学们想一想，真正的回调函数我们需要什么？因为我们知道他只要是走了氮方法 response 肯定是有内容了。是不是他复制了赋给了全局的response？所以我们只需要处理的一个结果就好了。在这里一般来讲，我们 run come back 的时候，我们可以这样去做 this 点response，我们就不让他去改变了。因为最终我们去做回调了。所以可以再用一个 final 去声明。你要注意实际的 final 的用法哈，他表示我不想再更改了，哈，我们去操作response。这怎么去做？是不是在回调的时候，回调处理器的时候，我们其实也可以再做一层线程池，异步的去做实际的回调处理，对吧？所以在这里边我们可以再搞一个线程池过去。


在最上面我们可以来一个 private thread pull executor， executor 等于 new 一个 thread 铺自定义的线程池。我们就找一个相对来讲参数少的，因为这个东西很简单哈，我们给他 16 个线程，这也是， 16 个核心线程，最大线程也是16。这里边我们设置 60 秒一分钟 time units，就是 time unit 等于 second 一分钟。
最后 work king 就是一个 new array blocking queen，瑞普 locking can？好了，我去定义它是一个 runable 是不是runable？这里边定义它的大小是65536，可以吧？OK，好了，现在我自己的一个线程池也已经定义好了，哈，叫做escort。


escort 我真正执行的时候是不是？在我真正执行的时候，我是不是也可以去做一个异步的实际的提交任务做真正处理？所以 excut 点 submit 就可以了，是不是你有一个 runnable 去做实际的真正处理？在这里边真正去调克外克是不是？好了，怎么去写if？如果你的 response 是不是我要做 response 处理？第二， get 什么？这里边有一个response，里边有什么？一个叫 get throttle 是不是？如果 get through 等于空，那我这样写，小伙伴能不能明白？证明没有异常？没有异常我就直接去调什么？我们 call back 已经传进来了，是不是回调函数？我说 call back 点什么success，是不是把 result 去写回去？这个 result 就是你当前的 response 点 get result 对吧？ else 情况下肯定是它。我们的 slope 不等于空，这个时候就失败，是不是我就 call back 点丢了对吧？把我们当前的异常传过去。其实你可以去 new 一个 run time exception，或者是 new 一个直接把你的东西扔过去就好了哈。 response 点 get through 就可以了是吧？这是最简单的。
好了，现在我们整个的 future 模型就已经写完了，对吧？

[image](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/56561bd5-8efb-47c3-80bd-12b7deb2f42d/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SXGLXAT4%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T230045Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDUGza3pYY3GJe6rzJwPc5NoRv1w7FpLhO0v43ScEOOCgIhAJsljwH%2FHps9t0Hr1en5B8gVxnFGpImscRt%2FiqOf2YTqKogECMb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1Igzj35XpKnw%2FHkov4bEq3ANoIHaUDrjegcW2W7dzmm21uO%2FJZhaYTrD%2B%2BWjB38boF%2BDe2qOEj4ciYRWfybcjHc%2BabYLWaLbUaxZzx8BhouA5lNJLUFbZXR8NJUAhU3BrKFVk6Pe2VUu%2Biyok5841MhYkhRxQXM5hkeqS0PEbc3DdLD3a9gnVDy9c7FLydS9p5MYS%2BmULR6Gzrplu2a1HVgSmKR6XHJTfu4lk4uPRdOFSRPEUuFJYuHSBLTz57%2Bl%2BJzq5illMMYV12k9m4BmwjlSWLFOl4AP2vPvVdqXS2KIvzP3jnRv9V88hh92OEhqZMNCzC6IrkuqM2Sf9c1OOrvvKG7tZ3XhsQNswf0a%2FWioGQsDsVjGX4oh%2FhhPfd8oXdjkpdL12PBt4M7vzhfwBrPptkN909cmNB49nkg0D6nEx2dEczugwFItMy3yQFpsO%2F1%2FUAN5kSJlMrf5g2vBk6tehMwpJV9Eo2c3II1T2ESbIeuUzwg8CBvR0durX4v180ih97q8hUU62sL3SWkGq7AgBEamRFkKIYkzF3X91DqiOBtw9EiLLVCVy3mz80igYqarcWyznc7%2Fr7WEncAajUsZdSAmltI9nzbRN4m%2FQUnCiX%2FgC%2F%2BdEc2CR4Lnn1ZGUiYZVXiQrMaCUzffCnTChuP%2FSBjqkAUpQdjubcTtTPmtkl5JyHrayqTDCl1KUxKIgWswFLnQEHAz0gH0V7D5IoSVHNxOOzZJKwiwCmBwGPzZ0lR02FQjNeFmvJHDwGMZ2YFZgqkeh0jpXaQONpEG2F6gdx%2Bua%2FBFRXBoQnoI4aXZ284nem5ca%2B0PgOJYN%2BahUGOfQSnlkViLSviHtr%2FBCHIa6Vqn5S9EkI5zoPPo7QMTrdUaYRyeDTlYX&X-Amz-Signature=d22387e87203ab9662fa85fa621e7c82fa30736fc609f51c1d7f502f72b1ebe1&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

我们来稍微回顾一下哈。稍微回顾一下逻辑，它确实是有一点绕，也就是我们异步的去发送请求之后，返回的是一个 future 对象哈， future 对象？它是在这等待着的对不对？它是放到一个叫做 pending RPC table 中去等待响应过来，去拿出来具体的 request ID 所对应的 future 对象去做后续的处理的，对吧？他直接把请求写出去了。


当我响应回来的时候，无非就是我们刚才所看到的代码 RPC client handler 里边的 channel read 0，它真正响应回来的时候，它肯定会触发 channel read 0 方法。我们去从响应里边把响应的 request ID 拿到，从 table 里边去取到 future 对象去调蛋方法对不对？蛋方法肯定是就执行了，对不对？蛋方法一定。一旦触发我们之前 send request 所返回的 RPC future，肯定是先调了点 get 方法对不对？他去等待，等待完了之后等待去处罚，再方法去做释放的时候，这个逻辑就继续可以去往下走了，对吧？他在这里认，如果成功，他直接去去批量的去。当然你看我们现在只我们现在 call back 可能只是传一个哈。 call back，我们里边其实可以给他加一个刚才我说的批量的 at call back，我们再把写上，不差这一点时间。批量的 call back 也很简单，我们写public，它返回的是一个 RPC future 对吧？我可以去继续去加吗？ RPC future 叫做 add call back 就可以了哈。总之给我一个 RPC call back，我可以帮你去加上去哈。加到 list 里边，它是有序的去加的。但是添加的时候OK，添加的时候也要加锁对吧？因为你做这种对 call 麦克去做处理，锁肯定是要加的。在这里边的操作对应着想一下，肯定是要判断一下，如果 is 旦处理完了之后，你才能去加这个事情是不是处理完了之后我们去做什么。


如果 e 字段，你就做 run call back 就好了，直接去执行 run call back 对不对？处理完了之后你直接可以就执行它了。如果没处理完了之后就放到等待队列里去去去去去，慢速的去后面去执行。那就是 DS 点 pending callback 点add，拷贝好这块我也稍微去把它优化一下哈。最后 return this 就可以了。因为当前 base 就是 RPC 销售对象对吧？这个逻辑是什么意思？就是我可以在应用执行的过程中添加回调处理函数对不对？为什么我加进来的时候我判断它是否淡？如果已经处理完了之后，就假设当前它当前已经有了一个 call back 了。处理它一个 call back 到底是执行中还是已经执行完了？如果执行完了 1 字段，我直接就调我现在新加的这一个它距继续去做 run call back。无非就是再去给它提交到一个异步的 task 线程池里边去执行就好了，对吧？但是如果没一直在，没执行完你就干什么？你把它放到队列里对不对？你放到这个队列里， list 队列里知道我们是run，方法是负循环，它执行完一个 callback 之后，它才会再复循环下一次。


再执行完下一次执行这个队列或者list，它的下一个元素肯定依次去执行，所以这里边需要加一个锁。好了，基本上我们整个的 future 也就封装完了。这节课我们就讲到这，感谢小伙伴们收看。

