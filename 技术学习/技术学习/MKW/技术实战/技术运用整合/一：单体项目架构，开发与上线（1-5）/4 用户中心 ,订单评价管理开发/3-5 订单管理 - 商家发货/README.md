---
title: 3-5 订单管理 - 商家发货
---

# 3-5 订单管理 - 商家发货

[image](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/a66f1cfd-a05b-4e4f-a31e-02df5d6c20fd/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666V47UXAT%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T224734Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCgwyJ9ym4GHpHe023LYUyigzCKy7sJ0PpiCiIApaAD%2FAIgJFByigjh7HUC8wZB2IvwrVKE3EfhFUvbnkLqWe2SumwqiAQIxv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDOkFwyb%2FaOfTjGMJeSrcA%2FEorfnLG7%2FLwrH6aLgKoY5agUiq1O%2BOnMyAEapPDKOOZiwmXSY3R9hIIeYYY7rNA%2BEIw7gZQObv%2BWv9gSqXwTbWVI8uv7hmSe9dmtA5zyVd2LvBu41O9Fvel029Nw7gvYWSG8RAjjjY4G5JKyKvW7uBVFw0f%2BjvHMxgKC%2Ff6f1%2BLtBVS0qwEb7vwSiwbZ82VqcYH4Sx5DwvOzlzjK8hytfd8CfMq7l3Lj4mCT%2BPn728HgFXTHh3NCuwV02zfavnAYkR3PfsqRtSk0AQ4%2F6ycxUYbDLZw4XgWgcN4LSQfDjlfEzJNwwG5qRtQ9cfCbTrHgIoIIM4bnA1OyEXCbycIUB8wfljRdJjgWepm7v%2FPoq06upMOe00Rx8Gbg3C2LUQJXd2hbqoEd9fNWZadPgO8CJYBYVTAuLtFdXnPh5T6fSN9VSc%2Fi6wxSINLbA5p2FKV5FXskv3svbPv0S2rb6V%2BEgtbUvey6CQLFBH7eZ5QDRCMZTmgMiuTIhON1jYgOjcRJrvqYb8PuxT7ka%2BlyRRNvj9HgzU21nzaxL1sZtctceVhLuT9IzJHsp2XvnQ1JVoG0XiY3xrZ61mn0umNItsR1uP%2FbnrmI%2BGdtWiuV3tmhF9dPlhQfyOfxYqgCHsMP64%2F9IGOqUBYA5tBf8Cfh3Jlk%2FpZPrfXJzPCshjG%2BSTP3ThQEBkziJkBTnkr27HOXl%2FoGo4mZRt43S%2B%2BOfMuCSdZy8%2FeapH%2B4HBxUf181hysbD%2FqUT%2BRD%2BhgyTxJHdoascFfOYK9HAMWF7NH7E%2FGO0vSFfA6vRCY6%2BIHenr6mx2FS9Kx1eIuaCWvMenjorfpOOtN8tYzTadCLeGFSVrPVf5nepWTjLJeUeX2Mu5&X-Amz-Signature=69e733b3c6442ef831a7f3deda7747ae50583c48e62d0e00779c48b8ca1af82d&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

上一节课我们是完成了订单管理的查询，并且查询是带有分页的，但是它会有一个小问题，这一节课我们就把小问题来解决一下。首先我们先来看一下咱们在 Controller 里面所定义的一个记录数。在 Controller 里面我们定义的是一个 10 条记录。 10 条记录在我们的一个页面里面展示的时候，应该在每一页所展示的订单都应该是有 10 条。但是我们现在可以来看一下，在这里是有一条、两条、三条、 4 条、 5 条、 6 条，总共是有 6 条订单记录，下面就没有了。


我们可以再来看第二页，它会有一条、 2 条、 3 条、 4 条、 1 条，它会有 5 条订单。很明显，现在我们每一页所展示的一个订单的条数不一样，都不是 10 条，它可能是5，也有可能是6，都不一致。发生这种情况，它肯定也会导致我们的一个分裂的。总的记录数会不一样，在这里它所展示是有 50 条，但是在我们的数据库里面，我们可以来全选看一下。


其实总共我们的一个订单表，这里面是有 26 条记录，但是在我们的页面上，很明显它有 50 条，很明显是出了问题，对吧？导致我们分页的数量不正确，这是不应该发生的。为什么会发生这种情况？主要是因为我们的一个订单表和订单商品的一个多表关联。一对多的关系。一对多就会引起一个嵌套。这个嵌套是我们在 map 层去进行一个设置，在这里它会有一个item，这些商品，我们实际上它嵌套成了一个 SubOrderItemList，是放在了 MyOrderVO 里面的。是这样的一种情况。我们来看一下官方的一个说法。这是官方 Mybatis PageHelperer 在 github 的一个页面，这是它的一个地址。作者在这边文档里面写了一句话分页插件。它不支持嵌套的结果映射。嵌套它是显示不了的，会出现一些问题。主要是由于嵌套结果的方式会导致结果即被折叠。因为重复数据是没有的，因此分页的查询结果在折叠后总数会减少，所以无法保证分页结果数的正确。


在这里可以看到，其实在我们当前，这一页其实订单应该有 10 条，但是它却少了，每一页都少了。这是因为我们的嵌套每一个订单里面都会有多个记录，我们可以来数一下。在这里这一条订单它会有两个商品的，我们把它们都加起来是两个3456，7890。你可以看到，其实它是把我们所有的一些商品，它是以商品为主进行的一个分页的，所以它总共的每一页所展示的一个关联的订单表，它的数据都是 10 条。


OK，如何去解决这样的问题？其实也有相应的解决方案的。第一种我们可以在前端去进行解决，我们在一开始查询出来的时候，我们只要去查询订单表。把订单表查询出来以后，在这里我们可以参考懒加载的一种模式，拿到了我们所有的订单的 id 号，总共是有 10 个，再把这些订单号传到后端，再去进行一个查询，把相关的一些关联的商品信息给查询出来，再一次的在我们的页面上去进行一个渲染。可以使用我们这种方式去做。还有一种方式也是通过 Mybetis 去进行的一个解决。和第一种方式其实是类似的，只不过它是可以通过它内部的一种方式去实现的，也是通过嵌套。只不过在我们查询的时候，原先我们在这里做的一个查询是通过一条语句去查询，现在我们把这一条语句进行一个拆分，我们先查询订单的信息，再根据订单信息里面的 order ID 去把它所对应的一个商品关联信息再去查询出来，就可以做到一个解决了。


OK，好，接着我们一起来实现一下。由于这个方法可以使用，但是会有一些小问题，所以我们这样子。在这里我把拷贝一份新的，原来的我们就废弃。我在这里取一个名字叫做 do not use。好，OK，我们就在这个方法上去做一些相应的修改。首先一个我们先查询订单相关的信息，所以我们的一个商品是需要去删除的。把 oi oi 就是 order_items 了，把这些内容全部都删掉，删掉以后不要忘记有一个逗号要去掉的。随后在多表关联里面，原先是 3 表关联，现在是两张表，所以我们可以把 order items 把 left join 给删掉了。以后在这里面其实我们就把没有必要用到的东西，没有必要用到的表给删掉了。删掉了以后在这里。


这边是我们所对应的买欧德斯皮优是一个 ResultMap。它在这一块内容是没有必要去做修改的，因为这些内容本身就包含在了这里。OK，所以这是第一次的查询语句。另外一半的语句我们是需要去重新的去构建的。我们在这里。在 clash 里面，它是嵌套的一个list。在这里面其实它还会有一个额外的属性。是什么属性？我们可以到这里去写一下。我们写一个叫做select，可以看一下。这是一个新的属性。 select 是代表一个查询，也就是当我们在查询完毕 query 买 orders 的时候，它会发现它当前的 Mapper 里面会包含一个 SubOrderItem。 list 会包含一个属性，这个属性会根据 select 里面去做一个相应的查询，所以我们对应的查询语句应该写在这个里面。在这边我们可以定义查询语句的ID。比方我们可以取名字叫做 getSubItems，我们就取名字好了。相应的我们就应该在这个下方去把对应的 select 去写一下贴过来，这样子语句就会被调用了。


OK。但是我们的一个商品里面要和订单去关联，它必须要传入一个订单号，所以我们在这边我们还是需要去传入一个相应的属性值。这个参数其实也是某一列我们写上一个column，某一列其实就是从里面去获得的，也就是这一列的数据。把这一列 order ID 给写过来，写过来以后就可以作为一个参数传递到 select 语句里面去了。在我们来换一个行，这样子可以看得清楚一些。好。OK，这两个就是我们在原先的基础上新加的两个属性。好，随后我们来完善一下。 getSubOrderItems 到下方，在这里去完善一下。


首先我们已经是定义好了一个ID，定义好了 ID 以后，在它的后方，你是需要去传入一个对应的参数类型。由于它的一个订单ID，它是一个 string 类型，所以我们在这里可以去写一下。找到 parameter type string 写一下。另外它还会有一个对应的 result 菜盘。它返回出去的一个类型是什么类型？其实返回出去的类型就是这个类型。直接把拷贝一下，拷贝了以后贴到这里。好，在这里面我们就可以去写相应的一个思考语句了。SELECT。要查询哪些内容，我们只需要把之前删掉的这一部分内容全部都拿过来。贴到这里。贴过来以后，这些内容本身在我们这张表里面都是在 order item 这张表里面的。直接写一个from，再来一个，加上一个条件，这个条件先把表名先写好， orderItems  oi 好。再来一个条件 where 条件就是根据 oi 点它有一个 order 下划线ID，根据去查询，我们会传入进来一个string，也就是 order ID。所以在这边把给写一下。


o 的 ID 就是我们在这里 collection 中所定义的 column，它叫 orderId 的名称又是从这里面去找的，所以相应的值就会被拿到。这样子其实我们就把原先的一条语句拆分成了两条。OK，好，现在我们就可以来做一个测试，看一下我们在前端所拿到的一个分页数据是不是正确的。在这里我们是需要重新的去 install 一下。好， install 成功。再来一个重启。


好，重启成功。我们回到页面。现在我们再来做一次刷新。现在是刷新成功了对吧？数据也展现出来。我们往下面一行看。现在其实我们会发现我们的订单数现在其实是增多了，比刚刚明显要多了很多。在这里分页现在总共是有 26 条记录。来看一下我们的订单表，我们在刚刚也看了，它是 26 条记录，也就是现在我们拿到的订单数是没有问题的，不再是 50 条了。好，再继续。很明显，如果是 26 条，按照 10 条来做分页，每一页都应该是显示为 10 条。在第三页是总共有 6 条订单记录，我们可以来数一下，有一二345，6，总共是有 6 条记录。


OK，现在其实我们就已经是解决了这样的一个小问题，这一点大在大家平时的开发过程中一定要去注意，尤其是在你使用 Mybatis 的 PageHelper 这个插件的时候，肯定会有这种嵌套查询，一旦涉及到嵌套查询，就需要去注意你的一个分页。OK。

