---
title: 1-7 【Demo】Feign+Hystrix实现Fallback降级 
---

# 1-7 【Demo】Feign+Hystrix实现Fallback降级 

[image](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/b5f6b2b3-5d5a-4547-8fea-a8c6aee1c5a1/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UXRWRYRU%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T225637Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCRrrF7pFp%2FKqZ6GPkAW%2F5qb0IFqq%2B9rsYYRsEJDE3k%2BAIgTidjsygn9aYSuHpqiFI2zC2SWU%2BYZ7y4B20gOJg%2FNTMqiAQIxv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDLCX8a9B9%2FWpfoj%2BcSrcA7%2F95b%2F%2FJHZctCzJ9H%2FZmFi4glZwGv4ApuYZztBJYNsvq%2BVoEiGGTUgGJffRglqFza6Q5qX71YwSXQyeGn3rAiF9D9rH6rvJaciWIRMEa5eWzZGfbcECTninzAAXMsHyKGrE8ewlmjpQ6KZBIpc7AEk0%2FGB9FGwbtxVawC%2F2B0TE5RRgvCB3fYilz99eifXmQn0CrRKuHi9N5%2BLnN7SZHsbx1tKq2V2Gyoou%2B2pBMt9TVkF1xchHynl4EXHHEFP9lPKIjAts80G%2BE4Sgt2OfXGCbZpi%2FLktEzuziVOavLrtK2xRqA4ne3iI9ms3qucyKDNRta0jIP%2FDdXvZqaNo2H%2F1JC80f2T3v3TArGAB%2Fm45mBB2FC%2FdnyZof3vD3LISfmdsGTbDHAzcy5bu%2Ftn1DyK6H7t3rnEr%2Bjrq5kfwWOUNI1J6S4rWL8GmkCCmIahBFjhfo0%2ByrqBrji%2BPlpNycfnbKdtUKOQ6gAvGML6%2FQbTuHm6az8ZWdMu0hCUPx36q1e%2BZaYblDpptXS4mDgrvVudPU5HZ7i%2FEOdfdbfJNHS6U5qpNLGbs2IdgS6C824exZQxCe3APn4N4vZPRSia50Zi31YJuBD%2FWzsBUn%2Baya8f7n4mJ9BIOtNoUnWxwAMKC4%2F9IGOqUB0e20w1lbepd3F0b5iAp0ABRSPyr%2FkScIqQyp5%2FeKe2LjJWPcJ%2BTT7btmiGd7RNYkDvuwOQvwbsP2SOmnIa83rPDMDn8hTRHO59rekBGIPf6aogouz8WE%2FfMDMuRLVPTGm%2FPZiwlwtBpz7bF0fQRb9%2B%2FaXAJbfO%2BlrMVD%2BWuz7gRkIGmNXPTsGdNcxmWxzd2rOhzKnNHwK6ZRAgjt7YOHoYk4AryM&X-Amz-Signature=d1caee1462f0d9a3e9692c9e53b998238062bb25ca81f4b6c3f072b71585cb7e&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

[image](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/b16f49ae-40fb-4479-808f-6990b11f7714/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UXRWRYRU%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T225637Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCRrrF7pFp%2FKqZ6GPkAW%2F5qb0IFqq%2B9rsYYRsEJDE3k%2BAIgTidjsygn9aYSuHpqiFI2zC2SWU%2BYZ7y4B20gOJg%2FNTMqiAQIxv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDLCX8a9B9%2FWpfoj%2BcSrcA7%2F95b%2F%2FJHZctCzJ9H%2FZmFi4glZwGv4ApuYZztBJYNsvq%2BVoEiGGTUgGJffRglqFza6Q5qX71YwSXQyeGn3rAiF9D9rH6rvJaciWIRMEa5eWzZGfbcECTninzAAXMsHyKGrE8ewlmjpQ6KZBIpc7AEk0%2FGB9FGwbtxVawC%2F2B0TE5RRgvCB3fYilz99eifXmQn0CrRKuHi9N5%2BLnN7SZHsbx1tKq2V2Gyoou%2B2pBMt9TVkF1xchHynl4EXHHEFP9lPKIjAts80G%2BE4Sgt2OfXGCbZpi%2FLktEzuziVOavLrtK2xRqA4ne3iI9ms3qucyKDNRta0jIP%2FDdXvZqaNo2H%2F1JC80f2T3v3TArGAB%2Fm45mBB2FC%2FdnyZof3vD3LISfmdsGTbDHAzcy5bu%2Ftn1DyK6H7t3rnEr%2Bjrq5kfwWOUNI1J6S4rWL8GmkCCmIahBFjhfo0%2ByrqBrji%2BPlpNycfnbKdtUKOQ6gAvGML6%2FQbTuHm6az8ZWdMu0hCUPx36q1e%2BZaYblDpptXS4mDgrvVudPU5HZ7i%2FEOdfdbfJNHS6U5qpNLGbs2IdgS6C824exZQxCe3APn4N4vZPRSia50Zi31YJuBD%2FWzsBUn%2Baya8f7n4mJ9BIOtNoUnWxwAMKC4%2F9IGOqUB0e20w1lbepd3F0b5iAp0ABRSPyr%2FkScIqQyp5%2FeKe2LjJWPcJ%2BTT7btmiGd7RNYkDvuwOQvwbsP2SOmnIa83rPDMDn8hTRHO59rekBGIPf6aogouz8WE%2FfMDMuRLVPTGm%2FPZiwlwtBpz7bF0fQRb9%2B%2FaXAJbfO%2BlrMVD%2BWuz7gRkIGmNXPTsGdNcxmWxzd2rOhzKnNHwK6ZRAgjt7YOHoYk4AryM&X-Amz-Signature=8e8aec6072b8eaaf0707e891aa3a57b76bcedf930182c4e17a19e9cd1c5202f1&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

各网的各位同学们，大家好，终于要进到 high streaks 章节中第一个源码实践环节了。这一节我们来尝试如何使用最简单的 fall back 降级方案。这一节的主要内容有第一点，创建一个新的项目 high strikes consumer 然后把必要的依赖项引入进去。接着第二个内容就是这一章的主要部分实现 

fallback 降级逻辑。

[image](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/9f947681-6b8e-431b-8537-75d8893f4da8/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UXRWRYRU%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T225637Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCRrrF7pFp%2FKqZ6GPkAW%2F5qb0IFqq%2B9rsYYRsEJDE3k%2BAIgTidjsygn9aYSuHpqiFI2zC2SWU%2BYZ7y4B20gOJg%2FNTMqiAQIxv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDLCX8a9B9%2FWpfoj%2BcSrcA7%2F95b%2F%2FJHZctCzJ9H%2FZmFi4glZwGv4ApuYZztBJYNsvq%2BVoEiGGTUgGJffRglqFza6Q5qX71YwSXQyeGn3rAiF9D9rH6rvJaciWIRMEa5eWzZGfbcECTninzAAXMsHyKGrE8ewlmjpQ6KZBIpc7AEk0%2FGB9FGwbtxVawC%2F2B0TE5RRgvCB3fYilz99eifXmQn0CrRKuHi9N5%2BLnN7SZHsbx1tKq2V2Gyoou%2B2pBMt9TVkF1xchHynl4EXHHEFP9lPKIjAts80G%2BE4Sgt2OfXGCbZpi%2FLktEzuziVOavLrtK2xRqA4ne3iI9ms3qucyKDNRta0jIP%2FDdXvZqaNo2H%2F1JC80f2T3v3TArGAB%2Fm45mBB2FC%2FdnyZof3vD3LISfmdsGTbDHAzcy5bu%2Ftn1DyK6H7t3rnEr%2Bjrq5kfwWOUNI1J6S4rWL8GmkCCmIahBFjhfo0%2ByrqBrji%2BPlpNycfnbKdtUKOQ6gAvGML6%2FQbTuHm6az8ZWdMu0hCUPx36q1e%2BZaYblDpptXS4mDgrvVudPU5HZ7i%2FEOdfdbfJNHS6U5qpNLGbs2IdgS6C824exZQxCe3APn4N4vZPRSia50Zi31YJuBD%2FWzsBUn%2Baya8f7n4mJ9BIOtNoUnWxwAMKC4%2F9IGOqUB0e20w1lbepd3F0b5iAp0ABRSPyr%2FkScIqQyp5%2FeKe2LjJWPcJ%2BTT7btmiGd7RNYkDvuwOQvwbsP2SOmnIa83rPDMDn8hTRHO59rekBGIPf6aogouz8WE%2FfMDMuRLVPTGm%2FPZiwlwtBpz7bF0fQRb9%2B%2FaXAJbfO%2BlrMVD%2BWuz7gRkIGmNXPTsGdNcxmWxzd2rOhzKnNHwK6ZRAgjt7YOHoYk4AryM&X-Amz-Signature=1605c9bbba3961bcd090022dea9bbb3533efc265b8b7edac37bb8f005927e34c&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

最后一块内容是我们来聊一聊 fall back 降级除了静默降级手段以外还有什么其他的花式玩法。那对于很多在中小型公司或者是在一些传统行业工作的同学们，可能很难接触到熔断和降级。但是这两个手段可是互联网项目中非常非常常用的技术。我们整个 high streaks 章节也是铺的干货满满，相信很多同学已经迫不及待的要进入动手实操的环节了。对不？对知识的渴求，你的大脑已经即可难耐了。好满足大家。我们抄起家伙，主场开拔，大声喊出我们的口号，每天扣 01 小时，健康工作 50 年。
这一节新章节新气象，我们创建一个全新的 high strikes 的文件夹。好后面所有 high streaks 的项目我们都会放到这个文件夹里来进行。接下来就要创建本章的第一个毛九，给它起一个很贴切章节名称的名字它的 artifact 叫 high streaks 杠 fall back 一个非常负能量的标题 fall back 点击下一步，毛球 name 和前面保持一致。然后文件夹这里大家要写上 high streaks 不要走错门了大晚上进错门。不好的点击 finish 这里的 dependency 我们要从哪里，从 fin 里面 copy 一部分过来，从哪个地方copy。 Fain consumer advanced.这里我要把所有的 dependency 全 copy 过来。


大家看我这一个份章节的 dependency 这个 interface 大家还有印象吗？我为什么也要 copy 它？因为我们这一节的 high streaks 是一个服务调用者，它调用谁呢？没错，它正是要调用 thin client 所以它也需要这么一个 interface 那我把以上四个 dependency 全部给它引入进来，加到 high streaks 的 pump 文件当中一个 dependencies 节点，把这四个全部加入进去。完事还没有。


这里我要再给他加入一个新的注解，这就是本章的主角了，他的名字就是 high streaks 我这里从下面 copy 一个 dependency 的 group ID spring cloud 那它的 artifact 是什么？比较长，我们把它的全名给它念出来。 spring cloud 杠 starter 再杠 Netflix 再杠 high streaksok 这便是我们这一张主角 high streaks 的 dependency 了。定义完这两项，给他随手指派一个 package 这儿。好了，内蒙不给了，英雄不问出处直接写代码。


好了，在开始之前我们要先对 finn 动一点手脚。咱不是提到 fall back 吗？ fall back 什么含义啊？ fall back 的意思就是知错能改，那他得先犯错。我们目前的分 client 方法都是杠杠的，没有一个方法能抛出异常怎么办？那构造一个异常方法呗，给它构造一个就叫 error 的方法好不好？那它接收什么参数什么都不接，给它一个 get mapping 最简单的形式，一个 URL 叫 error 但凡访问这个error ，它总会抛出 error 好，接下来光改接口还不行，是不是还要改它的服务提供者 think client 好，我们点开 controller 走到上面看，已经标红字了，那就说有方法还没有实现，那就是这个 error 方法这里有什么业务逻辑吗？没有直接给它抛出异常。错是你的错。后面一句歌词叫什么呀？忘了呀。


这个 exception 给它的名字就叫 black sheep 这里顺带教大家一个词， black sheep 黑色的绵羊。 no 这叫害群之马。那有一首很出名的歌叫 season in a song 它里面就唱到 I was a black sheep of my family 我曾经是这个家族的害群之马，这里定义完了害群之马，咱们再回过头来开始定义我们 hystrix 的主流程了。在 Java 包下面创建一个如雷贯耳的 package bomb.eye milk.spring clot 紧接着跟一个闷函数，千里之行始于足下，给它起一个名字叫 high streaks fall back application 回撤。好很快感的 public static 闷方法咱就不享受了，从别的地方 copy 一个粘贴过来走起累的名字替换一下。


那它由多少个新的 annotation 挂在类上面呢？告诉大家四个哪四个呢？咱掰着手指头数一下 enable eureka 要不要？ discovery client 跟不？我跟接下来还有什么 spring boot 跟不？跟还有哪一个呢？前面还了谁学到了 fin 对不对？ fin 是哪个注解啊？ fin client 还是下面一个？ enable fin clients 再跟最后一个是谁啦？他是新同学。大家看名字有点奇怪。 enable circuit breaker 断路器。先把这个注解挂上去，后面章节都会有用到的。好三缺一凑起四个。然后咱再跟这个害群之马做个联系。前面定义了一个害群之马的方法，对不对？那咱这给它来一个首尾呼应。我这里定义一个 interface 叫 my service 走，这个 my service 它既成自 I servicei service 是不是就是刚才咱声明害群之马的地方这边咱在它的类上面加上一个分注解，顺带复习一下上一章的知识。


名字叫什么？名字是谁 think client 就是你要调用礼服务，接下来我要在它后面加上一个 fall back 属性，但是这里只是跟大家做一个小剧透，我现在还不会加，为什么呢？因为你只知道 for bike 不知道后面该填谁，咱先去把后面的部分完成，待会再来杀个回马枪后面的部分，就有那么点意思了，我这里给它新建一个 package 就叫 high streaks 回车。在这个 high streaks 里面给它建一个类叫做 fall back 句型要进入高潮喽。这个 fall back 怎么办呢？大家看好了， implements 谁我刚才创建的 my service 把里面的没有实现的方法系数列出来，召唤出来。好，前面几个方法咱们不用管它，咱们把最后这个老莫 copy 一下，把它给提上来，放在哪里放在排头。好勒。重点关注这个方法。害群之马，我要在这里把它怎么样绳之以法。看到这里，大家是不是似乎明白了一些什么东西呢？这个 fall back 就是针对于 my service 的容错类，也就是它的 fall back 逻辑的所在地方。这里我给它返回一个静默处理的结果叫 fallback 我要发出一句忏悔对不对？我做了这么长时间的害群之马，这句忏悔呢要发的深刻一点，真诚一点。


I am not a black sheep anymore any longer 好，这就处理完了吗？没有，咱给它加一个 annotation sl four G 在这里面给它打一个注解，你光喊出口号没有用，你要留有证据。那就要在 log 里面有所体现。对不对好不想当一个害群之马了，顺手给他加一个component 。加好了这些以后怎么办？我们回到刚才的回马枪的地方，来看这招回马枪怎么杀。


好点进去看这个分 clan 的属性走，你看这里面往下拉拉到最后这是什么？ fall back 它的类型是什么？一个 class 类型看到没？那接下来大家应该知道怎么办了？我这边指定一个 fall back 属性，紧接着把我刚才创建的 fall back 类的 class 给它添加进来。 OK 这就完成了。那每当你访问 iservice 的 error 方法。报出错误以后，我们的 high strikes 就会将你的这个用户访问请求导入到哪里？导入到这个 fall back 的 error 里面。那如果同学说假如超时了怎么办呢？没关系，超时了也算一种错误。对不对？待会儿我们去配置文件中，给这个超时专门加一行配置，大家就知道该怎么做了。
好，声明完了方法和 service 以及 fall back 以后，大家觉得是不是还缺少什么内容？你还少一个 controller 对不对？好，我们这里给你创建一个 controller 接收用户的访问请求，头顶上跟他挂一个 rest controller 然后注入一个类，注入谁呢？注入我们的 service my service 这就不要对它发起调用了， auto wire 的进来不能缺。


这个看出了，咱先加一个方法，跟这个 error 联系起来，把它调用一番，名字就给它起掉 fall back 好了，二话不说直接调用 myservice.error 明知道它报错还是要调用，明知山有虎，偏向虎山，行完事之后给它加一个 get mapping 那么它的 past 是什么？直接叫 error black ship 不太好，直接告诉别人我是害群之马。算了吧，这叫 fall back 。


OK 就这么轻松 controller 也定义完了，最后还缺什么？老师是不是每次都习惯在最后配置这个配置文件呢？没错啦，这里找到 resource 文件夹，给它添加一个 file application.properties 好，接下来进入算命先生起名环节，给这个应用起一个名字叫 spring [application.name](http://application.name/) 叫什么名字？ high strikes 杠 consumer 好听吗？接下来是 server 的端口，前面咱都是从 4 万开头，这次给它起名叫 5 万。好了，打麻将打到了 5 万了。


然后还有一个属性是什么？前一张 fin 里面我们讲到的 spring.man.olav bin definition override 允许 bin 上面的注解的重在对不对？ OK 这三个配置好之后，咱们有瑞卡注册中心的地址项给它 copy 过来，随便找一个项目。 Copy paste. 有瑞卡的注册中心，有了咱就可以放手的配置新的项目了。新的柱子也像是谁。咱大家看，我先给他配置一个 fin.high streaks.enabled 开启缝下面的 hystrix 注解，这个从名字上面就非常好理解 high strikes 注解功能。


开启完这个功能以后，我们还要再多配这几个项目这些项目实际上有些是默认开启的，我只不过是想让同学们看一看它都有哪些配置的。像所以说才把这里给拎出来给大家见个面。那下一个属性是 high streaks.comment 再点 default 看哪是一个默认 fall back.enabled 它是什么含义呢？它的含义就是告诉大家是否开启服务降级。那如果你不开启的话实际上也没问题的。但是你要是想关闭，可就要强行的在这边指定一个 false 喽。


那同学们想想还有其他属性吗？多了 high streaks 的属性几十个不止。那咱这里就暂且先开这两个小试牛刀。第一个功能就简单的把功能开起来，先尝试一下。如果 OK 接下来咱再做什么测试呢？超时测试，我们这里会定义一大串超时服务的指令来验证 high streaks 的超时降级功能。


OK 接下来是不是就要开启服务进行测试了？我们首先有请 eureka server 登场， spring 成功一半。紧接着咱 eurika server 启动成功以后，该启动谁了？ thin client 对不对？它是整个的服务提供者。等到分 client 也启动成功了以后，我们就要把当前的 high streaks fall back application 给启动起来。好切换到 high strikes 走，你这三个项目全部启动起来以后，我们转战到 post man 里去，对这个 high streaks for back application 发起一个调用。但是在调用之前，咱先把这个 log 给它清掉，这样方便看新发出的 log 对不对？转战 postman 我这里向 local host 5 万端口发送一个指令，这个 5 万是谁？是不是我们刚才创建的 high streaks application 没错，那它发送到哪呢？发送到 fall back 里面。 OK 三二一起飞。


看到吗？看它的返回值是谁？这个返回值是来自于分 client 吗？可不是。我们来看分 client 这边发生了什么事情，你看从 log 里面大家可以看出，分 client 直接抛出了异常，对不对？那他按理说应该接收到500。那为什么我这边有一个返回值呢？这个返回值是谁？没错，看到吗？这里 fall back IM not a black sheep anymore 它是来自于我们的降级流程。也就是说当我们的 I service 请求失败了以后，这个 my service 将我们的用户来访请求重新导到了这个当前的 fallback 类中的 error 函数里。


大家看这个 log 中和页面返回的结果是不是一模一样的？ IM not a black ship anymore OK 那既然这个方法测试成功了，说明什么呢？在直接产生异常的情况下，我的 high streaks 是可以工作的。那么接下来我们一起来看一看 high streaks 如何应对超时的问题。那我们开启一段中场休息，下一小节我们再见。



```java
~~Controller
package com.imooc.springcloud.controoler;

import com.imooc.springcloud.MyService;
import com.netflix.discovery.converters.Auto;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RestController;

/**
 * <h1></h1>
 */
@RestController
public class Controller {

    @Autowired
    private MyService myService;

    @GetMapping("fallback")
    public String fallback() {
        return myService.error();
    }

    @GetMapping("timeout")
    public String timeout(Integer timeout) {
        return myService.retry(timeout);
    }
}
```

```java
~~~MyService
package com.imooc.springcloud.hystrix;

import com.imooc.springcloud.Friend;
import com.imooc.springcloud.MyService;
import lombok.extern.slf4j.Slf4j;
import org.springframework.stereotype.Component;
import org.springframework.web.bind.annotation.RequestBody;
import org.springframework.web.bind.annotation.RequestParam;

/**
 * <h1></h1>
 */
@Component
@Slf4j
public class Fallback implements MyService {


    @Override
    public String error() {
        log.info("Fallback : I'm not a black sheep any more");
        return "Fallback : I'm not a black sheep any more";
    }

    @Override
    public String sayHi() {
        return null;
    }

    @Override
    public Friend sayHiPost(@RequestBody Friend friend) {
        return null;
    }

    @Override
    public String retry(@RequestParam("timeout") int timeout) {
        return "You are late";
    }

}
```

```java
~~HystrixFallbackApplication
package com.imooc.springcloud;

import org.springframework.boot.WebApplicationType;
import org.springframework.boot.autoconfigure.SpringBootApplication;
import org.springframework.boot.builder.SpringApplicationBuilder;
import org.springframework.cloud.client.circuitbreaker.EnableCircuitBreaker;
import org.springframework.cloud.client.discovery.EnableDiscoveryClient;
import org.springframework.cloud.netflix.hystrix.EnableHystrix;
import org.springframework.cloud.openfeign.EnableFeignClients;

/**
 * <h1></h1>
 */
@SpringBootApplication
@EnableDiscoveryClient
@EnableFeignClients
@EnableCircuitBreaker
public class HystrixFallbackApplication {


    public static void main(String[] args) {
        new SpringApplicationBuilder(HystrixFallbackApplication.class)
                .web(WebApplicationType.SERVLET)
                .run(args);
    }
}
```

```java
~~~MyService
package com.imooc.springcloud;

import com.imooc.springcloud.hystrix.Fallback;
import org.springframework.cloud.openfeign.FeignClient;

/**
 * <h1></h1>
 */
@FeignClient(name = "feign-client", fallback = Fallback.class)
public interface MyService extends IService {
}
```

```java
~~  application.properties

spring.application.name=hystrix-consumer
server.port=50000
spring.main.allow-bean-definition-overriding=true
eureka.client.service-url.defaultZone=http://peer1:20000/eureka

# 开启 Feign 的 Hystrix 功能
feign.hystrix.enabled=true
# 是否开启服务降级
hystrix.command.default.fallback.enabled=true

# 全局超时
hystrix.command.default.execution.timeout.enabled=true
# 超时时间
hystrix.command.default.execution.isolation.thread.timeoutInMillisecond=2000
# 超时以后终止线程
hystrix.command.default.execution.isolation.thread.interruptOnTimeout=true
# 取消的时候终止线程
hystrix.command.default.execution.isolation.thread.interruptOnFutureCancle=true






#===============Ribbon=======
# 每台机器最大的重试次数
feign-client.ribbon.MaxAutoRetries=2
# 可以再充实几台机器
feign-client.ribbon.MaxAutoRetiresNextServer=2
# 连接超时
feign-client.ribbon.ConnectTimeout=10000
# 业务处理超时
feign-client.ribbon.ReadTimeout=2000
# 所有的Http Method进行重试
feign-client.ribbon.OkToRetryOnAllOprations=true
```




