---
title: 1-3 对象池Commons-Pool2实战2：编写一个带监控的数据库连接池
---

# 1-3 对象池Commons-Pool2实战2：编写一个带监控的数据库连接池

[image](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/3f155d9f-12ae-4b9c-a090-ff7f1b6ae19a/SCR-20240727-ukvf.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664ZDGJUGY%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T230108Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIAn64KqbFaeetkVtEYEN%2B5vPUxRjY9%2Bpahe3KbdihlT2AiArSJ4LUcVB6mbPUFvdR8BSAc1aUkyEN2pKs3EGJPMMSyqIBAjG%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMy2HlbmmMpkHgXZ4NKtwDEN7EhmejGE4WzFlTHV4vmButAbQSZTxUUW79D2bznOCXo2h4IjePG8PezuuCBTV%2Bhbp2LdkgV%2BbI37h9ckXoUAqKOxJpsme%2B6V3x382Q2OIN%2B6HI%2B9VWP9VPIrDryZzY2Cot6RJzagfgCo1yUn4f9WfRKGhZNleJcFf3IYoSNAbI6nFbcn9Kzv04DN8Ih3ZA%2FLNiQnG2HZflIlZkkIsQrIyF5k2JAGmnTal5sfmj8koI46c%2B%2FpEv9RErrsXCubCbjTGTF6ApbkEwX79MuJG8o7jbCKXACgka2RGb9patM4BsUtwI4GukuQk0d2uSouU8PF4QZ4Rxl%2Bq%2Bd2Q784vy5FXB2oTSD0syDf5dWnFP7KkqCPrN3MHJOE9b2YyvcUW4BzZmFe160vMZouJ7wlRH%2Fkj0YKr3hF710r6WKYW7KnAduc3YRnCSbzqHqmpTibB9YPyd0ugM5w3lPaWi%2F6HXJ3RcfYAJiMEordP3tsPa3aKvbgEhw%2Bu%2B7MQAOatbznxiLFNjKB1NgV4AYmV8nu8MIcCueA0ii9CuLAh0axmfdbxhBddrJQZ3Kur3kqfCJmRxnsxdtwhDef5NYGCsx%2Fzp7%2B33awoLCb8Vv2Ocoo2vq177he9W9OYnyTr%2FR6cwt7j%2F0gY6pgHpRpCGgCj03de206N5W5dX%2FJbQzsSUH27%2FcNTeFJ3kva1JKj8Fix6t9QNjUo1Zvn4eJ4%2BowfRK%2Fh9m0naeELFJv%2BZbgqVQcEn99DQeMInzDWlfJhNquYbHY4Qa%2F45Le1%2FmN4nM%2F4DhFpgqpsUTEukgYKvOjcl3zqlK4ftWHeh8H87G19fZmd0lVhI9FWswUs0XSmvDkmH%2BEulkP6Un91WulpyWhZMX&X-Amz-Signature=50c3f3d46d411a510fd19041a278c069cfe196add052f4c7c577eb64cff639a0&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

[image](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/d5cfa43d-c386-48fc-be9f-72dd78f82b0d/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664ZDGJUGY%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T230108Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIAn64KqbFaeetkVtEYEN%2B5vPUxRjY9%2Bpahe3KbdihlT2AiArSJ4LUcVB6mbPUFvdR8BSAc1aUkyEN2pKs3EGJPMMSyqIBAjG%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMy2HlbmmMpkHgXZ4NKtwDEN7EhmejGE4WzFlTHV4vmButAbQSZTxUUW79D2bznOCXo2h4IjePG8PezuuCBTV%2Bhbp2LdkgV%2BbI37h9ckXoUAqKOxJpsme%2B6V3x382Q2OIN%2B6HI%2B9VWP9VPIrDryZzY2Cot6RJzagfgCo1yUn4f9WfRKGhZNleJcFf3IYoSNAbI6nFbcn9Kzv04DN8Ih3ZA%2FLNiQnG2HZflIlZkkIsQrIyF5k2JAGmnTal5sfmj8koI46c%2B%2FpEv9RErrsXCubCbjTGTF6ApbkEwX79MuJG8o7jbCKXACgka2RGb9patM4BsUtwI4GukuQk0d2uSouU8PF4QZ4Rxl%2Bq%2Bd2Q784vy5FXB2oTSD0syDf5dWnFP7KkqCPrN3MHJOE9b2YyvcUW4BzZmFe160vMZouJ7wlRH%2Fkj0YKr3hF710r6WKYW7KnAduc3YRnCSbzqHqmpTibB9YPyd0ugM5w3lPaWi%2F6HXJ3RcfYAJiMEordP3tsPa3aKvbgEhw%2Bu%2B7MQAOatbznxiLFNjKB1NgV4AYmV8nu8MIcCueA0ii9CuLAh0axmfdbxhBddrJQZ3Kur3kqfCJmRxnsxdtwhDef5NYGCsx%2Fzp7%2B33awoLCb8Vv2Ocoo2vq177he9W9OYnyTr%2FR6cwt7j%2F0gY6pgHpRpCGgCj03de206N5W5dX%2FJbQzsSUH27%2FcNTeFJ3kva1JKj8Fix6t9QNjUo1Zvn4eJ4%2BowfRK%2Fh9m0naeELFJv%2BZbgqVQcEn99DQeMInzDWlfJhNquYbHY4Qa%2F45Le1%2FmN4nM%2F4DhFpgqpsUTEukgYKvOjcl3zqlK4ftWHeh8H87G19fZmd0lVhI9FWswUs0XSmvDkmH%2BEulkP6Un91WulpyWhZMX&X-Amz-Signature=70338ae85d2b1b77e2524b3e365e3c393dcbab6be31c6605f256b4d9800c7a46&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

[image](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/6967ab5a-bb7b-4455-be2c-e8f1f6e8d8eb/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664ZDGJUGY%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T230108Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIAn64KqbFaeetkVtEYEN%2B5vPUxRjY9%2Bpahe3KbdihlT2AiArSJ4LUcVB6mbPUFvdR8BSAc1aUkyEN2pKs3EGJPMMSyqIBAjG%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMy2HlbmmMpkHgXZ4NKtwDEN7EhmejGE4WzFlTHV4vmButAbQSZTxUUW79D2bznOCXo2h4IjePG8PezuuCBTV%2Bhbp2LdkgV%2BbI37h9ckXoUAqKOxJpsme%2B6V3x382Q2OIN%2B6HI%2B9VWP9VPIrDryZzY2Cot6RJzagfgCo1yUn4f9WfRKGhZNleJcFf3IYoSNAbI6nFbcn9Kzv04DN8Ih3ZA%2FLNiQnG2HZflIlZkkIsQrIyF5k2JAGmnTal5sfmj8koI46c%2B%2FpEv9RErrsXCubCbjTGTF6ApbkEwX79MuJG8o7jbCKXACgka2RGb9patM4BsUtwI4GukuQk0d2uSouU8PF4QZ4Rxl%2Bq%2Bd2Q784vy5FXB2oTSD0syDf5dWnFP7KkqCPrN3MHJOE9b2YyvcUW4BzZmFe160vMZouJ7wlRH%2Fkj0YKr3hF710r6WKYW7KnAduc3YRnCSbzqHqmpTibB9YPyd0ugM5w3lPaWi%2F6HXJ3RcfYAJiMEordP3tsPa3aKvbgEhw%2Bu%2B7MQAOatbznxiLFNjKB1NgV4AYmV8nu8MIcCueA0ii9CuLAh0axmfdbxhBddrJQZ3Kur3kqfCJmRxnsxdtwhDef5NYGCsx%2Fzp7%2B33awoLCb8Vv2Ocoo2vq177he9W9OYnyTr%2FR6cwt7j%2F0gY6pgHpRpCGgCj03de206N5W5dX%2FJbQzsSUH27%2FcNTeFJ3kva1JKj8Fix6t9QNjUo1Zvn4eJ4%2BowfRK%2Fh9m0naeELFJv%2BZbgqVQcEn99DQeMInzDWlfJhNquYbHY4Qa%2F45Le1%2FmN4nM%2F4DhFpgqpsUTEukgYKvOjcl3zqlK4ftWHeh8H87G19fZmd0lVhI9FWswUs0XSmvDkmH%2BEulkP6Un91WulpyWhZMX&X-Amz-Signature=3603871521717b2899cb83552abbe9e020f4480163aaaa65dd2b1fd1e1e0e210&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

然后在里面再弄一个 private connection，还要再弄一个 private statement statement。那这里可能有人会有疑问，为什么不是 prepared statement 呢？大家看 prepare 的 statement 也是statement，所以只要用 statement 就可以了。


面向接口编程生成一下 get set 方法，然后这里 create statement，就可以用 this 点儿connection，点儿 create a statement 了。这种方式是用 my connection 包装一个 JDB seed connection，然后这里由于实现了相同的接口，就可以有相同的方法。在之后可以在这里填入 my connection，这样就可以实现 connection 的管理。同理，其他的方法也得照填。


同学们和我一起填一下， this 点儿connection，点儿 native circle this 点儿connection，点儿 set autocommit， get out of commit， the meets，rollback，close， this 点connection，点 is closed， this 点connection，点 get metadata， read only， is read only。这个方法真的好多， set catalog， get a kid a logger。


事物，还记得事物的隔离级别有几种吗？如果记不得的话可以百度一下。这是一个比较常见的面试题。 get a transaction isolation warnings， clear on this， create a statement this 点connection，点 creative statement 那么我们需要关闭 statement 对不对？所以我们需要用 this 点儿 statement 等于这里创建的statement，然后再 return 掉statement。同理，这里的 prepare statement 也是类似的写法。
Is there connection there? Prepare statement.参数不要写错，SQL， result set type。
Without the set concurrency, is there statements then you prepared statement.
Tissue this there connection there. Prepare call, get a type map.
Set a type of map. Good ability.
Face their connection. There are get hold ability. Seven Points.
Rebecca.
Release save point. Create a statement.
This their statement then is statement return statements.  还有这里的 prepare statements 都得做处理。


又是一个 prepare statement，我们到这里copy，把参数改一下，继续copy。topic， this 点connection，点 create a blob， quit blob， create n club， create a sequel xml， is valid。


client info， set client info， get planning info， create a rive， create a struct， set a schema， get a schema，about， then i work time out，yeah， i will go time out。 a wrap。
以及 easy wrapper fall。


终于改造完了。那么可以检查一下有没有黄色，因为一旦有黄色的话，表示有递归调用，会有死循环的。好，检查一下，没问题。最关键的方法其实在 close 方法可以这么玩儿， diff this 点儿 is closed。也就是说如果底层的 connection 已经关闭的话，那么说明这个 connection 再又没有办法给别人使用了。这个时候我们就可以用 object pull，点儿 invalid object 把 z 字传进去。因为一旦底层的 connection 都已经被关闭了，那这个 my connection 肯定也没有办法复用了，对吧？泡一场 try catch 一下， catch 到异常的话，我们就把异常抛出去。


好else，说明底层connection，没有关闭，那么可以继续复用。那这个时候该怎么办呢？我们就可以用 object pull return object 了，把 this 传进去，这里怎么处理异常？我们可以处理异常的话，就把底层的 connection 给关掉，然后再把异常抛出去，当然了，还可以打一些日志，对吧？这样的底层的 connection 就可以被 my connection 管理了。


我们的问题解决了一半，那么 statement 该怎么样回收呢？可以这里把它改成 my connection，改 guy guy 这里有一个 passive object， passive it 翻译成中文叫钝化，那么什么叫钝化？什么样的逻辑该放到这里，我们把代码写一下，大家就可以理解了。用 p 点儿 get object，拿到一个 my connection，然后用 my connection 点儿 get a statement，然后判断一下 if statement 不等于空的话，我们就可以 statement 点儿close。报错处理一下。这里用 new my connection，然后 my connection 点儿 set connection 是底层的connection，然后传入 Mac nation 这样的我们的代码基本上就 OK 了。


简单梳理一下请求，会通过这里的 get a connection 打对象 borrow 的时候，就会调用到 factory 里面的 make object 的方法，然后产生了一个我们包装过的 my connection，然后 connection 再prepare， statement 的时候，这里太不巧了，正好弄到一个没有处理的statement，对吧？我们还是得处理一下，去听一下。


connection。 prepare statement 的时候就会把 statement 放到这里来，同时返回给JDBC，然后我们的 mybadcase 等等去操作数据库，操作完了之后，它会自动调用 connection 的 close 方法。如果底层的 connection 已经关闭，我们会把 my connection 这个类从对象池拿掉，如果底层没有关闭，那么会调 return object，然后又会调用到 factory 里面的 passive object，这个时候就可以把 statement 给回收掉。当然了，这里我们只实现了第三两点，第二点我们没有回收，如果你想回收 result set 的话也是一样的。


好，大致上的业务逻辑就是这样了。我们这里还有一些报错，处理一下就可以了。 my connection pull，OK，重启项目，依然有报错， fully 编译一下不报错了，正式重启。好，调用一下试试看。 send 依然可以正常调用，刷新发现没有达到我们的效果。来看一下这里的 object 的 pool 没有设值，对吧？我们需要在 object factory 里面设一下值， my connection set pool， object pool，然后要传入一个pool，这个 pool 我们又可以放到这里， object pool my connection object pool 生成一下 get set 方法private， object pool，那么这个 object pull 又该怎么传过来？可以在 data source 里面构造方法改造一下，factory，然后再用 factory 点儿 set object pull，这样就可以了。


重启项目，访问测试，也请求两次刷新，我们发现这一次的效果依然不太正常，因为对象都被回收了，没有实现复用。问题应该出在 my connection 的 close 方法，这里，忘记删了，对吧？我们在这里把底层的 connection 都已经关掉了，下面再做判断，这个是一个低级错误，删掉，打个断点，编译一下，然后再次请求，F8，可以看到由于底层的 connection 没有关闭，所以归还给对象池了。


刷新变成一个空闲的连接，我们多访问几次，刷新依然是一个空闲的连接，这意味着我们的连接一直被复用，那么我们也可以模拟并发比较高的情况。用。 AB 是阿帕吉基金会开源的一个 Benchmark 的工具，用起来比较的方便。杠 c 表示并发数，比如说 10 个并发杠 n 请求多少次，然后跟上请求的地址， lockhost 8088 挑一个 get 方法的请求， my orders deliver 问号， order id 等于 demo data。好它这里就会用 10 个线程疯狂的请求刷新，可以发现活跃的连接是 8 个，有 0 个是空闲的。这意味着我们的连接一直被复用着，我们把它关掉刷新，又会变成空闲的连接了，这样就可以大幅度的提升性能。


好，我们已经实现了一个带有监控的数据库连接池。这个代码写的还是不太优雅，主要有几点，第一， object factory 和 object 的 pool 存在着循环依赖，也就是 factory 里面引用了pool， pool 又需要调用， factory 一般是不太优雅的。这里给大家布置一个作业，大家考虑一下怎么样去防止这种循环依赖。第二是这个 data source 类写的还不够健全，下面有很多的方法没有实现。第三是这里的配置我们是写死的，理论上应该读取一个配置文件，对吧？好，这节课就到这里，谢谢大家。




