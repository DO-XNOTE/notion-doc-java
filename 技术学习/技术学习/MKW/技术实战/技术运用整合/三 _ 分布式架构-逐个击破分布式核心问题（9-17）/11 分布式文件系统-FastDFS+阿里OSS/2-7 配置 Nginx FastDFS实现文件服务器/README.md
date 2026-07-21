---
title: 2-7 配置 Nginx FastDFS实现文件服务器
---

# 2-7 配置 Nginx FastDFS实现文件服务器

[image](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/60263fd6-56bf-4a08-9225-aa778755a16d/SCR-20240806-jsxq.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667R4QAHDD%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T225222Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIHGTZ7vl54xjiSQUwD8e5wHJ9RYL9wM6sF%2BbVKtbZ1%2BMAiEAz1i%2FHeestzVMcREbTlO2tkUAzygWDzTyGEhjBPgC694qiAQIxv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDAQrVSjnZHNifrZlnircA4rfWpdXzG1Ny8UVyQuqv4QDSoXobGpfpT%2Fa04dMWeb6Hho2eksqCo0vR5bRZN9GZ1y3wOUxuXKu9Mjd0NEmcHw3vbuZKjcOJ0GAt3FJKY6ABQTK1rx1qJ1Yx%2BbYP3%2BuROsAtfXHT60fzHKV6uAZfxmFtE84tRgO39O1m%2BsmPcClUpX2AiVwZa9UhtLlUe246CJoD0We3uUY6NZ53uFFxU8b6GtSYa%2FJaQIpYppj1IKTArA7O8IK8aQDgJbb8pnFzeMEtuQX%2FbApdLscOFX%2BduLfRtmL41iOEd15bJvneAux60gwdBr3GTCpRbp0VG1QQlEojCRUh2cJd%2FrfuhFnHbSRw%2FNmGijPJ6O4ELvml%2BGgOmWMxFswisMI%2FEoTSGt3Ra53BDS5dYMLM%2F4LGJSNL02mkZPXpmcjP%2Ba2f0FnzBiIQ%2F3v%2BpiI9ZBpCsWne%2BnYp72Gtp7oO7U8VaXKqlu9mXR51lmwoi%2BSRwKcNdcbZnhSW93sQwZB1hARiNTBBCYJAgB%2BYYGTVbXMo8ct7Prc9GOM3NQQyQhDW%2BlSVShm6rkXmkx7qDqwN4sP4%2BtxnY02%2B%2BWe52%2BjQkSab%2F%2BkhdmNcaWw%2F6voLRzXhJ3eVieX4lTKN5TGdduG6B06AIbrMLG3%2F9IGOqUBIuCEe2%2FCgT9sFJvgUBqUPz8RlzlNzsQymuZzQAyZNkc55yAE6pF582ee%2FtyNk%2BrOEcfRAdQCgSwpPcFd3xFuZrIEY2G9%2F9num3BN7oo8QOjDtxiTzcw1b%2FD8o33ombmsDfGcPIDecXAazOy4tl8F6Zt6%2FvBnoosEN4%2FxbyU6%2F%2BO33E7h4KrF7viYfEm%2FYCe%2FcV1fgF67rWMJk5H6vEQQ8B%2FilQxo&X-Amz-Signature=9510590ebd09e40ac48b28a1380d1998e4fdc324704c1b18ca8791503075501f&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

那么前两节我们是配置了 tracker 以及是storage，目前其实我们已经是实现了通过命令行去进行了一个上传，那么文件上传是 OK 的，没有问题。接下来我们要去安装一下它的一个 engines 第三方的一个模块，因为我们现在还无法通过咱们的浏览器去进行一个访问，所以我们要去做一个相应的配置。好，然后我们进入到home，然后再进入到software。好，进来看一下。那么在这里呢，我们要去安装nginx， Nginx 一定要和你的 storage 安装在同一个节点上，那么这样子你的服务才能够对外发布，才能够被访问到。


那么这样子的话来看一下，首先的话我们先来看到有一个 fast d f s nginx module，那么这就是它的一个第三方的模块，也是由作者所提供的，然后我们做一个解压。好，OK，解压成功，然后进入到当前这个目录。那么这里面包含了一些相应的内容，那么随后的话其实会有一个文件，这个文件的话叫做进去看一下有一个src，然后有一个configure，这个 config 文件你是需要去做一个配置的。 theme 打开 config 这个配置文件，那么其中这里面其实是有一堆相应的内容，那么你可能会看不懂，但是没有关系，我们只需要去修改一下就可以了。


我们搜一下斜杠 local 回收一下，在这里有一个user，斜杠 local 这边也有一个 user 斜杠local，那么这个 local 的话其实就是它所释放，我们之前在安装的时候会释放一些相应的文件，那么这个文件释放完之后，那么在这边我们其实是要去做一个整合的，只不过在这里的话，它的这个目录是不正确的。

[image](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/7046d18a-3c6f-4e30-bda7-ed1a363ca288/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667R4QAHDD%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T225222Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIHGTZ7vl54xjiSQUwD8e5wHJ9RYL9wM6sF%2BbVKtbZ1%2BMAiEAz1i%2FHeestzVMcREbTlO2tkUAzygWDzTyGEhjBPgC694qiAQIxv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDAQrVSjnZHNifrZlnircA4rfWpdXzG1Ny8UVyQuqv4QDSoXobGpfpT%2Fa04dMWeb6Hho2eksqCo0vR5bRZN9GZ1y3wOUxuXKu9Mjd0NEmcHw3vbuZKjcOJ0GAt3FJKY6ABQTK1rx1qJ1Yx%2BbYP3%2BuROsAtfXHT60fzHKV6uAZfxmFtE84tRgO39O1m%2BsmPcClUpX2AiVwZa9UhtLlUe246CJoD0We3uUY6NZ53uFFxU8b6GtSYa%2FJaQIpYppj1IKTArA7O8IK8aQDgJbb8pnFzeMEtuQX%2FbApdLscOFX%2BduLfRtmL41iOEd15bJvneAux60gwdBr3GTCpRbp0VG1QQlEojCRUh2cJd%2FrfuhFnHbSRw%2FNmGijPJ6O4ELvml%2BGgOmWMxFswisMI%2FEoTSGt3Ra53BDS5dYMLM%2F4LGJSNL02mkZPXpmcjP%2Ba2f0FnzBiIQ%2F3v%2BpiI9ZBpCsWne%2BnYp72Gtp7oO7U8VaXKqlu9mXR51lmwoi%2BSRwKcNdcbZnhSW93sQwZB1hARiNTBBCYJAgB%2BYYGTVbXMo8ct7Prc9GOM3NQQyQhDW%2BlSVShm6rkXmkx7qDqwN4sP4%2BtxnY02%2B%2BWe52%2BjQkSab%2F%2BkhdmNcaWw%2F6voLRzXhJ3eVieX4lTKN5TGdduG6B06AIbrMLG3%2F9IGOqUBIuCEe2%2FCgT9sFJvgUBqUPz8RlzlNzsQymuZzQAyZNkc55yAE6pF582ee%2FtyNk%2BrOEcfRAdQCgSwpPcFd3xFuZrIEY2G9%2F9num3BN7oo8QOjDtxiTzcw1b%2FD8o33ombmsDfGcPIDecXAazOy4tl8F6Zt6%2FvBnoosEN4%2FxbyU6%2F%2BO33E7h4KrF7viYfEm%2FYCe%2FcV1fgF67rWMJk5H6vEQQ8B%2FilQxo&X-Amz-Signature=965dde3dfc46878df4c5d88dff7e50dbcf24cf044ed33a0e7df607ec3142f013&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

这个目录是在 user local 之下，但是来看一下，我们其实是在 user include，我们是在这个里面，它是没有 local 的，我们之前在安装的时候其实也是看了这个 make 点SH，对吧？它是没有这个 local 的，所以可以进去看一下，它是在这个里面包含了一些相应的一些内容，它是释放到这里面的，所以我们只需要去做一个修改就可以了。


回到之前的一个目录， home software fast d f s。回过头来，在这边我们直接把这个 local 给去掉就可以了，因为 user include 是它默认的一个路径，所以在这边去做一个修改，然后修改完这两个地方之后直接保存，那么这个 config 文件就已经是 OK 了。


好，那么随后那么当我们这个 config 文件配置好了以后，在这边还能够看到有一个文件叫做 mode fast d f s，我们先把它做一个拷贝，把它的 copy 拷贝到 e t c 下的 f d f s，把它统一的放在我们其他的一些里面。


进去看一下，放入到我们当前的这个目录之下，有一个这个配置文件，这个配置文件就是我们和 NX 之间相互联调，是需要去使用到的一个配置文件。我们后面是需要去用到的，所以我们暂时先拷贝过来，我们先不去修改。好，随后接下来的话我们就需要去做一个安装Anex，那么当前我们这个节点 Anex 其实没有，所以我们再去，我们要需要去安装一下，我们回到之前的目录。那么在这边也会有一个engines，这边我就快速的去安装一下，因为我们之前其实都已经是安装过，那么首先它也需要有一个 GCC 的一个环境，那么已经是安装好了。安装好之后那么我们就不再去安装了，下一个是这个 PCRE level，把这个去安装一下，最后下一个，那么下一个是一个 c lip，我们也要去做一个安装。好，然后下一个是 open SSL，你去安装一下。这些都是 engines 的一个基本环境，我们之前在安装的时候其实都是有讲过的，然后在这边当前这一台节点上并没有安装，所以我们去安装一下它的一个基本环境。那么这样子我们才能够去把咱们的 enginex 去做一个安装好，OK，随后我们把这个 endings 去做一个释放啊。使用 time 命令去进行一个解压，好，解压成功之后，然后我们进入到 engines 这个目录。


那么接下来我们要去做一个 config 这个配置的，对吧？这个配置的话不要忘记有一个MKDIR，之前我们有一个 champ 文件，有一个目录，我们要去创建一下的，这个我们要去创建一下，不要忘记了让 p 在 v AR temper engines 放 p 去创建一下，这一步骤不要忘记。


好，随后我们就要去做一个 config 这样的一个配置了，那么配置之前我们先把这个看一下，我们先来看一下 faster GFS engines，当前这个里面，这里面会有一个 s r、c，那么如果说我们要把这个模块加载到我们的 n 进去里面来的话，那么这个当前我们要进入一下SRC，进去 PWD 这个路径，你是需要去额外的以一个模块的形式加载，加入到我们的 endings 里面去的，那么这一点是需要去注意的。那么随后的话我们这样子回到我们的engines，回到 ending 思目录，然后接下来我们就需要去使用到 config 这个命令了，那么在这里我把这样的一段配置我也是直接先拷贝过来看一下。


就是这个内容和我们之前是一模一样的，完全的一模一样，只不过我们现在注意一下，在这个后面多加一个反斜杠回车，你要去额外的去追加，你要去添加一个模块，杠杠来一个 ads 杠module。这个是指添加一个模块，然后你要把后面的一个路径给复制进去，也就是这一段路径拷贝一下贴到这个部位，那么这样子的话，其实我们就是在最后一行 at module 添加了一行，把这个作为我们的一个模块添加到了 Nginx 里面去了。回车一下，那么这个时候它会做一个相应的配置，好了以后，OK，那么接下来我们呢？ make 备考了之后，我们再去做一个 install 好，OK，然后 install 一下回车好， install 成功了。好，那么接下来，那么现在我们 endings 其实已经是安装好了，只不过我们也没有去配置它的一个配置文件，也没有去启动它的一个命令，没有去启动它。


好，接下来我们还要去做一个修改，那么这个修改的话进入到 etc 下FDFS，这一回我们要去修改这个mode， fast d f s 点 config 这个配置文件了，那么这个配置文件打开看一下。那么打开以后有一些内容我们是需要去做配置的，那么首先可以看到还是一样还有一个 base pass 这个地方，我们也要去做一个对应的修改。在这里使用这个 user local，再来一个 fast d f s，我们放在当前这个目录之下，作为我们的一个temper，那么这个其实也就是存储一些 log files、一些日志文件的。把这个目录拷贝一下，我先保存，然后 MKDIR 好，OK，那么这样子的话我们就已经是创建了，当然也可以进去看一下，目前里面有tap、 storage 和client。好，接着我们还是一样修改这个文件。那么下一个我们要去配置的，我们来找一下，往下面搜，其中会包含有一个叫做 track Server，在这里这个你要去修改的写一下，192.168.1.155，OK，这是我们的 truck Server，然后再往下你会发现有一个 group name 默认 group one 修改掉，我们使用 m 可。然后再下一个是询问我们 URL 中是否要包含 group name，那么在这里它是一个false，我们把它给开启改成true，开启一下，那么这样子的话，我们在 URL 中会可以看到这个组名，也就是m，可我们是能够看得到的，好，保存一下。那么这样子我们当前这个配置文件就已经是修改成功了。


随后我们进入到 Enginex 中，那么接下来我们要去启动engines，但是其中我们也要去做一个相应的修改，我们去修改它的一个 config 文件啊。修改安静时间，config，在这里面往下面搜，往下面找到一个虚拟主机，我们有一个80，对吧？我们要拷贝一下，我们先把没用的一些内容我们可以去删掉，这些注释太多了，我们都删掉。


好，OK，那么这个是 Server 80，对吧？那么 80 的话我们直接修改， 80 我们就不要了，我们改叫改成 88 四个8，那么四个 8 的话就是和我们在 storage 里面是配置的一样的，那么这一点的话你是需要去注意的，如果说你在这里不是配置的 4 个8，那么你再去访问的话可能会访问不了，这一点是需要去注意的，那么这个在官网里面其实也是有提到过的，在这里有提到说该端口为 storage config 中的一个 HTTP 点 Server port 是需要设置为相同的。


那么设置三农业以后，那么你才能够去做到一个相应的一个通信，好，然后在这边有一段内容，这段内容其实就是它的一个配置，那么你也可以去做一个相应的拷贝。在这边我们拷贝这个location，我们把这个 location 直接拷贝一下，拷贝贴过来，贴到我们的这里面来，这是它的一个匹配规则。
好，OK，那么在这里的话，这个是它的一个第三方的模块，我们使用这个就可以了。然后在这边会有一个location，那么这个 location 的话，它其实映射到的组名是 group 0- 9。但是我们其实在这个地方我们不是这个，我们直接改掉我们映射的一个组名叫做MK，我们把这个改掉就可以了，然后的话在后面你可以再加上一个M00，这是它的一个虚拟路径。这个前面这个我们也不需要使用，这样子就可以了。


好，那么这样子配置好之后，那么这个就可以作为我们的一个文件扶持的一个服务地址所对应的一个虚拟主机保存一下，那么接下来我们就可以去启动了，我们进入到 SB 目录之下，我们来杠 t 测试一下，那么现在就是 successful 成功的，没有任何问题，随后我们可以去启动一下。好，OK，那么现在我们是启动成功了，那么启动成功之后我们就可以去做一些相应的一个测试工作了。


那么这个的话我们是可以使用之前的一张图片，那么之前的图片我们去找一下，我们就不再使用 client 去做上传了。我们进入到storage，进入到00，应该是先进来，进来之后 CD 00 杠00。有这样的一张图片，我们把这个图片拷贝一下，拷贝之后，现在我们打开咱们的这个浏览器，在这边我们可以去搜一下啊。我们直接先把这个文件名先拷贝过来，然后我们在这里面一步一步可以去拼一下。


那么首先 HTTP 冒号斜杠我们的文件服务器的地址，也就是storage，或者说是 endings 所在的一个地址，192.168.1.156，冒号四个8，不要忘记拼一下。随后斜杠要加上我们的组名 i mock，再来一个回车M00，再来一个斜杠00，再斜杠00，那么这个尤其是相当于是找到某一个小区，这是这个小区的一个门牌号，再找到某一个人，随后回车，那么这个时候你会发现我们这个是404，对吧？那么 404 说明我们当前这个图片找不到。


那么这个图片找不到的话，其实也就是它的一个存储路径没有找到，那我们回到咱们的这个命令，行，我们这样子进入到 etc 下FDFS，然后去修改这个mode， fast DFS 这个是我们刚刚所修改的文件，那么进来看一下，我们之前其实是配置了一个叫做base，往上面找有一个 base pass，这是我们之前所配的，但是我们在这个下方其实你能够看到它有一个 store pass，这里我们没有去配，所以在这边我们把它修改一下。


我们把它修改到和我们的 storage 是一样的，也是在 user local fast DFS 之下。 storage 保持和这个一致。好，拷贝一下保存，然后我们进入一下，OK，这是当前的这个目录，那么这个和我们之前的 storage 是一起的。然后我们再来刷新一下，我们这样子去重启一下咱们的 engines 扁斜杠、 engines 杠 s 与load。好，OK，刷新，那么这个时候你会发现这张图片是我们之前所上传的这张图片，那么现在我们可以成功的在咱们的这个浏览器里面，通过咱们的一个 URL 去进行了一个访问。


那么一定要注意在我们刚刚出现的一个小问题，也就是我们的一个 store pass 存储的路径是需要和你的一个 storage 的存储路径要保持一致，那么这样子的话我们的 engine 才能够识别到，识别到以后它才能够在浏览器里面做到一个相应的展示。那么如果说你要去进行一个下载的话，直接右键图片存储为，那么它可以去做一个相应的下载。那么这样子咱们的fast、d、f、 s 和 Nginx 就已经是结合到了。


