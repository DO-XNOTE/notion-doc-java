---
title: 2-10 基于redis实现分布式锁
---

# 2-10 基于redis实现分布式锁

[image](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/840eb97f-d3f4-441b-ab0d-1ef4ae06df34/SCR-20240807-jrca.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665NPH7MVQ%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T225345Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCICFiCd2IFDKKuHZwtCbZnjQ8wxY4MTm40MRw8RfSo7%2FtAiBbzheeYxsQbMxzoYtZerRXZDPW84FnBagPCzLf%2FfIU1iqIBAjG%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIM%2F453AMf9kDV8DHdAKtwDxL6qiA35yqtdKpmW8quJdcznNdisc9BREp2sjA%2B0%2Bq8weiaXrmMXzjIR74B0o2h%2FRkWvHqDqzEJYtoi9jZzeWXcWFfWxBu1STo%2BZ7YqePeJy9efTu%2F%2FX87KTiRUkXYkB9mUV6sc5y4xoluTz2iriEY2Ie%2B%2BAGIDcpWGjqJ6foZUg0QR%2BU%2B5r4j55%2FjMYA%2B00oVkjwsS4Ec9CyzS7cX4mce9ZD4wOYXIVvXM73W6%2FMG8Ju2izKSho4oz8ICpZ8obwqLPqMrpCnkX9UEJYt4WvyBMPKzUnxt1B%2BqT4HWowau0qPCjLxEi4IPVenrteQsbsmyUyp6EgIJJsyvrA9feX9tTafSodBbAl1fDxcectvJocSde6kS170IWVRzzEsWj5qaUYbQn5F7xZFREGRjZTM7oe%2BROy9rkogW1%2BIKM3b3vxAarhU%2FM7MBsvPvXg%2BMHioq8Lv%2Fig4gad1eTkUpw5WMUjksHy%2BI7m0ww627BLNbSjUq1H4cZCcR8t%2BKAUuBja%2BJJvsHgzBZkTfB%2Bv3OD7pXAKUF%2BPoSFbMlas6XANtqdT8nUuuT%2FNxMZ%2B%2B34epjzUrAw4q2c1wjkzF5YMx%2FscW7es9AWDY5th1NSUMKHzYRC5H6EfS3Vl0TSixw8wnrr%2F0gY6pgHnp%2FK3sgxN10TcBkL8ODxQqvxlcR7B%2Fa8KwmdKT2tEIj9ofIgvNtBe7my0REBsyxKmmnla1%2FibuFiGHFHW2Ee7GjDjOQi7Obe0mmk1ehBVhNJo%2B1kYrKI4RegGl%2B8zlpzY%2Fa96XP7kOZ1gMsF7JV4tiJpi0HHUzmZ5MyJI1eCSnXQ8nW%2F2n9JTdo15VVZtTrLU7yO5cKiw%2FpycStGNwGdcAeFKLvth&X-Amz-Signature=7a186346fde2763520ce3a5ef2d4ab784facee6c661b1a53dc5024fe7a9fa046&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

[image](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/1635922d-8efc-471c-afac-d702e7c60684/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665NPH7MVQ%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T225345Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCICFiCd2IFDKKuHZwtCbZnjQ8wxY4MTm40MRw8RfSo7%2FtAiBbzheeYxsQbMxzoYtZerRXZDPW84FnBagPCzLf%2FfIU1iqIBAjG%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIM%2F453AMf9kDV8DHdAKtwDxL6qiA35yqtdKpmW8quJdcznNdisc9BREp2sjA%2B0%2Bq8weiaXrmMXzjIR74B0o2h%2FRkWvHqDqzEJYtoi9jZzeWXcWFfWxBu1STo%2BZ7YqePeJy9efTu%2F%2FX87KTiRUkXYkB9mUV6sc5y4xoluTz2iriEY2Ie%2B%2BAGIDcpWGjqJ6foZUg0QR%2BU%2B5r4j55%2FjMYA%2B00oVkjwsS4Ec9CyzS7cX4mce9ZD4wOYXIVvXM73W6%2FMG8Ju2izKSho4oz8ICpZ8obwqLPqMrpCnkX9UEJYt4WvyBMPKzUnxt1B%2BqT4HWowau0qPCjLxEi4IPVenrteQsbsmyUyp6EgIJJsyvrA9feX9tTafSodBbAl1fDxcectvJocSde6kS170IWVRzzEsWj5qaUYbQn5F7xZFREGRjZTM7oe%2BROy9rkogW1%2BIKM3b3vxAarhU%2FM7MBsvPvXg%2BMHioq8Lv%2Fig4gad1eTkUpw5WMUjksHy%2BI7m0ww627BLNbSjUq1H4cZCcR8t%2BKAUuBja%2BJJvsHgzBZkTfB%2Bv3OD7pXAKUF%2BPoSFbMlas6XANtqdT8nUuuT%2FNxMZ%2B%2B34epjzUrAw4q2c1wjkzF5YMx%2FscW7es9AWDY5th1NSUMKHzYRC5H6EfS3Vl0TSixw8wnrr%2F0gY6pgHnp%2FK3sgxN10TcBkL8ODxQqvxlcR7B%2Fa8KwmdKT2tEIj9ofIgvNtBe7my0REBsyxKmmnla1%2FibuFiGHFHW2Ee7GjDjOQi7Obe0mmk1ehBVhNJo%2B1kYrKI4RegGl%2B8zlpzY%2Fa96XP7kOZ1gMsF7JV4tiJpi0HHUzmZ5MyJI1eCSnXQ8nW%2F2n9JTdo15VVZtTrLU7yO5cKiw%2FpycStGNwGdcAeFKLvth&X-Amz-Signature=af5676318fc8736827c492ab601a0fc2e6f365e19d387a74317c6baaa62aa33d&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

在编写这个 Redis 分布式锁之前，咱们要把这个环境先准备好。在这里边咱们已经准备好了一个虚机， Redis 也上传到这个虚机里边来了。下面我们把这个 Redis 启动一下。关于这个 Redis 的环境搭建，在前面的课程当中，其他的老师已经给大家讲解了，如果大家还有什么不明白的地方，可以看一下前面老师的视频。现在咱们这里边就把这个 Redis 给它启动一下，现在已经启动起来了，然后咱们再打开 idea 编写这个分布式锁的程序。好，咱们还是在这个分布式锁这个项目当中，这个项目是上一节课，使用数据库作为分布式锁给大家搭建的对吧。然后咱们这一节要创建一个 Redis 的分布式锁。


下面咱们同样写一个 controller 是吧，新建一个 Java 类叫做 Redis lock controller 然后打上一个注解 rest controller 里边写一个方法叫做 Redis lock 然后返回字符串，咱们先返一个空，省得他报错。这个方法上打一个注解 request mapping 对吧，叫做 ready slog 在里边就需要写咱们的 Redis 程序了。在写这个程序之前咱们要引入一个 Redis 的客户端是吧，这个 Redis 的客户端是通过咱们程序连接 Redis 的这么一个工具。咱们在这里边采用 spring boot 为咱们提供的就是这个 spring date Redis 之前咱们在这块使用 spring date jpa 使用它去连接数据库。下面咱们再引入另外一个这个依赖 spring date Redis 它是连接 Redis 的工具，咱们刷新一下 Maven 好已经引入成功了。然后咱们可以在这个 props 文件里边儿配置这个 Redis 咱们看一下有什么东西 spring 点儿 Redis 咱们把这个 Redis 的 host 给它配上就行了，因为这个 Redis 咱们的端口就是默认呐 6379 这个 host 咱们看一下IP ，打开那个叉 shell 咱们的这个 IP 是幺九二点幺六八点七三点幺三零。回到程序当中，幺九二点幺六八点七三点幺三零。好，咱们只需要配置这么一个东西就可以了。


然后回到 controller 这个类里边来，咱们要引入一个 Redis 的 template Redis template 自动注入 autobear 然后咱们就要写这个分布式锁了，这块咱们同样还是写一个案例，把这个日志给它打印出来。日志打印咱们还是用这个 log back 是吧，用这个 long book 给咱们提供的这个日志的简写方法。


首先在这里面落个点 infer 我进入了方法，然后就要获得这个分布式锁，获得分布式锁咱们要调用这个 set 方法是吧。 set NX 方法这块咱们怎么用呢？咱们直接用这个 Redis templateredis template 点儿什么 execute 方法 Redis callback 是吧，咱们用这个它里边儿要传一个 Redis callback 咱们点进去看一下要传一个 Redis callback 咱们在这个方法前面先给它定义一下 Redis callback 引入一下，咱们看一下它也是一个接口，并且有一个 do in Redis 的这么一个方法都在这里边给它实现 do in Redis 这个方法这块咱们可以用 lambda 表达式，咱们再具体看一下。 do in Redis 这个方法它有一个 connection 这么一个参数是吧，咱们这个拉姆拉表达式就要这么去写了，已经给咱们提示出来了。然后 Redis template 的这个泛型咱们选择布尔，因为咱们要执行 set NX 这个方法，如果设置成功，它返回 true 表示咱们抢到了这把锁，可以进行后续的操作了。


然后里边咱们要执行 set NX 这个方法，咱们看一下，咱们要用的是不光 set K 和 value 还有它的过期时间，还有后面的这个 NX 这个操作。咱们先把这个方法给它写在这，咱们把这个四个参数先定义一下。首先是这个 set option 等于 set option.if absentif absent 它是什么意思呢？就是 NX 是吧，咱们点进去看一下，看到它的源码里边 if absent 上面就是 NX 就是说如果没有的话，这个 K 不存在的话，它会设置成功。如果 K 存在了，它设置的就是不成功的。这个咱们先在这一块给它定义好。然后还有一个过期时间，咱们点进这个 set 方法看一下传入一个过期的时间，咱们看看这个怎么写好。引入 expiration.second 就是秒的意思，后边 second 咱们设置过期时间，设置 30 秒，过期时间和这个 NX 咱们都已经写好了。那么前面还有 key 和 value 要去设置，咱们再看一下这 set 方法，这个 set 方法 key 和 value 都是 byte 类型，咱们的这个 string 类型不能够直接传进去。那么咱们先把这个 key 和 value 定一下。 string key 等于。那么写个字符串，Redis key string value 这个 value 咱们要保证所有的线程都不能相同，这个咱们只能使用 UUID 了，是最简单的对吧。


to string 这个 key 和 value 因为咱们在释放锁的过程当中也要用到，所以咱们把这个给它提到方法外边来，咱们来看一下里边这个 key bat ready 是 key 咱们这块不能使用 t.get bite 这么简单粗暴的转是不行的。这个 Redis time prodate 里边有一个 key 和 value 序列化的这么一个工具，咱们要使用这个工具去转换 Redis template 点儿 get key serilizer 是吧，key的序列化，然后点儿 serilizer 传入咱们的 key 这样就没有问题了，千万不能简单粗暴的直接 key.get back 这样你后续会出现问题的。同样 value 咱们也用这个方法，Redis value 等于 Redis template 然后点 get value three laser 对吧。前面是 get key 的序列化工具，下面是 get value 的序列化工具，然后点 serializer.value 这样 key 和 value 咱们都已经创建好了，下面就调用它的 set 方法。第一个参数， Redis key 第二个参数 Redis value 第三个参数过期时间。第四个参数是这个 NX 是吧。最后前面用变量给它接一下 result 结果。最后要返回这个 result 好乐意思。


call back 这个接口咱们就已经写好了，这块咱们给加个注释。第一行设置 NX 设置过期时间序列化 key 然后序列化 value 这一步是执行 set NX 操作对吧，最后返回一个操作的结果。然后咱们把这个具体实现好的这个 call back 放到这个 excuse 里边来，前面用变量接一下。它的返回结果应该是布尔类型，这个变量咱们叫做log ，获取分布式锁，如果获得到了锁，然后这块咱们打印一个日志叫做我进入了锁。


后边咱们再模拟一个处理过程 thread.sleep 模拟。这个过程咱们写一个 15 秒，咱们这个 set NX 设置这个 Redis 的值，过期时间是 30 秒。咱们模拟这个任务模拟它运行 15 秒，这块咱们加一个 trackache 最后 finally 不管怎么样，执行完成以后咱们要把这个锁给它释放掉。


那么这个释放锁的方法咱们要使用这个 Lua 是吧，Lua脚本这块咱们怎么写也是通过这个 Redis template Redis template 然后点找到这么一个方法，它需要传入的参数是 Redis script 也就是说是 Redis 脚本，这个就可以传入咱们之前写的那个 Lua 脚本，然后后边是 key 和 UG 和一些参数，咱们就使用这个方法就可以。然后前面咱们要准备一下这个 Lua 脚本是吧？ Redis script 咱们看看这块有一个泛型是吧，咱们看看这泛型是什么意思？这 script result type 这个泛型是你脚本的结果的类型。 should be one of 是下列当中的一个，可以是 long 型，可以是布尔型，可以是 list 或者是反序列化的一些实质的类型。在这里咱们使用布尔这块，咱们就写布尔就可以了。


Redis script 等于 Redis script 点儿。 off 是吧。 off 里边儿有两个参数，第一个参数 script 脚本是一个 string 类型，另外一个 class 它是 result type 咱们也需要传一下 result type 就是布尔类型要返回 true 和 false 然后前面咱们把这个 Lua 脚本写到这里边来，string script 等于这个 Lua 脚本，咱们回到前面的 PPT 在 PPT 当中把这一段复制一下，回到咱们的程序写在这个字符串里面。然后把这 4 query 的传到 off 里边来。然后还有一个参数就是返回值的类型，布尔点 class 对吧。这个 screw 的脚本也已经创建好了。


然后第二个参数咱们点进去看一下。 Redis template. 第二个参数是一个 key 它的 key 是一个 list 类型是吧。那么咱们也构造一个 list teeth 等于 [aris.at](http://aris.at/) least 然后传入咱们之前的这个 key 这个 key 是一个 string 类型的是吧。然后 y6 咱们再看一下，点进去看一下。


y6 是一个可变长的数组，这个咱们直接把这个 value 传进来就可以了。好，现在咱们把这个方法给它完善一下外地词 script 第二个参数，key最后再传入 value 这块咱们再用电量它接一下，给它强转一下，然后把日志给它打印一下。释放，锁的结果 result 对吧，最后返回一个方法执行完成。


方法执行完成，前面打一个日志，也叫做方法执行完成。这么一个锁的这么一个方法就给大家写好了，咱们再从头看一下一个请求发送过来，进入到 Redis lock 这个方法首先打印了一条日志，然后就是一些准备的工作是吧。准备请求这个分布式锁后边在这一步他就要获取这个分布式锁了。这个分布式锁咱们设置的 key 就是 Redis key 对吧，采用 set NX 这个方法如果成功了，那么就获得了锁，然后进入到这个锁里边来休眠 15 秒模拟其他的任务。这个任务执行完成以后进行释放锁的操作。释放锁，咱们用 Lua 脚本去释放，把这个脚本已经写在这了。最后把锁，释放成功，咱们打印一个日志。


最后方法结束，咱们先启动一个服务，咱们运行一下，看看有没有问题。好，启动成功是吧，端口是8080。然后咱们打开浏览器访问一下这个 Redis lock local host8080 Redis lock 是吧。那么访问一下，看看后台的打印结果，我进入了方法，我进入了锁对吧，看来咱们获取锁是没有问题的，然后等待 15 秒，看看它释放锁是不是有问题可以看到，释放锁也已经成功了，返回的结果是处方法执行完成。


那么没有问题，咱们再启动一个 8081 端口的服务。然后咱们分别访问 8080 和8081，看看他们两个后台的日志会是什么样的。好，现在 8081 这个服务也已经起来了，咱们先把日志先清一下，方便后边观察，咱们复制一下。这个是8081，咱们先访问8080，然后再访问8081。好可以看到 8080 这个服务打印出来，日志进入了方法，进入了锁，然后 8081 的日志咱们看一下，我进入了方法，然后方法执行完成。那么说明 8081 这台服务请求过来的时候他没有获取到这个分布式锁，他没有到这个 if 里边来直接打印方法执行完成。那么现在说明咱们这个使用 Redis 实现的这个分布式锁是没有问题的。好了，这一小节的内容先到这下一节，咱们要给大家介绍如何使用 Redis 分布式锁来实现定时任务的集群。






