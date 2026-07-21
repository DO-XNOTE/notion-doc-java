---
title: 2-8 如何解决业务接口高RT的情况-异步编排
---

# 2-8 如何解决业务接口高RT的情况-异步编排

[image](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/08093911-d12f-4669-9898-dc8d65dea7b7/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466Y7B67OOT%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T230646Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDOt%2B4AhWQLfm6hNSC%2B0p2%2BqosUqUa8b6KZv6JjKHsp5QIgI1lqQjhFtl6nC0qLKxNDtsP2tm%2FQkHLFrnS3bv9m2JIqiAQIxv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDKkcBfBL%2BtyfsiUeHCrcA5Zj%2FKFvb5R885%2FRCZzcnKK%2FC3cr3vJtBKW82gIJ%2BF%2BniTSjJQ3848bqDBAgBdvjJIWMUB90yrvCclLc6USXadn9hWTM%2BnhI%2F1ICqe07b5F8X85gnFVnpA0b7wt6Y%2FJOEN1C1lSjbwu%2Bf8R4V5I3k7uQ93wEUQl8lYrVqffskcJfeOgcTWbh9YQF1A%2BcBLGpIKuxUoPXi74ghR3pHkk9LXSdXWA%2BcqYSOuX5bqIDiOnsGHvnWsJ2GrGaB9SJrYa0LUc1S7%2FSjzum8Rtg%2FByaQk4nxkPXm9m90mGoDxdEMrWDtNTbEPw1%2Bb6b5e7jz5fpH9GO8uxmHDz1aCk%2Fu37135JKRtWejGsihGkTJvSdiTM8MGVOlPy3TIA%2BTvMBNLlccEJ4y8r6eyEKyfYSXS7uz4w8igubD3xwgZb1Y%2FgorEmR1ZPRg2FH1M1wiwWx9PZgYocMpNcqGh%2BmhAG85nvBOrD48Utpyt51Vm3K6z3o6PrXWGNN8myvIF90S7kLAI2F1sci4%2BPuhSJYP9dy7%2BeP9Yz9rS4xLwwYR6Fnep92taRbtW%2Fpe3Leqj8JFZfVPZR4ZCayvOd%2BH2WAS5cX%2FKD3Zr7ii3idvPu6Q5cH45rK4YaOZ4R%2F3%2FP7B26Xl6LrMK%2B3%2F9IGOqUBxdc0Xbw1%2Ft2uFs7gQkVt0QYqLkQVbN1VkRw%2B3ejU%2FWb3ctRqSQjv8w%2F3A5F9YLWm4T9uDQqMnlA2tAMANHkCh0dSs9maQMRwSdUm%2Fv3H9R1NRcDRHOrqvV2oljyyFNvvWd%2BbwdRhHk%2BeBDQFhJkGXV2aJMCwbz9hN4b3BoGjj728aVlIpks8oLLkRNCMW0crr7iA7S7zSqwPwPFnNIXPrrt50SxA&X-Amz-Signature=07f8b9e2faf345a27095c1080b87d782f7adfc55795798042387bfa4e5fb1793&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

hello，幕后网的各位同学们大家好，我是姚半仙，咱前面一节讲了如何使用 future 还有 callback 实现接口的异步化。那么这一节里我们继续这个话题，看一看如何利用原生态的 JDK 里面的功能，帮我们实现异步编排。

[image](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/0ed529f4-5afe-489d-a9af-ceffe1d3c5a8/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466Y7B67OOT%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T230646Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDOt%2B4AhWQLfm6hNSC%2B0p2%2BqosUqUa8b6KZv6JjKHsp5QIgI1lqQjhFtl6nC0qLKxNDtsP2tm%2FQkHLFrnS3bv9m2JIqiAQIxv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDKkcBfBL%2BtyfsiUeHCrcA5Zj%2FKFvb5R885%2FRCZzcnKK%2FC3cr3vJtBKW82gIJ%2BF%2BniTSjJQ3848bqDBAgBdvjJIWMUB90yrvCclLc6USXadn9hWTM%2BnhI%2F1ICqe07b5F8X85gnFVnpA0b7wt6Y%2FJOEN1C1lSjbwu%2Bf8R4V5I3k7uQ93wEUQl8lYrVqffskcJfeOgcTWbh9YQF1A%2BcBLGpIKuxUoPXi74ghR3pHkk9LXSdXWA%2BcqYSOuX5bqIDiOnsGHvnWsJ2GrGaB9SJrYa0LUc1S7%2FSjzum8Rtg%2FByaQk4nxkPXm9m90mGoDxdEMrWDtNTbEPw1%2Bb6b5e7jz5fpH9GO8uxmHDz1aCk%2Fu37135JKRtWejGsihGkTJvSdiTM8MGVOlPy3TIA%2BTvMBNLlccEJ4y8r6eyEKyfYSXS7uz4w8igubD3xwgZb1Y%2FgorEmR1ZPRg2FH1M1wiwWx9PZgYocMpNcqGh%2BmhAG85nvBOrD48Utpyt51Vm3K6z3o6PrXWGNN8myvIF90S7kLAI2F1sci4%2BPuhSJYP9dy7%2BeP9Yz9rS4xLwwYR6Fnep92taRbtW%2Fpe3Leqj8JFZfVPZR4ZCayvOd%2BH2WAS5cX%2FKD3Zr7ii3idvPu6Q5cH45rK4YaOZ4R%2F3%2FP7B26Xl6LrMK%2B3%2F9IGOqUBxdc0Xbw1%2Ft2uFs7gQkVt0QYqLkQVbN1VkRw%2B3ejU%2FWb3ctRqSQjv8w%2F3A5F9YLWm4T9uDQqMnlA2tAMANHkCh0dSs9maQMRwSdUm%2Fv3H9R1NRcDRHOrqvV2oljyyFNvvWd%2BbwdRhHk%2BeBDQFhJkGXV2aJMCwbz9hN4b3BoGjj728aVlIpks8oLLkRNCMW0crr7iA7S7zSqwPwPFnNIXPrrt50SxA&X-Amz-Signature=61d3f069ec10dd0b330fcd6f324c61423b31eb57b1a1fcbd3bcca6aba279e918&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

OK，异步编排是什么意思？哎，咱只听过容器编排，那啥是异步编排？我这里跟同学们画两个图，帮大家去理解一下。比如说我的商品详情页，如果想同时的访问这三个接口，异步置信，其实这就是一种异步编排。

[image](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/bc860c40-aadd-4669-a1c2-1cb810b63e8c/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466Y7B67OOT%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T230646Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDOt%2B4AhWQLfm6hNSC%2B0p2%2BqosUqUa8b6KZv6JjKHsp5QIgI1lqQjhFtl6nC0qLKxNDtsP2tm%2FQkHLFrnS3bv9m2JIqiAQIxv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDKkcBfBL%2BtyfsiUeHCrcA5Zj%2FKFvb5R885%2FRCZzcnKK%2FC3cr3vJtBKW82gIJ%2BF%2BniTSjJQ3848bqDBAgBdvjJIWMUB90yrvCclLc6USXadn9hWTM%2BnhI%2F1ICqe07b5F8X85gnFVnpA0b7wt6Y%2FJOEN1C1lSjbwu%2Bf8R4V5I3k7uQ93wEUQl8lYrVqffskcJfeOgcTWbh9YQF1A%2BcBLGpIKuxUoPXi74ghR3pHkk9LXSdXWA%2BcqYSOuX5bqIDiOnsGHvnWsJ2GrGaB9SJrYa0LUc1S7%2FSjzum8Rtg%2FByaQk4nxkPXm9m90mGoDxdEMrWDtNTbEPw1%2Bb6b5e7jz5fpH9GO8uxmHDz1aCk%2Fu37135JKRtWejGsihGkTJvSdiTM8MGVOlPy3TIA%2BTvMBNLlccEJ4y8r6eyEKyfYSXS7uz4w8igubD3xwgZb1Y%2FgorEmR1ZPRg2FH1M1wiwWx9PZgYocMpNcqGh%2BmhAG85nvBOrD48Utpyt51Vm3K6z3o6PrXWGNN8myvIF90S7kLAI2F1sci4%2BPuhSJYP9dy7%2BeP9Yz9rS4xLwwYR6Fnep92taRbtW%2Fpe3Leqj8JFZfVPZR4ZCayvOd%2BH2WAS5cX%2FKD3Zr7ii3idvPu6Q5cH45rK4YaOZ4R%2F3%2FP7B26Xl6LrMK%2B3%2F9IGOqUBxdc0Xbw1%2Ft2uFs7gQkVt0QYqLkQVbN1VkRw%2B3ejU%2FWb3ctRqSQjv8w%2F3A5F9YLWm4T9uDQqMnlA2tAMANHkCh0dSs9maQMRwSdUm%2Fv3H9R1NRcDRHOrqvV2oljyyFNvvWd%2BbwdRhHk%2BeBDQFhJkGXV2aJMCwbz9hN4b3BoGjj728aVlIpks8oLLkRNCMW0crr7iA7S7zSqwPwPFnNIXPrrt50SxA&X-Amz-Signature=d173770021f4d3d2031d2f1c12905f7ee450c1f64eb53d6154e1cebc7a9346b8&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

那么我们如果想这样来实现，我不想同时让这三个一起执行，我想先去执行前两个，执行完了之后再去执行最后一个接口。**那如果面试过程当中同学们被问到有什么解法，**


**那我相信大部分同学的回答可能是利用各种countdownlatch，山岚之类各种的 concurrent 类来做，那么其实咱这里有一种更通用而且更优雅的做法，那就是异步编排。那这是 JDK 里面给我们提供的原生能力，以后碰到这类场景我们就可以使用这一招。**


先，那接下来带同学们去到 Intellij 里看一下如何来做异步编排的实践。诶，每天 coding 一小时，健康工作 50 年，那我们又回到上一节当中给同学们讲到的这个累了。好，那么在这个类里，

[image](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/f117677b-1f41-4e61-ad9a-d39ed9438e49/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466Y7B67OOT%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T230646Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDOt%2B4AhWQLfm6hNSC%2B0p2%2BqosUqUa8b6KZv6JjKHsp5QIgI1lqQjhFtl6nC0qLKxNDtsP2tm%2FQkHLFrnS3bv9m2JIqiAQIxv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDKkcBfBL%2BtyfsiUeHCrcA5Zj%2FKFvb5R885%2FRCZzcnKK%2FC3cr3vJtBKW82gIJ%2BF%2BniTSjJQ3848bqDBAgBdvjJIWMUB90yrvCclLc6USXadn9hWTM%2BnhI%2F1ICqe07b5F8X85gnFVnpA0b7wt6Y%2FJOEN1C1lSjbwu%2Bf8R4V5I3k7uQ93wEUQl8lYrVqffskcJfeOgcTWbh9YQF1A%2BcBLGpIKuxUoPXi74ghR3pHkk9LXSdXWA%2BcqYSOuX5bqIDiOnsGHvnWsJ2GrGaB9SJrYa0LUc1S7%2FSjzum8Rtg%2FByaQk4nxkPXm9m90mGoDxdEMrWDtNTbEPw1%2Bb6b5e7jz5fpH9GO8uxmHDz1aCk%2Fu37135JKRtWejGsihGkTJvSdiTM8MGVOlPy3TIA%2BTvMBNLlccEJ4y8r6eyEKyfYSXS7uz4w8igubD3xwgZb1Y%2FgorEmR1ZPRg2FH1M1wiwWx9PZgYocMpNcqGh%2BmhAG85nvBOrD48Utpyt51Vm3K6z3o6PrXWGNN8myvIF90S7kLAI2F1sci4%2BPuhSJYP9dy7%2BeP9Yz9rS4xLwwYR6Fnep92taRbtW%2Fpe3Leqj8JFZfVPZR4ZCayvOd%2BH2WAS5cX%2FKD3Zr7ii3idvPu6Q5cH45rK4YaOZ4R%2F3%2FP7B26Xl6LrMK%2B3%2F9IGOqUBxdc0Xbw1%2Ft2uFs7gQkVt0QYqLkQVbN1VkRw%2B3ejU%2FWb3ctRqSQjv8w%2F3A5F9YLWm4T9uDQqMnlA2tAMANHkCh0dSs9maQMRwSdUm%2Fv3H9R1NRcDRHOrqvV2oljyyFNvvWd%2BbwdRhHk%2BeBDQFhJkGXV2aJMCwbz9hN4b3BoGjj728aVlIpks8oLLkRNCMW0crr7iA7S7zSqwPwPFnNIXPrrt50SxA&X-Amz-Signature=eb3e5d8f2a67b136787b526daeebb85a36d0b7faa06a436f5cf10196bfd5f344&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

我们前面是用到了这样的一个 complete able future 这样的一个类，我们这里的异步编排也是利用这个类的功能。好，我们这里先给同学们去简单的 show 一下第一个例子，如何通过异步编排的形式来实现三个接口同时调用。okay，那我这里给它起名方法，起名就叫 all in one，也就是同时的意思，三合一。OK，这里我们这行代码给它复制一下，分别把它调用三次，这里给它起名叫 future 一， future two， future three，然后我们的一部编排这时候就要上马了。


okay，假如我想在这 3 个方法执行完之后再执行一段逻辑，那么这种情况下，除了我们使用一些像Countdown， Ledge 之类的类，我们这里还可以这样来做。怎么来做？使用 complete able future 的 all of okay， all of 这里我们点进去看，它是一个可变参数列表，那它支持传入很多个 complete future 这个对象，这里我们就可以把 future one， future two and future three 全部给它放进去，并且调用这样一个方法。


我们看 then apply， async okay 这个方法里面它们具体来做什么呢？我们这里声明一个word，然后去写它的方法体。好，这里同学们就是你放业务逻辑的地方，那么异步编排的作用就在这。假如我们有一段业务逻辑，我希望让这三个代码执行完之后去执行，那我们就可以去用这样一种非常优雅的方法来实现okay。


那如果同学们说我发生异常了，怎么办？怎么办？我们这里可以调用它的另一个方法， exceptional exceptionally，然后把这个异常输出来就可以了，okay，非常的简单。好，我这里就简单化给它 return 一个 none okay。


那么我们在这个业务逻辑里应该怎么办呢？比如说我们就想象当前这是一个商品详情页，那我商品详情页需要获取到这 3 个结果当中的信息，那么我们就可以简单的这样来操作， return future one 点get，再加上 future two 点get，然后最后一个是谁？ future three okay，那同学们，这里就相当于把这三个子线程的结果全部汇总起来，并且做了一个返回，那它这里标红了，我们这只用加一个 try catch 就可以了。好，我们把这个 try catch 不负责任地放大成 exception okay，然后直接 return 一个空。


好，那么在最后打印一个方法， system out printo 打印什么内容？我想要打印这个 all in one 最后的执行结果，那么我们这里也需要使用一个 complete future，把这个结果给它拿到。好，我这里给它声明一个变量，就叫 all in one，然后它接收一个 string 类型的返回值，因为我们这里最终返回的是string，接收到之后，咱在这里给它打印出来。okay，那这里有异常，给它声明出来。好，那么这个方法到这里就已经执行了，那它的作用是同时执行123，然后最终汇总返回结果。


OK，那好，我们在这里把这个方法试着运行一下。okay，把 all in one 打上去，把异常声明出来。好，那接下来我们直接跑起这个 man 方法，看一下它的运行结果，应该可以看到他们的方法是同时执行，然后等待一秒钟之后返回一个最终结果。好，从这个日志里面可以看到，前面三次 future 的调用都是同时执行完毕，然后等待了一秒钟，最后一个 log 打印出来。


OK，那么这是其中的一个场景。咱在一开始还跟同学们讲过另一个场景是什么呀？我希望先调用一个服务，这个服务调用完之后，我在同时执行后两个服务，那这种方式我如何来使用异步编排的形式把它给搞定？我们这里来看咱同样的声明，一个方法叫 after you。好，因为咱要让一个方法先执行，其他两个方法紧随其后，所以就叫 after you。好嘞，那么这个先执行的方法，我们依然把它叫做 future one。OK，这个方法会首先得到执行。那接下来咱这边再声明一个 future to，我这里想让 future two 在 future one 执行过后再得到执行，应该怎么做？我们来看容器编排的方式。 future one，好，我们这里打上点谁 then apply acent，看到 then 这里同学们应该可以知道它是然后的意思，对吧？当你 future one 执行完之后，然后我再异步的方式去执行 future two，那我这个值可以加叫 value one，这个 value one 就是你 future one 执行过后的一个结果。


OK，那么接下来依然采用函数式编程的方式，把咱的这个业务逻辑给它打印出来。首先我们先打印一个 system out，在这个 system out 里面打印 future to start okay。然后 future to 这里我来去执行一段方法，这个方法是个耗时操作，也就是使用咱 service 里面的 nail 方法 sleep 一秒钟得到当前的时间，okay。最后我再采用 system out，把什么呢？把当前方法 to 执行的结果以及方法一 future one 里面执行的结果全部都打印出来。
好，我们这里 future one 等于 value one，然后再加上 future two，等于这个 time okay。那我们在现实的项目当中，不是每个方法它的返回值都是 long 型的，那我这里就模拟一个不同的情况，咱假定 future two 这里返回一个 string okay，那我这里返回的同样也要是个 string time，再加上 value one。好嘞，那么这就搞定了，我们把这个 track catch 给它写上，那咱 future to 的执行时间是在 future one 之后执行。


那咱前面说到 future one 执行过之后，我想同时执行两个任务， future two，还有 future three okay，那 future three 这里我也采用同样的方式。好，我把这一段给它复制一下，然后接着粘贴，把这个名称变一下，变成 future three。同时它也依然是在 future one 执行完成之后去执行一段自己的逻辑。那么这里我把它打成 future three start，那 future three 的返回值，我把它改回到浪形的time，OK，好嘞，那同样的，它的执行的阶段也依然是在 future one 执行之后执行。


好。那么最后一步我想要做这样的一个操作，我想在 future two 和 future three 这两个方法全部都执行完之后，再执行一段额外的逻辑，那么这个操作我们可以这样来做编排， future to 叠，诶， then combine okay，你看这个方法我们就把 future two 和 future three 把它连在了一块儿。那这个方法当中我的第一个参数是你要去组合起来的另一个 future 对象。那么我的方法的返回值的这个函数式编程里面的变量，我可以把它起名叫 f two 和 f three，那它分别代表着什么呢？它代表着是你 future two 和 future three 它们的返回值。好，我这里把这两个返回值给它打印出来。很简单， system out 点 print after you plus f three，这里把这两个值给它加上，然后直接 return 一个finished。


OK，那如果同学们说它发生异常怎么办？诶，咱前面是不是给同学们演示过，这里发生异常只用返回一个exceptional，调用一下它的这个变量。好，那么这个方法哎，也已经写完了，我们这里执行一下，看一看它的效果是不是如我们预期一样，把这个 all in one 注释掉，打上 after you，然后跑起闷。方法，走你。 32 一来睡过。


OK，同学们，刚才再回放一下，如果没有看清，再回放一下，它首先是打印出了这两行，那这两行是谁？这两个是 future one 执行的结果，OK，然后稍等片刻之后，它停顿了一下，然后同时打出了这两行，就是咱在这里执行的 future one 的 then apply ASNC，也就是 future one 执行之后接下来去执行的 future two 和 future three。那么当这两步都执行完成之后，它在最后去执行了这一句 f two，加上F3，就是我们最后写的这一个逻辑了。


那同学们通过这种异步编排的方式，可以自由地组合你在方法当中可以并行执行的业务逻辑，谁先执行，谁后执行，哪些可以并行，哪些必须异步，就可以用这种非常优雅的方式来把它编排起来。OK，同学们，那咱这一节的分享就到这里结束了。那这里呢？给同学们留一个小作业啊，把关于异步编排，这里还有很多其他的函数非常多的组合，同学们课后可以去自己稍加研究，去深入地了解一下这个异步编排的框架。OK，同学们，那咱在后面的小节里将跟同学们去分享一些性能测试的知识。好，同学们，我们下一小节再见。


