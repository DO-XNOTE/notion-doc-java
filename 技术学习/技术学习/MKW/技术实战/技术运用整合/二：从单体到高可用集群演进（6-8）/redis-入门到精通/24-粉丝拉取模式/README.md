---
title: 24-粉丝拉取模式
---

# 24-粉丝拉取模式

[image](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/d2368e51-4518-4bb9-965c-950608811c95/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RTSCJAMT%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T225059Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIG79phBSq%2FUS4EpuSo9IZPFaZqesQQLbf9Yx5PzTibOoAiAI8X%2BqGvc4mwY7OPmPH9hQK9oARRHq%2Fv%2F5GpTtz0lxjyqIBAjG%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMljAb4MuYWyfU5yUXKtwDHBcs2np7CMRv9HRvelj0f1bemBWqmS%2FCUf%2BZy4HV46ju3auKc1n%2FDzSWI9X4H8pUTN1RUsjB9Iz2707TpVLk2EkHQFqPofwny0ev5%2FzV7BwY%2F25JzacGM9xAzlFj%2BW7i4HxYInEew7phwc1a2KvjggWfzowbSSXmEmZ88RMs8WMPTXlBZoReFRb%2BEUkjq%2FFgcPlIjUa%2FixsFVLao944gIsHmilcyKc3xkadAAlSbOjz5%2FkrV%2BJUFm8GQNU21n7SYFwNGysILU2H70uprtakpUvo%2F0vdCTbnUEXzmKksgd0rgGecmofyzSf8aV6%2BRPmWQ4vzE%2FzUeXl4x%2FaeRPf7PUWgMPl1ZRyNrkCxmuNc2Icvwvd6jmS2g%2BzNpnxShm7z5hJsl2BgkCAyDwVyNW7MkmdQizDh%2BBF90skukw9iD6AmjcSi0qxjSPbm4r15SBGm0T%2Bk%2BdsutW78fXDAdyGMC7scoJUMBnCF0yguiZrmfmAyoPx81nOllpOQerZNE3nvkj%2FqdH2xBQqfr3ME4PkBVjsZrqXcEvEju4hHnuvJ0IqpvVXH9X%2FmvfWVakA3SqoaoKBQYHFIXxSQiE6NPEv1pCRvQTD%2F2fexf96lpZt6xSG7tiKSZsDzuAKyVCrEwhrv%2F0gY6pgFX8X1M2y8fOTP9SRUw7DI6Ytgo7Uc3Be4HrzmKswveiqblSEcokfW8wnkrIexKNAhNXVvegA7z0egRb8IYMF24kYSQHAt0bIB7WGDpWaIlYw2aFKxLodHxL7GvcAjUBWTZNlmQYlM49AgixueNWe%2FjBiaNQQ28Rg8YmrAHMCBwAPslqhLSraxW3eDyOocOpi1fIyvinhvD0OTHLlbo4lIeEZmhEq9j&X-Amz-Signature=2f4418b34d5d1a3903a66e99869587a8a2e7a8c729346952b1b00cd72bb7ea88&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

[image](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/a8bbb04a-0804-412a-8936-775f7e304a2c/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RTSCJAMT%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T225059Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIG79phBSq%2FUS4EpuSo9IZPFaZqesQQLbf9Yx5PzTibOoAiAI8X%2BqGvc4mwY7OPmPH9hQK9oARRHq%2Fv%2F5GpTtz0lxjyqIBAjG%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMljAb4MuYWyfU5yUXKtwDHBcs2np7CMRv9HRvelj0f1bemBWqmS%2FCUf%2BZy4HV46ju3auKc1n%2FDzSWI9X4H8pUTN1RUsjB9Iz2707TpVLk2EkHQFqPofwny0ev5%2FzV7BwY%2F25JzacGM9xAzlFj%2BW7i4HxYInEew7phwc1a2KvjggWfzowbSSXmEmZ88RMs8WMPTXlBZoReFRb%2BEUkjq%2FFgcPlIjUa%2FixsFVLao944gIsHmilcyKc3xkadAAlSbOjz5%2FkrV%2BJUFm8GQNU21n7SYFwNGysILU2H70uprtakpUvo%2F0vdCTbnUEXzmKksgd0rgGecmofyzSf8aV6%2BRPmWQ4vzE%2FzUeXl4x%2FaeRPf7PUWgMPl1ZRyNrkCxmuNc2Icvwvd6jmS2g%2BzNpnxShm7z5hJsl2BgkCAyDwVyNW7MkmdQizDh%2BBF90skukw9iD6AmjcSi0qxjSPbm4r15SBGm0T%2Bk%2BdsutW78fXDAdyGMC7scoJUMBnCF0yguiZrmfmAyoPx81nOllpOQerZNE3nvkj%2FqdH2xBQqfr3ME4PkBVjsZrqXcEvEju4hHnuvJ0IqpvVXH9X%2FmvfWVakA3SqoaoKBQYHFIXxSQiE6NPEv1pCRvQTD%2F2fexf96lpZt6xSG7tiKSZsDzuAKyVCrEwhrv%2F0gY6pgFX8X1M2y8fOTP9SRUw7DI6Ytgo7Uc3Be4HrzmKswveiqblSEcokfW8wnkrIexKNAhNXVvegA7z0egRb8IYMF24kYSQHAt0bIB7WGDpWaIlYw2aFKxLodHxL7GvcAjUBWTZNlmQYlM49AgixueNWe%2FjBiaNQQ28Rg8YmrAHMCBwAPslqhLSraxW3eDyOocOpi1fIyvinhvD0OTHLlbo4lIeEZmhEq9j&X-Amz-Signature=f01d5f7c9fe5736081650038c9b34604cc7a3426aae1f48b038f74b6ac5313e2&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

本身就是当天基础 7 分管理，很多时候就是像。准备这个管理上。


唉，继续看我们的这个内容，刚才我们是把这个微博完成了这个第一版，然后我们把它保存起来，咱们现在再来做一个版啊。
好在第二版里面我们刚才已经讨论过了，我们要做一个重要的改进。嗯，就是要把那个微博，就是我在我的主页现在已经不存在了啊。
如果要把在我的这个主页我看到的这个内容，嗯，由这个推模型改为这个拉模型，该怎么来操作？同时我也给大家分析了，就是说你拉取过来的这个信息其实在一定的限度内，也就比如说 100 条或者 1, 000 条， 1, 000 条，像刚才我们看新浪微博，其实 1, 000 条就够了啊。所以我们该怎么来做这个工作啊？我们在那个剑的设计上，我们在哪做改进？


在这个推送表里面我们要给它，那么我们这个推送表就不要了，就是说这个人他需要看到哪些东西？他还是得有一张表来维护，这个没问题啊。我们比如说再来一个拉取的表，拉取的这个表这就意味着呢？当你发一个微博的时候，你发出来就行了，你不用再推给你的这个用户了，但是这个用户登录的时候，他要从服务器端拉一些信息过来，这叫poop，总说拉容易引起歧义啊。好勒，我们这个地方给它改名，比如说叫破拉取过来的这个信息用什么格式来给它存储呢？我们依然是用这个，用链表来给它存起来。

[image](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/a5dec991-aa6e-43fd-b764-40f48e1761f5/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RTSCJAMT%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T225059Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIG79phBSq%2FUS4EpuSo9IZPFaZqesQQLbf9Yx5PzTibOoAiAI8X%2BqGvc4mwY7OPmPH9hQK9oARRHq%2Fv%2F5GpTtz0lxjyqIBAjG%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMljAb4MuYWyfU5yUXKtwDHBcs2np7CMRv9HRvelj0f1bemBWqmS%2FCUf%2BZy4HV46ju3auKc1n%2FDzSWI9X4H8pUTN1RUsjB9Iz2707TpVLk2EkHQFqPofwny0ev5%2FzV7BwY%2F25JzacGM9xAzlFj%2BW7i4HxYInEew7phwc1a2KvjggWfzowbSSXmEmZ88RMs8WMPTXlBZoReFRb%2BEUkjq%2FFgcPlIjUa%2FixsFVLao944gIsHmilcyKc3xkadAAlSbOjz5%2FkrV%2BJUFm8GQNU21n7SYFwNGysILU2H70uprtakpUvo%2F0vdCTbnUEXzmKksgd0rgGecmofyzSf8aV6%2BRPmWQ4vzE%2FzUeXl4x%2FaeRPf7PUWgMPl1ZRyNrkCxmuNc2Icvwvd6jmS2g%2BzNpnxShm7z5hJsl2BgkCAyDwVyNW7MkmdQizDh%2BBF90skukw9iD6AmjcSi0qxjSPbm4r15SBGm0T%2Bk%2BdsutW78fXDAdyGMC7scoJUMBnCF0yguiZrmfmAyoPx81nOllpOQerZNE3nvkj%2FqdH2xBQqfr3ME4PkBVjsZrqXcEvEju4hHnuvJ0IqpvVXH9X%2FmvfWVakA3SqoaoKBQYHFIXxSQiE6NPEv1pCRvQTD%2F2fexf96lpZt6xSG7tiKSZsDzuAKyVCrEwhrv%2F0gY6pgFX8X1M2y8fOTP9SRUw7DI6Ytgo7Uc3Be4HrzmKswveiqblSEcokfW8wnkrIexKNAhNXVvegA7z0egRb8IYMF24kYSQHAt0bIB7WGDpWaIlYw2aFKxLodHxL7GvcAjUBWTZNlmQYlM49AgixueNWe%2FjBiaNQQ28Rg8YmrAHMCBwAPslqhLSraxW3eDyOocOpi1fIyvinhvD0OTHLlbo4lIeEZmhEq9j&X-Amz-Signature=ce8c0f46c451cdf94e15b0191bf705a707eadb9a3054f556b96ab771c7fc53bd&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

用链表给它存起来，但是说起来好像是和刚才没太大区别似的啊。嗯，我感觉只是你登录的时候在 home 的页面把这给它沿着，把你的每一个就是关注的人，把人家的这个头几条信息给它取出来，形成一个链表，这不就行了吗？但问题是有几个问题需要有几个小小的问题需要我们去解决啊？我们需要把这几个问题给它解决掉才能完成拉模型问啊。比如说上次我拉取了这个，我的这个关注的人a，他的这个567，三条信息、三条微博。哎，我给他拉取过来了，下次我一刷新那个 home 点PIP，下次刷新 home 点 PIP 肯定得从这个8，得从大于 7 的这个微博开始拉取啊。


也就意味着你拉取一次之后，你得有一个标记，得知道你上次你有这个 2, 000 多个关注的人，你上次在某一个时间点，就这时间 t 这一刻你拉取过来 10 条，又过 20 分钟之后你再去拉取的话，你得有一个明确的点，从哪开始拉取吧？所以我们需要维护一个东西，就是什么呢？我们可以维护一个时间点，比如说就叫 last pull，上次拉取的时间点，我们下次再来去拉取的时候，就专门挑那个发布时间大于我上次拉取的那个时间点来拉取，可以，可以拉取多少条？比如说我们每一个关注的人，我顶，就算他发布了新的有 100 条，我也不会取太多，我就取 20 条，那我们怎么来解决？就是说我们每次拉取时要设定一个这个 last put， last pull 时间点，那么在下次拉取时只取这个，它的这个时间戳要大于 last pod。


微博。问有很多关注人，如何取也很简单解决，就是循环自己的关注列表，挨个儿逐个取他们的新微博，再问取出来之后放在哪儿啊？答，就放在自己的这个 push Po，又到 ID 里的链表里啊。再问，再问就是如何像新浪微博那样，就是保证个人中心只有那什么呢？只有前 1, 000 条，那这个好办，这好办，就是我们只需要用那个 link 的 trim 给它去掉切这个 1, 000 条以后的，或者说 l trim 这个只取前 1, 000 条，多余的我们自动就给它去掉好了。


那现在经过我们的这个讨论，我们基本上讨论出来这么几条，但是还有一个小小的问题。嗯，你有两，你有 5 个这个关注的人， 5 个关注的人，我从 a 里边取了三四条，从 b 里边取了最新的三四条，加起来有七八条。这七八条得按什么排序呢？肯定得按发布时间来排序了，也就意味着这七八条这两个人取得七八条有可能是交错的。你不能说先把 a 的三条取出来，然后一下子显示完，再把 b 的 3 条取出来，一下子显示完。因为他们俩加起来的这六七条有可能时间上有一个交错关系吧。所以我们要把这六七条微博要给它交错开按，那既然要交错就得按时间来排序，也就意味着我们还得按时间来排序才行。


按时间排序我发了一条微博之后，我是写到一个，就是写到一个这个那个哈希结构里面的。但现在问题来了，哈希结构我不便于给它排序，还得再问。如果我关注a、 b 二人，然后从两人中各取 3 条儿最新信息，各取 3 条最新信息了啊。再然后，嗯。这 3 条信息，这 3 + 3 条信息就是从时间上是干什么的？是交错的，从时间上是交错的，所以如何排序啊？那问如何排序？如何按时间给它排个序呢？怎么来解决这个问题？因为我们发布时是发布的，这个发布的微博主内容是一个哈希结构，时间是体现在哈希里的，因此我们没有办法利用那个时间来排序。


嗯，怎么整好？不能按时间来排序。所以在发布的时候我们还要再多增加一个东西，还得再多增加一个东西。那么解决就是在发布一个微博的主内容的时候，还应在发布，在同步维护一个什么呢？一个这个排序表，一个有序集合，一个有序集合，一个有序集合。 post ID，你说你的意思是说 post ID 是越来越大的，是不是这个意思？但是时间上你怎么把握呢？就是时间上，因为它不体现时间微博的大小，我想我上次比如说这个a，它有 1- 100 都是 a 发的，我上次取到 100 了，我下次再来取，我得取 100 的这个时间点，以后的这些微博 launcher 上色扩展系统，去 POS ID 以后的可以，但是这样的话我有 100 个关注的人。


也就是说我取a，它是我取到 a 的，上次我是取到 a 的第 100 条微博了， ID 是100，取 b 是取到 130 了，这就需要这个思路，也可以，这就意味着我有 100 个关注的人的话，那么我取这 100 个人，我要维护 100 个取出来的那个ID，是吧？就是说我取a，我上次取到 100 了，取b，我取到 130 了，取c，我取到 150 了，我把这些记录我要都给它记录下来。然后下次再取的时候我取a，我从 130 以后取，还是一个时间点，就是 POS 的ID，我感觉 Pod ID 它和时间是对了的。嗯，时间是什么？还有 POS ID 都是这样吗啊？对，然后按照时间是怎么做的？就是套路 ID 完全可以和它一样。


它体现的都是一个有虚线，所有的用户之间所发的微博，这样画个图来试一试，来，就是。这是一个数轴，比如说这个用户他发的，他发了这几条，然后这个用户发了，是这几条要错开，错开，错开啊。上次我取到这了，下次取这三条，对吧？如果他还有一个关注的人是在这的，在这下一个人就在这，下次我就从这直接取，也就是说循环我所有的关注的人就取比上次那个 post ID 大的，是吧？就取比那个 POC ID 大的。只不过就是说他在这个时间点以前，如果后来关注的话，渠道后关注的人，如果他之前在这个时间点之前发的。
是的，是这样的，你在微博上你新关注一个人，也只能从你的关注那一刻开始起，他才能不断看到，就是你关注以后的内容，这个逻辑上也没有允许这样啊。好，那你的意思就是说因为所有的用户在时间点上它的微博的这个 post ID 和时间也是，就是说一个相当于是正比关系，对吧？嗯，这样的话我们不记他上次同步的时间点，而是记他上次同步的那个 ID 在下次同步的时候，我循环我所有关注的人，我就把那个比这个 ID 大的那些微博我给他拽过来，可以是一个好办法。那我们就这样啊。


解决，我们在这个同步时，我们在同步时，嗯，取这个，取微博后，然后干啥呢？嗯，记录本次取好，记录本次取得的微博的最大ID，然后下次同步时，然后只取比这个最大 ID 更大的微博。好。那现在我们就要来重做一下这个功能。主要还是在 pose 的这里要发生变化，首先把微博推给自己的这个粉丝，不要再推了，不要再推了，这个地方把它屏蔽掉，不要再推了，既然你不推了，那是，嗯。这个微博信息怎么样得到呢？我们来到 home 点PIP，也就是说关键的这个问题来到这个 home 里了，现在我不取出自己在这个粉丝推过来，这个粉主推过来的信息了，而是主动的去取。所以你看刚才是我们 for 一写自己的那个粉丝，挨个去推，现在要反过来，要循环谁，循环自己所关注的所有的分组啊。所以我们就得降来做了，在把它屏蔽掉，那我首先要把自己的那个关注的那些人，我都得给他知道才行，都得给他知道我关注了哪些人，我关注了哪些人。嗯，那是怎么来写的啊？我关注的人那属于到了饵get， get 谁来着？那个键值结构是怎么样的啊？我们要去看一下。cost。


我关注的人是在 following 好， following s member。来在这里。
首先啊。嗯，获取我关注的人是一个集合，因此我们用 s members，然后 k 是谁？ k 是那个叫我关注的人，是 follow in following 冒号，然后我的 user ID 就是我关注哪些人，然后点user。有的 ID 好，比如说我们把它叫做。star。我关注的人都找到了，然后 star 我还得看，我自己发的我也得能看见啊。也就是说还要把我自己也加进去 user ID 好了，我关注的人都已经找到了，那我现在我就得同步了，我就得同步，也就是要拉取数据了。拉取数据，要拉取的话你就得这么来 for each dollar star as dollar s。比如说，也就是说你所有关注的人，他们的 user ID 你都知道，然后把他们的要满足什么条件的给他拉取过来。


第一我们维护了一个上次拉取的最大的那个 POC ID。其次我们还得是属于我们关注的这个粉丝，我们想一想我们关注的这个明星，我们想一想怎么来做这个工作最省事。我们要循环的把这里边的每一个人。


来保存，看一看 v i m post 来看看我们发微博的时候发生了什么？发微博的时候我们是这样来发的。有一个 POS ID，有一个 user ID。
似乎出问题了啊。大家来想一想，我要取我关注的那些人发布的那个微博，但是你看出的是啥问题啊？出了啥问题？这个 post 的表里面我们就光放了一个 post ID，这你怎么区分呀？是吧？你怎么知道这个 post ID 是是你的这个关注的，是你关注的这个人发的，那你说这里边有 user ID，但是它已经被我们写到一个哈希，一个结，哈希结构里边被我们写到了一个哈希结构里，所以想一想这怎么办呢？因为每个人发的我们写成哈希结构了，我比如说我现在我就要取这个人连发了 10 条，我就要取前两条，前两条我也不知道。它这个用户 ID 是5，我要取 5 号用户的最新发的前两条 post ID 是有的，怎么样？根据 user ID 等于 5 来取。


林工达，你想一想。嗯，对，只能在发的时候我们必须储备用来排序，就这周排序或者时间就是都可以在只有排序。对，就是要他排序，就是要让他帮我排序，我要维护一个。嗯，不用 post ID 做统一标识和用户的 ID 和 post ID，就用户 port ID 对于每个用户来说都是统一开始的，对，这样的话 port ID 不会很大，就是每个用户都有一页 post ID，然后不，这个 post ID 是对所有用户都共同增长的，但是这样的话客户 post ID 会很大。


就是它如果超出了 p 除以范围。
嗯，很大，那你大不了可以使 big int，对吧？ big int 都能存的，那个都能 64 位，都大的都已经是天文数字了，所以你就不必考虑它溢出的这个情况。而且我们现在使用的就是 post ID，是全局自灯的。
就是这个意思。


我们关注了几个人，他们发了微博，他们都发了自己的一列微博。我们现在要把关注的这些人的这个微博前几条，我们要挨个的给他们拿出前几条。


拿出来就是我关注的人我能找到，但是我关注的人发的这个微博不好找了，所以这时候我们可以怎么办呢？我们完全可以，他们发一个微博的时候，我给他写一个这个 post ID 在这，pose， ID 在这。就是我把他发的那个 post ID，这个人发的 post ID，我给它放到一个集合里。


我的这个 a 号粉丝他所发的微博都在一个集合，微博的 ID 都在一个集合里放着 b 号粉丝， b 号这个关注者，他发的微博也都在一个集合里放着。c、d、 e 依次同理。所以我完全可以把它放在一个集合里，然后排序了之后，我就拿比我上次取的那个 ID 更大的那些，这不就行了吗？好，如果你嫌那个集合排序的功能不够强大，我们还有一个叫做有序集合的概念，有序集合、无序集合、有序集合。
好，有序集合，有序集合的操作很方便。来，那我们现在就应该得再维护一个东西了，得再维护一个有序集合。你每发一个微博的时候就是用 ZI 的key，然后 score member，那我就得这么着来写了。


不推给自己的粉丝了啊。把自己发的。微博啊。维护在一个有序集合里，而且这个有序集合还不用特别大。有个 20 条、 100 条就足够了，因为我们刚才说过，就算你三个月不登陆了，你的某一个，你关注的某一个人都已经发了 1, 000 多条了。但是没关系，我们只要他前 20 条，只要它前 2 条。因此我们来，我们，我们这样来操作到了r，然后 z 挨着 z either。然后这个键要好好设计一下。post。


用user，然后冒号， user ID，然后再冒号，再冒号。在冒号，那就是自己。到了 user 点 user ID。你看自己发的微博要维护在一个有序集合里。好，我先把这个 k 给它写好，也就意味着我们想取谁的那个微博的前 20 条的时候很方便，我们只需要通过 user ID 然后加它的那个值再取就可以了，这是k，有了，然后我们还需要给他发这个两个东西，就是一个它排序时用的那个叫做分数，其实就是排序的那个因要素SZADD。


key are 影响它权重的那个分数我们用什么来表示呢？我们就用那个 post ID 来表示，就用 post ID 来表示，然后它的值是多少值还是 put ID 来表示啊？然后我们只要前 20 个，就要前 20 个，为什么就要前 20 个呢？因为这 20 个就是为了让他的粉丝拉取信息用的，我没必要维护太多。


你要是好几个月都不上微博了，那你看到的也只是我发的前 20 条而已，所以我们只要前 20 个，因此我们可以再给它做一个操作 dollar r，然后我们要给它删掉一些，来我们这个有序集合里有一些好用的东西。 k member 一 member 2，好，我们先给他排序，再删除 they remove。


好，在这里 rank z remove rank 也 rank 按排名删除。太好了，我们就要这个 z remove range by rank 按排名删除， start 到。嗯，我不要删除，我要取出，我要取出，就取出第0名到第 19 名，因为它是从第 0 名开始的，咱们看看有没有比较好用一点的这个函数？
RIM key 是破壳， ID 是不断变动的符号， count 是属，不要是 run 念倒叙排列后 they score 我们只要钱 20 条。嗯，此处想一想，用这个有序集合是否是最方便的选择？


hey，此处我感觉此处我认为用有序集合，而且维护的这个 score 和 number 还是一样的啊。我觉得这个地方用有序集合并不是最好的选择。我们改个名字按叫 start post，这样便于区分，就是星星的发布。 start post ID 这个地方用有序集合并不是最合适的选择。我们用什么呢？我们用链表，我们把最新发布的，我们给它 l push 过来，然后我们再 l trim 它，也就是说我们把这个最新发布的维护在一个链表上，我都是塞在最左边的这个链标的，这个链表的最左边塞进去，因此它本身就是一个有序的，对不对啊？
来这样来操作， l push l trim 多少？ trim 是 0- 19。


star post 冒号 user ID 冒号刀了点儿。 user ID 019 那你看每个人发了微博，立即把他的微博的那个 ID 写到了一个相关的链表里，而且这个链表就存 20 个，这样的话他的粉丝再过来抓取的时候就方便多了啊。因此我们再一次回到 home 点 pip 里面， home 点 pip 里我挨个的抓取自己的这个关注的这个新所有的star，也就是分主我关注的关注者里面，我挨个去取。好，那我把他们的 user ID 拿过来了，我只需要这样来操作就可以了，挨个的去取，再一次维护一个集合 sample Temple。嗯，思考一下这个业务逻辑啊。我关注的人每一个人都有一个链表，维护着他们最新发的 20 条，最新的 20 条。
现在我要把他们挨个。
取过来，放在哪？


学过来，放在哪，也就是说我们打开微博的时候，你这一页一页往下翻，大概是一共有 10 页，一共有十页，这十页存在哪？你看始终就 10 页，也就是说我们还需要为自己收取到的那些明星的微博还得再维护一张表，对吧？还得维护一张表， ah 还要再为他们维护一张表才行。这个表得按照时间或者 POS ID 来排序，因此我们看看这一次，看看这个普通的集合能不能排序的集合。
ice ring。


集合 move 原字形操作pop。
但是集合不能帮我们排序，也就说我收到的这 1, 000 条微博，我该怎么来存储它？又是一个难点，再把这个要是再解决了，问题就不大了。我们收到的这 1, 000 条微博，刚才我们讨论过，有可能是从好几个明星拉取过来的，因此这几个拉取过来这 1, 000 条之间还得有一个排序关系。


那用什么呢？用链表还是用有序集合？还是用什么？
好，不考虑太多了，先用链表，或者是先用游戏集合，先给它做出来再说。 z 爱的这个 s 维护了一个链表，我们要把 s 的内容前，因为它始终只有 20 条。


我要把它内容取出来，嗯，而首先是。
这 20 条还是有难度，就算里边这有 20 条，你取到哪一条为止呢？你取到哪一条为止，是吧？你取到哪一条为止？新的你得有一个记录，对吧？就是说我们刚才所讨反复讨论的那个最大的 pot ID 来做区分的问题，所以要这么一考虑，这么一考虑还真怪麻烦，还真会麻烦。


再次来到这个 pot 里，也就是把自己维护的这个东西发了微博，放在链表里，要是放在链表里的话，比如说链表里有从 1 到 20 这 20 个微博，我要想判断取第几条，那我就得循环这个链表了，是不是我的循环到底取到第一个可以吗？第二个可以吗？是不是大于已经小于这个 POC ID 了？英母应该取了，所以这个比较麻烦。所以放在列表里只放前 20 个并不是一个好的选择啊。我们反复的来。选一下型。还是得给它扔在这个有序集合里，因为有序集合的话帮我们操作前几名还是比较方便的，比如说我就取那个前三名还是比较方便的。还是改改。 z i 的 Dollar post ID。好，这是一个游戏集合啊。这个有序集合我们要把前 20 名给它保存起来，所以我们只需要再找一个合理的函数，把它排好序之后的第 0 到第 19 名，我们给它拿出来就可以了，再把这个问题给它解决掉，来找找有序集合。有序集合。要找删除的，这个 RAM 不行。
they 软件不行。


they run it by stop。 Ray run it by score revenue Bison car。
i scope 取多少名？下来官方找一找有没有特别合适的这个有序集合的操作？
commands title sort of setters they add Belle。


不要 think by Belle the interstore will running return a running 表 they run 也 bison com 表 they rank determine the index。
利润没有美润 by rank 这个有希望删掉第0名和第一名，然后只剩下 three 了。 they rain by rank 它是从小到大闪，而我们留的就是，而我们保留的就是要保留那个大的值比较大的，因为 post ID 越大越新好就是他了啊。咱们的问题能够解决好，我们只需要做一个判断。唉，好了，男性的问题可以解决了。只要前 20 个我们这样来解决，我们先判断一下到了r，然后 z cut， z cut。我们判断一下这个人的那个就是有序集合里是不是已经超过 20 个了？我们这样来操作， star post 冒号 user ID，然后点 dollar user，然后 user ID。好，我判断一下它的值是否大于20。好，如果这个值要是大于二十大于 20 好办，我就把掉最旧的那一条删。怎么来？删第0名到第0名，我们要删第0名到第0名 z rim 软件 by rank key starter stop 好，我就要删第0名，第0名也就是把最旧的一个删掉啊。那我只需要这样，到了耳，然后 z remove run 也 by rank。 z 蕊木 run 也 by rank。
人物 run 点 by rank key。第0名Dall。


好，把这个 k 拿过来。 star poster 冒号 user ID，然后点 dollar user，然后是 user ID。好， k 拿过来了，然后说我要 remove 它的第0名到第0名，也就是把最旧的那个微博我给它删掉。好，那现在就达到一个什么效果呢？我们每发一个微博，我有一个有序集合，就存了我最新发的前 20 条，那么剩下的工作就该谁了呢？就该我的这个粉丝来工作了，你粉丝你过来抽取我的数据就行了，反正我有最新的 20 条公里抽取。


好，那我们获得我每一个关注的这个star，我能取得他们的 20 条，我并非都全要，我只要那个我之前没有取出来的，所以。
这个地方要做一个判断，叫做 laster 后，上次抽取的，上次抽取怎么抽取？ get 一个值， get 谁？ get last pull 上次抽取，然后 user ID，然后点 dollar user 下面的 user ID build ID。这个案例好。如果要是 last pull 飞针，飞针，如果要是 last pull 飞针，那我就dollar， last pull 等于0，也就最小。


注意，假设我们所有这个关注的人，他们的这个信息都拉出来完毕，都给它拽取出来，完毕这个地方要更新 last pool，更新 last pool，一会咱们要做这个工作，所以现在咱们就把核心的经历，把所有关注的这些人，他们的那个 20 条，每一条的那个有序列表咱要给它取出来，所以来取，咱要按照什么取呢？要按照那个 pot ID 的大小来取，我们看看这个有序集合有没有给我们提供按照范围来取的，来好好看一看。为 run 减 by 死 car they ran 检 by score。诶好，按分数升序排序取多少到多少之间的值，还有 limit offset count。我不要这个。
range key SATR 多少名到多少名之间的值 key 多少区间到多少区间的元素的数量，不要。 case com。倒叙排列后 starter 找多少直接的值，我想要的是根据那个什么呢？根据那个 post ID，某个区间内它稍微符合一点啊。


类 remove range by rank key。好，就用这个 rank 来取，就用 rank 来取去排名。 z 软件 buy score，但关键是这个最最最这个 mini 我们知道mini，你不就是上次我那个得到的那个结果吗？但是 Max 我怎么填？ Max 我们只能给它填一个巨大的非常巨大的一个数字了啊。好来取得动手这个地方啊。我们用 they run your bison call z they run 你 by score they run by score。然后 k 是谁？ k 是 star post，然后冒号 user ID，然后冒号冒号。谁冒号刀了s，冒号刀了 s 到了 s 我要取多少到多少之间的这个值？k，我知道了，取 d 取这个 last pool 到多大呢啊？到这个，比如说 2 的 32 次方。


这么大减一，其实应该，如果是真正微博系统得比这个大的很多，得 64 位甚至更大，好，就取这个范围内的这个值。然后我们立即就把它打印出来，看一看到底是一个什么样的效果才可以啊？我们现在的整体思路是这样，你的关注的人每发一个微博，就立即把它写到一个有序集合里，然后他的粉丝在挨个的挨个的取粉丝，挨个的取web。


好宇航，嗯，我有一个关注，再加我自己是俩人，然后我分别去取这俩人的这个发的微博没渠道，正常的，因为咱们改版之后还没有再发，这一次我们是用日有序集合来发的，看看能不能得到第四十三行。 yeah i m post 第 43 行 if z 少了一个小括号，刷新一下走好。得到一个8。要的就是他，就是要他的，我刚发的第8号微博有了，然后我关注的那个人在咱改版之后他还没发，因此这个是空的。好，这没关系，来，再接下来继续工作， home 点PIP，在这取出来。 8 号微博了，取出来之后 ill push。


拉取最新数据。叫latest， latest 等于一个a，瑞等于一个瑞啊。但然后每次取出来我就这样来操作啊。到了latest。latest。
等于 array 墨迹 dollar latest 这是要干什么呢？只是要把所有本次得到的最新的结果，我给它放到一个数独里。放到一个数组里啊。最后我打印这个数组，我来看一看。按一个速度在这里 PRINT 杠 2 打印latest。然后我关注，我再发一条，比如说叫。 they add two z and two 第二十六行，来帮我看一下。这个对应这个似乎多了一个吧。


好刷新， 9 也多出来了。然后我还关注了人，我关注的是 test two。 test two 也赶紧的去发一个试试。


test 1 好像关注的是 test 一，我也发一条 z either three 耶，刚才我是谁？ badcase 十八九。对的，因为他俩互相关注了，他俩互相关注。那我这样的，这样好，我们得到了这个10，这个八九十，这个东西正好就是我们就是说得应该得到的啊。嗯，我的主页应该看到的哪些微博的信息？但是我们光要这个数组还不够，我们针对这个数组还要再排一下序，还要针对数组再排一下序。然后针对数组排序之后，我们再把它塞到自己真正的就是那个接收的链表里就可以了。比如说就叫这个 receive post， see post 来排下去有点复杂。


thought 对数组排序，数组单元将被从最低到最高逐步排序，我们要反过来 sort numberic sorter numeric 好，就问他来 dollar latest 要再进行一次排序。 dollar latest 用 sorter numberic searcher numbric，然后再一次的打印这个lattice，看它有没有变化啊。那应该两个人看到的都是八九十才对啊。八九十。唉，好了，这个地方看到的也应该是八九十。


行了，现在我们就是说把自己关注的人，还有自己最新的那个微博，我们都给他取出来了，取出来了还不够，取出来还不够，我们得到的现在只是一个数组，我们呢。还要把这个数组放到咱们的这个 receive pose 里面去形成链表，然后后边就能和咱们这个之前所做的工作就能接上，就能对接成功了啊。也就是说我们现在还差一步，就是把这个八九十这三个单元我们给它写到这个 receive post 里面去。 receive post 是一个链表，好，来再把它往 receive post 里面写。 dollar r 到了r，然后往列表里面写，我们找一个看看有没有能一次性写一个数组的链苗是不对？


l range l pop 没有。
key value， ill push。
好，还有push，我们看看能否允许一次性多插入多个值，就是把我们那个速度直接给它插入进去。
这怪气人的examples。
还不允许我们一次性 push 多个。
ill push。


我们再把这个，只要再把这个数组给 push 到给想办法连到的这个链表上，那么就大功告成了，咱们现在再找一个再方便一点的办法，看能否把一个数组整体给它粘到一个列表上去。
ill push 不允许我们直接操作数组，挺让人失望。


be a pop prepend one of Multi values 一 Multi key noise 好，那既然不允许，那就算了。我们循环还是得循环好。再来一个循环，把 latest 放到自己，就是主页应该收取的那个，就是说微博链表里，然后我们 for 一切这个 latest as dollar l，比如说 as dollar l 然后我们只需要干什么呢？操作那个 receive post，我们只需要用l。 push 谁 receive post，然后冒号到了点 user ID，然后再来给他一个什么样的值给，当然是到了 l 了，循环的给它塞到最左边去，塞完了之后我们要就是保持个人主页至多收取 1, 000 个，至多收取 1, 000 条数据， 1, 000 条最新微博。因此我们再把他的那个遭了r，我们再给他 l trim 一下，依然是 receive post，然后冒号，然后 dollar user，然后 user ID，然后 0- 999999。他的主页上顶多有 1, 000 条，但是还差一点点更新 last poll，更新 last pole， last pool 不就是那个最大的那个 lets 里面最大的那个单元的值吗？所以我们只需要这样就行了。


更新到了耳，然后什么 set 什么？你的 last pole 放在哪的 last pole 冒号 user ID。好来。那应该这么着来写 last pull，然后冒号 user ID，再冒号，然后 dollar user ID，那它的值就是这个 Letis 里面最大的那一个，因为我们已经排了序，因此它就是最后那个单元的值啊。因此我们这样 letter latest 就可以了啊。


为了验证咱们这个 last pool 好不好使，我们应该做一个判断，就是这个 print 杠latest，我们看看到底能不能好使，咱看看是否每次收取之后，下次就不再收取了啊？来，我刷新一下那 z at three， z at three 这地方是八九十，收取了这三个。没问题，收取这 3 个，这个 last pool 就已经更新了，如果我要再刷新一下的话，它就应该是收取空数组才对了，对吧？好，应该是收取空数组才对啊。然后这个地方很奇怪，不仅没收取空数组，反倒又多了，是吧？看到没有啊？反倒多起来了，这个太离谱了，那我们检查一下这个逻辑上的这个问题，这个 last pole 是不是没发挥作用呢？我们有必要来看一下。


好，那我这么理，这么理connect，再连一下 CD user local Redis 点儿 binary Redis CLI 连上。我是 ID 是一， ID 是一。来，我得这么着，我得 get get。谁 get 那个 last pull 冒号， user ID 冒号一得到一个 10 没有问题，意思就是说你刚才已经收取到 10 了。好，那这个 10 明明有来，我们就得找到这个页面，好好看一看喽啊。好好看一看了。如果飞针 last pod 等于10，然后 z range by score z 让你 by score。就这里有鬼。


这里就不应该再能收到，所以我们再来判断一下 z 软件 8S call 有没有出问题啊。好，来看一看。 they run 也 by score， they run 也 by score。然后那个叫 star poster，然后是冒号 user ID，然后冒号一我就取我自己的 z run 减 8 s call they run it by s c o r e z 软件 by s call 嗯 u 的 ID 冒号一，然后一。
when you buy score。


十一百1919。9919。 1919 取出来了，取出来是对的，这个业务逻辑错在哪？这个业务逻。逻辑错在哪啊？这个业务逻辑错在哪？
这个业务逻辑是这样的，就是我们上次取到这是一个数轴，数轴上次我们取到第 10 名了，我们把这个 10 记录下来了，下次他从 10 名开始取，然后这个 10 包不包含，就是说这是大于这个10，还是正好包含这个 10 呢？就像我们在那个数学上说的是小于等于还是小于呢？大于 10 呢？还是大于等于 10 呢？导致的 z range 8 rank 这个东西，你给它的这个值，它是什么关系？是大于等于的关系，因此想改正它也很简单，我们这样来操作就可以了啊。这样来操作我们只需要把这个拉着 Po 略私小计，我给它加一个一不就完了吗？因为它是一 user ID。什么稍等，哪里？第几行？第 18 行。 last pull。搜嘎，这样它永远都是0，是吧？嗯，永远都是0，那即便如此，这个加一的问题也得给它解决掉啊。等于的问题，要不然他还是会有重复数据的。好了，然后我把自己的那个账目清空。


your team l trim receive post 冒号一 0- 1 清一下之后我看看现在轻的是不是叫什么名字啊？叫什么名字？叫 receive poster，这里看有的 ID 保存起来。这是好刷新。 receive post 倾向刷新一下。


好，现在这是不增长了。然后我们换一个用户，换一个账号，看看好 title 一 z add three 这没问题。然后再来一个 z either four z at four update 一下 z at four 好，也出现了，然后我再刷新还是 ZI 的four。一。然后大家观察还是有一点点的这个小毛病，就是似乎我刷新一下它为空了，再刷新一下又不为空了，这个业务逻辑又错在哪啊？你看这些代码主体不难开发，但是往往最细最那一点的细节上非常之复杂啊。问题在哪？问题在这，就是你如果本次刷新这个数组为空的话，就意味着没有什么好取的，没有什么好取的，然后你看我们更新谁呢？更新 last pool 的时候又是更新的latest，如果本次为空，那好了，本次为空，那你按的取这个空数组，那肯定是为 0 了，也就意味着数组一为空，你把拉特炮更新为 0 了，那当然不可以了，对不对啊？那当然不可以了。所以我们得做一个判断，如果这个速度非空，做一个判断就可以了，这是小问题。


latest 如果要是非空我才能去更新ah，我才能去更新这个 last pole 要是为空，说明你本次任何东西都没取到，那你还有什么好更新的啊？咦，稍等，如果不空， setter 好，刷新好， 123456789 好，一直刷新没有变化了。然后我再一次的 z either five z at five，好，我再一次更新 z at five，好，再刷新，哎，你看我刚发的时候是显示说，唉，你当前需要更新13，一旦更新完毕之后你再刷新就不需要了，数字就为空了。好，现在这个逻辑就没有问题了。然后我们回头把刚才那两个人的 receive 好，我们给它删掉。链表。
ill rain 删了， 2 号用户的删了， 3 号用户的删了啊。好，现在他的这个，咦，怎么没删掉？
oh 还有train。chain。随便来一个21。okay。


我要删清空这个列表，怎么还翻来覆去不让我清空来看看 receive post 冒号 user ID 没问题。 receive post 冒号 U1 我是 1 号用户，我要删我这个所有单元来，还出这样的怪事，我要删还。咳，找 l link，找 link 操作。


ill rain l rim 不能用它 l trim 剪切，左手从 0 开始，右手从- 1 开始。 l trim 零零什么情况？是啥？怎么这么顽固？ utid 等于 1L ran 捏瑞好连续开发了，连续敲了一个多小时，这个眼睛已经不够使了，大家看， receive 弄成了 re v c receive post 说怎么回事？这不好使啊。好啊，那现在空了啊。然后我们把这几个人收到的微博都先给它清空，也就是本页面的都要恢复一个初始状态，都为空了。然后我们再来发誓一试，我是 test 一，我说，hello。验更新一下，这是我发的，我能看见，没问题，我发的，我能看见。然后我们再用另一个页面，噢，先刷新一下能不能看得到， 10 秒前通过 test 一发布，没问题啊。然后我来那个 hello test 一，然后我发的在它排在它上面没有问题。再然后我在这里也刷新一下，看能否接得到，也能接得到，没有问题，也是按时间排的啊。


好，在此处刷新一下。OK，那好了，那至此我们就把这个微博第二版我们就给它改造完毕了，这次我们用的是一个这个拉的这个模型。好，我们把它保存下来。


