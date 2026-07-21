---
title: 1-10 【源码品读】负载均衡策略解析-2
---

# 1-10 【源码品读】负载均衡策略解析-2

[image](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/3a47d05a-dd53-47e5-bf68-8e8162461293/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466Y5HIH6E6%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T225610Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIFvkN67y6mgifoNP3ECLkVUKfr2%2FuK4rFJ7Zrhf0D9raAiEA9Cx5dWxGn5APkDZ8y9rXIalnLb9ps9YQ6VccliKR4AYqiAQIxv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDI7Yfhh6A77fAGNALSrcA2f97Vv6qdwZtmcyw8e9fXpj8JVFP3TJrbQMDeiJiiVmgDXzYJ7x7f5I49faGZyoUhC80pBRA%2F9sOt9AP%2Fe3bW0bQl8%2Fq5%2FJMZbdSigKY%2Fw8C4%2FnoV901KWgbjlHDqRyOyxPShs0MEohjsO2qRJ%2FX2YNJlX9ZMEmXpg2eGvHC1Z9YoQDHRodNG2rSTDyHWnlDNAdofM6DS4%2F%2BneJ7F6eTMeFBl%2BNnMMwG63pTwgh6vtW7WdKTI8SEwhmMqd3QtJu5teh%2F%2BRkAMIbIvKzk6YlkqpKKELAKmdBesyORgkV48KxSIu35pFCo5XjAwGk%2FkUJD7VK4iAyUpVmLve03uHnmZTti5JdFyA8V70CaELtd4vSj8Qjq2wpIQ32J%2BIOvUsW%2FiYodcnly0XvFoLUcVn%2FbEXYwXUcLyiqdjk0TcYumzyysNaBNb%2B8hC2ybZhSiXb%2BRhC8r7ExDaJu3oRPU6FY%2BkIzJn0LvgeLUyrxu496Pvbru1mIx08RPPxAM%2BOodNmAYC0ZHt4TdjfLgjWmwJD4tOYBPHsyIe5DmAzFif8UbD6cROAirIslLrla63c8KspbsZw8D9r1MHhOczlAUgtbiawyXBvrS4xYK0ORdy4lAyY%2F8jXF40yu4Qxzbak2MNu3%2F9IGOqUBxoKZpZpdlG59Oq13DvbodpMXYksWzxi1XfBOzVgXXbGF0QyCk2rHyHtw%2BUc08pW94CYMKfOu%2B5S8yL2kUjbvu45JlPLgLkd6UlrKpbEy8qJq38MtQ%2FJLgKYgP2kq9DDOV33l4eo6a9tnU79h344OhZnJt9Nq%2F74zHXT2URRB9o9DSXiItCdfW7k3U7QUxgrphJpWrbB%2BZBIRuVy%2BrgXC%2FbFYZhL%2B&X-Amz-Signature=7f92c7a3b1426a47d573c84ac54083d3093fa65f77cbdd1696d24bb6e0a0f323&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

[image](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/eb0ae8c4-2d1e-4b16-a59d-b2352ab4fd70/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466Y5HIH6E6%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T225610Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIFvkN67y6mgifoNP3ECLkVUKfr2%2FuK4rFJ7Zrhf0D9raAiEA9Cx5dWxGn5APkDZ8y9rXIalnLb9ps9YQ6VccliKR4AYqiAQIxv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDI7Yfhh6A77fAGNALSrcA2f97Vv6qdwZtmcyw8e9fXpj8JVFP3TJrbQMDeiJiiVmgDXzYJ7x7f5I49faGZyoUhC80pBRA%2F9sOt9AP%2Fe3bW0bQl8%2Fq5%2FJMZbdSigKY%2Fw8C4%2FnoV901KWgbjlHDqRyOyxPShs0MEohjsO2qRJ%2FX2YNJlX9ZMEmXpg2eGvHC1Z9YoQDHRodNG2rSTDyHWnlDNAdofM6DS4%2F%2BneJ7F6eTMeFBl%2BNnMMwG63pTwgh6vtW7WdKTI8SEwhmMqd3QtJu5teh%2F%2BRkAMIbIvKzk6YlkqpKKELAKmdBesyORgkV48KxSIu35pFCo5XjAwGk%2FkUJD7VK4iAyUpVmLve03uHnmZTti5JdFyA8V70CaELtd4vSj8Qjq2wpIQ32J%2BIOvUsW%2FiYodcnly0XvFoLUcVn%2FbEXYwXUcLyiqdjk0TcYumzyysNaBNb%2B8hC2ybZhSiXb%2BRhC8r7ExDaJu3oRPU6FY%2BkIzJn0LvgeLUyrxu496Pvbru1mIx08RPPxAM%2BOodNmAYC0ZHt4TdjfLgjWmwJD4tOYBPHsyIe5DmAzFif8UbD6cROAirIslLrla63c8KspbsZw8D9r1MHhOczlAUgtbiawyXBvrS4xYK0ORdy4lAyY%2F8jXF40yu4Qxzbak2MNu3%2F9IGOqUBxoKZpZpdlG59Oq13DvbodpMXYksWzxi1XfBOzVgXXbGF0QyCk2rHyHtw%2BUc08pW94CYMKfOu%2B5S8yL2kUjbvu45JlPLgLkd6UlrKpbEy8qJq38MtQ%2FJLgKYgP2kq9DDOV33l4eo6a9tnU79h344OhZnJt9Nq%2F74zHXT2URRB9o9DSXiItCdfW7k3U7QUxgrphJpWrbB%2BZBIRuVy%2BrgXC%2FbFYZhL%2B&X-Amz-Signature=9db205deb6efeb8e5b77716525849d52b800344de73782012a8a612e3c52cc64&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

hello 慕课网的各位同学们，大家好，这一节我们继续上一节中讨论的内容，看一看剩下的负载均衡策略，它在代码层面是怎么来实现的。第一个负载均衡策略，我们来看一下。 best available row 好，屏幕放大。 OK 那这个 road choose 方法我们从前往后开始撸一遍。第一行，如果它的 load balancer status 是空，那么我们调用负例的 choose 方法，这个负例是什么？那从这个父类的名字可以看出，它似乎跟 round robin row 有那么一点的关系，对不对？我们可以看到它的成员变量是什么就是正儿八经的 round robin row 金屋藏窖。对不对？你看它这个 choose 方法中，如果这个 row 不为空，索性直接把负载均衡这个任务委托给了 round robin rowokay 那我们这里心里就明白了，这个 best available row 它的父类是基于 round robin row 底层的机制来实现的。


好，我们继续往下看，在这一行 server list 我从 load balancer 中获取到所有的服务节点。那这没什么问题，继续往下看。这一行 46 行获得到了 current timecurrent time 是当前系统的时间也没问题。那么到这个 for 循环里面看到这一句没有。我从 low the balancer status 中获取到当前服务的状态，当前服务有什么状态吗？那我们进去看一下。 OK 那再跟进一层 get service status 可以看到这里是从哪里从一个缓存中获得到 server 的 status 那如果从缓存中获取失败了会怎么样？它这里面有一个容错的逻辑，在 catch 里面，如果缓存失败了，它这边会给你默认创建一个 status 我们可以看看它这个默认创建的都是一些指定的值。 setbuffersize initialize 之类的指定值，它给你创建一个默认的 server status 并且把它添加到 catch 里面，然后从 catch 再获取一把。好，我们回退回去，再回退一把。


OK 那获取到了 server status 怎么办呢？看这里就是 best available 这个之所以叫 best available 的原因了，它这里做了一个什么判断呢？看它是不是处于熔断状态这个单词这个是熔断的意思，比较难念。那它把熔断状态一个判断条件是谁 current time 传进去了，我们来看它这个究竟是怎么个判断逻辑，这里稍微费那么点脑子。


OK 那我们这里首先第一行先要拿到熔断的 timeout 熔断的 timeout 如果小于等于0，那就不是处于熔断状态。对不对？如果它大于了当前的 current time 那说明是处于熔断状态的。那这个熔断它冒的是什么含义呢？就是说截止到未来的某个时间，这个熔断就停止了。大家明白吗？如果这个熔断状态是一分钟以后，那么意思就是说这个时间如果大于当前时间，说明到了一分钟以后的这个时间，熔断才会关闭。


在一分钟以前，熔断一直是开启的。而熔断开启代表着什么意思呢？大家在后面一节 high streaks 章节将会具体学习这个熔断。那熔断开启，我们可以把它理解成服务不可用，所以它叫 best available 那就是要找到最佳可用的服务器。你既然熔断了，服务不可用了，那我肯定不选择你了。对不对？所以大家这里看一下这个熔断的 timeout 这个属性是怎么计算来的。


OK 好，那这里我们，点进去看到又有一个方法叫 blackout periodblackout 这个词在外企里面会比较常见，因为我们经常会要发布项目对不对？如果碰到一些重大的事件，比方说国外的圣诞节、国外的某些总统日之类这种重大节日，它也有一段时间的封闭期，就叫 black out 在这段期间内是不允许发布项目的。


那 black out period 在这里面是什么计算方式呢？我们来点进去看到吗？这里有个 failure accountfailure account 是失败的个数，它是从哪里获得呢？从一个计数器中获得失败的个数，也就是在访问远程服务中你可以获知这个服务请求是失败还是成功，对不对？它可以保存到某个计数器中。


那这里 get 到了 failure account 然后还有一个阀值，我们可能会叫它阈值都是一样的含义了，它是从哪里获得呢？ connection failure thread 后也是从一个 patch 的 dynamic into property 一个缓存的属性中获得的。


好，那获得这两个阀值之后怎么来判断呢？你的 feel the count 如果小于这个阀值，那 return 0 说明你现在还不处于熔断。对不对？当你的 failure count 大于这个阀值的时候，那它要算一个 diff 也就是你 failaccount 和阀值之间的这个差值。通过这个 diff 我们再结合一些缓存中的属性来判断你的 blackout seconds 是多少秒，最终的秒数乘以1000，就是你的 blackout 时间段。 OK 我们这里返回，返回到前面一层。好，那拿到你的时间段以后，它这里怎么算？它这里会获取一个 last connection field time step 也就是你上一次连接失败的 timestep 再加上一个 black up periodblack up period 是一个缓冲，它并不代表着你接下去的访问一定会失败，而它是设置了一个缓冲，也就是从你上一次失败以后，直到这一段时间内加上这一段缓冲时间内我都认为它有可能失败，也就是让你不要再去继续访问，我们再往前。


OK 那通过前面的这个算法，我们拿到了熔断的探冒的时间。 OK 那它如果是大于当天时间，也就是在未来一个点熔断才会结束，这种情况下，那它就会返回什么？返回 true 如果它当前并没有处于熔断状态，那它返回什么？返回 false 那我们往后退一步。


好，这个 if 条件看到前面有一个反号对不对？一个感叹号。那假设当前处于熔断状态，这个 if 条件进不去，如果不等于熔断状态，我们才继续走后面的流程。那进入后面哪个流程呢？大家看这里，service status 里面我们 get active request account 那这个值是什么？是 concurrent connections 它代表着什么？代表着在当前时间连接到这台服务器的 connection 都有多少？ OK 那这里面的具体逻辑我就不带大家一起看了，大家感兴趣的小伙伴可以在这边打一个断点，在自己的服务当中应用这个负载均衡策略一路跟进去看一下。


那我这里获得了当前的连接个数，接下来怎么样，是不是要取得一个当前连接数最小的机器？那我这里有一个内部的变量叫什么 minimal concurrent connections 它的初始值是 int 的 max value 那在比较过程中，如果我的当前服务器的 connection 小于这个值怎么样？把这个 connection 替换到这个值里面去？同时这个 choose 也就是最终要访问的这台服务器，我们叫它天选之子，这个天选之子怎么样呢？就把它替换成当前这台服务器。


那我们注意到这个 if 里面，整个 for 循环它都没有一个中断条件。意思就是说这所有的服务节点我都要把它轮询一遍，直到找出最小连接数的这台机器。那我就叫他 best available 因为他怎么样他最轻松对不对？他承接的压力最小。找到这台服务器以后，就是最后两个步骤了。如果没有找到，把它扔给 round robin row 让上层的父类继续来找，如果找到了直接返回。


好到这里，整个流程就看完了，大家只要记住 best volleyball 肉的核心是什么，核心是找到一个最轻松的服务器对不对？那它的主要的逻辑在哪里？一个是 for 循环中的这个比较逻辑 if 条件。另一个就在 load balancer status 的 get single service status 中，这里包含了很多熔断判断。看到这里，这个 best volleyball 就已经完全读完了。接下来我们再去读另外一个row。


接下来一个row ，我们来看这个 retry row 好，我们直接到它的 choose 方法里。第一个属性是什么？第一个属性是 request time 当前的系统实践。紧接着我这定义了一个 deadline 它是当前的系统时间，加上一个最长 retry 的毫秒数。它是什么意思呢？就是说你可以不停的 retry 对不对？当你 retry 到时间超过了我的 deadline 比方说我现在的时间是一点钟，我的 deadline 是一点零两分。那在这两分钟之内你可以玩了命的 retry 但是一旦到了这个一点零两分这个时间点，那你就不能再 


retry 了就要停止了。 OK 好，我们这里看到第 84 行有一个 subrow subrow 来做 truth 来选择一台服务器。这个 sub row 是什么？我们看一下。你看这个 retry row 它也是金屋藏娇，它这里面有一个核心的 subrow 是由这个 subrow 来实施真正的负载均衡逻辑选择服务器的。那这里默认给 subrow 指定成了 round rubbing road 不过在相应的构造器里面，我们是可以替换掉这个 subroadok 好，我们再回来看这个 retry 是怎么来执行的。如果在第一次选择 server 的时候，他选择了一个空或者这个 server 现在挂球了，也就是无法响应我们的请求，并且当前的系统时间还没超过这个 deadline 那么这个情况下怎么样呢？我可以进行 retry 对不对？好？那我们看它是怎么来进行 retry 的。


那这个重试依赖于网友循环，它有几个中断条件，如果你的线程已经被中断了，那么同样我们这里要中断重试，如果你的线程没有被中断，那怎么样呢？我继续调用 sub row 继续选择一台服务器。而当这个服务器又选出来了空或者是这个服务器不幸的又牺牲了。而且当前的系统时间依然没超过 


deadline 那么我们怎么样？我们把这个线程，让步出去以后，等待下一次 while 循环的时候再去重新执行一把。那这个 if 条件里面判断逻辑，大家可以看到跟前面是不是一模一样的。没错，那它就是一个重试的触发条件。 OK 往后走到 while 循环后面，我们看到有一个 task cancel 对不对？我们杀个回马枪，看这个 task 是什么东西 interrupt task 什么含义？我在这里传入了一个 deadline 减去当前系统时间的差值。那这个 task 里面会做什么事呢？点进去看一下。
你看这里起了一个 timer 对不对？这个 timer 做什么事呢？它是一个后台的任


务，它在什么时候执行，它就在这个当前 deadline 减去系统差值的这个时间段来执行。如果 deadline 是 1 分 10 秒当前系统是 1 分 5 秒，那这个差值就是 5 秒钟。也就是说这个 interrupt task 将在 5 秒钟以后执行。那它执行了会做什么事情呢？就会中断这整个流程对不对？它相当于一个计时器，时间到了到点就直接中断流程。


Ok. 那如果我们在 y2 循环执行过程中这个计时器突然到了，那当然 y2 循环就被直接终止了来线程中断，走到最后我在计时器响应之前就已经拿到了需要访问的这台 server 那怎么样？ Y 循环执行结束，是不是应该把这个计时器给它 cancel 掉？ OK 继续往后走。


如果我的服务器已经找到了，并且它可以响应我们的请求，那当然是直接 return 了，否则怎么样？否则就 return 一个 none 也就是找不到服务器。Ok. we try road 的逻辑相对来说非常简单。它其实就一个特点依赖于底层具体的负载均衡策略，而它在这之上只是构建了一层 retry 的逻辑，对不对？
好到这里，我们已经跟大家分享了四个不同的负载均衡策略。接下来就是由实践过渡到理论学习的章节了。我们将用图文跟大家介绍 load balance 的注解，它的底层作用机制是什么以及瑞本的 IP 机制是如何作用的。同学们，我们下期再见。



