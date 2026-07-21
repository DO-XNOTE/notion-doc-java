---
title: 3-2 商品评价 - 实现评价等级数量查询
---

# 3-2 商品评价 - 实现评价等级数量查询

[image](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/9720409c-c01a-42fe-99e9-a21b472ea076/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466T6XAU2DP%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T224644Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIED6DnKNzh9FTPq9WT%2Fg32jTVmtxlOhyOMnBNDkKBl9NAiBsgiBCSP9qJIxevfH8fv%2FGM5FQnaer2t6IyJhaJT8sLSqIBAjG%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIM%2BTZ3yC1Xydz2ZPCeKtwDMkpQ0irJ66geIebO2I1RT5vIx1IzPhgxRYHX1khMCeCaPbOWiQ4Dw7NKWJRilrOCZEEpQPbCeDrS%2FbIdGwA7pLKIQfJcz3oQxGX6kjDLeRm7YI00qIwUNrMNNP%2FYVi2bsRtAKPZ64gYwR9dQlS0JKtS4x8z9bEu66cUecKjCjIbxJZw%2BwkO3bSYWeEXBw2Yj7%2FvKs21JQcACbxNuI%2Busq7eUj%2BlgxSxCgXSDfKQFT6DQcnm7v4nBk1ZOqcEAvSS%2FunaW4lsNwcEQA1yY7BzOu2%2Bux%2B%2BFWXnMKXqxW5Z7Bt3mlM7qJ8VwKxApDUfsirnnhZh5Q23%2BnWiwwTnTHrERDmCqWfr7hAyKRl8A8BnzISpwBg1Wj0h8p1c05%2BS%2FgscKsSmddP9AN4qyPqA0OWhCT1anV3OvEEET%2FiU8B3T0nb4K%2F1l%2FRl0mS1fX2V1HyYMJY5bBG7DfcobdKhZT0gA74GoAmL5c6iZb1uxdo7ANcNsF5eHtIW%2BmKHrbVfhZ7I1p2CCnyGPzMg9L2XXGOJyVQmI0RzB%2FbyJFAQcoRBcouLVKGnOxUZjaTd%2FTLJd%2BVxnjIruA2%2BywBX1kejii6nUod7E05KhbEg00z3pxlQArBCurCwcpbr%2B5fAYyVTwww7f%2F0gY6pgFDVgH9c0Upm1xxA%2FuoLzFLAL3jMEm6AoCd7taNuDE6oO0PwkEOkZ2CNlbKuxYT8iNX4nma4bKvC7t6gegjJi9GNRYCynJ0uHSkyxzOfOAUQ7IlCfYxEybdsWdlkq4CxkzCdr2AKRToAN0YM0tXpVakCh3X9thIOupBWALEYJMU2FZDVrId3uWuvKqTeNGWuLdSfb0Z59EpaxrpvNBlWBkXj98Y6OZ9&X-Amz-Signature=3f765630bed62967c28bd397781283c9727588fea8b672bbbd191a2f6b543490&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

上一节我们是讲了商品评价相关的一个功能的解析，这一节我们就可以先来实现一下内容也好，评度以及是商品的一个不同的等级的评价。好，我们可以先回到开发工具，评价是和商品相关的，所以 control 了。 service 我们目前也都有。好，先来写一下咱们的service。在这里我们是需要去查询comment。COUNTS。在这里面其实包含了三种类型。


先写一下。我们是需要传入一个商品的ID，好评，中评，差评和全部的评价数我们都是要查询出来，这是根据 ID 查询商品的评价等级数量。在这里我们会返回出一个VO，这个 VO 目前我们先来定一下这个VO，我们可以先到 Poo 9 层。先写一下，我们在这里可以来取一个名字，可以写上这是一个 comment level counts feel。名字稍微有一点长，但是没有关系，在它上方加一个注释，这是用于展示商品评价数的CEO。在这里面我们就需要去写上 4 种四个数量。第一个是 total counts，这个是代表所有的。此外还有是好中差分别，我们可以来写一下 good 代表是好评，中评我们就可以使用普通normal，好差评就是一个 bad counts。好。随后我们申请一下 get 和 set 好 OK VO，我们就已经是建立好了。好在这边改掉，把包给加入进来。我们就需要到我们的实现 service 里面去进行一个实现了。把这个方法给进行一个重写，由于它是查询的，所以我们使用事务隔离，使用 suppose 就可以了。


在这里面我们其实就应该要进行三次查询，好评，中评，差评都要去进行查询，把他们查询的数量累加合计一下，就是一个 total count。既然是有三次查询，其实我们可以写一个通用的方法。在通用的方法里面先可以写好，在这里面发起一个调用也是可以的。我们可以在这里写一下定义一个 integer get comment Cos，传入进来的，相应的就应该是不同的等级。首先一个 item ID 你是需要去传入的，另外一个是level，我们定义为就叫做联络。好在这里我们就可以去发起一个请求了。


之前我们其实都是使用的 example 对吧？在这里我们可以使用单独的一个polo，也是可以去查询的。我们在一开始介绍的时候其实有提过，这里是 items comments，直接来一个肯定行，因为它我们是把 polo 作为是一个条件了，把它给用出来。用出来以后，首先第一个条件就是一个商品的ID，也在肯定是里面，我们是需要去 set item ID 把放进去。有了以后，现在我们第一个条件就是根据商品的 ID 会去做一个查询。随后我们就要根据 level 去做查询了。在这里我们应该要去判断一下 level 不为空，不为空的时候，我们才会在 condition 里面点 set 去设置一个level，把 level 给传入进来。


OK，好，条件设置好了以后，我们就可以去做一个查询了。查询我们先来看一下map，我们还没有引入进来，所以我们要去做一个引入。 items comment mapa 好注入进来以后，在这里我们就可以去写了。 item common map 点select，在这里会有一个 select count，其实我们在之前我们还暂时没有用到过，从它的字面意思上就能够看得出来，它是去查询一个 count 数的。也就是现在我们在 condition 里面设置了两个不同的条件，它会根据这个条件去查询它的一个记录的总数。OK，在这边我们把 condition 直接拿过来就可以了。最终它会返回一个 Int 类型返回。在这里我们可以直接 return 就 OK 了。好，由于它也它查询是包含事物的。既然是查询，我们事务隔离把拷贝过来，使用 suppose 就可以了。在这个部分，它调用处也就是我们的service。在这里其实我们是会发起 3 次请求。好，我们在这里可以写一下。


首先我们是定一个 total counts，是等于 get comment counts。这个我们先不写，我们其实可以去做查询，也可以不查不查。把三种不同的评价的总数加起来就可以了。先把 good 先查询出来，这是一个 good counts，等于 get common 的counts。在这里首先第一个商品的 ID 外键是需要去传入的。随后我们就应该要传一个等级，等级设置为 1 就可以了。但是其实我们在之前也已经是过这种东西，由于是数字可变的东西，我们尽量要写得更加的通用化，所以我们还是会写上一个枚举。在这里我们可以去创建一个。我们拷贝一个 yes or no，改一下，把改成 comment level。好，这个枚举就已经是有了。我们在这里面去做一些修改。这个是商品评价等级的枚举，等级总共是分为了三种。我们在之前其实查看数据库表设计的时候，其实是有相应的对应的，所以我们写一下。第一个是good，它的 type 是1，值，我们设置为好评。随后下一个是 normal 中评， type 是2，再拷贝一下。很显然第三个就应该是 bad 差评，分别是 123 差评，中评。OK。这个枚举我们现在就已经是构建好了，以后在这里我们就不需要直接去填一了，因为这个是不太好的。使用 comment level，点 good 点 type OK 好。


这是第一个查询，第二个查询应该是一个 normal normal counts，再来一个 bad counts。传进去的值分别是一个 normal 以及是一个 bad OK，好。这三个数量都有了，以后对于我们的 total 总数只需要让他们进行一个相加就可以了。当然你要去发起一次查询也可以，但是尽量减少和数据库的交互是更加好的一种方式。好，OK。这样子。这四个数量现在都已经是全部都有了，以后我们是需要去把它返回到我们的一个前端，让前端去进行接收。这些cons，我们可以统一的把它放在一个 feel 里面，也就是我们在之前所定义的 comment level counts u。在这里我们直接把它给 new 一下。


counts u。分别去进行一个设置。set，先是一个total，把 total 放进去，随后一个我们都能够放进去，第二个是good，随后再来一个normal，最后一个bad。好，OK。设置好以后直接把 VO 给 return 出去就行了。好，现在我们 service 就已经是 OK 了。 OK 以后回到咱们的 Ctrl 了，在 Ctrl 里面去写一下。我们也是参照前面的把拷贝一下。以后在这里面去做一定的修改。先来改我们的 swag two，在这里应该是查询商品评价等级。


好，再来一个商品的后面的notes，把直接给覆盖过去就行了。 HTTP message get 就行了。在这里会有一个路由的请求，现在我们可能不知道，也没有关系，我们可以到前端去看一下。这是前端的源码，找到 create 的生命周期。在这里会有一个渲染 comment level count 全局的搜一下。在这里看到这个就是它的一个路由的请求地址。把 comment level 拷贝一下就行了。贴到这个位置，随后你还能够看到它。还有一个参数，就是 item ID，因为是我们要根据去查询的，所以我们会作为一个参数。需要注意，现在我们就不再是一个路径参数，它是一个请求参数了。在这里我们不再使用 pass variable，我们使用一个 request request pen 使用这个就行了。 info 改为 comment level 好，OK。这个方法我们是定义好了，是一个商品ID，这样子定义好，OK，没有问题。在这里要进行一个判断，我们就保留了。不去动。下方通过 item service 来一个 query 查询。 comment counts 把 ID 商品 ID 给传进去，获得的 level counts VO，我们就可以在这里直接去定义抗CPU。



好。拿到了以后这些我们都是不需要，我们直接往 m 结算， result 里面一丢在前端我们就可以去接收到了，OK，好。现在我们就可以去进行一个测试。我们先全局的 install 一下。好， install 成功，重启服务器。


好，OK，我们就可以打开咱们的。我们先来看一下。 swig two，刷新一下。在 swig two 里面，我们先来看一下。有一个查询商品评价等级，点击过来，在这里会有一个商品的ID，我们可以把 cake 1001 直接贴过来拷贝。传到这里，我们来测试一下。点击发送。OK，我们可以查到总数是23， good 是1472，全部都可以查询到了。我们可以回到咱们的商品页面，商品太大了，我们缩小一下。好，我们刷新。现在刷新了以后可以看到，在全部评价里面，好评度现在是100%，我们是可以获得到了。在这里全部好评，中评和差评他们都是零，因为在当前商品里面，我们并没有做任何的评价，我们就可以换一个商品，可以再来看一下，比方我们换这里的第一个，它其实就是 k 1001。点击一下。


好，我们把鼠标在这里全部评价。点一下你会发现全部好评，中评，差评，这些数量全部都有，好评度是61%。其实它是会进行一个计算的。OK，现在页面上我们显示是成功了，我们可以到前端页面去看一下。在前端的页面，在这里其实它进行了一个判断。我重新再来一次。我们先找到它的一个level，它有一个渲染的level，我们先可以回过去。在这个部位，这里是我们发起的一个请求。发起请求之后，我们获得一个 counts view，这个 counts view 我们通过 this 对象可以赋一个值。现在在我们的整个页面里面就会有这样的一个 view 了，因为它是通过数据绑定它，因为是 MVVM 这样的一个框架。页面里面当有了这样的一个对象以后，我们就可以去获取里面相应的值了。好，我们就可以来查询查询，在这里我们是可以去查询到的。我们就可以看到在 Div 标签里面，我们会有两个判断，第一个判断会判断我们的总数是不是为0，如果总数为0，默认我们的好评度就是100%，如果我们的总数超过零，我们就要去做判断了。在这里其实我们也能够判断的出来。首先我们是先要拿到它的一个总数，这是一个好评的总数，除以它总共的评价的一个数量，除完了以后乘以 100% 就可以得到一个百分之了，这就是它所计算的一个好评度。


OK。这个是用于去计算并且展示百分数。下面在这里它是会把相应的内容进行显示的。一个是 total counts，另外是一个 good accounts，还有是一个中评和差评。在这里全部都有，都可以通过 Moustache 表达式这样的标签去显示出来。 OK 好。现在其实我们在商品详情页，在评价里面的第一个小部分我们就已经是做完了，OK。

