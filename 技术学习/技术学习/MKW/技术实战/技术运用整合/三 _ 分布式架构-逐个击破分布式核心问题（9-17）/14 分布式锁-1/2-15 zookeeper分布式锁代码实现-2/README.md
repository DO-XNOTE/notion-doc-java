---
title: 2-15 zookeeper分布式锁代码实现-2
---

# 2-15 zookeeper分布式锁代码实现-2

[image](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/3539e9d1-8925-43c3-80b7-f1b504fd99d6/SCR-20240807-kdav.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46637H5HKXL%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T225350Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQD47ln5nbSdWRae1CnxdR4FOH1m0Y6w10PecERh%2FI7DEwIgBsCXB19PSgxEBBzGe%2BbYIEKstKDlu7ftapQzoUnAQT0qiAQIxv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDAjb3uThtvjQ7GE9jSrcAwbIb%2BuutDPiciNPwxcES59KhjAKBskIotFRSRar6Itmz8Czoea126FsS8NamZYFcds6dk5xoHw8SXs490GzLCafmDKllTfdEwORqeCzYJbZ2IIx5zG%2FbtOeBucNHP6Y%2FS3B3WB958D5gjnS9d02IFkz5SI4QGYS2Rw2PMKSiTKTsKSN%2B7b73TRzsB3JqFoHkhZn1oNf1rqGpSmUlAYCCPz10iW%2BOpQ%2FAvY%2FNAfZCdxDrhYpnKqVMQqBTf2VmPZOMy%2F7hfZs6jjAwOc%2ByD8XMIWMxy2qZ%2F3ppn%2FrHJUwbhBoyMiF7kWpJTqdaAT7N9JC8qsaCttuIx2FurhU%2FFrv941eRKDRyyxaKNHWwLgQLpqwrws%2FPDLdyjIiL1DR8ZAdcKuWLbPqJs9wuQE3KmBQvp%2FIw4tQsm%2FW7buvaK5fK7m%2Be52LTlXbFaAv%2FbFr6EEr6eF58m%2BA0TAoQsV8CGvPnJi9Zg2xnyb0w9xS6iW0hIDYcSemTLTU%2FY0X29cOotoEkJ2I4k%2BGm9Tf0EfwwcBSTGj8aZ5MGsfYBCP2bey6wEdLbBIngjA29Dgx6paWF8wi%2FgCa87g9B3yY%2F%2FN%2B7PRwmcXnhDQThBxQb%2BwrLUFhCzeXX3y4reCnah6jfgabMLG3%2F9IGOqUBI9ED8HiIOBt5X7zfJorHQMzmRFAl1OoTd%2BNFXe8h7DrN%2FXqOTxNUXgWBjLlw%2FdbHjbuodOi2ZZj7kEgMxNBAw0HZ%2BONAiYmwO1xEgaPyrxUm6Rhy2nz6L40CxrXw3k%2FchcuBPy3gS8jsZ88pseKAJrvryVNri3l6M384H%2Fu%2BfBQM9tvgidOfJOns24sIrFWdYeijaDbJcfHY%2BKeU2fW1QyFF84TP&X-Amz-Signature=e23b2ed28279d2b04a6df361643b93f4e6700928df9ecfa6a2d034643b8d6c98&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

[image](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/1db31415-665e-4cbf-8a90-538e581f9410/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46637H5HKXL%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T225350Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQD47ln5nbSdWRae1CnxdR4FOH1m0Y6w10PecERh%2FI7DEwIgBsCXB19PSgxEBBzGe%2BbYIEKstKDlu7ftapQzoUnAQT0qiAQIxv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDAjb3uThtvjQ7GE9jSrcAwbIb%2BuutDPiciNPwxcES59KhjAKBskIotFRSRar6Itmz8Czoea126FsS8NamZYFcds6dk5xoHw8SXs490GzLCafmDKllTfdEwORqeCzYJbZ2IIx5zG%2FbtOeBucNHP6Y%2FS3B3WB958D5gjnS9d02IFkz5SI4QGYS2Rw2PMKSiTKTsKSN%2B7b73TRzsB3JqFoHkhZn1oNf1rqGpSmUlAYCCPz10iW%2BOpQ%2FAvY%2FNAfZCdxDrhYpnKqVMQqBTf2VmPZOMy%2F7hfZs6jjAwOc%2ByD8XMIWMxy2qZ%2F3ppn%2FrHJUwbhBoyMiF7kWpJTqdaAT7N9JC8qsaCttuIx2FurhU%2FFrv941eRKDRyyxaKNHWwLgQLpqwrws%2FPDLdyjIiL1DR8ZAdcKuWLbPqJs9wuQE3KmBQvp%2FIw4tQsm%2FW7buvaK5fK7m%2Be52LTlXbFaAv%2FbFr6EEr6eF58m%2BA0TAoQsV8CGvPnJi9Zg2xnyb0w9xS6iW0hIDYcSemTLTU%2FY0X29cOotoEkJ2I4k%2BGm9Tf0EfwwcBSTGj8aZ5MGsfYBCP2bey6wEdLbBIngjA29Dgx6paWF8wi%2FgCa87g9B3yY%2F%2FN%2B7PRwmcXnhDQThBxQb%2BwrLUFhCzeXX3y4reCnah6jfgabMLG3%2F9IGOqUBI9ED8HiIOBt5X7zfJorHQMzmRFAl1OoTd%2BNFXe8h7DrN%2FXqOTxNUXgWBjLlw%2FdbHjbuodOi2ZZj7kEgMxNBAw0HZ%2BONAiYmwO1xEgaPyrxUm6Rhy2nz6L40CxrXw3k%2FchcuBPy3gS8jsZ88pseKAJrvryVNri3l6M384H%2Fu%2BfBQM9tvgidOfJOns24sIrFWdYeijaDbJcfHY%2BKeU2fW1QyFF84TP&X-Amz-Signature=ffd7b01d1e4db07e315d5d500696d72dbd88745099fe9acb22df052412e7f236&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

下面咱们要创建这个瞬时有序的节点。这个节点是干什么用的呢？它是在你多线程共同创建的时候，我要进行排序的。排序完以后，我要找到序号最小的那一个节点，这个线程才能获得到锁。对吧，咱们前面这块加个注释，创建业务跟爷爷。下面的这个步骤是创建瞬时有序节点。


好，咱们继续要创建这个瞬时有序的节点，咱们也是把上面这一段给它复制过来。然后这块这个节点，咱们要再往下去写一层，再加一个 B 字信的 code 然后再加上一个下划线再举一个例子，比如说咱们这个 business code 咱们传一个 order 是吧，假设传一个 order 那么前面它的根节点就是 order 是吧，然后再创建它的瞬时有序节点，下边还会再有一个 order 是不是？咱们看看这个路径一个杠 order 后边又一个杠 order 最后还有一个下划线侠文言，后边跟的是什么呢？跟的是它的这个序号是吧，这个序号咱们就不用写了，它会根据你创建的这个模式有关系，咱们这个模式要改一下了，这块要创建瞬时的有序节点是吧，咱们选择这个就可以了。


瞬时有序节点创建完成以后，用变量给它接一下是吧，叫做 Z note 吧是吧，这个 Z no 的，咱们不光是在这一个方法当中使用是吧，还有后边咱们要删除这个节点的时候也是要使用这个 Z node 的。所以咱们要把这个 Z node 给它提升，提升成一个类变量是吧，我们在这给它写一下。 private 然后 string Z node 这块就是 Z node 这个节点。


那么咱们看一下，如果你的这个线程是吧，是第一个创建节点的，那它可能得到的序列号就是001。那么这个时候 Z note 就等于上面的这一段杠 order 杠 order 001，咱们接着就要判断了是吧，判断你的这个 Z no 的是不是序号最小的那一个。那么怎么办？咱们要把这个 order 目录下所有的节点都给它拿出来，然后再去比较。那么咱们怎么去拿这个 order 节点下所有的这个瞬时节点呢？咱们看一下这块也有一个方法组 keeper 点，然后改 at children 是吧，获取它的子节点看看。也是有两个参数，一个是这个 pass 你的节点的路径。


另外一个是否设置这个观察器，在这一步当中，咱们也是不需要设置这个观察器的。是吧，咱们要获取哪个节点的子节点呢？也是杠加上一字 code 然后是否添加观察器 false 不需要接一下是吧，都是秋砖 no children node 得到了这么一个子节点的序列是吧。然后咱们要把这个序列给它排一下序 collections 对吧，点 salt 这样咱们就得到了一个升序的这么一个队列。如果这个队列当中的第一个等于咱们的创建的这个节点，那么就说明他获得到了锁，咱们把这个第一个给他取出来。
get 0 叫做 first node 如果你创建的这个节点点 equals 等于 first node 这个时候呢 return 一个 true 对吧，咱们看一下，你的 Z node 是什么样？你的 Z node 是这个字符串是吧？然后你 get children 在丘阵里边得到的字符串是什么样的？很显然不是这样的，它是后边的这一段，所以这块咱们判断是不能这么判断的。这块判断应该是 Z no 的点 end with 是吧。以你第一个节点的这个字符串为结尾的，等于是我获得到了这个锁。这块比较绕，咱们把注释给它补全。


这块是创建瞬时节点是吧，然后获取业务节点下所有的子节点。这个子节点排序在后边，获取序号最小的那个子节点，也就是说是第一个子节点。如果创建的节点是第一个子节点，则获得锁对吧未喷出。那么如果你的这个节点不是第一个节点怎么办？你的这个线程要去监听你前一个节点。如果前一个节点消失了，然后你的这个节点要唤起对吧，要得到这个通知，然后再继续的去执行你后边的程序是吧。这块咱们给大家再写一下加个注释。不是第一个子节点，则监听前一个节点是吧。这块咱们怎么写？咱们要先定义一下这个前一个节点是吧。定义一个 last last node 最一开始就是第一个节点对吧，前一个节点就等于第一个节点，然后咱们在后循环修正 node 要循环你获得的这些子节点同样也是。如果你创建的这个节点等于子节点等于循环到你的这个子节点是吧。比如说现在你的这个线程创建的节点是002，002怎么办？你要去监听前一个节点是吧，你要监听 001 这个节点。现在前一个节点是 001 了对吧？如果你现在这个节点等于 002 是吧，咱们要循环，要以这个节点为结尾。
如果你等于了这个 002 是吧，所以我要去监听这个 last node 对吧，这个时候咱们怎么去监听？要用到这个监听器了。组 keeper.exit 是吧，监听哪一个节点杠，然后加上 isnt code 再加上杠后边就是这个 last node 是吧，监听这个节点是不是存在对吧？然后选择一个 true 我要判断这个节点存在不存在，并且给它一个监听器。如果这个节点消失了，那么我这个监听器将会得到通知。


咱们再看 else 如果你的这个节点不等于它，那咱们这个 last node 就要变了是吧？ last node 等于 node 这块逻辑比较绕。咱们再看一下。假如说这个子节点有三个分别是010203。那么第一个线程如果它是01，那么它获得到锁是吧，这块直接属于存储就返回了。那么比如说你当前这个线程创建的是 02 这个节点，那么怎么办？咱们要先定义一个 last node 就是前一个节点，现在前一个节点等于 01 是吧。然后咱们再循环循环里边的这个子节点，按照顺序去取出。第一个节点是01，你的 Z node 你是第二个线程对吧？你的 Z node 是02，02肯定不等于 01 是吧。然后咱们进入到了 else 那么 last note 还是 01 是吧？其实和这个第一句是一样的。然后循环第二次，第二次取得的节点是02，然后你创建的这个节点也是 02 是吧。那么咱们要设置一个监听器了，你要监听前一个节点。前一个节点是几呢？是01，你要监听 01 这个节点。那比如说第三个线程循环到 02 是吧，02也不是它的这个线程创建的这个节点，所以他再继续走到 L4 里边来。那么这个时候 last note 就等于 02 了。然后循环第三次，你当前的这个线程，03等于创建的这个节点03。所以你要监听 02 是吧，因为 last note 现在已经是 02 了，所以写在这里边这样也是没有问题的。


这个监听器创建好以后，咱们要使这个线程给它等待是吧。要用 wait 这个 wait 这个方法，咱们使用的时候一定要加上这把锁是吧。 center nice 的 this 然后再去 wait 这块是 Java 里边固定的这种写法，咱们要想一想为什么这个 wait 要加上这把锁呢？这块咱们是怎么考虑的呢？等待的时候等于是把你的线程这个锁就给释放掉，等于你的这个线程是没有锁的。那么如果我们并发的去执行的时候，你的这一个对象它被多个线程同时调用。那么这个把锁到底是怎么释放只能一个线程去等待。所以等待就是说释放了这个对象的锁你同时去释放，那它的这个锁它是混乱的这么一个状态。所以这块要加上一个 session nice 的就一直在这等待，等待你的这个节点发生变化，变化以后我得到通知再去唤起这个线程，唤起完以后就等于是他获得了锁。


这块就 return 一个数是不是？咱们再看看设置监听器的这个地方，如果你当前的这个节点是节点，第二个节点设置了这个监听器。设置监听器以后，咱们这块就直接 break 跳出了这个循环，然后这块我就 wait 了，我这县城就不执行了，一直在这等待，等待着前面的一个节点消失，然后唤起我这个线程这块怎么做？咱们就要在这个 process 方法里边去写了。因为咱们这一块设置了这个监听器对吧，如果你的这个节点消失了，消失以后就会进入到这个方法当中。
event.get type 你的这个事件的类型等于 event type.node deleted 是吧，这有一个节点删除是吧，咱们就监听这个方法。如果你的这个事件是节点删除的这个事件，我要唤起这个线程是吧。唤起线程用什么 notify 同样 notify 也要去加上一个锁，这个也是固定的写法，它会唤起你前边等待的这个线程。唤起以后它是不是就继续执行了？对吧，这个就是一个整个的获取锁的这么一个过程，然后这个释放锁就非常的简单了，就直接的去删除这个节点对吧。


组 keeper.delete 比例的方法有两个参数，一个是你节点的这个路径，然后后边还有一个 version 是吧，这个 version 是干什么用的呢？咱们点进去看一下。第一个节点的路径是吧。第二个参数， version 是你期望删除的这个节点的版本号，对吧，他是怕你删错了是吧，咱们前面没有获取到这个 version 再往上，看看它的这个注释。 delete the node with the event pass 删除。你给定了这个路径 this call 是吧，这个命令会成功。


如果这个节点存在，并且给的版本号匹配你节点的这个版本号，再看看后边的这个括号里边如果给定的版本是负1，它将匹配所有的这个版本是吧，那咱们这块就直接传负 1 就好了，因为前面咱们也没有记录这个节点的版本号，那么这块咱们删除什么呢？ Z node 然后传入一个负1，然后怎么办？咱们 ZK 还要 close 一下，关闭咱们这块，也是把这个日志给它打出来。 close 里边咱们加个日志 log.infer 我已经释放了锁是吧。好，这个主 keeper 的这个分布式锁咱们就写完了。写完了咱们先写一个测试程序，写一个测试程序咱们验证一下，写一个 test public void test ZK lock 然后里边写咱们的这个 ZK 的方法是吧。 ZK lock 等于 new ZK lock 这块异常咱们直接给它抛出。然后 ZK lock 点儿 get lock 里边儿传入参数，咱们传一个 order 获取锁以后，然后释放锁 close 这块异常咱们直接改一下，这边咱们也是再打一个日志，前面用变量给它接一下，因为咱们这块是返回了一个布尔型是吧 log 点儿 infer 获得锁的结果。


lock 咱们先检查一下，看看 ZK 咱们现在已经启动了，然后咱们运行一下失败了是吧，咱们看看报什么？错 node 已经存在了是吧。 keeper error code 咱们看看 27 行是吧这块是吧，咱写错了应该是，节点不存在。咱们创建这个新的节点是不是好，修改好以后咱们再运行一下这个程序已经测试成功了是吧，咱们看看最后一个获得锁成功，然后释放锁也已经成功了，没有问题，看来咱们这个获取锁是没有问题的。


下面咱们再写一个 ctrl 的创建一个 zookeeper controller 打上一个 rest 是吧，里边创建一个方法 public 然后 string zookeeper lock 我们也是加上日志，然后 log.infer 我进入了方法是吧。然后后边咱们要使用这个 JDK 1.7 的这个新的写法踹，然后后边跟上你的 ZK lock 等于 new ZK lock 这块，如果有异常，咱们 catch 是吧。


ck.get lock 传入 business code 传入一个 order 是吧。 if 如果获得到锁，然后咱们再去执行。执行执行其他的方法这块，咱们就使用休眠。线程休眠 15 秒，模拟一下其他的业务的执行是吧。随后释放锁咱们就不用去写了，因为咱们使用了这个新的写法，它会自动调用 close 方法，最后再写一个方法，执行完成是吧。返回去，咱们这个方法还缺一个，缺一个 request mapping request mapping 然后 ZK lock 对吧，再启动一下。好，然后打开浏览器 local host 8080，然后杠 2 ZK lock 是吧。
汽车咱们看看后台执行。第一个进入到了方法，然后释放锁，方法执行完成。咱们这个获取锁没打日志是吧，咱们补上。这块咱们再补上一个，我获得了锁，重新的启动一下再访问一下看看后台的日志进入到了方法，然后获得了锁是吧，等待 10 秒释放锁，方法执行完成没有问题是吧。然后咱们再起一个服务。另外的这个服务是 808e 端口，咱们直接复制，改一下名字杠 808e 这块再加一个参数 server.pot 等于8081。 OK 咱们再起一个服务。一会儿咱们两个请求，一个请求访问8080。一个请求访问8081，看看它能不能在这块给它锁住，是不是 8081 也已经启动完成了，咱们把日志都清一下进入到浏览器，一个是8080。另外一个访问808，咱们先敲这个8081，先访问8081，然后再访问8080，看看后台的日志。第一个 8081 进入到了方法，获得到了锁，再看看 080 是吧，现在也获得到了锁，等待 10 秒以后释放锁方法完成。咱们看一下两个时间。 52 分 40 秒，8081这个服务进入到了方法是吧，也是 52 分 40 秒，他获得到了锁。 12 分 50 秒的时候他释放了锁是吧，咱们再看看 8080 这个服务。 8080 这个服务 52 分 40 秒 42 秒进入到了方法是吧，但是他获得锁是在 52 分 50 秒这个 50 秒是什么意思呢？是因为前面 8081 这个服务是在 50 秒释放的锁是吧？ 52 分 50 秒，8081这个服务释放了锁，然后 8080 这个服务在 50 秒的时候获得到了锁，然后再去执行释放锁方法完成没有问题是吧，等于是把你所有的这个线程都给你排队了。


那么这个使用组 keeper 实现这个分布式锁咱们也已经完成了，咱们来快速的回顾一下。其实最主要的还是这个 ZK lock 这个类咱们要多看一下。首先这个 ZK lock 要实现 water 是吧，这 water 就是监听器，你必须要实现它，你才能得到这个主 keeper 服务给你的通知，然后再去实现这个 auto close able ，这个接口就是自动关闭，咱们可以使用 gdk 1.7 的这个新的写法。然后那里边的内容组 keeper 这个是连接的里边的参数，一个连接串是吧，你连接主题板的地址和端口，绘画超时的时间。然后这个 water water 传什么？传的是 this 因为你当前的这个类已经实现了 watcher 接口是吧，所以你当前这个类也是一个 watcher 直接把这个 Z 字传过来。然后 get lock 这个是非常重点的一个方法了，咱们再捋一遍。


首先要去创建这个业务的根节点，你传 order 咱们要创建一个 order 你要传 product 咱们要创建一个 product 这个根节点，它的类型是持久类型。为什么要创建一个持久类型呢？也就是说你这个主题本挂了，或者你的这个服务重启了你的这个节点还是存在的，它只是区分不同的业务和你获得锁这一块是没有关系的对吧？然后创建瞬时节点，这个和锁就有关系了。这块创建 business in the code 下边再加上一个 business code 再加一个下划线，然后里边是一个瞬时有序的节点。然后你创建好以后，你的节点就应该是这个样子，order它是根节点是前面这一部分给创建的。后边这一部分就是这个 create 创建的。当你多个线程并发执行的时候，它的创建的节点并不会相同。比如你有十个线程同时的去执行这一个方法。那你得到的这个瞬时节点也是 10 个是吧，序号也是从一开始一直到是。然后咱们再获取业务节点下边所有的子节点。如果你现在有 10 个线程同时执行，你的这个子节点有 10 个，那么我获得这个子节点就是 10 个，然后咱们给她从小到大的去排序。如果你当前的这个线程获得的是第一个节点，那么判断你的这个 Z node 和后边的这一段是相同的。那么我就判断你是第一个子节点了，你的这个线程将获得这把锁，那去执行后面的业务。


如果不是第一个子节点，那么我要监听前一个节点监听前一个节点怎么写，就是这么一块逻辑。这块逻辑大家课后要好好的去看一下，尤其是这个 last node 然后这块还有一个 if 的判断是吧，咱们监听前一个子节点怎么写，exit X 的前一个子节点，然后加上一个 watcher 等于 true 是不是？然后咱们线程就等待了，等待着前一个节点消失。


唤起我这个线程前一个节点消失，消失要给你发通知是吧，发通知在哪儿？就在这个 process 方法，它是实现 watch 这个接口的。咱们判断一下事件的类型等于节点删除。然后我们去唤起前面的这个 wait 唤起以后被唤起的这个线程将水尘处获得到锁，这个就是获取锁的这么一个整体的逻辑。业务执行完成以后，你要删除这个节点或者 delete 了 delete 方法以后，然后就会通知下一个线程，就是在这不停的去循环。然后你所有的线程其实一开始在创建节点的时候就已经排序好了，我就会按照这个顺序去一个一个的去执行。


这个就是组 keeper 实现分布式锁的一个整体的步骤。课后大家还要多多的练习，这个组 keeper 这个分布式锁好像要比 Redis 更难理解一点。但是我觉得大家课后多下功夫看一下，完全掌握他对自己能力的提升还是很有帮助的。好这一节课就先给大家介绍到这，谢谢大家。




