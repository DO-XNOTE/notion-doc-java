---
title: 5-4 性能规划 - 性能指标和应用层优化策略
---

# 5-4 性能规划 - 性能指标和应用层优化策略

[image](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/74deb411-4ee0-4ae2-81bd-19ba9cce4328/SCR-20240731-thyf.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WB2W4R7W%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T230737Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDlpVmOHMag9AJwSNodVJC%2Bvn%2F%2F2XpKHPWVHroq6zhXUwIhAPifbSyso6tmSRGm7gpQCr2O%2FI1j%2BaUDmuVIsW6eE2XOKogECMb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1Igx9PLxCung%2FlV4n3VAq3APBnHkLuNqaXBK0cwi3fWYullpE8ohcih%2BAs%2FUgZ2e%2F0Um90g4Je48tEzZrTRyY7tXVGT0vJWfe6%2FZp7AIRmjM4FVcMoqu1uWtmJbheAjZb9TiRtw8BCOvFFwutzub7C3lfBJhKJWZYGfnUdlMG0wic1jqOwn9uUngko44oqEWz75kAekxSsjjrYye9tig6VwOHI02%2FxBalDkAVrTjOQCqoke%2BQ8h87YSKmjCp6vVVHThPrfjLjuKl1SIyilT5GC2MnOSCJ4aR01bqFja0iI5lelR0YvBWgSIZQfraJAFzTLR6t83L29SptfWNpJwiBMM%2Bje3cHyVoPd0B0Usxy7myzNrMWFxdt1g8JLg1BDyxFZM%2B5ucuWVZ36Cm11BtldqazZGGcvYWgm96S20648I02spa%2FRsaMH0k0CW8CZSvOjQ%2FXRhFaQpgsJsmLGG8OyHE8ExZV5oCyX1RUqJyisMf3DgTR4iyahdolTQLMiK41dM9QPycYL1Vyo6FrxqyOJP%2BxqHUsqz9YAk%2FKZLvKQP%2BARarV78GTzTHtV6oI4saQEaMtV8DLOD8FV6vxUXSdv9IEiBtNzvdCv%2FGrvKe%2BTZSHMuDmLtV%2F2lntVmspTjPauzN0XJHEQZdMC%2BGyEhjCjuP%2FSBjqkAcY4wdzyJnDQdcklcCHdm485DKvkskwIALfay1z1FjR4LOnVdJBjxmP7OD1%2BJcjFZbVRutoNOFl8WDJzWmXBeV8kIQG%2BCQd7tMTbhkhAbwNmZ7Tyr%2BR%2FLYndFjj9A0qC4WxHUGpk%2BIVfhb8Zw1xYN51StaLsz9wJvWYXBrlm5aK74RIV2Fq47rx9d4TskM7q6fOirkMK16W2aVI2Z%2BLbshxZmLQv&X-Amz-Signature=7dae097f0aa7595ec6e7e95fb0b8dc66a1f5cb8a00db51a2644075effd2df6db&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

[image](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/30312681-c555-4af8-b88e-a7ee35b43fb8/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WB2W4R7W%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T230737Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDlpVmOHMag9AJwSNodVJC%2Bvn%2F%2F2XpKHPWVHroq6zhXUwIhAPifbSyso6tmSRGm7gpQCr2O%2FI1j%2BaUDmuVIsW6eE2XOKogECMb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1Igx9PLxCung%2FlV4n3VAq3APBnHkLuNqaXBK0cwi3fWYullpE8ohcih%2BAs%2FUgZ2e%2F0Um90g4Je48tEzZrTRyY7tXVGT0vJWfe6%2FZp7AIRmjM4FVcMoqu1uWtmJbheAjZb9TiRtw8BCOvFFwutzub7C3lfBJhKJWZYGfnUdlMG0wic1jqOwn9uUngko44oqEWz75kAekxSsjjrYye9tig6VwOHI02%2FxBalDkAVrTjOQCqoke%2BQ8h87YSKmjCp6vVVHThPrfjLjuKl1SIyilT5GC2MnOSCJ4aR01bqFja0iI5lelR0YvBWgSIZQfraJAFzTLR6t83L29SptfWNpJwiBMM%2Bje3cHyVoPd0B0Usxy7myzNrMWFxdt1g8JLg1BDyxFZM%2B5ucuWVZ36Cm11BtldqazZGGcvYWgm96S20648I02spa%2FRsaMH0k0CW8CZSvOjQ%2FXRhFaQpgsJsmLGG8OyHE8ExZV5oCyX1RUqJyisMf3DgTR4iyahdolTQLMiK41dM9QPycYL1Vyo6FrxqyOJP%2BxqHUsqz9YAk%2FKZLvKQP%2BARarV78GTzTHtV6oI4saQEaMtV8DLOD8FV6vxUXSdv9IEiBtNzvdCv%2FGrvKe%2BTZSHMuDmLtV%2F2lntVmspTjPauzN0XJHEQZdMC%2BGyEhjCjuP%2FSBjqkAcY4wdzyJnDQdcklcCHdm485DKvkskwIALfay1z1FjR4LOnVdJBjxmP7OD1%2BJcjFZbVRutoNOFl8WDJzWmXBeV8kIQG%2BCQd7tMTbhkhAbwNmZ7Tyr%2BR%2FLYndFjj9A0qC4WxHUGpk%2BIVfhb8Zw1xYN51StaLsz9wJvWYXBrlm5aK74RIV2Fq47rx9d4TskM7q6fOirkMK16W2aVI2Z%2BLbshxZmLQv&X-Amz-Signature=48d37522e535b1796248e7c2f73445738e2a53b3d4613e7b026b44353e36295d&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

hello，我们课网的各位同学们大家好，我是姚半仙，在这一节要把同学们从这个 CRUD 的低级趣味当中脱离出来看一看。除了 CRUD 以外，我们还要在写代码当中关注什么呀？一个性能测试的这些指标和如何来做业务层的性能优化，那这是我们在写代码的时候应该在心里面有的这样一个方向。好，我们首先来看一下咱的性能测试指标都有哪些维度，那这里说来说去，其实大的指标就三个维度，

[image](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/8f3b0d34-d9ff-46b0-ad86-931a3db7ee64/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WB2W4R7W%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T230737Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDlpVmOHMag9AJwSNodVJC%2Bvn%2F%2F2XpKHPWVHroq6zhXUwIhAPifbSyso6tmSRGm7gpQCr2O%2FI1j%2BaUDmuVIsW6eE2XOKogECMb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1Igx9PLxCung%2FlV4n3VAq3APBnHkLuNqaXBK0cwi3fWYullpE8ohcih%2BAs%2FUgZ2e%2F0Um90g4Je48tEzZrTRyY7tXVGT0vJWfe6%2FZp7AIRmjM4FVcMoqu1uWtmJbheAjZb9TiRtw8BCOvFFwutzub7C3lfBJhKJWZYGfnUdlMG0wic1jqOwn9uUngko44oqEWz75kAekxSsjjrYye9tig6VwOHI02%2FxBalDkAVrTjOQCqoke%2BQ8h87YSKmjCp6vVVHThPrfjLjuKl1SIyilT5GC2MnOSCJ4aR01bqFja0iI5lelR0YvBWgSIZQfraJAFzTLR6t83L29SptfWNpJwiBMM%2Bje3cHyVoPd0B0Usxy7myzNrMWFxdt1g8JLg1BDyxFZM%2B5ucuWVZ36Cm11BtldqazZGGcvYWgm96S20648I02spa%2FRsaMH0k0CW8CZSvOjQ%2FXRhFaQpgsJsmLGG8OyHE8ExZV5oCyX1RUqJyisMf3DgTR4iyahdolTQLMiK41dM9QPycYL1Vyo6FrxqyOJP%2BxqHUsqz9YAk%2FKZLvKQP%2BARarV78GTzTHtV6oI4saQEaMtV8DLOD8FV6vxUXSdv9IEiBtNzvdCv%2FGrvKe%2BTZSHMuDmLtV%2F2lntVmspTjPauzN0XJHEQZdMC%2BGyEhjCjuP%2FSBjqkAcY4wdzyJnDQdcklcCHdm485DKvkskwIALfay1z1FjR4LOnVdJBjxmP7OD1%2BJcjFZbVRutoNOFl8WDJzWmXBeV8kIQG%2BCQd7tMTbhkhAbwNmZ7Tyr%2BR%2FLYndFjj9A0qC4WxHUGpk%2BIVfhb8Zw1xYN51StaLsz9wJvWYXBrlm5aK74RIV2Fq47rx9d4TskM7q6fOirkMK16W2aVI2Z%2BLbshxZmLQv&X-Amz-Signature=395911f949f6e4b39c4c551f42dbbcdd7a62d14f8e67bf9a57eb85fd416756aa&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

一个是RT，我们叫它响应时间 response time，还有一个 query per second 每秒访问的这个次数。那这两个指标老师在前面课程当中天天念叨，同学们应该比较熟悉了。


第三个是并发数OK，同学们往往觉得这个 QBS 和并发数其实看起来非常的相似，其实它们侧重的维度都有各自的不同。 QBS 这里我们往往会侧重于一个系统的吞吐量，你每秒钟可以去处理多少的用户请求，这是从吞吐量的维度来描述你系统的能力。而并发树这里是描述着你的系统的并发能力，也就是你同时可以处理的请求的数量。那它跟 QPS 其实有那么一点的差别。比如说我们衡量一个人的战斗力，假设这个人我们说他非常的能打，短时间内输出特别的高，是个DPS，那这个 QPS 就是形容你这个人每秒钟能打出几拳，这是形容你的出拳速度，你的输出。那你掌法再快，你佛山五英手好了，你只有两只手，这里并发数最大可支撑的就是2。


那回到我们性能测试的这个方向上来说，往往并发数并不是一个非常限制系统性能瓶颈的一个术式，因为我们总能通过一些像水平扩展等等这种集群能力，把你整个服务集群的并发数给它，把这个数值打高，那我们的关注度往往是关注于这个 RT 和QPS。那在前面一章老师也跟大家去分享了如何来做装机容量的评估，以及应用水位的监控。那这一部分同学们可以再去复习一下，去再熟悉温习一下这个RT、 QPS 和你访问压力之间的一个关系，以及如何来去在咱的测试压测过程当中构建你的这个性能基线。那除了这三个指标，通常我们还要去定位一个性能的瓶颈，那这个瓶颈我们怎么来定位？哎，这往往就要靠一些第三方的工具，比如说像 zibkin 或者是像 Yinger 这种去做链路追踪的系统，这种链路追踪系统可以把你整条请求链路上的所有经过的子系统，它们所花费的时间给它分门别类地列出来，那从这里我们往往就可以一目了然，看到它的性能究竟花费在了哪一块是最多的，然后对它进行一个针对性的优化。


那我们来做统计的时候，不光可以统计每一个链路环节当中的平均花费时间，也可以针对一些离散点，也就是离圈点分析，找出一个最慢的请求，把它揪出来，看这个最慢的请求里哪一部分花的时间最长，往往这个动作可以帮你们发现一些意尝不到的。比如说偶然间你的 connection 系统与系统之间的一个连接，可能会被防火墙不经意的掐断，那么在这个时候如果只统计它的平均时间，很难发现这个问题。那如果大家可以把一些特别慢的一些请求给它拉出来单独分析，往往就能发现出这些隐藏的很深的一些bug，那这个都是在做性能调优过程当中的一个经验之谈。


好，那我们接下来看一下对于复杂的业务来说，我们怎么来做一个性能的优化。咱这个说的复杂业务可不只是CRUD，我把它定位到一个像电商领域当中，要串联很多上下游链路调用的一个复杂的  RPC 接口，那么对于这个场景来说，我们单单只从业务层面跟大家做分析，那就是从我们开发人员角度，更多的是我们自己可以把控的这些方向。

[image](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/3ef6ade2-da73-41dc-968d-a52c26a458d6/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WB2W4R7W%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T230737Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDlpVmOHMag9AJwSNodVJC%2Bvn%2F%2F2XpKHPWVHroq6zhXUwIhAPifbSyso6tmSRGm7gpQCr2O%2FI1j%2BaUDmuVIsW6eE2XOKogECMb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1Igx9PLxCung%2FlV4n3VAq3APBnHkLuNqaXBK0cwi3fWYullpE8ohcih%2BAs%2FUgZ2e%2F0Um90g4Je48tEzZrTRyY7tXVGT0vJWfe6%2FZp7AIRmjM4FVcMoqu1uWtmJbheAjZb9TiRtw8BCOvFFwutzub7C3lfBJhKJWZYGfnUdlMG0wic1jqOwn9uUngko44oqEWz75kAekxSsjjrYye9tig6VwOHI02%2FxBalDkAVrTjOQCqoke%2BQ8h87YSKmjCp6vVVHThPrfjLjuKl1SIyilT5GC2MnOSCJ4aR01bqFja0iI5lelR0YvBWgSIZQfraJAFzTLR6t83L29SptfWNpJwiBMM%2Bje3cHyVoPd0B0Usxy7myzNrMWFxdt1g8JLg1BDyxFZM%2B5ucuWVZ36Cm11BtldqazZGGcvYWgm96S20648I02spa%2FRsaMH0k0CW8CZSvOjQ%2FXRhFaQpgsJsmLGG8OyHE8ExZV5oCyX1RUqJyisMf3DgTR4iyahdolTQLMiK41dM9QPycYL1Vyo6FrxqyOJP%2BxqHUsqz9YAk%2FKZLvKQP%2BARarV78GTzTHtV6oI4saQEaMtV8DLOD8FV6vxUXSdv9IEiBtNzvdCv%2FGrvKe%2BTZSHMuDmLtV%2F2lntVmspTjPauzN0XJHEQZdMC%2BGyEhjCjuP%2FSBjqkAcY4wdzyJnDQdcklcCHdm485DKvkskwIALfay1z1FjR4LOnVdJBjxmP7OD1%2BJcjFZbVRutoNOFl8WDJzWmXBeV8kIQG%2BCQd7tMTbhkhAbwNmZ7Tyr%2BR%2FLYndFjj9A0qC4WxHUGpk%2BIVfhb8Zw1xYN51StaLsz9wJvWYXBrlm5aK74RIV2Fq47rx9d4TskM7q6fOirkMK16W2aVI2Z%2BLbshxZmLQv&X-Amz-Signature=3618021bf1754dc74152f9d8071ccdfa4c9639b23bc2d466c9b956bdf696bce2&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

那对于一些像集群的优化以及前端的访问优化，比如说你应该把 CSS 放到页面的哪个位置，将 script 放到哪个位置，可以让页面响应更快以及熔断降级等等。


这些部分我们先不考虑，咱主要先看一下从代码层面我们应该注意哪些点，这样的话做到写代码的时候心中有数，往这些点上面去靠，让自己的代码性能更好。那从业务层面这边来分析，要我说咱点不在多，其实两点就够了，只用两点，一个是并行和异步化，另外一个是底层的存储方面的优化，只用叮嘱这两点，同学们大部分业务上面的性能优化其实超不过这两点之外的范围。那咱就先从这个并行和异步化来看一下它总共有哪些方面。


那老师主要把这一个话题分为三个方面，

[image](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/a4bab559-60a4-42e5-82cb-4ae0dc79a685/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WB2W4R7W%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T230737Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDlpVmOHMag9AJwSNodVJC%2Bvn%2F%2F2XpKHPWVHroq6zhXUwIhAPifbSyso6tmSRGm7gpQCr2O%2FI1j%2BaUDmuVIsW6eE2XOKogECMb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1Igx9PLxCung%2FlV4n3VAq3APBnHkLuNqaXBK0cwi3fWYullpE8ohcih%2BAs%2FUgZ2e%2F0Um90g4Je48tEzZrTRyY7tXVGT0vJWfe6%2FZp7AIRmjM4FVcMoqu1uWtmJbheAjZb9TiRtw8BCOvFFwutzub7C3lfBJhKJWZYGfnUdlMG0wic1jqOwn9uUngko44oqEWz75kAekxSsjjrYye9tig6VwOHI02%2FxBalDkAVrTjOQCqoke%2BQ8h87YSKmjCp6vVVHThPrfjLjuKl1SIyilT5GC2MnOSCJ4aR01bqFja0iI5lelR0YvBWgSIZQfraJAFzTLR6t83L29SptfWNpJwiBMM%2Bje3cHyVoPd0B0Usxy7myzNrMWFxdt1g8JLg1BDyxFZM%2B5ucuWVZ36Cm11BtldqazZGGcvYWgm96S20648I02spa%2FRsaMH0k0CW8CZSvOjQ%2FXRhFaQpgsJsmLGG8OyHE8ExZV5oCyX1RUqJyisMf3DgTR4iyahdolTQLMiK41dM9QPycYL1Vyo6FrxqyOJP%2BxqHUsqz9YAk%2FKZLvKQP%2BARarV78GTzTHtV6oI4saQEaMtV8DLOD8FV6vxUXSdv9IEiBtNzvdCv%2FGrvKe%2BTZSHMuDmLtV%2F2lntVmspTjPauzN0XJHEQZdMC%2BGyEhjCjuP%2FSBjqkAcY4wdzyJnDQdcklcCHdm485DKvkskwIALfay1z1FjR4LOnVdJBjxmP7OD1%2BJcjFZbVRutoNOFl8WDJzWmXBeV8kIQG%2BCQd7tMTbhkhAbwNmZ7Tyr%2BR%2FLYndFjj9A0qC4WxHUGpk%2BIVfhb8Zw1xYN51StaLsz9wJvWYXBrlm5aK74RIV2Fq47rx9d4TskM7q6fOirkMK16W2aVI2Z%2BLbshxZmLQv&X-Amz-Signature=9d5063adce9a109e90a4e6b2dc6cb2a1fca0ae1b7f1c33c7303d0b9200a18f49&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

分别是 Future THREAD 还有 MQ ，  future，这里就是指的我们 Java 里面的 future 接口，也就是一个异步执行，在未来执行完之后，你告诉我一个结果，这样的一个通知形式的接口，在一些特定场景中，我们可以使用这种异步化方式加快咱的这个代码的响应时间。


比如说我在商品主搜业务当中，像当年淘系的 open search，它要求你单次返回的这个结果集，它的响应时间要小于 100 毫秒，

[image](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/9ad1dbfa-4c80-4441-af93-f8a8d877abca/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WB2W4R7W%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T230737Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDlpVmOHMag9AJwSNodVJC%2Bvn%2F%2F2XpKHPWVHroq6zhXUwIhAPifbSyso6tmSRGm7gpQCr2O%2FI1j%2BaUDmuVIsW6eE2XOKogECMb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1Igx9PLxCung%2FlV4n3VAq3APBnHkLuNqaXBK0cwi3fWYullpE8ohcih%2BAs%2FUgZ2e%2F0Um90g4Je48tEzZrTRyY7tXVGT0vJWfe6%2FZp7AIRmjM4FVcMoqu1uWtmJbheAjZb9TiRtw8BCOvFFwutzub7C3lfBJhKJWZYGfnUdlMG0wic1jqOwn9uUngko44oqEWz75kAekxSsjjrYye9tig6VwOHI02%2FxBalDkAVrTjOQCqoke%2BQ8h87YSKmjCp6vVVHThPrfjLjuKl1SIyilT5GC2MnOSCJ4aR01bqFja0iI5lelR0YvBWgSIZQfraJAFzTLR6t83L29SptfWNpJwiBMM%2Bje3cHyVoPd0B0Usxy7myzNrMWFxdt1g8JLg1BDyxFZM%2B5ucuWVZ36Cm11BtldqazZGGcvYWgm96S20648I02spa%2FRsaMH0k0CW8CZSvOjQ%2FXRhFaQpgsJsmLGG8OyHE8ExZV5oCyX1RUqJyisMf3DgTR4iyahdolTQLMiK41dM9QPycYL1Vyo6FrxqyOJP%2BxqHUsqz9YAk%2FKZLvKQP%2BARarV78GTzTHtV6oI4saQEaMtV8DLOD8FV6vxUXSdv9IEiBtNzvdCv%2FGrvKe%2BTZSHMuDmLtV%2F2lntVmspTjPauzN0XJHEQZdMC%2BGyEhjCjuP%2FSBjqkAcY4wdzyJnDQdcklcCHdm485DKvkskwIALfay1z1FjR4LOnVdJBjxmP7OD1%2BJcjFZbVRutoNOFl8WDJzWmXBeV8kIQG%2BCQd7tMTbhkhAbwNmZ7Tyr%2BR%2FLYndFjj9A0qC4WxHUGpk%2BIVfhb8Zw1xYN51StaLsz9wJvWYXBrlm5aK74RIV2Fq47rx9d4TskM7q6fOirkMK16W2aVI2Z%2BLbshxZmLQv&X-Amz-Signature=d3fddf02b02188491110389cb16f6c4c7ac16ff40bdd2ae77514c3f40116005a&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

那比如老师这里有一种批量搜索商品的场景，它可能会返回上万条数据，那么在这里我在后台使用的方法就是把这上万条数据分成多个批次，通过 future 的这种机制去同时的发起调用。在所有调用完成的时候，再把它的搜索结果一起打包回来，并且返回给前端。那么在**这种场景下，你所花费的时间其实是这众多 future 接口当中最慢的一次请求调用返回的时间**，它并不是一个线性增加的时间，那这就是利用 future 来平滑你的响应时间的一个业务场景。


除此以外，还有比方说商品搜索列表页的渲染，那你的商品列表页往往它里面有些信息并不在商品中心里，比如说我的库存，那库存需要到另一个库存中心中来获取，那么这里的办法也很容易，我可以去同时请求商品和库存，对吧？那这个处理方法同学们就能猜出来，我可以去同时的请求商品和库存，那在大家去写代码的时候，往往是一种顺序的思想，先拿商品再拿库存。


但是同学们记住，在一些真正的高并发应用当中，

[image](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/04f46356-3c3f-42f9-805c-f27da6aaf474/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WB2W4R7W%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T230737Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDlpVmOHMag9AJwSNodVJC%2Bvn%2F%2F2XpKHPWVHroq6zhXUwIhAPifbSyso6tmSRGm7gpQCr2O%2FI1j%2BaUDmuVIsW6eE2XOKogECMb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1Igx9PLxCung%2FlV4n3VAq3APBnHkLuNqaXBK0cwi3fWYullpE8ohcih%2BAs%2FUgZ2e%2F0Um90g4Je48tEzZrTRyY7tXVGT0vJWfe6%2FZp7AIRmjM4FVcMoqu1uWtmJbheAjZb9TiRtw8BCOvFFwutzub7C3lfBJhKJWZYGfnUdlMG0wic1jqOwn9uUngko44oqEWz75kAekxSsjjrYye9tig6VwOHI02%2FxBalDkAVrTjOQCqoke%2BQ8h87YSKmjCp6vVVHThPrfjLjuKl1SIyilT5GC2MnOSCJ4aR01bqFja0iI5lelR0YvBWgSIZQfraJAFzTLR6t83L29SptfWNpJwiBMM%2Bje3cHyVoPd0B0Usxy7myzNrMWFxdt1g8JLg1BDyxFZM%2B5ucuWVZ36Cm11BtldqazZGGcvYWgm96S20648I02spa%2FRsaMH0k0CW8CZSvOjQ%2FXRhFaQpgsJsmLGG8OyHE8ExZV5oCyX1RUqJyisMf3DgTR4iyahdolTQLMiK41dM9QPycYL1Vyo6FrxqyOJP%2BxqHUsqz9YAk%2FKZLvKQP%2BARarV78GTzTHtV6oI4saQEaMtV8DLOD8FV6vxUXSdv9IEiBtNzvdCv%2FGrvKe%2BTZSHMuDmLtV%2F2lntVmspTjPauzN0XJHEQZdMC%2BGyEhjCjuP%2FSBjqkAcY4wdzyJnDQdcklcCHdm485DKvkskwIALfay1z1FjR4LOnVdJBjxmP7OD1%2BJcjFZbVRutoNOFl8WDJzWmXBeV8kIQG%2BCQd7tMTbhkhAbwNmZ7Tyr%2BR%2FLYndFjj9A0qC4WxHUGpk%2BIVfhb8Zw1xYN51StaLsz9wJvWYXBrlm5aK74RIV2Fq47rx9d4TskM7q6fOirkMK16W2aVI2Z%2BLbshxZmLQv&X-Amz-Signature=2f347f3c2c3de0651ce335748b92c8c7706ef99a4d2a0756535ec62aff9516bc&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

你的接口响应时间如果能把它缩短个哪怕 20，30 毫秒，在这个海量用户访问请求压力的这个加成之下，它对你整个集群所能承载请求的能力都是一个巨大的提升。要记住在能做并发的接口上面，尽量的我们就用并行的方式来处理好，那除此以外，再跟同学们再举个例子，老师做了很长时间的这个商品中心了，那又要扯到商品发布这样的一个话题。那我在商品发布的时候，一个商品它要发布到主搜，要发布到淘系链路，还要去发布到库存中心等等，那这些发布动作其实可以是并行来执行的。那之所以我们要把它做并行，还是基于前面一个原因，你的商品批量发布场景，它所要发布的商品数量真的是非常之大，那商品发布对于一些很大的门店，它往往同一时刻可以发布几十万个商品。


那么如果我们可以把它异步执行，同学们可以想象它所节省下来的时间和服务器资源，那是相当的大的，那我们通过 future 来做这个异步化的时候，同学们要注意一下它的一致性的要求，那往往对于一些弱一致性的场景，使用这种方式其实还是一个不错的选择。比如说你列表页渲染，那你的库存信息没有带出来，有没有影响？对用户的影响是非常少的。那么对于像商品发布这种场景，如果它其中一环发布失败了，那其实这个一致性相对来说影响就会比较大。那么因此我们对于一些非弱一致性的用户场景，如果采用了 future 接口，一定要去设计自己的一个失败处理的策略。比如商品发布当中，其中一环发布失败了，我们是回滚还是去重试这个失败的一环，这都是我们需要来考虑的，那并行和异步化带来的性能提升的同时，也往往会提高自己的异常处理的复杂度，那这是需要同学们去权衡的。


好，那我们再来谈第二个方面， THREAD 开启一个线程，

[image](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/cab560c0-fef8-4706-b2d7-31aa99baaf65/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WB2W4R7W%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T230737Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDlpVmOHMag9AJwSNodVJC%2Bvn%2F%2F2XpKHPWVHroq6zhXUwIhAPifbSyso6tmSRGm7gpQCr2O%2FI1j%2BaUDmuVIsW6eE2XOKogECMb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1Igx9PLxCung%2FlV4n3VAq3APBnHkLuNqaXBK0cwi3fWYullpE8ohcih%2BAs%2FUgZ2e%2F0Um90g4Je48tEzZrTRyY7tXVGT0vJWfe6%2FZp7AIRmjM4FVcMoqu1uWtmJbheAjZb9TiRtw8BCOvFFwutzub7C3lfBJhKJWZYGfnUdlMG0wic1jqOwn9uUngko44oqEWz75kAekxSsjjrYye9tig6VwOHI02%2FxBalDkAVrTjOQCqoke%2BQ8h87YSKmjCp6vVVHThPrfjLjuKl1SIyilT5GC2MnOSCJ4aR01bqFja0iI5lelR0YvBWgSIZQfraJAFzTLR6t83L29SptfWNpJwiBMM%2Bje3cHyVoPd0B0Usxy7myzNrMWFxdt1g8JLg1BDyxFZM%2B5ucuWVZ36Cm11BtldqazZGGcvYWgm96S20648I02spa%2FRsaMH0k0CW8CZSvOjQ%2FXRhFaQpgsJsmLGG8OyHE8ExZV5oCyX1RUqJyisMf3DgTR4iyahdolTQLMiK41dM9QPycYL1Vyo6FrxqyOJP%2BxqHUsqz9YAk%2FKZLvKQP%2BARarV78GTzTHtV6oI4saQEaMtV8DLOD8FV6vxUXSdv9IEiBtNzvdCv%2FGrvKe%2BTZSHMuDmLtV%2F2lntVmspTjPauzN0XJHEQZdMC%2BGyEhjCjuP%2FSBjqkAcY4wdzyJnDQdcklcCHdm485DKvkskwIALfay1z1FjR4LOnVdJBjxmP7OD1%2BJcjFZbVRutoNOFl8WDJzWmXBeV8kIQG%2BCQd7tMTbhkhAbwNmZ7Tyr%2BR%2FLYndFjj9A0qC4WxHUGpk%2BIVfhb8Zw1xYN51StaLsz9wJvWYXBrlm5aK74RIV2Fq47rx9d4TskM7q6fOirkMK16W2aVI2Z%2BLbshxZmLQv&X-Amz-Signature=53349c7dbf921306eb7e7b5950f08b3d031802c5896ea2176ed99c32487dff71&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

这个其实跟 future 有异曲同工之妙，我可以在你业务处理的这个过程当中，本地开启一个线程来处理。同学们觉得这个方法可行不可行，那从功能层面上来说它一定是可行的，没有什么问题。但是我们从另外一个角度来想，你每次执行我在后台开启一个线程，那同学们觉得每次执行方法的时候，我们都开启一个线程，这种方法好不好？那如果不好，它有哪些不好？那当然不好了，还用问吗？哎，我们光明正大的打出这个叉，好，从资源利用率的角度来说，你频繁的去开启关闭一个线程，也不能做到线程复用，其实对你的系统资源都是一种浪费。


那么我们怎么来去改善这种情况？那线程不是你想开就能开，我们使用什么方式让你去使用线程更加悠远？很简单，众人拾柴火焰高，我们可以用 THREAD pull，这里就有一个自愿复用的这样一个角度，比方说你的数据库连接池就是一个 threadpool 的一个很好的应用形式。那再比方，像我们后面微服务阶段，如果使用 high streaks 这样的框架，那我们可以使用线程隔离的方案来去做服务。


容错，那这里后台使用的也是线程池，因此在我们将要开启一个后台线程去处理请求的时候，我们要心中记住，如果能把它作为一个池化，线程池的池化，那么我们尽可能的使用线程池，而不是一个单独的线程。OK，那除此之外，我们还有没有其他的方式？不知道同学们有没有用过 spring 下面的一个注解，叫 SpringAsync 注解，那它通过把这个 Bing 交由 spring 管理，可以去开启一个异步化的这个能力。那相信上这门课的同学应该也有几年工作经验基础，我相信在工作当中肯定是用过 ASYNC 的，没用过也没有关系，是一个非常简单的注解，同学们

### 可以去到 spring 的官方网站上面去学习一下ASYNC，那知道这些小技巧，你们就会在编程的这个微观层面领先你们周围那些 CRUD 只知道顺序执行写业务逻辑的人领先他们了一大步。

```java
@Async注解在Spring中是用于实现异步方法调用的机制，它的底层确实是基于线程池来实现的，但它不是线程池本身。@Async提供了一种简单的方式来将方法标记为异步执行，而无需直接管理线程。

使用方法：

1. 启用异步支持：
   在配置类上添加@EnableAsync注解：

   ```java
   @Configuration
   @EnableAsync
   public class AsyncConfig {
       // 可以在这里自定义线程池配置
   }
   ```

2. 在方法上使用@Async注解：

   ```java
   @Service
   public class MyService {
       @Async
       public void asyncMethod() {
           // 这个方法会异步执行
       }
   }
   ```

3. 对于有返回值的方法，返回类型应该是Future<T>：

   ```java
   @Async
   public Future<String> asyncMethodWithReturn() {
       // 异步处理
       return new AsyncResult<>("result");
   }
   ```

使用场景：

1. 耗时操作：当某个方法执行时间较长，但调用者不需要立即得到结果时。

2. 并行处理：需要同时执行多个独立任务时。

3. 提高响应速度：在Web应用中，可以快速响应请求，而将耗时的处理放在后台进行。

4. 发送通知：如发送邮件、短信等不需要立即响应的操作。

5. 批处理：处理大量数据时，可以将任务分割并异步执行。

6. 定时任务：与@Scheduled结合使用，执行定时任务。

注意事项：

1. 默认情况下，@Async使用SimpleAsyncTaskExecutor，这个执行器每次都会创建新线程。在生产环境中，应该配置自定义的线程池。

2. @Async方法应该在不同的类中被调用，因为Spring使用代理来实现异步调用。

3. 异常处理需要特别注意，因为异步方法的异常不会被调用者直接捕获。

4. 对于有返回值的方法，可以使用CompletableFuture来更灵活地处理异步结果。

总的来说，@Async是一个强大的工具，可以简化异步编程，提高应用性能，但使用时需要考虑线程安全和资源管理等问题。





JDK的线程池：
Java Development Kit (JDK) 提供了几种线程池实现，每种都有其特定的使用场景和特点。以下是 JDK 中提供的线程池实现以及它们的使用场景：

1. **`CachedThreadPool`** (通过 `Executors.newCachedThreadPool()` 创建)
   - 特点：核心线程数为 0，最大线程数为 `Integer.MAX_VALUE`，工作队列是一个 SynchronousQueue。
   - 使用场景：适用于执行大量短期异步任务的场景，可以快速响应外界请求，但不适合执行大量长期运行的任务，因为这可能导致大量的线程同时运行，从而耗尽系统资源。

2. **`FixedThreadPool`** (通过 `Executors.newFixedThreadPool()` 创建)
   - 特点：核心线程数和最大线程数相等，工作队列是一个无界队列。
   - 使用场景：适用于任务执行时间相对固定且需要限制并发数量的场景，例如，控制同时运行的线程数量以避免过多的线程竞争资源。

3. **`SingleThreadExecutor`** (通过 `Executors.newSingleThreadExecutor()` 创建)
   - 特点：只有一个核心线程，工作队列是一个无界队列。
   - 使用场景：适用于需要保证任务顺序执行的场景，例如，当任务之间存在依赖关系或者需要按特定顺序处理时。

4. **`ScheduledThreadPool`** (通过 `Executors.newScheduledThreadPool()` 创建)
   - 特点：支持定时及周期性任务执行，核心线程数可以设置，最大线程数为 `Integer.MAX_VALUE`。
   - 使用场景：适用于需要执行定时任务或周期性任务的场景，例如，定时备份、定时检查等。

5. **`WorkStealingPool`** (通过 `Executors.newWorkStealingPool()` 创建)
   - 特点：由多个固定大小的线程池组成，每个线程池都有自己的队列，线程可以“偷取”其他线程池的任务来执行。
   - 使用场景：适用于工作负载不均匀或存在大量并发任务的场景，可以提高资源利用率和吞吐量。

6. **`ForkJoinPool`** (通过 `ForkJoinPool` 构造函数创建)
   - 特点：专为工作窃取算法设计，适用于可以分而治之的任务，如大数据处理、递归操作等。
   - 使用场景：适用于可分解为多个子任务并行处理的场景，例如，大规模并行计算和递归任务。

每种线程池都有其优势和限制，选择合适的线程池需要根据任务特性、预期的并发级别以及资源限制等因素进行综合考虑。在实际应用中，开发者可能需要根据具体需求调整线程池参数，或者自定义线程池实现以满足特定的性能要求。
```


OK，那这就是 THREAD 的一个考虑的方向，


剩下一个MQ。

[image](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/33b75e8b-9c97-4332-bcd7-1575891feaf1/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WB2W4R7W%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T230737Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDlpVmOHMag9AJwSNodVJC%2Bvn%2F%2F2XpKHPWVHroq6zhXUwIhAPifbSyso6tmSRGm7gpQCr2O%2FI1j%2BaUDmuVIsW6eE2XOKogECMb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1Igx9PLxCung%2FlV4n3VAq3APBnHkLuNqaXBK0cwi3fWYullpE8ohcih%2BAs%2FUgZ2e%2F0Um90g4Je48tEzZrTRyY7tXVGT0vJWfe6%2FZp7AIRmjM4FVcMoqu1uWtmJbheAjZb9TiRtw8BCOvFFwutzub7C3lfBJhKJWZYGfnUdlMG0wic1jqOwn9uUngko44oqEWz75kAekxSsjjrYye9tig6VwOHI02%2FxBalDkAVrTjOQCqoke%2BQ8h87YSKmjCp6vVVHThPrfjLjuKl1SIyilT5GC2MnOSCJ4aR01bqFja0iI5lelR0YvBWgSIZQfraJAFzTLR6t83L29SptfWNpJwiBMM%2Bje3cHyVoPd0B0Usxy7myzNrMWFxdt1g8JLg1BDyxFZM%2B5ucuWVZ36Cm11BtldqazZGGcvYWgm96S20648I02spa%2FRsaMH0k0CW8CZSvOjQ%2FXRhFaQpgsJsmLGG8OyHE8ExZV5oCyX1RUqJyisMf3DgTR4iyahdolTQLMiK41dM9QPycYL1Vyo6FrxqyOJP%2BxqHUsqz9YAk%2FKZLvKQP%2BARarV78GTzTHtV6oI4saQEaMtV8DLOD8FV6vxUXSdv9IEiBtNzvdCv%2FGrvKe%2BTZSHMuDmLtV%2F2lntVmspTjPauzN0XJHEQZdMC%2BGyEhjCjuP%2FSBjqkAcY4wdzyJnDQdcklcCHdm485DKvkskwIALfay1z1FjR4LOnVdJBjxmP7OD1%2BJcjFZbVRutoNOFl8WDJzWmXBeV8kIQG%2BCQd7tMTbhkhAbwNmZ7Tyr%2BR%2FLYndFjj9A0qC4WxHUGpk%2BIVfhb8Zw1xYN51StaLsz9wJvWYXBrlm5aK74RIV2Fq47rx9d4TskM7q6fOirkMK16W2aVI2Z%2BLbshxZmLQv&X-Amz-Signature=46123843f01bd2d47fb22f343cd5f938037c6a9c3fc861e668ee3645e6c2999e&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

只不过在使用 MQ 的时候，同学们要注意两点，一个是如何使用利用 MQ 的一个事物化的消息，将发送 MQ 的这个动作和你当前代码执行这两步绑定成一个原子操作，那这是发送事务型消息。


还有一个就是当你考虑使用 MQ 做并行异步化的时候，我们往往要记住这个场景通常是一个可靠性要求比较高的场景，因此我们用到了MQ，那这个情况下如果出现了异常，务必记住设置自己的 error handling 的策略，也就是异常容错的这个策略。


okay，那以上的三个方向是我们从并行异步化的方向来考虑复杂业务的性能优化的出发点。那除了这个以外，我们还可以从一个存储的方向，存储的方向非常简单，无非就是两点，第一个上缓存，我们可以使用分布式缓存或者是本地缓存，以及前面老师跟同学们去讲过专门开了一节来跟同学们讲的热点缓存的处理方案。

[image](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/127ab646-cd23-4e58-83b1-1520c1304bd0/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WB2W4R7W%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T230737Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDlpVmOHMag9AJwSNodVJC%2Bvn%2F%2F2XpKHPWVHroq6zhXUwIhAPifbSyso6tmSRGm7gpQCr2O%2FI1j%2BaUDmuVIsW6eE2XOKogECMb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1Igx9PLxCung%2FlV4n3VAq3APBnHkLuNqaXBK0cwi3fWYullpE8ohcih%2BAs%2FUgZ2e%2F0Um90g4Je48tEzZrTRyY7tXVGT0vJWfe6%2FZp7AIRmjM4FVcMoqu1uWtmJbheAjZb9TiRtw8BCOvFFwutzub7C3lfBJhKJWZYGfnUdlMG0wic1jqOwn9uUngko44oqEWz75kAekxSsjjrYye9tig6VwOHI02%2FxBalDkAVrTjOQCqoke%2BQ8h87YSKmjCp6vVVHThPrfjLjuKl1SIyilT5GC2MnOSCJ4aR01bqFja0iI5lelR0YvBWgSIZQfraJAFzTLR6t83L29SptfWNpJwiBMM%2Bje3cHyVoPd0B0Usxy7myzNrMWFxdt1g8JLg1BDyxFZM%2B5ucuWVZ36Cm11BtldqazZGGcvYWgm96S20648I02spa%2FRsaMH0k0CW8CZSvOjQ%2FXRhFaQpgsJsmLGG8OyHE8ExZV5oCyX1RUqJyisMf3DgTR4iyahdolTQLMiK41dM9QPycYL1Vyo6FrxqyOJP%2BxqHUsqz9YAk%2FKZLvKQP%2BARarV78GTzTHtV6oI4saQEaMtV8DLOD8FV6vxUXSdv9IEiBtNzvdCv%2FGrvKe%2BTZSHMuDmLtV%2F2lntVmspTjPauzN0XJHEQZdMC%2BGyEhjCjuP%2FSBjqkAcY4wdzyJnDQdcklcCHdm485DKvkskwIALfay1z1FjR4LOnVdJBjxmP7OD1%2BJcjFZbVRutoNOFl8WDJzWmXBeV8kIQG%2BCQd7tMTbhkhAbwNmZ7Tyr%2BR%2FLYndFjj9A0qC4WxHUGpk%2BIVfhb8Zw1xYN51StaLsz9wJvWYXBrlm5aK74RIV2Fq47rx9d4TskM7q6fOirkMK16W2aVI2Z%2BLbshxZmLQv&X-Amz-Signature=8d263375b6453498eb5a2af67cd66c98cb5d56aa4639389404c8c48df44bcb56&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

咱通过这几个方式将你的访问请求从底层最薄弱的数据库，把它往上升到缓存层面，或者是 ES 等等这样的搜索引擎的层面。那这个知识点就和前面咱的这些热点数据的分析等等串联起来了。所以学习知识，一个知识往往会跟其他的很多的知识点相串联起来，如果同学们能从这个课程当中把前后所有章节的知识串联成一个网状结构，那就是一个词叫触类旁通。这时候你会发现自己去吸纳新知识，吸纳新的技术方案，或者从自己的知识库当中想到一个未知问题的解决方法，都变得非常非常的容易。这个方法就叫把自己已有的知识串联成网，而不让它成为一个个的单点，这是从这一点发散出来的一个小心得。


好，我们再回来看看这个存储上面，从数据库层面我们的优化策略还有哪些，比如说我们可以做一些数据异构，还有数据冗余，那这种方式可以帮助我们去做更好的查询的优化，比如说从不同的维度来做分库分表，前面老师也讲过了，同学们可以去复习一下。以及对于一些慢SQL，我们可以做一些 SQL 的调优，或者使用一些 hints 来强制使你的 SQL 走相应的索引，这些都是大家可以去思考的点。其中我个人认为相对来说比较复杂的是你如何去设计一套数据异构的方案，那么这一点也可以使用老师前面跟同学们分享的 Canal 的增量数据仪式来构建自己的异构系统。


还有另一个比较复杂的方向是 SQL 的调优，这一块完全是一个经验火，经验加运气的火，需要大家去在平时的工作过程当中不断的积累，去了解你 SQL 的一些调优的技巧，以及你对应数据库它的执行策略当中有哪些索引策略，这些索引策略的优劣以及它底层的数据结构是如何来支持实现它的？那这个就需要同学们注意，在平时的过程当中，工作过程里**多积累，多学习，多沉淀自己的经验，把所有解决复杂问题、疑难杂症的经验都把它固化下来，成为自己以后解决此类问题的一个经验和依据。**OK，同学们，那咱这一节解决复杂问题性能优化的一些角度，还有性能指标这个内容就跟大家分享到这里了。在下一节当中，我们简单的跟同学们去理一下咱们的性能测试的一些方法手段，同学们，我们下一小节再见。


