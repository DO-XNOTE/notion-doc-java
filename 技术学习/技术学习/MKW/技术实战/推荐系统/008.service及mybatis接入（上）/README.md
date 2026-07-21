---
title: 008.service及mybatis接入（上）
---

# 008.service及mybatis接入（上）

我们刚才完成了 spring boot 当中 spring MVC 搭建的一个c，也就是 control 了，我们可以通过 Web 接口去简单的访问对应的一个项目，并且得到了对应的一个 test 的一个string。接下来我们要解决 service 的一个问题，那我们刚才新建了一个 user service，那我们可以看到这个 service 在这边标注为一个class，往往在我们企业级的项目当中会使用 interface 的方式去做对应的一个service，这样做有一个什么样的好处呢？我们假设我们在这边需要有一个获取用户服务这样的一个service，那这个 service 如果是以 interface 的方式去做接口，需要通过 implement 的方式去做对应的一个实现，我们新建一个 implement 包，然后在这边新建一个 user service implement，去做对应的一个 user service 的implement。


那这样做的一个好处是说，我们只要确保对应的一个 user service 对外提供的服务的接口形式不变，那它的 implement 类可以任意的实现，有可能叫 user service implement 一，也有可能叫 user service implement 2。只要它们俩的实现同时可以实现这个 user service 的接口，那我们可以替换服务的一个实现方式，那这种样子的方式就是我们面向接口编程的一个多态加接口抽象这样的一个设计思想。因此我们在一般做项目的时候会声明一个 user service 的INTERFACE，再加上一个 user service 的 implement 的一个实现去做对应的 user service。那我们一般在这个 user service implement 当中会加入 service 注解。那这个时候同学们可能会问，为什么我加上了这个 service 注解，我们对应的一个 spring boot 就能够感知到，并且将这个作为一个 Bing 去做对应的一个 string 容器的初始化，那包含我们刚才这边有一个 user Controller 也是一样，打上对应的 Controller 标签之后它就能找到。


那是因为我们在对应的这个点评application，也就是这个没方法上面打上了这个 spring boots application 这样的一个标签，这样的一个 annotation 默认，我们可以看到对应的 spring boot application 内有一个叫 scan base package，默认是个空值，那空值的话不代表它不去 scan base package，而是它会去扫描对应这个项目包下的所有的一个类。那这样的话我们其实可以看到，虽然说我们对应的项目包下有那么多的类，但是其实并不是所有的类都被打上对应的一个标签，所以说我们一般做项目的时候会去手动指定它对应的一个 scam base package。


在这边我们可以把它打上叫 com 点 IMOOC 点点评，它是一个级联查找的动作，这样的话就会导致我们 scan base package 的路径是对应的 com 点 IMOC 点点评下面这个包，下面所有的这样的一些包结构，那当然同学们可能会问，这样的话跟我全部扫描没有任何的一个区别。


那往往在企业级的项目当中，这些项目的分层结构都是有多层的，因此我们最好是指定我们对应的一个 scam base packages。因为我们这个课程着重于在搜索推荐的相关的一个知识点的开发，因此我们对业务系统对应的一个要求就会相对来说降低。保证业务系统能够为用户提供服务，能够支撑我们对应的一个搜索推荐的一个接入接口即可。


好，那接下来我们来看一下，我们现在将对应的这个 service 层建起来之后，我们接下来需要搞定一个什么样的事情呢？那接下来我们需要将对应的一个数据库建起来。那自然我们这个项目是需要有数据库的，那我们来看一下这个项目，我们使用的一个数据库在我的本地安装了MySQL，是 5.6 的版本，并且使用了 Namicat 这样的一个工具去做了 MySQL 数据库的一个 client 端，那我们接下来新建一下对应的一个数据库，那同学们在做这个研发的时候，尽可能的跟我对应的一个服务器的环境保持一致，因为我们对应的数据库之后不光要提供给 Java 应用程序使用，还需要做对应的一个 Cano 的一个 binlog 的接入。那当然使用 MySQL 5.6 以上的版本都是 OK 的，但是不能小于 MySQL 5.6。那尽可能的，我们的同学还是基于 MySQL 5.6 跟我们一起做开发。


接下来我们来看一下我们对应的一个 MySQL 的一个安装，其实也非常的简单，我们直接到 MySQL 的官网，我们可以看到这边是官网的一个 MySQL 的 downloads 的链接，那我们在这边只需要做对应的 customer download，包括这边的一个 customer download 这样的一个点击就可以进入对应的一个 download 的界面，那我们看一下这边的DOWNLOAD，我们选择这边的一个 community Server，然后这边有对应的 MySQL community Server 5.6 版本的下载，点击进入之后下载自己需要对应的操作系统的一个 MySQL 的版本即可。


好，那我们对应的一个 navicate 的下载，直接百度找对应的一个下载资料即可。接下来就在我们这样的一个本地的一个环境下新建一个数据库，我们把它叫做点评，然后我们在这边数据库的这样的一个默认的字符集，我们在这边选择 UT F 杠8，然后这边也选择 UT F 杠8。但是这边要选择 Unicode 这样的一个排序的规则，那 UT F 杠 8 的字符集没什么好说的，我们现在大部分使用的都是 UT F 杠8，然后排序规则是它要基于 Unicode 的方式去做对应的一个排序。


好，我们选择OK，创建好这边，我们换一个名字，我们把它叫做点评 d b 保存好这边，我们在这边连接属性上面，要把对应的这个点评 d b 给它搞出来。好，然后我们可以看到我们对应的这个点评 d b 就被新建好了。新建好之后我们开始做表的创建，我们可以现了上来最简单的先使用 user 表做一个新建 user 表的动作，那我们有一个自增的 ID 作为对应的一个主键，当然这个不是绝对需要看具体的一个业务逻辑，然后非 now 不要使它是主线并且自动递增。


好，然后我们干照数据库的规范，所有的一个数据结构都需要有对应的两个字段，一个叫 created at，也就是这条记录的创建时间使用的是 data time 的数据结构，而且勾选它非null。然后我们所有的数据结构最好都有一个默认值。对于 data time 它的默认值就是 0000 零杠零0，也就是年月日时分秒都是0。然后还需要有第三个，也就是updated， at 代表的是更新的一个时间，然后也是一样默认值是这样的，我们点评的对应的一个用户，他默认是使用手机号加密码的方式做注册登录的。那我们就新建一个叫 telephone 的字段，长度我们设置为40，然后也非 null 默认值是一个空，然后我们对应有一个 pass word，我们的 password 需要加密的方式做对应的一个存储，然后我们给它字段长度稍微开的长一点 200 加密后的字符串 200 默认值是null。我们需要有对应的这个点评用户的昵称nickname，然后 nickname 我们给它也设置 40 对应的字段长度。默认值是空字符串，我们还再加一个性别 gender 可以设置为一个 int 类型，直接默认值是个0。


好，在这样的一个操作完之前，大家不要觉得这个表就算完了，我们按照业务属性来讲的话，一个用户对应的手机号是全表唯一的，这样的话才可以保证我对应用户的登录名是否可以完全代表这个用户。我们在这个索引来新建一个索引，我们把它叫做 telephone unique index，然后这个索引栏对应的这样的一个栏位是一个 telephone 这样的一个索引，对应的这样的一个字段。


索引类型，这边选择unique，唯一索引方法是 b tree， b tree 跟哈希结构我们一般都采用对应的二叉树作对应的一个 unique 的索引。我们点击对应的一个保存按钮，那在点击保存按钮之前，我们可以做一个 CQ 的预览，将对应的这个数据库的 CQ 语句拷贝下来放到我们的工程目录内，方便我们做追溯。我们可以在对应的这个 resources 目录下新建一个叫 d d l l 点 c q，这个 d d l 点 CQ 用来存放我们对应生成的所有的一个 CQ 语句，这样的话方便我们做一个数据表结构的一个代码追踪。然后我们新建的这个 table name，我们可以把它叫做user。好，然后我们点击保存，这边让我们输入user。好，然后我们可以看到对应的这个 user 表就被新建好了，它有 ID created at updated at telephone、 password 以及对应的nickname、 gender 等字段。


好，那这个数据表结构建好之后，我们接下来一步就需要使用 mybadcase 的方式接入到我们对应的这个项目当中来。那首先我们需要指定几个 my badcase，接入相关的一些霉问的价包。我们打开 home 文件，我们在之前加入了一个 spring boot start Web 项目，当中继续多引入几个价包。首先我们要需要引入MySQL，然后我们对应的 ARTIFACT ID 我们也使用 MySQL connect 杠Java，然后我们对应的这个version，大家记住，由于我们对应的 spring boot 的这个 starter 才需要能够继承住这边的一个 parent 的version。那其他的我们都需要手动指定version，不然它也下载那个2.1.6，其实它是不对的，我们对应这边的这个 MySQL 的 Java 的version，我们使用5.4.1。


接下来我们需要引入对应的一个阿里巴巴德鲁依这样的一个依赖，阿里巴巴德鲁依依赖是用来管理数据库的一个连接池的阿里巴巴，然后对应的 ARTIFACT ID，我们可以选择德鲁伊，然后对应的一个 version 1点1.3。好，我们需要真正意义上接入一些 spring boot 对应的一个mybadcase，那我们接入 spring boot 对应的 mybetis o r g mybettis 点 spring boot 好，对应的一个 artifact ID 是 my betis spring 杠 boot 杠 starter 这个，然后对应的一个版本我们在这边使用的是1.3.1。
好，完成了这样的一个操作之后，我们接下来首先将我们对应的这些价包更新过来。这边在 reload dependency。好，更新过来之后，我们现在拥有了 mybadcase 的接入的能力，那接下来我们要做的其实就是配合上 mybadcase 的一个 auto Generator，生成我们对应的 mybadcase 的一个文件，那我们在有 mybetis auto Generator 对应的一个生成器之前，我们需要将对应的 pass 等等这样的一个 XML 文件 new 出来，并且手动创建。当有了 ibadcase auto Generator 之后，我们就可以做对应的一个自动生成的一动作。


