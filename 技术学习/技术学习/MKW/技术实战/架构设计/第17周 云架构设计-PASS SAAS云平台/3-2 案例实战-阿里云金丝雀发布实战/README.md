---
title: 3-2 案例实战-阿里云金丝雀发布实战
---

# 3-2 案例实战-阿里云金丝雀发布实战

[image](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/eea410c5-037f-402c-8fda-d81dcf70f959/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663TP5VK4W%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T231124Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIAyNfM%2B6nRozqd3WtWkFJBUwU5F%2Fu9IRCcxgkQqHtncTAiAzzcjm%2Bzus4Xyw%2BEc4z7Rs7Gv09nCYqTKKS01C9unRMiqIBAjG%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMG0umTuVQeqRxX8wyKtwDCCRIlXJuPOCtCk6daN993nU360Qa1JZIE9aAMrMwEYzI9yfYZ6MOAZZzQ01L%2Fa387mtn07c4439Pd%2BBWTY9vldSe5oaMbyL0tWaLxnaqKk1W%2FN9fQh51nl36IrMRZcfOqLOMjVUUYj6VKNjh2bhGjBiAUlaaLWo5XBnPTDDfMJ%2BcyvWJawMFaq0JW9dda4s%2FSWSzU8BotMoZsyAc2jlD7sE%2FX3ImsMtR9CzR8nSJeJjnYnGurIgUVYXI1%2BqZOdupPP%2BpLmnTCxqYilIYQ0puigvEuY7a6JQPE2GxOKe%2FlxPn72yHmN7fykUdANHrq7l3QuToE8D%2BcKlaUfA3tpMFxWLANWuH1lKUdZiOpYnvWeniHOgCyl7yoQhnIgxm9bog2%2F6YVNcbtNNs242oKw3gnCAQIzbs7AXlLLsihxlqrz9SZpC42Bag%2FANEApgv9W1lYioWNgVbWhcafdxHUIpsEKEO3CI4SZevWtsrF%2Fn6SZ738vo6tS91GGbZANf0gas45h22%2BBjEDDmhvFjgjOZhZYaDLK5Jy%2FdZgWYlYaKRLBPEcyBupJknc%2BGDeLjBhyBqPQoiskMiGqWFrNAIGD4tXvTXQ6a0NdAKEwAdH80SALutXaRLE9AOw6ism2Qwhrf%2F0gY6pgHUxmpKuwbb%2FcFkIPRNHhsECS%2BqNEqxstUwcvGyy00KXnh6tKts0oTGRlknRirAhyBuA%2FexMJ8EIFREIC%2B%2FC3gMQ011NRHcLQ0Z8q6GOLpHPq0cxsWxB3VtanPYu4D%2B0pjGK%2F9VlyEtdqaUgmUN9G7V2Fb7jlMt%2FwDhN%2F5plglcQgpqFaebQJhs5R3K7ObJun5NJGDbuw%2FBlxjiPVG%2Feiv7SuTm6uLU&X-Amz-Signature=464c207b36e34906b61ba5fcfb5c2397c2fdf9344868965ab413c0530e2acf4d&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

需求到落地的桥梁，构建 IT 新蓝图。我是张飞扬。上一章节我们聊了聊云发布这个章节，我们在阿里云的 Kubernetes 里面来实战一下，看一看如何实现金丝雀发布的。首先我们什么？

[image](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/2faaa498-477b-4282-b5e4-a0772f181a40/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663TP5VK4W%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T231124Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIAyNfM%2B6nRozqd3WtWkFJBUwU5F%2Fu9IRCcxgkQqHtncTAiAzzcjm%2Bzus4Xyw%2BEc4z7Rs7Gv09nCYqTKKS01C9unRMiqIBAjG%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMG0umTuVQeqRxX8wyKtwDCCRIlXJuPOCtCk6daN993nU360Qa1JZIE9aAMrMwEYzI9yfYZ6MOAZZzQ01L%2Fa387mtn07c4439Pd%2BBWTY9vldSe5oaMbyL0tWaLxnaqKk1W%2FN9fQh51nl36IrMRZcfOqLOMjVUUYj6VKNjh2bhGjBiAUlaaLWo5XBnPTDDfMJ%2BcyvWJawMFaq0JW9dda4s%2FSWSzU8BotMoZsyAc2jlD7sE%2FX3ImsMtR9CzR8nSJeJjnYnGurIgUVYXI1%2BqZOdupPP%2BpLmnTCxqYilIYQ0puigvEuY7a6JQPE2GxOKe%2FlxPn72yHmN7fykUdANHrq7l3QuToE8D%2BcKlaUfA3tpMFxWLANWuH1lKUdZiOpYnvWeniHOgCyl7yoQhnIgxm9bog2%2F6YVNcbtNNs242oKw3gnCAQIzbs7AXlLLsihxlqrz9SZpC42Bag%2FANEApgv9W1lYioWNgVbWhcafdxHUIpsEKEO3CI4SZevWtsrF%2Fn6SZ738vo6tS91GGbZANf0gas45h22%2BBjEDDmhvFjgjOZhZYaDLK5Jy%2FdZgWYlYaKRLBPEcyBupJknc%2BGDeLjBhyBqPQoiskMiGqWFrNAIGD4tXvTXQ6a0NdAKEwAdH80SALutXaRLE9AOw6ism2Qwhrf%2F0gY6pgHUxmpKuwbb%2FcFkIPRNHhsECS%2BqNEqxstUwcvGyy00KXnh6tKts0oTGRlknRirAhyBuA%2FexMJ8EIFREIC%2B%2FC3gMQ011NRHcLQ0Z8q6GOLpHPq0cxsWxB3VtanPYu4D%2B0pjGK%2F9VlyEtdqaUgmUN9G7V2Fb7jlMt%2FwDhN%2F5plglcQgpqFaebQJhs5R3K7ObJun5NJGDbuw%2FBlxjiPVG%2Feiv7SuTm6uLU&X-Amz-Signature=2ba91183c3d35e8329a94a7ba2aab4b6338006c17b10d7bf0369bc6195ac434a&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

我们会准备好两个镜像。这两个镜像是从网上找来的。一个镜像就是一个Nginx，改了一下小小的配置，使它什么。打开 Nginx 主页的时候，只看到三个英文字母o，l，d，也就是old。新的镜像，大家可以猜一猜，也是三个英文字母n，e，w，new。这两辆各镜像很容易区分。


我把 old 镜像通过 Kubernetes 里面的 deployment 发布了到两个容器上。右上角看到的两个蓝颜色容器，它共同对外提供一个服务，叫做 old 横杠Nginx。这样一个服务，也就是在容器的集群内部 Kubernates 里面，你要访问容器，其实你只要克 old 横杠Nginx，就能返回一个old。这有一半的概率在上面。一个容器也有一半的概率在下面。一个容器总体它的应用代码是 v y。另外还有一个容器是什么？是 v two 的容器。它是用什么？因为会返回 new 的镜像来发布的。


发布完了以后，在上面提供了一个服务，叫 new Nginx。一开始我们是传统的所有代码，所有压力，全部什么压在 old Nginx 上，这100%。这是第一步。实验的第二步是什么？尝试做一次应用发布，发布完了以后，让飞扬老师可以在内部做测试怎么样来实现传统的负载100%？还还是发布在上面什么 old Nginx 里面。但是对于 HTTP 的头部，如果 value 是负等于 8 的这种负载就证明什么是飞扬老师在偷偷做测试。这个时候这种负载是压到了绿叶子上，就相当于什么把金丝雀放到了煤矿厂里面，放到煤矿场里面来看一下这个金字去死没死什么，就证明 OK 了。就让很多的什么矿工可以进到矿场里面来开始挖矿了。旷工进场的方法怎么样？下面把实际的客户负载以 10% 2 十五十八十一百的形式逐步压到新的 new Nginx 上面。


如果是传统的虚拟机，大家可以感受到你虚拟机的数量有可能就决定了你的负载的数量。比如老的虚拟机有两台新的虚拟机，有一台新的虚拟机只能接收到 33% 的负载。但是在 Kubernetes 里面，一旦用了 ingress 就不一样了， ingress 的负载比百分比是可以随意切控的，我们尝试切个 5 十给大家看一下。


两个老容器，一个新容器，但是可以精准的实现 50% 50 的负载压力。废话不多说，我们来看一下代码。在我们之前搭建好的 Kubernetes 集群上，实战已经打开了我们的 ID 平台。我们看一看 endings Kubernetes 里面怎么写。很简单，先指定它的 API 版本，说明我是一个deployment，我是一个什么？我是一个无状态的应用。取个名称，指定好副本数，两个副本，也就是起两个容器组，两个pod，它对应什么？对应这样一个舰支队，叫做run，等于 old Nginx。这是容器身上的舰支队，舰支队的具体的容器，它会跟下面的 service 对应起来。 service 就是对外提供服务的什么那种统称，或者是网络负载均衡的概念。内部的负载均衡它会指定的。我希望我映射到的是吗？是哪一个键？指标是 round 冒号。 old endings 恰恰就是跟上面那两个容器相对应。我刚刚图里面画的 old endings 服务会映射到这两个容器，是从阿里云的仓库里面下载下来的。其中它的什么映射端口是80。另外它是每次都尝试从什么从镜像里尝试去下载，也启一次应用，它就会去下载一次。 80 也是跟下面的什么 target 80 对应起来，也就是我的服务接听端口是80，正好了。


service 把内部的容器的 80 端口映射到什么服务名。冒号霸凌端口，也就是在集群内部，你要访问它就是 old 杠engines。冒号 80 就可以访问服务了。有一半的概率打到其中的一个pod，还有一半概率打到另外一个pod。这是第一个蓝颜色的服务的发布。绿颜色服部。
engines new 其实几乎是一样的，取个名称不一样。打一个 label 叫 new Nginx，下载的 image 也是一个 new engines，所以它会返回一个new。这里面端口也是80，它映射到服务，我们也取个名字叫 new Nginx。同样也是什么 new Nginx 映射的容器就是上面选中的唯一的run，等于 new Nginx 的这样一个容器，也是只有一个。


我们把刚刚图里面画的内容通过什么，通过羊毛文件描述了一遍， Kubernetes 要运行它。其实只要 Kube apply 羊毛文件就能够创出对应的服务，也能创出对应的应用。我们就来实战一下。好，我们回到了 Imock demo Kubernetes 的集群。我们尝试什么？我们尝试看一下当前是什么样的状态，有没有什么deployment。之前什么在我们容器章节里面部署的 endings 还在，它也有跟它对应的符 my service。另外也跟它对应的一个路由，叫什么叫 Imock antics。但这次我们新建的内容不会去修改，原来的什么 URL 都不会修改，原来的服务也不会修改。我们会创建一套新的。同时我们会给大家展示一下怎么样用命令行来完成指定的任务。我们控制台这里有一个命令行，我们打开以后我们可以进到飞扬老师的目录。这个目录底下提前准备好了。


刚刚我们在什么？我们在 i d，e， a 里面看到了几个 YY 文件，已经准备好了。其中先部署engines，也就是我们刚刚看到 y 文件里面什么部署两个 old Nginx。起一个服务，用 Cuba control apple lie 杠 f and Jinx。我们放大一点是不看更清晰一点。好点，羊毛就把什么两个容器给起来，已经起完这两个容器了。


这条起完这两个容器 deployment 下一条是什么？服务也创建出来了，他虽然企外了，其实是什么？后台还在慢慢启动，只是把什么把资源定义发给了Kubernetes。完成了后台启动，还要花点时间，我们不用等它。我们再看一下另外一个Nginx，new，这个应该是起一个会返回什么 new 的endings，我们看一下是不是这样，跟我们刚刚看到的一样，起一个它的类型，或者它的 image 的名称叫 new Nginx 的这样的一个容器。同时它会把它相关的服务也给起来。我们已经成功了。什么起来了？容器完成了服务的创建。这些准备工作完成以后，我们回到图形化界面，看一下有什么区别，还是无状态。是不是出现了一个 new Nginx，一个 pod 还没起完，还在启动。我们看一下 old Nginx，两个 pod 已经都起完整了，状态都是 OK 的。这里显示二级表示状态都是OK。我们看看服务。


回到图形界面的服务，这里是不是 new Nginx 起了一个服务， old Nginx 也起了一个服务，每个服务有它自己的IP，所以你在集群内部可以访问 i p，加上它的端口也可以直接什么访问服务的 u r l。比如这里就是 new 杠 engines 和它的端口就可以直接访问了。但是我们会尝试用 fair 老师的笔记本电脑。所以是在外部的，不能直接访问服务，必须通过路由或者是什么。要把服务改成负载均衡，或者是 know the port，要使用它的物理节点。这些都不是常见的方法。最常见的方法应该就是采用 ingress 对某些 u l 进行不同类型的金丝雀访问。我们回过头去看一下是不是无状态应用。 new endings 也起来了，要起一个 pod 也起，已经起成功了。我们下一步就开始要压力上去了。我们要把什么压力 100% 压到我们的 old engines 上？还是用命令行？我们再打开我们的命令行。我们用什么用 ingress 来实现施压？我们看一下刚刚在代码里面没有带大家来看 Nginx 是吧？我们来看一下在 i d e 工具里面看一下ingress。


其实规则很简单，就是它的 API 类型是 extensions v y， Meta 的类型。他说我是一个ingress，我具体要干什么事情？这是取个名称，无所谓的名称。我要对所有访问我 ip 地址的负载来看一下。你在压力压过来以后，我要看一下你是不是想访问 3W 点 example . com。如果是，我要看看你的路径了。如果你要访问根路径也不带目录，或者是根目录的，我就会把什么。我就会把所有的压力都发给 old Nginx。所以这样的情况下，你是什么？我的笔记本电脑用 postman 去调用 3W 点 example . com，永远返回是 old Nginx，不会有看到 new 字样。


好，我们试一下。怎么样来部署 ingress 呢？我们用Cooper，图跳 apply 一下， ingress 已经创建完成了，我们可以在图形化界面里确认一下。其实可以用 kube get 命令来确认。我们这里用命令行跟图形化界面互动，可能感受更好一些。是不是有一个 ingress 就生成了？它是永远指向什么？ old engines 名称无所谓，它的重点是内容规则。它是永远指向 old endings。我们用 post man 来发起一下压力，但是我们 i p d 只知道吗？还不知道，我们还要回过去看一下。


跟上一节一样，我们看一下什么时候它能够把 ip 地址显示出来。这里还没有把端口显示出来，就证明什么 Nginx 服务还在创建，服务还没创建完，等它显示出来为止。这时候我们就可以用压力了。而压的时候要注意就是要把 host header 里面的 value 改成3W，里面 example . com 还慢慢的端口还没出来，所以还要等一会。


Nginx 我们应用测试的也是 Nginx 是吧？实际的什么我们的负载均衡路由 ingress 也选的Nginx。听上去有些混淆。其实无所谓。外面才是什么。真正做路由做 a p i 网关的。里面 engines 只是我们采取做实验的一个小程序，比较方便的返回一个数据给大家。我们再等一会刷新出来了。通常我们一个系统里面是吧。它不管起多少个ingress，它只是什么不同路径，它的 i p 地址都是一个。这也是 ingress 相对于什么 loader balance 的一个好处。我们 Kubernetes 里面其实还是可以支持 loader balance，但 load balance 一个项目里面可能每创建一个 loader balance 都会花钱。但是 ingress 不一样，通常一个项目创建 ingress 就会只用一个 ip 地址就够了，这样就可以很省钱的模式。所以 ingress 也是 Kubernetes 里面最主流的什么对外提供服务的一种模式。就是 ip 地址。我们就输入IP，在 header 里面输入叫host。好，名称是什么？ 3W 点一个 zone pot . com，我们来 get it。是不是old？我反复尝试几下，放宽大一点，放大一点，看得更清晰一些。好，已经最大了是吧？怎么样尝试都是 old 就证明什么？就证明我们前面说的 PPT 里面的那张图已经实现了100%，达到了什么老节点？下面我们要调整一下这个策略。


我们要用另外的一个代码，我们还是用 IDEA 打开。我们看一下第二步实现什么？某些用户的负载转换，还是 ingress 命名不变，还是对应原来前面叫 gray release ingress。我们尝试什么？对其中的一个，整个 ingress 加一个annotation，就加一个注解。
这个注解说什么？这次我用了一种服务的匹配模式。我匹配到如果我的 key 是 full value，是以 bar 开头的，我就什么。我就会把所有压力压到 new endings 上。我现在有两个方向，一个方向是 old Nginx，还有一个方向是 new engines。但是根据最先匹配原则先，通常默认是匹配上面，也就是大概率我是会打到 old Nginx 的。小概率的触发条件一定要是 key 是负 value 是以 bar 开头的。这个时候我们会什么？不光以 8 开头，而且是什么要以刀的结尾，也就是8，所以以 full 等于8。这种情况下的应用，我们才能用什么打到我们的 new endings？我们来试一下嘴巴放大，太大了。


好 Cooper Ctrl apply 杠 f 我们前面的 great 已经生效了，看看效果是不是立马显示出来。我们回到界面上看一下，点 gray release 点进去看下面有很多什么，有很多变化，看到吗？前面是创建，现在是生效。如果状态是什么，是这种正常的规则已经能显示出来，它有一定的概率会达到什么。 new endings 有一定概率会达到 o endings。证明什么已经生效了。我们拿 Postman 来实测一下。来看一看我们在没有特殊什么 value 的情况下应该是什么。始终显示old，我要加一个key， value 叫four，等于bar。我们看会有什么结果。没有翻测，我们显示了new，而且你反复测，结果都是一致的。这就是什么金丝雀发布。里面什么把小麻雀放到了矿藏的所在地，经过了实测，发现麻雀没死。我们可以逐步什么切换压力，把它把工人一个安排过来。什么访问新的应用了，我们回到代码。我们下一步直接跳过了10%。什么？我们直接进入50%，还是跟刚刚差不多。在 annotation 里面，我们注解一下，这里有个叫 service wait。我们再回过去看一下。上次写的叫 service mess，是用匹配规则的，这次我们用权重改变叫 service weight。其实这个就是什么？这就是整个服务的 API 的名称。下面就是它子服务叫 service weight。标注一下这里百分比了，它们加起来是100%，中间的值随便控制。


new years 你可以先写10，后面9020805050。我们直接测试一下5050。下面的内容都不变对吧？也正常情况下，什么是会打造这两个不同的service？概率完全由这里掌控。有一半的概率是老的应用返回old，一半的概率是新的应用返回new。我们切换回这里了，重新打开公职命令堂。我们用 Cooper Ctrl apply 杠 gray 2 进行一半的压测，很快的完成了。我们看一下是不是现在是一半的概率在 new 了。我们打开postman，这次不需要什么再有什么 for bar 这种测试了，已经是全面向用户敞开了。你就把它勾掉。


我们看看第一次是old，第二次也是old。因为什么我们刚刚机的键频率比较快的情况下有缓存。给我们稍微讲了一会，再来还是old。两三次都是old，拗了。我们再等一会，又是尿了还是new，又出现old，是不是差不多一半 old 跟 new 差不多。


如果你用什么 collection run 来跑，中间间隔时间稍微长一点可以看出来，可能大部分概率是 old 和 new 的交替进行，或者中间有了连续两三次old，两个连续两三次new，总体来看是比较平均的。这就是通过ingress。说白了， ingress 其实就是个engines，什么负载均衡， 7 层的，把不同的压力压到不同的指向。我们可以采用什么？ PPT 里面讲到的这种，什么根据 header 的这种方式，也可以采用什么？我们完全根据负载数量的方式控制，粒度很细，也就是完全不受后面容器数量的影响。


如果你不用ingress，只是用传统的什么我们新的蓝绿发布的套路，增加容器的数量，微超容器的数量你没法控制到 5% 10% 15% 这种精细的操作。所以通过ingress，通过容器化技术，通过一些类似于服务、网格等等的技术，可以很方便地实现什么 cicd 的全自动化。我们的云发布有很多的灵活性，下一个章节我们重点会聊一聊什么云监控，大家敬请期待。

