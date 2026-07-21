---
title: 1-8 【源码品读】资源文件加载流程深度解析
---

# 1-8 【源码品读】资源文件加载流程深度解析

[image](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/6d67deb1-dd0e-476c-b5f6-23fb00a48a32/SCR-20240720-psrw.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RECLAZE6%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T225708Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDb8Zu31z7cn7DKH960r846mO4YlsK0CoTEZ0gOi8O5MwIgRwHnS13MEJuNh0V4NRRk6LzSkYQq5ZSLS%2BaC0Saa7xIqiAQIxv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDP%2FHmNPeZppgNIVeCircA2HTe6v89iPiDiDlAdBARohP5Tg%2BHah9NTAxaX7pVSTOk8jgEYUIwYGVMtHkns80yjApv0esFAEMUWHPZA7jTkd05laZLiuoK3SWgnKksyy2C479DrzGf80UQOL%2BTCk0xnCBiuxOvrVj2JccO3r3Al7RZ8ZCfKAqC0VQcUGi1NMzw8QTmh7t6zbY8gTLn3UkiTKTjIWFDYLAiGMxUw%2FO9av9%2BtSfyGwuXGo8MQemz5rdZ4xSOiFAd%2FNebH2S2KGSV%2F6q7z7PJrLP9YoPe17ehmQeTC%2B%2FmnFMszSQdkLa%2Fxqb8XG3PENp5BRmJGAdf%2BTDN9TNu%2F5Thae9YallUBcAoIe541EQEzTBLBYf2g3Dz0VlAMDO1w2%2BMnbP86P%2FwhKloeOuHV2mxVv9wsYxztj%2BcmPRdY%2BVk8Tw6jQQUxEQH4c0fY1WmPrTTzOoDCeJOK8%2Be0kCmVRSZO%2BblwiFCEMyE%2BN2MQmPnBK6lO5tdtFQX4ol2y3ZOzYCmPDACF44MsGuLzX1MI5Gx%2F2ayd%2FzDgKzXtfWcCgVmhGvRYiEMd9ey8m38EfWi%2BqkyPwlR39UO7kNe%2B1r83BvwutdXdJY6dCzdg2MiCRoQrb2LyoMxq%2FZNMHK1yHLd1XvG72NkOswMJa3%2F9IGOqUBCN7%2F1I8ssNuEZ6EbOsyK2MDW%2BeBQQsIHtSvx6pJVcWPrdeMU%2B9YgQqWDv%2Bl9f09zJ3S6IW28U7uCP7nqf4S3d1rBI3Yu0w3%2FjnN2cfhpUlyyYO07La7zlN5SMx6BAbl9mlJvYrXS3JScmhqIO9zM0vR1lSIftsgl42SddMug7jx5JuFJOkN7QGDptgiMbrr97J%2Fe9%2B4%2BGRzJB7o%2FyfPiqyzM%2FD5S&X-Amz-Signature=4103f0899fcaef93145d78a5374a8d08e1bd4a7fa8164f8c2cdfac087c17be79&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

[image](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/93b8245e-4e42-4deb-a7c4-1792d0852120/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RECLAZE6%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T225708Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDb8Zu31z7cn7DKH960r846mO4YlsK0CoTEZ0gOi8O5MwIgRwHnS13MEJuNh0V4NRRk6LzSkYQq5ZSLS%2BaC0Saa7xIqiAQIxv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDP%2FHmNPeZppgNIVeCircA2HTe6v89iPiDiDlAdBARohP5Tg%2BHah9NTAxaX7pVSTOk8jgEYUIwYGVMtHkns80yjApv0esFAEMUWHPZA7jTkd05laZLiuoK3SWgnKksyy2C479DrzGf80UQOL%2BTCk0xnCBiuxOvrVj2JccO3r3Al7RZ8ZCfKAqC0VQcUGi1NMzw8QTmh7t6zbY8gTLn3UkiTKTjIWFDYLAiGMxUw%2FO9av9%2BtSfyGwuXGo8MQemz5rdZ4xSOiFAd%2FNebH2S2KGSV%2F6q7z7PJrLP9YoPe17ehmQeTC%2B%2FmnFMszSQdkLa%2Fxqb8XG3PENp5BRmJGAdf%2BTDN9TNu%2F5Thae9YallUBcAoIe541EQEzTBLBYf2g3Dz0VlAMDO1w2%2BMnbP86P%2FwhKloeOuHV2mxVv9wsYxztj%2BcmPRdY%2BVk8Tw6jQQUxEQH4c0fY1WmPrTTzOoDCeJOK8%2Be0kCmVRSZO%2BblwiFCEMyE%2BN2MQmPnBK6lO5tdtFQX4ol2y3ZOzYCmPDACF44MsGuLzX1MI5Gx%2F2ayd%2FzDgKzXtfWcCgVmhGvRYiEMd9ey8m38EfWi%2BqkyPwlR39UO7kNe%2B1r83BvwutdXdJY6dCzdg2MiCRoQrb2LyoMxq%2FZNMHK1yHLd1XvG72NkOswMJa3%2F9IGOqUBCN7%2F1I8ssNuEZ6EbOsyK2MDW%2BeBQQsIHtSvx6pJVcWPrdeMU%2B9YgQqWDv%2Bl9f09zJ3S6IW28U7uCP7nqf4S3d1rBI3Yu0w3%2FjnN2cfhpUlyyYO07La7zlN5SMx6BAbl9mlJvYrXS3JScmhqIO9zM0vR1lSIftsgl42SddMug7jx5JuFJOkN7QGDptgiMbrr97J%2Fe9%2B4%2BGRzJB7o%2FyfPiqyzM%2FD5S&X-Amz-Signature=7441b3982c1ba3efbad1a3d7488cc2cc69ba6500b95c7b906115eb64a29fe3ea&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

[image](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/570f2ed2-76d6-42e3-8fae-a2c7c80581e4/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RECLAZE6%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T225708Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDb8Zu31z7cn7DKH960r846mO4YlsK0CoTEZ0gOi8O5MwIgRwHnS13MEJuNh0V4NRRk6LzSkYQq5ZSLS%2BaC0Saa7xIqiAQIxv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDP%2FHmNPeZppgNIVeCircA2HTe6v89iPiDiDlAdBARohP5Tg%2BHah9NTAxaX7pVSTOk8jgEYUIwYGVMtHkns80yjApv0esFAEMUWHPZA7jTkd05laZLiuoK3SWgnKksyy2C479DrzGf80UQOL%2BTCk0xnCBiuxOvrVj2JccO3r3Al7RZ8ZCfKAqC0VQcUGi1NMzw8QTmh7t6zbY8gTLn3UkiTKTjIWFDYLAiGMxUw%2FO9av9%2BtSfyGwuXGo8MQemz5rdZ4xSOiFAd%2FNebH2S2KGSV%2F6q7z7PJrLP9YoPe17ehmQeTC%2B%2FmnFMszSQdkLa%2Fxqb8XG3PENp5BRmJGAdf%2BTDN9TNu%2F5Thae9YallUBcAoIe541EQEzTBLBYf2g3Dz0VlAMDO1w2%2BMnbP86P%2FwhKloeOuHV2mxVv9wsYxztj%2BcmPRdY%2BVk8Tw6jQQUxEQH4c0fY1WmPrTTzOoDCeJOK8%2Be0kCmVRSZO%2BblwiFCEMyE%2BN2MQmPnBK6lO5tdtFQX4ol2y3ZOzYCmPDACF44MsGuLzX1MI5Gx%2F2ayd%2FzDgKzXtfWcCgVmhGvRYiEMd9ey8m38EfWi%2BqkyPwlR39UO7kNe%2B1r83BvwutdXdJY6dCzdg2MiCRoQrb2LyoMxq%2FZNMHK1yHLd1XvG72NkOswMJa3%2F9IGOqUBCN7%2F1I8ssNuEZ6EbOsyK2MDW%2BeBQQsIHtSvx6pJVcWPrdeMU%2B9YgQqWDv%2Bl9f09zJ3S6IW28U7uCP7nqf4S3d1rBI3Yu0w3%2FjnN2cfhpUlyyYO07La7zlN5SMx6BAbl9mlJvYrXS3JScmhqIO9zM0vR1lSIftsgl42SddMug7jx5JuFJOkN7QGDptgiMbrr97J%2Fe9%2B4%2BGRzJB7o%2FyfPiqyzM%2FD5S&X-Amz-Signature=b1fccde129ee001b9e396d7da5cc285c9b1c36a84f9ab3f08251df37999891d9&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

的。各位同学们，大家好，这里又到了本章唯一一处源码品读的环节了。这次我们来看哪部分的源码呢？那就是 config server 也就是咱的配置中心在资源文件加载的过程中是如何从 github 上面拉取文件的内容，非常简洁，咱依然采取 debug 的方式，把这个流程从头到尾走一遍。


好，同学们准备好的话跟我到 intelligi 我们开工编程是我快乐 996 是我的福报，又到了大家享受福报的时候了。那这次从哪里开始呢？就从当前这个闷方法的注释开始。好了，大家看这个注释里面有两个不同的 URL mapping 咱前面是不是通过 postman 向 config server 发送了一个请求，就可以获取到配置文件中的属性了。那我们今天来看一下这背后的动作都是怎么样完成的。首先要先找到入口对不对？好的开始是成功的一半。那咱这次从哪个类开始呢？

[image](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/4f88a7b3-f8bb-4b9f-8f6b-d8dcac615b7d/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RECLAZE6%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T225708Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDb8Zu31z7cn7DKH960r846mO4YlsK0CoTEZ0gOi8O5MwIgRwHnS13MEJuNh0V4NRRk6LzSkYQq5ZSLS%2BaC0Saa7xIqiAQIxv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDP%2FHmNPeZppgNIVeCircA2HTe6v89iPiDiDlAdBARohP5Tg%2BHah9NTAxaX7pVSTOk8jgEYUIwYGVMtHkns80yjApv0esFAEMUWHPZA7jTkd05laZLiuoK3SWgnKksyy2C479DrzGf80UQOL%2BTCk0xnCBiuxOvrVj2JccO3r3Al7RZ8ZCfKAqC0VQcUGi1NMzw8QTmh7t6zbY8gTLn3UkiTKTjIWFDYLAiGMxUw%2FO9av9%2BtSfyGwuXGo8MQemz5rdZ4xSOiFAd%2FNebH2S2KGSV%2F6q7z7PJrLP9YoPe17ehmQeTC%2B%2FmnFMszSQdkLa%2Fxqb8XG3PENp5BRmJGAdf%2BTDN9TNu%2F5Thae9YallUBcAoIe541EQEzTBLBYf2g3Dz0VlAMDO1w2%2BMnbP86P%2FwhKloeOuHV2mxVv9wsYxztj%2BcmPRdY%2BVk8Tw6jQQUxEQH4c0fY1WmPrTTzOoDCeJOK8%2Be0kCmVRSZO%2BblwiFCEMyE%2BN2MQmPnBK6lO5tdtFQX4ol2y3ZOzYCmPDACF44MsGuLzX1MI5Gx%2F2ayd%2FzDgKzXtfWcCgVmhGvRYiEMd9ey8m38EfWi%2BqkyPwlR39UO7kNe%2B1r83BvwutdXdJY6dCzdg2MiCRoQrb2LyoMxq%2FZNMHK1yHLd1XvG72NkOswMJa3%2F9IGOqUBCN7%2F1I8ssNuEZ6EbOsyK2MDW%2BeBQQsIHtSvx6pJVcWPrdeMU%2B9YgQqWDv%2Bl9f09zJ3S6IW28U7uCP7nqf4S3d1rBI3Yu0w3%2FjnN2cfhpUlyyYO07La7zlN5SMx6BAbl9mlJvYrXS3JScmhqIO9zM0vR1lSIftsgl42SddMug7jx5JuFJOkN7QGDptgiMbrr97J%2Fe9%2B4%2BGRzJB7o%2FyfPiqyzM%2FD5S&X-Amz-Signature=9e1eea76c43a28c9a5cf1208ac0bd45702f5ea9689e404bcf975c84c8d4d03af&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

老师这里就直接给出了这个类的名字，它叫 environment controller 那可以看到它其实就是一个普通的 controller 在这个 controller 里配置了很多很多的方法参数，其中每一个方法它都对应了一个 request mapping 用来匹配我们 postman 中发送的请求。比如说现在这里是一个正则表达式的通配符，它可以匹配很多请求。


那接下来我们看一看咱要使用的应该是哪一个方法呢？我们往下滑，直到这里，我们通过 name 杠 profile.json 通过调用这个方法开启 debug 的入口。好在开始之前咱要先把这个项目用 debug 模式给它启动起来，在启动的过程中我们先切换到 postman 里。 OK 这里我们构造了一个请求，它是发送到 local host 6 万，也就是 config server 这里后面跟着的是 config 杠 consumer 杠 prod.json 好，我们现在就要发送这个指令了，看后台的断点我们已经打好了一个断点，看它能不能接收到参数就在这里。 OK 发起请求。好，断点已经到达了。
那我们先来看一下它的入参。好了，它这里有几个关键的信息，分别是 name 和 profile 你看这里实际上它用的 path variable 就是从 HTTP 的访问路径中获取这两个属性。那它的 name 也就是 application name 是 config consumer profile 就是 prodok 那它这里实际上调用了一个方法是哪是下面的这个方法，因为我们在调用请求的时候是不是没有给出label ，那它因此默认就给了一个空的 label 实际上当你 label 给空的时候，咱就访问它的 master branch 这是默认的行为。 OK 那我们走下来，看它。


第一步， validate profile 它 validate 什么内容你看它这里只有一个 if 条件，你的 profile 中不能有短横杠。什么意思呢？就是说你整串 UR L 的最后一个属性它才是 profile 前面的属性都是 application 所以 application 可以有很多杠，但是 profile 这里只能是最后一个拼接单词。咱可以回顾一下，你看咱发送的 URL 里面前面是 config 杠 consumer 杠 product 所以 prod 是最后一个词组。不管你这个 profile 前面有多少个横杠，你就是杠上开花也没关系。但是它匹配的时候只会匹配最后一个横杠后面的部分 we profileok 咱再回到代码里面。这一关轻松通关，咱们又被拦住。


Ok. 到了下面， label 的这个 method 是什么意思呢？我们点进去看一下，那它这里先对 name 动手了。这个 name 如果不为空，并且它包含了下划线，大家看这是下划线，它会把你的这个正则匹配时匹配到的内容替换成一个斜杠。好动完 name 咱们再接着来动 label 那如果你的 label 不为空，它同样的要做这样一副操作，不过我们的 label 是不是为空的，所以这两关都没有，难倒我们。


OK 那到了这里，咱进入了一个 find one 的方法，这个 repostary 它的名字非常拗口，它叫 environment incorapter environment repostary 所以说看到它跟加密应该有那么点关系了，那我们直接。好，点进去我们可以看到它这里面用了一个 delegate 这里有一个代理的对象。其实这种 delegate 的模式在各个的开源系统中是非常非常常见的，大家在不同的开源组件中应该可以见到它的大规模应用。这个其实是咱天天说到的单一职责的一个代表。 OK 使用它可以对很多业务进行解耦。那咱看这个 delegate 类它身后藏着的是谁。 OK 你看这个 delegate 它里面包含了一个 environment repositories 这个就是实际上向 git 发起请求的 repostary 类了。 OK 那我们知道了接下来该往哪里走，那就直接进入 delegate 的 find one 方法。这里的第一步操作非常简单，它只是构造一个 environment 对象，传入了 application name 还有 profile 的名称以及 label 等等。


OK 到了第二个对象，咱这里可以看到这个对象是一个 list 什么含义呢？也就是说我们的 server 实际上不只可以从 git 上面拉取文件，它也可以同时配置其他的 reports rate 比如说你可以同时从 git 以及从数据库两个地方拉取配置文件。


咱在 demo 中简单起见，只配置了 git 的方式，同学们课后可以自己去尝试着再配置数据库拉取文件的方式。那在这一步大家就可以看到，如果你只配置了一个拉取方式，它接下来是走这个 if 条件。当然如果你配置了数据库以及 git 或者是本地文件系统等多种的 repostary 那它实际上是会进行一个 for 循环，对每个 repostary 调用它的 find one 方法，从各个地方去收集这些配置文件，然后共同作用。这里就有一个偶遇的支线任务，等待大家去探索一番。什么任务呢？如果我在数据库以及 git 文件中同时配置了同一个 name 的属性，那么究竟是哪一个生效呢？同学们可以去尝试着 debug 一番，寻找答案。咱这里由于只配置了一个 environment 所以当然是走到这个 if 条件里了。点到这里打一个断点，咱可别手一滑，直接错过了，精华都在这个不起眼的方法里。 Find one. 咱先看一下 environment reposry get 0，也就是 get 第一个节点，它 get 到的这个类叫什么名称？它的名称叫 multiple G git environment repository 所以说它是目前 config server 中用来与 git 交互的一个 repostary 我们在对类的命名当中有一个约定俗成的方式，就是对数据语言等等这一类的类我们通常使用 repostery 来命名，这也是开源项目中一种约定俗成的规则，也叫潜规则啦。


OK 在进到这个具体的类之前，我这里加一个小拓展知识，大家知道当前的这个类叫什么名字吗？我往上滚一下，让大家看一下它的名称。第一个单词是什么？是组合的意思，这里透露出一个什么理念我们写代码的时候其实倡导这样一种理念，叫组合，优于继承，也就是说尽可能的减少类的层次结构，尽可能少用继承。而代码经验比较丰富的同学可能能体会到这之间的差别。当你在超大规模的项目中，如果过多的使用了继承结构，那你可能就要发生类爆炸。我们在写代码的时候尽量的控制类的继承层次，就像咱们现在组织架构一样都倡导扁平化，那现在代码开发的规范也越来越偏向这个方向，尽可能用组合代替继承，使你的整个代码结构类的层次保持一个扁平化。所以时代在进步，编程的理念也在一直推陈出信。


好，我们接着回到主线剧情，那咱这里直接进入 find one 方法，点进去再走。好嘞，这就到了 git environment repulsory 这个类中。首先映入眼帘的是一个 for 循环，它循环谁呢？循环我们当前这个类中的 Repo 那因为咱这是第一次启动，第一次访问 URL 来拉取文件，所以这个 ripple 应该是个空。不出意外的话，果然它的 size 是0。 OK 那么这个循环也就进不去了，我们可以 YY 一下，假设进去了怎么办？假设进去了他会看你当前这个 rapper 是不是 match 上了你传入的 application profile 以及 label 如果 match 上了，走下面的逻辑。好，那我们这里就直接跳过 for 循环往下走一行。


OK 在这里我们进到 get repulsory 这个方法里面，看看它都做什么事儿。第一步是检查 repostery 的 URL 如果它不包含括号就直接返回。如果包含括号，这里要对它进行一些改造，怎么个改造法？咱是知道括号代表着什么，代表着属性，对不对？那说明你这个 repository 的 URL 里还有没有转译好的属性，那要把它的属性通通给它替换掉。


好，下面这些流程都是用来做替换属性操作的，我们先不去管它咱的 repostary 是不包含画括号的，都已经替换完毕了。好，那这里就直接 return 了 return 回来，它叫什么 candidate 那这个 candidate 怎么用呢？我们往下看。


第一个， if 条件，如果 label 没有传入，咱前面没有给定，所以它默认是空，那这里给它一个默认值。 label 在缺省情况下，它会给定一个默认值叫 master 也就是让咱去 gate 下的 master branch 拉取所有的属性文件。我们看看这个 label 的值果然是 masterok 那接下来这一步，如果 candidate 是当前的这个类，那我们就走进来调用父类的 find one 方法，咱看在它的父类的 find one 里面能搞出什么幺蛾子点进去。


好在这第一步里，我们要组建一个 native environment repostary delay 这里面有一个关键的方法叫 get environment 它是做什么的呢？它是获取到咱们在外面配置文件中给定的各种属性。比如说它这里面的有一个叫 property sauces 的属性，这里面有 13 个属性之多。那这 13 个属性都是咱在外面配置好的 property 比方说第一个属性就是 server port 那它是指定了 6 万。那在这 13 个属性中还有一些比较关键的属性咱在这里面会用到的，让我们来找一下，应该是在这里好找到你了，看这里咱定义了 spring cloud config 的属性，那这里不就是咱们配置的 git 地址对不对 OK 这些属性在稍后都会有用到的。那接下来我们把这个 native environment repository 给组建好以后。


第二步， get location 这个 location 里面有料了，咱进去求一眼。好，这第一步是一个 for 循环，咱前面说的我们的 Repo 因为是第一次加载，对这个相当于缓存的 list 里面实际上是没有任何对象的。那这个 for 循环就跳过了。大家看现在这套代码流程的结构是不是感到似曾相识。我们讲了 get a location 这个方法和前面咱看的 find one 方法，实际上在执行流程上它是一个模板，大同小异。 OK 这里我们就直接往下走，走到这个 super 方法的 get location 里面点进去。 OK 这里咱就开始有料了 label 我们已经给了一个默认值，是 master 往下走一步。在 refresh 方法里，我们要进去看一眼，看这名字起的好像是掀不起什么大风浪。但是咱进去看看好像不是。这个名字起的就是 git 实际上是什么意思呢？咱既然是从远程拉取 git 文件，那总要把这个文件存在某个地方。对不对？它其实是在本地的文件系统中也保存了一份 git 使用 git 命令从远端 pool 文件的。好，这个 create git client 里面，咱点进去就可以看到这里有一个 file 对象，这个对象就是 git 的 lock 我们平时使用 git 的时候，应该也经常常见 git log 这样的一个文件。好，那我们看看这个 working directory 指向哪里，就是它存放本地 git 目录的地方。你看实际上它是存放在 var 下面的 focus 文件夹里，这后面是一串临时的目录。好我们不去管它，让它在这个目录下面放飞自我。


这里先判断，如果当前的 lock 存在，那就是说有其他的线程可能正在访问这一个对象或者也在同步的拉取文件。如果它存在，那就把这个锁直接给它 delete 简单暴力对不对？我就喜欢这种风格。如果这个锁不存在，那么我们这里判断你是否存在 git 文件。 OK 如果你存在，那么就是 open git repository 如果不存在怎么办？ copy reposry copy reposary 怎么做呢？第一步，扫清一切障碍，delete看它怎么个。 delete 法很简单，它把当前 base 的 directory 下面如果你存在任何文件，那么我给你个 for 循环，把它循环的 delete 掉，所以它相当于从头到尾创建一个全新的目录。


okok 把当前目录的文件全部删除以后，这里重新创建一个 base directory 的文件夹。在接下来一步用 assert 验证一下你这个文件夹是不是创建好了，如果没创建好直接中断流程。在这一步它要验证我们配置的 get 地址了，这个 get UR I 实际上就是咱在 problems 文件中配置的 get 目录，它可以看到指向我的这个 config repook 它这里要判断你这个 git 文件地址是不是以文件名开头的，也就是 file 这个属性开头的，咱是怎么样，咱是以 htd B 开头的。对不对？所以说它就到了下面一步。


cologne to base directory 也就是这一步要进行一个克隆操作喽。所以你看平淡无奇的 refresh 方法后面大有玄机。我们看这些开源代码的时候，经常一不小心就错过了是吗？但是好像又不知道这件事在哪里发生的。所以第一次看代码，每一个流程都要把它走进去看一下。
OK 那这一步它实际上是构建一个克隆的命令。大家如果在自己的项目中需要在 Java 中操作 get 也可以用这种方式。它使用的是 eclipse 下面的 git 组件，可以看到这个包名是 eclipse 下面的 J gate 也是非常常用的一个组件。 OK 那我们这里就不点进去看了，它实际上是克隆一个 command 对象。


Command. 这也是一个非常非常经典的设计模式。就像前面我多次提到过设计模式是怎么样，是一个内功。尤其我们在互联网这种复杂的场景中，经常需要定义一些领域模型。那这领域之间它通过组合模式跟哪些边界进行交互？比方说你给这个商品进行评分，那这个评分可能来自于评论，可能来自于打分各种边界。那为了划分你这个边界之间的界限，通常我们要借助大量的设计模式，从代码层面把你各个组件之间的边界给它划分清楚。所以大家在设计模式上不能说只看那是没用的，真的要在代码里面把它给应用进来最有效的方式。


咱就是看这些开源软件的代码。你在开源软件中的代码遍地都是，设计模式遍地都是宝 OK 那咱接着回过来。那这第二步是对前面创建的 command 对象进行一些装配，装配什么呢？一个 timeout 你要设置好多少秒之内没有返回，就中断。其实咱在本地网络访问 github 服务器，这时候经常会发现网络反应非常非常慢，这里建议带大家怎么样呢？搭建一个代理服务器就好，这样的话访问会非常快。那其实有的时候并不需要买代理服务器，像谷歌它的云服务器都会提供一年的免费使用。你可以在谷歌上面自己搭建一个代理服务器不花钱的，这也是锻炼自己动手能力的方式。非常简单，搭建一个代理服务器没有这么复杂的。


OK 那接下来这些步骤，比方说这个是创建一些 callback callback 的钩子给它放好，剩下的 credential 你这里要用到，咱访问 git 的时候没有设置任何访问权限或者是用户名密码等等都没有配置。所以这里应该获得的是一个空。


好，那返回到这一步，就真正的发起 get 调用了，我们就先不 debug 进去了，直接点进去看一下就好了。 OK 这里的核心流程在哪呢？这个 try 可以直接把它放过，它只是构建一些 URI 然后做一些 directory 的验证。那么它真正的流程下面，在这个操作里面。


第一步先要 fetch 一把，咱对 gate 都非常熟悉了，fetchpull push 之类的。 OK 那这个 fetch 里面构建了整个 remote config 对象，那么设置一些访问头，然后构建一个 fetch comment 并且发起最终的 call 好，我们假定这一个请求完成了，然后它会返回回来。这里对每种异常情况都有自己的处理，处理的粒度还是蛮细的。 OK 那到了这后面还有一个 check out 操作，就是说如果你没有 check out 这个分支，那这边会对这个分支进行 check out 当这一切都准备妥当以后，返回一个 get 对象。 OK 那我们返回回来，走到最外面的断点处。这个 clone 操作我直接把断点放开了，就不点进去一步一步看了，直接让它跳转到上一级。好，我现在放开断点。 OK 那这里又回到了 refresh 方法，在上一步中咱已经把这个 get 克隆下来了。那这一步我们就要判断是不是该拉取 get 文件了，也就是 pull 操作，这个 should pull 咱们进去看一眼。


这里会根据 refresh rate 还有你上一次刷新的时间，并且结合系统时间做一个比较。那如果我们给出了 refresh rate ，并且它大于1，说明它是有一个自动刷新的机制对不对？然后当前的系统实践减去上一次也就是 last refresh 的时间，如果这个值小于 refresh rate 乘以1000，也就是说 refresh rate 的单位是秒。那如果你这里配置了60，也就是说 60 秒钟刷新一次，我们继续往下走。这一步获取 git 的 status 接下来的判断是 is working trickling 同时获取到它最初的 URL 那这个最初的 UR L 实际上就是 htdp 我们配置上的 git 路径。到了这一步，咱们在前面配置的强制拉取参数就起作用了。


force pull 强制拉取是什么意思？就是说如果你的 working tree 当前的工作分支上它不是 clean 状态，那么你就会制作一次强制的拉取动作。那咱这里没有进到这个条件往下走。那这里如果 working tree 是 clean 的，并且你的 original URL 咱已经配置好了不为空，那么它就会做一次拉取。所以说 should pull 这里应该是 true 接下来把这个返回回来之后这里就开始进入了正儿八经的拉取。


我们可以看它主要分为三个步骤，第一步 fetch 第二步 check out 还有 merge 那这 fetch check out 和 merge 三步走咱就不跟进去看了。这里面大同小异，也没有什么有趣的灵魂，我们就直接跳过好了。Ok. check out emerge 咱一次跳过同学们对 git 操作如果还是使用命令行的话，我这里可以跟大家推荐一个提高生产率的小工具，它的名称叫 SaaS tree 是一款非常方便的 git 的图形化操作界面，保准你用了之后爱不释手。不要998，今天你免费全拿走，只用注册一个账号这个是完全不收费的。


Ok.那么到了最后一步 return 什么呢？咱提交的时候都知道有一个 version 对不对？就是一串非常非常长的数字。那它这里把当前 Repo branch 下面的这个 head 的节点最后的一次 head 提交，把它的 name 给拿到了。返回到这一层，这个 refresh 就结束了。你看这样一个不起眼的refresh ，所有的操作全都在这后面，这就像一个桃花源一样，山有小孔。你点进去，仿佛若有光，进去以后别有洞天。 OK 那咱后面的流程这里就直接返回了，再返回一层。


到了最外面 find one 方法，拿到 location 以后，咱这个对代理对象就有交代了，把这个 location 传回到代理对象当中。那这下一步，怎么又有一个 find one ，这个 find one 并不是指 git 的操作。不信，我们点进去，稍微瞄那么几眼，大家看到这眼花缭乱的代码，不要被迷惑了，咱看这个主线就在这里。


好。 context 构建的上下文，这可是这个上下文中设置的启动参数，咱看看都有谁。咱前面辛辛苦苦跑完的 git 方法在这里有用武之地了，看到没有？ 0123 最后一个属性是什么？它是 spring.config in location 它是指定了某个 config 文件的地址，而后面它跟着的是什么？就是我们从 github 上拉取到的远程文件存放在本地的一份拷贝，它会使用这个文件作为初始化的参数来构造整个上下文。看到这同学们是不是把整个链路都给拎起来了？好，我们点击下一步。 OK 整个上下文已经构造完成了，剩下的流程我们就直接返回。


好了，接下来的几步，没有什么核心逻辑，咱也一并把它返回掉，返回直到最外层。好，那我们的 environment 对象在这里已经构建完毕了。那将 Repo 中获取到的这些 version 啊 property sources 啊统统加到 ENV 对象中，最终返回回去。好，那到这里多提一句，大家可以看到这有一个 environment encrypter 它要对 environment 中的属性做一个什么解密操作， decrypt 操作，那它是我们后面章节中将要学习到的知识。所以这里咱就把它略过了，等后面同学们学了文件属性的加密和解密，再回过来，通过 debug 的方式详细了解里面的步骤。好，咱这里就把它走到最后一步直接返回。


OK 终于到了最外层的方法，我们成功构造的这个 environment 对象，从这个对象中可以获取到所有需要的 properties 把它转成了一个 map 然后最终返回给了前端的 UI 页面。好，看到这里，整个流程就结束了。那我在这里跟大家简单的总结一下，我们的 config server 通过对外暴露出的 environment controller 接口接收访问请求，然后通过 eclipse 的 jgate 组件向远程的 github 目录发起一系列的 git 操作，将远程的文件拉取到本地。在这之后将本地的 git 文件作为一个上下文的参数加入到 context 当中，最终将所有获取到的 properties 返回给调用方。


那在这个过程中，咱还看到了一些设计模式的应用，比如 delegate 模式，比如 command 模式，并且提到了一个组合大于继承的编程理念。 OK 那到这里我们就可以收工了。下一节当中我将跟大家介绍如何配置一个动态参数拉取的过程。也就是说我们可以在 github 上动态的修改自己的参数，然后在我们程序的运行期改变调用方的业务参数。 OK 同学们，那我们下一节再见。



