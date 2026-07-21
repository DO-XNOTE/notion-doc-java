---
title: 4-5 微信支付 - 向支付中心发送商户订单
---

# 4-5 微信支付 - 向支付中心发送商户订单

[image](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/fe06cb15-67a7-4e65-b9cb-f194e2368943/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YKGHZ3JF%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T224711Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIHolzmV7PyDvkbKklRKV1i5WuXZnpdpVrj8Qq0gnBBfDAiEApCRRaV9O%2BuwGZuUohO%2BBqfA8fI%2Fu3rFnJYtLGnIMty0qiAQIxv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDEIwTH9RkrmshCFLJSrcA%2FZlMatUs8xqrMErYt1j93jyZcU8NQdX96MIlyPBJ6lN22wvRiRrMecEjehwQ0EtgXj6VkyihtjpLTaKBYWOHgqJ2G5UodSVq%2F5KoaIs7Sd9jCdoXvPN%2FCW2aYLLAdq5RaeHUPIOWSa4uLH%2Fzn%2F106%2BtoF19fKuv%2Bg%2FMfkz7IxsmHxHzXVMYhrVMNvcckGZfhRxlRRLgrCb4bN1nhnoUHN3rcA2pVKTMtC6WPZnp9KRpdnJh4ttZ8aiz5q8pMWP66WqOhcl5Wv1N%2F6A2pBAMMzdn1loVeFOQyjj55nj%2Bb5qsw2CGUzwwTGQ%2FpY8DFfYeCklRspcNIlyzPPtsOwV7LQdNvpbn8Uw8BA4g5XKtsUtcKeT1KoDhikiiG%2FjbneJ17CcMZkOL8VNsKe5639IWEMAF7I%2BEdr%2F457BXMjm7sRF1j0MOzYtYjLC4H7NmmdO2N3CyfS4tS%2Fl43tSOhK6QfOwXgONvYQiK761%2Fm6zm6nY29A7k7BBUm9tubhqDZ28Oi5amyasXFfPEnUxGjNoxq65OjP9Z6WKYIeq2FdUs%2BY5tm4dW3b78wk4pm9DsrycvzIZMlemSq4LsmzDCE9C7ofiIaUKeRmF4x5yqzRYbs%2BMt4%2F9g6BNXJkguFRMlMIq6%2F9IGOqUB%2F8fVoaXAxq3k0Wd0hDBeFADwUEbEMTO9medw0E4i5tMz6XmgdUjGMtBRlEWbHmkNFvkboxzCbuLPfy67dDep%2Fm09HNWgeGIefZSoyLcw2zoN%2FEyaNEerk18zVVXJ%2FpW1wSYelZ4C24jVhz%2F8R2dRDB8TpHSrnCz5%2FvlBc17RsPyjhGrVg5mOltWsQxuehI4MgtzaY8gSDegiT1hxayGysyfJBMz1&X-Amz-Signature=da4b2c32b7464fc7b51102cc8acbb6aa2a27c8358c1e50e62d731b0c687d04b4&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

上节课我们是构建了一个商户订单，这个是用于去传递给支付中心。好，现在我们要把要传给支付中心，应该怎么去传？我们可以看到，在我们支付中心里面，其实它本身用于去接收订单信息，它自己也是一个 rest 风格的接口。所以在我们自己的项目里面，在这一端我们也可以去构建一个 rest 请求，对吧？构建完毕以后，直接把对象传过去，以后对方接收处理完毕以后就 OK 了。所以我们只要去做这样的步骤就可以了。


**如何去调用另外一个系统？在我们 Java 的代码里面去发起一个 rest 请求，是有多种方式，可以使用 http 的方式，也可以去使用 spring 所提供的一个 rest template，由他去提供一个 rest 请求的支持**，我们可以来看一下。在这里我们可以来写一个。我们先把定义好，最后来看一下。它有一个 rest template。其实 rest template 它在 spring MVC 里面就有了。


我相信大家如果使用过的同学应该会有点熟悉，但是如果你没有使用过也没有关系，因为它使用起来也并不是很难。它其实使用的时候和前端发起的请求风格也是类似的，可以构建headers，也可以去配置一些相应的参数，都是没有问题的。在这边注入了以后要去使用，其实还并不能够去使用。


我们还要去做一个配置，让我们的容器去扫描到。在这里我们来创建一个配置项，我们创建以后取一个名字叫做 web n v c config，在这里面做一个配置。既然是配置，所以第一个我们要加上一个注解configuration。随后在这里面我们要去为我们的 rest template 去处理一下，把它当做一个bin，让我们的容器去怎么了。写一个bin，写一个 public rest template。 rest template 在这里面怎么去做？传入一个参数，这个参数叫做 rest template。builder，在这边我们只需要 return 一下就可以了。 return 一个 builder 点build，也就是构建一个 rest template。这样子在我们的容器里面我们就可以去使用 rest template 了。OK，好，我们在这边已经是写了，写了以后在这个地方就可以去发起请求了，我们把订单我们拿过来放到这里。第一步下面就不需要有其他的东西了。有一个 SOT 注释掉。


rest template，我们应该如何去使用？首先我们在传输一个参数的时候，现在我们传的是一个对象。虽然是对象，但是我们应该要以一个 Jason 的形式去进行处理。所以我们首先一个要构建 HTTP 的head，把这个给构建一下，取个名字叫做海德斯。在这边可以直接把它给 new 出来。


new 了以后我们要去设置一下它的传输的数据类型。它有一个点 set content type。在 type 里面我们应该要放一些什么东西来看一下。它有一个参数叫做 media type。在 media type 里面，其实它会有很多的一些类型，比方我们可以来搜一下 a p、 l i 来放大看一下。其实在这里面有很多的一些类型，每一个类型都会对应一个相应的数据类型。其实像比较熟悉这是 form 形式的，这个是一个 JSON 形式的，等等都有。OK，对于我们来讲，我们就直接使用一个使用 application JSON 就可以了。把拷贝一下贴到这里，使用 media type 点 application JSON，这样子传输的数据类型我们就已经是设置好了。


设置好了以后，其实还有一个内容我们也是需要去设置的。在我们之前其实也说了要去调研，我们支付中心就需要联系一下老师，要提供一下相应的一个账号，老师会提供给大家，我们之前是说过的，所以这两个参数在 headers 里面是必须要去传的。OK，要写一下。在这里有一个点at，这个也是一个键值队对吧？第一个是 m user ID，它的值是 m k，好，OK，这是第一项，第二项是password， password 对应的其实也是一个m。OK，好。这样子。其实我们的一个海德斯就已经是设置好了。海德斯设置好了以后，下面我们就要去发起一个相应的请求了。请求一下要使用 rest template。在这里点有一个 post 来看一下，因为我们在发起请求，对方是以一个 post 形式去接收。


在这边可以看到，其实会有 3 种，有一个 for object， for entity，还有是 for location，在这里我们会使用一个entity，它是一个对象对吧？使用在这里会有一个 URL 的地址，这个 URL 地址它其实就是我们的一个支付中心，你要去调用的地址。


支付中心调用的地址是多少？在这里我们可以先来写一下，我直接拷贝过来贴给大家。这是支付中心的调用地址，这个是目前部署在生产环境上的一个项目，其实就是一个 payment 支付中心，它的路由地址对应的就是 payment 下的一个create。唱子欧的来看一下我们的源码就这个 payment 下的一个 create materials order。


OK，在这里我们地址写好了以后，其实我们就可以在咱们的 Ctrl 里面去做一个设置，也就是 UI 去设置一下。好，设置好了以后，下一个会有一个request，一个请求。这个请求其实是一个对象，就是我们的 post for entity。这个对象我们如何去进行构建？其实我们的一个 request 要把我们的 header 以及是我们的一个订单的信息给传过去。如何去构建 request 其实就是一个 HTTP entity。写一下entity，我们传输过去的一个对象类型是一个 account order feel，所以直接写过来，定义为entity。在这边我们直接可以把它给 new 出来， new 了以后它会有一个body， body 就是我们的对象。


写过来。这个是小写的，注意一下不是大写的，在它的后方。因为我们是需要携带上海德斯的，所以它的构造函数里面，其实它还会有一个head，把 head 给写进去，这样子我们的 entity 就已经是构建好了，换一行吧。好，随后我们在 post for entity 里面，我们可以去加上一个entity。好，随后它还会有一个类型。我们返回过来的类型是什么？其实我们返回过来的类型，它本身应该是一个 IMOCK result，所以我们在直接写上一个 IMOCK just result 点 class 就可以了。它是返回的类型。在这边我们要去接受该怎么去接受。我们接受的时候其实并不是一个 m 可接受lot，这个只是它返回过来的其中数据包装过后的一个对象，但是我们真正要去获取的时候，它会由另外的一个 response entity 去获取的。


写一下约 boss entity 在这里。OK。在这里面我们就需要去写好一个 imock just result 传给这里面，作为它的一个泛型，也就是它的类型。写一下，这是一个 response entity，换行一下，参数也都换好。好。OK。当我们拿到了一个 response entity 了以后，随后我们就可以去获得 entity 里面的一些内容。主要的内容来获取一下。通过他点 get body，这个 body 其实就是我们返回过来的 m k just result 了。


OK，好在前面我们定义并且接受一下，我们就可以写一个 payment result。拿到了杰森 result 之后，我们要去做一个判断，我们要去判断它的状态，点 get status 是不是200，如果它不等于200，说明我们创建是有问题的。来看一下。看一下我们的支付中心，在这里必须要返回200，如果是返回200，就是商户订单创建成功。如果一旦发生了异常，或者我们数据库的记录他没有去进行插入，相应的它都会返回一个error，都是一个错误的状态。所以在我们的一个调用方。在这里我们必须要去判断它的一个状态是不是200，如果不等于200，我们就可以 return imock just result 点 error message 直接可以提示支付中心订单创建失败，请联系管理员。


OK，好，这样子。其实我们在这一整个第三点向支付中心发送订单，保存整个商户订单代码，我们就已经是写好了。切好了以后，接下来其实我们应该要去测试一下。测试的目的主要是看一下我们的一整块商户订单数据有没有成功的保存到数据库里面去。OK，所以我们来一起测试一下。测试。我们在我们要去重新的 install 一下。


好， install 成功再来重启一下服务器。


好，服务器是启动成功了，启动成功以后到我们的前端，现在前端我们从头来一次。我们退回到之前的一个结算页面，刷新一下。在结算页面里面我们选择微信支付，在这边我们就可以再次的提交订单了。我们先把一些订单数据先去清空一下，这个是商户订单，我们先清除一下，这些都是我以前的一些测试记录，先清空以后在我们这里面就可以去发起一个测试请求，主要来看一下我们的商户订单有没有成功的。保存好来到我们的一个前端页面，好点击订单提交，点击一下，这个时候可以看到我们页面发生了一个跳转。页面发生跳转了以后，你会发现这个时候我们的一个微信的支付二维码已经是有了，并且在这里也会有一个支付的金额是 230 块钱，这都是没有问题的。但是在这里我们先不去做这样的一个操作，我们先不去做支付，因为相关的业务我们还没有讲到。现在我们主要是要来看一下在我们支付中心里面的一个订单有没有生成，在这里刷新一下，你会发现没有，这是为什么？因为这个是在我们本地的支付中心的，一个订单的数据库是在我们本地的，我们现在在调用的时候，其实是调用的云端的一个支付中心，所以我们应该要去看一下在云端支付中心里面的一个订单数据有没有成功的。


生成OK，云端在这里天天吃货生产，双击打开看一下，有一个orders，双击一下，在这里我们来看一下。其实这一条记录就已经是生成了，我们可以来看一下。在这里是这一条订单记录，它所对应的一个 merchant order ID，我们可以来搜一下，拷贝一下。我们到自己的项目里面来自己的项目，找到我们自己的订单，双击一下刷新搜一下可以看到，其实就是这一条订单数据。这一条订单数据目前已经在我们的生产库里面，对应的已经是生成了。这边的价格是 230 块钱。现在的一个 pay status 是10。另外它还对应有一个 return while，这个就是在支付成功以后，由支付中心在调用。我们的天天吃货的后台会通知到你，这笔订单支付成功了，你是需要去把它的状态改成支付成功。OK，好，现在其实我们的一个商户订单，我们就已经是成功的，在支付中心可以去生成了。OK。

