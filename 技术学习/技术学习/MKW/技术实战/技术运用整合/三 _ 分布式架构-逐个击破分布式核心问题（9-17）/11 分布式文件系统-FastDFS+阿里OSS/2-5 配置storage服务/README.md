---
title: 2-5 配置storage服务
---

# 2-5 配置storage服务

[image](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/037973a0-4eba-48a4-8b55-b3f07cad5ecb/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UQBTQDCD%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T225222Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDUQ1dKWsK%2FT6WdC%2BZj1HWqqPBvtblgDNeZmq4flpBtsQIhAIC7uWEHcwp0ZYXOEkqXCckxK6Nh00NDJvOJAZV1wmRoKogECMb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgwZHIa%2BLJGMeK3Sf%2BEq3APLiJ3gjBJu%2BSf7eFtiNQ4nnIDQqZ1c%2BgUXumaDj1HkRfW3OeowZMh5NL2YUxcEvKmtKcmr1dO3e1p61VoQYCuvzbLFtdSJPN31AnfXuw0veMFd5RZNkc7u6UeLswfMMF5VDoRq2N%2F1RO8rxBdDuVP%2Fss1ypCwku1FK0eVGX00InMWLlst3OcYwNFAymwfPAiJ7tWC7wuQ15dCZ%2FbD1K%2BawHprcVbG4Fczi92jvGVNDgjxef%2FyDhR5MJhXV1zDpd3UfL6lAE2MgZYx9Rzyl%2B50IggP%2FYfJi23bkt%2FYukZK5EDw6rAQEWffQMQO%2BaU6X7Anj%2Fa6TUgGaQ1zUcVreGi9ahUNN7PFBtMVZ0qRSOOvC6TxBZTj%2FMIy99rWJGj%2BHeiM718qqHouFBiOBf8ye7YejzuiafU9UqC3H4wMlOJnr1nQRpjQDqSxVOtVNjuIrNV9G3gi%2B7IciDV%2B9ZVYQL0z6f5Ir7W7fFgooWV37TJ3pr%2BbeR6MG6zwQTY%2B8ZmtgmioFGxli6vSdBrwF19Mw%2BFWrDUfDaoWpoDSHgUhZft3qnDUJ7iXzVYVk5CdV9TqZVPAZvzvbRpAuPpip7sYE0GBfpCexrkVwYE9Umn8peKM8LYDbFHrtsuaDWjvSgTC3uP%2FSBjqkAUECNg%2BAHaKh7aHKctg0C3602Vs0M5P6xV%2BXtU2GYUzBM0BWHt2GMBC%2FY%2BEBW7I50GN%2BtNNmXo88jC%2FLqad1TtnyWpAl7WkY4w7j5QthcISMN8hjcEzxMXqjBvUV8%2FyhJHkgj1APAGi7%2FydYdMVUr12IBkfh%2BOLJiPTAqWnFxb0SRMyAPY3%2B8mHKOKDlyfRFunTLsMhD9Oc4XdnSFqAoukmWGZVs&X-Amz-Signature=017b712c6b2570ff4c02d340de9c98b068ad95b72700012bb149f54a0d8e9358&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

那么上一节我们是把这个 tracker 服务去做了一个安装配置，那么接下来我们是需要去配置一下咱们的这个storage，这个服务还是一样，我们进入到咱们的一个配置文件目录，在 etc 下的FDFS，在这里面我们要去修改这个storage，点 config 这个配置文件。


在这里面，那么我们要去修改的一些内容就要比 track 里面稍微的多一些，那么首先我们来看一下第一个地方，在这里有一个叫做 group name，那么这个就是一个组名，或者说是一个卷名，这是它的默认是 group one。在这里我们去做一个修改，我把它改成这个 i MOOC。那么这个我们在后续检验的时候，那么我们是可以通过 URL 上去看到的。好，那么这是我们第一个所需要去修改的地方，随后下一个在这里有一个叫做port，那么这是它的一个通信的短口号，默认23000，那么这一点的话在这里注意一下，我们使用默认的就可以了。


然后再往下的话有一个 base pass 在这里也有，所以我们也去做一个相应的修改，在这里使用 user 下local，然后 fast d f s 斜杠storage，那么这个是作为我们的一个 storage 的一个 base pass。OK，好，然后我们把这个先拷贝一下，拷贝保存，然后我们做一个创建。然后我们可以去进入到 user local，那么在这里面它就会多了一个 fast DFS，然后再进去看一下，那么这个它是会帮我们创建的。


好，回到我们刚刚之前的一个目录，我们接着去修改这个storage。然后下一个的话我们往下面看。它除了当前这个 pass 以外，它还会有一个pass，有一个存储的一个路径。在这个下面有一个 store pass 0，那么这个我们也要去配的，那么这个是它的一个地址，我们这样子我们先把之前的一个地址直接拷贝一下，以防万一我们拼错。 user local fast DFS storage，把这个路径留在这边，我再拷贝一下，然后再去修改，把这个地址直接给删掉。


那么这样子的话，我们的一个 base pass 和 store pass 0，那么这两个路径我们都会采用同一个路径。好，那么这是我们的这个 store pass，随后下一个，那么在下方它还会有一个 track Server，那么这个其实我们在之前也说了， track 和我们的 storage 它们两者之间其实会有一个通信的一层关系，其实就是一层心跳。


那么这个在我们的这个 storage 里面是需要去配置的。那么我们配置只要配置一个，把其中的一个先注掉，配置当前这个节点，它的一个节点所在的位置，我们是在192.168.1.155，应该是这个节点，我们可以串一下。OK，是 155 这个节点，所以我们把这个 IP 写过来，那么这样子的话，我们的 storage 就能向 Tracker 发送一些相应的状态信息了。好， OK 啊，今后我们还有一个地方，我们再来看一下，它还会有一个端口号。我直接搜一下斜杠 4 个8，在这里有一个 h t d p 点 server 杠port，这是一个 Web Server 的一个突然口号，那么这个我们现在暂时还没有用，等到我们后续和咱们的 emix 配合之后，那么这个端口号就会起到相应的一个作用了。


好，那么现在我们直接保存一下，那么这样子我们 check 相关的一些内容，相关的配置我们就已经是配置好了，那么配置好了以后，接下来我们是需要去做一个启动，我们还是这样子使用 user Bing，然后 FD f s 下划线 storage 的，使用的时候去加载我们当前的这个 storage 的 config 这个配置文件。回车一下。那么这个时候在这里报了一个错，说我们这个 storage 点 configure 不存在，那么没有关系，我们这样子我们使用它的一个完全的绝对路径 e t c 下 f d f s 应该是 storage 点config，回车一下，OK，那么这样子就能够去加载并且启动了。


最后我们来看一下它的一个进程。 PS 杠 e f 来看一下它的 storage 回车，那么这样子，我们的这个 storage 现在就已经是启动成功了，一定要注意我们在进行配置的时候，之前我们也是说了 tracker 和 storage 它们之间的话， track 一定要先启动，启动完毕之后你再能够去启动它的一个storage，要不然我们的 storage 它的心跳会发不过去的。


好，那么现在我们这两个服务我们都已经是配置 OK 了。那么配置 OK 了以后，那么现在我们是可以去做一个测试。测试什么？我们可以通过命令行，去测试我们的一个文件，我们去测试某一个文件能不能够被咱们去进行一个上传吧。我们这样子，我们在当前 storage 里面我们去配置一下，看一下在当前的 etc fast DFS 这个目录之下，它会有一个 client 点config，那么这个是一个客户端。这个客户端的话我们去配置了以后是可以去做一个上传的动作的。所以我们去修改一下，修改这个 client 点 config 文件，那么在这里面我们就要去做相应的修改了，那么可以看到这边又有一个 base pass。所以我们去修改一下 user local，然后 fast d f s 斜杠client，注意不要拼错。然后我把这个拷贝一下，我先保存一下，然后 make DIR 回车创建成功吧。然后进去看一下。


那么当前这个目录里面包含了client，也就是storage，好，那么还是一样回到 etc 下FDFS，那么这个时候我们还要再去修改 client 点config。那么这个文件里面还有一个地方我们也要去修改，那么就是它的 track Server 在这里看到我们注掉一个，然后再把另外一个去做一个配置，改成192.168.1.155，这是我们的 track Server，好，OK，保存，那么这样子我们的这个当前这个配置文件就已经是配置好了。


那么配置好了以后，我们可以来做一个测试，测试的内容就是用于去做我们的一个上传。如何去测试？上传呢？我们来看一下，我们进入到user，然后 being 目录之下，我们来看一下 f d f s 星号，在这里面会有一个叫做 FD f s 下划线test，我们可以使用这个来测试一下我们的一个当前整个 track 和 storage 有没有安装成功，因为我们最终的一个目的要去把我们的文件去做一个上传嘛。


那么上传之前我们是需要有一个文件，那么这个文件的话我们可以去找一下，打开浏览器，你可以随意的去找一下，在这边我随便拷一张图片，复制图片的一个地址，然后我们通过在这里面我们 w get，我们去做一个下载，然后回车一下。那么现在目前已经是下载好了，下载好的话是在我们当前的目录里面 l s content 星号。然后我把这个做一个移动move，当前这个文件 content home 转移过去，当前的这个目录之下包含的内容太多了，然后我再对它做一个重命名 move content，把它修改为一个叫做IMK，点 j p g。


好，OK，然后我们就可以做测试，做一个上传，我们这样子， user Bing f d f s 下划线test，使用刚刚的这个命令，然后空格一下，这个时候我们就要去做一个上传，那么上传的话它会有一个命令叫做upload。使用这个命令，然后后方再去加上我们要去做一个上传的一个路径，那么这个路径是在我们 home 之下，直接 m 可点 j p g，那么这样子就可以去做一个上传，但是不要忘记在使用这个 test 这个命令的时候，那么我们也要去加载我们的一个配置文件的。


这个配置文件就是我们刚刚所去修改的一个 client configure 这个配置文件，那么是在 etc 下 f d f s 有一个 client 点config，那么这个结构就是我们通过 test 这个命令，然后加载 client 配置文件，然后 upload 一个图片。然后我们在这边回车一下。那么这个时候当我们回车以后，在这边可以看到有一堆的日志信息，那么如果说你上传成功之后，在这边它会返回给你一个内容来看一下。


那么这些就是我们和咱们上传图片的一些相关的信息，其中就会有一个叫做 group name，这个就是我们的组名，另外有一个 remote file name，这就是我们上传之后的一个文件的名称，在这个里面。然后我们再来看一下它最终结合的一个地址是在这里，是这个地址，但是这个地址的话，如果说你去拷贝，你可以尝试一下去访问是访问不了的，因为这个并不是一个真正的服务地址，你是访问不了的。我们后续要结合engines，那么这些都是它的一些日志的信息，那么像这个 size 等于多少？然后呢？ time stamp 等于多少？那么其实这些的话都是它的一个元数据信息吧。


好，然后我们现在其实已经是上传成功了，那么我们进入到 user local fast d f s 下的 storage 来看一下，这里面有一个data。然后我们就能够看到在这边有很多很多的一些文件名，那么这个其实是由 storage 来帮我们去做的一个生成。那么在我们当前目录之下，我们 PWD 那么这个 data 的话，其实就是相当于我们之前在上传成功之后的有一个叫做M00，相当于就是这样的一个路径，这是一个虚拟路径。然后后面的话就是它的一个真实的路径了，我们可以进入到零零下的，零零可以进去看一下 CD 00，然后我们再来看一下LS，你会发现这里面又有一堆的文件夹，这些都是由他来帮我们去创建的，相当于是你住在家里的一个门牌号地址，他会帮你去做好相应的配置。


某一个人要做到哪里去分配一下，那么图片文件上传其实也是类似的一个道理，我们在 CD 00 再进入一下看一下，这个时候就会有相应的图片了，那么这个图片就是我们之前所上传成功之后的一个图片，都会保存在这个当前的目录之下，在零零杠零之下，然后在斜杠拼接一下你的一个图片的名称。
这个图片的名称的话，我们可以这样子，直接你可以拷贝这一段内容，这是他的文件名，然后LS。后面加上一个新回车一下，那么这总共是四张图片，都是刚刚我们所上传的，那么上传之后它会帮我们额外的去做一些相应的生成的。那么这样子现在我们其实通过命令行的一个客户端的测试，那么就验证了我们的 tracker 以及是 storage 这两个服务我们都是成功的安装了，其实也就是 fast d f s 这个本体我们都已经是安装成功了吧。

[image](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/b699b32c-26ab-44bf-a27b-b0ccbce6f507/2020-09-17_174130.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UQBTQDCD%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T225222Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDUQ1dKWsK%2FT6WdC%2BZj1HWqqPBvtblgDNeZmq4flpBtsQIhAIC7uWEHcwp0ZYXOEkqXCckxK6Nh00NDJvOJAZV1wmRoKogECMb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgwZHIa%2BLJGMeK3Sf%2BEq3APLiJ3gjBJu%2BSf7eFtiNQ4nnIDQqZ1c%2BgUXumaDj1HkRfW3OeowZMh5NL2YUxcEvKmtKcmr1dO3e1p61VoQYCuvzbLFtdSJPN31AnfXuw0veMFd5RZNkc7u6UeLswfMMF5VDoRq2N%2F1RO8rxBdDuVP%2Fss1ypCwku1FK0eVGX00InMWLlst3OcYwNFAymwfPAiJ7tWC7wuQ15dCZ%2FbD1K%2BawHprcVbG4Fczi92jvGVNDgjxef%2FyDhR5MJhXV1zDpd3UfL6lAE2MgZYx9Rzyl%2B50IggP%2FYfJi23bkt%2FYukZK5EDw6rAQEWffQMQO%2BaU6X7Anj%2Fa6TUgGaQ1zUcVreGi9ahUNN7PFBtMVZ0qRSOOvC6TxBZTj%2FMIy99rWJGj%2BHeiM718qqHouFBiOBf8ye7YejzuiafU9UqC3H4wMlOJnr1nQRpjQDqSxVOtVNjuIrNV9G3gi%2B7IciDV%2B9ZVYQL0z6f5Ir7W7fFgooWV37TJ3pr%2BbeR6MG6zwQTY%2B8ZmtgmioFGxli6vSdBrwF19Mw%2BFWrDUfDaoWpoDSHgUhZft3qnDUJ7iXzVYVk5CdV9TqZVPAZvzvbRpAuPpip7sYE0GBfpCexrkVwYE9Umn8peKM8LYDbFHrtsuaDWjvSgTC3uP%2FSBjqkAUECNg%2BAHaKh7aHKctg0C3602Vs0M5P6xV%2BXtU2GYUzBM0BWHt2GMBC%2FY%2BEBW7I50GN%2BtNNmXo88jC%2FLqad1TtnyWpAl7WkY4w7j5QthcISMN8hjcEzxMXqjBvUV8%2FyhJHkgj1APAGi7%2FydYdMVUr12IBkfh%2BOLJiPTAqWnFxb0SRMyAPY3%2B8mHKOKDlyfRFunTLsMhD9Oc4XdnSFqAoukmWGZVs&X-Amz-Signature=249cf459247f4ace396197dc7f4ffaf5245ae86941ac2dba83cd84661b474d56&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)


