---
title: 1-10 基于Dubbo-Admin的服务治理-1
---

# 1-10 基于Dubbo-Admin的服务治理-1

[image](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/d17bc4c2-ab41-4df1-82d3-094ad435b32d/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TL7YI2TS%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T225859Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIEANVlbb5op8E4aVTLbQnqOmQyTTNDyupq49HzYUlCNVAiAWcbxd2AZ0rGwCNsLAuOq8QdIo4P0im2KUfYMF9lrU5yqIBAjG%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMd7NbcBimCldm8UNLKtwDfoLbZ0pzLn%2BbdqorPlBbciPwndcNg9o0qf1DTtqCStx1Qub9W8zeF4xN5jKxGsS7C%2FzHJIeXKJn3rw1WYOCjKbd3C9CzF7Rw%2FJWRwd3DALP1aPnNPK80dBeThHuvsnp4XqRSt1poQiQq8QNb238ihbKZnxKoXsnbrdGoq1ElSfHqhsFX7aDYaEiYugAEaPWZC%2B0RsVpUdWlb7EDgmn3kgUp5QpW%2BaOq2shVRksjFU37tBkIlGmlxkus%2B2Sj%2FffBsVmJii6h4qye80nzsu9r%2FWrHaaxt0Lz01DHFDSMiOZBQcaQ%2ByFwc1LFbvsiteccEIQHAGPmVPBjVhxAX0RiQZDMYgL5W%2BX6ezdMo3%2B0OI24u7Dv3P%2FaZKqRhXVLo1D56TC%2Bdo4CEZ3pkYg5tlLQCA4ViH2eZrIt5ERKBl2OVSoJKRy6U6huiMGaJ7o6Dac5Gbqf%2FawI6bGD1eajF%2Bk6CIcRWEX7dMKsfqeknhTPRorEAtW21lT4Ziio%2BTBVj%2BaT%2BDXXkEv0qdvf81dzVj3NQF2w3oJOLvuF8BhomXN4Y6qDM12sG86XNS0Gufm68os9nO9pp5oEen6vegWKKTiScQ2g8T%2BADqyAoOsVrZ51k7G8zP1X31ot1TlYefrsowirr%2F0gY6pgGWVv5h0l9wesC9s2cSpHhF1xH3KiGNLCO%2FTmV7Kcz8xcECkLB%2BbksR9nQWMJ%2FH%2Bql3B%2B6Mk%2BY2ByVS%2BgaqD8esOAOK%2B68Mb%2FOrMAdyXJTYCIW2P8qjgHz20VmRw1KajOcKZDJyGD7Vi8QGI6b3dAImREPQ7KWczn1D0Z7J%2FnyxVYQ%2BJRXvVeor75QRkYxfnJgbTTyLfbrDo%2F5fmDXEY5TmwP9Ll47F&X-Amz-Signature=9167aa83b6cc314b0734b1a994d234732dc94e4fad0d8a2e6844b309b06c6ad3&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

[image](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/64efd911-2ad7-412b-b889-ece8367cb991/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TL7YI2TS%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T225859Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIEANVlbb5op8E4aVTLbQnqOmQyTTNDyupq49HzYUlCNVAiAWcbxd2AZ0rGwCNsLAuOq8QdIo4P0im2KUfYMF9lrU5yqIBAjG%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMd7NbcBimCldm8UNLKtwDfoLbZ0pzLn%2BbdqorPlBbciPwndcNg9o0qf1DTtqCStx1Qub9W8zeF4xN5jKxGsS7C%2FzHJIeXKJn3rw1WYOCjKbd3C9CzF7Rw%2FJWRwd3DALP1aPnNPK80dBeThHuvsnp4XqRSt1poQiQq8QNb238ihbKZnxKoXsnbrdGoq1ElSfHqhsFX7aDYaEiYugAEaPWZC%2B0RsVpUdWlb7EDgmn3kgUp5QpW%2BaOq2shVRksjFU37tBkIlGmlxkus%2B2Sj%2FffBsVmJii6h4qye80nzsu9r%2FWrHaaxt0Lz01DHFDSMiOZBQcaQ%2ByFwc1LFbvsiteccEIQHAGPmVPBjVhxAX0RiQZDMYgL5W%2BX6ezdMo3%2B0OI24u7Dv3P%2FaZKqRhXVLo1D56TC%2Bdo4CEZ3pkYg5tlLQCA4ViH2eZrIt5ERKBl2OVSoJKRy6U6huiMGaJ7o6Dac5Gbqf%2FawI6bGD1eajF%2Bk6CIcRWEX7dMKsfqeknhTPRorEAtW21lT4Ziio%2BTBVj%2BaT%2BDXXkEv0qdvf81dzVj3NQF2w3oJOLvuF8BhomXN4Y6qDM12sG86XNS0Gufm68os9nO9pp5oEen6vegWKKTiScQ2g8T%2BADqyAoOsVrZ51k7G8zP1X31ot1TlYefrsowirr%2F0gY6pgGWVv5h0l9wesC9s2cSpHhF1xH3KiGNLCO%2FTmV7Kcz8xcECkLB%2BbksR9nQWMJ%2FH%2Bql3B%2B6Mk%2BY2ByVS%2BgaqD8esOAOK%2B68Mb%2FOrMAdyXJTYCIW2P8qjgHz20VmRw1KajOcKZDJyGD7Vi8QGI6b3dAImREPQ7KWczn1D0Z7J%2FnyxVYQ%2BJRXvVeor75QRkYxfnJgbTTyLfbrDo%2F5fmDXEY5TmwP9Ll47F&X-Amz-Signature=04d3e38bd7bf013d0b90c82f460d030af8048a72dfa8eac3b34d035d702262eb&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

hey 慕课网的各位同学们，大家好，这一节咱来学习基于 double admin 的服务治理，同学们不要被吓到了，这不是一个新的服务治理技术，它是什么呢？只是一个帮助我们管理 double 服务的界面。但是这个 UI 管理界面可有点厉害，咱来看看它厉害在什么地方。


我们首先来介绍一下什么是 double admin 它都能干些什么事儿，咋说它是帮我们更好的管理组织 double 服务的一个界面。所以它这第一个功能一定是服务治理的可视化。那在这个界面上我们都能操作哪些内容呢？我就来随便挑那么几样跟大家说一说。


好了，一个是我们可以设置路由规则，比如说条件路由、标签路由，甚至还可以去设置黑名单白名单。除此之外，我们可以给每个 W 服务设置权重，指定它的负载均衡，以及在界面上拼装 request 发起一个服务测试这六项功能只是随便挑的小技能。 double admin 它能做的事情可多着呢。那咱了解了它的基本功，接下来看一下它都有哪些组成部分。 double admin 实际上是由一个前端工程和一个后端工程组成的。它的前端工程使用的是现在比较流行的 vueg S 还有 volatify 来实现的。那后端工程就是一个标准的 spring boot 工程，咱如果想要在本地跑起来，这一套工程需要同学们先去安装 Nodejs 这样的话咱就可以在本地执行 npm 命令了。


对 double admin 有了基本的了解以后，我们再来聊一聊 double 版本和服务治理的兼容性的问题。 double 在 2.6 和 2.7 版本之间有一个比较显著的变化，比如说在 2.6 版本的时候，它的所有信息都存在于哪里注册中心这里，比如说咱在前面 demo 中使用的 zookeeper 但是到了 2.7 版本以后，这个情况发生了变化，注册中心还是那个注册中心，但是 double 这里又多出了一个配置中心和元数据中心。那在这里面元数据实际上指的就是像服务名、接口名以及服务的版本号等等。之前这些信息是全部丢给注册中心来做的。所以这个注册中心的数据结构就会显得比较臃肿庞大。


那在 2.7 版本里， double 把这部分信息抽取了出来，专门放到了源数据中心当中。那配置中心也比较好理解，它是为了实现配置的集中管理而构建的一个外部化的配置中心。 OK 那到这里咱的理论部分就全部学完了。接下来我们看一下本章的动手环节。我们把 double admin 的部分分为上半场和下半场。咱在这里完成前面的一部分准备工作，我们来看一下这里面包含的内容。首先咱要下载 double admin 这里给出了一个 get hub 的地址，我们可以在阿帕奇的项目空间里面找到 double admin 组件，这里只要把它下载到本地就可以了。


接下来第二步是安装前端工程，我们要确保本地已经安装了 Nodejs 也就是说可以执行 npm 指令了。在这里我们对着前端项目执行 npm install 指令，但是首次执行下载的组件会非常非常多，所以需要大家把 npm 的代理添加上去。否则下载速度简直就是龟速太慢了。 OK 同学们，那准备好的话我们就动手开工。


编程是我快乐 996 是我的福报，咱最后享受福报的几次机会，大家好好的珍惜咱这里在运行 double 的命之前要做那么一些准备工作，什么工作呢？第一步自然是大家要到 git 中把这个 double admin 给它下载下来，在这里从 git 上下载 develop 这一个分支。不过大家如果没有挂代理的话，会访问得非常非常慢。所以我这里把这个项目也给下载到了本地，那就是咱在 double 文件夹下的 double admin developer 这个项目就包含所有的源代码了。大家如果想体验那种从头到尾一次通关的感觉，那就自己受虐去下载。剩下的同学们就直接使用我下载好的这个项目就可以了。


然后接下来咱要编译前端项目怎么编译呢？第一步，我们要安装 node JS 这里的各位老司机就自己各显身手了，百度谷歌用起来把 node JS 给安装上去。然后先别着急执行 npm 命令。因为第一次加载它的包比较庞大，我们需要在这个配置当中添加一串 registry 的地址，我们打开命令行。然后把这个文件给大家看一下，直接用 VI 把它打开。在这里，整个文件空空如也，只有。这一行就是我在这个 read me 文件中写上的 registry 等于一个 HTTP 开头的镜像网址。那把这个镜像添加在文件中以后，咱下载包的速度就会非常非常快了。


等这个镜像添加完，咱到 double admin 项目下面的 double admin UI 中，大家注意层次结构，要到这个项目当中，这里面有好多个文件夹，咱到 double admin UI 里面执行 npm 命令。那咱不妨第一次来尝试着安装一下。我们把项目路径 copy 下来到 terminal 里面，走到项目路径下，然后直接打起 npm install 命令，这里将会去拉取 npm 的包。同学们你看这个拉取速度其实非常快的，因为咱去使用了它的镜像服务。好刚才半炷香的时间已经过去了，然后整个项目已经 build 完了，大家如果看到没有任何报错的话，那这里已经是安装成功了。大家如果想直接抛弃这个项目，就执行 npm run DEV 咱现在先不着急来启动，等待会儿咱全部布置妥当之后，把后台应用、前台应用一起启动起来。然后到 UI 界面上去看一下 double 注册服务如何通过图形化界面的形式来管理。


OK 同学们，那这一节就讲到这里了，在下一节当中，我们将启动整个完整的项目，咱也快要到完结篇了。所以后面几节学习课程不宜太累，让大家放松。 OK 同学们，那这一节的内容就到这里结束了，我们下一节再见。

