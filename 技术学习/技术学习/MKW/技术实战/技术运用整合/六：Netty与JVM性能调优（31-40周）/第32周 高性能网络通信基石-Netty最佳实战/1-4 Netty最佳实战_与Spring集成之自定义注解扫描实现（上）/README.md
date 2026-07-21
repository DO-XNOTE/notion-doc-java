---
title: 1-4 Netty最佳实战_与Spring集成之自定义注解扫描实现（上）
---

# 1-4 Netty最佳实战_与Spring集成之自定义注解扫描实现（上）

[image](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/2d157513-26b2-4950-9060-7981290778fc/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466S3X63OTP%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T230014Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCwJ3aX72CKnUhlDM2dxY%2F%2FZYABGCfg4RhBtJDlUJ7VxQIhAKFdjz21qxzxLN0eaN%2F5f7CT06vWTH4y%2FwxSDP55TN3VKogECMb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1Igyof1acU63nTHqIVioq3AP1vpifYL3EExoxPfIKw6TqXqA0qsH0EUAx6GnqzST9mD1%2FBRytAs6FRkWvKsVX33fHLe1k7P20nSltnImQCP%2FeiyiLJ8C4K4jUgrzo20LDQ33JPcW4kpy0BZq2YFJGlIlRjHHG3AvoQ3lOt6AJUlBfQ08al0VyyK%2BrQOHcB7qAt%2FgJLccSPFcILa15RVOAwulKnBBydgVQNdPEFfay5s%2F8nHlAR0UqaNOmbg%2Bk%2FSdnvjhSpAdCqpLgQdKPO4dUlji3AqadEpRMJaNvARsEiYXCx%2F%2BwLFVHar2IuhPIFbE0f1D8rp9OAYLoFla137YygDHdgSosZB6ONlJz%2Bx4b80mU2ObA7nWG6H4Hyo3d5JqzN9xhipvXPYBfLtjLLz9FTAKM41v8uGdYnwD1fJtRAzMa6V0KQY6PylQqyx9n1zkhc06n0XmHU5SVoujwegp0QFUFpSHChroRvb%2BldCzU%2Fs1nymTNyLHzLvqRs%2F0oZqjjw%2BrCL2NSXbRfBl9F1SGVlohxDZvvkFvEJt6WD0u7EE7rSB4lQ%2Fk25yGeMS9Rl5x0vvw0BRkEzvZLmD3Qxf3tYvy%2BxYvH43MWxJoLXzvvaZVTYMpa0U%2F5S9gl7QK7a2KfyyUUZvKMGl%2Bl1ixWazCHt%2F%2FSBjqkAS1X6l4kccJbuvKCdo0D%2FXWJ4H29pW92BYBqcbD7bGHqAw%2BNUmaDS3JOhx1LiDENQSYMB1Mnyza4royXJbyBF1L8gNgxGgE7eLih7rEpt2Wmi1fGrp8XYGfm03nG2rTBjzpTusm5MhXyV7t0GOfNpiWuXQRpQQcog50%2BJF6lzhAHxrGKkujdnzoAHgPTV8k0ZlIyeC4hYJWG%2BJtYWJLlgjhCwWxt&X-Amz-Signature=48d9797630b9ce2d2ba1791a5f959c626d66f2044d21e409d07375ab8e75b6e4&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

OK 小伙伴们大家好，这节课我们开始进入真正的编码。刚才我们数据包结构已经定义好了，接下来我们看一看我们要做什么事情，还是我们要看到这个了？看到这幅图，可能要从头看到尾了，无论是我们现在已经把不同的模块还有新增，修改，删除。这块用我们的 message put buffer 的message。数据包结构已经定义好了，接下来要做的事情是什么？接下来要做的事情就是我们看我们右边不同的处理逻辑。我们现在用的是 net 网络通信。 net 网络通信。
最终我们要跟我们的 spring boot 进行一个集成。怎么去跟我的 spring boot 集成？这就是一个大的问题。同学们想一想，我们看到了，对于 spring boot 而言，它其实就是spring。我们具体的一个 at service，下面有不同的save， update 以及 delete 方法。对好了，也就是我们现在可以从 at service，也就是 spring 的 bin 去着手。

[image](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/f1b97bea-0326-4574-a687-6728bd6ebe0f/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466S3X63OTP%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T230014Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCwJ3aX72CKnUhlDM2dxY%2F%2FZYABGCfg4RhBtJDlUJ7VxQIhAKFdjz21qxzxLN0eaN%2F5f7CT06vWTH4y%2FwxSDP55TN3VKogECMb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1Igyof1acU63nTHqIVioq3AP1vpifYL3EExoxPfIKw6TqXqA0qsH0EUAx6GnqzST9mD1%2FBRytAs6FRkWvKsVX33fHLe1k7P20nSltnImQCP%2FeiyiLJ8C4K4jUgrzo20LDQ33JPcW4kpy0BZq2YFJGlIlRjHHG3AvoQ3lOt6AJUlBfQ08al0VyyK%2BrQOHcB7qAt%2FgJLccSPFcILa15RVOAwulKnBBydgVQNdPEFfay5s%2F8nHlAR0UqaNOmbg%2Bk%2FSdnvjhSpAdCqpLgQdKPO4dUlji3AqadEpRMJaNvARsEiYXCx%2F%2BwLFVHar2IuhPIFbE0f1D8rp9OAYLoFla137YygDHdgSosZB6ONlJz%2Bx4b80mU2ObA7nWG6H4Hyo3d5JqzN9xhipvXPYBfLtjLLz9FTAKM41v8uGdYnwD1fJtRAzMa6V0KQY6PylQqyx9n1zkhc06n0XmHU5SVoujwegp0QFUFpSHChroRvb%2BldCzU%2Fs1nymTNyLHzLvqRs%2F0oZqjjw%2BrCL2NSXbRfBl9F1SGVlohxDZvvkFvEJt6WD0u7EE7rSB4lQ%2Fk25yGeMS9Rl5x0vvw0BRkEzvZLmD3Qxf3tYvy%2BxYvH43MWxJoLXzvvaZVTYMpa0U%2F5S9gl7QK7a2KfyyUUZvKMGl%2Bl1ixWazCHt%2F%2FSBjqkAS1X6l4kccJbuvKCdo0D%2FXWJ4H29pW92BYBqcbD7bGHqAw%2BNUmaDS3JOhx1LiDENQSYMB1Mnyza4royXJbyBF1L8gNgxGgE7eLih7rEpt2Wmi1fGrp8XYGfm03nG2rTBjzpTusm5MhXyV7t0GOfNpiWuXQRpQQcog50%2BJF6lzhAHxrGKkujdnzoAHgPTV8k0ZlIyeC4hYJWG%2BJtYWJLlgjhCwWxt&X-Amz-Signature=676344ec4f5fd499c3f8bd5b09996779cebe8635f3212de3b59d534b1e69a058&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

我现在想做一个什么事情？我现在想定义一些我自己的注解。我定义一些我自己的什么注解。我能够在我的艾特 service 上加一些我自己的注解。通过扫描的机制扫描到有什么作用？我把它放到，比如放到一个table，就类似于 map 的容器里。当我的对应的一个什么，对应的一个 modular 以及command，它组成的唯一的一个程序组成就是 module 跟command。我可以指定 user 的 save 方法，就可以去指定了。指定到 save 方法。我只要通过这两者的结合，找到唯一的一个方法就可以了。很明显，我们只需要做这么一件事情就好了。我们现在来做一个注解的定义。在这里我还是在 common 包下面去建立我一个package。咱们叫做 Com 点b，f，x， y 点什么？咱们叫做annotation， annotation fantastic。这个包。


我们来定义几个注解。首先我们来定义第一个注解，就是我们刚才所说的 module 了。还有 come on 的注解。 module 的注解，我们可以简单的去给它一个属性，比如 module 的属性，比如我们给它一个value。因为我们看一下数据结构。它的数据结构。我们来看一看module，它的数据结构既然是 string 类型的，所以我们直接给它一个 string 类型的 module 就可以了。好，我们在这里直接给它一个 string 类型的，叫做modular。可以。好了就可以了，我们只需要就可以了。它能放到什么？它可以在类上。


我们来写一个叫做target，这是 annotation 的一个注解，没什么可说的。你的 retention 是什么？在这里哈，我们这都是 annotation 哈，target，我们来给它。咱们是有一个叫做 element type，点 type 好，对应的 retention 就是我们的 retention proxy，等于 run time。运行时可以去给他找到。这样的一个注解就已经搞定了，非常简单。就是我定义模块的一个注解。


接下来我们再定义一个注解，就是我们刚开始说的 c m d， c m d 也是一样的。好，我们首先有一个target，它也是element， type 等于type。接下来就是 rotation t i o n rotation，它的 rotation proxy 等于 runtime 就可以了。


c m d 里面有什么样的注解？我们直接给他一个，也是尺寸类型的。刚才我们都看到了我们 c m d 注解就好了。好了，现在我们的注解已经定义完毕了。接下来我们现在来写一下假设。我们先不着急实现这个东西，我们来看一看。假设我们的对应的肯定是 server 服务端，哈，服务端里边，如果你的服务端想去调用我们的什么，想去使用这两个注解，应该怎么去用？很显然是这样的。比如我们在这里边再去来一个package，叫做 Nike 点什么？点service。 OK 有了一个 service 这个包，我们来定一个 user service，来，我们定义一个class，在这里我就不写接口了，哈。我 user service。有了 user service，我首先我得把它交给 spring 去管理，所以有一个 at service 注解，这是必须要有的。接下来比如我怎么去使用刚才我所定义的这两个注解。很简单，我就去 at model 了就可以了。


at model 了。 module 在这里边我一定要定义我 module 的它是什么内容，我这个 module 是什么内容，它肯定是一个怎么说，它肯定是一个对应的 string 类型的，我们直接可以写死。或者你用一个静态的类去做都可以。比如我们在这里最开始制造的，我觉得你是小写的哈，写死了user。好了，这里边肯定有一些方法，比如有一个 save 方法，在这里我们写public，比如返回值类型我们暂时不知道哈，可能返回的是 OK 什么的。我们暂时就写一个 save 方法， save 它里边具体执行的 save 的逻辑， return 一个nut，先返回空。


有了这个方法了以后我们再来一个public，比如是一个还是有返回值的，比如是一个 update 对不对，我们再返回一个 update 好了。当然这里边肯定有传数据的对不对，我们暂时先不去考虑这些，我们先把模板写好，比如现在有一个update。好了，接下来就是在具体的command，我直接在类上加c，m， d 就可以了。具体的命令是什么？命令就叫做seal。这就可以了。


好了，c，m， d 它的 type 也是可以的。这里边它有个报错，他说什么？他说 annotation is discuss this location。他说不能放到这里。是不是不能放到这里？我们要把它稍微改一改，给它改成能够放，把它换一下。现在是 element type 换成 method 可以了是吧？这样就可以再方法了。它只是存在于我们的方法上，哈，叫做 save 方法。在这里边咱们再给它一个叫做 update 方法。


这是我们自己定义的一个约束，对不？现在问题来了，同学们想一想我们的 spring boot 跟我们的 net 进行集成的时候，我们已经定义好了这两个注解以及 model 了。我怎么去把注解找到，给它放到一个地方？这就是一个问题。很简单，同学们想一想，花一点时间思考。


我们在 spring 并初始化的时候，并初始化肯定会有一些并初始化的逻辑，对吧？其实我们可以在挑一个 spring 的生命周期，在它初始化的时候，我们把它扫描出来。最简单的，我们去定义一个模块儿，定义一个package，咱们叫scanner。OK，定一个包哈。在这里面我写什么？写一个类哈，这个类叫做Nike，是canner，可以随便起一个名字哈，叫 native scanner。这个类。我是想做什么事情？想，首先它也是让 spring 去管理 at component，这是一定的。他去管理做什么事情。 component 我在这里边是不是没有 spring 的依赖？sorry，我们把对应的 spring boot 的依赖也搞进来，没有办法。怎么找不到对应的component。注解其实你单独可以去引 spring 的包哈。如果你不去单独引，你可以自己去找到对应的。我们现在用的 spring 的版本是什么版本？把 sprint 版本也引进来就可以了哈。在这里老师就偷个懒吧，我把副 Pom 还搞进来就可以了哈。是 parent 搞进来找到圆。


其实正常来讲我们应该去指引他 spring boot 里边的对应的 spring 的集成的 call 就可以了。我其实可以在这里面加一个parent，我可以去加一个dependency。 dependency 肯定就不是一个 web 项目了，哈，它就是一个 spring 的 starter 就可以了。


哈，就是一个 spring boot starter。把 web 去掉，它不是 web 项目。好保存好。这样对应的它的一些 spring 相关的依赖在我们的 common 包下面也有了。哈，咱们耐心等它去加载好了之后，我们去 update 一下。好，已经 OK 了。这样我们在 native process 看到我写一个native，怎么说？ native process c scanner 这写的有洁癖，肯定是 net 的程序，但是是bin。好，我要做一个扫描。哈，这个肯定。第一个就是 at component，这回肯定会有了。 add component 是 strain 的，这个类需要实现一个接口，大家注意看，这个接口我会选择一个 spring 的生命周期。


咱们叫做 being post processor， bin post processor 是在我们类加载完之后，他去做的一件事情。搞定完它之后把它保存。它可能需要重写两个方法。我们点击它的父类重写哪两个方法？在这里边我们可以去写一个叫做before，这个 before 是在并初始化之前，我们肯定是等到并初始化之后，所以我们肯定要重写。这个方法就是我们的它。在并初始化之后，我们做一些事情。并初始化之前，我们可以直接 return 一个bin，都没什么太大问题哈。把两个方法直接拿过来，我们直接放到这里。当然把注释什么都去掉。这里边肯定是 public 哈，把它去掉。


bin 初始化之前，我们可以不做任何操作，但是 bin 初始化之后，我们要做我们自己相关的事情。在并初始化之后我们做什么事情？我们来一起把代码去完善一下，其实才是核心。哈并初始化之后的时候， after in intellectual 我们去做什么事情？同学们想一想。当然最终返回肯定是也要返回bin，这是没问题的。首先我们通过 bin 可以去取到它的class，找到它的 class 了之后，我们其实就可以知道它 class 里边有一些对应的方法。什么 is annotation persistent 是否存在？注解 OK 我们就可以做一些自己相关的事情了。


首先在这里查注释。第一步首先获取当前 bin 的 class 类型对不对？叫做 bin 第二， get class 返回的是一个什么？返回的是一个 class 类型对不对？它肯定是一个。我不知道它是什么类型，我可以用一个不确定的去接受一下。好，我们叫做 c l a C z plus。 OK 知道了它之后，接下来我们要做什么事情？我们看看这段代码。找到了它，我其实可以去看这个类上点 is 它 sorry 是 class 哈。有了 class 之后， class 点 is annotation 诶， sorry 着急了哈。 is annotation 的意思是说有没有注解对不对？它还有一些其他的类对不对？


Is annotation persistent commission?
到底有没有指定的注解？我们其实类常放的是什么注解？同学们看一看我们之前所写的模型你就知道了。在 server 我们其实只需要找注解就好了。对，所以就是 model 点class，判断我们的病上有没有注解。如果有这个注解，我就可以去证明这个类是我想要做的哈，我想要找的事情对不对？如果有注解，它返回一个布尔类型，我们去接收一下。


孤儿类型，我们叫做起个名字哈， is persistence。Ok？好，到底有没有，我们判断一下。如果要是有，我们去做处理。没有，我们压根就不做处理。是不是没有你，根本上你就没有 model 的注解，我就干脆就不需要扫描，有注解我才去做。有注解之后，我们可以通过什么？我们可以通过它 class 我们都知道了，我们可以通过 class 去获取对应的它的method。 get a method 丝，我们可以通过得到反射的 method 丝，这个类，我们用 method 的丝哈。 method 咱们是 Java 点 reflect method 哈，咱们叫做 METHOD 4 哈。


METHOD 4 取到 METHOD 4 我们做什么事情？我肯定就是循环做一系列的循环。好，我要取到这里边的内容，我判断它里面。我其实可以先判断一下，看看它 mess 是不是不等于空，如果不等于空，并且它的masos，它有方法吗？是不是它是一个数组，所以它的点 lens 如果是大于 0 的时候，证明这个类里边有方法对不对？有我想要的方法。sorry，哈，我可能才去对应在走里面的逻辑，所以有些事情你要稍微写得稍微严谨一点。


我怎么去做？我看 method 上有没有annotation，有没有对应的 CMD 注解对不对？所以我就可以 for 循环，因为它是一个数组，我们就可以做一个循环。 method m 就是一个简单的 for 循环。我循环什么？内容很简单，我想去循环 method m 里边 get annotation 在这里边。


在这是不是？是否有 c m d 注解，能不能取到？如果你取到了注解，证明什么？我可以把它返回哈。我叫c、m、d。如果有注解，我去做对应的解析哈。如果你的c、m、 d 等于是烂，我就不做处理，我直接跳过。是不是直接continue，让他继续去往下去循环下一个方法。


continue else 的情况下，我们去做证明。是我找到这个注解了，不还简单嘛。我们取到注解所对应的内容。我们取到什么内容？其实从这里我们就知道 model 其实百分之百已经存在的。其实我们可以把 module 类型以及c、m、 d 都拿到，因为 module 是最开始进来的时候，模块类型是固定的，是user，因为我们看到了，找到我们的模块类型就是 user 了。 CMD 找到他是user，他们模块类型的值跟 CMD 注解的值就是我们的命令。它们两者在一起才能形成。唯一的就是定位到唯一的方法，某一个类下的某个方法。接下来我们要做的事情就是来做一个赋值，当然它都是这里形的。是不是咱们叫做modular？这个叫做 model 的value。这个值到底是什么？是不是我们直接通过注解里边他给我们带了 a sorry。当然注解如果有，我应该去临时的去取一下哈。所以还是在这里边我去再调一下。


get annotation 通过，因为我 class 我知道了， get annotation 去取到。如这肯定是有，我要再取一次。刚才上面只是判断取到我们拿到 module 了，咱们叫做module。好， OK 取到之后是不是我们拿小写的module？当然这是我们自己所定义的 annotation module，没问题哈。拿小写的 module 调用 module 的方法取到具体的 value 值到底是啥？同理下面的一样，我拿到小写的c、m、d。


第二c、m、 d 方法就是取到我具体的命令，到底是什么？我可以值，实际是什么？对不对？我们叫做c、m、d、 y 6。取到这两个东西，接下来怎么去做？同学们想一想，接下来你要把这两个东西放到一个地方去缓存起来。为什么这么去说这两个东西？缓存什么东西？肯定是缓存这两个内容，它所对应的是一个缓存的对象。其实我们确定了 module 了和 CMD 的值以后，其实我们就可以通过一种机制去直接帮我去调用私有方法得到返回值。


什么方式？最简单的去 Java 的反射的机制就可以去知道，我们只需要知道它这个对象以及 target 对象知不知道？对象肯定知道，就是当前这个bin，因为我们去找到了当前bin，它就是实际的对象。方法知不知道？方法肯定知道，因为在这里边我们能拿到m，拿到对象，拿到方法，我可以直接通过反射去做操作，所以后面的事情就简单了。


后面的事情就是我们两个有了以后。我们只需要在这里只需要把对应的反射对象我们在这里我给它起个名字，叫做尹沃克。只需要把对应的反射对象和我们的这两个属性。只需要把怎么说这句话组织一下，重复组织。只需要把它和加上他的值与对应的反射对象对不对关联起来，或者是管理起来。


肯定这里面最合适的就是用一个我们的 map 是最合适的，用 Java 的哈希 map 或者是 Concart map 都可以。 OK 这是最合适的。接下来的事情，比如如果没有，就是找不到哈，或者你写一个报错，或者怎么样都可以。接下来的事情就是我们怎么去定义承装对应的这两个值，所对应的一个inworker。这个肯定是一个key，它肯定是一个value。怎么样去组织起来我们下节课要跟小伙伴们去讲的事情了。好了，这节课我们就先讲到这，感谢小伙伴。

