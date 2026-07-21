---
title: 1-7 安装 elasticsearch
---

# 1-7 安装 elasticsearch

[image](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/8c5ad816-1c29-4a1c-a59d-88c407162f67/SCR-20240805-oeqs.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SIOPZF47%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T225127Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIEuUQkTM3jiHXvFlpf6tLGTWkWsw8iasRuKbhwgU2XihAiBgvLoBqlpP9RRklbKxwvjbQ38%2FYp%2FLwQyK8RguQPaSPSqIBAjG%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMpTN4iTOfM%2BPnXa5kKtwDdlKVXcCG6t4NIifzWMlz0y5p3W0PoWYkVR1zkfzHafxkJkMrRcV3I7sXN0UQKIgTR%2B1wmDojzxKQyV2vPQUXcUp6X1cUPBzLH7sQULbuLbM1sTSetznFopLSj4F4kIVpa43eIeWpSM%2BAURrPyGSu%2BDHtZT0YyqGVUapMBGmCQ8CsN19M7RAA7x9r2ncor%2B65ldLFM1vEs%2FLeVISiFQQ6R4j5WPdhsdZsnjxWCeUo0juD07PqbpwGEJ7gLknXxoFZsGoJjP7IJd19nbIIhodQy%2FveiY9sEISOYfHV1PSZKTExyQRsuq5OCMJulczGa2vClpL%2FrPm092NybOThXnmuBa%2Bwp37K6qHzZwE%2F4ZpRJw07Q4AptkXPTA7wTtP4HonSxlJ%2FhzvSvFJ3auV1HoyzzMs9oQ%2BHqcHyZVP0mrylQ8SjWJbVkHkqLNgYfyNBWHhxQFo7VtbhkFfUtaF91i11Ay9ENVZhnIcI1Ku%2BhQ3hu11FTT6OYcB1xkGV0fKtHdgxTB%2BErr6u%2FINYLWdJjR5YwnKsMPbXkyUdXVD6vJa81kr3u7D2haLWTuAOn2hd8hbjj8kxoLm1Jz7OnKfRzCBsMIH07iogSg9fmX2zV9gxRe21adgu2OFg4WHIjgwwsLr%2F0gY6pgHXJNIPhFUis0FV1nf3iehRvVcw1q%2BCXAAAV7jKMKBZH2mZ6YsZw9jF3K0XultP2XzOX0oKliN7R4kkJ34abB5jeKALgkr%2F7Xnj61VfwXIKtdYaIMTmc%2BG%2B5IdF%2B05WamavirmL1lF8WNne7NyKJjpBpTwxUuw%2F3FzMvxDpBruqymAhh6hMFgEURxj%2FNnhoX%2BKivqFIE3j6DpeGLS4qPz6akmmGHobr&X-Amz-Signature=e2eefee375442520f069205feea4a69bb367ad21d62ee0a2cee83dbe3583c02b&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

[image](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/8095fc5d-447c-4fee-9edd-7eb433c8e72c/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SIOPZF47%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T225127Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIEuUQkTM3jiHXvFlpf6tLGTWkWsw8iasRuKbhwgU2XihAiBgvLoBqlpP9RRklbKxwvjbQ38%2FYp%2FLwQyK8RguQPaSPSqIBAjG%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMpTN4iTOfM%2BPnXa5kKtwDdlKVXcCG6t4NIifzWMlz0y5p3W0PoWYkVR1zkfzHafxkJkMrRcV3I7sXN0UQKIgTR%2B1wmDojzxKQyV2vPQUXcUp6X1cUPBzLH7sQULbuLbM1sTSetznFopLSj4F4kIVpa43eIeWpSM%2BAURrPyGSu%2BDHtZT0YyqGVUapMBGmCQ8CsN19M7RAA7x9r2ncor%2B65ldLFM1vEs%2FLeVISiFQQ6R4j5WPdhsdZsnjxWCeUo0juD07PqbpwGEJ7gLknXxoFZsGoJjP7IJd19nbIIhodQy%2FveiY9sEISOYfHV1PSZKTExyQRsuq5OCMJulczGa2vClpL%2FrPm092NybOThXnmuBa%2Bwp37K6qHzZwE%2F4ZpRJw07Q4AptkXPTA7wTtP4HonSxlJ%2FhzvSvFJ3auV1HoyzzMs9oQ%2BHqcHyZVP0mrylQ8SjWJbVkHkqLNgYfyNBWHhxQFo7VtbhkFfUtaF91i11Ay9ENVZhnIcI1Ku%2BhQ3hu11FTT6OYcB1xkGV0fKtHdgxTB%2BErr6u%2FINYLWdJjR5YwnKsMPbXkyUdXVD6vJa81kr3u7D2haLWTuAOn2hd8hbjj8kxoLm1Jz7OnKfRzCBsMIH07iogSg9fmX2zV9gxRe21adgu2OFg4WHIjgwwsLr%2F0gY6pgHXJNIPhFUis0FV1nf3iehRvVcw1q%2BCXAAAV7jKMKBZH2mZ6YsZw9jF3K0XultP2XzOX0oKliN7R4kkJ34abB5jeKALgkr%2F7Xnj61VfwXIKtdYaIMTmc%2BG%2B5IdF%2B05WamavirmL1lF8WNne7NyKJjpBpTwxUuw%2F3FzMvxDpBruqymAhh6hMFgEURxj%2FNnhoX%2BKivqFIE3j6DpeGLS4qPz6akmmGHobr&X-Amz-Signature=59808b3975dd797213ee2cf65a289e6ba3ec984353b4e7f7638ade56da7078b7&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

这个 elsc search 给下载一下，然后做一个安装，我们要把它给玩起来。那么这是它的一个官方的网站，在产品这里面往上面找，找到一个下载，然后点击一下，在这里面，随后就能够看到 ST search 那么当然除了 ES 以外的话，其实它还有其他的一些产品都是它的一个生态，它的一个生态是比较全的。那么点击这个下载点一下。


然后看到现在目前的一个最新的版本是七点四点二我们会下载这个。那么这边有很多个版本，那么我们是以这个 Linux 为主，所以去点击这个 nex 去做一个对应的下载就可以了。那么目前的话其实我已经是下载好了，并且我已经是上传到了咱们的一个虚拟机。那么在我本地，那么我是构建了一个来看一下是幺九二点幺六八点幺点幺八三我是以这个 183 作为我们的一个服务的地址。那么随后咱们来看一下。那么进入到 home 下，然后再进入到 software 那么目前这个 elected search 这个包其实我已经是给上传了，然后我们可以做一个下载后的解压，使用差命令杠 C 的 xe F 解压一下。好。 OK 那么现在已经是解压成功了。那么解压成功之后，我们把这个文件夹去做一个移动，然后我们直接 move elastic search 我们把它放到 user local 的下方。好，那么已经是过去了，然后进入到 local 那么 ES 文件夹这个目录整个我们就全部的移动了过来。


好，随后我们进去看一下。那么这些是 ES 中的一些目录，我们可以分别来看一下。首先是一个 bin 那么 bin 的话其实是一些可执行的文件，那么像我们要去使用 ES 的一个脚本文件，其实就是包含在这个 bin 这个目录中的。那么下面还是一个config ，那么这是它的一些配置，配置文件是包含在这个里面的。那么随后还有是一个JDK ，这可是它所依赖的一个甲板的环境。那么下一个是一个 lib 那么这是它的一个依赖的一些库，价包的一些类库都是在这个 lib 里面。那么随后是一个lox ，那么很明显这是一个预置文件，都是在这里面的。那么还有是一个modules ，那么这个是一些相应的和 ES 有关的模块，都是放在这个里面。那么随后还有是一个plugins ，这是一个插件，就说如果说你可以自定义去安装或者说是开发一些插件的话，都可以是包含在这个里面的。那么随后我们再去创建一下 mkdir 我们创建一个 data 这个目录。然后创建好了以后，那么这个 data 其实就是作为我们的一个数据目录，像我们后续会用到的一些，所以目录等等，其实数据都是会存到这个里面去的。


我们在它的配置文件里面是需要去做一个对应的相应的配置的。好随后我们进入到 config 这个文件夹之下，然后来看一下，在这里面是包含了一些相应的配置文件。那么对于我们 ES 来讲，这个 elasticsearch.yaml yml 这个文件的话就是它的一个核心配置文件，我们要去做一个对应的修改。使用 V 命令打开打开来以后，那么首先我们来往下面看，那么它的一些配置其实都是在这里面的。


首先第一个配置在这里有一个 [cluster.name](http://cluster.name/) 那么这个是什么意思啊？这个其实就是描述第一个名称 for your cluster 为你的集群去提供一个名字的。那么一般来说如果说你不配，它也是会默认的会帮你去分配的。那么在这里我们去定义一下，虽然我们是单个节点，其实我们也是可以这样子去配的。 OK 吧。那么在这边我们取一个名字，取名叫做 IMock 杠 elasticsearch 好。OK ，那么这是我们第一个名称 last IMock 好。


最后下一个。那么下一个是 node node 就是节点在集群中，它是由多个不同的节点共同的组成的。这个节点的名称我们也是可以去改一下，比方说我们改一下改成叫做 ES 杠 node 这是第 0 个，我们这样子改成第一个，这边反正这是无所谓的，然后我们保存一下，再一次的进入。那么进入以后我们再往下面看。那么下面的话找到这里有一个叫做 pass 那么这是我们的一些路径的定义。那么路径的定义的话它其实包含了两块内容，那么第一个是贝塔，第二个是罗克斯，我们应该要去配一下，所以我们把它做一个修改。


那么来看一下，这个 data 的话是第一个目录，然后去存储一些相应的数据的。然后 logs 很明显就是日志，我们先保存一下，然后我们 pwd 我们进入到上一层目录 pwd 然后的话我们是把这个直接路径拷贝一下，我们现在要配置 data 和 log 是吗，所以我们斜杠 data 拷贝一下，把这个复制好。随后我们再一次的进入到 config 修改与 SC search 这个配置文件，我们把这个 data 给改掉粘贴过来。好，随后下一个是 logs 我们也是粘贴过来。好。OK ，那么这个路径我们就已经是配置 OK 了，随后我们先保存一下，好再一次进入。那么现在我们再一次进来的话，那我们直接往下面看，往上面找到有一个叫做 network 这是和我们网络相关的吧。首先这里有一个 network.host 那么这个其实就是一个绑定绑定一个地址。那么这个的话其实它的一个道理和我们的一个 Redis 其实是一样的。那么在这里我就直接改成0.0。那么这样子就 OK 所以下面还有是一个9200，那么这是它的一个对外部署对外发布的一个端口号9200。那么等到我们启动完毕以后，那么我们是可以通过这个端口去访问去测试我们的 ES 有没有正确的安装好是可以去做测试的，当然你也可以去自定义一个端口就可以。那么在这边我们保持默认就OK 。好，然后我再保存再进来。


好再往下下面在这里有一个叫做 discover 那么其实在这里面其实就是和我们节点相关的有一个叫做克拉斯特点 initial master notes 那么其实这个就是发现咱们的一个节点，就说我们的节点刚刚其实我们有配置我们当前第一个节点对吧，我们改成 ES 杠 node 1 保存一下，再一次进入。然后我们可以去搜一下，我们看看这个有没有。 OK 吧，这是我们刚刚配置的 [node.name](http://node.name/) 它是 ES 杠 node 1，然后这个是我们现在所配的。那么这样子其实我们这一块的内容其实就配好了。好，冒号 wq 保存一下。那么这样子我们和 ES 相关的一个基本配置就已经是全部都配置 K 好，随后我们再要去修改另外一个配置。那么另外一个配置在这里叫做 jvm.options 我们来看一下。那么我们先打开，打开来以后在这里面我们找到网下面它会有一个配置，有一个 XMS 和 xmx 这两个分别都是一个 G 那么如果说是在生产的话，你选这个没有问题。那么在这里我们本身就是在虚拟机里面。那么我这个虚拟机的一个内存没有这么大，所以我们可以去做一个调整，我把它改成 128 兆。好。OK ，那么这样子就可以了。那么这是和 jbm 相关的一个基本配置。
那么随后的话其实我们是可以去做一个启动，去启动咱们的一个 ES 但是 ES 的话它有一个规定，我们目前来看一下 who MI 目前我是 root 用户，我 root 用户他是不准你去启动咱们的 ES 的，你是需要额外的去创建一个新的用户，这个新的用户才能够去使用咱们的一个 ES 这一点是需要去注意的。


那么如何去做呢？我们可以这样子，使用这个 user add 这个命令添加一个 ES user 添加一下，然后添加一下以后。那么我们现在在这个路径之下，我们返回到上一个路径。添加完一个用户以后，我们这个用户是需要为他授权的，授权是和我们的这个 ES 这个文件夹相关的，所以我们可以做一个授权 chown 杠 R 然后指定一下我们的这个 esu 的这个用户名，然后再把这个目录直接给粘贴过来回收一下。 OK 好，那么售前 OK 了。


那那么我们再来看一下的时候，其实我们在这里其实都是 ES user 了吧。好，那么这样子设置以后，我们这个新的用户其实就可以去操作咱们的 ES 就可以去到这个笔里面去执行它的一些相关的脚本了。好可怜一下。然后我们进入到 bin 这个目录，在 bin 这个目录里面其实包含了很多的内容。其中第一个就是以 ST 设置这个我们就可以直接去做一个相应的运行了。好，如何去运行呢？点穴道比拉 C search 回车。那么这个时候等待它的一个起痛，我们可以观察一下有没有报一些相应的错误。那么这个时候是抛了一些异常来看一下。


这边有一个 elastic search on court exception handle 了，在这里往下面找有一个 runtime 他在这里说 can not run elastic search as root 也就是说我们不能够使用 root 用户去运行ES ，因为我们刚刚其实创建了一个 ES user 这个用户，所以 root 这个用户我们是不能够去使用的，这也是它的规定，你使用 root 去运行肯定会报错。所以在这里我们要做一个切换，切换成我们的 ES user 切换过去。好这个时候我们点斜杠 elastic search 回车运行一下，然后他又报了一个错，我们可以往上面看。这个时候在这里面提到 access demand 就是说我们当前在运行的时候，这个权限是被拒绝了对吧。然后呢在这边他是要去访问一个 last search.queue store 啊这个东西啊访问不了，访问不到。所以在这个时候我们就应该要去再一次做一个授权。我们这样子我们切换到 root 然后 root 立马去输入一下，然后我们再退出。我们在当前的这个目录之下再去做一个授权，我们来一个杠 R 然后 ES user 冒号 ES user 随后在后面把他的这个地址给跟一下粘贴过来，再来一个回车。好。 OK 那么这个时候我们再一次的去切换到这个 ES user 好，然后我们进入到 B 目录，随后我们再来做一个运行点斜杠 elastic search 然后来一个回车。


好，这个时候我们再等待一下它的一个启动，那么这个时候它没有抛一些异常，然后我们来看一下启动的过程，稍微有一些慢，然后在这里你会发现，然后 stopping stopped clothing closed 那么这个时候说明我们现在其实启动是有问题的，虽然它没有抛异常对吧，那么在这里有三个错误，123。


那么第一个是 ES 的一个进程，就是说它能够去打开最大的文件数，这里有点过少了，然后我们应该要把它提升提升到至少65535，然后这是它的最大的一个线程数。对于我们的 ES 舞者来讲的话，这是我们刚刚新创建的一个用户，也是太少，我们也要把它做一个提升。另外我们最大的一个飞书 memory 然后也就是这个参数，这个参数的话目前是太低了，我们也要去把它做一个对应的提升，提升到最少为 262144 对吧。


那么这些其实都是和我们的一个环境配置相关的，我们去做一个环境的配置就可以了。那么首先一个我们先去配置一下，我们打开一下，打开有一个叫做 etc 下，然后有一个 CS 应该是有一个叫做 security 然后再到里面有一个限制 limits.config 那么在这个下方来看一下，里面，在这个最下方其实是有一些相应的配置的，我们在他的这里面在这个位置我们去做一个添加。


那要去添加什么内容呢？那么其实我也是为大家提供了一份文档，这份文档的话大家可以去看，在这个位置，把这几行的代码的内容其实全部都可以拷贝过来就可以了。拷贝过来之后，那么你在这边做一个粘贴贴过来，那么这些基本的配置就已经是有了。最后你可以去做一个保存，你会发现保存出问题对吧，退出一下。那么现在我这个用户是不对，那么你的一些系统的配置文件你要使用如此用户去配置的。所以重新给车陆续再次的去做一个修改， etc 下 security 然后 limits configure 找到最下方，把刚刚的内容给粘贴好保存一下。那么这是其中的一个配置，随后还有是另外一个配置，这是在 frame 下找到 etc 有一个 CS ctl 很 figure 这个文件。


那么在这个文件里面目前是为空，对吧，什么都没有，我们在它的这个最下方去做一个内容的追加这就是它的刚刚的一个报错，有一个叫做 bm.max 下划线 map 下划线 count 对吧，这个配置你要去做一个设置，它刚刚的设置是262144，262144，我们把它设置为145。然后好保存，保存之后，那么这个配置文件的话你要去做一个刷新的，使用这个杠 P 刷新一下。
好，那么现在我们这个就已经是刷新成功了，刷新成功之后，这个时候我们再一次的切换到 E SU 者之下。随后点随到与 ST search 去运行去跑一下。我们再来看一下我们这一回能不能启动成功。好，那么OK ，那么现在其实我们 ES 均是启动成功了，只不过它是在一个前台的情况之下去启动的，它并没有在后台运行。


那么在这边我们来看一下，其实它有一个 9200 这个端口，还有是 9300 这个端口。那么 9200 的话其实就是它的一个发布地址，就说有一个叫做 publish address 那么这个是对外发布的，我们是可以通过这个去访问。那么它还会有一个9300，9300的话其实是它一个内部通讯的一个端口。那么像 ES 集群，它其实内部通讯节点跟节点之间是基于TCP ，那么它是通过 9300 这个端口去做一些通讯的。那么然后我们把这个地址是可以，拷贝一下。这个就是你虚拟机的一个内网的 IP 冒号，9200直接拷贝一下。然后打开你的浏览器，在这里面做一个粘贴。


然后这个时候来看一下，这是我们当前 ES 相关的一些信息。首先看一下 name 这个 name 就是你当前这个节点的名称这个其实我们是为它进行了一个设置，当年其实是单个节点。然后整体我们的 ES 它的一个 custom name 它的名称这是我们所设置的 M 可杠 last 然后下方是它的一个版本号 number 十七点四点二，这是我们的一个 ES 的版本号，当然这里面还包含了其他的一些信息。那么然后它的一个底层其实是 losing 对吧，losing的 API 它的一个版本号是八点二点零这个版本。Ok 。


那么通过这样的一个访问，其实我们的 ES 目前我们就已经是安装好了我们就可以去玩了。然后他这边也写了一个查克赖 you know for search 你知道的我们是可以通过 ES 去做一些搜索的，然后我们再回到命令行这个目前我们是启动者，前台启动。那么如果说你要去停止，很简单， ctrl C ctrl C 一下。然后它就是 stop close close 它会做一个关闭，那么这是它的前台的方式，你也可以通过后台的方式，那么可以通过点斜杠 last search 然后来一个杠 D 回车。那么这个就是代表是通过一个后台的方式去运行。杠 D 杠 D 其实就是第一个 nice 后台的方式去运行。那么然后我们再一次的刷新咱们的页面，那么对于我们这个现在还在启动，等到启动以后，那么这个是可以去查询到的，那么现在是成功的启动了，然后过了一会儿信息我们是可以去查询到的。


然后对于我们这个如果说是在后台运行如何去关闭呢？你可以这样子，去看它的一个进程， JS 杠 F 然后 GRE P elastic search 回车，你可以去关闭，这边有很多，你也可以这样子，GPS在这里有一个 9328 对吧，那么这个你也可以去关 q9328 回车一下，然后他就可以把这个区域关掉了，你再一次通过 GPS 去看，那么是没有它的进程了，然后你可以再通过 PS 杠 F 去看的话。那么其实在这里其实它对应之前那么多信息也都没有了，那么这样子也是一种关闭的方式。好，然后我们把它再启动起来。好。Ok 。那么这样子其实我们的这个 ES 现在我们就已经是安装好了，大家就可以基于这个 ES 可以去。

