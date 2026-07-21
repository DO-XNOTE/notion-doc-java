---
title: 5-3 购物车 - 渲染(刷新)购物车 - 上
---

# 5-3 购物车 - 渲染(刷新)购物车 - 上

[image](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/9bc0205a-8bae-413f-baba-4ab199251c8f/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466R7PVK6CU%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T224652Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIBienOjrCequbBpuiNLA1B1GQu%2FHf%2BqIh772irJwH4uWAiABjv91%2FGWAOBk7GXb4OdWzhf5WsZ6oR5x2vPorSDBqIiqIBAjG%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMcnoytlXEbtYdRCOHKtwDpTRbQjgL%2Borwy1ek9ls8fbzft0ycG1QNFHgJPSfPZ1O5JjcM%2BKk1aOK%2FnT5KlA97bcid%2BxLOIw6l7R3FW8m26i89%2F5GYJZxvioPBhrHk63ZT9LT0jjTGN%2FsqZQupK75c6JykFpnmssZdo0cScxL9spwzUKOHpFuE2R0fRBNkEUL%2BsDyEWjuSRSbdM3aEPoL4H4OyZIujld7%2Bsv6fRMAZFhtTwIJP5HZCoHyJxz0eqal94oZoMtw8FFdHfk5B%2B4E8H3tpiY3zW5851Fswqcj%2FRVKx3TW5tJhQFzVPN1skqYnBiRnZJsZKbv9gJyqggFTQiiYBYmFzgllv7lhMJa%2BN4EGl3719niSxRNV9FNJK3GKxg2MiQ77%2FOYB5sLCjUMJpKSS8RjHB1ibNfBeooRqbNICx2kMlYuQENHLp1mCdXJRmPAEXDh2HecwUSBLaTsTQjQHt3Jfcb9NQDZyLtTDUS8UZWQOeey9dT4iMXgV65xQ1saQyfDhcZYvV58tf1vIAT4qbC6pI1vgKnipL8VLSQ6OIp0icixIzuYVbnl4uCuoDb0JorekqS%2Fw8MmTUHrFnZmNZ9Ms5YZxcQNSXQ%2BkvnHcV3D53XtQokoYAY9HCDwlX188SVJD8LnunbCgw2rr%2F0gY6pgGdtK%2Bkbi9lLBolo%2Bw%2FC%2F9FXYvwxhclTue9E9DcgRa09uzgab3U65moB7lYY6CwDODOtELmH9I44OkPgbuY%2FnycIjdTjjpeiN6w0mLiIc3EwYNgy3irIkDHXuGs7CZ1NJiNh0j02s5fDGIR6P4q6Z4tn%2BUM%2FoH4NG5Oh1i%2B%2BEHkKUqvjm2ue2PJ9p%2BA7Yf%2FG7MZ8zfbKj3yVT%2BYq6ou5tFJx6866m8g&X-Amz-Signature=f10f89fe22e2527f0b5a720c4670278c3371eeafedd08ab71549a4493fb3455d&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

上一节我们是讲了把商品加入到购物车，在加入购物车以后，我们应该要点击购物车页面来看一下，也就是在这个位置它有一个购物车的数量，有一个 2 这个数字，这个 2 我们用户可以去点击以后页面发生一个跳转，这就是购物车页面。在购物车页面里面相应的一些购物车数据，我们是应该在这个地方进行一个展示，但是现在并没有。所以我们这一节就要来讲一下如如何去把购物车里面的数据拿出来做一个渲染。我们可以在这里可以先考虑一下我们现有的一些购物车数据，我们是临时的，可以是放在前端，也就是浏览器里面的cookie，我们能不能够直接把 cookie 里面的购物车数据拿出来，再放到我们的页面里面去进行一个渲染，也就是在这里面 cookie 的 shop card 直接拿出来去做一个渲染。


答案是不可以。这是为什么？这是因为我们的数据保存在前端，它只是一种临时的数据，主要因为是价格。我们用户放在购物车里面的一些数据，他不可能马上就去结算去买单的，他有可能明天后天过了一个礼拜再打开。再打开购物车的时候，相应的价格，它还是以前的价格，还是在 cookie 里面的价格。


所以当用户进入到购物车页面的时候，其实我们应该要刷新一下购物车里面的一些商品数据，如果价格发生了更改，如果商品的图片，商品的一些规格以及相应的名称都发生更改，其实我们应该要去重新的去刷新一下相关的数据，除了这个数量我们是可以不需要去做到一个更新的，其他的尤其是金额我们应该要去做一个刷新。所以我们在这里就需要把相应的数据，尤其是放到购物车里面的。规格的 ID 要发送到后端，让后端去查询出来。在这里面购物车相关的一些数据，随后再到页面里面去进行一个展示，这个其实就是刷新购物车，进行购物车数据渲染的一个相关业务。


OK，好，我们可以先来打开一下前端，看一下前端的购物车里面的业务是怎么走的。在这里面我们找到有一个叫做 shop cut 点HTML，这个就是和购物车相关的，点击一下，点击打开，在这个里面我们可以往下面看。我们直接找脚本，也就是找 create 的，这是它的生命周期函数。在这里会有一个this，点 render shop cat。这个就是渲染购物车商品的数据，我们搜一下， Ctrl f 直接搜来看一下。首先去获得一下当前在 cookie 里面的购物车，如果购物车里面是没有任何数据，没有商品就直接 return 了，我们就没有必要再继续后面的业务。随后再看一下，在这个地方我们要去进行一个规格的ID，规格 ID 我们是需要去进行拼接的，因为每一个商品有多个规格，我们存到购物车里面其实是按照规格去存的，所以我们会以规格为单位，把所有的一些商品规格 ID 都通过逗号间隔拼接成一个字符串，再发送到后端。可以看到这是一个 for 循环去进行一个拼接的。


拼接完后，它其实是这样子的。比方是一个1001，逗号2002，逗号3003，逗号4004。这里面的这些编号就可以当做是一个的规格ID。在这里这样子写一下好。规格 ID 拼接完毕以后，在这里他会发起一个请求，请求到后端，后端的路由会取一个名字叫做refresh，用于去做刷新的。在这里拼接的整个 item s， p c i d s。这就是规格ID。拼接后的一个字符串。会以一个请求的参数传到后端。以后我们就可以执行相关的业务了。在这里是一个 200 状态。


这一块内容我们先不说，我们等到完成后端接口以后，在这里我们再和大家去讲一下。现在我们可以先把接口所涉及到的一个数据层，也就是相关的一个 SQL 代码，带着大家可以先去写一下。打开我们的 Mary cat，来到查询，我们先新建一个查询，先把保存一下，取个名字，这个是刷新购物车中商品数据。好，我们写一个 select 放大。在这里面我们要查询出来的相关的内容，其实就是商品对象，就是购物车里面的商品对象。我们在上一节课里面其实已经是构建过一个了，就是这个 shop shop cut Bo 就是这里面的。这些相关的数据，除了 by cans 我们是不需要的，其余的这些内容我们都要。我们先把这些我们可以统一的拷贝放到这里，先拷贝进来。


好，我们来做一些相关的查询。首先第一个我们先直接写 select 星号 from 表规格表，因为我们是以规格为单位的，取一个别名，这个别名我们就这样来一个t。下划线 items s p c。写详细一些，你可以写短一些，也可以写长一些都是可以的。来一个 left join。我们是需要查商品的相关数据，所以在这里商品表是肯定要有items，别名叫做 t ITEMS。这里主要是我们做的一些多表关联都是和 items 有关的。 i 写的太多太短可能会容易搞混，所以我们在他们的前面加一个t，这样子会更加的好识别一些。


再来一个on，这是在 t items 点，它的 ID 是等于 s p c 的规格表，里面的 shop 应该是 item 下划线ID。这两个 ID 进行一个对等。这两个表还不够，还要有一张图片表，因为我们涉及到一个 item Imagey，有可能商品的图片是会被商家去更改，所以我们也需要去查询一下。去刷新出来。也是写一个 left join，在这里是 item image。


这张表取一个别名，叫做 t 下划线 items image。OK，来一个on，在这里。很显然，其实把直接拷贝过来把，应该是 item image，它里面的 item ID 要和这个的 item ID 进行一个对的，当然把如果我们不使用 image 的，我们使用 items 点 ID 也可以的。这样子把放到后面，这样子也可以。


好。随后我们就要加上一些相应的条件。where。首先第一个是我们图片的一个主图，所以把条件给加上 is man 等于1，这个是需要去加上的。再来一个and，这个 and 很明显就是我们 s p， c 这张表里面的 i d。把这个拿过来，它的 i d 点 i d 来一个印那么硬，它是有一堆的内容，所以我们在这边会使用。我们可以这样子使用一个括号，在里面放入一些相应的数据。虽然我们在前端传入过来是一个拼接的字符串，但是在我们后端接口接收到以后，是可以把这些字符串去进行分割，再以一个 list 传递进来的。所以我们在这里 circle 的时候就可以直接这样写。随后我们可以去看一下规格，在规格里面其实有很多的一些ID，在这边我们可以挑一下。简单的一些，我们直接在这边写一个 135 就可以去做一个查询了。好，我们全部选中运行一下。相关的数据是可以全部都查询出来，没有问题。只不过我们在这里是一个新号。既然是新号，我们可以把这些内容全部都拿过来。我们是需要去做一个精简信号太多了。


首先第一个是 item ID，所以把 t items 点 ID 查询后拿出来，直接 as 为 item ID。好，这是一项第一列。随后下一个应该是 items 这张表，它里面的名称商品名称就是 item name s item name。下一个下一个是商品的图片，应该是 t items image 这一张表，点它里面的一个 u r l s item image URL。商品的这三项内容就已经是有了。好。随后下一个我们就应该去使用。 s p c 就是规格的，把规格表的别名拿过来。首先第一个它的 ID 我们是需要拿到好别名，写好下一个。下一个应该是规格的名称，点 name s s p c name 好。OK，这一项我们是写好。


最后下一个是一个 by counts，我们是不需要去处理，因为它本身可以保存在前端的，就算更改了也无所谓，因为我们在乎的是商品的一个数据，尤其是金额。好。下面两个分别都是金额了，也是从规格表里面去取的。第一个是 price discount， s discount 好。最后一个是normal，普通的价格。 


price normal 好。OK。好。现在我们所需要去查询出来的内容，这些列我们都已经是OK，总共是有 7 个字段。 7 列好。我们来运行一下。以后在这里报了一个错，很明显多了一个逗号。最后一行是不能加逗号的。好。保存运行OK。相应的数据全部都查询出来了，总共是 7 列好。查询出来以后，我们就可以继续去完善一下我们的一个自定义的map，以及是service，还有是Ctrl。这些内容我们下一节一起写一下。

