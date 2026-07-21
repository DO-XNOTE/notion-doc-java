---
title: 2-6 MyCat和Sharding-JDBC的分布式事务
---

# 2-6 MyCat和Sharding-JDBC的分布式事务

[image](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/54f6e3ee-44b6-4dba-84d6-3724c4003932/SCR-20240808-dujf.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46653J3ESJQ%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T225431Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCIx9g%2BP8qphn56g4XL0co%2F0T%2BKNRUuH7BHqWQfWXZF7gIhANBbWhEE188Gv5IWthCfd%2BO0H5Jb3T2Ehhw9VFhhQ6ZnKogECMb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgwGTrCQlYsBQdP03xkq3AMwgExDXRYqx2aBLIBjmQjYyX0%2FV1G8neSfrm9H5eUSBcA%2FUvJJDBJEt%2FYc6h8NWNGr2doplpj4WdTImRD%2BiScsVafZuKo3WWDYFAzOJ6koLzuK3wbP%2B74X23oQb59avAh93QTRyxoXNvXE%2FY0C8InBX0wDjJuFA8NAZaCru0fuMZ3oycnLP9TsnzRpd6Ku3q%2Fnh%2FdbsJ2gav97tYn2uKVJF2qRmISQJsctqoDRr1HNOcjIZvACM31DCT1aAHX1vNNFQhBGheeyLuY8hGqxzUISK%2BisZt2aFlFMxJIF141uZDxOEhNOw%2BFVK1C7z%2FFoUNohj7EQ0oheUS8GitIcfkTbbqqsTfciw9etf3TI962CmjmWITquBCzu73OaK2175qi06ruRvN8ZYt9E4h94TVSZfAN0krOuRmTlWrcAjwWbUNUI0S%2BWF5pW3NEl%2B%2F3mKXLhL%2FU8hoLjT07cmSx1RVDFTVvJwaezvYHUY7ywaC6i7ex6SXv53TN21ffHb0QKKVFobtEPwxbDBSm5GUDoGLFzD7oD6Sn%2F8rbWwR2afhfvtf%2BvGV7Kjzp6DVUT%2BJd%2BFhRPgGVEnSTdRgxaohs86NCoRU4X7NySNX4t3hkClNUuXIkgF1q168qdSynUWDDet%2F%2FSBjqkAe6JcNzzzXz%2BKsqquM0c%2Fgq6iBJyZOu2abhOffTM%2BkQ24hAxjtr%2BReqU6xi3ccd%2FEgvyYZTjk9GeMNmVPWPbWFPujzKEBANbnM%2Bgx9z1hlXXtRe04d8ARt5cqPLThjGh%2FdXdhBShzC7BLgmKHOTF%2BuJ5J2dI3LcdO6Cm8nbmSI85hmGt%2F7tZf3VkgQLhThVzBgqjESVTTZhUOoTVxc1oxiFPZLfm&X-Amz-Signature=c39b355a73917392a61df448c3a2e04bb10102095e0d91c22d498c27e85d764c&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

[image](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/27a028f4-9999-4418-a9bd-0548036d7173/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46653J3ESJQ%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T225431Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCIx9g%2BP8qphn56g4XL0co%2F0T%2BKNRUuH7BHqWQfWXZF7gIhANBbWhEE188Gv5IWthCfd%2BO0H5Jb3T2Ehhw9VFhhQ6ZnKogECMb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgwGTrCQlYsBQdP03xkq3AMwgExDXRYqx2aBLIBjmQjYyX0%2FV1G8neSfrm9H5eUSBcA%2FUvJJDBJEt%2FYc6h8NWNGr2doplpj4WdTImRD%2BiScsVafZuKo3WWDYFAzOJ6koLzuK3wbP%2B74X23oQb59avAh93QTRyxoXNvXE%2FY0C8InBX0wDjJuFA8NAZaCru0fuMZ3oycnLP9TsnzRpd6Ku3q%2Fnh%2FdbsJ2gav97tYn2uKVJF2qRmISQJsctqoDRr1HNOcjIZvACM31DCT1aAHX1vNNFQhBGheeyLuY8hGqxzUISK%2BisZt2aFlFMxJIF141uZDxOEhNOw%2BFVK1C7z%2FFoUNohj7EQ0oheUS8GitIcfkTbbqqsTfciw9etf3TI962CmjmWITquBCzu73OaK2175qi06ruRvN8ZYt9E4h94TVSZfAN0krOuRmTlWrcAjwWbUNUI0S%2BWF5pW3NEl%2B%2F3mKXLhL%2FU8hoLjT07cmSx1RVDFTVvJwaezvYHUY7ywaC6i7ex6SXv53TN21ffHb0QKKVFobtEPwxbDBSm5GUDoGLFzD7oD6Sn%2F8rbWwR2afhfvtf%2BvGV7Kjzp6DVUT%2BJd%2BFhRPgGVEnSTdRgxaohs86NCoRU4X7NySNX4t3hkClNUuXIkgF1q168qdSynUWDDet%2F%2FSBjqkAe6JcNzzzXz%2BKsqquM0c%2Fgq6iBJyZOu2abhOffTM%2BkQ24hAxjtr%2BReqU6xi3ccd%2FEgvyYZTjk9GeMNmVPWPbWFPujzKEBANbnM%2Bgx9z1hlXXtRe04d8ARt5cqPLThjGh%2FdXdhBShzC7BLgmKHOTF%2BuJ5J2dI3LcdO6Cm8nbmSI85hmGt%2F7tZf3VkgQLhThVzBgqjESVTTZhUOoTVxc1oxiFPZLfm&X-Amz-Signature=c1bc518a04affc4e9a710865d606a8f378579358e2588069baed85266ae95289&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

[image](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/5f22b6c9-5d13-4531-ba3f-43fff5fd74ec/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46653J3ESJQ%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T225431Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCIx9g%2BP8qphn56g4XL0co%2F0T%2BKNRUuH7BHqWQfWXZF7gIhANBbWhEE188Gv5IWthCfd%2BO0H5Jb3T2Ehhw9VFhhQ6ZnKogECMb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgwGTrCQlYsBQdP03xkq3AMwgExDXRYqx2aBLIBjmQjYyX0%2FV1G8neSfrm9H5eUSBcA%2FUvJJDBJEt%2FYc6h8NWNGr2doplpj4WdTImRD%2BiScsVafZuKo3WWDYFAzOJ6koLzuK3wbP%2B74X23oQb59avAh93QTRyxoXNvXE%2FY0C8InBX0wDjJuFA8NAZaCru0fuMZ3oycnLP9TsnzRpd6Ku3q%2Fnh%2FdbsJ2gav97tYn2uKVJF2qRmISQJsctqoDRr1HNOcjIZvACM31DCT1aAHX1vNNFQhBGheeyLuY8hGqxzUISK%2BisZt2aFlFMxJIF141uZDxOEhNOw%2BFVK1C7z%2FFoUNohj7EQ0oheUS8GitIcfkTbbqqsTfciw9etf3TI962CmjmWITquBCzu73OaK2175qi06ruRvN8ZYt9E4h94TVSZfAN0krOuRmTlWrcAjwWbUNUI0S%2BWF5pW3NEl%2B%2F3mKXLhL%2FU8hoLjT07cmSx1RVDFTVvJwaezvYHUY7ywaC6i7ex6SXv53TN21ffHb0QKKVFobtEPwxbDBSm5GUDoGLFzD7oD6Sn%2F8rbWwR2afhfvtf%2BvGV7Kjzp6DVUT%2BJd%2BFhRPgGVEnSTdRgxaohs86NCoRU4X7NySNX4t3hkClNUuXIkgF1q168qdSynUWDDet%2F%2FSBjqkAe6JcNzzzXz%2BKsqquM0c%2Fgq6iBJyZOu2abhOffTM%2BkQ24hAxjtr%2BReqU6xi3ccd%2FEgvyYZTjk9GeMNmVPWPbWFPujzKEBANbnM%2Bgx9z1hlXXtRe04d8ARt5cqPLThjGh%2FdXdhBShzC7BLgmKHOTF%2BuJ5J2dI3LcdO6Cm8nbmSI85hmGt%2F7tZf3VkgQLhThVzBgqjESVTTZhUOoTVxc1oxiFPZLfm&X-Amz-Signature=e97f4bf0ec6f9a1e77fe364d22d6dfd0a5a7534352e29d64fb39148cdbcbed13&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

好，咱们接着再看一下 my cat 里边的分布式事务。首先咱们先进入到这个 navicate 看一下这个 my cat 咱们相关的这个规划是吧，也就是这个数据库还有表都是什么样子买开的里边咱们是连接了两个数据库，一个是131，一个是 132 是吧。然后里边具体的咱们连接的是 user 131 和 user 132。这里边咱们看一下这个 user 131 这个第一张表， my cat sequence 是咱们上一张的内容分布式的 ID 这一张分布式事务咱们选择user ，选择 user 表，给大家做一下这个分布式事务的演示。咱们先把这个 user 表里边把这些记录都给它清空，就给它删除掉，131删除了。然后咱们再看132，132咱们也给它删除掉。这个优色表它的分片规则是什么样呢？咱们还是进入到 my cat 的配置文件当中，看一下它当前的分片规则，进入到130，然后咱们进入到 my cat 的目录。然后看一下康复目录下边的 schema 的叉 L 这里边咱们配置的右侧表对吧。
table name user data node DN 131 DN 132。


它的规则是 model log 咱们来看一下这个弱，再看一下康复目录下边的弱点叉 L 摩德旺它是通过 ID 去进行分片，它的逻辑摩德旺咱们看一下方克神方克沈里边的摩托旺只需要配置一个节点就可以了。那么它是对 2 进行取模对吧，取模为 0 的将会分配到 131 的数据库，取模为 1 的将会分配到 132 的数据库。咱们看一下这个内威 cat131 的右侧数据库。然后 132 买 cat 它是从一点六点五版本以后都是支持分布式的事务的。它的这个事物在哪里配置了？它是在 CONF 目录下边的 server 的叉 ML 里边去进行配置。


在这个配置文件当中，咱们找到 property 这个 handle distributed 的 transaction 处理分布式的事务，上面已经给咱们注释得非常的明确了，零为不过月分布式事务 1 为过滤式分布式事务，如果分布式事务只涉及全局表，则不过滤。二为不过滤分布式事务，但是要记录分布式事务的日志。
这个不过滤是什么意思？这个不过滤其实就是支持的意思就是0，它是支持分布式事务的，1它是不支持分布式事务，就是把这些分布式事务的操作给它过滤掉。所以这块 1 为过滤分布式事务，把这些分布式事务的 SQL 语句给它过滤掉，它就是执行不成功的了，这样就比较好理解一些了。


my cat 默认的配置是支持分布式事务的支持分布式事务。那么咱们在这个内 case 当中给它做一下测试，咱们还是把这个买 cat 先给它启动起来并买 cat stat 买 cat 已经启动完了，咱们进入到 navicate 连接一下这个 my cat 咱们查询一下 user 表没有数据对吧，然后写一条 circle 语句， insert into user 后边跟他的列 ID user name 咱们就插这两个列，其他的列咱们就先不插入值了。然后第一条记录 ID 等于1，然后 user name 咱们给它写作基数，然后再插入一条记录 ID 是2，然后 user name 咱们写成偶数，咱们执行一下，运行一下插入了两条记录对吧，咱们分别看一下 131 和 132 的数据库，131的数据库插入的是偶数，然后 132 的数据库插入的是奇数，这个都没有问题对吧，然后咱们看一下如何开启这个事物。


这个事物，咱们先把这两条记录清一下，把这两条记录清一下，咱们看看如果这块它插入报错的话会是什么样子？咱们插入其中一这条记录不报错。然后 2 这条记录咱们给它插入一个报错的，试一下。这个咱们怎么去试呢？把这个 user 表的内容给它改一下。 user 这张表这个 user name 是 255 位是吧，咱们把这个字段的长度给它改的短一点，给它改成两位。好吧，改成两位，那么保存一下。然后这条插入的语句。


第一条 user name 插入两个字，这个应该是没有问题的对吧。然后第二条记录咱们这个 user 类目给大家插的稍微长一点，是不是第二条记录就报错了。而且这两条记录分别坐落在两个不同的分片上，看看买 cat 能不能保证这个分布式的事物咱们给它插的长一点，然后运行一下。咱们还是把之前这两条记录给它清空一下。好，然后咱们再执行这条记录报错了是吧。


date too long 和 column user name 然后咱们再看一下，因为是第二条记录报错了，咱们看第一条记录到底插入成功没成功，咱们回到右侧表刷新一下。 user 这张表，第一条记录是插入成功的了，是不是咱们看一下。第一条记录基数应该在 132 的这个数据库当中，咱们刷新一下，成功了是吧？然后 131 它应该是插入不成功的。也就是说在 navik 的当中，咱们直接插入两条数据，并没有保障事物的一致性对吧？第一条记录成功了，第二条记录并没有成功。


那么咱们怎么去保障这两个不同的数据库给它放到一个事故当中呢？首先叫 set 这个 auto commit auto commit set 成0，这样就是把自动提交的这个开关给它关闭了，然后再 set xa 等于 on 这样就是把 xa 的这个事物给它开启，最后咱们再进行 commit 这样就能够保障事物的一致性了。咱们把这条记录还是给它删除掉，保证现在优色这张表是没有任何记录的。然后咱们再执行这一段，咱们运行一下，前面 auto commit 等于 0 和 xa 等于 2 都已经生效，然后插入数据的时候报了一个数据超长，这回咱们再刷新一下这个右侧这张表，看看有没有记录刷新一下，这样是不是就没有问题了？这两条记录都没有插入到数据库当中对吧？看来咱们的这个分布式事故是生效的。
但是有的同学可能会说了，你使用 my cat 你这段配置都是在 navik 的当中去进行的，我可以进行 auto commit 等于0，可以进行 xc 等于2。但是这样的语句我在我的项目当中怎么去写呢？因为我项目当中连接了 my cat 我使用的 my betis 我这一段要去怎么在项目当中去使用呢？这个咱们看一下，咱们新搭建一个项目，直接用 my betis 连接这台 my cat 看看它支持不支持分布式的事务。


咱们打开 idea 然后咱们新建一个项目还是使用 spring boot 然后名字咱们叫做 my cat demo 。好吧， my cat 看 demo 然后选择比较常用的依赖 homebook spring web 然后 circle 里边咱们选择 jpa MySQL 的驱动，还有 my betis 的框架，然后选择下一步完成。
在一个新的窗口，打开项目创建好以后，咱们先把这个买白迪斯的生成器的给它配置好。在这个 plugin 里边，咱们还是找到先前的项目，把这个拜拜一次 generator 给它复制一下，粘贴到咱们新生成的这个项目当中，刷新一下 Maven 然后还有一个配置文件和这个配置文件，咱们也给它粘贴过来，复制一下，粘贴到咱们的项目当中。
resource 目录下咱们配置一下，这个咱们直接连接买 cat connectionurl 这块，咱们要配置成 130 端口 my cat 的端口是8066，数据库连的是 user 其他的不用变。然后用户名和密码。用户名咱们配置的是 boot 密码123456。这个这 BC connection 就配置完成了对吧。然后后边生成的目录，咱们统一配置一下，配置到当前的这个目录下边来买巴基斯 demo 这个买卖基斯这块就不用区分它是哪一个数据库的了，总之都是连接 my cat 这块也要统一的修改一下。最后就是这个表 schema 咱们是 user 然后 tablename 也是 user 映射成的实体类大写的 user 配置完成以后，右边点击 Maven 找到插件，然后双击一下 madis 生成器，创建成功没有问题是吧。咱们进入到项目当中，再去看一眼买卖 is 叉 ML 正常的生成了，然后 do mode 两个目录都有生成的文件，这张表已经映射到咱们的项目当中。


然后咱们要进行数据库的配置是吧。咱们进入到 application.props 里面，首先要去配置它的数据源， spring.data source.username 咱们配置的是 root 然后 spring.data source.password123456，还有 spring date source URL 这个 URL 咱们直接从这里边把它复制过来，是不是就可以了给它复制过来。然后这个 and 符咱们不需要转译了是吧，直接把这个后边的 amp 给它删除掉，这样是不是就可以了？数据源配置好以后，然后配置买 Betty 斯的 mapper location 第一个， mapper location 咱们指定 matis 的叉 ML 配置文件 matis 杠星点叉 ML 最后在这个启动类当中，要配置它的 mapper 的路径，加一个 mapper scan 它的路径指定到 DAO 这个目录咱们复制一下，然后粘贴过来，这样是不是就配置完了？配置完以后咱们写一个 service 然后分别往这两张实习表里边。


插入记录，其实咱们只需要连接买 cat 就可以了。这两条记录的 ID 一个是奇数，一个是偶数，看看它能不能正常的插入成功。咱们还是创建一个目录 service 再创建一个 user serviceuser service 类上打一个 service 的注解，然后把 user 的 mapper 给它注入进来，加一个 resource 的重点。然后写一个方法， public word test user 然后写一个 user user 1 new user user 引入一下，然后设置一下他的 ID 第一个 ID 咱们设置成1，第二个 user name 咱们设置成基数，然后插入一下 user map.insert user 1，然后咱们再创建一个u42，咱们统一改一下 642id 是 2 插入的 user name 是偶数，这个列咱们要给它插入的长一些，这样它就会抛出异常了。这里面这个方法咱们要给它加上一个统一的事物，像 sectional 配置一下 go back go back for 或者什么 exception 是所有的异常咱们都要进行追滚，这个 service 就写好了。然后咱们在这个测试内当中调用一下这个 service 新写了一个 test user 然后把 user service 给它注入进来下一个 auto where 的注解，然后调用一下 test user 这个方法，再加一个太词的注解，这样是不是就行了。


然后咱们在这个数据库当中，把这个 user 这张表给大家清空一下，都清空完了是吧？ user 132 和 user 131 目前都是没有任何记录的，咱们运行一下这个程序，看看她还会不会一个插入成功，一个插入不成功报错了对吧，咱们看看什么？错。 date 粗暴是吧，数据超长了。然后咱们再回到那位 case 刷新一下，没有记录是吧，没有任何的记录说明。在咱们的这个项目当中，你直接连接 my cat my cat 它是支持分布式事务的，咱们在这个 user service 当中一个插入了奇数，一个插入了偶数。他们这两条记录分别坐落于不同的分边库当中。


第一条记录应该是插入成功的，因为它的 user name 是两位符合数据库的要求。第二条记录咱们右上内部差不了 5 位数显然不符合。那么第二条记录不符合数据库的，咱们设置的这个长度是不是他就要进行回滚。回滚咱们连同第一条记录也进行了回滚，也就是说这两个分片库同时进行了事物的回滚，这样是没有问题的，没有问题。
下面咱们再看一下，看一下这个康复目录下边的 server 点叉 ML 咱们如果把它配置成为 1 会是什么样子配置成为 1 是什么样子？咱们给它改一下配置成为1，它表示是过滤分布式事务对吧？那就是所有分布式事物的这些思考语句，它会给它过滤出来，执行是不成功的。咱们给它保存一下。然后重启一下 my cat 你 start 充气完了是吧。咱们这回在 user 上，咱们先刷新一下，没有记录是吧。然后咱们只执行中间的这一条记录只执行这一条记录，咱们给它剪切一下，只执行这一条记录。然后后边长度咱们也全都符合要求，咱们再运行一下


看到现在报什么错了，报了一个 distribute transaction disabled 分布式的事务是关闭的，不能执行的 disable 的是吧。这个就是 my cat 当中的这个开关，咱们还给他调成0，再给它调成0，然后保存一下，再重启一下。


再看到这里，这个买 cat 的分布式事务就给大家介绍完了。买 cat 从一点六点五以后它是支持分布式事务的，而且支持的也非常的好。如果咱们通过 navik 的进行连接，要让它支持分布式事务，咱们要自动提交的这个开关，先给它关闭，然后打开 xa 的这个开关，最后统一的去提交事务，这样就能保证它的分布式事务。


如果在咱们项目当中，咱们直接连接买 cat 直接连接买 cat 以后它是支持事务的，和咱们使用单一数据库是没有任何的区别的，只需要在咱们的方法当中打上 try 三个人的这个注解和单体的应用是没有任何区别的。到这里，这个 my cat 分布式事务给大家讲到这。接下来咱们来看一下沙厅类 BBC 看看沙丁这 gbc 里面如何配置它的分布式事务还是和之前一样。咱们先看一下沙丁这 BBC 这个项目，咱们之前规划的数据库，咱们先把右边的这些全都给它关闭掉。山亭 DC 的这个项目，咱们也是在 131 和 132 这两个数据库当中，它对应的 schema 分别是 shutting order 还有一个是 shard order 咱们之前给大家演示都是使用的 T order 咱们现在还是使用这个 T order 给大家做演示。


咱们回到这个沙丁 GDB C 的项目，咱们把这个然后打开沙丁 GDB C 打开这个项目。咱们看看当前的这个项目使用的是哪些配置。咱们先进入到 pom.xml 这里边咱们使用的是 spring boot starter 对吧，咱们看一下 application.properties 这里边咱们使用的 I E 的生成器是雪花算法，然后它的。分片规则咱们使用的是自定义的这个分片规则，咱们还是进去看一下。


自定义的这个分片规则它是用 ID 取模是吧，取模以后决定它的 T order 1 还是 T order 2，咱们再回到 application.promise 首先数据库的分片使用的是 user ID user ID 对 2 取余，然后再使用 order ID order ID 也是对 2 取余对吧。只不过咱们写到了买 shut 这个类当中。下面咱们也是写一段程序，分别往这两个分片库当中去插入数据，还是进入到之前的 test 的目录，找到这个测试类。测试类当中，咱们写了泰斯 order 对吧，咱们把这一段测试程序稍微给它改一下，咱们这里边指定它的组件set。 Order id. 第一个咱们设置成为1，然后再给它插入另外一条 order 这个 order 咱们给大家统一改一下。 order 2 order 2 order 的这个 ID 咱们设置成为2，然后 user ID 咱们也给它设置成一个偶数，设置成16。然后咱们再进入到这个 av case 把之前的这个调整的数据统一的给它清空一下，132的清空完了，咱们再清空，131的也给它清空一下。


咱们接着再看，看看这个调的表里边，咱们怎么去让它报错，咱们看一下，这里边都是数字型的长度是吧，咱们这里边就先不动了，咱们直接在程序里边抛出一个异常。好吧，这里边咱们 throw 一个 throw 一个 new 注释叫 text xa 然后直接在这个测试方法上打一个 transaction 这样一个注解到这里，这个测试程序咱们已经修改好了，咱们运行一下，看看能不能正常的回滚报错了是吧，应该就是咱们之前写的那个错误 test xa 咱们回到 navicate 当中，看一下这几张表。先看一下 131 的 T order 1 没有记录，131的 T 腰带 2 也没有记录。
再看看啊，132的 T 腰带 1 和 132 的 t2 的 2 都没有记录，说明沙丁这 DB C 也是支持这个分布式事务的沙鲸这 EB C 它默认已经为咱们开启了分布式的事务，咱们也是和 my cat 一样，直接连接沙鲸 GB C 的这个数据源，就可以实现分布式的事物。到这里买 cat 和沙定 gdbc 的分布式事务就给大家介绍到这儿了，感谢大家的收看，谢谢大家。



