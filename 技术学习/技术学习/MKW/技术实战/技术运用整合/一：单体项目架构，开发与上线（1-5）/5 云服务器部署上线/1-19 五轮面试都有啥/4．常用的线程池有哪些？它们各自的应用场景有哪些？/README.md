---
title: 4．常用的线程池有哪些？它们各自的应用场景有哪些？
---

# 4．常用的线程池有哪些？它们各自的应用场景有哪些？

[第36周 应用监控与调优-技巧与实战篇](/4d4e6bdcfee741879ed53861b4656ad7)

[2-1 线程池ThreadPoolExecutor详解](/0f4cf829a5754cddb04b92a19f59f77d)

[2-2 线程池BlockingQueue详解、选择与调优](/1326a31ea48640018bc04c747acf6acc)

[2-3 线程池ScheduledThreadPoolExecutor详解](/06c03845a44a4df6acc16fa2b0daf861)

[2-4 线程池ForkJoinPool详解](/bc959cc329e740d080182ebcbff01696)

[2-5 线程池Executors讲解](/ce004b15ecbe4364809876ffd51fdf6e)

[2-6 线程池调优实战](/c6397af80f784ea5a2fc1f0f99df6080)

[2-7 线程池总结](/7cab7396a47c4e2486bd8f66fc75a65b)






常用的线程池主要有以下几种:

1. FixedThreadPool: 固定大小的线程池,线程数目不会改变。适用于执行一些重复且固定数目的任务。
1. CachedThreadPool: 缓存线程池,线程数目不固定,可以根据任务量动态调整。适用于执行一些突发或大量的短期异步任务。
1. SingleThreadExecutor: 单线程池,只有一个线程处理任务,保证任务顺序执行。适用于需要保证顺序地执行各个任务的场景。
1. ScheduledThreadPool: 定时调度线程池,支持定时及周期性执行任务。适用于需要重复执行的定时任务。
1. ForkJoinPool: Fork/Join框架中的线程池,适用于可以进行任务拆分的 CPU 密集型计算。
主要的使用场景:

1. 处理多用户的请求,如Web服务器,使用FixedThreadPool或CachedThreadPool。
1. 需要定时执行的重复任务,如定时報告,使用ScheduledThreadPool。
1. 需要保证顺序地执行依赖关系的任务,如工作流,使用SingleThreadExecutor。
1. CPU密集型计算任务,使用ForkJoinPool提高运算效率。
1. 执行大量的短期异步任务,如页面请求,使用CachedThreadPool。

线程池的参数主要包括:

1. corePoolSize:核心线程数,线程池保持存在的最小线程数。
1. maximumPoolSize:最大线程数,线程池能创建的最大线程数。
1. keepAliveTime:空闲线程最大存活时间,空闲线程存活时间超过此参数会被终止。
1. unit:keepAliveTime 的时间单位。
1. workQueue:用于保存任务的阻塞队列。
1. threadFactory:线程工厂,用于自定义创建线程。
1. handler:拒绝策略,当线程数满了且阻塞队列满了时的饱和策略。
这些参数的作用是:

1. corePoolSize 和 maximumPoolSize 控制线程池的大小。
1. keepAliveTime 和 unit 控制空闲线程的存活时间。
1. workQueue 缓冲提交的任务。
1. threadFactory 自定义线程创建。
1. handler 定义线程池饱和时的拒绝策略。
通过合理配置这些参数,可以优化线程池的性能,满足不同应用场景的需求。


为什么要使用工厂模式创建线程池？

使用工厂模式创建线程池有以下几个好处:

1. 避免线程池的参数直接暴露给调用者,调用者只需要知道工厂类。
1. 封装线程池的创建细节,调用者不需要关心线程池的实现机制。
1. 可以根据不同的业务场景,返回不同配置参数的线程池。
1. 统一管理线程池的创建,避免多个线程池实例的重复创建和资源浪费。
1. 线程池本身就使用了工厂模式,线程工厂 threadFactory 可以自定义线程创建逻辑。
1. 通过传递 threadFactory 给线程池构造函数,可以方便地自定义线程创建行为。
1. 工厂类可以自由控制线程池何时创建,以及在应用关闭时可以优雅关闭线程池。
总之,工厂模式提高了线程池创建的灵活性,将线程池本身复杂的创建和生命周期管理封装起来,使用方便,符合开闭原则,这是使用工厂模式的主要优点。



自定义线程池

这里是一个使用工厂模式自定义线程池的示例:

```java
public class CustomThreadPoolFactory {

    public ExecutorService createCustomThreadPool(int corePoolSize, int maxPoolSize, long keepAliveTime, TimeUnit unit) {
        return new ThreadPoolExecutor(
            corePoolSize,
            maxPoolSize,
            keepAliveTime,
            unit,
            new LinkedBlockingQueue<>(),
            new CustomThreadFactory()
        );
    }
}

class CustomThreadFactory implements ThreadFactory {

    private int counter = 0;

    @Override
    public Thread newThread(Runnable r) {
        return new Thread(r, "CustomThreadFactory-" + counter++);
    }

}

```

使用方式:

```java
CustomThreadPoolFactory factory = new CustomThreadPoolFactory();
ExecutorService pool = factory.createCustomThreadPool(5, 10, 60, TimeUnit.SECONDS);

```

在这个示例中,我们实现了一个自定义的线程工厂CustomThreadFactory,它会给每个新建线程赋予一个唯一的线程名。

然后在CustomThreadPoolFactory中利用这个线程工厂来创建线程池。这样就可以获得一个拥有自定义线程名的定制化线程池。

通过工厂类来创建线程池,客户端代码只需要交给工厂类,而不需要关心线程池的创建细节。

