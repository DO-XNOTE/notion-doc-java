---
title: 3-24 【技术改造】电商系统集成Eureka - 注册中心和公共web组件 
---

# 3-24 【技术改造】电商系统集成Eureka - 注册中心和公共web组件 

[image](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/caf50723-7b37-41ff-8283-a185561cf914/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZRL6T7PO%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T225552Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCSRAtbmqOcdCAjGz41DhpFToUo2wj2QNcXr55YH%2BAscgIhAPfCFHePYWPG4fzcRzuGLLIKQOEMlefmEzvKqq6raDgVKogECMb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1Igyj%2BDnBySkm7OJMMWEq3APj6Z2frFts5diRrpRIawve346g%2Fck0cEBBeFEsSmOx3c9VzFKBo32bsBy5nVeWQMv%2Byy93mQSjHqa0f8H4dhPuda62BOIMuVISG8n4W70Tg05RSINvW6zJtsU2S%2FsWaxovLA%2BSH6acRutpShzLbbjhD43tEJTc4cu9crkDdbZd%2F4U3SQrZYM451bx68Ph62pu1Mg5BSurv07aRCA6EQ8UU8h9ThSMTSdfbdZaq%2B%2FRm5XeYdV3%2FPuhD%2FwxxXUsLRaOWe4Yy1ceiyCttxDjYCu5Z5acaJL6Iqx%2B7FLpEA5ZC2htsDBD8p4D%2BZbLWQtz%2Fr8WXeZlB0uQAKDOmm7xFtWBr%2BTSI22hsjt40pMm9NQSmtzPk%2FZrzfOf6jvn0JSmgSuPh9AwFU6Z%2FFw%2Bo92HIh4W3kB1KQroj760kamoEBa1N9Ku9RqNtz%2FWx559kYZwm56uqMaW0Hu0Wltcd8oa0Evq2hOs%2B4vl5zGuJdSLlcOzAAC6zarcab5kZgLEb6AOMl5eln%2Br2jUSe5KhyfjqbE9tyDho2xByR%2Bz%2BhOxaCBopaABhRfgOgeLDtcpE1CY9JWbcY4YRNtyYbpB3PBVAmsJzXzmCXySs0q3ktON0gsJVMlvdZgA0bucKRi%2F%2BeyTCFuf%2FSBjqkAdyexJHRSC7ZpE5F1O2M5WKRKrDyzC%2FR1gI61mlH6aTWRp%2F1xE3xe1qYxPYY%2F3kepO%2FDX004leePcxqsOK5dxbgWyBFdvGHXS4OHoQ3BRMfxq%2Bs%2BYTNxenOHc4Cu8%2BlJgRQu1zUI%2FDa2nZFfMRJuajKwjZH6PSQd3Wp7NH0y4SD2%2FM8YeHSSSK%2BeDNadarwHeN51UoaMQEOW05l1MU8DAWbn35Pd&X-Amz-Signature=1e003eb5ba35f81e34d554713dbf562878c9f4b0f522b39485bb62a77354f394&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

hello 慕课网的各位同学们，大家好，那咱这一小节里进行电商项目改造的第二步，那就是注册中心和公共 web 组件的搭建。

[image](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/a5a70ec6-0ab5-40bd-9827-8819e2fc9ea1/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZRL6T7PO%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T225552Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCSRAtbmqOcdCAjGz41DhpFToUo2wj2QNcXr55YH%2BAscgIhAPfCFHePYWPG4fzcRzuGLLIKQOEMlefmEzvKqq6raDgVKogECMb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1Igyj%2BDnBySkm7OJMMWEq3APj6Z2frFts5diRrpRIawve346g%2Fck0cEBBeFEsSmOx3c9VzFKBo32bsBy5nVeWQMv%2Byy93mQSjHqa0f8H4dhPuda62BOIMuVISG8n4W70Tg05RSINvW6zJtsU2S%2FsWaxovLA%2BSH6acRutpShzLbbjhD43tEJTc4cu9crkDdbZd%2F4U3SQrZYM451bx68Ph62pu1Mg5BSurv07aRCA6EQ8UU8h9ThSMTSdfbdZaq%2B%2FRm5XeYdV3%2FPuhD%2FwxxXUsLRaOWe4Yy1ceiyCttxDjYCu5Z5acaJL6Iqx%2B7FLpEA5ZC2htsDBD8p4D%2BZbLWQtz%2Fr8WXeZlB0uQAKDOmm7xFtWBr%2BTSI22hsjt40pMm9NQSmtzPk%2FZrzfOf6jvn0JSmgSuPh9AwFU6Z%2FFw%2Bo92HIh4W3kB1KQroj760kamoEBa1N9Ku9RqNtz%2FWx559kYZwm56uqMaW0Hu0Wltcd8oa0Evq2hOs%2B4vl5zGuJdSLlcOzAAC6zarcab5kZgLEb6AOMl5eln%2Br2jUSe5KhyfjqbE9tyDho2xByR%2Bz%2BhOxaCBopaABhRfgOgeLDtcpE1CY9JWbcY4YRNtyYbpB3PBVAmsJzXzmCXySs0q3ktON0gsJVMlvdZgA0bucKRi%2F%2BeyTCFuf%2FSBjqkAdyexJHRSC7ZpE5F1O2M5WKRKrDyzC%2FR1gI61mlH6aTWRp%2F1xE3xe1qYxPYY%2F3kepO%2FDX004leePcxqsOK5dxbgWyBFdvGHXS4OHoQ3BRMfxq%2Bs%2BYTNxenOHc4Cu8%2BlJgRQu1zUI%2FDa2nZFfMRJuajKwjZH6PSQd3Wp7NH0y4SD2%2FM8YeHSSSK%2BeDNadarwHeN51UoaMQEOW05l1MU8DAWbn35Pd&X-Amz-Signature=96802c9cc77455a912b9dc8e7ab487d53ee7183b2e04bc071f62bc517f790444&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

那这里第一步就是创建一个注册中心。与之前 demo 项目中不同的是，咱这次创建的注册中心，我们尝试以命令行的形式把它启动起来。那第二步就是抽取公共的 web 组件模块。这里面可不是单纯的 copy paste ，而是会涉及到一点代码的小改动。同学们在完成了这一节的内容之后，就可以去开始正式的微服务改造。那我们说干就干，转战 intelij 立即。好。同学们，那我们开始创建一个新的毛酒，用来存放注册中心的代码。这个 module 的名字我们给它起名叫 registry 一个横杠 center 也就是注册中心的意思。那我们把它放在哪里呢？同学们这里注意一下文件路径，我们把它塞到 platform 这一层文件夹下面。 did you finish321 走。


OK 那接下来我们开始添加他的依赖项，这里只用添加一个依赖，因为我们只是单纯的作为一个注册中心，没有其他的功能。所以它这里需要引入的是谁？就是 spring cloud 的 eureka 它的 group ID 是 spring framework 然后后面是 cloud 那它的 artifact ID ，我直接把它 copy 过来，是咱 spring cloud 当中的 eureka server 的依赖项。


OK 那到这里还没有完全结束，我们这因为要在外面的命令行启动，所以这里给他多添加一个 build 那这个 build 节点是做什么内容？我们接下来往后看添加一个 plugin 那这个 plugin 是谁呢？咱之前应该没有用过它的 group ID 我们来看是 or 级 spring framework 下面的 a spring boot 咱前面添加的这个 build 这个 build plugin 是阿帕奇没问的 plugin 那这里不一样了，这里我添加的是 spring boot 的 plugin 目的是什么呢？目的是指明我 spring boot 提供启动的时候的闷方法主类好，它的 artifact 我们也给它添加上去。
Frame boot laven plugin.


OK 那接下来是 configuration 其实指定主类的方式有很多种，我们是把 manifest 运行器指定都是可以的。那么我们在这里通过用梅文配置的形式来指定，相对比较规范一些。那它的 configuration 我们这里怎么样呢？先把它留白 main class 咱先把这个标签给它加上，等到咱创建完了启动类之后再把它回填下来。


OK 接下来我们要指定你的 execution 方法，在 execution 方法里，我们这个标签下面要给它指定一些动作，指定什么呢？一个 repackage 这下面再添加一个呼入节点，然后打上 RE package 那这一个执行目标顾名思义就是重新打包。只不过在你重新打包的过程中，这个价包它的 many fast 文件中的主类会被你这里写的 main class 标签中的主类替换掉。 OK 那这个 pom 文件就先定义到这里。那我们接下来回到代码当中去创建它的启动类。首先我们创建一个 package package 的路径还是 calm.imock 然后紧接着去创建一个 class 对象，它的名称我们把它叫做 eureka server application 好回撤。


那大家知道这上面都要添加哪些大帽子吗？应该都非常熟悉了，咱先添加一个 spring boot application 紧接着是谁呢？与瑞卡有关的对不对？ Enable eureka server. 那这两个注解添加上去，我们接着来写它的闷方法。这个闷方法和咱前面 demo 当中随堂练习里面启动方式是一样的。好我们以什么样的方式启动，就是直接 new 一个 spring application builder application builder 在这好，然后把当前这个类的名称 copy 进来，它是个点 class 对象，然后以 web 形式 web 形式中的参数是什么呢？ web application 类型是 serve let 好，指定好这些步骤以后，你的 arguments 参数给传递到 run 方法当中。 OK 这个类就创建完成了。


接下来我们要去创建注册中心的启动配置项，非常简单，我给这个配置项创建的格式是 YAML 类型的 application.yaml 类型。那同学们在跑微服务的过程中，一定要记住第一个启动的组件是谁呢？那就是这个注册中心。所以我在这里多加一行注释，叫启动顺序，它是 number one 的第一位。
OK 那咱在这个 YAML 文件当中去创建哪些节点？第一个，spring然后是 application 我们要给它起一个名字，这个名字就把它叫做 eureka 杠 serverok 那我接下来要指定一个 profiles 多打了一个 E 把它去掉。好。 profile 我们这里给它起 dead 那这里定义完了 spring 标签下的内容，接下来我要给他指定一个端口了。对不对，server后面跟 port 端口我们从哪里开始？我们从 2 万开始。好了，端口 2 万。


那最后一个就是定义 eureka 自己的内容了。那咱先定义 eureka client 这里的 fetch registry 等于什么呢？ false 因为咱是一个注册中心，对不对？咱不是一个服务节点，所以并不需要去拉取注册内容。 OK 那下一步， register with eureka 这个是什么也是false ，我们启动的时候不需要去自己注册自己。


好，那接下来最后一个 instance 这个 instance 我们给它指定的 host name 是谁呢？是 local host 那所以我们这里既然指定了 local host 这里要提醒同学们一句，千万不要忘了改本地的 host 文件。改 host 文件的目的是什么呢？将 local host 指向本机。好，这个是通过 host 文件。那到这里整个配置文件就已经完成了。那同学们如果感兴趣，可以用咱之前学习的高可用的注册中心结构来搭建两个互相备份的注册中心。


OK 那咱这里最后一步是什么？改 pom 文件？把咱刚才创建的这个主类 main class 给写到哪呢？写到这个 main class 标签下，那它的路径是 com.imock 再点这里已经提示出来了，是谁是 eureka server applicationok 那把这个路径配好之后，咱的注册中心就创建完成了。


接下来我们通过命令行把它启动起来，咱先把这个项目的路径给它 copy 下来。那接下来我到命令行当中直接 CD 到当前项目的路径。下面我跑一下梅文的 clean store 方法很快执行完了之后，我们接下来去直接 CD 到他的 target 目录下面。这里已经编译成功，我到 target 目录。好直接用 Java 杠 jar 的形式把它启动起来。咱这里也不通过 intelligence 启动，直接通过外部的命令行把这个 registry center 1.0 点 Snapshot 打出来，然后回车用 Java 杠架的形式启动。好，这里可以看到它的 log 在刷往上刷新。好，看到这里最后一行 log 已经显示启动起来了，我们转粘到浏览器看一眼。这里 local host 2 万，我把它刷新一下。


好，刷新完毕，同学们可以看到这个注册中心已经启动起来了，那说明咱的配置完全生效，那万事俱备，就等着咱的微服务来注册上来了。好，那我们回到云泰的这里面，接下来咱这一节还有一个任务是创建什么呢？公共的 web 组件。那我们这里直接右键开始创建一个新的茅酒。那这个新猫就我们给它起名字叫什么呢？叫 foodie 杠 cloud 它名字比较长，后面再来一个杠 web 既然是 web 组件，就给大家起这样一个名字叫 web component componentsok 好，我们把它复制一下，然后点击 next 毛球 name 这里改一下，并且把它放到哪里呢？把它放到 common 这个文件夹下面。


OK 那这里这个项目已经创建好了，那接下来我们把 dependency 给它添加进去。咱这个项目需要两个 dependency 分别是谁呢？好，第一个 dependency 他是咱的自己人，这个自己人是谁呢？咱前面创建的 foodie cloud common 项目。好，那我们这里把这个依赖给它引入进来，咱 common 项目的 elle 我们把它 group ID 给写上，是 project group ID 然后它的 artifact 是 foodie 杠，我们这里选中第三个 foodie cloud commonok 它的 version 我们这里不把它写死，把 version 改成 project 杠 version 这样一个变量。


好。第二个， dependency 是咱前面经常使用的 accurator 我们把它加入进来。 group ID 是 org framework.boot had the artifact she spring boot starter。 Activator spring boot. Starter. Act. reader OK 那 version 这里不用指定，它会从父类 palm 当中这个 dependency management 节点搭下面我们引入的这个 spring cloud dependency 当中，把需要加载的这个 version 版本引入进来，这就是咱添加这个 dependency management 节点的一个目的。我不用在子项目当中具体的指定某些组件的版本，而是把这些版本它的 version 信息通通在这里，先给它预先的导入进来。 OK 那我们在 web component 当中已经指定好了，这两个 dependency 接下来去写几行代码。好，我们找到下面的 Java 文件夹给他，把咱的赞助商 com imok 先打上创建这样一个package 。


在这个里面，我们将引入三类项目代码，它分别是哪三个呢？第一个是 aspect 那小伙伴们看名称就知道这里是要引入谁，引入一些切面对不对？那接下来第二个包，我们把它引入什么呢？ config 某些配置项。好，接下来再创建最后一个 package 是 controllerok 那这三类包名分别对应哪些内容呢？我们这里去到其他地方抄作业了。这个 aspect 下面只有一个类。好，我们切换到腹地 DEV 项目，把这个类给它找出来是谁是 service log aspect 好，这里把它复制一下，然后切换回复的 cloud 当中，把它给 copy 过来。


那 copy 过来以后，咱这里要改动一行代码，我们往下看改动哪一行。那在这里同学们看到它 around 这里配置的execution ，它的包路径我们在后面的微肤改造当中将引入额外的一层包路径。那咱目前来看，它的 service 都是在 com.imock.service 下面。不过到以后它的包路径结构将变为 com.imock 后面点跟的不是 service 了是什么呢？而是咱微服务的模块名称，比如点 item in service 这是商品中心或者点 user.service 那是用户中心。


因此咱的 around 接口中这里匹配的路径我们要怎么改呢？很简单，我们在这里把它的点后面再跟一层结构，我们这里跟一个通配符，点星号再来一个点。 OK 那改成这个样子就可以了，这里就可以匹配咱在微服改造过后多引入的这么一层文件夹结构，也就是微服务的名称模块名称的结构。 OK 那咱这一个类已经改造完了。那接下来我们去 copy configconfig 里面都有哪些内容呢？有三个内容。好，我们切换到 food DEV 找到下面的 config 文件夹。那这里总共有一二三四四一个 config 文件。我们这里只 copy 3 个，把哪一个给它留下来呢？就是他这个 order job 那从领域划分来看， order job 是不是一个定时的任务去干什么？关闭超期未支付的订单。那咱这里把它划分到订单中心的领域来做。所以这里我们就不把它去添加到公共的 web component 项目当中。因此我这里挑选123，把这剩下的三个类 copy 一下，切换到 food cloud 当中，给它添加到这里。


OK 那这三个我们有没有需要改动的地方呢？当然有了，咱接下来要对 swagger 做一个改动，改什么内容呢？同学们这里看好停在这里，它在 create arrest API 在这样一个 bin 的声明当中，它这里用到了什么呢？用到了一个匹配规则，它匹配的是什么？我们看这个 API 那在这个方法内，它匹配的是所有 base package 为 hum.imock.controller 这个路径下的 controller 里。那我们在经过唯一服务改造之后，会引入很多的 service 那这些 service 就不一定会放到 base package 这个 controller 下面，他可能有五花八门的包名，但是他们有另外一个共同特征。


同学们经过前面尤瑞克的学习，应该会发现咱的这些服务也会被声明成 rest controller 对不对？它也是一个 controller 层，因为咱的 eureka 是基于 HTTP 的这种服务发现的形式。所以我们把基于 base package 的匹配规则改成什么呢？我们这里来看改成基于注解怎么来改？我这里调用另外一个方法叫 with a class annotation class annotation 我这里给哪一个类呢？那就是 rest controller.class 好嘞，经过这么一改，所有类你只要在上面声明了它是一个 rest controller 那么就会被咱的 swagger 给它抓取到。 OK 那我在后面添加一个注释，叫指定 service 上的 rest controller 注解。


好，那这个类改完，咱接下来就去 copy 这一个 control 类，那它从哪里来呢？咱切换到 food DEV 当中，在 controller 这个文件夹下面，我们挑选这么一个哪一个呢？当然是 base controller 因为它是所有 controller 共同继承的一个父类，也是一个 web 通用组件。所以咱们把它给 copy 一下，然后切换回复的 cloud 好把它给拿过来，然后在这里要动一点手脚怎么动呢？我们往下看同学们看到这里有一句标红的语句是什么呢？这里会调用 my order service 调用它的一个方法来判别你的当前的 order 是不是由指定的用户来创建的。


那这是一个订单中心的方法，所以我们自然而然会把它移植到哪里移植到订单中心中去。所以在这个公共的组件当中，我们先把它注释掉好，但是加一个 fix me 提醒大家一下提醒大家什么呢？下面的逻辑移植到订单中心东去移植到订单中心。 OK 好，那我们网上再把 import 当中引入的这些没有用到的依赖项，给它清理干净。好，这个清理依赖项有快捷键的，同学们不用一行一行的删，直接点一下快捷键一键清理就好了。 OK 那到这里，咱需要用到的 web 组件也已经创建完成了。至此咱在微服务拆分之前所需要用到的公共组件结构已经全部创建完毕了，我们就要在下一个小节当中正式开始微服务领域模型的拆分。那咱第一个拆分的模块是谁呢？这里先不剧透，同学们到下一节一看便知，那小伙伴们，我们下一个小节再见。



