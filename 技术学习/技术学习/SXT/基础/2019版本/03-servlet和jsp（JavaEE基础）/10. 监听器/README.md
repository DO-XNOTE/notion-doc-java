---
title: 10. 监听器
---

# 10. 监听器

[file](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/fce89a9c-430f-4b7e-ae26-228a33a67c9d/%E8%BF%87%E6%BB%A4%E5%99%A8%E7%9B%91%E5%90%AC%E5%99%A8%E5%AD%A6%E4%B9%A0.pdf?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466Y4RS6WBA%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T232857Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIGBnn27cgvLGjQ%2Bftbe4PPlSYXCIrUiGKgykPIY3BHZ8AiAP0FLuZ4KEzZbQJdlk5vwYQWSHqRxFCWKVj%2FYF9%2BBtLSqIBAjG%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIM1CTQbJ5G3JEN8BaGKtwD9PN4kivdE0m8VhD99IjKSnn4FbhY1a%2BH%2FumH9PVfi%2Bx9uAXbW9nM3hj9JgsneFUnPcz2cz8ygOfGj%2B0%2FIOqtWz%2BV3a%2FImZyEZAmXQfelnicavwJBKHEWzCJvsgJP1wCxZSP43iH6s4WwLJDYyn7V4SnNlxf1HlYsptwQN2K%2FJ9be6pDDD2q5MzAKdXOaSnQJOOWCYrSeT8CNg9X6LfPg%2FHO6tx8yd53nUE9bqVfvH0uf%2F19biiWBK5dZzMPneC2AsEIWCEjE94Pr%2FzwZRxvCBkY8NFwFcPmin6oHBrsgjMIRJlzBCEnR8kRwPOj3ZLWS2puHOEUeSespIGOHNidMqjPD2Z9yI6GkNjqv1bmD6hqLgxZqZ7SwKLDWY00Civ9L97d39vFs9B%2FJbHyH%2BTkFbXtvXip4h%2FDrJpn4P4v6bbgUSn%2Fo%2BIDr9aYIYYAS%2FnYjOT%2FX82DWU1VFO9VyKFk0eAKn%2BANIiLwdLB4tsO2xiEYw6hrEoQNPACsND6gOlf5KCkoEHibe8EiTa6zpbc7XyrymRi%2BHv48Qz2EDkbIleTsVuU7Hp2nmtPuMsQGKmm9SM4EYRBiZezaxyRF9ke3Xtgk5Il%2Bhx6Y0Jzr59MKLUnoeg%2FQcEgo5XpWss30wg7n%2F0gY6pgEMr78IqZWOcYWtQ91SuXB1JxhcJpSsv25yKYgPY8QnoblVbD5S3qN6GTEB074NblMttBh%2F0mrpHWStFI9Xr9N9kP1JN%2FZIN0iME3rCa4dUqHofzZkR%2Bmfov6dpuMOJTU%2BflQFkj%2FYdl%2FvVJlWrHc5IjAIatO4llkZn9UrOHnKvoo6f%2F4FCgRzNpzQSTiJoQfM29LyrTxy%2FSoLlvAwdjiI%2FoRRe2isq&X-Amz-Signature=9a0b2ac05fd47174dee625105fcf3ff97d049d1504b8198b8ebd3503830b5b6d&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

```java
package com.bjsxt.listener;

import javax.servlet.*;
import javax.servlet.http.*;

/**
 *我的监听器，用来做服务端请求后的监听处理
*作用:
 *监听作用于对象request, response, application的创建，销毁和内容的改变
*使用：
*创建一个实现了指定接口的java类
*监听request---> ServletRequestListener监听Request对象的创建和销毁
*              requestInitialized(ServletRequestEvent sre) //创建
*              requestDestroyed(ServletRequestEvent sre)  //销毁
*注意：
*形参可以获取监听request对象
*                  sre.getServletRequest()
 *
 *监听request---> ServletRequestAttributeListener监听request作用域的数据的变更
*              attributeAdded(ServletRequestAttributeEvent srae)
 *              attributeRemoved(ServletRequestAttributeEvent srae)
 *              attributeReplaced(ServletRequestAttributeEvent srae)
 *注意：
*形参可以获取被监听的数据
*                   srea.getName()
 *                   srea.getValue()
 *
 *监听session--> HttpSessionListener监听session的创建和销毁
*              sessionCreated(HttpSessionEvent se)  //创建
*              sessionDestroyed(HttpSessionEvent se) //销毁
*注意：
*形参可以获取被监听的session对象
*                   se.getSession()
 *
 *监听session--> HttpSessionAttributeListener监听session的数据变更
*              attributeAdded(HttpSessionBindingEvent event)
 *              attributeRemoved(HttpSessionBindingEvent event)
 *              attributeReplaced(HttpSessionBindingEvent event)
 *注意：
*形参可以获取被监听的数据
*                  event.getName() //获取数据的键名
*                  event.getValue() //获取数据的值
*
 *监听application --->监听ServletContextListener监听application对象的初始化和销毁（是ServletContextListener的别名）
*             contextInitialized(ServletContextEvent sce)初始化 服务器启动
*             contextDestroyed(ServletContextEvent sce)销毁 服务器关闭
*注意：
*形参可以获取当前的application
 *                sce.getServletContext();
 *
 *监听application ---> ServletContextAttributeListener监听的数据的变更
*             attributeAdded(ServletContextAttributeEvent event)
 *             attributeRemoved(ServletContextAttributeEvent event)
 *             attributeReplaced(ServletContextAttributeEvent event)
 *注意：
*形参可以获取当前监听的数据
*                event.getName()获取数据的键名
*                event.getValue()获取数据的值
*
 *在web.xml中配置监听器
*
 *
 *案例：
*      1:统计当前的在线人数
*      2:统计网页浏览次数
*
 *
 */
public class MyListener implements
        ServletRequestListener, ServletRequestAttributeListener,
        HttpSessionListener, HttpSessionAttributeListener,
        ServletContextListener, ServletContextAttributeListener{

// request 对象销毁
    @Override
    public void requestDestroyed(ServletRequestEvent sre) {
//        sre.
        System.out.println("我被销毁了Listener");
}

// request对象初始化
    @Override
    public void requestInitialized(ServletRequestEvent sre) {
//        sre.
        System.out.println("我被创建了Listener");
}
/**----------------------------------------------------------- */
// 监听 request 用户的数据的添加
    @Override
    public void attributeAdded(ServletRequestAttributeEvent srae) {
System.out.println("request中增加一条数据-" + srae.getName()+ ":" + srae.getValue());
}

// 监听 request 用户数据的的删除
    @Override
    public void attributeRemoved(ServletRequestAttributeEvent srae) {

    }

// 监听数据的替换
    @Override
    public void attributeReplaced(ServletRequestAttributeEvent srae) {

    }
/**----------------------------------------------------------- */
// 监听session的创建的
    @Override
    public void sessionCreated(HttpSessionEvent se) {
System.out.println("seeesion被创建了");
}

// 监听session的销毁
    @Override
    public void sessionDestroyed(HttpSessionEvent se) {
System.out.println("session被销毁了");
}
/**---------------------------监听session数据操作-------------------------------- */
// 增加
    @Override
    public void attributeAdded(HttpSessionBindingEvent event) {

    }
// 移除
    @Override
    public void attributeRemoved(HttpSessionBindingEvent event) {

    }
// 替换
    @Override
    public void attributeReplaced(HttpSessionBindingEvent event) {

    }
/**----------------------------ServletContext------------------------------- */
@Override
    public void contextInitialized(ServletContextEvent sce) {
System.out.println("application对象被初始化了");
}

@Override
    public void contextDestroyed(ServletContextEvent sce) {
System.out.println("application对象被销毁了");
}
/**----------------------------ServletContextAttibuteListeners数据的变更/*------------- */
@Override
    public void attributeAdded(ServletContextAttributeEvent event) {
System.out.println("ServletContextAttribute/application中存储的数据： 增加" + event.getName()+ ":" + event.getValue());
}

@Override
    public void attributeRemoved(ServletContextAttributeEvent event) {

    }

@Override
    public void attributeReplaced(ServletContextAttributeEvent event) {

    }
}

```

```java
package com.bjsxt.servlet;

import javax.servlet.ServletContext;
import javax.servlet.ServletException;
import javax.servlet.http.HttpServlet;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;
import javax.servlet.http.HttpSession;
import java.io.IOException;

/**
 *请求servlet
 */
public class TestServlet extends HttpServlet{
@Override
    protected void service(HttpServletRequest req, HttpServletResponse resp)throws ServletException, IOException{
// 获取请求信息
        // 处理请求信息
        req.setAttribute("str", "监听学习");
        HttpSession hs = req.getSession();
        hs.setAttribute("str", "session中增加数据");
        hs.invalidate();
        ServletContext context = this.getServletContext();
        // 响应请求的结果
        resp.getWriter().write("this is listener study yes");

}
}

```

```java
<?xml version="1.0" encoding="UTF-8"?>
<web-app xmlns="http://xmlns.jcp.org/xml/ns/javaee"
         xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
         xsi:schemaLocation="http://xmlns.jcp.org/xml/ns/javaee http://xmlns.jcp.org/xml/ns/javaee/web-app_4_0.xsd"
         version="4.0">

    <servlet>
        <servlet-name>TestServlet</servlet-name>
        <servlet-class>com.bjsxt.servlet.TestServlet</servlet-class>
    </servlet>
    <servlet-mapping>
        <servlet-name>TestServlet</servlet-name>
        <url-pattern>/ts</url-pattern>
    </servlet-mapping>

<!--配置监听器-->
<listener>
        <listener-class>com.bjsxt.listener.MyListener</listener-class>
    </listener>
</web-app>
```


