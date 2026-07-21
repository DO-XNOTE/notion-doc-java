---
title: 5-3 中心首页 - 订单动向完成接口联调
---

# 5-3 中心首页 - 订单动向完成接口联调

[image](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/47e552f5-96b8-434c-8b01-e88dd3e90299/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SRN7YEBO%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T224742Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCYUao4Xjy4t63otWU0Bb8iJSXjhaX9WToeZi347bsCVQIhAIplU8pzVgrjNmKl3Ww0F1FFkPTBhicHnFn4ZcmVb1E9KogECMb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1Igwl1PuBv9kda4GWX4Aq3AMw2TYrV%2FxBitMNVB6IaThJ%2BQUKqgfs1DuWdYR53yMUwzSJTnu%2FCopcVTxUPGDJidXcg%2Bu0eGGSrYy5LGWxdJavWfJWHQe%2Fzy0rVUh76K1v7clzZiKtQpRvGU1kw8Q6cAiSfxLH0AvIRaPiP%2FMvC8GvRBzNHvxEb6GSaBhso%2BJaknjyVQL9kD1t8aa6aMaMznPi%2BJsDYVsMR7q18fr9BgGorvSdHbXB7NccfpHfN1WkVeeUSNGHRLvzbiREO0bvRyefwddi3%2Bfqph1LtoJ4JyLRjfwgVV3VBF9OzvXWL2ttUWBZVMsDvpVchaGjNgyD%2FbXM56gH0YoCrwworXoXfSZCW3wCHtDxT9OAaJaH5Vu4HEl7ESM5J0odDMAGt39JA2NkqG48xXlcd23JN3BuwfzGa9CDmlo%2BFafkittpWN95yJ3UOs30HdWYQ0dLeN6ClM3nBbdlEy4aofY1ksUNYIiJmHSC9IjYEreaR1AZL5s2Mmolfj%2F%2Faa%2F894gY%2Fr1gmMtO8zurEhd0hXLrG3jTu47gd9ZuAY3LK71Cvigizam6TEdNjxOX7xcZzSmxbk3Irm93lqs8UnOuP%2FDbjAsIxTkCz875OGNgp1M5oCQuBMRN%2BzVLHtFJNN2njoWaUjDOt%2F%2FSBjqkAQOcLuA2%2BAMKvCWL%2FXgxdWE041f2tr44GfyIfRxvaOw4jEJ9YWfk7TKMj6oOWQirTERUNym1XLYP4tYnp8Zwdjw0e4pjShT41zfug3VaV8V215LrA9DYC4QEj2DCg89jkOSyeOkUb5uIr8HEM1J8R0mVpq55axhUYsvCsUbubMDc0s1CKCTfPWNtIyZBbwh1HBE5vz3ZWjBgMRETJ5Mb6dq%2BMlCa&X-Amz-Signature=c58cad954a322ea80c1b120467bd7e81a93caf03e0be03bfdadbedb8370ae17b&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

前两节我们是完成了订单概况，是根据不同的一个订单状态，它的状态数在这边进行一个展示。接下来在这个页面还剩下一个，也就是订单的动效。订单动效其实也就是我们当前用户中心的一个最后的功能了。用户动向。我们可以先来看一下生产环境。在生产上，在这里会有一条订单，这条订单是这样子显示的，他会说这笔订单号是多少，它的一个状态是该订单交易成功的时间进行的一个展示。其实这样的一条记录其实就是我们的一个订单的状态表所对应出来的一个信息。只要是这一笔订单，它的订单状态发生了一个更改，它的动向，在这里我们就可以去进行一个展示。并且在这边其实也是以一个分页的形式去展示的，但是需要去注意这里的一个需求。我们并不是把所有的订单状态全部在这里都会去做查询，我们只会查询 2030 和40。可以看一下我们的订单状态。这是订单枚举，对于我们来讲，我们在动向里面只需要查询这三个状态就可以了。在付款完以后，这一笔订单会正式进入到一个订单流程里面，随后就会进入到 2030 和40。 40 是交易成功，交易关闭，我们也没有必要去显示。所以我们会查询 2030 和 40 这些状态的一个订单状态。这是对应的一个动向记录在我们的首页，在用户中心的首页去做一个显示就可以了。


OK，好，接下来我们就可以去写一下咱们的 map 了。在这边其实我们又是一个多表关联，所以我们也是要写到自定义的 map 里面去的。我们还是一样。先写一下circle。先写circle，这是我们之前所写的，我们新创建一个，新建一个，到这查询里面。新建一个查询。先保存一下。这是用户中心订单动向，好确定select，放大一下，写上一个 select 星号from。我们应该是 from 一张 from order。这是我们的订单表，别名取名为 o left join。这是关联订单的状态。其实和我们上一节所讲的 SQL 语句这两张表都是一样的。这两张表也是我们平时开发中使用的比较多的。


好，再来一个 o 点 i d 等于 o s 点 o 的 i d。好。再来一个 where 条件。首先一个我们的订单是不能够被删除的，所以 o 点它有一个 o 点 i b， o 点 is delete，它是要等于为0，是未删除的。除这个以外，还要再加上一个and，这是用户的ID， user ID 等于拷贝一个，这是我们之前写的。把用户 ID 写过来。好，这是第二个条件。随后再来一个订单的状态，订单状态是 o s 点status，在这里会涉及到 2030 和40，所以我们直接写一个 in 就可以了。


20 30 40 好，OK，好。除了以外，我们是需要做一个时间的排序，应该说是根据我们订单 ID 的一个排序。我们来一个 order by，根据 OS 点order， order i d，使用 d s，c，这样子其实就是一个倒叙的排序。OK，刚刚我们说的是一个时间，其实这时间并不能够很明确的进行一个展示，因为时间它本身它是会有不同的列。因为我们在构建订单状态的时候，订单状态里面像它的一个发货时间，成功时间，它都是由一个单独的列去定义的。所以我们在这里做一个排序的时候，以 order ID 进行一个排序就可以了。因为本身 order ID 里面其实也是带有一个时间的，可以看到它前面这几个是一个日期。


OK，好，我们在这里就可以去发起一个查询的，点击运行查询一下相应的数据，我们在这里全部都能够展示到，但是这里面查询出来的一些内容其实列太多了，在我们前端用不到。在我们前端里面，其实只需要把订单号，订单的状态，另外它的一个时间涉及的比较多，不同状态下都会对应的不同的时间，你要把时间也要拉出来。所以在我们做查询的时候，我们是根据特定的一些内容去做一些特定的查询，在这里星号就不去这样子去写了。查询的内容我预心也已经是准备好了，我就直接贴过来了。在这里可以看一下。


我们是需要查询这些字段，首先是订单ID，订单状态，下单时间，支付时间，发货时间，成功交易的时间，订单关闭的时间以及是一个留言时间。这些内容其实都是在订单状态表里面的。在我们前端，它所展示的内容也是根据订单状态表里面的内容去做展示的。所以我们查询出来以后的一个对象，直接就是一个订单状态对象了。


OK。保存一下。我们运行 OK 可以看到查询出来的内容其实都是和我们订单状态相关的。OK。好，这样子我们就可以去把这些内容推到咱们的一个自定义的 map 里面去了。回到我们的项目，在下方去写一下。我们把 select 语句拷贝一份，把 ID 改掉。


这是一个 get my order。这个叫做 trend 劝的，是动向趋向的意思。趋势传入的参数。我们也可以定义为是一个 map result type 传出去的。由于我们本身和订单状态相关，所以在这里我们直接可以把一个订单状态对象给拿过来。在这边我们去找一下。找到这张表所对应的对象就是这个。拷贝一下他的reference，配到 result type。好。OK，好。下方的查询语句，我们可以直接把这一段内容拷贝。接过来。贴到这里。贴过来有一段，删掉，格式有点问题，把格式稍微改一下。在这里我们所要去做的一个查询条件，把 user ID 去改掉，改成这里的。把 map 给拿进来。在这里其实只有一个参数。在我们做一个马白底斯的映射的时候，我们传入进来的参数可以写一个 string 类型的 user ID。当然使用 map 也可以map，它兼容性更好，以后可以扩展更多的参数。


OK 好。这个方法在这里我们就写好了。写好之后我们是需要去写一下它的 map 映射，找到命名空间。在这里在这里我们就可以去写一下public，返回的是一个list，是 order status。好，再来把我们的一个ID，这个 ID 是直接拷贝，把贴过来传进去的，一个参数就是map。好。OK，这样子我们 map 自定义的语句就已经是写好了。


