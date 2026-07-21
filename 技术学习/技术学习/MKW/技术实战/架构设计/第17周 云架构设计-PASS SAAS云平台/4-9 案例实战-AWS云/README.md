---
title: 4-9 案例实战-AWS云
---

# 4-9 案例实战-AWS云

[image](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/16d9b499-1880-4fa2-b4a2-65fe7c9be86e/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RUT5OTAH%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T231134Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDPxnMuJtp5CN3uNdy4mZgM5UJdaZul2rt1XE6AYHtDjwIgQZTg%2BEqBNE8zNymJFCR1jGkYI6JG%2FN%2BLU0zt9qci5wsqiAQIxv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDO1ndPTYm6Gm%2FCzX1CrcAyi0e6M3QTDfP77QQfcARuo3h4KGM%2F86zjQZKEH58p1TTN1ql31LWetSKOJG443ORx65YcG6mCuWWPPt9At%2FH3H5UJ4VbvJeW3%2BmiRyx1HQXQg0jq4FhqSQxYsq7dfMPeSHJewRYZHdZ7LNuUdpB3BSfTnWcmSUZ57w4hla%2B2s3QTYiF%2BgtVXrFUZoQEHj6kqB1b9VQyeJqVwuozSmw268u%2BT5NfxXCd4B7NMdStsdK5zPedJswn0StV4PTuBOGUkSezQsORUccEU6NnEIipebL%2B%2BxoaMXHXWUtq%2BGYgGHtaENRkLl1L7PZxEu9Tqb562Fj0Aj5d8lEBoBl7U0N1QsDFZcnQmklzuGD2gHjBGrBhIlsPysgOHRfVGW9aZv5HH4MSqV9bGoV2wT0No9ShOr2zCgrf91hrWkQsRvPYG5D37sy69iRGWkVhYwjj7oWTXSq9m659G3yonupgZwF%2ByDt11bmLyNSiXpdi9PxK1GJoPxwqB26RCpCxtU0DH%2BePnJCMQrutlYjiGMtRNgUKuUccsigZL5AKTVkmqgjvonPDlB64xboDm7a%2FpzP8WmxhIyF7FfFR7800idCZO%2BQ0okyw40mUC5Y%2FxqPw9tqA7E5Z2lhMaYRpDHHCKgxlMNW5%2F9IGOqUBQYvD%2FubVIJc74z4HfdwCEQiAfTo%2FG%2FqOT092TmiHpQ3bU4QDPnM5cmfQeQnaf8BLq01rKyTJ8AGMCyzOujNksaAc4VpH0MtvTFIjnJSKuszpHCw7gMZyUE8vzt2LbyNt%2F8cJnaBwq3dD9lB5O7olKPah1VXv9K%2BZiosrhK3W5%2Fm0R7zcwL6pRB%2BLOwB4kjWhQo5eLFzJE9Guy%2Fm%2BDMn9LE2xb8mB&X-Amz-Signature=b9a7a1d1957b399106c1826cd1e71cb4ce46e79b9f70bfd97778d983b397a51f&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

架起需求到落地的桥梁，构建 IT 新蓝图。我是张飞扬好，上一章节我们聊了聊AWS，作为全球第一大云平台运营商，它的优点和它的几个独有的服务。这章节我们就在它的全球站点 a w s 点 Amazon . com 这样一个全球站点，

[image](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/4b2c82a0-c565-47c0-a0f4-84094ccf0f3d/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RUT5OTAH%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T231134Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDPxnMuJtp5CN3uNdy4mZgM5UJdaZul2rt1XE6AYHtDjwIgQZTg%2BEqBNE8zNymJFCR1jGkYI6JG%2FN%2BLU0zt9qci5wsqiAQIxv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDO1ndPTYm6Gm%2FCzX1CrcAyi0e6M3QTDfP77QQfcARuo3h4KGM%2F86zjQZKEH58p1TTN1ql31LWetSKOJG443ORx65YcG6mCuWWPPt9At%2FH3H5UJ4VbvJeW3%2BmiRyx1HQXQg0jq4FhqSQxYsq7dfMPeSHJewRYZHdZ7LNuUdpB3BSfTnWcmSUZ57w4hla%2B2s3QTYiF%2BgtVXrFUZoQEHj6kqB1b9VQyeJqVwuozSmw268u%2BT5NfxXCd4B7NMdStsdK5zPedJswn0StV4PTuBOGUkSezQsORUccEU6NnEIipebL%2B%2BxoaMXHXWUtq%2BGYgGHtaENRkLl1L7PZxEu9Tqb562Fj0Aj5d8lEBoBl7U0N1QsDFZcnQmklzuGD2gHjBGrBhIlsPysgOHRfVGW9aZv5HH4MSqV9bGoV2wT0No9ShOr2zCgrf91hrWkQsRvPYG5D37sy69iRGWkVhYwjj7oWTXSq9m659G3yonupgZwF%2ByDt11bmLyNSiXpdi9PxK1GJoPxwqB26RCpCxtU0DH%2BePnJCMQrutlYjiGMtRNgUKuUccsigZL5AKTVkmqgjvonPDlB64xboDm7a%2FpzP8WmxhIyF7FfFR7800idCZO%2BQ0okyw40mUC5Y%2FxqPw9tqA7E5Z2lhMaYRpDHHCKgxlMNW5%2F9IGOqUBQYvD%2FubVIJc74z4HfdwCEQiAfTo%2FG%2FqOT092TmiHpQ3bU4QDPnM5cmfQeQnaf8BLq01rKyTJ8AGMCyzOujNksaAc4VpH0MtvTFIjnJSKuszpHCw7gMZyUE8vzt2LbyNt%2F8cJnaBwq3dD9lB5O7olKPah1VXv9K%2BZiosrhK3W5%2Fm0R7zcwL6pRB%2BLOwB4kjWhQo5eLFzJE9Guy%2Fm%2BDMn9LE2xb8mB&X-Amz-Signature=a374086834c697cf97df5052901fdb2b5bda1ae9713552e9a7a0f2b925333e77&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

来实战一下它的那些酷炫的功能。这里首先要提示一下，在注册的时候，它会提示你是要选择中国站点还是全球站点。通常你是企事业单位，在国内要实现云平台，他会选中国站点。但是中国站点是需要有什么？需要有我们的法人证书以及法人代表相关的资质背书的。所以如果你是个人做尝试，进行实验，建议就跟上一节说的一样，是选 . com 的全球站点。


在全球站点注册过程当中，它要求你们输入一张万事达卡或者是 visa 卡，或者是 AE 的卡，也就是全球的认可的支付的 PCI 卡。除此以外，还要有一个全球收货地址，也就是海外地址。这个时候大家随便去 booking . com 或其他的网站找一个全球的地址，包括它的邮编号，在这里进行输入就可以了。我这里输入一个美国湾区加州的地址，输了一张我自己有的 one star 卡之后，就可以成功地注册了。
注册完了以后，大部分情况下你都可以享用它什么免费资源来实现，包括计算数据库存储，甚至于是我们说到的什么 London 这种完全是 serverless 的服务。好，我们就来看一看前面说到过的几个关键服务该如何使用。这里我已经采用我新注册的账号登录了。登录完了以后，我们可以在左边 service 里面可以看到好多不同的服务。


英文它是什么？它是欧美主站，所以它的中文翻译可能没有到位，所以有些是中文，有些是英文。大家将着来看。我们重点关注一个数据库对不对？数据库里面我们说什么？ dinodb 是一个很强大的分布式的 no sickle。除此以外，我们要聊一聊RDS，这才是它最酷炫的一个能力。我看点击 RDS 以后，稍微等待整个过程是什么？因为我们去跟海外网站进行交互，所以略有延时。稍微等待一下。


好， RDS 这里已经打开了。它提示什么？我很推荐你 RDS 用什么引擎？ Aurora 引擎也是什么？也是 Amazon 主推的一个引擎。但是我们要强调什么？我们其实它的优势在哪里？优势在于有很好的MySQL， Postgresql 的支持，以及强大的 OREA 的引擎。还有独有的点就是对 Oracle 的支持。所以我们来尝试创建数据库的时候选择 Oracle 好。


这里有好几种创建方法，通常我们是什么标准创建，往下看 oral MySQL，Meridb，Postcode， SQL server 这都不稀奇，最稀奇就是它对 Oracle 有原生支持。但是这里要注意 Oracle 安装的时候是需要有什么有 license 的，它这里提示叫什么？叫 b y o bring your own license。也就是你要在企业内部或者你个人要有一套 Oracle 的什么企业版的license，这个时候你可以选择跟 license 对应的版本，比如是 Oracle 11 或者是 Oracle 12，或者甚至于是 Oracle 19。


你要找到跟你 license 对应的版本进行安装，在安装完了以后，把你的企业版 license 或者是什么标准版 license 给什么加载到 Oracle 上面，这样你才能享受到它的集群或者是单点的这种强大的运算和处理能力。下面具体内容我们可以选生产，也可以选开发。测试之后选择数据库的名称，它连接的用户名，密码以及数据库的实例。因为是Oracle，所以它实力都是很大的。你看至少是 2 c 8G 是高带宽的，甚至于起步可以达到 64 C200 多 g 这样的配置，它的价格也是非常惊人的。如果你选完了网络，选完了其他内容以后，这么贵，上手就是几千个刀了，几万块钱诶。当你要真正要在生产系统上去搭建的时候，尤其是全球搭建的时候，你会选择海外的 AWS 的Oracle。如果你在国内市场，你也许可以选择国内点 CN 的什么。亚马逊的 Oracle 服务，很方便地进行 Oracle 数据的转移。但是我们 demo 因为什么资金有限，我们要尝试使用到它。什么？它的免费功能？免费功能它提供了哪几个平台？ MySQL 引擎，还有什么 Merity 的引擎和 postgres SQL 引擎才提供了免费功能。所以我们来将就一下。跟着敷衍老师进入省钱模式，选择 MySQL 8，来一个免费套餐版本，最省钱的版本。免费套餐版本意味着什么？意味着我们这里只能选 1C1G 内存的。测试版。好，测试版也有，好过没有。


网络选默认的VPC，每个用户天生就自带一个 VPC 的。选默认值，不对外公开，只在子网内部进行沟通，其他都应该保持不变就可以了。它是个免费的，可以用个一年左右。空间比较小，我们也使用很小的空间。它默认很小的空间。这里不用选那么多，我们选了这里 21G 或者最小值21G。我就选个 21G 好不好。我们再看看。这是空间默认分配是20G，最大就21G，省点钱。


磁盘就选s，s，d。好，我们就创建密码没选好，我们确认一下密码，好好了。创建。整个过程稍微等一回，它界面上是首先返回给你了。其实后台还在创建中。这里的 MySQL 包含Oracle，其实说白了还是什么。跟其他的语音平台一样的，也是在 v p、 c 里面起了一个虚拟机，这个虚拟机后面挂一个磁盘，而是快设备磁盘。同时它把虚拟机上面配置了什么，默认的一个镜像，这个镜像就是我们刚刚学的 MySQL 的镜像。如果你选Oracle，说白了它就是装了 Oracle 的镜像。而 Oracle 有很强的依赖条件，它要求 Linux 特殊的版本，它的底下的什么， CPU 内存的整个虚拟化也是属于特殊的版本。所以 AWS 是能够什么进行 Oracle 的验证？也完成了 Oracle 的官方验证，它能提供合适的版本，同时能通过 Oracle 验证实现什么。有 Oracle support 的情况下的部署。其他平台，你也许也能装出一套Oracle。当你装完以后，你打电话给 Ora 考试，让他支撑我出了一个bug，怎么进行调试。他会告诉你，你所选用的物理机型号我们不支持，所以我们不能提供服务和保障。但是在 Amazon 里面，在 atables 里面，如果你选Oracle，你能拿到 Oracle 的支持，也能得到亚马逊的什么强大的o，e， m 或者是叫甚至于是 Oracle s 的支持。所以很好的能支撑你的整个的云平台的数据库。


好，我们数据库具体就不用去登录调试或者跑线命令了，相信大家可以在自己的实战环境很方便的找一台物理机去连接数据库，完成什么数据库的读取访问。在免费的资源的使用的情况底下，能够完成很多酷炫的操作。好，我们再看一看前面说到了什么。 Landa 令人非常吸引人的 lander 该如何部署？还是点击这里 service 在计算下面是不是有个叫Landa，我们点击它。稍等片刻，好， Landa 已经显示出来了，我们当前是没有 Landa 应用的，我们可以先点击这里。


函数 lander 的本质其实就是什么，一个的 function 翻成中文，有的翻成函数，有的翻成什么 service 应用是吧，无服务器应用等等。这里它就分成了函数，我们点击创建函数。创建函数过程当中有很多种创建方法，我这里偷懒选一个，用模板来创建。这里最右边浏览无服务器应用程序存储库，从中间挑一个应用程序。所谓应用程序什么，其实就是前面说到过的 cloud formation 全自动化应用部署的自动化套件。我们这里选择公共应用程序里面的hello， world 这样一个套件。好，我们点击这个套件，它会告诉你说做的就是 AWS 是经过他们发布和验证的源代码。在这里 GitHub 这里大家可以点进去看。


模板里面告诉我们你说什么，我需要传一个参数，这个参数是一个什么？ string 类型，它就代表着我整个的模板的基本的能力。同时它底下什么有个叫resources，这就是核心了。我们说 cloud formation 里面所有的内容都是什么，定义成resources，把它的最终状态在这里面进行输入。实际的部署过程当中，我们后台的不管是 AWS 还是其他的平台，都会按照你定义的resources，把你的最终目标的状态给建出来。


我这里希望什么？创建一个函数叫 hello world，它是属于什么？属于 service 的一个function，也就是属于lander。同时它什么支撑的 wrong time 是 node JS 也在上面，很方便的跑 note g s 很可惜不是个 spring boot 的应用。不过相信大家能玩后台的，对前端都有一定了解， note JS 代码是也能很方便地进行读懂的。所以我们就用 Nodejs 来进行一个展示。除此以外，它什么？它所有的代码是会放在一个 bucket 里面的。这是一个默认的bucket。好，它的大小、尺寸以及一些策略全部在这里定义。好了，这就是它的模板。基于模板， cloud formation 就会去创建对应的资源。这次创建的资源不是一个普通的服务器，而是一个 lander 的service。名称叫什么？叫 hello vote。好，下面的权限许可证都是很普通的内容，我们用的是 MIT 许可证。好，这里说好了，要传一个参数。我们随便选一个，叫Imock。


点击部署。整个部署过程其实是什么？是它后台直接调用了 cloud formation 的API，就把刚刚我们传进去的这段什么 YAML 或者是 JSON 文件的，这里是个 YAML 文件，把这段内容已经传给了整个 AWS 的，后面的 cloud formation 的 server 通过它来进行快速的部署。我们等待一会，所谓快速可能也要 1 到 2 分钟左右的时间。在这个时间段之内，我们再聊一聊我们的整体思路是什么。
Colorformation 是作为基础架构的自动化解决方案，也就是我们什么是所有资源都可以用Callformation，包含普通计算资源，存储资源，以及刚刚我们创建的什么 RDS 数据库。还有就像这里的lander，甚至于是消息队列中间件，以及很多的什么 AI 的功能的套件，也都可以用 cloud formation 进行创建。好，我们这里不做太多等待，差不多了，它已经创建出来了。创建过程当中具体蓝的该怎么样去运行，我们可以点到蓝的里面来进行查看。期间是什么。它是把一个 row 重叠出来了。每一个服务都需要有个 i a m row。 i m row i 就是identity， a 就是什么 authentication 或者叫access， m 就是 module 或者是什么一些功能，也就是用户的认证登录功能。这里 land function 出来了，而下面画的 row 叫 i m row。


好，我们就点击 Landa function 去看一下。 Colorformation 创建出了 lander function，到底该怎么样玩它。这也是个概述。我的整个 lander 的全网唯一 ID 就叫这样一串名称。下面具体的代码在哪里？在这里根据刚刚前面看到模板，它把这个模板 copy 进去以后，还包含了一个叫 index 点JS，也就是它的主的什么应用代码，它这个代码大家可以看到。


就打一串字，我开始loading，又打一串字，什么？我的 value 1 是多少？ value 2 是多少？ value 3 是多少？这些 value 在哪里来？通过一个event，就跟我们之前说的一样，我们的 API 可以打到 API 网关，会发生一个event。我这里就不跟 API 网关进行对接了，我直接常通过 test 这个方法来传输一个event，这个 event 里面就是个键值对吗？我只要把键。


为什么 T1 的内容传给他， K2 的内容传给他， K3 的内容传给他，它会逐一打印出来。最后它会把 K1 的内容给打印在什么。整个的个应用的返回callback，就是整个 function 返回 lander 的返回。好，我们来看一看我们该怎么样去传一些内容给他。返回一个内容。我希望返回的内容名称就叫飞扬。我们点击一个test，自己可以看到我们刚刚说的K1，K2， K3 的值。在这里我们这里尝试 K1 就叫飞扬。刚刚代码最终会返回飞扬。过程当中还可以打印一些其他的内容，比如张张飞扬。我们的当前的展示平台是Imock，我们就以这个为例创建。这要写一个名称，就叫test。第一次测试我们创建一下。我们已经创建好了event，但是并没有向什么 landed 的 function 进行发送event？我们点击 test 就发送了。看看它的运行好结果出来了。整个 lander 的返回飞扬。在过程当中，它会把每个 key 的对应的值打印出来，对应 key 的值就是飞扬，对应 key 2 的值叫张in， key 3 的值就是imock。这就是我们整个代码什么后台的日志以及最终的展现了。如果你需要改动，很简单。我们在什么？我们在index。这里面我们不希望打印fail，我们希望打印一个到底是哪一家企业在对我们提供整个视频的教学。


打印一个 key 3。这个 key 3 我们在传递过程当中再仔细看一下 key 3 对应的什么，不就是Imock？所以我们最后应该返回Imock，好稍微改一下代码，点个deploy，几秒钟时间就能够部署完成。你再测试一下，看什么样效果好运行了。看到了没有？所以最终出现了Imock，也就是所见即所得，快速部署，轻松测试。


这是测试实际过程当中，其实什么是有 a p i k t v 会向它发一个event，或者是对象存储，或者是一些什么 i o t 物联网的消息，中间件会向它发一个event，触发整个 land function，进行一个什么特殊的处理。这个时候日志可以打印出来，整个处理完了，以后的结果也可以返回出去。这就是 land 酷炫强大，轻松发布的一套能力。


大家是不是感觉以后我们不需要再搞什么connect，不需要再搞我们的物理机，不需要搞虚拟机，甚至于网络，我也不想管，我都想用 lander 来实现。不好意思，如果我们是长期运行的 web 网站，并不适合lander。哪些场景适合lander？物联网还有消息驱动的一些事件，还有一些通常是什么？是一些沟通过程当中的，比如像我们的手机推送， push notification 等等。这些场景也许更适合于采用无服务、无状态的这种lander。好，聊完了。我们的 lander 的酷炫的操作，大家是感觉是不是有点欠缺什么？ coral formation 的套路好像不是那么完整。我们在模板里面创建了 cloud formation，但是我们没有尝试修改，也没有尝试在 cloud formation 里尝试进行一些资源的删除，我们这里就尝试带着大家来感受一下 cloud formation 的酷炫。


我们回到函数这里，我们选中它，我们可以到这里，到 lander 这里点击应用程序。应用程序就是整个 coral formation 创建出来的所有内容。我们刷新一下是不是这就是我们的 cloud forbation 创建出的整个内容，里面包含了我们刚刚 land 函数。我们点击什么删除，看清楚了。他告诉你，删除应用程序没那么简单，你必须什么来到我们的 Colorformation 进行合理的配置才能删除好。我们点击它。还因为是连到外网的关系，所以稍微有点慢。我们就看到什么。他自己说 Colorformation 里面我们建了一个堆，称所谓堆栈，就是一个整套的什么资源组。堆栈是要创建一起创建，要回退一起回退一套标准资源组。这个资源组就叫 service Pro close world。


这里面有很多的具体的状态内容。如果你要做对这样的统一回滚，统一配置策略调整，可以在这里进行调整。改完以后它可以什么？在底层基础架构改变前面 function 的基本功能 function 里面，你可以去改代码，你可以在 cloud formation 里面去改变 function 的整体运作。甚至于我不希望通过 event 来触发，我希望读取一个bucket，一个对象存储的值来进行触发。一个事件返回值可能写到了什么， Dynamodb 里面等等。有不同的解决方案，都可以通过 cloud formation 进行资源的串联。我这里展现的是 cloud formation 的酷炫的删除功能。点击删除。我说确定一键就可以把整个 function 它的对事件的监控， function 内部的代码以及 function 的所有的功能全部进行删除了。我们刷新一下。我们回到对战。刷新一下。诶，是不是对战里已经没有 function 了？我们回到刚刚的 lander 里面，我们看看 lander 所在的应用程序和函数还在吗？好，应用程序下面是空的，我们前面创建的函数看一下是不是也空了。


很方便的通过 cloud formation 进行资源的创建、修改以及删除。如果你的整套资源里面包含了一堆物理机，一堆容器， lander 对象存储r，d， s 什么很复杂的那些什么 Dynamodb 的配置，这个时候仍然可以在刚刚的 cloud formation 里面一键删除。好，聊完了 AWS 的 London 以及 r d s，我们下一节就是面试环节和本章小节，大家敬请期待。

