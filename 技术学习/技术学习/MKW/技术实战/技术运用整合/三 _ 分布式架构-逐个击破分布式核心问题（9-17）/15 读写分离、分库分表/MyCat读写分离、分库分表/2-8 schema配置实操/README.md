---
title: 2-8 schema配置实操
---

# 2-8 schema配置实操

[image](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/7a761efe-d055-4895-83f5-5289feefac48/SCR-20240807-qomg.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466S3X63OTP%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T225408Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCwJ3aX72CKnUhlDM2dxY%2F%2FZYABGCfg4RhBtJDlUJ7VxQIhAKFdjz21qxzxLN0eaN%2F5f7CT06vWTH4y%2FwxSDP55TN3VKogECMb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1Igyof1acU63nTHqIVioq3AP1vpifYL3EExoxPfIKw6TqXqA0qsH0EUAx6GnqzST9mD1%2FBRytAs6FRkWvKsVX33fHLe1k7P20nSltnImQCP%2FeiyiLJ8C4K4jUgrzo20LDQ33JPcW4kpy0BZq2YFJGlIlRjHHG3AvoQ3lOt6AJUlBfQ08al0VyyK%2BrQOHcB7qAt%2FgJLccSPFcILa15RVOAwulKnBBydgVQNdPEFfay5s%2F8nHlAR0UqaNOmbg%2Bk%2FSdnvjhSpAdCqpLgQdKPO4dUlji3AqadEpRMJaNvARsEiYXCx%2F%2BwLFVHar2IuhPIFbE0f1D8rp9OAYLoFla137YygDHdgSosZB6ONlJz%2Bx4b80mU2ObA7nWG6H4Hyo3d5JqzN9xhipvXPYBfLtjLLz9FTAKM41v8uGdYnwD1fJtRAzMa6V0KQY6PylQqyx9n1zkhc06n0XmHU5SVoujwegp0QFUFpSHChroRvb%2BldCzU%2Fs1nymTNyLHzLvqRs%2F0oZqjjw%2BrCL2NSXbRfBl9F1SGVlohxDZvvkFvEJt6WD0u7EE7rSB4lQ%2Fk25yGeMS9Rl5x0vvw0BRkEzvZLmD3Qxf3tYvy%2BxYvH43MWxJoLXzvvaZVTYMpa0U%2F5S9gl7QK7a2KfyyUUZvKMGl%2Bl1ixWazCHt%2F%2FSBjqkAS1X6l4kccJbuvKCdo0D%2FXWJ4H29pW92BYBqcbD7bGHqAw%2BNUmaDS3JOhx1LiDENQSYMB1Mnyza4royXJbyBF1L8gNgxGgE7eLih7rEpt2Wmi1fGrp8XYGfm03nG2rTBjzpTusm5MhXyV7t0GOfNpiWuXQRpQQcog50%2BJF6lzhAHxrGKkujdnzoAHgPTV8k0ZlIyeC4hYJWG%2BJtYWJLlgjhCwWxt&X-Amz-Signature=4f41d4e4cbcc83c100a3344b373f6ef544cd10c5c2bb10e0d054d35df373a2f8&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

[image](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/e3ebab5f-14cb-4a1e-8afd-ea510219c3a2/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466S3X63OTP%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T225408Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCwJ3aX72CKnUhlDM2dxY%2F%2FZYABGCfg4RhBtJDlUJ7VxQIhAKFdjz21qxzxLN0eaN%2F5f7CT06vWTH4y%2FwxSDP55TN3VKogECMb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1Igyof1acU63nTHqIVioq3AP1vpifYL3EExoxPfIKw6TqXqA0qsH0EUAx6GnqzST9mD1%2FBRytAs6FRkWvKsVX33fHLe1k7P20nSltnImQCP%2FeiyiLJ8C4K4jUgrzo20LDQ33JPcW4kpy0BZq2YFJGlIlRjHHG3AvoQ3lOt6AJUlBfQ08al0VyyK%2BrQOHcB7qAt%2FgJLccSPFcILa15RVOAwulKnBBydgVQNdPEFfay5s%2F8nHlAR0UqaNOmbg%2Bk%2FSdnvjhSpAdCqpLgQdKPO4dUlji3AqadEpRMJaNvARsEiYXCx%2F%2BwLFVHar2IuhPIFbE0f1D8rp9OAYLoFla137YygDHdgSosZB6ONlJz%2Bx4b80mU2ObA7nWG6H4Hyo3d5JqzN9xhipvXPYBfLtjLLz9FTAKM41v8uGdYnwD1fJtRAzMa6V0KQY6PylQqyx9n1zkhc06n0XmHU5SVoujwegp0QFUFpSHChroRvb%2BldCzU%2Fs1nymTNyLHzLvqRs%2F0oZqjjw%2BrCL2NSXbRfBl9F1SGVlohxDZvvkFvEJt6WD0u7EE7rSB4lQ%2Fk25yGeMS9Rl5x0vvw0BRkEzvZLmD3Qxf3tYvy%2BxYvH43MWxJoLXzvvaZVTYMpa0U%2F5S9gl7QK7a2KfyyUUZvKMGl%2Bl1ixWazCHt%2F%2FSBjqkAS1X6l4kccJbuvKCdo0D%2FXWJ4H29pW92BYBqcbD7bGHqAw%2BNUmaDS3JOhx1LiDENQSYMB1Mnyza4royXJbyBF1L8gNgxGgE7eLih7rEpt2Wmi1fGrp8XYGfm03nG2rTBjzpTusm5MhXyV7t0GOfNpiWuXQRpQQcog50%2BJF6lzhAHxrGKkujdnzoAHgPTV8k0ZlIyeC4hYJWG%2BJtYWJLlgjhCwWxt&X-Amz-Signature=509c74268f7a2e830a029afb4076438e1923cce2737b74d792e5b0e5d624fa23&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

[file](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/30a52013-b1f4-4bc1-9aa0-4004f0059fbc/schema.xml?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466S3X63OTP%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T225408Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCwJ3aX72CKnUhlDM2dxY%2F%2FZYABGCfg4RhBtJDlUJ7VxQIhAKFdjz21qxzxLN0eaN%2F5f7CT06vWTH4y%2FwxSDP55TN3VKogECMb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1Igyof1acU63nTHqIVioq3AP1vpifYL3EExoxPfIKw6TqXqA0qsH0EUAx6GnqzST9mD1%2FBRytAs6FRkWvKsVX33fHLe1k7P20nSltnImQCP%2FeiyiLJ8C4K4jUgrzo20LDQ33JPcW4kpy0BZq2YFJGlIlRjHHG3AvoQ3lOt6AJUlBfQ08al0VyyK%2BrQOHcB7qAt%2FgJLccSPFcILa15RVOAwulKnBBydgVQNdPEFfay5s%2F8nHlAR0UqaNOmbg%2Bk%2FSdnvjhSpAdCqpLgQdKPO4dUlji3AqadEpRMJaNvARsEiYXCx%2F%2BwLFVHar2IuhPIFbE0f1D8rp9OAYLoFla137YygDHdgSosZB6ONlJz%2Bx4b80mU2ObA7nWG6H4Hyo3d5JqzN9xhipvXPYBfLtjLLz9FTAKM41v8uGdYnwD1fJtRAzMa6V0KQY6PylQqyx9n1zkhc06n0XmHU5SVoujwegp0QFUFpSHChroRvb%2BldCzU%2Fs1nymTNyLHzLvqRs%2F0oZqjjw%2BrCL2NSXbRfBl9F1SGVlohxDZvvkFvEJt6WD0u7EE7rSB4lQ%2Fk25yGeMS9Rl5x0vvw0BRkEzvZLmD3Qxf3tYvy%2BxYvH43MWxJoLXzvvaZVTYMpa0U%2F5S9gl7QK7a2KfyyUUZvKMGl%2Bl1ixWazCHt%2F%2FSBjqkAS1X6l4kccJbuvKCdo0D%2FXWJ4H29pW92BYBqcbD7bGHqAw%2BNUmaDS3JOhx1LiDENQSYMB1Mnyza4royXJbyBF1L8gNgxGgE7eLih7rEpt2Wmi1fGrp8XYGfm03nG2rTBjzpTusm5MhXyV7t0GOfNpiWuXQRpQQcog50%2BJF6lzhAHxrGKkujdnzoAHgPTV8k0ZlIyeC4hYJWG%2BJtYWJLlgjhCwWxt&X-Amz-Signature=4eae3024a0d213b726cce5b9149fd67d76a741ca5c4693e9a62dce7010d64c24&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

```javascript
<?xml version="1.0"?>
<!DOCTYPE mycat:schema SYSTEM "schema.dtd">
<mycat:schema xmlns:mycat="http://io.mycat/">

	<!-- <schema name="user" checkSQLschema="true" sqlMaxLimit="100" randomDataNode="dn200"> -->
	<!-- mycat的bug ===>checkSQLschema="true" 会导致操作全局ID的时候失去连接：  改成false 就可以了 -->
	<schema name="user" checkSQLschema="false" sqlMaxLimit="100" >
		<!-- auto sharding by id (long) -->
		<!--splitTableNames 启用<table name 属性使用逗号分割配置多个表,即多个表使用这个配置-->
		<table name="user" dataNode="dn200,dn201" rule="auto-sharding-long" />

		<table name="province" dataNode="dn200,dn201" type="global" />

		<!-- 配置父子表 childKey parentKey -->
		<table name="o_order" primaryKey="id"  autoIncrement="true" dataNode="dn200,dn201" rule="auto-sharding-long" > 
		     <childTable  name = "order_item" joinKey="order_id" parentKey="id" />
		</table>
	</schema>
	<!-- <dataNode name="dn1$0-743" dataHost="localhost1" database="db$0-743"/> -->


	<dataNode name="dn200" dataHost="db200" database="user_200" />
	<dataNode name="dn201" dataHost="db201" database="user_201" />


    <!--主要针对读的聚恒类型： balance="0" 负载均衡的类型 “0”;不开启负载均衡  “1”和“2”表示读写平均分配， “3”：读落在readHost上 -->
	<dataHost name="db200" maxCon="1000" minCon="10" balance="1" writeType="0" dbType="mysql" dbDriver="native" switchType="1"  slaveThreshold="100">
		<heartbeat>select user()</heartbeat>
		<!-- can have multi write hosts -->
		<writeHost host="M1" url="172.16.136.200:3306" user="guojun" password="guojun12" > 
				<readHost host="S1" url="172.16.136.202:3306" user="guojun" password="guojun12"/> <!-- 演示一下读写分离效果，并不是真的读写分离，因为数据不会同步 -->
		</writeHost>
		<!-- <writeHost host="hostM2" url="localhost:3316" user="root" password="123456"/> -->
	</dataHost>

	<dataHost name="db201" maxCon="1000" minCon="10" balance="0" writeType="0" dbType="mysql" dbDriver="native" switchType="1"  slaveThreshold="100">
		<heartbeat>select user()</heartbeat>
		<!-- can have multi write hosts -->
		<writeHost host="M2" url="172.16.136.201:3306" user="guojun" password="guojun12" /> 
		<!-- <writeHost host="hostM2" url="localhost:3316" user="root" password="123456"/> -->
	</dataHost>


</mycat:schema>
```

在上一小节当中，咱们给大家介绍了 schema.xml 里边的一些比较基础的配置。这一节咱们就给大家实战演示一下上一节的内容。咱们还是先把这个买 cat 给它启动起来，咱们先进入到买 cat 的这个目录，然后启动买 cat 之前咱们都是用 console 去启动了。 console 启动是什么意思啊？就是说它会把你的启动信息打印到这个控制台，然后我们是没有办法进行其他的操作的，我们验 ctrl C 这个 my cat 就停止了。那么现在咱们换一种启动方式，这块直接咱们敲 start 大家看到，这样它的启动方式就变成了后台启动，前面咱们还可以进行其他的操作。


好，启动起来以后，咱们再进入到这个 navigate 连接一下这个 my cat my cat 当中的 user 这张表有两条数据。然后咱们上一节是改了这个 SQL dmit 运行的时候只能查出一条，现在咱们再给它还原回去，进入到这个抗洪目录康复目录下的 schema.xml 咱们还把这个 limit 给它改成100，然后保存一下。
那好了，到现在咱们把这个配置文件保存完了，如何让这个配置文件生效呢？很多同学可能会想了，那我重启一下买 cat 是不是就可以了？对，这样没有问题。重启是一种方法。但是如果咱们应用到生产环境，你想想如果你每改一次配置的话，你都要重新买 cat 那是不是影响非常大。重启的时候，那你等于所有连接的这个请求是不是就全都断了？下面咱们就告诉大家这个让配置文件生效的第二种方法。


买 Kite 它启动的时候有两个端口，一个是8066。 8066 就是咱们连接的这个端口，8066它主要是做一些数据库的操作，增删改查这些东西。然后它还有一个 9066 端口。 9066 端口是干什么用的呢？他是买 cat 的管理，管理端口都有什么内容？咱们可以看一下，这块咱们再新建一个连接名字叫做 my cat manager IP 还是幺九二点幺六八点七三点幺三零端口 9066 用户名 root 密码 123456 咱们连接测试一下，没有问题，进入到这个 macite 的管理。


然后大家看到这个 user 是打不开的，那么怎么办？咱们这块可以打开一个命令行，命令行。然后咱们可以敲一下 show help 咱们可以看到里边它的一些命令，这些都是咱们可以执行的。可以看到第一列是它的命令，第二列是它的描述，可以看到你的 database 有哪些 data node 咱们敲一下试试。咱们敲一个 show data node ，咱们直接敲。 data node 咱们看看。 data node 有两个 DN 131 和 DN 132 这没有问题是吧，这里边咱们要着重的介绍一下，这个 reload 命令是可以重新加载你的配置文件，有一个 reload config 还有一个 reload config all 可以看看后边的这个描述 reload 基础的配置文件，然后还有 reload 所有的配置文件。


咱们刚才已经改了这个 limit 咱们如何让那个 limit 生效呢？在这里面咱们 reload 一下 reload config 回车，大家看到这块已经打印通的日志 success 成功了。然后咱们再执行一下查询，看看她能不能查出两条来好没有问题。所以以后咱们如果再修改了 schema 点叉 ML 文件，咱们直接可以在这里边 reload 一下就可以了。
这个主要是给大家介绍这个 my cat 的 9066 这个管理端口，咱们来快速的回顾一下上一节的内容。上一节这块咱们主要给大家介绍了这个读写分离，然后还有这个 balance 和 red type 这两个字段。下面咱们就配置一下，把这个毒库给它配置上。咱们在那个 red host 里面给他写个 read host 然后后头的名称等于 S1 然后 URL URL 写什么呢？咱们一会在这个 130 这台机器上再新建一个 MySQL 数据库。那么现在在咱们的这个实例当中就有了三个数据库，幺三幺一个132。这个是之前就已经创建好的，一会咱们在这个 130 上也创建一个就是三台数据库。


三台数据库怎么分配？ 132 这台它是一个独立的数据节点，它只有一个写库。然后 131 和 130 这两个数据库咱们给它做一个读写分离，咱们这块并不是真正的读写分离，它的数据不会同步的，咱们只是测试一下这一段配置。如果真正的要搭这个两台数据库的读写分离，咱们在后面的课程会给大家做一个简要的介绍。这块咱们先写上幺九二点幺六八点七三点幺三零端口还是 3306 in wall 慕课 passport 等于大写的慕课艾特123456，这样这个读写分离就已经配置完了。


然后咱们会在这个读库和写库两个数据库分别做两条数据，这两条数据是不一样的。然后咱们看看它读的时候咱们 select 这条语句它到底是从哪一个数据库去读，们这一段就已经配置完了，保存一下这个数据库的搭建就不给大家做演示了。这个 130 我之前也已经搭建了一个 MySQL 数据库，咱们可以看一下进程，有这个进程是吧，没有问题。咱们在这个内 Wiki 的先给它连一下，创建一个 130 的数据库，幺九二点幺六八点七，三点幺三零。这个咱们备注一下 MySQL 和这个 my cat 给大家区分开来，3306，然后用户 5 克连接一下，没有问题是吧，我们要在这个 130 这台数据库上再创建一个 schema 这个名称要和你 131 这个名称要对起来。为什么要对起来呢？因为咱们做的这个事例是 131 和 130 是一个主从，那么它的数据库这些名称都应该是一致的。这里面有一个数据库叫 user 131 这里边同样咱们也要创建一个数据库，叫做 user 131。然后字符集咱们还是选这个 UTF 8 LB 4 里边表一张右侧表，我们也是新建一下，里面有两个字段，这个也必须一模一样再添加一个叫做 user name 保存一下名称叫做 user 这样没有问题了。然后这里边咱们给它换一个名字，这里面叫做 DB 130，咱们再保存一下。


由于刚才咱们修改的配置文件这块咱们要重新 reload 一下，这块要给大家特殊说明一下，如果你修改配置文件，修改了是数据源相关的东西，咱们这个 schema 当中修改的就是数据源，因为加了一个读库 read host 如果你修改的是数据源的配置，那么你在 reload 的时候要使用这个 reload 这个大家一定要记住，咱们回车一下，这个 reload all 比较慢，大家看到也已经成功了。然后咱们回到 navigate 回到这个 user 的查询窗口，就是这个窗口，咱们点击一下查询现在查询的还是 131 这个数据库怎么呢？把这些没用的先给他关一下。看到这个是 130 这个数据库，咱们的这条记录是 idv 2 右侧 name 是 DB 130。


再看这个 131 这台数据库，这个是没有问题的，和咱们的这一段是对应起来的。下面咱们再看一下这个 schema schema 里边咱们配置了什么东西，主要是看这个字段配置了 balance 等于0。大家还记得这是什么意思吗？ alance 等于零，说明不开启读写分离，你所有的读请求都会落到这个写库，落到这个 right host 上。这个就和咱们刚才演示的这个是一样的，它的查询结果就是这个 ID 唯一的这条记录。然后咱们把这个 balance 给它改成 1 改成 1 是什么意思？ 1 是在你的读库写库之间来回切换这个 1 它的具体的切换和 2 还是不一样的。这个咱们上一节给大家说的是 1 和 2 都是在读写之间随机切换。我也是去了买 cat 的官网，找到了一个 my cat 的使用手册，咱们打开这个 my cat 的使用手册，然后进入到入门篇。这里边有一个 my cat 的配置，有一个 date host 标签，咱们往下看。这块有 balance 的介绍，但是等于零不开解读写分离，所有的读操作都落到当前的 right host 上。


这个就是刚才咱们演示的那样，所有的查询的记录还是 ID 唯一的那条记录，如果 ByteDance 等于 1 怎么办？大家看一下，全部的 read host 和 stand by read host 将参与这个 select 查询，它是什么意思呢？这个主要是针对主双从这种模式，大家可以看到主双从是什么意思？有一个主从m1s1，还有另外一个主从m2s2，并且这两个主库还互为主备。
那么这样咱们 schema 当中要怎么配置呢？这块是不是总共有四个数据库，一个主从就是这样一个 red host 一个 read host 然后另外还会再有一个这样的配置，就是等于有两个 red host 两个 read host 总共是四条记录。


那么这四个记录它怎么去分配呢？正常情况下m2s1， S2 会参与 select 查询。这个 m1 它是不参与的。也就是说在咱们的配置当中，第一个 read host 和后边的这个一个 read host 再加上一个 read host 总共三个数据库去承担 select 的查询。但是在咱们的这个例子当中，只有一个 red host 那么这个如果你配置成 1 的话，它所有的请求现在看一下，现在这块咱们已经给大家配置成 1 了。然后配置文件保存一下，在这个命令行里边再重新 RE 漏了一下。这里边 reload 咱们还是要用 config all 因为你修改的 balance 也算是数据源的配置这块咱们也要用 reload config all 好就已经刷新完成了，咱们再查询一下来看到了，现在这个 select 的查询是分配到了 130 这个数据库，这条记录已经变了，咱们再刷一下，多刷几遍，看看是不是他所有的 slack 的查询都落到了 130 数据库。


这个就和刚才咱们之前说的是一样的，你配置的是 1 你配置成为 1 以后，但是你的里边只配置了一个 red house 第一个 read host 是不参与读的，所以它只能落到 read host 上，然后咱们再改一下，把这个 balance 给它改成 2 保存一下，咱们看看 2 是什么意思所有的读操作随机分配到 red hose 和 read host 上。
咱们再来看一下这块咱们要再重新 reload 还是 reload config O 这块是有错误，他说有未完成的 DB 的事物。在执行你重新加载配置文件之前，所以他说了这个执行中断的逻辑，然后让你稍后再试。这个就是因为你执行了 reload config O 之后，买开头的后台会执行大量的操作，要替换掉之前的那些数据源的链接，这个是非常耗时的。所以这块他报出这么一个错，咱们要等一会再执行就没有问题。


咱们还是再看看这个文档等于 2 随机分配。如果 ByteDance 等于 3 是什么意思？所有的读请求都会分发到 red host 对应的 read host 上， red host 读负担读的压力，也就是说咱们这个 schema balance 配置成3。那么所有的请求也是落到 read host 上，read host 上是不会有这个读的请求的。好，咱们下面再执行一下这个 reload 看看行不行还是不行，还是要再多等一会儿。


好，咱们再试一下，没有问题了，再运行一下这个 slack 的查询。那现在又落到了 131 这台数据库上， ID 是1。然后咱们再运行一下，都变了，都变成 idv 2 的这条记录大家可以看到，我在这不停的刷新，它是随机的分配在读库和写库上，这个就是 ByteDance 设置成2。接下来咱们再给它改一下，改一下变成 balance 等于 33 的话其实还是落到这个毒库上，查询的结果都应该是 ID 等于 2 的这条记录。


这个咱们还要再刷新这个配置，你马上刷新是不成功的，咱们试一下看到了吧，咱们要等一会儿等一会再去刷新这个配置文件，咱们再试一下没有问题了，然后再刷新这个此 act 语句，这回刷新应该全都是 ID 等于 2 的这条记录没有问题了。好，咱们再把这个 balance 给它改回到最原始的状态，最原始的状态是不进行度假分别配置成零。然后咱们再介绍第二个，也就是这个 red typered type 等于 0 是什么意思？就是说当你有多个写库的时候，有多个 red host 的时候，它默认是写到第一个 red host 上。如果第一个 red host 挂了，再会去执行到第二个 red host 上，这个就是 red type 等于 0 的意思。 red type 等于 1 是两个 red host 随机分配，这种方式在这个买 cat 1.5 以后就已经废弃了不用了，所以这个 bad type 咱们只设置成 0 就可以了。


下面咱们给大家演示一下同样还是这三个数据库。但是现在这个 read host 这台数据库的角色要变了，它就不是读库了，要给它配置成为写库，咱们先把这个 read host 给它删除掉，然后再创建第二个 red hosthost 等于 m2 URL 等于幺九二点幺六八点七三点幺三零。然后端口 3306 user 等于慕课 password 等于。


这样是不是就可以了？咱们有两个 red host 咱们把这个配置文件给它保存一下，然后再刷新一下这个配置文件，还是要刷新 config 咱们看看能不能刷新还是不行，稍微的等一会儿咱们再看一下这schema 。一会咱们给大家演示的时候就要用 insert 一句了。 insert 一句。咱们还记得之前的分片规则吗？咱们看一下这张表的分片规则。 user 这张表有两个 data node 一个是 DN 131，一个是 DN 132 它的规则凹凸沙丁浪。这个规则是根据你的 ID 去分片的 ID 小于 500 万会分配到第一个这个数据节点上如果大于 500 万会分配到第二个这个数据节点上。咱们一会演示的时候就给它插入一个小于 500 万的一个 ID 就会分配到 DN 131。 DN 131 它的 data host 是 DB 131，也就是会落到这个 data host 上。这个 data host 里边它有两个 red host 如果你配置的这个 red type 等于0，那么这个 insert 语句会插入到第一个 red host 上，也就是会插入到 131 这台数据库。如果 131 这台数据库挂了，那么你再插入的时候会插入到 130 这台数据库。咱们记住这个规则，一会咱们验证一下是不是这样。咱们再看看这个配置文件已经刷新完成了。


这回这个 circle 咱们要重新写一个新的 insert 金兔 user 然后里边 ID username values 这个 ID 咱们插一个3，然后后边这个值咱们插一个，它应该是落在 DB 131 上是吧，咱们写一个， DB 131 我们执行一下没有问题，插入一条成功了。然后咱们去这个 DB 130 这个是 DB 130 的数据库，那我们刷新一下没有 ID 等于 3 的这条记录。然后这个 DB 131 的数据库咱们刷新一下 ID 等于 3 是吧，没有问题。和咱们这个 schema 当中配置的是一样的，你现在所有的写都会落到第一个 right host 上。然后现在如果我把 131 这个数据库给它停掉，那那么 131 这个数据库是不是就模拟成宕机的这种情况了，你再插入就会插入到130，咱们模拟一下。
咱们进入到 131 这台机器，把这个 MySQL 给它停一下，怎么停？那个 MySQL 命令 system ctl stop my circle D 好，这个 MySQL 已经停止了，咱们这回再给他插入一条记录，插入 ID 等于 4 的这条记录名字，咱们改一下，改成叫做 DB 130。


运行一下可以看到，第一次运行的时候这块报错了， connection exception 拒绝连接。这个说明 131 这台数据库已经挂，咱们再执行。这个有插入成功了，咱们再去看一下。这个是 130 的这台数据库，咱们刷新一下看到 ID 等于4，这条记录已经展示出来了。


再看131，131咱们刷新一下连接不了了，因为 131 已经挂了，咱们再把这个给它启动起来，把 131 这个数据库给它启动起来。 start 好，启动完成了。咱们同学们想一想，现在 131 又启动成功了，我们现在如果我再插入一条记录，这个 ID 等于5，那么你说它会插入到 130 还是 131 呢？答案是还会继续插入到 130 这个数据库。
虽然你的这个配置文件当中配置的是 131 在前面，但是你在前面你已经挂了一次了，那么 130 就排到了第一个。所以每次都会插入到130。然后如果你 131 服务又起来了，那么你又会在后面继续的去排队，所以 130 就排到了第一个。咱们试一下插入，然后在这里面再刷新一下。


5 这条记录也已经出来了，这个就是它的这个 red type 等于 0 自动切换到这里。这个读写分离的这一段配置就给大家先介绍到这了，大家也通过实战的案例去了解了每一个规则是什么样的。然后还给大家介绍了这个买 Kite 的管理端口9066。如果你修改的这个 schema 当中的配置和数据源有关系，那么你 reload 的时候要使用 reload a config all 这一小节就给大家先介绍到这。下一节咱们会给大家演示如何去搭建 MySQL 的毒血分离。因为这一节这块模拟了它的读写分离了，但是它并不是一个真正的读写分离。下一节咱们会给大家演示这一块的内容。




