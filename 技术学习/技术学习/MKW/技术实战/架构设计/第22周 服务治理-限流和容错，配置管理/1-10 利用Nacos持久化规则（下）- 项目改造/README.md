---
title: 1-10 利用Nacos持久化规则（下）- 项目改造
---

# 1-10 利用Nacos持久化规则（下）- 项目改造

[image](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/b4cee298-8199-4aa3-9d06-136463f47f2e/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZHWOYAQR%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T231421Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIEwQ4UPlGQA1sTN64UevW1cNt193B%2FQ%2B8VUE8ftpcOuBAiBVtFWcHoTFK9YFUPIPj3bpJvgSZ201rcItBdHaHhFYXCqIBAjG%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMlh8Lz2G8Q7SHthAkKtwDx00rZUXpIeurSOIS6ys0ut8x1Vhzmh2QqHIsJoLqkPbuyTj4OGWJVqEnoO1bztIkNrBa4UdleVav06WAriISXBjzGG5MnE%2FZmKixof7a9yWUJ9PniGLX2OWmUcsF7jilylZlXy6x9rWWcEaIJj1LFJUgT3qoSnUf3R8WytXvnVHbOd3HRLi6mizB4TWOlN%2FDxW4%2BEb9FVr9KF3x6vPDsB5kmOC8%2Fxi4AUUNp1Lmg3LZa%2Bo6lGhOz5nOsB7c%2BILpA4pELqmrcz%2FiOm9bVNo4e9%2B2gNsS3o7LUIRAmz9nfMUQKYAiURmXp9kNwC6w%2BwLeOZnUqX80ji0w2JlfXsrUKLT0eeYX24rlbqoS32tyLx7RfQnolIx1phYa73a3QAwCH2c6%2BN%2F%2Bru0kfDo%2F9pEJtm9bFGe2fsg9UT%2BPUxu%2Be1mk%2FnU6vj%2FYAgPHinEgXU0%2FiDwBVADKh2QSs4hIbbj8igdP3oMZ44JGA6jl59Vosp6I9d6awjJOcsZBIfzutHYSfeQtXKvKvapsu7zedVNueWXHBkHwooo7zfE0X3Q0QptkhQbjwWsn%2FK6Cjh0ZmUG1aWC49LxCXHsmy9TgXJ%2BxtBUzb9tPxERGBAq4%2FIfUqhGnJ9PmkFF4QLrqBx7kwwbr%2F0gY6pgFtr7ESmz4008RxIuBmF%2FHmoPUKlqpd2GkUOQBSgmRM3vPam3o8zRoANPIOrxVeH6Z4bmsR2J2%2FfnB8SsPZ8eSI9UCJRsvS0z77Cyx0S5rGurSIIZG82aZdQG6P1z%2BrZWU73shZZ1EXexMGYdlr0xn9LwaqCVWLwkl%2Bs6m%2FP6eMCJIxScOGUZ5B9SVRptdv1Z8ekt6mL5o7XDIELe1QmyttMi2Zlqec&X-Amz-Signature=680d181f1a392d2e272d8e90a5a69cb09a02b83ef6fa019d40c41779f4c85485&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

[image](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/54453834-8f87-4d53-97e4-9b807adf49a5/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZHWOYAQR%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T231421Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIEwQ4UPlGQA1sTN64UevW1cNt193B%2FQ%2B8VUE8ftpcOuBAiBVtFWcHoTFK9YFUPIPj3bpJvgSZ201rcItBdHaHhFYXCqIBAjG%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMlh8Lz2G8Q7SHthAkKtwDx00rZUXpIeurSOIS6ys0ut8x1Vhzmh2QqHIsJoLqkPbuyTj4OGWJVqEnoO1bztIkNrBa4UdleVav06WAriISXBjzGG5MnE%2FZmKixof7a9yWUJ9PniGLX2OWmUcsF7jilylZlXy6x9rWWcEaIJj1LFJUgT3qoSnUf3R8WytXvnVHbOd3HRLi6mizB4TWOlN%2FDxW4%2BEb9FVr9KF3x6vPDsB5kmOC8%2Fxi4AUUNp1Lmg3LZa%2Bo6lGhOz5nOsB7c%2BILpA4pELqmrcz%2FiOm9bVNo4e9%2B2gNsS3o7LUIRAmz9nfMUQKYAiURmXp9kNwC6w%2BwLeOZnUqX80ji0w2JlfXsrUKLT0eeYX24rlbqoS32tyLx7RfQnolIx1phYa73a3QAwCH2c6%2BN%2F%2Bru0kfDo%2F9pEJtm9bFGe2fsg9UT%2BPUxu%2Be1mk%2FnU6vj%2FYAgPHinEgXU0%2FiDwBVADKh2QSs4hIbbj8igdP3oMZ44JGA6jl59Vosp6I9d6awjJOcsZBIfzutHYSfeQtXKvKvapsu7zedVNueWXHBkHwooo7zfE0X3Q0QptkhQbjwWsn%2FK6Cjh0ZmUG1aWC49LxCXHsmy9TgXJ%2BxtBUzb9tPxERGBAq4%2FIfUqhGnJ9PmkFF4QLrqBx7kwwbr%2F0gY6pgFtr7ESmz4008RxIuBmF%2FHmoPUKlqpd2GkUOQBSgmRM3vPam3o8zRoANPIOrxVeH6Z4bmsR2J2%2FfnB8SsPZ8eSI9UCJRsvS0z77Cyx0S5rGurSIIZG82aZdQG6P1z%2BrZWU73shZZ1EXexMGYdlr0xn9LwaqCVWLwkl%2Bs6m%2FP6eMCJIxScOGUZ5B9SVRptdv1Z8ekt6mL5o7XDIELe1QmyttMi2Zlqec&X-Amz-Signature=57c39527e1d5ef402a1ff3e68bb359b0eff2d643c6602d8ce16484d46fd62911&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

哈喽，幕后的各位同学们大家好，我是姚半仙。那我们这一节继续咱上节当中的内容，做这个 NICOS 持久化规则的下半场。这里我们将跟同学们一起去把限流这部分的规则做一个联动改造，让我们的应用可以从咱的 next 这里把这个限流规则拉到本地，然后生效。okay，那我们这里就 intelligent 里面走起，写 bug 的每一天都是超越自己。


同学们，我们这里首先做一个改造，当然要先从它的依赖项开始。那咱这边打开我们 restroom service call 当中的 palm 文件，在这个 palm 文件当中我们前面已经添加了 Sentinel 的注解，咱在这个 sentinel 下面再去添加一个特殊的一个依赖项，来我们这里的 group ID，它跟前面不太一样，前面都是阿里巴巴Claude，那咱这边要添加的这个 group ID 是com。点阿里巴巴它不是 Claude 了，它是CSP，那它是 CSP 下面的 ARTIFACT ID 是 Sentinel 杠 data source 杠necklace。


okay，那我们把这个项目引入进来之后，把这个 maven 重新 reimport 一下，把这个依赖项加载进来。那同学们这边如果你是想使用 neckles 作为它的 data source，那这边引入的就是neckles，那对应的我们可以点进去看，点到它的父类。那如果你这边想去引入zookeeper，阿波罗Redis，那它这边都有不同的依赖项，可以让我们来去引入。


okay，好，那我们回过来，实际上这个包儿它并没有完全的包含在 spring Claude STARTER，阿里巴巴 centenal 这个包儿下，所以如果我们不把这个包引入，你在启动过程将会爆出一个 class not found 这样的异常。


那咱这边把这个依赖项引入进去之后，接下来咱去到配置文件当中去做一个小修改，不用改任何代码，咱这次只是配置文件的一个改动。配置文件改哪里？自然是咱的这个 Sentinel 这一部分，我们要让 Sentinel 去从 neckhouse 这里去拉下来这些限流的规则。


好，我们定位到sentinelle，okay，在这边，那我们接下来在这个 transport 这里不是指定了咱的 dashboard 吗？那么我们在下面一行跟 transport 同级别，咱去指定一个 data source，okay，那同学们看到这个 data source 这一个对象，它里面是一个什么形式？ map 形式，那所以我们的这个 intelligent 里面，它不能提示出这种 map 形式的数据，所以接下来的这些东西要大家自己来手，打不过打什么内容？同学们其实可以从这个 sentinelle 的这个类里面，你看 data source configuration 这个类里面略知一二，那这些变量相当于说是咱的这些什么呀？这些值，你要是连接 next 就用对应的这个 next 作为对象属性。你要是连接 Redis 就用Redis，那这边可以去参考这里面的具体数值，连接串等等。


okay，那么我们回过去到这个 data source 里面跟同学们一起来打了，那咱说过这是个 map 形式对不对？这个 map 的 key 是什么呀？ key 就是我们的限流flow，同学们如果后面想去同步更多的规则，降级规则、熔断规则等等，那么这里可以去用前面在上一节当中，老师跟同学们讲过的方式，自己来改造一番。


好在 flow 这里我们对应的 data source 是谁？咱前面说过这个 key 对应的这个value，在这里面我们连接的是neck，对不对？所以我们这里要写上它的 value 对应的这个值是neck。 next 这里的细节属性有很多，那我们这边去具体添加哪一个，我们来看一下。


在 next 这里，首先你这个 server address，这是必要的，对吧？你当前 next 连接到谁，那你不指定它，你就连接跑偏了，对吧？这是第一个很需要的。然后后面这个对应的 group ID，我们也需要对它做一个小小的定制。因为咱前面在 Sentinel dashboard 里面，其实插入的 group ID 是一个特殊的叫 Sentinel group，所以我们这里要从这个 default group 给它做一个变更。然后面对应的这个 data ID 也是我们需要做一个变化的，我们这里将要从一个特定的规则里来去拉取，这是个配置文件，那这个规则是什么？待会儿我一写，同学们就能回想起咱上一节讲的内容了。


好，我们这里返回去。在这个 necklace 这里，我首先添加 server 点 a d r address，因为它这个没有自动提示，所以同学们要稍微注意一下，不要把它填错了。好，那 Server address 这里写完之后，我们接下来再写 group ID， group ID 就是我们 dashboard 添加的 3 TINELL 下划线group。


好嘞，对应的还有一个 data ID，这个是我们后面章节的内容，这个配置中心的内容咱这边先不去深究，我这边把这个 data ID 直接写在这里，它是使用了一个通配符，然后后面跟 spring application name 再加一个什么呀？同学们，这里应该就能回想起来咱上节说的一个内容， flow 杠 rules OK，是不是有点眼熟啊？同学们，有没有想起来咱上一节我给大家来看一下，咱在这个流控规则里面我们定义了一个什么呀？一个config，对吧？咱再看这个 Sentinel dashboard 这个类，咱同步的 neckles config YouTube 里面你看 group ID 写成了 Sentinel group，然后对应的这个flow，它 flow 的 data ID，我们这里是什么呀？ flow 杠rules，然后前面跟的就是 application name，那这是我们在上游定义的这样一个规则，所以说我们下游应用这里要采用同样的规则来去获取数据，否则的话你这个 data ID 配错了，它数据是获取不到的。


那大家如果这边想要定义其它规则， system 也用neckles，那这就是一个给同学们的小作业，不光要引入限流，我们还要引入降级等等其他的规则。那就在上游这里，我们把规则的 data ID 定义下来，把这个 pattern 在你的具体项目当中把它给沿用一样的模式。


okay，那咱这个配完了 data ID 之后，我们接下来再来配一个叫 root type。好嘞， root type 这里我们定义的是什么呀？定义的是 flow 对应的这个限流这样的规则。接下来我们就把这个应用把它给启动起来，那启动之前尽可能的整体做一个编译，以防一些宾译问题或者报错。在启动咱的应用之前，咱要把这个 necklace 这里给启动起来，与此同时也要把这个 sentinelle dashboard 也给它启动起来。那这两个启动完，我们接下来回过来去找到它的孟函数，直接把它执行掉，就以 run 的形式好了。我们这里不做源码深究，我们就不用 debug 模式了，然后打开小说板，看到这里没有什么报错，哎，非常好，好到这边似乎已经完成了，那我们走到咱的浏览器这里刷新。


OK，那在这个 restroom 这边，我们随意的发起一个调用，就调用 get available，然后让我们的这个监控节点在这个链路当中出现。OK，那出现好了之后，我们不要在这边去添加流控，咱不要在这边添加，添加完之后它不会自动出现在这个流控规则里，它会出现在这个下方的这个 in memory 内存的流控规则。那如果想要同步 next 的流控规则，咱这边要费点事儿。把这个资源名 copy 一下，点到流控规则 v one，然后去添加一个新增的流控规则好， check available，然后对应的单击阈值我填写一，然后高级选项这里默认是直接流控快速失败。


那在做这个流控之前，我们可以看你点击这个 send 没有问题的，对吧？他没有被流控，那我这边点击一下新增，新增完之后我刷新一下这个页面，诶，出来了，对吧？然后到这个 negos 这里也去看一眼，好样的也出来了，那看一下详情，里面对应的这个规则里面的 count resources 是 check available，对应的 count 是一。OK，那咱这边去再次调用一下 postman 看看效果。


没事儿，走，点击快点儿，同学们，看到它就被降级了对不对？返回了一个空，那这是为什么捏？同学们，别忘了咱这边在代码里面配置了当前 resources 的一个 fallback 属性，对吧？它这边被降级之后，被限流之后，紧接着去达到了这个 fall back，好，那这个就是我们想要达到的一个效果，对吧？限流的效果，为了验证我们这个是持久化的规则，我接下来把这个应用给它停掉，我给它 stop 掉。


stop 之后咱可以看到在你的这个配置项里，在 next 的配置项里金枪不导，对吧？这个配置项还是很刚的躺在这边，那我们接下来把这个应用把它停掉之后，再重启一下，来看一下应用会从 neck 当中自动拉取这个同步规则吗？好，这边点击启动，那稍等片刻，它启动起来之后，如果是一个持久化的规则，它应该是默认自动生效的，对不对？好，启动起来了，我们小心翼翼的再来点击一下，走，好，没有事儿，那我们点击快一点走走。


哎，同学们看到吗？对应的，我点击一块，它这个限流规则自动生效了，变成了 fall back，对不对？OK，那所以说我们这个持久化的限流规则也就已经把它实现了。那同学们这里也可以做一些额外的测试，去从各方面来佐证它这个持久化规则。比如说我们把应用停掉，对吧？然后在这个 neckles 当中，或者在 Sentinel 当中把这个持久化规则变一下，把它的内容给它变一下，然后再去启动应用，看一下它是否可以拉到变更过后的内容，那这都是大家可以在本地做的实验。


当然那这一节当中比较想让大家做的一个动手的小作业，就是说我不光想要同步流控的规则，流量整形规则只是一部分，那咱在这个 sentinel parent 里面，我还希望让同学们去把这些降级规则、系统规则、黑白名单等等，我把它全部同步过来，所以说大家这里需要自己进一步的做一些开发。


那这一步怎么做？很简单，第一个我们首先要去定义对应的 flow data i d post fix 定义这种规则，然后紧接着我们在对应的实现类里面，我们创建不同的这个 rule necklace provider，咱这边创建的是 flow rule，那我们接下来可以创建一些像具体的降级规则的类，把这些都定义成provider，然后在下面去定义它获取资源的方式，那我们这里是从 config 这里通过 APP name 加上这个 prefix 来去获取的。那么我们这里对应的这种模式就要把这个 prefix 从这个 flow data ID 替换成咱后面新加的一些其他的ID，那就通过这种方式把 next provider 给它偷梁换柱替换掉。


然后在对应的这些 controller 里面，比如说我们这里使用的 Controller VG，在这个 flow Controller v two 我们是做了一个具体的类的替换，那同学们就可以也仿照这种类似的形式来去定义自己的其他的各种规则，那也可以对它当前的这个 flow Controller 做进一步的改写，对吧？可以在这里面动态地加入很多不同的配置项，然后在这个配置项里面，根据它的参数，不同路由到不同的 data publisher，还有 data provider，但是这个配置过程还是需要花一些功夫的，这里建议大家想深入学习的同学可以去往这个方向上走一走。


那这是后台的部分，那对于页面的部分其实也是有一定的工作量的，那在这个 set bar 里面，我们是使用了 data board 点 flow 这个方法来去做相应的配置，那么咱这里也需要研究一下它的这些 GS 代码，把这个前端和后台都给它联动起来，那这剩下的工作量还是蛮大的，那相信大家这一个作业估计花上一两个星期都是很有可能的。
OK，这里就跟同学们讲到这了，咱下一节当中跟大家再去了解一下，咱 spring Claude 当中还有一个更加轻量级的降级熔断的组件，那是一个客户端的 high streaks 组件，那相比 Sentinel 它这边是要轻量级简单得多，那同时也不用部署一些额外的中间件来去支持它的这个应用。OK，同学们，那我们下一小节再见。


