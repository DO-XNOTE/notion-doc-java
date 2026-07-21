---
title: 2-5  【Demo】Gateway急速落地-创建默认路由规则
---

# 2-5  【Demo】Gateway急速落地-创建默认路由规则

[image](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/16c620c4-07b4-46c0-bdda-1f6579faebf4/SCR-20240721-dtvn.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YS4IVGHI%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T225733Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIAj%2FSN1KLH00AKQnmO0udDKXozEv3qgekh4eFeKvrdgSAiAH1fmGzMJppSaJYyVkGHfjJu7bRmK%2BEKENAn3S6E0vcCqIBAjG%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMz5i7iogFtCdn6aftKtwDNzbyQYwkdG0DGCVY6ZwPK3W56ai3CbH48quqesJy4PcqoClVA9kRswtx63cnJBWI83Nq5NyBO5Jz5zXkNhc8uIAH%2F6UodnLba2tghqpumxGCbonyLvRYT0kz5sDLlpR02gJuo7sly3t84AFUmCq0yG8czQ9Czy23RUhX2YeRUHz6Z%2FvvylBsoUMhqlb7jN2Wybd9jJ9QKpSsRCq1TuQWCEmFbpH377FAirmFVNFVnaXjgNLw2FKgc8WP3oyQho6vzEFs4JnPvqXRWntfbd9UN8NC3FEppjAUXSRUdNzXfRo8ULCOj0Azn24Dvxv%2BVkAilZWh3j4AqdSgJSJZ%2F5TVZIviz9KM9i7rzw5UplTBEy%2B4i6HFM0%2FWVmAYJ8D6sZWHiIHDxYzrVeNfM79sWjle0P6Lm6PdLGW4qy0Jw2L15ZcMkfkcnnvO3xBsO167ixZo2yg0ZRKO5uJLPeXA7aUo5zba8zDxMUAGpsuAJZ0S8YxR07cxEZOKwOC5rQsgSm61ro54V9A6i8S7dkPZjTtst4drI8TVVY%2Bn2YbSz%2BP8%2BZL0Jl3sDlGrIc6x%2Fy98B1NSSuDFKUOaz1GNXC9%2Fo4cYtj5kwK6yxAyDKBEt8t%2Fl0ldM425gtp%2BKrdsYTfkwtbj%2F0gY6pgE7lTl6zfpo29XbMBZQvWMZ5MWHB0GaB%2Bf5t%2BudFVbX77%2By3PucyuanswkEVNGZzML9NFiXwufPgi49Z5F35y0zmMzrJ2NKm3o5OrLgBGHRQMpOLtHDFMHl0aX%2BOd0rklZHlTY64JWMp9HX4hCGmLh9xz8BGOJwAolq6urzIZ7u2WyM3bj2Y%2BF5kVoqSiwriJjd1OcBsL00%2FYVgkgcCOfw8hj4IvhWt&X-Amz-Signature=a6dff11833812e6720cd310aad822660650f28b8b58cea599a21a40589289942&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

[image](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/e0d86d2a-c2d5-4733-b9c3-f0e7ec4b5c9e/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YS4IVGHI%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T225733Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIAj%2FSN1KLH00AKQnmO0udDKXozEv3qgekh4eFeKvrdgSAiAH1fmGzMJppSaJYyVkGHfjJu7bRmK%2BEKENAn3S6E0vcCqIBAjG%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMz5i7iogFtCdn6aftKtwDNzbyQYwkdG0DGCVY6ZwPK3W56ai3CbH48quqesJy4PcqoClVA9kRswtx63cnJBWI83Nq5NyBO5Jz5zXkNhc8uIAH%2F6UodnLba2tghqpumxGCbonyLvRYT0kz5sDLlpR02gJuo7sly3t84AFUmCq0yG8czQ9Czy23RUhX2YeRUHz6Z%2FvvylBsoUMhqlb7jN2Wybd9jJ9QKpSsRCq1TuQWCEmFbpH377FAirmFVNFVnaXjgNLw2FKgc8WP3oyQho6vzEFs4JnPvqXRWntfbd9UN8NC3FEppjAUXSRUdNzXfRo8ULCOj0Azn24Dvxv%2BVkAilZWh3j4AqdSgJSJZ%2F5TVZIviz9KM9i7rzw5UplTBEy%2B4i6HFM0%2FWVmAYJ8D6sZWHiIHDxYzrVeNfM79sWjle0P6Lm6PdLGW4qy0Jw2L15ZcMkfkcnnvO3xBsO167ixZo2yg0ZRKO5uJLPeXA7aUo5zba8zDxMUAGpsuAJZ0S8YxR07cxEZOKwOC5rQsgSm61ro54V9A6i8S7dkPZjTtst4drI8TVVY%2Bn2YbSz%2BP8%2BZL0Jl3sDlGrIc6x%2Fy98B1NSSuDFKUOaz1GNXC9%2Fo4cYtj5kwK6yxAyDKBEt8t%2Fl0ldM425gtp%2BKrdsYTfkwtbj%2F0gY6pgE7lTl6zfpo29XbMBZQvWMZ5MWHB0GaB%2Bf5t%2BudFVbX77%2By3PucyuanswkEVNGZzML9NFiXwufPgi49Z5F35y0zmMzrJ2NKm3o5OrLgBGHRQMpOLtHDFMHl0aX%2BOd0rklZHlTY64JWMp9HX4hCGmLh9xz8BGOJwAolq6urzIZ7u2WyM3bj2Y%2BF5kVoqSiwriJjd1OcBsL00%2FYVgkgcCOfw8hj4IvhWt&X-Amz-Signature=bd92162ac87f31ba3ecf75a03952454af580fe31cbb02f550506af93ce92f131&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

[image](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/09fcd83b-fae2-4fc0-b32f-4df31bd75db7/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YS4IVGHI%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T225733Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIAj%2FSN1KLH00AKQnmO0udDKXozEv3qgekh4eFeKvrdgSAiAH1fmGzMJppSaJYyVkGHfjJu7bRmK%2BEKENAn3S6E0vcCqIBAjG%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMz5i7iogFtCdn6aftKtwDNzbyQYwkdG0DGCVY6ZwPK3W56ai3CbH48quqesJy4PcqoClVA9kRswtx63cnJBWI83Nq5NyBO5Jz5zXkNhc8uIAH%2F6UodnLba2tghqpumxGCbonyLvRYT0kz5sDLlpR02gJuo7sly3t84AFUmCq0yG8czQ9Czy23RUhX2YeRUHz6Z%2FvvylBsoUMhqlb7jN2Wybd9jJ9QKpSsRCq1TuQWCEmFbpH377FAirmFVNFVnaXjgNLw2FKgc8WP3oyQho6vzEFs4JnPvqXRWntfbd9UN8NC3FEppjAUXSRUdNzXfRo8ULCOj0Azn24Dvxv%2BVkAilZWh3j4AqdSgJSJZ%2F5TVZIviz9KM9i7rzw5UplTBEy%2B4i6HFM0%2FWVmAYJ8D6sZWHiIHDxYzrVeNfM79sWjle0P6Lm6PdLGW4qy0Jw2L15ZcMkfkcnnvO3xBsO167ixZo2yg0ZRKO5uJLPeXA7aUo5zba8zDxMUAGpsuAJZ0S8YxR07cxEZOKwOC5rQsgSm61ro54V9A6i8S7dkPZjTtst4drI8TVVY%2Bn2YbSz%2BP8%2BZL0Jl3sDlGrIc6x%2Fy98B1NSSuDFKUOaz1GNXC9%2Fo4cYtj5kwK6yxAyDKBEt8t%2Fl0ldM425gtp%2BKrdsYTfkwtbj%2F0gY6pgE7lTl6zfpo29XbMBZQvWMZ5MWHB0GaB%2Bf5t%2BudFVbX77%2By3PucyuanswkEVNGZzML9NFiXwufPgi49Z5F35y0zmMzrJ2NKm3o5OrLgBGHRQMpOLtHDFMHl0aX%2BOd0rklZHlTY64JWMp9HX4hCGmLh9xz8BGOJwAolq6urzIZ7u2WyM3bj2Y%2BF5kVoqSiwriJjd1OcBsL00%2FYVgkgcCOfw8hj4IvhWt&X-Amz-Signature=e55cb51546b3f454b41f9b5529d0c992ab03823f674095b63920ebcc7d57b83a&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

嗨慕课网的各位同学们，大家好，这一节我们来进行 gateway 章节中第一个动手环节叫 gateway 的极速落地。这个极速我要跟大家解释一下什么叫极速落地。它的意思是说在这一节的 demo 当中，大家要秉承好读书，不求甚解，知其然，但是不要知其所以然的精神，咱先把这个 gateway 的 demo 从头到尾给它快速搭建起来。这里面我们不会深入细枝末节，跟大家介绍每一个技术点。同学们如果看到不明白或者不熟悉的点，咱先把这个问题给藏起来，等到后面的章节再一一揭晓。 OK 秉承咱互联网行业超快猛的精神，咱看看这一节如何来做这个极速落地。

[image](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/8a5948b2-9615-446d-9c68-675fe2b1b9de/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YS4IVGHI%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T225733Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIAj%2FSN1KLH00AKQnmO0udDKXozEv3qgekh4eFeKvrdgSAiAH1fmGzMJppSaJYyVkGHfjJu7bRmK%2BEKENAn3S6E0vcCqIBAjG%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMz5i7iogFtCdn6aftKtwDNzbyQYwkdG0DGCVY6ZwPK3W56ai3CbH48quqesJy4PcqoClVA9kRswtx63cnJBWI83Nq5NyBO5Jz5zXkNhc8uIAH%2F6UodnLba2tghqpumxGCbonyLvRYT0kz5sDLlpR02gJuo7sly3t84AFUmCq0yG8czQ9Czy23RUhX2YeRUHz6Z%2FvvylBsoUMhqlb7jN2Wybd9jJ9QKpSsRCq1TuQWCEmFbpH377FAirmFVNFVnaXjgNLw2FKgc8WP3oyQho6vzEFs4JnPvqXRWntfbd9UN8NC3FEppjAUXSRUdNzXfRo8ULCOj0Azn24Dvxv%2BVkAilZWh3j4AqdSgJSJZ%2F5TVZIviz9KM9i7rzw5UplTBEy%2B4i6HFM0%2FWVmAYJ8D6sZWHiIHDxYzrVeNfM79sWjle0P6Lm6PdLGW4qy0Jw2L15ZcMkfkcnnvO3xBsO167ixZo2yg0ZRKO5uJLPeXA7aUo5zba8zDxMUAGpsuAJZ0S8YxR07cxEZOKwOC5rQsgSm61ro54V9A6i8S7dkPZjTtst4drI8TVVY%2Bn2YbSz%2BP8%2BZL0Jl3sDlGrIc6x%2Fy98B1NSSuDFKUOaz1GNXC9%2Fo4cYtj5kwK6yxAyDKBEt8t%2Fl0ldM425gtp%2BKrdsYTfkwtbj%2F0gY6pgE7lTl6zfpo29XbMBZQvWMZ5MWHB0GaB%2Bf5t%2BudFVbX77%2By3PucyuanswkEVNGZzML9NFiXwufPgi49Z5F35y0zmMzrJ2NKm3o5OrLgBGHRQMpOLtHDFMHl0aX%2BOd0rklZHlTY64JWMp9HX4hCGmLh9xz8BGOJwAolq6urzIZ7u2WyM3bj2Y%2BF5kVoqSiwriJjd1OcBsL00%2FYVgkgcCOfw8hj4IvhWt&X-Amz-Signature=4062eca0f8f1a3cdb6a283d7c2317f09953fd8a1506cc1577022da81ba141a37&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

第一个环节，我们先创建一个新的项目叫 gateway sample 然后把必要的依赖引入进去，这一步非常简单。接下来的第二个环节，我们要通过 eureka 的服务发现机制自动创建路由，不用任何手动配置。我们的 gateway 组件会为 eurika 上所有注册的服务。创建一个自动的路由规则是不是很神奇呢？那第三个环节更神奇了，我们通过 activator 实现动态的路由功能。什么叫动态路由功能？就是说在你 gateway 这个网关层运行期间，我可以动态的向里面添加新的路由规则。


好敌人还有 5 秒抵达战场，同学们抄起家伙 intelligi 走起编程是我快乐 996 是我的福报。
又到了享受福报的时候了，我们先来创建一个 directory 一个文件夹，给它起名叫 gatewaygateway 里弟兄不多，咱先来创建这个老大哥，你有一个新的毛九，然后他的 artifact 咱前面说过了，叫 gateway 一个横杠，然后 sample OK next 毛球 name 和前面保持一致，把它扔到哪个文件夹下。咱们刚创建的 gateway 好三二一起好勒。这里要给他添加 dependency 啦，咱来看看都有哪些 dependency 需要我们添加一个大的 dependencies 节点，先给它添加进来，剩下的 copy paste 就可以。那我们找一个 copy 不走样的目标，就从 config 这里找好了，咱找到 config 下面的 config client 从它的 palm 里面偷点东西进来，要偷哪些东西呢？同学们看到这一个dependency ， spring boot starter web 咱以前每一个猫九都使用了它，但是在 gateway 里面我们要把它踢出家门。为什么呢？待会儿再向大家解释。



gateway 实际上是一个非常特殊的存在，它并不依赖于 spring boot starter web 组件，它跟 spring cloud 下面的其他组件这一点是很大的不同。好，那咱把其他的 dependence 给 copy 过来都有哪些？这里有两个可以供我们 copy 的，一个是 act reader 一个是 eureka client 好，有多少是多少？先把这两个给拿过来。除了这两个以外，还有没有其他的 dependency 啊？那当然有了，它是 gateway 自己的 dependency group ID 也依然是偶尔几点。


spring framework 再点 cloud OK 它的 artifact 是 spring 杠 cloud 再杠 starter 后面是跟 gateway OK 那除了这三个组件以外，我这里还想额外引入一个组件，这个组件等后面的章节大家会有用到是什么呢？是咱利用网关层进行限流所必要的一个组件。它是 Redis okay 在前面分布式章节是不是已经学到过了 Redis 和 Lua 脚本的限流。那这里我们再来提供一个新的切入角度，咱可以利用 spring cloud 的 gateway 网关来进行限流。


这个 dependency 在这一节当中并不会用到，不过是为以后的小节做一个准备。它的 group ID 是 org spring framework.foot can you spring framework 大家有没有觉得 spring 简直可以在整个 Java 界一统江湖，真的这是武林盟主。遥想十几年前各种框架群雄逐鹿，层出不穷的时代，到如今依然活跃在这个一线开发市场，只有 spend 这一家了。


好说这么多，还没给大家介绍他的 artifact ID 那咱引入的这一个也是 spring boot 下面的一个 Redis 插件，把它给加进来，就可以在 spring 的配置文件当中配置 Redis 的连接串等等。 OK 那最后给它这里留个到此一游，把 packaging jar 给它加上。好到这里我们的 pump 文件就已经配置完成了。
来创建启动方法。好，我们找到刚才咱创建好的 gateway sample 项目 Java 文件夹里创建那个大家非常熟悉的 com.imock.spend cloud 这一个包。然后创建一个闷方法，这个闷方法我们可就不从其他地方 copy 过来了，因为它会长得跟其他的组件中的启动方法稍微有那么点不同，则给它起名叫 gateway application 走起好又可以打这串行云流水的 public static void main 方法了。但是在这个闷方法里面，它这个启动方式可以有那么一点不同了，我们给它换一个姿势启动它叫 spring application.run 好，把这个类名拉进来，紧接着参数传入进去。好了，然后接下来给他戴高帽子了。
第一个高帽当然是友瑞卡，因为咱刚才引入了友瑞卡的依赖，所以我们还要基于 eureka 的服务发现创建自动的路由规则。那么这里给它做 enable discovery client 加上来。第二顶高帽子是 spring boat application 暂且咱就给他带这两点，等后面做权限验证的时候，还会陆续的加入 fin 还有其他的扫包路径 component scan 等等之类的。


注解。好，那么一切准备妥当，接下来咱就可以去配置文件了。在 resources 方法下，我们创建一个新的文件，它的名称叫 application.yaml 这里有些内容咱是可以从其他地方 copy 过来的。比如说我们到前面的 config 章节里，把有瑞卡还有 active rate 的方法的配置文件给它 copy 过来，从这里的 management 节点一直 copy 到尤瑞卡节点，换回到咱的 YAML 文件里来。剩下的部分我们就要自食其力来手打了。


好先手卤。第一个也就是最重要的 spring 的名称，你这个项目叫什么名字自报家门，它是 spring application 下面跟的是 name 我们给它起名就叫 gateway service 。紧接着名称这里的节点就不同了，大家看它是在 cloud 下面有一个叫做 gateway 的新的节点。好， gateway 下面都有什么内容呢？咱这里不写多先写本章中最需要用到的部分。那我们前面说过了，要利用服务发现机制来自动创建路由规则。所以下面的这个节点名自然是跟 eureka 有那么点相关，它叫 discovery okay 那在 discovery 下面还有一个叫 locator 好看到的 locator 大家应该心中有数了。它的意思就是说通过 discovery 的服务发现，把你的服务在 eureka 注册中心上面注册好的所有服务通通的给它定位到。那究竟要怎么定位到这个问题，咱交给 git 位来处理就好了。


咱这里只用把这个自动创建服务路由的开关给它打开好了，所以接下来的一个节点它的名称就叫 enable 它的值我们给它加入一个 trueok 到这里就结束了，非常非常简单。然后咱在下面再给它指定一个 server port 前面几个组件都是61,000，咱这里给他起一个叫65,000。好了。好，到这里基本上配置就结束了，大家看是不是非常简单呢？那是因为大部分的路由规则、什么断言，还有过滤器，我通都没有配置。咱这里只是使用的最简单的配置方式。那么到这里其实还有一个属性需要大家配置的，我先卖个关子，咱待会先瞧一眼它自动创建的路由规则都是什么样子，然后回过头来再配置这个属性，这样印象更深刻。


好，咱接下来就可以测试如何通过尤瑞卡拉取自动路由了。 OK 我们这里需要先启动几个应用。第一个应用首当其冲的 eurika 都要先在线，对不对？我们把 eurika server 给它启动起来，在启动的过程中我们还要启动几个服务，那我们就挑选分 client 好了，把这个分 client 启动几次呢？启动两次为什么要启动两次？大家能猜到吗？因为我们要验证一个负载均衡。



同学们可能想了，咱压根就没有配置负载均衡，怎么会实现负载均衡功能呢？这个不用担心，通通都是 gateway 它自动给我们配置好的人家创建的自动路由规则是有三包服务的。好，我们把分 client 的 server port 从 40,005 再改到40,006，然后再把它启动一次。在分克兰德启动的同时，咱要把 gateway 也给启动起来，找到 gateway application 的 main 函数，直接把它跑起来。万事俱备了，我们看看 gateway 已经开始加载，很快的全部跑起来了。


好，那接下来咱第一件事儿先到浏览器里面看一下。有瑞卡注册中心，打开浏览器，我们这里刷新一下。好，刷新一下。大家看到这里已经注册了两个服务，分别是 gateway service 还有分 client 那咱先要看一下 gateway service 如何创建这些路由规则。好，我们在旁边新开一个窗口，打上 local host 65,000。那有什么办法可以查看当前的 gateway 都有哪些路由规则？我们不妨借助于 activator 接口来做这件事儿。


咱先打开 actuator 界面，这里就是全部 expose 出来的端点。那在这些端点我们也叫 endpoints 里面，大家可以搜索这样一个 keyword gateway 那咱看到这里有一个新的endpoint ，就是由 gateway 组件创建出来的。咱不光可以通过这个端点来查看当前有哪些路由规则，同时也可以利用它添加修改删除路由规则。好，那我们把这个 URL 复制下来，然后打开。咦怎么是个404。 Not found. 那是因为这暴露出来的只是一个 end point 它后面还要有路径的，咱给它添加一个 roots 路径。



这个 roots 的含义就是让 gateway 告诉大家它现在都注册了哪些路由规则。相信大部分同学都知道路由规则是什么含义对吧？它就是说你的服务请求要通过 gateway 把它转发到一个后台的特定服务。那这个转发的逻辑什么样的 request 转发到哪个服务？这里面的逻辑我们就把它叫做路由规则。


好，我们回车这里显示的乱七八糟的 JSON 字符串，实际上就是它当前所有的路由规则，我们把它复制下来，在另一个窗口打开一个 Jason for matter 对它进行一下格式化，这样大家看的比较清楚。好，这里是经过格式化的路由规则，大家看到它实际上是一个列表，我们把它缩放进来。可以看到这个列表中有两个元素，这两个元素分别代表谁呢？我们先打开第一个元素看一下。相信同学们在这里一定看到了好多名词，不知道是什么含义对不对？没关系，老师反正也不会告诉大家的。


在后面的小节中，我可以向大家详细解释咱这里怎么样就知其然，但是不要知其所以然。好了，我们在这里主要看这么一个属性往下走。好。看到这里没有 uriuri 是什么，它后面跟的是 LB 冒号 thin clientthin client 是不是？就是咱刚才在 eurika 注册中心看到的一个注册上的application ，那 LB 是什么意思啊？ load balance 也就是说当我们的访问请求抵达 gateway 的时候，它会替我们做这个负载均衡。


那我们接下来看第二个元素，打开第二个元素往下滑，同样的看到 URI 我们这里看到它的 application name 是 service gatewayok 它实际上这里的 element 是和 eurika 注册中心里面已经注册上的服务名称一一对应的，你有几个服务，我的 gateway 就会自动的创建路由规则。那他创建的路由规则实际上有两部分，这两部分分别是一个断言，还有一个过滤器。咱先不去看这个 filter 和断言分别代表什么含义，我们来尝试直观的调用一把 gateway 看它如何做转发。那我们这里把分 client 给 copy 下来，就是这一段我们 copy 下来，然后到 postman 里。在 postman 我们向 local host 65,000，也就是我们的 gateway 发送一个请求。这个请求后面的 URL 是谁呢？就是咱刚才 copy 下来的分 client 然后在分 client 里调用哪个服务呢？大家还记得里面有个叫 say hi 的服务对不对？ OK 我们使用 get 方法来调用这个服务。


点击 send 好，同学们看到这里已经有一个返回结果了，他说 this is the 40,005，那我们再点击一次，看结果会不会有什么不同。点击完了之后，它变成了40,006，再点击一下又变回了40,005，然后又变回了40,006。这说明咱在刚才的路由规则里看到的这句话， LB 已经生效了，它会通过负载均衡进行转发。然后它的转发规则是什么？它的路由规则就是匹配你路径中的第一个位置，也就是我们当前这个分 client 所处的位置。如果这个位置你给出的路径它可以匹配上任何一个已经在尤瑞卡服务中心注册上的 application 那我们的 gateway 就会把当前的用户请求转发到对应的 service 里，是不是非常简单呢？那大家有没有注意到，在这个路径中分 client 是大写。是不是看起来有点那么突兀，有点那么奇怪，咱把它改成小写试一下。


点击 send 咦发现他报了一个 404 的错误 not found 难道路径从大写改到小写就不起作用了吗？这是为什么？我们不妨到注册中心上来瞧一眼。
好切换到注册中心，大家看到在注册中心里，咱注册上的 application name 这里就是大写对不对？所以我们的 gateway 就很无脑的，这个大写直接应用到了路由规则中。但是按照咱的开发习惯，包括用户习惯是不是小写更加的适合一些。那怎么办呢？这里就要回到我前面跟大家说的有一个没有配置的属性了，把这个没有配置上的属性给它添加进来，咱先把 gateway 给它关掉。那设置了这个属性以后，咱就能通过小写的路径来访问对应的服务了。这个属性名它落在哪里呢？就落在 enable 的同级，也就是 locator 下面，它的名称叫 lower caselowercase 就是小写的意思，然后一个杠 service 再杠 ID 它的值是 trueok 那设置好了这个属性以后，我们把 gateway 给它启动起来，然后重新切换到 postman 里，再尝试调用一下服务。这里是小写，我们点击 send 发现可以正常的得到返回数据了。



OK 那改成小写可以咱再改回到大写会不会依然起作用呢？同学们想多了，咱做人不能这样的反复无常。对不对？咱要么小写就小写，要么大写就大写。好了，我们配置了前面那个属性以后，如果你再通过大写访问，看到这里，它就会是 404 了。所以咱就不要期待两全其美的方法了。


当然了，如果大家手动创建路由规则，是可以既接收大写又接收小写的，这都没问题。对，它自动创建的路由规则咱就不必如此苛求了，所以就采用通通小写的方式就可以了。那做完这个测试以后，咱前面提到了 activator 可以在运行期动态的修改路由以及添加新的路由规则。所以 gateway 的路由配置真的是非常非常灵活。那咱接下来看一下如何给 git way 添加一个新的路由，然后使之生效。那我这里已经创建好了一个 postman 的项目，我们点开它。这里添加路由规则的路径也是在 activator 里面，后面跟着 gateway 然后一个斜杠 roots 和咱前面查看所有 gateway 中的路由列表的 URL 是一样的，但是这里还要在后面再添加一个属性这个属性它是作为你的访问路径中的一部分，它的含义是 root ID 就是当前添加的这个路由规则。它的唯一 ID 是什么？我们可以给它起个名字就叫 dynamic 好了，因为咱是动态添加的，就叫dynamic。 Ok. 然后这里面就是我们添加的路由规则了，大家可能看着会比较头晕，对不对，我这里跟大家稍加解释一下，咱先把这一段内容 copy 下来，放到浏览器里面放大来看好，我们切到浏览器中看。这里它的路由规则包含了四个部分的内容。从下往上看好了。


第一个是 order 生效的顺位，咱不管它下面一个 URI 意思是当你这个路由规则被匹配上了以后，它将转发到 eurika 中的分 client 服务。同时利用负载均衡策略，因为前面配置了 lbok 我们再往上看，这个 predicts 和 filter 是相互作用的，predicts是匹配你的访问路径的而 filter 是对你的访问路径或者是你的参数等等做一些过滤和处理。那在稍后的章节中，我将详细跟大家一一介绍都有哪些常用的 filter 并且有哪些常用断言可以来使用？那我们把这个动态路由就发送到 gateway 中，大家注意它发送的时候是用的 post 形式，然后 header 里面是接收的。


Jason 好，我们准备 123 走，你发送完成以后，咱看到它的返回参数是空的，但是它的返回的 HT TB status 是201，201的意思是 created 也就是说你的这个创建路由规则的请求已经被处理成功了。那我们现在来调用一下 gateway 中的路由列表，看看这个路由请求是不是被添加进去了。我们点击 send 最下面同学们看到这里有一个 root ID 这就是咱添加的新路由规则。 OK 那接下来我们尝试着访问这个路由规则，看它会不会生效。这个路由规则中关于地址匹配的断言是这样说的，当你的访问请求后面是以 dynamic 开头的，那么通通都会匹配上这个路由规则。好，我们这里继续尝试向 gateway 发送一个新的请求。前面咱是发送到分 client 的 say hi 我们把分 client 替换成 dynamic 然后同样是 get 方法再调用一次走这里已经获得了正确的结果，说明咱刚才添加的动态路由已经生效了。


其实咱不光可以动态的添加新路由，也可以在运行期更改或者是删除一个路由。那我这里再跟大家演示一下如何删除一个路由还是到刚才添加路由的这个托斯曼方法里，这个访问路径咱保持不变，然后把 pose 的请求改到 delete 说明咱的这套方法是完全遵循 rest 接口规范的。那咱的 body 可以删除啦，不需要 body 了。那他怎么知道该删除哪个路由规则呢？就是在路径中的这个参数。


最后一个路径名称 dynamic 这就是咱刚才创建的路由规则的 ID 还记得吗？我们这时候发送请求好，发送完之后服务器返回了200。那么我们回到路由列表中看一看这个路由还在不在好，我们发送一个请求，然后看看返回的结果中只有两个路由规则了。这两个是为有瑞卡自动创建的路由规则，咱刚刚新添加的那个路由已经被删除掉了。如果大家在尝试着继续调用这个路由请求，不出意外的，咱得到了一个 404 not found 这个路由规则再也不会生效了。 OK 那刚才我们尝试着添加了一个路由请求，然后删除了一个路由，还剩一个修改。对不对？这一部分就留给同学们当练手的小作业了。


OK 那到这里，咱这一节就结束了，我来简单的跟大家回顾一下。这节当中我们创建了一个 gateway 模块，这个模块所依赖的一个核心的组件是我们在 dependency 里面添加的 gateway 组件。然后 gateway 组件的核心配置是放在了 application YAML 当中。那在 cloud 节点下面，这个 gateway 属性里我们配置了它可以根据 ureka 的服务发现为已经注册好的服务，自动创建路由规则，并且还可以通过 lowercase service ID 这个属性决定路由规则中的路径是匹配大写还是小写。


另外咱开放了所有 act rate 的 endpoints 然后在页面或者是 post man 当中可以去查看所有的当前已经激活的路由规则。我们又尝试通过艾克特瑞特的接口为当前的服务网关在运行器动态的添加了一个路由，然后又做了删除操作。那后面还给同学们留了一手就是修改操作了，大家可以在自己的本地搭建起这个很简单的小 demo 来尝试一下。


那本节内容到此就全部结束了。在接下来的一小节里，我将跟大家介绍本章中的某些遗留问题，比如说断言是如何来生效的，这里面最重要的一个断言就是地址匹配。那么在下一个小节当中，再跟大家深入介绍如何通过 pass 断言来把访问请求转发到对应的服务上。 OK 同学们，那我们下一小节再见。



