---
title: 3-19 dsl搜索 - 排序
---

# 3-19 dsl搜索 - 排序

[image](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/01867bab-17db-4e06-a497-211c0e25d67a/SCR-20240806-dvqb.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664KWZKA6C%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T225142Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIFBIm3qN7OrDoH4PREWFPAhJEV%2Bo9gYI7MVrXYH38l99AiAoYQXSKieM36FW3SG90KG%2BBs31WioQiGgtIBdxDRbWnSqIBAjG%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMD8NbrOsA5SD%2F5VVDKtwDg7pIpuFaGXvqyyqeP%2BRo0K21zlxQdFYGuMsx59m8lwVQDBMlq4AZHPsidjo1IzX37l2We1iCml18jEWFrDYyNetNVhu7RL57%2FOvfcD4EoesxqmyKGdAl6b61QoGbHHR4%2FI3AXhsMBgYVs9%2BGM5OFoGBKwk0oVPMXXYWq6%2FntzdEJtg%2FQozZB%2B19MARCuNArwoABdO26Ld9FH53PTtuWPv%2FlGlaa9bi%2FRRgT6LJtMuMTiJFaocaGvkOXPUpkt48WgISf6pswTEW7C%2FGXnWDgEOsaVxMdjmaD0WUELVHgCfJfCx7kXZkqezTK%2FEyAUv%2BBb1Xn07tVgQkvZV5yZFDF7X0Tynh1Fv%2BtpPhdnsvuNBt8pNCvUZRipmBv9HvYkIYQumxjgUAYDWNzI%2BPAh8RDwElf8HqZ6Mx8%2B6a9IfsdFaJgnzxsoRk8pO1zJG2nzSvKIN%2BX3b47YyNapvbqfB3bLarjMIrWTZnWCGQG6YrEnxTeaSKPC1WUuZPu342O5CYyBT6UxjV4DssXIMNJ9EjY83iGjEwNG3toY%2FmK%2FYT71cyisFW4ePoVxfmVQF6P8zrZdNFL6n%2BZlG1mxmSbHbHjEhGvM4QSoh%2FRwTUdP7%2B6gqHykIM7lNsBnASab1jYwmLf%2F0gY6pgGjAFRRVVdC7repXnP7Jr7YUu0P2x%2BS0yJwU%2BF9XTnGeeILunteLMGSI8hV7wa0LaQYEC0%2F8XhWmIytRA18Qi5dxXX7l3CbGofkt8kEUAHyJLTcGikx%2BEF2OM%2BJh2yfQIsh%2Ff6FjAVPibdd%2BVlnwX6TE34hyx30dIWUfEmDh9Q1iNgi3i33WKu%2FTnvHXyOuo2roKf4Emyr7IQyRHny4WB6Oq0Zbei%2Bg&X-Amz-Signature=34ef2dedbad499bc0fe445a44fbbbbcfa1519d9a70229af1c6d91c28c01fab74&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

[image](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/9cbeb917-878b-415f-915f-38e721c252e0/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664KWZKA6C%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T225142Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIFBIm3qN7OrDoH4PREWFPAhJEV%2Bo9gYI7MVrXYH38l99AiAoYQXSKieM36FW3SG90KG%2BBs31WioQiGgtIBdxDRbWnSqIBAjG%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMD8NbrOsA5SD%2F5VVDKtwDg7pIpuFaGXvqyyqeP%2BRo0K21zlxQdFYGuMsx59m8lwVQDBMlq4AZHPsidjo1IzX37l2We1iCml18jEWFrDYyNetNVhu7RL57%2FOvfcD4EoesxqmyKGdAl6b61QoGbHHR4%2FI3AXhsMBgYVs9%2BGM5OFoGBKwk0oVPMXXYWq6%2FntzdEJtg%2FQozZB%2B19MARCuNArwoABdO26Ld9FH53PTtuWPv%2FlGlaa9bi%2FRRgT6LJtMuMTiJFaocaGvkOXPUpkt48WgISf6pswTEW7C%2FGXnWDgEOsaVxMdjmaD0WUELVHgCfJfCx7kXZkqezTK%2FEyAUv%2BBb1Xn07tVgQkvZV5yZFDF7X0Tynh1Fv%2BtpPhdnsvuNBt8pNCvUZRipmBv9HvYkIYQumxjgUAYDWNzI%2BPAh8RDwElf8HqZ6Mx8%2B6a9IfsdFaJgnzxsoRk8pO1zJG2nzSvKIN%2BX3b47YyNapvbqfB3bLarjMIrWTZnWCGQG6YrEnxTeaSKPC1WUuZPu342O5CYyBT6UxjV4DssXIMNJ9EjY83iGjEwNG3toY%2FmK%2FYT71cyisFW4ePoVxfmVQF6P8zrZdNFL6n%2BZlG1mxmSbHbHjEhGvM4QSoh%2FRwTUdP7%2B6gqHykIM7lNsBnASab1jYwmLf%2F0gY6pgGjAFRRVVdC7repXnP7Jr7YUu0P2x%2BS0yJwU%2BF9XTnGeeILunteLMGSI8hV7wa0LaQYEC0%2F8XhWmIytRA18Qi5dxXX7l3CbGofkt8kEUAHyJLTcGikx%2BEF2OM%2BJh2yfQIsh%2Ff6FjAVPibdd%2BVlnwX6TE34hyx30dIWUfEmDh9Q1iNgi3i33WKu%2FTnvHXyOuo2roKf4Emyr7IQyRHny4WB6Oq0Zbei%2Bg&X-Amz-Signature=23621e510d652d0c454ba36bb54baddf1eed7b3ffec9c571a868fbd19c40f00c&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

那么上一节我们讲的这个过滤器使用的是这个 range 那么其实不仅是使用 range 你可以去使用侧面也可以。就比方说在我查询出来这个墨扣网游戏培之后的一些内容之后，那么我仅仅只想去把某一个 birth 去做一个过滤，那么其实也是可以的，你把它作为一个 term 去做一个过滤也行。比方说在这里去把这个 range 改成称。然后在这边你把这个 birthday 写过来，再把它的日期你想要去过滤的日期给拿过来，再去进行一个搜索。在这里的话你也可以去搜索，这里的话就是精确到了只有一条记录，那么也是可以的。那么像这种情况的话，在有一些的一个搜索界面上，它也会有一个日期的日历选择器，可以让你去点击去筛选。那么其实也是可以通过这种方式去做的。OK ，那么这个是它的一个策略。


好，那么随后我们来讲咱们的一个排序，就是说我们如果说按照我们之前做一个 range 了以后，那么你会发现在这里其实我们在这边可以来看一下它的一个年龄或者说是它的一个金额。像这个年龄排在第一条，这是第一条年龄的话是18。那么随后我们再往下这个是20，再往下这个是25，那么它其实是一种正向的排序。那么其实这个和排序还没什么关系，因为在这里它其实使用的是 score 通过这 score 去排的。比方说我们在这边想要去做一个倒序的排序，我们完全是可以去做到的。在这边我们就会使用到一个新的元素和我们这个 query 也是在同级的一个顶级的元素叫做 sort 那么这个其实就是一个排序的意思，那么使用起来是非常简单的。那么这个 sort 我们平时在数据库里面做一些排序的话，我们是可以有多种多个针对于多个字段的排序。所以在 ES 用其实也可以。那么在这边你可以完全使用一个束缚去排。那么第一个比方说我们先使用这个 H 做一个排序，我们就可以这样子写上一个对应的 H 然后你的排序排序的话其实是有两种，一种是正序，一种是倒序。那么正序 ASC 倒序 gsc 我们点击 send 去排下。


那么然后当我们使用 A 级去排了以后，那么现在我们就是年龄是25，然后其实在这边会有一个 sort 有一个 25 再往下22，随后最后是一个 19 再往下18。OK ，那么这这个其实就是把数值的从高到低，那么你改成 as C 的话，那么其实也行。在这里一开始是18，在十九一直是正向的排序。那么当然我们也可以使用组合的排序也行。在这边我们可以去为他加上一个 money 这个 money 我们可以去从低到高去排，先去排，排完之后再去根据这个 age 去排。所以我们在这边你能够看到的就是一个 sort 再是一个五十五点八二十二对吧，这个是它的一个金额，金额是最少。随后再是一个66.8，再一个是它的88，再到155，最后到这个156，然后就是 1000 多。那么这个它的一个金额是逐步的提升的。


那么你在使用gsc ，那么这是一个倒序的排序， OK 吧，那么这个是可以的。那么像这种方式，其实我们在搜索一个商品的时候，那么其实这种排序是会用得到的。像我们在使用这个淘宝，比方说淘宝的话，你是可以在这里有一个价格对吧，价格从低到高价格从高到低。那么这个其实也是类似的一个道理，除了使用这种，我们现在是针对于这种数值，像这个是金额还有是年龄，甚至于我们使用这个 date 类型 birthday 也是可以去做一个对应的排序的。


那么现在假设我想对我这个 nike name 去做一个排序，可不可以呢？我们把这个拷贝过来，针对于我们尼克内，我们来做一个排序，我们来看一下会不会发生一些问题。点击 send 那么在这里会报一个错。会说我们当前 nike name 是无法去做一个排序的，就说排不了对吧。为什么呢？这个主要原因是我们这个尼克利它是一个 text 它是一个 text 的一个类型。那么 text 类型目前其实我们只是对它做了一个分词，再去做了一个检索。那么试想一下，就是说我们在这个索引库里面倒排索引里面其实有很多，针对于这样的一个尼克利姆去做了一个分词对吧，那么它会有很多的分词。那么你要去做一个排序的话，其实就会写得很乱，而且会很难以去做排序这样的一个功能。所以你单单使用这个 nike name 去排的话，它是不会让你去排的。


除非你可以使用另外一种方式，就是为我们的尼克 name 去增加一个附属的属性，也就是使用一个 keyword 的一个类型。为什么要使用这种方式呢？其实我们可以来看一下，我们使用 user name 去做一个排序点击线的，那么你会发现是可以的，这是为什么？因为这个 user name 我们在设置的时候，它本身就是一个 Q word Q word 它是不会去进行分子的，不会去进行倒排索引的，所以它本身就是一个一整串的一个字符串，它是可以去做一个正序倒序的，这种排序的是没有问题的。对于我们的 make name 来讲的话，尼克利它本身就是一个 text 文本，它会去做分词的。所以如果说我们想要对我们的尼克利再去做一个排序的话，那么我们就可以去为它去增加一个附属的属性。那么这个附属的属性它的类型就是 T word OK 。那么这个其实我们在课程的一开始前期我们是有提到过，我们可以看一下，打开我们的 head 然后去看一下我们的 my Doc 这个文档这个文档里面其实有一个叫做 fields 对吧，这个 fields 然后看一下这里面有一个 keyword 然后这个 Q word 其实就是这个 name 的一个附属的属性，它的类型叫做 Q word 所以当我们要去针对某一个文本再去做排序的话，我们就可以去使用这个 name 的一个附属属性，也就是 name.q 的去做一个排序。那么是可以的。 OK 吧。接下来的话我们就可以使用这种方式来做。


首先我们先来创建一个新的索引，这个索引的名称我们取一个名字叫做 shop2 shop 点击。 OK 好，现在已经是创建成功了，在这里有我们可以去看一下他的信息，这个 mapping 里面现在没有任何的内容。接下来的话我们就可以去为他设置一个咱们的索引。我们去为它做一个 mapping 的一个添加。打开 POS 面在这里面我们可以这样子，我们把这个拷贝一下拷贝到这里。然后使用这个 post 那么当然它的一个 body body 要使用这个 JSON 好，随后在这里面你是需要去设置一堆的内容，那么我们可以快速的去手敲一下。


首先第一个你要去为它设置一些属性，也就是 promise 好，那么它是一个对象，在这边的话我们还是使用手插的方式。好。首先第一个属性，我们试试这个 ID typetap 在这边我们简单一下使用它的一个浪。好。随后第二个，那么第二个我们可以设置为一个尼克 name 在这边我们给它增加一个菜盘，然后这个菜盘很明显是使用的是 text 然后我们要去为它设置一个分词器 anylike 那么我们使用的是中文分子器 IK 下划线 maxword 随后的话这个如果说我们直接去进行一个 send 去保存的话，那么我们就会创建一个 ID 和 nike 这两个属性，对应的 mapping 都会去创建。这个时候我们是由于想要对这个 text 去做一个排序化，这边你可以去增加一个额外的属性，我们都可以为它设置一个 fuse 那么它是一个对象。随后我们可以为它去取一个名字，我们就可以为它叫做统一的。如果说所有的 tax 文本你都想要有这样的一个属性的话，你可以取同样的名字都叫做 Q word 都行。之后，这个 Q word 你要去为它配置一些相应的内容。那么其实也是一样，这个 Q word 这边拼错了，这个 Q word 其实就是我们的一个对应的 make name 你把这个它的 type 复制一下，然后把它的类型改成 Q2 的这样子就 OK 了。


好，那么现在我们可以点击发送去看一下它的一个结果，为了演示的话我们只设置一个 nike name 就可以了。其他的一些属性我们就不去添加了，点击现在。好，然后在这里出了一个错，有一个 nok 就是说 practice 看一下是否拼错在这边应该是 P 吧对吧， pop 点击线的。然后在这里又报了个错，说我们的一个解释出了一个问题。那么这边很明显没有这个我们是没有拼错。


检查一下我们的一个 URL 这个 URL 写的不对吧，我们要去建立 map 的话应该是这样子，我们是使用在 shop 2 的一个下方去建立一个 map 点击 send 好OK ，建立成功。随后我们打开咱们的 head 做一个刷新。那么这个时候我们再来看一下咱们的 shop 号，这个时候你会发现咱们这个尼克 name 它的一个菜谱下方多了一个 feels 这个 feels 它其实就是尼克 name.keyword 它的一个类型就是 keywords OK 。好，随后这个时候我们可以回到咱们的 postman 那么在这里我们可以去做一个对应的排序了。不要忘记，这边应该是针对 shop 2 去做到的一个搜索。然后我们点击我们现在还没有数据，对吧，我们去为他加一下数据。那么这个数据的话我们也是模拟的去加一下数据就可以了。这边我们是下划线 Doc 这个数据我也是预先准备了，直接拷贝进来就可以了。好，随后下一个我在这里准备个五条数据，然后他们的 ID 我就不去为他设置了，让它自动的去生成使用一个字符串也可以。


好OK ，那么这几个创作成功，到我们这里面刷新一下，去看一下它的一个数据浏览在社报里面。好OK ，这些数据都已经是有了，然后我们就可以去做一个对应的解锁。那么解锁的话到这里我们搜一下这边我们其实是搜不到的对吧。那么我们把这个其实我们全部都拿掉，我们这样子我们先来做一个所有的内容的一个数据的检索。总共是有五条记录对吧？有了这五条记录以后，那么我们再去做一个 sort 我们直接去搜 chicken 你会发现它还是不能够去做搜索，因为这个尼克 name 是它的一个主属性，它的一个附属性的话其实就是我们的尼克 name.q word 你要这样子去加上一个点 key word 然后再去做一个 send 去做一个搜索的话，那么这个时候他就可以根据我们的这个 Q word 里面的一个规则去做排序了。


那么总共是有五条可以看一下，这边是一个飞翔对吧，然后是美丽再是漂亮对吧，这样子做了一个排序，那么你把它改成 ASC 的话，那么这样子它的一个顺序就相反了。Ok 。好，那么这样子其实我们就针对于这样的一个 keyword 比如说文本进行了一个排序的设置。那么在这里我们来提一下。


就说一般来说，其实在我们进行搜索的时候，其实很少会使用到针对我们文本类型的一种排序其实场景相对来说是比较少的，我们就拿这个淘宝的搜索为例好了，当我们去搜索一个手机的时候，我们查询出来的内容我们要去做一个排序的话，往往我们其实都是针对于这种价格总价或者说是它的一个信用的分数的一个从高到低或者说是它的一个销量，其实都是针对于它的一个数值的排序。


如果说你要去使用一个文本去做一个排序的话，那么很有可能它排出来的内容并不是用户想要去搜的内容，它的一个匹配度其实会相当的低，它的一个相关度也是分数会相当的低。所以说我们这种排序的话，往往我们使用这种，像销量、信用这种价格去排，那么基本上就 OK 了。那么或者你可以在这里再去加上一个区经，也就是我们前面所提到的一个 range 去做一个这种搜索的话，那么其实就可以为用户提供更加精准的一个搜索服务。那么基本上这样子就 OK 了吧。

[image](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/e7cf6942-2b67-4659-a1c3-d8cd16cd685a/2020-09-17_175516.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664KWZKA6C%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T225142Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIFBIm3qN7OrDoH4PREWFPAhJEV%2Bo9gYI7MVrXYH38l99AiAoYQXSKieM36FW3SG90KG%2BBs31WioQiGgtIBdxDRbWnSqIBAjG%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMD8NbrOsA5SD%2F5VVDKtwDg7pIpuFaGXvqyyqeP%2BRo0K21zlxQdFYGuMsx59m8lwVQDBMlq4AZHPsidjo1IzX37l2We1iCml18jEWFrDYyNetNVhu7RL57%2FOvfcD4EoesxqmyKGdAl6b61QoGbHHR4%2FI3AXhsMBgYVs9%2BGM5OFoGBKwk0oVPMXXYWq6%2FntzdEJtg%2FQozZB%2B19MARCuNArwoABdO26Ld9FH53PTtuWPv%2FlGlaa9bi%2FRRgT6LJtMuMTiJFaocaGvkOXPUpkt48WgISf6pswTEW7C%2FGXnWDgEOsaVxMdjmaD0WUELVHgCfJfCx7kXZkqezTK%2FEyAUv%2BBb1Xn07tVgQkvZV5yZFDF7X0Tynh1Fv%2BtpPhdnsvuNBt8pNCvUZRipmBv9HvYkIYQumxjgUAYDWNzI%2BPAh8RDwElf8HqZ6Mx8%2B6a9IfsdFaJgnzxsoRk8pO1zJG2nzSvKIN%2BX3b47YyNapvbqfB3bLarjMIrWTZnWCGQG6YrEnxTeaSKPC1WUuZPu342O5CYyBT6UxjV4DssXIMNJ9EjY83iGjEwNG3toY%2FmK%2FYT71cyisFW4ePoVxfmVQF6P8zrZdNFL6n%2BZlG1mxmSbHbHjEhGvM4QSoh%2FRwTUdP7%2B6gqHykIM7lNsBnASab1jYwmLf%2F0gY6pgGjAFRRVVdC7repXnP7Jr7YUu0P2x%2BS0yJwU%2BF9XTnGeeILunteLMGSI8hV7wa0LaQYEC0%2F8XhWmIytRA18Qi5dxXX7l3CbGofkt8kEUAHyJLTcGikx%2BEF2OM%2BJh2yfQIsh%2Ff6FjAVPibdd%2BVlnwX6TE34hyx30dIWUfEmDh9Q1iNgi3i33WKu%2FTnvHXyOuo2roKf4Emyr7IQyRHny4WB6Oq0Zbei%2Bg&X-Amz-Signature=3b7536fdcc39efb70b03946fe4f3d70a24a8aba85512dc3ae173bdc7ed3d135c&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

