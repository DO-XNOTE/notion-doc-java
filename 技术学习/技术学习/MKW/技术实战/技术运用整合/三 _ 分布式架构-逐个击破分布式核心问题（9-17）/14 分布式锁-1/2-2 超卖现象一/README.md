---
title: 2-2 超卖现象一
---

# 2-2 超卖现象一

[image](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/7fe43707-d8c3-474d-876e-f5bf86f3d13d/SCR-20240807-isin.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666FSXQKMF%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T225339Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIEbzo6KPzIR9WqgRuB67gEk3WU3v2KmKd%2BzYmvg81riCAiAr931HVwFedgCN4On5%2F6clEfPcdd6punMJFI2sy%2FLEwCqIBAjG%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMf3JQX5GJhg9dbOCrKtwDUmrBEUJLWkdjUBKZQPQBijz8HCSjJESFfMINK8uqCSF9fVWV8VY5x0aTusfBo%2FT2wMII7wTTOb6Ouh%2FeDLbs14%2FYXj1XppcYzFSvTpkHjdubcfSXwJ6qlO35c9bRg7UY6bAhcIEP63EPGSO4t3tgJ86n532IHHi%2FlItlzVkkpVCQwDKDJM%2BDLFKAnNPg8yH0pZiu6vLaldSz%2FsTumDgDDeMRyJA%2FeNm6LjufHpNvTIVEyE0wm%2FyE8GJg91rQ6TTn9BJbR7EM4chrflSc2DFI3pwC9%2ByTsVBxpAFdhS%2F1dcSTSVtQDxMozsqpdz2bh6dXVqclvcbWu726xp16WTeT0J3Eko6VPp15LGAyESVFODlu72K9uBkpztksWaa%2FEd8Y58ixCiClzzBSVul%2FSKg3GjKXWSJZ7Hc8E7VB16XDtpVQfZYW%2BEVm0t5jQ5vP04A76oSTjMrH9ieJYn5tior4%2Fg8D2VdyU5YHDCPOH2DFAWhA78E0fFLhWtRmaQyK5je%2F%2FQ9UbRzy3u2XG%2BL9BefMTpxKNdXZZ0m%2Byzsix0CGgVKa8hwlO3hG1ZvJgPt4a%2F1AgGfWMIZt6gffvDVF44km5bvjpzrVZ7uyo6H29ZrgWd2NXlT69zhF7HcVfj0wt7j%2F0gY6pgFynhrac8OlrLxYn9%2B15wEET0LNcDv%2Bk1DzudJ%2FTF6Y8myugXu49dqrRTiCIwmrlH%2BBLbOfVjYEvi25zWkOBZ5Lf661p%2BiAEnpjbPI9RN%2FNvmgUpg6GX17WxepDwVc0aS1LO0YKW4OusMAEDD2FJWZ0BdQXh5XjwYWIcugYjvX2UMfpjoP0soM7CaRhrGJBMbxmupBNIH5inAOxWY2OgCYJu84%2Bk773&X-Amz-Signature=7f97710582345384cddb411ade4e2a4ac4db08182e5134c49ad8d27a333fc956&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

[image](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/e567ffaf-86f6-460a-8a12-30d5dcd78f46/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666FSXQKMF%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T225339Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIEbzo6KPzIR9WqgRuB67gEk3WU3v2KmKd%2BzYmvg81riCAiAr931HVwFedgCN4On5%2F6clEfPcdd6punMJFI2sy%2FLEwCqIBAjG%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMf3JQX5GJhg9dbOCrKtwDUmrBEUJLWkdjUBKZQPQBijz8HCSjJESFfMINK8uqCSF9fVWV8VY5x0aTusfBo%2FT2wMII7wTTOb6Ouh%2FeDLbs14%2FYXj1XppcYzFSvTpkHjdubcfSXwJ6qlO35c9bRg7UY6bAhcIEP63EPGSO4t3tgJ86n532IHHi%2FlItlzVkkpVCQwDKDJM%2BDLFKAnNPg8yH0pZiu6vLaldSz%2FsTumDgDDeMRyJA%2FeNm6LjufHpNvTIVEyE0wm%2FyE8GJg91rQ6TTn9BJbR7EM4chrflSc2DFI3pwC9%2ByTsVBxpAFdhS%2F1dcSTSVtQDxMozsqpdz2bh6dXVqclvcbWu726xp16WTeT0J3Eko6VPp15LGAyESVFODlu72K9uBkpztksWaa%2FEd8Y58ixCiClzzBSVul%2FSKg3GjKXWSJZ7Hc8E7VB16XDtpVQfZYW%2BEVm0t5jQ5vP04A76oSTjMrH9ieJYn5tior4%2Fg8D2VdyU5YHDCPOH2DFAWhA78E0fFLhWtRmaQyK5je%2F%2FQ9UbRzy3u2XG%2BL9BefMTpxKNdXZZ0m%2Byzsix0CGgVKa8hwlO3hG1ZvJgPt4a%2F1AgGfWMIZt6gffvDVF44km5bvjpzrVZ7uyo6H29ZrgWd2NXlT69zhF7HcVfj0wt7j%2F0gY6pgFynhrac8OlrLxYn9%2B15wEET0LNcDv%2Bk1DzudJ%2FTF6Y8myugXu49dqrRTiCIwmrlH%2BBLbOfVjYEvi25zWkOBZ5Lf661p%2BiAEnpjbPI9RN%2FNvmgUpg6GX17WxepDwVc0aS1LO0YKW4OusMAEDD2FJWZ0BdQXh5XjwYWIcugYjvX2UMfpjoP0soM7CaRhrGJBMbxmupBNIH5inAOxWY2OgCYJu84%2Bk773&X-Amz-Signature=889490d7364de431603a0253378953b125b4adb76449b3588f0ca18a96ee8172&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

[image](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/4424a75f-adc1-4e6c-a9ce-a995e9c4b210/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666FSXQKMF%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T225339Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIEbzo6KPzIR9WqgRuB67gEk3WU3v2KmKd%2BzYmvg81riCAiAr931HVwFedgCN4On5%2F6clEfPcdd6punMJFI2sy%2FLEwCqIBAjG%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMf3JQX5GJhg9dbOCrKtwDUmrBEUJLWkdjUBKZQPQBijz8HCSjJESFfMINK8uqCSF9fVWV8VY5x0aTusfBo%2FT2wMII7wTTOb6Ouh%2FeDLbs14%2FYXj1XppcYzFSvTpkHjdubcfSXwJ6qlO35c9bRg7UY6bAhcIEP63EPGSO4t3tgJ86n532IHHi%2FlItlzVkkpVCQwDKDJM%2BDLFKAnNPg8yH0pZiu6vLaldSz%2FsTumDgDDeMRyJA%2FeNm6LjufHpNvTIVEyE0wm%2FyE8GJg91rQ6TTn9BJbR7EM4chrflSc2DFI3pwC9%2ByTsVBxpAFdhS%2F1dcSTSVtQDxMozsqpdz2bh6dXVqclvcbWu726xp16WTeT0J3Eko6VPp15LGAyESVFODlu72K9uBkpztksWaa%2FEd8Y58ixCiClzzBSVul%2FSKg3GjKXWSJZ7Hc8E7VB16XDtpVQfZYW%2BEVm0t5jQ5vP04A76oSTjMrH9ieJYn5tior4%2Fg8D2VdyU5YHDCPOH2DFAWhA78E0fFLhWtRmaQyK5je%2F%2FQ9UbRzy3u2XG%2BL9BefMTpxKNdXZZ0m%2Byzsix0CGgVKa8hwlO3hG1ZvJgPt4a%2F1AgGfWMIZt6gffvDVF44km5bvjpzrVZ7uyo6H29ZrgWd2NXlT69zhF7HcVfj0wt7j%2F0gY6pgFynhrac8OlrLxYn9%2B15wEET0LNcDv%2Bk1DzudJ%2FTF6Y8myugXu49dqrRTiCIwmrlH%2BBLbOfVjYEvi25zWkOBZ5Lf661p%2BiAEnpjbPI9RN%2FNvmgUpg6GX17WxepDwVc0aS1LO0YKW4OusMAEDD2FJWZ0BdQXh5XjwYWIcugYjvX2UMfpjoP0soM7CaRhrGJBMbxmupBNIH5inAOxWY2OgCYJu84%2Bk773&X-Amz-Signature=df5c2c419045244713a9ee1dde5b32f51726b193f17a16edf771d920723a45ab&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)


hello，大家好，咱们接着前一节的内容，看看怎么去模拟并发下单的这个场景，并且使用 up day 的航锁去解决并发的问题。在具体看程序之前，咱们先看一下数据库里边都有哪些表。这个是在我之前设计好的几张表，咱们分别给大家看一看，因为咱们只是模拟这表设计，就是保证它的一些基本的字段就可以了。大家看一下有order，这个就是订单表， order item 就是你订单里购买的商品，对吧？都记录到这张表里边。
最后还有一张商品表，先看一下商品表里边的内容，商品表里首先有ID，对吧？商品的ID，然后商品的名称、价格数量，这个数量就是这个商品的库存，一会咱们模拟的时候会把这个字段给它设置成1，就只有一件商品，后边商品的描述。最后是 4 个比较基础的字段，创建时间创建人、更新时间更新人，这个就是商品这张表。


接下来咱们再看一下订单这张表，订单表ID，这个就是订单的ID，订单的状态，咱们这里边就只默认了一个 1 是待支付这种状态。然后边收货人姓名、收货人手机，其实还有很多其他的一些字段，比如收货人的省市区、详细地址、邮编，这些其实都属于收货人的地址，这些咱们只挑选两个比较基础的字段，在这给大家做一个演示就可以了。然后 order amount 订单的金额，后面是 4 个基础的字段，接下来再看一下奥德item，这张表也是有一个ID，然后有订单的ID，你购买的这个商品是属于哪一个订单的？然后商品的ID，你购买的是哪一个商品，你购买时的价格、购买的数量，这些都是比较基础的。后边 4 个基础的字段，创建人创建时间、更新人更新时间。好，这个表呢就给大家介绍到这。然后咱们在这个商品表当中创建了一个商品，它的 ID 是100100，名称测试商品金额是 5 块，库存数量只有一个。


接下来咱们看一下这个程序，这个环境搭建咱们就不给大家做介绍了，咱们直接看一下程序，在程序里边mode、d、 o 这些都是对应的数据库的表，这个就不给大家做过多的介绍了，然后 service 层里边咱们写了一个订单的服务，订单的服务里写了一个创建订单的这么一个方法，前面引入了 3 张表对应的Mapper、 order item Mapper 还有 product paper 这块购买商品的ID。咱们就是下边这个创建订单的这个方法，就是模拟一个下单的过程，这个购买商品的 ID 就是咱们数据库当中创建的那个商品100100，然后购买商品的数量是一，然后再看一下具体下单的过程。


在这个创建订单的这个方法上，咱们写了一个事物的注解，对吧？因为咱们要涉及到三张表的数据的修改，要确保所有的这些动作在一个事务当中，所以加了一个事物的注解，咱们看一下具体的过程，首先要检索出你购买的这个商品，就是这个100100，然后做了一个判断，如果商品等于空，就抛出一个异常，说你这个购买的商品不存在，然后获取到商品当前的库存。


接下来就是比较关键的步骤了，就是这一步校验库存，是吧？我们看一下这个判断，如果你购买商品的数量大于了当前的库存数，然后抛出一个异常，对吧？说商品仅剩了多少件无法购买，看一下这两个数量，前面的这个是你购买的数量，后边是你商品的库存的数量，购买数量大于库存数量就要抛出异常，如果小于或者等于这个库存数量，那就是可以购买的。


可以购买以后咱们要计算一下它的剩余的库存，就是用当前的库存数减去购买的数量，得到了剩余的库存，然后我们更新这个商品的库存，把这个 product 的这张表的这个 count 字段设置成剩余库存，然后更新时间，更新人。最后我们更新数据库这一块，整个的步骤就是在程序当中计算库存的数量。


库存更新完以后，我们呢去创建订单这块都是比较简单的 set 方法了，这块就不给大家做过多的介绍了。订单创建完以后，创建订单明细 order item 同样也是一些 set 方法。最后我们返回订单的ID，创建订单的方法写完了，咱们这块再写一个测试的用例，对吧？来模拟一下多线程并发的这个场景。


创建订单这块是写了一个这 unit 测试程序，把刚才的咱们写的这个 order service 给它注入进来，然后写了一个并发订单肯卡润的 order 这么一个方法。咱们具体看一下这个方法前边这两个 count on lash 和 Celic Barry，这个咱们先不管，咱们先看后边的程序，后边咱们创建了一个线程池，这个线程池里边有 5 个线程，然后我们复循环 5 次给这个线程值分配任务，咱们用 excuse 的方法在这里边去调用订单服务的创建订单方法，对吧？前面这个 await 先不管，然后最后执行完成。


接下来咱们再看一下这个赛迪克贝瑞是干什么用的？这块我们为什么要加这个赛迪克贝瑞？咱们想象一下，比如说你现在创建了一个线程池，线程池里边有 5 个线程，然后你现在是 for 循环，对吧？如果你不加这个赛迪克贝瑞，它负循环会顺序的执行，一遍、两遍、 3 遍，那么你创建订单的方法也是紧跟着一遍、两遍、三遍，可以说并没有达到一个并发的效果。


这块加一个赛迪克贝瑞是什么意思？就是让所有的县城都在这里等待，等到某一时刻同时去往下执行。咱们看一下这具体的用法，塞这个白瑞这里边构造方法咱们传了一个5，就是说会等 5 个线程都同时达到 await 这个方法的时候，然后 5 个线程同时去执行下边的这个创建订单的方法，这样保证了创建订单这个方法是并发执行的，然后再看一下后边还有创建了一个 b 锁，对吧？也是传了一个 5 进来，然后每个线程执行完以后都会扛得到减一对不对？然后在这块进行额外它等五个线程都执行完以后，再去进行后边的步骤。


这块为什么要这么做？其实它和咱们的具体业务是没有关系的，为什么要这么做？这块其实是和数据库的连接池有关系，如果你不加这个闭锁的话，你主线程结束完以后，你的这个数据库连接池就关闭了。关闭以后你所有的这些新开的这 5 个线程，它是获取不到数据库连接的，就没法用了。


所以这块咱们加了一个闭锁，等待 5 个线程执行完以后，这个主线程再去给它关闭，这个测试的程序就写好了，然后咱们再看一下数据，商品表里边咱们创建了一个商品，数量是一，对吧？仅有一个，咱们来看 order 表，报到表里也没有数据，对吧？然后这块咱们 5 个线程同时去执行创建订单的这个方法，看看会有什么效果，咱们运行一下，运行完成了，对吧？咱们这个日志也已经打印出来了，创建了 5 个订单，咱们看一下数据库里边的记录，这个是订单表，咱们刷新一下，产生了 5 个订单。然后咱们再看一下这个商品表，之前商品的库存数量是1，咱们再看一下，刷新一下变成了0，这样这个超卖的现象就产生了，只有一个库存的商品，结果我们产生了 5 个订单，这个就是超卖这个现象，那咱们怎么解决？它解决的思路就是减少库存的时候，咱们看一下程序创建订单，扣减库存这一块，咱们现在是在程序当中完成的。


咱们如果用 up day 的航锁要把这一块给它下沉到数据库当中去执行，那么这块儿我们怎么写？这块儿计算剩余库存的这个步骤咱们就不要了，包括这块儿 set 的方法咱们也不需要了，这里边更新库存，咱们要新写一个方法， update product count。


这里咱们是通过增量的方式去更新数据库的库存，增量是什么呢？增量就是你的这个购买的数量，所以第一个参数咱们传入购买的数量，第二个参数传入更新人，咱们就随便写了，最后再传入一个更新的时间 new date，是吧？好，咱们创建一下这个方法法，返回，返回Int，然后咱们在这个 XML 文件里边创建这个方法，写这个增量更新库存的这个方法。


update product，对吧？然后 set 库存数量等于当前的库存数量，减去增量这块咱们加个注解，购买数量，对吧？然后第二个注解是更新人 update user 时间， Updata Type，咱们再回到 XML 文件当中，减去当前的库存是前面的这个注解，购买商品数量，这是一个，咱们重点关注一下这个写法，这块就是增量扣减库存的这个写法。


update， set 这个库存数等于当前的库存数，减去增量，对吧？这个增量就是你购买的数量，是吧？然后 update user 等于 update user，这个就不用动了，咱们直接复制过来就行。然后where， ID 等于这个商品的ID，咱们再回到程序当中，这块咱们还要把商品的 ID 传进来，对吧？忘了传了，刚才，加一个参数，这块再加个注解ID。好，现在咱们这个方法就已经改造完成了，咱们再回顾一下，之前咱们扣减库存的方法是在程序当中进行的，在程序当中计算好剩余的库存，然后去更新你的数据库，这个时候在并发的情况下，就像咱们这例子当中 5 个线程同时去执行，同时检索出了商品，同时发现商品的库存是1。然后又进行了判断，发现自己都可以去进行购买，然后接着往下计算剩余的库存，都是用当前的库存减去购买的数量，当前的库存是1，对吧？然后减去购买的数量也是1，计算得出剩余的库存是0，然后五个线程都去更新数据库，这个时候就产生了五个订单，然后商品的库存数都被更新成了0。


改造完成以后，咱们扣减库存的方法已经移到了数据库当中，通过数据库的增量的方式，用 update 增量的方式去更新这个库存，这块用 count 减去购买的数量，在这里计算出剩余的库存数。那那么这个 update 的语句也可能 5 个线程同时的去执行，对吧？但是 update 有航锁， 5 个线程同时执行这条语义其实只有一个线程能够执行成功，另外的 4 个线程都需要排队等待，等待第一个线程执行完以后，然后再去争抢这个航锁，谁抢到了锁，然后再去执行更新。
好，咱们呢现在把数据库里边的数据给它改一下，这 5 个订单咱们就先给它删除掉， order item 里边的数据，咱们也给它清一下，再把商品的数量给它改成一，对吧。这个时候咱们再运行一下程序，程序都运行完成了，也产生了 5 个订单，看来咱们的并发并没有防住，咱们来看一下数据订单，看一下 5 个订单都已经产生了，再看一下商品的库存数，刷新一下变成了-4。


这块也是没有问题的，因为你在 update 的时候是一个线程的去执行，第一个线程执行完以后，它的库存的数量已经变成了0，然后还有四个线程要去执行，四个线程依次的去执行以后，这个数量就变成了- 1- 2- 3- 4，最后一个线程执行完以后就变成了-4。这个问题就是接下来要给大家讲解的超卖的第二种现象。好了，这一节的内容就先给大家介绍到这。




