---
title: 2-13  本地消息表（定时任务）
---

# 2-13  本地消息表（定时任务）

[image](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/298e3a65-dc9b-4dc7-be57-7ab3d2af0a56/SCR-20240808-fiok.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665P52I4X3%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T225436Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIQC9BnaIb7Y3NGbZJXMAWZ1ObYCPKS44ty9kZ7vvO%2BNVQAIfHW1eAsGd97EzfxYQAuJKYBkPjqHo1w1z2V8Nn72KrCqIBAjG%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMX5szKKlpyK1LfHtSKtwDQ8xJmtPQ0m2Bh7fbPWtbAYK7qHcEICDTrH6ZPW0UV2xFhqRRTKdArggtL0MPis8yxOhGxlGkxriHgD9fxt1bSuYf0qxLVkVWHBMT1bRDqWOY7o5ptjXrYM2JNSNVyyvtBaLmsx5LPvQi0r%2F%2BVDfEi7kl7GDFbQgRcYeBJiNinwfSthP1ehxIlQ%2FO%2B7vzzSsomASj5BIFKX4t9a4g%2BOeP%2FA1OxLvi5gX0UAH7hVnnqYAtzfeefUlOKNyBZskh92gSv9o5%2FC6yndkDJKOyA18rbVVa%2FVoE2HFC3IkN%2B2KLz%2BV0at1NQnJMJVmr2XiyTSje%2BprFBcb%2FqRcM%2BQaB21YJQN4DMNeckVrLH%2BZ5Jc523SLflk9ISvcohDdlvDA2VEtRvWNuYEIHnU7eXMGpXZ2jFxMI13Dc5EYI1eT2sCHDSoCA0NzKun9KRQpba3p4ysBOxPxf%2BD2kqaha0Pa5ov7qPyvXbF6scChOAqylxXN%2FpeucvRyY6iwe6S572LjXDMEvgJ0d0V3YM8m5XHweaqLDhjpIKbfjXpL%2Bk4E69gftkHdjHcyB2nSYYTBDuOoH2zwW0LOXApg9m1c5%2BvPmq6HsydPi0DhzY1f6vBJCOGRKE%2BEA2fyNk02K0DMXvvMwlbf%2F0gY6pgE7zhJEItj0q7R5P2gOscmN7MAgWg3bZpr9ELIpY32EnOeq14XgdvJIftnzk6qE%2BFI%2Fg1z%2BcrtC%2F%2BpkPVreIrQAqxBPZ%2FKcslA5g77wM4ngWkU%2F%2Fgs7u1Alj4aTRTJnoqn8Lsus4kGaw7F1fAZomuKIxxGoBaBVdivgWNrKloHNs5jPFqO3j13E%2FRFQGVHVQvpRN9FYeQVTuItLOHI8BsyHXl1W1vUa&X-Amz-Signature=d4b15be0fce68d9357a7bfdc8ccede1770c24783dd0975fd07ba45deec7e5d88&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

[image](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/24998775-5990-46e4-98e0-6faa6fd9f006/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665P52I4X3%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T225436Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIQC9BnaIb7Y3NGbZJXMAWZ1ObYCPKS44ty9kZ7vvO%2BNVQAIfHW1eAsGd97EzfxYQAuJKYBkPjqHo1w1z2V8Nn72KrCqIBAjG%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMX5szKKlpyK1LfHtSKtwDQ8xJmtPQ0m2Bh7fbPWtbAYK7qHcEICDTrH6ZPW0UV2xFhqRRTKdArggtL0MPis8yxOhGxlGkxriHgD9fxt1bSuYf0qxLVkVWHBMT1bRDqWOY7o5ptjXrYM2JNSNVyyvtBaLmsx5LPvQi0r%2F%2BVDfEi7kl7GDFbQgRcYeBJiNinwfSthP1ehxIlQ%2FO%2B7vzzSsomASj5BIFKX4t9a4g%2BOeP%2FA1OxLvi5gX0UAH7hVnnqYAtzfeefUlOKNyBZskh92gSv9o5%2FC6yndkDJKOyA18rbVVa%2FVoE2HFC3IkN%2B2KLz%2BV0at1NQnJMJVmr2XiyTSje%2BprFBcb%2FqRcM%2BQaB21YJQN4DMNeckVrLH%2BZ5Jc523SLflk9ISvcohDdlvDA2VEtRvWNuYEIHnU7eXMGpXZ2jFxMI13Dc5EYI1eT2sCHDSoCA0NzKun9KRQpba3p4ysBOxPxf%2BD2kqaha0Pa5ov7qPyvXbF6scChOAqylxXN%2FpeucvRyY6iwe6S572LjXDMEvgJ0d0V3YM8m5XHweaqLDhjpIKbfjXpL%2Bk4E69gftkHdjHcyB2nSYYTBDuOoH2zwW0LOXApg9m1c5%2BvPmq6HsydPi0DhzY1f6vBJCOGRKE%2BEA2fyNk02K0DMXvvMwlbf%2F0gY6pgE7zhJEItj0q7R5P2gOscmN7MAgWg3bZpr9ELIpY32EnOeq14XgdvJIftnzk6qE%2BFI%2Fg1z%2BcrtC%2F%2BpkPVreIrQAqxBPZ%2FKcslA5g77wM4ngWkU%2F%2Fgs7u1Alj4aTRTJnoqn8Lsus4kGaw7F1fAZomuKIxxGoBaBVdivgWNrKloHNs5jPFqO3j13E%2FRFQGVHVQvpRN9FYeQVTuItLOHI8BsyHXl1W1vUa&X-Amz-Signature=63258791c1f6745f25474482e6ff4841daca02faca920b2398c88723e0c78cac&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

最后一步，咱们要把这个消息发送给这个订单处理接口，编写这么一个定时任务是吧。这个定时任务第一步咱们要在这个启动类上加上一个注解。 enable scheduling 是吧，标志着咱们的这个项目是可以使用定时任务的，

[image](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/9cc3bf73-14a6-41d1-b12d-3de75c987e16/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665P52I4X3%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T225436Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIQC9BnaIb7Y3NGbZJXMAWZ1ObYCPKS44ty9kZ7vvO%2BNVQAIfHW1eAsGd97EzfxYQAuJKYBkPjqHo1w1z2V8Nn72KrCqIBAjG%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMX5szKKlpyK1LfHtSKtwDQ8xJmtPQ0m2Bh7fbPWtbAYK7qHcEICDTrH6ZPW0UV2xFhqRRTKdArggtL0MPis8yxOhGxlGkxriHgD9fxt1bSuYf0qxLVkVWHBMT1bRDqWOY7o5ptjXrYM2JNSNVyyvtBaLmsx5LPvQi0r%2F%2BVDfEi7kl7GDFbQgRcYeBJiNinwfSthP1ehxIlQ%2FO%2B7vzzSsomASj5BIFKX4t9a4g%2BOeP%2FA1OxLvi5gX0UAH7hVnnqYAtzfeefUlOKNyBZskh92gSv9o5%2FC6yndkDJKOyA18rbVVa%2FVoE2HFC3IkN%2B2KLz%2BV0at1NQnJMJVmr2XiyTSje%2BprFBcb%2FqRcM%2BQaB21YJQN4DMNeckVrLH%2BZ5Jc523SLflk9ISvcohDdlvDA2VEtRvWNuYEIHnU7eXMGpXZ2jFxMI13Dc5EYI1eT2sCHDSoCA0NzKun9KRQpba3p4ysBOxPxf%2BD2kqaha0Pa5ov7qPyvXbF6scChOAqylxXN%2FpeucvRyY6iwe6S572LjXDMEvgJ0d0V3YM8m5XHweaqLDhjpIKbfjXpL%2Bk4E69gftkHdjHcyB2nSYYTBDuOoH2zwW0LOXApg9m1c5%2BvPmq6HsydPi0DhzY1f6vBJCOGRKE%2BEA2fyNk02K0DMXvvMwlbf%2F0gY6pgE7zhJEItj0q7R5P2gOscmN7MAgWg3bZpr9ELIpY32EnOeq14XgdvJIftnzk6qE%2BFI%2Fg1z%2BcrtC%2F%2BpkPVreIrQAqxBPZ%2FKcslA5g77wM4ngWkU%2F%2Fgs7u1Alj4aTRTJnoqn8Lsus4kGaw7F1fAZomuKIxxGoBaBVdivgWNrKloHNs5jPFqO3j13E%2FRFQGVHVQvpRN9FYeQVTuItLOHI8BsyHXl1W1vUa&X-Amz-Signature=5293d83ac06b654f86f222cb3f6c17c8bec41093ee296d5644d278c43a6eaea5&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

然后咱们再创建一个 service 这个 service 主要是运行这个定时任务对吧，这个类咱们叫做叫什么呢？叫 order scheduler 。 scheduler 好吧，同样也要打上一个 service 的注解。里边咱们要写一个方法是吧。 public void 这个方法就要给这个订单处理接口发送通知是吧，这个咱们叫什么叫做 order notify 。


好吧，首先第一步咱们要把所有状态为未发送的消息给它取出来是吧。那么这里边咱们还是要把这个 payment message map 给它注入进来，加上对 source 的注解。然后咱们要检索出发送状态等于未发送的这块咱们要写一个 payment example 是吧。 payment message example new payment message example 然后 criteria 然后 and status equals two 什么 0 是吧，0是未发送。然后咱们用这个 viper 给它检索一下 select by example 对吧。


然后 payment message example 如果这个 message 不存在的话或者它等于空，咱们就直接结束了是吧。 payment message 等于等于，那是吧或者它的赛字等于0，咱们就直接 return 对吧。如果它不为空的话，咱们要它对吧，便利找到每一个订单的 ID 是吧。把订单 ID 给它取出来 at all the ID 然后请求这个处理订单的接口是吧。这块咱们怎么去做呢？咱们要通过 HTTP client 要调用这个订处理订单的接口是吧。


那么在咱们的项目当中还要引入 httd client 的这个依赖是吧？咱们还是先进入到这个浏览器，进入到 mvn reposity 搜索一下 HC DP 是吧，HT DP 阿帕奇对吧，搜索一下一个阿帕奇 h7 at client 对吧，点进去，选最新的这个版本四点五点一零。咱们把这个依赖给它复制一下，粘贴到咱们的项目当中，进入到 pom 文件，把这个依赖给它粘贴过来，刷新一下。


Maven 引入成功了是吧，咱们再进入到这个定时任务的这个类这块，咱们要给他创建 HTTP client HTTP client 对吧，这是 TTP client builder 也就是这第一个它是阿帕奇的这个包下边的。那么选中它然后 create 是吧，然后选择 build 就直接创建了一这个 HTTP client 了是吧，叫做 HTTP client 好吧，这样这个 HTTP client 创建好以后咱们要 excuse 是吧执行这个请求，咱们看看选择执行哪一个，咱们选择执行这第一个是不是就可以了。


htpuri request 是吧，就是这第一个。那么在这之前咱们要写一个 HTTP URI request URI request 这个是吧，咱们你有一个咱们看，这个 HTTP URI request 它是一个接口是吧，咱们点进去看一下，看一下它有哪些实现类，咱们直接选择这个 HT pose 对吧，这个就可以了。我复制一下粘贴过来这个 pose 引入一下，然后里边传入咱们的这个地址是吧，这个地址咱们写一下。 HTTP local host 8080，然后 handle order 是吧。再，看看它有没有看那它能不能设置这个咱们传递的参数。没有参数是吧，没有参数咱们改一下，把这个直接改成一些信息地 post 这是 tdp post 这回咱们来看一下点 set ntt 是吧。 httntt 那么前面咱们还是要写一下这个。 Httntt. 同样它也是一个接口是吧，咱们点进去看一下它有哪些实现类。


那么我找，咱们使用最后一个 URL encoded form entity 是吧，这个是一个 form 表单的这种形式，咱们还是使用这个，然后看一下它的构造函数。
构造函数它是一个内部 y6 的一个对是吧，看看它的构造函数里边传入的参数是需要你继承内部 value 是吧。那么前面咱们还是要写一个内部 value pair 是吧，这个第一个是 ocid order ID pair 等于 new 内部 value pair 这个咱们写这个最基本的 basic 内部 value pair 是吧，里边传入咱们的这个键值段 order ID 它的值就是咱们从这个 payment message 当中取出来的这个 order ID 是吧，这个还不能使用 int 性，要使用 string 类型的，咱们给它转一下这样是不是就行了？然后咱们还要把它放入到一个 list 当中是吧，这块很麻烦， come on 写一下。暴露到一个 list list 点儿 add 把这个第一个参数咱们给它传进来，然后再把它放入到这个分机器当中是吧，这块可能会抛错，咱们直接把这个异常给它抛出去。好吧，最后再把 htentd set 进来，这样是不是就可以了？最后执行 htd 的 post 这块也有可能是吧，有异常咱们直接给他抛出，最后得到一个返回的结果。


HT DP response 对吧，还是快速的先回顾一下这个 HTTP client 怎么用。首先你要创建一个 hct client 咱们直接用 hct client builder 去创建，然后创建一个 HC TT post 指定咱们这个处理订单的这个地址是吧，指定到这个 local host 8080 handorder 然后要给大家传入这个参数，参数都是以键字段的这种方式，给它先设置好内幕 value pair 先设置。


第一个是 order ID 是吧，如果你有多个，你这块就可以写多个内幕 value pair 了是吧。最后把这些内幕 value pair 都放入到这个 list 当中，最后把这个 list 再放入到这个 foam 整个表单当中是吧，这个几个步骤都比较繁琐，咱们还是要找到它的规律，就不会用错了。那么把这个 HTTP 设置好以后，把它放入到 HTTP post 当中。
最后执行这个 HTTP post 是吧，得到一个返回的结果。这个返回的结果咱们用 ND DU 挺 entity utils 给它处理一下 to string 是吧。 response.get entity 这样是不是就可以了？得到一个结果了是吧？如果这个结果的值是 success 也就是说咱们之前设定的这个值是吧，在这个处理订单接口返回的这个 success 如果它等于 success 咱们要更新这条消息的状态是吧。 payment message 然后 set 它的 status 等于一发送成功对吧？如果他不等于 success 是不是就？失败了，咱们要看一下它的失败的次数是吧。


payment message 然后 get failure count 咱们把这个值先给大家取出来，给他加 1 是吧。然后这个 filter count 咱们要看一下，看一下它是不是大于5。咱们规定如果超过五次的话，就把这个状态给它改成失败是吧，payment message set status 等于是吧，二就是失败。


最后再用那个 mapper 给它更新一下，在 primary key payment message 对吧。前面还是要把这个更新时间更新人给它设置一下 DAT date 引入一下，然后再设置一个更新人是吧。 update user 等于0，这个是系统更新，这样是不是就可以了？如果你的失败次数大于了5，我把这个消息的状态给它更新为失败，咱们下次定时任务再去运行的时候，就不会检索到这条消息了是吧，这个一个整体的逻辑应该是没有什么问题的对吧？最后咱们要在这个方法上加上定时任务的这个括号表达式 scheduler 的是吧，然后里边 cron 表达式咱们 10 秒钟执行一次。好吧，零杠10，然后四个星号一个问号，这个矿泉表达式就写好了。


咱们在运行这个项目之前，先去数据库当中把这个数据给它恢复到最初的状态。首先这个订单订单的状态咱们给它改成 0 是吧。然后再进入到 131 的数据库，这个订单的消息咱们先给它删除掉用户账户的金额，改成 1000 好吧，这样是不是数据就恢复完成了？然后咱们启动一下这个服务，好启动完成。


咱们执行一下这个支付的接口是吧。支付完成以后，用户的账户表会扣减 200 块钱，然后消息表当中会增加一条消息记录，然后定时任务扫描到这条消息给这个处理订单的这个接口发送通知是吧。处理订单的接口，处理完订单，然后返回一个 success 返回 success 以后，程序将这个消息的状态也给它进行更新，给它更新成发送成功是吧，整个流程就完成了闭环，咱们现在访问一下支付的链接。


好吧，推车支付结果变成了 0 是吧，咱们接下来等待着这个定时任务运行，现在报错了是吧，咱们停一下，看看报道什么。错这个地址咱们少写了一个冒号是吧，犯了一个低级的错误，咱们再运行一下。这个消息咱们已经进入到数据库了是吧，执行完成了，现在咱们就等待着这个定时任务运行。定时任务运行完以后，咱们会更新这条消息的状态是吧，这块是不是？咱们先停一下，这块是不是咱们也漏了？如果是成功的话，咱们也要进行这个 update 这块漏写了，咱们给它补上，然后起一下这个项目。
好，这项目已经启动成功了是吧，咱们看一下这个数据库当中的订单的状态，进入到 order 表，咱们刷新一下变成 1 了是吧，订单已经支付成功，然后咱们再刷新一下这个 message 表， message 表这个状态也变成了 1 是吧，发送成功。


那么下次这个定时任务再运行的时候是搜索不到这条记录的 so 看来咱们的这个基于本地消息表的分布式事务也已经成功的实现了。那么现在咱们再给他恢复一下，看看这个超过最大失败次数会不会改变这个消息的状态。咱们还是把项目先停一下，项目停一下，然后订单的状态给它改成零消息，咱们还是给它删除掉。用户的账户刷新一下800，这个咱们就先不改了一会再支付一下。咱们把这个程序给它改一下。在这个 order service 里边这块是处理订单状态的是吧，这块咱们直接抛出一个异常。好吧，时间抛出一个 one time exception 叫做系统异常。好吧，那么下边这些都执行不了了，咱们就直接给它注释掉，那再运行一下这个项目，这样的话咱们在调用 handle order 的时候是不是永远就得不到这个 success 这个字段了是吧，咱们再去浏览器当中访问一下这个支付的链接，支付成功是吧。然后看一下，金额减了二百块钱。
然后消息现在失败的次数还是 0 是吧，失败的次数并没有增加，咱们看看失败的次数咱们打一个，断点过来了是吧，看看失败的次数是0，然后count ， count 加加以后，这个失败次数变成了一对吧，然后 1 和 5 去进行比较，咱们这个失败的次数并没有更新回来是吧，咱们还是把这个项目给他停一下，这块要给他设置一下 set filter count 等于 failure count 对吧。


最后不管它是不是大于 5 次，都要进行数据库的更新，是不是咱们再启动一下项目，这块逻辑还是比较绕的是吧，咱们写程序的时候一定要多多的进行调试。好，这回咱们再在数据库当中看一下，刷新一下，别的 cos 已经变成 2 了是吧， status 还是 0 还是未发送？现在就变成了3。最后咱们会经过 50 秒的时间，经过 50 秒以后它会变成 2 是吧，我们再刷新一下。好，现在这个消息的状态变成2，说明这条消息是失败的。现在菲雷克是 6 是吧，六次执行了 6 次，然后他的状态变成失败。那么这一条的订单消息就需要进行人工的处理了。咱们看一下这个订单表里边的数据，订单表里边订单的支付状态还是未支付是吧，这条消息也已经失败了，需要进行人工的处理。
到这里，这个基于本地消息表的分布式事务是吧，这种解决方案就已经给大家完全的实现了，这里边咱们只不过是一个简易的实现是吧，其实里面还有很多的细节需要大家去好好的去琢磨。咱们再快速的回忆一下这种基于本地消息表的分布式事故的解决方案。其实这里边主要是分为三步是吧。一个是处理你的业务逻辑，然后把和你的当前的业务逻辑以外的这些事务的消息放在一张表当中对吧。另外一个数据库要提供数据操作的接口，要操作这个分开事故的这个这些表和你之前的那些表不在一个数据库当中的这些表的这么一个操作要提供一个接口，这是第二步是吧。


第三步是一个定时任务，它要读取消息表，然后调用这个操作的接口，操作的接口处理完这些操作要把成功和失败的状态返回给这个定时任务是吧。定时任务在拿到这些状态以后再去更新消息的状态。更新消息的状态以后，这个消息在定时任务下一次执行的时候就不会被读取了。也就是说这一条消息处理成功了。最后保证两个数据库的事物是一致的。就像咱们的例子当中，你支付的状态和你订单里边的这个状态最终是保持一致。这个就是基于本地消息表的分布式事务。好，谢谢大家的收看。下一节咱们给大家介绍基于 MQ 的这个分布式事务，谢谢大家。




