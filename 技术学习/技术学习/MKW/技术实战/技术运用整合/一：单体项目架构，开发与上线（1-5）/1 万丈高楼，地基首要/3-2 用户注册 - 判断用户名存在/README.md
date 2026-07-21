---
title: 3-2 用户注册 - 判断用户名存在
---

# 3-2 用户注册 - 判断用户名存在

[image](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/2c64ce14-458d-440a-886d-3eadccffd9a2/SCR-20240816-tffh.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662WPARSRH%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T224622Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIBUA88LMdl0PUGH8MGOfgr%2BHjouWYcQyOJy0h7wQD2ZAAiAJ5dVbG8G1T6QKLtvs2%2FQVAk6K8opJJziBok%2BDlflGRSqIBAjG%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIM4LBF5MiDgCcb9tnzKtwDouzjzLLbbYiDahjukVDqQiNoT0xhPvBUrAOcR%2FTGqjGB2J5%2F%2FeGD6rvZKKXuj13vQdWbtLr9lEtgeCMq4TTa065Tnwzp0FvVsYhm9ZASKabqli24KDZThZCzEAsK%2BmVYNT8w6P0GG%2Bp2XHZPq1ubK0ux%2FynZiuopf4PO4ofX%2F7zXoMIw8FOVFd9fdZEbyj4voZBnWtm8MlJtcUfj0xOzBPYLFk1dg0JB0l3ZX%2BqEJc%2BmdQzqA5P4ZQp8HUT%2BHuv3%2FNuFUQ5NRXq%2FYtirYOVmGjQgJ3CTf63c%2FLML9E%2BFzNDT6UHifAlH7j24zFUh9k7%2B2da%2FLjQX%2B%2FOzMEegM%2F9jrUBqDq6epUirrc3%2FCV8hs8WjFx5Qaqr1sz1eJjGMYz4Wo81kYQy6R5tUNpshhOaB6c3PSMOJAoQOUOm%2FtiDcMqVvh6wEDS3jyThN85R4xgTHKhbRCYTsGmax2GlZ7UK35qwYZj7RT1r4i3jAw9bQ6ZxdUZp7pVvACTAVeZbJIdq0ku9nvng3%2BYlmZj33lm29xhP7NB%2B9qaQ%2Bk%2BnzCTSEXdhOVfNasx%2FNzZ4lWfywn2vKK2vVU0Mt8KOsnhEYNfeIbrnmi7YuYOk5xq3Z7gXjY6Y0xlJBAZynQhMPsRww17r%2F0gY6pgEZVHKTgqwnE1Gyw%2F0tIX6xqN1N%2BCOh7A0kJfsWGpu6vIAE2xCyw%2B0R76vZ38grjBb1fBINBq8XfWwvHe3LKW%2BXBFOOdSFlXiEDrwPdaimwYZUuF2GvS7KLzIdiQM4uN6OykjNe4JEt0YJNi6vu%2Bp0F7xO8pLFy0btGFvcCLqaVc7CHGtoFqbGAiO%2BCnTRPQzFwbJJqZ9lautmrh%2B5XtfMe8uI60Nkd&X-Amz-Signature=7c9e0109290833d06863f00aa435a232176534784c9435237a7991a716261f23&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

[image](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/6e4a75bf-31ff-4f0a-8ff0-095401e13382/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662WPARSRH%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T224622Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIBUA88LMdl0PUGH8MGOfgr%2BHjouWYcQyOJy0h7wQD2ZAAiAJ5dVbG8G1T6QKLtvs2%2FQVAk6K8opJJziBok%2BDlflGRSqIBAjG%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIM4LBF5MiDgCcb9tnzKtwDouzjzLLbbYiDahjukVDqQiNoT0xhPvBUrAOcR%2FTGqjGB2J5%2F%2FeGD6rvZKKXuj13vQdWbtLr9lEtgeCMq4TTa065Tnwzp0FvVsYhm9ZASKabqli24KDZThZCzEAsK%2BmVYNT8w6P0GG%2Bp2XHZPq1ubK0ux%2FynZiuopf4PO4ofX%2F7zXoMIw8FOVFd9fdZEbyj4voZBnWtm8MlJtcUfj0xOzBPYLFk1dg0JB0l3ZX%2BqEJc%2BmdQzqA5P4ZQp8HUT%2BHuv3%2FNuFUQ5NRXq%2FYtirYOVmGjQgJ3CTf63c%2FLML9E%2BFzNDT6UHifAlH7j24zFUh9k7%2B2da%2FLjQX%2B%2FOzMEegM%2F9jrUBqDq6epUirrc3%2FCV8hs8WjFx5Qaqr1sz1eJjGMYz4Wo81kYQy6R5tUNpshhOaB6c3PSMOJAoQOUOm%2FtiDcMqVvh6wEDS3jyThN85R4xgTHKhbRCYTsGmax2GlZ7UK35qwYZj7RT1r4i3jAw9bQ6ZxdUZp7pVvACTAVeZbJIdq0ku9nvng3%2BYlmZj33lm29xhP7NB%2B9qaQ%2Bk%2BnzCTSEXdhOVfNasx%2FNzZ4lWfywn2vKK2vVU0Mt8KOsnhEYNfeIbrnmi7YuYOk5xq3Z7gXjY6Y0xlJBAZynQhMPsRww17r%2F0gY6pgEZVHKTgqwnE1Gyw%2F0tIX6xqN1N%2BCOh7A0kJfsWGpu6vIAE2xCyw%2B0R76vZ38grjBb1fBINBq8XfWwvHe3LKW%2BXBFOOdSFlXiEDrwPdaimwYZUuF2GvS7KLzIdiQM4uN6OykjNe4JEt0YJNi6vu%2Bp0F7xO8pLFy0btGFvcCLqaVc7CHGtoFqbGAiO%2BCnTRPQzFwbJJqZ9lautmrh%2B5XtfMe8uI60Nkd&X-Amz-Signature=ef7eb59082c81d0b915b63b9ed74297055bc077566ccdba7ef6f10ceebd25e83&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

现在我们就来实现一下我们的用户注册功能了。首先我们可以先来注册一下，现在其实在我们网站里面，我们是 0 注册，没有任何的用户填写，用户名是m，密码是123123，在这里这个密码我是输错了，点一下会提示密码与确认密码不一致。这个是由前端所做的一个验证。其实验证不仅仅是在前端要做，在后端也要做。要这样子做的目的是什么？在前端做是为了防止有一部分的一些校验信息到达咱们的后端，减少我们后端的一个负载，这是你必须要去进行处理的。


另外一方面，在后端要去做是为了防止某些用户绕过我们的前端，直接来访问我们的服务器，这样子如果在服务端没有去做到一个验证，两端都没有可能就会造成黑客的攻击，这一点其实两端都必须要去控制好。我们再来把密码修改一下， 123123 点击注册，这个时候其实我们的用户其实就已经是注册成功了。用户注册成功以后，我可以再来点击一个退出，退出是在这个位置，可以大家来看一下，在我们的侧边这个位置有个小人，点击一下有个退出登录好，退出登录以后我们再来进行一个注册。这个时候我们的 m 可其实我们就可以来看一下，他会提示一个问题，目前用户名已经是存在了。


OK，其实主要是因为我们做好了一个校验的控制，这个校验的控制是由前端所发起的，只要是前端的用户在框里面输入内容，它就会发送一个异步请求，到后端去进行一个校验。所以我们首先要做的第一个接口应该是要校验一下用户所填的用户名是否存在。好，现在我们在做这些，我们还是不能马上的去写咱们的代码。我们要去看一下我们的数据库的一些结构，这个是我们的一个用户表，我们可以来看一下。


在表里面。首先第一个用户的组件是必须要有的，在这里用户组件我设置为是字符串 64 位的。我们没有使用自增长ID，我们在这些其实已经是强调过多次了。在集群分布式或者是微服务环境的一个情况之下，我们的所有的表的 ID 我们都要控制为一个全组唯一的，除非是那种表的一个访问量是非常非常小，表的数据量可能只有十几条，几十条，上百上千。对于这种其实无所谓，你要使用自增长是没有问题的。


好，下一个是用户名密码，这个密码我们是会进行过加密，你用户进行过，用户输入的是一个明文，我们到达后端以后，我们要去进行加密。加密我们在这里使用的比较简单，我们直接使用 MD5 去进行一个加密就可以了。随后是昵称，还有是用户的一个真实姓名，头像，手机号，邮箱地址，性别，生日。创建时间和更新时间。创建时间其实也就是用户的一个注册时间。此外还有是更新时间，更新时间是用于给用户去更新的，用户在进行一些相应的信息的修改的时候，只要修改完你的更新时间就可以去更新一下，像手机号和邮箱，我们一开始虽然没有输，但是用户在后续的过程中也可以去根据自己的一个需要去修改用户的信息。当然我们头像还会涉及到文件的上传，一张图片。OK，这些其实我们都是会涉及到的。好，这个表其实我们在数据库表里面其实也已经是生成了，在这里都会有，大家可以去过一下。好，随后我们就来编写咱们的一个接口了。


在编写接口之前，其实我们的一个写的方式，我们要有一定的原则，我们的原则其实是从下往上写下，其实我们的数据层从底往上去做，这也就相当于是我们在造楼的时候，不管你是在造房子，造楼还是造别墅，我们首先要去做的其实就是修地基，修完 d g 以后再逐步向外去做。在我们开发的时候，其实我们也是推荐以这种方式去做。先把我们的数据层，也就是 service 去写好，写完以后再去写我们的接口层。好，我们在这里可以先把service，我们可以先展开在 service 里面。现在我们可以先来看一下，目前在 service 里面是没有任何内容，这些都是我们之前去用于去做测试的。好，我们直接拷贝一个，直接比较方便。


Ctrl c Ctrl v。

在这里我们可以来创建一个叫做 user service，这是一个接口。好在接口里面我们就可以去编写相应的内容了，我们先可以把这些先删掉。我们首先进行第一个接口的编写，是用于去查询的 query user name is exist，判断一下用户名是否是存在的，加上一个注释，判断用户名是否存在。在这里我们就需要返回一个布偶值，我们传入的是一个 user name 传进来，传进来以后我们就可以去做一个判断，这是咱们的一个接口。好，我们来写一下咱们的实现。实现我们还是一样直接拷贝分比较方便。 user service 好双击一下打开。


打开来以后，首先第一个我们需要把它的接口给改掉，是 user service。随后在我们当前这个类里面，其他的一些内容我们全部都可以去删除了。随后我们可以来把导入一下。好，导入进来以后，我们就可以去实现咱们的方法。快速导入是 command 加i，或者是在 windows 端是 Ctrl 加i，是可以去快速导入的。


好，我们把写一下 users Mapper，把它的 Mapper 映射，我们先可以去写好。写好以后，在这里我们就可以去做一个查询的操作了。要去做查询之前，其实我们演示的是使用某一个 map 点select，然后 select 是one，使用的是这些都是可以去做查询的。但是我们 example 其实我们没有做演示，所以我们可以使用 example 来去进行一个查询的，也是没有问题。 example 通过条件去进行查询的，我们在这里可以去写。


首先我们先来写一个example， d 为 user example，你是需要去把它给 new 出来的， new 的时候在这里可以看到初始化，其实要把它给实例化的时候，你要传入一个class，你要去查询每一个对应的实体类，在这里面实体类就相当于是一个 users 点 class 把它给传进来。这个时候针对用户这张表映射它的 example 就已经是创建好了。


随后我们要去创建条件，条件其实就是在 example 里面，我们可以通过 user example 点 create 来看一下，它有一个创建条件，它会返回一个，这个其实就是类似于 habit 里面的一个条件，你可以根据这种条件去组合各种不同的一些查询。多样化都是可以去使用的，我们直接来进行一个创建，可以看它的源码就会返回这样的一个条件，我们在写一下，定义为可以加上一个user， user 前缀好。


创建好以后我们可以来看一下。通过可结它，其实可以构建很多的一些条件，比方它会有 and equal to，这个时候是判断参数的一个对比，你要一致。另外它还会有 between 区间，还要去加上一些条件，肯定是大于，另外还有是大于等等都会有，包括还有是像in，还有是 is not more 不为空有很多，包括小雨等于也全部都有。另外还有是使用查询最多的like，这里面会有很多。


在这里其实我们只需要使用一个就可以了，因为我们是需要去和我们的用户名去做一个对比，所以使用 and equal to 在这边会传入两个相应的属性。属性前面一个是property，我们来看一下。 property 其实就是针对于我们 users 里面的用户名 user name，所以只需要把拷贝一下贴到这个部位就可以了。你要去和数据库里面哪一个字段去进行对比，你只需要去把这个属性拿过来就可以了。


好，下一个我们传入的一个值就是 UED name，这样子我们的条件其实就已经是构建好了。随后接下来有了条件我们就要去做一个查询的。使用 users map 点会有一个 select 找一下。现在其实我们是根据 user name 去判断是否有一条记录，所以我它其实会有一个 select one，找一下。在这里 select one by example，我们通过 example 去查询一条记录，所以我们只需要把 example 往这边一贴。这个时候我们就可以去做到一个查询了。随后我们只需要在它的前方我们去加上一个users，把用户类去进行一个接收。我们定一个result。好。拿到了这个 result 以后，我们只需要去做判断，我们要判断它是不是为空，如果为空我们就是force，否则就来一个true。查询我们的用户名是否存在。 true 代表就是有，force，代表就是没有。


好写完了 service 以后，我们就应该要去编写一下咱们的 control 的了。 control 其实是和用户相关，写一下。我们找到 API 这一层，我们在这边其实可以拷贝一份，把s，t， u 的拷一下。我们在这边通常来说可以定义为 user control 了，但是我们不这么做，我们使用为passport，通行证的一个意思。在这里面去进行咱们的一个代码编写。先把这些内容先去精简一下。新我们查看一下的 service 上，我们是加了一个事务，由于他去查询，我们使用 sports 就可以了。事物传播我们在之前已经是讲过了。好，回到我们的 Ctrl 了。在这里我们所需要注入的 service 其实应该是一个 user service。


写好了以后，对于我们整个 control 的，其实我们应该要加一个路由进来的 request map，写上，我们直接作为写上是一个 passport 通行证好，我们就要写上我们第一个所要去使用的接口的名称。在这边我们可以返回一个Int，判断 user name is exist 返回的值。 Int 我们后面会说的，我们后面会针对状态码会来进行一个讲解，并且我们也会把它进行一个封装好。首先一个我们先要定义一下，由于它是查询，而且查询的内容比较简单，所以我们直接可以把它定为是一个 get mapping。通过 get method 这可以请求到我们当前接口了，好为它定义好路由。


user name is exist 好，我们要传入相应的一个参数，这个参数只要传进来一个 user name 就可以了。定一个 user name，当然我们可以在前面加上一个前缀，前缀可以写上一个 at request，Tom，这个就是代表它是一种请求类型的参数，而不是一种路径参数。


好，拿到了以后，首先第一个我们要判断邮件内是否为空，如果为空肯定是不可以入库的。我们直接抛一个错，比方，我们先可以判断使用 string 有跳丝找一下。在这里面有很多的一些utils，但是这些 utils 其实对于我们来讲我们现在用不到，我们要使用另外一个 string 有效来辅助我们去做。


关于工具类，其实我已经是预先为大家所准备了，我们可以来看一下。我们可以到当前福迪的一个聚合工程里面，我们把 Pom 文件打开到最下方，我直接把内容给贴过来，这一部分就是咱们的依赖。这一部分的依赖其实都是属于阿帕奇的，都是阿帕奇下方的一些工具类，我们是可以去使用的。其中我们所要使用的一个工具类就是判断字符串的是在 comments long 3 包依赖里面。


现在我当我导入了以后，在这边我们再来看一下它就会有一个阿帕奇下的一个 string toss，我们使用这个就可以了。其中它会有一个 is not blank 和 is not empty，这两个其实我们都是可以去使用，只不过使用 blank 它可以额外的再去判断一下你是不是空字符串，所以我们使用就可以了。


我们来判断一下，在这边我们应该不是使用not，使用判断它是不是为空，如果为空，我们在这里直接 return 一个错误的状态就可以了，比方我们在对于出错了，我们就可以定义为是一个 500 错误，直接返回一个500。随后在下方我们就可以来判断一下我们的用户名是否存在了。我们来加一个注释。第一个判断用户名，也就是入参不能为空，围攻就直接不需要去验证了。第二步查找注册的用户名是否存在。在这里我们只需要通过 user service 点第一个方法 query username is exist，把这个参数传进去，随后我们会得到一个布尔值 yes exist。


好。随后我们来做一个判断，如果它为true，为 true 就代表是有吧，有我们在直接就可以。报错了直接给称一个500，你称了 500 以后就可以。我们其实是一个用户名是存在的。当然如果我们这些都没有问题，到最后我们直接也蹭一个 200 就可以了。 200 状态是代表我们。 HTTP 是请求成功的第三一步，请求成功用户名没有重复。这个其实就是我们第一个开发的接口，现在其实就已经是写完了，内容相对来说也不是特别的复杂。




