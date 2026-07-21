---
title: 4-10 批量操作 bulk 之 增和删操作
---

# 4-10 批量操作 bulk 之 增和删操作

[image](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/b179cb80-3212-4181-a626-60e890c4476b/SCR-20240806-fmai.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466X4R3KCPX%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T225149Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIC3BrWdqacVdPLojOpZCmLyM4snmLoco0tyu0liarWtzAiEAhpEiarXth55LHdEVu8oEq7ReCYBukNuPydYJGjXzSLQqiAQIxv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDGq5kOAk11vJJhsXJCrcAy32DMXbaflFNpH4VCHfcTi17xfW3sfIdansWap3KyY%2FFF1wSawCDQNPbVFX1B80NT%2Fo1I%2F%2BO267%2FisTOpVZaW12kmwgJHvoF%2BEVCoteZSLi%2FcdZdQ93CmOiqXrEnmOVVVBapBTnGorLjLsxUyd1GacEdr5quGypZ9%2FpbtNT6XcN8NWqgMADPuW4unjGoW%2FrzLAaXGjPP7jJ6shNMLhyDcP6amMJ9BOdLeXjLQmv%2BDmOj5G%2BSitD6EF4IFiQ4BtzpoqcFF%2ByuqwEls5USrB9mxZQsekSw1YBJsTo1%2Bda7aGHKotMewoP5AY78zVb0qNMP9dVTKQaJOyKfu6mbgJ5CZfFoMDTcIRZKxutvBDVNFQkuFpHwr1gwHj9NfX7CgscnzcnPzJuudaFAMUmxM0i01uIveeriQJ7lxr8qeG0QD10S%2FxVxAukrPYXDrqSARioBdoicoxAFaV2r1iJvTLG00ass4Hgtc4LpnXisQ2FRNWtI2iHhHtjbWR1F%2Bdgb22apaVxK6m3eYr5dyl6WLApB6%2FMY5km%2BrTk2NuPeK11UmrYcA5gN1pOIVlGygIu3LiHIDXTd8zOafR9PLK3F3%2BzfLAa4CwpVvseblgv%2BIqZ9bgJP6Nf8gW9tI8w3XyVML23%2F9IGOqUB3%2B%2FgIeewUXdGTUj%2BRfqbn3gTug3IEoTZ2EwkEGSZmkhLLFVaAz7n2kFOPdXVG4UohoTQziI0NKhEVGHAqOqtOLiX9e3YIJFxJNSGVkVJf20QsZMuw7eJ1LYaeWJdmLtkaA51VBFHw9J8261QMSymhGoisNX8D7SvyaGstQxU7v68S1jgkF3d0FNuvjmLIsi6cDM9dSjKs%2FepD3d3kJpdOvKRiXxp&X-Amz-Signature=ab61f41770ba94be6d7b07521de8c301c6ad60f314cf8d22a35aaf67ba53b4ab&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

那么上一节我们是讲了这个 index 的，接下来我们再来讲下面的两个 action 那么一个是 update 我们先来写一下 update 那么我们就做两个P 。第三个我们就删掉这个 update 是什么意思呢？它其实和我们之前有一个叫做下划线 update 单个去做一个批量的更新其实是一个道理。批量的更新是指的我们在这里面我们只需要去写其中的一个属性就可以了。那么比方说我们在这里我们要去局部的去更新它的一个 ID 所以我们把这个 name 把这个 nike name 给删掉。下一个我们要去更新它的一个 nike name 所以我们把 ID 给删掉。那么这样子我们就可以去做一个批量的更新。最后我们点击 send 那么这个时候他会报一个错。


那么这个错是什么意思？这个其实是我们的一个语法错误，就是说我们在之前使用这个下划线 update 去做一个局部更新的时候，就是在它的玻璃里面会有一个属性元素叫做 Doc 那么在这里其实我们也是需要去加上的。在这里我们可以去写一下它是一个 Doc 冒号，然后大括号，你要把这个 ID 2004 把这个作为一个 JSON object 付给我们的 Doc 那么这样子就可以了。同理下方的 nike name 其实也是一样的。 OK 吧，然后我们去做一个更新，你会发现在这里 update 它是一个 nope 它是一个空操作。那么下面一个其实也是一模一样的。那么这是因为我们的一个数据去没有去做一个修改对吧，我们的这样子，把这个 2004 它对应文档数据中的 ID 这个属性我们把它改一下。改成比方说 3304 随便去改。然后这个尼克利姆我们改掉，比方说把这个改成 name 杠 up 这种 send 点击。然后 result 在这里是更新。然后下面一个也是更新成功了，我们可以来看一下。
刷新一下，来看一下我们的数据。一条是 2003 应该是这里，2004这不是 2004 这一条是改成了3304。那么另外一条应该是2007，2007这一条它是改成了 name 杠 update 对吧？那么这样子我们就可以通过这个 update 也就是批量的操作来进行了一个局部范围的一个更新。


那么这个就是 update 除了 update 以外，那么还剩下最后一个就是 delete 那么 delete 操作它其实是一个删除，那么如何去删呢？那么要这样子，你要把这里面的这个 body 给去掉，因为吉利特它其实本身的话我们在之前操作单个文档的数据的时候，那么是在这里改成了一个吉利特，然后在这个 URL 里面去写上一个文档的 ID 就可以了。那么它是没有的，没有 body 的。所以在我们进行批量的删除的时候其实也是同样的道理，你是不需要去加上 boy 只不过在这里你需要改成比例子。


OK 吧，这边我们去删 0407 远之 send 好OK ，在这里可以看到 result 是可以成功的删除了吧，我们在这里刷新一下。OK ，那么这两台数据我们现在已经是删掉了。Ok 。那么这样的话其实我们总共涉及到四种 x4 种操作，一个是 create 一个是 index update 还有是举例子，那么我们都已经是做到了相应的实操。其实这些操作我们也可以把不同的操作类型放在一起，其实也是可以的。那么我们在这里可以来演示一下，比方说我们现在可以来删一个，把 01 和 03 我们都删掉，01，03把它给删掉。然后你还要去做其他的一些额外的操作。比方说我们在这里我们可以去额外的再去做一个创建。举个例子，我们可以创建一个8008，我们再去做一个修改，我们去修改一下。咱们的比方说有一个搜一下，我们搜一个2002，我这个代码就直接贴了，把这个 2002 改一下，改成 4 个2。好OK ，点击 send 然后我们的操作来看一下，这个是删除成功，下一个也是删掉了。随后这是创建成功，然后最后一个是更新成功，总共是四种操作，四个操作，三种不同类型。然后你可以再去做一个刷新，去看一下咱们的一个数据浏览。


OK ，8008实习增的，然后去筛了两条数据，又去修改了一条数据。Ok 。那么这样子的话，我们就是把它不同的数据的一种不同的操作都可以整合到一起做一个批量操作。那么其实也是可以的。那么随后我们可以再来看一下这个官方的文档，那么这个地址的话我也是会贴到文档里面的。这里有一个叫做代价较小的批量操作，其实就是 bot API 这个的话其实我们这个是我直接复制到文档里面的，那么这是它的一个语法，然后可以浏览一下。那么要注意每一行都要以这个回车来进行一个结尾，包括最后一行。


然后这里是它的一些操作，总共是有四种不同的 action 这样的一个动作。然后我们来卡戴卡，你是需要去指定 index 菜本和 ID 另外在这个下方这是它所贴出来的一部分的一个操作，这些都有了。那么这是综合了几种不同的 action 组合到一起，形成了一个完整的 bug 请求这是它的一个形式。然后在这里有一个请注意，吉利特这个删除的话它是不能有请求体的，它后面跟着的是另外的一个操作，这点是需要去注意的。那么刚刚我们也是提过了OK ，然后往下面看我们，找到最后有一个是多大师太大了，那么这个翻译的话我相信大家应该是很难去理解，就是这个应该是老外去翻译的。


那么他的意思其实应该是跟我们要去说明阐述，就是说当我们要去操作这个批量的一个 bug 的时候，那么我们的一个数据量我们的批量操作的一个数目应该是多少？其实应该是这个意思来看一下。就是说我们整个批量操作的一个请求是，它是会加载到内存里面的。那么我们的一个请求也就是批量操作我们这一部分的内容，它的数目越多的话，那么相应的我们这个请求也会，请求越大，它所占用的一个内存也会很大。当我们达到一定的阀值以后，那么它的一个性能就不会提升，反而这个批量操作它的一个性能会有所下降，这点是需要去注意的，所以它是会有一个最佳的值的。


那么最佳的一个值是什么意思？就是说它不是一个固定值，最佳的一个批量的条数。这个数目的话它完全是取决于你的硬件的一个环境配置，比方说你的 CPU 你的内存等等。另外和我们的这个文档的大小、复杂度，索引的搜索和负载整体的情况。所以它是一个综合性的一个情况。那么在这里他也会说幸运的是，我们是可以非常容易的去找到最佳点阀值。那么我们可以去通过一个批量索引的一个文档去做一个不断的调试，可以去尝试这样的一种操作。比方说那么在这里你可以把这里的一个数目你按照 1000 去进行一个相应的操作。那么 1000 的话那么逐步往上的去调，当达到一定数值以后，那么你的一个搜索你的操作的性能会下降的时候，相应的那么你的一个阀值就会达到了。OK ，这就是它的一个推断的一种方式。然后在这里它就会说就说当我们要去做一个操作的时候，其实我们发生的一个请求它是有一定的大小的。那么 1000 个 1 KB 的文档是完全不同于 1000 个遗照文档所占的一个物理大小，所以这个是需要去注意的。那么一个好的批次，批量的大小，在开始处以后，它所占用的一个物理大小大约是 5 到 15 兆。Ok 。那么所以这个其实，总的来说，其实这个就是你的一个批量操作，你的一个数据量不能够太大。如果说你要保险起见的话，那么每次你要去做一个商业的批量操作，那你就可以直接设置为 1000 对吧，你2000。那么你就按照两个批次，3000按照三个批次 1 万，那就按照 10 个批次可以这样子去做一个相应的查询，都没有。

