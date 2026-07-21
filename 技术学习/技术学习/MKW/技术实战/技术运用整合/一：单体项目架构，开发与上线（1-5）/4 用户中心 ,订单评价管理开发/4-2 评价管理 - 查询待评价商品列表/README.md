---
title: 4-2 评价管理 - 查询待评价商品列表
---

# 4-2 评价管理 - 查询待评价商品列表

[image](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/77f863a4-0a41-42eb-bc1d-095824d58495/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663AXYZQBU%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T224737Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCICtpHjqCnmPN2EfbvnMRsKajfenuHSivnhzkBBdksr1jAiEA8XIS6l%2Bj7saUbpxt4tVAm%2FmOfYN8o8FoUeEnUGKXr88qiAQIxv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDCnKZ3DjRTiwVA8hiCrcAwe5dgh5Nx%2BybskS13Z1LzqkzVg2ttPpV6jwTpnJUD6QulfEySo4d6lPVAqSnr7E9uSfbGnbB2w3PRQC2g080y4tgfDZiwyQjD%2FnXkQs0Ey96a5mBzubprOUR16rFku5YA2gN3BttN4w055H5pAA4B65Nui3gKi1l4BxN59Mm5yl4at2jpx8A2BC4T9Si3z%2FBmbY8VjvTG3c3alQ%2BVobZhrHIn4vNM8cSN0NolY%2BCurPb%2FJMu3oCDDLefLQgipZX9cZJYYxmmK28gGHTFst0GXZHg4SilkxQIRpWDa1dNL0Emw9erixdXJOkBt0xqjhW%2FB3UJ4%2FPmJ96yzXx3AH2jA3dVnNBaWyesW%2FYtfJO2sGMPUTRAUyUjYLNmillD82rrYwqoczLI27gMnsXQMr7oQ0jcp%2BSK9KBqXX3Bf%2FoDFNeXDCh7KrvsAcGKb7itaA%2B6fQu7GazWGbGr43cTMVty9OPxdpKSuM5W5IGhvVxuV%2B%2F%2Ftxe3aqNv4dE21aQ3X742dDldWlHIPWQD%2FeBTMQ6lcj4TsFe0VaElkKfrIy3xGJkjJli3UqaxteIhXfB8xcrYdruaF0%2Flhl5xlGog1cfI8qqh5bDF3Cy4Pz50C534ncjq5q%2FL%2BzRIcV5EqceMMu3%2F9IGOqUB5wb97EEyxc3xmjVNjZeAQc%2FuNtz2QNaaBCCbHmNtn4fkdH6uaQNMebCobBad8lYHPEkBoHaV8XnLMh8%2Fm2NzR6GeH%2BXjsbdNa94P%2FTR2Wh7o6At6ZPFbycjwu8AV1ZvXOR72ZoXdKhWRJiaApopxO9ndllJPyWLEsEJxYNVrzFkr%2FFc3Bz13rIEuazsolWvKdyM%2BXPtebjcRnAK9JrzMz2O4q7w%2F&X-Amz-Signature=fd17eb00f7806bd0bf0c72c8cae0aec3fa2e3c4c428b6d64c8f8e47338c95a40&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

在用户跳转进行发表评论的页面时候，我们应该要去把这笔订单所对应的一些商品都给查询出来，在这边进行一个展示，展示了以后用户才能够对应到某一个商品去做评价。所以这一张表我们应该要对应的去查询 order items，在这里面就会有商品的图片名称以及是它的规格名称，把这些内容是需要在页面去进行一个展示的。


好，现在我们来看一下前端的页面。前端页面是叫做 do comment 点HTML，这个是跳转的一个页面，这个是从上一个页面跳转过来的，可以给大家看一下它的一个代码逻辑。我们在这里会有一个 comment items 来搜一下。进入到脚本里面以后，其实页面发生了一个跳转到 do comment 页面。


好，我们来看一下我们的评论页面，它所对应的一个事件。先找到credit，这是生命周期函数，在这里有一个渲染评论页的内容。找到 render item comment，搜一下。在这里它会发起一个 post 请求，这是它的一个路由。 my comments pending，意思就是要查询那些等待评价的商品。传过去也是一个对应的用户 ID 以及是订单ID。查询到以后，查询到的是一个 order item list。在页面里面去做一个相应的渲染就可以了。


好，现在我们回到后端去编写一下。首先我们还是要从下往上去写。我们要去创建一个 service 的，我们直接拷贝一份，直接去写一下。找到我们的Santa，在这里面去写好，背取一个名字，叫做 my comment， my comments service，我的评论一个它的对应的service。另外再把它的实现我们也直接拷贝一下， my comments service IPL，好双击。在这里面我们就可以去把相应的代码去完善一下。


这些是我们以前写的一些内容，我们先都关闭好。在这边我们要先去写一个方法，这个方法是用于去查询的。写一下 query pending comments，传入进来，应该是对应的 all 的ID。订单的编号。根据订单编号去做的一个查询，因为它是一对多的关系，返回出来就相应的是一个list。 list 在这里它的类型要写好 order items 好加上注释，规范一下。根据订单 ID 查询关联的商品。好，随后我们回到它的一个实现，把实现的 service 要去写一下。买 comment service 对应的。这里面的一些内容我们全部都要删掉，重新去导入。好实现已经是 OK 了，它的事物就使用 sports 就行了。在这边我们会要去实现一下。我们导错了，应该是 command o 渴望着爱快捷镜写错了，这样子就可以导入进来。OK。好。


在这边我们就可以去发起一个查询。查询是根据 order ID 去做一个查询，所以我们只需要去把去 new 一下， new 一个query，再把它 new 出来。直接在这里面塞入一个条件，这个条件就是订单的ID。塞入以后，我们就可以通过 order items map 在这边写一下。


map，通过我们就可以去做一个查询了。直接点select，它会有一个 select by，也就是它会根据 record 记录去返回一个对应的列表。这个 record 其实就是我们所写的这个query，它是一个条件。这样子直接塞进去就可以了。它会拿到一个对应的list，你直接return，我们在啃错了就可以去拿到了。三行代码就比较简洁。好回到咱们的 Ctrl 了。 Ctrl 了，我们也要去写一个对应的。我们也取个名字叫做 my comment control。我们直接拷贝，把 my orders control 了，拷贝一份新的，取一个名字叫做 my comments 我的评价 control 了。好，OK。在这里边我们就需要去修改一部分的内容。首先是这一个类所对应的路由 request mapping 看一下前端，前端是 my comments，把直接拷贝一下，贴到这个部位。贴过来以后，它的 a p i 就是 10 来个处。这是用户中心评价模块。用户中心评价模块相关的接口。


好，OK。下方这里应该是一个 my comments service，把对应的给注入进来。下面我们就可以去发起一个查询了。我们先把一些没用的方法全部都删掉。把这里面的清空。参数，我们只需要保留 user ID 以及是一个订单 ID 这两个就可以了。这些都是从前端所传过来的，一个是 user ID，另外是一个 order ID，这是订单编号，两个 required 全部都是true，对应的是 post mapping。另外在这里我们应该不是这个 query 吧，看一下应该是一个pending，所以把贴过来。好。OK。在这里面我们就可以去做对应的一些代码实现了。


首先，当我们拿到了一个 user ID 和 old ID 以后，其实我们也应该要向订单里面要去做一个判断。你要去评价这笔订单，首先我就必须要保证你所传进来的用户和订单是有关联关系的，也就是我们之前在订单的 Ctrl 里面所写的一个内容。也就是我们搜一下，在这个部位有一个 check result，把我们直接拷贝一下贴过来。贴过来了以后会有一个 check user order 这个方法其实在这个里面会有，对吧，但是我们为了避免它的一个重复性代码，其实我们可以把这一块内容我们可以拷贝一下，我们这样子拷贝到 base Ctrl 了，配到里面。在这个里面我们也是可以去写对应的一些方法的，只不过在这里会有一个买 order service 没有关系，我们把这一块内容给注释掉，再把 my order service 写一下。在我们可以把我们可以放入到 base Ctrl 里面来放到这个里面来。放到这个里面来了之后，只要去继承了 base Ctrl 了，在对应的我们里面我们就可以去使用了。在这边应该是一个 public product 是无法使用的，这样子在买 orders controller 和 my comments control 里面，我们就可以去使用对应的方法了。


好，随后 check 完毕。我们的用户和订单是关联了。以后，在我们还要再去做一个判断。应该是判断一下咱们的订单。 check result。点 get data 这是拿到的一个订单，它拿到的一个类型，现在我们不知道是什么类型，它是一个 object 的对象，所以我们在这边是需要对它进行一个强制转换，把它转换为orders。随后把拿到取一个名字叫做买order。


好，再来做一个判断。你需要判断我的订单。点 get is comment 你要判断一下有没有评论过，如果它是 yes or no 里面的yes，它已经是评价过了，对吧？已经是评价过了，我们就不需要再让你去做一些查询工作了，我就不让你再往下面的业务继续走了。所以直接 return imock result，点 error message 返回一下，说该笔订单，已经评价。好，这样子就可以了。我们加一个注释，判断用户和订单是否关联。下面一个判断该笔订单是否已经评价过了，就不再继续好。


OK，业务往下面走。现在我们应该是通过 my comments service 点，我们把对应的一些内容给查询出来，等待评价的那些商品。在这边我们只需要把订单 ID 给传进去，这样子就行了。在这边我们会拿到一个对应的list，这个 list 我们直接拷贝一下这个list，好，拿到了以后直接我们反馈到前端就行了，这样子我们后端的接口就已经是 OK 了。好，我们在这里 install 一下。好， install 成功。再来一个重启服务器。好，重启成功。到我们页面现在是一片空白，我只需要刷新一下，刷新以后在我们的页面上没有任何的反应，对吧？来看一下。


很明显我们是出现了一个问题，在这边会抛了一个 500 的错误， 500 是代表我们服务端错误，也就是我们接口里面发生了异常，所以才会导致在我们前端出现了一个500。这个时候我们只需要到后端去看一下。在后端这里面我们拉出来往上面看，在这边出了一个错误，有一个空指针。异常是在我们 Ctrl 的第 44 行，在这边可以点一下，我们看到 44 行是在这个位置出现空指针异常，肯定是 my order， my order 是空了。在这边通过 get is common 的，你要去获取这个值是获取不了的，所以这个是一个空为空间一条。


在这里我们可以打上一个断点，我们通过断点也是可以进行调试的。在我们以一个 debug 的形式去运行。在这里给一个小虫子点一下，重新再去启动，这样子重启以后，现在就是一个以断点的形式去进行一个运行了。到我们的前端重新再刷新一下，刷新以后现在断点已经是进来了。进来以后在这边我们可以看一下。在我们拿到的 check result 里面双击一下，我们拿到了一个message，是一个OK，拿到 message 是 OK 了以后，我们会再从这里面去拿一个data。这个 data 我们在这边是作为一个对象，也就是 owner 去进行的强制转换。但是它其实是为空的。为空本来就是一个空对象，空对象你再从这里面去获取一个 is comment，很显然就会报一个空子进行。所以我们原先的目的是应该从 check result 里面去拿到一个订单。我们可以点击一下control，再点result，点一下，在这里再往上面点。这是我们所调用的一个地方。在这里我们是查询订单有没有，既然返回 OK 是代表有的。我们可以把 order 给放入进来。存过来以后，在我们的 Ctrl 的部位，我们就可以去拿到这样的一个 data 了。拿到 data 以后强制转换买 order 就有值了。


好，现在我们再来一次重启一下，再进行重启。好，重启成功，再来回到页面刷新一下。这个时候你会发现我们这一笔订单所对应的一个商品就已经是展示出来了。如果有多个商品，他在这边会以一个列表的形式往下面去展示，大家可以去试一下。现在其实我们就可以去针对这一个商品去做一个评价了。

