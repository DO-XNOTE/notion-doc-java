---
title: 4-5 评价管理 - 历史评价列表Mapper
---

# 4-5 评价管理 - 历史评价列表Mapper

[image](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/cc91ee91-49cf-42cf-8d2f-8e15e9c9416c/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662CTTEFEI%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T224739Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDnrdP8OJoDUH%2BdGXMW5TuAWlA7FJEGre5d7IcMBhRJXwIgHa24P2GmRaYMTftDzRBit1F6GJ%2F8P7ta8HSkFX73iv4qiAQIxv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDIGe9MlS0SMYQiNqRyrcAy4kp9AAE7Auq9HRawEJv0gw1MGeKHX84J52tzeoVaIGAa6tJqC2G7O%2FNwNKB4kKM%2FdEavGFYXjz3chr7ZPmnWzVKob1TshR5aLCIH%2FE5EJe44Jij53AYDmvDkP7qucNF6iTTxUpiunXgH%2Bur2IhXUXkHnB8ap0j7MamtupaXlJvB6emlTNwhxQxSFtx6tYD6fynUCphTVJN5Pvf01VvH3S4HAy1TMx92q518DOrzDQqJfPtpJA0zYvI0GFC7lNVRni%2Bi2V2pMQQ4cLi5JlNaQ57lonlG1Bs9uwvQtpiVLp6kZrS2wLGqU1114Hz0B6vlbxDyCb%2FCm2ngQgMk75doNfEzofdcc%2F8RZHIig29X5DDWGbEQTwH7Ip2kiSlSdp5PnMdIFC8l66yW0HwmA7RVxwAtGV5lL3jdaGeBvm8Z0mQMfy8yDV1Xc37JhK8tBlNGehY5JBB5LgFmEQ1AYjh9x6Ni9sJd1CHidZAQaXL2htmxFiURkIqBzJ2HIxutkYrUUn4R%2BFdXgxaeeDNZ3%2B3IoLEIjkLtqWtI%2BsC9%2FxYYv4HoRXpTQn%2FsF%2F%2FPSeu5T2S8JtD1OqS8m9QKDSwnKSo7DUAuXg2stmFfCS8a9vXV8uJMLkYNi8tfeq1TJ1RMMW3%2F9IGOqUBdxrwp6hB%2Fr22y7nleNVVGRWn9KVpo9OrYGtEcflvefDtXWSyhRrGDmUg3WgqNFB3Rqb4dyGK%2Bkvs6J%2BCoYuYmr7X%2BkSS4xdYN7SwQCdWfy6xnK60hP94yFMq5u3ZsbXVbwkmswidGuKa0pHTXmDUu%2F3VEFvAeYuLPLJl7qALE5kh%2BRJGQyk5YAClv26iTsOgG5HdxkqUQb%2BL%2FjSDzNctnUG9ukhE&X-Amz-Signature=abe9b3e570b8f8d3f5ff2ef1f00aec735e6c826a223e741d03e9200a597a31c9&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

上节我们是完成了订单管理中的评价商品，我们现在是可以发布评论的，接下来我们就应该要去到我的评价里面去看一下，要把我所有的一些历史的评价展示出来，并且是带有分页的。这个我们是可以参考一下目前的一个生产环境，生产上其实是有两条记录，可以来看一下评价。其实我们评论表里面的内容外加一张图片，这个图片是需要我们到数据库里面去进行一个关联查询的，相应的一个关联查询应该是 item image，相应的这两张表应该要放在一起去进行查询。


OK，好。现在我们就可以先来把 SQL 语句先去写一下，在这里新建一个查询，先保存一下，取一个名字用户中心，我的评价。好。随后在这里面去写上select，我们放大到最大。好先写一个 select 星号。 from 这是一张商品的评价表，所以 items comments。在这里为它取一个别名，叫做 i c。好。再来一个 left join 是要需要去关联一张图片表，图片表是 item image，取个别名好。OK。来一个 on 把两个关联的 ID 写上，一个是 IC 点，他们是通过商品表的组件去进行关联的，所以应该是 item ID 等于 item ID。把两个商品的 ID 进行一个关联，这样子就OK。随后我们就可以去写上相应的条件了。 where 首先我们是应该要把当前的一个用户的 ID 给标上，把用户 ID 等于在这里，我们可以去找一个。我们到评价表里面去随便找一个，找这个，再把 user ID 给拿过来。


好，这是第一个条件。随后第二个条件。第二条件是针对于咱们的图片，我们应该要把商品对应的一个主图给拉出来，所以把这张表中的一个 is man 要设定为1。好，这两个条件 OK 了。以后我们可以再来加上一个 order by。我们是可以根据留言的一个时间去进行一个排列。 great 参根据它的创建时间好使用g， s c。好，OK，我们可以去运行一下。这样子所有的信息就在这里可以全部都进行展示了是吧。但是列太多了，我们可以去精简一下。信号我们就直接删掉。


首先一个IC，也就是留言表中它的一个组件，我们应该要拿出来 s comment ID。最后一个 i c 点它的内容 content s Concerns。下一个 i c 点 create time，这是创建时间，把驼峰改一下好。再下一个是我们这张表里面的商品ID，把商品也可以去加一下 item i d s item ID 好。再来一个规格，规格是 i c 有一个叫做 s e p c name yes name。好，这是规格的名称。最后一个这张图片也就是商品图片，从图片表里面的 u l s 取个名字，就叫做 item image 好。OK。这样子我们这些相应的一些查询的字段我们就已经是列出来了，总共是有 6 列， 6 列我们再加一列，再加一个 item name，这是商品的名称，我们也要去加的 s item name，这样子总共 7 列都是我们所需要去用的。点击运行，这样子OK。相应的语句我们是可以去查询出来的。好，这样子保存一下。


随后我们就可以去编写一下我们的map。我们可以把这些 SQL 语句先全选拷贝，推到我们项目里面来。在项目里面打开自定义的map，在这边我们写一下 select 标签，把结尾标签写上，再把这一段 circle 给贴过来。贴过来以后， select 我们就中间的一部分内容是好了，为它定义一个ID，这个 ID 取个名字叫做 query my comments。随后后方我们传入的一个参数 parameter type。它就是一个map。 map 里面会包含一个用户的ID，也就是这里把删掉先把可以先去写好 PUMS map，点 user ID 好。OK，它后方还有一个返回出来的对象，返回出来是一个list。

其实这一块内容我们应该要去映射吧。映射为一个 result map，在这里定一下，叫做 my comments。既然会使用到 result map 了，所以在这个上方我们可以去加上一个 result map。标签 ID 对应的就是这个，把它写过来。


type tap 其实就是我们之前一直所说的，它所需要去映射的一个 v o，这个 v o 也就是映射这里面所有的一些字段属性，相应的 v o，我们已经是直接添加了进来，在这个地方我已经是加了双击看一下。这里面包含了一些相应的属性，这些属性和我们这里所对应的总共是有 7 个属性，总共是有 7 个。好，在这里我们可以去右键拷贝一下它的引用。在这里我们就可以去贴一下了。在 tap 直接贴过来。好，贴过来以后在这里面我们要定一个第一项，也就是ID。 ID 是对应我们的 comment ID 斜过来映射的属性property，也叫做 comment ID。好，OK，这个 ID 行了。好，这是它的第一列，第二列是 result 结果。我们可以先把结尾的先写好。这里面也是包含了 column 以及是 prompt column property。我们先把拷贝总共是 7 列好，下一个是 content 内容，随后是创建时间，再来一个商品的ID，随后商品的名称，再一个是商品规格，好。


最后一个是 item image 商品的图片 s e p c 应该是拼错了，应该叫 s p e c，但是也没有关系，也是可以去使用的。OK，好。这样子我们对于这样的一个 map 就已经是写好了。写好以后我们到命名空间里面去，这是他的 name space，我们把这里面对应的方法也去写一下。 


public 返回一个list，这个 list 我们会返回出来一个 my comment c o，它的 i d，也就是方法名，直接拷贝一下，叫做 query my comments 贴过来。传入进去的一个参数就是一个map。把 map 加上前方，前方。我们可以去加一下 pump 它的一个注解，对它定义一个名称叫做 pump snap。在我们这里面所引用的名称直接写过来。这样子我们的一个定义的方法就已经是写好了。OK。

