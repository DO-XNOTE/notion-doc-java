---
title: 3-6 【技术改造】电商系统集成Gateway - 网关层登录校验-2
---

# 3-6 【技术改造】电商系统集成Gateway - 网关层登录校验-2

[image](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/44b2433a-9c42-40a4-a47d-4ada20054bd1/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UX4KIAT3%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T225751Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIF0VF0Ph9aPgqPRRANzxW3wyPH0%2BXFrJByHUTEjTVWdZAiB%2F5SSYbqjq3wjESbKeWbAsA2t6HSxFOF%2FIAQ1lWyAEMyqIBAjG%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIM%2BBOBroUIKySOYRWpKtwDo2wLPr8bzGfYr5odDwH2mcBmn3xwlz9uCV3zeWQmr%2FU4tYmM%2FV%2Ft89l9NJ9f39Sp58mEEj9Bd%2FEUJW%2BBDdXQmIduduRnAM4mBHBUK7QH%2FFlG6mlV%2Fnn3UcQfx7E8WaJegOC1f9czJWfqDP2oru60EvdAzeXWUTjqMrGDH3LC0jGUQ8lkzIZlOFbxcs8fItaDhMevPwTefrlfx1K9lMpvb9JcHBIPWWNaUqpF5svhyKnYQLOlEH3JlWCJ68v1FfgpeIHn59h3kgEWKW2pNKS9udKAjfi2xc99iCkDxRRx9SVE8OngFu%2FvB1jGMq%2F5hoxfdo6KaI9EJpIyeDeAysy1c%2Bbn8nXZorLsIoFXMbRtCJFvth%2F3ITlO59a15%2Ft%2F9UfPa%2FognQqFFKcw5aWRpfPpseWD5a%2FlIjl1A8gxtvB6l2oErAiA4dmmSmoXuWjgQzy5ef5eHV4XCsYp4yqoZ0aoFjN4CJOJ%2FQ1pX4qkeucuSdOzExYMi%2Fnw%2BzVBEUmOQvd6Of0xyYC3lDQF3gY6i5rcdngv%2F2lYw5vSeF2DkgmgP2JZhtA1eiyxCAJ2e6k3viP1hAKVDL4JjPNC4QcfW2%2FImotM%2Be6zvTE4XsJLpZT%2B08hTlRdJcCWJQU2iW2owhrv%2F0gY6pgGzXlvv8FUCD%2F0DbcILenYM3IjsEBtG%2Fkq4CCa02e%2BtQRUnweFa28VZx4AjM9mR7yLge%2FI8d31sv4Ndnj8MfP5aa6O%2BNcSGQQmaRq0cfuzB1lGAodynegPDDvuOLLR8ffHoWosrNYkdwQVxFyXuMQF8PiUXW22ClYiXWh5ka4c4t%2BMC5AkTzcq4URLebY3c%2B%2BPFsPaxD9Yb6vW8PXKvmWQ1AOtf3AHu&X-Amz-Signature=76f87a12e64195c03720251bd3c4c1177b4861318646bd0e562f4a4c82a7f566&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

[image](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/277fe3ee-660c-4757-bcb2-aa272ea731cd/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UX4KIAT3%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T225751Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIF0VF0Ph9aPgqPRRANzxW3wyPH0%2BXFrJByHUTEjTVWdZAiB%2F5SSYbqjq3wjESbKeWbAsA2t6HSxFOF%2FIAQ1lWyAEMyqIBAjG%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIM%2BBOBroUIKySOYRWpKtwDo2wLPr8bzGfYr5odDwH2mcBmn3xwlz9uCV3zeWQmr%2FU4tYmM%2FV%2Ft89l9NJ9f39Sp58mEEj9Bd%2FEUJW%2BBDdXQmIduduRnAM4mBHBUK7QH%2FFlG6mlV%2Fnn3UcQfx7E8WaJegOC1f9czJWfqDP2oru60EvdAzeXWUTjqMrGDH3LC0jGUQ8lkzIZlOFbxcs8fItaDhMevPwTefrlfx1K9lMpvb9JcHBIPWWNaUqpF5svhyKnYQLOlEH3JlWCJ68v1FfgpeIHn59h3kgEWKW2pNKS9udKAjfi2xc99iCkDxRRx9SVE8OngFu%2FvB1jGMq%2F5hoxfdo6KaI9EJpIyeDeAysy1c%2Bbn8nXZorLsIoFXMbRtCJFvth%2F3ITlO59a15%2Ft%2F9UfPa%2FognQqFFKcw5aWRpfPpseWD5a%2FlIjl1A8gxtvB6l2oErAiA4dmmSmoXuWjgQzy5ef5eHV4XCsYp4yqoZ0aoFjN4CJOJ%2FQ1pX4qkeucuSdOzExYMi%2Fnw%2BzVBEUmOQvd6Of0xyYC3lDQF3gY6i5rcdngv%2F2lYw5vSeF2DkgmgP2JZhtA1eiyxCAJ2e6k3viP1hAKVDL4JjPNC4QcfW2%2FImotM%2Be6zvTE4XsJLpZT%2B08hTlRdJcCWJQU2iW2owhrv%2F0gY6pgGzXlvv8FUCD%2F0DbcILenYM3IjsEBtG%2Fkq4CCa02e%2BtQRUnweFa28VZx4AjM9mR7yLge%2FI8d31sv4Ndnj8MfP5aa6O%2BNcSGQQmaRq0cfuzB1lGAodynegPDDvuOLLR8ffHoWosrNYkdwQVxFyXuMQF8PiUXW22ClYiXWh5ka4c4t%2BMC5AkTzcq4URLebY3c%2B%2BPFsPaxD9Yb6vW8PXKvmWQ1AOtf3AHu&X-Amz-Signature=34be5e19ac66bf3a70aa04586af8c99f7b2d1fd5edce17a2528906ac6007933b&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

好，也就是说我这个 token 在每次签发了之后，那再过一天它就会过期了。所以我要把这个信息怎么样？前端 javascript 那同样我也把它选择添加在这个 header 当中，把它叫 token expiration time 然后把这个 time 给它直接返回一个 get time in many seconds 这样的一个对象。因为它是一个浪形，所以我们这后面跟一个字符串，把它强转成字符串了一些。

```java


// TODO 修改前段代码
    // 在前端页面里面拿到 Authorization , refresh-token 和 imooc-user-id
    // 前端每次请求服务，都把这几个参数带上
    private void addAuth2Header(HttpServletResponse response, Account token) {
        response.setHeader(AUTH_HEADER, token.getToken());
        response.setHeader(REFRESH_TOKEN_HEADER, token.getRefreshToken());
        response.setHeader(UID_HEADER, token.getUserId());

        Calendar expTime = Calendar.getInstance();
        expTime.add(Calendar.DAY_OF_MONTH, 1);
        response.setHeader("token-exp-time", expTime.getTimeInMillis() + "");

    }
```

[image](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/d1b23b86-a14a-4681-92bb-cc1956359ed1/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UX4KIAT3%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T225751Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIF0VF0Ph9aPgqPRRANzxW3wyPH0%2BXFrJByHUTEjTVWdZAiB%2F5SSYbqjq3wjESbKeWbAsA2t6HSxFOF%2FIAQ1lWyAEMyqIBAjG%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIM%2BBOBroUIKySOYRWpKtwDo2wLPr8bzGfYr5odDwH2mcBmn3xwlz9uCV3zeWQmr%2FU4tYmM%2FV%2Ft89l9NJ9f39Sp58mEEj9Bd%2FEUJW%2BBDdXQmIduduRnAM4mBHBUK7QH%2FFlG6mlV%2Fnn3UcQfx7E8WaJegOC1f9czJWfqDP2oru60EvdAzeXWUTjqMrGDH3LC0jGUQ8lkzIZlOFbxcs8fItaDhMevPwTefrlfx1K9lMpvb9JcHBIPWWNaUqpF5svhyKnYQLOlEH3JlWCJ68v1FfgpeIHn59h3kgEWKW2pNKS9udKAjfi2xc99iCkDxRRx9SVE8OngFu%2FvB1jGMq%2F5hoxfdo6KaI9EJpIyeDeAysy1c%2Bbn8nXZorLsIoFXMbRtCJFvth%2F3ITlO59a15%2Ft%2F9UfPa%2FognQqFFKcw5aWRpfPpseWD5a%2FlIjl1A8gxtvB6l2oErAiA4dmmSmoXuWjgQzy5ef5eHV4XCsYp4yqoZ0aoFjN4CJOJ%2FQ1pX4qkeucuSdOzExYMi%2Fnw%2BzVBEUmOQvd6Of0xyYC3lDQF3gY6i5rcdngv%2F2lYw5vSeF2DkgmgP2JZhtA1eiyxCAJ2e6k3viP1hAKVDL4JjPNC4QcfW2%2FImotM%2Be6zvTE4XsJLpZT%2B08hTlRdJcCWJQU2iW2owhrv%2F0gY6pgGzXlvv8FUCD%2F0DbcILenYM3IjsEBtG%2Fkq4CCa02e%2BtQRUnweFa28VZx4AjM9mR7yLge%2FI8d31sv4Ndnj8MfP5aa6O%2BNcSGQQmaRq0cfuzB1lGAodynegPDDvuOLLR8ffHoWosrNYkdwQVxFyXuMQF8PiUXW22ClYiXWh5ka4c4t%2BMC5AkTzcq4URLebY3c%2B%2BPFsPaxD9Yb6vW8PXKvmWQ1AOtf3AHu&X-Amz-Signature=c2f1f1aaf1fc6d3b904585dd898a0ae31de56c948feda2fc345edfbbefc4eefb&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

那这样做的目的是什么？我其实是想让前端感知到这个 token 还能存活多长时间。那我这里设置过期时间一天。那你临近过期的时候，咱前端服务就怎么样，可以调用 refresh token 使用当前老的 refresh token 来刷新，得到新的 token 以及新的 refresh token 那咱这个方法添加好了之后，我们接着再回到刚才的 login 方法里面往上走。在这。 OK 好，我们这里调用这个 login 方法，把 response 传入进去，同时我还要把这个 token 当中的 account 也给它传入进去。


好勒，那到这里我的 login 就已经完成了，接下来我要去处理另一个方法叫什么 logout 那你 login 了，你就生成了这些 token 同理，你捞杆的时候你要怎么办呢？要把它给删除掉对不对？那怎么删除呢？非常非常简单。我这个 log out 的第一步，我什么都不做，我直接过来就先调用 off service 把你给删掉。好，我用一个 auth response 来接收你的这个请求。


OK 那这个 delete 它需要构造一个什么参数呢？我们看到它有一个 account 那因此咱也要构造出这样一个对象怎么来构造？很简单，咱就直接声明一个 account 然后利用咱在上面加的 long book 的 build 方法，可以很方便的把它给使用 build 模式，把它给构造出来。


OK 那这里有这样几个参数，我都要去把它传入进去的一个是 token 另外一个 refresh token 最后一个是谁。 User id. OK 那 user ID 非常好找，直接在这个入参这里就能把它轻轻松松的拿到。剩下两个我采用怎么样的方式呢？我从 request 当中把它给它拿到。那这个 token 它的 request header 就是我们刚才声明的 of header 同样的下面的一个 refresh token 就是谁呢？就是咱这个 refresh token header 好 OK 构造好了 count 之后把它传入进去。


那接下来我怎么知道它成功失败呢？和前面 login 的过程我们做的方式是一样的，我们找到login ，把这一段判断给他 copy 一下，然后返回到 logout 好直接拿过来。但如果你最终返回的是成功，那么你继续往下走。但是如果返回失败，那我们就不好意思啦，就给你提示一个 token L 然后就中断这一个 log out 登出操作。


那 log in 和 log out 都已经创建完了，似乎看起来所有步骤都完成了，对不对？咱还漏了这样一步，哪一步呢？我们往下看。这里前端知道了过期时间，它是不是需要去调用网关层来刷新自己的token ，所以我们还要再绕回到网关层里面，给他创建一个路由规则。 OK 我们来看这个路由规则是给谁创建的，是给咱的 of the service 创建的，它的名称叫 foodie of service 然后它的路径是什么呢？我们到上面来看一下，那它的路径就在咱的奥斯维服务里面，我们打开它的 API 好看一下这个 of service ，它的 URL 是以 of service 开头，然后调用了这个 refresh 方法。好，我们把这个给它 copy 过来，把这个 header 然后再回到咱的这个路由配置这里，我们把它的 pass 给它更正一下。


前面记得一个斜杠，后面 of service 再一个斜杠跟谁跟 refresh 那为什么其他的几个接口不用暴露出来，因为我们其他几个接口对 security 要求非常高。对不对？我们只允许在应用内部咱的授信的这些应用内部来调用，我不允许把它暴露给外部。那在这几个接口定义完了之后，接下来就可以去挨个的启动服务了。我们按照顺序先启动了有瑞卡。有瑞卡，我们已经在外面的命令行里面给它启动起来了。


那接下来第二个启动谁启动咱的 config server 为什么？因为 user 服务它是依赖于 config server 来拉取一些注册信息的，它有配置信息，需要从 github 当中把它给拉下来。所以咱这里第二步要记得把 configuration survey 给它打开。


那第三个开启的应用是谁？是咱的 of service 做权限验证的，我们也把它启动起来。按照这个依赖的顺序，咱的用户微服务模块是依赖于权限校验 token 生成的这个 auth service 所以咱就先启动 auth service 然后接下来启动好了吗？好了，那这里紧接着启动 user application 好，我们这里看到用户微服务已经启动起来了，接下来网关层给它打开。


好。那么在网关层启动的同时，我们现在转战到 postman 来尝试发起一个注册和登录的操作。我们看到网关层起来了。好，我们转战到postman ，往下拉。好拉到这个网关层这里，咱先尝试通过网关层调用用户微服务来创建一个账号。那这个创号的用户名和密码我给它起名就叫半仙。 OK 那我们走起了一二三走，你第一次调用可能时间会稍微长一点。好，我们看到经过两秒钟之后，他返回了一个。 OK 好，那我们到后台到 data grade 里面去尝试 select 星 from users 看刚才这个用户有没有创建出来。那这里同学们看到吗？这里有一个用 username 为半仙的用户，证明他已经创建出来了，那剩下的事儿就容易了，我们接着回到 postman 尝试去给她做一个登录。那这个登录依然是通过网关层来进行，他发送到 local host 20,004 passport locking 好，那他的用户名密码就是半仙，我们走，你 321 走。 OK 很快返回了，我们看他的请求是200。那说明已经登录成功了。


登录成功还没完，我们看一下这个 header 有没有把咱想要的信息添加进去。好，麦格看一下 authorization 对不对？在这里咱的用户的 token gwt token 令牌在这。那 refresh token 也在这里找到了。那剩下最后一个咱的 user ID 在哪？ IMock 和 user ID 好在它上面这三个需要的信息我们都已经拿全了。接下来我们就要用这些信息去调用一下用户的地址模块，看一看它能否通过用户的登录检测。好，那我们接下来转移到 postman 的另外一个方法，我这里尝试去发起一个 address list 的方法调用。但是我需要把这个 authorization 给它清空，我这时候来发起一个调用，看它会返回什么走。你看它显示什么 401 unauthorizedunauthorized 什么意思啊？我的用户权限检测是不是没有通过，所以他这里报出了这样一个错误。


那接下来我们怎么样？我们尝试的把这个 authorization 给它添加进去。好，走到刚才 login 的结果这里，我们把这一串 header 非常长，同学们不要 copy 漏了，把它全部 copy 下来，然后复制粘贴到这个 header authorization header 当中。注意这后面不要留一些空格，我们把这个字符串紧凑的放到这里啊，啊让它排列的紧致一些。


好，那接下来点击 send 看看会有什么效果。 OK 那这里已经看到它返回了一个 message 是什么？是？ OK status 是 200 说明，这个接口已经调通了，并且咱的用户登录检测也已经完美生效了。 OK 同学们，咱经过这四小节的电商项目改造，漫漫长征路，终于把这一章节给它结束掉了。那我们简单的回顾一下这四小节都做了什么内容。首先我们在第一个小节里创建了 gateway 这样一个组件，然后创建了一些简单的路由规则，在它的 configuration 那第二小节里我们使用了基于 Redis 的网关层限流，把限流功能集成到了咱的 gateway 当中。那其实这个网关层限流表面上是使用的 Redis 但是实际它背后它的限流脚本是使用的，谁是使用的 Lua 脚本。不过这个 Lua 脚本可不是老师写的，是咱的这个 git 位框架内置的一个 Lua 限流脚本。


OK 那在后面的两个小街里，我们分别去创建了一个 authorization service 这个微服务。并且把这个微服务集成到了咱的网关层以及我们的用户微服务模块当中的登录还有登出操作。这样一来，我们就在登录的过程中请求 off service 生成一个用户的指定 token 然后在网关层利用一个 off filter 来对那些需要做登录检查的请求地址做过滤。


那这就是本章 gateway 章节的全部内容了。同学们学到现在，学完了 gateway 基本上这个微服务的神功已经练到了七八成的火候了。下一周我们就趁热打铁，把那剩下的两成功力一鼓作气修炼干净，再到神功大成的那天，立马跳槽出门，斩获 offer 无数。好同学们，那我们在下一周的 slow 链路追踪章节里再见。







