---
title: 2-5 使用Atomikos做分布式事务
---

# 2-5 使用Atomikos做分布式事务

[image](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/1adcf390-e98d-4bc0-bf54-6599543fe933/SCR-20240808-drto.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZC2K7N7K%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T225430Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCk9MpOiYBz9xiSDoYLAmj0Gi70gF75ycr3SbqAyh3xJAIgVMULYBHSLhyXCMEZDSq8z6KmR8EAkOAXaTV%2BwF6euRkqiAQIxv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDH9Y%2FcwLkRk0VDGluSrcA1xYf5T%2BTIikXmvdR9nl90uWb9mxaSpo4DMNN%2BbPW1xUz1qk8hOBCcX51Y5c8G09PUpKe0uxqdnqZdspRberjU9h00YXa%2BDRhgTcNffbpynd5jo9zW9Cg5Wu%2BbN%2FTf%2FAPgPcRfpJ%2Fy0%2FSSzLFMrLubGDik%2BFZPyjB8bfPPyhEXbn5kwe5UIB6CMxLcbxWlEXuq4Eyl3xLGBq4II%2BDcHbT5sS1ZnPCzzLWiMVToFYF0mBPrj91vu%2BOPKu8ue54HT74GOl4Ivt7QB1DOYAToZ2%2Bsx8DosEQ%2FmXDrasW7eQQDuixK2wP%2FHSt9uE2di%2BFx51TRnHwXKvDYOdAmud2Qcs3a12Df5XKStIcQmnZzfNNcaUVCv34k1Z8xGFf8D7Lu00NN%2BKv4XBfzkLRV4huWo23h%2FF%2BeMMRLVBHgVI0FFeWApIL69pmSxDIXk85nCIrKKWvcNyaLHgt1t2qjXiDrt8zOCS9iqh5HmZjK%2B7CbOFg0dq7qE3aS3d6s8UPoC6Rf6%2BqJqWIeaRIGSEqiIuvjq2HRFJ1G1OtNnrDeE3krPDPUw1%2FLNpgL9vCwbgfC5r0qaXFR42NrvNoQmtK%2BdCp6juRjCgXwt%2FdcIuzGwahdd4RZhnDWo9729eregEYb%2FQMIu6%2F9IGOqUB2gxrfDZ4hbh0pe9TZ4h98wWO51lnCEhV4H7Aa1KeBvKyCdtaAv2drxZvO3Awjs0xYqWzUDDgZch05nmtRMf53xHfamXQqKFHSwmEEEAeITgU3zh%2BsP2JkmH7KTlsUO8xgwxBZzfoptBBrMBJsxFYoltINcXwZUu8bqw0PvJXaC%2FpmukyFVOvR1MBBEhaGo4P%2Bnkk7bLPH7qA96eUCwCSavo0YA1v&X-Amz-Signature=417d231ce34f2e265d2b1fc7565947ea29b02b7d5d9f0a8f3fd6158a3da67409&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

[image](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/1c3f9228-727a-4dfb-b859-2bca85f3fd1c/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZC2K7N7K%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T225430Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCk9MpOiYBz9xiSDoYLAmj0Gi70gF75ycr3SbqAyh3xJAIgVMULYBHSLhyXCMEZDSq8z6KmR8EAkOAXaTV%2BwF6euRkqiAQIxv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDH9Y%2FcwLkRk0VDGluSrcA1xYf5T%2BTIikXmvdR9nl90uWb9mxaSpo4DMNN%2BbPW1xUz1qk8hOBCcX51Y5c8G09PUpKe0uxqdnqZdspRberjU9h00YXa%2BDRhgTcNffbpynd5jo9zW9Cg5Wu%2BbN%2FTf%2FAPgPcRfpJ%2Fy0%2FSSzLFMrLubGDik%2BFZPyjB8bfPPyhEXbn5kwe5UIB6CMxLcbxWlEXuq4Eyl3xLGBq4II%2BDcHbT5sS1ZnPCzzLWiMVToFYF0mBPrj91vu%2BOPKu8ue54HT74GOl4Ivt7QB1DOYAToZ2%2Bsx8DosEQ%2FmXDrasW7eQQDuixK2wP%2FHSt9uE2di%2BFx51TRnHwXKvDYOdAmud2Qcs3a12Df5XKStIcQmnZzfNNcaUVCv34k1Z8xGFf8D7Lu00NN%2BKv4XBfzkLRV4huWo23h%2FF%2BeMMRLVBHgVI0FFeWApIL69pmSxDIXk85nCIrKKWvcNyaLHgt1t2qjXiDrt8zOCS9iqh5HmZjK%2B7CbOFg0dq7qE3aS3d6s8UPoC6Rf6%2BqJqWIeaRIGSEqiIuvjq2HRFJ1G1OtNnrDeE3krPDPUw1%2FLNpgL9vCwbgfC5r0qaXFR42NrvNoQmtK%2BdCp6juRjCgXwt%2FdcIuzGwahdd4RZhnDWo9729eregEYb%2FQMIu6%2F9IGOqUB2gxrfDZ4hbh0pe9TZ4h98wWO51lnCEhV4H7Aa1KeBvKyCdtaAv2drxZvO3Awjs0xYqWzUDDgZch05nmtRMf53xHfamXQqKFHSwmEEEAeITgU3zh%2BsP2JkmH7KTlsUO8xgwxBZzfoptBBrMBJsxFYoltINcXwZUu8bqw0PvJXaC%2FpmukyFVOvR1MBBEhaGo4P%2Bnkk7bLPH7qA96eUCwCSavo0YA1v&X-Amz-Signature=fdc3aee785421e11723eeeffbb5d4c7d814623a5384e9ff5d0c029605dd6550a&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

在正式的编写分布式事务的这个示例之前，咱们先看一下这个数据库，咱们打开那位 case 咱们把这个数据库给它重新的规划一下。前面的课程，咱们创建了这个沙丁 order 是吧沙丁 order 这个数据库，然后还创建了 user 131 user 132 是吧。为了和前面的这个示例咱们区分开，咱们再新创建两个数据库。然后咱们在一个事务里边分别向这两个数据库插入数据，看看它能不能保障事物的一致性。


首先咱们在 131 数据库当中创建一个新的数据库，咱们叫做 xa 131 子符集还是 UTF 8 MB 4。然后在这个 132 里边同样也新建一个数据库，叫做 xa 132 字符集 UTF 8 MB 4 对吧。然后在这两个新建的数据库当中再创建一张表是吧，表咱们只写两个字段，方便一些吧。一个是 ID 11 位是吧自增，然后再创建一个内部字段，它是 255 保存一下表的名字叫做 xa 131。接着在 132 这个数据库当中同样创建一个表，也是两个字段，id11位自增。
对吧，再创建一个内幕字段，255表示名字 xa 132 这两个表咱们就要创建好了，然后咱们要新建项目是吧，打开 idea 然后新创建一个项目，咱们还是使用 spring boot 这个项目对吧，选择 spring 初始化的这个工具版本，这一 K 的版本还是用1.8，然后点击下一步。


这里边咱们的这个 artifact 咱们给它改一下，叫做 xa 杠 demo 点击下一步。这里边常用的一些工具 long book 咱们给它选上 4 分钟 web 给他选上，要看一下 SQL 数据源是吧，数据源里边 GPA 咱们就不选了。之前咱们一直在选这个 GPA 是吧，因为这个 GPA 里边有一个数据源，但是现在这个数据源咱们要使用 atomicals 所以这个 GPA 咱们就不选了。然后咱们要选择什么？选择 MySQL 的驱动是吧。然后 mytis 的这个框架，其他的咱们看一下，其他的就没有了对吧，其他的就没有了。然后左边其他的像一些 GT A 的事物这些东西都没有。在他的这个选择的工具当中，这个后边咱们要手动的去添加，这个咱们先不管，然后点击下一步完成。
在当前的窗口打开好这个项目，就已经创建好了对吧，咱们怎么引入这 atomix 这个依赖呢？咱们看一下。打开浏览器，进入到 spring 的官网，选择项目 project 在这里面咱们选择 spring boot 因为咱们这个项目就是用 spring boot 搭建的对吧，然后选择这个文档，选择一下当前的最新的文档。在文档当中。


看一下这个目录，往下找，找到分布式事物，我们往下看。下面这一块是 circle 的数据库是吧，然后有 GPA 咱们再往下看。这个是 no circle 缓存消息对吧，看到 39 里边分布式事物是吧？使用 GTA 点进去看一下。这一段就是介绍了 GTA 的这个分布式事务包括两种是吧，一个是 atomix 另外一个是 trinix 咱们使用的是 atomics 咱们看一下 39.1 对吧。 39.1 里边就是 atomics 的事务管理器。这里边咱们可以看到 you can use 则 spring boot starter GTA atomics starter to pull 则 appropriate atomix leverage 咱们可以使用这个依赖去拉取 atomics 相应的这些夹包对吧，咱们把这段给它复制一下，粘贴到项目的 pom 文件当中，咱们在这里面再重新写一个 dependence 把前面的这个 group ID 咱们复制一下就可以了。刷新一下 Maven 这个 GTA 的 atomics 这个价包就已经引入完成了。
接下来就是咱们的项目怎么去配置？咱们还是使用 mybetis 去进行配置？之前咱们配置都是在这 application.properties 里边是吧，直接写 spring.data source.url 但是这种方式它只是配置一个数据源。咱们的项目当中有两个数据源，分别是 xa 131 和 xa 132 是吧。所以这种使用配置文件的方式不能够配置多个数据源这块，咱们要手动的去写它的这个 configuration 配置类。


首先咱们要先在这个包当中创建一个 config 目录，咱们会把两个数据源的配置都写到这个 config 目录当中。首先咱们要配置这个 131 的数据库这个类的名字咱们叫做 config DB 131 是吧。类创建好以后，类的上面要打一个注解，叫做 configuration 标志着它是一个配置类。然后第一个就要配置的是数据源对吧。 public 然后 data source 名字咱们叫做 DB 131 是吧。这个上面加上一个注解 bin 它的名字叫做 DB 131 里边咱们怎么配置？咱们要配置这个数据源。


数据源咱们要用 MySQL 的数据源是吧，但是这里边也有一个值得注意的地方，咱们要用 MySQL 的 xa 数据源，它要使用 xa 这个协议，所以这块咱们要用 MySQL xa 是吧。 xa 咱们先查一下 xa 这个数据源。 xad source 对吧，咱们先点进去，它是一个接口是吧，咱们看咱们看一下它有什么实现类这块有一个 MySQL xa data source 咱们选中这个，然后把这个复制一下粘贴到咱们的配置类当中。然后 xad source 等于 new MySQL xa 给它扫死，给它引入一下这块引入不了是吧，引入不了，让咱们添加依赖。
咱们这个 pom 文件当中已经添加了这个 MySQL 的驱动，咱们来看一下 MySQL 在这是吧添加了 MySQL 驱动。那么在这个类当中它为什么引入不了看到没有。这块有一个 scope 是吧，它的范围是 run time 那么标志它只有在运行期间有效是吧，咱们把这个给它删掉是不是就可以了删掉再回来看看能不能引入可以了是吧，可以 input class 了，这样 MySQL 的 xa 数据源就已经引入成功了是吧。


引入成功以后，咱们要给他设置用户名、密码，还有这个 URL 这块咱们先设置用户名。 Set user. user 咱们使用的是 5 克，然后密码 set passwordpassword 是慕课艾特 123456 是吧，然后再 set 这个 URL URL 是 GD DC 冒号， SQL 冒号转个后边跟他的 IP 地址幺九二点幺六八点七三点幺三幺是吧，然后端口 3306 跟他数据库的名字，咱们再回去看一下 xa 131 是吧。


xa 杠 131 这样这个数据源就配置完了，数据源配置完咱们是不是就直接返回吗？这样可以吗？这样当然是不可以的。这个数据源咱们要通过奥托 mix 统一的去管理，所以这块你直接返回 MySQL xa 的数据源是不行的，这块咱们要用 atomix atomics did source bin 是吧，咱们要选中这个创建一个 new atomics this source bin 然后把这个 x1 的数据源给他塞他进来 set xa data source 把前面这个 MySQL 的 xa data source 给它 set 进来，最后返回 atomics 这个数据源。


好，这个数据源咱们就配置好了，然后要去配置 bybettis 的这个 circle session factory 是吧，这个咱们也需要进行配置。 circle session factorybin 是吧，就是这第一个 my betis spring 这个包当中的这个类，咱们给它配置一下。然后咱们要注入这个 data source 是吧，把这个 data source 给它写进来，前面加个快递 fire 注入是吧，注入哪个 data source 呢？注入 DB 131，然后创建 SQL session factory bin 是吧。 new circle session factory bin 然后 set 它的 lead source 是吧。 lead source 咱们已经注入进来了，给它塞了进来。


另外还需要设置一个什么？设置一个 madismap location 是吧，也就是它的这个 mabetis 叉 ML 配置文件的位置对不对？这个咱们怎么去写呢？这里边需要一个参数是吧是 resource 这个咱们怎么写啊？咱们回到application.properties ，咱们在配置 my betis 的时候，在这里边咱们通常写的就是 my bettis mapper location 是吧，点进去这段配置，看看它这里边这个 map location 它是怎么去进行设置的？咱们在这进来的这个类当中搜索一下 map location 咱们看到这块是不是就是返回的 resource 的这么一个数组，只需要使用这个就可以了是吧。然后看看它的 return stream 它用了一个 stream 里边又判断了 mapper location 是否为空，然后再去用这个是吧。


最后拖睿这个 get resource 是不是就是这一段咱们用这一段就可以了是吧。有一个 resource reserve 咱们看看 resource reserve 这么一段是吧，咱们把这段给它复制一下，复制到咱们的 DB config 当中来，然后用它去 get resource 这块有两个，咱们这块一定要选择这个数组，数组这种形式。 get resources 然后里边 location 咱们配置的是 my betis 杠。咱们在这个 my betis 这个目录下，一会儿创建两个目录，一个是 DB 131，一个是 DB 132db 131 和 DB 132 这两个叉 ML 给它区分出来。所以这块咱们写 DB 131，然后星是吧点叉 ML 这块还要有一个异常，咱们把这个异常也给它往外抛一下，最后再返回这个 SQL session factory bin 这个方法上面咱们也需要打一个 bin 的注解，这个 bin 的名字咱们叫做 circle session factory bin 是吧，然后 131 给它标志一下，这样这段配置就配置好了对吧，131的把白奇斯配置已经完成，接下来咱们再配置 132 的是不是咱们直接复制一下就可以了。


复制一下，改个名字叫做 config DB 132 这里边咱们都要把 131 改成132， bin 的名字改成 132 IP 地址 132 后边的数据库，132这个数据源咱们就改好了。然后 circle session factory bin 也需要进行修改。 131 改成132，注入的数据源改成 DB 132 后边叉 ML 文件放的位置也需要改一下 DB 132 是吧。好，这两段就配置完了，然后配置 YY 意思，咱们除了要指定叉 ML 的位置，是不是还要指定这个接口的位置就是它的这个 mapper 类的位置。这个咱们直接在这个配置类当中加上一个注解。
paper scan 是吧。 paper scan 第一个要指定它的包的名字是吧，这个包的名字，咱们先把这个最基础的包给它复制一下，然后粘贴过来，这里边咱们要给它再指定一层是吧。指定一个 DAO 131 DAO 131。然后把这一段给它复制一下。


在 132 的配置列当中也要进行一下配置，它指定的是 do 132 之前咱们配置一个数据源的时候，这个 mapper scan 是不是写到了这个启动类上对吧？在启动类当中，咱们直接配置了它的这个包的名字。但是现在如果咱们配置两个数据源，你这样去配置 mapper sky 它会不会生效呢？这个时候他找到了这个 map 的类，但是它对应的数据源是谁并不知道是吧。所以这个注解当中咱们还要指令一下它的 circle session factory bin 是吧。也就是这个第一个 circle session factory ref 是吧，它指定的是哪个 circle session factory 这块咱们要配置一下实行的是谁呢？ 132 里边，那它指定的就是 circle session factory bin 132 对吧。同样在 131 里边咱们也需要进行配置 SQL session factory ref 它指定的是131，我们把这段再给它复制过来。
好，这样就没有问题了是吧，买白尼斯的配置文件就已经配置好了，到这里 my badges 的配置就告一段落了。但是咱们还要配置这个 xa 的事务管理器，这个 xa 的事务管理器只需要配置一个就可以了是吧，因为这一个事务管理器它要管不同的数据源，这个就是相当于咱们的 TM 事务管理器对不对？然后咱们刚才配置的这两个买卖意思相当于 rm 也就是资源管理器对吧。


这块咱们先配置一下，这个名字叫做 gtagta 咱们随便起一个方法名字。然后里边咱们要配置 user transaction user transaction 它里边有一个实现类，就是 user transaction imp 是吧，这个也是 atomix 这个包当中这么一个类，我们选中它这个类设置好以后还有一个类，这个大家要记一下，就是 user transaction manager 是吧，等到它然后你有一个 user transaction manager 最后咱们要返回一个 GTA 的事务管理器 new GTA transaction manager 咱们看一下，然后把前面写的这两个类给它传到构造方法当中，一个是 user transaction 另外一个是 user transaction manager 事务管理器就配置好了，前面加上一个 bin bin 的名字咱们叫做什么叫做 xa transaction 好吧，咱们就随便起一个 xa transaction 对吧。到这里边分布式的事物这一段我们就配置完了。然后咱们配置买 betis 的生成器，将数据库这两张表映射到咱们的项目当中。咱们还是打开这个项目，进入到 pom 配置文件。在这个文件里边要引入 my betis generate 的插件这块，咱们还是看一下之前的项目。


沙丁 gdbc 的这个项目，咱们把这个买白吉斯的生成器给它进来，引入到 xa 的这个实力项目当中，在考拉个印里边粘贴一下对吧，然后刷新一下还有一个配置文件生成器的配置文件是吧。在 resource 目录下 generator config 叉 L 复制一下粘贴到 xa 的这个项目当中来，也粘贴到 resource 这个目录下。下面咱们就改一下这个生成器的配置文件，将数据库的这两张表映射到咱们的项目当中。


第一个要改的 IP 131，端口3306，这个都没有问题。咱们先连接这个 131 数据库，咱们指定 xa 杠 131 用户名密码没有问题，后边生成了这个包的名字对吧，这个咱们也是，复制一下它的路径，然后在这里边粘贴一下。这里边咱们再创建一个文件夹，叫做 DB 131。把两个数据源的这些映射的配置给它区分出来。一个是 DB 131 是吧，另外一个是 DB 13。


2 这个咱们看下一个这个是叉 ML 配置文件的位置对吧，这个位置咱们也已经规划好了，叫做 DB 131 是吧，咱们看一下这个 config 类是不是就是这一段咱们一定要把这个名字给它对应起来，一定要对应起来。 DB 131 对吧，mapper的位置这块咱们也是用目录给它区分出来，这样是不是就可以了？ schema 改一下 xa 131 表的名字， xa 131 映射成的实体，咱们改成大写的 xa 131 对吧，这样是不是就都配置好了？然后咱们进入到右侧的 Maven 选择插件，然后点击这个 my vedisa 生成器对吧，我们把这个类给它生成一下，没有问题是吧。


创建成功，咱们在进入到项目当中，看到这块已经生成了一个 DB 131 的目录，里边有 xa 131 的 mapper 是吧，还有它的两个类，这个都没有问题。咱们再看一下这个 resource ，resource目录下也创建了 1 米 131 的这么一个目录，下面是它的叉 ML 配置文件，咱们再回到这个生成器的配置文件，131这个数据库咱们已经创建好了，接下来咱们再创建 132ip 首先改一下 132 对应的数据库。 xa 132 对吧，用户名密码这些都不用变。 Model. 这个类的目录给它改成了 DB 132 是吧叉 ML 配置文件 132 mapper 映射类的目录。 132 最后映射的这张表 schema 是 xa 132 表名 xa 132 映射成了十几类大写的 xa 然后 132 咱们再进入到生成器，双击一下摆拍意思的生成器，创建成功是吧。


咱们再看一下 DB 132 的目录也已经创建好了，这些都是没有问题的。接下来咱们再编写一个 service 分别往这两个数据库的两张表当中去插入一条记录，咱们再创建一层创建一个目录叫做 service 在这里边咱们再创建一个 service 类 xa service 打上一个注解 service 的注解对吧，写咱们的插入的方法。
public test xa 首先往 xa 131 这张表里边儿插入一条记录，xa 131 new xa 131 对吧，给它插入两个值，一个 set ID set ID 等于 1 内幕，咱们 set 一下 xa 131 对吧。这块咱们落了一个 word 是吧，给它补上，然后插入咱们要引入 xa 131 mapper 是吧，然后给它注入一下这块咱们用resource ，用奥特曼它会报错，还要把这个 xa 132 的 map 也给它引入一下。同样 resource 对吧，这块咱们用 xa 131 的 mapper 对吧。 xa 131。然后咱们再复制一下，往那个 xa 132 里边去插入数据，咱们统一的改一下，这样是不是就没有问题了？然后咱们要注意一点，因为咱们分别往两张表里边去进行插入数据了。
所以这个方法咱们要给他打一个 transactional 注解是吧，这个注解标志它是一个统一的事物，咱们加这个注解还是需要指令一下，指定一下传 section manager 是吧，在这传 section manager 咱们指定谁指定配置类当中配置了这个是吧。


打开 config 这个目录进入到康菲克 DB 131 是吧？咱们这个 xa 的事物是不是配置在这儿了对不对？咱们要指定 transaction manager 要指定成这个对不对？ Xa transaction. 再回到 service 在这里边，给他指定一下。
这样是不是就没有问题了？这个 service 咱们也已经写好了，然后咱们再写一个测试类进行测试对吧，在这个 test 的目录当中写一个测试方法 public void test xa 对吧，然后调用 service 当中的 test xa 这个方法。这块咱们要把这个 service 给它注入进来 xa service 对吧，打一个 o2l 这个时候用 o2l 是没有问题的是吧，因为它是 spring 的这一套东西。


刚才咱们这一块使用 resource 对吧？如果你使用 auto air 这个 idea 编译器是找不到你的 my badges 的这个 mapper 的，它总是带一个红线是吧。虽然不影响运行，不影响编译，但是这么看着就是不舒服对不对？所以这块咱们用 resource 到这个测试类当中，咱们用 auto wear 然后这个方法 xa service.test SA 对吧，然后打一个太死的注解。


现在这个测试类就已经写好了，咱们给它运行一下，看看有没有问题，报错了是吧，咱们看看报什么错没有找到 xa 131 的这个 mapper 是吧，咱们来看一下这个配置类，看一下配置类 config 里边的 config DB 131 咱们看一下 mapper scan 咱们配置的是 DAO 131 的是吧，和咱们的这个类是不一致的，对不对？咱们这块改一下，统一一下，复制一下这个 DAO 的目录，然后给它粘贴到这样是不是就可以了？同样菲克 DB 132 也需要进行修改，这块改成 DB 132 这样是不是就可以了？这个方法名咱们也改一下。
之前改漏了，咱们再运行一下这个测试程序，看看有没有问题，成功了是吧。没有问题没有报错是吧。咱们进入到这个数据库当中，刷新一下这两张表，看看数据。 xa 131 已经有数据了是吧，再看看 xc 132 也有数据，说明咱们插入的时候两张表都插入了数据，这个正常的事物是没有问题的。然后咱们要给它做一个异常的示例，看看能不能进行统一的回滚。先把这两条数据给它删除， xa 132 的删除了 xa 131 的，再给它删除。这个异常咱们怎么去做呢？咱们进入到这个 132 的这张表的配置之前咱们这个内幕配置的长度是 255 是吧，咱们现在给它改一下，给它改成 2 改成2。咱们的 132 的这条记录是不是要了？插不进去它就要进行报错。那么这两张表都要进行统一的回滚，是不是这样？ 11311 会儿是没有记录的，132也是没有记录的，这样才是正确的。


对不对？咱们再回到程序当中，再重新的运行一下这个 test xa 的程序，这回报错了是吧？咱们看一下后边看看是什么错误。数据太长是吧？ date too long for clam name name 这个列的数据太长了，咱们看一下这个数据，咱们刷新一下 xa 132 这张表里是没有数据的对吧？然后再看一下 xa 131 刷新也没有。
这个是不是就说明咱们的分布式事务配置成功了，要回滚两个数据库，咱们统一的进行了回滚，配置还是比较成功的。这个就是使用 atomics 这个分布式的数据源，去统一的管理分布式的事务。咱们再快速的回忆一下这个项目这个项目首先咱们要引入 GTA automix 的依赖， spring boot 项目当中已经提供了这个 starter 是吧，直接引入就可以了。


然后就是数据源的配置，配置了两个数据源对吧，咱们采用 configuration 这个类的注解进行配置。 DB 131 DB 132 这个配置当中，第一步要配置 xa 的数据源对吧，这个数据源咱们要统一使用 MySQL xa data sourcemysql 的 xa 数据源，配置完以后一定要记住，要把它设置到 atomix 这个数据源当中，用 atomix 数据源就要统一的管理，最后也要返回 atomix 的数据源后面的配置 circle session factory bin 这个就是 bytebetis 的配置了，不用给大家进行细讲了对吧。两个类， DB 131 和 DB 132 两个配置，类数据源和 mybetis 的配置都配置好，最后还要配置这个 GTA 的事务管理器，也就是。这一段配置咱们只配置一个就可以了，它在这里边充当 TM 的角色，也就是事务管理器的角色。然后上面这两个数据源它充当的是什么角色是 rm 的角色是吧，就是资源管理器的角色。这个就是它的统一的分布式事务的这个配置。
然后再看一下咱们的 service 层咱们的 xa service 是吧， xa service 分别引入两个 map 然后写咱们的统一的方法。这个方法一定要在方法上面打上 transaction 到注解，这个注解还要指明它的事务管理器对吧。


事务管理器一定要和咱们的配置文件当中配置了这个名字对应起来，这样是不是就配置好了，其实也没有什么太难的地方，怎么把 xc 协议的模型一定要牢牢记住，就是事务管理器和资源管理器，咱们对应的把这些配置都配置好以后，咱们的分布式事务就没有问题了。好到这里，使用 atomics 作为分布式的事务管理器，就给大家介绍完了。在咱们的课程当中，这个数据源咱们还使用了 mycat 还有沙丁类 BBC 对吧，这两个框架当中已经集成了 xa 的事物管理器是吧。如果咱们项目当中使用了买 cat 或者使用了沙金类 dpc 其实是不用你手动的引入阿汤 mix 的这些内容，咱们在下一节的内容当中再给大家做详细的介绍。好了，谢谢大家。



