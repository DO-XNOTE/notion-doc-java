---
title: 1-3 RocketMQ技术架构
---

# 1-3 RocketMQ技术架构

[image](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/9fd06356-4b43-4e5d-9e68-546a7431c98d/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WGWMXN25%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T232220Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDJgqIcRpuip6fl8W%2BthUXlBJGNph4jOkDvhNYKhk1htAIhAKcnLrT1y7WYqHDsUzCl9%2FbC10YiuKZS%2FMR0Ct%2BkIkhfKogECMb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1Igya3S6PuevlwOaqywMq3AOSzUtbV%2F5nLasf3oVXOdVIzIlC734%2BCtpZmkf9CXw404PxOcZmaZH08aCjmXT8GyhWRC%2F%2F4EuU1w%2BO%2Fh1VANa7LMTEtDprPpV3WzxX%2BrpNngPdByGQq1%2BRlLydO99ergNPvfkIm5AeqOVk1%2FyN8Z07HHz2BCYY6%2FQjW1S186d7P%2BGDiyJKV4kU1BWJYP%2B7AT4Bc95EB8Q20sCrGcWGcj7LHH072HUxyTzgGeLX3yxWre9AjOM%2BG26CWRjYY6ojIgeVomUotZiqgPQ7ecw41SQmg02y1xk6qsbeSS87wXCDezwcIqxXpN6lBZBqeKEKgPr6AaBwEmYKT%2BgxyxtQrLu96YJ2sVQws%2F5ZjkajeoU%2B7svQfBOFrFWiWEgd%2FPx7EC2rU1JLN96l1v9f%2BECcyCA3L%2FBPUZ8kSmqqoPMk8lbuXd0%2Fkah7GbRPF4WrYSpWbya%2F6bun%2FkC51q5WjF%2B7GMPcqJ2%2BdVT1daT3gdSFC4b%2BfTwqdtxIXdFUlk7uedXTqxqj3UTDEjQq9KDgslZx%2BtixXof6NCz06K6i1Icz23RL69Lu%2Fiy7M6JZFRfI42nFP%2F4O7nWpF7jQYlfgqyxbBjoBzxb3fv4W38utr6bheKWfqX5R1zYCPfsjYkR8TjCAuP%2FSBjqkASa0ZH7bpWWwoyGUj4EnW1JOkue1go0kGkMib6bVR0dWZQJvsupLSx8tqdTbFylf986XZxc1%2BOkiXoyON2b7ujd8NKKwDUIMbDvfjodA2qJzWwJvsjSjd8w1V5oC168M55TB%2BsnrKZwAQXPGCrr3YvOtkQIpNIbEmF5dSkyxD45dhRGm5uKsPkQaCSzoY%2F0A1RfQ2RN%2BApQ5ExjYsDipJrg%2Bp0OT&X-Amz-Signature=c580336937d7423d5e2bd07c2176b7e3bfcf39db31e87f457962d00c40590553&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

同学们大家好，这章节我们开始学习 Rocketmq 的技术架构。通常我们介绍消息队列，大家更关注的是生产者和消费者，那么大家公安部生产这个消费者的原因，大多数我们同学主要是负责一些业务开发，对于生产和消费，它属于业务系统端的一些处理逻辑，它们都属于消息队列的传统端内容。那么业务上我们使用消息队列最重要的就是我们能通过消息队列完成我们的业务功能，也就是说我们可以把消息发出去，那么消费者我们可以把消息接收到正常业务处理。


在完成业务功能的基础上，我们要学习一下 rock MQ 的工作原理，提高对 rock MQ 的认知。我们学习 rock MQ，现在更关注 rock MQ 作为消息中间件服务端的内容。从这张图里面我们可以看到对于我们生产者集群和消费者集群，他们都是跟我们服务端对应的 rock camera 的集群进行打交道。那么这里面通常我们的业务逻辑作为我们的消息生产方，我们对于消息的业务系统把消息发出去，对于消息的消费方，我们去我们的服务队里面接受消息。那么至于服务端它做了哪些事情，我们其实关注的比较少。


通常我们对于 MQ 集群，它会有我们的比如说个 t seed 中间件来进行维护这个系统，那么或者也有时候对应的 OPS 或 s r e 同学去维护这个 rock m q 它的一些正常运行。通常说对于我们的 rock m q 消息有积压，或者说 rock MQ 它的负载较高，需要进行扩容，那么这些事情通常是不需要我们作为业务方同学关心的。那么这里面我们可以去了解一下 rock m q 它服务端的架构的设计。对于 rock MQ，我们从这里面可以看到它这里有 name Server 集群和我们的 BROKER 集群。其次这里面我们看到了 name Server 集群和 BROKER 集群跟我们生产者，消费者之间的关系。如果大家了解 double 的话，可以这样去对比一下，对于我们的double，它是也有一个对应的注册中心，那么注册中心它会接受我们对于我们的 provider 端和 consumer 端之间的一些应用的注册，那么这里面我们可以看到其实我们生产者或者是消费者，那么真正进行数据传输的过程中，它并不经谓 name server，他们真正的数据传输是直接跟 broker 进行交互的。那么 name Server 做的事情主要也就是一些我们的数据注册以及元数据的一些处理。


对比 double 的RPCDL，我们的 provider 端和 consumer 端都会注册到我们的注册中心，那么这里面也是对于我们的消费者，它的调用不会直接通过 name server，也就是对应的注册中心。我们的消费者集群，它会直接调用我们的provide，那么这里面是我们的 double RPC，它也是消费者直接调我们的生产者，如果说我们基于 MQ 机制的话，我们的生产者和消费者之间它是属于异步传输，这个异步传输的机制中间会集成 BROKER 代理，所以说这称我们对 BROKER 集群也将称为 BROKER 的代理集群。


那么代理集群它做的事情就是生产者发出的消息以后，现在我们的 broker 集群进行存储，[ broker 这里面缓存完信息以后，其实就建立起了生产者和消费者之间一个缓冲地带，那么这个缓冲地带其实也就做到了我们生产者与消费者的系统的关系的解耦，同时也可以做到我们负载均衡和我们的削峰填谷的一个中间件的一个作用。](/05f59d36344e486c9889853acfc258fe)
好，那么现在我们大概了解了 rock m q 它宏观的几个关键点，这里面我们看到 name Server 集群， BROKER 集群以及对应的生产者集群和消费者集群。接下来我们来看一下 name Server 和 BROKER 以及生产者和消费者他们具体做了哪些事情。


首先我们来看一下 name Server，那么 name Server 它称之为命名服务，主要是它是消息主题的一个注册中心。 name Server 它是一个非常简单的一个 topic 的一个注册中心，同时也提供了路由的功能。通常我们接触到的一些支持分布式微服务的一些应用都会依赖注册中心。比如说像 spring Claude，阿里巴巴应用的依赖 Nicos 作为注册中心，那么常规的 spring Claude 它会依赖 Europe 或 cancel 作为注册中心。


name Server 的角色我们刚才也介绍它可以理解为 double 中的ZK，支持 broker 的动态注册与发现。也就是说，我们 name Server，它作为注册中心，它可以接受 broker 的注册，也可以接受 provider 和 consumer 的注册。简单来说， name Server 它主要包含两个功能，一个是 BROKER 的管理和路由信息管理。


BROKER 管理是指 name Server，它接受 BROKER 集群的注册信息，并且保存下来，作为我们路由信息的一些基本数据，然后提供心跳检测机子检查我们的 broker 是否还存活。那路由信息管理是指这里面的每个 name server，它都会保存博客集群的整个路由信息，主要是用于客户端来查询我们的队列信息，这样的话， producer 和 consumer 它通过 name Server 就可以知道整个播客机群的一些路由信息，从而进行消息的一些投递和消费。


name Server 通常也是集群的方式部署，只是它这里面各个实例的节点，它们的信息并不只有互相通讯。这一点跟我们了解的大多数的注册中心实现方案是不一样的。通常的注册中心，它会保证每个节点数据的最终一致性。我们参考AK， Eurocarnicos 这些常见的注册中心实现。无论是 ZK 的 CP 模式或者是 urack 的 AP 模式，我们从注册中心的任意一个节点获取的信息都可以理解为是一致的。那么 name Server 它做到各个实例之间不进行业务数据的通讯，它主要是为了保持注册中心，实现逻辑简单。


那么这里面其实我建议，如果说我们的 rock MQ，他拿 Nicos 作为注册中心其实也是可取的，也许后面的话， Nicos 和我们的 rock MQ 进行一个整合的过程中，可以做一些这方面的事情。如果说我们的 name Server 之间不进行互相通讯，它又是如何做到数据的一致性的？这里面是我们的broker，它会向每一台 name Server 都注册自己的路由信息，所以每一个 name Server 的实例都保存一份完整的路由信息。如果说某个 name Server 因某种原因下线了， broker 依然可以向其他的一些 name Server 同步一些路由信息。所以像 producer consumer，它仍然可以动态地去感知 BROKER 路由的一些信息。那么这是 name Server 的命名服务。


接下来我们看一下 BROKER Server。我们作为代理服务 BROKER Server，它主要负责我们消息的存储、投递、查询以及服务高可用的保障。这也是 rock MQ 最复杂的部分。 BROKER Server 对消息的处理是 rock MQ 的核心。为了实现这些功能， broker 又划分了几个重要的子模块儿，这里面有 remoting model 和我们的 client manager，以及 store service 以及 SA service 和我们的 index service 这几个模块儿。首先是 remote model，它是整个 broker 的实体，它负责处理来自 client 端的一些请求，那么 client manager 比较容易理解，它是负责管理客户端，这里面包括 producer 和consumer，来维护 consumer 的 topic 的订阅信息。对于 store service，它主要是提供简单的 API 接口，处理消息存储到物理磁盘和我们的一些查询的一些功能。


IC service，它主要是做高可用的服务，提供我们的 master BROKER 和 Thrift BROKER 之间的一些数据同步的功能。对于 index service，它会根据特定的 message k 对投递到 BROKER 的消息进行一些索引服务，以提供消息的一个快速查询的功能。这是我们对于 broker 的一些简单的介绍。


producer，consumer，它都是消息队列的用户，也就是我们对应的 client 端producer，它负责发送消息， consumer 负责接收消息。producer，它定位于我们消息发布的角色，支持分布式集群。胖子部署Audio，它通过 MQ 的负载均衡模块选择相应的 BROKER 集群队列进行消息投递的过程，它可以支持快速失败模式，整体控制消息低延迟响应。那么对于consumer，它作为我们消息消费的角色，它也支持分布式集群方式部署，它可以支持 POS 的推模式，也支持 pool 两种模式对消息进行消费，同时也支持集群方式的或广播方式的消费。这里面它提供实时消息的订阅机制，能满足大多数用户的需求。


接下来我们来看一下 rock MQ 各个主键的一些部署结构，这里面我们可以看到，这里面是我们 name Server 的集群，这是我们 broker 的集群，对应我们生产的 producer 的集群和我们的 consumer 的集群。从这里面可以看到，对于我们的 name Server，它是一个几乎无状态的一个节点。这里面为什么用几乎无状态节点？它主要为了描述我们的业务信息，不进行交互，但其他还是有一部分心情是有一些关联的。这么对于我们的内容 Server 进行，虽然说是集群部署，但是每一个节点我们可以理解为是独立的，他们节点之间不会进行我们已有数据的交互。


那么我们来看一下 BROKER 集群，对于 BROKER 集群的部署会比较复杂一些， BROKER 通常它对于每个集群，我们对一个 BROKER 主题，它会分为 master 和slave。比如说我们看这里面是对应的我们的 broker MASTER 一，我们的 broker slave 一，这里面还有对应的 broker MASTER 2 和 broker slave 2，那么对于一个 master 的人，它可以对应多个slave，也可以有对应的 slave 2， slave 3 等等这样一个操作。这里面主要是为了说明我们的一个对应的 broker name 指定的名称，它只能有一个master，那么这个 master 下面会有指定多个slave。


这个 slave 和 master 我们可以理解为是一对多的关系，也就是说 slaver 它只能指向相对应的一个master，那么 master 下面可以指定多个slave，那么对于多个 slave 节点它也有区分。这里面通常我们的 master 节点它会定义为第零个节点，我们的 slave 有对应的 1234 这样一个节点的区分，我们通过这里面的 broker ID 去区分哪个是master，哪个是第一个 slave 节点。


这里面为什么要区分第一个 slave 节点？是因为通常我们集群在部署的过程中实际上有多个 slave 节点，那么也只有我们的第一个 slave 节点会提供我们的数据传输的服务，那么其他 slave 节点只是用来做一个数据备份。那我们了解了，一个 master 可以对应多个slave，一个 slave 只能对应一个master，那么 master 与 slave 的对应关系是如何确定的？对于相同的一个集群的小集，我们可以理为小集群，它的 master 与 slave 的对应关系是通过我们相同的 broker name 来区分的。


对于相同的 BROKER name，我们可以理解为它是一个小的 BROKER 集群，记取它的是 master 和slave，它是通过 broker ID 来定义 broker ID 为0，那么也就是我们 broker 的第一个节点表示为master，非0，它表示slave。那么 Mustin 可以部署多个。每一个 broker 与 name Server 集群中所有的节点都会建立长连接定词注册 topic 信息到所有的 name Server。这里面有一点我们刚才也介绍到我们现在的 rock MQ 的版本，在部署架构上，它会支持一个 master 和多个slave，但是也只有我们的第二个 broker 节点，也就是 slave 的第一个节点就是 broker ID 等于一的这个broker，它才会从服务器参与消息的一些读的负载。


那么接下来我们来看producer，它会与我们 name Server 集群中的一个节点进行链接，那么这里面要区分一下我们的BROKER，每一个 BROKER 它会跟我们 name Server 的所有的节点进行长连接。我们的 production 它只会随机地去选择我们 name Server 其中的一个，建立长连接，那么这个连接会定期的通过 name Server 获取我们的 topic 路由信息，并且 production 定期的向 name Server 汇报自己的心跳状态，保持自己一个在线的状态。


对于 producer 它是我们业务系统的各个节点的部署，那么我们各个业务系统通常我们的应用系统的实现，它是完全无状态的，可以我们的集群进行一个扩展部署，那么这样一个过程，那么我们来看consumer， consumer 在一方面跟我们的 producer 是类似的，那么 consumer 它也会选择我们 name Server 集群里面的一个节点进行一个建立长链接。


那么这个选择的方式我们可以理解为是一个随机的选择，它也是定期的冲我们 name Server 获取我们的 topic 路由信息，并向我们的 topic 服务的 master slaver 建立一些长链接，并且同时定时向 master slave，它会发生定期心跳，那么 consumer 它既可以从 master 订阅路由信息，也可以从 slaver 订阅信息。


那么消费者在马斯尔拉取消息的过程中，马斯尔服务器会根据我们的移动的偏移量和最大偏移量的距离来判断是否读取老消息。这里面如果说需要消费我们消息内容的话，就会产生 IO 进行我们的消息消费，同时它也会冲服务器 4 伏可读等因素来去判断。我们下一次去获取消息的过程中给予一个建议，就是建议我们的消息是从 master 获取还是从 slave 获取，这时我们可以理解为对于 rock MQ 这些具体的这些各个节点他们处理的一些逻辑。那么接下来我们来看一下对于 rock MQ 指各个组件部署的它的一些流工作流程的过程，那么我们首先会启动 name Server， name Server 启动完成以后，它会等待BROKER，producer， consumer 进行注册。那么接下来我们来启动我们的 BROKER Server，它会与所有的 name Server 保持长连接。刚才我们已经介绍到了，这样的话，我们保证虽然 name Server 的之间不进行通信，但它可以获取到我们所有的 BROKER Server 的信息。


那么接下来对于我们的 name Server 和 BROKER 都启动完成以后，我们可以启动我们的客户端对应的 producer 和consumer，它是跟 name Server 中间的一个节点保持一个长连接的一个过程，那么我们从 rock m 官方的一个架构图的启动过程来进行一个描述，这里面我们看第一步我们的 name Server 的启动，那么 name Server 启动过程，我们这里面涉及到多个 name Server，那么我们进行 name Server 集群的启动部署，那么 name Server 启动部署完成以后，我们就应该我们的 broker 进行部署。
那么 broker 启动它会跟我们所有的 name Server 保持一个长链接，定时发送我们的心跳包中，它会包含我们 broker 的一些信息，这里面最常用的像都有区分度的就是我们的 IP 和端口，以及存储所有的一个 topic 信息，这里面注册成功以后， name Server 集群就有 topic 跟 broker 的一个映射关系了，这里面我们看我们的 broker 启动完成以后，第三步这里面有一个 create topic，那么这个并不是必须的，我们也可以在发送消息的时候去创建这个topic。


那么我们接下来看我们应该是 producer 的启动，那么 producer 在启动的过程中，它也是跟我们的 name Server，这里面会选择一个节点进行一个长链接的构建，这样它可以获取到我们跟 broker topic 相关的一些信息。


得到了这些 topic 的一些路由映射以后，我们 producer 它在发送信息的过程中，它可以获取我们对应的 topic 信息发送到哪个 broker 上，同时也可以轮询的从队列里面选择一个队列，然后与队列 broker 建立长链接，进行我们的 broker 信息的一个发送，那么 consumer 这块跟 producer 也是类似，它会跟其中的一个 name Server 建立长链接。


那么获取我们订阅的 topic 信息存储在哪个broker，然后直接跟 broker 直接建立链接通道，开始消费信息。现在我们了解了 rock MQ 部署过程中各个模块之间的交互方式，同时也初步了解了 rock MQ 的技术架构。我们这章节的内容就先介绍到这里，同学们，我们下一章节再见。

