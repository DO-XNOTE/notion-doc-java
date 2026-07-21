---
title: 3-17 用户退出登录清空cookie
---

# 3-17 用户退出登录清空cookie

[image](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/72066211-341b-480c-8205-bf8dbcee39e7/SCR-20240816-uiuo.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663XOD2UBL%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T224634Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDAk56MbiKxn1bMQmqUlxxYvSaC5T8d4BPLHyjBX6VJzwIhAIz7ewfmmJORfrtVBvfThQemef9gmGGH9Fzdic7PZ2X4KogECMb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1Igwp%2BblLBOBKvcsJ%2BOQq3APZBh88j4NQ0nWnJHMr0ddY5aqMj9KvfRLkI5a9QZl045e5hUA06abg2VbhC6NtiZOcodetU%2BHQHv2Us7g4kyaoOGN2yU8u5wvRfHzcHxcBDcTnUkE%2FlAj4dxbKMA8W%2BZaoTIpp56ynbLR0WFzd3q7dqGXs8W8qDUeJ4%2FBUhtrym%2FqpvryFHlCJI%2BUPAO1Ap%2B74lB4GmiR3Wk1w4YY0BU7y2X6AZweFB08zNhNVV9Oj1nYzEaUcRYyE8MwNr21%2F%2Bde1WBxDDm5lWBQaWcn8sxpXm01PeuAZ5LDRMojEPnqw%2B6Rbnru5xw3iE7r3wd7WTl0Lzm4SsDEvzoDu0WtARteKNdEBxXHcxu93H7lo5iVzkHfW4m13EOTF2xbwYk%2FV%2B%2FvVojEWVMT4ckGS%2FSP1XJiKJzDW13o5sGuxS2Uq7%2BxWjC9yjGJnr5bqIGXGdAdGwl0fl1Qz16LbQAt13PcTROYVEmttMvvUxuFwCL1bN%2BLkJiVVqPdXLWgzRCViSEyOqc4ntyMMo0M5Nxn5i2SKczUe3i%2B2sgJcnZACU4J%2FDL%2BM1ZMcSqNpKR9gZy%2BrbE8IzU9ibfglsi%2FVmN0NpMnPPWTsDXHuARIpF9otW3m65Niqoxdck93l5iTTd6DhczCKuv%2FSBjqkASPBT0TZlIgLPZb14jaJbcb8bj%2FG8M8oGAYh24hH6T2me23US3lHZnLo%2Fs7bPzvCdaoBbPHEegYbkYSoJacn64XKdvCbVEAXWg13fHxwwz14xHevygueN1ksY4fYruyE1q7g0FAl61RsUg4DMLE%2FXwBD9Fn1aWfyZLC7EGIosW2BBYbO4TPPYxRkJFlrSld4bBrmqSiEg3oNP89GTmKlmr5gu0A8&X-Amz-Signature=c12778dab07c50a2380fded5646650d35ffad84fc274ae7deed6156404f1d541&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

登录和注册我们都做完了以后，我们要在首页这个地方看一下，我们是需要去点击退出登录，要把功能给实现一下这个功能，我们是需要去发送一个请求到后端清除相应的用户的信息。可以先来看一下我们的前端，前端打开 VS code 来看一下。


找到首页index，点HTML，在这个页面里面会有一个方法，叫做 log out，搜一下，在这里会有一个 logo out，这个 logo out 方法主要就是用于做用户的退出登录的。我们来看一下。在这里面它会发送一个请求。这请求比较简单，是在 passport controller 里面定义了一个 log out 这个方法，这是它的路由。随后通过一个请求参数 user ID 传递到后端，后端接收到以后就可以去做一个相应的处理。在退出登录成功以后，它的状态是200，随后就会回跳到首页。OK，好，我们就可以到咱们的后端把这个方法实现一下。在它的最下方，我们可以来定义一个方法 public imock JSON result log out。首先我们在它的上方加上注解，主要是把直接拷贝一下来看一下。直接拷贝到这里，这里应该是使用 log out，这个是 swag two。写一下，这个是用户退出登录拷贝一下。好，它的一个 HTTP method。我们就直接使用 post 就可以了。


对应是 post mapping，是需要去传入一个用户的 ID 的。写一下request，这是它的一个注解，叫做 request Tom。定义一个 string user ID，如果退出成功，直接就来一个 return imock 杰森result，点OK，直接返回一个 OK 就可以了。我们不需要去返回其他的一些数据。现在其实在我们的后端并没有使用到session，这个会话我们没有使用到。如果是在曾经的 JS p 时代，在这个里面一旦用户要做退出，其实就应该要把 session 里面相应的用户会话数据都要去清空。在这里我们就不需要去做。在咱们的项目里面，其实我们使用到这是一个cookie，所以在用户退出以后，相应的 cookie 信息你是需要去清除的。


OK，因为你如果不去清除，如果你的电脑被别人登录，被别人使用相应的你的一些数据可能就会被别人拿到，虽然是加密的，总归也会有一些不放心。所以在这里我们要去清除用户相关信息的cookie。在这里我们又会用到 cookie 与跳丝，在这个后方我们就相应的也要去加上一个 request 和response，加过来。


好，OK。通过 cookie 有 tells 点，里面有一个方法叫做 delete cookie， request 和response，你是需要去写进来的。另外 cookie 的 name 名称叫什么？我们在前方在这里是定义的叫做 user cookie 的名称。所以只要写到这里这样子，其实用户相关的一个信息 cookie 就会在我们的前端被清除掉了。这一点是需要去注意的。其实如果我们在后方向整合了分布式绘画，以及是一个购物车，在这个地方我们也应该要去做一个清除的。我们其实可以先写好一个Todo，比方用户退出登录需要清空购物车，我们后面会用到，会回过头来再说的，因为还有是在分布式会话中需要清除用户数据。OK，这两个我们会在后面都会去实现的。现在我们就比较简单，直接通过 cookie 去删除用户的数据就可以了。


我们来重新的启动一下，启动之前我们可以回到咱们的service，之前我们在 service 里面其实加上了 three 的sleep，把我们都清掉，不然我们在测试的时候会比较慢的。好，重新的 install 一下。好， install 成功，我们再重启服务器，好，启动成功，回到咱们的页面，在咱们的页面里面刷新一下。现在其实是登录的一个状态。在这里面其实是有用户的一个昵称，以及是用户的头像都有。现在我们在这里退出登录。我们点击点一下以后你会发现跳转是比较快的。现在其实我们的用户头像就变成了没有了。另外这个时候的一个欢迎某某这个昵称在这里其实也已经是消失了，说明其实我们的 cookie 信息就已经是被清除了。我们可以展开来看一下我们的cookie。在这里面目前我们的 user 其实它没有值的被清空了，OK，现在我们就已经是初步的做好了第一阶段的时候的一个用户退出功能了，OK。


