---
title: 009.service及mybatis接入（下）
---

# 009.service及mybatis接入（下）

要接入 mybadcase 的一个 auto Generator，我们就需要加载 mybadcase 对应 Generator 的plugin，那我们需要在这样的 build 的一个节点上加上对应的一个 plugin 相关的一些属性。那我之前已经准备好了这样的一个 plugin 属性的节点，我们就不带着大家敲了，我们先把它 copy 过来。我们可以看一下这个 plug in 需要加载哪些事情。


首先我们需要指定对应的一个 mybadcase 的 generator 的plugin，使用的是 1.3.55 的版本。然后它需要 dependency 几个东西。第一个东西是 my Betis Generator 的一个call，对应的这样的一个Maven，以及我们现在使用的是 MySQL 5.1.4 这样的一个驱动。然后在这边引入一个 executions 对应的一个节点，这个 executions 它有一个对应的 ID 叫 mybadcase Generator，然后它的 face 是在 package 间断，需要 ghost 调用 Generator 命令生成对应的一个 XML 等等这样的一些文件的内容。
然后我们这边有几个 configuration 是 verbals 等于 true and overeyes 等于true。大家一定要小心这个 overwrite 属性，我们这边设置的是true，那就是说重复跑对应的这样的数据会覆盖掉我们之前所生成的一个文件，然后这边有一个 configuration file，也就是我们 my badcase 的一个Generator，需要读取一个 configuration file，这里边指定了我们所有的配置生成的一个规则，我们现在建在 source may resources 下面的一个 my betas generator 杠XML。那我们就来新建一下对应的这个文件，在 source may resources 目录下新建一个，买 Badcase Generator XML。然后我们将准备好的一个数据 Badcase Generator 我们把它 copy 过去。


合并过去之后，我们需要看一下。首先在这边需要指定一个数据库连接串，我们连接的是本地的MySQL，这边叫点评 d b，然后我对应的用户名是root，密码也是root。然后我们需要指定我们对应的生成 data object 类存放的位置，也就是说对应的 Java 的一个model，我们会新建在 com IMOC 点评点 model 下面，我们会新建在这个目录下面，然后在对应的这个搜索点评课程当中，由于最重要的是要学习搜索点评相关的一些技术，因此我们的业务系统的一个分层模型就使用单独的一个 model 分层，也就是说这个 model 涵盖了与数据库交互的一个 data object，并且涵盖了对应的自身的一个业务处理。也就是被 service 层引用的一个model，并且包含了最终返回给前端对象的一个 json 对象的一个model，使用了一层 model 的结构，代替了我们对应的传统意义上的三层 model 的一个分层结构。


那我们一般会使用最简洁的一个数据驱动关系 model 层的开发，完成对应的业务逻辑，直接跟着我们的思路继续看 Java model 的 Generator 就是用来将我们对应的一个数据库的 model 文件生成在哪个 Java 的一个 pass 下，然后生成映射文件的存放位置，我们在这边会在 source made resources 下面有一个叫 Mapping in 的一个文件夹，用来生成 mybettest XML 文件的位置，那我们直接可以在这个 resources 目录下新建一个Mapping。这里边会存放 XML 文件生成的一个地址。然后我们继续往下看。


有了对应的model，那还需要一个DAL，一般来叫 DAO 类，那这个 DAO 类我们就需要生成在 d AR，也就是我们刚才分好的对应的 DAL 这样的一个路径下面，然后 target project 也是 source made Java。好，那然后我们现在就要开始生成我们对应的一个表，我们刚才有一张表叫 user 表，那我们生成对应的一个 object 的name，我们把它叫做 user model。然后我们需要将这些 count by example， update by example， delete by example， by query ID example 类这些复杂的 example 查询全部都设置成false。这样的话就可以保证我们生成的类只有最基本的CRUD，也就是我们对应的 select by primary、key、insert、 update 跟 delete 四种对应的操作即可。


然后由于我们对应的一个数据库是 ID 自增长的，所以说我们在这边需要设置一个 ID 自增长对应的一个column，也就是 ID 列 my betis 对应的 auto Generator。就算是配置完了，我们首先更新一下 even 项。更新完成，然后我们在这边我们先将原本的应用停止。然后我们直接在这边新建 Maven 的一个启动，这边有个Maven。好，然后我们把它起名字为 my badcase 杠 generate writer，我们对应的这个 walking directory 没有问题。然后我们的 command line 输一下 my badcase 杠generator，执行 generate 操作。点击 apply OK。然后我们尝试着执行一下。好，我们看到由于第一次启动，它会到我们指定的 Maven 点阿里云的仓库去下载我们需要的价包，然后执行build。那我们其实可以看到它这边生成了对应的三个文件，分别是 user model Mapper XML、 user model 以及 user model Mapper 点Java，那我们来看一下生成的文件分别长什么样。


打开我们对应的source，我们首先来看一下最简单的，我们的 model 目录下已经生成了一个 user model，看到我们有对应数据库字段 ID created at， updated at。然后telephone、拉锁、nickdin， Gender 跟我们的数据库完全一一对应，然后我们在 DL 层生成了一个 user model 的Mapper，这里边它其实本质是一个interface，它有一个 delete by 主键 insert selective。那我们等会儿可以看到 insert 插入跟 insert selective 选择性插入的区别。有一个 select by primary key 组件查询。
Update by primary key, Selective Yiji update by primary key.


那我们来看一下，在这个 resources 目录下，原本的 Mapping 的空文件夹生成了一个 user model Mapper。点XML，我们可以看到这里边有我们对应的一个 user model 这样的一个 result map 的映射，并且包含了所有的一些字段，然后这边 select by primary key 就是一个 select include， include 的话其实就是 include 这句话。
这句 c q 我们可以看到这个 include 的 ID 和对应的这个 ID 是相同的，然后我们有 delete by primary key，那我们可以看到 insert 的话，就是一个所有的字段都必须为非 null 的情况去做对应的一个insert，也就是说它不管 Java 对象对应的这个 property 是否是个null，它都去做对应的这个 insert 的操作。


那 insert selective 其实就是 insert 操作，可以去判断若对象的属性部位 null 的时候才去拼接对应的这个字符串。否则的话就用数据库默认值。那我们由于数据库内全部都设置了非null，所以说我们大部分情况都会使用这个 insert selective，对应的这个 update 操作也是一样。


update selective 也是指定非 now 的字段才会做update，对应的 update by primary key 就是无脑做对应的 update 好数据库对应的这个 Mapper 文件，那就算生成完了，那接下来我们要做的就是集成 mybadcase 对应的这个数据。那首先我们需要改变一些东西。我们需要改变一下我们对应的 application 点properties，那我们在这个 application 点 properties 当中需要指定哪些东西呢？我们由于刚才指定了对应的一个 my bettest mapping，地址是在这个路径下。但是这个路径其实是指定给我们对应的 mybadcase auto Generator 的插件去看的，我们还需要告诉我对应的 spring boot 到这个 Mapping 的路径下去寻找对应的这个 XML 文件单，因此我们需要加入一个 mybadcase mapper locations，等于 class pass，这个 class pass 就是指定到对应的这个 resources 目录下。那 class pass 下面有一个mapping。然后我们要它的新点XML，就是它所有的点 XML 结尾的文件都可以用来加载，那我们可以看到 class pass 其实是指定到这个 resources 目录下。


然后我们需要指定对应的数据库的一个数据源， spring boot 默认使用 spring data source 点 name 的方式指定数据源。那我们这个数据源把它叫做点评DB，然后我们对应的这个 data source 的 UIR 我们使用的是j、d、b、c，那我们可以把 mybadcase Generator 上的一个给它拷过来。我们对应的这个数据源是这样的一个地址。
j、d、b、c，然后我们后面需要多加几个东西，首先我们需要使用 Unicode 的方式做对应的一个连接，并且它对应的 character encoding 使用的是 UT F 杠8，因为我们对应的一个数据库的一个字符串用的是 UT F 杠8。好，然后我们需要设置对应的 data source 点 username 是一个root，然后我们对应的一个 password 也是一个root。


我们需要指定使用德鲁伊做数据源，我们其实可以看到它的思路是说我们首先配置 Mapper 文件要加载的地址，然后这边写一下配置数据库连接等数据源，然后我们需要使用德鲁伊做 data source，也就是做连接池的管理 data source，这个 data source 使用德鲁仪做连接池管理。 data source 点type，我们指定的是 com 点阿里巴巴，点德鲁伊，这边已经帮我们自动带出来了，也就是我们使用德鲁伊的 data source 做连接池的管理，然后我们指定对应的一个 driver class name 等于一个com，点MySQL，点j，d，b，c，点driver。完成了这些操作之后，我们就完成了对应的一些数据库的相关的一个 data source 的一个配置。然后我们接下来要做的其实就是将我们对应的这些内容串起来。那我们首先需要在我们对应的这个 spring boot application 下面，我们需要指定另外一个注解叫 Mapper scan，也就是我的 Mapper 文件。我们在 property 文件内指定了 XML 文件的路径，那接下来我们需要在 Java 类当中使用对应的 Mac of scan 指定 Java 的一个路径。那我们 Java 类的路径就在我们这个 DAL 层，那我们把它写一下 IMOC 点点评点 EAL 好。


完成了对应的这个操作之后，我们需要将流程串接一把，我们首先在我们对应的这个 user service 当中，我们开一个方法叫 user model，它是一个 get user 的操作，传入一个 ID 这样的一个组件。然后我们在这边 user service implement 当中去实现对应的一个方法，在这边我们需要通过 autowild 引入我们对应的一个 user model Mapper，然后我们直接 return 出一个 user model Mapper select by primary key，也就是说我们对应的这个 service 其实非常的简单，非常的薄。就是根据主键获取一个用户 ID 的一个用户模型，返回给上游调用它的地方。那我们上游调用它的地方就在 user Controller 上，那我们可以直接在这边新开一个 request mapping，那我们直接可以使用 request mapping，我们把它叫做get。它返回一个 responsively 这个 responsibody 我们目前暂时使用 user model 叫 get user request a param 接收一个 get 请求， ID 为 name 等于ID。然后它是一个 intrigger 赋给这个 ID 对象，然后我们直接返回一个，我们在这边autowild，然后引入 user service，然后我们直接使用 user service，点 get user 对应的一个操作，将把这个 ID 传入返回即可。


好，那我们接下来开始启动一下我们对应的应用，我们使用 debug 的方式启动。我们可以看到 spring boot 成功启动在了 8010 端口，那我们首先访问一下刚才的测试类，好， test 访问成功了，那我们接下来换一个链接，我们叫get，然后访问 ID 等于一，我们可以看到什么内容都没有输出，然后我们看一下控制台有没有抛出异常，也是正常的，那因为我们对应数据库里压根没有对应的这个 ID 这个字段，因此自然而然返回出去的就是个null，什么都没有。


那我们现在来尝试着往这边加一个数据，那我们可以在这边直接手动插入的方式新增一个数据。我可以设置 2019 年零七杠，零七它是 10 点整创建的，然后 updated at 也是 10 点整，那我们可以设置个手机号 1312345678 password，我们先用铭文的方式存储123456，那 nickname 我们可以把它叫做 Jack Gender， 1 代表男， 2 代表女。


OK，点击勾，那我们可以看到对应的这条数据就进去了，它有一个自增的 ID 1，并且有相应的一些数据。然后我们再次访问一下，我们可以看到对应的这条数据就出来了，它有一个ID，然后对应一个 created update，完全跟我们数据库的结构是一一映射的，那完成到这一步就说明我们将数据给它做完了 my Betas 对应的一个接入。

