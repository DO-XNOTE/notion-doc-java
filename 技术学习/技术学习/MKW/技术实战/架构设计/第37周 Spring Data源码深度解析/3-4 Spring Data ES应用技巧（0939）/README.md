---
title: 3-4 Spring Data ES应用技巧（0939）
---

# 3-4 Spring Data ES应用技巧（0939）

[image](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/5a5c19aa-ce93-4242-82cc-7a382c549fd5/SCR-20240814-jfrc.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SRQF6MQJ%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T232144Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIEZsrNUwIUod67LHrYZ%2BDKy398V0RQqPmYA6U2cKBtrOAiAizp6vjrOC22HfXZxo%2FBFUWqwg7BprZm5kNcu3l5IpOiqIBAjG%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMOO8CnT%2B3gzxqL7l8KtwDVabZTONLNbYyv2NWRSdsnaLBx3uZHiOvSWjqqW88bRLtu8pXQq8F1%2BBJrwk34qyArED0rJimW%2Fo4%2FSOk4F6xF4SH0IbIdY01G1X9p%2Fi070SYreuEF2inRqPkJWizgP%2FTnLG1SCCufDPXGJ8KwYgcuui7vRyuEhRk17zcuJzYr%2FCW%2FiI6DyfLS2aEbmEdh6gbHRAbDO30VgCs%2BIAhwyxv%2BcMtzToYeZuGtoBg%2BfF%2BlV9tJjUy5keHZ1I9fmxrdEnW9mY%2BoEs3%2Bt8MEy2VgMZhlBPcKB3BDa1cyiaweAf0NQHb4jHde5EhcAtpSU8atP%2FvID7kiQ1tmMXggdpF6HM7IzbEycLZhad1raRFMiuYRh4OuvFxpfMqvuDfiB4q3mHtQBQmsoblox1xKXUxbaWjOuJlfJ6j6hXnZbbTnT2VptK7T0B4LoNOmVFXSpOq7aarfSY6Yf4B2qUaqVz%2B3vP5Jj50eJutSIolim4Wm3hJ8IVLPNFrPJsoVNUYFkk9IRtLPDqszewLZoIPBDX5ZC4yp88q%2BJPx87WGgAsuw05S%2BtC2TYbpk5c9dNM20%2B1Ci3KJpALm422pOTU2cGYAq5wh0moyQ8cnLiSrVhc9lUgeV4tyEIfeNaebZnfZTNcwybj%2F0gY6pgHmYyDYSeKFUlio7pLLC1cUYf2%2BUIwQugIVX%2FxIlCEbIG3iEB9c283uEycUKN%2FXnqJy6B51UUAK7qllKHCiXdOCk6Wrt6XeJWUxV6j9HZBBKRGsuFpdQPXjfD4iqOCwvcTllEXvGCnj8ZsItIKruGyt5lz6WOOqRPx6Pi5e%2Bc43o%2BMmBeTnllT7CNoVxfc%2Bi%2FlQQSJXgdOJ5mq3thTJSmmnwZe52B8L&X-Amz-Signature=13275c6b5c2aa9315e98e2ffcde0717123efbee28a0835536f381f1a66b8e65a&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

[image](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/3b138343-6a5e-4468-bd9f-a672f0a44f5b/SCR-20240814-jead.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SRQF6MQJ%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T232144Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIEZsrNUwIUod67LHrYZ%2BDKy398V0RQqPmYA6U2cKBtrOAiAizp6vjrOC22HfXZxo%2FBFUWqwg7BprZm5kNcu3l5IpOiqIBAjG%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMOO8CnT%2B3gzxqL7l8KtwDVabZTONLNbYyv2NWRSdsnaLBx3uZHiOvSWjqqW88bRLtu8pXQq8F1%2BBJrwk34qyArED0rJimW%2Fo4%2FSOk4F6xF4SH0IbIdY01G1X9p%2Fi070SYreuEF2inRqPkJWizgP%2FTnLG1SCCufDPXGJ8KwYgcuui7vRyuEhRk17zcuJzYr%2FCW%2FiI6DyfLS2aEbmEdh6gbHRAbDO30VgCs%2BIAhwyxv%2BcMtzToYeZuGtoBg%2BfF%2BlV9tJjUy5keHZ1I9fmxrdEnW9mY%2BoEs3%2Bt8MEy2VgMZhlBPcKB3BDa1cyiaweAf0NQHb4jHde5EhcAtpSU8atP%2FvID7kiQ1tmMXggdpF6HM7IzbEycLZhad1raRFMiuYRh4OuvFxpfMqvuDfiB4q3mHtQBQmsoblox1xKXUxbaWjOuJlfJ6j6hXnZbbTnT2VptK7T0B4LoNOmVFXSpOq7aarfSY6Yf4B2qUaqVz%2B3vP5Jj50eJutSIolim4Wm3hJ8IVLPNFrPJsoVNUYFkk9IRtLPDqszewLZoIPBDX5ZC4yp88q%2BJPx87WGgAsuw05S%2BtC2TYbpk5c9dNM20%2B1Ci3KJpALm422pOTU2cGYAq5wh0moyQ8cnLiSrVhc9lUgeV4tyEIfeNaebZnfZTNcwybj%2F0gY6pgHmYyDYSeKFUlio7pLLC1cUYf2%2BUIwQugIVX%2FxIlCEbIG3iEB9c283uEycUKN%2FXnqJy6B51UUAK7qllKHCiXdOCk6Wrt6XeJWUxV6j9HZBBKRGsuFpdQPXjfD4iqOCwvcTllEXvGCnj8ZsItIKruGyt5lz6WOOqRPx6Pi5e%2Bc43o%2BMmBeTnllT7CNoVxfc%2Bi%2FlQQSJXgdOJ5mq3thTJSmmnwZe52B8L&X-Amz-Signature=ab1a85b4a2a225a28fdd62ea20472c24de896e0f65a538a917dc324877ed7f77&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

学友们大家好，今天我们来介绍 spring date e s 应用技巧解析。那么首先我们来去认识一下 e s rest template，那么我们认识完对应的 rest template，我们来去了解一下依赖色子它的一些客户端，这里面分别是 rest high left client 和 rest client。同时这里面还跟大家提醒一下，现在我们已经不推荐使用 ES template 和 transport client，为什么呢？这是因为在依然是最新的版本，它不再支持这个 transport client 的调用，也就是不太推荐，更推荐大家使用 rest high left client 和 rest client 进行跟 ES 相关的一些操作。


那么对于 elexorts template 和 elancer 词 red template，它们的关系是什么呢？我们可以理解它们是有具有共同的一个父类，也就是 abstract 依赖色子对应的template，那么在这里面，我们对于 rest template，它对应的是 rest high level 的 client 和 rest client，那么对于依赖测词template，它是对应的是 transact client，因为是 transport client，它已经不推荐使用了，所以说这里面对应的依赖色子的 template 也不再推荐使用。所以说优先大家使用对应的依赖色子 rest template 去进行我们 ES 相关的一些操作。


那么我们来去看一下对于依赖色子 rest template 和依赖色子template，它们之间的一个对应关系。在这里面我们首先看到对应的 rest template，它里面会涉及到，首先我们这里面更重点关注的是 rest high life 的client，那么我们通过 rest high level client 可以获取到 rest client，同时对于 rest template 里面还涉及到我们这个 exsearch 的 exception translator，也就是对于我们异常的一些转换。因为我们在了解到对于 spring did，对于这些各个数据库操作的一些封装，我们知道它通常会把底层的这些 exception 转换成我们对应的 data access exception，那么同时像 rest template 它也依赖到了一些present，那么这里面的 operation 也是我们 spring did 对 ES 的一个抽象碰撞。


这里面我们简单列举，比如像 index 和present，主要是对我们应该设置这些映射的 index 进行一些管理，那么这里面还有 document operation，也就是对我们对应的 document 这些对象进行管理。这里面涉及到一些 search operation 和我们的collection，也就是我们的 ES 集群相关的一些操作。
注意，下面我们看这里面是依赖色子operation，同时我们应该知道一蓝色子operation，它可以理解为这是我们一个前面这几个 operation 的一个组合。其实我们重点去了解上面这些组合，对于一单四次operation，其实它这个接口其实依赖测试 rest made，本身它就实现了依赖测试reset，依赖测试 operation 这个接口。


下面我们来看到像 electrace template 相比我们在对应的是 JDBC template，我们去想的话好像依赖 4 的，他们的这个命名是更加合理的，但是因为它是早期定义，它是基于 transport client 定义出来的，所以说我们感觉它命名是更加合理。但其实因为 transport client 它已经不再作为推荐的一个客户端，所以说那么通过 transport client 构建的 ES template 现在也处于一个 play 推荐的一个状态，所以说我们现在使用的过程还是优先使用依赖色次 rest resize template 和我们这个 reset high level client， rest high level client 它是依然色子 client 官方提供的一个client，那么我们现在切到源码里面去简单了解一下，在这里面我们切到了对应的 elecserts rest template，那么这里面我们去看一下它的一个树结构的情况，对于这里面我们看到它是继承了 abstract electri 词template。


对于我们看一下 abstract 依赖词template，它其实是实现了依赖词的 operation 这样一个接口，那么同时也实现了对应的像 vacation contact VR，给我们设置一下我们的 spring 容器的上下文信息，那么对于它的子类，我们可以看到这里面涉及到 elects template 这个 index temperate，我们可以它已经被标记为我们的是不推荐使用了，不推荐使用的原因也是因为我们在构建一代测试 template 的过程，我们使用到了client，那么我们可以看一下这个client。


我们可以看到对应 client 的一个实现是 transport client，我们点进去看一下，对于 transport client，我们可以看到这里面它已经不推荐使用了，它其实推荐我们使用 high love 的 reset kind，并且这个我们这个 transport kind 它应该会在 ES 的 8. 0 的话就会 remove 掉，所以说它里面的这些 API 接口我们就不再去关注了，我们要关注的就是我们在使用的过程中不再使用 transport client。


那么对于一些历史维护的项目应该大多还是使用的是 transport client，这个可能是需要我们在系统维护的过程中去迭代层级替换红对应的 rest 有 high live 的kind，那么好我们切换到，嗯，我们这里面的是依赖色子 reset template，我们可以看到对于我们构建依赖色的 rest template 的过程中，我们用的是 rest high level client，那么我们应该看到对应这个 rest high level calendar，它其实是对应的 exercise 对应的 calendar 的一个炸包里面。


所以说这里面的内容其实就是跟我们依赖塞子原生内容是紧密相关的，这里面它依赖了各种对应的kind，这里面我们看 index client、 class client 和相当于是 task 等等这些client，其实这些 client 对于使用，对于依赖 search 进行深入研究的过程中，我们发现一部分操作都会逐渐地去深入使用到，那么我们还是回到 ES rest template 它这一层级去关注的内容。


在这一层级我们知道在构造这个 elecors rest template 的方构造方法的过程中，我们必须要传入 rest high level kind，也就是必须跟我们一台 search 的 kind 链接构建出关系。其实本身这个一台测试 rest template，它也就是对我们 rest high level kind 进行一个包装，同时在处理的过程，这里面我们看到是依赖色子 exception translator，也就是他的工作主要就是把我们跟疑难四字相关的一些异常进行一个转换，我们可以在这里面看到它转换的处理的内容是什么，我们可以看一下这里面的操作，我们把我们的代码区域放大扩大一些，我们可以看到在这里面注的是什么处理。


我们可以看到它这个方法就是 translate exception，也就是把我们这个异常进行一个转换，它转换的过程中在什么情况下会调用我们 exception translate 进行转换？这里面我们可以看到，首先会看判断当前这个 exception 它是一个运行式异常还是非运行式异常，如果是运行的异常，它就会直接传过来进行转换。如果是非运行字异常，它首先会通过一个 runtime exception 进行包装，通过 runtime exception 进行包装以后，这里面我们看到是 exception translator 的一个转换，我们可以跟进去看它的转换的操作流程，是这样的，这里面我们可以看到它还是对应的一类测试 core 下面的我们一个转换器，首先这个 runtime excellent 过来以后，他首先去判断一下一些是否有一些序列化的冲突，那么如果有序列化冲突的话，它会直接是 count index document 丢丢抛出一个这样一个异常。


那么如果说它是我们正常的 excepts 相关的一个exception，在这里面会进行一些判断，最终会转换成我们可以看到它最终输出的实际上是一个 did access accepts，因为我们知道在 spring date 相关内容，它构建这个 date accept，其实它构建的这个数据结构也非常复杂，我们可以看到它下面的子类会非常多，它其实把各种数据库超出的这些情况都构建出了一个对应的exception。所以说我们在这里面转化的过程中，也会根据当前 ES 的操作，不同的情况会进行一些操作。


n 其实这里面我们最容易去理解的，如果说当前这个 index 不可用的话，我们可以去忽略，去抛出这样一个意向，是 no SaaS index excitement，也就是说它并不存在这样一些index，也就是并不出现这个树因跟我们在查询的过程中我们就是 not 放它，也就是说我们没找到这样一个对象，类似一个这样一个excess。


其实下面还要会涉及到一些数据校验相关的异常，它统称会转换成像我们这里面的是数据相关校验的异常，我们可以看到这个异常，它最终它其实是我们是 did access example，我们看跟下面到这里面它是一个 did accept 相关的一个子类，那么这里面我们简单了解了一下我们这个异常转化的一些功能，我们还回到一天测试 reset template，那么我们了解完这些内容以后，我们去简单去看一下这里面的 attack search reset template 它提供了哪些？超看到一个 count 方法，这 count 方法其实也就是根据我们 ES 构建的 query 和我们指定的类型，去查询一下我们当前这个查询推扫描的一些记录数，也就是指定一个索引在依赖测试的索引库里面能查到的记录数。同时我们可以从这里去看一下我们整个一个概况，可以看到这里面是一个bug，一些批量的一些 index 操作，这是 bug operation，就是我们 GMV 和 do bug operation 相关的一些操作的信息，做一些批量的操作，这里面我们看有相关的 delete 操作，也会有我们相关的一些 save 相关的一些操作，这里面是 save 相关的操作，这是我们 search 查询的。


这里面还有 search for stream，你查询出一个对应的 stream 流相关的操作，其实我们可以看到对应的跟一带 4 的相关的操作，我们基本上都可以在依赖色的 rest template 里面找到一个对应的一个关系，那么关于这个 string d 的依赖色词它的应用技巧解析，我们就先简单的介绍到这里，对于依赖色词更多的一些操作的话，大家可以对于 rest high level planned 更多的细致进行一些了解。


