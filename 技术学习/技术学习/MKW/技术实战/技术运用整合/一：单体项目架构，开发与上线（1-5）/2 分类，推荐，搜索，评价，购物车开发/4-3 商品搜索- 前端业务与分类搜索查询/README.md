---
title: 4-3 商品搜索- 前端业务与分类搜索查询
---

# 4-3 商品搜索- 前端业务与分类搜索查询

[image](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/1c577faf-e864-4ad5-8ffa-02df1cfa9333/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TLH5JQTK%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T224649Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIBamMrO94iX3f4bv12NaO3t%2BV1OSkjf%2BeRCohs559%2FScAiEAheRTSDAwUMjVv9ruvgo8rIfvDLlGQidHziwqEP5z4wMqiAQIxv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDEbdPKkE2mstDRxjRircA8a34rCvqZtfBCYa6YZSiUWsAiw6ZPN%2BazT2llCtmjzOn4Ztry%2BIvANw%2FjTUUihqDvgtq5Bethn%2B2NePwZ58tiSffFEYt%2Fe7fi2%2FtD6ovO6xUTqgJsR96iotOoiyTz2HdMtXK0r%2FHCRdtRfXhB%2BPnnMJQvf44TgdtiltrTZloPmGi72%2B%2FOJiIVbdS5%2BiWhfTByB%2BTYAjHQp2G%2FP2erwCPGlq%2F76ps5%2BZmt%2BwAA3IZNfaRQ5KCwcQinCmJPWBEc029VkgAy4XcjdoQ7xoTl7x69z3f0gv%2FOtaz8GUrlqijA%2BVpc34IFOa%2Fwnf2AR2g9NKBAZl5qLu0Pr%2FhRQ%2Bmkd95bJrjvLuiRrd53JT%2F983Rvv5XlHIZD5PRIO6SBLH5fnGoTkg5GhmRgXMXA%2BiHQHjA5WikhcaxOiHzRBZE4dezjKzjOnu5MGIHjS0gRRtOoUwbN1eklzOei0kdgkRR2cWLUilIn%2BKJqmjGMORB6UuLx4wvxUvJU%2FyjuZWLZPYA66p2nmK%2F8eHurnrAVKRm1vM9VlzMGv0YxNFFLU6NZH1UyM1yPO3P4LkBFEZgei02l1wUqcKBLGuC3UjXjUdd2G7Aq6Fw2ZlBO4R2SOXN8J5rFcZlhi8kqUibjKDAMLeMLq5%2F9IGOqUBBW9oF%2F87%2FqkWg4aXU%2FcMgNcgudjiLtyd0udYpH6Qtc2ydOFG%2BGrxp38t6YHBFyyGyRi2AzuhgC5mJpFZc0m5Xg%2BoFgDd9L6pi0Qh3RykNsCZCCKu6burDW548b4YPq0KpJPxRG7KiC9MSXBd%2F6NfroeLmo80M8v0NYps1nUKfNhXhAvSPzQMZiKZ8k33LvhIzMlRU7ECVEDsrIXhXI5zS6oKgzxG&X-Amz-Signature=267b7ec2b09412c6192271369699f9d0616b3124c0ec5d14e358f3e6ee516ac6&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

前面两节我们是实现了搜索商品列表的功能，并且也是和前端联调了，没有问题。接下来这一节我们先来看一下咱们的前端业务，它是怎么走的。还是一样我们是应该要打开 index 首页，我们在这个页面我们可以先查找一下。我们可以查找一个搜索。查找到以后，在这里大概是在 70 行的位置会有一个 form 表单。首先它会有一个文本框，这个文本框就是让用户去输入相应的关键字的，在这边定义了叫做一个keywords。它使用的是一个 v 杠model，它其实是一个数据的双向绑定。只要用户在文本框里面输入一些内容，我们就可以通过 this 点 t words 获得相应的一个内容。这个主要是因为涉及到了 form 下就是一个按钮，这个按钮如果用户点击它就会触发一个 click 事件，这个世界名称叫做 do search。


我们再来查找一下。随后我们就查找到读 search 这样的一个 JS 方法。首先通过 CS 点 QS 就可以拿到文本框里面的内容。当然你是需要去进行一个判空的，因为我们的业务其实也是设置的 Q2 紫为空，我就不让你去搜。下一个应该是做一个页面的跳转，我们是这样子去做的。


首先一个我们是需要把这个 Q2 的内容我们要携带到下一个页面。随后我们会有增加了一个叫做 search type，叫做 search items。什么叫 search type，主要是因为其实在我们的页面里面，不光光是在这里可以通过关键字去进行搜索，其实还有一个搜索功能，在首页其实也有的。在之前我们是做分类的时候，其实是有提到过的，我们把鼠标移上来，在这里其实可以看到很多的一些子分类，其实这些都是一些三级分类。


三级分类当用户去点击的时候，比方我们点击一个蒸蛋糕，点击一下页面发生跳转，它其实是通过它的一个三级分类的分类 ID 去查找当前分类下所有的商品。它所产生的一个搜索结果页和我们之前通过关键字去搜索的一个结果页，其实是同一个页面。在这里面你查询出来的内容，你也可以去做一个分页。另外它也包含了销量的排序，价格的优先排序其实都是可以的。


也就是当前的搜索页，它会有两个入口进来，一个是通过首页或者是其他页面的一个搜索框去搜索，另外一个就是通过它的三级分类，根据分类 ID 去进行搜索，它就会有两个入口，两个入口会对应两个不同的搜索类型。所以在我们的前端页面里面就包含了一个 search type。在这里我们是使用的是 search items，它会带上一个keywords。另外还有一个，我们把 search type 拷贝一下。在当前首页，我们可以往下面去搜索，在这边可以看到它会有一个 cat items，这个其实是在做拼接。三级分类的时候，这是我们的一个懒加载，懒加载是需要鼠标上移，第一次查询出来，它就会拼接一部分的 HTML 内容，这一段内容就是去做查询的。本质上其实也是差不多。它是重新会跳转到一个新的页面。可以看一下它的 target 是下划线 blank search type，它也会带过去。另外带过去的同时它会附带上一个 cat ID。这个 cat ID 其实就是什么三级分类的一个分类ID。好，随后我们就要来看一下我们下一个搜索页。

搜索页是在 cat items，也就是这个页面。我们一起来看一下。首先我们要看的应该是生命周期函数 create 的，来看一下。首先它会拿到相应的一个内容，拿到 search type，这个是从可以通过 APP 点 get u r l pump，获得上一个页面所传递过来的参数。拿到参数了以后，在这里是需要去进行一个判断的。如果你 search type 为空，当前页面我们是没有任何的一个内容展示的，直接就 return else 了。随后如果有值，就需要去进行判断。它会有两个分支，一个是判断是不是根据关键字去搜索，另外一个判断它是不是根据分类去搜索。在这里它是会有一个判断的。如果是根据关键字去进行搜索，肯定我们要去获得keywords。拿到了 keywords 以后，我们就可以去 search in background，可以来看一下。在这里就会调用这个接口。


其实我们刚刚是看过了，这是它的一个路由，我们是把 keywords 在这里进行一个传递，当我们拿到了一个结果值以后，就可以在当前的页面里面去做一个渲染了。当然还包含了一些基本的分页信息。我们在做评价的时候，商品详情页面里面用户评价的一些相应的内容，和分页相关的不去多说了。


好，下一个。下一个是判断它是不是 cat items，这个就是代表它是根据分类去搜索一些商品的结果列表，是需要去获得它的 cat ID。这个是从首页拿过来的，如果它有值，我们就可以去做一个查询了。这是 search cat items in background，我们拷贝一下。搜索在这个位置，在这里他就会发起另外一个新的请求。他请求的路由是 items cat items，他会把 cat ID 给传过去，随后它后面所携带的一些参数和我们在进行查询关键字的时候其实是一样的。只不过它唯一的不同点是一个路由不一样，菜茶机也不一样。


接下来我们所需要去做的，应该要是根据分类的 ID 去进行一个查询。我们可以到前端页面来看一下。在前端页面里面，一个是根据它的三级分类去查询，另外一个是根据搜索的关键字去查询。他们最终的一个结果页其实都是一样，所展示的内容也是一样。他们其实在本质上进行 circle 去查询的时候，也是多表关联查询都是一模一样的。唯一的一个不同点就是关键字和分类。关键字和分类又都在 iTunes 这张表里面。


其实对于后端来讲，这两次不同的查询，我们可以放在同一个 service 里面，或者放在同一个接口里面，是完全没有问题的。但是如果我们放在前端来看它，其实入口是不一样的。一个入口是在搜索框，一个入口是在首页。这样的分类。如果你是作为一个架构师或者一个甲板高级开发人员，你其实应该要想得到。在后续，随着时间的推移，网站的用户量会越来越多，业务也会越来越多。这两个接口如果你放在一起写，他们有可能会造成的一个后果业务越来越复杂，耦合度越来越高。如果在进行一个分类查找的时候，它可能会有一些其他的业务要去做，你可能就必须要把另外一个搜索接口给区分开，耦合度相应的，如果你写在同一个接口，同一个 service 里面，你可能会做一系列的判断。耦合度太高，相应的接口的性能可能会下降。所以这一点是需要在我们前期应该要考虑到的。


就相当于我现在有一棵大树，大树上有一条枝干，枝干上有两片叶子。这两片叶子你是让他们在一条枝干上去慢慢的成长，还是让他们在额外的两个不同的枝干上再去成长的？其实这也是需要去考虑的。如果这两片叶子是单独的，各自去发展，当然他们在后续的耦合度肯定是会下降的。另外，他们独立去成长，他们是相互彼此，没有任何影响的，而且各自也可以成长的越来越快，所以这是一个简单的举例。所以我们在这里在前期要考虑到这样的一个情况，所以我们就会把这两个不同的接口区分开来去做好。


现在我们可以先来把数据层的一个 map 先去写好。其实也是可以把这段代码我们可以拷贝一下，也就是 search items 直接拷贝，拷贝以后贴过来。只不过它的名称我们是需要去进行修改的。在这里我们可以取名为 search items，它是和一个cat，也就是 category 分类是相关的。写一下 by third，它因为是三级分类，第三级的小分类 by third cat，这样子看的就更加的清晰了。


随后参数我们传进来，还是一个 map result type，由于是一模一样的，所以使用 search items 比优也是没有问题。查询是没有问题的，我们是格式稍微的改一下。随后的下方在这个部位它会有一个 keywords 的判断。 t words 我们现在是不需要了。我们现在要去判断，其实是根据它的一个 cat ID，所以把删掉。在后方我们加上一个 and 再来一个 i 点。它会有一个三级的分类的ID。我们来看一下它的数据库。在我们数据库里面所对应的应该是有一个 cats ID。把字段直接拷贝一下，拷贝以后贴到这个部位。 i 点。 cat ID 等于你传进来的ID。井号大括号是map。点来一个 cat ID，这就是传进来的，参数是从前端传过来的。这样子我们的围绕条件其实就 OK 了。下方是一个 order by， order by 我们可以不用管，因为是和我们搜索商品通过关键字搜索是一模一样的，所以我们使用这样的一个片段就 OK 了。好，这就是我们的一个map， map 就已经是开发OK。

