---
title: 3-9 使用tomcat运行前端源码
---

# 3-9 使用tomcat运行前端源码

[image](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/5a5ec4db-3c97-494b-9fb3-668540da7653/SCR-20240816-tnsh.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46624MPDPMZ%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T224628Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIANzk3ZGZvGJHmUn%2BZL5IPruWFNcdoCOkhG%2BsSKDQVEkAiEA12Vd7W3wM9Tnx%2BU8nawdVClupNJ7ILQBFLVbP1Rxw1kqiAQIxv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDOrmtRyccDbVcR2ndSrcA8hwlC%2F9MRLJD4VGeNkGrAhMODADyJ5x33ac%2FoDPrXWzKUHnWy3Sak3jtjcUol07qYtbkVhgQeL%2FH3brKHNnjRonGI1iUm0ah7P%2FoLRllql%2BEhtqGDH%2FceLCjqxMCTSh%2FAMT0lcUXrvSKiV3BEboWg5a6cKjC%2BDqbG0dCTvQRasm7zK%2BUQ0hm8MEprYDfQZdntzmn1mcys1moDrCDVjR8xwnSzm2JnPYiMCjk%2FGslWOvGguKwAH0bxHXmx8YDSL%2Bi3pxjcVlpcyUgxhy6DZVmA6pJa5X77OtONs3rTp6w8lxvtLK%2BM3ymUTyMz6elAt8lQlQ7GM5jWuf2%2FEXh%2F1%2BDw1eKvYv11d9g%2BGR6Z570cZJdCFB5XKT8bnEwgQfU8LQh59Fw3c2ayHHlT5yFovaVM3y2fZE92d9biVgym3B6vWjnYoA2p8Gy0LCTOGd%2FvgA9MGHv%2Bi3bEDRbKn2OA9JTyniDyv%2FvLsEJhSWJ%2FRsHuhXcmIbvKPnIHgb2SNviDyqQYeipSZxQU0vW%2BnSp0jTWaAYFPHc715ZXGMq48H%2B9%2FWqsbbquft2pXxXj614ljEU3WeaSkNvtcRDeptSnCLJH2KyGl2dSYYKw6lNDCdeV3R086WaEcc6iUmdm0JGMJO4%2F9IGOqUBbSbcyWiZ69YUXKyCTWrNM3aQLbu3fq4KbOxD4NzcmkdMs0LXy5ThWa1HuqbPDigQKS26bs231PnspOAVMut%2FbRyhQ1JE6zv07aG68weYaOyEk69vMU3%2BPXYknnWpUwrOH%2FQ0vGRRlpiLHfF5Fjmm4U1ldugqAdLin%2BSEWkx26xtZ%2B%2BEoVYSZyc%2Bq2tsusADdC7%2BWJAJzeZAGEdiDoVX%2BICNFyYKs&X-Amz-Signature=080de337e7f25433cafbb07fe525faefb9232eb10df3d58eb189533a123c2198&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

现在我们的两个接口已经是开发完毕，并且也有了一份对接的文档，也就是 Swagger2。现在我们要去对接前端的源码，我们假设现在在一个企业的团队里面，你是需要把一份文档提供给前端开发人员的，他们会根据你的文档去进行一些对接。现在对接工作其实就是我们自己来做，我们所有的一些前端源码我们全部都是有的，我们可以来看一下，在里面有一个福迪shop，这就是前端的野马。展开看一下，里面包含了很多的一些内容，比方有 HTML 页面，另外还有是 JS 也有就是JS，还有些静态资源，就是图片，另外还有是一些CSS，其实全部都是有的。好，我们就可以需要把前端源码运行起来，去跑起来，跑起来。我们会依托一个静态资源。服饰静态服务区其实会有恩迪克斯或者阿帕奇，我们肯定是使用恩迪克斯了，但是恩尼克斯其实我们还没有讲到，所以在这里我们会使用talk。我们在后续讲到发布上线的时候，我们会使用尼斯来发布咱们的前端源码的。在我们本地使用 top hit 其实也是一样的。


Tomcat，它不仅可以去运行 z two e 项目，静态资源也是没有问题的。这是 Tomcat 它的官网，大家可以百度一下，或者直接可以敲一下这个网址也是可以的。在它的首页。其实目前的主流版本还是三档 7. 09. 0 和 8. 58. 5，其实就是 8. X，我们主要是使用 9. 0 这个版本，这是最新的，而且在我们的项目里面，其实可以来看一下。


展开我们的library，往上面找它，其实会有一个 template 的，搜一下。就这个我们内置的 Tomcat，它的版本号也是 9. 0，它的小尾巴是 19 小版本号其实无所谓的，最新的是 0. 22。在我们直接去点 download 去下载。


在里边来看一下，会有一个call，其实主要也是根据我们不同的一个系统，比方你现在是一个 windows 系统，你去下载 32 位或者 64 位就可以了。下面还有一个 windows service installer，这是一个安装器，在有一些甲方或者客户，他可能会直接使用这种安装器去运行，因为它可以去设置系统的自启动，把你的一些项目部署进去就可以了。这个汤姆克塔其实就相当于是一个软件，运行在你的 windows 上，大家有兴趣可以自己尝试着去下载了。去看一下也是可以用的。叫他其实是在 Linux 上。我是 Michael s，所以使用 SIP 就可以了。关于 tank 的，其实我本地已经是下载好了，可以来看一下。下载的目录。在这里双击进行一个解压。解压完以后我们可以再进入到它的一个目录。其实我相信大家只要是使用过 Tom get，你就应该要了解每一个目录是什么，它代表是什么意义，用来干嘛的。在这里我们就不去细说了。


进入到 web apps，这个是用于去放一些我们的项目，它所在的一个目录的，我们本地的源码直接可以拷贝进去，贴到这个位置，贴过来以后，其实文件夹的名称就是我们的项目的名称。现在我们就可以去尝试着先去运行一下我们的项目。应该说是把汤姆特先启动起来，因为这个项目现在你要去运行肯定是会有一定的错误的。好，我们可以找到上一个目录，进入到bin。由于我是 Michael s，使用方式和 windows 可能会有一些不同，我们来看一下我是怎么去运行的。其实也是通过命令行脚本去运行的。


点斜杠 start 点 SH 直接回车。由于系统的权限比较高，所以我还是需要去为它增加一个权限。进入到上一个目录。 c h mode 杠 2 来一个三个区，针对所有的屏，我们都给它加上一个权限，再进入到屏幕录启动。好，现在OK，启动成功了，超 k 的 started 系统成功。随后我们就可以去运行一下。


运行我们可以把咱们的一个项目的名称先拷贝一下。项目名称，在这里把直接拷贝，拷贝以后直接访问咱们的一个浏览器就可以了。浏览器我们把，拼装一下，也就是 Tomcat，它是默认的是 8080 对吧。直接杠这个项目的名称就可以去运行了。运行以后，很显然现在在这个页面里面其实没有任何的东西，这只不过是一些静态的样式，它是会展示的。我们按一下 F12 可以看得出来，当前其实在浏览器的控制台会有一堆的错误的，但是没有关系，现在其实我们已经是运行了咱们的项目了。

