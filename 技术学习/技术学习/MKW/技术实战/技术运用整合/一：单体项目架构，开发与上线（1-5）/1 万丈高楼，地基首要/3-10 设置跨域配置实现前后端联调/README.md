---
title: 3-10 设置跨域配置实现前后端联调
---

# 3-10 设置跨域配置实现前后端联调

[image](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/53bdae36-f7df-4221-9449-d4042bd1634a/SCR-20240816-tpbv.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YJ7YVFBN%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T224629Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIG82%2BJ5nXoa%2FvmYtaWoStJp2PsEgb0Z3ZO0z%2FtMWc7qRAiEA6MAH9yt%2B2DbqSCRwL32XC%2FkmvWkt1iGmgToKpvo%2FKN8qiAQIxv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDEkmEm0kL8nRa7v1bCrcA8OOICR0EIWP2ZrLT9Q8X4nqLgMVWvcQhYk1BKJbtKuKwSofc3%2BMy1A8PAAQ%2FuUZt19XXmQkX8zpPosoDoS4EM6He4%2FXbYD0mVFp1TmMs32NYbUAeevsItaTeNR6SVw9W7CiZ1Z3ZUL5OvXSGCvaqX9P49ypBsrD48qV%2BjUcJJ4htRlmjfaUNavvq2YrKpmpwwuukqhokCa%2BqawsWdiSfjB9IgCCzeKzhBSVxDQ14ywPMQEuAY1EMKFJ3zdOv0oL4yEDe3BEeE7J%2FUkWhzKzXOpzNwrKSzGjk4WSHUFHatRDQycHdcMwm8g4ruaxfwDiodBEzzQehWGv2Gusef%2BaeviC%2BCDbPBGFNRsCxIDavbZltA2h32HZN0pDU1F0xHnvgtAIaTKuWTPuDwBuSbjhBVSSMFQxdJv5jqopkfdHpPhSoPkLK6EGCgWf3y%2BHS9VPcayxCdExXgOviMvU2tOeTWSe0%2FtYYbUVceRox7nu64DGolRLgTbDiKcaXcEQvR%2F%2Fm5%2BSC9AMLA0fCP1Skh7SrwrjM0x2dP1FETCm3t%2FQWjymMDqdrrw0TYCM9wI3utnssPL%2FZEJdSiF2ELFXXnhOZvnm157X0YroJZvF2Fjasy0ifbhd%2BvFZ7ygSNHDjMIq6%2F9IGOqUBc5SW4HMgi05qRWaUXNNvoUc6x5dtqyij05fGTg7JzGA2sjb%2BYS1KY139wo6DewbHbyE9Sx5rFER3%2Fc%2FMz0UUQiqIzGOlK5jJIwaVqikJNlQdPOX2ClWAHt0tdTrlySFH5mkpYCDXwoNdaJgXhHmS3torwYOtj%2BtReCqT5em9jRR%2F38T%2BIptprpdqwUOGnEidRjbx7AulxeYY1YlGT7Lx9wlvr%2FlP&X-Amz-Signature=27d7a0ea3974b3e3e742eeaee8263ae5362ad6398538ab5435615158ef4b9795&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

现在我们的 Tomcat 服务器是运行了，以后，我们也能够去访问一下我们的静态页面了。很明显我们现在是无法请求到我们的后端的。我们点击注册，在注册里面我们是也无法发送任何的请求。按F12，很明显在它的控制台也会有很多的错误。OK，现在我们就需要来看一下如何去修改我们的前端的源码。


其实要去开发前端的一些功能模块的时候，其实是会有很多的一些开发工具，我在这里使用的是来看一下，也就是 c s code 是这个工具。这个工具是由微软所提供的，我个人认为是非常好用的，目前来讲其实也是比较主流。当然你也可以去使用 h 标的，或者有 subline idea where storm 其实也都可以去进行开发。当然你要使用 CXT 文本也没有问题。在这边我们就来看一下。大家可以自己根据自己的一个喜好去下载各自的一个开发工具。在这里我会推荐使用 c s code 打开。 c s code 打开以后，就可以把直接选择选中项目往开发工具里面一拖拖进去了。以后等待一下片刻，这个项目就会被加载到我们的开发工具里面去了。


我们简单的来看一下前端源码的目录，虽然我们不用去开发，去实现前端的内容，但是其实前端里面所涉及到的一些业务我们是需要去了解的。先来看一下我们的目录结构。首先这一块内容其实都是一些静态的资源，有一些图片，c、s， s 样式，g、 s 脚本等等。都在下面的这一部分。全部都是h、t、m。我们首先来看一下注册，注册的是在Redis，这个页面里面，我们其实是可以来看一下的，在这边我们可以适当的去放大一下。我们就可以来往下面看。注册的时候其实在下方会有一段 GS 的一个提交。这里面其实是什么？是feel。之前我已经是说了，在有一个 readest user，这个是用于去做注册的。这一部分是判断一下我们的一些用户所输入的内容是不是符合要求，是必须要去进行一个数据的校验的。随后构建了一个 user Bo，这个 user Bo 很明显是我和我们后端所一一对应的，也就是我们在后端来看一下。在后端我们找一下Bo，这个 Bo 里面所涉及到的一些内容， user name password 以及是 confirm password。你必须要和前端的要进行对应，或者要让前后端都要相互的对应，如果不对应，在后端是接受不了这个值的。


OK，好。随后再来看到这里，在这里其实它就会有两个相应的一个内容了。两个参数主要是一个 server URL 和一个 return URL。不用管，其实是用于去做一个页面的重定向的。我们主要是要看这个 server URL。这个 server URL 其实就是和我们后端去进行调试的时候，它所需要的一个地址。这个地址看一下拼接了后面的 passport 杠register，这个就是一个注册。


OK，来看一下 server UL 是在哪里定义的，它是写在 APP 里面。 APP 又在哪里？ APP 在我们当前页面这个地方是引入了一个JS。来看一下。 APP 是在部位展开以后有一个 APP 点 JS 打开以后，在这里有一段内容我们是需要去进行修改的。这两块内容适用于去干嘛的？其实主要我们设置了开发环境以及是生产环境的一些 URL 的地址，我们只要来把这边的一些内容去做一个修改就可以了。


目前我们所需要去修改的是哪里？是这一块内容是 server u i r 对应的是啥？是对应到接口服务的一个接口地址接口服务就是我们的 a p i OK，所以在这个地方我们只需要把改掉，改为 localhost。后面的 8088 端口号其实和我们在后端所定的是一致的。在 y m l 里面，这里是 8088 OK。好，现在其实 server UL 就已经是设置好了。设置好了以后，随后我们返回到前端页面里面，我们来刷新一下。以后我们再来试一下。我们先把 F12 展开， F12 目前在控制台没有任何的错误。我们来一个Imock，当我们输入的时候，其实它会发送一个验证，这个验证也是要和后端去进行一个联调的，这个是判断我们的用户名是否存在。来看一下。在前端控制台他报了一个错，这个是我们在后端所定义的一个接口，他会报一个什么错，他会说一个 from origin。这个是我们前端，这个是后端，他会说什么？他说现在是被 block 了，也就是被卡住了。卡住的原因是什么？它有一个c，o，r，s，这个代表的是一个跨域，看到它有一个access， Ctrl allowing。这就是一个跨域的内容，我们是需要去设置的。


如何去设置跨域，或者什么又是跨域？我们来看一下现在其实我们在当前静态服务器，也就是 Tomcat，它所运行的是一个 localhost 8080 这一个端口，我们在后端所运行的时候，其实我们后端它所启动的时候，它是好在它是在这里。 8088 端口，其实对于我们前端来讲，前端的服务器要发送请求到我们后端的另外一个服务器，两个端口完全不同，它其实就会有一个安全的因素，所以这也是一种限制。我们如何来打破这样的一个局面。其实在我们的后端，其实在 spring boot 里面，我们就可以去设置一下跨域的问题，如何去设置。我们来看一下。


在我们当前的 config 里面，目前其实有一个 Swagger2 了，我们可以来再一次，我们可以来创建一个类，这个类也将作为一个配置类，会被我们的容器去进行扫描。我们可以来定义为一个c、o、r、 s 来一个configure。好创建这个类成功了。既然要被容器扫描到，很明显在它的上方，你是需要去加上一个艾特 config 这样的一个注解。随后我们在这个类里面我们加上一个构造函数，在这个下方我们就可以去建一个病了。这是一个什么病？它其实是一个 Cos 标特，它是一个过滤器。来看一下。有个叫做 Cos filter。来看一下，这里边会有两个。


首先第一个写一个注释。第一步来添加 course 配置信息。第一个就有一个 course configuration。来看一下是直接作为一个 config 来 new 出来。在 config 配置里面，我们就可以去添加一些相应的内容了。比方我们可以来 add 有一个allow，能不能看到有一个 allows origin，这个就是添加允许的跨域信息的内容，也就是我们的前端。我们的前端是哪里，我们在这里去进行一个添加就可以了。我们前端是 h t p，冒号是 localhost，再来一个冒号8080，这样子，其实我们就为它添加了一个前端请求的，相当于是一个调用端。OK，不建议在这个地方使用一个星号。有时候可能会有一部分的服务端在这里直接写一个星号，这样子会导致所有的不管是哪里都可以向我们的服务器来请求，这样子会不太好，会有一定的安全的隐患。所以我们是需要去设置的，直接设置为这样子的一个就可以了。


既然我们是用到了config，所以我们再额外的去设置一些东西，比方我们在这里面可以设置一个allow，有一个credentials，这个是什么东西？就是凭证，指我是否可以让我们请求去携带一些相应的内容，比方是否允许发送 cookie 信息，我们在设置为true，我们在后面几节，其实我们会涉及到 cookie 和session，所以我们在后面会具体的去叙叙说一下。


设置是否发送 cookie 信息。这个其实在前端也会有相应的一个设计，我们可以看一下前端，在前端源码里面给大家看一下。当我们的一个请求提交的时候，其实他也写了一个。在前端，我们在这里使用的是一个x，这个其实是 feel 框架里面所携带的一个组件，它是专门去用于去做一些异步提交调用我们的后端的。其中它会有一个 VIS credentials，这个也就是它是否要携带相应的凭证信息。在这里一旦设置为出了以后，我们的 cookie 前后端是可以相互可以拿得到的。OK，所以 credentials 注意一下。所以我们在后端也是设置为 true 了。


下一个我们再来看一下 configure 点它有一个add，看一下有一个叫做method。这个是什么意思？这个是指是否要放行哪些请求的方式。比方像get， put post 这些，其实都是 method 了。所以往往我们在这个地方写上一个星号就可以了。写一下设置无需请求的方式。好，所以下一个我们再来设计一个。它还会有一个 at Aloud，有一个header，这个 header 是我们的一个 header 参数。我们其实前端和后端进行交互，有一部分的信息是可以放在 header 里面的，所以我们在这个地方我们跟他 allow 所有，写上一个星号就可以了。加上注释设置允许的，header，OK，这样子。


其实我们当前的 config 设置所需要去配置的一些基本信息，我们都已经是添加好了。随后我们就应该要去做一个路径的映射。路径的映射其实就是请求的URL。这是第二步为 URL 添加映射路径。映射路径我们是针对所有的路径都可以去使用相应的一些基本信息，所以我们只需要斜杠星星就可以了。


URL 叫做URL，有一个叫做 base 的来看一下。在这里有一个 base 的 course configuration source，这个很明显应该是在产品榜，在 web 点， Cos 在下方和下面不要搞混，双击一下。定义为configure，太长了，我们直接使用叫做 Cos sauce，直接把它给 u 出来就可以了，我们只需要针对 sauce 要它。有一个叫做注册的方法，叫做 register cause config region 就是注册。在这个地方你会发现有一个pass，也就是我们在前方所设置的 config 配置，要放到映射里面去，也就是放在。pass。请什么，我们来一个杠星星，这个就是代表请求进来，其实适用于所有的路由。现在其实我们 source 就已经是配置好了。配置好之后，第三步最后一个我们是需要去返回重新定义好的source，在这边我们直接可以 return 你有一个是新的，什么是新的？一个 Cos filter，你是需要去把它给 new 出来的。 new 了以后你会发现在这里面你是需要放入一个 config source，其实这个就是 Cos filter，它自己的一个构造函数，所以你只需要把参数给放进来就可以了。把添加进来。


OK，好，现在我们跨域的一个配置就已经是设置好了，我们重新去运行一下咱们的项目。好，现在是启动成功了。启动成功之后，我们打开页面，我们刷新一下，刷新一下以后在用户名我们加上一个m，这个时候当我们在填入相应的文字的时候，我们的控制台没有报任何的错。


OK，其实现在已经是正确的。我们再来一个c，这个时候你会发现用户名已经存在，OK，用户名已经存在，也就是我们的前端和后端现在已经是通了，因为我们配置了跨域的这一个配置，所以数据交互是没有问题的。当然我们的设置完毕密码以及是确认密码，我们是可以去实现注册的。我们把用户名改掉，我们使用 test 密码，我们可以来一个123123123123，好，点击注册。这个时候你会发现OK，没有问题。现在我们页面已经发生了跳转了，只不过发生跳转后的首页，首页肯定是有问题的，因为首页上的一些接口其实我们都还没有去做，所以肯定是会有问题的。但是我们当前的用户已经是真正的注册了。我们可以打开咱们的数据库，打开数据库以后可以去看一下我们的数据有没有进来。OK，可以看到有一条最新的数据test，这就是我们刚刚所注册的OK，现在我们第一个接口就已经是实现了前后端的一个联调，并且其实我们现在所涉及的一个开发模式就是前后端分离的一种模式。OK。


