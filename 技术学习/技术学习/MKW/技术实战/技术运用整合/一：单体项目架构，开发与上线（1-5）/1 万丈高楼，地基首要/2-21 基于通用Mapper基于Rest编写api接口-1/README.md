---
title: 2-21 基于通用Mapper基于Rest编写api接口-1
---

# 2-21 基于通用Mapper基于Rest编写api接口-1

[image](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/0dc4a573-9075-440a-92f0-f205f64e3ede/SCR-20240816-qify.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WH2FCH7U%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T224614Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDv0b0Zv170V4L7uPcFGk9PgSbu8TpXS6ByYFP8s25NgwIgHUmNCewOLEiU1WXTAExrZqvzUHUKykbw54yB45iDMVsqiAQIxv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDP8cOrGgp3uU72PRVyrcA%2F5wHdtd6DLoivRUqiJCQBNIOaIyHGswNKqEEetbfuOMqLLNCH679Xbi1vMRjY%2F8TRJzgv2MevL%2F8NZPmQQdFzKgwJPry0Yd%2BEe6xY3rbSNIcKHAdAgGxkKn6r0tt%2BZUBtXfvxBg5bqrtAtLkqy%2BwMGD5XCc74IBFiVhcZeNruUxiwxMcKbtkICzFB96W7KdfplK7rQoEnnQMDiVkHNhSKTrjUulrzpU%2B08oH4utBvB9b7zEay3RG6Tpnkj2pkYjHQaWnRHsOr8zHs0UMtN%2BVkh%2FdkbSqZWnRdlZq8YiPfRLOrD%2FdHeUmjT7q5fwamkgWPjnG0U5Sb9FLVCuoukZCkkjHKDnV7cLnJAwI9KnIC2Cr95022S75H3nkm7xZIEiBUd%2B5jp%2B7Y547IuvBT71F3b4n2UNIMl4nRx60iTknRxDN%2BW0MLB981FDakgdRxeK92%2B%2Ba5YngY7t7Lf5OFXpsX8et99zkUGHm1BdR0ekRxEd8gbsD4iwLBPZOMt1wv9AEbKzB6Dfg%2BWBjAYPKgmSXhyHiXTWr3SBnqCXfbfzUwtqPbKaw1c8VVevuBcKZ9uo%2Fb0nvH3RnfV7hAWoManxrhSz1sEgfYVg6BPaTajI9OfGcaUncP9TU7MrjuI8MOi5%2F9IGOqUBdjIQeQLgabtLOaYLxJgLe7Nqnnp77BtJ9FwxQGUTvn8SfwQDwhTgmc3a3iIudQOOFepSKdrtn%2BUGp0pZHm1Xdcd8Wd4S0WhhQa9paCmQsSOLcblNvhgVXDq5chJ2Vst%2BMSNvtgsGWdXDNt7%2FXZBmocBDN2rH2Eq7AP8rn%2Br6jWbJTWWAd93xPULoz99fiqpaMlWN4s23ikGVDcIkRsd715Q2uHRE&X-Amz-Signature=1d3e45e6fb493960a67236c04523ae712b32ded5d6520dd6d9e3e50d9fce5732&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

[image](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/9257132b-f906-4771-ab94-bc33a6c9850f/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WH2FCH7U%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T224614Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDv0b0Zv170V4L7uPcFGk9PgSbu8TpXS6ByYFP8s25NgwIgHUmNCewOLEiU1WXTAExrZqvzUHUKykbw54yB45iDMVsqiAQIxv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDP8cOrGgp3uU72PRVyrcA%2F5wHdtd6DLoivRUqiJCQBNIOaIyHGswNKqEEetbfuOMqLLNCH679Xbi1vMRjY%2F8TRJzgv2MevL%2F8NZPmQQdFzKgwJPry0Yd%2BEe6xY3rbSNIcKHAdAgGxkKn6r0tt%2BZUBtXfvxBg5bqrtAtLkqy%2BwMGD5XCc74IBFiVhcZeNruUxiwxMcKbtkICzFB96W7KdfplK7rQoEnnQMDiVkHNhSKTrjUulrzpU%2B08oH4utBvB9b7zEay3RG6Tpnkj2pkYjHQaWnRHsOr8zHs0UMtN%2BVkh%2FdkbSqZWnRdlZq8YiPfRLOrD%2FdHeUmjT7q5fwamkgWPjnG0U5Sb9FLVCuoukZCkkjHKDnV7cLnJAwI9KnIC2Cr95022S75H3nkm7xZIEiBUd%2B5jp%2B7Y547IuvBT71F3b4n2UNIMl4nRx60iTknRxDN%2BW0MLB981FDakgdRxeK92%2B%2Ba5YngY7t7Lf5OFXpsX8et99zkUGHm1BdR0ekRxEd8gbsD4iwLBPZOMt1wv9AEbKzB6Dfg%2BWBjAYPKgmSXhyHiXTWr3SBnqCXfbfzUwtqPbKaw1c8VVevuBcKZ9uo%2Fb0nvH3RnfV7hAWoManxrhSz1sEgfYVg6BPaTajI9OfGcaUncP9TU7MrjuI8MOi5%2F9IGOqUBdjIQeQLgabtLOaYLxJgLe7Nqnnp77BtJ9FwxQGUTvn8SfwQDwhTgmc3a3iIudQOOFepSKdrtn%2BUGp0pZHm1Xdcd8Wd4S0WhhQa9paCmQsSOLcblNvhgVXDq5chJ2Vst%2BMSNvtgsGWdXDNt7%2FXZBmocBDN2rH2Eq7AP8rn%2Br6jWbJTWWAd93xPULoz99fiqpaMlWN4s23ikGVDcIkRsd715Q2uHRE&X-Amz-Signature=f386126d4675d13e4d5f59a325f7d9f92a3d751bf3b7822131021a5a973f6ceb&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

在前面几节课程中，我们已经是把 Mybatis 数据层进行了一个整合。当然我们在上一节课程中我们也讲了 restful web service。在这一节我们就需要结合两者，我们来做一个基于 restful web service 的一些增删改查的操作。可能有一部分同学都已经是接触过了，但是没有关系，可以当做是一种复习。我们主要也是为了照顾一些没有接触过 restful web service 同学。我们一起来试着一起进行几个相应的操作。


首先一个我们要去做一些相应的请求处理操作。数据库往往我们都是从下往上去做一些开发的，也就是我们事先要进行数据库的设置，再去编写数据层，再编写service，随后到控制层，所以我们可以先打开数据库，在数据库里面预期我已经是创建了一张表，叫做 s t u。这个是用于做我们演示给大家看的，我们可以来设置。表里面比较简单，就是三个字段，一个是ID，一个是姓名，一个是年龄。 i d 是一个组件，在它的下方我们可以为它来设置为一个自增长，可以设置为的increment。好，随后保存一下。现在我们应该要去申请一下。咱们的表，就会使用到我们的逆向生成工具，还是一样，我们可以把这个表进行一个打开，随后在这里面我们就可以把这些全部都精简了。


把 s t u 写过来，随后我们再到这里面来进行一个运行，运行完毕以后我们把全部都展开看一下，在这里可以看到 s t u 相关的内容都已经是生成了，我们可以把这里面的一些内容我们可以拷贝一下。我们先拷贝 s t map，点 XM 拷贝一下，推到我们现有的项目里面来，找到现有的， Ctrl v 直接贴过来。好，这是一个。最后我们把它所对应的一个接口映射，我们也可以去拷贝一下，选择 s t u map， Ctrl c 拷贝。随后我们再到自己的项目里面来，在这里面 Ctrl v 贴过来就可以了。好，下一个是我们的一个实体层，也就是我们的泡酒，这个泡酒我们也是需要把它给拿过来的。


s t u 拷贝一下，把这个项目直接展开以后贴过来拷贝一下，在这里面的 s t u 就已经是有了，相应的东西都有。我们在这里面附加的强调一下，针对于我们的逆向生成工具，目前我们在这里生成的时候是只生成了一张表， SQ 对吧？我们可以把 s t u map 叉庙，我们可以展开看一下。在这里面其实我们之前就已经了，当它在生成一个数据库表的时候，会有一个 result map，这个其实应该是帮我们做到一个映射关系的对吧？映射关系是映射到 s t u 里面。我们来看一下。假设我们现在在这个项目里面，我们再次运行一下我们的 generator display，也就是我们再一次的来运行一下run，跑一下，我们来看一下。好，现在是运行成功。


运行成功以后，这个时候我们再来看一下当前的文件，你会发现它在下面部分又追加了一个 result map，名称 ID 和上方的是一模一样的。OK，这一点在我们使用逆向工具的时候一定要去注意。当我们的表重新的生成了以后，它这里面生成的一个 result map，它是一个追加式的。如果这个时候你没有去打开，重新的看一下文件，直接复制到我们的项目里面去。这个时候肯定在运行项目的时候是会报错的。这一点一定要去注意。这是因为在一个 map 里面，它的映射所存在的 ID 可以看到 ID 必须要保证唯一这里面有两个 base result，map，所以一定会报错的。这种情况其实我已经是遇到过，好些个学生都遇到过类似的情况，所以一定要去注意。因为逆向工具的生成在这里面它是一个追加式的，而不是覆盖式的，一定要去注意，所以这个是需要去删除的。


好，注意点。说完之后，咱们回到自己的项目，现在在咱们的项目里面立项工具生成的一些相应的内容都有了， map 就代表已经是 OK 了。随后我们就要去针对咱们的 service 去进行一个编写。好，我们把 service 展开来看一下。目前在 Java 里面其实并没有东西，我们来创建一个 package 包， come 点 Imock 点service。我们在这里创建包的时候需要注意，一定要 come 点Imock，因为这个东西是要被我们的 sprint put 容器要去扫描的，因为在我们的启动类里面。其实在之前我们也说了，在启动类里面，在 Com 点 m 可包以下，也就是它的子包都会被我们的容器所扫描，所以在这里要去注意一下 Com 点m。


随后在这里面我们来创建一个接口，取个名字叫做 s t u service，OK，在这里面我们只需要把这 class 改为 interface 就 OK 了。之后我们写几个相应的方法，第一个是查询，我们查询要根据他的 ID 去获得整个 s t u 的信息，把 s t u 给写过来， get s t u INFO 在这里面我们只需要去传入一个 Int 类型的 id 就可以了。


最后下一个 public 第一个是查询，第二个我们就可以来做一个保存，保存来一个save。 s t u 在这里面我们的信息我们就不直接去传了。后续我们在和前端整合的时候，保存的信息往往都是由前端封装为一个 JSON object 传过来。我们在 service 里面直接把一些数据去写死就可以了。这个是没有关系的。我们再来一个。我们来做一个修改，修改我们可以传一个ID，把名字改一下， Update 好再来一个删除。delete。 s t u 传也是传一个 ID 就可以了。现在我们在接口里面所定义的 4 个基本的c、r、u、 d 方法就已经是有了。随后我们就需要来再创建一个包，再来牛一个package，这里面就是实现类。好在这个里面我们来创建一个加班类，这个类取名为 s t u service i、m、p、 l 代表它的一个实现。在这里面你就需要去实现我们的接口，把 s t u service 接口给加进来。千万不要忘记，由于它是一个service，是需要被容器去扫描到的，所以你在这个类的上面，你需要加上一个service，这样就 OK 了。


我们是需要把一些抽象的方法全部都引入进来，我们可以按 command 加i，或者是在 windows 应该是 Ctrl 加i，可以把这些相应的方法全部都可以一次性的生成。生成好了以后，第一个在这里要去做一个查询的操作。在这里面我们来加上一个 private s t u Mapper，这个是把它的 Mapper 引入进来，应该是注入进来盯一下，使用 how to read。这个时候 map 其实在我们项目里面就可以去进行一个使用了。只不过在 map 下面有一个红色的波浪线，这个里面它会说无法去进行一个注入。


找不到 s t u map，这个其实没有关系，这是 idea 的一个关系。我们先暂时先不管，随后在这里面我们就可以来做一个查询了。由于我们在之前其实已经说过了，我们现在使用的 map 是一个通用map，它其实帮我们封装了很多的一些方法，我们前面有说过，所以在这里 return 的时候怎么做？写一个 s t u map，拿一个点，你会发现这里面有很多的方法。在之前我们写过的一个文档里面，其实全部都包含其中。我们可以来敲一下，来一个select，这里面其中就会有一个什么，会有一个 


select by 主键对吧？这个的时候我们可以看一下，直接双击一下，把 ID 写过来。你直接相当于是帮我们做好了数据库脚本。些相应的内容，帮我们做到了封装。如果你不使用通用map，相应的一些 circle 查询的脚本，你是需要去自己写的。OK，所以这个时候其实就非常的方便了。好，这是我们第一个方法。随后我们来做一个简单的测试。回到咱们的接口这一层Ctrl，我们可以在我们创建一个恒春的，我们直接把复制一下。我们可以来一个 s t u f o o 代表我们。这是一个事例，到这里面来看一下。首先一个我们指定的是一个 rest control 了，你 get 这个就用于去获取 get s t u，在它的后面会加上一个ID，直接可以在这里面写上一个 string ID，这样子就 OK 了。 service 我们也是需要去住进来一个 all to word。随后再来一个private， s t u service 给住进来以后，随后我们在直接可以通。

stuService。


The end. Get student info. 把 ID 给加入进来，这样子其实我们就可以传进去，应该是一个 Int OK service，其实我们现在还没有写完，回到 service 来看一下。在这里其实我们是需要去为它再加上一个事物，OK，所以把这个事物加上一个生命，是事物。再来一个propagation，等于 propagation 点suppose，因为它是查询，我们只需要事务的支持就 OK 了。随后我们就应该要去运行一下我们的项目，由于我们在其他的一些子工程都是做了一些修改，我们必须要重新的去进行安装。这个是在聚合工程里面一定要去注意的。把 maven 展开一下，install。好。安装成功。



怎么安装成功了以后，我们是需要去进行重新的运行的。我们把 application 重新的去运行一下。在这里面很显然报了一个错。这个措施指什么？是我们找不到这样的 map 定义找不到。这个是为什么？在这里红线我们先不管，不是因为红线的问题。我们来到application，这是我们的启动类。启动类我们在之前说了，它其实默认会把我们 com 点 m k。以下它所有的词包其实全部都会被相关的类，不管是 service Bee component 都会被它扫毛进去。但是对于我们的 map 来讲，也是需要去扫描的。这个其实是让 my baddies 去进行扫描的。所以千万不要忘记，在这里面你还是需要去再加上一个注释，叫做 map scan。注意一下， map scan 其实会有很多个，我们使用 t k 点 Mybatis ，使用这个包一定要注意，如果使用下面的会报错的。在这里面会有一个basic，应该是 base packages，这个就是我们的 Mapper ，应该说是通用 Mapper 。所在的。那些包在哪里，你是需要去进行一个指明的。很显然我们只需要把包名拷贝一下。包名在这里拷贝，随后贴到部位贴过来就可以了。我们前面的他没有加进来，写一下 COM 点 m 点map，我们在这边也可以去加上一个注释，扫描 Mybetis 通用 Mapper 所在的包是这个意思。随后我们再来重新的运行一下。


OK，这个时候其实我们就已经是启动成功了。在 8088 端口我们就可以直接去访问一下，我们是一个 get 请求，所以直接通过浏览器是可以去进行访问的。我们打开浏览器，我们直接在这边做一个修改。现在其实我们在数据库里面并没有任何东西，来一个 1001 回车，这个时候其实页面里面什么东西都没有。为什么？这是因为我们的一个资源请求路径不对。当你看到这样的一个错误以后，其实就相当于是一个404，可以看到 404 not found，为什么？我们来看一下我们的一个路径，我们的请求参数ID。我们 ID 是放在路径里面的，所以它是一种路径参数。在 restful web service 规范里面。


这样子的一个路径，对于我们的后端来讲，其实我们应该要去做到一个一一的映射，但是我们并没有去做到一个路径参数的映射，所以我们 ID 应该要作为一个请求参数去传进来的。OK，所以我们再回到这里面，我们去进行一个修改，我们只需要在后方加上一个问号ID，等于 1001 回车。这个时候我们就不会再报这样的一个异常了。只不过现在是一片空白。为什么？


因为我们数据库里面并没有任何的内容，所以我们双击这张表，我们在当前这张表里面去添加内容，有一个加号，点一下。随后在我们来个 ID 是 1001 name，来一个 imock age 18 岁，好点打勾。OK。随后再一次回到页面，刷新一下，你会发现我们相关的数据就已经是成功的可以获取了。OK，现在其实我们第一个 rest for web service 这样的一个接口就已经是 OK 了。





