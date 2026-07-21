---
title: 1-4 Hystrix体系架构和核心功能解析
---

# 1-4 Hystrix体系架构和核心功能解析

[image](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/2f5ad5a7-ec1b-4f26-8b01-369767ea6fa5/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QEWQ2MPT%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T225634Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCGjIuBcXsfUCYslINt0%2BknoeiWQdHLu7F0knxTQcZVcQIhAJvw51Eid7%2FanK6zlKl6TZeCKBm2BNcZ7LRPwqhL6jFgKogECMb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgyRU772ISBDWq52MBoq3APGmIWelD5g%2BS9Oz0bjPs6g5%2BpmovvlKU3GHr2uFyk80mZQNdRQMQwu2oXFcevbviHYwL%2FjY4loQAq2E9F4PUnv%2Fky0NYVKN%2FJt66mLaw%2Few930mBCyUCyrPdnzRn9V9p7alPNKVT5n%2F6I5Dh7m9U0CE35s1SVhP%2FHb4%2FoE0dCeIb0i8mtWZuPm%2BlBAwyajHDWRj2ozFDKc16GFE%2BzgODlKO%2FcRboMNXiKpVUHEtCFqT8kbkWrLaPTpveSxwfAiN92CIXcVoX9argKwxU0gZxuAIth%2BOLqQq2AyKTOlPS7dzU%2FpLmcBXWRQ%2FxJziJXiqKfzIrVFyeJKA%2F5jjd8ziwVGoUWk7jGgfKnlyvkQNN9%2FoUv16eCTHJ%2FqJR1vsj8gH53XEWTb%2FiObZfHWRh1gde7h%2FDyW7l0KNRxLuCrvCCuuDjX9IF4AXN0NtijKE3UGVrYIm5Vh7MiJAyBt%2F%2FfZDYR4uXkWb%2FbzLvK7btGUNMeXBqwe1RZptJlOzAgHlHsdXF3m%2F1p5CCz1C%2BLC%2FSS17x381POI7ZGn%2BJPvichPWOrQOwaMD9kZSH7FXe6txKV50D0kjfoCpiNAzaLBQC4%2F6oItbchfX3yMy%2BBUl6ETZl6L2jHtcdCEAGg7rdeOjDDLt%2F%2FSBjqkAZiK5viq2KqIb%2FfY7QI848bTfXVKEXkNGArdxbezbwLHW6ndnKRxn8npblJMpfiRRA44PYZ6Sr16GD%2FQ5VBaoz5AeydQM92%2Fs64xyS9Ut2oCa3Qj11CDV2D6kCRwlyblTGHDLi7IHGbc%2FCSBEMn8Em62g84DsuL2wnClDsGzAIFZxqLrzr3T7sOMjCRsIJb7mNzUDUXMcBHoLMRBTr5ijhOIlPxn&X-Amz-Signature=63347b42a42d75f0a2ec483605cbd552576baef216556eac71bc6a0417c4fc31&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

[image](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/726b58a2-eaf1-48a9-b7fb-823ad7082c8f/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QEWQ2MPT%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T225634Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCGjIuBcXsfUCYslINt0%2BknoeiWQdHLu7F0knxTQcZVcQIhAJvw51Eid7%2FanK6zlKl6TZeCKBm2BNcZ7LRPwqhL6jFgKogECMb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgyRU772ISBDWq52MBoq3APGmIWelD5g%2BS9Oz0bjPs6g5%2BpmovvlKU3GHr2uFyk80mZQNdRQMQwu2oXFcevbviHYwL%2FjY4loQAq2E9F4PUnv%2Fky0NYVKN%2FJt66mLaw%2Few930mBCyUCyrPdnzRn9V9p7alPNKVT5n%2F6I5Dh7m9U0CE35s1SVhP%2FHb4%2FoE0dCeIb0i8mtWZuPm%2BlBAwyajHDWRj2ozFDKc16GFE%2BzgODlKO%2FcRboMNXiKpVUHEtCFqT8kbkWrLaPTpveSxwfAiN92CIXcVoX9argKwxU0gZxuAIth%2BOLqQq2AyKTOlPS7dzU%2FpLmcBXWRQ%2FxJziJXiqKfzIrVFyeJKA%2F5jjd8ziwVGoUWk7jGgfKnlyvkQNN9%2FoUv16eCTHJ%2FqJR1vsj8gH53XEWTb%2FiObZfHWRh1gde7h%2FDyW7l0KNRxLuCrvCCuuDjX9IF4AXN0NtijKE3UGVrYIm5Vh7MiJAyBt%2F%2FfZDYR4uXkWb%2FbzLvK7btGUNMeXBqwe1RZptJlOzAgHlHsdXF3m%2F1p5CCz1C%2BLC%2FSS17x381POI7ZGn%2BJPvichPWOrQOwaMD9kZSH7FXe6txKV50D0kjfoCpiNAzaLBQC4%2F6oItbchfX3yMy%2BBUl6ETZl6L2jHtcdCEAGg7rdeOjDDLt%2F%2FSBjqkAZiK5viq2KqIb%2FfY7QI848bTfXVKEXkNGArdxbezbwLHW6ndnKRxn8npblJMpfiRRA44PYZ6Sr16GD%2FQ5VBaoz5AeydQM92%2Fs64xyS9Ut2oCa3Qj11CDV2D6kCRwlyblTGHDLi7IHGbc%2FCSBEMn8Em62g84DsuL2wnClDsGzAIFZxqLrzr3T7sOMjCRsIJb7mNzUDUXMcBHoLMRBTr5ijhOIlPxn&X-Amz-Signature=6e33131b8093afb7bb8bafe8c93f56e8fea2d94bae25774f721c12222d07b329&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

1—4_Hystrix体系架构和核心功能解析
上一节我们了解了服务容错的应用领域，它可以防止服务雪崩离异常服务）提供降级服务方案。那我们今天就来了解一下SpringCloud是如何借助Hystrix做到服务容错的。
断舍离
《断舍离》，是日本作家山下英子的著作，这本书传达了一种生活 理念。断=不买、不收取不需要的东西。舍=处理掉堆放在家里没用 的东西。离=舍弃对物质的迷恋，让自己处于宽敞舒适，自由自在 的空间。
对过往不迷恋，拿得起放得下，这样的生活哲学确实可以帮助人们 度过一些困难时期。我们知道Hystrix也是为了帮服务节点度过他们 的困难时期（缓解异常、雪崩带来的影响） ，它也有同样一套佛系 的设计理念，分别对应Hystrix中三个特色功能

1. 断 - 熔断
1. 舍 — 降级
1. 离-线程隔离
那就让我们倒杯茶，细细品味Hystrix“断·舍·离”的智慧。
P.S.降级和熔断的具体应用场景和作用机制，我们会在对应小节深入探讨
服务降级—舍得
无端拜失仪，放弃令自新
                                                                                           — 宋·苏轼
微服务架构强调高可用，但并非高一致性，在一致性方面远比不上 银行的大型机系统。也就是说，在且常服务调用阶段会出现一系列 的调用异常，最常见的就是服务下线。举个例子重启服务节点的 时候，服务下线指令发送到注册中心后，这时还没来得及通过服务 发现机制同步到客户端，因此某些服务调用请求依然会发送到这台 机器，但由于服务已经下线，最终调用方只能无功而返。404 NotFound。


再举一个破坏力更大的例子。前面我们讲到了服务的雪崩效应，大 家可能只听说过缓存雪崩 其实雪崩效应不仅仅针对缓存，它更大 的危害是在大规模分布式应用上。我们举一个真实的案例，电商系 统很多模块都依赖营销优惠服务 比如商品详情页、搜索列表页、 购物车页和下单页面都依赖营销服务来计算优惠价格、因此这个服 务承载的负载压力可谓非常之高（老师经常和阿里井享事业部的营 销平台团队打交道，了解到这块服务的承压可以排在淘系全链路to p5）。我们设想，假如这个服务出现了异常，导致响应超时，那么 所有依赖它的下游系统的响应时间都会被拉长，这就引发了一个滚 雪球的雪崩效应，由最上游的系统问题，引发了一系列下游系统响 应超时，最终导致整个系统被拖垮。

[image](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/af6cb1dd-e790-4285-86f1-ae800c76635e/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QEWQ2MPT%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T225634Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCGjIuBcXsfUCYslINt0%2BknoeiWQdHLu7F0knxTQcZVcQIhAJvw51Eid7%2FanK6zlKl6TZeCKBm2BNcZ7LRPwqhL6jFgKogECMb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgyRU772ISBDWq52MBoq3APGmIWelD5g%2BS9Oz0bjPs6g5%2BpmovvlKU3GHr2uFyk80mZQNdRQMQwu2oXFcevbviHYwL%2FjY4loQAq2E9F4PUnv%2Fky0NYVKN%2FJt66mLaw%2Few930mBCyUCyrPdnzRn9V9p7alPNKVT5n%2F6I5Dh7m9U0CE35s1SVhP%2FHb4%2FoE0dCeIb0i8mtWZuPm%2BlBAwyajHDWRj2ozFDKc16GFE%2BzgODlKO%2FcRboMNXiKpVUHEtCFqT8kbkWrLaPTpveSxwfAiN92CIXcVoX9argKwxU0gZxuAIth%2BOLqQq2AyKTOlPS7dzU%2FpLmcBXWRQ%2FxJziJXiqKfzIrVFyeJKA%2F5jjd8ziwVGoUWk7jGgfKnlyvkQNN9%2FoUv16eCTHJ%2FqJR1vsj8gH53XEWTb%2FiObZfHWRh1gde7h%2FDyW7l0KNRxLuCrvCCuuDjX9IF4AXN0NtijKE3UGVrYIm5Vh7MiJAyBt%2F%2FfZDYR4uXkWb%2FbzLvK7btGUNMeXBqwe1RZptJlOzAgHlHsdXF3m%2F1p5CCz1C%2BLC%2FSS17x381POI7ZGn%2BJPvichPWOrQOwaMD9kZSH7FXe6txKV50D0kjfoCpiNAzaLBQC4%2F6oItbchfX3yMy%2BBUl6ETZl6L2jHtcdCEAGg7rdeOjDDLt%2F%2FSBjqkAZiK5viq2KqIb%2FfY7QI848bTfXVKEXkNGArdxbezbwLHW6ndnKRxn8npblJMpfiRRA44PYZ6Sr16GD%2FQ5VBaoz5AeydQM92%2Fs64xyS9Ut2oCa3Qj11CDV2D6kCRwlyblTGHDLi7IHGbc%2FCSBEMn8Em62g84DsuL2wnClDsGzAIFZxqLrzr3T7sOMjCRsIJb7mNzUDUXMcBHoLMRBTr5ijhOIlPxn&X-Amz-Signature=408f14279faafbea601f313665b7441bab1d2c70b21619de8824b865a4f3fdcf&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

服务降级用来应对上面的几种情况再合适不过了，假如HystrixClie nt调用目标请求的时候发生异常（exception），这时Hystrix会自动 把这个请求转发到降级逻辑中，由服务调用方来编写异常处理逻辑 。对响应超时的场景来说，我们可以通过配置Hystrix的超时等待时 间（和Ribbon的timeout是两个不同配置），把超时响应的服务调用
也当做是异常情况，转发到fallback逻辑中进行处理。
服务熔断
天门中断楚江开，碧水东流至此回
                                                                                                                                   — 唐·李白
服务熔断是建立在服务降级之上的一个异常处理措施你可以将它看做是服务降级的升级版。服务降级需要等待HTTP请求从服务节 点返回异常或超时，再转向fallback逻辑，但是服务熔断引入了一种叫“断路器/熔断器”的机制，当断路器打开的时候，对服务的调用请求不会发送到目标服务节点，直接转向fallback逻辑。

[image](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/062490e0-07bb-4942-b0c7-989599d64a04/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QEWQ2MPT%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T225634Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCGjIuBcXsfUCYslINt0%2BknoeiWQdHLu7F0knxTQcZVcQIhAJvw51Eid7%2FanK6zlKl6TZeCKBm2BNcZ7LRPwqhL6jFgKogECMb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgyRU772ISBDWq52MBoq3APGmIWelD5g%2BS9Oz0bjPs6g5%2BpmovvlKU3GHr2uFyk80mZQNdRQMQwu2oXFcevbviHYwL%2FjY4loQAq2E9F4PUnv%2Fky0NYVKN%2FJt66mLaw%2Few930mBCyUCyrPdnzRn9V9p7alPNKVT5n%2F6I5Dh7m9U0CE35s1SVhP%2FHb4%2FoE0dCeIb0i8mtWZuPm%2BlBAwyajHDWRj2ozFDKc16GFE%2BzgODlKO%2FcRboMNXiKpVUHEtCFqT8kbkWrLaPTpveSxwfAiN92CIXcVoX9argKwxU0gZxuAIth%2BOLqQq2AyKTOlPS7dzU%2FpLmcBXWRQ%2FxJziJXiqKfzIrVFyeJKA%2F5jjd8ziwVGoUWk7jGgfKnlyvkQNN9%2FoUv16eCTHJ%2FqJR1vsj8gH53XEWTb%2FiObZfHWRh1gde7h%2FDyW7l0KNRxLuCrvCCuuDjX9IF4AXN0NtijKE3UGVrYIm5Vh7MiJAyBt%2F%2FfZDYR4uXkWb%2FbzLvK7btGUNMeXBqwe1RZptJlOzAgHlHsdXF3m%2F1p5CCz1C%2BLC%2FSS17x381POI7ZGn%2BJPvichPWOrQOwaMD9kZSH7FXe6txKV50D0kjfoCpiNAzaLBQC4%2F6oItbchfX3yMy%2BBUl6ETZl6L2jHtcdCEAGg7rdeOjDDLt%2F%2FSBjqkAZiK5viq2KqIb%2FfY7QI848bTfXVKEXkNGArdxbezbwLHW6ndnKRxn8npblJMpfiRRA44PYZ6Sr16GD%2FQ5VBaoz5AeydQM92%2Fs64xyS9Ut2oCa3Qj11CDV2D6kCRwlyblTGHDLi7IHGbc%2FCSBEMn8Em62g84DsuL2wnClDsGzAIFZxqLrzr3T7sOMjCRsIJb7mNzUDUXMcBHoLMRBTr5ijhOIlPxn&X-Amz-Signature=f0ef78433d268ab64c09e6e4aaf19b33b181604474286ff0fc0c4b17c8f57f9b&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

断路器的打开/关闭有很多的判断标准，我们在服务熔断小节里再 深入探讨。（好吧，这里我先剧透一点好了（比如我们可以这样设 置：每10个请求，失败数量达到8个的时候扛开断路器）。


同学可能会问了，假如断路器打开之后，就这么一直开着吗？当然 不是了，一直开着多浪费电啊。服务一时失败，不代表一直失败，Hystrix也有一些配置规则，会主动去判断断路器关闭的时机。在后续章节，我们再来深入学习断路器的状态流转过程，我会带大家通过Turbine监控大盘、查看Hystrix断路器的开启关闭。



断路器可以显著缓解由QPS （Query Per Second，每秒访问请求，用来衡量系统当前压力激增导致的雪崩效应，由于断路器打开后， 请求直接转向fallback而不会发起服务调用服务的系统压力。因此会大幅降低承压
线程隔离
明日隔山岳，世事两茫茫
                                                                                                               -唐·杜甫


[image](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/d4c6b263-3f67-4164-94e3-9ca63ee920f9/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QEWQ2MPT%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T225634Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCGjIuBcXsfUCYslINt0%2BknoeiWQdHLu7F0knxTQcZVcQIhAJvw51Eid7%2FanK6zlKl6TZeCKBm2BNcZ7LRPwqhL6jFgKogECMb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgyRU772ISBDWq52MBoq3APGmIWelD5g%2BS9Oz0bjPs6g5%2BpmovvlKU3GHr2uFyk80mZQNdRQMQwu2oXFcevbviHYwL%2FjY4loQAq2E9F4PUnv%2Fky0NYVKN%2FJt66mLaw%2Few930mBCyUCyrPdnzRn9V9p7alPNKVT5n%2F6I5Dh7m9U0CE35s1SVhP%2FHb4%2FoE0dCeIb0i8mtWZuPm%2BlBAwyajHDWRj2ozFDKc16GFE%2BzgODlKO%2FcRboMNXiKpVUHEtCFqT8kbkWrLaPTpveSxwfAiN92CIXcVoX9argKwxU0gZxuAIth%2BOLqQq2AyKTOlPS7dzU%2FpLmcBXWRQ%2FxJziJXiqKfzIrVFyeJKA%2F5jjd8ziwVGoUWk7jGgfKnlyvkQNN9%2FoUv16eCTHJ%2FqJR1vsj8gH53XEWTb%2FiObZfHWRh1gde7h%2FDyW7l0KNRxLuCrvCCuuDjX9IF4AXN0NtijKE3UGVrYIm5Vh7MiJAyBt%2F%2FfZDYR4uXkWb%2FbzLvK7btGUNMeXBqwe1RZptJlOzAgHlHsdXF3m%2F1p5CCz1C%2BLC%2FSS17x381POI7ZGn%2BJPvichPWOrQOwaMD9kZSH7FXe6txKV50D0kjfoCpiNAzaLBQC4%2F6oItbchfX3yMy%2BBUl6ETZl6L2jHtcdCEAGg7rdeOjDDLt%2F%2FSBjqkAZiK5viq2KqIb%2FfY7QI848bTfXVKEXkNGArdxbezbwLHW6ndnKRxn8npblJMpfiRRA44PYZ6Sr16GD%2FQ5VBaoz5AeydQM92%2Fs64xyS9Ut2oCa3Qj11CDV2D6kCRwlyblTGHDLi7IHGbc%2FCSBEMn8Em62g84DsuL2wnClDsGzAIFZxqLrzr3T7sOMjCRsIJb7mNzUDUXMcBHoLMRBTr5ijhOIlPxn&X-Amz-Signature=82bb8df36deb8e0e7d637693f8add54405144e6e19f11b9f910bc3e38e6d86cc&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)


大家知道Web容器通常有一个线程池来接待来访请求，如果并发量 过高，线程池被打满了就会影响后面请求的响应。在我们应用内部 ，假如我们提供了3个微服务，分别是A. B. C.如果请求A服务 的调用量过多）我们会发现所有可用线程都会逐渐被ServiceA占用，接下来的现象就是服务B和服务C没有系统资源可供调用


Hystrix通过线程隔离的方案，将执行服务调用的代码与容器本身的线程池（比如tomcat thread pool）进行隔离，我们可以配置每个服务所需线程的最大数量，这样一来，即便一个服务的线程池被吃满 ，也不会影响其他服务。


与线程隔离相类似的还有信号量”技术，稍后的小节我们会对两个 技术做一番对比，看看这两个技术方案适合在哪些业务场景里应用


老师最近想了一个问题，我们上这门课程其实不是为了学一套百科 全书更重要的是提炼一套适合自己的学习方法。通过前面几个大 章节的学习，想必同学们对从0开始学习开源项目有了一些小心得 。那么这次就给大家一个试炼的机会，希望同学们使用自己领悟的 方法也好，学到的方法也好，总之，八仙过海各显神通，自己做一 “Hystrix线程隔离”的小demo（后面会涉及线程隔离的核心流程， 但落地的部分就需要同学们自己摸索了）。老师丕建议大家直接搜 索别人写好的示例程序，可以试着通过SpringCloud官网提供的英文 文档，加上阅读Hystrix源码完成这个小demo，这才是锻炼“Hands—o n”能力的正确打开方式。
小结
学习Tips：很多时候我们学习技术就是通过搜索引擎，搜索别人已 经实现的例子，然后copy过来。其实这是一个有些急功近利的学习 方式，尽管能快速见效、但也只是停留在“会用”的阶段。如果大家 时间比较充足，并且想系统的学习一门技术，可以尝试从官方的文 档开始利用开源社区的资料加上阅读源码深入了解一个技术的 方方面面。从我个人经验来讲、国外的开源社区和stackoverflow这 类网站都可以提供很好的帮助，国外技术圈并不像国内这般浮躁， 很多社区大牛也非常有奉献精神，大家没事可以经常去逛一逛这些 社区、看看别人提出的问题，如果有你可以解答的问题也不妨去尝 试解决一下。



这一节带大家了解Hystrix的主要功能，下一节我们去看一下Hystrix 的服务降级是怎么一回事儿。

[image](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/ccd4679c-f6eb-4a3d-b71c-150f55cd91b8/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QEWQ2MPT%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T225634Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCGjIuBcXsfUCYslINt0%2BknoeiWQdHLu7F0knxTQcZVcQIhAJvw51Eid7%2FanK6zlKl6TZeCKBm2BNcZ7LRPwqhL6jFgKogECMb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgyRU772ISBDWq52MBoq3APGmIWelD5g%2BS9Oz0bjPs6g5%2BpmovvlKU3GHr2uFyk80mZQNdRQMQwu2oXFcevbviHYwL%2FjY4loQAq2E9F4PUnv%2Fky0NYVKN%2FJt66mLaw%2Few930mBCyUCyrPdnzRn9V9p7alPNKVT5n%2F6I5Dh7m9U0CE35s1SVhP%2FHb4%2FoE0dCeIb0i8mtWZuPm%2BlBAwyajHDWRj2ozFDKc16GFE%2BzgODlKO%2FcRboMNXiKpVUHEtCFqT8kbkWrLaPTpveSxwfAiN92CIXcVoX9argKwxU0gZxuAIth%2BOLqQq2AyKTOlPS7dzU%2FpLmcBXWRQ%2FxJziJXiqKfzIrVFyeJKA%2F5jjd8ziwVGoUWk7jGgfKnlyvkQNN9%2FoUv16eCTHJ%2FqJR1vsj8gH53XEWTb%2FiObZfHWRh1gde7h%2FDyW7l0KNRxLuCrvCCuuDjX9IF4AXN0NtijKE3UGVrYIm5Vh7MiJAyBt%2F%2FfZDYR4uXkWb%2FbzLvK7btGUNMeXBqwe1RZptJlOzAgHlHsdXF3m%2F1p5CCz1C%2BLC%2FSS17x381POI7ZGn%2BJPvichPWOrQOwaMD9kZSH7FXe6txKV50D0kjfoCpiNAzaLBQC4%2F6oItbchfX3yMy%2BBUl6ETZl6L2jHtcdCEAGg7rdeOjDDLt%2F%2FSBjqkAZiK5viq2KqIb%2FfY7QI848bTfXVKEXkNGArdxbezbwLHW6ndnKRxn8npblJMpfiRRA44PYZ6Sr16GD%2FQ5VBaoz5AeydQM92%2Fs64xyS9Ut2oCa3Qj11CDV2D6kCRwlyblTGHDLi7IHGbc%2FCSBEMn8Em62g84DsuL2wnClDsGzAIFZxqLrzr3T7sOMjCRsIJb7mNzUDUXMcBHoLMRBTr5ijhOIlPxn&X-Amz-Signature=7a81025c022de583dde1bb3ed8aebaecb89675c5962f563a3f73c34aa072300c&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)


