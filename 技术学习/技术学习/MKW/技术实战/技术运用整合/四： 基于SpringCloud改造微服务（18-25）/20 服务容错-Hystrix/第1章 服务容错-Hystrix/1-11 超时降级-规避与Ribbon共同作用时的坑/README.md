---
title: 1-11 超时降级-规避与Ribbon共同作用时的坑
---

# 1-11 超时降级-规避与Ribbon共同作用时的坑

[image](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/32bc189e-e70d-42e0-82f1-ea0f3a882fc0/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XYX2ZJYE%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T225640Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDmAaew5DusYDtGSjIxyAJzMRJUw5Ykky4QP2%2F0zNO1swIgYcklA6i5FjxZcbF5%2Bpv125jElrgfOnnaFC1fSkX0fXgqiAQIxv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDHDGppqdRM9Hzm%2B%2BRircA%2FWfy5lmTa7YwuxtbgGRKbPp7E5a3zB4jQ1cuIfN83ClozplWbxuTUW%2FwZkI0syZ9TC0yULTYZgzkz7BWazPGW%2FchY6ZJvPLa5f3e24cn4xcc%2BnRQ8FOhX%2BbKrnBndyt%2BvscHI3rbgL4QCjZJ0k8nk%2BHbOmqv880i2sY%2FctwHd9fCkykm1OEeAaameXV5PPMqwW2wtfTRgD5er8O6I%2F9IR2MjP4Fq7nW%2FGim%2FPcJ69rs26UQ9%2FgAGCebGKt0JQtecH7SdZIlbtNIH0YFSsI9kNCZHPQKxA6qlKPaYDHI8yaBjpPliYrdrTL8yAu%2F12Z5Rk2%2BSbW2VGpv7I%2Ba8QLHpSlF3HsoT6zdluNgGCy5JSNCZJSQrhFkyjE%2B8pWtHpowuZ59AIg0HQE9lw46f8txacqxHsYHRXJmIk20k2FUVfbComL3e%2FmSgpC%2FBv71AmK9h7watW1BCOXkHxfrRQLGuctvBgn%2Fw%2FciFL9DWLQ8wKH%2BjOzBAwRgAsLR5g3TTvn7iMrylrKg8j8R%2Br1m20ATqNg5PH8sFokjWj50ivvaAXy4NrCMj6mLAjBsi9XL6qw3p0qE2EBS3DeHVdJPqrnKBRiNdCzxoIJsa6Q9b5PV7bqrybG1PqOuXyp3SRuzMIXE%2F9IGOqUBbDeFILYzs8tjhGQJOMjHcIbmcMdy3UtD6eEh7E%2FZhS0uDghrlm8xmknrUEMxIuGq0scYNyWCQLZqoapfz7ak%2FkgOamxnGaEtO8wJJH9GRkiVGHt1Hk8twDMDfaC9pp2GfBeSiWhgM80BKiiSKq9oalOBZ50oGDAuk1W3UU7mUVgfALxUiFS1HjADNa26C5KTPIaC8CF7YBjw%2FeGHTTKXRLgGChyv&X-Amz-Signature=381bf96710400788f44017a7cbefa796dfcff6e836dfc1081ad7404507c9be8a&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

[image](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/45816a5a-12b1-45c5-afc9-5cf39415c032/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XYX2ZJYE%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T225640Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDmAaew5DusYDtGSjIxyAJzMRJUw5Ykky4QP2%2F0zNO1swIgYcklA6i5FjxZcbF5%2Bpv125jElrgfOnnaFC1fSkX0fXgqiAQIxv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDHDGppqdRM9Hzm%2B%2BRircA%2FWfy5lmTa7YwuxtbgGRKbPp7E5a3zB4jQ1cuIfN83ClozplWbxuTUW%2FwZkI0syZ9TC0yULTYZgzkz7BWazPGW%2FchY6ZJvPLa5f3e24cn4xcc%2BnRQ8FOhX%2BbKrnBndyt%2BvscHI3rbgL4QCjZJ0k8nk%2BHbOmqv880i2sY%2FctwHd9fCkykm1OEeAaameXV5PPMqwW2wtfTRgD5er8O6I%2F9IR2MjP4Fq7nW%2FGim%2FPcJ69rs26UQ9%2FgAGCebGKt0JQtecH7SdZIlbtNIH0YFSsI9kNCZHPQKxA6qlKPaYDHI8yaBjpPliYrdrTL8yAu%2F12Z5Rk2%2BSbW2VGpv7I%2Ba8QLHpSlF3HsoT6zdluNgGCy5JSNCZJSQrhFkyjE%2B8pWtHpowuZ59AIg0HQE9lw46f8txacqxHsYHRXJmIk20k2FUVfbComL3e%2FmSgpC%2FBv71AmK9h7watW1BCOXkHxfrRQLGuctvBgn%2Fw%2FciFL9DWLQ8wKH%2BjOzBAwRgAsLR5g3TTvn7iMrylrKg8j8R%2Br1m20ATqNg5PH8sFokjWj50ivvaAXy4NrCMj6mLAjBsi9XL6qw3p0qE2EBS3DeHVdJPqrnKBRiNdCzxoIJsa6Q9b5PV7bqrybG1PqOuXyp3SRuzMIXE%2F9IGOqUBbDeFILYzs8tjhGQJOMjHcIbmcMdy3UtD6eEh7E%2FZhS0uDghrlm8xmknrUEMxIuGq0scYNyWCQLZqoapfz7ak%2FkgOamxnGaEtO8wJJH9GRkiVGHt1Hk8twDMDfaC9pp2GfBeSiWhgM80BKiiSKq9oalOBZ50oGDAuk1W3UU7mUVgfALxUiFS1HjADNa26C5KTPIaC8CF7YBjw%2FeGHTTKXRLgGChyv&X-Amz-Signature=fab79081e9160c6e4e5f5768f986c1c86eb412abd928846071cdcb1ad2f17de1&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

[image](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/190d2b8e-5560-4b40-9f9e-fd64617e9919/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XYX2ZJYE%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T225640Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDmAaew5DusYDtGSjIxyAJzMRJUw5Ykky4QP2%2F0zNO1swIgYcklA6i5FjxZcbF5%2Bpv125jElrgfOnnaFC1fSkX0fXgqiAQIxv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDHDGppqdRM9Hzm%2B%2BRircA%2FWfy5lmTa7YwuxtbgGRKbPp7E5a3zB4jQ1cuIfN83ClozplWbxuTUW%2FwZkI0syZ9TC0yULTYZgzkz7BWazPGW%2FchY6ZJvPLa5f3e24cn4xcc%2BnRQ8FOhX%2BbKrnBndyt%2BvscHI3rbgL4QCjZJ0k8nk%2BHbOmqv880i2sY%2FctwHd9fCkykm1OEeAaameXV5PPMqwW2wtfTRgD5er8O6I%2F9IR2MjP4Fq7nW%2FGim%2FPcJ69rs26UQ9%2FgAGCebGKt0JQtecH7SdZIlbtNIH0YFSsI9kNCZHPQKxA6qlKPaYDHI8yaBjpPliYrdrTL8yAu%2F12Z5Rk2%2BSbW2VGpv7I%2Ba8QLHpSlF3HsoT6zdluNgGCy5JSNCZJSQrhFkyjE%2B8pWtHpowuZ59AIg0HQE9lw46f8txacqxHsYHRXJmIk20k2FUVfbComL3e%2FmSgpC%2FBv71AmK9h7watW1BCOXkHxfrRQLGuctvBgn%2Fw%2FciFL9DWLQ8wKH%2BjOzBAwRgAsLR5g3TTvn7iMrylrKg8j8R%2Br1m20ATqNg5PH8sFokjWj50ivvaAXy4NrCMj6mLAjBsi9XL6qw3p0qE2EBS3DeHVdJPqrnKBRiNdCzxoIJsa6Q9b5PV7bqrybG1PqOuXyp3SRuzMIXE%2F9IGOqUBbDeFILYzs8tjhGQJOMjHcIbmcMdy3UtD6eEh7E%2FZhS0uDghrlm8xmknrUEMxIuGq0scYNyWCQLZqoapfz7ak%2FkgOamxnGaEtO8wJJH9GRkiVGHt1Hk8twDMDfaC9pp2GfBeSiWhgM80BKiiSKq9oalOBZ50oGDAuk1W3UU7mUVgfALxUiFS1HjADNa26C5KTPIaC8CF7YBjw%2FeGHTTKXRLgGChyv&X-Amz-Signature=8d2e3d0046d0cd9f8d924148a114510647156e64540bc5a100be75b97a8ae5ec&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

1-11    超时降级    -    规避与 Ribbon  共同作用时的坑
Hystrix  与  Ribbon  不得不说的事    -    超时配置
前面的小节里我们做了几个小练习，熟悉了 Hystrix 服务降级的使用，这一节我们来学习一下 Ribbon 和 Hystrix 共同作用时要注意的地方-超时配置。之前我们学习了很复杂的Ribbon 超时计算公式-求极限，那么再加上 Hystrix 情况会变得更复杂吗？
**数学课代表之争**
我们知道  Feign  集成了  Ribbon  和  Hystrix  两个组件，它俩都各自有一套超时配置，话说一个班级不能有两个数学课代表，那到底哪个超时配置是最终生效的那个呢？
我们先来复习一下  Ribbon  的超时时间计算公式：最大超时时间=（连接超时时间+接口超时时间）*（当前节点重试次数+1）*（换节点重试次数+1）
假如经过上述计算，Ribbon  的超时时间是  2000ms，那么  Hystrix  的超时时间应该设置成多少才合理呢？我们先来看看  Hystrix  的默认全局配置：

```java
hystrix.command.default.execution.isolation.thread.timeoutInMilliseconds=1000
```


以上全局配置设置了 Hystrix 的熔断时间为 1000ms。这里 Hystrix 的超时时间设置比Ribbon 配置的时间短，那么不等 Ribbon 重试结束，Hystrix 判定超时后就会直接执行熔断逻辑。因此，Hystrix 和 Ribbon 是一个共同作用的关系，谁先到达超时指标就会率先起作用。通常来讲，Hystrix 的熔断时间要比 Ribbon 的最长超时时间设置的略长一些，这样就可以让 Ribbon 的重试机制充分发挥作用，以免出现还没来得及重试就进入 fallback 逻辑的情况发生。那如果我们有一些接口对响应时间的要求特别高，比如说商品详情页接口，元数据必须在2s  以内加载返回，那我们怎么针对方法设置更细粒度的  Hystrix  超时限制？
Hystrix  方法级别超时控制我们有两个方式针对  Method  级别做超时判定，我们先来看两个配置例子：基于方法签名的超时配置

```java
hystrix.command.ClassName#methodName(Integer).execution.isolation.thread.timeoutInMilliseconds=1000
```



上面的配置是基于“方法签名”生成的，其中 ClassName#methodName(Integer)就是一串类名+方法名+方法参数的组合，对于复杂的方法，人工拼出这一套组合字符串也挺费脑子的，Feign 提供了一个简单的工具根据反射机制生成字符串：

Feign.configKey(MyService.class, MyService.class.getMethod("findFriend", Integer.class))
如果说上面的配置对于你来说太过于麻烦，那你可以采用下面的一种。
**基于  CommandKey  的配置**
我们在声明@HystrixCommand  的时候，可以给方法指定一个  CommandKey，就像下面这样：


```java
@HystrixCommand(commandKey = "myKey"，fallbackMethod = "fallback")
```


这里我们给方法指定了  commandKey  为  mykey，接下来只要使用  myKey  来替换方法签名就可以实现同样的效果，是不是更简单了？

```java
hystrix.command.myKey.execution.isolation.thread.timeoutInMilliseconds=1000
```


小结
这一小节我们知道了  Hystrix  和  Ribbon  共同作用的时候如何判断超时时间，接下来，我们就来点烧脑的，去源码里探秘  Hystrix  的降级触发方式。


学习 Tips：

对于小型应用来说往往不需要降级措施，设计降级方案会增加系统复杂度和维护成本，我们尽量不要为了降级而降级，这样反而是画蛇添足了。也就是说，学习了一项新技术，未必就要生搬硬套应用在自己的项目中。技术只有使用在合适的场景下才能发挥真正的作用。

[image](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/e6388175-956c-4a89-90f0-9ae12dadd5fe/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XYX2ZJYE%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T225640Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDmAaew5DusYDtGSjIxyAJzMRJUw5Ykky4QP2%2F0zNO1swIgYcklA6i5FjxZcbF5%2Bpv125jElrgfOnnaFC1fSkX0fXgqiAQIxv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDHDGppqdRM9Hzm%2B%2BRircA%2FWfy5lmTa7YwuxtbgGRKbPp7E5a3zB4jQ1cuIfN83ClozplWbxuTUW%2FwZkI0syZ9TC0yULTYZgzkz7BWazPGW%2FchY6ZJvPLa5f3e24cn4xcc%2BnRQ8FOhX%2BbKrnBndyt%2BvscHI3rbgL4QCjZJ0k8nk%2BHbOmqv880i2sY%2FctwHd9fCkykm1OEeAaameXV5PPMqwW2wtfTRgD5er8O6I%2F9IR2MjP4Fq7nW%2FGim%2FPcJ69rs26UQ9%2FgAGCebGKt0JQtecH7SdZIlbtNIH0YFSsI9kNCZHPQKxA6qlKPaYDHI8yaBjpPliYrdrTL8yAu%2F12Z5Rk2%2BSbW2VGpv7I%2Ba8QLHpSlF3HsoT6zdluNgGCy5JSNCZJSQrhFkyjE%2B8pWtHpowuZ59AIg0HQE9lw46f8txacqxHsYHRXJmIk20k2FUVfbComL3e%2FmSgpC%2FBv71AmK9h7watW1BCOXkHxfrRQLGuctvBgn%2Fw%2FciFL9DWLQ8wKH%2BjOzBAwRgAsLR5g3TTvn7iMrylrKg8j8R%2Br1m20ATqNg5PH8sFokjWj50ivvaAXy4NrCMj6mLAjBsi9XL6qw3p0qE2EBS3DeHVdJPqrnKBRiNdCzxoIJsa6Q9b5PV7bqrybG1PqOuXyp3SRuzMIXE%2F9IGOqUBbDeFILYzs8tjhGQJOMjHcIbmcMdy3UtD6eEh7E%2FZhS0uDghrlm8xmknrUEMxIuGq0scYNyWCQLZqoapfz7ak%2FkgOamxnGaEtO8wJJH9GRkiVGHt1Hk8twDMDfaC9pp2GfBeSiWhgM80BKiiSKq9oalOBZ50oGDAuk1W3UU7mUVgfALxUiFS1HjADNa26C5KTPIaC8CF7YBjw%2FeGHTTKXRLgGChyv&X-Amz-Signature=65dc77352dea7f4c7a675d009b6f6a3f48c8e5936b3c47eacb78a34b75ffae34&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)




