---
title: 文章内容
---

# 文章内容

[**MySQL Binlog 【ROW】和【STATEMENT】选择**](https://www.cnblogs.com/zhoujinyi/archive/2013/01/15/2836131.html)

**前言：**

二进制日记录了数据库执行更改的操作，如Insert，Update，Delete等。不包括Select等不影响数据库记录的操作，因为没有对数据进行修改。二进制主要的功能有：复制（Replication）和恢复（Recovery）。具体的二进制里面的格式表示的意思请见

[这篇文章](http://www.cnblogs.com/zhoujinyi/archive/2012/11/19/2773650.html)

。

MySQL记录的日志有三种模式：STATEMENT、ROW、MIXED，这3个到底有什么区别呢？对Replication有什么区别呢？本文开始进行一些说明，如有遗漏请大家补充。

**一，大小：日志产生量。**

Client1:

```sql
View Code 
root@localhost : test 11:33:58>show variables like 'binlog_format';
+---------------+-------+
| Variable_name | Value |
+---------------+-------+
| binlog_format | ROW   |
+---------------+-------+
1 row in set (0.00 sec)

root@localhost : test 11:34:01>select count(*) from me_info;
+----------+
| count(*) |
+----------+
|    84183 |
+----------+
1 row in set (0.00 sec)

二进制日志：106个字节。
-rw-rw---- 1 mysql adm  106 2012-12-28 14:44 mysql-bin.000001
```

Client2:

```sql
View Code 

root@127.0.0.1 : test 11:34:23>show variables like 'binlog_format';
+---------------+-----------+
| Variable_name | Value     |
+---------------+-----------+
| binlog_format | STATEMENT |
+---------------+-----------+
1 row in set (0.00 sec)

root@127.0.0.1 : test 11:34:25>select count(*) from me_info;
+----------+
| count(*) |
+----------+
|    84183 |
+----------+
1 row in set (0.00 sec)

二进制日志：106字节
-rw-rw---- 1 mysql adm  106 2012-12-28 14:44 mysql-bin2.000001
```

Client3:

```sql
View Code 

root@127.0.0.1 : test 04:09:07>show variables like 'binlog_format';
+---------------+-------+
| Variable_name | Value |
+---------------+-------+
| binlog_format | MIXED |
+---------------+-------+
1 row in set (0.00 sec)

root@127.0.0.1 : test 04:09:14>select count(*) from me_info;
+----------+
| count(*) |
+----------+
|    84183 |
+----------+
1 row in set (0.00 sec)

-rw-rw---- 1 mysql adm   33 2012-12-31 16:15 mysql-bin3.index
```

除了binlog_format不一样之外，其他都是一样的。先看下事务操作的日志大小（物理）。删除数据：

`delete from me_info where id < `**`2153269`**`;`

查看他们日志的大小：发现ROW 和 其他2个大小不一致，而MIXED和STATEMENT一致。通过mysqlbinlog 发现他们记录的格式ROW不同于STATEMENT和MIXED。

小结1：       通过上面的说明得出一点是ROW格式比MIX和STATEMENT要大，原因是ROW记录的是记录更新后的值（不需要记录上下文信息），而其他2个模式记录的只是一个逻辑的SQL语句（需要记录上下文信息），具体格式可以看[这里](http://www.cnblogs.com/zhoujinyi/archive/2012/12/25/2832543.html)的ROW日志信息。因为上面的表删除了3W的记录，ROW模式会记录每一条删除语句，所以日志会很大。这也说明将格式设置成ROW，对于磁盘空间的要求增加了，而复制采用传输二进制日志方式实现的，所以复制的网络开销也有增加。所以最后的结果是：**ROW>STATEMENT=MIXED**

**二，复制：对复制产生的影响**

表：

```sql
View Code 

root@127.0.0.1 : rep_test 05:38:06>desc user;
+---------------+--------------+------+-----+---------------------+----------------+
| Field         | Type         | Null | Key | Default             | Extra          |
+---------------+--------------+------+-----+---------------------+----------------+
| id            | int(11)      | NO   | PRI | NULL                | auto_increment |
| username      | varchar(20)  | NO   | UNI |                     |                |
| status        | int(4)       | YES  | MUL | NULL                |                |
…………………………………………
…………………………………………
…………………………………………
+---------------+--------------+------+-----+---------------------+----------------+
42 rows in set (0.03 sec)
```

**1，****磁盘IOPS，网卡流量，cpu****:**

一个更新脚本，更新一个字符串字段。

```sql
View Code 

import MySQLdb
from random import choice
from random import randint
def get_str(n):
    A=''    
    for i in range(n):
        A=A+chr(97+randint(0,25))
    return A

if __name__ =='__main__':
    pwd = get_str(16)
    conn = MySQLdb.connect(host='localhost',user='root',passwd='123456',charset='utf8',db='rep_test')
    for i in xrange(1000000):
        query ="update user set password = '%s' where id =%d" %(pwd,i)
        cursor = conn.cursor()
        cursor.execute(query)
        print query
    print 'OK'
```

执行脚本,查看网卡流量：{iftop、ifstat、dstat -N eth0 }

STATEMENT下主从的情况：

```sql
View Code 

STATEMENT
-rw-rw---- 1 mysql adm 128M 2013-01-15 09:29 mysql-bin.000001
主：
----total-cpu-usage---- -dsk/total- --net/eth0- ---paging-- ---system--
usr sys idl wai hiq siq| read  writ| recv  send|  in   out | int   csw 
 50  16  31   0   0   2|   0     0 | 362k 1184k|   0     0 |  12k   48k
 45  15  37   2   0   2|   0  6892k| 196k 1041k|   0     0 |  11k   45k
 58  20  21   0   0   2|   0     0 | 332k 1088k|   0     0 |  10k   46k
 52  17  31   0   0   2|   0     0 | 353k 1122k|   0     0 |  12k   45k
 52  19  28   0   0   2|   0    84k| 308k 1032k|   0     0 |  10k   42k
 50  17  31   0   0   2|   0     0 | 360k 1171k|   0     0 |  12k   47k
 44  17  33   4   0   1|   0  9560k| 350k 1092k|   0     0 |  11k   44k
 49  18  31   0   0   2|   0     0 | 355k 1111k|   0     0 |  11k   46k
 47  24  27   0   0   3|   0     0 | 357k 1144k|   0     0 |  11k   48k
 64  18  17   0   0   2|   0    76k| 264k  985k|   0     0 |7621    43k
 56  16  26   0   0   1|   0     0 | 365k 1146k|   0     0 |  11k   47k
 49  16  31   3   0   2|4096B 6820k| 341k 1071k|   0     0 |  10k   44k
 51  23  25   0   0   2|   0     0 | 357k 1170k|   0     0 |  11k   48k
 56  17  25   0   0   1|   0     0 | 334k 1068k|   0     0 |  11k   44k
 50  15  32   1   0   3|   0  2132k| 375k 1170k|   0     0 |  12k   47k
 46  18  33   0   0   2|   0  2048k| 374k 1180k|   0     0 |  12k   47k
 59  16  23   0   0   2|   0     0 | 362k 1168k|   0     0 |  10k   49k
 48  13  29   9   0   1|4096B   12M| 271k  889k|   0     0 |8581    37k
 48  19  32   0   0   2|   0     0 | 385k 1209k|   0     0 |  12k   49k
 59  18  21   0   0   2|   0    92k| 311k 1022k|   0     0 |8799    44k
 47  20  31   0   0   2|   0     0 | 375k 1190k|   0     0 |  12k   48k
 50  18  30   0   0   3|   0     0 | 313k 1086k|   0     0 |  10k   44k
 59  19  20   0   0   3|   0    16k| 360k 1134k|   0     0 |9620    48k

从：
----total-cpu-usage---- -dsk/total- --net/eth0- ---paging-- ---system--
usr sys idl wai hiq siq| read  writ| recv  send|  in   out | int   csw 
 64  12  18   0   0   6|   0   512B|1204k  381k|   0     0 |  19k   16k
 48  14  33   0   0   6|   0     0 |1134k  357k|   0     0 |  17k   16k
 30  18  46   0   0   6|   0     0 |1070k  319k|   0     0 |  13k   14k
 45  18  34   0   0   4|   0     0 |1069k  326k|   0     0 |  13k   15k
 70  11  15   0   0   3|   0    33k|1156k  363k|   0     0 |  12k   15k
 42  12  43   0   0   3|   0   512B|1092k  338k|   0     0 |  14k   17k
 34  16  46   0   0   4|   0     0 |1195k  349k|   0     0 |  15k   17k
 56  11  14  15   0   5|   0    52M| 973k  177k|   0     0 |7848  7420 
 69  10  16   0   0   5|   0     0 |1107k  352k|   0     0 |  12k   15k
 31  14  49   0   0   5|   0    41k|1066k  316k|   0     0 |  13k   16k
 39  18  39   0   0   4|   0   512B|1117k  340k|   0     0 |  13k   15k
 60  13  20   0   0   7|   0     0 |1105k  349k|   0     0 |  17k   14k
 61  14  18   1   0   7|   0  9216B|1189k  377k|   0     0 |  18k   15k
 32  12  52   0   0   5|   0     0 |1109k  344k|   0     0 |  15k   17k
 34  20  42   0   0   4|   0    33k|1068k  319k|   0     0 |  13k   14k
 63  14  17   0   0   6|   0   512B|1063k  304k|   0     0 |  15k   12k
 61  10  22   0   0   7|   0     0 |1071k  340k|   0     0 |  17k   14k
 36  19  42   0   0   4|   0     0 |1141k  354k|   0     0 |  15k   18k
 26  17  53   0   0   4|   0     0 |1125k  347k|   0     0 |  15k   18k
 58  15  18   1   0   8|   0   141k|1119k  347k|   0     0 |  17k   14k
 62  12  18   0   0   7|   0   512B|1173k  374k|   0     0 |  18k   15k
 33  17  43   0   0   6|   0     0 |1182k  367k|   0     0 |  17k   19k
 27  15  55   0   0   3|   0     0 | 889k  273k|   0     0 |  12k   14k
```

从上面信息可以看出：产生了128M的二进制日志，在复制期间，Master网卡出去（send）流量平均1M左右，Slave网卡接收（recv）流量平均1M左右，Master的CPU空闲30左右，Slave的CPU空闲30~40，磁盘读写都比较小。

ROW下主从的情况：

```sql
View Code 

ROW:
-rw-rw---- 1 mysql adm 706M 2013-01-15 09:37 mysql-bin.000002
主：
----total-cpu-usage---- -dsk/total- --net/eth0- ---paging-- ---system--
usr sys idl wai hiq siq| read  writ| recv  send|  in   out | int   csw 
 53  20  25   0   0   2|   0  4096k| 189k 4376k|   0     0 |  11k   43k
 55  16  29   0   0   1|   0  8176k| 232k 4644k|   0     0 |  12k   45k
 64  19  13   1   0   2|   0  5548k| 234k 3379k|   0     0 |7497    36k
 50  19  26   3   0   3|   0    26M| 322k 4692k|   0     0 |  12k   47k
 52  19  27   0   0   2|   0     0 | 311k 4638k|   0     0 |  12k   46k
 52  18  28   0   0   1|   0     0 | 276k 4157k|   0     0 |  10k   42k
 55  20  24   0   0   2|   0     0 | 308k 4353k|   0     0 |  11k   44k
 57  16  23   2   0   1|4096B 4624k| 262k 3772k|   0     0 |9495    39k
 47  16  29   7   0   2|   0    21M| 229k 3982k|   0     0 |  10k   40k
 54  14  31   1   0   1|   0    16k| 296k 4572k|   0     0 |  12k   45k
 50  20  29   0   0   2|   0     0 | 322k 4595k|   0     0 |  12k   44k
 54  15  31   0   0   1|   0     0 | 308k 4461k|   0     0 |  11k   45k
 58  20  20   0   0   1|   0     0 | 154k 4133k|   0     0 |8725    43k
 58  16  23   1   0   2|   0    60k| 293k 4133k|   0     0 |9969    42k
 59  16  24   0   0   2|   0  4096k| 283k 4388k|   0     0 |  11k   44k
 50  18  30   0   0   3|   0  4096k| 184k 4681k|   0     0 |  12k   46k
 50  19  28   1   0   1|   0  4072k| 306k 4716k|   0     0 |  12k   46k
 53  19  27   0   0   2|   0    31M| 329k 4701k|   0     0 |  12k   47k
 51  19  28   1   0   2|   0   100k| 306k 4560k|   0     0 |  12k   45k
 50  17  31   0   0   2|   0     0 | 307k 4587k|   0     0 |  12k   45k
 53  19  26   1   0   2|   0    28k| 279k 4120k|   0     0 |  10k   42k
 52  16  30   0   0   2|   0     0 | 323k 4628k|   0     0 |  12k   46k
 47  17  28   9   0   1|4096B   26M| 106k 3751k|   0     0 |8305    39k

从：
----total-cpu-usage---- -dsk/total- --net/eth0- ---paging-- ---system--
usr sys idl wai hiq siq| read  writ| recv  send|  in   out | int   csw 
 71  19   7   0   0   4|   0     0 |4635k  319k|   0     0 |  12k   13k
 53  18  24   0   0   4|   0     0 |3844k  264k|   0     0 |  15k   21k
 47  31  12   0   0  10|   0   178k|4710k  173k|   0     0 |  16k   16k
 58  27   8   0   0   7|   0     0 |4332k  180k|   0     0 |  14k   11k
 60  12  25   0   0   3|   0    25k|2918k  206k|   0     0 |  11k 9933 
 49  19  28   0   0   4|   0     0 |4200k  292k|   0     0 |  22k   29k
 33  28  35   0   1   3|   0     0 |4434k  297k|   0     0 |  26k   37k
 48  25  21   0   0   6|   0    33k|4238k  283k|   0     0 |  18k   24k
 67  14  16   0   0   3|   0     0 |3682k  254k|   0     0 |9446    12k
 43  24  30   0   0   4|   0     0 |4461k  305k|   0     0 |  23k   33k
 32  29  35   0   0   4|   0     0 |4273k  293k|   0     0 |  27k   40k
 58  21  17   0   0   4|   0     0 |4012k  275k|   0     0 |  14k   20k
 67  16  14   0   0   3|4096B  161k|4135k  285k|   0     0 |  11k   13k
 39  34  21   0   0   6|   0     0 |4255k  185k|   0     0 |  17k   20k
 40  32  13   8   0   7|   0    26M|4198k  164k|   0     0 |  15k   14k
 77  18   0   0   0   5|   0     0 |4560k  277k|   0     0 |  11k 9888 
 57  20  16   0   0   7|   0     0 |4707k  328k|   0     0 |  17k   22k
 35  29  31   0   1   4|   0    33k|4571k  298k|   0     0 |  26k   36k
 40  18  38   0   0   4|   0     0 |3493k  203k|   0     0 |  15k   18k
 56   5   1  36   0   2|   0    96M|1607k   44k|   0     0 |5375  7012 
 57  23  16   0   0   4|   0    11M|6747k  149k|   0     0 |  18k   20k
 31  31  34   0   0   4|   0     0 |4691k  314k|   0     0 |  27k   39k
 48  24  22   0   0   5|   0    45k|4471k  286k|   0     0 |  19k   22k
 64  16  12   0   0   8|   0     0 |4607k  319k|   0     0 |  17k   16k
 47  22  27   0   0   4|   0  5120B|4295k  293k|   0     0 |  21k   27k
 47  32  12   0   0   8|   0     0 |4645k  194k|   0     0 |  17k   17k
```

从上面信息可以看出：产生了706M的二进制日志，在复制期间，Master网卡出去（send）流量4M~5M，Slave网卡接收（recv）流量4M~5M，Master的CPU空闲20~30，Slave的CPU空闲20左右，磁盘读写也不算大。

对比Row和Statement：R比S产生的日志量大5.5倍，网卡流量高4~5倍，cpu稍微忙了10个百分点。在复制过程中，从均没有延迟。因为SQL过滤条件WHERE 后面的字段利用好索引，ROW和STATEMENT模式下效果一样。要是没有利用好索引，则：STATEMENT下：在主上执行（3~5s）一条，从上也是需要这个时间，并且出现延迟。（Seconds_Behind_Master）。本来就单线程的，导致从的可用性更差。ROW下：在主上执行（3~5s）一条，正常情况下每张表都有主键，所以按照ROW的记录的SQL格式，不会出现对这类sql的延迟。除非极端情况下更新一张没有主键甚至没有任何索引的表。

**范围内的批量更新结果怎么样?**【update user set password = 'serqrnncavfyozeu' where id > 0 and id < 1000000】

STATEMENT下主从的情况：

View Code

MIXED：
-rw-rw---- 1 mysql adm  253 2013-01-15 10:32 mysql-bin.000005
主：
----total-cpu-usage---- -dsk/total- --net/eth0- ---paging-- ---system--
usr sys idl wai hiq siq| read  writ| recv  send|  in   out | int   csw
5   1  93   0   0   0|  27k  119k|   0     0 |   0     0 | 630  1346
30  16  40  14   0   0|   0    43M|  20k  594B|   0     0 |1175  2851
41  25  32   2   0   0|   0    44k|2892B  126B|   0     0 | 985  2651
32  25  43   0   0   1|   0    25M|2623B  192B|   0     0 |1035  2008
33  25  43   0   0   0|   0    12M|  18k 1116B|   0     0 | 981  2184
30  24  45   0   0   0|   0     0 |1486B   66B|   0     0 | 804  1777
31  27  43   0   0   0|   0     0 |2285B   66B|   0     0 | 836  1841
39  28  32   1   0   0|   0    12k|  12k 1056B|   0     0 | 923  2629
17  10  72   2   0   0|   0    32k|2017B  464B|   0     0 |1208  2311
8   2  91   0   0   0|   0    32M|7847B 1548B|   0     0 |1259  2339
10   2  88   0   0   0|   0     0 |  19k 2454B|   0     0 |1389  2807
7   1  92   0   0   0|   0     0 |3712B  312B|   0     0 |1231  2340
35   9  57   0   0   0|   0     0 |4467B  315B|   0     0 |1703  4129
19   3  77   2   0   0|   0    44k|  23k 2028B|   0     0 |1709  3545
8   2  90   0   0   0|   0     0 |2338B   66B|   0     0 |1329  2613
6   2  92   0   0   0|   0     0 |1750B   66B|   0     0 |1140  2200
10   2  89   0   0   0|   0     0 |4356B  594B|   0     0 |1225  2494
25   5  71   0   0   0|   0     0 |1956B  196B|   0     0 |1344  2732
4   1  94   2   0   0|   0    68k|1852B  132B|   0     0 |1257  2282
8   3  89   0   0   0|   0     0 |3958B  594B|   0     0 |1393  2760
14   5  81   0   0   0|   0     0 |1268B  132B|   0     0 |1150  2443
13   3  84   0   0   0|   0     0 |1953B  600B|   0     0 |1447  2805
9   4  87   0   0   0|   0     0 |  12k 1182B|   0     0 |1211  2596
7   1  91   1   0   0|   0    44k|2194B  132B|   0     0 |1086  2118
28   5  64   2   0   0|   0    32k|3019B   66B|   0     0 |1408  3612
17   5  79   0   0   0|   0     0 |5726B 3213B|   0     0 |1533  3338
23   5  72   0   0   0|   0     0 |1937B  246B|   0     0 |1233  2707
21   2  78   0   0   0|   0     0 |1646B   66B|   0     0 |1247  2401
20   5  72   3   0   0|   0   500k|  10k  924B|   0     0 |1434  3315
18   3  76   3   0   0|   0    52k|5458B 1706B|   0     0 |1523  3153
16   3  81   1   0   0|   0    24k|2884B   66B|   0     0 |1378  2761
13   4  84   0   0   0|   0     0 |  19k 1452B|   0     0 |1427  2940
9   2  86   2   0   0|   0    76k|2580B  132B|   0     0 |1217  2491
7   1  92   1   0   0|   0  4096B|1754B   66B|   0     0 |1089  2104
9   2  88   2   0   0|   0    28k|  18k 1512B|   0     0 |1225  2531
17   5  78   0   0   0|   0     0 |2340B   66B|   0     0 |1154  2553
8   2  90   0   0   0|   0     0 |1893B   66B|   0     0 |1128  2214
17   4  79   0   0   0|   0     0 |5156B  660B|   0     0 |1421  2914
9   1  90   0   0   0|   0     0 |2130B   66B|   0     0 |1346  2704
7   1  86   6   0   0|   0   316k|3846B   66B|   0     0 |1148  2157
30   6  63   0   0   0|   0     0 |  11k  840B|   0     0 |1585  4107
15   4  81   0   0   0|   0     0 |2800B   66B|   0     0 |1208  2547
29   4  67   0   0   0|   0     0 |4188B  360B|   0     0 |1351  3017
10   2  89   0   0   0|   0     0 |  15k  954B|   0     0 |1289  2587
11   2  88   0   0   0|   0  8192B|5822B  378B|   0     0 |1396  2586

从：
----total-cpu-usage---- -dsk/total- --net/eth0- ---paging-- ---system--
usr sys idl wai hiq siq| read  writ| recv  send|  in   out | int   csw
10   2  87   0   0   0|  56k   47k|   0     0 |   0     0 |1499  1703
1   1  97   1   0   0|   0    62k|1208B  932B|   0     0 | 476   835
43   1  56   0   0   0|   0   512B|3402B  354B|   0     0 |1260   748
47   1  52   0   0   0|   0     0 |2544B   17k|   0     0 |1417  1091
2   2  97   0   0   0|   0     0 |1893B  354B|   0     0 | 586   847
4   1  95   0   0   0|   0     0 |1922B  468B|   0     0 | 488   680
50   1  49   0   0   1|   0     0 |2253B   17k|   0     0 |1729  1349
33   1  66   1   0   0|   0    13k|1733B  354B|   0     0 | 834   565
2   1  97   0   0   0|   0     0 |2571B  354B|   0     0 | 485   679
19   1  80   0   0   0|   0     0 |2438B   10k|   0     0 |1110  1232
73  24   4   0   0   1|   0     0 |2872B  712B|   0     0 | 997   260
50  22  29   0   0   0|   0    13k|3316B 4624B|   0     0 | 805   729
27  25  47   0   0   1|   0   512B|4177B   20k|   0     0 | 958  1404
56  26  18   0   0   0|   0     0 |2316B  462B|   0     0 |1006   539
74  26   0   0   0   0|   0     0 |2920B  354B|   0     0 | 986   206
34  24  43   0   0   0|   0    21k|4486B   17k|   0     0 |1067  1262
26  25  49   0   0   1|   0    73k|1710B  354B|   0     0 | 644   656
72  25   4   0   0   0|   0   512B|1517B  354B|   0     0 | 987   269
64  25  11   0   0   0|   0     0 |2114B 3276B|   0     0 |1141   621
24  28  48   0   0   0|   0     0 |1655B  420B|   0     0 | 606   595
37  28  35   0   0   0|   0    17k|1412B  468B|   0     0 | 745   537
74  26   0   0   0   0|   0    21k|1334B 3218B|   0     0 |1313   545
49  27  23   0   0   0|   0   512B| 928B  468B|   0     0 | 763   366
28  27  45   0   0   0|   0     0 |1579B  468B|   0     0 | 646   582
40  17  43   0   0   0|   0     0 |3081B   10k|   0     0 |1196  1076
50   1  49   0   0   0|   0     0 |1060B  468B|   0     0 | 893   301
9   0  91   0   0   0|   0     0 |2731B  354B|   0     0 | 603   817
4   1  94   1   0   0|   0    21k|1710B 5046B|   0     0 | 918  1344
43   1  56   0   0   0|   0     0 |1156B  354B|   0     0 | 870   416
44   0  56   0   0   0|   0     0 |1504B  354B|   0     0 | 824   313
4   1  95   0   0   0|   0     0 |4265B 8780B|   0     0 |1039  1549
7   1  93   0   0   0|   0    97k|3218B  354B|   0     0 | 576   815
50   1  49   0   0   1|   0   512B|2776B  354B|   0     0 | 861   249
31   2  68   0   0   0|   0     0 |4484B   16k|   0     0 |1261  1272
2   1  98   0   0   0|   0     0 |2048B  468B|   0     0 | 618   846
22   1  77   0   0   1|   0     0 |1406B  354B|   0     0 | 655   573
50   2  49   0   0   0|   0     0 |2518B   17k|   0     0 |1566  1173
16   1  83   1   0   0|   0    13k|1986B  354B|   0     0 | 569   531
1   1  98   0   0   0|   0     0 |2217B  354B|   0     0 | 471   699
35   2  63   0   0   1|   0     0 |2378B 3668B|   0     0 |1241  1001
51   0  49   0   0   0|   0     0 |2486B  354B|   0     0 | 915   321
5   6  83   6   0   0|   0    20M|2950B  354B|   0     0 |1942  3311
5   3  59  31   0   2|   0    94M|2864B 9480B|   0     0 |4795  7901
47   1  52   0   0   0|   0    50M|2475B  354B|   0     0 |1133   532
39   1  60   0   0   0|   0     0 |4052B  550B|   0     0 | 820   379

ROW下主从的情况：

```sql
View Code 

ROW:
-rw-rw---- 1 mysql adm 430M 2013-01-15 10:28 mysql-bin.000004
主：
----total-cpu-usage---- -dsk/total- --net/eth0- ---paging-- ---system--
usr sys idl wai hiq siq| read  writ| recv  send|  in   out | int   csw 
  5   1  93   0   0   0|  26k  116k|   0     0 |   0     0 | 629  1346 
 38  15  36  11   0   0|   0    45M|5389B  576B|   0     0 |1226  2611 
 40  15  44   0   0   1|   0    50M|2406B  192B|   0     0 | 945  1807 
 38  18  43   0   0   0|   0    49M|3046B  132B|   0     0 | 903  1945 
 50  20  29   0   0   0|   0    49M|  13k 1056B|   0     0 |1137  2528 
 38  18  45   0   0   0|   0    51M|2137B   66B|   0     0 |1014  1799 
 30  12  42  16   0   0|   0    44M|3315B  192B|   0     0 |1120  2265 
 39  18  40   4   0   1|   0    47M|  11k 1056B|   0     0 |1030  1875 
 40  17  43   0   0   1|   0    52M|2783B   66B|   0     0 |1000  1833 
 43  25  33   0   0   0|   0    18M|2348B   66B|   0     0 | 997  2614 
 36  25  36   2   0   0|   0   112k|5197B  594B|   0     0 | 984  2248 
 31  26  44   0   0   0|   0     0 |1337B   66B|   0     0 | 906  1896 
 34  26  37   3   0   0|   0    52k|2538B   66B|   0     0 | 985  2414 
 21  25  33  21   0   1|   0    65M|3987B  198B|   0     0 |1295  2320 
 12  10  40  38   0   1|  11M   96M|1710B  132B|   0     0 |1611  2545 
 16  17  39  28   0   2|  52M   47M|1154B   66B|   0     0 |2005  3721 
 12  13  45  29   0   1|  49M   53M|4747B  528B|   0     0 |1983  3472 
 21  15  33  30   0   2|  44M   41M|1448B  132B|   0     0 |1992  4209 
 26  16  34  24   0   1|  29M   70M|1867B   66B|   0     0 |2138  4630 
 10  11  66  12   0   1|1244k   74M| 209k 9216k|   0     0 |3629  2743 
  9   3  86   1   0   1|1552k    0 | 251k   12M|   0     0 |3872  2699 
  6   5  90   0   0   0|  11M    0 | 279k   12M|   0     0 |4125  2620 
 13   4  82   1   0   1|  11M    0 | 287k   12M|   0     0 |4361  3143 
 10   5  82   3   0   1|  11M   32k| 276k   12M|   0     0 |4283  3006 
 36  10  49   5   0   1|  11M   12M| 265k   12M|   0     0 |4141  3853 
 10   4  86   0   0   1|   0     0 | 292k   12M|   0     0 |4078  2534 
  7   4  89   0   0   1|   0     0 | 276k   12M|   0     0 |3908  2307 
 21   7  69   1   0   0|   0    28k| 271k   12M|   0     0 |4012  3055 
 14   4  82   0   0   1|   0     0 | 278k   12M|   0     0 |3850  2545 
 20   7  71   1   0   1|   0    52k| 278k   12M|   0     0 |4000  2541 
 16   5  76   2   0   1|   0    28k| 278k   12M|   0     0 |4000  2865 
 20   6  74   0   0   1|   0     0 | 292k   12M|   0     0 |3956  2509 
 11   2  85   0   0   1|   0     0 | 276k   12M|   0     0 |3918  2462 
 33  10  56   0   0   1|   0     0 | 273k   12M|   0     0 |4071  3322 
 18   5  76   2   0   1|   0    20k| 291k   12M|   0     0 |4005  2400 
  7   4  89   0   0   0|   0     0 | 286k   12M|   0     0 |3895  2242 
 22   6  72   1   0   1| 736k    0 | 290k   12M|   0     0 |4019  2692 
 31   7  62   2   0   0|4096B   12k| 278k   12M|   0     0 |3912  2513 
  8   2  90   0   0   0|   0     0 | 280k   12M|   0     0 |3885  2214 
 26   6  68   0   0   1|   0     0 | 278k   12M|   0     0 |3966  2838 
 11   3  85   1   0   0|   0    56k| 286k   12M|   0     0 |4005  2606 
 22   6  72   0   0   1|   0     0 | 277k   12M|   0     0 |4050  2390 
 34   9  54   4   0   1|4096B  468k| 274k   12M|   0     0 |3886  2832 
 21   6  72   1   0   1| 304k    0 | 287k   12M|   0     0 |4371  4179 
 21   6  70   2   0   0|   0    24k| 281k   12M|   0     0 |4150  3492 


从：
----total-cpu-usage---- -dsk/total- --net/eth0- ---paging-- ---system--
usr sys idl wai hiq siq| read  writ| recv  send|  in   out | int   csw 
 10   2  87   0   0   0|  56k   47k|   0     0 |   0     0 |1499  1703 
 50   1  49   0   0   0|   0     0 |1446B  834B|   0     0 | 952   348 
 34   0  66   0   0   0|   0     0 |2706B  468B|   0     0 |1180   895 
  1   1  98   0   0   1|   0     0 |4082B   10k|   0     0 | 577   997 
 19   1  80   0   0   0|   0     0 |2083B  354B|   0     0 | 683   583 
 50   1  49   0   0   0|   0     0 |2413B  354B|   0     0 |1323   719 
 21   2  77   1   0   1|   0    13k|2557B   10k|   0     0 | 714   902 
  3   1  96   0   0   0|   0     0 |2565B  354B|   0     0 | 602   867 
 31   1  68   0   0   0|   0     0 |2282B  354B|   0     0 |1273   971 
 51   0  49   0   0   0|   0     0 |2233B 3554B|   0     0 | 940   413 
  7   0  92   0   0   1|   0     0 |1191B  354B|   0     0 | 635   786 
  3   1  96   0   0   0|   0     0 |2316B  354B|   0     0 | 872  1219 
 46   1  54   0   0   0|   0     0 |1797B 2710B|   0     0 |1420   915 
 40   0  60   0   0   1|   0     0 |1052B  468B|   0     0 | 854   476 
  4   1  95   0   0   0|   0     0 | 866B  354B|   0     0 |1051  1330 
 11   2  87   0   0   0|   0     0 |1803B 3472B|   0     0 | 587   762 
 51   1  48   1   0   0|   0   105k|1162B  468B|   0     0 |1437   879 
 30   1  69   0   0   0|   0   512B|1614B  354B|   0     0 |1252  1085 
 24  24  47   0   0   5|   0     0 |9578k  215k|   0     0 |  17k   22k
 46  26  18   3   0   6|   0    20M|  12M  250k|   0     0 |  19k   22k
 63  21   9   0   0   8|   0     0 |  12M  277k|   0     0 |  21k   21k
 55  22  18   0   0   5|   0    25k|  12M  285k|   0     0 |  21k   25k
 32  33  30   0   0   5|   0   512B|  12M  275k|   0     0 |  21k   30k
 48  25  22   0   0   5|   0     0 |  12M  263k|   0     0 |  20k   24k
 66  17   9   0   0   8|   0  5120B|  12M  290k|   0     0 |  21k   22k
 58  20  15   0   0   7|   0     0 |  12M  275k|   0     0 |  21k   24k
 33  31  32   0   0   4|   0    97k|  12M  268k|   0     0 |  21k   29k
 40  29  25   0   0   6|   0   512B|  12M  276k|   0     0 |  20k   26k
 65  20   8   0   0   7|   0     0 |  12M  277k|   0     0 |  21k   21k
 61  24   9   0   0   6|   0     0 |  12M  277k|   0     0 |  21k   22k
 33  31  33   0   0   4|   0     0 |  12M  286k|   0     0 |  21k   31k
 37  29  29   0   0   4|   0    25k|  12M  268k|   0     0 |  20k   28k
 64  19   8   0   0   9|   0   512B|  12M  274k|   0     0 |  20k   20k
 60  22  10   0   0   8|   0     0 |  12M  289k|   0     0 |  20k   22k
 38  28  29   0   0   5|   0     0 |  12M  285k|   0     0 |  21k   29k
 32  31  31   0   0   6|   0     0 |  12M  284k|   0     0 |  21k   30k
 66  19   8   0   0   7|   0    21k|  12M  276k|   0     0 |  14k   18k
 74  18   3   0   0   5|   0    57k|  12M  277k|   0     0 |  13k   20k
 33  29  33   0   0   4|   0   512B|  12M  277k|   0     0 |  21k   31k
 34  32  29   0   0   5|   0     0 |  12M  284k|   0     0 |  21k   30k
 74  18   2   0   0   7|   0     0 |  12M  275k|   0     0 |  13k   18k
 63  21  12   0   0   4|   0    25k|  12M  272k|   0     0 |  15k   22k
 34  29  31   0   0   7|   0   512B|  12M  285k|   0     0 |  21k   30k
 44  28  21   0   1   6|   0     0 |  12M  276k|   0     0 |  19k   25k
 71  22   3   0   0   5|   0     0 |  12M  277k|   0     0 |  13k   19k
```

对比发现：在执行此类sql的时候，在STATEMENT下面，（利用好索引）主和从的各个开销都很小，网络流量都不大。而在ROW下面：因为日志产生量就很大，导致在复制期间网卡流量就很大：12M。网卡流量：【1：10000】，日志大小：【1：2000000】，CPU空闲：【80：20】。这个只限于这个例子，看范围大小和表字段的大小。总之在网络和磁盘开销上面比较，他们差距了好几个数量级。

小结2：    对于更新单条的sql语句，在STATEMENT和ROW下1，CPU消耗差距不大，都需要执行这么sql。消耗 R=S2，磁盘写和网络传输上，因为ROW记录的格式的原因。消耗 R>S3，SQL效率来看，合理利用索引的更新，效率差距不大，不合理利用索引的更新，效率 R>S4，日志文件大小上，因为都需要记录这么多SQL，但是由于R和S的记录格式不一样，大小 R>S

对于执行一个大范围的sql语句，在STATEMENT和ROW下1，CPU上，主上只要执行一条SQL，而从上需要执行N条，消耗 R>S2，磁盘写和网络传输上，因为ROW记录的格式的原因。消耗R>S，看范围条件，大的话，差距巨大。3，日志文件大小上，主记录一条，从记录N条，并且还由于R和S的记录格式不一样，R>S，差距巨大。从上面的分析得出，STATEMENT要比ROW划算。要是使用STATEMENT没有任何问题的话，就推荐使用STATEMENT/MIXED格式记录二进制日志。

**2，****数据的一致性:**

其实ROW有很多一些好处。特别对数据的一致性有了很严的要求。情况1：

```sql
View Code 

STATEMENT/MIXED
主：
root@localhost : rep_test 11:24:56>select * from tt;
+------+------+
| id   | name |
+------+------+
|    1 | a    |
|    2 | b    |
|    3 | c    |
|    4 | d    |
|    5 | e    |
|    6 | f    |
|    7 | g    |
+------+------+
7 rows in set (0.00 sec)
从：
root@127.0.0.1 : rep_test 11:22:32>select * From tt;
+------+------+
| id   | name |
+------+------+
|    1 | a    |
|    2 | b    |
|    3 | c    |
|    4 | d    |
|    5 | e    |
+------+------+
5 rows in set (0.00 sec)

主上执行：
root@localhost : rep_test 11:25:11>update tt set name =upper(name) where id =7;
Query OK, 1 row affected (0.03 sec)
Rows matched: 1  Changed: 1  Warnings: 0

从：
root@127.0.0.1 : rep_test 11:25:01>show slave status\G;
*************************** 1. row ***************************
               Slave_IO_State: Waiting for master to send event
                  Master_Host: 127.0.0.1
                  Master_User: rep
                  Master_Port: 3306
                Connect_Retry: 60
              Master_Log_File: mysql-bin.000001
          Read_Master_Log_Pos: 450
               Relay_Log_File: zhoujy-relay-bin.000002
                Relay_Log_Pos: 595
        Relay_Master_Log_File: mysql-bin.000001
             Slave_IO_Running: Yes
            Slave_SQL_Running: Yes
              Replicate_Do_DB: 
          Replicate_Ignore_DB: test
           Replicate_Do_Table: 
       Replicate_Ignore_Table: 
      Replicate_Wild_Do_Table: 
  Replicate_Wild_Ignore_Table: 
                   Last_Errno: 0
                   Last_Error: 
                 Skip_Counter: 0
          Exec_Master_Log_Pos: 450
              Relay_Log_Space: 751
              Until_Condition: None
               Until_Log_File: 
                Until_Log_Pos: 0
           Master_SSL_Allowed: No
           Master_SSL_CA_File: 
           Master_SSL_CA_Path: 
              Master_SSL_Cert: 
            Master_SSL_Cipher: 
               Master_SSL_Key: 
        Seconds_Behind_Master: 0
Master_SSL_Verify_Server_Cert: No
                Last_IO_Errno: 0
                Last_IO_Error: 
               Last_SQL_Errno: 0
               Last_SQL_Error: 
1 row in set (0.00 sec)

ROW：
主上执行：
root@localhost : rep_test 11:25:11>update tt set name =upper(name) where id =7;
Query OK, 1 row affected (0.03 sec)
Rows matched: 1  Changed: 1  Warnings: 0

从：
root@127.0.0.1 : rep_test 11:25:47>show slave status\G;
*************************** 1. row ***************************
               Slave_IO_State: Waiting for master to send event
                  Master_Host: 127.0.0.1
                  Master_User: rep
                  Master_Port: 3306
                Connect_Retry: 60
              Master_Log_File: mysql-bin.000001
          Read_Master_Log_Pos: 687
               Relay_Log_File: zhoujy-relay-bin.000002
                Relay_Log_Pos: 595
        Relay_Master_Log_File: mysql-bin.000001
             Slave_IO_Running: Yes
            Slave_SQL_Running: No
              Replicate_Do_DB: 
          Replicate_Ignore_DB: test
           Replicate_Do_Table: 
       Replicate_Ignore_Table: 
      Replicate_Wild_Do_Table: 
  Replicate_Wild_Ignore_Table: 
                   Last_Errno: 1032
                   Last_Error: Could not execute Update_rows event on table rep_test.tt; Can't find record in 'tt', Error_code: 1032; handler error HA_ERR_END_OF_FILE; the event's master log mysql-bin.000001, end_log_pos 614
                 Skip_Counter: 0
          Exec_Master_Log_Pos: 450
              Relay_Log_Space: 988
              Until_Condition: None
               Until_Log_File: 
                Until_Log_Pos: 0
           Master_SSL_Allowed: No
           Master_SSL_CA_File: 
           Master_SSL_CA_Path: 
              Master_SSL_Cert: 
            Master_SSL_Cipher: 
               Master_SSL_Key: 
        Seconds_Behind_Master: NULL
Master_SSL_Verify_Server_Cert: No
                Last_IO_Errno: 0
                Last_IO_Error: 
               Last_SQL_Errno: 1032
               Last_SQL_Error: Could not execute Update_rows event on table rep_test.tt; Can't find record in 'tt', Error_code: 1032; handler error HA_ERR_END_OF_FILE; the event's master log mysql-bin.000001, end_log_pos 614
```

更新主上有的数据，但从上没有：在STATEMENT/MIXED下，复制正常，没有报错。而在ROW下，复制终止。

情况2：和ROW记录的格式有关

```sql
View Code 

STATEMENT/MIXED
把从的name字段从varchar 改成 char
主：
insert into tt values(8,'H'),(9,'I');

从：复制成功
root@127.0.0.1 : rep_test 12:40:43>select * from tt;
+------+------+
| id   | name |
+------+------+
|    1 | A    |
|    2 | B    |
|    3 | C    |
|    4 | d    |
|    5 | E    |
|    8 | H    |
|    9 | I    |
+------+------+
7 rows in set (0.00 sec) 

ROW
主上执行：
root@localhost : rep_test 12:41:55>insert into tt values(10,'J');
Query OK, 1 row affected (0.00 sec)

从：
root@127.0.0.1 : rep_test 12:41:59>show slave status\G;
*************************** 1. row ***************************
               Slave_IO_State: Waiting for master to send event
                  Master_Host: 127.0.0.1
                  Master_User: rep
                  Master_Port: 3306
                Connect_Retry: 60
              Master_Log_File: mysql-bin.000003
          Read_Master_Log_Pos: 658
               Relay_Log_File: zhoujy-relay-bin.000011
                Relay_Log_Pos: 574
        Relay_Master_Log_File: mysql-bin.000003
             Slave_IO_Running: Yes
            Slave_SQL_Running: No
              Replicate_Do_DB: 
          Replicate_Ignore_DB: test
           Replicate_Do_Table: 
       Replicate_Ignore_Table: 
      Replicate_Wild_Do_Table: 
  Replicate_Wild_Ignore_Table: 
                   Last_Errno: 1535
                   Last_Error: Table definition on master and slave does not match: Column 1 type mismatch - received type 15, rep_test.tt has type 254
                 Skip_Counter: 0
          Exec_Master_Log_Pos: 429
              Relay_Log_Space: 1002
              Until_Condition: None
               Until_Log_File: 
                Until_Log_Pos: 0
           Master_SSL_Allowed: No
           Master_SSL_CA_File: 
           Master_SSL_CA_Path: 
              Master_SSL_Cert: 
            Master_SSL_Cipher: 
               Master_SSL_Key: 
        Seconds_Behind_Master: NULL
Master_SSL_Verify_Server_Cert: No
                Last_IO_Errno: 0
                Last_IO_Error: 
               Last_SQL_Errno: 1535
               Last_SQL_Error: Table definition on master and slave does not match: Column 1 type mismatch - received type 15, rep_test.tt has type 254
1 row in set (0.00 sec)
```

主从上的字段属性不一样，在STATEMENT/MIXED下，不受影响，复制正常，而在ROW下，复制报错。varcar <=> char

主从上的字段长度不一样，在STATEMENT/MIXED下，不受影响，复制正常，而在ROW下，复制报错。varchar(10) <=> varchar(20)

对于情况2，在5.1里面没有办法自动处理复制的错误，但是在[5.5版本中](http://dev.mysql.com/doc/refman/5.5/en/replication-features-differing-tables.html#replication-features-attribute-promotion)增加了一个参数控制：[**slave_type_conversions**](http://dev.mysql.com/doc/refman/5.6/en/replication-options-slave.html#sysvar_slave_type_conversions)

```sql
ALL_LOSSY：仅支持有损转换，比如一个值本来是bigint存储为9999999999999，现在转换为int类型势必会要截断从而导致数据不一致。
ALL_NON_LOSSY：仅支持无损转换，只能在无损的情况下才能进行转换
ALL_LOSSY,ALL_NON_LOSSY：有损/无算转换都支持
空，即不设置这个参数：必须主从的字段类型一模一样。
```

表示允许相同类型字段、长度不同，否则默认为空，会导致主从停止

```sql
View Code 

zjy@localhost : test 01:52:45>show variables like 'slave_type%';
+------------------------+-------+
| Variable_name          | Value |
+------------------------+-------+
| slave_type_conversions |       |
+------------------------+-------+

zjy@localhost : test 01:53:00>set global  slave_type_conversions ='ALL_LOSSY,ALL_NON_LOSSY';
Query OK, 0 rows affected (0.00 sec)

zjy@localhost : test 01:53:30>show variables like 'slave_type%';
+------------------------+-------------------------+
| Variable_name          | Value                   |
+------------------------+-------------------------+
| slave_type_conversions | ALL_LOSSY,ALL_NON_LOSSY |
+------------------------+-------------------------+
```

在从上修改了之后，情况2的复制报错不会再出现。

目前只发现这2个，后期发现再补充进来。

小结3：对于ROW和STATEMENT的复制，ROW在数据的一致性上面要求更好，从库要是提供服务，最好把复制模式改成ROW。

**3，复制下的各种情况:**可以参考[这篇文章](http://www.mysqlperformanceblog.com/2011/12/16/statement-based-replication-with-stored-functions-triggers-and-events/)

对于ROW和STATEMENT下的存储过程，函数，触发器，事件的记录方式有什么区别呢？结果：

```sql
View Code 

触发器（TRIGGER）：
ROW
主上有，从上没有，复制正常，数据正常。
主上有，从上也有，复制正常，数据正常。

STATEMENT/MIXED
主上有，从上没有，复制正常，数据不正常，触发器里面的sql语句没有执行。
主上有，从上也有，复制正常，数据正常。

函数（FUNCTION）：
ROW
主上有，从上没有，复制正常，数据正常。日志里记录的是UDF转换过的结果。
主上有，从上也有，复制正常，数据正常。

STATEMENT/MIXED
主上有，从上没有，复制报错。从不识别UDF函数。
主上有，从上也有，复制正常，数据正常。

存储过程（STORED PROCEDURES）
ROW
主上有，从上没有，复制正常，数据正常。记录的不是call sp，而是SP里面的sql。
主上有，从上也有，复制正常，数据正常。

STATEMENT/MIXED
主上有，从上没有，复制正常，数据正常。记录的不是call sp，而是SP里面的sql。
主上有，从上也有，复制正常，数据正常。

事件（event）：
ROW
主上有，从上没有，复制正常，数据正常。记录的不是计划，而是EVENT里面的sql。
主上有，从上也有，复制正常，数据正常。（默认，DISABLE ON SLAVE），ALTER EVENT event_name ENABLE/DISABLE

STATEMENT/MIXED
主上有，从上没有，复制正常，数据正常。记录的不是计划，而是EVENT里面的sql。
主上有，从上也有，复制正常，数据正常。（默认，DISABLE ON SLAVE）, ALTER EVENT event_name ENABLE/DISABLE
```

小结4：

Event最好在主上，其他的都可以在主从上同时存在，要是人为的操作数据库而修改模式（R-S）也不会出现问题，更能确保数据的一致性。

对于【小结2】和【小结3】，说明了ROW和STATEMENT的各自优势，下面这个功能更能体现出ROW的优势。

**三，****数据回滚:**

误删除、更新的回退

请见：[这里](http://www.cnblogs.com/zhoujinyi/archive/2012/12/26/2834897.html)和[这里](http://www.cnblogs.com/zhoujinyi/archive/2012/12/25/2832543.html)



**总结：**经过上面的分析，到底是使用ROW好还是STATEMENT好？这个需要权衡， 在【小结2】中：

更新一个大范围的SQL，针对STATEMENT没有什么疑问。对比ROW，其磁盘写和网卡流量以及CPU消耗都比较大，特别是一大个范围的sql语句，差距很大，这时候用STATMENT相对来说更好，因为在利用好索引的前提下，STATEMENT更划算。如上面的例子。

更新小数据，比如每次sql更新一条或则几条，ROW和STATMENT差距不是很大。虽然有几倍的差距，但是这些影响对目前的设备来讲也没任何压力。而且利用ROW之后，可以使没有利用好索引的sql，在从上能更好的执行，并且更能保证主从数据的一致性，更诱人的是ROW下可以实现误操作回退的功能。

所以权衡下，有大范围的更新（一般线上很少），人为的去执行，在执行前，把当前session设置成STATEMENT，其余的都用ROW。这样就避免了上面所说的情况。要是线上有这类操作的话，可以让程序先执行 ：

`set session binlog_format=mixed;`


