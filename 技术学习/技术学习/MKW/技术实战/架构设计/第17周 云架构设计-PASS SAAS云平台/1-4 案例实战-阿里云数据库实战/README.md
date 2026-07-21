---
title: 1-4 案例实战-阿里云数据库实战
---

# 1-4 案例实战-阿里云数据库实战

[image](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/b037e0f4-fce3-456a-88ba-4c8c67cca570/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VQJPV5PL%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T231114Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIGQ2SL0IvQPgcHJSEY2aMmYlSZmFti6lvz%2BcasxJ4yDAAiB5kH1%2BzknMN%2BAqWzLZT4jMmXrOSgdBfe3AH9W2sL1ZviqIBAjG%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMKMGV4md%2FgACOEO9gKtwD3m8ylrGUGdiZ6lQIRGgJsjJoEDpS%2FQd%2BprkbPZK0WIvqjE1g%2Bz0bTctvEDcWsBE4sbYgbGzcpS17ZZIkzzGu5irugtKlJFZJ48QhDhWaa7X9WR5A2HMYJwNcaPkon800BDKBLRtZ3ztAUmOVQRlB8MFCDYSxc4YiBl8pqSiCFfPCDWWa%2B3R3iOew6cdiamfvjzMqOVWo5XJnALsFsHHHodQo9XZr5KtFRsU6QBLlaDS%2F%2F%2BxGYlKQGh9wiao8X4WDbnNkYYuKgcHnTbAJOTm2Ze2t0tXDYKdRDA%2Bfn8MUzcdIRMcnQGVOPwlQ6jarlw2daShba3I4tdbOdTiixsJGtB3Q45J%2BCZstM5q6HiVElSNITPLcAexNGjR67QzZvbDL5%2BPMnPPXyNUJzBhLKJL8%2FDUKKP8hisSwa7OQzBdmlasFroqYRRZr2hsp7Sf42BXMuthNwxfVRi9WMPT81gDYeejKVICghkHssty7nQcuyR1er8%2FD91wnHHawSeQ5%2BeTsAYlZ2uvqyzr9zrBk77R6%2Bi%2FRKqnDEM%2F4TT8Thl2M5OkFRni2E6Mx4N2pyjuZtLcfEigRIn7ms8%2BA6zl1fQ5smRGP9JjZRHuBeloBYepz2s3ECrQbHYXvqK2lbMMwlbj%2F0gY6pgGecaddQAWOYOhWy9wi3ygsho0wEHkKisrza8J6tmaqZzBFS4SQC67Ar5co%2B8FmZgjFvt%2BvGsYMU4k8j5dkCK%2B6XKn1RPMMaJXEOEuHEP9pawWg6r23Mi0hoeCds2gC6wftAoU8x%2FJzBQ%2B9i6xhXbnyQla91sbrWWSytSCqq4D1cq6%2BWsqpKa8z%2BQbzuttk9%2B6pudNm71btqtuvKYWWhb3CBl9jQt8m&X-Amz-Signature=0c8a6aa4fd66de0d74cf30d71f681111d0913ac366f0fc8977f10ec87381a4f2&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

价值需求到落地的桥梁，构建 IT 新蓝图。我是张飞扬。上一节我们聊了聊RDS，聊了聊 OceanBase，以及其他的不同的类型的 NOSQL，不同的云平台的解决方案。我们就来实战一下吧。首先看一看 OceanBase，我们是在控制台输入ocean，看到 OceanBase，当然了我们也可以什么在旁边的红蓝色按钮点产品，我们可以找到有一个叫数据库。这一点大块里面重点就能看到最凸显的 OceanBase 了。点进去看一下 OceanBase 默认是什么，是没有创建集群的，所以它会什么？提供一个老版的接口和一个新版。如果大家要玩 OceanBase，当然用新版本。点击这里立刻创建。


OceanBase 是一个很贵的服，因为它是这种高性能的并发式的SQL，或者叫 NOSQL。它包年包月。你可以看到什么？这是 1 万多块，太贵了。我们可以看看按量，如果你按量付费，即使是选一个，比如北京或上海，选单机房部署，可以看到什么价格也要在什么几十块钱每小时，相对成本是非常高的。而且几乎没法进行什么进一步的降价了。因为什么至少也要 14 盒，七十几，最低配就是这个价格。如果大家真的想玩，就可以点立即购买，一路点下去。


最后通过一些这种 OceanBased SDK 跟我们应用对接起来，感受一下它强大的并发性。当然，体现强大并发性，光是思和有点不够，可你要买六十几盒，哈哈，有点贵，我这里就不做演示了。大家只要知道对吧，在云平台上这种什么 NOSQL 是可以很容易的。什么按量使用，按量购买对应的SDK，用起来就能够很方便的让应用来访问这些非关系或者是 NOSQL 的数据库。我们下面重点是来展示一下SQL。我们关掉这个页面，点击左边阿里 s 是吧，是整个阿里云系统里面最著名的数据库，所以很容易在什么我们常见的服务列表里找到。然后点击 RDS 就可以进入 RDS 的控制台。 r d 的控制台。如果你要创建一个新的集群对吧，就可以。什么点击这里创建实例，或者在实际列表里面点击什么点击创建都可以，因为我这里已经什么提前创建了一台实例，这台实例是为了待会给大家演示怎么样进行进一步的管理。因为整个实例创建过程大概在 10 分钟左右，稍微有点长。我们看一看在实例创建之前需要进行怎么样的配置。点击这里创建实例也有好几种模式对吧。


包年包月是很贵的，我们看一下，就算是优惠，它的价格也是会很贵，它要算一回还在询价也是 1 万多是吧，是不是好贵。专属其实也非常贵对吧，你要买专属的集群系统，通常高配也会非常贵。飞扬老师自然的推荐我们小伙伴们就跟飞扬老师一起按量付费，大量付费。选择什么就近原则，你城市旁边是哪一个什么城市？或者是一线城市，你就选所在区。这里选了。滑动 2 有好几种具体类型可以选择。通常我们会什么？根据大家的习惯。比如我们之前是熟悉MySQL，就选MySQL，如果是 donate 系列，很多时候用的是 c q server、 Merry DB。 MySQL 的变种 Postgresql 是另外一个我们的 SQL 的引擎。 p Paas 是什么？是阿里云最推荐的，既能兼容Oracle，也能兼容MySQL，同时性能各方面优化相对都比较好。所以很多时候纯阿里云用户就用。但如果你是一个三心两意的用户，今天想用阿里云，明天想用腾讯云，后天想用百度云，我建议就用MySQL，不要花那么多时间来折腾。 MySQL 底下也有好几个不同的版本，比如高可用版，它就列出来，其实就是什么主备节点版， polo DB 版，就是另外一种什么云原生，支持一组多背的这些形式。


三、节点版其实就是什么前面说的跨多个不同的机房的什么集群版本，我最当然推荐什么。我们在 demo 里面就选基础版最便宜。磁盘其实价格差不了太多。磁盘也有好几个选择，什么 poloDB, SSD、 ESSD。相对来说 ESSD 性能很不错，同时也不会，所以选这个就可以了。


主节点所在区对吧？我们就一个节点，所以就选所在区。比如华东的什么2，我们看有没有滑动 2 可用，去 f 就可以了。选上对应的 CPU 内存，日标性入门级就选小量CPU，少量内存。比如像这种是吧？更便宜点。选个什么一颗 CPU 1GB，你看一小时只要 9 分钱，是不是很便宜。好，我们再往下滚，看看还有什么磁盘，磁盘这里越大就越贵，我们自己玩玩起个20GB，基本上就可以供你玩了。


价格算好了，我们点一个下一步，最后他这里会把所有信息都给你确认出来，你点开下一步确认订单就好了。在整个过程当中，可以仔细看一下是不是高可用，配的很差。没有关系，因为我们什么只是去做一个小小的demo，只要同意条款，最后去付钱。它是一个什么后付费的形式，你用一个小时，它就会扣你一个小时的钱，但是就算你用一分钟，它也会扣你一个小时。


回到控制台，我们可以看到什么？我们刚刚配置RDS，已经在创建过程中了。到左边选择什么实例列表。我因为是 150 的分辨率，所以看上去好像阿里云的界面，有点丑。如果是 100 的分辨率，整个界面比较漂亮一些。我们可以看到什么？刚刚我们点击的什么按量付费的，已经在创建中了。有一条创建中，但是要等个 5- 10 分钟，稍微有点长，所以我们不等它了。


我们用飞扬老师提前创好了一台干干净净的什么？ MySQL 数据库，这在数据库要访问它，就点击蓝色按键，点进去以后就有了。数据库的基本功能。什么功能？可以做一些监控报警，看看它的整体性能情况。 CPU 利用率你看很低，因为没有用起来。也可以看看它的数据库连接。我要连数据库，别人要知道他是怎么样去连的，他有好几种连法，他告诉你了是吧。因为我们是单库，所以其实你只要什么e、c、 s 找到对应的 URL 就可以去连它了。如果你是高可用模式，还有主库备库这样的一些切换的原理。


我们这里你看内网连接没有打开，原因是什么？因为没有设置白名单。和我们前面说到的安全的什么 security group，服务器的 security group 类似的。我们在什么RDS 上是也要设置白名单的。当你不设的情况下，任何资源，任何机器，任何容器，任何服务器都不能访问这台数据库，同时这台数据库其实也可以打开公网模式，这样让我们让公网，让外网也可以进行访问，你就可以申请一个外网IP。但是辅导员老师强烈不建议我们数据库用来什么内部服务器访问，而不是让外部黑客来访问。所以千万不要申请外网IP，不要打开外网访问我们一定要走内网。


好，我们先来设置一个白名单。白名单这里其实很简单，就是什么设置哪台机器能访问它，默认只有它自己能访问。我们要添加一个白名单组，取个组名叫什么。我们找一台 console 能访问他，填入他的 ip 地址，或者是什么子网，可以是个子网，可是个 ip 地址。我提前启动了一台小机器，我们看一下 ECS 里面。我们打开一个 ECS 的界面，看一下我们提前在什么。在内网里面启动了一台实例，这个实例是之前菲亚老师在直播课程里面给大家演示 Docker 的时候用的这台实例。内网地址是什么？是我们就把内网地址贴过来，在这里加入白名单，让这台机器能够访问什么 MySQL 服务。


点击确认有点慢，他说什么 1 分钟以后生效，但是照理应该这个键应该点下去，立马生效。可能是名称不太符合要求，我们看一下有没有名称符合要求的写法。不能用大写，我们换成小写。好吧，我们点击确认已经完成了，已经出现了，叫console，他的 ip 地址已经写进去了。完成了什么白名单以后，也就是网络部分完成了。但是你登录光有网络还不行，还有账号对不对？我们这里空空如也。什么没有账号进行过设置，也意味着我们其实是没法正常登录的。所以我这里可以创建一个比如叫 Imoock 的账号密码。我这里随便输入一个。好输入一个密码，重复再来一遍，保持两个密码一致吧。这是一个高级账号，所以它可以访问各种各样内部的表。点击创建。这套用户名密码也创建出来了。现在我们有了，用户名密码也有了，什么也有了。打开的白名单，允许外部的服务器能访问它。这个时候我们重新回到数据库连接，把是吧新的内网地址给看一下，复制下来，我们复制下地址端口，就是标准的 3306 端口。复制完了以后，我们就去云 ECS 控制台，打开那台 ECS 远程连接，点击登录。优惠密码，我这里提前已经输好了。登录完成了以后，我们就可以采用 MySQL 的命令 host 加上这个地址。然后 user 就是刚刚说的 eye MOOC password，输入一下，人工输入一下刚刚设置的password，诶，是不是已经进去了。


我们可以 show data bases 看一看默认写多少数据库，是不是标准的回收数据库。 MySQL 自身数据库性能schema， information schema 和 seize schema 都建出来了，很好。也就是我们的 MySQL 本身的创建很成功，同时我们的网络确实打开了。另外用户名密码的设置完全正确。这就是什么 RDS，一个标准的 MySQL 数据库。


大家回过去看一下整个 RDS 的创建过程是不是非常简单，所见即所得，点几个键，如果你是熟悉命令行，你只要拍几条命令就可以完成它的 RDS 创建。在创建完的 RDS 里面，重点去设置它们，它的账号信息，它的数据库的连接信息，哪些的安全组能够正常的进行访问就可以了。


除此，其实我们还有很多高级功能，比如备份和恢复，比如快照，比如容灾。这些可以留给大家在我们的课后进行小小的实战。因为 RDS 成本很低对吧，只要几块钱就能够玩几小时，大家完全可以慢慢的安心的进行实战。感受一下RDS 的方便。一个小小的 MySQL 很方便， OceanBase 很强大，所以阿里云平台很多的数据库组件都能带给大家一种什么比较舒服的、快速上手的感觉。聊完了数据库章节，我们下一集内容会非常丰富，各种五花八门的中间件，不管是阿里云独有的还是什么，很多云平台都提供的，我们逐一来跟大家分析交流，大家敬请期待。

