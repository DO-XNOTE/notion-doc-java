---
title: 3-2 不同顶级域名的单点登录
---

# 3-2 不同顶级域名的单点登录

[image](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/6e44728f-cfd0-4893-8128-c8d968516341/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YPLQM6XD%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T225110Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQD87%2F86wGf2TMKr9sq8zF4z9uIu7oYNgd%2FvKqlTnf2LuQIgdUuyk5bRoJpHPzPHTXb0FXTEmP448IU3qNceCa8XqS4qiAQIxv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDHAu%2BaQmGuAy5xmQoircAwRFWqN7r9KNijkZPjo7fYmaDo%2BJAsWeKiivYHzPB4m44ra24%2Bswdwc38sOF8yJJoH0bforoSYy%2BxkixO8wvpbulDnEPAjSXou4vSOwxOU7kSEWBNxiLiVoVsT1TFw6mfxLuaKBI8KLZu7Pda5SCrk9Gi9M86y%2BXyW%2FSrld8juEuYeyoEa%2BOw5mmKSIAm%2BLUHERV31KU5J89biLtvZpnBGn7Ss31VVdDOwLFrlGIBT6V2xQ4LEN8BJQsc%2FHqiJfbK9njYeqCYmbXoc18s7KaKj9LyGMGxvtFrxIiqfBu3ReYb1VieIGEmZl%2B6kSXbCLdcCG9oVLrDubOguLzrJM8ud7QjyPggGapvEr2ZG9jFpxYIjIyaohlGCUaD0yKVJn7y93zh7xo3jQIA%2BKKNONu2%2FR7bKGdWMBwZcMtDi1OraryQjWt5oX%2FQPOrZDia8T7QKUjPK2ZzKGmrzerRj2oHggFMEnFqMJuPKx7EAXkeKRrIhINyL9fpG6sQuh2Thh%2FBBwQiluqT2Mb1%2FsHVN6Wg8KOlAeuUtsy0cCt1GDZ1zZDTEb%2FEaG8z7YnO0tLPI6R0QPus6VfrD1sBOushN20g5zjFttcndYzQzcBCi6hn5vuO3mlWjO0OfIFQqItSMK23%2F9IGOqUBguAWDxH1W%2Ft0nX7Fo8HeU%2Bd2cZS175xLP579EMyWNVTVaKQMq9APusn2hgxpjO9XXRDr%2FsWh%2FdUkqyvyKrW%2BnnozFK%2F2OxAGiYGJ78YJLq8vwIK9nxP5jY1J5n%2BsO8EVjo7WaefAWPOKj3tZvmBiTYoSB5PUYIzEZmqzknUazYBj1jaTp07LtoYeadsOHi4O1BHYxuqNiYUb6JFq1DWYZGP0kJ%2Fv&X-Amz-Signature=6e141a1dc166d3b1f517ecce324940310a057054b1e969962712ba9e9db3ed42&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

3—2不同顶级域名的单点登录（预习）
顶级域名不同怎么办？
上一节单点登录是基于相同顶级域名做的，那么如果顶级域名都不一样，咋办？比如www.imooc.com要和www.mukewang.com的会 话实现共享，这个时候又该如何？！如下图，这个时候的cookie由于顶级域名不同，就不能实现cookie跨域了，每个站点各自请求到服务端，cookie无法同步。比如，www.imooc.com下的用户发起请 求后会有cookie,[但是他又访问了www.abc.com](http://xn--www-0h9d9nuvp6w0x3b0w0e4jva.abc.com/),由于cookie无法携 带，所以会要你二次登录。
[www.imoac.com](http://www.imoac.com/)[www.abc.com](http://www.abc.com/)[www.123.com](http://www.123.com/) Tomcat
Tomicat2
Fomcat3 Redis
那么遇到顶级域名不同却又要实现单点登录该如何实现呢？我们来参考下面一张图：
[www.imooc.com](http://www.imooc.com/)[www.abc.com](http://www.abc.com/)[www.123.com](http://www.123.com/) Tomicatt
Jomcat2
tomcat3
。 Redis
CAS
如上图所示，多个系统之间的登录会通过一个独立的登录系统去做验证，它就相当于是一个中介公司，整合了所有人，你要看房经过中介允许拿钥匙就行，实现了统一的登录。那么这个就称之为CAS系统，CAS全称为Central Authentication Service即中央认证服务，
是一个单点登录的解决方案，可以用于不同顶级域名之间的单点登录。那么在咱们课程中呢目前的项目结构源码不需要去破坏，我们只需要构建两个静态站点来测试使用即可。
在CAS中的具体的流程参考如下时序图：客户端
MTV系统
MUSIC系统
CAS系统 1.初次访问
2.验证是否登录
3.携带returnUrl跳转至CAS
4.验证未登录 5.显示CAS登录页面
6.用户名密码登录
7.登录成功 8.创建用户会话 创建用户全局门票
10.创建临时票据 回跳并携带临时票据
2.校验临时票据
3.校验井成功
13. 14.用户会话回传
15.保存用户会话 显示登录成功
1.初次访问
2.验证是否登录 3.携带returnUrl请求CAS
4.校验已登录
5.创建临时票据 回跳并携带临时票据
7.校验临时票据
8.校验成功 9.用户会话回传
10.保存用户会话 11.显示登录成功
上图的流程具体分为两阶段，大家先看一下，当做预习，这张图的流程以及具体实现我们会后面视频课中来讲解和完成。


[image](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/e6a6236c-e9f8-4f41-83d3-d3b8c0bcb7d5/2020-09-17_180153.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YPLQM6XD%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T225110Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQD87%2F86wGf2TMKr9sq8zF4z9uIu7oYNgd%2FvKqlTnf2LuQIgdUuyk5bRoJpHPzPHTXb0FXTEmP448IU3qNceCa8XqS4qiAQIxv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDHAu%2BaQmGuAy5xmQoircAwRFWqN7r9KNijkZPjo7fYmaDo%2BJAsWeKiivYHzPB4m44ra24%2Bswdwc38sOF8yJJoH0bforoSYy%2BxkixO8wvpbulDnEPAjSXou4vSOwxOU7kSEWBNxiLiVoVsT1TFw6mfxLuaKBI8KLZu7Pda5SCrk9Gi9M86y%2BXyW%2FSrld8juEuYeyoEa%2BOw5mmKSIAm%2BLUHERV31KU5J89biLtvZpnBGn7Ss31VVdDOwLFrlGIBT6V2xQ4LEN8BJQsc%2FHqiJfbK9njYeqCYmbXoc18s7KaKj9LyGMGxvtFrxIiqfBu3ReYb1VieIGEmZl%2B6kSXbCLdcCG9oVLrDubOguLzrJM8ud7QjyPggGapvEr2ZG9jFpxYIjIyaohlGCUaD0yKVJn7y93zh7xo3jQIA%2BKKNONu2%2FR7bKGdWMBwZcMtDi1OraryQjWt5oX%2FQPOrZDia8T7QKUjPK2ZzKGmrzerRj2oHggFMEnFqMJuPKx7EAXkeKRrIhINyL9fpG6sQuh2Thh%2FBBwQiluqT2Mb1%2FsHVN6Wg8KOlAeuUtsy0cCt1GDZ1zZDTEb%2FEaG8z7YnO0tLPI6R0QPus6VfrD1sBOushN20g5zjFttcndYzQzcBCi6hn5vuO3mlWjO0OfIFQqItSMK23%2F9IGOqUBguAWDxH1W%2Ft0nX7Fo8HeU%2Bd2cZS175xLP579EMyWNVTVaKQMq9APusn2hgxpjO9XXRDr%2FsWh%2FdUkqyvyKrW%2BnnozFK%2F2OxAGiYGJ78YJLq8vwIK9nxP5jY1J5n%2BsO8EVjo7WaefAWPOKj3tZvmBiTYoSB5PUYIzEZmqzknUazYBj1jaTp07LtoYeadsOHi4O1BHYxuqNiYUb6JFq1DWYZGP0kJ%2Fv&X-Amz-Signature=be9ba6165b235cfb591dc4a5b6330b7cfae133af0252c7c8a866fea943f99a30&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

### 


