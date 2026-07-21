---
title: 2-21 【技术改造】电商系统集成Stream- 批量强制用户Logout
---

# 2-21 【技术改造】电商系统集成Stream- 批量强制用户Logout

[image](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/e82252f5-91f3-4d3a-98b7-76786c2c5b62/SCR-20240722-ehuq.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46652N3X3LF%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T225823Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIDXHc4j%2BAvgwtdM1dUznF9Vq6EFItaEWmf32mzmh%2FawyAiEAiIEtJMHioBwCGawAHTCVPgNDBHlYKrMNbvGt3F4gaR4qiAQIxv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDMXFWdWIxZNu7PcEESrcA3%2Bl6s2lZeaLGaarqjoHZSeaIMzKJ%2BTHKn%2FEtSa0bzodXCrIzKMVwioXEEk0v5vnbvX5owAQPoTLslP9HCbzInyi2fGXlpPSBSuiTUuMww6pUDjKK6vdHR9nxShSXkqmSmFAAetrXyuQoIZzt7An67zFrjrUocs8nABsxYdomTn4PaJSVM3Tdxde6GbngAEPbFJhHGY5xdgu5JT%2FawBtMuwJ5%2FpBeQpdOSwZxcyg78uvrosDrg%2Bj4Vm2t%2FXEdEc55Taw%2BYmm5zWCWAsMzbxHlK67J67styJzWPSNP3PCtzMC8RzCdmio2z78kdD6WFGEQ1fB3ftIKOph6%2Fy9tum4koxor6wkrTNs2TsOxDfdZyO59m793x4rinlCgZe84lQdMR4SCx%2BFSoNyRP31%2Br2zhedKztqd%2B%2BohWdFHPi8Dj9KfSvrVSKVhTi6rLy4P%2Bp9PreP1seIeV47T6EwehPk%2Fl6dmzEKK3pILuA5V%2FGwyrGNCIihEoMwgHWo9BZZ8ObQ4Opk1JES0tgitGayDZjp6p80oGTp2qkCtO5SJlTJnSbl%2BMnubwGqx%2Fq92aRIhdf2AjlOT6WyPOE8pj2z4sx62yNArLzWVEbLdAys6RxGmyz43bLUSH5SP8U%2BZBwwjMJa3%2F9IGOqUBAgK2VoycMGF1hd%2FgPHLA1SLQKQH1BG35%2FCmG3zWcYk3n4fGM4iT8V4dTBB%2Bitn75l851GbDUAtbTS0eh6dPiPjXI16vYkCD0hP8r2gA9zhNYX%2BemFmeCzWAFiunqSzzn3l0GlVBTtQvKzNRUpAubwWQipfeG2wTVMCRtQnykpUBaksxUYJUVMBUb0hCwdamaB6mpkK09T5p%2B1LW3WKS%2FkEAWPzue&X-Amz-Signature=c65fccff2614c0e5516804a0662b189964568d4123e29c8124a9be6d0f7be66a&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

[image](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/25373c06-3609-4d1d-9bcd-35659655d7ba/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46652N3X3LF%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T225823Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIDXHc4j%2BAvgwtdM1dUznF9Vq6EFItaEWmf32mzmh%2FawyAiEAiIEtJMHioBwCGawAHTCVPgNDBHlYKrMNbvGt3F4gaR4qiAQIxv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDMXFWdWIxZNu7PcEESrcA3%2Bl6s2lZeaLGaarqjoHZSeaIMzKJ%2BTHKn%2FEtSa0bzodXCrIzKMVwioXEEk0v5vnbvX5owAQPoTLslP9HCbzInyi2fGXlpPSBSuiTUuMww6pUDjKK6vdHR9nxShSXkqmSmFAAetrXyuQoIZzt7An67zFrjrUocs8nABsxYdomTn4PaJSVM3Tdxde6GbngAEPbFJhHGY5xdgu5JT%2FawBtMuwJ5%2FpBeQpdOSwZxcyg78uvrosDrg%2Bj4Vm2t%2FXEdEc55Taw%2BYmm5zWCWAsMzbxHlK67J67styJzWPSNP3PCtzMC8RzCdmio2z78kdD6WFGEQ1fB3ftIKOph6%2Fy9tum4koxor6wkrTNs2TsOxDfdZyO59m793x4rinlCgZe84lQdMR4SCx%2BFSoNyRP31%2Br2zhedKztqd%2B%2BohWdFHPi8Dj9KfSvrVSKVhTi6rLy4P%2Bp9PreP1seIeV47T6EwehPk%2Fl6dmzEKK3pILuA5V%2FGwyrGNCIihEoMwgHWo9BZZ8ObQ4Opk1JES0tgitGayDZjp6p80oGTp2qkCtO5SJlTJnSbl%2BMnubwGqx%2Fq92aRIhdf2AjlOT6WyPOE8pj2z4sx62yNArLzWVEbLdAys6RxGmyz43bLUSH5SP8U%2BZBwwjMJa3%2F9IGOqUBAgK2VoycMGF1hd%2FgPHLA1SLQKQH1BG35%2FCmG3zWcYk3n4fGM4iT8V4dTBB%2Bitn75l851GbDUAtbTS0eh6dPiPjXI16vYkCD0hP8r2gA9zhNYX%2BemFmeCzWAFiunqSzzn3l0GlVBTtQvKzNRUpAubwWQipfeG2wTVMCRtQnykpUBaksxUYJUVMBUb0hCwdamaB6mpkK09T5p%2B1LW3WKS%2FkEAWPzue&X-Amz-Signature=57a2283746c7332e650d99ec9046c808c9edcef5c8a2c8b59c73e86d06aa6b73&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

[image](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/ed0b540d-a61d-4713-b21e-b7efcc1a54cc/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46652N3X3LF%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T225823Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIDXHc4j%2BAvgwtdM1dUznF9Vq6EFItaEWmf32mzmh%2FawyAiEAiIEtJMHioBwCGawAHTCVPgNDBHlYKrMNbvGt3F4gaR4qiAQIxv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDMXFWdWIxZNu7PcEESrcA3%2Bl6s2lZeaLGaarqjoHZSeaIMzKJ%2BTHKn%2FEtSa0bzodXCrIzKMVwioXEEk0v5vnbvX5owAQPoTLslP9HCbzInyi2fGXlpPSBSuiTUuMww6pUDjKK6vdHR9nxShSXkqmSmFAAetrXyuQoIZzt7An67zFrjrUocs8nABsxYdomTn4PaJSVM3Tdxde6GbngAEPbFJhHGY5xdgu5JT%2FawBtMuwJ5%2FpBeQpdOSwZxcyg78uvrosDrg%2Bj4Vm2t%2FXEdEc55Taw%2BYmm5zWCWAsMzbxHlK67J67styJzWPSNP3PCtzMC8RzCdmio2z78kdD6WFGEQ1fB3ftIKOph6%2Fy9tum4koxor6wkrTNs2TsOxDfdZyO59m793x4rinlCgZe84lQdMR4SCx%2BFSoNyRP31%2Br2zhedKztqd%2B%2BohWdFHPi8Dj9KfSvrVSKVhTi6rLy4P%2Bp9PreP1seIeV47T6EwehPk%2Fl6dmzEKK3pILuA5V%2FGwyrGNCIihEoMwgHWo9BZZ8ObQ4Opk1JES0tgitGayDZjp6p80oGTp2qkCtO5SJlTJnSbl%2BMnubwGqx%2Fq92aRIhdf2AjlOT6WyPOE8pj2z4sx62yNArLzWVEbLdAys6RxGmyz43bLUSH5SP8U%2BZBwwjMJa3%2F9IGOqUBAgK2VoycMGF1hd%2FgPHLA1SLQKQH1BG35%2FCmG3zWcYk3n4fGM4iT8V4dTBB%2Bitn75l851GbDUAtbTS0eh6dPiPjXI16vYkCD0hP8r2gA9zhNYX%2BemFmeCzWAFiunqSzzn3l0GlVBTtQvKzNRUpAubwWQipfeG2wTVMCRtQnykpUBaksxUYJUVMBUb0hCwdamaB6mpkK09T5p%2B1LW3WKS%2FkEAWPzue&X-Amz-Signature=87472ee427549a2614c88a2157ed7fcc098202f0fad3542c2f4211313df49f5b&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

各位同学们，大家好，我是小半仙，咱这一节开始正儿八经的电商项目改造了。那我们就从现有的电商业务当中 YY 出一个场景，那把这个场景集成到 stream 改造当中。比如说这里老是 YY 处的这个场景叫批量强制 logout 简单来说，咱构造一个接口，这个接口是 producer 它可以接收一大长串的用户 ID 并且在后台把这些用户 ID 分发到各自的 consumer 来把这些用户强制 logout 那咱要做的工作也非常简单，总共也就两步。


第一步我们对 authentication 这个微服务做一点小小的改动。这里的改动主要是针对删除 token 这个操作。 OK 那最后一步第二步就是我们要构造一个可以进行重试，并且在重试最终失败以后会流向到 fallback 降级流程的 consumer 好同学们，那咱抄起家伙准备开工。那按照剧本，第一个我们需要改的就是这个 off 服务咱找到 auth 服务里面专门用来删除 token 的操作，我们来看它藏在哪里，在 auth service 里面，我们打开它。它这第一步需要什么？需要 verifyverify 什么内容呢？它要看看你当前传入的这个 account 和它的 user ID 是不是相匹配的？ OK 那在咱这个强制登出的业务当中，为什么需要对它做一番改造呢？而因为我们强制登出只会提供一个 user ID 我并不会提供一个 token 这样一来，那你每次 verify 肯定都会失败了。好，所以我们这里要做一个改造，让咱的强制登出的这个请求到达 auth 微服务之后不做这一步检测，直接跳过去。


那怎么来改呢？很简单，我们打开这个 account 在这里面加入一个机关，那这个机关是叫 skip verification 好，那它的默认值是 falseok 那剩下的流程就简单了，我们先来判断一下这个 account is skip a verification 如果是 true 那是这么办。如果是false ，是那样办。咱下面这段逻辑是这样办还是那样办？下面这段是那样办在 else 里面。


好，那上面的这样版的这个逻辑怎么来啊？我们直接在 Redis 当中直接 delete 就好了。好，我们这里有两行 delete 咱 delete 哪个呢？同学们只用 delete 这一个 user token 就可以了。好，那我们再把这其中的公共的部分给它抽出来，公共部分就是这个它的最终返回值的构造。好，我们这里直接把这个 return 给它返回回来，然后把这一句删掉。这个 success 我们也可以简化一下，直接把它放到最上面。


好，那我们这个 delete 的请求就已经改造完成了。不过同学们有没有想到咱在这个 auth 服务的生成 token 的时候呢？我们往 Redis 当中插入了 user token 然后在 delete 的时候又删除到了 user token 那我们这 1 来 2 去，添加完了又删，但是却没有用它对不对？是不是发现咱这里漏了这样一步，用它在哪里用我们在 verify 方法里面，那在这个 JWT service 的 verify 里面，我们只是单纯的用算法对它做了一个 decode 它并没有去 Redis 当中检查你这个 token 是不是一个仍然有效的 token 比如说我在今天早上 10 点钟我创建了一个 token 理论上它到明天 10 点钟之前一直是生效的。但是我这个用户做了一些坏事，我中途被咱的这个系统管理员强制登出了。那这样一来，我这个 token 是不是已经失效了？没错，那这个 token 就不能再使用了。


不过我这个 verify 方法里，其实并没有去 Redis 当中检查你这个 token 当前的状态，所以他仍然会认为你是一个生效的 token 那我们这里添加一个 todo 这里要怎么样呢？检查 Redis 中当前 token 是否还生效好，怎么检查非常方便，你用他的这个 ID 只要能找到这个 token 就可以了。那如果你这个 token 在这里被删除了，那你在 verify 方法里面 100% 肯定是找不到这个 token 的，那就代表着 token 已经失效了。 OK 那这里我们用超快锰的方式完成了 auth API 的改造。那接下来我们就移步到用户微服务模块，来构造咱的 stream 集成的主体业务逻辑。那在微服务里面，我们可以把咱的 topic 还有 producer consumer 放到 web 文件夹下面，也可以把它给塞到用户微服务 user service 里面。那本着业务逻辑下沉的这种理念，我们尽量把跟 UI 层交互的部分放到 web 里面，那具体的业务逻辑咱都给它塞到 user service 里面。所以说我们这里就要把咱的 MQ 的 topic producer consumer 统统加到 user 微服务里面。好，那这里我们在加入这些业务逻辑之前，咱们要先把 dependency 在 palm 里面加上。


好，我们来看一下 user service 老师加入了两个 dependency 一个是 stream 那咱 stream 底层实现的是这个包使用的是基于 rab MQ 的 stream 那下面一个是 foodie auth API 因为我们在强制登出的这个操作当中需要去调用 auth API 所以才把它给拽了过来。那同学们还记得，咱不光这里，在 service 层里面把 user API 给拉了进来。在这个 foodie user web 当中，同样的也有这个 auth a PI 那这两个地方我们只留一个就可以了。所以我们这里也可以从 user web 当中，把这个依赖给它删除掉。


那咱接下来转移到这个 user service 当中，我们在这里创建一个包，那这个 package 的路径依然是叫 com.imock.user 那后面我们为了跟之前的 service 有所区别，我这里给它起名叫谁叫 stream okay 点击回车，先来这里创建第一个类应该说是一个接口 interface 咱的所有 topic 都是以接口的方式来定义的，它的名字叫 false lock upok 那这里和咱之前的 demo 是一样的。我先来声明一个 input 还有一个 output 那大家还记得哪一个是 consumer 吗？咱的 input 是 consumer 好，我们给它起名字叫 false lock out consumer 那下面的这个 output 我们给它起名就叫 false log out producer OK 接下来给咱的 consumer 创建一个 channel 它叫 subscribable channel OK 那它的名字自然就叫 input output the channel now 是 message channel 它的名称方法名叫 output 是不是定义完这两个之后还少了点什么？注解，我们别忘了给它加上这个input ，我们给它加上一个 input 注解，同时把 input 的大名给它附上。


OK 那自然下面的 output 我们要加上的是 output 注解大名，就是咱的 output 好，那到这里，我们的 topic 已经声明完成了，接下来是该创建 consumer 了。好，这里你有一个新的类，咱们把它就叫做 user message consumer。


Okay. 好，那创建完之后，我们先给它加上 sl four G 这是干什么？打 log 对不对？接下来咱要把刚才绑定的信道给它打通叫 enable bending 那这里我们把 value 给它括起来，这个 value 就是刚才我们创建的 class 的名称。


好，那下面我们就可以去写具体的业务逻辑代码。我们先说明一个方法， public public 谁 public 谁都不返回，然后它的名称就叫 consumer log up messageok 那它接收的参数是谁呢？我们简单一些，就接受一个 payload 就可以了。那我们可以认为这个 payload 就是一个 user ID 第一行先打一个 log 保持好习惯，每一个方法开头的时候，方便线上问题排查，那要打一行 70 的 log 好我们把这一个 UID 给它打印出来，叫payload。 Ok. 那接下来，我们就要去调用咱的 auth 方法，把它的这个 token 无效化。那调用方法我们这里就要去把谁给引入进来。


没错，就是我们的 off service 那这里我们要调用它的 delete 方法之前，我们要构造一个 account 对象，account对象还是沿用之前的 builder 模式我们声明一个 account the builder 然后在这里面把 user ID 给它传入进去， user ID 就是 payload 然后直接给它 build 出来。好， build 出来的这个对象直接塞进去就行了。不过在这之前别忘了咱前面设置过的一个 skip verification 对不对？要把它设置成 true 这样的话就会绕过你的 token verification 这一步。好，那这个方法的返回值我们用 of response 给它接收，接收过来之后做一个判断。


如果咱的这个 off code 不是 success 不是 success 怎么办？那说明，你这个删除操作失败了，那失败之后比较理智的做法是什么呢？那就是自暴自弃，我这里就直接 through 一个 runtime exception 老子不干了，处理不了叫 cannot delete user session okay 那这之前要留一个证据，不是我说不干就不干。是我确实没办法，这里要留一个 log 那我可以起名叫 error curd。
Then the letting user session.


再把它的 UID 也给它补上。 OK 还大功告成了吗？还没有，我们这里方法开头，如果想让它生效的话，别忘了要声明 stream listener 的 stream listener 他后面要跟自己的 consumer 的大名 false lock up topic okay 那这里就是我们的主体逻辑不过最后一步咱自暴自弃了之后，我们得有个办法再抢救一下。


那怎么抢救？咱前面说过，使用一个降级流程来把它抢救回来。好，我们这个降级就叫 public fall backok 那它的方法参数就不用细究了，直接来一个 message 最通用的方法参数，把它给接下来就可以了。把这个 message 没有 S 引用进来。好嘞，把饭先拿掉。好，那这里我怎么知道，这个 fallback 是接上面这个无可救药的 runtime exception ，那这里就要靠 service activator 那跟前面我们在 demo 环节讲的是一模一样的。好我在这里指定一个 input channelinput channel 是谁？是咱 topic 的名称，咱 topic 还没有定义，但是这里先给它名字给它起，好叫 false logup topic。Ok.那 topic 名称接后面跟谁跟一个 group 我这里要把它作为一个消费组。这样的话不管你上面声明了多少个 consumer 咱就是有 100 台机器。那你这个组内只有一台机器可以去消费这个 logout 的 message 好，那这个消费组的名称咱把它就叫做 false logout 后面跟 group 保持队形，然后再加一个点 errorsok 那这样一来我就可以去接收你的一场消息了。


好，那在开始我要打印出一行log ，叫 boss lock up build 把它作为 info 级别的。 OK 那剩下怎么办呢？剩下的就是八仙过海，各显神通了。同学们这样想，我们这是一个批量的登出操作，对不对？也就是说它的这个批量可能会非常非常多，比如几千个上万个用户的登出操作。那么请求到达我们的 producer 之后， producer 只负责分发，那每一个 consumer 在处理好了以后，那它的结果并不是同步返回给 producer 的，这是一个异步的请求。


所以如果出现了错误怎么办呢？那通常有这么几种方法，咱还记得前面处理过的这几种异常策略，有重试对不对？那待会儿我们会配置的在配置文件里面会把这一个给它加上。那重试的姿势可以有单机重试，还可以有 recue 那重新放回到队列当中。 OK 那除此之外还有什么其他操作我也可以加词信队列。对不对？我们把一个失败的消息给它转移到死信队列里面去。如果你不想配置一个死信队列，我们就可以用这种降级的手段服务降级。那服务降级怎么来做呢？通常来讲，死信队列表示我对你这个消息实在是没辙了，老夫处理不了，你去死信队列呆着吧。那服务降级就是说你还可以有挽救的余记，那这里面具体怎么挽救就要看各自的业务了。


那这里举一个例子，比如新零售发布库存，那它也是一个异步请求。那在这个异步请求当中，如果你后台的 consumer 处理失败了，我们怎么办呢？我们在降级流程里面会这样做，使用钉钉钉钉群的接口。那怎么样通知运营？这就是表示我需要人工介入。因为库存来说相对一个比较核心的电商场景，我需要立马通知工作人员进行人工介入。所以服务降级更多的是根据你当前的业务它的紧急程度或者你可以接受错误的这个严重程度来制定不同的降级策略。 OK 那我这里就搭一个空架子喽，同学们可以去自己在里面发挥，我这里也可以去发挥一下。想象一个场景，比如说你的强制登出失败了，但是我就无法从你的 session 或者是 Redis 里面把你的用户 token 给它删除掉。那这怎么办呢？那我的强制登出业务，就可以转变为另外一个业务场景叫 inactive user 把你的用户直接给 inactive 掉。那这有可能需要大家去怎么做呢？我在 user 的表上面加一个 flag 那这个 flag 就是 active 还有 inactive 这样的标记。


那如果咱 user 表上面的 flag 是 inactive 那表示你当前用户已经被禁止了，那禁止了之后怎么办呢？那下次登录的时候，我就不让你下次登录了，我直接给你返回一个错误，比如说叫当前用户已被禁止这样是不是一个降级流程的思路。 OK 那我这里只跟大家探讨一下场景后面的流程，还要同学们自己来处理。
那接下来，我们就要去配置这个配置文件了。 foodie user service 已经完工了，这个配置文件我们要找到 foodie user web 打开它的 application 杠 DEV YAML 文件。然后我们看到这个文件里，我们已经给 stream 留下了这一席之地。好， stream 的配置它是坐落在 cloud 下面的，那是 string 下面的 cloud 再下面才是 stream 所以我们这个对齐方式要注意，前面留两格。


好，这里写 cloud 另外换一行写上 stream 好 stream 下面我们先来配置咱的 bindings 前面绑定了几个信道第一个是我们的 consumer false lock up consumer 好，这里把它配置一个 destination destination 就是我们 topic 的名称叫前面配好的是 false log up topic 同时给它指定一个消费组，它叫 false log out group 消费组指定好之后我们再来给它设置一个重试的次数。 consumer 的 max attempts 是三次。好了，其实默认就是三次，我们可以给它设置的稍微短一点两次。
OK consumer 配置好了，接下来给 producer 也指定同样的一套流程，first log out producer 它的 destination topic 的名称也是一样的。 OK 那到这里就配置完成了。那咱在这个配置里就采用了重试加上 feedback 的流程。那咱接下来就要配置最后一步了。


创建 producer 准确的说应该是创建一个 controller 来使用这个 producer 好，我们接下来找到它的 passport controller 那这个 controller 是控制用户登录、登出以及一系列操作的地方。那咱要找一个地儿，把它给添加进去。找谁就找 logout 把这个方法给它复制一下。好，复制到最下面，那开始改造了。这个名称，我把它改成叫 false logoutok 那它其实并不需要你的 request response 这里都不需要它只需要一个什么呢？一个 user ideas 好，我们约定这个 user ID 是以这个逗号分割开来的一串场字符串，这样的话约定比较简单。 OK 那它的 post mapping 我们也把它改成 false logout API 的说明，叫用户强制退出登录。 OK 很霸道的名字。对不对，那我们把这里的逻辑统统给它删除掉。在这里主体逻辑部分我们先来判断一下，如果你的当前的传入参数不为空，那我给它加一个判空操作。 its not blank 不为空怎么办呢？我们这里就直接采用最简单的方式，给它做一个循环 use UID 然后把这个 user ID split 一下。


那 split 好之后，咱就直接可以把这个消息给它怼出去了，怎么怼？好，我们把文件转到最上面，这里要 auto wire 的一个家伙进来谁 producer 对不对我这个 producer 的名称就是叫 false log in topic 好，我们给它起名就叫 producer 一切从简，好在滚到下面。然后 producer 我们先把它的 output 拿出来，这就是它的 producer 然后调用一个 send 方法。


send 什么内容呢？我们最简单的就直接把这个 UID 作为 payload 给它发送出去。 message builder 把这个类给它构造出来 with the payload 把 UID 塞进去。好嘞，这里调用一个 build 完事了。每次发送之前，别忘了保持一个好习惯，打一行 log send log out message 并且把这个 UID 给它带上。 OK 那这个方法看起来是不是有那么些简陋啊？没关系，咱高效的方法看起来就是这么枯燥且朴实无华，那咱再普适无法也要保证一个安全性。


对不对？当前的这个 controller 可是可以暴露给前端用户访问的。那也就是说我的一个终端用户可以随意构造 user ID 来清空别人的登录信息。所以我们这个 fix me 里面要让大家去做一件什么事，将这个接口从网关层移除出去，不对外暴露。


好，那咱的开发工作就结束了，那接下来我们只用把 user application 给它启动起来，然后尝试从 postman 发送一个请求，测试一下结果就可以了。 okay 那除了这个 user WAF 以外，咱的 auth V 服务我这已经预先给它启动起来了，那我看一下这个 user wave 服务。好，这里已经显示 started 我们把 log 清空一下，转战到 postmanok 在 post one 里面我们尝试往 userway 服务中的 passport 后面跟 false log out 发送一条指令，这个指令带有一个查询参数 user ID S 这个查询参数里面，我们通过逗号分隔了这几个 user ID 那都是仿造的。


好，我们这里点击一下 send OK 这里已经返回了结果。那我们回到云台的这里瞄一眼同学们看这里，先是 send send send send 四条发送。那紧接着下面 user message 这里也有 4 条接受。 OK 那这个低调且朴实无华的接口就已经测试完毕了。


其实借助 message Q 可以，玩转很多的花式应用。小伙伴们也可以充分利用这一节学习到的业务知识或者技术知识来挖掘一下当前应用哪些场景，可以利用 rabmq 做更好的解耦。然后提高可用性和接口的吞吐量。 OK 同学们，那这一小节内容就到这里结束了。我们下一小节再见。




