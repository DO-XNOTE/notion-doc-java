---
title: 2-12 【源码品读】Gateway过滤器机制解析
---

# 2-12 【源码品读】Gateway过滤器机制解析

[image](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/25bddadb-e9fd-471d-826c-b3d43e8e0385/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667C3GJKYA%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T225739Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDinRG5Ph9ATRj0bgN%2FWPxYU%2FOSZKOmOh2aGPtZ3euRFgIgUrnFKNwf4DxFuGTTL4qPkx6R1BzVjokTZJd5%2FC90%2Bm4qiAQIxv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDBhiR7Yq6HE93qn%2BbCrcA5Uq3GbvrrP7Dh4RH7%2B2JCwdee1LpiDepAjS8LNZOyDMAitxs46ArGYfZt6YxJVqJMtqSRJm5CjQ0rARcvZEhUNyLzwCtdoIHPnLzFvwUgGFPvOTM0%2FkgCI%2Fycfo%2BH%2Bwy%2FFz8Ha%2FzJg5M92QZhSeCntmfAXTANrtROnayRSoLhg3AXjsItG7C0LaJhCB3kQ3%2BWb%2FprIX%2BWNGvYzfQc%2FDeOxZUuG4Zsdknw98NsWAqp5giEGbBbJsPDqY6lUhi2gMFF7c6JLt0Zf%2BFS%2BTj1%2F3zrvVdulcqzLMSGH4%2BJ2Yp%2BqERJboS%2BI5pOIpzdqnOlVe4S32iA5bhbyJzjT4e70nKmx%2BMBMQVtu%2FULLeYirdnQtQCmn6SFTKnkrZmHHrHiFdx%2FHRawIvFoXasRarNItFbj0yONnOw844kWsWpG8iPHta0E23K1c9UcXIGmLfqDdexeg4Ymol82yuyRhuf68sjy9aJTFHNynTZz57lWJdNm6dcvlc6esgdxyU%2B0VE4MKD%2B2O%2Bi5aC37MXt45%2BOIZDNbUzOU4pUgFAkDF4uLkiNKVb44FPuIKBb9Bl1oPgz4rnXRW3iHBTq80Y4l0PjNhYcNSAD1i14f88bE9XGkjndE5BOqrUpF8yv8wB5w%2BRMP65%2F9IGOqUB2BzaZ%2BsPc%2FWpqSdG7kVJoelKnC1w5ej2vgoxn8JKXN0ysV%2BqhljBj2%2FmOG8E6DF7WofrrLNSykZvOoJEfcNYpXfXXq4a6%2Frn5iDKtRMaygXmVH6WEwPc0HyLPYV4lmb8gD4pMBiJXWs1Qk5msuxMGUy2qpDy3ei2%2BIe7%2Fa7X1tZVAPivFNkw%2Fn%2FC68cIMLTCqUqLy483JkAlUQ8m03KU4R78qACm&X-Amz-Signature=2c33183679e6b9c0ea4a9775cf0071d4b73c8c0610ba8c5302f3bda6af3abf14&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

[image](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/ab80eb06-4043-4c96-9c10-1bca71b450d3/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667C3GJKYA%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T225739Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDinRG5Ph9ATRj0bgN%2FWPxYU%2FOSZKOmOh2aGPtZ3euRFgIgUrnFKNwf4DxFuGTTL4qPkx6R1BzVjokTZJd5%2FC90%2Bm4qiAQIxv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDBhiR7Yq6HE93qn%2BbCrcA5Uq3GbvrrP7Dh4RH7%2B2JCwdee1LpiDepAjS8LNZOyDMAitxs46ArGYfZt6YxJVqJMtqSRJm5CjQ0rARcvZEhUNyLzwCtdoIHPnLzFvwUgGFPvOTM0%2FkgCI%2Fycfo%2BH%2Bwy%2FFz8Ha%2FzJg5M92QZhSeCntmfAXTANrtROnayRSoLhg3AXjsItG7C0LaJhCB3kQ3%2BWb%2FprIX%2BWNGvYzfQc%2FDeOxZUuG4Zsdknw98NsWAqp5giEGbBbJsPDqY6lUhi2gMFF7c6JLt0Zf%2BFS%2BTj1%2F3zrvVdulcqzLMSGH4%2BJ2Yp%2BqERJboS%2BI5pOIpzdqnOlVe4S32iA5bhbyJzjT4e70nKmx%2BMBMQVtu%2FULLeYirdnQtQCmn6SFTKnkrZmHHrHiFdx%2FHRawIvFoXasRarNItFbj0yONnOw844kWsWpG8iPHta0E23K1c9UcXIGmLfqDdexeg4Ymol82yuyRhuf68sjy9aJTFHNynTZz57lWJdNm6dcvlc6esgdxyU%2B0VE4MKD%2B2O%2Bi5aC37MXt45%2BOIZDNbUzOU4pUgFAkDF4uLkiNKVb44FPuIKBb9Bl1oPgz4rnXRW3iHBTq80Y4l0PjNhYcNSAD1i14f88bE9XGkjndE5BOqrUpF8yv8wB5w%2BRMP65%2F9IGOqUB2BzaZ%2BsPc%2FWpqSdG7kVJoelKnC1w5ej2vgoxn8JKXN0ysV%2BqhljBj2%2FmOG8E6DF7WofrrLNSykZvOoJEfcNYpXfXXq4a6%2Frn5iDKtRMaygXmVH6WEwPc0HyLPYV4lmb8gD4pMBiJXWs1Qk5msuxMGUy2qpDy3ei2%2BIe7%2Fa7X1tZVAPivFNkw%2Fn%2FC68cIMLTCqUqLy483JkAlUQ8m03KU4R78qACm&X-Amz-Signature=82e277cfb5308a407a6ac24b45df3477fe8a1fbd06f84844902c8898cd70c2bf&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

[image](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/1e88b7ba-a4d2-4c04-841b-2c93f550eb41/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667C3GJKYA%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T225739Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDinRG5Ph9ATRj0bgN%2FWPxYU%2FOSZKOmOh2aGPtZ3euRFgIgUrnFKNwf4DxFuGTTL4qPkx6R1BzVjokTZJd5%2FC90%2Bm4qiAQIxv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDBhiR7Yq6HE93qn%2BbCrcA5Uq3GbvrrP7Dh4RH7%2B2JCwdee1LpiDepAjS8LNZOyDMAitxs46ArGYfZt6YxJVqJMtqSRJm5CjQ0rARcvZEhUNyLzwCtdoIHPnLzFvwUgGFPvOTM0%2FkgCI%2Fycfo%2BH%2Bwy%2FFz8Ha%2FzJg5M92QZhSeCntmfAXTANrtROnayRSoLhg3AXjsItG7C0LaJhCB3kQ3%2BWb%2FprIX%2BWNGvYzfQc%2FDeOxZUuG4Zsdknw98NsWAqp5giEGbBbJsPDqY6lUhi2gMFF7c6JLt0Zf%2BFS%2BTj1%2F3zrvVdulcqzLMSGH4%2BJ2Yp%2BqERJboS%2BI5pOIpzdqnOlVe4S32iA5bhbyJzjT4e70nKmx%2BMBMQVtu%2FULLeYirdnQtQCmn6SFTKnkrZmHHrHiFdx%2FHRawIvFoXasRarNItFbj0yONnOw844kWsWpG8iPHta0E23K1c9UcXIGmLfqDdexeg4Ymol82yuyRhuf68sjy9aJTFHNynTZz57lWJdNm6dcvlc6esgdxyU%2B0VE4MKD%2B2O%2Bi5aC37MXt45%2BOIZDNbUzOU4pUgFAkDF4uLkiNKVb44FPuIKBb9Bl1oPgz4rnXRW3iHBTq80Y4l0PjNhYcNSAD1i14f88bE9XGkjndE5BOqrUpF8yv8wB5w%2BRMP65%2F9IGOqUB2BzaZ%2BsPc%2FWpqSdG7kVJoelKnC1w5ej2vgoxn8JKXN0ysV%2BqhljBj2%2FmOG8E6DF7WofrrLNSykZvOoJEfcNYpXfXXq4a6%2Frn5iDKtRMaygXmVH6WEwPc0HyLPYV4lmb8gD4pMBiJXWs1Qk5msuxMGUy2qpDy3ei2%2BIe7%2Fa7X1tZVAPivFNkw%2Fn%2FC68cIMLTCqUqLy483JkAlUQ8m03KU4R78qACm&X-Amz-Signature=ffbf5021d90ceab145ddb3dfbce2f77fecd73bd666abcf2b5f06cc7ce569d3d9&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

hello 慕课网的各位同学们，大家好，这次又到了看别人的代码，大家来找茬环节了。这节当中我来带大家一起看一下 gateway 的 filter 机制解析。咱说是filter ，实际上也会牵扯到部分路由表的逻辑。第一部分是 gateway 所有故事的起点。当你接收到一个 web 请求的时候，你要把这个请求定位到某个路由表。这里的核心逻辑是如何通过我们配置的断言表达，也就是 predicate 将你的用户请求转发到一个正确的路由当中。
接下来我们来看一看和过滤器有关的逻辑，去了解一下 gateway 中如何执行一个过滤器，它的具体类是 filtering web handler 最后一个环节也和过滤器有关。咱前面不是看到过滤器有一个执行的顺序吗？那这里我们就去一起了解一下 filter 执行过程中是如何进行排序的。 OK 那么请大伙移步到 intellij 我们 debug 走起编程使我快乐。 996 是我的福报。

[image](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/55fc5035-f29c-4958-a980-66d25f41be3b/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667C3GJKYA%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T225739Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDinRG5Ph9ATRj0bgN%2FWPxYU%2FOSZKOmOh2aGPtZ3euRFgIgUrnFKNwf4DxFuGTTL4qPkx6R1BzVjokTZJd5%2FC90%2Bm4qiAQIxv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDBhiR7Yq6HE93qn%2BbCrcA5Uq3GbvrrP7Dh4RH7%2B2JCwdee1LpiDepAjS8LNZOyDMAitxs46ArGYfZt6YxJVqJMtqSRJm5CjQ0rARcvZEhUNyLzwCtdoIHPnLzFvwUgGFPvOTM0%2FkgCI%2Fycfo%2BH%2Bwy%2FFz8Ha%2FzJg5M92QZhSeCntmfAXTANrtROnayRSoLhg3AXjsItG7C0LaJhCB3kQ3%2BWb%2FprIX%2BWNGvYzfQc%2FDeOxZUuG4Zsdknw98NsWAqp5giEGbBbJsPDqY6lUhi2gMFF7c6JLt0Zf%2BFS%2BTj1%2F3zrvVdulcqzLMSGH4%2BJ2Yp%2BqERJboS%2BI5pOIpzdqnOlVe4S32iA5bhbyJzjT4e70nKmx%2BMBMQVtu%2FULLeYirdnQtQCmn6SFTKnkrZmHHrHiFdx%2FHRawIvFoXasRarNItFbj0yONnOw844kWsWpG8iPHta0E23K1c9UcXIGmLfqDdexeg4Ymol82yuyRhuf68sjy9aJTFHNynTZz57lWJdNm6dcvlc6esgdxyU%2B0VE4MKD%2B2O%2Bi5aC37MXt45%2BOIZDNbUzOU4pUgFAkDF4uLkiNKVb44FPuIKBb9Bl1oPgz4rnXRW3iHBTq80Y4l0PjNhYcNSAD1i14f88bE9XGkjndE5BOqrUpF8yv8wB5w%2BRMP65%2F9IGOqUB2BzaZ%2BsPc%2FWpqSdG7kVJoelKnC1w5ej2vgoxn8JKXN0ysV%2BqhljBj2%2FmOG8E6DF7WofrrLNSykZvOoJEfcNYpXfXXq4a6%2Frn5iDKtRMaygXmVH6WEwPc0HyLPYV4lmb8gD4pMBiJXWs1Qk5msuxMGUy2qpDy3ei2%2BIe7%2Fa7X1tZVAPivFNkw%2Fn%2FC68cIMLTCqUqLy483JkAlUQ8m03KU4R78qACm&X-Amz-Signature=fcbc0c2223acc10a5f5b2ef149fcafbb7c42d8e9d382bb1a174164371cf5e081&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

答说万事开头难，任重而道远。对于 gateway 来说，这万事开头就从这个类开始叫 rootcreditkeyhandlermapping 咱先从这个类往下一步步深入进去。咱自己当前这个 gateway 组件就配置了很多个 root 也叫路由。我们看它既有 application 中配置的路由，同时也有 Java 里面配置的路由。那当一个服务请求过来以后，是怎么挑选到正确的路由？这么多路由，谁是那个真命天子，那就看谁能一步步闯关，把他所有的 predicate 断言全部给它通过。
好，咱这里以 debug 模式启动，打开断点开始，从头到尾跟一个用户请求来看一下。这里有这么几个类需要把它打开。一个是 eureka server 则需要把它启动起来。接下来是分 client 这个项目是咱配置在路由规则中的转发路径，就是这个 URI 了，所以要把芬克兰特也给它加上那么最后就以 debug 模式打开 gateway 这个项目。


好，我们把 log 清空掉，然后回到 gateway 这里，在这个方法上打一个断点 get handler internal 这是什么意思呢？当一个 web 请求到来的时候，这个 exchange 实际上就可以把它理解成一个 web request 我们二话不说发起一个请求看一下就好了。走，你。


Ok. 那第一个 if 条件非常简单，它实际上是一个过滤条件。如果咱在项目的配置文件中配置了 management 端口，那么它就不会通过咱的路由来转发请求。我们在自己的项目中并没有配置 management port 所以这里可以直接把 App 条件略过。


OK 好，到这里，我们往 exchange 的 attribute 里面塞了一个属性，这个属性的值是 simple namesimple name 实际上就是当前这个类的类名了，我们往下走一步。你看这里有很多个函数式编程的语句，咱们在下面的这些都可以暂时不看。主要关注点在哪里呢？在这个 lookup root lookup root 实际上就是帮你去寻找路由表了，我们直接把代码跟进去。 OK 那这里就是寻找路由表的规则了。


那对于没有接触过函数式编程的同学来说，不要紧，大家可以把这个函数理解成什么呢？先获取到所有的 root 然后挨个循环，这里面的每个 root 做一件什么事，挨个查看到这一句吗？ r.get predicate 那这里就是把当前 root 的所有 predicate 给它拿出来，然后怎么样呢？把用户的请求 apply 上去。 apply 的意思就是说看看你的用户请求是不是满足我 predicate 里面的限制条件，那你如果全部满足了，就说明是这个天选之子，那最后就会返回 rootok 那咱这里打两个断点，一个是在 133 行，一个是在方法返回的尾部打两个断点，我们让断点先走进来。


OK get a predicate 方法的 apply 里，大家知道后台是怎么用的吗？我这里带大家先看一下咱的 Java 代码。比方说我们现在做的这个路由器分别有三个验证规则，一个是路径，另外一个是 method 最后一个是 header 那这三个规则它究竟是怎么实现的？我们需要点进去看一下它的代码。比方说我们点 method OK 点进去。


那大家可以看到它是一个 async predicate 但是是由谁来生成的？这个类是这个 factory 类。我们点到 factory 里面看它生成的方式是什么？基于一个匿名内部类对不对？也就是说当你执行到这个 predicate 的时候，它没有一个单独类来执行代码，而是在这个 factory 里面通过匿名内部类的形式。这个 apply 方法就是我们外面将要调用的。在这个匿名内部类的方法体中，我们完成了 htd B method 的验证。


OK 那我们再分别来看一下剩下的两个 predicate 比如 part 也是同样的玩法，也是通过一个 factory 在这里面说明了一个匿名内部类，但是 pass 的流程相对会比较复杂一些，你看它这里还会有一些正则的表达式。 OK 那我们就以这个 method 的断言为例，看一下它是怎么调用过来的。
好，我们回到 debug 的断点处。 OK 这里点进去跟一步，实际上这是多个 predicate 的共同作用的。这里有一个 and 那我们直接把断点放掉，它就会走到我们刚才打的那个 master 断言当中。 OK 走，你这个断言已经过来了。然后咱在断言当中从 exchange 里面 get 到了他当前的 HTTP method 那么也就是说当前断言的最终的返回条件是什么？是一个 true 完美通过。 OK 我们这时候把断点放掉，那它最终经过一系列的检查，所有的断言都通过了以后，最终选定了一个 root 但是由于它是使用的这种函数式编程的风格，所以在方法的跳转上可能会让人有点迷糊。


不过只要知道 flux 几个关键的节点流程，那就可以把这整个章节梳理出来。比方说 lookup root 就是一个很好的例子。那它的关键流程第一个是在这里，在这里会定用每一个 predicate 对当前的用户的 request 进行校验。如果通过以后，把这个当前的 root 返回回去。那这就是 gateway 从接收请求到选定路由的所有流程了。


同学们以为通关所有的 predicate 以后，这件事就完成了吗？没有，咱在网关层里面通关了 predicate 只是确定了有哪个路由承接你的请求。那么咱在路由表中是不是还配置了其他的属性 filter 对不对？ OK 咱接下来选定了路由以后，就看看 filter 是如何的处理流程。
我这里打开一个类，这个类的名字，大家跟我念一下叫 filtering web handledok 它就是处理 filter 的地方了。咱在哪里在最上方打一个断点就是 handle 方法这里。在这里打完断点，然后回到之前断点的地方。 OK 选定 root 这里已经选好了，我们把它放开 321 走。你。 OK 这里已经到了我们的 filtering web handler 那咱的用户请求还要再过五关斩 6 将，经过所有 filtering 处理一把。


那这里在第一行，大家看这 get 了一个 required attribute 这个 gateway root attribute 是不是看起来似曾相识啊？同学们大家知道它是在哪里安插进去的吗？我们回到前面的 predicate 断言处理的地方，在这个方法 get handled internal 里面，在你选定了路由之后，在下面的方法里，这这里有一句 96 行，这个句很关键，它往 attribute 里面放了一个 gateway root attribute 那通过这一个属性，接下来的 filter 就知道是哪个路由最终被选为了天选之子。那么接着回到主线上来，这里获得了 root 也就是路由表以后，接下来第二步就是拿到这个路由表的所有 gateway filters 咱来看看这里总共拉出了几个filter 。 OK 有 4 个。前面的两个，分别是我们在 Java 文件里面配置的一个叫 strip prefix。 Ok. 第二个过滤器是 add response header 那下面的两个 time filter 和 auth filter 这是我自定义的两个filter 。所以说你看这一步，从 root 里面把所有我们自己添加的 filter 全部拿到了。


那接下来的这一步 79 行，不光有咱的 filter 参与进来，还有 global filter 参与进来。 global filter 包含咱指定的全局 filter 也包含 gateway 给我们自己添加的 filter 因为我在这个 case 里面没有指定 global filter 所以这里看到的都是整个 global filter chain 里面自动添加进来的。那把它组合到了一块儿，global filter 添加到了 list 里。然后这个 list 中再把我们的 gateway filter 也添加了进去，各路好汉云集，那总要排个座次，对不对？谁是老大，谁是老二怎么排？这就是咱这一节的第三块内容了，看它是怎么来 sort 的。这里用到了一个类 annotation aware order comparator 我们点进去看一下。这个类非常简单，朴实无华。如果你的 list 大于一个，我直接调用 list 的 sort 方法，只不过这里要传入一个comparator。


okay 看一下这个instance ，你看它是一个 static final 的变量，相当于一个单例了，它具体来做什么？我们直接看它的方法，它的核心方法就在这里。 find order 排座次。 OK 它怎么 find order 法？你看它调用 super 的 find order 方法，我们进去看一眼它是怎么来 find order 的。如果你继承了 order 的这个接口，它就会从你这个接口中调用 get order 方法。那咱回过头来看看我们自定义的那些filter ，我们打开一个 timer filter 看它继承的接口列表。


第二个接口 ordered 就是我们想要的这个接口了，咱们给它指定了一个顺序是0。对不对？ OK 大家还记得这个顺序是怎么排的吗？是给出的这个数值越大它的顺位就越低，给出的数值越小是负数，那它的顺位就越高。 OK 那咱再回到主线上来。那这个 instance 它的 find order 方法通过父类的 find order 拿到了接口层中咱定义的这个 order 数值，这样的话直接把它返回就好了。


好，大部分的 global filter 到这里就结束了。如果你没有去继承 order 这个接口，那它剩下的流程就尽己所能的深挖你当前 filter 的整个户口本，不管怎么样，总归再给你造出一个 order 来。你看它这里分别对应了你如果是个 class 对象，如果是 master 的对象或者是个 annotate element 对象，它都有不同的方法给你编造出来一个 order 顺序，那咱就不去管它了。我们回到主线上来，咱是继承了 order 接口的。所以说这个 sort 方法以后，我们可以看到这个 list 已经被排好序了。


我们来看看咱定义的两个接口， order 顺位是 0 的，这两个接口分别被排到了第 6 位和第 7 位，都是在中间。如果你 get order 获得的值越小，那你排的就越靠前。反之越大你排的就越靠后。 OK 那我们继续往下看。这一行是打出一个 log 我们不用管它。 OK 到这里它新 new 了一个对象 default gateway filter chain 把所有已经排好序的 filter 传入进来，就是有点像疑似长蛇阵，想进去看一下这个类。就在下面我们看到这个类的 filter 方法，咱把断点放进来走。你 OK 好，到这里，大家看它是以 defer 方法来开头的。同学们有没有在哪见过这个 defer 用法啊？有的同学如果是做全栈或者是对前端稍微有点了解的，应该在前端加 script 代码里看到 defer 这个属性。


咱看 gateway 里面的源码有很浓重的函数式编程的痕迹。所以你看不光像 Netflix 公司出品的开源软件，有很多的函数式调用的痕迹。那么像由 spring cloud 直接挂牌的 gateway 里面也大规模地用到了这种函数式的编程体验。像我平时会花一些时间阅读各个开源软件源码，我就能明显感觉到这种趋势。尤其在最近几年，这种函数式编程的风格在开源软件里面日渐盛行了起来。


不过大家在企业级开发项目中，说实在的很少碰到这种模式，我建议大家一定要有所技术储备，咱说开源社区或者开源软件往往是引领技术风潮的，咱要敏锐的探秀到这种变化这种体验编程风格上的变化，做一些适当的技术储备。如果大家想在自己项目中也试验的用一下这种函数式编程，我建议大家就可以从这个 mano 也就是 reactor 这个包下面的类开始使用，尝试着体验一下这种 X Java 类似的编程体验风格。


OK 我们回退回来，接着进到他的方法里面，看他都做了什么事情，你看他这里的用法有点那么别出心裁，他不是把你所有的 filter 全部从头到尾 for 循环一遍，它是这样做的，如果你当前的 index 怎么样小于 filters decides 那么我就从你的 filter 里面把当前的这个 gateway filter 给它拿到，拿到以后怎么办呢？我先不着急处理，我怎么样再重新 new 一个新的 filter chain 把当前的这个 chain 添加进去。但是 index 加1。你看它没有把当前的 index 加1，而是把加 1 过后的 index 传给了下次需要运行的这个 chain 这个 chain 在哪里用到呢？就在 filter 里面作为一个参数又传入了进来。那它是怎么应用的呢？我们点进去 filter 接口，看它的接口定义。 OK 这里就挑选 timer filter 也是咱定义的一个 filter 进去看一下。


OK 同学们看到后面有一个券对不对我们往下看。那这里是你的主体业务逻辑，当你的业务逻辑执行完了以后，咱把这个用户请求交给谁就交给你传入进来的这个券继续处理了。所以说它就像一个击鼓传花的游戏，从最外层这里在上面把第一个 filter 称在这里给它声明好了以后，然后调用它的 filter 方法。在里面循环的时候，每经过一个 filter 它重新创建一个 filter chain 这样，你每个 filter 处理完自己的流程以后，都会把用户的请求再交传给下一个 filter chain 与此同时，你每个 filter chain 中的 index 是在这里加一这样操作的。这种方式。比起咱在这里写一个 for 循环，是不是显得特别那么小清新一点没错。 Ok. 看到这里，咱的 filter 处理流程也就完结了。


同学们以为 gateway 是一个蛮复杂的组件，实际上它的底层代码是不

是讲起来非常非常简单，有一种以为是个王者，实际上是个青铜的感觉。不过反过来说，把一件复杂的东西用简洁的代码清晰明了代码表示出来，那这也是一种本事。相比较而言，我确实感觉 spring cloud 直接挂牌的组件，它的代码复杂度会比 Netflix 组件降低好几个层次，可读性也是大大的提升。所以如果大家去学习 spring cloud 的源码，我建议可以从 spring cloud 直接挂牌的组件先看起，等你熟悉了这些步骤以后，再去尝试读更难的 Netflix 组件的代码。 OK 同学们到这里，咱的源码阅读环节就要结束了，我来带大家梳理一下。


咱的 gateway 处理一个用户请求，总共分几步，总共分两步。第一步是在 predicate handler mapping 里面，把当前的用户请求从所有的 predicate list 中鲁那么一遍，如果你通关了某个 root 的所有 predicate 那么这个 root 就是你的天选之子啦，也就是说被选定为处理你用户请求的一个路由表。
OK 那选定了路由表以后，接下来咱的用户请求还要在经过 filtering web handler 这个类，是专门从路由表中把所有的 filter 拿出来，使你的用户请求挨个过一遍 filter 这个 filter 既包含咱自定义的 gateway filter 也就是在路由级别定义的 filter 也包括了 global filter 也就是应用到所有路由表的 filter 在代码实现中，它通过每次创建一个 default filter chain 然后借助函数式编程的组件，将每个 filter 应用到用户的访问请求上，这就是整个 gateway 中最重要的两处底层代码了，非常简洁明了清晰。那么到这里本小节就完结了。在下一个小节里，我将跟大家介绍一下如何在咱的网关层中引入权限验证组件。 OK 同学们，那我们下一小节再见。




