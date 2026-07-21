---
title: 6-6 Sentinel核心源码解析-SC自动装配（1113）
---

# 6-6 Sentinel核心源码解析-SC自动装配（1113）

同学们大家好，接下来我们介绍一下 spring Claude 阿里巴巴 settle 的相关制动装配的内容，这里面我们还是回到对应的 spring Claude 阿里巴巴这个功能模块。刚刚才我们也介绍的对于 swing code 阿里巴巴里面跟 Seasonal 相关的是四个模块，这里面涉及到自动装配的是前三个模块，这里面分别是 spin Claude start 阿里巴巴 settle 和 spin Claude sick breaker settle 以及 spring code 阿里巴巴 settle Gateway。



对于 Saturday source 我们可以这会儿是不考虑，那么我们重点建去看一下对应的这三个模块里面的一些自动装备相关的一些内容。现在我们就直接切到 spring code 阿里巴巴这个源码里面，我们进行去一些看一下，首先我们来看一下是 spring code，阿里巴巴 settle 呢，我们对应的starter，那么 starter 是在这里面，这里面是 spring code start 阿里巴巴settle。那么我们先看一下这个 spring factor 里面的内容，我们可以看到这里面对应的 enable auto configure 自动装配会刺激到。


首先是 Seasonal Web auto configure，我们可以看到这是 Web Plex，可以想象它是对应 spring Web i m a C 和 spring Web Plex 两种不同方式实现的对照。那么我们要先看一下到这里面，在这里面我们可以看到它实现的过程，我们看到对应这里面是首先是condition，这是一面 condition on Web application，也就是说我们的 Web 类型，那么如果是选中的是 settle Web auto communication，它的类型必须是 type 对应的select。


那么这里面我们也可以看一下这里面 Seasonal Web Flex，它对应的参照，我们可以看到它是对应的，我们必须 Tab 是对应的active。那么好，我们先还是先回到我们的 settle Web to configure 里面，这里面它首先还需要要求我们肯定是 on class，这里面有 signal Web intercepted，这是什么意思？也就是对于这个，我们看一下 Seasonal Web intercepts 它是在哪个包里面，这个包它是对应的是在Adapter，对应的是 string Web Mac，就是说我们可以看到对于跟 string Web IC 集成的过程中，它需要我们引入 Sentence spring Web MC Adapt 这个包，也就是说我们基于 stream 集成引入对应 FCC 的 Adapt 才可以。


那么这样我们再去看一下它的一些配置，一些信息。在这里面我们关注的是比如这里面是 UR cleaner 以及是 block accepts handler，以及像其他的一些信息，这里面是 Sentinel Web intercept，这里面我们可以看到对于 block exception handler，也就是说我们抛出这个异常以后怎么去处理。


另一种方式是我们可以看到是它是怎么处理，它是通过 Satin Web intercept，也就是说它是基于 sum v seed 一个拦截器来实现这个我们塞斯诺限流的。那么这里面我们可以看一下这个 settle Web incept 它的实现的过程，因为我们在 spring Web Mac 的时候，我们也看了这个 adapt 的内容，所以说我们从这里面去看的话，会感觉是相对来说比较熟悉一些。


我们可以看到这里面首先 get result name 开始抄name，它里面涉及到 URL cleaner，也就是说它避免那些 restely restful 的 URL 进行那个 URL 数量的膨胀，所以说通过 URL cleaner 进行一些 URL 的聚焦。这里面这是 get context name，它是通过 rescade result name 获取的一些组合，那么我们看对应它的父类里面实现的内容。这里面我们可以看到最终 Pre handler 做的一些事情，它会获取到我们的 resource name，通过获取到的 result name 来进行我们一些通过 Su 进行 entry 进行一些内容，也就是它的 result name 作为它唯一资源的一些区分，那么这是我们对应的settler，我我们的 Web settle Web auto configuration，那么这里面对应的是 Sentinel Web Flex auto configuration，这个它的逻辑是大同小异。我们可以看到这里面首先是 type 是active，并且我们这里面是 signal active transform，那么对于 transform 它要求是我们需要把 signal Rector Adapter 这样一个 debt 添加进来，其实逻辑我们可以去对应的上，那么我们来接下来看一下后面的，这里面是一个 seasonal endpoint auto configuration，那么我们看一下这个 endpoint 实现了哪些内容。


首先这 endpoint 我们看首先是 settle endpoint，还有一个是 settle bells direct，也就是说我们首先实现了一个 settle 的一个端点，同时我们还实现了一个健康检查的一个指标，一个健康指标。我们先看一下 settle endpoint，那么对于 settle endpoint，我们看这里面对应它的 URL 是对应的是settle，同时它是 read appracing，也就是说这个请求是只读的5。如果说我们的对于这个 any point 是可用状态的话，我们会把对应的像 APP name，log，d， l 以及我们相关的一些 block 配置等等这些元数据信息，我们组装到一个 map 里面，把这个 map 返回过去。


所以说我们可以基于 settle 这个 in the point 了解一下我们系统里面关于我们这些 settle 相关的一些元数据的一些，配置信息，同时这里面我们可以看到它里面还有一些规则信息，也就是说规则这是流控的，这是我们就是限流的，这是我们降级的。当然 system 等等这些规则信息也可以在这里面体现出来，这是我们的 settle endpoint。
当然我们还列了一个，下面我们看一下这个健康检查 health 健康检查指标，这个健康检查指标我们可以看到它也是首先判断一下这个健康指标是否开启，如果说它没有开启的话，就直接把原来的这个默认的逻辑返回过去一下，如果说它已经开启的话，那么这里面要注的事情我们看到首先大家去判断一下dashboard，那么 dashboard 的这些服务列表是否注册的正常，也就是说我们的控制台没找着的话它会带套的意思configure，也就是说你没有配置它会认为是启动失败。


这里面还涉及到一些心跳相关的一些信息，发现这个接机源的心跳的情况，后面还会有一些跟数据源，就是说我们配置数据源的信息是否获取得到等等。这里面其实你看我们对于数据源它里面有一个 data source load configure，如果说 little source load configure，如果说正常执行的话，那么这里面它会认为 states up，如果是抛异常的话，它就会认为是嗯，没有获取到正确的值这样一个情况，那么我们再看一下 signal auto configuration Sentinel。


我们看一下这里面，对于这个 center complication 里面更多的是在初始化的过程中对于这些属性进行了一些设置，就是对属性进行了一些处理，这个可以看到这里面并没有什么太多的业务逻辑，我们就跳过这里面是 session phone auto configuration，看这里面看起来是比较简单，这里面首先它的 condition on class，这里面是FCIU，说明我们首先当前依赖了我们的sentinel，同时也依赖了份。那么对于这里面它唯一做的就是把这个 builder 做了一些替换，我们看一下 Seasonal phone builder 它做了哪些事情，对于这个 builder 的过程中，它实现了对于在 IMO case handler 进行了一个替换，它获取的我们可以理解为我们找到对应这个分刊的 package bin 里面的对象，那也就是这个 bin 构造会找到对应的callback，也就是说我们找到 callback 相关的信息，如果说存在 call back 相关的内容的时候，它就会进行一些 setting 的 invoke handler 的替换就是主要是在这里面也就是把 settle 的相关的一些机制植入进来了，这是我们看到是 settle 相关的一些内容。


接下来我们来看一下这个，对应的是我们这个 secret breaker 它的一些自动装配，这里面自动装配是两个自动装配，我们可以进来看一下，通过这里面我们看到它是这里面构造出来一个 circle break 的factory，基于这个 factory 来实现 Sentinel 它的一个断路器。下面这里面的内容是我们实现一些 customer 的一些操作，也就是说我们可以通过 customer 来对于 settle 我们这个熔断器的 Fax 来进行一些自定义。


我们可以进来看一下对于这个 setonal circle breaker factory，它这里面是通过 create 最终构调内容，就是我们的 SETANA circle breaker，其实我们可以在这里面去看到最终它会需要的一些元素是我们这里面 resource name，我们的 entry type，以及我们相关的一些 rule 这些内容。这边另外一个是 reactive settle circle breaker，我们可以想象到它是一个对应的关系，里面active，我们看到这里面是对应的是 negative circle breaker factory，其实它实现的逻辑可以是理解是一样的，底下是也是customer，就是说对我们这个 Pector 进行一些配置的一些超出的一些持入方式。


接下我们来看一下Gateway，那么 Gateway 下面它里面也会涉及到两个对应的 auto configuration，这里面我们看它这是基于 spring close KTV 的 auto configuration，这里面我们看一下它的condition。首先是 condition on class 是 global filter，也就是说如果说有 global filter 的话，说明我们的当前上下文是依赖了我们的Gateway。
接下来我们看对于这里面的内容，这里面是我们首先有 block request handler，就是说如果说我们对于请求主设以后我们需要怎么去处理？我们这里面会涉及到 init APP type，应该 init fall back，这里面在初始化的过程中，对于我们的 APP Tab，这里面我们看到它设置的内容，我们这里面统一的是标记为11，这里面的它的 k 对应的是 fashion APP type 这样一个 KV 的一个设置。


后面是我们初始化我们的 four bug，一个快速失败的一些设置信息，这里面还有对应的 Sentinel get away block exception handler，也就是说也是对于 block exception 的一些处理，这里面是 signal Gateway filter，其实这个是真正的生效我们对于 Sentinel 环节的一个filter，其实在这个 filter 里面我们能看到它对应的逻辑构造，对应的 resource name 与称，同时以进行我们真正的一些执行。


这里面我们看到是 entry configure，这里面 Sentinel record transfer，它里面做的事情其实是在我们执行 polite 的时候进行一些操作的替换，我们再跟进来，可以看到这个里面它的内容，我们可以再看到在这里面它最终会用到我们 SIP SEO，这么我们记住看到它是基于异步的旁次去执行的，最终得到一个 async 的entry。


其实这里面就是真正我们之前 settle 它规范的一些内容。我们孩子回到KTV，这里面我们看另一个基于这个 auto configure 它实现的内容，我们可以看到这里面是对于一些 API 项的一些处理，我们看到这是 API particular item，以及跟一些 m 这里面object， Mapper and JSON 序列化相关的一些信息。这里面其实我们可以不用花太多精力。


这样的话，我们对于 spring Claude，阿里巴巴 settlement 相关的一些内容，我们只是把自动装备的问题过了一下，其实它在执行流程跟我们 settle 的原生的执行流程都是一致的，不管它用哪种方式，最终不管是直接还是间接的，它最终是通过我们的 slot chain，也就是我们的插条链进行我们这些 Slardar 的执行，去进行我们一些规则的校验。关于我们 swing Claude Sentinel 它的自动装配的内容，我们就先介绍到这里，同学们，我们下一节再见。

