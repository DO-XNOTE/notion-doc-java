---
title: 3-29 【技术改造】电商系统集成Eureka - 用户中心-2 
---

# 3-29 【技术改造】电商系统集成Eureka - 用户中心-2 

[image](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/1e2c5bf6-948e-493a-a653-7112015507dc/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665HET7IWM%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T225556Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCICk1LFsJtEO02uCczYrOEAS%2BPaODbBx2efxeXBv4UZVDAiEAklrK7qR83YwLV3SKBc80Sy5CO0WycYPBdnAswfUQVTsqiAQIxv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDMOJKyYvgnsxkLxotSrcA1AW66YvJcovdHQZBQ3ZjIx9%2Fz%2FpFmsgVgwCNcW3JivjCPn1a0Ti8IzQUKLyrBNODZuCsKf9uv%2Bvqt5ttvdWrFyt6s43z%2BA%2BhQcbzssJ56dgzyW1XBp%2BcmObpMCOSkT1sAqGCLzXKwz2%2FE%2BWyKiznk1rN3SXdiFjBjUAfZda24J7t8%2BngkT2Q%2FKp58SoDvcWGULsmyJtvEkxBsJN1EBS%2BdxV4kX10WjWN7k%2Biyd3aVZCdLEwuWQhjcWN%2FoTbkZTqs74uD%2B4onTX4BcfQOieOC5mp%2FzzfnLXSaHfyW%2B0OJWVpg28ifXFvS7xpKSHetJgswp2qCqUhxDAIa2UA4fBxh9mNhxy31wu81TCQNMgu3s7Wx7I7eAgbEVWF5d%2BlhT6R%2Bugz052Am9LAdQ0NLtB3tA1mrCh74UeYWMc71Dnyd4QkvO43yYx91ZNRYou1FbmYWL3148e%2B9ct752cIDPyi6MQrmzsJ4wD5NTdBY41tQlL9G5TGFQz7BxtyXBMrFQsImSmZEv%2FMUS66Q68eI2g5gcP3UTmKhH0moyz7wBpRKB%2BIFJe5Vt7rQX0PZjs1EOCReghMqEP8xjvirnUs03a%2FGOFojOD8fFa731XI2Zi%2FMzoEPh%2BMdJuTsVRSQZ7cMKG4%2F9IGOqUBTmTtFItK49%2BI6JiGUQ%2BwuKi3%2BCHylox7wQw1ghu%2FDNTbkQZpNvtUDtllfuQFsTOaT8neci0K0CRRqJ7LTePIHppFnvDiNf1tmX%2BZln7PLlBKJ4zSzZZtptLrwAZh2p06ljcjD9zoeB%2FJuz%2FIozfyzXiJkfpv6%2BR7VLX5Uoh4LZPu2bvn4lxf0JD9iGvyimw367p4nVqQSA7XJfAsASuFaDVcBd6k&X-Amz-Signature=134f8f1d9c080ccf2814b9109d7149899cb6ff44f5042ae7ca2784c0fd62f3b4&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

[image](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/ddda2032-534b-4fe2-80c0-cb6ab265ea50/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665HET7IWM%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T225556Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCICk1LFsJtEO02uCczYrOEAS%2BPaODbBx2efxeXBv4UZVDAiEAklrK7qR83YwLV3SKBc80Sy5CO0WycYPBdnAswfUQVTsqiAQIxv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDMOJKyYvgnsxkLxotSrcA1AW66YvJcovdHQZBQ3ZjIx9%2Fz%2FpFmsgVgwCNcW3JivjCPn1a0Ti8IzQUKLyrBNODZuCsKf9uv%2Bvqt5ttvdWrFyt6s43z%2BA%2BhQcbzssJ56dgzyW1XBp%2BcmObpMCOSkT1sAqGCLzXKwz2%2FE%2BWyKiznk1rN3SXdiFjBjUAfZda24J7t8%2BngkT2Q%2FKp58SoDvcWGULsmyJtvEkxBsJN1EBS%2BdxV4kX10WjWN7k%2Biyd3aVZCdLEwuWQhjcWN%2FoTbkZTqs74uD%2B4onTX4BcfQOieOC5mp%2FzzfnLXSaHfyW%2B0OJWVpg28ifXFvS7xpKSHetJgswp2qCqUhxDAIa2UA4fBxh9mNhxy31wu81TCQNMgu3s7Wx7I7eAgbEVWF5d%2BlhT6R%2Bugz052Am9LAdQ0NLtB3tA1mrCh74UeYWMc71Dnyd4QkvO43yYx91ZNRYou1FbmYWL3148e%2B9ct752cIDPyi6MQrmzsJ4wD5NTdBY41tQlL9G5TGFQz7BxtyXBMrFQsImSmZEv%2FMUS66Q68eI2g5gcP3UTmKhH0moyz7wBpRKB%2BIFJe5Vt7rQX0PZjs1EOCReghMqEP8xjvirnUs03a%2FGOFojOD8fFa731XI2Zi%2FMzoEPh%2BMdJuTsVRSQZ7cMKG4%2F9IGOqUBTmTtFItK49%2BI6JiGUQ%2BwuKi3%2BCHylox7wQw1ghu%2FDNTbkQZpNvtUDtllfuQFsTOaT8neci0K0CRRqJ7LTePIHppFnvDiNf1tmX%2BZln7PLlBKJ4zSzZZtptLrwAZh2p06ljcjD9zoeB%2FJuz%2FIozfyzXiJkfpv6%2BR7VLX5Uoh4LZPu2bvn4lxf0JD9iGvyimw367p4nVqQSA7XJfAsASuFaDVcBd6k&X-Amz-Signature=9f967223e98aeda69c10f42ca0a7b1a9b0a5f89303b0b4fa9799ef93f6c3c77a&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

hello 我们过往的各位同学们，大家好，我们跟进超快猛的项目节奏，接下来开始创建用户中心的下一个毛九，也就是 user service 那咱这里新建一个子毛九，它的名称叫做 foodie gun user gun service 好， next 文件夹依然是把它放在 domain user 下面。 321 出来。好，这个炮，我们选择借鉴商品中心的 service 层，把它 copy 过来，那改改就可以了。好，我们这里 copy 了商品 service 层，然后把这部分的依赖项原封不动移到 user service 然后把它的 artifact 小动一番。这第一栏 artifact 把它改成 food user API 下面的 mapper 同样的改成是 user 的 mapperok 那接下来就轮到我们去创建 service 层了。


首先咱的独家冠名商 IMock 的路径打上，后面跟 user.service 再一个点 RN PL implementation 好，那接下来我们就要到福地那边去 copy copy 两个需要用到的 service 好我们到 foodie 的 service 层里面，我们找到这两个和 user 相关的实现类，一个是 address service 还有一个是 user service 我们把它 copy 一下回来粘贴好。接下来我们要去做生产线工作，更正路径名称。 OK 我们在这里看一下，首先 package 把它设置正确，然后 import 里面我们把这些不用到的 mapper 都给它删除掉。像这个第一个 mapper 是没有用到的。那下面这两个这个 post 也是没有用到删除掉。那剩下的我们把它前面加上 user 前缀，这个 service 也把它删掉。 OK 这里没有报错了。很好。很好。


那接下来我们把这个 service 给它删掉。替换成什么替换成 rest controllerok 其实更规范的做法是什么呢？更规范做法是把咱在 service 里面定义的这些 annotation request param request body 等等。把它们怎么样把它们给 copy 到 service 层的 parameter 这里，那这是相对比较规范的做法，所以同学们不要轻易的改这个属性的名称。


好，那接下来我们去改动另外一个类， user service implementation 这个类同样的 package 先把它更正过来，然后 import 当中有哪些没有用到的类啊？这个 stu mapper 删掉没有用到， stu 也没有用到，剩下的都用到了。


好的，那我们接下来就要改成 user 的路径。好，这一个也给删掉。 OK 那接下来依然要把这个 service 替换成谁 rest controller 好嘞，那这两个 service 都更正完了以后，我们这里创建另外一个 package 是 center 好，我们要把 center user service 从 foodie DEV 当中把它给拿出来，就是它了。好，我们到这里找到 center user service 把它 copy 一下切换回来。那对它我们要做同样的事情，把这个 import 当中错误的路径，给它修复掉好。
123。 Ok. 那这三个修复掉之后还有错误吗？没有错误了，把 service 给它替换成 rest controller 这一套操作怎么样？简直如行云流水，无丝毫障碍。同学们现在熟能生巧，自己把剩下的没有改造的微服务三下五除二，大家自己动动手就当成作业了。


那 service 完了之后，接下来我们创建最后一个毛九也是最麻烦的，它的名称叫 foodie user 杠 web 其实话说回来，我们这个 service 层和 web 层实际上本质都是接口这个两个词可以二合一。只不过我们为了兼容以前的项目结构，不对它造成太大的结构上的改变。所以我们这里依然保留了一个 web 层和一个 service 层。不过同学们如果有时间，可以追求一下完美，追求极致，把这两个二合一。


好，那接下来我们把它的路径写上是 domain 杠 user okfinish 好，这里又多出了一个毛九，那它的 palm 里面我们要添加什么内容呢？太好办了。我们到上面找商品中心去抄作业，把商品中心的外部项目打开，把它的胖从头抄到尾，好， copy 一下，全部给他拿过来，拿过来还不能直接用。你这抄作业不能把别人名字也给抄上去，对不对？那把别人名字给他去掉。那上面这几个地方把名字给改一下，改成 user service 把这个 item 全给替换成 userok 好，看上去都已经 OK 了。那接下来我们去创建一个启动类，这里打开 Java 文件夹，把冠名商 com.imock 敲进去，然后后面再跟上 user 好，就在这，那咱这个启动类依然可以上去，把 item web 当中的这个 item application 给它 copy 过来。 copy 完之前我们先要给它改一个名字，改成 user application 好， user application 这里我们要添加几个不同的路径，比如说，扫包路径，我们把它改成 com.imock.user.mapperok 那接下来我们把启动类当中的类名替换掉。


好到这里，咱的启动类创建好了。那我们先把这个创建好的启动类添加到 pom 文件当中，以防忘记。这个 pom 里的 main class 我们添加上 com.imock 然后点 user user 里的 user application 这个类。 OK 了，却一桩心愿。
咱的启动类创建好了之后，接下来我们要创建几个子 package 第一个 package 是resources。 Resource. 同学们没看错，这个就是 resource 那它里面放谁呢？我们到 foodie DEV 当中，好，到 foodie DEV 里的 result 下面，你看这里放了一个 file upload 我们把这个类 copy 一下拿回来。
好，这个文件夹完事了，接下来咱来做第二个文件夹。那第二个文件夹是 exception 那看到文件夹名称，大家就知道我要去 OD DEV 当中拿谁了。拿这个 exception 下面的专门为文件大小设置的 error handler 好，把它拿过来。拿过来以后这个路径返回类的路径，我们这里给它重新引入一下。


OK 好，这两家伙完事了以后，最后就轮到咱的谁 controller 登场了。在这个 controller 里数量还真的不少，我们到附地 DEV 当中，把这几个 controller 给揪出来。好，这里在 controller 层，我们先拿到 address controller 还有谁还有下面的 passport controller 这两个家伙给它 copy 回来。 OK 这里面同样的也有一些代码要改动的这些路径，我们都要把它重新添加上 user 很简单，这个是改成泡酒。 OK 这一个完事了。


好，先生请起下一位到这个 passport controller 了路径这里依然是把 user 给他交代上去，剩下这里还有很多标红的，我们把这个 result 类导入进来之后，然后往下走，发现这里什么这里有个 shop card BO 那这个 shop card BO shopping card 实际上是怎么样？是购物车的内容。


所以理论上这个 synchronize 购物车数据应该放在哪里呢？我这里建议放到购物车模块当中，放到购物车模块。也就是说这一个服务同步购物车应该是购物车模块中的一个接口。那咱在 user 服务里，通过调用购物车的接口来实现对购物车数据的恢复。 OK 那咱这里就暂时用简单的方式把它处理掉了，我们怎么处理呢？理想和现实再妥协一次。我们把这个类从 food dive 当中给它揪出来，然后怎么样呢？ copy 一下 copy 一下，把它放回到哪里呢？找到希尔的泡酒这个类里面，我们把它就直接丢到这里。
好吧，老师这个有点老油条是不是，同学们可不要当老油条回国老油条我们要追求极致，同学们有时间的话就尝试怎么样呢？尝试自己构建购物车模块，同时把咱用户模块当中的这个服务抽到购物车模块里面，做成一个接口提供出来。 OK 那我这里就采用懒省事的方法了，把这个 BO 给它放到了希尔的泡酒里面，我们重新导入一下一个问题，就这么轻易的解决了。


实际上同学们在真正的企业级项目中，经常会看到这种理想和现实之间的妥协。有些情况当然是为了图省事。不过大部分情况还是因为某些服务之间的边界确实不好划分。所以有时候我们经常会看到一些冗余的类，在不同的项目中出现很多次。好，那咱这一个服务也给它摆平了。


接下来在 controller 里怎么样创建一个 package 这个 package 叫 center 好，我们去继续拉撞钉。到 foodie dive 当中，我们找到 controller controller 层的 center 我们把它打开。这里面有两个controller ，都跟用户中心相关，分别是第一个 center controller 和第二个 center user controller 我们把它都复制一下，再回到后迪代夫当中，把这两家伙花姑娘给他 copy 过来，好生产流水线开始作业，我们要把这些路径给他 fix 一个两个三个好，手起刀落全部搞定，不爆红了。
那有请下一位感觉做这个活跟搓澡的师傅一样，一个故在接客，我们把 import 打开，这里几个路径把它都给改过来。还有这里好久。 OK 好勒，看起来已经没有任何问题了。我们接下来最后一步是什么呢？创建配置文件对不对？我们这个配置文件非常省事儿，只要从哪里呢？只要从前面的 item web 当中，把这一股脑的给它 copy 过来，好，放到 resources 下面走，你那光放过去还不行，所以抄作业要把别人的名字抹掉怎么抹？我们往下看，往下看。


首先这里 spring application 的名称，咱要把它改成 user service 对不对？那接下来我们，再往下看走，你走你走停到这里。 my baddest 扫包路径，我们这里要把它改成 user.portal 好，再往下这里已经没了。 OK 我们转战到 application 杠 DEV 在这里面有哪些要改的呢？那是这里把它的 port 改成10002。 OK 那我这里把单机实例我改成我本地的地址了，local host 同学们如果是跑的虚机之类的，要把这里改成自己的地址。


好，那我接下来还要去 copy 两个不同的文件是什么呢？在 resources 下面，还记得之前在 fully DEV 当中，咱还看过几个和文件上传有关的对不对？在哪在这两个对不对？ file upload 和 file upload product 好，把这两个给它拷贝过来，也放到 resources 下面。


那这里我要提醒大家一个地方是什么，这个端口改了改端口，因为咱是微服务，目前每个微服务都是不同的端口，咱还没有引入网关层统一端口。所以这里同学们注意把端口改成自己的就可以。 OK 那咱现在所有都已经准备妥当了，对不对好万事俱备。接下来我们去把项目启动起来，是骡子是马遛它一圈。那在启动之前，同学们要记住开两件东西，一个是注册中心老师在外面命令行已经把注册中心启动起来了。那第二个组件就是 Redis 我在命令行也同样 Redis 给大家启动起来。那最后一步我们走到 user application 这里，瞄准闷方法干它一炮走。你好，稍等半炷香的时间，看到控制台在刷 log 那就说明你的应用是完好的。就像我们坐绿皮火车一样，就喜欢看到火车在开一停，就感觉好像要晚点了一样。很多 90 后同学们可能没坐过绿皮火车。


好，看到这个应用已经启动起来了，我们切换到 postman 好 postman 这里我已经预先设置好了几个方法，想先去调用一下项目最外层的 web 模块当中的 controller 比如说我拿一个这个地址模块 address list 传入一个 user ID 我们来一次有点慢返回，那再来一次。好，这后面就稍微快了一些。
其实核心链路我们在核心主链路中的接口返回时间要求一般，我们希望它在 100 毫秒以内，最多你的超时时间控制在 1000 毫秒，这是对核心主链路的要求如果你超过 1000 毫秒，这个其实已经很容易引发一些线上的问题了，那我们都会有很多监控来确保主链路的这个响应时间，也就是 rt response time 好，那在这个接口试验成功了，我们接下来去测试几个新进的 production 接口什么叫新进？就是之前是 service 层，我们经过改造之后把它改造成的 controller 好，我们这里看一下 center 接口。
好了，center user API 我通过一个 user ID 获取他的账户信息 profile 好，我们点击 send 你看也可以顺利返回了。那再换一个 hs 依然是顺利返回。 OK 那现在我们就可以宣告用户中心已经基本完工了，为什么叫？基本怎么像商品中心一样又没有完全完工吗？没错，因为这里有一个小作业留给大家。是什么内容呢？那就是刚才老师在 passport controller 里懒省事儿，留的一个小尾巴就是这一步。


synchronize shopping card data 我们要把购物车的业务逻辑从用户中心给它剥离出去，放到购物车的微服务模块当中。 OK 同学们相信经过这一节，大家对微服务改造已经是熟能生巧了。实际上就像老师说的，微服务真的是一个非常简单的东西， spring cloud 已经帮我们摆平了 90% 微服当中需要碰到的问题，剩下的 10% 就靠同学们各自发挥了。 OK 同学们这一节我们就讲到这里了，我们下一小节再见。


