---
title: 2-6 整体框架联调测试
---

# 2-6 整体框架联调测试

[image](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/e247fab9-e1ed-457f-af69-a0d8a549b4ca/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XMAUN2M6%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T230047Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDBk%2FbvN%2BkeHuRSnyqwp3TwCrYNXC4tOLHQ2v%2F%2FggyjeQIhAMbRfwsFKl%2FIUOm9OHIdQ0x3grhvZ8xklz9iU74kIAUJKogECMb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1Igyay7H%2BDbSF0zjdRzEq3ANaEDZQuP5Egxuds8wxg7poVO2UfLA9BCBJ3q8i2KKL7gl3kmZcBKqV82h2XGIjO8xMitDrVFLoI69qKxR1hQjv8%2FZHmNjLz7j4mslqktzkLB%2FjcbR3N%2FDNxWVTQ3YnXbO0aR5rHa4Rguq706z1MdoA3rSzhnysv%2BmGeJdankcnwR2YwaiCWYHHqncSpP7AVn8s%2BCo3z5Gw74YIetbpzLrtVdCMkV2hSGQRpz%2BEzqXEx%2FZ6O%2BjvcPwyckmM0CaBVVljf10Bu93bvf09jsoo6tgbWlFkWVDPHTU5sUgZ0XuOR1xnvsC4GVow7fM48wIvyFD5JjZV5V3cwtiZtX%2Bryvlq%2B6XSnD7gV0G0fdJCHCjBXubcEuksIcJO6JDRqO%2FLnAS6GSrBawj%2FL%2B0LSYkopZEp6SoFmGP81T%2Br2tYtr1Bz%2B%2FOmrxKWvmrWkkiH8GGha7%2FBrpsLBAvLDjY9el6YCkstbmpMY0Luoe8JbK4qZlZRAKb1M%2BTNjgiNfIRxlTLPU4%2FLXcWgbwdMV4CXsKpYRIef1VbE%2F%2BSG%2BugyWGwvGU%2B0g32Az2CPeWs4DFonYEb9Yn9lN%2FvzlgCN4gsyaMBRZ2omJXOW7DeyzeaqwaH3Uv4MLDtBXwunD1U%2FXSgDNjCVt%2F%2FSBjqkAQoTfvKpXtZlho076zSKS%2BosJ7MschDUF6AdXHWZcbbdI6HgippJ5yS07wzwvkMcwDJc1FVbg474%2BOOOXQUmglA%2FM%2F6qM6%2F9kmYgK4WF9nKxARredmGPfTsGi1CEFYa047lfAYEqCESgUDWZjZPTAOqQO1Jh3FNLRGRZYkXJ6qa7qkRlmY9gY%2BTXqXfZLCEhPtx2A5W17O5rqjfZ4tekEgSE0yyj&X-Amz-Signature=3e567f02bdfb73e46de0097fe2daacb63b4e05ddc4d90d8b9efdbe3e845b21ba&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

hello，小伙伴们大家好，这节课我们来最终把我们自己实现的 RPC 框架做一个测试，让大家看到实际的调用结果。上节课其实我们已经把我们具体的服务的启动类，也就是 RPC service config 已经完成了。接下来我们来看一看。我们老师已经提前写好了我们的单元测试。单元测试无非就是两个，第一个就是我们的 COM 点 b f x y，点repeat，点 r p c，点inwork，点consumer，点 test 在这个包下面。第二个是在我们的 provider 的 test 包下面。


这两个首先我们要看一下，要知道我们要做发起远程调用，所以我在这里定义了一个接口，叫做 hello service hello service 其实我还可以定义一些其他的接口，比如user， service 等等都可以去定义。我在这里先定义了一个 hello service，它具体两个方法，传一个字符串，还有一个传一个 user 对象。具体接口的实现类在哪里？在我们 provider 这一方，因为 provider 是相当于服务的提供者，服务的提供者有实现调用 hello name， hello user 点 get name 就是 user 点 get name 获取 user 对象的名字。


好了，我现在问你，我们现在应该怎么去实现我们r、p、 c 的调用？我们首先看一下 provider starter，现在老师是以硬编码的方式去完成的，没有跟 spring 整合，所以我们就需要去自己去把一些关键的配置类去给他应援码出来，让他组织好。我在这里边去起了一个线程，在线程里边我们所有的核心代码就在这里。


首先我们知道我们每一个具体的服务的提供者的配置类都是叫做 provider config。首先我把 provider config 去创建出来，我去给它指定对应的 interface 就是我们对应的。我们看到接口的名字 Com 点b，f，s， y 点什么什么什么一大堆。


第二 hello service，说白了是谁？就是我们对应的这个类，它的权限包名加上类名地址。紧接着有了它之后还不行。为什么？因为我们对应着 provider config 里边，它需要一个比较关键的参数，就是 reference 接口它的实际的实现类的实例对象。所以老师在这里强制的手工的去把它创建出来了，调用 hello service，它的类加载器就是class，点 new instance 方式把它直接强制的去弄出来，给它 set reference 放到引用里了。我是这样去写的，如果后面跟 spring 集成就不需要了。我们可以用这种自己写一个自定义注解的方式，就把它自己初始化放到此吞并容器中，跟我们的 provide config 去关联起来。


接下来就是什么，因为我们不仅仅是一个interface，可以是多个interface，所以我们要有一个集合。在这里我只是写了一个 hello service implements。好了，我最终把集合创建出来，把我们想要引入配置的 provide config 去加到集合中。最终我们去 new 出来我们的服务启动类，也就是我们的 r p c server config 去把它 new 出来，把对应的一个 provider config 列表放进去，去给它设置端口号。最后调用它的 export 方法。 export 方法做了什么事情？这是我们上节课讲的。首先是 new 出来了，我们的 r p c server，就是真正的我们的 Nike server 已经启动了。紧接着把之前的 provider config 列表一个一个的去循环，去注册到 r p c server 上，是调用了我们的 r p c server 的 register processor 方法。这样我们整个的服务器端已经启动完了。


服务器端启动完了之后，我们在这里边可以先把它运行起来，看一看这个结果，预警起来，运行起来之后，它会有两个日志，会打印两个日志。我们耐心等待一下哈。就是我们之前所写的start。我们的 repeat RPC success。回调的时候会有一个否定。当前的端口，就是本机地址加上8765，这是我设置的。我们当前的服务端已经启动起来了。


再看我们的客户端是调用，这方老师实现了两个方法，一个是s、y、n、 c 同步调用，还有一个是a、s、y、n、 c 异步调用。我们先看一下同步调用。我们说了，我们所有的r、p、 c client 现在都是把它 new 出来，为什么我去 new 出来就全是硬编码把它 new 出来？因为我们没有跟 Superman 集成是不是？所以我们就用最原始的 Java API 去使用就好了。把它 new 出来之后，我要首先第一点，我要知道它的我要连接的 ip 地址跟端口号。我要连接的，比如是一个 ip 地址是本机的8765，当然这些你对应的客户端可能都不知道这个地址。


如果没有ZK，其实如果有 zookeeper 作为注册中心，说白了，我们的服务端启动的时候， export 就应该把每一个服务的 IP 端口，包括每一个服务的 provider 的一些信息，都应该把它注册到 ZK 上。我们的 consumer 就是服务的调用方，应该直接从 ZK 去拉取服务列表。所以这些IP，人家地址端口号都应该是从 ZK 服务列表中去拉取出来的。包括什么？包括我调用的 hello service。这个 hello service 我也完全可以放到服务列表中。当然如果这样去显示调用，我肯定会依赖个它的 API 的。这么一个包是肯定的。接口包。我在这里面去同步的去调用 inwork a single， inwork single 去调用。在这里我调用它的 hello 方法。传进去值是张三。这种方式是同步调用，为什么？因为我们在 in worker 实现的时候，虽然这里边 new 的是一个什么， new 的是一个动态代理proxy。它动态代理它具体的实现是 r p c proxy implements。它最终调用的时候会调 inwork 方法。 inwork 方法是不是在 handler 发请求之后？虽然这一块是异步的，但是它紧接着在第 42 行的时候，它是同步的阻塞的，所以我们也管它叫同步的。 RPC 要用是这么来的。我们回过头来看什么？看我们具体的客户端的 start 哈，我们来运行一下哈。当然其实我们运行是肯定没问题的哈，我们在这里去调用心口同步，我们去右键去执行一下。


好了，同学们请看。在这里hello，张三已经出来了对吧？因为我们给他传的是张三。hello，张三已经出来了，这是没有任何问题的。在这里小伙伴们要注意一点，老师在之前写代码的时候，有一个小的问题，它会报一个空指针异常。在这里我提前已经把它修复了。在什么地方？其实是在我们客户端创建的时候，就是 f p c client 端创建的时候，它不是应用了连接管理器，它会把连接去加入到我们的缓存中，在我们往下去拉再去调用。真正去加入缓存中的方法就是 add handler 的时候。在这里 add handler 的时候，质景太老师也打了一个断点哈。我刚才测试的时候发现这有一点小问题。我们之前获取远程的地址的时候，我是，我直接 handler 点 get remote beer 去这样去做的。但是在这个时候，因为是异步的，可能我们的人特别还没有通道，还没有被激活， active 还没有被激活，它只是有了channel，但是可能还没真正建立连接激活，所以可能还没有去走到这个方法的时候。现在 remote beer 可能是空的值，所以我们换了一种方式去写，不用这种方式去做了。


总之，你要获取 remote 地址很简单，我们只要它连接服务器的启动，我们的客户端去连。通道。肯定最开始有一个注册，注册会拿到channel，我们直接通过 handler 点 get channel，点 get removed address 就可以了，这样就不会抛控制人异常了。但这里边我会有一个提供一个 get channel 的方法，在我注册的时候，我的 channel 就有了，通过 channel 去拿到我们的什么，我们的 remote address 用这种方式更好一些，这样就不会出现异常了。


好，是我简单的去修复了一个小的问题，我们回过头来再去看一下我们刚才的代码，哈，我把它先都关掉了，哈，保留我们的 provide starter 跟我们的 consumer starter。目前我们现在是已经把 consumer starter 停掉了。现在我再去启动一下 consumer starter。当然我现在启动它的时候，我想调用另外一个方法，就是 a s y n c。因为同步的。刚才我们已经看到是成功的异步。这里体现在哪儿？我们用编码来跟大家简单来介绍一下。


这个异步主要体现在我现在也是创建一个对象，我去发起连接，我去调用 inwork a single。我要知道我自己的服务列表是 hello service 对不对？在这里你看我调的是 call 方法。 call 方法调 hello 传个李四，我调 hello 传了一个user，看见了吗？它会返回两个 future 对象。它说我们这两个它是异步的，当我真正去调 get 的时候，才是同步阻塞的。所以把我们阻塞的时机交给了用户，就交给了实际使用者。它可以自己去控制，它可以去发起 100 次靠调用，最后做一个 get 阻塞，这次都可以。所以它的异步是体现在这儿了。
OK，其实我们来看一看具体的异步。因为这两个 hello 方法是不是一个？哈，为什么这么说？因为我们看一下hello，一个是传一个字符串，还有一个传一个 user 对象，它肯定不是一个，所以它对应的实现也都不是一个。虽然你看到最终返回的是这样的。


OK，我们来调用一下。在这里 a C 口我们去直接 rise Java application 去执行一下。好，同学们请看他会直接返回什么？返回李四，返回王五，因为我们这里传的是李四跟王五。OK，这就证明我们整个的 RPC 框架已经实现完成了。但是现在我们是完全的使用 Java 的方式硬编码去做的。所以其实我们还是希望如果能跟 spring boot 或者跟 spring 去整合起来，这是最好的。后边我们会跟小伙伴们去分享两个小的作业，一个作业就是我们怎么去跟 spring boot 整合，我简单的把整个思路跟小伙伴说一下。还有一个我想去加上 zookeeper 应该怎么去做。我们现在其实就是最开始老师说的那句话，我们其实做一个 RPC 框架，我们应该一步一步的去做，

[image](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/5bc0ff07-262a-4a93-b743-3984fff3dc6c/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XMAUN2M6%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T230047Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDBk%2FbvN%2BkeHuRSnyqwp3TwCrYNXC4tOLHQ2v%2F%2FggyjeQIhAMbRfwsFKl%2FIUOm9OHIdQ0x3grhvZ8xklz9iU74kIAUJKogECMb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1Igyay7H%2BDbSF0zjdRzEq3ANaEDZQuP5Egxuds8wxg7poVO2UfLA9BCBJ3q8i2KKL7gl3kmZcBKqV82h2XGIjO8xMitDrVFLoI69qKxR1hQjv8%2FZHmNjLz7j4mslqktzkLB%2FjcbR3N%2FDNxWVTQ3YnXbO0aR5rHa4Rguq706z1MdoA3rSzhnysv%2BmGeJdankcnwR2YwaiCWYHHqncSpP7AVn8s%2BCo3z5Gw74YIetbpzLrtVdCMkV2hSGQRpz%2BEzqXEx%2FZ6O%2BjvcPwyckmM0CaBVVljf10Bu93bvf09jsoo6tgbWlFkWVDPHTU5sUgZ0XuOR1xnvsC4GVow7fM48wIvyFD5JjZV5V3cwtiZtX%2Bryvlq%2B6XSnD7gV0G0fdJCHCjBXubcEuksIcJO6JDRqO%2FLnAS6GSrBawj%2FL%2B0LSYkopZEp6SoFmGP81T%2Br2tYtr1Bz%2B%2FOmrxKWvmrWkkiH8GGha7%2FBrpsLBAvLDjY9el6YCkstbmpMY0Luoe8JbK4qZlZRAKb1M%2BTNjgiNfIRxlTLPU4%2FLXcWgbwdMV4CXsKpYRIef1VbE%2F%2BSG%2BugyWGwvGU%2B0g32Az2CPeWs4DFonYEb9Yn9lN%2FvzlgCN4gsyaMBRZ2omJXOW7DeyzeaqwaH3Uv4MLDtBXwunD1U%2FXSgDNjCVt%2F%2FSBjqkAQoTfvKpXtZlho076zSKS%2BosJ7MschDUF6AdXHWZcbbdI6HgippJ5yS07wzwvkMcwDJc1FVbg474%2BOOOXQUmglA%2FM%2F6qM6%2F9kmYgK4WF9nKxARredmGPfTsGi1CEFYa047lfAYEqCESgUDWZjZPTAOqQO1Jh3FNLRGRZYkXJ6qa7qkRlmY9gY%2BTXqXfZLCEhPtx2A5W17O5rqjfZ4tekEgSE0yyj&X-Amz-Signature=6a913ca246772f09514cbf3fa071e65a16c02d64b22c56cc9e8fcbc0ac7b8a5b&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

我们首先第一步应该完成这些事情应该完成的事情，起码我们的远程方法调用 r p c，用 Java 去做到我们调用接口，他另一方面就能去把具体的接口下面的实现类去执行给我返回。结果这块我们去实现了。我们已经实现了我们之前给大家看的这幅图的所有的内容，粉色的地方哈，我单独提出来的，后面可能比如我们跟 spring 整合的时候，我们这样去把它模块单独提出来更好一些。


OK，我们整体的课程就是整体的 r p c 框架的课程。已经到此全部结束，感谢小伙伴们收看，希望小伙伴们能有一个非常好的一个收获。OK，这节课就到这。


