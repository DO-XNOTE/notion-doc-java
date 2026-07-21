---
title: 3-6 源码分析 - RoundRobin和Weight策略
---

# 3-6 源码分析 - RoundRobin和Weight策略

[image](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/6f470b68-270e-46c6-a445-f47e8701b2d5/SCR-20240801-umos.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RYPKMGZV%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T231320Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCInoe%2BPS%2By9eV5tW%2FN5%2B7q2NE8BP0U%2BEUKnRD8rYQDxAIhALQEOTZnUPNj3Gcu9Ny4uNMRhBZe5qnLqExWLd9Nzg3HKogECMb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgwS45XsfTn76p%2F7vScq3AMVFenxNJNWQ2bWsIU4cDbIQxnDETCn%2Fz%2BOzHfJ8AcRbzTufCznXq%2BCKlDL%2FsYw1LlkufHM6zuzKtoQuuB0OqsqL0Mc6urxvusM7bWNk6Sq9svt8BoEWY%2B86VQ1HyvxymY87Ep1ihqwV4JmslOWqErl%2FwIh8BxARNIaSk5G2R%2BZ2HhDr5iWBr4XyIpSBTUWhBhI5e1hQEyB0UPrdG7UcKpxrGe9RSTqw3UdcBNRCcsunMIHo9InSwNrUiGdU5DH2ZOMSZpMzgd1mQXoxAMg60wKTfddxbHEdm3X6o1t9Wm5DT0PdjEMEFG0A0xpC2kLhoOd1nqUcVa1QAH7lKQTr31HSzrkq50KiAyvmedHV%2BY0ze4kfiJnF3wPaz%2FgQ8lYtrRkhJ1quoNg%2FjM5WtEJNoiSfw%2FnnVNg3ahApVV7XLKEdtXE8HvR098vs%2B3O05vQQHsAiduZp6czWWCfjXPaMlawBasPOMMPepH82hUyV0nrTFePyHDm%2BWABRKRXJI4x9z471SXBFgFSKd3AqtLgI3kszGQ1hp5XQwwdshYEH7H7EYgEZPQAD5vvDApN2lFiVwN%2FgB4FicidvWNtn1h1M2twol8Ztl9%2FPiviur%2BywAa4uS4nuTyqv9LiRoI%2BPDCUt%2F%2FSBjqkAd3c6j0ktuJ3zChVcbQ9%2FeNCVZH5q3cYwLxWtL3Rin0nT%2FqBxB7p5csEnqmIRXRS6tnUg2QWmj%2FO%2BEp%2BHJpvVbhYhjN%2BaUjRZqvaxvAVtIE4Zmn5mNjPNRixoJat3pwT25ZqZqaxvXSVA0RmYdX%2F6P9q5bMO0LM%2FqRmnDrXVw5R7KV54SHir46bl3J7GExtfk4Cirth51cLYimfI7EMtAOCDT%2B1Q&X-Amz-Signature=ef634843ac5ad2af2bb7c9424e87cfbc640e013fe4ff2d72434b362da277a225&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

[image](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/4e20fc26-593e-4f90-aa30-ff87c42ce174/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RYPKMGZV%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T231320Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCInoe%2BPS%2By9eV5tW%2FN5%2B7q2NE8BP0U%2BEUKnRD8rYQDxAIhALQEOTZnUPNj3Gcu9Ny4uNMRhBZe5qnLqExWLd9Nzg3HKogECMb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgwS45XsfTn76p%2F7vScq3AMVFenxNJNWQ2bWsIU4cDbIQxnDETCn%2Fz%2BOzHfJ8AcRbzTufCznXq%2BCKlDL%2FsYw1LlkufHM6zuzKtoQuuB0OqsqL0Mc6urxvusM7bWNk6Sq9svt8BoEWY%2B86VQ1HyvxymY87Ep1ihqwV4JmslOWqErl%2FwIh8BxARNIaSk5G2R%2BZ2HhDr5iWBr4XyIpSBTUWhBhI5e1hQEyB0UPrdG7UcKpxrGe9RSTqw3UdcBNRCcsunMIHo9InSwNrUiGdU5DH2ZOMSZpMzgd1mQXoxAMg60wKTfddxbHEdm3X6o1t9Wm5DT0PdjEMEFG0A0xpC2kLhoOd1nqUcVa1QAH7lKQTr31HSzrkq50KiAyvmedHV%2BY0ze4kfiJnF3wPaz%2FgQ8lYtrRkhJ1quoNg%2FjM5WtEJNoiSfw%2FnnVNg3ahApVV7XLKEdtXE8HvR098vs%2B3O05vQQHsAiduZp6czWWCfjXPaMlawBasPOMMPepH82hUyV0nrTFePyHDm%2BWABRKRXJI4x9z471SXBFgFSKd3AqtLgI3kszGQ1hp5XQwwdshYEH7H7EYgEZPQAD5vvDApN2lFiVwN%2FgB4FicidvWNtn1h1M2twol8Ztl9%2FPiviur%2BywAa4uS4nuTyqv9LiRoI%2BPDCUt%2F%2FSBjqkAd3c6j0ktuJ3zChVcbQ9%2FeNCVZH5q3cYwLxWtL3Rin0nT%2FqBxB7p5csEnqmIRXRS6tnUg2QWmj%2FO%2BEp%2BHJpvVbhYhjN%2BaUjRZqvaxvAVtIE4Zmn5mNjPNRixoJat3pwT25ZqZqaxvXSVA0RmYdX%2F6P9q5bMO0LM%2FqRmnDrXVw5R7KV54SHir46bl3J7GExtfk4Cirth51cLYimfI7EMtAOCDT%2B1Q&X-Amz-Signature=da161833c867ec583257fdb2f23ba4ec1c6ef75600f3dc72c95a24290f9f1576&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

hello，幕后的各位同学们，大家好，我是要半仙，咱这一节带同学们一起来一睹 ribbon 当中两个拳头组件， round Robin 负载均衡规则，还有另一个基于响应时间权重来做负载均衡的规则。咱这一节里就去深入到源代码，带同学们来了解一下这两个规则它的底层实现是什么样的。

[image](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/60c72b52-1a9f-4b05-89a2-cf38993ac56b/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RYPKMGZV%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T231320Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCInoe%2BPS%2By9eV5tW%2FN5%2B7q2NE8BP0U%2BEUKnRD8rYQDxAIhALQEOTZnUPNj3Gcu9Ny4uNMRhBZe5qnLqExWLd9Nzg3HKogECMb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgwS45XsfTn76p%2F7vScq3AMVFenxNJNWQ2bWsIU4cDbIQxnDETCn%2Fz%2BOzHfJ8AcRbzTufCznXq%2BCKlDL%2FsYw1LlkufHM6zuzKtoQuuB0OqsqL0Mc6urxvusM7bWNk6Sq9svt8BoEWY%2B86VQ1HyvxymY87Ep1ihqwV4JmslOWqErl%2FwIh8BxARNIaSk5G2R%2BZ2HhDr5iWBr4XyIpSBTUWhBhI5e1hQEyB0UPrdG7UcKpxrGe9RSTqw3UdcBNRCcsunMIHo9InSwNrUiGdU5DH2ZOMSZpMzgd1mQXoxAMg60wKTfddxbHEdm3X6o1t9Wm5DT0PdjEMEFG0A0xpC2kLhoOd1nqUcVa1QAH7lKQTr31HSzrkq50KiAyvmedHV%2BY0ze4kfiJnF3wPaz%2FgQ8lYtrRkhJ1quoNg%2FjM5WtEJNoiSfw%2FnnVNg3ahApVV7XLKEdtXE8HvR098vs%2B3O05vQQHsAiduZp6czWWCfjXPaMlawBasPOMMPepH82hUyV0nrTFePyHDm%2BWABRKRXJI4x9z471SXBFgFSKd3AqtLgI3kszGQ1hp5XQwwdshYEH7H7EYgEZPQAD5vvDApN2lFiVwN%2FgB4FicidvWNtn1h1M2twol8Ztl9%2FPiviur%2BywAa4uS4nuTyqv9LiRoI%2BPDCUt%2F%2FSBjqkAd3c6j0ktuJ3zChVcbQ9%2FeNCVZH5q3cYwLxWtL3Rin0nT%2FqBxB7p5csEnqmIRXRS6tnUg2QWmj%2FO%2BEp%2BHJpvVbhYhjN%2BaUjRZqvaxvAVtIE4Zmn5mNjPNRixoJat3pwT25ZqZqaxvXSVA0RmYdX%2F6P9q5bMO0LM%2FqRmnDrXVw5R7KV54SHir46bl3J7GExtfk4Cirth51cLYimfI7EMtAOCDT%2B1Q&X-Amz-Signature=9d0691ff263571a4d696ce342954325ad679e04497ed3263cefc51c7c0e9abd3&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

好，那咱接下来切换到 Intelligent 里面，我们走起第一个规则， round Robin room 这个规则，我们直接去搜索这个名字， round Robin row，搜索到第一个结果打开，因为这个类是在 ribbon 的价包里。同学们如果打开之后发现是一个 doc class 文件，咱这边会跳出一个 download sources 选项，我们点一下使用 Maven 把它的源码给它拉到本地就可以了。


好，那我们看这个类它核心的一个方法是谁？这一猜就猜出来了，这个方法 choose 方法。为什么呀？我们顺着它的依赖项直接找到顶 i rule 这个规则，它其中最核心的就是它选择你要访问哪个服务器。那咱接下来看一下 round Robin 轮询这样一个简单的算法，它在底层实现有什么别样的技巧？OK，那这个算法通篇读下来还是非常简单清晰的，核心部分不多，大概100。行，咱看一开始你的 load balancer，这个如果没有传入，那直接 IM sorry，拜拜。再见您嘞，这是一通正常操作。我们接下来往下看。


这个 Server 就是我最终要选中的，翻到牌子的那台服务器，我就要访问它。好，那我们看这个 while 循环，这里其实是一个类似自旋的一个功能，只不过我们在这之上做了一个限定，一旦我选中了将要访问的服务，或者我当前已经尝试了 10 次，那么这两种情况下，不好意思，我就不想让你继续来浪费时间了，我就直接把这个循环中断。那咱接下来看这个循环的过程。


第一个它获取了两个list，第一个 list 是 reachable servers，那是可达的服务器。第二个是 all servers，那就是所有服务器都在里面。这两者有什么不同？从它的命名上我们就可以看出来， reachable Server 是可达，也就是说你当前服务器是一个可被响应的服务器，那下面的 all servers 是注册表当中的一个全集，有一定的可能性，或许会包含那么几个老弱病残，就是叫不醒的人。所以我们在这里计数的时候，把它作为一个服务器的总数，上面叫 up count，也就是当前状态是 up 的机器。


好，那么接下来往下看，如果你当前没有可用机器，或者说你的机器列表一个都没有光杆司令，那这时候一样的操作， im sorry，直接出门右转左拐不送，直接 return 一个空。那接下来同学们来看，这里就是它其中比较精妙的一个操作了，你看去计算下一个访问的index，那怎么来计算？其实这里我们点进去看，它有这样的一个操作，自旋，再加上什么，再加上 case 操作，那这就是一个非常经典的组合，那他要完成一件什么事儿？实际上他只要做这样一件事儿，就是轮询的访问下一个节点。
那你如果当前访问到第一台机器，我下一台访问第二台机器就可以了，简单的一个加一操作。但是我们这里可不能简单的把它做成一个加一，为什么呀？因为你可能有四面八方的服务请求，一起来去做 round Robin 的计算。那我既然是一个轮询，我就要确保每一个请求它要抵达依次向后的服务节点。如果我这个方法只是单纯的加一，那么就有可能在请求高峰到来的时候，那你这边你就不能做到一个同步。


那我们这边为什么使用CAS？实际上就是为了应对这种线程操作，熟悉 CAS 的同学应该知道， CAS 是一个多线程同步下面的一个非常轻量级的解决方案。那不用上 synchronize 这种重量级的锁，我们来看一下它具体是怎么样来做的。首先第一步，我从这个 counter 这里拿到一个 current 的下标，那这个下标，比方说我当前下标是一，OK，那我接下来要访问的第二个下标是谁呢？就是当前下标加一，并且取于你的这个传入的参数。传入的参数又是谁？我们来看是你服务器的当中包含的节点的总数。那比如说你现在有三台机器，上一次访问到了第一台，那这一次第一台加 1 等于2， 2 再取于3，那这个下标就是 2 了。很简单，那么如果你当前的这个机器数量小于下标怎么办？有没有可能发生？同学们想什么时候可能发生啊？服务下线的时候对不对？那这种情况下，因为我这里选的是一个取余，所以我能保证我的这个 next 不会数组越界。


okay，那我们接下来往下来看，我这里需要做的一个操作，就是我要把当前的这个 next 的下标，把它重新塞到这个 counter 里面。那我们这里用了一个 compare and set，就是我们熟悉的一个 case 操作，它是类似一种乐观锁的机制。如果你当前这个 counter 里面的数值是current，那么这时候我就可以利用一个原子操作把它设成next。那如果不是 current 怎么办？很简单，看到这里有个 for 循环自选，那么自旋走到下一次循环里，我再次的把最新的 current 拿出来，再加一区域，获取到一个新的next，然后再尝试走 case 操作。


我们如果点进去这个 case 操作，我们会发现它这里应用了谁？应用了 unsafe 类，那 Java 经典的 concurrent Atomic 包下的 unsafe 类。再点入一层，我们就会发现这个 unsafe 类的底层方法其实不是在 Java 层实现的。


看到这个 native 吗？ native case 操作，它是由操作系统层面实现的。我们可以认为在操作系统层面，你的 compare and swap 这两步操作，在我们的操作系统当中，实际上是可以把它当做一个原子操作的。OK，那我们接着返回，获取到了一个新的下标之后，这里从所有服务器当中把当前节点给它拿到。那如果这个节点为空，这时候怎么办？其实这个情况极难发射，几乎可以认为它不会发射。但是一旦发生之后，我这里要做一个线程让步，这是一个很轻的调优方案。那线程让步出去之后，我进入到continue，走到下一个 while 循环，等待线程被再次启用调用。


好，那我们接着往下看。当你的选中的这台服务器 its alive，或者它是 ready to serve，是就绪状态的情况下，那么这时候我会把它当作一个合格的负载均衡器，把它最终直接返回出去。否则我会把你当前的 Server 给它置空，然后进入到下一次循环当中。如果你的总循环次数大于 10 次，我这边额外打出一个 learning 级别的日志文件告诉你。


okay，这个就是 round Robin，它的底层的实现非常简单的需求。但是它这边用了两个技术点，一个就是我们前面说的这个 for 循环自旋锁，加上 case 操作一个经典组合。第二个它做了一个小的调优，这里线程让步 THREAD yelled。好，那我们看完了 round Robin。接下来我们来看咱前面说的第二个类，叫 wet it response time rule。好，我们把它打开走，你okay，这一个负载均衡的规则非常的长，我们这里挑重点，啥也别说，直奔主题。同样的，我们把它定位到这个 choose 方法，OK，这个 choose 方法里面比也有洞天，它是如何根据你接口的响应时间来做一个权重的？我们接下来往下来看，那同样前面还是正常操作，如果 load balancer 是空，那出门右拐直接return，再往下一个哇偶循环，我誓不罢休，必须找到一个Server，如果没找到我就一直的找好。这里的一个变量非常关键。


current wait 什么意思？当前的权重，这个权重跟服务的下标是一一对应的，你下标为 0 的服务器，它对应的权重就是你这个 list 里面第0个下标对应的这个 double 值。接下来往下看，这个在什么地方用到？好，如果你这边线程被中断了，不好意思，我直接中断当前循环 return 回去，那么往再往下，获取到你所有的服务器的列表，以及你服务器的个数。然后一个 if 判断，如果你当前没有可用服务器，同样的也直接返回。再往下，这里就到了我们做权重计算的这一步了。


我们来看这个参数叫 Max turtle weight，那它什么意思？这一个 current with 下标当中，它有一个约定，你最后的一个下标，你这个数组当中的尾节点，它其实是你所有的权重加起来的总和，它有这样的一个约定，所以你看如果我想获取到最大的总权重，那么怎么办？我这边加一个判断，如果你的 list 当中什么值都没有，那就是0，否则我去获取到你最后一个节点，这就获取到了你所有权重总和的数值，那如果你这个数值太小了，根本不够看 0. 001 或者我当前哎出了一些岔子，我的服务器的个数和你这个 current weight 当前权重列表的个数不一致，这种情况怎么办？很简单，我就不做权重的负载均衡，我直接调用 super 方法，调用它负类的方法，帮我找到一台机器，直接 return 了。那它负类的方法，这个 choose 是哪一个？负载均衡策略，同学们还有印象前面课程讲过的，大声喊出他的名字是 round Robin roll，对吧？看到这里，他才是站在背后的老大哥。


好，我们回退回去。那这是其中的一个 if 条件，当你的服务器个数和权重个数不一致，或者你的最大权重过小的时候，执行 round Robin。那接下来当另一种情况下，我怎么来根据我的权重来去分配你的机器呢？那就是这一行具体的算法我们来研读一下，你看，首先我这里使用 random 点 next double，这里会产生一个什么呀？一个 0- 1 的数字，用这个 0- 1 之间的数字乘以我最大的这个权重总权重，我就得到了一个随机权重。


接下来有意思的事情在这，我这个算法其实非常的投机取巧，非常的简单，我只要把你的这个 current weights 这个列表做一个 for 循环当前的机器，如果我的权重大于我这个随机权重，那我就把它给筛选出来，最终把它返回。就是这么简单的一件事。这个算法我怎么保证我响应时间越短，就越有可能被选中？这个问题我分两步来回答，第一步，你的响应时间越短，它在你这个权重列表当中的数字也会越大，也就是说你越有可能被最终选中。


这解答了第一个问题，第二个问题，我的响应时间是如何与这个 current weights 这个权重之间去做一个关联的？这里就要提到我的一个定时任务了，那接下来我们就带大家来看一下当前的这个负载均衡规则是如何将响应时间把它换算成权重的。好，我们往上走，走到最上面看这一个方法。 init 方法 okay initialize，那这个方法会在你负载均衡策略开始加载的时候，设置 load balancer 的时候就会被调用。那它这里面主要是做一件事儿，就是启动一个timer，你可以把它理解成一个后台去运行的这样的一个job，那这个 job 它具体的代码在哪里？它是在这个地方看到这个schedule，去 schedule 这样的一个task，那我们点进去看它的这个内容是什么？走，okay，那到了这里同学们可以看到它其实继承的是个 TIMER task， TIMER 是 Java utility 当中的一个标准的计时器任务，那它这边主要是做了这样一件事情，每次被运行的时候，执行 run 方法的时候，它都会去做一个统计。


好，我们来点进这个统计方法看一下，它是一个内部类，那这个内部类当中的这个方法它主要做的一个事情就是统计你接口的访问时间，把它做一个权重的汇总，那咱过来看一下它这里面主要的流程。第一个我在去执行这个方法的时候，我要给它打上一个标记叫 in progress，也就是说我当前方法正在执行，当前后台运算的这个 job 已经被驱动了，那它是采用一个 case compare and swap 这样的操作来去执行的。那如果前一个处理还没有结束，那么这个 case 操作会返回一个false，也就是最终会做一个退出。


如果当前这个任务没有被触发，那么这个 case 操作去获得这个任务的执行权之后，接下来去执行它的主要逻辑，那这个逻辑在这里我们把它往下走，走到这个关键部分。那同学们看这里这个逻辑当中核心的部分就这么一点，这一个屏幕就装下了它的核心部分。首先我 for 循环，把这些服务器给它挨个拉出来排排站，排排站之后我这里去自动的获取你当前的状态，你当前状态信息这么多，砸其他的不要直捣黄龙，我就要获得这个数值。 response time average 平均响应时间，我把它加到你响应时间的总和里面去，待会儿这个数字会能派上大用场。


好，我们接下来往下看，那这个 double 同学们看到这里它就是你当前的权重，你看它后面的这个命名叫 so far， so far 就是截止到现在为止你的权重，那我们看它是如何来计算的。首先我声明了一个 final weight，那就是你权重最终计算结果，接下来咱再把前面拉出来遛过的这个服务器列表，再把它给拉出来遛一遍，然后依然的获取到你的 service states。这个 service states 我怎么来去计算权重呢？同学们，看我的 turtle response time，也就是当前所有服务器平均响应时间的总和，减去你当前这一台服务器的平均处理时间，那么你就得到了你的权重，同学们看是不是很精妙？你当前响应时间越短，那么自然而然你这个相减出来的数字也就越大，那你当前响应越大，那这个权重也就越小。原来这一个权重加权就是这么简单的计算方式。


OK，那计算好之后，我要把它加到这个权重总和里面去，那把你这个权重的总和加到它最终的服务列表里，所以同学们这里有没有明白咱前面说的，你的权重列表当中最后一个数字是它所有的服务权重的一个总和，那就是这样来的，然后再把这个最终计算出的结果给它写入到权重里面，同时在 final 里面将这个任务制成结束。
OK，那这里我相信同学们一定有一个疑惑，就是说我的权重，咱一开始以为你在这个列表下标当中的每个权重是这台服务器的权重，而从这段代码当中我可以看出来，它其实并不是指你当前服务器自己的权重，而是它把你当前服务器权重和之前服务器的所有权重全部都加了起来，作为当前下标的权重。那这样算为什么也可以满足需求？这里同学们不妨把这个鼠标移到最上面看。


官方给出了一段解释的例子，OK，那我们看到这里，假设我们有四个endpoints，那这四个 endpoints 它对应的权重分别是131040，还有20。OK，那么接下来经过我们这个算法计算出来的权重是这样的，第一个节点权重依然是10，没错，第二个 b 节点，它的权重就是10，再加上 30 成为了一个40。再往后 c 节点是80， d 节点是100。


好，那这个算法之所以能满足你的响应时间需求，其实它是主要运用了概率论的这样一个思想，如果我在 0- 100 之内做一个随机数，同学们看，如果这个随机数小于10，那么你第一个节点相当于有 10% 的几率来让你的随机数落到 1- 10 这个范围当中。第二个节点，由于它的响应时间短，因此它自身的权重比较高，那它自身权重有30，也就是说它有 30% 的几率让这个数字落到 11- 40 这之间的 30 个点，以此类推。第三个节点，你只要数字落到 41- 80 之间，那就可能被它选中这个范围整整 40 个点，也就是说它有 40% 的几率。因此这个算法的精妙之处就在于此，运用了概率论的思想，你每段范围它的宽度决定了你有多少概率来落到这个范围之内。


OK，同学们，这一节的分享就跟大家分享到这了，想不到小小的一个负载均衡啊，这么简单一个组件，那背后还真的有不少道可以让我们来学习的这一节就跟大家先聊到这里，下一节再跟同学们去聊一聊 i PIN 和 i road 保护机制。好，同学们，我们下一小节再见。

