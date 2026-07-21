---
title: 1-5 分类实现 - 自定义mapper实现懒加载子分类展示
---

# 1-5 分类实现 - 自定义mapper实现懒加载子分类展示

[image](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/1271cdf8-4ce5-4308-8c5e-a799052952e1/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46623EKT66I%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T224639Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIGEunowe5h927W3N%2Bg7W0lIWrUwuAuclNlp4Xrm0HwvcAiBut1znoR0%2BulmP1Ku3pTna9x8Xb0qJt3Fug%2FqnEp2EeiqIBAjG%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMgWR3B4fEy4Wti5E1KtwDAN0iVbZ3O2qWe0VgRLzd0z8%2FuzB0yFFAokNtP9sp7yUP2gcFZCkoiAOCaCABpkfhPnWEvs8w3jJ%2FEqfMNF8wvYthOywGxZ9PNiDdz5hFjrlLP5UfhBzJEE67qw7ARLGzBK61P6n846BQGPzRri7AhcF9jc5XMIBInBEuo4ZT9myLRTuQIsS7OxWEpPxN76FMnn%2B6aHs%2FYtHCBF%2BQF6GfBQsL7uLG%2Fz1RLWWVMfYKqKlOwT0ePxskKSO3ugVpXq5yuNVaLE5oZsk1pvpvU2a3C5OD5Ql8dbahOsFMEguJW%2B1XMcRgvaLYgjXpxewA39yA2oLDFS1AtOsHMjaAXMaldwoAa1J64gOpAWp4%2FArIIMeeKKmFq2w9j%2FbVvYNAEGLSGPmOQm2NIfUAGFhjtUm4LXM%2FqKqjSr%2BMZbHxXfO4z5UWnWdDdncLHv2ZDL6moRuerHkqZGT%2B0dslnHSHcLmm%2Fe4CLV2S8DVyDcXB7H8rz%2BnYfIpmXzh%2Brb76IZzUrMeAyud64XaH%2F0QNgnc%2BFl5qKI4akYUHuGm8tJb9R8i4EI5h2AN7t7Z%2FUVf0CIGMhBMRUW%2F%2BmcHMVhIL%2FunvSUNeb33tON6s8jAkQs2tUxcAtJzNIO427nnV9Xm5GUww2rr%2F0gY6pgFGMUNMRvfC%2B37IYMdMjRhCFcDlUK9D0h7Eh3dqpLHLRvAtDEGRo3RladYJSYYSt5zCv4LomhMibfRYqlS3pbEN32u6AN4%2BEzEMrkQAb0B3i%2FWWUF6iBIPCYjDqQPd%2FmR6%2BKsR5WVyWqVGQ6DWaUsqmO6rpIJGeqyRqhzUXDWz5voEhe2xhqWB0RfEMaWJ0nCWrZ7KMIeXYTJI6etSfziFuuv3MWpLg&X-Amz-Signature=3c07dc75455475e3b19779182da33e67aa0f9ed0da6715225eb4e23dfde5641d&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

[image](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/08382c2f-e417-4c28-8313-214496669a18/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46623EKT66I%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T224639Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIGEunowe5h927W3N%2Bg7W0lIWrUwuAuclNlp4Xrm0HwvcAiBut1znoR0%2BulmP1Ku3pTna9x8Xb0qJt3Fug%2FqnEp2EeiqIBAjG%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMgWR3B4fEy4Wti5E1KtwDAN0iVbZ3O2qWe0VgRLzd0z8%2FuzB0yFFAokNtP9sp7yUP2gcFZCkoiAOCaCABpkfhPnWEvs8w3jJ%2FEqfMNF8wvYthOywGxZ9PNiDdz5hFjrlLP5UfhBzJEE67qw7ARLGzBK61P6n846BQGPzRri7AhcF9jc5XMIBInBEuo4ZT9myLRTuQIsS7OxWEpPxN76FMnn%2B6aHs%2FYtHCBF%2BQF6GfBQsL7uLG%2Fz1RLWWVMfYKqKlOwT0ePxskKSO3ugVpXq5yuNVaLE5oZsk1pvpvU2a3C5OD5Ql8dbahOsFMEguJW%2B1XMcRgvaLYgjXpxewA39yA2oLDFS1AtOsHMjaAXMaldwoAa1J64gOpAWp4%2FArIIMeeKKmFq2w9j%2FbVvYNAEGLSGPmOQm2NIfUAGFhjtUm4LXM%2FqKqjSr%2BMZbHxXfO4z5UWnWdDdncLHv2ZDL6moRuerHkqZGT%2B0dslnHSHcLmm%2Fe4CLV2S8DVyDcXB7H8rz%2BnYfIpmXzh%2Brb76IZzUrMeAyud64XaH%2F0QNgnc%2BFl5qKI4akYUHuGm8tJb9R8i4EI5h2AN7t7Z%2FUVf0CIGMhBMRUW%2F%2BmcHMVhIL%2FunvSUNeb33tON6s8jAkQs2tUxcAtJzNIO427nnV9Xm5GUww2rr%2F0gY6pgFGMUNMRvfC%2B37IYMdMjRhCFcDlUK9D0h7Eh3dqpLHLRvAtDEGRo3RladYJSYYSt5zCv4LomhMibfRYqlS3pbEN32u6AN4%2BEzEMrkQAb0B3i%2FWWUF6iBIPCYjDqQPd%2FmR6%2BKsR5WVyWqVGQ6DWaUsqmO6rpIJGeqyRqhzUXDWz5voEhe2xhqWB0RfEMaWJ0nCWrZ7KMIeXYTJI6etSfziFuuv3MWpLg&X-Amz-Signature=11bc1ae7c258e2195977d176d9fd5c48f351ba5603596bd61e9197b176865ef8&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

现在我们已经是通过自定义的一个 SQL 语句，把相应的子分类数据全部都进行了一个查询，都可以查询出来。接下来我们如何把相应的内容我们放到代码里面去进行实现，我们可以来看一下。在代码里面，其实我们目前其实都是使用的是通用map，通用 map 它会有一个相对应的map，比方 category map，这是一个通用map。我们可不可以去自定义？我们自定义就可以去编写一些自定义的 SQL 语句了，这样子就可以实现我们自定义的一些语句的编写，这也是非常灵活的。好，我们就可以来一起写一下。


首先，既然我们要去自定义对应的 map 和相对应的叉mail，预设我们要写两份，我们可以先来看一下。我们先来找到当前的这样的一个map，这个 map 文件其实就是我们所需要去自定义的。OK，这个是我们现在对于我们来讲其实是我们生成的。我们可以这样子，我们可以把额外的拷贝一份，拷贝一份以后在后方加上一个后缀，叫做custom， custom 就代表是自定义，这样子就代表它是一个自定义的分类map。点击OK，好，双击一下。


在这个类里面，后方会有一个 extend my map。这个是通用map，现在我们还需要用吗？我们是不需要用了，我们把它给删掉。好，删掉了以后，我们可以来写一个方法，这个方法就是需要和相对应的 Map 叉 mail 文件里面的查询语句所对应的 ID 需要去一致的，我们可以先把它给写好，先写一下，写一个 public list，然后把引入进来写一个名字，比方叫做 get sub cat list。我们要传入相应的一个值，这个值是一个integer，它是一个一级分类的ID。 root cat ID。好，假设这是我们所要去实现的一个方法。这个方法我们现在还要去再构建一个对应的 Map 叉 mail 自定义的文件，找到 category map 点叉妙，我们也是需要去把它进行一个复制，拷贝一下，定义为custom。


好，有了以后我们展开展开。这是我们之前所用到的内容，在我们这里我们还需要去用吗？我们是用不着了，所以我们直接把它给删掉，因为这个是为通用 map 所服务的，我们直接把它给删掉就行了。需要注意，它会有一个 name space，这里你一定要去写的 name space，我们使的是custom，一定要改过来。好。随后在这里面我们就可以去写相应的方法了。


这个方法很明显，写一个 select 有一个ID，这个 ID 就是我们刚刚在这里所定义的 get subcat list。把它拷贝过来，贴到这里。OK，贴过来以后，我们先把 select 结尾标签先写好。好，在这个里面就是我们自定义的 SQL 语句了。我们把数据库打开，把这一段内容全部都拷贝一下，贴到这个部位，贴进来。好，贴进来了以后来看一下。我们先说个题外话。所以当我们把 SQL 语句拷贝进来以后，这一片内容会呈现黄色。


黄色其实就是我们的格式并不是很好看。但是这样的一个格式是我们自己公司现在正在使用的一个规范。因为这样子去写，它的一个可读性会非常的高。如果把所有的语句全部都写在同一行，再进行一行换行，其实它的可读性会比较差。这种规范一个是自己看，一个也是给别人看。


别人当然是相应的一些开发工程师，你的下属还有一个相应的d、b、a，这样子去做，也非常有利于后续d、b、 a 在做优化的时候的一个可读性，这一点是非常有必要去注意的。OK，好，我们在这里它会有一个ID，这个 ID 我们是要通过在外部传入进来的。在外部我们在这里定义的是一个叫做 root cat ID，所以我们在这里要去定一下，写上这个就是代表一个占位符，把 root cat ID 给写进来就可以了。只不过在这个地方 select 标签里面，我们是需要去加上一个叫做 parameter type，也就是你所传进来参数的一个类型。


你的参数类型是什么？我们参数类型使用的是 Int 是吧？其实就是Int，在这里写上一个 INS 就可以了。好，随后在这里面我们所查询出来的时候，其实我们在之前就已经是看到了。在这里面其实前半部分的它的一个 father 的，也就是二级分类的内容，其实这边的内容非常的冗余对吧？对于我们来讲，我们只需要用两条记录，一个是蛋糕，一个是点心。只需要有两条记录就可以了。


后面的内容其实我们可以把它们分别作为两个 list 包给这两个，一个是蛋糕，一个是点心对吧？其实是我们可以通过一个 polo 再去包含一个 list 这种数据格式，把它们封装到一起，我们可以通过这种方式去写。当然买 Betis 也提供了这样的功能，我们是可以去实现的。


好，我们可以来一起先写一下。我们可以先把它的一个 VO 先写好。我们先来写一下。我们先写 FO 什么是FO？我们一会来说。我们先把 POJO 工程全部都展开，目前在我们项目里面用到了 POJO 和Bo。 Bo 是属于和业务打交道的一些实体类。现在我们是从数据层查询出来的内容吗？我们先创建一个包， new 一个package，取个名字叫做VO。好，现在就已经是有了。在 VO 里面，其实 VO 和 VO 可以是类似， VO 相当于是业务型的，它是从前端业务层封装过后的一些数据传入到我们的后端，它是发送一个请求过来的。如果是从我们内部要传取，内部传出去，其实就相当于需要传给前端，前端可以是手机端，可以是 H5 前端都可以。


拿到了相应的数据之后去进行一个展示，它是展示在显示层的，显示层又称之为是表现层，其实就是一个feel，写一下就这个feel，就是这个feel，所以我们就可以把它作为一个feel。就是代表 feel 的feel，就是这个feel。显示层。OK，好，我们在这边我们可以去创建一个相对应的类，这个类就是我们所使用的第一个 do 类。创建一个plus，出名字叫做 category VO。其实这个就是二级分类的 VO 了。我们在这个上面我们加一个注释。二级分类VO。只要是 VO 专门用于去进行展示的，是显示层的一部分。


的数据结构。好在这里面怎么去写我们的 circle 又是怎样的circle。在这一块内容我们全部都拿过来，我们先把没必要的一些 service 先关掉。 catch me。好，我先把这一段先拷贝贴到我们的 CEO 里面来。首先第一个我们是要把 ID 要拿过来，这个 ID 不是stream，我们在数据库里面定义的时候来看一下数据库里面，因为它没有所谓的一个分库分表。我们分库分表不可能会针对于这种分类去做的，因为分类使用运行就可以了，它不可能会有很多的分类，所以在后续分库分表，像这种分类表不太会纳入后续的一个分库分表里面去考虑的。所以在这个地方我们直接把它定义为一个英语者就可以了。 private intake i d 这就是它的一个二级分类的ID。


最后是name，一下好，下一个是type，再下一个是 father ID。好，这些都没用了，这是一个integer。好。其实我们在之前的 SQL 工具里面也说了，我们可以把后面三级分类作为一个list，封装到前边的二级分类里面去。所以我们就可以在当前的 VEO 类里面，我们再去定一个 list 来定一下。比方这个类我们可以取个名字，叫做 sub category CEO，对吧？这个类我们还没有进三级分类的一个list，我们简短一些叫做 sub cat list。好，加个注释。

三级分类 CEO list 好，这个类我们还没有去创建一下，到这里面 new 一个class，直接贴过来。好，OK，好，在这里面把相应的属性给加上去，这个属性其实就是对应到我们的 SUB 那些属性，我们直接把里面的内容拷贝过来，贴到这里，其实和这个是一样的。我们这样子我们只要把这里面的 ID name 都修改掉就可以了，这样子也比较方便，比较快。


好，OK。这个就是它三级分类所需要查询出来的一些内容，我们是需要去生成 get 和set，我们可以来一个get， set 好全部生成了以后，对于我们的二级分类的VO，我们也要去生成。快速通过快捷键可以去生成x。set。好。OK，全部都有了以后，现在我们就可以去处理一下我们的自定义 map 文件了。好，现在我们可以一起来看一下。


在这个里面，我们在这边其实每一个 select 标签，它查询出来的内容都需要去对应一个相应的实体，或者是相应的一个map，它其实是什么？它会有一个 result map，对吧？会，或者是一个 result type，它需要你去进行对应的。在这里我们所需要去使用的是一个 result map，这个 map 是做映射的，映射到哪里？我们可以来写一下这个map，其实在这个上方，如果是通用map，里面会有一个base，给大家看一下。


每一个通用 map 里面会有一个 result map，会有一个base， result map。这个 result map 就是我们现在所需要去使用的，它会映射到某一个具体的 pod 对吧？我们现在把它映射到某一个具体的 VO 是没有问题的。所以我们在这个上方也可以这样子去写一下。我们在这里写一个 result map。 result map 和是要对应的，这里面填什么it。比方来一个 my category category c o 这个 ID 在这个地方你需要去使用的，所以匹配过来。在这边会有一个type。这个 type 有什么？这个 type 代表我们当前 map 所要去映射对应的那一个类是什么？这个类就是 category VO。所以我们只要把 VO 拷贝过来。又见 copy reference，把它直接给拿过来。OK？ copy reference 其实就是它的当前这个类，它所在的一个完全限定的路径。加上类名直接贴过来。好，来一个结尾，把结尾标签给加上。在这里面我们就需要去做一些相应的基本映射了。基本映们也可以参考。之前的我们也是参考一下。通用 map 双击打开一下，在通用的 map 里面可以看到第一行是ID，就是它的一个组件。随后下方所有的类全部都是一个的results。在我们这里也可以这样子去使用。我们把拷贝一下，拷贝到我们自己这里来再去定义。


第一个是 ID column， column 和 property 属性是一一对应，全部都是ID。一个是对应到我们的circle，一个是对应到我们这里面的实体类。现在其实对于我们来讲，所有属性我们全部都做好了统一。打个比方，发则 ID 我们是驼峰式命名，在这里面我们要去使用的时候， column 也是会使用 father ID。当然 property 由于我们的 VEO 里面也是这样子去定义的，所以两边统一都可以使用发者 ID 的。OK，这一点是需要去注意的。


好。这里面首先第一个是 column ID， property ID 后面有一个j、d、b、 c type 这个类型是可加可不加的。在这里我们就去掉多余看了，其实内容会比较多。第二行也就是 column 所对应的就是一个name，和里面的 category 是对应的。然后是 type 和 father ID，我们一个一个的去修改， type 是一样的。下一个就是 father ID，拷贝一行，把发子 ID 贴过来。OK，这样子就是我们第一个 category VO，它所对应的基本字段的映射全部都 OK 的。接下来在 CEO 里面，它还会有一个list，这个 list 我们该如何去映射？我们来看一下。其实在 result map 里面，它还会有一个标签，这个标签是什么？尖括号，你会发现它会有一个自动提示，其中就包含了一个叫做collection。 collection 是一个集合的意思。双击一下好来看一下。


首先你是需要去定义一个property，它的名称，这个 property 名称是什么？它是对应到了 FIO 类里面的属性，这个属性也就是我们三级分类的属性。它叫做 sub cat list，你需要拿过来贴到这里。OK，这就是你为它所负的一个属性的值，它会做好映射的，你必须要这么写好。下一个。它。还会有一个叫做 of type。 of type 是什么意思？就是指我们当前的 subcat list，它对应的一个什么？它的 FO 类型是什么？其实这个东西把它的一个完全限定路径和它的类名称拷贝一下就可以了。在这里右键 copy reference。


好，我们贴过来，贴到这个部位。OK，这样子 of type 就好了。最后我们监控号结尾。在这里面我们就只需要和上方一样，把相应的这些内容给贴过来就行了。好， column 和 property 我们是需要去做一一的对应的。写一下 sub ID，下一个是 sub name SUBTYPE，最后一个是 sub father ID。OK，这个 collection 我们就已经是定义好了，现在我们自定义的一个 result map，其实就可以为它提供相应的服务了。在这边我们加一个注释，我们来把 collection 写一下。


collection 标签。第一个是property， property 是干嘛的？对应三级分类的 list 属性名 of type，对应集合的类型，其实也就是三级分类的do。这个 collection 我们也加一下，用于定义关联的 list 集合，它是一个类型的封装规则。好，OK，这样子其实我们现在就可以去运行一下对不对了。现在我们有了一个 map 以后，我们是需要去有 service 去调用的。所以咱们把 service 打开category。 service 先要定义它的一个接口中的抽象方法，写一下。 public list，在它所对应的范型就应该是 category VO 了。 category VO get sub cat list 你是需要去传值的，这个值其实在自定义的类里面锁定的 root cats ID，把它拿过来是需要去传进来的。这个是由用户请求传入的。写一下，这是根据一级分类 ID 查询子分类信息。


好，OK，随后我们要去实现一下，快速导入。在这里面去加一下。我们发现漏掉了对吧？我们的一些 transcation 全部都漏掉了，我们一会加一下。我们先加一下。这个是事物是比较重要的对吧？我们现在好像很多地方都漏掉了，但是没有关系，我们可以去加一下。由于全部都是查询，所以我们使用 suppose 就可以了。好，要加一下，也要去加一下。OK，这个是需要去注意的。在我们之前的 user 里面检查一下， user 全部都有。好，OK，继续。现在我们就要去调用自定义 map 了。自定义 map 我们现在在这里有吗？并没有。所以你需要在它的头部。在这里你是需要把自定义 map 给引入进来的。custom。好，OK。引入进来以后，随后我们就要去进行一个调用了。调用其实你使用起来和他自己本身的一个通用 map 用起来是差不多的。非常简单。怎么做？我们可以在这里使用。


custom，这个是 category Mapper custom 点 get sub catalyst，把直接传进去。传进去以后，它就会得到一个list。这个 list 在这里我们还没有定义它的类型，你要把 category VO 给写进来。好。OK，写进来以后相应的类型和我们要传出去的类型一模一样，所以我们在这里直接 return 一行代码解决就 OK 了。好，回到咱们的 Ctrl 了，现在我们就需要在 Ctrl 了，里面要去实现一下我们鼠标动到上方所要去实现的一个功能。把拷贝一下。 step two 写一下获取商品子分类，不要写了获取商品。此分类。 HTTP method 也是可以使用 DS 形式也可以。在前方我们要定义为 sub cat 斜杠。来看一下我们在前端源码里面它是怎么定义的。它发起查询的时候是一个 index subcat，它是传入了一个路径参数，路径参数在我们后端如何去定义？在这里我们是需要去使用一个占位符，一个大括号，在其中会定义我们的路径参数的名称，比方定义为 root cat ID。好，定义好了以后，我们在这边我们先把给改一下，改成subcat。


路径参数。我们在参数位置，我们是需要去给它给加上的。它是什么？它有一个注解叫做 at pass。 pass 什么？需要注意？它不是 pass Tom，它是一个 pass variable 是这个东西。OK，好，双击一下，随后在后方来一个integer，把直接拷贝进来就可以了。它这两边的参数是对应一致的，这样子就可以了，它是可以接收到的。OK，由于我们使用了 swag two，我们可以在上方针对参数做一个解释，这个解释我们之前应该没有写过，我们在直接可以去写一下艾特API，它有一个胖，这就是 API 的参数对吧？这个参数我们是可以去定义的，你们可以进去看一下。


点进去看一下源码，其中有一个name，这个 name 是什么？是参数的名称。 separate name，我们是可以去写的。后方还会有一个value，这个 value 并不是值的意思，它是一个description，它是针对于参数所做的一个行为做的解释。OK，所以我们在这里直接去写一下name。 name 把 root cat ID 给写过来，后面去加上一个value。 t l 写一下一级分类。 ID 写了之后其实不是给我们自己看的，我们是提供给对接人员，也就是给前端人员去看的这个参数。它还有一个属性叫做request，我们在这里直接设置为true，它默认应该是force，看到它默认是force。我们是必须要填的，你不填我们就不能够让你去做查询。OK，好，在这里我们就可以发起一个 service 的调用。但是我们不能够仅仅依托 strike two 做的一个必填校验。在这里我们是必须要加上一个if。我们也必须要来自己的去判断一下。我们要判断是不是为空，如果为空，我们是不会让你去做任何的查询的。直接 return 一个 imock result，点 error message。


其实你可以显示一个空字符串，因为我们一般来说只要是从前端发过来请求，基本上都是会携带ID，如果发现没有ID，很有可能是有一些恶意的用户会伪装一些请求来发送，可能是爬虫，也有可能是其他的一些恶意的攻击。有这种可能。所以你在这里可以直接返回一个空字符串就可以了。


当然你要显示的更加的全面，直接可以写一个分类。不存在我们自己公司之前发送过被攻击的事件。有一个接口被攻击了，因为可能是受到国外的一些黑客攻击。对应的开发人员在这边是写了一堆英文的，一些不太好听，我们茶余饭后聊的好。在这里我们就要定一个list，这个 list 就应该是一个 category VO，在直接使用 list 短语 category service 点 get sub cat。 list 在这里把 root cat 给丢进去做一个查询，OK，查询出来之后 list 直接给抛出去就行了。好，现在我们就可以来测试一下我们当前这个方法 o 不 OK 了。


首先第一步还是一样，我们是需要去 install 安装一下，因为我们涉及到了 photo 层工程，也涉及到了service，你安装好了之后，你的车子才能够重新的去上路对吧？一个道理好，重启服务器，好运行。成功之后我们还是一样。我们先来看一下 swag two 在这里面现在多了一个获取商品的子分类在这里面。比方我们现在一级分类的ID，我们就写一个 1 点击发送，此时此刻你会发现我们查询出来数据有了，它是一个 JSON list。我们先把这里有一个井号先去掉。你会发现现在我们所查询出来的内容是二级分类的一个list，一个是蛋糕，一个是点心。 sub cat list 里面是有值的。放大一下，我们点击加号再展开，你会发现相应的三级分类的内容全部都包含在 sub cat list 里面了。


OK，每一个数据里面都是一个对象，被对象所封装的。当然在典型里面也可以展开OK，都是有值的。好，现在我们就可以来测试一下我们的前端和后端的一个对接了。在这里我们直接来刷新一下。好，现在是刷新成功，我把鼠标慢慢的移过来，可以看到我们的值在这边已经是展示了，我们当然一个往下面滑，我们就可以看到每一个大分类都对应了一个小分类，相应的全部都进行了一个展示。


OK，这种方式也就是我们所推荐的一种软加载方式，不仅是在这里使用，我们在下方后面还会加载一些其他的list，我们也是使用类似的方式去加载的。这种方式是我们在开发前端的时候所需要去使用的。当然可能对于我们后端人员来讲，不用去过多的去在意前端，但是前端要去这么做，我们就必须要提供相应的一个支持，你是需要去提供相应的接口给他们去调用的。现在我们就已经是实现了前后端的联调分类也是一个懒加载的一种模式。OK。



