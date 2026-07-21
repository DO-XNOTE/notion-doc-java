---
title: 011.页面请求资源处理
---

# 011.页面请求资源处理

好，同学们，那我们继续刚才的课程当中我跟大家介绍了通用的异常处理的流程，定义了一个通用的返回错误码，以及通用的正常的一个请求响应格式。那接下来我们处理完了动态请求的一个处理之后，我们要做对应的一个静态请求的处理。那静态请求的处理在我们这个项目当中分为两大类。第一大类是真正意义上的静态资源，也就是说不需要服务端 Java 代码的一个参与和渲染，直接输出 html 文件的一个静态资源。第二种是使用 spring boot 的 semlive 的一个模板引擎的技术去做对应的一个动态的服务端的渲染，最后输出一个 html 文件给到前端的一个过程。


那我们首先来解决纯静态资源的一个接入的过程。当我们需要在对应的 application 点 proxy 当中加入一行，我们把它的注释写一下，叫接入前端静态资源页面。这个时候我们加上 spring 点MVC，点 static 杠 pass 杠pattern，那这个参数的意思是说我们将定义一个 pattern 的正则表达式，用来将我们对应的一个 URL 符合这个正则表达式的一个路由去寻找预设定义的一个静态资源。那我们在这边加入一个 static 杠行星。也就是说当我们的前端访问杠 static 这个目录的时候，所有的后面的请求把它当做静态资源文件去做对应的一个处理。在做这样的一个操作的时候，我们需要在 resources 目录下定义起对应的一个 static 的directory，然后我们假设写一个 test 点 h t m l。好，这个时候我们写一个 test h t m l five，然后启动一下应用，看一下对应的效果是否真的如我们所想的一样。当前端访问 static test 点 html 的时候，就能拿到我们对应的一个请求的响应。好，打开我们的 Chrome 浏览器，我们在这边输入 static test 点 h t m l。


好，这个时候我们其实看到并没有像我们想象的一样输出对应的一个文件，而是直接是找不到对应的执行操作的路径，也就是说类似于 404 not fun 这样的一个请求，那我们来看一下问题出在哪？打开我们的 application Pro case，这个时候我们需要在这边将对应的这个之前设置的 add mappings 原本是设置false，这边必须要设置成true，那这个是什么原理呢？我们在这边加一下对应的注释， add mappings 等于true，表示如果所有的 Controller 都没有命中，则使用默认的静态资源处理器做匹配。也就是说我们刚才 add Mapping 设置成 false 的意思是为了让它 404 的时候抛出对应的一个异常。那这边设置成 true 的时候是说如果说所有的 Controller 都没有命中的时候，我们再去做一把匹配。用什么匹配？用我们系统自定义 spring boot 自带的一个静态资源处理器，也就是我们定义的这边 static pattern 去做最后一次匹配，在没有匹配上抛出 404 异常，若匹配上了，则以对应的一个静态资源的请求去做解析。那我们来看一下设置成 true 之后的效果。


我们尝试着轮一下，看到这边 test h t m l file 已经出来了，那我们回到刚才，我们找一个 user at ID，等于一正常的动态请求也出来了，那我们改变一下对应的一个UL，改一个看不懂的，仍然能够被正确的捕获到，也就是整个处理的一个链路，是首先找对应的这样的一个 UIL 是否能匹配到Controller？如果说匹配不到Controller，尝试着匹配我们这边定义的一个 static 的一个pass。若再没有匹配到，那不好意思直接抛 404 异常。


那解决了这样的一个问题之后，我们在这边再来试一下，我们其实可以在这边定义成千上万的一个 h t m l，比如说 index 点 h t m l，我们把它叫做首页，然后我们再次启动一下，朋友们在这边修改一下 static index 点h。


天猫这边我们可以看到报了一个乱码，那原因是我们对应的这个界面的处理上面并没有告诉浏览器，我们需要以 UT F 杠 8 的格式去做对应的一个解析，那我们直接在这边把它搞成完整的一个 h 天猫的格式， doc type h t m l，然后在这边指定 h t m l，指定对应的一个header，在这个 header 内指定Meta，告诉他说okay，我们需要以 character set 是以 UT F 杠 8 的格式。然后我们在这边使用 body 关键字将首页搞到 body 里边，好重新启动一下。也就是说我们依靠 HTTP 的 header 告诉它方法要用 UTF 8 的编码去做对应的一个解析。好，刷新一下，我们可以看到首页就可以正常的显示了。那解决了静态请求的一个静态资源文件之后，我们接下来要解决使用 semlive 模板去做接入的一个动态模板的渲染。那我们首先停掉应用，打开我们对应的 palm 文件，我们需要将 spring boot 对 SEMIF 模板的一个依赖引入进来。那我们对应的 hobby 一分下来，我们把这边改一下 spring boot starter seem live。我们把对应的这个 semleaf 模板 copy 下来之后需要 Maven update 一下，然后将对应的依赖的价包下载下来。


那接下来我们要做的就是打开我们对应的 application 点 properties 文件，我们在 application 点 properties 文件当中需要多引入两个 semiff 相关配置，我们写在下面 Steam live 相关的配置，第一个配置是 spring 点 semlive 点prefix，也就是说我们对应的一个 seamless 的一个模板文件放在哪儿？我们指定我们放在 class pass 下面一个叫 templates 对应的一个目录下。第二个我们要指定 semlive 的文件的一个 suffix 后缀。我们就使用最简单的点 h t m l 后缀，然后我们在对应的这个 resources 下面需要将对应的 templates 建起来，建一个 templates 目录。


templates。然后我们仍然一样写一个测试的一个html，我们假设写一个叫 index 点html，那写 SEMIF 模板的方式其实非常的简单，就跟我们写 html 文件一样。当然我们首先来解决 semift 一个测试接入的问题。我们随便写一个字符串 templates index，然后我们怎么使用对应的这个 semlive 呢？那使用对应的 semlive 其实全靠 spring MVC 机制当中的 model and view 这样的方式去做对应的一个简单的接入即可。


那我们接下来看一下怎么样子将本文件接入进来，那我们进入唯一刚才实现的一个 user Controller。我们在 user Controller 当中我们之前已经写过一个test。那我们在下面再写一个，我们假设返回是一个 model and view，我们可以看到返回 SEMIF 模板必须得使用 model and view 的方式。我们取别的名字叫index，然后 new 一个 model and view。你又出来一下。 new 出来的时候我们需要指定一个，我们读取哪一个模板，那我们这个根其实就是templates，我们打开根就是在 templates 下面，我们直接读取 templates 下的index，点html，然后返回 model and view。好，然后我们在上面指定对应的一个 request mapping，加一个 index 这样的一个路径。好，然后我们启动一下应用。这个时候我们可以看到对应的这样的一个路径，就是 user 下面的一个index。 user index，我们可以看到 templates index 就这样展示在了我们对应的界面上。


同学们可能会问我使用动态渲染的方式使用了 model and view 输出了一个 index 点html，那看似好像对任何的一个性能上面也好，逻辑上面也好，没有任何的帮助，仍然是返回一个死的静态资源文件，那其实既然要用到模板，那就不得不说模板文件中的一个变量替换，那我们可以来看一下。


假设我们在这边有一个变量，这个变量是username，我们假设这个username，我们把它叫做IMOC。然后我们需要在对应的这个 model and view 当中 add 一个object， add object 有一个 attribute name 和 attribute value，那我们先来讲一下对应的一个 attribute name。那 attribute name 是不能为 null 的，那我们指定一个 name 作为 attribute name value 的话就是这个username，然后我们在 index 点 h 天猫当中怎么去使用它呢？其实很简单，我们假设这边有一个 p 标签，我们需要在这个 p 标签内打出对应的这个 IMCIO seed user name，我们直接使用 CF 模板的 TH text，然后使用这样的一个括号，我们来尝试着启动一下。


好，我们可以看到 IMOC 在这边被作为这个变量使用对应的一个大括号所替换掉的一个 attribute name 从 Java 的一个变量当中传了进来，并且配合 t h 就是 semlive 的一个简称，使用 t h 冒号text。 text 的意思是说我将对应的这个 HT 猫的标签的 text 设成了这个使用 name 变量替换掉的一个value，那至此我们的整个的项目的一个初级的框架就搭建完了。


来看一下我们在整个项目的一个初级框架当中，首先使用 spring Boots 搭建了我们的一个 Java Web 的一个项目，并且使用 mybadcase 做了一个 MySQL 数据源的一个接入。最后业务系统做了通用的一个 response body 的一个返回处理，以及对应的一个静态资源动态文件模板的一个接入。


那接下来我们要带着大家一起来完成我们的一个业务系统的一个搭建。那我们回到课程开始跟大家讲解的这张图，我们在这节课程当中已经使用了 spring boot 加 Mybetis 搭建起了一个项目的基础骨架。在之后的课程当中会分别去实现对应的一个业务系统的一个功能模型，以及搜索推荐服务的一个接入，那我们在业务系统当中会去实现运营后台、商户服务类目以及门店的业务系统的功能，并且在对应的一个业务系统的基础上，我们使用 MySQL 做搜索推荐点评 V 1.0 对应的一个版本去使用 MySQL 接入了搜索及推荐的一个服务，然后我们会发现 1.0 架构的一个不足以及缺陷。将对应的架构演化到V2.0，也就是在业务系统的基础上，使用 Elastic search，即 Spark machine learning Lib 去做一个 2.0 的搜索推荐服务。


对比于 1.0 架构的 MySQL 的服务，可以看到 ES 及 Spark 马逊伦的 Lib 应对这样的一个业务场景的一个强大的功能。好，那接下来我们就进入后续的一个课程。

