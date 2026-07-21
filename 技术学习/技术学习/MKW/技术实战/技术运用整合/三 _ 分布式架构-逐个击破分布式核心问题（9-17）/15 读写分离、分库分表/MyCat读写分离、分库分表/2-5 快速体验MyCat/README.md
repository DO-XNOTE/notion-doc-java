---
title: 2-5 快速体验MyCat
---

# 2-5 快速体验MyCat

[image](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/cb573137-2d58-4c1b-bf43-5ba90e24d1f5/SCR-20240807-qglm.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46667VTGZ5L%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T225405Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIDcvA3CoDrnJ8ZCbuXVnKCh3g%2Fw3jR2UjOGylju0DhVmAiEAsJ9ogFwubHO42%2BI3Lo3azzpgPJ84hcn0Qn7BlkM4IakqiAQIxv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDIC6SFtZqsegURpjYCrcA%2FMq4FV0ckWVneJzRZFavKCIFYZgTPl5mVXDM92hmiwvZF0jfZJMNN%2Fi4YOiKd5nWLtojNJg10iSV9CgoTru%2BjV0SUKkg20RY3ugxOnMH%2B0x0mLJ47CRS38DkflFWSvF61PXkOBqrq%2FRIKK%2BHVvaujFYYVs%2F5SYYrfPvDwc5H%2BYAtN9f25xDNtpuif%2BJ0Fg%2FnqGQIUsCu3jrlwdzeb5wYKp4KwCkO2oMfEdqoLdptR1FZDsPzI75a9fLHenWlNu791bOT3WyJAgm2ygwv1kJ8kSbn64x8x8FiTmiZyhK8XqY%2FL6Ofh%2Fjrh3mOXVuvlgwIVymFj0dP8q8FuGLlRbcOX1UF0xXfsWR227L%2B5RzlnRkxxQhpMU1ohPYPQPx1MUK2bENkv3tZ19yDbm0ox8mwvrmGZMnBrgMCevrjwDpRdWirvZN7RjmF866MSH9kP%2BgePcOiVnk%2FJk3RopGmGZpJoMQlLL5d%2FitJLkzgAtiA%2B5RTwuDhdfCG6rXFP5q7PKp2qtylCXFL844q8aGoUqss1eUaYTA0AbEq4YBsPtWd5Upjp8Sjqt5DBxe4I6X9ntMebsg3AvU44vL36Sk9t27JOHwWjnmO4Vv4K8xhrMD560E8SCZ5%2FzyWK50UNu6MO%2B3%2F9IGOqUB0fE4wlSDHaTSfHKBBxeaIMUnTsiUWbmPzlnOadK%2FfEIO3zsQUl3EuexV5yGE4cBLOGkyDjvXxDkb3nzmjj8T078Tqg57PkDTijaZ23m29UivRv0bS2m6RwKOXx3yQycP2PJKa3dpa4aQWJ52F0mC8e45lMrc7QCr%2BDNzLv3nhBUsurkmDiMjEyt1aMVQ8hQ2%2BnAkejGD5wXwS42WI82dxzWSWDpi&X-Amz-Signature=c2a7bad8c509108ced4aa7c200b5b62a8b464ca3ec3d698b98c744f4eb48ffe9&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

[image](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/d86b01ea-161d-4057-97ae-ffb17ec896cf/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46667VTGZ5L%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T225405Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIDcvA3CoDrnJ8ZCbuXVnKCh3g%2Fw3jR2UjOGylju0DhVmAiEAsJ9ogFwubHO42%2BI3Lo3azzpgPJ84hcn0Qn7BlkM4IakqiAQIxv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDIC6SFtZqsegURpjYCrcA%2FMq4FV0ckWVneJzRZFavKCIFYZgTPl5mVXDM92hmiwvZF0jfZJMNN%2Fi4YOiKd5nWLtojNJg10iSV9CgoTru%2BjV0SUKkg20RY3ugxOnMH%2B0x0mLJ47CRS38DkflFWSvF61PXkOBqrq%2FRIKK%2BHVvaujFYYVs%2F5SYYrfPvDwc5H%2BYAtN9f25xDNtpuif%2BJ0Fg%2FnqGQIUsCu3jrlwdzeb5wYKp4KwCkO2oMfEdqoLdptR1FZDsPzI75a9fLHenWlNu791bOT3WyJAgm2ygwv1kJ8kSbn64x8x8FiTmiZyhK8XqY%2FL6Ofh%2Fjrh3mOXVuvlgwIVymFj0dP8q8FuGLlRbcOX1UF0xXfsWR227L%2B5RzlnRkxxQhpMU1ohPYPQPx1MUK2bENkv3tZ19yDbm0ox8mwvrmGZMnBrgMCevrjwDpRdWirvZN7RjmF866MSH9kP%2BgePcOiVnk%2FJk3RopGmGZpJoMQlLL5d%2FitJLkzgAtiA%2B5RTwuDhdfCG6rXFP5q7PKp2qtylCXFL844q8aGoUqss1eUaYTA0AbEq4YBsPtWd5Upjp8Sjqt5DBxe4I6X9ntMebsg3AvU44vL36Sk9t27JOHwWjnmO4Vv4K8xhrMD560E8SCZ5%2FzyWK50UNu6MO%2B3%2F9IGOqUB0fE4wlSDHaTSfHKBBxeaIMUnTsiUWbmPzlnOadK%2FfEIO3zsQUl3EuexV5yGE4cBLOGkyDjvXxDkb3nzmjj8T078Tqg57PkDTijaZ23m29UivRv0bS2m6RwKOXx3yQycP2PJKa3dpa4aQWJ52F0mC8e45lMrc7QCr%2BDNzLv3nhBUsurkmDiMjEyt1aMVQ8hQ2%2BnAkejGD5wXwS42WI82dxzWSWDpi&X-Amz-Signature=ad7c250fdd6cc880c310949efc26c7cbbb9c59e05c383019b21d4bee01f04cde&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

[image](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/e1036685-c8ff-4708-a57d-a0c377d90605/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46667VTGZ5L%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T225405Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIDcvA3CoDrnJ8ZCbuXVnKCh3g%2Fw3jR2UjOGylju0DhVmAiEAsJ9ogFwubHO42%2BI3Lo3azzpgPJ84hcn0Qn7BlkM4IakqiAQIxv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDIC6SFtZqsegURpjYCrcA%2FMq4FV0ckWVneJzRZFavKCIFYZgTPl5mVXDM92hmiwvZF0jfZJMNN%2Fi4YOiKd5nWLtojNJg10iSV9CgoTru%2BjV0SUKkg20RY3ugxOnMH%2B0x0mLJ47CRS38DkflFWSvF61PXkOBqrq%2FRIKK%2BHVvaujFYYVs%2F5SYYrfPvDwc5H%2BYAtN9f25xDNtpuif%2BJ0Fg%2FnqGQIUsCu3jrlwdzeb5wYKp4KwCkO2oMfEdqoLdptR1FZDsPzI75a9fLHenWlNu791bOT3WyJAgm2ygwv1kJ8kSbn64x8x8FiTmiZyhK8XqY%2FL6Ofh%2Fjrh3mOXVuvlgwIVymFj0dP8q8FuGLlRbcOX1UF0xXfsWR227L%2B5RzlnRkxxQhpMU1ohPYPQPx1MUK2bENkv3tZ19yDbm0ox8mwvrmGZMnBrgMCevrjwDpRdWirvZN7RjmF866MSH9kP%2BgePcOiVnk%2FJk3RopGmGZpJoMQlLL5d%2FitJLkzgAtiA%2B5RTwuDhdfCG6rXFP5q7PKp2qtylCXFL844q8aGoUqss1eUaYTA0AbEq4YBsPtWd5Upjp8Sjqt5DBxe4I6X9ntMebsg3AvU44vL36Sk9t27JOHwWjnmO4Vv4K8xhrMD560E8SCZ5%2FzyWK50UNu6MO%2B3%2F9IGOqUB0fE4wlSDHaTSfHKBBxeaIMUnTsiUWbmPzlnOadK%2FfEIO3zsQUl3EuexV5yGE4cBLOGkyDjvXxDkb3nzmjj8T078Tqg57PkDTijaZ23m29UivRv0bS2m6RwKOXx3yQycP2PJKa3dpa4aQWJ52F0mC8e45lMrc7QCr%2BDNzLv3nhBUsurkmDiMjEyt1aMVQ8hQ2%2BnAkejGD5wXwS42WI82dxzWSWDpi&X-Amz-Signature=cc1eace209fdb4bb78de770451c7f8101f2e7ff835fb1cf020d405fe5cdc95dc&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

咱们这个两个 MySQL 数据库已经搭建好了，咱们通过 navicat 也可以正常的去访问对吧，这两个 MySQL 搭建好以后，咱们就要安装 mycat mycat 怎么安装？咱们还是去官网去看一下，把这个买 cat 的压缩包先给它下，进入到 my cat 的官网 my [cat.io](http://cat.io/) 对吧，然后往下滑动，在这块下载链接，咱们下载最新的稳定的版本一点六点七三是吧，咱们点一下看到下边买开的 server 的最新的版本，咱们就下载这个点一下。


好，现在开始下载了。好，咱们看一下已经下载完了对吧，咱们把这个压缩包给它放到桌面上来，然后要把这个压缩包上传到咱们 130 的这台服务器上对吧。 OPT 下面咱们看一下当前的目录 OPT 有的同学可能比较习惯放在这个 date user 这个目录下，都没有关系，我个人比较习惯放在这个 OPT 目录下。然后咱们敲一下 rz 选择刚才那个压缩包是吧。买 cat server 好，现在已经开始上传了。好，上传完成对吧，咱们看一下，买 cat 这个压缩包已经上传过来了，然后咱们一下解压的命令卡杠 zxvf 然后买 cat 对吧。解压完成。解压完以后咱们要进入到买开的这个目录，然后修改一下它的配置文件。


配置文件咱们放在这个 CONF 下对吧，看不下很多的配置文件，咱们先快速的体验一下具体的一些配置文件，现在先不给大家做过多的介绍。首先要配置的是 server.xml 在这个文件当中要配置你的用户对吧，咱们看一下前面的这些配置，咱们先不用管，咱们直接到最后这一块配置你的用户。咱们可以看到这个配置文件当中有两个用户是吧，一个是 user 一个是 root root 是默认的账号。然后有一个密码都配在这里边。待会咱们用 navicat 连接这个，买 cat 的时候就直接用这个账号和密码去连接就可以了。咱们一会使用这个 root 对吧，他还要配置一个 schema 对应的这个数据库对吧，这个咱们起个user 。一会咱们给大家举例的时候会按照 user 去给大家演示如何去分库分表。


到这里， server.xml 就配置完了。可以看到 server.xml 里边主要是配置用户对吧，你连接的用户，包括你这个用户可以访问哪些 steamer 咱们保存一下，接下来再配置另外一个非常非常重要的这个配置文件，就是 schema 点叉 mlschema 点叉 ML 这里边都有什么东西看看有 table 配置了你这个分库分表的这些表是吧。


分片表，然后下边 data node 数据节点 data host 都是需要配置的。下面咱们就配置一下，咱们要从 it host 开始配置对吧，因为它是一层一层往下的，咱们先把最上层的这个给它配置了。 Date host. 第一个内幕属性要起一个名字是吧，这个咱们随便起一个，叫做db131，因为咱们有两个物理机，这个 data house 就是对应你的这个具体的数据库对吧，咱们看一下。 131 咱们这个 data host 对应的是 131 这台数据库，其他的配置都不用动。然后 red host 配置你的血库对吧，血库大家可以看到，可以配置多个血库，数据库 MySQL 的配置就要做成双组模式的。在咱们的这个例子当中，咱们只配置一个写库就可以了。所以下边的这个 red house ，咱们先给它删掉，给它注释掉。
然后里边 read host 大家看到读写它是怎么配置的？ read host 读库是放在这个写库里边的是吧，这个它读的时候会根据你的写库的这个配置找到你相应的读库，因为这块读库咱们也先给它注掉，咱们没有这个独库，然后上面的配置这个 host 名称咱们给它改一下，叫做m1，然后链接幺 9 二点幺六八点七三点幺三幺对吧，3306。


然后用户新建的这个用户慕课对吧，慕克索沃尔的慕克爱的123456，这样这一个 DIS host 就配置完了，咱们还有另外一个 data host 对吧，一共有两个，咱们把这个给它复制一下，然后在后边给它粘贴。这个叫做 DB 132，相应的咱们把这 URL 改一下就可以了，data host 就已经配置完了。接下来咱们要配置 data node 。数据节点咱们有两个，它这里边配置了三个对吧，那么删除一个，把最后这个给它删除掉。第一个节点咱们叫做 DN 131。第二个叫做 DNA 132，data host 配置成什么呢？和下面对应起来就可以了。咱们配置了两个是吧，一个叫 DB 131，另外一个叫 DB 132。 Database. 你对应这个数据库当中的哪一个库咱们改一下，这块咱们写错了 DB 132 对吧，它对应哪一个数据库呢？咱们随便起一个。这个 131 叫做 user 杠2131，这个对应叫 user 杠132。


好，这个 date node 也已经配置完了，date host 和 date node 配置完以后就要配置这个 schemaschema 里边配置的是一些分片表对吧，咱们先把这个给它清理一下。咱们只配置一个分片表，先体验一下 NPS 好，咱们，只留一个分片表。这个表的名字叫什么？咱们先起一个，叫做 user 然后 data note 它有几个数据节点，咱们给它配置成两个是吧，一个是 DNA 131，一个是 DN 132 它的分片规则自动沙顶。这个它到底是什么意思？一会咱们来看一下。那么好，现在这个数据库表咱们在这里边都已经配好了。然后咱们要在真实的数据库当中，把这个数据库和表给它创建一下，咱们打开这个 navigate 然后在 131 再一个新建数据库，数据库名叫做 user 杠 131 这个名称一定要和咱们配置文件里这个 database 给它对应起来是吧。 user 1314 幅级，咱们选择 UTF 8 MB 4 确定。同样 132 也需要创建一个数据库，这个数据库叫做 user 杠2132，也要和配置文件当中对应起来。


然后新建了一张表是吧，叫做 user 咱们在这个两个数据库当中分别去创建这个 user 新建表 ID 然后 int 行 11 位子增。然后再创建一个字段叫做 user name 咱们为了演示方便就只创建两个字段就可以了。然后表名叫做 user 这个表名不能随便乱起，表名一定也是和 schema 当中的这个 table 这个名称对应起来。咱们再回到那个 case 保存一下 user 131 这个库已经创建好了，然后在 132 这个库当中也创建一个 user11 位子增对吧，然后创建一个 username 保存一下，表名叫做 user 好，这两个表也已经创建好了，在这里边 schema 也已经配置好了，咱们保存一下，然后启动这个 makey 的服务。


咱们回到买 cat 的根目录，然后进目录下 my cat 启动，咱们现在先用这个 console console 是把所有的日志都打到控制台，以便咱们能看到这个买开启动的一些信息。咱们启动一下试试看到报错了是吧，咱们看一下这个到底是什么错误。


买 cat 配置的一些异常是吧，看一下以 legal 非法的表的配置 table user 弱 function 是吧，这个 user 表的分片规则是什么？是这个润之浪。然后帕提森 size 是 3 大于 table 的 data node 12 是吧。然后请确认 table 的 data node 和数据分片的这个类型是吧，咱们还是进入到这个 config 目录下看一下，先看一下 schema schema 里边咱们配置的分片规则是凹凸沙丁浪是吧，咱们去规则这个配置文件当中，咱们找到规则这个配置软件在这是吧。弱点叉 ML 咱们看一眼弱点叉 ML 规则咱们找到凹凸沙丁乐在这里边是吧，凹凸沙丁乐，然后它的这个规则的列的名字是 ID 就是咱们在数据库当中创建表时候创建的这个列的名字 ID 它会以这个 ID 去进行分片分辨，使用什么规则使用这个 run long 是吧，我们去哪找？在这个 table rule 的下面有一个function ，我这个 function 的这么一个标签，咱们找到这个润文烙是吧，在哪在这可以看到这个方式的分片的名称叫做这个。


然后它的实现类是这个凹凸帕提山摆落是吧，后边还有一个映射的文件，映射的文件是一个 tse 文件，咱们要找到这个 tse 文件，咱们看看这 tse 文件里边写的是什么，tst文件是不是在这凹凸帕提山浪是吧，咱们看一下凹凸帕提山浪这 tst 大家可以看到里边配了三个 range start 摁的是吧，看一下这注释 data note index K 是 1000m 是 1 万。咱看一下它的配置 0 到 500m 是吧，都分到数据库 0 是吧，然后 500 到 1000 分配到数据库。 1000 到 1500 分配到数据块。 2 咱们还记着之前的报的那个错的意思吗？好的，错的那个意思，他说你的这个规则是三是吧，咱们看到这块是有三个规则。


然后你的 data note 节点只有两个，那也就是说如果你的 ID 是 1000m 到 1500m 之间，那它就是没有分配的数据库了对吧？因为你的节点只有两个，但是你这一块配置了三个。所以咱们把这个 tst 文件给它改一下，给它改成两个就可以了。那我们把这个最后一个给它注掉，然后保存一下，再启动一下买 cat 又报错了是吧？也是一个配置的异常。然后 self check 自检的过程当中抛出来错。


Schema user referred by user root is not exit.
这个是什么意思？他有说到一个 user root 是吧，咱们看一下这个 server 的叉ML ，咱们的 user 都是在这个 server 的叉 mar 当中配置的。他说了一个 user root 然后 schema schema 咱们配置的是 user 咱们来看一下这个 schema 的这个配置文件。


schema 配置文件。第一行内幕，它的这个 schema 叫 test DB 是吧，但是咱们 server 里边配置的是叫 user 这个咱们也给他改一下叫做 user 保存一下，这回咱们再启动一下 makey 看看，现在又报这个 user 了，user的这个用户 schema 找不到是吧，咱们看一下这个 server.xmail 我们把这个也改一下，这个 steamer 咱们也改成 user 他就能找到是吧。保存一下，然后再启动一下 my cat 可以看到 my cat server startup successfully 是吧？已经启动成功了。然后咱们用这个 navicate 去连接一下，咱们先把这两个给它关掉，再新建一个连接幺九二点幺六八点七三点幺三零是吧，用户是 root 然后密码是123456，它的端口不是3306，它是 8066 这块咱们看一下，咱们再测试一下，连接成功没有问题对吧。


好，已经连接成功了，可以看到里边有一个 user 库，这个其实和咱们操作真实的 MySQL 是一样的，没有任何的区别是吧。然后咱们打开这个右侧表，没有内容，咱们写个 SQL 语句，插入一下 insert into user 是吧，然后两个字段 ID user name values 第一个咱们插个1，然后用户名叫做母课，咱们执行一下成功没有问题是吧，咱们再刷新一下这右侧表也没有问题。那么这一条记录它落的真实的数据库是在哪里呢？咱们这个时候再去这个 131 和132。再，咱们看一眼那个131。看到 131 里边有一条记录， ID 是一用户是慕课，再看看132。 132 没有这条记录，咱们再看一下这个分片规则。


回到这个买菜的这台服务器上，咱们复制一个会话，看一下它的这个配置，进入到来看的这个目录配置文件的目录，然后看一下这个 tst 凹凸提升老是吧，看看 0 到 500 兆都在第一个数据库 500 到 1000 兆了，是在这个另外一个数据库。一会咱们插入 ID 插入一个比较大的，咱们看看 M 是 1 万，然后这是 500 万是吧，5后边 6 个0，咱们给他这回再插入一条数据，插入一条数据 value 咱们写一个 600 万，咱们试一下，运行一下，插入成功没有问题是吧，看看在这个买 cat 是吧，咱们看一下这是 130 是吧，连接买 cat 的右侧表咱们是查了两条记录，咱们再看看 131 这个数据库，真实的这个数据库的表里边有几条记录，只有一条是吧。然后再看 132 这条数据库，咱们刷新一下。好，600万 ID 的序号分配到了 132 这个数据库，就是两个真实的数据库，一个数据库有一条记录。然后咱们在这个买 cat 130 这个里边去查询的时候，他是查询了两条数据，这个就是买 cat 的分库分表。好，这个快速体验的这一章节就到这里，咱们下一节会详细的给大家介绍买 cat 的配置，谢谢大家。



