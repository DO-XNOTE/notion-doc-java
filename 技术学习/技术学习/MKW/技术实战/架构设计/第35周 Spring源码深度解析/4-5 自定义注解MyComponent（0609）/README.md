---
title: 4-5 自定义注解MyComponent（0609）
---

# 4-5 自定义注解MyComponent（0609）

[image](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/0a0c4e78-5781-4e77-8bd9-84fe4c219a71/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662DWZIPFN%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T232029Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQC2ys0rhV1vNDQEnP12VwRl6IMcEcvo%2Frq9v6RFVMEjQQIhAOqODknqjnzysbwEjODlySSrl8%2FkTuRaGnNjHWrl38dZKogECMb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1Igz0qMzU61BvVF1MSi0q3AOWp9y0AtuThF2bohvL%2BTwJMfE9YPipmhA%2B9inLEndtRuHWWgDlKVhxKteCRaMHwDFiuDVrDTIzDHZ2da6xDljBeJ78D2dujoOajyXj3%2F%2Fy6KKG0aPrlNNPo74cLH8Cj7uSOhIOBn6WWXYgw9MP5Tr8KFpOquhRhHkVwVVcPy0cT4h94vWnmwjHgIdrpHf2AUx%2Bd2HEMuxfdetPx0bZnFLdwVulWUEg8d3iRCxKiXaE4GLoUtZFPGc1dMItTsbfYDD802AQkmsrPkAdRWXMHXnspy0u2QVpVAoD1uok0SYFTqh3eeQJBWeF7vuw1VHiQn4eokIIr1mCH9ASXaLGbIlXGSuYREGjxMnQK8H26ilwhPNf3NW4WWtkQJRvzknebAJ9tTFyqg7u82ArRS59ygEYEk%2BUNfoZFPx6e%2BWDZDrvXA5mBO9jCHeYc7RqL2rPbJgWmyF6G0wC%2Bz8l35u7n%2FDT%2BzSOFOM8jcgMppRuQe%2BYzT6y08reNja41NebjcpgfgC9po9kHJx%2Bs2jeYA8INdLpSKZoCA9GbqP8wv44%2BV1ZGCRgbAA3RQEBfprnYwyq9LgVdAzE1KcVBAhp7qyVKKjH3kCbQDZJVyUBepM%2FDm2hw456Z7PO9o8vadBwXjDXuP%2FSBjqkAbuR3OkQCeBUid7MCzprdv%2BA%2BfrYuO7z%2F78mLWGNeSUn%2FADEEMNiybqT0j7wM28UcFJxHT9lm3hypoSGZfHkMSsqX85vXCXmXTL4SYjEpu5EP7UzSRv77JGZW6ew9hX0tOyjIkyAZvg%2FoLzsQNWIelG9Fk3Z7HmvrlvIf42fT1ZpKlejDCDDm1taMniqcrRWz5j5kpezgwM56EPhqJZoRI4mRuCb&X-Amz-Signature=88fd0d291b0dec68e30d21d8caf69d3b065b09aff76c2d98a8d82352fa6df848&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

同学们大家好，这一章节我们来介绍一下子不用二次改造里面的自定义注解，也就是我们注定一个 my component，用来替换对应的像 ad service， ad reposer 这样的一些注解，现在在我们的工程里面去跟大家去演示一下。首先在这里面我们定义一个对应的注解，当然这里面我们先指定我们一个包结构定义 my competent，这里面我们注意要选中 a notation，好，我们现在完成。那么在这里面我们可以看到对于 my competent 这个注解，我们需要注意哪些事情？可以参考一下 stream 是怎么去构造的，可以在这里面看一下 ID come back，我们看一下 stream 默认的 component 它是怎么实现，它这里面有指定 token 的，也就是说这个注解呢要用到一个类型上，也就是我们对于类上的取准，同时这里面指定一下runtime，也就是说我们这个注解需要在运行时序执行，所以说在编译器的话不应该把它给消掉。


这里面还有对应的 document 和 index 的，那么我们通过这秒可以参考一下对应的 repository 和service，我们可以参考它的内容。对于它跟我们这里面 component 它的区别是我们可以看到对于 repository 它间接的去使用了component，我们可以在这里面去看到它还指定了一些对应的别名，我们在这里面是可以把它参考过去，那么好我们这里面去写我们自己的 my component，同时我们可以看到这里面对于这个 value 还做了一些修辞，对于repository，它的 value 同步于我们 competent 的value，可以把这段内容也拷过来。


可以看到我们通过参考 string 对应 reposure 这个注解的方式构造出我们一个 my component，那么这个 MIM component 这个注解它的使用场景是什么呢？那么我们可以在这里面去做个例子，通常我们会设置对应的 demo d o 和 demo service，那么假如说我们有个场景，我们需要一个 Demo manager，我们可以看一下，我这么预热，那么有时候我们对于业务比较复杂的话，我们可能需要在 control 层和 service 层中间再加一层 Demo manager。


对于 Demo manager 我们用哪种注解方式修辞？对于这种方式我们自定义的这种注解，当然我们也可以在这里面定一个注解，这个注解就叫manager，基于这个注解去做我们相关的一些事情。我们创建这个 Demo manager，它可以去依赖我们的 Demo service，对应，我们也是只是讲它对应的这个操作的逻辑，把对应方法去把它给拷贝过来，这样去实现我们的功能。同时这里面我们把 demo d o 换成 demo service，这样的话整个逻辑就已经完成了。基于这个逻辑完成，我们看一下我们在这里面定义的这个 my component，它有没有起作用，可以通过我们的单元测试去验证一下。好，这里面我们去构建我们的单元测试。


好，虽然是执行 create Demo model 能，我们重点还是去演示一下有没有把我们这个 Demo manager 装载到我们的 spring 容器里边。我们现在去写我们的逻辑实现，还是在这里面先构建我们的测试内容。好，好，我们参考这个内容， i m 在里面 shoot 标记一下add，清理一下业务。


好，现在我们这里面需要做的是我们去获取一下我们的 Demo manager，当然因为 Demo manager 它并没有实现 MOS 接口，那么我们就让它把 bin 来打印出来就行，我们这个 Demo service 可以保留，这样保证我们所依赖的内容是有的。


好，那么现在我们可以看一下整个这个执行的过程，它会扫描我们这个跟 Demo model 相同的包结构，这里面也就是对应的这个 bug 结构，它下面所有被注解修饰的，像这里面我们用 add repository，当然这里面我们有自定义的 my component，当然这里面 demo service 我们是特意把它给关闭掉了，我们是使用 package 方式去构建这个 Demo service。那么如果这样我们能在我们这里面获取到 Demo manager 的话，说明我们的 my companion 这个注解是生效的。


好，那么我们现在来去执行一下，可以看到现在获取到了我们这个 demo manager 这个b，也就是说我们在这里面去使用 my confident，这个注解也是这里面跟大家去介绍一下，这是在 spring 容器它的解析的过程中看到这些，它在解析的过程中通过这个注解它们的复合注解去找一下对应的注解有没有依赖 compend 的，也就是说有没有通过 component 注解去修饰它。如果有这个注解修饰的话，那么它也会作为一个 spring 支持的注解循环的去处理。那么其实我们这里面对应看到的repository，它的解析的原理也是一样的，因为这个 repository 注解也是在这里面通过 IN component 的方式去修饰，所以说它也能去识别repository，这是我们的自定义注解的一个方式的实践。自定义注解的内容就先介绍到这里，同学们，我们下一章节再见。


