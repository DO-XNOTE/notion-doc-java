---
title: 1-13 【源码品读】Dubbo调用链路深度解析
---

# 1-13 【源码品读】Dubbo调用链路深度解析

[image](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/87124d24-7f8f-4a43-b322-9edcf181c877/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RSR52IB5%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T225901Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDs47J8GOIzDv2OhuVlFr%2BPZKE9NCpNC53O2FUqM0jjDgIgd24LB9b34UfTmMUUoPCUl3mTnFASrRejPLEnF0rTZOUqiAQIxv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDHK3Fwyhn7W94z3iwSrcA5SDbN9smQo%2FfuCGlo4%2FTkpgH%2FnnisxAsxTshUyEDtFtpA6FcNMcsIvQ7wcx9Cg%2B5xqSGpBoAmOdQ6H3cTZ1Wcwvl%2Bk89lXWi2%2FC0wRkGWqhonljW4VYwh%2F6O56iA8njBEuzN1aEXHpRRZHYvRqBKSVLq4EydALBxa9YpV9fbEGz7KqK54JkOE4q8jYu7sYjLme%2BjKmMYCTPFgSb3zkUNcQ3ILEVL9cVKzqmFkQyTl%2BR%2FpIf2MsQs31aMOGQ%2FsHOAqQSbPoh7gm2enEld0YLds3tdC78M0sGkuHF5xsg964%2BUj069Qx0UhWvIFZ11O6uyRDyQUR2hkfTC6tjdv46OZjvT4q9Yl7oc0O8D696DZzaXz4hjVP2rR89InP0WyLFFwITXs6aLqs2gPYNJO%2BFlEGNmQhA3L%2FEJMXA08SRSKABz%2Bf9fzhEnMX27qnWZHGxFys4TRX7omIfn9qiz3JmgnROns07QoJzg0wR1Px2tllP5ap8jhIb77XSg%2BKNQUWPRcfhu8QMdGIBz0cr7JmxrPVcOXQv%2FfE5Nnb7RLERtZgCpyAurTX%2FlU8fom8Pb9YFUUA9AkxtCcb1Glppkh4P5aZzjz%2BhzYGIIshJ3VGfTMa4bSnrEThx7UBpRepvMPy5%2F9IGOqUBg15BMjx4IcWaEa65jZnyIfUlFRS1lKA5isEpjLnc4QaFwJmv1nTA%2FtL5rQv8uxsbIRTGZNniYj3uX4Q2eskTTMIEdmTjCCnrWeEc%2FT%2BmAzPeNKI173cz%2FpL2AQKP1Gr3etl%2BA97OPgZUWdTon06m4fPQ1nkLvqlQh2VJxzfkP5aNu05fYG8JEpmxkkApJrUSM5AFAFKPR0Igj%2FMsbo9jI1tA%2FP0%2B&X-Amz-Signature=a6f9ab4c56da1582890bebbf42819699ed0288967ff9ec897023d09121c25362&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

[image](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/12ed6496-c277-4190-a9d2-3c4dd76280f9/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RSR52IB5%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T225901Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDs47J8GOIzDv2OhuVlFr%2BPZKE9NCpNC53O2FUqM0jjDgIgd24LB9b34UfTmMUUoPCUl3mTnFASrRejPLEnF0rTZOUqiAQIxv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDHK3Fwyhn7W94z3iwSrcA5SDbN9smQo%2FfuCGlo4%2FTkpgH%2FnnisxAsxTshUyEDtFtpA6FcNMcsIvQ7wcx9Cg%2B5xqSGpBoAmOdQ6H3cTZ1Wcwvl%2Bk89lXWi2%2FC0wRkGWqhonljW4VYwh%2F6O56iA8njBEuzN1aEXHpRRZHYvRqBKSVLq4EydALBxa9YpV9fbEGz7KqK54JkOE4q8jYu7sYjLme%2BjKmMYCTPFgSb3zkUNcQ3ILEVL9cVKzqmFkQyTl%2BR%2FpIf2MsQs31aMOGQ%2FsHOAqQSbPoh7gm2enEld0YLds3tdC78M0sGkuHF5xsg964%2BUj069Qx0UhWvIFZ11O6uyRDyQUR2hkfTC6tjdv46OZjvT4q9Yl7oc0O8D696DZzaXz4hjVP2rR89InP0WyLFFwITXs6aLqs2gPYNJO%2BFlEGNmQhA3L%2FEJMXA08SRSKABz%2Bf9fzhEnMX27qnWZHGxFys4TRX7omIfn9qiz3JmgnROns07QoJzg0wR1Px2tllP5ap8jhIb77XSg%2BKNQUWPRcfhu8QMdGIBz0cr7JmxrPVcOXQv%2FfE5Nnb7RLERtZgCpyAurTX%2FlU8fom8Pb9YFUUA9AkxtCcb1Glppkh4P5aZzjz%2BhzYGIIshJ3VGfTMa4bSnrEThx7UBpRepvMPy5%2F9IGOqUBg15BMjx4IcWaEa65jZnyIfUlFRS1lKA5isEpjLnc4QaFwJmv1nTA%2FtL5rQv8uxsbIRTGZNniYj3uX4Q2eskTTMIEdmTjCCnrWeEc%2FT%2BmAzPeNKI173cz%2FpL2AQKP1Gr3etl%2BA97OPgZUWdTon06m4fPQ1nkLvqlQh2VJxzfkP5aNu05fYG8JEpmxkkApJrUSM5AFAFKPR0Igj%2FMsbo9jI1tA%2FP0%2B&X-Amz-Signature=1c08ef5aa0dec1af8537c1664967e0e1f0c6355b85e83d7a06b714986bd2ed49&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

[image](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/ee6515e1-40a5-4f0f-b171-90b6fa6bf80c/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RSR52IB5%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T225901Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDs47J8GOIzDv2OhuVlFr%2BPZKE9NCpNC53O2FUqM0jjDgIgd24LB9b34UfTmMUUoPCUl3mTnFASrRejPLEnF0rTZOUqiAQIxv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDHK3Fwyhn7W94z3iwSrcA5SDbN9smQo%2FfuCGlo4%2FTkpgH%2FnnisxAsxTshUyEDtFtpA6FcNMcsIvQ7wcx9Cg%2B5xqSGpBoAmOdQ6H3cTZ1Wcwvl%2Bk89lXWi2%2FC0wRkGWqhonljW4VYwh%2F6O56iA8njBEuzN1aEXHpRRZHYvRqBKSVLq4EydALBxa9YpV9fbEGz7KqK54JkOE4q8jYu7sYjLme%2BjKmMYCTPFgSb3zkUNcQ3ILEVL9cVKzqmFkQyTl%2BR%2FpIf2MsQs31aMOGQ%2FsHOAqQSbPoh7gm2enEld0YLds3tdC78M0sGkuHF5xsg964%2BUj069Qx0UhWvIFZ11O6uyRDyQUR2hkfTC6tjdv46OZjvT4q9Yl7oc0O8D696DZzaXz4hjVP2rR89InP0WyLFFwITXs6aLqs2gPYNJO%2BFlEGNmQhA3L%2FEJMXA08SRSKABz%2Bf9fzhEnMX27qnWZHGxFys4TRX7omIfn9qiz3JmgnROns07QoJzg0wR1Px2tllP5ap8jhIb77XSg%2BKNQUWPRcfhu8QMdGIBz0cr7JmxrPVcOXQv%2FfE5Nnb7RLERtZgCpyAurTX%2FlU8fom8Pb9YFUUA9AkxtCcb1Glppkh4P5aZzjz%2BhzYGIIshJ3VGfTMa4bSnrEThx7UBpRepvMPy5%2F9IGOqUBg15BMjx4IcWaEa65jZnyIfUlFRS1lKA5isEpjLnc4QaFwJmv1nTA%2FtL5rQv8uxsbIRTGZNniYj3uX4Q2eskTTMIEdmTjCCnrWeEc%2FT%2BmAzPeNKI173cz%2FpL2AQKP1Gr3etl%2BA97OPgZUWdTon06m4fPQ1nkLvqlQh2VJxzfkP5aNu05fYG8JEpmxkkApJrUSM5AFAFKPR0Igj%2FMsbo9jI1tA%2FP0%2B&X-Amz-Signature=99aa8011098c35e61a086e78a05fe7434ce59f7beb5027ce510108ed444e7196&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

各位同学们，大家好，这一小节是咱整个微服务章节中跟代码有关的最后一个环节了，因此它也是真正意义上的收官之战。在这个环节当中，咱要去品读一下 double 协议的解析过程，我们知道 double 是阿里出品的，对不对那阿里特别流行的就是。


996 享受福报了，我们来围观一下。在这个 996 打鸡血的高压状态下， double 的代码写的是群魔乱舞还是非常的优雅。本章的代码阅读依然沿用前面几章的方法，那就是通过 debug 模式，然后从double。



调用链路中的某一个环节开始，从头到尾走一遍整个流程。
我这里挑选了在调用链路中最恰当的一个切入点，那就是 double in worker 咱就从 double invoker 开始，陆续从上到下一个挨个走完所有流程，最终直到 net channel send 也就是最后一个方法，调用链路在发起调用请求前的最后一步。这里。 OK 同学们准备好的话，跟我一起奔赴intelligi。


打好这最后一场收官之战，编程使我快乐 996 是我的福报。想起过去这么几周接近两个月时间享受福报的过程，真的是感慨万千，相信同学们一定是收获良多，迫不及待的想把学到的知识用在自己的项目中，在小伙伴面前秀一番了。先别着急，秀咱这个最后一张代码阅读，先把它搞定。我们这里直接进入到哪一个类呢？大家看它的类名叫 double in worker 它是在整个调用链路中的一环。我们为什么选这一环呢？我们之所以从中截取一个环节，是因为 double 的调用链路非常长，其实它远比咱分的这个调用链路要长得很多。我们把这个长到步行的调用链路，从中一节为二，把最关键的部分拿出来跟同学们分享一下。


好，我们在 double inworker 中的 invoke 方法，这里 77 行打一个断点，大家选择源码的时候一定要选择正确的版本这里可能会看到好多个 double 版本，我们点击的是二点七点三的版本。当咱把断点打好以后，紧接着要把两个项目启动，分别是 double client 和 double consumer 因为我们发起调用，实际上是把这个请求调用到哪里。 double consumer 对不对？因此这个 consumer 要以 debug 的模式启动 double client 就以通常的 run 方法启动就可以了。


OK 那咱把这两个项目已经事先启动好了，这时候转战到 postman 发起一个真实的方法调用谁呢？调用 630 端口的 publish 方法 123 走起断点 door 在这第一行咱就接触到了一个拼装好的 RPC invocation 类，这个类在它的上游调用链路中已经拼装好了，咱这里直接拿来就用这个 invocation 对象里封装了当前咱调用的这个方法的一些特征量。比如我们看一下它其中包含的属性。这第一个变量是 method name 也就是方法的类型。接下来是这个方法它接收的参数的类型。再往后就是方法接收的参数了。那前面的几个变量它构成了当前方法的签名以及方法所接收的实体类的参数。


再往后大家可以看到有一个 attachments 看起来以为是附件，其实不是。你看这里面的内容包含两一个是 interface 它是当前 service 所继承的这个接口。通过前面 double admin 里面我们去做服务查询的时候可以看到这个就是它的服务名，也就是说它用接口的类名当做服务名。下面一个是 time out 默认是3000，也就是 3 秒钟。
再往下有两个比较重要的参数一个叫 invokerinvoker 是谁呢？它包含了很多我们需要发起一个真实调用所需要的信息，比如它这里一个属性 clients 是我们真正发起远程调用所需要依赖的一个类。再往下有 RPC 这当中很重要的一个概念 version 也就是你方法的版本号。然后还有一个 URL 这个 URL 可不是我们 HTTP 的URL ，你看它的协议栈是 double 也就是说它是通过 double 协议来真实的发起一个远程调用。那可以看到在这个 double 协议的 URL 当中，不仅有 IP port 还有后面跟的方法特征量这个方法特征量就是方法的名称、参数等等，它指定了你的 double 协议如何找到对应的服务器地址。


那再往下看，除了当前看到的其他几个属性以外，它还有一个 invoke mode 这也是一个蛮重要的它这里是 synchronize 同步，也就是说当前的调用其实是一个同步阻塞的调用，它不是一个异步调用。看完 invocation 以后，咱往下接着一步一步看。这里使用 RPC utils 从当前的 invocation 当中拿到你的 method namemethod name 就是 publish 拿到 method 以后，我们刚才看到 invocation 当中有一个属性叫 attachment 那这里接下来就往 attachment 里面加入两个参数，一个是当前版本的 version 也就是说你的 rp C 的协议栈其实可以为一个方法指定不同的 version 那如果你在调用的时候指定了你调用是0.0，这是默认的 version 那么他就会去寻找当前的默认版本。如果你的 client 暴露出的接口其实是一个多版本接口，也就是说同时有很多个版本在线上运行。那么你这里指定调用哪个版本，它就会去寻找哪一个版本对应的 client 咱再继续往下看。这里如果他的 client 也就是真实发起调用的 client 只有一个的话，那毫无疑问，我们从这里面取的第一个也就是 exchange client 那接下来这里会判断一个 is one way 什么是 one way 呢？我们进去看一下。


走进去 its one way 其实很好理解，咱去买机票到一个地方游玩，大家都会选择是单程还是往返，那这个 is one way 就是有去无回的意思。那它这里会从你的 invoker 当中查看你方法的 parameter 是不是包含了一个特殊的属性，那就是 return key 如果咱没有包含，那代表着什么意思呢？我们直接返回，看到这它的值就会变成了 false 也就是说你不是一个单程调用。那何谓单程调用呢？我们往这里看一眼就明白了。


同学们看到这里， if 条件，如果你是一个单程调用，它这里返回一个 asynchronize RPC result 当中构造的 default 默认返回方法。那这个默认返回里面有什么内容呢？我们点进去看一下，它其实上是会返回给你一个空的返回值。你看头两个参数都是空，最后一个把 invocation 传入进去。那这前两个空的参数用来构造什么？控造一个实际上没有任何意义的返回对象。也就是说你的方法调用并不需要真实的等待调用方返回一个结果，而是在发起调用的同时，就直接返回了一个默认结果。


你知道调用方处理成功还是失败吗？其实并不知道，我们只用把这个调用请求送出去就好了，相当于是什么接送机服务，我们只把这个人送到机场好了，他什么时候回来，他自己爱回不回，是出错还是怎么样，咱都通不管。如果你不是一个 one way 的调用，那是 two way DOS ，你要返回一个结果给我怎么样走下面的 else 方法，我们把断点放过去。在这里咱也构建了一个 synchronize RPC result 只不过这个 result 还要等待一个 future 的返回结果。


future 大家都很熟悉了，对不对？这是 concurrent 包下面一个非常重要的内容，咱们平时开线程池的时候，什么 competition service 都要用到这个 future 接口。那这个接口在这里将要发起一个调用，我们先把断点打上，不要让它溜走了，发起什么调用呢？同学们看到这里， current client 的 request 通常来说，以咱开源软件的尿性，通常不会直接让一个 client 发起调用，而必须通过一种代理的方式，我们不妨点进去，把断点跟进去。


这里看到他对象中实际有一个 client 对象，这是谁他是一个代理的实例。你会发现几乎在所有的开源项目中，但凡要发起网络调用的时候，它通常来讲都是一个类当中藏了一个代理对象，实际调用是从这个代理对象中发起的，这就像是开源软件中约定俗成的那个潜规则一样。那我们再跟进去一步，看看这个 client 里面它做了什么操作。


同学们看我说的没错吧，在 header exchange client 当中，它其实也并不是那个直接发起调用的一方。这里还有一个 channel 对象藏在这这个 channel 实际上是一个代理的通信通道。我们看它的类名是什么呢？这里看到了 nettie 的身影，只不过这一个 channel 可不是 nettie 轻生的，它是 double 和 Netty 私生的，你看它的包名实际上还是挂在 double 项目下面的，只不过是 double 用来通过 nettie 发送一个请求的代理通道类。我们接着回到刚才打断点的地方，不妨再跟进去一步，看看这个 channel 底层做了什么操作。第一个 if 条件是判断你当前的通道有没有被关闭。因为如果有过网络抖动或者。


任何异常原因通道关闭了，那这时候就要抛出一个异常。那假如你通道没有关闭，我这里将要构造一个 request 的对象，这个 request 可不是httprequest。
它是 double 里面封装的一个类。这个 request 当中包含了三个比较重要的属性，分别是 version 这个 version 可不是咱前面提到。


的你暴露出的接口 client 的 version 而是你当前协议的 version 不光后台的接口可以升级，那你的 double 协议也是可以升级的。它作为一个独立存在的协议层，有可能在以后的版本中会添加新的字段或者是删掉老的字段等等。那这里就要传入一个 double 的协议版本号，我们看到是二点零点二，把这个协议号放进 request 以后，接下来给它设置一个属性 set two ways 就我们刚才说的 two way door 它是 true 最后一步把 RPC 的 request 塞进去，这个 request 就是咱前面看到的 invocation 那个对象，它有方法的特征量，还有定位这个方法的 invoker 等等。


那接下来在真正发起请求之前，你看它这里生成了一个 future 因此这个方法返回的并不是一个已经处理好的 response 而是这个 future 接口让你通过 future 接口再去拿 response 好，我们这里就要真正的发起一个 send 请求调用了，我们不妨点进去看一下，走，你我们再点进去一层。


那这里就到了发送方法请求的地方了。首先判断当前连接的连通性。同学们注意到，但凡是跟网络请求打交道的底层接口，他对当前 connection 的连接一定都会做很多检查，因为咱知道连接会因为各种网络抖动不稳定的原因断开。所以当前的这个 if 条件如果你需要 reconnect 需要重新连接，或者你当前的连接断开了，怎么样？我这里调用 connect 方法重新打开一个连接，这里的连接是如何来建立的？我们就不深入看了。


不过这里跟大家提一句，你用 double 的时候，它默认的连接方式是谁呢？是 Netty client 我们前面图文教程有讲到，它底层依赖的组件。那这里同样也有另外的 client 的实现。不过 NAT client 是推荐的方式，我们返回到上一层。那连接建立好了以后，我这里接着拿到一个 channel 这个 channel 就是依赖于当前连接建立的 net 的通信通道。接下来对 channel 的连通性又做了一番检查。那我们继续往下走，到这一步，我们就要真正的发起一个 double 的调用了。我们跟进去，看他最后一道，这里就是方法发出前的最后一步了。我们这里拿到的 channel future 的返回值，它是 net 的组件。接下来咱们把这个断点完全放开，让它回到最外层。最外层是哪里呢？就是我们在开头的 double inworker 这里发起调用的地方。那它获取了一个 response future 以后，我们接下来要怎么样啊？它这里有一个很风骚的操作， async RPC result 这个类也就是结果类怎么样呢？注册到 response future 上，这是什么含义啊？就是有朝一日你 response 回来了结果以后，那我能监听到这一个动作，从而做出自己的一些响应。
同学们看这种编程方式非常的巧妙，咱们在处理异步方法的时候也可以运用这种方式，我们不妨进去学一下，看这个 subscribe to 里面做了什么操作，其实非常非常简单。
咱的 complete future 有一个方法就叫 when complete 它就是一个回调函数。这个 when complete 可以探知到两个结果，分别是你的正常调用的返回值，以及你在整个调用过程中如果发生了异常，它抛出了异常。那在咱代码中这个 if 条件这里就处理的是异常的情况，下面就是正常返回的逻辑。所以同学们也可以好好利用 compilable future 这个类的这种特性来在你的代码中实现这种异步回调的机制，非常的高效优雅。所以在这里我想把 double 和 Netflix 公司的众多组件做一个比较。我们看到 double 实际上也是利用了这种异步编程的方式。但是跟 Netflix 的组件比如 high streaks 相比， double 在这种异步调用的函数式编程的应用方面，相对来说是叫张弛有度，这个度拿捏得非常非常到位。那他并没有像 high streaks 这样通篇全部使用异步调用，让人眼花缭乱，摸不着头脑，而是在某些关键链路上把这个结构用函数式编程体现的更加清晰。所以从这个角度来说，不管是代码的可读性还是以后可维护性、扩展性我认为阿里巴巴在 double 组件的处理上是远比 Netflix 组件要优秀的多的。这里给 double 的团队，也就是 hs F 的团队点一个赞。


那咱的 subscribe 方法返回了以后，接下来怎么样？这个整个 asynchronize rp C result 就完整的返回了，换掉断点。那后面的故事就是顺理成章的发展了达布框架，把这个请求发送出去，然后获得到正确的返回结果，并且返回给客户端。


同学们刚才看到的全是 double consumer 发起 double 调用的过程。那接着咱要看一下 double client 在接收到一个 double 请求以后，它是怎么来处理的。这里我们打开这样的一个类，它的名字叫做 double cold see 就是这个类。然后咱再把 double client 以一个 debug 模式来启动。启动好之后，咱在这里打一个断点，在它的 decode body 这里打上断点，然后尝试着发起一个远程调用。 The postmanly. 这里断点已经走到这儿了。那咱看一下它在接收到一个 request 以后是怎么来对这个请求进行 decode 也就是解码的。这个方法的代码呢有点那么长。而且啊层层逻辑嵌到 if else else if 可读性也不是那么高，可能是那段时间加班比较猛，被 996 给逼出来的。
早安从第一行开始往下稍微过一下。这个入参 header 是一个 bat 数组。然后咱这里定义了一个 badflag 取这个当前数组中的012，也就是第三个数下标为 2 的后面还有一个 protocol 这个 protocol 它是通过前面已经得出的 flag 和一个 civilization 的十六进制数进行按位运算获得的。那我们往下走一步。接下来获取一个 request ID 它通过传入 byte 数组，然后指定一个 offset 的位数值把这个 ID 计算出来。那这里的值是238，它的 ID 转成了一个 long 型。然后这里的 if 判断把下面很长一段的逻辑一分为二。


怎么说？你看上面的这串 if 条件是 decode response 的，也就是对它的返回 response 进行解密的。那下面这个 else 逻辑是什么？是 decode request 所以从这个角度来说，这个整个流程在逻辑上还是比较清楚的，只不过在编码风格上没有很好的组织起来，这些 if else 条件看起来也比较绕眼。那接下来将 flag 和一个十六进制数进行一个安慰操作，如果它满足条件，那么将进到 decode response 那咱这里其实是发来的一个 request 所以它会进到下面的 else 方法，我们往后走一步。那这里进到 else 方法以后，咱要把这个 request 给它解析出来。第一步，创建一个对象，然后把刚才计算得到的 request ID 塞进去。第二步是把 double 当前的协议版本给它拿到，然后同样的塞到 request 里面去。咱的 flag 是一个 byte 类型。所以接下来的这一步从 byte 类型中的某一位获取到它是否是一个同步还是异步的调用。如果是同步调用，那有来有回，所以这里就是 set to way 等于 true 否则就是一个 one way 那么这里就是 false 操作，再往后依然是按文运算设置一个标记位，我们不去管它。我们走到这里。
接着到这一步，咱发现一行烂代码，什么叫烂代码了？同学们，假设这一步它不存在，我们往下看，接下来的 ifelse if 和 else 方法中，它是计算什么的呢？如果你当前的请求是一个 heartbeat 心跳包，那么它走下面的这段逻辑。如果它是发送的一个 invent 走下面的逻辑，然后咱再看这两行逻辑当中的一个参数 in 那这个参数就是咱这一行 123 行 debug 断点达到的这个位置。这一行所得到的 object input 这个变量它只在 if 和 else if 这两行代码中会用到。所以如果你的代码是走到下面这个 else 逻辑当中的，那实际上是不用计算这个变量的。因此这里更好的一种做法是怎么样把这行代码能尽量的移到 if 和 else if 里面，这样最好了，尽管这行代码会在条件分支里出现两次，但是考虑到咱大部分的有效请求是落在哪，是落在接下来这一步。这里才是正儿八经解析你数据包的地方。因此大部分请求实际上是落在这里。那它这里并不需要去额外的计算这样一个 object input 所以这里还是有一定的代码级别的优化空间的。 OK 我们把断点往下走，这一步咱没有用到，所以说就不去看了。


然后它是一个 heartbeat 吗？不是的，我们往下它是一个 invent 吗？还不是？它是谁呢？它是底层通过 Netty 接收到的一个正儿八经需要你去解密的那个数据包。所以咱这里需要判断一个 header 在你 channel channel 是一个 net 的通信通道。


在 Netty channel 的 get URL 中，你是否包含了这样一个属性叫 decode into thread key 如果你包含了这个属性指定它等于 true 那么就是说你这个方法是需要进行一步解密操作的。假如这个属性你没有加到 URL 当中，那它会给你指定一个默认值，就是默认让你需要进行一步解密的操作。咱往下走。这里声明了一个新的 decolable RPC invocation 我们在点进去之前，先来看一下它这四个参数。第一个参数是 channel channel 是什么 net channel 通信通道。第二个是咱发来的 request 第三个 is 是什么呢？它这个名字起的不是那么直观，它是一个 input stream 那后面的是一个标志位 particle 协议类型。 OK 咱进去看一下它是怎么组建的，非常简单，这里只是粗略的验证起一个值，它不可以为空。然后将它塞到自己当前的类变量当中。那返回回来以后，接下来的这个 D code 就是解析这个数据的核心操作了。我们点进去，但凡涉及到 D code 了，他很多都会参与暗卫运算操作。所以同学们对暗卫运算要比较熟悉。


我们往下走，看到这里一个 decode 的方法，咱进去这个方法里面，流程还是相对比较复杂的。第一行操作是做什么呢？它根据你协议当中定义的 serialization type 序列化的类型来获取一个序列化的类。咱这里前面图文提到了有很多个序列化的选项，he森 double 它自己的序列化选项。咱这里可以看到它的标志位是2，因此应该是一个 hashn 类型的序列化解析器。那么接下来这一步获得解析器以后进行一个解析，把当前的这个类转成 object input 的对象转成对象以后，那就挨个解析里面的数据了。这里先是拿 double version 来下手，看这里二点零点二咱发的也是二点零点二，这里解析的完全正确解析一个属性，就把它塞到 request 当中，然后还不忘把它塞到 request 当中的 attachment 变量里。你看这里有一个 attachments 变量，把它塞入进去，塞完以后咱接着继续往下读。


你看这个 in 操作，实际上它每次 read UTF 这个 UTF 是什么？是 UTF 杠 8 的意思。然后你每次就会 read 一个 UTF 杠 8 的字符串。那比方说下一个字符串，就是 pass key pass key 完了之后又是 version key 所以这里就严格的按照咱 double 协议中每一个位上它都包含了哪些信息来按顺序来把它解析出来，这里可不能前后颠倒。如果你把下面一行不小心移到了上面一行，那这个解析可就要出错了。那接着往下是 set set method name 我们走到里面，接着到了 DE SC description 这里解析出的是什么？大家看是你的入参 product 它的类型，我们把它的包路径 com IMock spring cloud.product 全都打印了出来。那接下来它要做的一件事就是通过反射工具把当前这个 description 转成一个 class 对象，这个 PT S 就是一个 class 接下来咱构造了一个 object 的数组，这个 object 的数组就是要传递给 double client 方法的参数。所以这几行代码的流程是这个样子的。


首先咱从反序列化中得到了当前方法所接收到的参数类型，然后把这个参数类型转化成一系列的 class 数组，就是这里的 PTS 并且在最后将 class 数组构造成一个 object 数组，你的 class 数组当中有几个元素，你也同样的要构造相同大小的一个 object 的数组。


那 object 的数组构造完了以后，里面的内容怎么填充呢？就是下面的 for 方法了，咱还是要从反序列化的这个对象当中依次读取到每一个对象它的值，咱这里就传入了一个 product 所以它这里 for 循环只执行了一次，我们看看它的 arguments 是不是已经获取到值了。


果然你看它这里的参数列表中已经得到了 product 这个 product 就是前面从反序列化的 Python 类当中读取到的一个入参，那它不是一个 class 类型，它是一个实打实的构造出来的 product 的对象，这里面的属性都是咱在调用方法的时候传进来的。接下来这一步，我们把前面获取到的参数列表的类型 class 类型添加到 attachment 当中去，紧接着再往后走。


这一步的 map 又是读取的什么呢？这个 map 其实是方法的一些特征量了，比方说你的接口 timeout 设置，还有你的 interface 的路径。我们来看一下，它这里有四个参数，分别是 path 还有 interface 这都是类的路径，还有接口名称，后面是 version version 是你要调用的接口，它声明的版本，这个不是 double 的 version 是你在暴露 double 服务的时候给你的接口指定的 version 那最后一个参数就是 time out 了。这几个参数，系数把它加入到了哪里加入到了 attachment 当中。
那最后一个操作，咱要对刚才已经解析出来的 arguments 入参做一个低扣的。那同学们可能在想了，前面已经不是解析出来 product 了吗？那为什么还要再低扣了一把？咱进去看一下。这里要根据你的 callback 函数的类型， callback status 来决定怎么个 decode 法。我们往后走，这里先获取到了 URL 然后从 URL 中判断 its callback 这个 URL 是 double 的完整调用地址，它是 IP 地址加端口号，再加上你的服务名称，后面巴拉巴拉跟了一大堆参数，从这里拿到你的 callback status 如果你的 callback status 是下面中的某一个 case 那么就要按照这里面指定的姿势来做 dq 的操作。


咱这里的 callback status 是0，因此它走到接下来的 291 这个 case 里面了，所以它对你传入的 argument 参数并不需要任何的解析，只要原封不动地返回就好了。接下来最后一步就是把 arguments 塞入到 attachment 里面，这里返回。那走到这， decode 的流程就完美结束了。最后一步，把 has decoded 设置成 true 告诉下面的调用链路，我的 decode 已经全部完成了，这就是 double 的协议解析部分的代码了。


OK 同学们，那咱这一节的课程就到这里结束了，我来带大家稍微回顾一下。咱前面看到 double 是如何发起一个调用请求链路的。然后底层是使用的 net client 在接下来，咱又通过 double code C 这个类看了 double 的接收端，也就是 double client 应用是如何承接这个调用请求，并且把请求中的内容给它反序列化解析出来的。那这两部分内容就是 double 的调用链路中比较核心的两个部分了。当然了这里只是带大家看了 double 这座冰山露出水面的那个部分，它还有更多的隐藏细节藏在水面，以下需要大家自己去探索的，万事开头难，任重而道远。这里给同学们开了一个好头，剩下的路大家还要自己去走。


那到这里，本节微服务课程的最后一部分，跟技术相关的内容已经结束了，可是还没有跟同学正儿八经的道个别怎么办呢？下一章我来带大家对整个的微附章节做一个简单的回顾，然后再跟大家聊一聊一些技术以外的话题。这些技术以外的话题可比单纯的学习技术要有料的多喽，浓缩着一个老法师。




