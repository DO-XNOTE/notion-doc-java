---
title: 23-微博key设计总结
---

# 23-微博key设计总结

[image](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/2a4b1bac-f12a-4f62-9395-32db846d0458/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SIS67EM6%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T225058Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIGX08Lcwp%2BalWQKKBLMv6Zq7S0PzpjzhM7BSVOdLwHEuAiB1YZwdYd5qtItoWKX1y8P445w1mgKQfVJ32CzJT6Nn%2ByqIBAjG%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMT9YKSgkIr26CLac2KtwDu0M7KGiN0MHMUH2Z%2FdWOFYaM91i31Z51Hgr7k4QfafCJ5pSkSPyO%2B5dWpIR0FQ15rEzkLZ8t2XoMceSnxacWA24I1dCiICQ76BVXWRkJcluZXVDM3ss33%2FgSqVj1SncWVi6HQtfZlTr8jEc6M7RX%2FhsBgYOVImmVHeymqkH%2FhmwMaedyRqAkD7Qp47TnEYgLg56KtIfPktTZshG3Zkntg4tioXkfIocn1WZlXP2hu9XT2JcSPL7zCvk0u6ulQEcaYhBnirJTVYBjUOF82Gbi2G2MBjYrPypLi32v2q8gd1%2BpV71EdR3vh7vxSOV3kfpUjd5Fz3CxC09tO1dew2I7mfd3sUMtIv1OBEdR9tkiUJ3i8AsvsK69qHHhFs%2BK6bxAy6hiSGhSC9uarQo2SWbHXXlIJBWXvDcl28BPIk%2FTbIwAGYtgRoFB2UIOOqh7Iai3ikB4y7n%2B5jwMN6jIRJYioch%2BtfUqRD%2F2LStLBbUYaztYRtBRzkawl%2BDoAUk3YLQBEJoxC7%2FB03biLLBTSG5xSME4Bv5HaUNlFEpP6BZhW8WqsLo7Id4%2BC71qdKf3mAiMWrZ9DtFSRjtZnmGhvW%2FyvHD4de4sNDdcJCzmgdRL7ljQm6G7fV3x%2FvWj0BAw17r%2F0gY6pgGZ8LyLzQH%2Bz8B13OS8uOvbfWAvlNZVXLlGMvgFrdKAI0v0c4CaOz6pQ3K1L8h5vTUarlDJiKGOn06TEJNoLpVQACZi50u4Ls4lphAeBFQ6RXIxdDg6bEuq%2BfRDlIWIMycLHqaDSx6yYlbbzh0zpsQMGrBSvhJhvI9QRXkWpxXgXL5gk3GhyhGpzy3J1rjiIABulDz5QlCOkZyAvBfINCzWHDEON7Rd&X-Amz-Signature=c5ee7b0d8e214a631123259d0b2d667e49354fb1402f2990e40f77741c684d40&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

[image](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/954b3ff5-22dd-4209-9b0d-dcf2396817a7/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SIS67EM6%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T225058Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIGX08Lcwp%2BalWQKKBLMv6Zq7S0PzpjzhM7BSVOdLwHEuAiB1YZwdYd5qtItoWKX1y8P445w1mgKQfVJ32CzJT6Nn%2ByqIBAjG%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMT9YKSgkIr26CLac2KtwDu0M7KGiN0MHMUH2Z%2FdWOFYaM91i31Z51Hgr7k4QfafCJ5pSkSPyO%2B5dWpIR0FQ15rEzkLZ8t2XoMceSnxacWA24I1dCiICQ76BVXWRkJcluZXVDM3ss33%2FgSqVj1SncWVi6HQtfZlTr8jEc6M7RX%2FhsBgYOVImmVHeymqkH%2FhmwMaedyRqAkD7Qp47TnEYgLg56KtIfPktTZshG3Zkntg4tioXkfIocn1WZlXP2hu9XT2JcSPL7zCvk0u6ulQEcaYhBnirJTVYBjUOF82Gbi2G2MBjYrPypLi32v2q8gd1%2BpV71EdR3vh7vxSOV3kfpUjd5Fz3CxC09tO1dew2I7mfd3sUMtIv1OBEdR9tkiUJ3i8AsvsK69qHHhFs%2BK6bxAy6hiSGhSC9uarQo2SWbHXXlIJBWXvDcl28BPIk%2FTbIwAGYtgRoFB2UIOOqh7Iai3ikB4y7n%2B5jwMN6jIRJYioch%2BtfUqRD%2F2LStLBbUYaztYRtBRzkawl%2BDoAUk3YLQBEJoxC7%2FB03biLLBTSG5xSME4Bv5HaUNlFEpP6BZhW8WqsLo7Id4%2BC71qdKf3mAiMWrZ9DtFSRjtZnmGhvW%2FyvHD4de4sNDdcJCzmgdRL7ljQm6G7fV3x%2FvWj0BAw17r%2F0gY6pgGZ8LyLzQH%2Bz8B13OS8uOvbfWAvlNZVXLlGMvgFrdKAI0v0c4CaOz6pQ3K1L8h5vTUarlDJiKGOn06TEJNoLpVQACZi50u4Ls4lphAeBFQ6RXIxdDg6bEuq%2BfRDlIWIMycLHqaDSx6yYlbbzh0zpsQMGrBSvhJhvI9QRXkWpxXgXL5gk3GhyhGpzy3J1rjiIABulDz5QlCOkZyAvBfINCzWHDEON7Rd&X-Amz-Signature=9fa5989ed8ba999e92098920107a54c38d197f0cb375c29279a74ecbc3e7f72c&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

好，我们现在来总结一下咱们的这个微博项目的 k 的设计啊。可以设计。我们知道在 MySQL 中重要，在开发网站前重要的一个工作就是设计表，设计表说白了就是设计那个列的那个类型i。那么在这个 Redis 里面我们重要的就是设计它的这个key，设计它的key。我们一共设计了这么几个，一共设计了这么几个k。


用户相关的key，来，我们看看用户相关的 k 有哪些啊？第一个是一直一个自增型的，一个，这个自增型的 global util i d global user ID 画一张表比较清晰一点，表明global。咱们这个地方还沿用 MySQL 的说法表名，两者对比让我们更容易理解它的这个 kid 设计的原则。
global，然后列名，然后操作。在 global 里面我们放了两个列，一个可以这么来说，一个是这个 global user ID，我们不断的对它做什么操作呢？做那个 increa 操作备注就是产生全局的 u u 的ID，对吧？然后还有一个就是global，然后是那个 post ID， post ID 也是只对它做 inquiry 操作，然后产生全局的 post ID，产生全局的 post ID，这是全局，这个应该叫全局相关的 k 下来。


嗯，怎么会奇怪？ control x 下来。好一会再挑他下。全局相关的k，那么这是一个小的技巧，就是如何在那个。这个 no CQ 里面设计全局的自增的这个t，我们完全可以整一个这个 global 的这个k，让它不断的来自增就可以了啊。利用这个技巧。然后是用户相关的k，用户相关的这个 k 或者说表，我们映射成 MySQL 的表来操作，那我们可以看到这个表有这样的这个特点，我们看看用户表是个啥样的。用户表，你注册的时候，如果我们非要把它化成嗯。 MySQL 的这个形式， MySQL 表的形式，那它就是一个这样的表，有 u 的ID，有 user ID，有 user name，有 part word，有它的这个 author key， author secret ax also secret。然后 user ID，比如说3，比如说是 test 3 然后 part word 111111 auto secret。随便打点，就这样的一个效果，如果是在 MySQL 中，我们肯定是这样来设计的，然后转到这个 Redis 里面，我们知道这个表名。是 user 表。


顾虑到。转到 Redis 里面，我们知道在 MySQL 中一行是你设计了这个表的结构之后，一行肯定含有这几列。现在我们来到了这个 Redis 里面，我们是怎么设计的呢？是把它这个列，它是横排的，我们给它变成竖排的了，就是这样的啊。对应的一个结果就是 dollar user 表在 Redis 中。变成以下几个key。


我们可以换成 k 前缀， k 前缀是 u 的，然后这个 u 的 ID 列，这是它的这个值是 user 表，然后冒号 user ID，然后是 user name 怎么来表示是user，这个用星来表示，用星 user 表下面的 user ID，然后冒号星，在冒号 user name，同理，这里 user 冒号，有的 ID 冒号星，然后是password，再过来 user 冒号 user i d 冒号星，再冒号 also secret。那么这里对应的 k 也给它各自来一个例子，那就是 user util i d 冒号 3 test 3 user 冒号 user ID 冒号 3 冒号111。


那么大家可以完全可以看得出来，就是咱们所用的这个 K Y 6 数据库，它的这个设计上其实完全可以通过 MySQL 这种传统的数据库给它推出来。表结构映射它的前缀，最左的这个前缀，然后你用什么区分？我用 user ID 做主键来区分，唉，好，那我就用 user ID，然后加上 user ID 的值来做区分。


每一个k，然后说我有三个列，后边还有三个列，分别是 user name，那好，我分别用他们的主键加主键的值，再加你的这个列名，有个 name part word 就能来操作了。好，这是 Redis 中的这个 u 的表，或者说用户相关的k，然后我们再来看一看，就是那个微博，发微博。好，微博。


相关的k，让微博相关的 k 我们是这样来操作的，在。好表名我们完全可以对应着操这个操作，表名是post，如果是在 MySQL 中，然后它的主键应该是 post ID，然后还得有 user ID，还得有 user name，还得有content、 time 和content。比如说 3 号微博， 4 号第四条微博是 2 号用户发的是李四，时间是 137 M 987654，内容是测试微博测试内容。那么同理转到同理，再转到这个什么呢？转到 Redis 中去之后就变了。根据我们所说的规则，我们完全可以推测出来，转到 Redis 里面啊。表设计来。


微博在 Redis 中与表设计对应的 key 设计。那 k 的最前缀， k 前缀，根据我们前面总结的， k 的前缀就是表名，那我们就把它叫post，而你用什么哪个字段来做区分？我用 post ID 来做区分。因此你的前缀就应该这样写， post 冒号 post ID，冒号星星代表具体的值，那同理， post 冒号。 post ID。再来 pose 上冒号，sorry，少了个星，冒号星，再冒号 your name。


好，我们通过这个两个例子对比，我们就可以发现和传统的这个表的这个设计其实区别不大，主要是一个思路上的一个转变，甚至他俩可以完全映射，相互映射起来啊。就是你会设计 MySQL 中的表，那么只需要按照我们的规则说表名字、段名，这样一映射也能把它的这个 k 设计出来啊。然后我们再来看，嗯，这个其他的几个我就直接，其他的几个表或者说 k 的设计我就直接写了啊。还有就是推送表怎么老变蓝色？很讨厌推送表。hey。还有就是这个关注表、粉丝表、关注表、粉丝表以及推送表怎么分别来设计的啊？关注表，我们是通过这样的，你关注了一个人来 v i m follow 好 user follow it 关注表following，我们是这样来设计的，是following，然后到了 user ID，然后它的值是多少值呢？我们直接给它设计的是一个集合，因此我这地方画一个椭圆来代替集合。同理，粉丝表 follower 也是冒号 dollar user ID，它的这个值也是一个集合好。推送表是怎么回事啊？推送表是怎么回事？


推图表是挨个的把你的那个是每个人都有自己应该看到的那个内容，应该看到的那个微博的内容啊。每个人都有自己的一个这个链表，都有一个链表啊。


来我们看看每个人的这个列表是怎么回事？也就是 poster 里面 post 推送，好在这里有一个 receive post，因此它的这个前缀是 receive post。然后冒号什么啊？就是用户的ID，准确的说是用户的ID，然后 dollar user ID，然后值是多少呢啊？值是那个微博的ID，值是微博的ID，那么这么多微博大 ID 怎么来放呢？每个人都维护着自己的一个链表，所以我们画一个这个图来表示它，看看每一个人的 receive post 是个什么样子。 receive post 在这它的前缀，然后加 dollar user ID 好连过去之后对应的这个值是什么？是一个链表。
来。


那就这啊， receive ID 里边接收的全部都是这个 pose ID，比如说 357 这样的，那每个人都有自己的这样的一个链表，这是推送表啊。那么如果按照说这个结合这个 MySQL 映射的这个方式我们来理解的话，那我们微博大概是设计了这么几张表，全局表、用户表，嗯，然后微博的表，然后关注的这个表，然后还有推送的这个表，那么你就把他的这个微博的第一版就给他完成了。那么接下来咱们要分析的就是还是刚才那个问题，就是说一个人有一百万个粉丝，一期甚至一千万个粉丝，目前最高的好像就是姚晨啊。看一看它是多少个十百千万、十万、百万、千万、五千万个粉丝？姚晨不算出名，他怎么会有那么多粉丝？


HAHA，任志强多少看一看。 1, 505 万，看马平在不在微博上面关注0。霸气，哈哈哈，谁都不鸟，哈哈哈啊。对，我觉得像，但是那个任志强我看他发的应该好多是他自己发的。我看他挺有一次访谈节目，他说他经常刷，一共发了 37 个，我估计这个应该是别人帮他打理的。好，你像这样的人，粉丝这么多的人，他每发一个微博都得引起这个八九百万个这个推送，这个速度就跟不上。然后我们再来看微博这个页面，我一点首页这个页面相当于你应该看到的微博，就是你关注的那些人，对吧？你应该看到的微博，大家一起一定注意一个问题，就是这个实时性、时效性这个东西，大家想一想，微博是传播非常快的一个媒体。就是今天，你今天看到这个微博还挺新鲜，说南方非常热，都把人都中暑好几个，咱们屋也非常热啊。然后这个过两天可能这个事就忘了，你比如说今天看到一个什么很奇葩的一个微博，当时大家都来一起讨论，两天后可能大家又都忘了这个，你看云南男子强制截扎路上死亡，这个老头快 60 了，59，你看 59 的人，这硬是给人弄来截扎去，唉，这这简直混蛋。


这哈还有这个什么女市长说这个女儿被性侵犯了就别吱声，然后也别问政府要钱的，这个可能大家当时群情激愤，然后一个劲儿骂，可能过十多天之后就没人记得了啊。这个就像鲁迅说的这个，嗯，时间永世流失啊。那然后你往第十页翻，第 10 页翻，唉，已经翻到第 10 页了啊。来，大家看，再往前翻没有了，再往前翻就没有了，因为你给一个人保存着他所有要接收的微博，其实意义是不大的，其实意义并不大。


那么你观察这个新浪微博的这个特点，就是说一个人需要看到的微博，其实我自注册以来，我收到的我的粉丝的微博肯定加起来不止 1, 000 条了，但是它只给我显示了 10 页，也就是 1, 000 条只给我显示了这 10 页。为什么呢？因为它就是出于这个时效性的考虑，它没有必要给你维护一个你完完全全的一个列表，他就给你维护 1, 000 条也就够了啊。


如果是用这个推模型有一个不好的地方，比如说我都三个月都没登录了，这三个月里边发生了很多事，哗啦一下推都得推过来 2, 000 条。比如说，但是你想一下给你推 2, 000 条，你会一条一条去看吗？其实也不会啊。所以就是说在网站的这个实时性，你是追求，就是说这个是一点都不少，或者说追求这个实时统计，比如说像那种一秒都不差的来统计，就是说这个真正在网站中那个完全的真的实时，或者是完全的那个统计其实并不多，信息他都稍微的打过折。嗯，那个比如说让你统计在线人数，如果让你就统计就当前这一秒，这一瞬间有几个人在线，我想你付出的精力会非常的大，还统计不准啊。


那如果说稍微给你打点折，说我就统计 10 分钟之内的这个在线的这个人数，这马上就好统计多了，也就是说这个你是否真的要求数据丝毫无误？就比如说这个微博似的人给你推了这个 1, 000 条，那要是按照按理说我接收到的微博肯定不止 1, 000 条，你怎么只让我看到这 1, 000 条？因为没有必要看到全部的，还有你在百度搜索的时候，你随便搜一个 70 多个。舞蹈。打架，那你这个使劲往后翻，你看到他给你搜，说搜到的结果个十百千万、十万、百万、千万亿，说搜到1亿个。其实你根本说1亿个，这每一页显示 10 个，那我翻到第1, 000 万页没有，你给它翻到哪呢？你给它翻到那个 1, 000，你给它翻到 1 千，你看再往后翻没有了，再往后翻没有了，就是告诉大家，就是人接受的这个信息量是有限的啊。


所以你在开发的时候就一定要注意这一点，符合人的这个正常的这个使用的业务场景，你不用说去追求所有的信息，一丝不落的都给它放在那儿，所以这将是这将就是给我们一个提示，如果我们用拉这个模型的话怎么来操作啊？大家思考一下我们该怎么样维护你看已经给你非常细的提示了，在他的个人中心，他就只能看到 1, 000 条，个人的首页只能看到 1, 000 条。当然了，他点自己个人中心自己发的，他都能看见。我们说针对这个实时性热点，他就只能看到 1, 000 条， 1, 000 条又是他的这个关注的人发过来的，所以大家考虑一下我们怎么来设计这个表，然后我们把它改成拉模型，已经给提示得非常详细了。

