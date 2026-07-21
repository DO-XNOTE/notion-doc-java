---
title: 1-17 Redis的数据类型 - zset
---

# 1-17 Redis的数据类型 - zset

[image](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/cb8b4abb-863b-47e4-a4c5-522355c22f59/SCR-20240805-hfdd.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XOIN43DF%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T224935Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIFoSErecGls169NoBcuwFPbabMcSE8A98eXZpBmB37UiAiEA9%2Bork91MiDFz9fNkGr1SCPYZO%2FcOOUVhud8aY8Aj5DQqiAQIxv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDEaU9VE9DKpR7WvrPyrcAwF9jTQh1FRI5wS9ZM3pjXA%2BIDCNiNwXisOxOOukufNkL2T1unpI1bEqNdDHUv6KjiEFxfMUhnpl15Uv0Ds%2F72e2KBysihxgOTpgIq4L65NCWsf2aHwo7raLM5tmJLrMSQAbZuaHWnHEv%2BepcpfI6WZ7Vc56orBNefEJX%2FIsc1Vg1Lo16Q%2F262hIxgSr8a7WMx4LqO27%2FrphBJNUP9PmR5m86aXs0i7oVOMgI9C0FD263iOzDSQJKuDVdEWlGfIk1I%2B6TXru2%2FRLJrsv%2FWbwcfP9Zm1LHECKyXCwWkC%2B6VX1Ro46KUnZ8pFqa6t5OoAsqpKNFv3Uwq7MiwjQ3sNU%2Bv4f4aGi9kev6dlKihXgPv7idSv0tagNz43v%2BSYVuGhfGkOCjndLGLnvcTHKsvLUeebGT0%2BSATwwUZHVS0O3Iw7%2FFb8%2FSGh3ZS8cjA6a5tjkba7IEz31MXbhsLvuUr2SChRaUeIWBAfo9piKJdDTGoaQWfyrMZ8QRLHmO8YauLatvc44GGqtysWIoz0rkAGN9KiimKR%2BvzIUo8BUtDkI8NbCqANy3E58M%2FWz2hlp17NHnGqx2U8dheOziSHEPhoVsHZQCbhm6OO98QXl49OypaTw6AewNnXoNQWNvLjCMJm3%2F9IGOqUBph5U0An7GAcMLOfkiGrbsjZULzq1ltwv7IaSVj%2F%2FJssSX3EOI5evjE090PH6gsbPJP%2F9Z1VhNeRV6vpduFcMgjuRjyQScXWcpnhkv0k4U4ZBYHBmPPXH55HVGK6dx%2BIevgmFNxyPfc973xTX8esNES7F0dBMtdFq1nOJPmQCggxTkUVhZU6yw%2FV4BWtWVSsDATx9zk3tz%2BFNFP%2Bxh2Pe4CnQrpXe&X-Amz-Signature=d7450c90b40eabd13a5d01852c98cc22646e5814c4cf3c2546a3ccc7ff893ee6&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

[image](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/909abfb2-46eb-44af-b169-7551ee42f488/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XOIN43DF%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T224935Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIFoSErecGls169NoBcuwFPbabMcSE8A98eXZpBmB37UiAiEA9%2Bork91MiDFz9fNkGr1SCPYZO%2FcOOUVhud8aY8Aj5DQqiAQIxv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDEaU9VE9DKpR7WvrPyrcAwF9jTQh1FRI5wS9ZM3pjXA%2BIDCNiNwXisOxOOukufNkL2T1unpI1bEqNdDHUv6KjiEFxfMUhnpl15Uv0Ds%2F72e2KBysihxgOTpgIq4L65NCWsf2aHwo7raLM5tmJLrMSQAbZuaHWnHEv%2BepcpfI6WZ7Vc56orBNefEJX%2FIsc1Vg1Lo16Q%2F262hIxgSr8a7WMx4LqO27%2FrphBJNUP9PmR5m86aXs0i7oVOMgI9C0FD263iOzDSQJKuDVdEWlGfIk1I%2B6TXru2%2FRLJrsv%2FWbwcfP9Zm1LHECKyXCwWkC%2B6VX1Ro46KUnZ8pFqa6t5OoAsqpKNFv3Uwq7MiwjQ3sNU%2Bv4f4aGi9kev6dlKihXgPv7idSv0tagNz43v%2BSYVuGhfGkOCjndLGLnvcTHKsvLUeebGT0%2BSATwwUZHVS0O3Iw7%2FFb8%2FSGh3ZS8cjA6a5tjkba7IEz31MXbhsLvuUr2SChRaUeIWBAfo9piKJdDTGoaQWfyrMZ8QRLHmO8YauLatvc44GGqtysWIoz0rkAGN9KiimKR%2BvzIUo8BUtDkI8NbCqANy3E58M%2FWz2hlp17NHnGqx2U8dheOziSHEPhoVsHZQCbhm6OO98QXl49OypaTw6AewNnXoNQWNvLjCMJm3%2F9IGOqUBph5U0An7GAcMLOfkiGrbsjZULzq1ltwv7IaSVj%2F%2FJssSX3EOI5evjE090PH6gsbPJP%2F9Z1VhNeRV6vpduFcMgjuRjyQScXWcpnhkv0k4U4ZBYHBmPPXH55HVGK6dx%2BIevgmFNxyPfc973xTX8esNES7F0dBMtdFq1nOJPmQCggxTkUVhZU6yw%2FV4BWtWVSsDATx9zk3tz%2BFNFP%2Bxh2Pe4CnQrpXe&X-Amz-Signature=de30235652033e7ad80b4ed3cbf92b33426071901089ec506faf8ca7242ff6b1&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

[file](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/b9903e55-bf82-4c48-8f3f-4c80c84cfb9a/1-18_%E5%9B%BE%E6%96%87%E8%8A%82.pdf?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XOIN43DF%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T224935Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIFoSErecGls169NoBcuwFPbabMcSE8A98eXZpBmB37UiAiEA9%2Bork91MiDFz9fNkGr1SCPYZO%2FcOOUVhud8aY8Aj5DQqiAQIxv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDEaU9VE9DKpR7WvrPyrcAwF9jTQh1FRI5wS9ZM3pjXA%2BIDCNiNwXisOxOOukufNkL2T1unpI1bEqNdDHUv6KjiEFxfMUhnpl15Uv0Ds%2F72e2KBysihxgOTpgIq4L65NCWsf2aHwo7raLM5tmJLrMSQAbZuaHWnHEv%2BepcpfI6WZ7Vc56orBNefEJX%2FIsc1Vg1Lo16Q%2F262hIxgSr8a7WMx4LqO27%2FrphBJNUP9PmR5m86aXs0i7oVOMgI9C0FD263iOzDSQJKuDVdEWlGfIk1I%2B6TXru2%2FRLJrsv%2FWbwcfP9Zm1LHECKyXCwWkC%2B6VX1Ro46KUnZ8pFqa6t5OoAsqpKNFv3Uwq7MiwjQ3sNU%2Bv4f4aGi9kev6dlKihXgPv7idSv0tagNz43v%2BSYVuGhfGkOCjndLGLnvcTHKsvLUeebGT0%2BSATwwUZHVS0O3Iw7%2FFb8%2FSGh3ZS8cjA6a5tjkba7IEz31MXbhsLvuUr2SChRaUeIWBAfo9piKJdDTGoaQWfyrMZ8QRLHmO8YauLatvc44GGqtysWIoz0rkAGN9KiimKR%2BvzIUo8BUtDkI8NbCqANy3E58M%2FWz2hlp17NHnGqx2U8dheOziSHEPhoVsHZQCbhm6OO98QXl49OypaTw6AewNnXoNQWNvLjCMJm3%2F9IGOqUBph5U0An7GAcMLOfkiGrbsjZULzq1ltwv7IaSVj%2F%2FJssSX3EOI5evjE090PH6gsbPJP%2F9Z1VhNeRV6vpduFcMgjuRjyQScXWcpnhkv0k4U4ZBYHBmPPXH55HVGK6dx%2BIevgmFNxyPfc973xTX8esNES7F0dBMtdFq1nOJPmQCggxTkUVhZU6yw%2FV4BWtWVSsDATx9zk3tz%2BFNFP%2Bxh2Pe4CnQrpXe&X-Amz-Signature=bf1c0aa7733e03c513d7d522ff78b46c288ba80ac441a6b359089f18e73fffbe&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

那上一节我们是讲了 set set 的话，它是可以去把一些重复的数据可以去除的，接下来我们来讲一个叫做 zset，那么 zset 它是一个有序的，是可以去排序的一个set，其实我们也是可以把它称之为是一个叫做 sorted set，那么这两个是可以去画上一个等号的。


**如果说我们根据用户的一个积分去做排名的话，我们是可以使用我们 zset 可以去做的 ,zset 和 set 它们的一个区别的话就是 zset 它会带有一个分数，有一个szore，每一个 member 其实都是和这个 szore 捆在一起去使用的，他们是组合到一个组里面去的。**好，然后我们就可以来操作一下，在这里的话先考虑了一下，我们可以先使用 zadd，其实 z 开头 z 就是代表一个是 zset，然后我们可以来设置一个叫做 zset。


在这里面我们就可以来看一下，这边有一个szore，还有是一个member，比方说我们可以来一个十分的话，来一个duzk，再来一个 20 分，可以来一个pig，再来一个 30 分，可以来一个 zhizken 再来一个 40 分。我们来一个beef，再来一个 50 分，来一个sheep。


回车一下，这个时候我们就像这个 zset 里面塞入了总共是有 5 个值，然后我们可以来看一下这 5 个值里面是包含了一些怎样的内容。那么我们可以使用 z range，然后来一个 zset，从第 0 个，然后所有这样子，那么总共是 5 个全部都展示了出来。如果说你要去带有分数的话，在这个后边可以去加一下，这是一个可选的。写上一个路易斯szores，根据他后面这个去敲一下相应的我们的一个内容，也就是 member 和他的一个数值，也就是分数会统一的一起显示出来，那么一个对于一个，那么在这里面虽然是显示了有 10 项，但是这里面总共是包含了 5 组数据。


OK，好，然后我们假设在这个里面把这样的一句话再去执行一下的话，我们来一个回车，你会发现这里影响的是0。所以再一次去做一个查询的话，这里面的数据其实是不会有的，因为它是会做一个去重的。OK，当然我们可以再来做一个。现在我们可以在这个里面去插入一个新的分数，比方说我们插入一个 25 分对吧， 25 分的话我们就来一个a，b，z，再来一个 35 分，比方说来一个x， y z。回车添进去以后，由于我们之前也说了ZSET，它是一个有序的，它是一个sorted，所以我们来看一下。这个时候你会发现 25 分和这个 35 分的是插入在他们的中间了，那么他是帮我们做到了一个有序的排序。


OK，这个就是 z 艾子以及是 z range 它最基本的一种使用方式。OK，好，然后可列一下。接下来我们可以来看一下，就是说我们是可以去获得某一个值，它所在的一个分数，以及是它的一个下标的，因为有时候我们是可以去做一个相应的获取的，比方说我们先查询出来，在这里面我们可以去找一个叫做beef，我们来找一下。可以通过一个 z rank，再加上一个 zset，再加上你的一个 member member，就是这个beef，把这个拷贝过来回车你会发现在这里打出来是一个5，也就是说 5 是它的一个下标。


这个的话是不能按照 v szores 的，因为它这个 v szores 其实它会把所有的数据全部都会展示出来，我们可以这样子把这个 szope 给去掉，那么这样子的话可以看到咱们的一个 beef 所在的一个位置其实就是58，从 0 开始的话， 5 就是它的一个下标，这里数字为6，因为它是从 1 开始的。


OK，这个就是 z rank 获得它的一个下标。那么当然除了下标以外，我们也可以获得它的一个分数。这个 beef 现在它分数是 40 分，很明显我们也是可以去获得的。通过 z szore 再加上一个 zset，你要去拿到它的 beef 回车一下，然后你的分数 40 分就可以拿到了。


OK，那么这个就是获得它特定的某一项特定的member，它的一个下标以及是它的一个分数。好，然后的话我们还能够做一个统计，比方说可以使用 z zard，这个 z zard 的话，其实我们之前有用过zard，我们来写一个 zset 回车。目前在这个 zset 里面总共是有 7 项内容，所以这边的数值显示的是一个7，OK，是一个7。那么当然除了这个以外，我们还能够做一个统计，比方说我们可以来这样子， z zount 我们还是先显示一下 zrange， with szores，在这里面我们可以去抽取一下，比方说可以在 20 分和 40 分之间的内容，只要是在 20 分和 40 分之间我们就可以把它的一个个数给统计出来。就可以使用一个 z zount zset，然后它的最小和最大的一个分数写上一个 20 分，再加上一个 40 分。按一下回车，总共是有 5 项。在这里是pig，就是一项两项三项四项五项。这个的话其实也就是一个大于等于 20 和小于等于 40 分的，所有的内容都会在这个里面等。OK，这就是一个获得它的内容， z zount。


最后我们还能够再来做一个分数的获取，肯定一下这个分数的获取。比方说这个时候我们可以使用 z range，它有一个 by szored，这个是根据它的分数 see range by，szore。然后 zset 有一个 20 和一个30，写上一个 40 回收一下。这个时候是可以看得到是在 20 分和 40 分之间，我们加上一个 VS szores 回车，那么就是 20 分和 40 分。也就是大于等于 20 和小于等于 40 的内容我们都可以展示出来。可能有同学会问我能不能去查询一个大于 20 小于40，就是说不要有等于的，也可以在这里面。我们可以在这个比方说在这里可以加上一个括号，这个括号就是代表小于40，等于的话就会不带的，回测一下你会发现这个 40 分就不会包含了。


那么这个 zset 20 后面的这个我能不能不要等于20，我这样子写写这样的一个括号，这个就是一个大于 20 小于40，这个 20 分不要包含在这里面。这个 pig 我不要。回车一下你会发现这个语法有问题吗？其实是一个括号的问题，这个括号的话你应该要写在它的一个左侧，这样子就是代表一个大于 20 小于 40 在他们区间，这样子的话 pig 就不会包含在这个里面了。


OK，那么这个就是一个 z range by szore，根据这样的一种分数，根据分数去获得它区间里面的所有的一些内容，是可以根据这个去做的。另外的话，其实我们根据他拿到的一个结果值以后，还是可以去做一个 limits 给大家演示一下。在这里面的话，我把这个 40 和 20 去掉， with szores 我也去掉。

可以看到在这边有个可选项limit，写一下， limit offset zount，那么这个知识就类似于 MySQL 里面的一个分页对吧？比方说我offset，我们从 1 开始，我写一个2，然后按一个回车，那么这个时候他就获得了一个a，b， z 和zhezk。我们把这个先展开看一下，在这里面下标唯一也就是a，b，z，那么从这个a，b， z 往下总共是获得两项，也就是a， b z 和这个 zhezking 可以拿到。如果说我们写一个 limit 是 2 和 3 的话，我们就会从它的 zhezking 开始往下面找，总共是找三项zhezking，x，y， z 以及是 beef 都会取得。


OK。那么这个也就是在我们的一个根据这个z，u， n 值班szore，根据这个分数做好一个排列以后，从新的一个列表里面再去做的一个Linux，相当于是一个子检索了。OK，好。然后我们肯定了一下，那么其实还有一个叫做 z rain，其实就是remove，就说我们之前也都用过了，那么这个是在我们这个 zset 里面去把某一项给删除，这个 member 是它的一个值。比方说我们可以删除这个pig，把这个 pig 给删掉，然后这个 memo 里面是可以写多个，我到这边就写一个删除，影响了一个。随后我们可以来查询一下 z range 找一下。那么在这里面的话可以看到我们的这个 pizk 已经是没有了。


如果说我们再来上一个sheep，再来上一个beef，回车影响了两项，然后我们再来做一个查询，你会发现在这个里面的话，很明显已经是没有了， sheep beef 都没有。OK，那么这个就是一个删除。OK，好。那么我们在这几节课程里面，其实主要就是针对了这五项，主要是 5 种数据类型去做的一个讲解，这些内容的话，其实相关的操作，相关的一些命令的话会有很多，我们是不需要去死机密的，用到什么就去查一下 API 就可以了，包括在工作的时候也是一样的。那么我也不会特地的去记住，如果说是忘记了，百度上去搜一下就可以了。


而且对于学过 Redis 基础的同学的话，这些其实应该都接触过，如果说你是第一次接触俄历斯的话，那么这些 5 大基本数据类型还是要去在课后好好的去写一下，去操练一下，去理解每一个 API 是用于去做什么的，到命令行里面都去输入一下，都去敲一下。


OK。那么另外的话，其实还会有一个网址给大家看一下，

[http://redisdoc.com/](http://redisdoc.com/)

这个网址的话是 ready stop，也就是这个网址，那么在这个网址里面其实可以看得到，这里面包含了很多的命令，有些命令的话其实我们在课程里面也没有去讲，因为我们没有那么多的时间。有兴趣的同学到这里面可以去敲一下，去找一找，看一看，每一项里面都是包含了很多的内容，或者说你直接去看一下，浏览一下，过一遍有一个 g 就可以了。如果说以后再用到的话，那么再根据他的一个文档再去查也是可以的。OK。

[image](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/462deaec-af10-4156-9447-001581117073/2020-09-17_195632.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XOIN43DF%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T224935Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIFoSErecGls169NoBcuwFPbabMcSE8A98eXZpBmB37UiAiEA9%2Bork91MiDFz9fNkGr1SCPYZO%2FcOOUVhud8aY8Aj5DQqiAQIxv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDEaU9VE9DKpR7WvrPyrcAwF9jTQh1FRI5wS9ZM3pjXA%2BIDCNiNwXisOxOOukufNkL2T1unpI1bEqNdDHUv6KjiEFxfMUhnpl15Uv0Ds%2F72e2KBysihxgOTpgIq4L65NCWsf2aHwo7raLM5tmJLrMSQAbZuaHWnHEv%2BepcpfI6WZ7Vc56orBNefEJX%2FIsc1Vg1Lo16Q%2F262hIxgSr8a7WMx4LqO27%2FrphBJNUP9PmR5m86aXs0i7oVOMgI9C0FD263iOzDSQJKuDVdEWlGfIk1I%2B6TXru2%2FRLJrsv%2FWbwcfP9Zm1LHECKyXCwWkC%2B6VX1Ro46KUnZ8pFqa6t5OoAsqpKNFv3Uwq7MiwjQ3sNU%2Bv4f4aGi9kev6dlKihXgPv7idSv0tagNz43v%2BSYVuGhfGkOCjndLGLnvcTHKsvLUeebGT0%2BSATwwUZHVS0O3Iw7%2FFb8%2FSGh3ZS8cjA6a5tjkba7IEz31MXbhsLvuUr2SChRaUeIWBAfo9piKJdDTGoaQWfyrMZ8QRLHmO8YauLatvc44GGqtysWIoz0rkAGN9KiimKR%2BvzIUo8BUtDkI8NbCqANy3E58M%2FWz2hlp17NHnGqx2U8dheOziSHEPhoVsHZQCbhm6OO98QXl49OypaTw6AewNnXoNQWNvLjCMJm3%2F9IGOqUBph5U0An7GAcMLOfkiGrbsjZULzq1ltwv7IaSVj%2F%2FJssSX3EOI5evjE090PH6gsbPJP%2F9Z1VhNeRV6vpduFcMgjuRjyQScXWcpnhkv0k4U4ZBYHBmPPXH55HVGK6dx%2BIevgmFNxyPfc973xTX8esNES7F0dBMtdFq1nOJPmQCggxTkUVhZU6yw%2FV4BWtWVSsDATx9zk3tz%2BFNFP%2Bxh2Pe4CnQrpXe&X-Amz-Signature=92d0957de68c0a609fdf32d04e6b11801d686162efe8693bf640f6b624179bbd&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

[image](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/a838b287-129a-41a2-aa5e-1dfaa51cc2ab/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XOIN43DF%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T224935Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIFoSErecGls169NoBcuwFPbabMcSE8A98eXZpBmB37UiAiEA9%2Bork91MiDFz9fNkGr1SCPYZO%2FcOOUVhud8aY8Aj5DQqiAQIxv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDEaU9VE9DKpR7WvrPyrcAwF9jTQh1FRI5wS9ZM3pjXA%2BIDCNiNwXisOxOOukufNkL2T1unpI1bEqNdDHUv6KjiEFxfMUhnpl15Uv0Ds%2F72e2KBysihxgOTpgIq4L65NCWsf2aHwo7raLM5tmJLrMSQAbZuaHWnHEv%2BepcpfI6WZ7Vc56orBNefEJX%2FIsc1Vg1Lo16Q%2F262hIxgSr8a7WMx4LqO27%2FrphBJNUP9PmR5m86aXs0i7oVOMgI9C0FD263iOzDSQJKuDVdEWlGfIk1I%2B6TXru2%2FRLJrsv%2FWbwcfP9Zm1LHECKyXCwWkC%2B6VX1Ro46KUnZ8pFqa6t5OoAsqpKNFv3Uwq7MiwjQ3sNU%2Bv4f4aGi9kev6dlKihXgPv7idSv0tagNz43v%2BSYVuGhfGkOCjndLGLnvcTHKsvLUeebGT0%2BSATwwUZHVS0O3Iw7%2FFb8%2FSGh3ZS8cjA6a5tjkba7IEz31MXbhsLvuUr2SChRaUeIWBAfo9piKJdDTGoaQWfyrMZ8QRLHmO8YauLatvc44GGqtysWIoz0rkAGN9KiimKR%2BvzIUo8BUtDkI8NbCqANy3E58M%2FWz2hlp17NHnGqx2U8dheOziSHEPhoVsHZQCbhm6OO98QXl49OypaTw6AewNnXoNQWNvLjCMJm3%2F9IGOqUBph5U0An7GAcMLOfkiGrbsjZULzq1ltwv7IaSVj%2F%2FJssSX3EOI5evjE090PH6gsbPJP%2F9Z1VhNeRV6vpduFcMgjuRjyQScXWcpnhkv0k4U4ZBYHBmPPXH55HVGK6dx%2BIevgmFNxyPfc973xTX8esNES7F0dBMtdFq1nOJPmQCggxTkUVhZU6yw%2FV4BWtWVSsDATx9zk3tz%2BFNFP%2Bxh2Pe4CnQrpXe&X-Amz-Signature=0c596275ffa59d1e8c52ccd1d265279614b1be5f5f01b75e2da67982bd0c5899&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)


