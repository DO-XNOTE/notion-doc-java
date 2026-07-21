---
title: 2-7 Kafka海量日志收集实战_logstash日志过滤实战-1
---

# 2-7 Kafka海量日志收集实战_logstash日志过滤实战-1

[image](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/9856babd-5bfd-4c86-bd3b-6ec85ae7ecda/SCR-20240807-heqq.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466THCYQB3N%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T225328Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIEkWBrQ%2BMB3d3QHLur7ir4XNM2i%2B7%2Fuh1mTCihncFVhGAiEAm8XFghD755sB5dvceXuT122p%2F2HeM4TakfgXWHB%2BgvgqiAQIxv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDEiuMExJ0VGBhrC8%2FircA2WlW5koWDEgKjDaLOHtjey4%2F9MVmXyOxFE%2Bcku3TF%2FRAhIUb%2FvOJ1VdW%2B23uExPycKccbxNcF2Tljjvqqr2S0NYklaONDY0Zznxm7uq67r7YOP9JuSZdVNJBKXRY3sDsY4tQNDDdPtLzVgdlzstNhxhXORKnXTO%2BwXnGb0irMAmP1FlY%2BSBdjXWJDpMqJ6NISOg0xbUyZ5Bmu1XXoeoVNFphC01nvxjGdgm%2Ffgs0d56vl6UkzN2DKVBSgOs%2FqTxBXOnjK0EzLMguqF6le%2FQ0r59YyzT1N4rH%2BioBM01iDvFk5xP8BcYwVCkqosbv3p97GKx1rVYjZCZ1vKdyXImF8%2Bxs9EwvD7KUnuYIZGd4CejJJyDxfuVJmmffhohr1pGWM4Lot%2FPBQrGrIgQkgQjjea6tHxuCJ2y9TX%2BcdBUTTiWWIh88BxfE3jG%2FliYWR6yqs7OObHaV3cNCTdVG690G0hhitNinLUMXpTgfX4iD70bOnUzxrV1sLEwHWi0gu2aYlyPtBCwkwYkzePS15gKSmiXf8mCFUwBF4rK1SdYkGZMq3fDw%2FOVVcrbs9RCgTP3RYhMAtrN3YnMNJbxWey%2BRNjw54BHNwp2k1gGlW81SDfpcY0Iwtd9coAs%2BajkMMe6%2F9IGOqUBGOcjFDZbngQfE4zeaBhwC5zS8ODE9fnpkQDNHIuw9MiOljyMNq3oY0vJ8WaehRQqSkFQktCfg7S6HTgzrAzUCa9MkJXbqTOgPynoXN3uzTrIBUK6R55V5NWICSijy5r0ne0US9RQeXlTODbvqxO82i8ZB3bQYe9nNSm6CVAdFRdj2AGZsx9uEQSqaejdePkEEXuyXMB3FNGu62a4JMySn6XPOCEx&X-Amz-Signature=cca2c335442e02dd8a657201f774c4fe1229d1bb4a3bd2655c01a08848a93398&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

[image](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/8bf54b36-5586-4c56-b000-35e175ad4db9/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466THCYQB3N%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T225328Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIEkWBrQ%2BMB3d3QHLur7ir4XNM2i%2B7%2Fuh1mTCihncFVhGAiEAm8XFghD755sB5dvceXuT122p%2F2HeM4TakfgXWHB%2BgvgqiAQIxv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDEiuMExJ0VGBhrC8%2FircA2WlW5koWDEgKjDaLOHtjey4%2F9MVmXyOxFE%2Bcku3TF%2FRAhIUb%2FvOJ1VdW%2B23uExPycKccbxNcF2Tljjvqqr2S0NYklaONDY0Zznxm7uq67r7YOP9JuSZdVNJBKXRY3sDsY4tQNDDdPtLzVgdlzstNhxhXORKnXTO%2BwXnGb0irMAmP1FlY%2BSBdjXWJDpMqJ6NISOg0xbUyZ5Bmu1XXoeoVNFphC01nvxjGdgm%2Ffgs0d56vl6UkzN2DKVBSgOs%2FqTxBXOnjK0EzLMguqF6le%2FQ0r59YyzT1N4rH%2BioBM01iDvFk5xP8BcYwVCkqosbv3p97GKx1rVYjZCZ1vKdyXImF8%2Bxs9EwvD7KUnuYIZGd4CejJJyDxfuVJmmffhohr1pGWM4Lot%2FPBQrGrIgQkgQjjea6tHxuCJ2y9TX%2BcdBUTTiWWIh88BxfE3jG%2FliYWR6yqs7OObHaV3cNCTdVG690G0hhitNinLUMXpTgfX4iD70bOnUzxrV1sLEwHWi0gu2aYlyPtBCwkwYkzePS15gKSmiXf8mCFUwBF4rK1SdYkGZMq3fDw%2FOVVcrbs9RCgTP3RYhMAtrN3YnMNJbxWey%2BRNjw54BHNwp2k1gGlW81SDfpcY0Iwtd9coAs%2BajkMMe6%2F9IGOqUBGOcjFDZbngQfE4zeaBhwC5zS8ODE9fnpkQDNHIuw9MiOljyMNq3oY0vJ8WaehRQqSkFQktCfg7S6HTgzrAzUCa9MkJXbqTOgPynoXN3uzTrIBUK6R55V5NWICSijy5r0ne0US9RQeXlTODbvqxO82i8ZB3bQYe9nNSm6CVAdFRdj2AGZsx9uEQSqaejdePkEEXuyXMB3FNGu62a4JMySn6XPOCEx&X-Amz-Signature=7574afef3879c412eb50a0d1550eba557594f367460fd0c90739e4911e9bf2b0&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

[image](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/923f44a0-f840-44e7-8b7c-24d566ecf9fc/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466THCYQB3N%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T225328Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIEkWBrQ%2BMB3d3QHLur7ir4XNM2i%2B7%2Fuh1mTCihncFVhGAiEAm8XFghD755sB5dvceXuT122p%2F2HeM4TakfgXWHB%2BgvgqiAQIxv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDEiuMExJ0VGBhrC8%2FircA2WlW5koWDEgKjDaLOHtjey4%2F9MVmXyOxFE%2Bcku3TF%2FRAhIUb%2FvOJ1VdW%2B23uExPycKccbxNcF2Tljjvqqr2S0NYklaONDY0Zznxm7uq67r7YOP9JuSZdVNJBKXRY3sDsY4tQNDDdPtLzVgdlzstNhxhXORKnXTO%2BwXnGb0irMAmP1FlY%2BSBdjXWJDpMqJ6NISOg0xbUyZ5Bmu1XXoeoVNFphC01nvxjGdgm%2Ffgs0d56vl6UkzN2DKVBSgOs%2FqTxBXOnjK0EzLMguqF6le%2FQ0r59YyzT1N4rH%2BioBM01iDvFk5xP8BcYwVCkqosbv3p97GKx1rVYjZCZ1vKdyXImF8%2Bxs9EwvD7KUnuYIZGd4CejJJyDxfuVJmmffhohr1pGWM4Lot%2FPBQrGrIgQkgQjjea6tHxuCJ2y9TX%2BcdBUTTiWWIh88BxfE3jG%2FliYWR6yqs7OObHaV3cNCTdVG690G0hhitNinLUMXpTgfX4iD70bOnUzxrV1sLEwHWi0gu2aYlyPtBCwkwYkzePS15gKSmiXf8mCFUwBF4rK1SdYkGZMq3fDw%2FOVVcrbs9RCgTP3RYhMAtrN3YnMNJbxWey%2BRNjw54BHNwp2k1gGlW81SDfpcY0Iwtd9coAs%2BajkMMe6%2F9IGOqUBGOcjFDZbngQfE4zeaBhwC5zS8ODE9fnpkQDNHIuw9MiOljyMNq3oY0vJ8WaehRQqSkFQktCfg7S6HTgzrAzUCa9MkJXbqTOgPynoXN3uzTrIBUK6R55V5NWICSijy5r0ne0US9RQeXlTODbvqxO82i8ZB3bQYe9nNSm6CVAdFRdj2AGZsx9uEQSqaejdePkEEXuyXMB3FNGu62a4JMySn6XPOCEx&X-Amz-Signature=b2fdd65cae1920c5eb94d58c3a049ec2a6365027782e42ad899af94d406682ee&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

OK 小伙伴们，那么这节课我们继续往下去学习，来学习我们这个高性能的这个吞吐量核心实战。就是说我们对于海量日收集的这么一个实战的，继续往下去讲来说一下这个日志的过滤。那对于日志过滤，我们来看一看它有一个组件叫做 log stash 那对于 log stash ，我相信小伙伴们应该是有对于基础部分有进行学习，老师已经给了相关的基础文档了，那我们来看看我们怎么去对这个 loss dash 做学习。

[image](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/932b1daf-1520-4afc-89c5-9e2cfb3a7927/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466THCYQB3N%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T225328Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIEkWBrQ%2BMB3d3QHLur7ir4XNM2i%2B7%2Fuh1mTCihncFVhGAiEAm8XFghD755sB5dvceXuT122p%2F2HeM4TakfgXWHB%2BgvgqiAQIxv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDEiuMExJ0VGBhrC8%2FircA2WlW5koWDEgKjDaLOHtjey4%2F9MVmXyOxFE%2Bcku3TF%2FRAhIUb%2FvOJ1VdW%2B23uExPycKccbxNcF2Tljjvqqr2S0NYklaONDY0Zznxm7uq67r7YOP9JuSZdVNJBKXRY3sDsY4tQNDDdPtLzVgdlzstNhxhXORKnXTO%2BwXnGb0irMAmP1FlY%2BSBdjXWJDpMqJ6NISOg0xbUyZ5Bmu1XXoeoVNFphC01nvxjGdgm%2Ffgs0d56vl6UkzN2DKVBSgOs%2FqTxBXOnjK0EzLMguqF6le%2FQ0r59YyzT1N4rH%2BioBM01iDvFk5xP8BcYwVCkqosbv3p97GKx1rVYjZCZ1vKdyXImF8%2Bxs9EwvD7KUnuYIZGd4CejJJyDxfuVJmmffhohr1pGWM4Lot%2FPBQrGrIgQkgQjjea6tHxuCJ2y9TX%2BcdBUTTiWWIh88BxfE3jG%2FliYWR6yqs7OObHaV3cNCTdVG690G0hhitNinLUMXpTgfX4iD70bOnUzxrV1sLEwHWi0gu2aYlyPtBCwkwYkzePS15gKSmiXf8mCFUwBF4rK1SdYkGZMq3fDw%2FOVVcrbs9RCgTP3RYhMAtrN3YnMNJbxWey%2BRNjw54BHNwp2k1gGlW81SDfpcY0Iwtd9coAs%2BajkMMe6%2F9IGOqUBGOcjFDZbngQfE4zeaBhwC5zS8ODE9fnpkQDNHIuw9MiOljyMNq3oY0vJ8WaehRQqSkFQktCfg7S6HTgzrAzUCa9MkJXbqTOgPynoXN3uzTrIBUK6R55V5NWICSijy5r0ne0US9RQeXlTODbvqxO82i8ZB3bQYe9nNSm6CVAdFRdj2AGZsx9uEQSqaejdePkEEXuyXMB3FNGu62a4JMySn6XPOCEx&X-Amz-Signature=dd9252042832ef07f51e2af77d044108b9508b5843c58c4198b64469e6046b30&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

首先第一点就是安装入门，这个没什么可说的。然后第二点就是我们对于 erk 环境的一个搭建，其实已经进入了中间的一部分环节了。后面其实就是把这个数据 think 到我们的这个 elastic search 上就可以了。接下来对于这个基础语法就是我们的 log 赛事的基础语法，老师会给大家写一些相关的这个文章供小伙伴们去学习。那我相信小伙伴对这个 logstash 基础语法应该是非常快的就能够掌握了，所以说我们这节课就直接进入这个 logstash 的这个实战应用了。

[image](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/216c42a8-bf58-4c31-b812-f3a9bbf8ad48/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466THCYQB3N%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T225328Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIEkWBrQ%2BMB3d3QHLur7ir4XNM2i%2B7%2Fuh1mTCihncFVhGAiEAm8XFghD755sB5dvceXuT122p%2F2HeM4TakfgXWHB%2BgvgqiAQIxv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDEiuMExJ0VGBhrC8%2FircA2WlW5koWDEgKjDaLOHtjey4%2F9MVmXyOxFE%2Bcku3TF%2FRAhIUb%2FvOJ1VdW%2B23uExPycKccbxNcF2Tljjvqqr2S0NYklaONDY0Zznxm7uq67r7YOP9JuSZdVNJBKXRY3sDsY4tQNDDdPtLzVgdlzstNhxhXORKnXTO%2BwXnGb0irMAmP1FlY%2BSBdjXWJDpMqJ6NISOg0xbUyZ5Bmu1XXoeoVNFphC01nvxjGdgm%2Ffgs0d56vl6UkzN2DKVBSgOs%2FqTxBXOnjK0EzLMguqF6le%2FQ0r59YyzT1N4rH%2BioBM01iDvFk5xP8BcYwVCkqosbv3p97GKx1rVYjZCZ1vKdyXImF8%2Bxs9EwvD7KUnuYIZGd4CejJJyDxfuVJmmffhohr1pGWM4Lot%2FPBQrGrIgQkgQjjea6tHxuCJ2y9TX%2BcdBUTTiWWIh88BxfE3jG%2FliYWR6yqs7OObHaV3cNCTdVG690G0hhitNinLUMXpTgfX4iD70bOnUzxrV1sLEwHWi0gu2aYlyPtBCwkwYkzePS15gKSmiXf8mCFUwBF4rK1SdYkGZMq3fDw%2FOVVcrbs9RCgTP3RYhMAtrN3YnMNJbxWey%2BRNjw54BHNwp2k1gGlW81SDfpcY0Iwtd9coAs%2BajkMMe6%2F9IGOqUBGOcjFDZbngQfE4zeaBhwC5zS8ODE9fnpkQDNHIuw9MiOljyMNq3oY0vJ8WaehRQqSkFQktCfg7S6HTgzrAzUCa9MkJXbqTOgPynoXN3uzTrIBUK6R55V5NWICSijy5r0ne0US9RQeXlTODbvqxO82i8ZB3bQYe9nNSm6CVAdFRdj2AGZsx9uEQSqaejdePkEEXuyXMB3FNGu62a4JMySn6XPOCEx&X-Amz-Signature=454eb67109197c564318f071474dd6a3b94abf267f87f34b68512f74a2a84563&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

那么其实为什么有同学说老师为什么这个我们不从头开始去讲这个 local 赛事，它的一些基础语法到底怎么去用，因为我觉得这东西很简单，小伙伴们花个半小时你就可以把它的基础语法学会了，只不过你可能比较难去搞懂，就是说在实际工作中应该怎么去最好的去应用这个 loss session 他应该怎么去写，他应该怎么去配置。那这个是我们在课上跟小伙伴们一起分享的。


好了，那我们现在就开始快速的去进入我们的这个 log 赛事的这个环境搭建以及这个配置文件的讲解。然后我们最终的目的是想要从这个 love 赛事上能够消费我们之前往 Kafka 上扔的一些数据，就是 fail beat 作为 producer 扔数据到卡夫卡，然后我们的 love 赛事去消费数据。


好了，那我们马上去进入学习，老师在这里已经准备好了一台服务器，就是我们对应的三四这台节点。 34 这个节点我们 CD 到这个 USR local CD 到这个 software 下。那我们去安装好我们对应的我先把这个文件传上来。这个文件就是有两个文件，一个是还有他 OK 把他们两个传上来。传上来以后咱们稍微等一下。因为什么呢？因为 log stash 这个文件相对来讲有一点点大，它相对于这个 lbeat 来讲还真的是很大，你会看到它大体上有多大来看，基本上我们看到劳斯莱斯它有这么大，而我们的 fail beat 其实是非常小，就是 56 兆。


好。接下来我们一起把我们的这个 logstash 做一个安装。如何去安装它呢？我们其实现在已经看到了我们有了这个 logstash 它的这个踏点 gz 那其实你直接解答就好了。那在这里老师也是给小伙伴写了一个文档，就是 logstash.tst 我们来看一下。


首先你去做解压安装，我们一步步走。首先第一步把它放到 USR local 下，回车还是用到6.0，这个版本就版本都是一样的。你看 love 赛事安装的过程相对来讲就复杂一些。为什么呢？因为它的这个包是很大的，因为 logo stage 它本质上它是一个 Java 去写。所以说其实现在一些大型的互联网公司都是期望有新的这个探索。


就是说虽然 Java 还是主流技术，但是逐渐的有一些高兴的东西可能是更偏向于用 go 浪去写或者是什么呢？或者你会看到比如说大家熟悉 Spark 或者是熟悉你的这个 Flink 我们知道就是他用一些 Scala 用 Scala 写去编程，他那个语法特别简单，其实包括我们 Java 也是在一点点的进化。比如说 Java 里边的这个十一十二十三的版本，它的这个编程的方式模式是越趋近于简化的。你比如说我们 Java 10 里面都支持以 VR 就是那种像 Java script 声明的那表达式去做了，所以说它慢慢的也变得越简单。因为我们之前的 Java 你比如说写一个匿名函数，你首先得重写方法或者怎么样。后来有了这个 let me 的表达式之后就更简单了，慢慢的都会往这个编程简单化。可能之前写 100 多行的代码，后面我可能写四五十行，三四十行就可以解决了，都是这么一个慢慢这个眼镜的一个过程。


好了，废话不多说，我们回过头来来看一看我们的这个 lost 6.0，然后我们 CD 进来看进去，如果看到它里边有 bin 有 config 等等这些配置文件。然后在这里我们先 make DIR 我们创建一个 script 这么一个目录。这个 script 有了之后，然后我想把我刚才的配置就是我们刚才一并上传出来在 software 下的这个配置，我把它 MV 它到什么呢？到我们刚才的 script 那个下面 USR local logstash script 下。


OK 我们这回 CD 到这个 log stash 下面，我们去 CD 到 sprint 下面。我们看到这个脚本，然后你可以给他赋予权限，比如说这个他没有执行权限，你给他一些执行权限这些都可以。 OK 那接下来我们重点来看一看这个 log stash 它的 script 对应的一些配置有哪些？它是怎么去配置的？他在说这个配置之前，其实有一个很关键的，就是说让赛事他去做调优的一些点，我们要注意一下。首先我们来看一看这个目录，那肯定是从 config 里面去找，那我们私域到这个 config 配置文件里，

[image](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/b5c71724-8729-4243-af42-6c694dc0a095/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466THCYQB3N%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T225328Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIEkWBrQ%2BMB3d3QHLur7ir4XNM2i%2B7%2Fuh1mTCihncFVhGAiEAm8XFghD755sB5dvceXuT122p%2F2HeM4TakfgXWHB%2BgvgqiAQIxv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDEiuMExJ0VGBhrC8%2FircA2WlW5koWDEgKjDaLOHtjey4%2F9MVmXyOxFE%2Bcku3TF%2FRAhIUb%2FvOJ1VdW%2B23uExPycKccbxNcF2Tljjvqqr2S0NYklaONDY0Zznxm7uq67r7YOP9JuSZdVNJBKXRY3sDsY4tQNDDdPtLzVgdlzstNhxhXORKnXTO%2BwXnGb0irMAmP1FlY%2BSBdjXWJDpMqJ6NISOg0xbUyZ5Bmu1XXoeoVNFphC01nvxjGdgm%2Ffgs0d56vl6UkzN2DKVBSgOs%2FqTxBXOnjK0EzLMguqF6le%2FQ0r59YyzT1N4rH%2BioBM01iDvFk5xP8BcYwVCkqosbv3p97GKx1rVYjZCZ1vKdyXImF8%2Bxs9EwvD7KUnuYIZGd4CejJJyDxfuVJmmffhohr1pGWM4Lot%2FPBQrGrIgQkgQjjea6tHxuCJ2y9TX%2BcdBUTTiWWIh88BxfE3jG%2FliYWR6yqs7OObHaV3cNCTdVG690G0hhitNinLUMXpTgfX4iD70bOnUzxrV1sLEwHWi0gu2aYlyPtBCwkwYkzePS15gKSmiXf8mCFUwBF4rK1SdYkGZMq3fDw%2FOVVcrbs9RCgTP3RYhMAtrN3YnMNJbxWey%2BRNjw54BHNwp2k1gGlW81SDfpcY0Iwtd9coAs%2BajkMMe6%2F9IGOqUBGOcjFDZbngQfE4zeaBhwC5zS8ODE9fnpkQDNHIuw9MiOljyMNq3oY0vJ8WaehRQqSkFQktCfg7S6HTgzrAzUCa9MkJXbqTOgPynoXN3uzTrIBUK6R55V5NWICSijy5r0ne0US9RQeXlTODbvqxO82i8ZB3bQYe9nNSm6CVAdFRdj2AGZsx9uEQSqaejdePkEEXuyXMB3FNGu62a4JMySn6XPOCEx&X-Amz-Signature=6b8450824b132b93edc09996e6c5a2e4348f176116e51216433613b83eb26c09&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

再去看这个配置文件里好几个。首先这个是 log forty two 也就是说 log stash 它本质上它的日志收集它的日志，这个组件它自己内部的日志也是用 slfg two 去做的。


还有一个 gvm options 那肯定是配置 jvm 相关的。因为我刚才说了它是一个 Java 写的，所以说它应该有对应的配置。好了，我们来看一看吧。比如说我们现在要配置对应的我们的这个 gvm 参数，我们来找一找。比如说我们点去看一下就好。


gvm OPS 其实默认因为我在这里做测试，所以说我就不想太配它，它默认都是一个 G 在实际的生产环境中，根据你自己的需求。一般来讲 log stash 这个内存尽量稍微大一点会比较好，因为它运行起来的时候它是很吃内存的。比如说你是 8g 的服务器，那你要至少去配置 6G 左右预留两 G 防止它这个系统被 cue 掉。其实有的时候对于一些性能调优，在这里可以简单的跟小伙伴说一说。比如说我 8g 的服务器那我配 8g 内存可以吗？理论上来讲也是可以的。但是有一个问题就是说当你的 gvm 如果我们先说没有对外内存没有对外内存，有的高峰期的时候可能这个内存满了会导致什么呢？你的系统一共就 8g 然后你 GM 也配了 8g 有的时候你操作系统会把我们的这个进程 Q 掉，因为内存溢出多问题。


还有就是说如果有对外内存的情况下，你最好配一半就好，或者配60%。比如说 10g 那你配 6G 剩下那 4G 给对外内存。比如说我们使用 let it 它肯定是 direct buffer 去用了一些对外内存相关的东西。所以说你再去写一些 NIO 或者是使用了对外内存的一些应用程序的时候，你尽量要给对外内存预留一些空间。要不然的话你会看到你的应用程序一共 10g 你配了 8 个 G 然后你 down 不出来的内存的文件，你会发现才用了几百兆，或者是才用了不到这个 8 个 G 才用了两三个 G 它不可能操作系统 cue 掉。那原因就是我们可能对外链层使用的比较大，导致把我们的操作系统 cue 掉，这些都是一些小的在实际工作中的一些技巧，在这里简单的跟小伙伴们一带而过。 OK 那我们回过头来，其实这些配置我们比较关心的是哪一个呢？比较关心的就是刚才我们说的这个 log [stache.ml](http://stache.ml/) 它里边有一个配置是比较关键的，我们来打开有一个什么配置呢？其实你可以去找。

```java
# 解压安装
tar -zxvf logstash-6.6.0.tar.gz -C /usr/local/

## conf下配置文件说明：
# logstash配置文件：/config/logstash.yml
# JVM参数文件：/config/jvm.options
#  日志格式配置文件：log4j2.properties
#  制作Linux服务参数：/config/startup.options


vim /usr/local/logstash-6.6.0/config/logstash.yml
## 增加workers工作线程数 可以有效的提升logstash性能
pipeline.workers: 16


## 启动logstash
nohup /usr/local/logstash-6.6.0/bin/logstash -f /usr/local/logstash-6.6.0/script/logstash-script.conf &
```

在这里我就直接说就是这个 paper line 沃克斯这个 paper line worker 是很重要，它是在性能调优的时候会起到决定性作用的。那这个具体 paper line 沃克斯是一个什么概念？那其实在老师后面给你的文档里会有这个很详细的介绍。那我们现在你去增加 workers 可以有效的去提升我们 log 赛事它的这个性能，可以去增加它的这个工作线程数。那这里边是配了 16 个。那其实我们它 default 是 2 就 CPU 和数，你看说的 default to the number of the host CPU cause 因为我们现在做测试程序，我肯定是没办法给他搞了几座，我们就默认了就好，要不然的话可能会有问题。好在这里我就不配了，

[image](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/b6cb0c04-8107-4af5-8aa9-236468f4bac8/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466THCYQB3N%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T225328Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIEkWBrQ%2BMB3d3QHLur7ir4XNM2i%2B7%2Fuh1mTCihncFVhGAiEAm8XFghD755sB5dvceXuT122p%2F2HeM4TakfgXWHB%2BgvgqiAQIxv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDEiuMExJ0VGBhrC8%2FircA2WlW5koWDEgKjDaLOHtjey4%2F9MVmXyOxFE%2Bcku3TF%2FRAhIUb%2FvOJ1VdW%2B23uExPycKccbxNcF2Tljjvqqr2S0NYklaONDY0Zznxm7uq67r7YOP9JuSZdVNJBKXRY3sDsY4tQNDDdPtLzVgdlzstNhxhXORKnXTO%2BwXnGb0irMAmP1FlY%2BSBdjXWJDpMqJ6NISOg0xbUyZ5Bmu1XXoeoVNFphC01nvxjGdgm%2Ffgs0d56vl6UkzN2DKVBSgOs%2FqTxBXOnjK0EzLMguqF6le%2FQ0r59YyzT1N4rH%2BioBM01iDvFk5xP8BcYwVCkqosbv3p97GKx1rVYjZCZ1vKdyXImF8%2Bxs9EwvD7KUnuYIZGd4CejJJyDxfuVJmmffhohr1pGWM4Lot%2FPBQrGrIgQkgQjjea6tHxuCJ2y9TX%2BcdBUTTiWWIh88BxfE3jG%2FliYWR6yqs7OObHaV3cNCTdVG690G0hhitNinLUMXpTgfX4iD70bOnUzxrV1sLEwHWi0gu2aYlyPtBCwkwYkzePS15gKSmiXf8mCFUwBF4rK1SdYkGZMq3fDw%2FOVVcrbs9RCgTP3RYhMAtrN3YnMNJbxWey%2BRNjw54BHNwp2k1gGlW81SDfpcY0Iwtd9coAs%2BajkMMe6%2F9IGOqUBGOcjFDZbngQfE4zeaBhwC5zS8ODE9fnpkQDNHIuw9MiOljyMNq3oY0vJ8WaehRQqSkFQktCfg7S6HTgzrAzUCa9MkJXbqTOgPynoXN3uzTrIBUK6R55V5NWICSijy5r0ne0US9RQeXlTODbvqxO82i8ZB3bQYe9nNSm6CVAdFRdj2AGZsx9uEQSqaejdePkEEXuyXMB3FNGu62a4JMySn6XPOCEx&X-Amz-Signature=51e45aae9379e4f561219b5c07cd2adef8b67ef20bcf5f5fecf38586d90c9d75&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

但是你要注意在生产环境上，一定要配。好说是 CPU 核数。但是比如说你是 4 毫 8g 的，你配个 8 或者配个 16 都没什么太大问题。


好了，然后我们重点关注刚才老师说的这个 script 下面。这个配置是在 log 赛事启动的时候，你一定要对它加载的，启动的时候是依赖这个配置文件的，所以我们一起来读一读这个配置文件。 OK 这个配置文件老师还是说你用那个栏窗口打开那个不太好看。所以说我们用这个来看一看，这个配置真的是比较多也没关系，我们一会先把后面的这一块东西先干掉。然后我们保留前面的部分，我们来看一下。首先这个对于 log stash 而言，它有两个比较大的内容，应该说有三个比较大的块。第一个叫做 input 这一长条都是 input 还有一个叫做 filter 然后再往下就是一个 output 当然无论是 input 还是 filter 还是 output 都可以有多个。你看我现在这个是一个奥特布特，然后两个奥特布特 OK input 你看我们在这里刚才说了我们要做什么事情，我们 lock stache 是充当于卡斯卡的 consumer 也就是消费者的角色。那消费者应该怎么去做呢？这里边大家有兴趣可以看那个 love 赛事API ，就是直接配一个卡夫卡一个大括号，然后里边就可以对卡夫卡进行一些配置。

```java
## multiline 插件也可以用于其他类似的堆栈式信息，比如 linux 的内核日志。
input {
  kafka {
    ## app-log-服务名称
    topics_pattern => "app-log-.*"
    bootstrap_servers => "192.168.11.51:9092"
	codec => json
	consumer_threads => 1	## 增加consumer的并行消费线程数
	decorate_events => true
    #auto_offset_rest => "latest"
	group_id => "app-log-group"
   }
   
   kafka {
    ## error-log-服务名称
    topics_pattern => "error-log-.*"
    bootstrap_servers => "192.168.11.51:9092"
	codec => json
	consumer_threads => 1
	decorate_events => true
    #auto_offset_rest => "latest"
	group_id => "error-log-group"
   }
   
}

filter {
  
  ## 时区转换
  ruby {
	code => "event.set('index_time',event.timestamp.time.localtime.strftime('%Y.%m.%d'))"
  }

  if "app-log" in [fields][logtopic]{
    grok {
        ## 表达式
        match => ["message", "\[%{NOTSPACE:currentDateTime}\] \[%{NOTSPACE:level}\] \[%{NOTSPACE:thread-id}\] \[%{NOTSPACE:class}\] \[%{DATA:hostName}\] \[%{DATA:ip}\] \[%{DATA:applicationName}\] \[%{DATA:location}\] \[%{DATA:messageInfo}\] ## (\'\'|%{QUOTEDSTRING:throwable})"]
    }
  }

  if "error-log" in [fields][logtopic]{
    grok {
        ## 表达式
        match => ["message", "\[%{NOTSPACE:currentDateTime}\] \[%{NOTSPACE:level}\] \[%{NOTSPACE:thread-id}\] \[%{NOTSPACE:class}\] \[%{DATA:hostName}\] \[%{DATA:ip}\] \[%{DATA:applicationName}\] \[%{DATA:location}\] \[%{DATA:messageInfo}\] ## (\'\'|%{QUOTEDSTRING:throwable})"]
    }
  }
  
}

## 测试输出到控制台：
output {
  stdout { codec => rubydebug }
}


## elasticsearch：
output {

  if "app-log" in [fields][logtopic]{
	## es插件
	elasticsearch {
  	    # es服务地址
        hosts => ["192.168.11.35:9200"]
        # 用户名密码      
        user => "elastic"
        password => "123456"
        ## 索引名，+ 号开头的，就会自动认为后面是时间格式：
        ## javalog-app-service-2019.01.23 
        index => "app-log-%{[fields][logbiz]}-%{index_time}"
        # 是否嗅探集群ip：一般设置true；http://192.168.11.35:9200/_nodes/http?pretty
        # 通过嗅探机制进行es集群负载均衡发日志消息
        sniffing => true
        # logstash默认自带一个mapping模板，进行模板覆盖
        template_overwrite => true
    } 
  }
  
  if "error-log" in [fields][logtopic]{
	elasticsearch {
        hosts => ["192.168.11.35:9200"]    
        user => "elastic"
        password => "123456"
        index => "error-log-%{[fields][logbiz]}-%{index_time}"
        sniffing => true
        template_overwrite => true
    } 
  }
}
```

[file](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/4ed18cb4-907d-4a97-9e6b-e828c417233d/logstash-script.conf?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466THCYQB3N%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T225328Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIEkWBrQ%2BMB3d3QHLur7ir4XNM2i%2B7%2Fuh1mTCihncFVhGAiEAm8XFghD755sB5dvceXuT122p%2F2HeM4TakfgXWHB%2BgvgqiAQIxv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDEiuMExJ0VGBhrC8%2FircA2WlW5koWDEgKjDaLOHtjey4%2F9MVmXyOxFE%2Bcku3TF%2FRAhIUb%2FvOJ1VdW%2B23uExPycKccbxNcF2Tljjvqqr2S0NYklaONDY0Zznxm7uq67r7YOP9JuSZdVNJBKXRY3sDsY4tQNDDdPtLzVgdlzstNhxhXORKnXTO%2BwXnGb0irMAmP1FlY%2BSBdjXWJDpMqJ6NISOg0xbUyZ5Bmu1XXoeoVNFphC01nvxjGdgm%2Ffgs0d56vl6UkzN2DKVBSgOs%2FqTxBXOnjK0EzLMguqF6le%2FQ0r59YyzT1N4rH%2BioBM01iDvFk5xP8BcYwVCkqosbv3p97GKx1rVYjZCZ1vKdyXImF8%2Bxs9EwvD7KUnuYIZGd4CejJJyDxfuVJmmffhohr1pGWM4Lot%2FPBQrGrIgQkgQjjea6tHxuCJ2y9TX%2BcdBUTTiWWIh88BxfE3jG%2FliYWR6yqs7OObHaV3cNCTdVG690G0hhitNinLUMXpTgfX4iD70bOnUzxrV1sLEwHWi0gu2aYlyPtBCwkwYkzePS15gKSmiXf8mCFUwBF4rK1SdYkGZMq3fDw%2FOVVcrbs9RCgTP3RYhMAtrN3YnMNJbxWey%2BRNjw54BHNwp2k1gGlW81SDfpcY0Iwtd9coAs%2BajkMMe6%2F9IGOqUBGOcjFDZbngQfE4zeaBhwC5zS8ODE9fnpkQDNHIuw9MiOljyMNq3oY0vJ8WaehRQqSkFQktCfg7S6HTgzrAzUCa9MkJXbqTOgPynoXN3uzTrIBUK6R55V5NWICSijy5r0ne0US9RQeXlTODbvqxO82i8ZB3bQYe9nNSm6CVAdFRdj2AGZsx9uEQSqaejdePkEEXuyXMB3FNGu62a4JMySn6XPOCEx&X-Amz-Signature=c6e98c0f6ed32dd690dcce44ab2417ac3d9bb4242a87ceb6a379a11e8d5a3234&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)


比如说 topics partition 就是我应该接收哪些 topic 下的消息，就是我的输入是什么？我的输入就是 App 杠 log 杠星，所有以 App 杠 log 杠修开头的这个 partition 或者说这个 topic 4，因为它那个 partition 后面只是说对于 topic 加一个杠零杠一杠2，所以说你可以简单的认为就是 topic 就好了。 OK 他都会做一个收集上报，就是相当于他订阅的主题，可以这么去理解。然后我们要去配置卡夫卡的 server 就是51，然后9092。接下来你的 code C 是不是你可以用 Jason 当然基本上现在目前都是 Jason 然后接下来就是你的 consumer threat 丝，你的 consumer threat 丝在这里边。因为我们只有一个 partition 所以说你配四个也没有意义，能理解。我说意思，就配一个就好了，因为我们一个 partition 你就对应着一个 consumer thread 这就可以了。对应着如果你有 10 个 partition 那你在这里要配 10 是吧，你配多了也没有意义，你太少了，可能够用可能会增加这个卡夫卡就是 log search 的压力。


然后这个对应的这个 event 就是设置为 true 就好了，它的 offset 到底是从哪开始？它默认的情况就是 last 这个是卡夫卡，我们之前已经学的以及这个非常重要，就是说你的卡夫卡应该有个组，你的组给它起个名字，我们在这里叫做 App 杠 log group 好，那这个卡夫卡是做什么事情呢？这个卡夫卡是监听对于 App 杠 log 杠应用服务的 topic 下面所有的数据接收好。
第二个卡夫卡以 error 杠 log 杠服务名称的一个接收就是 error 杠 log 杠星所有的我们都去做接收，然后对应的它的这个 server 卡 server 以及它的 thread 我说了一个 Python 就写一个就好，其他的 group 可以改成 error 杠 log 杠 group 那上面这些东西无非就是监听了或者是说叫做订阅了所有的 App 杠 log 和 L 杠 log 的就是这两个 topic 的consumer ，你可以理解为就是这两个 consumer 好了，那再往下看 filter 是做什么事情？ filter 就是说我把这些数据都抓回来之后，有些数据是我想要的，有些数据是我不想要。那我怎么去做一个区分或者做一个过滤呢？来同学们一起看。


首先这一块就是说我应该有一个当前时间，这个当前时间作用于什么呢？后面再说我们先看核心的说，如果 if 你的 fields 杠 log topic 这个东西是从哪来的？同学们想一想，这个东西其实是从 file beat 上来的。我不知道小伙伴们还记不记得 fail beat 之前我给大家看的那个对应的配置。 fail beat 上面我们其实是有的，我们可以看一下 fail beat 我们 CD 到 well beat 然后去 vim 我们 fell beat 它的这个点 yml 其实你会看到这里边 fields 的 topic 这个它是两个有层级的，

[image](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/f5b8d22f-7780-4f30-8679-38a2ee166323/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466THCYQB3N%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T225328Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIEkWBrQ%2BMB3d3QHLur7ir4XNM2i%2B7%2Fuh1mTCihncFVhGAiEAm8XFghD755sB5dvceXuT122p%2F2HeM4TakfgXWHB%2BgvgqiAQIxv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDEiuMExJ0VGBhrC8%2FircA2WlW5koWDEgKjDaLOHtjey4%2F9MVmXyOxFE%2Bcku3TF%2FRAhIUb%2FvOJ1VdW%2B23uExPycKccbxNcF2Tljjvqqr2S0NYklaONDY0Zznxm7uq67r7YOP9JuSZdVNJBKXRY3sDsY4tQNDDdPtLzVgdlzstNhxhXORKnXTO%2BwXnGb0irMAmP1FlY%2BSBdjXWJDpMqJ6NISOg0xbUyZ5Bmu1XXoeoVNFphC01nvxjGdgm%2Ffgs0d56vl6UkzN2DKVBSgOs%2FqTxBXOnjK0EzLMguqF6le%2FQ0r59YyzT1N4rH%2BioBM01iDvFk5xP8BcYwVCkqosbv3p97GKx1rVYjZCZ1vKdyXImF8%2Bxs9EwvD7KUnuYIZGd4CejJJyDxfuVJmmffhohr1pGWM4Lot%2FPBQrGrIgQkgQjjea6tHxuCJ2y9TX%2BcdBUTTiWWIh88BxfE3jG%2FliYWR6yqs7OObHaV3cNCTdVG690G0hhitNinLUMXpTgfX4iD70bOnUzxrV1sLEwHWi0gu2aYlyPtBCwkwYkzePS15gKSmiXf8mCFUwBF4rK1SdYkGZMq3fDw%2FOVVcrbs9RCgTP3RYhMAtrN3YnMNJbxWey%2BRNjw54BHNwp2k1gGlW81SDfpcY0Iwtd9coAs%2BajkMMe6%2F9IGOqUBGOcjFDZbngQfE4zeaBhwC5zS8ODE9fnpkQDNHIuw9MiOljyMNq3oY0vJ8WaehRQqSkFQktCfg7S6HTgzrAzUCa9MkJXbqTOgPynoXN3uzTrIBUK6R55V5NWICSijy5r0ne0US9RQeXlTODbvqxO82i8ZB3bQYe9nNSm6CVAdFRdj2AGZsx9uEQSqaejdePkEEXuyXMB3FNGu62a4JMySn6XPOCEx&X-Amz-Signature=29e43ec3fb101abf3170759182423071ae4425a98c9a943f446d840a4627b1cc&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

你要用中括号去表示。那对应着我们这里就是那个配置是不是 fields topic 就是说你这个 topic 这个 key 是不是包含 in App 高 log 如果包含的话，我下面做什么处理？那同理这个 error 杠 log 也是一样的。就是如果这个 fields 有这个前缀，或者说里边包含这个内容， in 就表示包含，如果它的话，我应该做这个处理。


好。那这个处理到底是什么东西呢？这个就是 group 表达式了。那 group 表达式很简单，你把数据接过来，我怎么去做过滤？它里边开始都是固定的是表示匹配。然后一个等号和尖角号就表示怎么去匹配，匹配的规则是什么样子的？那匹配的规则就是后面写的这一长串。好，我把后面写的这张串 copy 过来，跟大家简单说一下，大家就知道了，就是这两个匹配规则是一样的，无论是 App log 还是 L log 它的格式是一样的。那这个格式到底是按照什么规则去定的呢？那这个就得说来话长了，就得回过头来看一下。


我们最开始在讲这个日志输出的时候，在讲我们 Java 程序的时候，我们来看就是说你那个 logstash 规则必须得按照这个来

[image](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/4726085b-27af-4f5a-9ac6-0c941ea77ede/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466THCYQB3N%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T225328Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIEkWBrQ%2BMB3d3QHLur7ir4XNM2i%2B7%2Fuh1mTCihncFVhGAiEAm8XFghD755sB5dvceXuT122p%2F2HeM4TakfgXWHB%2BgvgqiAQIxv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDEiuMExJ0VGBhrC8%2FircA2WlW5koWDEgKjDaLOHtjey4%2F9MVmXyOxFE%2Bcku3TF%2FRAhIUb%2FvOJ1VdW%2B23uExPycKccbxNcF2Tljjvqqr2S0NYklaONDY0Zznxm7uq67r7YOP9JuSZdVNJBKXRY3sDsY4tQNDDdPtLzVgdlzstNhxhXORKnXTO%2BwXnGb0irMAmP1FlY%2BSBdjXWJDpMqJ6NISOg0xbUyZ5Bmu1XXoeoVNFphC01nvxjGdgm%2Ffgs0d56vl6UkzN2DKVBSgOs%2FqTxBXOnjK0EzLMguqF6le%2FQ0r59YyzT1N4rH%2BioBM01iDvFk5xP8BcYwVCkqosbv3p97GKx1rVYjZCZ1vKdyXImF8%2Bxs9EwvD7KUnuYIZGd4CejJJyDxfuVJmmffhohr1pGWM4Lot%2FPBQrGrIgQkgQjjea6tHxuCJ2y9TX%2BcdBUTTiWWIh88BxfE3jG%2FliYWR6yqs7OObHaV3cNCTdVG690G0hhitNinLUMXpTgfX4iD70bOnUzxrV1sLEwHWi0gu2aYlyPtBCwkwYkzePS15gKSmiXf8mCFUwBF4rK1SdYkGZMq3fDw%2FOVVcrbs9RCgTP3RYhMAtrN3YnMNJbxWey%2BRNjw54BHNwp2k1gGlW81SDfpcY0Iwtd9coAs%2BajkMMe6%2F9IGOqUBGOcjFDZbngQfE4zeaBhwC5zS8ODE9fnpkQDNHIuw9MiOljyMNq3oY0vJ8WaehRQqSkFQktCfg7S6HTgzrAzUCa9MkJXbqTOgPynoXN3uzTrIBUK6R55V5NWICSijy5r0ne0US9RQeXlTODbvqxO82i8ZB3bQYe9nNSm6CVAdFRdj2AGZsx9uEQSqaejdePkEEXuyXMB3FNGu62a4JMySn6XPOCEx&X-Amz-Signature=35f799855a00da77131aa69de6f170d04cfacfb477d42e2e33eb86db7d14f624&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

看见了吧，这是必须的。那这个到底是怎么来的呢？我们来关注一下。那这个 message 说的是什么呢？它这个是 log 赛事固定的格式，前面固定写死了数据过来我统一叫一个名字叫 message 这个 message 能不能匹配后面的这个表达式？如果能匹配那就不过滤。如果匹配不了，它就会过滤掉。

[image](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/e4dd0500-f8c1-4fd2-8a81-c49cb1d63692/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466THCYQB3N%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T225328Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIEkWBrQ%2BMB3d3QHLur7ir4XNM2i%2B7%2Fuh1mTCihncFVhGAiEAm8XFghD755sB5dvceXuT122p%2F2HeM4TakfgXWHB%2BgvgqiAQIxv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDEiuMExJ0VGBhrC8%2FircA2WlW5koWDEgKjDaLOHtjey4%2F9MVmXyOxFE%2Bcku3TF%2FRAhIUb%2FvOJ1VdW%2B23uExPycKccbxNcF2Tljjvqqr2S0NYklaONDY0Zznxm7uq67r7YOP9JuSZdVNJBKXRY3sDsY4tQNDDdPtLzVgdlzstNhxhXORKnXTO%2BwXnGb0irMAmP1FlY%2BSBdjXWJDpMqJ6NISOg0xbUyZ5Bmu1XXoeoVNFphC01nvxjGdgm%2Ffgs0d56vl6UkzN2DKVBSgOs%2FqTxBXOnjK0EzLMguqF6le%2FQ0r59YyzT1N4rH%2BioBM01iDvFk5xP8BcYwVCkqosbv3p97GKx1rVYjZCZ1vKdyXImF8%2Bxs9EwvD7KUnuYIZGd4CejJJyDxfuVJmmffhohr1pGWM4Lot%2FPBQrGrIgQkgQjjea6tHxuCJ2y9TX%2BcdBUTTiWWIh88BxfE3jG%2FliYWR6yqs7OObHaV3cNCTdVG690G0hhitNinLUMXpTgfX4iD70bOnUzxrV1sLEwHWi0gu2aYlyPtBCwkwYkzePS15gKSmiXf8mCFUwBF4rK1SdYkGZMq3fDw%2FOVVcrbs9RCgTP3RYhMAtrN3YnMNJbxWey%2BRNjw54BHNwp2k1gGlW81SDfpcY0Iwtd9coAs%2BajkMMe6%2F9IGOqUBGOcjFDZbngQfE4zeaBhwC5zS8ODE9fnpkQDNHIuw9MiOljyMNq3oY0vJ8WaehRQqSkFQktCfg7S6HTgzrAzUCa9MkJXbqTOgPynoXN3uzTrIBUK6R55V5NWICSijy5r0ne0US9RQeXlTODbvqxO82i8ZB3bQYe9nNSm6CVAdFRdj2AGZsx9uEQSqaejdePkEEXuyXMB3FNGu62a4JMySn6XPOCEx&X-Amz-Signature=3e80a0820b463c90bd10903cb438404883a607a280af319470700e88d2b37aee&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

好了，我们来看一看这个过滤规则。首先它是以这个是反斜杠，是转译，是不是是以中括号开头的。然后它是一个叫做 nospace 就是不能有空格。然后 current day time 这个 current time 是东八区的，跟我们之前的日志输出的是相匹配的。看见了。然后第二个我们回车大家可以看 no space level info 这个是日志的级别 level 听到了。然后再往下看 no space 是什么是 thread ID 这个 thread ID 当然他们两个的名字是否要叫的一样呢？这个无所谓，这里边的值你自己随便去定义，就是 P 值你自己随便去定义，但是数据的格式肯定要对应上，然后再往下看就是 class 了。我这个 logger 它叫 logger 但是我这里叫 class 为什么？因为它就是一个class ，你看它就是一个 class 好然后再往下看还有什么 host name 主机名称IP。


