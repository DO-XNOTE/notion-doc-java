---
title: 2-7 单体应用锁的局限性-实操
---

# 2-7 单体应用锁的局限性-实操

[image](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/33f8fea0-c12c-4a3d-abef-9e113004af6a/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YZJNIDXS%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T225343Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCXvHTrkWQwTx8oijYCycdSNtTSnJC5D6bGnNQcCqvz4gIgbOrrZV7b9kUngtiAcsSxmveJdUz%2BEJq3VNAlsehKM7EqiAQIxv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDMMq%2BTt%2BXSVkWSWJWSrcAzSPcXAu5x6C0mg7qB4BJOliFgIpKWqVxWP%2B4o7YVQXW0%2Bi%2BLTorC1PNShXrDyklL7OFm5LPpoD4I1LIPBExwi5OLYf%2BECng2Hrz3vVr%2FtJVWDDQkPSHwwcS%2BXGb1kKthYobhKCHVtDdkO32%2BFM2cALf7%2BgS3TdGh0HM3QbxCCV55kI1QzUuCE%2BctyOfnRlPWYA4fzjwu%2FyJGzhP7IGbqR2QRXd1HWmcWet61FhSXEXTXGcoLV1uS9UcWXkcL3PKzikXc4KCB193QUlrBHBmr3nNRgcTAOCz%2BSU%2BKx1gX3xUjnMNBwM%2Bu0uLBFNYJAEaFhMKvvzO3yu%2BY%2BJ838a%2F%2BT2RX8gNtDT0YLT3eKmLjS7g7hjFEWydf9lEDJdqNUavlXoRAvc1G84cZ8Duu5%2FS94JrgTP3Yu21yXcgZhlz5HCdP%2FNCDuNTydfVQRzxO8cpAMB9bO4N7jkBMjXAU0c%2F88jUcPE2jeRozuWpeQno3Qc%2BVvjDoZkuX9eLDk5eR1stytl%2FSuN2rdb%2FGzZlTCsL0f2%2Bb5Txbk3ewhSm8uow8wMw593c1OgmgzeP4EbyiU8ugi4CZEl0VGTPXSG7tfd4zpKgVEWZA%2BpSecIMaf%2BPA%2FPwc90LUPhZWdMVHap4MJW4%2F9IGOqUBW02Qj3yji3lnRSduanLg8gnX0um8mX5bdEr3r3I1etMNbQo3w7YOfkkONqXGgpgkPQMAerUUA8mpc6s7sirp%2BCuuog%2B2gFzX3eBhN9w1x%2F6A2WFkPklgVu4hV535pIDFOgo7NLQwPUIS6mp0ebLb1MjOZgl2CgAAYauZi%2FM8AjbgMetqht8Y0MMsa5eQ%2FN%2FGYq9WslL%2BLdiSK1d%2FGYbnDGjuvmI2&X-Amz-Signature=af220e6a36b7b92509efcec513a57e443770ce7c0897c22d5c4720cddf5ed877&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

[image](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/ffc1c7cd-884e-4b34-89be-5d91b28f6d17/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YZJNIDXS%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T225343Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCXvHTrkWQwTx8oijYCycdSNtTSnJC5D6bGnNQcCqvz4gIgbOrrZV7b9kUngtiAcsSxmveJdUz%2BEJq3VNAlsehKM7EqiAQIxv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDMMq%2BTt%2BXSVkWSWJWSrcAzSPcXAu5x6C0mg7qB4BJOliFgIpKWqVxWP%2B4o7YVQXW0%2Bi%2BLTorC1PNShXrDyklL7OFm5LPpoD4I1LIPBExwi5OLYf%2BECng2Hrz3vVr%2FtJVWDDQkPSHwwcS%2BXGb1kKthYobhKCHVtDdkO32%2BFM2cALf7%2BgS3TdGh0HM3QbxCCV55kI1QzUuCE%2BctyOfnRlPWYA4fzjwu%2FyJGzhP7IGbqR2QRXd1HWmcWet61FhSXEXTXGcoLV1uS9UcWXkcL3PKzikXc4KCB193QUlrBHBmr3nNRgcTAOCz%2BSU%2BKx1gX3xUjnMNBwM%2Bu0uLBFNYJAEaFhMKvvzO3yu%2BY%2BJ838a%2F%2BT2RX8gNtDT0YLT3eKmLjS7g7hjFEWydf9lEDJdqNUavlXoRAvc1G84cZ8Duu5%2FS94JrgTP3Yu21yXcgZhlz5HCdP%2FNCDuNTydfVQRzxO8cpAMB9bO4N7jkBMjXAU0c%2F88jUcPE2jeRozuWpeQno3Qc%2BVvjDoZkuX9eLDk5eR1stytl%2FSuN2rdb%2FGzZlTCsL0f2%2Bb5Txbk3ewhSm8uow8wMw593c1OgmgzeP4EbyiU8ugi4CZEl0VGTPXSG7tfd4zpKgVEWZA%2BpSecIMaf%2BPA%2FPwc90LUPhZWdMVHap4MJW4%2F9IGOqUBW02Qj3yji3lnRSduanLg8gnX0um8mX5bdEr3r3I1etMNbQo3w7YOfkkONqXGgpgkPQMAerUUA8mpc6s7sirp%2BCuuog%2B2gFzX3eBhN9w1x%2F6A2WFkPklgVu4hV535pIDFOgo7NLQwPUIS6mp0ebLb1MjOZgl2CgAAYauZi%2FM8AjbgMetqht8Y0MMsa5eQ%2FN%2FGYq9WslL%2BLdiSK1d%2FGYbnDGjuvmI2&X-Amz-Signature=13969aaabfd2e051235601cfcd76a6f6bfabb42474f17958144a850efc43cbe6&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

hello 大家好，在前面图文的课程当中，我们给大家介绍了单体应用锁的局限性。单体应用锁的局限性就是它不能够跨 JVM 就是你有两个 gvm 进程的话，它只能在一个确定的 gvm 里边去使用这个锁，如果跨 gvm 它是实现不了的，正是为了解决它这方面的局限性，所以才有了分布式锁。

对不对？在给大家介绍分布式锁之前，咱们先搭一个 demo 让大家看看这个单体应用锁是不是存在这个局限性。咱们还是先打开 idea 然后新建一个项目，咱们选择新建对吧。新建项目。这里面咱们还是新建一个 spring boot 项目，使用 JDK 使用的是 1.8 这个版本。然后点击下一步。在这里边写一些咱们项目的基础的信息，咱们只把这个名字给它改一下，叫做 distribute lock 分布式锁。然后点击下一步。在这里边添加一些咱们比较常用的夹包我们比较常用的 long book 然后 web 里边选择 web starter 再有就是数据库的一些配置，咱们选择 SQL 对吧。首先要选择四名 data GPA 这里边有一些数据源的配置都在这个 GPA 里边，所以咱们要给它选中，然后 MySQL 的驱动这个也是必须要选的。


最后在咱们的项目当中使用 mybatis 对吧，然后把 mybatis 也给它选中，其他的一些咱们暂时先用不到，在这里就先不选了对吧，难得下一步，然后完成在当前窗口打开，然后刷新一下 Maven 好了，这个项目已经搭建好了，咱们看一下这个项目里边的泡沫文件都没有问题对吧。


然后咱们新建一个 controller 进入到它的这个 Java 的目录当中来，这个就是它的启动类是吧，咱们点开看一下也没有什么问题。再新建一个目录，创建一个 controller 是吧，咱们要写一个 controller 然后通过这个访问来模拟它的这个锁的情况对吧，新建一个类咱们叫做 demo demo controller 然后在这个类上打个注解。 rest controller 里边咱们写一个方法， public stream 叫做 single lock 对吧，单体应用锁 single lock 然后加个 request mapping 是吧，也叫做 single lock 然后里边咱们攒个字符串，攒个什么叫做我已经执行完成。在前面咱们要加个锁，看看它在这种分布式的环境下，跨 JVM 能不能把这个语句给它锁住。这块咱们还是用 central needs 的还是用 reentry 的lock ，咱们还是用 1.5 以后这个官方比较推荐的，这个可重误所对吧。


reentrant lock 第二个对吧？然后这块咱们给它加一个锁。 Lock. 下边咱们要打印出日志是吧，日志用 long book 给咱们提供非常简便的写法。对吧？在这个类上给它加一个注解，然后直接就可以使用 lock.infer 这块咱们写什么呢？写我进入了锁对吧，然后这块咱们再给它线程休眠一下，休眠多长时间呢？休眠一分钟。 60 秒对吧，它的这个单位毫秒是吧？ 1000 毫秒等于 1 秒，咱们写了 60 秒，然后再加个 try catch 最后咱们再把锁给它释放，按 lock 对吧，一会咱们模拟的时候直接访问到 single lock 里边来。然后这块要休眠一分钟。


在这休眠的一分钟当中，咱们如果再次访问的话是进入不了下面的这一段的，他会在这给锁住。但是如果在分布式的环境下他能不能锁住呢？一会咱们给大家演示一下，为了方便，咱们在这个锁前面咱们也加个日志，我进入了方法，然后咱们先启动一下访问启动一下应用。这块报错了是吧，咱们看看报什么错，说你没有配置 data source 的 URL 那这块咱们先把这个数据库的相关的东西，咱们先给它注掉。就是因为你引入了这个 GPA 的价包，所以它去寻找你的数据库的配置，但是咱们还没有配是吧这块所以报错了，咱们先把这个给它注掉试试 my betis 也给它注掉。


好，咱们再启动一下程序，现在已经启动起来了对吧，端口是8080，然后咱们再打开这个头，斯特曼工具，投资人们通过它去模拟这个两个请求，咱们先新建这个。第一个请求是吧， local host 8080 杠 single lock 咱们把这个给它复制一下，然后发送请求，再新开一个窗口再次发送。这个时候就是有两个请求同时访问了 single lock 对吧，咱们看一下这个日志可以看到第一个请求已经进入了方法，进入了锁。


第二个请求只进入了方法是吧，锁它是没有进来。咱们再看一下前面的这个日志这个日志的这一段，这个就是它的线程号是吧，可以看到前面这两个日志是同一个线程去执行的，后面的这一条日志是另外的一个线程去执行。第二个线程由于获取不到锁，他一直在这等待进入不到下面的这个方法。好，咱们看到这块在 52 分钟 12 秒的时候，它进入了锁，整整等待了一分钟。因为它前面的这一个线程是在 51 分 12 秒的时候进入到锁过了一分钟以后，也就是咱们县城休眠的这个时间，过了这么长时间以后，这个锁释放了。然后另外一个线程进入，就是 52 分 12 秒进入的这个线程对？这个是单体应用对吧，在单体应用的时候，我们可以正常的使用这个锁对吧，咱们来看看 post map 现在两个请求都已经执行完成了，日志也已经打印出来了。下面咱们再模拟这个分布式的情况。


在现在一般一个应用都很少只部署一台了，现在这种情况就是只部署了一台机器，这样就存在了单点故障。如果我这台机器不可用，那么所有的这些应用服务就全都不可用了。所以咱们一般都会集群部署两台三台，最少咱们也要部署两台，能够非常有效地避免它的单点故障。


现在咱们在同一台机器上，咱们再启动一个服务端口，咱们给它设置成为 8081 对吧，这样就是模拟出两台应用了对吧，咱们只需要把这个给它复制一下，起个名字，后边就跟它的端口号 8081 是吧。然后我们给它加一个参数，杠杠 server.pot 等于 8081 剪辑。 OK 好，咱们现在再启动一个服务，已经启动起来了，端口是8081，前面的这个应用它的端口是 8080 对吧？然后咱们模拟一下，现在这两个请求访问的都是 8080 这个服务。那么如果在分布式的情况下，一个访问8080，另外一个访问8081。这个时候咱们再看看打印出来的日志这块这个锁到底能不能锁住？咱们模拟一下 8080 这个服务发送请求，然后 8081 再发送请求，再回到程序当中去看一下日志。


现在这个是 8080 这个服务对吧？打印出来的日志是进入了方法进入了锁，咱们再看八零八一，八零八一也是进入了方法进入了锁，那等于是说这块这个锁是没有生效的。我们在集群部署的情况下，这个锁是没有办法实现这种跨 JVM 跨多应用。咱们分布式锁就是要解决这个问题，就是要在集群部署的情况下，这个锁依然有效好。单体应用锁的局限性，这个 demo 咱们就先给大家介绍到这。接下来咱们要给大家介绍的就是使用数据库去实现分布式锁。



