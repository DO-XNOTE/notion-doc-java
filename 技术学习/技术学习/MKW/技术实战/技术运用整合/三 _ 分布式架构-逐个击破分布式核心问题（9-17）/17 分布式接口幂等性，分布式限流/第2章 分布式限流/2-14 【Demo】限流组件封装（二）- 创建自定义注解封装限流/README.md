---
title: 2-14 【Demo】限流组件封装（二）- 创建自定义注解封装限流
---

# 2-14 【Demo】限流组件封装（二）- 创建自定义注解封装限流

[image](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/56288f23-7e2b-41cf-8994-693923d208c6/SCR-20240808-iwda.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662QE4WBC7%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T225506Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCbGczkuTrVc7iB4M9LlCqervRjdC3Foqusu9CfIvuwxQIgPTpQX%2FtT%2BMS9QOvXEgSagLdpPcu1d3fwx7VvTTMRb6oqiAQIxv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDCTteTTmWOfUv95HBSrcA9hf%2BG2aGn50OZ7dhy%2Bs%2F4Y612wS%2B2rKL2%2FBP3VJIXA3CHG0jeqWM83l5Ol1HevPqTMSRHSDrOT9aD1vzGiK1mNFgTwz4iSFjFDoP6TQYRl1vJpOjX9rEoX0WwtkBgurMR3%2BJW4UZ2XAbPiqRS3IpJ4eUA9I75N%2BL%2BkGbr4QA2IW0CZ5VHwymKTTabTmc%2FUdaqmUaDhTpNia8PnZJt5ZhuYm3T3N0UOWctgO5kBNKvincIEaUUNX2niXv1VYvWyIciGHbAV5lvE85Wtnl%2Fc6utpQd9%2B05uq0gZa%2FZGkvPPS53MEnCRXiQvGdvBcvK7E7wYq3EzF5sfHSicTve8Jt7ZHrZ9OTG2t6ucOB42ovYnwbhzaiGudswMubqXtIocqWoZDPrWUujAY%2Fko%2B6IQekJoNc6Y24JKaIFHvOqWhAcAikEdecKB2CczSs1S6hh06YdGxzJaJOkLs6WheDCUp8J4Nv%2B91Diyx5UhOTKY9SWVtX2j2PXLOVgrBgshl8HA2%2F4oEY3M720jaZRH6WZavB3WwyxTjBYfdswQ8ix6n0%2F6zoBG5GBgait0l4NHZQZa6rnKwvxRhfq9fwZin9D0TiTW8WysqtUzmXV8riyu9ZA12LISPTQTMX2oFEm4pPMLe4%2F9IGOqUBs5yZPtW7qT7BLtVvFvc2WODsyYznsX0MXth%2FDBxOwOFrBTTS%2FgWj5tzDpoN3eM4fXMNhYINsSSXecD3Ap3Vf8uLS%2Frmfff%2BBjzYGpAvS3II%2BLIhSi7I0qL93DiSKhTvjCuImz2bgaKWGion%2FEe2ETK%2BngiZtBMoVHIZZ4ixrbp2G%2Bc36YdccyMKOnBw1wQZisitb%2BGJYPBoTr%2Be2Emggs5wnAuEV&X-Amz-Signature=feaa17527049ddae665e3e11ff5029e7212a3d68a6fc87fca1c7b99f9e3212ca&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

[image](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/149ee283-e67b-4386-a42c-9ca5242ea31e/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662QE4WBC7%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T225506Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCbGczkuTrVc7iB4M9LlCqervRjdC3Foqusu9CfIvuwxQIgPTpQX%2FtT%2BMS9QOvXEgSagLdpPcu1d3fwx7VvTTMRb6oqiAQIxv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDCTteTTmWOfUv95HBSrcA9hf%2BG2aGn50OZ7dhy%2Bs%2F4Y612wS%2B2rKL2%2FBP3VJIXA3CHG0jeqWM83l5Ol1HevPqTMSRHSDrOT9aD1vzGiK1mNFgTwz4iSFjFDoP6TQYRl1vJpOjX9rEoX0WwtkBgurMR3%2BJW4UZ2XAbPiqRS3IpJ4eUA9I75N%2BL%2BkGbr4QA2IW0CZ5VHwymKTTabTmc%2FUdaqmUaDhTpNia8PnZJt5ZhuYm3T3N0UOWctgO5kBNKvincIEaUUNX2niXv1VYvWyIciGHbAV5lvE85Wtnl%2Fc6utpQd9%2B05uq0gZa%2FZGkvPPS53MEnCRXiQvGdvBcvK7E7wYq3EzF5sfHSicTve8Jt7ZHrZ9OTG2t6ucOB42ovYnwbhzaiGudswMubqXtIocqWoZDPrWUujAY%2Fko%2B6IQekJoNc6Y24JKaIFHvOqWhAcAikEdecKB2CczSs1S6hh06YdGxzJaJOkLs6WheDCUp8J4Nv%2B91Diyx5UhOTKY9SWVtX2j2PXLOVgrBgshl8HA2%2F4oEY3M720jaZRH6WZavB3WwyxTjBYfdswQ8ix6n0%2F6zoBG5GBgait0l4NHZQZa6rnKwvxRhfq9fwZin9D0TiTW8WysqtUzmXV8riyu9ZA12LISPTQTMX2oFEm4pPMLe4%2F9IGOqUBs5yZPtW7qT7BLtVvFvc2WODsyYznsX0MXth%2FDBxOwOFrBTTS%2FgWj5tzDpoN3eM4fXMNhYINsSSXecD3Ap3Vf8uLS%2Frmfff%2BBjzYGpAvS3II%2BLIhSi7I0qL93DiSKhTvjCuImz2bgaKWGion%2FEe2ETK%2BngiZtBMoVHIZZ4ixrbp2G%2Bc36YdccyMKOnBw1wQZisitb%2BGJYPBoTr%2Be2Emggs5wnAuEV&X-Amz-Signature=8a833487a05e3e3a2477c577da410ee569991b6e2346d0f98904a88a198d8ec5&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

hello 我们课网的各位同学们，大家好，咱这里就接着上一节中的内容，把限流的服务改造成一个基于注解的功能。

[image](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/95fa7eac-4b72-4fae-b4b5-8cf57c625c70/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662QE4WBC7%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T225506Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCbGczkuTrVc7iB4M9LlCqervRjdC3Foqusu9CfIvuwxQIgPTpQX%2FtT%2BMS9QOvXEgSagLdpPcu1d3fwx7VvTTMRb6oqiAQIxv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDCTteTTmWOfUv95HBSrcA9hf%2BG2aGn50OZ7dhy%2Bs%2F4Y612wS%2B2rKL2%2FBP3VJIXA3CHG0jeqWM83l5Ol1HevPqTMSRHSDrOT9aD1vzGiK1mNFgTwz4iSFjFDoP6TQYRl1vJpOjX9rEoX0WwtkBgurMR3%2BJW4UZ2XAbPiqRS3IpJ4eUA9I75N%2BL%2BkGbr4QA2IW0CZ5VHwymKTTabTmc%2FUdaqmUaDhTpNia8PnZJt5ZhuYm3T3N0UOWctgO5kBNKvincIEaUUNX2niXv1VYvWyIciGHbAV5lvE85Wtnl%2Fc6utpQd9%2B05uq0gZa%2FZGkvPPS53MEnCRXiQvGdvBcvK7E7wYq3EzF5sfHSicTve8Jt7ZHrZ9OTG2t6ucOB42ovYnwbhzaiGudswMubqXtIocqWoZDPrWUujAY%2Fko%2B6IQekJoNc6Y24JKaIFHvOqWhAcAikEdecKB2CczSs1S6hh06YdGxzJaJOkLs6WheDCUp8J4Nv%2B91Diyx5UhOTKY9SWVtX2j2PXLOVgrBgshl8HA2%2F4oEY3M720jaZRH6WZavB3WwyxTjBYfdswQ8ix6n0%2F6zoBG5GBgait0l4NHZQZa6rnKwvxRhfq9fwZin9D0TiTW8WysqtUzmXV8riyu9ZA12LISPTQTMX2oFEm4pPMLe4%2F9IGOqUBs5yZPtW7qT7BLtVvFvc2WODsyYznsX0MXth%2FDBxOwOFrBTTS%2FgWj5tzDpoN3eM4fXMNhYINsSSXecD3Ap3Vf8uLS%2Frmfff%2BBjzYGpAvS3II%2BLIhSi7I0qL93DiSKhTvjCuImz2bgaKWGion%2FEe2ETK%2BngiZtBMoVHIZZ4ixrbp2G%2Bc36YdccyMKOnBw1wQZisitb%2BGJYPBoTr%2Be2Emggs5wnAuEV&X-Amz-Signature=630fd470a7cb18f1e26efc970738fd2176a93c798937a376a14ff774451cf042&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

接下来我们看一下本节的主要内容都有哪些。首先我们通过 aspect G 创建一个自定义的注解，它名字叫做 access limit 然后再为这一个注解配置限流规则的切面。那在我们具体的限流的业务里将要加入两个维度的功能。第一个维度就是使切面配好了以后在什么阶段生效。第二个维度就是对我们上一节中的 method key 不知道大家还有没有印象，我们 method key 是由上游业务传入的，那我们这里会根据具体的调用方法，自动生成一个方法签名作为 method key 传入到 ludscript 当中。 OK 那最后就是为目标方法添加上这个 access limit 注解，验证这个限流的效果。 OK 同学们准备好的话就抄起家伙跟我开工。


好嘞，开动了。咱先打开前面创建的 rate limiter annotation 这个项目，在 calm.imock.spring cloud 下面再创建一个 package 给它起名叫 annotation 这里我们将要放新生成的注解以及它的切面流程。 OK 那第一步就是给这个文件夹下面创建一个 annotation 把它的类型从这里选择到 annotation 这个类型，然后起名咱依然把它叫做 access limiter 好了，点击 OK 好，那接下来咱开始修饰这个注解了，首先给它定义一个运行周期 rotation 那这里我们指定它的运行周期是什么呢？是 runtime 级别，这里有很多个类型，有点 class.runtime 还有 source 那分别对应什么编译级别，运行级别和源码级别。咱这里去选择的是运行级别，然后给它加一个 document 注解，这个 document 实际上这个注解无所谓。


咱这里还有一个更有所谓的注解叫 targettarget 里面指定什么内容呢？咱先来指定哪些方法或者哪些对象可以应用这个注解，我们把它指定到 element type 的 master 上，也就是方法级别生效，所以我们要把这个 master 给它加上。


好，那这三顶大帽子已经戴完了，咱们来编写注解里面的内容。首先第一个应该是什么呢？应该是 key key 就是 method key 我们给它加一个默认的值 default 是空。好，除此以外，咱前面还有一个属性叫什么 int 对不对？ Limit. 那 limit 这里我们可以给它加一个默认的值，比方说是 1 或者是2，那这里我先给它置空了。好，那这两个属性也定义完了。那接下来空空的一个注解也没有作用，我们是不是要定义一些切面的流程呢？好，那接下来依然是在这个 annotation 这个包下，我们创建一个class ，它叫 a access limiter aspect 专门为这个注解指定的这么一个切面流程。我们把小桌板收起来，你说它是切面，它就是切面了吗？这是怎么生效的？那就要靠 aspect G 了，我们这里给 aspect G 把它引入进来。


OK 那再给大家一个 sl four G 好勒，接下来怎么办？很简单，我们给它创建一个切面点，比如说 public void cut ，我相信同学们在工作当中应该都有过自定义注解的经验，而且这也是初级加程序员面试的很容易问到的问题。所以我就不太过深入地讲这每一个注解的具体功能了。咱这里就直接真刀真枪开始写。
第一个 point cut 我这里给它指定什么，在什么时间点下我才会进入到这个切面流程。那我们这里指定 annotation 哪个 annotation 呢？就是咱刚才创建好的那个 annotation 它的类是 come 点、 IMock 点、 spring cloud 下的 annotation 下的谁 access limit 对不对？这个可不要写错了，这个写错了，它不能生效。那这句话的意思是你但凡正确的引用了 access limiter 在自己的方法上。怎么样啊？就被我的这个切点牢牢地捕获住了。那说把你抓住就把你抓住。你要不信。那好我们打一行log ，证明你被。好，那抓住了怎么办？抓住了。那后面就好玩了。


怎么上大型？我们再写一个方法叫 public void before before 什么？我这里再给它添加一个注解。 before 注解，这也是 aspect G 里面的注解。那我会指定一个 cut 这个 card 是谁？同学们目光往上移，是不是在这个 card 里，就是说你这个切点被捕获到了之后，我预先执行一段什么样的流程？这里就是我们要执行的限流流程，咱有这么几步，第一步是怎么样获得方法签名，这个方法签名用作什么用呢？作为 method keyok 那第二步就是很简单的调用 Redis 好，总共就分这两步。那我们先这样先从后往前写好了，我们先把调用 Redis 的部分给拿过来，就从哪里拿呢？从咱前面写的这个 access limiter 这个服务中，我们把这一段全部给它 copy 过来。好嘞，然后复制到这里。 OK 那复制过来以后，我们发现这里有几个引用，我们同样的也要把它给拿过来走，再去抄作业，去把这两行给抄下来，放到哪就放到 expect G 的最顶上。


好了。 OK 那剩下的红字是哪里？是一个 key 和一个 limit 对不对？那好办， key 就是我们第一步中要获取的内容。那怎么获取？大家想这个 key 和 limit 都是放在哪里呢？放在咱的注解里对不对啊？那如果我们在一个切面中想获取到这个注解，那应该怎么办呢？是不是应该用反射拿到方法，再通过这个方法拿到它上面的注解呢？所以我们这里方法入参不要写上 join point 这是它的入参。


那我们接下来需要用到的东西都从这个 join point 里面来拿，怎么来拿？第一步，刚才咱说的要拿到谁方法的签名，方法的签名怎么拿呢？ signature 它从 join point 我们看它里面有很多方法，其中有这样一个方法， get signature 来给我签一个名，让你给我签个名，咋还给我整红了，怎么办给它强转一下。好嘞，那这不就是可以了吗？那获得了签名之后，接下来怎么办呢？很简单，通过这个签名把 method 给拿到，这个 method 是 reflect Java reflect 包下面的反射类直接从 signature 里面 get method 是不是非常简单。拿到 method 以后，那后面的事儿就超级简单了。咱要把这个注解拿到 access limit 注解拿到。这有两个类，大家注意要引用这个咱创建的 annotation 这个注解，不要引用到前面创建的 service 了，好叫 annotation 好从 method 当中 get annotation 把这个注解的名称 class 也给它传入进去。


因为你方法上面可能不止这一个注解，所以我们要指定你想拿到的注解是谁？是咱这个 access limiter 好。拿到注解以后如果注解为空怎么办呢？咱叫防御性编程。对不对？注解为空啥都不干，直接 return 实际上但凡你到了这个界面，这个注解应该不会为空的。不过老师这个人比较怂，我有这种强迫症，我非要在每一个可以判空的地方加一个判空，同学们就放过老师的这个小任性。


好，接下来我们要拿到什么？拿到它的 key 这个 key 从哪里拿？就从 annotation 里面拿它的 method key 接下来还要拿谁拿它的 limit 也同样的从 annotation 里面把它给拿到。好，那这里就要判断了，我们说过这里我想根据什么呢？根据方法的 method 自动生成这个 key 不过如果你在调用我的时候，把这个 key 已经指定好了，那意思就是告诉我用你的 key 不要用我自动从 method 当中生成的这个 key 所以我这里第一步先给它做一个判空。


如果你是 empty 谁，就是你没有传入给我这个 K 那么接下来怎么样？我从方法中自动给你生成一个如果没设置 matter key 那从调用方法签名生成一个 K 好，这是自动生成一个 K 怎么自动生成？非常简单，咱的方法签名包括什么？方法的名称，那还有什么？还有它的入参包括它 return type 这些我们可以自由组合，比如说 class 我们把它的这些 parameter types 先给拿到，那这部分同学们应该不用老师再深入讲了。 Java 反射技术，我相信上这门课的同学应该都是相当熟了。


get parameter types 好，拿到这些 types 以后，那我这个 key 怎么样？先把方法签名给它获取到 matter get name 我们这里之所以要考虑到它的入参是因为什么？因为你的方法签名中你的名称方法名可能是相同的，然后两个相同方法也可能在同一个类里面，那只能依靠你的入参来决定是哪一个方法发起了调用，所以我们这里要加一个判断，如果 type 不等于空怎么样呢？那就把它循环一把循环拼接一个谁一个 pyram type 好，那这里用 lambda 表达式来做了，因为这样最简单最省事。


这里使用 aries 的 stream 方法，stream方法把谁传入进去，把前面的这个 type 传入进去之后再调用它的 map 方法。因为咱传入的是个 class 对象，但是我们只需要谁只需要这个 class 的 get name 我只要调用它的 get name 就可以了。然后再使用 collect 方法把这些结果给它收集起来。但是在收集的过程中我不想让它看太乱。所以我这里要怎么样呢？我想要 collectors 把它给中间分隔一下。好 joining 怎么样分隔，以一个逗号来把它分割一下。Ok.好，那我们这里不妨打一行 log 验证一下这个分离的结果。这个 log 就叫 harom types 不过在咱的生产环境当中，大家尽量把这种 annotation 里的 log 改成 debug 级别，尽量让这种跟业务无关的代码，而且对插播 shooting 没太大作用的代码不要让它打印出来，咱这里只是为了测试先来看看效果。所以把这里放这了。


其实对很多的公司对 log 是有规范的。比如说你运用不同的链路追踪技术，它可能对你的 log 格式甚至都有一定的要求。如果你想要根据 business key 来查找 log 那它可能要求你每一个 key 比方说叫 ID 那 ID 要严格遵照什么呢？ ID 等于叉这种格式来定义，通过这种方式它就能抓取到这行杂乱无章的 log 中，这一段是带有业务含义的。那么如果你根据这里定义的 ID 来在链路追踪系统中查找特定的 log 会搜索得非常快。


好，我们这里只是把这个 parameter types 给它打印出来，打印完了以后我们要怎么样？我们要把这一行 pyramid types 加到 key 的末尾。好，我们在这个 key 的 master name 和 pyramid type 之间加上这样一个井号，到这一步咱已经完成了 key 的提取。
那接下来我们把前面创建的 access limiter 给它标记一个什么呢？ Deprecated. 也就是说这个类已经被淘汰了。那所以同学们如果在开源软件当中看到某一个类标记了 deprecated 那说明要么它被淘汰落伍该退休了，要么它有更新版本或者更新的机制来替代，那咱就尽量避免使用这种类。


好了，有些公司有很严格的代码检查，比方说像 sona 它里面会配置一些规则。如果你在方法中引用了某些开源组件已经标记为 deprecate 的类，那么它会报错，甚至不让你提交代码。 OK 那我们这里再回到 controller 里，咱这个 controller 要来升级改造一番了，我们添加一个新的方法，这个方法同样也返回 string a test annotation 同样它的 get mappings 我们也起一个不一样的名字叫 test annotation 好嘞，返回一个 return success 非常简单。那怎么 test 我们这样写引入这一个注解，然后 key 我暂时不指定，我让它通过这个方法签名自动获得。但是 limit 是你一定要指定的，我给大家指定 limit 等于 1ok 那这里就成功了。不过我这里要提醒同学一下，由于咱这个 access limiter 它的路径是什么呢？你看它是在 calm.imock.spring cloud 下面的。如果你的项目在不同的路径下，你想让 access limiter 生效，那可能要配置扫包路径。扫包同学们应该都知道怎么做，我这里就不再演示了。不过我在这里要提醒一句叫提醒，注意配置扫包路径。因为为什么呢？ home.i mock.spring cloud 路径不同。咱在电商项目中使用的是另外一个包，同学们就可以把这个组件引入到电商项目中。然后你看哪个服务不顺眼，怎么样给它添加一个 access limit 限制他的访问就说闭嘴，老夫看你不顺眼让你限流。


那咱配置好了之后，我们就启动这个项目看一下效果，走到闷函数里直接走，你稍等半炷香的时间，看到 spring 标签打印出来成功了一半，这里已经显示 started 了。那我们转战到 postman 好，这个 postman 里的路径还是之前的老方法，即使咱把之前的 service 标注成 duplicated 但是它的功能依然是不受影响的。我们把这个方法改一下，改成 test 杠什么 annotation 好，我们尝试调用一下。


好，第一下正常配置的是匀速一秒钟我们点快一些，好点快。同学们看到吗？说明怎么样？说明此案通过注解形式的限流功能，也可以正常的提供限流服务。 OK 那到这里本节的内容就结束了，同学们在前面体验了网关层的限流，在这里又体验了在业务层面的限流，大家可以去思考这两种风格都适用在哪些项目当中，两种方法各有利弊，同学们在项目中可以去结合的使用。那网关层的限流，它可以避免你的流量冲击到服务器，它在到达服务器之前就把你拦住了。而这种限流方式，你的流量怎么样？需要去引到服务器，在业务层面才会拦住。这是网关层限流优于业务层限流的地方。但是咱业务层限流它的控制更加的灵活。我们可以把这个 annotation 加入到任何方法当中，比方说我不想在这个方法最外层限制，我想在这个方法里面调用的 12345 很多个 service 当中，我先是其中一个 service 的访问可不可以？当然。所以这是业务层限流的优点，它更加的灵活。那同学们可以因地制宜，在合适的场景中用合适的方法。


那到这里，整个分布式章节就告一段落了，同学们一定要好好的加几个菜吃一顿，庆祝一下。我们接下来将步入一个新的篇章，微服务体系架构课程。那半仙老师在下一章课程中等着你们，我们下节课程再见。



