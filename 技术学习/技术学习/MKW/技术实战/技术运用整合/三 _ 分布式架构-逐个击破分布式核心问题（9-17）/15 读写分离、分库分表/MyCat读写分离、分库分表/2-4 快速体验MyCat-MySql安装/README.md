---
title: 2-4 快速体验MyCat-MySql安装
---

# 2-4 快速体验MyCat-MySql安装

[image](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/d96fdfc7-b483-4bf4-b3ba-aa2df45b79e1/SCR-20240807-qbnp.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46647WZS3XW%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T225404Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCICZX9b0hQsYf89zG6VFXGsYwzQy6nVVmS9O%2FKlhr%2BB%2BFAiAnl8QrOxuVDAUZmfZenm62liRu2pJ%2BNMM3xBXvwmjFhyqIBAjG%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMObZ99Zey4HI5dZP4KtwDE6skoA0e6Kb89b894t67tKklSIUw158pIEZDdP8HPo%2F%2FrBqlOucu5sffAT1KuHow3UCvQzphEh1IJm5ck%2FxWK2hO%2BdDIqbnTsZmQhxVjqtv8Sn1npUmgIeusyHJCJQ8ownEa6p1nuNS3rabz4XveCnC%2B371c5H3hrACZdDIjHCyMyb9mCUCGrAZ0M9BkdQcybH9vYJSyqjjWyoFNgP0aOB%2FeE5IOd%2FQHow%2FNiPtqIOphHGHWghY4XJZoICjjRKLcY2MyTv8vcX79SwwOb5HMxrL3nOY3bSZ8vyezFbF88NEsZeF9Z%2F99%2FHMHYipp5JisevpVhtTZoXnc7bPtBfC658wil5f4au4yKQC79ChnTKYYGto7zNTiEd86o4sxnzAj4CO%2BoB5HfS2JIW%2BvNn08cJ9%2BUPmjSrLSusx8dx80y1JsHNH6ep0j6TIrCdZiehl8xTjFEgb2PYIjQIOQPYFxNKgiJMntBZafipKaCauq21DuAIVdARqrA8id%2FhFxTFMbITA95KUhq3xGIs5nr5mqluqPlZSQR%2BDxFd%2B6CxLqt4C11hdIsubZqwzKgYaYtyAtTaftkZwrNx1gOjgMztsD3JoaEJUg8Xn5uhSMUte2gRWCVDBV63OZPAcHuwAw6Ln%2F0gY6pgGqC8qZ6xrezXbIOMME07VkzmPZ7RIFzdwLIJ94eYh6zTg4QQ7Jv1l3SBb7zFztVG4VIPUiURW5IiNyn5RC77bbQ82wsraUJd9cSKhcYXDOjSmxbfGW0DD6lcfyUnN1l36age3kvT6vM%2B6zUflsbh0MO1rRY%2B6rjjOTmY8uSp%2BAvR4XKCjh78%2Fwba396Gcr1aao9E8xitFPVDh5Stm5yeYXcQxxb%2F5e&X-Amz-Signature=38bdb4753b25bc210e628cad76742cd4591240f29107e234a4bdf2d3b07fa09f&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

[image](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/eca83fc8-84b3-4655-9b7e-39ae08c407b6/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46647WZS3XW%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T225404Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCICZX9b0hQsYf89zG6VFXGsYwzQy6nVVmS9O%2FKlhr%2BB%2BFAiAnl8QrOxuVDAUZmfZenm62liRu2pJ%2BNMM3xBXvwmjFhyqIBAjG%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMObZ99Zey4HI5dZP4KtwDE6skoA0e6Kb89b894t67tKklSIUw158pIEZDdP8HPo%2F%2FrBqlOucu5sffAT1KuHow3UCvQzphEh1IJm5ck%2FxWK2hO%2BdDIqbnTsZmQhxVjqtv8Sn1npUmgIeusyHJCJQ8ownEa6p1nuNS3rabz4XveCnC%2B371c5H3hrACZdDIjHCyMyb9mCUCGrAZ0M9BkdQcybH9vYJSyqjjWyoFNgP0aOB%2FeE5IOd%2FQHow%2FNiPtqIOphHGHWghY4XJZoICjjRKLcY2MyTv8vcX79SwwOb5HMxrL3nOY3bSZ8vyezFbF88NEsZeF9Z%2F99%2FHMHYipp5JisevpVhtTZoXnc7bPtBfC658wil5f4au4yKQC79ChnTKYYGto7zNTiEd86o4sxnzAj4CO%2BoB5HfS2JIW%2BvNn08cJ9%2BUPmjSrLSusx8dx80y1JsHNH6ep0j6TIrCdZiehl8xTjFEgb2PYIjQIOQPYFxNKgiJMntBZafipKaCauq21DuAIVdARqrA8id%2FhFxTFMbITA95KUhq3xGIs5nr5mqluqPlZSQR%2BDxFd%2B6CxLqt4C11hdIsubZqwzKgYaYtyAtTaftkZwrNx1gOjgMztsD3JoaEJUg8Xn5uhSMUte2gRWCVDBV63OZPAcHuwAw6Ln%2F0gY6pgGqC8qZ6xrezXbIOMME07VkzmPZ7RIFzdwLIJ94eYh6zTg4QQ7Jv1l3SBb7zFztVG4VIPUiURW5IiNyn5RC77bbQ82wsraUJd9cSKhcYXDOjSmxbfGW0DD6lcfyUnN1l36age3kvT6vM%2B6zUflsbh0MO1rRY%2B6rjjOTmY8uSp%2BAvR4XKCjh78%2Fwba396Gcr1aao9E8xitFPVDh5Stm5yeYXcQxxb%2F5e&X-Amz-Signature=f2b0eef98c744c425af597605cf9f7374efb9efb8d45e169fb8a35216c4a3f79&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

从这一节开始，咱们就来快速的体验一下 my catmy cat 它是一个中间代理模式的这么一个分库分表的中间件，所有的数据库的请作都会发到这个 my cat 上，然后 my cat 再根据你的这些操作去分配到具体的数据库当中操作相应的数据。那么在体验买 cat 之前，咱们要先把这个环境给搭建一下环境，咱们采用 vml 做虚拟机，然后咱们虚出三台机器，这三台机器都是用 Linux 操作系统，咱们采用的是汕头s7，然后采用亚木这种方式在其中的两台虚拟机上安装 MySQL 数据库。然后另外一台机器咱们安装 my cat 体验一下它的这个分库分表，它怎么去分配这些数据的。


安装完这两台MySQL ，咱们要检查一下这个 MySQL 连接的是否正确无误。以后咱们下载 my cat 这个软件包，一定要下载这个 Linux 版本的，在第三台机器上安装这个买 Kite 修改它的配置文件，配置它的分片表、分片规则，还有最基础的 date host 和 date node 这些概念，咱们在前面图文的课程当中也已经给大家做介绍，咱们就牢记这些概念，知道它到底是什么意思。然后咱们再配置的时候就能够快速的进行配置。整体的架构就是这样有两个数据库 A 数据库 B 分别在两个兄弟机上购买 cat 在第三台虚拟机上，你所有的请求都会连接到 my cat 由 my cat 去分发到不同的数据库。咱们这个环境搭好以后，你可以使用 navik 的直接连那个买 pad 和你连接数据库是一样，一会咱们也体验一下，然后怎么连接买 cat 对吧，体验一下它数据的这些增删改查好，现在咱们就启动一下虚拟机。


这个是我之前做好的三个虚拟机，咱们分别给它启动一下这个虚拟机的搭建的过程。前面老师已经给大家讲过了，咱们趁着这个机会再把这个叉 shell 打开，我这三台虚拟仪的 IP 分别是幺九二点幺幺八点七三点幺三零，131和132。然后咱们分别连接一下 130 连接上了对吧，然后再连接131，还有一个 132 是吧，这三个虚拟机咱们都已经连上了，咱们分配一下要在其中的两台安装 MySQL 然后一台安装买 cat 这档怎么分配呢？咱们暂时定一下。 130 这台机器咱们安装买 cat131 和 132 咱们安装 mysqlmysql 怎么安装？咱们直接进入到 MySQL 的官网，mysql.com是吧，下面咱们点什么？点 document 是吧文档，咱们看看它的安装的步骤。点击这个8.0，咱们要用的是 MySQL 8.0。


下面咱们再往下看看，左侧有一个 installing and upgrading MySQL 是吧，安装和更新 MySQL 那么点进去这块看看各种的安装方式是吧。在 Windows 下的，在 Mac 下，在 Linux 下的是吧，咱们点击这个 Linux 然后这块在 Linux 系统上又有不同的安装方式是吧，通过 YAML 的是吧，然后通过 Docker 的通过 apt 的咱们采用这种 YAML 的安装方式。


那么点第一个，看后面是吧，全新安装 MySQL 的步骤，咱们看到了这个是吧。第一步，安装 MySQL 的亚布仓库。亚布仓库从哪下载？这块有链接是吧？咱们打开这个链接，然后这块往下滑，有它的亚木的仓库，咱们选择的是 linux7 点击下载，然后咱们直接下载就可以了。我们看看已经下载成功了对吧，咱们打开是吧，把这个先给它复制到桌面上来。


然后咱们要把 BM 的这个仓库传到 131 和 132 上，咱们怎么传用 rz 这个命令是吧并没有找到，看来咱们这个虚拟机上并没有安装这个命令是吧，我们看一下亚默 search rz 好，那么安装一下这个名称也比较绕是吧。 lrzsz 有安装的亚默杠 Y install 然后粘贴一下。同样这个 132 这台机器，咱们也执行一下这个名字 YARN 杠 Y is 豆，然后这个名称叫什么？给它复制一下这边粘贴这个已经安装完了，然后看 132 还在下载，咱们先把这个亚墓炎给它传上来是吧，传到哪呢？传到这个 okt 这个目录下是吧，咱们先进入到 OPT 然后 rz 对吧，选择咱们这个 yam 仓库桌面，然后选择这个对吧，咱们看看已经有了是吧。然后 132 这台机器同样咱们进入到 OPT 然后选择这个亚马仓库。好，因为已经存在了是吧，咱们再看看这个文档。下载完这个样子仓库以后，要安装这个亚马仓库是吧，要安装用什么命令？咱们看一下咱们是 el 7 是吧。汕头s7。所以咱们要用这个命令那个给它复制一下，然后在这给它粘贴 version number 是吧，咱们改一下改成 3 和上面这个对应起来就行了对吧。好，执行选择 yes 没有问题，咱们在 131 上再执行一遍，选择3。在这个 131 这台机器上咱们已经安装过了是吧，咱们就不管了。然后咱们再看看这个官网后边怎么办，咱们要安装这个 MySQL 第二步，选择一个 release 的版本，咱们看看最新的 g1 的这个版本是默认选中的。如果你正要安装这个版本，你可以跳过这一步是吧。直接安装 MySQL 咱们看看。


第三步，第三步，安装 MySQL 直接亚密斯豆，咱们把这一段给它复制一下，然后在 131 上执行一下。亚米 store MySQL community server 是吧，买 SQL 的社区版本选择 yes 这个过程比较慢，总共有 400 多兆，然后在 132 上咱们也执行一下，选到 yes 下面就是这个安装的过程了。


好，经过漫长的等待，咱们这两个服务的 MySQL 都已经安装完了，大家看一下，131和 132 MySQL 都已经安装完了，咱们再看看官方的文档，看看它接下来怎么启动是吧。他们之前执行的步骤是 yami store 然后要执行 starting MySQL server 这个，咱们看看命令就是 server MySQL D star 是吧，咱们复制一下回到 131 这个服务，咱们启动一下 MySQL 没有问题是吧，咱们再把 132 给它启动一下。咱们检查一下这个 131 这台机翼的 MySQL 的进程。 MySQL 是吧，没有问题，已经启动起来了，132咱们也同样检查一下也没有问题，咱们再去官方的文档看一下。


起来以后咱们要登录是吧，登录的话要找到他的密码，咱们看一下这个密码从哪找，咱们要使用这个语句去找密码是吧，复制一下，然后回到 131 这台服务上粘贴从这个 MySQL 的 log 当中查找这个关键字临时的密码，咱们看一下可以看到临时的密码是这个咱们用 root 账户登陆一下 MySQL 杠 U root 然后杠 T 对吧，把咱们的密码粘贴一下。
好，登进来了没问题对吧，然后咱们再看看文档文档下边这一段话是让咱们修改这个临时的密码对吧，咱们修改一个比较好记的密码，改成什么呢？改成慕课，123456。好吧，就这样咱们看到他的密码是不满足这个安全策略的是吧，咱们再复制一下，中间再加一个加 1 at 。好，没有问题了是吧，咱们再刷新一下 sash religious 这个单词拼写没有问题。退车好没问题对吧，咱们再退出，然后再登录一下。 root 对吧。


杠 P 然后 in mooc 艾特 123456 没有问题，已经登录进来了。同样咱们要把这个 132 这台机器也给它改一下。同样咱们要执行抓取临时密码这个命令，找到临时密码。然后 MySQL 杠 UR OT 杠 P 然后把这个临时密码给它粘贴一下。好，进来了没问题，然后修改这个临时密码。临时密码，咱们还是用这个慕课艾特 123456 慕课艾特 123456 好，然后再刷新一下 Flash village 退出，然后再登录一下杠 P 慕课艾特 123456 好没有问题。然后咱们在每个数据库当中新创建一个账号是吧，然后咱们从 navik 进行连接创建用户，咱们用 create user 是吧，然后跟着用户名称，用户的名称咱们就叫做慕课。艾特后边跟他的可以访问的地址是吧，咱们就用百分号，所有的 IP 也都可以访问。然后 identify 是吧。


Identity fight. 后边密码这块咱们要注意一下。后边密码，咱们因为 MySQL 8，它用的是新的加密方式对吧，咱们用 vk 的连的时候是连不上的，所以这块密码咱们一定要用老的加密方式对，用这个要用 MySQL native password 对，然后拜这个什么呢？咱们也用。慕课艾特 123456 创建成功对吧，然后给这个用户进行授权。


brand o2 星点星 to 出什么？出这个 emock 艾特百分号是吧，回车，咱们再刷新一下权限。 Flash 是吧？他们 Flash 写错了好没有问题是吧桌面对吧。然后打开 navicat 咱们在这连一下，看看它能不能连这个navicat ，它使用的就是老的这种加密方式是吧，咱们给他连接一下这个应该是幺九二点幺六八点七三点幺三幺是吧主机或 IP 幺九二点幺六八点七三点幺三幺用户名以 mock 是吧，密码咱们粘贴一下，连接成功没有问题对吧，确定这样是不是就没有问题。同样咱们要在 132 这台机器上也创建一个账号，也是 create user 然后 emock 咱们和 131 创建的账号选择一样艾特百分号对吧。
Identify he bad with my circle native guard password.


拜密码还是慕课艾特 123456 好没有问题，然后给他授权 grant o2 星点星图给 emock 这个账号是吧没有问题。然后刷新一下 Flash free village 对吧？没有问题，咱们退出，然后在这个内 vk 的当中再创建一个连接，连接幺九二点幺六八点七三点幺三二是吧。用户慕课密码慕课艾特 123456 咱们连接测试一下连接报错是吧，咱们再看一下 132 那台机器连接报错 132 咱们看看 MySQL 的服务是不是正常，没有问题对吧，咱们来看一下它的端口。 grab MySQL 也没有问题对吧？ 3306 这个端口有可能是这个防火墙是吧，咱们再把这个防火墙给它关一下。 C some ctl 然后 stop 财务是吧。


D 这回咱们来试一下幺九二点幺六八点七三点幺三二是吧。用户名，慕课密码慕课艾特 123456 在连接没有问题是吧。好，到现在了，咱们两台数据库都已经搭建成功了，并且能够正确的连接。好这一小节就先给大家介绍到这下一页，咱们要下载买 cat 用买 cat 去链接这两个数据库。好，谢谢大家。


[image](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/78cbbea4-7320-4596-83f6-255a4f112068/2020-09-17_172655.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46647WZS3XW%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T225404Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCICZX9b0hQsYf89zG6VFXGsYwzQy6nVVmS9O%2FKlhr%2BB%2BFAiAnl8QrOxuVDAUZmfZenm62liRu2pJ%2BNMM3xBXvwmjFhyqIBAjG%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMObZ99Zey4HI5dZP4KtwDE6skoA0e6Kb89b894t67tKklSIUw158pIEZDdP8HPo%2F%2FrBqlOucu5sffAT1KuHow3UCvQzphEh1IJm5ck%2FxWK2hO%2BdDIqbnTsZmQhxVjqtv8Sn1npUmgIeusyHJCJQ8ownEa6p1nuNS3rabz4XveCnC%2B371c5H3hrACZdDIjHCyMyb9mCUCGrAZ0M9BkdQcybH9vYJSyqjjWyoFNgP0aOB%2FeE5IOd%2FQHow%2FNiPtqIOphHGHWghY4XJZoICjjRKLcY2MyTv8vcX79SwwOb5HMxrL3nOY3bSZ8vyezFbF88NEsZeF9Z%2F99%2FHMHYipp5JisevpVhtTZoXnc7bPtBfC658wil5f4au4yKQC79ChnTKYYGto7zNTiEd86o4sxnzAj4CO%2BoB5HfS2JIW%2BvNn08cJ9%2BUPmjSrLSusx8dx80y1JsHNH6ep0j6TIrCdZiehl8xTjFEgb2PYIjQIOQPYFxNKgiJMntBZafipKaCauq21DuAIVdARqrA8id%2FhFxTFMbITA95KUhq3xGIs5nr5mqluqPlZSQR%2BDxFd%2B6CxLqt4C11hdIsubZqwzKgYaYtyAtTaftkZwrNx1gOjgMztsD3JoaEJUg8Xn5uhSMUte2gRWCVDBV63OZPAcHuwAw6Ln%2F0gY6pgGqC8qZ6xrezXbIOMME07VkzmPZ7RIFzdwLIJ94eYh6zTg4QQ7Jv1l3SBb7zFztVG4VIPUiURW5IiNyn5RC77bbQ82wsraUJd9cSKhcYXDOjSmxbfGW0DD6lcfyUnN1l36age3kvT6vM%2B6zUflsbh0MO1rRY%2B6rjjOTmY8uSp%2BAvR4XKCjh78%2Fwba396Gcr1aao9E8xitFPVDh5Stm5yeYXcQxxb%2F5e&X-Amz-Signature=c4934eed45846d03a4e0d7626f9b218d747f46f532df776c0868b38f8fd87926&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)


