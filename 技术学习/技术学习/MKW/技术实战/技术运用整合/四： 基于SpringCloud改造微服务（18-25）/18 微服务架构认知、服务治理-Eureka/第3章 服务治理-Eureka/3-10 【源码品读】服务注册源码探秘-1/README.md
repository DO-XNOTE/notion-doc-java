---
title: 3-10 【源码品读】服务注册源码探秘-1 
---

# 3-10 【源码品读】服务注册源码探秘-1 

[image](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/af2f39ff-97c9-4700-9943-dbf92f81665c/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466X3BN4432%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T225540Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIBIiC26C8OfkS8q1LVsv9Nlp5i7F9tyrgR7LP7Op9wcdAiByAQcQ4zrSqKvBTpEvHzVK33PoTsNB9FxRXerkXB4hSiqIBAjG%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMrvnbuo3eiH8eux2yKtwD2pUI%2FWTOGF0RVQqUlHl6rrezjb4uaFh1P%2FjtFmIgBf1jZtADIy96lQiY5lHR9eBXagRZZha0bwhZe9c3MOh2Z1%2BOz3wwiR3Cs%2BptUVcb0xlv6%2FoM5uxyCM2sPndudp3c3HuTsPh20puVSDnhQi%2Be2cjNLcP23xqPJL%2FplYmGWKj8P3TESRcthHYy1JpZbD2O6F5PU2kivqjGGlHXez9N2f7%2Bq52sggNoo24ivG0yZKz2Cbmd7phtCfdkr0U%2FMMTEORG5aHIJah%2FOcuPHdk8knFtTNvr2OTCQaX%2Fcs3fxgb0Dokoo6PAhwbNdr%2BkVHtWi5J2CMV3st3OXzKAKJRLyvTFjwRTmI%2FvkOa1sx%2FlXrqvg4KS5wygaYtEEskZvoJKP7AiZlDFY8Bn8gBTnDoMASSSTYDhGQEHQgefl4Od8VR1vHTRRftDr72hI3wo7gUbWlxo1y5yXJJVDXRYDjo%2BPjgebsIYV4JWTxmqdwDGlI0LZpjwoWHxbi%2FZZfx4UorJ%2Bk9qbDrkV4p1pL7HxAhf0EQUTphsZ6pRT9aQX0%2BikZ32e9TvjRmDLc%2FlssR7yXi6QSbsP8WE9OgkWvUB%2FyjzOJj8SLltkz%2Bhupal%2FFCwRXlUIKB5LbAht9ZIgNbow8rr%2F0gY6pgG1mqCsQGuyn%2Fi%2FgYFzIfjoGZTNyvbNgM%2F2M10GmR0ZdZMgMpBl1oZyGMw%2FKRu%2FBwvj4gLi80IAHeLtPP44t2BrLNdTeg55MLR6%2BQxFmJaE5RClDZ%2Bd3S9z6q%2BrTVdaLQA5lGjGIXgKlBx8SQkQGiY9JBIoQdjeqmRlOz3dbwHSC7hu%2BfWipWbSCIBluOM4ZbIgZEP9UKRqNacqjHFHMYpcYlVtpIdV&X-Amz-Signature=a118a4f01af7e3faed593d924300edf38ef7545cfcaf87fb218d2195aad7dbaf&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

[image](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/98c1ed06-cbe6-4e2e-973b-943b8586439b/SCR-20240717-dlmq.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466X3BN4432%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T225540Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIBIiC26C8OfkS8q1LVsv9Nlp5i7F9tyrgR7LP7Op9wcdAiByAQcQ4zrSqKvBTpEvHzVK33PoTsNB9FxRXerkXB4hSiqIBAjG%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMrvnbuo3eiH8eux2yKtwD2pUI%2FWTOGF0RVQqUlHl6rrezjb4uaFh1P%2FjtFmIgBf1jZtADIy96lQiY5lHR9eBXagRZZha0bwhZe9c3MOh2Z1%2BOz3wwiR3Cs%2BptUVcb0xlv6%2FoM5uxyCM2sPndudp3c3HuTsPh20puVSDnhQi%2Be2cjNLcP23xqPJL%2FplYmGWKj8P3TESRcthHYy1JpZbD2O6F5PU2kivqjGGlHXez9N2f7%2Bq52sggNoo24ivG0yZKz2Cbmd7phtCfdkr0U%2FMMTEORG5aHIJah%2FOcuPHdk8knFtTNvr2OTCQaX%2Fcs3fxgb0Dokoo6PAhwbNdr%2BkVHtWi5J2CMV3st3OXzKAKJRLyvTFjwRTmI%2FvkOa1sx%2FlXrqvg4KS5wygaYtEEskZvoJKP7AiZlDFY8Bn8gBTnDoMASSSTYDhGQEHQgefl4Od8VR1vHTRRftDr72hI3wo7gUbWlxo1y5yXJJVDXRYDjo%2BPjgebsIYV4JWTxmqdwDGlI0LZpjwoWHxbi%2FZZfx4UorJ%2Bk9qbDrkV4p1pL7HxAhf0EQUTphsZ6pRT9aQX0%2BikZ32e9TvjRmDLc%2FlssR7yXi6QSbsP8WE9OgkWvUB%2FyjzOJj8SLltkz%2Bhupal%2FFCwRXlUIKB5LbAht9ZIgNbow8rr%2F0gY6pgG1mqCsQGuyn%2Fi%2FgYFzIfjoGZTNyvbNgM%2F2M10GmR0ZdZMgMpBl1oZyGMw%2FKRu%2FBwvj4gLi80IAHeLtPP44t2BrLNdTeg55MLR6%2BQxFmJaE5RClDZ%2Bd3S9z6q%2BrTVdaLQA5lGjGIXgKlBx8SQkQGiY9JBIoQdjeqmRlOz3dbwHSC7hu%2BfWipWbSCIBluOM4ZbIgZEP9UKRqNacqjHFHMYpcYlVtpIdV&X-Amz-Signature=dbc1fc4b7ad3d9214e8c4268fadb27974c62bfb52a8bd611f92449c1e0330366&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

一节我来带大家到服务注册的源码中进行秘境探秘。那本节的主要内容有一个注解引发的血案，我们来看一看 eureka 是怎么通过一个注解把整个架构启动起来的，看一看这个悬案的现场。第二个， A 代理模式，装饰器模式，傻傻分不清楚。那这两个模式是什么？为什么我们偏偏介绍这两个模式，因为它们都在服务注册的源码中有所应用，所以这里我们把它拎出来，单独介绍一下。第三点，我们看一下服务注册都注册哪些内容。然后通过 debug 手段，从头到尾把整个链路给走一遍。

[image](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/e40036cd-0529-47b3-8b5c-cbe978c7b789/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466X3BN4432%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T225540Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIBIiC26C8OfkS8q1LVsv9Nlp5i7F9tyrgR7LP7Op9wcdAiByAQcQ4zrSqKvBTpEvHzVK33PoTsNB9FxRXerkXB4hSiqIBAjG%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMrvnbuo3eiH8eux2yKtwD2pUI%2FWTOGF0RVQqUlHl6rrezjb4uaFh1P%2FjtFmIgBf1jZtADIy96lQiY5lHR9eBXagRZZha0bwhZe9c3MOh2Z1%2BOz3wwiR3Cs%2BptUVcb0xlv6%2FoM5uxyCM2sPndudp3c3HuTsPh20puVSDnhQi%2Be2cjNLcP23xqPJL%2FplYmGWKj8P3TESRcthHYy1JpZbD2O6F5PU2kivqjGGlHXez9N2f7%2Bq52sggNoo24ivG0yZKz2Cbmd7phtCfdkr0U%2FMMTEORG5aHIJah%2FOcuPHdk8knFtTNvr2OTCQaX%2Fcs3fxgb0Dokoo6PAhwbNdr%2BkVHtWi5J2CMV3st3OXzKAKJRLyvTFjwRTmI%2FvkOa1sx%2FlXrqvg4KS5wygaYtEEskZvoJKP7AiZlDFY8Bn8gBTnDoMASSSTYDhGQEHQgefl4Od8VR1vHTRRftDr72hI3wo7gUbWlxo1y5yXJJVDXRYDjo%2BPjgebsIYV4JWTxmqdwDGlI0LZpjwoWHxbi%2FZZfx4UorJ%2Bk9qbDrkV4p1pL7HxAhf0EQUTphsZ6pRT9aQX0%2BikZ32e9TvjRmDLc%2FlssR7yXi6QSbsP8WE9OgkWvUB%2FyjzOJj8SLltkz%2Bhupal%2FFCwRXlUIKB5LbAht9ZIgNbow8rr%2F0gY6pgG1mqCsQGuyn%2Fi%2FgYFzIfjoGZTNyvbNgM%2F2M10GmR0ZdZMgMpBl1oZyGMw%2FKRu%2FBwvj4gLi80IAHeLtPP44t2BrLNdTeg55MLR6%2BQxFmJaE5RClDZ%2Bd3S9z6q%2BrTVdaLQA5lGjGIXgKlBx8SQkQGiY9JBIoQdjeqmRlOz3dbwHSC7hu%2BfWipWbSCIBluOM4ZbIgZEP9UKRqNacqjHFHMYpcYlVtpIdV&X-Amz-Signature=fa1ea5d921364e509c9461fbd602f28a17497a7c8499fa984cdeb2e6b3c264d0&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

好，准备好了就抄起家伙开拔去吧。每天 poding 1 小时，健康工作 50 年，又来到了主场 intellij 好，下面我们干什么？是不是看一下这个注解引发的血案？我说这圆起圆灭都是因为这一个小注解，一个注解能掀起多大了？这里带大家一起去看一下注解在哪里。有瑞卡克兰特下面的那函数对不对？ OK 我们把它打开。看到这里好像没什么文章，对不对？就挂着一个 enable discovery client 注解。那像这种表面上不起眼这个背后故事肯定不简单，点进去看看里面有什么东西。好，我们放大页面点进来。发现一个叫 auto register 的方法，它的默认值是什么？是 true 对不对？自动装配，那是打开的状态，默认这就没了吗？这就引发什么血案啦。


你看这个作案现场好像还留了一行字，对不对？他解释说如果是 true 的话，后面这个 service registry 会自动的注册 local serverlocal server 是谁，就是当前我们这台 instance 对不对？那感觉看上去线索也不够，那我们要找找看其他线索往上滚。 AA 停打住。这里有个 import 它导入了什么东西，好像有点可疑。你看这名字还非常长。


enable discovery client import selector 那我们啊点进去看一下哟。呵，你看别有洞天豁然开朗，看到没有？那线索进一步明了，继续之前我来跟大家分享一点小插曲，就是我这个人本人学习技术的过程是比较虐心的什么意思啊？就是说我学习一个新技术的时候，


**我不去网上找一些 sample 也就是样例来看，我是到官方的开源网站里找一个开头。那什么是开头呢？比如说尤瑞卡，那我们在这个闷方法上的这个注解就是一个开头。对不对？我只知道这样一个开头。**


好了，我就此打住，我不再看剩下的 sample 我通过怎么样选形式学习，我自己摸索**，我把整个链路给摸索清楚。那这个过程是不是非常虐心对不对？我这里并不是说让大家也这么虐心，我这么错主要是有一个原因，因为我太闲了对不对？**开玩笑，其实大家也可以尝试，部分采用我这种摸索的方式。
比如说你们用了几年的 spring 对不对？


那很多人可能只知道怎么用，压根没有研究过源码，那你怎么知道它的底层是怎么运行的？大家都到网上搜资料看面试宝典是不是？那我跟大家讲面试宝典，看到那些问题，你只能忽悠住神，同样不研究源码的这些面试官对吧？你比如说我自己面试别人，我只要看到谁简历上写了这样几个字，精通 spring cloud 他只要这样写了，反正我面到现在还没有让其一个人通过，他还不如写精通。


所以言归正传，我今天就要用我这种方式带大家虐心一把，我们进到这个类里面。接下来怎么办？最快的一个清理线索的手段是什么？是 debug 对不对？那我们虐心也要讲究方式方法 debug 大家看到这里有一个小红色的光圈，这个就是 debug 的断点，我们在这个 select import 上面打上一个断点，因为到这类里面线索几乎就中断了，我们通过断点最快的找到下一个线索。


OK 接下来打完断点。我们要把这个服务注册中心给它启动起来，到尤瑞卡 server 里直接点击 run 这里，把注册中心先跑起来，还注册中心再到 eureka client 服务提供者的门房处理这里我们怎么跑？我们不用 run 了，我们要 debug 对不对？这样才能打到我的断点里面。好走起，看待会是不是能到断点中。好勒到断点里面了。我们收起小桌板来。


段田你看一下这都是什么内容，先看它的入参这个 metadata 是什么。这个 metadata 就是挂在我们闷函数上的一个修饰符，看它里面都有什么内容。这个字比较小。我跟大家读一下，这个 metadata 里面主要的一个内容是 annotation 它有两个，一个是 spring boot application 一个是 enable eureka client 那大家知道这两个都是什么，都是在闷函数里我们挂的两个注解对不对？那接下来往下走。这个 attributes 获得什么？它会获得我们的 enable eureka client discovery client 这个注解。
进一步获得注解以后，下面的方法是从这个注解中读取 auto register 这个属性。 OK 继续往后 auto register 的值是 true 那这个 if 条件就要进去了，再往下。看到这里，大家发现有进一步线索了，对不对？它这个 imports list 它需要导入什么？导入一个手工注入的一个类。那这个类叫什么？
Auto service registration configuration.


看到是一个配置类，那虽然没有接近最后的真相，但是我们离真相又近了一步。把这个累的名字记住，待会我们秋后算账。好，这里继续。往下没了，往下 return 了。好，那我们现在就来秋后算账号了，进到这个类里瞧一瞧，看一看看你有什么进一步的线索。空空如也是不是，那就奇怪了，我们要到他的 annotation 上面再找线索了。


这里看到有一个 enable configuration properties 它要读取属性对不对？读取 properties 那这里我们到这个类里面看一下它都读取哪些属性。从这上面看到它读取了以什么打头的这个 spring cloud service registry outer registration 自动注册。那我们得联想一下，因为这种虐心的方式也要靠一些联想。我们联想你一个应用启动的时候都要自动注册，对不对？那你这个属性肯定多多少少跟自动注册是有关系的。那接下来看这个属性后面还跟着哪些子属性，由 enabled 是否开启 register management feel fast okay 那我猜想这个属性一定会在某些配置项加载的流程中被应用到。
好，我就尝试着去找一下它的引用，看一下哪些类会引用它。 A 我这找了一圈，你看很多类都会引用它对不对？那接下来我挑一个类，因为我现在还不知道究竟是在哪个类中调用它的。因为我们很多方法它的抽象层都会定义在 abstract 里面。所以我一般看到这种情况，我会先到 abstract 里面找一找线索。


那既然这里 abstract auto service registration 这个类也引用到造的这个 property 点进去，我们来一探究竟。好看他在哪里引用到的？在一个初始化流程中引用到的，它怎么引用啊？它这里好像把 properties 注入到了哪里当前的属性当中。对不对？那这一步没什么平淡无奇。但是它关联的一方，它上一行七十七行这里看起来是有蹊跷，对不对？它注入了一个 service registry 服务注册。看到这里怎么眼前一亮，对不对？我们看一下这个服务注册这个类，点进去。发现它是个 interface 那 interface 一定有自己的实现类，我们到实现类里找一下。好，这里点进去，因为 intelligent 同学都比较熟悉，怎么找实现类？用 eclipse 是 ctrl 加 T 应该刚才这个 interface 方法它只有一个实现类，那就是 eureka server registry 看到吗？在这个实现类上面得来全不费工夫。


我看到了一个很可疑的方法是什么 register 那就是注册了对不对？好，那我这样我尝试着在这边打一个断点，看他的方法能不能进来好不好？ OK 前面我们已经抓住了一个断点，那我把这个断点放掉来，我把它放掉，看它会不会进到 regist 那个方法里。没有动静。好勒，再放掉。进到过来了。那既然她过来了以后，我们就来挨个读一下这个 register 里面都有什么内容。


第一步，这个方法叫什么？叫 maybe initialize client 这个名字叫的好像有点虚，是不是我们点点进去看一下。好了，他做什么事。他上面有一行注解叫 force initialization 就强制的初始化一些代理。那我看你强制初始化的什么内容，这有个 get info 这样子，是资源的一些预加载，看你 get info 里面有个 instance info 那好，我进去看一下。好了，这个 instance info 是什么内容 A 过来了，我点开 expression 这个面板，字比较小，我跟大家逐行的念几个主要的属性。


好了，在 instance info 里面打投的是什么？一个叫 instance ID 的东西，他什么？我看他的 IP 地址好像当前机器，然后端口是 3 万。这不就是我们当前这个服务提供者对不对？再看它 App name eureka client 也是服务提供者。 IP address 也是当前的机器，还有 homepage URL 还有 health check URL。这个分明是什么？分明就是我要向服务中心注册的东西是不是我的自报家门，我自己的信息个人简介。那我明白了，这个 instance info 好像就是要向注册中心发送的东西，我心里有底了。好，那就直接接下来我们回退上一层，放开断点到上一层这里。 OK 这个 get App 我们就不看了。小支线剧情我们，再往上走。刚才看了没？ B 方法，那我们接下来在方法下面继续走断点走，这两个 log 我们先忽略过去。


好，这里看到了一行是做什么的？ Set instance status. instance status 是什么？是我们在注册中心页面上看到服务的状态，大家还记得有 up 有 down 这些服务状态对不对？那我看一下这里 instance 是什么？看到吧。这个 name 是 up 那就是说我服务注册的时候，我发送的这个状态是个 up 接下来是什么？ health check OK 那我们这里不管了。


好勒，大家知道，接下来我们寻找线索怎么寻找吗？我们断点断到了 register 对不对？但是它并没有向服务注册中心发送请求，正好看起来好像不是最终请求发起的地方。那我怎么知道它的上一层是什么呢？这里就是通过 debug 站，我就可以很轻松的知道上一层谁调用它的。 OK 我们这里往上找，就在它的第二行。这个类的名字叫什么？


Enable auto service registration.
这个类好像更接近真相，我们点进来看它是在哪一行调用到的？看到这一行蓝色的行吗？它是在这里调用到的 service registry DN register 但是这个 register 并没有发起服务调用，这看起来就有点奇怪了，那服务调用一定发生在它后面的地方是不是？好，那我们在这里打一个断点好了，看他会不会走到这往下走了一行，断点果然到了这里。


那这一句看起来就有些蹊跷，为什么呢？它往上下文中 publish 的一个 event 这是什么含义啊？就发布了一个事件对不对？它什么事件？ instance registered event 你还没有注册，你就发布一个已注册的事件吗？好像不对，那我们再来看一下它的这个参数是什么？ registration.get instance config 那我这里把它打开一下，随便浏览几个属性我这里又看到了 instance ID 还有 host nameap B name 等等。那这些确确实实真的是要注册的东西。那我可以这样猜想对不对？我猜想一下，这个 event 发布了以后，在 spring 的上下文中肯定会有一些流程响应这个 event 发布，从而真正发起一个服务注册。接下来往下去一行。我们看到他这里往 spring 的上下文中发布了一个事件，这个 context 就是上下文 application context 它发布了一个什么事件叫什么？ instance registered inven 是说 instant 往下走一行。


好，到了这里是一个什么方法？ publish event 发布了一个世界，它往哪里发布的？这个 context 是什么？ application context 就是我们 spring 的上下文，它发布了一个什么事件叫 instance registered event 说它的 instance 已注册。那我们先到这个注册中心的页面看一下，我刷新一下，两万两万端口刷新。你看 application 里面没有应用对不对？那说明他还没有注册，但是在这一步他却将要发布一个已注册的 event 那说明什么？说明在这个 event 发布之前和 event 发布之后肯定发生了什么事？让 eurika 的服务提供者向注册中心发送的请求。那既然你看，这个 event 发布之后这个 running 的状态就变成了 true 那说明确实应该是运行起来了。


OK 大家，这里有一个小任务什么呢？利用前面我们的一些 debug 手段，大家自己找一下这个 publish event 跟下接下来的一个步骤是怎么衔接上的。那我这里，因为时间关系，我就不 demo 这个流程了，我直接跟大家做一个剧透。


好了，你看下一个流程是在哪？是在一个叫 discovery client 我们在图文的教程里面也说过这个 discovery client 相当于一个什么相当于一个 facade 类型的类，对不对？它封装了我们服务的 client 和注册中心之间的各种交互。 OK 我们看一下它都有什么方法 renew register 什么都有。那这里我们先到一个叫 register 的方法里，放开断点看他是不是到了 register 里。接下来我们打开 debugger 看一看它的调用栈前面不是说过同学们研究 publish event 之后的通路对不对？这里就可以顺着这个调用栈把这个调用关系捋清楚，你看它粗略的看一下，它是从一个 thread pool 里面定时启动的。对不对？一个 future task 好，我们这里先不多管前面的章节，这里往后继续。好勒。那走到这里，它这应该是一个正儿八经的 register 方法。通过这个 residuster 方法以后就完成了服务调用了对不对？但它不是这么简单的一层。


我们先看一下是由哪个类发起的 register 好不好？我们把这一段复制下来，打开 expression 看一下这里再点 get class 好，我这里盖了一下 class 它是从哪个类发出来，有个叫 stationed eureka HD TB client 那我明白了。好，那我就去找这个类。好了，我们打上 session 这正好跳出来了。 OK 他是到这个类中的哪个方法？ register 是不是？那我寻找一下 register 发现它在这里。这个类跟刚才那个类不一样，它叫什么名字？ eureka HTTP client decorator 说明什么？说明刚才我们进入了那个类中的 register 方法，在这个顶层的抽象类中。


那我们再来看这个 register 直接打 register 好我们进入进来看它是一个 execute 的方法执行的。那这个 execute 方法在哪？就在它上头对不对？它上头发现它是一个 abstract 一个抽象类。那就是说每个子类肯定都实现了一套 execute 的方法。


而 execute 方法的参数是哪里传入的？是它在顶层负层类里传入的这个参数对不对？那这里传入了一个什么东西，传入了一个 delegatedelegate 是什么？是代理？对不对？那他使用代理来进行了一个注册。这个方式蛮巧妙的对不对？你看通过一个子类实现的 xq 的方法，然后参数是由父类传入的一个代理，那非常绕人。



