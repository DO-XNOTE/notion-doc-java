---
title: 5-3 手写IOC容器-3（1509）
---

# 5-3 手写IOC容器-3（1509）

[image](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/b578e605-8b59-4845-b730-9bb365a7403a/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YNPDM6WY%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T232031Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDoYh%2Flg6E4XajN1b13EfXcMxWNbqQXe9i%2BvH71GePW6AIgKHvgePrPk5Aw5a6CMlDJEQRioJscjWgxFa%2B7uId7%2BU8qiAQIxv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDNpltXqIqYlDj4eVJyrcA9GIZ4HwCk7bdm4wKlEbnXM33ZyIMwRuxGeOjXeQh%2FSLGzDlqRjxcCXZ04VHTs07OPE%2B3GOfD%2FsLXd7L%2BZ7t7YNjXX2zt%2FY9attFsxA5zBFT6rmUpukRb1Y1vGJNzHDskygdwu56iQdyPjsq%2BkcIbtX4HdF2cEcOjpEp6U6HCShd98nnUnw4OASFQwzDv%2BZT%2BxrGidzNpoHXlRTk078f%2Bm7kQRJhOSTHG6AgNO2VdlZqbu9BXTiEPXBoEOAUIjiuFsGFoPyviyJEjR7LcdinqXuaBrbT6P%2FV1L6nkJVubOm2Yp%2BbGscoz4IlSJBhJ9qr67SEsT9LvNwWUAUw7qkcspiiciV1o6FdODBVWFDQ%2F%2FzKdTEP3K5Cz2tyffSjvmdmYF2HOCuFsn8CdO7Z0nAPoh6vhMfprwgxa5J5k1RQnd2Hb0xfcisRPKnbJsYwTea%2BWWSezjteJAiOlLXk68srybtQZCOpB9POQU0wKFgWcE7pby1L8DmZHSe9OotUjO4igWQlFaiuY%2FwoZs%2BrDzW5MiNO9tlGSp0CcRX7QRYh6jsk53yu5Nx9MwW4D5%2BETcnDYZ%2BEtIIj%2BgUmV3n88PbWhyO5pFTVcTDVpV6rLa%2Bjh8kca8T4Ozyipu43QzaCMM%2B3%2F9IGOqUBIVbhMKHLyVhO8tytTLdKQ4RoO0LAF4vgx3C2RGmePB5g0AZIw3bw7Dy0VgxoP%2FMB7C2G%2FENcPKua%2BUnq7MOWvUnz8Dx90njBL2HEmuiOygaZh8AgIfWFax8rBi18SemulmJ46ZR1u4Shm8IgCOGfrlkFOIWD0hq8D8du8RVxkmnaA17AlLmGrGseohggyOXd1QXEZ2rm9oCwEeYOy8mgozH0%2BRpM&X-Amz-Signature=0649f6c3dc9b4bd6ae7d1ced56b5655b2f4818603f6502a4296ea981858d011d&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

接下来我们创建我们的 be infactory 的实现，我们知道在 string 容器里面它都用了接口，我们这里面为了简便，我们直接用类来去实现。对于一个 bin factory，我们知道它的这些 bin 都会存在对应的一个 concurrent 哈希 map 里面，我们可以首先声明一下我们这个 contain 的哈希map，好，这个 high map 定义好了以后，我们这个 Bing factor 它需要实现对于这个 map 里面相关的增删改查的操作。


首先比如说我们会需要从里面去获取bin，我们可以 get 变，实现这样一个方法。那么对于 get 宾语，我们需要对应的参数，这个参数它可以是 be name，同时它也可以是指定一个类型，我们这里面可以是，同时我们可以指定返回的内容慢性，那么我们当然也会可以对这个容器里面的变进行删除，就是一个删除操作，remoble， remove 的过程，我们一般指定一下 bin 的名称，还有我们需要可以对我们病进行一个注册，就是我们增加比。


在注册的过程中我们需要怎么样一个参数？注册过程中我们会指定一个 b name 和我们的 b 的一个实现，这是一种方式，这就相当于是我们通过 k 和 value 把它放到对应这个 being 对象里面。好，我们待会去统一去实现。那么还有哪些操作我们还会有一些，我们会看一下当前这个 b 是否存在，也就是跟我们 map 对应的关系，那么我们看一下还有当前 bin 是否存在，这里面，它对应也式参数是 be name。好，我们待会去具体思想。


我们知道我们在 spring 容器里面，它注册的内容通常是一个 being definition，那么因为我们这里面并没有 being dependation，所以我们可以支持一个注册 class 的方法，我们这里面可以去添加对，我们的，也就是说它可以把一个 class 注册进去作为我们的bin。OK，那么接下来我们开始继续实现。


那么对于我们注册的class，我们回忆一下我们的鼻音容器，它里面处理的过程是首先把对应的鼻音 defending 注入进去，作为一个集合，一个 map 里面存起来，那么只有在 get being 的时候才会把我们 being declint 实例化我们的容器，那么这里面同时我们也在这里面去添加一下我们的对应的一个 being definition 的操作，那么这里面我们是对应的是class，那么我们来这里面 class 它的 key 也就是我们的24。


好，这样我们看，如果说我们在这里面这种情况下去执行我们的 reject class，它的操作就比较简单了，需要操作的内容就是我们在这里面去把对应的我们这个 class 放进去就可以了，那么我们就放进去我们可以看到 this 点儿，但我们想一下我们这里面的k，我们需要构造一下我们的 class 刚才对应的class，那么我们的 k 从哪里面获取？我们可以在这里面声明一个变量这个k，我们就可以通过这里面去写个方法，这个方法我们可以定义为 get b name，或者说是我们可以理解为是一个 type ToB name，就是我们把一个 class 的内容，参数是class，那么我们实现这个方法，这个方法对应我们容器里面的内容，就是我们通过一个 class 生成我们 BN 名称的方法。那么通常我们会把我们的类名获取出来，获取到一个破风命名的操作，那么我们在这里面也是简单起见，我们可以直接把我们的 class 对应的 symbol name 获取出来。好，这样也就完成了我们对于 retest class 的一个注册的过程。


接下来我们来看一下对于我们的其他的这些方法，我们怎么去实现？我们在 get being 的过程中，我们应该要做哪些事情？首先获取 get being 它需要进行一个初始化的过程，也就是说我们先判断一下当前容器里面有没有这个bin，如果 bin 已经初始化完成，那么我们去直接执行。如果说这个 bin 它没有初始化，那么我们应该从对应的 bin depending 里面去实例化这个bin，也就是我们从对应的 cos map 里面去找这个内容，那么现在我们开始去执行。


好，我们首先我们去通过我们的 Bing 里面去获得一下有没有当前的 Bing name 对应的内容，如果并存在不等于 now 的话，我们就可以直接把它给返回。我们初始化的时候，第一次它应该是获取不到，其他情况我们应该怎么做？我们需要去看一下当前的 cos map 里面，去获取一下对应的cast。


那么获取到 class 我们要做什么事儿？我们先判断一下 class 不会闹，因为我们有可能是获取不到内容，应该对我们的 class 进行一个私立化的操作，那么我们这里面去实现一个方法，把我们的 class 作为参数传入进去，这里面我们生成一个对应的，我们应该是 object 的类型。


好，我们实现这个 new instance 方法，这里面实现的操作应该是比较简单的，我们直接通过反射的方式把这个对象创建出来就可以，我们这里面应该是实现的相对比较简单一些，我们并没有考虑你那些有参数的构造方法的情况，我们在这里面去处理一下。像这里面如果说我们把对应的地方把异常去包装一下，直接把它给继续抛出，那我们对这些类异常我们统一抛为对应的我们的错误的状态，那么这个异常对长，我们就在这里面不用打印了，它在最外层抛出的时候不用打印。好，现在我们构建出我们的对象，那么在这里面构建出对象以后，我们知道我们对象构建完成以后，如果它不为 now 它应该要做的事情是什么，那应该把我们这个对象放到我们的 bin 里面，同时把。这里面是 project 不是 b 替换一下获取到。如果说在这里面没有获取到的话，我们就返回一个 null 对象，那么这里面我们需要看一下，我们在这里面只是通过 class map 里面得到这个类，并且对这个类进行了一个实例化。那么其实这里面还有一件事情需要做的就是什么呢？它需要对我们做一些依赖注入，如果说我们对于依赖注入的内容，我们需要把我们相关的信息注入进去，那么注入进去我们需要对于这个 object 进行一个处理，那么我们来实现一下这个依赖注入的方法，对于这个方法来说是相对比较复杂一点，不过也不是太复杂，我们可以在这里面去快速去写一下。


首先我们需要去获取一下当前这个对象的类，获取完成以后，我们去获取一下它里面所有的属性，那么我们要对属性去做一个什么呢？做一个查找，我们先判断一下属性不为空，进行循环迭代，那么我们需要做的事情就是我们判断一下这个属性它有没有被 resource 这个注解进行修辞，那么如果被它修饰的话，我们需要获取到这个 field 的类型，这样我们需要从容器里面获取对应的 bin 进行注入。


那么我们得到这个文件类型以后，我们去通过类型去获取我们对应的bin，那么会遇到这个Bing，如果 Bing 不为空，我们把 Bing 进行一个注入，我们先把这个属性变成可访问的，我们进行set，当前的对象就是我们这个 object 的对象，我们的属性也就是新的bin。对于这个我们需要进行处理一下， catch 一下，我们同时把这些内容也，那么这里面我们也是相同的，把一层抛出。好，这样的话我们这个对于属性猪的功能也就完成了。那么在这里面如果说 bin 为 null 的情况下，我们应该要做什么处理呢？如果 Bing 为 now 的话，我们应该也要抛出一张，告诉它我需要的这个 Bing 是不存在的。


OK，那我们看一下，在这里面我们对 get Bing 通过类型获取的方法，我们现在还没有实现，那么对于我们去获取 bin 的话，我们通常会把它类型转成 bin name 去获取，那么我们 be name，我们这里面是转的方式，我们通过统一的 type to be name 保持我们的一致性，那么这里面我们就会得到对应的being。如果 bin 不为null，那么我们就可以把这个对象抛出去，进行一个转换。


好，那么这种情况下，其实它还有一种情况是它没找到这个对象，那么待会儿我们来解释另一种情况，也就是说如果说我们 bin 对应的名称，我们通过它的负例来去获取，那么我们怎么去获取到呢？比如说我们举个例子，在我们的 Demo service 里面，我们对应我们的依赖注入是用 Demo d o，那么我们的实现是 Demo deal in memory，那么我们用这种方式去转化的话，它应该是获取不到我们对应的内容的，所以这种情况下我们还需要去做一些特殊处理。


这个处理的逻辑就是说我们需要遍历一下我们所有 classmap 里面这些类，它的接口是不是也能匹配上？如果能匹配上把它对应的接口去返回出去，那么好，我们这里面去做一个操作，我们通过 cos map 里面我们获取它所有的values，那么我们进行一个迭代，迭代的内容就是我们先把这个对应内容里面我们获取它所有的接口，我们再进行一程式解带。如果我们当前指定的这个类型，我们是跟我们当前的接口能匹配上，我们去查找当前这个b，这里面意思可以解释一下，如果说我们在获取所有的这些类里面过程，发现我们指定的这个class，它是我们某个类里面的一个接口，那我们就把当前这个类的实现去返回出来，注意它 bin 的一个实现。那么这样的话我们几个关键的方法就已经实现完成，我们看一下还有哪个没有关系，像这里面是用 remove bin 和其他方子 adjust bin 的，其实我们暂时还用不到，那么我们待会在使用到的时候我们再去实现它。

