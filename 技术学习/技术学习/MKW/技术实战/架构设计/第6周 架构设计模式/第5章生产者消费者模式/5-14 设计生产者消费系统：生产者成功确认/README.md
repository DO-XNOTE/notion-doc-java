---
title: 5-14 设计生产者消费系统：生产者成功确认
---

# 5-14 设计生产者消费系统：生产者成功确认

数据单元第一步以后，下面就是我们的一个重头戏了，就是我们的生产者如何设计一个合格的生产者，这是非常有挑战性的。顾名思义，生产者的核心职责就是生产数据单元，它当然是会做数据单元打转的，那这里其实它是两层含义的，对于生产者来说，它所谓的生产就是根据当时的系统创作出新的数据单元之后，将生产的数据单元放入到容器当中去。一般来说这个生产数据单元是没有什么特别复杂的逻辑的，但是在发送或者是将数据单元放到容器的时候，这个就有很多种不同的做法，而且也是很有挑战性。其实发送数据本身它并不会很复杂，复杂的是如何确保你已经发送成功了，或者你要不要注册成功？我这里大概就简单的总结了一下，大概你可以概括什么？这以下几种做法。


首先当然它的核心是对发送或者生成这个成功的一个确认，

[image](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/9bbf93e5-158e-40f0-8868-b1fcc4de96ab/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466Y7TTZIDY%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T230621Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIFxvSQ9Wu1tH1%2B73%2B%2BBu5bZuH5HAX2TnrMDNwTBT8UpZAiAaUG3mC9Vx3h2mv8MCuaTuu7DRabC35A19KqQBlgDB2SqIBAjG%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMycm08WprmS6EvvRhKtwDBRDvMib3vXSeTI12QhihqguKsRSvwDMQ%2Ba1B0d%2B8Y3nZVuuIshtAS7Aslpwrac81WL0DY6LeqHGJl5yxEBg0vpkSDrYQYa%2BzDiFLMIaNAXbpHZ3g0YQaT6%2BzoiLQHIm53rjTaSqTfSJlFMVIdo1eRDX2G32nc7aGxbnhbuN4ZbIQh1HKM3qXHxnLvOajgLGaO1G77ovgLvXTEjPT2eT%2FcIG8iDuX7pcD%2B7PqeZ5fww8Jiy9h3Dd6nAo7Skcucjp0Sd%2BcvkJnvUMc%2B0KlTpy5YxOI3fTMayUq3wQyLbxpiZovgWMz%2BDvEpw4DTxLKf76BwW7%2F1A1W5i%2B1%2BrDlBCoNyEMSMiVzu8opoe0vqQbgC0m8kxyNX0mBhGPhkFJmrR47%2FhFrCSUJZ2JVNe5Y5d4jc4B2MPhElfYQ9BY8oBPhBZFC7R3DF0HWFed7PygGzGTLVPZVgC2iP84qNInkrGQSO5lQufhy5r8HiHy%2Fau27cKC1qA1a3hup2rpVAiPQDDnpcx6NG1KlL5iKSUTuO6ROepc15GYdQvn9yx7Yv8gRO812JE9m7iMNch7kPhSRaF%2B7V76P4TQ9eK24uqemtao26mMMy0XAVfK7%2BXkurMPBQeZxoDKQy68Mo5bd8v4wnrr%2F0gY6pgFdj9HvbqSEaSmUo9PkvOWNv2dXV2RVSutOwIZ4DmrH8DLYUJl0xIUyHOTJuWKyhJYSdhIMQZK4ufCAgMZDxdk5jrk%2BrVNKPq7ka%2FfhdP7tKn4io6b9wsola4w2XCmlPZRHGpyOv%2B7Ox4a8y56GG3ClhzMX1K5sGWvgxQdB9Z9D8R0QCrPjfPDypVnhTgnZT6RNayRggVAd%2FlTbUCqE5Mndu5mPRKCV&X-Amz-Signature=64638ffb9c23bd4fa2d9809f55597e3c28ca0b626c12d04c1eb0bc6f38a0856f&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

这就是我们的一个重点。你举个简单的例子好了，你现在向一个人送了一个东西，你得确定说这个东西他收没收到。别人不管你是点外卖还是送的一个包裹，还是你自己发的邮件，你都得确保人家收没收到。那简单一点的讲的话，你怎么做？比如说我给我的妈妈买了一个礼物，然后我送去了，那同时我可能会打个电话确认一下，都会按照不同的线路和渠道来确定这件事。那做得怎么样？他完成下来，完成还是没有完成？这就是一种要发送成功的确认。


就所以说你一般都会有一种跟你发送这个动作的传输的本身不太一样的一些圈，我大概总结了一下就 30 模式，一种叫始断终弃，这个名字是不是一种渣男的感觉？大家不要想那么多，这个话用学术语来讲对 fire and i forget 这是什么意思？我只管发送，发送完了之后好了 thats all。我根本就不用去等你确认说我发送已经成功还是没有成功， i dont care 是不是就是最初的时候。哎呦，我很执着，我一定把这个东西发出去，但发完之后就好了，我再也不管你有没有给我告诉我消息说发送成功了没有，我也不会主动的问你发送成功了没有，就是说 bug and forget 这个动作就有点像。


是什么呀？你给你的家人送了一份礼物，送完就好了，不管了，有点像 UDP 这种消息一样，反正我就丢嘛，我反正丢出去就好了，丢成功没有？不关心不是我的重点，而这是一种模式，作为production，它要对这个发送成功的这个确认，这件事情上面就它根本不需要确认，这是一种。


第二种，望穿秋水，英文讲一下 synchelanus send 这是什么意思？我一直在等待望穿秋水，看着你什么时候来到底。哎，这个感觉有没有很好体会的？一个非常痴情的人对不对？马上引用渣男变暖男。你想啊，发送就一封信给自己心爱的女子，这个女孩子啥时候给我回信？我不知道，我一直等着这个女生给我回信，她就是不给我回信，这怎么办？所以我望穿秋水，就是没有信，这个信一来我就很开心，信不来，我就一直等待，一直等待。


这个在学术语上就是一种同步的这样一个句确认，什么意思？它是一种有点像被 block 的这种感觉，就我发出去一个消息之后，我一定要等到这个确认不来，我有两种办法就一直等下去，这是一种二，就是我不停的该过一段时间，比如说我过 2 秒钟我再发一次， 2 秒不行，我等 4 秒钟再发， 4 秒不行我等 8 秒再发。就一直这样发，但是时间可能会拉长，有的可能是匀速的，有的是不匀速的，它可能会推迟这个时间，因为各种原因设计，反正都是可取的。


有点相应，他不仅在那里串，一直等他响应你追那个女孩子，给他写一封情书，他不理你，你就写他个 100 封，你一定要等着他一封回信，哪怕是写作一个。呸，就这个感觉，这是望穿秋实的感觉，大家记住啊。所以说在你设计一个 producer 这个方式的时候，你就得想想你到底是要选哪一种，就跟你说，你要做一个什么样的阴阳。每次追一个女孩子，给他发一封信，这封情书写出去之后，送出去了，回不回你不关心，那就始难终止，我一定要等到你给我。哎，你不给我，我就一直给你发这件事。


忘川秋实 synchronized send，有点像被 broke up 一直在揣的这种感觉。最后一种把它叫云中随记锦书来用学术语讲什么 unsynchronized send，就是说我给你发了，好，我还是会等你，但是我不会被block，就是我不会一直等你，就相当于说我今天给我喜欢到的女孩子写了一封情书，写出去之后我就干别的去了，我该读书，我可以刷剧歌刷机，我该玩游戏。
他什么时候回我信，不是不关心，只是我不会一直就傻傻的就在这里等着他，我该干嘛的还干嘛别的，这是一种方式，但是最终你能不能等到这个人的回信，其实你是不知道的，但是你一直还是在想云中龙随即锦书了，这个人到底啥时候给我回？会不会不回？其实这个事情场景下不回也不耽误你啥事儿，说难听点，你就没有那么喜欢那个女生，但是你也有一点点意思，她回你那是最好，她不回吗？你就那么回事，那这种场景就看你怎么选了。


所以说在这个地方就是这三种模式对这个发送成功的确认，你自己要想一想你到底选哪一种方式？这个对你整个系统，不光是说对你这个production，其实对整个系统都有一定的影响的。你想想你如果说发完就不管它 fire and forget，那这个事情就有可能说其实发生根本就没成功，但你也不知道，因为你根本就没去确认这事发生过没有，你包裹可能丢了，包裹丢了它怎么办？没了也不知道，忘传秋实一直等你就导致下一条消息什么时候发，完全不知道，整个系统这个速度 superput 都被降下来了，所以这种是很 heavy 的，怎么说？就是整个很重的这个模式。


最后一种我给你发了，但是这个成功的确认迟迟等不到，但是我也不管，我会发下一条，但是我会一直等你，等你最好了。就是异步的这样一个方式，所以这三种不同的模式，你在给一个系统设计 potential 的这个方式的时候，你必须得选一种的，自己要想好选哪一种。


