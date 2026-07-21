---
title: 1-12 【源码品读】解读Hystrix框架降级方案的触发方式 
---

# 1-12 【源码品读】解读Hystrix框架降级方案的触发方式 

[image](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/7651f8f6-cab6-490a-82cb-a73172c2bce3/SCR-20240719-cdlv.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663ZEFN2KU%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T225640Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDGrfJQpP8spPFD5G4eGw5lYs6V550q1ldJnQcW3lVeiAIhAPqBdQyYmnCQp4axMtgJ17hzon9If9wwvLsEF1qE5oGSKogECMb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgyOeix%2BBUjIxiT0Qg0q3AMBZ1Zjf0pKPqhlOWIX%2BN2aYz%2BqFMz5%2Bp2UuDu3%2FjJ%2BtOEQbcKjD8a0lFO0uE5zUvlC7IvuPPkYoOl0WARxwjcAUZfVQ03TkR2t4rzwbjZLIkp9oJ0ZqMfQnhUKl91gEcd1nqMDjFvtIosRZ830NGt55oHiuG0AjG8SyZL08R5iniCrFPpHsm7tSKUUSmtXNabmQd%2BqM4cFs9lCrUR67mSLLJ8a%2B4GCYusd7nJ5JmogZzYu%2BQgo5dhjGaPg1KfT2R3u%2FuWVidb2WZXwg8fiaat0AN%2FUTDJCeCJGcJEJvBMBLH34vklUzO68tkz8RbuxqfjsuV28pyFcBw%2BEGpxc3Fxrqx13h3lIVYCYQjmCJ8QMQc5b3R0YSqws4pAAjITcZOP5Hdl7uF6vQVmYodIkpZZT4PchzWF3lm05Cly9NUmK%2FjvdBS2rpEu87%2F2zDrDyYJRtD%2FQ4%2BckSO3ZvHny%2BeJJvsR%2FakxQZLfvyxhq588fSWibddVel4%2BwKAvLpA9vaa3DWDSwyULm6DazJqDfxgwbq%2BXdsnhXrMvTNMDuXOFViqfIxjAJWXPzbwvjXjA2HffBVMMR%2FEIl6om1aLPanXaH71Pnfg3rMYLxoqVyPBSHNemZb3WYm1yUz4u0Z0zDiuf%2FSBjqkAT%2Fk79dJvA2W%2FIVNc2q5cqI3sxnNFApcwg6uTZ5YdB03IyPqaER7Vt%2Fy7joFQF5BVvIX0THWxJTnzlE5KokAEKk0EtwuQ1jwwNEVqvJ3poKBfixD8IDlHlVWOI6ndU6tWoEq%2FVX22WE01hS34NLCKj2PnLOBPJ8vdGvb46yujS%2Bu1bvWxxJ2rmV26QjCrIf6ZDOP2yMTtCYRxcWAPqtDGkpsQwgQ&X-Amz-Signature=9dde1fc4a865cc76889c884e383e051429c464fd1a48473e4b230b582133d66d&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

[image](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/6af5acfb-5025-4265-9401-108c3ee4c132/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663ZEFN2KU%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T225640Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDGrfJQpP8spPFD5G4eGw5lYs6V550q1ldJnQcW3lVeiAIhAPqBdQyYmnCQp4axMtgJ17hzon9If9wwvLsEF1qE5oGSKogECMb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgyOeix%2BBUjIxiT0Qg0q3AMBZ1Zjf0pKPqhlOWIX%2BN2aYz%2BqFMz5%2Bp2UuDu3%2FjJ%2BtOEQbcKjD8a0lFO0uE5zUvlC7IvuPPkYoOl0WARxwjcAUZfVQ03TkR2t4rzwbjZLIkp9oJ0ZqMfQnhUKl91gEcd1nqMDjFvtIosRZ830NGt55oHiuG0AjG8SyZL08R5iniCrFPpHsm7tSKUUSmtXNabmQd%2BqM4cFs9lCrUR67mSLLJ8a%2B4GCYusd7nJ5JmogZzYu%2BQgo5dhjGaPg1KfT2R3u%2FuWVidb2WZXwg8fiaat0AN%2FUTDJCeCJGcJEJvBMBLH34vklUzO68tkz8RbuxqfjsuV28pyFcBw%2BEGpxc3Fxrqx13h3lIVYCYQjmCJ8QMQc5b3R0YSqws4pAAjITcZOP5Hdl7uF6vQVmYodIkpZZT4PchzWF3lm05Cly9NUmK%2FjvdBS2rpEu87%2F2zDrDyYJRtD%2FQ4%2BckSO3ZvHny%2BeJJvsR%2FakxQZLfvyxhq588fSWibddVel4%2BwKAvLpA9vaa3DWDSwyULm6DazJqDfxgwbq%2BXdsnhXrMvTNMDuXOFViqfIxjAJWXPzbwvjXjA2HffBVMMR%2FEIl6om1aLPanXaH71Pnfg3rMYLxoqVyPBSHNemZb3WYm1yUz4u0Z0zDiuf%2FSBjqkAT%2Fk79dJvA2W%2FIVNc2q5cqI3sxnNFApcwg6uTZ5YdB03IyPqaER7Vt%2Fy7joFQF5BVvIX0THWxJTnzlE5KokAEKk0EtwuQ1jwwNEVqvJ3poKBfixD8IDlHlVWOI6ndU6tWoEq%2FVX22WE01hS34NLCKj2PnLOBPJ8vdGvb46yujS%2Bu1bvWxxJ2rmV26QjCrIf6ZDOP2yMTtCYRxcWAPqtDGkpsQwgQ&X-Amz-Signature=04d8cf870c8c25b1b345732172d5e5a62133d9e869cbe7d3f567e2d8ff9e0bc1&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

[image](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/83c095bc-cbe1-4613-9981-6c2b5ff4e6cb/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663ZEFN2KU%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T225640Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDGrfJQpP8spPFD5G4eGw5lYs6V550q1ldJnQcW3lVeiAIhAPqBdQyYmnCQp4axMtgJ17hzon9If9wwvLsEF1qE5oGSKogECMb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgyOeix%2BBUjIxiT0Qg0q3AMBZ1Zjf0pKPqhlOWIX%2BN2aYz%2BqFMz5%2Bp2UuDu3%2FjJ%2BtOEQbcKjD8a0lFO0uE5zUvlC7IvuPPkYoOl0WARxwjcAUZfVQ03TkR2t4rzwbjZLIkp9oJ0ZqMfQnhUKl91gEcd1nqMDjFvtIosRZ830NGt55oHiuG0AjG8SyZL08R5iniCrFPpHsm7tSKUUSmtXNabmQd%2BqM4cFs9lCrUR67mSLLJ8a%2B4GCYusd7nJ5JmogZzYu%2BQgo5dhjGaPg1KfT2R3u%2FuWVidb2WZXwg8fiaat0AN%2FUTDJCeCJGcJEJvBMBLH34vklUzO68tkz8RbuxqfjsuV28pyFcBw%2BEGpxc3Fxrqx13h3lIVYCYQjmCJ8QMQc5b3R0YSqws4pAAjITcZOP5Hdl7uF6vQVmYodIkpZZT4PchzWF3lm05Cly9NUmK%2FjvdBS2rpEu87%2F2zDrDyYJRtD%2FQ4%2BckSO3ZvHny%2BeJJvsR%2FakxQZLfvyxhq588fSWibddVel4%2BwKAvLpA9vaa3DWDSwyULm6DazJqDfxgwbq%2BXdsnhXrMvTNMDuXOFViqfIxjAJWXPzbwvjXjA2HffBVMMR%2FEIl6om1aLPanXaH71Pnfg3rMYLxoqVyPBSHNemZb3WYm1yUz4u0Z0zDiuf%2FSBjqkAT%2Fk79dJvA2W%2FIVNc2q5cqI3sxnNFApcwg6uTZ5YdB03IyPqaER7Vt%2Fy7joFQF5BVvIX0THWxJTnzlE5KokAEKk0EtwuQ1jwwNEVqvJ3poKBfixD8IDlHlVWOI6ndU6tWoEq%2FVX22WE01hS34NLCKj2PnLOBPJ8vdGvb46yujS%2Bu1bvWxxJ2rmV26QjCrIf6ZDOP2yMTtCYRxcWAPqtDGkpsQwgQ&X-Amz-Signature=27699f546946469c50f366e597e64ca79e4a1107d77fce08ae6e4c8044c11761&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

[image](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/b6f4a4b2-1368-4bf3-8fcc-1746434e5df2/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663ZEFN2KU%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T225640Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDGrfJQpP8spPFD5G4eGw5lYs6V550q1ldJnQcW3lVeiAIhAPqBdQyYmnCQp4axMtgJ17hzon9If9wwvLsEF1qE5oGSKogECMb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgyOeix%2BBUjIxiT0Qg0q3AMBZ1Zjf0pKPqhlOWIX%2BN2aYz%2BqFMz5%2Bp2UuDu3%2FjJ%2BtOEQbcKjD8a0lFO0uE5zUvlC7IvuPPkYoOl0WARxwjcAUZfVQ03TkR2t4rzwbjZLIkp9oJ0ZqMfQnhUKl91gEcd1nqMDjFvtIosRZ830NGt55oHiuG0AjG8SyZL08R5iniCrFPpHsm7tSKUUSmtXNabmQd%2BqM4cFs9lCrUR67mSLLJ8a%2B4GCYusd7nJ5JmogZzYu%2BQgo5dhjGaPg1KfT2R3u%2FuWVidb2WZXwg8fiaat0AN%2FUTDJCeCJGcJEJvBMBLH34vklUzO68tkz8RbuxqfjsuV28pyFcBw%2BEGpxc3Fxrqx13h3lIVYCYQjmCJ8QMQc5b3R0YSqws4pAAjITcZOP5Hdl7uF6vQVmYodIkpZZT4PchzWF3lm05Cly9NUmK%2FjvdBS2rpEu87%2F2zDrDyYJRtD%2FQ4%2BckSO3ZvHny%2BeJJvsR%2FakxQZLfvyxhq588fSWibddVel4%2BwKAvLpA9vaa3DWDSwyULm6DazJqDfxgwbq%2BXdsnhXrMvTNMDuXOFViqfIxjAJWXPzbwvjXjA2HffBVMMR%2FEIl6om1aLPanXaH71Pnfg3rMYLxoqVyPBSHNemZb3WYm1yUz4u0Z0zDiuf%2FSBjqkAT%2Fk79dJvA2W%2FIVNc2q5cqI3sxnNFApcwg6uTZ5YdB03IyPqaER7Vt%2Fy7joFQF5BVvIX0THWxJTnzlE5KokAEKk0EtwuQ1jwwNEVqvJ3poKBfixD8IDlHlVWOI6ndU6tWoEq%2FVX22WE01hS34NLCKj2PnLOBPJ8vdGvb46yujS%2Bu1bvWxxJ2rmV26QjCrIf6ZDOP2yMTtCYRxcWAPqtDGkpsQwgQ&X-Amz-Signature=0d3660545248b0dd77926ddc712d01f186fc9fd03e1a088fae734c49c15e01af&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

hello 慕课网的各位同学们，大家好，这一节我将要带大家去完成一个 mission impossible 不可能完成的任务。为什么这么说，因为我们将要来到整个 spring cloud 中代码写的最精妙、最绕人、最难以维护、最眼花缭乱的 high streaks 部分，来看它的什么功能呢？那就是降级的触发以及判定。

[image](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/76beb633-02ed-4f6a-a70e-39851287ee4e/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663ZEFN2KU%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T225640Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDGrfJQpP8spPFD5G4eGw5lYs6V550q1ldJnQcW3lVeiAIhAPqBdQyYmnCQp4axMtgJ17hzon9If9wwvLsEF1qE5oGSKogECMb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgyOeix%2BBUjIxiT0Qg0q3AMBZ1Zjf0pKPqhlOWIX%2BN2aYz%2BqFMz5%2Bp2UuDu3%2FjJ%2BtOEQbcKjD8a0lFO0uE5zUvlC7IvuPPkYoOl0WARxwjcAUZfVQ03TkR2t4rzwbjZLIkp9oJ0ZqMfQnhUKl91gEcd1nqMDjFvtIosRZ830NGt55oHiuG0AjG8SyZL08R5iniCrFPpHsm7tSKUUSmtXNabmQd%2BqM4cFs9lCrUR67mSLLJ8a%2B4GCYusd7nJ5JmogZzYu%2BQgo5dhjGaPg1KfT2R3u%2FuWVidb2WZXwg8fiaat0AN%2FUTDJCeCJGcJEJvBMBLH34vklUzO68tkz8RbuxqfjsuV28pyFcBw%2BEGpxc3Fxrqx13h3lIVYCYQjmCJ8QMQc5b3R0YSqws4pAAjITcZOP5Hdl7uF6vQVmYodIkpZZT4PchzWF3lm05Cly9NUmK%2FjvdBS2rpEu87%2F2zDrDyYJRtD%2FQ4%2BckSO3ZvHny%2BeJJvsR%2FakxQZLfvyxhq588fSWibddVel4%2BwKAvLpA9vaa3DWDSwyULm6DazJqDfxgwbq%2BXdsnhXrMvTNMDuXOFViqfIxjAJWXPzbwvjXjA2HffBVMMR%2FEIl6om1aLPanXaH71Pnfg3rMYLxoqVyPBSHNemZb3WYm1yUz4u0Z0zDiuf%2FSBjqkAT%2Fk79dJvA2W%2FIVNc2q5cqI3sxnNFApcwg6uTZ5YdB03IyPqaER7Vt%2Fy7joFQF5BVvIX0THWxJTnzlE5KokAEKk0EtwuQ1jwwNEVqvJ3poKBfixD8IDlHlVWOI6ndU6tWoEq%2FVX22WE01hS34NLCKj2PnLOBPJ8vdGvb46yujS%2Bu1bvWxxJ2rmV26QjCrIf6ZDOP2yMTtCYRxcWAPqtDGkpsQwgQ&X-Amz-Signature=ee5594280764d528e57d63943f15873240cb3b432ba30930b4292004d14f87e5&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

OK 这一节的主要内容有以下三点，

第一点，我们来看一下 Hystrix 是如何运用 aspect 的切面编程来切入降级流程点的。

第二点，我们看一看 RxJava 中的 observer 模式。如果大家对 rx Java 并不那么熟悉，可以预先去了解一下。因为 RXJava 在编程体验上来说更接近函数式编程的风格。那各种回调函数用的那是天花乱坠。如果在项目中应用过  RXJava 的同学，可能这一节稍微会那么轻松一点，那咱们就可以携手负重前行了。


最后一点是什么呢？是我们看一下 Rxfunction 回调函数如何实现异常判定。前面我已经跟同学打过预防针，这节功能并不麻烦，但是代码写的真是非常的复杂。所以我希望大家在这一节秉承这样一个精神，好读书，不求甚解。咱有些功能点只可意会不可言传，意思到位了就可以酒肉穿肠过这个真意心中流。看了 Hystrix 的代码，相信大家再也不会说其他人写的代码像一坨屎山了。大家调节好心情以后就可以跟我出发了。我们到主场 in 泰迪 J 里面见识 Hystrix 这个乱拳打死老师傅风格的代码。走起，同学们这一节我就不喊口号了，因为我估计接下来的半小时大家过得不会很快乐的，但是难啃的骨头我们依然要迎难而上去啃。好，我们打开小桌板，这里从哪里开始入手呢？我们就直接从 HystrixCommand 这一个注解上开始。好不好？我们在项目中定义了很多HystrixCommand 我们看看这个注解是如何来起作用的。这里点进去。


看很神奇，神龙见首不见尾，这个注解里面空空如也怎么办？这种情况下老师前面怎么说的？查找他的引用对不对？我一番查找就嗅到了一丝蛛丝马迹，是谁呢？在看到这个累了吗？ aspect 切面对不对？通常来讲，这些注解都会跟 aspectJ 的切面来绑定，构造一个切面，让你的业务流程可以滚到切面里转那么一圈。


我们直接点到切面里面看，它这应该是哪一个方法执行了？我们的 Hystrix 简单了，你在切面上配置的时候是不是要配置一个 pointCut ，那我们只要看哪个 pointCut 挂上了我的名字。你看这一个切点是不是就是 HystrixCommand 标签？没错，那接下来它这里面的流程在哪？不用急，我们把这个方法名复制一下，往下走两步。就找到了他真正的方法执行的逻辑了。这个方法是用 around 标签括起来的。 around 什么意思啊？同学你到现在还不知道 around 的意思吗，赶紧去先复习一下。

好，我们在这个方法的第一行先打上一个断点，用我们最有效、最快速最直接的方法，直接用 debug 模式把这个 Hystrix 项目给它启动起来。当然了，前面你要确保有瑞卡的注册中心以及分 client 项目都已经启动好了。好，我们这里使用 debug 端口把这个 HystrixFallbackApplication 启动起来，然后静候佳音。


一炷香的时间已经过去了，项目也启动好了，我们收起小桌，怎么让这个断点达到这一行容易。我们打开 postman 调用一个方法，调用哪个方法呢？就调用它的 Fallback 方法，因为这个方法一定会走到降级流程里。对不对？好，我现在要点击 send 了，大家不要眨眼。好，敌人已经抵达战场，我们第一行已经到了，那这里随着它往下走，我们一行一行来看一下。


第一个方法，同学们还用看吗？直接跳过好不好了，因为这个 master 是谁，我们这里这个 master 应该指的是当前的 fallback 类，也就是 fallback 类中的 error 方法，看它的 master name 正好指向这个类。 ok 那接下来一个 validate 如果你的 method 为空，那么它会爆出一个异常，那咱这里肯定不为空了，所以没问题的。那接下来这个 if 条件是什么呢？就是如果你当前的方法中被 HystrixCommand 声明了，并且它又同时声明了 HystrixCollapse 那这种情况下它会抛出一个异常，因为为什么呢？因为你同一个方法，大家记住，不能把 HystrixCommand 和 collapse 一同使用。 OK 我们这里没有违反这个条件，放行。


到了下一步是构造一个 matter hold factory 你看凡是框架级别的项目都非常重视什么呢？这个 metadata 大家看前面分章节的源码品读应该也有这种感觉。 metadata 在框架层面尤其涉及到反射、协议解析等等这种类型的业务。 metadata 的收集非常常见。那么这里是根据谁根据 method 的 cut point type 来决定它是用哪个 meta hold factory 的。那我们这里的 point cut type 是谁？是 command 证明它是通过 HystrixCommand 注解来加上去的。那这里还有哪些其他方式呢？我们不妨点进去看一下。


卡这里总共就有 command 和 collapse 两种形式。所以咱前面说了，为什么有这样一个验证在上面这两个注解不能同时存在，因为它涉及到后面的初始化方式都是不同的。你要么使用 command 要么使用 collpase 好，我们不管它了，继续往下走。

[image](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/816aa970-d395-45d3-a9b6-0ca44bba8a25/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663ZEFN2KU%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T225640Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDGrfJQpP8spPFD5G4eGw5lYs6V550q1ldJnQcW3lVeiAIhAPqBdQyYmnCQp4axMtgJ17hzon9If9wwvLsEF1qE5oGSKogECMb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgyOeix%2BBUjIxiT0Qg0q3AMBZ1Zjf0pKPqhlOWIX%2BN2aYz%2BqFMz5%2Bp2UuDu3%2FjJ%2BtOEQbcKjD8a0lFO0uE5zUvlC7IvuPPkYoOl0WARxwjcAUZfVQ03TkR2t4rzwbjZLIkp9oJ0ZqMfQnhUKl91gEcd1nqMDjFvtIosRZ830NGt55oHiuG0AjG8SyZL08R5iniCrFPpHsm7tSKUUSmtXNabmQd%2BqM4cFs9lCrUR67mSLLJ8a%2B4GCYusd7nJ5JmogZzYu%2BQgo5dhjGaPg1KfT2R3u%2FuWVidb2WZXwg8fiaat0AN%2FUTDJCeCJGcJEJvBMBLH34vklUzO68tkz8RbuxqfjsuV28pyFcBw%2BEGpxc3Fxrqx13h3lIVYCYQjmCJ8QMQc5b3R0YSqws4pAAjITcZOP5Hdl7uF6vQVmYodIkpZZT4PchzWF3lm05Cly9NUmK%2FjvdBS2rpEu87%2F2zDrDyYJRtD%2FQ4%2BckSO3ZvHny%2BeJJvsR%2FakxQZLfvyxhq588fSWibddVel4%2BwKAvLpA9vaa3DWDSwyULm6DazJqDfxgwbq%2BXdsnhXrMvTNMDuXOFViqfIxjAJWXPzbwvjXjA2HffBVMMR%2FEIl6om1aLPanXaH71Pnfg3rMYLxoqVyPBSHNemZb3WYm1yUz4u0Z0zDiuf%2FSBjqkAT%2Fk79dJvA2W%2FIVNc2q5cqI3sxnNFApcwg6uTZ5YdB03IyPqaER7Vt%2Fy7joFQF5BVvIX0THWxJTnzlE5KokAEKk0EtwuQ1jwwNEVqvJ3poKBfixD8IDlHlVWOI6ndU6tWoEq%2FVX22WE01hS34NLCKj2PnLOBPJ8vdGvb46yujS%2Bu1bvWxxJ2rmV26QjCrIf6ZDOP2yMTtCYRxcWAPqtDGkpsQwgQ&X-Amz-Signature=c044e40e940f016713cf145a1831a1fb41ea4e12f99485cb161a7bc579a07f72&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

```java
# 正儿八经的参数
# 熔断的前提条件（请求的数量）， 在一定时间窗口内，请求达到5哥以后才开始进行熔断判断
hystrix.command.default.circuitBreaker.requestVolumeThreshold=5
# 超过50%的的失败请求，则熔断开关开启
hystrix.command.default.circuitBreaker.errorThresholdPercentage=50
# 当熔断开启以后，经过多少秒再进入半开状态
hystrix.command.default.circuitBreaker.sleeepWindowInMilliseconds=15000
# 配置时间窗口
hystrix.command.default.metrcs.rollingStas.timeInMilliseconds=20000

# 打酱油的路人参数
hystrix.command.default.circuitBreaker.enabled=true
# 强制开启熔断开关
hystrix.command.default.circuitBreaker.forceOpen=false
# 强制关闭熔断器
hystrix.command.default.circuitBreaker.forcceClosed=fasle
```

下一步是创建一个 MateHolder 这里没什么好看的，我们接着往下走。这一步是一个 Hystrix  Invokable 这实际上就是类似一个代理调用的形式，我们不必深究。前面咱说了好，读书不求甚解，对不对？就要每一行给你点进去看。这课程加个 10 小时。

OK 同学们到了这一步是什么？这一步通过 metaholder 里面的 is collapse annoted present 也就是说你是否声明了 collapse 咱这里是通过哪种类型进来的 command 对不对？所以这个属性一定是 false 那继续往下走。

好，我们往下走一步，看到这里的 execution type 应该是同步的形式，我们看一下 grand synchronize 那它有哪些其它形式呢？我们这里点进去了解一下。 asynchronize synchronize 和 observable 三种形式咱用的是哪一种？左青龙右白虎，老牛在中间，咱用的是中间这头老牛最厉害的。好，接下来这个判断 is observable 当然是 false 了，咱不是 observable 那号人。好，进到这里来，我们点进去难的地方马上要开始喽。点进去。好，这里两个 validate 安然通过。那在 switch 环节中，我们是 synchro nice 的方式进到了哪里？进到了 cast to executable 名字起的平淡无奇。这个故事一定不简单，我们硬着头皮点进去。好，这里只是把它做一个转译，把它转为 Hystrix  executable 类型。


好转完以后，这个 execute 的真正执行起来可就麻烦了，我们点进去看一下。大家看到这里一个 Q 和一个 get 简约而不简单，低调而奢华，我们再硬着头皮点进去一下。好到这里了，同学们是不是觉得这一行应该直接放过往下走，你看下面好多逻辑对不对？非。咱的故事都在哪，都在这里面了，不要被他迷惑住。所以很多同学如果自己去读 Hystrix   源码，可能想找到这个门，都蛮麻烦的。你看 histrix 它的方法起的特别有迷惑性，你一旦使用了这种函数式编程，还有这种回调的方式，你就不得不在整个代码库中辗转腾挪，到处跳转。所以你如果是一个功底深厚的 Java 老法师，也有可能被绕进去。好，我们这里点进去，看一看他的特 observable 搞什么鬼。好，我们已经。

登堂入室了，继续往下走。登堂入室怎么听起来像贬义词呢？你看下面的这些方法，眼花缭乱，都是一个接一个的回调函数是不是？那我们的逻辑究竟在哪呢？还记得前面我提到这一章的主旨是什么呢？ how 读书。

不求甚解。意思就是把支线句型全部略过，我们只看。


主线。好，下面是 5 秒钟的剧透环节，我们的主线在哪里？在这里，在这里先把它提前打几个断点。好，5秒钟到了，剧透环节结束，那我们再回到主线上来，一步一步的往下走。支线要不要不要？我们跳过这个支线，要不要同学课后可以自己研究一下，老师就不要了，我们还是跳过这一句，他就不是一个没有故事的女同学了。但是咱把它晾在一边，我们要显出这种高冷范，直接越过去头都不回往前走。


好，这些回调函数统统都长了一副德行，我们不管继续往后在 A 等等，这就不能往后了。大家看到一个 return 了对不对 OK 在这个 return 函数里，它用的 observable 的 defer 方法，这可是一个异步方法。大家如果有 Java script 的经验，前端编程的经验，可能对这个 defer 方法非常的熟悉。这里我们可以把它理解成某种异步回调的形式。咱先在这个主函数里面打上这样一个断点待会，不等咱招呼这个女同学就会追过来。好放开断点走。 OK 在这里他们做了什么操作呢？看第一个，第一个操作是用 compare 的 swipe cast 操作，咱甭管后面跟的是 swipe 还是 set 都是一个道理。其实这里只是利用 cat 操作做一个检查，验证资源的锁定，我们可以不加理会，把目光聚集在后面的流程里。我这里真的需要吐槽一下 Hystrix  的编码，回调函数它可以锦上添花。但是如果通篇都是回调函数，我个人并不觉得这是一个很好的编程风格。就像你在写 C 语言的时候使用 go to 语句一样，而且你会逐渐的发现你在维护这种超大型项目的时候，它往往会给你带来很多的麻烦，你不知道自己的条件触发了哪段回调，所以你不得不在每个回调上面打上各种断点。


我个人说实在的并不太建议同学们这样大量使用回调，那我们自己写的爽了，但是这种快乐可能建立在其他队友的痛苦之上。所以说句玩笑话，为什么 Netflix 公司决定暂停 Hystrix  的开发？我感觉可能这个代码真的维护不下去了。吐槽结束，我们继续往后看。这里看我们在属性中有没有开启 request log enabled 这也是 Hystrix   中的一个属性。同学们如果感兴趣，可以去了解一下这个 request log 是什么功能，我们这里跟主线无关，通略过。你看咱这走一趟主线剧情啊，接了多少支线剧情，这都是一个个 flag 呀，同学们有空的时候可以回过头来把之前剧情的经验都给刷掉。好，这里就走到了 request cache 拿到这个属性，咱这个标签上应该没有设置 request cache 所以它是 false 往后这个 cache K 应该也是空，我们这里就不去管它。


好，到了这里，同学们稍加留意，函数式编程加回调，你稍不留神可能就要把主线句型放过去了，大家看这是谁似曾相识对不对？他是不是？就是刚才咱说的那个有点故事的女同学我们这个高冷饭也不能一直高冷，咱现在可以回头去找人家了。点过来，果然就是他是他是他就是他，但是你现在还不能撩他对不对？咱得先把手头的正事给办完，再回来撩妹子，我们继续往下走。


大家看到这个妹子是在这里被勾搭上的。好，往后走这个条件会不会了？不会进去？咱没有 request cache 。这里跟同学提醒一下，这段逻辑算是一个相对重要一点的支线，同学们可以在这边打一个断点。然后当你调用 request cache 方法的时候，可以从这里看看它背后是什么流程，我们这里走到 else 逻辑里面。好把这个 Hystrix  observable 替换成最后要返回的对象。


Hystrix  Observable 就是刚才我们说的勾搭上女同学的人，他带着女同学走到了最后的 return 方法。好在这里咱声明了三个函数分别是什么， on terminate 在终止的时候还有 unsubscribe 就是在取消订阅的时候以及在完成的时候分别会调用哪些回调函数呢？就是前面我们定义的这些 X 我们回到主线上来，先不管他我觉得在 Hystrix  项目团队中一定有不少 Java scribe 技术的狂热爱好者。

你能很清晰地感觉到 Hystrix  的项目风格、代码风格跟其他的开源软件非常不同，每个开源软件的编码风格都像一种文体一样，像 Spring  这种很稳重的框架。大家可以说它像议论文，井井有条，头头是理的。这个 Hystrix  简直就像火星文了，但是我们要硬着头皮读好，这个 return 咱不管，直接把它断点放掉。


前面我们说到了，这个女同学将要登场了，对不对？我们把目光聚焦在女同学这里。好，我们放掉断点再放。好，现在可以聊妹子了，怎么撩？第一个，人家要给你做一个状态检查，看你是不是已经取消订阅了。你要是都不关注人家妹子，人家干嘛理你，咱没有取消订阅。好，那就进入了 apply Hystrix semiticsok 又是一串很绕人的各种回调，好在不是那么长。 OK 我们要关注的地方来了。好，骑手给你来一钩子。 execution hook on start 标注。好。接下来看到这里。

Circuit breaker all of request.这可就大有学问了。


大有学问又怎么样？照样跳过。为什么？它不是主线剧情吗？没错，但是咱这一节讲了下一节讲什么呢？我们会放到下一节中，再跟大家讲解熔断器断路开关，它前面的配置参数在实际的业务中都会起到什么作用。好，那我们继续往下走。这一部分都是信号量相关的知识点。我在这一节先不跟大家剧透了，后面会有详细的教程，跟大家说什么是信号量，还有相应的线程隔离方案。 OK 我们往后走，走到这里，大家看这里受信号量控制的一个 try acquire 决定了你当前是不是受控的访问，我们这里可以安全放行。 OK 往后依然把重点放在哪里呢？我们把重点放在 return 函数里，大家看到这里有一个 do on error do on terminate 还有 do unsubscribe 这里约定了一系列异常情况下我将要调用哪些的回调函数，对不对？比如说 exception 抛出的情况，那这里需要 event notifier 去发布一个 event 再比如上面我们会在完成应用请求的时候关闭信号量，就是释放当前这个信号量。对不对？ OK 这里都不用管，关键是在哪里。


这个不起眼的方法里面有点学问，我们进去看一下。又是一堆回调，看 Hystrix 的编码一直游走在崩溃的边缘。这个研发团队的程序员太任性了。 Hystrix 想说爱你不容易，相爱没有那么容易，每个写代码的程序员有他的脾气。 OK 我们在这几个回调中要重点关注哪一个。这个剧透的太明显了，这里一个断点已经打上去了。好，我们看这个 handle fallback 这里是什么，我们待会儿扔出异常的时候，将要走到这个流程里面。好，那我们剩下的就先不用看了，直接返回。好，返回回来。那这时候如果放掉断点了以后啊，不出意外的他会访问失败。对不对？那么最终的请求将会落到刚才跟大家剧透的 handle fallback 里面，这一步真是请君入瓮啊。开启上帝视角就是好办走放断碟好。果不其然过来了。

那咱第一个先获得了这个 exception 我们看看这个 exception 是什么类型，是不是咱声明的 runtime exception 看它的 error message 叫 first fallback 这就是我们在容错逻辑中抛出来的这个 runtime exception 的 message 那同学可能这里会有一个疑问，我们在这个 debug 过程中捕捉到的是谁呢？是容错逻辑里面，也就是 fallback 函数里又再次抛出了异常。


那这个异常会被我们的 Hystrix  command annotation 给捕捉到，然后导到二级降级流程里。如果你在原先调用方法中发现了异常，那是谁来捕捉的呢？其实这个过程没有区别，还是刚才咱看的这一串串回调来捕捉的，只不过它的入口的地方不同了。如果你是通过注解形式的，也就是 Hystrix  command 标签注解的，那么它是通过 S back J 来注入的。那么你如果没有通过 Hystrix   command 标签做注解，而是直接通过 fin 比如 fin client 标签下面的 fallback 属性指定一个降级类。

那么它的入口是在哪里呢？虽然它后面的处理逻辑跟咱刚才 debug 看的代码都一样，但是入口可在其他地方，这就是留给大家的作业了，给同学们一个大展身手的机会。大家迷失在 Hystrix  里面。 OK 我们继续往后看，这个 runtime exception 接着会进入哪一个分支呢？它是不是 rejected 不是，再往后 Hystrix   timeout 也不是，那 bad request 更不是了。原来是 else 里面。 OK 往下走进到了最后一个 handle barely while fallback 你看这个意思说的已经很明了，叫什么呀？你 fallback 中又变成了 failure 错上加错了，那我们点进去看一下。好，我们看这里做了什么操作。


第一个，一个 invent notifier 把这个异常信息给它发布出去，对不对？它的 command key 是谁就叫 errorok 我们接着往下走。这一步在 execution result 里面把它的 exception 已经给塞入进去了。然后到了最后的 return 方法。 return 方法中决定了什么？是叫 get fallback or through exception 最终审判的时候到来了，是生存还是毁灭？是抛出异常还是进入下一个 fallback 很简单，拿到 request 的上下文，一个事件发不出去。然后这里的一些if 。第一个判断是那 be wrapped 这里只是判断你的 exception 类型，如果你不是特定类型，那么它这个 if 条件不会走进去，我们直接往后看。


第二个判断 is unrecoverable 看你是不是无可救药，咱是不是还能抢救一下。好，所以咱到了 else 里面。 OK 那在这个衣服条件里 promise fallback enabled 这里又允许了 fallback。我的一个神呐，又是一连串的回调。回调回调。 OK 我们老样子放过他们吧。好读书，不求甚解呢。 OK 那我们走到最后一路往下不回头。在这一步我们看它能否获得 fallback 的信号量。 OK 它一旦获得了，然后就标志着另一串 fallback 生涯的开启，接着就进入了这个轮回当中。

OK 好，到这一步应该就算完结了，同学们还想再根据看第三层的 fallback 吗？ come on 放过我。大家如果意犹未尽的话，我建议大家可以配置 18 层 fallback 一层一层点进去，这样体验整个流程，就像下了 18 层地狱一种感觉。那到了最后，这个 return 我可以宣布自己解放了。 OK 那我们一路返回苦笑三声还是不放过我。因为为什么呢？因为我这里配置了好多层的降级，所以当二级降级失败了以后，这个回调又回到了哪里 handle fallback error 那既然前面咱们都已经走过整个流程了，我这里啦就不要再重新来过了，所以今天的主线剧情就到此为止了。


那我跟大家总结一下这一节的内容，我们通过一个 Hystrix  command 的注解入手，来了解了这个注解是如何对我们的降级业务流程植入一个切面，并且它通过 RxJava 组件提供的 RxFunction 实现了一系列的异步回调流程来处理整个的降级熔断业务。

我们通过前面的代码阅读也了解到 Hystrix  的主线剧情非常非常的庞大，咱今天只是走了其中一条比较省力的路径，剩下的各方支线巨型，还有各方主线巨型，不同的发展方向还有待同学们自己去研究。好了，那这一节的内容就到此结束了。下一节我将为大家介绍 Hystrix strong 同样重要的一个知识点，那就是熔断器我们有时候也叫它断路器。 OK 那同学们我们下期再见。


