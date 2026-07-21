---
title: 4-3 案例实战-腾讯云
---

# 4-3 案例实战-腾讯云

[image](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/b2f587ae-a1bb-4a50-a290-62e117409310/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XD4OAXBZ%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T231129Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQC1SsoKd%2FRgBUyEN%2BfG7iYsbtrSUka2manJ3s5y1YqlIAIhAJDZEBPbmdrcPfXpHJVLhsN4xFcIMcXIL436QRz4FnqpKogECMb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1Igx1LVFTav8KUms5mfcq3AOxPxw2NxtPzd4MmNlRYPzpvgtNQd0hoMeTMAzTnB7SQkJbV0H23AyNdKy8wq3E4NCPGBv6U%2B5N8ADIAv9nIkjZAp0lYbIN52shBgs02NEeq2qe65hShY%2FYGPQvYm6o4qb2n7CmgYCIPhszMaDyliRkga5a97FkdCZ1kpqUhOKmIUetZ7TGB1pzhWpgJW%2FUcfWuBHV7KJCQjIN4ezbVzyfZrUTFJRwk%2BvJrUCoDMNtnpNP8cA3IfEbN99aMhhY0AMoZMkrNW%2FzknOMJ0%2BeChXXDfWXr1XOeJwK0KrDPPOP6fa5zi2wuofYG1nNBvmq3tLhvh2mE9sfNOdi9wdYlE8HJxjsOcdh2ea0ZHA%2FRskpl8WvRsgGjz8FQ7EKG%2BWi7czmIT%2BF4gqzGZryWAFczDNkwiU4GKrfdzG%2FuXi6VLQ8B1pOLzUW6Rpd2kIhnQ9of0Iurmc3Z9w%2FM6%2FKkKNjyC1Ogcfpw1Rt5rZ5I0iX%2FElWM5MP5OgG55GLbLjj%2Bs6lQoOv2ZKC3TmjIycLT6OKvW7gFAvbjXDwP6b6HWr583F7OukRpbWjlV%2FVqaoW%2FRXMhvwf9knaZMUOG1Mf7G6QSwOg%2FGxS15lgTRf4KmgZ0ep86ZI4kUGf%2F4eAf%2BTygEjCTuP%2FSBjqkAR7F1Z6tYRK%2BkC%2FaODiSoMyKD%2F5nZKG6%2FNapU5qQ3vWFW9qqlD4YYEBezsUdvVYhhlQ9WZMHz5%2FYMWEDwDpkHVj6NqfS2XSMuQxqmjQrq3oxmhXOvSEALzNdpH1o%2BGcNGeonM%2BE3Hm%2FdRsAd7vuXyPxI4paWh4rQrozQGXgGcJzNGRbnkUv8pn47%2FPeE6axGYJGeSSLD8a79%2FG8DoTfUHWvFHJCT&X-Amz-Signature=118b588e90c0a0886bcca79d64f523c4f50c783ce92b759fa6681f229865a5df&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

加起需求到落地的桥梁，构建 IT 新蓝图。我是张飞扬。上一章节我们聊了聊腾讯云大部分的计算、存储、中间件、数据库以及网络单元，和其他云平台没有太大的差异。这里我们就重点来实战一下。其中有差异的部分就是 t s f 腾讯云的服务框架。这是什么样的一套功能？我们首先需要在腾讯云的 consul 里面进行注册，注册完了以后，

[image](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/14e57591-a421-4edf-b810-4f92137a9d36/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XD4OAXBZ%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T231129Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQC1SsoKd%2FRgBUyEN%2BfG7iYsbtrSUka2manJ3s5y1YqlIAIhAJDZEBPbmdrcPfXpHJVLhsN4xFcIMcXIL436QRz4FnqpKogECMb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1Igx1LVFTav8KUms5mfcq3AOxPxw2NxtPzd4MmNlRYPzpvgtNQd0hoMeTMAzTnB7SQkJbV0H23AyNdKy8wq3E4NCPGBv6U%2B5N8ADIAv9nIkjZAp0lYbIN52shBgs02NEeq2qe65hShY%2FYGPQvYm6o4qb2n7CmgYCIPhszMaDyliRkga5a97FkdCZ1kpqUhOKmIUetZ7TGB1pzhWpgJW%2FUcfWuBHV7KJCQjIN4ezbVzyfZrUTFJRwk%2BvJrUCoDMNtnpNP8cA3IfEbN99aMhhY0AMoZMkrNW%2FzknOMJ0%2BeChXXDfWXr1XOeJwK0KrDPPOP6fa5zi2wuofYG1nNBvmq3tLhvh2mE9sfNOdi9wdYlE8HJxjsOcdh2ea0ZHA%2FRskpl8WvRsgGjz8FQ7EKG%2BWi7czmIT%2BF4gqzGZryWAFczDNkwiU4GKrfdzG%2FuXi6VLQ8B1pOLzUW6Rpd2kIhnQ9of0Iurmc3Z9w%2FM6%2FKkKNjyC1Ogcfpw1Rt5rZ5I0iX%2FElWM5MP5OgG55GLbLjj%2Bs6lQoOv2ZKC3TmjIycLT6OKvW7gFAvbjXDwP6b6HWr583F7OukRpbWjlV%2FVqaoW%2FRXMhvwf9knaZMUOG1Mf7G6QSwOg%2FGxS15lgTRf4KmgZ0ep86ZI4kUGf%2F4eAf%2BTygEjCTuP%2FSBjqkAR7F1Z6tYRK%2BkC%2FaODiSoMyKD%2F5nZKG6%2FNapU5qQ3vWFW9qqlD4YYEBezsUdvVYhhlQ9WZMHz5%2FYMWEDwDpkHVj6NqfS2XSMuQxqmjQrq3oxmhXOvSEALzNdpH1o%2BGcNGeonM%2BE3Hm%2FdRsAd7vuXyPxI4paWh4rQrozQGXgGcJzNGRbnkUv8pn47%2FPeE6axGYJGeSSLD8a79%2FG8DoTfUHWvFHJCT&X-Amz-Signature=76c6b50c6296b96e2a419130c84a9c61a914e9e87ba7d290d6635a99b1b99eed&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

通常还要进行一个个人的实名认证。当认证完了以后，它会跳到一个首页，叫什么免费产品个人专区。我们就从免费的产品开始走起。首先我们看一看这里有哪些免费的服务。有一些前面类似于我们说到的亚马逊的 Landa 的这种叫 service 服务，也有轻量级的 c v m。这个 c v m 其实就是什么虚拟机是什么？是云上的腾讯的虚拟机，也就是类似于阿里云里面的 ecs 的机器。我们就从免费的是在北京的 15 天可以使用的小机器开始尝试。首先去创建一些资源，我们就开始采用这种 tsf 的框架进行应用的部署。点击这里试用。这也可以看到什么只有指定地区指定的 CPU 内存才能够免费。我们既然是做小demo，就使用它的指定的内容操作系统。我们可以换个新一点的，比如它这里默认是 7. 6，是 364 最新的了。好，就用它私有网络对吧。默认网段全部用默认的。我们就用 15 天，不用升级，点击领取就属于处理中。稍等一会好。领取完成了以后，我们就点击支付就可以了。选择确认 0 元的一套系统。


我们点击什么进入控制台，来看一看这台机器是不是还在创建中。我们把页面放大一些，这是什么？这就是腾讯云的云服务器 c v m 的界面了，我们刷新一下，看看什么时候才能建立完成。当前地区选错了，好吧，我们刚刚是选的是北京，所以我们要切换到北京地区。是不是一台机器已经在运行中了，也就算已经创建过出来了。这个时候如果你是个人，是用手机账号注册或者微信注册，它就会向你的微信账号和手机账号推送短信。你已经购买了什么什么资源，这个资源已经在创建中，或者已经创建完成。


创建完成以后，其实我们就可以登录它做一些基本的操作了。今天我们不是要看它普通的虚拟机怎么创建，而是要什么，而是要做一个酷炫的 TSF的实战。所以我们在我们的产品页去找一找强大的TSF 它在哪里。它属于中间件平台，里面叫腾讯微服务平台，其实就是 Tencent service framework 的缩写。微服务平台现在还没有把机器的管控进去，所以语音主机是没有集群，也没有建应用，也没有部署。我们一来做，我们先去建一个集群。建集群我们就点击这里新建集群。大家可以看到是不是刚刚说的，它既能支持虚拟机集群、容器集群，还能支持serverless。所谓 serverless 集群完全按什么使用量收费，它不会根据你的 CPU 内存来收费。这样集群我们这里用最简单的也是什么腾讯最独特的，居然可以在虚拟机里面用 spring cloud 帮你完整的实现一套服务治理。也可以什么用服务网格在虚拟机层面实现服务治理。


酷炫。我们就叫Imock，集训名叫Imock。所用区我们就选北京一区。我们要首先要看一下到底是选北京几区合适。是这样看，我们云产品里面找到我们刚刚的服务器，服务器下面其实它对应的有一个叫网络，它的网络我们在网络那个地方，我们要确认一下它是属于哪一个网络，是不是北京一区还有没有看到这机器就建在北京一区，所以我们在刚刚的咨询创建在北京一区上，北京一区选择他前面创建的默认网络，点击提交。


好很快对吧？集群就出来了，但集群里面还没有主机，所以我们要导入一台主机，准备用来做什么应用的部署。北京一去，这台主机就自动找到了，点击它，下一步它说重装系统，装 agent 都可以，大家看如何实现更方便。我们这里就可以选择是重装系统，因为无所谓。我们选择 open 阶 DK 的部署方式，它在里面什么装错系统的时候，会用一个带 open 阶 DK 的什么 image 来进行快速重装。我们还是喜欢用 Cento s 设置一个密码，设置一个辅导老师的常用密码。设置完了以后，我们点击一个提交，它是要有一个等待的过程。导入成功了，我们点击关闭。这个时候那台机器已经开始进行重装了。重装的过程当中，它为什么把相关的密码进行重设。操作系统重装，我们看一下是不是还在重装过程中稍微花一点时间。


在重装的过程当中，我们其实可以准备应用了。我们应用怎么准备？是这样点击应用管理，这里我们可以去新建一个应用。这个时候小时候我们就取的名字叫什么，叫producer。我们会用一个默认的 demo 应用，也就是腾讯的 t s f，里面默认提供了一个 demo 应用。我们待会去到官网去下一个应用的包，采用虚拟机部署普通应用。所谓普通应用就是用 spring cloud 的技术来实现服务的智力。你如果选了mesh，就是什么 service mesh。对，虚拟机的 service mesh 就是前面说的什么 spring cloud sidecar 的形式。如果你是容器形式的mesh，就是 is still a service mesh。


好，我们就选普通应用。我们提交一下，他说要上传一个应用包，我们就要去下载应用包了。应用包在哪里下载其实很方便，我们只要在腾讯云的官方的文档里面去找一个叫做什么 TSF 的文档，随便找他的。比如总览页，这里就会有开发者手册。我们放大开发者手册通常是什么。每个云平台我们要对接平台，首先就要看的是开发者手册，阿里云、百度云、腾讯都一样。这里如果你是以 open JDK 的形式进行部署的镜像，它这里就会提供一些标准的价包的下载地址。敷衍老师已经提前下好了。


什么打包，编译好的架包。如果你希望是从无到有开始，你可以点击什么基础手册，从这里面找到对应的一个源码。对应的源码自己进行什么编译打包。如果你要发布成容器，你也可以参照其中的这种什么基础手册，把它什么先编译成架包，再什么用 doctor 把它转成对应的image，发布到腾讯云的镜像仓库里面，选择容器的方式进行发布。


我们这里因为是虚拟机，只要下载价包就可以进行了实操了，我们看一看我们刚刚的操作系统重启是不是已经完成了。我回到这集群，已经有一台完成了，已经属于我们叫什么虚拟机集群了。这个时候我们就可以开始真正的去部署代码了。我们在应用管理这里重新点击应用，我们尝试进行软件包的管理，上传一个软件包，点击一个文件，好分享老师也提前准备好下载好的一个软件包，就叫provider，一个小应用好版本随便选就选 1. 0 好了。我们点击个提交。整个提交过程其实就是把我价包发布到腾讯云的什么后台的这种代码仓库，或者是弓箭仓库。传完了以后，后面还有一步叫做部署。部署的时候才是什么真正在我们的服务器里面前往部署，所以在部署的时候，我们才是真正的在什么服务器里面去部署。


加包。我们新建一个复数组，开始真正部署了，我们就叫它producer。这样一个部署包。我们选择我们的集群，就是刚刚创建的什么虚拟机集群，命名空间选 default 就可以了，日志项也都是默认的。好，我们点下一步。这个时候我们就要选择在整个什么集群里面有很多机器，我们有哪台机器部署，我这里只有唯一的一台。点击应用部署，系统就开始把价包上传上去，启动我们。


什么。我们指定了 JDK 的 Java 的进程，尝试去以一定的参数，以这样的参数而最后的真正刷新我们的整个进程，从而实现应用代码对外展现。我们点进去要选的部署的版本是 1. 0 版本，点进去好，这个过程就开始进行真实的什么应用的发布了，是不是很快？应用快速的进行了什么上传，以及快速的启动。我们看一看启动完了以后会有什么样的一个应用的状态。好，我们把鼠标移到左边的面板，这里不选应用管理，而选服务治理。当应用发布完以后，它默认会以一个服务的形式对外提供出来。我们首先看一下服务有哪些具体的功能，以及如何对它进行访问，再来看如何对它进行治理。



首先我们点到具体的服务名称，叫 m s 杠 V6R z g k 9V。这是一个自动随机生成的服务，会跟什么我们刚刚的应用属于同一个命名空间。冰冰空间可以理解成我们 Kubernetes 里面的 name space，或者是其他的这种什么。租户的概念，云上租户的概念。一个租户可能就是管理一部分的服务，这部分服务通常是处于某一个大的领域，或者是大的系统里面。这套所有的服务可以什么？通过这种服务拓扑展现的形式，能展现出多个不同的微服务之间的调用关系。因为我们这里只发布了一个服务，一个 provided 的小服务，所以它只有一个。如果多个，每一个服务都有状态，它们之间还有箭头的关联关系。好，我们不看具体关联关系，我们看看服务的具体信息是什么。这个服务对外提供了一个 ip 地址，叫什么？叫 140 点几。我们先复制一下，在这里输入一下它的 ip 地址。服务还有一个对外的服务端口，通过 ip 地址跟端口就可以访问服务了。


有了 i p d 的装好以后，我们看看 a p i 的路径到底是什么，我们可以在哪里可以在接口列表里拿到。整个 a p i 都是 documentation 的，都是有文档的，中间有很多标准的 SWAGC 这样一些状态检查的文档。我们尝试在下面的地方用一个 get 的命令，比如 Echo 来实现一些基本的功能。 Echo 就是什么你输出给他什么，他就返回给你什么。我们尝试一下进行一个 Echo 的显示，尝试来一个飞扬，是不是有返回值？我们放大一点。好返回值。诶，你的需求就要飞扬，我就返回你飞扬。同时我告诉你是哪个服务返回给你的，叫 Echo provider default name，这是服务内部的名称。既然这样，我们就成功地访问到这个服务。服务开了一个公网地址，对任何用户，任何的请求者、任何 IP 都可以进行响应。我们尝试对服务进行一些少量的治理工作。
怎么验？治理上面有很多功能，比如鉴权、路由、限流、熔断服务等等功能，我们点击鉴权，所以可以看到什么此版本不支持此功能。这是什么原因？我们应该什么去看一看如何进行规格的调整，从而能让它能支持像鉴权、路由、限流、熔断等功能，我们点击前往调整规格。
在这里我们可以看到我的默认是吧，是北京的。同时我是基础版，而基础版是不支持一些高级功能的。我们这里打开看一下基础版能支持哪些，附带均衡服务，发现都是可以支持。也就是如果我刚刚选了应用部署到 4 个节点，这 4 个节点默认什么？每个是 25% 的 round Robin 的概率。他们可以实现服务的整体的注册和发现。同时包含虚拟机管理、仓库管理、镜像管理以及配置推送，这样些基本功能都可以统一在基本版里面进行提供。


但是如果你要玩这种酷炫的服务智力，比如像我们这次会实现的服务的鉴权，以及大家课后可以去尝试限流熔断，只要专业版或者铂金版，我们废话不多说，我们就直接改成专业。这里要强调一下，改成专业版的时候，千万不要增加节点数。增加节点数它是什么？它是按院收费，价格是比较贵的。同时如果你选铂金版，它的价格就会更贵。所以我们推荐是专业版的最小配置。


在当前环境，在整个新的 TSF 架构，在什么试运行一年之内，它都是免费的。如果我们在 2021 年年底，我们可能会出现收费的情况，这个时候大家可以斟酌是不是要实战一下。好，当前免费，我们把它转成 20 节点的专业版，北京地区好提交订单。也不用进入控制台了。我们就重新刷新一下刚刚的控制台，看看能不能把鉴权功能给大家演示一下。诶，是不是服务鉴权的功能就可以使用了？因为已经采用了专业版的什么TSF，当前是不启用，我们当然需要启用了。我们搞一个白名单好不好？白名单确认以后是吧？黑白即黑，不支持该操作。我们来个黑名单也不支持。看一下。通过标签黑白名单提示进行访问控制。诶，怎么会不支持呢？很奇怪。


可以了对吧？刚刚可能只是因为什么，因为我们刚刚升级完以后，他白名单的规则有点慢。好，我们现在点出来白名单了，允许调用。我们这里点击新建鉴权规则。在新建成规则里面，我们什么 my IP，只有我的 IP 才能访问，别人的 IP 都不能访问。这里面我们可以取一个什么规则的名称，我们看一下上游服务名称等于什么？什么把服务名称等于什么？什么？我看看上游 i p。好，上游 i p 等于假设我们等于什么。九点九虚假的我没有 i p 的。也不用动态生效状态了，不用管，直接生效就可以了。


好，我们点击确认了，添加具体的白名单规则。好。确认完以后，下面什么可以看到鉴权规则为空，我们点击新建鉴权规则，输入一个名称 new rule 的新规则。好，这里可以什么给它取一些标准的系统标签，也可以自定义一些系统标签。通常我们采用一些标准的标签，我们看一下有哪些标签和套路。最常见的就是根据上游服务名，也就是服务 a 才能调服务b，服务 b 才能调服务c。因为我们当前只有一个服务，我们可以把它变成死循环是吧。自己才能调自己就是provider， demo 才能访问provider。当然了，你也可以根据什么命名空间，应用版本号，部署组等等具体信息，甚至于根据路径，根据方法都可以进行什么服务调用的控制。


我这里偷懒选择一个 ip 地址，选择一个不存在的 ip 地址，什么九点九点，九点九，也只有特殊 ip 地址的什么笔记本或者电脑了才能访问我。服务我们选择生效状态为确认，也就是一旦创建完以后，立马把生效好，稍等片刻。这条规则什么正在刷新过程中，等到刷新完了以后，它会生效，完了就处于已生效状态，已开启状态。好，如果大家点不启动或者点黑名单，会导致整个的什么？整个白名单无效。所以非黑即白。通常你选择白名单，你就建一堆的白名单规则，没法同时兼容黑名单规则和白名单规则。这也是服务治理里面很多的平台都普遍存在的一个限制。好，我们现在去看一下。再访问刚刚应用现在是什么？我们笔记本电脑的 ip 地址不是九点九点九点九，所以可以详见应该是什么。报一个鉴权出错对不对？ 403 你没有授权访问网页了，我们如果尝试把它重新加回我们的什么，或者把它改成黑名单好不好？我们把九点九改成黑名单看一下 i p、 d 是等于九点九点，九点九是黑名单还是动态生效。好，我们再来看一下。我的笔记本电脑肯定不是 ip 地址，所以是不是能够正常访问了，又能正常访问了，又返回了。飞扬好，我们的鉴权功能就到此演示为止了。大家可以尝试一下进行一个路由设置。路由设置通常什么你要设置一个路由规则，你要指定多个不同的部署组，不同的版本号，进行什么负载均衡的，权限的掌控。同时大家也可以尝试一下这些包括什么设置上限，设置容的等等。刚刚这里有点卡，我们可以在这里再点进去。刚刚服务，我们对服务也可以去设置它的熔断网络稍微有点慢，稍等一下。


好，我们也可以对服务设置它的限流，设置一个限流规则，在什么时间之内能请求多少次，一旦你的次数超过它，比如你用 Postman 的 runner 的功能，或者是 load runner 一些压测工具尝试，或者是解密特进行压测。你可以看一下它的限流效果是不是非常好。
除此以外，熔断也是一个很酷炫的功能。我们可以创建熔断的规则，只要你的 springcode 接 DK 的版本是比较新的，我们默认从官网下载的版本，或者是我们默认的在应用部署的时候选择的版本都是新的版本。所以你可以选择你是用服务的级别进行熔断，还是实例还是API，也有它自身的熔断的滑动窗口，以及什么它的具体出错的情况，什么时候触发半开全开的设置等等，大家有兴趣可以逐一实战。
好，聊完了。什么 TSF 的实战，大家是不是感觉到一个特点，不管是服务器还是容器，不管是什么我们的服务网革性的这种服务治理，还还像是 spring cloud 这种应用发布的智力，这些功能都很方便的。什么集成在一个平台里面，这就是腾讯云此套软件的优势。同时我们其实有些基本功能没有具体展现，比如服务的监控，链路的追踪，弹性的伸缩这些。


什么是 Kubernetes 所具有的功能，或者是腾讯云的c、v、 m 本身的什么高可用弹性组所具备的功能，它也把它整合在了整个什么整个t、s、 f 的整体服务框架里面，可以腾讯云的亮点其实都在新平台里面了，大家可以什么好，来平台里面感受一下它的酷炫之处。好，聊完了腾讯云，下一个章节我们尝试给大家聊另外一个云华为云，大家敬请期待。


