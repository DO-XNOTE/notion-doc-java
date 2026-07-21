---
title: 3-7 RabbitTemplate池化封装
---

# 3-7 RabbitTemplate池化封装

[image](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/f84e1d55-90da-41be-b333-f055f38ecb6b/SCR-20240806-rcng.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466U4BP5GLP%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T225301Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDgm0Bzv9ymEOQIsL2BQtHlKXbKrjFfGmEeh6Xy9P1c%2BgIhAM7S4FRKhuRytU71s3k01ARh5ojnt5U4SawPDcRO2bBwKogECMb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgyVL92%2B6E4ElUxFUXMq3AOKo%2BDoMraNHnua4E8m6qpXneC9QBTLj8L12OCeU1o%2BFVdE5oBm4kCOHm8kVXmRXeIqZPFkEYdxMEib%2Fi16ksoBM8LADKH2nlYPfKyu1NvHeR6njsYMEIuQZp57hJ2txLuZyL89hl2bfr6aHs7hObXaDoFjQSMpWXlItmKTi7kjWzAMMLPPzdwaiZ1w4kcD2ipb8tVwxFdxzVW6eAfYOmo%2FJDxe87CwFmFW%2BDVMQvMEqJxpREgOexaYRZCO4EvOTJtNMrkX74hptVrk0gl6IQIoS98NtmZXLBAu3aID6teOZCF5v1%2FMZl4iykPWrLFK8YBnw0L5VZdFzD3Szst3LYjKO2fsG9f4EX6WoKaKbou9YGbb5Wl4G3k84FzqY3S%2Bfc9m%2FRCYqnlp3xBcrfptQGDRNYt4WQuU7gYwjXBn%2FaUk73CDHCvhjYRq4VIZXwi407hR7Uy3%2BSQH4aSv9pUV8llDRu3lpWNjs5LvPwpOBmnnGQOrWrqp8BYKy0s7WcdsxwHSzstU96CdXxltN6X9frt2g8V%2BEtBESiMnYT9GowbjWdP0Mgm8tun0MTERgGdyVTg5yFjRpNYHNT5KjBK3OVsQnPQBnjzIJgzbDCWzSpsbzI0JrG04KFyPVI90%2FzD8uf%2FSBjqkAWldmX%2FSOjiYkKWpGz8KJI8eQHajTd3251yiGyBNo2RYHZbFf04vJ4AtKR99UZeppdjnphJ8A1L3culERLRjcPNySbZgCXkS5CoqbddH3zE7t2YUuDtO9zu%2FRscyLb7l%2FIahdjL5USw5uk5NhrhYW0M2cFZP6wH%2BLd%2B5bYu8wk5Uxh6aBrsFqvXwU2X0qnexDCKGIdfeEhGrxZnJ5cOYaINZTpvb&X-Amz-Signature=38f8393e5d123b7deb0c22586764a715e3d9515dc422fcd91d7f1c494f43740f&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

[image](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/5589fcc6-4574-407d-996e-2d11977fae08/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466U4BP5GLP%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T225301Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDgm0Bzv9ymEOQIsL2BQtHlKXbKrjFfGmEeh6Xy9P1c%2BgIhAM7S4FRKhuRytU71s3k01ARh5ojnt5U4SawPDcRO2bBwKogECMb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgyVL92%2B6E4ElUxFUXMq3AOKo%2BDoMraNHnua4E8m6qpXneC9QBTLj8L12OCeU1o%2BFVdE5oBm4kCOHm8kVXmRXeIqZPFkEYdxMEib%2Fi16ksoBM8LADKH2nlYPfKyu1NvHeR6njsYMEIuQZp57hJ2txLuZyL89hl2bfr6aHs7hObXaDoFjQSMpWXlItmKTi7kjWzAMMLPPzdwaiZ1w4kcD2ipb8tVwxFdxzVW6eAfYOmo%2FJDxe87CwFmFW%2BDVMQvMEqJxpREgOexaYRZCO4EvOTJtNMrkX74hptVrk0gl6IQIoS98NtmZXLBAu3aID6teOZCF5v1%2FMZl4iykPWrLFK8YBnw0L5VZdFzD3Szst3LYjKO2fsG9f4EX6WoKaKbou9YGbb5Wl4G3k84FzqY3S%2Bfc9m%2FRCYqnlp3xBcrfptQGDRNYt4WQuU7gYwjXBn%2FaUk73CDHCvhjYRq4VIZXwi407hR7Uy3%2BSQH4aSv9pUV8llDRu3lpWNjs5LvPwpOBmnnGQOrWrqp8BYKy0s7WcdsxwHSzstU96CdXxltN6X9frt2g8V%2BEtBESiMnYT9GowbjWdP0Mgm8tun0MTERgGdyVTg5yFjRpNYHNT5KjBK3OVsQnPQBnjzIJgzbDCWzSpsbzI0JrG04KFyPVI90%2FzD8uf%2FSBjqkAWldmX%2FSOjiYkKWpGz8KJI8eQHajTd3251yiGyBNo2RYHZbFf04vJ4AtKR99UZeppdjnphJ8A1L3culERLRjcPNySbZgCXkS5CoqbddH3zE7t2YUuDtO9zu%2FRscyLb7l%2FIahdjL5USw5uk5NhrhYW0M2cFZP6wH%2BLd%2B5bYu8wk5Uxh6aBrsFqvXwU2X0qnexDCKGIdfeEhGrxZnJ5cOYaINZTpvb&X-Amz-Signature=d4b16d580007c9971dd55355bacc7b6ad32a57311bbb41e11a47734cb9608201&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

[image](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/d2e930df-1711-43e7-b6ed-cc2a34d4c71e/SCR-20240806-redt.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466U4BP5GLP%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T225301Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDgm0Bzv9ymEOQIsL2BQtHlKXbKrjFfGmEeh6Xy9P1c%2BgIhAM7S4FRKhuRytU71s3k01ARh5ojnt5U4SawPDcRO2bBwKogECMb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgyVL92%2B6E4ElUxFUXMq3AOKo%2BDoMraNHnua4E8m6qpXneC9QBTLj8L12OCeU1o%2BFVdE5oBm4kCOHm8kVXmRXeIqZPFkEYdxMEib%2Fi16ksoBM8LADKH2nlYPfKyu1NvHeR6njsYMEIuQZp57hJ2txLuZyL89hl2bfr6aHs7hObXaDoFjQSMpWXlItmKTi7kjWzAMMLPPzdwaiZ1w4kcD2ipb8tVwxFdxzVW6eAfYOmo%2FJDxe87CwFmFW%2BDVMQvMEqJxpREgOexaYRZCO4EvOTJtNMrkX74hptVrk0gl6IQIoS98NtmZXLBAu3aID6teOZCF5v1%2FMZl4iykPWrLFK8YBnw0L5VZdFzD3Szst3LYjKO2fsG9f4EX6WoKaKbou9YGbb5Wl4G3k84FzqY3S%2Bfc9m%2FRCYqnlp3xBcrfptQGDRNYt4WQuU7gYwjXBn%2FaUk73CDHCvhjYRq4VIZXwi407hR7Uy3%2BSQH4aSv9pUV8llDRu3lpWNjs5LvPwpOBmnnGQOrWrqp8BYKy0s7WcdsxwHSzstU96CdXxltN6X9frt2g8V%2BEtBESiMnYT9GowbjWdP0Mgm8tun0MTERgGdyVTg5yFjRpNYHNT5KjBK3OVsQnPQBnjzIJgzbDCWzSpsbzI0JrG04KFyPVI90%2FzD8uf%2FSBjqkAWldmX%2FSOjiYkKWpGz8KJI8eQHajTd3251yiGyBNo2RYHZbFf04vJ4AtKR99UZeppdjnphJ8A1L3culERLRjcPNySbZgCXkS5CoqbddH3zE7t2YUuDtO9zu%2FRscyLb7l%2FIahdjL5USw5uk5NhrhYW0M2cFZP6wH%2BLd%2B5bYu8wk5Uxh6aBrsFqvXwU2X0qnexDCKGIdfeEhGrxZnJ5cOYaINZTpvb&X-Amz-Signature=9e11e261ab70a0ebffddfdc54c3fbfbf6577e4cf01f30059fcfac70c57b128de&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

刚才其实我们已经把发送迅速消息跟大家已经封装完了，我录一下这个代码。首先第一步就是我们，哎，有一个 Rabbit broker，就是有一个这个 producer client 这个类，然后真正去 send message，当然这个 send message 有几种方式，有正常的去发消息，还有带回调函数的以及批量发消息这三种。然后在我们真正的去根据不同的消息类型去做真正的发送的时候，又抽象出来一个叫做 Rabbit broker 这个接口，它能够帮我们去真正的去发迅速消息，确认消息以及可靠性消息这三种。然后我们再去调真正的去发消息的时候，你会发现它是 Rabbit broker implements 去做的实现。


然后真正发消息的时候用的是谁？用的是 Rabbit template，对吧？那 Rabbit template 在真正发消息的时候又做了一层异步化，就是我们的这个 async base key，它其实就是一个线程池，然后做一个异步的发送，在成功的时候就发出去了，可能拒绝的时候就 reject execution handler，打一个 l 日志OK，然后调用它的这个 submit 方法去做一个提交。


回过头来同学们想下一件事情，就是说我们每次发消息，那 Rabbit template 这个东西如果你这样去用会不会有问题？其实 Rabbit template 呢？它 auto where 进来它是一个什么？它是一个单立，我们都知道这个东西肯定是一个单立模式，比如说我现在经常的去改它的topic，包括它的 routine key 也经常的去发生变化，包括其实后面你的 rapid template，它其实有一些自己个性化的这些定制。


比如说我想去发确认消息，是不是得封装一层 consume callback，有些消息我可能需要做一个什么 return 消息等等都可能，那它可能有的时候它在 set 的时候它有好多属性，我们来看一看，看一看这个 timely 它能 set 出来多少个。比如说它的 set ministry，还有 set Queen，它有可能不同队列，包括 set recover callback，就是在故障的时候还有一些什么其他的 time out 等等，那其实对应着就是每一种 topic 它可能都对应着不同的template，所以说如果你这样只用一个单例的话，它的性能会很慢，所以说我建议在这里给大家提供一种方式。


就比如说我们把 RAB 的 template 做一个池化操作，我们以谁为key？我们可以以一个不同的 topic 为key，这个 topic 它就对应着一个 Rabbit template。所以说我们要做一个迟换，目的是提高多生产者去发送，提高性能，你就单生产者去发送的话，你的 rap template 它是一个单立模式，它的性能肯定不高，我多生产者肯定它的发送效率会高，这是第一点。


第二点就是说有一些 template 它有自己制定化的需求，那你也可以去进行自己制定的配置，这个是非常灵活的。所以说一般在实际工作中，如果你想去封装的话，都会去把 Rabbit template 做一个池化处理，我们先去看看这个池化的 Rabbit MQ，这个 Rabbit template 应该怎么去做？那在这里我现在不用这个，直接奥特维尔进来 rapid template，因为我要做一个池化处理，所以说在这里我先建一个类，在这里我叫做 Rabbit template container，这个目的的意思就是说池子 Rabbit template container，它就是一个池化。然后比如说他做一个什么 component 交给 spring 管理，然后他要有一个日志输出，就是s，l，f，o，g，k。


然后在这里首先我们需要哪些内容？首先第一个就是我要做池化，我就有一个 private 的什么呀？map，然后他 string 是我们的这个topic，对不对？我们可以写上value， value 就是我们的 Rabbit template，就是我把 Rabbit template 放到这里来了，同学们要注意，然后这个我们叫做 container map，等于什么呀？这叫做 Rabbit map OK，然后在这里它等于直接等于 new 一个maps，点 new 一个 concurrent map，可以了。


好了，同学们第一步做完了一个池化的 Rabbit template，对象已经构造出来了，对不对？它很简单，就是然后做完池化操作，我们应该做什么事情呢？比如说连接工厂，因为你需要用到这个 rap 的template，那肯定必然需要连接工厂了，这个连接工厂我们可以直接注入进来，因为你现在用的都是这个 spring 的方式，所以说你就直接 all to where 的。


Habit connection factory. connection factory 肯定是用了我们的这个 MQP 的哈，OK，然后 connection factory 注意，在这里你一定要注意我到底是选择哪个。你现在用的都是 spring from Mock 的，所以说你这里边也尽量要是 spring from Mock 的 MQP 的产品，就是连接工厂直接注入进来就可以了。


接下来还有哪些？比如说，那我既然是想通过这个 rapid template container 去获取一个template，那怎么办？我有一个方法，比如说我说 public get template 返回的就是我们的 Rabbit template，咱们叫做 get template，然后传进来一个message，我就能根据这个 message 里边的 topic 去判断我到底有没有这个。他们 throws 一种 message 就 throws message exception，因为这是获取，获取不到它就不一定是 run time 了。OK，我就先这么去写了。然后这个 message 就由我们自己的。首先我可能要做一个校验，那个校验我们之前就已经做过了，我们在发散的客人消息的时候就这个做一个check，第一步就是这个 message 是否为空？ message 如果为空的话，那是不是也是有问题的？然后接下来干什么？我们来获取它里边的topic，所以 message 点 get topic，你现在是 topic 当成 key 了，然后跟一个 Rabbit template，这个为 KV 建设。对的，所以说那你就直接取呗，你直接从这个 map 里取吧。


我说点 get p topic，返回的肯定是一个 Rabbit template，对吧？我就直接这样去写，如果它不等于空，那就直接返回呗，不等于，那对不对？那就证明我们之前这个容器里边已经有了，所以说我们就 return 这个 right 他们就可以了，其他情况下就不等于空。那我们可以打一个日志，是不是 log 点 infer 说topic。

She is not exist.


然后 create one，然后把 topic 放进来，就当前我们的这个里边一个井号 a 点我们的 get template，对吧？还是用我们的写法好，当前打一个日志，说当前如果不存在这个 topic 所对应的 rabbit template 的话，那我们就帮你创建一个，然后打一个日志。


好，已经有了的话，那我们怎么去做呢？同学们想一想，那 rap 的 template 怎么去创建？很简单了是不是？这就是 spring MQP 嘛？我们自己手动的去创建一个 rap 的template，那太简单了，这个怎么还有一个 re 呢？re，去掉， Rabbit template，然后咱们这个叫做 new Rabbit template， new Rabbit template 等于 new 一个 Rabbit template，这里面需要一个什么呀？一个 connection factory 就是我们之前需要传递的奥特维尔进来的，对吧？然后有了它之后接下来我们要做什么事情？刚才我说了这个它一定要 set 我们的exchange，这个 exchange 就是我们所谓的什么topic，然后还要去对它一系列的内容做一系列的设置，比如说我们现在有了 topic 了，还有什么呀？比如说它有一个点set，那我们来看一看哪个比较关键？比如说 retry 


template，做厨试的时候可能需要用到，那在这里我们把它弄出来就好了，就直接 new 一个 re try template，好让他帮我们一个同事。还有其他的吗？我们来看这个太长了，我们叫做 new template 吧，给他起一个比较简单的名字，还有比如说他的 roading key 是吧？这个 roading key 一旦确认肯定就是一致的了。


OK，像 set routing key 是吧？这个 routing key 那肯定是通过这个取出来的，那就是 message 点 get routing key 就好了， message 有，是不是？那我们直接取吧， get rooting key 好，然后接下来其实还有一个很关键的内容，是什么呢？就是你去做序列化的时候，这里边有一个比较关键的叫 set message come water，这个是非常关键的，就你怎么去做序列化？我其实我想去做一个提高性能的序列化机制。这个我在这里先打个注释，我们下节课的时候再跟小伙伴们一起去讲序列化。对于 message 的序列化方式，这是我们下节课去讲的，我们这节课先把它放到这，我们继续往下去走。


接下来什么呢？我们的 rap MQ 里边有什么样的类型？比如说就像我们的confirm，那 confirm 就是表示一个确认，那 confirm 要做什么事情？要做一个回调函数，这个回调函数在哪写比较好？其实我完全可以这样去写，还记得那个回调函数应该怎么去做吗？我们回过头来看一下我们之前写的这个 Rabbit producer，这个回调函数就是直接 confirm call back，就是我们很早以前讲 spring boot 跟 red MQ 结合的时候，对吧？就是一个 confuse call back，然后要重写 confuse 方法，那其实我们完全可以干什么？我们完全可以把我们自己的现在这个 Rabbit template container 让他去实现，我就直接这样去写，没问题。是不是让他去实现 Rabbit template？重写一个方法就是重新实现它的 confirm 方法，保存一下，这样是不是就可以具体这个 confirm 怎么去实现？这个我们后面再说具体的消息应答。


好，那同学们想一想，现在这是一种确认的消息，什么情况下我们需要加上这个 config call back？说白了就是一句话，只要不是迅速消息，其他的任何的消息都需要对消息的应答做一次confirm。 call back 就是做一个可靠性投递，也需要做一个 concern 模式。需要，那比如说我们来看之前的这个 API 的定义，我们来看我们的这个 message type 有三种，第一种是迅速消息，第二种是 confirm 消息，第三种是 relate 消息。就无论是 confirm 还是说这个relate，它都需要做一个confirm，只有什么？只有迅速消息是不需要 confime 的。


所以说其实这个条件判断很简单，就是你写一个最简单的判断，我们在这里取到我们自己的这个 message type，等于 message 点 get message type 取到了之后直接判断说if，如果 message type 第二，这不是迅速消息嘛。第二 ECO 是你自己的这个 message type，那这个我就不需要填充了。反之只要它不是迅速消息，那我都需要设置 call back，对不对？ call back 就是当前本身这个 Rabbit template container 自己，它实现了这个 rapid template，点 callback consume callback 这个接口，对吧？所以说完全就直接这样去写，当我的 template 这个 new template，直接点 set confirm 好吧，就是 diss 了，只要它不是迅速消息，那我就把它加上回调就可以了。


然后最后做什么事，最后就是直接往这个 map 里去 put 就可以了，对吧？唉，直接第二 put if such 就是如果存在了，那我就不往里 put 了，如果不存在我就去put。那它的 key 是什么呀？ key 就是套便啊， value 就是当前的这个新的产品的本身。好，然后最后我就把它返回就可以了。我 put 进去了，直接返回就可以了。return？谁？return？就是这个 map 点 get 差不多，对吧？同学们来看一看这个逻辑是不是很简单？就是说我通过消息去获取一个模板，如果存在的话直接返回，如果不存在那很简单，我就去创建一个template，创建一个template，然后把它 exchange 设置好，然后把它 routing key 设置好，然后把它 retry template 设置好。如果有序列化，再把它的序列化的这个一些相关的内容设置好，然后根据 master type 去判断它是否要加它的这个 return callback 接口的内容，这个时间类它的这个 confirm call back，这就是本身就因为我自己这个 rapid template container 已经实现了这个接口了，后面我们把这个 config 方法写好就可以了，然后做完这个事情之后就只要它不是迅速投递的消息，那它都应该去设置一下，对吧？然后最后把它放到容器里，然后把它取出来，这就 OK 了。


同学们想一想，我现在问你，那我应答的时候我应该做什么事情呢？以及我这个序列化我应该做什么事情？这个是小伙伴们应该思考的问题。那其实我们先可以简单的去看一看，当我们去做确认消息的时候，我应该做哪些事情。比如说我们做确认消息的时候，我们能返回几个参数？第一个是 collation date，第二个是ACK，第三个是它的一个异常信息。那首先我们这个 coloration date 是怎么来的？我们回过头来看一看迅速消息，迅速消息的时候就是等于他我们点进去，它具体实现迅速消息的时候，调的是这个car，对不对？ car 的时候已经做了一次处理了，说我按照井号去分隔了，前面这个是我的 message ID，后面这个是我的 current minutes 当前的时间戳，对吧？那我按照井号是不是可以做一个分隔？那所以说我们在这里边可以去按照井号去取到这个 calculation date 里边的两段，前面这一段就是我的 message ID，后面这一段就是我们的当前时间戳了哈。


OK，好，那我们来写一写，我们直接可以再加一个。嗯，小的一个对象，我在这里直接可以写死了，很简单，private，它叫split，这个肯定是也是 Google 的，包括下面的这个具体的这个一个简单的工具类了，斯克利特，然后等于斯克IT。点就井号嘛，关键字，是吧？按井号分隔，然后有了这个 split 就好了。那我直接来看一看这个具体的内容，我应该怎么去把它做出来？那第一步就是按照它去分隔，比如说我现在把它就是按照什么去做一个灯格，那就是 split 点，它有一个 split to list 这么一方法，直接帮我转成一个list， calculation date 点 get ID。


calculation date 点 get ID 是什么？就我们之前已经写了这里边的这个 format 这个东西，它其实里边存的就是一个ID，只不过把它 ID 按照井号去给它拼接在一起了，前面是一个 message ID，后面是一个当前时间戳，所以说我截的时候我也按照井号截就好了，没什么可说的好。


截出来返回一个list，是不是我们用一个 list 来接收一下这个string，我们叫做strains，接收完了之后它肯定会有 SPA ID 是什么？我们叫做 message ID，肯定就等于点 get 0 了前面这一位，然后接下来第二位是什么？第二位就是我们的发送消息的时间，直接点 get 1，然后也可以把它这个转成 long 类型，就是我们的long，我们叫做 sand time，等于 long 点 pass on 对不对？我们按照这个规则去拼的，所以说我们就取也是一样的，这肯定不会有问题。然后我们接下来看 a C k 了，如果 a C k 了，证明他给我成功返回结果了。


如果成功返回结果了，我要做一件事情，我要做一下记录，比如说我要做一个叫confirm，我在这里先打一个日志，说 send message，意思OK，发送消息成功了，然后 confirm message ID 是什么对吧？ message ID，然后逗号 send time 是什么？是不是我直接把 message it 跟 send time 放到里边就可以了？OK，这没问题吧？如果是这样的话，我就直接然后 else 的情况下就是不OK，对不对？我没有收到这个 ACK 是失败的，可能返回的是false，那这里边我暂且做一次，比如说 wonder 或者是 error 的一个告警就可以了，是不是？我说 is not is confirm message，对吧？这是错误的时候，我都这么去记录一下，这是不是没有问题？好，这里边我暂且这个逻辑是这样去写，后面我们再去完善。

```java
package com.bfxy.rabbit.producer.broker;

import com.bfxy.rabbit.api.Message;
import com.bfxy.rabbit.api.MessageType;
import com.bfxy.rabbit.api.exception.MessageRuntimeException;
import com.google.common.base.Preconditions;
import com.google.common.base.Splitter;
import com.google.common.collect.Maps;
import lombok.extern.slf4j.Slf4j;
import org.springframework.amqp.rabbit.connection.ConnectionFactory;
import org.springframework.amqp.rabbit.connection.CorrelationData;
import org.springframework.amqp.rabbit.core.RabbitTemplate;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.retry.support.RetryTemplate;
import org.springframework.stereotype.Component;

import java.util.List;
import java.util.Map;
import java.util.Spliterator;

/**
 * <h1>池化 RabbitTemplate 封装</h1>
 */
@Slf4j
@Component
public class RabbitTemplateContainer implements RabbitTemplate.ConfirmCallback {

    private Map<String /* Topic */, RabbitTemplate>  rabbitMap = Maps.newConcurrentMap();

    private Splitter splitter = Splitter.on("#");

    @Autowired
    private ConnectionFactory connectionFactory;

    public RabbitTemplate getTemplate(Message message) throws MessageRuntimeException {
        Preconditions.checkNotNull(message);
        String topic = message.getTopic();

        RabbitTemplate rabbitTemplate = rabbitMap.get(topic);

        if (rabbitTemplate != null) {
            return rabbitTemplate;
        }
        log.info("#RabbitTemplateContainer.getTemplate# topic {} is not exists ");

        RabbitTemplate  newRabbitTemplate = new RabbitTemplate(connectionFactory);
        newRabbitTemplate.setExchange(topic);
        newRabbitTemplate.setRoutingKey(message.getRoutingKey());
        newRabbitTemplate.setRetryTemplate(new RetryTemplate());

        // Rabbi的序列化方式
//        newRabbitTemplate.setMessageConverter(messageConvertror);

        String messageType = message.getMessageType();
        if (!MessageType.RAPID.equals(messageType)) {
            /**
             * 只要不是迅速发送消息，那么久加上回调函数（RabbitTemplate.ConfirmCallback）-- 因为RabbitTemplateContainer实现了
             * RabbitTemplate.ConfirmCallback 所以直接返回 this 即可
             */
            newRabbitTemplate.setConfirmCallback(this);
        }
        rabbitMap.putIfAbsent(topic, newRabbitTemplate);
        return rabbitMap.get(topic);

    }


    /**
     * ConfirmCallback 回调
     * @param correlationData
     * @param ack
     * @param cause
     */
    @Override
    public void confirm(CorrelationData correlationData, boolean ack, String cause) {
        // 具体的应答消息
        List<String> strings = splitter.splitToList(correlationData.getId());
        String messageId = strings.get(0);
        long sendTime = Long.parseLong(strings.get(1));
        if (ack) {
            log.info("send message is OK, confirm messageId: {}, sendTime{}", messageId, sendTime);
        } else {
            log.error("send message is OK, confirm messageId: {}, sendTime{}", messageId, sendTime);
        }
    }
}
```

这样的话其实老师就已经把石化的 rabbit template 已经跟大家写完了，这里边我说叫做石化 rabbit temple late 红歌。好，搞定了这个 Rabbit template 的石化封装以后，我们再回过头来改一改这个代码是不是就可以了？之前我们直接注入进来的是一个单例的这种模板，现在可不是了。现在我们用的什么？我们用的是 Rabbit template 什么container，只是我们用它了。好，把它拿过来，我们稍作修改 auto where 的就变成 Rabbit tempted container 了，注意在这里就换人了，换成 rap 的 template container，下面你就不能直接 convert send 了，你应该怎么去做？很简单，稍微改一改就是就他先做什么事情，先直接 get template 的方法，把 message 直接扔进来，返回一个什么呀？有的话直接返回已经存在的 rapid template，没有的话它会帮你创建一个，然后再返回 Rabbit 他们这肯定是有的，然后用 Rabbit 他们接收一下，然后再调好，但是这块它会在 get 的时候它会抛一个异常，我们来看一看是不是这样的。

[image](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/864d4678-4b32-41a7-a2cc-dc6e24efa813/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466U4BP5GLP%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T225301Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDgm0Bzv9ymEOQIsL2BQtHlKXbKrjFfGmEeh6Xy9P1c%2BgIhAM7S4FRKhuRytU71s3k01ARh5ojnt5U4SawPDcRO2bBwKogECMb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgyVL92%2B6E4ElUxFUXMq3AOKo%2BDoMraNHnua4E8m6qpXneC9QBTLj8L12OCeU1o%2BFVdE5oBm4kCOHm8kVXmRXeIqZPFkEYdxMEib%2Fi16ksoBM8LADKH2nlYPfKyu1NvHeR6njsYMEIuQZp57hJ2txLuZyL89hl2bfr6aHs7hObXaDoFjQSMpWXlItmKTi7kjWzAMMLPPzdwaiZ1w4kcD2ipb8tVwxFdxzVW6eAfYOmo%2FJDxe87CwFmFW%2BDVMQvMEqJxpREgOexaYRZCO4EvOTJtNMrkX74hptVrk0gl6IQIoS98NtmZXLBAu3aID6teOZCF5v1%2FMZl4iykPWrLFK8YBnw0L5VZdFzD3Szst3LYjKO2fsG9f4EX6WoKaKbou9YGbb5Wl4G3k84FzqY3S%2Bfc9m%2FRCYqnlp3xBcrfptQGDRNYt4WQuU7gYwjXBn%2FaUk73CDHCvhjYRq4VIZXwi407hR7Uy3%2BSQH4aSv9pUV8llDRu3lpWNjs5LvPwpOBmnnGQOrWrqp8BYKy0s7WcdsxwHSzstU96CdXxltN6X9frt2g8V%2BEtBESiMnYT9GowbjWdP0Mgm8tun0MTERgGdyVTg5yFjRpNYHNT5KjBK3OVsQnPQBnjzIJgzbDCWzSpsbzI0JrG04KFyPVI90%2FzD8uf%2FSBjqkAWldmX%2FSOjiYkKWpGz8KJI8eQHajTd3251yiGyBNo2RYHZbFf04vJ4AtKR99UZeppdjnphJ8A1L3culERLRjcPNySbZgCXkS5CoqbddH3zE7t2YUuDtO9zu%2FRscyLb7l%2FIahdjL5USw5uk5NhrhYW0M2cFZP6wH%2BLd%2B5bYu8wk5Uxh6aBrsFqvXwU2X0qnexDCKGIdfeEhGrxZnJ5cOYaINZTpvb&X-Amz-Signature=6e3766b9bbbf768e2644e7967ff3b9ddb846827f4186a653a16b896bee7a67f9&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

你看到它往出抛一个 message exception，那我们是不是可以稍作修改，因为这里边你要做 try catch，因为我们之前我记得有一个有 run time 运行时异常，肯定我就不需要突破了，你看这样的话，只要他抛 runtime exception，那在这里边他就没必要说再往出再做锤 ash 了。做运行时的异常，那不存在的时候，反正他也会帮我去 new 出来一个，除非说你 message 就写出一个空，他直接报那个 no point excess，这没问题。


好了，那这一块呢？我们来看，基本上我们整体代码对于池化这块就已经跟大家讲完了，那我们来整体回顾一下。首先我们从最上层 Rabbit API 来说，它里边就这么几个属性，这个message，一个 message ID，一个topic，还有一个 routing key，还有它的参数以及delay，包括我们的这个 message type OK，默认是 config 来想的，然后提供了几个构造方法，这个大家都没问题对不对？然后 message builder，它专门是为了什么呀？创建 message 去做的，然后 message listen，这是消费端的事情，我们不需要管好。比较核心的就是 message producer，它里面有 3 个发消息的方法，有一个带 call back 的，还有一个没有 call back，还有一个是批量发送，然后根据这个 message producer 所衍生出来的一个具体的实现，咱们叫做 producer client。


producer client 它怎么去做？它实现 message producer，然后重写这 3 个方法，后面两个我现在都没有实现，我现在只实现了其中一个方法的一点，说白了我只是实现了迅速发消息，那其实针对于不同的发送消息的方式，那我还应该做一层抽象，就是我们的 Rabbit broker。


Rabbit Brooke 就是做一个抽象四种方式，一个是迅速发，确认发，可靠性的发，还有一个是批量的发message，然后它具体的实现类就是我们刚才看到的叫做 Rabbit broker implements，然后回过头来具体的这个 producer client 他发送的时候他要根据 master type 去判断，就是每一种方式我应该具体怎么样去发，然后实现类把它注入进来以后我们来看他最开始的时候就是用一个普通的 Rabbit template 去发的，并没有做池化操作。然后迅速发消息，直接设置一下类型，然后调 Santa 像的客人，方法是用一个异步的线程池去包装的，然后去把一些什么唯一的ID， calculation date 以及 topic routing key，然后去做一个这个设置，最后调用 ragged template convert。


后来我们这节课讲的就是做一个池化，池化的好处有两点，哪两点在这里我们来说一说。第一点就是每一个 topic 对应一个template，这样的好处是提高发送的这个效率，就是你单个 provider 跟多个 provider 发肯定是不一样的，就是性能会更好。


第二一个就是说不同的 topic 对应一个，这么说我应该这样去写，第一点就是提高发送效率，第二点是可以根据不同的需求制定化不同的 template 模板，就是这两点，就比如说你想发事物的topic，是不是你后面扩展的时候也很简单，你这个 message 如果是带事物的，你可以再封装一种这个 message 类型说事物的，然后你去判断是不是你根据 message type 判断。


这里边其实我们来看一看，这里边有一个metastry，就是说你在做 return 消息的时候也可以去做，在这哈叫做 send channel transacted，我在这里生成true。什么意思？就是说这种 template 它是支持这个事物，也可以这么去做。当然其实实际的生产中一般都不会去选择事物小型，因为它的这个性能太慢了。


好了，然后还有一点最关键的就是说每一种 routine key 它都是不一样，就是说每一个 topic 它所对应的 routine key 这个路由规则它都是不一样的。我举个简单的例子，在这里其实这块很重要。假设说我们这一块，你说老师我就想用 react template，好，我们直接把它注入进来。比如说那我问你，他在设置 Routine key 的时候，比如说这个 routine key，比如说叫做 Rabbit 点星号，对吧？那也就是说他发送的消息发送完了之后，它能匹配的是所有 Rabbit 点星号或者 rap 点井号。以这个 rabbit 点前缀的后面，比如说我改了改成 spring 点型号，这时候你就是每次发的时候你自己都要对这个这个东西重新做一个设置，就是这个路由的规则重新做一个设置，而这个很麻烦。


所以说我们倒不如把每一个 topic 都做成它对应的一个template，这样的话这是非常好的，所以说这是迟缓的一个原因，就是刚才老师说的，在这里根据不同的需求制定化不同的revenue，他们比如每一个 topic 都有自己的 routine 规则。


好了，那到此为止，我们关于这个 Rabbit template container，关于这个迟话已经讲完了。那下节课我们干什么？下节课我们来看一看这个对于这个什么序列化这块，我们应该怎么去做，我们现在还没有去做任何序列化的事情。后面我们来看一看这个序列化，序列化的作用是什么？为了提高我们的性能。OK，这节课我们就先讲到这，谢谢小伙伴们收看。




