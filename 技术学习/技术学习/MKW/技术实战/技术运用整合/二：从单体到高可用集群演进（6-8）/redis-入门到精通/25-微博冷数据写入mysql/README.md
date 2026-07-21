---
title: 25-微博冷数据写入mysql
---

# 25-微博冷数据写入mysql

[image](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/e3aa6348-c744-482e-b2c6-cfe23619e030/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466THSDTVLM%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T225100Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDBbRQq%2BsjS8HDqwnqSCo3jPIumcuiEOIHrTzA0q96fwgIgOfsrEbSo7H7HGQ1N%2Bh%2F81IV5xas1f7Fa2g%2Bey2YtC%2BUqiAQIxv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDDBXGXKgUv0ajVV3iSrcA4KfEYq6UtbxoIzm92SkD164v4wJ97F%2BKKG%2B6rNtxCq%2FUUqpIUBXBYYJoRvHHgECoIb43LMXUe%2Fs%2Fnj57PQNxE4kbUH1sCKJEuasbwNNqQyM%2FyzCkfaLO2i4Wp%2FQNWRCn7LRNYlQtfqojdRoYALK13vItl31%2Fu%2F%2FZdDXxFeNhg2BSRcvkCmUrX8GpMhZ9B9qFLWZlqSFVPDG%2Ft4pyEPTCrZZ%2Bl2EVrlkTZ0w1dnE1fa2MgYygOZapz04Ohve%2Bu9xe0F%2BiwZSl16eUKRcmzdeJd7UA6vdzDOuoIDsIUBvvJs1LtqajuxelNuaj4ViBwneMMxhWicWqo8XXdkieqGL5vwZvwbbdLZ9LiyC9pOsasqPxBQxh61FJ6087voEWwrxx%2BFaWcqWXe4YqnOu4Jvn6kTD%2B%2BnCPnUMxbmIqqPVK%2BGT%2Br9sWPwvxBTnbpSNdu9O7q07iX%2FRHY81AnJ7to%2FjGcV3masshcYlk3bw6AKa6hgtQl%2F5ctRdic4M5HUTtvLKMra2skvxGLRRdPJ65ZAGo3QpPBxSZsBjChNHSmXwm%2Bh4OytARdc8ZCemDqubMZginW7QcXNlWgpVA3u5y3mDJn59wBr8KfTQv2HyiCzvMVz1lB9rMoWJvYAXklZnMOm5%2F9IGOqUBVHTBycoQtjoiFaHIRm8PjBkVLmokFRpsCKojyCfAE7CSpRA%2Fk00T46XIslfn3ew3TqjwEctQX4hd%2FQB0fgY%2FEGHZ59bRXvc5whvHjXLULRXPM1kCBAl3BsyJiRnSgAQtBpMVHT%2BxkX8JUf8s8tfXpN%2FWg5RQBWTMEEXuGOKyI2MP8UqrSYfVRVOhBURECtP3%2Fn3h%2BCwopdCffLQiwmTSr5xjyobT&X-Amz-Signature=d9ee6661e92d57dfc6aa53ac04caf11ea412923eeb3d2bd78c06196476cb0888&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

[image](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/f08201f4-8f45-4e82-85e1-2b4341b5fc23/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466THSDTVLM%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T225100Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDBbRQq%2BsjS8HDqwnqSCo3jPIumcuiEOIHrTzA0q96fwgIgOfsrEbSo7H7HGQ1N%2Bh%2F81IV5xas1f7Fa2g%2Bey2YtC%2BUqiAQIxv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDDBXGXKgUv0ajVV3iSrcA4KfEYq6UtbxoIzm92SkD164v4wJ97F%2BKKG%2B6rNtxCq%2FUUqpIUBXBYYJoRvHHgECoIb43LMXUe%2Fs%2Fnj57PQNxE4kbUH1sCKJEuasbwNNqQyM%2FyzCkfaLO2i4Wp%2FQNWRCn7LRNYlQtfqojdRoYALK13vItl31%2Fu%2F%2FZdDXxFeNhg2BSRcvkCmUrX8GpMhZ9B9qFLWZlqSFVPDG%2Ft4pyEPTCrZZ%2Bl2EVrlkTZ0w1dnE1fa2MgYygOZapz04Ohve%2Bu9xe0F%2BiwZSl16eUKRcmzdeJd7UA6vdzDOuoIDsIUBvvJs1LtqajuxelNuaj4ViBwneMMxhWicWqo8XXdkieqGL5vwZvwbbdLZ9LiyC9pOsasqPxBQxh61FJ6087voEWwrxx%2BFaWcqWXe4YqnOu4Jvn6kTD%2B%2BnCPnUMxbmIqqPVK%2BGT%2Br9sWPwvxBTnbpSNdu9O7q07iX%2FRHY81AnJ7to%2FjGcV3masshcYlk3bw6AKa6hgtQl%2F5ctRdic4M5HUTtvLKMra2skvxGLRRdPJ65ZAGo3QpPBxSZsBjChNHSmXwm%2Bh4OytARdc8ZCemDqubMZginW7QcXNlWgpVA3u5y3mDJn59wBr8KfTQv2HyiCzvMVz1lB9rMoWJvYAXklZnMOm5%2F9IGOqUBVHTBycoQtjoiFaHIRm8PjBkVLmokFRpsCKojyCfAE7CSpRA%2Fk00T46XIslfn3ew3TqjwEctQX4hd%2FQB0fgY%2FEGHZ59bRXvc5whvHjXLULRXPM1kCBAl3BsyJiRnSgAQtBpMVHT%2BxkX8JUf8s8tfXpN%2FWg5RQBWTMEEXuGOKyI2MP8UqrSYfVRVOhBURECtP3%2Fn3h%2BCwopdCffLQiwmTSr5xjyobT&X-Amz-Signature=d42ad3fb2c1255b79b693cfd13c162a07b3c8793a265a713613b42d9bff96c59&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

好，上午我们把这个微博做了一个重要的改动，就是把它的这个数据获取自己就是关注的人的那个数据，由这个推模型给它换成了这个主动获取拉模型微博。


那么接下来咱们还有一个重要的工作，就是要把它和这个 MySQL 要结合起来。嗯，比如说我们发的前 1, 000 条数据，我帮你存在这个这个 Redis 里面。 1, 000 条以后，我都给它存在这个数据库里。这就好比说我们来到哪呢？我们来到这个微博里，我们看自己的这个发的微博的时候，他自己发的微博的时候也可以，你看他一开始他给你显示了那么七八条的样子，还显示了七八条，然后你点的话，主动获取的话，再给你来更多一点，再来更多一点，也都是阿贾克斯获取的啊。然后你可以继续往后翻，翻到自己的第几页。


当然了，自己发的这个微博你发了多少是多少，人家不会给你减少的，就说你就算想看最后一页，人也能，也得应该给你找出来才对，然后呢？嗯，我也就是说我们，嗯，这个查看微博的时候，第一页的时候人给你显示的那么少，其实也就基于一个假设，就是说人一般针对微博都是看最近一两千的，这个东西离得太远就往往就不是说绝对不会再去看，往往就去看的少，这个概率上来说，所以现在我们就要做一个工作，就是要把每个人发的每一条微博要给它存起来，前面我们是存在 Redis 里面，这没有问题啊。但是如果都超过了 10 条，比如说我们把超过第 100 条的给它写到哪里面去呢？给它写到那个那个数据库里面去，写到数据库里面去，怎么给它写到数据库里面？现在我们要完成的就是这个工作。


每个人我们给他就是在 Redis 里面只给他存 1, 000 条，只给他存 1, 000 条，那你说刚才不就提到一个 1, 000 条了吗？刚才是指你收到的这个微博的这个数据，就是你相当于你获得的新闻信息、资讯信息收到别人的。现在我点我的这个人中心自己的这个发布的东西全部都是保存起来，比如说前 100 条放在这个 Redis 里，后边都放在这个数据库里。现在我们就来做这个工作，想一想思路上这个问题还真存在一些啊。大家来看一下这个问题，我们共同把它解决掉。就是在这个 post 的时候出了点问题。


就在这个地方，大家看我们针对这个 post 有一个 post ID，那么这一条微博你是把它写到 Redis 里面去之后，那么相对应的你是不是要比如说这个是 1 号用户发的，那你就得判断一下 1 号用户现在已经发了哪些微博了？然后那么这就意味着我们要把这个 1 号用户所有的微博都找出来，难点出在哪了呢？难点出在于我们这个微博只用了 post ID 做了区分，现在我就问你， 1 号用户想找自己发布的那些微博，你怎么找？就这个问题，现在你看看怎么找啊？存在一个这样的问题，来，大家一起想办法来处理这个东西。我们想把每个人的微博肯定得就是说人家来自己个人中心，肯定得看自己的微博，这是很常见的一个应用问题，就是按照咱们目前设计的这个键值的设计，用户想找自己的微博不是很好找了，我们该怎么办？


这时候我们可以怎么办呢？想一想办法，我们自己发的微博前 1, 000 个留在最新的， 1, 000 个留在 Redis 里，旧的给它弄到 MySQL 服务器里。嗯，光明那个就之前不是做过，就是下边不是有通过 ID 或者他那个就是做的这个可不可以？林光达的意思是说在这个地方，这地方只要前 20 个改一改成那个前 1, 000 个，改成前 1, 000 个，嗯，很好，对对，嗯。要么就是说从我们这个剑的设计上，我们再用点心把它的剑的设计键，嗯，给它改一改，让我们直接还能通过用户名来获取它的这个这个发布的微博，要么就是说我们在维护一个链表或者是集合这样来操作。


那现在看一看怎么来做比较妥当？维护前 1, 000 个倒不难，我们大不了再重开一个，这个键对应一个链表，就维护这个人，他的前一天千条微博，另外一方面就是超过了那个一千条之后的，我们不能把它立即就扔掉了，这一次我们不能把它扔掉，我们应该把它写入到这个数据库中去，对吧？我们应该把它写入到数据库中，嗯，来好好想想啊。


比如说我又为每个人维护一个链表，这里边始终就放。这个人，他发的钱最新的 1, 000 个微博，然后又突然又过来一个，那这个就得被挤掉了，这个就得被挤掉。挤掉了之后你不能直接扔，不能把它直接扔了。我们把它放在哪呢？我们把它放在一个全局的这个链表里面。
global，也就是说无论是谁，张三李四，你的微博只要超过 1, 000 条了，那现在这已经是第1, 001 条旧微博了。我们都给它弄到一个 global 的这个，能弄到一个 global 的这个链表里面， global 的这个链表我在干什么呢啊？然后我在每隔几秒钟跑一次，每一次我取 1, 000 条，取出他们的数据，往 MySQL 里面写。这个大致的思路考虑一下，我画一张大一点的这个图，来，大家理一理这个思路啊。是这么个意思。比如说这是张三的个人中心的微博，然后这是李四的，王五的。


咱先把思路分析清。果然人是铁饭是钢，吃完了午饭之后思路都清晰了啊。这个这是张三，这是李四，这是王五，这赵六他们每个人有 1, 000 个这个列表。然后你不论是谁，只要再往里一写，肯定得把最右侧的这个给它挤掉，是吧？最右侧的人给它挤掉，挤掉了之后我们不要扔，因为虽然是张三、李四、王五他们各自的微博，但是挤掉了之后有一个共同点，挤掉的这些数据都要写到那个 MySQL 里，都要写到 MySQL 里，既然都是要写到 MySQL 里，那好办了。所以我只需要维护一个这个 global 的这个链表，全局的链表挤掉的东西都往这放啊。


放了，放过来之后我大家知道这个 global 里面的数据不能说没用了，只能说这些数据就等着一件事就行了，干什么呢？写入数据库，是不是啊？写入数据库？所以我们在隔个在弄一个定时任务，每隔个一段时间，比如说几秒钟就一下子取出 1, 000 条来，取出来就往那个数据库写，这样不就达到这个热数据在 Redis 里，冷数据在这个 MySQL 里。好，现在这个思路我想已经分析的比较清楚了，那也就是说我们还需要造，根据用户的 ID 造一个链表，然后造一个 global 列表，然后再把 global 列表用定时任务往 MySQL 里面写，OK，动手试试啊。


把自己发的微博放到有序集合里，只要前 20 个，这个是前 20 个是干什么的啊？是供粉丝获取用的啊。来，再把自己的这个微博的 ID 放到一个链表里，对，然后放 1, 000 个目的是干什么？目的是自己的这个自己看。是自己看自己的微博用的。


自己看自己的微博用，然后 1, 000 个之前的旧微博都给它放到哪呢？给它放到这个？放到MySQL，那我们要根据 user ID 来维护一个独特的链表，因此我们得这么来操作，然后 l push， l push 给他，嗯，这个叫什么呢？给他起个名字，比如说就叫 my post 得了， my post， my post。然后 user ID 冒号，然后点 dollar user ID，那造一个独特的k，然后呢？然后把那个 pose 的 ID 给它写下来， pose ID 给它写下来，好，这就 OK 了。 io pose。但是我们需要判断一下它的长度，看看有没有超出 1, 000，因此我们用那个有一个叫 l 烂，对吧？ l 烂，要是大于 1, 000 了，要是大于 1, 000 了，好，大于 1, 000 很好办。大于 1, 000 的话，我们就是要把那个最右边的这个单元拿出来放到哪呢？放到 global 的最左边，是吧？这不正好是我们学的一个命令吗？叫 r 泡泡 l push，对吧？ r 泡泡 l push 来。


r 泡泡 l push，哎，列表之 r 泡泡 l push，那这个对我们来说正合适，就是把你的这个，唉，正好你有一，你这个人发了第1, 001 条了，然后把这个最旧的一条 r 吗？右边给 POS pop 出来，然后 io pose 到 global 里面去。你看好了，因此我们用 l 泡泡 l push。好，那咱们就来操作它。如果大于 1, 000 了，那我就。


dollar r，然后来一个 r Hop l push 耳泡泡的是谁？耳泡泡的是谁？耳泡泡的是自己的 my post，然后冒号 user ID，然后点 dollar user，然后是 user ID。这是一个列表，把它的值跑步出来，抛不出来给谁放到哪里？我注意放。


再来声明一个 global 就是待入库的，待入库我们不妨把它叫做回收站，或者是什么global，然后比如说叫仓库store，先来一个store， global store，只要你大于 1, 000 了，我立即就把它写到这个 store 里面去。好，那为了测试，我不妨先把它改小一点来把它保存下来。然后我们不断的发这个微博啊，不断的发这个微博来。
STORE 1 到 2 STORE 3 八个，十个 4 s T5。 this 体系。


should。好，我连续发了十个了，要是再发 T41 再发，应该说这个十一就不应该存在我的那个 my list 里面了，应该准备入库了，所以此时我应该在这地方，我应该能。
Tusuk dengan my list my sites. Sorry fo

r my space. Kalau kalau lo aja. Ah. Stok kalau stok. Saya. -1 global S T O R E global S T O R E l ran 检好我 12341111 再来一个 S T 12 global 冒号 stop 来，咱们检查一下啊。我在写的时候不断的往 my post user ID 来检查 my post。如果 l sorry l line 这个地方有问题， l line 这个地方你取谁的长度？ my post 冒号 user ID，然后冒号点 user ID 来力来走 1345678910 唉，再写这一条应该给我写到 global 里面才对，我们看看 global 里面有没有还真的挺奇怪啊。哎，检查一下哪里 ARPU 是这地方。大意来个冒号清一下，再来 123456789 是好，再发一个，他就应该进到 global 里面才对才合理。来，我们看一看 restore global 第27。好，我把它清空一下。


l Trim global 冒号 stop 1L。
Trim global S T O R E。


好，空了我再发一条，就也应该立即来到这个 global 才对啊。28，这个 28 是个干什么的啊？ 28 是个干什么的？有点奇怪。唉，来一个数据挺对的，应该来一个数据，立即来一个数据。这没问题，因为我这里边已经多于 10 条了，你再发一条新的，就得挤到 global 里面。但是那个值不对呀？来一起观察观察。


那个值。 my post user ID 冒号 user ID 没问题哦。值值对不对呢？值，对不对呢？那咱得判断一下，来，我们判断判断值对不对啊？值应该是他那个列表最右侧的那个值，对吧？列表最右侧的那个值，因此我们有必要把它列表的那个最右侧的值，我们给它取出来看一看就明白对不对了。


来，我们看一看 l range，然后那个 my post 冒号 user ID，然后冒号一，然后我就要看最后一个- 1 到-129，那现在也就意味着最右侧放的是29，那也就意味着我要是再发一条微博的话，应该把那个 29 挤出来，对吧？把 29 挤出来再 update 一下，然后我们看看这里是不是得到29，挤出来的是不是 29 就 OK 了？又挤出来一个29，没错吧？没错。


既然这个 global 我们也维护好了，那接下来就好说了啊。我们只需要写一个定时任务，不断的跑这个global，把 global 的数据取出来往那个那个 MySQL 里面存，咱们一次取 1, 000 条，一次取 1, 000 条啊。这样的话就减少 MySQL 的这个压力，一次存 1, 000 条啊。好，因此我们现在来再来建一张表。 LSVI read me 走。


好，这个是啊。美人的微博，前 1, 000 条在 Redis 存于Redis，更旧的存在于数据库啊。我们的这个思路，美人的 1, 000 条以前的都推到哪去呢？都推到这个 global store 里面去了。因此我们可以用定时任务，然后取 global store 中的钱 1, 000 条，前 1, 000 条入数据库。
好，那思路已经有了啊。保存退出走，然后我们写一个脚本。来，再来一个VIM，比如说叫这个 C R O N two MySQL 点PIP。
醒一醒，醒一醒，这会的很重要， Redis 和 MySQL 我们要结合起来使用。


include live 进来，我们要做的工作就是连上这个，他得连两个东西去空调底下站一会啊。咱们人少，不必那么强的纪律性，一动不动好连上Redis，然后这个还得连上 MySQL 才行，因为他要连，两者结合了啊。连上 Redis 之后，他要取微博，先要把里边那 1, 000 条的数据都给取出来，先要把里面 1, 000 条的数据都给取出来。那我们就得怎么样呢？就得这么着，先扫他一下，看有没有更简单的办法啊。
我们要把链表里面的所有的数据给它拿出来，问题倒是有一个，就是我们我从这个 global 拿的时候，一次拿多少呢？一次拿多少呢？我们的目标是一次拿 1, 000，一次拿 1, 000，因此咱要把那个链表最右侧的这个 1, 000 个单元都给它拿出来。链表最右侧的 1, 000 个单元，好，那我们选一个 s pop 有什么比较好？取 1, 000 个，那我们可以用 l trim，我们用 l trim 从右往左减 1, 000 个下来。好主意，就这样来，咱们从右往左剪切链表 l l line。


好，但是剪切之后直接用这个 f trim，你要是剪切了最右边的 100 个，剪切掉最右边的 100 个，它的这个值就变成最右边 100 个了。这这这个又不符合我们的这个用途，还真怪麻烦，真的挺麻烦。用什么办法呢？用什么办法呢啊？我们看有没有更好的这个命令来做它啊？我们的目标再强调一下，我们的目标是把那个链表最右边的 1, 000 条拿出来之后干什么？拿出来之后根据这 1, 000 条到再去挨个的查这些微博的真正内容，查出来之后再干嘛？再写入数据库，这就是我们的目标，这就是目标。


那我干脆我不找什么好用不好用的函数了，我这么的，我直接泡泡它，直接耳泡泡它不就行了吗？来，我们来一个。哇，有循环。什么时候开始循环呢？我来一个计数器，我 dollar i 等于 0 = 0 啊。哇，有哇？有什么哇？有耳，它的这个 LL 烂，也就是说只要你的这个 global stop，只要你的这个 global store 里面还有内容，并且什么呢？并且我的这个 Dolly i 小于 1, 000 这样写，可以这样，他是不是会循环的把那个链表给我往外取值啊？只要满足这个条件的时候我就干什么呢？我就 dollar r，然后我来一个 r 泡泡。


r 泡泡？谁？当然是泡泡 global store 了， global store S T O R E。好，就算你把这个结果得到了这个 post ID 给它取出来，取出来之后又干什么？又干什么？再根据这个 post ID 就能取最终的微博了，我们就能取微博了。好，去微博。那取微博来取。那这个具体的 post 就是道拉尔，然后是那个。


这个地方，这。就是 m 哈希get，哈希get，就是哈希 get 了，哈希get，它的这个建是post，冒号， post ID，再冒号，然后再点post， ID 是这样的，又取出来这个 post 应该是一个数组，得到这个数组之后你又干什么呢啊？你又干什么呢？好，稍等，我要取出它的哪些字段？我要取出它的 user ID，我要取出它的username，我还要取出它的这个叫time，还有它的 content 来，取出来这个 poster 之后又干什么呢啊？我再来。我要拼接SQL。 dollar SQL 等于 insert in two insert into。然后 post 的表，然后 post ID，然后是 user ID，然后是 user name，再然后是time，再然后是content，再然后是 container values。


那接下来咱在这个蛙有循环里面是不是就应该不断的拼接这个 CQ 语句了？不断的拼接这个c、 q 语句，来拼接 c 口语句，那就是点等于 Y6 是多少呢？一个一个来，一个一个来啊。嗯，这个拼接 c 口语句可是一个比较痛苦的过程啊。
好，那就是 post 冒号下面的。 post ID， post ID，然后是到了 post 下面的 user ID 在是 post 下面 user name，再是 time 和content。
你看这好了，那拼到这不行，下一个分号结束。小心一点的来拼接。
比较烦。


当然在开发中，真正开发中你不会老这么去拼接的，都是由通过数组来自动生成的，不会说让你手工去拼接。
post ID 有的 name 加上或者 time 是数值，不要好，继续来拼接。


poster 好，还有最后一公里，最后 10 米。好了，拼接完毕，然后给它加一个逗号好了，再然后蛙又循环完毕之后，请注意我们的这个 CQ 语句是不正确的啊。为什么不正确？因为拼接到最后一次末尾有一个逗号，对吧？所以我们还得再把它截一下，到了 c 口等于substraw，然后到了SQL，再然后那个 0- 10- 1，然后我们 Echo 这个 SQL 来，注意珍惜机会，这个 SQL 我会运行一次，只能运行一次，运行一次之后因为这个 global 里面东西就被清空了，我们来试试它是叫什么？叫那个 c r n C R O N two MySQL 点儿 PIP C R O N two MySQL 点 PAP 好了 on define master l l e n t 好，这个不是 l l e n t 写反了，是 l l 烂好了。
再一次的来测是走 Redis x get x patter，希望两个参数都是数组，你给的是一个希望，第二个参数是string，你给的是array。来，我们看看这个哈希get，哈希get。


好，我们看看这个哈希 get h get。 key field。哈希哈希 m get sorry，因为我们要获得多个域，因此我们要用哈希 m get 好了保存起来，然后再来测试values，直接就结束了。这是因为我们 global 里面的那个代入库的东西空了，没关系，我随便再来点，走，这次我们再来刷新，那你看这个就是待入库的，对不对？这个就是待入库的，我们看看拼接的字符串，对不对啊？没问题。然后我再来一个，这次我多来几个。那这 3 个你刷新好，已经给我们拼接成了一个 insight into pose 的 pose ID name time contents values 逗号。行了，就是这个语句，我们要的就是这个语句，所以在此处我们要做一个小小的判断。什么判断呢？如果要是为假的话，那 i 就没走的话， i 还是0。所以如果 i 要是小于一的话，或者说它等于 0 的话，说明当前没有任务要做，对吧？没有任务要做 no work， no job，然后就直接退出就行了，否则的话我们就把 CQ 拼接出来，光 AQ CQ 还不行，我们还得连接上数据库来Dollar。


那好写，连接 MySQL 并把旧微博写入数据库。那 Dollar RES Dollar R E S 等于 MySQL Connector，然后就是 local host， local host， local hoster router 右稍等，咱们这个机器上有没有MySQL？有，还没有密码？ show get a best show database 有个test，然后 use test。嗯， show tables 只有一个新闻表。


好，那我们接下来是不是得创建一个这个微博表？比如说就叫 post 来创建一个 post creator table post create table post。然后有一个 post ID，然后我们给他来这个 big int，因为它相当大。 big int 然后那个设为主键 promo key 好，为了查询速度快，加个主键。而紧接着是 user ID，然后我们给它来个 int 型。


可以， int 型也够了，然后再给他来一个这个就是 user ID 过是 user name 是这个叉型啊。在紧接着是发布的时间，我们是用 int 型存着时间戳，因此就叫time。此处叫 time 不大合理，因为 time 是那个是它的关键词吗啊？好，先试一试time，因为别和它的这个函数冲突了，函数名冲突了来， time 还是一个 int 型。再然后是他的 content 就直接差行就行了，因为微博不是 144 个字就 144 得了。
好，再然后安静点， My AI c m 然后 XSET UTF 8 建起来。好，这张表我们建立起来，这张表既然已经有了。再然后我们来看看连上本地空密码，连上之后我们选库， MySQL query dollar 柚子 test 库， dollar c，o， n 再然后选了库之后干什么？设置字符集， set names U，T， F 8，到了con，然后再执行我们的 SQL 就 OK 了。再执行我们的 SQL MySQL query，然后 dollar SQL， dollar SQL， dollar CON，这才完毕啊。


好，来试试咱们的这个入库行不行？ no job。好，然后再发微博来 CRONECRNECRONR 好，然后我们刷新走啊， no such a file 这是个什么问题啊？这是个什么问题？ time 和 MySQL 知不知道这是个什么错误？连 article 没连上好？这个问题很简单，就是它默认是到哪，它是它没通过那个就是 TCP 连接的形式，它走的是这个什么呢？走的是这个进程内通讯。明白了，他通过的是 socket 接口，而且他去 Temple 底下找的这个 MySQL 点， SOCKET 未必在这，你实际在哪你得说清楚。当然了，你要最简单的想解决这个问题，怎么办呢？想最简单的解决这个问题，很好办，就这样改成IP，强制它走 TCP IP 就可以了。


no job，然后再来CRONECRONR。好，再来刷新一下，走，OK，之后我们再来看一看这里有没有 select 星 from 叫post，果然有，我们的这个36、 37 这两行数据没有问题，这说明我们这个微博同步到这个 MySQL 中去了，对吧？同步到 MySQL 中去了啊。稍后我们要给我们这个同步脚本，让他写一个定时任务，让他定时跑，各位，比如说隔个几秒钟跑一下啊。那么同学们再来想，接下来我们要做的测试工作怎么来测试啊？我们写一个脚本，让他不断的往这个，往这个。嗯妈，这个咱们的这个推特里面、微博里面发数据，往里面发数据，不断的发，然后发的同时咱们看这个能不能同步成功就 OK 了啊。好，保存好这个地方，还给它改回原形，改回 1, 000 或者折个中100，便于测试100。yes。


好，接下来咱要做的就是这个测试工作了，测试咱写一个脚本，不断的批量的往里面模拟各个用户，往里面灌数据，往里面写数据，然后再让这个定时更新脚本，不断的往数据库里面来写。咱们看看如果说是只用 MySQL 的话，还要每秒能写 1, 000 个，那就几乎濒临极限了，咱们看看能不能每秒写他个 1, 000 条微博啊。好了，休息一会，咱们来做测试啊。


