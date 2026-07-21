---
title: 3-16 定时任务通用组件封装-1
---

# 3-16 定时任务通用组件封装-1

[image](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/8a62e472-4dd4-46ec-a03c-a5b09cd43468/SCR-20240806-svpv.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466Q2PA2ZWP%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T225308Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQD6GTRxeU6QCJRzCpiARuDvgQj3H6vKSxChqeZpaLqBzgIgc4FWHDINGeSCq0dASAJLh1s0f0kh8EmaEVf7ZR9NVA8qiAQIxv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDLqd9%2BsLv6u3hBgeAircAwk8PlqA8wADf33aM7FwbWKHZnA0LdB6kDYI2sGgcRK6sLAHiJPbbNxe4%2BJVPJVoVPHIjGrFF1bOH1KYuoeDQxOQ9s2MU819lMSVNUi0m%2BBUnJv75%2Fi%2FNBKykqyToy85shp%2BRlEjXVIFezCrgukqgsKzyP9JGUW0uQTq%2FYCBYuhSmM0g1O8EQXmOuY6b6iYbJW5blVcgcAbIyT79SQQKIt03s01ZTp%2BcwmR54oGHkZWg5WquG9HskyfzD0gGzPVIcL1rbMvVbUB6Wtw7J79dzwQLLuJ563yfZ%2B938jexO%2BIqnU1VnVJrMjlPyA2ibCfOtMhS%2F%2FXpRrcOqFAeU7ZVDTzv%2FGUbGs2D7etixNtQZR%2BVr7RkEISAAk4VG8xSH636tDPu%2B3fDKvPdZW2lsLRqXx53%2Bnt%2BA3vAJZGlXTi5SkyTqz7xVtDEO5U4mYfpgOEbrpOh4v3NgJM3ErgJP4JMr1uborgJBpthwAgYqrW0lqejMQWxT7dFI6YxhSoRzSwkd7oMZzMztwHixkFF3hiqElolKS0RvS%2BwHyzeKuH92TlRLB%2B2BwWhUQ1u0RFtZdN8NwZB1b9insj6nqKCy8Fc5caZU3pXhORPxS6FhJCKu21BgmA0W9NqUGRy3H2HMJa7%2F9IGOqUBeV%2BzNplZO%2FvAIqpzgjQO4aHedVhTY%2F%2F1gGUAwDP7XJBhAzpwmqnKBbKIrfZR37r87wQ1xHJa%2Fg1K7hB71CHlnD2vfafsjwAymaOrzQRC9Jv7VTepJFdn6qV8iIXYGiP6QIXpO%2Fd8jpgHkS%2BI8uOUKvZg5SGcUh3kBkJzzipcfdl6hPTZnVr0srDGCnq09YfP8G%2FXiRRkt9PcGYvTBVec8bWU2ilZ&X-Amz-Signature=50746c914757acb0a8c2f93c6bc62e9e480fcbd026329b3bc30937e234d61bdf&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

[image](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/7c30d454-f79a-4a2f-85f3-05d20f815e47/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466Q2PA2ZWP%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T225308Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQD6GTRxeU6QCJRzCpiARuDvgQj3H6vKSxChqeZpaLqBzgIgc4FWHDINGeSCq0dASAJLh1s0f0kh8EmaEVf7ZR9NVA8qiAQIxv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDLqd9%2BsLv6u3hBgeAircAwk8PlqA8wADf33aM7FwbWKHZnA0LdB6kDYI2sGgcRK6sLAHiJPbbNxe4%2BJVPJVoVPHIjGrFF1bOH1KYuoeDQxOQ9s2MU819lMSVNUi0m%2BBUnJv75%2Fi%2FNBKykqyToy85shp%2BRlEjXVIFezCrgukqgsKzyP9JGUW0uQTq%2FYCBYuhSmM0g1O8EQXmOuY6b6iYbJW5blVcgcAbIyT79SQQKIt03s01ZTp%2BcwmR54oGHkZWg5WquG9HskyfzD0gGzPVIcL1rbMvVbUB6Wtw7J79dzwQLLuJ563yfZ%2B938jexO%2BIqnU1VnVJrMjlPyA2ibCfOtMhS%2F%2FXpRrcOqFAeU7ZVDTzv%2FGUbGs2D7etixNtQZR%2BVr7RkEISAAk4VG8xSH636tDPu%2B3fDKvPdZW2lsLRqXx53%2Bnt%2BA3vAJZGlXTi5SkyTqz7xVtDEO5U4mYfpgOEbrpOh4v3NgJM3ErgJP4JMr1uborgJBpthwAgYqrW0lqejMQWxT7dFI6YxhSoRzSwkd7oMZzMztwHixkFF3hiqElolKS0RvS%2BwHyzeKuH92TlRLB%2B2BwWhUQ1u0RFtZdN8NwZB1b9insj6nqKCy8Fc5caZU3pXhORPxS6FhJCKu21BgmA0W9NqUGRy3H2HMJa7%2F9IGOqUBeV%2BzNplZO%2FvAIqpzgjQO4aHedVhTY%2F%2F1gGUAwDP7XJBhAzpwmqnKBbKIrfZR37r87wQ1xHJa%2Fg1K7hB71CHlnD2vfafsjwAymaOrzQRC9Jv7VTepJFdn6qV8iIXYGiP6QIXpO%2Fd8jpgHkS%2BI8uOUKvZg5SGcUh3kBkJzzipcfdl6hPTZnVr0srDGCnq09YfP8G%2FXiRRkt9PcGYvTBVec8bWU2ilZ&X-Amz-Signature=d936ec9ef8e014a50cd97585ad1d4c5a6461fa3849b2adbfad37f1019cfe6a22&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

[image](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/7fa3b34a-c478-40c2-a679-23e4df3f0358/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466Q2PA2ZWP%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T225308Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQD6GTRxeU6QCJRzCpiARuDvgQj3H6vKSxChqeZpaLqBzgIgc4FWHDINGeSCq0dASAJLh1s0f0kh8EmaEVf7ZR9NVA8qiAQIxv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDLqd9%2BsLv6u3hBgeAircAwk8PlqA8wADf33aM7FwbWKHZnA0LdB6kDYI2sGgcRK6sLAHiJPbbNxe4%2BJVPJVoVPHIjGrFF1bOH1KYuoeDQxOQ9s2MU819lMSVNUi0m%2BBUnJv75%2Fi%2FNBKykqyToy85shp%2BRlEjXVIFezCrgukqgsKzyP9JGUW0uQTq%2FYCBYuhSmM0g1O8EQXmOuY6b6iYbJW5blVcgcAbIyT79SQQKIt03s01ZTp%2BcwmR54oGHkZWg5WquG9HskyfzD0gGzPVIcL1rbMvVbUB6Wtw7J79dzwQLLuJ563yfZ%2B938jexO%2BIqnU1VnVJrMjlPyA2ibCfOtMhS%2F%2FXpRrcOqFAeU7ZVDTzv%2FGUbGs2D7etixNtQZR%2BVr7RkEISAAk4VG8xSH636tDPu%2B3fDKvPdZW2lsLRqXx53%2Bnt%2BA3vAJZGlXTi5SkyTqz7xVtDEO5U4mYfpgOEbrpOh4v3NgJM3ErgJP4JMr1uborgJBpthwAgYqrW0lqejMQWxT7dFI6YxhSoRzSwkd7oMZzMztwHixkFF3hiqElolKS0RvS%2BwHyzeKuH92TlRLB%2B2BwWhUQ1u0RFtZdN8NwZB1b9insj6nqKCy8Fc5caZU3pXhORPxS6FhJCKu21BgmA0W9NqUGRy3H2HMJa7%2F9IGOqUBeV%2BzNplZO%2FvAIqpzgjQO4aHedVhTY%2F%2F1gGUAwDP7XJBhAzpwmqnKBbKIrfZR37r87wQ1xHJa%2Fg1K7hB71CHlnD2vfafsjwAymaOrzQRC9Jv7VTepJFdn6qV8iIXYGiP6QIXpO%2Fd8jpgHkS%2BI8uOUKvZg5SGcUh3kBkJzzipcfdl6hPTZnVr0srDGCnq09YfP8G%2FXiRRkt9PcGYvTBVec8bWU2ilZ&X-Amz-Signature=18f5deb14443287ddd052f9b5f8c5b82fc691d9e5d696e44288f9e092e443fc2&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

**那么这节课我们继续往下去讲，上两节课我们已经对这个 ES job 进行了一个简单的学习和了解，那相信大家对这个 ES job 的基本使用已经没什么太大问题，那接下来我们要做什么事情？接下来其实我们要对 ES job 再做一层更好的这个封装，那为什么这么去做？因为我们现在整个的这一大章节课主要就是去做一些基础组件的封装。**


**那么像这种 ES job 的话，我们如果说单独的去按照我们之前的这种方式跟 SpringBoot 进行集成的方式去写的话，那我觉得其实是相对来讲有点麻烦。为什么呢？比如说每次有一个新的 job 的话，首先这个配置是必须要有的，然后放到这个 application 点 practice 里，然后还有麻烦的事情是什么呢？可能如果你每次有一个新的job，你肯定自己要做什么呢？当然 registry center 我们可以不用去写这个，注册一遍就好了。**


**它有一个问题，就是比如说我们的这个 my simple job config，你肯定要写一个configuration，然后把这个相关的需要有眼的依赖把它这个注入进来， out where 进来，然后包括这些配置看见了，比如说我们的这个 job schedule 这些配置，以及这个 let job configuration 包括往下的其实还有一个什么？还有一个这个 simple job configuration，或者是 data flow job configuration 等等，你可能都需要去做一些编码，都需要做一些配置，就是说你每创建一个job，就这些都是固定的模式化的东西，那这个是不是感觉比较麻烦？我们能不能自己再做一层封装，把它变成什么呢？把它变成类似于我们像 spring boot 比较友好的方式，然后能够帮我们去把它集成进来。 **


**然后我们可以通过比如说自定义注解的方式，在指定的类上写一个注解，然后具体你要配什么，那你就直接把你自己原先 properties 里边的东西去配置到初级里边，然后它就可以在项目启动的时候帮你去动态的去生成对应的。像这些config，就是这些代码相当于我们都想要动态生成，而不是想要说每次加一个 job 我都要把这东西写一遍。**


**OK，那其实接下来我们要做这件事情，那回忆一下，那我们再去使用这个 spring 做一个这个扩展的时候，最常用的方式就是一些什么 out where 的自动装配，或者是嗯， module Ware 的模块装配。那可能大家对 auto Ware 的理解的比较多，比如说我们正常的去，像我们之前就这种方式就是 auto configure，这种方式就是一个自动装配，那其实模块装配其实也是按照奥拓 config 去做的，但是它有一点点小的区别。**


那有同学说老师什么是模块装配？很简单，之前我们去用spring，比如说我们的 spring MVC 跟 spring 整合的时候，是不是得用什么 enable MVC？然后比如说你的定时任务想去整合到 spring 里的话，你是不是写，比如说 enable 你的这个 scheduler，或者 enable a single，或者是你有一些什么对应的 spring 跟一些重试模板进行集成的话，肯定要去要 enable 我们的这个retry。


**比如说我们就采用这种模块装配的方式，就把一个模块整体引到我们的 Spring 工程里，然后我们通过几个自定义注解就把那个事情完成了，现在开始去对我们的这个 ES job 跟 spring 再进行一次封装**。首先我们已经准备好了包了，就是我们的 rabbit 杠task，然后这个 Pom 文件其实老师已经准备好了，我们来看一下，我来打开，那目前我现在用的是 ES job 二点一点四，这没什么可说的，然后它引入了几个dependency，就是我们的 springboot starter 以及对应的 ES job 的就是相当于它的这个 API  jar 包。然后再往下就是我们的 configuration processor 了，有了这几个基础的类，那我们就可以在这几个依赖的包的基础之上去做我们的代码编写了。


首先我们来看一看第一步应该怎么去做，很明显我们可以继续去按照之前的这个自动装配的方式把它配置一下，我们叫做COM，点 BFX y，点Rabbit，点 task okay task。然后我们现在第一件事情肯定是要有一个这个凹凸configure，所以说前面的步骤其实是一样的，我们还要有一个凹凸 config 这么一个类，OK，那这个 auto config 类呢？我们可以给它起个名字，在这里我们比如说叫做 job Caser auto config，就是解析 ES job 的这么一个配置类，那我们在这里或者Parser，然后 auto config ration auto configuration 好了。


那么有了这个类之后，那这个类同学们想一想他要做什么事情？一样的，第一件事情肯定得是做一个consideration，这是必须要有的，因为你 spring 的自动装配这是必须要有的。然后这个类我们自动装配怎么去解析？很明显我们要在我们的这个就是 class pass 下面建一个border，就是 m e t a info，这是必须要有的。然后还会有一个对应的 factory 文件，这个我们去上面去找，我也懒得去写了，就他把它 copy 进来，然后只不过这里边的对应的这个类名我们要变一下了，这个类名我们叫什么呀？我们叫做 task Com，点 b f u s y，点rabbit，点task，点 auto configure 这个名字我怕写错了，已经把它粘过来 auto config，然后把这个类写上，OK，就是我们的 job Parser auto configuration。那这样的话，我们把这个 task 包引到我们的 producer 里边的时候，它就会自动的去找到这个文件，然后帮我们去把这个 configuration 声明的这个 job passer auto configuration 去做相关的自己的这个初始化，或者是其他操作。


好了之后，大家记不记得这个主角？或者说你有没有了解过这个主角叫做candidation，对于这个 conditional 它其实有好多对应的方式，比如说 conditional on bin， conditional on class， conditional code platform，然后等等， expression 等等等等。还有 conditional on Java， conditional on missing class，还有 on missing theater bin 等等，还有 on practice，还有 on property 斯和 on property 都有，那这些是为了干什么呢？这些其实就是一个条件，就是说什么情况下我会帮你去加载这个 auto configuration 这个类，那如果你不加这个，他默认就帮你加载了。


但是说有些情况我可能不会帮你去加载这个类，那这个时候就要做一个条件声明，一般大家最常用的就是 conditional on property，为什么呢？因为我们一般都是在配置文件里配置的那个东西，我说你只要配置一些对应的内容，那我就帮你去加载这个我对应的这个类好了。


那在这里呢，我们说在我们 ES job 什么情况下它会启动呢？首先第一点，我们回过头来，我们看一下我们之前的这个 ES job 对应的，看它的purpose，这些 job 我们到时候都用注解方式去做了。但是有一些固定的配置是必须要有的，比如说 ES 照膜，它是强依赖于我们 CK 的，如果你没有ZK，我是不是就不应该帮你配置，对不对？只要你有ZK，那我才可以说帮你去配置。


所以说在这里边其实我们可以这么去来，我先给它起一个前缀叫做prefixed，我说你必须要有 electric 点job，点 z k，这个 z k，我们直接就配这个前缀就好了，就是说你必须有这个前缀还没完，然后必须要有一个具体的属性才可以，对不对？我说你必须有几个属性，其实这里面就两个属性，为什么我这么说，其实还是我们看自己之前的job，也就是说我们之前的 ES job，像这些都可以是可配可不配的。还有默认值的，比如说 connection time out 啊， session time out 以及 Max retrace，OK，就是最大城市次数。那也就是说这两个东西是必须要有的，比如说你必须告诉我 JK 地址和 name space。


好了，那我们这样去来写吧，我们必须要有一个叫做 name space，这个就是声明我们的这个 ES job，它的这个就是根节点在 ZK 上的，然后在这里我给他起个名字，跟我们官方表保持一致叫做 server list。也就是说你的这个以前缀以这个为前缀，点 name space，点 server list，就是这两个配置项必须有，那只有这两个配置项必须有的情况下，我才会帮你去加载这个 job Parser auto configuration，其他情况下我不会帮你去加载。OK，那这样也很合理，你没配我为什么要帮你去加载？相当于你没有配我这个模块，然后我说 match if missing 等于boss，就是说如果不没有这两个注解的话，那我这个模块就不加载了。OK，好了，这是我的一个强的约定。


然后接下来像 e s job 里面是不是有好多对应的配置？刚才我们看到了，是不是这些配置可能还会有这么几个嘛？所以说呢？我说我把这些配置读出来之后，我要放到哪里去，对不对？这些配置一般读出来我都会放到一个，就是也就是对应的配置文件里，所以说相当于我们在这个配置 OK 的时候，我们要加载配置文件，把配置文件读到一个我们自己的 Java class 类里。


那所以说在这里很容易能想到我们会有一个配置类，在这里我们把它创建出来，我们叫做 job zookeeper purpose，对不对？因为它都是跟 zookeeper 相关联的，跟 ZK 相关的，我们叫做 properties job ZK properties，那这个 job ZK practice 它是以什么为前缀的？同学们首先想一想，肯定是以这个为前缀，就是它的preface，肯定是它，就是说我读取你的配置文件，以这个为前缀的所有的配置，把它加到我们的 job JK practice 里。


那我们在这里边写一个这个就不需要写 config ration 了，这个是写这个 config ration properties，OK，然后把这个粘过来，就是说以这个为前缀的，我把属性全过来，有哪些属性？首先我们这两个属性是必须要有的，一个是我们的 name space，就是你的命名空间会写一个private。


Screen name, space, your private. I was straight. 叫什么呢？叫做 server list，是还有哪些对不对？还有哪些？其实还有很多，我们把最常见的来跟大家说一说。刚才我们看到的那几个，我们都把它粘过来，就起码会有这 3 个，对不对？这 3 个就是collection， time out，那其实你可以叫的全一些，在这里先把这 3 个先写一下。比如说第一个是 Int 类型的，就是 Max Retry，这个最简单，它的默认我说等于3，对不对？因为这个不是说必须要配的，像就上面这两个，那这个我可以给它一个默认值，包括下面这两个我也给它一个默认值，是可不可以？也可以，没问题， private 它我们也叫Int，然后叫做 connection time out，minutes，等于我们让它等于 10 秒可以 come out minutes second 的词这样去写，然后下面这个也是一样的，也是叫做 session timeout，然后 minute session seconds 这个超时间。我们说 session 的话，我们给的时间长一点，比如说 60 秒一分钟连接超时就是 10 秒或者是 15 秒，这个你自己去定好了，接下来还有哪些属性在这里，那你就不能是靠想当然了，是像一般你去对一个基础组件去封装，你一定要去看官方的 API 去了解整个的这个组件，这样你才能知道它里边到底有什么属性，有什么配置。然后你对应着把它写到你自己的配置里来。好了，在这里老师打开我们的这个浏览器，然后electrijob，点IO，OK，然后直接点文档，点Docx，我们选择lit，然后点到这个配置手册里边，我们就能看到这对应的一系列的配置。我们看到这些配置之后，我们其实今天要做的工作就是把这些配置全都用我们代码来实现。你比如说刚才我们说对于做 keeper 它的一些属性配置，那我们来看一看。首先这个列表不说了，就是 ZK 的列表，用逗号分隔 name space 就是一个 zopaper 的命名空间，然后 Max retry，还有这个你看为什么我叫做明年seconds？因为人官方就是这么去写，对不对？所以说我们按照官方的来，那其实官方还有 3 个属性，那其实我们也可以把它加上表示什么意思叫做base。

Sleep time in minutes, seconds?


意思叫做等待重试的间隔的初始化值，默认初始化，你看它都有缺省值，看见了，你看它这缺省值多少？这是 60 秒，这是 15 秒，是不是？你最好要跟人保持一致，我们也 15 秒，是不是？然后接下来我们把那三个属性直接带过来，用一个来先做这个属性，它默认是多少？默认是 1 秒，还有一个属性我们来看一下，还有一个叫做 Max sleep time， Mini seconds。

什么意思？重试等待最大的支持 3 秒，它这里边还有什么构造器注入？是否是构造器注入，下面全是否就两个？是是，就是说你必须要有列表和 name space，所以说这也正好契合了我们刚才所看到的，就是说我们的这个 ES job，它这个模块启没启动，完全看你的配置项里面有没有这两个配置，有这个两个配置就OK，没有这两个配置不好意思，那我就不会帮你去配。

所以说其实我们自己去封装一个这个组件的时候，你一定要对这个组件的 API 或者对它的一些配置项关方文档一定要非常熟悉，这样的话你才能去进行一个更好的这种基础组件的封装好了，那这也是我想要教小伙伴们的一个学习，或者说一个封装的方式，然后接下来这块最大是 3 秒。


好了，搞定这件事情之后，对应的一些盖沙的方法我们就直接就好了。那这里边我们说data，因为我们已经把这个 long book 已经引进来了，所以说他直接就帮我们去生成盖赛的方法好了，那这样的话，我们对于最基本的足 keeper 的几个配置就已经配置好了，是对应的这个文件以这个为前缀的所有的属性都会赋值到这个下面，这里当然也有默认值，当然如果你自己配了，那肯定会把默认值覆盖了，这没什么可说的。然后接下来我们一般怎么去使用？一般的使用方式就是 enable configuration practice 就是启用就可以了，对不对？ able configuration 直接就是这个注解，然后把我们当前的这个 class 类给它启用，这表示什么意思？当我们这个 on conditional e 通过了之后，马上就会把所有的就是以这个为前缀的一些配置都去读到我们的这个 job ZK practice 里。

好，那接下来我读完了 ZK 的配置，我们要做什么事情？我们原来做的事情就是 register center。我们原来做的事情就是读 ZK 嘛，就是初始化，这个就 keeper registry center。所以说接下来的任务还是一样的，就是我们要去做 registry center 的一个初始化工作，这个都没有什么变化。


好了，那我们来做，这里边我们看看怎么去写。比如说我们在这里叫做bin，对不对？艾特 bin 这个 b 有一个 init 方法，记得就是 register center。好，其实你可以参考老师之前的代码，你看 init method 是 init 方法，然后对应的我之前的做法是艾特 Y6 的方式，把这些配置都读进来，然后再解析。现在其实我们把它放到一个什么呀？放到一个这个配置文件所对应的这个 Java 对象里了，对不对？叫做 job to care for practice，所以说这样就更简单了。


OK，好，然后我们来看它的名字叫做 super registry center。好，然后它也叫做 keep register center。那这个就是说我如果把它当成 bin 注入到 spring 的时候，那它这个 bin 的名字就是这个方法名字，那小伙伴们一定要注意。OK，然后呢？干什么？我这个病要初始化，肯定要依赖这个里边的配置，所以说我们直接把它拿过来就可以了，因为它已经初始化完了，这个也要小写哈，记得。好，然后最后我直接把它 return 掉就可以了，对不对？就是把对应的这个 register center new 出来，然后 return 回去。那其实我们直接 return 的东西就是它，但是你 return 它的时候它需要用一个new，一个，它需要一个 jukier configuration，对不对？ JK config。那我们来看一看这个租 keeper configuration，是不是我们就要去读取我们对应的一些内容？ Zoo keeper config，然后我们去把它拗出来，拗它的时候需要一个非常非常关键的东西，就是你的列表和对应的 name space 就是两个必填项。哎，你看他已经给你提示了一个是列表，还有一个是 name space，那这里边是不是都已经放到我们的 practice 里了？我的 Props 里就有这两个属性，是不是直接 get 就好了？所以说在这里我们直接 get 我们的 server list 4，然后我们再我们说一下，然后再 get 我们的 name space 就可以了。


好，这个 configuration 搞定了之后，接下来就 b 天象都已经确认完了，剩下的就是一些其他的无关紧要的了，我们就挨着旁的去把它 set 这词好了。比如说 set basic sleep time minutes，这直接就 get basic 就可以了，对不对？接下来的事情就是一些无脑的炒作， Max 就直接讲 get 麦克斯。

好，有这两项之后还有 set 什么 collection time out，直接为什么我们名字要起得一致，其实到时候你写的时候就非常方便了。还有几个 set connection，还有 session time out， JK config get session time out minutes，还有最后一个 set 什么呢？ Max Retry。那我们就 z k 跟 big 点 get Max Retry。

```java
# Auto Configure  ????
org.springframework.boot.autoconfigure.EnableAutoConfiguration=\
com.bfxy.rabbit.task.autoconfiguration.JobParserAutoConfigution

---------------------------------------------------------------------------------------------

package com.bfxy.rabbit.task.autoconfiguration;

import lombok.Data;
import org.springframework.boot.context.properties.ConfigurationProperties;

/**
 * <h1></h1>
 */
@ConfigurationProperties(prefix = "elastic.job.zk.")
@Data
public class JobZookeeperProperties {


    private String namespace;

    private String serverLists;

    private String maxRetries;

    private int connectionTimeoutMilliseconds = 15000;

    private int sessionTimeoutMilliseconds = 60000;

    private int baseSleepTimeMilliseconds = 1000;

    private int maxSleepTimeMilliseconds = 3000;

    private String digest = "";

}

---------------------------------------------------------------------------------------------------------------------------------------
package com.bfxy.rabbit.task.autoconfiguration;

import com.dangdang.ddframe.job.reg.zookeeper.ZookeeperConfiguration;
import com.dangdang.ddframe.job.reg.zookeeper.ZookeeperRegistryCenter;
import lombok.extern.slf4j.Slf4j;
import org.springframework.boot.autoconfigure.condition.ConditionalOnProperty;
import org.springframework.boot.context.properties.EnableConfigurationProperties;
import org.springframework.context.annotation.Bean;
import org.springframework.context.annotation.Configuration;

/**
 * <h1></h1>
 */
@Slf4j
@Configuration
@ConditionalOnProperty(prefix = "elastic.job.zk" , name = {"namespace", "serverLists"}, matchIfMissing = false)
@EnableConfigurationProperties(JobZookeeperProperties.class)
public class JobParserAutoConfigution {


    @Bean(initMethod = "init")
    public ZookeeperRegistryCenter zookeeperRegistryCenter(JobZookeeperProperties jobZookeeperProperties) {

        ZookeeperConfiguration zkConfig = new ZookeeperConfiguration(jobZookeeperProperties.getNamespace(), jobZookeeperProperties.getServerLists());

        zkConfig.setBaseSleepTimeMilliseconds(zkConfig.getBaseSleepTimeMilliseconds());
        zkConfig.setMaxSleepTimeMilliseconds(zkConfig.getMaxSleepTimeMilliseconds());
        zkConfig.setConnectionTimeoutMilliseconds(zkConfig.getSessionTimeoutMilliseconds());
        zkConfig.setSessionTimeoutMilliseconds(zkConfig.getConnectionTimeoutMilliseconds());
        zkConfig.setMaxRetries(zkConfig.getMaxRetries());
        zkConfig.setDigest(zkConfig.getDigest());


        log.info("初始化注册中心成功....， zkAddress : {} ,  namespace : { } " , jobZookeeperProperties.getServerLists() , jobZookeeperProperties.getNamespace() );
        return new ZookeeperRegistryCenter(zkConfig);
    }


}


---------------------------------------------------------------------------------------------------------------------------------------

```

在这里我刚才好像又看到一个属性，刚才好像又看到一个属性点过来，它的这个 API 里边有一个属性叫做Grace，表示人家 ZK 的这个令牌是不是缺省为不需要？那么这块呢？缺省时不需要就是空呗。那其实我们是不是也把它写下private？对，这个名字等于空，这是默认值。


好，有了这个之后，我们回过头来是不是还可以去做设置，对不对？叫 j k config 的 get OK，一共几个属性？一共 8 个属性。我们来看看我们这里边是不是 8 个属性，检查一下没问题，一共 8 个属性。好了，那第一步我们就做完了，做完之后这个 JK 这块帮我触发成功了，我就表示 JK 触发成功了，是不是？然后我打印一下，那我加一个日志可以吧？我加一个 s l，s，l，f，o，g， s l u g 打一个logger，我说 log 点infra，我说初始化 job 注册中心配置成功了。然后我们说 c k 的 address 是什么？然后还有一个它的 name space 是什么？我们直接两个逗号把它填进去就好了，一个是对应的它的这个东西是列表，然后还有一个是这个东西是对应的，他的 name space info。日志来告诉大家，我的 ZK 已经数据化成功了。好，那其实呢，就这么 30 行代码就已经把租 keeper 的配置封装得更好了一些，我把它这个配置读到一个这个 Java 对象里了。那我们做完了第一步之后，同学们想一想第二步我们应该。





