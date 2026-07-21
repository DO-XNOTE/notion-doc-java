---
title: 2-6 【源码阅读】EnableFeignClients底层机制深度解析
---

# 2-6 【源码阅读】EnableFeignClients底层机制深度解析

[image](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/5d08a5fa-e1e8-4673-922b-992afb1c3316/SCR-20240718-pxre.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TYI6JOKR%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T225622Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIGtlD%2B8GPygILXbTJ6mYKHSwM4DC%2BSWyaMuuwXeZJjRaAiEAik2Fr5s5DI52kaIeoVwyu7wnmkLimfmQjHdW6ssrh2QqiAQIxv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDNoHlXvaxfSJqjzXSSrcA%2Foa6U86QIu9srKN11bKFuL%2FZ7J8kzMIVmq%2BeXNQwG3f2Qhz%2FNgYh6%2FVbxbXtJTDxQom%2FLcYZEuaypdiLgXH0t%2FUHgfAAt2wPdzxPfA4xGCn%2BECEmWJIeDRL0besMuKYyEi079JVb0EGp2ZSFlzhhS%2BkvwErgJ8Hjjs10umHV7WXfhXnADQcwC7S8IYbdn23hrj2zvq0vDOsVyWNCJncLGBU1BMERCN3aUvhRRqf1hj5sTa%2B9VJ0OXzBKhh%2B0xmOOFVSLhzVxowqAjrnooGoLZUTm%2BOr%2FXL5og%2FOjNXbm%2BxcPHr0oGvPCWq2qtQRPSxXT%2FE2z4tetAnQofbtNkR4w1oFdhPvpVfUZV9kzBXg9lsLjCVdyyUMa8%2BqF5%2BC3K%2B05hXz00y33nUWqOl7YwAL%2FrtxJpQOZ2efUOxcL0TZ7HKdRf7hHJAfkJIiWN2FToBQwBCl9UY9RmgnSogjjlFCv3CEc%2BMMfVYt%2BcdxpGNdHRcgCXhVgxqHjvGjbQh4AR4O0r%2F4dRb1sDgrnU8MexSdJ66kgkRtA1906OqqPGrp7EzVwf8wvWRWKtRHboOSUFhh9WinWuyKx73GtDfZqf8ZyfURkmvq1QLV0JwZJwgKG%2Fbf5olWx8bSBCAjnfCbMNi6%2F9IGOqUBox9Qo%2FV8HOpu36%2F9FVKjTHZ39BK8Ilz8GOBdU%2B67bbf%2FV8rQUy3D4V0QU3Gcu%2F3lwS2NVu7OyfwUMLXU%2B0LkVhW5NO7NsTNNelUdcfGQnXMHcswgdtFQ9tBiu0qwtTgaklldA6IEzhoW8F1k7TGY24Uu6hdo%2FyY%2FRcP8JKA9m4h14ZbcjddOjRHK2eQSn1mHggLDYpxPF4UEUxIOP5RWoSHec%2F%2Fy&X-Amz-Signature=b912ee798b9b3d9fb3e938b0724707ffa5b35f936e1ee3b90c6074beb923c79f&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

[image](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/067938ea-631e-445c-90fb-52a2d60c9599/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TYI6JOKR%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T225622Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIGtlD%2B8GPygILXbTJ6mYKHSwM4DC%2BSWyaMuuwXeZJjRaAiEAik2Fr5s5DI52kaIeoVwyu7wnmkLimfmQjHdW6ssrh2QqiAQIxv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDNoHlXvaxfSJqjzXSSrcA%2Foa6U86QIu9srKN11bKFuL%2FZ7J8kzMIVmq%2BeXNQwG3f2Qhz%2FNgYh6%2FVbxbXtJTDxQom%2FLcYZEuaypdiLgXH0t%2FUHgfAAt2wPdzxPfA4xGCn%2BECEmWJIeDRL0besMuKYyEi079JVb0EGp2ZSFlzhhS%2BkvwErgJ8Hjjs10umHV7WXfhXnADQcwC7S8IYbdn23hrj2zvq0vDOsVyWNCJncLGBU1BMERCN3aUvhRRqf1hj5sTa%2B9VJ0OXzBKhh%2B0xmOOFVSLhzVxowqAjrnooGoLZUTm%2BOr%2FXL5og%2FOjNXbm%2BxcPHr0oGvPCWq2qtQRPSxXT%2FE2z4tetAnQofbtNkR4w1oFdhPvpVfUZV9kzBXg9lsLjCVdyyUMa8%2BqF5%2BC3K%2B05hXz00y33nUWqOl7YwAL%2FrtxJpQOZ2efUOxcL0TZ7HKdRf7hHJAfkJIiWN2FToBQwBCl9UY9RmgnSogjjlFCv3CEc%2BMMfVYt%2BcdxpGNdHRcgCXhVgxqHjvGjbQh4AR4O0r%2F4dRb1sDgrnU8MexSdJ66kgkRtA1906OqqPGrp7EzVwf8wvWRWKtRHboOSUFhh9WinWuyKx73GtDfZqf8ZyfURkmvq1QLV0JwZJwgKG%2Fbf5olWx8bSBCAjnfCbMNi6%2F9IGOqUBox9Qo%2FV8HOpu36%2F9FVKjTHZ39BK8Ilz8GOBdU%2B67bbf%2FV8rQUy3D4V0QU3Gcu%2F3lwS2NVu7OyfwUMLXU%2B0LkVhW5NO7NsTNNelUdcfGQnXMHcswgdtFQ9tBiu0qwtTgaklldA6IEzhoW8F1k7TGY24Uu6hdo%2FyY%2FRcP8JKA9m4h14ZbcjddOjRHK2eQSn1mHggLDYpxPF4UEUxIOP5RWoSHec%2F%2Fy&X-Amz-Signature=910914ea860222db53af1fe80b1637a86df2f574a49f64f1057b54ee78428c40&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

[image](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/c4f641f4-e6fb-4d1d-bebc-e87d2724c193/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TYI6JOKR%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T225622Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIGtlD%2B8GPygILXbTJ6mYKHSwM4DC%2BSWyaMuuwXeZJjRaAiEAik2Fr5s5DI52kaIeoVwyu7wnmkLimfmQjHdW6ssrh2QqiAQIxv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDNoHlXvaxfSJqjzXSSrcA%2Foa6U86QIu9srKN11bKFuL%2FZ7J8kzMIVmq%2BeXNQwG3f2Qhz%2FNgYh6%2FVbxbXtJTDxQom%2FLcYZEuaypdiLgXH0t%2FUHgfAAt2wPdzxPfA4xGCn%2BECEmWJIeDRL0besMuKYyEi079JVb0EGp2ZSFlzhhS%2BkvwErgJ8Hjjs10umHV7WXfhXnADQcwC7S8IYbdn23hrj2zvq0vDOsVyWNCJncLGBU1BMERCN3aUvhRRqf1hj5sTa%2B9VJ0OXzBKhh%2B0xmOOFVSLhzVxowqAjrnooGoLZUTm%2BOr%2FXL5og%2FOjNXbm%2BxcPHr0oGvPCWq2qtQRPSxXT%2FE2z4tetAnQofbtNkR4w1oFdhPvpVfUZV9kzBXg9lsLjCVdyyUMa8%2BqF5%2BC3K%2B05hXz00y33nUWqOl7YwAL%2FrtxJpQOZ2efUOxcL0TZ7HKdRf7hHJAfkJIiWN2FToBQwBCl9UY9RmgnSogjjlFCv3CEc%2BMMfVYt%2BcdxpGNdHRcgCXhVgxqHjvGjbQh4AR4O0r%2F4dRb1sDgrnU8MexSdJ66kgkRtA1906OqqPGrp7EzVwf8wvWRWKtRHboOSUFhh9WinWuyKx73GtDfZqf8ZyfURkmvq1QLV0JwZJwgKG%2Fbf5olWx8bSBCAjnfCbMNi6%2F9IGOqUBox9Qo%2FV8HOpu36%2F9FVKjTHZ39BK8Ilz8GOBdU%2B67bbf%2FV8rQUy3D4V0QU3Gcu%2F3lwS2NVu7OyfwUMLXU%2B0LkVhW5NO7NsTNNelUdcfGQnXMHcswgdtFQ9tBiu0qwtTgaklldA6IEzhoW8F1k7TGY24Uu6hdo%2FyY%2FRcP8JKA9m4h14ZbcjddOjRHK2eQSn1mHggLDYpxPF4UEUxIOP5RWoSHec%2F%2Fy&X-Amz-Signature=7d7a581a1b53f85f215a864032372818b602bd44da22d63ed717bef3a610551c&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

hello 慕课网的各位同学们，大家好，我们又见面了，这一小节我们来看什么呢？我们就来学习一下 fin 注解背后的那一股神秘的东方力量。好，本节的主要内容分为三大部分。第一部分我们看一下入口类上面挂载的这个 enable 分 client 注解的背后是怎么把这一套 fen 的框架给加载起来的？它的扫包的流程都是什么？这个对大家以后自定义一套框架层面的注解是很有作用的。比方说我们自己也要想研发一套 fin 风格的框架，那么你可能就会用上这里面的很多的技巧。
好，第二部分是什么呢？我们来看一下 spring 中 bin 加载模式的扩展点。这个乍一听还不太好理解对不对？

[image](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/28b5cb7e-336a-4036-acb2-9b5447c761c9/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TYI6JOKR%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T225622Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIGtlD%2B8GPygILXbTJ6mYKHSwM4DC%2BSWyaMuuwXeZJjRaAiEAik2Fr5s5DI52kaIeoVwyu7wnmkLimfmQjHdW6ssrh2QqiAQIxv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDNoHlXvaxfSJqjzXSSrcA%2Foa6U86QIu9srKN11bKFuL%2FZ7J8kzMIVmq%2BeXNQwG3f2Qhz%2FNgYh6%2FVbxbXtJTDxQom%2FLcYZEuaypdiLgXH0t%2FUHgfAAt2wPdzxPfA4xGCn%2BECEmWJIeDRL0besMuKYyEi079JVb0EGp2ZSFlzhhS%2BkvwErgJ8Hjjs10umHV7WXfhXnADQcwC7S8IYbdn23hrj2zvq0vDOsVyWNCJncLGBU1BMERCN3aUvhRRqf1hj5sTa%2B9VJ0OXzBKhh%2B0xmOOFVSLhzVxowqAjrnooGoLZUTm%2BOr%2FXL5og%2FOjNXbm%2BxcPHr0oGvPCWq2qtQRPSxXT%2FE2z4tetAnQofbtNkR4w1oFdhPvpVfUZV9kzBXg9lsLjCVdyyUMa8%2BqF5%2BC3K%2B05hXz00y33nUWqOl7YwAL%2FrtxJpQOZ2efUOxcL0TZ7HKdRf7hHJAfkJIiWN2FToBQwBCl9UY9RmgnSogjjlFCv3CEc%2BMMfVYt%2BcdxpGNdHRcgCXhVgxqHjvGjbQh4AR4O0r%2F4dRb1sDgrnU8MexSdJ66kgkRtA1906OqqPGrp7EzVwf8wvWRWKtRHboOSUFhh9WinWuyKx73GtDfZqf8ZyfURkmvq1QLV0JwZJwgKG%2Fbf5olWx8bSBCAjnfCbMNi6%2F9IGOqUBox9Qo%2FV8HOpu36%2F9FVKjTHZ39BK8Ilz8GOBdU%2B67bbf%2FV8rQUy3D4V0QU3Gcu%2F3lwS2NVu7OyfwUMLXU%2B0LkVhW5NO7NsTNNelUdcfGQnXMHcswgdtFQ9tBiu0qwtTgaklldA6IEzhoW8F1k7TGY24Uu6hdo%2FyY%2FRcP8JKA9m4h14ZbcjddOjRHK2eQSn1mHggLDYpxPF4UEUxIOP5RWoSHec%2F%2Fy&X-Amz-Signature=39dd1604a9096ec8dee77b70d28de1fa8fd38db83fa532f931036df07423f254&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

待会儿到了代码里，我们再来仔细的研究好最后一个部分是什么呢？我们看看 thin 是如何构造上下文对象的。我们知道 spring 有它的上下文， spring context application 也就是 serve led 也有它的上下文。同样， fin 这里也有一个 fin context 这里我们就来看一看它在。


源码层面是怎么构造着的？ OK 那大家抄起家伙转战我们的主场，每天扣丁 1 小时，少活我健康工作 50 年。大家接下来要去看一看 finn 的注解加载流程对不对？我们打开它的入口类圆起圆面 spring cloud 的组件都是从这个入口类来说起。那这个入口类里面看哪一个注解呢？

[image](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/be193083-6602-4f2e-a699-e5a5f5bbfb01/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TYI6JOKR%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T225622Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIGtlD%2B8GPygILXbTJ6mYKHSwM4DC%2BSWyaMuuwXeZJjRaAiEAik2Fr5s5DI52kaIeoVwyu7wnmkLimfmQjHdW6ssrh2QqiAQIxv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDNoHlXvaxfSJqjzXSSrcA%2Foa6U86QIu9srKN11bKFuL%2FZ7J8kzMIVmq%2BeXNQwG3f2Qhz%2FNgYh6%2FVbxbXtJTDxQom%2FLcYZEuaypdiLgXH0t%2FUHgfAAt2wPdzxPfA4xGCn%2BECEmWJIeDRL0besMuKYyEi079JVb0EGp2ZSFlzhhS%2BkvwErgJ8Hjjs10umHV7WXfhXnADQcwC7S8IYbdn23hrj2zvq0vDOsVyWNCJncLGBU1BMERCN3aUvhRRqf1hj5sTa%2B9VJ0OXzBKhh%2B0xmOOFVSLhzVxowqAjrnooGoLZUTm%2BOr%2FXL5og%2FOjNXbm%2BxcPHr0oGvPCWq2qtQRPSxXT%2FE2z4tetAnQofbtNkR4w1oFdhPvpVfUZV9kzBXg9lsLjCVdyyUMa8%2BqF5%2BC3K%2B05hXz00y33nUWqOl7YwAL%2FrtxJpQOZ2efUOxcL0TZ7HKdRf7hHJAfkJIiWN2FToBQwBCl9UY9RmgnSogjjlFCv3CEc%2BMMfVYt%2BcdxpGNdHRcgCXhVgxqHjvGjbQh4AR4O0r%2F4dRb1sDgrnU8MexSdJ66kgkRtA1906OqqPGrp7EzVwf8wvWRWKtRHboOSUFhh9WinWuyKx73GtDfZqf8ZyfURkmvq1QLV0JwZJwgKG%2Fbf5olWx8bSBCAjnfCbMNi6%2F9IGOqUBox9Qo%2FV8HOpu36%2F9FVKjTHZ39BK8Ilz8GOBdU%2B67bbf%2FV8rQUy3D4V0QU3Gcu%2F3lwS2NVu7OyfwUMLXU%2B0LkVhW5NO7NsTNNelUdcfGQnXMHcswgdtFQ9tBiu0qwtTgaklldA6IEzhoW8F1k7TGY24Uu6hdo%2FyY%2FRcP8JKA9m4h14ZbcjddOjRHK2eQSn1mHggLDYpxPF4UEUxIOP5RWoSHec%2F%2Fy&X-Amz-Signature=742b3eb1ec1698e9fa512fdb84cee3a9262752bae53be416a8680842bd3d8dfd&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

当然是 enable 分 class 了对不对？那我们接下来就像这个大侦探去探案一样，一点点寻找它的蛛丝马迹。从这个 finn 的加载方式里面，我们可以学到很多自定义一个框架层面注解所要用到的小技巧，非常的简单高效。那我们接下来就进去看一把，点进去。


好，那这个注解大家看有什么内容，有一个 value 有一个 base packages base package classes 这里就是一些扫包的路径。那我们看前面我有没有配这些扫包的路径，这里空空如也对不对？唱空城记了什么都没有配，那他是怎么把这个份加载起来的呢？ OK 我们接下来往下看。
你从这里能看出它的加载流程从哪里入手？原曲原面在哪里往上，是不是在这个 import 这里？这是第一个小技巧了，大家以后自定义这种注解的时候，也可以使用一个 import 加载谁呢？加载一个，这个实现类 fin client registry 顾名思义就是做 fin 的注册。那他这里是怎么来注册整个框架的呢？我们进去看一眼。


好，你看他这里实现了哪些接口 import bin definition register 那这个是谁的 sprint 接口对不对？ OK 除了这些，他还注册了哪些 resource aware environment aware 这两个接口大家是不是都很熟悉了？ spring 提供的鼎鼎大名的 aware 系列接口，这两个我就不过多深入了，大家工作中应该非常常见。作为有几年经验的程序员，应该对这个是了如指掌的。


OK 那接下来我们来看一下这个 bean definition registry 他做什么东西，你看他这边有一个什么注解，有一个 register been definition 好，他其他什么都不干，把这个发挥空间留给了谁，留给了我们自己。那 fin 是如何来利用这个注解实现自己的功能的？我们来看。


回到这里找到刚才那个注解的名称叫 register bin definition 对不对？在这里。那我们来这里直接二话不说上断点学习一个框架，它最快的途径是什么？ debug 从头到尾 debug 一番，你什么都了解了好，打上断点以后接下来做什么？启动分 consumer 用什么方式启动？ debug 模式走起倒数 5 个数 43 它已经悄悄来到我的身旁。


好，这两个注解挨个进去看一下。第一个它的名称叫 register default configuration 注册默认的配置断点，走进去看里面有什么名堂。好，那这里第一步是 get default attributesget 谁的 default attributes 就是我们这个注解 enable 分 clients 的 default attributes 那这个 map 里面有什么内容呢？大家可以看到有 5 个key ，这 5 个 key 是在哪里声明的？没错，就是在这个注解中声明的五个变量，只不过我们没有给它赋任何的值，所以说这五个变量都是空的，他们就是需要扫包的时候，指定你扫哪个包路径等等的信息。好，那接下来这个 if 条件进去。


如果这个 matter has closing class 有没有没有？ enclosing class 是什么意思啊？就是说你这个方法还含不含有附层的 top 类，也就是一个顶层的类。那我们这里有没有继承任何类没有。所以说它这里到了 else 的逻辑里面。这个 else 拼装的 name 是什么呢？它就是 default 后面跟我们的包名如雷贯耳的 com.imock.spring cloud 再跟我们的 class 名字 finn consumer application 非常简单。
OK 那接下来这一个方法， register client configuration 我们进去看一眼看这个类做什么，大家看到这里就非常明白了。对不对？它传入了一个什么 bin 一个 registry bin 那在这个 registry bin 里面就构造了谁上下文中需要用到的 bin 信息。那这个 builder 先构造了分 client specification 这个类。接下来把我们的 main 函数的类名传入进去，并且把配置项也传入进去，然后就怎么样就在这个病 definition 里面，把这个病注册进去了，对不对？ OK 那我们直接返回。这里流程还比较简单。刚才我们看了第一个方法是注册默认的配置。那接下来这个方法就是和 fin 息息相关了，叫 register fin clients 大家还记着什么叫 thin class 吗？我带大家再回顾一下，前面一个小节当中我们定义了 service 在这里，看到它上面这个标签没有 thin client ，那这个就是 thin clientok 接下来我们到 debug 断点，马上这里的流程就要去注册这些分 client 了，我们看他是怎么来注册的。
点进去。第一步，拿到 scannerscanner 是什么东西，非常简单，就是一个 class pass scanner 是作文扫包用的。 OK 返回。那接下来这一步塞入一个 results loader 平淡无奇。


那么接下来到这里就有点变数了，我们再一次拿到了 enable 分 clients 上的 attribute 并且大家看这里声明了一个 filter 这个 filter 是做什么的呢？它会过滤 thin clients 注解的一些类。那这个 filter 往后有用处，紧接着我怎么样？如果你的 attributes 是空，那么返回一个空，如果不是空怎么样 get 你声明到的 clients 那我们有没有声明 clients 呢？我们在闷函数上的注解当中什么都没有声明，所以这个 clans 是不是也是空好，那如果它是空说明什么呢？说明我没有指定让你加载哪些分 clients 那这种情况我们怎么样？万箭齐发。你哪里声明了，我们就到哪里去加载你。所以这里加入了一个 annotation type filter 我加载所有声明了，分 client 注解的接口和类。


好，再往下走一步，从 metadata 里面 get 什么？ get 一个 base package 这个 base package 会用来做什么呢？我们点进去看一看它是怎么来获取的。这里又去拿了一遍 enable thing clients 实际上这个 attributes 多次获取，它是不是可以从这个方法的签名中给它传进来？但是为什么不这样做呢？大家想象，如果你每个方法上下文都要传递一个 attributes 而且还是个 map 这写起来是不是每个接口显得特别的臃肿。对不对？那既然它是一个不那么费时的操作，所以我们没必要在这里太苛求极致保持代码的整洁，反而能提升编程效率哟。


所以我们在每一个方法中，独立获取一次 attributes 好，接着往下我们的 attributes 有没有声明的任何属性没有，所以 for 循环都进不去这些属性大家也可以进行额外的声明，这样我们的 fin 就会知道我该去扫描哪些包路径哪些 class 了。


那如果你都没有声明怎么办呢？这里有一个备选方案是什么 class YouTube get package name 它会怎么样呢？它会拿你当前声明的闷函数里的那个类，把他的 package name 拿到，然后扫描谁扫描 com.imock.spring cloud 凡是在这个包下面声明的类，即便你在下面又多建了几层目录，只要你的这个类是在这个 package 下面的，我都会把你加载进来，都会扫描你。所以这就是为什么我让大家在所有的 demo 项目中全部给它起一个统一的名词，叫 come.imock.spring cloud 这样会省去不少的配置。那么大家在自己的项目中，有可能是会引用来自于不同业务方的配置文件或者是不同业务方的接口，你要去调用它那怎么办呢？你的包路径不同，这种情况下，你就要在自己的注解上面指定 base package base package classes 去引导份来加载你想要的这个类。


好，那我们这里继续往下走。它的 base package 里面添加了一个节点是什么？就是 come.eye mock in spring cloud 好，那么我们回到上一层， base package 加载完了，接下来我要循环每个 base package。


这个过程也不难。在循环每一个 base package 的时候，我们用谁来扫包 scanner 对不对？那这个 scanner 大家还记得前面把它加了一个 filter 吗？是 annotation type filter 那它就会把这个包路径下的所有加载了对应 annotation 的 class 或者 interface 给它揪出来。好，我们往下走一步。这里看 candidate components 他救出来了几个对象，只有一个，是不是因为我们只声明了一个 I service 所以他这里只发现了一个那循环每一个发现的 candidate 我们看这里它是怎么操作的。


首先判断你这个 candidate 它是不是 annoted being definition 这种类型。那我们这里一定是因为我们上面是加了注解的。那我们正式使用了芬克兰斯注解来声明的这个接口，所以这个 if 条件我们进过来。第一步，把它进行一个类型转换，转成 annotate bin definition 紧接着把这个 definition 的 metadata 也就是主数据给它拿到。那这里它有一个 assert 而设置什么内容呢？这个 bin 它必须要求是一个 interface 那如果你不是 interface 这个 assert 它不会通过，你会收到一个错误信息。那这个错误信息下面已经写明了， thin client can only be specified on an interface 好，接下来往后走，从 metadata 里面拿到哪一个属性呢？拿到分 clans 属性好。那再往下继续走。


之前我们来看一下定义 I service 的时候是怎么来声明这个 class 的。好，你看这里我们有几个属性，我只声明了一个属性，这个 fin class 里面它不仅有 service ID ，还有 context idname dq 404 等等一系列的属性。


这里大家看到了几个以前没见过的属性，对不对？什么是fallback ？ fallback factory 又是什么东西啊？大家不用急，这些属性是后面 high streaks 将要学到的内容，我们在后面会再进行详细介绍。那我们回到断点这里，继续主线任务。这里。


第一步，把 attributes 拿到以后，先 get client name 它是怎么 get 的呢？首先看你有没有声明 context ID 如果你没声明 context ID 他拿你的 value 我们的 value 是什么？我们的 value 就是 eureka client 那他这里已经拿到了。如果 value 还没有拿到，他在尝试从 name 中获取， name 中还拿不到，他在尝试从 service ID 总之一层总归得给你拿到一个值，如果什么都拿不到，那这里会抛出一个什么错。你看他说要么 name 要么 value 必须提供出来。也就是说当我们声明了分 clients 这个注解的时候，你必须给他指定一个 service idea 或者是 name value 等等。总之你要让他知道这一个接口所要代理的对象是需要把请求转发到哪一个微服务当中的，没有这个属性 think 是没法工作的。这里返回。


接下来这一步是注册 client 的配置信息，我们进去看一眼。同样的，它实际上就是在你的上下文中把这个 bin 的 definition 给它构造出来，非常简单，传入一个 name 还有对应的配置项，并且在最终 registry 里面把这个 bin 给它注册进去。


好，那我们返回最后一步，我要注册 thin plant 了。走进来看，第一步是什么呢？ get class name 非常简单。对不对？把这个声明了分 client 注解的类的名字，包括它的路径全给拿到。拿到以后，生命一个 bin definition builder 和前面一步是一样的。在这之前要对属性做一番验证，点进去看它做什么验证。它这里实际上是针对 fall back 和 fall back factory 这两个属性做的额外特殊验证。因为这一节我们暂且先不涉及到 high streaks 降级容错的逻辑。所以说这里暂且先跳过返回，紧接着把所有在分 client 里面配置的属性挨个给它塞进去。


好，这个 name 是 eureka client 也就是我们配置的目标服务的名字。 OK context ID 是什么和 name 是一样的。虽然我们没有配置 context ID 如果 context ID 取不到，它会尝试着从 get name 这个方法里面再次获取服务的名称。
Ok. 接下来就是一堆其他乱七八糟的属性。好都设置完了以后，这里给它定义了一个注入类型是什么？是 out wire by type 根据类型进行注入，而不是根据名称。 OK 往后给他创建了一个别名，这个别名是 context 加分， client 别名稍后会用到。


好，我们再往下看。这里有一个特殊的属性 is primary 这个 primary 有什么作用呢？如果我们现在是在 F 版的 sprint cloud 里面写代码，那么有两个相同类型的 interface 它们继承了同一个 interface 我们可以把它看作是相同类型。并且这两个类型都声明了分 client 同样的分 client 那这里如果你启动项目，它就会报错。为什么呢？因为当你注入的时候，你的 spring cloud 并不知道该把哪一个分 client 注入进来。所以这里就要声明一个 primary 等于 true 来指定，我是带头大哥，每次去尝试注入的时候注入我。 OK 那这是 F 版中的内容，那我们这里用的是哪个版本？
不是 F 版，我们用的是更新的。


G 版 greenwhich 那在 G 版里面，假设我父类的 interface 声明了一个分 client 那我在此类的一个 interface 在继承父类的同时又声明一个分 client 当你注入的时候，你就要额外声明一个配置项。那这个配置项是什么呢？我们暂且不表，等后面一小节我们再来说。 OK 接下来往后看，这些属性大家就走马观花，过掉就好。


酒肉穿肠过到了这里，我们看它是定义了一个 bin definition holder 那这个病 definition holder hold 哪一个病，是不是？就是我们前面已经把它构造出来的病definition ，而且你还给它起了一个外号对不对？一个别名就像 95271 样这样的别名。最后一步当然是要把这个 bin 注册进去，把这个 holder 和 sprint registry 关联了起来，依次来完成了注册。那最后一步我们都看完了，返回到最外层，整个 register bin definition 的过程就到此结束了。


这一节我们主要学习了 enable thing clients 在底层是如何运作的，并且学到了一招在 spring 中扩展注解功能的一个小技巧是什么呢？就是在我们的注解里声明一个 import 并且在 import 进来这个类里面，继承相应的 string 中提供的接口来完成 bin 功能的扩展。大家也可以把这种方式应用到自己的工作中。


可能在业务团队中自定义注解的方式并不多，但是如果大家是在 platform 这种团队制定框架流程的，这种团队中应该经常会接触到需要自定义开发一些框架，添加一些新的注解。那么我们就可以借鉴 spring cloud 中各个组件是如何定义他们的注解以及如何来扩展注解的行为。我们来一个中场休息，等中场休息以后下半场我带大家一起来看 think context 也就是分的上下文是如何来构造的。好同学们，我们下一期再见。




