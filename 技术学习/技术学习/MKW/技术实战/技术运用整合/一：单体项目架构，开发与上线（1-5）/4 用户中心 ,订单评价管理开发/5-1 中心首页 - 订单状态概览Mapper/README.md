---
title: 5-1 中心首页 - 订单状态概览Mapper
---

# 5-1 中心首页 - 订单状态概览Mapper

[image](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/2cf61bd2-0f6c-4020-b1f2-3d4afa1c159d/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662SKFFDTT%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T224741Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCg%2BvJpTOQqBqH1UY8RUZxuTVxnTa6sRddOrn65MfG36QIhALHvIAq2uhdTXVbTAT8Slhq6XPRv5RFfj7Oqw7eCidd0KogECMb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1Igw0z4oYY1bcLks59ukq3ANGdkZ5ke32JR7LE8lGy1r5KMSO0tYzyJyz%2F27FiOp7VifXOj6zUF5kiQHca3ddqIZ2%2BaCRtp5mAPCfu6AtCf%2Bv1OpapMDUTtpa5Pcd5kU9HIucjOCD30HPPrZJfEOTVsYDtAc3AIk%2BiH2DokkIYZCLIPcfCTxG2KeDiBqieNTZ50p%2FY9ruKPolJzgnP%2FDgLchDw1ZULiwTOkc6kcs%2BrQYDLblpU9qnam2wZLZcba771v6Ejd86U2WOTE5DWUEmFNGv35qvCbN2WzsaNN8tKvCaQZXJb3OWVB8VcZdhHgx0EiaFHtnt5l77g8Bsrj0NVOoQsnKOz2f4kitr%2F%2B1pVEGXqy4yhz%2BrF%2BY0536MPwpdEqIS0Ez8oupP0EnqbAZnS%2FZbteyncgscRUIN9D8V7K195tqQXJMJu7YD0OItTV6OvQM33MCIC9ZPWwPXkBJ5N2AyC%2FY4TxaTr3Wdv9tWpVqbsQo56ye9mAqeTi18NCnsG4VPPgHrw4TPoI%2BeHsgqOWVfjxW09WLErNKtMUB4d%2Fq%2FMXNANPwxscEm9QaYLOy%2F8WULVW7u2scNeWGWx9AmA2uhh%2F%2FVK%2BezJfuLIBIbFv4%2FxT3zNQue2scDtCSqi3eKWpOwSDJglAQ%2FdQJRGDCWu%2F%2FSBjqkAemkVvK0ExbQDt19lAiY%2BRfGGWY7s2Hh0LE9ZFmNh2I2A%2BYwNU1xF%2BG%2FGn4%2BshSxnPKSAJMNiOqEcibh2YCZcwdZYHMr3iZpC8S1moI2rdCo1LNx1jBkt%2B8PoqM8lCp8uF9zw2LdELoVFKhtswfMdcTodcB%2FZGSiGhmsVmT8rVo9ImCj1j%2FtcQrO53XAoMR01ynziauNH4k23CybRP35HTBpac5E&X-Amz-Signature=8746da27a125d03f96c629cd1be9369e04e5fa766dccd7dccc6827f197567b32&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

前面几节课我们是完成了用户评价中相关的一些功能，包含了用户在不同订单中不同的商品进行一个评价，并且你也可以选择性的去进行好评差评。当用户发表完评价以后，可以在我的评价页面去看到你历史的一些评价，在这里面也是包含了一个分页的。接下来其实我们到这里为止，在这一块内容，也就是用户导航，我的信息，收货地址，订单管理以及是我的评价。这几块内容其实我们都已经是完成了。还有一块内容在个人中心，用户进入到我们个人中心的时候所展示的一个中心的首页，在这里面也包含了两个功能，一个是我的订单，另外一个是订单动向。


接下来我们把这两块内容去做一下，在这里我的订单其实是一些用户的非中泰订单，会在这里进行一个展示。比如有一些订单下单之后，他没有付款，他就是等待付款，像待付款、待发货、待收货、待评价这些等待字样的一些状态，在这里他都会以一个数字的形式去进行一个展示。我们可以看一下生产环境。


生产环境上，目前在订单管理里面有两条订单，既然有两条订单，其中有一条是交易成功，并且是已评价了，这样子在个人中心里面，在这边是不会有相应的数字的展示的。只有这一条，这一条是一个等待付款。等待付款在个人中心里面就会有一个一，如果他付款完毕以后， 1 这个数字就会到这里，在会有一个待发货，发货完毕以后会有一个待收货，当用户确认收货以后，这样的一笔订单他还没有评价，所以在这里又会有一个评价。接下来我们就把这一块的内容可以去实现一下。


在这边我们可以先去写一下 sql 语句。 sql 语句其实又涉及到了多表关联。在我们也是涉及到两张表，其中一张是订单表，一个是orders，另外一个是订单的状态。这两块是需要关联去进行查询的。所以我们在这里还是一样去写一个查询。先把保存一下，我们可以取一个名字，这是一个订单状态数查询，这个是用户中心的，点击确定，保存一下。在这边我们可以去写了select， select count。在这边我们写一个1，你可以写 count 星，也可以写 count 1，但是一般来说我们不要写 count 星，这样子太多了。


from 两张表，一张是订单表orders，取一个名字叫做 o 好。随后下一张表进行关联。 left join order status，好给他一个别名，叫做OS。再来一个on，一个是订单的ID，等于 OS 点 o 的 ID 好，这是关联。随后我们加上一个条件 where word 就是用户的ID，用户的 ID 是必须要加上的。 o 点 user ID 等于。我们可以去找一下。


找到订单表，里面在有一堆的 user ID，随便拷贝一个。这里面其实都是我们当前登录用户所做的一些操作，所以每一个用户 ID 都是一样的，拷贝一下就可以了。贴过来。这是第一个条件。第二个条件是根据我们订单的状态。因为在我们的页面里面其实也能够看得出来，不同的订单状态你都应该要去做一个查询。所以在这下方我们要加上一个 o s 点 o 的 status 状态短语。打个比方，我们就使用 10 熊 10 好，这样子，其实这两个我们就能够查询出来。


此外还有一个是用户的待评价，它其实是要满足这笔订单必须要成功。在这里我们改成4040，是一个交易成功了。还有一个应该是 o 点 is comment。短语0，这是未评价，这样子是可以去查询一个等待评价的订单的。运行一下，现在我们看似是 0 对吧？没有关系，我们把改为10，下面我们就注释掉。再运行一下，可以看到这边的数量现在是有三条， 10 的话是一个代付款对吧，所以代付款现在是有三条。


记录好写完之后我们就可以把这些内容拷贝到 map 里面，去做一个自定义的查询。我们先回到咱们的项目，这里面现在都是和comments，也就是和评论相关的，我们可以把所有的都关掉，我们重新的去找一下。找到我们的一个订单，有一个orders，map，custom，另外还有一个对应的叉描文件，打开一下。打开以后在这里面我们就可以去做相应的查询语句了。我们在直接拷贝一个select，写到最下方，这中间的 connect 语句就不需要了，从我们的里面拷贝一份出来。好，拷贝以后我们先拿掉，把格式化一下。好。OK。


首先我们先来定义一下咱们的ID。我们可以取名字叫做 that my order status COUNTS，查询我的订单状态的数量。传入进来。在这边我们也使用一个map，也就是这个对吧。使用 map result type 我们要返回出去的。在这里其实我们是 count 1， count 1 它拿到的是一个整形，所以我们在这边就没有必要再去定一个 VO 了。我们可以直接通过一个Int，这样子它就可以返回一个整数出来就可以了。好在这里我们还需要把两个参数都改掉。由于传入进来的是一个map，所以我们直接写一个 map 就行了。 pumps map 点这是 user ID。另外一个是用户所传入进来的一个订单的状态。 order status 好OK，这是两个条件。还有一个我们的 is common 用户是否是评价过，应该说是待评价的。再来加一个 and 这个 and 去掉，因为我们是要做判断的。传入进来我们可以传一个 is comment，如果为空，我们就直接查询这两个。如果 is comment 不为空，我们就可以把附带的一个条件给加上去。所以我们在直接使用 if 判断的一个条件标签写上就可以了。


test 在这边我们就可以直接使用 map 点 is comment 判断一下它是不是为空，如果不为 now 不为空的情况下，在这里我们就可以去加上一个and。


Oh dear, you just use comment.

短语再把这个给加进来 is common 贴上。这样子就可以完成我们的一个查询语句的操作了。OK，好。现在有了这样的一个select，以后，我们还需要到达它的一个映射里面，去把对应的方法要去写一下。 public 返回的是一个 Int Int 方法写上，再传入一个参数，和上面的一样，直接把map，把 map 贴过来拷进来。这样子这个方法我们就写好了。好，这样子我们 order map custom 自定义的map，我们就已经是写好了。OK。

