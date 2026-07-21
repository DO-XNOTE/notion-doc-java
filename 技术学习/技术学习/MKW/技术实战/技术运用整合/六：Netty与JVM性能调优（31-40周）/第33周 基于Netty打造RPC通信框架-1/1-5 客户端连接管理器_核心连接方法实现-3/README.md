---
title: 1-5 客户端连接管理器_核心连接方法实现-3
---

# 1-5 客户端连接管理器_核心连接方法实现-3

[image](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/19552e4b-7fc0-49b2-b504-3cca1eeae819/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662R7FQJOB%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T230026Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDMMmtF2qnsboL8DzE%2Bp6K6X%2BrUJyHFFu72YNGVX7oSxAIhAJ9rgF8bOqU8KB%2FJMlmiRp8uDCp2rsYy3FDO2DN13E7WKogECMb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1Igxdd9uRCG%2B%2FLrFpJr4q3APhokzcmz%2FnSxUZBSkfhmWNLVhoKAxkEDIh8JbLi50IGHpnlO9R6OG6k1DiJNp4oKlTnp0LA4NhrcwABNmhcTtPoJB4%2BmF9GxpT2FEmgG0%2F2NSbVXAtsN%2BO8gSW4KeMg%2BfwzH2p24UHVF3RtjC6y7M%2BvhGCvKeGuUhrtaypkEgxKzoTJhab9dUjhAO%2BaK9huDTqHXSvr%2BlR6jePibsDEWrSR9TvyaG3kTBEnKLxyUnzzN3iJ3mYYFxs9zogxF0UlkWnbJYwhFz8usYHarH1i0ESPmhIZDv8U1duUSwMRhKAiumNnjJR1iQzMBAToPTMlGPs1FU8%2BDNA%2Bt%2BckhADZ%2FWsq6t8tysEE3IzAOhkHoX1X%2B%2F9pfee1W57fOeQq9vtVia2Prgly%2FklEV%2F0cQAp5ttGrJQUKSG3LBrOSaUPcsYtRu0ElxnczTGhj1BmwOjKi0YdKVISpoRxXv41V54ZcXdI%2BErnLsExzn2ZVUAMASOSoI%2Bishhv2NlirFEKsyyHQL4x%2B8PLVnxOTKbFDgC2%2FDj8nEdoK14ffzdr0qE24gaXg1UbTc0r%2F4FVU%2B8xR5ubjhQ0wKmRVAdAD%2Fp4sxc%2BqYrVpWtjbVMcy7yZtHjnUl%2FRlkdJGSrqVkTPe1tQgzCdt%2F%2FSBjqkAUFj6Bf5v6sYAQ%2FQ6t1ypHHRB5m5Qq8N0oS0kUwXM3B9xDq%2FVze%2FgFXPv1hhyOaCLOnp2eUr07WR9EQyxSrBIQdgPa7GZnDIjqws%2Bo5wyJgmIfvwBGgezWRVo%2FoKYsV67sy8H0uGJk2JDGnxInDpAxqFyk2kxMB3xUaxIaFRNAny6ydOYVa%2BAerZxTPVc%2B7Xb1uhWzQxWkbEB2ImqeJneKtcrvn2&X-Amz-Signature=bcf7dfe3e5c08d78242f173098d5f7d05584c40a2d109d5dbb629d608070c581&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

OK 小伙伴们，这节课我们继续来往下去讲 connect a single 这个方法。其实最终就是一个线程池异步的去提交，去调用 connect 方法。 connect 方法主要做什么事情？在这里我们去看一下我们具体的流程图。 connect 方法异步的去通过线程池提交。紧接着下一步他要做三件事情。首先是真正的去用 boost up 去发起连接，连接之后我应该加两个监听。同学们看到第一个监听就是连接失败的时候，我们要去做一个清理的工作，释放资源，做一个重连。连接成功的时候，我们要做一个回调监听，把我们具体的新的连接去加入我们的缓存中。

[image](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/e727f98a-15b7-4dbf-94e0-83f48e7626a7/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662R7FQJOB%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T230026Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDMMmtF2qnsboL8DzE%2Bp6K6X%2BrUJyHFFu72YNGVX7oSxAIhAJ9rgF8bOqU8KB%2FJMlmiRp8uDCp2rsYy3FDO2DN13E7WKogECMb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1Igxdd9uRCG%2B%2FLrFpJr4q3APhokzcmz%2FnSxUZBSkfhmWNLVhoKAxkEDIh8JbLi50IGHpnlO9R6OG6k1DiJNp4oKlTnp0LA4NhrcwABNmhcTtPoJB4%2BmF9GxpT2FEmgG0%2F2NSbVXAtsN%2BO8gSW4KeMg%2BfwzH2p24UHVF3RtjC6y7M%2BvhGCvKeGuUhrtaypkEgxKzoTJhab9dUjhAO%2BaK9huDTqHXSvr%2BlR6jePibsDEWrSR9TvyaG3kTBEnKLxyUnzzN3iJ3mYYFxs9zogxF0UlkWnbJYwhFz8usYHarH1i0ESPmhIZDv8U1duUSwMRhKAiumNnjJR1iQzMBAToPTMlGPs1FU8%2BDNA%2Bt%2BckhADZ%2FWsq6t8tysEE3IzAOhkHoX1X%2B%2F9pfee1W57fOeQq9vtVia2Prgly%2FklEV%2F0cQAp5ttGrJQUKSG3LBrOSaUPcsYtRu0ElxnczTGhj1BmwOjKi0YdKVISpoRxXv41V54ZcXdI%2BErnLsExzn2ZVUAMASOSoI%2Bishhv2NlirFEKsyyHQL4x%2B8PLVnxOTKbFDgC2%2FDj8nEdoK14ffzdr0qE24gaXg1UbTc0r%2F4FVU%2B8xR5ubjhQ0wKmRVAdAD%2Fp4sxc%2BqYrVpWtjbVMcy7yZtHjnUl%2FRlkdJGSrqVkTPe1tQgzCdt%2F%2FSBjqkAUFj6Bf5v6sYAQ%2FQ6t1ypHHRB5m5Qq8N0oS0kUwXM3B9xDq%2FVze%2FgFXPv1hhyOaCLOnp2eUr07WR9EQyxSrBIQdgPa7GZnDIjqws%2Bo5wyJgmIfvwBGgezWRVo%2FoKYsV67sy8H0uGJk2JDGnxInDpAxqFyk2kxMB3xUaxIaFRNAny6ydOYVa%2BAerZxTPVc%2B7Xb1uhWzQxWkbEB2ImqeJneKtcrvn2&X-Amz-Signature=b828b8840f67286d8681e204f28e08433c87d5932fc9191f2cfd9c8a9287d4ff&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

最终我要做一个叫做 signal available handle 的一个方法，这个是一个唤醒业务的执行器，这个业务的执行器指的是谁？其实我们来看一下代码。我们的业务执行器其实指的就是我们最开始创建的 concurrent 哈希 map 里边的r、 p c client handler 他。 OK 接下来我们开始进行编码。首先第一步就是真正的去调用 net 的 boost up 点connect，真正的去建立一个连接我们的 b 点connect。方法这里边直接传递一个是我们的 i net socket address 就可以了。连接之后它返回一个 channel future 对吧？我们直接 final 定义一下 channel future，我们叫做 channel future。好了， channel future 把它引进来，哈是 net 的。好了，有 channel future 之后我们怎么去做？接下来就是来添加监听。连接失败的时候，我们要加监听。连接失败的时候，添加监听，主要的目的是清除资源后进行发起重连的操作。接下来连接成功的时候做什么事情也是添加监听。主要添加监听的事情就是把我们的新连接接入缓存，放入缓存中。这就是我们相关的一个步骤。


好了，我们接下来看一看。 channel future 肯定是可以加一些异步的回调的。这么一个listener，第二channel，第二 close 标签。就是在关闭之前，我们要去加一个 add listener。这个 add listener 我们可以去 new 一个，咱们叫做 channel future listener，对吧？它这里边会实现一个什么方法？我们的一个 complete 方法，当然在这里边还缺少一个括号。好了，这是第一件事情要做的。我们这是在关闭，是不连接失败的时候，总经理资源得关闭。
好了，看一下。这里面我们先打一个日志，叫info。这个日志我们可以写一下，叫做channel。 future 点 channel 的方法叫做close。我们去先把日打做 operation complete 逗号。比如我们 remote beer，它的远程的连接地址是什么？是不是我们去加上先打印出来我们的 remote 比尔登记地址？哈，先给他一个info。


接下来我们看一下处理失败的时候我们做什么事情。处理失败的时候，我们就拿到 future 点channel。点儿，我们去获取当前 channel 所在的 event loop，其实就是 n i o event loop 它会有一个可以去调它的submit，或者是有一个什么有一个 scheduler 都可以。两个符号都可以做一个执行。这个执行我们执行什么内容？无非我们去指定定时多长时间，我们去发起重连，或者是间连接，我们可以，比如 3 秒钟一次。这后面我们就可以写 thread time unit 时间戳 time unit 点second。


好了。接下来就是 runable 接口，我们应该怎么设？你有一个 runable 好了，就这么一个事情，这个事情每隔 3 秒钟我就去重新去发起连接。但是发起连接之前我们要做一个什么？做一个把之前旧的连接清空的工作对不对？在这里我们打一个 warning 日志，表示连接没正常失败的时候，我们要做的事情咱们叫做 connect feel， to reconnect。先打个日志，接下来首先你要有一个方法， clear connected，先清空一下旧的连接，再重新发起连接。说白了，重新发起连旧还可以重新调这个方法。它是一个你可以认为像一个递归似的。在这我就不用 reconnect 法，我用 connect 就可以了。我再把原先的参数传进来，就是我们的 boost 跟我们的 remote beer。 OK 这就可以了。这个方法我们去实现一下哈。当然这个方法我不要写到里边哈，我再重新写到外边，因为我后面可能其他的也会共用。


我们怎么去做？这就是清空。打个注释说连接失败时，及时的释放资源，清空缓存是这么一个简单的事情，怎么去做？首先，假设连接成功了之后，肯定我们会把连接放到一个，比如放到 map 里，或者是放到一个 list 里边，这些都可以。在这里我们先创建一个 connected handler list。在这里小伙伴们，如果你不懂没关系，我们先把资源先定义一下，后面我们去一点点解释。我们之前有了一个 concurrent map，它主要存的是一个连接的，具体的 i net socket address 为 key 的一个地址values，对应的是一个 r p c connect handler，具体的执行器可判断的。


接下来我还想去定义一个变量叫做什么，叫做private，它可能就是一个list。好，我们就写一个list，当然这个 list 你写一个线程安全更好一些。大家还记得这个吗？ copy on right array list 它具体的值是什么？其实这个 list 它具体的值我们都可以直接写死，就叫做 r p c connect handler，我们给它起个名字，叫做 connected handler。 list 连接成功的时候，我们一定要把所有连接成功的，具体使用的 RPC client handler 去给它缓存到 list 中。为什么会有两个存储？后面我们再去详细去说。我们先把代码编写成功，先把它写上好。


小伙伴们，假设我们所有连接成功的，在这里哈。我打个注释地址所对应的任务执行器列表。 OK 就是它了。假设我们所有连接成功的，它的任务生成器都会有一个列表哈，当然它不是 copy right list 哈，是这玩意是因为它的泛型是 RPC connect handler 哈。假设所有连接成功的地址，它都应该存到 list 列表里，当然也会存到 map 里。现在有两个这样的缓存集合。我们来看看这个东西后面我们去清空的时候应该怎么去做。清空的时候我们找回到后面的代码clear。这个方法我肯定去 for 循环去做真正的具体的删除的操作。这个应该怎么去做？我们就后循环一下哈。负循环谁就是刚才我们所创建的叫做 connect handler list，它每一个变量都是我们刚才所看到的。


RPC connect handler 这个东西我们叫 RPC connect handler。我去 phone 循环它失败的时候，首先失败的时候你这个 handler 具体是哪个 handler 你现在不知道，因为这个 handler 它跟谁对应，它跟具体上面的我们看到了这个 map 是相对应的。
这个 map 里边有一个 i net socket address，它跟我们的 r p c connect handler 是一一对应的。我们连接失败的时候，我现在想去干什么？我现在想去通过 handler 我找到具体的。在这里通过 r p c connect handler 找到具体的 i net socket address 地址。我们要找到具体他 i net socket address 就是他哈 remote beer 做的事情。


如果我们找到了之后，接下来我就直接进行删除就好了。删除谁？从我们的 concurrent 哈希 map 中去把对应的内容移除，因为我们坎康的哈希 map 是 key 对不对？我找到具体哪个地址之后我把删除就好了。所以我们应该找到它从 map 中哈进行移除指定的他。


如果我们这里面我们能够保存一下，比如我们用做一个引用能够存储，我们就可以去删除了。当然它这里边是真正的去进行 n i o 通信的，所以你应该把它进行。比如做一个锐目操作，你的意思列表里边是不是应该也应该做一个 clear 操作，因为你是连接失败的时候，应该所有的内容应该都去给它干掉了。因为我们看到了 beer 相关的，我们都应该做一个clear。所以在这里我们来看一看这应该怎么去写。


我们先回到我们具体的在创建 RPC client handle 的时候在哪创建的。我们比如我们给它加一个引用就可以了哈。我们来想一想这个东西怎么去价格引用。 RPC client handler 到底是一个什么东西？我们点进去哈。 RPC client handler 无非就是我们 net 的这么一个实际业务处理器。我们这节课先把它去先简单写一写，让大家看到。比如我们正常来讲， RPC handler 都应该继承一个什么叫做 channel inbound handler adapter，或者更简单的，大家可以去继承 simple channel amount handler 更好一些。为什么？因为他会直接帮我们去释放资源。这里边的范型我们可能暂时不知道，我在这里先给他一个object，因为后面我们要去对它做一个实际的定义。


OK 好了，这应该重写一个方法，就是我们的实际的 channel 瑞德 0 的方法。当然除了 READ 0 的方法，你可以有一些其他的对应的方法。比如现在我想要 RPC client handler，里边包含我们具体的一个 remote address，它的地址怎么去做？其实这个也很简单，我们再重写它一个方法就好了。


我们记不记得有一个方法？这个方法应该大家都应该比较熟悉，我们 channel 在激活的时候，我们可以有一个叫做 channel active 这么一个方法，它里边传一个context，叫做 channel handler context c t x 这个方法。然后应该是往出抛异常的保存，你看这里边有一个绿色的表示 Oray 的复写的。这个就是我们当通道激活的时候触发此方法好了，在通道激活的时候，我们可以去调用一下父类，我们要重写它。我们先应该把布雷的该怎么去做，你就怎么去做，你不能去变哈，还是c，t，x。


在这里边我们可以去做一个远程的地址的缓存，也就是我当前的连接，它到底连接的是哪个远程地址，这是不是可以？比如我们能拿到channel，我们在这里边我们可以去定义一个，比如我说有一个 private channel，当然这个 channel 肯定是我们的 NIO 的channel。好，这个 channel 我们什么时间把它初始化？在我们注册的时候，我们可以把 channel 去做一个初始化。当然 net 也给我们提供了一个注册的方法。这个注册方法也很简单，我们再把它注册方法重写一下，这个是叫做 channel active，还有一个叫做 channel rejected，应该这样去写好。


看到 channel rejected，它应该调父类的 channel rejected。当然先应该是注册，再是激活。所以注册的时候我就应该通过c、t、 x 找到对应的我是注册的哪个channel，我c、t、 x 点 channel 就取到了 channel 了，是不是我这上面所定义的是不是我就是this，点 channel 等于 channel 就可以了，这个 channel 是不是就有值了？有职了之后，我们可以通过 channel 在激活的时候，激活什么意思？就证明他真正的有连接了吗？真正的去发起连接了。我就直接可以说 this 点channel。


第二， remote address。这是 net 的API，哈，我们看一下我 channel 所对应的远程的地址是谁，我就知道了。这个远程的地址我们可以是保存一下吗？其实就是一个 socket address，我们看一下它返回的就是一个 Nike 的 socket 的战士，所以我们直接就有了它了。我们再做一个他 socket address，我们叫 socket address 小写。有了它之后，我们来看一看。其实我可以再写一个详细一点，它就叫 remote beer 就好了。这就是我们的远程连接地址，你直接可以赋一个值， dis 点 remote beer，等于 channel 所对应的 remote address。


好了，同学们，看我写完了之后这什么意思？实际的业务的处理器就是handler，它在通道。在注册的时候，我们能拿到它的channel，给它用一个成员变量保存一下。在激活的时候，因为有通道的时候，激活的时候我就知道远程我要连的是哪个地址了。我就可以再缓存一下，这样我们实际的业务处理器哈，挡住我们的实际的业务处理器。有了业务的处理器之后，它已经帮我去缓存了。 socket address 就是它的远程地址。这个远程地址跟谁是一样？同学们，回到 manager 是不是从 handler 里面我们就能取出来具体的它的远程中心地址？

