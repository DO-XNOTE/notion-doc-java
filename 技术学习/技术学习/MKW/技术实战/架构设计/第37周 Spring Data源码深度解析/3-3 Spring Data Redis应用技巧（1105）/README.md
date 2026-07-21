---
title: 3-3 Spring Data Redis应用技巧（1105）
---

# 3-3 Spring Data Redis应用技巧（1105）

[image](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/5d905268-6015-4240-8d20-fe3d24332e29/SCR-20240814-iwvq.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662NBU4YB6%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T232143Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDMTVZZXGSPwCp1xvoImw%2BEGMBdbzyt%2BabTcYJLlgysKgIgeh27JjZE%2FYszYM0GCM40vmdzE0CNOp%2FD4dksTLDMQ5cqiAQIxv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDGj%2BLuD%2F1WSZ%2FW9iayrcA3AhxWV2FJhHCq6PqK4wiCj6KH9qWcW%2Fy1wPDB89hTJUoKDiTnVY8vi2vrOJMibqpp2mZortxzTn6JvRJfKIEOqwmegTthhQrKoRYEzTDSY2xpCg9hMkbMepKuF6xAxITp%2Foi2CaDQvh%2FxZ0GzDWMtebUbxhRQDyCKY6EYqaAEjwNwFv34j1d6N%2FRKuoCknAS5M%2FtZKiH6Rbw%2FsepHFjLmgvDXL7U%2Frj400xiP35DSIyPML6svVNPlWeXN8TBuw3rRrDpdlYYpPVQW7vj1VhG3ToWFe3LbzamIDOzqc30AymXPYQRSLBp2jpznIFVQoNVPRRbCaM3uyaSwgbDc0CLfQfmLfVaQbc3%2Bo8RSeniittbKnEzR0fVNjSt7WATh%2FLTQhDyypIXiQlSiVT7a1JyuH3PUUcFd0IO3IuzTp%2FnLlBunA%2B52gkcNsON9LmNxnuvQJ4wiUQY70mSq5rLwwqRx1nqBx8vP%2Fro2AAflFEYev0rTW8m%2BQgjnvb4gWNAr55ua50dTMQuIfymEIuqot1Mx7g3TyGtvVZQkWY%2B98%2FswisZi1%2BNyeNqljOLY%2FW6U1UQXq1emkzZKmSQSzw9YC1RC4IpslJlGMt%2BZKerDUdacMRPRSVZBR8jMGneD8iMJu6%2F9IGOqUBICtQly9np1WDg0bmGY75FcEnZU7YfBaJoYm9TWQ%2FgQHIq71Cyot9a7XRrL2FuaDoaBSMv44cNgKh5NgELzygeZH%2BwEP6UaN3BVmu3Dt1vJhgxCh2K55OZYgE2929WgiQTwHd4wKrIWHeXU6uMq5nbPwB%2BI8r40QQ0gRcQmlYMCTpn1w9VIL%2BLtO2bV7FKoBPl1CpUOvSVL4pFBtu5rhm8oYdqHXq&X-Amz-Signature=8e832e8b1cf2f02f867116ca0b4f5d0c2138006aa0d180509a24b5927f46730c&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

[image](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/34a401ab-2565-4a7c-8e7b-aa02a06a1da7/SCR-20240814-iuyv.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662NBU4YB6%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T232143Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDMTVZZXGSPwCp1xvoImw%2BEGMBdbzyt%2BabTcYJLlgysKgIgeh27JjZE%2FYszYM0GCM40vmdzE0CNOp%2FD4dksTLDMQ5cqiAQIxv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDGj%2BLuD%2F1WSZ%2FW9iayrcA3AhxWV2FJhHCq6PqK4wiCj6KH9qWcW%2Fy1wPDB89hTJUoKDiTnVY8vi2vrOJMibqpp2mZortxzTn6JvRJfKIEOqwmegTthhQrKoRYEzTDSY2xpCg9hMkbMepKuF6xAxITp%2Foi2CaDQvh%2FxZ0GzDWMtebUbxhRQDyCKY6EYqaAEjwNwFv34j1d6N%2FRKuoCknAS5M%2FtZKiH6Rbw%2FsepHFjLmgvDXL7U%2Frj400xiP35DSIyPML6svVNPlWeXN8TBuw3rRrDpdlYYpPVQW7vj1VhG3ToWFe3LbzamIDOzqc30AymXPYQRSLBp2jpznIFVQoNVPRRbCaM3uyaSwgbDc0CLfQfmLfVaQbc3%2Bo8RSeniittbKnEzR0fVNjSt7WATh%2FLTQhDyypIXiQlSiVT7a1JyuH3PUUcFd0IO3IuzTp%2FnLlBunA%2B52gkcNsON9LmNxnuvQJ4wiUQY70mSq5rLwwqRx1nqBx8vP%2Fro2AAflFEYev0rTW8m%2BQgjnvb4gWNAr55ua50dTMQuIfymEIuqot1Mx7g3TyGtvVZQkWY%2B98%2FswisZi1%2BNyeNqljOLY%2FW6U1UQXq1emkzZKmSQSzw9YC1RC4IpslJlGMt%2BZKerDUdacMRPRSVZBR8jMGneD8iMJu6%2F9IGOqUBICtQly9np1WDg0bmGY75FcEnZU7YfBaJoYm9TWQ%2FgQHIq71Cyot9a7XRrL2FuaDoaBSMv44cNgKh5NgELzygeZH%2BwEP6UaN3BVmu3Dt1vJhgxCh2K55OZYgE2929WgiQTwHd4wKrIWHeXU6uMq5nbPwB%2BI8r40QQ0gRcQmlYMCTpn1w9VIL%2BLtO2bV7FKoBPl1CpUOvSVL4pFBtu5rhm8oYdqHXq&X-Amz-Signature=4c725594bc1bc6fd361ebf0f8c2fe6403b6198094b82bc877cde60b5481cfe65&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

同学们大家好，这一章节我们来介绍一下 spring day 的 Redis 应用技巧解析。那么关于 Redis 呢？我们重点来看一下对应的 Redis template。那么 Redis template 里面主要包含两类对象，一个是operations，另一个是一些跟序列化相关的内容。首先我们来看一下对于操作成这一些 operations 跟 a Redis template 的关系。然后我们来看一下序列化，也就是跟 Redis seller 相关的这些序列化相关的内容。


那么我们接下来看一下对于 Redis template，它这里面去包含的内容主要是什么呢？主要就是 operations 和 Redis sellers，还有一些基于配置性的一些 configuration 相关的一些内容。那么对于operation，我们这里面列出来一些，我们可以看到通过 Redis template 对 Redis 进行操作，最终还是依赖 all presents 进行一些操作。比如说我们对于哈希的一些操作，这里面有哈希operation，对于 list 操作有 list operation，对于set，value， reset 这些都有它对应的一些operation，同时还有一些 GU 的prison，关于一些位置相关的操作，后面还有一些 bound 赛的operation， bound 哈希 operation 这些你等等一类对于 operation 的操作。


其实它是 ins 了 Redis 真正的一些操作的一些过程，那么这里面对于通过 Java 的对象，通过 operation 操作存储到我们的 Redis 里面，这个过程还涉及到了一些序列化和反序列化的操作，那么对于序列化和反序列化，我们这里面的 string date Redis 提供了一些常见的一些 Redis 的 sellers 的一些实现。


这里面首先我们使用最多的应该就是我们的 screen Redis realize，他就把我们的对象的 string 就是序列化和反序列化成。首先是序列化和string，我们通过 string 获取这个对象的过程，在反序列化我们对应的对象另一种方式就是这里面词有 Jackson two，我们使用 Jackson two 的 Jackson 的方式进行 it is service 的一些序列化的操作，我们还支持一些 x narrow 相关的一些序列化操作。


底下有对应的是 generic to string generic，它就是我们会对于泛型的一些炒作，通常我们对一个 list 里面这个泛型的对象进行一些序列化的一些实现方式，底下还有一种是一个 JDK 的 series Redis series，其实这种方式是不推荐大家使用的，至于为什么不推荐大家使用，大家可以想象一下，其实我们在迭代开发的过程中，如果说我们把一个 bin 直接使用 JDK 的方式序列化成一个枝节流，把它存储到 Redis 里面再返回来的话也会返回来流对象。但如果说在整个我们代码迭代的过程中，我们把这个对象修改了，那么它在反序列化过程会失败。


所以说如果说我们使用了 GDK 的序列化工具的话，那么对于我们系统兼容升级会带来很大的挑战，所以说这里面通常我们会建议大家基于 string 的 Redis 或者基于Jackson，我们基于 Jackson 的方式进行序列化，那么这两个方式都是比较给大家推荐的。那么关于 Redis template 怎么使用？我们来看一下我们 showcase 的对应的 Redis 的模块，这里面我们看首先我们到我们的 Redis showcase Redis 模块，在这里面我们来看一下相关的一些内容。


首先我们这里面写了一个单元测试，就是基于 Redis 的 template test 单元测试，如果说我们正常使用 spring boot 对应的 spring Redis 方式启动的话，我们的上下文里面会构建出我们的 Redis template 这样一个bin，那么我们可以直接注入这个 bin 就可以进行我们相关的一些操作了，对这个 rest template 在什么时候构建还产生疑问的话，我们可以通过它的引用去看一下它在什么阶段去调用的。


那么什么阶段去实例化的，我们来这里面去看一下 Redis template，我们根据引用我们去查找一下。通过这里面我们看这里面有一个 Redis auto configuration，也就是我们 spring boot 的自动装配的对象。在这里面我们会看到涉及到了一个 new Redis template 的一个操作，在这里面我们可以猜想到它在这里面去构建了我们 Redis template，我们可以贴进去看一下。从这里面我们可以看到在这个自动装配的类里面，我们实现了一个 Redis template being，我们看对应的 bin 的注解，这里面构建我们 Redis template。


必应的过程中，我们使用了 Redis connection factory，那么在这里面我们首先通过 new 构造出我们的 Redis template，然后把我们这个 connect factory set 进去，这样就得到了一个我们可用的 ready template，一个这样的对象，这样我们就知道了 Redis template 的词在什么时候实例化的。


那么接下来我们再看一下 Redis template 的这个类里面，它包含的内容都有哪些，我们可以看到从这里面一眼看过去，首先是我们 ready services，也就是说我们跟序列化相关的一些内容，这里面我们看涉及到 k series 和value，还有哈希，我们的哈希 k 哈希 value 等等，这里面还涉及到一些。这里面 string serverless，再向下滚动，我们可以看到相关的一些operations，这里面有 value operation，我们的list，set，我们的 stream 等等。


reset， GU operation 等等，这里面会很多，我们可以看到这每一个 operation 它都是对应一个接口，整个接口它有一个默认的实现，我们可以看到它默认的实现通常是 feel the value operation，它这个 operation 它通常也是继承了 abstract operation。


我们可以看一下整个这样的一个树结构，我们可以看到在 abstract operation 下面的一些对应 operation 的一些 debug 的实现，这里面可以看到它的结构是很清晰的。那么我们回到我们的 Redis template，那么这里面我们可以简单知道它整个这个过程，那么我们在使用过程中怎么使用呢？我们可以看到这里面是 of the prodecide，那么使用的过程呢？我们是比较简单的，这里面如果说我们进行操作，我们首先去看一下我们是对什么进行，对于 KV 操作还是对于哈希操作，或者对于赛的操作。
我们通过 Rights template 直接 OPS for value，我们获取到我们对应的这个 operation 就可以了。同时如果说我们对于其他的类型的操作，我们也可以，我们可以看到这里面我们能获取到我们想获取到的所有的这些对应的operation。我们可以看到这里面是value，哈希 list set plexer，我们的GEO，我们的Hyperlog，我们的stream， reset 等等，这里面是跟 bounds 相关的一些这样的一些 operation 对象。


所以说我们可以看到其实这样我们获取到对应的一个 operation 对象以后，可以进行我们对应的相关的一些操作，我们可以看到 reset 相关支持的一些内容，我们看到 RESET operation 支持的一些方法，这里面涉及到像 rings 相关的一些操作。


通过这里面我们可以看到如果说我们简单的去对 Redis 相关操作的时候，我们去如果说是也定义一个 reports 的，这样的话我们的工作显得比较重一些，那么如果我们只是简单的对于一些 KV 缓存的操作的话，也建议大家直接在这边使用 Redis template，用通过 Redis template 获取到对应的 operation 来进行我们相关的一些操作，那我们了解了我们这些 operation 相关的一些操作的情况，其实我们需要做什么操作就获取到什么对应的 operation 就可以了。


接下来我们来看一下我们的序列化相关的操作，我们从这里面 Redis template 里面看到这里面有很多跟序列化操作相关的一些属性，里面key，value，最终它还是都是实现了 Redis strategy 这样一个接口，那么我们看一下它底层的一些实现。


首先我们看最基本的一个实现就是 string Redis strategy，那么我们可以看里面的两个关键的方法，这个方法分别是我们的序列化和反序列化操作，这是我们把一个 string 的序列化，我们的一个字节流，那同时这是我们通过 ready 的获取到字节流，反序到我们对应的 string 对象。因为我们的字节流和 string 对象它是有一个天然的映射关系，我们可以看到在这里面我们序列化的过程中，就是我们把我们的 string 对象 get badcase，我们去指定一下我们的支付器编码。那么对于反序列化，同时也是我们把我们的字节流字，也就是字节的数组字节，通过 new 的方式构建出这个string，这种方式其实是天然，对于我们 string 类型的存储的话，是支持这样直接去使用的。


那么另一种我们可以看到对于我们 Redis 常见的也就是我们的Jackson，那么对于我们的 Jackson to Jackson 的 Redis service，这里面我们对于每一个我们的序列化执行器需要指定一种 Java 类型，那么因为我们在构建的过程中，我们可以看到在这里面我们通过构造方法创建这个序列化器的时候，需要指定一个加 r 类型，因为我们在序列化和反序列过程序列化无所谓，因为我们序列化的时候它本身这个对象是带着类型的，但是反序列化就会有问题。


那么我们把一个字符串反序列化的一个对象，我们必须指定反序列化为什么对象，那么这个参数，这个 type 就是在这个阶段时使用。这里面我们可以看到对应它的序列化和反序列化，其实也就是我们把一个对象序列化的一个 JSON 对象，或者是把 JSON 对象反序化一个 Java 对象的一个过程。如果说我们对于 JSON 是用 Jackson 的 object Mapper 进行，我们的 JSON 的序列化比较清楚的话，那么对于这里面也是非常容易理解的。


那么接下来我们再看一个例子，这里面我们看一下是 GTK 的servertiser，也就是说我们基于 GTK 默认的序列化排序的话，工具，其实这个刚才也提到了，并不推荐大家使用，但是它也是整个默认的，所以说我们也要了解，所以说建议大家去在底层配置的时候把它给替换掉。


我们可以看到这里面对于序列化、反序列化的操作。首先我们来看一下序列化的操作，对于序列化操作，这里面我们看到这里面是由 services 进行一个转化，我们看一下它的实现，对于它的实现我们去跟一下，这里面我们有一个默认的设置，在我们的构建我们的这个 DDK select 这个区域化系统，这里面一个是序列化convert，一个是反序列化的convert。我们先看一下序列化的convert，那么序列化 convert 这里面是一个 debug 的surless，那么我们也跟进去接着看。


那么对于一个 debug 的 service 它是怎么实现的？我们可以看到这里面是有一个 object output stream，也就是这样的话我们可以看到是一个对象的一个 output stream，所以说它使用了我们 GDK 默认的一个序流化的一个对象流，输出流，那么这样其实它就存在的问题就是当我们反序流化的时候，如果说我们的 b 在迭代过程发生变更，那么它在过程就会出现一些问题。也就是说通过这种方式序列化跟我们的语言进行了一个强绑定，那么我们通过这种方式放到 Redis 里面的对象，它不可能被其他语言读取出共享，所以说这就是它带来的一些弊端。


那么我们还回到 Redis template，我们可以看到整个这些过程，我们可以通过里面去进行一些操作，获取到我们对应的 operation 进行相关的操作，那么在操作的过程中会使用到了我们这些序列化、反序列化的一些机制去完成我们跟 Redis 数据的一些读写。那么回到我们 spring day 的 Redis 的对应的PPT，这里面我们简单去介绍了一下 spring day 的 Redis 下面的 Redis template，以及我们的operation，我们这些 operation 的集合，还有我们常见的跟 Redis 相关的序列化，反序列化相关的一些默认实现。那么我们 string d 的 Redis 的应用技巧解析就先介绍到这里，我们去，我们下一章节再见。


