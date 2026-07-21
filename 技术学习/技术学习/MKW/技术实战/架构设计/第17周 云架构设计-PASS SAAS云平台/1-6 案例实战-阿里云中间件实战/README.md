---
title: 1-6 案例实战-阿里云中间件实战
---

# 1-6 案例实战-阿里云中间件实战

[image](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/72ef9d16-b2b8-4d68-b62d-cfd36862eedc/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466Y2YUH4II%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T231116Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDT8BXbZmsbmxJENHy3MDjnhi1mPKLAdDzCByt0i%2FvMYQIgQJwsToDqOXB%2BWXKHbJDmKSKszbTxyBKdlg2K4jcdIgEqiAQIxv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDE3GIscHSkXjt3P%2FhSrcAxvLUnPV0Zw4Dg7xZU4PWdP2T%2BopcMIQIlCaNvUWYFlWo3woJM4yT4gxa4IJwg9gnhecWZG8x%2FKrIzlteB9ekW0i4vug5mli9RNvAfOBer7a%2B4uymrNpY6CWIQfrqute8dtUqZ77r8hO6U3Ar2WtaMbr9VuuXkJ7kf2gl2b2p8ttDQoAy3TmqOxJumIWW3A%2FlFQH8Na4ZYtyV92pMmAH%2F%2Fjm8C5GWM15kQ8DvAzUE3GF2J3CO1U3a0%2BB%2B%2B%2FJvpNgezi5Bjv7N0nBDLqmhVmAwN5FR5WfzfgVsZLt0ypNaVIQYlP0mDXx7rlutom2iZmcBzFHWp8FkLCatngfCKfJnsNBEhr8lWmWVRpLF4Oja7UDOwytdn2gAREghbDHXVDZVRi%2Bsz6blq5KMWI4B0e0LIA9ePboMQUqir7OrhJFBju6C3PW8KYmg%2B2q%2BpS7Reg7mypW8%2B6X%2BKCp61F2lnykuga0UOV5tnCNHXaepKyJd7o%2BKwAoyeF6vn7mIcgyWLWcSkpFYEv4FrMubgpaVWEr0olJYWQcwfspYboPwxy5AvdFwnGLFjfqfz2Xgq%2FlKcGXQREipin9rKo%2BeFtsg79ERcQQp4A5CbQM0joOOkf7sVZsumqXsFDJ4kMVAuzpMO%2B3%2F9IGOqUBk0uiJaX3JkeuhpSNknrK%2BW%2B%2BEVMxRKaarkCLOWqn4al3h6kvkX0ElEOBau4PDOg4wdveoYlfJoxjB9%2BE5Ss6brG4%2FsTjcjq9Elat1T5kGShDHhEa0t2RlB0e%2BxX00EHd084esfxepbKcBvHbmap2m3MRig1y%2FJOviGhlGq9JIlXGz1cpRRvDvX6Jw8CPmek3%2FRNonENNn1W%2BzUqL7ZBj4FCs98HE&X-Amz-Signature=b7659fa19315fae2e016f058255734cea1fbbcd83df8b7be3ac784a35dcf13af&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

架起需求到落地的桥梁，构建 IT 新蓝图。我是张飞扬。

[image](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/dbdc822a-49fa-4058-8098-381f242131c3/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466Y2YUH4II%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T231116Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDT8BXbZmsbmxJENHy3MDjnhi1mPKLAdDzCByt0i%2FvMYQIgQJwsToDqOXB%2BWXKHbJDmKSKszbTxyBKdlg2K4jcdIgEqiAQIxv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDE3GIscHSkXjt3P%2FhSrcAxvLUnPV0Zw4Dg7xZU4PWdP2T%2BopcMIQIlCaNvUWYFlWo3woJM4yT4gxa4IJwg9gnhecWZG8x%2FKrIzlteB9ekW0i4vug5mli9RNvAfOBer7a%2B4uymrNpY6CWIQfrqute8dtUqZ77r8hO6U3Ar2WtaMbr9VuuXkJ7kf2gl2b2p8ttDQoAy3TmqOxJumIWW3A%2FlFQH8Na4ZYtyV92pMmAH%2F%2Fjm8C5GWM15kQ8DvAzUE3GF2J3CO1U3a0%2BB%2B%2B%2FJvpNgezi5Bjv7N0nBDLqmhVmAwN5FR5WfzfgVsZLt0ypNaVIQYlP0mDXx7rlutom2iZmcBzFHWp8FkLCatngfCKfJnsNBEhr8lWmWVRpLF4Oja7UDOwytdn2gAREghbDHXVDZVRi%2Bsz6blq5KMWI4B0e0LIA9ePboMQUqir7OrhJFBju6C3PW8KYmg%2B2q%2BpS7Reg7mypW8%2B6X%2BKCp61F2lnykuga0UOV5tnCNHXaepKyJd7o%2BKwAoyeF6vn7mIcgyWLWcSkpFYEv4FrMubgpaVWEr0olJYWQcwfspYboPwxy5AvdFwnGLFjfqfz2Xgq%2FlKcGXQREipin9rKo%2BeFtsg79ERcQQp4A5CbQM0joOOkf7sVZsumqXsFDJ4kMVAuzpMO%2B3%2F9IGOqUBk0uiJaX3JkeuhpSNknrK%2BW%2B%2BEVMxRKaarkCLOWqn4al3h6kvkX0ElEOBau4PDOg4wdveoYlfJoxjB9%2BE5Ss6brG4%2FsTjcjq9Elat1T5kGShDHhEa0t2RlB0e%2BxX00EHd084esfxepbKcBvHbmap2m3MRig1y%2FJOviGhlGq9JIlXGz1cpRRvDvX6Jw8CPmek3%2FRNonENNn1W%2BzUqL7ZBj4FCs98HE&X-Amz-Signature=9ba0eba3b2ca1e323daf8a19588bd9aea5de9c5c2651645afd21c20c3bbb61f0&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

好，上一章节我们聊了聊万家灯火的中间件。

[image](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/3a6686d1-0df6-4eaf-bdb6-30f5442b8c2b/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466Y2YUH4II%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T231116Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDT8BXbZmsbmxJENHy3MDjnhi1mPKLAdDzCByt0i%2FvMYQIgQJwsToDqOXB%2BWXKHbJDmKSKszbTxyBKdlg2K4jcdIgEqiAQIxv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDE3GIscHSkXjt3P%2FhSrcAxvLUnPV0Zw4Dg7xZU4PWdP2T%2BopcMIQIlCaNvUWYFlWo3woJM4yT4gxa4IJwg9gnhecWZG8x%2FKrIzlteB9ekW0i4vug5mli9RNvAfOBer7a%2B4uymrNpY6CWIQfrqute8dtUqZ77r8hO6U3Ar2WtaMbr9VuuXkJ7kf2gl2b2p8ttDQoAy3TmqOxJumIWW3A%2FlFQH8Na4ZYtyV92pMmAH%2F%2Fjm8C5GWM15kQ8DvAzUE3GF2J3CO1U3a0%2BB%2B%2B%2FJvpNgezi5Bjv7N0nBDLqmhVmAwN5FR5WfzfgVsZLt0ypNaVIQYlP0mDXx7rlutom2iZmcBzFHWp8FkLCatngfCKfJnsNBEhr8lWmWVRpLF4Oja7UDOwytdn2gAREghbDHXVDZVRi%2Bsz6blq5KMWI4B0e0LIA9ePboMQUqir7OrhJFBju6C3PW8KYmg%2B2q%2BpS7Reg7mypW8%2B6X%2BKCp61F2lnykuga0UOV5tnCNHXaepKyJd7o%2BKwAoyeF6vn7mIcgyWLWcSkpFYEv4FrMubgpaVWEr0olJYWQcwfspYboPwxy5AvdFwnGLFjfqfz2Xgq%2FlKcGXQREipin9rKo%2BeFtsg79ERcQQp4A5CbQM0joOOkf7sVZsumqXsFDJ4kMVAuzpMO%2B3%2F9IGOqUBk0uiJaX3JkeuhpSNknrK%2BW%2B%2BEVMxRKaarkCLOWqn4al3h6kvkX0ElEOBau4PDOg4wdveoYlfJoxjB9%2BE5Ss6brG4%2FsTjcjq9Elat1T5kGShDHhEa0t2RlB0e%2BxX00EHd084esfxepbKcBvHbmap2m3MRig1y%2FJOviGhlGq9JIlXGz1cpRRvDvX6Jw8CPmek3%2FRNonENNn1W%2BzUqL7ZBj4FCs98HE&X-Amz-Signature=8b290426328ccdaeaeb2dd9083539b42734df2b1b4cc2e658bbfa9a99a0d56f8&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

这章节我们以阿里云为例，来实战几个常用的技术栈。点击左上角的红颜色，找到产品与服务，往下面找。这里面有什么？有Redis，

[image](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/40612b6f-caf9-4a22-842a-d408d5fdee1d/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466Y2YUH4II%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T231116Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDT8BXbZmsbmxJENHy3MDjnhi1mPKLAdDzCByt0i%2FvMYQIgQJwsToDqOXB%2BWXKHbJDmKSKszbTxyBKdlg2K4jcdIgEqiAQIxv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDE3GIscHSkXjt3P%2FhSrcAxvLUnPV0Zw4Dg7xZU4PWdP2T%2BopcMIQIlCaNvUWYFlWo3woJM4yT4gxa4IJwg9gnhecWZG8x%2FKrIzlteB9ekW0i4vug5mli9RNvAfOBer7a%2B4uymrNpY6CWIQfrqute8dtUqZ77r8hO6U3Ar2WtaMbr9VuuXkJ7kf2gl2b2p8ttDQoAy3TmqOxJumIWW3A%2FlFQH8Na4ZYtyV92pMmAH%2F%2Fjm8C5GWM15kQ8DvAzUE3GF2J3CO1U3a0%2BB%2B%2B%2FJvpNgezi5Bjv7N0nBDLqmhVmAwN5FR5WfzfgVsZLt0ypNaVIQYlP0mDXx7rlutom2iZmcBzFHWp8FkLCatngfCKfJnsNBEhr8lWmWVRpLF4Oja7UDOwytdn2gAREghbDHXVDZVRi%2Bsz6blq5KMWI4B0e0LIA9ePboMQUqir7OrhJFBju6C3PW8KYmg%2B2q%2BpS7Reg7mypW8%2B6X%2BKCp61F2lnykuga0UOV5tnCNHXaepKyJd7o%2BKwAoyeF6vn7mIcgyWLWcSkpFYEv4FrMubgpaVWEr0olJYWQcwfspYboPwxy5AvdFwnGLFjfqfz2Xgq%2FlKcGXQREipin9rKo%2BeFtsg79ERcQQp4A5CbQM0joOOkf7sVZsumqXsFDJ4kMVAuzpMO%2B3%2F9IGOqUBk0uiJaX3JkeuhpSNknrK%2BW%2B%2BEVMxRKaarkCLOWqn4al3h6kvkX0ElEOBau4PDOg4wdveoYlfJoxjB9%2BE5Ss6brG4%2FsTjcjq9Elat1T5kGShDHhEa0t2RlB0e%2BxX00EHd084esfxepbKcBvHbmap2m3MRig1y%2FJOviGhlGq9JIlXGz1cpRRvDvX6Jw8CPmek3%2FRNonENNn1W%2BzUqL7ZBj4FCs98HE&X-Amz-Signature=3e59e65dc2bb5c9b281379cd9dba2ce539dee1dea440f9e6c353a86cbb732886&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

有 MAM cash，我们选Redis。看一看键值对系统如何来搭建好。之前飞扬老师已经提前建好了一个键值对系统，我们现在先尝试人工重新创建一个。这个创建过程因为会比较长，它比 MySQL 可能还要长一点，大概在 10 到 20 分钟。所以我们点完所有按键以后，就让它慢慢创建。我们之后就直接对飞扬老师前面已经创建好了一个空空的这样一个 Redis 来进行处理，来进行访问。


好，我们先看一看如果是从无到有点击创建实例需要怎么样创建。通常包年包月的，太贵了。这个时候 Taya 集群是高级的一个Redis，也就是阿里云自身在跑着的，或者是阿里系自身在跑的，也比较贵。通常我推荐实战就玩按量付费，本地盘便宜好。点完以后其实看到价格就明显的降低了很多对不对？我就近选上海好可用区直到 f 没问题。好，专有网络，它自动找到了两个交换机，也没有问题。 ready 是 5 集群版其实是有点贵的。标准版比集群版弱一点。读写分离版。什么之前的一组多重或者一组一重，我们选一组一重，这样最便宜的对不对？再往下看， 1G 也就够了是吧。这个规格其实也就够了，带宽也不用很大对吧？空间也不用很多。密码我们可以把当前就可以设置一个好密码，我们可以设置，比如像 i mock 下划线123， i mock 下划线123。好，设置好了。以后购买一台取个名字，不取就会自动创建一个名称。资源组不选也可以点击购买好，他会让你说什么？要点一个，我同意。好，你点了，我同意。


点击开通就进入了创建流程，我们等一等。好，我们回到 Redis 控制台，可以看到什么？是不是有一个正在创建中。创建中的飞扬老师刚刚点的，可能要等个 20 分钟，时间太长了，我们可等不起。我们就用飞扬老师提前准备的空空如也的实力。好，我们点进去看这个实例里面有些什么基本功能，是不是很熟悉。这就是跟我们服务器的安全组，跟我们什么 MySQL 的白名单一样的，大部分的存储资源、数据库资源、中间件资源都是采用白名单。我们这里要让服务器访问别人要什么，要开通一个白名单是吧。同时如果是第一次创建一个集群，那个集群是不是有可能还没有进入部署阶段。我们看看刚刚建了一个集群，是不是在创建过程中，创建完了以后，有可能它没有记录完整的部署，所以还要点一些键才能让它完完整整完成。通常完全完成以后，白名单就可以进行关联设置了。
我们添加一个安全组，这里有几个安全组，我们都把它加进去好了，无所谓这些安全组就是现成的安全组，应该已经包含了复研老师的常用的几台服务器了。把这些服务器所在的安全组都加进去以后，服务器就可以正常的访问。什么 Redis 好。我们还看一看 Redis 本身还有些什么特点。 Redis 当前没有开公网地址，但它什么允许哪个交换机允许我当前服务器所在的网络和交换机来访问，也就意味着内网我的服务器同时符合安全组的策略，就可以访问Redis。


同时 Redis 应该要设一个密码，我们去设一个密码，密码的设置在哪里？在正常的这种连接管理里面应该有，看有没有。这里可以申请公网地址，我们不申请，其实要访问的就是这个地址，这就是访问它的地址。这里可以设置什么免密访问，但是我们默认是不会设置免密的，所以我们回到主节点，我们找一找密码设置应该在账号管理这里，对我们可以重设一下密码。就跟刚刚说的一样，我们说成 i mock 小划线123， i mock 小划线123。好确定我们不是免密的对吧？我们是需要密码的。另外我们刚刚复制了一下它的什么访问的u、 r l。这样准备好了以后，我们其实就可以开始什么找一台服务器来访问它。我们就在原来，虽然老师已经有在服务器里面，随便找他们一台。好，我们去找到 e c s 服务器，还是用之前的测试数据库的服务器远程连接，点击登录这台服务器有个好处。
这台服务器什么？是个 Docker 的服务器？ Dota 的服务器。也就意味着我如果要去测试Redis，我不用去装什么 client 了，我直接起个 Docker 的容器就可以了。我们看看有没有什么 Docker image。已经提前准备好了，有一些常见的image，辅导老师其实经常会使用，所以通常都有看看。已经有一个叫 Redis 的 image 了，所以我用 Docker wrong 是吧。交互式就是杠 IT 的命令，去起一个 Redis 应该就可以了。起的 Redis 的一般性是什么？是直接采用这种 Redis 这样的镜像就好了，也不需要只称名称了。一次性对吧？就是一次性使用的，起完以后要指定它的什么命令？如果大家对 Docker 命令不熟，可以查一些官方文档。
Docker run 杠 it 交互式指定你的 image 名称Redis，默认不带冒号，默认 latest 后面指定启动的命令。 Redis client 要什么？要跟它交互。所以我们还要写一个什么服务器地址。我刚刚其实已经复制了一个服务器地址诶，这就是什么？它刚刚显示的。我们再给大家看一下。


刚刚在 Redis 管理界面，其实我们的实例里其实是会显示它的什么？它的具体地址了。这个地址好对应这样一个地址端口不？显然就是 6379 哈。我们就可以尝试来进行一次交互式的访问，我们看看能不能成功。诶，是不是交互式了？我们要输个密码 auth 是吧？刚刚的密码应该是 IMOCK 123。如果没错。好，我们 set 一个key，叫 key 1，值叫 value 1。好，我们回撤，我们 get 一下key，一看能不能拿到刚刚那个值。诶， value 1。很好很成功是吧？我们顺利地完成了Redis， Redis 的创建，写读都已经顺利完成。整理一下怎么样？很方便。怎么在我们的 Redis 控制台点出一个实例，设置好它的什么账号管理里面的密码，打开对应的安全组白名单，就可以完成什么 Redis 的内部访问了。还非常方便，非常简单。
好，我们来再来看一看。卡夫卡也点击左上角产品与服务。卡夫卡是属于消息队列其中的一员，我们就找到消息 MQ 有好多MQ，我们选中卡夫卡。好，卡夫卡我们什么找到一个部署实例。辅媛老师也提前准备了一个空空的Kafka，这个 Kafka 大概创建时间也在 10- 20 分钟左右，我们先去创建一个。在创建过程当中，我就采用提前准备好的 Kafka 给大家演示一遍。 Kafka 千万要学按量后付费，否则钱用光了可不要找费老师。我们就选标准版，便宜点的上海 VPC 最小配置高效云盘，磁盘数小一点，稍微省点钱，时间保留时间短一点，省一点钱对吧。
TOP1 个数不能再小了哈，一台哈也就 2 块多买了。我们点同意就买了。所有自愿购买都一样，要求什么？你至少有 100 元以上的余额，否则的会购买不成功。好，到了控制台，我们去看一下，当前应该有两个实例的对吧？一个是什么还没部署，一个是部署成功的没部署。其实要点一个部署，它不是创建完了自动部署，它在后部署的时候要选择，比如你的 VPC 也要选择什么，你对应的交换机，我们就选跟我们这台几台服务器管理的交换机。第一个可用区的交换机，点击部署就可以了。
好，部署好，点击部署完了以后，一小时的什么 3 块钱就开始收费了。部署过程我刚刚说的 10 到 20 分钟有点长。我们不管它，我们就连我们已经准备好空空如也的卡夫卡，大家熟悉对吧？消息队列首先要创建一个topic。好，我们自己来创建一个topic，取名叫test。备注也搞个 test 好。分区不用那么多，我看看有多少分区好，最少 6 个。好就选 6 个。


点击创建。等一下好，创建出来了，对 topic 是不是可以发消息了？好，我们这次不用它来发。我们用什么？我们用我们刚刚的客户端连到 Kafka 来发消息。怎么连上来？我们看一看实例是吧，有没有什么连接的信息诶？有这样的几个实际信息，这串信息我们肯定要复制下来。我们跑一个容器， Kafka 的什么客户端连到什么？用 boot strap 的方法连到 Kafka 的集群，对集群发一段消息，我们来实验一下好不好。好，回到我们的 Docker 这里，我们看一下 Docker images 里面有没有现成的卡夫卡诶？有的。不过它的名称好奇怪。不管它，我们就叫这个名称。跟刚刚一样。 Docker wrong 杠 i t 就是交互式。选中名称把镜像跑起来冒号。后面不写了， latest 就对应它。好命令是什么？命令是有串长长的命令。其实是一个长长的脚本，叫Kafka，后面应该是肯 so producer。这是新点的Kafka。通常是这样 Kafka console producer 点 s h。后面直接跟的是 boot strap 的这个地址，而不是 zookeeper 的地址哈，或者叫 broker list 也可以。我们把这段 Kafka 的地址在这里贴一下。对它跑一个基本的功能。跑完以后但是没有指定topic，基本上会报错。所以我们要指定一个 topic test 差不多。


Kafka 不需要白名单。 Kafka 是这样默认的在某个交换机上起的 Kafka 对同一交换机的所有机器都是内部联通的。好，我们回车一下，看看什么效果好。这在起容器好，容器箭头出来就是容器起来了。这个时候我们可以打一些话，比如hello。
My name is Fei Yang. How. 发了一个消息，我们就可以把它退出了。


can you see control d 好像卡住了。没关系，我们先这样。我的快捷键跟命令行和终端的快捷键有点冲突。好，我们已经发完这个消息。我们去看看能不能收到这个消息。我们在哪里？我们在消息查询这里，按时间查询，否则按点查询。要知道你的具体的offset，知道你的partition。有点麻烦。我们这里选test，分区选all，时间点就选今天。好挑选一下。有一条记录叫什么hello， my name is 飞扬，对吧？老司机没翻车。好，我们顺利的把什么把消息队列也跟大家演示了。当然，大家用SDK，用 Java 代码springboot，完全可以很方便。作为它的 producer consumer 去跟 Kafka 沟通，大家说我其实起个容器。 Kafka 搭建也很简单。但不要忘了，如果你要集群，而且要有很高级的功能，比如是监控，比如是一些额外的这种什么消息的安全保证，加密， CSSO 等等用户认证系统这里全都能提供。如果你自己搭建，要花很多精力。


我们聊完了 Kafka 聊完了。缓存键字对Redis。我们看看前面说的 search 诶，这里对吧。 search 在哪里？在这大数据里面就有我们需要的各种各样的search，比如像 is take a search，点进去这里就可以什么经典界面了。不管你是用 bits 还是 Logstash 来收集，是不是有一个 search 还可以什么？还可以企业 Kibana 进行界面展示。


好。除此以外，我们还聊到了另外一个什么。在分析下面我们能找到前面说的叫开放搜索，我们说的 open search 也是我们非常强调或者主推的。什么强大的QPS，高并发的开放搜索，虽然是有点闭源的套路，但是整体来看它的性能更强，它的什么倒排速度更快，查询能力更强。


好。除此以外还有什么？还有我们前面说的大数据很多的功能对吧？像 Max computer 这些功能，以及 AI 里面说的什么自然语言处理，机器翻译是吧？人脸识别。所有这些功能。其实什么都在大数据和人工智能相关的里面都可以点出来，大家不妨去点试试。总体来看，这些产品价格都非常高，飞扬老师资金有限， budget 有限，所以不再做进一步的演示了。大家希望玩大数据的，玩人工智能的，完全可以点点弄弄就可以弄出来了，非常简单好聊。
完了中间件的实战，大家有什么感想？语音平台要实现高可用，实现安全性轻而易举，只要配置得当，大部分的连接通过SDK，通过简单的命令行和图形化界面也能完成，相对是非常简单的好聊。完了中间件，下一个章节我们尝试什么？聊一聊语音原生当中另外一个很关键的点容器化技术，大家敬请期待。


