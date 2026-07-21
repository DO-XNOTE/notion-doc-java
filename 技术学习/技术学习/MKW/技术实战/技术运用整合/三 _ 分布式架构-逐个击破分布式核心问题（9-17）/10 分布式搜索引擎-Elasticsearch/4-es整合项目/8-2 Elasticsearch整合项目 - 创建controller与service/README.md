---
title: 8-2 Elasticsearch整合项目 - 创建controller与service
---

# 8-2 Elasticsearch整合项目 - 创建controller与service

[file](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/16ec0d25-18af-4656-90fe-7c0ff85785cf/Alan_Beaulieu%EF%BC%9ALearning_SQL_2005_%28%E7%AC%AC1%E7%89%88%29.chm?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VNEFTWFW%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T225214Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCOiMenwY61o%2F0jetsd4Z65mLS%2BKOYszd142e0WoFXAdAIhANJ6mto80cD453KA87SLcZikL%2BK63G44duTHoIGXYvt9KogECMb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1Igwq5dCfHWG%2BmQz7iyEq3ANcbLiq2aE%2FdDhYmz3jtMRfxd60fRlGOFvrPw5e%2FQ00pJqkH5urOEwg6rVr8Lp4Ek4RsFipcWlGZx5KddqlQZttsv0%2FCQBnxY8cv7gsQYFlf1BP7KAo535bA6%2BjFukDESf2hZhTAwTgDgyOmoByijy3PTwqG7bxwjjhh78hBFd6hCrZ5mQB%2Fn3QO%2B3Fb84OnDQ%2BGO8uk4SqVKl0xC%2B2Ire3JXtuou%2Bp3LvBV0oK%2Fz2sIOO7QwK8bE0BI35K8mG99hdriRUjSf36t30Wqc20pa%2BlEM9RWtyk81gciwlF%2BS9jNYodP30RGH5vQ52yFvPdwyg6ebNl2UOzwmlHzB%2B7L6942DASJrg6c9EQFt5fCXFBd5Jmg7cu1ro9MTb0uMDZ6FeTDAOnizpmxOa%2FiBGI%2BZAhrir%2BcYRR0JeDpbykNOUWBvA83LWH%2BwswcOCa9JBJWwAnzyX%2FnitqRK8d90KE547DptBYSs22Fm88mPqtu%2BbuTlpcKLo4W2pXyKfeFcZFNXc%2Blnnkfuv8BlN97CaifMfQATmNMyIDTUrP21nMgo5A9fpsTsLddjQM2OuE1RmKJjoiWmFlXdrT7yyT0HB0h7oslKLHvHWSdgq7HItNUdg0CuuY9mND5IJGkioarzCNuv%2FSBjqkAYfQOcP4rP0dV34eGBPD%2FTCiO2Ho4Ne%2FA2Hfbej26f%2Bx7MazCQZV8ZsLLvlBXFJoK9r6aW0BSXaBCTn1X%2FDIq9ypMn5OAbd7vYyBgNbwlBKcV6a6d26yBPDEhIda0rcNOBQEnjOGa1s1ezaPaPJIzykvu38fzU%2F7XJugSLLjFXN8pWy4PmrODCPShYQrM94MCrFZsRwq8J9vVXKahyPxo%2BuQgapH&X-Amz-Signature=4146d0bc925e22bb68451f2112f1e82be721232407f50550542a9b13059e29c1&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

[image](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/c1f1834a-51a1-4778-ada5-64d73ae67eda/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VNEFTWFW%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T225214Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCOiMenwY61o%2F0jetsd4Z65mLS%2BKOYszd142e0WoFXAdAIhANJ6mto80cD453KA87SLcZikL%2BK63G44duTHoIGXYvt9KogECMb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1Igwq5dCfHWG%2BmQz7iyEq3ANcbLiq2aE%2FdDhYmz3jtMRfxd60fRlGOFvrPw5e%2FQ00pJqkH5urOEwg6rVr8Lp4Ek4RsFipcWlGZx5KddqlQZttsv0%2FCQBnxY8cv7gsQYFlf1BP7KAo535bA6%2BjFukDESf2hZhTAwTgDgyOmoByijy3PTwqG7bxwjjhh78hBFd6hCrZ5mQB%2Fn3QO%2B3Fb84OnDQ%2BGO8uk4SqVKl0xC%2B2Ire3JXtuou%2Bp3LvBV0oK%2Fz2sIOO7QwK8bE0BI35K8mG99hdriRUjSf36t30Wqc20pa%2BlEM9RWtyk81gciwlF%2BS9jNYodP30RGH5vQ52yFvPdwyg6ebNl2UOzwmlHzB%2B7L6942DASJrg6c9EQFt5fCXFBd5Jmg7cu1ro9MTb0uMDZ6FeTDAOnizpmxOa%2FiBGI%2BZAhrir%2BcYRR0JeDpbykNOUWBvA83LWH%2BwswcOCa9JBJWwAnzyX%2FnitqRK8d90KE547DptBYSs22Fm88mPqtu%2BbuTlpcKLo4W2pXyKfeFcZFNXc%2Blnnkfuv8BlN97CaifMfQATmNMyIDTUrP21nMgo5A9fpsTsLddjQM2OuE1RmKJjoiWmFlXdrT7yyT0HB0h7oslKLHvHWSdgq7HItNUdg0CuuY9mND5IJGkioarzCNuv%2FSBjqkAYfQOcP4rP0dV34eGBPD%2FTCiO2Ho4Ne%2FA2Hfbej26f%2Bx7MazCQZV8ZsLLvlBXFJoK9r6aW0BSXaBCTn1X%2FDIq9ypMn5OAbd7vYyBgNbwlBKcV6a6d26yBPDEhIda0rcNOBQEnjOGa1s1ezaPaPJIzykvu38fzU%2F7XJugSLLjFXN8pWy4PmrODCPShYQrM94MCrFZsRwq8J9vVXKahyPxo%2BuQgapH&X-Amz-Signature=480a6645cb34d023abb44e932c1e04d14f0f073f6369cb20d700218f57923da7&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

[image](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/e7ede093-cab7-42ec-ade5-3e45f27b7394/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VNEFTWFW%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T225214Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCOiMenwY61o%2F0jetsd4Z65mLS%2BKOYszd142e0WoFXAdAIhANJ6mto80cD453KA87SLcZikL%2BK63G44duTHoIGXYvt9KogECMb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1Igwq5dCfHWG%2BmQz7iyEq3ANcbLiq2aE%2FdDhYmz3jtMRfxd60fRlGOFvrPw5e%2FQ00pJqkH5urOEwg6rVr8Lp4Ek4RsFipcWlGZx5KddqlQZttsv0%2FCQBnxY8cv7gsQYFlf1BP7KAo535bA6%2BjFukDESf2hZhTAwTgDgyOmoByijy3PTwqG7bxwjjhh78hBFd6hCrZ5mQB%2Fn3QO%2B3Fb84OnDQ%2BGO8uk4SqVKl0xC%2B2Ire3JXtuou%2Bp3LvBV0oK%2Fz2sIOO7QwK8bE0BI35K8mG99hdriRUjSf36t30Wqc20pa%2BlEM9RWtyk81gciwlF%2BS9jNYodP30RGH5vQ52yFvPdwyg6ebNl2UOzwmlHzB%2B7L6942DASJrg6c9EQFt5fCXFBd5Jmg7cu1ro9MTb0uMDZ6FeTDAOnizpmxOa%2FiBGI%2BZAhrir%2BcYRR0JeDpbykNOUWBvA83LWH%2BwswcOCa9JBJWwAnzyX%2FnitqRK8d90KE547DptBYSs22Fm88mPqtu%2BbuTlpcKLo4W2pXyKfeFcZFNXc%2Blnnkfuv8BlN97CaifMfQATmNMyIDTUrP21nMgo5A9fpsTsLddjQM2OuE1RmKJjoiWmFlXdrT7yyT0HB0h7oslKLHvHWSdgq7HItNUdg0CuuY9mND5IJGkioarzCNuv%2FSBjqkAYfQOcP4rP0dV34eGBPD%2FTCiO2Ho4Ne%2FA2Hfbej26f%2Bx7MazCQZV8ZsLLvlBXFJoK9r6aW0BSXaBCTn1X%2FDIq9ypMn5OAbd7vYyBgNbwlBKcV6a6d26yBPDEhIda0rcNOBQEnjOGa1s1ezaPaPJIzykvu38fzU%2F7XJugSLLjFXN8pWy4PmrODCPShYQrM94MCrFZsRwq8J9vVXKahyPxo%2BuQgapH&X-Amz-Signature=32558c1d55ce274ca1f9d1368a6408238c2145a9cc81df02961068803ba2d651&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

咱们这个 search 它的一个 web 环境，我们目前已经是构建了，构建好以后，那么我们就可以来编写咱们和 ES 相关的一些代码。回到咱们的 idea 首先我们先去构建一下这文档数据的一个结构。在我们当前这个 portal 里面，我们去 new 去创建一个，我们拷贝一下，我们直接把这个 sto 拷贝一下也可以，你要去创建的话也行，把这个改成 items 点击。 OK 好，有了，有了以后，那么我们就直接在这里面去做一些相应的修改就行了。


首先我们的一个 index name 这个东西我们直接拷贝一下，现在会使用这个，福迪 items 杠IK ，就是带上中文分词的贴过来。随后下一个是一个 type 那么这个 type 的话我们之前其实也提过了， ES 区的话是没有这个概念，但是在 ES 区之前的一些版本。那么我们要在使用之前要去先看一下，点击这个索引信息，在这里面它的一个菜本是这个吧是 Doc 要注意一下。所以这个在我们的当前项目里面，你要去把这个改成 Doc 后面的这个我们就不需要了，它还会有相应的一个内容叫做 create index 这个是代表在没有索引的一个情况之下，是否要去创建，我们把它改一下改成 force 就行了。那么这个值的话就是它默认是 true 默认它会帮我们去做一个创建的。


好OK ，这个是我们的 document 相关的一个基本信息。随后对于我们的一些 field 我们也要去做一个相应的设置。那么首先我们先来设置一下咱们的一个文档的 ID 文档的 ID 其实是对应到我们的商品数据的一个 ID 来看一下，其实也就是在我们当前数据浏览用这个也行，直接搜一下，根据这里面的数据来。那么第一个是咱们的 item ID 拷贝一下贴过来，那么它是一个string ，它是一个 string 随后我们去为它加上一个 field 把后面的内容去加一下。它是一个 store 是存储，随后的话我们可以再为它去加上一个 type 这是它的一个。数据类型我们设置为 field field type.text 使用这个文本的一个格式。 OK 随后的话对于我们这个 item ID 的话，它只是本身我们可以为它设置 unx boss ，不需要针对于这个去做一些相应的倒排。索引，的索引直接设置为这个就行了。


最后下一个，下一个的话我们来看一下，下一个是我们的 name item name 在这里拷贝一下贴过来，我们直接把这个复制过来就行了。只不过我们在这里面的有一个 index 这个地方我们设置为 true 那么这个 item name 我们是需要去做一个大牌索引的，因为我们是基于这个商品的名称去做一些相应的全文解锁的。Ok 。


好，然后再下一个，下一个是我们的来搜一下。下一个应该是我们的有个图片的 UL 地址，这个是需要缩小一些，放大的话，它这个是不会显示这个图片，所以我们把这个缩小你就可以去做一个拷贝了，再一次贴过来。那么这个图片也是一个 string 类型，我们把这个拷贝过来。 store two type 是 text 的文本 index force 不需要去做这个相应的大为索引图片，它的一个地址的话，我们是不可能基于它去做检索的。


好，然后再下一个就是涉及到我们的一个价格了，价格是 price 拷贝过来。那么这个在我们的一个 ES 中，它其实是一个 long 的形式去存在的。那么在我们数据库定义的是一个 int 所以我们在这里你可以使用 int 也可以，然后把上面的这个拷贝一下，只不过它的一个类型在这里我们是需要去做一个修改，使用这个和保持一致，都是印着就行了，这个可以删掉。好，然后再下一个的话再下一个应该是我们来看一下。


下一个是我们的 CI cos 就是我们的一个售出的数量，拷贝一下这个也是映射类型。好。OK ，那么这样子其实就是我们日本的一些 feel 的一些属性了，下面的这些我们都不需要了，全部都删掉，再重新的去创建一下，当然也可以再去创建一个 to string 也行。好，OK ，那么这个就是我们的一个文档数据，和咱们目前和目前我们的 ES 中的一个数据是对应的。有了这个文档数据以后的话，我们再来到咱们的 controller ctrl 了我们这样子 ctrl 加 N 我们去搜一下我们之前所写的有一个 items ctrl 了这个是在 API 这个工程的，在这里面我们拷贝一下这个 search 就是我们用于去搜索商品列表的，把这个直接拷贝一下，拷贝之后复制到我们当前这个里面来。


好。OK ，然后我们做一些修改。首先我们的这个有 quest mapping 那么这个我们是需要和咱们之前刚刚的那个 control 了保持一致对吧，刚刚的那个我们把它复制一下是这个什么是 iTunes 这个需要保持一致。然后在这里这边会有一个search ，你可以不动也可以去做一些相应的修改。


在这边我为了区分我可以加一个 ES 但是就是不加也没有关系，因为我们服务起来之后，它的运行的端口是不一样的，所以是没有关系的。在这里我加了一个 yes 好，然后我们再去做一些相应的精简，比方说这个 API 奥博类型，这个我就不加了这些内容我都去做一个相应的金姐。然后像这个其实我也可以不要。好。 OK 那么这样子就行了。总共是四个参数，一个是 QoS 文字，另外是排序的一个 sort 还有是分页的两个，一个是配置和配置 size OK 吧。好，然后在这里面来看一下。
在这边有一个判断，这个我们保持不动，在这里它会有一个配置默认是1。然后在这里还会有一个配置 size 这里我就直接写死为20。另外在这个配置我们要去注意一下。所以说在我们执行分页的时候，其实 ES 它是从 0 开始的，所以在这边我们要去做一个设置配置，在这个地方我们直接剪剪，让它没剪映好。随后我们再往下这边就是开始我们的一个搜索是吧。


搜索的话我们是需要有一个 service 在这边我们去创建一个service ，创建一下创建一个 package service 好 OK 我们在这里面去创建一个 service 这个 class items ES service OK 创建了在这里面。那么它其实应该是一个接口，interface给它去加上一个方法，public它返回的一个数据是 page 的 great result 使用这个，然后方法名方法名 search items 我们直接使用这个就可以了，把这个拷贝过来。好，然后在这里面我们还要去加上一些相应的参数类型。


好，那么我们这个接口就已经是好了，随后我们再去创建一个实现，再去创建一个 package IM PL 好再去创建一个class。
首先不要忘记加上 service 然后在这里面我要去实现咱们的这个接口。好。 OK 然后我们再把一些方法要去实现，也就是 search itemsok 那么这样子的话我们只需要在这个里面去丰富一下咱们的一些方法就可以了。那么在这里面我们还是需要去把这个 item service 给住进来。


好，OK那么这样子我们基本的一个价值就可以了。主要的话其实要注意一点，一个是配置这边是要加加，因为我们的一个数据它的分页是从 0 开始的，我们是要去雷景音。然后我们的这个部分其实没有什么改变，主要是我们的 service 发生了一个变化，这个 service 的话我们是重新又去创建了一个新的 service 我们后续下面一节我们就可以把这里面在这里面把咱们的一个 ES 的搜索再去做一个完善。

