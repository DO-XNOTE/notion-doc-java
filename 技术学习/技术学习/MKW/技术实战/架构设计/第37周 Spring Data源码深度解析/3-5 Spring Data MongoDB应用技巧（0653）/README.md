---
title: 3-5 Spring Data MongoDB应用技巧（0653）
---

# 3-5 Spring Data MongoDB应用技巧（0653）

[image](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/8288e9a0-8df1-44b3-b89f-34d232e58533/SCR-20240814-jjht.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SNCMFJRN%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T232145Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIGwgpOImsrfnuHTJ1YcZua%2Bcgk69MCjKidXCQcPeDN6fAiEA5Xyc3TT6YFvX5ILlClZVdr3vCXHuZVaIhuc8jS5y3EkqiAQIx%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDKTH2hUMWNX1CgJEhyrcA4JzMOV8TCspBwPoJfe3viIYG9O4nyNgSFv%2Bteet6V%2BeB4LgLUeoUM3unTb4j8XxILVre%2BhRNEbUDxQfd7sg4cAFm631o8qoK5c5zOzZ2ZLTZ73i1eKPQvfyD2cEdzrCoEmGn69RD2qv%2FJbYGm%2F08OT121U6Vp1bBs%2Bhp40gZwz15Sih5FVk521lbKA4QPQbQN6myDqmhPYsQrJM7JyJyjEUHVX9ihRrvBgLLSHlfO6EtW8grSAOnZVEKADPMKR6b%2Fn6bEh6mqB19mNCjSDWrQ4Q91AuMI6XTQoW3zuRRK2qwlJ0t8Fp2S42ed3z1ouzIXtchY7NNcgPcNYvW1%2BKGOz137Q2Slr%2Fj6iMxs1aZz%2FyqQgVerNJagWWzLjyxXmANVHRfzNbdodJ%2FCKamxbHDzbstL5nPtYzFmZ7AOtF9SXqcWQL02Z9NfzbJicIwWlTuNeH%2Bsj1yQSqIgK8vmwAsr0Ocq%2BUaUcqy3SArvFUHgKVgpFiHvCYds3QJdGL2HLV533CSklX%2F6vssuftSvU%2B6h%2FP5OP92oRDQczqztyf8apQRYx6vg5g0JTosMmeMkx89oa9cyYBqSBjGaDKyv63Y8JbtRz7vw1PxLAlylpe4%2BO7OcNoHwR1JkuFS%2BqWMP3O%2F9IGOqUBFSstEJ6CsV6YdCRUtR4eIDcB99pQAkrp1yfj8KQDOcD4CEX1XXQwmhEcD1JJisghN4j4xHng1LA4Q1%2BUPmHKOAd5wcDVCR4e%2FffK4EhSQpxhwePHdQA1pbPMPI7ZHioKGf2dnJbV0mZfVOM%2BRXrtGMBfGtbQnPwU%2FjJjb00FfbwrxxvEXnMvAsp8U8yzygY5C4VFS7SyEfTJaSzR7oyP21hSSIw3&X-Amz-Signature=ad210b5b8e74b1e67bc1fd3f6f70bc688f9a81190dede7842bd8d85127af4bd9&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

[image](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/899e54c4-9b58-43f2-ac60-fc3b6429ae7a/SCR-20240814-jhtu.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SNCMFJRN%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T232145Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIGwgpOImsrfnuHTJ1YcZua%2Bcgk69MCjKidXCQcPeDN6fAiEA5Xyc3TT6YFvX5ILlClZVdr3vCXHuZVaIhuc8jS5y3EkqiAQIx%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDKTH2hUMWNX1CgJEhyrcA4JzMOV8TCspBwPoJfe3viIYG9O4nyNgSFv%2Bteet6V%2BeB4LgLUeoUM3unTb4j8XxILVre%2BhRNEbUDxQfd7sg4cAFm631o8qoK5c5zOzZ2ZLTZ73i1eKPQvfyD2cEdzrCoEmGn69RD2qv%2FJbYGm%2F08OT121U6Vp1bBs%2Bhp40gZwz15Sih5FVk521lbKA4QPQbQN6myDqmhPYsQrJM7JyJyjEUHVX9ihRrvBgLLSHlfO6EtW8grSAOnZVEKADPMKR6b%2Fn6bEh6mqB19mNCjSDWrQ4Q91AuMI6XTQoW3zuRRK2qwlJ0t8Fp2S42ed3z1ouzIXtchY7NNcgPcNYvW1%2BKGOz137Q2Slr%2Fj6iMxs1aZz%2FyqQgVerNJagWWzLjyxXmANVHRfzNbdodJ%2FCKamxbHDzbstL5nPtYzFmZ7AOtF9SXqcWQL02Z9NfzbJicIwWlTuNeH%2Bsj1yQSqIgK8vmwAsr0Ocq%2BUaUcqy3SArvFUHgKVgpFiHvCYds3QJdGL2HLV533CSklX%2F6vssuftSvU%2B6h%2FP5OP92oRDQczqztyf8apQRYx6vg5g0JTosMmeMkx89oa9cyYBqSBjGaDKyv63Y8JbtRz7vw1PxLAlylpe4%2BO7OcNoHwR1JkuFS%2BqWMP3O%2F9IGOqUBFSstEJ6CsV6YdCRUtR4eIDcB99pQAkrp1yfj8KQDOcD4CEX1XXQwmhEcD1JJisghN4j4xHng1LA4Q1%2BUPmHKOAd5wcDVCR4e%2FffK4EhSQpxhwePHdQA1pbPMPI7ZHioKGf2dnJbV0mZfVOM%2BRXrtGMBfGtbQnPwU%2FjJjb00FfbwrxxvEXnMvAsp8U8yzygY5C4VFS7SyEfTJaSzR7oyP21hSSIw3&X-Amz-Signature=b64f9083d850afacdb815cb24eb4a225ec215e0d2117880464785632518dfb8b&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

大家好，这章节我们来介绍一下 spring day 的 MongoDB 的应用技巧解析。涉及到 MongoDB 的，我们这里面重点介绍的还是 MongoDB 的template。对于 MongoDB template，它跟 JDBC template 很相似，因为我们对 MongoDB 数据库的操作跟关系型数据库操作它的 API 也非常接近。那么对于 Mongo template，这里面我们知道 Mongo terminate 它实现了 Mongo operation 这个接口。同时构建 Mongo template 过程中，我们需要指定一下我们的mongoclider，那么 mongoclider 它可以理解为我们对应的 this source，也就是跟我们 MongoDB 进行构建链接的一个客户端，那么我们通过 Mongo template 进行包装，这样的话我们可以完成对 MongoDB 数据库的 document 的增删改查，来看一下 Mongo template 这个类它实现的过程。


那么我们先切换到我们的 showcase MongoDB 这个模块，这里面我们定义一个 mongotemplate test，我们通过注入的 pass 把 template 这个类注入进来，那么我们可以看一下，我们可以切进去，这里面我们选择 Mongo template 作为注入，或者说是我们选择 Mongo operation 注入，它的效果可以理解为是等价的。那么这里面我们如果说选用 Mongo operation 的话，这里面跟我们定义的这些操作会更直接一些。这里面他们的关系也是类似于我们的 GDBC operation，它下面有对应的 GDP template，那么这个关系构建完成以后，我们可以通过 GDP to reason 进行操作。如果说我们使用 GDP template 会感觉操作要比 DBBC appraisy 会更方便一些，同时这里面也是更建议大家去直接使用 Mongo template 也可以。


如果说我们基于一个依赖抽象而不依赖丝线的原则的话，我们好像更多的应该是使用 Mongo operation，这里面对大家不做强求。如果说大家对源码比较感兴趣的话，我们可以使用 mongotimerly 的，可以对里面的一些内容来进行更多的一些熟悉。


如果说我们是遵循一个依赖的规范，那么说我们可以基于 Mongo operation，那么我们依赖 Mongo operation，这样注意一个接口，它的抽象性会更高一些，那么说一说它的稳定性更高一些。那么我们来先看一下门口 person 下面它有哪些操作？这里面我们可以看一下对于这些操作跟我们 GDBC template 操作的类型很相似。首先这里面我们总结起来，也就是对于这些增产改革的操作，我们可以看到这里面是一些批量的操作，这里面是判断 collection excess，就是判断一下当前对应的这个，因为在 MongoDB 里面我们对应的是collection，那么 collection 的话我们判断它是否存在。这里面是查询 count 相关的，这里面是我们创建 create collection，下面还有一些像我们删除collection，我们就可以理解为对应删除一个表这样一个操作。


这里面我们执行一些 collection callback，因为我们在 GDVC 操作的过程中也有一相关的一些 call back，我们对于把我们获取到的一些 result set 级量化进行了一些整理，下面我们可以看到这里面会基于 query 和 class 去判断当前指定对象那是不是存在，或者说指定的一些查询是不是存在。这里面还有 find all and remove 相关的一些操作，这里面是 find and multify，也就是我们查找完出来再进行修改。


那么通常我们 GDPC 修改的过程中，我们直接就会执行一个 update 语句，但是我们使用 GPT 操作更次面向对象的操作的话，我们通常会把整个对象读取出来，那么我们重新更新对象的值，然后进行一个save，通过这种方式更新的话看起来更符合我们一个面向对象的原则，那么我们这里面实现我们看是 find end modify，也就是说我们会首先把对象查找到这个对象，我进行一个更改，更改完再进行保存。


是基于这样一个逻辑，下面也是我们可以看到还涉及到 find by ID，大家这个非常容易理解，这里面还涉及到 find distinct，那么我们知道 distinct 是查找嗯，不重复的内容，这里面是 find one。总之我们去看到这个 Mongo operation，它的这个接口定义的这些方法跟我们 GDBC prison 相关的是很相似，所以说基于我们对于它的这些理解的话，我们可以很快的去使用这些 API 快速上手，那么这是我们的 Mongo operation，那么对于 Mongo reason 它的实现内也就是我们的 Mongo template，那么对于 Mongo template 我们可以看到它在构建的过程中它依赖Mongoclient，或者说是它依赖我们的 MongoDB factory，也就是构造我们 MongoDB 的一个过程。这个其实它是可以理解为是等价的。


我们可以看到我们这里面传入的 Mongoclient 会在这里面构建出一个 simple Mongoclient DATABASE 的factory，也就是说最终还会使用 Mongotobase faction 的方式，这个构造方法进行一些指向，这是它创建的 mongotemplate 的一个过程，那么我们可以从这里面去看到对应的这个 Mongo template，它还需要依赖到哪些相关的这些属性。


我们看到是 Mongo convert， Mapping context 的这些信息，这里面也涉及到一个持久化的 exception translate，跟我们 GDB seed 一个算 translate 跟刚才依赖色子的 translate 其实都是很相似的，这也就是对我们 Mongo 的 exception 封装成我们 spring date 对应的exception。这里面还会有一些 Mapper 因子关系， query Mapper，我们的 update Mapper，我们的 JSON schema Mapper 等等。


其实在命名为Mapper，大家会联想到我们在使用 mybytes 过程中，我们会在 DAU 层这一类的接口都命名对应的Mapper，那么基于 Mapper 进行一个跟数据库相关的一些操作，这里面还涉及到一些，我们看这里面是 connects resolver，还有一些对于 right result 的一个checking，对一些结果级的一些校验检查。但其实这对于 Mongo 它也支持一些审计操作奥迪艇，那么它跟 GPA 的奥迪艇磁器是类似的，我们在后面关于二次改造的环节会基于 GPA 的力挺去做一个审计的一个实现。


那么回到我们 Mongo template test 这里面，我们可以看到，如果说我们要去进行一些 query 操作，对于我们使用 Mongo template 进行一些原生的操作，我们可以看到，首先我们需要构建一个 query 对象，那么我们基于 query 对象和我们 user 这样一个类，它 user 类它可以映射到我们对应的 Clacson 这样一个感关系。


我们会通过 query 进行我们这个 query 对象的创建，那么 query 对象创建的这些条件构造是基于我们一个标准的一个查询对象 criteria 进行一个构造，那么我们这里面指定一下我们的条件，我们的 word name 意思 name 杠一，也就是说它跟我们对应的 GDPC 层的 SQL 也是类似的，我们可以理解为我们的条件就是针对的是name，等于 name 杠一这样一个戳会找到对应的用户，那么因为这里面我们并没有去指定精确查询，它返回的都是一个历史的一个对象。


那么这里面不管是一条记录还是多条记录，都会包装到一个 list 里面，这里面我们可以通过对于 list 迭代来去观察我们获取到的一些信息。那么关于 string 的 Mongo 的一些应用技巧，我们就简单介绍到这里，同学们，我们下一章节再见。

