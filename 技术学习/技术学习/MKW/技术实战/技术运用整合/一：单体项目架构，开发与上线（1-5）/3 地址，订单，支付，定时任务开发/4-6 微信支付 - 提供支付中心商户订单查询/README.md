---
title: 4-6 微信支付 - 提供支付中心商户订单查询
---

# 4-6 微信支付 - 提供支付中心商户订单查询

[image](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/8943d4c9-56a4-4283-ab31-27dca77527f3/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WGSDQZZJ%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T224712Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCBEkjVjzWNqeLWdSdg5Y6RUJJ0OE7ostYUqRPTNR%2FCFQIgYDailfOpY7IaTMT4jBaNvqUVggAzRf%2BTNYe9Ed2I7ycqiAQIxv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDHOJxWX4zGXiyvyLYyrcA%2FF2d0%2BelDA4XropmOnf3lQhyuobAQhlVPhldujfgKdzsFPbbZTZ6Nc%2FEPGFAeOxlcyrL6EFxKU5TqnD7t%2B3bvS7NNMjYTknS%2BFX8n5eytPUrR2fI%2B5xaK75pyRJ2mu5TXQbsgPiSxMLaQJ3qTOfI0zGbwmXM%2B2FtjhlvC330lQs1xyFM2h3ibUQ1QDbcl2Qdnwd6Y5B9fDwMchkjbTFbzUDaRjPtsS%2BXoJPiUDKtKjHYm70ayjkTw%2B%2FUC0wjoS3BD8E9AVZhkc9LIxPdkWkvFbMlOdtTMLsCAPlElIG2K5P11mnGuBKsepkE89w%2Fav3VhSzuTa9zjd7S0%2F0p74tIP98Dd6m%2FxHLASBThWRSC5O2RRKFDS2K1DKtKLTjT6rLnsZ0usMSkc6tVPt3ZiybM4KeCvq7F7HNtBzEZ%2BVF31NoacwXlKPWDFDsiC%2FCMCoKTkI9A5%2FY6P2Rgo0GyJBJvvs9vyPmfVs%2FJwRBptFSgRGFU3PMWW3zlDDEm2Xa9XiPwtl3MiD5fIwrkqJD65RjrIfOhDrw872ls5YefuBbUP7Bs%2F1Lm01kxMbkiEx%2BUqageTehU%2Bhbh5Ui9oIWVL1OvP1k%2FrXldt6swMBt8TxKxhzsDemh9WbN%2B4DC3FHzMLG6%2F9IGOqUBeF2LS1uZBSaL%2F9H7akDu9zJSHDHtUKbYM7dk0CHuaY%2Bnqh8PeWNpw%2FSO%2F3nmlsOd7aWbnCLTcIaOU2yFiPdAoZHC515TmN4jWIqKiHA%2BMdzWfaNL42Mo93qJBsRgDpf9%2BWTWGhLIJgTGpuSR9bsJId4K1SV0LsxS8EyoDSOT5r305ePUymtDXgaCVk%2B8augNNQ%2FK%2FS14UTiFQFVsf0YRjMjS2vgR&X-Amz-Signature=45917fdb1b942cf0bfa0d318b4cae46b1bd471ec67f0e444c85d197e2705c9d7&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

上一节课我们是在支付中心里面成功的插入了一条数据，这个就是我们 chant 欧的商户订单，是由天天吃货平台传递过来的。在这里面其实我现在测试它成功与否，有没有正确的插入到数据库里面，是直接通过打开云端的服务器里面去进行查询的，大家是权限的，没有这个权限，该怎么去测试，怎么去看订单有没有成功的插入。在这里来看一下。


其实我在生产库里面，在生产环境里面是新增了一个方法，这个方法主要是可以提供给大家去进行查询的，用于查询商户订单的信息的。OK，这就是他的一个请求的路由的地址 get payment center or the info，去通过查询，如果有对应的一个信息查询出来是 OK 的，没有问题就代表相应的数据是正确的。插入到数据库里面去的。 OK 接口如何去测试使用？很简单，可以通过 post man 去进行一个测试来打开看一下。


我们先把路由地址拷贝，打开 post man 在这里面。其实地址肯定是不对的，所以我们要先把调用的请求方法先写过来了。以后我们是需要把咱们的一个支付中心的 URL 写过来。 URL 其实我们在项目里面是有的，在这里面我们是上一节写了一个 payment UL 直接拷贝过来的。支付中心的调用地址其实就是一直到这里，这就是它的一个调用地址。 payment 加上下一个，这就是它的一个路由的地址，在我们直接把这一段内容直接拷贝到payment，拷贝一下贴到 post 面，贴过来，后面加一个斜杠。 OK 来看一下，比较的长，写了以后，现在我们还是需要去传入相应的参数的。参数主要是这两个来看一下。其中一个就是 machant order ID，就是我们商户添之后的一个订单ID，以及是我们的复盘方的一个用户ID。把这两个拷贝贴到我们的postman。好。再来一个是 user ID，总共是这两个参数。这两个参数写过来了以后，不要忘记是这两个参数，可以拼接在我们的请求后方，它是请求参数到数据库里面去搜一下。数据库里面我们就只要找自己的库了，找自己的库 OS 里面其实对应的就是这两个ID，这个是订单ID，这个是用户ID，拷贝一下，用户 ID 贴到这里，再来一个，再把订单 ID 拷贝一下贴到这里。OK，好。这些参数都有了，以后还不要忘记，在 head 里面也是需要去添加相应的内容的。比方在这里有一个key，这个 key 就是我们的一个，贴一下m，可 user ID 拷贝一下，贴过来，它的值是m，可下一个是password，也是 m k。


OK。这两项写好以后，现在我们就可以发起一个请求了。点击 send 请求一下，可以看到现在我们是请求成功，我把拉起来请求成功。现在状态是200。相应的信息其实全部都是在这里，这些内容其实就是在我们的一个数据库里面的内容，这些内容都是和生产库里面这一端这张表的最后一条数据是一模一样的，可以看到是 230 块钱，是 230 块钱。OK，大家就可以通过这种方式去测试一下你自己的一个商户订单有没有在我们的支付中心成功的去创建。另外在这边我们附带议题，现在要去支付它的金额是 230 块钱，我们在测试的时候肯定不可能会这么去支付的。所以在我们的代码里面有一个地方是需要去进行修改的。


在这个地方在这里有一个 Macant orders fill 对吧？在这里我们加一下点set，它有一个 set amount， amount 我们其实在接收的时候是需要去判断它必须要大于，也至少是一分钱，如果小于一分钱是0，或者你不填，肯定是不能够去进行支付的。所以这一点是一定要去注意的。在这里为了方便测试，我们在这边直接写一个 1 就可以了。写一下为了方便测试购买，所有的支付金额都统一改为 1 分钱。OK，这样子可以再次去测试。在我们的页面打开以后，它的一个金额就是一分钱了，OK。

