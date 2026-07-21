---
title: 开发指南
---

# 开发指南

[image](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/b9fdf2c1-d98b-4d09-bf27-9c9d2621962d/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466X4WT6DEU%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T225357Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIDVlq%2BSpCyCK7jblo2Rf8w1T2%2FbPM1qraSv6zFsiQ8bcAiAmVcp%2Bp1p8WFnSItitr%2FJmL%2FS5hD26%2BrDpn0VbR0VxwiqIBAjG%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMwTE82RT05mOecQFDKtwDF6oXgNIIc6gdCqq6%2FhCyoW3X7RpSvY5wamEEc6IhzKRxxieWd4eAFRPstkrNZaUD%2Fcm6oh0%2FOdvK5xD0RKZjZvizxDM4jzfakAgPVKofWV73DX1SMIAZz6VJvirrrevJ2cxjMQv06k6s7b5q1gX3HkCp1RKGy1TvvUJV1C5cP2GjkLu6ehCMB7DlNyZ75jWFnGEw4FRwNDYigsbrX3633xha9Kf0f37c2JA1fQPIfg55mj%2BH2wVxSagYadrDXrXiDulEtOgsS1vXaLpp31QXDSVdy6FF7Nr74I6GY70C41mVlGenW0CV0NmHh%2BIypA%2FJHGpO%2FlbSNkgVZmZcRF4AtBWxgg4c%2B%2BrxlrvDkjA%2Bvj%2B%2Bb3FpGcbEb87xJKOHFSaMEBdJx62Os5pM0lKaWllbTS%2BNTd78ypV2pCVvDxp3EHILacWXUqOOpcNJ21EZjRS6Ig7h5tWvWwVSoeKi1ZI%2FCQzEr%2BRsN67BXLkLINOeiss1d6jGBMWEyJYMat7TmUbZ3bPK0VG5NERH3nbjx708pQ%2Febyi5JPYWM9ojkTctoeRzDtBz6T1lTYk37jw7URWU17DRV0VUbhizNtIG8VjXFq0ole%2FodSD9xsb%2FmbrkwpNMJ6dWAGYg1zMsypswtLj%2F0gY6pgGzK56NwqPIB%2F8EuIqPqnUWF%2BM2aC2i3Jcj0EOaTYgV%2BNg6YMgY%2BdAIC7Eb4vaVRojJ4w84%2FHyTfzWOAFErZyb9q0c2tRB%2BpTkZnT8zvGxWKukmNmGG%2FczPr1mMP1PZYryAyjyD6QE6ZRRFyg9pSXhNtIXI9A83FFQQgYJUK0aVfmeXERtCF7GiVFHFqFQDKQ1a%2FITVU2TRId9OXWFRAqeeXZU25bE%2F&X-Amz-Signature=35b03eabb205cc3fdff2db33f89e911c7f862f7b8ccd1d103f5672d066c532d4&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

**MyCAT  In Action中文版**

MyCAT 1.3版本

**MyCAT介绍**

什么是MyCAT？简单的说，MyCAT就是：

· 一个彻底开源的，面向企业应用开发的“大数据库集群”

· 支持事务、ACID、可以替代Mysql的加强版数据库

· 一个可以视为“Mysql”集群的企业级数据库，用来替代昂贵的Oracle集群

· 一个融合内存缓存技术、Nosql技术、HDFS大数据的新型SQL Server

· 结合传统数据库和新型分布式数据仓库的新一代企业级数据库产品

· 一个新颖的数据库中间件产品

**MyCAT**的目标是：低成本的将现有的单机数据库和应用平滑迁移到“云”端，解决数据存储和业务规模迅速增长情况下的数据瓶颈问题。

**MyCAT  1.3**的关键特性：

· 支持 SQL 92标准

· 支持Mysql集群，可以作为Proxy使用

· 支持JDBC连接ORACLE、DB2、SQL Server，将其模拟为MySQL  Server使用

· 支持NoSQL数据库

· 支持galera for mysql集群，percona-cluster或者mariadb cluster，提供高可用性数据分片集群

· 自动故障切换，高可用性

· 支持读写分离，支持Mysql双主多从，以及一主多从的模式

· 支持全局表，数据自动分片到多个节点，用于高效表关联查询

· 支持独有的基于E-R 关系的分片策略，实现了高效的表关联查询

· 支持一致性Hash分片，有效解决分片扩容难题

· 多平台支持，部署和实施简单

· 支持Catelet开发，类似数据库存储过程，用于跨分片复杂SQL的人工智能编码实现，143行Demo完成跨分片的两个表的JION查询。

· 支持NIO与AIO两种网络通信机制，Windows下建议AIO，Linux下目前建议NIO

· 支持Mysql存储过程调用

· 以插件方式支持SQL拦截和改写

· 支持自增长主键、支持Oracle的Sequence机制

**MyCAT**的优势：

· 基于阿里开源的Cobar产品而研发，Cobar的稳定性、可靠性、优秀的架构和性能，以及众多成熟的使用案例使得**MyCAT**一开始就拥有一个很好的起点，站在巨人的肩膀上，我们能看到更远。

· 广泛吸取业界优秀的开源项目和创新思路，将其融入到**MyCAT**的基因中，使得**MyCAT**在很多方面都领先于目前其他一些同类的开源项目，甚至超越某些商业产品。

**· MyCAT**背后有一只强大的技术团队，其参与者都是5年以上资深软件工程师、架构师、DBA等，优秀的技术团队保证了**MyCAT**的产品质量。

**· MyCAT**并不依托于任何一个商业公司，因此不像某些开源项目，将一些重要的特性封闭在其商业产品中，使得开源项目成了一个摆设。

**MyCAT**的长期路线规划：

· 在支持Mysql的基础上，后端增加更多的开源数据库和商业数据库的支持，包括原生支持PosteSQL、FireBird等开源数据库，以及通过JDBC等方式间接支持其他非开源的数据库如Oracle、DB2、SQL Server等

· 实现更为智能的自我调节特性，如自动统计分析SQL，自动创建和调整索引，根据数据表的读写频率，自动优化缓存和备份策略等

· 实现更全面的监控管理功能

· 与HDFS集成，提供SQL命令，将数据库装入HDFS中并能够快速分析

· 集成优秀的开源报表工具，使之具备一定的数据分析的能力

MyCAT**架构**

如图所示：MyCAT使用Mysql的通讯协议模拟成了一个Mysql服务器，并建立了完整的Schema（数据库）、Table （数据表）、User(用户)的逻辑模型，并将这套逻辑模型映射到后端的存储节点DataNode（MySQL Instance）上的真实物理库中，这样一来，所有能使用Mysql的客户端以及编程语言都能将MyCAT当成是Mysql Server来使用，不必开发新的客户端协议。


当MyCAT收到一个客户端发送的SQL请求时，会先对SQL进行语法分析和检查，分析的结果用于SQL路由，SQL路由策略支持传统的基于表格的分片字段方式进行分片，也支持独有的基于数据库E-R关系的分片策略，对于路由到多个数据节点（DataNode）的SQL，则会对收到的数据集进行“归并”然后输出到客户端。

SQL执行的过程，简单的说，就是把SQL通过网络协议发送给后端的真正的数据库上进行执行，对于Mysql Server来说，是通过Mysql网络协议发送报文，并解析返回的结果，若SQL不涉及到多个分片节点，则直接返回结果，写入客户端的SOCKET流中，这个过程是非阻塞模式（NIO）。

DataNode是**MyCAT**的逻辑数据节点，映射到后端的某一个物理数据库的一个Database，为了做到系统高可用，每个DataNode可以配置多个引用地址（DataSource），当主DataSource被检测为不可用时，系统会自动切换到下一个可用的DataSource上，这里的DataSource即可认为是Mysql的主从服务器的地址。

**MyCAT逻辑库**

与任何一个传统的关系型数据库一样，**MyCAT**也提供了“数据库”的定义，并有用户授权的功能，下面是**MyCAT**逻辑库相关的一些概念：

**· schema**:逻辑库，与MySQL中的Database（数据库）对应，一个逻辑库中定义了所包括的Table。

**· table**：表，即物理数据库中存储的某一张表，与传统数据库不同，这里的表格需要声明其所存储的逻辑数据节点DataNode，这是通过表格的分片规则定义来实现的，table可以定义其所属的“子表(childTable)”，子表的分片依赖于与“父表”的具体分片地址，简单的说，就是属于父表里某一条记录A的子表的所有记录都与A存储在同一个分片上。

**· 分片规则**：是一个字段与函数的捆绑定义，根据这个字段的取值来返回所在存储的分片（DataNode）的序号，每个表格可以定义一个分片规则，分片规则可以灵活扩展，默认提供了基于数字的分片规则，字符串的分片规则等。

**· DataNode**:** MyCAT**的逻辑数据节点，是存放table的具体物理节点，也称之为分片节点，通过DataSource来关联到后端某个具体数据库上，一般来说，为了高可用性，每个DataNode都设置两个DataSource，一主一丛，当主节点宕机，系统自动切换到从节点。

**· DataSource**：定义某个物理库的访问地址，用于捆绑到Datanode上。

**MyCAT**目前通过配置文件的方式来定义逻辑库和相关配置：

· MYCAT_HOME/conf/schema.xml中定义逻辑库，表、分片节点等内容

· MYCAT_HOME/conf/rule.xml中定义分片规则

· MYCAT_HOME/conf/server.xml中定义用户以及系统相关变量，如端口等。

下图给出了**MyCATd **一个可能的逻辑库到物理库（Mysql的完整映射关系），可以看出其强大的分片能力以及灵活的Mysql集群整合能力。

**分片策略**

**MyCAT**支持水平分片与垂直分片：

· 水平分片：一个表格的数据分割到多个节点上，按照行分隔。

· 垂直分片：一个数据库中多个表格A，B，C，A存储到节点1上，B存储到节点2上，C存储到节点3上。

**MyCAT**通过定义表的分片规则来实现分片，每个表格可以捆绑一个分片规则，每个分片规则指定一个分片字段并绑定一个函数，来实现动态分片算法。以常用的基于整数映射的分片函数org.MyCAT.route.function.PartitionByFileMap为例，此函数通过一个配置文件来确定映射关系，以下面的sharding-by-intfile这个分片规则为例：

```java
<tableRule name="sharding-by-intfile">

<rule>

<columns>sharding_id</columns>

<algorithm>hash-int</algorithm>

</rule>

</tableRule>

<tableRule name="auto-sharding-long">

<rule>

<columns>id</columns>

<algorithm>rang-long</algorithm>

</rule>

</tableRule>

<function name="hash-int" class="org.MyCAT.route.function.PartitionByFileMap">

<property name="mapFile">partition-hash-int.txt</property>

</function>

<function name="rang-long" class="org.MyCAT.route.function.AutoPartitionByLong">

<property name="mapFile">autopartition-long.txt</property>

</function>partition-hash-int.txt的文件如下：

10000=0

10010=1
```

表明当字段**sharding_id**取值为10000的时候，返回分片节点ID为0，以此类推。

Schema.xml中定义**customer**表的分片规则为此规则：

```java
<table name="customer"  dataNode="dn1,dn2" rule="sharding-by-intfile" />
```


于是**customer**按照字段**sharding_id**进行水平分片，分片存储在两个数据节点dn1,dn2上。

如何知道某个SQL在哪个分片上执行？ 用explain sql语句：

```java
explain select * from customer where sharding_id=10000
```

根据业务场景和数据特点，可以选用以下的分片规则：

```java
**· auto-sharding-long**  主键自动增长的数字，按照范围进行自动分片，比如0-200万的数据在分片节点0,200-400万的数据在分片节点2，依次类推，根据数据库服务器的性能，可以每个分片存储100-500条记录之间，此种方式，每个分片表一个独立的自增长ID机制，确保记录的连续性。conf/ autopartition-long.txt中定义了分段范围与分片ID的关系。

**· sharding-by-intfile**，表中有字段sharding_id，其类型为整数，对应具体的业务含义，比如10000对应电信，10010对应联通，此外，按照省份编码进行定义，也是可行的方式，为了效率，编码被映射为数字而不是字符串，conf/ partition-hash-int.txt, 定义了某个整数值到某个分片id的映射关系。

**· mod-long，**对某些表，我们基本上很少会涉及到范围查询的，只根据某个字段（最常见是主键）进行查找定位，则可以用求余的方式，随机分配到其中一个节点上。

所有的分片规则都在rule.xml中定义，不同的表根据需求，定义不同的分片规则。

对于某些不分片的表格，或者分片规则一样的表格，table的定义可以用简化的方式来写,如：<table name="**customer,product**"  rule="auto-sharding-long" />  。对于此种方式，name中定义的这些表格具有相同的属性，并且都不能有childTable 元素。
```

**基于E-R关系分片策略**

传统的数据库分片方式都是基于单个表格，对于表关联这种操作，则很难处理，考虑下面的分片模型,customer与 orders分片在不同节点上，orders的 parent_id字段存放父表customer的主键：

为了能够执行customer与orders的联合查询，意味着分片表的数据必须要跨节点进行网络传输，以上图为例：

· DN1节点上的orders表JOIN时候需要DN1和DN2的节点

· DN2节点上的orders表JOIN时候需要DN1和DN3的节点

· DN3节点上的orders表JOIN时候需要DN1、DN2、DN3的节点

目前这种方式的JOIN，业界没有很好的解决办法，而且实现起来都很复杂，性能也达不到企业应用开发的要求。

**MyCAT**借鉴了NewSQL领域的新秀Foundation DB的设计思路，Foundation DB创新性的提出了Table Group的概念，其将子表的存储位置依赖于主表，并且物理上紧邻存放，因此彻底解决了JION的效率和性能问题，根据这一思路，提出了基于E-R关系的数据分片策略，子表的记录与所关联的父表记录存放在同一个数据分片上。

以上述例子为例，schema.xml中定义如下的分片配置：

<table name="**customer**" dataNode="dn1,dn2" rule="sharding-by-intfile">

<childTable name="**orders**"  joinKey="customer_id" parentKey="id"/>

</table>

**customer**采用sharding-by-intfile这个分片策略，分片在dn1,dn2上，**orders**依赖父表进行分片，两个表的关联关系为orders.customer_id=customer.id。于是数据分片和存储的示意图如下：

这样一来，分片Dn1上的的customer与Dn1上的orders就可以进行局部的JOIN联合，Dn2上也如此，再合并两个节点的数据即可完成整体的JOIN，试想一下，每个分片上orders表有100万条，则10个分片就有1个亿，基于E-R映射的数据分片模式，基本上解决了80%以上的企业应用所面临的问题。

多对多的表格如何处理？多对多的表格通常情况下，有以下几种：

· 主表+关系表+字典表

· 主表A+关系表+主表B

对于第一种，字典表可以被定义为“全局表”，字典表的记录规模可以在几千到几十万之间，基本是变动比较少的表，由MyCAT自动实时同步到所有分片，这样就可以三个表都做JOIN操作了。

对于第二种，需要从业务角度来看，关系表更偏向哪个表，即“A的关系”还是“B的关系”，来决定关系表跟从那个方向存储。目前还暂时无法很好支持这种模式下的的3个表之间的关联。未来版本中将考虑将中间表进行双向复制，以实现从A-关系表 以及B-关系表的双向关联查询。

关于全局表的实现方式，全局表在数据插入或更新的时候，会自动在全局表定义的所有数据节点上执行相同的操作，以保证所有数据节点都一致，由于这个特性，全局表可以跟任何分片或不分片的表格进行JOIN操作。对数据更新不频繁的，规模不是很大的（100万之内）的表都可以定义为**MyCAT**的全局表，以实现用存储换性能的目标。

**主键分片VS非主键分片**

主键分片还是非主键分片，这个问题并不是很难，当你没人任何字段可以作为分片字段的时候，主键分片就是唯一选择，其优点是按照主键的查询最快，当采用自动增长的序列号作为主键时，还能比较均匀的将数据分片在不同的节点上。

若有某个合适的业务字段比较合适作为分片字段，则建议采用此业务字段分片，选择分片字段的条件如下：

· 尽可能的比较均匀分布数据到各个节点上

· 该业务字段是最频繁的或者最重要的查询条件

常见的除了主键之外的其他可能分片字段有“订单创建时间”、店铺类别或所在省等。当你找到某个合适的业务字段作为分片字段以后，不必纠结于“牺牲了按主键查询记录的性能”，因为在这种情况下，MyCAT提供了“主键到分片”的内存缓存机制，热点数据按照主键查询，丝毫不损失性能。做法如下：

对于非主键分片的TABLE，填写属性primaryKey，此时MyCAT会将你根据主键查询的SQL语句的第一次执行结果进行分析，确定该Table 的某个主键在什么分片上，并进行主键到分片ID的缓存，以下面SQL为例，由于id 不是orders的分片字段，因此这个SQL第一次会发送给所有分片去执行：

select * from orders where id=1;

执行完成以后：

在缓存TableID2DataNodeCache.TESTDB_ORDERS中放入一条信息，key为主键的值，value为分片ID，当我们再次执行上述语句，MyCAT就直接将SQL发往dn2了：

对于多个主键的查询，一样可以自动优化：如 Select * from orders where id in (1,2,3)  ，则会分别存储1、2、3这三个主键到分片的缓存关系。

设想下，每个表有5000万数据，10%的热点数据经常按照主键查询，5000万*10%=500万，缓存上述信息大概需要1.5G内存，通过分析缓存使用信息，就可以最精确的调优这笔缓存的内存。通过连接MyCAT的9066管理端口，执行show @@cache，可以显示当前缓存的使用情况：

更多内容，参照MyCAT性能调优手册。

**SQL 99规范**

MYCAT支持SQL 99规范，包括DDL语句的支持，部分MYSQL特定的语法并不支持，但MYCAT 1.2通过了一个特殊方式来解决特殊SQL的问题，即通过MYSQL注解方式，以下面的SQL语句为例：

/*!mycat:sql=select id from travelrecord where id=2*/ select * from travelrecord where id=2;

其中/*! Xxxx */为MYSQL 特殊注解语法的格式，注解内以mycat开头，说明是mycat处理的注解，这里放置一个符合SQL 99的SQL语句，用来告诉MYCAT，用此语句进行语法解析和路由分析，然后将注释后面的真正的SQL select * from travelrecord where id=2提交到匹配的路由上执行，并返回结果。

比如MyCAT并不支持mysql的select into语法，若select into语法涉及到的表是不分片的，则可以如下来写注释，让此SQL能执行通过：

/*!mycat:sql=insert into B*/ select * from A insert into B

备注：后续版本注解格式修改为 /*!mycat: sql = select id from travelrecord where id=2*/ select * from travelrecord where id=2;

Mycat 1.3开始，支持Druid的解析器，可以配置选择Druid或者Foundation DB解析器，建议选择Druid解析器，未来可能取消Foundation DB解析器的支持，Druid解析器更好的支持Mysql的特殊语法，性能有明显优势。

在server.xml中配置如下参数，可以切换到Druid解析器：

```java
<mycat:server xmlns:mycat="http://org.opencloudb/">

<system>

<property name=”defaultSqlParser” value=”druidparser”/>

</system>
```

**MyCAT全局表**

一个真实的业务系统中，往往存在大量的类似字典表的表格，它们与业务表之间可能有关系，这种关系，可以理解为“标签”，而不应理解为通常的“主从关系”，这些表基本上很少变动，可以根据主键ID进行缓存，下面这张图说明了一个典型的“标签关系”图：** **

在分片的情况下，当业务表因为规模而进行分片以后，业务表与这些附属的字典表之间的关联，就成了比较棘手的问题，考虑到字典表具有以下几个特性：

· 变动不频繁

· 数据量总体变化不大

· 数据规模不大，很少有超过数十万条记录。

鉴于此，**MyCAT**定义了一种特殊的表，称之为“全局表”，全局表具有以下特性：

· 全局表的插入、更新操作会实时在所有节点上执行，保持各个分片的数据一致性

· 全局表的查询操作，只从一个节点获取

· 全局表可以跟任何一个表进行JOIN操作

将字典表或者符合字典表特性的一些表定义为全局表，则从另外一个方面，很好的解决了数据JOIN的难题。通过全局表+基于E-R关系的分片策略，**MyCAT**可以满足80%以上的企业应用开发。

全局表配置比较简单，不用写Rule规则，如下配置即可：

<table name="company" primaryKey="ID" type="global" dataNode="dn1,dn2,dn3" />

需要注意的是，全局表每个分片节点上都要有运行创建表的DDL语句。

**高可用性以及读写分离**

MyCAT的读写分离机制如下：

**· 事务**内的SQL，全部走**写节点**，除非某个select语句以注释/*balance*/开头

**· 自动提交**的select语句会走**读节点**，并在所有可用读节点中间随机负载均衡

· 当某个主节点宕机，则其全部**读节点**都不再被使用，因为此时，同步失败，数据已经不是最新的，MYCAT会采用另外一个**主节点**所对应的全部**读节点**来实现select负载均衡。

· 当所有主节点都失败，则为了系统高可用性，自动提交的所有select语句仍将提交到全部存活的读节点上执行，此时系统的很多页面还是能出来数据，只是用户修改或提交会失败。

MyCAT的读写分离的配置如下：

dataHost的balance属性设置为：

· 0，不开启读写分离机制

· 1，全部的readHost与stand by writeHost参与select语句的负载均衡，简单的说，当双主双从模式(M1->S1，M2->S2，并且M1与 M2互为主备)，正常情况下，M2,S1,S2都参与select语句的负载均衡。

· 2，所有的readHost与writeHost都参与select语句的负载均衡，也就是说，当系统的写操作压力不大的情况下，所有主机都可以承担负载均衡。

一个dataHost元素，表明进行了数据同步的一组数据库，**DBA需要保证这一组数据库服务器是进行了数据同步复制的**。writeHost相当于Master DB Server，而旗下的readHost则是与从数据库同步的Slave DB Server。当dataHost配置了多个writeHost的时候，任何一个writeHost宕机，Mycat 都会自动检测出来，并尝试切换到下一个可用的writeHost。

MyCAT支持高可用性的企业级特性，根据您的应用特性，可以配置如下几种策略：

· 后端数据库配置为一主多从，并开启读写分离机制。

· 后端数据库配置为双主双从（多从），并开启读写分离机制

· 后端数据库配置为多主多从，并开启读写分离机制

后面两种配置，具有更高的系统可用性，当其中一个写节点（主节点）失败后，Mycat会侦测出来（心跳机制）并自动切换到下一个写节点，**MyCAT在任何时候，只会往一个写节点写数据。**

下面是典型的双主双从的Mysql集群配置：

Log4j.xml中配置日志输出级别为debug时，当选择节点的时候，会输出如下日志：

```java
16:37:21.660  DEBUG [Processor0-E3] (PhysicalDBPool.java:333) -select read source hostM1 for dataHost:localhost1

16:37:21.662  DEBUG [Processor0-E3] (PhysicalDBPool.java:333) -select read source hostM1 for dataHost:localhost1
```

根据这个信息，可以确定某个SQL发往了哪个读（写）节点，据此可以分析判断是否发生了读写分离。

**全局序列号**

全局序列号是MyCAT提供的一个新功能，为了实现分库分表情况下，表的主键是全局唯一，而默认的MySQL的自增长主键无法满足这个要求。全局序列号的语法符合标准SQL规范，其格式为：

next value for MYCATSEQ_GLOBAL

其中MYCATSEQ_GLOBAL是序列号的名字，MyCAT自动创建新的序列号，免去了开发的复杂度，另外，MyCAT也提供了一个全局的序列号，名称为：MYCATSEQ_GLOBAL。

**注意，MYCATSEQ_必须大写才能正确识别。**

MyCAT温馨提示：实践中，建议每个表用自己的序列号，序列号的命名建议为MYCATSEQ _tableName_ID_SEQ。

SQL中使用说明

自定义序列号的标识为：MYCATSEQ_XXX ,其中XXX为具体定义的sequence的名称，应用举例如下：

```java
使用默认的全局sequence :

insert into tb1(id,name) values(next value for MYCATSEQ_GLOBAL,'micmiu.com');

使用自定义的  sequence :

insert into tb2(id,name) values(next value for MYCATSEQ_MY1,'micmiu.com');

获取最新的值

Select next value for  MYCATSEQ_xxx
```

MyCAT目前已经提供了一个本地配置版的实现，下面是配置说明：

配置说明

配置文件：sequence_conf.properties

格式说明：

```java
XXX.HISIDS= 1-100,501-800,3001-5000 //使用过得历史分段

XXX.MINID=10001 //当前可用分段的最小值

XXX.MAXID=20000 //当前可用分段的最大值

XXX.CURID=10000 //当前可用分段的当前值

全局sequence配置如下：

GLOBAL.HISIDS=

GLOBAL.MINID=1

GLOBAL.MAXID=50000

GLOBAL.CURID=10000

自定义sequence配置如下：

MY1.HISIDS=

MY1.MINID=101

MY1.MAXID=200

MY1.CURID=152
```

Mysql数据库表格保存全局序列号的配置如下：

Serfver.xml中启用，<property name="sequnceHandlerType">1</property>• 在某个分区(dataNode)数据库上创建序列号相关的表格和函数，SQL脚本在doc目录下的sequnce-sql.txt中，需要在数据库上而非Mycat上执行。• Mycat_home/conf/quence_db_conf.properties 中记录了sequnce所存放的db对应的配置信息。#sequence stored in datanodeGLOBAL=dn1COMPANY=dn1CUSTOMER=dn1• 在sequnce表中，插入相应的sequnce记录，并确定其初始值，以及增长步长，步长建议一个合适的范围，比如50-500，需要在数据库上而非Mycat上执行。INSERT INTO MYCAT_SEQUENCE VALUES ('GLOBAL', 0, 100);• 修改sequnce的当前值为某个新值，需要在数据库上而非Mycat上执行。SELECT mycat_seq_curval('GLOBAL');

提示：步长选择多大，取决与你数据插入的TPS，假如是每秒1000个，则步长为1000×60=6万，也不是很大，即60秒会重新从数据库读取下一批次的序列号值。

**自增长主键**

从MyCAT 1.3开始，支持自增长主键，依赖于全局序列号机制，建议采用数据库方式的全局序列号，并正确设置步长，以免影响实际性能。

首先要开启数据库方式的全局序列号，对于需要定义自增长主键的表，建立对应的全局序列号，与table名称同名大写，如customer序列名为CUSTOMER，然后再 schema.xml 中对customer表的table元素增加属性autoIncrement值为true.

```java
<table name=”CUSTOMER”  autoIncrement=”true”>

执行insert into customer (name,company_id,sharding_id) values ('test',2,10000);查看效果， 暂不支持主键为null如：insert into customer (id,name,company_id,sharding_id) values (null,'test',2,10000);
```

**JDBC方式支持其他数据库**

从MyCAT 1.2开始，实现了JDBC通用方式连接后端其他数据库，如Oracle、SQL Server、DB2等，在客户端，仍然可以把MyCAT视作是一个MySQL服务器。

配置方式如下，首先将符合JDBC 4标准的驱动JAR包放到MYCAT\lib下，注意检查驱动JAR包中包括如下目录结构的文件： META-INF\services\java.sql.Driver

文件内容为驱动的类名：

```java
schema.xml中如下定义JDBC的DateHost：

<dataHost name="jdbchost" maxCon="1000" minCon="10" balance="0"

dbType="mysql" **dbDriver**="**jdbc**">

<heartbeat>select user()</heartbeat>

<writeHost host="hostM1" **url**="jdbc:mysql://localhost:3306"

user="root" password="123456">

</writeHost>

</dataHost>
```

**NoSQL支持**

1.3开始支持NoSQL数据库通过SQL方式访问，目前试验性的支持MongoDB，未来会增加更多NoSQL数据库，具体配置参照相关文档。

**MyCAT配置**

Server.xml里面定义系统参数、用户权限，Mycat 目前支持只读与读写两种权限，readOlny表示只读权限。

```java
<user name=*"test"*>

<property name=*"password"*>test</property>

<property name=*"schemas"*>TESTDB</property>

<property name=*"readOnly"*>true</property>

</user>
```

**SQL拦截**

SQL拦截是一个比较有用的高级技巧，用户可以写一个java类，将传入MyCAT的SQL进行改写然后交给Mycat去执行，此技巧可以完成如下一些特殊功能：

· 捕获和记录某些特殊的SQL

· 处于性能优化的考虑，改写SQL，比如改变查询条件的顺序或增加分页限制

· 将某些Select SQL强制设置为Read 模式，走读写分离（很多事务框架很难剥离事务中的Select SQL

· 其他。。。。

用法是在Server.xml中配置系统参数，指定自己的SQL拦截器的Java实现类：

```java
<system>

<property name=*"* sqlInterceptor*"*>org.opencloudb.interceptor.impl.DefaultSqlInterceptor</property>

</system>
```

默认的拦截器实现了Mysql转义字符的过滤转换，SQL拦截器的实现很简单：

```java
/**

* escape mysql escape letter

*/

@Override

public String interceptSQL(String sql, int sqlType) {

if (sqlType == ServerParse.UPDATE || sqlType == ServerParse.INSERT||sqlType == ServerParse.SELECT||sqlType == ServerParse.DELETE) {

return sql.replace("\\'", "''");

} else {

return sql;

}

}
```

**Catlet**

Mycat 1.3开始支持Java类编程方式实现复杂SQL处理，类似数据库的存储过程，Catlet是一个实现了Catlet接口的**无状态Java类**，负责将编码实现某个SQL的处理过程，并返回响应报文给客户端，目前主要用于人工智能（非AI）编码实现跨分片SQL的处理逻辑，Demo中附带143行完成两个表JION的查询示例，采用流式处理机制，未来将会提供更多高质量API来简化跨分片复杂SQL的编程问题，下个版本有望实现不带子查询的两表关联查询自动处理，也采用此框架。

```java
**package** org.opencloudb.sqlengine;

/**

* mycat catlet ,used to execute sql and return result to client,some like

* database's procedure.

* must implemented as a stateless class and can process many SQL concurrently

*

* **@author** wuzhih

*

*/

**public** **interface** Catlet {

/*

* execute sql in EngineCtx and return result to client

*/

**void** processSQL(String sql, EngineCtx ctx);
```

Catlet 编写完成并编译通过以后，必须放在Mycat_home/catlets目录下，系统会动态加载相关class（**需要按照Java Class的目录结构存放，比如com\hp\catlet\XXXCatlet.class，目前还不支持Jar文件**）并每隔1分组扫描一次文件是否更新，若更新则自动重新加载，因此无需重启服务，下面的截图对应的是demo.catletes.MyHellowJion这个Catlet的目录结构和所有相关类的位置。

在Mysql命令行连接Mycat Server后，执行带Catlet注解的SQL，则启动具体的Catlet完成SQL的解析，如下面的例子，表明select a.*, b.title from travelrecord a ,hotnews b where a.id=b.id 这个SQL交给demo.catlets.MyHellowJoin来处理。

/*!mycat:catlet=demo.catlets.MyHellowJoin */select a.*, b.title from travelrecord a ,hotnews b where a.id=b.id

想要运行上述Demo，可以将demo.catletes.MyHellowJion编译好，并将Class放入指定的目录，执行上述SQL。此外Demo源码存在于demo.catlets目录下，这部分是属于Mycat开发，具备Java开发能力并有这方面需求的同学，可以参考另一片文章《MyCAT人工智能解决跨分片SQL》了解详情。

**MyCAT高可用性方案**

HAProxy或者MyCAT  Cluster做负载均衡，后端一组MyCAT Server，MyCAT Server之后的MySQL 数据库可以有以下两种选择：

· MYSQL主从复制，当主节点失败，自动切换到从节点写数据。

· galera for mysql集群，percona-cluster或者mariadb cluster

MyCAT与percona-cluster配合，schema.xml配置如下：

```java
<dataHost name=*"localhost1"* maxCon=*"1000"* minCon=*"10"* balance=*"0"*

**writeType**=*"1"* dbType=*"mysql"* dbDriver=*"native"*>

<heartbeat>select user()</heartbeat>

<writeHost host=*"hostM1"* url=*"localhost:3306"* user=*"root"* password=*"123456"/*>

<writeHost host="hostM2" url="localhost:3317" user="root" password="123456"/>

<writeHost host="hostM3" url="localhost:3319" user="root" password="123456"/>

</dataHost>
```

有几个percona-cluster节点，writeHost就写几个，同时**writeType必须设为1，这种模式下，没有readHost.**

**当任何一个**writeHost失败，会自动排除，恢复以后，自动加入写节点。

**快速上手**

是用Java开发，需要有JAVA运行环境，若本机没有，则需要下载安装，需要64位的JDK7以及JDK8版本才能运行：

[http://www.java.com/zh_CN/](http://www.java.com/zh_CN/)

获取**MyCAT的**最新开源版本，项目主页[https://github.com/MyCATApache/](https://github.com/MyCATApache/)

二进制包下载地址：

[https://github.com/MyCATApache/Mycat-download](https://github.com/MyCATApache/Mycat-download)

文档地址

[https://github.com/MyCATApache/Mycat-doc](https://github.com/MyCATApache/Mycat-doc)

windows下可以下载Mycat-server-xxxx.ZIP，linux下可以下载tar.gz解开在某个目录下，注意，目录不能有空格，在Linux(Unix)下，建议放在/usr/local/MyCAT目录下，如下面类似的：

下面是修改MyCat用户的密码方式（仅供参考）

目录解释如下：

Bin 程序目录，存放了window版本和linux版本，除了提供封装成服务的版本之外，也提供了nowrap的shell脚本命令，方便大家选择和修改，进入到bin目录：

· Windows 下 运行: mycat.bat  console 在控制台启动程序，也可以装载成服务，若此程序运行有问题，也可以运行startup_nowrap.bat，确保java命令可以在命令执行。

· Linux下运行：mycat  console,首先要chmod +x *

Warp方式的命令，可以安装成服务并启动或停止。

· mycat install (可选)

· mycat start

**注意，wrap方式的程序，其JVM配置参数在conf/wrap.conf中，可以修改为合适的参数，参数调整参照**[**http://wrapper.tanukisoftware.com/doc/english/properties.html**](http://wrapper.tanukisoftware.com/doc/english/properties.html)**。****用下面是一段实例：**

**# Java Additional Parameters**

**wrapper.java.additional.5=-XX:MaxDirectMemorySize=2G**

**wrapper.java.additional.6=-Dcom.sun.management.jmxremote**

**# Initial Java Heap Size (in MB)**

**wrapper.java.initmemory=2048**

**# Maximum Java Heap Size (in MB)**

**wrapper.java.maxmemory=2048**

**若启动报内存不够，可以试着将上述内存都改小，改为1G或500M。**

Conf目录下存放配置文件，server.xml是Mycat服务器参数调整和用户授权的配置文件，schema.xml是逻辑库定义和表以及分片定义的配置文件，rule.xml是分片规则的配置文件，分片规则的具体一些参数信息单独存放为文件，也在这个目录下，配置文件修改，需要重启Mycat或者通过9066端口reload。

日志存放在logs/mycat.log中，每天一个文件，日志的配置是在conf/log4j.xml中，根据自己的需要，可以调整输出级别为debug，debug级别下，会输出更多的信息，方便排查问题。

建议本地有一个Mysql Server，若没有，建议安装一个，下载地址：

[http://dev.mysql.com/downloads/mysql/5.5.html#downloads](http://dev.mysql.com/downloads/mysql/5.5.html#downloads)

启动Mysql，确保能正常登录访问数据，msyql命令行工具mysql\bin\mysql.exe建议加入PATH路径中，为了方便使用。

用命令行工具或图形化客户端，连接MYSQL，创建DEMO所用三个分片数据库；

CREATE database db1;

CREATE database db2;

CREATE database db3;

注意：若是LINUX版本的MYSQL，则需要设置为Mysql大小写不敏感，否则可能会发生表找不到的问题。

**在MySQL的配置文件中my.ini [mysqld] 中增加一行**

**lower_case_table_names = 1**

编辑MYCAT_HOME/conf/schema.xml文件，修改dataHost对应的连接信息：

**注意writeHost/readHost中的location,user,password的值符合你所采用的Mysql的连接信息。dataHdataHost元素的name**不是主机名(hostname)，只是一个代号，用来区分不同的机器，writeHost/readHostt元素中的host属性也同样不是主机名，url  中的“localhost:3306”这部分才是主机名或者主机IP地址。

修改完成后保存，进入到MYCAT_HOME/bin目录下，执行启动命令：startup_nowrap.bat 或者mycat console) ，启动成功以后显示如下信息：

注意，默认数据端口为8066，管理端口为9066。

客户端也可以用图形化的客户端如：mysqlworkbench、 navicat 、以及一些基于Java的数据库客户端来访问，注意要填写端口号8066，以及database 为TESTDB。

命令行运行：mysql -utest -ptest -h127.0.0.1 -P8066 -DTESTDB  就能访问OpenCloudDB了，**以下操作都在此命令行里执行**（JDBC则将mysql的URL中的端口3306改为8066即可）

**提示：访问MyCAT的用户账号和授权信息是在conf/server.xml文件中配置，而MyCAT用来连接后端MySQL库的用户名密码信息则在conf/schema.xml中，这是两套完全独立的系统，类似的还有MyCAT的逻辑库(schema)，逻辑表（table）也是类似的。**

Employee表，是根据规则sharding-by-intfile （分片字段为sharding_id）进行分片。创建employee表：输入如下SQL

create table employee (id int not null primary key,name varchar(100),sharding_id int not null);

运行explain指令，查看该SQL被发往哪些分片节点执行：

explain** **create table employee (id int not null primary key,name varchar(100),sharding_id int not null);

建议参照schema.xml中employee表的定义，以及其分片规则，来看看什么数据会出现在dn1上，什么数据会出现在dn2上。

**温馨提示：explain可以用于任何正确的SQL上，其作用是告诉你，这条SQL会路由到哪些分片节点上执行，这对于诊断分片相关的问题很有帮助。另外，explain可以安全的执行多次，它仅仅是告诉你SQL的路由分片，而不会执行该SQL。**

插入数据：

insert into employee(id,name,sharding_id) values(1,'leader us',10000);

insert into employee(id,name,sharding_id) values(2, 'me',10010);

insert into employee(id,name,sharding_id) values(3, 'mycat',10000);

insert into employee(id,name,sharding_id) values(4, 'mydog',10010);

company表是根据规则auto-sharding-long（主键范围）进行分片。创建company表：输入如下SQL

create table company(id int not null primary key,name varchar(100));

录入数据：

insert into company(id,name) values(1,'hp');

insert into company(id,name) values(2,'ibm');

insert into company(id,name) values(3,'oracle');

你会看到三个分片上都插入了3条数据，因为company定义为全局表，用explain来确认这个情况：

explain insert into company(id,name) values(1,'hp')

返回3个节点的信息：

| DATA_NODE | SQL                                         |

+-----------+---------------------------------------------+

| dn1       | insert into company(id,name) values(1,'hp') |

| dn2       | insert into company(id,name) values(1,'hp') |

| dn3       | insert into company(id,name) values(1,'hp') |

+-----------+---------------------------------------------+

创建客户表：

create customer:    create table customer(id int not null primary key,name varchar(100),company_id int not null,sharding_id int not null);

插入数据：

insert into customer (id,name,company_id,sharding_id )values(1,'wang',1,10000);  //stored in db1;

insert into customer (id,name,company_id,sharding_id )values(2,'xue',2,10010);  //stored in db2;

insert into customer (id,name,company_id,sharding_id )values(3,'feng',3,10000); //stored in db1;

查询结果：

Select * from  customer;

explain Select * from  customer;  （确认数据是分片存储）

创建表格orders，并插入数据：

```java
create table orders (id int not null primary key ,customer_id int not null,sataus int ,note varchar(100) );

insert into orders(id,customer_id) values(1,1); //stored in db1 because customer table with id=1 stored in db1

insert into orders(id,customer_id) values(2,2); //stored in db2 because customer table with id=1 stored in db2

explain insert into orders(id,customer_id) values(2,2);

select customer.name ,orders.* from customer ,orders where customer.id=orders.customer_id;
```

travelrecord根据ID主键的范围进行分片：

```java
create travelrecord: create table travelrecord (id bigint not null primary key,user_id varchar(100),traveldate DATE, fee decimal,days int);

insert into travelrecord (id,user_id,traveldate,fee,days) values(1,'wang','2014-01-05',510.5,3);

explain insert into travelrecord (id,user_id,traveldate,fee,days) values(2000001,'wang','2014-01-05',510.5,3); 这个ID就存放在分片2上了
```

看到支持跨分片的JOIN！

热点新闻，用取摸的方式随机分配到dn1,dn2,dn3上

```java
create table hotnews(id int  not null primary key ,title varchar(400) ,created_time datetime);

插入数据

insert into hotnews(id,title,created_time) values(1,'first',now()); 在分片1上

而Id为5，则到dn3上，5%3=2 ,即对应dn3的 index

其他：

goods表

create table goods(id int not null primary key,name varchar(200),good_type tinyint,good_img_url  varchar(200),good_created date,good_desc varchar(500), price double);一起探索MyCAT的奇妙新世界吧！ QQ群：106088787
```

**管理监控：**

MyCAT自身有类似其他数据库的管理监控方式，通过Mysql命令行，登录管理端口（9066）执行相应的SQL，进行管理

mysql -utest -ptest -P9066

show @@help; 此命令会显示所有的管理监控命令，另外请参照《Mycat命令行监控指南.docx》这个文档来深入了解。

**欢迎有志于大数据、分布式计算、数据库算法和优化等方面的大侠加入。**

附： MyCAT 1.0GA 版与Cobar 1.2.7最新版的对比

另外,MyCAT修复了众多Cobar的BUG还做了很多优化，以下是比较重要的一部分：

· Mysql连接数过大，拒绝连接后，Cobar报错,indexoutof bound，导致难以排查故障原因

· 当前活跃连接数和空闲连接数的计算存在BUG

· 当某些SQL执行比较慢，会导致Cobar卡死，可以用select  sleep(300)  from anytalbe，此SQL执行不到一百个，

就导致Cobar假死，无法响应新的请求

· 在某些情况下，后端连接得不到释放，另外，Cobar没有控制后端总数，当高并发的情况下，会创建更多连接，

导致数据库压力增大，系统可靠性降低。



