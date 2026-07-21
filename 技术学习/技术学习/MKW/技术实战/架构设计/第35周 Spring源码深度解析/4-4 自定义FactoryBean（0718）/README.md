---
title: 4-4 自定义FactoryBean（0718）
---

# 4-4 自定义FactoryBean（0718）

[image](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/35ceaeff-bcec-41d6-b2fa-f29ee83e3fb3/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UQM5UT4R%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T232028Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIETK6lPgr7VqrPXtVFj6gavD9j92lnuDFUgBhFVJRq30AiEAxo4s5Q72QtnGbI4G6a3T6lqOtIObTsg0hdZDInzPfDsqiAQIxv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDFSiBMbluDX%2BoTOB5yrcAyzgafWFeIGNvAv90m%2Foav6VFKqahOi23ylw6HFHD2SxNsGajeM%2FP0sIfDs0ZqJF7SYxYQ1oOYYyt2McMOSFGgJYvRb0a7TGkqIxaYN1IoiT1drzQta%2BOLfjy0cEI69fTLMgL%2F7xbIiv1RV4EcGMwoc0N3VqK%2BrvOOqVzsf1NSN0WC2FdJOzKi2ftVig06lpuXls0a99IaW7NkP6ESXd%2F0a%2FUCF8sjjOiHL1mxqVvBtIWhS8KoBKSoWFs%2F7B1L3qqCqRMlyIIKmwINxok%2FEuLkoT2dO9AeaLaN%2FkG3%2FVq6XITXnsEjPtnnt7wNnhnnJCuZv%2FwE7vkYQGVVeRz6Q55eZfhdA7ROo02UIGxmMMDm7CD%2B7MqTLl15bNCFFO221y1z7cDcMwYYPol1lzfoX0qRHuOvabTzSvW1i%2FwlkpP4Wa5spHnp9NF1ZdsNK2EPoy2Ns1Nw4tDKZpaeNwnFdcNJdj7RPiazlCEGXyHZCgMQ8Lp4JiZitZ6uPGYCd7fV%2BekEMmWJyVvxyuG40LvNNHGcKW9aoXmJjohgTzl0KWHX9hRpwPIaN6ZMHgAXWRiMYEcBOzxslFdAeXeX7psFn9hliGc60pu8vuycJwn9mNvd9vPeChcglE59qKMGupMIS7%2F9IGOqUB9lkkva1dMOdEg2H9LUY50MFxF3THP4zA5aT4BfzL5iMKdOwt7xZaEP6iy2gnU2af%2F0Nd3zOwD7pZczGGuNsvCY02B%2BpK3jJeHsWaym5A9gplVEA7nUKt8SKvl%2BU%2B4iGu%2BoLBtBX4hVX3wsEKUAHk3vS2RBvcF6bBrKL0l14r8fMrU2CpSHDpxB79J3gtuCJ5taXhaR9WywfCrpRgpzFtxfLMjM4p&X-Amz-Signature=6d974118463e306cf92b9ec115fb55bf2307ebc53d4b4bcf3b6fd838e1bbed89&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

[image](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/9d0d1181-6fe0-4855-92cb-501604567c36/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UQM5UT4R%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T232028Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIETK6lPgr7VqrPXtVFj6gavD9j92lnuDFUgBhFVJRq30AiEAxo4s5Q72QtnGbI4G6a3T6lqOtIObTsg0hdZDInzPfDsqiAQIxv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDFSiBMbluDX%2BoTOB5yrcAyzgafWFeIGNvAv90m%2Foav6VFKqahOi23ylw6HFHD2SxNsGajeM%2FP0sIfDs0ZqJF7SYxYQ1oOYYyt2McMOSFGgJYvRb0a7TGkqIxaYN1IoiT1drzQta%2BOLfjy0cEI69fTLMgL%2F7xbIiv1RV4EcGMwoc0N3VqK%2BrvOOqVzsf1NSN0WC2FdJOzKi2ftVig06lpuXls0a99IaW7NkP6ESXd%2F0a%2FUCF8sjjOiHL1mxqVvBtIWhS8KoBKSoWFs%2F7B1L3qqCqRMlyIIKmwINxok%2FEuLkoT2dO9AeaLaN%2FkG3%2FVq6XITXnsEjPtnnt7wNnhnnJCuZv%2FwE7vkYQGVVeRz6Q55eZfhdA7ROo02UIGxmMMDm7CD%2B7MqTLl15bNCFFO221y1z7cDcMwYYPol1lzfoX0qRHuOvabTzSvW1i%2FwlkpP4Wa5spHnp9NF1ZdsNK2EPoy2Ns1Nw4tDKZpaeNwnFdcNJdj7RPiazlCEGXyHZCgMQ8Lp4JiZitZ6uPGYCd7fV%2BekEMmWJyVvxyuG40LvNNHGcKW9aoXmJjohgTzl0KWHX9hRpwPIaN6ZMHgAXWRiMYEcBOzxslFdAeXeX7psFn9hliGc60pu8vuycJwn9mNvd9vPeChcglE59qKMGupMIS7%2F9IGOqUB9lkkva1dMOdEg2H9LUY50MFxF3THP4zA5aT4BfzL5iMKdOwt7xZaEP6iy2gnU2af%2F0Nd3zOwD7pZczGGuNsvCY02B%2BpK3jJeHsWaym5A9gplVEA7nUKt8SKvl%2BU%2B4iGu%2BoLBtBX4hVX3wsEKUAHk3vS2RBvcF6bBrKL0l14r8fMrU2CpSHDpxB79J3gtuCJ5taXhaR9WywfCrpRgpzFtxfLMjM4p&X-Amz-Signature=571299d870037eb86619fb6c662cb2e37309dbcd044e7a3a7d8065cca2e4d794&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

同学们大家好，这一章节我们来介绍一下 spring 的二次改造里面的自定义 factory beans。对于 factory bin 通常的应用场景就是说这个 bin 构造起来特别复杂，我们需要写大段的逻辑，我们通过这个 fact bin 的它的 get bin 的方法去获取对应的内容。那我们现在来构建一下 pact bin 的一个演示实例。


首先在这里面我们创建一个 pectory 这个packets，那么我们现在我们的需求怎样去定义呢？这里面我们看到对于我们的 d o 可以有 d o in， D b 和 d o in memory 同样多种选择的话，这样对于我们 Demo service 的依赖就会产生一定的负担。我们这里面可以约定一下把我们的 Demo service 去构建出一个 factory bin，那么我们看一下这个怎么去写一下。好在这里面我们去创建。


这名，我的命名是 Demo service，我们定为我们的 Demo service packs to be in，在这里面它需要去实现 packed being 接口，这里面 packed being 接口是指定一个泛型，泛型就说明一下它这个派克特病构建的类型是什么。我们这里面制定一下 Demo service 好，这个记录故障完成以后，我们有几个具体的方法是必须要实现的。在这里面有一个对应的 get object 和 get object type，这里面 get object type 就是我们对应的 demo service，我们可以直接在这里面去执行，那这里面我们需要返回一个 object 对象，这个 object 对象是 Demo service 的类型，那么我们可以先把这个作为一个属性声明出来，好我们去让它创建出这个类变量。


那么对于我们在构造这个 fact Bing 的过程中，我们是有一些依赖条件的，比如说我们这个 fact Bing，它也是依赖我们的 Demo do 的，所以说我们可以在这里面声明一个 demo deal 这样一个属性依赖。这个过了完成以后，对于 Demo d o 我们可以通过它的自动注入的方式去完成。但对于这个自动注入的话， MDO 我们假设它是不一定存在在我们的容器 b 里面的，那么我们去跟它构造一个 set 方法，好在这里面我们通过注解的方式把它注入，但是不一定存在，我们把这个 required 改成false，这样的话我们当前 3L 环境如果没有 Demo service 的话，它就不会进行报错。


做完这个事情以后我们需要做的是什么呢？我们需要在整个这个 factory being，它在初始化的时候去构建我们的object，我们一般会在 bin 的初始化完成，那么我们会在这面是选择时间点，就是一个初始化。 inside 拼音，这里面我们有一个对应的是 after pop set 这样一个方法，我们在这里面做一些事情可以这样去判断。


首先我们看一下 demo d o 是否存在，如果 Demo DAU 存在不为 null 的话，我们就可以去通过这种方式去创建我们的 Demo service。好，这里面我们可以改造一下，把这个可以把 Demo deal 作为它的一个参数放进来，我们看这里面去它并没有这个方法，那么我们把这个类去创建一下这样一个构造方法。这样完成以后，我们如果说通过 back ToB 的话，你需要把这个 auto where 注释掉，它就不生效了。同时我们把这个对应的 ad service 这个也注入掉，避免它扫描的时候通过这种方式注入进来。
好，我们在其他情况，如果说当前 demo TO 它为 null 的话，我们会怎么做？我们会这样就通过 Demo Swift 直接去 new 一个 demo deal in memory 的方式，我们这个 Demo service 构建完成，同时如果说我们是通过 Demo service effect being 构造的in，可以在这里面增加一个说明，可以 project 点 set 我们的 model name，来到 model name 里面，我们可以去标志一下当前我们是比如说是 Creator by Pixel b 去做一个说明。


好，这个完成以后我们来去构找我们的单元测试，好，我们去创建单元测试，那么对于这个单元测试，我们也可以去重用一下我们刚才的代码逻辑。这里面我们看一下 customer being propress，我们把这个内容去咖啡过来，在这里面我们加上我们的日志 SL 化解，有一些代码可能是重复性是比较大的，这里面我们把这些不相关的内容清理掉，让它更简洁一些。这里面我们去掉把我们的 fact 的 bin 注入进来，这样我们这个病逐步完成。那么现在我们可以去执行一下yes，看我们执行的效果。这里面需要把我们的 demo service 获取一下，获取完我们的 Demo service，看一下这个 Demo service 它的 model name，来确认一下它是通过什么方式去构建的。


这里面我们打印输出一下，这会儿我们的 model name，它主要就是为了去区分一下我们构建方式。好，这里面我们把这个删掉，现在我们去自行一下，好像我们可以看到得到这个 model name，它就是 create by factor b 这样的话我们对应的这种构造方式它已经生效了。


对于这个 factor b，它的词线非常多，我们可以从这里面看一下。一般跟 spring 集成的这些第三方类的话，它通常都会有 x Bing 的一个实现，可以看到 x 的 bin 相关的内容特别多，这里面有我们自定义的，可以观察一下，有对应的这里面几个。还有印象，这里面是集成的我们的 data source 数据源，它就是一个 factory bin，可以进来看一下。


在这里面它这个 imparted DATABASE factor bin 的这里面实现了 factor bin，同时它返回的内容是 data source，我们这里面可以看到它获取到 object 的方式是 get data source，最终 get data source 的方式去获取我们的处理的类型，同时这里面也是通过 after property set 的方式去初始化我们 date base，那么 factor bin 这个接口的使用 partner 我们就先介绍到这里，同学们下一节再见。


