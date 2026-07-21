---
title: 1-9 【Demo】构建服务消费者
---

# 1-9 【Demo】构建服务消费者

[image](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/e6203e9e-e1e7-4824-aa2c-cfe4f2e2c4fe/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666NTZHLBS%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T225858Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIAckKZ5onmeKBauoPZybo1O5jzMuVP4oM3LV5CvUrL%2FMAiEA1vpNaQ9xAG2%2BU0kMjSbx83fBB7xNZKNJHRdphFzLnjsqiAQIxv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDKogHf7giFn0EyjeUircA61D4JgyuO%2FUGW9hw0fEMPmV0lgi1fh79u2dbzIxSBgyObHrMN1uFLMVNTGuCHI8GEjo6R5rfxwdCoIjMijLJdYsqZOqiVAMUFRi3Ov7LP43Bdok%2F1uvc8ygXp2LLcUS5%2Fz8ivpNre6pVI7K15A1qVXuQgaYzm6rav3AWNpyZm%2BMEHXig1zVE8MGBuY5LgUj6zVi%2B65ZnnYQ3dJ2Q%2FeN8x7D91Q9EQGbvu7%2BxXQDgEaCxmZ6RiDGo6nSDk%2FnePdowuYmOML62R2C3XPmi1YUti4BUYTj2QWZf6WxeGpTAmryEW0Uk2HQJdbQYmHJuXk3tGw%2BjK5VWJFNUNTJulf5jiGCINgci%2BLj%2Bd76DZq2Gtf3ovQM8k8xBIUBLhsJoxx%2FWadvPDOosup1SjsubOHOqWebceHxsjgtgfcXPQTHPv58znu7vv5BBee7%2FfGD9UjWdT35ChMZe0uXeNBjT2AQKJTab6CxqZsXpfU193s%2FVDMb6whtakFR6PKKjLxpvTOS1bqL34AVYwraCJdohYXuf9lAii6ZfzE8AOGLhMdBigAwyuKvF2gCTIv6AC0psJlf%2B2m%2Fq9DSUwiXQKv48O0mcALW2QSX0OOyTh26cvxUcDNInGcp1%2FbN5h%2BknKXGMM63%2F9IGOqUBaJpNQgeoPt9oiV7kBEvbfEKL9sgGLHXYFIIgMTyvha2%2BQx44tm8IH%2FyRog9dMxVB5ALsB21j1YDLEvNaxcdAe1RxSlfdK83fDNVW3TbV%2BcdcC0LCmWglFRDb7MPNvlbRv6iNt%2BHUy1hJJYoMAuNpE91AT2cg64YoH38wLyJrMGsfLkWOCDV1eZQUC27N6JlXZzYhTs%2FgLm8gFJ26lFCfwki1jy36&X-Amz-Signature=64fb43ea57aefdc0d06885c7de1b74cbb8cf504e7d55fb9e52841371cd38cc7f&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

[image](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/93d44de6-f09c-49d6-bd6a-17db675c945a/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666NTZHLBS%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T225858Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIAckKZ5onmeKBauoPZybo1O5jzMuVP4oM3LV5CvUrL%2FMAiEA1vpNaQ9xAG2%2BU0kMjSbx83fBB7xNZKNJHRdphFzLnjsqiAQIxv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDKogHf7giFn0EyjeUircA61D4JgyuO%2FUGW9hw0fEMPmV0lgi1fh79u2dbzIxSBgyObHrMN1uFLMVNTGuCHI8GEjo6R5rfxwdCoIjMijLJdYsqZOqiVAMUFRi3Ov7LP43Bdok%2F1uvc8ygXp2LLcUS5%2Fz8ivpNre6pVI7K15A1qVXuQgaYzm6rav3AWNpyZm%2BMEHXig1zVE8MGBuY5LgUj6zVi%2B65ZnnYQ3dJ2Q%2FeN8x7D91Q9EQGbvu7%2BxXQDgEaCxmZ6RiDGo6nSDk%2FnePdowuYmOML62R2C3XPmi1YUti4BUYTj2QWZf6WxeGpTAmryEW0Uk2HQJdbQYmHJuXk3tGw%2BjK5VWJFNUNTJulf5jiGCINgci%2BLj%2Bd76DZq2Gtf3ovQM8k8xBIUBLhsJoxx%2FWadvPDOosup1SjsubOHOqWebceHxsjgtgfcXPQTHPv58znu7vv5BBee7%2FfGD9UjWdT35ChMZe0uXeNBjT2AQKJTab6CxqZsXpfU193s%2FVDMb6whtakFR6PKKjLxpvTOS1bqL34AVYwraCJdohYXuf9lAii6ZfzE8AOGLhMdBigAwyuKvF2gCTIv6AC0psJlf%2B2m%2Fq9DSUwiXQKv48O0mcALW2QSX0OOyTh26cvxUcDNInGcp1%2FbN5h%2BknKXGMM63%2F9IGOqUBaJpNQgeoPt9oiV7kBEvbfEKL9sgGLHXYFIIgMTyvha2%2BQx44tm8IH%2FyRog9dMxVB5ALsB21j1YDLEvNaxcdAe1RxSlfdK83fDNVW3TbV%2BcdcC0LCmWglFRDb7MPNvlbRv6iNt%2BHUy1hJJYoMAuNpE91AT2cg64YoH38wLyJrMGsfLkWOCDV1eZQUC27N6JlXZzYhTs%2FgLm8gFJ26lFCfwki1jy36&X-Amz-Signature=9c88140d8c6751dbb3c3142124d663f58b02dc2d3bd6dbf676226002bf55d882&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

hello 慕课网的各位同学们，大家好，在这一节当中，我们将构建一个服务的调用方，也就是 consumer 消费者，并且和前面的服务提供者形成一个完整的调用链路。咱先来看一下本节的主要内容都有哪些。首先我们创建一个新的 module 叫 double consumer 它是作为服务的消费者。接下来咱在服务消费者中创建一个新的 controller 然后在里面调用 double client 中的服务。这里是将 double client 的接口层引入进来，我们只用在引入的接口上添加一个注解，甚至都不用任何的其他多余配置就可以发起远程调用了。


在最后我再给大家演示一下序列化和反序列化过程中出现的异常情况。 OK 同学们，这就是全部内容了，大家准备好的话跟我一起 entirely J 走起编程是我快乐。 996 是我的福报，咱最后一个章节，享受福报的机会不多了，同学们且行且珍惜。那接下来咱给当前的应用创建一个新的茅酒，这个毛九的名字就叫 double 杠 consumer 它是一个消费者。 OK 复制一下这里， copy 到 module name 里，然后将这个项目的文件夹路径指定到 double 下面，点击 finish 321 走，你在这个抛母文件当中，咱们不用一行手打dependency ，只用把前面已经创建好的 double client 项目中的部分 dependency 拷贝过来就可以了。说干就干走，我们抄作业去。 double client 这里咱从头抄到尾，把这所有的 12345 这五个 dependency 全部 copy 下来，然后放到 double consumer 当中，再顺手给他指定一个 packaging 类型为价。 OK 那这里 dependency 就已经创建好了。


接下来咱就去创建一个，这个启动类的冠名权包的路径，我们先给它创建出来。叫 come.eye mock 点。 spring cloud 总理启动类从哪来？咱还是从 double client 里面把它借鉴过来。直接复制 double client application 把它复制过来，然后在这边把名字给它改掉，改成 double consumer application。


Ok.那这个启动类里面的内容还用变吗？都不用变，注解也不用变，只用把这个类名给它替换一下搞定。那代码环节就只剩下最后一个 controller 了，我们在这里添加一个新的类，就给它起名叫 controller 这个 controller 上面加上一个 rest controller annotation 这个大家都非常熟悉了。然后给他创建一个用来触发接口调用的函数，它的名称我们把它叫做 publish 和 double client 中的名称保持一致了，都是商品发布。


其实在这个电商链路当中，商品发布是一个非常非常重要的环节，它那就是创建生产资料的，也就是商品的基础数据。所以大家如果有机会接触电商项目，我建议大家就去做这些像商品中心、订单履约中心或者是营销中心这种跟业务息息相关的，能学到非常多的电商场景下的应用知识。


好在言归正传，给这个 controller 添加一个接收参数，它是 name 商品的名称。那么在这里我们先要构建一个商品 product 这个 product 属性不多，只是为了测试一下攒 double 的调用情况。所以我们这里只用给它添加一个 product 的 name 就可以了。 set name 把传入的参数塞进去。


OK 那接下来就是要正儿八经的发起 double 调用了，我们先把这个接口给它引入进来，I double service 给它起名叫 double service 然后在下面直接发起它的 publish 方法调用，把这个 product 传入进去。然后在这里添加一个 return 那 controller 的方法体就算完成了，我们给它加一个 post mapping 它的路径也同样的指向到 publish 上面。


OK 似乎所有代码都完成了，但是咱这里还有一个画龙点睛之笔，咱以前在 sprint boot 当中注入接口或者是注入实现类是通过什么样的形式通过 out wire 的对不对？但是咱这里并不能用 out wire 的。为什么我们只引入了接口层，接口的实现层根本就没有引入，所以 out wire 的肯定是不起作用了。


那这里我们用谁？用 double 给我们提供的一个特殊注解叫 reference 大家注意到 double 的很多注解都有两套，咱需要的这个 reference 是在阿帕奇这个包路径下面的 double referenceok 我们把它引入进来。你可别小瞧这个reference ，咱点进去看一下这里面属性可是别有洞天。


同学们看，这每一个属性背后都是大有文章，尤其是在 RPC 项目中这个 version 非常有用，指定版本号之类的。那再往下你还会看到它的懒加载 lazy 再往下还有很多非常有用的属性，比如说咱在配置文件中配置的 check 是否检查它这个 server 存不存在 callback 的配置项，然后还有重试。总之包罗万象，应有尽有。


咱这里不会把所有的属性都跟大家讲一下，我这里就随便挑这么一个属性跟大家演示一下就好了。比方说我们在瑞本当中，如果想配置 load balance ，是不是需要在配置文件中大改一番。那咱在这里只用轻轻松松的在注解上面加一个 load balance 然后它的值我们给它指定叫 round robinok 就这么简单就实现了。所以 RPC 框架从编程体验上来说，确实是有那么一点点的优越感，非常的方便简洁高效。 OK 那 ctrl 也定义完了，接下来就剩最后一步定义项目的配置文件了。


因为咱的 consumer 在配置方式上和 client 没什么区别，我这里就直接 copy 了一个 YAML 的配置文件，非常的简单。然后它这里面的主要配置和前面的 double client 几乎如出一辙。唯一的区别也就是端口号不同。那咱这里就直接把 consumer 服务给它启动起来。然后从 postman 里调用一把，看它是不是能发起一个通向 double client 服务的调用。 OK 很快这里就启动起来了，我们把 log 清空一下，然后转战到 post 曼里。好，这里我已经创建了一个商品发布的链接，那么它通过 publish 接口发布一个名称叫做 test 的商品。好，我们点击发送。 OK 返回值是200。那回去看一下 log 在 double client 这个 application 里面，看到这里已经打出了一行 log publishing product test 说明我们 double 的 consumer 到 double client 之间的调用通路已经完全打通了，那本节的任务也就完成了。


这里我想多聊两句 RPC 和友瑞卡之间的一个使用体验，从我个人的经验来说，我使用 RPC 的时间更长。那我在接私人项目的时候，我更多的会选择 double 然后在工作中大多是使用的 hsf 那是淘宝开发的一套 rp C 的框架。那它在整个阿里集团中已经成为一个既定的 rp C 框架标准了。 RPC 框架的成熟度以及它的发展速度在业界已经得到了广泛的证实。我们可以想大家在淘宝上经历的双11，双 12 的抢购，在后台支撑你的这些访问流量的全是 RPC 框架。


虽然我们章节中应用的是 spend cloud 的全家桶，所以咱使用的是基于尤瑞卡的 rest API HTTP 接口。那我建议大家作为技术储备同样的也去学习一门 RPC 框架，比如说 double 就是一个不错的选择或者是 hsf 尽管 RPC 框架有点那么单打独斗的意味，并不像 spring cloud 全家其上阵是整个 cloud 架构的一个体系组件。但是随着 spring cloud 中阿里巴巴组建的崛起，以及奈库斯作为一个注册中心的崛起，那我相信奈克斯为继承 double 所做的这么一番努力，也能给 double 和 spring cloud 做一个牵线搭桥。


而 double 也是近些年来阿里巴巴集团在开源领域上持续发力的一个体现，结合了阿里这么多年在电商领域持续积累的高并发、高可用的经验，相信 double 在后面的几个升级版中可以取得不俗的战绩。 OK 同学们，那这一节的内容到这里就结束了。在后面的章节里，我将通过图文教程跟大家介绍 double 的容错策略以及它的负载均衡。 OK 同学们，那我们下一节课程再见。

