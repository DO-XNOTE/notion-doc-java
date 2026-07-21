---
title: 3-3 RabbitMQ基础组件API封装-1
---

# 3-3 RabbitMQ基础组件API封装-1

[image](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/9de8cd1e-6f65-4478-a4ed-69119986b309/SCR-20240806-orim.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SFZGBIAW%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T225258Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIC56fwm73Zbn%2FYZGJrFAbmEho%2BSoPoFBpWHoGtEfvX2XAiBRlnp2d%2FWC5BcQ8zDLViuIKTUmqQ8OnYHxvuAxkFj%2FgCqIBAjG%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMSwr%2BBuKApNdGbuQqKtwDtK%2F58KHiK019oaMtOVpW0mtvfN3gPkyMdPw8fXPSpbzuvsrDYgpj%2BbvXJ6oXKzeCTqyh0P88bm77Wg2d%2FLELuLnuV7AzuXymhjwRvWw6C92sBtxUfdLh3Ni07g2fTPC%2BOc9ZiVI9cS67k9puM9K64I8y7Cni5FVHMKSzwJlb6K1JN1RQR7s8CYojVdooluISs1tHJaWovFH52v%2BIPk1LwyG0xCnaOaif2R6xbJ0bLiOrZYhM9u8tkG3%2BI6m%2BZcZGF%2FvJGk0x%2F3ENR0HFA4P2eMh1OeY5e2cz4%2BBIhVltmCmWBHNq%2FOu7Y7%2Ftqm6KTGVkUCMOV2%2BkQx%2FoULrwGxLgTaWMvxGYuE5dQQrODg%2F9dIAaNBQXIwm5ElLFNlcFZXg%2Frd04kC8FOyozlhWUwhNHOa8amo4XZucV6MKCGFF4uCYUb7Y0iRROyjkpPUZwTwGBVV%2FDUQjD3Y77%2BTSsdFmLulG8Kx5fqxLDupHq6uQzou8ss3xG1KhbMiG38wLhzUAMcUIL8LTDsbJSLJAKq%2B6GaH%2BTsceBmdmiydW3eD25MQIQUSBho327j0l204jYu28Z97tbdO7fVSuK7%2BMM8f%2BVtkUW9vA7ETkAlLuxeUacKpcOkitMu4Bs24c0xYcwubj%2F0gY6pgGYrGZ82VuSHcapmJneV%2FMhKqDw8IOAbyPsXIfD0h%2FaqlV1GPme41GpZhtDP8OmZCTDmxREBUFzsYBW7gQ08rwxU1L3TedsrDGL%2BcI8RQ2pP2kj2Ie8mya55Bm%2BpIEdQ6uZfUE7RZY%2F1RjpsjfECIhh3%2B7YwWVgRQVVE7wjmc5pWZ%2FgdeWj2IvJzDdLXbkHJl9N4WHAPDnhS7RQjTlS%2BAFyWKcm0%2Bm8&X-Amz-Signature=40b392648d8944c042d1ce462c2edbe5d663e39a7ac583e9fee63bb396800888&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

[image](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/3bda04f0-caae-4889-b3c3-622ff931faba/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SFZGBIAW%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T225258Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIC56fwm73Zbn%2FYZGJrFAbmEho%2BSoPoFBpWHoGtEfvX2XAiBRlnp2d%2FWC5BcQ8zDLViuIKTUmqQ8OnYHxvuAxkFj%2FgCqIBAjG%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMSwr%2BBuKApNdGbuQqKtwDtK%2F58KHiK019oaMtOVpW0mtvfN3gPkyMdPw8fXPSpbzuvsrDYgpj%2BbvXJ6oXKzeCTqyh0P88bm77Wg2d%2FLELuLnuV7AzuXymhjwRvWw6C92sBtxUfdLh3Ni07g2fTPC%2BOc9ZiVI9cS67k9puM9K64I8y7Cni5FVHMKSzwJlb6K1JN1RQR7s8CYojVdooluISs1tHJaWovFH52v%2BIPk1LwyG0xCnaOaif2R6xbJ0bLiOrZYhM9u8tkG3%2BI6m%2BZcZGF%2FvJGk0x%2F3ENR0HFA4P2eMh1OeY5e2cz4%2BBIhVltmCmWBHNq%2FOu7Y7%2Ftqm6KTGVkUCMOV2%2BkQx%2FoULrwGxLgTaWMvxGYuE5dQQrODg%2F9dIAaNBQXIwm5ElLFNlcFZXg%2Frd04kC8FOyozlhWUwhNHOa8amo4XZucV6MKCGFF4uCYUb7Y0iRROyjkpPUZwTwGBVV%2FDUQjD3Y77%2BTSsdFmLulG8Kx5fqxLDupHq6uQzou8ss3xG1KhbMiG38wLhzUAMcUIL8LTDsbJSLJAKq%2B6GaH%2BTsceBmdmiydW3eD25MQIQUSBho327j0l204jYu28Z97tbdO7fVSuK7%2BMM8f%2BVtkUW9vA7ETkAlLuxeUacKpcOkitMu4Bs24c0xYcwubj%2F0gY6pgGYrGZ82VuSHcapmJneV%2FMhKqDw8IOAbyPsXIfD0h%2FaqlV1GPme41GpZhtDP8OmZCTDmxREBUFzsYBW7gQ08rwxU1L3TedsrDGL%2BcI8RQ2pP2kj2Ie8mya55Bm%2BpIEdQ6uZfUE7RZY%2F1RjpsjfECIhh3%2B7YwWVgRQVVE7wjmc5pWZ%2FgdeWj2IvJzDdLXbkHJl9N4WHAPDnhS7RQjTlS%2BAFyWKcm0%2Bm8&X-Amz-Signature=d3b85102ff60f5cbd3fd987ef16ff229536a26f2f795bb37c3e7fa62d358e942&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

OK，小伙伴们，那我们上节课呢，已经把分包这个问题搞定了，那接下来我们来看一看，具体我们应该从哪一个模块或者哪一个包去入手了。那作为一个架构设计者，那我个人觉得你首先应该把通用的 API 做一个抽象，这是最关键的。OK，那所以说我们就把目光定位到 Rabbit 杠 API 这一层，那 Rabbit 杠 API 这一层我们都要做哪些事情？小伙伴们想一想，那首先你要做的事情是要发送消息，那你要发送消息是符合你自己业务的消息，你把消息归于我们的迅速消息，以及我们的延迟消息，还有可靠性消息，对吧？你把消息分成了这三类，说白了你就要对这三类做一个统一的消息的封装，对不对？OK，那接下来我们想一想这个实体应该怎么去抽象？在这里我们开始去做。


首先我们来定义一个包名叫做Com，点 BFX y 点 Redis 点API。好，这个包我们已经写好了。然后我们现在要对发消息进行封装，所以说很显然我们要做一个 message 这么一个类，这个 message 类主要做什么事情？就把我们自己所定义的一些消息做一个规划好，我们来写一写这个message。


首先第一点，我们最好一定是实现这个 Siri elizable 接口。然后接下来我们要做一个事情，就是要生成一个 depot ID，对吧？接下来我们来看一看它有哪些比较关键的属性。我们需要做一个封装，首先第一个 private string 类型的，我们叫做 message ID，这个作为一个唯一的消息ID，对吧？好，那么以后我们发消息就是以这个 ID 当成一个唯一的标记了，在这里我们引入了这个 long book，所以说我们直接叫 date 就好了，不需要说生成什么 set 方法。

接下来对于 ready MQ 它的一些特性，我们应该考虑封装了。比如说我们有一个 private string 类型的topic，虽然说 Rabbit m q 里边它是一个什么 exchange 的概念，那其实那么我们完全可以把它抽象成为一个topic，那可能我们在设计之初，我们就已经定义好了我们自己的整个的 exchange 的类型，我们就可以把它当成一个 topic 类型，这样是不是可以或者你又选择 direct 类型，或者你选择 front 类型或者等等？甚至于 header 你可以选择，但是其实为了统一性，我没有去说再去做一层 exchange type 的这么一个封装。


OK，在这里根据需求你也可以有，但是在这里我就不需要去做这个事情了，我们就叫做消息的主题，消息的主题就是我们的什么呢？我们的top。那其实呢，你既然选择 topic 类型了，那必然你就会有一个什么东西。对于 rap MQ 的exchange，如果是 topic 类型的，那很明显会有一个 routine key 的这么一概念，对吧？默认我们可以给他一个空的字符串，那这个就表示什么呢？表示我们的路由规则类似智能表达式，就是一个星号或者是井号的方式，对吧？就是什么什么点星，然后点井号这种方式。那我叫做消息的路由规则。


好了，有了这 3 个属性，这是比较关键的。那接下来我们再想一想，有没有什么特殊的内容呢？比如说我们现在想传递一些特殊的属性，像最开始 rap MQ 的时候，如果想要传递一些特殊的属性，那应该放到哪里？它应该有一个 Mac 类型，所以说我们在这里搞一个private，我们的 Mac Java util，然后可以是 string 类型的这个object，对吧？它的 key 是string， value 是object。那我们可以给他起个名字叫做attributes。对，弄一个哈希 map 就好了哈，好，另外一个哈希map。然后接下来我们再看现在我们消息分为哪几种？首先迅速的消息，然后延迟消息，考虑延迟，我想去延迟发送怎么办？是不是你应该有一个属性，去标记一下你延迟多长时间，然后在这里我叫做 delay in minutes，就是消息的延迟的时间，就是延迟消息的参数配置，只有延迟消息可能才会用到这个配置。然后这个我再打注释，注释是非常关键的，叫做消息的附加行。


OK，好了，那接下来还有哪些属性？比如说消息类型对不对？消息的类型一定要有，那我对于消息分为了 3 种，如果说你是延迟消息，那这个肯定不为零，对不对？它可能延迟一分钟，延迟多长时间？那它肯定会配置，默认的话，那是不是可能它也不会配置啊？所以说一个最关键的内容就来了，就是我们的消息是什么类型的？它可以是四肢类型的，我们叫 message type t i p 等于什么呢？我们先来一个空的字符串来代替这个表示消息的类型，然后接下来我们是不是会有一些构造方法生成这个构造方法，让它有一个有餐的构造方法，然后还有一个无餐的构造方法，对吧？有两个构造方法。

好了，那么接下来其实就搞定了，这个类我已经写完了，是吧？然后接下来我们考虑考虑这个消息类型的。消息类型我们可以给它一个简单的一个类叫做 message type，对吧？可以给他一个简单的类，叫做 message type，大写这个 message type 可以是，比如说它可以是 final class，对不对？反正它也不会变，定义好了就可以了。


okay，我们叫做 public final，然后static，然后 string 类型的好，我们比如说叫做repeat，好设置一个0，这什么意思？这个叫做迅速消息，我给消息定义一些类型和迅速消息。迅速消息代表什么含义？在这里打出是不需要保障消息的可靠性，然后在这里也不需要做confirm，确认这里边这个迅速消息，它就是说不需要保证可靠性，也不需要做可以费用就这么一个事儿。然后接下来我们继续来看第二种消息，第二种我把消息归为这种类型，叫做 final 的static，然后这类型的叫做confirm。好，这个默认给它写成1。这什么意思？这个叫做确认消息，这个正好契合了我们 rap MQ 的这种类型了，就这种消息它默认会有这种确认投定制机制，它会有一个这个 call back，之前讲这个 spring boot 整合 red MQ 的时候已经讲过了，他说不需要保障消息的可靠性，但是会做 config 确认，会做消息的 confirm 确认这样去说。然后接下来就是第三种了。


第三种是什么概念？就是一定要保证可靠性的，我们在这里 public final static 或者是 public static battle，是不是 public static final？这样读起来感觉更顺溜一些？我个人是这么觉得的，然后 string 我们叫做可靠 related 这个单词，你可以自己找一个单词，那我们在这里就叫做它是可靠的，那就是可靠性消息。那这是什么意思？一定要保障消息的百分之百可靠性调低，不允许有任何消息的丢失，就是做这个事情。


那说白了同学们想一想，那这种机制它是一个什么概念呢？在这里也就是说我们通常去做可靠性消息的时候，可能就是要跟数据库保证一个原子性。比如说我在发消息之前，我记录一个日志，然后我把数据的落库了，落完库之后消息发出基数，给我一个confirm，我去应答的时候我去再更改一下，数据库里边我记录那个日志的一个状态，那这个才叫一个可靠性，对吧？那这种就是保障数据库和所发的消息是原子性的，严格的原子性，它其实也不是，因为它就是用一个兜底，一个补偿的策略去保障了，所以说你可以认为它是一个最终一致的。


好了，后面的时候我们会把可靠性消息从 0 到 1 的跟大家把这个讲清楚。现在呢，你就先知道我消息可能有这 3 种类型就可以了。OK，记得打好注释，这都是一个规范。OK，那我们现在对于消息类型已经确认了，那我们同学想一想，默认是不是消息也可以有一种类型？默认消息类型是什么样子？比如说我们默认就是表示消息是 confirm 的，可不可以？也可以，对不对？我说消息的 message type 默认它就是 confirm 类型的，如果你不写，那它默认都需要进行confirm，那其实你可以给它一个默认的类型，就这意思。


OK，那在这里可以打开注释，默认为 campaign 消息。好了，已经写完了，最简单的，最上层的最基础的抽象了，那接下来小伙伴们能不能说搞一点小的设计模式，那在这里有一个比较初级的设计模式，那我跟大家一起完善一下。比如说我们的消息，每次去创建的时候，你可能都要去 new 这个message，对吧？有没有一种这种 build 的模式，也就是建造者模式，这样写起来我们可能会更舒服一些，那在这里很多开框架可能都使用了这种建造表模式，所以说在我们去讲这个基础组件封装的时候，老师也会带着大家去尝试去多写一写各种各样的设计模式，让大家在写代码的同时去把自己的这个设计模式真正的去用上，这也是一个编码你自己怎么去提高的一个过程。


那其实我期望小伙伴们，无论是你在做业务代码开发，还是在去做这种基础组件的封装的时候，一定要多写一写，多动脑筋，把你的代码写得更优雅一些，可能这个才是最关键的。好了，废话不多说了，我们再写一个，那在这里我就给他起个名叫做 message builder，那 message builder 顾名思义就是 message 的这个建造者。好，那建造者模式应该怎么去实现呢？在这里首先第一点我要跟你说，建造者模式默认的这个成员变量要跟你想要见证的对象一定是一致的。我这里边有这几种类型，那我是不是也应该有我们想要的那几种类型？所以说第一点就是说我们要把这几种类型原封不动的 copy 到我们的建造者模式里，这是必须得有的。然后把最基础的建造者模式里的类型在这里，我就把这个柱子都去掉了，让它这个紧凑一些。


接下来我们去做这个建造者的这个编写。这个建造者的编写我们应该怎么去做？好？那在写之前我们来看一看哈，看一下这个 message 默认的给我提供了一个有参的构造方法，是全参数，对不对？它有默认值的。其实你更好的方式是再提供一个构造方法，我把这个 message type 去掉是不可以，对吧？然后把最后这个 message type，我把它去掉，看一下，把它去掉。好，那这块其实你可以原封不动了，默认我也是这个 cancel 模式。那你想加就加，不想加默认就confuse，其实你也可以不写，无所谓。


好了，第二步就是构造函数的私有化， message builder 一定要把它私有化 private 好，把它私有化了以后接下来怎么办？那你对 i 是不是应该提供一个静态的这个创建它的一个方法？那我们可以搞一个叫做 message build，返回的是 message build 对象，然后我们叫做 create 可以或者是 build 好这个 create 方法，我们就返回 pretend new 一个 message order 就好了，返回当前 new 一个 message build，就是当前这个对象本身。

接下来就是让它有这种链式编程的效果，那就是 return 的时候都 return 这个 mastbued 就是 this 就可以了。好，那我们在这里来写一写，其实有很多，比如说我们叫public，返回值都是自己本身public，然后我们叫做 with 什么呢？ with message ID，可以直接把当前的string，然后叫做 message ID 传进来，然后这里边叫做 this 点 message ID。

We must rent it a whole return this.


就可以了，然后除了他以外还有几个你都可以写上来。好，我们第一个位置 message ID 写了，是不是？然后第二个就是我们的topic，不是我小妹子一个topic，对吧？然后把这个里边 topic 放进来，然后就是 this 点 topic 等于topic， topic 完了之后，那就下一个就是 routing key，是不是？这个 routing key 你是不是应该加一个呀？你要想加也可以，对不对？这个里边把它移上来，入侵t，在这里入侵t，是吧？然后把这个改一下，把这个 r 大写，然后 root k 完了之后还有什么呢？看一下。


还有这个attributes，是吧？ attribuce 很明显是一个map，那我们来看一看，那我们在这里叫做 with attributes，那这个里边它传的肯定是一个map，所以说你要把它这个类型来变一下string，然后是object，对吧？OK，然后位置attributes，这个 a 大写可以了。然后接下来我是不是应该还有一个位置 attribute 车为了写全把这个 s 去掉，然后这里边给我来一个简单来讲，比如说来一个key，对不对？这是最基础的 API 设计了，然后是一个object，咱们叫做value，那这个怎么去做呀？那肯定是要取到上面这个this，然后点put， put 我们当前的这个 PV 键值，对就可以了，就是往里去添加一个一个的属性嘛？OK，然后最后 routine t 也搞定了，最后我们就差哪个了？就差这个 delay 了，是不是？这个 delay 就是我们的延迟，对吧？那叫做位置 delay 哈。


先写一写这本书，改成 a 大写的，然后这个它是 Int 类型的，然后弄错了，还有最后一个，是吧？还有最后一个是什么呢？还有最后一个就是你的 mess type，你想不想？有的话你也加上，反正默认是什么呀？默认是这个 confirm 方式。那你就 with message type，来个 with 我们的 message type，然后这个我们拿过来，它也是 4 种类型的，这些就是硬编码了，是不是？好，你有的话你就加吧，没有的话你默认，你要不写它，我默认它就是这种 confum 类型的。其实这个你也完全不用写，因为就算你不写，构造的时候默认也是 config 类型的。


好了，然后我们第二步这些链式编程已经搞定了，最后要调自己的一个方法叫做 build 的方法，它返回的就是建造者本身的那个对象，就是message，然后我可以写一个 build 的方法，这个 build 方法很简单，我在这里就 new 一个 message 返回就可以了。我说 message 等于 new 一个message，用我们最多的那个参数，对吧？改回就可以了。


好，然后最后 return 我们的这个message，这就写完了。但是检测者模式其实更重要的一点就是它能帮我们做一个提前的这个预判，比如说我们要求这个 message ID 必须有，你没有 message ID 肯定是不行的，或者你没有Sid，我帮你去做一个生成，然后 topic 也这是必须要有。


我连你投递的哪个主题我都不知道，那我是不是干脆就可以不帮你去创建？所以说这里边其实你可以做一些自己个性化的一些判断，比如说如果 my Cid 等于none，就是你没有传嘛？没有传 s i d 的话，我可以去帮你去生成一个，对不对？那我就可以说 m s c i d 等于 u i d，我们就 Java 油条随机的去帮你去 to string 生成一个 message ID，这也可以吧，对吧？你不传的话我也帮你生成，我为了保障这条 message 不会出现问题。


然后比如说topic，我去生产一个 message 时候，我的 topic 是不是必须要有？没有的话我们直接可以抛异常，比如说我们可以抛我们自己的一个异常，比如说我们叫做 message exception，我们可以就往出 throw 一个我们自己的 message exception，如果 topic 等于空了，你就阻断它不让这条 message 生成好，OK，那是不是我们可以再去做一些基础的封装？比如说我举个例子，在这里边我们再来一个简单的包点，咱们叫做 Exe p t o n exception，其实这都是一些最基础的基础组件，你要做的一些封装的一些基础要点。


exception 我应该怎么去做？对于 exception 而言有两大类，第一大类叫做 runtime exception 在运行的时候出现的一些问题，第二类可能就是exception，可能在某个节点，你可能在初始化的时候没有去加这个参数，然后我会强行的去把这个抛出这个异常，就不让我们程序去运行了，可能就会有这么一个情况。


那其实呢？像我们现在这个需求就是我们的 topic 等于空，那这肯定是程序运行起来之后，然后发现了第一次 check 的时候发现你的这个 message ID 没有去写，那我可以帮你做一个补偿嘛？第二次 check 的时候发现你的 topic 等于 none 的话，那肯定是你运行，就是我程序已经启动起来了，发现你 topic 等于none，那这种情况很明显，我要抛出一个 runtime exception，这个比较合适，对不对？让我们的程序直接阻断掉，我们编译器肯定不会出现问题嘛。

还有一个就是我初始化的时候，比如说，唉，我初始化一个类的时候，压根参数传的就不对，那就不是 run time 了，就运行时你就可以把它给它阻断，就这个东西服务可能就起不来了，那这个时候你就不需要去用这个 run time 了。好了，那我们来说一说规则吧。


最基础的类我们可以来一个 base 类，对不对？我们叫做 message base exception，或者是我这么去起就叫做 message exception， d s e p t a l n message exception，这个 message exception 它可以去 exist 继承我们的exception，可以，然后这个继承了 exception 之外，就是我应该去对于 default ID 做一个生成，生成了之后比如说它有一些 cancel 构造方法，比如说 public message。我这个我是不是可以调一个super？是调它的父类，也就调那个 exception 的父类，对吧？我可以调它，然后比如说这个 message 是不是可以传一些参数？比如说我叫public，有好多构造方法都写一写好，比如说我可能这种异常，它既然是 exception 了，我需要一个描述，对不对？说 message 的描述是什么呢？我就直接 super 把 message 放进来， m e， s s， h e 放进来，对吧？这是一种构造容器。


然后还有哪些？比如说他抛异常了，就是那除了有具体的异常信息之外，可能我要把堆栈，这个我可以写的比较大，我们叫做case，把这个取出来，然后把这个东西扔进去，对吧？也可以。然后接下来，比如说我觉得这个我不需要message，是不是？我可以这样，我可以把这个去掉？这些都是一些比较基础、比较简单的这个封装的一些套路。


其实做基础组件做多了之后，你会发现这些东西也是大同小异的，就是可能唯一不同的就是一些设计上可能你自己要花点心思，就是基础的套路其实都是差不多的，就跟你去写 Ctrl 了，写c、r、u、 d 一样，不就是那些套路吗？音色塔先访问API，然后把所有的参数都拿到，然后拿到之后再做一层转换，做一层 validate 数据校验，这样你都通过了，然后做一次入库，然后再返回或者是在 RPC 调下游，对吧？这些都是大同小异的，一样的。


OK，好，那这个 message 我写完了之后，是不是我还可以写一个？比如说我是不是还可以做一层什么 RT 啊，什么什么的，是不是也可以？这个是没问题的，比如说现在我们再来一个类，这个类我们叫做 r t，叫做 runtime message， runtime exception 你可以去继承它，但是你继承它之后你就没法去继承 runtime excess 了。所以说你可以单独提出来。


如果你有 runtime 的需求的话，你比如说像我们刚才那个其实就有 runtime 需求了，那我就来一个 runtime exception。好，然后剩下的这个里边它也有default，我把它也 generate 出来，然后其他的我可以跟它保持一致的朋友都 copy 下来，这样的话就分为两大类了。然后这个我都改一下，其实都是大同小异的，都可以不用去变化。来，同学们想一想，那这个就专门针对于 run time 的时候，在运行的时候如果抛这个异常，我都可以放到这里。然后下面这个就是可能是在一些初始化的过程中出现异常，我们可以用这个类了，这就是最简单的区别。然后在这两个 base 异常，我们还可以具体定义一些特殊的异常，生产者发消息失败的时候可能就是runtime，那我可以继承这个 message runtime exception 这个类，然后再去扩展，比如说叫做 message producer send exception，叫做 message consumer receiver exception 等等就是我们去定义各种各样的异常。


其实这个东西就是一些最基础，做基础组件的封装，最关键的是什么呢？最关键的是你的 Java 基础好，回过头来我们的 topic 如果是空，相当于发送一场，那我完完全全可以去做一件事情，对不对？刚才我已经写了 through new，我们的就叫做 message runtime exception，然后传进参数是不是 topic is not 就可以了，对吧？我就抛出一个运行时异常好了，非常简单的一个建造者模式以及基础组件最基础的一些 API 的抽象就是关于 message 跟 message builder，以及 message type。还有我们怎么去定义异常这节课老师呢？已经讲清楚了。OK，感谢小伙伴收看。






```java
package com.bfxy.rabbit.api;

import java.io.Serializable;
import java.util.Map;

/**
 * <h1></h1>
 */
public class Message implements Serializable {


    private static final long serialVersionUID = 841277940410721237L;

    /**
     * 消息的唯一 ID
     */
    private String messageId;
    /**
     * 消息的主题
     */
    private String topic;
    /**
     * 消息的路由规则
     */
    private String routeKey;
    /**
     * 消息的一些其他附加信息
     */
    private Map<String, Object> attributes;
    /**
     * 消息的延迟参数
     */
    private int delayMills;
    /**
     * 消息的类型
     */
    private String messageType;


    public Message() {
    }

    public Message(String messageId, String topic, String routeKey, Map<String, Object> attributes, int delayMills, String messageType) {
        this.messageId = messageId;
        this.topic = topic;
        this.routeKey = routeKey;
        this.attributes = attributes;
        this.delayMills = delayMills;
        this.messageType = messageType;
    }
}
```

[image](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/bd0eb84e-ed3a-4117-ac95-139f500d17bf/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SFZGBIAW%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T225258Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIC56fwm73Zbn%2FYZGJrFAbmEho%2BSoPoFBpWHoGtEfvX2XAiBRlnp2d%2FWC5BcQ8zDLViuIKTUmqQ8OnYHxvuAxkFj%2FgCqIBAjG%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMSwr%2BBuKApNdGbuQqKtwDtK%2F58KHiK019oaMtOVpW0mtvfN3gPkyMdPw8fXPSpbzuvsrDYgpj%2BbvXJ6oXKzeCTqyh0P88bm77Wg2d%2FLELuLnuV7AzuXymhjwRvWw6C92sBtxUfdLh3Ni07g2fTPC%2BOc9ZiVI9cS67k9puM9K64I8y7Cni5FVHMKSzwJlb6K1JN1RQR7s8CYojVdooluISs1tHJaWovFH52v%2BIPk1LwyG0xCnaOaif2R6xbJ0bLiOrZYhM9u8tkG3%2BI6m%2BZcZGF%2FvJGk0x%2F3ENR0HFA4P2eMh1OeY5e2cz4%2BBIhVltmCmWBHNq%2FOu7Y7%2Ftqm6KTGVkUCMOV2%2BkQx%2FoULrwGxLgTaWMvxGYuE5dQQrODg%2F9dIAaNBQXIwm5ElLFNlcFZXg%2Frd04kC8FOyozlhWUwhNHOa8amo4XZucV6MKCGFF4uCYUb7Y0iRROyjkpPUZwTwGBVV%2FDUQjD3Y77%2BTSsdFmLulG8Kx5fqxLDupHq6uQzou8ss3xG1KhbMiG38wLhzUAMcUIL8LTDsbJSLJAKq%2B6GaH%2BTsceBmdmiydW3eD25MQIQUSBho327j0l204jYu28Z97tbdO7fVSuK7%2BMM8f%2BVtkUW9vA7ETkAlLuxeUacKpcOkitMu4Bs24c0xYcwubj%2F0gY6pgGYrGZ82VuSHcapmJneV%2FMhKqDw8IOAbyPsXIfD0h%2FaqlV1GPme41GpZhtDP8OmZCTDmxREBUFzsYBW7gQ08rwxU1L3TedsrDGL%2BcI8RQ2pP2kj2Ie8mya55Bm%2BpIEdQ6uZfUE7RZY%2F1RjpsjfECIhh3%2B7YwWVgRQVVE7wjmc5pWZ%2FgdeWj2IvJzDdLXbkHJl9N4WHAPDnhS7RQjTlS%2BAFyWKcm0%2Bm8&X-Amz-Signature=a98dfd32d07536650c11843b3ef18b08e1912b6588fcd66e55f9c315d9123ccb&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

## 

### 


