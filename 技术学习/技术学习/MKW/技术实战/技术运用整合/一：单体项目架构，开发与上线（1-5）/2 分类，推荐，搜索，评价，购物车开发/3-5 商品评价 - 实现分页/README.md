---
title: 3-5 商品评价 - 实现分页
---

# 3-5 商品评价 - 实现分页

[image](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/524704b4-f20c-4bae-b4b6-2c689c1e06ae/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SMEZQEJM%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T224646Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCICV%2FMlX2O38%2FNlqwELL6ZWcSeD182FudhpslzkZoSRX2AiEAzqq9dVNvZ7XWPAKQTp%2FyflN99ChiGDxW5iLS%2FLxMZvgqiAQIxv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDD8eVgQC8p8MFJIiTircA1FC500CCbHvsAey3nqyXz9F5G%2BrO16QZ6mVmhlC%2FFqgOE%2Fcz%2BQbzA6f7E%2BkhndSMVHc04JK4LEoy1U7G9cE9QxivwxUvxF%2FyXoRLkKV3N4eBKAUH6%2FO0fi1A0PMHdnpQCDw0GPvzHVeusz4L8KuPdHFQG9wpmkbEcNrAmvu4sRioAepz8HSU0CIlWI6fF8qu190S5AhSXMr%2Fk8hy5tiWTgT6SX0wIfmCfWNoYPLW0UgdRbteSnNWhDoov1Zh76jKS3ITIjLNJG1ZZZ3h1wedWAMnsSdsnLWrSb9LOPVF0YAWVnVoG%2FN0MBgbMPL%2Fq%2Bg4sJvgVVuv669eT7w3egVCrjdgrdmkdy7OHDUNkE8INkWrxVDXfsbaBlSlgoLtMPEMKRknQwVgh698dNR%2BgeTnAaHrJCCbFmJFukOUIy08ExaU%2FQYIYqB4ULza%2B%2BNQ8BfmOvbhpsQh0NANjhmVVCifUngX1Min7PFFrDUp%2Fc0Gt1rwN%2FxsOvvXwv8PjajBuvRzubg%2BmNRnNN0rhtnPATyK6xyHyTXXlOWAQrpDNnGKltJQ%2BjChlAGIxyR1UZQZF0G7Mu6IVlqmpTOxgNofGeeNrCtcUHMZUfGCBYS9Yo6bm%2FbumlVWSpmOUbrdyz0MPy5%2F9IGOqUB2DjMPM7qPx6LmWSC29Hz%2BF%2BAXOEjKVAzehqZWbHZDZ5RZMfA6pNrvhvD8cN8ktwMgT3nhShH3rnqQGexgHB%2BBg6xwNtaT2OFWp9ziLk2To81Yju4h8uhVAuwotSfD9jzxNd2i9Djt6aPbIK%2FaXHffxEy%2BWYJjfPcdxFO95BSNs4T%2BkBPVQgU%2BSWYafO7j2pzEjQ3pwCGQ67jvPNGJ8PiApl8LpUj&X-Amz-Signature=71b79faf4d3eb10531cc459845232e89dade6a84b8aa716815aa26939686d5d7&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

紧接着上一节，这一节我们就来讲一下分页。其实在每个系统里面多多少少肯定是会包含有分页的。你要去实现分页，其实在我们编写自定义 SQL 语句的时候，你就可以使用 limit 就可以去做分页，自己是可以去做到一个实现的。但是一个系统里面如果有很多的分页，你写起来，你可能无法都做到一个统一化。


其实 my Betis 它有一个插件叫做 page helper，我们在这边写一下 my Betis。 page helper 从字面意思上就可以看得出来，它其实就是为 my Betis 提供分页的一个助手。它其实是一个插件，我们可以依靠插件来实现分页。OK，好，我们就一起来看一下我们预先准备好的一封文档，这个文档就是整合 my Betis page 插件的一些步骤，我们可以先看一下。


首先一个我们要使用 page helper 这个插件，我们就必须要引入一个依赖，所以把这一段代码拷贝一下，贴到我们的项目里面，放到我们聚合工程的 Pom 点叉庙，在这个里面我们可以找到 my Redis 部分，在这里通用 map 和它放在一起。这个时候我们只需要把相应的价包导入就OK。好，导入完毕以后，我们的第二步来看一下。


第二步我们应该要配置一下 YAML 文件，我们来拷贝一下配置。回到项目应该是在这里 application 点 YAML 文件，双击打开，我们可以放到通用 map 配置放到这个地方，在这里我们可以来看一下。在配置 help 插件下方会有两个配置，第一个其实就是我们所使用的数据库，它的一个方言是什么，使用MySQL。另外一个是 support masses，它的一个参数是否支持分页的一些参数的传参，我们在这边设置为 true 就可以了。好，现在基本的配置设置完了以后，我们就可以去使用分页了。如何去使用分页？在这里可以看到，在使用分页插件之后，我们要在查询之前使用分页插件，也会使用到配置 help 点 start 配置，也就是开始执行分页。它是一个静态的方法，它的原理其实是会进行统一的 SQL 拦截，拦截了以后，它会为我们的 SQL 去拼接一些相应的 SQL 片段，为咱们所设置的一个社会语句去提供一个分页的功能。


OK，这一段代码我们可以拷贝一下，贴到咱们的项目，也就是在 service 的部分。在这个部位，我们是在这里去查询我们的一个评论的。所以在这个之前我们就要使用配置 help 把包导入进来。 start page，它会需要我们提供额外的两个参数，一个是配置，另外一个是 page size。 page 就代表你要去查询哪一页。 page size 是指我们要去查询的时候，每一页所显示的记录数，每一页所要展示的条数是多少条。你需要在这边也要去进行设置的。这两个参数很明显，其实都应该是由前端传进来的，所以我们要回到咱们的接口，在接口的后方，在这边我们再去额外的去添加两个参数，一个是 page size。OK，这两个都是 Int 型的，都是整形，所以在这边加上就可以我们换行一下。好，我们要去实现分页对吧？加了两个参数以后，在我们的 service 实现方法里面，我们也应该要去把这两个参数给加进来。好，我们把格式优化一下。


好，OK，现在这两个参数就可以传到我们 service 里面来。它在执行分页的时候， start 配置也是可以成功的去运行。成功的运行了以后，其实我们一会儿会通过在控制台打印 circle 语句，就可以看一下它的一个 circle 是怎样的。


好，拿到了以后，在这个地方其实 list 它已经是分页过后的了。分页过后的我们就应该要去进行一个分页的处理。来看一下分页的处理。在这里来看一下分页的数据是需要封装到一个 page 的 grid results。我们封装进去以后，我们再要去传给前端，因为在 page info 里面，它是包含了一堆的分页数据。比方当前是第几页，我们查询出来的分页数据是哪些，另外总共有多少页我们都要反馈到前端的。好，我们把这一段代码可以拷贝一下，贴到项目的地方。相应的我们把包都是需要去导入进来 page 的 grid result。这是一个对象，是封装的一个类。预先其实我也已经是提供给大家了，在这里在 Com 点 m 可点与 TOS common 子工程，在这里面就包含了这几个数据，这些数据都是要提供给前端的。一个是配置是当前的页数， total 是总页数， Records 是指总的记录数。另外还有是一个rose， rose 每一页所要去展示的内容，它是一个list， list 就对应到我们在这里所查询出来的list。OK，好，我们在这里看一下。


首先一个我们先把 list 放到配置 info 里面，放进去以后它会做一些相应的处理。这个处理比方首先一个我们要去设置一下配置，这个配置是当前第几页，我们要放到 grid 里面，然后再把 list 放进来，这个 list 就是我们分页后的数据。


再一个我们要拿到total，这个 total 是我们的一个总页数，在这里你是需要去注意的。我们 set total 的时候，我们是从 page list 里面去获得一个pages，这个里面我们也是可以去看的。点一下 page info，在里面包含了一些注释，都是由开源的作者所提供的。比方当前页是一个 page number，每页的数量是 page size，当前的页数是size。这些内容和我们在这里面提供给前端的其实是有一些差别的。所以在我们进行代码编写的时候，你是一定要去注意的。比方在这边我们是通过 get the total 传入到 grid 里面的records。在 grid 里面的 total 和我们使用 page info 里面的total，它们的意思是不一样的，在这里一定要去注意。可能会有同学会问为什么两者不统一，其实主要是因为 page in four 设计是由他的作者去设计的。如果我们把 page 的 grid result 统一的和去进行一样的设置了以后，前端它在做一些相应的操作了的时候，可能在参数上会有一定的变动。所以在这里我们其实也是相当于做了一个转换的过程。因为在前端可能会有很多的一些分页的组件，分页的组件它们的一些属性的定义和后端的定义可能都是不一样的。


OK，所以我们这样的一段代码是必须要去做设置的。当我们设置好了以后， grade 我们就直接可以也蹭出去了。OK，所以我们返回的参数这个类型在这边我们是需要去改掉。使用 page 的 create result，在这里也要去修改好。OK，修改好了之后，其实代码就已经是可以正确的去执行了。但是其实在我们的 service 里面，其实不光我们当前 service 会使用到分页，其他的方法可能也会用到。所以这一段代码我们是可以提取出来去共用化的。OK，在这个下方我们写一个 private 方法，返回出去就是一个配置的 grid result 写过来，写一个方法，来一个 set up 配置的grid，好传入参数。参数很明显是把 list 给传进来，把拷贝进来。注意一下，这里面的一个类型，由于需要提供公文化，所以我们不应该去写死它具体是哪一个类，所以我们写一个问号就可以了。再把这一段代码全部都贴到这里面来。设置好了以后直接在这里做一个 return 就可以了。把 grid 给赠出去就 OK 了。在这边会有一个配置，配置没关系，在这里我们可以加一下Int。


型的配置好OK，在调用地方，我们直接就可以使用 set 配置的grid，然后把 list 贴过来，再把一个配置写过来，随后其实我们分页的过程就 OK 了。如果我们在当前的 service 里面，我们还会有额外的分页，我们只需要加上这一句话，加上以后再来做一个 set 就可以了。 grid 我们直接返回到前端，就可以做到一个分页的功能了。


好， service 现在我们是写完了。写完之后我们就应该要去到我们的一个 Ctrl 里面去把 Ctrl 了做一个完善。好，我们来写一下。我们先到 items control 了，拷贝一个方法写一下，把拷贝，把 swag to 它的接口名称改一下，这是查询商品评论。它传过来的时候，它使用的是一个 get 方法，它的一个路由的名称。路由名称我们现在知道吗？不知道没关系，我们的到我们的 item 页面前端，我们直接去查一下就可以了。在生命周期找 create 的找到有一个 render comments，这是用于去渲染商品评价列表的内容。拷贝一下，搜一下，搜到这里再往下搜，这里是根据它的等级去查询的。等级。我们先不管，找到真实的方法，可以看到它的路由是 items 杠comments，所以我们只要把 comments 拷贝贴到我们这里就可以了。


好，都写一下。写好了以后，我们还是需要去传入一些相应的参数的，比方 item ID，你是肯定要去传吧。随后我们再看一下前端，它还传了一个level，因为我们是可以通过等级去做查询的，所以等级我们也要传过来。另外还有一个配置，以及是配置size，这两个值我们都要去写。OK，回到我们的接口，把这一段代码拷贝一下，我们可以拷贝多份，在多份里面去做一个修改。


item ID 第一个是保留不动，第二个是level， level 写到这里，并且它是一个 Int 型的，这是评价等级这些它后面会有一个required。在我们这里面。所有的 required 其实只有第一个，就是商品 ID 是必填的，其他的我们都传为一个 force 就可以了，如果他不传，我们是可以为他去设置内容的。

好，这是一个level。好。下一个应该是配置，也就是当前的一个页数。写详细一点，查询下一页的第几页。好。再来一个是配置size，这是分页的每一页显示的记录数。好，现在我们这些内容都已经是设置好了，都是有 quest time 请求参数。好，在这个下方。第一步我们应该要判断一下 item ID 不为空，这个是一定要判断的 item ID 为空，我们评论肯定是查不到的。好，随后一个我们就要去判断一下咱们的配置了。在这里我们可以判断一下配置，判断它是不是为空。如果为空，默认的，我们就可以为配置直接设置为1，定义为第一页就可以了。所以我们配置是可以不用传，是可传可不传的。OK，在这边他报了一个错，我们定义的不对，页数和记录数其实都是整形。好。随后在下方我们又可以再做一个判断。我们再来判断一下我们的 page size，判断一下我们每页所要去展示的条数是多少，判断是不是为空。如果为空，在这里我们就可以定义为具体的一个数量，比方你可以定义为 10 条，也可以定义为 20 条。在这里我们统一的。其实在前端我们显示的时候，它是显示的数量是有 10 条，你可以写一个10，但是我们为了更加的通用化一点，我们在这边我们可以来继承一个basic。啃出了，看一下 Ctrl 了有没有写，没有写我们可以来一个通用化一些的。我们可以复制一个 hello control 了。


重新定义为 base control 了。一些通用化的参数我们都可以写到这个里面去是可以的。我们把这一段内容全部都去掉。在这里面我们可以来定义一个参数，这个参数我们就可以写上一个 public static final。它是一个整形的数量，比方，我们这是用于提供给评论的，可以定义为 comment page size 定义为 10 条，它也是一个 control 了对吧？在这边 control 了，我们为它直接加一下。


随后我们把可以转换为大写。转换为大写应该是， shift 加u，但是大小写可以切换的好，我们在 Ctrl 里面就可以直接去继承了。以后在这个下方我们的 10 就不用去写死了，直接写好一个comments。 common page size 事实这样子就已经是写好了。


OK，接下来我们是需要去调用一下咱们的 service service。首先一个前面的参数应该是 page 的 grade result，查询出来是一个规则。通过 item service 点 query page 的comments，在这里面把相应的参数一个一个的去放进去。第一个是 item ID，第二个是level，第三个是page，最后一个是 page size。OK，好，这一行太长了，我们做一个换行，这样子大家可以看得更加清晰。OK，总共是 4 个参数。


拿到 grade 以后，直接往里面一丢。前端在接收到 grade 以后，它就可以根据自己的情况去做一个相应的渲染工作了。好，现在我们可以来做一个测试了。 install 一下。好， install 成功以后重启服务器。我们到前端可以来看一下。在前端这里面首先拿到一个grade。拿到 grade 以后，我们在后端定义了一个rose， rose 其实就是它的一个整个list。所以我们可以通过 this 点 common list 做一个赋值，赋给我们当前的配置，也就是 view 里面去设置一下，随后在这一端它会有一个前端年月日，也就是时间的一个格式化。通过 moment 插件是可以去做一个设置，设置好了它是会根据时间去做一个格式化的。当然我们在当前页面里面，只要是设置到分页总页数，还有是 total 这些内容都是需要重新去设置。这个是在页面里面也会涉及到一个分页的插件。前端的分页插件我也可以给大家去介绍一下。


在这里面有一个叫做 c page n a v，这是一个分页的插件，在当前页面里面来搜一下，它会有一个分页的。在这里有一个分页 start 和end。在这里面只要把页数Max，page，另外page，size， total 等等把这些数据传进去，它是会为我们做分页，其实主要就是在下方会有一个分页点击的d、 i v。另外它还会有一个 Zoom page，也就是当我们去点击某一页的时候，它会把当前页数。你要去选择第几页的业主会进行一个传参，可以给大家看一下。在这里只要点击就会拿到一个配置，随后再重新的去把配置去覆盖掉就可以了。比方现在第一页点击第二页，只要把配置重新的再放入到 render comments 里面去传递，到我们后端去的时候，配置就会变为 all 了。这样子请求又会重新的再去进行一个查询，最后再到页面去进行一个渲染。


OK，好，我们回到页面，我们来做一个测试，刷新一下。好，刷新成功。点击全部评价。点一下，现在就可以看到我们现在的一个所有的信息全部都查询出来了。用户的头像和用户明细没有，不用管，因为我们现在用户暂时还没有，所以我们可以先不管。然后点击分页，这是第二页，再来一个第三页，第三页是三条数据，总共是 23 条。点击好评，总共是有 14 条，分为两页。下一页总共是有 4 条。再来一个中评，中评是有 7 条，在当前页是可以显示的。再点一个差评，差评总共是有 2 条。现在我们的一个分页就已经是开发完毕了，OK。

[image](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/9c54c391-0e94-4301-a9d5-d5700507c418/2020-09-17_210433.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SMEZQEJM%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T224646Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCICV%2FMlX2O38%2FNlqwELL6ZWcSeD182FudhpslzkZoSRX2AiEAzqq9dVNvZ7XWPAKQTp%2FyflN99ChiGDxW5iLS%2FLxMZvgqiAQIxv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDD8eVgQC8p8MFJIiTircA1FC500CCbHvsAey3nqyXz9F5G%2BrO16QZ6mVmhlC%2FFqgOE%2Fcz%2BQbzA6f7E%2BkhndSMVHc04JK4LEoy1U7G9cE9QxivwxUvxF%2FyXoRLkKV3N4eBKAUH6%2FO0fi1A0PMHdnpQCDw0GPvzHVeusz4L8KuPdHFQG9wpmkbEcNrAmvu4sRioAepz8HSU0CIlWI6fF8qu190S5AhSXMr%2Fk8hy5tiWTgT6SX0wIfmCfWNoYPLW0UgdRbteSnNWhDoov1Zh76jKS3ITIjLNJG1ZZZ3h1wedWAMnsSdsnLWrSb9LOPVF0YAWVnVoG%2FN0MBgbMPL%2Fq%2Bg4sJvgVVuv669eT7w3egVCrjdgrdmkdy7OHDUNkE8INkWrxVDXfsbaBlSlgoLtMPEMKRknQwVgh698dNR%2BgeTnAaHrJCCbFmJFukOUIy08ExaU%2FQYIYqB4ULza%2B%2BNQ8BfmOvbhpsQh0NANjhmVVCifUngX1Min7PFFrDUp%2Fc0Gt1rwN%2FxsOvvXwv8PjajBuvRzubg%2BmNRnNN0rhtnPATyK6xyHyTXXlOWAQrpDNnGKltJQ%2BjChlAGIxyR1UZQZF0G7Mu6IVlqmpTOxgNofGeeNrCtcUHMZUfGCBYS9Yo6bm%2FbumlVWSpmOUbrdyz0MPy5%2F9IGOqUB2DjMPM7qPx6LmWSC29Hz%2BF%2BAXOEjKVAzehqZWbHZDZ5RZMfA6pNrvhvD8cN8ktwMgT3nhShH3rnqQGexgHB%2BBg6xwNtaT2OFWp9ziLk2To81Yju4h8uhVAuwotSfD9jzxNd2i9Djt6aPbIK%2FaXHffxEy%2BWYJjfPcdxFO95BSNs4T%2BkBPVQgU%2BSWYafO7j2pzEjQ3pwCGQ67jvPNGJ8PiApl8LpUj&X-Amz-Signature=dd45585f064dedca5e5e11fa1a918f40a0554a6f807390655f450dd7c3c03acc&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



