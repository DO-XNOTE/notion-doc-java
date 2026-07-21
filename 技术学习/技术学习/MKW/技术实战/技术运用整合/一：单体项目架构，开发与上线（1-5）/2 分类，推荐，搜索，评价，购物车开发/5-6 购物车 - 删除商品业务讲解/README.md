---
title: 5-6 购物车 - 删除商品业务讲解
---

# 5-6 购物车 - 删除商品业务讲解

[image](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/1f581c3a-7fa2-43b5-901d-1fe64c7e5862/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VIU4QNBJ%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T224655Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIFNGHVxJuN8V40GZQ9NQyGGUubc5kjdpPgjuJ482ZIFNAiBF2%2Bl0SQkDsRBJ76fdeNv2tJhozlL3uif7GwwdRA2wHyqIBAjG%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMtCamnOxfn7W9XQhqKtwDBRXu4Wtfr%2F8NnJiblmTdh2fvlG3NQBRZ8TjmgU2ih19PHNL%2FjUuAotb0eLT9RXyY4tFqHXRnBqWtumxS4kcnn0CPmr9fKP5SPcVCoJCSKBdCB57giyHsz6tYo42c5bXk5MCnZYeRysPzK2FVY%2FTgySf9RW03vJu1I8eKyVLR2rWEg6dwKabHSAyxTUNbybk4rBIcS5GCeR4NA8PEi42UZToFlE3nYfSrgKBg9HpJXhtyRqit6Z2CCZKkon2FhL7LO2CrBRxjJLYJ%2BYS8e4Z%2Fd61ImW10QPehcOoPAotXl83HdPKRe3yuLKHbNI5ZpZr56WUcyiYoW5RT0oNnPUkQ6k8WtwwZOiXbPxtsqYqQsck2G1OXRDAkEr12%2BA6NnGH8UX1jpysA4a1PkDKS43nwhiuz0MRrM5hhmoIfqEa4SzdJlAHsxYFTOxbgLHZiQuyuWHqLVyodNW4esEmimflX%2B3nmPvyHRUUucCBMt8fPyf5yEdgeUvpWl02canQMfowxg6WFHB%2BRoTnilkVWUqjr8OLA%2B0QaVKZUde4fg9W6e4T1s5UE4%2FNmxiGjSSJWmQZmOLdFuMTSNfEJJ7%2FwM5%2BJuOWecxN%2F8WaCRtZeS4vDqPfdLZsulwKx1yasa4ow7bf%2F0gY6pgFEvF8CUMWcGei59s5N1Tyk6itXONhVKftD9yu0ASAcvJmaSM%2FBzpwO5Gy3XK6r5yE47UBrzZbIeFXyH95OtpOr9f9ubHWEamqgVgLK99vNo%2B9FZtUCa7XuvdythDhnpzPqDk5Er%2FOK7mD8N0hPsYsNFL5kjzvGwnD2Ay06mlu4wCPmDisM95HFFEroL4TXkkEiHX73Sl3EIlFS%2F%2B4iUCeTYyUdKGyw&X-Amz-Signature=5ab6ec611468de68a8eff0625edf02255319b8355bb6304aaeb614d0bf1dee2c&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

既然我可以把商品添加到购物车，很显然我们也能够在购物车里面把某些商品进行删除。所以我们这一节来讲一下删除的业务。可以看到，在我们的购物车里面，其实每一个商品的后面都会有一列是操作列，我们是可以去进行删除的。比方我们可以删除这一条，点击以后，相应的内容就会被删除。这个时候其实我们应该要考虑两个情况，其实也就是在添加商品到购物车的时候，我们所考虑的一个是用户未登录，一个是用户已登录。两种情况我们都应该要考虑。如果是未登录的情况下，这样的一个数据，我们只需要在当前浏览器的 cookie 里面把对应的商品数据给删除就可以了，如果这一条数据是在后端，也就是后端用户已登录的情况下，我们也应该要拿着这条数据到后端的购物车数据里面去进行一个删除，这样子也是保证我们前后端数据的同步。OK。所以我们这一节就来讲一下业务。


我们先打开 VS code，先看一下 shop cut 页面，在页面里面我们可以来搜一下删除。我们可以搜到在我们的页面里面，在这个部位可以看到它有一列是专门用于操作，是用作删除的。在这个里面其实可以看得到它在被用户点击的时候，会触发一个 click 事件，会调用 delete from cut。


在这里面是传入的一个某一个商品的规格ID，因为我们之前也说了，在购物车里面每一个商品它是以规格作为单位的。好，我们再来搜一下。好，收到这样的一个方法来看一下，它是从购物车中删除商品的。我们逐步来看。首先我们是需要去提醒一下用户，因为有可能用户是误操作，所以你必须要让用户去确认一下你是否真正的要去做一个删除。随后我们就可以去执行前端删除的一个业务了。到这里我们可以来看一下。


首先一个先从我们当前的浏览器 cookie 里面获得一个整个购物车的列表，在购物车里面。随后可以看到我们在进行一个循环的时候，我们把它的一个规格 ID 和传入进来的规格 ID 进行一个判断，如果这个判断是它的一个值是true，就代表所对应的这一个商品我们应该要拿掉，所以就可以通过 shop cut list。它是一个 JSON 的数组。隐私please。可以把当前这是第二页元素进行删除一项，这样子其实就可以把它进行删除了。删除了以后，我们是需要把新的一个 list 重新的放入到 cookie 里面，也就是做一个覆盖。OK，这样子我们在前端的购物车其实做了一次更新。当然我们相应的要去把一个选中项去做一个清除。我们前面是讲了一个规格的 IDS 是做拼接的，在这里它其实也会有一个数组。其实道理也是一样，把数组循环的时候要判断哪一项是为 true 的。如果它的规格 ID 是和我们传进来的规格 ID 是一样的，很显然我们也要去进行一次space，把它的那一项给删掉，也就是对应在我们页面里面的这样的一个 check box。好OK，两项清出了以后，相应的，其实我们页面上的在前端的数据其实是清掉了，最终还是需要去进行一次重新的计算。这个方法是我们在上一节讲的，是重新计算选中的商品的件数以及是一个金额。这个是需要去执行的。因为有可能我们在页面里面是选中的情况下去进行删除，当然也有可能是在没有选中的情况下去删除，都有可能。所以在这里的已选中的商品件数以及是合资的多少钱，都需要去进行重新的计算的。


好，这些都是在用户未登录的情况，如果用户在已登录的情况下，我们就相应的是需要去把对应的一个商品的规格 ID 传递到后端，让后端的购物车也就是我们之前所说的存储介质。我们是使用Redis，在 Redis 里面把对应的这一条购物车中的商品数据去进行一个移除，移除之后我们前后端其实就达到了一个同步的删除的效果。OK，所以这一步操作是需要在用户已登录的情况下去执行的。当然如果删除成功了，以后来看一下。在这边我们只需要去判断它成功的状态是不是200，如果是 200 就代表成功了，我们就不需要去做额外的一些操作。OK，好，我们前端业务是前端的，讲完了，当然对应的我们的后端这一个接口我们也要去写一下，只不过和前面的添加商品到购物车是一样的，它只不过是一个空接口。因为我们要保证前端在执行的时候是没有任何的 404 错误的，因为路由对于前端来讲他找不到。


OK 好，打开我们的后端。在这里面其实也是一样，我们是需要编写到 shop cut Ctrl，在这个里面去进行相应的编写了。我们直接可以把之前这一段添加商品到购物车的代码拷贝一份，随后在这里面去做一些修改。首先第一个我们要把改成以及，其实就是一个举例子 swag two，我们改一下，这是删除，从购物车中删除商品。OK？ HTTP miss 的是使用的post，和我们前端也是一样的，前端也是post。好。下一个方法。名打掉传入进来的参数。其实总共是有两个，一个是用户的ID，另外一个是你要去删除的一个规格ID。规格 ID 是叫做这个名字，直接拷贝一下，贴到后端，贴到这个位置。它其实也是一个请求参数，所以注释我们是需要加一下的。另外它的一个 string 是它的一个类型。好，随后我们就可以进行这里面的一些操作了。对于 user ID 来讲，其实肯定要判断一下它不能够为空。除了 user ID 以外，其实还有一项规格 ID 你也要去判断，只要其中有一项出了问题，我们就在这里直接报一个错就可以了，或者写一个空信息，或者可以直接写一个参数，不能为空。这样子也行。只不过我们在这里面其实也是一样。我们要写一个Todo，这个 Todo 写一下用户在页面删除购物车中的商品数据，如果此时用户已经登录，则需要同步删除后端购物车中的商品。


Todo 我们先标记好，后续等我们。在分布式阶段，我们讲完Redis，我们会回过头来把空的接口去完善一下的。OK，好，现在我们就可以做一个测试了。我们先重启一下服务器，因为我们是改动了接口。现在我们就没有去进行一个维稳的因素，主要是因为我们的一些子模块子工程，我们都没有去进行相应的修改，所以你可以不用去 install 好。重启以后，我们到前端页面，我们先进行一个刷新，按一下F12，按 F12 主要是看一下我们会不会报 404 的错误。


首先我们可以先选中两项，现在价格总共是 1230 元，我来删除某一项。来删除第一项，点击确定，随后进行了一个删除。删除完毕以后，在这里原来选中的这一项还是会选中。另外目前的一个价格和已选中的一些商品的件数，在这边是进行了一个重新的计算，现在是有一件是 150 块钱，和这里是一一对应的。


OK。另外在我们的控制台，浏览器的控制台没有报任何的 404 错，所以请求其实到达了我们的后端，只不过在后端处理的时候，它是一个空接口。OK，我们在这里面其实也可以全部都清掉，删除，删除。OK。这样子全部删掉了以后，在我们的购物车里面，现在我们再次刷新数据都会没有了。当然也可以再按一下 F12 来看一下。在目前我们的 shop cut 里面其实是没有任何的值的，这个其实是空值。OK。好，现在关于如何删除购物车里面的商品数据，在这一节我们就讲了相关的业务。OK。

