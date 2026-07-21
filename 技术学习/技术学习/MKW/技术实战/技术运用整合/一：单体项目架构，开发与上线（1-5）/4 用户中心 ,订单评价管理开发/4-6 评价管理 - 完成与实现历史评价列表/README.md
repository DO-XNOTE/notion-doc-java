---
title: 4-6 评价管理 - 完成与实现历史评价列表
---

# 4-6 评价管理 - 完成与实现历史评价列表

[image](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/f62decc3-b09e-41ba-bb8f-58020c6771d3/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QHJGFDBM%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T224740Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIGKi%2FhRIDCg3zJgIZ8pbKk74Uc0dAoQawEllu0N2P8OQAiEAjZufNJmLHqvG1nTfrvBmlof5P9ZAZaRAUi3N3SBUcW8qiAQIxv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDIN00xyuO%2BiR%2B%2BClyyrcA5ZIduaheNNYTXQODoIhoopSjqZmH4X4iFSRZDFdZUftvj1yuL5LqNhBi9wSe4ag3ivjxteA2%2BUXkTfatK3qiBtlZ00BXCagXoBXZWFz7irvN16eCRiSBLKVbaCOMWGI4tHWiErge%2FlNKEPobSg3rXEBqKncInZa5IJRE%2BayLjF4ijDGqT4RxuWHi5FCGf7RNRJUF4Vk5qYEkT0c1p8nkJXa33jO30cRW5Ymronlj70XVv48ImTlx9RvccshiNCv6cTrbPIMbUFV34QmYb5L09M3X%2BQ79PuEtmIOyBJHZtl%2BHE6EQtCHLcg%2BqdIZWW7qvkR8TfMkPptpIZrWWAG%2FtuSswRQul0eKtUU%2FLbGZhqrSoHO7laGeg2z1t3kZjiSFT7r%2BJdVJXsPOlcmpSuKgV%2FwuqkKk1nX18hLvQKaSWwkwZ%2FyEZNfXGKQC0TojkP1IQmUkWxbdJmfyoPvgBZuHnkcMcNYPET0bM%2BlAQdM2FMjis2ba4IAlHfAkD85IiCW06LbGX4F8kkomdgBezlZtjADN%2B4KZmVRz972ouj8ODbRHKoRfOAGTdy%2BOpWUq5jO8vjDO026TEFIOA7hVHbjHQXa6NDvZmLkse66PyQtBdREVEHPjaAkHLZ5ukloiMNe6%2F9IGOqUByqGkbdW0s8XSROu7lKrenZZbZ3ffy0PlI4DOj%2BbKpFWgOjokkWmfW6%2FjOu6WswBJRwn5Swl%2BNaqSSYCdxHY0rCi105r9UF%2BtnN%2F%2Bni8GoXOj0C7HTRpRzpcJudqEIGRM%2BUDkkRgYHLPxHPaHjrTSx0uzH%2FpOKPvdVaMdX4XO5z1fNsOVU2%2F%2FHr%2B76M9aR2%2F%2Bxx%2BaEfNu0t91z4ANhYTRrlHfTwBI&X-Amz-Signature=eee9f3d21d441db8a76c64b755272798c8e2cbbb7671e31d63fed328e607ed3e&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

上节我们是写了查询我的评价的 Mapper 以及实现后语句。接下来我们应该要去把 controller 以及是 service 完善一下。我们先来看一下前端，前端对应的是叫做 comment 点HTML，把这张页面可以打开看一下。在这个页面里面，我们是可以找到 create 的，这也是生命周期参数。其中它会有一个调用的脚本，叫做render。 my comments list，这个是用于去渲染评论列表信息的。这一段内容它会传入两个参数，一个是 page size，这个是用于去分页的。我们不去多说了。分页我们前面都已经是讲过。在这里我们会发起一个请求，这是请求的路由 my comments 杠 query 传过去，当然是用户的一个ID。随后分页的两个参数，一个是 page test，都要传递过去。好，当我们的请求成功以后，拿到 result 进行一个判断，判断是 200 了，我们会获得一个分页的 grade grid，里面会拿到对应的 list 整个列表。这个就是我们在页面上需要去进行一个渲染的内容。


随后进行一个 for 循环。主要的目的是要把 date 类型的一个留言时间要把它去做一个更改，更改成一个年月日的格式化日期。随后在页面里面就可以去做到一个相应的渲染了。在页面里面是根据 my comment list 去做渲染的，可以去找一下，在这个位置有一个 before 这样的 for 循环。通过 my comment list 拿到里面每一项的元素就叫做comment，针对 comment 去做一个循环。


OK，这里面每一项元素都有，这是图片，另外这是商品的名称，这是留言的内容，这是规格等等信息，全部都会有。OK，好。接下来我们就会根据下面的路由去编写一下咱们的 Ctrl 了。好。到我们的 Ctrl 里面。在这边其实我们是会涉及到分页的，对吧？分页我们在这里直接去找一下曾经写过的，做一个拷贝就行了。既然写过的东西就没有必要重复的。再去造轮子。好过来是直接可以去使用的。到我的订单这里面去找到，找一下。分页的内容都是分页的，所以把这一段的内容全部都贴到这里。


接过来以后，在相应的其实也是一个 query 查询订单列表改一下，叫做 query 我们之前所写的这一块内容。这个方法其实写的不是很对，对吧，不太规范。我们把它也改为query，这样子会更加的好一些。好，先把我们 swaga two 名称改掉。这是用户中心不用写查询我的评价，好对应到前端所使用的一个方法。它是使用的post，所以我们在这里也会使用 post 传过来。对应的会有一个用户ID，以及是一个配置和 page size，中间我们就不需要了。


好，这样子 3 个参数在这里我们就写好了。写好之后在下方首先判断一下用户的 ID 不能为空，这两个是默认的，是需要去写上的。下方这一个是great，是调用我们的service，在这里会直接调用 my comment service。 service 里面目前没有对应的方法，所以我们去写一下。在这边写上public，需要返回一个 grid 配置的 grid results。这个方法名叫做 query my comments。


需要传入相应的几个参数，第一个参数 string user ID，随后是 page 以及是 page size 都写一下。好，这是咱们的设备方法，把注释给加上，这是我的评价查询分页。好，随后到我们的 service 里面去把对应的实现要去写一下。在这边我们这样子直接把这个方法给引入进来，把事物给加上事务，在这里使用supports。好。OK，我们换一下行吧。在这里面就要去调用我们之前所写的一个map，会使用到 items comments custom 这个map，点 query my comments，把对应的 map 给加进去。在这里我们是需要把 map 去 new 一下的。它是一个 string object，这是一个电子盾。现在我们传入一个参数，你写一个 string string 也可以。但是为了做到通用化，一般我们都是写一个object，这样子会更加的舒服一些。好在 map 里面去把相应的值给塞进去。 put user ID。


好，OK，这是我们的一个条件。再把 map 直接给丢进去了。以后我们就可以去执行我们的一个查询了。但是在这里我们是需要去执行分页的，所以在这里会使用 page helper 变 start page。第一个参数是page，第二个参数是 page size。好，这样子可以做分页。分页完了以后，在这里会获得一个list，这个 list 类型是 my comments b o。写上 list 等于好。


拿到了 list 以后，我们要去做一个设置，把里面信息都要拿出来，把一些信息以一个配置的 grade results 给返还出去。找一下我们之前所写的，我们从我的订单里面去搜到对应的这个方法。在这里会有一个 set of grade，这一段内容我们其实是可以拷贝过来。


还有一种方式，我们其实之前也说了，我们在这里可以去写一下。在我们当前的里面，我们是可以去创建一个class，这个 class 就叫做base，或者你可以取名叫做basic， basic 都可以，我们叫一个 base service，在这里我们就可以作为 service 去加上一些通用的方法。内容都可以写一下。以后在这里面我们就可以去写了。写一个就叫做 set up page 的great，在我们当前的 service 里面，在我们就可以多去继承继承了。以后在我们做分页的时候，我们加错地方了，这是订单的service，把 service 关掉，我们到评价的 service 在这边，评价的 service 是在这边，我们把这一段内容给加上。加上了以后在下方 return 的时候，我们就可以拿一个setter。这个方法名叫做 setup page 的grid，应该要改为private，它是使用不了的对吧，所以使用这个就可以了。 set 配置的规则，把 list 传进来，第二个参数，再把配置传进来。这样子通用的方法就做好了。在这里我们就可以让我们的 controller 再去做一个调用很多了。在这个地方，在这里 query my comments，把 order status 给删掉。这样子我们拿到了一个 grade 以后，这个就是针对于我的评价所做的一个分页了。


OK，我们通用的方法是写在 base service 里面的代码，这一段都是重复的，这是因为我们在订单的一个 service 里面也有，但是我就保留了，因为大家也可以去看一下。当然你在后续去整合的时候，你可以去直接继承 base service 也可以的。


好，接下来我们进行一个重新的install，我们要启动一下。到前端去测试 o 不OK，好，启动成功。这个是 install 成功，我们再做一个启动。好，OK，到前端，我们可以去测试一下我的评价。点击一下。在这里你会发现又报错了，报了一个 500 的错误。 500 错误是在我们的后端出的问题，我们可以来一起看一下。


在这里面会报了一个错，说 there is no setter for property s， e p c name。我们映射对应的不对，我们之前是拼的有问题对吧？在 my comment view，我们到这里面去看一下。在 my comment view 里面，找到这里。 my comment view 在这个 view 里面我们取的名字叫做s， p e c name 对吧？但是在我们的一个自己的代码里面可以看到，在我们自己代码里面找到map。在我们自己里面写的时候，在这边属性没有映射对，我们应该写上 s p c name，这样子才是正确的。这一块是属于 VO 的，是属于我们的一个 SQL 脚本的。 SQL 脚本在我们定义的就叫做 s e p c name。所以你在这边一定要去注意我们的映射，映射的名称是需要一一对应的。当然把这两边全部都改为 s p c name 也都没有问题。


OK，好，我们再来做一个重新的install。所以像我们平时遇到异常不要怕，多去看，根据我们的异常去分析问题，这样子是非常有助于我们的一个学习的进阶。的。好。重启成功，再回到我们的页面，再来我的评价，点一下，OK，好。这个时候我们所有的内容全部都已经是查询出来了。我们也带有分页，总共是 12 条。点击第二页，第二页是有两条。在订单管理里面，我们还有一个评价商品版，我们可以随便写一下。我们来个差评，发表评论。好。评论成功。再到我的评价里面去。这个时候总共是有 13 条。这一条差评的记录在这里就显示了。OK。这样子，整个我们涉及到评价的内容，我们都已经是全部讲完了。

