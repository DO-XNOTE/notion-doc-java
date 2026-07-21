---
title: 3-27 【技术改造】电商系统集成Eureka - 商品中心-3 
---

# 3-27 【技术改造】电商系统集成Eureka - 商品中心-3 

[image](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/8a68ae1e-8e0f-48c9-9da3-347635a204c1/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WWR3FEYE%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T225554Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIEmhZmQcjgkPXDwQiF3aXNANzOqF6%2FEbUxfKNdGSdSSSAiEA2lIGdpCF%2Fm0%2BHoz1V0dmAqaVDdykSlJTWfPUo2Q5a5EqiAQIxv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDDNXgh5RwwFGA54JsCrcA7IeBBASpYyvbHyYZ%2BUmrcPOONdA34hW9nVBi6tfri4DbStetVKPVQ%2FixzYOOwOzzOL4FFe0b2PVC%2BeJ3lj5ybMhOh1T4JjC5D0k9RNnichPIkxvZrV6gbvq8rxL8zy49JXAKvk%2FhAyqH7aExn68qGOBoQUx7cq73lxqrpAP9vu6YxgqJ4uOXZhJHnOFAC%2FAuc7vzvXU4zPXKeU45%2BDDX478n7EQhxZkCn7Ly%2BC78SsvhHvd1NgCnNr4ezWvFs58E9huTCEFEuA6tFFxLhBJJRoUb6KgzFpH2PdxTQ0caj%2B%2B9rRW3T0zJ2L28vkQfIqzf1fyi6Wq0eZPAgZPXpEtP4LPu8z01Plm3SAnUQLVkVYMDOydsBuE0VYn11HfWfVIIMP6bBdbaUkVYWWOMW4UP2YD3WlIArAKtFoR2d%2F66z5mTpYkhPlqxUkvc%2BTWXpAetEDGpch7SapXuswm1AHyO%2FoX3KjvAhcWaMwgI9g06vl7Be2JDJ%2BsmdgTXRUeoJLNhaG%2Bk%2F7DZ20fFiwhcOk4pVC7O6PynNjKkjkLr06XFwsiXbSMXGKb0Rq1i2I5ZeSzromUaLdallwnNqSyJLEzonTmrLceJuTyQmstfsPg8vn5yq75mLPDxkUr0wjkMIW3%2F9IGOqUB1sxAA7zixSbzZt7IUP0ldF2%2FMlmZrj2DOi%2BOISUg8NDCK4BeNT22LIHCQIroVvmT9id6ItEGAIWNehKocAsCaDmS2mQwJz%2FqREba4ZsVDGbJB9bUf%2FYtqTrS2nknOns%2BAedZAuAjQXjTvVH041LjY2Z1SYwWZVn2V%2BiK4i1VybXHCfLTo%2FVnwCJSCm8NHUosQ1tcoKXuSB0NzPRSLnVVdQv2pc7g&X-Amz-Signature=40efd4133e5f914ab07ca93ea7c1cc4696cc0ef8b74490b1f7cfa4da4c666234&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

在 API 层引入了一个 item comments 的 service 那同样的，这里也创建一个新的 item comments service。 Im pl implementation. 它继承自谁呢？我这里把小桌板先收起来，它继承自咱的 base service 这还没完，然后还要再多余的实现一个 implements 实现谁 item common service 这个接口，我们把没有实现的方法都给它列出来。 OK 那同样这里也有一部必须的操作，把它声明成 rest controller 好，那接下来我们就要开始写方法的内容了。其中第一个 query my comments 这里可以从其他地方 copy 过来，我们切换到 foodie DEV 找到 foodie DEV 的 my comments service 这个方法当中，把谁 copy 过来呢？把下面这几行 query my comments 这里同样的逻辑给它 copy 过来。好在这里一放。 OK 那这里还少了一个类。 Item comments mapper. 那咱在前面把它给声明上，就可以说明一个 private 的变量，把它给拿过来，首字母改成大写好勒引入进来，auto wire 的大帽子扣上。


那第一个方法已经完工了。那同学们如果直接继承自这个service ，你在自动引入的过程中它会把什么？把你这些参数通通都给你加过来。也就是说咱在方法入参上面声明的 request para 都会被一同的带过来。那咱接下来给这个方法添加一个 transaction 和前面的代码保持一致。


OK 那这后面的一个方法 save comments 这里调用哪个方法呢？调用 item comments mapper 是调用它的一个类，调用它这个 save comments 方法把入参传进去就可以了。这个方法没有什么特殊逻辑，只是让订单领域发起一个远程调用。 OK 那这里还有没有漏下的没有了。


好，我们打开小桌板洒 item service 里面的这两个类也定义完成了。最后咱还差着临门一脚就可以把商品中心启动起来了。好，我们创建一个 module 给这个猫就起名叫福迪杠 item 杠 web 它是放谁的呢？ I 放 controller 供 web 页面调用的，我们把它依然放到 domain item 这个文件夹下面，点击 finish 321 走。那它的 pom 也要引入几个自己人，这几个自己人，我就从其他地方把它 copy 过来，把这个模板 copy 到 item 外部当中。但是要把这个 artifact 改一下，它这里引入的首先要引入 item 杠 service 这是一个。


其次还要引入谁，因为它是一个 web 组件，这里 web 组件有一些公共的需要，用到的内容是放到了哪里呢？放到了咱前面创建的 foodie cloud web component 当中。 OK 那除了这两个以外，咱还要引入谁呢？当然是服务发现的基础组件了。那就是尤瑞卡。好，我们这里把它打上 org spring from a cloud 它的 artifact 把它 copy 过来是 eureka clientok 那除此以外，我还想让他可以在外面通过这样命令的方式来启动。


那么我就要指定他的 manifest 中的闷方法主类从哪里呢？从 registry center 这里把 build 节点给 copy 过来，就是你了把它 copy 到 item web 当中。但是这个闷方法我先把它删除掉，先留空，等后面创建好了之后再回来把它填上来。那接下来我们去做代码移植，打开 SRC 下面的 Java 在这里面创建一个 package 这个 package 它的路径是 com.imock.itemok 接下来我们创建 item 的启动类。


好，这个类的名称我们给它起名叫 item application 好这里面有什么内容呢？咱们 public static void 先给它加一个闷方法，好它的启动方式是 spring application 然后直接调用它的 run 方法，把这个类的名称给它传递进去到 class 对象后面，把运行期参数传入。


OK 那这上面要添加一系列的注解，我们到福地 DEV 当中把这些注解给 copy 过来，我们转移到了福地带，找到在 API 层里面的这个启动类 application 我们把这里哪些注解 copy 过来呢？从这里看，把咱这头三行给它拷贝过来，好回来把它放上以后，这里有一些地方要做小修改。比如说咱的这个 mapper scan 在这里， scan 的是通用包， com.imock.mapper 那咱这要加上一个 item 因为我们商品域的 map 都放到了这个新的文件夹结构下面。
OK 那接下来还有什么要改变的吗？这里要新添加主界，要添加哪个呢？服务发现 enable discovery client 好，把这个注解加上去。那接下来在后面的章节里我们还要再加上 fin 注解，所以我这里给他加一个 to dook 那这里有一步我们要补充一下，你看这个 component scan 它需要去扫描 ID worker 那这个 ID worker 之前我们没有把它移植过来，这里同学们自己去把 food DEV 当中 common 包下的 ID worker 移植到哪里呢？移植到这里， food cloud common 把这个报原封不动地移植过来，什么都不用改，这就好了。这个步骤在之前创建 cloud common 这一个模块的时候给漏掉了。


OK 那我们接下来就要去把 controller 层给拿过来了，我们这里添加一个新的 package 叫 controllerok 那 controller 从哪里移植呢？我们切换到 foodie DEV 找到 controller 的所在地。在 API 这里。那这么多的 controller 我们的 item 其实只用这其中的一个，非常的少，items controller 就用它就好了，其他的这些 controller 自然有相对应的微服务模块来认领。好，我们把 item controller 复制一下，然后切换回 item 外部项目，把它给拿过来。
好勒，拷贝过来以后，看到这里又是万里江山一片红，我们要把这里面的一些类的路径给他改一下，把缺失的 item 添加上去。好，这里 service 也同样的需要 item 剩下的两个 category 相关的我们把它移除掉，因为咱在服务里没有用到这一个 Jason object 把它的路径改一下。好勒，然后把贝斯 ctrl 给它引入进来，那看看还没有标红。这里还有，那应该是这把 post 也给引入进来。那现在看上去还有两处标红，我们看看是谁还这么顽固不化。原来是 search 那 search 接口我们移到了搜索服务。所以这两个 search 标红的 search 我们把它直接删掉。 OK 好勒世界，顿时清净了。


那我们 ctrl 也已经写好了，application写好了，剩下一步就是去创建 resources 配置文件。那这个配置文件我们只用到 DEV 项目当中，把这个配置文件 copy 过来。好，我们选择福笛带 vpi 到 resources 下面，把这一股脑的所有东西统统 copy 一下，然后切换回来。好放到 resource 文件夹下。那这里有些东西是不要用的，比如 file upload 那这两个待会是用户中心那边需要去上传的，我们把它给删除掉。好剩下的三个东西，applicationyamldev.yaml还有 product 这三个是我们需要用到的。
那咱接下来就开始添加配置文件了首先我在这里新建一个配置录像，叫什么名字叫 good strap.yaml 那在这里面放什么啊？同学们看 eureka 的注册中心。那我为什么要把 eurika 注册中心配置到 bootstrap YAML 而不是配置到 application YAML 呢？实际上，从我们 eurika 这个章节来看，你配置在 application 里面依然是可以起作用的。不过当我们学习到后面的时候，如果我们学习到配置中心 config 那你 eureka 注册中心的位置就要好好考量一下了。


因为咱前面说过有些配置项还有配置文件，它是有一定的加载顺序的。那我们引入配置中心以后，为了保证你在服务启动的时候先去拉取配置文件，那我恐怕要把配置中心配置在哪？配置在 sprint boot YAML 当中。如果我们同时也要关注配置中心的高可用化，那么必然而然要把配置中心挂到哪里呢？挂到注册中心里。所以说注册中心和配置中心都放在了同一个文件，也就是 boot strap 当中，同学们听了是不是觉得有点像听天书没关系，后面学习到配置中心的时候自然而然就明白了。好，那我们这里把注册中心先给放到这，接下来就没事了，我们回到 application.yaml 去把这里面的内容给它改。那么一改都有哪些东西要改呢？第一个，我们在 spring 下面要改一个谁要改一个 application 添加这样一个节点， application 的 name 我们给它起名叫做福地 item 杠 service 这就是我们微服务在注册中心里面的名字。那再往下没有什么好改的。再往下，再往下。走到这里。 my betis 那 my baddies 里面的路径，我们这里要把 item 给它写上去。那我这里在这边添加一个提示，提醒同学们注意更改路径。好把这个提示也同样的加在这里。


配置数据源信息的这个框里面叫更改 application nameok 我们再往下看除了这个步骤以外，通用 mapper 这里不用配，我们的路径没有变，还是这样一个路径。 OK 那接下来我们就要去变这个 application div 走进来到这个 application div 当中，我这里有这么几个地方需要变。首先 server port 那么 server port 我这里要启动很多个微服务组件，所以咱们每一个 port 就不用占用 8088 端口了，我们给他起一个万年老大10,001。


好吧。好。那改完端口以后，我们这个数据源也要做一些相应的改动。因为老师这里是怎么样了？我们把数据源都拆分成了不同的 schema 用这种方式模拟每个微服务有一个独立的数据库。不过同学们这里如果没有做拆分的话，也可以继续沿用之前的 foodie shop DEV 这个 API 索罗意义。
我在这里要添加一个注释，叫拆分数据源到独立 database 到独立的数据库实例或者独立 schemaok 那我这里给大家一个例子，我本地的环境是这样的，我把它拆分到了 foodie cloud item 当中，那这是一个独立的 schema 说到操作数据库，我给同学们推荐一个软件 data grade 那它是 intelligi 出品的一款软件，它操作数据库非常方便，创建数据源，也支持很多种不同的数据库，比方说 MySQL mariadb 那都是它可以支持的。


同学们如果想使用正版，其实非常方便，可以去淘宝上面买一个 EDU 的邮箱，这样的话 intelligg 可以持续的给你提供免费政策。那么每一年只要去注册一下就可以了。我就是用我学校发给我的 etu 邮箱。因为我们学校在毕业之后没有把邮箱收回，所以我还可以继续冒充学生。


好，那我这里数据源更改好之后，剩下还有没有要更改的？没有了临门一脚。这最后一脚现在又到了，可不是启动项目，我们杀回到 pom 当中改什么内容呢？这个 build 节点中，我的 repackage repackage 重新打包，它需要指定一个 main 函数。好，我的 main class 是 come.imock 我们把启动类给它交代出去。 item dear item application 好嘞这下临门一脚踹完了，我们可以去启动项目了。


在启动 item 项目之前，我们先保证什么呢？保证把 registry center 给启动起来。那老师这里已经在外面的命令行中把注册中心跑起来了。所以我这里可以直接去执行这个慢函数，同学们也可以在外面把它编译出价包，然后使用 Java 杠 jar 命令来执行。好这里直接启动闷函数，稍等半炷香的时间。等它启动好之后，我们到 postman 中调用几个方法，然后再到注册中心的页面上看一看是不是真正的跑起来了。好，看到这 log 在狂刷。 OK 那这里显示已经 started 那我们就到注册中心上面瞄一眼。好，我们切换到浏览器那这里把它刷新一下。 OK 它刷得很快，我们这个看到，已经有一个服务注册上去了。


Foodie item service. 那我们点开 postman 尝试调用几个方法。首先我们调用谁呢？ local host 10,001，那它的路径是 items 杠 info 然后传入了一个商品的 ID 那这个接口大家应该都比较熟悉了，我点击 send 这个接口已经顺利返回了。


那接下来我们再测试一个什么接口呢？测试咱改造的 service 接口，也就是我们在这个 service 层里使用 rest controller 注解了修饰的这个接口，看一看它是不是会生效。那我们调用这个接口中的哪一个方法呢？我们就调用最简单的好了，根据商品 ID 查询详情的这个接口。那它的路径是 item 杠 API 后面是 item 好，我们切换到 postman 里，这个路径已经在这里打好了。 item 杠 API 然后斜杠 item 那我查询的依然是这个 itemid 为饼干 1001 的商品。


点击 send 同学们看到这个接口也已经生效了，那咱商品中心的改造任务就已将基本完成了。为什么说是基本完成没有全部完成呢？因为咱还没有发起服务间的调用。待会儿我们去创建好其他的微服务之后，会发起对商品中心的调用。但是这里老师提醒大家一句，因为我们微服务阶段现在还没有引入网关，所以这里咱的每一个服务的端口都是不同的。如果同学们尝试从页面向后台发起指令，那可是会失败的。等到我们学习了网关层以后，那这样的话在前端页面上只要配置访问这个网关层，那网关会负责把消息转发给后台的各个微服务。 OK 同学们，这一节很长，那到这里就先告一段落了，我们下一节再来继续改造其他的微服务。那同学，我们下一小节再见。

