---
title: 1-15 哨兵控制台集成详解-2
---

# 1-15 哨兵控制台集成详解-2

[image](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/36972095-75fc-46db-a235-e4d52f61fd38/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667Y545HHM%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T225836Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIFPSshXlvM1JOzjFfHlKEi98yds0w%2F31tMAGqKF9OwApAiAMPG8hGA1rtL2strvIWahoptEoX7NYydYpUZD4%2FEF9qCqIBAjG%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMShKKghTQKJfsF2d%2BKtwDXu3tG6NoPBWz1JYAHY4Nh6E5ZVaHWez7HfD5SjdHVotrdspzJ7Lkra8bR%2BOC5qFoSlhkk3Jd5zthpb6niKgARYUuV9TVbzzmSkpaqwyPy3mO6vQSlo7zez98ceRmrHWg4QxC2nNfjAbec4oL0EglgJFcmHM3RWa0TtL1Mrd4FIsjsYY7%2FowMiubhFisyYxb%2FhcmSdkA1lKQ17QUmVc0g7mbRFBEosow1aKcXEqPY%2BNPfdqA2ZIFR21argO8eNoRp%2B%2BPLPo5p5COJ8Dk%2FsXxP3ZFbm%2FN37%2FP3eDljXvR6LF1u2Q%2BYFHuGTtjcw0iR1%2Fq4s8%2BbCX%2B2OwhqsN34uBVGZeta272HR6b4gvaEt%2FWB15ofvtiBN3P%2FrJll08u7yfJE4LEZC26SEjnhEwB0Ry06HiTp%2FuCiHUtfDDgPaPOOyxsdEVvqonpWsddUyWPppim9n6%2FUOSK27IDNcjOD%2FApxZkuRkg%2BIlowMOE21lk%2FgN8IzhFjec9Q0buXQXSwilRQwG473l5%2FTimXY2JyruRAPRyzKPRywJtGzBT4o5%2BRjEDVmkN4nWTPWW%2BUBnxdZ7gqqw%2BCHgC9%2FzFtaoEZpOg6VeELY4rcdV1LbsUOXVwezkt2EIcQsmelCN1Yjje4wm7r%2F0gY6pgGmJNZs9zzBfxTqM0O06OLnTXZS%2BAMJawguncIcw1ftP2SZIt9lYh3tooe66o4S1MrmYR7HPKIka4YQLHa4KhKmTt1yv2WJ8WrEshMQCexB14muMEQaLqj2P7QG5379vuxkKO%2FcWP2smWt6Do55Sy5fEbhYQFWKoiJIqUHuCjuBbTVOPWmTqQwKfGBDvKlhAzLIP8rzoO9Go5KNmXPZdkwtm2qVIHBY&X-Amz-Signature=08264a49d65a417b88aff6c4edd5a25857ba43e66d62e697f9724927566dc844&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

[image](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/b50332e9-0671-4af1-8ff0-62221a035341/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667Y545HHM%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T225836Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIFPSshXlvM1JOzjFfHlKEi98yds0w%2F31tMAGqKF9OwApAiAMPG8hGA1rtL2strvIWahoptEoX7NYydYpUZD4%2FEF9qCqIBAjG%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMShKKghTQKJfsF2d%2BKtwDXu3tG6NoPBWz1JYAHY4Nh6E5ZVaHWez7HfD5SjdHVotrdspzJ7Lkra8bR%2BOC5qFoSlhkk3Jd5zthpb6niKgARYUuV9TVbzzmSkpaqwyPy3mO6vQSlo7zez98ceRmrHWg4QxC2nNfjAbec4oL0EglgJFcmHM3RWa0TtL1Mrd4FIsjsYY7%2FowMiubhFisyYxb%2FhcmSdkA1lKQ17QUmVc0g7mbRFBEosow1aKcXEqPY%2BNPfdqA2ZIFR21argO8eNoRp%2B%2BPLPo5p5COJ8Dk%2FsXxP3ZFbm%2FN37%2FP3eDljXvR6LF1u2Q%2BYFHuGTtjcw0iR1%2Fq4s8%2BbCX%2B2OwhqsN34uBVGZeta272HR6b4gvaEt%2FWB15ofvtiBN3P%2FrJll08u7yfJE4LEZC26SEjnhEwB0Ry06HiTp%2FuCiHUtfDDgPaPOOyxsdEVvqonpWsddUyWPppim9n6%2FUOSK27IDNcjOD%2FApxZkuRkg%2BIlowMOE21lk%2FgN8IzhFjec9Q0buXQXSwilRQwG473l5%2FTimXY2JyruRAPRyzKPRywJtGzBT4o5%2BRjEDVmkN4nWTPWW%2BUBnxdZ7gqqw%2BCHgC9%2FzFtaoEZpOg6VeELY4rcdV1LbsUOXVwezkt2EIcQsmelCN1Yjje4wm7r%2F0gY6pgGmJNZs9zzBfxTqM0O06OLnTXZS%2BAMJawguncIcw1ftP2SZIt9lYh3tooe66o4S1MrmYR7HPKIka4YQLHa4KhKmTt1yv2WJ8WrEshMQCexB14muMEQaLqj2P7QG5379vuxkKO%2FcWP2smWt6Do55Sy5fEbhYQFWKoiJIqUHuCjuBbTVOPWmTqQwKfGBDvKlhAzLIP8rzoO9Go5KNmXPZdkwtm2qVIHBY&X-Amz-Signature=3f1e9f83898b1cb8b5cbbab832448d7b6266273a4fc1c02e566ca787d5957b36&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

流控包括降级也可以去做。那在这里老师跟大家简单来加一个新的降级规则，然后帮小伙伴们一起看一下。好了，我先把这个应用程序我先给它干掉，我说我再加一个降级的规则，看看行不行，我们自己手写一个。好，我现在先把这个都 close 掉，然后我们打开我们自己的 demo 我们之前有一个 index controller 我们在 index controller 基础之上我们再来做开发。好了，在这里边我们这个代码其实我都可以 copy 一下，稍微改一下就可以。当然这个流控我现在放到的是 controller 层，其实你可以放到 service 层对不对？我相信小伙伴们应该大家都比较了解 degree 的表示降级的意思。


那 degree 的我应该怎么去做呢？ degree 的这种异常我之前不是有一个 hello world 吗？现在我就不能再叫 hello world 了。对不对？我叫 hello world 他们的资源就冲突了，我再起个其他的名字，比如说这个名字叫做 degree 的杠 test 资源的名字。那有同学可能就问了老师，在***真正工作中，那这个资源名字应该怎么去定义啊？这个资源名字一般定义的方式就是你的权限命名加上方法名，假设说你是以方法为最小力度读法，那就是你的包名加上类名，然后都是用冒号。就是你的 com.bfx ***[***y.test.web***](http://y.test.web/)*** 冒号加上你的类名，就是点命名+方法名***。我们来搞一个生产环境下的这个命名规则。就是你的 resource URC name 应该怎么去定义？我来写一下 resource iesuurce name 其实就是这样，点你的类名，然后在字段号你的方法就可以了。

[image](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/d81999f6-d02d-415a-8b62-5bdf638aa6bd/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667Y545HHM%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T225836Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIFPSshXlvM1JOzjFfHlKEi98yds0w%2F31tMAGqKF9OwApAiAMPG8hGA1rtL2strvIWahoptEoX7NYydYpUZD4%2FEF9qCqIBAjG%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMShKKghTQKJfsF2d%2BKtwDXu3tG6NoPBWz1JYAHY4Nh6E5ZVaHWez7HfD5SjdHVotrdspzJ7Lkra8bR%2BOC5qFoSlhkk3Jd5zthpb6niKgARYUuV9TVbzzmSkpaqwyPy3mO6vQSlo7zez98ceRmrHWg4QxC2nNfjAbec4oL0EglgJFcmHM3RWa0TtL1Mrd4FIsjsYY7%2FowMiubhFisyYxb%2FhcmSdkA1lKQ17QUmVc0g7mbRFBEosow1aKcXEqPY%2BNPfdqA2ZIFR21argO8eNoRp%2B%2BPLPo5p5COJ8Dk%2FsXxP3ZFbm%2FN37%2FP3eDljXvR6LF1u2Q%2BYFHuGTtjcw0iR1%2Fq4s8%2BbCX%2B2OwhqsN34uBVGZeta272HR6b4gvaEt%2FWB15ofvtiBN3P%2FrJll08u7yfJE4LEZC26SEjnhEwB0Ry06HiTp%2FuCiHUtfDDgPaPOOyxsdEVvqonpWsddUyWPppim9n6%2FUOSK27IDNcjOD%2FApxZkuRkg%2BIlowMOE21lk%2FgN8IzhFjec9Q0buXQXSwilRQwG473l5%2FTimXY2JyruRAPRyzKPRywJtGzBT4o5%2BRjEDVmkN4nWTPWW%2BUBnxdZ7gqqw%2BCHgC9%2FzFtaoEZpOg6VeELY4rcdV1LbsUOXVwezkt2EIcQsmelCN1Yjje4wm7r%2F0gY6pgGmJNZs9zzBfxTqM0O06OLnTXZS%2BAMJawguncIcw1ftP2SZIt9lYh3tooe66o4S1MrmYR7HPKIka4YQLHa4KhKmTt1yv2WJ8WrEshMQCexB14muMEQaLqj2P7QG5379vuxkKO%2FcWP2smWt6Do55Sy5fEbhYQFWKoiJIqUHuCjuBbTVOPWmTqQwKfGBDvKlhAzLIP8rzoO9Go5KNmXPZdkwtm2qVIHBY&X-Amz-Signature=f0135be2cf90ca8f2d78c6903f9dcb8d2f07991f6495620f9c7b566a39399a2b&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

如果说你这个方法里边你要力度特别特别细怎么判，那你就再加个冒号。比如说你现在查数据库，你就是说 select DB 是不是你自己可以写 select DB 然后你查询缓存，你就可以写这个 select Redis 对不对？然后查 ES 搜索，比如说 select ES 都可以， lets search 都可以。


比如说看你这资源怎么定义，你这样去定义的话，起码有一个好处，就是说母资源肯定不会重复。好了，那你就把这个资源放到这里，这是我的资源。那我这个资源要设置什么？我说我要设置一种规则，叫做降级 degree 的 exception 好，很简单，我就来一个 degree 的一个三次就好了，我就拦截这个 degree 的三次，然后药房的资源被什么呢？被降级了，然后执行降级逻辑。正常来讲主逻辑没走的是降级逻辑对吧。


好了，然后这个写 greatok 接着跟大家做一个演示，怎么样去降级呢？有哪几种呢？当然这个还不长，因为这个是一个比较上层的API ，所以说我们就 block 就可以了。降级规则是什么样子？我们随便找一个。点开。降级有三种策略，第一种是 rt 就是平均的响应时长，如果太长了我就降级了。


还有第二种是什么是异常比例。这个异常比例比如说一秒钟，它的异常数比如说30%。说白了就是说一场比例一秒钟。如果说我一共总的请求数比如说 10 次，然后我出现异常，比如说出现了 4 次，那就会跑异常，因为你比例是30%。当然这个不一定是每秒是按照时间窗口就算了，这时间窗口你自己去定，比如说一秒钟之内你出了 5 次异常以上，那我就帮你去降级。

```java

/**
 *降级
*@return
*@throwsException
 */
@RequestMapping("/degrade")
public String degrade()throws Exception{

int count = 0;

    // 0: 引入依赖==============>使用 Sentinel 步骤

    // 初始话规则

    // 1: 定义资源
    while(true) {
Entry entry = null;
        try{
// 2.1 定义资源名称
            String resourceName = "com.bfxy.test.controlle.IndexController:degrade";

            entry = SphU.entry("degrade-test");

            if(count % 2 == 0) {
throw  new Exception("degrade --> 抛出异常");
}else{
Thread.sleep(20);
                System.out.println("执行正常");
}

// 2.2 执行职员逻辑代码

            Thread.sleep(20);

}catch(BlockException e) {
System.out.println("要访问的资源被流控了, 执行流控逻辑");
}finally{
if(entry != null) {
entry.exit();
}
        }
return "flow";
}
// 2: 定义规则

    // 3: 查看结果

    // 4：控制台

```


那其实我们可以模拟一下这个东西，我们都可以去通过代码去模拟的。比如说现在我可以这样去写，那这里边最简单的，我给他搞一个成员变量， private 一个 int 类型的 A 或者是用 count 来直接搞出来。默认等于 0 可以吧。 count 它有一个解耦线码，是不是我说 if count 它取 2 等于 0 的时候可以给它抛一个异常，因为它里边已经说了是不是这个异常的数量也可以有这里面异常的数量就是往出 sloth 异常。很简单，那我我就往出 sloth 异常，如果是这样的话，我就用 throw new 一个 exception excpti 问好了，然后这是我自定义复查，然后在这里边我肯定得 catch 住了，是不是因为我是 exception 所以在这里边立克三分。 OK 好了，就是偶数的时候就抛一个异常，然后激素的时候失联 20 毫秒。然后打印一句话说执行正常可以，就表示我这个 degree 的是执行正常的。然后这个是 degree 的抛出异常。可以吧，抛出异常，然后这个是 gray 的执行正常。


好了，然后我的代码逻辑已经写完了，那现在我写完代码之后又加了一个 degree 的策略，那这个策略是不是我也应该有对不对？好了，那这个策略我们来写一写，很简单一样的道理，把它 copy 一份改一下，然后叫做一个瑞，现在你只能是这么麻烦，因为现在我们还没有去学那种注解的方式。其实后面我们学注解的方式你会发现这东西没必要写这么复杂，我用注解就好了。


然后这里边我们用 degree 的 rule degrade ruler 好，把它都换成 degree 的 rule degree 的 grade 然后这个是变成 degree 的 rule manager 的 loadok 搞定好了，保存一下。然后这个 degree 的这里边肯定它的 resource 是谁，resource肯定是变成这个我们之前的这个 name 了，这个 name 我暂时就不把它写成全局的了，我就是 ctrl C ctrl E 把它 copy 一份过来，就是这个资源。那我们现在用的肯定不是 follow rules 我们用的就是 degree 的 ruler 对吧，这个 degree 的我们设置这个 count 对不对？好异常的 count 数。比如说一秒钟之内如果大于两次出现两个 exception 那我就帮你去做这个事情。 load 好，然后最后 init degrade ruler 就可以了。

[image](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/c8988989-5956-44a0-9545-d8560acd55c7/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667Y545HHM%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T225836Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIFPSshXlvM1JOzjFfHlKEi98yds0w%2F31tMAGqKF9OwApAiAMPG8hGA1rtL2strvIWahoptEoX7NYydYpUZD4%2FEF9qCqIBAjG%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMShKKghTQKJfsF2d%2BKtwDXu3tG6NoPBWz1JYAHY4Nh6E5ZVaHWez7HfD5SjdHVotrdspzJ7Lkra8bR%2BOC5qFoSlhkk3Jd5zthpb6niKgARYUuV9TVbzzmSkpaqwyPy3mO6vQSlo7zez98ceRmrHWg4QxC2nNfjAbec4oL0EglgJFcmHM3RWa0TtL1Mrd4FIsjsYY7%2FowMiubhFisyYxb%2FhcmSdkA1lKQ17QUmVc0g7mbRFBEosow1aKcXEqPY%2BNPfdqA2ZIFR21argO8eNoRp%2B%2BPLPo5p5COJ8Dk%2FsXxP3ZFbm%2FN37%2FP3eDljXvR6LF1u2Q%2BYFHuGTtjcw0iR1%2Fq4s8%2BbCX%2B2OwhqsN34uBVGZeta272HR6b4gvaEt%2FWB15ofvtiBN3P%2FrJll08u7yfJE4LEZC26SEjnhEwB0Ry06HiTp%2FuCiHUtfDDgPaPOOyxsdEVvqonpWsddUyWPppim9n6%2FUOSK27IDNcjOD%2FApxZkuRkg%2BIlowMOE21lk%2FgN8IzhFjec9Q0buXQXSwilRQwG473l5%2FTimXY2JyruRAPRyzKPRywJtGzBT4o5%2BRjEDVmkN4nWTPWW%2BUBnxdZ7gqqw%2BCHgC9%2FzFtaoEZpOg6VeELY4rcdV1LbsUOXVwezkt2EIcQsmelCN1Yjje4wm7r%2F0gY6pgGmJNZs9zzBfxTqM0O06OLnTXZS%2BAMJawguncIcw1ftP2SZIt9lYh3tooe66o4S1MrmYR7HPKIka4YQLHa4KhKmTt1yv2WJ8WrEshMQCexB14muMEQaLqj2P7QG5379vuxkKO%2FcWP2smWt6Do55Sy5fEbhYQFWKoiJIqUHuCjuBbTVOPWmTqQwKfGBDvKlhAzLIP8rzoO9Go5KNmXPZdkwtm2qVIHBY&X-Amz-Signature=7e5473d823ffc6f7044ddfde433d2b92b751b06829d95234d9612e3275192ba4&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

好两种规则我都加载一下。搞定好了。那在这里我们一起来把这个应用程序再重新起来。很简单。 Java OK 评审好。规则加载完毕。规则加载完毕之后，我们来看一下，这回我们再刷一下。直接f5。我的 dashboard 它的机器列表是没有的，是不是它是没有任何服务的？因为还是那个问题懒加载的问题？是不是你要刷？你刷一下之后你会看到这个 follow 请求。


好了，然后我们再看一下这个sentence ，我再刷一下。这回就有实力了，看见了吗？然后这个实力你会发现怎么只有 hello world 的实力对不对？怎么持有 hello word 这个资源呢？我们 degree 的， degree 的你也得要做这个事情，就是你也得要刷一下，它是懒加载的机制。


great 汽车那个名字应该不叫 degree 的叫啥？看一下他抛异常了。当然抛出异常是正常的，因为异常是我自己 throw 的，不过没关系，他既然抛出异常，他就那肯定就有我们再刷一下。我就想让他看到抛出异常刚才确实是抛异常的。但是抛异常之后，因为我已经把这个链路已经访问过了，所以说在触点链路里边，你又看到这两个资源，一个是我们之前定义的 hello world 资源。

[image](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/846330a2-5ab8-458e-9144-e1428373108d/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667Y545HHM%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T225836Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIFPSshXlvM1JOzjFfHlKEi98yds0w%2F31tMAGqKF9OwApAiAMPG8hGA1rtL2strvIWahoptEoX7NYydYpUZD4%2FEF9qCqIBAjG%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMShKKghTQKJfsF2d%2BKtwDXu3tG6NoPBWz1JYAHY4Nh6E5ZVaHWez7HfD5SjdHVotrdspzJ7Lkra8bR%2BOC5qFoSlhkk3Jd5zthpb6niKgARYUuV9TVbzzmSkpaqwyPy3mO6vQSlo7zez98ceRmrHWg4QxC2nNfjAbec4oL0EglgJFcmHM3RWa0TtL1Mrd4FIsjsYY7%2FowMiubhFisyYxb%2FhcmSdkA1lKQ17QUmVc0g7mbRFBEosow1aKcXEqPY%2BNPfdqA2ZIFR21argO8eNoRp%2B%2BPLPo5p5COJ8Dk%2FsXxP3ZFbm%2FN37%2FP3eDljXvR6LF1u2Q%2BYFHuGTtjcw0iR1%2Fq4s8%2BbCX%2B2OwhqsN34uBVGZeta272HR6b4gvaEt%2FWB15ofvtiBN3P%2FrJll08u7yfJE4LEZC26SEjnhEwB0Ry06HiTp%2FuCiHUtfDDgPaPOOyxsdEVvqonpWsddUyWPppim9n6%2FUOSK27IDNcjOD%2FApxZkuRkg%2BIlowMOE21lk%2FgN8IzhFjec9Q0buXQXSwilRQwG473l5%2FTimXY2JyruRAPRyzKPRywJtGzBT4o5%2BRjEDVmkN4nWTPWW%2BUBnxdZ7gqqw%2BCHgC9%2FzFtaoEZpOg6VeELY4rcdV1LbsUOXVwezkt2EIcQsmelCN1Yjje4wm7r%2F0gY6pgGmJNZs9zzBfxTqM0O06OLnTXZS%2BAMJawguncIcw1ftP2SZIt9lYh3tooe66o4S1MrmYR7HPKIka4YQLHa4KhKmTt1yv2WJ8WrEshMQCexB14muMEQaLqj2P7QG5379vuxkKO%2FcWP2smWt6Do55Sy5fEbhYQFWKoiJIqUHuCjuBbTVOPWmTqQwKfGBDvKlhAzLIP8rzoO9Go5KNmXPZdkwtm2qVIHBY&X-Amz-Signature=b6748dd798ed21a58ad653efcddd2fc54651d24988251b682eb752b3f8284625&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

[image](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/9937b8bb-e7c5-4d1b-af47-09bce8bbb4ec/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667Y545HHM%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T225836Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIFPSshXlvM1JOzjFfHlKEi98yds0w%2F31tMAGqKF9OwApAiAMPG8hGA1rtL2strvIWahoptEoX7NYydYpUZD4%2FEF9qCqIBAjG%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMShKKghTQKJfsF2d%2BKtwDXu3tG6NoPBWz1JYAHY4Nh6E5ZVaHWez7HfD5SjdHVotrdspzJ7Lkra8bR%2BOC5qFoSlhkk3Jd5zthpb6niKgARYUuV9TVbzzmSkpaqwyPy3mO6vQSlo7zez98ceRmrHWg4QxC2nNfjAbec4oL0EglgJFcmHM3RWa0TtL1Mrd4FIsjsYY7%2FowMiubhFisyYxb%2FhcmSdkA1lKQ17QUmVc0g7mbRFBEosow1aKcXEqPY%2BNPfdqA2ZIFR21argO8eNoRp%2B%2BPLPo5p5COJ8Dk%2FsXxP3ZFbm%2FN37%2FP3eDljXvR6LF1u2Q%2BYFHuGTtjcw0iR1%2Fq4s8%2BbCX%2B2OwhqsN34uBVGZeta272HR6b4gvaEt%2FWB15ofvtiBN3P%2FrJll08u7yfJE4LEZC26SEjnhEwB0Ry06HiTp%2FuCiHUtfDDgPaPOOyxsdEVvqonpWsddUyWPppim9n6%2FUOSK27IDNcjOD%2FApxZkuRkg%2BIlowMOE21lk%2FgN8IzhFjec9Q0buXQXSwilRQwG473l5%2FTimXY2JyruRAPRyzKPRywJtGzBT4o5%2BRjEDVmkN4nWTPWW%2BUBnxdZ7gqqw%2BCHgC9%2FzFtaoEZpOg6VeELY4rcdV1LbsUOXVwezkt2EIcQsmelCN1Yjje4wm7r%2F0gY6pgGmJNZs9zzBfxTqM0O06OLnTXZS%2BAMJawguncIcw1ftP2SZIt9lYh3tooe66o4S1MrmYR7HPKIka4YQLHa4KhKmTt1yv2WJ8WrEshMQCexB14muMEQaLqj2P7QG5379vuxkKO%2FcWP2smWt6Do55Sy5fEbhYQFWKoiJIqUHuCjuBbTVOPWmTqQwKfGBDvKlhAzLIP8rzoO9Go5KNmXPZdkwtm2qVIHBY&X-Amz-Signature=427b3f7c74484446537660711a73c62b15aa98316e3977068ccfdc85411a7c0a&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

[image](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/ded05462-339e-4ac5-b550-5d1971c8bec2/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667Y545HHM%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T225836Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIFPSshXlvM1JOzjFfHlKEi98yds0w%2F31tMAGqKF9OwApAiAMPG8hGA1rtL2strvIWahoptEoX7NYydYpUZD4%2FEF9qCqIBAjG%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMShKKghTQKJfsF2d%2BKtwDXu3tG6NoPBWz1JYAHY4Nh6E5ZVaHWez7HfD5SjdHVotrdspzJ7Lkra8bR%2BOC5qFoSlhkk3Jd5zthpb6niKgARYUuV9TVbzzmSkpaqwyPy3mO6vQSlo7zez98ceRmrHWg4QxC2nNfjAbec4oL0EglgJFcmHM3RWa0TtL1Mrd4FIsjsYY7%2FowMiubhFisyYxb%2FhcmSdkA1lKQ17QUmVc0g7mbRFBEosow1aKcXEqPY%2BNPfdqA2ZIFR21argO8eNoRp%2B%2BPLPo5p5COJ8Dk%2FsXxP3ZFbm%2FN37%2FP3eDljXvR6LF1u2Q%2BYFHuGTtjcw0iR1%2Fq4s8%2BbCX%2B2OwhqsN34uBVGZeta272HR6b4gvaEt%2FWB15ofvtiBN3P%2FrJll08u7yfJE4LEZC26SEjnhEwB0Ry06HiTp%2FuCiHUtfDDgPaPOOyxsdEVvqonpWsddUyWPppim9n6%2FUOSK27IDNcjOD%2FApxZkuRkg%2BIlowMOE21lk%2FgN8IzhFjec9Q0buXQXSwilRQwG473l5%2FTimXY2JyruRAPRyzKPRywJtGzBT4o5%2BRjEDVmkN4nWTPWW%2BUBnxdZ7gqqw%2BCHgC9%2FzFtaoEZpOg6VeELY4rcdV1LbsUOXVwezkt2EIcQsmelCN1Yjje4wm7r%2F0gY6pgGmJNZs9zzBfxTqM0O06OLnTXZS%2BAMJawguncIcw1ftP2SZIt9lYh3tooe66o4S1MrmYR7HPKIka4YQLHa4KhKmTt1yv2WJ8WrEshMQCexB14muMEQaLqj2P7QG5379vuxkKO%2FcWP2smWt6Do55Sy5fEbhYQFWKoiJIqUHuCjuBbTVOPWmTqQwKfGBDvKlhAzLIP8rzoO9Go5KNmXPZdkwtm2qVIHBY&X-Amz-Signature=6932ef7711d1bf1751f5584b64fb9a7fd053e7438746a26cab4926b95f208249&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

[image](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/84a1480c-0ef9-40ef-a73f-f9c401ed4833/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667Y545HHM%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T225836Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIFPSshXlvM1JOzjFfHlKEi98yds0w%2F31tMAGqKF9OwApAiAMPG8hGA1rtL2strvIWahoptEoX7NYydYpUZD4%2FEF9qCqIBAjG%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMShKKghTQKJfsF2d%2BKtwDXu3tG6NoPBWz1JYAHY4Nh6E5ZVaHWez7HfD5SjdHVotrdspzJ7Lkra8bR%2BOC5qFoSlhkk3Jd5zthpb6niKgARYUuV9TVbzzmSkpaqwyPy3mO6vQSlo7zez98ceRmrHWg4QxC2nNfjAbec4oL0EglgJFcmHM3RWa0TtL1Mrd4FIsjsYY7%2FowMiubhFisyYxb%2FhcmSdkA1lKQ17QUmVc0g7mbRFBEosow1aKcXEqPY%2BNPfdqA2ZIFR21argO8eNoRp%2B%2BPLPo5p5COJ8Dk%2FsXxP3ZFbm%2FN37%2FP3eDljXvR6LF1u2Q%2BYFHuGTtjcw0iR1%2Fq4s8%2BbCX%2B2OwhqsN34uBVGZeta272HR6b4gvaEt%2FWB15ofvtiBN3P%2FrJll08u7yfJE4LEZC26SEjnhEwB0Ry06HiTp%2FuCiHUtfDDgPaPOOyxsdEVvqonpWsddUyWPppim9n6%2FUOSK27IDNcjOD%2FApxZkuRkg%2BIlowMOE21lk%2FgN8IzhFjec9Q0buXQXSwilRQwG473l5%2FTimXY2JyruRAPRyzKPRywJtGzBT4o5%2BRjEDVmkN4nWTPWW%2BUBnxdZ7gqqw%2BCHgC9%2FzFtaoEZpOg6VeELY4rcdV1LbsUOXVwezkt2EIcQsmelCN1Yjje4wm7r%2F0gY6pgGmJNZs9zzBfxTqM0O06OLnTXZS%2BAMJawguncIcw1ftP2SZIt9lYh3tooe66o4S1MrmYR7HPKIka4YQLHa4KhKmTt1yv2WJ8WrEshMQCexB14muMEQaLqj2P7QG5379vuxkKO%2FcWP2smWt6Do55Sy5fEbhYQFWKoiJIqUHuCjuBbTVOPWmTqQwKfGBDvKlhAzLIP8rzoO9Go5KNmXPZdkwtm2qVIHBY&X-Amz-Signature=0b35efde3de671c8518fadb4316d43b0cdee32bbd764be88ef7f4b225c9ae1c7&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

[image](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/8f9aa767-3f91-4c47-a67c-0478745613c8/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667Y545HHM%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T225836Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIFPSshXlvM1JOzjFfHlKEi98yds0w%2F31tMAGqKF9OwApAiAMPG8hGA1rtL2strvIWahoptEoX7NYydYpUZD4%2FEF9qCqIBAjG%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMShKKghTQKJfsF2d%2BKtwDXu3tG6NoPBWz1JYAHY4Nh6E5ZVaHWez7HfD5SjdHVotrdspzJ7Lkra8bR%2BOC5qFoSlhkk3Jd5zthpb6niKgARYUuV9TVbzzmSkpaqwyPy3mO6vQSlo7zez98ceRmrHWg4QxC2nNfjAbec4oL0EglgJFcmHM3RWa0TtL1Mrd4FIsjsYY7%2FowMiubhFisyYxb%2FhcmSdkA1lKQ17QUmVc0g7mbRFBEosow1aKcXEqPY%2BNPfdqA2ZIFR21argO8eNoRp%2B%2BPLPo5p5COJ8Dk%2FsXxP3ZFbm%2FN37%2FP3eDljXvR6LF1u2Q%2BYFHuGTtjcw0iR1%2Fq4s8%2BbCX%2B2OwhqsN34uBVGZeta272HR6b4gvaEt%2FWB15ofvtiBN3P%2FrJll08u7yfJE4LEZC26SEjnhEwB0Ry06HiTp%2FuCiHUtfDDgPaPOOyxsdEVvqonpWsddUyWPppim9n6%2FUOSK27IDNcjOD%2FApxZkuRkg%2BIlowMOE21lk%2FgN8IzhFjec9Q0buXQXSwilRQwG473l5%2FTimXY2JyruRAPRyzKPRywJtGzBT4o5%2BRjEDVmkN4nWTPWW%2BUBnxdZ7gqqw%2BCHgC9%2FzFtaoEZpOg6VeELY4rcdV1LbsUOXVwezkt2EIcQsmelCN1Yjje4wm7r%2F0gY6pgGmJNZs9zzBfxTqM0O06OLnTXZS%2BAMJawguncIcw1ftP2SZIt9lYh3tooe66o4S1MrmYR7HPKIka4YQLHa4KhKmTt1yv2WJ8WrEshMQCexB14muMEQaLqj2P7QG5379vuxkKO%2FcWP2smWt6Do55Sy5fEbhYQFWKoiJIqUHuCjuBbTVOPWmTqQwKfGBDvKlhAzLIP8rzoO9Go5KNmXPZdkwtm2qVIHBY&X-Amz-Signature=2c77d452a32f5caa71ed205a28b6b7b67356785251e434579c69b708beed61b4&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)


还有一个就是刚才我写的这个根据权限命名的阿尔名冒号风格的这个流控的策略。那这个策略到底起没起到作用呢？我们去降级策略里看一看就好了。然后这个降级规则现在是没有的，这个降级规则是空的，那证明我没有把这个规则加进来，我不过无所谓，它既然能够识别就好了，我就可以动态去改好，现在这个降级规则是没有的，那没办法，我给它加一个不就好了吗？这个资源我能识别对不对？我给它加一个规则。好，我给它变成异常数，我说异常数在一秒钟之内或者是再大一点。两秒钟之内。如果说大于两次，那我就降级新增一规则，看见了。两秒钟。你看这回我的降级规则就有了。说两秒钟之内如果大于两次，我就降级。那同学们你发现了一件事情了没有？这个规则我压根初始化的时候，我即使是不给它定义规则，那我也可以通过 dashboard 动态给他加。



现在既然这个资源两个资源都有了，对于流控的 20 阈值，后面好像把它改成 6 了，是不是我服务器一重启，这规则又都没了？然后他这个重又重新加载的时候，又把加载的那个规则就写出去了，所以说这是一个比较致命的问题，后面我们一起去解决。当然阿里也给你了这个 sense 也给你了一些持久化的规则以及扩展。这就是我们后面在实战的时候重点要做的，就是重启了这个规则就不见了。那这个不太好了，我们看降级有了这个降级规则，那我就可以去玩这个 degree 了。
我说一次两次三次，我去访问了好多次，防瑞好多次，肯定不是每次都去抛这个异常，有的抛有的不抛，因为我是极有数。 OK 我先把这个服务停掉，我说怎么一直抛异常没任何。那什么呢？同学们你发现了一个小问题，没对，那个 ia 进行加加，这就尴尬了是不是？好了，把它这个加个加加个加加个数，你说默认是 0 是不是？但这个除以 21 直等于一直跑异常。然后他做完这个事情之后我不管了，就是说每次进来一次我都对这个看看进行加加可以吧，每次进来一次我都加进来一次我的加加这样就好了，不管它抛异常还是说不抛异常。总之访问一下我就加一个值，然后我再次去启动一下。就 run as application 资源加载完毕之后，然后我们来刷一下。好，但是 bot 还是没有，因为你还是懒加载机制，所以说你还是要先访问一下 follow 访问 follow 是没问题的，然后你再访问一下这个 degree 的。


好，帝贵的，这是成功的，因为我们是取二等零的时候才是帮我去抛异常不等零的时候，那就是什么呢？那就是正常执行逻辑对吧？没有代码是不是去写的？你看到了对吧，开始第一次的时候，这个边上一取二等于 1 肯定不跑异常对吧，肯定会走这个。那第二次的时候肯定跑你异常对吧？那接下来我们来看一看这个 dashboard 了，翻一下 f5 刷一下，我们看一下资源链路，两个资源都有。然后我看一下降级规则没有对不对？降级规则还是没加载上来证明我那个代码会写的有点问题。没关系，然后这 QPS 这个是有的，应该还是20。 OK 那接下来我们看一下怎么去做。接下来我们给它定义一个降级规则。好吧，我们把这个规则就它，我定义一个降级的规则，说两秒钟两次，我要把它设置成这个日异常数你不能是 rt rt 是平均响应时长。我们设置异常数就是说两秒的时间窗口内如果你异常数大于2，那就帮你降级，然后新增好了，现在有这个规则之后，然后我刷去F ， f5 疯狂的刷好。


烧完了之后来我看一下我们的控制台，正常执行抛异常。正常执行抛异常对吧，这都有的。那现在有一个问题出来了，正常执行抛出异常。正常执行抛出异常。那为什么没有帮我去做什么呢？降级就是说我们的降级的逻辑没有执行，因为你现在抛出的异常太大。 OK 来我们一起来改一下。那我们可以看到就是我们之前这个做法就是相当于用一个 block exception 去做的。那其实对于 locking session ，其实你最好这里边你把这个异常再扩大一点，比如说是 snowball snowball 就可以有这个业务异常对吧？那这个 super 然后你再抛出 exception 的时候，这样的话不管怎么样他都能捕获，然后都会打印这句话。那这样的话其实你就看不出来什么效果了。


那这一块其实对于这个异常，你其实比较难去看到结果。如果是抛异常，按照异常个数的，其实你可以通过官方其实它也有说明，我们可以看一看熔断降级它是怎么去说的。论证您说了就是说可以异常比例或者是异常数对不对？就是说这个资源在一分钟之内。如果说出现异常的数量超过这个阈值，比如说一分钟超过了 10 个异常，那我就可以对它做相机。但你要注意一个问题，这个异常只是针对于业务异常，对 sentence 自己的流控异常本身它是不生效的，就是 block exception 就是不影响。那你可以去用他自己的其他的业务去统计。当然我们在这里可以去换一种方式，比如说我们来设置一下他的 rt 就是平均系统的时间，我们可以做一下设置。


在这里我们可以换一种角度来思考，比如说在这里它是奇偶性。那如果说取于 2 等于 0 的时候，我就不让它跑异常，可以吗？比如说取 2 等于 0 的时候，比如说我写死这个 blocking exception 然后去表示降级。那这一块我怎么去做呢？比如说曲二等于零的时候，我让它这个响应时间睡眠的时间长一点，然后它睡眠 100 毫秒短一点。然后我说我这个规则可以改一下，这规则改成什么呢？我说平均响应时长每秒钟，如果是大于 30 毫秒，我就做一个降级，这可不可以，这是也可以的。我来看看能不能出现这个结果。
首先把它启动一下 run S Java application 其实你只要看到它，最终你看我现在整个代码都没有抛异常对不对？正常执行这是 100 毫秒，然后这边写正常执行 20 毫秒对吧，他们之间差了 5 倍。好了，这回我再把它骑起来一下，就是看到结果其实还不太好，容不太容易去看。当然后面我们去学注解的时候，你要看到结果就容易多了。
好了，我们现在来做一下这个测试，现在我还是首先访问一下 degree 的，没问题，然后访问一下我们的 follow 没问题。然后紧接着我刷新一下我的 dashboard 好，然后我们看一下缩减链路都有了对吧，我们来看一下这个 degree 的，把它加一个降级的策略。


说 rt 大于 30 毫秒，平均响应窗口 1 秒钟之内。如果大于 30 毫秒的话，那我就抛那个一场可以吧，这样的话应该能看到结果。 OK 那我们来看一下这个迪瑞的回车，然后回车访问了几次。同学们你看访问的资源被降级了，这样的话你就真正争论 get 到这个 degree 的这种异常了。因为这里边我做了一个除法，因为反正我取约 2 等于 0 和 100 取 2 不等于 0 的，那肯定是 20 毫秒，就搞定了取 2 等于 0 的 100 毫秒。那他们两个之间综合一下是不是都是平均的，肯定是大于我自己设置的 30 毫秒。
那这个就能体现出来这种策略的主要的这个思路了，因为你看我没有任何异常，他自己会帮我去 catch 到 degree 的异常，然后打印这句话，你不像那个抛出异常，抛出异常他肯定能 catch 到。所以说这个你不太好统计，你只能是加一个爱的方法自己去普及才行。


好了，基本上来讲，我们对于 sentence dashboard 哨兵控制台这块跟大家也就讲完了，大家知道怎么用了。当然注意它有一个硬伤是什么，就是我的服务一重启，你之前配的这几个规则什么的也就都没了，它只能是初始化的时候加载，你重启的时候它规则还得重复，初始化还得保持以前的你这做了计时修改，你说我把这 20 变成15，你现在服务器不重启，这是好使的，一重启就都不好使了，这是一个硬伤。后面我们把这些规则能够做一个持久化，然后再重启的时候去读那个持久化的规则，这是最好的。好了。那这节课我们主要讲的就是这个 dashboard 通过一个流控和一个降级两个策略，跟着小伙伴们把这个控制台熟悉了一下，感谢小伙伴们收看这节课，先到这

