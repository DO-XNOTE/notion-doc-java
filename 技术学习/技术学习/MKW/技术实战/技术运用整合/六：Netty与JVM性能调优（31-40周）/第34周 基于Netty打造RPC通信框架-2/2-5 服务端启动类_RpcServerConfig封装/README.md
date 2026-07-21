---
title: 2-5 服务端启动类_RpcServerConfig封装
---

# 2-5 服务端启动类_RpcServerConfig封装

[image](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/fcb77e3a-1932-409a-91b9-5d32df9b7d03/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VBC6K7JR%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T230047Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQC0OBpAv6jjwG0uwsCAbLamM7%2FpyqOyVjCwVHxUNeA7BAIgGnalS49YXCNdnsxpHdyPWjI1esZ%2FQ4VbitR84CPICV0qiAQIxv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDE9tOsQHODOAGhNduSrcAxuMCnkmbQhY8bmJYiyIP%2BbwkYjxQS9yh%2FgdgSfG2umorv%2Bi%2FyR90CqwSUbzHjPZ16WhjbbtEukCX3JlAEg0bKHE6y3xqw4mKehdNOQ9U0SLgniDzJEU0qnRZajiU6uBAJlmBdF9YPaou7WoeqaMwdIk%2BVO5wciyfXcC0YG7Nm5vtvXiclIGgH6kyjhTx0Z7SpK4BTZiCXPYE5sBEy7rHZ8wy%2FtShg1VLGyx%2FWF54QmigLe2PbgmGSK5keUhoVeDkCRtk4ZOWCPZwaK9SGIjkrdyzc0nNJbyNtFnpjfcQBy3F76rN72%2BptZl8VsagTlWU3d5Le4ApSwY5ObPy5m8j2aDXtniHB7GbszXuYewDXLfl7IKbkCu%2BHnxYbo0grZG6hd9UBdonQ5CEtwKJQ%2BFaHAa3yj%2BOsrmXq1pMTFD%2BFO5w9F2uDYYJAC7nTXkAe2b3ZJAWRTHwKSWaUmUgXrdAemM7%2FlGHwg7WfBHharXs7AlbSYPTNAb3iauZ%2Fh5D6ShKMB06DxJnIiyMwOQ5NP0nIkVJpZLmHVdKRuMCxi42Dafj3nPp2dEMPNc2ObZN4oPdK5bamhTGVeUyj7twzyXQhySI34lCPKd7ofGoBp%2B4evs0OBuI1ijw%2BiQoNhqMMC6%2F9IGOqUBmjlJ8WkxNbFMxhbPzK%2BWVSX9%2B042%2FemeIHdngayqSxLkH%2Foc37bvu1mzgzMN5eDOP9Z4%2FtEPZfwQerIoP4YCTarK6452Qq8o6akCP2AEJY%2BTtFyvQA1Krbn8UZUpmd4uevwsOICZp5r1XVIoUk1MiGWi9XH46uQEcXkwMI%2F3yjnAszdHhPB2qjOj9SWLhT%2Begd1KrybqwVk75H%2FfmYeuZx0RQJPk&X-Amz-Signature=0a20f331f677a83a732a00d273327baccba33b82caa3690c07572d2c9346eb1f&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

hello，小伙伴们大家好，上节课我们已经对于 proxy 就是客户端的 RPC client 的代理的两个接口，同步和异步已经实现了。这节课我们要实现什么？其实小伙伴们已经知道了，我们对应着客户端，只需要实质化 RPC client 对象去调用它的同步或者异步的方法，即可发起远程的 RPC 调用。


现在我们来回顾一下我们原先跟小伙伴画的比较复杂的图。我们的客户端其实大家都知道，使用我们的 r p c client 给它实例画出来调用就可以了。服务器端怎么去启动？我们来想一想。服务器端启动说白了它需要依赖我们的 provider config 对不对？ provider config 必须要注册到我们的 server 上，我们之前有一个 register processor 这么一个方法，就是注册我们的个 provider config。 provider config 它是一个比较上级的类，它的下面的子类具体实现可以是 user service implements，也可以是 hello service implements，对吧？其实我们只需要干什么，再写一个启动类，去把我们整个的所有端程序启动起来，把对应的我们所有的 provider config 注册到 solar 上，这样就可以去实现 RPC 调用了。

[image](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/8566ac80-2c01-4f6b-ba70-c10b6a79760c/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VBC6K7JR%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T230047Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQC0OBpAv6jjwG0uwsCAbLamM7%2FpyqOyVjCwVHxUNeA7BAIgGnalS49YXCNdnsxpHdyPWjI1esZ%2FQ4VbitR84CPICV0qiAQIxv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDE9tOsQHODOAGhNduSrcAxuMCnkmbQhY8bmJYiyIP%2BbwkYjxQS9yh%2FgdgSfG2umorv%2Bi%2FyR90CqwSUbzHjPZ16WhjbbtEukCX3JlAEg0bKHE6y3xqw4mKehdNOQ9U0SLgniDzJEU0qnRZajiU6uBAJlmBdF9YPaou7WoeqaMwdIk%2BVO5wciyfXcC0YG7Nm5vtvXiclIGgH6kyjhTx0Z7SpK4BTZiCXPYE5sBEy7rHZ8wy%2FtShg1VLGyx%2FWF54QmigLe2PbgmGSK5keUhoVeDkCRtk4ZOWCPZwaK9SGIjkrdyzc0nNJbyNtFnpjfcQBy3F76rN72%2BptZl8VsagTlWU3d5Le4ApSwY5ObPy5m8j2aDXtniHB7GbszXuYewDXLfl7IKbkCu%2BHnxYbo0grZG6hd9UBdonQ5CEtwKJQ%2BFaHAa3yj%2BOsrmXq1pMTFD%2BFO5w9F2uDYYJAC7nTXkAe2b3ZJAWRTHwKSWaUmUgXrdAemM7%2FlGHwg7WfBHharXs7AlbSYPTNAb3iauZ%2Fh5D6ShKMB06DxJnIiyMwOQ5NP0nIkVJpZLmHVdKRuMCxi42Dafj3nPp2dEMPNc2ObZN4oPdK5bamhTGVeUyj7twzyXQhySI34lCPKd7ofGoBp%2B4evs0OBuI1ijw%2BiQoNhqMMC6%2F9IGOqUBmjlJ8WkxNbFMxhbPzK%2BWVSX9%2B042%2FemeIHdngayqSxLkH%2Foc37bvu1mzgzMN5eDOP9Z4%2FtEPZfwQerIoP4YCTarK6452Qq8o6akCP2AEJY%2BTtFyvQA1Krbn8UZUpmd4uevwsOICZp5r1XVIoUk1MiGWi9XH46uQEcXkwMI%2F3yjnAszdHhPB2qjOj9SWLhT%2Begd1KrybqwVk75H%2FfmYeuZx0RQJPk&X-Amz-Signature=0bf09d5a9267eafd600d2ccefa6bc9ad413badbf109f7ca1822a841bfec61207&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

接下来我们就进入我们的服务端启动类的一个编码。首先我们来看一看现在我们的整体的代码，差不多写到这儿还差。最后一个就是我们的服务端启动类，我们来新建一个服务端启动类，咱们叫做 r p c server config。我为什么要起这个名字？比如我们后面要跟 spring 整合，其实它也就相当于一个启动bin，我们利用整合的启动 bin 可以去跟 spring 进行一个比较好的整合。
在这里面我们先把一些固定的属性先定义好，比如 private 我们对应的 ip 地址大家肯定都知道， final 当前的 local host 就等于幺二七点零点零点幺当前本机OK。 point 你是可以给我传过来的，所以在这里 point 我可以是一个 protected Int point，这是端口号，后面我们自己去定义。


但是还有一点比较关键的是什么？就是 r p server 启动起来的时候，必须要知道它到底有多少个我们的 provider config，说白了就是一个的引用对象，它的 key 是什么？还记得吗？我们的 RPC server，我们找到我们的 RPC server，关键有一个方法，就是在这，有一个很关键的方法，我要去注册对不对？我要把一个的 provider config 去注册到我当前的 map 里，就是注册到我当前的r，p， c server 里边，这是比较关键的。所以我们在启动类的时候，我们需要有一个引用，在这里我 private 我们的叫做它就可以了。一个列表叫做 provider config 斯对不对？在这里我们可以写 provider config 嘶一个引用进来。好了，这个引用很简单，在我构造对象的时候是不是就可以把所有的列表传进来？我不知道这个小伙伴们能不能听懂我所有的列表？传进来之后，然后我们 this 点儿我们的 config 等于我们的 provider config。


好了，接下来我给他提供一个方法。这个方法我叫做exporter，我们叫 public void。在这里我叫exporter。为什么叫exporter？因为比如后面你要跟 ZK 集成，你做什么事情？首先我们定义它是一个服务端的启动类。我打一个注释，它叫做服务器端启动配置类。哈，我这样去说，启动配置类。首先它有一个非常关键的属性，必须要有的一个。什么你的 r p c server，你要做一个包装，你要做一个代理包装，是不是有一个 private r p c server，肯定得包装进来。默认我说给它等于一个空对不对？我在我的 export 方法的时候，我第一步我要判断一下当前 r p c server 是否为空。如果等于空干什么？不是给它 new 出来吗？因为我要启动我的 r p c server，等于 new 一个 r p server，把地址传进去，地址就是我们当前本机的host，加上冒号对吧？再加上你的 point 到底是什么？这样我们当前的程序启动了，我给他去再看是吧。


check each exception 如果出现异常了，我们写一个 s l four g。如果出现异常了，我在这里边去打一个 log 点儿error，说我们的 r p c server config exporter exception e x c p t i n 是什么？你就可以把 e 加进来。好，我就简单这样去写。这是第一步调用 export 方法的时候，第一步先去启动。


第二步干什么？我要做注册，我要把所有我的 provider config 列表私对不对？我要都注册到我的 RPC server 服务上。这个是不是非常简单？如果不等于空的情况下，我们直接做的事情就是我们去 for 循环。什么？ for 循环列表，每一个列表它都是一个 provider config。 provider 我叫 PC config。我要去干什么？我去负循环它。我要注册到 r p c server 上。我说点什么，有个叫做 register processor，是不是就要注册它就可以了？这样是不是相当于把我们每一个 provider config 注册到了我们的什么r、 p c server 上对吧？后面的步骤如果小伙伴们你感兴趣，你可以自己去实现。


如果后面比如加上 z k 的信息，我们可以把所有暴露出来的provider，它的一些配置相关的信息都注册到 z k 上对吧。所以我给它起个名字叫做exporter，其实跟 double 就比较类似了。在这里我去把它的 point 包括它的相关的一些，可以去 get set 方法，我把它拿加上。


OK，其实现在我们对应的服务器端启动类就已经 OK 了。服务器端启动类搞定了之后，后面的步骤其实就是通过我们硬编码去实现的。比如我们来把整体的 repeat RPC，我们整体的来测试一下，看看我们的代码有没有问题，现在我们的启动类搞定了之后，其实我们整体编码已经完成了。这节课我们就简单讲到这儿，感谢小伙伴们收看。

