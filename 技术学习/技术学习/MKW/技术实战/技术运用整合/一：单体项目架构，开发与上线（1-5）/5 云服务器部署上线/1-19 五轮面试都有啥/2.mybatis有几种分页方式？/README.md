---
title: 2.mybatis有几种分页方式？
---

# 2.mybatis有几种分页方式？

MyBatis 有以下几种常见的分页方式:

1. RowBounds 分页
这是 MyBatis 内置的最简单的分页方式,通过在查询方法中传入 RowBounds 参数进行分页。

```java
List<User> findList(RowBounds rowBounds);

```

在调用查询方法时传入 RowBounds 即可:

```java
RowBounds rowBounds = new RowBounds(0, 10);
List<User> list = userMapper.findList(rowBounds);

```

缺点是所有的记录都会被查询出来,之后再进行分页截取,不推荐在大数据量的情况下使用。

1. Limit 分页
通过在 SQL 语句中添加 LIMIT 子句进行分页:

```sql
SELECT * FROM user LIMIT 0,10

```

需要在 SQL 映射文件中直接编写带 LIMIT 的 SQL 语句。

1. PageHelper 分页插件
这是 MyBatis 中最常用的分页插件,可以很方便的对 SQL 语句进行分页操作,无需手动编写 LIMIT 语句。

```java
PageHelper.startPage(1, 10);
List<User> list = userMapper.findList();

```

PageHelper 会自动为查询加上 LIMIT 语句。

1. MyBatis 分页插件
这是 MyBatis 提供的另一个分页插件,基本用法与 PageHelper 类似,但不如 PageHelper 功能强大。

所以综上,MyBatis 分页最佳实践是使用 PageHelper 插件,可以大大简化分页操作,避免手动编写 LIMIT 语句。


