---
title: 1-4 Nginx安装与运行
---

# 1-4 Nginx安装与运行

[image](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/e8a63748-42cd-4336-b6e5-f9ca3a0d1ecf/SCR-20240804-dfcb.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466S67RZ3WS%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T224839Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQD8%2BRqZ0cwI4I%2Fw0qbpk01NzXd%2F6LoOh%2FEcXZlV6HBV5AIhAOvGMp0OrQpDbUQ%2BYB%2BLQwUe2k6vbdKHda%2B6nbdFSyw3KogECMb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgyVZI8cg1q89XDaoMMq3AOlBZQjNUWtv06bM2VvqFiQWbNUbIu3Tr899AaCSQbPI05To2sStM6%2FFtvW2eox5Kg9XzLHj4WJro7dvqbEgNxYJxs3dmj1PjR9iN8DctajGcKf0q3RGWTnTTUf3LKxlTw387iCHKKBsdr5ELE5%2BlzkHxId76z%2FCg9cafcKMPwVs8HNqYjxxnhZO393DMxr7Hcdo176cXollsi%2Bya38WD44%2F3GpINbni4ebAPjIv6t04TvfSQfH9GMxx%2BMIlVmKLcVK0xmasARdWhKdEXNhUwHkk%2BI9PMnazAOwKVq8WTP%2BIcouAQQYfRl2OAJZPLxvkezIZmxhtaOPUXcItwnGhV08ab1Kuxf9KbdN%2Foz2fT5Zp33X06129yCGQrAThR%2BMz2bTzbjxLNjHthIeApipgiONDF4ezuuiFXjjPKqKU8N1ajQf5zgtV5NSsp1Yrt5CCmjFvj%2FsYyUVrl%2B8xuqs5yG6z%2BQLASJ%2BC6QblUNV9Fr7GjC6kH8ksFoYyopKRoST91MYDZZ627ywdc0jqw12jsm9ZsaC8f0cQ6%2FwZ8SCVBjo4PeaSA7P4pPGi4Nexc1ep1KhZOuKPyCrO2YtRn0T3ssOkClGskJ69vt8ip0U7VE5Y1PaWhEwhf4ZBUf%2FmDCvuv%2FSBjqkAXiFIp%2Bk1dqS%2BkQNR7jfBDI5zuhjmfbTcsxf8zewlojD4sSsJFMRpxDVPlx1b0lWgXqDijm6rMWG42iXAcnUTjZHYxI28Tnqzb7DYLnmLm947bdBuLfEvs7jhFPtzMeUWnzaSaxXqNdZfbuCABplXgnaCN5tkL9xD8xoqqVDs2JSjTWNw8R%2Bz9wbwIc1qS%2BSceYhF7qNJTJm7MMg5BTQ8euP3nIU&X-Amz-Signature=b75aafb59216d3c9ccd726c81f1f84468f25c16c0d77fe7a011534e30def1362&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

[file](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/d44e5301-3711-478d-9e85-bfb2dedc5fce/1-5_%E5%9B%BE%E6%96%87%E8%8A%82.pdf?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466S67RZ3WS%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T224839Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQD8%2BRqZ0cwI4I%2Fw0qbpk01NzXd%2F6LoOh%2FEcXZlV6HBV5AIhAOvGMp0OrQpDbUQ%2BYB%2BLQwUe2k6vbdKHda%2B6nbdFSyw3KogECMb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgyVZI8cg1q89XDaoMMq3AOlBZQjNUWtv06bM2VvqFiQWbNUbIu3Tr899AaCSQbPI05To2sStM6%2FFtvW2eox5Kg9XzLHj4WJro7dvqbEgNxYJxs3dmj1PjR9iN8DctajGcKf0q3RGWTnTTUf3LKxlTw387iCHKKBsdr5ELE5%2BlzkHxId76z%2FCg9cafcKMPwVs8HNqYjxxnhZO393DMxr7Hcdo176cXollsi%2Bya38WD44%2F3GpINbni4ebAPjIv6t04TvfSQfH9GMxx%2BMIlVmKLcVK0xmasARdWhKdEXNhUwHkk%2BI9PMnazAOwKVq8WTP%2BIcouAQQYfRl2OAJZPLxvkezIZmxhtaOPUXcItwnGhV08ab1Kuxf9KbdN%2Foz2fT5Zp33X06129yCGQrAThR%2BMz2bTzbjxLNjHthIeApipgiONDF4ezuuiFXjjPKqKU8N1ajQf5zgtV5NSsp1Yrt5CCmjFvj%2FsYyUVrl%2B8xuqs5yG6z%2BQLASJ%2BC6QblUNV9Fr7GjC6kH8ksFoYyopKRoST91MYDZZ627ywdc0jqw12jsm9ZsaC8f0cQ6%2FwZ8SCVBjo4PeaSA7P4pPGi4Nexc1ep1KhZOuKPyCrO2YtRn0T3ssOkClGskJ69vt8ip0U7VE5Y1PaWhEwhf4ZBUf%2FmDCvuv%2FSBjqkAXiFIp%2Bk1dqS%2BkQNR7jfBDI5zuhjmfbTcsxf8zewlojD4sSsJFMRpxDVPlx1b0lWgXqDijm6rMWG42iXAcnUTjZHYxI28Tnqzb7DYLnmLm947bdBuLfEvs7jhFPtzMeUWnzaSaxXqNdZfbuCABplXgnaCN5tkL9xD8xoqqVDs2JSjTWNw8R%2Bz9wbwIc1qS%2BSceYhF7qNJTJm7MMg5BTQ8euP3nIU&X-Amz-Signature=455e0d0bd3f7cb4ce530560ada61bbe6d76eca0e81b00dd59611e8987c220d90&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

[image](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/3975c98c-c83f-496f-9087-2e9f88d7b224/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466S67RZ3WS%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T224839Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQD8%2BRqZ0cwI4I%2Fw0qbpk01NzXd%2F6LoOh%2FEcXZlV6HBV5AIhAOvGMp0OrQpDbUQ%2BYB%2BLQwUe2k6vbdKHda%2B6nbdFSyw3KogECMb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgyVZI8cg1q89XDaoMMq3AOlBZQjNUWtv06bM2VvqFiQWbNUbIu3Tr899AaCSQbPI05To2sStM6%2FFtvW2eox5Kg9XzLHj4WJro7dvqbEgNxYJxs3dmj1PjR9iN8DctajGcKf0q3RGWTnTTUf3LKxlTw387iCHKKBsdr5ELE5%2BlzkHxId76z%2FCg9cafcKMPwVs8HNqYjxxnhZO393DMxr7Hcdo176cXollsi%2Bya38WD44%2F3GpINbni4ebAPjIv6t04TvfSQfH9GMxx%2BMIlVmKLcVK0xmasARdWhKdEXNhUwHkk%2BI9PMnazAOwKVq8WTP%2BIcouAQQYfRl2OAJZPLxvkezIZmxhtaOPUXcItwnGhV08ab1Kuxf9KbdN%2Foz2fT5Zp33X06129yCGQrAThR%2BMz2bTzbjxLNjHthIeApipgiONDF4ezuuiFXjjPKqKU8N1ajQf5zgtV5NSsp1Yrt5CCmjFvj%2FsYyUVrl%2B8xuqs5yG6z%2BQLASJ%2BC6QblUNV9Fr7GjC6kH8ksFoYyopKRoST91MYDZZ627ywdc0jqw12jsm9ZsaC8f0cQ6%2FwZ8SCVBjo4PeaSA7P4pPGi4Nexc1ep1KhZOuKPyCrO2YtRn0T3ssOkClGskJ69vt8ip0U7VE5Y1PaWhEwhf4ZBUf%2FmDCvuv%2FSBjqkAXiFIp%2Bk1dqS%2BkQNR7jfBDI5zuhjmfbTcsxf8zewlojD4sSsJFMRpxDVPlx1b0lWgXqDijm6rMWG42iXAcnUTjZHYxI28Tnqzb7DYLnmLm947bdBuLfEvs7jhFPtzMeUWnzaSaxXqNdZfbuCABplXgnaCN5tkL9xD8xoqqVDs2JSjTWNw8R%2Bz9wbwIc1qS%2BSceYhF7qNJTJm7MMg5BTQ8euP3nIU&X-Amz-Signature=e56514ef344db02fe2b22a9b649231ed4d33d7e32eda4a6f354ee59ffc9991ca&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

那么前面我们讲了安吉姆斯这些基本概念了以后，那么接下来这一节我们就一起来安装一下安吉克斯。那么首先的话我们是需要去打开一下它的一个官方的网站，大家可以去百度一下，或者直接手敲一下 n x 点 o r d。

[https://nginx.org/en/download.html](https://nginx.org/en/download.html)

[https://nginx.org/](https://nginx.org/)

那么在这个首页的里面，它的一个大部分的一个占比都是它一些历史版本的发布，相关的信息都会在这里列出。然后在右侧导航，在这个地方会有一个download，那么这个就是去用于下载 engines 的软件包的，点击一下在这里面，那么我们就可以看到在这边会有一个mainline，version， stable 以及是legacy，那么这些都是对应到一些相应的版本。


mainland 的话，它其实相当于是一个正在开发的一个开发版，或者说是一个预览版，那么它有可能是不太稳定的，所以我也不推荐大家去下载。那么往往我们会使用一个最新的稳定版本，也就是 stable version。那么在这边会有一个幺点幺，六点幺这个版本，

[image](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/5bf220e3-7a8c-4698-a7a8-673234829c70/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466S67RZ3WS%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T224839Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQD8%2BRqZ0cwI4I%2Fw0qbpk01NzXd%2F6LoOh%2FEcXZlV6HBV5AIhAOvGMp0OrQpDbUQ%2BYB%2BLQwUe2k6vbdKHda%2B6nbdFSyw3KogECMb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgyVZI8cg1q89XDaoMMq3AOlBZQjNUWtv06bM2VvqFiQWbNUbIu3Tr899AaCSQbPI05To2sStM6%2FFtvW2eox5Kg9XzLHj4WJro7dvqbEgNxYJxs3dmj1PjR9iN8DctajGcKf0q3RGWTnTTUf3LKxlTw387iCHKKBsdr5ELE5%2BlzkHxId76z%2FCg9cafcKMPwVs8HNqYjxxnhZO393DMxr7Hcdo176cXollsi%2Bya38WD44%2F3GpINbni4ebAPjIv6t04TvfSQfH9GMxx%2BMIlVmKLcVK0xmasARdWhKdEXNhUwHkk%2BI9PMnazAOwKVq8WTP%2BIcouAQQYfRl2OAJZPLxvkezIZmxhtaOPUXcItwnGhV08ab1Kuxf9KbdN%2Foz2fT5Zp33X06129yCGQrAThR%2BMz2bTzbjxLNjHthIeApipgiONDF4ezuuiFXjjPKqKU8N1ajQf5zgtV5NSsp1Yrt5CCmjFvj%2FsYyUVrl%2B8xuqs5yG6z%2BQLASJ%2BC6QblUNV9Fr7GjC6kH8ksFoYyopKRoST91MYDZZ627ywdc0jqw12jsm9ZsaC8f0cQ6%2FwZ8SCVBjo4PeaSA7P4pPGi4Nexc1ep1KhZOuKPyCrO2YtRn0T3ssOkClGskJ69vt8ip0U7VE5Y1PaWhEwhf4ZBUf%2FmDCvuv%2FSBjqkAXiFIp%2Bk1dqS%2BkQNR7jfBDI5zuhjmfbTcsxf8zewlojD4sSsJFMRpxDVPlx1b0lWgXqDijm6rMWG42iXAcnUTjZHYxI28Tnqzb7DYLnmLm947bdBuLfEvs7jhFPtzMeUWnzaSaxXqNdZfbuCABplXgnaCN5tkL9xD8xoqqVDs2JSjTWNw8R%2Bz9wbwIc1qS%2BSceYhF7qNJTJm7MMg5BTQ8euP3nIU&X-Amz-Signature=39679ead6c9bcf6f773dffc5725c960abaf332e67b8051e0ff88a090f4e9086a&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

那么目前我已经是预先的进行了一个下载。那么 endings 的安装，它其实可以分为在 windows 以及是Linux，那么我们的课程是以 Linux 为主的，所以下载这个就可以了。旁边的这个是一个 windows 版本，那么当然如果说是在 windows 上去运行也是可以的。


OK，那么下方这些都是一个 like c 歌曲，那么这些都是曾经的发布过的一些历史版本，那么在这边我已经是预先下载好了，下载好了以后，那么大家需要把这个相应的软件包上传到你的一个Linux，那么我在本地的话预先已经是搭建好了一个虚拟机，那么虚拟机里面是安装了一个三头s，这个是用于去学习的。


那么一般来说我们在学习的时候，我们使用虚拟机里的雷姆斯就可以了，等到学习好以后，你熟悉的运用了，那么我们可以再到云服务之上去使用 n x，那么现在这一台我们就已经是启动了，启动以后那么我们可以先来拧一下来看一下，这是一台 172 双击。那么先进入到我们的一个软件的目录，我是上传到了 software 看一下，这里会有一个 Nginx 这个包下载的直接上传，然后上传好了之后，那么我们就要去做一个相应的安装了，那么关于 engines 的一个安装步骤等等的一些内容，那么我也是事先写了一份文档，

[https://nginx.org/en/docs/](https://nginx.org/en/docs/)

[https://nginx.org/en/linux_packages.html#RHEL](https://nginx.org/en/linux_packages.html#RHEL)

这份文档的话也会给到大家的。那么我们可以一起来看一下。


那么首先在这一块是去官网去下载一下 Linux 的一个包，下载好了以后，那么我们要上传到 Linux 的系统。上传好了以后，我们在安装之前必须要去安装一些相应的依赖环境，比方说我们要去安装一下g，c， c 的环境，随后我们要去安装一个p，c，r， e 的库，那么这个是用于去解析一些正则表达式的。随后第三个是一个 c 列的，这个是用于去做压缩和解压缩的一个依赖。


第四一个依赖是一个s，s，l，那么这是一个安全的加密的套接字写一层，它主要是用于h，t， t p 的安全传输，其实也就是 h t t p，s。所以对于这几个依赖环境的话，我们是需要去进行安装的。好，那么随后我们就把这里面的一个命令一步一步的拷贝过来，去做一个安装。


先安装第一个是g，c，那么其实我们的一个安尼克斯，它底层它的一个源码也是使用的这个 c 语言去开发的，那么在这里 is this OK，直接输入一个 y 进行一个安装就可以了。那么这个包的话，其实它相对来说会有一些大，所以它在一开始安装的时候会稍微的有一些慢，等到它下载完毕以后再去安装了，就会非常的快了。


那么如果说像有一些云服务器或者数据集，它自带的这些环境的话，那么我也是建议大家可以先去检测一下，如果说安装了，那么就使用原来的，没有安装的话，那么它会自动的去安装。那么在这里看到完毕了，就代表我们这个环境就已经是安装好了。最后我们再来安装下一个，那么下一个是一个 PCI 库，直接把这个命令拷贝贴过来。好，OK，那么这个是这个包比较小，所以它安装的也比较快，随后我们再把下面的两个，一个是 c Lib，另外一个我们再来拷贝，最后一个是 open s l 拷贝一下贴过来。


好，OK。那么到这里的话我们就 4 个依赖的包，依赖的环境就已经是安装 OK 了。那么随后下一个的话，我们是要去把这个进行一个解压吧。使用差命令去进行一个解压。好，OK。解压成功以后，那么在这里会有一个恩尼克斯这样的一个目录，这个是就是被我们刚刚所释放出来的，那么随后下一步，那么下一步的话我们要去创建一个目录来看一下，那么这个目录的话是一个tap，是一个临时目录，是为恩尼克斯去创建的。如果说你不去创建的话，那么在我们后续去启动 engines 的时候会报错，所以这个命令我们拷贝一下，做一个创建。好，那么这样子敲完以后就已经是创建好了。


好，随后下一步，那么下一步的话，那么我们可以来看一下。下一步的话，其实我们就可以开始一步一步的去进行安装了，但是在安装之前的话，我们来看一下，我们是需要去进行一个编译的，因为在 Linux 上那么它的一个包其实都是源码，所以我们必须要先去编译，编译好以后再去做一个安装。但是在编译之前的话，我们在这个安尼克斯的目录里面，我们是需要去做一个配置的，来看一下，在这里会有一个 config 这个配置，那么这个配置的目的其实主要是为了去创建一个 make file 的文件，通过 make file 我们才能够去做一个编译以及是安装，那么在这里面这是一大段的命令行，然后的话我们来看一下，那么这里面会有一个斜杠，这个斜杠的话它其实是代表我们的一个命令的换行。那么这个作用其实主要是便于我们的一个可读性可以提高一下，那么随后在这里面每一行它都是代表相应的一个意义的，那么在这个下方那么我也其实已经是贴出来了，那么首先看一下，首先我们是通过点斜杠config，那么这其实是一个命令，在我们的这个文件夹里面是有的，我们是可以来看一下。


我们先进入到安静思这个包，进入了以后我们来看一下，在这个里面我们会包含了一个config，那么这个其实就是用于做配置的，所以就是一个配置命令配置项，随后我们继续。


那么在这里面第一个是一个perfect，那么它是指我们 engines 所安装的一个目录的位置。我们会统一的把所有的一些安装包，我们一般都会放到 user local 之下的，那么随后下一个。下一个是一个指定我们 engines 的一个 p i d，那么其实这也是和进程相关的。那么下一个是一个 look pass，那么这个是我们要去锁定一下我们的一个配置。那么在这个下方也都有是用于去锁定安装文件的，主要是用于防止被恶意的篡改或者说是误操作。那么随后下方还会有一个 error log，于是 HTTP log，那么这两个其实都是和预置相关的，指定一下它的一个位置就可以了，我们一般会指定在 g a， r log 之下，那么随后下方有一个 with h t p， g c 那么它是一个模块。看到它是一个 model 结尾的，那么它的一个目的是启用 g ZIP 这个模块，那么它是主要用于去在线的实时压缩输出的一个数据流。


好，随后继续。那么下方其实这些内容，这些其实全部都是一个 table pass，都是一些临时的目录，临时的文件夹，我们为他们进行一些相应的提供的，那么在这边都有，都是为这些内容 client proxy， fast c， g i 等等去设定一些临时的目录。


OK，当我们这些配置全部配置好了以后，我们直接按一个回车，那么我们就可以去创建一个生成一个 makefile 这个文件了。OK，好，那么在这里我们直接把这一段内容 Ctrl c 全部都拷贝一下，然后直接贴到我们的这个命令行贴过来，那么在这个时候我们直接按一个回车，然后我们来看一下，那么这个过程的话是用于去做一个 check in，然后到最后可以看到他创建了一个 makefile 这个文件。


随后我们来看一下，那么重新的 l l 看一下，在这里面创建了一个 make fell，那么这个就是我们刚刚所创建出来的一个文件，那么当我们的配置全部都 OK 了以后，那么现在我们就可以继续下一步了，那么下一步操作就是通过 make file 去进行一个make，也就是编译来看一下。在这里我们执行 make 这个命令就可以了，随后我们敲一下，直接敲一个 make 来按一个回车，那么编译的文件数量还是比较多的。


到最后一步，那么现在其实我们已经是编译成功了，那么编译成功之后我们再来一个 make in store，那么这个就是代表进行安装了。好，那么速度也非常快，按了以后我们就已经是安装成功。安装成功之后我们可以来找一下安定斯，通过 VIS 安利斯来搜一下，那么这个时候它会指定我们的一个 Nginx 在 user local Nginx 这个目录之下，那么这个其实我就是我们之前在进行安装的时候，在配置项里面所指定的一个 Nginx 的perfect，就是它的一个安装目录，那么到这里的话到这一步那么我们的一个安装就已经是成功了。那么接下来我们其实可以去测试一下我们的安利斯有没有正常的一个安装配置。好我们可以去进行一个测试的。


我们可以进入到我们的一个安装的目录，我们直接c， d 进入到这个 n g x 下直接进去，然后再来看一下，那么在这个 n g x 的目录之下，我们包含了三个文件夹，第一个是config，其实这个就是一个配置项配置文件我们可以进去看一下，在这里面会有一堆的内容，其中有一个非常非常重要的文件就叫做 Nginx 点configure，这个是我们后续一直要用的，这是核心的配置文件。


随后再返回再来看，那么下方还会有一个HTML，那么这是一个静态字节文件夹，就是包含了一些相应的 HTML 的文件，我们也是可以进去看一下的，在这里面包含了一个50X，这个其实代表是一个出错的一个HTML，那么下方就是一个 index 点HTML，那么这是一个默认的首页。


随后我们再返回再进入到SB，那么这是一个比例的话，其实就是二进制文件嘛，我们进入到 SB 目录来看一下，这里面会有一个endings，那么这个其实就是一个可执行的一个文件了，我们是可以直接通过点斜杠 ending 去做一个运行的。回车一下，那么可以看到没有出任何的错，那么现在其实我们的安尼斯就已经是启动了，那么启动了以后我们就应该要去访问一下吧。那么其实恩尼克斯它默认的首页配置是通过它的一个 logo host 去进行一个访问的，那么它的 logo host 我们可以在 Linux 系统里面去进行访问，但是现在我们是在另外一台电脑上，所以我们是要访问它的一个内网的IP，那么它的一个 IP 是幺九二点幺六八点幺七二，我们直接访问这个 IP 就可以了，直接复制一下，那么我们可以贴到我们贴过来，贴到这个浏览器里面来，然后直接按一个回车。那么这个时候你会发现他打印了相应的内容。


welcome to engines，那么这个其实就是它默认为我们展示的一个静态的一个文件，然后我们可以回到上一个目录，那么这个就是一个肯定的，这个是HTML，就是SD，一定要注意。然后我们可以进入到 HTML 这个目录去修改一下index，那么可以看到在这边会有一个 welcome to endings，我们是可以去做一个修改的，比方说我们写一个 hello world， hello 窝子好保存一下，保存一下以后，那么现在我们到页面里面去进行一个刷新，刷新以后你会发现在这里 hello world 就已经是展示了，那么这个就代表我们的一个 annix 现在已经是正常的安装成功，也是正常的启动了。


那么在我们的安装过程中，安装之后其实有两点是需要去注意的，在我们的文档里面其实也是提供了，在这里会有一个注意事项。如果说你是在云服务器里面安装的话，那么是需要去开启一下 Nginx 的默认端口，也就是巴黎，那么开启了以后我们才能够去访问。那么一般来说在云服务器里面的话，这个 80 端口它默认就是打开的。那么如果说是在虚拟机安装的话，那么你的一个防火墙是需要去关闭的，那么这个我已经是关闭了，提前的关闭的。然后那么你本地如果说你要去发起内网互通的这种情况的话，那么其实你本地的 windows 或者说是 Mac 的话，你也需要把自己的一个防火墙去关闭的，那么在我这里的话，其实我的目前的一个状态也已经是关闭了，那么在防火墙关闭的一个情况下，那么内网的话那么就是可以互通了。



那么对于我们 Nginx 的话，其实还有两个，一个命令，那么一个是停止，通过点穴杠 Nginx 杠 s stop 就可以停止我们的index，然后它还会有一个重新加载我们的一个配置文件，通过杠 s reload 那么就可以去生效了。那么这个的话这两个命令在我们后续的课时里面我们还是会使用到的。

```java
1-5 附：安装Nginx与运行
安装Nginx
1. 去官网http://nginx.org/下载对应的nginx包，推荐使用稳定版本
2. 上传nginx到linux系统
3. 安装依赖环境
(1)安装gcc环境
yum install gcc-c++
(2)安装PCRE库，用于解析正则表达式
yum install -y pcre pcre-devel
(3)zlib压缩和解压缩依赖，
yum install -y zlib zlib-devel
(4)SSL 安全的加密的套接字协议层，用于HTTP安全传输，也就是https
yum install -y openssl openssl-devel
4. 解压，需要注意，解压后得到的是源码，源码需要编译后才能安装
tar -zxvf nginx-1.16.1.tar.gz
5. 编译之前，先创建nginx临时目录，如果不创建，在启动nginx的过程中会报错
mkdir /var/temp/nginx -p
6. 在nginx目录，输入如下命令进行配置，目的是为了创建makefile文件
7.直播推流模块
git clone https://github.com/arut/nginx-rtmp-module.git

注： 代表在命令行中换行，用于提高可读性
配置命令：
./configure \
--prefix=/usr/local/nginx \
--pid-path=/var/run/nginx/nginx.pid \
--lock-path=/var/lock/nginx.lock \
--error-log-path=/var/log/nginx/error.log \
--http-log-path=/var/log/nginx/access.log \
--with-http_gzip_static_module \
--with-http_ssl_module \
--add-module=../nginx-rtmp-module \
--http-client-body-temp-path=/var/temp/nginx/client \
--http-proxy-temp-path=/var/temp/nginx/proxy \
--http-fastcgi-temp-path=/var/temp/nginx/fastcgi \
--http-uwsgi-temp-path=/var/temp/nginx/uwsgi \
--http-scgi-temp-path=/var/temp/nginx/scgi 


命令 解释
–prefix 指定nginx安装目录
–pid-path 指向nginx的pid
–lock-path 锁定安装文件，防止被恶意篡改或误操作
–error-log 错误日志
–http-log-path http日志
–with-http_gzip_static_module 启用gzip模块，在线实时压缩输出数据流
–http-client-body-temp-path 设定客户端请求的临时目录
–http-proxy-temp-path 设定http代理临时目录
–http-fastcgi-temp-path 设定fastcgi临时目录
–http-uwsgi-temp-path 设定uwsgi临时目录
–http-scgi-temp-path 设定scgi临时目录




7. make编译
make
8. 安装
make install
9. 进入sbin目录启动nginx
./nginx
停止：./nginx -s stop
重新加载：./nginx -s reload
10. 打开浏览器，访问虚拟机所处内网ip即可打开nginx默认页面，显示如下便表示安装成功：
注意事项:
1. 如果在云服务器安装，需要开启默认的nginx端口：80
2. 如果在虚拟机安装，需要关闭防火墙
3. 本地win或mac需要关闭防火墙
```

[image](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/efe03bdf-ab0b-4a27-8736-723af62b9623/2020-09-17_201303.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466S67RZ3WS%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T224840Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQD8%2BRqZ0cwI4I%2Fw0qbpk01NzXd%2F6LoOh%2FEcXZlV6HBV5AIhAOvGMp0OrQpDbUQ%2BYB%2BLQwUe2k6vbdKHda%2B6nbdFSyw3KogECMb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgyVZI8cg1q89XDaoMMq3AOlBZQjNUWtv06bM2VvqFiQWbNUbIu3Tr899AaCSQbPI05To2sStM6%2FFtvW2eox5Kg9XzLHj4WJro7dvqbEgNxYJxs3dmj1PjR9iN8DctajGcKf0q3RGWTnTTUf3LKxlTw387iCHKKBsdr5ELE5%2BlzkHxId76z%2FCg9cafcKMPwVs8HNqYjxxnhZO393DMxr7Hcdo176cXollsi%2Bya38WD44%2F3GpINbni4ebAPjIv6t04TvfSQfH9GMxx%2BMIlVmKLcVK0xmasARdWhKdEXNhUwHkk%2BI9PMnazAOwKVq8WTP%2BIcouAQQYfRl2OAJZPLxvkezIZmxhtaOPUXcItwnGhV08ab1Kuxf9KbdN%2Foz2fT5Zp33X06129yCGQrAThR%2BMz2bTzbjxLNjHthIeApipgiONDF4ezuuiFXjjPKqKU8N1ajQf5zgtV5NSsp1Yrt5CCmjFvj%2FsYyUVrl%2B8xuqs5yG6z%2BQLASJ%2BC6QblUNV9Fr7GjC6kH8ksFoYyopKRoST91MYDZZ627ywdc0jqw12jsm9ZsaC8f0cQ6%2FwZ8SCVBjo4PeaSA7P4pPGi4Nexc1ep1KhZOuKPyCrO2YtRn0T3ssOkClGskJ69vt8ip0U7VE5Y1PaWhEwhf4ZBUf%2FmDCvuv%2FSBjqkAXiFIp%2Bk1dqS%2BkQNR7jfBDI5zuhjmfbTcsxf8zewlojD4sSsJFMRpxDVPlx1b0lWgXqDijm6rMWG42iXAcnUTjZHYxI28Tnqzb7DYLnmLm947bdBuLfEvs7jhFPtzMeUWnzaSaxXqNdZfbuCABplXgnaCN5tkL9xD8xoqqVDs2JSjTWNw8R%2Bz9wbwIc1qS%2BSceYhF7qNJTJm7MMg5BTQ8euP3nIU&X-Amz-Signature=f0e8afdfd81e30d1509bd6758757dbff544ab93b06c9b16570725d6027e0573c&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)


