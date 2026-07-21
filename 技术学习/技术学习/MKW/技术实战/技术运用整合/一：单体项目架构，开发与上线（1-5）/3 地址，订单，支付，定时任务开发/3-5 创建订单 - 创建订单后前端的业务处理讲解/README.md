---
title: 3-5 创建订单 - 创建订单后前端的业务处理讲解
---

# 3-5 创建订单 - 创建订单后前端的业务处理讲解

[image](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/fd5f80c1-56a1-40cc-9a8c-6901961f3478/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664MFB3UBB%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T224706Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDXhOmSHO1EIYs46%2BzZ%2BD2T0HoMXwUT2qip6S%2F%2B6Nb77gIhAIWOGiCDoEIhmuTVJlfXtCshPadstEMLalOMYx4wGGv7KogECMb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgwbPOnadY7In6d0EUEq3ANr%2BDA88vz2aAb3C3Q7NIgxiAAuMMp4LkLdT4Z5sGTXcMTpqooC98VSAc3nfYcaka17jbXM5HkjxwQ1kljO0ALxxWXI%2BBhTjBudIDfKqM%2Bl%2BKAs1X%2FscjT7xHCJOQtb9LuBjsF%2FBOx6LazEKziZdhcucc06dixqUlbiE7skzqcmtw56NbrpIEbrAWfAR%2FFUH8TO85OStvLhtJAm1pr1jmJkRPQcpb76lSYSbUBYF24QBA016Y4B5n4OrFaoU82uMjKT4WFkSfvu7u1zT7MSybi1SoBvOzeehsX%2FsDzgHM5uVW3XSqeeeIrV%2F0oYbmRHdafv%2Bg03WVLbupAd7eDnp%2F7ePGrC1fg6jQAHjhmPSFiMx1sAelC5R2SNT%2F%2F7qjSuWef%2FomSy46Sc%2FXr7bu%2BIJ3011uVYhqcyHMdoaYH40gfrXidTWrHbCBOy6WeEAMS%2FrqjEWO1sAHxyMguAK7PS0jlf78%2FSOjbAE%2BLvv4K7DB5qvoIw6J8VZuPiG%2FQRp3GPeYH7mHYWZ1oRRGffSFZBmT5tgQUnKVa39hk%2Brlk0gH0YKDhELbAZ2yFJZnnXRBupOI3apkaTwhSS3cV%2FBrwyiWYhhwO8H2V3uOo4EpRB%2FAp6DkL%2FZ1cxgE2MXKQZ1zCLuv%2FSBjqkAa3DkJWly3QP9kBBlArAfJubtCsBSxAOHfBuKVxISmxnPEI8p00CJgocfHsrZV0HUTMsB80%2F1JV367O%2FWt56oZLsKZTQpRFIV9oJHUDGrvTOFv8IO4SjkJiskkztBVEfmUfQ3pHbbmeJJ8FMea9a4Z6VpYV8BN%2F%2BnH2DGjTHPjiOpaDv0KeLgu6qwlTSmQ7r7q%2BvDIZz1T9xvXNswOc1DgVTBafg&X-Amz-Signature=a4601fdf0e9d0b4e99011b64fd49344e1ad8484f534a2fa36aca01e0378d989e&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

上一节我们就把创建订单的 service 我们就已经是写完了。好，随后我们来看一下在这里。第二点，在订单创建以后，应该要移除购物车中已经结算，也就是已经提交的一些商品。这个其实是什么意思？我们在这里可以这样子来写一下。比方我们现在在购物车里面有几个商品，有1001

[image](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/0c51d82e-806d-4661-ba96-fa6ac5bf3e5a/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664MFB3UBB%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T224706Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDXhOmSHO1EIYs46%2BzZ%2BD2T0HoMXwUT2qip6S%2F%2B6Nb77gIhAIWOGiCDoEIhmuTVJlfXtCshPadstEMLalOMYx4wGGv7KogECMb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgwbPOnadY7In6d0EUEq3ANr%2BDA88vz2aAb3C3Q7NIgxiAAuMMp4LkLdT4Z5sGTXcMTpqooC98VSAc3nfYcaka17jbXM5HkjxwQ1kljO0ALxxWXI%2BBhTjBudIDfKqM%2Bl%2BKAs1X%2FscjT7xHCJOQtb9LuBjsF%2FBOx6LazEKziZdhcucc06dixqUlbiE7skzqcmtw56NbrpIEbrAWfAR%2FFUH8TO85OStvLhtJAm1pr1jmJkRPQcpb76lSYSbUBYF24QBA016Y4B5n4OrFaoU82uMjKT4WFkSfvu7u1zT7MSybi1SoBvOzeehsX%2FsDzgHM5uVW3XSqeeeIrV%2F0oYbmRHdafv%2Bg03WVLbupAd7eDnp%2F7ePGrC1fg6jQAHjhmPSFiMx1sAelC5R2SNT%2F%2F7qjSuWef%2FomSy46Sc%2FXr7bu%2BIJ3011uVYhqcyHMdoaYH40gfrXidTWrHbCBOy6WeEAMS%2FrqjEWO1sAHxyMguAK7PS0jlf78%2FSOjbAE%2BLvv4K7DB5qvoIw6J8VZuPiG%2FQRp3GPeYH7mHYWZ1oRRGffSFZBmT5tgQUnKVa39hk%2Brlk0gH0YKDhELbAZ2yFJZnnXRBupOI3apkaTwhSS3cV%2FBrwyiWYhhwO8H2V3uOo4EpRB%2FAp6DkL%2FZ1cxgE2MXKQZ1zCLuv%2FSBjqkAa3DkJWly3QP9kBBlArAfJubtCsBSxAOHfBuKVxISmxnPEI8p00CJgocfHsrZV0HUTMsB80%2F1JV367O%2FWt56oZLsKZTQpRFIV9oJHUDGrvTOFv8IO4SjkJiskkztBVEfmUfQ3pHbbmeJJ8FMea9a4Z6VpYV8BN%2F%2BnH2DGjTHPjiOpaDv0KeLgu6qwlTSmQ7r7q%2BvDIZz1T9xvXNswOc1DgVTBafg&X-Amz-Signature=625fab5c499cb781b1a74610ee3808d64a4d758e6d3878dd4cf7c36fa8c70385&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

2002， 3003 以及是4004，这个时候用户他选择了 2002 以及是 3003 进行一个支付，这个时候只要支付完毕之后写一下，这是用户购买下一个 3003 也是用户购买。这两个购买了以后在我们的购物车里面现在应该只能够剩下 1001 以及是4004。所以相应的其实我们应该要把这两项从我们的一个购物车里面去剔除。剔除首先我们应该要在后端里面先去把相应的一个后端购物车去剔除，剔除完毕以后再覆盖到前端的cookie。在我们的后端现在还没有讲到Redis，所以我们还是写一个Todo，只不过我们的 cookie 我们在这里可以预先的先把我们在前端 cookie 中的购物车直接把它给清空就可以了。后续我们再回过头来再来进行一个完善。先写一下Todo，整合 Redis 之后完善购物车中的已结算商品清除，并且是需要同步到前端的cookie。OK，在我们这里我们就直接来使用一个cookie，有 tales 直接去覆盖一下。


点set。在这里面是需要用到一个request，就是 response lets gdp server it requested，这个不要写错，这是一个request，下一个是 h c p server it response。好，OK。在这里面我们的 cookie 就可以去设置了。第一个是request，第二个是response，第三个是 cookie name，我们所设置的一个名称。 cookie 的名称我们在之前应该没有写，应该没有写。我们在这里写一个extends，有一个 base controller 在这里面我们来写一下。我们可以写一个固定的字符串，这个字符串统一的就可以定义为是一个购物车。在这里写一下 public static final street 取一个名字叫做 foodie shortcut，转换成大写的，取名就叫做 shop cut。简单一些， shop cut 其实就是和我们的前端里面的 cookie 中的 shop cut 其实定义成是一样的，在前端里面其实也是有的F12，大家可以看一下，也就是这个名字是需要和一一对应的。好定义完毕之后，我们就可以在 Ctrl 里面，在这个地方就可以直接去设置的。


这是一个 shop cut，我们的一个 cookie 的名称，随后 cookie 的名称后面你还是需要去进行一个 cookie value 的设置。在这里其实我们就可以设置一个空的list，也可以我们这样子我们直接设置为一个空字符串，因为我们把这个当做是购物车直接去清空就可以。再来一个true，我们的 is including 设置为true，这样子我们前端的一个购物车就可以进行清空了，只不过这一步的操作，清空特定的数据，我们会在后续整合完 Redis 之后，我们再回过头来完善。


OK。第三步我们先不做，第三步我们到后面我们讲到的时候，我们再来做。在这里会返回一个OK。OK。目前还没有携带任何的数据，我们可以打开前端，我们来看一下。前端这里是发起一个请求去创建订单的，它会有一个回调，这是一个result，在这里我们是判断一下 200 是200。随后可以看到它其实会获得一个 order ID， o 的 ID 其实就是由我们的后端创建完毕订单以后，相应的数据在数据库里面都会有了。随后你是需要把这样的一个订单的 ID 传到前端的。所以在我们的后端其实在这个地方创建订单的时候，其实我们就应该要在这里返回一个 string 类型的 order ID 了。好，我们在这里面要去改一下，在这里 return order ID 要传出去的，在这里面也要改。 string 不是使用的 word order ID，是在这里本身就可以生成的，生成之后直接在这边 return 出去就可以了。在我们的 Ctrl 的里面，在这个地方直接可以去写一下 string order id，好，拿到了以后直接可以把 order ID 放到 OK 里面去，这样子在我们的前端其实就可以获得了。


来看一下前端获得到 order ID 以后，在这边会进行一个判断，要判断我们的一个支付方式，这个值支付方式其实就是在页面上用户选择之后，他会获得的一个值，这个值首先判断是不是1，唯一如果是1，它是一个微信支付。在这里会发生一个跳转到微信 k 点 h t m l，后面会携带上一个参数，这是 o 的ID，这个就是从我们后端生成的一个 ID 之后再携带过来的，它是会发生一个页面的跳转的。OK，好，下一个。如果他选择的是一个支付宝支付，在这里支付宝支付他也会跳转一个页面的。在这里可以来看一下。首先一个当前页面是进行一个页面的跳转，是跳转到阿里 pay 点HTML，会把一个订单的 ID 以及是 amount 金额携带过去。另外一个会在我们的浏览器里面额外的再打开一个页面，是 RD pay temp transit，点HTML，把订单 ID 给传过去，是支付宝。


支付我们会先讲微信，讲完微信以后我们再讲支付宝，所以这两个我们是分开讲的。如果我们的支付方式不是 1 也不是2，在这里我们就可以做一个提醒，在创建订单完毕以后的一个相应的判断。在我们可以先把微信配点 h t l，我们先可以打开来看一下。在这里有一个微信 pay 点 h t m l 好打开。打开来了以后我们可以到这里面我们来看一下咱们的脚本。这个页面的内容其实是比较少的，其实在这里面点击我们可以来看一下。直接点提交订单，页面会发生一个跳转，我们后端还没有重启，一会再说。我们回到前端的代码，在这里面我们来看一下 create 的其中会有一个。先来看这里，这里是获得一个订单号，随后如果获得到了之后，我们通过一个赋值给我们当前的 c s 对象。 c s 就是当前我们的实验，也就是 view 的一个对象。我们就可以去做一个事情，就可以 get 微信配 q r code URL。


q r code 其实它是一个二维码，在我们的一个网页里面，我们是通过微信的扫码去进行支付的。我相信大家在其他的一些购物平台，只要是微信支付，基本上都是使用的 QR code，也就是二维码去进行支付的。OK，现在我们可以来做一个测试。我们先把我们的后端进行一个重启，因为后端我们在是修改了service，增加了一个 order ID 的返回。另外我们前端的一个购物车在这边，我们也是把一个数据去进行一个清空了。所以我们在这边我们是需要先把 maven 全局的去 install 一下。好。OK。现在我们 build 是 success 了。随后我们就要去启动一下我们的服务器。


启动服务器之前我们在这里先说一下，我们现在已经是把 cookie 的设置，这个代码是写的，我们会直接把购物车里面的数据给进行一个清空。但是这样子会不便于我们后续的一个测试，因为我们要去进行支付，肯定要频繁的进入到订单详情页，再加入到购物车，再点击结算，随后再去进行一个支付，这个流程比较多。


为了精简这样的流程，所以我们在购物车里面数据，我们就不去轻功了，我们把直接给注释掉，等到我们后续开发完毕以后，可以把注释给放开，或者直接可以把 Redis 整合完毕以后，我们再来把进行完善。其实都是没有任何问题的。好，在这里我来重启一下服务器。


重启服务器成功之后，我们到页面里面刷新一下。页面刷新一下，好，没有问题。点击微信以后，在这边我就可以直接点击提交订单了。好，点击提交一下。提交以后在我们的后端报了一个错，这是因为我们的库存我们做了一个设置，所以千万不要忘记。我们在进行测试的时候，我们把数据把库存 0 多改掉一些，比方改成 1002 这样子，保证库存充足的情况。我们再来做一个测试，点击订单提交，再点一下。好，OK。


现在我们的一个页面已经是跳转过来了，只不过是在这个页面里面所展示的一个订单金额，这个订单金额现在是没有任何的内容。另外我们的一个支付二维码现在也没有，肯定的在我们的页面里面，在控制台报了很多的一些 404 的错误，但是没有关系，因为已经是涉及到了支付中心相关的一个业务了。到这里其实我们的一个订单流程的第一步也就是用户购买并且提交到后端创建订单的步骤，其实我们已经是做好了。我们从下一节课开始会讲解我们的一个支付中心，正式进入到我们的支付阶段了。

