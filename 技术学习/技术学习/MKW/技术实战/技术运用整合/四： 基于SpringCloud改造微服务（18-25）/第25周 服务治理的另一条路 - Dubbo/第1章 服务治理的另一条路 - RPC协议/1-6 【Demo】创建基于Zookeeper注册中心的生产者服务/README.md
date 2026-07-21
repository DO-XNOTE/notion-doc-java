---
title: 1-6 【Demo】创建基于Zookeeper注册中心的生产者服务
---

# 1-6 【Demo】创建基于Zookeeper注册中心的生产者服务

[image](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/00bc1834-54ae-4381-ace2-dcf341355288/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TQYS2QYW%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T225855Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIB%2BRv8a3htggsKyMtgd0l%2FlCcgHWiNn5D6%2FyihMRUqMxAiEAkGVLgL9RnOwrzIxsEsLJ8sPFwakli04WIW%2B3TkqwxdUqiAQIxv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDOgKYs5MB69dK4n2XCrcA8JB2BdonpIwOx8cNFE5qBKDABsU3eZnfGlZiHvD06umlMFcJFoyYLDtkKWCv6DOWKH%2Fc3WrB38jGJfw9gX9%2F5KNoIv3XiulDL50NIpvngMv2YVCdHTlDqGs3OzdN7gV6W%2FqpfEDXx5kd%2F1NORWWwJnMxrvBlj6ywa3ClBkf%2F6lsOvOHDzMZ0SMFa97rwBWASLir77Ly5xW5HwJdU5McxARmG9iosAHWWZ3MYQXJo%2Fz9vgXtVJqWbHgq%2FeMb1e%2BWEx57qSMSSU5H62JifdAXLtEMOlOraMsjUbJ%2BicDIqoWaK3OdlTiLwh2VbFIQeSZvEZdxGAqezbyOUBFZWKEgEJjCAbd7tK%2FUWzFR%2FGiuUu6b43zUdsyyW7BWOthBt4PQnALFEwsWhHyO06Ut2%2FIsDaQftDPXI7cnz6YhJsS8MQx%2B95MuY9moeBQRNVqFMIHTL1Fv7GyWWnmuvOHmKFn7oY4wHRdGgOoeHVFSD5CYf3iHEGR8rT3AX6r%2Fw17aLhhiiqV7otg1GEQlC996TEpICymDBV64y3jHUfcI5yCiI5ZYDn5AqGiHwQ%2FuM%2BOQ%2BBvpYOeghUUO7ge7Oy3OIU8Mpa822vqyhPTwz7GfjjQw%2FISFG%2FsLJ42a1WVXNTaHMLO6%2F9IGOqUBda7rIMh1bm3GRAJaHOTTlp1DaPo9r106LkrTm1lxQcj8OsCWtqzYNhfMIpZS2XpyGSpskesiQCkwwBnLX5%2F5qB5n5dXiXbPvA%2FebCuaI%2Be0BcB5CtDdgu2zjkpG8aaeqsAd55Aj6X6lBVElSDcUSOv7KXZ91jVXJe1S%2FUcrutkuFmVAe8Ag0qnxRCXgjS%2Bt1nEyNZ%2B3Y8fTer1m%2BEz3Iq7UA3yIv&X-Amz-Signature=dd0c38f414581be2dbdcea3a59b2c8342311bee3799615b4d1154bb59b305627&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)


[image](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/4b42b7e6-f72e-4668-b044-3349b49bdee9/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TQYS2QYW%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T225855Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIB%2BRv8a3htggsKyMtgd0l%2FlCcgHWiNn5D6%2FyihMRUqMxAiEAkGVLgL9RnOwrzIxsEsLJ8sPFwakli04WIW%2B3TkqwxdUqiAQIxv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDOgKYs5MB69dK4n2XCrcA8JB2BdonpIwOx8cNFE5qBKDABsU3eZnfGlZiHvD06umlMFcJFoyYLDtkKWCv6DOWKH%2Fc3WrB38jGJfw9gX9%2F5KNoIv3XiulDL50NIpvngMv2YVCdHTlDqGs3OzdN7gV6W%2FqpfEDXx5kd%2F1NORWWwJnMxrvBlj6ywa3ClBkf%2F6lsOvOHDzMZ0SMFa97rwBWASLir77Ly5xW5HwJdU5McxARmG9iosAHWWZ3MYQXJo%2Fz9vgXtVJqWbHgq%2FeMb1e%2BWEx57qSMSSU5H62JifdAXLtEMOlOraMsjUbJ%2BicDIqoWaK3OdlTiLwh2VbFIQeSZvEZdxGAqezbyOUBFZWKEgEJjCAbd7tK%2FUWzFR%2FGiuUu6b43zUdsyyW7BWOthBt4PQnALFEwsWhHyO06Ut2%2FIsDaQftDPXI7cnz6YhJsS8MQx%2B95MuY9moeBQRNVqFMIHTL1Fv7GyWWnmuvOHmKFn7oY4wHRdGgOoeHVFSD5CYf3iHEGR8rT3AX6r%2Fw17aLhhiiqV7otg1GEQlC996TEpICymDBV64y3jHUfcI5yCiI5ZYDn5AqGiHwQ%2FuM%2BOQ%2BBvpYOeghUUO7ge7Oy3OIU8Mpa822vqyhPTwz7GfjjQw%2FISFG%2FsLJ42a1WVXNTaHMLO6%2F9IGOqUBda7rIMh1bm3GRAJaHOTTlp1DaPo9r106LkrTm1lxQcj8OsCWtqzYNhfMIpZS2XpyGSpskesiQCkwwBnLX5%2F5qB5n5dXiXbPvA%2FebCuaI%2Be0BcB5CtDdgu2zjkpG8aaeqsAd55Aj6X6lBVElSDcUSOv7KXZ91jVXJe1S%2FUcrutkuFmVAe8Ag0qnxRCXgjS%2Bt1nEyNZ%2B3Y8fTer1m%2BEz3Iq7UA3yIv&X-Amz-Signature=16fa218f5b0447920ebac341729b1f46088ff4def9016ccd442935d577a4ce53&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

嗨慕课网的各位同学们，大家好，咱迎来了第一节 double 章节的实操课。在这一节当中，我们一起构建一个服务提供方。咱们先来看一下本节的主要内容都有哪些。首先咱安装，然后启动 skipper 作为 double 的注册中心。紧接着创建一个 double 的 API 接口层，这个接口层是在后面章节会留给服务的消费者来进行调用的。最后一个环节就是创建 double provider 添加一个 service 层。在这里我会跟大家简单的过一下 double 的配置。 OK 大家抄起家伙在 entire dj 里面见。


我这里先跟大家稍微过一下 zoom 的启动过程，咱如果没有安装的同学，可以到这个下载地址上下载最新版的三点五点五的 zookeeper 下载好以后，咱做一个配置，打开 zookeeper 的安装目录，我这里是用的 Mac 系统，所以它的安装目录在 user 杠 local 下面有个阿帕奇的 zookeeper 包。


在这个包下的 CONF config 文件夹下，我们会找到一个叫 zoo 下划线 sample.cfg 的文件，咱把它原封不动，先不用改内容，把它复制一份重命名为 zoo.cfg 这一步就做完了。接下来咱打开组 keeper 的安装文件夹，然后走到下面的 bin 文件夹里面，执行一个启动命令，我把这个给 copy 下来，这是 Mac 版的启动命令，如果 Windows 的同学就直接执行对应的 CM D 文件就好了。好，我这里已经走到了这个 bin 的文件夹下，然后复制过来命令直接启动。如果同学们看到这样几行提示，我转到 intelj 里面，如果看到了这个 started 的这个提示，那代表着启动成功了。那接下来同学们也可以去跑一段命令是 zkcl I 的命令，它也在 bin 文件夹下面去验证一下它的运行效果。
在开始本节的内容之前，同学们要先确保把本地的 zookeeper 启动起来。那这一个步骤，我把它放到了咱的 double 这一个文件夹下面有一个 zookeeper TXT 文件，大家到这里面找就可以了。 OK 那接下来我就开始进行本章的 coding 任务了。本节的 coding 任务主要有两个，第一个是创建一个接口层，接下来再创建一个服务的提供者作为接口层的实现。那咱先从易到难好了，先创建这个接口层，给它起名，它的 artifact ID 就叫 double 杠 apiok 直接进入 next 把它扔到哪个文件夹，扔到 double 文件夹里面，我们把 double 在这写上。


OK 点击 finish 321 这个项目的 palm 特别的简单，因为它只是一个接口层，所以几乎什么都不用引入，把几乎去掉，它就是什么都不用引入咱现在可以直接来创建接口方法了。当然了，在创建接口之前，要把咱的独家冠名赞助商 I mock 给它打印到包名上，创建一个包名叫 imock.spring cloudok 好，那接下来咱就要在这个包下面去创建一个类，我们给它起名字叫 product OK 它就是一个商品。那我们给这个商品随便加那么几个属性，比如说第一个属性，你卖商品肯定要有名称对吗？也就是 name 给它改成 private 除了 name 以外，咱还要有一个关键属性是价钱，给它一个 big decimal 叫 price OK 在 double 里面的 entity 一定要怎么样？一定要支持序列化和反序列化。所以大家不要忘了添加上 serializable 接口，就是这个序列化的接口。否则的话当我们的 consumer 来调用它的时候，可是会报错的。


好我们定义完了 product 以后，接下来定义一个空的 Java 方法，这个方法没有实现，是个接口层，我们给它定义为 I double serviceok 那这个 service 咱就做一件非常简单的事儿。好了，给它定义一个方法叫什么，它返回一个 product 它的方法名叫 publish 商品发布。这是老师最熟悉的接口，这个接口依然接收一个商品作为它的接收参数。


咱接口层定义完了以后，接下来就去再创建一个新的茅酒，我们给它就起名叫 double 杠 client 它是一个服务的提供者。 OK 点击 next 这里，依然把它放回到 double 文件夹下。好，finish那这个 palm 文件咱要稍微动那么点手脚了，先给它加一个 dependencies 然后这里面都有哪些项目呢？可多了，咱先要把最基本的一个项目 boot 的 starter web 给它引入进来。我们随便找一个之前创建好的项目，把这个应用给它 copy 下来，找任意一个就可以了。咱找这一个 boot starter web 给它 copy 过来。那剩下的 dependency 都是全新的了，我们来一个挨个认识一下。


首先咱既然是使用了 double 那一定要把 double 先给请进门。 double 其实有好几个不同的版本，那咱这里引入谁呢？咱就引入那根正苗红明媒正曲的 or 级阿帕奇下面的这个 double 好，它的 artifact ID 就叫 double 那我们给它的 version 指定成 release 版本二点七点三。


okdouble 定义完了之后，咱们别忘了它底层还要依赖一个注册中心对吧，它的注册中心是 zookeeper 所以这里还要额外的引入一个同样是 or 几点阿帕奇。 double 下面的一个包是谁呢？他是 double 用来和 zookeeper 进行合体的 artifact 答叫 double dependencies 杠苏 keeper OK 这些名字都非常长，大家打的时候注意一下，不要打错了，同样它的 version 也是二点七点三。 OK 那这一个 dependency 定义好以后还需要一个是谁？咱的 double 是不是跟 springboot 组件一起结合使用的？所以这里为了和 springboot 合体，还需要引入一个 or 及阿帕奇 double 下面的一个组件，它的名称叫做 double 杠 spring boot starterok 那它的 version 同样的也是三点七点三。


这三兄弟是一套定义完这三兄弟以后，我们是不是要把接口层也给引入进来呢？就是咱刚才定义好的接口层，它的 group ID 和咱当前的 project ID 是一样的，我们给它打上叫 project.group ID。 Ok. 那 artifact ID 就是 double 杠 API version ，我们这里不用写死，咱也给它打上 project 注解下的这个 versionok 那到这里， pum 文件看似就定义完了，那咱接下来可以定义启动函数了。


定义启动函数之前，咱再把我们的独家冠名赞助商 IMock 创建出来，它的包名是 com.imock.spring cloudok 接下来的这个闷方法咱给它起名就叫 double client application 好勒，这里的启动函数 M 函数咱就从 stream 里面 copy 过来。好了，就不用一行手打了，我们找到 stream 的内函数，完整的 copy 过来，然后把类名给它替换一下。接下来给它戴绿帽子啦。


第一顶帽子是 spring boot application 因为它是一个 spring boot power 的应用，后面一个属性这可就是新的注解了，叫 enable double 大家看这里有两个不同的注解，其中上面的一个 enable double 注解被标记成了 duplicate 为什么？你看它的包名叫 com 点阿里巴巴点 double 那咱要使用的是下面的这个注解，你看它的包名是 or 级点阿帕奇是名门正取出自名门。 OK 这样的话我们的 man 方法就定义完了。接下来咱给它定义一个 service 层。同学们肯定这里习惯定义一个 controller 了，咱 double 不是这样玩的。我们不用什么 controller 只要添加 service 就行了。那这个 double 的 service 咱给它命名就叫 double service 就可以了。然后让它继承自谁呢？继承自咱前面创建的这个方法的接口叫 I double service 这个实现类给它添加进去。然后给这个接口也添加一个注解是 service 注解不再是 control 了。添加完 service 以后，给他把 lock for G 的注解添加进去。


OK 那这里我们就是简单的测试一个方法的序列化和反序列化过程。所以这里的 product 咱就不做任何的修改，只是把它原封不动的返回。但是这里多打一行 log 告诉大家咱正在发布商品，publishing product AH 这个 product 的名称给它打上 get nameok 那 service 也定义好了。不过木然之间好像发现了那么一点小瑕疵，瑕疵在哪里啊？那咱平时引入 service 这个注解是不是引入的就是 spring framework 的service ，咱的 double 可不是这个了，double有自己的一个 service 注解，我们不要引用错了。


OK 那到这里咱的 service 层就已经定义完了，接下来我要带大家一起去创建 double 的配置文件。 double 的配置文件它的配置项比较多，那老师这里就不再带大家一起去一行手打了。我这里已经准备好了一份 double 的配置文件，我来带大家看一下 double 中几个比较重要的配置属性，我们打开 application.yaml 文件。 OK 咱在配置文件的顶上就打上了，这是极简配置。为什么？因为 double 的配置下真的是特别的多，所以咱这里只挑几个重要的属性跟大家看一下我们 double 的起始节点，它不是以 spring 开头的。同学们可能有的时候配置习惯了，直接在这里打一个 spring 后面再跟 double 这样不生效的。


咱的根节点就叫 double 然后后面跟 application 是当前应用的名称，然后再下面这个 registry 这个就很重要了，它是注册中心的配置项。咱在前面的小结里了解过，double可以集成很多种不同的注册中心。那么咱在这里选择的注册中心是 zookeeper 并且它的地址指向了咱默认的 zookeeper 端口。 OK 下面的这个 check 它其实是一个启动时的检查，如果你启动的时候没有找到注册中心，那它这里就会抛出一个错误。我们这里把 check 指定成了 false 也就是说抑制这种检查，你即使注册中心不存在，我也能安然无恙地启动。


OK 在下面大家可以看到两个节点看起来奇奇怪怪的，一个叫 metadata report 另外一个叫 monitor 这两个家伙大家可以把它当做是 double 的配套设施。在后面的章节里，我将跟大家详细介绍。 double 除了注册中心以外，还有一个监控中心和元数据中心的概念，我们这里暂且不展开来讲了。


OK 那 double 这里还有一个比较重要的属性叫 particle 它是协议，这个节点下也有很多不同的属性。咱这里只选了一个必填的属性叫 name 咱在 name 中指定了它的协议栈使用的是 double 类型。在后面的图文小结中我还会带大家认识不同的协议类型。那 double 协议也需要缺省的一个端口来用作服务。发现咱这里如果没有指定端口，那么 double 协议将会使用默认的端口，就是2080。那同样的其他协议也有自己的默认端口，比如 RMI 就是1099，HD DP 就是80。 OK 这里就是 double 的核心配置了。


除了这些以外，还有一个老生常谈的 server 端口，咱给他写的就是63001。 OK 那到这里整个 W 项目也就构造完成了。不妨现在启动它的慢方法，看一下能否成功启动。直接对慢方法点击一个 run 让它跑起来，稍等半炷香的时间，看到 spring 成功一半。你看它这个 log 提示中前面跟我们普通的 spring boot 项目不太一样。它这里打印出的 log 带有鲜明的 double 色彩。你看前面三行把核心的几个 double 组件全给它打印出来了，包括版本还有 githubok 咱往下滑，看到最后一行 started 那证明这个应用已经成功启动了。


OK 那到这里，本节内容就到此结束了。在这个章节当中，我们创建了一个 double 的服务提供者，并且把它的接口层独立抽取了出来。那在后面的小节里，我还会带大家一起创建一个消费者，然后让消费者通过接口层发起对服务提供者的调用。 OK 同学们，那我们下一小节再见。

