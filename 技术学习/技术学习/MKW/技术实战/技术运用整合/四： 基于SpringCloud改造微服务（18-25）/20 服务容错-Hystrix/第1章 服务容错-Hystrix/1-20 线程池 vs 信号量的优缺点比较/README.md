---
title: 1-20 线程池 vs 信号量的优缺点比较
---

# 1-20 线程池 vs 信号量的优缺点比较

[image](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/a2305a61-0e5d-4d87-8f1e-0e99db1bb48e/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YNPDM6WY%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T225648Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDoYh%2Flg6E4XajN1b13EfXcMxWNbqQXe9i%2BvH71GePW6AIgKHvgePrPk5Aw5a6CMlDJEQRioJscjWgxFa%2B7uId7%2BU8qiAQIxv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDNpltXqIqYlDj4eVJyrcA9GIZ4HwCk7bdm4wKlEbnXM33ZyIMwRuxGeOjXeQh%2FSLGzDlqRjxcCXZ04VHTs07OPE%2B3GOfD%2FsLXd7L%2BZ7t7YNjXX2zt%2FY9attFsxA5zBFT6rmUpukRb1Y1vGJNzHDskygdwu56iQdyPjsq%2BkcIbtX4HdF2cEcOjpEp6U6HCShd98nnUnw4OASFQwzDv%2BZT%2BxrGidzNpoHXlRTk078f%2Bm7kQRJhOSTHG6AgNO2VdlZqbu9BXTiEPXBoEOAUIjiuFsGFoPyviyJEjR7LcdinqXuaBrbT6P%2FV1L6nkJVubOm2Yp%2BbGscoz4IlSJBhJ9qr67SEsT9LvNwWUAUw7qkcspiiciV1o6FdODBVWFDQ%2F%2FzKdTEP3K5Cz2tyffSjvmdmYF2HOCuFsn8CdO7Z0nAPoh6vhMfprwgxa5J5k1RQnd2Hb0xfcisRPKnbJsYwTea%2BWWSezjteJAiOlLXk68srybtQZCOpB9POQU0wKFgWcE7pby1L8DmZHSe9OotUjO4igWQlFaiuY%2FwoZs%2BrDzW5MiNO9tlGSp0CcRX7QRYh6jsk53yu5Nx9MwW4D5%2BETcnDYZ%2BEtIIj%2BgUmV3n88PbWhyO5pFTVcTDVpV6rLa%2Bjh8kca8T4Ozyipu43QzaCMM%2B3%2F9IGOqUBIVbhMKHLyVhO8tytTLdKQ4RoO0LAF4vgx3C2RGmePB5g0AZIw3bw7Dy0VgxoP%2FMB7C2G%2FENcPKua%2BUnq7MOWvUnz8Dx90njBL2HEmuiOygaZh8AgIfWFax8rBi18SemulmJ46ZR1u4Shm8IgCOGfrlkFOIWD0hq8D8du8RVxkmnaA17AlLmGrGseohggyOXd1QXEZ2rm9oCwEeYOy8mgozH0%2BRpM&X-Amz-Signature=808c537dee832cd3de32ae57379f7c56239d04784b9aa79724454a65c9b25ec3&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

[image](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/076ed827-9536-430e-90cb-76e92d88f108/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YNPDM6WY%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T225648Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDoYh%2Flg6E4XajN1b13EfXcMxWNbqQXe9i%2BvH71GePW6AIgKHvgePrPk5Aw5a6CMlDJEQRioJscjWgxFa%2B7uId7%2BU8qiAQIxv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDNpltXqIqYlDj4eVJyrcA9GIZ4HwCk7bdm4wKlEbnXM33ZyIMwRuxGeOjXeQh%2FSLGzDlqRjxcCXZ04VHTs07OPE%2B3GOfD%2FsLXd7L%2BZ7t7YNjXX2zt%2FY9attFsxA5zBFT6rmUpukRb1Y1vGJNzHDskygdwu56iQdyPjsq%2BkcIbtX4HdF2cEcOjpEp6U6HCShd98nnUnw4OASFQwzDv%2BZT%2BxrGidzNpoHXlRTk078f%2Bm7kQRJhOSTHG6AgNO2VdlZqbu9BXTiEPXBoEOAUIjiuFsGFoPyviyJEjR7LcdinqXuaBrbT6P%2FV1L6nkJVubOm2Yp%2BbGscoz4IlSJBhJ9qr67SEsT9LvNwWUAUw7qkcspiiciV1o6FdODBVWFDQ%2F%2FzKdTEP3K5Cz2tyffSjvmdmYF2HOCuFsn8CdO7Z0nAPoh6vhMfprwgxa5J5k1RQnd2Hb0xfcisRPKnbJsYwTea%2BWWSezjteJAiOlLXk68srybtQZCOpB9POQU0wKFgWcE7pby1L8DmZHSe9OotUjO4igWQlFaiuY%2FwoZs%2BrDzW5MiNO9tlGSp0CcRX7QRYh6jsk53yu5Nx9MwW4D5%2BETcnDYZ%2BEtIIj%2BgUmV3n88PbWhyO5pFTVcTDVpV6rLa%2Bjh8kca8T4Ozyipu43QzaCMM%2B3%2F9IGOqUBIVbhMKHLyVhO8tytTLdKQ4RoO0LAF4vgx3C2RGmePB5g0AZIw3bw7Dy0VgxoP%2FMB7C2G%2FENcPKua%2BUnq7MOWvUnz8Dx90njBL2HEmuiOygaZh8AgIfWFax8rBi18SemulmJ46ZR1u4Shm8IgCOGfrlkFOIWD0hq8D8du8RVxkmnaA17AlLmGrGseohggyOXd1QXEZ2rm9oCwEeYOy8mgozH0%2BRpM&X-Amz-Signature=c480201d8e3e835c87ca3201c96f55ce0741cc6dae8cc8185eb2da5602e7597c&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

1-20 **   线程池    vs    信号量的优缺点比较**
前面我们学习了  Hystrix  中的线程隔离，通常我们都采用基于线程池的实现方式，这也是最容易理解的方案。Hystrix  还提供了另一种底层实现，那就是信号量隔离。小时候我们就知道“红灯停，绿灯行”，跟着交通信号的指示过马路。信号量也是这么一种放行、禁行的开关作用。它和线程池技术一样，控制了服务可以被同时访问的并发数量，乍一看好像两种技术并没有多大区别，我们接下来比较一下它们在应用场景上的不同之处。

大家来找茬
**线程隔离原理**
线程池技术：它使用  Hystrix 自己内建的线程池去执行方法调用，而不是使用Tomcat 的容器线程
信号量技术：它直接使用 Tomcat 的容器线程去执行方法，不会另外创建新的线程，信号量只充当开关和计数器的作用。获取到信号量的线程就可以执行方法，没获取到的就转到 fallback
**从性能角度看**
线程池技术：涉及到线程的创建、销毁和任务调度，而且 CPU 在执行多线程任务的时候会在不同线程之间做切换，我们知道在操作系统层面 CPU 的线程切换是一个相对耗时的操作，因此从资源利用率和效率的角度来看，线程池技术会比
信号量慢
信号量技术：由于直接使用 Tomcat 容器线程去访问方法，信号量只是充当一个计数器的作用，没有额外的系统资源消费，所以在性能方面具有明显的优势
超时判定
线程池技术：相当于多了一层保护机制（Hystrix  自建线程），因此可以直接对“执行阶段”的超时进行判定
信号量技术：只能等待诸如网络请求超时等“被动超时”的情况
**使用场景**

我这里引用  Hystrix  的官方文档，里面特地讲到了信号量的使用场景：
Generally   the   only   time   you   should   use   semaphore   isolation   for HystrixCommands  is  when  the  call  is  so  high  volume  (hundreds  per  second,  per instance)   that   the   overhead   of   separate   threads   is   too   high;   this   typically   only applies   to   non-network   calls
当请求量非常密集，导致线程隔离的开销比较高的时候，建议使用信号量的方式降低负荷，这种情况通常用来应对非网络请求（不需要调用外部服务）。根据官方建议，信号量适用在超高并发的非外部接口调用上（还是中文言简意赅），注意“the
only time”，意思是官方只建议在上述场景中应用信号量技术，在其他场景上尽量使用线程池做线程隔离。
除此之外，线程池技术要特别注意 ThreadLocal 的数据传递作用，由于前后调用不在同一个线程内，也不在父子线程内，所以如果你在业务层面声明了 ThreadLocal 变量，将无法获取正确的值。


小结
这一节我们了解了线程隔离底层的信号量和线程池技术，接下来，带大家玩一个支线剧情，
通过  Turbine  监控  Hystrix  服务健康度。

[image](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/cca22b06-de9b-4c75-8d52-efcb18ecdc9e/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YNPDM6WY%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T225648Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDoYh%2Flg6E4XajN1b13EfXcMxWNbqQXe9i%2BvH71GePW6AIgKHvgePrPk5Aw5a6CMlDJEQRioJscjWgxFa%2B7uId7%2BU8qiAQIxv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDNpltXqIqYlDj4eVJyrcA9GIZ4HwCk7bdm4wKlEbnXM33ZyIMwRuxGeOjXeQh%2FSLGzDlqRjxcCXZ04VHTs07OPE%2B3GOfD%2FsLXd7L%2BZ7t7YNjXX2zt%2FY9attFsxA5zBFT6rmUpukRb1Y1vGJNzHDskygdwu56iQdyPjsq%2BkcIbtX4HdF2cEcOjpEp6U6HCShd98nnUnw4OASFQwzDv%2BZT%2BxrGidzNpoHXlRTk078f%2Bm7kQRJhOSTHG6AgNO2VdlZqbu9BXTiEPXBoEOAUIjiuFsGFoPyviyJEjR7LcdinqXuaBrbT6P%2FV1L6nkJVubOm2Yp%2BbGscoz4IlSJBhJ9qr67SEsT9LvNwWUAUw7qkcspiiciV1o6FdODBVWFDQ%2F%2FzKdTEP3K5Cz2tyffSjvmdmYF2HOCuFsn8CdO7Z0nAPoh6vhMfprwgxa5J5k1RQnd2Hb0xfcisRPKnbJsYwTea%2BWWSezjteJAiOlLXk68srybtQZCOpB9POQU0wKFgWcE7pby1L8DmZHSe9OotUjO4igWQlFaiuY%2FwoZs%2BrDzW5MiNO9tlGSp0CcRX7QRYh6jsk53yu5Nx9MwW4D5%2BETcnDYZ%2BEtIIj%2BgUmV3n88PbWhyO5pFTVcTDVpV6rLa%2Bjh8kca8T4Ozyipu43QzaCMM%2B3%2F9IGOqUBIVbhMKHLyVhO8tytTLdKQ4RoO0LAF4vgx3C2RGmePB5g0AZIw3bw7Dy0VgxoP%2FMB7C2G%2FENcPKua%2BUnq7MOWvUnz8Dx90njBL2HEmuiOygaZh8AgIfWFax8rBi18SemulmJ46ZR1u4Shm8IgCOGfrlkFOIWD0hq8D8du8RVxkmnaA17AlLmGrGseohggyOXd1QXEZ2rm9oCwEeYOy8mgozH0%2BRpM&X-Amz-Signature=a398fb8da2c3116bb1e29ac25291f99e6ea959397e641bf58c2e9de99eab67c7&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)





