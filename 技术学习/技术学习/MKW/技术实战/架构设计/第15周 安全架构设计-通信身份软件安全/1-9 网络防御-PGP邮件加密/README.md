---
title: 1-9 网络防御-PGP邮件加密
---

# 1-9 网络防御-PGP邮件加密

架起需求到落地的桥梁，构建 it 新蓝图。我是张飞扬。

[image](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/f359a82e-e770-47d4-b245-df613d20f0b6/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VG7XTQUS%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T231032Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCICk3z0R5jIm6slnItjaYrfZgRDbLu8BvC5C%2BMD6fsLZCAiA9TN%2B8so5JMrOL74OYpOkyW%2BboN%2BmlgN9Y3CS1A9pfqyqIBAjG%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMxqUqXU7jg9iS1V2EKtwDtTCItrMUy5QJ%2FgqsmQdM%2F1K9Ldrc%2Be9JIVTKn4CNTD%2BfsD6DEVLHpT5Q5hivHiAQ1L3m8XPYOvPUbBMnAH8EmVHJvxtCWznh%2FZeRp1q%2F%2F1E2yqV2tGv6%2FA3c5VLwKOvifYKOjGZqel998AlGFUcYsVJxVkKo5pC3hnH8RiVK5yPNzQsE5j39ikR5ui0iiHSqbiuW4hJTnWbHq25aAfxgOitD7b8e76W9f3TbiGMcSlMpITTHUn2cV30UzVS7qKu%2BDm6TmuTHcNtkxlCd9Uuj6X22Rz3D6UNyQcjYUhzK1HnY9eJHusp5YtvE8PYzAAetLJDkH%2BEoSksBPyZbQAuGprKHCOop4vATsnc%2FWDAvBhMhVe4tuGnTQIUxCSOHRlGneU8Vyeq%2BKGQXidJV4V2Yr%2F8YS57h%2B%2Fn%2BVTKtFW89CuvYhpyRE90uoKVi7kfFCIOkioMcWH3J7zYIktpAGV%2BuEHq%2B6Vppje6YFudbSC1lZ7vogbNbioBi%2FP9tuJtbGh6L8t%2B19%2Fpp%2B05fgsggP%2FrYFxqI%2BnPs2%2B2xMJIizjSgQzcr%2BVIttbuJ0tgWr%2FinM8TQDaY44qfICQ6OERiYvDDpcs8PsLM%2FSzVGmBxGV%2FtWRseYfpTeMSKEj7%2BoGVAwnbf%2F0gY6pgEeVIbDQfuKiYr5mgdOc2LS%2F%2Ff72uT%2FPOdIH8cxPBRa74mqhSuZn9Y%2BNvBTtYJqr8p7hI3C1CIWWOjRw8sLjbYeKZNH%2FagQskMr2Hy%2BqTRlG1jCMsdCcHbdABegumVQmkARIoOnvibXMKZKlpQRTS4gTXMcdKPvbMJDX3hrCt0SfJ2wqQldPE6UPLHKoARI7HIq%2Fsnx%2Bkhl7NvsWxaBPabaVfhDjqb1&X-Amz-Signature=139d6068206e5ca2a9e9d77a37f32b4688f07c2c8099d2f41eac03b08e6bdb81&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

好，上一节我们聊了聊VPN，也聊了聊其中比较复杂的 IPC VPN，它的 2* 2 两种不同的模式，两种不同的实现。那这一节我们看另外一个话题，如何实现邮件的加密。那首先我想讲一下，其实邮件加密有很多种不同的方法，一个比较传统的方法就是 mine 多渠道、多用途的互联网邮件扩展，其中有个扩展叫安全扩展。那通过安全扩展也可以实现邮件的签名、加密、传输等等功能，但是整个流程相对复杂，没有那么精妙，所以逐步已经被淘汰了。


那当前最流行的安全邮件加密，比如说 CEO 和CTO、 CFO 之间传输，很有可能就是传输中传输的这种完全加密非常安全的邮件。这个邮件叫做PGP，光看名称就非常酷炫，英文叫做 pretty good privacy，非常非常棒的一种。


什么私密的安全加密，是不是光名字就取得很好？其实它的算法也非常精妙。好，阜阳老师就用一张图来跟大家聊一聊如何实现邮件的加密，以及在接收端应该如何来解密这个邮件呢。嗯，这张图英文很多，没有关系，

[image](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/910da9b8-4cd2-44d1-a89c-95b224919a04/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VG7XTQUS%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T231032Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCICk3z0R5jIm6slnItjaYrfZgRDbLu8BvC5C%2BMD6fsLZCAiA9TN%2B8so5JMrOL74OYpOkyW%2BboN%2BmlgN9Y3CS1A9pfqyqIBAjG%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMxqUqXU7jg9iS1V2EKtwDtTCItrMUy5QJ%2FgqsmQdM%2F1K9Ldrc%2Be9JIVTKn4CNTD%2BfsD6DEVLHpT5Q5hivHiAQ1L3m8XPYOvPUbBMnAH8EmVHJvxtCWznh%2FZeRp1q%2F%2F1E2yqV2tGv6%2FA3c5VLwKOvifYKOjGZqel998AlGFUcYsVJxVkKo5pC3hnH8RiVK5yPNzQsE5j39ikR5ui0iiHSqbiuW4hJTnWbHq25aAfxgOitD7b8e76W9f3TbiGMcSlMpITTHUn2cV30UzVS7qKu%2BDm6TmuTHcNtkxlCd9Uuj6X22Rz3D6UNyQcjYUhzK1HnY9eJHusp5YtvE8PYzAAetLJDkH%2BEoSksBPyZbQAuGprKHCOop4vATsnc%2FWDAvBhMhVe4tuGnTQIUxCSOHRlGneU8Vyeq%2BKGQXidJV4V2Yr%2F8YS57h%2B%2Fn%2BVTKtFW89CuvYhpyRE90uoKVi7kfFCIOkioMcWH3J7zYIktpAGV%2BuEHq%2B6Vppje6YFudbSC1lZ7vogbNbioBi%2FP9tuJtbGh6L8t%2B19%2Fpp%2B05fgsggP%2FrYFxqI%2BnPs2%2B2xMJIizjSgQzcr%2BVIttbuJ0tgWr%2FinM8TQDaY44qfICQ6OERiYvDDpcs8PsLM%2FSzVGmBxGV%2FtWRseYfpTeMSKEj7%2BoGVAwnbf%2F0gY6pgEeVIbDQfuKiYr5mgdOc2LS%2F%2Ff72uT%2FPOdIH8cxPBRa74mqhSuZn9Y%2BNvBTtYJqr8p7hI3C1CIWWOjRw8sLjbYeKZNH%2FagQskMr2Hy%2BqTRlG1jCMsdCcHbdABegumVQmkARIoOnvibXMKZKlpQRTS4gTXMcdKPvbMJDX3hrCt0SfJ2wqQldPE6UPLHKoARI7HIq%2Fsnx%2Bkhl7NvsWxaBPabaVfhDjqb1&X-Amz-Signature=d42b26b8e64dd3e5ca011e96b1c70b5e59e54b10070320d574668ec58947ec28&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

大家回顾一下之前我们在数据安全里面学的很多算法，我们在这里会逐一用到。好，阜阳老师依然是拿出一支笔，从左往右跟大家比比划，划好，先从左边的邮件开始，这是一个什么？ a 要发给 b 的邮件，好，那先对这个邮件采用哈希算法生成一个摘要，这个摘要要么？然后采用一个什么 a 独有的私钥进行签名，签名完的内容是不是就在这里啊？这个签名过程其实就是拿 a 的私钥对这个摘要进行加密，加密完了我们就认为这是一个签名喽，把签名放在邮件的前面，形成一个。


什么？形成一个签名完成以后的内容，那如果你把这个内容发给 b 会怎么样呢？会证明只有 a 才能够什么签处这样的签名，所以这个内容的发送者很清楚是a，而且不难抵赖，这就是签名的用处。但是整个邮件发送过程当中是不是这个绿颜色内容是明文的？这样是不是就违背了安全性的要求啊？安全性最关键，什么机密性？你不光是要不能抵赖，要验证是 a 发的，而且你只有让 b 才能接受吧。任何其他人在中间进行一个网络侦测，网络抓包就能够看到你的邮件。那你公司大事、国家政务还能够发送吗？当然不行。那怎么办呢？那也很简单嘛，把整个内容给加密，对吧？包含你的签名头和你的邮件身体都给加密了。那怎么加密呢？能不能用公私钥机制进行加密？哎，回忆一下付杨老师强调的什么呀？只要超过一个千个字节以上的内容，千万不要用公司要加密机制，因为太慢了，太花内存、太花CPU、太花时间了。我们邮件经常是什么？打几个字，然后贴一个附件，这个附件可能几k、几兆，甚至于几 g 都就可以。


所以这种 Email 是不能够采用什么非对称加密的，我们必须用对称密钥，所以这里面很关键，就是采用一个临时的对称密钥，然后进行快速加密。对称密钥的加密时间可能是非对称密钥的 1/ 101%，甚至于千分之一二。好，加密完了以后，我们就把这个内容发给了，发给 b 了，然后 b 收到这个文件就一头雾水，为什么？因为 b 没有这个对称密钥，对吧？对称密钥是什么？是两者之间的默契，但你 PDP 加密，你跟对方可没有什么默契，你只是一个邮件发送者，对方是个邮件接收者，你们之间没有默契，所以他没法解你的密钥。


那怎么办呢？那很简单，我把钥匙跟信封都给你不就可以了吗？对不对？所以要把钥匙加在信封上面，通常是先发钥匙再发信封里面的内容，这样呢，就可以让对端解密了。那这又出一个安全隐患了，你把钥匙放在信封上面，人人不是都拿到钥匙，每个人都可以解开你的内容，那怎么办呢？好，我把钥匙做一个处理，我把钥匙本身给加密了。用谁的密钥加密啊？用接收者的公钥加密。那这个时候这个内容不长，这个内容可能就几百个字节，那把这个钥匙，几百个字节钥匙进行加密是不是也是很快的过程？但是我用的是 b 的公钥，也就意味着谁能解密，只有 b 才能解开这个钥匙。好，当这个钥匙跟这封信一起发给对端的时候，假设黑客截到了，他一看头上有一段密钥，这段密钥是一个乱码，我怎么样解密呢？我得拿一个私钥解密，但我没有 b 的私钥。好，我解不开密钥。然后后面的明文也是一堆乱码，因为我是拿这个密钥进行加密的明文黑客什么一筹莫展？没有任何办法，但是如果 b 拿到 b 会怎么做？ b 会把前面的那部分字节的内容先截取出来，然后拿自己的私钥解密。解开了以后他就知道什么这个对称密钥什么内容了，然后很方便他就拿这个对称密钥再进行一次加密，所谓的再加密也就是解密，所以对称算法很简单，再加密也就相当于解密，然后很快就把什么签名跟邮件的铭文都拿到了，然后读一读。嗯，整个公司出现了重大变故，即将被分拆。


好，我赶紧抛股票，对吧？就看到明文了，然后再验证一下到底是 CEO 发给我的还是什么，还是假的人发给我了，一看这个文章的签名怎么验证呢？我把这个文章的签名用a，对吧？就是 CEO 的公钥进行解密，解出一个哈希的内容，然后我再用标准的哈希对什么邮件正文进行哈希计算，两个哈希一比较，嗯，这两个 DI 杰斯的摘要完全一致，证明什么确实是 CEO 发给我的，那我是 CTO 或者是我是CFO，我确认 CEO 通知我了。
什么呀？公司即将分拆，那我该做什么？我赶紧抛售股票，对吧？就这样一封邮件在CEO、 CTO 或CEO、 CFO 之间传输，只有这几个 o 才能够打开。同时整个加解密过程全是用对称密钥进行明文加解密，非常快。另外什么我可以保证确实是 CEO 发给我的这个签名是确实是有效的。所以 PGP 算法很漂亮的一个算法，它既实现了密钥的传输，又实现了快速加解密，另外又能验证发送者，同时也只能有指定的接收者才能够解开这封密钥，才能够解开这封邮件。


是不是很酷炫的一个算法？如果大家在听这个过程当中还有不懂，嗯，证明前面数据安全章节课没有学扎实哦。回过去重新温故而知新吧。如果已经非常懂了，也许我们可以用 Java 代码，用什么 spring boot 小程序来自我实现一次 PDP 的加密跟 PDP 的解密。那这个时候你就不用去收费的去买一个 PGP 软件了，可以很方便的自己实现邮件的安全传输。


好，聊完了 PGP 大法，我们下一节呢会聊一聊另外一个更加有用，更加知名的安全加密传输。什么HTTPS，我们看一看 HTTPS 是怎么样在网络的？ 5 层、 6 层、 7 层实现握手，实现通信，实现密钥的交换，以及数据的端到端的安全传输的，大家敬请期待。

