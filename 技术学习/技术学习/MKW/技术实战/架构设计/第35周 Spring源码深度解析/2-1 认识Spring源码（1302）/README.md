---
title: 2-1 认识Spring源码（1302）
---

# 2-1 认识Spring源码（1302）

[image](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/b5df71b1-2606-473e-86f3-81d97d59d51d/SCR-20240803-llyt.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663X3TTKKI%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T232001Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQD9gaqAaUrHR7nn%2BYEGkE2yjWHvePRQMlGGokb6TOSzMQIgVczDoldEGGzRVOoDv3xkqSHH0g6HVA60WoeOnoFzMnAqiAQIxv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDJ7F%2BMRpHzboroMCJSrcA9s9AmyNj0ZTdFnsU9OXLQkPWOa2L23xGeFi0Sx5arHv%2BFhGecMmY4Wy07qfYUBKxd77aJaKIdgYm8ulO87Xyl0i87xAP7rpTNXYt6MU1NZzF%2FC9FEP7xMutMZVXVLlmbLvF9y4kRqT%2FWlnBCpjSNw3TZxIIm5phvn%2FOv4R6S90EFgJXjRpFjqzZg5rBi0cAl1k2ycbCK0IXltpPEfp0%2BBWgkvZwai1zKIqKj1rCpJZ4fs1nQQhomejpD4UuIusgf0CBjGqp1zUXR5ekMf4uvLdPK0GE1cpgl3XoNAkmrZCsDhlJynWNUH6ywcjf2tHiuORKzmSB2Lj%2FE2eUdWOA4Tk3Kt%2FczqPSRKcjoo4YmB6%2FiRhfLd4zRLTtyt3ppb1fehWq7GZrbhugigFJUt%2BJ92duDONTTmXgwPYTRFvs5LvS4M%2BWJApzbObjDpJQFzQd%2FPXKmMnZjPPybESsvyyOnQKwje0%2FixjJOOAwOxGHvjZqbghQ0c0Wlz8dP4QuCv3sJL5lh0%2FYpZb6GZoZ1X7O8QsSVFXHlti5Fx6hdi6MOjsKBQ%2FPyhezHXZu7zlFAaTLFVp6fGNsLBn0%2B4tPsi7srELnXV61Ov5sCfvVcTFYy%2FUAZAv%2Ba8CUreKH6xONMN23%2F9IGOqUBsozCjlHz%2BPSvjUu6kfRV8sAmpCUEmMuQae0ZtUSmcfo1oZCY0z5qZEfCy9qRdBRlQyaSiw12zTF3nCVk336RrF%2F5L8iobTV7RVD6iITZXqD7kBI5xeaKLcdDO%2BRgTJJTpsEbv7ZSTa99sVOI9Vg9oq40hrOR05I7d0pMeytgNROI3fuGGZ9oSdux9yYVP1mSBhf%2Fv9qVDjBZ%2FXf1uS3GNe%2BOcLIe&X-Amz-Signature=ec9b3b264db80606ff245c93b19b105a11ec78a1728ccc42a2eccf5f0f3fd5a4&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

同学们大家好，这一章节是认识一下 spring framework 源码，我们会通过源码介绍、搭建 spring 源码环境以及 spring 源码结构三方面来认识一下 spring 分布的源码。首先我们来看一下 spring 的源码介绍，我们知道 spring 的项目源码都放在 GitHub 上面，我们可以在 GitHub 很容易搜索到 spring 框架的源代码，可以看到在源代码里面，这个 spring framework 是非常受欢迎的项目。我们可以通过 water 数量和以 star 数量 fork 数量，我们可以知道关注 Spark 的人非常多，尤其是像这里面 issue 和 pull request 也PR，从这些数量能看到它的热度非常高。另一方面我们可以看到这里面的 commit 的进展，我们可以看到最近四天都有代码提交，所以说它的活跃度非常高。另外我们可以看到 release 的版本会很短的周期，里面都会有一个正式版本去 release 出来。


目前 spring Frameker 它 release 的最新版本是 V5. 三点儿一，我们可以看到在 V5 点儿三点儿一以后，它对于版本儿的名称有了一些变化，原来它会以 release 作为结尾，现在它就是直接以数字编号作为我们的写命名编码。这里面我们课程也会以 5. 1 最新版作为我们源码的基础去介绍。


3. 通过这所谓的内容我们还可以看到，其实 spring boot 它是基于 grade 去做了项目管理，同时它把项目划分了很多模块，从这里面我们能看到的像比如 string a o p， string beings， string context 等等多次 string 划分的这些子模块。


接下来我们去克隆我们的代码，去搭建我们的源码环境，跟我们的 spring boot 课程的计算内容是一致的。其次我们是需要Java，Maven，Griddle，Git， idea 等这些作为我们的基础环境，但这些环境我们在 spring board 课程跟大家介绍过了，希望这些安装对大家应该不是什么问题。目前的话，希望大家的机器上的这些环境都是必备的。


那么我们唯一缺失的就是获取 string 分 MOS 源代码，词本分为源代码，我们刚才可以看到 GitHub 的地址，我们可以在这里面去执行我们的获取操作。首先我们还是 get 克隆，我们去访问对应的这些例子，也就是我们注意一下，这里面是 spring protect 对应的 spring framework，如果说我们因为是 get have 的话，它外网的速度是比较慢的，如果说大家对这个速度比较介意的话，我们可以通过 get e 上面的代理，我们可以通过 get e 对应的镜像对应的 spring framework 去下载我们的代码。但是这里面有一点，我可能看起来会有一些别钮，这里面这样我们的 spring frame 可能都是小写给的 e 的镜像，它在这里面对于 s 和f，对于这个首字母注的大写看起来有些不习惯，当然也并没有别的问题，总的来说是 get e 下载我们代码的速度是非常快的。


好，我们下载完成以后，我们把我们最新的版本，也就是我们的 V5. 3. 1，我们 check out 杠 b 就是新建一个分支，作为我有 5. 1 steadily 这样一个分支，去对我们的代码去阅读理解，或者说是做一些笔记之类的一些事情，可以在这里面去看。 3.


那么我们把代码克隆下来，并且把新的分支拆改完成以后，需要校验一下我们的环境，对环境做一个验收，那么对于 string framework 的分支注意验收。怎么验收呢？还是跟我们 spring boot 是类似的，我们执行一下 get diff，我们把我们的 v 五点，三点 1- 2 点 steady 这个学习的分子跟我们正四版的 V5. 1 这个 Tiker 去做一个 DIFF 的结果，我们通过 w C 杠 w 去统计一下它的 DIFF 的差异内容是什么，只要我们执行完成以后能得到的 DIFF 差异为0，就说明我们在这个分支处理的并没什么问题。 3.
这一点处理完成以后需要保证我们当前 Gradle 环境是没问题的。如果我们当前版本 Gradle 是安装了的话，我们可以直接执行 Gradle test 的 class 去进行我们代码的编译， test class 编译和执行。如果说我们本地 Gradle 版本有问题的话，我们可以执行点 Gradle w，也就是说这个 grill 的包装器去执行我们 test class 的操作。注意一下，这个操作的过程是需要从远程下载我们的 griddle RIP 包，这个过程如果也是需要一些外部网络，可能会涉及到一些网络速度上的问题。


如果大家执行 gradle test class 没什么问题的话，大家看到的效果应该跟我这里面是类似的。我们在这里面看到我们 spring from 这个工程下面所有的这些 model 都已经点亮了，点亮也就是说被引入成我们项目的模块儿，通过这里面可以看到它引入的模块儿是非常多的，我们可以打开 setting gradle，这里面通过 include 的目录，所有 include 的目录都是在这里面对应我们一个模块儿，通过 include 这里面的直言结构去找我们对应目录的代码。比如说这里面的AOP，我们可以看到对应 AOP 下面的 spring AOP 的gradle，它这里面去设置了我们这个模块符合依赖的内容。在这里面我们可以看到真正依赖内容，也就是我们的 spring beans 和 spring core，其他的依赖我们可以理解为可选依赖和我们的测试依赖，这是我们看到编译完成的效果。那么对于这些模块的内容，我们可以跟大家去简单地过一下，我们看一下。


首先通过这里面可以看到这里面大概二十几个项目模块。首先我们去了解一下我们的整个 string 源码的核心，核心内容是包括DI，也就是 IOC 和 AOP 和我们的一些 event 文字SPER，也就是与表达字相关的内容涉及哪些包？比如这里面首先是我们的容器，也就是 spring bean，这里面是重放我们的 DI 容器。 spring context 也是我们的 IOC 容器，但是它的功能要比 beans 更强大一些。 beans 它只是提供了一个容器的一个注入和获取，那么 context 它会把我们跟四件相关资源获取，和我们的一些属性文件相关的一些操作都会放到这个里面。这里面还有 context index 的和我们 connect support，这是对我们容器的一些内容的一些辅助性的操作。 index 它会在我们打包的时候生成一个索引，这个索引就是说我们所有需要去容器装载的一个目录，这样可以提高我们在容器启动时查找的速度。 spin contact support 它是给我们提供了一些边缘的支持，比如像涉及到缓存的，或者说定时任务的相关的一些依赖，它是在 context support 里面操作的。


spring call 就不用过多介绍了， spring call 其实是所有的项目基本上都会依赖到call， call 是提供了一些公共的基础的服务和一些公共的一个 YouTube 类。这里面还有我们的express，也就是 spring 提供的表达式， spring 的 er 表达式在这个里面提供它的定位也是非常基础的。


很多项目它们依赖的内容就是 spring CRO 和 spring expression，可以说我们 spring 一二百单四作为一个非常基础的应用，可以说我们大多数模块去使用，我们看还有 AOP 相关的内容，这里面是instrument，它的功能是跟我们 spring 的，它对预编译的一些信息去做一些功能。


我们接下来再看我们的 Web 相关的内容， Web 相关的内容，这里面主要来看下面，这里面有 spring Web、 spring Web flags、 spring web VC 和 spring Web SOCKET。我们的重点是 spring Web Mac，因为 Web Mac 它是依赖了 spring Web Flex，我们也会介绍一些它的一些基本原理。对于 Websocket 我们可能会不会碰出太多的精力？接下来是 data access 数据访问，这里面主要包括我们的 spring text，也就是我们的思路，还有 spring d b c。这里面还有我们新加入的一个模块叫 spring r to DBC，对于这个模块跟我们对应的 Web Flex，它的异步操作是对应起来的。这里面含有 spring OM，也就是我们跟 ZP have done 的集成所用到的一些 arm 框架的一些扩展页的东西，还有 OXM 也是一些数据映射的功能，但是这块儿我们不会过多介绍好，这是我们跟数据访问相关的内容。


接下来是 spring test 相关的内容， test 内容主要是对应一个 spring test 包，这个 spring test 这个模块它支持了我们 core Web 和 data access 相关所有这些功能的测试。当然它的测试还依赖一些外部其他的一些测试包，比如像最重要的像unit，还有mock， ITO 和一些test， NG 等等这样一些外部组件。


这里面有一点我们可能还没有提到的，比如像这里面的 spring JCL，它是 spring 为了解决沼气依赖日志的一些主键的一些适配关系，所以把我们的日志主键提取出来一个 JCL 作为一个桥的过渡。这可以说是我们整个 spring 框架主要这些模块儿，我们通过源代码去更多地去感受一下 spring 框架这些源码库的内容。通过在这里面，我们首先通过我们最根的 setting gradle，通过 setting gradle 我们可以理解我们整个源码模块里面 include 的这些模块都有哪些内容。


另外我们可以看到我们 Gradle 引入的版本，这里面我们可以看到对应的 Gradle 的模块，我们在这里面有一个 Gradle 的引入，这里面Wrapper，我们在 Wrapper 里面可以看到 read the upper proxy 设置，这里面它是有一个版本对应的内容，我们从这里面可以看到版本，它现在是 gradle 6. 7，这个你可以跟本地的程序我们的 gradle 的杠 version 去匹配一下，看是不是 6. 7 的版本。


如果不是，这个版本的最好跟版本是匹配上一致的，但是其实这些项目构建的版本其实关系不是太大，因为对于spring，它在前个版本我们可以看到它是 10 月 15 号刚对版本进行更新，它在前一个版本它用的还是五点多的内容，我们可以从这里面去看一下，去比较一下在这里面我们的上个版本它是 5. 4，那么它现在就更新到了 6. 6. 7，所以说这个跳跃还是比较大的好。这是它的一些版本的信息。


那么其他的一些编译构建的方式，我们可以看到这里面 build 和 s r c，这里面提供了一些编译构建的一些策略呢，可以理解为是我们整个源码库的内容。我们先大概了解了这个 spring 源码的它的源码结构，后面我们会针对具体的章节来去深入的去介绍，像我们的 LC 和AOP，包括我们 Web MVC 执行的流程，涉及到的源码一些过程的跟踪。


我们看了 spring 的源码，我们再看一下我们的学习的这个工程，对于这个工程来说，我们在讲 spring boot 的时候，我们选中的是二点儿三点儿 4 的版本儿，当时的最新版本儿，目前 spring boot 它已经更新到二点儿四点儿 0 的版本儿。


那么我们为了使用 spring framework 最新的版本，也就是 5. 1 这个版本，那我们需要把我们的版本号拿通过 2. 3. 3. 4 更新到 2. 0，因为在 stream 部的 2. 4. 0 这个版本，它默认依赖的是 5. 4. 3. 1 这样一个版本号，但其实整个它们依赖的变化并不明显，为变化比较大的，也就是说我们的 r to d b c 这个模块只有在 5. 1 以后才有的，这是一个最重要的更新的原因。


3. 我们把这个更新完成以后，那么我们可以看到我们下面是 spring LC 这样一个 Demo 模块，它里面所依赖的 spring Bing 和 spring core 这些版本，它都已经变为了 5. 3. 1。我们对 spring 源码的前期的了解先介绍到这里，后面会通过 showcase 的示例和源码跟踪的方式，深入的去介绍核心流程的执行过程。同学们，我们下一节再见。


