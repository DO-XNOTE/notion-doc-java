---
title: 10.mybatis如何编写一个自定义插件？
---

# 10.mybatis如何编写一个自定义插件？

编写MyBatis自定义插件的步骤如下:

1. 创建一个实现org.apache.ibatis.plugin包下Interceptor接口的Java类。需要实现该接口的intercept()和plugin()方法。
1. 在intercept()方法中,编写在MyBatis执行SQL语句时需要调用的自定义逻辑代码。可以通过Invocation对象访问SQL、参数等详细信息。
1. 在plugin()方法中,返回自定义拦截器类的实例。这会告诉MyBatis使用哪个拦截器。
1. 在MyBatis配置文件中的<plugins>元素下配置插件。指定拦截器类的完全限定名。
1. 添加拦截器需要的任何属性作为<property>元素。
1. 可以使用@Intercepts等注解指定拦截器的确切调用时机(查询执行前、后、周围)。
1. 将插件JAR文件与MyBatis JAR文件一起构建和部署。拦截器现在会在查询执行时被调用。
总结一下 - 创建拦截器,在MyBatis XML中配置它,注解拦截点,部署为JAR文件,以激活自定义逻辑。


举一个简单的自定义MyBatis插件示例:

1. 创建一个Interceptor实现类:
```java
public class SimpleInterceptor implements Interceptor {

  @Override
  public Object intercept(Invocation invocation) throws Throwable {
    //实现自定义逻辑
    System.out.println("Before query: " + invocation.getMethod());
    Object result = invocation.proceed();
    System.out.println("After query: " + invocation.getMethod());
    return result;
  }

  @Override
  public Object plugin(Object target) {
    return Plugin.wrap(target, this);
  }

}

```

1. 在MyBatis配置文件中注册插件:
```xml
<plugins>
  <plugin interceptor="com.demo.SimpleInterceptor"></plugin>
</plugins>

```

1. 使用@Signature注解指定插件绑定点:
```java
@Intercepts(@Signature(type= Executor.class, method="query",
  args = {MappedStatement.class, Object.class}))

```

这样,SimpleInterceptor会在查询执行前后打印日志。我们就实现了一个简单的MyBatis自定义插件。

