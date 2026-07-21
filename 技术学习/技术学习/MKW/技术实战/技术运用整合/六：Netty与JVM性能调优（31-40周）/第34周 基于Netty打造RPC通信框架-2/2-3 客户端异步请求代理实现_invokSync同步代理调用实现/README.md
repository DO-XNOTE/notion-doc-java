---
title: 2-3 客户端异步请求代理实现_invokSync同步代理调用实现
---

# 2-3 客户端异步请求代理实现_invokSync同步代理调用实现

[image](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/4f8ce298-39cc-4f94-bc0e-dd154efd71f0/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666V6JJLTQ%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T230045Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDvfCQltYCaWiS%2By405BbYTBSPBu3AOK2EYBMoWt1TRrwIhAL63fNjbT%2BV1g2%2BwHq6N%2BGz2zDElAiETEMfOHt5hKg1YKogECMb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgzJzu9kQwBPgct0%2Fx0q3APyU5bcrdS6nipyiLG3DLAZcCFJcfIcJ2nDLLG0Pj7HgovGXDqlAkQa0aWWQItgld7sevJ2JK9r8%2F8HKKaUn%2FtmXvejsHaTOGGUyEdDBIj2W88rC8Iowy4F6FWbWPJaeFGhGavqBEMFF8xYiViXjb5OYXdEEpnoIqetax%2FOlny3hBH4XjA6Un97Zk%2Fzvil7vLtxANtOpmXkkCbTWNplm5JIPVByf%2FcALMVMcmHJXKQU6CBUP8mbDMXHtccFtHT2GVPgGgI%2BPgm4fSeeLrPmuuhRaxTtU9O5ornlHTX1rZLwNhLjHmCLeA3oyuUy2tT5VACzQ8EFdddwniLznw%2B5LQt7OHowamygTsIsIu%2BAyJdtnInzxTv%2FrKFoyPWxyB%2BzcLy6ShVrLTqLcDTFaPy2BRoq5JygWHXPRUZPOMk0rvYFNQUCBe5DE%2Bv3SzRW%2B5LADIctZj1r2fujyuUY5Pw4XmbbK%2FprZV1d4NwIyNEAdN7cGvfcubpPRSwNoH2G%2B0wHoaCSyz8xfVlMdCIQ3xaMX0h7MwAYuzHnyyYwZHZEskwsAFYd271X3Oo1EwE4BWcw94AymLLMDcE0NXd%2BLFYDfNAmJuM1Q56UFl%2FrJxrejPtGpANlIW0GdpNq3sDU4jDYuv%2FSBjqkAYaoHc9Rdt3mMo%2FpQKAL8385K9fuhDr4cZNw1JrvG2GQIaV%2F4O%2FBU276qjkIX1l7K20R4gomzIVEFvSE7yfLKX1zV8X%2FGPIkIN3R2%2F%2Bl56Z%2B0G011TGtOlSbyqH%2FYhYI48gXHhVJn7qaRa9fEXdcVCJQEXnjehoy2CV803jsnM9DwbRNr09z0Sie7AxGXeIn6vWMRb8tvDhKpCFpWBJiSJHfi96b&X-Amz-Signature=328f6befcbc45b9acc07eb58ef948d56ade896dbe7fc211dc87de925e914aa9a&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

上节课我们对于 future 模型异步的封装已经搞定了，这节课我们来看一看我们最后的这一块。

[image](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/3d379823-cc1c-4ffc-8218-24544800596e/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666V6JJLTQ%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T230045Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDvfCQltYCaWiS%2By405BbYTBSPBu3AOK2EYBMoWt1TRrwIhAL63fNjbT%2BV1g2%2BwHq6N%2BGz2zDElAiETEMfOHt5hKg1YKogECMb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgzJzu9kQwBPgct0%2Fx0q3APyU5bcrdS6nipyiLG3DLAZcCFJcfIcJ2nDLLG0Pj7HgovGXDqlAkQa0aWWQItgld7sevJ2JK9r8%2F8HKKaUn%2FtmXvejsHaTOGGUyEdDBIj2W88rC8Iowy4F6FWbWPJaeFGhGavqBEMFF8xYiViXjb5OYXdEEpnoIqetax%2FOlny3hBH4XjA6Un97Zk%2Fzvil7vLtxANtOpmXkkCbTWNplm5JIPVByf%2FcALMVMcmHJXKQU6CBUP8mbDMXHtccFtHT2GVPgGgI%2BPgm4fSeeLrPmuuhRaxTtU9O5ornlHTX1rZLwNhLjHmCLeA3oyuUy2tT5VACzQ8EFdddwniLznw%2B5LQt7OHowamygTsIsIu%2BAyJdtnInzxTv%2FrKFoyPWxyB%2BzcLy6ShVrLTqLcDTFaPy2BRoq5JygWHXPRUZPOMk0rvYFNQUCBe5DE%2Bv3SzRW%2B5LADIctZj1r2fujyuUY5Pw4XmbbK%2FprZV1d4NwIyNEAdN7cGvfcubpPRSwNoH2G%2B0wHoaCSyz8xfVlMdCIQ3xaMX0h7MwAYuzHnyyYwZHZEskwsAFYd271X3Oo1EwE4BWcw94AymLLMDcE0NXd%2BLFYDfNAmJuM1Q56UFl%2FrJxrejPtGpANlIW0GdpNq3sDU4jDYuv%2FSBjqkAYaoHc9Rdt3mMo%2FpQKAL8385K9fuhDr4cZNw1JrvG2GQIaV%2F4O%2FBU276qjkIX1l7K20R4gomzIVEFvSE7yfLKX1zV8X%2FGPIkIN3R2%2F%2Bl56Z%2B0G011TGtOlSbyqH%2FYhYI48gXHhVJn7qaRa9fEXdcVCJQEXnjehoy2CV803jsnM9DwbRNr09z0Sie7AxGXeIn6vWMRb8tvDhKpCFpWBJiSJHfi96b&X-Amz-Signature=6a5e35faf2896043760f13784cb09f6aa3b28922e0deb15556fc1dbc660d150c&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

其实相对来讲比较简单，因为要封装一个代理去我们的客户端，会有一个代理去调用它，就可以看看代理整体的实现的流程是什么样子的。代理它的最核心肯定我们要实现 g d k 的 invocation handler 接口，这是毋庸置疑的。我们主要需要小伙伴们来关注一下代理接口什么时候被调用。被调用肯定是在最下面。


这里原来有一个叫 RPC client， RPC client 它提供了两种方式，一种叫做隐沃克斯口同步的去调用，还有一种叫做 inwork a single 异步的去调用。我们这节课先把同步的调用实现，下节课我们再实现异步调用。同步调用它只需要实现 invocation handler 接口去实现，以 work 方法去同步的去做就好了哈。对应着异步的调用，我们需要再加一个新的接口，咱们叫做 r p c proxy，或者是 r p c a single proxy 都可以，不管是同步的还是异步的，我可以封装到一个类里边，叫做 r p c proxy implements。实现类实现类去实现。同步的调用和异步的调用。我们来看一看。


刚才我已经说了，我们整体的服务端调用的过程肯定是 RPC clan 端，它提供的方法，提供真正的同步和异步的请求，对不对？所以我们应该先从 r p c client 入手，先把同步去搞定 r p c client 里边应该有一个同步的，叫做 in worker single 方法。


in worker single 方法肯定得去做代理对象真正的调用代理对象里面实际的同步的调用才可以。当然我们去调用完了之后，我们的代理其实也可以把它缓存到一个 map 中，这里边也会有两个，一个是同步的代理缓存，还有一个是异步的代理缓存。好了，接下来我们就来着手去写一下我们对应的 r p c client 它的同步的方法了哈。首先我们对应的 r p c client 找到我们之前写到写得非常简单，就是一个外壳对不对，现在我们要对它进行详细的编写了。比如我们现在先写同步的方法 public 首先返回值对象肯定是一个代理对象，这个代理对象是什么？我们不知道对不对。代理对象它到底代理什么类，我们可以用一个泛型去描述，它就是一个t。最终他给我们返回一个t，我可以给他写一个叫做 in work s， y n c 的方法代理。他要需要传一个什么东西，肯定是全一个 class 类类类型对不对？ class 类类型我不知道，我就来个 t 对不对。它因为是我们都是接口的方法调用，所以我们在这里面给他一个 interface plus。好了，我们就拿这个方法去来判断。其他的。我们先把代理直接弄出来，这个代理弄出来返回很简单，我们 g d k 的动态代理proxy？点儿你有一个 proxy instance 对不对？它里边传递参数我们找一个比较多的。第一个要传的是 class loader 对不对？ class loader 是什么？就是类加载器。类加载器是不是直接可以通过 interface 去拿出来？对不对？我们直接把它来。


第二 get class loader 好。另外一期渠道具体的接口，它是一个数组，我应该叫做 class 数组。具体类型我不知道，用一个问号表示，我们就是一个大括号，把类型接口类型放到这里。最后 h 就是一个代理类，这个代理类我们现在还没有，对不对？我说我现在应该有一个代理类了。这个代理类一定是实现了 invocation handler，我们之前所看到的它是非常重要的，所以我们这个类叫做 r p c proxy implements 对吧？所以我们直接 new 出来一个 r p c 什么 proxy implements 就可以了。是不是具体类型我不知道。


当然代理类肯定要传递的比较关键的属性是什么，你肯定比较关注的是具体的接口是什么。还有超时是不是假如我调用超时了，这超时我们之间已经给的了哈，超时这 time out 好了。返回这里边返回之后我们直接 return 就好了。我们说return，我给他少了一个括号，这里边我们直接 return 当前的一个代理就好了。 return 我们的proxy。这个 proxy 可以用一个变量接收一下。代理类我也不知道是什么，注意是一个 proxy 对象，等于它返回就可以了。就这么简单，我们把它实现就好了。这个类我们创建一下。在这里面我们再创建一个包，这个包叫做就叫做proxy，可以。当然这个包肯定是我们 clan 端的代理，所以叫做 clan 的proxy。OK，把这个类去实现了哈。


对应的叫做 r p c approxy implements，它肯定实现了。我们的叫做 invocation handler。接口 Java 点 long 点 reflect invocation handler 重写 inwork 方法，对吧？这是必须要有的。在这里边我们把它导进来，里面传递两个参数，我们要加上哈 private public。它第一个是 class 对吧？类型的东西，我们直接把它拿过来。
第二个是一个 time out，这个 time out 是一个浪类型的。哈，浪类型的 time out。好了，这样你对应的 proxy 对象是一个泛型，这个泛型你应该传进去对不对？在这里带过来，你还有对应的成员变量应该有是吧？接收一下 private 我们的 class 类类型，它是一个 t 大型，我们就叫做克拉斯，可以里边可以改成克拉斯。还有一个成变量叫 private long 超时间 time out 成为变量去做一个赋值。 this 点什么 class 等于class。 this 点儿我们的 time out 等于 time out。好了，写完了，这里边就应该保存一下，我拗出来它的时候就不会报错了哈。


好了之后我们把代理对象就是 proxy 去返回去强转一下对不对？因为你现在我不知道它是什么类型，你如果不去做强转它可能会有问题。小括号加一个 t 强转。好了，现在其实我们的整个的 in work think 同步的调用已经做完了。在这里我打个注释哈。同步调用方法，这是我们最上层的 API 对不对？后面我们创建了 RPC client 以后，我们想去远程的调RPC，我们就调这个方法就可以了。会帮我们去生成代理。帮我们生成代理。我期望什么？我期望你会有一个缓存。能理解我说意思，你要有一个缓存，你要没有缓存，你每次都 new 一个代理对象，太浪费资源了。


在这里面我们去声明一个map，把它缓存起来， final 的叫做map，它的 key 是 class 类型的，对应的哪个类做代理对不对？我们可以去加一个泛型 Y6 就是一个object，就是一个代理对象了。我们叫做同步的缓存 sync proxy instance。 map 等于 new 一个concurrent，拉齐 map 就可以了是吧？好，搞定它之后，我们在这里边。


我们如果是新建的哈，如果一直没有代理对象，我是不是应该去直接把它 put 进去就可以了？调它点儿put，它的 key 就是我们的 interface class， value 就是我们刚才新的代理对象就可以了。同学们想一想，如果代理已经存在，是不是你得做一个判断。在这里我们先来做个判断if。如果我们当前 map 里边已经有代理对象，直接返回代理对象就好了。如果是 contents key，包含当前的 interface class 的情况下，就证明已经有了。我们直接 return 就好了。 return 什么？return？他点get。如果已经有代理想直接返回。


当然我们要强转成一个什么 t 类型的，这是对应的存在的情况下，不存在的时候我再去new，是不是我再去重新创建，把它放到这里？对，不存在。我们新创建一个代理，把它放到 map 里，最后返回。当然这里边有一些警告，你可以直接把它 uncheck 对不对？以萨布斯 money 按 check 就可以了。
现在我们对应的同步的代理方法已经搞定了。同步的代理方法搞定了，接下来我们来看一看，回看一下我们流程图，也就是我们对于 client 端的第一个 inwork simple 这个方法已经搞定了，也把它存到 map 里了，是不是也加了缓存了？我们接下来就看一下 r p c proxy implements 它 inwork 具体的实现应该怎么去实现就好了。它的 inwork 方法应该怎么去实现，我现在还不知道，我们应该把它去写一写。所以在这里边我们就重点关注一下 r p c proxy implements 它里边 inwork 方法应该怎么去做。


我们不考虑其他的一些特殊情况，我们就考虑它能够有代理，它是一个普通的代理对象，我们怎么去做这个代理对象。引 work 方法，它到底的代理的是哪个？它代理的是 client 端，代理的是我们整个的 client 端 RPC client。既然代理 RPC client，他代理的事情是什么？同学们想一想，说白了，我调了一个隐沃克sync，它应该帮我去做什么事情，他就应该生成一个代理对象，并且帮我去发送 RPC 请求，把数据发过去给我，等待回送响应这么一个事情。后面我们的 API 写法非常简单，就是用把它 new 出来去调它的 inwork simple 方法就可以了，你不需要关注其他的。


所以我们现在应该怎么去做？我们现在直接在这里边代理对象，无非就是我们应该把具体的 request 什么，我们都应该通过什么，通过代理对象拿到代理。方法就有这几步。第一步设置请求对象，第二步选择一个合适的任务处理器，就是业务处理器哈。任务信息肯定是 client 的，实际的处理器干什么？去发送真正的客户端请求返回结果就可以了。其实就这么三件事情。因为 inwork 方法才是我们真正的client，它的inwork，它其实走的是代理的方法，对不对？因为它是一个代理对象，我们在这里代理的对象才是真正的要去发请求的事情。所以在这里我的 r r p c。什么 r p c request？我要把它搞出来，等于 new 一个 RPC request。这个 request 里边要设置一些东西，比如他发请求每次发的请求 request ID 是什么？在这里可以用一个简单的 UID 去代替一下。第二， random to string 对不对？每次发一个请求 ID 就是接下来。比如我去填充它的 class name，它的 class name 是什么？同学们想一想。代理对象 class name，我们通过 master 是不是也可以找到 Max 的点 get declare 声明，这里边有一个当前方法所声明的 declare class。


第二， get class name，这是不是也可以？对不对？接下来你再去全都是通过代理去走的哈。 set master name 就非常简单了。这里边直接就是 master 点 get name 是不是接下来非常简单？ request 点 set perimeter types，我们把所有的关键的属性都设置进去就好了。


master 点 get 对不对？还有最后一个实际参数是不就是request？点 set parameters 就是我们所带来的 x 就好了？现在我已经把请求对象设置好了，是不是紧接着我去发送出去？但是在发送之前，同学们还记得我们最开始第一节课讲的 r p c connect manager 吗？ r p c connect manager 里面它有两个你可以认为是有两个核心线程去做的事情。我们来回看一下之前我们去讲的 r p c connect manager 连接管理器。首先 connect 方法是去做的，第一件事情就是一个线程建立连接，还有另外一个叫做 truth handler。选择一个业务处理器对不对？其实同学们想一想，我们在真正去使用代理的时候，是不是请求对象包装好了之后，我应该选择一个实际的 client 的它的业务处理器去发请求？这里边就简单了。这里面我们直接这样去写 r p c connect manager。


第二， get instant，因为这是一个单例，是不是第二， truth handler，这样 true handle 里面它是不是会帮我们去返回一个可用的 r p c client handler？ r p c client handler 里边是不是有对应的 send request 方法可以去发数据？发数据是不是需要 re r p c request？是不是我们通过代理的时候提前已经设置好的？所以逻辑都是非常紧密的哈，一环扣一环的。小伙伴们要稍微体会一下哈。


r p c connect handler 我就叫做 handler 了哈，有了这个 handler 之后，我们 choose 选择了一个handler。很简单，我就调用真正发请求，第二发请求是不是 send request，最后给我返回一个什么对象？同学们想一想，返回的是一个 i p c future 对不对？我们可以叫做 future 对象。 future 对象。我们是不是可以根据他给我的 time out 去给它定义一下，对不对？我说 future 点 get 这个方法是不是在这里等待它多久？比如我等待多久？我说你等待时间超长时间，你自己去设时间戳，你自己定义。比如我自己定义的时间戳是 time unit 点 second 秒，是不是我可以同步阻塞多长时间？整个从我发请求，这是异步的对不对？它真正的方法是异步去发到我们的 solo 端，我接着 39 行执行完了之后，我可以走第 40 行。


get 方法相当于一个同步阻塞，因为它底层是一个 a k s，是不是？你们还记得吗？是一个同步阻塞，所以你这种方式它本身也是一个同步阻塞。它返回一个 object 是什么？就是 inwork 方法调用的一个结果。这个结果无非就是我们整个调用了实际的接口的代理类的一个结果。所以我直接把这个结果返回去。这个结果就是响应信息的object。


我不知道小伙伴们能不能理解我说的意思，为什么我说这是一个同步的过程？因为我 39 行，虽然是异步的，但是我第 40 行的时候直接调用 get 方法把它阻塞住了。所以如果你这样去写，我写了好几个send，这 4 个 send 都是并行的去发的，这肯定都是异步的。但是我最后 get 在这同步的去阻塞住了。所以其实整体来讲，虽然是 future 模式，但但是这种 future 模式，我这种写法，它也是一种同步阻塞式的。


代理调用就是代理的调用。好了，基本上我们这个方法就写完了，我不知道小伙伴们能不能理解，这个才是真正的代理的调用哈。代理接口调用方式OK，这是代理接口调用方式，你具体它代理的是哪个类，我不关注它到底代理的是 user service 还是 hello service，我不关注，我只需要关注代理对象。实际我知道了，我真正调用的是 user service 的什么方法，我能拿到代理，他传递的参数是什么？我能取到，帮他去选择一个实际的代理的业务处理器，去发请求，去在这阻塞等待结果就好了。


这就是一个同步阻塞式的代理调用方式。好了，我们这节课基本上就把同步阻塞式的代理调用方式已经讲完了。我们这节课暂时先到我们下节课的时候再跟小伙伴们去讲异步的方式。我们同步的方式其实你会发现他没有用到。什么没有用到。我们上面损传过了， class 对象只有异步的时候才会用到。好了，我们这节课先讲到这，谢谢小伙伴们。

