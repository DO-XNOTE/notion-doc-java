---
title: 1-16 哨兵SpringAOP注解方式应用-1
---

# 1-16 哨兵SpringAOP注解方式应用-1

[image](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/07fd8fde-8b6b-4e79-922e-c45fefcfde77/SCR-20240722-rxnl.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466T7JUVLKJ%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T225837Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIAEtnTi%2F%2F39r3gPzUsQXPmPOCP%2BsCzMmOIYEz%2FTjvGHUAiEA%2FgHDsKIGlveG7UB7M1IouE9VaCZlJLCu2o64nOVPC7gqiAQIxv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDPhR6eJCFyg3OmS0YircAx3UA3P2MlReOJ8bO2BkWj5dr8kFAF7fI6uIilU4rnbENvwz0B3%2FUFmMWB4m4Mza5iR9cst4jiDVzuRlZjQPW3XrETAmc5YcWR3nG5qrKk1cUZsJvgz2s%2FrC3OEnMwMUQ5qc9djzpfOK5QYXuZi%2B13OqEv9KeuNb640P1v4r0jHG%2BUy1CX2Tn25DoREnUUctt9LxHiN1iO4PQNthyKiIxNMjjo4UmnTABDbEKIWj3er9zcmygD4JZV1Jggo9qkVxMXiCEmwSEBjJIRE2bC%2BKH1VwXRz5Uvn7FIoO%2BsG0nZHKe%2BOEqKTULnS626elCzNPqN9T3W7HvGQyMs04csEzjRGuEtgbGuTzNoFQk28yKeQhigk6lWMq8CHCMpY2uBVKQQsK08eLvnPUCdU10yTH2yVdqM0bnuJAiROKUT4fn9wk3NDZqrQZPuh%2FvpmzCqfoOwmkO4UmCoMyyhMXQ9ABgRorJf9x2Y%2BS1sV9%2Fn9eBwV5DNdR94dmWmZSOydmiQa70HQU2EVWDVZoWb7dqU8XNC52OCIhi9tYDEAiOHkhuqEb3QrL%2BX8WrctH2cGfYc6J9ARiIEyMvYrBZpMiIhGmBjDutl9kmpzdVaTtJnt4xXlFTb%2FLKZP0qPKtTE9WMM63%2F9IGOqUBaLimfrBEtHuWDKCBAAx1FUPD2ZajOEzINf4x1BtYowtEshpVSIa9oIxob3oYwz9UCBZ%2FfzmbPYlLhM8%2FqobxALJ9J0wnjge0GoJpfzN3BNVWYO3zwIHN%2BVmW%2FrWjKzeJEbqQy%2F%2FddQcBUzpZH1f4%2Bjept812iyZWr0mhfB4pc8Vx02w2YwFw4CuSEmikUAH8NGFgxpktwEbeFMDHquaPtu94y%2By%2B&X-Amz-Signature=bdbc8b2d6e7f67c94f39af166c7996ecce26e122078d44c66e79bc65ed6b4776&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

这节课我们继续往下学习，来学习一下这个哨兵他的这个跟我们 spring 进行一个整合的这么一个使用。首先我们还是要看一下对应的这个官方的文档。那这个对于跟 spring 进行整合，其实我们的哨兵提供了一个注解，它的名字叫做 sentinel resource 它提供了这个注解它经营资源的一个注解。那其实它本质上提供了一个这个 aspect G 的这个扩展，然后用于实现自定义资源，然后处理一些像 block exception 等等的一些流控的手段。

[https://github.com/alibaba/Sentinel/wiki/注解支持](https://github.com/alibaba/Sentinel/wiki/注解支持)


OK 那其实我们使用这个 sentence 它的这个 annotation aspect G extension 的时候，这是它的全称。也就是说 asse 这个时候你需要引入的一个依赖就是有它这是必须要有的，就是我们的这个 annotation 的 aspect G 这个注解，那前提也是你必须是一个 supreme 的服务才行，因为它底层其实就是说是依赖于这个 spring 的。那么有了这个依赖之后，接下来我们就看一看这个注解。

```java
<dependency>
    <groupId>com.alibaba.csp</groupId>
    <artifactId>sentinel-annotation-aspectj</artifactId>
    <version>x.y.z</version>
</dependency>
```

那这个注解其实里边的内容说得非常多，那在这里老师还是想着跟小伙伴们去一点一点详细的去把整个的这篇文档去看完。为什么呢？因为这个注解其实才是我们真正工作中用得最多的。比如说我们经常来讲，虽然说你的这个 sentence 它的功能非常强大，支持这个代码片段级别的这个注解。但是其实在实际的工作中，我们还是在方法上用注解还是比较多的。你比如说我们的这个 hastix 断路器这种东西，它就是在方法上加注解，然后使用的比较多。当然在有一些特殊的核心链路的场景下，那使用代码片段这肯定是最合适的，但是一些不是那么特别重要的，但是也相对来讲需要保障服务的稳定性，要做一些流控的手段。


那其实可以说 80% 以上我们用注解用的是最多的。所以说这个是我们整个哨兵的一个重点，我们一起来学习一下。那首先老师在这里把这个 dependency 也直接 ctrl C 粘一下，然后把它引到我们的项目里。我们之前那个 hello world 的项目，就是在这里叫 demo test 那我们在 point 文件里第一步要做的事情要把这个依赖也要引进来才可以。在这里面我们对应的这个 xy Z 版本号，我们的 version 是 163 版本，我们把它放在这里。


好了，那接下来我们一起来读一读对应的我们的这个哨兵基于注解怎么去用。首先我们看到这个 sentence 注解它是用于定义资源的，并在这里提供可选的异常处理和 fail back 的配置项。比如说你异常处理我应该怎么去做降级，我应该怎么去做熔断，我应该怎么去做处理。包括 fail back 就是失败。它有两个配置项，一个是异常处理，一个是 fail back 这两个是非常重要的。然后这个 sentence resource 它里边有一些注解的属性，这个是很重要的。首先第一个就是 value 这个属性它表示资源名称。也就是说我们之前所学的那个资源就是那个 resolve name 那个东西 sphu.entry 里边加的那个资源名字就跟我们这个 value 是一致的，就说你必须要填这个不能为空。当然是不是真的不能为空呢？我们一会看源码你就知道了。就是虽然说可以为空，但是为空的话它会调反射，就是你每次请求走反射的话，这是非常非常浪费性能的。所以说建议大家一定不等于空。


然后对应着有一个叫做 entry type 这个东西。什么意思？就是你的到底是 in 类型还是 out 类型，它默认就是为 out 我们经常用的基本上百分大多数都是 outin 是比较少数的表示流入， Alt 表示流出。然后这里边两个比较关键的属性，其他的就是非常重要的属性了。 OK 我们一起来读一读。


有一个叫做 block handler 或者叫做 block handler class 那这个是什么意思呢？ block handler 对应的其实它处理的叫做 block exception 的函数名称，那这是可选项。 block handler 的意思就是访问的范围必须要是 public 然后返回值类型要与原方法的类型相匹配，参数类型也要和原方法的相匹配。但是且最后它加了一个额外的参数类型为 block exception 然后这个 block handler 的函数你的名字包括其他的点都需要与原方法一致。



如果说你想使用这种其他的类的函数可以指定叫做 block handler class 这个是对应的 class 类对象，那这个类对象必须要被这个 static 函数声明就是 static 修饰，不然的话是无法解析的。那这句话其实感觉比较别扭，看着比较多。


好，我们慢慢来。这里有一个叫做 fail backfail back 函数一个是可选项，它是用于抛异常的时候提供一个 fail back 处理错误的这个降级处理。可以这么去理解 file back 函数它可以针对所有类型的异常，除了 exceptions to agnos 就是排除里边哪些异常进行处理？然后这个 fail back 它的函数和签名和位置的要求也是一样的。要与什么返回值类型原函数要一致，然后参数列表也跟原函数的一致，然后可以额外多加一个 throbal 类型的这个参数用于接受异常 fail back 的这个默认的也应该跟方法名称一样的，然后也可以指定一个叫做 fail back class 那这两个其实差不多，就 block handler 跟这个 fail back 也差不多，我这么看。


然后这里边还有一个叫做 default fail back 在一点六点零之后才有的一个默认的 fail back 函数名称，这是一个可选项，通常用于通用的 fail back 逻辑处理，也就是通用的时候我们可以去干什么？我们可以看这个 default fail back 就比如说我一些其他的服务，所有的一些降级的处理都可以用这个方法，这是可以的。然后这种 fail back 函数可以针对所有类型的异常，当然它里边有一个新的属性也是在 160 里边才提供的。就是说我可以排除掉哪些异常类型，就是一个 exception to agonos 然后这里边如果你同时配置了 fail back 跟这个 default fail back 那只有 fail back 会生效。 default fail back 这签名的要求是什么呢？也是很多个一致，然后可以加一个额外的参数等等等等然后它会有一个什么 fail by class 对应的。注意也要是声明为 statue 我们大概浏览一下。


然后它新加了一个叫做什么呢？ 1.6 之后新加了一个特性叫做过滤，就是我们排除不必要的异常 exceptions to agnos 然后用于指定哪些异常被排除掉，不会记录到这个异常统计中，也不会进入这个 feel back 函数，而是原样的进行抛出。然后在这里注意这句话一点，6.0之前版本 fail back 函数只针对于降级异常处理，看见了吧。
在 160 之前，我们的 fail back 函数只是针对于降级的处理的，就是你只有抛出 degree 的 exception 才会被什么才会被这个 fail by 函数去捕获到，然后去灰掉，这是 160 的，然后不能针对于一些业务异常进行处理，这是一点非常关键的一些特性。


为什么？其实 160 版本特意的对这个 degree 的 exception 然后去处理了这个 fallback 的异常。这个如果小伙伴们后面你看它源码你就知道了，在 1600 之前，它特意有个判断。首先它判断的应该是如果异常是 block exception 的话，会进入那个降级的逻辑。然后它又做了一个判断，就是如果这个异常 instance of degree 的 exception 的话，然后它回调 fail back 函数，它多了这么一个处理，这是 1600 之前的版本。然后这里边特别说明，如果 block handler 跟 fail back handler 都配置了，看见了吧，一般它们两个都是做错误降级的手段，都配置了则被限流降级。而抛出 block exception 只会进入什么？ block handler 里处理，如果没有配置这三个，则被限流降级，将会直接抛出这个 block exception 这是新的区别。


好了，那其实我们可以看一个这个小例子，那这个怎么去用呢？首先就是在方法上加的这个注解 sentinel resource value 就是表示资源名称叫 test 然后 block handler 然后这里边有个 block handler class 看见了吧。好，这个 block handler class 它后面有说叫做 exception YouTube classok 这个里边正常的逻辑我会走这个 test 方法。然后我们看一看当发生降级的时候会走哪个方法呢？它会走这个名字的方法就是 handler exception 这里边你是看不到的，因为这是仅仅是一个小的demo ，我所以说你看不到。


好了，那我们再往下看，这是原始函数，这也是另外一个函数，叫做 hello 它的资源一个是 test 一个是 hello 然后这里边也有一个 block handler 还有一个叫做 fail back 然后叫做 hello fail back 那这个 hello fell back 在这里是不是。然后这里边叫做 exception handler 那你看它其实这两种形式的这个异常就是一个是 block handler 跟这个什么 fail back 它们两个感觉会很像。我们来打开代码来看一下。刚才我们已经加进来这个类了，加进来了这个 at annotation aspect G 了，你加进来这个类之后其实你还要做很多事情。


我们后面再说。我们先来看一看它的官方的源码。首先我们来看什么呢？我们来看对应的例子，

[image](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/1ca5cba6-0614-4764-81aa-3047ce3d4b18/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466T7JUVLKJ%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T225836Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIAEtnTi%2F%2F39r3gPzUsQXPmPOCP%2BsCzMmOIYEz%2FTjvGHUAiEA%2FgHDsKIGlveG7UB7M1IouE9VaCZlJLCu2o64nOVPC7gqiAQIxv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDPhR6eJCFyg3OmS0YircAx3UA3P2MlReOJ8bO2BkWj5dr8kFAF7fI6uIilU4rnbENvwz0B3%2FUFmMWB4m4Mza5iR9cst4jiDVzuRlZjQPW3XrETAmc5YcWR3nG5qrKk1cUZsJvgz2s%2FrC3OEnMwMUQ5qc9djzpfOK5QYXuZi%2B13OqEv9KeuNb640P1v4r0jHG%2BUy1CX2Tn25DoREnUUctt9LxHiN1iO4PQNthyKiIxNMjjo4UmnTABDbEKIWj3er9zcmygD4JZV1Jggo9qkVxMXiCEmwSEBjJIRE2bC%2BKH1VwXRz5Uvn7FIoO%2BsG0nZHKe%2BOEqKTULnS626elCzNPqN9T3W7HvGQyMs04csEzjRGuEtgbGuTzNoFQk28yKeQhigk6lWMq8CHCMpY2uBVKQQsK08eLvnPUCdU10yTH2yVdqM0bnuJAiROKUT4fn9wk3NDZqrQZPuh%2FvpmzCqfoOwmkO4UmCoMyyhMXQ9ABgRorJf9x2Y%2BS1sV9%2Fn9eBwV5DNdR94dmWmZSOydmiQa70HQU2EVWDVZoWb7dqU8XNC52OCIhi9tYDEAiOHkhuqEb3QrL%2BX8WrctH2cGfYc6J9ARiIEyMvYrBZpMiIhGmBjDutl9kmpzdVaTtJnt4xXlFTb%2FLKZP0qPKtTE9WMM63%2F9IGOqUBaLimfrBEtHuWDKCBAAx1FUPD2ZajOEzINf4x1BtYowtEshpVSIa9oIxob3oYwz9UCBZ%2FfzmbPYlLhM8%2FqobxALJ9J0wnjge0GoJpfzN3BNVWYO3zwIHN%2BVmW%2FrWjKzeJEbqQy%2F%2FddQcBUzpZH1f4%2Bjept812iyZWr0mhfB4pc8Vx02w2YwFw4CuSEmikUAH8NGFgxpktwEbeFMDHquaPtu94y%2By%2B&X-Amz-Signature=6fe806fd852e7021566eeff30c4e1c99254f3c8e44b49d39bf6e2e3eab395fad&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

哪个例子就是 demo annotation spring lop 看看怎么去用它。首先你看它的 pom 文件里边必然会有一个对应的这个 dependency 依赖 annotation aspect G 有了它之后，这是第一步要做的事情也依赖第二步做什么事情呢？第二步你要做的事情就是它举例说这个就是我一个 supreme boot 工程。但是第二步要做的事情要加一个 configuration 就是有一个叫做 AOP 的 configuration 你看这有个 at configuration 然后要把它自己的一个类叫做什么呢？叫做 sentence resource aspect 这么一个类你要实例画出来，这是必须要实力画出来的。你只有实力画出来，它才能帮你去做切面。因为 lop 它就是一个切面。当你做好切面之后，接下来你就可以去用了，怎么去用呢？我们来看一看。

[image](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/7a15d5cc-93d6-415e-b6f2-c02a6e16ab1c/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466T7JUVLKJ%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T225836Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIAEtnTi%2F%2F39r3gPzUsQXPmPOCP%2BsCzMmOIYEz%2FTjvGHUAiEA%2FgHDsKIGlveG7UB7M1IouE9VaCZlJLCu2o64nOVPC7gqiAQIxv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDPhR6eJCFyg3OmS0YircAx3UA3P2MlReOJ8bO2BkWj5dr8kFAF7fI6uIilU4rnbENvwz0B3%2FUFmMWB4m4Mza5iR9cst4jiDVzuRlZjQPW3XrETAmc5YcWR3nG5qrKk1cUZsJvgz2s%2FrC3OEnMwMUQ5qc9djzpfOK5QYXuZi%2B13OqEv9KeuNb640P1v4r0jHG%2BUy1CX2Tn25DoREnUUctt9LxHiN1iO4PQNthyKiIxNMjjo4UmnTABDbEKIWj3er9zcmygD4JZV1Jggo9qkVxMXiCEmwSEBjJIRE2bC%2BKH1VwXRz5Uvn7FIoO%2BsG0nZHKe%2BOEqKTULnS626elCzNPqN9T3W7HvGQyMs04csEzjRGuEtgbGuTzNoFQk28yKeQhigk6lWMq8CHCMpY2uBVKQQsK08eLvnPUCdU10yTH2yVdqM0bnuJAiROKUT4fn9wk3NDZqrQZPuh%2FvpmzCqfoOwmkO4UmCoMyyhMXQ9ABgRorJf9x2Y%2BS1sV9%2Fn9eBwV5DNdR94dmWmZSOydmiQa70HQU2EVWDVZoWb7dqU8XNC52OCIhi9tYDEAiOHkhuqEb3QrL%2BX8WrctH2cGfYc6J9ARiIEyMvYrBZpMiIhGmBjDutl9kmpzdVaTtJnt4xXlFTb%2FLKZP0qPKtTE9WMM63%2F9IGOqUBaLimfrBEtHuWDKCBAAx1FUPD2ZajOEzINf4x1BtYowtEshpVSIa9oIxob3oYwz9UCBZ%2FfzmbPYlLhM8%2FqobxALJ9J0wnjge0GoJpfzN3BNVWYO3zwIHN%2BVmW%2FrWjKzeJEbqQy%2F%2FddQcBUzpZH1f4%2Bjept812iyZWr0mhfB4pc8Vx02w2YwFw4CuSEmikUAH8NGFgxpktwEbeFMDHquaPtu94y%2By%2B&X-Amz-Signature=d011c09c9ba117f84842676f8a8179f82f03e4bb8dde57efb1a59e00884819f2&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

首先有 controller 这个 demo controller 里边基本上没做什么事情，就是我们正常的一个 supreme C 然后主要的它的逻辑都在什么都在这个 test service 里。这个 test service 里定义了三个接口，一个是 wide test 一个是 string hello 传了一个参数浪类型的 S 还有一个就是 hello another name 那它们具体的实现是什么呢？我们就来看一看具体的实现就看到了。


首先我们把它最大化来看一看，读一读这个类它是被 spring 所管理的这是一个 spring 的这个一个 at service 注解。然后它里边比如说 test 方法，这个不就是我们刚才通过什么通过阅读这段官方的 demo 给我们写的这个demo ，只不过它要比这个官方的 demo 要更清晰一些，落地到代码中了。然后这里边你看这个资源名称叫做 test 然后有一个 block handler 那 block handler 它其实在下面肯定会有，我们来找一下。你看这个 block handler 我发现老师这个 block handler 我没有找到，看见了吧，那从哪里找？很简单，往下找。

[image](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/a442ed49-1788-47a1-8d6d-adbd50606ff0/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466T7JUVLKJ%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T225837Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIAEtnTi%2F%2F39r3gPzUsQXPmPOCP%2BsCzMmOIYEz%2FTjvGHUAiEA%2FgHDsKIGlveG7UB7M1IouE9VaCZlJLCu2o64nOVPC7gqiAQIxv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDPhR6eJCFyg3OmS0YircAx3UA3P2MlReOJ8bO2BkWj5dr8kFAF7fI6uIilU4rnbENvwz0B3%2FUFmMWB4m4Mza5iR9cst4jiDVzuRlZjQPW3XrETAmc5YcWR3nG5qrKk1cUZsJvgz2s%2FrC3OEnMwMUQ5qc9djzpfOK5QYXuZi%2B13OqEv9KeuNb640P1v4r0jHG%2BUy1CX2Tn25DoREnUUctt9LxHiN1iO4PQNthyKiIxNMjjo4UmnTABDbEKIWj3er9zcmygD4JZV1Jggo9qkVxMXiCEmwSEBjJIRE2bC%2BKH1VwXRz5Uvn7FIoO%2BsG0nZHKe%2BOEqKTULnS626elCzNPqN9T3W7HvGQyMs04csEzjRGuEtgbGuTzNoFQk28yKeQhigk6lWMq8CHCMpY2uBVKQQsK08eLvnPUCdU10yTH2yVdqM0bnuJAiROKUT4fn9wk3NDZqrQZPuh%2FvpmzCqfoOwmkO4UmCoMyyhMXQ9ABgRorJf9x2Y%2BS1sV9%2Fn9eBwV5DNdR94dmWmZSOydmiQa70HQU2EVWDVZoWb7dqU8XNC52OCIhi9tYDEAiOHkhuqEb3QrL%2BX8WrctH2cGfYc6J9ARiIEyMvYrBZpMiIhGmBjDutl9kmpzdVaTtJnt4xXlFTb%2FLKZP0qPKtTE9WMM63%2F9IGOqUBaLimfrBEtHuWDKCBAAx1FUPD2ZajOEzINf4x1BtYowtEshpVSIa9oIxob3oYwz9UCBZ%2FfzmbPYlLhM8%2FqobxALJ9J0wnjge0GoJpfzN3BNVWYO3zwIHN%2BVmW%2FrWjKzeJEbqQy%2F%2FddQcBUzpZH1f4%2Bjept812iyZWr0mhfB4pc8Vx02w2YwFw4CuSEmikUAH8NGFgxpktwEbeFMDHquaPtu94y%2By%2B&X-Amz-Signature=07a2a46731e67b156ca50a270a0c5f62719ba3ff4b62111d1beee7a138b84c8c&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

block handle 的 class 在这里，在这里边肯定必然有这个 handler exception 这个方法我们来点进去。这个方法我们看见来，就它这个方法有了，那就是说这是它的一种策略，你可以把这个对应的降级方法放到一个类里，可以去提出来公用。所以说它可以写一个什么，叫做 block handler class 然后这个 block handler class 里边写你自己的方法，这 class 的名词你自己定义，然后这里边它叫什么？它叫做 handler exception 它里边可以额外多传一个参数，就是在 block exception 的时候，我可以拿到它的异常信息，然后做一些相应的处理。但是你要注意这个方法必须要被 static 所修饰，要不然是不好用的。从哪儿能看到呢？就是在这块儿注意对应的函数必须有 static 所修饰，要不然是无法解析的。所以说你在使用这种策略的时候，小伙伴们你要注意你必须要加 static 关键字，不然的话是不识别的。

[image](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/73bc594c-1057-405f-a8a8-09e7e6c60a13/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466T7JUVLKJ%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T225837Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIAEtnTi%2F%2F39r3gPzUsQXPmPOCP%2BsCzMmOIYEz%2FTjvGHUAiEA%2FgHDsKIGlveG7UB7M1IouE9VaCZlJLCu2o64nOVPC7gqiAQIxv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDPhR6eJCFyg3OmS0YircAx3UA3P2MlReOJ8bO2BkWj5dr8kFAF7fI6uIilU4rnbENvwz0B3%2FUFmMWB4m4Mza5iR9cst4jiDVzuRlZjQPW3XrETAmc5YcWR3nG5qrKk1cUZsJvgz2s%2FrC3OEnMwMUQ5qc9djzpfOK5QYXuZi%2B13OqEv9KeuNb640P1v4r0jHG%2BUy1CX2Tn25DoREnUUctt9LxHiN1iO4PQNthyKiIxNMjjo4UmnTABDbEKIWj3er9zcmygD4JZV1Jggo9qkVxMXiCEmwSEBjJIRE2bC%2BKH1VwXRz5Uvn7FIoO%2BsG0nZHKe%2BOEqKTULnS626elCzNPqN9T3W7HvGQyMs04csEzjRGuEtgbGuTzNoFQk28yKeQhigk6lWMq8CHCMpY2uBVKQQsK08eLvnPUCdU10yTH2yVdqM0bnuJAiROKUT4fn9wk3NDZqrQZPuh%2FvpmzCqfoOwmkO4UmCoMyyhMXQ9ABgRorJf9x2Y%2BS1sV9%2Fn9eBwV5DNdR94dmWmZSOydmiQa70HQU2EVWDVZoWb7dqU8XNC52OCIhi9tYDEAiOHkhuqEb3QrL%2BX8WrctH2cGfYc6J9ARiIEyMvYrBZpMiIhGmBjDutl9kmpzdVaTtJnt4xXlFTb%2FLKZP0qPKtTE9WMM63%2F9IGOqUBaLimfrBEtHuWDKCBAAx1FUPD2ZajOEzINf4x1BtYowtEshpVSIa9oIxob3oYwz9UCBZ%2FfzmbPYlLhM8%2FqobxALJ9J0wnjge0GoJpfzN3BNVWYO3zwIHN%2BVmW%2FrWjKzeJEbqQy%2F%2FddQcBUzpZH1f4%2Bjept812iyZWr0mhfB4pc8Vx02w2YwFw4CuSEmikUAH8NGFgxpktwEbeFMDHquaPtu94y%2By%2B&X-Amz-Signature=6d1f211ce9c7efe26c23ee4af4d28da52b6b8d3092e17891c6498fe6b6a9ab80&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)


好了，那这样的话第一种使用注解的方式。小伙伴已经看到了，就是使用 at sentinel resource 配合 block handler 以及我们的这个 block handler class 去定义。有的人说老师，那这个好像跟 hashtags 差不多，对不对？它其实也是相互去借鉴了这个 sentence 它的一个使用。然后按照那个模式，我降级的时候我直接找这个方法，这个方法是在这个类里边直接就降级了。 OK 这是第一种形式，然后我们再看第二种形式。

[image](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/823eca9b-d7e7-4559-8390-4501eab224b3/Home--alibaba-Sentinel-Wiki-%E9%A6%96%E9%A1%B5--%E9%98%BF%E9%87%8C%E5%B7%B4%E5%B7%B4-%E5%93%A8%E5%85%B5%E7%BB%B4%E5%9F%BA.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466T7JUVLKJ%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T225837Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIAEtnTi%2F%2F39r3gPzUsQXPmPOCP%2BsCzMmOIYEz%2FTjvGHUAiEA%2FgHDsKIGlveG7UB7M1IouE9VaCZlJLCu2o64nOVPC7gqiAQIxv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDPhR6eJCFyg3OmS0YircAx3UA3P2MlReOJ8bO2BkWj5dr8kFAF7fI6uIilU4rnbENvwz0B3%2FUFmMWB4m4Mza5iR9cst4jiDVzuRlZjQPW3XrETAmc5YcWR3nG5qrKk1cUZsJvgz2s%2FrC3OEnMwMUQ5qc9djzpfOK5QYXuZi%2B13OqEv9KeuNb640P1v4r0jHG%2BUy1CX2Tn25DoREnUUctt9LxHiN1iO4PQNthyKiIxNMjjo4UmnTABDbEKIWj3er9zcmygD4JZV1Jggo9qkVxMXiCEmwSEBjJIRE2bC%2BKH1VwXRz5Uvn7FIoO%2BsG0nZHKe%2BOEqKTULnS626elCzNPqN9T3W7HvGQyMs04csEzjRGuEtgbGuTzNoFQk28yKeQhigk6lWMq8CHCMpY2uBVKQQsK08eLvnPUCdU10yTH2yVdqM0bnuJAiROKUT4fn9wk3NDZqrQZPuh%2FvpmzCqfoOwmkO4UmCoMyyhMXQ9ABgRorJf9x2Y%2BS1sV9%2Fn9eBwV5DNdR94dmWmZSOydmiQa70HQU2EVWDVZoWb7dqU8XNC52OCIhi9tYDEAiOHkhuqEb3QrL%2BX8WrctH2cGfYc6J9ARiIEyMvYrBZpMiIhGmBjDutl9kmpzdVaTtJnt4xXlFTb%2FLKZP0qPKtTE9WMM63%2F9IGOqUBaLimfrBEtHuWDKCBAAx1FUPD2ZajOEzINf4x1BtYowtEshpVSIa9oIxob3oYwz9UCBZ%2FfzmbPYlLhM8%2FqobxALJ9J0wnjge0GoJpfzN3BNVWYO3zwIHN%2BVmW%2FrWjKzeJEbqQy%2F%2FddQcBUzpZH1f4%2Bjept812iyZWr0mhfB4pc8Vx02w2YwFw4CuSEmikUAH8NGFgxpktwEbeFMDHquaPtu94y%2By%2B&X-Amz-Signature=03631cee7dbfe866c087e75f63050499d6c22fdb01524067e14dbd96530681c0&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)




