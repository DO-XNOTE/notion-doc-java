---
title: 5-4 手写IOC容器-4（1329）
---

# 5-4 手写IOC容器-4（1329）

[image](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/f3d54273-8b52-47b5-9c0e-268413001e29/SCR-20240803-syhh.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UX4KIAT3%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T232032Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIF0VF0Ph9aPgqPRRANzxW3wyPH0%2BXFrJByHUTEjTVWdZAiB%2F5SSYbqjq3wjESbKeWbAsA2t6HSxFOF%2FIAQ1lWyAEMyqIBAjG%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIM%2BBOBroUIKySOYRWpKtwDo2wLPr8bzGfYr5odDwH2mcBmn3xwlz9uCV3zeWQmr%2FU4tYmM%2FV%2Ft89l9NJ9f39Sp58mEEj9Bd%2FEUJW%2BBDdXQmIduduRnAM4mBHBUK7QH%2FFlG6mlV%2Fnn3UcQfx7E8WaJegOC1f9czJWfqDP2oru60EvdAzeXWUTjqMrGDH3LC0jGUQ8lkzIZlOFbxcs8fItaDhMevPwTefrlfx1K9lMpvb9JcHBIPWWNaUqpF5svhyKnYQLOlEH3JlWCJ68v1FfgpeIHn59h3kgEWKW2pNKS9udKAjfi2xc99iCkDxRRx9SVE8OngFu%2FvB1jGMq%2F5hoxfdo6KaI9EJpIyeDeAysy1c%2Bbn8nXZorLsIoFXMbRtCJFvth%2F3ITlO59a15%2Ft%2F9UfPa%2FognQqFFKcw5aWRpfPpseWD5a%2FlIjl1A8gxtvB6l2oErAiA4dmmSmoXuWjgQzy5ef5eHV4XCsYp4yqoZ0aoFjN4CJOJ%2FQ1pX4qkeucuSdOzExYMi%2Fnw%2BzVBEUmOQvd6Of0xyYC3lDQF3gY6i5rcdngv%2F2lYw5vSeF2DkgmgP2JZhtA1eiyxCAJ2e6k3viP1hAKVDL4JjPNC4QcfW2%2FImotM%2Be6zvTE4XsJLpZT%2B08hTlRdJcCWJQU2iW2owhrv%2F0gY6pgGzXlvv8FUCD%2F0DbcILenYM3IjsEBtG%2Fkq4CCa02e%2BtQRUnweFa28VZx4AjM9mR7yLge%2FI8d31sv4Ndnj8MfP5aa6O%2BNcSGQQmaRq0cfuzB1lGAodynegPDDvuOLLR8ffHoWosrNYkdwQVxFyXuMQF8PiUXW22ClYiXWh5ka4c4t%2BMC5AkTzcq4URLebY3c%2B%2BPFsPaxD9Yb6vW8PXKvmWQ1AOtf3AHu&X-Amz-Signature=0cbea46c3581f5abc537101bc868c11f58e67198139b3f9a1fd89c1e3f6e4a95&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

接下来我们来创建application，那么对于 applixin context，我们回忆一下，在 SPU 容器里面，它是把其他的 be impact 和一些东西去做了一个组合，那么在这里面我们要去看到其实我们这里面的 application context，它也是对我们刚才实现的 packets class scanner 和我们的 bin factor 进行一个整合。


那么首先我们来去声明一下这两个属性，在这里面我们声明 final 的话，我们就需要进行初始化，我们知道在我们对应的默认构造方法里面我们进行初始化，同时如果说我们没有这个参数的话，我们也可以去进行它的一个默认的初始化，这是我们一个默认构造方法的重量。


对于我们这个 appeal context，它可以支持我们的包结构进行扫描，那么它应该有一个构造方法，这个构造方法它注的方法是把我们的 packs name 作为一个参数传入进来，那么我们来写这个，它可以通过我们的 packet name 进行一个注入，那么在这里面我们需要调用一下this，这样主要是为了解析我们 bin factory 默认初始化的问题。


那么我们现在要需要做的事情是，如果是 packs name，我们需要对 pack name 进行一个注册，那么我们可以实现一个，这样一个方法，也就是说我们把我们的 package 进行注册。同此，如果注册完成以后，我们应该对我们这个方法进行一个 refresh 刷新。


好，这是我们传入 package 的path，那么如果说我们是指定一个 class 的话，我们也应该去做相应的对应的事情，那么我们可以在这里面可以做到一个卡死的，那么对于class，那么我们应该需要支持一个配置 class 的操作个方法的实现。那么好，好，这样的话，我们这样的构造方法的内容我们现在完成了，其实我们参考我们 annotation configure Clinison，它也是这样去实现的。


我们如果说传入过 packet name，它会进行一个首先是 request packet 的注册，进行一个扫描，同时 refresh 刷新一下，那么接下来我们来实现一下这两个操作，一个是 register packets，那么我们再首先来看一下 register packets adjust packs，因为我们这里面有 package scanner，所以说我们这个实现是相对比较简洁的。那我们首先来进行一下 package scanner，进行 scan 我们的package，这样我们得到一个集合，我们对这个集合进行一个注册，这个注册我们要知道这个注册其实我们是使用了 bin factory 去代理去注册这些class。好，那么如果说我们专门指定的一个class，它就会更简洁一下，我们在这里面直接去使用 register cross 就可以了。


那么我们这里面 Refresh 操作应该做哪些事情？对于 Refresh 操作的话，其实它就是对我们的操作进行一个循环的遍历，把我们 bin fix 里面的 bin 都进行一个实例化的过程。好，我们这里面首先Refresh，我们实现一个方法是 Refresh b，我们在这里面去实现我们的操作，其他的功能我们也可以在这里面去扩展方法去完成。那么在这里面我们要做的事情是什么呢？我们首先要遍历所有 bin factor 里面的bin，我们需要有一个操作的是 get 我们的 be names，也就是说我们把所有的必应名称去获取到。当然这个方法我们现在还没有实现，我们去实现一下，这里面我们期望获取到的是一个 bin 的数组，其实我们这里面获取到，因为 being 还没有实例化，我们不能获取到 being name，我们可能获取到的是对应 class 即可的name。好，我们现在继续创建它。


那么在这里面我们会怎么去生成这个 string 呢？我们这里面去通过我们的classmap，我们获取到我们的一个 key side，一个所有 key 的集合，这样的话得到我们这样所有我们的 be name 的集合，这样注入进来。那我们再想一下，对于我们这个 applicon context，它还有什么其他的方法吗？对于我们的一个 application contact，它还需要进行一个对应的差异，就是close，当我们系统运行完成以后，可以对我们的系统进行一个关闭，那么我们其实关闭操作，对于 a place contact 它相对来说并没有过多的属性，那么它的关闭其实也是对我们变容器的关闭，我们在这里面对闭容器具实现一个 closed 关闭，这里面关闭操作我们可以理解为对 map 的清空。


我们首先对 Bing 进行clear，同时我们再对 classmap 也进行一个clear。好，这样的话我们这个简洁的这个 string 容器也就完成了。那我们现在去验证一下我们这个容器能不能达到我们想要的效果。好，我们创建一个车子类，测试一下我们这个 contact 的容器。那么我们第一步我们要测试的是，如果说我们直接去你有一个 packs name，看能不能正常使用。我们首先 application context，那么这里面我们指定一个 packs name，那么我们这里面指定的 packet name 跟我们这个 package scanner 指定的我们设置成一样的，这样呢，我们得到这个 context 以后，我们可以进行一个 being 的查找，看能不能找到我们对应的 context 内容。但这里面我们就需要，我们可以通过里面去获取我们的必应信息，那么我们应该有这样一个操作，这个 b 它可以支持我们的一个类型，我们的指定一个名称。好，那么我们返回对象是一个 object 类型。好，我们去生成一下这个方法，当然我们这里面应该是 b name，这个实现是比较简单的，我们直接用 be infactory 的代理去获取就行，因为它有对应的 get being 的方法，那么同时我们把对应的这里面 bin factor 里面去根据我们类型去获取的，也把它这实现了。


好，那么我们可以在这个单元词里面去验证我们的内容，我们可以去首先打印一下，其实通常我们是关心一下这个里面 bin 的容器的数量，那么我们可以再去写 get 我们 bin 的count，这里面我们是一个 int 类型，那么这里面我们也应该去使用 be infactory 里面的对应操作。我们并没有实现该的 being count，我们可以在里面一写，实现这个功能。


好，对于这个 being count 我们可以去通过我们 cos map 里面的 kid 设置获取到。大家可以想一下我们这会儿为什么不用 beans 的size，而是用 classmap 的size，这也可以去想一下。好，那么我们同时把这个 being count 打印一下，我们执行。好，我们现在看到我们对应的 being count 是三个，那么同时我们得到了 Demo service 的内容也是正确的，我们还是把它改成 get simple，那么我们来验证一下它对应的依赖注入的信息是不是正确的。我们在这里面加个断点，我们去执行看一下它这个容器里面的内容。好，通过这里面我们可以看到这个 applixin context，它的内面属性是一个 bean factory，我们把 bean factory 展开，我们可以看到当前它是有 beans 和 cos map。


这里面我们看到beans，它的 size 为0， classmap size 为3，这个 beans 的数量跟我们预期是不一样的，我们可能代码是有些问题，那我们怎么去排查呢？其实我们在我们执行这个方法的时候，我们会进行我们那个 Bing 的 Refresh 操作，就是 Refresh being，那么跟到这里我们可以看到对于 reset d 这个方法我们并没有实现，那么这里面我们去把它的功能去实现一下。这里面实现的过程就是我们通过 be integrate 去干了病，也就是把我们整个 Bing name 去遍历一遍去获取一下，就能得到我们这个 bin 的实例的过程。那么好，我们现在关闭，我们再重新执行一下。好，我们现在看到我们的 beans 和 clutmap 都是 3 这样一个过程，这样的说明我们这获取的内容是正确的。


好，我们执行完断点，那么同时我们在实现我们这个 piggling contact 过程，我们还可以用另一种方式去执行，我们可以在这里面去写一下，也就是我们去一步步去执行，我们并不用构造方法去完成它，我们在这里面是这样去。


好，我们注册进 package 以后，我们再对这个容器进行一个刷新，这样我就可以进行接下来的操作了。后面的内容我们可以点位是一致的。好，那么我们可以回到 PPT 来看一下我们这个执行的过程。首先我们是执行默认的构造方法，我们在注册扫描b，我们进行我们刷新方法，同时去 get Bing 获取到我们的bin，进行我们的业务操作。进行业务操作完成之后，我们可以把我们整个容器再进行关闭，完成关闭，那整个我们这个单元测试已经完成了。好，关于我们手写框架，在这里面 LC 容器的过程我们就先介绍到这里，同学们，我们下一节再见。

