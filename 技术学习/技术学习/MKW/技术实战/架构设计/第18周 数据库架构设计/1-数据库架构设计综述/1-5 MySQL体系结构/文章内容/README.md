---
title: 文章内容
---

# 文章内容

### **9. InnoDB通用**[**表空间**](https://so.csdn.net/so/search?q=%E8%A1%A8%E7%A9%BA%E9%97%B4&spm=1001.2101.3001.7020)

```sql
通用表空间是InnoDB 使用CREATE TABLESPACE语法创建的共享表空间。本节中的以下主题描述了常规表空间功能和功能：

通用表空间功能

创建通用表空间

将表添加到通用表空间

通用表空间行格式支持

使用ALTER TABLE在表空间之间移动非分区表

通用表空间表分区支持

使用ALTER TABLE在表空间之间移动表分区

删除通用表空间

通用表空间的限制

9.1 通用表空间功能
与系统表空间类似，通用表空间是可以存储多个表的数据的共享表空间。

与单独表空间相比，通用表空间具有潜在的内存优势。在表空间的生命周期内，服务器将表空间元数据保存在内存中。通用表空间中的多个表对于表空间元数据消耗的内存要少于单独表空间中的相同数量的表

通用表空间数据文件可以放在相对于MySQL数据目录或独立于MySQL数据目录的目录中，该目录提供了单独表空间的许多数据文件和存储管理功能 。与单独表空间一样，将数据文件放在MySQL数据目录之外的功能允许您分别管理关键表的性能，为特定表设置RAID或DRBD，或者将表绑定到特定磁盘。

通用表空间支持Antelope和Barracuda文件格式，因此支持所有表格行格式和相关功能。由于支持这两种文件格式，通用表空间不依赖于 innodb_file_format或 innodb_file_per_table 设置，这些变量也不会对一般表空间产生任何影响。

该TABLESPACE选项可用于 CREATE TABLE在通用表空间，单独表空间或系统表空间中创建表。

该TABLESPACE选项可用于 ALTER TABLE在通用表空间，单独表空间和系统表空间之间移动表。以前，无法将表从单独表空间移动到系统表空间。使用常规表空间功能，您现在可以执行此操作。


9.2 创建通用表空间
使用CREATE TABLESPACE语法创建通用表空间
CREATE TABLESPACE tablespace_name
    ADD DATAFILE 'file_name'
    [FILE_BLOCK_SIZE = value]
        [ENGINE [=] engine_name]


例子：
1) 在MySQL数据目录中创建通用表空间
mysql> create tablespace `ts1` add datafile 'ts1.ibd' engine=InnoDB;

# cat /etc/my.cnf|grep datadir
datadir = /data/mysql/mysql3306/data

# cd /data/mysql/mysql3306/data/

# ls -l
...
-rw-r----- 1 mysql mysql      65536 Aug 13 14:05 ts1.ibd
...

2) 在MySQL数据目录之外的目录创建通用表空间
mysql> create tablespace `ts2` add datafile '/data/mysql3306_data/ts2.ibd' Engine=InnoDB;
如果外部目录是数据目录的子级，创建时会报错，例：
#为避免与隐式创建的单独表空间冲突，不支持在MySQL数据目录下的子目录中创建通用表空间。

mysql> create tablespace `ts3` add datafile '/data/mysql/mysql3306/data/mysql3306_data/ts3.ibd' Engine=InnoDB;
ERROR 3121 (HY000): Incorrect File Name '/data/mysql/mysql3306/data/mysql3306_data/ts3.ibd'.
注意
该ENGINE = InnoDB子句必须定义为CREATE TABLESPACE语句的一部分，或者默认存储引擎定义为InnoDB（default_storage_engine=InnoDB）。
9.3 将表添加到通用表空间
CREATE TABLE：
mysql> create table t2(c1 int primary key) tablespace ts1;
ALTER TABLE：
mysql> ALTER TABLE t1 TABLESPACE ts1;
9.4 通用表空间行格式支持
通用表空间支持所有行格式(REDUNDANT, COMPACT, DYNAMIC, COMPRESSED)。需要注意的是，由于物理页面大小不同，压缩和未压缩的表不能在同一个通用表空间中共存。

对于包含压缩表（ROW_FORMAT=COMPRESSED）的通用表空间， FILE_BLOCK_SIZE必须指定，并且该FILE_BLOCK_SIZE值必须是与该 值相关的有效压缩页大小 innodb_page_size。此外，压缩表（KEY_BLOCK_SIZE）的物理页面大小必须等于 FILE_BLOCK_SIZE/1024。例如，如果innodb_page_size=16k和 FILE_BLOCK_SIZE=8k，则KEY_BLOCK_SIZE 必须为8。

下表显示了允许 innodb_page_size， FILE_BLOCK_SIZE和 KEY_BLOCK_SIZE组合。FILE_BLOCK_SIZE值也可以以字节为单位指定。要确定KEY_BLOCK_SIZE 给定的有效值FILE_BLOCK_SIZE，请将 FILE_BLOCK_SIZE值除以1024.表压缩不支持32K和64K InnoDB页面大小。
```

[image](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/310ce482-76b9-45ee-a8c3-904d0ef130d2/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663AEVRP3A%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T231144Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIAcNSwNhKN4O5XidBAf5LL6QRXbJ3bxdSQQBKFUoqjOXAiEAhvRPppYZ8g49tQiYiMdkO%2Bual6iVu2FtIniEVgJtOR0qiAQIxv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDL%2F21zvsy3suK86l6SrcA7bqWWmZzbbv8V4WEbRzA5ePEZxVbsU5ZVBC8%2BrWPon4%2FOTO%2BmuqAB%2BqDdMM76odgZdRuP%2B3fhqj6t4vh5PfdKRNN4w3ui73NRqGivTjKhWPbJkXt3jwaCXPcvKy1sJE5UGHt4XV81pfSxDwJcOFEzbHLNCPmXzbAsr5BfPAZKeRPZEO9FXpYVyuWUWy5nqRtHTOndo2ThQfcFj1E%2BNtP0qrLJMrUuX1y7ObTTLRKH7k6664MXdF%2BxFXMrtSjLkC64XmFUmMJo2oRAfnd02U87%2BgwY%2BwA8dkBYVy%2FSHn0kWUWYgVQEbbVohUqHdiLle9U9wXWH4XUP7LoK%2FMIoB5XLeAUcq%2BAv1vhFkHwHQv0YT1JCQ6p%2F3q%2Bz723kgC9VMzJzVb0ty9ioZpTiD9SILCkwCoZzjfWJ1RTH4BU%2Fi%2BOtokb2aEuYiPxy8dVEFkBOHASKbcNm1TllCfBB3%2BzzHq8ZZbSNYAj3mWJZOO6spj5ujrCQ4sYzNUE7KQI4RYL5pIFs%2BLjo3KXsgy6AHIU9OEgdoEydeFiktFA%2FLEUaz6PDskiMeIXM7Un%2FyExpkniUbwQFxAyXZILGFTQTazBxo4HOiZuNv56vsZ9tC01pnCeiZM%2FEBXcpq%2F%2FTM04xVGMOu3%2F9IGOqUBmV9V7qLBQp1Xvq0DN7W3Xh02wnZMB5SkIZmZFWCGcj6%2F2htZBYK7H%2BNqsyHgOHJmdyx6bVO0OM1I8tN2Wq7%2BxMEIKLwD8YPME62TX%2Fhxyc6FG86pU8e%2FvoeUG2oUfDKWcS2xbRhlMYktecBq6ZFCwjt8KHHZBoFHlSzHj1ogZhf3rzKtsWIhXt22O5GxHkTm%2F3YBrCX6Erzx3HXhAJamDRo36iy1&X-Amz-Signature=b99bf63857114ef944a94e4bbff99b1fe49edb36b6d2aff23e21aeec10f3e83e&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

此示例演示如何创建通用表空间并添加压缩表。该示例假定默认 innodb_page_size值为16K。在 FILE_BLOCK_SIZE 为8k时，要求压缩表有8个KEY_BLOCK_SIZE

```sql
mysql> CREATE TABLESPACE `ts2` ADD DATAFILE 'ts2.ibd' FILE_BLOCK_SIZE = 8192 Engine=InnoDB;

mysql> CREATE TABLE t4 (c1 INT PRIMARY KEY) TABLESPACE ts2 ROW_FORMAT=COMPRESSED KEY_BLOCK_SIZE=8;
```

如果未指定FILE_BLOCK_SIZE创建通用表空间，则 FILE_BLOCK_SIZE默认为 innodb_page_size。当 FILE_BLOCK_SIZE等于 innodb_page_size，表空间可能只包含未压缩的行格式（COMPACT， REDUNDANT和DYNAMIC行格式）。

```sql
mysql> create tablespace `ts2` add datafile '/data/mysql3306_data/ts2.ibd' Engine=InnoDB;

mysql> CREATE TABLE t5 (c1 INT PRIMARY KEY) TABLESPACE ts2 ROW_FORMAT=COMPRESSED KEY_BLOCK_SIZE=8;
ERROR 1478 (HY000): InnoDB: Tablespace `ts2` cannot contain a COMPRESSED table
```

### **9.5 使用ALTER TABLE在表空间之间移动非分区表**

你可以使用alter table tablespace选项移动非分区 innodb表至通用表空间中，或者单独表空间，或者系统表空间。

移动单独表空间的非分区表或者系统表空间的非分区表到通用表空间中：

```sql
ALTER TABLE tbl_name TABLESPACE [=] tablespace_name
```

移动通用表空间的非分区表或者单独表空间的非分区表到系统表空间中：

```sql
ALTER TABLE tbl_name ... TABLESPACE [=] innodb_system
```

移动通用表空间的非分区表或者系统表空间的非分区表到单独表空间中：

```sql
ALTER TABLE tbl_name ... TABLESPACE [=] innodb_file_per_table
```

ALTER TABLE … TABLESPACE会导致全表重建，即使TABLESPACE属性没有从其先前的值更改。

ALTER TABLE … TABLESPACE 语法不支持将表从临时表空间移动到持久表空间。

DATA DIRECTORY 子句允许CREATE TABLE … TABLESPACE=innodb_file_per_table ，但不支持与TABLESPACE选项结合使用。

### **9.6 通用表空间分区表支持**

> 注意InnoDB从MySQL 5.7.24开始，不推荐 支持在共享表空间中放置表分区， 并且将在以后的MySQL版本中删除。共享表空间包括InnoDB 系统表空间和通用表空间。
TABLESPACE选项可用于将单个表分区或子分区分配给通用表空间，单独表空间，或者系统表空间。所有分区必须属于同一存储引擎。 以下示例说明了用法：

```sql
mysql> create tablespace ts1 add datafile 'ts1.ibd';
mysql> create tablespace ts2 add datafile 'ts2.ibd';


mysql> CREATE TABLE t1 (a INT, b INT) ENGINE = InnoDB
       PARTITION BY RANGE(a) SUBPARTITION BY KEY(b) (
        PARTITION p1 VALUES LESS THAN (100) TABLESPACE=`ts1`,
        PARTITION p2 VALUES LESS THAN (1000) TABLESPACE=`ts2`,
        PARTITION p3 VALUES LESS THAN (10000) TABLESPACE `innodb_file_per_table`,
        PARTITION p4 VALUES LESS THAN (100000) TABLESPACE `innodb_system`);


mysql> CREATE TABLE t2 (a INT, b INT) ENGINE = InnoDB
       PARTITION BY RANGE(a) SUBPARTITION BY KEY(b) (
        PARTITION p1 VALUES LESS THAN (100) TABLESPACE=`ts1`
          (SUBPARTITION sp1,
           SUBPARTITION sp2),
        PARTITION p2 VALUES LESS THAN (1000)
          (SUBPARTITION sp3,
           SUBPARTITION sp4 TABLESPACE=`ts2`),
        PARTITION p3 VALUES LESS THAN (10000)
          (SUBPARTITION sp5 TABLESPACE `innodb_system`,
           SUBPARTITION sp6 TABLESPACE `innodb_file_per_table`));
```

这里tablespace选项也支持ALTER TABLE：

```sql
mysql> ALTER TABLE t1 ADD PARTITION (PARTITION p5 VALUES LESS THAN (1000000) TABLESPACE = `ts1`);
```

```sql
【注意】
如果TABLESPACE = tablespace_name选项未定义，则ALTER TABLE … ADD PARTITION操作增加表分区指定默认的表空间，可以在CREATE TABLE或ALTER TABLE期间在表级别指定。

ALTER TABLE tbl_name TABLESPACE [=] tablespace_name 操作只修改分区表默认表空间。它不会移动分区表。但是，更改默认表空间后，如果未使用TABLESPACE [=] tablespace_name子句显式定义另一个表空间，则重建表的操作（例如使用ALGORITHM = COPY的ALTER TABLE操作）会将分区移动到默认表空间。
```

要验证分区是否已放置在指定的表空间中，可以查询INFORMATION_SCHEMA.INNODB_SYS_TABLES

```sql
mysql> select NAME,SPACE,SPACE_TYPE from information_schema.innodb_sys_tables where name like '%t1%';
+-----------------------+-------+------------+
| NAME                  | SPACE | SPACE_TYPE |
+-----------------------+-------+------------+
| test/t1#P#p1#SP#p1sp0 |   190 | General    |
| test/t1#P#p2#SP#p2sp0 |   191 | General    |
| test/t1#P#p3#SP#p3sp0 |   192 | Single     |
| test/t1#P#p4#SP#p4sp0 |     0 | System     |
| test/t1#P#p5#SP#p5sp0 |   190 | General    |
+-----------------------+-------+------------+
5 rows in set (0.00 sec)

mysql> select NAME,SPACE,SPACE_TYPE from information_schema.innodb_sys_tables where name like '%t2%';
+---------------------+-------+------------+
| NAME                | SPACE | SPACE_TYPE |
+---------------------+-------+------------+
| test/t2#P#p1#SP#sp1 |   190 | General    |
| test/t2#P#p1#SP#sp2 |   190 | General    |
| test/t2#P#p2#SP#sp3 |   193 | Single     |
| test/t2#P#p2#SP#sp4 |   191 | General    |
| test/t2#P#p3#SP#sp5 |     0 | System     |
| test/t2#P#p3#SP#sp6 |   194 | Single     |
+---------------------+-------+------------+
6 rows in set (0.00 sec)
```

**9.7 使用ALTER TABLE在表空间之间移动表分区**

```sql
【注意】
InnoDB从MySQL 5.7.24开始，不推荐 支持在共享表空间中放置表分区， 并且将在以后的MySQL版本中删除。共享表空间包括InnoDB 系统表空间和通用表空间。
```

要将分区表移动到其他表空间，必须对每个分区使用语句ALTER TABLE tbl_name REORGANIZE PARTITION

以下示例演示如何将分区表移动到其他表空间。 INFORMATION_SCHEMA.INNODB_SYS_TABLES 和 INFORMATION_SCHEMA.INNODB_SYS_TABLESPACES可以查询以验证分区是否存放在指定的表空间中。

```sql
【注意】
如果 TABLESPACE = tablespace_name选项为定义在REORGANIZE PARTITION 语句中，InnoDB 将移动分区至默认表空间中。以下示例中，表空间ts1，在表级定义的是表t1的默认表空间。分区P3从系统表空间移动到表空间ts1，因为在分区P3的ALTER TABLE t1 REORGANIZE PARTITION语句中没有指定TABLESPACE选项。
```

```sql
mysql> create tablespace ts1 add datafile 'ts1.ibd';
mysql> create tablespace ts2 add datafile 'ts2.ibd';


mysql> CREATE TABLE t1 ( a INT NOT NULL, PRIMARY KEY (a))
       ENGINE=InnoDB TABLESPACE ts1                          
       PARTITION BY RANGE (a) PARTITIONS 3 (
        PARTITION P1 VALUES LESS THAN (2),
        PARTITION P2 VALUES LESS THAN (4) TABLESPACE `innodb_file_per_table`,
        PARTITION P3 VALUES LESS THAN (6) TABLESPACE `innodb_system`);

mysql> SELECT A.NAME as partition_name, A.SPACE_TYPE as space_type, B.NAME as space_name
       FROM INFORMATION_SCHEMA.INNODB_SYS_TABLES A
       LEFT JOIN INFORMATION_SCHEMA.INNODB_SYS_TABLESPACES B
       ON A.SPACE = B.SPACE WHERE A.NAME LIKE '%t1%' ORDER BY A.NAME;
+----------------+------------+--------------+
| partition_name | space_type | space_name   |
+----------------+------------+--------------+
| test/t1#P#P1   | General    | ts1          |
| test/t1#P#P2   | Single     | test/t1#P#P2 |
| test/t1#P#P3   | System     | NULL         |
+----------------+------------+--------------+



mysql> alter table t1 reorganize partition p1 into(partition p1 values less than(2) tablespace=`ts2`);

mysql> alter table t1 reorganize partition p2 into(partition p2 values less than(4) tablespace=`ts2`);

mysql> alter table t1 reorganize partition p3 into(partition p3 values less than(6));


mysql> SELECT A.NAME AS partition_name, A.SPACE_TYPE AS space_type, B.NAME AS space_name
       FROM INFORMATION_SCHEMA.INNODB_SYS_TABLES A
       LEFT JOIN INFORMATION_SCHEMA.INNODB_SYS_TABLESPACES B
       ON A.SPACE = B.SPACE WHERE A.NAME LIKE '%t1%' ORDER BY A.NAME;
+----------------+------------+------------+
| partition_name | space_type | space_name |
+----------------+------------+------------+
| test/t1#P#P1   | General    | ts2        |
| test/t1#P#P2   | General    | ts2        |
| test/t1#P#P3   | General    | ts1        |
+----------------+------------+------------+
```

9.8 删除通用表空间
DROP TABLESPACE语句用于删除InnoDB通用表空间。

删除InnoDB通用表空间之前，必须从表空间中删除所有表。如果不为空，则DROP TABLESPACE返回错误。

如果DROP TABLESPACE操作删除一个空的通用表空间返回错误，则表空间可能包含由服务器中断的ALTER TABLE操作留下的孤立临时表或中间表

当通用表空间中最后一个表删除时，通用表空间不会自动删除。

通用表空间不属于任何一个数据库，一个DROP DATABASE操作可以丢弃属于通用的表空间的表，但它不能删除表空间，必须显示删除表空间。

```sql
mysql> CREATE TABLESPACE `ts1` ADD DATAFILE 'ts1.ibd' Engine=InnoDB;

mysql> CREATE TABLE t1 (c1 INT PRIMARY KEY) TABLESPACE ts10 Engine=InnoDB;

mysql> DROP TABLE t1;

mysql> DROP TABLESPACE ts1;
```

```sql
9.9 通用表空间的限制
生成的或现有的表空间不能更改为常规表空间。

不支持创建临时通用表空间。

通用表空间不支持临时表

存储在通用表空间中的表只能在支持通用表空间的MySQL发行版中打开。

与系统表空间类似，truncate或删除存储在通用表空间中的表会在通用表空间.ibd数据文件内部创建可用空间，该 文件只能用于新InnoDB数据。不会像文件单独表空间一样把空间释放回操作系统 。

此外，ALTER TABLE驻留在共享表空间（通用表空间或系统表空间）中的表上的表复制操作可以增加表空间使用的空间量。此类操作需要与表中的数据和索引一样多的额外空间。表复制ALTER TABLE 操作所需的额外空间不会像单独表空间一样释放回操作系统。

ALTER TABLE … DISCARD TABLESPACE 与 ALTER TABLE …IMPORT TABLESPACE不支持通用表空间
```

