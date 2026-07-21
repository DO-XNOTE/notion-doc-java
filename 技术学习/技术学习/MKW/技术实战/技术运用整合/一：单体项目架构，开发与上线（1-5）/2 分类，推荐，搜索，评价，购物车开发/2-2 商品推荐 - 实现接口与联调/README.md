---
title: 2-2 商品推荐 - 实现接口与联调
---

# 2-2 商品推荐 - 实现接口与联调

[image](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/9d7076b2-3cbc-4610-b9e0-ecf98551be4f/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667PBSYLZY%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T224641Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIEV0leM8QN%2B8O69USuNICHYL4R3w4P2O%2FGGOFcSnHEqAAiEA%2BWlJ3CFV1kF343AWIHY2kbodLhihmsQ9wtxd8DrSgvsqiAQIxv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDI1P2yOu0%2BHDeN%2BiXSrcA1OrEdG%2Fsg9fA8277hPNcPyiE6SAJQRpwVk%2B%2BKyGCUoSDryMtyLdWfgt29lTsF5hO9FoWZK3miIhpIID%2BBwghnr%2BNqJAne8nTIV4OkOE0u55%2B18tBCpVt9iSpTzYzUG8G2JrMxg%2BrAwhFQZvpGUXuUGPUMc8c8v3jvRn7nhXChHt48N2fVqkV8P9yw5tDnwslpZR0aDoqBNbC49f%2F2%2Fjo4LRjTs8CrnlRPur3VS7O5iRY7hNaO%2FTz63A5u1wXCpxsw1S1xXq7G%2Bqmh31aRBU%2ByildSnTKGhmkEzPnihUMuJT5ZOvMavrBe1loSDoP336HAM5wItP2aqDNouUisBeJZIU%2BRbXW4H6uWjs1fwwukKSt6h5juj0%2BviyN8tsNO5oP2AjxJypZbpSzE7SDhk2zBLehOFBEpXG%2BVQM8%2FmxToCtZqesGgvYhm89myHqaI4MMz2gUP9BgMr16CKJ1jRU%2B0%2BS8INkrWfNGgdU1%2Bs9Yr7dmUthJB64CDm5LarsruEoeM5%2Fu6Tzz7SGNldmWeFQ15Ub2Mm4iRY1RO23oE9QkDIhhAE42yDECNEWrwY4%2B%2BSkhPv7exdj1Q8%2FLrLdtsEf1jyanpzlezvHiczUC9ic3MASljep3puITvgvrGzyMI24%2F9IGOqUB2bioCaVWb6Jv90yQJjrTNA7JlJOpoCTG%2Ff5kUbT5%2BWP%2Bp6lBSwCigxp%2Bvr7jTz%2F8dOqnWlp3YMADL%2BYR0nL9ZP3uJIws3Gl9iqHo72Lp9Ukl4H6Tvb32vYcqyrPyYYppqDMHq1zgesxWYMCpoMHMSF9UcGjOvxLmU8yzRnvMbK6D6tmqKgExuKiimLwQKTza3QkId6ta7b5oQLRTpajEYh6a9F2c&X-Amz-Signature=194b206e665e29bc536f91b85afda227f44d544f36d65a3e47bc474fd8dbed2b&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

写完咱们的 SQL 以后，我们就需要去编写代码进行实现了。打开开发工具，在这里我们还是一样从下往上去写。接下来写一下咱们的service，它的一个方法先定一下，取一个名字 public list， get six new 6 个新的商品items，这是lazy。好在这里面是需要去传入一个参数，这个参数和也是一样的。如此 cat ID 是一级分类，加个注释就是查询首页每个一级分类下的 6 条最新商品数据。我们在 service 里面需要把这个方法进行实现。


好，这个 service 我们就可以先不管了。因为我们可以先去编写咱们的map。在 map 里面其实在和我们上几节课里面讲到查询分类的时候，可以它的一种实现方式差不多是一模一样的。我们先把拷贝一下，我们先定义它的一个接口中的方法。我们先不写，我们创建以后我们再回过来，头来再写取的名字。其实我们可以和 service 里面保持一致，在这里可以去加过来。在这里也可以传入一个 root cat ID。在这里我们可以换一种新的方式，因为在 my Betis 里面。


在这边我们一做映射的时候，参数你不仅是可以传 string Int，像一些对象或者是一些map，我们也是可以传入到自定义的 SQL 文件里面去进行查询的，也是可以的。所以我们在这里面完全可以写一个map，定一个map。这里面的 t value，一个是 t 是string， value 是object，因为它的值可能是Int，也有可能是string，都是可以的。当然你在里面传一个 list 也是没有问题的。在这里我们取名就叫做map。另外在它的前面我们可以加上一个注解，也就是参数。这个参数的名称我们是可以为它去加一个的。比方在这里我们就可以取名叫做 PUMS map，这个就是作为参数所传进去的一个map。OK，好，我们把名称复制一下，到咱们自定义的 Map 叉庙里面，我们可以去写一下。在这里写一个 select ID，就叫做这个是和我们在接口里面所定义的 ID 这个名称是一模一样的。下一个下一个。其实我们就可以参考上方去进行相应的定义了。其中在这里面我们就会包含一个 result map，写一下，把直接贴过来。 result map 现在我们其实还没有去写，但是我们可以先写好，对吧，我们定义为。

Why new items co?


再来一个我们传进来的什么时候是什么类型？这里有一个 parameter 菜品，传进来是一个map，所以我们直接在这边写上一个 map 就可以了。写一个map，随后把标签进行一个结尾。在这里我们就可以把之前所写的 circle 我们直接全部都拷贝到这里。我们贴到这个位置，贴过来它的格式，我们把它按一下tab。好，这样子就 OK 了。好，OK。内容比较长，但是没有关系，这样子它的可读性会好一些。如果你嫌太长，在这里，比方像 left join，可以把每一张表作为一个单独的，这样子它的可读性也会好一些。


这样子其实也行，好在这里面会有一个参数，这个参数就是 root cat ID 在这里，由于我们前面是定义了叫做 pump snap，所以我们直接在这里把它使用一个占位符给替代掉就可以了，因为它是一个参数。这样子 PUMS map 点你传入的某一个值在 map 里面所对应的 string key。比方假设我们在这里取名为把拷贝一下，我们就把它称之为是一个 root cat ID，这是它里面的某一个键值。好，这样子参数就能够被它所拿到。


随后回到这里，现在我们就要去构建一个 my new item c o 了。这个其实我们也是要参考我们之前所做的。我们到上方我们可以去拷贝一下，把这一段内容我们可以拷贝到部位来。好贴过来。贴过来了以后我们把先写好买 new items bo，这个是一个 result map，和这个是相互对应的。对于 type 来讲，现在我们就要去创建一个属于我们自己的一个 FO 了。


VO 我们来看一下。我们先找到目前的一个位置，在这里我们可以直接拷贝一份，取一个名字叫做 new items bo。好在这里面我们去做一些相应的修改。他这个名字我们改掉最新商品do，把这里面的内容我们全部都删掉。好，每一个属性都可以做一个相应的编写了。


首先我们先来看一下，在我们之前做查询的时候，其实在前面这一些内容也是从 root cat ID 一直到BG，开了这一块内容就可以作为我们外层的 Fu 了，所以我们可以在这里面去写一下。我们可以先写这块，我们可以把先写掉这个注释不需要了。也就是把这一块内容从 root cat ID 一直到 BG color 全部都写过来。首先第一行是ID，这是它的组件，我们只需要在这里做好这样的映射关系就可以了。随后是一个 string 类型的，也就是一个result，把 result 再贴过来，此时举需要把 root cat name 拿过来就行了。这是它的一个分类的名称。


再是一个slogan，我们再复制两行，一个是图片，另外一个就是它的背景颜色，我们就已经是写好了。这个是在我们的 VO 里面所定义的， VO 的名称我们写过来叫做 new items VO，不要忘记一定要去改掉，不然它做映射会出问题，是会有问题的。在这里面我们把这些我们再贴到这里面来。贴过来以后，我们就根据这里面的内容去做一个相应的修改就行了。


写一下。首先第一个private，它是一个integer，如此k，s，i， d 拿过来好。随后下面的内容全部都是 string 了。 string 这是一个名称，是slogan，cat，image，还有是背景颜色，这几个全部都有了。以后还有一个是 sub list，就是我们所嵌套的一个list，这个 list 就包含了 6 个商品的元素。 private 是定一个list，它的类型我们先不去定义，比方我们就先写一下，我们称之为 simple item do，就是简单数据类型的一个商品，它的表现成对象。在后面我们就可以来写一个叫做 simple item list，这样子就行了。好bo，我们现在还没有，所以我们也是需要去创建的。在这里面我们去 new 一个 Java plus 贴过来也OK。好，有了以后加个注释。


这是 6 个最新商品的简单数据类型。好，在这边我们就需要去。在这个地方我们要去做好映设了。首先一个它的 property 名称，我们要去设置好叫做 simple item list 贴过来。 of type 它所对应的类型是什么？叫做 simple item do 是需要把这里去进行一个覆盖。好。下面几个。下面几个这几项内容应该是对应到我们的这里了，从 item ID 一直到 create time，其实这个时间也不需要，可以无所谓，我们只需要拿到商品的ID，商品的名称和它的一个图片这几项，这三项是最重要的就可以了。


好，我们到这里面去写一下。首先第一个是 item ID，我们是需要放到这里来的，因为这是一个组件，而且它是一个字符串，它并不是一个 Int 型的。还有是商品的名称贴过来，还有是商品的图片， item URL 这样子。这里面所包含的这些属性在里面作为的一个集合。 Clang 就已经是写好了。不要忘记了，在我们的 simple item du 里面，你也是需要去编写的。在这个里面其实也是一样，写一下，拷贝，这样子快些。一个是 item ID，另外是 item name，其后一个 item u r， l 这些不需要删掉。我们来生成 get 和 set 全选好，生成功 VO 我们就已经是好了。以后我们回到这里。在这里你也是需要去把 get 和 set 去进行生成的。好，全部都生成。 OK 了，这两个 fu 现在我们就已经是就绪了。


好，回到我们的 map 仓料里面。在这一块内容我们来检查一下。在这里你是需要去递一个ID，这个 ID 是 result map 或这里是需要映射 new item CEO。在这里。还有是下方的一个 simple item p，o，这两个都要有相应的数据。在这里面数据的属性要一一的做好映射，它的 collection 里面所有的映射也是需要去做好的。好，我们可以返回到这里。现在他所查询出来的一个list，它的类型我们已经是有了，以后把拿过来，这样子其实就可以去做一个相应的查询了。现在对于我们的数据层，也就是 map 内容我们是就绪了，就绪了以后我们就可以去编写一下咱们的 service 了。回到service，这是它的实现类，在这里我们就可以去写一个。由于在我们的map，它的一个实现接口里面，我们定义的是一个 map 这样的参数，所以我们是需要去传一个 map 进去的。


首先我们先定一个map，在 map 里面，这个时候我们就要放值了，放入一个 key 和 value key。我们在 SQL 语句里面，我们写的是 root cat ID，所以我们只需要在这个地方把作为它的 t 键就可以了。值只需要把传入进来的 root k，s，i， d 放到这个位置，我们的参数这整个 map 就已经是封装好了。随后我们只需要进行一个查询。我们通过 category map custom 点 m 查询刚刚的方法，也就是 get six you item lazy，把 map 丢进去，这样子他就可以去做一个相应的查询了。


好，现在我们就可以来做一个测试了。测试之前还是一样，我们是需要去进行一个 install 的。好，现在 install 成功，然后启动一下服务器。好，启动成功以后，现在我们 service 和数据层是都好了，但是我们 Ctrl 的还没写好，所以我们启动服务器没有用。我们把这 Ctrl 的来编写一下。

在我们拷贝份，拷贝一份我们的 10 来个处接口写一下查询每个一级分类下的最新 6 条商品数据。拷贝一下，贴到后面的去覆盖。它的查询方式也是一个get。另外它的一个路由地址，路由地址我们可以参考前端，在前端我们找一下有一个six，在这里 six new items 拷贝贴到这个位置，它会传入一个 root cat ID，这也是一个路径参数。这样子其实就 OK 了。参数名称没有问题。好，我们在这边也是要做一个判断，因为你这个判断没有你查询不出来任何东西，所以判断一下。判断 OK 了，以后我们就可以去做一个查询的。

Get 6 new items lazy.


把 risk cat ID 给传进去，好拿到一个list。当然这个 list 在这里我们是不是没定义泛型，对吧，所以在这里也要去定义的。所定义的内容和我们在 map 里面所定义的是一样的，它是一个 new items。 b o。好，我们在这里。这是它的实现。也要加的。贴过来。现在我们其实 Ctrl 就已经是写好了，会有一个封号，写的是中文的了，改成英文的就行了。千万不要忘记我们的事务，虽然它是一个查询，但是 sports 我们还是要加上的。好在全局的 install 一下。


好， install 成功我们再重启服务器。好。OK。现在是启动成功了，我们就可以到咱们的首页。现在我们可以打开咱们自己的页面，我们可以来刷新一下。刷新现在发现我们的页面还没有启动，但是没有关系，这是因为我们 Tom case 还没有打开。所以这一步在每一次大家在重启电脑以后千万不要忘记，是需要去做的。把自己的 Tom kit 去启动一下就可以了。这个步骤有时候我自己在操作的时候也可能会忘记，所以我们在去启动一下。点斜杠 start up s h 回车。好， Tom k 的就成功的启动了。启动以后我们在这个页面我们刷新好。


OK，轮播图分类没有问题。我们这个时候鼠标往下慢慢移动，你会发现这一块内容我们现在是加载起来了。 c s s 有一点乱没有关系，因为我们的大小放的太大了，我们缩小一下页面就可以了。好，现在OK。第一块内容有了。往下面滑动，你会发现现在我们所有的内容会顺着我们的鼠标滚轮向下去进行相应的展示。OK，没有问题。我们可以再按一下F12，把页面重新的刷新一下。把 network 我们可以全部都清掉。把 network 清掉，我们往上面拉一下，给大家看一下。鼠标往下面滚，你会发现往下面滚了之后，它就会有一个查询，这个就是我们刚刚所定义的一个路由，也就是后端的一个接口。当然相应的图片也会随着我们的一个内容的渲染而进行展示。这是它的一个root， ID 为3。


最后我们再往下面滑，一直往下面滑，你会发现每一个分类 ID 一直会查询，直到查询到第 10 项就没有了，因为总共我们就只有是 10 个分类。好，现在咱们在首页的一个根据一级分类去查询它最新的商品数据，就已经是完成了。并且它的一种加载模式和我们使用这个分类是一样的，都是懒加载的。

