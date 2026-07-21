---
title: 7-5 Logstatsh数据同步 - 测试数据新增与修改
---

# 7-5 Logstatsh数据同步 - 测试数据新增与修改

[image](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/979513d9-b29d-4d1f-8f22-9c0965637d51/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZBLWTCHP%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T225210Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDVRCmNHBotJ2fNpyYv2c6t5%2Fk7RFuD9BZnPirfrOf7BQIgR0Ef7xl0DPQmvy7OHsZ1mhlOI0Aw%2BzqUYRB%2BU777bWIqiAQIxv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDM3jQjH0uVdtQCzl3SrcA8KmS%2FE9kOnB2LedrwMnp3EiK91PtNr%2FHxiG5ADidj5a42FCU%2BlvUb6FEvqc4%2BK6ertMWUU%2FVEHhMBsfDYNKFCjJR1085fczdyvSLzm6V%2B34Ei%2BJn%2FJURrmwRBogWbSftXUMPRXuK%2F0dPJcXRUqqUy0sxHwrQ17rGkvvoRrcxAnDf2MVqi%2B4BZW%2Fr3UwmYB92gzufMkQ3eEtsT02oHWkolOGZrtAUUlwnzXIG52%2BGiVvJRqf15RRv698k%2B%2F%2BEmMIW5JggJbIT8HR3Ni2rJbqeN6288ch0MNa%2FCkxy7fei5X8iC1drHMWwobdCH8haxMrb3PT6l%2FxCb85AtLtw%2Bs%2B%2BwDE7rVmoEAMVLQzyPwRYcWZb19hTbneU1ci37jAFEScqN%2FhiG7kotz1BMCeR3iDfAkwYztwO8Dj8a2YY2QzMypC8nxtvgRAPpjz0%2BQXkwov27x7bLd6Gc2%2Fs%2F0CuyIIJNgmJuxBWvSrlobR0daoZycHKeYITNzC%2BzxClb3BQA23ZUGmjknympe1u7caB0TjTy%2Fl1ihuAhcqZB%2BGni2oX83bz3rkHfhiKEdtpacuCpLbNycIYXYnvwVec6uJfai3oHPA1AZz2x8O4ETch%2FBcgKyjbGfaGiHPNGGoNYa8MNS5%2F9IGOqUBaIsNTLzKKYm7AE2eParvRpJoZkZrkUHHc6RltHtYPfViG1F5eMlOjs4Sb09dH238CMz%2FQTkbzINGB7j4hmDBpWLz9jhxoB5YPdkfgxC4oU%2F7ur74jlwGnWA1ZHnpGWBkTf3B3TNzLxzlKZrRYc7nbJQUAeUMRJsuDN%2F%2BmFexXa%2BKshqaKO%2B7MZDI7QooJ6JfYf8fkfHmC1GIJM7lbyhEjg1EvEuY&X-Amz-Signature=ecaad9cd9ba7fd9faf723468910e1eba1fa5ea88033833764593b79688fc6c58&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

[image](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/02b71a12-30e8-4857-a659-256b34efc2a6/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZBLWTCHP%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T225210Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDVRCmNHBotJ2fNpyYv2c6t5%2Fk7RFuD9BZnPirfrOf7BQIgR0Ef7xl0DPQmvy7OHsZ1mhlOI0Aw%2BzqUYRB%2BU777bWIqiAQIxv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDM3jQjH0uVdtQCzl3SrcA8KmS%2FE9kOnB2LedrwMnp3EiK91PtNr%2FHxiG5ADidj5a42FCU%2BlvUb6FEvqc4%2BK6ertMWUU%2FVEHhMBsfDYNKFCjJR1085fczdyvSLzm6V%2B34Ei%2BJn%2FJURrmwRBogWbSftXUMPRXuK%2F0dPJcXRUqqUy0sxHwrQ17rGkvvoRrcxAnDf2MVqi%2B4BZW%2Fr3UwmYB92gzufMkQ3eEtsT02oHWkolOGZrtAUUlwnzXIG52%2BGiVvJRqf15RRv698k%2B%2F%2BEmMIW5JggJbIT8HR3Ni2rJbqeN6288ch0MNa%2FCkxy7fei5X8iC1drHMWwobdCH8haxMrb3PT6l%2FxCb85AtLtw%2Bs%2B%2BwDE7rVmoEAMVLQzyPwRYcWZb19hTbneU1ci37jAFEScqN%2FhiG7kotz1BMCeR3iDfAkwYztwO8Dj8a2YY2QzMypC8nxtvgRAPpjz0%2BQXkwov27x7bLd6Gc2%2Fs%2F0CuyIIJNgmJuxBWvSrlobR0daoZycHKeYITNzC%2BzxClb3BQA23ZUGmjknympe1u7caB0TjTy%2Fl1ihuAhcqZB%2BGni2oX83bz3rkHfhiKEdtpacuCpLbNycIYXYnvwVec6uJfai3oHPA1AZz2x8O4ETch%2FBcgKyjbGfaGiHPNGGoNYa8MNS5%2F9IGOqUBaIsNTLzKKYm7AE2eParvRpJoZkZrkUHHc6RltHtYPfViG1F5eMlOjs4Sb09dH238CMz%2FQTkbzINGB7j4hmDBpWLz9jhxoB5YPdkfgxC4oU%2F7ur74jlwGnWA1ZHnpGWBkTf3B3TNzLxzlKZrRYc7nbJQUAeUMRJsuDN%2F%2BmFexXa%2BKshqaKO%2B7MZDI7QooJ6JfYf8fkfHmC1GIJM7lbyhEjg1EvEuY&X-Amz-Signature=750f8a66ca9b2fe9f23786bf7f5dd3bea881506919d48a035afd45842b0697a7&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

那么上一节我们是做了一个数据的同步，把数据从数据库中同步到 ES 中。那么这个是 OK 没有问题。那么接下来我们可以来做一个，来测试我们数据的新增以及是修改。我们先打开这个数据库，我们可以先去修改一条数据，比方说我们来修改这条153，我们要这样子在后面加一加修改数据测试同步打个勾更改。然后我们再来看一下它的时间时间的话我们可以这样子去看，我们再来打开一个新的命令行，我们进入到 user local love stash think 我们来看一下这个 check time 这个就是记录它的一个追踪的时间。那么在这里会有一个 20 年的 1 月 30 号，也就是说在我们再一次要去做执行更新的时候，我们的时间我们要大于这个 1 月 30 号的这个时间，你才能够做一个数据的同步。OK ，所以我们只需要这样子，我们在我们当前的数据库里面把这个时间我们改一下，改成到我们改大一些，比方说我们改成 2 月份，改到 2 月 1 号。点击 OK 好打个勾。那么这样子我们这一条数据在数据库里面就已经是更新了。随后我们可以等待一下咱们的这个命令行，看一下它的一个执行，我们先把这个退出，然后我们再来看一下。


那么你能够看到这里已经是修改数据测试同步已经被我们的 lost 所拿到这样的数据了，所以他会去做一个这样的更新，会同步到我们的 logstash 也就是说由 logstash 来同步到 ES 中。那么随后我们再来可以看一下它的时间，你会发现这个追踪的时间也会随之而改变。好。然后我们打开 header 我们刷新一下，我们再来做一个搜索。这个时候你能够发现这一条数据，我们放大一下这条数据在这里修改，数据测试同步就已经是更新到我们当前这个 ES 中来了，那么修改就没有任何问题了。


随后我们可以再来测一下咱们的一个数据的新增，我们把这里打开一下还是打开数据库。那么我们先来做一下这个 ID ID 的话我们随便写一下。比方说我们来一个 log stash 杠1001，然后我的这个这边我就随便写，因为我们也是为了模拟一下这边的数据自己去填。然后还有一个时间这边放大的话他有点看不到，我们缩小缩小再写时间的话先去写一下。这个时间的话我先写一个老的时间。好点击。OK ，那么这条数据我们现在就已经是新增了，那么新增好了以后，那么这个仅仅只是一个商品数据，那么我们还需要为它去新增加一些像图片以及是这个规格对吧，我们再来打开图片这张表，打开 image 好，随后我们也在这个下方去为他新增加一个这个我们就随便写。


123。然后这个这是他的一个 item ID 的组件名，组件名在这里，我去拷贝一下 logstash 1001 贴过来，图片地址随便写123。然后这里有一个 sort 对吧，这边我随便，写一个3，写个 1 也行。这边来一个一这是什么意思？这是 is man 写了1。


好，然后两个时间这个时间的话其实无所谓，我随便去填一个就可以了。好，点击打个勾，这是图片。随后我们再来一个，我们再来找有一个规格，把规格表打开。然后我们创建一个新的这个规格 ID 我们随便写。然后这是它的组件，这是 item 商品信息的组件，这个随便写。然后后面这是它的，这应该是库存，库存100，这是它的折扣。 0.8 这个随便写就是后面价格信息。然后这边有个时间，这个时间的话我们不是以这个为主的，所以这个时间你可以随便去填写一个我随便写一个测试的时间，点击打个勾。好。然后我们到这个里面去运行一下 select 做一个查询。好，现在是可以查询到一百七十五条数据，那么这个数据是可以被我们的劳斯莱斯给识别，随后我们在这边我们就可以去把这个时间去做一个修改了，把这个时间修改 2 月 3 号。


好，点击打个勾。这条数据现在我们就其实已经是新增了之后，我们就要等待一下我们的这个 logo stash ，等待它的一个同步。看一下我们的数据。能不能够新增。OK ，刚刚刷了一下，这边多了一条记录，那么这个记录其实就是新加的一条数据，那么这条数据就是 lost 101，这是我们新增的，然后我们再来回到咱们这里面再去搜一下，点击搜索。然后我们来搜一个 log stash 看一下这条数据，就是我们刚刚新增的一条数据。那么这样子它就能够被同步到我们 ES 中来了。OK ，那么在这边也能够看到命中是一百七十六条数据。 OK 那么这样子我们就做到了一个测试，不管现在我们是新增还是修改，我们都可以把数据做一个同步。


那么要注意一下，如果说我们要去做一个删除的话，如果说一条数据从数据库被删除，没有了不存在了，那么在 ES 中它是不会做到一个同步的。所以一般来说对于我们数据的话，如果说你是一个逻辑删除，也就是它是一个 is delete 作为逻辑删除的话，那么一旦数据逻辑上被删除了，那么我们就可以以一个时间的更新来把这个标识同步到咱们的 ES 库中。那么这样子就代表我们这个数据在 ES 里面也是被逻辑的删除的。OK ，那么这一点注意一下。好，如此以来，我们现在其实通过 log stash 就能够做到把我们数据库里面的信息做到了一个同步了。 Of.



