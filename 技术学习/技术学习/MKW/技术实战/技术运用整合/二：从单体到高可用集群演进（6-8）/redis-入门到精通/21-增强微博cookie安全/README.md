---
title: 21-增强微博cookie安全
---

# 21-增强微博cookie安全

[image](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/e3ae4016-17f0-4da6-b100-b4267a4125de/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TQPA3SFK%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T225057Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIHjwFzuWc4bFKcfkkAJscZEVkTp4p6Jzctg4x37I%2BoVrAiEA%2BGh4vPXU8YEb7dDGnfPWzPKJfLm8v%2BthRtZEys7VKLAqiAQIxv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDK4glQx4FMe%2BrrIDFSrcAxLrqU338sGal%2FL9CROM7UEUdcVQGAkVqVTm%2B%2F9UlurZsgNsCb2x5RklkYuLypYVqztJRja9IBE%2BGHJPytT4S%2BFKz4ByihNLa0m6i1TVSvHfy3CoaHksQgzRzjllH%2FKBT%2BDZraM0zgWKyaF%2F%2Fr%2FETXLiXrkINxGqAvj%2F8tobOsY%2FzIeJdt%2FNoskaJWJR5zBLJ15v%2FoHnLlLl%2FOU9wMz1YDeiKa3HHBTRY1tv9n%2BNX6JBzCkQpQGEk2HN9VltXB%2FBh5b2MTEoLFCUHVVGqitQkIj6EXDxC2qVF0tFXGDuIoKQfFrikFVYwdV0Q750YwfVJGHxjVtAlC4esEnci6CvI8z02X3s0mD313VhXEQRzMw5dhBjgTjUFAcwWGlvhzTzZOz%2FdA%2FfjtF0ZKE6aATn%2FKp%2Beb1U%2Fsaq2mgd2aKnrtVbOitwGM6DZBWDaB0aPDCbqOQQoFy%2BuWBADdoThUqD3N9lqc3UlB9kCyZCCNhZGyuDVnJteCyf7Mjk%2By5uOego9Fbi2grSN8y18WIzPSEO3QxsNtorf9DvmffOnVyJ81aSe7Wr%2BYtyfiYRiCnE1AtKPBHbLaOrHcWtYoSsZKmL6NLkdxHin7kNcK1KV28X%2Buj550S1l1ZSHQw5UFHOML%2B7%2F9IGOqUByoU6pS%2BMIn4swEmqpcPIuuqzJ4VtWVk7JScabDWRMa6CetbX8DZXbCoHv0xAR%2Bz39jgBEX%2FAz%2FiktUnMm4OAjBxjMe6G0DKs1EfgLTQGJTZqy01bSaBS9XNwAQrVcdwMnlK%2BDQx0xdwNDjuPgDruyTz3uLaFfaPBUs6tiGG9nU3mGzdtBoBobOgvphz6ydjpTOZ5%2Fj0HBlS150eCdR2061GidEAf&X-Amz-Signature=5023505b23ee6391def13a1af08160f5dfe383457f04f8246689e4104765548a&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

[image](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/4686433c-270b-48bf-8c56-68534fb64c44/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TQPA3SFK%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T225057Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIHjwFzuWc4bFKcfkkAJscZEVkTp4p6Jzctg4x37I%2BoVrAiEA%2BGh4vPXU8YEb7dDGnfPWzPKJfLm8v%2BthRtZEys7VKLAqiAQIxv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDK4glQx4FMe%2BrrIDFSrcAxLrqU338sGal%2FL9CROM7UEUdcVQGAkVqVTm%2B%2F9UlurZsgNsCb2x5RklkYuLypYVqztJRja9IBE%2BGHJPytT4S%2BFKz4ByihNLa0m6i1TVSvHfy3CoaHksQgzRzjllH%2FKBT%2BDZraM0zgWKyaF%2F%2Fr%2FETXLiXrkINxGqAvj%2F8tobOsY%2FzIeJdt%2FNoskaJWJR5zBLJ15v%2FoHnLlLl%2FOU9wMz1YDeiKa3HHBTRY1tv9n%2BNX6JBzCkQpQGEk2HN9VltXB%2FBh5b2MTEoLFCUHVVGqitQkIj6EXDxC2qVF0tFXGDuIoKQfFrikFVYwdV0Q750YwfVJGHxjVtAlC4esEnci6CvI8z02X3s0mD313VhXEQRzMw5dhBjgTjUFAcwWGlvhzTzZOz%2FdA%2FfjtF0ZKE6aATn%2FKp%2Beb1U%2Fsaq2mgd2aKnrtVbOitwGM6DZBWDaB0aPDCbqOQQoFy%2BuWBADdoThUqD3N9lqc3UlB9kCyZCCNhZGyuDVnJteCyf7Mjk%2By5uOego9Fbi2grSN8y18WIzPSEO3QxsNtorf9DvmffOnVyJ81aSe7Wr%2BYtyfiYRiCnE1AtKPBHbLaOrHcWtYoSsZKmL6NLkdxHin7kNcK1KV28X%2Buj550S1l1ZSHQw5UFHOML%2B7%2F9IGOqUByoU6pS%2BMIn4swEmqpcPIuuqzJ4VtWVk7JScabDWRMa6CetbX8DZXbCoHv0xAR%2Bz39jgBEX%2FAz%2FiktUnMm4OAjBxjMe6G0DKs1EfgLTQGJTZqy01bSaBS9XNwAQrVcdwMnlK%2BDQx0xdwNDjuPgDruyTz3uLaFfaPBUs6tiGG9nU3mGzdtBoBobOgvphz6ydjpTOZ5%2Fj0HBlS150eCdR2061GidEAf&X-Amz-Signature=6f39ae2f5ffbc58a059de85e3b3056ab608eee19f2c5e461598a4b0ca0ae41f3&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

[image](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/e58083a7-e8e6-42ee-bdfc-d018007e01f2/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TQPA3SFK%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T225057Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIHjwFzuWc4bFKcfkkAJscZEVkTp4p6Jzctg4x37I%2BoVrAiEA%2BGh4vPXU8YEb7dDGnfPWzPKJfLm8v%2BthRtZEys7VKLAqiAQIxv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDK4glQx4FMe%2BrrIDFSrcAxLrqU338sGal%2FL9CROM7UEUdcVQGAkVqVTm%2B%2F9UlurZsgNsCb2x5RklkYuLypYVqztJRja9IBE%2BGHJPytT4S%2BFKz4ByihNLa0m6i1TVSvHfy3CoaHksQgzRzjllH%2FKBT%2BDZraM0zgWKyaF%2F%2Fr%2FETXLiXrkINxGqAvj%2F8tobOsY%2FzIeJdt%2FNoskaJWJR5zBLJ15v%2FoHnLlLl%2FOU9wMz1YDeiKa3HHBTRY1tv9n%2BNX6JBzCkQpQGEk2HN9VltXB%2FBh5b2MTEoLFCUHVVGqitQkIj6EXDxC2qVF0tFXGDuIoKQfFrikFVYwdV0Q750YwfVJGHxjVtAlC4esEnci6CvI8z02X3s0mD313VhXEQRzMw5dhBjgTjUFAcwWGlvhzTzZOz%2FdA%2FfjtF0ZKE6aATn%2FKp%2Beb1U%2Fsaq2mgd2aKnrtVbOitwGM6DZBWDaB0aPDCbqOQQoFy%2BuWBADdoThUqD3N9lqc3UlB9kCyZCCNhZGyuDVnJteCyf7Mjk%2By5uOego9Fbi2grSN8y18WIzPSEO3QxsNtorf9DvmffOnVyJ81aSe7Wr%2BYtyfiYRiCnE1AtKPBHbLaOrHcWtYoSsZKmL6NLkdxHin7kNcK1KV28X%2Buj550S1l1ZSHQw5UFHOML%2B7%2F9IGOqUByoU6pS%2BMIn4swEmqpcPIuuqzJ4VtWVk7JScabDWRMa6CetbX8DZXbCoHv0xAR%2Bz39jgBEX%2FAz%2FiktUnMm4OAjBxjMe6G0DKs1EfgLTQGJTZqy01bSaBS9XNwAQrVcdwMnlK%2BDQx0xdwNDjuPgDruyTz3uLaFfaPBUs6tiGG9nU3mGzdtBoBobOgvphz6ydjpTOZ5%2Fj0HBlS150eCdR2061GidEAf&X-Amz-Signature=9f55eafe3a21455acc726c036e41a786832478be4efe9f81a5c90656e9a38dca&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

好，先来看一下这个上次的做的仿微博的项目，这个项目咱已经把它基本完成了，如下功能，就是注册登录，然后关注取消关注，发微博的时候能让你的粉丝看到。那么这样说来一个微博的这个demo，一个模型，我们就把它完成了。但是嗯，还存在着一些问题，我们先来看小问题，咱先把最小的问题先给它解决掉啊。第一个小问题就是你登录了之后，你点这个首页的话，他还是直接给你体现一个登录注册这个界面，应该判断你有没有登录，如果要是登录了，就给你转到个人主页去，这样才合理一些。嗯，这个是小问题，咱们加一个判断就可以了啊。其次我们打开 F12 来看一看就知道问题出在哪啊。我们打开这个resource，我们看看这个 user ID， username 这个东西。如果我们把它改一改的话。


这个是cookie，很容易就把它修改了。
后，在这个 Chrome 里还做了一些防范，没有让我们改，不允许我们改，那么我们用那个火壶。


用 test 一 111111 log in，好，登录进来之后我们看看这个cookie，这个 cookie 是特别的容易改的。我们之前学过 ATDP 协议，我们知道用 ATDP 协议想来修改它。你看这个，我给它改成一。这个改成一。嗯，或者改成 3 tag 这个地方给它改成 test 2 title 2 啊。然后我们再点到这个热点去看一看的话。好，那我们现在再点到自己的这个人主页来，主页 home 点PIP，那他就问 TEST 2 有什么感想？也就是说我已经变了一个身份了，这是第二个存在的这个问题。就是我们用 cookie 之前我们也说过这个问题，当时我们说学 cookie session 的时候，我们谈到过一个 cookie 容易被篡改，我们需要给它加电，需要给它加点盐，叫 cookie salt，对吧？现在这个问题就真的发生了，很容易就被篡改了，所以同学们思考一下，我们怎么来预防它？手段很多，我们找一个比较简单一点的，容易实现的来预防就可以了。


同学们先考虑一下，这是第二个问题，第三个问题就比较难一点喽，就比较复杂一点了。就是牵涉到微博的这个数据，这个模型的这个问题。在我们第一版的这个微博的这个设计中，我们是这样来设计的，当我发布了一个微博的时候。


CD user local ITD PITD OCSCD 微博 CIM post，我们在发布一个微博的时候，我们都干了些什么？大家来看一看，尤其是注意这个 for 一起循环。我们是这样一个操作，就是你发布一个微博，就把这个微博推给你的所有的粉丝。大家想一想，如果你像那个姚晨这样的，还有那个什么李开复这样的人，还有任志强，人家都有好几百万、上千万个粉丝，这样的话，这一帮人他要发一个微博，那你的这个 Redis 服务器里面就迅速的增加了 1, 000 万条微博，同样的微博，而这 1, 000 万条微博内容还几乎都一样，内容还都一样。


所以这就牵涉到你关注的人发了个微博，或者说某个人发了微博和他的粉丝之间这个信息如何来到达他的这个粉丝这里，到底是主动的推给他的粉丝，还是这个由他的粉丝主动去获取？我们来到这个微博网站上啊。我们来看一看。其实在这个微博早期的这个设计里面，它其实就是用了这个推模型。这样的话就出现了一个问题，就是刚才咱们所说的，当你这个人过多的时候，一个人的粉丝过多的时候，将会产生一些障碍啊。你这个发一个东西一下推给 100 万个人， 1, 000 万个人，那这个数据库受不了，做了很多无用功啊。


所以后来微博改成了这个游推，改成拉，改成往回拉，怎么样？往回拉就是你这个用户一登录，你把自己关注的那些人，他们的最新信息给他拽过来。所以你在这个微博里面，你可能去见谁就关注见一个人，就你就点个关注，你试一试。嗯，之前这个微博的一篇文章介绍说他们设计的是上限是 2, 000，也就是说你顶多能关注 2, 000 个人，这样的话就算你去这个拉这个数据，也无非是循环 2, 000 次，也无非循环 2, 000 次。所以，嗯，这个就这个要是改动的话，改动就比较大了，我们直接把它的这个架构模型给它改了，所以我们先在第一版里面，嗯，把刚才咱们所说的那两个小问题先给它解决掉，然后我们再做一个再更换它的模型还连不上，这是什么情况？王胜连上了吗？连了，连上了那个 100 连上了啊。你是不是100？你看他被人悄悄地给改了。没问题，你先坐张德志旁边，先看着，下课再说。第一节课下课再说。


好，第一个小问题咱们要解决的就是判断他这个登录之后自动给他跳到个人主页去，跳到 home 去，这也好办，就是判断一下而已。好，那我们在这个地方给它 copy 这几行过来。然后我们来到首页去啊。你带个点pip，来到首页。
好，我们给它粘过来，粘上这么几哈。


好，这个如果要是不等于false，那也就意味着登录了。登录的话我给它 location 到home，点 PIP 去，好，然后保存退出啊。那我们来刷新一下 undefined is login。好，没关系，我们少引入了一个它的库文念好再来 include 当前目录下的 lab 点PAP。


好，再次保存退出，然后我们来刷新一下，好了，那现在我们点它的这个主页，它也会自动给我们回到这个人主页，而不是系统主页啊。那如果当我们退出之后就来到这个主页了，就是 index 了系统主页了啊。好，第一个小问题我们很容易给它解决掉，再来解决第二个小问题。第二个问题在哪呢？嗯，就是我们刚才已经通过这个火狐来给大家做了一个演示，就是我们把这个 cookie 只要一给它改一改，哎，立马自己的身份就变了。为什么可以做到这样呢？这是因为 cookie 的原理决定的。 cookie 的原理是因为由客户端在那个 IDP 协议的头信息里面带过去的服务器再来解析你客户端带过来的这个数据，所以你带过来数据是什么？你就，你说你是谁，服务器就认为你是谁，他没有一个校验机制。我们之前也讲过这个，讲过这方面的内容，有人说需要再给他额外加一个字段来预防这个事儿，防止这种情况的发生。我们说叫 cookie 要加点儿盐，加个salt。所以现在我们如何就是说在改动最小的这个基础上来完成它，改动最小的基础上来完成它啊。
就是说让别人想伪造用户ID，因为用户 ID 在这个热点区域都能推测出来的，一看它叫 test 就知道它叫 test yeah， test profile， test 一， test 一，而且也能也能推测出来，这个人的也能想办法推测出来。你看这个鼠标往那一放，左下角就看出 f 等于一，也就是说 u r d 等于2，也就是说很容易就能得到一个人的用户名和一个人的用户ID，这样就能很容易带来这个 cookie 的仿造啊。


这时候我们想一个办法，其实很容易，我们给它加一个字段，让它不好仿、不好猜不就行了吗？最直观的办法，我们给他这个登录的时候，除了分配它的 cookie 里面的 user ID 和 user name 之外，我再给它分配一个随机数，再分配一个随机数，这个随机数我每次到这个 Redis 里面我查一下，看看是否匹配，那样一登录它要一退出，退出了那这个随机数就给它消除掉啊。


所以别人能猜到你的这个用户ID，能猜到你用户name， user name，但是这个随机数不好猜，因为就是因为随机的，你下次一登录也换了这个数也已经换了，所以在登陆的时候我们要给它略施改造，我们要给它改造一下，给他改造改造。是登录 login 点 pip 来看看这里怎么来给它改造。


就在这个地方设置了 cookie 之后还不够，我还要再多给它设置一个cookie。多给他设置一个cookie，比如说就叫 secret also sacred，给它来一个加密。嗯，那么我们为了便于操作，我们写一个产生随机数的这样的一个函数来点PIP。


好，我们给他来一个，比如说十六个这个位的这个长度，来个随机字符串，这样。最简单的办法就是给他打乱。
好勒，然后我们把它打乱好，打乱了之后我们截取，截取，截取 16 个，那就够了啊。


好勒，我们写好一个这样的随机字符串的这个函数，然后我们来到这个 login 里面。那我就需要先生成一个这个author， secret 等于那个叫做 run 的secret。这个函数生成了之后，我把它写到这个author，写到这个 cookie 里面去。


author secret？大家想一想，我光往 cookie 里面写行不行？够不够呢？那肯定不够，那用户随便给你带一个 16 位的乱七八糟字符串过去了，你说这个字符串是真的还是假的呀？你不得验证吗啊？所以我们还得把这个字符串再次放在哪里，想一想。我们还得再次把它放在哪里啊？我们把它放在服务器 Redis 里面，所以我们这样来操作set。嗯，根据我们上节课所讲的那个规律，先是 user 表，然后冒号 user ID，然后再冒号，然后是到那 user 冒号， user ID 冒号，然后点 user ID， user ID。嗯，是的，好， user ID，然后再点冒号， author secret。


那你看现在是个什么效果呢？就是你登录的时候，我给你设置了一个随机的这个码，放在了 Redis 里面啊。放在 Redis 里，同时在你的 cookie 里也给你设置了，你看这样的话，当我们既然写了这一步，这就意味着我们检验这个用户登没登录的时候，光检验用户名密码，光检验用户名是不行了，还得判断一个什么东西，还得判断一个什么东西呢？还得判断那个 is login 里面还得再多判断一个东西，就是你 cookie 里面有没有 also secret，就算有还得和 Redis 服务器里面的匹配才行。是这样的，得这样才可以，所以这个 is login 就要复杂一点了，就得这么着来啊。好，来到 42 行之后还不够，还得再做判断啊。


说如果cookie，看看里面有没有那个 author secret 要是没有直接 return false，直接 return pose 要是有就一定是真的了吗？也未必有，也未必就意味着是真的。然后我们在查询他一下 global 到了r，然后我们用 dollar r get 一下， get 一下， get 谁啊？刚才我们写的那个键是 user 表下面的 user ID 冒号，然后点cookie。


user ID，然后再点冒号 Otter secret，我们把它取出来称为author。这个 author 必须和 cookie 里面的那个 author secret 一致才可以，所以还得再做一个判断，如果这个 auto secret 要是不等于 cookie 里面的 author secret 也直接 return false 也不行。好，就是这样的一个效果。来，那我们现在把它加上更改了这个 login 之后，我们到这个其他几个页面去看一看，其他几个页面受到了一些干扰啊。什么干扰呢？就是你在那个 login 里面，在这个地方就已经调用谁了，就已经调用那个刀了饵了。但你此处你看有没有 dollar r？此处没有 dollar r，就也就是那个 Redis 的连接， Redis 的那个对象没有，所以我们这几个地方页面还都得相对的改一改，就是把那个 do 拉尔的连接还得往上提一提。如果你要是感觉这样改动有点大呢。我们想一个稍微简单一点的办法，比如说你看在post。


在这里判断的登录 is login 判断登录，在判断登录的时候就已经用到了这个dollar，这就意味着这个 dollar 应该提到最前面去，提到前面去，这样的话我们几个页面都得改，你要是不想改动这么大，我们也可以在这里写一个局部的哆啦 r CONN Redis，他自己局部内维护着一个dollar，也就是 Redis 的这个连接，这样就省得我们改其他的影响的页面。


对，就一个静态的，也就是说仅仅是多一次函数调用而已，那个对象并没有变多。嗯，好，那我们把它引过来，好保存起来。唉，现在我们，我再来点这个人的这个，比如说点这个热点，热点一下子把我给我转向到 index 点 PIP 去了。为什么转到 index 点 PIP 了呢？我看看我的 cookie 丢没丢，我的 cookie 根本没变，但是他却认为我没登录，这是为什么呢？这是为什么呢？就是因为我们已经启用了最新的这个判断标准，就是因为我们在那个 cookie 里面应该还得校验一个 author secret 才行，所以我重新登录一下，看看这次登录之后有没有什么变化。


那这次同学们看多了一个 auto secret 之后，那我就应该这个我已经登上了才对，我已经登录上了才对，我点热点还是给我退到首页去了，这就说明我们这个判断的这个时候我们看一看 VIM home 点PIP，后面点PIP，我们看看发生了什么啊？我刚才点 home 点 PIP 还有点热点的时候都是用的 is login 等于false。好，那我去检验一下叶子 login 到底是怎么回事，我们看看有可能是在哪出的问题，来，咱们调试一下。哎，这个地方出了问题， get user 冒号 user ID，然后 cookie 下面的 cookie 下面的 user ID 没问题，再然后是author，冒号 author secret。


取出来判断它俩不相等， the return false。好，那我们。在这个地方 PRINT 杠 2 Dollar author secret 看看到底怎么回事，然后在普任特杠尔我打印一下 dollar cookie，我再看看怎么回事，怎么这么奇怪，然后我退出，到底看出了什么症状啊？我再一次点热脸来看一看 user ID。


那这个 cookie 里面有这个 also right secret 没有问题。 cookie 里面是没有问题的，那肯定有问题就出现在 Redis 服务器了， Redis 服务器有问题了，服务器里面没有存我们想要的东西，所以我们再次来到 log in，我们看看怎么给我处理的。
set user 冒号 user ID author secret 光设了一个键，还没有给他把纸给他填上，果然很奇怪。 secret 来保存，再次保存好了，再次的来登录一遍，拜拜灯登录上来，这一次我们看到有这个 author secret，同时我也登录成功了，登录成功，然后，嗯，来到热点去看一看，没有问题。


这次我多了一个这个 auto secret，如果这一次我想仿别人，你看我现在我是 TEST 2，然后我想仿别人，比如说我想仿那个编辑，我要仿 test 一好，我给他改了他的 user ID，我也知道，我也能看见，我也给他改了，这两个都没有问题，然后我一点热点还是给我退出来了。
为什么退出来了？因为那个 also secret 你仿不出来，所以我们很容易就通过一个小小的手段，嗯，给他来一个加密的字符串。其实 cookie 你要是用 cookie 的话，光存他的那个用户名和ID，那肯定是不行的。那相当于是完全没有对用户没有一点的屏障，别人爱怎么改，别人仿冒成管理员你都不知道。所以必须要给它加一些加密手段。


好，那么这是咱们把这个，嗯，微博项目又给他做了一点点的改进了。哪两点呢？来说一下。首先是那个首页如果登录了自动跳转过来，其次是那个登录的安全性的问题，登录安全性的问题，话说回来，还有一处还得改。你想一想，你登录进来的时候设置了一个 also secret，那个关那个密码。然后判断的时候也用密码判断，当你登出的时候，登退出的时候，想一想，退出的时候不仅要消除cookie，还得消除什么呢？你防止别人把你这个，你要这个密码老不变的话也没有意义了，是不是还得把那个用户，它存在 Redis 服务器里面的那个 author secret key 也得给它清除掉，对吧？也得给它清除，因此我们这样来操作，当前 label 点 PAP 在 set cookie author secretary 列为- 1 之后，还不够海底刀了。 r 等于 c o n Redis，然后到了r，我们要销毁一个键，或者说把它的键值变为空也行啊。那我们就这样来做， set user 冒号 dollar user ID，再然后 dollar 多少呢？好，我们来读一下。


dollar cookie， dollar user ID 等于 cookie 下面的 user ID，先把它保存起来啊。此处 user i d 点，然后冒号在 author secrets 给它设成多少，我就给它设成空就行了。 user ID 好在这里少了个冒号，退出的时候不仅要消除cookie，还要消除 ready 服务器里面存储的那个加密码，这样才算完成好再保存再退出啊。然后我们现在看这个 cookie 是有 auto secret，然后我退出之后 author secret。
在这里变成空值，并且复议消失，好分好把它的 cookie 就都给消除掉，同时把 Redis 服务器里面的那个加密的 k 也给它去掉，这样的话，嗯，这个从登录注册到发微博关注，那么这个第一版的这个 demo 我们就给它完成了啊。


好，那么接下来我们再来改正，再来继续迭代它的功能，就是之前所说的这个地方，这个 11 分钟，这是个死的，用户名字也是个死的，这个要给他改，再一个功能改动，嗯的，工作量也不算太大啊。然后最关键的还在于第三步，就是要把这个微博发布的这个推模型给它改成拉模型，这一步是比较重要的一个改变。

