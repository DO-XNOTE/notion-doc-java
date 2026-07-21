---
title: 3-1 相同顶级域名的单点登录
---

# 3-1 相同顶级域名的单点登录

[image](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/8be0f536-dccc-408c-bed0-308d5ac622f3/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TPYABIY2%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T225110Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCuFDgHX6wOSzR74Pf644emMBBQASlYYEXNEgr8qUmvyQIgP9ZKrOs1Pf7A%2Fqf9tkBi%2FH8%2BjtJSZL4Emz1%2FdZ3UUEEqiAQIxv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDBebTyXUElr3RN%2FQQyrcA7qoFmx85n%2FsElwewv7nrgfVSaoo%2FH%2BkhwtAgO5yype4ilFNqqYvzPIEC%2FwYO%2FpwrUkDmgrwaged9D6wggBIKA31YJoKO8Sfue8YvksOJtRcTSy93UrFLHdPSnGv5WGrpvvJQwQbEu0U9vbeImw7sE2agwNwEsh4zjctGbsZh6XgMN7lmkGT0a00Jg5eup%2BKbFN%2BAQjjvonXWxH6AiUeMRGTZ9i74%2Bqs0DJEqQbqqmOO6DUL1ZPdrpJWmHq%2BT4LriA%2FzT%2BFr76V77KkTD%2Ftg5hTyLyYDcd%2Fsa7C5F4gxQca7epaRt5GoZ1%2BW%2B7XI%2BOnkt%2F1YwkF%2BKDaT96NRHQE%2BBQoP0wmuLvUAHOQzjWvQji9n6YQ6EhRJBPcIOdjUZl03vDMzNo2sy3HoMLRIBDk%2FxFZYb6zyltjzdsiE64HaW9Pzvhz6XV%2FYwVzCfJ8rHjF%2B3TCPkz3gOWs6GLBTXdJJSvNhrtYAT4OKgauu7fNvFN37Mj5ZuB%2Fa5LmWlHxRyEDPZT3SFantiz3W0lmiLfhTb5dStfiQIfDjfj4JPbdWq3lMy%2FDD1LsYR42iCGY5PnbAF8qEvPJS%2FCjFTha4F90pB%2Fdnpe7Z7SQaEJAqhFolX4ZQedlVubwXqgQvbZy2MNW5%2F9IGOqUBz3GZw6va6K896z1jM8FOnuRCYp2edNi635PzuJKHHD8RlE9TVlHpUKSPJn0hVlAJsjDvsOEamMOYbn11T3yin5nCqSA2zKERpr%2BC8JbvPo4B2DpZVE%2Bej16wbh2ssljdxyIUBq%2BU%2BZQpUUxzutcacYA%2BfSN8%2BQ5EoAHqepNXaQtqK3E0HwoSO0dDZcMN0cHs2LQmQo%2B%2FmqMhRuAcAfLlJ3aWkK%2FY&X-Amz-Signature=ed7b048206df8439715064d036492e75655e93787b3b321d7a6f29980487c8f1&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

3—1相同顶级域名的单点登录SSO
引子
在面试过程中有时候会被问到单点登录，那么单点登录又称之为Single Sign On，简称SSO，单点登录可以通过基于用户会话的共享，
他分文两种，先来看第一种，[那就是他的原理是分布式会话来实现比如说现在有个一级域名为www.imooc.com](http://xn--www-p18dnhqds5ctpl4s3mey8ar4wbmcr5io5icncpwm33eby6bca996bz8b5z2cw96bca93te23a5x7c6b2e4ta547i.imooc.com/)，是教育类网站，但
是慕课网有其他的产品线，可以通过构建二级域名提供服务给用户访问，比如：[music.imooc.com](http://music.imooc.com/),[shop.imooc.com](http://shop.imooc.com/),blog.imoo c.com等等，分别为慕课音乐，慕课电商以及慕课博客等，用户只需要在其中一个站点登录，那么其他站点也会随之而登录。
也就是说，用户自始至终只在某一个网站下登录后，那么他所产生的会话，就共享给了其他的网站，实现了单点网站登录后，同时间接登录了其他的网站，那么这个其实就是单点登录，他们的会话是共享的，都是同一个用户会话。
Cookie +Redis 实 SSO
那么之前我们所实现的分布式会话后端是基于redis的，如此会话可以流窜在后端的任意系统，都能获取到缓存中的用户数据信息，前端通过使用cookie，可以保证在同域名的一级二级下获取，那么这样一来，cookie中的信息userid和token是可以在发送请求的时候携带上的，这样从前端请求后端后是可以获取拿到的，这样一来，其实用户在某一端登录注册以后，其实cookie和redis中都会带有用户信息，只要用户不退出，那么就能在任意一个站点实现登录了。
·那么这个原理主要也是cookie和网站的依赖关系，顶级域名www.imooc.com和*.imooc.com的cookie值是可以共享的 ，可以被携带至后端的，[比如设置为.imooc.com](http://xn--siqv8y8xospsj8n.imooc.com/)，.t.mukewang.com,如此是OK的。
·二级域名自己的独立cookie是不能共享的，不能被其他二级域名获取，比如：music.imooc.com的cookie是不能被mtv .imooc.com共享，两者互不影响，要共享必须设置为.imooc. com.
Cookie共享测试
找到前端项目app.js，开启如下代码，设置你的对应域名，需要和SwitchHosts相互对应：
cookieDomain: " t. mukewang. com;
SwitchHosts!
#foodie R
127.0.0.1 shop. t. mukewang. com 4
127.0.0.1 center.t. mukewang. com
如下图，可以看到，不论是在shop 或是center中，两个站点都能够在用户登录后共享用户信息。
Annleatine
CFilte Name
Value shopca
658967B9622itemld62263A9622cake-
%7B%22id%22%3A%221908148845RYG Storaoe
Seeelon et IndeyedDp Web SQL
[http://shop.t.mukewang.com](http://shop.t.mukewang.com/)
如此一来，cookie中的信息被携带至后端，而后端又实现了分布式会话，那么如此一来，单点登录就实现了，用户无需再跨站点登录了。上述过程我们通过下图来更加具象化的展示，只要前端网页都在同一个顶级域名下，就能实现cookie与session的共享：
[www.imooc.com](http://www.imooc.com/)[music.imooc.com](http://music.imooc.com/)[mtv.imooc.com](http://mtv.imooc.com/) Tomcatt
Tomicat2
Fomcat3 Redis
那么目前我们的系统在经过分布式会话的完成以后，外加cookie设置的配合，就已经能够达到相同顶级域名下的单点登录啦～！



[image](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/177912e0-359e-4b5f-bf09-3c579eed318d/2020-09-17_180132.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TPYABIY2%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T225110Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCuFDgHX6wOSzR74Pf644emMBBQASlYYEXNEgr8qUmvyQIgP9ZKrOs1Pf7A%2Fqf9tkBi%2FH8%2BjtJSZL4Emz1%2FdZ3UUEEqiAQIxv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDBebTyXUElr3RN%2FQQyrcA7qoFmx85n%2FsElwewv7nrgfVSaoo%2FH%2BkhwtAgO5yype4ilFNqqYvzPIEC%2FwYO%2FpwrUkDmgrwaged9D6wggBIKA31YJoKO8Sfue8YvksOJtRcTSy93UrFLHdPSnGv5WGrpvvJQwQbEu0U9vbeImw7sE2agwNwEsh4zjctGbsZh6XgMN7lmkGT0a00Jg5eup%2BKbFN%2BAQjjvonXWxH6AiUeMRGTZ9i74%2Bqs0DJEqQbqqmOO6DUL1ZPdrpJWmHq%2BT4LriA%2FzT%2BFr76V77KkTD%2Ftg5hTyLyYDcd%2Fsa7C5F4gxQca7epaRt5GoZ1%2BW%2B7XI%2BOnkt%2F1YwkF%2BKDaT96NRHQE%2BBQoP0wmuLvUAHOQzjWvQji9n6YQ6EhRJBPcIOdjUZl03vDMzNo2sy3HoMLRIBDk%2FxFZYb6zyltjzdsiE64HaW9Pzvhz6XV%2FYwVzCfJ8rHjF%2B3TCPkz3gOWs6GLBTXdJJSvNhrtYAT4OKgauu7fNvFN37Mj5ZuB%2Fa5LmWlHxRyEDPZT3SFantiz3W0lmiLfhTb5dStfiQIfDjfj4JPbdWq3lMy%2FDD1LsYR42iCGY5PnbAF8qEvPJS%2FCjFTha4F90pB%2Fdnpe7Z7SQaEJAqhFolX4ZQedlVubwXqgQvbZy2MNW5%2F9IGOqUBz3GZw6va6K896z1jM8FOnuRCYp2edNi635PzuJKHHD8RlE9TVlHpUKSPJn0hVlAJsjDvsOEamMOYbn11T3yin5nCqSA2zKERpr%2BC8JbvPo4B2DpZVE%2Bej16wbh2ssljdxyIUBq%2BU%2BZQpUUxzutcacYA%2BfSN8%2BQ5EoAHqepNXaQtqK3E0HwoSO0dDZcMN0cHs2LQmQo%2B%2FmqMhRuAcAfLlJ3aWkK%2FY&X-Amz-Signature=b515e898cdd3aa62b55e1b3aca8e98d3916f0539658891b8046f0b210ba7dabd&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)


