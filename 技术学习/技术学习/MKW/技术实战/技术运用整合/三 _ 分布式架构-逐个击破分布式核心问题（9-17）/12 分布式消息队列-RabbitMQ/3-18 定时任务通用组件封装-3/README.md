---
title: 3-18 定时任务通用组件封装-3
---

# 3-18 定时任务通用组件封装-3

[image](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/ab287457-2bce-4bbb-b007-3dfd49f1b376/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667G5P3YFI%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T225310Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDAKnh8klk4W6vLhi%2BbIYvdbl2ZvL5Qe%2B%2BTCdhUedH%2FEAIgAr%2BmSG2hloXoWU9FNLvl30L0D%2BdfXFm5NCsKkUhdH%2FQqiAQIxv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDKMtW995sG7Eu9jU4CrcA9y1lcOvUg2HXOdo3kJygwAgeN7IzfUIp3bdZLjdUnqaT94MiRabhLE%2FMyG6xvSSTEeWzXW%2FOHchNMYia9ytrL6cVSG5IDp03CG%2BXcXeZ9sjoqK%2FQEMoOEsFAjVSvR5P2eVlao5xhSw5P59USj7I0xtITqbk%2FAFyyKOlKP%2BAwDW5tkI1Ym88Tbo5cxCMlSUmxBrnFIZJxYddoTsqljFWvdBJomyjgfw9%2B4AMzj%2B8UeOg5sG7eZgGrv8JKhkDSymauX%2BObSvKXf4D9ZxiZb6YZFd9G7UPCXby1idI4ArRemXUd0bkzNC%2B359g45%2FXeDrkixOZZ2y%2Fw5JcgPyzFWlFcyeMsgMbqbAYWp8eAIEfXaRpfubciQDRQBf6zeEhzPYlx62qoNeyS5LpwV5tkRWIXqRuA%2BExHZqVoDlQh5A7lDo49qnUYprBF0IvToPesnjWrLQ3dxlXVddFzQt6Zv2xEi2rrDEvzTI0TIOwxA7TN0YdxZ1X2RZQG66O1aT5zecRGF9z2fgIpgKusZxGg2Y%2B3Ea0R9LfNjL2RzBU8V26iiVXvkoK0MM4UHJNMrgj6%2FgzDiXmcQ4MJ3WH2QQRuDGDYhg3J1giljoETCK15t1QmLK7%2BYLiAuXF5J3peGfBMNe6%2F9IGOqUB7NYSNMbDfyhJTPCEZ78wYfrMr23O2GsMEaOpat%2FDPqoz0Jue%2BQVIuPGJGcjlS8m7iL4KrUgloSJtywPg9vBmMmEgxibrSgpZWB1p8iDsEtXnaLjaYgeQbG3BybtOaZcLx8l%2FcCYf1p1zqEmhbMe7pMNAaYuj7utU0qUVpVqHc8nawZ%2BKfTCdKw0RG0E0xbpQT%2FZWuQfquZw84BgOP4wuHP4RnNXy&X-Amz-Signature=4c24fd8d9df499659cdffdd5d48863f2fbfbdff5418df6bd51a40adf2709d19d&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

[image](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/095ca6f6-eb3f-4e14-aba7-bcc7a77580eb/SCR-20240806-tayk.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667G5P3YFI%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T225310Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDAKnh8klk4W6vLhi%2BbIYvdbl2ZvL5Qe%2B%2BTCdhUedH%2FEAIgAr%2BmSG2hloXoWU9FNLvl30L0D%2BdfXFm5NCsKkUhdH%2FQqiAQIxv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDKMtW995sG7Eu9jU4CrcA9y1lcOvUg2HXOdo3kJygwAgeN7IzfUIp3bdZLjdUnqaT94MiRabhLE%2FMyG6xvSSTEeWzXW%2FOHchNMYia9ytrL6cVSG5IDp03CG%2BXcXeZ9sjoqK%2FQEMoOEsFAjVSvR5P2eVlao5xhSw5P59USj7I0xtITqbk%2FAFyyKOlKP%2BAwDW5tkI1Ym88Tbo5cxCMlSUmxBrnFIZJxYddoTsqljFWvdBJomyjgfw9%2B4AMzj%2B8UeOg5sG7eZgGrv8JKhkDSymauX%2BObSvKXf4D9ZxiZb6YZFd9G7UPCXby1idI4ArRemXUd0bkzNC%2B359g45%2FXeDrkixOZZ2y%2Fw5JcgPyzFWlFcyeMsgMbqbAYWp8eAIEfXaRpfubciQDRQBf6zeEhzPYlx62qoNeyS5LpwV5tkRWIXqRuA%2BExHZqVoDlQh5A7lDo49qnUYprBF0IvToPesnjWrLQ3dxlXVddFzQt6Zv2xEi2rrDEvzTI0TIOwxA7TN0YdxZ1X2RZQG66O1aT5zecRGF9z2fgIpgKusZxGg2Y%2B3Ea0R9LfNjL2RzBU8V26iiVXvkoK0MM4UHJNMrgj6%2FgzDiXmcQ4MJ3WH2QQRuDGDYhg3J1giljoETCK15t1QmLK7%2BYLiAuXF5J3peGfBMNe6%2F9IGOqUB7NYSNMbDfyhJTPCEZ78wYfrMr23O2GsMEaOpat%2FDPqoz0Jue%2BQVIuPGJGcjlS8m7iL4KrUgloSJtywPg9vBmMmEgxibrSgpZWB1p8iDsEtXnaLjaYgeQbG3BybtOaZcLx8l%2FcCYf1p1zqEmhbMe7pMNAaYuj7utU0qUVpVqHc8nawZ%2BKfTCdKw0RG0E0xbpQT%2FZWuQfquZw84BgOP4wuHP4RnNXy&X-Amz-Signature=55e9a285c091b0e6b107705e017d03ca06b494f32920550caf8c7937960c65d2&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

[image](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/bedc14b3-4818-47f8-8139-667077575a6c/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667G5P3YFI%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T225310Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDAKnh8klk4W6vLhi%2BbIYvdbl2ZvL5Qe%2B%2BTCdhUedH%2FEAIgAr%2BmSG2hloXoWU9FNLvl30L0D%2BdfXFm5NCsKkUhdH%2FQqiAQIxv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDKMtW995sG7Eu9jU4CrcA9y1lcOvUg2HXOdo3kJygwAgeN7IzfUIp3bdZLjdUnqaT94MiRabhLE%2FMyG6xvSSTEeWzXW%2FOHchNMYia9ytrL6cVSG5IDp03CG%2BXcXeZ9sjoqK%2FQEMoOEsFAjVSvR5P2eVlao5xhSw5P59USj7I0xtITqbk%2FAFyyKOlKP%2BAwDW5tkI1Ym88Tbo5cxCMlSUmxBrnFIZJxYddoTsqljFWvdBJomyjgfw9%2B4AMzj%2B8UeOg5sG7eZgGrv8JKhkDSymauX%2BObSvKXf4D9ZxiZb6YZFd9G7UPCXby1idI4ArRemXUd0bkzNC%2B359g45%2FXeDrkixOZZ2y%2Fw5JcgPyzFWlFcyeMsgMbqbAYWp8eAIEfXaRpfubciQDRQBf6zeEhzPYlx62qoNeyS5LpwV5tkRWIXqRuA%2BExHZqVoDlQh5A7lDo49qnUYprBF0IvToPesnjWrLQ3dxlXVddFzQt6Zv2xEi2rrDEvzTI0TIOwxA7TN0YdxZ1X2RZQG66O1aT5zecRGF9z2fgIpgKusZxGg2Y%2B3Ea0R9LfNjL2RzBU8V26iiVXvkoK0MM4UHJNMrgj6%2FgzDiXmcQ4MJ3WH2QQRuDGDYhg3J1giljoETCK15t1QmLK7%2BYLiAuXF5J3peGfBMNe6%2F9IGOqUB7NYSNMbDfyhJTPCEZ78wYfrMr23O2GsMEaOpat%2FDPqoz0Jue%2BQVIuPGJGcjlS8m7iL4KrUgloSJtywPg9vBmMmEgxibrSgpZWB1p8iDsEtXnaLjaYgeQbG3BybtOaZcLx8l%2FcCYf1p1zqEmhbMe7pMNAaYuj7utU0qUVpVqHc8nawZ%2BKfTCdKw0RG0E0xbpQT%2FZWuQfquZw84BgOP4wuHP4RnNXy&X-Amz-Signature=1943284652119828360c46c22c8f8261f017f086e01b333a9c8f3f5565ac24cc&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

**接下来我们要做的事情就是解析我们刚才所定义的这一堆的配置项的这么一个注解。那既然要解析注解，那同学们想一想，还是要回到这个 job pass 里面，那我们要定义一个类，这个类专门就来对我们刚才的这个 elastic job config 做解析的。那我们先写一个包，我们叫做Parser，那这个 Parser 我们给它起个名字，我们叫做 elastic job config c of elastic job like g。我大写一下，好，现在我又有了这么一个类，叫做 elastic job config passer，他就来专注去解析，我们刚才所看，就上节课所定义的这个差不多能有好多，能有四五十个这么一个注解属性，其实就要解析这个注解了。**


**那怎么去做这个东西？是不是要把它拗出来？肯定是要弄出来的，所以说你要干什么？你要在我们的 auto configuration 里边，你要做的事情就是把它也当成一个，并注入到 spring 去管理**，然后我们叫public，这个它的猪肉的名字就是小写的。然后它需不需要哪些属性？首先有些属性是传到这里的，那我可能需要用到，所以说我把它也带过来。当然注册中心就是 registry center 也需要用在上面所声明的这个 registry center，它也直接带过来好搞定。然后我把它 new 出来就行了。比如说给我提供一个构造方法，我去 new 它， new 一个它，然后传过来两个参数，一个是普尔克斯，还有一个是我们的这个 zookeeper registry center，这就是搞定了吗？然后把它 create 出来一个 cast track 构造方法，然后顺理成章的去把这个成员变量定义出来，以及这个成员变量 private 都定义出来。好，然后这里边很简单，就 this 点我。


The 2 people to practice, do you practice this down the.

to paper just center 那个 to paper just center 好了，搞定完这件事情之后，我们再回过来捋一下这个逻辑。我们最开始一定要加这个注解，就是 enable 我们的 es job 之后它会把我这个类引进来，引进来之后会去判断 condition o 不OK， condition OK 的话才会往下走。把所有 application 点practice，就是你配置文件里配置的东西，以这个为前缀的所有的配置都会放到这个 Java 对象里。然后接下来我去初始化ZK，然后调他的 init master 的方法。


做完这件事情之后我再去初始化我们什么呢？ elastic job， config Parser 他的事情就是专注于解析我们什么呀？定义的那个注解了。好，那我们回过头来想一想我们的注解，一共有几种类型？一共有 3 种类型，老师说了，我们是不是可以定义一个类，比如说叫做伊尼尔摩尔斯，就枚举类，然后它就一个枚举，比如说叫做 elastic job type anymore elastic job？什么意思？我现在要对我们 ES job 里面有三种类型做一个枚举的定义，我们这个应该没问题，好搞定三种类型，首先简单任务simple，然后叫 super job，给它一个定义叫做简单类型的job，然后打逗号还有哪些？还有 date flow 流，还有一个叫做script，那这里边叫做斯科瑞克特job，这里边叫做 data flow job data flow，那这个是什么呀？这是刘氏这个脚本类型好，非常简单。

然后接下来经济两个变量，一个就是它的 type 了， t i p e，还有一个就是后面我刚才说的，其实这就是一个描述，我们叫做 d s c 可以，然后来私有化它的构造器，然后把两个参数传进来。


小迪斯点 type 等于传进来的type，然后 this 点 DSC 等于DSC。好，然后最后给它生成概晒方法可以。好，我这个枚举类已经搞定了，基本上准备工作都做完了，然后我们就重点关注我们现在解析这个事情要怎么去做。那其实我想怎么去做呢？我想说后面真正去使用的时候，我说你就不要配这些东西了，你只需要做什么？你只需要做这几件事情，看 elastic OK，我们没把它引进来，这尴尬了，那我们来引一下，就是说他是吧？他的group，它的 artifact ID 叫这个名字，然后 group 是这个名字，然后它是零点，零点一，然后其实我直接把它拿进来就好了，这是我们之前的 ES job 的那个测试类，然后现在你就引这个包就好了， dependency 直接。只是它发生变化，它变成 task OK，这个包引进来之后我要做什么事情？之前我们要实现自己的这个 ES job 的它的这个接口， simple job，除此之外我们还要对它的这个一堆的配置进行配置项的配置。


那我们自己封装完这个基础组件之后，我期望就是直接这样去做 elastic job config，然后我们去把必须要配的有哪些，就他没有写 default 的对不对？就它配一下这个crown，它也有default，但是它默认是空就可以了。比如说它有一个name，比如name，就是比如说 COM 点什么什么，就这个名字首先命名是吧？假卖job，然后这里边就好配，接下来就是 Pron 的逗号，Pron，比如说每隔 5 分钟跑一次，那其实你就在这里面每隔 5 分钟或者每 5 秒钟跑一次。


然后再接下来还有哪些属性？就是好多好多好多属性，看见了就是说我们把什么把原来在配置里配完了之后，又要读到 Java 里边写config，**写 ES job 代码的所有的事情都变成这种注解的方式，或者说这种注解的方式是不是你再把它引进来用刀的画括号的方式？那也可以，你说你不写死代码就是相当于什么呢？这个配置，还有除此之外里边的这个就是之前我们写的这一大坨逻辑都没有了，（es-job中的下面这张图中逻辑都用注解来来代替）**

[image](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/cbd31384-cb6c-4cb4-95d2-b9ecfe2e4a37/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667G5P3YFI%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T225310Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDAKnh8klk4W6vLhi%2BbIYvdbl2ZvL5Qe%2B%2BTCdhUedH%2FEAIgAr%2BmSG2hloXoWU9FNLvl30L0D%2BdfXFm5NCsKkUhdH%2FQqiAQIxv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDKMtW995sG7Eu9jU4CrcA9y1lcOvUg2HXOdo3kJygwAgeN7IzfUIp3bdZLjdUnqaT94MiRabhLE%2FMyG6xvSSTEeWzXW%2FOHchNMYia9ytrL6cVSG5IDp03CG%2BXcXeZ9sjoqK%2FQEMoOEsFAjVSvR5P2eVlao5xhSw5P59USj7I0xtITqbk%2FAFyyKOlKP%2BAwDW5tkI1Ym88Tbo5cxCMlSUmxBrnFIZJxYddoTsqljFWvdBJomyjgfw9%2B4AMzj%2B8UeOg5sG7eZgGrv8JKhkDSymauX%2BObSvKXf4D9ZxiZb6YZFd9G7UPCXby1idI4ArRemXUd0bkzNC%2B359g45%2FXeDrkixOZZ2y%2Fw5JcgPyzFWlFcyeMsgMbqbAYWp8eAIEfXaRpfubciQDRQBf6zeEhzPYlx62qoNeyS5LpwV5tkRWIXqRuA%2BExHZqVoDlQh5A7lDo49qnUYprBF0IvToPesnjWrLQ3dxlXVddFzQt6Zv2xEi2rrDEvzTI0TIOwxA7TN0YdxZ1X2RZQG66O1aT5zecRGF9z2fgIpgKusZxGg2Y%2B3Ea0R9LfNjL2RzBU8V26iiVXvkoK0MM4UHJNMrgj6%2FgzDiXmcQ4MJ3WH2QQRuDGDYhg3J1giljoETCK15t1QmLK7%2BYLiAuXF5J3peGfBMNe6%2F9IGOqUB7NYSNMbDfyhJTPCEZ78wYfrMr23O2GsMEaOpat%2FDPqoz0Jue%2BQVIuPGJGcjlS8m7iL4KrUgloSJtywPg9vBmMmEgxibrSgpZWB1p8iDsEtXnaLjaYgeQbG3BybtOaZcLx8l%2FcCYf1p1zqEmhbMe7pMNAaYuj7utU0qUVpVqHc8nawZ%2BKfTCdKw0RG0E0xbpQT%2FZWuQfquZw84BgOP4wuHP4RnNXy&X-Amz-Signature=5a3eb4826c79482e978d83d09523133df10212438ae8fe723177a36a5577c37f&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

**就是要做这件事情。好了，我不知道小伙伴们这回你没理解我们要做什么事情，暂时我们把它都关掉，大家知道我们现在要做什么事情了。**然后我们再接下来开始起来了。首先同学们想一下这个类它是跟 sprint 是一个什么关系？那我个人觉得它跟 screen 是有一个比较密切的关系，因为它是强依赖 screen 的，它脱离不开screen，它如果脱离开spring，它就是 ES job 原生的代码就跟 spring 没关系了，所以说我们需要在一个时机做什么事情，同学们想一想我们后面的事情。比如说我们自己的这个星图job，它实现了我们自己刚才所说的那个 elastic job config 以外，我们再把它注入到 sprint at component 就可以了。那这样的话它就会读取我们自己定义的这个注解，而里边我们配置的所有的属性都去做解析。然后帮我们把什么 spring 的这个 job skater，包括 late job config 等等一些我们之前在 my simple job config 里边要做的事情，都放到我们的 pass 中去做好了。


那要这样的话，首先这个类必须要实现这个接口，然后必须也要注入到spray，**那有这个前提，同学们想一想，接下来你是不是就应该明白我要怎么去做了？接下来我们来看一下。首先既然我们要从 spring 中去读取带有我们自己注解的那个类，那我们在什么时机比较合适呢？其实在很多时机，比如说application。**

And contest aware the infection post process.


还有什么呀？还有init，Lisa，bin，还有包括我们这个application， listener 等等等等等等。 spring 给我们好多好多这种扩展的这种接口，这种时机，那我们来选择一个最稳妥的时机。什么意思？就是说其实我们是想让我们的这个解析的过程，什么时间点去执行最万无一失。很明显就是当我们所有 spring 的 bin 都实例化完成以后，我们再去说把我们自己的 job 解析好，这是最 OK 的。针对于不同的需求，你自己会有不同的这个选择，比如说你现在这个job，它首先比如说我艾特 component 或者是 service 都可以。然后比如说我这里边我写伪代码，我 private 一个什么 my do， my do，然后我这样去做凹凸，哦， VR 的我去注入了一个我的DAO，然后去操作数据库，或者是注入一个service。那有的时候你如果选择时机不对，可能会出现这个东西还是空着的。那有同学说老师那很简单，你就实现一个 instance in，或者是怎么样，或者是老师那样 spring 他没问题，既然有 out where 的话，他会帮你去自动去调这个顺序，那其实不是这么简单的，有些极端情况下可能会出现。



**说什么呢，就看你自己代码怎么去写了，可能出现你这个类有了，然后其他的你想去调的那个东西，可能它不是直接的OPS，要直接的奥特曼，他肯定帮你去做顺序了。你可能在这个定时任务里边，你去调其他的service，那个 service 里边又调其他的，他们可能没有一个那种依赖关系，这个时候最稳妥的方式是什么呢？就是在我们整个应用服务都启动完了以后，就是起码是我们所有的 spring 并加载完成之后，我们去做这个 ES job 解析这个事情。**


**本身定时任务这个事情，你的应用服务都没起来，你就开始执行定时任务了，那可能比如说你有好多东西可能还没初始化完成呢？所以说一定是最好等到我整个 spring 都初始化完成了，我的应用真正起来了之后，我的定时任务才开始跑嘛？也不可能我应用起一半内容开始跑不太合适，所以说我们选择一个时机，就是刚才我们只能选择什么呢？ application radius 就在这个时机去做是最合适的。就在我们整个应用服务器都已经搞定了，都已经启动了之后，我们再去对我们自己声明的 ES job config 注解去做解析才是最合适。那我们来写一写吧，看看这个代码应该怎么去写。**


首先呢，我们的应用都已经初始化了，它只是初始化完成了吗？已经准备好了这个叫做 application ready event 初始化完成了的事件给我了，那完成了我随便我去拿任何东西都能拿到了，比如说我 get application context 就可以取到，我就取到 application context。


取到这个 application context 之后我们干什么事情？那我们刚才说了我们自己要实现的这个注解，我们是放到什么呢？我们自己，我把这个关掉，现在我可能不用它。sorry，我们自己要实现这个注解，就是我们的这个 elastic job config 这个注解它肯定是要放到一个类上的，然后这个 z 它是已经交由 spring 去管理的，也就是说它已经是 spring 的一个 bin 了，说白了就是这个注解一定是在 spring 的一个 bin 中，那就简单了。


通过这样的分析，直接 get 病死位子annotation，就是我自己刚才写class，就是说我的病上如果有这个注解，那我全渠道它返回是一个map，那我们把这个 Mac string object，我们把这个取到。我们叫什么呀？我们叫做 be Mac 取到之后干什么呀？就是说我现在在整个 spring 的环境中，我把带有我自己声明的这个 elastic job config 注解的 b 全拿到，然后我针对于是不是我要负循环对我所有的这些注解的病，我要读里面的配置，然后初始化相关的内容。OK，那就简单了，定义一个类，我们定一个。

Mapped values each other.


返回的是一个以特特对象，那这个以特特对象我是不是可以接受一下缺口？然后这个以缺特我可能不知道它具体是什么类型，所以说我们叫做IT，OK，然后我们要去做循环，那就 it 点 has next，OK，如果有下一个，然后我们去做事情。好，那就是说我们要把所有的我的这个里面小封号，我要把所有的我的带这个注解的病都拿出来，拿出来之后我无非就是找到病，然后去看看它的class，通过它的 class 之后，然后再拿一些东西，其实很简单，那我们来看一看怎么去做。那就是 IT 点 next 嘛， next 就取到下一个，然后因为我这打了问号了，现在我们只能说它是一个 config bin，带有我自己配置的这么一个bin。


好，有这个 bin 之后，我们看一看这个 bin 的 class 是什么？是不是能取到第二 get class，然后这 class 我不知道是什么，我用 class 声明一下，我得到了它的 class 之后我要干什么呢？同学们想一想，比如说我们父类有子类或者是有匿名类的情况下，是不是这 class 它里边会带那个什么 dollar 符号？在这里边我们其实也做得严谨一些，比如说它带有 dollar 符号的时候，我们要做一个判断，我说点 get name，如果说你是一个特殊的，我说点 index off，如果带有 dollar 符号的话，然后它大于0，然后我再做一些处理。我说string，我们再定一个叫做 class name，等于克拉斯点 get name，然后对克拉斯等于克拉斯点 for name，然后这个 name 就是克拉斯name。


第二 substraight 从 0 到他的刀乐符号之前，加 index off，到了，同学们想一想我这是在做什么事情？当然这里边会有一个异常，这个异常我们整体的去做一个 try catch。好，这个开始我们一会再去写啊，现在先打Todo。好，那刚才这个是说什么事情？如果说你这个是一个子类带有这个匿名的，或者是这个带 dollar 的，那我帮你把这个真正的名字取重来码，然后复制给这个克拉斯码。就是说因为我要从 0 开始截到这个刀了，之前那个才是正常的类嘛。然后用 class 点 full name 把那个正常的类取出来，是他吗？OK，那这样这个 class 才能确保我取到的是对的，我取到的 class 是对的之后，然后我用 class 去就是获取接口类型，然后用于判断是什么类型的任务吗？到底是简单任务还是流式任务？那就是 class 点 get interface 0 嘛。


我说取到第一个嘛， get simple name 就可以了。那你取到的肯定是 simple name 或者是 data flow name，就直接取到它的简单名称了。好，那我就简单写。但真正工作中千万别这么玩，我可能继承多个。是不是你要循环这个 interface 接口，要把所有的时间内挨着盘的去循环去判断，判断完了之后，然后再看符不符合，好了，搞定这个事情之后，我们取到它是什么类型的任务了。

```java
package com.bfxy.rabbit.task.parser;

import com.bfxy.rabbit.task.annotation.ElasticJobConfig;
import com.bfxy.rabbit.task.autoconfiguration.JobZookeeperProperties;
import com.dangdang.ddframe.job.reg.zookeeper.ZookeeperConfiguration;
import com.dangdang.ddframe.job.reg.zookeeper.ZookeeperRegistryCenter;
import org.springframework.boot.context.event.ApplicationReadyEvent;
import org.springframework.context.ApplicationContext;
import org.springframework.context.ApplicationListener;

import java.util.Iterator;
import java.util.Map;

/**
 * <h1>解析注解</h1>
 */
public class ElasticJobConfParser implements ApplicationListener<ApplicationReadyEvent> {

    private JobZookeeperProperties jobZookeeperProperties;

    private ZookeeperConfiguration zookeeperConfiguration;


    public ElasticJobConfParser(JobZookeeperProperties jobZookeeperProperties, ZookeeperRegistryCenter zookeeperRegistryCenter) {
    }

    /**
     * Handle an application event.
     *
     * @param event the event to respond to
     */
    @Override
    public void onApplicationEvent(ApplicationReadyEvent event) {
        try {
            ApplicationContext applicationContext = event.getApplicationContext();

            Map<String, Object> beanMap = applicationContext.getBeansWithAnnotation(ElasticJobConfig.class);

            for (Iterator<?> it = beanMap.values().iterator(); it.hasNext(); ) {
                Object confBean = it.next();
                Class<?> clazz = confBean.getClass();

                if (clazz.getName().indexOf("$") > 0) {
                    String clazzNmae = clazz.getName();
                    clazz = Class.forName(clazzNmae.substring(0, clazzNmae.indexOf("$")));
                }

                /** 获取接口的类型， 判断是什么类型的任务 */
                String jobTypeName  = clazz.getInterfaces()[0].getSimpleName();
                /** 获取配置项 ElasticJobConfiguration */
                ElasticJobConfig conf = clazz.getAnnotation(ElasticJobConfig.class);
                String jobClass = clazz.getName();
                String jobName  = this.jobZookeeperProperties.getNamespace() + "."  + conf.name();

                String cron = conf.cron();
                String shardingItemParameters = conf.shardingItemParameters();
                String description = conf.description();
                String jobParameter = conf.jobParameter();
                String jobExceptionHandler = conf.jobExceptionHandler();
                String executorServiceHandler = conf.executorServiceHandler();

                String jobShardingStrategyClass = conf.jobShardingStrategyClass();
                String eventTraceRdbDataSource = conf.eventTraceRdbDataSource();
                String scriptCommandLine = conf.scriptCommandLine();

                boolean failover = conf.failover();
                boolean misfire = conf.misfire();
                boolean overwrite = conf.overwrite();
                boolean disabled = conf.disabled();
                boolean monitorExecution = conf.monitorExecution();
                boolean streamingProcess = conf.streamingProcess();

                int shardingTotalCount = conf.shardingTotalCount();
                int monitorPort = conf.monitorPort();
                int maxTimeDiffSeconds = conf.maxTimeDiffSeconds();
                int reconcileIntervalMinutes = conf.reconcileIntervalMinutes();



            }
        } catch (Exception e) {
                 // TODO
            e.printStackTrace();
        }
    }
}
```

那接下来这核心就来了，获取，这指向什么？配置项，就是我们刚才这个注解的配置项，就是我们的 elastic job config 的配置项。这里边茫茫多，怎么去获取啊？这个类你都有了，我直接去取这个 l t c，然后他帮我去返回这个annotation，我通过这个 annotation 我就知道所有的配置了。有了这个

annotation，那这个 annotation 所有的配置我都能有了。比如说 job class 是什么？等于 class get name，这就取到他当前的这个job，它所对应的这 class 什么？然后 job name 我们怎么去起？ job name 就是我们通过这个配置去取的点name，那如果说你这个 job 内幕想取的名字怕有冲突，那怎么办？那你可以加一个嘛？我们之前是不是把它传进来了？这个 practice 这个里边有一个约束的一个比较关键的东西，就是命名空间，比如说我们可以中间加一个点去区分一下，可以吗？OK，就是说你具体的租 keeper 的那个最根上的那个命名空间，就是它的 name space，然后点你的名字，这个是表示你的 job name，然后接下来你再去取，比如说比较核心的你的 crowd 表达式是什么？那就是 c o f，点 config 等等等等等等。那这里这段代码老师就不再一点点敲了，我现在就把这个整体的代码完全都 copy 过来，那无非就是你一个配置项去获取，没有什么含金量。好，我在这里直接把它 copy 过来。


刚才我们是取到crowd，然后我们再往下看，比如说它的这个 sharing item parameters，还有它的 description 描述，还有 job parameter 以及 job execution handler，还有 execution service handler，包括它的 job 分片的策略还有等等 fail over，还有 miss fail over ride，还有一些分片总数，还有跟 monitor 相关的。就是说这些配置其实都是我们刚才所看到的 ES job config 注解里边的这个配置项，就你配不配，反正我都取到，我按照这些为基础取到了之后，然后再帮你去一点点的去创建什么呢？去创建一个 ES 照。好，那接下来我们看怎么去做。

