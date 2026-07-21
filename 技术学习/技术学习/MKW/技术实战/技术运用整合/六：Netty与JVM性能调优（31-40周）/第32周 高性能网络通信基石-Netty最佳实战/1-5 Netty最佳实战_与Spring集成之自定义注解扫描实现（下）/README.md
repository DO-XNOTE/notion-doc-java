---
title: 1-5 Netty最佳实战_与Spring集成之自定义注解扫描实现（下）
---

# 1-5 Netty最佳实战_与Spring集成之自定义注解扫描实现（下）

[image](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/0aae224c-30bf-4d8f-903c-10a60706622e/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663WTROR75%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T230014Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIE3Xt4%2FUORRz35tXFfDuwK%2F5G3CT4YgYGr0vH7rVXywsAiBOdVWVsvMKAttmlxg6ygGVVWK9ype8KDv4Q33MJRz9%2FCqIBAjG%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIM9lWklNLCJG5F5UyLKtwDIC42DtlMRq80cftFZa00P4IIc6AH0DZ6yaRHEbDPBymQX8Xd4ppzxzaYcuw9Pr5Rv1FcKlaE1ABMb23%2Bt5Pxe%2FBT4ss0ZlEZDyaHOzTmEucwi36i2Znl7PjoOSVC7BdCYzwl6ElNcNgAh0IGH7DYvBNewdXQtXgqYqYV6n%2Ba%2FQ7cULQx%2BoQGJqJ917jst%2F3imsXAKsTTAsB69AExw6rbBixeCxMvZDYpqD95AJHPE1Evg75FEK59y4ZE%2FV6zUvUO6JyjM8f3myWbkPQFfst7aRhLmBrUW44ztLsrg0YJZ9xbUCgt7zYmxTOloM79dLuyX%2BFpTTKY4vfeIBog2P%2FaIDSgZhtdFqvkmPBsJgGxEvRGhANmTW34lovcW5ex%2FbzO%2B%2BP2NAQCXM9%2F2vlP8IFdWjJcEbqpLA3yDK7LziHHBouu7OYT%2BVUM71n1CYOZCp%2FNcajwf9OFpv1kPLDWhfIX0wd41%2BEzV4B7Lb%2F6EjtyV9VmiELnOqGYjWVu9e%2FyObPoFnG8TqxycqovXupmARVSmNzAuJFJWSNTSHz6Ocm8Kjc4SqIkbBT09EPYir4VY0wdxgjTH2r7%2Fp%2BmVq0hBO4ZEEsA%2Bcddxr05EDSEyzUenL%2BzC%2FGC9z2DRV2g5rgwpLf%2F0gY6pgFC%2By3R2QfnWXlExqUqa312IZDiSyJNb77FeHu8dJ%2FNr%2FjfZDnjN3k%2FB0m6%2FLqisduEg1u952BljclDj9WzrXjEFcBAFvQhcGpNn1jbNwfoKElykQtfYnCWsgNG4y2GcTfzVaJX41gaYHzEKattKHu%2B5JEt%2FIuKuOw%2B3S4UtaqEdzEkxOFB47T6JV0VK%2BTSvNmHxGjB3dNiBPgeSUjMekPnWAjhogu3&X-Amz-Signature=c94c4276c539cf1c0a68edfc2fa5cda815b1304cd9a4840481a9e7c396d1a8f1&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

OK 小伙伴们大家好，咱们来继续开始往下去走。上节课我们已经分析过了。我们用 process bin post processor 去把我们自己所定义的注解，去通过判断类有没有注解的方式，以及判断方法有没有注解的方式去获取到了，也获取到了它真实的 module 跟 CMD 的值，也就是已经获取到了。假设我们的 user service，它的 save 和 user 对不对？ OK update 当然也可以获取到，因为我是一个负循环的便利。其实最终我是要把它们两个的内容加上我们对应的反射的对象值。你看，以 module 的 value 加上 command value 与反射对象进行管理起来，其实可以把它存储到 map 里边。


首先我们来看一看第一点我们要接触的一个问题中， inworker 我们怎么去定义，对吧？你首先得创建 inwork 对象，把它跟 module 的和 command 去绑定在一起。我们来看一看首先怎么去创建inwork？在这里面我们去 new 一个 Java class，咱们叫做inworker。可以来我们来写一写。


首先 inworker 比较关键的类，sorry，就比较关键的属性，肯定第一个是private，我们的 method 是不是？你具体是什么方法？ Java reflect 的 method 肯定得需要有的，这是第一个比较关键的。第二一个比较关键的是什么？你的目标对象就是你的 class 是什么，对不对？因为我们反射都知道你得需要用到目标对象，我们叫做target，有了 target 之后，这两个之后，我们来看看怎么去创建一个invoke。我们可以定义一个类，可以是static，静态的返回值肯定是一个inworker，我们叫做 create inworker 可以吧。


creating worker 把里边我们想要的属性直接放进去就可以了。首先第一个是我们的method， method 逗号，第二个是我们的target，咱们叫做。当然这种类型它肯定是一个object。好了，有了这个之后，我们去做一个创建，我们就把 in worker 的像是 new 出来就好了。 in worker 等于 new 一个 in worker。这里边肯定得提供改善属性。我们来 data 就是 long book， long book 对应我们也把这个拿到，因为我不想去自己手写。 get 方法 none book long book 我们直接放到 common 包下就可以了，对吧？把它放到最后好了。有 long book 之后就没问题了哈。把这 client 端 run book 也去掉。注意其实你必须得从头开始，跟着我一起去敲代码，这样你才能知道我有些地方加了一些什么新东西，做哪些修改你才会知道。很明确。如果只是看视频看一半，这个就不太好。 OK 这样你没有一个完整的跟着老师一点点去做这么一个过程，我还是希望有这过程的哈。


set method 是什么？那就是传进来的 method in worker。点 set target 哈，对不对？ target 就是传进来的target，最后返回 inworker 即可。好，其实这样就已经把 inworker 是不是诶？这样我们就已经把 inworker 弄出来了。每次去创建的时候只需要创建 inwork 就可以了。接下来 invoke 有什么用？它起码它最关键的方法就是我们要去调，引入worker，让反射去调用对不对？好了，怎么样去反射去调用很简单，在这里我就写一个最简单的public。反射类型我都不知道哈，我就直接做inwork。方法。参数我也不知道，我是object。参数点我们叫做 parameter 思可以，反正我叫做 param 丝。具体的方法里面的参数我也不确定，所以只能是用这种泛化的方式去做一个封装。


最后我们method，我们有 method 点， Ework 是不是直接就调用了？ object 就是你传递的 target 对象， x 就是我们具体的 params 参数。 OK 直接搞定。搞定之后它这里边要做一个catch。sorry，我们直接 catch 不往出 throw 了。我们有个 mullet catch，有个catch，我们一个 catch 就好了。它有这几种方式。好，已经写完了。最后如果找不到，就 return 一个 none 就可以了。好，我们把这个方法写一下。这个方法当我们存储了。创建是不是创建 inwork 对象对吧？创建 work 对象 OK create in work 方法创建 invoke 对象就拿到了。 invoke 对象，我怎么去调用？比如我拿到了 invoke 对象， modular 跟c，m，d，它们对应的是 user 下的 save 方法，我怎么去调用对不对调用？我在这里也提前封装了一个简单的反射调用，对吧？在这里做一个，反射调用返回方法的执行结果是不是 OK 好了，非常简单，这样我们已经对 e worker 已经封装完了。


接下来的事情我们怎么去存储了。怎么去存储？我们其实可以去建立一个 class 就可以去做到。比如我把它存到一个 Hashmap 里面，或者是一个 concurrent map 里面都可以。我们在这里面写一个 inwork table，我们起个名字叫做 inwork table。 inwork table 的目的就是为了去保存 inwork 对吧？保存什么样的involve？在这里我先把保存的内容咱们先定义一下，咱们就用 concurrent map。


concurrent 哈希 map 这里面的 key 是什么key？你可以认为我的 key 是不是可以是一个 string 类型的，叫做modular，可不可以？ value 是什么？Value？其实你可以再去往下去走。我如果再创建一个map， value 就是一个map。这个里边我给它起个名字叫做什么？叫做 inworker table。 in worker table 等于new。一个常态行哎，又一个坦克人的Hashmap。当然泛型。我现在还没有去定义好。sorry，我不能这样去写。我这样去写肯定是不对的。我说我怎么一直没点出来。所以我们的 key 它是 string 类型的，它里边一定要存储的内容就是什么我们的 model 的对象value。我说它是一个map。为什么这么去说？因为我再来是不是好，这里边来看。我说在是 CMD 这个里边具体的是什么？是一个隐魔可对象。好，我这样去写，小伙伴们应该一定能看懂。我把它最大化 north table 回收。这里边泛型我直接 copy 过来就可以了。也就是我们对应着一个 module 的下面，它对应了一个map。当然这是 2 层map。


注意小伙伴们，第一层 map 主要解决的问题是什么？主要解决的问题是我到底是哪个module？一个 module 下面肯定有多个方法，每一个方法肯定是对应一个uworker，因为我 inwork 封装的是这个方法，以及目标对象调用的是 Inwork 方法去调反射的。所以我们结构都已经定义好了。


定义好了结构以后，其实我们给它提供一些add，get，还有删除等等一些操作就可以了。当然在这里就更简单了，我们写public，比如我们怎么去添加一个英文课 why 的返回，哈。比如 add in worker。它里边需要的参数一定是那几个，比较关键的。


第一个就是module， command 和invoke，就这三个属性了，好，直接拿过来。第一个就是 NO do 了。第二个是它的对应的c，m， d 是什么，以及它的 inworker 是什么。你我可。好了。就这 3 个属性怎么去做？首先我们从通过第一层，通过 model 的取到 map 里边的最外层map，通过 invoke table。 Forget. Okay. Talk to she. Study. 通过它点 get 最外层的就是我们通过 module 取出来。 map 集合。肯定是一个什么？肯定是一个。里边的 map 就是 CMD 跟尹摩科的这么一个 KV 电子。对哈。所以我们在这里返回一个，直接 copy 过来。咱们叫做什么？咱们叫做Michael。


得到 map 之后，我们判断的是为空。是不是为空就创建一个等于null，如果为空就临时创建一下对吧。 map 等于 new 一个，这玩意，我们写一个哈希 Mac 就好了，哈，让行给好。另一个哈希。 map 搞定了之后，然后再把它 put 进去对不对？因为我是inworker。 inwork 点 put 对应的什么？肯定是把 CMD 跟 inwork 做一个关联关系，如果不等于空，直接添加就好了。是不是？如果不等于空，直接就把这句话拿过来？sorry，写错了，应该是放到。因为你最外层 map 都没有，所以这句话先放到这里边，去添加到最上层的 map 里。最上层的 map 就是我们的，他有 work table。把 table 真好。去做 put modular 是为 key 对不对？ value 我们当前 map 好。这样最后 map 肯定是有里边的map，再把它铺得一次。 OK 逻辑应该是非常简单的。


这是第一层，我先从 inworker table 里边去取，看看有没有。如果没有，我把 map new 出来，再把 modeler 跟对应的 map put 进去，再去把里边的c，m， d 跟我的 invoker 做一个put。必须的是这么一个逻辑。这是 add in worker 的方法。 get in worker 的方法就更简单了。是不是？我们暂时先写两个方法哈。 static 既然是 get in worker，返回的肯定是一个 in worker，咱们叫做 get in work。


get in work 需要哪些属性？首先我得知道你具体的 module 是啥？ string 你如果不知道 module 是什么，你还得知道什么 CMD 是什么。好。你得通过这两个值才能唯一的定位。一个具体的一个英文课类对不对？这是我们之前画图的时候老师就已经跟大家说清楚了。


的。我们怎么办？我们首先来还是从 table 里边去点 get 一个 in modular，取到对应的map。取到 map 之后，我们去把它 copy 过来，等于一个map，这个 map 我们去直接取if，如果 map 不等于空的情况下，我们才去做这个事情。就是 map 表 get c m， d 对不对？ c m d 直接就可以返回了。这样直接就返回我们的 invoker 了。 OK 如果连 map 都没有，你就返回空就好了。好， OK 现在这个方法我们打一个注释，这个方法就是爱的 in worker。这个方法就是我们去 get in worker。好了。搞定非常简单的代码，应该是很简单。好了，现在我们已经做完了 inworker 跟 inworker table。


最后我们来看一看。回到我们最开始的 annotation 扫描的这个方法，也就是我们的scanner，叫做 Nike processor bin scanner。 OK 我们来看看怎么去做这个事情，是不是这样。非常非常简单明了。我们已经取到了这两个值，我就只需要去 new 出来就好了。但是 new 之前我可以先判断它是否为空的时候我才去new。不为空我就说命令重复或者已经存在就可以了，对不对？ OK 做一个判断。


我们就是 in worker table 是吧？点 get in worker 通过你给我拿过来的 model 的key，还有 CMD key，我去判断一下是否等于none。如果等于none，然后我去添加 L4 情况下是证明什么？证明我们已经存在了，我就不去添加了。好在这里注释放到这。好，我加一个。我就直接打印一句话 else 情况就是模块儿下载命令，对应的程序缓存已经存在，不能重复添加是不是？你把对应的到底是哪个模块的打印一下哈。


module 是什么？ module 这个名字就是我们的 module value 是吧？再加上再加上 c m d 是不是？是什么？你就是加上 c m d 的Y6。好了，搞定。接下来就是最简单的了，直接调用它的艾特 invoke 方法，把这几个东西都传进去就好了。 invoke 怎么去创建？ invoke 创建我们 invoke 它自己本身好像有一个创建的方法，记得没错的话。 


inworker 点 create inworker，然后把 method 和 target 存进去。 method 是什么？在这里同学们想想， mess 其实就是我们已经遍历这次复用循环的m，是不就是 mess 的target？目标对象是什么？目标对象就是你扫描的具体的哪个 bin 对不对？就是 bin OK 也把它加进去。好，这样就搞定了。同学们，咱们现在最基础的 components 就是我们最基础的scan，扫描这个类就已经搞定了。这个类做的事情就是使用我们的 bin post processor，在 bin 初始化之后，加载所有的bin。 spring 定容器中的bin。哈，找到带有我们的注解和 c m， d 对不对和艾特 c m，d。我这样去说，找到带有的病对象，把他们加入到我们的 inwork table 里，最后创建对应的 in worker，并把它们加入对应的引入和 table 中。 OK 这是整体的。


通过这 4 句话就已经把我们的 spring 相当于 spring boot 跟我们的 net 已经集成好了。我不知道小伙伴们能不能理解这个意思。当我们还是这幅图，当我们模块一次 Nike 一次 request 球，里边肯定会带有模块名称以及具体的方法是什么。这两个东西传过来的时候，我们直接因为 invoker table 它是基于内存的对不对？我们直接从 invoke table 里面取到这两个所对应的唯一的那一个反射的对象，直接调它的反射方法，调一下引入和方法，这样就执行了具体的方法了。这样就已经完美的去做到了。


跟我们的 spboot 做一个整合，做一个集成， OK 这个其实是一个思路。当然还有一些其他的方式。我们在这里选择这种方式，因为老师觉得这种方式比较简单，而且对于小伙伴来讲也比较容易接受的。 OK 当然其实你也可以做一些更复杂的，比如自定义注解，就真正的去自定义注解，自己去扫描，自己去帮我去注入到spring。在这里我没有去这么做，为什么？因为我们其实是已经依赖了 spring 的 at service。假设没有 at service，同学们思考一下，没有 at service，我加上拒绝，我就想让你帮我把它直接注入到 spring 容器，可不可以？其实也可以，你可以参考一下其他的跟 spring 集成的一些框架，比如 double 的 component scan， double 的service，或者是等等，他们是怎么去扫描注解，并把注解所对应的 bin 直接注入到 spring 容器中的？OK，所以大家可以去思考。


还有很多更复杂的方式，也可以是更优雅的方式。但是在我的角度来看来，因为我们既然就是一个service，我就认为它是一个 spring service，它一定被 spring 管理。我就可以找到一个切入点，加上我自己的注解，我把它扫描到，把它存到一个 table 下面。最终在我去 Nike 通信的时候，给我对应的 model 的和 come out，我就可以去做一个，找到具体的哪一个对象，下面的哪个方法去通过反射去执行就好了。这就是一个整体的逻辑。 OK 这节课我们先到这，感谢小伙伴们的收看。

