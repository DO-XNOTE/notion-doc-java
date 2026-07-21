---
title: 2-5 架构设计-智能装配AutoConfiguration（2320）
---

# 2-5 架构设计-智能装配AutoConfiguration（2320）

[image](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/ae7017f1-ed2f-47d1-8e8c-fece8dc64559/SCR-20240803-jbep.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SU54GG4R%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T231953Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIAZK10ni6pJlNGQy5V%2FsEISi%2Bur4tz4mCCeRUtYdKlmsAiBB9iaxtszFQICoq4lcfhVhjAjo3AfYEMHOkt%2FxhpMtHCqIBAjG%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMaieZ%2FEXIwajEnExIKtwDP2eK8ax7kODgQLC2L1XxFg0Vd32MXDDDwzIeYfBnHyHwEG0%2FX9NesPZsZAmLu6HWf3vgAsyb9jb28HS24I5nB%2FXtpxqnbXXd%2B5HFTp1Ch%2B5l7YIJJLyLgYKrvbcsp0zN2i1CC1pPH6qBzumePFLJGkcQH5U7BXPVv%2BSJvC25IJUHTGW3ELIlHM3h3raLyxILfGjXFt0prN5CrZZk7n8M1jjTsA%2BBtpIjDOkhQ5KEh5cdjkBdtFiVDEoIGXnf3fgIjDxLW70%2BRd9UcFT5gjcJX5z%2F1U0O5EQwlHY3n8qUF0FbSwapxa%2BG0VTqnM3BHza5yKZ0AcAqeS1VRO0aGQ3%2F4DKiMVjj6ipaBgEaPQ186OH7nmYviyVogeTWb8acgrnlfORUeRBTLV6clBtyOZQMVqxWYyDl2lsyfrhjHZE3PQGApG2WUwt2AaR85z6JMnadoJXTAOtIjRId4OtYQ7q%2FRsHl8VZpa922mxYE5FdA1OVZAKzd3HOGHD6NxoIPFZhftmB3IQEd5%2FqbkNzGZ1psYreePrtd2pXOr5i%2Fj2qoET9suFs3y%2BEgqXgQv6mT3TGUr4He%2BFotk%2BV%2BLkonNap6XgyY9oUNuImw9qOcs20u4BY54Xo6sS7XO16llVgwgbf%2F0gY6pgFYatv3q%2FZgcZvBSlF7BMbX05sx5OgDkVbm5gK8ZCM%2FTSbJuS88OuoQ5joR%2Fw8STwQju5RrAdKNF6NOOnIHYWAXFPOzWJS2bNzDYGXHjmmWSArHLEuuInQFvcjeLavpVpiqmWa7%2FuHWtpBzFDNoBmzFQjie8P4AXZCwIlkXmqkc32gd3pgWhVcy4G6iUf6iBxyiuvnDe1LNiFKnmqhImf8dESR1yc3G&X-Amz-Signature=6448be9ddf06551d4466685398da07704c3da5b922762eda29d9ff52fc1fdcee&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

[image](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/89a9576a-5609-4795-933d-c95895261c74/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SU54GG4R%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T231953Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIAZK10ni6pJlNGQy5V%2FsEISi%2Bur4tz4mCCeRUtYdKlmsAiBB9iaxtszFQICoq4lcfhVhjAjo3AfYEMHOkt%2FxhpMtHCqIBAjG%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMaieZ%2FEXIwajEnExIKtwDP2eK8ax7kODgQLC2L1XxFg0Vd32MXDDDwzIeYfBnHyHwEG0%2FX9NesPZsZAmLu6HWf3vgAsyb9jb28HS24I5nB%2FXtpxqnbXXd%2B5HFTp1Ch%2B5l7YIJJLyLgYKrvbcsp0zN2i1CC1pPH6qBzumePFLJGkcQH5U7BXPVv%2BSJvC25IJUHTGW3ELIlHM3h3raLyxILfGjXFt0prN5CrZZk7n8M1jjTsA%2BBtpIjDOkhQ5KEh5cdjkBdtFiVDEoIGXnf3fgIjDxLW70%2BRd9UcFT5gjcJX5z%2F1U0O5EQwlHY3n8qUF0FbSwapxa%2BG0VTqnM3BHza5yKZ0AcAqeS1VRO0aGQ3%2F4DKiMVjj6ipaBgEaPQ186OH7nmYviyVogeTWb8acgrnlfORUeRBTLV6clBtyOZQMVqxWYyDl2lsyfrhjHZE3PQGApG2WUwt2AaR85z6JMnadoJXTAOtIjRId4OtYQ7q%2FRsHl8VZpa922mxYE5FdA1OVZAKzd3HOGHD6NxoIPFZhftmB3IQEd5%2FqbkNzGZ1psYreePrtd2pXOr5i%2Fj2qoET9suFs3y%2BEgqXgQv6mT3TGUr4He%2BFotk%2BV%2BLkonNap6XgyY9oUNuImw9qOcs20u4BY54Xo6sS7XO16llVgwgbf%2F0gY6pgFYatv3q%2FZgcZvBSlF7BMbX05sx5OgDkVbm5gK8ZCM%2FTSbJuS88OuoQ5joR%2Fw8STwQju5RrAdKNF6NOOnIHYWAXFPOzWJS2bNzDYGXHjmmWSArHLEuuInQFvcjeLavpVpiqmWa7%2FuHWtpBzFDNoBmzFQjie8P4AXZCwIlkXmqkc32gd3pgWhVcy4G6iUf6iBxyiuvnDe1LNiFKnmqhImf8dESR1yc3G&X-Amz-Signature=0994f7adf1fbbdf0e5c884fb02d6e89d114f53aa6c62a166f658dce620c494b2&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

[image](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/fc217138-2737-4ac2-b2c3-aa4ffc872166/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SU54GG4R%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T231953Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIAZK10ni6pJlNGQy5V%2FsEISi%2Bur4tz4mCCeRUtYdKlmsAiBB9iaxtszFQICoq4lcfhVhjAjo3AfYEMHOkt%2FxhpMtHCqIBAjG%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMaieZ%2FEXIwajEnExIKtwDP2eK8ax7kODgQLC2L1XxFg0Vd32MXDDDwzIeYfBnHyHwEG0%2FX9NesPZsZAmLu6HWf3vgAsyb9jb28HS24I5nB%2FXtpxqnbXXd%2B5HFTp1Ch%2B5l7YIJJLyLgYKrvbcsp0zN2i1CC1pPH6qBzumePFLJGkcQH5U7BXPVv%2BSJvC25IJUHTGW3ELIlHM3h3raLyxILfGjXFt0prN5CrZZk7n8M1jjTsA%2BBtpIjDOkhQ5KEh5cdjkBdtFiVDEoIGXnf3fgIjDxLW70%2BRd9UcFT5gjcJX5z%2F1U0O5EQwlHY3n8qUF0FbSwapxa%2BG0VTqnM3BHza5yKZ0AcAqeS1VRO0aGQ3%2F4DKiMVjj6ipaBgEaPQ186OH7nmYviyVogeTWb8acgrnlfORUeRBTLV6clBtyOZQMVqxWYyDl2lsyfrhjHZE3PQGApG2WUwt2AaR85z6JMnadoJXTAOtIjRId4OtYQ7q%2FRsHl8VZpa922mxYE5FdA1OVZAKzd3HOGHD6NxoIPFZhftmB3IQEd5%2FqbkNzGZ1psYreePrtd2pXOr5i%2Fj2qoET9suFs3y%2BEgqXgQv6mT3TGUr4He%2BFotk%2BV%2BLkonNap6XgyY9oUNuImw9qOcs20u4BY54Xo6sS7XO16llVgwgbf%2F0gY6pgFYatv3q%2FZgcZvBSlF7BMbX05sx5OgDkVbm5gK8ZCM%2FTSbJuS88OuoQ5joR%2Fw8STwQju5RrAdKNF6NOOnIHYWAXFPOzWJS2bNzDYGXHjmmWSArHLEuuInQFvcjeLavpVpiqmWa7%2FuHWtpBzFDNoBmzFQjie8P4AXZCwIlkXmqkc32gd3pgWhVcy4G6iUf6iBxyiuvnDe1LNiFKnmqhImf8dESR1yc3G&X-Amz-Signature=6e178c5281c4eb58a8c3f29d86c07e31e611f2c992223c9f131da6066be641d1&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

[image](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/8590abe5-609a-48f9-a9d6-c59760bbd242/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SU54GG4R%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T231953Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIAZK10ni6pJlNGQy5V%2FsEISi%2Bur4tz4mCCeRUtYdKlmsAiBB9iaxtszFQICoq4lcfhVhjAjo3AfYEMHOkt%2FxhpMtHCqIBAjG%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMaieZ%2FEXIwajEnExIKtwDP2eK8ax7kODgQLC2L1XxFg0Vd32MXDDDwzIeYfBnHyHwEG0%2FX9NesPZsZAmLu6HWf3vgAsyb9jb28HS24I5nB%2FXtpxqnbXXd%2B5HFTp1Ch%2B5l7YIJJLyLgYKrvbcsp0zN2i1CC1pPH6qBzumePFLJGkcQH5U7BXPVv%2BSJvC25IJUHTGW3ELIlHM3h3raLyxILfGjXFt0prN5CrZZk7n8M1jjTsA%2BBtpIjDOkhQ5KEh5cdjkBdtFiVDEoIGXnf3fgIjDxLW70%2BRd9UcFT5gjcJX5z%2F1U0O5EQwlHY3n8qUF0FbSwapxa%2BG0VTqnM3BHza5yKZ0AcAqeS1VRO0aGQ3%2F4DKiMVjj6ipaBgEaPQ186OH7nmYviyVogeTWb8acgrnlfORUeRBTLV6clBtyOZQMVqxWYyDl2lsyfrhjHZE3PQGApG2WUwt2AaR85z6JMnadoJXTAOtIjRId4OtYQ7q%2FRsHl8VZpa922mxYE5FdA1OVZAKzd3HOGHD6NxoIPFZhftmB3IQEd5%2FqbkNzGZ1psYreePrtd2pXOr5i%2Fj2qoET9suFs3y%2BEgqXgQv6mT3TGUr4He%2BFotk%2BV%2BLkonNap6XgyY9oUNuImw9qOcs20u4BY54Xo6sS7XO16llVgwgbf%2F0gY6pgFYatv3q%2FZgcZvBSlF7BMbX05sx5OgDkVbm5gK8ZCM%2FTSbJuS88OuoQ5joR%2Fw8STwQju5RrAdKNF6NOOnIHYWAXFPOzWJS2bNzDYGXHjmmWSArHLEuuInQFvcjeLavpVpiqmWa7%2FuHWtpBzFDNoBmzFQjie8P4AXZCwIlkXmqkc32gd3pgWhVcy4G6iUf6iBxyiuvnDe1LNiFKnmqhImf8dESR1yc3G&X-Amz-Signature=967c4be3d4cf1e4618d0455ef11638028d6a34d56c12523a9d81d8afd8897c41&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

同学们大家好，这一节我们来学习 spring boot 架构设计之智能装配 auto configuration。这里我们还是通过三方面给大家介绍。


首先介绍智能装配是什么，如何理解智能装配autoconfiguration。其次我们介绍一下 autoconfiguration 智能装备的工作原理，最后进行 autoconfiguration 自动装配的使用实践。好，我们现在开始看如何理解 autoconfiguration 使命put，在程序启动过程中，它通过上下文环境自动配置 spring 容器里面的这些bin。这里的上下文可以理解为程序依赖的第三方 job 和我们的配置文件，不管是属性文件还是不 IML 文件。比如说，如果说 HR 数据库这个炸包是在我们的 cost Paas 里面，并且我们也没有手动配置其他的一些数据源，并这样 spring boot 就会通过自动装配一个内存的数据库，也就是HR，这就是它一个自动装配的原理，也就是说我们没有做任何配置。它跟我们构建出一个猜测，我们可能会用到的一个bin，这里面就是 data source 识别不等，它是通过一种非侵入性的方式提供智能装配的策略。


怎么理解自动装配？它在任何时候我们都可以通过定义自己的配置来替换自动配置的一些特点。毕业比如说我们还是拿数据源举例，通常的业务我们不会使用内存级的数据库， HR 数据库，我们更希望是使用持久化的。像 MySQL 数据库，它的应用比较广泛。如果说我们配置添加了自己的 MySQL 数据源b，也就是我们配的一个 MySQL 的 data source，那么默认的嵌入式数据库就是内存数据库，它就会失效，也就是说这个 b 在自动装配阶段就不会装配这个 H2 数据库的 data source 了。


spring boot 提供的自动装配 auto configuration 非常多，如果说我们需要了解当前正在运行的应用中，哪些自动装配 auto configuration 是符合条件的，并且完成了自动装配，以及这个制动装配为什么能完成，也就是说它满足了哪些条件，这个其实有多种途径可以了解，我们可以在启动过程中开启指定的 debug 日志来查看。另外更建议大家通过 accuator 提供的自动装配的 Endpoint 给大家去看出来，后面会跟大家去讲到这一块。


另外 autocompaker 它支持自定义的配置策略进行干预，嗯，这个怎么理解？还是 spring boot 它提供的 auto configuration 非常多，某些特定情况下，我们是不希望某一个满足条件的 auto configuration 配置运行的，我们可以采用一种方式，也就是说对指定的 auto configuration 进行排除。排除的方式一般我们可以通过 enable auto configuration 配置include，或者说是通过 spring boot application 配置include，这种方式可以在对应的主函数方法上对应的类去执行。那么更推荐大家通过配置文件，也就是说在 application yml 里面，我们配置 spring 点 auto configuration，点 include 这种方式排除是也属于是全局生效的，现在我们开始学习智能装配 auto configuration 的工作原理。


我们如果说要启动通过 spring Boots 的自动装配，首先我们需要开启一下开启自动装配的方式，也就是我们加上注解 enable auto configuration，我们抛开 spring boot，在 spring 本身里面它是支持类似于这种 enable 什么什么操作的，比如说 enable cats， enable aspect 接等等这一些的注解它的使用原理是一样的，也就是开启某一个功能的等等原理。


那么对于这个注解它其实做了一件什么事？这个注解它的依赖是需要通过 auto configuration import selector 去驱动，引导我们去加载，那么他注的事情就是通过我们在 Meta info 下面的 spring their factory 的文件里面去找到我们配置了enable， auto configuration 为 kid 这些自动装配的类，我们获取到去进行执行。


那么我们看整个过程，也就是说首先要开启我们的自动装备，开启完自动装配，在系统启动的时候，通过 auto configuration import selector 去引导我们的系统去加载 Meta info 下面的 Sprinter factories 这个属性文件里面的内容。加载到这些内容，我们再通过反思方式调用 auto configuration seed 判断它当前条件是否达到装载的条件，达到条件就装载这个bin，如果没达到相当于是忽略，那么我们看一下在代码层面我们怎么去主。


首先我们要开启 enable auto configuration，一般我们写代码，我们的入口就是类似于这样一个 demo application 这样一个入口，但是我们看到这么简单一个 main 方法里面并没有看到 enable auto configuration 这个注解。其实我们在这里面可以看到这里面的 spring boot application 其实是对 enable apple configuration 做了一层包装。我们继续从这里面我们可以看到 spring boot application 它其实引入了 enable auto configuration，其实在 spring 里面它实现了这样一个语法的约束，也就是说当我们在一个定义的注解上面引入一个注解，相当于是这个注解的功能类似于一种继承的原理，当然它在注解是不存在继承这个功能的，它实现了类似于继承的效果。


好，我们接下来就看 enable auto configuration，我们在 enuv auto configuration，我们可以看到这里面的 add import 这样一个注解，这个注解的意思是什么呢？相当于是我们在解析的过程中要引入这个对应的一个实现类，这个类里面的内容是需要进行执行的，我们看它做了什么事儿，其实它做的工作相对比较简单，它就是要加载到我们对应的 Springer factories 这个属性文件里面的这些 KV 的值，在这里面我们只关注对应的 enable auto configuration 这个k，下面对应的value，我们可以看到这个 k 对应的 value 非常多，每一行就可以理解是 stream boot 提供的自动装配的一个类。那么在这里面这么多类，我们拿一个我认为是相对来说比较容易理解的 auto configuration，这个我们就去找一下 GDV seed autocompreson，也就是 GBV c template auto competition。其实 spring boot 它对整个实现做的抽象的非常简洁，我们看如果说我们想自动装配这个 GDBC template，那么我们它的实现方式是什么呢？我们可以冲着每一行去看一下。


第一个是configuration，这行我们可以简单理解，就是说它是作为一个 being 的配子，那么第二行就相对比较重要了，是 condition on class，它是什么意思？如果要装配 GDPC template auto configuration，它的一个条件，也就是说它必须满足当前的应用里面是有 data source 和 GDBC template 这两个类的，这也是比较容易理解的，如果说我们这个程序里面并没有引入数据源，或并没有引入GDBC，当然它是不可能去装载的，这是第一个条件。


那么第二个条件是什么呢？肯定是 on single cadicade，它的意思是什么呢？我们看注解的意思，可以理解为在整个容器里面只有一个 did source 这样一个数据源，其实我们是这样理解，但是 spin 容器它在装载实现的过程是这样的，其实我们的编译容器里面是可以有多个 data source 数据源的，但只是要求我们在 did source 里面必须有一个primary，也就是说指定为主数据源的一个鼻音。这是第二个条件。


那么我们接下来看，我们知道 GDBC template 这个对象是依赖 data source 这个 bin 的，所以说这里面构建了一个顺序，也就是说 auto configuration，它 off 的，也就是说 off 的 data source auto configuration 这个说明 g d b c template auto communication。我们构建 GDBC 对象， g d b c template 这个对象是依赖一个 data source 对象的，如果说我们 data source 也没有去配置的话，它需要通过制动装备的方式配置，那么它的顺序必须要在 this source auto configuration 之后。


好，我们完成这一步，我们再看这行是 enable configuration property，其实 enable configure property 它本身跟自动装备没有直接的关系，在这里面它是为了构造一个bin，这个 bin 的名字就是 GDBC property。后面我们会讲这个注解的意思，也就是说把我们在配置文件里面以某一种前缀开头的这些 KV 映射到对应的这个 b in 的属性上面。


好，这几个注解讲完了，我们看最重要的几个，也就是说 at import，它属于 spring 里面的注解。它注的作用就是说我再去引入 g d b c template configuration 和 name 的parameter， g d b c template configation，也就是说 g d b c template 这个对象，其实它包括一个本身的 g d b c template，还有一个 name 的 parameter g d b c template，也就是 spring 给我们提供的支持命名的一个 g d b c 操作，我们这里面我们进入 g d b c template configuration 去了解一下。


从这里面我们可以看到它的实现也非常简单，这里面它我们能看到它实现了 condonation on missing being，这是什么意思？也就是说在我们容器的上下文里面，或者我们的 bin 容器里面，它并没有一个 g d b c operation 的存在，这是什么意思？也就是说首先要求我们自己没有去配置这 DBC template，只有我们没有手工配置，那么这个自动装配才会生效，这也就相当于体验了它这个智能装配的道理，大家现在可以理解整个这个过程，现在我们开始进行自动装配的使用实践，使用词件我们是首先通过源码去了解自动装配原理，跟我们梳理一下自动装配的过程是一样的。


第二我们要理解自动装配过程的一些核心注解，我们通过源码去看一下这些核心注解的一些特征。最后我们通过单元测试与自动装配的一些关系去了解一下自动装配，为单元测试专门提供了一些类似于分片的自动装配方式。我们现在开始这里面我给大家构建了一个 auto configuration 的一个工程模块，这个工程模块是相对比较简单的，我们先看一下 power 文件，通过文件这里面首先它是整个是一个继承关系，向奥特康被用人继承 showcase 搜 case 继承 string 部的study，最终它是依赖了我们 string 部的 part 这样一个工程。好，对于这里面的依赖，它依赖到两个核心的，也就是我们的 stream boot starter Web 和 stream boot starter g d p c，这里面代表了我们的 Web Mac 开发。以我们的 Web 层和我们的数据层，这里面我们的数据源用的是内存数据库。 S2 这里面用到 long book 去简化一些我们的注解的方式。这里面是引入了一个我简单一个showcase，这个 tools 其实主要是为了打印 Bing 里面的一些 bin 实例对象。下面是test。好，我们现在看一下。


通过我们的入口方法，这里面我们的入口方法就是，嗯， Demo application 跟我们在 PPT 上讲的整个过程是一样的，我们把这个快速回顾一下，从这里面我们在启动的过程中是因为 spring boot application 它去加载了我们对应的 enable auto competition， enable auto configuration 其实在这里面它做了一层代理，在这里面怎么理解这个代理？我们可以看到这是 enable Automation 对应这里面且给一个别名，本来我们需要在 enable auto configuration 配的这些排除的超错，所以说通过代理它可以直接在我们的 spring boot application 里面就去可以去做这些配置。


好我们进入到 enable off competent，在这里面它这些配置也相对是比较简单配置的方式，我们可以通过类去配置排除，也可以通过名称去排除，这里面最重要的一个操作，也就是我们的 add import，它指定了我们的 auto configuration import selector。


如果说大家应该是明白这个 import selector 它的意义是什么？它主要就是说是一个 import 的一种实现方式，它就是说引入我们需要的一些类，这里面它实现了这个延迟的 import selector，我们可以跟进来看一下。对于这个 import selector，它最重要的一个方法，也就是 select importers，它是什么意思？它就是说我们通过这个类能找到哪一些需要加载的内容，所以说我们可以看一下它对应的实现，我们看这里面 slack 的import，我们可以跟进来，这里面它首先需要去获取到我们需要自动装配的一些配置，自动装配的配置是怎么去获取？通过这里面的方法获取自动装配，我们可以跟一下，在这里面我们看到他去需要去我们去做的事情是什么呢？我们需要首先找到我们可选的这些配置，找到可选的配置，再去排除掉那些我们需要排除的内容。


可选的配置是怎么做的？可选的配置是调用到 spring factory loader，如果大家比较理解的话，我们知道对于这个 spring factor loader，它是需要会去充 Meta info 里面去找 Sprinter factories，大家可以跟一下，我们接着跟进来，我们可以看到在这里面对应的它需要去取的文件就是这个配置文件，这个配置文件也就是我们的 BYTE Infor spring factories。


大家看到，那我们回过来继续看我们的主流程，这里面也就是说它获取到我们配置的这些configuration，与我们需要排除的这些去做一个差级的话，就是得到构建成一个对象，就是 auto configure entry，在这个对象我们就能获取到我们对应的内容，那么获取到对应内容其实我们这会儿可以去到我们这个文件里面去看一下我们 spring 步的 auto configuration，大家不要选错。从这里面我们可以看到它里面有 enable auto configuration，从这里面可以看到内容非常多，是很多的一些内容，所以说我们不会每一个都去看一遍，我们接着去看我们对应的 GDB seed，我们这里面可以去找到GDBC， template auto configuration，那么我们从这里面找到这个类跟进去看一下它的实现。


这几些属性我们都已经刚才介绍过了，所以说这里面我们重点的一看一下对于这些条件注解，我们看其实 string boot 它提供了很多这些相关的条件注解，我们可以看一下条件注解是基于这个肯定是 no 它去实现的，我们实现一个肯定的是 on class，基于肯定 ISM 在实现一些自己的一个条件注解，我们可以这样去看一下我们的内容，我们找到这个对应的实现的内容。


我们可以看到从这里面我们找到很多类似于 conditional on 一个什么条件的一些操作，可以看到充值里面首先是 on being on being，也就是说这个容器里面有这个 bin on class，也就是这个启动的 class bug 有这个类，这里面是在一个特定的 Claude platform，一个云环境，这个是当缺少某个病因，缺少某个class，这里面是当某个属性满足某个条件等等。


我们可以看到这些条件注解提供的非常丰富，也比较多，当然我们也可以根据自己的条件去扩展这些条件注解。所以说对于我们了解自动装配的原理来说，我们需要了解一下这些自动装配的注解还是很有必要的。我们还回到这里面一看一下，其实我们看整个这个过程，我们设计这个装备的这些注解还是需要思考一下的，这样真正能做到，如果说我们没有配置的话，它给我们构成，如果说我们配置的话一定要让这个条件能达到以我们自己配置的优先级最高，如果说已经出现我们的配置它就自动退出。


其实也就是通过后面这里面的内容，我们看一下这个对应的 GD b c template auto configuration 这个内容的意思，也就是说 condition on misbean，也就是说只有在我们的 Bing 容器里面不存在 GDBCA prison 它的实例，我们才会去构建这 g d b c template。


这个大家应该要有一种认识，就是说其实 GDB c template 它是我们类的实现 GDBC operation 是真正它的一个接口，我们可以看到 GDB c template 它是实现了 GDBC operation，这样更严谨地满足了。如果说我们自己实现了一个 GDBC operation 的实力，而不是 GDBC template，那么可能跟我们的预期就是不一样的。


好，我们接下来看一下智能装配单元词相关的内容。如果说我们实现这个，嗯， Demo application，如果说我们要进行单元测试，我们可能用到的方式就是这样的，我们会通过收构建一个单元测试类，这里面我们使用 spring boot test 方式去测试。那么我们看一下，这里面我做了一个对于 context 内容的一个打印，我们打印版看一下结果，当我们在执行的过程中，它会输出我们这个 contact 里面的内容。嗯，现在执行完成，我们可以看一下整个输出的内容非常多，我们可以看一下这个方法的实现，这个方法是打印的 bin 的 class name，所以说这里面对应的 name 和开 contact 对应的bin，我们可以从这里面看到就是这样一个格式，对应 test mock ITO 相关的一些内容，这里面还有一些事件监听相关的一些处理。


我其实比较想给大家介绍的是最终会输出一个 name count，也就是说整个 b in 容器里面有多少 b in，这里面我们可以看到有 150 多个。如果说我们在执行单元测试的时候，每次启动都需要引入这么多的bin，那么启动整个过程是需要耗时的，所以说 stream boot 它也考虑的这一点，所以说它会提供了一些，我们可以理解为 auto configuration benefits，用来去做一个分片的。


比如说我们看数据g、d、b、 c 相关的，在这里面我们可以引入一个叫g、 d p、 c test，它的意义是什么意思？其实它做的内容就是说我只是加载跟g、d、b、 c 相关的内容，我们可以看一下这个 GPT test 它的实现，这里面对于它的这个注解上面有一个 auto configuration test device，这里面含有 auto configuration g、d、b、c，也就是说我当引入g、d、b、 c test 的时候，它可以跟我自动装配g、d、b、 c 相关的内容和 test d base 相，就是 test DATABASE 相关的内容。这样的话我在启动的过程中，对于像string，web， yv c、 web 相关的内容它就不会装载，那么我们执行一下，看一下效果，这里面也同样是调用了刚才的实现方法。


我们看一下结果，这里面我们看到这个容器里面的 bin 是大概 50 多个。同时我们做数据测试的话，这里面有 GDBC template 的对象和 data source 的对象，也就是说能满足我们进行数据源测试的要求，这是我们 GDPC 的相关的，我们看一下 spring Web Mac 的，假如说我们只是测试 Web 层的内容的话，可能我们会对 service 和 DO 层的相关的数据去除mock，但这里面我们并没有去写 mock 实现的过程，后面我们的实例会会写这些相关的单元测试的代码，这里面我们先执行看一下效果，我们看很快执行完成。


这里面它涉及到的 bin 的个数是八十几个，我们想相比我们整个测试的过程，这个 b 数量少了很多，当然我们的启动的测试的过程也会稍微快那么一些。大家在了解这些功能和它的实现原理的过程中，大家一定要去思考，我们就要去想 spring boot 它是为什么要实现这个功能，或者说是它为了解决我们某个问题，所以说大家在一边学习新东西，一边去思考的东过程中，我们就会加深对这个知识的一些理解。比如说我们现在我们的对于 Web Mac test 和 GDBC test，那么还有没有其他类似的这种可以做分片测试的？这些 test 类当然还是有一些的，我们可以通过官方文档去看一下它全部的一些介绍，还有我们刚才提到的这些条件性注解。


那么条件注解 spring 本身是这个条件性注解，本身就是 spring 框架里面提供的内容，而在 spring put 它的实现过程中，它能对这个条件注解做一个比较友善的扩展出这些可自定义的这些条件，那么可以帮助我们完成 string boot 的自动装配。所以说基于 string 框架 string 部的做了一些新的扩展和一些创新性的用法，那么所以说带来了 spring 的一个新的延续。 spring 的一些自动装配的内容我们就先介绍到这里，好，谢谢大家。


