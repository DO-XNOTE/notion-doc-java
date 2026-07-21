---
title: 2-17 RabbitMQ与SpringBoot整合_消费端-2
---

# 2-17 RabbitMQ与SpringBoot整合_消费端-2

[image](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/ab65abde-624e-46e2-bc41-0bba96d082a0/SCR-20240806-nynn.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466Z4CT2HHE%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T225254Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIGg7YBn0d2%2Fya5xsVFlZ%2B9zSpYGJDDXXNavVbN8tXvBPAiAyWluA4iYL8eW3TJNmA0Z0XzvToBeTYqbDcSFdOY4ItyqIBAjG%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMAOoXDd4Can5El%2FULKtwD3s1okhNWKxOsDTGePIcnEx50ZiZ5ZK9WmSe4i1F2KP37y8isW4L%2BL0teyKVWsYVXKsaMfJUC65uECYr0OUF%2BbvC36siMPpa8R4KFR5m9QPMy9wtl9uO1EBG1pvuWY8tfOHXhlerJ6hphsCM1C987BAiWflDuohwWeGTCn1OGgDBUehoFP2ITzjw%2FSWij90ELQFV9kvkIon8WU3NKEkGeg1W2p8xJzQnulOCU4b2ch0Birk%2F1qLNMe49xvsgDOzoigsm771wNdI1YeXmzAIApW%2BJtFT03lsFvuf6BePnXdW%2BkW%2FDwx5Mf28gvMa4sHKoZEoQq8CfzZ5KaDqxx0dL7kFYNIyWole9mdLRe0N%2F9NQl3VEUCmlRPjOLB2%2B8uxLcAhMO5nizNGuwZX8lFxeXESnuJRMeVI4EKmvFShjE8gIYmkLKwgHE%2FZv6WKjW0kEeqtyKk0iY39f%2Fgi1c6%2Bucfa7eLH%2BKwBlFg7V7%2B4Ty0NbdD20f2EOMytQTPqjpFcu60TQumv3OCv6T1UIiQvfWiTV67PoBHsp0qOgIhxGTgby8rMO0HqYFeoyKMWO8WCZUVqU0cjvyWQSf1H6o57IVxyGXLlMMTtq%2Fk79T5lnymXQy9Pd6T%2BSvMJ9KYNwIwr7f%2F0gY6pgGQNxergZd3T5OSvAlwJMLrn1WbjKrR1AU6T9t5FvMucf3zIn%2Fx2nyJ3FKMWMiB3dTU1Ckpsw%2BiAr8QnOziapfT8kAzSMwQ2A12qHByRvNG8Sn3GCbtuvprMQTMu%2BaStp93pDj6r5uTM%2BY02jzkf462p320VlqBzJqncAjIp7TJDMjVDXPkj3YlvMxj%2BfPuKFx0ZQJ2F65z7DgWr%2FawNewPKddQMoLL&X-Amz-Signature=45cd3c44a7266f78e16f83178353a77a577a24f4d80312dfacd9dab92f46d080&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

[image](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/f7d65204-f2fa-4ad0-b236-876d74871153/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466Z4CT2HHE%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T225254Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIGg7YBn0d2%2Fya5xsVFlZ%2B9zSpYGJDDXXNavVbN8tXvBPAiAyWluA4iYL8eW3TJNmA0Z0XzvToBeTYqbDcSFdOY4ItyqIBAjG%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMAOoXDd4Can5El%2FULKtwD3s1okhNWKxOsDTGePIcnEx50ZiZ5ZK9WmSe4i1F2KP37y8isW4L%2BL0teyKVWsYVXKsaMfJUC65uECYr0OUF%2BbvC36siMPpa8R4KFR5m9QPMy9wtl9uO1EBG1pvuWY8tfOHXhlerJ6hphsCM1C987BAiWflDuohwWeGTCn1OGgDBUehoFP2ITzjw%2FSWij90ELQFV9kvkIon8WU3NKEkGeg1W2p8xJzQnulOCU4b2ch0Birk%2F1qLNMe49xvsgDOzoigsm771wNdI1YeXmzAIApW%2BJtFT03lsFvuf6BePnXdW%2BkW%2FDwx5Mf28gvMa4sHKoZEoQq8CfzZ5KaDqxx0dL7kFYNIyWole9mdLRe0N%2F9NQl3VEUCmlRPjOLB2%2B8uxLcAhMO5nizNGuwZX8lFxeXESnuJRMeVI4EKmvFShjE8gIYmkLKwgHE%2FZv6WKjW0kEeqtyKk0iY39f%2Fgi1c6%2Bucfa7eLH%2BKwBlFg7V7%2B4Ty0NbdD20f2EOMytQTPqjpFcu60TQumv3OCv6T1UIiQvfWiTV67PoBHsp0qOgIhxGTgby8rMO0HqYFeoyKMWO8WCZUVqU0cjvyWQSf1H6o57IVxyGXLlMMTtq%2Fk79T5lnymXQy9Pd6T%2BSvMJ9KYNwIwr7f%2F0gY6pgGQNxergZd3T5OSvAlwJMLrn1WbjKrR1AU6T9t5FvMucf3zIn%2Fx2nyJ3FKMWMiB3dTU1Ckpsw%2BiAr8QnOziapfT8kAzSMwQ2A12qHByRvNG8Sn3GCbtuvprMQTMu%2BaStp93pDj6r5uTM%2BY02jzkf462p320VlqBzJqncAjIp7TJDMjVDXPkj3YlvMxj%2BfPuKFx0ZQJ2F65z7DgWr%2FawNewPKddQMoLL&X-Amz-Signature=094aa4409e840d50118124858bacec06ff0ee39aaf75b78f2fe90e84c7e0b4cd&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

好了，消费者的部分代码编写完了，然后我们做什么事情呢？接下来我们就要对他们做一个实验了，我们现在可以把这个 consumer 先提起来，看看能不能起来。不过在启动之前，我们先来想一个问题，就是说我们之前在雷斯那里面配置的什么 pin 杠1，然后什么exchange，包括他们之间的绑定关系 key 这些是不会帮我们去做一个设置。我们来考虑这个问题，那我们先在这之前先看一下 rap m q 的控制台， F5 刷新一下，好，没问题。现在默认里边是有 8 个exchange，然后没有任何队列。这 8 个 exchange 我们看到都是以点 AMQ 开头的，这是它默认自带的。也就是说我们现在控制台里边并没有任何exchange，也没有任何队列，并且更没有任何绑定关系了。那接下来我们来看一看我们怎么去做，现在就把它提起来吧，看一下我们把 consumer 提起来。

A screw put application.


我们来起一下，对应着已经起来了，看见了吗？ 8002 端口，这是没有问题的。起来之后我们再回到这个 cancel 控制台，你会看到这个 cancel 控制台已经多了一个 King 1 这个队列了，然后它是 h a 杠2。这什么呀？这就是镜像队列的方式，老师现在搭建这个集群就是一个镜像队列的集群。然后我们现在来看一下应该怎么去做。


这个 exchange 已经有了 exchange 杠1，那么它们之间有没有什么绑定的这个关系？我们点进去，你看一下 boundness 里边已经有一个绑定关系了，我们当前的这个 exchange 1，然后它跟我们的 GIN 1 做一个绑定，它的 routine key 是 spring boot 点星，也就是说只要匹配 spring boot 点后面可以吃任何东西的，都会帮我们去路由到。就你一发到这个 exchange 的消息，它会帮我们去路由到。这个 pin 1 这个队列，只要你匹配这个固定 key 的规则就可以了。好了，那这证明是完全没问题的。然后我们看到，唉，还有什么变化？我们其实一定要仔细的去观察，我们观察什么呀？我们刚才观察的是 exchange 跟队列，包括之间他们的这个绑定关系，以及节点的这个 NO 的模式。


现在我们来看overview， overview 里面有一个connection，就有一个连接，这个连接是什么？幺九二点幺六八点幺点二，这是我可能说我自己的本机，然后 user name 是guest，是我们自己的访客，然后使用的是 a m q p 协议channels，看见了就这个连接里边有 5 个channels。

为什么有 5 个channels？除了有 5 个channels，你对应着还有什么呀？ 5 个consumer，当然这个是没法点的，那我们可以看一下我们的 connection 4，你只能从这点，从这点看到 5 个什么呀？ 5 个channel，然后你点进 channel 之后，你会看到 channel 对应的consumers，就是每一个 channel 对应的一个consumers。然后现在就证明我现在是 OK 的，完全没问题，我们的消费端代码已经搞定了。


好了，那消费端已经起来了，那接下来的事情是什么呢？接下来的事情就是我们要对生产端做一个test，做一个测试。好，生产端我们要做一个发消息的这个 test 测试，那我们直接去 new 一个测试类，在这里我们叫 COM 点 BF x y，点儿rabbit，点儿producer，点儿test。OK，好了，然后我们创建一个测试类，咱们叫做 application test applification tests，好了，按照我们正常的一样的，然后这个 run with 是不是 run with？就是 spring 什么 banner 加class，然后接下来就是写你的斯克多的test，注解好了，搞定这个东西，我们先做一个什么事啊？是不是直接可以去奥特维尔的什么呀？我们Rabbit，我们写的是 Rabbit 什么 sander 那个类，然后我们把它引进来，直接就可以用。然后我们直接艾特test，做一个 unit 单元测试哈贝克，然后这个单元测试一般肯定都是 y 的，然后我们的 test Thunder，然后这里面我们 through ex 撇他一起来问好了。那我们看看怎么去发消息的代码呢？其实就调用这个 send 方法， send 方法传两个参数，一个是practice，还有一个是真正的这个message，真正这个 message 你可以随便传啥都行，比如说我们就传一个字符串就可以了，无所谓的就是 hello Rabbit QQ 好就写完了。


然后这个 practice 呢是一个map，我们把这个 map 搞一下，这个 map 就是我们 Java 的 util map，它是string，然后这是object，然后我们叫 Pro practice，等于 new 一个 practice map 好， practice OK，哈希map。


接下来我们对这个属性做一个填充，比如说我们 put 一个参数，咱们叫做 a t r e，然后这个里边我们可以写12345，然后我们再来一个 a t r 2 点 put a t r 2，然后这个写成a， b c d e 好了，搞定非常简单。然后其实我们就可以做一个 test 测试了。


注意还有一个问题，就是你发消息你要发到哪？是不是你都不知道发到哪？你没跟我们说，你只是说把，这个 send 方法包装了一下，点进去的时候，然后在这里边你说卡沃尔特 send 什么？exchange，然后包括它对应的什么呀？就是 exchange 以及 routine key，我现在是这样去封装的，那其实更好的方式你应该把这个东西暴露出去。


你比如说在构造 message 的时候，因为它是一个object，你是不是可以自己自定义？比如说这个 message 既然是一个object，你是不是可以把这个 exchange 这个属性封装到这个 object 里边？因为你这样去散的你非常不灵活，相当于你所有的 send 消息都是固定死了往这个 exchange 里send。但是如果你说你把这个属性给它变成这个 object 里边的一个其中一个属性，那我可以根据这个 message 里边的那个属性去判断我把它发到哪里。


那当然我们现在做的是一个小的 hello world 的这个示例，就是跟 spring boot 如何整合，所以说你不用 care 这个事情，后面我们去讲这个基础架构，就是 MQ 的这么一个封装的时候，老师会跟着大家从 0 到 1 的把这个 rap MQ，它的比如说可靠性投递，还有一些核心的一些东西去做一个完整的封装，包括蓄力化等等很多。OK，那我们现在先不用看有什么事情，大家知道这个事就好了。那我们现在其实做一个消息发送是不是就可以了？当然在这里我期望你可以做一个停顿，比如说 thread 点sleep，你可以休眠个 10 秒钟。好，我们去做一次发送。


我现在 consumer 是起着的， 8002 是起着的，8001，我们现在要准备开启了做这个单元测试， 801 肯定也起来了，单元测试去发这个消息，好，同学们请看哈， 10 秒钟之后他才会把这个停止掉。所以说你看测试成功，唉，同学们请看，发现一个问题，什么问题？我们生产端做了什么事情？生产端他打印了一句话，叫做 post to do。 post to do 在哪里？还记得吗？我们最开始说，当我们消息发送完之后，它会执行一个什么？它会执行这个回调函数，就是消息只要发送完了之后，因为它是一个同步的，所以说它会等着那个线程阻塞，它执行完了之后，它才会认为消息发送完了，然后他才会。


给你做一个什么？ host to do 这么一句话就是消息发送完了，但是具体的这个 config 我们现在还没写这块，其实我们可以做一个什么呀？再打印一句话，叫做消息 a C k，然后结果是什么呀？结果就是我们 a C k 它到底是 true 还是false？然后 calculation 是不是calculation？其实我们也可以打印一下，直接加上座号，加上这个calculation，点它有个 get ID，然后如果 a C k 是 false 的话，肯定会有这个cost，对吧？我们先不用去考虑，现在肯定是正确的。


好了，这是关于消息的生产者，你会发现它执行完成之后，刚才已经把这个 POS 速度已经打印了，就是我们发送之后打印了。然后最开始的时候我们的 consumer 是不是一直消费消息？ hello y m q 是不是把它 play load 里边的消息已经取到了，因为消费消息已经打印了，消费消息就是我们刚才所看到的。什么呀？编码的时候，对于消费者看一下consumer，消费者的时候你会看到他有一句话，就是消费消息，消费消息，然后把 play load 打印一下，然后在这之前打一堆横杠好了。然后 ACK 了，没有看控制台里边，对于 pin 它没有任何什么total，包括这个 n check， n c k read，那就说明他已经帮你去 ACK 了，这是没问题的。


那我们再来一条消息，我们首先尝试着把 consumer 先停掉，看我现在把 consumer 先停掉。 consumer 停掉之后，然后我们做一件事情，就是发一条消息，这回发消息，注意，我这回发消息 ACK 有结果了，打印我们再测试一下，看看消息发没发成功。你看为什么我要在这睡眠 10 秒钟？我就是想看到这个效果，看到他 post 做了，并且 ACK 这个结果也有了。


a C k 就是我们之前回送的那个 u v i d，在之前我们发送的时候，在这个 send 方法里边已经生成了一个 u v i d 了，看到了，就在这后面已经生成 u i d 了，回来的时候又来一个UID，是不是？这个UID？肯定，但是只不过我没打印，但他们两个肯定是一致的，就证明我们博客收到消息并给我们生产端的那个监听，就是 call back，我们刚才写的这个 confirm call back，所以送的这个ACK，并且这个 ACK 的结果是数就表示成功。


那现在我们来观察一下我们的控制台，你看有一条 ready 已经准备好的消息，然后unchecked，那这一条消息是什么情况？是还没有被消费。好了，那没有被消费，我们来看一看我们的consumer，我们把这个先关掉。哈，我们就单纯的去看consumer，我现在把这个最后的这一行我给它注释掉，就让他不去帮我们去 a C k，如果不 a C k 的话，它会有什么结果？来看一下，我们来启动一下，如果你不去做 a C k 的话，消费消息。唉，这事也打印了，但是你没有 a C k。


我们的控制台里边看见了这里边，它就是说unchecked，它从 ready 的状态就变成 Uncheck 的状态，就说明什么呢？就说明我消息发出去了，但是你没有给我做 a C k，它就是处于这种状态，那他需要去要 a C k，能理解我说意思，所以说我把它停掉，然后我再把它放开。


好，同学们，你看这回呢？又把这个消费消息的这个 hello word 又消费了一遍之后，同学们，你这次再看见了吗？刚才 total 是有一条消息，然后状态是 uncheck 的状态，然后当你的消费端又起来之后，它是不是相对来讲，它会把那条之前没有消费成功就没有得到 ACK 的那条消息，它会再帮你去重新推一遍？也就是说消费端会保证，如果我没有收到 a C、 k 的消息，我肯定不会删，我肯定会帮你再重新推过去。


这就是我们消费端 broker 端做的一个可靠性的这么一个事儿，跟消费端他自己。所以说一般而言，我们做 MQ 的可靠性投递，你只需要做生产端跟布洛克的可靠性就好了。至于说布鲁克跟消费端， MQ 自己会帮你去做，任何 MQ 基本上都满足了。这事儿咱们就是说卡夫卡他也能够做这个事情， Rocketmq 更不用说了， Rocketmq 还有消息，各种各样的城市策略 rap MQ 刚才我们看到了也可以去做，相当于这两节课老师在这里就把我们 Rabbit MQ 跟我们 spring boot 如何去进行整合？然后里边有一些结合控制台，还有一些细节的问题在这里跟小伙伴们一起去讲清楚，那么这节课就到这感谢小伙伴们。


