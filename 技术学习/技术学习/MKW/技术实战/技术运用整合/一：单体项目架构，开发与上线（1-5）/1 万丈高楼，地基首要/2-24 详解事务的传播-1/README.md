---
title: 2-24 详解事务的传播-1
---

# 2-24 详解事务的传播-1

[image](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/142bfcf7-1fa1-4e8f-96ca-81f1f4e50fe4/SCR-20240816-qndw.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TOEDPRRI%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T224616Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCO%2FnMNCZ0Xyb8WWkGab90fbbVAyDdRapjf2OMQYj%2FFLQIhANsIo2YYxVhKXGGb1gNE%2FPQthhK9awN5VNviNHafHYiBKogECMb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgwMTvLoYAt7LgxXwNsq3ANoKcYPmMyBOBwuuptKU1TQVRlQBRaqXYb44RKhoVw8xHGA8ZjDCJW59FTxEp0sSNRZi%2FN39LEkTBpPzDCaTcRLfq1wLIaKDfi47gubT%2B2SfBPaKu9n8c0R3lw9BJ2Jvk4uproND%2BVdjaIyarfRoRsa4nJ1IXisyV5nRTzzurprijouHGzWK%2FFses5JUS2ho0x3E3UsW9HQmgrXqtSbit%2F7tU%2FOYXQMguDaR%2Fh%2F1FkY9XQ%2Fbnh8No%2F3HtYaIYzZ6jpQE7quNC1WNG2BRnbnapcO3mvTWuYsZGXjRjgfF1lpzu5S%2BCMgfUg5f41rF%2BPkhho4qhqGjEOfQkRQ9PLEHUbsM3lADfcmCZcQd9wua%2FKUn241LlwoM0SfOT4NV4mZiYoxFFlFZvSXOwLTu97%2B5dwdhT16C5PGh%2Fi3NT2OfXEeQwubcPR%2FWF8jJPtsYvV8x2g%2Bx%2BvyoctLhlxDSVm%2FGXNf7W%2FtjE0f1Pwzx%2FNFs5ujI2fpi3Q08NLdjRMA7J1ENtTWdnSZm64S1Enxa%2B1vhnSAy0NGziJ0xBSiGKElAzYkzlj8ermF9dXXr4TuQFpwIDzxPCLgMNAevMAsv1Pau2D7w%2BeGUVoD16aE%2BSKfkCL5GqkQm5BC9obLRjfxyzDCt%2F%2FSBjqkAR51FuQh%2BlIxNz2ogcjU%2BY9So6t98xYIxFy0yJ%2BzwD8%2BkLG19QgwiZFOlMxie4BC2XaIdlvNB6IQaWawkXPUMQwPN0JNgDVdyxh00V211FUYrzBP%2BKTEfOv%2FbLBJS%2BveDWod2Mk%2FMC7XV5f4SpdDsxQwdstDRFxhbl2oPu2owfobVrF2%2B9IvYpy4MhhUc9ARlN0tzc0HeLCjCIe3k5j%2BcCMRucUv&X-Amz-Signature=384967c7637448ba7f7beb1fd2ee43b1347b87e81028c1cc3d51a8be57d7f40d&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

[image](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/e7d07db6-c09d-4a9d-9a9c-40d902e5b682/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TOEDPRRI%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T224616Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCO%2FnMNCZ0Xyb8WWkGab90fbbVAyDdRapjf2OMQYj%2FFLQIhANsIo2YYxVhKXGGb1gNE%2FPQthhK9awN5VNviNHafHYiBKogECMb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgwMTvLoYAt7LgxXwNsq3ANoKcYPmMyBOBwuuptKU1TQVRlQBRaqXYb44RKhoVw8xHGA8ZjDCJW59FTxEp0sSNRZi%2FN39LEkTBpPzDCaTcRLfq1wLIaKDfi47gubT%2B2SfBPaKu9n8c0R3lw9BJ2Jvk4uproND%2BVdjaIyarfRoRsa4nJ1IXisyV5nRTzzurprijouHGzWK%2FFses5JUS2ho0x3E3UsW9HQmgrXqtSbit%2F7tU%2FOYXQMguDaR%2Fh%2F1FkY9XQ%2Fbnh8No%2F3HtYaIYzZ6jpQE7quNC1WNG2BRnbnapcO3mvTWuYsZGXjRjgfF1lpzu5S%2BCMgfUg5f41rF%2BPkhho4qhqGjEOfQkRQ9PLEHUbsM3lADfcmCZcQd9wua%2FKUn241LlwoM0SfOT4NV4mZiYoxFFlFZvSXOwLTu97%2B5dwdhT16C5PGh%2Fi3NT2OfXEeQwubcPR%2FWF8jJPtsYvV8x2g%2Bx%2BvyoctLhlxDSVm%2FGXNf7W%2FtjE0f1Pwzx%2FNFs5ujI2fpi3Q08NLdjRMA7J1ENtTWdnSZm64S1Enxa%2B1vhnSAy0NGziJ0xBSiGKElAzYkzlj8ermF9dXXr4TuQFpwIDzxPCLgMNAevMAsv1Pau2D7w%2BeGUVoD16aE%2BSKfkCL5GqkQm5BC9obLRjfxyzDCt%2F%2FSBjqkAR51FuQh%2BlIxNz2ogcjU%2BY9So6t98xYIxFy0yJ%2BzwD8%2BkLG19QgwiZFOlMxie4BC2XaIdlvNB6IQaWawkXPUMQwPN0JNgDVdyxh00V211FUYrzBP%2BKTEfOv%2FbLBJS%2BveDWod2Mk%2FMC7XV5f4SpdDsxQwdstDRFxhbl2oPu2owfobVrF2%2B9IvYpy4MhhUc9ARlN0tzc0HeLCjCIe3k5j%2BcCMRucUv&X-Amz-Signature=178fc11518fe8cb6ceb81ca7259b1295574d8ad1a7cb14f752dfa57f117a45ac&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

在前面的几小节课时里面，我们已经是实现了和数据层的交互，其实只要是和数据层，数据库打交道，肯定我们会涉及到的一点就是事物。其实我们已经是使用到了事物注解这一节，我们一起来看一下事物的传播。因为当你去面试的时候，有时候面试官其实也会问你，在 spring 里面事物的传播有哪几种，分别是怎样的，这些可能都会涉及到。


首先我们先来看一下这个事物，我们可以点进去看一下它的一个源码，在它的源码里面，它首先是一个接口，既然是接口，来看一下它，在这里面其实可以看得出来，当我们直接去使用一个 transcational 这样的一个注解的时候，它其实是会有一个默认的值的。后面你是可以不用去写。默认是什么？默认是一个propagation。


点required。 required 其实是指我们当前的事物，你是一定要去使用一个shift。如果当前的事物没有，不存在，会自己新创建一个新的事物。如果当前的事物或者当前的一个方法，它本身是存在，有事物，它就不需要去额外的去创建一个新的事物，它会加入到现有的事物里面去。OK，好，我们可以来看一下我们的一些演示的例子。


这是我们第一个类型，看一下propagation，这个其实是一个枚举，在当前的枚举类里面其实有很多的一些内容，其实总共是涉及到有七个。 Ctrl 加 F12 是可以把这些当前类里面的一些方法内容都可以这样的一个列表的形式可以展现出来，可以让我们进行快速的浏览。其实可以看得出来，在这里面总共是有1234567，我们都会来进行一个讲解。


第一个也就是required，它是一个默认的。在这个里面，每一个方法它的上方都会有一定的英文的注释，英文的注释就是我们所需要去聊的。好，我们把直接就关掉。为了方便我们的测试，我预先已经是写了一些非常简单的方法。我们来看一下。在当前 s t u service 里面，我新增加了几个方法。首先一个是 save parent，另外是一个 save children，这两个是用于去做一个保存的，这个是保存了一个parent。最后又有一个子方法，就是 save children，这里面包含了两个保存，分别是一个 child 1 和 child 2。这个方法是非常简单的，大家拿到我的源码之后可以去看一下。


随后会有另外一个service，这个 service 主要去用于去调用这两个方法。这个 service 一个是调用 safe parent，另外一个是调用 safe children。这两个 service 都同在同一个方法里面。OK，在这边我写了一个注释，这个注释就是事物的传播，总共是有 7 个。我们会最先来讲 required 我们一些相应的代码。我们会使用 j unit 进行一个测试。要使用 j unit，首先我们就需要去使用相应的依赖。我们可以来看一下在当前我们项目里面，也就是在 a p i 工程里面我们的测试内容我是放在了 a p i 里面的，所以我就在 a p i 子模块的 Pom 文件里面去加入了一个 test OK 这一段代码。这一段代码我就不再去提供一个专门的笔记文档了，大家根据直接去手敲一下就可以了。


这个是非常简单的 sprint mode start test OK。它的作用域仅仅只是在 test 里面，把写好之后相应的依赖就可以安装到自己的本地了。随后在这里我又新建了一个 test 类，它的位置是在 test 包下面有一个 come 点 test trans test。首先要去运行，其实在这个里面首先要加的是一个 run with，是一个 sprint runner 点class。


最后对于我们整个 spring boot，它的一个启动类，你是需要去写进来的，也就是 spring boot test。把 class 定义为 application 点test，这两个是需要去写进去的。另外对于我们的一个test，这是我们的一个要去测试的方法，只要去测试我们相应的 service 就可以了。这个 service 其实就是对应到我们 test trace service 里面这一段的内容。OK，这个其实就相当于是一个副service，在它的这里面。这两个方法可以认为是一个子service，这点去注意一下。

OK。当我们在写好一个 at test 这样的注解以后，我们就可以去运行了。首先我们先来看一下，假设我们现在都不写它的一个事物，我们全部都不写，我们来看一下会出现一个什么样的问题，要出问题也就是要让他去抛一个异常。所以我们在这个方法里面我们可以定一个变量为a，它是一个整形的，让 1 去除以0，很明显这个是除不尽的，所以肯定是会在这个方法里面抛一个异常。这个方法是在这里面去执行的。所以我们会看一下我们的数据库。


最终我们现在不使用事务的时候，在数据库里面所出现的数据是怎样的？这个是我们的数据库刷新一下，现在没有任何的数据。好在这里我们只需要直接去运行一下我们的 test 这个类就可以了。右键直接运行，点 run trans test，点击一下，这个时候我们的控制台就会去运行了。当然很显然它是会报一个错的。我们来看一下这个错应该是在这里 my test，这里面有一个 by zero，除不尽对吧。


我们再来数据库刷新一下，你会发现保存了两条数据，一个是parent，一个是 child 1。好，我们回到咱们的 service 里面。children，它只保存了一条，也就是 child 1，这个是保存了。随后到这一行的时候，它发生了异常，以后 child on 是无法保存到数据库的。当然报了错以后，这里整个方法是没有回滚。随后我们再看一下 save parent。当然这个方法是在我们的负极负方法里面直接去调用的，它没有异常，所以它会保存到我们的数据库里面。


OK，现在我们是没有使用到事物。随后我们现在来开启一下咱们的事物。我们首先先把这个事物开启，我们定义为request。随后我们来看一下在这里面发生了异常以后它会不会回滚。好，为了进行验证的更加清楚，我们把数据库里面的数据删掉，把直接 unit 好，回到我们的开发工具，右键跑一下test。OK。现在又发生了异常，很明显还是白丝yellow。我们来看一下。


打开数据库进行一个刷新。现在我刷新以后你会发现其实并没有任何内容。刷新没有任何内容，这是为什么？这是因为在我们的方法里面，我们的事物其实是进行了一个传播。在这里它的负方法里面我们是写了一个required，它是需要有事物的。在我们的子方法里面，虽然我们没有为它去增加一个 transaction 的注解，但是这个事物是会传递到我们的下一个方法里面去的。所以当我们的子方法里面的异常出现了以后，其实我们两个方法里面的事物都会进行回滚。OK，这一点是需要去注意的。


好，随后我们再来看一个，我们把这个来进行一个注释，再把我们上一个副方法的给注释掉。现在其实就可以看得出来，在我们的负极方法里面，它没有事物。在它的子方法里面，我们为它添加了一个 required 这样的注释。随后我们再来运行一下，右键跑一下，现在我们数据库没有数据，刷新一下，你会发现我们现在跑完了，跑完以后现在还是一样会报一个错。


刷新你会发现现在所出现的情况是，我们的 parent 是保存进去的， parent 是它的负极方法，它的负极方法其实它并没有事物。在这里面我们把缩小负极方法里面并没有事物，所以它所调用的 save parent，其实它是会保存到我们数据库里的。

在这里我们之前也说了，如果当前我们这个方法所在的整个方法题里面，它本身就不带有事物，它会去重新的去创建一个事物的。也就是 save children 方法是必须要一定要存在于某一个事物里面去运行的，所以它进行了一个回捆。相反，我们的 save parent 它没有失误，所以 parent 会保存到我们数据库里面的。


OK，这一点是需要去注意的。我们再来做一个演示，我们在它的负方法里面把 request 给开启，一旦开启了以后，其实我们这里面所有的方法都包含了相应的一个事物了。所以我们在运行的时候肯定是会进行事务的回滚的。我们把数据库数据再进行一个删除。好，回过头来，我们再来运行一下。好，OK。在我们的空气台报错了，来到我咱们的数据库刷新一下。多次刷新没有任何的内容。OK。也就是现在我们的数据。这两个方法里面的内容，不管是复方法还是子方法，它们都会有事物，并且数据也进行了一个回滚。OK。好，在这里我们把它的一个注释给大家，可以去写一下。越快的主要是使用当前的事物。如果当前没有数，则自己新建一个数。子方法是必须运行在一个事物中的。OK，再补一下，如果当前存在事物，则加入这个事物，成为一个整体。我们换一下行。OK，使用当前的事物，如果当前没有事物，则自己重新去新建一个事物。子方法是必须要运行在一个事物里面的。如果当前存在事物，很显然，子方法会加入到这个事物里面，成为一个整体。


OK，我们可以来举一个简单的小例子，方便大家去理解。下方每一个我们都会做一个举例的例子。假设我们是有一个领导，领导没饭吃，这个时候我有钱，我会自己买了自己吃。这个其实也其实没有事物，我会自己去创建一个事物，如果领导有了吃，领导有了吃，他会分一些给你，领导有的吃，会分给你一起吃。


OK，这个就是我们的一个小例子，现在我们第一个传播，我们就已经是讲完了。在事物的传播里面，其实默认的就是required。 required 其实也是比较多用于一些增删改这样的一些操作，所以你使用 required 就可以了。随后我们来讲一下supports， supports 从字面意义上来看，它是一种支持，对于这种支持类型的一些事物，它主要是用于去做查询的，我们一起来看一下。


首先一个我们可以先把这个事物，我们外层的事物先注释掉，把外层事物注释，把它自己的事物改为suppose。我们先不说 supposed 意思是什么，我们直接可以先来看一下它的一个结果。我们来运行一下。先看一下数据库，数据库没有数据，好，直接来跑一下。跑完报了一个错之后，再来看一下我们的数据库里面新增加 2 条数据。OK，有数据。有了数据以后，其实主要是因为当我们使用 supports 了以后，其实我们的外层它并没有事物，外层没有事物，它就不使用事物，它是跟着我们外层走的。如果我们现在把外层使用了request，我们再来看一下。把数据库数据还是一样，我们 delete 删除一下，跑一下我们的test。好，也报了一个异常。报异常以后，我们再回到数据库里面来看一下，这个时候在我们数据库里面，我多次刷新它是不会有任何的数据，也就是我们数据没有入库。


事务是进行了一个回滚，这个其实也就是 suppose 的一个机制。我们来看一下什么是suppose，它是指如果当前有事物，则使用事物，如果当前没有事物，则不使用。 15 OK，我们在刚刚的演示里面其实已经是有了。它其实主要可以用于去做查询，因为查询我们可以不需要去有这种回滚的机制。OK，查询里面使用 supports 就行了。我们也是一样。举一个小例子，我们还是以领导吃饭为主，比方领导没饭吃，这个时候我也没饭吃。如果领导有饭吃，这个时候我也有饭吃，也，他是跟着领导的对吧？领导有饭我就有饭，领导没饭我也没饭。OK？所以这就是 support 的一个事物的机制。


大家课后也可以去试着操作一下，看一下 supports 和 required 它们之间的一个区别，手动的去操作一下，这样子会方便你更好地去记忆。我们再来看一下第三个，第三个传播，也就是mandatory。 required 和 supports 是两个最常用最常见的一个事物类型。关于military，其实我们也可以看一下源码，它里面的注释。通过源码的注释，其实我们也可以很好的去区分它是用于去干嘛的。来看一下它的一个注释。注释就是它的一个用法。首先它是需要去支持一个当前的事物的，如果当前没有任何事物，也就是它的负极方法，没有事物，此时此刻它会抛出一个异常的，也就是它是强制性的。强制我。当前这个子方法在运行的时候，我的调用方，谁调用了我，它就必须要有一个事物，它没有事物，就会抛出一个异常。OK，这个特性是比较强制的。它其实是比较类似于e、j、 b 的一个事物的属性，他们的名称是一模一样的。什么是 e c、b？有兴趣的同学可以去看一下。好，我们可以通过代码可以一起来演示一下。


首先我们先可以去演示他没有事物的情况，我们先把负方法，也就是调用方它的事物给注释掉。随后在我们被调用方的地方，我们就可以使用 mandatory 好保存一下。随后运行一下我们的test。这个时候我们的 test 报了一个错，我们来看一下。这个时候就不再是一个 by zero 这样的被 0 除的错误了。来看一下，它会说没有存在的一个事物被找到无意思什么，它是必须要配合 manatory 这样的一个传播性的传播属性的，它找不到，所以它就报错了，它是比较强制的。最后我们再把它的事物给加进去，我们再一次来运行一下我们的test。好，OK，现在我们已经是跑了。现在我们就没有再报那样的一个错误了。这个错也是由于我们自己去写的一个被淋除才出现的一个错误，所以这个就是一个 manatory 的事务传播机制，我们还是一样。我们在这里面我们写明一下该传播属性强制必须存在一个事物，如果不存在，则抛出异常。还是一样。我们举个例子，我们在这里所举的这些例子，其实都是主要来辅助我们去记忆的。这个举例其实就是我在公司，我在企业里上班。领导，你必须得管饭，你不管饭我就不干了，我就自己抛一个异常。领导必须管饭，不管饭，没饭吃，我就不乐意了 ，就抛出异常了。抛出异常，其实我就不干了。OK，这个就是一个 mana 图。第三个，一个传播机制。






