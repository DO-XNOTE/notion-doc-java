---
title: 1-2 Java中单体应用锁的局限性&分布式锁
---

# 1-2 Java中单体应用锁的局限性&分布式锁

[image](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/26bfaaac-70e1-4b5a-8e97-ccec2638a9f5/SCR-20240807-ipcb.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QPVJWHCH%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T225337Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCl14z%2BQhvrSTbRJjwKjQO%2BkdVs2jDoj1OPOvNo2V1YdAIhAPoy27ZEsdR5Nz3erwq0L2LKpLkKNRm3Hfngl1%2FvvYqGKogECMb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgwYognO%2Fi7e2snVWJkq3AN%2FBkm%2BXP%2F7zREovTa1o0FLss0KbIYDl59gueOcEH0AeWqulUVaDqgt6lf9QVJXLpN8TLf%2B5TA10iUJ056uFFEIY6bFYadstDqsD9YyzHN1234kjD6L2KTTaGupwp6mOhInVk9S7YNDElwfQLlWWTr3kLc0CJsV4o8yXNK09iL9qP85QIKB60yufTPFdbE0KIEVtKUmthBCG8EpXKxkWmTvATiRB%2BP29rZeuEswPk6vSPBC6TDZIMdI85p7jlLwzeFmdJzC0hj4ZN4rmMu%2FKEI7e6Y4aE0fvlejPO1q%2Bw%2BBv%2BD5tI8UDMY7XWFg47ltiOemWuhWvyvrTLqwxLAeNFgJUVofCsLi3YyLDIEZJ%2Br%2FYV6ym4J7z%2BIcK29Qx6sOZXIpbqVGC%2BHVE6EqvQrkBBDf6x9uquYnoTE5VUTfv2SF%2B77ZPlcI4eHrFnk11XaZWS3vQP8wFU3kyrZAv2VLEQpqKMGd5Y%2FG29k%2BXIvHG481BImCxoD%2FlBIySzjh%2FEGgmNTPpBfmdLvODKw%2B9Tk9FlAwFf%2B7zhn3Tcm4AgxKCW8MdqAhYIpt9BZi0Y9boEDSQk%2FZ%2FCP%2B1WqzLDIyqgodRjvxqgk%2Blq3LQDkTRVaOkpvURymT%2BhubKPw9dQE3YjCQuP%2FSBjqkAdLry3VfrUmOuvEAeFGuZ2pmlfBhZ4bf4QpRbohKs5caz91llTDJa2jgq27mgCAKqU4VFyXt4NFUtvPWCmZYXszfyBv2R88lVLSRcA19GeKO6VYplj9sx2JS5Uu%2BDOkT1%2Fj9Equ4jyyqgi%2FXXmEft8XLWcSeGSG%2Bg%2F8m3fJMsZ6oYOHh7Abp9qtXYTVe2IRiQPRtVyiONvnhWwcrox2v%2F71sxd43&X-Amz-Signature=803c5d491dc2c4e78b5f537b41f92bed9626235b4dc209f2ec8c26e93cedde09&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

<1—3 Java中单体应用锁的局限.
1—3Java中单体应用锁的局限性&分布式锁前言
通过前几节图文和视频的学习，我相信大家对JAVA中的锁有了深刻的理解，并且可以在项目中熟练的使用锁来解决一些问题。前面内容中讲到的锁都是有JDK官方提供的锁的解决方案，也就是说这些锁只能在一个JVM进程内有效，我们把这种锁叫做单体应用锁。但是，在互联网高速发展的今天，单体应用锁能够满足我们的需求吗？
互联网系统架构的演进
在互联网系统发展之初，系统比较简单，消耗资源小，用户访问量也比较少，我们只部署一个Tomcat应用就可以满足需求。系统架构图如下：
网关
Tomcat
DB
一个Tomcat可以看作是一个JVM进程，当大量的请求并发到达系统时，所有的请求都落在这唯一的一个Tomcat上，如果某些请求方法是需要加锁的，比如：秒杀扣减库存，是可以满足需求的，这和我们前面章节所讲的内容是一样的。但是随着访问量的增加，导致一个Tomcat难以支撑，这时我们就要集群部署Tomcat，使用多个Tomcat共同支撑整个系统。系统架构图如下：
Nginx Tomcat
Tomcat DB
上图中，我们部署了两个Tomcat，共同支撑系统。当一个请求到达系统时，首先会经过Nginx，Nginx主要是做负载转发的，它会根据自己配置的负载均衡策略将请求转发到其中的一个Tomcat中。当大量的请求并发访问时，两个Tomcat共同承担所有的访问量，这时，我们同样在秒杀扣减库存的场景中，使用单体应用锁，还能够满足要求吗？
单体应用锁的局限性
如上图所示，在整个系统架构中，存在两个Tomcat，每个Tomcat是一个JVM。在进行秒杀业务的时候，由于大家都在抢购秒杀商品，大量的请求同时到达系统，通过Nginx分发到两个Tomcat上。我们通过一个极端的案例场景，可以更好地理解单体应用锁的局限性。假如，秒杀商品的数量只有1个，这时，这些大量的请求当中，只有一个请求可以成功的抢到这个商品，这就需要在扣减库存的方法上加锁，扣减库存的动作只能一个一个去执行，而不能同时去执行，如果同时执行，这1个商品可能同时被多个人抢到，从而产生超卖现象。加锁之后，扣减库存的动作一个一个去执行，凡是将库存扣减为负数的，都抛出异常，提示该用户没有抢到商品。通过加锁看似解决了秒杀的问题，但是事实上真的是这样吗？
我们看到系统中存在两个Tomcat，我们加的锁是JDK提供的锁，这种锁只能在一个JVM下起作用，也就是在一个Tomcat内是没有问题的。当存在两个或两个以上的Tomcat时，大量的并发请求分散到不同的Tomcat上，在每一个Tomcat中都可以防止并发的产生，但是在多个Tomcat之间，每个Tomcat中获得锁的这个请求，又产生了并发，从而产生超卖现象。这也就是单体应用锁的局限性，它只能在一个JVM内加锁，而不能从这个应用层面去加锁。
那么这个问题如何解决呢？这就需要使用分布式锁了，在整个应用层面去加锁。什么是分布式锁呢？我们怎么去使用分布式锁呢？什么是分布式锁
在说分布式锁之前，我们看一看单体应用锁的特点，单体应用锁是在一个JVM进程内有效，无法跨JVM、跨进程。那么分布式锁的定义就出来了，分布式锁就是可以跨越多个JVM、跨越多个进程的锁，这种锁就叫做分布式锁。
分布式锁的设计思路
Nginx Tomcat
Tomcat DB
在上图中，由于Tomcat是由Java启动的，所以每个Tomcat可以看成一个JVM，JVM内部的锁是无法跨越多个进程的。所以，我们要实现分布式锁，我们只能在这些JVM之外去寻找，通过其他的组件来实现分布式锁。系统的架构如图所示：
Nginx Tomcat
Tomcat
第三方组件 DB
两个Tomcat通过第三方的组件实现跨JVM、跨进程的分布式锁。这就是分布式锁的解决思路，找到所有JVM可以共同访问的第三方组件，通过第三方组件实现分布式锁。
目前存在的分布式的方案
分布式锁都是通过第三方组件来实现的，目前比较流行的分布式锁的解决方案有：
·数据库，通过数据库可以实现分布式锁，但是在高并发的情况下对数据库压力较大，所以很少使用。
·Redis,借助Redis也可以实现分布式锁，而且Redis的Java客 户端种类很多，使用的方法也不尽相同。
·Zookeeper,Zookeeper也可以实现分布式锁，同样Zookeeper 也存在多个Java客户端，使用方法也不相同。
这3种方式具体的实现方法，我们会在后面的视频教程中做详细的介绍。


上面的程序中，我们模拟了50个线程同时执行i++，总共执行5000次，按照常规的理解，得到的结果应该是5000，我们运行一下程序，看看执行的结果如何？
执行完成后，i=4975执行完成后，i=4986
执行完成后，i=4971
这是我们运行3次以后得到的结果，可以看到每次执行的结果都不一样，而且不是5000，这是为什么呢？这就说明i++并不是一个原子性的操作，在多线程的情况下并不安全。我们把i+的详细执行步骤拆解一下：
1.从内存中取出i的当前值；2.将i的值加1；
3.将计算好的值放入到内存当中；
这个流程和我们上面讲解的数据库的操作流程是一样的。在多线程的场景下，我们可以想象一下，线程A和线程B同时从内存取出i的值，假如i的值是1000，然后线程A和线程B再同时执行+1的操作，然后把值再放入内存当中，这时，内存中的值是1001，而我们期望的是1002，正是这个原因导致了上面的错误。那么我们如何解决呢？在JAVA1.5以后，JDK官方提供了大量的原子类，这些类的内部都是基于CAS机制的，也就是使用了乐观锁。我们将上面的程序稍微改造一下，如下：
public class Test
private AtomicInteger i new AtomicInteger(0); public static void main(String[] args){ Test test new Test();
ExecutorService es Executors. newFixedThreadPo ol(50) ;
CountDownLatch cdl new CountDownLatch(5000); for (int i= 0；i < 5000； i++){
es. execute(()->{
test. i. incrementAndGet(); cdl. countDown();
}); 上
es.shutdown(); try
cdl. await();
System.out.println("执行完成后，i="+test.i); catch (InterruptedException e){
e. printStackTrace(); }
我们将变量i的类型改为AtomicInteger,AtomicInteger是一个 原子类。我们在之前调用i++的地方改成了i.incrementAndGet( ),incrementAndGet()方法采用了CAS机制，也就是说使用了乐 观锁。我们再运行一下程序，看看结果如何。
执行完成后，i=5000执行完成后，i=5000
执行完成后，i=5000
我们同样执行了3次，3次的结果都是5000，符合了我们预期。这个就是乐观锁。我们对乐观锁稍加总结，乐观锁在读取数据的时候不做任何限制，而是在更新数据的时候，进行数据的比较，保证数据的版本一致时再更新数据。根据它的这个特点，可以看出乐观锁适用于读操作多，而写操作少的场景。
悲观锁与乐观锁恰恰相反，悲观锁从读取数据的时候就显示的加锁，直到数据更新完成，释放锁为止。在这期间只能有一个线程去操作，其他的线程只能等待。在JAVA中，悲观锁可以使用synchronized 关键字或者 ReentrantLock 类来实现。还是上面的例子，我们分别使用这两种方式来实现一下。首先是使用synchronized关键字来实现：
public class Test
private int i=0;
public static void main(String[] args){ Test test new Test();
ExecutorService es Executors. newFixedThreadPo ol(50) ;
CountDownLatch cdl new CountDownLatch(5000); for (int i= 0；i < 5000；i++){
es. execute(()->{ //修改部分开始 synchronized (test){ test.i++; //修改部分结束 cdl. countDown(); )
}
es.shutdown(); try
cdl. await();
System.out.println("执行完成后，i="+test.i); catch (InterruptedException e){
e.printStackTrace(); }
我们唯一的改动就是增加了synchronized块，它锁住的对象是test，在所有线程中，谁获得了test对象的锁，谁才能执行i++操作。我们使用了synchronized悲观锁的方式，使得i++线程安全。我们运行一下，看看结果如何。
执行完成后，i=5000执行完成后，i=5000
执行完成后，i=5000
我们运行3次，结果都是5000，符合预期。接下来，我们再使用ReentrantLock 类来实现悲观锁。代码如下：
public class Test //添加了ReentrantLock锁
Locklock new ReentrantLock(); private int i=0;
public static void main(String[] args){ Test test new Test();
ExecutorService es Executors. newFixedThreadPo ol(50) ;
CountDownLatch cdl new CountDownLatch(5000); for (int i=0;i<5000;i++){
es. execute(()>｛ //修改部分开始 test. lock. lock(); test.i++;
test. lock. unlock(); /修改部分结束 cdl. countDown(); }1;
es. shutdown(); try {
cdl.await();
System.out.println("执行完成后，i="+test.i); catch (InterruptedException e){
e. printstackTrace();
我们在类中显示的增加了Lock lock=new ReentrantLock();, 而且在i++之前增加了lock.lock（），加锁操作，在i++之后增加了lock.unlock（）释放锁的操作。我们同样运行3次，看看结果。
执行完成后，i=5000
执行完成后，i=5000
执行完成后，i=5000
3次运行结果都是5000，完全符合预期。我们再来总结一下悲观锁，悲观锁从读取数据的时候就加了锁，而且在更新数据的时候，保证只有一个线程在执行更新操作，没有像乐观锁那样进行数据版本的比较。所以悲观锁适用于读相对少，写相对多的操作。
公平锁与非公平锁
前面我们介绍了乐观锁与悲观锁，这一小节我们将从另外一个维度去讲解锁——公平锁与非公平锁。从名字不难看出，公平锁在多线程情况下，对待每一个线程都是公平的；而非公平锁恰好与之相反。从字面上理解还是有些晦涩难懂，我们还是举例说明，场景还是去超市买东西，在储物柜存储东西的例子。储物柜只有一个，同时来了3个人使用储物柜，这时A先抢到了柜子，A去使用，B和C自觉进行排队。A使用完以后，后面排队中的第一个人将继续使用柜子，这就是公平锁。在公平锁当中，所有的线程都自觉排队，一个线程执行完以后，排在后面的线程继续使用。
非公平锁则不然，A在使用柜子的时候，B和C并不会排队，A使用完以后，将柜子的钥匙往后一抛，B和C谁抢到了谁用，甚至可能突然跑来一个D，这个D抢到了钥匙，那么D将使用柜子，这个就是非公平锁。
公平锁如图所示：
A
正在执行方法
多个线程同时执行方法，线程A抢到了锁，A可以执行方法。其他线程则在队列里进行排队，A执行完方法后，会从队列里取出下一个线程B，再去执行方法。以此类推，对于每一个线程来说都是公平的，不会存在后加入的线程先执行的情况。
非公平锁入下图所示：
D B
E A
正在执行方法
多个线程同时执行方法，线程A抢到了锁，A可以执行方法。其他的线程并没有排队，A执行完方法，释放锁后，其他的线程谁抢到了锁，谁去执行方法。会存在后加入的线程，反而先抢到锁的情况。
公平锁与非公平锁都在ReentrantLock类里给出了实现，我们看一下ReentrantLock的源码。
/**
Creates an instance of {@code ReentrantLock}. This is equivalent to using {@code ReentrantLock(
*/
public ReentrantLock(){ sync new NonfairSync(); }
/**
Creates an instance of {@code ReentrantLock} with given fairness policy.
@param fair {@code true} if this lock should use
*/
public ReentrantLock(boolean fair){
sync fair new FairSync( ) new NonfairSync( ReentrantLock 有两个构造方法，默认的构造方法中，sync=n ew NonfairSync（）；我们可以从字面意思看出它是一个非公平锁。再看看第二个构造方法，它需要传入一个参数，参数是一个布尔型，true是公平锁，false是非公平锁。从上面的源码我们可以看出sync 有两个实现类，分别是FairSync和NonfairSync,我们 再看看获取锁的核心方法，首先是公平锁FairSync的，
@ReservedStackAccess
protected final boolean tryAcquire(int acquires){ final Thread current Thread. currentThread(); int c= getState();
if(c==0){
if ( hasQueuedPredecessors()&& compareAndSetState(0, acquires)){ setExclusiveOwnerThread(current); return true;
else if (current = getExclusiveOwnerThread()){ int nextc c acquires;
if (nextc <0)
throw new Error("Maximum lock count exceede d" ) ;
setState(nextc); return true; }
return false;
然后是非公平锁NonfairSync的， @ReservedStackAccess
final boolean nonfairTryAcquire(int acquires){ final Thread current Thread. currentThread(); int c getState();
if (c == 0) {
if (compareAndSetState(0, acquires)){ setExclusiveOwnerThread(current); return true;
} }
else if current = getExclusiveOwnerThread()){ int nextc c acquires;
if (nextc 0)// overflow
throw new Error("Maximum lock count exceede d") ;
setstate(nextc); return true; }
return false;
通过对比两个方法，我们可以看出唯一的不同之处在于！hasQueuedPredecessors（）这个方法，很明显这个方法是一个队列，由此可以推断，公平锁是将所有的线程放在一个队列中，一个线程执行完成后，从队列中取出下一个线程，而非公平锁则没有这个队列。这些都是公平锁与非公平锁底层的实现原理，我们在使用的时候不用追到这么深层次的代码，只需要了解公平锁与非公平锁的含义，并且在调用构造方法时，传入true 和 false即可。
总结
JAVA中锁的种类非常多，在这一节中，我们找了非常典型的几个锁的类型给大家做了介绍。乐观锁与悲观锁是最基础的，也是大家必须掌握的。大家在工作中不可避免的都要使用到乐观锁和悲观锁。从公平锁与非公平锁这个维度上看，大家平时使用的都是非公平锁，这也是默认的锁的类型。如果要使用公平锁，大家可以在秒杀的场景下使用，在秒杀的场景下，是遵循先到先得的原则，是需要排队的，所以这种场景下是最适合使用公平锁的。
这一节讲的内容到这里就告一段落了，接下来，会给大家视频讲解如何使用锁解决电商中的超卖现象。



[image](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/6a8a40df-020c-4eea-a897-836171392086/2020-09-17_172930.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QPVJWHCH%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T225337Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCl14z%2BQhvrSTbRJjwKjQO%2BkdVs2jDoj1OPOvNo2V1YdAIhAPoy27ZEsdR5Nz3erwq0L2LKpLkKNRm3Hfngl1%2FvvYqGKogECMb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgwYognO%2Fi7e2snVWJkq3AN%2FBkm%2BXP%2F7zREovTa1o0FLss0KbIYDl59gueOcEH0AeWqulUVaDqgt6lf9QVJXLpN8TLf%2B5TA10iUJ056uFFEIY6bFYadstDqsD9YyzHN1234kjD6L2KTTaGupwp6mOhInVk9S7YNDElwfQLlWWTr3kLc0CJsV4o8yXNK09iL9qP85QIKB60yufTPFdbE0KIEVtKUmthBCG8EpXKxkWmTvATiRB%2BP29rZeuEswPk6vSPBC6TDZIMdI85p7jlLwzeFmdJzC0hj4ZN4rmMu%2FKEI7e6Y4aE0fvlejPO1q%2Bw%2BBv%2BD5tI8UDMY7XWFg47ltiOemWuhWvyvrTLqwxLAeNFgJUVofCsLi3YyLDIEZJ%2Br%2FYV6ym4J7z%2BIcK29Qx6sOZXIpbqVGC%2BHVE6EqvQrkBBDf6x9uquYnoTE5VUTfv2SF%2B77ZPlcI4eHrFnk11XaZWS3vQP8wFU3kyrZAv2VLEQpqKMGd5Y%2FG29k%2BXIvHG481BImCxoD%2FlBIySzjh%2FEGgmNTPpBfmdLvODKw%2B9Tk9FlAwFf%2B7zhn3Tcm4AgxKCW8MdqAhYIpt9BZi0Y9boEDSQk%2FZ%2FCP%2B1WqzLDIyqgodRjvxqgk%2Blq3LQDkTRVaOkpvURymT%2BhubKPw9dQE3YjCQuP%2FSBjqkAdLry3VfrUmOuvEAeFGuZ2pmlfBhZ4bf4QpRbohKs5caz91llTDJa2jgq27mgCAKqU4VFyXt4NFUtvPWCmZYXszfyBv2R88lVLSRcA19GeKO6VYplj9sx2JS5Uu%2BDOkT1%2Fj9Equ4jyyqgi%2FXXmEft8XLWcSeGSG%2Bg%2F8m3fJMsZ6oYOHh7Abp9qtXYTVe2IRiQPRtVyiONvnhWwcrox2v%2F71sxd43&X-Amz-Signature=e8ae9f2396fdbff06227a02df2c24648524459f1d167502d978293c7aa36ad90&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

[image](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/24fe1e6b-6fb7-4e33-b976-7bd5b7aa8026/2020-09-17_172956_copy.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QPVJWHCH%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T225337Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCl14z%2BQhvrSTbRJjwKjQO%2BkdVs2jDoj1OPOvNo2V1YdAIhAPoy27ZEsdR5Nz3erwq0L2LKpLkKNRm3Hfngl1%2FvvYqGKogECMb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgwYognO%2Fi7e2snVWJkq3AN%2FBkm%2BXP%2F7zREovTa1o0FLss0KbIYDl59gueOcEH0AeWqulUVaDqgt6lf9QVJXLpN8TLf%2B5TA10iUJ056uFFEIY6bFYadstDqsD9YyzHN1234kjD6L2KTTaGupwp6mOhInVk9S7YNDElwfQLlWWTr3kLc0CJsV4o8yXNK09iL9qP85QIKB60yufTPFdbE0KIEVtKUmthBCG8EpXKxkWmTvATiRB%2BP29rZeuEswPk6vSPBC6TDZIMdI85p7jlLwzeFmdJzC0hj4ZN4rmMu%2FKEI7e6Y4aE0fvlejPO1q%2Bw%2BBv%2BD5tI8UDMY7XWFg47ltiOemWuhWvyvrTLqwxLAeNFgJUVofCsLi3YyLDIEZJ%2Br%2FYV6ym4J7z%2BIcK29Qx6sOZXIpbqVGC%2BHVE6EqvQrkBBDf6x9uquYnoTE5VUTfv2SF%2B77ZPlcI4eHrFnk11XaZWS3vQP8wFU3kyrZAv2VLEQpqKMGd5Y%2FG29k%2BXIvHG481BImCxoD%2FlBIySzjh%2FEGgmNTPpBfmdLvODKw%2B9Tk9FlAwFf%2B7zhn3Tcm4AgxKCW8MdqAhYIpt9BZi0Y9boEDSQk%2FZ%2FCP%2B1WqzLDIyqgodRjvxqgk%2Blq3LQDkTRVaOkpvURymT%2BhubKPw9dQE3YjCQuP%2FSBjqkAdLry3VfrUmOuvEAeFGuZ2pmlfBhZ4bf4QpRbohKs5caz91llTDJa2jgq27mgCAKqU4VFyXt4NFUtvPWCmZYXszfyBv2R88lVLSRcA19GeKO6VYplj9sx2JS5Uu%2BDOkT1%2Fj9Equ4jyyqgi%2FXXmEft8XLWcSeGSG%2Bg%2F8m3fJMsZ6oYOHh7Abp9qtXYTVe2IRiQPRtVyiONvnhWwcrox2v%2F71sxd43&X-Amz-Signature=78e849d7ed119078201ad21bcb188bc8e056d2a23a7559c12c4659254d4c9bf4&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)


