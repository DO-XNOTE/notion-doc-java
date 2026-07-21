---
title: 2-16 【Docker技术落地实战】部署微服务-4
---

# 2-16 【Docker技术落地实战】部署微服务-4

[image](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/fb66d6b5-813d-4377-8fbb-d0825fb031ad/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663ELQWAOJ%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T225928Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQC8wKbWRKq0bVdMaw5glQ2tAxqRMA80hV2XnLyZ%2Bl2NggIhAIWuZ4orhKXhxifwbrB%2BwRQllD7YQ%2FDOoYuDhTYsr2tjKogECMb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgwFMGheTn94R%2FJkRnsq3AOe8ABmhEY9ymvh3k9BM3AWIev3lVG2znp%2Fe19U1Z2KPqNGVCuFDTy3kEuHr3GZDDXsbuCz0vJge6SxsIIBhS%2Bwbkqnu9pEmN3iOJ5KAh7SRdkidrNyZhoj5uQI5xD4%2FoejYwbWqvScv4hGor4OM1QGkMmcqJgrueZUm%2FOtHWCy7kgr07XhND64r2gWB22u%2F%2FnqItn7EY%2BxBoXV1pMhFhQsWV%2B7jnTMRhiUJJpww4%2FEnawL%2BXWryN1c1XJCy7exASeZSZlmA4yM8cIdCO5ABMx%2BpCWC09qgEW587ncv%2Fa4B39zXhcbEOQPSvbEkShFYV6uAbV61aLNUg4cwI%2BjkLlUsNuh%2FGzW7Cai%2FHdXlLQA%2FfBlYJ8RjLeh2%2F6QdNn93OXbZDPKiZiWSgr24K%2B5SsX0AdoYmyEYV0a7BB6XIyFIVFTQGco2YnhUh5eFIGQnkSxaaAzs47d%2BRfUzaG8AawLRdyEYjTE03f0tkm8BhPGyP5ObtndS6nz4FpKGyUkXLzYkin6Ve25%2FgIpKleLkedTDgJ3Yi43JWJB52wgJ5thN1SdAE34DBybMjJc%2BL19jmS75M7suwc5%2B0wyYGoQOKYVQCc7qw1%2Bx2gbhOErr4rG7SCZKvn4ngNUOex3ATATDCuP%2FSBjqkAZrdenRc7DwmsGYfZScY7u1yn%2BQ1AuN1BK9FMPb%2FayUgJ4IoekN0lsYXzsjjJiYWHFOwMHRN1EJoC6mSauTgjCWW%2BaIb4NGJ388gzLy%2Fdv57gPF65pxr3aOrSKftBS3mPTqVxP9BwwiWfeKQOPV1JY2mIrXS%2FVoB9JkLqAGeHxPesbUricBif2NsyVwuen07ZSBoTnKBkw6BEY2Z3G8p5vb6do9Y&X-Amz-Signature=4a58b2cc1ae1e20260b980fb11ba64566ea5afec331ccf9f84cae90a88e85d46&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

[image](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/46885e10-fc77-4be3-8bc2-758c8b0c5e55/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663ELQWAOJ%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T225928Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQC8wKbWRKq0bVdMaw5glQ2tAxqRMA80hV2XnLyZ%2Bl2NggIhAIWuZ4orhKXhxifwbrB%2BwRQllD7YQ%2FDOoYuDhTYsr2tjKogECMb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgwFMGheTn94R%2FJkRnsq3AOe8ABmhEY9ymvh3k9BM3AWIev3lVG2znp%2Fe19U1Z2KPqNGVCuFDTy3kEuHr3GZDDXsbuCz0vJge6SxsIIBhS%2Bwbkqnu9pEmN3iOJ5KAh7SRdkidrNyZhoj5uQI5xD4%2FoejYwbWqvScv4hGor4OM1QGkMmcqJgrueZUm%2FOtHWCy7kgr07XhND64r2gWB22u%2F%2FnqItn7EY%2BxBoXV1pMhFhQsWV%2B7jnTMRhiUJJpww4%2FEnawL%2BXWryN1c1XJCy7exASeZSZlmA4yM8cIdCO5ABMx%2BpCWC09qgEW587ncv%2Fa4B39zXhcbEOQPSvbEkShFYV6uAbV61aLNUg4cwI%2BjkLlUsNuh%2FGzW7Cai%2FHdXlLQA%2FfBlYJ8RjLeh2%2F6QdNn93OXbZDPKiZiWSgr24K%2B5SsX0AdoYmyEYV0a7BB6XIyFIVFTQGco2YnhUh5eFIGQnkSxaaAzs47d%2BRfUzaG8AawLRdyEYjTE03f0tkm8BhPGyP5ObtndS6nz4FpKGyUkXLzYkin6Ve25%2FgIpKleLkedTDgJ3Yi43JWJB52wgJ5thN1SdAE34DBybMjJc%2BL19jmS75M7suwc5%2B0wyYGoQOKYVQCc7qw1%2Bx2gbhOErr4rG7SCZKvn4ngNUOex3ATATDCuP%2FSBjqkAZrdenRc7DwmsGYfZScY7u1yn%2BQ1AuN1BK9FMPb%2FayUgJ4IoekN0lsYXzsjjJiYWHFOwMHRN1EJoC6mSauTgjCWW%2BaIb4NGJ388gzLy%2Fdv57gPF65pxr3aOrSKftBS3mPTqVxP9BwwiWfeKQOPV1JY2mIrXS%2FVoB9JkLqAGeHxPesbUricBif2NsyVwuen07ZSBoTnKBkw6BEY2Z3G8p5vb6do9Y&X-Amz-Signature=3a55b40fa6b34e23274a457f45a647afff8d07d0a5458c130b0d27986326d34c&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

上一节我们把 boss 还有 user 这两个 domain 的应用已经起来了，并且注册到了 eureka 那相信大家也已经把其他的比如像 itemordercut 甚至于search 、 payment 这些核心的 domain 的功能都已经拉起来了。那这个拉完以后，我们其实就该到什么前后端打通真正对外提供服务了。


那在前后端打通之前，首先要什么？在后端的所有应用，虽然你已经在用 URL 卡注册了，但有瑞卡这个注册的应用，只是在我们什么我们的这个子网内部进行什么互通的，也就是应用之间互通并不是给我们的浏览器从外网进行什么调用的，就通常从外网调用的时候，首先要什么把我们的 gateway 给配置好，这里我们首先要看一下 gateway 的配置。 gateway 配置完以后，我们还要把我们的数据库准备起来，因为像Redis ，像 rapid MQ 这些都不是非持久化的。但是我们的什么我们的 MySQL 或者说你用的是 merry DB 那它是需要持久化数据的。所以我们先要把那些持久化数据给准备起来，那之后才是什么前后端的完全的这个打通以及什么解决一些跨域问题。


好我们来看一下我们 spring cloud gateway 这一块是怎么处理的？ sprinkle gateway 其实我们打开整个这个代码里面有专门的一个在什么，也是在我们的 platform 底下有个 gateway 那这个之前半仙老师其实已经把它配置好了，我们打到 resource 底下。


application 羊毛旺大。那看一下这里面配一些什么内容呢？那首先它是配了一个什么，我们访问 Redis 那需要什么 IP 地址？那这里我已经替换成了是吧，我们的这个虚拟机这个我们的内网地址或者说是服务器的内网地址，大家可以如何炮制？端口不变，写着被子还选0，然后 password 注注掉我们不需要对不对？那 zip key 如果大家已经有的话也一样改成相关的 IP 地址和 URL 那再往下底下看。


这里就是关键点就是如果要支持跨域，首先要 allow each origin 到底 L 哪些呢？最关键是这里星号。因为有了这个星号，其实我们可以 L 各种各样的，那因为这是开发测试环境。那真正生产环境是我们不管是前端还是后端都会有一套 uil 那通常 uil 会在主域上是一致的，你只有子域不同。所以这个时候当我们的浏览器去渲染页面，从前端拿配置渲染页面 JS 拿 CSS 渲染完了以后，再靠后端阿贾克斯 call 的时候，因为它的 cookie 或者说它的整个域的跨域是主域不变，子域不同。


所以这个时候可以用什么点 Z 点什么就是点子域的方式进行什么允许允允许跨域，但是不是随便任何域都能允许跨，而是在同一个主域底下允许跨域，这是生产的处理方法。那我们因为是开发测试环境的，我们就星号，那使得后端允许前端来进行跨域。除此以外，我们要支持各种各样的 header 各种各样的 method 以及各种各样的这 header expose 这都是星星。


好，这些配置完以后，我们就看我们端口，我们端口是多少，20,004是我们 gateway 注册的一个端口，那它也是为什么注册在我们的 ureka 这个服务上，有 record 服务器的这个地址端口和其他的应用服务配置是完全一致的。同时底下的 instance 选择也是这样，就是选择什么以 IP 地址的形式，那这个 IP 地址就是我们内网的 IP 地址，然后对外暴露的这个端口也就是刚刚看到的 20004 


server.port 那这样注册完了以后，我们在有瑞卡上是可以发现我们这个什么我们这个 gate 为服务的。在这些改动完以后，我们一样我们是选择 food 的，直接找到那个 gateway 的服务。然后我们在 life cycle 里面选择这个没有install ，先修改再每本编译。


编译完了以后，我们会把这个包相关的这个 target 目录底下这个 gateway Snapshot 点价的包复制到我们的服务器。这里也是提前已经复制完成，我们等到那个腹肌看一下叫什么叫做 gateway 杠 1.0 点 Snapshot 点价包。那为了这个应用起来，我们一样我们要去修改这个 Doc phone 大家可以新建一个文件，然后在 Doc build 时候指定也可以直接去改之前的那个已经生成 Docker file 我们把这一段很长的一段文字全部替换掉，统一用 get away 这样的一个字符 global 形式进行替换。


替换完了以后保存，那它就会什么它是从 Java 的这个 base image 起，然后会把这个包复制到我们的新的这个 image 的镜像里，摆在它的根目录底下。然后当容器起来的时候就运行 Java 杠加，然后运行这个价包。好我们下一步就是 doctor build 杠 T 取 my gate away 作为 image 的名称，在当前环境找 doctor for 进行我们的什么镜像海报。


好，今天打包完了以后，我们用 doctor wrong 以 demo 的形式 wrong 以 demo 的形式端口刚刚看的是多少是 1004 来确认一遍端口号。 2004 它是一个平台性的，所以我们在这里统一规范是 1 是以应用的，1万是应用的，而平台性都是以 2 万卡在 2004 到我们什么容器的 2004 这样进行映射。那映射完了以后，我们再看一下我们要取什么样的名字，还是按照我们之前的命名规范，就取跟我们的 image 一样的叫 my gate away 这样一个容器名。那 imag 也是这样一个名称。好这样我们用 Docker PS 看一下是不是除了 rabiterredis mycq 以外，我们又起了一个最新的就是 my get away 之前那些 my user my auth 、 my config my registry 也还依然在运行。不过大家还起了其他的服务，还有更多的这样的容器一定跑起来。


这时候其实内存已经开始打量占用了，我们用 free 杠 M 这个命令看到什么以及有 5G 内存被占用掉了。如果大家所有应用都起来的情况下，已经可能达到 10g 以上了。所以我建议大家在 16g 内存的环境当中去运行，它 CPU 消耗不大，但是内存消耗非常之大，这样的微服务改造真正到压力上来的时候才是 CPU 开销的时候。但是容器的启动的过程当中已经会占用很多内存，所以内存一定要配的比较大。


好我们的这个 gateway 这样一个环境准备完毕了。那下一步就是刚刚说的什么数据库准备数据库我这里其实是已经从我们的这个 git 里面，在我们第一讲里已经有一个数据库的，基本上 schema 就 DDL 的这个 CQ 我已经下载下来，就是在 merry DB 里面进行修改的内容。但是我这里不会用 foodie shop 杠 DEV 刚刚已经聊到过了，就是 MySQL 对这个横杠知识差，可以通常用下划线来代替。所以我要先建一个叫腹地下划线 shop 下划线 DEV 这样一个数据库。那我先连进我们的整个这个 database 密码是 IMO OC 就是当时我起这个容器的时候选的。然后我再说一遍 databases 看一下到底有没有这个数据库没有时候我们跑一个命令，我们跑一个 create database 以后叫 food 下划线 shop 下划线 do 这样一个 database 然后 default 是我们的 set 叉 set 用 UTF 8，然后我们的 collate 用 UTF 8 下划线 general 下划线 CI 好不好？好这样 database 就好了。我们看一下说 databases 是不是已经有个叫 food 下划线 shop 下划线 David 了。那这个时候我们可以去 source 一下刚刚的，那个文件大家明还记得吗？遇到 food day shop can dev.seek message 刷锤子执行一个 sauce 好它是没有 data be selected 刚刚我忘了 use 了关系，所以等它报完报错结束了。
我刚忘了 use 再看一下名字。


Data bases use the foodie shop.
好，我们现在就什么正在往那个数据库里面灌大量的这个 DDL 的操作，把它那个相关的表以及相关的这些我们的肉都映射进去，稍微等一会会，当这个表和 row 全部音色完了以后，我们可以用 show tables 看一下对不对？这些表什么都已经灌进去。
好，灌完以后我们其实就可以什么，我们可以进入下一步，就是把前端起来了。那此前端一样的，我们在第一讲里面其实什么已经拿到了一份是吧我们的这个前端的代码。那把这个前端代码直接复制到了我的这个应用服务器上，它的目录叫什么叫 foodie show 我把它复制在了我们的这个当前目录看一下，我们根目录的 food cloud 这个主目录底下这个 food shops 目录，我们进到福利 shop 这个子目录去看一下，有这么多的这个基本文件，那这是原始下载下来的。那其中应该如果大家还记得第一讲内容，还记得 video [apps.gs](http://apps.gs/) 是需要去修改去指向我们的我们自己的后台，那这里就是这样把它给注册出来。


那这里其实我提前做了改动了，就是已经指向是吧我们的这个 IP 地址的公网 IP 地址，因为我们的前端代码是被我们的渲染在我们的浏览器上的，而浏览器去靠我们的后台的时候是没法靠到我们私网地址，所以只能通过什么阿里的公网地址，这里就是我已经提前把公共例子写在里面，大家就是注完以后就是取消掉这个注释对吧，然后把实际的当时服务器的公网地址，然后冒号 20004 这是什么地址就是刚刚 gateway 的对外端口号是吧，atv端的话就是 2.004 公网地址会自动映射到我们服务器的时候私网地址。因为而那个私网地址就是在我们刚刚启容器的时候，那个杠 P 虚拟机的私网地址，映射容器的私网地址的 2004 端口一一对应的，就这样就能真正的把 traffic 们打到我们的容器的 2004 端口上。下面玉我们建议允许把那个玉给做出来，选这个好其实关系不大。然后可以把原来的那些什么域再注释掉，也把原来的服务器的这个 server 注释掉。下面那些 payment shop 和 center 我们在演示中都不会采用，这无所谓好，弄完以后我们就可以来进行一个保存。这个时候我们相当于是前端代码的改动已经好了。前端代码改动完了以后，我们可以尝试着什么去用 endings 去起一下。那起 xing 是融四怎么样呢？也是这样。


Docker 对吧，我们 run 一个 engines 容器的服务，你这个 engines 容器的服务我们可以取名字 name 叫 my front 然后我们还是要映射一些端口。通常我们用 80 端口对外提供服务。因为很多时候一个服务器的 80 端口可能已经被占了，所以 anex default 容器端口是80。但是我们把它服务器端口 8080 来对外进行服务。同时什么我们要把当前的目录 root 底下的这种 fooding 底下的这个 food shop 这个目录映射到我们的这个服务器里面。所以用杠 V 如果大家还有问题，可以回过去看我容器的存储的这个磁盘卷这一张，看下怎么样进行目录映射。


通常我们一个 NGINX 服务起来的时候是 user share NGINX 底下的什么 HTML 这底下会有一个 index 的文件，以及其他相关的各种各样的 CSS 文件各种各样的我们的这个 GS 的文件。好吧，所以把主目录底下的这个 foodie shop 映射到 user share engines HTML 底下。那这样就可以当我们打开这个页面的时候，就会自动访问我们当前这个 fully shop 里叫做 index 文件了。


