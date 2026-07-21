---
title: 1.mybatis中 #{} 和  ${}  的区别是什么？
---

# 1.mybatis中 #{} 和  ${}  的区别是什么？

主要有以下两点区别:

1. #{} 是预编译处理,会将参数设置到 sql 中的参数位置,${} 是字符串替换。
1. #{} 可以有效的防止 SQL 注入,而 ${} 则不能防止 SQL 注入。
例如:

使用#{}:

```sql
select * from user where id = #{id}

```

会被预编译为:

```sql
select * from user where id = ?

```

参数会设置到这个?位置上。

使用${}:

```sql
select * from user where id = ${id}

```

会直接替换为:

```sql
select * from user where id = 1

```

这样就会有 SQL 注入的风险。

所以一般来说,推荐使用 #{} 进行参数绑定,可以防止 SQL 注入。

