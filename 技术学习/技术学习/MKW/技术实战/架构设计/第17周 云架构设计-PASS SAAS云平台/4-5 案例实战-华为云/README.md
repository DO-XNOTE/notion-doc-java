---
title: 4-5 案例实战-华为云
---

# 4-5 案例实战-华为云

[image](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/cad5569c-b273-47b9-a758-a2c41fc4dff7/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RPRCX53D%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T231132Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCbZsTx%2FGsramCkHFb7Qy8hw6Q2bdogHAkqv2YF1mY%2FzQIgJ5hbbfGFNZBEKFgdsdROFlhxFKeblHY2KQSE2ZS3Y%2FgqiAQIxv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDJXiEiA6V9BBwuzaBCrcA3ma%2BtnOKiOSDfA6z4mzoiNQdaLrOJ3NxAlMC4zZC55v0IdWalGAYGgcyJzmQD9C0szjEmutULiBMwJMVLIzanZitLx%2BlcTRB8cEKjGA%2F4F3VixwDrNbBmgtAX77hE0fSRYna%2BcWrbWrmZXHmLPN3fc%2BjzGnqjfgPCalyj28P2n1d6nBWNmwK1FyczKucu1zfGChKitMmXnyv2tHXkufIREnoRKbx2iEDblno2QEQFqKuSIZoSQ5ArKf2T85oBOHEsjgTNrD1NSvzuASsQbZxEmWpidDfMnRIxR%2BxCbLwoJvQmspfpUGKKR0W8iIausumv3Cefq27E%2FBB8oZ3lERuW%2BaG%2FQRg6f0tQpq7MqEvb1FsGFnTvRaMwyGB7PAfMRQjbLI4fdRRyf%2Fel6HaAjYGOLGzVrlGfWaj4oTLav8rarNAAVyEUke%2BBaB4A4CpZzqTGq3JiOMjAfkwELR6FRiCQtkn3qMdFr0e4rCSUziYPkt5IYypgLF7R4c7LX%2FiBt%2FoiDB%2BB5Q3%2FiVdEbR0TMBHeRYqNeBBuhYQkL0vNkvJGg1xED0HC%2BEk2DtahIuk7jMsE3JdsZE0MmZbmDjrOQHH8jY%2BvTZDQUDFiqmEBC7IPVZRiKOOFLvexhCzKYtMNq3%2F9IGOqUByODxhD49wHQ%2FvIexanC0SQaSW3cxPK01Z0gQjyAQv8PZ7%2F7ZKrY1rj3ijcSYKkGIgTQ%2BPMTxzUn2V6L6fd%2BznRaTptddKTXflL7k5FoUGSOMGV1bBYwP1xyUbioHo5eKQuvUCg43wqS3rJgivh8kgzgJl5UIOn6ktdDUO4lIksYuHodMdFnoFjLw%2FMq5eJcfJ0%2Fkrp3EfzSrjsr%2FyvrhpCiU%2FAUR&X-Amz-Signature=58a78af8de932deb27fa5e0abc05242010daec7425d5b0e28439279c82ca5a79&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

架起需求到落地的桥梁，构建 IT 新蓝图。我是张飞扬。好，上一章节我们聊了聊华为云的架构，它的特点，它的选型。这一节我们就在华为云上实战一下。

[image](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/d2a173cd-b14a-4cff-98bb-dfc64b30f558/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RPRCX53D%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T231132Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCbZsTx%2FGsramCkHFb7Qy8hw6Q2bdogHAkqv2YF1mY%2FzQIgJ5hbbfGFNZBEKFgdsdROFlhxFKeblHY2KQSE2ZS3Y%2FgqiAQIxv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDJXiEiA6V9BBwuzaBCrcA3ma%2BtnOKiOSDfA6z4mzoiNQdaLrOJ3NxAlMC4zZC55v0IdWalGAYGgcyJzmQD9C0szjEmutULiBMwJMVLIzanZitLx%2BlcTRB8cEKjGA%2F4F3VixwDrNbBmgtAX77hE0fSRYna%2BcWrbWrmZXHmLPN3fc%2BjzGnqjfgPCalyj28P2n1d6nBWNmwK1FyczKucu1zfGChKitMmXnyv2tHXkufIREnoRKbx2iEDblno2QEQFqKuSIZoSQ5ArKf2T85oBOHEsjgTNrD1NSvzuASsQbZxEmWpidDfMnRIxR%2BxCbLwoJvQmspfpUGKKR0W8iIausumv3Cefq27E%2FBB8oZ3lERuW%2BaG%2FQRg6f0tQpq7MqEvb1FsGFnTvRaMwyGB7PAfMRQjbLI4fdRRyf%2Fel6HaAjYGOLGzVrlGfWaj4oTLav8rarNAAVyEUke%2BBaB4A4CpZzqTGq3JiOMjAfkwELR6FRiCQtkn3qMdFr0e4rCSUziYPkt5IYypgLF7R4c7LX%2FiBt%2FoiDB%2BB5Q3%2FiVdEbR0TMBHeRYqNeBBuhYQkL0vNkvJGg1xED0HC%2BEk2DtahIuk7jMsE3JdsZE0MmZbmDjrOQHH8jY%2BvTZDQUDFiqmEBC7IPVZRiKOOFLvexhCzKYtMNq3%2F9IGOqUByODxhD49wHQ%2FvIexanC0SQaSW3cxPK01Z0gQjyAQv8PZ7%2F7ZKrY1rj3ijcSYKkGIgTQ%2BPMTxzUn2V6L6fd%2BznRaTptddKTXflL7k5FoUGSOMGV1bBYwP1xyUbioHo5eKQuvUCg43wqS3rJgivh8kgzgJl5UIOn6ktdDUO4lIksYuHodMdFnoFjLw%2FMq5eJcfJ0%2Fkrp3EfzSrjsr%2FyvrhpCiU%2FAUR&X-Amz-Signature=52c75ae24faecc44565fd96e0fd0741e8e1addb9e3256489ef819a5a011936c3&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

华为云其实什么注册和使用非常简单，我们可以拿个人的一些手机账号，或者是微信 QQ 账号等等进行一个快速的注册。注册完了以后，点击控制台，也就是华为 cloud . com 的 consul 控制台。点进去以后我们就可以什么登录它的主界面了。



主界面我们放大可以看到左侧什么是它几乎的主要的功能，都在这里一一列举。 ECS 就是我们标准的虚拟机 BMS 物理器，弹性伸缩，跟阿里云的 auto scaling group 是对应的。这里的 EVS 就是硬盘我们的快设备块，设备的备份也作为一个主力功能在这里展示了。


除此以外，网络 VPC ELB 就是阿里云的SLB，弹性申诉的 loader balance EIP 就是标准的弹性外网。 ip 地址 RDS 就是最常见的关系型数据库，通常后台是MySQL， Postgresql 等等。好这些功能，在其他的云平台可能还需要你进行实名验证，甚至有的云平台还需要你能够进行公司验证。但是在华为云还是相对方便的，你可以在一个简单登录的情况下就可以开始使用了。只有一些高级功能才需要完成实名认证。我们这里最简单的来弹性的弹一个我们标准的 ECS 好不好。好点击ECS，也就是准备创建我们的虚拟机，大家底层的技术栈应该已经很熟悉了是吧？基于 open stack 的什么 fusion sphere。好，我们点这里。购买弹性云服务器。在购买过程当中依然有很多选择，包年包月是很贵的对吧，几百块钱按需就便宜一些。而比较好的云平台都会提供什么竞价对吧？特别适合于开发测试的。


我跟你比价，我跟全球的华为用户比价。如果竞价过程当中我的价格不占优，我的资源就给你。如果我的价格占优，就归我。通常竞价模式能够把整个价格变得更加的便宜。我们看一看在上海的随机分配，我们看能不能挑出一个竞价模式，相对是非常便宜的。像这种竞享模式是不是很便宜，一小时只要 4 分钱对吧？你普通的竞价模式可能还是要 4 角钱，我这种模式诶，好便宜，要几分钱。这种情况下有可能的保障力度就很差。他说的你在这个小时，一旦你竞价不成功，他立马就把你资源回收了，也都不帮你备份，也不帮你做任何的数据的获得，系统的保障。


这个时候我们的测试开发是不是完全够了？下面挑机器，你可以挑个这种 2 C 4G 的photo，抛我们 spring boot 的小机器快速启动的应用，所以完全是够的。镜像里面可以选择一些，比如我们常见的Santos，大家熟悉的什么，比如是 8 对吧。是不是要进行主机的安全加固，通常选加固，即使我们开发测试环境，也建议有少量的加固。另外硬盘现在主流都是什么 SSD 是吧？所以不用太吝啬点。下一步是进行网络的配置和创建。他这也会说竞价模式有什么什么的缺点不用管，我们确认就好了，对吧。这里可能就要创建一个 v p c，它会给每个用户默认创建一个 v p c。 v p c 跟什么？跟阿里云，腾讯云一样的概念。也就是所有的 ip 地址段其实都可以冲突，没有关系，只要是你 VPC 内部是不冲突就可以了。每一个 VPC 是一个虚拟的网络，底层是通过大二层跟 BGP 三层的协议来共同实现。所以你的 BBC 就是你的。你在这里面可以定义自己的子网，自己的网段不会跟别人的有任何的冲突。


好，这里默认会有一个天生的子网。这个子网是什么？是幺幺九二点幺八点零下面的从 0 到 255 这样不等的 200 多个 ip 地址，它通常也够了。默认了一块网卡也可以。有的云平台是不支持多网卡的，比如像谷歌云等等。它只支持什么？每台虚拟机只允许一个网卡。但是华为云之前已经聊到过什么，华为云是很偏私有云的，在私有云环境，哪里有一台服务器只有一个网卡。所以在华为云里面，为了能够很好的对接私有云，甚至于公有云也向私有云妥协了，也变成了什么支持多网卡的这种场景。好，我们这里一个网卡就够了。


另外，入口和出口的安全策略是不是就是跟阿里云的安全组是一致的。对，不管是AWS，阿里云，甚至于是其他的各个云平台，其实都会有这种安全组。可能叫法不通，有的叫s、l，有的叫防火墙规则策略，有的就直接叫安全组弹性公网。这个通常我们都不建议对吧？不建议购买。通过什么s、l、 b 跟 net 对外提供服务。好，这样完成以后，我们点下一步进行高级配置。这里我们会选择比如用户名的密码，或者是密钥对，以及云备份什么亲和性等等，最终选择一个确认。当你全部确认完以后，我们自己输一个密码。好，点击一下不确认。好。当你确认完以后，就到了什么到了点击购买付钱的阶段了。


好，飞扬老师，除了我们前面的阿里云吧是单独付费的，后面的所有的这些尝试我们都会尝试采用一些免费策略来跟大家演示。这里也一样，我就不直接去创建服务器了，大家可以尝试一下创建服务器登录。其实管理的套路基本上跟什么跟阿里云都是完全神似的。大家都是什么 call 越不走样，源头都是 AWS 原因的，大家都是模仿它，超越它。好聊完了华为的计算，我们再来看一看华为的另外一个大的功能 RDS 云数据库。好，我们点击了RDS，进入了 RDS 界面，这里可以看到什么它能够进行，我们把这种指导性的内容关掉，它能够进行备份，还有一些标准模板，甚至于做一些数据的迁移、容灾归档等等的套路都可以在这里得到很好的服务。


另外，你也可以购买不同类型的数据库实例。通常我们还是买能选按需的就选按需是吧，不用去一次性付几百几千块钱。这里MySQL、Postgresql、 Microsoft SQL 都有。大家都说了诶，好像没有阿里云那么丰富，也不如腾讯云诶。是的，因为什么？因为是吧。华为云如果大家要用华为云，其实更偏一些通用解决方案。也就是我的这套解决方案是非常通用的。不管公有云、私有云都可以跑。不管你是华为云，甚至于迁移到其他云，或者从其他云迁过来都可以跑。


华为什么更强调每一个功能，进行精心的雕琢，从而降低它的成本，降低它的价格，而不是提供特别多的不同的这种 CQ 解决方案，这是它跟其它云平台思路的不同。它通过一些什么企业级的支持，企业级的咨询，增强整个云平台的优势。好，如果是选了一个Mycql，选一个 8. 0 单机模式的，相对比较便宜的单机模式，选一个 2 核 4G 内存。这样的形态。以后把网络都选好来默认网段，选好安全组。策略选好就可以。什么输好用户名密码就可以点击购买了。是不是价格也很便宜，一小时也就几角钱。好，大家如果想实验可以依次尝试。
这里其实跟其他的存储或者数据库套路是一样的，也有什么访问策略，也有网络。除此以外，在内网 EPC 里面可以进行方便的互通。有无？所以这种保护的方式可以什么？通过端口，通过安全策略，通过网段来保障我们的数据库不会被外网的黑客所访问到。大家思路都是类似的，只是实现的世界上略有不同而已。


好，聊完了数据库，聊完了计算，还要聊一聊什么网络。进到 VPC 网络网络里面看，左边是不大家非常熟悉的那些内容，整个网络叫VPC，下面有子网的概念，默认我们已经有了，叫做斜杠 24 对吧，具有 256 个地址段的这样一个子网。除此以外的路由表里面可以配置一些高级功能。如果大家是吧对网络技术不熟悉，通常不建议去修改路由表，因为这个时候会容易导致出现很大的问题，甚至于整个网络不可通。
除此以外，这两个内容基本上你是回避不了一个什么 net 网关，尤其是公网的 net 网关，它是服务出去的一个。出口的 ECS 服务，要访问外网，就可以通过 SNET 去访问，而不要在上面开公网地址，又贵又不安全，对吧？出口要走 net 进口，就是弹性负载均衡器。
在弹性负载均衡器里面，这里也能提供 4 层的，比如像是 TCP 的负载均衡器， UDP 的负载均衡器，以及 7 层的 HTTP 的负载均衡器。思路跟什么？跟阿里云的思路也非常类似于，一个是engines，一个是LVS。在这里，特别是 7 层这里的可以实现什么证书的管理，这就是证书的卸载。在内部走HTTP，在外面走 HTTPS 都可以。


好。除此以外，这里要聊一聊了我们的VPC，什么是可以互联的？所以通过这种对等互联，可以把两个 VPC 连接起来，变成多数据中心的单元化解决方案。同时我们还可以支持 VPN 去把我们的私有云和我们的公有云进行互联，也实现了多个 VPC 和多个数据机房的单元化解决方案。所以有很多的这种互联手段，比如这里云专线，这是一个昂贵的手段。当然也有什么也有像 i p sect、 v p n 这种便宜的手段等等。把这些所有的套路串联起来，形成了一个华为公有云私有云混合云的网络接入手段。


聊完了华为的网络，聊完了华为的数据库，也聊完了华为的服务器，是不是感觉出来云平台相对是轻量的，简单的，而且是很容易公有云、私有云对接的一套解决方案。这就是华为云的一个特点，快速上手，强大的咨询，完善的售后服务，帮助从无到有，从有到优，逐步从数据中心转移到云平台。好，聊完了华为云，我们下一节就来聊一聊度云，或者叫百度智能云，大家敬请期待。


