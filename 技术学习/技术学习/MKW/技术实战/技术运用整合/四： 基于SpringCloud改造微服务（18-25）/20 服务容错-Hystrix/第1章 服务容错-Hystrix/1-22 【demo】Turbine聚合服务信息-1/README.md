---
title: 1-22 【demo】Turbine聚合服务信息-1 
---

# 1-22 【demo】Turbine聚合服务信息-1 

[image](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/d79caef4-c552-4c30-b147-006c9f6ff873/SCR-20240719-emrz.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RS6RMOHK%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T225650Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDXYfg45UG3qDAQum3c6n5L3WTIvvXR1UtLYiqQr1z6MQIhAMxjguc1rZhmawmGuYTtCotzWv0JnAidI7qHSqY4HGWTKogECMb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1Igwl%2FofVqX%2BK7eF4dXAq3APNausNGmFvjYroRAGPTsVqDXSUOgPpjgNW5mcW2GhMAHsDutpH08HuyX2LJV6sm9TuhWNYJStkeKRNalS%2FoZCwDLiM9Tr6Z9qx2nam6g8py2WNuEiQzNIe8QIGt1IFptVkeUp4BApq%2F8omI4N8WLMPc%2BN7Deb948Sk6v%2B8YF4ImdbvIzCi0PZ1SRoBogOZLemJ%2BdWqGSL6ekr8dEjnosn4ZGBptgNrAnMjSoiY2Pi%2FIAID29EJsQA9fHV3vSwQvZBXKDFEstYkoqW6jlErXWZVduA%2BX%2BUq4Vf4AnFmhWvWPp0mJkp8NhBT96vi7IY%2BVOnsxrxSOwD3m3Dv7bSDNamb7rwwXIIyGOuTiSnagKwpjANm4KIdDS6vNMuwrtDWaqDSZCRmcknZckSJXQA7tnkFkD0iwlWkZMCJ%2Bg7tV54AcNamQStHydIdHawGpJK%2FV%2FIG20ul%2BEKvEn7op6Sz9Lya7W2OBcHNAQV1eq0skwkrJrRCaBY9kfN7ucc0Xr%2FFnSFAe6wITZ668tZcv8gVZRTARwXuIZ2ydOmw2smYUj3UzZM8oPkqEhJNu5xb333S4EFbNjLRqFFo0Zwvmr3vfYDYlMqaxcn1em28QQqHef2vnLXG1eas%2BK4rusDCFzDruf%2FSBjqkAeFqYUw%2BV7fHqCaqYpiJqhtm1Z0Mo70ZF1%2FSVJeP%2BUgVcPiLA3pp0mOMeHuYv6Yl0VoYWNwb%2FbKlCOh%2BjFYohC55nUGAL731CFSon9bPsHOKZ4UpZa9FzgSd4WDro0jLQAGbh3ai27sCSHgFvW%2BB0hwvRd755dVKn%2FOhzh886u2HlTjcabnmpdpeBQ%2BVjPmwN%2FsY%2BX2wbkJ7LRhcCoIbf8Az%2FUm%2F&X-Amz-Signature=299bd4c05e938e1512c925d98f6a1a03804ef2ab10dbc9822cdddfe9aaa3f6cb&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

[image](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/29bf6838-f704-428c-80cd-652bfe2e320c/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RS6RMOHK%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T225650Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDXYfg45UG3qDAQum3c6n5L3WTIvvXR1UtLYiqQr1z6MQIhAMxjguc1rZhmawmGuYTtCotzWv0JnAidI7qHSqY4HGWTKogECMb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1Igwl%2FofVqX%2BK7eF4dXAq3APNausNGmFvjYroRAGPTsVqDXSUOgPpjgNW5mcW2GhMAHsDutpH08HuyX2LJV6sm9TuhWNYJStkeKRNalS%2FoZCwDLiM9Tr6Z9qx2nam6g8py2WNuEiQzNIe8QIGt1IFptVkeUp4BApq%2F8omI4N8WLMPc%2BN7Deb948Sk6v%2B8YF4ImdbvIzCi0PZ1SRoBogOZLemJ%2BdWqGSL6ekr8dEjnosn4ZGBptgNrAnMjSoiY2Pi%2FIAID29EJsQA9fHV3vSwQvZBXKDFEstYkoqW6jlErXWZVduA%2BX%2BUq4Vf4AnFmhWvWPp0mJkp8NhBT96vi7IY%2BVOnsxrxSOwD3m3Dv7bSDNamb7rwwXIIyGOuTiSnagKwpjANm4KIdDS6vNMuwrtDWaqDSZCRmcknZckSJXQA7tnkFkD0iwlWkZMCJ%2Bg7tV54AcNamQStHydIdHawGpJK%2FV%2FIG20ul%2BEKvEn7op6Sz9Lya7W2OBcHNAQV1eq0skwkrJrRCaBY9kfN7ucc0Xr%2FFnSFAe6wITZ668tZcv8gVZRTARwXuIZ2ydOmw2smYUj3UzZM8oPkqEhJNu5xb333S4EFbNjLRqFFo0Zwvmr3vfYDYlMqaxcn1em28QQqHef2vnLXG1eas%2BK4rusDCFzDruf%2FSBjqkAeFqYUw%2BV7fHqCaqYpiJqhtm1Z0Mo70ZF1%2FSVJeP%2BUgVcPiLA3pp0mOMeHuYv6Yl0VoYWNwb%2FbKlCOh%2BjFYohC55nUGAL731CFSon9bPsHOKZ4UpZa9FzgSd4WDro0jLQAGbh3ai27sCSHgFvW%2BB0hwvRd755dVKn%2FOhzh886u2HlTjcabnmpdpeBQ%2BVjPmwN%2FsY%2BX2wbkJ7LRhcCoIbf8Az%2FUm%2F&X-Amz-Signature=b6f0595f26ba3d34167e6838cf45986b1b19cbc0596dd1d1dcb7ca09a706d104&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

慕课网的各位同学们，大家好，这一节我们来学习一个新的组件，它叫 turbine 同学们可能是第一次听到这个名词，turbine具体是来做什么的呢？那我们就要从这个三兄弟的故事说起了。 high streaks 如果是大哥的话，他有两个左膀右臂分别是谁呢？ turbine 和 high streaks portal 这三兄弟搭档在一起，法力无边，他们分别都负责什么事情呢？ high streaks 我们前面学习到了，就是负责降级、熔断这些功能。那 turbine 这个家伙他会从 eureka 中发现指定服务的机器列表，并且从这些机器特殊的 end point 端口上，把 high stricks 的降级熔断以及接口的成功率等等 metrics 信息收集过来。这还没有完。
收集好以后，我们可以通过 high streaks portal 也是一个大盘的应用，将 turbine 中的信息展示出来。那有了 turbine 还有大盘监控。那我们 high streaks 各位是左青龙右白虎，老牛在中间横行江湖，无所不能。

[image](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/250bc6c5-88f4-4cf0-9bc6-8e16d9714b1c/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RS6RMOHK%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T225650Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDXYfg45UG3qDAQum3c6n5L3WTIvvXR1UtLYiqQr1z6MQIhAMxjguc1rZhmawmGuYTtCotzWv0JnAidI7qHSqY4HGWTKogECMb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1Igwl%2FofVqX%2BK7eF4dXAq3APNausNGmFvjYroRAGPTsVqDXSUOgPpjgNW5mcW2GhMAHsDutpH08HuyX2LJV6sm9TuhWNYJStkeKRNalS%2FoZCwDLiM9Tr6Z9qx2nam6g8py2WNuEiQzNIe8QIGt1IFptVkeUp4BApq%2F8omI4N8WLMPc%2BN7Deb948Sk6v%2B8YF4ImdbvIzCi0PZ1SRoBogOZLemJ%2BdWqGSL6ekr8dEjnosn4ZGBptgNrAnMjSoiY2Pi%2FIAID29EJsQA9fHV3vSwQvZBXKDFEstYkoqW6jlErXWZVduA%2BX%2BUq4Vf4AnFmhWvWPp0mJkp8NhBT96vi7IY%2BVOnsxrxSOwD3m3Dv7bSDNamb7rwwXIIyGOuTiSnagKwpjANm4KIdDS6vNMuwrtDWaqDSZCRmcknZckSJXQA7tnkFkD0iwlWkZMCJ%2Bg7tV54AcNamQStHydIdHawGpJK%2FV%2FIG20ul%2BEKvEn7op6Sz9Lya7W2OBcHNAQV1eq0skwkrJrRCaBY9kfN7ucc0Xr%2FFnSFAe6wITZ668tZcv8gVZRTARwXuIZ2ydOmw2smYUj3UzZM8oPkqEhJNu5xb333S4EFbNjLRqFFo0Zwvmr3vfYDYlMqaxcn1em28QQqHef2vnLXG1eas%2BK4rusDCFzDruf%2FSBjqkAeFqYUw%2BV7fHqCaqYpiJqhtm1Z0Mo70ZF1%2FSVJeP%2BUgVcPiLA3pp0mOMeHuYv6Yl0VoYWNwb%2FbKlCOh%2BjFYohC55nUGAL731CFSon9bPsHOKZ4UpZa9FzgSd4WDro0jLQAGbh3ai27sCSHgFvW%2BB0hwvRd755dVKn%2FOhzh886u2HlTjcabnmpdpeBQ%2BVjPmwN%2FsY%2BX2wbkJ7LRhcCoIbf8Az%2FUm%2F&X-Amz-Signature=a75960f5907692bc1424180d12f7e67385ddefb3e408ec9328a75dd23f116cc4&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

好。说了这么多，那咱先从第一步开始，看一看如何通过 turbine 来聚合服务的信息。本章的主要内容有三点，第一部分，创建 high streaks turbines 模块，然后将相应的依赖加入到 palm 当中。第二步就是添加 turbine 的配置。在这里我们将要指定监控服务的名称以及配置 eurika 注册中心等等各种属性。最后一点，我们要开启 high streaks fallback 项目的 activator 服务。为什么要这样开呢？因为我们的 turbine 和后面将要学习到的 high strikes 监控大盘，实际上是通过 activator 暴露的服务端接口来访问 high strikes 聚合信息的。因此我们要把相应的服务给它暴露出来。 OK 那我们怀着轻松愉悦的心情走向 intelligj 准备开工，每天扣订 1 小时，健康工作 50 年。这回我们是真的要正儿八经 coding 了。


接下来咱要创建一个 high strikes turban 的服务，我们这里 create 一个新的 module 给它起名叫什么呢？就叫 high strikes turban 点击 next module name 和前面的 artifact ID 保持一致，然后把它放到 high streaks 文件夹下，点击 finish 倒数三个数三二处好，收起小桌板，咱开始添加 dependency 了。


我们这里用一种新的方式添加dependence ，咱先添加谁呢？咱添加这一章的主角 turbine 的服务，然后再去添加那些边边角角的其他类型的dependency。 Okay. 这里声明一个 dependency group ID 是 orgspring framework.cloud 大家非常熟悉的 artifact 是谁呢？ spring cloud 杠 starter 杠 Netflix 又是 Netflix 的组件。所以这家公司真心佩服一家影视公司可以做到这种程度，后面跟着谁 turban OK 好，这个依赖引入进来了，大家还需要其他依赖的。那我们从别的地方把它给 copy 过来。好了，从哪个项目中 copy 呢？


我看 high streaks fall back 这个项目挺合适的。浓眉大眼的，咱就从这个家伙里面 copy 一下。 copy 谁呢？ eurika 要不要要 springboot 当然也要了 actuator 把它拿下。除了这些还有谁呢？当然是 high strikes 了。对不对？所以说这一页所有应用咱都把它 copy 下来。好像还加塞了一个人，谁这个 interface 咱不要的，咱们把它 copy 过去，再给它剔除出名。


OK 现在 copy 到 high strikes turban 中，把这个 interface 拿掉，我们数一数，现在加了几个音，123455个 dependency 好了，那到这里所有 dependency 都已经加完了，接下来要做什么呢？创建启动累了对不对？有一个好消息要告诉大家，我在思考是现在告诉大家还是待会创建完启动类要告诉大家算了，还是现在告诉大家吧，咱这个项目啊它只有启动类，写完启动类改配置就好了，没有其他的代码要写。


那刚才我创建了一个 com.imock.spring cloud 的包，接着在这个包下面创建一个 turbine application 回车。那接下来要把慢方法也给写上，我们依然从 high streaks fall back 中把它 copy 过来一个闷方法 copy 到这里，然后把类名换一下，换成我们的 turban application。


Ok. 那么下一个环节是什么呢？给这个类戴高帽对不对？往类上面加注解。那给他戴几顶高帽子好几顶。第一个，高帽子是谁？是我们的服务发现对不对？ eureka 的 enable discovery client 注解 enable discrete client OK 那它需要正注解做什么呢？待会我们要配置 turban 需要监控的服务。那这个服务是以服务名的形式给出来的，具体的机器名称它到哪里找呢？当然是到 eureka 上面来找了，所以它这里需要 eureka 的服务注解。


OK 第二个应用是谁呢？ enable high strikes OK 我们需要这个注解，大家点进去看一下。这个注解中暗藏玄机有谁看到吗？有这样一个注解，很眼熟对不对？ enable circuit breaker 那这个注解就是我们前面的 high streaks for back 项目中配置的注解了，其实这里你可以把它拿掉，我这里就是为了让大家回忆一下之前学的内容，把这个单独拎了出来。


Ok.除了这三顶高帽子还有谁呢？还有就是我们自己的高帽，给自己戴高帽叫 enable turban 然后还有吗？我这里再给它添加一个注解，叫 enable auto configuration 启动自动装配到这里，咱带了 123455 顶高帽子。完了后面做什么事情呢？添加配置文件对不对？好？我们到 resources 文件夹下添加一个什么了？application.properties。 Ok application the practice.


这里我们可要大显身手了。第一个属性大家应该都非常熟悉了，叫什么？这个属性的名称就叫报上名来。 spring [application.name](http://application.name/) 我们给它起名叫 high streaks turbine turbineok 第二个属性，给它配置 server port 在一台机器上做测试就这点麻烦你每一个 port 都要启动不同的端口，除非你用Docker ，我这里给它起叫52,000。好了，那保持个好习惯，有些应用它莫名其妙的会在后台开启管理界面的端口 management port 那我们给它起到 one 2001。


好了。好，这两个配置好之后，接下来咱要配置 eureka 的服务，发现我们从前面的 high streaks fall back 应用中把友锐卡的这行配置给它 copy 过来，一行万年不变的配置永远连到 2 万端口。好和往后的配置。可就是跟特尔版非常有关系了。我们来看，这里都是大家没见过的配置。
第一个铁板点 App 杠 config 大家能猜出它是什么意思吗？接下来我往后写，大家应该就能知道了。 high streaks fall back 这是什么含义啊？大家是不是一目了然了，这个 high streaks fallback 是什么？是一个服务名，对不对？那前面的这个应用是指定了所需要监控的服务名，我这里就他指定，你给我盯好 high strikes fall back 这个服务把他所有机器的熔断信息，降级信息全部都给我返回回来。那他到哪里拿机器列表，就像我们前面说的，他是到这个尤瑞卡注册中心的，对不对？ OK 接下来我们往后配置。

[image](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/3546434d-0b2e-4ab0-a91a-8b3ddd3d664a/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RS6RMOHK%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T225650Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDXYfg45UG3qDAQum3c6n5L3WTIvvXR1UtLYiqQr1z6MQIhAMxjguc1rZhmawmGuYTtCotzWv0JnAidI7qHSqY4HGWTKogECMb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1Igwl%2FofVqX%2BK7eF4dXAq3APNausNGmFvjYroRAGPTsVqDXSUOgPpjgNW5mcW2GhMAHsDutpH08HuyX2LJV6sm9TuhWNYJStkeKRNalS%2FoZCwDLiM9Tr6Z9qx2nam6g8py2WNuEiQzNIe8QIGt1IFptVkeUp4BApq%2F8omI4N8WLMPc%2BN7Deb948Sk6v%2B8YF4ImdbvIzCi0PZ1SRoBogOZLemJ%2BdWqGSL6ekr8dEjnosn4ZGBptgNrAnMjSoiY2Pi%2FIAID29EJsQA9fHV3vSwQvZBXKDFEstYkoqW6jlErXWZVduA%2BX%2BUq4Vf4AnFmhWvWPp0mJkp8NhBT96vi7IY%2BVOnsxrxSOwD3m3Dv7bSDNamb7rwwXIIyGOuTiSnagKwpjANm4KIdDS6vNMuwrtDWaqDSZCRmcknZckSJXQA7tnkFkD0iwlWkZMCJ%2Bg7tV54AcNamQStHydIdHawGpJK%2FV%2FIG20ul%2BEKvEn7op6Sz9Lya7W2OBcHNAQV1eq0skwkrJrRCaBY9kfN7ucc0Xr%2FFnSFAe6wITZ668tZcv8gVZRTARwXuIZ2ydOmw2smYUj3UzZM8oPkqEhJNu5xb333S4EFbNjLRqFFo0Zwvmr3vfYDYlMqaxcn1em28QQqHef2vnLXG1eas%2BK4rusDCFzDruf%2FSBjqkAeFqYUw%2BV7fHqCaqYpiJqhtm1Z0Mo70ZF1%2FSVJeP%2BUgVcPiLA3pp0mOMeHuYv6Yl0VoYWNwb%2FbKlCOh%2BjFYohC55nUGAL731CFSon9bPsHOKZ4UpZa9FzgSd4WDro0jLQAGbh3ai27sCSHgFvW%2BB0hwvRd755dVKn%2FOhzh886u2HlTjcabnmpdpeBQ%2BVjPmwN%2FsY%2BX2wbkJ7LRhcCoIbf8Az%2FUm%2F&X-Amz-Signature=fd30dcf968757b95878f9a9e035c5be9e34f90eacc9c1450f4b832a630314932&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

第二个属性是什么呢？ turbine.plaster 杠 name 杠 expression 那这个属性因为咱现在有几个 cluster 咱是不是只有一个 default cluster 这就不用问了，给它默认配一个 default 号。如果大家在大规模的分布式应用中，比方说我现在有好多个机房，那每个机房中成千上万台机器，一个 turbine 有可能收集到所有机器的信息吗？当然不能喽，这样的话对一个 turbine 来说压力就太大了，可能我们就要分配多个 turbine 然后每个 turbine 负责监控一个机房，等到这时候大家可能就需要配置 cluster name 杠 expression 这个属性了。那这里暂且把它放为default ，我们继续往下走。


好，下一个属性可跟大家本地测试息息相关了。为什么这么说呢？我们看它叫 turban.combine 杠 host pot 这是什么含义啊？怎么 host 和 POD 都出来了？大家知道为什么吗？因为我们的 turbo 默认情况下是以 host 来区分聚合服务的。那如果大家都在本地做测试，我们的 host 是不是相同的？都叫 local host 对不对？所以我这里要指定它不仅通过 host 做服务聚合，也要根据 POD 来，否则的话会怎么样？否则的话咱在本地启动的不同服务就会被聚合成了同一个服务来返回了。


那我这里，当他把 port 也考虑进去以后，即便我本地都是 local host 因为我的端口号不同，所以说在这种情况下，他依然会把所有不同端口的服务当成不同的服务来进行数据聚合和收集。那我们的注释怎么写呢？将端口和 host name 作为区分不同服务的条件。那默认情况是什么？我这里多加一句，默认值使用 hostok 这一个属性配置完。接下来还有吗？当然有了是什么？ turban 然后后面跟 instance URL suffix.default 它是什么值呢？大家往后看就知道 activator 杠 high strikes.dream 这一个属性看起来是谁是 activator 暴露出的一个 high strikes 服务。对不对？这个大家一看就明了，我就不在这添加注释了。


那最后一个属性，大家走马观花看一下就好。也是 turban aggregatoraggregator 是什么含义啊？ aggregator 是聚合的意思，后面跟 cluster config 依然是 default 为什么？跟前面这个属性一样，咱现在只有一个 default cluster okay 那配置完了这些配置以后，接下来还缺少


一个重要的步骤，我们要闯到 high streaks fall back 这个项目里改一通配置。
为什么大家要注意这一个属性，这个属性为什么和 high streaks fallback 有关系呢？是我们的turbine ，它需要连接到对应的服务，并且通过这个服务下的 accurator 暴露出的 endpoint 获取 high strikes 收集起来的信息。因此我们也要在目标服务上 by actuator 端口给它开放出来。好，那我们动身去 hystrix fall back 中等等。


别急，老师夜观星象隐约中看到了东方紫气腾升，好像是要出现一个运行期错误，让我看一下哪里配置不对？这里是只要监控的服务名称，咱们配置的成什么？咱配置成 artifact ID 了。所以同学们在这里一定要注意，它是你的服务名，可不是你在 Maven 中配置的 artifact 的名字。那它正确的服务名叫啥叫 high strikes 杠 consumer 好，这下我们可以放心的去另外一个项目中修改配置了，我们转移到 high strikes fallback 这个项目里。


在 application properties 里面配置那么几个参数，打开 accurator endpoint 第一个参数，咱先以给它的注释打上叫 activator 暴露接口。暴露这个词用得很到位，简单粗暴，其实应该叫开放接口。那第一个参数它的起手式是 management 后面跟什么跟 security 在跟 enable 的，我们把它写成 false 这是什么含义啊？就是我访问你的 actuator 接口，我并不需要 security 检查，我们 demo 就一切从简了。

[image](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/9f5bf437-621e-4008-9d88-7e82a965fecd/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RS6RMOHK%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T225652Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDXYfg45UG3qDAQum3c6n5L3WTIvvXR1UtLYiqQr1z6MQIhAMxjguc1rZhmawmGuYTtCotzWv0JnAidI7qHSqY4HGWTKogECMb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1Igwl%2FofVqX%2BK7eF4dXAq3APNausNGmFvjYroRAGPTsVqDXSUOgPpjgNW5mcW2GhMAHsDutpH08HuyX2LJV6sm9TuhWNYJStkeKRNalS%2FoZCwDLiM9Tr6Z9qx2nam6g8py2WNuEiQzNIe8QIGt1IFptVkeUp4BApq%2F8omI4N8WLMPc%2BN7Deb948Sk6v%2B8YF4ImdbvIzCi0PZ1SRoBogOZLemJ%2BdWqGSL6ekr8dEjnosn4ZGBptgNrAnMjSoiY2Pi%2FIAID29EJsQA9fHV3vSwQvZBXKDFEstYkoqW6jlErXWZVduA%2BX%2BUq4Vf4AnFmhWvWPp0mJkp8NhBT96vi7IY%2BVOnsxrxSOwD3m3Dv7bSDNamb7rwwXIIyGOuTiSnagKwpjANm4KIdDS6vNMuwrtDWaqDSZCRmcknZckSJXQA7tnkFkD0iwlWkZMCJ%2Bg7tV54AcNamQStHydIdHawGpJK%2FV%2FIG20ul%2BEKvEn7op6Sz9Lya7W2OBcHNAQV1eq0skwkrJrRCaBY9kfN7ucc0Xr%2FFnSFAe6wITZ668tZcv8gVZRTARwXuIZ2ydOmw2smYUj3UzZM8oPkqEhJNu5xb333S4EFbNjLRqFFo0Zwvmr3vfYDYlMqaxcn1em28QQqHef2vnLXG1eas%2BK4rusDCFzDruf%2FSBjqkAeFqYUw%2BV7fHqCaqYpiJqhtm1Z0Mo70ZF1%2FSVJeP%2BUgVcPiLA3pp0mOMeHuYv6Yl0VoYWNwb%2FbKlCOh%2BjFYohC55nUGAL731CFSon9bPsHOKZ4UpZa9FzgSd4WDro0jLQAGbh3ai27sCSHgFvW%2BB0hwvRd755dVKn%2FOhzh886u2HlTjcabnmpdpeBQ%2BVjPmwN%2FsY%2BX2wbkJ7LRhcCoIbf8Az%2FUm%2F&X-Amz-Signature=1503a2c67472ddf0dcb61615d4922cc54886181c110b2a4384d1aa6a258a322c&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

如果你在生产环境的时候可能需要配置一些 security 检查，因为不是所有人都可以在你的内网中访问 activator 接口的。因为 actuator 接口对你当前应用来说，它会将里面一些比较隐私的信息暴露出去。如果不想被其他业务方看到，咱这里要启动 security 检查的机制，我们这里把它先给关闭掉。
接下来第二个参数也是以 management 的开头，后面跟 endpoints.web.expose exposure include 这是什么含义呢？待一会儿我们把这个项目启动起来以后，可以通过它的 activator 接口看到很多很多的 endpoint 那这些 endpoint 就是由后面这个通配符决定的。这里配置的星号就是说把所有 endpoint 全部暴露出去，同学可以指定某些个别 endpoint 暴露。在实际的生产环境中我们往往只是暴露几个特定接口，这里为了简单起见所以就把全家福一次放出去了。


最后一个属性，咱们配置一个 management.endpoint 再点 health 看到 health 我突然想多提两句，其实我们很多人读 health 的时候都会读成 health 把尾音发成了 S 我们不太容易发出这个清辅音和浊辅音就像我们读谢谢逗号读三颗油对不对？到国外点菜都是 this one that one 蛮有意思的。那后面的一个 field 是 show details 顾名思义啦，就是我总 always 把所有的 detail 全盘放出，毫无保留。
OK 那配置好这三个参数，我们就可以尝试着启动项目来验证一番了。启动哪些项目？那我们依次要先启动尤瑞卡的注册中心，紧接着启动分 client application 启动完了这两样以后，我们再来启动 high streaks fall back application 把这三个项目先启动起来，我们先别着急启动 turbine 我带大家到页面上看一下 high strikes fall back application 的 activator 接口长什么样子。


好，我们转战到浏览器，打开一个新窗口，我们把 high streaks 的端口号打出来，它的端口是 5 万，紧接着跟什么参数跟 actuator 作为路径。好点击回撤。

[image](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/007b39db-8dd2-49ce-9521-7ac41b7f94d0/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RS6RMOHK%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T225652Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDXYfg45UG3qDAQum3c6n5L3WTIvvXR1UtLYiqQr1z6MQIhAMxjguc1rZhmawmGuYTtCotzWv0JnAidI7qHSqY4HGWTKogECMb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1Igwl%2FofVqX%2BK7eF4dXAq3APNausNGmFvjYroRAGPTsVqDXSUOgPpjgNW5mcW2GhMAHsDutpH08HuyX2LJV6sm9TuhWNYJStkeKRNalS%2FoZCwDLiM9Tr6Z9qx2nam6g8py2WNuEiQzNIe8QIGt1IFptVkeUp4BApq%2F8omI4N8WLMPc%2BN7Deb948Sk6v%2B8YF4ImdbvIzCi0PZ1SRoBogOZLemJ%2BdWqGSL6ekr8dEjnosn4ZGBptgNrAnMjSoiY2Pi%2FIAID29EJsQA9fHV3vSwQvZBXKDFEstYkoqW6jlErXWZVduA%2BX%2BUq4Vf4AnFmhWvWPp0mJkp8NhBT96vi7IY%2BVOnsxrxSOwD3m3Dv7bSDNamb7rwwXIIyGOuTiSnagKwpjANm4KIdDS6vNMuwrtDWaqDSZCRmcknZckSJXQA7tnkFkD0iwlWkZMCJ%2Bg7tV54AcNamQStHydIdHawGpJK%2FV%2FIG20ul%2BEKvEn7op6Sz9Lya7W2OBcHNAQV1eq0skwkrJrRCaBY9kfN7ucc0Xr%2FFnSFAe6wITZ668tZcv8gVZRTARwXuIZ2ydOmw2smYUj3UzZM8oPkqEhJNu5xb333S4EFbNjLRqFFo0Zwvmr3vfYDYlMqaxcn1em28QQqHef2vnLXG1eas%2BK4rusDCFzDruf%2FSBjqkAeFqYUw%2BV7fHqCaqYpiJqhtm1Z0Mo70ZF1%2FSVJeP%2BUgVcPiLA3pp0mOMeHuYv6Yl0VoYWNwb%2FbKlCOh%2BjFYohC55nUGAL731CFSon9bPsHOKZ4UpZa9FzgSd4WDro0jLQAGbh3ai27sCSHgFvW%2BB0hwvRd755dVKn%2FOhzh886u2HlTjcabnmpdpeBQ%2BVjPmwN%2FsY%2BX2wbkJ7LRhcCoIbf8Az%2FUm%2F&X-Amz-Signature=4b1ff19a2c53d4e8c0651dbe49208e08f6a19cbbe3da302999c142d6b19df730&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

同学们可以看到这个浏览器页面上多出了很多的服务，我们叫它 and points 那在这些服务上有大家认识的，比如叫 health check ，可能剩下的大家都不认识了。没关系，新同学见面，不要求认全，咱今天就认识一个新同学谁看排在最后面的这个 high streaks stream 接口，咱们把这行地址复制下来，然后打开新窗口。


咦同学们看到这里有一个 pin 命令在不停的旋转跳跃，它不停歇。这个拼命令是什么呢？咱可以把它理解成是一个 Matrix 这个 Matrix 它会在每隔一段很短的时间里去收集当前机器的 high strikes 调用信息，比如说熔断开关的开启或者关闭状态，或者你接口的调用失败率以及成功的概率。


咱看到这个浏览器上面有一个小叉说明什么？如果大家打开 inspect 面板，会发现这个请求是一个 get 请求。但是这个 get 请求是处于一个长连接的状态，它会不停地接收信息。

[image](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/73cb1e12-db79-4bb6-a7bd-a216da2cf997/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RS6RMOHK%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T225651Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDXYfg45UG3qDAQum3c6n5L3WTIvvXR1UtLYiqQr1z6MQIhAMxjguc1rZhmawmGuYTtCotzWv0JnAidI7qHSqY4HGWTKogECMb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1Igwl%2FofVqX%2BK7eF4dXAq3APNausNGmFvjYroRAGPTsVqDXSUOgPpjgNW5mcW2GhMAHsDutpH08HuyX2LJV6sm9TuhWNYJStkeKRNalS%2FoZCwDLiM9Tr6Z9qx2nam6g8py2WNuEiQzNIe8QIGt1IFptVkeUp4BApq%2F8omI4N8WLMPc%2BN7Deb948Sk6v%2B8YF4ImdbvIzCi0PZ1SRoBogOZLemJ%2BdWqGSL6ekr8dEjnosn4ZGBptgNrAnMjSoiY2Pi%2FIAID29EJsQA9fHV3vSwQvZBXKDFEstYkoqW6jlErXWZVduA%2BX%2BUq4Vf4AnFmhWvWPp0mJkp8NhBT96vi7IY%2BVOnsxrxSOwD3m3Dv7bSDNamb7rwwXIIyGOuTiSnagKwpjANm4KIdDS6vNMuwrtDWaqDSZCRmcknZckSJXQA7tnkFkD0iwlWkZMCJ%2Bg7tV54AcNamQStHydIdHawGpJK%2FV%2FIG20ul%2BEKvEn7op6Sz9Lya7W2OBcHNAQV1eq0skwkrJrRCaBY9kfN7ucc0Xr%2FFnSFAe6wITZ668tZcv8gVZRTARwXuIZ2ydOmw2smYUj3UzZM8oPkqEhJNu5xb333S4EFbNjLRqFFo0Zwvmr3vfYDYlMqaxcn1em28QQqHef2vnLXG1eas%2BK4rusDCFzDruf%2FSBjqkAeFqYUw%2BV7fHqCaqYpiJqhtm1Z0Mo70ZF1%2FSVJeP%2BUgVcPiLA3pp0mOMeHuYv6Yl0VoYWNwb%2FbKlCOh%2BjFYohC55nUGAL731CFSon9bPsHOKZ4UpZa9FzgSd4WDro0jLQAGbh3ai27sCSHgFvW%2BB0hwvRd755dVKn%2FOhzh886u2HlTjcabnmpdpeBQ%2BVjPmwN%2FsY%2BX2wbkJ7LRhcCoIbf8Az%2FUm%2F&X-Amz-Signature=9681b49c133772df50e11e79e93bc7fb84fce4d5d3b4eb69b7d4a874e2cc5676&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

所以说这个 pin 并不是每次都会发送一个新的请求，而是指它会在当前的这个连接下持续的传送信息。所以说它是建立一个连接持续传输数据的过程。这里怎么不刷新了，因为我前面点击叉号把这个链接中断了，咱现在让它刷新起来。然后这时候我们尝试调用一个方法，看看它的 pin 函数会发生什么样的变化。我们走到postman ，调用 high streaks fallback 接口中的一个必然触发降级的流程。好，我们发送出去。 OK 再回到页面上，同学们往下翻，会发现它这个 pin 返回的内容不同了，我们刷新一下界面好，然后点击叉把这个连接中断掉，密密麻麻的数字佳佳从这些数字中可以读出什么东西，我放大一点。


首先 name 是 service name 对不对？我们调用的方法的名称。然后这个 service name 远程调用的是哪个 endpoint 它是调用的 fin client 以及当前的时间戳和熔断开关的开启和关闭状态。后面跟着的就是失败率，失败的请求数量以及发送的请求数量等等各种信息。那这些信息留给谁用？还能有谁用？ turbine 呗。

[image](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/ee5cda7d-23c8-4964-b8f4-c010df119aac/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RS6RMOHK%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T225651Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDXYfg45UG3qDAQum3c6n5L3WTIvvXR1UtLYiqQr1z6MQIhAMxjguc1rZhmawmGuYTtCotzWv0JnAidI7qHSqY4HGWTKogECMb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1Igwl%2FofVqX%2BK7eF4dXAq3APNausNGmFvjYroRAGPTsVqDXSUOgPpjgNW5mcW2GhMAHsDutpH08HuyX2LJV6sm9TuhWNYJStkeKRNalS%2FoZCwDLiM9Tr6Z9qx2nam6g8py2WNuEiQzNIe8QIGt1IFptVkeUp4BApq%2F8omI4N8WLMPc%2BN7Deb948Sk6v%2B8YF4ImdbvIzCi0PZ1SRoBogOZLemJ%2BdWqGSL6ekr8dEjnosn4ZGBptgNrAnMjSoiY2Pi%2FIAID29EJsQA9fHV3vSwQvZBXKDFEstYkoqW6jlErXWZVduA%2BX%2BUq4Vf4AnFmhWvWPp0mJkp8NhBT96vi7IY%2BVOnsxrxSOwD3m3Dv7bSDNamb7rwwXIIyGOuTiSnagKwpjANm4KIdDS6vNMuwrtDWaqDSZCRmcknZckSJXQA7tnkFkD0iwlWkZMCJ%2Bg7tV54AcNamQStHydIdHawGpJK%2FV%2FIG20ul%2BEKvEn7op6Sz9Lya7W2OBcHNAQV1eq0skwkrJrRCaBY9kfN7ucc0Xr%2FFnSFAe6wITZ668tZcv8gVZRTARwXuIZ2ydOmw2smYUj3UzZM8oPkqEhJNu5xb333S4EFbNjLRqFFo0Zwvmr3vfYDYlMqaxcn1em28QQqHef2vnLXG1eas%2BK4rusDCFzDruf%2FSBjqkAeFqYUw%2BV7fHqCaqYpiJqhtm1Z0Mo70ZF1%2FSVJeP%2BUgVcPiLA3pp0mOMeHuYv6Yl0VoYWNwb%2FbKlCOh%2BjFYohC55nUGAL731CFSon9bPsHOKZ4UpZa9FzgSd4WDro0jLQAGbh3ai27sCSHgFvW%2BB0hwvRd755dVKn%2FOhzh886u2HlTjcabnmpdpeBQ%2BVjPmwN%2FsY%2BX2wbkJ7LRhcCoIbf8Az%2FUm%2F&X-Amz-Signature=935b60014c8e06c723e55147aa9edac50cd6886b6d20c8768a9bc0b2895b9dc4&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

好，那么这里就把 hystrix 抛下，不管啦，我们到 intellij 里面把 turbine 启动起来，看一看 turbine 是不是能获取到同样的信息。好，看到 spring 标签成功一半三二一起来了。 okay 好，turbine起来以后，我们到 eureka 的注册中心这里，刷新一下页面，发现已经有一个 high strikes turbine 注册上去了。好，这里是它的端口52,000。那我们打开一个 52,000 的浏览器端口，52,000后面跟什么呢？后面可不是 accurator 咯，那后面的路径叫 turbine.streamok 好激动人心的时刻，看看能不能获取到信息。


回车好完美。我们暂停这个请求，同学们在这个信息上是不是看到了似曾相识的内容？那这些信息来自于哪里呢？全部来自于各自应用通过 accurator 暴露出来的 hystrix 统计信息。所以从这个角度来说， turbine 它不生产数据，它只是数据的搬运工。


好了，同学们那这一节的内容到这里就快结束了，我来总结一下咱这一节了解了 high streaks 的一个好搭档 turbine 它用来收集 high strikes 的统计信息，它有这么几个要素。第一个，我们要搭建一个 turbine 的服务，在这个 turbine 的应用中，我们要指定需要监控哪些应用服务，并且在对应的应用服务中呢？开放 accurator 的 high streaks endpointok 同学们可以在自己本地尝试着搭建起这套应用。然后在下一节当中，我们将会介绍 high streaks 的另一个好搭档，也就是 high streaks dashboard 大盘监控，利用一个监控面板把所有 turbine 中的信息汇集起来，最终呈现在 UI 页面上。 OK 同学们，那这一节就到这里结束了，我们下一小节再见。




