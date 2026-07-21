---
title: 22-哈希数据存储微博
---

# 22-哈希数据存储微博

[image](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/fe95d09b-a956-4077-b879-a98648a6bdf3/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XENEDHLQ%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T225058Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIFXxC6d0lS5ux94PvJ1vS185rjFIdGUAOPaVSSp3oKP5AiEAkML7T%2BspY%2B0JqK0APvh9sTTHZpEvOzckgdoz0mJCmrMqiAQIxv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDAt46TledmJBNNHaKCrcA%2FlbcpFw8rDZ8qM51xw9oGlxNFPMI23ff%2BQ%2BGNQy%2Fm8NV%2Bs%2B8cmwy0Vrzb7PpxJd6uGrZckN1bJOvUMPJfe5ZkK5cX2aqsBt1DGz%2Fj7IjEQCCmLPqBjfAHMYHav%2BSev2l%2B9x8GLUyxnb2TzfDvRxLS7CKHe5kn%2BnQ%2BK%2FxQPbfyfFW0kA2ZSBNM1ep%2BdnUNshjFX7JkHGkDFkAXybmV8iWkxPwttXt2N5mSJuKdDnOHfVasm6WailtsuxOs1IB4gH4OGHsgpVGSpBoNKuZQ49rGJjMYkD%2BOyNKBejm0vdVANN5%2BKrkqwHIreYKCTVB1JIN5VXwGCVcscZBA9941aFlA%2B5ODBlPlIcD7dmSyjvG3nkP0G2YG1Z0HfMttentwRXue0bjrvBadUSX7l2d95HOt%2F3e3%2FvbdLYHckkFzl5N5nnhHQTB0cMUwOmROPkmD%2FjQPc%2BIxiT4crW9Z03UbB2%2FTUaf74H%2BdWLqBUyOABHB7E3bngM7%2FaKuOIezk7WOSC3m3WAyTDcBIb%2FczntgiUySbINcxePwdY1YCxx%2BcahOLFxM6trdG0pMzqnitXWUTjc9PBb7wM6BS0YcmNZPP9YwRgZSlyPANXSKjygRD6UM6J%2Bs3YY34eCbxon2n%2F%2BMMy3%2F9IGOqUBXDDtmmn7rQxQvrLbZ241DHZpdGOeW%2BhIDm2%2BbVRdjraFPwkuHbeh2wzkLZAPifmOhRFbF9ReQTmi%2Fq7ZJKAAilcjxYCZQJ57%2B78E4Pbp6s2BVVGTQP46PGyvZX5kVt62NJmxTbQsks0wIc1%2FEsNkL0yCzKHcPtgyXPfvMzqlad3PATNZH1qQF%2BVH5%2Bog0GP55IiQhTsSVPru6WafumaA%2BxXtH04Y&X-Amz-Signature=b0844a5e3b59c4d06f8473c8caba29593259b93d3a9ee923962bc6472fedbb7b&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

[image](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/e5534929-3ba8-4543-912c-dc98125c8dbc/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XENEDHLQ%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T225058Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIFXxC6d0lS5ux94PvJ1vS185rjFIdGUAOPaVSSp3oKP5AiEAkML7T%2BspY%2B0JqK0APvh9sTTHZpEvOzckgdoz0mJCmrMqiAQIxv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDAt46TledmJBNNHaKCrcA%2FlbcpFw8rDZ8qM51xw9oGlxNFPMI23ff%2BQ%2BGNQy%2Fm8NV%2Bs%2B8cmwy0Vrzb7PpxJd6uGrZckN1bJOvUMPJfe5ZkK5cX2aqsBt1DGz%2Fj7IjEQCCmLPqBjfAHMYHav%2BSev2l%2B9x8GLUyxnb2TzfDvRxLS7CKHe5kn%2BnQ%2BK%2FxQPbfyfFW0kA2ZSBNM1ep%2BdnUNshjFX7JkHGkDFkAXybmV8iWkxPwttXt2N5mSJuKdDnOHfVasm6WailtsuxOs1IB4gH4OGHsgpVGSpBoNKuZQ49rGJjMYkD%2BOyNKBejm0vdVANN5%2BKrkqwHIreYKCTVB1JIN5VXwGCVcscZBA9941aFlA%2B5ODBlPlIcD7dmSyjvG3nkP0G2YG1Z0HfMttentwRXue0bjrvBadUSX7l2d95HOt%2F3e3%2FvbdLYHckkFzl5N5nnhHQTB0cMUwOmROPkmD%2FjQPc%2BIxiT4crW9Z03UbB2%2FTUaf74H%2BdWLqBUyOABHB7E3bngM7%2FaKuOIezk7WOSC3m3WAyTDcBIb%2FczntgiUySbINcxePwdY1YCxx%2BcahOLFxM6trdG0pMzqnitXWUTjc9PBb7wM6BS0YcmNZPP9YwRgZSlyPANXSKjygRD6UM6J%2Bs3YY34eCbxon2n%2F%2BMMy3%2F9IGOqUBXDDtmmn7rQxQvrLbZ241DHZpdGOeW%2BhIDm2%2BbVRdjraFPwkuHbeh2wzkLZAPifmOhRFbF9ReQTmi%2Fq7ZJKAAilcjxYCZQJ57%2B78E4Pbp6s2BVVGTQP46PGyvZX5kVt62NJmxTbQsks0wIc1%2FEsNkL0yCzKHcPtgyXPfvMzqlad3PATNZH1qQF%2BVH5%2Bog0GP55IiQhTsSVPru6WafumaA%2BxXtH04Y&X-Amz-Signature=eda81127524dd01c3de1ab1a2374f300ced8cefcce1e732e9d0c1278dce5c591&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

[image](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/075884d5-3bed-41f8-9e38-82f6f0c43684/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XENEDHLQ%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T225058Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIFXxC6d0lS5ux94PvJ1vS185rjFIdGUAOPaVSSp3oKP5AiEAkML7T%2BspY%2B0JqK0APvh9sTTHZpEvOzckgdoz0mJCmrMqiAQIxv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDAt46TledmJBNNHaKCrcA%2FlbcpFw8rDZ8qM51xw9oGlxNFPMI23ff%2BQ%2BGNQy%2Fm8NV%2Bs%2B8cmwy0Vrzb7PpxJd6uGrZckN1bJOvUMPJfe5ZkK5cX2aqsBt1DGz%2Fj7IjEQCCmLPqBjfAHMYHav%2BSev2l%2B9x8GLUyxnb2TzfDvRxLS7CKHe5kn%2BnQ%2BK%2FxQPbfyfFW0kA2ZSBNM1ep%2BdnUNshjFX7JkHGkDFkAXybmV8iWkxPwttXt2N5mSJuKdDnOHfVasm6WailtsuxOs1IB4gH4OGHsgpVGSpBoNKuZQ49rGJjMYkD%2BOyNKBejm0vdVANN5%2BKrkqwHIreYKCTVB1JIN5VXwGCVcscZBA9941aFlA%2B5ODBlPlIcD7dmSyjvG3nkP0G2YG1Z0HfMttentwRXue0bjrvBadUSX7l2d95HOt%2F3e3%2FvbdLYHckkFzl5N5nnhHQTB0cMUwOmROPkmD%2FjQPc%2BIxiT4crW9Z03UbB2%2FTUaf74H%2BdWLqBUyOABHB7E3bngM7%2FaKuOIezk7WOSC3m3WAyTDcBIb%2FczntgiUySbINcxePwdY1YCxx%2BcahOLFxM6trdG0pMzqnitXWUTjc9PBb7wM6BS0YcmNZPP9YwRgZSlyPANXSKjygRD6UM6J%2Bs3YY34eCbxon2n%2F%2BMMy3%2F9IGOqUBXDDtmmn7rQxQvrLbZ241DHZpdGOeW%2BhIDm2%2BbVRdjraFPwkuHbeh2wzkLZAPifmOhRFbF9ReQTmi%2Fq7ZJKAAilcjxYCZQJ57%2B78E4Pbp6s2BVVGTQP46PGyvZX5kVt62NJmxTbQsks0wIc1%2FEsNkL0yCzKHcPtgyXPfvMzqlad3PATNZH1qQF%2BVH5%2Bog0GP55IiQhTsSVPru6WafumaA%2BxXtH04Y&X-Amz-Signature=cfd66b3fb10106035e7f37bd7b5cbb918a975d82d7b5fddbaff13196afdd58e4&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

来，我们继续改进这个，咱们的这个微博的这个项目，刚才又提到一个地方需要改进。就是上节课我们所说的，嗯，微博的这个内容就是发布人以及他发布的这个时间我们没有没有得到。为什么没有得到呢？我们来看一下这个 home 点 p a p 发生了什么，我们是这样来做的啊。嗯，取出自己的这个微博，还有他的这个粉主推过来的这个信息，也就是说我们取了这个 49 条、 50 条出来， 50 条出来，然后取出他们的这个ID，然后来一个这个连接查询到这个内容 post 的这个content。因为我们是把那个微博发布时间，发布的那个作者以及发布的内容都是分成三个字段来进行的，所以导致我们现在是取出了内容。那你说我既然能取出内容，当然能取出发布时间，这样的话我们还需要再 sort 一下，也就是说我们为了取出这个 50 条微博，我们要分别取 50 个微博的内容、 50 个微博的时间，然后再一一给他们拼凑起来，这样就比较麻烦。所以接下来我们要改，要调整这一点。怎么来调整呢？我们来到那个发布页面，我们去调整一下啊。那大家看一看啊。在发布的时候，在这个地方我们可以看得很清晰。就是我们把它的嗯 user ID 单放起来了，然后把它的时间担放起来了，再把它的这个 content 也担放起来了。


现在就是这种方式还是有一点弊端的，我们选的我们取的时候取出内容倒容易，取出时间，并且取出这个用户来结合一下就稍微麻烦一点，所以这个地方我们怎么做好？这个地方我们给它改正一下，不，这就相当于什么呢？这就相当于把 user ID 一个字段、 time 一个字段、 content 一个字段都用 POS ID 做主键，现在我们要把它 user ID time 可能要绑在一块，那么我们用这个 Redis 很容易把它们绑在一块，我们知道 Redis 里面还有一个重要的结构，叫哈希结构。我们现在就用哈希结构来搞定它，那我们用哈希的 m 赛特。


好，那我把之前的这三行给它屏蔽上，我们用 m 哈希的 m set 键不变，然后 post 冒号ID，然后点 post ID，然后直是多少值是多少啊？我要给它传一个这个哈希结构过去，我们用 m set。
我们去找一下他的这个Redis。


来看一下它的官方文档，看看 PAP 的这个接口如何帮我们发送。嗯， IM set，阿西， IM set。好，在这，那先是一个k，直接再以一个关联数组的形式传过去就可以了啊。那对我们来说很容易，我们只需要这样就行了。k，我准备好了，那我后边我只需要这样写，我只需要来一个数组，就是user， user ID，对吧？然后 dollar user ID 是这样的，再然后是time， time 是当前的时间time，再然后是。 content 内容是 dollar container，好，现在我们是达到一个这样的效果。你发一个微博，然后产生了一个微博的主键，然后这个主键除了主键之外，第二个键是什么呢？第二个键是一个复合的数据，是一个关联数组啊。所以我们发微博之后啊。我们再来到自己的这个 home 页面，我们取的时候。


我们就不能再取它的这个 content 了，就不能再取它的 content 了啊。我们看看它的那个啊。来我们。
post ID 这个地方应该是星，好替换成星没有问题。哎，等等把这句话屏蔽掉，不能删。


好，我们再次 sort 取它的这个值，这次我们想应该取出来是一个关联数组才对，当然我们先发一些试一试。好，再发一个 from 哈希，好，我们来发布啊。发布好，这次更夸张，我发布是发布成功了，结果连内容都没有啊。为什么连内容都没有呢？因为这次取出来的是应该是一个关联数组的结构，我们不妨把那个 new poster 我们打印出来看一下就知道了。 new poster 走 01012 Yan 空的，我们来分析一下这个语句，我们执行的是一个 sort 获取它的内容。


get post ID。星来再去看一看刚才的那个页面，刚才我们改动过的页面， POS 页面，我们看看是不是两个的这个 k 不匹配，或者 post ID， post 冒号 post ID，然后 dollar post ID。好勒，我们来到这里啊。
好，这个 get 我先不要了。get，先不要。


好，543，这就意味着这三条微博，他们的这三条微博就是我想要的啊。那么我现在就要把这 3 条微博我给他取出来啊。那好办，我们这样来操作。


这个地方已经修改了，这一行是用这个哈希结构存储微波，存储微博，存了之后我们要把它做一个 for 一切循环。 new post，因为我们此处取出来的仅仅是他要取他要看到的那些微博的主键，因此我们还得再转个弯。把他们的这个微博内容都给它取出来，我们用这个 m get，哈希 m get，再来试一试。阿西 m get。这是 key 数组，还得循环。


new post as dollar post ID 到了 post ID，然后在循环的过程中到了 r 在不断的 m 哈希 m get 什么啊？首先要拼接那个键是 pose 的表下面的pose，这 ID post ID，然后是点儿 post ID，这是它的k，然后你要取哪几个这个列呢？你要取哪几个列呢？你要说清楚啊。比如说我要取这么几个列，一个是它的 user ID，一个是它的发布的时间，也就是time。一个是它的content。那取出来的这个结果我们不妨把它打印出来看看，应该是一个关联数组才合乎我们的需要。我用哈希 IM get 保存起来，也就是说我已经获得了 543 这三个微博的组件是我想要的，但是我得沿着这三个组件把他们的那个内容挨个给查出来，然后我们看一看是不是这个样子，一时间，唉，很好，就是我们想要的。那你说这条怎么不对啊？这是因为什么呢？这是因为之前的那个键，我们存的不是哈希结构啊。


好，那现在已经得到了我们想要的这个目标，然后我们在循环的时候在哪里循环？在这个地方循环的时候第 3D 好了，我们把这个 for 减循环移到哪呢？移到这里，移到这个下面的显示部分来 for 一起啊。好，我们替换掉这个 for 一起。也就是在这里。
此处我们给它换成 post ID，拿着这个 post ID 干什么？
把这句话拿过来。


好，取出来的这个结果是有 user ID、有time、有 content 这个东西，所以我们不妨把它给命名成一个这个数组，比如说到了p，刀罗p，你心中要清楚，这个刀罗 p 是一个数组，在此处这个 IQ dolly c 就不能再 IQ Dolly c 了，而应该是 IQ Dolly p 它的 content 这个 11 分钟前，这个也不能显示一个 11 分钟前了，而应该显示它的这个时间戳。


目前我们得到的只是一个时间戳，因此我们应该这样来做到了p。然后 contact sorry time 这个地方也不能再显示这个人家的用户名了，而应该显示。不能显示一个，而应该显示这个 Dolly p 下面的 user ID。好，来，又经过一次迭代，然后我们再次来看它的这个结果啊。好，哈希 to form，哈希没有问题啊。但是要是没有问题还是存在的，哪呢？大家可以看得到，第一就是这个 user ID，还是这个直接以数字形式体现的，这不太合理，得能把人家用户名体现出来才好啊。


另外一方面就是多少时间前通过 Web 发布，我们来看看多少时间前通过 Web 发布的？嗯，好，少了一个 Echo 来我们再来刷新，这是时间戳。所以我们还需要做两个工作，一个就是把用户名也显示出来，再就是把这个时间戳要给它格式化了，对吧？时间戳要给它格式化，就是能得能变成多少分钟前或者是多少小时前，或者是几天前发布的，这样才比较好。


ah，嗯，那怎么来解决呢？先来解决其中一个，就比如说把这个用户名换掉这个 user ID，换掉 user ID。好，我们应该从哪来？从来解决这个问题呢？应该从发布的源头就来解决，它就是说有了用户 ID 了，我们肯定是能查到用户名，但是我不希望你去查，也不应该去查，因为这个地方你想一想，我们直接存储的时候，如果多存储一个字段的话，虽然是多了那么一个字段，浪费了一点空间，但是我们查询的时候是不是就不用再左连接查询了？当然我是用了 MySQL 中的一个说法，也就是说我们在发布信息的时候，你多加那么一两个字段，那有可就是说你精心设计，故意的来多增加那么一两个字段，将会给你的这个查询带来几大方面。你比如说我此处有 user ID，我有很多场合光知道 user ID 还不行，我还得知道用户名。那你说我根据 user ID 我再查呗？查你当然能查到，但是你不麻烦吗？多查了一次，所以这个时候我们就可以顺手把它的这个存的时候，我们完全可以把它的这个 user name 我们给它存进去啊。咱把它的 user name 给存进去，我就往上找，看看它的 user name 在哪？ user name 是存在哪里的？ user name 等于 dollar user 下面 user name 好保存起来，我们网上找一找是不是有 username 那回事。 VIM label 点PIP，我们看看登录的时候是不是有 user name 登录。咦，我的。
VIM login。好的，视角游的 name user net。


老隔音。 VIM label 点 PIP 还得再找一找确认一下 e 的 log in 在这。我看看我返回的值，如果登录成功了，返回的值是什么？是不是叫 user name？哎，是好，是就好了，那我就可以放心的来做这个工作了啊。所以当我发布一条微博的时候，我就把这个微博的这个用户ID、用户名、发布时间以及内容，我都写到一个这个数图里面去啊。这样的话呢。那么当别人读的时候，就完全有能力只不通过这个 user ID 来获取用户名了，而是直接就能得到，因此我们这个地方可以直接 user name，这样就方便多了。


好，我们通过一个字段的冗余 she user name。好，再一次的把它保存起来，然后我们再发Hush， hush three，第三条 i see three harshy for，来看看什么情况，好，什么情况？在这里我们发这个微博的时候，确实把微博的这个 user name 给它发到 Redis 服务器去了，但是我们往回取的时候我们有没有？你看看这里，我们只取了 3 个字段，user、ID、 time 和content。因此我们还得在多取一个字段，多取一个 user name，好保存起来，然后我们再来刷新好了，这会就成功了啊。那么至此我们就把这个 Redis 的这个发布的这一小块我给它完成了啊。等等，还有一个小问题，时间戳格式化，我们希望能给它格式化成几分钟钱。


那这个问题好做，我们只需要再来一个函数就可以了。嗯，来一个函数，其实这个东西交给谁做比较好？这个不应该交给 PIP 来做，也不应该交给 Redis 来做，大家觉得交给谁来做最合理？这也其实交给 GS 来做最合理。对，把这个任务交给用户，因为在浏览器端你 GS 完全有能力算这个东西的，对不对？这样的话你省的服务器多一个负担了啊。所以就是说现在不是这个说，在服务端我们经常说MVC，其实现在这个甚至连前端都有这个 MVC 框架，别人直接给你一个阶层数据，阶层格式的数据，而且还是原始数据，剩的那些格式化的工作都拿 GS 在上面，这个在浏览器上操作，给你格式画出来。另一方面，因为现在的这个浏览器 GS 操作也越来越快，所以这个工作其实交给 GS 比较的合理啊。好，然后我们再来到这个 Libra PIP 里面啊。好，我们再来一个格式化时间， for matter time， format time。
好，给我一个时间戳，然后我要获取当前的这个时间戳，减掉你传来的参数。那不就是已经过去的秒数吗啊？秒数好，这个没有什么技术含量，就一直是 if else 判断， if else 判断啊。嗯，那我们这样来判断，如果到了 second 要是大于等于86400，这都已经是一天前发布的了，对吧啊？一天前发布的了，那我们就判断一下啊。到了second，然后比上86400，取得的是这个天数。flow。return。


几天前。否则 elseif 如果要是大于等于 3, 600，那就说明已经过去得以小时为单位了啊。那我们就这样 flow block，然后 second 比上 3, 600，然后点小 10 钱。小时前既然都有一个钱，那我就把钱去掉再来判断。如果连几小时都不够，那肯定就得用分钟来判断了。所以到了second，然后减这个 dollar 大于等于60。好勒，那我们就 return flow dollar second 比上60，然后是分钟啊。好，那最后一种情况连一分钟都不够了，就直接，嗯，返回这个秒数就可以了。


flow dollar second 海。 flow 什么呀？ dollar CK，秒秒啊。好了，那我们来到这个格式化函数，我们给它写好了，再来到 home 点 PIP 里面，我们只需要把这个 p time 传给 format time，由它来格式化一下就可以了啊。好，然后我们再来看这个是 20 分钟前通过 Web 发布 20 分钟前这个数据，这三个数据因为都是之前的格式都不对，所以产生了这个错误啊。这个没关系，我们看最新的两条几分钟前来发布的。好，那至此我们把这个微博的项目，这个第一个版本我们就给它做完了，那么我们来总结一下我们所做的这个设计。 Redis 在这里。

