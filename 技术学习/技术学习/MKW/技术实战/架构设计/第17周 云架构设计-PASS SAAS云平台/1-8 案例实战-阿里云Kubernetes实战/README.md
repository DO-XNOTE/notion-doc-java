---
title: 1-8 案例实战-阿里云Kubernetes实战
---

# 1-8 案例实战-阿里云Kubernetes实战

[image](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/7542fc6c-10e2-491a-b817-02149b0e5190/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664VADDAV5%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T231118Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIBupqCLlqfIc58FYQ112sT337PmKeQh3leSMqs7PrfgrAiBcE%2BdusLPjT5%2B0n%2FpGCZ6BCSVL4Yv9NtzfRKtMRh4rgSqIBAjG%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMTDCctu1%2FhDMCIXHjKtwDzMpQaCGgEyQwyHuPh17lsgBZ3wa0FuKLMcMqjKjDY4sFkCdUoumC%2FOcAcsvDBHn0vm9RVL8Z7PTs60z7srumJxFay4WTaOWF0EVuDN9oalK%2F9fU143KyI3x1NEUXzaI0FAC0sy1Xnxu65Pn5h%2FZ%2BT%2FaK3%2BRemFPdbBLdL8%2Fh%2FogzaoPavQYMB%2FXeNEQz8b4YZnfd3KtrOMokw4IhXRAx7uBc%2BPj9SAeqalNO%2B1EqYqbBMQfp6dRr5QuEMUd5MkUD%2FrFYZUeNi4FDHn7c5exwcEuKwmMgbnTBRHB%2FaTLOag%2BFxMIPBItJyodYldBDfyWwI1E9i11itJiOavTzSD%2BuuTMwDzNc7BOolyDakMfVuQEnfo37ARQOR9mDEaR3eP4bPSr%2BY5JlhlfFeNp9XwErhhVmYy8RK679A1yi4xscMBxga92d4svxRspAW6r%2F1uL01HezCrlpyIubUASIz65Y4QACOx520J7ewg%2Bclspd64LOiL7KX17Thx2wi0TDmP0iWpJ7XHD9OFdp%2BrDYErs6P1jwFo4%2FRZYxC3ccfT6Mx9i%2B0%2FEPzdAcN9W%2B1AZH7HJoQrebUnxH47I%2B9C%2BYG9kBqCbF%2FwBfvB3cl%2FRAJfmVLB5XymK2yW7VYhHLv3Aw2bf%2F0gY6pgE9mXTSg1e0gPRKXpmmbq0BJ0ZQ4DERDemSTs%2BO6hJejyDgDWdHZpw79ZOc9D9i1ynvpte8YvAUX%2B7RRXGLmoViP87Mh3jSzj7JzJ6Yvm7QOIkdgVRDGAZoR6LLJqZsaYKh2%2B5vZ6y8sUIHzI3Jr6TjVov1W8ThsBytkerXDZbzWHy3B3I564Q3NFVU2%2BA4kroX2VbzGcqiEA%2Frsx31%2FE%2FPgULle08q&X-Amz-Signature=95a4706f68dbf36c025ce5a8411a2f7fe63fae014b0982c6e175b8ea09accd00&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

架起需求到落地的桥梁，构建 IT 新蓝图。我是张飞扬。上一章节我们比较了一下不同的容器和编排技术，也讲解了一下 Kubernetes 的主要的思路和原理。这一章节我们就来实战一下。在阿里云上搭一套Kubernetes，在上面部署一些小应用。打开阿里云的控制台，选择左侧产品与服务，往下找找看能不能找到容器服务。 Kubernetes 版本，点进去阿里云上。当前 Kubernetes 有好多种不同的套路和玩法，我们自己看一下。辅导老师已经提前准备了两个集群，这个是用来做后续 demo 的。我们首先去创建一个新的集群，选集群模板。打开一看吓一跳，有这么多种不同的类型，托管的就是这么多种。


还有一些什么其他非托管的？所谓托管是什么？我们在刚刚说的 master 节点不需要我们管，最复杂的主控节点，灵魂歌手不由我们管，由它来帮我们管，所以相对来说是比较方便的。有个别情况下，我们 master 节点也要我们来管。这个时候比如像罗金，有些某些特殊场景，我们 master 节点自身管理，可能在上面要做一些特殊的处理。比如我们不满足于阿里云的次星级版本，我们要求用最新的Kubernetes，这个时候阿里的 master 版本可能跟不上我们最新的要求，所以可能会有点落伍。这个时候我们可能在物理机上采用全定制化的 master 节点来进行部署。相信大厂都是什么都是不会直接用公有云的，这种全托管的，都是会做一些自定义，做一些版本的自我掌控的。但是如果是中小企业，都建议采用全托管。甚至于是采用什么，这里飞老师很推荐的 serverless 集群。


所谓 serverless 集群，就是整个部署过程当中只有master，没有 node 节点，怎么工作？有了 master 以后，根据你的需求，你需要跑一些容器，承载一些压力了，它就会创建一些note。如果你没有压力，没有新的容器起来了，它有可能只是一个虚拟的概念在那里。所以这种被压力触发的，被消息触发的按量收费的方式很适合我们做demo，价格非常便宜，同时也适合那种弹性伸缩，从需求低谷到高峰之间差距很大，有百倍千倍差距的这种企业来使用。


我们废话不多说，就点 serverless 集群创建。点完以后大家可以看到这里可以填名称了。我这里填了一个 Imock Ark 的我们的架构师课程，他呦他说好像还不符合要求，不能支持下划线。好横杠 Imock Ark 哈。架构师的 Imock 课程我们选择上海。我们再往下看。
17 就是加 8 对吧，版本就是 1. 18，算比较新，但远远不是最新的 19 已经出来了。所以它通常都是一个次新版或者是更老一点的版本。网让它自建。选就选，随便选个区自驱 net 很关键。我们前面在e、c、 s 节点已经教过了 net 什么，内部节点访问外面最关键的一个路由协议就是靠 net 来实现。同样道理，默认了 Kubernetes 集群都是内部节点，它的节点你没法直接什么对外暴露，同时你也没法让这个节点去公网拉image。怎么样才能让这些节点从公网上可以拉到image？就需要开一个net，有了 net 以后，它就可以转换成公网地址去公网。


不管是谷歌的registry，阿里的 registry are dead，去拉一些 image 下来完成容器的部署。 service 的c、i、d、 r 就是什么它的服务网络的网段不用开的特别大，但是也至少也要有一个像 20 这样的大小，这样尺寸能保证什么？我们可以起很多个不同的服务，同时给每一个服务一个 ip 地址。所谓服务，可以认为是一个应用，一个微服务，就是一个应用，对吧？也是一个服务，这就是它。


ginities 的服务的概念，重点在于对外提供一种统一的用户体验，一种负载均衡的思路。这里 a p i server 就是我们刚刚说的架构图里面的什么灵魂歌手对外访问的一种方式。它是通过 a p i 的方式对外访问，不管你是图形化界面还是用 command line，其实底层调的都是 a p i。我们这里选一个很小的 a p i server 的负载均衡就可以了。


要暴露公网地址，因为待会我们拿一个控制台去访问它，所以要打开一个公网地址。如果在企业内部，你就会采用跳板机，跟服务器要在同一个网段的同一个交换机上互联，交换机对它这里创建出来交换机，你要把跳板机绑在他同一个交换机上，这个时候其实就不用开公网地址了，就更安全。我现在反正是demo，我们就简化期间开一下服务，发现不需要。


ingress 就是我们刚刚说的什么对外的一种API，网关，或者是一种路由。这种 ingress 路由我们选择endings，这两个都可以选。 English 是一种 7 层的路由，你选 s l b 就是tangent，你选 engines 就是标准engines。这两个有什么区别？ s l b 键的速度更快，性能更好一点，相对于普通的engines。但是有一个缺点，阿里云的 s l b 是一个定制化的天景，所以它不支持那种很酷炫的什么根据指向形成金字雀发布，根据你的 token 或者 cookie 实现u、i， l 的不同的转换。这些酷炫的功能在什么s，l， b 里面，气层里面天生不支持。所以我们还是建议选用endings，更灵活，虽然性能可能稍微打一些折扣。


要对公访问的，因为我们待会要去什么，要去用公网的一个节点就是我的笔记本来访问它，所以开一个公网。地址也是一个最小配置。 metrics server 主要是用来做监控和弹性伸缩的。我们也打开它。通常都会打开这里。日志服务是为后续我们的运维章节里面给大家看日志收集做准备。所以也勾上我们创建一个项目，每一个日志服务，其实它都可以挂在一个项目里面，或者用独立的项目。我星集群就有一个独立的项目，这样更直观更简单。


k native 就是我刚刚说的 serverless 的概念，它有一个头脑，有个眼，有个手，组成一套全自动的基于时间触发的弹性伸缩的功能。这个功能不是我们这次课程也主体，我们就省掉了。省掉可以省掉我们很多资源。基本弄完以后，点一个确认服务，再点创建就可以了。
创建过程当中要求什么？你至少有 100 块以上的余额，他会告诉你一堆价格，大部分按量收费，少部分像 net 和 e i b 又稍微有点贵。 s l， s 也小贵，也就是几角钱，几块钱每小时的价格，因为大家应该是都能承受得起，我们就点确认就可以了。整个过程有点小慢，他说 3 分钟，其实可能要在 5 分钟以上，所以我们就不等了。我们就回过去看一看。我们已经创建完了这个demo。我们给大家看一下它的日志。看它的日志，你就可以看它当时怎么样。它从下往上是看。先创建了一个什么集群的 certificate 开始初始化集群。 a s k 就是它的名称，叫阿里的serverless。就是你不用管 no 的节点，你也不用管 must 节点，全托管的 serverless 的 Kubernetes 2. 0。他会去建网络，建完网络以后建唯一的交换机，建完交换机以后建SLB，负载均衡，对外提供 a p i 访问，再开始创建它的 t c p listener，再建它的 i p 地址。


最后全部创建完了以后，绑上它的 ip 地址。同时因为我们刚刚每个节点本身要去什么公网拉image，所以启动了一个 net Gateway。所以它要把 net Gateway 准备好，一直到完全准备好把完 Nat Gateway 的 IP 才算是 Nat Gateway。全部创建完成了。之后，他要装一些小插件，全部装完以后他就自解自检。完了以后就告诉你，我的 serverless 的 class 大概在 5 分钟左右，或者六七分钟创建完成了，你可以来玩了。


这样一段话我们回到集群，我们不等它初始化完成，我们就在直接点 Imock demo 就可以进到这个集群里面工作。负载其实就是我刚刚说的叫 controller 的概念。这是 Kubernetes 里面一个概念，但下面有好多种不同类型，比如像不要。大家不光看中文，要重点关注一下英文。平时大部分的平台都是有不同的中文翻译，但是英文都是一样的。 deployment 这是最常见的一种部署方式，我们这里就部署一个deployment，可以采取用镜像来创建，也可以采取用模板，也可以用 kubectl 命令。我们这里带大家演示，就用图形化界面点点点。
这里面看到什么？是个羊毛文件对吧？这个羊毛文件就是最经典的。部署什么容器的时候，用 Kubernetes 创建一个小容器 pod 的部署文件，它自己说什么我调用某某 a p i 当前 deployment 这种类型的 a p i，最常见的就是 apps v y。选好 a p r 以后，选好我的应用版本的类型是deployment。所谓deployment，就是我刚刚说的无状态的一种应用，支持多副本。它的 replica 是 2 两个副本。每一个副本就是一个pod。这个 pod 里面会什么？会打上label，它叫什么？就叫做engines。 a p p 是 engines 的这样一个服务。你这个服务里面只起一个容器。


一个 pod 其实是一个容器组，可以起多个容器。它通常就起一两个就够了。我们这里只起一个。里面拉一个image，叫一点七点九，他从哪里去拉？如果你在阿里云，默认就去阿里云的什么官方的 registry 去拉一个 image endings，一点七点九。


拉完以后，它的 port 就是什么？是 80 端口运行起来，容器里面的应用会起来，端口会对外打开。就这样一套部署，我们点创建就完成了。我们再去点左边无状态，你可以看到什么？他希望起两个pod，这两个 pod 就是两个容器组，现在一个都没起来，要稍微等一会。在这段时间之内，我们点进去看一下它在干什么，它在什么？它是不是在container，在creating，在创建第一个pod，每个 pod 里面还有一个容器。我们再点进去看 pool 叫容器组，点进去看以后，诶，是不是下面有一个容器只有一个？它的 image 是一点七点九，它现在处于什么？正在什么？从初始化到 ready 到整个 port schedule 完，我估计是完成了。我们退回去看一下是不是完成了 running 了。
这两个容器组都已经完成了。我们再回到之前的无状态里面去看，两个容器组现在都完成了，右边斜杠需要起两个，左边是已经两个都运行起来了。很好完成了无状态应用的部署，起了一套endings。有状态英文的是什么？是那种我们说的中间件服务，比如是卡夫卡，比如Rabbit，m， q 这些中间件服务，或者是Redis。它们本身是什么？是要存储数据的，不是云原生的应用，不是业务代码的不舒服环境。所以它需要有一些状态。 coinities 就对它提供了 statefulset 的什么？一种工作负载的控制器。任务是什么？是定时的，通常是某个时间运行一次，或者是短时的。定时任务叫定时，这个任务叫短时就跑一次，跑完就结束的。


除此以外，刚刚说的容器组就是pod。它是什么？附属于job，附属于Cron， job 附属于Statefulset，附属于deployment。这里面其实有些漏，还有些什么demo， set 等等。因为什么？因为它这只是一个图形化界面，所以它功能没有像命令银行那么完整，那么全面。这是工作负载，为了洗一些容器对吧？洗完以后要对它外提供服务。需要什么？通过路由跟服务。


所谓服务，其实这样理解就是类似于s，l， b 的 v p 一个负载均衡器的 ip 地址，或者是一个 u r l 大部分场景下都是一个 ip 地址。我们这里可以看到它天生就起了一个whip，这个 whip 其实就是什么，我们之所以能登上 Kubernetes 的命令行，就是因为用了 a p i server。甚至于我们的图形化界面后台，你点击每一个按键的时候，它其实都是发一个 a p i，发到 ip 地址，发到内网的集群内部的 ip 地址，告诉他我要干嘛，我要查询，我要创建等等。


我们这里尝试来创建一个服务，也通过我们图形化界面的叫 YAML 创建，不用手敲了对吧？也不用通过 IDE 上装一些插件来帮我们自动补全那些 YAML 文件了，我们直接在界面上看，我们要起个服务，服务名字叫 my service，也不用改了。我们最关键是这里我服务要选择什么？打个label，这个 label 叫 a p p， key 是app， value 是endings。是不是跟刚刚我们看到的容器上面 label 完全一致？很好，我们服务就会自动选中刚刚容器，然后它起了端口。什么是 30080 端口？这个端口实际上对应到容器里面是80，也就是服务你要访问服务的时候，你要访问它的i、p、d，加上 30080 端口，但是它会映射到后台那两个容器的。我们刚刚起了两个容器，每个容器都是 80 端口。同时 nodeport 表明什么？我可以对外提供一个集群化的软件的 ip 地址，也可以对外提供一个每个物理节点的 ip 地址。有点细节，我们可以看看直中科课程里面辅妍老师的具体讲解。所以直接就跳过我们创建出来。


创建完成以后，我们回到服务，可以看到很快 my service 已经立马创建出来了它。虽然创建出来以后，其实对外提供的这种服务是吧？只在集群内部使用，或者是只在同一个 VPC 内部可以访问，外部其实访问不了，我想用我的控制台访问不了它不是很舒服。你这个时候怎么办？我就要建一个类似于 API 网关，类似于外部路由。我们在 Kubernetes 里面叫做ingress。 ingress 怎么建也很简单，我们就点击一个空空的创建，取个名字叫什么 imock Nginx 好，随便取的。我们要绑定一个域名，这个域名正常情况是要买的。飞扬老师说我买了一个叫飞扬点 imock . com，这是假的。待会我们用 postman 测试的时候，我会强行在 header 里面指定。因为辅导老师没有买域名。


好。我们假设买了路径，我们也不提了，来个斜杠表示跟路径。有人如果要访问飞扬点 Imock . com，假设我买了域名，它就会访问。什么访问？刚刚我们建了 my service 服务， the 自动补全了 800 到30080，端口不开的就是 HTTP 访问。就这样我们创建一下，立马就创建好了。如果你去直接点会发现失败。为什么？因为我们没有做 DNS 解析对吧？所以我们要在本地用 ETC host 文件做一次修改，你就可以点击了。但这样有点烦，要改本地系统文件。所以我们起个Postman， Postman 焊住了，好写。 Postman 开一个新的，是个get。我们把刚刚那个 ip 地址输给它，我们新建路由了。它是有个 ip 地址，我们点进去看它的 ip 地址是还没创建完成。 Nginx 我们刚刚说的它没有像 s l b 那么快。创建完成以后，在端点就可以看到它的 ip 地址了，现在还在创建过程中。 s l b 因为是阿里已经用 Tanjing 做了一个增强的服务，所以它创建非常快。但是我们选的是Nginx，它创建有点慢，但是相对更灵活，所以我们要稍微等一会，我们刷新一下。


诶，出来了。看到没有 ip 地址？复制一下，我们在 Postman 这里输入 ip 地址，因为我们头部其实 URL 是不没法解释的，没有什么飞扬点 Imock 点com。所以我们要写一个host，告诉他我是强行转换成了一个UI，叫飞扬点 i mook . com，他不用是什么根目录或者是不写都可以。


好，我们 get 一下。诶，是不是出来了？ welcome to endings 这就是成功地打造了我们刚刚的什么。对外的，这个叫ingress。对外路由，或者叫对外网关。是以什么？以这种形式，以 u i l 这个网关是 7 层的，它会判断你 u i l 不对，它就给你回个不对。比如我叫飞飞，不叫飞扬。好， not found。你不对，你访问我好像身份不对对吧？你要访问的 URL 不是我，你偷偷发给了我，不认。那就看完了。


ingress 这种 7 层的负载均衡也看完了。 service 这种什么把一个压力一个 i p 地址压到两个不同的 pod 也看完了。前面的什么无状态的应用部署是不是图形化界面点就完成了？好简单好酷炫。其实就是这样，容器化，尤其是在公有云，很多时候通过点你就能快速上手。但是飞扬老师要强调一下，其实有一点刚没跟大家聊整个 Imock demo 的集群创建的过程。


其实后台用的是什么？是 r o s 基础架构自动编排。也就是大部分的成熟用户是直接写 YAML 文件，采用自动编排创建出来。在什么？在 imock demo 里面部署的时候，也用 Coupo control 命令 apply YAML 文件来进行自动化部署。而初学者才会什么在界面里点出集群，在这界面里面点出负载，点出service，点出ingress。这些都是初学者。资深的用户全部可以用命令行。甚至于把命令行封装在什么？封装在像 Jenkins 这样的 CICD 工具里面，变成不可变技术架构，变成完整的什么？由代码触发的整体管控。聊完了容器的编排，聊完了容器的实战，下一节是什么？是面试环节和本章小节，相信大家其实是意犹未尽是吧？融资云这么酷炫，我怎么样实现金丝雀发布，我怎么样去实现监控？这个会在后续的云监控章节来跟大家实战的，大家敬请期待。

