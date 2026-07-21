---
title: 9. 过滤器
---

# 9. 过滤器

[file](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/341876e7-ad13-4e69-9941-d2f01ec7d77d/%E8%BF%87%E6%BB%A4%E5%99%A8%E7%9B%91%E5%90%AC%E5%99%A8%E5%AD%A6%E4%B9%A0.pdf?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TNNWLG33%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T232856Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCICRInpCx%2FyFwkRUnjKBSN3%2FcKWwluNo1WmB%2FlDA%2B%2BqeYAiA5BhX1EC7ug81ksbLZtFg%2BWREPDFnHJJsk%2BMCWC5Kb5iqIBAjG%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMQgpkBV31gZ400gbXKtwDzNvaNPUEP%2B4RDmhF7fzK7UFxVkHjSJOEBcLqhKMydSs%2FfXfWz2ZgknfB%2Fk2VPWPF9JXDWW0e%2BqV8T%2FTvzgZwK0HXwLVGVKA4fKzkBZLW9ecwX0ZrdRD28VKzsdohwBqjGUiaD3b2FS7dLjQ5DYU9R875ITZ6FXbeAveo3NUOTt%2FU2woGKDFQyvIDAnpoh1Zo7Xv5oBIg7ldTGse3KR7rTHMRjxQCYXfUJ7Hi0EaB9TRGI64Ezl7ALi9rhc0T3v4qzpm4emWhvmf%2Fk8Mvy7PL7h90Js0B5AJelh6QiIo3TDkTrgDS21GigaIOISSFW3za7ajtrwB%2FwDmtoRJR9QoMR2lahFJKu%2BwbzhwJ3NYMPeZr9FnKahH2CLzNXFeXpLONIn4%2BAnpfxmAmKlZho0CtoTl5g4cjjx8PsN5C7%2Frrc%2BjI23arung1qVAJL0y4EkQ3bmGFAErmSUcPVg51sed9CLQlWzUlDSyx%2Bj7lF7rb%2B27UTKlRKRfVfG1iRVH9yS3m9PSNkUH0cClPfw8j2i7XJxN%2Fh4JO1%2B2Z7mvK0030pAIeYqDGFX6bqmMPcGsJJtmp4kg3tofP5dpr8xKZfFWHmwz3i%2BGb5kxZ7LqevbRV1RBaVtMdfTJn71n0Q4Mwnbf%2F0gY6pgFc9PtFdjuJOKENpPB6Br0%2Bx9wGbICw3dhcbl1rCO1s%2FVB1i3IVyUndrTDN1LUqLdW2QQdonD6jBJQJbesglpDdzD70Hrt70OCAYoRe1WvAvMZOPFgdYVIZpolKi4iOrWBGbUURZO7AVDiJfqKULeCAqfQT%2Fa8%2ByNA%2FzYQKDcuiUB11%2BCNja%2FDUrAuvGRZVcvoD3aw3f9i9OFcWq9HCD7E4mGPM95Ts&X-Amz-Signature=1048e03edaff68aa08deabc5a4b34e429539343d05cd6bcb124e24fc57c5f5ed&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

```xml
<?xml version="1.0" encoding="UTF-8"?>
<web-app xmlns="http://xmlns.jcp.org/xml/ns/javaee"
         xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
         xsi:schemaLocation="http://xmlns.jcp.org/xml/ns/javaee http://xmlns.jcp.org/xml/ns/javaee/web-app_4_0.xsd"
         version="4.0">

<!--配置过滤器-->
<filter>
        <filter-name>MyFilter</filter-name>
        <filter-class>com.bjsxt.filter.MyFilter</filter-class>
    </filter>
    <filter-mapping>
        <filter-name>MyFilter</filter-name>
        <url-pattern>/*</url-pattern><!--拦截所有的请求-->
</filter-mapping>
<!--配置第二个过滤器-->
<filter>
        <filter-name>MyFilter2</filter-name>
        <filter-class>com.bjsxt.filter.MyFilter2</filter-class>
    </filter>
    <filter-mapping>
        <filter-name>MyFilter2</filter-name>
        <url-pattern>*.do</url-pattern><!--拦截请求中后缀是.do的-->
</filter-mapping>
<!--配置第三个过滤器-->
<filter>
        <filter-name>MyFilter3</filter-name>
        <filter-class>com.bjsxt.filter.MyFilter3</filter-class>
    </filter>
    <filter-mapping>
        <filter-name>MyFilter3</filter-name>
        <url-pattern>/ts.do</url-pattern>
    </filter-mapping>


    <servlet>
        <servlet-name>TestServlet</servlet-name>
        <servlet-class>com.bjsxt.servlet.TestServlet</servlet-class>
    </servlet>
    <servlet-mapping>
        <servlet-name>TestServlet</servlet-name>
        <url-pattern>/ts</url-pattern>
    </servlet-mapping>
</web-app>
```

```java
package com.bjsxt.filter;

import javax.servlet.*;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;
import javax.servlet.http.HttpSession;
import java.io.IOException;

/**
 *过滤器的作用：
*作用：
*对服务接受的请求资源和响应给浏览器资源进行管理
*保护Servlet
 *使用：
*创建一个实现了Filter接口普通JAVA类
*复写接口的方法
*              init方法
*              doFilter方法
*              destory方法
*在web.xml中配置过滤器
*
 *过滤器的生命周期：
*服务器启动到服务器关闭的整个过程
*
 */
public class MyFilter implements Filter{
@Override
    public void init(FilterConfig filterConfig)throws ServletException{
System.out.println("我被初始化了");
}

@Override
    public void doFilter(ServletRequest request, ServletResponse response, FilterChain chain)throws IOException, ServletException{
System.out.println("我被执行了");
        // 设置编码格式
        request.setCharacterEncoding("utf-8");
        response.setContentType("text/html;charset=utf-8");
        // 判断session
        HttpSession hs =((HttpServletRequest)request).getSession();
        if(hs.getAttribute("user")== null) {
            ((HttpServletResponse)response).sendRedirect("/a/login.jsp");
}else{
// 放行
            chain.doFilter(request, response);
}
System.out.println("我被执行了22");

}

@Override
    public void destroy() {
System.out.println("我被销毁了");
}
}

```

```java
package com.bjsxt.filter;

import javax.servlet.*;
import java.io.IOException;

public class MyFilter2 implements Filter{
@Override
    public void init(FilterConfig filterConfig)throws ServletException{
System.out.println("我是MyFilter2初始化...");
}

@Override
    public void doFilter(ServletRequest request, ServletResponse response, FilterChain chain)throws IOException, ServletException{
System.out.println("我是MyFilter2被处理了");
        chain.doFilter(request, response);
        System.out.println("我是MyFilter2执行完成了");
}

@Override
    public void destroy() {
System.out.println("我是MyFilter2被销毁了");
}
}

```

```java
package com.bjsxt.filter;

import javax.servlet.*;
import java.io.IOException;

public class MyFilter3 implements Filter{
@Override
    public void init(FilterConfig filterConfig)throws ServletException{
System.out.println("MyFilter3初始化...");
}

@Override
    public void doFilter(ServletRequest request, ServletResponse response, FilterChain chain)throws IOException, ServletException{
System.out.println("MyFilter3被处理了");
        chain.doFilter(request, response);
        System.out.println("MyFilter3执行完成了");
}

@Override
    public void destroy() {
System.out.println("MyFilter3被销毁了");
}
}

```

```java
package com.bjsxt.servlet;

import javax.servlet.ServletException;
import javax.servlet.http.HttpServlet;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;
import java.io.IOException;

/**
 * guojun
 *
 */
public class TestServlet extends HttpServlet{

@Override
    protected void service(HttpServletRequest req, HttpServletResponse resp)throws ServletException, IOException{
// 设置请求编码格式
        // 设置响应的编码格式
        // 获取请求信息
        // 处理请求信息
        System.out.println("TestServlet.service(我是servlet)");
        // 响应处理结果
}

}

```


