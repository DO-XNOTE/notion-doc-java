---
title: 006.springbootweb搭建
---

# 006.springbootweb搭建

好在刚才的课程当中完成了开发环境的搭建，并且使用了 spring boot 的一个initializer，初始化了项目的一个架子。接下来我们就将使用 spring boot 去搭建基础的一个 Java Web 的项目，并且接入 mybetis 作为我们对应的一个 MySQL 业务数据库的一个接入。完成了这两步操作之后，我们才可以做真正意义上的一个业务。
系统搭建好打开我们对应的一个项目，刚才我们搭起了 spring boot 项目的一个最基础的一个架子，那接下来我们要做的是，首先我们需要移动一下项目的分层结构。首先在我们 com 点 IMOC 包下新建一个叫点评这样的一个包，然后将我们对应的一个点评的 application 1 到这个包下。那我们在移之前先稍微等一下，我们先将对应的一个项目分层结构大概介绍一下，我们对应的一个根包现在是 com 点IMOC。那我们现在想要将灯包加载到对应的点评下，那我们将这个点评直接移过去，然后点refactor，我们的系统就会自动将点评 application 对应的这样一个 package 给它改掉。


然后我们需要搭建项目的一个根目录结构，比如说我们会将项目分成好几层，我们有项目的一个 Controller 层，我们可以新建一个包建一个package，我们把它叫做Controller，然后我们可以在 Controller 上面写一些最基本的 Controller 的类。假设现在我们第一个要实现的是一个用户相关的 Controller 的一个服务，我们把它叫做 user Controller。好，那我们这个 Controller 就可以在这边先建好。


然后我们对应 spring MVC 有 Controller 之外，我们还需要有service，那我们自然要有一个 service 的package，我们可以在下面建一个最基础的 user service 好， Controller 跟 service 有了之后，我们还需要有数据库的一个访问层，比如说我们一般把它叫做 DAL 层，也就是 DAL 是用来处理数据库访问的，那我们有了这三个层之后， spring 对应的 Controller service 和 DAL 就有了。那我们还有一个叫 model 层，定义对应的一个模型对象。有了这几层之后我们就可以做一些基本的操作了，那我们再回顾一下这几层对应的含义。


首先 Controller 层是用来接受 Web 的一个 Controller 服务，然后会由我们的 service 层提供对应的一个服务， service 层会对DL，也就是 data access layer 做对应的数据的一个访问。那这个 model 就是我们贯穿整个项目对应的一个模型，完成了这样子的一个层级关系之后，就可以开始做正式的接入。
首先我们打开 home 文件，我们来看一下这个 palm 文件，就是我们做 Maven 的一个 palm 的管理的根基础。当我们可以看到它在我们刚才做 spring initializer 的时候，给我们加载了一个 parent 的一个 palm 属性，也就是说我们所有 spring boot 对应的一个 starter 都是基于这个 parent 的一个 palm 包，它默认使用的是我们选择的 2.1.6 的一个 version 的release。那我们其实可以看到在我们对应的 dependency 上面，目前使用了 spring boot 的一个最基础的starter，还有一个test，这两个都是没有指定 version 号的。没有指定 version 号它就会从最基础的 parent 这样的一个根节点去做对应的一个 version 的抓取。也就是说我们所有的 spring boot 依赖对应 spring boot 的版本都是不能指定的，这样的话它就会从对应的这个 version 去取，保证所有的一个 version 都是一致的。


好，我们来看一下，在我们实现对应功能之前，首先需要做几个事情。我们首先要指定对应的这个properties。我们其实可以看到这个 practice 目前指定的是 other 点 version 是 1.8 版本的，那光指定这个就够了吗？其实我们最理想的情况不光要指定使用的 Java 的一个version，还要指定对应的 source encoding 的version，也就是我们的 source encoding 的文件。我们保险一点指定一下 build 点 source encoding，我们需要指定是 UT F 杠 8 告诉 Maven 的编译的一个文件。
5 以 UT F 杠 8 的方式读取 source 文件。然后我们需要指定 Maven 是用来调用起来我们对应的 Java 编译的一个环境。那我们保险一点，如果一台机器上装了很多个 JDK 的版本的时候，我们需要强制指定我们执行，没问命令的时候，使用的是 Java 1.8 的版本。一个是source，还有一个是target，也就是说生成的对应的一个 compare 也是需要使用 Java 1.8 版本。


好，这样的话就保证了我们对应的一个 source 文件使用 UT F 杠 8 标准去解析，并且我们对应的 Java 对应的一个 Maven 都是使用 1.8 版本去做编译和运行的。那接下来在这边目前只有一个 spring boot STARTER，那我们现在由于是启动的是一个 Web 项目，所以说我们不光要依赖 spring boot 杠starter，我们还需要依赖 spring boot 杠 starter 杠Web，也就是说我们需要只使用 spring boot start a Web，也就是一个 spring MVC 这样的一些依赖的包帮我们做管理。


好，那我们首先来看一下 spring boot 杠 start Web 对应的这个项目引入之后会否有什么异样的效果？那我们在这边直接做一个更新。做这个刷新的操作，我们就会将对应的一些 spring boot 依赖的一个 started 的包加载到我们对应的工程当中。然后我们看一下这个 external library。


我们其实已经看到 spring boot starter 当中会给我们引入了对应的 STARTER gun、 Web STARTER gun tombcat 等等，这些 spring boots 需要启动对应的 Java 的一个应用程序所需要涵盖的一些内容。


好，那我们接下来需要打开 application 点properties。我们现在可以看到 vacation 点 properties 是一个空文件，当我们首先要指定这个 spring boot 的应用程序是启动在哪一个 Web 端口上？我们使用一个 key 值叫 Server 点port，然后我们可以指定项目启动在 8010 端口。好，做完了这个操作之后，接下来开始进入项目的一个配置。


首先我们来看一下我们之前写过一个 user Controller，当我们可以直接使用 user Controller 做一些文章，我们直接使用Controller，然后指定它对应的这个 Controller 的名字是叫杠user，然后我们可以指定对应的一个 request Mapping 的话，我们也把它指定为杠user。然后我们直接写一个方法， public 方法返回一个 string 叫test，然后我们 return test 这样的字符串。这个 test 方法需要指定一个是 request mapping，也就是访问这个 test 方法对应的一个名字，我们把它叫test。然后我们指定一个 response body，告诉它这是以 body 的一个字符串的方式去返回，而并非返回对应的一个页面。那我们通过这种样子的方式尝试着第一次启动一下我们点评的一个 application 启动。


好。好，我们其实可以看到 palm cat 打出来一句话，就是我们 on cat 对应的一个 started on port 8010 端口，那我们尝试着可以访问一下 8010 端口，使用 local host 8010 端口访问 user 杠 test 这种样子的一个路径。好，我们其实可以看到这边打印出来一句话叫test。这样的话就说明我们 dream boot 对应的一个项目就算是搭建成功了。

