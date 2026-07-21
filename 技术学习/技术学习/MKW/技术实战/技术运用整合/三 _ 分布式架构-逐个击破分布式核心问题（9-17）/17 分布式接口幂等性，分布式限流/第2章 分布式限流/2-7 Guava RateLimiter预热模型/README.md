---
title: 2-7 Guava RateLimiter预热模型
---

# 2-7 Guava RateLimiter预热模型

[image](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/22dad0e0-dd56-4f90-a764-3cd6c7dcaf03/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46642LYPHOA%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T225457Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCHorya6JGCIvIm%2BXZrLG5J%2Fcuyh9l3rT29ITd1B%2FjXqgIgO7%2FsyYxEvrZgvoRe9P8Ecov1bTfXTpLNgPSdir2V%2BSAqiAQIxv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDBuUBBGvUsghG5iYyyrcA%2B9ReuvO%2FPEV35xMBbEoSjXkR1bdzpuKG8UdSa6Zibmck4lnLd5jgS%2FpNLh%2B4JjiNTEblmj081wHVtEg2u7rzgCxzPxghox5FKM4c0tioW%2Ff%2FN9ucU%2Fep88Aq7SCvxri3KNgHb5sgyJ6XRUcGad8Zbd57TuQffY82FD1nuFcN83ccR6WlnNenIdPOerQAGDfJZr355%2FvAGpUn%2B0%2Bvtd49ip1D6tOHl1kUd4em4WURuWwFnZBZR8bpXm4s3acWmzJsf%2BWmewRzn6wCJJzmJgH6Y6i7favnFC6mqJyzlQNEaWh2VrnTU9Qmba64dAe0Ini9owWUdW0EukbSrveeVE%2B3kYVDw2Q5Z%2BEZ6P%2F1KbMk8xrQYUKq95KcsU86spEf8ldO%2F6KPXm55knR2TlmpvLAPv6%2BOjFvDIalps340UoULIWcPEzMwMqk983%2FAqv%2Bkkc38V8u8Nh26Jm2dZPkXd%2FI4q4PZcCNI0gMvNIMC36yzeo5oIz0pp9vCMVmc0YmFQZ%2FW5xbNPt4rckjwbr5NENVio7DAVwL%2BjmpmubYKnzBFcWAJrh0MmK3o%2FuugFE%2FKW%2FTdyi48Zk%2FAtDPyqo%2FwhihvAn7qDKDXTCg%2FPdwJybCykPBxBAoNfHREGCBgkKMMMW6%2F9IGOqUB0VUbUJnETilATg1F1gNQQfoxwi4WjtF5QMzjTFMOFtVgijIJd4A7RZXoAdvodb%2Fj77bmOQcTyBKWrtqNqMmlgcPeegQzpPlm9o%2FQzItK6zjPnZd%2FQL30%2BaQY20CwFsyYA6MksaKCts47THmWG7LsxtE9C3Ikpq7aaDfmC1oH%2F8Eu22kmcIajQ2taN6R8Kwdl7fygvMn6nauzgAFoGpYAVXpSGBTO&X-Amz-Signature=79c681e4d44f0bd2a36af800cc6754d7b7aa9698ba33aad383a24e4021367f0b&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

**2-7 Guava RateLimiter预热模型**

**Guava RateLimiter预热模型**

上一节我们了解了Guava组件是如何提供客户端限流功能的，这一节我们借Guava来讲一个和限流有关的小技巧 - 「流量预热」

**什么是流量预热**

我们都知道在做运动之前先得来几组拉伸之类的动作，给身体做个热身，让我们的身体平滑过渡到后面的剧烈运动中。流量预热也是一样的道理，对限流组件来说，流量预热就类似于一种热身运动，它可以动态调整令牌发放速度，让流量变化更加平滑。

我们来举一个例子：某个接口设定了100个Request每秒的限流标准，同时使用令牌桶算法做限流。假如当前时间窗口内都没有Request过来，那么令牌桶中会装满100个令牌。如果在下一秒突然涌入100个请求，这些请求会迅速消耗令牌，对服务的瞬时冲击会比较大。因此我们需要一种类似“热身运动”的缓冲机制，根据桶内的令牌数量动态控制令牌的发放速率，让忙时流量和闲时流量可以互相平滑过渡。

**流量预热的做法**

我们以Guava中的RateLimiter为例，看看流量预热在RateLimiter中是如何运作的，我们用下面的状态转换图来展示整个过程：

[image](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/6b68ac41-1264-48e8-ab26-430f76acd468/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46642LYPHOA%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T225457Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCHorya6JGCIvIm%2BXZrLG5J%2Fcuyh9l3rT29ITd1B%2FjXqgIgO7%2FsyYxEvrZgvoRe9P8Ecov1bTfXTpLNgPSdir2V%2BSAqiAQIxv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDBuUBBGvUsghG5iYyyrcA%2B9ReuvO%2FPEV35xMBbEoSjXkR1bdzpuKG8UdSa6Zibmck4lnLd5jgS%2FpNLh%2B4JjiNTEblmj081wHVtEg2u7rzgCxzPxghox5FKM4c0tioW%2Ff%2FN9ucU%2Fep88Aq7SCvxri3KNgHb5sgyJ6XRUcGad8Zbd57TuQffY82FD1nuFcN83ccR6WlnNenIdPOerQAGDfJZr355%2FvAGpUn%2B0%2Bvtd49ip1D6tOHl1kUd4em4WURuWwFnZBZR8bpXm4s3acWmzJsf%2BWmewRzn6wCJJzmJgH6Y6i7favnFC6mqJyzlQNEaWh2VrnTU9Qmba64dAe0Ini9owWUdW0EukbSrveeVE%2B3kYVDw2Q5Z%2BEZ6P%2F1KbMk8xrQYUKq95KcsU86spEf8ldO%2F6KPXm55knR2TlmpvLAPv6%2BOjFvDIalps340UoULIWcPEzMwMqk983%2FAqv%2Bkkc38V8u8Nh26Jm2dZPkXd%2FI4q4PZcCNI0gMvNIMC36yzeo5oIz0pp9vCMVmc0YmFQZ%2FW5xbNPt4rckjwbr5NENVio7DAVwL%2BjmpmubYKnzBFcWAJrh0MmK3o%2FuugFE%2FKW%2FTdyi48Zk%2FAtDPyqo%2FwhihvAn7qDKDXTCg%2FPdwJybCykPBxBAoNfHREGCBgkKMMMW6%2F9IGOqUB0VUbUJnETilATg1F1gNQQfoxwi4WjtF5QMzjTFMOFtVgijIJd4A7RZXoAdvodb%2Fj77bmOQcTyBKWrtqNqMmlgcPeegQzpPlm9o%2FQzItK6zjPnZd%2FQL30%2BaQY20CwFsyYA6MksaKCts47THmWG7LsxtE9C3Ikpq7aaDfmC1oH%2F8Eu22kmcIajQ2taN6R8Kwdl7fygvMn6nauzgAFoGpYAVXpSGBTO&X-Amz-Signature=f708f453ec8a0c2d10835a2b4ac3b952ea76c0a16ec4222ced02dc21163fd319&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

横坐标是令牌桶的当前容量，纵坐标是令牌发放速率，我们先从横坐标来分析

**横坐标**

下面两种场景会导致横坐标的变化：

闲时流量 流量较小或者压根没流量的时候，横坐标会逐渐向右移动，表示令牌桶中令牌数量增多

忙时流量 当访问流量增大的时候，横坐标向左移动，令牌桶中令牌数量变少

横轴有两个重要的坐标，一个是最右侧的“令牌桶最大容量”，这个不难理解。还有一个是Half容量，它是一个关键节点，会影响令牌发放速率。

**纵坐标**

纵坐标表示令牌的发放速率，这里有3个标线，分别是稳定时间间隔，2倍间隔，3倍间隔。

这里间隔的意思就是隔多长时间发放一个令牌，而所谓稳定间隔就是一个基准时间间隔。假如我们设置了每秒10个令牌的限流规则，那么稳定间隔也就是1s/10=0.1秒，也就是说每隔0.1秒发一个令牌。相应的，3倍间隔的数值是用稳定间隔乘以系数3，比如上面这个例子中3倍间隔就是0.3秒。

**运作模式**

了解了横坐标和纵坐标的含义之后，让我们来试着理解预热模型的用例。继续沿用上面10r/s的限流设置，稳定间隔=0.1s，3x间隔是0.3s。

我们先考虑闲时到忙时的流量转变，假定当前我们处于闲时流量阶段，没几个访问请求，这时令牌桶是满的。接着在下一秒突然涌入了10个请求，这些请求开始消耗令牌桶中的令牌。在初始阶段，令牌的放行速度比较慢，在第一个令牌被消耗以后，后面的请求要经过3x时间间隔也就是0.3s才会获取第二块令牌。随着令牌桶中令牌数量被逐渐消耗，当令牌存量下降到最大容量一半的时候（Half位置），令牌放行的速率也会提升，以稳定间隔0.1s发放令牌。

反过来也一样，在流量从忙时转变为闲时的过程中，令牌发放速率是由快到慢逐渐变化。起始阶段的令牌放行间隔是0.1s，随着令牌桶内令牌逐渐增多，当令牌的存量积累到最大容量的一半后，放行令牌的时间间隔进一步增大为0.3s。

RateLimiter正是通过这种方式来控制令牌发放的时间间隔，从而使流量的变化更加平滑。

**核心代码**

理解了预热模型的运作流程之后，我们来看一下具体代码是如何实现的。

实现流量预热的类是SmoothWarmingUp，它是SmoothRateLimiter的一个内部类，我们重点关注一个doSetRate方法，它是计算横纵坐标系关键节点的方法，先来看一下SmoothRateLimiter这个父类中定义的方法


```java
// permitsPerSecond表示每秒可以发放的令牌数量
        @Override
        final void doSetRate ( double permitsPerSecond, long nowMicros){

            resync(nowMicros);

               // 计算稳定间隔，使用1s除以令牌桶容量

            double stableIntervalMicros = SECONDS.toMicros(1L) / permitsPerSecond;

            this.stableIntervalMicros = stableIntervalMicros;

               // 调用SmoothWarmingUp类中重载的doSetRate方法

            doSetRate(permitsPerSecond, stableIntervalMicros);

        }

        父类在这里的作用主要是计算出了稳定时间间隔（使用1s / 每秒放行数量的公式来计算得出），然后预热时间、三倍间隔等是在子类的doSetRate方法中实现的。

        接下来我们看子类SmoothWarmingUp中的doSetRate做了什么

        @Override

        void doSetRate ( double permitsPerSecond, double stableIntervalMicros){

            double oldMaxPermits = maxPermits;

               // maxPermits表示令牌桶内最大容量，它由我们设置的预热时间除以稳定间隔获得

               // 打个比方，如果stableIntervalMicros=0.1s，而我们设置的预热时间是2s

               // 那么这时候maxPermits就是2除以0.1=20

            maxPermits = warmupPeriodMicros / stableIntervalMicros;

               // 这句不用解释了吧，halfPermits是最大容量的一半

            halfPermits = maxPermits / 2.0;

               // coldIntervalMicros就是我们前面写到的3倍间隔，通过稳定间隔*3计算得出

               // 稳定间隔是0.1，3倍间隔是0.2，那么平均间隔是0.2

            double coldIntervalMicros = stableIntervalMicros * 3.0;

               // slope的意思是斜率，也就是前面我们图中预热阶段中画出的斜线（速率从稳定间隔向3x间隔变化的斜线）

               // 它的计算过程就是一个简单的求斜率公式

            slope = (coldIntervalMicros - stableIntervalMicros) / halfPermits;

               // 计算目前令牌桶的令牌个数

            if (oldMaxPermits == Double.POSITIVE_INFINITY) {

               // 如果令牌桶最大容量是无穷大，则设置当前可用令牌数为0

               // 说实话这段逻辑没什么用

                storedPermits = 0.0;

            } else {

                storedPermits = (oldMaxPermits == 0.0)

                        ? maxPermits                // 初始化的状态是3x间隔

                        : storedPermits * maxPermits / oldMaxPermits;

            }

        }
```

通过上面的两个函数，RateLimiter限流器就对maxPermits和slope（预热期斜率）两个变量做了初始化配置。我把关键步骤都注释在了代码里，大家理解了之后，可以尝试去阅读这个类的其他方法，弄清maxPermits和slope是如何影响令牌发放速率的。

**小结**

这一节我们了解了预热模型的知识点，下一节我们来看一个正儿八经的分布式环境限流方案，基于Nginx网关层的限流。

学习Tips：很多同学对实践部分比较感兴趣，花不少时间去学习，但是对理论部分不求甚解，看到纯理论的图文就一扫而过，其实这是一种买椟还珠的学习方式。学会使用一项技术是非常简单的一件事，一步步跟着照做就可以，但是弄清技术背后的原理，知道为什么这么用，在什么情况下该采用什么策略，这才是更深一层的内功。所以希望大家在学习技术的时候，不仅能知其然，更能知其所以然。

[image](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/2773e1c9-3c42-4b7e-8966-82fb866e77b1/2020-09-17-172113.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46642LYPHOA%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T225457Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCHorya6JGCIvIm%2BXZrLG5J%2Fcuyh9l3rT29ITd1B%2FjXqgIgO7%2FsyYxEvrZgvoRe9P8Ecov1bTfXTpLNgPSdir2V%2BSAqiAQIxv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDBuUBBGvUsghG5iYyyrcA%2B9ReuvO%2FPEV35xMBbEoSjXkR1bdzpuKG8UdSa6Zibmck4lnLd5jgS%2FpNLh%2B4JjiNTEblmj081wHVtEg2u7rzgCxzPxghox5FKM4c0tioW%2Ff%2FN9ucU%2Fep88Aq7SCvxri3KNgHb5sgyJ6XRUcGad8Zbd57TuQffY82FD1nuFcN83ccR6WlnNenIdPOerQAGDfJZr355%2FvAGpUn%2B0%2Bvtd49ip1D6tOHl1kUd4em4WURuWwFnZBZR8bpXm4s3acWmzJsf%2BWmewRzn6wCJJzmJgH6Y6i7favnFC6mqJyzlQNEaWh2VrnTU9Qmba64dAe0Ini9owWUdW0EukbSrveeVE%2B3kYVDw2Q5Z%2BEZ6P%2F1KbMk8xrQYUKq95KcsU86spEf8ldO%2F6KPXm55knR2TlmpvLAPv6%2BOjFvDIalps340UoULIWcPEzMwMqk983%2FAqv%2Bkkc38V8u8Nh26Jm2dZPkXd%2FI4q4PZcCNI0gMvNIMC36yzeo5oIz0pp9vCMVmc0YmFQZ%2FW5xbNPt4rckjwbr5NENVio7DAVwL%2BjmpmubYKnzBFcWAJrh0MmK3o%2FuugFE%2FKW%2FTdyi48Zk%2FAtDPyqo%2FwhihvAn7qDKDXTCg%2FPdwJybCykPBxBAoNfHREGCBgkKMMMW6%2F9IGOqUB0VUbUJnETilATg1F1gNQQfoxwi4WjtF5QMzjTFMOFtVgijIJd4A7RZXoAdvodb%2Fj77bmOQcTyBKWrtqNqMmlgcPeegQzpPlm9o%2FQzItK6zjPnZd%2FQL30%2BaQY20CwFsyYA6MksaKCts47THmWG7LsxtE9C3Ikpq7aaDfmC1oH%2F8Eu22kmcIajQ2taN6R8Kwdl7fygvMn6nauzgAFoGpYAVXpSGBTO&X-Amz-Signature=98231b23065f7f3ad0512a4000d873d4722a57be2bcc2725ff129babc289cd4a&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



