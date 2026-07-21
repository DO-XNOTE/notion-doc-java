---
title: 2-8 事务补偿机制程序示例
---

# 2-8 事务补偿机制程序示例

[image](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/556aa4c6-02d6-4553-93c1-23f636ea48e7/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XCZH563D%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T225432Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCnTGVdWNq09jtHNQh3XGE47AbcpHBOdOSNx4Z3%2BNP6gQIgOElrosc6d9bM6pZF05tfvDe0wPJqs1is9MUfDbbt2UgqiAQIxv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDOeA4YX3DLyPesNtkCrcA3TQet9cNyB37Bpk%2BJXESdcPrWL2UkClJkccaqVMUHTLBvF8aQtQVZXhzjxb0WX8UTXSOkA7caLi6qenREiiq1m5YU91wBrAS4kVDE6YyXUS92Dfzb9jMUo2zt%2FF3xzV%2BWry7U3XgBnLbBUfMoICSkSAoMChFtJfreCyIOsdwNwJuORCLMzRCw%2Bq5wNwWSYTlcyVKzjt9nVYlsRgwSvbD7fdBZDRj%2B2UaEav92DGgFA6M3Ew4HSI85KyZgty7agJoMHv4VeRGUi2oDHELCWTpvis5%2BUjnWRd9vvsrRzLYF2kaNc7g2BtaqPU5c6JphmjO%2F3pyyR4w%2FS57FuHsHsxBFhLmG7RSRH7DfMglQFQBiIiY4Q0KKp5KWCev55IDbPI0mQFEI2WYv2GPbP7OsUTOhWXeg8pJoDKA0EQFBIfdFYgB5UTj%2F09azkRNQ5wnPKWX0nZNE8lVArmYgx%2BdfgTXzkWU9NNQOFKuAkf69dpbcpb5dUH6EAAUMgAQPC5E9Nr8iIlBrA4z7N2mWsYsB2Lp0ehXZ3TsQOQZ0FSZqLkDagBTbqelgxWQ%2BuLMsk3hy8dclZPzoel4Nl6rlE4DSKfaB2yMyABq%2BJ1WmMFUVG%2FPijtvcBE7SyHZ2YacFA%2BMOG3%2F9IGOqUBNiGhxTqOAXJOjnaAPBhvyMZmGradpRmYVYoMgf0GVOJDGxeo2gEo%2FBvzz746Blb5HgHKlE9e2HAmq1oILEpWQrSCQGYaNZ%2B1zn%2BSHzTiCcCY6CvGrkYm05xdGDy0lXP2Q0fUw7oaL7rn9jmKCqKbb1mL9N1ZI2OZf64y0DJhD3GZGystT5jw606j3Cocntw%2FjgCCwbKW4xgc%2F%2FjJqsc9QSwAaJ5y&X-Amz-Signature=4559da5105726840d972354c72a8aec082ba9028f83bcf91223993d598eb5c82&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

[image](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/5626100d-b42d-430a-8351-6d30a6ba299b/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XCZH563D%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T225432Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCnTGVdWNq09jtHNQh3XGE47AbcpHBOdOSNx4Z3%2BNP6gQIgOElrosc6d9bM6pZF05tfvDe0wPJqs1is9MUfDbbt2UgqiAQIxv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDOeA4YX3DLyPesNtkCrcA3TQet9cNyB37Bpk%2BJXESdcPrWL2UkClJkccaqVMUHTLBvF8aQtQVZXhzjxb0WX8UTXSOkA7caLi6qenREiiq1m5YU91wBrAS4kVDE6YyXUS92Dfzb9jMUo2zt%2FF3xzV%2BWry7U3XgBnLbBUfMoICSkSAoMChFtJfreCyIOsdwNwJuORCLMzRCw%2Bq5wNwWSYTlcyVKzjt9nVYlsRgwSvbD7fdBZDRj%2B2UaEav92DGgFA6M3Ew4HSI85KyZgty7agJoMHv4VeRGUi2oDHELCWTpvis5%2BUjnWRd9vvsrRzLYF2kaNc7g2BtaqPU5c6JphmjO%2F3pyyR4w%2FS57FuHsHsxBFhLmG7RSRH7DfMglQFQBiIiY4Q0KKp5KWCev55IDbPI0mQFEI2WYv2GPbP7OsUTOhWXeg8pJoDKA0EQFBIfdFYgB5UTj%2F09azkRNQ5wnPKWX0nZNE8lVArmYgx%2BdfgTXzkWU9NNQOFKuAkf69dpbcpb5dUH6EAAUMgAQPC5E9Nr8iIlBrA4z7N2mWsYsB2Lp0ehXZ3TsQOQZ0FSZqLkDagBTbqelgxWQ%2BuLMsk3hy8dclZPzoel4Nl6rlE4DSKfaB2yMyABq%2BJ1WmMFUVG%2FPijtvcBE7SyHZ2YacFA%2BMOG3%2F9IGOqUBNiGhxTqOAXJOjnaAPBhvyMZmGradpRmYVYoMgf0GVOJDGxeo2gEo%2FBvzz746Blb5HgHKlE9e2HAmq1oILEpWQrSCQGYaNZ%2B1zn%2BSHzTiCcCY6CvGrkYm05xdGDy0lXP2Q0fUw7oaL7rn9jmKCqKbb1mL9N1ZI2OZf64y0DJhD3GZGystT5jw606j3Cocntw%2FjgCCwbKW4xgc%2F%2FjJqsc9QSwAaJ5y&X-Amz-Signature=e816a00f2636828721aa3f3a334e9d4ebdacbba25b8c9e5054c03218b8b8fa59&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

还是先来规划一下数据库。咱们打开这个内威 cat 之前，咱们在做这个 xa 的这个实例的时候，新建了两波数据库，应该是 xa 131 和 xa 132，咱们就复用这两个数据库就可以了，不需要再新建其他的数据库了。咱们这个 xa 131 当中新创建一张表，这张表是用户 A 的这个账户，咱们也是写几个关键的字段就可以了。首先是 ID 长度 11 位子增的主见，然后再添加一个 name 姓名是非空，随后再添加一个余额字段 balance 余额看咱们要用 decimal 这个类型 10 位，然后两位小数我们先创建这么一张表，看叫做 account A 这个用户的账户。然后同样的这张表咱们要给它在 132 的数据库当中也创建一个，咱们直接复制，把 count A 给它复制过来，开始复制完了刷新一下，然后把这个表名给它改一下，改 account B 然后咱们分别在这个 account A 和 account B 当中创建一条记录。


这个咱们写 ID 等于 1 姓名，咱们给他叫做什么呢？叫做用户 A 余额，咱们给他写一个1000。一会儿用户 A 给用户 B 要转账 200 元保存一下，然后再打开 account B B ID 12 咱们写个用户 B 它的余额也是 1000 元。一会儿咱们从 A 转账二百转到 B 这个账户当中。那么 B 的账户余额就变成了1200， A 的账户余额变成了800。这个数据库咱们就规划好了，然后创建一个新的项目，打开 idea 然后创建一个 spring boot 的项目。这个名字咱们叫做 tcctcc demo 事务补偿机制的这么一个实例，还是选中常用的这个几个依赖 circle 里面 jpa 然后 MySQL 的驱动 badges 完成好，这个项目给咱们生成好了。


然后咱们要配置一下这个配置，咱们配置很多次了，这个就不给大家做具体的演示了，咱们快速的配一下。由于咱们使用的是两个数据源，所以使用 fdk 3 点 props 是没法配置两个数据源的，咱们要手动的去进行配置，和上一节配置 xa 的这个数据源是一样的。咱们新创建一个 config 目录，然后创建一个 config DB 131 它是一个配置类，所以要打一个注解。 configuration 里边首先要配置的是数据源。 public in the south DB 131 里边配置 MySQL 的 data sauce。 Mysql data sauce. 这块还是，引入不了。咱们上一节课已经找到了他的问题，这个 MySQL 的驱动它的范围是运行期是吧，我们把这个 run time 给它删掉 NP 我刷新一下妹妹这块是不是就可以找到了，咱们试一下。


my circle did sauce it sauce 等于 new 然后 my circle did the sauce 别人上次 set user 咱们的 user 是慕课，然后再 set password password 是慕课艾特123456，最后再 set 一下 uil URL gdbc 冒号 MySQL 冒号杠杠，然后幺九二点幺六八点二七三点幺三幺端口 3306 后边跟数据库。数据库咱们看一下，数据库咱们还是用的 xa 131，咱们直接给他写上 xa 杠131，这样是不是就没有问题了。然后再把这个 date source 给它返回方法上加一个 bin 的注解，拼的名字叫做 DB 131 好，数据源配置完成，然后配置 mybatis 的 circle session factory SQL session factory bin 就是这个咱们也是快速的配置一下 factory bin 然后给他 new 一个设置他的 date source 这个 sauce 咱们这块儿土肉加一个快递 fire 注入哪个 this source 呢？就是前面创建的这个 bin DB 131，然后 set this sauce 把这个 data sauce 给它 set 进来。


还有一个就是咱们的 mapper location labor location 咱们也要给它指定一下，咱们统一放在了 resource 目录下的 my badge 这个目录下这块咱们怎么去配置还是找一下。去 application 加 properties 里边写一下 appetis mapper location 找到它的源码，搜索一下 mapper location 看到这一段咱们看看它是怎么定义的，把这一段复制一下，粘贴到咱们的项目当中。然后这个 mapper location 就是 resource reserve.get resources 然后里边跟咱们的路径来 betis 然后新人点 XML 这块有异常，咱们要给他画出就 OK 了。


最后把这个 factory bin 给它 return 一下，方法上加个 bin 的注解，这个三个 factory 叫做 factory bin 131 这样是不是这个数据源就配置完成了？然后这个配置类上还要再加一个注解 wiper sky 这个指定的是买白金丝接口的这个路径，这个接口的路径咱们先不指定，等一会把这个映射生成完成以后，咱们再指定这个麦克斯干 DB 131。那么咱们就写到这儿，这算告一段落，然后再复制一下再去配置 DB nose R EB 132，统一的进行一下修改。 131 咱们都给它改成132， IP 改成132，数据库也要改成2132， factory bin 也统一改成 132 这块买 badges 这个 Apple location 咱们也是要用这个目录给它区分一下 EB 132，再回到 131 的这个 config 这块，也是需要进行区分，这个是131，这样是不是就没有问题了，配置完成了。


然后咱们把这个买卖意思的生成器引入到咱们的项目当中，还是看一下之前的项目，把 Betty 的生成器拧过来粘贴一下，还有一个配置文件，在 resource 目录下复制一下粘贴过来。然后咱们把这个两张 account 表给它映射过来。首先改一下这个 gdbc connection 第一个连接 131 端口 3306 用户名，慕课密码，顾客艾特 123456 包名，咱们要统一的改一下，复制一下这个咱们的项目当中的这个包名，统一修改这个买卖。


第四，这块咱们要改一下了，要改成 DB 131，eo我们也需要改一改这块咱们是不是都要统一的加个 DB 131 把目录给它区分出来， DB 131 这样是不是就可以了，都区分出来了是吧。好，最后咱们把这个表给它生成一下这个 schema 咱没有改，这个 schema 是 xa 131 xa 131 表名咱们看一下。那是 account A 粘贴过来映射的实体类，咱们统一给它改成大写。看了 A 然后咱们找到迈文的这个插件，买贝利斯的升值器的插件生成一下没有问题，咱们看一下项目当中的目录， DB 幺三幺一个 DAO 一个 mod 然后买 vs 叉 ML 的目录，买 vs.db 131 这个也没有问题，咱们再修改再生成一下 xa 132 的配张表。


132， xa 132 后边都统一改成 DB 132 映射的表，这个是 account B 那么统一进行一下修改，然后再生成一下。好也没有问题是咱们再回到项目当中去看一下 DB 131， DB 132 都已经生成了，没有问题。最后咱们再去这个两个数据源的配置类当中，把这个 map scan 给它改一下。 DB 131 扫描的是 DB 131 的 do 咱们复制一下这个包名粘贴到这里边来，然后还需要指定一下它的 session factory sophosession factory reef 它指定的是什么？就是咱们下面配置的这个 factory bin 131。同样 DB 132 咱们也需要改一下，我们直接把这一段给它复制过来。扫描的是 DB 132 的 do 然后 factory B 改成132。好到这里，买 veggies 的配置就都已经配置完成了。
然后咱们写一个 service 这个 service 要进行转账，新建一个 service 的目录，创建一个 account service 这么一个服务打上一个注解。 service 里边咱们要把 DB 131 和 DB 132 的这个 map 给它引入一下 account a member 这个 resource 注解，然后再写一个 count B map 也加一个 resource 注解，然后咱们就要写这个转账的方法了 public word 然后 transfer transfer account 转账


然后这里边第一步先要查询出用户 A 的这个账户，咱们用 account mapper 然后点 select 咱们看一下这个 key 这个 key 应该是 1 咱们把这个用户 A 的这条记录先给它检索出来签课书这一条记录。然后把它的金额给它减 200 减 200 咱们应该是 set balance 等于 account.get balance 然后 subtract new 一个 decimal 200，这样 A 账户的余额就减掉了200。然后咱们要更新一下这条记录。
Update by primary key account a.


这样 A 的账户就减掉了 200 元，同样要在 B 上面给他加 200 元。 account B 它的 ID 是2。同样的操作， account b.set balance 等于 account B 加 get balance 然后 add 你有一个 decimal 200，给它加上200。然后再更新一下 account B 是吧，他们两个应该是在同一个事物当中，但是咱们的数据源直接使用的是普通的数据源，并没有使用 xa 的这种数据源，所以它这两个库的事物应该是不一致的，没法保证两个数据库的事物的一致性。咱们先试一下，这个方法上咱们也打一个 transaction 后，正常的情况下应该是 A 减200， B 加 200 没有问题。但是如果出现错误怎么办？咱们在这里边先模拟一下，如果在更新账户 A 的时候出现错误了，看看账户 A 会不会回滚。这块咱们直接写一个， int I 等于 1 除以0，这样是不是就报错了？抛出了一个异常了，咱们要看一下这个 A 看一下这个 A 账户操作会不会进行回滚。


这个方法，咱们就先写成这样。然后写一个测试程序，调用一下进入到 test 这个目录，咱们写一个测试类 test account 然后把之前的 service 给它注入进来。 account service check out where account service 点儿 transfer account 再加一个 test 这样这个测试类咱们就写完了。然后运行一下，运行的时候执行到这是不是就报错了？ account B 的这个操作是不会执行的，咱们先要看一下这个 account A 这个用户之前的这一段操作会不会进行回滚，我们先试一下运行报错了是吧，报出的就是这个逻辑错误不能除以0，咱们再回到这个数据库当中。这个是用户 A 的表是吧，之前都是1000，用户 B 也是1000。咱们刷新一下这个用户 A 的这条记录，看看他的钱有没有少变成了800，也就是说这块出现错误，他并没有进行回滚。


咱们再看一下这个日志，看一下这个逻辑的错误，它是什么样的异常。咱们先搜寻一下它是一个 runtime exception spring 它的这个事物它默认就是捕获 runtime exception 然后进行事务的回滚。但是由于现在是多数据源，所以第一个这个事物他也没有进行回滚。这块的这个事务管理器咱们也手动的去配置一下。


这个两个数据源咱们要配置两个事务管理器，然后这块 transaction 弄到注解当中，咱们就可以指定这个事物管理器了，就是这个 transaction manager 那么分别在这两个配置类当中，配置一下这个事务管理器，咱们统一使用这个 spring 为大家提供的，它的名字叫做 platform transaction manager 就是这个咱们统一使用这个事务管理器里边咱们直接 return 一个就可以了。 return new data source transaction manager 然后把这个数据源咱们要给它注入进来，这个数据源咱们还是参照之前的 session factory 咱们给它写到这个方法上，然后把这个 data source set 一下，这样是不是就配置完成了，然后加上一个 bin 他的名字叫做 TM 131，加个引号。
好，这个 131 就配置完成了，咱们给它复制一下，粘贴到 DB 132 的这个配置类当中，名字 TM 132 数据源也改成 DB 132。然后在这里边咱们是不是要可以指定它的事物管理器了，咱们先指定一个 TM 131，这样是不是这个事物管理器咱们就指定了 DB 131 的事务管理器了。这下咱们再运行一下，看看 account A 是不是会回滚，那么还是把这个数据给它恢复一下，这个数据咱们还给它恢复成 1000 保存一下。下面咱们再去执行一下这个测试程序， A 的这条记录会不会进行回滚好还是报道这个错。


By zero. 然后咱们还再回到数据库当中刷新一下，大家看看 A 是不是并没有扣减那个二百他的事物进行了回滚了，咱们还是回到这个程序当中如果我在执行 B 之后再抛出这个异常会是什么样子？抛出异常，由于咱们的事务管理器设置的是 TM 131，那么 131 会进行事务的回滚，也就是 A 账户这 200 块钱不会扣减。


那么 B B 账户这个二百块钱会不会加上呢？由于咱们这个 15 关系没有配置 132 是吧，所以这个 B 账户会加上这个二百块钱，咱们试一下看看是不是这种结果，再运行一下这个测试程序还是这个错误。然后咱们再回到数据库当中，咱们看一下 a A 账户刷新还是 1000 元钱，并没有扣减，再回到 B 账户，咱们刷新一下，这个钱变成了1200。所以这个事物并没有保持一致，咱们还是先给它改回来，改回到1000，再回到冲击当中。有的同学可能会说了，你这块事务配置了一个 131 的数据库，但能不能再配置一个 132 的呢？我配置两个事务管理器，是不是就能够保证它统一了呢？这个是不可以的，咱们试一下。首先咱们看看能不能配置两个 transaction 能的注解不可以，你配置两个注解它会报错了，我们，改一下也是会报错的，这种方式是不可以的，咱们还是给它删除掉？咱们用逗号隔开 TM 132 这样可不可以，咱们也再重新试一下，钱咱们都刚才已经给还原回去了，咱们再重新运行一下。报错了是吧，咱们看看报的什么错。没有这个名称，它是根据你的这个名称去找你的事务管理器，没有这个名称，看来这样配置也是不行的。所以这块一个方法咱们只能指定一个事物管理器，咱们就看你要指定哪一个事物管理器了，你指定一个事物管理器，只能保障一个数据库的事物，另外一个是保证不了的，就像现在这样，你保证不了 DB 132 的这个事物。


所以这块你要提供一个事物的补偿机制，这个事物补偿机制怎么去提供呢？这块有异常了，那咱们就统一的去加一个 try catch 把这一段给它放到里边来，然后 cash 住异常，如果出现异常，咱们要进行事物的补偿。怎么补偿？因为你之前是加了二百，所以这块咱们要进行减二百的操作。


减 200 这块咱们要 subject 这样是不是就没有问题了？之前你加了二百，我开始入异常，因为你这个 1 除以 0 报错了，所以我这块要进行减二百的操作，把之前加的这二百给它再减回去，这样是不是就可以了？这块还有很多的细节，因为你的错误是在这儿爆出的，所以我减二百是没有问题的。


但是如果你的错误是在这一块爆出了，在这个 update 的语句之前，你就已经抛出了这个错误。那我 cash 住是不是也会有问题啊？你在 update 之前抛出错误， D 账户并没有多加二百块钱，并没有多加二百块钱。你 catch 住了这个错误，你又把 B 账户给减了二百，是不是就等于多扣个 b200 块钱了？所以这块还是有很多的细节去需要处理的，包括你 catch 的这个异常，最好是自定义你的异常，什么情况下抛出什么异常？我 get 住哪一种异常，我才进行这个事物的补偿。


这块咱们并没有给大家做详细的演示，其实咱们可以把这一段给它放到这个踹外边来，这样是不是就行了？你在 update 之前如果你有错误的话，我就直接抛出异常了，抛出异常，然后 DB 131 的事物进行回滚。 DB 132 你也没有进行 update 的语句，如果没有异常直接执行 132 的数据库也已经更新了，然后执行 1 除以0。


这个操作有异常了，咱们开始住，然后把 B 锦翔回滚这块咱们给他改一下。看看改成小B ，我给他改成小 B 这样是不是就可以了？就是这个异常咱们做了补偿的一个操作，咱们最后是不是还要再把这个异常给它抛出。如果你不抛出的话，那么 catch 住以后，这个方法就正常的结束了，正常的结束。你的这个方法并没有异常，没有异常。那你看到 A 这个用户是不是事物要提交了，并没有回滚。所以这块咱们还要把这个异常给它抛出来。


抛出来以后这块咱们还是要改一下 rollback rollback for 它默认的是 runtime exception 咱们抛出的是整个的这个 exception 异常这块，所以咱们要加一个 exception.class 这样再试一下，看看这个 A 账户和 B 账户的这个金额是不是平的，咱们还是回到数据库检查一下。现在用户 b1000 元没有问题，用户 A 也是 1000 元也没有问题。咱们再运行一下这个测试程序破错还是 by zero 然后咱们再回到数据库看一下用户 A 它的余额刷新一下 1000 没有问题。再看看用户 B 咱们刷新一下也是 1000 也没有问题。


看来咱们的这个事物补偿机制是没有问题的。这个事物补偿机制，所有的逻辑都在这个应用层。所以对于程序员来说，他要非常熟悉这个事物补偿机制的这段逻辑，把这个逻辑搞清楚，才能把事务补偿机制给他写好，对程序员的压力是比较大的。而且咱们这个势力当中，只是写了两个数据源的这种事务补偿，如果你有多个数据源，那么你补偿起来可能会更加的麻烦。尤其是你的这个补偿机制在什么时间点去调用是非常的有学问的。咱们可以看一下。就咱们的例子当中，如果你在补偿的时候再出现了错误，那是不是也是有问题。这块其实咱们可以在这一段当中再去进行 try catch 再 catch 它的异常如果没有异常，那么就正常的结束，一点问题都没有。如果有异常了怎么办？如果有异常，咱们再去循环掉这一段，再去进行重试。如果重试的次数超过了它的最大的次数，比如咱们允许他重试三次，超过了三次，咱们就要把这个异常给它记录下来。


然后咱们就要进行人工的介入了，所以这段逻辑是非常的复杂的，对于程序员来说要求也是比较高，所以在咱们的项目当中是不推荐使用这个事物补偿机制的。到这里了，这一节的课程就给大家介绍完了，谢谢大家的收看。咱们下一次课程再见。



