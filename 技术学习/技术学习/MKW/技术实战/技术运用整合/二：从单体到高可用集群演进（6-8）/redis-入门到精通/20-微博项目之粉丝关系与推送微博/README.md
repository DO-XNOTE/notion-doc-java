---
title: 20-微博项目之粉丝关系与推送微博
---

# 20-微博项目之粉丝关系与推送微博

[image](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/df2a0ae0-3dd3-4ebc-8384-9c4f3639a093/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WT7ZIFMT%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T225056Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCAlJz3gcvMPYL8XToLoI%2F9FVZOsoDq%2FbDUDXvYPQ%2FJwAIhAJk8DW2jWvhAVWrEpAlyTXyEpajrqERLmM84C2vCqUlvKogECMb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgwGLlh8kPFYaKrlTywq3ANC9RKJoRFT2CGyCQ%2F1zma%2FV2c%2F1952a8BqQHpsnN2VkNEDuSibMKspHtZSXcHrGcmyxHEu%2BeY2Lp%2BT4WhQ8QrJy1J38%2F%2BHYdHBiGoN%2FQckc%2B%2F1tJZAbUo4eBSC6cMqmjUSf7R2prKLjT5Md4zciSrlp%2FyouF5jwCxDwrpNlYa4%2BRmRu76Q8yfP3fDsMKDJJQoGkABF1WC9dAk%2BsJiEdFwb%2FrIZiulMB8TI3DWa3ga2qZTE%2BVCwbW88F8CAqCbb3A9M1ZGqqUuIvoe0I5IcFAXceCFrw6X9tjVmXlLUc1r6OGL1Ig8xNxZV0%2FPh8Xh4qKSdERRsNNKgICMPz1TLAU%2F9g3L1rn%2BxTB6Hw6e6%2BlYmtbOISUWV4fJGMeQ2YtLyREzPuEkDhDhClkYzWA2BeKBhZFuYPHTY3Qxa%2FCtT5iubPuwaPfCE%2FaQToQSv%2FGKu844TXS0HIb37Cxos9gnwn7ubailq5%2BIVmrhQ6dk3%2FHwWoa5XMknuFQssjnXH%2Frw0wL%2BKej4rXvN5hb5DuSk3tBej3cI74DP3khMMnpeR3JV6ccs33CNz8vHBhJ2I82Iw9W6z2TkoJg49ile1YGOOSmcDqAVjVxCSL6dt1hk%2BtFPFsLLfAfp6zWiqiiIljTD9uf%2FSBjqkAQymsYuQebkoEHguZVZ3ws%2Fs0voKC8XvqPMXbvGAdzvpfFakUBFQANSVENQ379AZI9Bd3Gk8UinqxjBjHTi%2BwBHuZUjDU%2BZxCgDStR54zLkZ3Yz5sKbjdRr509mBoxwybkYS6URYYER21pY9vPJtIww1EEKZkgp9t54%2BeLGMAO3oJeSJ3PRjB650jI%2FJgFAZ7kx2UiRODm%2BXqym939WpBWaQuouy&X-Amz-Signature=a67ec3e5bb3ddb4b82c7222887bcd77ececa86399567558aaace54ba0da71edb&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

[image](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/c72d27fb-512d-477e-b583-2a6574175e87/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WT7ZIFMT%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T225056Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCAlJz3gcvMPYL8XToLoI%2F9FVZOsoDq%2FbDUDXvYPQ%2FJwAIhAJk8DW2jWvhAVWrEpAlyTXyEpajrqERLmM84C2vCqUlvKogECMb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgwGLlh8kPFYaKrlTywq3ANC9RKJoRFT2CGyCQ%2F1zma%2FV2c%2F1952a8BqQHpsnN2VkNEDuSibMKspHtZSXcHrGcmyxHEu%2BeY2Lp%2BT4WhQ8QrJy1J38%2F%2BHYdHBiGoN%2FQckc%2B%2F1tJZAbUo4eBSC6cMqmjUSf7R2prKLjT5Md4zciSrlp%2FyouF5jwCxDwrpNlYa4%2BRmRu76Q8yfP3fDsMKDJJQoGkABF1WC9dAk%2BsJiEdFwb%2FrIZiulMB8TI3DWa3ga2qZTE%2BVCwbW88F8CAqCbb3A9M1ZGqqUuIvoe0I5IcFAXceCFrw6X9tjVmXlLUc1r6OGL1Ig8xNxZV0%2FPh8Xh4qKSdERRsNNKgICMPz1TLAU%2F9g3L1rn%2BxTB6Hw6e6%2BlYmtbOISUWV4fJGMeQ2YtLyREzPuEkDhDhClkYzWA2BeKBhZFuYPHTY3Qxa%2FCtT5iubPuwaPfCE%2FaQToQSv%2FGKu844TXS0HIb37Cxos9gnwn7ubailq5%2BIVmrhQ6dk3%2FHwWoa5XMknuFQssjnXH%2Frw0wL%2BKej4rXvN5hb5DuSk3tBej3cI74DP3khMMnpeR3JV6ccs33CNz8vHBhJ2I82Iw9W6z2TkoJg49ile1YGOOSmcDqAVjVxCSL6dt1hk%2BtFPFsLLfAfp6zWiqiiIljTD9uf%2FSBjqkAQymsYuQebkoEHguZVZ3ws%2Fs0voKC8XvqPMXbvGAdzvpfFakUBFQANSVENQ379AZI9Bd3Gk8UinqxjBjHTi%2BwBHuZUjDU%2BZxCgDStR54zLkZ3Yz5sKbjdRr509mBoxwybkYS6URYYER21pY9vPJtIww1EEKZkgp9t54%2BeLGMAO3oJeSJ3PRjB650jI%2FJgFAZ7kx2UiRODm%2BXqym939WpBWaQuouy&X-Amz-Signature=a8c690240d4d322dd5638aeef04c39c8f012123cd2db84148afe3b8c2d04d765&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

来，我们接着刚才的这个话题来进行，刚才我们是说到这里稍微遇到一点障碍，就是我发微博也发成功了，发成功了之后我自己要看到自己的这个微博啊。这一说，这个也不难，这个我们可以查询自己的微博是容易查询的，还是等等，问题出在哪呢？就是这个地方这个领域内不仅要出现我的微博，还有我所关注的那个人的微博。在同理，我发的这个微博不应该仅仅在我这个出现，就是当我的粉丝登录的时候，他也应该看到我这条微博，也就这个地方上稍微难了一点点。那现在因为牵扯到粉丝与关注的关系，我们现在还没有粉丝，没法关注，所以我们不妨先把这个关注功能给它做了啊。我们来到这个热点页面，我们建立一个热点页面，这个热点页面干什么呢？把最新的用户我们给它拿出来，把最新的用户拿出来。好，我们 VIM 一个timeline，sorry，直接木一下timeline，点PIP，然后 VIM timeline。这个 timeline 我先让大家看一下它是干什么的？它的功能很简单，其实就是做一个广场镜的东西，把最新的注册用户给取出来，最新的注册用户取出来啊？最新的 50 条微博取出来啊。那好了，那我们把这个页面先给他整，整好了再说滴。


11 第依然是 include 这个新浪微博他们的粉丝关注关系啊。嗯，就用了，也很不错的一个开源的软件，一个挺不错的算法来存储的。用了是 200 个 g 的内存，把微博的这个关注关，相互关注关系就给它存储完了。 include 这个 lab 点pip。 include 这个。 200G 内存，然后这个 header 点 pip 保存过来，然后我们到底部去 DG o，然后。 include 谁当前目录下那个 foot 点pip。


好，保存我们这个页面，它要显示最新注册用户和最新的微博的，其实是，嗯，好，这个地方我们也让他判断一下有没有登录，判断一下。好， if is log in 钥匙没登陆，我们就让他走。 hello cation index 点 APP 推出来保存走人，接下来我们就做这一块了，最新的这个注册的用户，最新的注册的用户。最新的注册用户怎么得到？最新的注册用户怎么得到？还要得到他的名字才行。
怎么样得到最新的注册用户ID？从 RD 里面选。那肯定的，就是具体一点。
来，我们来到它的官方，我们之前 PPT 里面也。


介绍了一个叫啥键操作，键操作里面有一个叫做最还得最新的用户，因此我们还肯定得排序。我们之前讲过一个叫做sort，难道我没有写在里边？字符串啊？那不可能，扫他哪去了？


好，这样啊，我们先把最新的几个 user ID，我们就得给它拿出来才行。最新的几个 user ID 给它拿出来，那么最新的几个 u 档 ID 怎么拿呢？要是说用这个关系型数据库的话，我们肯定会这么来想， select 星 select user ID from user 表，然后 old bug user ID desc 倒序排一下，是吧？倒序排一下取个前 50 名，这不就行了吗啊？取前 50 名，但是在这个 K y 6 数据库里面，我们的观念要改变一下，你就不要再这样了，需要的数据你就直接存，不要带拐弯的，直接存起来。所以我们注册的时候我们就得。回头去操作一下了，我们再回头看看 v i m register。


这个地方，你得到了一个 user ID，之后得到一个 user ID 注册成功之后，你应该把它直接存在某一个地址，而不要说像 MySQL 那样再去查直接存这个东西。我们还希望对它排序之类的，那我们可以怎么样呢？我们可以整一个这个l，我们可以整一个link，对它来做操作很容易吧。比如说我们就保持前 50 个最新的用户，这个时候我们可以怎么做？很容易很容易，我们只需要这么做这个地方我们通过一个链表，然后维护 50 个最新的 user ID，通过这 50 个最新的 UL ID，嗯，可以的啊。然后怎么来做 l push， l push 是吧？这个地方 in Creator 是谁啊？我看看。


in create 英科瑞叫 global user ID 起名起的不太好。那就这样， ipos 我们这个地方叫一个名字，嗯，叫那个 new user link， new user link。比如说link，然后我们往有新用户的话，我们就把它推在这个 pose 的最左端， pose 最左端我们要让它的这个规模保持在 50 个以内，因此我每次 pose 一个 zo 后，它有没有可能超过50？很有可能，也有可能 51 了。


所以这时候我再干什么一下，我再对这个 link 干什么一下，我再把它截短，对吧？截短 l trim 一下， l trim 链表之 l trim 剪切列表左数从 0 开始，右数从- 1 开始。我们只需要，因为我是塞在最左边的吗？塞在最左边，我要保持每有心的我就塞在最左边，因此我应该从最左边减，因此我应该这样来操作，应该是 new user link，对吧？然后是0，然后是我要截 50 个0123449，对吧？截到 49 这不就保持前 50 个最新的用户了吗啊？这就保持前 50 个最新的用户啊。好，保存起来啊。再然后我 Flash 傲一下，我清一下东西啊。好，清一下，清一下之后我这次就可以这个重新注册了。稍等，重新注册，我的先退出，因此我们先再来一个最简单的 log out 功能， log out 点 p i p logout 点PIP。


对于 logout 点pip，我们要做的功能很简单，我们直接就 set cookie，然后是那个username，然后是轰，然后是-1，然后 set cookie， set cookie，然后是 user ID，然后是空，然后是-1，- 1 好了，再然后是header， header 到哪去？ header 到首页去 low k 升某号音 dex 点PIP。好，我们刷新来到这个首页的这个退出。好，退出，退出，这一次我再次注册啊。 1111111111 注册。嗯， undefined index user id on live 38 行，来，我们找一找 VI live PIP 第 38 行 is login is dollar 下划线cookie，这是一个notice。其实这个不是错误，不是错误，就是因为这个 cookie 里面压根就没有 user ID 这个键， notice 我们只需要把它的那个选项给它屏蔽一下就可以了。


register 微博index，这好办啊。easy，我们只需要，嗯， set 叫什么来着？ error reporter 怎么不变色？ error 变 error reporting，我们给它换成这个 e 傲，然后反选，是这个反选，然后是反选 e no 气死波浪号是求反好。是的，保存起来啊。


注册用户名已被注册，更换 undefine next。不对，设置的不对。这个加个什么来着？我记得是易傲，然后是专让他不报这个notice，专让他不 notice 在这，邮件在这，并且 sorry 这个地方应该是，并且关系，并且欧了，来再试一下啊。


好了，正常了，正常了之后我们那个 flush 一下，好，重新来注册111111111。注册好，注册完毕，应该说登录才对的，我看看登录成功了没啊？要登录成功了，按说他得给我设置那个 cookie 才对的啊。好，我们看看这个 reject 是不是啥时候已经？我们不小心，难道啥时候把它碰着了啊？看看怎么回事？瑞杰斯的点 pip 来，我们看看咋回事啊？噢噢，对的，这是对的，因为我们注册的时候我们应该干什么呢？我们光注册了没有登录，对吧？光注册了没有登录，我们还得干什么呢？专门来登录一下，还得专门来登录一下这个地方，怪不得他一刚才不给我们跳转，忘了这个事了，我们是光做了注册功能，没有随之让它自动登录，正常情况下应该你注册成功了就应该自动登录上，对吧？好，我们一会再来处理这个小的问题，咱们现在先捡着主要的干线来进行，然后现在来到热点那个区域，来到热点那个区域，来到热点这个区域，你注意我现在我要查询谁呢？我要查询那个 l 软件，查询那个 l range，查询那个叫 new user link，对吧？查询它的第0名到第- 1 名，其实就一个，他的一，这一个用户就在这摆着了。


我们目的是要把这个这一个用户以及他的姓名拿出来，对吧？所以我们怎么样取出这个列表？取出这个列表来，取出这个列表内容来，然后还得循环取出他们的这个姓名来，这个时候我们来到这个它的官方，我们看一看 a Redis。哎呦，我看看它的命令， case 有通用的命令啊。有一个挺好使的命令叫 salt 啊， sort key by pattern。排序用的好。干什么的啊？我来看看他干什么的。嗯，说 n is the number of elements in the list all sort to s all set to set 就是说它帮你能排序什么啊？排序这个链表里的 element in the list 列表里的这个值，帮你排序的同时，这个 sort 很有一个很牛的功能，类似于啥呢？类似于那个马西口中的左连接，很神奇，你看好了还能帮你 limit offset，就是像那个 MySQL limit salt 似的，来了那个我再打开一个。好，我多注册两个页面来看它的功能。来，我退出，退出了之后我 test 一 111111111 注册好，注册了之后我在 test 二。来注册好，现在这里面是已经有 321 这三个用户了，现在我要把这三个用户我给他取出来，那我们可以这样，就用sort。


sort？谁sort？那个 new user link 默认它是给咱们 a C 升序排列的，我现在就要让它倒序排列也容易，我们只需要告诉他这个，这个排序ASC、 DESC 就行了啊。



所以你看我这样来操作，比如说我就取前两条limit，先不说limit，我就那个DESC， DIC 又变成321，注意这个 321 它取出来的是什么呢？是用户的主键，对吧？是用户的主键，也就是转。我是用 MySQL 的语言来说，是 u user ID，我们根据这个 user ID 是想要他的什么呢？要他的用户名吗？要他用户名。如果是在 MySQL 下，是不是应该来个左连接？所以它这个 sort 有一个很强很牛的功能，你看它有一个 get pattern， get pattern 他 get part 就意味着什么呢？ get part 意味着什么？就是你不是要循环的得到 321 吗？他在循环把这个 321 带入到你那个 part 里面去，那个 part 是什么？又是一个键，这样的话也就意味着我们写一个那个叫 user 表下面的 user i user ID 下面的那个，此时这个321，我们把它把说，把它叫做一个变量，到了v，到了v，然后到了v，或者我直接在此处写一个星，然后我们获取它的那个 user name you 的name，你看好了，他在 sort 这个链表的时候得到的321，将会把这个 321 循环的替换这个星。


那岂不然后再重新获取这个k，那岂不是就循环的把 user name 都给我们取出来了？是这样的，所以这个 sort 的这个功能很强大。来，我们就写这个 sort 的这个用法来看看这个short，那因此我们这样来操作，我们来到哪里？我们来到 timeline 点 PIP 里面，好，现在啊。嗯，需要我们写一个稍微复杂一点的了，稍微复杂一点的我们要一个 new user list，新用户列表等于一个空数组，接下来我们要干什么啊？接下来我们要干什么？接下来我们应要多拉尔等于 CON Redis，是这样的， Redis C o n 还是 C o n redis c o n redis 然后刀拉尔，我要执行命令。


执行什么命令？我要执行 sort 命令。我要执行 sort 命令。 sort 谁 sort 那个 new user link，牛油的 list 还叫牛油的link？刚才去看一眼，保存 VI VIM register 是叫啥？这个地方维护的 50 个最新的链表 new u 的 link 好，那此处也得叫 link 了。 new u 的link。好，你就去给我 sort 他 sort 的同时我还要给他声明几个条件，声明条件就是奥特曼排序那几个，我们到哪去？这回得到哪了呢？得到那个坡 redis 它的 document 去看一看了。我们看看人家的这个 sort 来怎么来调用好，我们来看一看它的sort。


在这里来看一看它的sort，而 sort 你首先它是要求传两个参，第一个是它的那个列表，列表的名，名称，列表的名称，然后再传一个数组，说明你想按什么来排序，按什么来排序，然后还要 get 什么什么什么啊。好了，那我们就要这个用法，我们说是那个 all sort 是叫sort。 sort 的值是DESC，我们要倒叙，因为从最新的放在最前面，然后还没完，还得说。你要是排序的同时去挨个取这个 new user link 里面的 321 的同时还得再按照这个 321 帮我去get。谁？我不是要321，我是要一个左连接get，谁 get user？表下面那个 user ID，然后那个什么星，然后再是 user name。这样的话它将会产生一个什么效果呢？把 new user link 里面的 321 取出来， 321 分别替换这个星就得到，分别得到这三个k，就分别取出这 3 个 u 的 name 来，这其实就相当于 MySQL 中的这个左连接了，因此我们把它取出来的这个结果调一下，个取出来的这个结果给它放在这个 new user link 里。


dollar new user list 里， list 这里放在这，然后我给你打印一下，看一看咱们这个行不行？ new user list 悠悠的list。
保存一下，退出，保存好，然后我们来到这个 timeline 里面， timeline 里边热点。好，我得登录才能看好。111111，我来登录，登录，我再次点这个热点啊，现在是不是就看到这三个用户名了？占到这三个用户名已经 OK 了。好，我们再把这三个用户名干什么呢？我们给它。嗯，生成循环打印出来，生成这个链接，这就简单了，对吧？这就简单了，一旦到了这一步，那就好说了，来，我们观察他的这个用户。oh，在这里啊。好，我们不就是循环这个，写个for，一起循环这个最新用户嘛？这好办，这个地方这里来，我们要循环它写一个 for 一且循环。写一个 for 一且循环，谁循环？ new user list 当然了得，那什么 pip 啊？pip。
在这里好了。


抱一起，在这个地方 u 我给它换一换，刚才打印出来的结果是一个几位数组，一位数组那就好说了，一位数组这个地方我就直接给它换成那个 dollar v 不就行了吗啊？到了 u 也行， for each user list as dollar v，这不就行，就这样的意思吗？这里 PAP Echo，到了 u 这里同理也是 PIQ 到了u。


保存起来走好了，最新注册用户，我的注册用户哪里去了啊？来，我看一看，是不是 new user list 写的有问题。 new user list 噢， at v，你看，上面写个v，下边写个u，过分，好，保存起来，走，然后我们再一次刷新。那最新的这三个用户得到了这个地方，这一个小的地方练习的是 Redis 的 sort 的用法。然后我们点到的，我们点到某一个用户上去，比如 TEST 一， test 一，接下来我们，你看我们绕了多大一个圈，我们现在就是为了做这个关注的问题，那现在我们点到他的这个人中心才能去关注，才能去关注，因此我们写好再来写profile， move 过去profile，然后 profile 点PIP，然后 VI profile 点 p i p 好，然后给他 include 过来谁当前目录下的 libra 点pip。拿一把脸 p i p 在 include 过来，谁 in close 的过来，当前目录下的 header 点PIP。说了都包含过来，然后再来做一个判断有没有登录的，没登录直接让它滚开， is 不等于false，粘过来啊。


好好，这个地方要是登录等于false，那就是给他，让他去注册，好，让他去注册 index 好保存走，那登录了之后他才能来到这个页面上。然后这个页面我们重点关注的就是要。关注他，或者是取消关注这个功能啊。现在我们就先完成这个关注，先完成这个关注，你觉得一点之后，我关注了这个人，这个作为 K Y 6 数据库将要发生什么变化？将要发生什么变化？


来思路我们这样啊。这个美人啊，美人有。自己的这个粉丝记录，我们用集合来记录，然后每人有自己的这个关注的记录，也是用一个set，当我们关注某人，其实是发生了什么啊？ AID 关注了，关注 BID 其实是发生了什么？发生了什么？发生我们发生了一个这样的事情，user。


我们再来一个关注表，其实发生了一个这样的事，follow。 follow 是这样写的，这个是follow， follow in，follow，这个是粉丝 follow 表下面 follow 表下面这个。AID。follow，这是一定，记住这个是粉丝表，默念三面，这应该是这么来操作，是 follow in。我关注的人这个表里面AID，我关注的人是一个集合，里面添加一个什么呢？添加一个BID，是不是这个样子？同时反过来 follower 表里面谁关注的我啊？我的粉丝？我的粉丝。怎么来说啊？粉丝里边其实是这样的，你关注了BID， BID 多了一个粉丝，因此 follower 下面， BID 下面多了一个AID，是这样的。好了，那思路已经理清，那就好办了啊。我们就这样来操作就可以了，给它设两集合，设两个集合来，那么这个是到底是显示关注他还是取消关注？这就说明我们得判断我是不是他的粉丝，对吧？我是不是他的粉丝？好，我是不是他的粉丝，那我就得从我的 following 里面来，来来，来读取，我的 following 里面来读取。好，要想从读自己的 following 就得知道自己的 u 大ID，因此这个地方还得再来一个 dollar user，等于好来往下走。


另外还得知道，嗯，这个用户的名字，用户名是经常变的，所以我们还得这样来操作，还挺麻烦啊。取得地址栏上0，获取用户名一，然后查询他的ID，查询ID，这是我们刚刚注册时，我们就已经预留了这个功能。根据用户名查询ID，查询到 ID 之后，我再查询此ID，然后是否在我的 following 集合力，是不是这个道理？好，因此我们来抓紧操作好获取用户名是这样的， Dollar user 从地址栏上我们怎么来传啊？地址栏上怎么来传？我们看看刚才那个是页面是怎么来传的啊？到了， u 那好，我们从地址栏上获取那个u，或者就简单一点， Dolly u 等于GU。


然后我们是不是要获取这个用户名啊？获取这个用户，获取了这个用户名之后，我们就得获取他的uid。获取它的 uid 就是Pro，就是它的主人的uid，我们就给它获取当前这个页面的主人的uid，到了 poor UID 不是我的UID，以示区分，然后等于什么啊？等于什么？等于到了r，然后查询什么，按照那个规则来拼，是 user 表下面， user name 下面，然后再冒号，再冒号，然后点 dollar u，再点，然后冒号 u LID 是这样的，查询出当前这个页面它的主人的 user ID 来查出它 uid 来，要是为假， Pro uid 为假，要是 Pro i 到了 Pro UID 非真非真，那我们就给它错误啊。那就是说非法用户或者说不存在的用户名就给他退出了，来到这一步那就说明这个用户存在 uid 我也找出来了，那我得判断我有没有已经关注它，对吧？我有没有已经关注它，怎么来判断呢？非常的容易，我们只需要这样就行了。


我们知道集合里面不是有一个叫做 is members 吗？是吧？哎， is members 好， is member。那我就得让他让这个 dollar r 来再帮我判断一下 is member。判断什么呢啊？判断什么呢？判断这个主人我有没有已经关注他？怎么叫已经关注呢？那就是 following 我的这个，我的 following 里边，我的 following 里边。我的这个 following 表里边，然后对应的我的aid，我的这个 user ID，也就是 dollar user， dollar user 下面的 user ID， following you 的ID，我们来看看 following a i d 往集合里面判断我这个集合里面有没有这个人啊。好，那要是有 dollar is following is e 的f。


好，要是我已经粉过这个人了的话，这个地方你就要给它变一变，这个地方就要给它变一变，这个地方就给它变成Echo。那个婆UID，当前主人的 UID 就是我不再粉你了， Pro UID 不再分离了啊。然后 and f 等于等于多少啊？等于多少？这个地方得我们得做判断了。得做判断还挺麻烦，得做一个判断。好在这里 is f 等于 is f 为真，数值为一，否则问号为一，否则为0。


然后 is f 的这个文字， is f 的这个关注的文字握着也是要判断ESF， dollar ESF，然后问号，然后如果是为真说明为真错，为真了，说明已经关注过了，你就只应该取消才对啊。然后如果为真，同理，你这个字应该显示为取消关注，那要是为假，说明你没关注，那你就是关注他，关注他。好了，我在上面做好了判断，就是为了下面代码稍微清晰一点，所以在这个地方直接 Echo Pro ID，在这个 f 这地方我直接 Echo 那个 is f，对吧？跟上来。 e 子 f class 这个地方关注它也要变一变，给它变成PAP，然后 Echo Dollar ESF word 就是中文表示好保存起来，然后我们再次来刷新看一看， test 一 test 一好，嗯， call to a member function get 好，没关系没关系，因为我们落了一小步，很关键的一小步啊。什么呢？就是到了 r 等于。 COONN Redis CON Redis o 保存起来好，再一次的来刷新它，刷新它好。竟然说我的这个是非法用户，这简直不可忍啊。


来，我们看一看，我们看看是怎么回事？ user 表下面， user name 下面的用力工库里，我向 5 GPT 手感 Web lab 点PIP。多谢题型这个地方 get 好了，然后我们再一次的来刷新它 Redis is member，他说这个 is member 没有，那好，我们看看 is member 是在这个 SE 的member，sorry，好，再给它拿过来 s is the member 保存，然后我们来刷新它啊。那我啥时候关注的他，这不挺奇怪吗？刷新 TikTok e 好，来调试一下。


oh sorry sorry sorry sorry。
这么理is。它反应过来， e 的 f 等于一， d 的 f 等于一，说明这为 d 的 f 为甲喽， e 和 f 为甲喽甲确实是甲，这没问题，这个地方啊。嗯， a 的 f number 这样改一改，保存 e 的 f status 好了， you have status。这样来就可以了，来，在这里 e 的 f taters 再保存好，再一次刷新好了，现在 test 就在这，我要点关注它，又绕了一圈，我们现在来完成这个关注功能。完成关注功能，关注它，你看 UID 等于2， follow 等于一。


这个关注其实我们已经把它分析得很清楚了，已经关注，已经分析的很清楚了，就是完成这么两句话，往 following 里面写一个东西，往 follower 里面写一个东西，是吧啊？所以这样来操作VIM，来看看它的名字叫做 follow 点 PIP 来 follow 点PAP，好，include。这怎么那又是这几句，换换，烦死了。而刚才我们写的那个是叫 pro five，点 p a p。读过来，读过来，读读，走走走走走。唉，好了，要是没登录，我们把他踢走。好， include foot 点PIP。


好了，重点就在这一小块上，要我们要完成粉丝的关注了，要完成粉丝的关注，那我们只需要，其实说起来麻烦，其实因为我们都是用的是集合做操作，它就没有那个 pip 里面那一行一行的那个概念了，就是一个集合。所以我现在我要收取一下啊。收取什么？ UID 是谁？ f 是一还是0？ f 要是一就说明你要关注 F1 是0，你就说明要取消关注，仅此而已啊。所以我们先收那个 f 和uid，收 uid 收 uid 等于G2， UID 哆啦 f 等于 g f 什么情况？是噢，怎么是替换？胡闹好了， GF 我给它获取过来这个地方应该来说应该做什么呢？合法性判断。
应该判断 UID 是否合法， UID 是否 UIDF 是否合法值，这是一个，第二个还得判断一个东西，这个 UID 干什么呢？是否是自己不能等于自己，你自己关注自己算什么呀啊？所以要经过这样两个判断。所以这两个判断有好，同学们自己来啊。同学们添加上，那我就直接写主要的这个逻辑好，假设都通，判断通过了。


判断通过之后，那我应该怎么做啊？我无非是我要关注这个人，因此我应该在我的这个 follow in 表里面。我应该这样来做到了， sorry dollar r 等于 c o n redis c O N redis 叨了饵，然后 s 挨着集合添加吗？集合添加什么？添加什么？往哪个 k 添加？是往那个following， follow in，冒号following，我的就是关注的表，关注表？谁关注的表呀？那就是在这到了 user 下面的，就是当前登录者到了 user 下面的 user ID，这不就行了吗？然后我关注的是我关注的人是谁，是谁？那就是地址栏上接过来的这个uid，这就完成了。


很简单，关注完成之后，这个人是不是就对方是不是就被关注了呀？对吧？对方那不就被关注了吗啊？你偷窥了别人就被偷窥了啊。因此我们还需要给他来一个，就是那个 follower o w e r follow 表里面是不是应该填对方的uid？是不是对方的 uid 干什么呢？这里边填我的u，我的UID，也就是说对方被我关注了，被我很猥琐的关注，然后呢？然后我们关注完毕了的话，我们就可以这样就把它还转到刚才那个页面上去，还转到刚才那个页面上，还转到叫 profile 点 pip 问号 u 等于，然后那个那个等于点叫啥来着？叫Dollar。
那我们还得根据他的 UID 获取他的用户名才行，是吧？


还得获取他的用户名才行，你看我这地方放的是 UID 等于 2 吗？还得根据那个 URD 等于 2 知道它的这个哦。手嘎。好，那这个地方咱既然用 K Y 6，就用 K Y 6 来写来对方的 u name，对方的那个 u name 应该是等于在这写对方的 u name，应该是等于那个到了r，然后get， get 谁？我们根据那个表的那个 k 的规则，是在那个 user 表下面的，根据 user ID 来查询值是只是 dollar UID，然后查询的列式，壮士查询的列式 user name，对吧？ user name，这不就把它查出来了吗啊？查出来，因此我这个地方直接写那个you，然后 dollar you name，我给它 header 过去就可以了啊。然后来 location 冒号走人，好，保存起来。


现在我们看看这个千呼万唤关注功能好不好使，变成取消关注了，成功了，成功了。好。唉，取消关注，yeah，取消关注，yeah。什么情况啊？什么情况？说明这个取消关注不灵，对吧？取消关注不灵。取消关注为啥不灵啊？很容易分析，因为我们只做了关注功能，没多取消关注功能。


如果传过来的是0，你看我们这个地方压根就没讨论，如果传过来的是 0 的话，我们是不是就要把这个单元给它去掉？就是说，是吧？我们光往里加就没往里减，就没 s 瑞姆，所以我们此处做一个判断，所以我们要做一个判断，到了 r s is member 那个东西， s is member sorry 什么意？ SE member 不用判断谁，判断f，要是 f 等于那个一，那就正常走这一块，那没问题的。否则的情况下，我就认为你是要取消关注的。你是要取消关注，你是要取消关注。取消关注更简单，那就是从我的这个 following 表里面我给它 dream 过去不就行了吗？既然是集合，你就直接删就行了，不用关心顺序的事。没有集合，没有顺序。following，然后依然是我把这句去掉，我把这两句我给他 y y 二y，我给他复制过来，我就粘啊。好，我只需要把这个 SADD 我给它换一换不就行了吗？给它换成REM，这个我也给它换一换，我给它换成REM， OK 了，就这么简单保存起来，然后我再取消关注，加上关注， OK 了啊。


现在是我们完成了这个加关注的这个功能，加注关注的这个功能。你说那个属于黑名单功能，那个需要我们单做一个 block 表，就是黑名单表、 black list 黑名单表，然后用这个 Redis 做这个关注和黑名单，特别的方便。你看他取出他的粉丝中，比如说我的粉丝中，我查到了我的粉丝啊。就是说关注我的人不能叫我的粉丝，关注我的人，我再取出我所屏蔽的人，他俩求一下那个差吉不就行了吗？是不是不就正剩下就是我想要的那些粉丝了吗？所以对他来说，对这个 Redis 来说做这个功能是非常简单的。


好，我们现在完成这个功能了，完成这个功能化回正题，回归正题就是说test，我关注了test，那我现在我再打开一个这个浏览器，再打开一个浏览器，再打开一个浏览器，192.168.199，然后微博，然后我用test，我关注的是 test 几 test 人，关注人就是test，什么情况这是关注的是 test 的一，这地方应该显示出来，咱先不管这个细节，然后我先用test。一来登录 test 的，一来登录111111，我登上来了。登上来。登上来之后我要发 hello update。


好，其实已经发成功了，只不过我们没有看到，现在问题就来了，现在的问题就来了，就是对于这个，这个，这个主页热点我是谁啊？好了，对于我来说燕十八来说这个地方，你看自己的这个 home 的时候，看自己的这个 home 的时候， home 点 pip 的时候，这个地方不仅要得到自己的微博，还要得到这个我关注的 test 一发出发的那一条微博啊。这个问题要再解决掉，我们的这个开发就算基本完毕了。
其实要是最笨的办法，我把我的那个关注的人我循环一遍，可以，我关注的人我循环一遍，我把他们的那个取出来，或者取出来就行了，或者取出来。


还有一种办法，就是当一个人发微博的时候，我直接推给我的粉丝。an，那么我们到底用哪一种业务？逻辑上直接推好写一些啊？其实拉也不算麻烦，怎么来操作？


是这样的，我们先用推来做，就是我发一条微博不要紧，我还顺手把它推给 VIM post 点 PIP 光发微博还不算，然后干什么呢？
把微博推给自己的粉丝。好，来。把微博推给自己的粉丝，你自己首先得把自己的这个粉丝给求出来，对吧？自己的粉丝你给查出来，查好办了，我们直接那个查出自己的粉丝，好，先把自己的粉丝查出来再说。 s members。 s members 怎么查？自己的粉丝？应该从那个？following，follow，关注following。别人应该查 follow 还是查follow，也查自己粉丝。晕乎乎的理，我要查我的粉丝，我的粉丝有个什么特点呢？他们的我的粉丝不都在 following 里面放着的吗？是吧？被关注表吗？是吧？follow。


搜嘎，回去看一看VIM，然后follow。第二 p a p 来看看大卫，你看如果我关注某个人是怎么操作的，是把我自己的 ID 写在这，然后对方的 UID 写在后边文件。所以我要想找到关注我的人，然后对方被关注了是怎么回事？对方被关注了followers，我们应该找follower，对吧？找 follower 才对。


粉丝表，找到粉丝表，找粉丝表，那就是谁找那个 s sorry follow。粉丝表是这样写的， follower 下面我要找那个我的粉丝，对吧？我的粉丝，那就是 user 下面的 user ID，这不是我的粉丝吗？这就是我的粉丝。好，我找出来所有的粉丝， my fans。好，然后我 PRINT 杠 2 打印一下再说，来看看能不能找到我的粉丝。退出来保存一下，看能不能找到我的粉丝。这是在哪个页面？这是在 post 页面，这是在 post 页面。好，来，我来到这个页面，我看看我的粉丝， hi my fans hi， my fans ya。


瑞一，诶 18 是我的，是 TEXT2 的粉丝， TEXT 一的粉丝找到了，找到了啊。找到了之后你下一步的这个工作就是把你的这个微博推给他，把你的微博推给他啊。好，怎么推？我们又要为每一个人再创建一张表，这个就叫当前接收的那个微博表，因为微博固然是多，但是你仔细观察，人能看的微博无非就是前两页，所以我们完全可以给他维持前 1, 000 条就够了，那么他要再翻再多的这个微博。好，那我们调数据库往 1, 000 条往后的都写到数据库里面去了。


所以我们可以这样做，我们查到自己的粉丝之后，然后我们继续来给他们推微博，挨个的给他们推 Dollar fans，然后干什么啊？等于 Dollar user ID， user ID 这是干什么呢？因为自己的微博还要推给自己一份，也要推给自己一份。好，再然后我们循环 for each dollar fans as dollar v。


到了v，所以我们还得再维护一张表，还得再维护一张表，比如说就叫那个表，就叫那个真正看的微博，虽然那么多，你真正看的并不多，眼前真正看的就是说你接收到的推给你的那些微博，我们比如说就叫 receive post 好了， receive post，谁 receive 的这个post？谁得 receive 的这个post？那个。


到了 v receive 的这个post，到了 v receive 的post，然后。 receive 的post，你这个要接好多个好多条数据，那我们以链表的形式依然在以链表的形式，我们，嗯，给它存，比如说最新我给它存为 1, 000 条或者 100 条啊。


来，我们做一个模拟，那就是刀拉尔来 l push， l push，唉，我们把这个微博给他推进来，推一个 receive post，到了v，这个 v 是什么啊？这个 v 我把它叫直观一点， i d 叫 fans ID 要找 ID 好往里推。


推什么内容呢？推什么内容呢？当然是推这个 post ID 了，推 post ID 了，推 post ID 推进来，这样的话你发一条微博不仅仅是发一条，而是发了 n 条，你有多少个粉丝就发了多少条，是不是你给他推过去啊？当然为了保持这个粉丝，他的这个微博不至于膨胀的过厉害，我们比如说就前期就让他，当然这个前期我们可以，我们就可以让他只保持 100 条或者 1, 000 条。


当然这个业务逻辑放在此处不合适，应该放在人家的个人主页上，要放在人家这个每个人的个人主页上来维护才是比较合理的啊。所以此处我们干什么循环他的粉丝团把要接收的这个 post 的这个 ID 推到一个链表里，所以我们这一次的我们再一次的来到一个地方，来到哪儿？来到那个人的主页，也就是 home 点PAP，所以在此处这个地方 11 分钟前通过。谁这个地方好好，这就要干什么呢？就要把自己接收到的那些微博都要取出来了，自己接收到的那些微博都取出来了，这个自己接收到他自己发一条要推给自己，同时他的粉丝，他的它的分组发的也要推给他。所以我们就得这样来操作，就得取出别人，就是取出自己发的和粉主，粉主推过来的信息在哪呢？对我们来说取已经非常的容易了，因为我们专门做了一个链表来操作它，我们这样来操作。


到了 r 等于 new reader CON Redis，然后到了RNN，只需要干什么呢？只需要这个 sort 一下就行了，又一个sort，当然了我们先把它保持在一个，比如说我们先简单一点，就保持在一个十条的这个范围内，十条的这个范我们先让他的这个逗乐它的推过来的数据，我们就先简单一点，先保持在 50 条，比如说我们那就 50 条也很好办，我们只需要 l trim 一下我们用过的，我给它切割切割切割。


谁切割？那个 k 是谁？ k 那个是叫做 receive post 着，对吧？ receive post 冒号什么？就是我接收到的那些博客、微博，那就是 user ID， user 下面的 ID 根据 user ID 来区分的， user ID 来区分的 l trim 这个列表， l trim l trim。 l trim 我们看一看， l trim 走走。 l trim 我们给他 049 就可以了，给他一个049，我就保持在前 50 条，我们先做出最 demo 来，然后再完善。然后我取出前 50 条，我要对他臊他了，我要对他臊他了。


排序，其实我并不是想要别人推给我的那些博客的RED，那只是一堆数字，没有什么意义，对吧？我想要他的内容，是吧？我想要他内容以及它的发布者。好，那我别的不说，先把内容给你整出来再说。好，于是我这样来做 receive i v e post 又变成替换了 receive post，然后冒号，然后点 dollar user，然后 user ID，然后 sort 他。


之后我们知道，嗯，按照什么排序啊？按照什么排序？按照什么排序？其实这个他不应该给我排序才对，就应该正常的给我取出来。正常的取 post UID 推过来的，那为应该越新的应该越靠前，因此 sort DIC 倒叙越信量越靠前。然后我们还得有一个get，现在问题已经很明了。


你写一个get，就是你看你这个 receive post 里面满满的都是 post ID，也就是微博的ID，我们只需要再写一个 k 的模式，根据 post ID 把那个微博取出来不就行了吗？微博我们当时是都放在统一的一张表里面，是怎么来写的来着？这个得找最原始的记录了，你去看一眼。你看一眼啊？我们看一眼。那个 post 是怎么发的？来看看。


噢，是post，冒号 post ID，然后 post ID 它的 content 是这样的吧。于是我们来这里操作，集中精力 post 上冒号 post ID，然后是该谁了，这个地方该填啥了？并给我拿这个地方填啥。对，就填星，因为它循环的取出别人推过来的 post 的所有的ID，然后循环的把 ID 替换掉这个星，再取出它的内容出来啊。取出来之后这个就叫，我们把它就叫这个 new post，比如说就叫 new post，到了 new post。好，于是我们在这个地方要做一个循环了，要。
做一个循环。


for each dollar new post new post 这个叫 post 不合理 e 而是人称代指好 new post 来 new post 然后 as post as post 叫 at c 得了，省事一点省事。然后打括号结束掉。在这里结束掉，然后我就把这个内容hello，我给他，你替换 Echo dollar c，这不就行了吗？好，我们保存下来，看看这个 home 能否成功啊。


能够成功，第十四行有语法错误，第十四行可以耐心的找一找第十四行，第十四行 are salt？是不是括号有问题？不走看看咋回事？ receive a 瑞。sorry，这地方少了一个括号，来走，来，保存起来，走，来，刷新它，刷新它， class c o n Redis 什么？ class c o n 怎么new？这是直接调用才对，它不是一个累。好，再保存。走，来刷新走。有啥感想啊？问我有啥感想啊？来，我此时来到，hi， my fans 吐来滑痛，那自己已经能看到自己发的东西了。这是一个进步，推给了自己。我在这一刷新，唉，也看到了，但是这个地方仍然有不足之处。哪不足呢？你看这个名字不对，名字都写死的，太死的，时间也不对，时间也不对，时间也不对。这个不对怪啥呢？怪我们有一个地方设计的有点过度了，我们把那个 post 拆的太厉害了，拆成了时间段，拆成了那个内容段，拆成了 user ID 那个段，这就导致什么呢？我们想获得一条微博的内容，我们得干什么呢？得获取 3 次，对吧？不应该分的那么细，此处我们有点过度设计，我们可以把它整成一个，叫什么呢？整成一，我们完全可以把它整成一个，那个哈希类型，是不是？我们整成一个哈希类型，就相当于把一个微博的 time 那个什么都放到一个哈希结构里面去。


二。或者是最土的办法，你可以把它给，就是用竖杠给它连接起来也行，所以这个地方好解决，然后我们再来看看第几它有几个粉丝，它有几个关注这个地方，这个就更 easy 了啊。来，我们来到这个 home 点pip，这就是 home 点pip，还有几个粉丝，几个关注，这个其实很特别的容易解决，因为我们都是用那个去除自己粉丝，哎，计算几个粉丝，几个关注，这个很简单，其实就是干什么呢？不就是集算，计算那个集合的元素个数，是不是计算与集合的元素个数啊？所以我们只需要这样，我先算我的那个粉丝的个数。


Dollar my fans，我的粉丝的个数啊。我的粉丝个数，那就是我们知道有一个函数是专门用来计算，有一个命令是用来计算那个集合的个数的，叫 s 卡的，还有印象吗？ s card，那我们第一天学习的时候讲得非常枯燥的命令现在就派上了用场。


我要记我的粉丝，粉丝表在哪？粉丝表是在follow，因此我应该这样来取，应该是 follow 冒号点我的 user ID，这不正好是取这个 k 对应的是什么？是一个集合，我要数数这个集合里面有多少个内容。然后 my star，我关注的这个明星 Dollar r 再一次的 s card。 sorry c r d card s card 只需要把这个 follow 改成啥玩意儿？


我关注了几个人，是选 following 吗？我想一想 my fans。
所有自己关注的都在，是吧？这一个关注，一个被关注，这到了user，然后是 user ID 保存，然后往下写，在这个地方有几个粉丝？好，这里我有几个粉丝。 works for us Echo Dollar my fans 我的粉丝然后是关注表，然后是 Echo dollar my star 保存走啊。那么我关注了test，那我应该是有 10 个粉丝一个关注才对，是吧？正确的，没有问题。然后我们再来到这个地方，它应该是反过来是一个粉丝 0 个关注，对吧啊？一个粉丝 0 个关注没有问题，我们也来到热点，他俩相互粉一下，互个粉来关注他一下。现在我们再回到自己的这个主页来，这个主，这个 index 需要做一个判断，已登录了，直接给他回到 home 就行了啊。我们一会给它加上，然后是 home 点PIP，一个粉丝一个关注，那同理啊。


这个页面一个粉丝一个关注，没有问题，没问题。那么这个地方还有一些东西需要我们去完善的，哪呢？就是一，就是这一小块这个时间因为我把那个 pot 拆的过于散，导致取出来的时候不方便，你可以把它更聚合一下。其次还有一个，当你看别人主页的时候，我们看到那个微博里都有说你和他的共同关注，我们怎么算？共同关注？对于 Redis 来说算共同关注非常简单，你自己想一想怎么做，我们争取在这两个方面再继续给它加上共同，就是一个共同关注，一个是这个地方，这个几十分钟前这个地方给它算出来。求共同关注、求交集，求一次交集就可以了，非常的简单啊。然后还有就是这个数据，这个数据太多之后，比如说都三天前的这个微博了，三天前的微博了，我们可不可以把它归到 MySQL 里面去？ Redis 要和MySQL，你不可能说光用 Redis 的， Redis 要和 MySQL 真正配合起来使用才能显示它这个威力来。你要光用 Redis 意义并不大。


那这三个问题同学们先思考一下，我们下节课继续来完善，他们一个就是这一小块把它完善了，然后就是看到别人页面的时候能算出共同关注，然后还有能和 MySQL 要配合起来，这个 Redis 就专门负责热数据，今天的这个数据过了今天直接就把旧数据打入冷宫，放到 MySQL 里面储存着好了。


那么同学们可以观察出来，这个主要是使用Redis，难度并不大，主要还是一个设计思路上的这个转变，由一种关系型的这个数据库变成 K Y 60 一种设计的这个特点设计的技巧啊。好了，那我们这个demo，这个仿微博的这个项目，我们 demo 已经完成，下节课我们继续把它优化和 MySQL 结合起来，好保存起来啊。

