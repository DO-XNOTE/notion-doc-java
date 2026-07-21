---
title: 9.mybatis分页插件的实现原理是什么？
---

# 9.mybatis分页插件的实现原理是什么？

对MyBatis分页插件的实现原理可以简要概括如下:

1. 分页插件会拦截Executor执行SQL语句前,修改SQL语句,在SQL语句后面加上分页的limit条件。
1. 在查询结束后,分页插件会从结果集中取出总记录数,以CalculatingDialect接口实现。
1. 分页插件会把SQL语句执行结果包装成Page对象,Page对象包含了分页相关的数据,如总记录数total、当前页结果list等。
1. 在MyBatis处理结果集时,如果返回类型是Page,则直接返回Page对象。如果返回类型是List,则从Page对象中取出list放到List中并返回。
1. 这样在DAO层你的方法就可以返回Page对象或List对象,透明的实现了分页功能,而不需要手动处理limit和offset。
1. 分页插件默认使用RowBounds进行分页,也可以实现自己的分页逻辑,只需要继承Dialect实现某种数据库对应的分页查询语法。
1. 分页插件是一个Mybatis的拦截器,所以它可以拦截SQL执行过程,修改SQL实现分页。这是它的核心原理。


举一个简单的MyBatis分页插件实现例子:

1. 自定义一个MyBatis拦截器,实现Intercept接口:
```java
public class PageInterceptor implements Interceptor {

  public Object intercept(Invocation invocation) throws Throwable {

    // 原始SQL语句
    String sql = (String) invocation.getArgs()[0];

    // 获取分页参数
    Object parameter = invocation.getArgs()[1];
    int pageNum = (Integer)parameter.get("pageNum");
    int pageSize = (Integer)parameter.get("pageSize");

    // 修改SQL,添加limit条件
    sql = sql + " limit " + (pageNum-1)*pageSize + "," + pageSize;

    // 执行分页SQL
    List result = (List)invocation.proceed();

    // 从结果集中获取总记录数
    int total = getTotalCount(sql);

    return new Page(pageNum, pageSize, total, result);
  }

  // 执行count查询获取总记录数
  private int getTotalCount(String sql) {
    // ...
  }

}

```

1. 在MyBatis配置文件中注册拦截器:
```xml
<plugins>
  <plugin interceptor="com.mybatis.PageInterceptor"/>
</plugins>

```

1. 在 Mapper 接口方法中返回 Page 对象即可:
```java
public interface UserMapper {
  Page<User> selectByPage(Map<String, Object> params);
}

```

这样就可以实现 MyBatis 的分页功能了。

