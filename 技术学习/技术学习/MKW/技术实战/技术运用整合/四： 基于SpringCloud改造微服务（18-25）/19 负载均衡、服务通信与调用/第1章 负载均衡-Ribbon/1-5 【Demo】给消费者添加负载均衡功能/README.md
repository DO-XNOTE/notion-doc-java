---
title: 1-5 【Demo】给消费者添加负载均衡功能
---

# 1-5 【Demo】给消费者添加负载均衡功能

[image](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/7435ceea-326e-4061-aa0a-d5256ef6f0a1/SCR-20240718-dukf.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XUMK24VC%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T225607Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIHE34R4VbtMuwyb9b%2BMN5G2Ze7x8liYUQzuf45tQ8QHRAiEAyOZI2km75kdYcqKSt%2BsQyvV7AV9yY7tzTH6ox0NLKvQqiAQIxv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDN7ETRnrjQMHlS5UjSrcA9aVh2tFQPPDEDYT2RrGzSVoq92z8G98XkKdUdgi9kFQvx1PQhT9L3t97x1qWTdZ5mdGJy8T0CU7qHhElqt%2FT3%2F4tztOlXRavqUesSeqfMJISiHmmP3upnpgwv3N6KLHCXUVsdrAokVq3uGDyL797xgFhDK7BgbAjnRZu0bvlVemWvdz5Soa5EQCcllc5p6So%2BgzbsJTW33jh41B7FNGhdZcO87gKl3mfqbVUZP5YMJeBlMPEvE%2FDsQQdU5mq903n5KIpmd2Q97PYXu0HJ3Qex3v1%2FgTCpTXc5biYaMa011QMQi85b1nfUIM8AnMFJrVBHrvA0C6NiFkpuVFoandQbvxBhkeKr%2FvV%2BvRUJIZo3HvFnGUTNFD%2FPpWMoMZsjWMjUVgHvW2Gw9IkFS6omAkiViLqiQnLEPtfDaPjmlY1cYQoO3OLFkDxQi3ZdloxcMr6qisPa%2FyH%2FUzRCOrOpr3vP4lSCVlo%2B9o6EBd9OLTsHW3Kk%2B%2BBEBTshiZBos3%2BD3DXZSlgL4Lhq1GlYyrt4Q4%2B1yAN9iY1G4Q1ScO60ABeVFmXkcr6eQG48do2TIWLhCB4PW9iG4aEIrwmHXvGcgqCDhspZRNDZI6c8wvY7w1mZH5qDKz9i7LLQdYd2jlMIu6%2F9IGOqUB2tzSNd00sWi5ZdXOSTuyp%2B40zSFzon%2BtQqZh8OKTf2aJxS7Yb584iYtHOeaHxHANxW%2FHXmH%2BCf6pxYiSUykaSiGX18vZ%2FZd4z8z%2BY0LHP%2BKRrnPa7Z1wCppFZRqYMqdv4mIYOG3XGSIZTQmdvwgTZmAmRk3%2BynO%2B54cggh161e1m%2FyFbb0hsPZ0raEjHyCxzPgkFvGjnaYFPdo%2FrPy5sIqGkXmsu&X-Amz-Signature=276faa8345805b84bbcce5fc242b47b8b30d2cfed0fca60448ef680720b1b151&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

[image](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/275951ba-ab11-464b-82d5-baf572b636e2/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XUMK24VC%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T225607Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIHE34R4VbtMuwyb9b%2BMN5G2Ze7x8liYUQzuf45tQ8QHRAiEAyOZI2km75kdYcqKSt%2BsQyvV7AV9yY7tzTH6ox0NLKvQqiAQIxv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDN7ETRnrjQMHlS5UjSrcA9aVh2tFQPPDEDYT2RrGzSVoq92z8G98XkKdUdgi9kFQvx1PQhT9L3t97x1qWTdZ5mdGJy8T0CU7qHhElqt%2FT3%2F4tztOlXRavqUesSeqfMJISiHmmP3upnpgwv3N6KLHCXUVsdrAokVq3uGDyL797xgFhDK7BgbAjnRZu0bvlVemWvdz5Soa5EQCcllc5p6So%2BgzbsJTW33jh41B7FNGhdZcO87gKl3mfqbVUZP5YMJeBlMPEvE%2FDsQQdU5mq903n5KIpmd2Q97PYXu0HJ3Qex3v1%2FgTCpTXc5biYaMa011QMQi85b1nfUIM8AnMFJrVBHrvA0C6NiFkpuVFoandQbvxBhkeKr%2FvV%2BvRUJIZo3HvFnGUTNFD%2FPpWMoMZsjWMjUVgHvW2Gw9IkFS6omAkiViLqiQnLEPtfDaPjmlY1cYQoO3OLFkDxQi3ZdloxcMr6qisPa%2FyH%2FUzRCOrOpr3vP4lSCVlo%2B9o6EBd9OLTsHW3Kk%2B%2BBEBTshiZBos3%2BD3DXZSlgL4Lhq1GlYyrt4Q4%2B1yAN9iY1G4Q1ScO60ABeVFmXkcr6eQG48do2TIWLhCB4PW9iG4aEIrwmHXvGcgqCDhspZRNDZI6c8wvY7w1mZH5qDKz9i7LLQdYd2jlMIu6%2F9IGOqUB2tzSNd00sWi5ZdXOSTuyp%2B40zSFzon%2BtQqZh8OKTf2aJxS7Yb584iYtHOeaHxHANxW%2FHXmH%2BCf6pxYiSUykaSiGX18vZ%2FZd4z8z%2BY0LHP%2BKRrnPa7Z1wCppFZRqYMqdv4mIYOG3XGSIZTQmdvwgTZmAmRk3%2BynO%2B54cggh161e1m%2FyFbb0hsPZ0raEjHyCxzPgkFvGjnaYFPdo%2FrPy5sIqGkXmsu&X-Amz-Signature=a0e96b65519c9fd73f8ef5980c6ac0f2a7b23f9c8929bed2324bd148e89c2161&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

hello 慕课网的各位同学们大家好，又到了这一期的 demo 环节了。那么在 demo 之前，老师想跟大家分享一下最近的一个心理感悟小体验是什么呢？我发现自从我开始做视频培训以后，这个每天的时间过得就非常的快，眼睛一闭一睁。不知不觉又到了下个月发工资的时候了。每个月过得都很快。回想以前带团队，那每天的事情是什么？大清早六七点钟就起来开会，晚上也有杂七杂八的事情，平时就是甩锅撕逼，各种各样的烦心事。每天过得神烦，这个日子过得特别慢，生命感觉特别长。那这说明什么？说明我喜欢做这些培训的事情，你做自己喜欢的事情，你就会感觉到这个时光飞逝。那同学们如果在学习中也有这种感觉，那就说明这就是你自己喜欢的事情了。

[image](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/ceb6d3c4-abd2-43ea-aa40-c8273c37f426/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XUMK24VC%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T225607Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIHE34R4VbtMuwyb9b%2BMN5G2Ze7x8liYUQzuf45tQ8QHRAiEAyOZI2km75kdYcqKSt%2BsQyvV7AV9yY7tzTH6ox0NLKvQqiAQIxv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDN7ETRnrjQMHlS5UjSrcA9aVh2tFQPPDEDYT2RrGzSVoq92z8G98XkKdUdgi9kFQvx1PQhT9L3t97x1qWTdZ5mdGJy8T0CU7qHhElqt%2FT3%2F4tztOlXRavqUesSeqfMJISiHmmP3upnpgwv3N6KLHCXUVsdrAokVq3uGDyL797xgFhDK7BgbAjnRZu0bvlVemWvdz5Soa5EQCcllc5p6So%2BgzbsJTW33jh41B7FNGhdZcO87gKl3mfqbVUZP5YMJeBlMPEvE%2FDsQQdU5mq903n5KIpmd2Q97PYXu0HJ3Qex3v1%2FgTCpTXc5biYaMa011QMQi85b1nfUIM8AnMFJrVBHrvA0C6NiFkpuVFoandQbvxBhkeKr%2FvV%2BvRUJIZo3HvFnGUTNFD%2FPpWMoMZsjWMjUVgHvW2Gw9IkFS6omAkiViLqiQnLEPtfDaPjmlY1cYQoO3OLFkDxQi3ZdloxcMr6qisPa%2FyH%2FUzRCOrOpr3vP4lSCVlo%2B9o6EBd9OLTsHW3Kk%2B%2BBEBTshiZBos3%2BD3DXZSlgL4Lhq1GlYyrt4Q4%2B1yAN9iY1G4Q1ScO60ABeVFmXkcr6eQG48do2TIWLhCB4PW9iG4aEIrwmHXvGcgqCDhspZRNDZI6c8wvY7w1mZH5qDKz9i7LLQdYd2jlMIu6%2F9IGOqUB2tzSNd00sWi5ZdXOSTuyp%2B40zSFzon%2BtQqZh8OKTf2aJxS7Yb584iYtHOeaHxHANxW%2FHXmH%2BCf6pxYiSUykaSiGX18vZ%2FZd4z8z%2BY0LHP%2BKRrnPa7Z1wCppFZRqYMqdv4mIYOG3XGSIZTQmdvwgTZmAmRk3%2BynO%2B54cggh161e1m%2FyFbb0hsPZ0raEjHyCxzPgkFvGjnaYFPdo%2FrPy5sIqGkXmsu&X-Amz-Signature=f9d30041bb58fbd53faa73c715f4804f6a47059df10e9fbbed9d954b0cc60d9c&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

OK 分享完了，那我们进入正题这一节学什么内容呢？我们来试着，给 consumer 加上负载均衡的功能。那这一节的主要内容都有什么？我们来看一下。第一个，我们创建一个新的 module 是什么？ Ribbon consumer. OK 在这个 module 里面，我们要添加依赖特殊的日本依赖，然后使用本地的服务调用谁呢？调用 eureka client 调用我们 eureka 中的服务提供者。


第三点，启动多个 eureka client 因为大家要验证负载均衡功能，对不对？那如果只有一个服务提供者，那肯定验证不出来了。我们这里启动多个服务提供者，看一看这个负载均衡是不是会生效。那最后一点，我们把负载均衡策略应用到全局或者应用到指定的服务。


那看完了提纲，大家就抄起家伙准备到主场 into J 里面开拔，每天扣订一小时，健康工作 50 年。好，到了主场大家开始创建项目。打开 eureka 的项目，我们看到这里已经有五个节点啦，那我们就给瑞本创建一个新的文件夹，不用瑞卡的文件夹了。这里点击项目右键创建一个什么 directory directory 名字叫做ribbon，右下角这个更新提示审法，总是跳出来关掉它。


好，瑞本创建完了以后，在项目中我们创建一个新的 module 这个毛九还是没问类型。点击 next artifact 是什么？是叫瑞本 consumer 中间加个斜杠，和之前创建友瑞卡项目的模式是一样的。这个 module name 是 ribbon consumer 大家也可以使用一些 spring cloud 的插件帮大家一键创建出这个项目来。


但是我总觉得用手工创建的印象更深刻。对不对？就像手工做出来的什么面包、馒头，总是比机械做出来的好吃对不对？ OK 点击 finish 好，那这里看到 ribbon 目录下已经有了一个 ribbon consumer 接下来做什么？接下来是不是给 palm 里面加依赖了？好，我们看一下都需要加哪些依赖，其中有部分依赖我们可以从 eureka 这里把它 copy 过来， copy 哪些内容呢？我们看第一个就是要把 ereca client 这个依赖 copy 过来。接着 boot 的两个依赖，同样的也是把它一并 copy 过来。好，这三个 dependency 我们把它放到 ribbon consumer 里。


好勒，那接下来需不需要引入一个新的瑞本依赖，那我们找一个这里放在这个空白的地方。它的 group ID 是什么？是 or 级点 spring framework 跟上面一样的也是 spring frame cloud 下面的。 OK 它的 artifact 我们把上面的给 copy 下来，这段非常非常长的 Netflix copy 下来。 OK 后面是杠瑞本。好，这就没了。


那这四个应用，dependency就是我们本节章节需要用到的所有 dependency 了。这里我们上面再给它加一个 packaging 给它指定成这，然后把 name 给它写上，这样编译起来更友好一些。这部分内容完了以后，我们接下来要添加一个入口类，是不是先创建一个 folder 它的 package 是 com.imock then spring clot 好，这个入口类我就不费劲写了，我们从前面把 eureka consumer application 给它 copy 过来。好，拷贝过来以后做一点小改动。主要是改什么呢？改这个 name class name 我们把它改成 ribbon consumer application 点击 refactor 好，这个名字已经改过来了，但然后这个 template 我们待会要对它动一动手脚，所以我们这里先把它给删除掉。


好，那么这个入口类只有一个 static 的闷方法，这就够了。接下来我们去写 controllercontroller 这里同样的，在 spring cloud 这个包下，你有一个 class 起名叫 controller 好创建好了，收起小桌板，把屏幕放大， controller 的头非常简单，也是一个大家非常熟悉的 rest controller 的 annotation 把它给挂上去。


接下来方法我们和前面有瑞卡 consumer 在方法上面是相似的，但是有那么一点点不同。这里我们调用其中的一个什么方法 get string 的那个方法。 say hi 对不对？好？ say hi 他的方法头依然是 get mapping 路径，我们也同样的写成 say hi 因为它的端口号待会启动起来的服务端口号不一样，所以说我们这个路径可以跟 U 瑞卡的服务提供者和服务消费者保持一样的路径。 say hi 完了以后，大家看怎么来 return 怎么来去调用 eureka 的服务提供者。


这里有那么一点区别了，IM声明一个 private rest template 这个引用进来。好嘞，同样的把这个 rest template 用 out wide 的注进来。那前面我们知道在开发友瑞卡应用的时候同样也是使用的 rest template 发送请求，对不对？那我们在 man 方法中是不是声明了一个自定义的 rest template bin 直接 new 了一个 bin 那我们这里没有定义行吗？当然不行了，待会儿下一步我就来大家定义一个 rest template 看如何将 ribbon 和 rest template 结合起来一起使用。


OK 那下面我们调用远程方法的方式就很简单了。在这之前我来先带大家复习一下之前有瑞卡中是怎么调用的。这里是 eurika 的 consumer 我们看到它是通过一个 low the balancer client 选择了一个指定的服务，对不对？他借助这个 load balancer 的组件帮我们选择出了一个服务。那这个服务的 host 和服务的 port 我们都在代码层指定好了，也就是说这个 target 就是我要访问的服务对不对？那它有固定的 IP 地址，固定的端口。


那在我们瑞本项目里面是不是也这样做呢？不是的，瑞奔项目很简化，我们既然引入了负载均衡组件，那也就不必要在我们的代码层面实现获取负载均衡节点的逻辑了。那他怎么做啊？那大家来看他直接调用 rest template get for object 那后面是什么呢？是 TTP 冒号，我直接把 eureka client 这个地址打上去，后面还需不需要端口呢？不需要直接是服务路径。 Say hi. 那它的返回值是什么？我们把它折一个行，返回值就是 string.class 这就完成了。是不是？没错，直接 return 你看到吗？这里既不用指定 IP 地址，也不用指定端口，而是直接应用服务名。那它背后是怎么找到对应的服务和对应的端口呢？我们这里接下来就要定义这个 rest template 了，他就是机关所在，瑞本的精华好，走到 application 慢方法里留一块空地，我要大展身手了。


我们 public 返回一个 rest template 给它起名叫template ，这个方法名就叫 template return new rest template eh 这是不是看起来似曾相识啊？我们再到有瑞卡这里看一下，怎么感觉看起来这么眼熟啊？咦你看是不是，这尤瑞也是这样声明的。一个 bin 那这不是一模一样的吗？没什么区别。瑞文跑哪去了？别急，别急，客官稍安勿躁，我们再回过来，再到 ribbon consumer 里看，给他挂一个 bin 是不是长得跟友尔卡一模一样。


接下来妙笔生花，画龙点睛画蛇。不添足。这里一个 at at 一个新的 annotation 是什么呢？ load balanced 5 这个就是什么呢？大家可以看出来是个新的注解对不对？它就是给什么呢？给这个 rest template 添加了 load balance 功能。这是不是很神奇啊？你添加了这个注解以后，我就不用在代码里面给 rest template 传入一个具体的服务器地址，我只用给他传入一个服务名，由他自己来给我们怎么样来给我们选择一个具体的服务。


Ok.好了，那代码层面我们已经搞定了，接下来大家知道要做什么吗？配置对不对？ OK 我们接下来去配置项里面看一看。这里在 ribbon consumer 的 resources 文件夹下，我们创建一个文件 application.practice 和前面几个应用一样，你收起小桌板。这里第一步大家知道吧，应该很熟悉了。创建项目的名称对不对？ spring [application.name](http://application.name/) name 是什么？ raban 杠 consumer 第二步，我们给它指定一个 server 的 pot 我想前面我们定义的是 3 万，那这里给它定义31,000。好了，这样跟前面不会发生重复。


下面一步，要指定有瑞卡的服务注册中心地址，有 reca.client.serviceurl 有的同学这里把这个 service 打成了 server UL 结果发现注册不上对不对？大家这里注意一下，这个叫 service uil 。 Default zone. 那这里是 HTTP local host 还是 2 万 gang eurekaokay 那后面就暂时先不配置了，我们接下来尝试着把这些所有应用启动起来，看负载均衡配置是不是生效。


第一个，找到 eureka server 好吧， eureka server 的 main 函数启动起来。第二步我们要启动两个服务提供者对不对？尤瑞卡克兰特要启动两次。好，我们这里先启动第一次，在尤瑞卡克兰特里面同样找到闷函数，把它启动起来。在启动第二次的时候，这个端口号要改一下对不对？因为我们这里是用多少 3 万端口号启动了第一次。那启动第二次的时候要把它改成30,001，这样的话跟前面不会发生冲突。


好嘞，那我们接着把它启动第二次，这样你就会看到我们通过一个 intelligi 里面的应用启动了两个不同的 instance 好，这里看到已经启动成功了，前面的两个服务也都启动成功了。那么接下来要启动谁了呢？启动 ribbon 了对不对？我们打开 ribbon consumer 在它的闷函数里，用正常的 run 方法不用 debug 把它启动起来。好， spring 看到成功一半往下走。已经启动成功了。接下来我们做什么呢？做两件事情。第一个到注册中心上看一看，这三个应用是不是都已经在注册中心上可以显示出来了。接下来就通过 postman 去调用 ribbon consumer 看它在后面会不会轮询的调用两个不同的 eureka client 来验证负载均衡功能。好我们先到浏览器上看一下。



好，下面到了尤瑞卡的注册中心，大家看到这里 instance 还是空的，我们刷新一下。看到这里出现了两个服务，第一个服务是 eureka client 来看它的 available zones 是两个对不对？那 status 后面也跟着两个服务节点，那说明我们前面启动了两个都已经成功的连接上了注册中心。那下一个是 ribbon 的 consumerok 接下来我们就调用一下 ribbon 的 consumer 看它是怎么连接 eurika client 的。我们启动 postman 这个 local host 后面端口号是31,000，我们把它的 post 方法改成 get 最后的 URL 是 say hi 我们现在发送一下，这里已经有返回了，这个字有点小，跟大家念一下，返回的是 this is a30,001。


那 30,001 大家还有印象吗？是响应端的，它的端口号对不对？那说明我们响应这个请求的是谁？是端口号为 30,001 的 eureka client 服务，对不对？那我们再发一下看到吗？这个端口号变成了 3 万，那就是另一个 eureka client 响应了这个服务。那每次点每次点它都会有不同的服务来响应。你看这一下又是 3 万，这一点又成了30,001。所以这证明了什么呢？证明了我们代码层。
我们来回看一下 eureka consumer 代码层的这句 load balanced 那这个注解已经生效了，如果没有它的注解，那我的 rest template 实际上是不知道该怎么去做 load balanced 那这一节的内容就到这里快要结束了，我来做一个下期预告。


好了，那接下来在图文章节中，我们将要学习 ribbon 的负载均衡策略。大家可以会看到很多种不同的负载均衡策略，以及它背后的流程都是什么。并且我们还会告诉大家如何根据具体的业务以及具体的模型来对负载均衡策略进行选择。 OK 那负载均衡策略定义在哪里？我剧透的好像多了一点，它在 application properties 里面，我们可以给一个应用一个 application name 指定一个整体的负载均衡策略，甚至全局的负载均衡策略，也可以对每个不同的服务指定负载均衡策略。那接下来这就是后面的内容了。


其实我觉得 ribbon 是整个 spring cloud 生态系统中相对功能来说比较单一，然后短小精悍的组件，言下之意就是说它怎么样比较简单，对不对？那我这里甚至建议同学怎么做呢？我们通过自己的方式八仙过海，各显神通。我们做一个跟瑞本类似功能的组件，当然更进一步，如果可以把它集成到 spring cloud 这个生态系统中，那便最好不过了，这就是同学们自己研发的迷你版的瑞本。那这种学习方式有点像古代学书法时候的临摹对不对？看到一个好的字帖，然后我们学习它的笔法走势，然后把它尝试着融入到自己的书法当中。


那我们这里通过对瑞本的学习以及后面的源码阅读环节，了解了瑞本的核心思想以后，我们看能不能融入到自己的知识体系当中，构建一个跟瑞本类似的迷你瑞本，这对大家学习开源项目以及积累相应的架构方面、软件设计方面的经验是非常有帮助的。 OK 那这一节的内容就到这里结束了，同学们，我们下期再见。




