---
title: 5-7 购物车 - 提交购物车至结算页
---

# 5-7 购物车 - 提交购物车至结算页

[image](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/c4ba8729-3dd8-4a14-baf7-9f922fe7cc70/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663JSUDK5D%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T224656Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIEF78LZToDnKt86ofKxaIoou%2FSeSwzXJvToP8LXs3CiJAiB5dEYjB6QyMHh%2BjhsQREAObBGHAPH5%2BqVNTakkhorWLyqIBAjI%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMYLAG0vrTq3PLUDJkKtwDaSugso4UavDenlaujlFJnNNeeDX7d3l7tn2CbE0VhrwdVzAoaaUtW5OZFrhTSL2C6iHd8v1wSyeCpeomInEOwHrJajVRFmJ2i4MhOpfOktu9M2SLQcNPDQya8cjpOMOInSdOYhuwrmnKdoOQKxx86g661jve5jzWd0PbGysNt3wBmC4UT7a03EZ5VPjiy4bdK9yygFTzcMwwk4yrsR%2FN3FpP2hnPQ%2FruJwWOevs%2BuhyTVyoQ5o1KU2f5%2Fl3baahzHkwJYRu6FCO%2BOzLvRQJmTKfWRhJZmANtS9CDZQ1R8LpXGX%2BiYLxavbwxZrFaFi12%2FN0KzFa4HfIESPpcxbXR9b07rmI4s8Y1u7BJ3AGlltO1yYwB79juurrgV%2Fn2YNIOcduC5KbSX%2FfpFrgiVjLoz5JbtTLfy8lNG%2B5jfNcn1Ti91McfjEeo%2FlswvdZ465KButaf7vBy6mRudED4YqOZpsXCFd6UsxX%2Bpv6Dw%2BQps3x9O1oXp7g0g2hhCF%2FD8OQNeL0QvSZPp0o3egKB7VLGf%2BfwcJjx4gF%2BqBX4p9LxR0UKrOQsqB6pVAeHasclqdQyk9ah%2BUzG6P2zukajNnXQ%2B7r7bTQOOpTgIrjeUwUDZpXxrL7sZWfB1%2F1vW6Qw5%2Bv%2F0gY6pgGQRsFVRnSIQHdQYKjuzNG7NcgTVX%2FVEj%2FIC2POD%2FET3zBNyLToqZJ62eSl2IX1a7OhPuLES0N26uHl8AwQJYoza7RezZpkA5BbC19ursEoqc8DxznaEJRQIKm%2Fu6zU1Mt8AUrLgnP2YzzkumP1OpLKcamGp%2Bs0OPrEWla2uNJphCHZ%2FtfjpCLqAfC06iqkNkt9OokORnbnbe4hBamgmRpP9rBAn1Gf&X-Amz-Signature=2cc5f2ab10633555c10815c3713397e9f3574d6c67628ddb0aa0af69a113f88f&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

前面几节我们是讲了和购物车相关的一些业务，这一节我们来看一下购物车的结算。其实也就是把当前用户想要购买的数据提交到订单页，要去生成订单了，这个时候用户还没有登录，并且他也没有去选择这里的商品，我直接点结算肯定是不可以的，因为现在在购物车里面没有任何的商品让用户去选中，并且现在要结算的价格是 0 块钱，所以页面是跳转不了的。所以在这里要打个勾，打完勾以后在这里就会有相应的价格了。


这个其实也相当于你在超市里面买东西，你把购物车拿到收银台，把一些你想要购买的东西拿出来，可能有一些你是不想要了就直接放掉，剩下来的在收银员扫码以后，会有一个相应的价格就会显示到这里，最终你再去进行支付。道理是一样的，但是这个时候还没有登录，来看一下。点击结算，它会提示请登录后请登录，注册后再进行结算。这个时候我们点击确定以后，页面会发生一个跳转。来注意一下。这个时候其实在我们的页面里面，在 u r l 里面多了一个 return u l，其实和我们之前在做登录和注册的时候，其实我们是有提到过的，对吧，是没有去讲。所以其实 return URL 就是用来做一个回跳的，在你登录注册成功之后，一旦 return u l 里面会有一个值，有一个地址，它会回跳到购物车页面。


好，现在我们可以来登录一下，点击登录，你会发现它不会跳转到首页，而是会跳转到购物车。这个其实就是我们在之前的登录注册里面的，其实我们有提到过来看一下。有称 u r l。在这里一旦用户登录成功，我们会进行一个判断，主要是判断 UL 是不是为空，如果不为空，让我们当前的 window 点老科线点 h r v f 进行一个跳转就可以了。


好，现在我们已经是跳转到了购物车页面。随后我们就要去进行一个结算了。全选点击结算。跳过来之后，其实这就是一个订单的，可以准备要去创建订单的这样的一个页面了。让用户去确认一下相应的信息。这个页面是配点HTML，在这里有的配点 HTML 页面是怎么跳转过来的？我们也是要预先的先来看一下。在这里找到 go pay，这个就是前往结算页面。


首先是要判断我们的购物车里面有没有商品，如果没有商品是不能够让你去进行结算的。不仅如此，我们也必须要让用户要在购物车里面选择一项才能够去进行结算。这个就是要判断一下规格的i， d s 这样的一个数组是不是小于0，只要是小于 0 就不行，应该是小于等于0。要去判断一下用户是否是登录，用户登录了我们才能够让用户去进行一个购物车商品数据的提交。也就是在这里判断是处。


在这里就可以直接跳转到 pay 点HTML，这就是准备要去进行支付了，确认一下你的支付信息，还有选择地址，另外支付方式也要去进行选择。OK，好。到这里我们订单页面，在创建订单页面之前的一个购物车相关的业务，其实我们都讲到了。随后我们可以到配点HTML。到页面里面来了之后，首先一个我们肯定是需要把购物车里面你选中的商品，你要支付的商品信息在确认订单的页面，我们应该要去展示一下。OK，所以我们可以来看一下。


在这个页面里面我们找到 create 的生命周期函数，找一下，这个代码比较多，找起来会稍微慢一点。在这里 create 的其中有一个渲染结算订单的信息，来搜一下。在这里首先我们先要从 URL 里面去获得选中的那些规格的ID，也就是把这个值我们拿掉在前端，它传过来的时候可能会有多个，它是以逗号去进行间隔的，比方是这样子，逗号102，在逗号 1003 这样子一个传过来。在我们当前页面拿到了之后就可以获得一个IDS，是拼接的。也可以看到在这里会进行一个split，最终再把这些 IT 一个放到数组里面去了。


以后相应的我们每一项会从可以看到 get item，也就是从 cookie 里面的购物车把相应的商品信息一个一个的数据都拿出来，作为一个item。随后再把一个的 order item 再放入到 order item list， order item list 最终就有了相应的商品数据了。不仅如此，你同时还要去计算这笔订单的一个总价格。总价格就是把每一项的单个商品的单价。成语商品在购物车里面的一个购买数量进行一个累加，也就是 total amount。最终在页面上会进行一个展示，就是最终的价格。最终价格在这里有一个实付款是 150 元。


OK。还有是一个 order item list，我们可以搜一下。在这里，其实也是一样，会使用 Vue 的 free 杠 for 循环的标签去一行把相应的商品数据进行一个展示。简单可以看一下，比方有一个，这是一个名称，商品名称，这是规格名称。另外还有是一个价格，这个价格是以分为单位，所以要出100。另外购买的数量在这里也都会有相应的一些展示。并且在这里还有一个，这是什么？这是一个总值的价格。


OK，这是一个单个商品的总值价格，也就是在这里所展示的一个金额。好，这样子，我们从上一个购物车页面，用户点击结算，提交相应数据，到确认订单的页面的一个商品信息我们就讲完了。其实在当前页面里面还包含了其他的内容，比方还会有地址相关的，我们在后面也会去说。当然时差的一些内容我们会在后续课程一节一节的来进行讲解，因为现在我们已经是正式进入到了一个订单流程了。OK。





