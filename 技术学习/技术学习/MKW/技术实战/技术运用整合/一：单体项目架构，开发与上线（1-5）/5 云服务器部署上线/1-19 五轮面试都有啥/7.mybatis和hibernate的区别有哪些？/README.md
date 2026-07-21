---
title: 7.mybatis和hibernate的区别有哪些？
---

# 7.mybatis和hibernate的区别有哪些？

主要区别有:

1. MyBatis 是一款ORM框架,Hibernate是一款ORM解决方案。MyBatis更加灵活,Hibernate更加自动化。
1. MyBatis允许SQL代码和Java代码的分离,Hibernate要求将实体类与数据库映射文件绑定。MyBatis可以自由编写SQL,Hibernate自动生成SQL。
1. MyBatis是一个半自动的ORM框架,需要开发者自己编写SQL语句。Hibernate是一个全自动的ORM解决方案,可以自动生成SQL语句。
1. MyBatis支持编写自定义SQL,存储过程和高级映射,适合对性能和灵活性有更高要求的项目。Hibernate对对象的维护和跟踪更好,数据库无关性更强,适合要求更简单的CRUD操作项目。
1. MyBatis SQL和代码解藕,减少数据库迁移工作量。Hibernate数据库无关性强,对数据库的操作都转化为对对象的操作。
1. MyBatis有更细粒度的性能优化空间,可针对某些查询进行优化。Hibernate性能优化更复杂,全自动优化空间较小。
1. MyBatis的学习曲线更低,上手较快。Hibernate门槛相对较高,需要掌握复杂的配置与映射关系。
1. MyBatis XML配置信息与SQL语句存在冗余。Hibernate映射文件可重用性及维护性较好。
总体来说,MyBatis更简单灵活,Hibernate更自动全面。需根据项目特点选择使用。

