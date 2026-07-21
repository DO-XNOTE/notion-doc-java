---
title: 2-1 配置FastDFS环境准备工作
---

# 2-1 配置FastDFS环境准备工作

[image](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/f84b9705-87b4-4569-bef7-ea16ed5894f1/SCR-20240806-iikc.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YFJ5PZSU%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T225220Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIHI9cDatTaxs6nGc6vyfVVSXfsJoe0ZxGMYol5AT3cPHAiBUA4jlUlQc7i81OsiYiw7XuJwdrb%2B6EnXa89T3JGfvNyqIBAjG%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMZp%2FIX7%2Fl5nSSWwR3KtwDxpM80hZiQR8WP06A5tJGS%2BxiPA1v90Hz43pxSRCh4jJc1qcXC5qmS86jNuQcNaaCqEb8s1Z%2FZjhfumIvMhdajUUxSXt%2BwM29P5tRDu0msqO04vVk8ZZZ0UhU%2FdPIKxjo2WLuEmIMJTgoEI4NYhYhCdwgLaAzfVj84a7Wn7rjsCxjzC4Eiteazcac5xvY50%2BWH41IWLXeg84gZa%2FBgDSg%2FqeSNlcRXomB517lcPkoWHfqym6dfneov8xihP1TUMUPScToYqrehSvoye28GUVWarRChcvotA5X4yNWEkClUYMxvERxVPBM6EJy6Y2MPWwHpeig5ApSOZmfREOrbMfCV%2B2xNgImKtFugTEBKPatDBGEsjUVtOlqC3ur3R334cn64jMAEYTd%2BZ7ExPnAIgg%2FD1BTjK1yJf9X1vXla7S1J8v3wjzS7GdO4OHseGJFKbQFwGewt7vjEkrBs31v8Qj6Iaa1wGBjrRsL3ANI%2FiwoQ7dZ7Wo0s2htXrl%2B4v9KmC2k2kmkThOKlIVwYu4avu7ZGFe%2FoMEVLjcpozU5tRYmBl5wPlzaIN%2F%2Bc6EvhKC73ZsY%2FMTP%2BIDeUj6%2BzWdcvPdALa3M%2BRI5JmkVDEJ6RHy%2FreEzbHm8YLHnJF8uGPkwoLj%2F0gY6pgEE5R%2FyLSu7CXyFMr0shanaHZ2p9a0vAaupmttKBtYmNS0UDJVz2LPBayhI8xUM5ojEoi0Qj8LL8sIeKV3cJggs21ZvgZuzubfI3nGPcNk4e3kk%2FvOH6ca4lZ4nGzqb6YE7ZV%2FVJGWmBpN8UyM5tbncIy0g2uI521%2F90XofOlcUexvkyqJ4H3xNdv%2BrSiWhgH%2Fc88KRZtC6zkgd2vyCMIL7E0Bla0im&X-Amz-Signature=ac3fc571b8ca5b9a07f9042c84c1123b50facf0fdb773a3de57cb5051b62f190&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

那么前面几节课我们是针对 fast z f s 做了一个概念部分的一个讲解，那么接下来的话我们要去实操，去进行一个安装，那么安装是需要去有一些相应的环境的准备的。那么先来看一下这个是作者的一个官网，那么是在 Git Hub 上，那么大家也可以去进行相应的一个下载，那么来看一下必备的一些软件，

[https://github.com/happyfish100/fastdfs/wiki](https://github.com/happyfish100/fastdfs/wiki)

那么首先 Santa OS 七点叉你是必须要去准备的，如果说你用的是 Santo S6 点差，那么也是可以的。随后是一个common，那么这个是由 fast z f s 所分离出的一些公用的函数包，那么这个东西你也可以去下载。那么我在这里支持相应的一些下载的安装包，我都已经是准备好了，在这个位置，那么我都会提供给大家。那么如果说你想要自己去下载，可以我在这里下载的话，目前是最新的一个版本。那么如果说你要自己去下载的话，在这里你可以打开它的相应的一个源码，比方说这个是 Lib fast common，点进去以后在这里会有一个 release 找到，在这里面可以去下载，也可以看一下这里面会包含压缩过的一些压缩包，可以自行去下载。


那么在这里的话，他这里应该是拼错了，可以看一下 Lib fast，这个是拼错了，他写的是 Lib fast，这一点注意一下，然后下一个是 fast g f s 的一个本体，那么这个也是需要去下载。那么下载的话这里在它的一个源码的网站也可以去看一下。

[https://github.com/happyfish100](https://github.com/happyfish100)

那么这个是 git Hub 的一个源码，包含了很多的内容， release 点进去，然后的话在这边有很多发布的内容，目前最新是6.04，可以去下载。那么最后下一个是 fast GFS nginx module，那么这个是一个结合，就是说 fast GFS 如果说你想要去把它的一些文件以一个服务的形式发布到网站，在网站浏览器里面通过一个 URL 去访问的话，那么我们就可以使用 engines 做一个关联，那么所以这个就是由他所提供的一个第三方的模块。


那么在它的源码里面，大家也可以去下，给大家看一下，在这边有一个这个点进去，然后 release 有一些相应的版本可以去下载的。OK，好，最后一个是endings，那么是这个版本号无所谓，那么我目前的话也是使用的是一个最新版本，那么配合这些就可以去搭建这个 fast GFS 了，那么然后是下方，下方是官方所提供的一些安装的步骤，那么你可以去参考，那么在这里的话我会按照我自己的一个方式来讲解给大家，跟着我的步骤去做，那么也是可以的。


好，然后来看一下我们的一个虚拟机，那么虚拟机的话目前我是准备了两台，一台是155，一台是156，那么一台是tracker，另外一台是storage，这两台我是分开进行一个部署。那么如果说你想为了方便或者说你的一个内存偏低的话，你把这两个放在同一台节点上去安装也是可以的。

[image](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/ea28ab61-3f20-43fa-a2f8-4157a66c47d8/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YFJ5PZSU%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T225220Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIHI9cDatTaxs6nGc6vyfVVSXfsJoe0ZxGMYol5AT3cPHAiBUA4jlUlQc7i81OsiYiw7XuJwdrb%2B6EnXa89T3JGfvNyqIBAjG%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMZp%2FIX7%2Fl5nSSWwR3KtwDxpM80hZiQR8WP06A5tJGS%2BxiPA1v90Hz43pxSRCh4jJc1qcXC5qmS86jNuQcNaaCqEb8s1Z%2FZjhfumIvMhdajUUxSXt%2BwM29P5tRDu0msqO04vVk8ZZZ0UhU%2FdPIKxjo2WLuEmIMJTgoEI4NYhYhCdwgLaAzfVj84a7Wn7rjsCxjzC4Eiteazcac5xvY50%2BWH41IWLXeg84gZa%2FBgDSg%2FqeSNlcRXomB517lcPkoWHfqym6dfneov8xihP1TUMUPScToYqrehSvoye28GUVWarRChcvotA5X4yNWEkClUYMxvERxVPBM6EJy6Y2MPWwHpeig5ApSOZmfREOrbMfCV%2B2xNgImKtFugTEBKPatDBGEsjUVtOlqC3ur3R334cn64jMAEYTd%2BZ7ExPnAIgg%2FD1BTjK1yJf9X1vXla7S1J8v3wjzS7GdO4OHseGJFKbQFwGewt7vjEkrBs31v8Qj6Iaa1wGBjrRsL3ANI%2FiwoQ7dZ7Wo0s2htXrl%2B4v9KmC2k2kmkThOKlIVwYu4avu7ZGFe%2FoMEVLjcpozU5tRYmBl5wPlzaIN%2F%2Bc6EvhKC73ZsY%2FMTP%2BIDeUj6%2BzWdcvPdALa3M%2BRI5JmkVDEJ6RHy%2FreEzbHm8YLHnJF8uGPkwoLj%2F0gY6pgEE5R%2FyLSu7CXyFMr0shanaHZ2p9a0vAaupmttKBtYmNS0UDJVz2LPBayhI8xUM5ojEoi0Qj8LL8sIeKV3cJggs21ZvgZuzubfI3nGPcNk4e3kk%2FvOH6ca4lZ4nGzqb6YE7ZV%2FVJGWmBpN8UyM5tbncIy0g2uI521%2F90XofOlcUexvkyqJ4H3xNdv%2BrSiWhgH%2Fc88KRZtC6zkgd2vyCMIL7E0Bla0im&X-Amz-Signature=03f0661c98561d32f6ad9d8ebf45d8446305eabac52c1c1f6294a7e1dd1d202e&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

随后我们来看一下，那么打开咱们的一个命令，行，目前的话我一个是Tracker，一个是storage，在这里设置了它的一个 host name。那么进入到 home software 来看一下这个 fast DFS，我目前是事先已经上传好了，那么包含了这些内容。那么首先我们要去做一个操作，第一步的话我们要去安装一些相应的环境，那么 fast GFS 它的源码是 c 语言，所以这个 GCC C + + 的一个环境你是需要去安装一下的，那么视线我已经是安装好了，那么如果说你没有安装的话去安装一下，那么随后下一个，下一个是需要去安装一下这个 lip event，把这个环境包去安装一下。那么安装好以后把这个包去做一个解压，我先把事先解压后的先删掉，然后我们来解压一下。使用差命令杠 set x u f，然后在一个 lib fast 后门先把这个包先来释放一下，解压好，OK，随后我们进入到这个 lip fast common。进入到这个包，那么其中包含了一个 make 点sh，那么这个是它的一个安装编译的一个命令，点斜杠 make 点sh，回车一下。那么这样子的话等待它的一个编译完成以后，那么我们再去做一个install。


随后我们再来一个 install 回车，那么在这里的话来看一下这边它会有一个 make Z I r 杠p，这边有三行，那么这个其实就是它安装以后释放出来的一些相应的文件内容，都是在这相应的一个目录里面。那么这个是我们第一个所安装的，那么随后我们就要去安装一下咱们的 fast g f s 它的一个本体，那么还是一样，我们回到上一个目录，那么把这个 fast DFS，这个是它的一个本体的一个压缩包，把它做一个相应的解压，还是一样 tar 杠 seed XF 回车。
好，OK，目前已经是释放了，随后进入到这个目录里面来看一下，那么这里面是包含了它里面的一个相应的一些内容和文件，那么随后的话我们就可以去做一个安装，这个安装和我们之前安装 live fast common 其实是一样的，它也有一个 make 点SH，就这个东西。然后你也可以去打开，使用 v 命令去看一下。


在这里面的话它其实包含了这个三个路径，这个也就是它所安装的一个安装之后的一些相应的内容所释放的一个路径。那么这个 user 放以及是这个 etc 下的 fast DFS，这个我们后面会用到的。好，然后退出一下我们的点斜杠， make 点SH，直接来做一个编译。


好，然后我们再来 install 一下回车，那么在这里能够看到这边是它所释放出来的一些文件所存在的一个目录都是在这个里面，一个是 user bin，另外是一个 etc 下的 fast ZFS。那么其实我们也是可以进去看一下，我们进入到 user bin 的里面，然后 l s， f d， f s 来一个星号。因为这里面包含的内容会很多，然后我们通过这个命令去看的话，那么这些都是和我们 fast DFS 相关的一些命令。那么像这个来看一下，有一个storage，这个是和我们的存储节点相关的。另外还会有一个track，这个是和我们的跟踪节点相关的，OK，那么此外的话它还会有这个 test 等等，这里面包含了很多的一些相应的命令，都是可以去执行的。


然后我们再进入到斜杠 etc 下有一个 f d f s 进去一下，那么在这里面都是和我们相关的一些 config 配折键，都是点config，后面是它的一个点sample，那么我们要去修改的话，我们可以拷贝一份新的，那么当然我们也可以从它的一个解压缩之后的包里面把那里面的一些相关的内容拷贝进来，那么其实也是可以的。


那么我们可以进去看一下，我们进入到 home software faster d f s，然后我们进入到这个主体的文件包里面，然后它会有一个找一下，有一个config， config 配置文件进入一下，然后可以看到这里面包含了相应的一个内容，那么这些内容的话，像这个 storage tracker，还有是 client 这些我们后面都要用到，都要修改，那么在这边我们直接拷贝所有的内容。


copy 新阳，把当前文件夹里面这些配置文件，我们全部都统一的拷贝一下，拷贝到我们刚刚的 etc 下的FDFS，直接全部都拷贝进去。随后我们再进入到 f d、 f s 之下来看一下相应的一些文件内容，我们都已经是拷贝进来了，好， OK 啊，那么这些内容都是我们在安装之前所需要去做的一些准备工作。
那么这些我们在当前这一节课我们所讲的这些内容的话，你不仅要在 check 上去进行安装，那么你也要在这个 storage 上也要去安装，所以给大家布置一个小任务，把我们当前这节课所做的这些内容在你的 storage 上也去做一遍。这个步骤我就不再去做了，省略了这个，那么我在后面我会花一些时间，我主动的去会做一下，那么大家跟着前面的步骤也去做一下，OK，两台节点上都要。

[image](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/dab65396-4ad3-447a-9a50-ab45f292d355/2020-09-17_174053.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YFJ5PZSU%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T225220Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIHI9cDatTaxs6nGc6vyfVVSXfsJoe0ZxGMYol5AT3cPHAiBUA4jlUlQc7i81OsiYiw7XuJwdrb%2B6EnXa89T3JGfvNyqIBAjG%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMZp%2FIX7%2Fl5nSSWwR3KtwDxpM80hZiQR8WP06A5tJGS%2BxiPA1v90Hz43pxSRCh4jJc1qcXC5qmS86jNuQcNaaCqEb8s1Z%2FZjhfumIvMhdajUUxSXt%2BwM29P5tRDu0msqO04vVk8ZZZ0UhU%2FdPIKxjo2WLuEmIMJTgoEI4NYhYhCdwgLaAzfVj84a7Wn7rjsCxjzC4Eiteazcac5xvY50%2BWH41IWLXeg84gZa%2FBgDSg%2FqeSNlcRXomB517lcPkoWHfqym6dfneov8xihP1TUMUPScToYqrehSvoye28GUVWarRChcvotA5X4yNWEkClUYMxvERxVPBM6EJy6Y2MPWwHpeig5ApSOZmfREOrbMfCV%2B2xNgImKtFugTEBKPatDBGEsjUVtOlqC3ur3R334cn64jMAEYTd%2BZ7ExPnAIgg%2FD1BTjK1yJf9X1vXla7S1J8v3wjzS7GdO4OHseGJFKbQFwGewt7vjEkrBs31v8Qj6Iaa1wGBjrRsL3ANI%2FiwoQ7dZ7Wo0s2htXrl%2B4v9KmC2k2kmkThOKlIVwYu4avu7ZGFe%2FoMEVLjcpozU5tRYmBl5wPlzaIN%2F%2Bc6EvhKC73ZsY%2FMTP%2BIDeUj6%2BzWdcvPdALa3M%2BRI5JmkVDEJ6RHy%2FreEzbHm8YLHnJF8uGPkwoLj%2F0gY6pgEE5R%2FyLSu7CXyFMr0shanaHZ2p9a0vAaupmttKBtYmNS0UDJVz2LPBayhI8xUM5ojEoi0Qj8LL8sIeKV3cJggs21ZvgZuzubfI3nGPcNk4e3kk%2FvOH6ca4lZ4nGzqb6YE7ZV%2FVJGWmBpN8UyM5tbncIy0g2uI521%2F90XofOlcUexvkyqJ4H3xNdv%2BrSiWhgH%2Fc88KRZtC6zkgd2vyCMIL7E0Bla0im&X-Amz-Signature=36ff4cd2066c9f3d75e532e450d2c3f1b5360173b767afd144e129193e1f2e23&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)


