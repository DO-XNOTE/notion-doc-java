---
title: 3-28 【技术改造】电商系统集成Eureka - 用户中心-1 
---

# 3-28 【技术改造】电商系统集成Eureka - 用户中心-1 

[image](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/3d7e624f-f297-40eb-b79d-6dcbd87588c0/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SHYMEXKW%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T225556Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDnVpmqCX9oCAkIIXmYa6opzIYBlz9qsma%2Fuo%2BlT0e0YAIhAPqBDY0N2lCX0TpRqEbOfwU%2FgWHlGB0s%2FesjZGuZDf1sKogECMb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgzOhphj7xqxMOKXokwq3ANNFLkZac%2FgHVVZ7X09ML4ZDzQ%2FlzrWnd56gKSx8Mw4dLGOp%2BJGlzIHt7evYkKAOFAJJ6rUe7xJnXnaO7buUzEp4CqfQogZMeXEmI9LZ%2FDrLcMF7AFMOYlHs579DBdSI41UvUwIUzNItTpgktrOSircNmCeBWqLPBAJtcgZJkctK6cPifVsNxFARQhaLCOOqkjK%2BfnhFEoK0EXpfT0%2FC0KQzF9q5wOgrOv8A%2FNhAYfxOnj3QHg8oXc4vw%2BUDldUvr27CpyH6TDutioPqd%2FQpw7Xh%2FFSvzWSFeDWTexxqld13buiIqHx3T8VvYMKXGAWA6Tg5lDkJHB2Ob5G5CuvWKtPOm5uzsaMr9XyGAkODcwXdSswrp8ZMFf7jN0A%2FqZhFGwTUPzkzbSugVDkWKyirLbZJXGyyTaYk5R%2F5SkbR7T4QxDCBBCwOw3RjWYmYRVD40o5kFIGbsTd5blEXh3iQkDkEw5gk3VkpRAwdPeF%2F9uIaL729CNs5w8NIn5geaoeQ67wUr8mIyefl2kvIQvai5YOUaPpBy1Ka3OyfbmV3SHQywrvWPivbbL%2FYXcWqNRculzWJWOhlfOz5oRi%2BftVFuH8PbvZD0h0KkJ4xM1GtXGHV8kdfOM%2Bf5%2BaogbNhjC0t%2F%2FSBjqkAddeusoM0JU6R%2F75Mg0bGGt%2FdHK9BjvinEblqNQj2HrznakenzXo%2Fz2pygKxS9XmZMN1%2FCnFbsE%2BT%2FH21PMPVivG2%2F%2FTWZY82IPDWdnDjm%2Fg3Ke98O8ra%2FP1TYRjsU9abKI%2FqRRHuKZPJVGaVDjdO6OYcoqIO7zuE7y%2FBRIPS1FOmfBhwpUerkCm%2FjQbA8u%2BCpihCNojIAG47Ry8C9Xors5d2UY9&X-Amz-Signature=89d5255cf63f8b80ebf3b2e289f71c200811acf8f892e3a6d82c99f3d00b4564&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

[image](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/9f656b09-e980-45d7-b48e-4dacd4419839/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SHYMEXKW%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T225556Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDnVpmqCX9oCAkIIXmYa6opzIYBlz9qsma%2Fuo%2BlT0e0YAIhAPqBDY0N2lCX0TpRqEbOfwU%2FgWHlGB0s%2FesjZGuZDf1sKogECMb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgzOhphj7xqxMOKXokwq3ANNFLkZac%2FgHVVZ7X09ML4ZDzQ%2FlzrWnd56gKSx8Mw4dLGOp%2BJGlzIHt7evYkKAOFAJJ6rUe7xJnXnaO7buUzEp4CqfQogZMeXEmI9LZ%2FDrLcMF7AFMOYlHs579DBdSI41UvUwIUzNItTpgktrOSircNmCeBWqLPBAJtcgZJkctK6cPifVsNxFARQhaLCOOqkjK%2BfnhFEoK0EXpfT0%2FC0KQzF9q5wOgrOv8A%2FNhAYfxOnj3QHg8oXc4vw%2BUDldUvr27CpyH6TDutioPqd%2FQpw7Xh%2FFSvzWSFeDWTexxqld13buiIqHx3T8VvYMKXGAWA6Tg5lDkJHB2Ob5G5CuvWKtPOm5uzsaMr9XyGAkODcwXdSswrp8ZMFf7jN0A%2FqZhFGwTUPzkzbSugVDkWKyirLbZJXGyyTaYk5R%2F5SkbR7T4QxDCBBCwOw3RjWYmYRVD40o5kFIGbsTd5blEXh3iQkDkEw5gk3VkpRAwdPeF%2F9uIaL729CNs5w8NIn5geaoeQ67wUr8mIyefl2kvIQvai5YOUaPpBy1Ka3OyfbmV3SHQywrvWPivbbL%2FYXcWqNRculzWJWOhlfOz5oRi%2BftVFuH8PbvZD0h0KkJ4xM1GtXGHV8kdfOM%2Bf5%2BaogbNhjC0t%2F%2FSBjqkAddeusoM0JU6R%2F75Mg0bGGt%2FdHK9BjvinEblqNQj2HrznakenzXo%2Fz2pygKxS9XmZMN1%2FCnFbsE%2BT%2FH21PMPVivG2%2F%2FTWZY82IPDWdnDjm%2Fg3Ke98O8ra%2FP1TYRjsU9abKI%2FqRRHuKZPJVGaVDjdO6OYcoqIO7zuE7y%2FBRIPS1FOmfBhwpUerkCm%2FjQbA8u%2BCpihCNojIAG47Ry8C9Xors5d2UY9&X-Amz-Signature=df4b66a58815156f7720f7310c93bc08b96383a3b5d239e870c0ecb89cabf43e&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

hello 我们课网的各位同学们，大家好，在这一节当中，我们开始对用户中心进行剥离和改造。咱用户中心的业务主要是围绕在用户信息的管理、登录注册这一类。那有前面商品中心的改造经验，那我们用户中心这里就快马加鞭，加快进度，那同学们我们就 in 泰迪 J 里面见。

[image](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/343c9ae2-dab0-40ad-9d5e-ae745238821d/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SHYMEXKW%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T225556Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDnVpmqCX9oCAkIIXmYa6opzIYBlz9qsma%2Fuo%2BlT0e0YAIhAPqBDY0N2lCX0TpRqEbOfwU%2FgWHlGB0s%2FesjZGuZDf1sKogECMb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgzOhphj7xqxMOKXokwq3ANNFLkZac%2FgHVVZ7X09ML4ZDzQ%2FlzrWnd56gKSx8Mw4dLGOp%2BJGlzIHt7evYkKAOFAJJ6rUe7xJnXnaO7buUzEp4CqfQogZMeXEmI9LZ%2FDrLcMF7AFMOYlHs579DBdSI41UvUwIUzNItTpgktrOSircNmCeBWqLPBAJtcgZJkctK6cPifVsNxFARQhaLCOOqkjK%2BfnhFEoK0EXpfT0%2FC0KQzF9q5wOgrOv8A%2FNhAYfxOnj3QHg8oXc4vw%2BUDldUvr27CpyH6TDutioPqd%2FQpw7Xh%2FFSvzWSFeDWTexxqld13buiIqHx3T8VvYMKXGAWA6Tg5lDkJHB2Ob5G5CuvWKtPOm5uzsaMr9XyGAkODcwXdSswrp8ZMFf7jN0A%2FqZhFGwTUPzkzbSugVDkWKyirLbZJXGyyTaYk5R%2F5SkbR7T4QxDCBBCwOw3RjWYmYRVD40o5kFIGbsTd5blEXh3iQkDkEw5gk3VkpRAwdPeF%2F9uIaL729CNs5w8NIn5geaoeQ67wUr8mIyefl2kvIQvai5YOUaPpBy1Ka3OyfbmV3SHQywrvWPivbbL%2FYXcWqNRculzWJWOhlfOz5oRi%2BftVFuH8PbvZD0h0KkJ4xM1GtXGHV8kdfOM%2Bf5%2BaogbNhjC0t%2F%2FSBjqkAddeusoM0JU6R%2F75Mg0bGGt%2FdHK9BjvinEblqNQj2HrznakenzXo%2Fz2pygKxS9XmZMN1%2FCnFbsE%2BT%2FH21PMPVivG2%2F%2FTWZY82IPDWdnDjm%2Fg3Ke98O8ra%2FP1TYRjsU9abKI%2FqRRHuKZPJVGaVDjdO6OYcoqIO7zuE7y%2FBRIPS1FOmfBhwpUerkCm%2FjQbA8u%2BCpihCNojIAG47Ry8C9Xors5d2UY9&X-Amz-Signature=cb35771d7cf5b6801d32663945c58feedad7183971271ef4b97ef722d4e56ce2&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

好，那我们开空了，还像上次一样，咱先从 poto 这个类开始做起啊。啊我们这里创建一个 directory 是 user 证明它是用户的领域模型，然后创建一个 module 第一个 module 我们给它起名叫 food 杠 user 杠 pojo 好，点击 next 然后把它塞到哪个文件夹，塞到 domain 下面的 user 这个文件夹里，点击 finish 那这个 dependency 和咱前面创建的商品中心是一样的。所以我们在商品中心 item 抛折这个项目里面，把这两个 dependency 给它 copy 过来，复制到哪里，复制到咱刚才创建的 user 抛出这里。


好，那这创建完了之后，咱就开始去迁移代码了，我们在 Java 文件夹下面创建 come.imock 然后后面跟 user hold you 路径名要注意前面看同学们把路径打错，导致这个道层没法解析出来，尤其是后面的 mapper 路径都要特别注意这个路径名称不要打错。


那咱接下来看一下 user 抛出下面有哪些类需要迁移，我们切换到 foodie DEV 好，我们到 polo 这里开始抓壮丁了，跟 user 有关的不多，就这俩一个是 user address 还有一个是 users 好，我们把这两个 copy 一下迁移过来直接复制过来就好了。那我们这里需要把它的 package 给更正一下，设定到 user 这个包路径下。
OK 那这两个数据层的 entity 创建完之后，咱们开始去移植业务类了，那这里给他创建一个子文件夹叫 BO 接下来再去抓壮丁。 BO 对象，我们切换到 food DEV 当中，看这个 BO 哪些是跟 user 有关的。我们看第一个 addressbo 还有 user BO 好把这两个拿过来 copy 进来。那咱们每次迁移之后，同学们都注意一下这个编译里面有没有出现错误，因为咱的包路径换掉了，一不小心很容易编译出错。


接下来我们在 BU 里面再创建一层文件夹，是谁呢？是 center 用户中心这个 center 咱的文件夹结构也和福地代瓦保持一致。好我们再切换到 foodie DEV 拿到 center 下面的这个类只有一个就是 center user BO 我们把这个类给它迁移过来， copy 到 center 里面。 OK 那这里抛休对象就已经写完了。
接下来第二个 module 我们去写 mapper 好，这里创建一个没问类，然后 artifact 写 OD 杠 user 杠 mapper 点击 next 同样的，这个毛9，它的位置是在哪？是在 domain user 里，不要跑偏了，写到商品中心了，咱们把它放到用户中心。 OK 那咱在这个 mapper 模块下，它的依赖项也可以 copy 之前商品中心创建的 mapper 依赖项，这前任在数后人乘凉。


好，我们把这个依赖项 copy 过来 copy 到 user 里，但是这里要改一下，看这个引用的是 item 的pouch ，我们把它改成 user 的 pouch 好，这就完事了。同学们发现你分拆完一个微服务，后面的微服顺理成章，非常简单。熟练的话你一上午就能把这所有应用都给拆解完。
我们接下来在 mapper 里创建一个 directory 是 com.imock.user.mapper 我现在每次写代码，这个 com.imock 都深深地印在脑海里，我是天天打爷爷打这个路径，上次在公司写公司的项目，莫名其妙也打成了 [com.mo](http://com.mo/) 我们同事就奇怪了，这是什么东西，我只好顺带着安利了一波我的课程。


好，那咱这个包创建完了之后，继续去 four D DEV 里面抓壮丁，现在抓到 map 里面了，咱把这个属于用户相关的这个 map 给它揪出来都有哪些不多。就最后两个用户以 user 开头的 user address mapper 和 user snap 把这两家伙抓过来走，你进来。那 package 我们这里要改一下，然后引用类的时候，这个 user address 后面把它的报名给他打全。那同样的，下面的 users mapper 咱也给予他一样的待遇包名，还有他引入的这个 user 类，把他的路径更正过来。
那这两个改完之后，我们就可以去迁移 resources 的。在 resources 文件夹下面，我们给它创建一个路径叫 mapper 好，我们这里去切换到 food DEV 那走到 mapper 里面开始拉壮丁，咱的 mapper 是在这里。好，我们看哪些 mapper 跟 user 有关呢？依然是这倒数后两个，我们把它 copy 一下，拿。粘贴过来以后这里同样也有路径的问题。我们把 com.imock copy 一下，用替换工具，把 com.imock 改成 com.imock.user 全局替换。那同样的下面的类，下面这个 map 我们也用这种方法把它里面的路径全去替换过来。


OK 了，那到这里 mapper 也创建完了，非常的迅速。那紧接着咱去创建 user API 好，我们这里新建一个没问的毛九，给它起名叫 user a foodie 杠 user 杠 API 好，点击 next 毛球 name copy 一下，把它的文件夹路径定位到 domain 杠 user 下面已经 finish 那 user 子模块它的 pom 文件我们也可以借鉴 item API 好，我们到 item API 里面抄作业，咱把 item API 这 dependency 里面加上的三个依赖项统统 copy 过来。好，我们放到这里。那然后其中有一个要改一下，看到这里引用的是 item post 我们把它改成谁改成 user post 只有这一个改动。那改完了之后，我们去扯一扯代码。


在 Java 这个文件夹下面，我们再次创建 com.imock M 格后面跟谁 user.service 多打了一个 E 好，这就对了，别看它的 portual 类不多， mapper 力不多，他们的 service 还真的不少。那我们继续到 food dive 里面去拉壮丁，那都有哪些 service 层，它的接口需要 copy 过来呢？好，我们到 foodie DEV 这里去找跟用户中心有关的service ，首先 address service 是不是把它拿下。最后一个 user service 好，这两个 copy 一下再切换回去，我们把它先给复制过来点击。 OK 好嘞，那接下来我们干什么？更改包路径对不对感觉现在做的工作有点像这个流水线的男工女工，这里第一个泡酒没有用到给它删掉。


好，下面的两个 portal 把它路径补上。 OK 那接下来下面的这个 user service 一样的待遇，把它这里面的没有补全的路径给它补上。然后怎么样呢？我们要去给它定义 mapping 什么？ mapping controller 里面的路径寻址 request the mapping 好，我给它起一个什么名字，响亮一点的名字叫 address API 好像也不怎么响亮。那接下来每一个服务这个给它叫 getget 什么呢？ get list 好了，叫 address list 。
接下来的一个是用户新增地址，这是一个 post 了 post 叫什么呢？就叫 address 咱不用再叫 add address 这个添加动作已经被下放到了哪里呢？到了这个 HTTP method 的类型 post 那与其对应的用户修改地址，我们这里用什么呢？用 put 标准的 rest 接口规范。


那 put 学 put 也是 address 这两个是一样的，唯一区别是什么？ master 类型不同对不对？ OK 那我们接着往下走 delete user address 终于用到了咱不太常用的 delete mapping ，有的公司其实是不允许 delete 的，甚至会在网关层怎么样把你的 delete 请求全部给它封杀掉？比如我们公司就是。对这种情况怎么办？我用 post 来 delete 对不对？那还不好绕过去吗？接下来的是修改默认地址，那它这不是修改某个地址的内容，它是去设置你的默认地址。那我们给它一个 post 它的名称叫什么叫 set default address 好设置默认地址。


那最后一个查询我们这是一个 get 命令，那它的路径也叫它 query address 这个 hs 好像拼错了，少打了一个 S 大丈夫不拘小节。 OK 我们继续给每一个入参指定 request parameter 那这是为了什么，这是为了应用份的时候，它不会报错。我们这里给它叫做 user ID 那它叫 user ID 我们往下你叫什么？ address bill on 什么名称都没有给你安一个 request body 好了，那同样的，下面这哥们也是 request body 好勒，那再往下我们要把这一行 copy 下来。那再往下的这个接口。第一个参数， user ID 第二个参数 address ID 放过来。那再下面一个方法是一样的，我们直接把这个入参给它 copy 一下， copy 完粘贴到这里。


OK 那最后一个依然是一样的参数，我们把它 copy 过来。但是老师记得，好像下面的这个参数可能是允许非空的，对不对？可能允许空。那我这里给它加一个 require 的，等于 falseok 那 address service 定义完了之后，我们去到 user service 这里。好，这个 user service 我们也用同样的方式把它每一个方法给它定义一个访问的路径。那首先是这个类顶层的这个类，我们把它的访问路径定为什么呢？叫 user API 那第一个方法它是判断用户是否存在的一个方法，那我们给它叫get ，那它的路径我们就叫 user 杠 exist 那第二个方法其实是创建用户，这个注释好像写错了，是创建用户，那我们给他一个是叫 post post mapping 那它的路径就是 user 最后一个。当然是检索用于登录的，那这里依然给它一个 mapping get mapping 它叫 verify 好了，verify什么呢？去看你的用户名和 password 是不是匹配。 OK 那接下来我们给它每一个字段指定 request 的 parameter 第一个是 username 这个没问题。那第二个先把它晾在一边，咱先去看最后。第一个参数 username 没问题。第二个参数。 Password. 好，现在回过头来给这哥们添加一个 request body 好勒，那咱这个类也已经处理完了。


好，这个 service 没有全部做完，我这里给它添加一个新的 package 这个 package 给它起名叫 center 走。你好， center 里面去移植谁呢？我们到附地 DEV 里面一看，究竟我们打开 center 目录，找到那个跟 user 相关的非常显眼，就是这个名字里带 user 的他 center user service 我们把它复制一下，切换回来给它 copy 过来。


好嘞。好，那接下来又要做流水线工作了，把这个 import 给它规整好，就要 user.portal 第二个也是的，下面我们要给 center user service 指定寻址地址 request mapping 那它的名字我们就给它起叫 center user API 好了。
那第一个方法是什么？是查询用户的信息。那我们这里一个 get mapping 叫 user info 或者我们用更标准一点的做法叫 profile 用户的个人信息，个人档案一般叫 profile 好，那接下来第二个我们给它起名叫 toot mapping 修改用户信息。那它的路径我们给它写 profile 杠这里添加一个 user ID 好，那后面这边是用户头像更新，我们给他写 post 好了，我不写 update 了，可以叫 update photo oto 好嘞，那接下来给这些属性添加寻址地址。
第一个 request parent 它的名称是 user idok 那第二个这里我们在路径里面给定了 user ID 那所以把它定义为 pass variable 那它的名称是 user ID 第二个参数叫什么？ request body 对不对？好嘞，那接着往下看。


下面这个 user ID 我们把第一个的参数给它 copy 过来。 copy 的第一个参数，第二个参数叫 vase URL 他把这个也给 copy 过来。 OK 那这个文件就创建好了，到现在我们已经创建了 user portal user mapper 和 API 效率非常非常高。那接下来我们要创建的是 user service 不过我们在创建 user service 之前要做一点小改动。什么改动呢？因为咱们在这一章节当中用到了 Redis 对不对？ Redis 在之前是没有加入到我们这一个 foodie cloud 当中的。那我们现在要把 Redis 的一些通用组件给它加入进来。那我们要加入哪些内容呢？首先我们打开 common 下面的 food cloudcommon 好，在这里找到 common 文件，咱要先把 Redis 的依赖给它加入进来。就在这里。好，我们切换到 foodie DEV 把这段依赖给它 copy 过来，我得 dive 的这一段依赖 Redis 依赖。


那 copy 过来以后，我们这里还要引入一个 Redis 的工具类是谁呢？我们把它所在的文件夹先给它打开。好，我们打算把它放到这里 youtuss 文件夹下面。 OK 那我们知道放到哪里了，现在该去找人了，我们切换到 hold DEV 把跟 Redis 相关的这唯一一个工具类 Redis operator 给它找到。 OK 就是它了，copy一下切换回 goody cloud 然后把它直接粘贴到这个 YouTube 包下面。好嘞，刚才我在后台重新跑了一把 RE import 那这里已经不报错了。那现在 Redis 已经就绪了，接下来我们就可以去创建谁创建 foodie user service 了。那这一部分我们就放在下一小节跟同学去手把手一起去做，久坐伤身，同学们合不起来撒泡尿休息，我们下一小节再见。


