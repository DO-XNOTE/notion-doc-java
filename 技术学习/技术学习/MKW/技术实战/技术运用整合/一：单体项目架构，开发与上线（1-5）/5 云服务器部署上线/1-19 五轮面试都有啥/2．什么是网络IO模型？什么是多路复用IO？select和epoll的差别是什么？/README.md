---
title: 2．什么是网络IO模型？什么是多路复用IO？select和epoll的差别是什么？
---

# 2．什么是网络IO模型？什么是多路复用IO？select和epoll的差别是什么？

网络IO模型主要有以下几种:

1. 阻塞IO(Blocking IO):每个socket连接都需要独立的线程来处理,如果线程正在进行IO操作则会被阻塞。这种模型直接简单,但当连接数增多时系统无法承受。
1. 非阻塞IO(Non-blocking IO):通过设置socket为非阻塞模式,然后不断的轮询每个socket的状态来判断IO操作是否完成,如果没有完成则继续下一个socket。这种模型需要占用很多CPU资源来不断轮询。
1. IO多路复用(IO Multiplexing):select/poll/epoll等方法可以同时监控多个socket的IO事件,当某个socket就绪时再进行真正的IO操作。这种模型单个线程可以处理多个socket连接,系统不会大量占用CPU。
1. 信号驱动IO(Signal Driven IO): 通过SIGIO信号来通知程序进行IO操作,这种模型可以处理大量连接,但是编程比较复杂。
1. 异步IO(Asynchronous IO):通过异步回调函数来通知应用程序IO操作完成,这种模型编程比较复杂,需要操作系统支持。
**select和epoll都是IO多路复用的实现,主要区别有:**

- select最大同时支持1024个socket,epoll理论上没有限制。
- select需要遍历整个socket列表来获取就绪socket,epoll只需要获取就绪列表。
- select需要重复调用来获取就绪socket,epoll可以通过epoll_wait直接获取。
- epoll更加灵活,可以modal和level触发,select只能level触发。
所以epoll性能要远高于select,可以支持更多的并发连接。



模式触发(edge-triggered)和水平触发(level-triggered)是I/O多路复用机制中的两个重要概念:

1. 模式触发(edge-triggered):只要socket状态变化了,无论变化前后状态如何,都会上报一次。比如一个socket从未ready变为ready,会上报一次;但如果socket一直处于ready状态,不会重复上报。
1. 水平触发(level-triggered):只要socket满足就绪条件,就会不断上报。比如一个socket一直处于ready状态,会不停地上报就绪事件,直到它不再满足就绪条件为止。
epoll同时支持两种触发模式:

- epoll默认是水平触发,只要socket就绪就通知,这可能导致大量重复通知。
- 设置EPOLLET可以切换为边缘触发模式,只通知一次状态变化。
select仅支持水平触发模式,没有边缘触发。

所以epoll的边缘触发可以大量减少重复通知,减轻负载,这也是epoll性能出色的原因之一。正确使用边缘触发模式可以充分利用epoll的优势。


