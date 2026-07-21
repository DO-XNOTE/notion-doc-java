---
title: 2-13 Spring数据访问源码解析-2（1607）
---

# 2-13 Spring数据访问源码解析-2（1607）

[image](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/fce045e8-82bc-4047-bf0d-1d98dc2cb884/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466Q7C7AG7Q%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T232014Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDjx6%2FqRX95toM1%2BoOW7CrmBDBbYVT0109VX3yTecHFdAIgUb81eNpq%2FF8Gp%2Bl2ULMurMVrLYx9dUhN%2Bu7O6ZfnkL0qiAQIxv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDFLeSaTyI6rdRCzC4yrcA7x1yiRko7OR50x%2FSQ%2Bill6bb1uhz5FrEKQAXoOk%2FoHJl0uFzfkxFVoDLagW%2BbWhbPaQr%2FGiJlPL6ru5FSt3klbEUlj2QX7rLGEaNUwBR8EAJUIh5o1vPQ0EstdM4N9RmptaEcE%2FWVFacJt01nkfwBZDUi0iA%2BB6MX%2BzT6QTiWKiiYw%2BLWqijRaoDbPVXixRvpP0AYaG9E5C%2B7mw0YPKrqx2IAWTQPSVdb9NkzJGsRJxjuQg%2FiOll2Hzw2F8fqje7eATUnTcUubxIrjSqbm2KrU113O9tCu23trOxI2XJvR23f80r4DveAlEANhaEqkIMlHA0P7Vf1jdGBgz91TPD8K6ct59qRF89PDK2f4QT8mCcX09Yw453jCPQJQPJiycYldnrobCMeh58D4cZ%2FXTBvbIYO1I2F6m5li1w%2Fps%2FpsQdcFQO0jjsPP42Zmx7re0uOmJDK9WP3%2B6Qcy4%2BMGIsB8gfrMXgwYM5RRtVndvNj%2BN1RptvD9TxMOWLFgznz%2BvZC4MCuXOzfBjOhwfJoNFUy%2FP9nB%2ByWzQwjbzh5bXTRKPRLd5PgzGdVjEJujCg%2Bk4k%2BSUijzoGlVoujoQkjqP812nqTfLT5A9k1AJfBST5b%2BdDQAo9Gw55RqwAS%2FkMNW5%2F9IGOqUBK5ZkDbTb2Jno8EfBa8DoCjhlJIVV0huIKjZHuXSHbFq%2FGYDI8yG9sj3qPQUnkQ3wpLQHC1qa30B%2F4kKgDAJH1azFv4l9qDgy%2FDRFC74mm2AsYgPviCKG17Dngaa%2BEO8ZZCKwQFKqYJvC7oRM731FShzNtJo5eaxP76EWAAN%2Ff8KLaH6hqF0dHtJwHz4UpPv9rT4dk5xzlzraOkW2KTLsiVBPqxzR&X-Amz-Signature=eb4e26a2901c61bd598c66806eaabcb01f2f2619b7fcc9f2de1f020cdad9bece&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

我们看一下这个四五执行的过程，首先需要去选中当前我们要执行的这个对象，对于我们这里面也就是 Demo model d o，也就是这个对象，对于这个对象，因为我们对于这个对象是我们只是使用了一个类，我们并没有为这个 Demo 的 DU 提供一个接口。这种情况下它会基于 CD lip 给我们生成一个动态代理，其实它的实现类，也就是 CD lip 下面的 Dynamic Adviser interceptor，它会做什么事情？它会通过调用 perfect factor 里面去获取一下真正去处理的这些intercept。


找到以后，也就是这里面是我们真正处理的 transaction Intershamp，也就是刚才我们介绍的最重要的这个拦截器，它里面通过 invoke 为一次 transaction 操作去真正去做我们的事务，一些管理相关的内容。整个这个过程执行完成以后，并不是执行完成，应该在他执行的过程中去判断一下有没有相关的四五操作。通过我们四五管理的这里面它会构建出一个 transaction signalization 这样一个对象，它放到跟我们四五的一个容器里面，当我们的四五进行提交，或进行回滚，或进行完成这个四件的变迁的时候，去判断一下是否需要去接收这个四件，进行四件的处理。


我们这是四五生命之四五执行的一个流程，那我们来通过 debug 去执行一下关键代码的一些点，我们去观察一下，我们现在回到单元测试，那么在这里面我们选中一下我们这个 seal 方法，还是再跟大家去确认一下我们在 Demo model d o 的过程中，我们实现的这个自有方法。


在这里面特意为了跟大家去演示一下基于事务监听的一些区别，我们在整个四五方法里面，也就是说它会在四五之内，在四五里面去注意一个事情，就是说它会发布一个事件，这个发布事件的内容也就是 create event，我们的 event 对象也就是一个普通的model，也就是我们 save 一个 model 的时候会发布出一个事件出来。


对于这里面我们会对一个特定的 model 进行一个抛出异常，在这里面抛出这个异常，也就对应的我们的 runtime exception，它的一个子类，它会对四五进行回滚，也就是说我们普通的一个四五回滚的话，那么我们来想我们四五回滚的操作是在我们事件发布之后，如果说我们正常发布一个普通的事件，这个事件是可以被接收的。
如果说我们接收基于跟四五相关的一个eventation，那么这个事件它就不会接收。这里面我们看一下在这里面它一个死陷的过程，我们看这里面是一个 create event listener，也就是说这个 listener 它会监听我们 create event，在这里我们看到首先这是我们正常的使用我们的事件监听的一个机制，我们使用 eventlistener 就会监听到我们发布的这些事件，这是我们特意要强调的，是 transactional event listener，也就是说如果说我们想必须是事物提交以后的事件才是有效的，那我们应该用这种方式。


我们可以通过执行的过程去跟大家演示一下这个效果，那么我们现在去执行一下这 4 步操作，我们通过日志来去跟大家解释一下执行的效果。我们现在来看四字形过程，我们现在确认一点就是如果说我们的方法名称里面是 test 一的话，它就会抛一场，我们可以看一下在整个这个过程执行的过程中，我们可以看到 unquit in the time，这里面有 test 一，对于 test 一、 test 2、 test 3 它在执行的过程中，比如说我们看 test 二跟 test 二相关的是两个词件，一个是我们普通的一个 uncreate event，一个是 uncreate event transaction。我们看 test 3，它也是支持两个事件，也就是说在我们这个 listener 里面，正常情况下它都会把这两个事件都会监听到，也就是说这两个字都会正常执行。只有我们的 TEST 一。


TEST 一我们可以看到对于这个 test e 这一行内容，它只有我们的 on create event，也就是说它只有我们这个 event listener， on create event 它并没有这一行，也就是说因为 test 一代执行的过程中，它事务发生了回滚，发生了回滚，我们基于 transecond event listener 获取到的事件才是真正事物提交的一些事件。所以用这种方式去监听事件的话，会把一些回滚的相关操作也会监听到，所以说对我们的数据会有一些干扰。


我们可以看到在这个 transection event listener 里面，它可以配置一些信息，比如说它的一个阶段，也就是我们在什么阶段下去监听这个事件，也就是这里面默认是 after compete。当然我们可以自己根据我们的业务场景去定义我们的这些词件阶段。这里面比如说我们是有 before commit 和 off 的templates，你就完成 off 的robug，这几个都是可选的，这样我们去可以比较明确地区分出这个 transaction eventation 它的作用。


现在我们去回到这里面，我们通过单元测试的方式，我们去跟一下这个执行的过程。首先我们在这个 seal 方法里面在这里面去加个单元测试断点，我们现在开始执行，我们看第一步它会执行到哪里？执行到我们这里面是 transact management configure select，也就是在这里面它会去选择我们两个 register 这个配置，我们看它是执行到 process 里面，我们执行过去，在这里面获取到对应的import，它就会装载到我们的 Bing deep 内容器里面去进行一些初始化。那么我们跳过这个断点，在这里面我们可以看到它到哪里面，在这里面它就执行到 transact interact，也就是这是我们在执行我们的 AOP 拦截的过程。


那么我们首先看一下这里面获取的这个 target class 是什么？在这里面 target class 就是我们的 demo model d o，也就是说它就是我们当前要执行的这个 d o，这个 d o 去判断是如何执行。我们这里面跟进去，这是 invoke with transex，这里面是真正我们处理的过程。


接下来获取 transacent tribute，进一步获取 transegment manager，我们可以看一下 Trans manager 当前的对象实现是什么。这里面获取到TM，这个 TM 它就是 data source Trans manager，也就是我们普通的一个数据源的四五管理器。这步判断的内容是什么呢？这是reactive，也就是在 spring 5 以后，它提供的是基于 record 四五管理器，这步它不会执行到，我们可以先跳过这一步，它正常执行。


跳过这里面我们看获取到我们的 platform transect manager 去做的一个四强，这里面去包装获取到 join point 的一个标记，这里面会去在这里面去创建我们 transect info，我们可以根据你看一下它处理的内容是什么，在这里面它就去通过 get transaction 去开启我们的四五，把我们获取到我们的四五状态，也就是整个在这一过程就把我们的四五已经开启完成了。


执行，完成以后，下一步这里面去执行我们的相关的业务操作，我们看一下这步他做的什么事情，我们跟进去看一下它是还是process，我们接着跟进去继续在这里面我们自行跟进去，在这里面我们点击的话它就会到我们写的业务方法了，我们可以进来在这里面它第一步执行的是 find 2 操作，它这个 transection 它是一个 read only 的情况。我们继续，这样的话，我们指业务逻辑已经执行完成了。


业务逻辑执行完成以后，我们现在要做的事情就是对我们的四五进行一个提交，一个后处理的操作，这样的话我们整个四五就处理完成了，这是一些 process commit 的操作。我们现在这些内容我们可以跳过，这样的话我们整个过程就自行完成了，因为整个这个单元测试里面它涉及到多次的循环，那么我们就不在这里面把每一个过程的操作都通过断点去演示一遍了。


我们现在结束我们的单元特字，在这里面我们可以看到如果说我们是需要通过四五来执行的过程的话，这几个关键的方法也就是我们的 transaction intershaft，它里面处理的内容是比较重要的。另一方面就是我们如果说是需要监听会议，监听是当我们的事务提交以后的一些事件，那么我们需要注的事情是在我们 public event 的过程中，这是正常操作的。那么我们在监听的过程中，也就是我们的listener，我们在这里面是监听的过程中，我们需要添加的注解是 add transactor event listener，而不是 event listener 了，虽然它默认的是这里面是一个 of the compete。当然我们也可以根据自己的业务场景是去写，比如说我们当四五回滚以后去做一些什么补救措施也可以在这里面去完成，这是我们 spring 森明的四五执行流程相关的一些内容。


接下来我们来看一下基于 spring 的一些数据访问的拓展。首先我们来看一下是 HR 数据库控制台，还有也就是我们多路由于数据源数据监控相关的一些内容。下面来看一下 HR 数据和思路。一、数据源项目的一些演示。在这里面我们构建了一个 showcase HR 的这样一个模块儿。我们先看一下这个模块儿里面依赖了哪些内容。我们依赖了 HR 的 DATABASE 和 spring boot STARTER，g，d，b， c 和阿里巴巴，也就是 through 一的 spring boot STARTER，这里面会间接地依赖自主一的数据源。


下面就是正常的STARTER、 wap 和一些其他的超，这些不是很重要，接下来我们看一下，如果说我们需要开启 H2 控，我们先看一下 H2 控台，打开以后会是这样一个效果。我们有一个登录界面，这里面也可以选择语言，在这里面我们输入对应的 URL 和我们的用户名密码就可以点击进去，这样的话进去以后它就相当于是一个 Web 版的一个数据控制台，也就我们可以在这边去输入 SQL 去进行操作。对于德鲁因的话，它的操作我们可以在这里面看到，它可以看到一些我们数据库线上的一些信息，基于这些信息我们可以比如说 SQL 监控、防火墙、 Web 应用、 URL 监控相关的一些内容，基于它会对我们问题排查和定位就会方便很多，那么我们知道了 HR 和这个思路一的一些功能，那么看我们如何开启。


对于我们在使用 string 布的工程的话，我们开启是比较简单的，我们在这里面需要注的是，首先是 H2 cancel enable，也就是说我们的 H2 这个控制台的页面是 enable 为true，那么它默认值是false，所以说我们需要去手工去开启一下。


对于德鲁伊数据源的这些监控，我们需要做的事情是 data source，德鲁伊这里面我们需要指定一下 FILTER state，也就是说它的统计的这个 FILTER 的它的 enable 设置为true，同时我们可以打开 SL four 接这个 in filter 也设为true，它可以做的事情就是把我们这些执行 SQL 的一些操作，比如说我们的返回值和我们的参数都打印出来，这样也方便我们去调字和一些问题定位。我们确保这几个参数是设置没问题的话，那么我们就可以去启动我们的程序。


还有一点需要去注意的，在这里面我们为了让我们的因为这是内存数据库，让我们的数据有一些数据内容，那么所以这里面去指定Scammer，这里面是 class part init DB SQL 这里面是做什么事儿，也就是把我们这个 SQL 脚本作为一个初始化的信息，那么初始化进去，这样我们在登录数据库里面它就会有一些默认的数据源在这里面，我们回到看这么 HR application 这个模块，对于这个模块也比较简单。我们这里面是通过 spring boot application 去启动对应，这里面有我们的 main 方法，只是我在这个里面去写了一个 name 类，去为了把我们 demo model 去一个做一个展示，一个序列化这个内容，它的内容是跟我们 spring DDVC 里面这个 demo model 是完全是一模一样的。


我们现在去启动一下我们这个 HR application，在启动的过程中大家一定要注意一下，作为一个内存数据库，我们可以看到它是 its a pencil available 的，也就是可用了它的 URL 是这样一个UL，大家一定要记住。


还有一个需要大家记住的是下面这个 GDB seed，它的 UL 链接我们可以看到，对于我们平常的话，我们会指定一个数据库链接的一个固定的一个值，但是我们因为它是内存数据库，我们并没有对它做一个特殊的配置。那么这个 GDBC its a memory 后面它是一个UID，也就是每次我们启动随机生成的，所以说我们需要把这个字符串儿拷贝出来。


接下来我们去看一下我们的控制台的效果，在这里面我们去打开 HR cancel，那么这里面我们可以选择中文简体，这里面我们看选择 HR 数据库，我们选的是一个浅入式集成的数据库，同时它也支持 Server 模式，我们当前是浅入式的方式，这里面我们需要注的是 favor 跟我们已经默认填上了，我们现在需要把这个 URL 替换成我们刚才从控制台拷贝出的URL。接下来我们可以测试链接，现在我们可以看到是测试成功，用户名字SA，密码是空。


接下来我们来看一下这个点链接的效果，现在已经进来了，我们可以看到在这里面是我们这个数据库的一个控制台效果，这里面我们一看它的功能还是挺强的，我们可以选择是自动提交、自动刷新等等，这里面我们可以有一个自动提示的一个 SQL 的自动完成，比如说执行相关的一些内容。


我们可以看到这是我们的一个默认的SQL，那么我们双击它就去执行我们的操作，我们可以在这里面去执行我们的SQL，我们可以看到这里面是执行 SQL 的这些数据内容，这个就是我们可以去访问我们程序数据库的一个控制台，其实大家应该要知道它可以连接各种数据库，比如说我们MySQL、 Oracle 等等这些数据。


如果说我们在线上去集成这样一个控制谈话，我们就可以做到了对线上输出库的操作，所以说大家对这一点一定要有一个比较敏感的沉静，对于我们线上这些测试环境的一些内容，尽量不要发到线上，对线上的这些功能尽量不要打开，这样避免我们的数据库安全的问题。这是我们这个 H2 的一个控制台，来看一下自主一的这个控制台，自主一提供了一些我们数据监控的一些信息，比如这里面是数据操作里面防火墙相关的，我们可以去加一些白名单，黑名单去对于我们一些 super 套路的一些统计，这里面 Web 应用相关的内容我们就不介绍了，这个跟数据库关系不是很大，只是说这个 Server Lite filter 它可以做一些这方面的一些监控。


其实我们刚才看到如果说我们在执行过程中这个URL，如果说因为我们的日志量比较大，我们没有找到这个URL，同时我们可以通过这里面基于自主一的 data source，我们可以在这门数据源里面找到这个 URL 链接，我们可以看到这个链接就是这个内容，我们可以整个拷贝过去，这里面选中用户名是AC，它就可以去自行通过。所以说这也是我们在工作过程中使用的一些小技巧。


现在我们还回到我们的PPT，介绍完这些内容的话，跟 spring 数据库访问相关的内容我们就先介绍到这里，因为我们在做业务开发过程中，跟数据库交互的内容是非常重要的，对于 string 框架跟我们提供的这些 45 RGDP seed 包装也好，相对来说还是比较简洁的。对于我们来说，业务上我们来使用 my Betas，或者说我们使用 spring date， GPA 或 spring date 其他的一种方式，那么我会在后面的课程就会做一些详细的介绍。我们今天的课程就先到这里，同学们再见。

