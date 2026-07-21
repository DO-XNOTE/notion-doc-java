---
title: 4-13 搭建Keepalived+Lvs+Nginx高可用集群负载均衡 - 配置Master
---

# 4-13 搭建Keepalived+Lvs+Nginx高可用集群负载均衡 - 配置Master

[image](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/12135620-04a1-4331-ae5c-36970efeffad/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662SH6GAQE%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T224922Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIDU%2BV7tFYl97g8XhlZmPwiEfMbGJeWtBZSpv%2BImEcY6FAiEA%2FdBiPDENLhRf4iDAVPze1UsCHMiy53KO4Py1tNRMJIEqiAQIxv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDLXJdNYRP7WtSEqDECrcAwU2gr4Nq57wvdo3KoRv4Mw5IdO7%2F00MJ%2Ft8GcwMOULl%2FjcuWVixx5WovsREZjRaB0I3Ox0oLWOOFArvNomh5rX34tC%2F38uoPJUmlcdx7A6Kkg76zaUm0SWn7AY5EG%2B14A63BF7f73soPdIuN423mjV7YLt4i5JbUP47ka0jtq9NGMGRLrZRfxY%2B6tVf2dq5YKs14sTCs6ua4p19nk9RZuLYTn6oHVqPeknllGek%2FIxMg1uhcB1DuEbh6H%2FLhLbtVYLcxLC70a9ewM058usHtGfoELfKlcyaTEaboXwKpWfeCOFVzAO32Oi8oGSqhNVhTJdPsqbPMwP4nigkN28dvvvf1WF5Rv2usNsCyISnptovVSK5HssTYwPPI0dp4ZOb9Nw2xwjz0J3k1T1nNpvt98w0t5fKRYerNSKYH%2FMlK4qJQTWqOhKXN9nRD1fFCxYLq1pJkrNS8gxsZnlYrcbnbCJaf30JApfjUvrRx2tL5DI1XZOjyShf355kHd0vPhrgROo80s%2BYYGia%2B0aYzoPmAvJ%2B0T%2F4f5vs0rJnxGK3qSFKWVfR%2B7ZCyVBGFpDBQ1%2Ffv2%2Fdqs6UVXNKarLsbPGCk6pzRXbfPEsgGRpq5HCmVG2N3f2pgK4zwN%2F9CG%2BSMP23%2F9IGOqUBS%2FoZs5Jlo7iC7SjnHf8xR6YlNG31p%2BPOdw7Pmk0u26dGE8slcJ20Lx8Ju4wYQiAtTC5ZGvHRjv9NnlFkPzjUTqdMk07WcOzodWMEJyCrrr55KlDEdKUEfenIhffwKbu4K0wtjPmj4cD%2BgcSce%2F2lNc4ORvFoOoUO9kFL2z8nt%2F%2BXNeu7x1WyOR%2FFGR4GSmEJRnYTGITZ6OcdI6RxUASJZawckpKj&X-Amz-Signature=effbc19433217383f99f3bf05ebf1ade2d98c6840299ce2bf41999b9874bc107&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

[image](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/e217ae3b-8030-47af-98c7-45fa36f26475/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662SH6GAQE%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T224922Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIDU%2BV7tFYl97g8XhlZmPwiEfMbGJeWtBZSpv%2BImEcY6FAiEA%2FdBiPDENLhRf4iDAVPze1UsCHMiy53KO4Py1tNRMJIEqiAQIxv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDLXJdNYRP7WtSEqDECrcAwU2gr4Nq57wvdo3KoRv4Mw5IdO7%2F00MJ%2Ft8GcwMOULl%2FjcuWVixx5WovsREZjRaB0I3Ox0oLWOOFArvNomh5rX34tC%2F38uoPJUmlcdx7A6Kkg76zaUm0SWn7AY5EG%2B14A63BF7f73soPdIuN423mjV7YLt4i5JbUP47ka0jtq9NGMGRLrZRfxY%2B6tVf2dq5YKs14sTCs6ua4p19nk9RZuLYTn6oHVqPeknllGek%2FIxMg1uhcB1DuEbh6H%2FLhLbtVYLcxLC70a9ewM058usHtGfoELfKlcyaTEaboXwKpWfeCOFVzAO32Oi8oGSqhNVhTJdPsqbPMwP4nigkN28dvvvf1WF5Rv2usNsCyISnptovVSK5HssTYwPPI0dp4ZOb9Nw2xwjz0J3k1T1nNpvt98w0t5fKRYerNSKYH%2FMlK4qJQTWqOhKXN9nRD1fFCxYLq1pJkrNS8gxsZnlYrcbnbCJaf30JApfjUvrRx2tL5DI1XZOjyShf355kHd0vPhrgROo80s%2BYYGia%2B0aYzoPmAvJ%2B0T%2F4f5vs0rJnxGK3qSFKWVfR%2B7ZCyVBGFpDBQ1%2Ffv2%2Fdqs6UVXNKarLsbPGCk6pzRXbfPEsgGRpq5HCmVG2N3f2pgK4zwN%2F9CG%2BSMP23%2F9IGOqUBS%2FoZs5Jlo7iC7SjnHf8xR6YlNG31p%2BPOdw7Pmk0u26dGE8slcJ20Lx8Ju4wYQiAtTC5ZGvHRjv9NnlFkPzjUTqdMk07WcOzodWMEJyCrrr55KlDEdKUEfenIhffwKbu4K0wtjPmj4cD%2BgcSce%2F2lNc4ORvFoOoUO9kFL2z8nt%2F%2BXNeu7x1WyOR%2FFGR4GSmEJRnYTGITZ6OcdI6RxUASJZawckpKj&X-Amz-Signature=14aba6c6cdb68622dfed5986887becb82fe5bb9dd709ab3c47091b65d5b95706&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

[image](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/c21e2503-0bfb-476c-a0d1-cf5e498371f3/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662SH6GAQE%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T224922Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIDU%2BV7tFYl97g8XhlZmPwiEfMbGJeWtBZSpv%2BImEcY6FAiEA%2FdBiPDENLhRf4iDAVPze1UsCHMiy53KO4Py1tNRMJIEqiAQIxv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDLXJdNYRP7WtSEqDECrcAwU2gr4Nq57wvdo3KoRv4Mw5IdO7%2F00MJ%2Ft8GcwMOULl%2FjcuWVixx5WovsREZjRaB0I3Ox0oLWOOFArvNomh5rX34tC%2F38uoPJUmlcdx7A6Kkg76zaUm0SWn7AY5EG%2B14A63BF7f73soPdIuN423mjV7YLt4i5JbUP47ka0jtq9NGMGRLrZRfxY%2B6tVf2dq5YKs14sTCs6ua4p19nk9RZuLYTn6oHVqPeknllGek%2FIxMg1uhcB1DuEbh6H%2FLhLbtVYLcxLC70a9ewM058usHtGfoELfKlcyaTEaboXwKpWfeCOFVzAO32Oi8oGSqhNVhTJdPsqbPMwP4nigkN28dvvvf1WF5Rv2usNsCyISnptovVSK5HssTYwPPI0dp4ZOb9Nw2xwjz0J3k1T1nNpvt98w0t5fKRYerNSKYH%2FMlK4qJQTWqOhKXN9nRD1fFCxYLq1pJkrNS8gxsZnlYrcbnbCJaf30JApfjUvrRx2tL5DI1XZOjyShf355kHd0vPhrgROo80s%2BYYGia%2B0aYzoPmAvJ%2B0T%2F4f5vs0rJnxGK3qSFKWVfR%2B7ZCyVBGFpDBQ1%2Ffv2%2Fdqs6UVXNKarLsbPGCk6pzRXbfPEsgGRpq5HCmVG2N3f2pgK4zwN%2F9CG%2BSMP23%2F9IGOqUBS%2FoZs5Jlo7iC7SjnHf8xR6YlNG31p%2BPOdw7Pmk0u26dGE8slcJ20Lx8Ju4wYQiAtTC5ZGvHRjv9NnlFkPzjUTqdMk07WcOzodWMEJyCrrr55KlDEdKUEfenIhffwKbu4K0wtjPmj4cD%2BgcSce%2F2lNc4ORvFoOoUO9kFL2z8nt%2F%2BXNeu7x1WyOR%2FFGR4GSmEJRnYTGITZ6OcdI6RxUASJZawckpKj&X-Amz-Signature=e646e552c01ff1e93060cb39f46430176ea0d726c0fe5cc6000a29f212310331&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

那么前面几节课我们是讲了 LVS，并且也是实现了 LVS 的一个 DR 模式，

[image](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/c218bed4-d73d-4f1e-9682-f65a696e9318/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662SH6GAQE%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T224922Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIDU%2BV7tFYl97g8XhlZmPwiEfMbGJeWtBZSpv%2BImEcY6FAiEA%2FdBiPDENLhRf4iDAVPze1UsCHMiy53KO4Py1tNRMJIEqiAQIxv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDLXJdNYRP7WtSEqDECrcAwU2gr4Nq57wvdo3KoRv4Mw5IdO7%2F00MJ%2Ft8GcwMOULl%2FjcuWVixx5WovsREZjRaB0I3Ox0oLWOOFArvNomh5rX34tC%2F38uoPJUmlcdx7A6Kkg76zaUm0SWn7AY5EG%2B14A63BF7f73soPdIuN423mjV7YLt4i5JbUP47ka0jtq9NGMGRLrZRfxY%2B6tVf2dq5YKs14sTCs6ua4p19nk9RZuLYTn6oHVqPeknllGek%2FIxMg1uhcB1DuEbh6H%2FLhLbtVYLcxLC70a9ewM058usHtGfoELfKlcyaTEaboXwKpWfeCOFVzAO32Oi8oGSqhNVhTJdPsqbPMwP4nigkN28dvvvf1WF5Rv2usNsCyISnptovVSK5HssTYwPPI0dp4ZOb9Nw2xwjz0J3k1T1nNpvt98w0t5fKRYerNSKYH%2FMlK4qJQTWqOhKXN9nRD1fFCxYLq1pJkrNS8gxsZnlYrcbnbCJaf30JApfjUvrRx2tL5DI1XZOjyShf355kHd0vPhrgROo80s%2BYYGia%2B0aYzoPmAvJ%2B0T%2F4f5vs0rJnxGK3qSFKWVfR%2B7ZCyVBGFpDBQ1%2Ffv2%2Fdqs6UVXNKarLsbPGCk6pzRXbfPEsgGRpq5HCmVG2N3f2pgK4zwN%2F9CG%2BSMP23%2F9IGOqUBS%2FoZs5Jlo7iC7SjnHf8xR6YlNG31p%2BPOdw7Pmk0u26dGE8slcJ20Lx8Ju4wYQiAtTC5ZGvHRjv9NnlFkPzjUTqdMk07WcOzodWMEJyCrrr55KlDEdKUEfenIhffwKbu4K0wtjPmj4cD%2BgcSce%2F2lNc4ORvFoOoUO9kFL2z8nt%2F%2BXNeu7x1WyOR%2FFGR4GSmEJRnYTGITZ6OcdI6RxUASJZawckpKj&X-Amz-Signature=a13ce529c85ecbd96703fdc8a13bb519dbeb7752b4686281ba249235d9ab549f&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

那么接下来我们来看一下当我们使用单个 LVS 的时候会发生一个什么问题。那么还是一样，用户通过浏览器发送请求到我们的LVS，那么请求拿到以后会分发给我们的流量 server，当请求处理完毕以后，会把相应的报文数据再一次的返回给用户，那么这是我们目前现有的一个架构。那么现在的我们一个 LVS 是单个机子，那么如果说它挂掉了以后，那么它所有的请求都不会到达我们的后端，所以这样子的话，对于用户来讲的话，一旦发生了 LVS 的故障，所有的请求所有的服务都不能够向用户提供了。所以我们会和之前一样，我们会使用 keepalived 的。


当使用 keepalived 的以后，那么这个时候我们就会有两个 LVS 主机了，

[image](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/aa92ba47-6e1b-4309-95fb-488ad8d2eb2f/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662SH6GAQE%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T224922Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIDU%2BV7tFYl97g8XhlZmPwiEfMbGJeWtBZSpv%2BImEcY6FAiEA%2FdBiPDENLhRf4iDAVPze1UsCHMiy53KO4Py1tNRMJIEqiAQIxv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDLXJdNYRP7WtSEqDECrcAwU2gr4Nq57wvdo3KoRv4Mw5IdO7%2F00MJ%2Ft8GcwMOULl%2FjcuWVixx5WovsREZjRaB0I3Ox0oLWOOFArvNomh5rX34tC%2F38uoPJUmlcdx7A6Kkg76zaUm0SWn7AY5EG%2B14A63BF7f73soPdIuN423mjV7YLt4i5JbUP47ka0jtq9NGMGRLrZRfxY%2B6tVf2dq5YKs14sTCs6ua4p19nk9RZuLYTn6oHVqPeknllGek%2FIxMg1uhcB1DuEbh6H%2FLhLbtVYLcxLC70a9ewM058usHtGfoELfKlcyaTEaboXwKpWfeCOFVzAO32Oi8oGSqhNVhTJdPsqbPMwP4nigkN28dvvvf1WF5Rv2usNsCyISnptovVSK5HssTYwPPI0dp4ZOb9Nw2xwjz0J3k1T1nNpvt98w0t5fKRYerNSKYH%2FMlK4qJQTWqOhKXN9nRD1fFCxYLq1pJkrNS8gxsZnlYrcbnbCJaf30JApfjUvrRx2tL5DI1XZOjyShf355kHd0vPhrgROo80s%2BYYGia%2B0aYzoPmAvJ%2B0T%2F4f5vs0rJnxGK3qSFKWVfR%2B7ZCyVBGFpDBQ1%2Ffv2%2Fdqs6UVXNKarLsbPGCk6pzRXbfPEsgGRpq5HCmVG2N3f2pgK4zwN%2F9CG%2BSMP23%2F9IGOqUBS%2FoZs5Jlo7iC7SjnHf8xR6YlNG31p%2BPOdw7Pmk0u26dGE8slcJ20Lx8Ju4wYQiAtTC5ZGvHRjv9NnlFkPzjUTqdMk07WcOzodWMEJyCrrr55KlDEdKUEfenIhffwKbu4K0wtjPmj4cD%2BgcSce%2F2lNc4ORvFoOoUO9kFL2z8nt%2F%2BXNeu7x1WyOR%2FFGR4GSmEJRnYTGITZ6OcdI6RxUASJZawckpKj&X-Amz-Signature=d5f2b525af332d33b67866d19138104adc5272e4cb866e59a2464949ee108e58&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

一台是MASTER，另外一台是BACKUP，是备用机。如果说组织发生故障的话，那么备用机就会充当原先的一个角色，继续的为用户去提供服务。那么这样子的话，主备切换就能够实现一个高可用了。并且当我们使用了 keepalived 的以后，那么当它结合了LBS，它还能够提供对我们后台这些 real server，针对这些真实的服务器做一些健康检查。


如果说我们的 RS 真实服务器宕机了以后，那么它就会把它踢出咱们的集群，如果说它恢复了以后会自动的加入，那么如果说你不使用 keepalived 的，按照我们之前的一种模式的话，那么它是不支持健康检查的，你要去实现自动的剔除的话，那么你就需要自己的去编写脚本去实现。


**那么 keepalived 的话，它其实本身就是为了 LVS 而设置的，它们是可以结合在一起去使用的，它们的匹配度结合度非常的高**。*通过 keepalived 的就能够配置 LVS 与 RS 的关系，比方说负载均衡的算法，持久化连接，健康检查配置等等*，这些我们都可以通过实际的搭建来实现的。**那么目前这个架构的话，其实也是很多公司所采用的一种高可用，高性能的集群负载均衡的方案，**那么接下来我们就一起来实现一下。


那么首先我们先打开虚拟机，那么先来看一下目前虚拟机的话， 151, 171 和 172 是我们之前在配置 LVS DR 模式的时候所使用到的，那么这一台 151 的话我们会把它作为咱们的一个MASTER，另外我又创建了一个152，那么 152 的话会作为我们 LVS 的一个BACKUP，那么这两个机子我们现在都已经是启动好了。那么总共目前是有 4 台，这两块是 151 和158，那么分别对应的两台 LVS。另外还有是我们的真实服务器，也就是 171 和 172 是这两台。


然后为了咱们的一个观察的方面，那么在这里的话我也是把他们的 hostname 修改了，那么一个是 LVS-MASTER ，另外一个是 LVS-BACKUP ，那么这样子的话也是便于大家的一个观看。好。首先一个那么我们要去实现 LVS 加 keepalived 的话，肯定的我们要去安装和配置 keepalived 的，那么在这里的话安装的话我们就不再去演示了，因为我们之前就已经是操作过了。在这边的话，其实我也已经是在我这两台机子上都安装好了这个 keepalived 的。那么在这边我们呢写一下咱们的一个步骤，给大家去回顾一下，复习一下。


那么第一步是上传 keepalived 的，那么第二步的话你应该是要去配置吧，你要是典型杠它有一个config，第三步是 make，第四步是 make install ，那么当我们的一个安装都结束了以后，那么相应的文件它会存在于 etc 下，会放在 etc 下有一个 keepalived 的会在这个里面。那么随后我们就应该要去配置一下在这个目录里面的一个核心配置文件，但是这个核心配置文件的话我们暂时先不备，因为我们会使用到LVS那么最后一个，那么你是第五步。


第五步你是需要去注册，把 keepalived 的注册到我们的一个系统服务，那么这样子的话这个流程就已经是 OK 了。那么这些流程我目前在我当前这 MASTER 和 BACKUP 这两个节点上都已经是做好了，那么现在的话我们就只需要去配置一下我们的核心配置文件，那么进入到 etc 下 keepalived 的，那么随后这个就是当我们安装完毕以后，它所产生的一个核心配置文件，我们只需要对它去做一个相应的配置就可以了，那么随后我们打开这个配置文件，打开以后那么这个文件里面其实我们之前所配过的大家应该都知道，那么这个是 global defense 是全局的一些定义。


那么在这边还是一样，我们都做一下精简，我们只保留 root ip 就可以了，那么在这边那么我们是需要去为他取一个名字，那么这个名字的话我们就取名为 LVS 下划线151。好，随后那么下面就是我们的一个实例了，那么这个实例的话就应该是配置咱们的一个MASTER，那么在这里 MASTER 我们就保留，随后下面是我们的一个网卡的话，那么在这边我也是需要去做一个修改，应该是 ens 三。这个是大家根据自己的一个情况去做一个修改，那么随后这边会有一个虚拟的路由ip，在这里我也去做一个修改，改为 40 亿，那么下面是它的一个权重配比，那么保持它是 100 就可以了，然后它是一个间隔，那么是 1 秒，那么下面是它的一个密码，那么这个我们都保留它的原样就可以了。


那么下面就是配置它的一个虚拟的 ip 了，在这里我们就直接去做一个修改，把它修改为幺九二点幺六八点幺五零，使用这个就可以了。然后下面这两个我们都删掉。OK，那么这个就是我们的一个MASTER。那么现在我们就配置好了，配置好以后这仅仅只是一部分的配置。那么我们之前在做 keepalived 的配置的时候，其实我们把下面的这一部分内容其实全部都删掉了。那么下面的内容其实就是我们 LVS 的一个配置，其中这个 feature server 就是咱们的一个LVS。然后下面还会有一个 real server， real server 就是咱们的RS，也就是对应到我们的真实服务器。


那么目前我们在这里使用的是egygs，所以我们只需要把这里面的内容去做一个配置就可以了，那么在这个里面的话，当前配置文件里面其实会有很多，那么我们保留其中的一份就可以了，然后下面的我们全部都删掉，那么从它的配置文件里面可以看得出来，它总共是配置了有三个，有三个虚拟的server。我们把最后的两台全部都删掉，保留一台。好，OK。随后我们就对它做一个相应的修改。首先我们先来加一个注释，那么这个是写一下，就是配置集群地址访问的ip，另外是还有加端口，那么端口和 Nginx 保持一致，都是80。随后我们在这里写一下，这边访问的就应该是咱们的虚拟 ip 1. 150 空格80，这是它的一个端口，一定要注意在这里是一个空格，它不是一个冒号，你写了冒号的话会配置错误的。随后下一个是一个 delay loop，它其实是一个健康检查的时间，单位，私聊好，随后下一个。那么下一个的话应该能够看得出来，这个 rr 其实就是咱们的一个轮询配置负载均衡的算法，然后默认写一下，默认是轮询。好，OK。


最后再下一个是 lb 看的，那么这个其实就是它的一个类型，那么很明显它在这里写的是一个 NAT，那么我们是什么？是第二，所以我们要去写一下，就是设置 LBS 的模式，我们使用 DR 就可以了。那么在这边总共是有三个选项，一个是 NAT，那么另外一个是 TUN，还有是一个 DR。这个三种模式我们都说过了，那么在这边的话 LB 说一下。 LB 的话其实就是 loadbalance 的一个缩写， LB 就是负载均衡。那么随后再下面一个，那么这个是什么呢？这个是 persistent 蔡帽子。


这个其实也就是绘画持久化的一个时间，那么这个时间的话就是我们之前有说过，所以说保持我们客户端一开始第一次请求和后续的请求它的一个间隔，它的请求的一个持久化时间设置为 10 秒。写一下设置绘画持久化的时间，默认是50，我们改成 5 秒。那么下面一个是协议，这是协议，协议的话其实就是杠小t，这个我们之前在使用ipvsadm 做设置的时候其实就这个啊。


小t，那么这一部分我们都设置好了以后，随后我们再往下，那么下面的话我们就应该要配置一下咱们的真实服务器了，真实服务器的话，其实我们总共是包含了有两台，那么中间这一段内容我们都不需要全部都删掉，那么很明显我们目前的话当前配置文件里面少了一个大括号加一下。

```shell
## 230-lvs-master的配置文件配置（主节点） 

global_defs {

   # 路由 id，当前安装的 keepalived 节点注解的标识符，全局唯一
   router_id lvs_230

}

# 计算机节点
vrrp_instance VI_1 {

    # 表示的状态,当前的 230 的 nginx 的主节点, master/backup
    state MASTER
    # 当前实例绑定的网卡
    interface ens160
    # 保证主备节点一致
    virtual_router_id 51
    # 优先级/ 权重,谁的优先级高,在 master 挂掉以后,就能成为 master
    priority 100
    # 主备之间同步检查的时间间隔,默认是 1s
    advert_int 1
    # 认证授权的密码, 防止非法节点的进入
    authentication {
        auth_type PASS
        auth_pass 1111
    }
    # 虚拟 IP
    virtual_ipaddress {
        192.168.13.231
    }
}

# 配置集群地址访问的 ip+端口，端口和 nginx 保持一致，都是 80
virtual_server 192.168.13.231 80 {
    # 健康检查的时间， 单位：秒
    delay_loop 6
    # 配置负载均衡的类型，默认是轮训
    lb_algo rr
    # 设置 LVS 模式的 NAT | TUN | DR
    lb_kind NAT
    # 设置会话持久化时间
    persistence_timeout 5
    # 协议 -t
    protocol TCP

    #f 负载均衡的真实服务器，也就是nginx节点的具体的真实的 ip 地址
    real_server 192.168.13.225 80 {
        # 轮训的默认权重比设置为 1
        weight 1
        # 设置健康检查
        TCP_CHECK {
          # 检查的 80 端口
          connect_port 80
          # 超时时间
          connect_timeout 2
          # 重试次数 2 次
          nb_get_retry
          # 间隔时间 3 s
          delay_before_retry 3
        }
    }

    real_server 192.168.13.226 80 {
         # 轮训的默认权重比设置为 1
        weight 1
        # 设置健康检查
        TCP_CHECK {
          # 检查的 80 端口
          connect_port 80
          # 超时时间
          connect_timeout 2
          # 重试次数 2 次
          nb_get_retry
          # 间隔时间 3 s
          delay_before_retry 3
        }
    }
}
```

那么这样子这是我们在其中的一台 real server，我们要去做一个修改，我们要把它改为咱们的171，随后空格80，这是它的一个端口，那么它会有一个 weight 权重，那么我们在使用轮询的时候，那么轮询的一个权重默认我们有多少台，所以说只有多少个 1 就可以了。随后我们在它的一个下方可以再去拷贝一份新的，把这个拷贝一下，那么这样子的话就是我们的第二台，我们只需要把这个 172 设置一下改掉就可以了。


那么这样子的话，其实我们整体的配置就已经是好了，只不过我们还能够再做一个额外的配置，也就是我们之前所说的，它就要做一个健康检查。在这里写一下，我们先把这个注释先加一下，应该是负载均衡的真实服务器，也就是安杰克斯节点的具体的真实 ip 地址，然后 weight 这是轮询，轮询的默认权重配比设置为 1 就可以了。


好，随后下一个，那么当我们设置完这个 is 以后，那么在这个里面其实我们可以设置一个健康检查，设置健康检查，那么这个设置的一个健康检查的话，其实我们是针对的，也是当前的协议是TCP，它有一个叫做 TCP 下划线，然后给它加上一个大括号。在这个 TCP check 里面我们可以去做一些相应的内容配置，比方说它有一个叫做连接的端口，因为我们需要设置它的一个端口号，根据它的端口号去做检测的，所以我们要去设计一下叫做 connetc 下划线。


port 设置是 80 端口，这是检查的 80 端口，那么这个其实也就是和我们在这里的一个 80 是相对应的，都是80，希望下一个，那么下一个的话我们应该要设置它的一个检查的超时时间，超时间的话它叫做connetc，先 connetc 写错了它是etc，随后这个超时时间是 time out，那么我们可以设置为 2 秒稍微的短一些。然后再来一个，它还有一个重试的次数，从事次数。重试次数的话我们可以把它设置为两次，那么一般来说你可以设置为五次或者六次，可以稍微多一些，那么这里的话我们是为它做的一个测试，所以我们的像这个超时间和次数的话，我们可以设置的尽量的短一些你就可以了。


它是 NB 下划线，它有一个 get 与try，获得它的一个重试的次数与 try 的次数。好还有一个，那么最后一个是它的一个间隔时间，间隔时间的话是 delay 下划线，它有一个 before we try，其实我们都可以通过它的一个字面意思上可以翻译出来是在于 try 之前的一个时间间隔，那么在这边设置为 3 秒，这个是两次超市时间 2 秒。


那么这样子的话我们就已经是设置好了它的一个健康检查，随后我们可以把这段内容拷贝一下，拷贝一下以后那么我们可以给他的一个下面一台给到下面一台，也可以去做它的一个健康检查拷贝过来，那么这样子就 OK 了。然后我们附带要说一下，当我们在这个里面去做一些配置的时候，你会发现像 weight 后面还有是配置一些端口号的，后面它是没有分号的，它是直接一个回车就可以了，那么这样子的话我们的配置就已经是 OK 了，然后我们保存退出，那么保存退出以后，那么这个时候我们应该要针对这个 ipvsadm 我们要去做一个清除。


先来看一下咱们的帮助文档，

[image](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/1b468430-5482-459a-bbb3-30637a560a71/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662SH6GAQE%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T224922Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIDU%2BV7tFYl97g8XhlZmPwiEfMbGJeWtBZSpv%2BImEcY6FAiEA%2FdBiPDENLhRf4iDAVPze1UsCHMiy53KO4Py1tNRMJIEqiAQIxv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDLXJdNYRP7WtSEqDECrcAwU2gr4Nq57wvdo3KoRv4Mw5IdO7%2F00MJ%2Ft8GcwMOULl%2FjcuWVixx5WovsREZjRaB0I3Ox0oLWOOFArvNomh5rX34tC%2F38uoPJUmlcdx7A6Kkg76zaUm0SWn7AY5EG%2B14A63BF7f73soPdIuN423mjV7YLt4i5JbUP47ka0jtq9NGMGRLrZRfxY%2B6tVf2dq5YKs14sTCs6ua4p19nk9RZuLYTn6oHVqPeknllGek%2FIxMg1uhcB1DuEbh6H%2FLhLbtVYLcxLC70a9ewM058usHtGfoELfKlcyaTEaboXwKpWfeCOFVzAO32Oi8oGSqhNVhTJdPsqbPMwP4nigkN28dvvvf1WF5Rv2usNsCyISnptovVSK5HssTYwPPI0dp4ZOb9Nw2xwjz0J3k1T1nNpvt98w0t5fKRYerNSKYH%2FMlK4qJQTWqOhKXN9nRD1fFCxYLq1pJkrNS8gxsZnlYrcbnbCJaf30JApfjUvrRx2tL5DI1XZOjyShf355kHd0vPhrgROo80s%2BYYGia%2B0aYzoPmAvJ%2B0T%2F4f5vs0rJnxGK3qSFKWVfR%2B7ZCyVBGFpDBQ1%2Ffv2%2Fdqs6UVXNKarLsbPGCk6pzRXbfPEsgGRpq5HCmVG2N3f2pgK4zwN%2F9CG%2BSMP23%2F9IGOqUBS%2FoZs5Jlo7iC7SjnHf8xR6YlNG31p%2BPOdw7Pmk0u26dGE8slcJ20Lx8Ju4wYQiAtTC5ZGvHRjv9NnlFkPzjUTqdMk07WcOzodWMEJyCrrr55KlDEdKUEfenIhffwKbu4K0wtjPmj4cD%2BgcSce%2F2lNc4ORvFoOoUO9kFL2z8nt%2F%2BXNeu7x1WyOR%2FFGR4GSmEJRnYTGITZ6OcdI6RxUASJZawckpKj&X-Amz-Signature=be15d13fed20d96a4556a59718bce1725b19e7d13d99501099f85542eebaf404&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

[image](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/ac73a51a-0fae-4d4a-8980-0372fbbe2610/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662SH6GAQE%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T224922Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIDU%2BV7tFYl97g8XhlZmPwiEfMbGJeWtBZSpv%2BImEcY6FAiEA%2FdBiPDENLhRf4iDAVPze1UsCHMiy53KO4Py1tNRMJIEqiAQIxv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDLXJdNYRP7WtSEqDECrcAwU2gr4Nq57wvdo3KoRv4Mw5IdO7%2F00MJ%2Ft8GcwMOULl%2FjcuWVixx5WovsREZjRaB0I3Ox0oLWOOFArvNomh5rX34tC%2F38uoPJUmlcdx7A6Kkg76zaUm0SWn7AY5EG%2B14A63BF7f73soPdIuN423mjV7YLt4i5JbUP47ka0jtq9NGMGRLrZRfxY%2B6tVf2dq5YKs14sTCs6ua4p19nk9RZuLYTn6oHVqPeknllGek%2FIxMg1uhcB1DuEbh6H%2FLhLbtVYLcxLC70a9ewM058usHtGfoELfKlcyaTEaboXwKpWfeCOFVzAO32Oi8oGSqhNVhTJdPsqbPMwP4nigkN28dvvvf1WF5Rv2usNsCyISnptovVSK5HssTYwPPI0dp4ZOb9Nw2xwjz0J3k1T1nNpvt98w0t5fKRYerNSKYH%2FMlK4qJQTWqOhKXN9nRD1fFCxYLq1pJkrNS8gxsZnlYrcbnbCJaf30JApfjUvrRx2tL5DI1XZOjyShf355kHd0vPhrgROo80s%2BYYGia%2B0aYzoPmAvJ%2B0T%2F4f5vs0rJnxGK3qSFKWVfR%2B7ZCyVBGFpDBQ1%2Ffv2%2Fdqs6UVXNKarLsbPGCk6pzRXbfPEsgGRpq5HCmVG2N3f2pgK4zwN%2F9CG%2BSMP23%2F9IGOqUBS%2FoZs5Jlo7iC7SjnHf8xR6YlNG31p%2BPOdw7Pmk0u26dGE8slcJ20Lx8Ju4wYQiAtTC5ZGvHRjv9NnlFkPzjUTqdMk07WcOzodWMEJyCrrr55KlDEdKUEfenIhffwKbu4K0wtjPmj4cD%2BgcSce%2F2lNc4ORvFoOoUO9kFL2z8nt%2F%2BXNeu7x1WyOR%2FFGR4GSmEJRnYTGITZ6OcdI6RxUASJZawckpKj&X-Amz-Signature=cedd66561eded9ac225181c952431cf90cd3b8c4371361f986605d3186892bde&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

这里面会有一个肯列，也就是杠大c，那么这个是清楚我们目前的一个负载追求的规则，

[image](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/278e124f-f0ae-4e05-849c-9f21c2b9df34/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662SH6GAQE%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T224923Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIDU%2BV7tFYl97g8XhlZmPwiEfMbGJeWtBZSpv%2BImEcY6FAiEA%2FdBiPDENLhRf4iDAVPze1UsCHMiy53KO4Py1tNRMJIEqiAQIxv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDLXJdNYRP7WtSEqDECrcAwU2gr4Nq57wvdo3KoRv4Mw5IdO7%2F00MJ%2Ft8GcwMOULl%2FjcuWVixx5WovsREZjRaB0I3Ox0oLWOOFArvNomh5rX34tC%2F38uoPJUmlcdx7A6Kkg76zaUm0SWn7AY5EG%2B14A63BF7f73soPdIuN423mjV7YLt4i5JbUP47ka0jtq9NGMGRLrZRfxY%2B6tVf2dq5YKs14sTCs6ua4p19nk9RZuLYTn6oHVqPeknllGek%2FIxMg1uhcB1DuEbh6H%2FLhLbtVYLcxLC70a9ewM058usHtGfoELfKlcyaTEaboXwKpWfeCOFVzAO32Oi8oGSqhNVhTJdPsqbPMwP4nigkN28dvvvf1WF5Rv2usNsCyISnptovVSK5HssTYwPPI0dp4ZOb9Nw2xwjz0J3k1T1nNpvt98w0t5fKRYerNSKYH%2FMlK4qJQTWqOhKXN9nRD1fFCxYLq1pJkrNS8gxsZnlYrcbnbCJaf30JApfjUvrRx2tL5DI1XZOjyShf355kHd0vPhrgROo80s%2BYYGia%2B0aYzoPmAvJ%2B0T%2F4f5vs0rJnxGK3qSFKWVfR%2B7ZCyVBGFpDBQ1%2Ffv2%2Fdqs6UVXNKarLsbPGCk6pzRXbfPEsgGRpq5HCmVG2N3f2pgK4zwN%2F9CG%2BSMP23%2F9IGOqUBS%2FoZs5Jlo7iC7SjnHf8xR6YlNG31p%2BPOdw7Pmk0u26dGE8slcJ20Lx8Ju4wYQiAtTC5ZGvHRjv9NnlFkPzjUTqdMk07WcOzodWMEJyCrrr55KlDEdKUEfenIhffwKbu4K0wtjPmj4cD%2BgcSce%2F2lNc4ORvFoOoUO9kFL2z8nt%2F%2BXNeu7x1WyOR%2FFGR4GSmEJRnYTGITZ6OcdI6RxUASJZawckpKj&X-Amz-Signature=891b81cb4bd276f3f9956423762752021012bc55fdcc0f2cbc716183925fb9ff&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

也就是我们之前所配置的，那么这些内容的话我们直接全部都清掉，所以我们可以来敲一下来一个杠大c，那么这个时候他会把我们目前现有的一个规则去清掉的。清掉了以后，那么这个时候我们再来看一下杠大写的l，再来一个n，你会发现我们的规则这个整个规则是清空了。

[image](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/889c30fc-d93a-4b6a-9ce8-3b4b5639ffac/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662SH6GAQE%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T224923Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIDU%2BV7tFYl97g8XhlZmPwiEfMbGJeWtBZSpv%2BImEcY6FAiEA%2FdBiPDENLhRf4iDAVPze1UsCHMiy53KO4Py1tNRMJIEqiAQIxv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDLXJdNYRP7WtSEqDECrcAwU2gr4Nq57wvdo3KoRv4Mw5IdO7%2F00MJ%2Ft8GcwMOULl%2FjcuWVixx5WovsREZjRaB0I3Ox0oLWOOFArvNomh5rX34tC%2F38uoPJUmlcdx7A6Kkg76zaUm0SWn7AY5EG%2B14A63BF7f73soPdIuN423mjV7YLt4i5JbUP47ka0jtq9NGMGRLrZRfxY%2B6tVf2dq5YKs14sTCs6ua4p19nk9RZuLYTn6oHVqPeknllGek%2FIxMg1uhcB1DuEbh6H%2FLhLbtVYLcxLC70a9ewM058usHtGfoELfKlcyaTEaboXwKpWfeCOFVzAO32Oi8oGSqhNVhTJdPsqbPMwP4nigkN28dvvvf1WF5Rv2usNsCyISnptovVSK5HssTYwPPI0dp4ZOb9Nw2xwjz0J3k1T1nNpvt98w0t5fKRYerNSKYH%2FMlK4qJQTWqOhKXN9nRD1fFCxYLq1pJkrNS8gxsZnlYrcbnbCJaf30JApfjUvrRx2tL5DI1XZOjyShf355kHd0vPhrgROo80s%2BYYGia%2B0aYzoPmAvJ%2B0T%2F4f5vs0rJnxGK3qSFKWVfR%2B7ZCyVBGFpDBQ1%2Ffv2%2Fdqs6UVXNKarLsbPGCk6pzRXbfPEsgGRpq5HCmVG2N3f2pgK4zwN%2F9CG%2BSMP23%2F9IGOqUBS%2FoZs5Jlo7iC7SjnHf8xR6YlNG31p%2BPOdw7Pmk0u26dGE8slcJ20Lx8Ju4wYQiAtTC5ZGvHRjv9NnlFkPzjUTqdMk07WcOzodWMEJyCrrr55KlDEdKUEfenIhffwKbu4K0wtjPmj4cD%2BgcSce%2F2lNc4ORvFoOoUO9kFL2z8nt%2F%2BXNeu7x1WyOR%2FFGR4GSmEJRnYTGITZ6OcdI6RxUASJZawckpKj&X-Amz-Signature=b9e8c411ff7b2d979ddbf5c47adcc2091cb8fc45e8e555d59ea5b472c6ae89ac&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

[image](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/52cc980a-30ae-4ccb-9e4a-975ad1eeeed5/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662SH6GAQE%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T224923Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIDU%2BV7tFYl97g8XhlZmPwiEfMbGJeWtBZSpv%2BImEcY6FAiEA%2FdBiPDENLhRf4iDAVPze1UsCHMiy53KO4Py1tNRMJIEqiAQIxv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDLXJdNYRP7WtSEqDECrcAwU2gr4Nq57wvdo3KoRv4Mw5IdO7%2F00MJ%2Ft8GcwMOULl%2FjcuWVixx5WovsREZjRaB0I3Ox0oLWOOFArvNomh5rX34tC%2F38uoPJUmlcdx7A6Kkg76zaUm0SWn7AY5EG%2B14A63BF7f73soPdIuN423mjV7YLt4i5JbUP47ka0jtq9NGMGRLrZRfxY%2B6tVf2dq5YKs14sTCs6ua4p19nk9RZuLYTn6oHVqPeknllGek%2FIxMg1uhcB1DuEbh6H%2FLhLbtVYLcxLC70a9ewM058usHtGfoELfKlcyaTEaboXwKpWfeCOFVzAO32Oi8oGSqhNVhTJdPsqbPMwP4nigkN28dvvvf1WF5Rv2usNsCyISnptovVSK5HssTYwPPI0dp4ZOb9Nw2xwjz0J3k1T1nNpvt98w0t5fKRYerNSKYH%2FMlK4qJQTWqOhKXN9nRD1fFCxYLq1pJkrNS8gxsZnlYrcbnbCJaf30JApfjUvrRx2tL5DI1XZOjyShf355kHd0vPhrgROo80s%2BYYGia%2B0aYzoPmAvJ%2B0T%2F4f5vs0rJnxGK3qSFKWVfR%2B7ZCyVBGFpDBQ1%2Ffv2%2Fdqs6UVXNKarLsbPGCk6pzRXbfPEsgGRpq5HCmVG2N3f2pgK4zwN%2F9CG%2BSMP23%2F9IGOqUBS%2FoZs5Jlo7iC7SjnHf8xR6YlNG31p%2BPOdw7Pmk0u26dGE8slcJ20Lx8Ju4wYQiAtTC5ZGvHRjv9NnlFkPzjUTqdMk07WcOzodWMEJyCrrr55KlDEdKUEfenIhffwKbu4K0wtjPmj4cD%2BgcSce%2F2lNc4ORvFoOoUO9kFL2z8nt%2F%2BXNeu7x1WyOR%2FFGR4GSmEJRnYTGITZ6OcdI6RxUASJZawckpKj&X-Amz-Signature=68ae3e8692d50ae63127a8ed07ca86c705bdc78e2affc4f00a9786441015f9a6&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

好，那么接下来的话我们就可以去做一个重启。我们是需要去重启一下咱们的 keepalived 的这个服务，从此以后我们刚刚所设置的这些内容就会生效了。那么我们在这里把这个 keepalived 的服务重新启动一下。几周一下之后，我们再来看一下 -Ln，然后你会发现在我们这里面集群的列表并没有。那么我们可以回顾一下我们之前在使用LVS。在配置 DR 模式的时候，我们第一步应该是杠大 a 添加一个集群，第二步是添加一个 s 服务器，也就是杠小a。那么很明显杠大 a 我们连它的一个集群的虚拟ip，它的一个地址都找不到，那就说明其实相应的在 keepalived 的它的配置文件里面，那么我们就配错了，所以我们可以进去再去检查一下，那么可以往上面找到我们配置的维修server，在这个位置你会发现我们在这边很明显是配置错误，这个并不是一个 ip 地址，它漏掉了点1，所以我们在这里再去添加一下点1点幺零。


如果说是错误的一个ip，那么我们的 keepalived 它去启动的时候，它其实并没有发现这样的一个错误ip，它是找不到的，所以相应的 LVS 它也是启动不了，所以把这个改正确就可以了，改正确重新的去保存以后我们再一次的去重启一下 keepalived 这个服务。

[image](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/50e23572-7364-4472-ada5-11005e8e6a67/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662SH6GAQE%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T224923Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIDU%2BV7tFYl97g8XhlZmPwiEfMbGJeWtBZSpv%2BImEcY6FAiEA%2FdBiPDENLhRf4iDAVPze1UsCHMiy53KO4Py1tNRMJIEqiAQIxv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDLXJdNYRP7WtSEqDECrcAwU2gr4Nq57wvdo3KoRv4Mw5IdO7%2F00MJ%2Ft8GcwMOULl%2FjcuWVixx5WovsREZjRaB0I3Ox0oLWOOFArvNomh5rX34tC%2F38uoPJUmlcdx7A6Kkg76zaUm0SWn7AY5EG%2B14A63BF7f73soPdIuN423mjV7YLt4i5JbUP47ka0jtq9NGMGRLrZRfxY%2B6tVf2dq5YKs14sTCs6ua4p19nk9RZuLYTn6oHVqPeknllGek%2FIxMg1uhcB1DuEbh6H%2FLhLbtVYLcxLC70a9ewM058usHtGfoELfKlcyaTEaboXwKpWfeCOFVzAO32Oi8oGSqhNVhTJdPsqbPMwP4nigkN28dvvvf1WF5Rv2usNsCyISnptovVSK5HssTYwPPI0dp4ZOb9Nw2xwjz0J3k1T1nNpvt98w0t5fKRYerNSKYH%2FMlK4qJQTWqOhKXN9nRD1fFCxYLq1pJkrNS8gxsZnlYrcbnbCJaf30JApfjUvrRx2tL5DI1XZOjyShf355kHd0vPhrgROo80s%2BYYGia%2B0aYzoPmAvJ%2B0T%2F4f5vs0rJnxGK3qSFKWVfR%2B7ZCyVBGFpDBQ1%2Ffv2%2Fdqs6UVXNKarLsbPGCk6pzRXbfPEsgGRpq5HCmVG2N3f2pgK4zwN%2F9CG%2BSMP23%2F9IGOqUBS%2FoZs5Jlo7iC7SjnHf8xR6YlNG31p%2BPOdw7Pmk0u26dGE8slcJ20Lx8Ju4wYQiAtTC5ZGvHRjv9NnlFkPzjUTqdMk07WcOzodWMEJyCrrr55KlDEdKUEfenIhffwKbu4K0wtjPmj4cD%2BgcSce%2F2lNc4ORvFoOoUO9kFL2z8nt%2F%2BXNeu7x1WyOR%2FFGR4GSmEJRnYTGITZ6OcdI6RxUASJZawckpKj&X-Amz-Signature=8a74caaf244a389e80f33cbfe3c5a046e756795c7c5ffd19d52551a0514ed025&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

好，重启成功，然后再来看一下我们的  -Ln，这个时候你会发现咱们现在设置的内容就已经是有了，那么这个是咱们的一个集群的一个地址，随后它下面挂着的两个 RS 服务器也都有，一个是171。另外在这里你会看到它的一个 persistent 是 5 秒。好，所以我们现在就可以来做一个测试了。那么这个是 LVS . com，我们进来之后直接刷新一下，你会发现我们这个服务现在是可以正常的访问。



