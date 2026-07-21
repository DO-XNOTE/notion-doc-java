---
title: 2-13 [Demo]限流组件封装（一）- Redis + Lua
---

# 2-13 [Demo]限流组件封装（一）- Redis + Lua

[image](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/f310e981-58be-4765-8f36-0ab1c669a39d/SCR-20240808-iulm.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665BWHEADZ%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T225505Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIBDZOSmL2hwlKO9QQ4bVZW4jnj2Gzd%2BXa00tGyS3OJqyAiBT8LbH%2Bpy04Ql3YUpANzB93VdTPa3fae6%2FwQaDD8kKyCqIBAjG%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIM6W9MC3hLvesPxdKuKtwDxgpMnIWyB173Box5yGSkErwACDmlFjAtYlxels1EoIbsxFqRt8rvDdFQHzT%2FkZeXScid45D%2B0%2FMAbFQiiMs98%2FSDmKS%2F8IMCJV4FLCQIiGr24jWfpQgD6kA4e2Vi9Y7wShv29yA7q1vRRi8rg2CftUokVD4yhaZRXvggfczn7NlCDJnLKeFPf6URlF1Z7ds7Wvt%2BAu5M%2FJxjH0ALAUeM78olOyYaf5qQy%2Fn%2FDgeoi55l4edEDXcGZKqsYHhoObPgQ4GgM0nYEkrh%2FvfONU2qiEUPe2BZ3CurBs3TBnDw69YSwCMUqV5tumaFdTeO2E1SMPMT4ACm3szvucx9qgjQN50MW0lu%2BrkmOjqssW7hZnpM8Ulymf36nR705BkL0WthXnXy%2Fl7dlyYlTcOlgX5bqvuzcYgVlGdGTn5kvIF%2Bxd%2Bp6hqWD6xHFyUHyBZTP%2Ft%2FcfdaMy18icmTzigFEsBXOJdNuC7Lph2r%2F0log1AItN9G0rAvI41QQfkSVul0eKfjt4umDd03CNHcFLWnwok29ApgwI0iyHWXz4Lsd1ddt036DniEd6lAm3CF3thd%2BxI%2FOP9shgOHY7RxtduJ6rmD1pNV016F2s88e8USeLKoZA0GO2vw%2Fyz4J7UHgSgw3bf%2F0gY6pgGlWfPZ%2BeEzSzA96mhV5QcJzvWuQ5raQRwaOT0cZ9dvYwADVU2Vs4DS%2Fkc%2B78lU0lpPpJH7xXEo27kCpat46pvGMhK97PivG4EhdbWrE51QhQZBCnl1Xjtq0R%2B%2FysyfFYaEzFkuS%2F6DtLUYJoRHpLAeHRMEbW2YFu1V9VMpbwLCnLXlEt4ewh4N31%2FyYTdkqaZ%2FWTOSxDrHJO4LICbWy%2BuaYVeXVwaL&X-Amz-Signature=d58c2b01481d0ab36b6a61c7aeb4ea0976017c992f9f0462e1dc0b24f991e18e&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

[image](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/237517ea-e2cd-4360-888e-2aaf1f56ab3f/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665BWHEADZ%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T225505Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIBDZOSmL2hwlKO9QQ4bVZW4jnj2Gzd%2BXa00tGyS3OJqyAiBT8LbH%2Bpy04Ql3YUpANzB93VdTPa3fae6%2FwQaDD8kKyCqIBAjG%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIM6W9MC3hLvesPxdKuKtwDxgpMnIWyB173Box5yGSkErwACDmlFjAtYlxels1EoIbsxFqRt8rvDdFQHzT%2FkZeXScid45D%2B0%2FMAbFQiiMs98%2FSDmKS%2F8IMCJV4FLCQIiGr24jWfpQgD6kA4e2Vi9Y7wShv29yA7q1vRRi8rg2CftUokVD4yhaZRXvggfczn7NlCDJnLKeFPf6URlF1Z7ds7Wvt%2BAu5M%2FJxjH0ALAUeM78olOyYaf5qQy%2Fn%2FDgeoi55l4edEDXcGZKqsYHhoObPgQ4GgM0nYEkrh%2FvfONU2qiEUPe2BZ3CurBs3TBnDw69YSwCMUqV5tumaFdTeO2E1SMPMT4ACm3szvucx9qgjQN50MW0lu%2BrkmOjqssW7hZnpM8Ulymf36nR705BkL0WthXnXy%2Fl7dlyYlTcOlgX5bqvuzcYgVlGdGTn5kvIF%2Bxd%2Bp6hqWD6xHFyUHyBZTP%2Ft%2FcfdaMy18icmTzigFEsBXOJdNuC7Lph2r%2F0log1AItN9G0rAvI41QQfkSVul0eKfjt4umDd03CNHcFLWnwok29ApgwI0iyHWXz4Lsd1ddt036DniEd6lAm3CF3thd%2BxI%2FOP9shgOHY7RxtduJ6rmD1pNV016F2s88e8USeLKoZA0GO2vw%2Fyz4J7UHgSgw3bf%2F0gY6pgGlWfPZ%2BeEzSzA96mhV5QcJzvWuQ5raQRwaOT0cZ9dvYwADVU2Vs4DS%2Fkc%2B78lU0lpPpJH7xXEo27kCpat46pvGMhK97PivG4EhdbWrE51QhQZBCnl1Xjtq0R%2B%2FysyfFYaEzFkuS%2F6DtLUYJoRHpLAeHRMEbW2YFu1V9VMpbwLCnLXlEt4ewh4N31%2FyYTdkqaZ%2FWTOSxDrHJO4LICbWy%2BuaYVeXVwaL&X-Amz-Signature=748a7171f515d17538c5259f5def7d019eac9aefb4879ce615aca906791e0a65&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

hello 我们课网的各位同学们，大家好，在前面的 demo 当中，我们学习了 Lua 的基本用法，也学习了怎样把 Lua 组件植入到 Redis 当中，通过 Redis 命令来运行 Lua 脚本。那接下来我就要展现真正的技术了。在这一节和下一节里，我将要封装一个限流组件。这个限流组件的最终体现形式是一个 annotation 注解，我们只用在服务层里轻松地加上这么一个注解，那你的方法就自动具备了限流功能。和 N jacks 最大的不同是，这个注解它非常灵活，你可以安插在方法中的任何地方，只要确保这个方法的调用点可以被 spring AOP 机制拦截就可以了。那下面我们一起看一下这一节的内容都有哪些。

[image](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/c3522b0e-cd9b-4aaf-a327-c57ea0226148/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665BWHEADZ%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T225505Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIBDZOSmL2hwlKO9QQ4bVZW4jnj2Gzd%2BXa00tGyS3OJqyAiBT8LbH%2Bpy04Ql3YUpANzB93VdTPa3fae6%2FwQaDD8kKyCqIBAjG%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIM6W9MC3hLvesPxdKuKtwDxgpMnIWyB173Box5yGSkErwACDmlFjAtYlxels1EoIbsxFqRt8rvDdFQHzT%2FkZeXScid45D%2B0%2FMAbFQiiMs98%2FSDmKS%2F8IMCJV4FLCQIiGr24jWfpQgD6kA4e2Vi9Y7wShv29yA7q1vRRi8rg2CftUokVD4yhaZRXvggfczn7NlCDJnLKeFPf6URlF1Z7ds7Wvt%2BAu5M%2FJxjH0ALAUeM78olOyYaf5qQy%2Fn%2FDgeoi55l4edEDXcGZKqsYHhoObPgQ4GgM0nYEkrh%2FvfONU2qiEUPe2BZ3CurBs3TBnDw69YSwCMUqV5tumaFdTeO2E1SMPMT4ACm3szvucx9qgjQN50MW0lu%2BrkmOjqssW7hZnpM8Ulymf36nR705BkL0WthXnXy%2Fl7dlyYlTcOlgX5bqvuzcYgVlGdGTn5kvIF%2Bxd%2Bp6hqWD6xHFyUHyBZTP%2Ft%2FcfdaMy18icmTzigFEsBXOJdNuC7Lph2r%2F0log1AItN9G0rAvI41QQfkSVul0eKfjt4umDd03CNHcFLWnwok29ApgwI0iyHWXz4Lsd1ddt036DniEd6lAm3CF3thd%2BxI%2FOP9shgOHY7RxtduJ6rmD1pNV016F2s88e8USeLKoZA0GO2vw%2Fyz4J7UHgSgw3bf%2F0gY6pgGlWfPZ%2BeEzSzA96mhV5QcJzvWuQ5raQRwaOT0cZ9dvYwADVU2Vs4DS%2Fkc%2B78lU0lpPpJH7xXEo27kCpat46pvGMhK97PivG4EhdbWrE51QhQZBCnl1Xjtq0R%2B%2FysyfFYaEzFkuS%2F6DtLUYJoRHpLAeHRMEbW2YFu1V9VMpbwLCnLXlEt4ewh4N31%2FyYTdkqaZ%2FWTOSxDrHJO4LICbWy%2BuaYVeXVwaL&X-Amz-Signature=aa5903c1ff181a47239b82e06d4b4540a8c965c773fd00129af619830c76a6fc&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

首先我们编写一个 Lua 限流脚本，当然了大家也是刚刚接触 Lua 所以这个限流脚本非常的简单。那写好了限流脚本以后，我们就要通过 string data Redis 组件集成 Lua 和 Redis 这里面包含两个步骤。第一个步骤，我们使用 default Redis script 来加载 Lua 脚本。在这一步当中，我们将把路 2 脚本上传到 Redis 并且拿到一个 ID 那么往后只用去调用这个 ID 对应的脚本就可以了，再也不用重新上传。那第二步就是配置一个 Redis template 来调用 Redis 服务。当 load 和 Redis 都已经集成妥当了。然后我们就在 controller 里添加一个测试方法，验证限流的效果。 OK 同学们准备好的话，那就抄起家伙，咱 teddy jelly 开工了。好嘞，同学们要开工了。


前面咱们编写的 Lua 和 rate limiter 这两个项目，我把它重新规整了一下，放到了这个 rate limiter 文件夹下。那咱接下来这一节和下一节要编写的内容也都放在这个文件夹里了。 OK 那现在我们先创建一个 module 这接下来是要写一个注解，对不对，作为一个公共的组件，可以应用在电商项目当中。所以我们给这个注解起名 artifact ID 就叫做 rate limiter 杠 annotation 好了，名字随意发挥，和这个 module name 和前面保持一致，然后也把它扔到哪个文件夹下。咱刚才创建的 rate limit 这个文件夹下面 atti finish 好，收起小桌板，我们开始写 palm 文件。在一开始给它指定一个 packaging 的类型是价包。 OK 那接下来给它添加 dependency 都有哪些？ dependency 需要添加，咱注意这是一个什么？这是一个 annotation 是需要在不同的 module 之间公共使用的一个 shared 包。所以它的 annotation 不宜引入过多长，怎么样？你不用的 dependency 一定不要引入只引用那些需要用到的，比如说需要用到的有哪些。


第一个，我们要给它加一个 Redis 的配置。那这个 Redis 我们采用谁呢？我们跟前面的章节选用的 Redis 组件不一样，我们用 org spring framer boat 下面的这个 Redis SaaS spring data 大家都用过吗？没用过，肯定也听说过。那 spring data 里面同样也有对 Redis 的支持，那它叫 spring boot starter 然后后面是再来一个杠 data 杠 redisok 把这个注解引用之后，我们还需要引用另外一个注解。这个注解是初级程序员面试，非常容易被问到，几乎是必问的。我记着我刚毕业第一家公司，人家就问我，请说你对 AOP 的理解，当时准备工作做得足，我足足给他理解了半个小时，然后就过掉了。


接下来一个注解就和 AOP 有关，叫 org spring from milk.boot 下面的 artifact ID 是 spring boot starter 后面就是 AOP 其实像我工作这么久了再回过来看。 AOP 在当年十几年前还是一个非常先进的理念，在当年也是个很玄乎的名词。就像我们现在说起高可用 HA 还有像服务治理这些名词概念一样。那如果我们用现在当今的眼光来看，那 AOP 概念是不是太简单了，随便挑一个 Java 程序员都能洋洋洒洒说上很多很多。所以咱用发展的眼光看问题，你现阶段看起来那些很难的技术听起来很晦涩难懂的概念，随着你工作经验增加，你过个三五年再回头看，真的也就是那么回事。


技术这种东西，从咱做业务应用的角度来说，都是非常亲民的，没有什么很高的学习曲线。 OK 那接下来我们给 rate limiter annotation 添加一个包，那就开始我们的编码了。这个包的名字我先给它起名叫 arm.imock 后面跟 spring cloud 虽然咱还没有进入 spring cloud 章节，我这里先暂写齐 spring cloud 所以待会儿同学们如果要引入到商城项目的时候，记得扫包要配好这个路径，因为这个路径跟你商城项目的路径是不一致的。


OK 那我们创建好了这个包以后，那接下来创建一个什么类呢？一个最简单的 service 我们待会要把它改造成annotation 。所以我们先来写这个业务逻辑叫 access limiter 好在这个类里面我们做什么事儿？那接下来要在里面写方法啦，我们这个方法给它起名叫 public avoid 什么都不返回，因为它就是一个限流，我业务层根本不关注你怎么限的，你只要在这里，能把我不合理的请求拦截掉就可以了。这个方法名称就把它叫做 limit access 好，那这个参数是什么？你对我方法限流对吧，你要告诉我你方法的特征是什么，不然咱这整个应用的所有方法那都是共用一个限流标准了。所以这里要告诉我一个 key key 就是你方法的身份标识。


然后你告完我 key 之后，你还要告诉我一个 int 类型的包装器，这个包装器是什么？是 limit 也就是说你想让它过去一秒钟被限流多少次，因为我们这里简化一个配置，我这里不用像 NGINX 里面这么复杂的控制，比方说它还可以控制一小时多少个，1分钟多少个，咱就以秒为单位。你这个 limit 就是告诉我一秒钟之内你想让它最高可以通过多少个请求。好，那方法体非常简单，party我先跟他加个 step one step one 是 request Lua script 你要调用 Lua 脚本，然后这个 Lua 脚本返回一个什么呢？返回一个布尔值叫acquire。 Acquired. 就是说你当前这个方法有没有达到它限流的阈值，如果你没有达到，我让你继续访问。如果你达到了怎么办？那在这里办。如果你达到了，就 acquire 你没有获取到访问条件，加一个反这里同学们可以自由发挥了。


我简单来做就是直接扔出一个 exception 这个 exception 我们就把它简单封装一下，就叫 runtime exception 给它起名叫 your access is blocked 或者 your access is limited 都可以随便大家起在上面给这个方法加一个 service 的 annotation 同样加一个 sl four G 那这 sl four G 打 log 就在这里面打一个 error 级别的 log 告诉他什么呢？告诉他你的 key your access is blocked 然后把 key 打印出来。好嘞，那这里主体部分就完成了吗？当然还没有完成了，你看咱这里写的是 false 这一步可是关键。 OK 我们这里要给它加上几个辅助的类，那这个类名叫什么呢？我们来看。


第一个是 private string Redis template 这一个大家以前没见过吧，这是 spring data 里面的 Redis 的支持类，它其实就可以理解为 rest template 一个道理，我个人其实比较喜欢使用 spring data 我自己做私人项目的时候我都是使用 spring data 但是公司级别的项目大多使用的还是 my badis 因为这 spring data 开发起来特别的快，你像我做私人项目，经常是几个星期甚至一个月就要交付一个大项目，所以说用 spring data 能省下不少事儿。那这里给它加一个 out wired 从哪儿来？咱待会儿要声明一个 stream ready template ，这里咱先给它 out wire 的加上还没有进行声明，稍安勿躁，我们接下来做第二个注入。


第二个注入是叫 Redis script 这一个大家来进去看是谁也是 spring data 的，spring一统江湖，统治天下。我这里给大家加一个泛型，其实有的设计理念，说尽量不要泛型，用泛型模板有好处也有坏处，只要适合你自己项目的就是好的。其实架构这种东西就像医生看病一样，同一种病有不同的看法，但是你只要能把问题解决就可以了。所以我提倡适合自己的才是最好的。


and ready subscribe 这里声明晚安，想给它起名叫 Rita lament Lua 这怎么把 Lua 带出来了？因为咱 Lua 是什么？是一个 script 的脚本。对不对啊？咱要想在 Redis 里面执行，那就要靠这个 Redis script 同样的也给它加一个 auto wired 把它拉进来。好，这两个类。那大家知道用在哪儿吗？猜一猜这里对吧。这叫 hard code 咱要把这个 hard code 给它 replace 掉。怎么 replace 我们看，先来调用 string Redis template 然后调用它的什么呢？ Execute. execute 什么内容，那就是执行一段脚本了。那我这里首先要把这个 read limit Lua 传入进去，大家看这是个类对不对？实际上待会儿我在声明这个 Redis script 的时候，会把一段我写好的 Lua 脚本塞入到这个 script 当中。所以这里大家可以把它理解成它就是一段 Lua 最后这里加一段配置它是 LU script 的真身老夫真身在此。


然后后面跟什么呢？我好像这里没有把呱娃的包给它引入进来。那咱这里添加一个刮瓦包，把这个刮瓦包放到 rate limit 这里好保存一下。那咱在后面就可以开心的使用 list 了。谷歌真是造福全人类，还发了这么多非常方便的小组件。


这个 list 传入的是谁呢？传入的是 Lua 脚本中的 key 列表。咱前面学过对吧？ Lua 脚本中你可以拿到 key 你也可以拿到这个 key 对应的 argumentsarguments 也就是参数 value 好，我们这个 key 传入一个谁，他就是你方法的 key 那接下来后面传入的是谁？大家应该能猜到了吗？当然是咱的这个 limit 了对不对？也就是说你想要被限流到每秒钟访问多少次？那这个叫做 value Lua 脚本 value 列表，因为咱这一章的内容并不多，所以同学们如果有余力的话，可以怎么样去 debug 看一下这个 string Redis template 里面究竟是什么东在哪，直接在这边上一个断点，调一个方法，走进去挨个看一下整个流程，那就能搞明白 spring data 是怎么样来操作， Redis 怎么样来植入 Lua 脚本的。


我个人强烈推荐使用 debug 这种模式来学习框架源码。你看外面的这些教程，他怎么说，这个框架怎么架构、AOP怎么做，哪些关键类没有用。同学们进去 debug 一把，从头到尾一走，什么都搞清楚了。好，这 todo 是不是可以拿掉了？咱先给它拿掉。


接下来我们来写什么？我们来写这两个类，他前面说了这两个要手动声明一下，咱这边光写上引用，还没有对他们进行声明。那接下来我们创建一个 class 专门用来声明这两类。那这个 class 名字就给它起叫 Redis configuration 好了，因为毕竟是跟配置有关的，既然跟配置有关，那骑手一顶绿帽子给它扣上叫什么 configuration 好，你这个 annotation 加上去，然后接下来在里面就要去声明这两个类了。


第一个 bin 的声明非常简单， public 开头，然后返回的是 Redis template 那这里给它加一个半形 string string 的泛型 K value 的类型。 OK 那它的方法名字这里可以随便起，就叫 Redis template 好了，那接收的参数这里我要指定一下，他接受一个 Redis connection factory 那这一个 factory 就不用我们去手动的声明了，那这框架会自动注入进来。 OK 那它返回什么内容，骑手直接一个 return 我这里不需要其他额外操作，只用简简单单的返回一个 new 谁呢？ new string Redis template 然后把这个 factory 塞入进去非常简单。那完事儿之后，在上面加一个并注解，把它添加到上下文当中。


那接下来咱定义第二个 bin 第二个 bin 咱前面看到是封装 Lua 的脚本。那么它这里返回的这个类型就是叫 default Redis script 前面多了一个 R 去掉 default Redis script 那同样这里也有一个泛型，我们给大家添加谁先 hold 先不要动。那这个泛型咱在代码里面再指定，不用在这上面直接声明出来，给这个方法起名就叫做 load Redis script 因为要加载 Lua 脚本，那我们这里第一步先给它声明出来一个 default Redis script 在这声明这个类好，直接 new 出来，什么参数都不要。那么接下来这里要添加几个初始化的参数，比如说 set location 谁的location ，那肯定是咱 Lua 脚本的 location 对不对？咱来看一下 Lua 脚本在哪。
我们待会儿打算把这个 Lua 脚本放到 resources 这个文件夹下，就是说他肯定在 class path 下面。对不对那我们如何呢？加载一个 class path 下面的资源文件，那我们就用这种方式 new class path results 那这个 Lua 脚本叫什么名字呢？咱虽然还没有开始创建，不过可以先把名字给起了就像咱玩没落地先把名给起了，给它起名就叫 read limiter 好了点 Lua OK 那是名字起。


好了，接下来我要给它定义什么？你的 Lua 脚本，它总之是一串 script 脚本语言，它最终有一个什么呢？返回值，我给它定义的返回值是 set result type 什么呢？布尔值。那为什么是布尔值呢？同学们，因为我想让这个脚本最终告诉我行还是不行，怎么个行法呢？就是说你的这个请求如果没有被限流，那么 OK 你可以放行过去。那这时候它就返回一个 true 如果被限流，返回一个 false 是不是非常简单？好，我们给它这里把布尔值的类型给它打上，点 classok 最后一步直接 return 回去。好完成了吗？还漏了个什么。漏了个 bin 把这个 bin 给它添加上去。 OK 那好，接下来做什么呢？接下来咱把这个浏览脚本给它写了。


好，打开小桌板，在 resources 下面创建一个 Lua script 这里 new 一个 Lua 给它起名就叫 rate limiter.lua 在 Lua 脚本就一切从简，用最简单的方式，最高效的方式把这个任务给它完成。好，我这里第一步先声明一个 local 变量叫什么叫 key 给它起名叫 method K 好了，那它从哪里来？它从 case 1 来，那这个 case 1 是啥？是第一个变量，就是我们传入的 key list 中的第一个值。那它代表着什么意思？我这里给它添加一行注释，它的意思是获取方法签名特征。在稍后我们做成注解的时候，会通过 aspect 把这个当前调用方法的签名给它拿到，然后传入到 key 当中。


那接下来我还要再获取另外一个值，同样也是 locallocal 什么 limit 它从哪来呢？它从咱的 arguments 也就是 value 当中来第一个 valueokay 大家知道它是一个什么类型，它是一个 int 型，所以我们这里要把它转一下，给它调用 lord to number 方法把这家伙给它塞进去走。你好嘞，那这个 limit 又是什么意思呢？叫调用脚本的时候传入的限流大小。 OK 那这两个值都获取到了。那我接下来还要获取一个叫 countcount 的，谁 count 的就是你当前这个方法它在过去一秒钟调用量是多少？那这个值从哪来啊？咱不能让调用方法自己来传入了，那不是自己蒙自己对吧，咱要从 Redis 当中获取。 OK 我们这里调用 Redis corp 靠谁呢？靠 Redis 自己的方法了。这里要 getget 谁？ get 我们前面这个 method key 把它的值 get 到，并且我要怎么样给它转成 number 转成 number 还不够你这个值如果是第一次调用，那它是不是空的，就什么都 get 不到，怎么办呢？这里给它加一个 default 的值，就说如果你 to number 这个 get 不到，那么我这里给它返回一个谁呢？返回一个 0 这种脚本语言的语法看起来真的是非常简洁。那我们这一句给他再添加一个注释，叫获取当前流量大小。


很多人看学习一门新语言，从入门到上手编写一些简单的脚本，真的非常非常快的。那你有 Java 的基础去学习其他的语言，简直如鱼得水。括弧这些语言可不包括 C 加加。
那接下来我们就要开始判断了，判断什么呢？叫是否超出限流阈值。 OK 怎么个判断很简单，如果你的当前的 count 怎么样？把它加上 1 还大于你调用的时候传入来的这个浴池。怎么样？就毫不客气了。 then then 干什么呢？ return 一个 false 代表着什么？返回拒绝服务访问，这就是说你已经被限流了。那如果你没有被限流怎么办呢？那就是一个 else else 谁这里叫没有超过阈值？好嘞，那我这里 else 的逻辑就是调用 redis.call 就是把你当前的 count 加 1 给它保存进去。但是咱可不能在这里计算好这个 count 值，然后再把它保存进去。我们这要怎么样啊？我们这里调用 Redis 的一个函数来替我们做这个操作，这个函数就是 incret by 摆什么？我们把这个加入进去，把这个 K 对应的值加上 E 那么这个计算是不是又放到 Redis 那边了？ OK 在这里给它加一行注解叫什么呢？设置当前访问的数量，加一好，加完 1 还不够，我这里还要怎么样？还要再给它配置一个 expire 过期时间，给他个 1 这里是设置过期时间，好马上就要完工了最终你这都准备妥当以后，我们要给你怎么样？ return 一个 true 告诉你完事了，你可以继续往后走了，叫放行完成了吗？这怎么还有个红色的小尾巴要怎么样？这就是这种上古语言，上了年纪的语言，非常讨厌的地方。你要加一个 and OK 那散出来脚本也准备好了对不对好，我们接下来怎么样打印几行 log 我们在这里分别把它打印出来。


redis.log log 谁呢？我先要给 log 级别给它打上 debug 级别，然后把这个 key 给它输出进来。 key is key 是谁呢？就是咱传入的这个 master keyok 就打这一行 log 就可以了。那剩下的同学们可以自己去在这里多打几行，像这里也可以打一个 log 把这个 limit 输出进来，以及最终的这个限流访问过后的结果。你是放行还是不放行？把这个 log 都给它补补全。


那这个 Redis 的 log 它会打印到哪里呢？是 log 文件还是控制台其实都不对，它会打印在 Redis 的控制台里。不过我这里设置的是 debug 级标，对，同学们可能是看不到这行 log 的。不过没关系，这里面有很多个级别，同学们可以在这边改一下。


OK 那这里老夫，那这个 Lua 脚本好像已经写完了，这里搭眼一看，好像漏掉了一个地方，这个 key 应该叫 method key ，我们把这两个 key 给它改正过来。不然的话如果你这个传的 key 是一个不存在的 key 那么 Redis 在调用的时候会报出一个错误，告诉你说这个 key 不存在 Redis 这点做得很好，它的每一个错误提示都非常非常的清晰。那咱的撸脚本到这里已经完工了，接下来咱进入下一步。


这一个处理完了以后，接下来我们再创建一个新的项目，这个新的项目做什么呢？专门引入 rate limit annotation 来发起一个调用。那这个项目的 module 咱给它起名就叫 rate limit 杠 test copy 一下 next 毛球链保持一致，后面把它扔到同样的文件夹下叫 rate limiter 文件夹。


OK 点击 finish 走，你咱如何来验证呢？这里就要去写个 controller 来进行调用验证了。好，那这里我们把它的 dependency 需要的全家桶都给它加进来。那都有哪些需要的部分呢？就一个谁 a group ID 是 org spring from a boot 使用它只用一个 starter spring foot starter web 没提示出来。 starter webok 咱接下来要怎么样？要把咱创建好的 reader limiter annotation 把这个项目也给它加进来。那我们在这里再添加一个dependency ，然后它的 group ID 就是使用 project.group ID 给它加进来。然后 artifact 从刚才创建的项目里把它 copy 进来，我们来看一下它的 artifact 在这里。
rate limiter 杠 annotation 好嘞，那最后还有一个谁 version 对不对，咱 version 同样的也使用刚才引入 group ID 的方式把它给加进来。 project 然后点 versionokay 多了个括号把它去掉。好，这里就完成了，咱需要的 Redis 还有 LP 的注解，其实都在这个项目里会给它引入进来的。我们在当前的这个 controller 里，就只用关注于简简单单的调用一下就行。那这里给大家创建一个 package 叫 com.imock 咱的独家冠名上 IMock 还有后面跟 spring cloud 在这下面搞一个 Java 的类叫 rate limiter application 走。你好，在 application 上面第一步先给它一顶大绿帽子扣上加 spring boot application 好自动双配慢慢玩去吧。下面跟 public stat it 把闷方法给它打上。这个闷方法里我们要把它启动起来，通过什么方式呢？直接一个 new spring application builderbuild 什么东西啊？ build 你当前这个类点 class 加入进来换一行走。你 web 以什么方式启动 web 呢？ web 来 vacation.serve let 的形式直接 run 起来。 run 起来的参数在哪里？就在这儿。 arguments okay 好。


启动类创建好之后，咱快刀斩乱麻，把这个 controller 也给一起创建出来走，你看出来有没有绿帽子，叫什么 rest controller 对吧，带上看你头大，这衣领不够再给你加一点，sl four G 搞上去。


好嘞，大家这里要 autowired 进来一个咱刚才创建好的 service 这个 service 叫什么名字，瞧这记性刚创建好就忘了叫 access limiter 我其实应该给它起名叫 access limiter service 没关系，反正后面咱要把它再改写到 access limiter 怎么样 out wire 的进来。然后我这里添加一个测试方法叫就把它叫 test 好了。好，这个 test 返回一个 string 然后在这里面只是简简单单的怎么样简简单单的 return 一个 success 就可以。但是在 return success 之前，我要怎么样调用一下这个方法，调用它的 limit access 我给它做一个限定，我当前方法的 key 我想给它指定叫 reader limiter test 这是我方法的特征量，那后面我给它限定怎么样，每秒钟访问一个。好，我看看它能不能调用成功。然后这里给测试方法添加一个 get mapping get mapping 的 name 就叫 test 好嘞，那这个方法创建完了以后，我们接下来是不是还少了一个步骤是在 resources 下面，把配置文件给它创建出来对吧，咱叫 application.properties 同学们如果喜欢 YAML 格式，把这个创建成 YAML 都一样的。


这 properties 里面都有哪些内容呢？第一个，自报家门 spring [application.name](http://application.name/) 那这个应用叫什么呢？叫 rate limit 杠 testok 那接下来给你指定一个 server port 你就叫10086。好了，恨死 10086 了，我要给他指定谁呢？ Redis Redis 怎么指定 spring.redis.database 前面大家应该都配置过，都非常熟悉了。那我就不介绍这每一个属性都是什么意思了。


第二个， spring redis.host local host 那老师这里的 Redis 是没有设置什么其他用户名密码的。这接下来是一个 port 是默认端口，我给它指的是6379，那 log 还是给你指定一下，省得乱丢垃圾。现在上海实行垃圾分类，你这个 log 不能放的，整个文件夹到处都是，咱们给它定位到这里叫什么呢？专门一个 log 的文件夹 string.application name ，你就到自己的专属文件夹去点 lockok 那咱这个应用到这里为止，就已经是写好了。好，我们尝试把它启动一下，看一看效果。二话不说，对着慢方法直接走了。看到 spring 标签成功一半，我们往下走，很快已经 started 了。 OK 那我们这里走到 postman 里，调用这个方法，咱切换到 postman 我这里已经把这个请求创建出来了，发到 local host 10086 端口，然后它的 URL 是 test 好，这是一个 get 请求，我们直接发送 send 每秒钟。咱记住可以放行一个请求走，咱来一个。好，这已经 success 了，我们再来一个。你看，如果以每秒钟一个的匀速，它是可以正常返回的。那我们这时候加快速度，开始点起。同学们看到这里是什么错误啊？你看这里有一个 status 500 的异常，然后它的 message 是什么？是 your access is blocked 这个 message 是不是似曾相识呢？这不就是咱在异常中包含的信息吗？那说明咱这个限流组件已经是正常生效了。


OK 那么接下来我还要做一点小改造是什么呢？咱基础人员不满足这种调用方式，你看看我还要在业务代码中再调用你的方法。就像这样，虽然这只有一行，但是我总觉得这个很别扭，咱都是追求完美的。对不对？我们把这个方法怎么样？抽成一个注解，我在这里注解，轻轻松松一配置，就自动的可以提供限流的功能，这样是不是很酷炫呢？ OK 同学们，那这一节就到这里结束了，下一节跟老师一起手把手做一个限流的注解。同学们，我们下一节再见。





