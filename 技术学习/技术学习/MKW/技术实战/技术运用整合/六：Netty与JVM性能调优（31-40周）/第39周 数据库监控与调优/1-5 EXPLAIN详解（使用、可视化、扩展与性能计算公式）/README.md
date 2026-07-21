---
title: 1-5 EXPLAIN详解（使用、可视化、扩展与性能计算公式）
---

# 1-5 EXPLAIN详解（使用、可视化、扩展与性能计算公式）

[image](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/3e42c4ed-4635-482c-9d5b-ec99b066a6b8/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XUMK24VC%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T230208Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIHE34R4VbtMuwyb9b%2BMN5G2Ze7x8liYUQzuf45tQ8QHRAiEAyOZI2km75kdYcqKSt%2BsQyvV7AV9yY7tzTH6ox0NLKvQqiAQIxv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDN7ETRnrjQMHlS5UjSrcA9aVh2tFQPPDEDYT2RrGzSVoq92z8G98XkKdUdgi9kFQvx1PQhT9L3t97x1qWTdZ5mdGJy8T0CU7qHhElqt%2FT3%2F4tztOlXRavqUesSeqfMJISiHmmP3upnpgwv3N6KLHCXUVsdrAokVq3uGDyL797xgFhDK7BgbAjnRZu0bvlVemWvdz5Soa5EQCcllc5p6So%2BgzbsJTW33jh41B7FNGhdZcO87gKl3mfqbVUZP5YMJeBlMPEvE%2FDsQQdU5mq903n5KIpmd2Q97PYXu0HJ3Qex3v1%2FgTCpTXc5biYaMa011QMQi85b1nfUIM8AnMFJrVBHrvA0C6NiFkpuVFoandQbvxBhkeKr%2FvV%2BvRUJIZo3HvFnGUTNFD%2FPpWMoMZsjWMjUVgHvW2Gw9IkFS6omAkiViLqiQnLEPtfDaPjmlY1cYQoO3OLFkDxQi3ZdloxcMr6qisPa%2FyH%2FUzRCOrOpr3vP4lSCVlo%2B9o6EBd9OLTsHW3Kk%2B%2BBEBTshiZBos3%2BD3DXZSlgL4Lhq1GlYyrt4Q4%2B1yAN9iY1G4Q1ScO60ABeVFmXkcr6eQG48do2TIWLhCB4PW9iG4aEIrwmHXvGcgqCDhspZRNDZI6c8wvY7w1mZH5qDKz9i7LLQdYd2jlMIu6%2F9IGOqUB2tzSNd00sWi5ZdXOSTuyp%2B40zSFzon%2BtQqZh8OKTf2aJxS7Yb584iYtHOeaHxHANxW%2FHXmH%2BCf6pxYiSUykaSiGX18vZ%2FZd4z8z%2BY0LHP%2BKRrnPa7Z1wCppFZRqYMqdv4mIYOG3XGSIZTQmdvwgTZmAmRk3%2BynO%2B54cggh161e1m%2FyFbb0hsPZ0raEjHyCxzPgkFvGjnaYFPdo%2FrPy5sIqGkXmsu&X-Amz-Signature=42a06318931586e39d4af8efa6ac5b54a10f4dbd910ed65c39862157b283aa83&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

[image](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/1af9af0b-e4d7-4ca3-9bb7-1148068ee537/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XUMK24VC%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T230208Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIHE34R4VbtMuwyb9b%2BMN5G2Ze7x8liYUQzuf45tQ8QHRAiEAyOZI2km75kdYcqKSt%2BsQyvV7AV9yY7tzTH6ox0NLKvQqiAQIxv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDN7ETRnrjQMHlS5UjSrcA9aVh2tFQPPDEDYT2RrGzSVoq92z8G98XkKdUdgi9kFQvx1PQhT9L3t97x1qWTdZ5mdGJy8T0CU7qHhElqt%2FT3%2F4tztOlXRavqUesSeqfMJISiHmmP3upnpgwv3N6KLHCXUVsdrAokVq3uGDyL797xgFhDK7BgbAjnRZu0bvlVemWvdz5Soa5EQCcllc5p6So%2BgzbsJTW33jh41B7FNGhdZcO87gKl3mfqbVUZP5YMJeBlMPEvE%2FDsQQdU5mq903n5KIpmd2Q97PYXu0HJ3Qex3v1%2FgTCpTXc5biYaMa011QMQi85b1nfUIM8AnMFJrVBHrvA0C6NiFkpuVFoandQbvxBhkeKr%2FvV%2BvRUJIZo3HvFnGUTNFD%2FPpWMoMZsjWMjUVgHvW2Gw9IkFS6omAkiViLqiQnLEPtfDaPjmlY1cYQoO3OLFkDxQi3ZdloxcMr6qisPa%2FyH%2FUzRCOrOpr3vP4lSCVlo%2B9o6EBd9OLTsHW3Kk%2B%2BBEBTshiZBos3%2BD3DXZSlgL4Lhq1GlYyrt4Q4%2B1yAN9iY1G4Q1ScO60ABeVFmXkcr6eQG48do2TIWLhCB4PW9iG4aEIrwmHXvGcgqCDhspZRNDZI6c8wvY7w1mZH5qDKz9i7LLQdYd2jlMIu6%2F9IGOqUB2tzSNd00sWi5ZdXOSTuyp%2B40zSFzon%2BtQqZh8OKTf2aJxS7Yb584iYtHOeaHxHANxW%2FHXmH%2BCf6pxYiSUykaSiGX18vZ%2FZd4z8z%2BY0LHP%2BKRrnPa7Z1wCppFZRqYMqdv4mIYOG3XGSIZTQmdvwgTZmAmRk3%2BynO%2B54cggh161e1m%2FyFbb0hsPZ0raEjHyCxzPgkFvGjnaYFPdo%2FrPy5sIqGkXmsu&X-Amz-Signature=98292d071d0e04638b4abbe8f82e32371095f345fe2e784e9245a398576bb953&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

[image](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/525d0448-d078-41e9-bac8-ae2490cbae77/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XUMK24VC%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T230208Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIHE34R4VbtMuwyb9b%2BMN5G2Ze7x8liYUQzuf45tQ8QHRAiEAyOZI2km75kdYcqKSt%2BsQyvV7AV9yY7tzTH6ox0NLKvQqiAQIxv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDN7ETRnrjQMHlS5UjSrcA9aVh2tFQPPDEDYT2RrGzSVoq92z8G98XkKdUdgi9kFQvx1PQhT9L3t97x1qWTdZ5mdGJy8T0CU7qHhElqt%2FT3%2F4tztOlXRavqUesSeqfMJISiHmmP3upnpgwv3N6KLHCXUVsdrAokVq3uGDyL797xgFhDK7BgbAjnRZu0bvlVemWvdz5Soa5EQCcllc5p6So%2BgzbsJTW33jh41B7FNGhdZcO87gKl3mfqbVUZP5YMJeBlMPEvE%2FDsQQdU5mq903n5KIpmd2Q97PYXu0HJ3Qex3v1%2FgTCpTXc5biYaMa011QMQi85b1nfUIM8AnMFJrVBHrvA0C6NiFkpuVFoandQbvxBhkeKr%2FvV%2BvRUJIZo3HvFnGUTNFD%2FPpWMoMZsjWMjUVgHvW2Gw9IkFS6omAkiViLqiQnLEPtfDaPjmlY1cYQoO3OLFkDxQi3ZdloxcMr6qisPa%2FyH%2FUzRCOrOpr3vP4lSCVlo%2B9o6EBd9OLTsHW3Kk%2B%2BBEBTshiZBos3%2BD3DXZSlgL4Lhq1GlYyrt4Q4%2B1yAN9iY1G4Q1ScO60ABeVFmXkcr6eQG48do2TIWLhCB4PW9iG4aEIrwmHXvGcgqCDhspZRNDZI6c8wvY7w1mZH5qDKz9i7LLQdYd2jlMIu6%2F9IGOqUB2tzSNd00sWi5ZdXOSTuyp%2B40zSFzon%2BtQqZh8OKTf2aJxS7Yb584iYtHOeaHxHANxW%2FHXmH%2BCf6pxYiSUykaSiGX18vZ%2FZd4z8z%2BY0LHP%2BKRrnPa7Z1wCppFZRqYMqdv4mIYOG3XGSIZTQmdvwgTZmAmRk3%2BynO%2B54cggh161e1m%2FyFbb0hsPZ0raEjHyCxzPgkFvGjnaYFPdo%2FrPy5sIqGkXmsu&X-Amz-Signature=19b7203688c443e65cc8f1b086de63a5497d4f98e3dbd48bd563367eb0cc71b9&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

大家好，我是大木。经过上节课的学习，我们已经能够通过麦查询日志有效的发现 MySQL 了。找到 MySQL 之后的下一步就应该分析它为什么这么慢，并去优化它了，对吧？这个时候， explain 可以闪亮登场了，它可以帮助我们分析 SQL 的执行计划。考虑到 explain 非常的重要，所以我又专门写了一篇，手记一起来看一下。


explain 有三种使用形式，第一种，第二种、第三种。使用最广泛的是第二种形式。演示一下explain，比如 select * from salary where from Bait 等于 19961202 执行，就可以知道这条色格语句它是怎么样执行的了。展示出来的结果有这么些字段，比较重要的字段有这么几个。首先是type，它表示连接使用了哪种类型。连接类型有很多种，性能从好到差。排列是这样子的 system 性能最好， constant 第二， ecariff 第三。以此类推。同学们可以看一下，这里就不去展开了。在调优的时候，应该想办法让 type 保持在性能比较好的级别。一般来，如果你能够把 type 的级别控制在 REF 以及更高，这个的性能应该都是不错的。当然了，这只是经验之谈。


好，继续看。 possible keys 它可以展示 MySQL 可能会使用的索引。如果这一列为空，表示连个可选的索引都没有。 key 表示执行这条 circle 的时候实际会选择的索引。 k 莱斯表示当前使用的索引的长度。一般 k 莱斯的值越小越好。如果你想知道 k 莱斯如何计算，可以看一下这篇文章，里面有完整的分析过程。结论在这里。OK， rose 表示估计要扫描的行数字越小越好。 rose 字段是 explain 里面最重要的性能，和扫描的行数息息相关。在做授课调优的时候，一个原则就是要降低扫描的行数。如果扫描的行数比较多，性能是很难上去的。像咱们这条SQL， rose 是 260 多万行性的，一般是比较差的。


filter 的表示符合查询条件的数据的百分比，这个数值也是越少越好。比较有意思的是，使用 rose 乘以 filter 的就可以获得这张表和下一张表连接的行数。当然了，这个计算出来的值也是一个估算值。另外需要注意的是，如果你能 MySQL 版本低于 5. 7 的话，那么需要用 explain extended 叉叉叉才能展示出 filter 的这一列，否则的话是不展示的。而对于 MySQL 5. 7 以及更高版本，就不需要使用 extend 的关键字了。


最后是extra，可以展示一些额外的信息。 extra 的可选值也是非常多的，有小 20 个，其中最重要的有两个。首先是 using Firesalt，单查询条件里面包含 order by 操作，而且没有办法使用索引去排序，就会展示。 using Firesalt 表示直接使用文件去排序，而使用文件排序性能是比较差的。因此一旦出现 using Firesalt，一般都是要优化的。


第二是 using temporary，它表示 MySQL 使用了临时表，如果你的查询语句里面包含不同列的 group by 和 order by 子句的话，比较容易出现 using temporary。一般来说，一旦出现 using temporary 也是要优化的。其他的选项同学们在遇到的时候可以到手机里面去查询。


OK，现在我们来分析一下 explain 的结果。首先， select type 是simple，表示这是一个简单查询。查询的表是celery， type 是or，表示发生了全表扫描。对照我们的手机可以发现全秒扫描的性能是最差的。 possible keys， key killings 都是空，说明没有使用任何索引。 rose 他说执行这条 circle 的话，需要扫描 200 多万行数据才能返回， filter 的是10%。


最后， extra user where，它表示使用了 where 条件。从这个结果来看，这条 circle 的性能应该是不太好的。我们来执行一下看看。运行点击 output 可以发现，执行这条 SQL 花费了 600 多毫秒，性能果然不太OK，对吧？下面我们再来分析一条社科语句。比如explain。 select theme from employees e left join salaries s， where e 点儿 e m p number 等于一万零一。


you see 从中可以发现， explain 展示了两行结果，当有多行结果的时候，这个 i d 字段还是有用的。它可以描述 circle 的执行过程。如果 explain 的结果包含多个 i d 值，比方 i d 等于 1 以及 i d 等于2，那么数字越大越先执行，也就是 ID 等于 2 的先执行， ID 等于 1 的后执行。而对于相同 ID 的行，比方，咱们这里两段数据的 ID 都等于1，会从上到下依次执行。


好，下面来分析一下这两行结果。其中一条操作了 employees 表，另外一条操作了 salaries 表。由于我们起了别名，所以 table 这一列展示了别名。从 tab 来看，操作 employee is 表的时候是Const，这是一个非常好的级别，可能会使用主键，实际使用的也是主键，并且只扫描了一条数据，因为我们使用的是 e m p number 去查询的。使用 rose 乘以 filter 的等于 1 行，也就是MySQL。它预估会使用 employee is 表的一行数据和 salaries 表去关联。 Tony 操作 salaries 表的时候， tab 是REF， REF 的性能也是不错的，也使用了主键。


最后经过估算，他说需要扫描十七行数据，我们可以执行一下运行。添加 output 可以发现这条 circle 只需要花费六十几毫秒，现在还是不错的，对吧？对于更加复杂的语句，我个人建议使用 tree 的格式去展示，只要这样写就可以了。 format 飞鱼 tree idea 给了我一个错误提示，我们运行一下看看。运行。他报错了。我们把 select 的语句放到后面，不换行，再次执行，这一次能够正常返回结果。这个其实是 idea 对 format 等于 tree 的格式支持的不够完善所导致的。来分析下结果，从结果可以发现，使用 tree 这种格式展示出来的结果更加结构化一些。可以一眼知道 circle 的执行过程以及每一步的开销。比方在这里，他说开销是 1. 95，预估会扫描 17 行。当然了， format 等于 tree 的时候，展示的结果没有表格的形式那么丰富，对吧？另外，你还可以指定 format 等于JSON，这样会以 JSON 的格式展示结果。
好，有关 x plan 还可以发一个福利，分享两款可视化分析 x plan 的工具，可以帮助大家更加轻松的分析 x plan 的结果。第一是使用 idea 可视化分析 explain 的结果。可以这样玩把 explain 给去掉，直接选中这条 select 语句，右击点击explain，这样它会给我们展示一个树状的结果。点击 show virtualization 就可以看到一个图表。这样在分析 x plan 的时候就会轻松一些。


第二是使用 MySQL 官方提供的 MySQL Workbench 去可视化分析。点击 database connect to database，输入数据库的主机名、端口、账号以及密码。注册。123，点击OK。然后把 select 的语句贴到这里来，选中它。再点击放大镜按钮。报了个错，他说 no database selected。所以我们还需要 use 一下employees。先执行在此选中这条色格语句。点击放大镜，这样就会展示出可视化的结果了。 0. 11. 95 等等是执行这一步的开销数字越小越好。 11 row 17 rows 指的是执行这一步的时候， MySQL 预估扫描的行数。OK，这是 explain 回答手记。


explain。还有一个东西叫做扩展的explain，可以为 explain 展示更多的信息，从而帮助我们了解 circle 的更多详情。这个扩展的explain，它和 MySQL 的版本也有关系，同学们可以看一下。使用起来非常的简单。只需要在 explain 一局之后，紧跟一个 show warnings，就可以看到各种扩展信息了。需要注意扩展的 explain 功能，它使用 idea 是没有办法正常演示结果的，必须要在 MySQL 终端里面执行才行。来对比一下。比方，我们想要查看这条 SQL 语句的扩展 explain 信息，理论上应该使用 explain 执行这两四个语句。再使用 show warnings，查看扩展信息，最后发现没有任何的结果。下面我们到 MySQL 中单里面去执行一下看看。


首先用 use employees 选择数据库，接着执行 explain 一句，再使用 show warnings，可以看到是有结果的。从中我们可以发现 MySQL 优化之后的 SQL 语句是这样子的，和我们原始的 SQL 语句差异还是挺大的。比方它直接把在 employee is 表里面查出的结果作为字段了。当然了，现在这个结果里面并没有任何的特殊标记，如果有特殊标记，同学们可以参考我的手记去查询一下。


最后分享一个性能评估公式，在这里。这个公式是由 MySQL 官方提供的，从结果可以看出来，入 count 的越大，性能越差。 index block lens 是 1024 字节，可以不管。 data pointers 一般是 4 字节，也可以不管。 index length 越大，性能也会越差。这也论证了刚刚说的索引长度。 key length 越小，性能越好，对吧？好，有关 x plan 我们就讲到这里，希望同学们经过学习之后能够有能力使用 x plan 分析 SQL 语句。这节课就到这里，谢谢大家。

[image](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/edcd7dde-ac40-436e-9f1a-b5f6ba503829/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XUMK24VC%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T230208Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIHE34R4VbtMuwyb9b%2BMN5G2Ze7x8liYUQzuf45tQ8QHRAiEAyOZI2km75kdYcqKSt%2BsQyvV7AV9yY7tzTH6ox0NLKvQqiAQIxv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDN7ETRnrjQMHlS5UjSrcA9aVh2tFQPPDEDYT2RrGzSVoq92z8G98XkKdUdgi9kFQvx1PQhT9L3t97x1qWTdZ5mdGJy8T0CU7qHhElqt%2FT3%2F4tztOlXRavqUesSeqfMJISiHmmP3upnpgwv3N6KLHCXUVsdrAokVq3uGDyL797xgFhDK7BgbAjnRZu0bvlVemWvdz5Soa5EQCcllc5p6So%2BgzbsJTW33jh41B7FNGhdZcO87gKl3mfqbVUZP5YMJeBlMPEvE%2FDsQQdU5mq903n5KIpmd2Q97PYXu0HJ3Qex3v1%2FgTCpTXc5biYaMa011QMQi85b1nfUIM8AnMFJrVBHrvA0C6NiFkpuVFoandQbvxBhkeKr%2FvV%2BvRUJIZo3HvFnGUTNFD%2FPpWMoMZsjWMjUVgHvW2Gw9IkFS6omAkiViLqiQnLEPtfDaPjmlY1cYQoO3OLFkDxQi3ZdloxcMr6qisPa%2FyH%2FUzRCOrOpr3vP4lSCVlo%2B9o6EBd9OLTsHW3Kk%2B%2BBEBTshiZBos3%2BD3DXZSlgL4Lhq1GlYyrt4Q4%2B1yAN9iY1G4Q1ScO60ABeVFmXkcr6eQG48do2TIWLhCB4PW9iG4aEIrwmHXvGcgqCDhspZRNDZI6c8wvY7w1mZH5qDKz9i7LLQdYd2jlMIu6%2F9IGOqUB2tzSNd00sWi5ZdXOSTuyp%2B40zSFzon%2BtQqZh8OKTf2aJxS7Yb584iYtHOeaHxHANxW%2FHXmH%2BCf6pxYiSUykaSiGX18vZ%2FZd4z8z%2BY0LHP%2BKRrnPa7Z1wCppFZRqYMqdv4mIYOG3XGSIZTQmdvwgTZmAmRk3%2BynO%2B54cggh161e1m%2FyFbb0hsPZ0raEjHyCxzPgkFvGjnaYFPdo%2FrPy5sIqGkXmsu&X-Amz-Signature=1e05423ea0ae0d42c4c2306fe6d0a9a22155dfdb54091219027884ba91e1423d&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)


[image](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/ca82f48e-4dcf-4357-8aa0-968461677dd6/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XUMK24VC%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T230208Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIHE34R4VbtMuwyb9b%2BMN5G2Ze7x8liYUQzuf45tQ8QHRAiEAyOZI2km75kdYcqKSt%2BsQyvV7AV9yY7tzTH6ox0NLKvQqiAQIxv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDN7ETRnrjQMHlS5UjSrcA9aVh2tFQPPDEDYT2RrGzSVoq92z8G98XkKdUdgi9kFQvx1PQhT9L3t97x1qWTdZ5mdGJy8T0CU7qHhElqt%2FT3%2F4tztOlXRavqUesSeqfMJISiHmmP3upnpgwv3N6KLHCXUVsdrAokVq3uGDyL797xgFhDK7BgbAjnRZu0bvlVemWvdz5Soa5EQCcllc5p6So%2BgzbsJTW33jh41B7FNGhdZcO87gKl3mfqbVUZP5YMJeBlMPEvE%2FDsQQdU5mq903n5KIpmd2Q97PYXu0HJ3Qex3v1%2FgTCpTXc5biYaMa011QMQi85b1nfUIM8AnMFJrVBHrvA0C6NiFkpuVFoandQbvxBhkeKr%2FvV%2BvRUJIZo3HvFnGUTNFD%2FPpWMoMZsjWMjUVgHvW2Gw9IkFS6omAkiViLqiQnLEPtfDaPjmlY1cYQoO3OLFkDxQi3ZdloxcMr6qisPa%2FyH%2FUzRCOrOpr3vP4lSCVlo%2B9o6EBd9OLTsHW3Kk%2B%2BBEBTshiZBos3%2BD3DXZSlgL4Lhq1GlYyrt4Q4%2B1yAN9iY1G4Q1ScO60ABeVFmXkcr6eQG48do2TIWLhCB4PW9iG4aEIrwmHXvGcgqCDhspZRNDZI6c8wvY7w1mZH5qDKz9i7LLQdYd2jlMIu6%2F9IGOqUB2tzSNd00sWi5ZdXOSTuyp%2B40zSFzon%2BtQqZh8OKTf2aJxS7Yb584iYtHOeaHxHANxW%2FHXmH%2BCf6pxYiSUykaSiGX18vZ%2FZd4z8z%2BY0LHP%2BKRrnPa7Z1wCppFZRqYMqdv4mIYOG3XGSIZTQmdvwgTZmAmRk3%2BynO%2B54cggh161e1m%2FyFbb0hsPZ0raEjHyCxzPgkFvGjnaYFPdo%2FrPy5sIqGkXmsu&X-Amz-Signature=b08260441cf877aba85e1785f0f866ecab12a0b0797b2b909c851c2c951d65bb&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)




