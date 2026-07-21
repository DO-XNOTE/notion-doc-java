---
title: 3-04 Redis的持久化机制 - AOF
---

# 3-04 Redis的持久化机制 - AOF

[image](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/851c7602-9c8c-4326-b836-669ac153e195/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UULC5QZW%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T224949Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIEfsAgWHikv3bJNqU190kwz44hxnnCS1hYPUrDJy5p5pAiB33m5dP9vc46r9g2wEfN86DwU%2BHw%2F5ofb4k%2BirosPHhCqIBAjG%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIME62WB%2Fn11YSPL01bKtwDKEzWoy9lI8C6Zeap6Vkrg67UmHs8sa1ZFnZNaUBe0NNyPc1sUHNYDgS%2Bki%2FyEF%2BKMtCwv5BOBY4G7Y7vkZ98ka8fE6iQYzQss6x73hAFqhtItevpIwN3MLFfhRgQs4dKVbPq1PQIRE4PRDGvpXVnFsDyZZOmNCXDEAUQ%2FgjZn1jAH1qtvoQSyqz8coa8QrJRLP4CfmzkT%2BjtdmOtlPLMkINlWk6A%2FghL4IzkPMILmKqz1ZiXYCJZBdKfbzMiUSXNOrXYvRpPANgTpMly1bxBu5pvyshQsre4C3YyCbpcpz%2BCIOR8MYHMkgysw5fYHTzr4eX8DSOVIIWuVbkFjHqBTWQ6Np5X%2FoqyTo4m%2FHl8vd2DtaNWf2REBYBYKW4926XCITNK%2Bs0lO2SDYi9vha%2BZ0WNKfGoG7DVyjUsUfZraAyQ9FKnwH6%2FWmyTBLgrWcP94VcEbdMdXYY%2FuorhzP5HDhUUdMrMY47mKoyUAJZB4muCVfMGEMydzOrSjrmrMFZAMecIy9caG6vxT%2FdZpaMZRBVBY6vefqrvnsBzmLGtpl7jS0qkdr7pdP2kxkMTQp03b4IBTje3RCIxBldXyOAOF4HxTgSivd%2Bf63cz3icRmzbuN8Qmcik9gwwtBpUIwwLr%2F0gY6pgE409YbTWvFvYVr1c%2Fiv4vDn3D1rPwgvVH76OeV0ZlUV1P3IL215MZL8iYHMbSBI%2FPdbz251ngajf%2BUioWcZQAC8cq9%2BaqsAKj6t%2BPqJmAIewaTGc8Q2gIcE0TOZHeUw%2Fv1hkV2B7lkACXASiABfQWD%2BGLYhiW%2BwzMavXDJBVDe8xomzR4UqyIcY3jBzVPkzQ4uo2FzBJdRp9Oc4q42%2B6un6coS6kl4&X-Amz-Signature=02bc27303fec7d6e5b24b08688485ce7073745eaaa71605f812553b7f8028c87&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

[image](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/50ce17ba-9144-432e-b809-c258de624fab/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UULC5QZW%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T224949Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIEfsAgWHikv3bJNqU190kwz44hxnnCS1hYPUrDJy5p5pAiB33m5dP9vc46r9g2wEfN86DwU%2BHw%2F5ofb4k%2BirosPHhCqIBAjG%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIME62WB%2Fn11YSPL01bKtwDKEzWoy9lI8C6Zeap6Vkrg67UmHs8sa1ZFnZNaUBe0NNyPc1sUHNYDgS%2Bki%2FyEF%2BKMtCwv5BOBY4G7Y7vkZ98ka8fE6iQYzQss6x73hAFqhtItevpIwN3MLFfhRgQs4dKVbPq1PQIRE4PRDGvpXVnFsDyZZOmNCXDEAUQ%2FgjZn1jAH1qtvoQSyqz8coa8QrJRLP4CfmzkT%2BjtdmOtlPLMkINlWk6A%2FghL4IzkPMILmKqz1ZiXYCJZBdKfbzMiUSXNOrXYvRpPANgTpMly1bxBu5pvyshQsre4C3YyCbpcpz%2BCIOR8MYHMkgysw5fYHTzr4eX8DSOVIIWuVbkFjHqBTWQ6Np5X%2FoqyTo4m%2FHl8vd2DtaNWf2REBYBYKW4926XCITNK%2Bs0lO2SDYi9vha%2BZ0WNKfGoG7DVyjUsUfZraAyQ9FKnwH6%2FWmyTBLgrWcP94VcEbdMdXYY%2FuorhzP5HDhUUdMrMY47mKoyUAJZB4muCVfMGEMydzOrSjrmrMFZAMecIy9caG6vxT%2FdZpaMZRBVBY6vefqrvnsBzmLGtpl7jS0qkdr7pdP2kxkMTQp03b4IBTje3RCIxBldXyOAOF4HxTgSivd%2Bf63cz3icRmzbuN8Qmcik9gwwtBpUIwwLr%2F0gY6pgE409YbTWvFvYVr1c%2Fiv4vDn3D1rPwgvVH76OeV0ZlUV1P3IL215MZL8iYHMbSBI%2FPdbz251ngajf%2BUioWcZQAC8cq9%2BaqsAKj6t%2BPqJmAIewaTGc8Q2gIcE0TOZHeUw%2Fv1hkV2B7lkACXASiABfQWD%2BGLYhiW%2BwzMavXDJBVDe8xomzR4UqyIcY3jBzVPkzQ4uo2FzBJdRp9Oc4q42%2B6un6coS6kl4&X-Amz-Signature=53de915b068939a32d9a8266ee5cf2dbc23f57151da1bd43c77add841816a808&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

那么上一节课我们是讲了 RDB 的一种持久化机制，那么需要注意 RDB 的话它是一个全量的备份模式，那么除了 RDB 以外，那么还有一种就是AOF，那么这节的话我们就一起来看一下什么是AOF。那么还是一样，我们是以这个官方的文档为例。那么我们上一节的这个 rdb 的话，其实我们也知道它会有一个弊端，就是说它很有可能在执行最后一次备份的时候会出现一些问题，那么这样子的话就会导致你最后一次的备份文件，它的一个rdb 会丢失。那么其实这样子的话也是无所谓的，可以说你可以去忽略不计，因为毕竟是缓存，丢了就丢了，但是如果说你要去追求数据的完整性，数据的一个安全性的话，那么你就需要去考虑一下使用 AOF 这样的一个持久化机制了。来看一下。那么这个 AOF 的一个持久化机制，其实可以看到它是一个日志的形式是存在的，然后当只要有每一次的一些操作，那么过来的时候，那么它就可以被我们的一个 aof 去做一个相应的写入。那么需要注意这里的一个操作的话，是一个写操作，只有是写操作，它才能够被记录到 i o f 的一个日志文件里面。如果仅仅是一个读操作，那么相应它是不会被记录的。

[https://redis.io/docs/management/persistence/](https://redis.io/docs/management/persistence/)

[file](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/eecf0a7e-8d67-4358-8c3e-62c86089eefc/redis.conf?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UULC5QZW%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T224949Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIEfsAgWHikv3bJNqU190kwz44hxnnCS1hYPUrDJy5p5pAiB33m5dP9vc46r9g2wEfN86DwU%2BHw%2F5ofb4k%2BirosPHhCqIBAjG%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIME62WB%2Fn11YSPL01bKtwDKEzWoy9lI8C6Zeap6Vkrg67UmHs8sa1ZFnZNaUBe0NNyPc1sUHNYDgS%2Bki%2FyEF%2BKMtCwv5BOBY4G7Y7vkZ98ka8fE6iQYzQss6x73hAFqhtItevpIwN3MLFfhRgQs4dKVbPq1PQIRE4PRDGvpXVnFsDyZZOmNCXDEAUQ%2FgjZn1jAH1qtvoQSyqz8coa8QrJRLP4CfmzkT%2BjtdmOtlPLMkINlWk6A%2FghL4IzkPMILmKqz1ZiXYCJZBdKfbzMiUSXNOrXYvRpPANgTpMly1bxBu5pvyshQsre4C3YyCbpcpz%2BCIOR8MYHMkgysw5fYHTzr4eX8DSOVIIWuVbkFjHqBTWQ6Np5X%2FoqyTo4m%2FHl8vd2DtaNWf2REBYBYKW4926XCITNK%2Bs0lO2SDYi9vha%2BZ0WNKfGoG7DVyjUsUfZraAyQ9FKnwH6%2FWmyTBLgrWcP94VcEbdMdXYY%2FuorhzP5HDhUUdMrMY47mKoyUAJZB4muCVfMGEMydzOrSjrmrMFZAMecIy9caG6vxT%2FdZpaMZRBVBY6vefqrvnsBzmLGtpl7jS0qkdr7pdP2kxkMTQp03b4IBTje3RCIxBldXyOAOF4HxTgSivd%2Bf63cz3icRmzbuN8Qmcik9gwwtBpUIwwLr%2F0gY6pgE409YbTWvFvYVr1c%2Fiv4vDn3D1rPwgvVH76OeV0ZlUV1P3IL215MZL8iYHMbSBI%2FPdbz251ngajf%2BUioWcZQAC8cq9%2BaqsAKj6t%2BPqJmAIewaTGc8Q2gIcE0TOZHeUw%2Fv1hkV2B7lkACXASiABfQWD%2BGLYhiW%2BwzMavXDJBVDe8xomzR4UqyIcY3jBzVPkzQ4uo2FzBJdRp9Oc4q42%2B6un6coS6kl4&X-Amz-Signature=1614ae2c54eb8ee26ae570430899e8c82af1f0ba0d5d59f0016ba26401b82b59&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)


OK，那么对于我们的一个 aof 的话，那么它其实是以一个文件的形式，然后它是一个append，它是一个追加式的，往我们的日志文件里面去追加相应的一个指令的。另外的话我们的一个Redis，它也是可以去做一个重写，所以说我们的LF，它的一个日志可能会越写越大，那么你就可以去启动它的一个重写机制，去把它的一个日志，把它的 AOF 文件变得更加的小，那么这个也是可以去做的。OK，好，然后往下面看。下面的话是一个它的优势和劣势，那么先来看一下它的一个优势，那么使用这个 l f 的话，那么咱们的一个Redis，它可以变得更加的健壮和持久，也是更加的耐用，那么它可以提供不同的一个同步方式。需要注意在这里有一个 f think，那么这个是它的同步方式，它其实是有两种的，应该说是有三种，一个是关闭，另外一个是使用每秒，可以每一秒去做一个持久化的一个日志记录。另外一个的话就是根据每一次的一个请求，根据每一次的操作去做，那么这个我们也是会在后面的一个核心配置文件里面我们会去说的，这个里面会包含。然后如果说我们是使用的默认的机制的话，它默认的一个策略就是以按照每秒每秒去进行的一个写入，那么这种方式的话也是比较好的。


然后对于我们的一个AOF，它的一个日志，那么它的形式是一个append， append 就是追加，就是以日志的形式去进行一个追加。如果说我们的一个 desk 磁盘满了，或者说是由于其他的一些原因的话，那么也是可以去使用这个 Redis check 杠 AOF 这个工具，这是一个命令工具，然后可以使用它去非常简单的去进行一个修复，那么也是可以的。然后下一个的话是说 Redis 它是可以去做一个自动的重写，那么做自动重启的时候，那么它其实是在background，也就是在咱们的一个后台去做一个运行的，那么随后的话我们的一个重写，重写就是在就是运行在他的一个后台，那么这样子的话，当 Redis 他继续把一些日志追加到老的文件中去的时候，那么其实对于重写来讲的话，它也是非常安全的，它是不会去影响客户端的相应的读写的操作的。那么这个重写的话，它的一个机制以及是出发点，那么也可以在 Redis 的核心配置文件里面去做相应的修改的好。


随后是第四一点的话，是我们的一个AOF，那么它的话是一个日志，那么这个日志里面是包含了所有的一些操作，然后它是 one after see other，也就是它是一个接着一个去进行的一个叠加式的追加，它里面包含了所有的写操作，那么这样子的话就是会更加便于我们的 Redis 去做一个解析和恢复，在这里是更加的。

To understand and pass for that it just found.


方便的去让 Redis 去做一个理解以及是解析，然后的话在这里看一下，那么你可以去尝试着非常简单的把一个 of 导出，然后比方说你可以去把所有的内容全部都flash，可以通过一个 flash or 这样的一个命令，然后全部清除了以后，那么这个时候其实我们是没有任何数据的。然后你可以再把这个 AOF 文件打开了以后，你只要把这个指令，它会有一个最后一行的指令，就叫做弗拉硕，你直接把它给删掉。删掉以后这个时候你再去做一个重启，那么也可以看到在这里可以去做一个删除，把最后的一个命令给删掉。


其实最后的一次命令执行的就是一个flash，删掉以后然后再去做一个重启，那么这个时候我们 AOF 里面的一些之前的那些数据，它会被我们恢复到 Redis 的OK，那么这些操作的话，我们后面也会带着大家去做的，那么这些是它的一个优势。随后我们再来看一下它的劣势，那么这是劣势。那么首先一个那么既然是日志，所以只要是日志的话，那么他一旦去写的话，那么其实他的文件肯定会很大，那么如果说和这个r、 d b 去做一个对比的话，对于相同的数据集来讲的话，那么 a of 它的一个文件，它的日志文件肯定要比咱们的一个r、 d b 文件要更大，那么这一点是需要去注意的。


当然如果说我们的一个云服气，我们的一个磁盘空间很大，或者说又挂载了很多的一些硬盘的话，那么其实也无所谓，那么你的一个这个数据的体积，不管是有几个 g 或者十几个g，那么其实都是没有问题的，问题也不大。然后我们再看下一点，下一点的话是指我们的一个同步的机制，就是说当我们在使用不同的一个同步机制的时候，一个是每一秒，另外是一个每一次的一个请求，每一次的一个写入，那么它其实都会有相应的一个 IO 的一个操作，那么一旦有 IO 的一个操作的话，那么相应的肯定是对我们的一个服务是有一定的性能的影响的。


那么和 r d b 去相比的话，那么其实 r d b 其实我们是在每隔一段时间去做的一个全量的备份，那么对于l， f 来讲的话，它其实会一直的去频繁的去做一个i， o 的一个写入，所以的话它其实会有一定的性能的损耗。但是如果说仅仅是一个 every second 的是每秒的一种形式的话，那么其实它的一个性能还好，那么就是这一句话所突出的。那么如果说你要去针对每一次用户的一个写操作，你都要去做一个备份的话，那么它的一个性能的损耗是比较大的，尤其是在一个超高并发的一个情况下，所以一般来说的话，我们都是使用它的一个默认的，也就是 LV second 的 OK 好。然后最后一点，这一点的话是它的一个bug，就是说当在使用 AOF 的时候，其实他在曾经可以看一下它其实出现过一个BUG，是啊，出现过一些问题，那么发生过这些问题的话，其实就是在进行数据恢复的时候，会导致我们的一个数据恢复过后和我们以前的数据会有一点不完整，那么这样子的话其实就会显得我们的这个 AOF 会比较的脆弱，比较容易出现BUG。


那么这样子的话，其实对于我们的 r d b 来讲，其实 a of 它本身它的机制就是要比 r d， b 相对要稍微的复杂一些，那么 r d b 会更简单，那么这样子的话，其实对于它的一个官方来讲的话，官方它为了防止 bug 的产生，所以 AOF 的话它是不会去根据过旧的就是老的一些指令去重构，而是会根据我们当时在我们当前的内存里面，当前的缓存里面的一些所存在的一些数据。针对这些已有的缓存数据去做一个重构，那么这样子的话它就可以显得更加的健壮和可靠了。


OK，好，那么接下来的话我们讲了这些内容之后，其实我们就可以去针对咱们的一个配置，去做一些配置上的一些查看，我们可以打开这个命令行工具，那么还是一样。那么这个时候我们先看一下，我们要进入到 user local，再进入到Redis，那么这个就是咱们的核心配置文件，然后进去看一下，那么上一节我们是看的是看这一块内容，那么这些都是 r d b 的，这是 r d b 的内容。


那么如果说你要去看 a o f 的话，那么直接可以去搜一下，搜一个append，在这里有一个 append only model，也就是 a o f 模式来看一下。那么当我们在 Redis 安装完毕以后，那么其实它默认的方式使用的是这个dumps，其实也就是 RDB 模式就是默认的。那么使用默认的方式的话，这种 r d b 模式其实是比较好，也是比较简单易用的，其实存在于很多的一些应用里面。OK，那么这个词其实也是可以去使用的。当然如果说是在一个大并发的一个场景下的话，那么可能就显得不太好。


随后我们可以往下面看，那么在这里有一个 append only，那么它默认是关闭的，那么你是可以把它给开启的，改为yes。那么这样子我们的一个 AOF 就开启了，随后保存一下再进来，然后下面一个，那么这个是我们的一个 AOF 的一个名称，就是说一旦我们做了一个备份以后，那么它会产生相应的一个文件的名称的。那么这个的话其实我们也是可以去做，我们一会儿会去做一个查看，它会做一个生成的，然后再往下，再往下的话就是它的一个策略。


在这里它有一个 append f think 这样的一个同步策略，总共是有三种，一个是always，一个是 every second，另外一个就是NO， NO 的话其实就是关闭 every second，就是每一秒去做一个持久的一个同步。那么另外一个就是always， always 就是总是其实在它的一个文档的上方其实也是有的。在这里 always 的话其实就是针对于每一次的写操作，只要有写操作，那么它就会把我们所有的数据都会写到这个 AOF 的一个日志文件里面。


然后的话在这里如果说你使用了always，那么它会非常的慢，它会slow，但是它是比较安全的，因为它可以保证你几乎所有的数据它都是完整的，它不会丢失。但是一般来说我们使用这个 every second 的就可以了，那么在这里的话其实它也会有一个提示，在这里这边是它的一个默认的一个家的注释，那么默认时就是 IV second 的，然后的话它也是经常会被时的一种方式，那么区别于其他的两种然后的话，他这个的话是可以由你去决定你想要去使用的哪种方式。然后的话如果说一般来说的话，你如果说没有必要太过于纠结的话，那么我们就可以直接使用这个 f second 就可以了。在这里有一个分数，如果说你不确定，那么直接使用这个 ivsecond 的就行了。


好OK，那么到这里的话，然后这是一些资本的配置，然后我们保存一下以后这个时候我们进入ETC，也不需要我们这样子点斜杠，直接斜杠 etc 下 unit 减d，然后 Redis stop，因为我们是修改了配置，最好要重启一下。然后做一个重启，重启成功之后，然后我们看一下，在我们当前的这个文件里面，其实我们能够发现之前只有gap，现在一旦我们重启了以后，你就能够发现我们现在就多了一个 AOF 这样的一个预置文件了。我们可以打开去看一下，目前为空，因为里面没有任何的数据。好，随后我们 Redis 杠client，然后密码输一下好进来以后，那么这个时候我们来做一些操作，比方说我们先这样子，我们先来做一个 flash DB，先清空一下，然后 T4 星号现在是空的数据，然后 set 一个m，比方说加。然后再来一个 set age，来一个18，再来一个set，来一个 sex boy。好，那么这个时候我们总共是有三个 key 吧，有了 3 个 t 以后，随后我们退出。


退出以后我们来看一下，你会发现我们之前所做的这些内容，它全部都是以一个指定的形式存在，然后在这里面我们就能够看到。在这里面的话，比方说有一个 set 可以看到 set m 可是一个Java，然后再来 set a 值是一个18，它在这里面的一些指令其实全部都放进去了。OK，它会记录你每一个的写操作，读操作，在这里面是没有的。OK，好，退出。


随后我们再回到，回到这个 Redis 里面，那么然后继续，那么我们之前也说了，其实对于我们的这个 AOF 来讲的话，它是可以去做一个重写的，那么重写的话在它的下方会有一个重写的机制，在这里它会有一个 no append f think on right 是no，那么这个意思是指当我们的一个重写它正在重写的时候，那么其实它可以不要去做同步，不要去把一些新的操作放到我们的日志文件里面。如果说你在这里改为 yes 的话，那么这样子就有可能会导致我们的一个文件日志内容的一个不一致性，它会显得不太完整，所以一般来说我们建议把它直接改为 NO 就可以了。


OK，然后再往下的话就是它的一个大小，在这里的话它有一个 Santa h，另外一个是最小的一个size，那么这两个是什么意思？所以说它的一个重写机制其实就是为了避免我们的一个 AOF 这个文件越来越大，那么它其实可以让它自己去做到一个在后台运行的一个自动优化，那么它那么它是可以去压缩的，那么这样子的话其实就可以 fork 出一个新的进程，去完成重写的这一系列的动作。


那么在 Fork 出一个新的进程以后，那么这个进程里面在内存里面所包含的一些数据，缓存数据，那么它都会被进行一个重写，那么这个时候它的一个老的旧的 AOF 文件的话，是不会被它去使用的，它其实它就是类似于 RBB 这种模式，那么这个现在也是100%， 100 就是 100% 是一个比例。那么如果说他当前在进行检查的时候，他当前的一个文件的大小超过了上一次文件的大小的一倍，或者说你可以改成 200 就是两倍，或者说是一半。在这里它会有的，它其实会记录你的上一次的一个大小，它的这个注释里面其实都会有，那么可以看这里是它的一个如何去工作的一个执行原理，工作原理。


所以说咱们的一个Redis，它其实会记住它一个 LF 文件的一个大小，那么是在我们上一次重写完毕之后去记住的一个大小。如果说在这里有一个，如果说是第一次，也就是从来没有重写过的话，那么其实我们当前这个 success 当前的一个大小其实就是我们初始的一个 AOF 文件的一个大小，那么这个大小的体积是可以去进行一个比对的。


那么在我们要去进行一个重写的话，如果说我们的一个新的日志文件，新的 LF 文件的话，和我们的上一次去做一个对比，那么在这里是 100% 100% 其实就是一倍，如果说是超过一倍的话，那么它是会被触发的。假设我们上一个备份的 g 文件是一个g，那么这个时候当我们的一个 AF 文件达到了 2 个g，也就是在这里是 100% 的时候，那么你会发现这个 surwhite the white is triggered，就是说它会被触发，但是的话，其实你还需要满足第二个条件，也就是在这里有一个 main size，这是一个百分比，那么这是一个文件的一个大小。那么在这里的话，它其实设定的是一个 64 兆，那么其实相对来说会比较小。


那么假设我按照我们刚刚所设定的，如果说我们初始是一个g，那么达到了 2 个 g 的话，那么其实会被触发，同时我们在这里也要满足这个条件，那么假设我们在这里写的是 500 兆，那么 2 个 g 肯定是超过 500 兆的。所以两个条件你都满足的话，那么我们的一个 rewhite 重写就会被触发。


OK，那么这一点的话是需要去注意这两个策略，两个条件要同时的满足，那么在这里的话，这个 100% 其实你也可以自己去设置，不管是 50% 还是 200% 都行。另外对于家的一个日志大小的话，其实 64 兆在生产环境里面是偏小的，一般的话你可以设置为像 5 个g， 8 个g， 10 个 g 都可以达到一定大小的时候，那么我们再去做一个压缩，再去做一个重叠，那么也是可以的。那么如果说是在高并发的环境下的话，那么其实它的一个日志的写入是非常非常快的，那么它的一个这个膨胀的体积也会越来越大，所以这个体积的话， 64 兆肯定是太小的。


那么一般来说根据一个运维的一个监控，根据运维提供的信息可以去做一个修改，那么当然像这些内容的话，一般来说其实也都是由运维人员去做一个相应的修改的。OK，那么随后我们回到他官方的文档。之前我们在这里也说了，如果说我们在这里就是说平时的操作的时候，假设假如说发生一个误操作，使用的一个 flash or 或者说是 flash DB，这个时候我们的所有的数据全部都会被清空。那么清空了以后，其实这个 flash or 这样的一个命令的话，它也会被记录到我们的 AOF 这个文件里面的。那么这个时候你要去做一个修复的话怎么办？那么你只需要打开这个文件，打开文件移除最后的一次命令，也就是把这个命令给删掉，删掉以后做一个重启，那么就可以了。


OK，最后我们可以来测试，我们可以来看一下，目前我们的一个 AV 文件里面，我们可以先打开，那么在它的最后其实是一个boy。好，最后我来退出，退出以后这个时候我们再一次的记住，我们再一次 Redis client， kiss 查看一下，随后我们来一个发售，或者说是 flash DB。好，这个时候我们所有的 kiss 全部都没有了。


随后退出以后我们来观察一下，这个时候我们来观察一下我们当前的这个文件，这个 l f 的文件里面，在最后它其实多了一个 last d b，那么如果说这个时候我们想要去做一个恢复的话，不管是我们是停止重启以后，其实我们的一个命令虽然是一个一个的去加载，加载到最后我们所有的数据还是会被清空的，所以我们只需要把最后一个内容给删掉就可以了。


我们先这样子，先来把我们的一个服务器 BTC unit，然后 ready stop，我们先停止了以后，然后我们去把这个文件的最后把这一行删掉好，保存退出。随后我们这个时候我们再来做一个重启，重新启动。重新启动以后，这个时候我们再来看一下咱们的一个 kiss UID，plants，这个时候你会发现我们的所有的内容还是能够存在的，这是因为我们是把 flash DB 给清掉了，如果说你没有把 flash DB 删掉，那么你这个时候你再去重启 ready 服务的话，那么我们的这里的数据还是获为空的，那么这一点的话是一定要去注意的。


那么对于我们的这个两种模式来讲的话，其实你到底应该使用哪一种模式会比较合适？其实在官方这里也是贴了一段内容，那么如果说你能够接受在一段时间内，不管是 5 分钟 10 分钟，那么它的一个缓存丢失的话，那么你可以去使用这个 r t b 是没有任何问题的。那么如果说你对它的一个实时性的数据比较care，比较关心的话，那么你就可以去使用AOF。


那么其实在我们平时的一个使用过程中，你是完全可以同时的搭配 r t b 和 AOF 配合在一起去做使用的，那么这样子在一起去做一个持久化的话，其实我们又可以称之为是一种冷热备份的机制，那么 r t b 的话是作为一个冷备份，那么可以在不同的时期对不同的版本去进行管理，去进行恢复。


那么 AOF 的话是可以去做一个热备的，它可以保证我们的数据仅仅只有 1 秒到 2 秒的一个损失，最大是不会超过 2 秒。那么这样子如果说我们的 AOF 文件，它的日志发生了破损坏掉了，那么这个时候的话我们是可以把它给删掉，然后再使用 RDB 替换，并且去做到一个恢复。那么这样子的话，其实我们就可以做到这两者的相互结合。也就是说 Redis 的恢复其实它会先去加载AOF，然后如果说 AOF 它发生了问题，那么它会如果说你直接删掉以后，那么它会再一次的去加载r，d，b，它是有一个顺序之分的，先去加载l，f，然后再去加载一个r、d、b。那么以此我们就可以达到一个冷热备份的一个目的了。 OK 那么关于我们这两节的一个持久化的一个机制的话，其实我们也是会有文档的，那么这个文档的话也是配合着我们的视频，那么大家也是可以去参考着去看的。OK，NP。

[image](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/e7dd2305-0623-4976-8fae-6b372fbbc45e/2020-09-17_195728.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UULC5QZW%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T224949Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIEfsAgWHikv3bJNqU190kwz44hxnnCS1hYPUrDJy5p5pAiB33m5dP9vc46r9g2wEfN86DwU%2BHw%2F5ofb4k%2BirosPHhCqIBAjG%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIME62WB%2Fn11YSPL01bKtwDKEzWoy9lI8C6Zeap6Vkrg67UmHs8sa1ZFnZNaUBe0NNyPc1sUHNYDgS%2Bki%2FyEF%2BKMtCwv5BOBY4G7Y7vkZ98ka8fE6iQYzQss6x73hAFqhtItevpIwN3MLFfhRgQs4dKVbPq1PQIRE4PRDGvpXVnFsDyZZOmNCXDEAUQ%2FgjZn1jAH1qtvoQSyqz8coa8QrJRLP4CfmzkT%2BjtdmOtlPLMkINlWk6A%2FghL4IzkPMILmKqz1ZiXYCJZBdKfbzMiUSXNOrXYvRpPANgTpMly1bxBu5pvyshQsre4C3YyCbpcpz%2BCIOR8MYHMkgysw5fYHTzr4eX8DSOVIIWuVbkFjHqBTWQ6Np5X%2FoqyTo4m%2FHl8vd2DtaNWf2REBYBYKW4926XCITNK%2Bs0lO2SDYi9vha%2BZ0WNKfGoG7DVyjUsUfZraAyQ9FKnwH6%2FWmyTBLgrWcP94VcEbdMdXYY%2FuorhzP5HDhUUdMrMY47mKoyUAJZB4muCVfMGEMydzOrSjrmrMFZAMecIy9caG6vxT%2FdZpaMZRBVBY6vefqrvnsBzmLGtpl7jS0qkdr7pdP2kxkMTQp03b4IBTje3RCIxBldXyOAOF4HxTgSivd%2Bf63cz3icRmzbuN8Qmcik9gwwtBpUIwwLr%2F0gY6pgE409YbTWvFvYVr1c%2Fiv4vDn3D1rPwgvVH76OeV0ZlUV1P3IL215MZL8iYHMbSBI%2FPdbz251ngajf%2BUioWcZQAC8cq9%2BaqsAKj6t%2BPqJmAIewaTGc8Q2gIcE0TOZHeUw%2Fv1hkV2B7lkACXASiABfQWD%2BGLYhiW%2BwzMavXDJBVDe8xomzR4UqyIcY3jBzVPkzQ4uo2FzBJdRp9Oc4q42%2B6un6coS6kl4&X-Amz-Signature=8b10009987de9e25547fecb7644f125f09543c00234d649e571c25ad8d2f8619&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)




