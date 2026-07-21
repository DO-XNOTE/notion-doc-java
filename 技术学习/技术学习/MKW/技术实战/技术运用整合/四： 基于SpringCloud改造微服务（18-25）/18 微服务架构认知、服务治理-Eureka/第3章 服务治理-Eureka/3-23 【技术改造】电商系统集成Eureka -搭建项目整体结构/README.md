---
title: 3-23 【技术改造】电商系统集成Eureka -搭建项目整体结构
---

# 3-23 【技术改造】电商系统集成Eureka -搭建项目整体结构

[image](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/2700c194-9158-44c2-8ebd-22af0c9c9778/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WKO3FF3Z%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T225551Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIFnM7ld1tVVDnOxSkIDG8cihcqHpHjulkj42x3FJtCmJAiEAgM5awCubTirH6578cbOMZAfytocio%2BA7tvypTnn%2BTo0qiAQIxv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDDyBISrgDqVjx5tIQCrcA4fAvUJOzPF5wlVbKeMi1sHaDLb8%2BYNrUh%2BZWdEq%2F0ER8iShaOY8BTkjaRxc3U7fGrxUzAr0CTsUiuwoFtxJlW9FrZM1GdHnFKtM9Ro7nJG0jFEtUZcGC0hxiM0N7%2BuD4vHE6vGxqurshEyzTkvjkyyLtE8wB0BP2B7o1kaTnLvWvnZ%2B4XMc9Q2EbwqoPyPjRO952veOcA7olbLmvOU6UdlK77Q8fb66Jxt6aMT6pkX9AtQyEMYeU7uB1f%2FcU6aJG7GExwuZze12pklTyZJSviUo5EsqFJsmy7qsa6qd%2F3C9aqVIEohfXhByy9uC6LkGQkebtDMVSIP5e65uPTpOsY6AeYE238ogbWHkOfyQc%2FftQVqx%2FaaoCMSzFRvbAUBqHzjSzqQ6GJ1ZxDXsaCcquJRG8I0dzequeoAk%2FuzL0r1GZ%2FtpndFvzSAIteTbah0Ve0iXqlQGVm9oIJtmwFAJVFWpG%2BALGRC%2BT1QNJEr5tKqSLThP9iMENX4AQvSXizFvdSQ%2BubUdvFmiJ34kZABwtBnISxLlJLS78ljcJNs8sQR9vTBKpdpJ83OEcA7x3PjJF3jEe3HMK%2FhbaHvw3YJMjKOGhjLs8%2B6vcA8RYwZwcTdSuGJCQ%2FYf5vrvER67MLG6%2F9IGOqUBmNWXy2nZjbPxBm1xLlVgJhRUYDCZKlkt4znJOdG32EMO088lIU1R7Oz1mEZLC3bChxeYSQRyEvFQ4wdThvdQ3H0V7UEAyHMaC7qmiSH1FGZF1J0eCtWmEjPdOunXsHe0%2Fv6JiBKCIhjmUWskWLsqSVmK50ibvia4teKG6mDpxomTcD7YK%2BMOJFOJUf6slrPuI4hOKZLRdDbGxq9cOHtXd9SKiTyu&X-Amz-Signature=ade695fd2883fefe425285315f812320a4e77f4bf75a9fdee57f0b0803103014&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

hello 慕课网的各位同学们大家好，我是姚半仙。那同学们，终于等到了推进老城区改造计划的时候了，咱现在开始进行电商项目改造的第一步。那在这一个小节当中，我们先着手去搭建项目的整体结构。那这里主要分为三个步骤。第一步我们先去创建一个全新的 Maven 项目。接下来我们把主要的公共模块还有主要的文件夹结构把它搭建起来。

[image](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/3a935e90-4c6b-44c7-a244-171490a539d9/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WKO3FF3Z%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T225551Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIFnM7ld1tVVDnOxSkIDG8cihcqHpHjulkj42x3FJtCmJAiEAgM5awCubTirH6578cbOMZAfytocio%2BA7tvypTnn%2BTo0qiAQIxv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDDyBISrgDqVjx5tIQCrcA4fAvUJOzPF5wlVbKeMi1sHaDLb8%2BYNrUh%2BZWdEq%2F0ER8iShaOY8BTkjaRxc3U7fGrxUzAr0CTsUiuwoFtxJlW9FrZM1GdHnFKtM9Ro7nJG0jFEtUZcGC0hxiM0N7%2BuD4vHE6vGxqurshEyzTkvjkyyLtE8wB0BP2B7o1kaTnLvWvnZ%2B4XMc9Q2EbwqoPyPjRO952veOcA7olbLmvOU6UdlK77Q8fb66Jxt6aMT6pkX9AtQyEMYeU7uB1f%2FcU6aJG7GExwuZze12pklTyZJSviUo5EsqFJsmy7qsa6qd%2F3C9aqVIEohfXhByy9uC6LkGQkebtDMVSIP5e65uPTpOsY6AeYE238ogbWHkOfyQc%2FftQVqx%2FaaoCMSzFRvbAUBqHzjSzqQ6GJ1ZxDXsaCcquJRG8I0dzequeoAk%2FuzL0r1GZ%2FtpndFvzSAIteTbah0Ve0iXqlQGVm9oIJtmwFAJVFWpG%2BALGRC%2BT1QNJEr5tKqSLThP9iMENX4AQvSXizFvdSQ%2BubUdvFmiJ34kZABwtBnISxLlJLS78ljcJNs8sQR9vTBKpdpJ83OEcA7x3PjJF3jEe3HMK%2FhbaHvw3YJMjKOGhjLs8%2B6vcA8RYwZwcTdSuGJCQ%2FYf5vrvER67MLG6%2F9IGOqUBmNWXy2nZjbPxBm1xLlVgJhRUYDCZKlkt4znJOdG32EMO088lIU1R7Oz1mEZLC3bChxeYSQRyEvFQ4wdThvdQ3H0V7UEAyHMaC7qmiSH1FGZF1J0eCtWmEjPdOunXsHe0%2Fv6JiBKCIhjmUWskWLsqSVmK50ibvia4teKG6mDpxomTcD7YK%2BMOJFOJUf6slrPuI4hOKZLRdDbGxq9cOHtXd9SKiTyu&X-Amz-Signature=10a77770a6e4b8cbbba68d575e2c11d735c53791380d8091d26057015a2cc186&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

最后一步就是划分 pom 当中的依赖项，咱要把之前在父类 palm 当中分繁复杂的那一大堆依赖项，把它分门别类规整好，分派到不同的组件当中。这样我们就达到了依赖项治理的目的。就是说每一个子猫就它只引入自己需要用到的依赖项。那万事开头难，任重而道远。我们从这里就踏出了商城改造项目的第一步。同学们准备好的话，抄起家伙跟我 intelligi 开工。同学们这就是过去几个月中日夜陪伴我们学习的 foodie DEV 项目。我们在深情地凝望他最后一眼，因为现在要展开全新的篇章，跟他 say goodbye 了。


在一片难忘今宵的音乐声中，我们点开了新建项目的面板，这里创建一个全新的项目，它的 group ID 是咱的课程赞助商 com.imockok 那接下来 artifact 我们把它起名叫 foodie 杠 cloud 接下来点击 next 然后这个 project name 把这个福地 cloud 中间加一个横杠项目的存储路径，选择一个合适的本地存储的路径就可以了。


OK 那这里是老师自己的文件夹结构。好，我们现在点击 finish 等待倒数 3 秒钟。三二一好出来了。接下来我们就要在这个项目当中创建一些必要的文件夹结构。那都有哪些文件夹呢？我们先来看。第一个，咱前面提到了有一些公共的组件包对不对？比如咱常用的工具类，还有咱一些通用的 portal 对象，那咱这里都把它放到 common 文件夹下面。 OK 咱创建好 common 以后，先别着急，在这里面创建新的项目，我们接着去创建后面的文件夹。


第二个是 platform 大家还记得这里面放什么吗？注册中心、配置中心等等这些平台组件。那最后一个文件夹是咱放微服务的地方，它叫斗门。 OK 那这三个文件夹创建好之后，咱接下来做什么呢？找到这个顶层的泡沫在福地 cloud 下面的这个泡沫文件。那我们接下来对他做一做手脚，做一做重新定义。 OK 那这第一个地方，我这里要给他指定一个 packaging 那他的 package 类型是什么？ palm 类型？ OK 那下面的部分我们要从 food DEV 当中把它 copy 过来。 OK 那我这里切换到 food DEV 好，我这一股脑从哪里 copy 呢？我从这个 parent 一直往下拉，拉到最后面，把这一大串全部给它 copy 过来。好，我再切换回去。然后我们把它 copy 不过咱前面提到过，这里要做依赖项治理，那不需要用到的依赖项，我要把它删除对不对？那我们先来看删除哪些内容。


首先这个 parent 同学们在自己的个人项目当中，这样定义是非常方便的，也能快速搭建起咱自己的应用。不过在企业级应用当中，通常来讲我们的 parent 一般是继承自谁呢？一般是继承自。这个公司给你提供了一个统一模板，这是为什么呢？因为通常来讲，在大型的互联网公司，像 bat 他对自己的这些项目都有一些规范。那这些规范的具体细则通常就体现在一个父类的 palm 当中。比如说它可以在你父类 palm 当中指定什么指定你可以引入的依赖版本，还有它可以去引入一些 enforce row 之类的强制代码检查的组件。所以咱在这个项目当中就把自己当做是在做一个大型互联网公司的项目。那么我们这个 parent 就不再继承自开源项目组件，那我这里把这个节点先给它删掉。 OK 删掉之后我总要找一个方式来替代这个被删掉的 spring boot starter parent 因为为什么这个 parent 当中它引入了很多的依赖项，那我把它删掉了以后，我要把这些依赖项给它引入进来。


那怎么办呢？前面做 demo 的时候，我们也用了同样的方式来管理依赖，是什么呢？ Dependency management. 那这个 dependency management 同学们应该比较熟悉了，它是什么？它其实是把依赖项的版本控制引入进来。也就是说我在这个 dependency management 当中相当于制定了一个模板。如果你的子项目需要用到这个依赖，那你不用指定版本，这个版本从哪里来？就是从这个 dependency management 当中来。


好，我们在父类项目中指定两个 dependency 分别是什么呢？第一个是 org spring framework 后面是 cloudok 咱先把 spring cloud 当中的依赖版本给它加入进来 spring cloud dependencies 那它的 version 是什么呢？我们采用的是 green witch 基本的 sr oneok 那接下来我这里给它指定一个引入的类型 pom 类型，并且把它的 scope 限定为什么限定为 import 好，那咱引入了第一个依赖之后，接下来再引入一个是谁呢？前面是 spring cloud 那下面自然是谁 spring boot 了对不对？好，我们把这里改一下，改成 spring boot 然后下面的 artifact 是 spring boot 后面跟的是 starter parent 就是它了。


好，那这个版本我们和前面的 foodie DEV 项目保持一致，也是引入二点一点五的 release 版本，release。Ok.同样的它的类型也是 palm 然后 scope 是 import 那到这里我们的 dependency management 已经定义完成了。


接下来我们去清理一下 dependencies 咱前面说我的 pom 需要用到什么依赖才加入什么依赖，比如说像这个依赖 spring boot starter 那这个依赖在哪里才会需要呢？在你真正启动这个 web 项目的时候才会需要。所以如果你把它放在这里，那咱所有的猫就都会多引入这么一个依赖。咱前面提到过，我们的微服要专门剥离出一个接口层，这个接口层要提供给其他第三方的应用或者其他微服务来去调用的。所以在这种情况下，我们每个依赖项用到什么才加什么，这样的话可以大范围的避免依赖项的冲突。


那我们在这个顶层的 palm 当中尽量保留什么呢？只保留那些公共的大家都需要用到的组件。好，我这里从这个 spring boot 开始一直删到哪，我们往下删 AOP 也不要，这个 configuration process 也不要再往下看。 MySQL 和 mybatis 要不要这两个应用通常我们只放到 Doc 和需要启动项目的地方。那对于 API 层这两个应用也是多余的，所以也把它给删掉。 mapper 逆向工具 page helper Redis 这里都删掉。


好，我们删到这里打住以下的部分都是一些工具类，那这些就是需要在各个不同组件当中都要用到的配置。所以我们把这些配置给它暂时留在这里。 OK 那前面删掉的配置，待会我们创建公共组件的时候，会把这些缺失的依赖项加入到公共组件当中，也就是在 common 包下的一些毛酒类。


好，那我这里在 dependency 下面再多加入一个组件是什么呢？是我非常非常喜欢的一个大 I 的组件，那就是轮 book 偶尔及后面是 project loan book 没有提示出来。 loan book OK 它的 artifact 就叫 loan book 这里 version 我给它指定一个一点一八点八好一个 release 版本的 versionok 那我再往下在最后给它添加一个 build 节点。在 build 节点里面我把它指定一个 plugin 这个 plugin 是什么呢？是 spring boot 的 Maven compiler 也就是编译器，通常在 pom 当中加入这样一个 build 编译器是一个比较规范的方式。那好我这里 group ID 把它指定是 or 级点阿帕奇 Maven plugins 再下面它的 artifact 是没问 compiler plugin 第一个好，把它打上这里给它指定一个 version 是三点六点零。 OK 好了吗？还没有，还少那么两步。再下面给它加入一些 configuration 这个 configuration 我指定你的编译版本 source 是1.8，目标版本同样的保持一致也是1.8。那同学们这里可以使用引用使用变量的方式把它打进来。那老师这里就直接 hard code 了，省电视。


好。那再下面它的 encoding 是 UTF 杠8，实际上这几个变量都已经定义在这个 practice 上了，同学们也可以从这边直接把它引入进来。 OK 那到这里，父类的泡沫就已经定义完了。那接下来我们到这个 common 当中创建一些子的毛酒好，有哪些子毛酒呢？咱们来创建。第一个，给这个茅酒起名叫什么呢？它的名字叫 foodie 杠 cloud 杠 common 好，把这个 artifact 复制一下，点击 next 那 module name 和前面保持一致，然后把它扔到哪个包里呢？这里同学们注意一下，这个包名我们要在这里指定一下，把它放到 common 下面。


common 好，很容易拼错。 OK 点击 finish 那这个 common 包是做什么内容的？那我这里要把它的功能给它先声明出来。这里的 description 我给它添加一句，也就是这个包的作用是公共包和什么呢？和依赖项和依赖的组件。 OK 那咱前面删掉的这些依赖项，我现在要把它加回到哪里，就加回到当前这个 common 项目当中。 OK 那给它声明一个 dependency 节点。在 dependency 里面，我们要把前面删除的这些依赖项给它找回来。好，现在切换到 feed dive 项目当中。我们往上哟滑到这里。好，咱从第一个依赖项 spring boot 一直往下滑，往下滑，把它滑到哪里滑到这里。 page helper 好，到这里全复制过来。那这个 Redis 我们暂时先放这里不管它好再切换回去，把这些 dependency 全部复制到这里。


OK 到这里，我们这个 common 项目的依赖项就已经全部 copy 完成了。那接下来我就要去写这个福地 cloud common 下面的代码了。与其说写其实是借鉴咱从之前的腹地 DEV 项目当中，把这些需要用到的代码给它 copy 过来。


那首先我这里找到 food common 下面的 Java 文件夹，在这里创建一个包路径结构叫 com.imockok 那创建好这个结构之后，咱接下来再创建一个 my.map 那大家看到这样一个文件夹结构，肯定能猜到这里面是放什么呢？放一个公共的组件，这个公共组件是谁？就是 my map 好，那咱切换到 foodie DEV ，我这里全局找到 my mapper 然后就是它了。好，我们把它直接给 copy 过来。你看这个 mapper 下面有这么多类，为什么我只单单的 call my mapper ，因为剩下的这些 mapper 是不是都应该归属于不同的微服务模块下，只有这个 my mapper 它是一个公共的组件。所以我们把它给它 copy 过来，好再切换到 cloud 项目当中，直接把它copy。


Ok.那 my map copy 过来了以后，同学们还能想到还有哪些公共的组件需要移过来。工具类对不对好，我们接下来在这里面去创建另一个 package 工具类的 package 我们把它放到 utils 下面。 OK 那咱接下来就去 food DEV 当中，把需要用到的公共的 you Tuesday 给它拷贝过来。好，我们切换到 foodie diver 你看这里有这么多 util 的 sleep 咱 copy 哪些呢？来跟我一起数数。


第一个，这个 cookie utils 要不要，当然要了 data YouTube 同样的也要，然后这个也把它拿到。再下面一个类，同学们注意叫 IMock Jason result 这是个工具类吗？不是，它其实是一个公共的封装对象 PO 旧类。那么我们把它跳过，这里我们只 copy 这些 YouTube 类。好，那接下来这个 JSON you two MD 5 you two 还有 mobile email you two 4 号这几个 123456 把这六个类给它 copy 下来。那同学们会问了，剩下这几个无处安放的没有 copy 过来的类，那怎么办呢？不用担心，我们待会儿自然有地方把它们安置妥当。


那这六个类我们把它 copy 过来，好转到福地 cloud 当中。一二三走。你好勒。那写到这里，咱的福迪 cloud common 这一个项目就算已经写完了，那这里面是一些公共的工具类，还有这个公共的 mapper 也就是说各个项目都需要依赖的部分，我们把它放到了这里。


好，那接下来我们创建第二个公共的模块，这第二个公共模块我们给它起什么名字呢？好，这里创建一个梅文的毛九，它的名字叫做同学们看好，foodie cloud 后面跟什么 shared 泡酒。同学们看到这里应该就明白了，这个 share 的 portual 的名字就说明了它这里存放的是什么？是一些公共的需要引入的泡酒对象。那咱之所以把泡酒对象单独拎出来是为什么呢？因为泡酒对象 pogo 往往是什么呢？是非常纯净的 Java 对象。那纯净到什么程度呢？纯净到它几乎不需要任何第三方的依赖。所以我们把这部分对象单独抽了出来。同样在它的 Maven pom 依赖管理当中，我们这里什么都不，只添加一个谁呢？那这里唯一要加入的这个依赖项，我这里把它打出来 come.github get hub 里谁 page helper page helper OK 那它的 artifact 是 page helper 好，打完之后给它指定一个版本，我的 version 就是让它直接去拉 release 版本。好了，那这里就是咱需要引入的全部依赖项，保持了泡酒对象的纯洁性。


好。那接下来我们去到代码当中把这些对象给它 copy 过来。那第一步依然是创建一个包名，这个包名以我们独家赞助商 com.imock 的名义创建。好这个包。下面我们有这样几个子包，分别是什么呢？ in nums 它的枚举类除了 in num 这里还有一个 pojo 那第三个包我们创建把它名称起做 service serviceok 。


那这三个包下面分别放什么呢？我们挨个来看，这个 in num 同学们可能直接就猜出来了，这个 in num 下面存放的内容我们切换到 food DEV 当中再过来抄作业了抄哪些作业呢？我们就把这些音浪给它拷贝过来，那分别是这12345，把这五个对象统统给它拷贝过来。好，我们再切换回去到 food cloud 这五个对象排排坐到 in num 里面，待好我们重新 import 一下，没问项目。那完事以后，咱接下来就去 copy pojo pogo 类。好依然是到 food dive 当中，我们来搜寻花姑娘这两个 poture 类，它们就躲在这里，在 utils 里面，我们看挑哪两个呢？一个是 IMock Jason result 还有一个是 page 的 grade result 这两个实际上都是和前端进行交互的一个封装类，一个是封装的这个 JSON result 还有一个是封装了分页的结果。那我们把这两个类给它 copy 一下好，再回到 hody cloud 当中，把他们俩给放到这个泡酒目录里。 OK 那我看到有一个字段，好像标红了是谁这个 object mapper 。那怎么办呢？我同学们不要慌，看到这个 mapper 对象有人引用吗？好像没人引用。那我们偷偷摸摸把它给注释掉就好了。这就像有的时候我们提交代码，发现自己的代码被一个 UT block 住了，这时候怎么办？直接把这个 UT 注释掉，大不了被主管骂一顿。


对不对？好，那这两个类 copy 完了以后，咱接下来去找这个 service 那 service 为什么被放到了这个 share 的 portual 这个对象里来呢？同学们可能感到有点奇怪，实际上这个 service 并不包含业务逻辑，它跟这个 pojo 是没有什么区别的，叫谁呢？那就是咱的这个 base service 。
好，同学们可以看到这个 base service 的实际上就是包装了一个 page result 对象而已，只不过它会被所有的上下游微服务给公共使用，因此咱才把它 copy 过来，然后放到哪里呢？放到咱这个 share 的 portal 项目当中的 service 类里面。


同学们看到这里标红了，为什么？因为咱的这个 page 的 grade result 类是不是变了地方，咱变到哪了呢？本来是在 util 这个包下对吧？我们现在把它放到了哪里呢？放到了这个 portual 包下，所以这里咱需要重新把它引入进来。


OK 那到这一步，咱的 foodie cloud share 的 podu 也已经完成了。那在这个小节当中，我们搭建了一个很 high level 的微服务项目的结构。其中这个 common 模块封装了公共的工具类以及一些公共依赖。下面的一个 share 的 portal 类是一个非常纯净的不引入其他第三方的多余依赖，仅仅是封装了这些 pog O 类。


那在后面的章节里，我们这个 share 的 pojo 就会被引入到接口层。因为咱前面提到过微服务的接口层是要给其他的微服务进行调用的。那因此这个接口层里面的依赖越少越好，保持越纯净越好用到什么因物是吧？ OK 那咱这一节的内容就到这里结束了。下一小节，我们一起去搭建注册中心以及另外一个用于 web 服务的公共模块。 OK 同学们，那我们下一小节再见。


