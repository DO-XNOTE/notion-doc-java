---
title: 1-11 基于Dubbo-Admin的服务治理-2
---

# 1-11 基于Dubbo-Admin的服务治理-2

[image](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/429d0ee7-47b1-45e1-9f53-868cb7e8c213/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466R7D3B5F4%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T225900Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCICJUnuCr0FE49MWpof1Q9B1wQlHxrhVDNk%2BcAXwQGRBkAiEA2bC3qMpRCFCjeJmZEXLnKDRgEdjrHfTDQRbeuZS%2B5pAqiAQIxv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDMQaa8WLkvYOXx3mtyrcA%2FxpYTTJ27tpYbfrWMkSQAhj4o5GIn9HFCchTbdhtmHDnbjDb%2BBoz4lqZaop3TFeDNnwbZ6K8Ti2JL0Pw08zndcj4c0Ut2ouX%2FAF1q%2BXZwBnLTU5g08%2B7iAjMq%2FMiE9Kj33L4z6kMm9XXxMakrgj1%2BBc3aDAR4z4HNrfmlYPLPkBERQMSPuHNelGWrbyWOEAl9EZXq5Nbxuf301DXTDR0db2IAiTOcDqBcN3Ake3QMwC3A9Q5h46CGTU8HugrUJZRbKgc%2BjG68j%2FFkuPuFVMUbiE4d2MbCw%2F4hVsZRY7nsdw%2B4CT4GKUBkAGbOPNDm4KNO2EGOOB%2B4EDjYHMRBgs3SAEojVgOhXY4pLvPyyWdiIfyo6tM17VZNE2NtCd0xF4mjYLxIsrriitDMIWPslF2z0vNOiNp58m4ZtepxKO5tIVzOJ%2FKSGM9yXGLzROK1RPxLmQwaMzLimgrSW5Dhvm1rmIYjo083awrApjsi3ULucxs6I1PaAotqUO54R4xBxbIDJ81LTC6Gbr3tNtgPzEpoPB%2BuBZlgNrioo0u0%2B8kiM6cFF1RFbHYnY0XZMjVg2uagYgcv61R%2BcaQHISoA867UdgECN4WZKrD4ETGGTb5el%2FT0nVZ%2BJxkcLlH66pMI66%2F9IGOqUBiBAHFmGyCjjTuXzeSfoBI0f01bsDhinIA7EMCnW7v0Iiyfk0Ea09nirj%2FQiZoF0FnXPkGH5YyW384cKbcr83b0JLIkcuF2OUjy5c7Skjj5yhtKzV%2BrDTgWAl%2FvZOZM%2BZYGNQvtVPvGqau6thVtvMf3hazz1fbNmCqFsTqBtBNRKxiSTxaUm53NvmXV4ZY4HxQ95xoTrlep9KS1xhdGspd8vREV%2F0&X-Amz-Signature=ba97cdb70eadbeed889a491ea010480df9895be629e33894ca05ec21b651840a&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

[image](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/01e5e1f6-a22b-437c-91c5-d77d6916498e/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466R7D3B5F4%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T225900Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCICJUnuCr0FE49MWpof1Q9B1wQlHxrhVDNk%2BcAXwQGRBkAiEA2bC3qMpRCFCjeJmZEXLnKDRgEdjrHfTDQRbeuZS%2B5pAqiAQIxv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDMQaa8WLkvYOXx3mtyrcA%2FxpYTTJ27tpYbfrWMkSQAhj4o5GIn9HFCchTbdhtmHDnbjDb%2BBoz4lqZaop3TFeDNnwbZ6K8Ti2JL0Pw08zndcj4c0Ut2ouX%2FAF1q%2BXZwBnLTU5g08%2B7iAjMq%2FMiE9Kj33L4z6kMm9XXxMakrgj1%2BBc3aDAR4z4HNrfmlYPLPkBERQMSPuHNelGWrbyWOEAl9EZXq5Nbxuf301DXTDR0db2IAiTOcDqBcN3Ake3QMwC3A9Q5h46CGTU8HugrUJZRbKgc%2BjG68j%2FFkuPuFVMUbiE4d2MbCw%2F4hVsZRY7nsdw%2B4CT4GKUBkAGbOPNDm4KNO2EGOOB%2B4EDjYHMRBgs3SAEojVgOhXY4pLvPyyWdiIfyo6tM17VZNE2NtCd0xF4mjYLxIsrriitDMIWPslF2z0vNOiNp58m4ZtepxKO5tIVzOJ%2FKSGM9yXGLzROK1RPxLmQwaMzLimgrSW5Dhvm1rmIYjo083awrApjsi3ULucxs6I1PaAotqUO54R4xBxbIDJ81LTC6Gbr3tNtgPzEpoPB%2BuBZlgNrioo0u0%2B8kiM6cFF1RFbHYnY0XZMjVg2uagYgcv61R%2BcaQHISoA867UdgECN4WZKrD4ETGGTb5el%2FT0nVZ%2BJxkcLlH66pMI66%2F9IGOqUBiBAHFmGyCjjTuXzeSfoBI0f01bsDhinIA7EMCnW7v0Iiyfk0Ea09nirj%2FQiZoF0FnXPkGH5YyW384cKbcr83b0JLIkcuF2OUjy5c7Skjj5yhtKzV%2BrDTgWAl%2FvZOZM%2BZYGNQvtVPvGqau6thVtvMf3hazz1fbNmCqFsTqBtBNRKxiSTxaUm53NvmXV4ZY4HxQ95xoTrlep9KS1xhdGspd8vREV%2F0&X-Amz-Signature=e82c988c3863aa8cff6f5b8c9dcd47e3e49b34630140ac84b490300a7a9f9e6a&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

hello 慕课网的各位同学们，大家好，咱这里进入了 double admin 的服务治理的下半场。咱这一节的主要内容有这么几点，首先我们在启动项目之前要去修改一个 zookeeper 端口，因为 zookeeper 它里面的一个管理端口和 double admin 的程序有冲突，所以这里要把它替换成另外一个端口。接下来咱来稍微了解一下 double admin 中的配置，尤其是其中的元数据配置。看一看它和咱前面创建的 double consumer double client 里面的元数据配置有什么共同之处。


最后一个部分，咱就要把整个应用给它启动起来，包含前端和后端，然后在页面上去把玩我们的 double 服务。 OK 同学们，早安，intellig这里我们一行人来到了 zookeeper 的安装目录，咱先进入 config 这个文件夹，然后找到哪一个文件呢？就是 zoo.cfg 它的配置文件。我们把它打开，然后这里页面我放大一些。同学们可曾知道，在最新版本的鲁 keeper 当中，它有一个内置的管理小程序是用 jetty 启动的。 jetty 它这里也占用了 8080 端口。所以咱得把其中一个组件的端口改成一个没人使用的端口。那这里咱就挑选组 keeper 了。在配置文件中，咱要在底部加入这么一行，我们把页面放大。同学们看这一行 admin.server port 等于63010，这个 63010 同学们可以随意发挥，只要是一个没有人用过的端口就好。其实你改了这个端口对 zookeeper 的应用没有什么影响的，大家可以放心大胆的去改就好。不过要记得改完之后，把 zookeeper 重启一下，使它的改动生效。


Ok. 那 zkeeper 改完之后，咱可以回到 intellij 里面来瞄一眼 double admin 的配置文件。在 double admin 的项目结构中，它的配置文件是放到 double admin server 这个子项目当中。我们打开 resources 下面的 application.properties 那在这里面大家可以看到其中有一个 meta data report 那这个就是它的元数据中心。我们知道在 2.7 以前，这个 double 还处于一个大一统的状态。什么意思啊？只有一个注册中心包揽所有活。然后到了 2.7 以后就变成了三足鼎立。


咱既有注册中心，也有配置中心，还有 metadata 所以咱 double the mean 如果也是使用的 2.7 以上的 double 版本，那我这里建议大家在自己的 double 项目当中使用和 double admin 配套的版本。否则当大家启动 double admin 的时候，有可能是获取不到源数据的，这样也就不能去选择接口，发起调用测试等等了。


OK 那这里是 double admin 的配置，我们再稍微回顾一下咱在自己的 double 项目中是怎么来配置的。我们这同样也把注册中心和它的元数据中心给分离了开来。比如说这里这个 registry 就是注册中心下面的信息。那下面的 meta data report 这个地址，它和咱的 double admin 服务中配置的元数据中心地址是一模一样的，这俩应用都到同一个地方去拿取服务的元数据信息。所以大家如果要接入 double admin ，一定要在自己的 double 项目中，把这个节点添加上去 metadata report 而且必须让它和 double admin 中的配置是对应起来的。那咱接下来看完了配置以后，我们可以把整个项目给它启动起来了。在启动这个 double admin 之前，我们先把自己的 double client 和 double consumer 启动起来，因为咱要通过界面来管理这两个服务，自然要把这两个目标服务先让它跑起来。好，我们这里已经启动起了 double client 接下来到 double consumer 里面，把这个应用也给启动起来。


好，我们走起 consumer 然后这两个项目启动起来以后，我们来到 double admin 先把这个 double admin 的 admin survey 就是后端应用给它尝试跑起来。这个后端应用的启动方式也是一个标准的 spring boot 的启动方式，直接抛起闷方法就可以了。那我们这里把它跑起来，等这个后台项目跑起来以后，咱就把它的前台项目 UI 项目通过 npm 命令也给它跑起来。那咱让这个后台项目先在这跑着，先不去管它，我们切换到前台项目使用 npm 命令来对它来一发，让它跑起来。 npm run 后面加个 devok 走，你他这前台项目启动起来是比较慢的，它需要加载很多的毛九，稍等半炷香的时间。


等这个前台项目加载完了以后，我们这里就可以看到它启动成功的提示叫 your applications running here 在哪里呢？后面跟了一个端口， localhost 8081，我们把它复制一下。然后转战浏览器，我们打开一个新的 tab 把这个 URL 给 copy 下来。这里就是 double admin 的管理界面了。其实 double 界面里的功能和 hsf 的后台管理界面有那么些相似，毕竟 double 和 hsf 都是同一个团队开发的，我们挑几个功能给大家演示一下。


这里有个服务查询对不对？咱点击一下，你看到服务查询里面，这里的查询结果就是它从源数据中心中可以找到的所有服务了，这里是它的服务名，我们可以看到它是类的一个包名加类名，也就是类的完整路径。那么后面有它的 application name 就是 double 杠 client 这里有几个操作，比如说这个绿色的标签叫详情，我们点击看一下它有什么料。
这里面大家看到它有服务者和消费者两个 tab 那从这里咱就可以获得这个目标服务，它的服务提供者的 IP 地址端口和它的权重都有哪些，以及消费这个接口的消费者都有哪些。那这两个 tab 之内的内容其实是不同的，你看到提供者也就是它的生产者，这里会有很多的配置，你可以配置接口的超时时间，还有获得权重权重是负载均衡的时候会有用到的。那再往下这个源数据是什么意思？元数据就是你接口的特征量，比如你的方法名是什么？你方法中每个的参数列表还有它的返回值，那这几样组成了方法的签名。


OK 那除了服务查询以外，实际上咱这里还有一个更常用的功能，项目开发的时候经常需要用到这个功能，在预发环境甚至在生产环境上做接口的直接调用测试。因为 RPC 接口毕竟不像 HTTP 接口调用起来这么方便，直接通过浏览器 postman 就可以发起调用了。那他这里没有这么简单，他需要借助这个测试功能，我们点击一下，然后就跳转到了服务测试的页面。在这个页面中，咱可以选择当前服务下的各个方法中的一个。比如说咱这个服务下只有 publish 方法，也就他可以选了我们点击旁边的测试按钮，这里需要大家怎么样拼装出一个访问信息，比如说它的接口接收的参数是什么？是一个 product 的对象对不对？那咱点击这个 00 是什么意思啊？它接口中第一个参数，咱点击 0 看到这个下面有一个 name name 就是 product 的名称。


还有一个 price price 是 big decimal 的类型，那咱的 double admin 探知到了它为 big decimal 的数据类型，所以它这里把 big decimal 中可以配置的属性都给我们列出来了，看着就神反，特别麻烦。


如果你不想拼这种很复杂的参数，怎么办？还有一种方式，咱就是拼成一个 Jason 串，在这个里有一个下拉框，我们把它从 tree 选成 code 实际上即便你借助这种 JSON 形式的字符串，像我以前在集团里面使用 hs F 的经验告诉我，如果你是非常复杂的类型，那你拼起来是非常痛苦的。尤其是当你的方法接受一个 map 作为参数，哇那个拼起来就特别特别的费劲。如果有了接口，它接收的参数更变态是 map 中又嵌套一个map ，那你就基本上不用想通过这种方式拼出参数了，这个反序列化过程能让人抓狂掉。
那咱这里就简单的测试一下。那我们这里在调用的时候，把这个 price 给它设置成 none 就好了，把它设置成一个 none 类型。那么这里咱可以直接去发起这个调用了，给它的名字随便填一个名称叫 test 好了。好，咱在旁边找到这个执行按钮，眼睛盯着这里看，结果里面会出什么东西走。


你好，大家看到这里有一个成功，那结果集里面会给咱返回三个信息，一个是当前对象的 price 和 name 还有这个对象的 class 的类型。在预发或者线上测试接口，我们通常都要借助于这种方式来发起 RPC 接口的调用。 OK 除了这几个方法以外，咱还可以去看一下统计。我在使用以前老的 double admin 版本的时候，其实还没有见到统计，那它这里应该是后面加进来的。那从这个界面，可以获取到你的服务提供者、消费者的性能数据，比如说 response time rt 还有 QPS 并且还有它的成功率。除了这些以外，它的统计结果还可以细化到每个不同的方法。


OK 那除了这个功能以外，咱看到下面有个配置管理，那配置管理对应的是谁？就是配置项远程的 config 咱这里可以从 skip 中拿到当前的 global 配置。甚至咱可以创建一个新的配置。比如说 global 是全局配置，如果不配置global ，咱可以给每个特殊的应用自己当前的应用来创建配置项。 OK 除了这些功能以外，大家可能关注的是这一项。咱们本节的内容叫服务治理，那它专治什么呢？专治各种不服。你看这里面工具可多了，咱要不从下往上随便看一看。


这里均衡在负载均衡里，咱可以按照服务名或者按照应用的名称来搜索负载均衡的规则。比方说我这里看一看咱创建的 double client 是不是可以提示出来。好，提示出来了，我们搜索一下。看到这里其实是没有任何结果的。如果你想给一个特殊的方法指定负载均衡。那这里你只要创建一条负载均衡的规则就可以了。这里指定好用户名方法，然后选定一个策略。所以这种配置方式是不是看起来要比 ribbon 灵活也方便的很多？ OK 除了配置负载均衡以外，我们还可以调整接口的权重。那如果咱这里选择按服务名搜索，咱的服务名应该是 iw 跳出来了，这里搜索一下应该没有结果返回过来。


那如果咱想给服务名指定权重，怎么办呢？同样的也是创建一条新的规则。那这里默认选中给的是100，我们可以把它调大调小，根据自己的需要。 OK 那我们再随便看一看其他的几个标签，这些标签实际上内部实现看起来是千篇一律，不信你看，页面都长的是同一个样子，我们点击动态配置也是一样的形式。咱可以搜索一个服务名或者应用名，然后为他创建一个配置项。 OK 咱再去看一下其他的几个功能，黑白名单，这里大家应该都很熟悉了，设置黑名单白名单。那我这里跟大家介绍一下这个条件路由，这个条件路由功能可有那么点强大。比方说咱要给一个服务创建路由规则，那点击创建按钮，这里有一个弹窗，同学们在这个弹窗里面的 condition 咱可以加很多复杂的语句。所以你从这个角度来看，这个 double admin 界面，它所提供的服务治理功能俨然把咱们后台的这个 double 符变成了一个武器库，什么功能都可以往上加，甚至这个路由功能看起来都可以构建一个小型网关了。


那除了条件路由，这里还有个标签路由。标签路由实际上理解起来很简单，根据不同的标签值，然后把它路由到不同的服务器地址上。 OK 同学们到这里，咱整个 double admin 章节的上下半场就全部结束了，我来带大家回顾一下过去两节课程的大概内容。


咱首先准备了 double admin 的安装环境，包括修改组 gateway 的端口，安装 npm 命令，最后顺利的把 double admin 的前后端应用启动起来了。然后咱通过 double admin 的页面，可以轻松的查询一个服务，它的元数据，所有的方法及它消费者服务者的机器列表。我们还可以通过这里面的服务测试功能，轻松的发起一个服务测试接口调用。并且咱实地走访了服务治理这个标签下的几个功能点。


那大家如果在自己的项目中也应用了 double 组件的话，非常推荐大家使用 double admin 来管理自己的 double 服务。那到这里，本节内容就结束了。那接下来的一个小节，那是 double 最后一个视频章节。在下一个小节里，咱将去了解 double 它底层的协议解析过程。 OK 同学们，那我们下一小节再见。

