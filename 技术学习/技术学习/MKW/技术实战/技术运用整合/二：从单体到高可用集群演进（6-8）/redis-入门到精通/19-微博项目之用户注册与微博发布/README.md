---
title: 19-微博项目之用户注册与微博发布
---

# 19-微博项目之用户注册与微博发布

[image](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/dc85e987-b74a-4eb8-8a64-1fb6d593569e/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZD6QXTDQ%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T225055Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCJVMH%2F7A9SR2jxCSkXKmPhOFJHsbcJyQPKqtGlev8BIAIhAIxLYMwAJFVBQ%2BiGolUPMMFsorPD2jLIdNmyAlR3YQduKogECMb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1Igw91L0u%2F2yws2ubxH8q3APJz9a8x6UPl1Qj3WwTsB0%2Brfe6FhLwzdcctrdXJTWzjcOqi2NwhV8hu9BJMpGVprwTPPb2qhdj9qbIT1gdlUVKpA52r8WrxaHEU7oZaLJpvPFMRQgrJc0MOkZyquEh6vmr7rSGMjyzJu11HwrTjeY0rEzQ%2FeVoiAAoBeFHb5b9ON1HsiTY8Axr8787qABZ%2FsVYF6lQtL%2Fgd6LtOARxhvB3LfWghpwyopeGxcnrqHtgVvt4cAwn2CClxJLq%2BiWbqY4x3D%2BlDgZBn9ak02uOR2pQJnCBdLCUIxaQBPo3aB%2FPM8ssF0yRkpS8wpbSLmTZJTX6xTjIkyNIViA9XN7Z4VsHRTYTc7Alss264ZY0mKesO9dAjlcHyy1%2BPBk8l1t6NTTgU6%2FvQyOn0kafbxn8TRRJlBaunzIX0pdWjnXxU1zaEU4YaRnbz5FMFCc4apJPZe3oAOAtaa3WPDsRpaQ6vXMuftYuu3WEe%2BMSKLNgrn1wT94eU4ixl3Jrtl3DTQMksW6WPMyHQ0A4a5wXUAamYB0Fx9X5I5HgRlGECan4qpNHhcb8z5JPyVWJfWJFosCEAq%2B9wnYyPpkpvnhTkTM1JtB4S%2FVNG6tcClMLv0M8X7G%2FQN7S1sf8qVcTHcFAyDDwuv%2FSBjqkAQUjUfrbQ1wb5vVXk71x4Wdczm4wJB6KDKN19iLpyTJHnOzxwcImuoyX2jI%2BUyjFkWuyhZBh5Tb2eM0%2BGTnmBtfOivHnQizTrnUHVkKvqZGNwV9ftjnhqCTYJKZS9mAQ6DtHYOneSCagAvQg%2F%2FM9KX%2BN7yHgq%2FUC4D91%2FyWVf1A2OSo%2BmlPJ7SuSYJ26Mjgx5lM63HliDrQNrW4oFvkKKnKbb0UZ&X-Amz-Signature=458460f65722b5292bc297c2cef5bd4461cf547c02a1203b73bff536e03f861a&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

[image](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/4ca11f9f-30e2-46fc-852d-f26e68b7e450/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZD6QXTDQ%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T225055Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCJVMH%2F7A9SR2jxCSkXKmPhOFJHsbcJyQPKqtGlev8BIAIhAIxLYMwAJFVBQ%2BiGolUPMMFsorPD2jLIdNmyAlR3YQduKogECMb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1Igw91L0u%2F2yws2ubxH8q3APJz9a8x6UPl1Qj3WwTsB0%2Brfe6FhLwzdcctrdXJTWzjcOqi2NwhV8hu9BJMpGVprwTPPb2qhdj9qbIT1gdlUVKpA52r8WrxaHEU7oZaLJpvPFMRQgrJc0MOkZyquEh6vmr7rSGMjyzJu11HwrTjeY0rEzQ%2FeVoiAAoBeFHb5b9ON1HsiTY8Axr8787qABZ%2FsVYF6lQtL%2Fgd6LtOARxhvB3LfWghpwyopeGxcnrqHtgVvt4cAwn2CClxJLq%2BiWbqY4x3D%2BlDgZBn9ak02uOR2pQJnCBdLCUIxaQBPo3aB%2FPM8ssF0yRkpS8wpbSLmTZJTX6xTjIkyNIViA9XN7Z4VsHRTYTc7Alss264ZY0mKesO9dAjlcHyy1%2BPBk8l1t6NTTgU6%2FvQyOn0kafbxn8TRRJlBaunzIX0pdWjnXxU1zaEU4YaRnbz5FMFCc4apJPZe3oAOAtaa3WPDsRpaQ6vXMuftYuu3WEe%2BMSKLNgrn1wT94eU4ixl3Jrtl3DTQMksW6WPMyHQ0A4a5wXUAamYB0Fx9X5I5HgRlGECan4qpNHhcb8z5JPyVWJfWJFosCEAq%2B9wnYyPpkpvnhTkTM1JtB4S%2FVNG6tcClMLv0M8X7G%2FQN7S1sf8qVcTHcFAyDDwuv%2FSBjqkAQUjUfrbQ1wb5vVXk71x4Wdczm4wJB6KDKN19iLpyTJHnOzxwcImuoyX2jI%2BUyjFkWuyhZBh5Tb2eM0%2BGTnmBtfOivHnQizTrnUHVkKvqZGNwV9ftjnhqCTYJKZS9mAQ6DtHYOneSCagAvQg%2F%2FM9KX%2BN7yHgq%2FUC4D91%2FyWVf1A2OSo%2BmlPJ7SuSYJ26Mjgx5lM63HliDrQNrW4oFvkKKnKbb0UZ&X-Amz-Signature=aaa45c17dc71d94554e2c6e7c644f75de7f7a7f3d4faa96e23bd8b8229828e44&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

接下来我们就做一个实战的这个项目，用这个 Redis 来完成一个仿微博的这样的一个功能。好，那么我们，嗯，先把这个模板，刚才已经给大家发了这个模板啊。我们来看一看它的这个首页，首页是注册，然后和登录，嗯，然后是登录了之后他的个人主页可以发微博，然后有他几个粉丝、几个关注也能列出来。好，这是来到某个某一个人的主页上去，某一个人的主页上还有这个热点，统计出最新的用户和最新的 50 条微博。


我们用传统的关系型数据库，我们的重点在于设计那个表结构上，现在我们换成了这个 Redis 来做它，那重点就在于设计它的这个 k 上， k 如果设计的合理，实际来就高效，还容易理解啊。关于 k 的设计原理，那刚才已经给大家做了一个讲解，那么接下来我们就实际的操练一下啊。


好，我先把这个微博点 VIP 给他传上。唉，这样啊，给他传到这个服务器上去。PS， FTP open fruit 好， CD 到 user local 下面， ITD PD 下面。嗯， ITD OCS 下面好了啊。然后这个路径是在哪里啊？看一看桌面，是。这个路径是在哪？


桌面， palm chart c 好勒。然后我们来到 c users Y18 Desktop 好了。 l c d c users Y18 Desktop 好了，然后我把这个 Web 微博点 VIP 破了上去。好了，现在已经传过去了，那我们来到这个远程来看一看。好，我们来到远程看一眼啊。嗯， iOS 一下多了一个微博点VIP。好，那我 on zip 一下微博，点zip。好， iOS CD 到这个微博下面去。


iOS 我们依然是从最简单的做起，我们不断迭代这个网站，我们不断用最简单的迭代法来开发它啊。那我们观察这个 index 点 TML 这个页面呢？这个页面有一些部分是相同的，就是顶部和尾部那一块是相同的，我们看看从哪开始DRVID，我们从这一块给它切出来，一直切到哪呢？切到这个尾部这一块目的是什么呢？目的是因为所有的页面就是顶部和这儿这都是一样的啊。我们直接给他弄两个这个点 PAP 给它包含进来就可以了，就没必要各块都写一下重复的内容了啊。因此因此我来这个。 VIM 一下 VIM 一个这个叫header，点PIP。然后我读进来index，点 TML 读进来，读进来之后我们把它的哪一块看一看？好，从这开始，从 12 行开始往下我们都给它删掉，好保存起来啊。


这是头部已经洗好了，然后复特点PAP，同样是 index 点TML，那从这个复特开始往上的部分都给它切掉好，保存好了，福特也写好了，然后我们把这个 index 点TML，我们给它重命一下名字，重命一下名字，给它命成 index 点pap，然后编辑它啊。我要给它删到第12、第 11 行i，因为我已经把它放在头部了嘛。


3 到头 11 行之后，自然我这个地方就得给他来一个这个 PAP include 那个当前目录下的 header 点PAP，对吧啊？至此，任何复杂的逻辑都没有，仅仅就是一个包含啊。同理，我从这个 div 附这我开始删了之后，同理，我这里 include 进来那个尾部 footer 第二 pip 好了，虽然我们做的东西还很简单，那起码也是一个进步啊。来稳顿一下199，然后微博 index 点PIP，好，没有问题，那么接下来我们这个要注册一个用户，我们要注册一个用户啊。我们就先完成这个注册功能，然后我们来看一看发送给了谁，把这个 pose 数据发送给了谁？来我们看一看它的发送给了 regist 点PIP，那么这个软件的 PAP 将要干什么？我们如果是用 MySQL 的话，我们都已经很熟练了，把它数据一接，形成一行数据，往那个 user 表里面一塞insert，这不就 OK 了吗？同理，现在我们呢不往 MySQL 里面写，我们只是往 Redis 里面写而已，仅此而已啊。


那么这个 Redis 的 key 怎么设计？根据我刚才所说的，我们这个 VIM read me，咱也来一个 read me，大写专业一些。 read me。我们先是这个设计 user 表，然后转换成我们这样来设计设计 u 的表。我对应的这个k，对应的这个 k 规则，也就是说我们毕竟使数据库使的多了，现在猛的一转到 K Y 6，我们可以先理解成这个 KV 这个关系型数据库，然后再往这个上面按照它的转换规则来转。


根据刚才我们所说的那个规则，如果注册一个用户的话，我们应该注册一个用户，假应该是注册用户，那应该是这样一个规则 SET 一，首先是那个最前缀，是表明，对吧？表明一过是它的那个主键的值，如果说你这个表里面有很多个除了组件之外，还有那个像 user name 和 Email 也是经常查的，如果你要想更严谨一些，当然这样 k 也将更长一些。


你可以这么来写 user ID，冒号一，冒号一，然后一一用户一，他的这个什么呢？嗯，他的这个 username 是张三。这样打眼一看就知道 user 表下面的这个 user name 列哪一行。 user ID 等于一的那个 user name 列其实是张三同理，我们只需要 set user 冒号 user ID，然后一，然后一，然后他的password，他的 password password，然后 111111 SET，然后是好，就要这两个就够了，就够了。粗略的看要这两行就够了。


但是你在看这个登录的时候，你看他传的是什么啊？登录的时候看看他传的是什么？传的是一个用户名，对吧？用户名那就意味着他将要到这个 Redis 里面去查找这个用户名，但问题是这个问题恰好我们上节课就已经分析过，你看你要想查用户名怎么查？难道你要遍历所有的k，查谁的值等于张三吗？这显然是不够合理的，这就意味着我们还需在 user 表里面，我们还往往还用那个 user name 来查询，所以这个时候我们要来一个冗余，那 user 表下面 user name 等于谁？等于张三，张三的什么？张三的 user ID 值是一直是一，这样的话你传过来，张三，我只需要按照这个，你传的是张三用户名，那我只需要按照这个表列名或者叫索引名，索引名，然后它之，然后要查的字段有的 ID 等于一啊。


如果我压根把它一拼接，唉，根本就没有这个k，那不用再说了，没有你这个用户，没这个用户，所以我们注册用户大致已经分析清楚了，其实就是要写这么三个 set 而已，仅此而已。这就完事了。我们用这个最简单的这个迭代法来开发它，我们先分析一个最小、最微型的功能，一个单元功能我们就把它实现，我就把它实现。所以此处我们 VIM 那个一个 register Jess sir，是这样的吗？怎么这么别扭？ re Jester，好，没有问题，就这样了，就这样的。


好勒。那该分析的东西我们分析完毕了，那具体的步骤那就是接收，这就和这个什么呢？这就和一一一输入法，这就和这个用 MySQL 注册已经殊途而同归了，已经回归到具体步骤，那就是第零步是接收 poster 参数，是吧？接收过来之后还得判断一下合法性，比如说那个用户名你是不是没钱，或者是两次的 password 是不一致，所以我们要给他判断一下啊。


判断这个。稍等，我看看能不能把这个颜色调得更清晰一些啊。好判断参数，判断这个用户名密码是否完整啊。那要是不完整，那就直接给他一个提示就退出了。那如果完整，而如果完整好办，那就是我们要连接Redis，然后干什么呢？查询该用户名，判断是否存在，如果也不存在，那也好办啊。要存在了，那只能是抱歉了，这个用户名已经被占了啊。


好，如果不存在，那好了，我们写入数据库应该叫写入Redis，把用户名和密码写入Redis，注册成功了，然后再给他完成登录操作，再完成登录操作，这就 OK 了。好，我们把它保存起来，这个思路已经有了。好， iOS 一下啊。那么具体的来说，具体的步骤我们只是分析出了 4 个步骤，还得具体的代码怎么来实现啊？我们还得要不断的去接它的参数判断等等，我们于是再来制造一个叫做基础库，比如说我们再来制造一个这个label，点PAP，我们知道一个基础库里边我们用来放一些常用的函数，这个基础函数库我们就放在这做一个简单的封装啊。然后，嗯，先封装一个获取 poster 值的，因为老写那个 POS 怪麻烦的啊。这样啊。方科生 p 方科生p。 dollar key dollar key 就直接 return 到了 post 到了k。


因为其实这个地方这样来封装还是比较简略的，只不过我们此处这一个小项目重点在于完成这个 k v 6 的操作，我们不值当的为它封装特别丰富的这个底层的库，所以来两个简单的封装就可以了啊。好，那我们再次回到 VIM register，点 PIP 里面去，回到这来。


好，回到这来之后我们的下一步操作就是接收 pose 的参数了啊。接收 pose 的参数啊。好，那我们接，我们要接哪两个表单？来，我们打开看一下，我们要接 user name、 password 和password。好勒，我们做一个判断，如果那个 p pass user name 它要是不真，或者那个 p 传来的 pass word 也非真，要是再或者那个 p 传来的这个 password two 对针，这时候怎么办啊？那我们就给他提醒一下这个地方，我来一个收message，收message，或者叫收error，再封装一个error。那你把错误原因写出来，请输入完整信息啊。完整信息，起码请输入完整注册信息，那我们还得封装一个 error 函数才行，这个 error 函数我们一会再封装，现在先写这个。


这三个都齐了之后，我们还得再判断，就是那个，此处我老是用函数调用，不大舒服，是吧？建议这么找，建议这么找 dollar username 等于p，因为下边我们还要用这几个变量，你再调用就显得笨拙了。 dollar pass word 等于p。然后是 pass word，再然后是 dollar pass WORD 2 等于 p pass WORD 2 好了，完毕。然后我们把这三个变量都给他得到了，都给他得到，这个地方要稍微改一改了，这个地方给它改成。


嗯， i 好了，这个地方改成感叹号 dollar user name 到了， part word。到了，趴到窝点吐好了，完毕改过来了，然后先判断他的注册信息是否完整，如果注册信息完整了，那我们还得判断他的密码是否一致。判断他的密码是否一致啊。


判断密码是否一致啊。好了， if 到了 pass word 要是不等于 dollar pass word to 有问题，然后我们也给他error，这个请输入一致的密码，是吧？请输入一致的密码。或者说两次密码不一样就口语化一点。那如果两次密码也一样的话，好了，那就进入这个注册环节了。注册环节等等还不等，还得连接Redis，查询该用户名是否存在。


这回就得连 Redis 喽，连 Redis 好，连 Redis 我们一个要 new 那个 Redis 的那个类对象，上午我们刚刚做过演示。好，那我们。假设有一个线程的函数叫到了r，等于这个。叫 c o n red CON Redis c o n Redis。简单一点，那一会这个 CON 和 Redis 还有这个 error 都得我们在写好连接上来之后，我们让这个哆尔就要做工作了。还不能做工作，还得这是连接Redis，然后是查询用户名是否已被注册，就这样的，怎么查给我用户名了？那好办，我们知道根据用户名来查是它的k，规则是这样的，它的 k 规则是这样的，是 u 的表。 username 列具体的 user name 的值，那你既然查的时候这样查，注意你一会写的时候也得这样写才行啊。然后我们要查它的邮杂 ID 存不存在。点冒号 user ID，我就要查这个 key 存不存在啊。来，我们把查到的这个结果我们给它打印出来， VR dump 出来，好保存一下。


现在我们需要我们经过一番的这个摸索，接下来我们还有两个函数得去完善它，一个是 error 函数，一个 CON Redis 来，那开始写 VIM 这个label，点PIP，然后我要写两个函数，一个是啊，一个是 error 报错函数 function error function error。艾若，给我一个艾若的这个 dollar message，它很简单，就是干什么呢？就是直接 Echo message 而已，然后并且并且退出，在此处退出的话在此处退出。那我们尾部的那个东西怎么包含进来呀？是吧？这可不妙，这可不妙，那我们尾巴那一小块的东西哪去了？


gecko，我们直接退出了，退出这样直接在此处我就给它包含一下，把尾部给它包含进来，是吧？就直接给它包含，点footer，点pip，反正他退出之后底下我们再重复包含，那也不会出错啊。莱文还有一个函数是啥呢？是那个 function 叫 CON Redis。 CON Redis。 C O N Redis 也比较的简单啊。我们申请一个 static 变量， static dollar r，比如说等于那，然后我们让这个 dollar 等于 new Redis，然后让这个 dollar 它有一个 connect 方法， connect 方法 connect 那个 local host 连上来。好， if 到了 r 不等于，那就好办了，那我们就直接 return 这个dollar。否则的话我们就让它等于 new Redis，然后 connect 过去啊。


最后再 return 到了 r 写他默认 6379 别的，那你就在第二个参数，你给他写一个 6380 就可以了，这和 MySQL 连接不是一个性质的。好，我们给它包装过来保存退出，然后再一次的回到 rejects 里面来，阿尔杰斯里面来。好，那么我们在它的顶部，然后我们给它。
include 进来那个头部拍着点 pip 好行，好在尾部在。 include 进来 a footer 点儿 PAP 走你就这样的好，保存退出，然后我们看看行不行。什么查询？噢噢噢，我们这不是查询了吗？查询他有没有注册，是不是我现在还不需要往里注，真正注册，我现在就是看看查询好不好使啊。我先不填，然后 call to undefined 方声p。好，这个有点离谱。 p 函数拿去了拉一波，这方科生 p 拉一波点PIP，哎，拉一波我们包含进来了吗？这个尽管有意思，首先最基础的你就得包含这个 lab 才行。include，然后这个当前目录下的这个 lab 点 PIP 来保存起来。
好，保存起来，讨论起来之后，我们再一次刷新它说请输入完整注册信息，挺好使啊。好，然后我再输入111111，然后123456，我再说的不一致，两次密码不一样也行，也能提示啊。然后我再1111111111，他将会给我查询这个用户是布尔值false，那就好，那就是没有这个用户，没有这个用户，所以我们继续来给他做这个业务逻辑，这个 error 有点太简陋了。


div div，咱们先来一个包装一下啊。好，我们继续来看，我们现在是来到了哪一步了呢？已经查询用户名是否被注册了，所以这个查询到之后我们做一个判断。好，如果那要是为真的话，如果要是为真，嗯，就不用再说其他的了啊。你这个用户名已经被注册，因此我们只需要 error 用户名已被注册，用户名已备注册，请更换。好了，好，那如果说能来到 43 行，那就说明你采取的这个用户名也是可用的。
来，具体怎么，既然是可用的，那我们就把他的用户名、密码都写到数据库里，然后还要把他的用户名反映射到 user ID 上，你看这个是 user ID 映射张用户名，这个是用户名映射这个 user ID。刚才为什么这么多？刚才已经解释过了，但是等等，我们知道在那个 MySQL 中，在 MySQL 中 user ID 我们往往都是让它 auto increment 就是自增长，对吧？所以我们不必关心它的值，但是在此处它的 user ID 的值应该是多少呢？这是一个事儿，是吧？它值应该等于多少？
查询用户总量单设一个UID。


但是这个用户要删电话，也不要老给黑屏上。
好，这个还是这个思路，我们需要转一转，来这地方，我们再来一个就是生成user，或者叫 user ID，生成 user ID 生成我们可以不断的 in 刻一个键叫做global，然后 user ID 那第一次英科的时候是不是就是一，第二次再调用英科的时候，它不就是 2 吗？这样的话它不就相当于得到一个自增型的东西了吗？是吧啊？这和，这就达到了和 MySQL 中的那个 increment 或者是那个 Oracle 中的序列 sequence 是一样的这个效果了。


所以我们来到这个 Redis 下，就用 Redis 的方言来说话，那于是我们就是要获取这个 uid 了，获取 user ID，那我们就得这么来操作， Dollar user ID 等于这个 dollar s，它不是已经 dollar r 已经连接过了吗？连接这个英克英科，谁？英科那个global，然后 user ID 就这就够了，因为他每次调用肯定得到的是不同的值。


好了，那现在 user ID 也有了，这是一个 user name 也有了， part word 也有了。嗯，就是该具体的操作了啊。好，那我们就得这么来操作 dollar r，然后是set， set set 谁啊？注意，我们刚才的规则是 user 表下面的，然后是 user ID，然后是 Dollar user ID，然后再点冒号之后的是 user name，它的值是 dollar you the name，这就欧了。然后还得写那个密码，还得写他的密码，因此 pass word 这地方换成 pass word，你看在关系型数据库下，这些 user name password 其实写在一个行里的。现在来到这个 k y 6 下，它是分拆成了多个k，因此你就要写多遍。好，那注册完毕了，这已经注册完毕，等等我们还得再写一个东西啊。在写什么呢？就是 set username，然后它的具体的name，然后对应的 user ID，也就是说我们还有可能根据 user name 查 user ID，所以这样来操作啊。


再来写一个来，这是 dollar r set 赛特 user 表下面 user name 列做主键，然后值是多少？ user name 的值是点 dollar user name，然后点，然后冒号 user ID 直示到了 user ID，这就 OK 了，这个注册过程就完成了啊。好，我们保存一下。好，来，我们再一次的来操作它，1111111111。


好，我们注册注册，注册就是成功了倒是成功了，就是有点简单，连个提醒都没有啊。那没关系，我们先手工观察 case 星， kiss 星，大意，刚才的东西应该都给他去了啊。那我们可以看得到 user user name 验18，然后 user ID，然后 user ID 冒号一帕特word。我们看一看来 get user ID 冒号 1 号用户，他的 user name 轴验 18 他的password，呦呦呦呦呦呦，这就注册完毕了啊。当然了，我们好歹给人一个提示，或者是跳转到他的这个首页去啊。那么接下来，嗯，好，注意，我把它重刷一下，都给它清了，等等等等等等等等，我还得再测一下，再注册一个验18，看看它能否给我一个合理的提示。唉，正常的没有问题，注册用户完毕了。


好，接下来我们还得让他登录才行啊。来，接下来咱就完成他登录啊。登录就最简单的，我们就用 cookie 就可以了，就用 cookie toolbar 判断他有没有登录，要是没有登录就给他转到首页去，要是已经登录就给他转到 home 页去。唉，好，注意。好，我们做一个登录页面。VIM，然后 login 点 PIP log in 点PIP。老兵现 include 进来。先 include 进来那个谁莱伯点 P a p 在 include 近来还有谁没有谁了。


header 啊header，嗨点嗨点先不管 header 点 PIP 好了，包含您来登录页面，登录页面怎么来写？登录页面就是你要传一个用户名，传一个密码，传一个密码，所以他的工作很简单，无非就是拿着这个用户名把他的密码取出来。只凭用户名能直接取密码吗？取不出来，取不出来，用户名只能取出来，那个根据用户名只能取出来，刚才我们不是写过吗？ user ID，对吧？我们得转个弯，根据 u user ID 再取密码。不过虽然转一个弯我们思路还是明确的，所以我们的大的思路是这样来做登录页面，我们的步骤，来步骤就这样来操作啊。第零就是接收这个表单数据，接收到了post，然后。


判断合法性，再来这个合法性仅仅是指有没有，是否完整，应该叫完整性啊。判断完整性，判断完整性，再然后是这个根据用户名查询用户名是否存在啊。然后如果说用户名也存在，好，然后再查询密码是否匹配，如果也匹配，那好了，你登录成功，那就登录成功了，就给他设一个 cookie 不就行了吗啊？给他设一个cookie，来给大家设一个这个cookie，如果第三设置 cookie 好来操作啊。


嗯，思路接收 post 判断完整性来， dollar username 等于这个 p user name，然后 dollar pass word 到了 pass word 等于p，然后pass。握着拿过来做一个判断，如果，如果 user name， user name 或者是 pass word 好，再见。那我们就告诉他出了点问题，请输入完整啊。用户请输入完整到了 22 行， 23 行说明你输入是完整的，那接下来我们就得判断了。根据什么判断？根据 user name 判断我，因此我们要先拼接那个k，我们就得这样来操作刀了，耳等于。 Cone redis? 然后刀拉尔 get 一下 get 的这个结果，我们把它叫做 user ID，然后 get 什么？ get 什么，我们是不是应该这样来 get 它的 user 表下面username，然后它的值是 dollar user name，再然后是它的这个有的ID，我就查询他这个k，要是这个没要是这个 user ID 要是非，真要是飞针，那就坏了啊。唉，要是飞针出问题了。


好，你又出错了，说用户名不存在，要是能到 30 行的话，说明用户名是对的，那你的这个密码还得匹配我们，于是还得根据这个 user ID 再取密码，这就好办多了，我们再取那个帕斯。唉呦，帕斯沃尔已经被占据过了，是吧？已经被这个变量占过了啊。因此，那此处我们只好这个叫 pass 了。 Rio pass，真实的密码啊。真实密码干嘛用 Redis 取啊？怎么取？用 user 表下面的 user ID 列做其组件，然后是它的值，是 dollar user ID，然后再冒号我取它的pass， word 我取出来，我只需要做一个比较就可以了，就是 pass word 要是不等于到了，不等于这个 dollar real pass，那又出问题了，因此我们说这个密码不对。好，如果到此也成功了的话，那就好办了，我们就可以设置cookie，登录成功，对吧？设置cookie，登录成功。


好，设置 cookie 很简单， set cookie。设置它的username，然后只是 user name 在 set cookie，然后他的 user ID 等于 dollar user ID， dollar user ID 设置完毕了之后，我们给它转到这个个人中心去，转到这个人中心 location 冒号 home 点 pip 是这样写的， location 后面点 pip 是吧？ home 是的，加什么不用第 17 行衣服少了一个刀了啊。


好了，那么登录也完成了啊。好勒，我们现在就来登录看一下，我用 111111 来登陆好， log in home 点PAP，这说明什么情况？跑到 home 点 PIP 去了，这说明什么情况？不对，这说明登录成功了。因为我们刚才不是判断了吗？最终要是登录成功了，不就 header 到这吗？还有一个可以办法可以检验，我们打开F12，我们看看这什么呢？看看我们的这个 cookie 有没有，不就明白了吗？ user ID 等于一 user name 验18。有，有，这个 cookie 已经设置成功了啊。


然后我还得，我们还得经常判断这个用户到底登没登录，所以我们还得再来到这个 lab 点 PIP 里面，我们再给它来一个函数。好，我来一个判断用户是否登录来function，然后那个的 is login 叶子老根鹰怎么来判断呢？嗯，我们要判断两样， if 这个 dollar 一，cookie。cookie，cookie。cookie，下面 user ID 要是飞针或者 dollar cookie 还是cookies？有印象吗？ cookie 还是cookies？cookie。OK，拿不准。查一下手册， cookie 还是 cookie 丝，这地方是个 cookie 丝，那么我以为你告诉我答案了。


好，然后如果这两样有一样，我们就给他 return false，我就给他 return false。好，否则的话我们就给它 return 一个，把它的这个值给它。嗯， return 过去便于接收。可以，否则我们就 return 一个 array 速度，按 array 速度就这样。嗯，有的 ID 有的 ID 到了下划线。好，李帅，帮我查一下手册是 cookie 还是cookies？cookie。好， user ID，然后是 user name dollar cookie，然后是 user name，我把这个值给它返回过去，便于引用好保存起来。


嗯，现在我们已经有了这个 is login 这个操作了，就是能判断是否登录了啊。那我们来到哪呢？我们来到 VIM login 下面， VIM login 下面，我们这地方要给它多追加一个功能了啊。追加一个什么功能呢？你这个 login 你不能总往这请求，你是不是已经登录过了？所以我们做一个判断， a if is log in。你要是已经登录过了的话，你要是已经登录过了的话等于false，你要是已经登录过了，那我就直接给你 header 走就行了，给你 header 到这个 home 点 PIP 去location，后面点PIP，然后您退出来啊。好，这 3 句我把它复制下来，后边还要用的判断 login 判断完毕。同理，我们还得再register，其实也应该给它加一下判断，如果你都已经登录了，你还访问这个注册页面干什么呢？


直接就给它粘过来就可以了，好，保存，再回头看一下老哥一写的对不对啊？对，没问题。好，退出，走。好，现在我们来到这个首页里，来到这个首页index，点PAP。我要是再点这个注册的话，再点这个注册，应该给我转到 home 点 pip 好了，判断成功了，那现在我们的这个力量就着重放在这个 home 点 PIP 上，这个 home 点 pip 我们打开它再看一看，它大致是想要一个什么东西好？ home 店pap，我们应该做一个判断，你要是没登录的话，应该你转到首页让你登录去，你就不能无权看这个页面。因此好 VIM home 点 PIP 要先木一下了。
home 点 ITML 木乘 home 点 PAP VIM 然后 home 点 PIP 好，前 12 行，我们先给他前十几行，前 11 行我们给它删掉。前面我们自然是这个include。include， include 那个谁自然还是 header 点 PAP 还得多一个，还得再多 include 一个，他在多 include 一个谁？ include 那个基础库当前目录下的 level 点PP？当前目录下的 level 点 p i p 好包含进来，好到最底部去。唉，删掉依然是 pip include 进来那个谁啊？当前目录下的 footer 点 p i p 好了，改造完毕，我们现在来刷新一下它的home，点pip。唉，好了，有点内容了啊。这个某某某有啥感想啊？有啥感想？这个某某某得换成咱们的名字，登录者的名字是吧？登录者的名字啊。好，因此我们 VIM home 点PIP，后面点 PIP 这个地方我们要做判断。判断什么？有没有登录？要是没登录，你滚到首页登录去，所以我们此处做一个判断啊。


这个好， if dollar user 等于。然后 is log in ah its log in。要是传来的结果非真等于false，或者说等于 false 的话，等于 UU u u。这个括号似乎放的位置不太对，是吧？此处必定有诈。在这你看user，它圈起来当成一个表达式，然后外边也包一个小括号，当成总的表达式，等于好，对了，这样就对了啊。然后我们是，那就是没登录成功， error 不就可以了吗？ error 那个就是噢，不用 error 了。那你都没登成功，还说啥？直接给你转走啊？给你转走，给你嗨点儿，给你转走。 header 给你转到这个首页，让你去登录，去 location 冒号index，点PIP，然后退出保存。


那如果说能运行到下边，那就说明你登录进来了，那这个某某某不就得换成用户名吗？反正用户名呢？这个地方我们直接 PAP Echo 啥来着？ Echo dollar user 下面的 user name 这不就可以了吗啊？很easy。走，保存起来，我们刷新一下。唉，有啥感想？好了，我们又完成了一个小小的功能，接下来那就是更核心的这个功能了，就是干啥呢？发微博，发微博，这个微博又得我们设计设计喽啊。怎么来设计呢？怎么来设计这个k？关键又是设计这个 k 的功夫喽啊？设计k？


来，我们看它往哪发的，往 post 点PIP，因此我们还需要造一个 post 点 PIP 好 VIM post 点PIP。快刀乱麻。
先 include 那个 live 点PIP。 include either 点PIP。
include。


footer 点 PAP when IM read me。注册用户，刚才发生的事情，注册用户，我们发生了阴客英克谁？ global user，英科 global user ID 发生了这么多的事情，然后现在我们就是要发微博了，发微博我们只要能把这个 k 给它设计出来，那微博就容易做啊。发微博。如果说你设计 k 没头绪，那么我想问你，你设计那个用数据库来存微博有没有头绪啊？容易有头绪很容易设置一个 post 表吗？库存表。库存表就得有主键，就得有内容，就得有发布时间，有发布时间怎么弄啊？怎么弄啊？这个是 u 的表，这个发微博是 pot 表，因此我们得这样来设计，嗯， pot 表，然后呢？ pot ID， put ID，然后具体的 ID 的值，比如说3，比如说323。


然后他的 content 还得存他的 time 当前的时间戳 times temple。然后还得存它的 pose ID 冒号 3 冒号。然后是 time sorry 不再是time，也得存他的作者就是谁发的都得知道，是吧啊？作者都得知道。嗯，那群作者好臀。


作者存作者，那个存作者，那就得是他的这个叫 user ID，是吧？ user ID，比如说 5 号用户， 5 号用户，然后还得 post 冒号，然后 post id，然后冒号3，然后冒号，它的这个 content 行就叫 content content this is my home are。


可以了，就这样，大概是要这么三条，要这么三条有发谁发布的？嗯，啥时候发布的？时间戳还有内容。因此我们需要做一个这样的操作， in create global，然后那个 post ID 做一个自增长的这个ID。然后就是 set 的工作了， set post，然后 post ID，然后冒号这个 dollar post ID，然后冒号time，获得当前的时间戳time，然后 set 好。


设置它的content， dollar content 这个地方 dollar time 这个地方。哎哎哎，不是time，是 user ID 到了， user ID 保存起来好了，保存起来，我们看这是发微博的思路，思路都有了啊。了解下来。那然后我们再来到这个 post 页面里面，来到 post 页面里面保存走，然后 VIM post 点 PIP 走，把它保存进来。我们的思路首先得是那个判断有没有登录，没登录当然不能让你发了判断是否登录啊。第零部，最基本的第零部判断是否登录啊。然后第一步，然后就是那个接收post，接收 post 内容， post 内容啊。然后第二步，第二步干什么啊？粘过来第二步啊。嗯， set Redis 了。那就好，思路这么明确的情况下，那我们再动手就非常快了。


来看好了，首先判断是否登录好，可以 if 又得写这一句， if 等于false，谁等于false？ dollar user 然后等于谁等于 is login 它的返回值啊。好，如果等于 false 的话，那就别玩了，直接我给你嗨带过去就行了。


header，我们给你 header 到 location 到 index 点PIP，你去登录去，然后给你退出。好啊。那如果能走到第 25 行，说明那已经登陆了。已经登录了，那我们得收他的这个数据，我们点右键看源码，看看他收到这个数据收到了什么啊？收到了，这个叫做status。状态还是叫状态好？那你叫状态就状态啊？我只需要叫状态好，状态就状态啊。


好，那我需要 dollar r 等于 red c o n，然后我们开始写微博数据，写好来写。怎么来写？那就是 dollar r set 德拉尔赛特。 set 什么啊？ set 它的 post 冒号， post id 冒号，然后UI， dolly ID 等于多少？这是个问题。 dollar con c o n Redis 然后我们来一个 post i d 还得等于dollar，然后 in 克 ink 谁啊？英科那个 global post ID 是吧啊？然后我们把它 set 过来， set post ID，然后是点 dollar post ID，是这样的吗？然后再然后冒号。冒号？什么冒号？他的 user ID， user ID。好，我要查他的 user ID，给他 user ID 设一个值，那值是多少值？当然是我们刚才判断有没有登录时的那个 user 中的，然后 user ID 喽，还没完，还没完啊。然后我们再继续设置它的，有 user ID 之后我们再设置它的 time 发布时间。
user i、 user ID，user。


对的，来再设置time。来设置它的time，它的值是，那就是当取当前的这个时间戳就可以了，取当前的这个时间戳time，这样不就行了吗？然后还得再设置它的 content 内容是哪传过来的呢？是表单传过来的呀？是表单传过来的。因此我们需要判断一下他的那个表单是否完整，因此我得这样来操作， dollar content 等于dollar，等于 PP 冒号，然后那个它是叫 status 这个状态啊。


好，我做一个判断，钥匙 dollar content 飞针，我直接也 error 退出，直接 error 退出啊。说什么呢？说你这个请留言，请填写内容，好，保存，走。好，有内容了，此处肯定有内容了，然后我他的 content 等于你接收到的 dollar content。好了，这一个 pot 不也就写完了吗啊？也就写完了。
u 为 user ID，我这不是设了吗？
在 u r i d 查钱。
查询啥呀？哪些东西。
通过 user ID 定式？嗯，是。


通过 u 的ID。嗯，好啊。这个先保留一会，我们遇到困难的时候再回头来看这个，再看你说的这个建议，我看会不会遇到障碍啊？那现在我们就把这个 pose 的给它写进去了。写进去之后我们还是给他就回到，而写成功了的话就还给他回到 home 点 PAP 就可以了。回到 home 点PAP，然后退出location，后面点 PAP 保存起来啊。
好，然后我们做一个操作。嗯，看看发布能不能发布成功了啊？


来我们 update 发布它一下，发布又回到这个页面了，这就说明其实我们已经发布成功了。然后我们来到这个case，然后是post，冒号post，行，我们看到有一个 post ID 的密pose，是三条数据，对的，三条数据是对的，然后我们还得 get 他们的分别的内容，来试一试，来 get post，冒号， post ID，冒号，一冒号， user ID，走你 1 号用户发的没错，然后 time 走。唉，这个点发的也没错，然后content。也没错，发是发成功了，但问题是就是在我们这个地方，这个页面是不是应该把它显示出来呀？这地方还是死的？那哪行，我们就应该把这个内容给它显示出来才对了。显示出来，嗯，唉，这我们又遇到了一个挑战，就这一块很关键，这块很关键。怎么样把自己的微博是要查出来？其实这个倒不难，按照令王达刚才说的就可以了。但问题是如果你有一个关注的话，你的那个你是对方的粉丝，对方是你的什么呢？粉丝主，粉主，哈哈，你的那个粉主发的，你也应该能看到才对。问题在。
这地方是有一点难度的。
一个 bug ID，一个自己的ID。


肯定要从，肯定要记录自己的分组，找到分组的ID，然后通过分组 ID 再去用这个放。按照实验。
除了有自己的，还有自己粉主的都要给它取出来。那么如果我们能把这个问题再给它搞定，就是自己的这个东西要查出来，分组的东西要查出来，怎么来讲其中存在多少？


还有这个粉丝关系我们怎么样来维护选择关系啊？
好，那我们这一会做的成果也不小了，那给大家 5 分钟的时间考虑一下，这其实剩下的两个问题才是核心啊。注册那种小玩意儿，一个是粉丝关系，一个是茶自己及粉主的那个。取出来他们对应的那个内容来，好想。


