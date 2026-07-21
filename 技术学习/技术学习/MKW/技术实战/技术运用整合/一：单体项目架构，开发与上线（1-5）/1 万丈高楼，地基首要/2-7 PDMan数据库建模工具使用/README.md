---
title: 2-7 PDMan数据库建模工具使用
---

# 2-7 PDMan数据库建模工具使用

[image](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/876a1e44-154d-466d-8371-1adff2897118/SCR-20240816-cnhb.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UZHOLCRP%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T224604Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIG7JaKg2pzYoGW0W9VTTYiWCYnwZpziIlEtpE6DN4F8XAiBB9uPvN4b1tKPnHM4NuU8s4ww1%2BaCHhP8Lcxby4AsE5CqIBAjG%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMkjTic5ecqFYVUnS8KtwDGVsaCpv%2FvDHVSKfC2erkWJIhFuJgy7AY2rwI2WzdFwSiK0qCoLFO1az%2Fi95JbP6yeeKAfiOywQ8AQqJZ%2BTsJy%2FeQeUMOdUBFBvGWjAKr%2Bgp2jI%2Fz%2F5d7y4UufFvHCIKkIeMbf7YUhCcDcNue1kH4bXiwTKShsZpcATXIF3HOzE%2FnM5xD0Rm5tNn8PFY9UHB0FP0Djl1Z3g6Bn4S4BPDfdUMk51%2FIvqvAiaxmnJ%2B4Ys%2FhQa8GrpEOsuoeTLqJOrjZQupJoDRfT7dAGZ5MtRfe44tFXPRk3dEzb48WSSXF9FnJ8pLv5krKv4uRxlfGfnLwVJLd0BlaiW5M50m7JfC9uLzRXdWkq9UAUOtQcpHPS%2BNHWkuIAHaN75pxpl2MdNy6nDfUxHe75RiZhmlLN8iM%2BmjHqIGhUf0Wl3r44JFvNBofTjwvFGH7icbBeHVtWJh0rM3RmY8Xf1CyeU4oGfmavtFHlw6OsjnlMJB3fnZ9c10TrbHH4X7RPRj324QuKb%2BErY6XIvEyLVG1RDvxqGw2x5QHtffuorxo76YAETDWSG23invgjDhLPtBrVUbsCbTiOTulaPYRoEvaVDCQjNYCZ8XTrQofCC0yrmlCvN3o4iLg352d9aiJqwA9NfEws7r%2F0gY6pgGx21pdpLW4Oq2V%2B0gQrpRVYZiei%2BBfcg%2FqzVjHM5FQ4GJM4qO6BG%2FxpD%2FkeERv9mEmt%2Bmf%2BO150aoZHHiz24ilvnKuLZO97aLemCJoteqklYqAfcbzNnrQ6dQMzAG36xcbqnZhcCg4XILMrnpcexQwS2g4eLAoEzheBBytLXtoDe9%2FZzaJk%2FKF%2FcNlB%2BSKeXhAn79whfFuTipXjGQu5ESspcIVdVi3&X-Amz-Signature=e167c9db9a06b99fd80753387a184e1a613735e64f45b6a0a79e9cdb94b33398&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

[image](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/b65183d3-3a9f-4bc8-ad7d-ee81aaf4fd37/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UZHOLCRP%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T224604Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIG7JaKg2pzYoGW0W9VTTYiWCYnwZpziIlEtpE6DN4F8XAiBB9uPvN4b1tKPnHM4NuU8s4ww1%2BaCHhP8Lcxby4AsE5CqIBAjG%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMkjTic5ecqFYVUnS8KtwDGVsaCpv%2FvDHVSKfC2erkWJIhFuJgy7AY2rwI2WzdFwSiK0qCoLFO1az%2Fi95JbP6yeeKAfiOywQ8AQqJZ%2BTsJy%2FeQeUMOdUBFBvGWjAKr%2Bgp2jI%2Fz%2F5d7y4UufFvHCIKkIeMbf7YUhCcDcNue1kH4bXiwTKShsZpcATXIF3HOzE%2FnM5xD0Rm5tNn8PFY9UHB0FP0Djl1Z3g6Bn4S4BPDfdUMk51%2FIvqvAiaxmnJ%2B4Ys%2FhQa8GrpEOsuoeTLqJOrjZQupJoDRfT7dAGZ5MtRfe44tFXPRk3dEzb48WSSXF9FnJ8pLv5krKv4uRxlfGfnLwVJLd0BlaiW5M50m7JfC9uLzRXdWkq9UAUOtQcpHPS%2BNHWkuIAHaN75pxpl2MdNy6nDfUxHe75RiZhmlLN8iM%2BmjHqIGhUf0Wl3r44JFvNBofTjwvFGH7icbBeHVtWJh0rM3RmY8Xf1CyeU4oGfmavtFHlw6OsjnlMJB3fnZ9c10TrbHH4X7RPRj324QuKb%2BErY6XIvEyLVG1RDvxqGw2x5QHtffuorxo76YAETDWSG23invgjDhLPtBrVUbsCbTiOTulaPYRoEvaVDCQjNYCZ8XTrQofCC0yrmlCvN3o4iLg352d9aiJqwA9NfEws7r%2F0gY6pgGx21pdpLW4Oq2V%2B0gQrpRVYZiei%2BBfcg%2FqzVjHM5FQ4GJM4qO6BG%2FxpD%2FkeERv9mEmt%2Bmf%2BO150aoZHHiz24ilvnKuLZO97aLemCJoteqklYqAfcbzNnrQ6dQMzAG36xcbqnZhcCg4XILMrnpcexQwS2g4eLAoEzheBBytLXtoDe9%2FZzaJk%2FKF%2FcNlB%2BSKeXhAn79whfFuTipXjGQu5ESspcIVdVi3&X-Amz-Signature=02c18561b78ee270f4c321632545aa63accd3addbb1daf7f7b2e8da6773f04bb&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

到这里，我们现在整个项目通过每本去进行了一个构建。到这里其实我们就可以编写一部分代码了，但是往往在编写代码之前，我们所需要去做的，应该要针对我们的业务去做一个理解透彻以后再去设计一下我们的数据库。当然数据库设计可能不是开发人员去做的，也有可能是由架构师或者是其他的一些系统分析师去做的设置。在做设置的时候是不会直接使用数据库，在数据库里面去做一些表的创建设置等等。往往我们都会使用一些相应的数据库建模工具，可以有像 ES Studio，另外还有像是一些 PDMan等等类似数据库建模工具。


在这里会使用 PDMan，目前这个软件我已经是装了，叫做 PDMan，它是一个开源的数据库建模工具。网址我们是可以直接打开的，在这里 3W 点 PDMan 点CN。

[http://www.pdman.cn/#/](http://www.pdman.cn/#/)

如果你在企业里面使用过一些类似的数据库建文工具，可以按你自己的一个原则去使用你自己的一些工具是没有问题。在这里这个工具我是比较推荐的。首先它是一个开源的工具，另外它在windows， Linux 以及是 Mac 上，它都是跨平台的。另外它还有一个非常重要的功能，也是我所看中的。它有一个类似于 Git 的版本管理。每一次提交的生成的一些脚本文件，它都会有一个记录。比方你操作了哪一张表的字段，你去修改了什么，你去更新了什么，它是都会有记录的，这一点是非常不错，而且软件整体来说它也是轻量级的。就是他所打开的一个视图，所有的一些表他都帮我们放在了视图上，这个视图是可以一目了然，就知道这张表有哪些字段。


可能会有一部分同学会说，这种数据库设计工具其实到底有没有用，其实他们的用处是非常大的，尤其是在我们的一些像项目经理，产品经理。当你拿着自己的项目到外面去谈事情的时候，你肯定会使用类似的建模工具。你可能会直接打开这个工具，或者你可以使用它的相应的功能去生成一张表来跟大家去谈事情，而不是你拿着一个数据库出去谈，这样很显然是不专业的。当你拿着一个数据库建模工具，拿在这里面相应的设置，拿出去谈，会显得你相对来说是比较专业的。


OK，好在这里大家是可以自己去下载，可以看到三个平台都有。下载完毕之后，这就是它的一个主界面，现在我们在这里就直接把软件进行一个打开，打开以后整体的界面是分为了两侧，左侧的底部有一个案例，这个案例是可以去进行参考的，它是一个学生信息管理系统，可以点一下去看一下。在这里我们就不点了，因为我们会带着大家去讲一下的。在它的中间这一侧，在这一块它有一个创建新项目和打开项目。创建项目其实类似于创建一个脚本，打开项目是把现有的一个脚本文件导入进去，其实在目前其实我已经是有一个文件来看一下，有一个 food 杠 dev 点 PDMan点JSON，它的一个保存是以点JSON，是一个 JSON 文件，我是会给到大家，大家可以直接去进行导入。我们来看一下如何去创建。


首先一个在这里我们是需要点击创建新项目，点击一下，在这里会有一个路径，大家可以各自去选择一下就可以了。在这边我直接点默认克瑞斯。随后我们项目界面就已经是出来了，出来以后简单的看一下。在这里是一个保存按钮，做了一些修改，在这边进行保存。在这边还能去进行打开新进和另存为。


这三个就不去多说了，它还有一个是设置和数据库连接，我们在点一下这个是什么意思？点设置，它是指当我们去创建一张表的时候，它默认的会包含哪些字段。比方在里面它会有默认的 5 个字段，乐观所创建人、创建时间，更新人以及是更新时间，这些都是默认的。比方在这里假设我把创建人给删掉，更新人我也删掉。


点击确定。在下方这个地方是数据表，我们可以点击新增一个。比方我们创建一下，中文名叫做测试。点击确定。其实就相当于是创建了一个数据库。在这里面我再去新增一张数据库表，选择右键。新增数据表。选择了以后，比方我们随便来敲一个user，点击确定。这个时候我们来看一下，双击这一张用户表，随后在这边会有一个字段信息，点击一下，你会发现之前我们在设置里面所看到的一些相应的内容，它会默认的帮我们填充，填充了以后我们就可以直接去使用了。这个就相当于是一种预处理的模板，我们是直接可以拿来用的。


我们再来看一下。在这里面还会有一个基本信息。基本信息其实是针对于我们表的一个基本信息。比方这个表名就是在我们数据库里面所对应的名称，我们就可以取它为user。但是 user 在 MySQL 里面，尤其是高版本里面，它是一个关键字，所以我们在后面加一个 s losers 逻辑名是一个中文，我们就可以取名为用户表。这个说明是对于我们数据库表的一个comment，是一个解释，这是一张用户表，好， Ctrl s 可以进行一个保存。


随后我们来看一下它的代码信息，点击一下代码信息，可以看得出来，这就是一个代码。它是一个脚本。你可以在这里直接很多 c 拷贝，放到我们的一个数据库里面去。运行了。以后，这张表相应的内容，它是可以帮我们去生成的。这种方法是比较 low 的，我们是不建议直接复制，再到我们的数据库里面去生成，这种方式其实不太好。当然我们现在是在 MySQL 之下，其实它也包含像耳口， SQL servers， postgres 其实都有。另外它还可以映射成假法的实体类，可以看到，非常的方便。这里面相应的数据都有。OK，这个就是去生成一张表。

在这里我们可以先来创建一个字段。比方我们点击加号，我们来一个 user ID，这就是我们的一个用户组件。但是要注意字段名。在这里它其实是一个comment，我们可以直接写中文。比方用户组件ID。在它的逻辑名。逻辑名就是和我们数据库表里面的字段所对应的。把 user ID 拿过来，在这里会有一个类型，类型代表我们 ID 是什么类型。你可以设置为它是一个它。这下面有很多，可以设置为它是一个整数，也可以默认变成一个 Int 型了。说明加字段名。这两个加起来就是我们在数据库里面的一个comment。

写一下唯一组件。好，随后我们再来看一下，在这里它还会有一个组件，这个组件我们是需要去打勾的，把勾打上，随后我们再往旁边移，当我们打了组件以后，它必须是非空的。另外由于它是整形的，所以我们可以点击自增，打上一个勾，默认值我们就不用去设置了，因为它还会有一个关系图。另外还有是一个 UI 建议， UI 建议我们就不用去管了。

在关系图是什么意思？关系图就是我们有一个眼睛，如果你去掉这一列，在我们的一个视图里面是看不到的，在这里边我们往往会把所有的都展示出来， Ctrl s 进行保存。随后我们可以再来看一下，我们可以双击关系图，双击关系图以后，我们可以把这张表给拖进来，拖进来以后你就会发现你们相应的一些内容全部都有了。这个其实就和我们在它的一个官网里面看到的是一致的。当我们数据库表有很多，你把相应的表拖进去，所有的视图全部都在一张页面里面。这样子，当你不管是和团队在交流的时候，还是在开会的时候，还是跟你的领导老板，或者是你和第三方公司在一起谈合作的时候，你就可以拿出来侃侃而谈了，是非常有帮助的。

好，随后我们继续。现在我们在这个页面里面，假设我们现在就只有一张表，因为我们是做一个测试，有了一张表以后，如何去把我们的一个数据库和我们当前的这样的一个模型图去进行一个对应，因为我们要把这张表里面的数据，它的结构生成到我们的数据库里面去对吧？在这里面我们来看一下会有一个模型，在这边我们来看一下，其实它会有数据库逆向解析，这个其实当我们的数据库和我们工具连接在一起以后，可以把数据库里面的一些相应的内容逆向的可以解释一下，但是这种操作我不太建议，往往我们其实都是先设置好我们的数据库，随后在我们正向的向我们数据库里面去进行一个生成的。当然它还会有可以上去解释，PDMan，还有是 Erin 文件等等，这些都有，但是我们没有这种文件，我们就不去解析的。


d 2 脚本，还有导出JSON，导出文档都可以，都是可以去进行导出的，所以它的一个导出功能还是比较强大的。另外在这里会有一个白本模型，版本模型我们暂时先不说，其实就是类似于一个版本管理的。我们继续在这里，其实它还有一个数据库连接。数据库连接我们来看一下，目前我们并没有数据库对吧？所以我们要去把我们的数据库和当前的 PDMan 做一个连接，做一层关系。我们来看一下。


点击加号目前我们选择的是MySQL，它里面有相应的内容，选择 MySQL 就可以了。在旁边有一个驱动，驱动，它是可以去自定义的去选择驱动的。它还会有 drive class 和 URL 这两个。第一个它的一个整个 class 我们是不需要去管的，我们所需要去管的就是 URL 地址， ip 地址是什么，端口号是什么，还有数据库名称。因为我们当前这样的一张表是要放到某一个特定的数据库里面去的，所以数据库名你也要去加上去。另外在它的后面也加上了一些默认的设置。像我们的一个字符集是 UTF 杠8。还有是否要使用 ssl ，在这里是一个force。另外 use Unicode 是true。


还有是一个 server time zone， u t c。一般来说 UL 其实也就是我们在 spring mode 里面整合数据源的时候使用的，其实是类似的。另外还会有一个用户名和密码。我自己本地的数据库， MySQL 是 root 和root，停一下 ip 地址，直接写一个 local host。


端口号 3360 数据库目前都还没有对吧？我们可以来随便测试一个数据库，写一个 test a b c，先拷贝一下测试一下。这个时候报了一个错，连接失败。很明显主要是因为我们 test a b 7 库我们还并没有对吧。另外我们端口号写错了，应该是3306，点击测试说unknown，我们 test a b c 找不到，所以我们先点击确定。


随后再回到我们本地。我们是需要去把这样的一个数据库给创建。在本地我相信大家都是按照 MySQL 的，它还会有相应的一个数据库工具 Merry cat，我相信大家都用过。随后我们一起来把数据库去进行一个创建，来右键新建一个数据库。随后我们要把 test a b c 粘贴过来。字符集。很明显我们会使用 UTF 8，在这里还有一个 UTF 杠 8 的 mb4。什么叫 mb4？代表它是支持我们的一些表情的，尤其是手机端上的 emoj 表情，点击一下，下方会有一个排序规则，默认就可以了。


点击确定。这个时候我们 test a b c 就已经是创建好了，只不过这个库里面它没有任何的表。随后我们继续我们回到PDM，在这个 PDM 里面把数据库再打开，我们在这里面再定进行一个测试，点击一下，随后他就会提示我们连接成功了，也就是我们当前的数据库建模工具已经适合我们本地的数据库， MySQL 已经是建立了一个连接了。


点击确定好，随后我们该怎么做？我们应该要把这张表里面的一些信息生成到数据库里面去，来看一下如何去生成。要去生成点击模型版本，这个模型版本其实类似于一个 Git 或者是 SDN 的这种版本管理。来看一下。首先一个我们要去使用，要先初始化机械点击一下，点击确定它必须要强制性，我们输入一个版本号，比方来一个1点，来个零点，零点一版本描述随便输。点击确定，这个时候它会有很多的一些提示信息。我们是做一个版本的构建，我们最初的一个版本，我们到数据库刷新一下，你会发现在我们的数据库里面多了一张表，这个表叫做 PDMan d b fashion，也就是我们在刚刚的操作结束完了以后，他会在这里面创建一张表。相应的一些表，记录相应的一些版本。信息其实都是保存到这里的。比方我们在一开始所构建的对吧，都是由它系统去生成的。所以当我们在操作数据库的时候，这张表千万不要去动。好，继续。


我们来看一下，在这里会有最新的一个版本，还没有同步对吧？我们可以点击一下，点击一下可以看到，如果我们要同步在这里，它会有相应的一个叫什么，它的一个脚本文件，它会直接帮我们把脚本文件同步到我们的数据库的，在这里直接点击同步就可以了。当然如果这个版本你不想要同步，直接标记为同步也可以。我们在这里点击同步，点击一下，在这里提示数据库同步成功。随后我们把窗口直接关闭就可以了。关闭以后我们再来看一下，这个时候，当前这一行它就变成了一个绿色了。绿色代表我们当前的版本是已经同步到数据库里面了。


OK，回到数据库，我们来一个刷新。刷新以后你会看到在这里新建了一张用户表。OK，双击一下用户表，里面相应的内容全部都有。来看一下。拿一个表设置。第一个是版本的，它自带的一个版本号有邀请乐观锁，是创建时间和更新时间。另外这个就是我们自己新增的自定义的一个字段 user ID，它的类型是整形，长度默认 11。在后面像一些组件设置，还有是一个不能为空有个勾。另外有一个注释。可以看到这些全部都是从我们的一个数据库里面，从我们的 PDMan 里面逆向的应该是正向，如果是逆向应该是由数据库出来，如果正向是我们把一些相应的脚本往我们数据库里面正向的去生成。现在其实我们就已经是通过 


PDMan 去进行的一个生成。这个工具大家在课后去下载一下，去操作一下，非常便利的。当你尤其在使用它的一个版本的使用的时候，尤其是多个版本之间切换对比一些脚本记录的时候，是非常非常方便的。OK？

