---
title: 3-31 【技术改造】电商系统集成Eureka - 订单中心-2 
---

# 3-31 【技术改造】电商系统集成Eureka - 订单中心-2 

[image](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/5d4f53de-7f57-4202-ab46-eef4192d57b3/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665FXKKLQH%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T225558Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDzBHedzDxFDQ1o1EmvUsoc5khus10UNqCQoGp4u8vymAIhAP7mToAj%2BGs6mtW%2F8uv1LT775oKG65ggtC30HbDCxsMjKogECMb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgxWkZPdz55cRY8iAFsq3AM5CgAmmLCU%2BumW2VTzpOfZgUxoCSV85ACaGHajdBh8XOrphqG%2Fcr4Ckxx8HOECkCYR8OHTMjRJ%2BLwVYK6sTdsxWVYf0fFxmNv72SHXDSgbUuOvg4tY%2FTggX5WLcR8POuuNHP15iUiT%2B7WEX6LeW9j5AmPkCfegPJHLXvt2%2FibQzfL8uLhjqMby%2BPzeaL1DwhLTb1jUiovk3bCandukaa1%2BvjAXC4cAk%2FsC4mCgj9fcUGPl24PqEkZN7VXGnDU3Ug9XmWezJCt88w2ZQOrt%2BsjprL7%2Ftkkb6UWFodTYB6W8vchQcwdP28ZoQflm1JbMfHAwVj9ues5PlKO7eM3uXMbMY9CYuFprHGX5qt7%2B68%2BQTvAWRZGT%2Biow0OF7jIPSsK90z8JylHz9pxbX2zrNwwvcCmL%2BAsmgrP43WAXZbm08erFnaTcvS9T6D2sWSx2XGFbmqZS8TnHWm24l3WyEq0eMln8q%2Fg0DuEnjV8RPKCOyXPnNb%2FP1XC2WvGQcLBxPdCJejRaE6NoYEvbQyw2a2QUvEtnhKU3HrZhpCV2HWbxYjEiDkVd9qFWjWNeA2ZDALFhUZhg6ygBSWX%2B7yGCNKuzxqhuXeAUNvkSrM1BjR4PuiCBILI9%2BkS3rEowXiDCHuP%2FSBjqkASWNlQmP0C5H5LO%2B%2FAqonQVza2czaQZ9CQsGc8TsusXmK%2FJsvp8xKOVMD1sHGCoudDfgKyt5Fi%2FomGSMQge2J52AzcDFODIoCiiU8ivVHHbSGsdCHURwV0CtPsPojaRhedtRCxl9P7MBT6d8mY3U9KRDJ852jySn%2BQgNlomC7%2BD7QbUYSTVphLMz%2FfCMhrygGTPNsSeP%2FSHyBtPzKwlJFPmjPgit&X-Amz-Signature=ab0f05f1155587779ae7649b54e24a4105eeeb603a49f6e397c6c745ea267077&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

[image](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/581e2cd7-b585-4322-b479-99e25e4f9586/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665FXKKLQH%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T225558Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDzBHedzDxFDQ1o1EmvUsoc5khus10UNqCQoGp4u8vymAIhAP7mToAj%2BGs6mtW%2F8uv1LT775oKG65ggtC30HbDCxsMjKogECMb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgxWkZPdz55cRY8iAFsq3AM5CgAmmLCU%2BumW2VTzpOfZgUxoCSV85ACaGHajdBh8XOrphqG%2Fcr4Ckxx8HOECkCYR8OHTMjRJ%2BLwVYK6sTdsxWVYf0fFxmNv72SHXDSgbUuOvg4tY%2FTggX5WLcR8POuuNHP15iUiT%2B7WEX6LeW9j5AmPkCfegPJHLXvt2%2FibQzfL8uLhjqMby%2BPzeaL1DwhLTb1jUiovk3bCandukaa1%2BvjAXC4cAk%2FsC4mCgj9fcUGPl24PqEkZN7VXGnDU3Ug9XmWezJCt88w2ZQOrt%2BsjprL7%2Ftkkb6UWFodTYB6W8vchQcwdP28ZoQflm1JbMfHAwVj9ues5PlKO7eM3uXMbMY9CYuFprHGX5qt7%2B68%2BQTvAWRZGT%2Biow0OF7jIPSsK90z8JylHz9pxbX2zrNwwvcCmL%2BAsmgrP43WAXZbm08erFnaTcvS9T6D2sWSx2XGFbmqZS8TnHWm24l3WyEq0eMln8q%2Fg0DuEnjV8RPKCOyXPnNb%2FP1XC2WvGQcLBxPdCJejRaE6NoYEvbQyw2a2QUvEtnhKU3HrZhpCV2HWbxYjEiDkVd9qFWjWNeA2ZDALFhUZhg6ygBSWX%2B7yGCNKuzxqhuXeAUNvkSrM1BjR4PuiCBILI9%2BkS3rEowXiDCHuP%2FSBjqkASWNlQmP0C5H5LO%2B%2FAqonQVza2czaQZ9CQsGc8TsusXmK%2FJsvp8xKOVMD1sHGCoudDfgKyt5Fi%2FomGSMQge2J52AzcDFODIoCiiU8ivVHHbSGsdCHURwV0CtPsPojaRhedtRCxl9P7MBT6d8mY3U9KRDJ852jySn%2BQgNlomC7%2BD7QbUYSTVphLMz%2FfCMhrygGTPNsSeP%2FSHyBtPzKwlJFPmjPgit&X-Amz-Signature=ade815d72e71f5e6e8e22503fad1e454e3da795f51e6794d986a1d7aa65c3f7c&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

ello 我们客网的各位同学们，大家好，那我们这里继续做订单中心的下半场改造，我们这里创建一个新的 module 咱这次要创建的是订单的服务层 foodie order service 那它跟之前的改造不一样，咱这里有一些比较麻烦的东西，等待会咱进到代码里面，带大家一起去看一下怎么来做改造。因为他要去交互的调用其他不同的微服务模块，我们把它放到 domain order 下面。这里有哪些 dependency 需要加入呢？来问变魔术一二三走，这里挨个看一下这些依赖都是什么。


第一个，依赖 order mapper 在订单中心的 mapper 层。那接下来的三个分别是用户服务接口、订单服务接口还有商品的接口。这里面其中用户接口和商品接口等到后面我们学习了分组件，咱就可以通过接口层发起服务间的调用。那么这里我们先预先的把它加入进来。那到后面咱这里看到还引入了一个特殊的依赖是什么？以瑞卡克莱恩特通常来讲它都是放在咱的 web 层。那咱 service 层这次为什么要引入它呢？因为咱这次也需要在订单中心的 service 层发起向服务中心和用户中心的调用。那这种情况下，我们就不得不把这个尤瑞卡给加入进来了。但是我这里要加一个注释，要学到分章节以后，要怎么办？就能把下面的依赖给它移除掉了，就可以把它删掉。因为份组件可以通过服务接口直接发起远程调用。但是如果没有份，我们只能通过优瑞卡和 load balancer 这种形式来发起调用。好我们把这个保存一下。那接下来去开始写代码了。那这里先创建一个 package come.imock.order service 后面跟谁呢？ IM PL 那在这个类下面，我们要移入 order service 好我们到 food DEV 当中把它给揪出来，就是你了，我们把它 copy 一下，再复制到刚才创建的文件夹下万里江山一片红。咱先不管它，然后紧接着在这个文件夹下面再创建一个叫 center 的文件夹，接着再去抓壮丁转到 foodie DEV 看 center 里面哪个跟 order 有关。


那 my order my comments 这两个有关对不对？把他们俩 copy 起来转移过来。那我们接下来就有一二三三个服务需要来改造了。那三位客官里面请毛巾，小手牌，请拿好，咱先来接待哪一个呢？就从这个开始。 my comments service 开始。好，我们点开它那大红灯笼高高挂，看到这么多错误，我们先把这些 import 的路径给它更正过来。这里已经全部更正完了。咱看到还有几个少量的红色报错，分别是它还有它。那我们从后往前开始处理。首先这一个你看它 over right 的报错说明怎么样，它从接口层已经移除掉了对不对？那它移到哪了？它已经移到了 item comments service 当中。所以我们这里已经不用管它了。


那么接下来往上看，同学们看到这个报错，items commons mapper 那它为什么引用不到呢？我们点开看一下这个类它在商品的领域模型当中，也就是说我们订单域不能直接去 touch 商品域的数据结构，那商品域的数据库访问不到，我们怎么办？很好办，我们把它注释掉，然后替换成什么呢？我们替换成远程方法调用。


前面咱们学到远程方法调用，我们需要两个组件，一个是 rest template 还有一个 load balancer 对不对？那我们接下来把这两个组件加入进来，这里留出几个空行，从你那 load balancer 我们用来找寻服务器地址，那 rest template 就用来发起服务的调用，这个只是临时的方案。
等后面学到分章节之后我们会怎么做改造份章节，这里我们就要改成 service 访问，那通过 item service 我们就可以直接访问到对方的远程服务调用。那然后我们滚到下面到这一距离这里怎么改造呢？咱先把它给注释掉，然后迁移一段代码。你看这段代码首先是从 client 这里拿取谁拿到 food item service 紧接着咱要拼出这个服务的请求。


咱先来看一下我们需要调用的 item comments mapper 它的服务是保存在哪里，它是在这里 item comments service 里面。我们到接口层看一下，这里就可以把它的这个路径给它 copy 过来。你看它的路径是 item comments API 并且后面跟着是什么。 Save comments. 那我们这里返回回来，把路径给它拼上。那接下来后面的一个是 save comments 好勒。那把这两个拼上之后，我们就可以直接发起调用了。对不对啊？那接下来我们怎么来发起这个调用啊？ rest template 它是一个 post 请求。那我不要返回值，它这个接口没有返回值，我直接就调用这个 post for location 好了，直接把 target 把这个名称改成 URL 把这个 URL 给传进去。然后后面咱需要传递的 map 那咱需要返回值吗？不需要什么，因为咱看到这个 item comments ，它是个 word 什么返回值都没有，直接传递给它就可以了。


好，那咱这个接口算是已经改造完成了，那咱接下来去改造下一个接口。好来有请下一位 my order service 那这一个接口看上去改造起来应该比较简单。你看它这里用到的 mapper 都是订单于自己的，所以不需要发起一个远程调用。对不对？我们这里先把这些 import 给它改正，好，321好。这里改正完了之后我们看还报错。


怎么回事 my order service 里面好像还有没有实现的方法？是 check user order 大家还对它有没有印象？这个方法以前是在 base controller 里的，因为这个 controller 会在很多个微服模块中共用，所以咱把这个跟订单中心强相关的业务从 ctrl 里剥离了出来，放到了这。那它的业务逻辑是什么？我们这边来写一下，很简单。


首先去验证你这个 order 是不是跟这个用户是一样的，是不是当前这个用户创建的呢？我们直接调用这里面的 query my order 这个接口，把 user ID 和 order ID 通通传入进去。然后再看如果 order 等于 0 等于不存在，那怎么样？我直接 return 一个 JSON result 和之前代码保持一致，给它返回一个 error message 叫什么呢？叫订单不存在感叹号加两个感叹号三个。那如果存在就 return 一个 JSON resultokok 你说 OK 我也 OK 大功告成。那这个类也改造好了。


好，前面已经送走了两位，那么先生最后一位里面请这个接口看起来有点麻烦了，你看又要调用什么 item center 又要调用 user center 的 API 那我们这里先把 import 给它改正。好三二一走改到这里咱先打住。好嘞，这里 import 能改的都改了，剩下不能改的。你看这里 address service 那它是 user domain 的对不对？然后这个剩下的是 item domain 的，但是我们不能把它引入进来。为什么呢？因为这两个现在只是接口，你把它引入进来了，那下面这个 auto wire 的它就会报错了，当前 spring 上下文中没有对应的 bin 来给你做 out wired 所以那我们怎么办呢？忍痛割爱，把你先给注释掉。然后我们后面 to do 加一个，学了 fin 再来拯救你，再来把下面的注释打开。那现在就先让你们委屈一下，待会儿我们还要用那种比较繁琐的方式，通过 load balancer 和 rest template 发起调用。


那我们接下来看这里又标红了，标红什么？你看 implemasters 那说明有个方法没实现，这个方法大家有印象吗？我们是不是更改了 place order 的方法，把这个方法签名给它改掉了，那我们会退回来。这个好办。我们这里不是有 shop part list 和 submit order BO 吗？这还不容易，我们把这个方法签名给它更正过来，把它改成 place order BO 然后把这两个对象怎么样呢？从 place order BO 里面拿出来，这是 get items 下面这个对象是谁呢？是 get order 那我们接着去更改剩下的部分，你看这里标红的都是什么 address service 那还有 item service 那都是外部的服务。


对不对？那我们这里打开面板，我们从前面已经改造好的 my common service 里面，把这两个 load balancer 和 rest template 给它 copy 过来，拷贝过来，放在哪里，放在 order service 这里。那接下来我们要做一件非常讨厌的事，怎么叫讨厌呢？你看这个方法，它从 64 行一直绵延了很多，已经绵延了接近 100 行了。那我们接下来要把这个长度给它翻了一翻，因为咱这种调用方式可谓是非常的复杂。

