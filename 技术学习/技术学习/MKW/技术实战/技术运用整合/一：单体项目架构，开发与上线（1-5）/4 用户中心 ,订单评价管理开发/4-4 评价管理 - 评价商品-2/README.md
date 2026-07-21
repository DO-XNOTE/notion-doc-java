---
title: 4-4 评价管理 - 评价商品-2
---

# 4-4 评价管理 - 评价商品-2

[image](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/296638fa-50d2-486f-85b6-69c5f81859b1/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663OHPTVME%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T224739Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCICUg0xAhfFb7U0GQHeVYoqByS9%2FKd6aODnkuSZNg1AM%2FAiA0HHPwpT6jRWghAuQFSJ0odd213w7FAZXeDoTZRQf5SiqIBAjG%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMnTUqIw2yxi64CM1iKtwD2cjGtxqOXc1NFomrLKxUckTUNhkiZt4noHR1Mvibxu2%2F3gN1pwSxq2CiuD2SaRme79In6x8meVdjkGrpB15FrnEtdwPjhxUMjkgcacGNtr1uU81hDSKvIbfvxtn9%2F2Jhs0Jj8PyACukWczmCtg1ciG2cRFKMaigcds5zPZqgAA6YK5CdQ8D%2Bs3U1ucfXMSzBPm4xhsL9Bly1e9VmZs9MUNxiasz9lKRssMRAkYK97Zvx6D0bO972yEJtO3TUvIZTQitR36GKJzw2W9UyJ2F%2FOU4vQysFBH0PLAJOG7kVOGzhut8Czojpc0z0T525Gd668qnGFjfRF489Nd%2FJPkKLUR%2B9Eb0X8Sbm1rJm3LyxDIVAJagfA%2B2noadKCJKXG9A0480axk0CmMOT9pEsqQkd1bmqem4JCOUNMuSJc9jTgbp%2B4a9Rx2S20B6hPIdrIDX8nXRIaXjMgaZYb2qYtvAGnsXIBSLFqW8ny7vderu6EQ4LLHzci2Z6u%2F0YICM2EPzMj%2BH3SYnLL1TAr2yktT3%2Bm%2F327c1FArCNEMMBUyez4LPNuRkb%2Fuu4QUHUTDCTwHYG%2FEtBlHS%2BPyB2XKHe3BGwjkUW8b5mbfs%2FBjvCfPng%2BBykA2LmLaQKF7Pc3rkwjrr%2F0gY6pgHnjHpYMkkT8pr1kvJsCD4F2qOJt70ZGFwcVU3rdv0tXz%2FDE1sOpWGx9QzXS5R1Naviab9qqxHiUMQEisKosT4DDQ4hHClV%2BYCSeTOtxSmR0K0Lvsv1AmTGCDTPwGOgprfzr0fXDBIq0KA72QEMGEmiu5n2CEdfIht8FBWavYqY8lcFLYM7XHNTmVh679AuJrgtI%2Fxf13CL%2BczJoXMA5wOVergvmmR9&X-Amz-Signature=daa106c93d5eb7d38eafd5d05f4faef57eb1eee706f96e0ab62b198b0f796360&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

在我们后端 Ctrl 了，拿到 comment list 以后，咱们就可以去做一个保存的操作了。好在这里我们要去写一下service。在 service 我们先去定义一个方法 public void save comments，然后传入相应的参数，第一个是 order ID，第二个是用户ID，第三个是list。这个 list 我们就拷贝一份，从这里直接拷贝一下。好。OK。我们在写上注释，保存用户的评论到我们service，我们就需要把相应的方法去实现一下。在我们画一行，不要忘记我们的事物，要加上使用愉快的。好，在这里我们就需要去编写相应的代码。其实总共分为了几个步骤。


第一个步骤我们应该要去保存评价，这个是要保存评价到我们的表里面，这是一张叫做item，叫items， comments 叫这个拷贝一下，这时是第一张表。除了这个以外，我们还应该要去把订单的一个状态，评价状态去修改掉。第二步修改订单表改为以评价这张表对应的就是orders。好。


最后第三一步，除了这两张表的内容，我们有了新增和修改，还有一点是必须要去注意的，就是我们的订单状态表。在订单状态表里面，它其实会有一个时间进来看一下。 order status。有一个叫做 common 的time，这个是用户的留言时间，用户在交易成功之后是可以去留言的，留言一旦成功了以后，相应的我们的 comment time，这个时间你是需要去进行一个存入的，所以我在我们的业务就涉及到了这三张表。把写上，拷贝过来，这是修改订单状态表的留言时间。


好，我们先来做第一步。第一步在这里我们是应该要去循环的，拿到 comment list 去做一个保存。循环的时候我们应该要为每一项去增加一个ID，也就是我们的一个，数据库的组件。其实在 Bo 里面我预先也已经是定义了叫做 comment ID，所以我们应该要去把 ID 去设一个值设进去。设进去了以后，我们再进行一个保存的时候，我们就可以去把对应的 IT 保存到我们的数据库里面去了。所以其实在我们保存的时候，我们也会通过一个循环去做一个保存的。好，在这里我们来看一下。在。写一个 for 循环去循环这个 comments list，每一项都是一个 b o，定义一个元素，就叫做 o i c o i c。点 set comment ID 去设置一个组件，这个组件在我们当前的这个service，我们其实是拷贝过来的，它会有一个Sid， Sid 在这里我们就直接可以去使用了。通过 Sid 点 next short，我们就可以去获得一个组件，往这里面塞值，这个 list 就包含了这样的内容了。


随后在这边我们要去定义一个参数，把相应的参数去放到我们的 SQL 语句里面。因为我们涉及到了一个循环保存，所以我们也会使用一个自定义的 SQL 语句，我们会放入到 map 里头去。在这边我们先可以定一个map， map 还是一样。 p 是 string 类型的，值是object，定义为叫做 query map， new 出来。好，我们在 map 里面，我们就定义为map，叫做 query map。在这里这样子的参数名称可能会不太好，直接 map 点put。


第一个我们应该要去把咱们的用户 user ID 给放进去。好。下一个应该是我们的list，把 list 放进去。这样子其实在 map 里面就包含了两项内容，一个是 user ID，一个是 comment list。 user ID 是根据用户的 ID 去做一个保存，因为我们在做查询的时候也是根据用户的 ID 去做查询的。好，随后继续。有了我们 map 以后，咱们在这里就可以去执行一个保存了。保存我们是需要去自定义一个 SQL 语句，我们要写自定义的map。这个 map 我们来先看一下。找到 map 工程。现在我们是有一个叫做 item comments， item comments napper。


我们没有一个 custom 对吧？拷贝一份好，拷贝一份以后取名字叫做custom。自定义好。在这里面我们做一个精简result。 map 我们就不要了，它是需要有一个 name space。 name space 在我们拷贝一份，我们也是一样。拷贝 item comments wrapper 在定义为 custom 好。OK，在这里面我们就可以去写上相应的一个方法了。写一下 public point save comments 传入的参数就是一个map，这个 map 我们拷贝一下，在我们的 service 直接把参数贴过来。好，这样子我们命名空间所对应的我们就已经是写好了。好，随后我们要去写一下我一个自定义的 map 具体的售后语句了。相应的在这里。一定要去把命名空间改成custom，这样子就相互对应了。


好，在这里我们就可以去写上一个select。 select ID 要和我们命名空间里的方法要一致，叫做 save comments。好，我们结尾。先结尾一下标签传入进来的参数叫做 parameter type，类型是一个map。好，要进行一个插入的操作。我们会使用音色的 insert in two 插入的表叫做 items comments，也就是这张表写过来。好在这里面我们要去定义一下要去插入的那些字段，这些字段有哪些，在这边我就直接拷贝一份了。


有这些内容，为了格式更加好看一些，我们可以让他们一个一个的换行，可以在同一行，也可以在也可以换行，这两种方式都是没有问题的，这样子稍微的好看一些，格式更加的美观。在这里面，其中像用户ID，我们是可以拿到进行保存的。此外还有是 item ID， item name 以及是 item 它的一个商品规格， ID 规格名称。这些内容其实都是订单商品的一个关联表信息里面所拿到的。既然拿到，其实本身我们在前端也是把这样的一个 list 拿到了以后再传递到我们后端的，所以这些数据在传入进来的 list 里面，其实全部都可以拿得到。所以拿到了以后，在这里面我们就可以去做一个相应的插入的。


OK，好在这里 insert 下一个就应该是values， insert value values 好，再来一个括号。这个时候我们要去做一个相应的值的插入，要把所有的值一个一个的在这边列一下。但是由于我们是一个list，所以我们在应该以一个循环的批量的形式去做一个保存。所以买白迪斯它有一个叫做 for each 这样的一个标签，通过 for each 我们都可以去实现一个循环的保存，它其实也是一个 for 循环collection，这个 collection 是指的一个集合，集合是从 map 里面来的，我们在 service 里面，我们是放了一个 comment list，这个就是它的key。所以拿到 key 了以后，在这边填入一下就可以了。


好，先把结尾标签先结尾一下。结尾标签最后一个是放在括号的后方，因为我们循环是循环这里边的一个内容。OK，好，我们循环第一个。既然是循环，它就会有元素，元素叫做item，我们可以去取一个名次，我们就叫做item。好了，这个也没有关系。下一个是index，不用多说，也就是一个下标。好。对于我们循环的时候，我们每一项是一个怎样的间隔形式，它有一个separate，我们是以一个逗号的形式去进行间隔的，这样子我们的一个 for h 这样的循环标签就固定好了。随后在括号里面就可以去把相应的职能一个一个的放进去。


首先第一个就应该对应的我们的ID。 ID 在这里我们应该是这样子，井号，大括号，逗号。在这里面把相应的 comment list 里面的内容拿出来，这是我们定义的一个 item 元素，所以通过 item 点这个ID，其实就是我们这里所说的 comment ID，也就是 Bo 里面的内容拿过来填到这里，这样子第一个它的 ID 就已经是有了。


随后是 user ID，用户ID。写一下用户ID，我们是在 service 的里面，在 map 里面直接插入了，放入了一个 user ID，所以只要把 key 拿回来就行了，这是用户的ID。好，下一个。下一个就应该是对应了商品的ID。 item ID 在这里也是一样。通过 item 点，在这里我们可以多写几个。多写几个 item 点，我们从 Bo 里面去获取。这是 item ID 贴过来。下一个是 item 的名称写过来。随后再下一个是规格的 ID 和名称。这是 ID 以及是名称写过来，OK，好。下面就对应的是一个评论的等级，以及是评论的内容了。评论等级和内容也在 Bo 里面，所以直接切过来就行了。


好，OK。这些内容我们全部都已经是填充，都已经是有了。接下来的两个，一个是创建时间，一个是更新时间。这两个直接可以使用函数就可以了。使用 null 当前的时间。这样子我们就可以去做一个循环的插入保存了。


OK，好。现在我们可以到 service 里面去调用一下。在这里直接写 save comments，当然我们的一个 map 要写进来。public，这是 item comments custom map 写过来，注进来。把。直接通过 map 点 save comments，把这个 map 给丢进来。这样子它就可以去做一个保存了。OK，好。这是咱们的第一步。好了，以后接下来我们要去做第二步了。第二步是把订单表它的一个状态改成评价。在这里我们直接把 orders 给 new 出来，把条件给写上，条件就是它的组件ID。把 o 的 ID 给放进来，要去修改的值，修改的属性，修改的那一列其实就叫做 set is comment 对吧？把它改为 yes 就可以了。好，这是我们的一个条件和要改的值。好了以后通过 order map。在这里我们没有注入，所以我们把去写一下。 order mapper，通过 map 去做一个点。还有一个方法叫做 up date by。使用 primary key 根据主键去进行一个修改。必须要使用selecting，因为我们其他的属性是不需要去做更改的。把 old 给丢进来。好，这是咱们的第二步。


最后第三步是要更改订单状态表的留言时间。写一下是 order status。这张表。其实也是一样。首先一个我们要去设置一个组件，它的是 o 的ID，因为他们是因为这张表的组件就是我的 ID 给塞进来。好，随后根据主键去做一个修改。有一个 set comment time 把时间直接通过 new date 就行了。好。 old status map 来看一下，在这里也没有把卡辈分。 order status makeup okay，在下方就可以去做一个修改了。 update by primary key selective 把 old status 这张表给丢进去。好，OK。这样子我们就可以实现我们 service 所要去执行的 3 块方法。OK。好。现在我们就需要到 Ctrl 里面去调用一下 control 了。在这里 service 叫做 my comment service 点 save comments，把订单ID、用户 ID 以及 list 给丢进去了。以后这样子就可以做一个保存的操作了。


好，在这里我们就可以去测试一下。我们先来 install 一下，好， install 成功，再来做一个重启，好，使用成功了。好，现在我们到前端来测一下。先刷新一下。我们先来看这一张。我们先这样子从订单管理过来，我们把订单编号我们用这里面包含了两个商品评价。商品在这里好评，这个是差评的。这留言是好吃，这个是不好吃。点击发表评论。现在我们保存成功了。保存成功以后，在这里我们再来看一下。已完成这一条订单，它所对应的在这里它的按钮就没有了。它显示的是一个已评价，因为刚刚我们是评价过了，所以对应的订单表的一个字段 is comment。现在是 1 的，我们可以到数据库里面去看一下。我们先来看订单表，这是订单表，我们来搜一下，搜到这条订单，这条订单来看一下。其中它的 is comment 现在是 1 了，OK，所以这张表是更新成功的。


我们再来看一下我们的一个 order status，就是订单的状态表，在这里有这一条订单，看一下。在这里会有一个 common 的时间，这是当前留言的时间，有了好OK。关闭时间是没有的，因为只有是取消了订单，它才是关闭的，所以我们这条订单留言是 OK 的。


再来看一下我们的一个留言表， items comments 进来看一下。在这里面对应的其实应该就是最后两条。不是最后两条是在中间两条。在这里是中间的。这两条一个是马卡龙，一个是动物饼干，其中一个是好吃，一个是不好吃。1、是代表好评，这个是差评。这个是我们刚刚的留言的时间，这是创建时间，这个是更新时间，OK，好。现在其实我们从咱们数据库里面就能够看得出来，咱们用户的一个发表评论，现在已经做完，已经是 OK 了。相应的如果你可以到商品里面去看，他的留言，也是可以看得到的。我们可以点进去看一下，这是对应的商品有一个全部评价，点进来看一下。这个就是我们刚刚所做的一个评论好吃，这个是芒果味的，这就是我们所评论的，并且它是一个好评，OK。

