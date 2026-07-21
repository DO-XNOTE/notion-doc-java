---
title: 3-23 可靠性消息最终演示
---

# 3-23 可靠性消息最终演示

[image](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/847b8911-a06c-470b-a0cd-072fd928b67c/SCR-20240807-fgqr.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664O5YPOPN%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T225315Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIAMBKgLUBOQ%2BJ1t%2B1dQRAkh83nOmx5IRmJhb%2BaU0SQ%2BbAiADbu5YvofY8y4ccIREno6dY67XIaNlZjF0cZshi0lI9iqIBAjG%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMYAJ9UF3EJOpTzMUzKtwDm6GWHmH8td4%2FVlO%2B2MrcdRYPNnqO16aHTdDQkE5HmBB2cY%2BvAz1Ijz667KqFh5H9FuZyV1dXgceRBJiiWOP59ujt2oPQ8QXObXOP5v%2FV5eKVYsCuvXEIw0LvcpECW%2Fi7Tp7MmnzXIG%2BMKfke19uuUCjGb%2BToRQAwB461mZe5nrQ%2FbqPqOthQ4VW9yc%2BHq4z3hoXOJWIGAwaKIgPlsJKMpH19nIUC7GjL%2FoBtAnPWd7H8PWKCBRme4AdUbZey%2Bez1eJl4gzQjJmdTUL3IOAVdY7VGaG57NqgIll0Rn8mivP7KjZmxmYAge8adxjoV17JY4KxSo9B00DXRGXaqoJ7v6EBGHjPFwBZpyadY2zEGpfFU5OKD9aA6T2q3zCe2V9DwfM98hkyrU2HjEulhs1rQxJaTuumE%2Faj2Bu46b8jvbPAiW6iv%2F46FkSomXS5RaOBhSew%2B%2BkNwXl11UyLAnj0NArsPt3eQFydilrZbrHubehPgqed4V5pkyRWbKSvD6SX%2F%2F0SajxcVgQtRSddvMeB2jqbBUReEOFAy6hohqHvoClSM6tYUKdLZS%2BQm75FxarwJVuOR98z5WlO7pVrDUXj7MIRXxlYHAHB5DIEog%2Bco3j21Ml6h5%2BKrvldzWJkwy7f%2F0gY6pgGWWQ2eWdinzvv%2F6zcKn8UXIP81odeqOEbxpi03VJ6CTfYMem0VczNChP85539BckmwmXEdg%2Bwz4g0pobCfs7vdZS5rovi5qYzw7u5tGrw26qnMX%2BY9ZUpmHKdd%2FiQvYQ9OPQuqgotfxbhZXyGYBcBtEPXV9zXkcdZuRPD85ulUT4Fh9MKY858othAUcuSlrjN%2F2NySP5QsDaZ4f1nC4itQUIkwvq3r&X-Amz-Signature=059960d31c23b713c56681cf699c55375f38d8e5bdadcf835906beff33e74d42&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

[image](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/f1d89ec6-a39b-49f6-8873-c0083c1e29e0/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664O5YPOPN%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T225315Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIAMBKgLUBOQ%2BJ1t%2B1dQRAkh83nOmx5IRmJhb%2BaU0SQ%2BbAiADbu5YvofY8y4ccIREno6dY67XIaNlZjF0cZshi0lI9iqIBAjG%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMYAJ9UF3EJOpTzMUzKtwDm6GWHmH8td4%2FVlO%2B2MrcdRYPNnqO16aHTdDQkE5HmBB2cY%2BvAz1Ijz667KqFh5H9FuZyV1dXgceRBJiiWOP59ujt2oPQ8QXObXOP5v%2FV5eKVYsCuvXEIw0LvcpECW%2Fi7Tp7MmnzXIG%2BMKfke19uuUCjGb%2BToRQAwB461mZe5nrQ%2FbqPqOthQ4VW9yc%2BHq4z3hoXOJWIGAwaKIgPlsJKMpH19nIUC7GjL%2FoBtAnPWd7H8PWKCBRme4AdUbZey%2Bez1eJl4gzQjJmdTUL3IOAVdY7VGaG57NqgIll0Rn8mivP7KjZmxmYAge8adxjoV17JY4KxSo9B00DXRGXaqoJ7v6EBGHjPFwBZpyadY2zEGpfFU5OKD9aA6T2q3zCe2V9DwfM98hkyrU2HjEulhs1rQxJaTuumE%2Faj2Bu46b8jvbPAiW6iv%2F46FkSomXS5RaOBhSew%2B%2BkNwXl11UyLAnj0NArsPt3eQFydilrZbrHubehPgqed4V5pkyRWbKSvD6SX%2F%2F0SajxcVgQtRSddvMeB2jqbBUReEOFAy6hohqHvoClSM6tYUKdLZS%2BQm75FxarwJVuOR98z5WlO7pVrDUXj7MIRXxlYHAHB5DIEog%2Bco3j21Ml6h5%2BKrvldzWJkwy7f%2F0gY6pgGWWQ2eWdinzvv%2F6zcKn8UXIP81odeqOEbxpi03VJ6CTfYMem0VczNChP85539BckmwmXEdg%2Bwz4g0pobCfs7vdZS5rovi5qYzw7u5tGrw26qnMX%2BY9ZUpmHKdd%2FiQvYQ9OPQuqgotfxbhZXyGYBcBtEPXV9zXkcdZuRPD85ulUT4Fh9MKY858othAUcuSlrjN%2F2NySP5QsDaZ4f1nC4itQUIkwvq3r&X-Amz-Signature=e84d018438bd65f8d3fd872e5352a79b81b6df55879f1b196048eead9bea4ac1&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

那这节课我们做一个实验，就是说我们针对于上面的这个可靠性投递这块，整个的组件差不多已经封装完了 90% 了，还差一些细节，那我们下节课再说，那我们来先看一看能不能去做到，我们要的效果就是可靠性投递。老师在这里已经写好了一个简单的工程，用于这节课的测试。


首先我们来看一下这个叫做 Rabbit 杠test，我们来看一下，首先它的这个 Pom 文件我们来简单阅读一下，那我们现在用的是 spring boot 的二点一点五这个 release 版本，接下来我引入了三个dependency，两个都是关于 spring boot 的 starter web，还有一个是 starter test 去做单元测试的。最后一个就引入了我们刚才封装的这个 Rabbit call 和 user 只需要引入这一个包就可以了，然后我们来看一看它能不能帮我们去发送消息。


那我们后文件读完了之后，我们来看一下整体的代码，非常简单，首先就是application，就是这个启动类慢config，就是我们配置一下它的 component scan，接下来我们去看一下它的这个配置文件。来我们打开注意一下，首先它的端口是8001，然后它跟 rap MQ 只建立的连接就是幺九二点幺六八点幺幺点七幺，一直到73，就是我们之前做 spring boot 整合 rap MQ 所配置的这个地址。


上面这些东西都没什么可说的，最后这两个东西看见了，就是我们需要自己封装 ES job 那个基础组件要这两个比较关键的参数，一个是 server list，还有一个是我们的这个 name space，OK，这些事情都搞定了以后，那么我们就可以去做可靠性了。


老师呢？现在这个 rapid MQ 已经启动了，就整个 rapid MQ 的集群已经启动了，当前它有一个对应的 exchange 叫做 exchange 1，然后这个 exchange 1 所绑定的队列就是叫做 Queen 1，它们之间的这个路由key，你其实可以点进去看一下路由key，就是说当前我的 this exchange，它 routine key 就是我们的这个 spring boot 点星，然后绑定到 key 1 这个队列 key 1 这个队列里边没有任何数据，因为它的这个数据都是0。接下来我们就可以去做实验了。那怎么去做？在这里老师写了一个test，就是一个吉尼 test 的一个类，那我们来看一下，首先直接把我们 com 点 b f、 x y。

The rabbits that produce their brocade are.


叫做 producer client 直接引进来看了吗？直接就引进来这个 producer client 就可以了，因为这个 producer 之前已经帮我去做实体化了，对不对？怎么去做实体化呢？你可以看一下我们的producer，你看到这个 producer 他是怎么去做实例化的？在我们的 producer client 里边，我直接是艾特component，直接艾特 component 帮我去加载到 spring 中了。


那有同学说老师这个东西他怎么去读到这个文件的呀？就是在这里，是不是在我们的这个 auto configuration 的时候， Rabbit produce auto configuration 的时候，我已经指定了component，让他再帮我去扫描这个包下面所有的内容，对不对？好了。然后这样的话，也就是说整个我的 call producer 里边所有的类都被 spring 去管理了，因为你看我的这个 producer client 也好，还是我们的这个 message store service 也好，都是加上了我们的 spring 的这个注解了，让容器帮我们去管理。


那有人说老师那这样去做好吗？这样去做，说实话如果你是作为一个基础组件去做的话，这么去做是不太合适的，你最好怎么办？你最好在这个里边全都去以艾特病的方式去帮我生成。然后这个类里边我在这里举个简单例子，比如说我们知道它是吧？那这个 rabbit broker，它的 implements 肯定也是艾特component，对不对？那也就是说我现在想做什么事情？我现在想要这些全部是 out to where 的方式，就是说你认为这个注解是没有的情况下，你怎么去做？那你肯定都是得要艾特 bin 的方式，把具体的 public 我们的这个 producer client 是不是？然后呢？我还得 new 出来一个 producer client 等于 return new 一个 producer client。


好，你得这样去写，然后这个去小写，这样的话你这么写难道说就可以把这个 component 去掉吗？不是的，因为什么呢？因为你这里边 out to where 的， out to where 的你必须得用一个构造方法，相当于你必须有一个 public 构造方法，然后把这个传进来，这样去做 this 点什么 produce 等于你这样去写，同学们，然后在这里边你在初始他之前你先得把什么呢？你先得把刚才我给你们看的对应的这个 Rabbit broker 也要去做艾特病的方式，在这里我就不演示了，我是跟大家说一下应该怎么去做。


这个其实课下留给我们小伙伴去当成一个小的作业去把它搞定，老师在这里直接就用 at 可能 scan 方式把下面的包都扫描了，所以说这个里边他是 OK 的，他也是 OK 的，对不对？那我其实在这里给小伙伴留一个作业了，这个小任务就是说所有艾特 service 帮我们去管理的地方，都统一放到我们的这个 rabbit producer auto consideration 这个类，下面你艾特 bin 的方式帮我去管理，而不是说用这种方式去扫描，那这种其实是更优雅一些，个人觉得。


好了，那我们看完了这块之后，就是证明我们现在直接可以去用，叫做 produce client 直接 out where 住进来，对吧？那直接注入进来之后，我们去调这个 test 方法，然后去发一条消息，我自己 generate 一个UID，这个 UID 是我自己生成的，看见了这个UID，我这样放进去，然后 exchange 我们就叫 exchange e roading key 就叫做 spring boot 点ABC，然后 attributes 我就加一些其他参数。


这个参数还记得吗？这个参数是什么？你看一下最后一个参数，相当于它就是延迟的这个参数消息延迟参数，这个我们后面再去做，最后把它发出去，假设你设置延迟 5 秒的，但是现在没有意义，因为你没有去做延迟的一些相关的内容。那接下来我们发的消息是什么消息？你只需要在 message 上去设置你的这个relight，就是我们的可靠性消息就可以了。然后在这里我去 sleep 很久，为什么我要看一下那个 ACK 的效果好，基本上我们整个的这个 demo 代码就领着小伙伴们读完了。接下来我们去 run s 就内test，只要控制台输出没问题，就证明我们的这个 demo 演示成功了，也就证明我们的可靠性消息也就投递成功了。同学们请看 skate 了，已经启动了，证明我们的定时任务就 OK 了。注意往下看info，看衣服是不是抓取数据，但是抓取数据是0，因为我们消息可能已经投递出去了。


注意观察日志，这个 message ID 就是我们生成这个 message ID，那接下来你就看什么呢？你就看这里面都打印了吗？说这个 X1 is not exist，就是在我们的这个 container 容器里边，所以说我们去 create one 创建一个对应的这个 Rabbit template，这都是容器化。然后我们就是每隔一段时间，每隔 10 秒钟，是吧？定时任务都会去扫一次。


看见了，那接下来要验证的事情就是我们对应的那个message，就是 broker message 那张表里边有没有数据？其实在这里我们已经看到了，就是这个 broker message 数据库里面的这个 broker message 表，我们去刷新一下，同学你看这张表已经有数据了，这是我们所传递的一些参数，它用 JSON 格式帮我们去封装了，然后还有就是 try count 等于0，这次等于几？等于 1 = 1 是谁更新的？很明显等于 1 的话肯定是我们这个 Rabbit template container 里边的这个 confirm 方法，帮我们去更新了一下这个数据，然后我们来点进去看一下 Rabbit template container 里边只有什么呀？只有这个满足条件他才会装，我去更新对不对？那这些逻辑都是我们上几节课去封装的，所以说没有任何问题，这是正常情况下，我们把它停掉，停掉以后我们观察一下我们的这个 rapid 控制台，发现有一条消息，对不对？这是待处理的。


好，接下来我们再次去发一条消息，发这次消息我们来测试一下失败的场景，比如说我们现在就想测试一下我们发送失败，怎么样让他发送失败？比如说我们在这里改一下，改成 Exchange 2，很明显我们当前的这个 Rabbit 里边，他所有的 exchange 里边是没有 Exchange 2，他最多就有一个 exchange 1，对吧？所以说你发消息肯定是发失败的，发失败就是错误，错误的话定时任务会抓出来，只要超过 1 分钟超时间，它就会抓出来帮我们去做重试，重试 3 次以后如果还失败怎么办？那就直接认为这条记录fail，把我们的这个 state 状态更新成2，表示最终失败。


好，那接下来我们再重新去启动一下现在我的X2，我们来观察一下。好，这个 Skido 也起来了，是不是 skider 起来了，消息发没发出去？你看消息发出去了，但是发出去的这个内容是什么？是一个 l 的这个日志，看见了，他这里面说的很清楚，他说没有 exchange 的这么一个记录，你看 no exchange 没有，对吧？跑定时任务的时候，你看每次都会抓出来这一条，那我们来刷新一下我们这个表吧，所以我们请看最终的状态，就是刚才这条记录是不是它的 exchange 是几？它的 exchange 是 exchange 等于2，然后它已经 try count 3 次了，最终三次都失败了，最终就是失败了，所以说把 states 状态更新成2， try count 是 3 次，尝试了三次，大家可以看到是不是尝试这是第一次，第二次、第三次是不是？那其实我说我大于三次，所以说它允许0123，再往后他就不执行，所以说抓取的数据都是 0 了。


OK，那整个的这个可靠性消息的投递这一块如何去保障百分之百的成功？其实说白了就是使用定时任务扫描我们中间状态，或者是说你认为不正确的状态，但是是有一个超时间限制的，那这个逻辑就已经完全的跟大家讲清楚了。OK，接下来还剩下一点小的内容，比如说我们如何去发送一个批量消息，或者是发送一个带有延迟消息的这种方式的消息投递，这个是接下来的内容，感谢小伙伴们收看。

