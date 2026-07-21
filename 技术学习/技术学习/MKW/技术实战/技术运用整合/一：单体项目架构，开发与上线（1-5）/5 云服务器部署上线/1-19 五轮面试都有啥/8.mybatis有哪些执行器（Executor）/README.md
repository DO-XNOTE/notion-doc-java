---
title: 8.mybatis有哪些执行器（Executor）
---

# 8.mybatis有哪些执行器（Executor）

MyBatis有三种主要的执行器(Executor):

1. SimpleExecutor - 简单的执行器,它为每个语句的执行创建一个新的预处理语句(PreparedStatement)。这种执行器适用于SQL较少的简单应用程序。
1. ReuseExecutor - 重用执行器,它重用预处理语句(PreparedStatements)。这种执行器适用于SQL语句数量非常大的复杂应用程序,它可以显著提高性能。
1. BatchExecutor - 批量执行器,它可以批量执行批量更新语句,例如多条INSERT语句。这种执行器可以提高批量插入或更新性能。
另外,MyBatis还支持自定义执行器,如果默认的三种执行器不满足需求,可以实现自己的执行器。

总结一下,SimpleExecutor简单但性能较差;ReuseExecutor重用PreparedStatement性能较好;BatchExecutor适合批处理。实际使用时根据应用场景选择合适的执行器可以提升性能。




MyBatis怎么自定义执行器,原理是什么？

MyBatis可以通过实现org.apache.ibatis.executor.Executor接口来自定义执行器。主要步骤如下:

1. 实现Executor接口,该接口包含查询、更新、批量更新、提交、回滚等方法。
1. 在自定义执行器中实现自己的逻辑,比如覆盖query方法实现自定义的查询执行。
1. 在MyBatis配置文件中指定使用自定义执行器,例如:
<executor type="自定义执行器全类名">

1. 将自定义执行器设置到SqlSessionFactory中。
自定义执行器的原理是通过实现Executor接口,覆盖其方法来定制MyBatis的执行流程。

其中查询方法query是关键,它包含SqlSession、StatementHandler等参数,可以通过它们自定义SQL执行流程。

实现自定义执行器的主要目的是extends MyBatis的执行流程,实现一些特殊的业务逻辑,比如自定义缓存、SQL执行过程插件等。


