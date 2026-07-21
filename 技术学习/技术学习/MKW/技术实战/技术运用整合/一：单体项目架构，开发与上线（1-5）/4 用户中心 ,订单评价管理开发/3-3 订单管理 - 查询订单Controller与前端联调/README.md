---
title: 3-3 订单管理 - 查询订单Controller与前端联调
---

# 3-3 订单管理 - 查询订单Controller与前端联调

[image](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/0a4b2c55-fa3e-41b1-b3f7-f00149c37a46/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QSDYTQ6H%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T224730Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDKOEgnzWf8nSCmlUKsxv6w5w8MxHGqz3Zr1EOEksKtowIgJhq8mYNBa6%2BQ3Pq72QY0ONNAvgFMQf4EHFGzNW%2FUqKQqiAQIxv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDFboLLko0z0IfTo0ESrcA3fXL3kcDsk5RBAhL3o3xdPBspSr5oI3OUVE9bHAbavyzoiDOAKqbHv4U1rQr2qN3qcijbw%2BTIiJ4FzeXe0gYujs0guUH48WneeSC2kiLv9C%2FnObrfZZ3fKlSfpnssg2jyZS9Qg5kCqLYJBa44XgPkbJU7dOWGLy8ZaADEIWFpN5jkOl%2FDvXgHn%2Ft3GvvF8EFWX0kuoDhtKKewhcslnfXHKsahoT4AhkV0%2FWXO%2FYY27xj9tDEe%2F6EeDb94B1ky%2FPmPIZXFoS9961NhVMGguRqY2mKgEe0rwYsM1MJ6dk%2B%2BFtAhfxm7m5dYLPYMtET18rIh7Z%2FCCNWFGwNHEsC%2BN8BwDbRoLkIrMwh7tenGtbLwne4gkBqoSVEkqNLuzxi9fRsGnZtYC48aGkCD3Ql%2FyuFgcK6JzLzwIYPCCYdXPH45UnR8m8eUW7egYhrnxb9aVy7U7%2FVVmjvAt4WxTvFZJYtJ3Ut9S%2F9b%2FES%2BBbq9iUbxgy6qgwRaiaiyg7%2F%2F8hpMPSuDlIeC6X36PH5tRCKxlr%2BxyceQIM0j6DKT1GCNqARUJQ7YEcYv1F0azYE28CEIQzbEej7Q7P%2B2k%2BfiVsPOUnTo0dBXqPxinBiBsEImuO7ScOrsGDF5%2Bw3IdojJYNMJ63%2F9IGOqUB36Y1VD0cR0yP0Gdzf98%2B%2BI7ck938FJg2by%2B3NedPLEf7Rih1nGs4sEjattI27LvJCb%2BPwtDEIDhx%2BbwHNp5XFx6GZB%2Bj65%2F5Y8Sr1tV07%2BJwWW0YtIua5rGOYjvE3NLWcmBwlrUEXGe56rxlwogCOIdsE3PaiqAYTBWcYNOAvMPgN9tK03Qrb5EnIG6XY33Mgw800iRlcLwWvmsSJwOt5OStSvuf&X-Amz-Signature=cce40a0703cc45891f1929605cdc1ebc8dc5dfcd0ab4e6aac00aaa8282b5c868&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

上节我们是写了查询订单信息的一个service，就是Mapper。接下来我们就需要去编写一下controller，和前端去进行联调。在编写 controller 之前，我们先到前端先看一下前端的代码，找到order，点HTML，这个就是我的订单它的一个页面。找到created，再找到 render order list，这个就是渲染订单列表信息的一个方法。搜一下，在这里找到有这个方法。传进来，会传入相应的内容。一个是订单的状态，然后是配置和配置size。在这里会构建一个post，请求传过去的时候相应的内容。一个是用户ID，一个是订单状态，这个订单状态它可能是为空的。另外我们的一个配置和配置 size 这些其实都要传过去，这是一个路由的地址，所以 control 了会根据这个地址来。


最后下方这个是成功以后的信息，是进行了一个渲染。在这里是拿到了一个 order list，一个列表，在这边去进行一个循环。循环的处理是时间，因为我们拿到的一个时间在后端直接拿过来是一个 date 类型，他要去进行一个格式化，成一个年月日时分秒这种形式。格式化了以后，再把新的一个 list 直接附给我们当前的一个页面，里面，它就可以去做到一个循环的渲染了。


好，接下来我们就来根据路由去把后端的一个 controller 的去构建一下。先打开咱们的后端工具，在这里面我们应该要去先创建一个Ctrl，我们可以先拷贝一份，我们把拷贝一下，直接在上面去修改。 my orders。好。首先一个我们要把它的一个路由在这里，它的一个 request mapping 先去改掉。在前端，前端是买orders，直接把推过来。 API 区域改掉，这是用户中心订单，是我的订单。后面的 tags 改掉好。 service 应该是买 order service 好住进来。下面的这些内容我们全部都删掉。


在这里我们重新去贴一个新的方法。我们还是找到以前的，因为我们以前是写过分页的对吧。所以我们找到这是。我是找的是iTunes。 Ctrl 的，在这里面是会有分页的，找一下。在这里找到一个商品评论的分页，把这一段内容直接拷贝一下，贴过来，再去做一个修改就行了。


首先来改它的 a p i operation，这是查询订单列表，全部都修改。请求方式。在这里看一下前端。前端定义的是post，因为其实在我们后端来讲，其实这些都是属于用户中心的。为了更加的安全一些，我们可以构建为post，这样子会更加的好一些。


在这个地方，它的请求方法应该是 query 的 my orders， query 推过来。好，下面一个应该是用户的ID， user ID，贴过来，它的 value 写一下，这是用户 ID 一块的，为处是必填项。下方下面一个应该是订单的状态，从前端值贴一下 order status 贴到这个位置，它的类型也是 Int 型的。好，这边的 failure 改掉，它是一个订单状态，有快的可以为false。


好，下面的是 page 以及是 page size，这个保持一致，不去动就可以了。在这里首先我们要判断一下 user ID，判断用户的 ID 是不能够为空的。判断一下配置，如果为空，默认从第一页去分页。再下一个是我们的查询分页的每页所显示的记录条数，在这里我们定义的是 10 条。就是comment， page size。把改一下。我们这样子把改为common，也就是通用的意思。通用的一个分页，它所定义的一个记录数，我们改成 10 条。在这里我们就可以使用 10 条了。当然我们在之前所写的一个 Ctrl 了，肯定是需要去修改的。之前是在 items 这里，你是需要把这一段内容去修改掉。好，OK，返回到我们现有的。在这里来看一下。我们应该要使用 my order service 去做一个查询，点 query my orders，第一个是 user ID 传进来，第二个是订单的状态，随后就是配置以及是配置 size 了，这样子就 OK 了。好，我们格式好，拿到了一个 grade 之后，直接抛给前端，让前端去做一个相应的渲染，这样子就行了。


好，现在我们就可以来做一个测试了。首先是需要去进行一个全部的 install 完毕以后，我们再来做一个重启。好，重启一下。好，重启成功了，我们到页面里面，现在我们回过来，在这里点击订单管理，点一下刷新一下。这个时候你会发现在这个页面里面是一闪而过的，很明显我们是出现了一些问题，出现了一些错。我们到后端来看一下。在后端可以看到在这里有一个 there is no setter，有一个叫做 item 商品规格的一个ID，在 my suborder item fuel 里面是没有的。也就是其实我们并没有使用到这样的一个ID。我们返回到 map 去看一下。


在定义 Mapper 的时候找到我们刚刚的一个 custom order Mapper， custom 遇到异常我们就要去分析相应的问题。在这里是一个 item 的规格ID，微博 ID 是应该映射到里面买 sub order item do 里面。在这里面我们没有定义两种方式，一个是为它去新增一个，另外一个我们直接把查询里面的规格 ID 删掉就可以了。两种方式都可以。在这边我就直接去删掉了，因为在我们的前端应该是没有使用到，所以我们的 CEO 是没有的。


把这一行直接删除以后，我们再来重新的去启动一下。必须要注意要install，因为我们改的是 map 层的 map 层，在 install 了以后才可以在我们的 a p i 的子中程才能够被使用到。好，重启成功了，再来测试一下。刷新一下。这个时候可以看到我们当前页面里面的一些数据全部都能够查询出来了，OK。并且它也可以带有分页，可以看到一页往后面分数据是会跟着变的。OK。现在我们订单管理的查询的内容信息以及是分页就已经是 OK 了，但是它会有一个小问题。这个小问题我们在下一节来跟大家去说一下。大家可以在这里去观察一下它的一个结果集，看一看你能不能够发现它是存在什么问题。OK？

