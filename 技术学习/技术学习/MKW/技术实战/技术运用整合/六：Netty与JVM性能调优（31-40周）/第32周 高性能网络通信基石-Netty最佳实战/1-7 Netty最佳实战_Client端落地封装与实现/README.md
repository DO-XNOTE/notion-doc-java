---
title: 1-7 Netty最佳实战_Client端落地封装与实现
---

# 1-7 Netty最佳实战_Client端落地封装与实现

[image](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/49aca149-29eb-457b-a61c-cc6534987da2/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VBCY6V73%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T230019Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDew3Nyb7HhZVEHSVCbZO8rbiKYYEL7zsQXkABJYTUkkAIhAOnX48%2FzNXtqE9PhFfIJEpJjSfWrkFWKd4fpARtMTnX6KogECMb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgxmV0Y7JSG1Etu9A6Uq3AMHA4iZOGCRUYgbQ2mwfgNJ5V8M1b3si%2BdXILGQkvgI%2FkcTFr%2FSsfvj5qtYXbW1OPI3XUbkRziNdjjsnCxlkVbnEuHcoxJTDfJqRGnSQ%2BKk8XwMLW2ScGntoM0h8z9Dt5XglhdkmhU9vsOVQQAFeWMaBJdOon6vYxCW9KGQDLucxiqK%2FJD7visouRNNplMZyxA8obW0dQciQq9Eva56%2FYfeFqbFC%2B1pSAqzTjuUqIpH5xwbVO4D9z4%2Fn%2Fi0rc39NzZmmBPoDkWPhnTmpUkjiGpSEjoTOb8Vv2rI8lyyImUgAokOvNjyZDlFUydx3FzmwRj7GAPviOKwO6GpYwKGHR%2BsvdulLbVGUD38ppD8JoY8JtLlXURoO64LytqrGrXkTBrZnFlggCW1xFtuJohggbh6YLCLujhcANLCRZpQScV4pD7ZP5ZBWBgUEZRYpWvcy3YKfJ8%2F2L3YRdskZ%2FGkEVQReYI5MtANZTaKYpU%2Ff8uw92QxeHsvGhIKK3%2BAWrziZzNz6w5N%2FoZx1QmnizrgrDFgu6PcY3pRFK9sfU%2FYQqgQdoDVs%2FGW8c3uMYg4zeFOdtmN8FlMsPnwy3bm2%2BI4r1tsKeyERh%2BOZFy3aGK7%2BHPcs32gZQM6HajtwCCSnTCHt%2F%2FSBjqkAVilz3TP8AuAc6w667tp7rTfRtRuWpYIzbnDTcVC%2B8g3sfDPO06PJ2cbPZJdUt12%2BA5iSefOab1vw0GXtlFiTpKk7N7MfZIb3Gttx%2FAbdnaiKcj07%2Fs0VcQiwwhp4jvTU02x%2BkS6oO8YjCyWgkmMivrlomDl3qBOm9UlWjAvJHoIZ6zxVWjP8oJ583SfkMuree4p76WEPvy6xnRAK45WXjI9iBhC&X-Amz-Signature=91cd3651a5941e9c38ea001f6b07eb7d474c93ba12e44b0aa7978048151cb42b&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

OK 小伙伴们，这节课我们来继续往下去讲。上节课我们已经对于 server 端，我们数据给我发送到 server 端， server 端对于 handler 怎么去做处理已经讲完了，我们使用这种方式去做处理。接下来其实我们要想考虑一个问题，我们现在给我回送响应，以后就是 server 端给我们的客户端回送响应，我们应该怎么去接收？在这里我们直接来看一下client， client 里边肯定是由他的什么由 client handler 去做处理了，我们来点进去。 client handler 稍等一下哈，有点卡。


client handler 点进去之后，我们来看看。这块很简单，对于对象，它肯定也是我们的message，对象对不对，我们可以直接拿过来去做一个实际的解析，我们做什么事情还是要做一个异步化处理，因为我们要不能去阻们 client 端的 IO 线程，就是我们 client 端的 worker 的 IO 线程。OK，同理。老师在这里直接把 worker 代码 copy 过来，异步去提交就好了。在这里边我们首先这是肯定要有的。接下来就是写代码转换，肯定是 message module 了，点 message message，这肯定是 response 了，哈。 response 等于转换一下，把 message 转过来，转成我们对应的就可以了。直接把它提交到异步的线程池里面去做一个处理就好了。点什么submit，submit， summit task 什么，肯定也是实现了 runner more 接口的一个具体的类了。在这里小伙伴们可以参考我们 common 包下了什么 comment 包，里边有一个叫做 message task for request，我们肯定会有一个 message task for response 对不对？ message task for race once 好了，他肯定首先是实现了 run 接口的。我们来快速的去把这个东西实现一下。这个东西都是大同小异的，它实现我们的乱方法。


好。接下来它的构造函数里边肯定也会有那两个参数对不对？一个是我们写对于 message request module 的点和 sorry request modular。 sorry 现在这个 message model 了，哈，所有的没有 request 点 message 这第一个。


第二一个就是我们的 channel under context c， t x 有这两个对象，我们声明对应的成人变量做一个声明。好在这里边我们private，它还有一个 private 我们的 channel handler context 对不对？有这两个，c，t， x 有这两个。之后，紧接着我们在构造方法上我们去做一个赋值就好了。 this 点儿 message 等于message， this 点儿什么 contest 等于contest。


好。搞定完这件事情了之后，接下来我们看一下乱方法里边我们要写什么样的内容。同学们想一想，也是跟我们之前的逻辑可以保持一致。我们从 message 里边拿出我们想要的信息，调用我们回调的方法就可以了。好了，小伙伴们，现在其实大家可以看老师的这幅图，回过头来我们看这幅图，在这里边把重新切换到这里。看这幅图，

[image](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/f8d6a988-0e43-4c56-b3b4-2c1654838c5d/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VBCY6V73%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T230019Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDew3Nyb7HhZVEHSVCbZO8rbiKYYEL7zsQXkABJYTUkkAIhAOnX48%2FzNXtqE9PhFfIJEpJjSfWrkFWKd4fpARtMTnX6KogECMb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgxmV0Y7JSG1Etu9A6Uq3AMHA4iZOGCRUYgbQ2mwfgNJ5V8M1b3si%2BdXILGQkvgI%2FkcTFr%2FSsfvj5qtYXbW1OPI3XUbkRziNdjjsnCxlkVbnEuHcoxJTDfJqRGnSQ%2BKk8XwMLW2ScGntoM0h8z9Dt5XglhdkmhU9vsOVQQAFeWMaBJdOon6vYxCW9KGQDLucxiqK%2FJD7visouRNNplMZyxA8obW0dQciQq9Eva56%2FYfeFqbFC%2B1pSAqzTjuUqIpH5xwbVO4D9z4%2Fn%2Fi0rc39NzZmmBPoDkWPhnTmpUkjiGpSEjoTOb8Vv2rI8lyyImUgAokOvNjyZDlFUydx3FzmwRj7GAPviOKwO6GpYwKGHR%2BsvdulLbVGUD38ppD8JoY8JtLlXURoO64LytqrGrXkTBrZnFlggCW1xFtuJohggbh6YLCLujhcANLCRZpQScV4pD7ZP5ZBWBgUEZRYpWvcy3YKfJ8%2F2L3YRdskZ%2FGkEVQReYI5MtANZTaKYpU%2Ff8uw92QxeHsvGhIKK3%2BAWrziZzNz6w5N%2FoZx1QmnizrgrDFgu6PcY3pRFK9sfU%2FYQqgQdoDVs%2FGW8c3uMYg4zeFOdtmN8FlMsPnwy3bm2%2BI4r1tsKeyERh%2BOZFy3aGK7%2BHPcs32gZQM6HajtwCCSnTCHt%2F%2FSBjqkAVilz3TP8AuAc6w667tp7rTfRtRuWpYIzbnDTcVC%2B8g3sfDPO06PJ2cbPZJdUt12%2BA5iSefOab1vw0GXtlFiTpKk7N7MfZIb3Gttx%2FAbdnaiKcj07%2Fs0VcQiwwhp4jvTU02x%2BkS6oO8YjCyWgkmMivrlomDl3qBOm9UlWjAvJHoIZ6zxVWjP8oJ583SfkMuree4p76WEPvy6xnRAK45WXjI9iBhC&X-Amz-Signature=d84dac816e297e34ae6d9fb2f47ab706b477ffd8b5d6dbeea4c845ddef348c40&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

这幅图就是消息的实时推送。最开始我们的 client 端去把消息推送到我们的 server 端， SO 端执行了自己的业务逻辑，可能做落库了，给我回送响应，是不是回送过来，回送给ACK，现在是什么？我们现在实现的回送 ACK 的对不对？回送 a C k。


我们要做确认，更新一下数据库的标记，如果有一些不符合我们状态的，我们通过定时任务把它抓出来，然后再重新推过去。就是这么一个逻辑。我们现在同学们想一想，我们发送消息的时候，我们请求的模块对于 module 是user，它具体的指令可能是update、 Z5 或者是查询等等。操作。根据具体的 module 和具体的 CMD 指令，找到对应的反射的对象去调用执行，执行完了之后给我回送结果的时候，我们回送结果应该怎么去回给他？其实我们给他回送结果可按端其实也是一个道理，也是想通过反射去把我们的具体的业务逻辑去封装到 inwork table 里边，对不对？他们两个因为我们 common 包，他们两个是共有的，公共的，所以在这里边就需要考虑一个回送标记的。


回送的时候他的command，回送的时候他的 model 了。跟 command 应该怎么去写的问题。好了，我不知道咱们小伙伴们对业务有了解，我们回过来代码，你想一想，我们暂且去找到 server 的service，这是我们 server 端的module，是 user command。做完了这个事情之后，我是不是要给它写回去？我给它写回去的逻辑我都封装到 task request 里边了，对不对？在 request 里边。这里边调完引入课之后，我给他回送 module 跟command。


这个 module 跟 command 是不是我们的客户端也应该实现一个service？同学们想一想，是不是我们的客户端也应该实现一个service？这个 service 里边去。其实你如果没有太多的强迫症，你可以直接写上什么，咱们叫做 user return。 user return service 里边，你如果没有太多强迫症，你就可以按照正常的方式去写就好了。我们还是要有 module 的对不对？这个 module 的它的值还是等于什么？还是等于user？能理解我说意思。这里边具体的方法，比如public，当然这里边给我回送响应，我就不需要再确认了。所以 why 的具体我还可以叫做save，或者是叫做 save return 的方法，对不对？好了，这里边还需要一个注解，我们的 c m d， c m d 也是一样的，他们两个应该是对称的，对应上咱们叫C5。方法能理解。我说意思。可能后面还有一个 update 方法。


好。如果你没有强迫症，相当于我们的客户端跟我们的服务器端所对应的 handler 所对应的实际的业务处理器同一个key。但是如果你有强迫症，想区别开来，客户端跟服务器端其实也很简单。其实我举个例子，简单来说，你在调用完 serve 方法之后，你手工的去重新定义一下我们的 module 了，跟我们的 command 重新定义的就跟我们客户端保持一致。但是如果你说老师，我就不想这么去叫，我就不知道他到底是 so 的端还是 come on 端。


很简单，举个最简单的例子，就是在你进行 request 设置的时候，你可以搞一个常量，比如我们定义一个固定，好规范，咱们叫做什么？叫做 prefix 或者叫做 post 固定变量，我也不知道怎么去形容它哈。咱们叫做 inwork return。尹洛克维特这个尹洛克 return 我可以去写，死了我说就叫中华线杠return。好。这样的话或者简单搞一个 return 就好了哈。简单搞一个return，不要搞那么复杂。大家能小伙伴们能理解老师的意思就可以了。好了，这个杠 return 什么意思？就是我在回送的时候，我把我的内容上面加上一个VK，好固定的请求过来。


我们 server 端是通过 module 了跟 command 去确定我们 user service 里边的 save 方法的对不对。通过这两个，我想用回去的数据响应数据。我们的 client 端怎么去接收？通过哪个方法去接收对不对？没有强迫症，你看小伙伴们，你就用原来的 save 原来的 user 跟 save 就可以了。如果你有强迫症，你就像老师说的是不是我们可以定义一个常量加杠return，标记一下，给他的数据包，后面加一个杠return。


很简单，我们刚才我跟小伙伴说的就是我们最开始叫做 user return service，是不是？是不是叫这个名字就好了，对吧？他叫这个名字都加上return，这样是不是就对应上了？我的响应过来的时候，我其实本质来想也是可以把这些数据扫描加到了我们的 worker table 里边，是不是？那也是一样道理。 OK 好了，这样其实也可以，我们再回过头来加上这个类型之后就好办了。我们再继续去写我们的编码，我们的response，我们看看怎么去做响应过来的数据是不是我们 model 了，可以取到它具体的点。 get model 了取到 sorry get model 了。这个 model 的同学们是什么？同学想一想对不对我们这个 model 了，它还不支持什么？哈，这个 model 其实它具体的内容是什么？我们刚才所看到的 request 里边叫所拼接的，它加上 return 加后缀，说白了是什么？比如 user 杠 save 杠 return 对不对？它的 command 很简单，那就是 save 杠 return 对不对？ save 杠 return 这个叫CMD，这个叫 get c m d。搞定好了，这两个出来了。还有比较关键的吗？响应的结果是不是？响应的结果叫做 result type 是不是 result type？ t y p e 好，等于我们的 this 点 message 点 get result type 取出来了。


这个响应结果有什么意义？我们可以通过响应的结果来知道他到底请求成功了还是失败了，对不对。这响应结果是很有意义的，除了有他，其实还有一个。我们的。响应的内容是什么？我们写一下响应的结果到底是成功 success 还是失败。响应的内容是什么？响应的内容很简单，通过它转 get body，点 get 点 to 贝塔 string 直接可以取到。在这里边我们用一个字符串是一个贝塔字节数组来接收一下。哈，贝塔好是不是就可以了。我们再调我们自己的 involve 方法，因为我们自己的对于 client 端自己的，是不是他也会去帮我们去封装到加载的时候，在我们扫描的时候会帮我们扫描到 inwork table 里。所以道理是一样的。我们直接来看一看。


直接通过 in worker 去可以去叫做 in worker table 是不是 d r get in worker 直接取到了？ get in worker 直接取到对应的你的 module 了？跟 command 这两个是不是？其实说白了跟对应上它返回的什么？它返回的方法，它返回的 inwork 对象，我们来执行它一下就好了，是不是来执行一下？第二调一下 in work 方法，把参数传进去。


这里参数我可能需要比较关注的，我不关注这个。它具体返回响应的 module 跟 command 是不是？我可能比较关注于这个结果，我可以把这个结果扔进来，我可能还关注 data 内容是什么，对不对。掉完了之后，因为我们就再也不需要返回值了，因为这回是相当于服务器端给我的响应，我再也不说再给他回送响应，就相当于没完没了，所以我暂时就不需要了。
在这里边我们看一看，就多了两个参数，一个是贝特字节数组的data，还有一个是 result type。所以我们现在就可以确定，在响应的时候，我们直接拿过来叫做 b y t e data 可以了。 OK 这里边也会有。好了，我们现在其实就已经完美的去解决了这个问题。我们 response 的时候注意，在响应的时候我们做完了这件事情。调用完了之后，也不用给他再回送，再 right flash 再发出去，不用了。但是你用完了，这个 message 你用完了。为什么？我说老师不把 message 传进去，为什么你要非得去传它里边实际的值？因为 message 这个内容，你仔细再看一看这个message，它其实是我们message。东西到底是什么？我们通过 client handler 把它异步去提交。当然这块还没有去做 new 什么。 new 一个message，我们叫做 task for response 对不对？OK，其实我传递的内容就是 message 跟 c t x。在这里我可以去把 message response 传进去，也就是我们最大化一下。我跟小伙伴讲清楚，我现在 channel read 我的客户端读取服务器端给我的响应信息。


说白了message，说白了就是response。把 response 传进去了，引用在这里对不对？然后点进去这个引用是谁？是不是他？也就是他。我为什么在这里不去把这个 message 直接传给野沃克函数，为什么？因为在 net 里边，我们去要做资源的释放，尤其是你。其实它message，说白了它的最上层是什么东西？从 handler 里的 object 来的，它其实是一个什么东西？它就是一个buffer。这个 buffer 用完了，你必须要自己回收释放。所以为了让你的引用不再去往下去使用传递，我建议小伙伴们一定在这里用完了之后，就不要等到调用之后再去把它回收。你把你想用的这传进去调用就好了。所以我们的代码一定要这样去写。sorry，叫做 try finally。把里边的代码放到这里，在 finally 的时候去把你想要的资源引用的 reference a reference a reference cut beautiful 最后一个第二release，就一定要把你自己的资源释放，我们要释放的时候它okay。这个就是我想跟大家说的一个重点，在实际的开发中经常可能会出现错误，就在这一定要把它注意释放。当然这 context 你隐了，如果不用，其实你完全可以把它去掉，因为你再也不用去回送响应了。


好了，为什么我要释放？同学们其实可以想一想这个问题。好，现在整个我们的编程模型，整个我们的编程模型就已经搞定了，我们的从 server 端到客户端，已经把整个的通信模型已经搞定了。接下来刚才那个问题，为什么我说我要资源释放？好，在这里我们下节课跟小伙伴们来讨论一下关于资源释放的问题，也就是关于我们在 response 的时候，我一定要资源释放，但是 request 的时候就是 message task for request 的时候，为什么这里边用完了资源没有去释放，是不是好？这个问题其实是一个比较有意思的问题。我们现在把整体的逻辑实现了之后，下节课我们来比较关注资源释放。好了，这节课就讲到这，感谢小伙伴们收看。

