---
title: 2-14 zookeeper分布式锁代码实现-1
---

# 2-14 zookeeper分布式锁代码实现-1

[image](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/e983d155-d522-4d2f-88ea-54635374dfe4/SCR-20240807-kbiu.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46675HGFQWW%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T225349Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDd5HL1OcvgrhpSFOjkbkXDiiGZzDAUdrSXuLgw0i2GswIhALN5DT3lWeVrr8PZFB9QFqSBqEZVUUH0OM3ni4%2F02ZGvKogECMb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgwjVMCAyM4aDlyiDtkq3AMf7mkxnCMOEUQQ8g0kZfDZLE7D6ryQ0H%2F9vJfipSWgOagWHLfZ4i%2BLhzov2g7fqaN49fSudK18ABlrur5nBTGsyNxc5BzzzgP2SJaWMWuWmuU7PmSjBzFD1K7TQP97XSTChhObnFHiG0hgvHHRVe8uT3MFMy9J%2BReluoMc13zoqyEgNMXYuD2uXB%2Fe3eCzIGYtkZpK9uN9PlVtMtZLt%2BDdfmvm4YH7bpFXJihxeBeK3LP2y6hDy66HUsHV6hJqKfcffeI%2BLt%2BoQpmxv980LYlTDz3pGo9jfmaEy7iaI0BckjLx4qtv5%2BQIPIWYG979S9oEkMVBXFW%2BStcLMicuwAHdM0id4gKOXuzv7Si%2F3IGbbr%2F7QiRXQklPly9Ooi7%2BxwhKoEhLsk1NVPxFgQi7rPinT2Mv%2BA8xi%2FiQZ8bV70JRs7fdsGDF%2FcEIAo9c0e8riAXDk6dw6kBs%2F7Qo%2Fg%2FEdBo%2BmP66r8pv0jiVE%2BnMmL%2B3z5PS7bxj%2BtYjZ2BWcly8GqAkcMQeN5Snj6j3RnkQAfpFNuCky70rtmhaIyt0LK8LuUfbXiitRQHm2RPfdRKByR%2BCMolPVDZDAjXE0w%2FOQbwC6SuiDKHXo%2FHNS%2BrgdLt32p92EuSrtgsjGIJH6DC0uP%2FSBjqkAeLS2jNoAmVm2%2FAk1Il1B879pWttmXpMkoKl7OQ1a%2BBsdkTbKlXan69bSltaaz4fMNUy%2FyVp8caFFgtPIYHeFl%2ByvwxJTZtUWHR0HHfPrwwVK7x%2FF1f8lfgA8UsuGqaLlPpzE7cIDTUf7fT8%2FTHe9lkRuViv9D0VKHrYn0uAgAH7jngraJYF7IMeDmfKEnjW%2FDo%2FdNQcjZfz5QZJ%2B0hYA0Qmv06d&X-Amz-Signature=b75dab0d25c9019e0b151b792d6436e1743a4c6cf4fe2cf8a7590d2c41415207&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

[image](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/f251872b-a493-4143-b77f-b8092f97e5e4/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46675HGFQWW%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T225349Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDd5HL1OcvgrhpSFOjkbkXDiiGZzDAUdrSXuLgw0i2GswIhALN5DT3lWeVrr8PZFB9QFqSBqEZVUUH0OM3ni4%2F02ZGvKogECMb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgwjVMCAyM4aDlyiDtkq3AMf7mkxnCMOEUQQ8g0kZfDZLE7D6ryQ0H%2F9vJfipSWgOagWHLfZ4i%2BLhzov2g7fqaN49fSudK18ABlrur5nBTGsyNxc5BzzzgP2SJaWMWuWmuU7PmSjBzFD1K7TQP97XSTChhObnFHiG0hgvHHRVe8uT3MFMy9J%2BReluoMc13zoqyEgNMXYuD2uXB%2Fe3eCzIGYtkZpK9uN9PlVtMtZLt%2BDdfmvm4YH7bpFXJihxeBeK3LP2y6hDy66HUsHV6hJqKfcffeI%2BLt%2BoQpmxv980LYlTDz3pGo9jfmaEy7iaI0BckjLx4qtv5%2BQIPIWYG979S9oEkMVBXFW%2BStcLMicuwAHdM0id4gKOXuzv7Si%2F3IGbbr%2F7QiRXQklPly9Ooi7%2BxwhKoEhLsk1NVPxFgQi7rPinT2Mv%2BA8xi%2FiQZ8bV70JRs7fdsGDF%2FcEIAo9c0e8riAXDk6dw6kBs%2F7Qo%2Fg%2FEdBo%2BmP66r8pv0jiVE%2BnMmL%2B3z5PS7bxj%2BtYjZ2BWcly8GqAkcMQeN5Snj6j3RnkQAfpFNuCky70rtmhaIyt0LK8LuUfbXiitRQHm2RPfdRKByR%2BCMolPVDZDAjXE0w%2FOQbwC6SuiDKHXo%2FHNS%2BrgdLt32p92EuSrtgsjGIJH6DC0uP%2FSBjqkAeLS2jNoAmVm2%2FAk1Il1B879pWttmXpMkoKl7OQ1a%2BBsdkTbKlXan69bSltaaz4fMNUy%2FyVp8caFFgtPIYHeFl%2ByvwxJTZtUWHR0HHfPrwwVK7x%2FF1f8lfgA8UsuGqaLlPpzE7cIDTUf7fT8%2FTHe9lkRuViv9D0VKHrYn0uAgAH7jngraJYF7IMeDmfKEnjW%2FDo%2FdNQcjZfz5QZJ%2B0hYA0Qmv06d&X-Amz-Signature=f74acaa45579d7d8d7d52045a7d6095198b033fa681bb208ce76043c844c1404&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

在上一节当中，咱们学习了主 keeper 分布式锁的原理，现在咱们要根据这个原理去实现咱们的程序。咱们还是打开 idea 这个项目是咱们使用 Redis 作为这个分布式锁时创建的这个项目。使用组 keeper 咱们再新创建一个项目，也是使用 spring boot 去创建。点击下一步名字，咱们改一下叫做 distribute ZK lock 组 keeper 的分布式锁。然后咱们点击下一步，在这里边选择一些常用的一代的价包，咱们还是选择 long book 然后 web starter 先选中，其他的咱们暂时就可以先不选了，等用到的


时候咱们再手工的去添加，然后点击下一步完成。在当前这个窗口打开刷新一下 Maven 这个项目就搭建成功了。咱们看一下这个结构。这里边咱们在创建两个目录，一个是这个 lock 目录，一会咱们这个组 keeper 分布式锁的实现，就在这个目录下去完成，然后再写一个 controller 这个目录咱们模拟一下这个请求对吧。请说了好，目录建好以后，咱们需要引入这个 ZK 的价包，因为咱们要连接组keeper ，但是这里边并没有 ZK 的依赖，所以咱们要把这个价包给它添加到这个 home 文件当中。
咱们还是打开这个浏览器，然后进入到 mvn reposity 对吧，搜索一下组 keeper 第一个就是组 keeper 咱们点进去往下滑动，找到三点四点一四。因为咱们这个本机安装的组 keeper 的版本是三点四点一四对吧，所以咱们也选择同样版本的这个客户端点击，然后把下边的这一段依赖复制一下，粘贴到咱们的 home 文件当中。


这块咱们要注意一下，大家看到这块它的 type 是 pom 它并没有把这个价包下载下来，而是把这个 pom 文件给下载下来了。所以这块咱们要把这 type 这个类型给它删掉，然后刷新一下 Maven 咱们检查一下，看看这个组 keeper 的假包是否已经在咱们的项目当中了。
咱们看左侧项目这一块有一个外部包是吧，点开看看有没有组 keeper org 是吧。好，可以看到 zucuva 的价包已经引入到咱们的项目当中了，咱们可以放心的去使用了。然后咱们就要编写这个组 keeper 的分布式锁了对吧，咱们在这个 lock 目录下创建一个 ZK lock 是吧。 ZK lock 这块咱们要仿照上一节课的内容，就是基于 Redis 编写的这个分布式锁。咱们这个类的结构和那个 Redis 锁的结构是一样的，也是要实现自动关闭这么一个接口。


另外还有一个接口是非常非常重要的，就是这个 watcher 观察器咱们看看。第一个就是这个接口后面看它的包名祖 keeper 里边的 watcher 这个接口选中这个位要实现这两个接口，咱们先把方法生成一下，没有问题是吧，这两个方法咱们留在最后再写，先把前面的一些基础的功能给它写好。
首先咱们要写一个构造函数，这个构造函数干什么用呢？勾的函数要连接这个组 keeper 对吧。所以咱们这个类里边还要有一个组 keeper 的变量组 keeper 第一个是吧组 keeper 包下的组 keeper 它就是连接咱们组 Q2 服务用。然后在这个构造方法当中，咱们去实例化这个对象 this 点主 keeper 等于 new zookeeper 是吧，他的这个构造方法里边都传哪些内容呢？咱们点进去看一下看看。



有四个构造方法，咱们就用第一个就可以了。第一个构造方法它有三个参数都是干什么用的咱们也不清楚，咱们点进去看一下它的注释看看。这个就是三个参数的构造方法，可以通过它的这个参数猜出它的含义。第一个， connect string 连接组 keeper 的字符串，这个无非也就是 IP 加上端口对吧。然后 session time out 绘画超时的这么一个时间，咱们可以看到前面这块已经有注释了 session time out in milo second 它的单位是毫秒对吧？然后 watch 观察器看看这块有注释，当你的这个节点的状态改变的时候，你要通知这个 watch 所以这块咱们也要传一个 watcher 这个 watcher 一般都是自己的这个类，把自己的这个类传进去就可以了是吧，因为自己的这个类已经实现了 water 这个接口了对吧。


再看看 connect string connect string 可以看到它是一个逗号分隔的 IP 加端口的这么一个字符串是吧，下面也有例子，这个咱们就不用多说了，这块咱们怎么写？ to keeper 咱们连接本机的 to keeper 对吧，local host 2181。第二个参数，超时的时间咱们设置为 10 秒。就是一万是吧，1万毫秒。


最后一个参数， watcher watcher 因为咱们这个类本身已经实现了 watcher 这个接口，所以咱们把自己传进去就可以了是吧。 this 好看看这块还有红线是吧，它会抛出异常，咱们也是在这块直接把异常给它抛出。然后咱们要写这个获取锁的这个方法，咱们同样也是写一个方法 public 然后 or 这个方法名称也叫做 get lock 是吧。


lock 这块咱们要不要加参数，咱们加一个参数，这个参数也是 business 叫做 business code 业务代码是吧，因为你不同的业务你这个锁是要区分开的。咱们在组 keep 当中创建节点，这个节点咱们也要分不同的目录是吧，通过这个业务节点把不同的目录给它区分开。比如说你在创建订单的时候要用到这个分布式锁，我都给它放到 order 这个节点下，在这个节点下我创建一些瞬时的有序的节点去代表着它的锁。比如说我要在创建商品的时候可能也用到分布式锁。那么我要创建一个 products 节点，在这个节点下，这些锁的这些瞬时节点都代表着商品这个服务的锁。所以这块咱们传入一个 business code 这个节点，咱们要判断它在组 paper 当中是不是。如果不存在，咱们要创建一个这样的节点对吧，现在咱们就要写这个逻辑，咱们看看怎么去判断这个节点。


组 keeper 点有一个 exit 这么一个方法，大家可以看看这个方法有两个参数，第一个参数就是你这个节点的路径，咱们把路径传进去。然后第二个参数是否观察这个节点是吧，是否给这个节点添加观察器。咱们还记得前面的内容吗？有三个方法是可以添加这个观察器的，一个是 exit 方法，一个是 get day 的方法，还有一个是 get children 方法。在这里咱们使用了 access 方法， access 方法它是可以添加监听器的是吧，但是咱们现在用不用添加这个监听器，是吧，不需要咱们这个第二个参数就传 false 就可以了。


前面咱们要把这个节点的路径给它写上，节点都是以这个杠去开头的是吧，咱们要判断这个节点存在，不存在第二个参数传一个 false 我不需要监听看看这块也是报错了是吧，下个踹开是吧。开始一个 exception 后边的咱们都不需要，然后 return 一个 force 这块，咱们节点前面要用变量接一下是吧。然后如果这个节点不存在，组 keeper 去创建这个节点，create创建这个 business code 这个节点对吧，咱们看看这个 create 方法。 create 方法也有两个，咱们也是使用第一个方法就可以了。第一个方法需要传入四个参数对吧，咱们


点进去，看一下它的前面的注释。第一个 pass pass 这个变量就是说你创建节点的这个路径。
第二个参数 date date 是你这个节点所存储的内容是吧，你初始化的一些数据。第三个， ACL node 这个是一个组 keeper 的权限这块咱们暂时先不用考虑，传的时候，咱们传这公开的这个权限就可以了。最后，创建的模式可以选择瞬时节点，还可以选择持久节点。这个咱们一会再看一下，再回到这 CK log 这个类里边来。


第一个参数，pass这个节点传完了是吧。第二个参数咱们要传初始化的数据，初始化的数据其实咱们也用不到是吧，但是咱们给他传一个，这个比斯尼的扣子给他传进去。第二 get a bat 第三个参数是这个 ACL 咱们就固定的传这个 ID S 看看。第一个， zukira 包下的 I DS 点讲什么？看看咱们要传入这个 open ACL unsafe 就是这个不需要使用账户密码就可以连接组 people 的这个方法就传入它就可以了。最后你创建这个节点的模式是什么样？咱们看看有什么模式 create mode 是吧。然后点看看里边它有四种模式是吧。第一种瞬时，然后瞬时有序。第三个是持久。第四个是持久有序是吧。咱们创建业务的这个节点其实和你后边的这个锁还没有关系是吧。创建这个业务节点只不过是区分你不同业务的锁放在哪个目录下，所以这块咱们创建这个持久节点，创建这个持久节点。好这样，这个持久节点，也就是说这个 easy 的 code 咱们已经。




