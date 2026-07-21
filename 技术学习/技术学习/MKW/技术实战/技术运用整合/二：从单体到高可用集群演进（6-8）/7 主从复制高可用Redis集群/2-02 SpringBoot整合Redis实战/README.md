---
title: 2-02 SpringBoot整合Redis实战
---

# 2-02 SpringBoot整合Redis实战

[image](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/73d88f04-0619-4d2b-b869-bca72fb3556e/SCR-20240805-hlgh.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RQ3YRXE4%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T224941Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIBPjEjULsTlXJB4egcONf%2Ffhi%2B9uxj94srPdE63oM5enAiEA4lDQuzfxAj%2F3J37TEHpFIm577ph7TcCUkfL0rndPt3oqiAQIxv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDKpg3U%2B%2BDDqGnZ9foyrcA%2Bmpk9QpnBnRRxW5ounp1FZGSMpFoOGU49hEzlTB8S804M11ppAnqom9YoM7lIB%2FkIwrqaaeShz6MMtBye3nKYLxW2rflfBukigALLzQPjKg69AQL3IEZqmMs8wCHM3EX6SR1XTmSiFCOK27OYO%2BoiTqdB75wNOPwOcvyJS0H3dsU2T5j41x2dn2m8iXFfjPaq%2BojL9OBH0fzJAL63o0qT6UIR8I6nzuxCEkBkpQmLNQmEeJnjZ73sMIOF9D88xvIFm7ljewd9Qwc2RIuBQlynmr5lP7PSCwjYpuaPxlrM10Skp7MQSnM8fcIab%2F64FtiRdJJ4GRViyvdMDaZteO3CtjgBz7ZVT%2FvTnKddk4OZAuYzbH%2Fl149109qCn5okMASEf1YUEd0932V6Xj1ZHg4eUbT34KWkSNa0DHgWEcCeQT8klooAFQcief78RGqtC%2BwYPVwmBdIj%2BK00kR%2BAzhdeMwu0w8%2FNZiMu9eRQydLpX9Nbm%2F8Hh%2BvIU6QFnotrsrJtUq4loTTQqddk0WYUhB4u8OQyK8EvVROu1r9TyAseMnzgD7tSnGP06Y60BQtKaIPJVnbZRBw6zNQLIz3uC5QH%2BzRJiRzkqF4kwlEHWpY1DEb5pZBbcj7DOlSa2wMNm5%2F9IGOqUBxeg2zjgb1Zwztn%2BbZQCh2yWGsFQBEcCUTKtnTFj3dg5%2BDUt4cVgc270TKrCPsH3pUwgg%2BdJlfJuCv%2B6svGCwN9AEFrVrX4du0KrgJMXqPqxulgEvyKEN2U45YS5VVaVa2QDd%2BtR1hvG53tIG%2B2xpG3bXoBp53L3G1UmLnEMc4uI3KLVgqyJHAjrdQ%2F05W9FqKV99SiSzIJsqMgNQvuX%2BMb1InQkz&X-Amz-Signature=065b58f4958436fae3ce884918515de69c1ba80031ed2dc71f243fd9db175ee4&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

[image](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/4ca0c34b-8771-4321-b552-62f4dec0e8d7/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RQ3YRXE4%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T224941Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIBPjEjULsTlXJB4egcONf%2Ffhi%2B9uxj94srPdE63oM5enAiEA4lDQuzfxAj%2F3J37TEHpFIm577ph7TcCUkfL0rndPt3oqiAQIxv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDKpg3U%2B%2BDDqGnZ9foyrcA%2Bmpk9QpnBnRRxW5ounp1FZGSMpFoOGU49hEzlTB8S804M11ppAnqom9YoM7lIB%2FkIwrqaaeShz6MMtBye3nKYLxW2rflfBukigALLzQPjKg69AQL3IEZqmMs8wCHM3EX6SR1XTmSiFCOK27OYO%2BoiTqdB75wNOPwOcvyJS0H3dsU2T5j41x2dn2m8iXFfjPaq%2BojL9OBH0fzJAL63o0qT6UIR8I6nzuxCEkBkpQmLNQmEeJnjZ73sMIOF9D88xvIFm7ljewd9Qwc2RIuBQlynmr5lP7PSCwjYpuaPxlrM10Skp7MQSnM8fcIab%2F64FtiRdJJ4GRViyvdMDaZteO3CtjgBz7ZVT%2FvTnKddk4OZAuYzbH%2Fl149109qCn5okMASEf1YUEd0932V6Xj1ZHg4eUbT34KWkSNa0DHgWEcCeQT8klooAFQcief78RGqtC%2BwYPVwmBdIj%2BK00kR%2BAzhdeMwu0w8%2FNZiMu9eRQydLpX9Nbm%2F8Hh%2BvIU6QFnotrsrJtUq4loTTQqddk0WYUhB4u8OQyK8EvVROu1r9TyAseMnzgD7tSnGP06Y60BQtKaIPJVnbZRBw6zNQLIz3uC5QH%2BzRJiRzkqF4kwlEHWpY1DEb5pZBbcj7DOlSa2wMNm5%2F9IGOqUBxeg2zjgb1Zwztn%2BbZQCh2yWGsFQBEcCUTKtnTFj3dg5%2BDUt4cVgc270TKrCPsH3pUwgg%2BdJlfJuCv%2B6svGCwN9AEFrVrX4du0KrgJMXqPqxulgEvyKEN2U45YS5VVaVa2QDd%2BtR1hvG53tIG%2B2xpG3bXoBp53L3G1UmLnEMc4uI3KLVgqyJHAjrdQ%2F05W9FqKV99SiSzIJsqMgNQvuX%2BMb1InQkz&X-Amz-Signature=0cd87d9447f8340a11c5acfa5e1b86e13770a6a2a25c280f414e8be5b6effc22&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

那么前面几节课我们是讲了 Redis 相关的一些知识，涉及到一些基本的类型以及是线程模型，那么接下来我们就回到咱们的开发工具，那么接下来就需要把我们的一个项目和 Redis 去做一个整合，那么整合的话，那么其实我们就相当于是把 Java 端作为我们的一个客户端，作为一个 client 去连接到咱们的 Redis server 去操作我们的一个 Redis 里面的一些内容，像set， get 这些请求都是可以去处理，都是可以去做的。


那么接下来该如何去做一个整合呢？那么首先我们是需要去打开我们的 POM 文件，在这个 POM 文件里面我们找一个位置，我们找到这里，我挑在这个 Redis 的，它在这个 my 卑鄙的下方，那么去增加一个Redis，那么这个 Redis 的话，那么它是需要有相应的一个依赖的，那么这个依赖的话我直接拷贝过来，那么这个就可以直接导入到咱们的一个项目里面来。那么它主要会使用到的是一个 spring mode start data Redis 使用的是这个依赖，然后 Ctrl s 保存。

当我们的一个整个一个项目构建完毕以后，那么相关的 Redis 包就会加入到我们的一个整个项目里面来，那么加入进来以后，那么千万不要忘记，那么我们是需要去做一个整体的全局的install，这个 install 要去做一下安装去跑一下。那么我这里的 Redis 是预先已经是下载好了，所以加载的时候会比较快，如果说你是初次的话，那么建议大家也可以去把自己的美文的库可以去改成阿里云，那么这样子下载起来的话会稍微的快一些。


然后那么这个时候我们就可以去做一个相应的内容方面的配置了，那么展开我们的这个 API 这个项目，找到咱们的 YAML 文件，在这个里面那么我们是需要去配置Redis，所以这个 Redis 其实是在这个 spring 这个下方的，那么在这个里面我们可以去做找一下有一个Redis，有 Redis 的一些很多的内容，然后在这里面其实可以看到有效密码等等的一些内容，我们都是可以去设置的。包括它还会有一个database，这是他 16 个库里面去选一个，默认的话是0，另外这个是host，那么这些内容的话，我们其实照理说我们不应该写在这个里面，因为这是我们统一的一个配置文件。那么其实我们之前是讲了profile，其实我们就应该要把相应的配置写到这个 Dev 的这个 YAML 文件里面来了。OK，写到杠 Dev 这个里面来，然后在这个地方我们就可以去加上咱们的一个配置了，它是一个Redis，然后 Redis 点首先第一个有一个 database 在这边，那么我们可以随便的去指定，你可以指定为0，在这边我就可以写一个1，我就以 1 为例。


然后你是需要去写上一个host，那么这个是你的Redis，它所在的一个位置，它的一个 ip 地址是多少，那么在这边写一下，那么这个其实也就是对应咱们的一个虚拟机，这个虚拟机你写的是一个每一个IP，那么停一下就可以了。那么我的虚拟机在内网的 IP 是191，所以那么直接就可以把这个 191 填写过来就行了。幺九二点幺六八点幺九幺保存OK，好。那么这个是它的host，除了这个以外，那么它其实还会有一个端口号，也就是pot，那么 6379 写上。随后除了这个以外，它还会有一个密码，密码的话是 m 写好。那么这样子对于我们的一个 Redis 的一个配置，那么就已经是配置好了。


配置好了以后，那么接下来我们就可以去操作 Redis 里面的一些相关的内容了，那么在这边我们呢可以这样子，我们找到 control 了，然后我们直接拷贝一个，把这个 hello control 的改成一个Redis，这个是用于去做测试的，然后没用的东西我们都全部删掉。


在这里我们可以写一个set，这是专门去用于去设置的，随后我们再来写一个，这边我们加上一个mapping，这个就叫做Redis，这里是get，然后再来一个delete。好，那么这三个方法的话，会分别对应到我们的一个 string 类型的一个get， set 以及是delete。OK，然后在这边set，我们是可以去做一个内容的设置，在这里我们可以去加上一个， string key，然后get，那么这个是 get 它的一个 key 的名称，delete，那么也是一样去删除某一个t。


好，那么这是几个基本的方法。那么当我们要去调用的话，其实在这个里面我们是需要去把 Redis 的一个格里斯的模板是需要去注入到我们的 Ctrl 里面来，那么这个模板类其实就叫做，这个叫做 Redis template，可以看到它是一个键值对的形式，然后双击一下，在这个上方我们加上 all to y 的把它直接给注进来。注进来以后在它的后方我们就直接可以定义为叫做 Redis temperate，那么这个时候我们就可以直接去使用它了。


然后在这个下方我们来看一下，在这个 Redis template 里面它会有很多的方法，我们往下面找，其中就会有一个找这个 o p s，然后 o p s 里面你会发现它其实里面会有很多的内容，比方说第一个是cluster，第二个是 g u harsh list set， value 和 c set。那么这些里面其实大多都是我们在之前在命令行里面是有讲过的，那么关于 string 的话，其实是这个 OPS for value 点一下，随后这个就是我们现在现阶段是针对 string 类型的内容去做的一个操作，来一个点你会发现这里面有很多的内容，比方说这是一个set，这是最简单的来写一下，那么这个 key 写过来，然后加上一个value，这个 value 那么我们也是从外面传入进来，那么这样子的话其实我们就做了一个设置。是把我们外部以 get 的形式给塞进来，一个是key，一个是value，根据键值去做的一个设置。


OK，那么这是一个set。好OK，这个我们返回一个OK，这里返回一个OK，然后我们再来做一个get，那么 get 的话，那么直接就是通过这个 Redis template，然后 o p s for value 点它会有一个 get 这个方法，然后直接把 t 给传进来，那么它就会得到一个内容了。那么这里是返回的是一个string，在这里我们再来做一个强制转换，那么这样子的话就可以根据我们 t 的内容直接给返回出来，然后这边有一个，再把这个名字改掉，方法名不能重复。

好，OK，那么这是一个 get 内容，然后这是一个delete，直接把这个拷贝好，背过来点，它会有一个方法叫做 delete key。它这个是不在这个 OPS for value 里面，它是直接可以去 delete 某一个 key 的，它是针对于所有的类型都可以去删的。把这个 key 的名称传入进来，它就可以去做一个删除了。删除之后在这边我会返回一个。OK，那么这样子的话，其实我们就是做了 3 个最简单的操作，一个是set，一个是get，另外的话是一个delete。那么现在我们就来做一个测试。那么在这里我们先去运行一下，先运行一下，然后我们再来，随后的话我把这个命令行工具先打开，因为我们在做测试的时候，我们是可以去看一下咱们的这个数据的。


然后当前直接输入 Redis 杠client，然后密码输一下 peace 新，然后回过来，现在我们已经是取证成功，随后打开浏览器，那么这是我们之前的 8088 所定义的，然后访问一下请求 Redis 斜杠set。然后来一个问号 key 等于name，我们给它赋予一个值，这个名称 value 敢与 m 可回车。那么这个时候报了一个 404404 的话，那就是我们是找不到了，找不到的话回到我们的idea，然后找一下这边我们刚刚写错了，应该是一个 request p 在这个里面给它加进去，随后我们再来做一个重启。


好，OK，启动成功。回过来我们再来做一个刷新，那么这个时候你会发现， OK 表示我们设置成功了。回到命令行工具，来一个 kiss 信号，你会发现这个 key 没有。这是因为我们在这个项目里面，我们所设置的这个库，我们设置的是这个1，所以我们要做一个切换， select 1 回车。


然后再来一个keys，那么这个时候你会发现在这里面多了一个key，这个就是我们刚刚在页面里面所设置的这个key，这个 k 就叫做是name，但是为什么会有一个乱码，那么这个我们可以先不用管，因为这个是它的一个序列化的一个问题。OK，然后的话这个 name 的话，那么现在其实已经是在我们这个里面存在了，那么随后我们是可以通过这个浏览器再去做一个获取，我们在这里面把这个改为get，然后这边已经是取得了，然后 get 这个 key 是等于name，根据这个 name 去获取它的一个值，那么很明显这个 m 可就是我们刚刚所做的一个值。随后我们再去做一个删除，那么这个删除是一个delete，根据这个 key 的名称去做删除，那么这样子的话我们直接把这个 get 改为delete，再做一个回车。OK，删除成功，然后到命令行里面去看一下，这个 kiss 就已经是被我们给删掉了。


OK，那么这样子其实我们就已经是把这个 Redis 整合到了咱们的一个项目里面来，那么除了我们的一个客户端，现在我们所涉及到的客户端一个是 Redis client，一个是在我们项目中的，那么其实我们再为大家来推荐一个工具，那么这个工具叫做 Redis desk group manager，那么这个其实是一个 Redis 的可视化的一个桌面工具，那么不管是在 windows 还是在 Mico s 上其实都有。那么推荐大家可以去安装去使用一下，那么这个的话我目前也已经是安装了，打开给大家可以去看一下。


那么在这里面的话，在这边可以去创建一个连接，那么这个连接首先在这边取一个名字，比方说我起一个叫Imock，然后这是你的 ip 地址，幺九二点幺六，八点幺九幺，然后端口号默认是6379。如果说你改掉不要忘记要去修改，那么当然如果说我们的密码，这个密码是一个可选项，那么我们是修改了，所以把这个 Imock 给加上，那么其他的一些配置的话，你默认保留就行了。


随后在这个下方 test 肯定要选去测试一下，你会发现 OK 没有问题，然后点击OK，那么这样子在我们的这里面多了一个m，可双击一下，你会发现这边有很多的一个DB，总共是有 16 个，那么下标是从零一直到这个下标15，那么 DB 0 的话就是我们之前在测试的时候所用的。那么像这个就是一个 c set，很明显这个 set 里面所包含了一些内容，这个是它的一个 score 分值，这个是它的里面的内容。OK，那么当然我们也能够去看一下这个DBE，这里面没有数据，我们把这个浏览器回退一下，然后我们来看一下。到 set 回车，然后重新去设置一个值。我们再去改一下其他的名字，比方说这个是再来加一个 a 级，来一个 18 岁，然后再来添加一个，比方说sex，来一个woman，再来一个male，来一个 a b c admin . com。回车。好，OK。


然后到我们的这个工具里面来，这个时候我们只需要在这个地方，这是一个刷新按钮， RE 漏了一下，你会发现我们在这里面所设置的一些值全部都会有OK，只不过我们在进行查看的时候，其实它还是会包含这些乱码，它里面的一个 value 其实也是这样子，但是这个的话我们可以不需要去管OK，这是它的一个序列化的机制。好OK，那么这一节的话就是我们针对于这个 Redis 做的一个磁屏布彩方面的一个整合，以及是它的一个桌面的一个管理工具的一个使用OK。

[image](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/7be54fc4-cb93-420f-9560-3e7ff3c3c82d/2020-09-17_195637.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RQ3YRXE4%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T224941Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIBPjEjULsTlXJB4egcONf%2Ffhi%2B9uxj94srPdE63oM5enAiEA4lDQuzfxAj%2F3J37TEHpFIm577ph7TcCUkfL0rndPt3oqiAQIxv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDKpg3U%2B%2BDDqGnZ9foyrcA%2Bmpk9QpnBnRRxW5ounp1FZGSMpFoOGU49hEzlTB8S804M11ppAnqom9YoM7lIB%2FkIwrqaaeShz6MMtBye3nKYLxW2rflfBukigALLzQPjKg69AQL3IEZqmMs8wCHM3EX6SR1XTmSiFCOK27OYO%2BoiTqdB75wNOPwOcvyJS0H3dsU2T5j41x2dn2m8iXFfjPaq%2BojL9OBH0fzJAL63o0qT6UIR8I6nzuxCEkBkpQmLNQmEeJnjZ73sMIOF9D88xvIFm7ljewd9Qwc2RIuBQlynmr5lP7PSCwjYpuaPxlrM10Skp7MQSnM8fcIab%2F64FtiRdJJ4GRViyvdMDaZteO3CtjgBz7ZVT%2FvTnKddk4OZAuYzbH%2Fl149109qCn5okMASEf1YUEd0932V6Xj1ZHg4eUbT34KWkSNa0DHgWEcCeQT8klooAFQcief78RGqtC%2BwYPVwmBdIj%2BK00kR%2BAzhdeMwu0w8%2FNZiMu9eRQydLpX9Nbm%2F8Hh%2BvIU6QFnotrsrJtUq4loTTQqddk0WYUhB4u8OQyK8EvVROu1r9TyAseMnzgD7tSnGP06Y60BQtKaIPJVnbZRBw6zNQLIz3uC5QH%2BzRJiRzkqF4kwlEHWpY1DEb5pZBbcj7DOlSa2wMNm5%2F9IGOqUBxeg2zjgb1Zwztn%2BbZQCh2yWGsFQBEcCUTKtnTFj3dg5%2BDUt4cVgc270TKrCPsH3pUwgg%2BdJlfJuCv%2B6svGCwN9AEFrVrX4du0KrgJMXqPqxulgEvyKEN2U45YS5VVaVa2QDd%2BtR1hvG53tIG%2B2xpG3bXoBp53L3G1UmLnEMc4uI3KLVgqyJHAjrdQ%2F05W9FqKV99SiSzIJsqMgNQvuX%2BMb1InQkz&X-Amz-Signature=4233788d7b0343b99cf1e13c77dc2fa4879bcc609df25c96c9bc561b4cde2223&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

