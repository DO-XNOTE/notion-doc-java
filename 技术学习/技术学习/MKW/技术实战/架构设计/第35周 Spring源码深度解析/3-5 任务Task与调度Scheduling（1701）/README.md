---
title: 3-5 任务Task与调度Scheduling（1701）
---

# 3-5 任务Task与调度Scheduling（1701）

[image](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/a354a6e6-6eda-4394-a816-b6c558c25f4a/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664E5ZHAF2%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T232022Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIB82sgmKk%2F0Lijllg9CPuon3GZVnL5S4j5iTW8PAsf%2BiAiARIKWGcE9rRn8gJeHbHzUMWHYVKBwwKsMYQ7EGnYHxqSqIBAjG%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIM2DzVAVUdezsYR%2Bd8KtwDs5Dj9jMYiI1jHtRkqnwzbDu9eEHek5bzbtPKbbGonQwC1iXlX%2BcBfJmAxFwOIevJ7wEdyU%2Fb40LXsXJI6RvXuGfhzw4x3N4%2FjAWc%2FDROeNmi1Qst4rq7RMWGLXI6KdKqiMVDkw5csHRpLkW31eaojjwAk%2F1FpN5Zb7qRfsDPRnpN63GHfLkPe0X5go8QCifJiY4mLQW3cAeCny7Z9dLFfHCSZmF7pVXOwAC798%2FfGt8ktq%2BBuIIyoed7%2BNqM9GDrYEQ815XA4JeYW3I6c%2Bb%2Fl7j8LAoNOkPfHwINYOb01D0LVCsvM%2FwRJrO9rl3YFuU9n1JNdq7fbMjoKZLkDbkaUkpNeSND0lwgoHJSAY6lZ3iH8YecjpBI12tRSYdU9HuPPkZn8pkCiYx7hhWtm3O6mKQujwoKDymPPMqLFzOVqU5uX9y24CjdAE1bQz9rOPOjWg%2BhxnS6GyepR5QwppB351aSB0BX21CX68cdw3vqv70uyuJS5v9VaEE2Bdx1HPb7W2WVkfOxaAgZYyrlsS6uM5s5AmMKHZVXCLeg1A%2B7j328eu3HaP5Uzx2lH1i%2FutNr1qKGkcMhj8IHDHgvPpPzpv2IOCF3x3iUXg%2FlM6irwLJEi%2Fh94jmZI%2Bt7YrUw77f%2F0gY6pgFBZZXG8qkvxKtcGqliZRiQA6SiwuVAK%2BBw3M1o5KhQGK3ml1Uai6YVIIxL0gJhy1bMlBFIkar0uLBfMDqlw47Y7IQetiRPFTfgqkIP1iXLuO5nQrighTPINX1lddEylCwbFSrxsCtq7MxfIIlmdsw2I3OB706b%2Ff9KbDHG3EFEMGl%2Bv4yiDHs8RXdsiycoi%2BL85j6UXu8X1gZXs%2FV%2BLpKu9nPJfTM8&X-Amz-Signature=1bf47299753c3e3d03aa4f6ba89d978c3ae390f9993bded77f5adee288b7ec41&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

同学们大家好，这章节我们来介绍异步任务与调度。异步任务依赖线程词构建多线程环境。任务调度主要是解决周期性定时执行的一些相关操作。 spring 框架提供了 task exector 和 task Gaddler 解决异步执行和任务调度，并提供了相关的类实现给开发者使用。同时提供了基于注解或 x mal 的方式方便使用。这里面我们首先介绍一下 task exutor 的工作原理，即 task scheduler 的工作原理。介绍完这两个接口以及它的一些实现，我们来去介绍一下整个这两个接口它的一些使用的方式。


好，首先我们来看一下 task exator 的工作原理，从这里面我们可以看到 task user 它里面有几个默认的实现，首先这是一个 single 的 task exutor，也就是说这种是它是非异步的，它是一个同步的执行方式，这种情况下使用的是非常少的，它只是为了保持我们接口的一致性。这里面有一个 simple SYNC task editor 以及 concurrent task editor。其实这里面我们重要说的是也就是 third pool task user，因为它的实现是跟 JDK 对应的 u two concurtain 下面的 third pool excluder 的实现原理是很类似的，那么这里面我们先看一下 task equator 它的这个接口的一些构造方式。


我们可以看到在这里面 task exter 这个类它是在对应的，也就是这个接口它的实现是在对应的我们的 spring corn 里面，也就是可以看到这个接口，它是基础性还是比较强的，在这个接口里面它是继承了executor，也就是继承了 JDK 里面的，我们这里面可以看到是加 u to concurrent 里面的executor，也是默认的一个extriter。
所以说其实 task extrator 它相比 JDK 来说，其实可以理解为它是一致的一个，也就是 Java user concurrent extrator，那么它的方法并没有去扩展更多的方法，也是执行对应 renope 的方法，那么对于 task return，在这里面 spring 提供的默认实现我们看。


首先看到这是一个同步的一个执行操作，在这里面的执行操作只是使用了 task 的润方法，整个这个过程是一个同步操作，它并没涉及到线程池，那么我们看下面这些内容，下面这里面是一些异步的一些操作的内容。在这里面我们可以看到，首先是最重要的，也就是 third pull task Creator，它的实现过程是依赖到我们的一个线程池，这里面就是 set poor executive，也就是 JDK 默认的线程池。在它实现的过程中我们可以看到它在构建的过程也需要配置相关的一些内容。这里面比如说我们看到核心线程池和我们的最大线程池数量，以及我们的队列的容量等等这样一些内容。


其实整个我们的 third pull task exter，其实也就是对 third pull exter 做了一个包装。好，接下来我们来看一下 task schedule，对于这个 task schedule 它其实也有几个默认实现，这里面还是我们重点去看一下 set pool 的 task schedule，对于我们在执行这个过程的时候，我们一般会需要一个 trigger 对象，这个 trigger 对象表明了一下我们这个定时任务触发的方式，我们可以基于 Coin 的表达式，也可以基于一个定时的一个定词间隔取自相好。


我们进代码看一下 task schedule，跟我们这个 task Skuter 不同的是，这个 task schedule 它是在我们可以看一下，我们看到 task schedule，它并没有在 spring core 里面，它是在 spring context 里面，在 spring context 下面有一个schedule，你这样的一个包结构下面有它 schedule 在这里面我们可以看到它里面提供的一些方法，这里面主要是 schedule 的一些操作，这里面提供一个可以 runnable 方法一个操作。我们冲这里面可以看到 schedule 它提供的这些方法可以分为三类。


第一类我们可以理解为 schedule rely，它指定的一些时间，也就是说我们在指定一个时间去执行这个rely，它的一个读线程的一个实现。那另外也就是我们看 schedule off 的 fixed rate，也就是说它在执行的过程中是指定我们什么时间开始的话，对应的一个延长周期，这是也就是说我们指定，也就是说对于这个方法来说，它在指定的时间这个时间点开始执行，并且每隔多久这个浪子每隔多久开始就是重复执行一次？下面这个方法是 schedule with fixed delay，也就是说我们在这两个参数，它的意思是首先我们在指定延迟多久的一个时间段，我们去执行某一个 relabel 的实现，那么同时我们这个 long 也就是指定了一个时间抽屉会去进行一个重复执行。


其实这里面看我们可以理解为 schedule 提供了三种我们对于指指定时间的一个执行的方式。我们看一下在这里面对应的它的一个 trigger 对象，这个 trigger 对象可以包含我们的 coin 表达式，或者一个正常的一个时间周期的一个trigger。我们可以看到在这里面它是支持一个 trigger 对象，那么 trigger 对象我们可以看一下它的一些时间里面，我们可以看到这是一个 common 表达式，我们知道它通过几个通配符去定义我们对于每天、每月、每周的一个spend，一个实际情况，这个的具体这个表达式怎么去写，大家可以很容易地从网上去查询出来。


接下来我们来看一下跟这些 task 相关的这些注解的一些工作情况。首先这里面我们几个注解是，首先是 enable a sync，也就是开启我们的异步功能操作，如果开启 enable async 以后，我们可以通过 async 这个注解去对我们的方法去标明一下这个方法，它是通过异步的方式去执行的。另外一个就是我们开启 enable scaling，也就是开启我们的定时任务执行，那么说这个注解打开以后，我们就可以使用 at schedule 的这样一个注解去标明一下，我们这个方法是定时任务执行的方式是怎样，我们可以自行一个 com 表达式，也可以制定一个延迟的时间周期，就是如何去定期的去执行。


那么我们可以看一下这几个注解对应的实现，因为我们看到这些 enable 相关的注解的话，大家应该是现在已经比较很清楚了，我们可以知道这个注解它肯定是加入某个一个select，通过 select 解析去定义一些配置，比如这里面是 add a sync 的话，它肯定是通过一个异步的操作进行。对于这个方法进行代理，那么通过 AOP 进行代理，以及在执行的过程中进行 AOP 的包装，那么把它完成一个异步处理的一个过程。


好，我们现在通过源码来去了解一下这个过程。首先在这里面我们可以打开看一下这个 enable async 这个方法，这个注解，对于这个注解我们可以看到它是通过 import async configuration selector，它去装载我们相关的一些处理情况，那么我们跟进来看一下，在这里我们可以看到它是对应两种方式，一种是基于普通的代理，一种是通过 s five 的接。那么我们可以在这里面是通过普通代理的方式去看一下它处理的方式。在这里面我们应该可以看到它在这里面配置的内容是配置了一个 being post process，也就是做了一个后处理，这个后处理的工作方式是什么呢？我们可以从这里面看一下。


首先定义出这个 async 的 notation being post price，对于它来说这里面去配置的一些内容，配置的一个是accurator，就是一个处理器以及对应的 acceptance handler。这里面我们可以看到它是继承了父类里面的内容，也就是在这个处理的过程中，它提供一个异步执行的一个多线程的线程环境。同时如果说抛异常以后如何去处理这个异常的内容？同时这里面去判断了一下 enable async 的一个条件，在这里面是获取对应的一些注解。


我们接着看这里面有一个获取一个 customer async noticing 的一个操作，这个操作它的意思是什么呢？它是指其实我们的异步操作默认是 async 这样一个注解，同时也可以自己支持扩展我们自己的一些支持的一些注解的情况。那么如果说有存在的话，我们可以把它也放到我们这里面。


async noticing type，也就是我们指定的一些 end type，那么这个 Tab 在什么地方使用？我们可以从这里面看一下这个 a single notify being post process，它做的事情。在这里面比较重要的一点就是我们看一下它 AOP 处理的这个Advisor。


其次在构建这个 Advisor 时的时候，它构建的是一个 async notation Advisor，我们可以看到如果说这里面也是判断，如果 async notation type 不为空的话，把这个 notice on tap 的存放到这Advisor，我们看一下 Advisor 实现的内容，在这个 Advisor 里面它注的事情是比较简单的，我们可以看到这里面首先去构建这个 async notation type，同时它默认的把 async 这个 class 添加进去，同时去判断一下这个加 XEJB 下面的 async size，也就是这个异步超出的这个类是否存在。如果存在的话同时把它也放进去，这是 E J B 3. 1 的一个接口的注解，也就是说我们默认的话同时支持 async 注解和这个 async nice 这样一个注解。同时如果说我们这里面对于其他的 async type 如果不为空的话，也可以把它放进来，这样的话就构建我们判断看的时候是基于这个注解的方式，这样我们看到这个 enable think 它注解的一些处理方式。


那我们接下来看一下这个定词任务以内部 scheduling 它的处理的逻辑是怎样的，我们还是基于这个注解呢？作为我们程序的入口，我们可以找到这里面，对于这个注解它也是通过 import 的方式引入了 scheduling configuration 这样一个配子类，在这个配子类里面它是我们可以看这里面定义的是非常简单，这里面只是基于一个 schedule a notation being post a process，也是基于一个 being 后处理的方式。但是在这里面它的实现就比较复杂了。


在这里面的首先它会定义一个 schedule task register，也就是说在这里面我们对于所有定时任务的一些方法，我们先定义一个注册中心，我们会扫描所有用到了 schedule 这个注解的这些方法，都会把它放到这个主持中心，同时跟他定义一个类似于注册表，一个注册列表根据时间消耗顺序去进行执行。


在这里面我们可以看到对于这个 schedule notice and being post，它实现的接口非常多，可以看到这里面的我们比较重要的是这里面跟 schedule 相关的是 schedule task HOLDER，也就是说它会去处理对应的这些 task 的一些列表。


我们看一下最终相跟我们这里面紧密相关的一个操作，我们可以看到在后面，好，我们在这里面找到这里面它是 post process of the installation，也就是我们这个后处理的执行操作。在这里面我们可以看到它其实是去查找跟嗯， scheduled 和这个 schedules 这两个注解相关的内容，找到这两个注解的内容以后去进行一些处理，同时把这两个注解对应扫描的方法，把它注册到我们这个关于任务的一个注册表里面，这样的话整个 schedule 它的一些注解的解析过程也就完成了。


这里面要注意的话，这里面它并没有使用到代理 AOP 的方式去处理这个 schedule 注解，它主要是把这个注解找到以后，把它注册到一个注册表里面去，直接执行对应的方法就可以了。好，这是我们关于 task 注解相关的内容，这里面主要重要的也就是这 4 个注解，那么接下来我们看一下这个 task if filter，一个 task scale dealer 的它一些使用实践。好，我们还是到我们的 split scale 这个工程。而在这里面我们先看一下这个跟任务相关的代言测试，我们构建这个单元测试的时候是依赖 task skill，我们点进来看一下，在这里面我们定义了一个我们的线程池的执行器，我们可以看到这里面我们默认使用的是设置 pool task issue 的，在这里面我们对于这个线程池构建的过程中，我们设置几个关键的参数，这里面比如说核心线程数，我们的最大线程数以及我们的队列大小。


在设置这个执行线程池的过程中，我们要建议大家去对于这个 search name，也就是我们的线程池的名称前缀去做一个设置，这样我们可以通过这个线程名称后缀，在我们以后在定位问题的时候，看到这个线上词汇非常容易定位，这样的话可以避免我们去再去排查一些多线程的问题的时候，不容易定位到代码的位置。


同时建议大家去设置一下我们的rejects， reject extra handler，也就是说当我们的线程池和我们队列都满以后，那么如果说我们的线程是无法接受更多的请求，那么应该做什么处理？在这里面对于它默认的处理的话，也就是相当于是具体策略就是抛出一个异常，那么中断掉，那么在这里面我们可以通过我们自定义的一些实践，可以对这个处理的方式添加一些日志或一些监控相关的一些信息，这是我们这个定义的 task extrator，那么我们可以看到在这里面我们开启了我们的异步和我们的调度这两个注解，通过这两个注解就能开启我们的功能。


那么我们还回到我们的测试类，在这里面我们可以看到我们这里面进行 test Creator 的时候，这里面我们定义了一个异步操作，这个异步操作也就是 create user，我们对它进行了一些改造，对于这个 create user，我们加上了这个异步超出的这个注解，那么我们在这里面去执行的时候，我们应该能看到它可能执行的顺序，它不再是 a starter 和执行方法和end。我们可能会先输入starter，再输入end，最终我们可以看到它执行 create user 的执行的一个过程。这里面我们为了避免干扰，我们可以先把这个定时任务的这个单元测试，把它它的执行句把它给暂停，那么在这里面我们可以执行一下，看它的效果。


好，我们可以从这里面这些比较简短的几行日志里面去看到我们内容。首先它打印出了 star 的操作，从此 star 执行完成以后，它就是start，就直接是end，并没有等我们的 create user 去执行。那么在这里面我们可以看到 create user，这是 create user 执行的日志，在执行 create user 的时候，它这里面的线程已经发生变化了，这里面是 task skill e。我们还应该记得我们在这里面去定义这个线程池的时候，我们跟我们的线程池加了一个前缀，这个前缀就是 task skill。其实我们这个线程是在构建线程的时候，它去根据我们的数字去增加，达到一定的一些数量，这样可以看到我们这个线程池执行的过程，就是能通过我们的 async 这个注解完成了一个异步化的操作。
那么接下来我们来看一下定时任务的操作，在这里面我们是已经开启了定时任务的注解，那么开启完成以后，我们在这里面是通过 schedule 的这个注解去标明一下我们对于这个方法需要让它去进行一个循环的执行，那么循环执行的操作就是固定的言辞，比如说每 100 毫秒去执行一次，那么我们现在来执行一下，看一下它执行的效果。


大家注意一下，在这里面我们特意让线程睡眠 500 毫秒，也就是说为了我们在这个定时任务，因为它是不一样的线程，如果说我们当前线程如果中断的话，那么整个程序就已经结束了，所以我们让它 sleep 500 毫秒，等着这里面执行的过程我们可以启动一下，看一下效果。


我们看一下等它启动完成以后，它跟刚才我们的正常的义务执行是没有关系的。我们这里面是 sort end 以及我们的 create user 执行完成以后，这里面开始执行我们的 task schedule，也就是我们定时任务的执行。这里面我们可以看到我们每 100 毫秒执行一次，这里面留了 500 毫秒的过程，那么我们在这里面可以看到它执行了五次，这样的话这个定时任务的执行效果也给大家以展示了。我们回到PPT，这样的话，我们关于这个异步的多线程的执行效果和我们定时任务的执行，就跟大家先介绍到这里，同学们，我们下一章节再见。

