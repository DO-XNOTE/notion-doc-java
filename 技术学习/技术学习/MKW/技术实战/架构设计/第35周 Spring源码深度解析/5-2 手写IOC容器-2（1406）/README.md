---
title: 5-2 手写IOC容器-2（1406）
---

# 5-2 手写IOC容器-2（1406）

[image](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/f5748994-e7ff-497f-afcf-4bad9e6e1ab5/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466S4QDEFCO%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T232030Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIDn2fbzH34w675OXsv5XMPJx%2FrenEioI%2F1ImARKAIx0vAiEAhQLlur8ng23Ul35w%2FZHnrbuETErp69Mqxq5CuivC6v0qiAQIxv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDDUP%2FsUQAxArQvkrCCrcAwieF%2F%2BvYOmKtGjYIpTWJw4hhoIFsSvogoVQy47809Aq%2BcRrJ8brk8DIm83tmpwsC2bOthQy3DjncrewXYceP47Y9VXQMc1rgx8u7dkayXI4YheMHp2pxlmWDDhXLSaeVibuVEbIGC4igRz3qtayv8c%2B7jIrAWv67ezpU95yCmqrPYLJgWeU0C7hRyYeocJSARQVY%2F9Ffx%2BgTdfev5Dit5cEIfbFTjmEvx4qsfoyttIk%2FtN%2Bnold9nYLqEFBLXETWwRjS7i7ZmZby%2Fl1z%2F%2F%2BO1DxzimmhCAgYyztY45hUupsP2yUqituBk8RZlOVDWXBwMzJ6QhLoVrAhGOjC%2BTNFZRgvVsKMLwR32qQ7eL6qXs28oFL1CyFUY9gf7OpoG0O4cRNEX2eINu28oD46avgDVPiLiE3%2FJ45rwbkdPDXmpmmq8BpcjOVclSBT1sKdNX8PRal7PYOxtdjsbtq7jXee87w%2BwH0dnxuTUCLa6P5gb16I%2Bc9QARAcOrsV8B4Y5g8hNImCgGw6%2BFd3pXwy6x1OCbAc%2BkGNaqb9DpeH6umrnVAnIMxPGP%2BV72NupCzk7RrqYHng7InKjmA%2BUXwQlC1HL0LwI1cOJl7mWqaJfSE%2BgwXkrqepv87YdcYx5EqMMO3%2F9IGOqUBGMBhShHU7qV%2BiCD6HhoelKdzDVdNtWfJynui9zfHEtBnH%2F2Yt1vWFXn2L9praYmPmVWm2MGmgEZP8rGWVxMlVYO%2BFZjorVlLwEcJ8QEHZkD6lJETFTYzkUMuWxx00RkC2qX8WQC4JMKe5NvU4W19rBfugejJtAAW52rxQJ%2FRcv8y6OokDb09RSaFnqF3RJPfEQVdmKE60KxLWjcH1fFVaKF69%2B9Q&X-Amz-Signature=73f3f35e826c9b6b91273bb7d932d06301bfe45f5a87793ef4248a900e387a8d&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

好，那么接下来我们要做的是什么呢？去构造我们的 LC 模块儿，那么 IOC 模块我们在想，我们在做这个事情，第一件事我们要做的就是对于我们包结构的少，那么在做我们具体 LC 容器之前，我们先写一个工具类去对我们包结构进行扫描，那么我们包结构扫描我们可以命名一个scanner，这里面我们要做的事情是对于我们指定的一个包扫描里面去对应的类，我们可以去这样。


我们命名为 packet class scanner。对于这个类我们可以参考我们 bin 里面对于注解扫描的类，当然它扫描的结果是一个 being definition，我们这里面为了简化，我们这里面并没有去保留 being dependent 的概念，我们只是直接把我们里面对应散描的包构造成一个类。


好，我们这里面去先定义这个方法，这里面的方法是什么呢？我们通过， scanner 方法，我们先定义这样一个方法，同时它是参数， package name，那么我们定义完这个方法，它的目的是我们输入一个包结构，那么返回这个包结构下合理的这些类的集合，也就是我们扫描出所有这些通过我们 manager bin 去管理的这些bin。那么好，接下来我们来去写它的实现。好，这里面首先我们去声明一下我们的返回值，定义 class set，我们就使用哈希 set 来去存储，同时我们把卡塞的区域返回，接下来我们需要扫描我们的包，那么扫描包的话，我们需要通过 cast loader 对应去获取我们的resource。


那么首先我们来去得到我们的 class loader， cast loader 我们可以通过当前线程的方式去获取，那么我们通过 class loader 去加载这些资源，这里面加载资源我们一定要注意它可能加载多个资源，我们在这里面选择 get resource，在 get resource 里面我们需要传入我们的路径，我们的 package name。看这里面需要我们举办内容 catch 一下。去返回我们的结果，这个结果的内容是它是一个枚举的类型，我们在这里面是需要把这个异常去转换一下抛出，这样我们就把一个非运行词异常改成一个运行词的异常。那么接下来我们对这个 packet name 需要进行处理一下，因为我们知道对于 Java 里面的包结构，它是以点符号去做处理的，那么我们需要做一个怎么操作，我们需要注的操作就是把它进行一个替换，我们把这个点改成我们对应的文件符号。


好，这样的话我们去查找对应这个枚举，我们对这个枚举进行一个遍历。对于枚举的便利，我们一般通常是 has 它有没有更多的节点，同时我们通用对这个节点去获取它的节点的信息，这里面我们得到一个 URL 对象，那么对于 URL 对象的话，我们一般会去关注一下它的一个协议，我们这里面只关心我们的 fail 协议，如果只有它是 file 协议的话我们才进行处理。


好，我们接下来我们去应该对这个文件去协议进行扫处理，那么在这里面我们需要去扫描文件，那么这里面我们先得到文件的路径，这个文件的路径我们这里面通过 URL pass 获取到，那么我们就可以去扫描我们这个目录了，那么我们接下来看一下这里面去如何去写。


我们扫描这个目录的话，它可能会涉及到一些嵌套一个循环，这里面我们会使用到一些递归的操作，对于我们的文件去嵌套的去处理，处理的过程中我们只关心我们去关心的加 2 点 class 文件以及我们的一个目录。好，那么现在我们去先写我们这个签到的循环，那么对于我们这里面定义这个方法的话，我们应该是这样，我们首先我们 scan fail，在这 scan fill 里面我们支持的内容首先是pass，那同时我们还需要去把我们的 packet name 来进行传入处理。还有一点就是如果说我们去替换的话，我们这里面的 plus side 可以做一个参数把它传入进去，这样的话我们可以在里面去进行对于它的集合的去处理。


设置好，我们一创建我们这个文件，这个方法，好，方法创建完成以后就开始我们进行对它的一些处理，那么首先我们去获取到这个 file 文件，我们获取 POI 文件，我们对它进行一个过滤，这里面是支持一个 fail 过滤器，这 fail 过滤器我们通过 lumbbs 去写这个过滤的过程。


我们关心哪些内容？我们首先这个 fail 它如果是目录，我们需要去签到执行，或者如果它是文件，我们需要去判断一下它，同时它的后缀，也就是我们的点 class 文件，在这里面我们用小括号标记一下它的顺序，我们这里面进行一个换行，这样看起来更方便一些。


好，对于这个结果我们会得到一个文件的列表，那么我们接下来对文件列表进行处理，一般我们会需要去迭代的去处理，在这里面我们处理的过程我们还是先获取到这个文件的名称，那么我们看如果说我们去通过这个名称我们去判断一下，在这里面我们对于文件和我们的目录去做一些处理。


那么首先我们看如果文件它是文件，那么我们要怎么处理？我们需要把我们的名称和我们这个包结构去进行一个关联，我们可以知道我们得到文件的名称，也就是对应我们 Java 的类名，我们可以跟这里面关联起来。那么我们判断如果说做一些为空的判断 not empathy，那么我们去构造一下我们的 class name，它就等于我们的 packet name 加上我们的类名，同时我们就过滤出我们第一个 class name，那么对于这个 class name 我们还需要做一些判断条件，我们需要判断一下它是否符合我们的一些逻辑，那么我们去进行一下对于我们几个方法去添加我们的class。在里面，同时把我们的 class size set 作为我们参数传入进去。那么另一个就是我们的 class name，同时我们去生成我们的class，在这里面我们去实现它，我们得到这个 class name 的时候，我们需要去把这个 class 去加载上来，看它是否是存在的。我们这里面需要指定一下我们的classloader，我们刚才在这里面已经用过一次 classloader 了，所以说多次使用的话我们可以把它进行一个方法化，我们去把它抽出一个方法，那么我们在这里面可以继续使用，好，因为 class bar name 它是需要我们对于 cats 一下，获取对应的变量，那我们接下来我们需要判断一下这个 class 它是否有对应的注解，我们怎么去判断也是比较简单。


我们先看这个class，我们可以看到，我们可以看它有一个是意思， annotation print present，也就是说当它的注解有没有出现我们指定的一个注解，这里面我们指定的注解是什么呢？我们指定的注解就是对应的 manage bin to class，如果存在的话，那么这个我们去进行添加，添加上我们这个 class 如果不存在的话，我们就不进行处理了，这样的话就完成我们对于这个 class 的一个添加，那么在这里面我们可以看到我们这里面只是对于 fail 进行对我们 class 的处理，那么对于如果是目录的话我们要怎么做？目录的情况下，我们需要进行一个递归的一个处理，我们需要做的就是继续执行我们的 scan fail，同时我们去传入 field pass，这里面要注意一下我们的 packet name 需要再进行处理一下， packet name 需要传入我们当前路径的名称。


好，这样就完成我们这样一个文件的扫描的过程。那么我们完成以后，我们进行一个单元测试，我们看一下它能不能得到我们想要的效果，在这里面我们创建单元测试列，其次我们去测试我们的 SCAN 方法，我们在这里面去scan，我们去指定一下我们的目录，那么我们可以在这里面去看一下我们的内容都是在对应的 demo 下面，那么我们可以去把这个包结构作为我们的参数输入进去。


这样我们得到一个 class 的集合，我们可以去打印一下，这里面我们需要把跳过破戒我们的 look back 对应的内容，我们这里面先自行看一下它执行的结果。
好，我们可以看到我们现在是打印得到的内容是第三个。诶，我们的 Demo deal in memory， Demo manager 和 Demo service，同时我们这里面可以去 get a simple name，这样执行的结果看起来会更清晰一些。好，现在我们得到一个正确的结果，那么接下来我们要去写什么内容？接下来我们去需要去实现我们的 being factory。

