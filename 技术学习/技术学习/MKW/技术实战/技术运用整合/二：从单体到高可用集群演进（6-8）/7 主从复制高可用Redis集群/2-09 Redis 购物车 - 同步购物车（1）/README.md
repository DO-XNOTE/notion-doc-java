---
title: 2-09 Redis 购物车 - 同步购物车（1）
---

# 2-09 Redis 购物车 - 同步购物车（1）

[image](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/c4ac36f5-cafe-4bb7-bff2-2ebc521809d3/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VIRTXFOA%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T224946Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCICqucsRPyBEeGwuNlc7JoiY1Kc96M1kNytP2%2BLqcY%2BFxAiBTxfTvurpZdkW0LA3%2BfSz%2B6F4%2FQiocGeW2GFvTwMxs9CqIBAjG%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMQMPbKPDTUlik4ypOKtwD3qsgLtKKdov6cXkxqnnNgDE9m%2Boo3b45rOgRDQ%2Fhn%2FJLSdfSARgj6vDov6aNkzPxzgUzfQLFKwtaq6gMWeHXa2oiZ4eQyyroGXMHFW1rwF%2BrwlzXD%2FZxIuiWCMYKQ6mUo3XyAi70Y1rLn%2FZhKvntm4%2BmdYW3Aow7q654C7mNrNheEcTdC%2Fr%2F47c7kHONwFCS31gR14lktX2v2Kz1OpNUlg36obhiGMmbYvhM7maaKWsS1NqsJoWqmblMV3Sw%2BumJG5w5NpCgLmcCuI8NEodu%2FhIfE1RpUZwk8sVBatQnk5upOZ97%2Fg6WXF%2FlEofCsqrUCclc6Vz9jaVQQU9v43hgi88bKiuANHPPtStD%2Bu8pX9jS3WCx8iDczHXqIF5iyZEwUSLJQW1tZZBkszVtfEscbmDUoMHS8nGVc%2BWBzZqv7rJl5k5921zDhIVyFv6zLTBM4lN%2FwxThAqM%2F8vu%2B1Il6Zv4EgtpVt0Eb2QBa%2BvI835V0Is2bvS87nJJZW8YDOvBapPxajqXOyyURubdgc9eothxR6ZdB3ySCne0%2B3Gk8EYnnBQswmSN%2FRVKsWXfBSAGPeCQosCXBBJx5gfwdvZ8wULPSqGf5oS56SB9Crb3J88M%2B1101RLkHWLR881Uwnrf%2F0gY6pgGoDyqgo%2FK%2FKg0I%2Bq3efqjgIkinEvxJKG%2BJd2iQIQim7FsfAmD2uxBsZPmuoq%2B9T95GmxkXL%2BGtV6pf5UYaxrvK8R0Cv4SePCSYhlvJw9%2BgtOX5UdRZqpn3II8xD4MzVHt1QJ7Jk0Tih1z%2Fa2srdS3KeDUAYWF8FVPAWpnZOGvVDqnMJ0ux85LA2z6LUyJqfl8l%2BMBRgqPwS9tXyz5MmrQzKWqTHc6G&X-Amz-Signature=5576f8b946842ed64b735a3c4b03841c81b27ef99fb3a783e8c67852b8ed8ee2&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

[image](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/4c622195-39f5-402d-aa9a-9144f9506a8c/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VIRTXFOA%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T224946Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCICqucsRPyBEeGwuNlc7JoiY1Kc96M1kNytP2%2BLqcY%2BFxAiBTxfTvurpZdkW0LA3%2BfSz%2B6F4%2FQiocGeW2GFvTwMxs9CqIBAjG%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMQMPbKPDTUlik4ypOKtwD3qsgLtKKdov6cXkxqnnNgDE9m%2Boo3b45rOgRDQ%2Fhn%2FJLSdfSARgj6vDov6aNkzPxzgUzfQLFKwtaq6gMWeHXa2oiZ4eQyyroGXMHFW1rwF%2BrwlzXD%2FZxIuiWCMYKQ6mUo3XyAi70Y1rLn%2FZhKvntm4%2BmdYW3Aow7q654C7mNrNheEcTdC%2Fr%2F47c7kHONwFCS31gR14lktX2v2Kz1OpNUlg36obhiGMmbYvhM7maaKWsS1NqsJoWqmblMV3Sw%2BumJG5w5NpCgLmcCuI8NEodu%2FhIfE1RpUZwk8sVBatQnk5upOZ97%2Fg6WXF%2FlEofCsqrUCclc6Vz9jaVQQU9v43hgi88bKiuANHPPtStD%2Bu8pX9jS3WCx8iDczHXqIF5iyZEwUSLJQW1tZZBkszVtfEscbmDUoMHS8nGVc%2BWBzZqv7rJl5k5921zDhIVyFv6zLTBM4lN%2FwxThAqM%2F8vu%2B1Il6Zv4EgtpVt0Eb2QBa%2BvI835V0Is2bvS87nJJZW8YDOvBapPxajqXOyyURubdgc9eothxR6ZdB3ySCne0%2B3Gk8EYnnBQswmSN%2FRVKsWXfBSAGPeCQosCXBBJx5gfwdvZ8wULPSqGf5oS56SB9Crb3J88M%2B1101RLkHWLR881Uwnrf%2F0gY6pgGoDyqgo%2FK%2FKg0I%2Bq3efqjgIkinEvxJKG%2BJd2iQIQim7FsfAmD2uxBsZPmuoq%2B9T95GmxkXL%2BGtV6pf5UYaxrvK8R0Cv4SePCSYhlvJw9%2BgtOX5UdRZqpn3II8xD4MzVHt1QJ7Jk0Tih1z%2Fa2srdS3KeDUAYWF8FVPAWpnZOGvVDqnMJ0ux85LA2z6LUyJqfl8l%2BMBRgqPwS9tXyz5MmrQzKWqTHc6G&X-Amz-Signature=dfa3d63b20dbd3df8a2546a0b8e71a58229825ce5117782a55ffd85df27b097f&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

[image](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/fa056bdd-0511-4df2-a410-fe59cf541c39/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VIRTXFOA%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T224946Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCICqucsRPyBEeGwuNlc7JoiY1Kc96M1kNytP2%2BLqcY%2BFxAiBTxfTvurpZdkW0LA3%2BfSz%2B6F4%2FQiocGeW2GFvTwMxs9CqIBAjG%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMQMPbKPDTUlik4ypOKtwD3qsgLtKKdov6cXkxqnnNgDE9m%2Boo3b45rOgRDQ%2Fhn%2FJLSdfSARgj6vDov6aNkzPxzgUzfQLFKwtaq6gMWeHXa2oiZ4eQyyroGXMHFW1rwF%2BrwlzXD%2FZxIuiWCMYKQ6mUo3XyAi70Y1rLn%2FZhKvntm4%2BmdYW3Aow7q654C7mNrNheEcTdC%2Fr%2F47c7kHONwFCS31gR14lktX2v2Kz1OpNUlg36obhiGMmbYvhM7maaKWsS1NqsJoWqmblMV3Sw%2BumJG5w5NpCgLmcCuI8NEodu%2FhIfE1RpUZwk8sVBatQnk5upOZ97%2Fg6WXF%2FlEofCsqrUCclc6Vz9jaVQQU9v43hgi88bKiuANHPPtStD%2Bu8pX9jS3WCx8iDczHXqIF5iyZEwUSLJQW1tZZBkszVtfEscbmDUoMHS8nGVc%2BWBzZqv7rJl5k5921zDhIVyFv6zLTBM4lN%2FwxThAqM%2F8vu%2B1Il6Zv4EgtpVt0Eb2QBa%2BvI835V0Is2bvS87nJJZW8YDOvBapPxajqXOyyURubdgc9eothxR6ZdB3ySCne0%2B3Gk8EYnnBQswmSN%2FRVKsWXfBSAGPeCQosCXBBJx5gfwdvZ8wULPSqGf5oS56SB9Crb3J88M%2B1101RLkHWLR881Uwnrf%2F0gY6pgGoDyqgo%2FK%2FKg0I%2Bq3efqjgIkinEvxJKG%2BJd2iQIQim7FsfAmD2uxBsZPmuoq%2B9T95GmxkXL%2BGtV6pf5UYaxrvK8R0Cv4SePCSYhlvJw9%2BgtOX5UdRZqpn3II8xD4MzVHt1QJ7Jk0Tih1z%2Fa2srdS3KeDUAYWF8FVPAWpnZOGvVDqnMJ0ux85LA2z6LUyJqfl8l%2BMBRgqPwS9tXyz5MmrQzKWqTHc6G&X-Amz-Signature=16500ce885bea9a0609c6f138460c0d69af99f4605506708259ace4eb2dc26a1&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

上一节我们是完善了购物车的一个商品的删除，另外是在用户购买以后，也就是订单提交以后的一个购物车数据的清理。那么接下来的话我们来继续往下面看一下。那么现在还剩下购物车的话，还剩下是一个同步。同步在这里来看一下，这里是注册，这是注册的部分，另外还有是一个用户登录的地方，那么登录和注册以后其实都会有一个同步购物车的数据，那么这是两个一模一样的方法。那么这个同步购物车的数据是什么意思？可以先这样子，我们来先把这个方法先写好，之后我们来给大家先分析一下

private void，然后来一个同步，这是一个 sink shop cut data，加上一个注释，这是注册登录成功后同步 cookie 和 Redis 中的购物车数据，那么在这里面其实做同步的时候，其实我们就需要去考虑 cookie 和 Redis 是否为空的情况，那么我们在这里可以去写一下


首先第一种，如果说我们的 Redis 中无数据，如果说 cookie 中的购物车为空，那么这个时候不做任何处理，因为两边都为空，我没有必要去做同步。那么随后还有一种情况，如果 cookie 中的购物车不为空，那么这个时候的话我们就应该要同步吧，此时直接放入 Redis 中，因为我们的 Redis 是空的，所以我们就可以直接把 cookie 中的这个购物车 list 直接往这个 Redis 里面一丢，那么这样子的话就可以去实现一个同步了。


随后第二个，那么第二个这个时候我们在 Redis 中如果说有购物车的数据，这个时候拷贝一下，如果 cookie 中的购物车是为空的，那么直接把 Redis 的购物车覆盖本地cookie。因为这种情况的话，比方说我现在是在公司里，我可能会把一些数据是放到购物车里面的，然后下班回家了，下班回家我重新登录我家的电脑，这个时候如果说我是在之前公司里面存的一些数据的话，那么我应该要同步到我当前的本地，放到我自己家里电脑的一个 cookie 里面去。所以要去做这样的一个同步的覆盖好。


如果说再一个，如果我们的 cookie 中的数据这个时候不为空，那么这个时候它就会有一种情况，如果说我们的两边，我们不管是 Redis 还是我们的 cookie 中，这个购物车其实都可能会包含有同一个商品数据，这个时候怎么办？这个时候我们是以咱们浏览器中的 cookie 为主。


写一下，如果 cookie 中的某个商品在 Redis 中存在，则以 cookie 为主，那么这样子的话我们会覆盖或者说是删除。 very stronger，把 cookie 中的商品直接覆盖。原理思中，那么这个的话大家可以去参考一下京东参考，京东其实就是这样子去做的，那么京东的话它其实是 cookie 和一个 Redis 的相互结合，然后我们把这个我们换行一下，可以看得清楚一些，那么这个其实是京东的一种做法，京东是结合了 cookie 和Redis，那么如果说是淘宝的话是必须要登录的。你如果说你不登录的话，那么你的一个购物车是不会让你去添加的，你一旦要点击加入购物车，那么它就会让你先去做一个登录。那么当然这种做法的话，其实也是可以去做的，有兴趣的同学大家可以去把这一块业务改成和淘宝一样的，那么也是可以的。


那么这个就是在 Redis 和 cookie 中两种不同的一个情况的一个相互的结合。那么另外还有第三一点，第三点同步到 Redis 中去了以后，那么这个时候的话，其实我们应该要覆盖本地 cookie 购物车的数据，保证本地购物车的数据是同步最新的，那么这个也不要忘记。那么这些的话都是在我们当前这个方法里面去实现的时候，我们就可以去写一下咱们的代码了。那么首先的话，第一步从 Redis 中获取购物车，第二步应该从 cookie 中获取购物车。然后我们在这里就可以来做一个定义，这边是shop，我们拷贝一下，拷贝一下我们之前所写的代码，这一段应该是get，拷贝一下，然后 Redis operator 操作的 Redis 类我们要住进来，放到它的顶端，其实这个位置你要放在中间的话其实也可以。


那么这样子就去获取了，然后这边还会有一个，那么这个我们应该还是要去继承一下，base， extends base control 了，那么下面我们就可以去用了，然后在这里还会有一个用户的ID，那么这个用户的 ID 其实我们应该是可以传入进来的，在这个地方 string user ID 可以让他去做一个传入。在这边我们就直接把它贴过来，那么这样子我们就可以去获得我们 Redis 中的购物车数据。


最后下一个是cookie，那么 cookie 的话我们在这边要获取，我们要通过 request 和response，这个我们可以也拿过来，这是两个额外的参数。然后在这边我们就可以直接写一下，这是一个 shortcut s t r，等于这边我们这样子，这边我们改成一个cookie，这样子的它的标识可以更加鲜明一些。这是。

ジャービス。

这个是从我们的哭。


Okay, you tell us. That's a cookie value.

那么 request 你是要丢进来，随后第二个参数是这个，随后下一个是一个true，那么这样子我们这两个数据全部都有，那么有了以后，随后我们就应该要去做一个判断。


第一个判断，这个时候的判断其实我们是要选择其一为主，在且注释的时候我们其实看得出来我们是以 Redis 为主的，所以在这里面的话我们把这个 Redis 拿过来，用它作为我们的一个判断。 string 与 tells 点 is blank，先判断它是不是为空。如果说这个时候我们的一个 Redis 中购物车的数据为空的话，那么在这里我们就可以额外的再去做一个判断。那么这个时候的判断我们是用于去判断咱们的一个cookie。写一下， Redis we call， cookie 不为空，直接把 cookie 中的数据放入Redis，那么这样子是最简单的一种方式，所以在这边就直接可以使用 UID operator 点set。在这边的话我们就要把这个把 k 拿过来，那么 fellow 的话它本身就是一个字符串，既然是一个字符串的话，那么直接把这个 cookie 丢过来，丢在它的后面，那么就可以了，那么就是它的第一个判断，也是最简单的。


好，随后来一个else，那么这个时候写一下，那么第一个判断我们来写一下。在这里面其实就是 Redis 不为空， Redis 不为空， cookie 不为空，那么这个时候需要去做合并，合并 cookie 和， Redis 中购物车的商品数据，如果说是同一商品，则覆盖格里斯。


这个我们先写好，然后它会有一个判断，那么这个判断是咱们的cookie，这是一个 is not blank，然后这边写错了，这边应该也是 is not plan，就说只有在它不为空的情况下才会去做一个覆盖。如果说两边都为空，那么就是没有任何意义的，不需要去做的。然后这里的话是 is not blank，这是合并这个内容的话，这里面的业务代码会比较多，所以我们暂时先不写。那么这边的话就是我们的，就是约蒂斯不为空，然后我们的 cookie 流通，直接把 Redis 覆盖cookie，那么这样子就可以了。


总共其实是有三项判断是要去做的，其中一个双为空，两边都为空，不做处理，其他的情况我们都需要去考虑的，所以在这里的话我们需要考虑的方面是比较多的，那么这个也是比较简单的。那么既然是进入到 else 里面来了，那么我们就可以直接去覆盖掉我们的一个cookie，那么在这边我们直接可以使用找一下 cookie 跳死，点 set cookie，一个是 request 一个是response，写好下面是我们的 cookie bell name，那么这个是 foodie shop cut，然后后面的话是我们的具体的值的话我们现有的一个 Redis 就这个直接把这个数据拿过来，丢过来，然后后面不要忘记我们加一个去，也就是 incode 我们要处理一下。


那么这样子的话，其实我们最基本的一些，除了两个都不为空的情况下，其他的我们全部都考虑好了，那么这个时候我们就可以来做一个测试了，我们来测试现有的两种情况。先看一下我们的这个Redis，目前 Redis 是有数据的，我们先清空，先把这个数据先删掉，然后 reload 一下， Redis 目前是没有数据，然后在我们的前端的话，我们刷新一下购物车，购车目前有一个数据直接在这里删除。回到首页，那么现在这个时候我是登录的一个状态，这个时候应该要先我们先来看一下我们的后端，我们后端首先做的一个应该是我们的 Redis 为空，然后 cookie 不为空，所以这个时候我们先做一个退出。好，退出成功以后，那么我们先来加上一些内容到咱们的购物车。好，现在我是加了两个数据，加了两个数据以后，那么我们的 cookie 肯定是有数据的。


来到我们的后端 Redis 刷新一下，里面没有购物车内容，然后这个时候我们在前面做一个登录，点击立即登录点，登录密码不能为空。 123456 登录好，现在是登录成功。登录成功。现在目前我们页面上是没有任何问题，还是这两个数据。回到咱们的 Redis 刷新一下，你会发现在我们的 Redis 里面暂时还没有购物车数据。这是为什么呢？一方面是我们的一个服务，我们的服务还没有去做一个重启，另外一方面我们当前这个方法在这里是灰色，没有办法去调用，所以不要忘记一定要去调用一下，调用一下以后，那么你才能够去做一个相应的设置。这边是有一个 user result ID 要拿过来的，点 get ID，然后 request 以及是一个spouse，这是同步购物车数据，这是一个登录，那么相应的注册也要。那么这样子的话我们可以来做一个重启了，重启之后我们再做一个测试，重置群中，回到页面刷新一下，现在我是登录的一个状态，登录的状态的话我们先去做一个退出，然后再一次进入到咱们的购物车。


现在购物车里面有两个数据，然后 Redis 来看一下，现在 Redis 里面没有任何的购物车数据，那么之前我们发生了一个小插曲对吧，那么这也是为了给大家加深一下印象，重新再来看一下，点击登录，登录一下现在数据是有了，然后打开我们的 ready 刷新一下你会发现数据同步了。


数据是同步到我们这里面来了，一个是儿童早餐，另外一个是铜锣烧，这个数据和我们在购物车里面的是不是一模一样，所以我们现在的第一个我们当前这样的一个看一下，那么第一个其实我们做测试 OK 了，随后我们再来测试第二个，那么第二个的话是针对于我们一开始的是 Redis 是不为空，然后 cookie 为空。那么这个时候的话我们这样子我们到首页退出一下以后我们是购物车里面是有数据，然后我们只需要去把这个购物车的数据去清空一下，那么 cookie 清空以后，那么我们在前端就没有了，那么当然如果说在我们的后端，后端肯定还是有数据的。


刷新是有数据，我们主要是看一下它能不能够把相应的数据同步的放到咱们的 cookie 里面去，点击登录，那么这个时候你会发现登录以后我们的数据就能够从 Redis 里面拿过来，那么现在在我们的前端页面里面，现在 OK 相应的数据在 cookie 里面有有没有了，那么这样子的话就是我们就已经是两块内容做了一个测试，我们目前的一个速率是可以达到了一个同步的。


