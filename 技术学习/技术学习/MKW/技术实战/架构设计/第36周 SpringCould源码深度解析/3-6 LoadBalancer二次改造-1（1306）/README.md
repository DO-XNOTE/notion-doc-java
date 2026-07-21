---
title: 3-6 LoadBalancer二次改造-1（1306）
---

# 3-6 LoadBalancer二次改造-1（1306）

同学们大家好，这章节我们对 spring code load balance 进行一些二次改造，主要是通过 load balance 提供的这些设计入口进行一些基本的二次改。首先我们介绍如何自定义负载均衡策略来替换默认的轮询的负载均衡策略。那么第二个改造点我们认识一下 load balance 的F3，从命名上我们可以理解为它就是负载均衡执行的生命周期，那么我们通过 load balance life SQL 的接口来实现完成我们扩展的一些业务。


那么首先我们来看一下如何去自定义这负载均衡策略，那么如果说我们需要自定义负债均衡策略，那么通常我们需要定义 customer load balance configuration，在这里面我们可以看到是这样一个结，那么在这里面我们特意注意一下，对于我们通常我们定了 configuration 相关的类，这里面通会通过艾特 configuration 这样注解去进行修饰的，那么但是在对于 load balance 的话，这里面相对比较特殊，那么这里面虽然有 bin 的一些注解，那么但对于这个类的话它并没有使用 at configuration 进行修饰。


待会我们会重点去讲解一下为什么在这里面我们对于这个 configuration 下面我们配置了一 react load balance，也就是说在这里面实现我们自定义的负载均衡策略，当然我们这里面并没有自己去定义一个负载均衡策略，我们使用了 load balance 默认提供的第二种负载均衡策略，也就是我们的random，也就是我们随机的一个负载均衡策略，那么这里面我们要做到是什么呢？我们通过负载均衡策略，它提供的第二个就是我们的随机借负载均衡策略替换掉默认的我们的轮询的负载均衡。那么在这里面我们看我们在这里面定义的这个随机的负载金融策略，它这里面其实并没有什么特殊的内容。


这里面我们是首先我们定义这个闭隐的过程中，我们命名random， load balance，同时我们传入我们的 3M 环境以及我们的 load balance， client fix。那么基于这两个参数进行我们内部的一些定义。在这里面我们首先去获取到我们对应的这 load balance 跟 client factory 对应的一个名称，这里面我们通过 random load balance，它进行一个构造，构造的过程中需要输入我们 load balance client factory 对应指定的这个provider，那么这里面 cos load balance configuration 定义完成以后，我们可以在我们的 load balance applicase，也就是我们的启动类上加上我们的爱的 load balance client 这样一个注解。


在这个注解里面我们要指明一下我们首先这个 value 也就对应的内幕，也就是说我们这个负载均衡，需要负载的它的服务是什么，这里面我们可以理解为它的思维，在我们这里面指定是 nicos provided，那么这里面的configuration，它指定的就是我们在这里面定义的这个 configuration 类，也就是说我们这装配的一个配置类，那么这里面大家想一下对于 configure 这个我们的 config 润这个类，这个类里面可以附我们自定义哪些bin。


其实这里面我们可以参考一下我们的 load balance client configuration 这个类里面它有哪些内容，我们这里面可以在这里面去切换一下，在这里面我们看对应我们这个 load balance client configuration，它里面这些东西我们都可以自定义去替换的，我们看这里面是我们的 record load balance，我们已经把对应的轮询的 load balance 我们替换成我们的这里面的一个 random load balance，那么它后面还有一些像我们看到比较关心的 service instance list supply，那么它也就是我们的服务实例的一个列表提供器，那么这个服务列表提供器的话，这里面有各种它对应的一些构造的方法。假如说我们需要根据自己的方式再去构造它一个组装的过程，那么我们也可以在这里面进行一个复写，那么我们通过自定义的 b 就可以把我们默认的 bin 去覆盖掉。


那么至于为什么我们自定义的这个 configure 的 bin 能覆盖到它默认的大家，这是 spring boot 的工作原理，这里面我可以看到，也就是因为在这里面它有一个对应的注，这个注解是肯定是 on missing，它是什么意思大家应该是比较清楚了，也就是说只有当我当前的上 l 环境里面不存在它对应的实例，那么它才会进行初始化。
那么构造到我们这里面的 react load balance 的话，也是这样一个原理，那么因为我在制定的时候就已经有了 react load blins 这个 bin 了，那么在这里面在执行的过程中，因为这个条件不满足，因为当前已经有这个 b 了，所以说整个这段代码它就不会再进行执行。


这也就是说我们通过我们自定义去覆盖它默认的配置，那么这里面我们大概了解，那么我们接下来去看一下这段代码它执行的原理，还是我们回到我们刚才的一个疑惑，为什么我们在定义这个 configuration 类的时候，并没有去标明一下这里面的注解 at configuration，那么这段代码我们还是通过这个入口类 load balance application 来看起，也就是说整个它跟负载均衡这个自动配置相关的，也就是我们的 i 的 load balance client。


那么我们切到代码，我们看在这里面我们在 load balance application 定义的这个鲁班森克兰的，那么我们可以跟一下看这个注解，这个程序是怎么对这个注解进行处理。我们跟到这个注解里面可以看到它里面提供的一些属性，这里面 value 和 name 它都是一个互补的一个注意我们不管是name，它的效果是一样的。接下来这里面会配置一个configuration，制定一些 config 软件信，其实我们在解读这个 load balance 对应的这个注解的时候，通常我们去看一下它有没有对应的 import 这样一个注，如果是通过 import 引入了对应的 resist 这样一个类，那么通常它会通过这个类进行一个对于它的一个处理的一个引入，那么好我们去跟进来看一下，可以看到这里面它也是实现了 import being definition registry 推，也就是说当我们使用了这样一个注解，那么 load badcase 看的这个注解的话，这个注解的内容它会通过这样一个 register 它这个类去处理。那么这里面我们重点关注对应的这里面是 register being definition，也就是说我们会通过这个注册必应定义文件的方式，嗯，把我们配置的相关信息注册进来，那么在这里面我们可以看到，在我们去分析这段代码，我们可以看到它是这样一个过程。


首先我们看它会通过 Meta state 里面获取对应的注，这个注解我们特意区分一下，这里面是 load balance，也就是说这里面是两个注解，它只是两个注。我们切进去看一下，对于这两个注解分别是 load balance client 和 load balance client s，我们可以看到它的关系，对于 load balance client s，它里面可以支持使用 load balance 这样一个组合的一个关系。


那么理解这一点我们就来看一下它那个解析，首先它会解释一下，也就是解析的过程，首先找这个 Meta date 里面有没有 load balance planters，也就是带 s 的这个注解，如果有这个注解的话，它会去做相应的这些处这个处理的内容。


接下来我们其实这个处理的内容其实是比较简洁的，最终它处理的效果是一样的，通过 regist client configuration 定义一个我们指定的一个，那么我们直接来看一跟我们当前这个 load balance client 它相关的一些内，我们看一下当通过 Meta data 里面获取这 notice attribute，也就是说找这个对应它这个 bin 所配置的一些属性的时候，它得到一个 map 列表， map 列表分别是一个对应的 string 和 object 的一个 KV 的结构。那么它会通过这个 get client name 获取一下对应的属性里面那个值，那么 get client name 我们看一下其实它实现的功能是比较简单的，如果说这个 map 为 now 就直接 return null，那么它去获取是 value 和name，里面找到只要 value 和 name 有一个存在，那么 h bug 只对应获取，如果 name 和 value 都没有配置的话，那么就会抛出一异常，就是说这个状态是不正确的这样一个异常。


好，那么我们还回到我们这个 import 它的一个处理的过程，在这里面它首先得到这个 name 以后，那么我们判断一下 name 不等于null，如果 name 不等于 now 的时候，我们进行去一个 b 的主，我们看到这里面必应的注册，首先是当前这个注册器以及我们配置的name，以及我们通过这个client，也就是说我们通过 map 里面获取到 configuration 信息。这个 configuring 信息我们可以在这里面去看一下，也就是我们指定的这个类，也就是我们指的那个配置类，那么在这里面我们接着跟进去看一下它的一个处理的逻，这里面会通过 Bing dependency builder 构建出一个 Bing dependent builder，那么这个 builder 我们可以看到这个 Bing depending 它的原生的类是什么？就是 load balance client specification，这个我们怎么理解？它就是我们在定义 load balance 一个客户端的过程中它的一个规范，这里面定义了一个名称，一个configuration，我们可以理解为它就是一个元数据的一个封装，这样我们看这里面会在 builder 里面构造了两个参数，也就是它的构造方法里面，我们填第一个参数是name，第二个参数是configure。


对于这个方法里面我们可以看到对于这个构造方法是第一个参数是name，它的第二个参数也就一个configuration，一个类的一个数组，也就是说我们可以支持多个类的传。这里面我们同时把这个 Bing dependence 里面注册到我们的，也就是我们的 bin 容器里，他注册的过程中我们看到这个 name 是如何定义的？在注册过程中拿 name 和我们这里面是 load balance client specification 做一个后缀，那么同时把这个 bin definition 注册进去，这样的话就也就是把我们指定的这个 bin 注册到容器里面了，其实这里面注册的并不是我们的configuration，而是注册了一个指定的 load balance client 一个规范。


那么这里面我们要想一下，我们把这个 load balance client 的这个规范注册到我们的变容器里面，它在什么时候使用？这会我们可以切换到我们自动装配的这个 auto communication，我们看这里面的 load balance auto communication。这个 bin 在构造的过程中它需要一个参数，这个参数就是一个 look balance client surprise case 这样一个list。那么我们可以看到也就是说我们在制动装备的过程中，可以把对应的我们制定义的这个制动装配的规范会搜集到，那么搜集到的这个规范它其实是在创建我们的 loadbase 川的 factory 的时候，会把它作为一个传到我们的 load badcase factor 里，那我们可以跟到这个里面，我们看对应 load balance client factor 里面，其实是它是在这里面是使用最终我们的内容会放到对应的这个 concern 的 hashtap 里面，也就是说我们刚才定义的这个 load back Claude 这个规范它会以这种方式保存起。
那么我们看一下这个 configurations 它是做什么使用了在这里面，它其实最终我们把它复制到这个 list 里面，那我们可以从这里再看，其实当我们在 create context 的过程中会用，首先在 create context 过程中它会把一个 name 传输过来，那么首先会判断一下当前指定的name，这在我们的 context 这个 configurations 的这个 map 里面是否如果存在的话，那么就把对应的这个 map 获取出来。那么基于这个配置去创建我们的这个contact，也就是一个子的一子龙。这会我们可以去想一下，因为我们在这里面定义的过程中，我们可以看到我们在这里面定义的过程，我们的name，我们的 name 是指定的 nicos provided，那么在这里面在这里面使用的过程，我们获取到这个 name 也是对应的是 nicos provided，那么这个 configuration 类也就是我们这里面指定的这个 being 就是 customer load blanks config。


那么现在大家已经明白了我们在制定的这个过程是怎么装载的？那么我们现在去想一下，我们在定义这个 customer load balance 的时候，我们这里面并没有去使用艾特 computer 这个柱形，它的原因是什么呢？假如我们如果使用了艾特 config 这个注解的话，其实在程序启动的过程中，就会把这个 customer load blank configuration 的装载到我们当前这个容器里，那么这样的话它的问题就是什么呢？其实我们当前容器是并不希望去装载这个 configuration 这个computer，它装载的逻辑是在这里面，是在我们对应创建这个子容器的过程中去装载的，也就是说我们在 create context 的过程去专门的去加载这个 configuration 配置，所以说这样的话，我们这个在自定义的这个 cos look blanks configuration 的话，它就不需要在这里面添加爱的 config 这样一个修辞，这样希望大家就能够明。其实在这里面我们可以定义很多不同的 customer configuration，那么这样我们就基于不同的服务可以对应一个不同的一个子容器。我们看到 annotation configure application context，也就是基于我们这个配置生成一个子的容，最终通过子容器里面获取到我们当前负载均衡对应的 service ID 里所需要的这些。

