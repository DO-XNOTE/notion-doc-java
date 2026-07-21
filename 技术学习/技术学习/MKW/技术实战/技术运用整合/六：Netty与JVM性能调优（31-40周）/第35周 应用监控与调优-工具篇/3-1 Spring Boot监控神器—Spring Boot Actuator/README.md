---
title: 3-1 Spring Boot监控神器—Spring Boot Actuator
---

# 3-1 Spring Boot监控神器—Spring Boot Actuator

[image](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/be9cad65-8435-4968-b9fa-a155717774d7/SCR-20240727-sojc.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZCH3RIU6%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T230059Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIGaJNb0nK1uhQKmI2e65fCNKxMy4kqcoHES%2B3I%2BPDmuqAiBngJ%2FzQN9smLDQz3NwdjKhSLB8XfGK4DAnDA0gyvLwmyqIBAjG%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMHt397bB1qc6KuAz5KtwDSfolu1CJxWRu%2FrmZYKm7VYp6EuOhYrgxVIQn8dD5CcXmW9MdCFbutjc02rHxAhi9hHwuWuxRYLb2eHbOsburq6F1%2FzeC%2FDac0M3Ibj6P9MSbUHMt2D44axxXdzWkl7A%2BRJjfEhWsa%2BwzeusAcTPw8l443gnk0TLNXx0NfkdGrIQhLCjBUt2kvC%2FNhGrSOjbI%2B1xE9MVWZTap4x%2Ff13veBv0EhG%2F8Nykvn0TQxhGUv9KVSnuKcbwrdHY8TzUCy1fAjiA4BdvCq08owb9n5o2OdEZ%2FWW0%2Fphrfx0%2BQlfboqk%2BlZdkoj%2FORDBYa345Tcp1eQub%2BPSgUPOne0lopd5lur0yae7xWJjVR%2BqAxELPsQv3yG562ixuS8lfh5uuM4Dq8iuBCqSlDdeuka7%2BY5BN%2FY%2FvTwBp838xcippKbTlmaf09ni7o7Ft25CSXgqeyLHBYUZEh8aKaskZ6bWjO3JrS4gP4%2FWoRJw6ljxFJ4c9vjeGFH8tW6HaBr8ioR%2BfOxrbd4Ik694i1RqmTFjhgcVRyuIKYP5%2Fs94HNSy8rX32frLllyvMXUcOmf93l2Ilk4ZeKss9I%2BgX1sLl0I4YNkFWdIIh%2BfVgp8OeazHkJLUkUTbIyj48SUw%2B7bgcq1UowzLf%2F0gY6pgHsr1uL4Efo7RopVsZWWvL2utspurxPhcSKPrME7S9G666NNXdrZ1nMF7%2F5QHDmL3GV8%2FSoF%2Bdrg6vMJFYI0dU89KDqyJLpu%2FOKL70ckkk%2F5F%2ByAVIcYQ%2B7YPEMyz1rWxHAKqe%2Fp6gKOLCdvqAjY%2BPqWMP960ZVC7LHNUb5K6Ax573OWUtOQMvHc1B51%2BEvzq%2Bsmepxdd7QqQt3bx9yeGpJc3KKybWF&X-Amz-Signature=e88827854a4a53af5622a2784a1b99727481a9b893943e6cc4b3e04e548f0942&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

[image](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/b2c77249-88cb-4ef0-b5da-d88b434300a9/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZCH3RIU6%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T230059Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIGaJNb0nK1uhQKmI2e65fCNKxMy4kqcoHES%2B3I%2BPDmuqAiBngJ%2FzQN9smLDQz3NwdjKhSLB8XfGK4DAnDA0gyvLwmyqIBAjG%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMHt397bB1qc6KuAz5KtwDSfolu1CJxWRu%2FrmZYKm7VYp6EuOhYrgxVIQn8dD5CcXmW9MdCFbutjc02rHxAhi9hHwuWuxRYLb2eHbOsburq6F1%2FzeC%2FDac0M3Ibj6P9MSbUHMt2D44axxXdzWkl7A%2BRJjfEhWsa%2BwzeusAcTPw8l443gnk0TLNXx0NfkdGrIQhLCjBUt2kvC%2FNhGrSOjbI%2B1xE9MVWZTap4x%2Ff13veBv0EhG%2F8Nykvn0TQxhGUv9KVSnuKcbwrdHY8TzUCy1fAjiA4BdvCq08owb9n5o2OdEZ%2FWW0%2Fphrfx0%2BQlfboqk%2BlZdkoj%2FORDBYa345Tcp1eQub%2BPSgUPOne0lopd5lur0yae7xWJjVR%2BqAxELPsQv3yG562ixuS8lfh5uuM4Dq8iuBCqSlDdeuka7%2BY5BN%2FY%2FvTwBp838xcippKbTlmaf09ni7o7Ft25CSXgqeyLHBYUZEh8aKaskZ6bWjO3JrS4gP4%2FWoRJw6ljxFJ4c9vjeGFH8tW6HaBr8ioR%2BfOxrbd4Ik694i1RqmTFjhgcVRyuIKYP5%2Fs94HNSy8rX32frLllyvMXUcOmf93l2Ilk4ZeKss9I%2BgX1sLl0I4YNkFWdIIh%2BfVgp8OeazHkJLUkUTbIyj48SUw%2B7bgcq1UowzLf%2F0gY6pgHsr1uL4Efo7RopVsZWWvL2utspurxPhcSKPrME7S9G666NNXdrZ1nMF7%2F5QHDmL3GV8%2FSoF%2Bdrg6vMJFYI0dU89KDqyJLpu%2FOKL70ckkk%2F5F%2ByAVIcYQ%2B7YPEMyz1rWxHAKqe%2Fp6gKOLCdvqAjY%2BPqWMP960ZVC7LHNUb5K6Ax573OWUtOQMvHc1B51%2BEvzq%2Bsmepxdd7QqQt3bx9yeGpJc3KKybWF&X-Amz-Signature=aeaaa553c00f82ac46d99d4ebdd2b550c6c0dc25b85518b7ba74754eb874dcc4&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

这节课来探讨第二款监控工具，叫做 spring boot actuator。它是由 spring boot 官方提供的监控工具来演示一下。要想使用 spring boot actuator，只要为项目加上， spring boot start activator 的依赖就 OK 了。 import 一下整合好了。我们启动项目，可以发现，只要整合 spring boot actuator 之后，就会打印这一行日志。他说。现在项目暴露了两个端点，在这个位置我们不发法文，看看 log host 8088 actuator。 actuator 端点是 springboot actuator 的导航单点，它可以列出当前 springboot actuator 激活的所有监控单点。就目前来看， actuator 暴露了两个单点。

[image](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/d1381f13-648c-48d6-b2f9-1d8e1f925d24/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZCH3RIU6%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T230059Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIGaJNb0nK1uhQKmI2e65fCNKxMy4kqcoHES%2B3I%2BPDmuqAiBngJ%2FzQN9smLDQz3NwdjKhSLB8XfGK4DAnDA0gyvLwmyqIBAjG%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMHt397bB1qc6KuAz5KtwDSfolu1CJxWRu%2FrmZYKm7VYp6EuOhYrgxVIQn8dD5CcXmW9MdCFbutjc02rHxAhi9hHwuWuxRYLb2eHbOsburq6F1%2FzeC%2FDac0M3Ibj6P9MSbUHMt2D44axxXdzWkl7A%2BRJjfEhWsa%2BwzeusAcTPw8l443gnk0TLNXx0NfkdGrIQhLCjBUt2kvC%2FNhGrSOjbI%2B1xE9MVWZTap4x%2Ff13veBv0EhG%2F8Nykvn0TQxhGUv9KVSnuKcbwrdHY8TzUCy1fAjiA4BdvCq08owb9n5o2OdEZ%2FWW0%2Fphrfx0%2BQlfboqk%2BlZdkoj%2FORDBYa345Tcp1eQub%2BPSgUPOne0lopd5lur0yae7xWJjVR%2BqAxELPsQv3yG562ixuS8lfh5uuM4Dq8iuBCqSlDdeuka7%2BY5BN%2FY%2FvTwBp838xcippKbTlmaf09ni7o7Ft25CSXgqeyLHBYUZEh8aKaskZ6bWjO3JrS4gP4%2FWoRJw6ljxFJ4c9vjeGFH8tW6HaBr8ioR%2BfOxrbd4Ik694i1RqmTFjhgcVRyuIKYP5%2Fs94HNSy8rX32frLllyvMXUcOmf93l2Ilk4ZeKss9I%2BgX1sLl0I4YNkFWdIIh%2BfVgp8OeazHkJLUkUTbIyj48SUw%2B7bgcq1UowzLf%2F0gY6pgHsr1uL4Efo7RopVsZWWvL2utspurxPhcSKPrME7S9G666NNXdrZ1nMF7%2F5QHDmL3GV8%2FSoF%2Bdrg6vMJFYI0dU89KDqyJLpu%2FOKL70ckkk%2F5F%2ByAVIcYQ%2B7YPEMyz1rWxHAKqe%2Fp6gKOLCdvqAjY%2BPqWMP960ZVC7LHNUb5K6Ax573OWUtOQMvHc1B51%2BEvzq%2Bsmepxdd7QqQt3bx9yeGpJc3KKybWF&X-Amz-Signature=623078f127c3877d600b0de4eb79181ae68d996728b31b505cd5c9501509c216&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

第一个叫做 hairs 端点，也叫健康检查端点。我们访问看看，可以看到返回了一段JSON，说 status 是up，它表示状态正常。事实上， status 有 4 种。取值来看一下。 UP 表示正常，表示遇到了问题不正常。第三是 out of service，表示资源没有使用，或者不应该去使用。最后， unknown 表示不知道健康检查究竟检查的是什么。我们加一个配置，这样就会有直观的感受了。

[image](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/af841fca-8c43-4367-a594-7aaf8403cef4/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZCH3RIU6%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T230059Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIGaJNb0nK1uhQKmI2e65fCNKxMy4kqcoHES%2B3I%2BPDmuqAiBngJ%2FzQN9smLDQz3NwdjKhSLB8XfGK4DAnDA0gyvLwmyqIBAjG%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMHt397bB1qc6KuAz5KtwDSfolu1CJxWRu%2FrmZYKm7VYp6EuOhYrgxVIQn8dD5CcXmW9MdCFbutjc02rHxAhi9hHwuWuxRYLb2eHbOsburq6F1%2FzeC%2FDac0M3Ibj6P9MSbUHMt2D44axxXdzWkl7A%2BRJjfEhWsa%2BwzeusAcTPw8l443gnk0TLNXx0NfkdGrIQhLCjBUt2kvC%2FNhGrSOjbI%2B1xE9MVWZTap4x%2Ff13veBv0EhG%2F8Nykvn0TQxhGUv9KVSnuKcbwrdHY8TzUCy1fAjiA4BdvCq08owb9n5o2OdEZ%2FWW0%2Fphrfx0%2BQlfboqk%2BlZdkoj%2FORDBYa345Tcp1eQub%2BPSgUPOne0lopd5lur0yae7xWJjVR%2BqAxELPsQv3yG562ixuS8lfh5uuM4Dq8iuBCqSlDdeuka7%2BY5BN%2FY%2FvTwBp838xcippKbTlmaf09ni7o7Ft25CSXgqeyLHBYUZEh8aKaskZ6bWjO3JrS4gP4%2FWoRJw6ljxFJ4c9vjeGFH8tW6HaBr8ioR%2BfOxrbd4Ik694i1RqmTFjhgcVRyuIKYP5%2Fs94HNSy8rX32frLllyvMXUcOmf93l2Ilk4ZeKss9I%2BgX1sLl0I4YNkFWdIIh%2BfVgp8OeazHkJLUkUTbIyj48SUw%2B7bgcq1UowzLf%2F0gY6pgHsr1uL4Efo7RopVsZWWvL2utspurxPhcSKPrME7S9G666NNXdrZ1nMF7%2F5QHDmL3GV8%2FSoF%2Bdrg6vMJFYI0dU89KDqyJLpu%2FOKL70ckkk%2F5F%2ByAVIcYQ%2B7YPEMyz1rWxHAKqe%2Fp6gKOLCdvqAjY%2BPqWMP960ZVC7LHNUb5K6Ax573OWUtOQMvHc1B51%2BEvzq%2Bsmepxdd7QqQt3bx9yeGpJc3KKybWF&X-Amz-Signature=f98b81f40db0aaed9fd028ebdb4757a54bfc9faccf7c34c809182936cab47b4f&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

加上 management endpoint health show details，把它设成 always 重启项目。笑了。刷新可以看到 heres 单点能够监控项目的数据库以及磁盘是否正常。上面的 status 是一个总状态，它是一个聚合的结果。下面的每一项则是每种资源的监控结果。所谓的健康检查，其实检查的是当前应用所使用的资源。 my actuator 能够监控哪些资源的？来看代码。 spring boot 内置的 higher indicator 的实现类有这么多，每一款都是对一种资源的监控。比如可以监控 Passenger 一种 NO SQL 数据库，可以见过 coachbase 一种 NOSQL 数据库，数据源磁盘， elasticsearch，influxdb 等等。并且全部是自动的。它是如何实现的？我们来以数据源的检查为例分析一下。


核心方法在 do health check，我们打个断点刷新进到断点了。他说如果没有数据源，直接来个 status 是UP，来个 detail 是database，是unknown。也就是这里是 up detail，会来个 database unknown。目前我们肯定会进 l 四分之 f 8 command option are 跳到下一个单点，首先它调了一个 get product 这一行代码，它会用 JDBC template，这是 spring 自带的一个轻量级的操作数据库的框架。用 get product 加到这里，其实本质上是用数据库的驱动获取一下当前数据库是什么产品，是 Oracle 还是Mysql。


F8 查出来说数据库的产品是Mysql。接着它就直接构建消息体了，这状态是 up 的。再来个详情，是Mysql，也就是构建了这么一段。我们继续看F8，它又用 get validation query 把刚刚查到的产品名称 Mysql 传进去了。


come on up as in b， F8 首先它调了这里的query，查出来是 SELECT 1，我们这里代码就直接返回了F8，直接到 return 了对吧？如果这个 query 是个空字符串，它会用数据库的驱动传入数据库产品的名称，查到一个 validation query。这里其实也隐含着一个知识点，那就是数据库驱动有去定义数据库的检查SQL。如果用数据库的驱动依然查不到 validation query 的话，那么它就会进 default query，也是个 SELECT 1。总而言之，代码会返回 SELECT 1。好， come on everything up。又做了一次判断，说这个 validation query 有值的话，就进来F8，他就用 JJBC 


template 发送了 select 一everybody，结果肯定是1。最后他返回了一个响应体 HELLO 1，也就是这里的 hello 1。如果数据库不正常，这个代码就会抛异常。如果抛异常，在哪边构建消息体？我们在 do heres check 上面按下command，就可以找到 abstract health indicator。在这里他做了一个trackedge，这样这个方法只要构建 UP 的情况就可以了。一旦抛异常，这里统一做处理，把这里变成down。也就是一旦 do heres check 方法泡异常，这一段，它的 status 就会变成down，聚合出来的 status 也会变成down。因为我们的项目往往是强依赖数据库的，如果数据库都不正常了，我们的项目也不能正常工作了。


好，这是数据源的健康检查。其他资源的健康检查也是类似的。同学们感兴趣也可以看看。如果你的项目所使用的某种资源 springboot activator 并没有实现健康检查，该怎么办？比方你的项目使用了 fast d a f s，这是一款国产的分布式文件系统 spring boot actuator，并没有实现对应的监管检查。这个时候你就可以参照我们这里的代码去实现自己的健康检查。比如实现一个类叫做 fast d f s health indicator，继承一下 abstract health indicator，并实现一下 do cares check 方法，这是健康检查。


再来看一下 info 端点。 info 端点并不是一个监控端点，而是一个描述端点，目前它返回了一个空。 info 断点的使用方式非常简单，我们也来加一段配置。 info 配置方式 value 的形式就可以了。 key 和 value 可以随便写，比如 a 等于b， c 等于d，a、b、c、 d 应该写什么？建议写项目的描述信息。比如项目名称，叫做 foodie DV 项目的作者。比如叫大木。项目负责人的邮箱。比如是某个邮箱。这样只要访问 info 单点，就可以了解项目的基本信息了。重启项目，刷新，可以看到 info 端点已经展示了我们的配置。应付单点作为一个描述性的单点，它有什么实际的作用吗？我们可以举一个例子。
还记得前面讲解 Skyworking 告警的时候，我们可以实现一个自己的 REST API，一旦触发告警，就调用这个API。之前我们说可以把发送邮件等业务放到这里。你要知道，在一个大型的项目下面，不同的微服务可能有不同的负责人。 AV 服务的指标达不到要求，触发了告警，这里的告警应该发送给 AV 服务的负责人。同理， b 微服务的指标不正常，触发的告警应该发送给 b 微服务的负责人。


这里我们可以怎么写？可以这么弄。根据服务发现组件上面的服务名称，找到对应的actuator、 info 断点，进而找到对应的 owner email 配置的值。当然了，这里的 owner email 和配置文件里面，这里的 key 要相同，就可以实现刚刚我们说的目标了。回到PPT，除 heres 单点以及 info 单点以外， actuator 还提供了若干多的监控。单点有这么多？不过默认情况下只有 hairs 端点以及 info 端点是显示的，其他端点全部是隐藏的。要想把这些端点暴露出来，需要添加配置。


Your management and points web exposure include.
good 写上想要暴露的端点，比如 ENV config props，多个用逗号分隔。如果想要暴露所有的监控单点，配置人心就可以了。我们重启项目，观察日志可以发现现在暴露了 15 个单点，在 extrator 这边了。刷新这时候可以看到所有的监控单点了。挑两个端点演示一下。 bins 端点可以展示出当前项目里面所有被 spring 管理的。


Bin。 config props 端点可以展示当前项目的所有配置属性。 matrix 单点可以展示当前项目的运行情况。 matrix 端点自身只是监控项的一个列表，真正的监控端点是 matrix 的子端点。比如构造这样的一个单点，就会展示出当前 g m m 的最大内存。同理，想要查看线程状态，就这样构造其他的单点，同学们可以对照 PPT 里面的表格，花一点时间试试看，都比较的简单。


总而言之， spring boot actuator 可以认为是一个带有一定 spring 特色的监控组件，它比较的强大，也非常的好用。不过就现在而言， x RED 的监控信息都是以 JSON 形式返回的，使用起来其实不是特别方便。下一节我们将来探讨如何将 x RED 的监控数据可视化，让监控信息更加直观。好，这节课就到这里，谢谢大家。




