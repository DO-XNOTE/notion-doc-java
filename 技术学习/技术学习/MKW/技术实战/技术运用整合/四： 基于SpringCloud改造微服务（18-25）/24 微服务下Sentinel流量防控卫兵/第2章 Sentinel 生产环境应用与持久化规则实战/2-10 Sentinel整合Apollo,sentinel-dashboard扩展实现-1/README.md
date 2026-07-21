---
title: 2-10 Sentinel整合Apollo,sentinel-dashboard扩展实现-1
---

# 2-10 Sentinel整合Apollo,sentinel-dashboard扩展实现-1

[image](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/917ec7a5-207b-438f-8cc5-70483ca2ddb3/SCR-20240723-czvz.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466V3MF354D%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T225847Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIFrIB7p9s%2ByDNnvzCGDtObq%2F3IzhMkUsEBvZGvK95OyVAiBxCvjLLrE4qSbMZxWcCLfNvK9eWEoZRX4EHu%2B3yIjcIyqIBAjG%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMuMxolKDE%2BzNx%2F%2FL0KtwDDjSt325R4OxZ%2BSKYhnNt6esXk5%2BXZWzOmZ9QW3Z2YYBHbxdecQ0FO003sB%2FteqaS%2B0FniqwsJtw5yr3YUUOOIoti7MyVk1thogTXVjT5nfrZQAYP0yZOrmeRiYD0uhWSxiQFtpJEaT4bXSODbHT6GMpw4ehm2AyCEpuNzWZ23fY4DNPvvV%2B8S8Vpzf0V6B3q%2BsKG11fRPbeFGMrmW18zsGsTIFGlzI0wlEw1NgbPn6dy%2BSXTOpEOA1sMGLJ%2BH0MxHQCvX914Sy4RKelzRyx2Icq1GU7aNB8i2ecDHVaVsgTeff0iggm5HsD3Mdf7PcCUshbqoC%2FLX4vROWtHf%2FMjG0nMsJ6jipDlpFwM1ZsMj2zuKHydCsaA3yCA3MWSud73nqAdO7bU9eJkUy%2F8EoO9KVOyNohZzVWwYU9EtgUW7yj%2BneHP2p%2FQAfO0immMlOQE0FsExFGA%2B9A9NkGpI4BAKvEoiOmLX0CtjQ7PkiARC9vetuT6LF9mW30v2%2BnoSnhyEjx%2BkQlInE75yVEEfuXhStWEPHSw4lvIIztiMn2XhvCDwFRnp3ZD19wpOoJ2L6%2B56J9WXH1kDFxU2MQhHN8ncmDbxfNa8JkJXMOmUXS%2BmRQ%2FEMSDLg76oY8YjeUwu7v%2F0gY6pgH772NEFAn5EwxUyse8nUQt%2BKGvGCF7rFbbibiFCRbHdzyO1mSV%2F0F1f2y7yB6hCPoSdL6K5pTd4n9yi9NaFrDF2lf5Sj2s3%2FfEd82BcxjaPmtBRvPjWR5o0CbcjVfNW%2B7f%2FwbooAGBo3saq6SJWtQywW59bl43VnCjui9yr0DinIu6KbJ%2BtAURB%2FgqZC0LQjvdOI36QaDH78f%2FsO7cRp%2FgHbUBAxk0&X-Amz-Signature=e0e8e6a440da774ec87f13d40e35a48d8f0572497b5e4a0dfdcf28f2bb4d9b74&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

[image](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/8b00d45d-865d-40a9-93f8-c24ffeac6afb/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466V3MF354D%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T225847Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIFrIB7p9s%2ByDNnvzCGDtObq%2F3IzhMkUsEBvZGvK95OyVAiBxCvjLLrE4qSbMZxWcCLfNvK9eWEoZRX4EHu%2B3yIjcIyqIBAjG%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMuMxolKDE%2BzNx%2F%2FL0KtwDDjSt325R4OxZ%2BSKYhnNt6esXk5%2BXZWzOmZ9QW3Z2YYBHbxdecQ0FO003sB%2FteqaS%2B0FniqwsJtw5yr3YUUOOIoti7MyVk1thogTXVjT5nfrZQAYP0yZOrmeRiYD0uhWSxiQFtpJEaT4bXSODbHT6GMpw4ehm2AyCEpuNzWZ23fY4DNPvvV%2B8S8Vpzf0V6B3q%2BsKG11fRPbeFGMrmW18zsGsTIFGlzI0wlEw1NgbPn6dy%2BSXTOpEOA1sMGLJ%2BH0MxHQCvX914Sy4RKelzRyx2Icq1GU7aNB8i2ecDHVaVsgTeff0iggm5HsD3Mdf7PcCUshbqoC%2FLX4vROWtHf%2FMjG0nMsJ6jipDlpFwM1ZsMj2zuKHydCsaA3yCA3MWSud73nqAdO7bU9eJkUy%2F8EoO9KVOyNohZzVWwYU9EtgUW7yj%2BneHP2p%2FQAfO0immMlOQE0FsExFGA%2B9A9NkGpI4BAKvEoiOmLX0CtjQ7PkiARC9vetuT6LF9mW30v2%2BnoSnhyEjx%2BkQlInE75yVEEfuXhStWEPHSw4lvIIztiMn2XhvCDwFRnp3ZD19wpOoJ2L6%2B56J9WXH1kDFxU2MQhHN8ncmDbxfNa8JkJXMOmUXS%2BmRQ%2FEMSDLg76oY8YjeUwu7v%2F0gY6pgH772NEFAn5EwxUyse8nUQt%2BKGvGCF7rFbbibiFCRbHdzyO1mSV%2F0F1f2y7yB6hCPoSdL6K5pTd4n9yi9NaFrDF2lf5Sj2s3%2FfEd82BcxjaPmtBRvPjWR5o0CbcjVfNW%2B7f%2FwbooAGBo3saq6SJWtQywW59bl43VnCjui9yr0DinIu6KbJ%2BtAURB%2FgqZC0LQjvdOI36QaDH78f%2FsO7cRp%2FgHbUBAxk0&X-Amz-Signature=e2a9db9c519977a9d3adf31bdf75252db011b2666693156becd6704e8e3ca57c&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

[image](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/5691c643-4584-42ae-b432-d813575b9b47/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466V3MF354D%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T225847Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIFrIB7p9s%2ByDNnvzCGDtObq%2F3IzhMkUsEBvZGvK95OyVAiBxCvjLLrE4qSbMZxWcCLfNvK9eWEoZRX4EHu%2B3yIjcIyqIBAjG%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMuMxolKDE%2BzNx%2F%2FL0KtwDDjSt325R4OxZ%2BSKYhnNt6esXk5%2BXZWzOmZ9QW3Z2YYBHbxdecQ0FO003sB%2FteqaS%2B0FniqwsJtw5yr3YUUOOIoti7MyVk1thogTXVjT5nfrZQAYP0yZOrmeRiYD0uhWSxiQFtpJEaT4bXSODbHT6GMpw4ehm2AyCEpuNzWZ23fY4DNPvvV%2B8S8Vpzf0V6B3q%2BsKG11fRPbeFGMrmW18zsGsTIFGlzI0wlEw1NgbPn6dy%2BSXTOpEOA1sMGLJ%2BH0MxHQCvX914Sy4RKelzRyx2Icq1GU7aNB8i2ecDHVaVsgTeff0iggm5HsD3Mdf7PcCUshbqoC%2FLX4vROWtHf%2FMjG0nMsJ6jipDlpFwM1ZsMj2zuKHydCsaA3yCA3MWSud73nqAdO7bU9eJkUy%2F8EoO9KVOyNohZzVWwYU9EtgUW7yj%2BneHP2p%2FQAfO0immMlOQE0FsExFGA%2B9A9NkGpI4BAKvEoiOmLX0CtjQ7PkiARC9vetuT6LF9mW30v2%2BnoSnhyEjx%2BkQlInE75yVEEfuXhStWEPHSw4lvIIztiMn2XhvCDwFRnp3ZD19wpOoJ2L6%2B56J9WXH1kDFxU2MQhHN8ncmDbxfNa8JkJXMOmUXS%2BmRQ%2FEMSDLg76oY8YjeUwu7v%2F0gY6pgH772NEFAn5EwxUyse8nUQt%2BKGvGCF7rFbbibiFCRbHdzyO1mSV%2F0F1f2y7yB6hCPoSdL6K5pTd4n9yi9NaFrDF2lf5Sj2s3%2FfEd82BcxjaPmtBRvPjWR5o0CbcjVfNW%2B7f%2FwbooAGBo3saq6SJWtQywW59bl43VnCjui9yr0DinIu6KbJ%2BtAURB%2FgqZC0LQjvdOI36QaDH78f%2FsO7cRp%2FgHbUBAxk0&X-Amz-Signature=4ebc0934202720bc330961fec297647fb45d5b8d9a508e0475887ca77a8b9f2e&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

我们已经把对应的这个配置文件里的配置都解析了，然后也对应的是通过这个阿波罗的 config util 生成了就是我们的阿波罗的这个 Open API client 然后我们一通过这个 App name 然后去获取到 token 然后通过 token 以及它的这个 portal 的 UI L 去取到了我们对应的这个 client 那接下来我们有了这个 client 之后我们怎么办呢？其实我们通过 client 我们就直接可以去调 client API 去操作阿波罗了。


那在这之前我们来看一看这个官方他是怎么去做的就是官方他自己提供了两个扩展接口，一个是叫做 dynamic ruler provider 这个 provider 他做的事情就是获取，它里面提供一个叫做 get rulers 就是说你给我一个 App name 我可以把这个 App name 里边所对应的这个规则都取到返回给你。


还有一个是 dynamic ruler publisher 它是干什么呢？就是用人发布的，我们之前有发布，但是直接之前发布的是什么呢？那种原始的模式是我们 dashboard 直接发布给我们具体的 client 然后去更新内存。但是现在我们不是这样的，现在我们要直接更新阿波罗。所以说对应的这两个接口我们要做一个扩展来我们先扩展 provider 在这里我们给它起一个名字，我们叫做 follow ruler 阿波罗 provider 阿波罗 provider 可以吧。然后这个你肯定是一个 component 对不对？因为它是我们之前用 component scan 扫描了，然后我们去给它定义一个名字叫做小写的 follow ruler 阿波罗 provider 可以吧。


然后紧接着这个类肯定要实现接口，要实现我们刚才所看到的那个 implements dynamic provider 接口里边传什么内容？比如说我现在要做的就是流控规则对不对？我们来写一写流控规则，这个接口里边它肯定传的是一个 list 对不对？然后 list 具体的内容就是我们的 follow ruler entity 好了，搞定。然后我们要重写一个方法，就是 get rulers 好，那这个方法我们应该怎么去做？同学们想一想，这个方法很简单，现在有一个问题是传过来的是一个对象，然后可能还会跟 Jason 有一个转换。那我们其实我们在之前已经有了一个 converter 在 config 的时候还记得吗？我们传了这个 converter 就是这个 bin 一个是 decoder 一个是 coder 那这个 converter 我们直接把这个对象拿过来，也可以或者直接用也可以 auto aired 直接注入进来。就是 private 我们写 can were 这个 convert 一定是 center 的 convert 它的 key 是stringvalue ，就是我们自己的这个 follow ruler entity 然后给它起个名字，就叫 conwater 可以。


好了，搞定好了，然后接下来我看看我怎么去获取资源，这个事情就很简单了。获取资源，那就是它只有给我一个具体的参数，就是 App name 通过 App name 怎么去从阿波罗里边去获取它所对应的这个 App name 所对应的一些资源。首先你第一点你要获取这个阿波罗的 client 阿波罗 config util 第二 create 先从 map 里去取，然后取出来这个 apu name 它如果有对应的 client 就返回，没有，我就帮你先创建一个，然后再返回。就是这个东西我们上节课做的，然后返回一个 client 然后我们把这个包引进来，有了它之后，然后接下来我们判断，如果当前的 client 不等于空的话，那我们直接就可以调阿波罗 API 去取。如果等于空 else 的话，那我们直接可以 return 一个空的集合。 else 的情况下，我们可以直接 return 一个 collections.empty list 就 Java 油条的，点 empty empty list 返回约空集合。然后不等于空的情况下，我们应该对应的去用 clang 去调，把我们想要的结果都拿出来，怎么去拿？首先这里边不等于空。


那第一件事情我们要知道这个它真正存的这个 ID 是什么，就是那个规则 ID 通过它去 get follow 这个 ID 把 App name 传进去，他会帮我们做什么事情？拿到对应的 follow date ID string follow date ID 这个 follow date ID 是怎么拼的呢？同学们还记得吗？我们之前上节课领着封装的，他就是把这个当成 ID 了，是不是因为你这是项目名称了，然后再加上具体的一个前缀，就是后面的这块杠 follow 杠入了。


斯好，回过头来，我们拿到这个 App ID 之后，我们还要去获取一些其他的信息，比如说当前它的 App ID 是什么？你现在只是获取具体规则的 date idapp 是什么？这个从哪提取？小伙伴们还记得吧，这个我们可以去给他，比如说提供一个方法继续用这个类。


第二比如说我想 get 一下 App ID 然后通过什么 get 呢？通过 App name 是不是？然后 with App name 然后我就说我想把 App name 传进去，你就把 App ID 给我，这个其实是可以的，我们直接去 create 一个 method 那这个怎么去做呢？这里边不是有这个 App config ，直接 App config App ID map 然后点 get 就可以了。


这是怎么制作的？同学们还记得吗？这个 map 它的键值对，是 application name 和 App ID 我现在想取到这个 App ID 那我必须得把 application name 传进去，然后给我返回这个 App ID 对不对？它们是一个 KV 的键值。对。所以说我现在的做法就是通过 config 取到这个 map 然后把 App name 传进去，给我返回 App ID 就这么一个非常简单的逻辑。


好了，再回过头来，然后它还需要什么？它还需要去 get namespace 然后通过 namespace 取到我们的具体存储的信息。那在这里我们直接可以通过 client 端有 API 找一个，这里边这些参数都需要用到的。比如说我们现在第一个 apid 是什么呢？我们有了对不对？ ENV 环境是什么？我们是不是直接可以通过阿波罗 config 直接取到阿波罗 config E nv 取到环境 class 的 name 我们也可以取到这个里面，也是通过它第二 get class name 然后 namespace 也是可以取到的。看见了吧，我们直接可以通过它取到我们的 namespace 所以说这个通过它去 get name service 它返回一个叫做 open name service DTO 这么一个模型，我们通过这个模型里边其实我们就可以找到我们想要的东西了，它返回的是 open name swiss DTO 我们叫做DTO 。找到这个 DTO 我们怎么去操作，能取到我们自己想要的规则？这个 DTO 它里边有 get items 的属性，取到所有的 items 然后点 stream 在这里，老师就直接写了。


点 filter 去过滤。 filter 怎么去过滤呢？我想去过滤跟我匹配的内容，我怎么去过滤？这是咱们 Java 的那个stream ， Java 8 的那个 stream.get key 。然后我说这个key ，如果 equals 我们自己对应的这个规则，我们就取到这一条规则了，这就是一个过滤条件。然后最后我们可以去点 map 一下，我们用这个表达式，我们取到的其实就是 open item DTO 这是具体实际的规则。然后两个冒号 get value 然后取到 map 之后点 send first 我们取到第一个，然后点用这个什么也不要。 OK 那么这个就是一个一套这个链式编程了，很简单，缩进一下。 OK 通过它我们取到的内容就是我们所对应的 ruler 规则，这就是我们想要的规则。然后这个规则它是一个 string 类型的字符串，我想把它转换成我们自己的一个对象，那就用这个 converter 这 converter 就用到了，直接 return 它点 converter 就是我们的 rules 然后直接返回。
这样的话我们的 get 方法就已经搞定了，这也是他阿波罗 Open API 的写法，不清楚的，你可以看一看那个 OpenAPI 大家可以看看文档，我们搞定了这个之后，那接下来另外一个不就简单了。





