---
title: 2-1 Mybatis配置文件解析过程源码解析（1352）
---

# 2-1 Mybatis配置文件解析过程源码解析（1352）

同学们大家好，这一章节我们来学习一下买 Badcase 配置文件解析过程的源码解析，那么这里面也就是重点，我们在通过买 Badcase 项目启用的过程中， my BAT 是如何解析这些配置文件的？先来看一下对于买卖的解析，配置文件的一些关键的一些路径。


首先我们知道对于配置 MySQL session backdate，它是需要一个 configuration 对象，那么 configuration 对象它是通过我们的 my best config ml 或者说我们的 map 文件去组装而成。其实组装的过程我们知道这是XL，那么这是一个 Java 对象，它们映射的过程是怎么处理的？其实映射的过程是需要一个 xmail configure builder，请延续解析，我们通过 MR configure builder 去解析的过程，我们看到对于 my best configure 里面存在可能的一些元素里面， property setting，我们 type lines， type handler 以及 pack in Maps 或者一些环境信息。那么我们通过这个 config build 一步一步去解析而成的这样一个过程。那么好，现在可以通过我们的 map study 的这个工程去理解一下这个配置解析的一个过程。


好，那么切换到我们的 map start 这个工程，现在我们还是重点聚焦在我们的 Mybest entity 模块上面，这个模块里面我们是基于 my spend 构建这个工程，这里面肯定因为是约定那一配置减少我们的手工开发，这里面肯定没有我们手工构建 config 人的对过程，这里面我们先来了解一下这个工程。


我们先看一下我们的 palm 配置文件，对于这个配置文件，我们看一下我们依赖哪些东西。那第一步也就是我们的 my badcase spring boot STARTER。我们知道其实我们引入这个 my Beta spring boot STARTER，跟 my Betty 相关的依赖，我们就都不再需要依赖了。这里面像 my Betty spring boot auto configure，这个明显对于我们来说它其实是一个嗯重复的依赖，这个是我们可以是直接删除掉的。下面会有一个 map Sam leaf，也就是我们这些对于模板的模板语言的一些支持。


下面有我们的HR，因为我们整个工程是一个测试工程，我们就基于 HR 的数据库进行演示，后面是launbook，是为了简化我们对 b 的一些注射，这里面有 spring boot start 的test，我们这里面还有 my Betis spring boot start 的test，也就是测试相关的一些支持。好，那么我们看了这个依赖，我们来再去想一下。


如果说是想去探究配置文件解析的过程，因为我们是基于 XR 去操作的，所以说我们得去看一下对于 mybadcase 它的 auto configure 相关的一些信息，我们去通过这个追踪的过程找到 mybadcase XR 解析的过程，我们看到这里面是我们的 mybadcase auto configuration，那么对于 my base auto communication，我们看其实它跟通常的 case 很相似。


这里面有 condition on class，我们看有一个 single 的case，这里面也是 date source，还会有一个像 enable configure property，我们配置文件的一些注入，这里面会有一个 auto configure，一个排序的要求，它需要对于 mybadcase auto configure 它需要在 data source auto configure 之后，我们可以看到后面还会有一个 my base language driver out configure，这也是 my base 自己的一个 out config。这个我们不用花太多精力去了解。


看了这些以后，那么我们看一下 my base out configure 出了哪些事情。我们从这里可以看到这里面会涉及到一个 SQL science factory，对于 Badcase 来说， solution factory 是最重要的，所以说我们获取到这个 SQL science factor 的对象也是理所应当的，这里面我们并不是去细究 super session factory 创建的过程，其实我们是想通过 super session factory 倒推它的 configuring 推荐如何构建的。


那么这里面我们看到对于 SQL 30 case，它是通过 SQL 30 factor being 构建出来。对于这里面的我们的 SQL session factor bin，它里面会涉及到 get object 操作，就是构建 SQL session factor 过程。所以说这里面中间跟 factory been 设置属性的操作，我们可以先简单的跳过，我们重点是放哪，重点是看一下对于 factory get object 的操作，获取这个 SQL session factory 它重要的一些思想。


我们来看一下 factory get object 跟进的 factory get object，这里面的操作很简单，这里面是啊，我们看如果说当前的 SQL session factory 等于now，那么我们进行 of the property set，那么通过 our protect 来来去构建这个对象，如果说这个道具体项不等于now，他就直接把所有 30 case 给抛出来了。所以说我们这里面去看一下 off 的 party set 里面做了哪些事情。


我们从这里面能看到，对于 after Pro side 里面，它是首先对于我们的 data source，我们的搜索 session factor b row 的以及我们的clicks，我们的 configuration 进行了一个校验。如果说这些条件都满足，我们现在需要做的事情就是 builder SQL session factory。接下来我们看一下我们的 builder SQL session factory，这里面因为我们是基于绒布的去配置的，可以看到对于这里面还会有 configuration location 的一些设置的特殊性的一些要求。那么我们看如果说这里面 configuration 等于null，那么或者说是且 configuration 那个 location 也等于 null 的话，再满足一个条件，这里面如果说是都不等引导，我看这个表达式可能比较难以明白，所以说我们可以看一下它的属性描述，这里面是 property configuration and configure location，这里面是cannot，如果是它们不能是 specs with together，也就是说它不能同时配置或同时不配置。也就是说我们这两个是必须有一个配置的。


好，我们接下来看一下 build SQL session fact 具体做了哪些事情？在这里面我们可以看到很容易，我们现在已经看到了 XL configure buter，在这里面他做的事情是什么呢？首先会判断一下，在这里面首先声明了一个 final 类型的configuration，我们这里面定义为 target configuration，你看它在构建的步骤还是比较复杂的。首先会看一下当前的 configuration 是否为now，如果不 re 闹的话，我们这个 talk 的 configuration 就把这个属性直接设置过来，同时把一些变量以及我们的 variable 以及变量信息进行一些赋值。


我们可以看另一种情况，如果说我们的 configuration 它等于 now 的情况，那我们来看一下 config location 不等于null，也就是说我们的这个对象为null，我们的 config location 也就是我们的配置文件的 URL 不为null，这是我们比较关注的地方。


如果说我们的 config location 不等于now，也就是说我们有一个配置，这里面这个配置其实最终对应，这里面是 application property，这里面我们可以看到买 Badcase configurity location 它的配置信息，这里面的配置信息我们指定的是 my Badcase 下面的configuration，我们可以从这里面去对应一下，这里面我们可以看到对，在我们的 resource 下面也就是我们对应的略途径里面有 message config。那么基于这一点我们可以看到它。


其实如果说我们在这里面配置了指定location，那就会找到对应的一些属性信息，那么我们还切回来这里面的处理操作，我们可以看到在这里面 config location 指定了我们的 my best config 的路径，这里面就会创建我们的 xmail config build。基于 xmail config build，我们可以看它传入的一些信息，也就是我们的 config location 会获取到我们的 input stream，你可以看一下对于这样一个 config location 对象，它的内容是一个resource， resource 是指什么呢？是指一个配置的URL，可以看到这里面也是配置的我们的一个资源URL，也就是我们的 class pass 协议下面，那么 best configuration，那么还切回我们的 SQL center to be，在这里面继续跟，其实在这里面我们就定位到我们的 Xmail configure builder，基于它进行我们那些逻辑的一些处理就可以了。


切到 Xmail configure builder，那么来到这里我们可以看到跟我们在 PPT 上定义的是 Xmail coverage builder，其实是一致的，我们找到这个 builder 对象，也就是我们的Xmail，我们看到这个命令就是说基于 XL 配置的信息的进行一个构建，这里面构建的过程我们可以看到它其实也是对于构造方法进行了一些重载，最终在这里面执行的过程我们可以看到从这一层我们可以看到它其实通过 x pass 进行一个解析的一个过程。


对于这里面我们最终还会到这样一个处理的过程，我们看一下 Xplus 解析是怎么去解析的？其实我们应该要去了解，对于 XML 的肯定是它涉及到一个解析的过程，解析 XR 通常也是 DOM 破解或 j DOM，那么 j DOM 现在其实用的比较少，大多是用的是 DOM 破解。这里面解析的过程我们可以看到通过构建出一个document，那么这里面我们看到document，对于 document 这个对象，我们这里面用的是 W3 seed 一个协议得到一个 document 的对象。好，这里面我们看到 XL 题的处理的过程，到这里面我们这个构造方法把对象构造出来了。


构造出来我们要做的是什么呢？我们可以看到这里面直接去 get configuration，那我们看一下 get configuration 它做了哪些事情？我们看这里面是好像我们直接得到了一个 configuration 对象，这是如何去获取到的？这就需要我们去想我们是不是在构造方法的过程就已经把这对象构造完成了？所以我们看其实我们得到的configuration，其实它是在构造方法里面直接传入进来的，我们这里面要解析它直接从构造方法传入进来这个对象，肯定它是一个其实刚构建完成这个 control 对象，但是它的一个属性其实并没有初始化的，所以说我们像更外层，我们可以看到它底层的一些实像，可以看到这里面是我们的 XML config builder 还切进来，我们一起看一下在这里面去处理的过程。


其实我们跟到这里面我们可以看到我们直接是 new 了一个configuration，也就是说我们创建了一个 configuration 作为我们的实例，这里面再去获取这个过程，肯定它是没有做什么属性的一些初始化的，所以说我们要去想那么真正的初始化在什么地方去做的。


对于我们 config builder，我们应该讲到它是进要进行一个 POS 解析，我们可以看到通过这里面的方法，这里面最重要的应该就是我们对于解析的一个过程，这个解析的过程我们可以看到它会返回一个 config 的对象，会把我们的一些数据进行一些操作，但我们好像并没有看到显示的调用这个 PROS 操作并不是没有调用，其实是调用了我们只是孩子没有跟踪到，我们可以看到它在这里面的初始化的过程，并没有去调用解析，只是把我们的这个 talk 的 configuration 获取到了。


在 XML config builder 他会去做了一些校验，如果这个 builder 不为闹，会进行真正的一个解析的过程，我们可以在这里面看一下，可以看到在 585 行这里面我们去判断一下 xmail configure builder，如果是它不等于 null 的话，它就会进行解析。


这个解析的过程我们可以看到其实也就是我们 XR config builder 进行解析的一个操作的过程，它在解析的时候我们可以看到因为解析 XML 它会有一定的耗时，所以说这里面它会出这样的操作。首先判断一下当前是不是正在去解析，我们看这个是一个程序运行标志，它为了做一个线程安全，就是做一个安全性。如果说当前这个 part 正在执行的，那么这会就抛出一个异常，告诉这里面的 x mark builder on，也就是只能由一个线程进行一些解析。如果说这里面没问题，我们先把我们的 POS 的标为true，同时我们进行解析的操作，注意一下这里解析的操作。


我们看一下 evil note，它首先找到 configuration 这样一个节点下的内容进行处理，它下面的内容怎么去看？我们可以看一下 Web configuration，它其实找的内容是把这个作为一个根节点，也就是把里面的每一个元素获取出来进行解析，所以说这里面解析的过程我们可以看看它这里面是怎么解析的，在这里面点了个断点解析的过程首先是 property 元素，你们也说首先是 practice 解析出properties，我们在解析settings、我们的配置以及 type lines、 Tech in、 object factory 等等这些属性的一些信息。这里面我们其实比较关心的一个是我们的上下文属性，我们还涉及到一些 type handler 以及我们的maps，其实 map 是更重要的一些信息。


通过看到这里我们知道整个这个解析的过程，其实就开始了这里面具体的一些解析的内容，它就会涉及到一些 XML 的操作，我们可以进去第一个看一下这里面的操作，我们可以不用花太多的精力去了解，只是知道它在怎么步骤去进行解析就可以了，因为这个解析的过程也就是 IQ2 解析，平常我们去写 IQ2 解析，找准对应的 API 进行处理就可以了。


OK，这样的话我们可以看到它是在这个过程进行了我们的属性的一些解析。好解析完成以后它需要做的事情是什么呢？首先这 POS 它就已经认为是解析过了，这个值就变成true，它就不会再进行二次解析了。那么这样的话我们可以看到了对应我们这个配置文件解析的过程，是通过 XML config builder 进行一些解析的过程。有一点我们需要注意的，其实我们解析的过程中也就是把我们的属性设置的过程，我们可以看到最终我们解析的这些属性，它都会通过我们的 configuration 这里面 set variable，也就是说把我们解析的过程跟我们当前这些，比如说当前 configuration 所有的这些信息进行一个MOS，把数据进行 MOS 完以后，把这值设置到我们的 configure property 里面。这里面我们就理解其实解析的过程，也就是说把 XL 里面各个元素的属性获取到，同时把它放到我们的卡佩克对象里面，那么就完成了一个解析的过程。好，那么关于买 Badcase 配置文件解析的过程，我们就先继承到这里，同学们，我们下一章节再见。

