---
title: 5-2 中心首页 - 订单状态概览完成接口联调
---

# 5-2 中心首页 - 订单状态概览完成接口联调

[image](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/3af0a282-1288-4b81-9abc-f45b56d6ab8c/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TFNLJW6N%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T224741Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIDpDdz%2BXnM1%2FMhtXqSYY3w4yau7bR%2Fbcu9HYaCLUO%2FCsAiEAy4JeqTzqswF4xztsIrNEd%2BPSEKRJxVvTMwvHvtwlpHsqiAQIxv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDGlxJ0qe2qsF5K4GgircAzHHgDQjVv8lKfqltGM2I0t89970ZELKj8cgHMfwRzyGcOb2sElgwWPux4fBAOQFxWCiMCQQrhVhRiGRqZHbuSs5hwVizcGu%2FqufcjZ9InbLSbNSW5zVTcmfB1k2VOYqtUJnb0ZjUAGukGIQC1btYdP6nY6lXuyha2d15Xu80xkXlSQE3HM1U%2B2lzp%2BjW48Ltchk0ugyepc9H0I%2BsOqWlROH29bFKuItzi4YgGPtpy6J07YLFu7RaOxgATGwqYxocEutcnlvtge0fl%2Bchlsll0Zt8IQ8ekQqka54JRSqpEUkbip6XO41IzEwhdJbliK9teFkZigWdkz2umODzOxBdPXoCAUMM05hxevCZhxATrZ8X4CkD5QGCT1rGAsbnc0%2BTGKBrivVzRd7HiH1sUK%2BHyh%2FUPxAIaPW6TvKyY2s8FKEddxatiYE2CX9dOBDA5XRnjt%2BJdwiQXsCezXhaZZkraNkY9iZfRbvGi1ek6mmUxAvbGN8cr7CZ0ExaOJuw0RBbtChe3i9L2DA%2BEZA%2B%2FUzNLbfAyDpOqQuqhq%2F%2BUTt4S8pp9gLf%2BDeJPTGqLytvXll6twDK8gc%2Bm3ZiYyHNxQIjW4yT6Q27DBGRRNReKCBkwjVL8aw%2FZoymQ%2BpI3xRMKG4%2F9IGOqUB5ihyVfzhYPr2Fp%2F0CYqiUQ483bAzEPn%2Fav9wrqrCLLczkz1vd524%2BeM8nyJBcdBAAUD5w5Dq7EQic2SwC208LoKPeX52v%2B8BbzHAmFRGaJt8wY%2FZtYTow8wRaK%2FyldRnfdtnagsDLP4ODv0YqIsTQPacK2wvfIKGxxotdOI%2F7YLxR0dFra%2BW6wtNnWf3S18A6JuOlGBw7YBx0jOs9XrAZRVR%2FmKC&X-Amz-Signature=d7647a14851a013b70642b44a4db46189ca0fc50237d273391b2ad6037dafaba&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

查询订单数的一个 map 写完之后，我们一起来把相应的 service 可以写一下。在这里面也是要找到我们的一个 order service，应该是在 center 里面的 my order service。其次还有它所对应的一个实现。我们打开service，在这里面我们先可以去把它的一个方法先去写一下。这是在接口里面的取个名字叫做 public avoid get order status counts。传入的参数。很显然我们是根据用户的 ID 去进行查询就可以了。


查询用户订单数。好，我们到这里面去把对应的去实现一下。先把方法导入，然后再把事物给加上，这里使用 suppose 就可以了。好，我们之前写的这样的一个语句是有一条一条，其实我们在是根据不同的订单状态去查询的，在页面上其实是有 4 种不同的状态是需要我们去做的，是需要去展示的，所以在我们后端去进行查询。其实也应该要有对应的 4 次去做查询，所以在这边我们会发起 4 次的调用，四次调用我们的一个map。


在这边首先构建一下我们的一个参数，还是老样子，我们会使用 map 到前面去找一下，拷贝一个，好背一个 map 过来。第一个就是把 user ID 给放进去，放进去了以后我们要做的第一个查询的条件，使用 map 点 put 把一个订单的状态给放进去，这个订单状态我们定义的是一个 order status 贴过来，随后它的一个值在这边我们直接可以去写死，我们就可以使用 order status 它的枚举点 wait wait a pay 等待付款的状态，去做一个查询。好，这是我们的第一次查询所需要的两个条件。随后我们就可以去做一个查询了。可以使用 order map up custom 点 get my order status counts，把这个 map 给传入进去，它所获得的是一个整数，也就是数量。所以在它的前方我们可以递一下，取个名字，叫做等待付款 wait pay count。 OK 好，这是第一个待付款的数量。随后第二次查询，我们应该是把这个状态去改掉，所以我们只需要把改一下，把这个状态改为 wait delivery，也就是 wait a deliver 等待付款改为这样的一个状态就行了。在下方我们只需要把再来发起一次查询。这里由于我们的一个参数名是一样的，所以在他第二次去做查询的时候，他拿到的一个值是deliver。这样的状态值。OK，在这边取一个名字，就叫做 wait deliver。胖子好，这是第二个数量。


随后接下来，下面一个应该是把 wait deep 给去掉，写上一个 rate receive 待收获。我们是在比例了之后的一个状态。把改掉 receive 好，这是第三次再查询最后一个。最后一个是在我们的订单交易已经是成功之后，但是他还没有评价，所以是一个待评价的。把贴过来，这里应该是一个小case。除了这个以外，我们还是需要再追加一个条件，也就是在我们 map 里面所写的一个 is comment。把写过来。在这边我们写的一个值。我们其实应该是 yes or NO，使用这个枚举点 NO 点type，它是0，只有 0 才可能够去做一个条件。在这边写上 wait comment。


好，这是一个待评价的数量。当我们这些数量全部都拿到以后，我们是应该要返回出去。返回出去有 4 个数值。所以我们在可以去构建一个VO。 VO 我预先也已经是创建好了，给大家可以看一下。取得一个名字，叫做 order status。找一下。在这里 order status counts 比o。在这里面总共是有对应的 4 个不同的状态。在这边我们只需要把它给 mute 出来，去写一下 order status counts bo 写一下，这是一个 cos b o，在我们分别把不同的状态给写进去。在这边我们是使用了它的一个构造函数。好， 4 个全部都写进去，我们都换行一下，OK。总共是这几个顺序，不要搞错。第一个是 wait pay，第二个是有 wait deliver，然后是 wait receive，最后一个是等待评价。好。OK。对象构建好了以后，我们是需要有衬出去，有衬一个 counts b o。在我们的一个 boy 的就需要改为 view 了，相应的在接口里面把 boy 的改掉。好。OK。这样子我们的 service 就已经是写好了。 service 写好了之后，我们就应该要去写一下 control 了。到我们的前端先去看一下，前端是在用户中心，也就是 index 页面，到这里面还是一样。我们应该要找到 feel 里面的 create 的这样的一个生命周期函数。在这边会有一个渲染订单状态数 render order status counts 搜一下。在这个下方可以看到。


在这边构建了一个路由，在买 orders status counts 发起一个请求，这个请求里面只包含了一个用户ID，这样子就可以去拿到相应的内容了。当我们拿到了一个这样对象了以后，直接付给我们当前 this 去对象。在我们的页面里面，我们就可以拿到相应的内容了。


可以到页面去看一下，在这个地方其实都有，是根据 order status cons 去做的一个判断，就是一个 v 缸show，它大于 0 了，就显示不同的一个内容。这边其实都是需要去做一个判断的，只有在它的数量大于 0 的情况下，这个值才会在这边进行一个展示。


OK，好。这样子我们就可以去根据路由再搜一下。刚刚的一个对象。我们找一下路由是在下方的这里 say status counts。OK，把这个方法拿到我们的 Ctrl 里面去建一个方法。 control 了 center 找到 my orders control 了，我们直接写在这里，可以去写一个方法名叫做 status CONS，对吧？在我们拷贝一个，拷贝一下，把贴过来，这样子他就可以去请求到了。把他的 strike two 接口的名字改一下，这是获得订单状态数概况。发起的请求。和前端看一下。前端是一个post，所以在这里我们也使用的是一个post。传入进来的参数。我们只需要一个用户 ID 就可以了，其余的我们全部都删掉。在这边判断了一个用户的ID，用户 ID 是不能为空的。下方这些我们就不需要了。这是其他的判断。通过买 old service 去请求。在这边的话是 get order status counts，把 user ID 给传进去。传入进去以后，我们会拿到一个VO，这个 VO 在这边进行一个接收，这是一个results。最终把 results 放到 OK 里面，传到前端。这样子我们后端所对应的一个方法就写好了。好在我们使用 Maven 全局的 install 一下，好 build success，随后再做一个重启，好，重启成功。


随后到我们的页面，我们在这里来刷新一下。刷新了以后可以看到这边的待付款有 3 条，待发货有 9 条。这个是对应在我们的订单管理里面的一些状态，一个是待付款，一个是待发货，可以看一下数量。待付款有 3 条，待发货，在这里是有 9 条。OK，没有问题。在这边其实我们可以去把它的状态去更改一下，我们可以搜一下。


我们找一下这一条商品，这一条订单所对应的一个记录，到我们的数据库里面去搜一下。在这里是这一条订单，是这条订单，我们是需要到订单状态表里面去。在这里我们把它的状态改一下，手动改，改成30，更新一下。随后我们到页面里面去刷新，看一下，有一条待收货的记录。对于这样的一条待收货记录，我们只需要再点击确认收货，点击确定。这样子我们再来看一下。这个时候确认收货以后，就代表这一条的订单其实已经是交易成功了，我们就可以去等待评价，对吧。到我们的已完成里面有一条对应的记录，也就是这条订单去评价一下好评，点击发票评论。评论成功以后，在这里再看到这边的一个数值 1 就没有了。OK，这样子。对于我的订单的订单概况，订单的一个未完成数量，我们就已经是完成了。

