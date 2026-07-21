---
title: 9．数据库事务有哪些特点？事务隔离级别？项目中的事务怎么实现？脏读、不可重复读、幻读能各举个例子吗？
---

# 9．数据库事务有哪些特点？事务隔离级别？项目中的事务怎么实现？脏读、不可重复读、幻读能各举个例子吗？

数据库事务有以下几个特点:

- 原子性(Atomicity):事务是一个不可分割的工作单位,事务中的操作要么都发生,要么都不发生。
- 一致性(Consistency):事务必须使数据库从一个一致性状态变换到另一个一致性状态。
- 隔离性(Isolation):一个事务的执行不能被其他事务干扰,即一个事务内部的操作及使用的数据对并发的其他事务是隔离的。
- 持久性(Durability):一个事务一旦被提交,它对数据库中数据的改变就是永久性的。
事务隔离级别从低到高依次为:

- 读未提交(Read uncommitted):允许脏读、不可重复读、幻读。
- 读已提交(Read committed):允许不可重复读、幻读。
- 可重复读(Repeatable read):允许幻读。
- 串行化(Serializable):最高隔离级别,完全禁止上述三种情况。
项目中的事务一般通过声明式事务(使用@Transactional注解)或编程式事务(直接使用TransactionTemplate)来实现。

脏读例子:

- T1读取了某个数据,T2修改了该数据,T1再次读取了该数据。T1读取了T2未提交的数据。
不可重复读例子:

- T1读取了某条记录,T2更新了该条记录,T1再次读取同一条记录。T1两次读取的数据不同。
幻读例子:

- T1根据某个条件读取了多条记录,T2插入了满足T1条件的新记录,T1再次读取发现多了新记录。T1的两次查询结果集不同。

使用TransactionTemplate实现事务的示例代码如下:

```java
@Autowired
private TransactionTemplate transactionTemplate;

public void method() {

  transactionTemplate.execute(new TransactionCallbackWithoutResult() {

    @Override
    protected void doInTransactionWithoutResult(TransactionStatus status) {

      // 执行事务中的逻辑
      try {
        // 业务逻辑代码
        dao.insert();

        // 手动抛出异常测试回滚
        throw new Exception("error");

      } catch (Exception e) {
        e.printStackTrace();
        status.setRollbackOnly();
      }

    }

  });

}

```

主要步骤:

1. 通过@Autowired自动注入TransactionTemplate。
1. 调用TransactionTemplate的execute()方法,传入TransactionCallback实例。
1. 在TransactionCallback的doInTransactionWithoutResult()方法中编写事务的业务逻辑。
1. 如果要手动回滚事务,可以通过status.setRollbackOnly()设置回滚标志。
1. 发生异常也会触发事务回滚。
1. 方法执行结束后,事务会自动提交或回滚。
这种通过编程的方式可以更灵活地控制事务,适用于有较复杂事务逻辑的场景。



[3-3 分布式事务终结者 - Alibaba Seata框架介绍](/e7af3d89096841ca91451d4f34cc1d87)

[3-4 Seata如何拆解分布式难题](/576c95ca30b644319c59471abc00327a)

[3-5 Seata AT方案原理-分布式事务的生命周期](/9440432d16a64a2ba11acaeb12d230fb)

[3-6 使用Nacos+Seata搞定分布式事务-搭建Seata服务器](/53d29f243b4a4f4183c7858d1656a2be)

[3-7 使用Nacos+Seata搞定分布式事务-应用集成AT方案](/57afb1050ccd43b99c90bd17b8912346)

[3-8 蚂蚁金服核心分布式解决方案TCC介绍](/761e25cf8d0844faa484e73f55c45c54)

[3-11 Seata TCC三大坑-空回滚、幂等性、悬挂](/e20030e9e2584918ace090de65f6989f)


