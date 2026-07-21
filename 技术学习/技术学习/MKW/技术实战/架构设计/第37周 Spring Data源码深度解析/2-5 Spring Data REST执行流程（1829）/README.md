---
title: 2-5 Spring Data REST执行流程（1829）
---

# 2-5 Spring Data REST执行流程（1829）

[image](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/77246d27-3352-4edd-9db2-5ca01025af7e/SCR-20240814-hxmb.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662T6M64RV%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T232135Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCcnXuNyv1XLFoh1gOWp%2B6giD1dWCmleVO5DbuC%2BlBpgQIhAMco%2BWD8Z7nZly%2BqGu3EYjhOZ%2FXU5ZPA4UAKlzE1nY4fKogECMb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1Igzc3lAtZm7%2BAFKm0eAq3AN3iRhiMdFCYeJqM43VsXmFFCgtsXY%2F7HhoYOsvL5xSdpQn%2BZFav305zzvZtOarofjxGqarOODdaoeFFjCmnAfbox2OjMWQ3ER1T8vQrWdd39V5mOUui3Ep0CSVLEMquemMqRxVFIOXNsQXqnIUlHHUY0M39NNGhbc1a5d5f6%2BQpdk%2BH2O5fcCrRUs1Lw4sPQhkaAD%2BQa%2BjoIK8A0CUHmMiIzC1t0NJ4GnSsGH90b%2Fa%2FMC1wQNeauGhRywyy6x1i6OKvYT7DuTK3RMDqYD85sJ7IG7Kwx8Buxo1MlaG3%2Fjyh7jo0%2FcJtz4M4GjjGcV%2B46OCw3urlp7WXhrfVvDCPtjgGTin21gICpV4HIin%2FUDJyj1WaV34JLPIIcaOvSQaqzAu0J1G2t6JlaQcwfjcW0hlcDdUukbBtTlWTt53vK2L7jHVP8DUce%2FG5wmPmVSxtbRHbk2S%2BJRslnS2DV%2F%2B2Q8HhtQBAF4YF7JmXhXnPI1ytfJdqc1%2ByLIMIEiuFxaHUlQYAHxYp5w2uWx%2BhxAtCIetq5BDrSFt%2FvciGaPA2Wc3OH5k362HlV54AI67J3UDPnZDBiTjUZSL3%2Bgf5Y5uJ7zQMKIpue3L9u46ezdl5A%2F%2BigQBdmaCPOq8Kg%2BsSjCjuP%2FSBjqkAeFoxbKahED%2BRcJ6H8Va3bEveyQXQl3hj%2BGlzyxvIs7UfXTEtTlS9CyIXbcLwE%2BrSJSV1Ev5QXlS9mJr5MerNr76P1i9R1V%2FJEqk8AVTfvfCgSm0HHIBP1vHQEUzKa7nnWTwI6CvIcmtrBxagZozu9LbZOcJNcr%2FLxFtBP9BOOuGLTBhTcO5Okl%2Fs7hkY6apM%2BpBk4Pir8PB%2BhFdzO9UqYIg62LR&X-Amz-Signature=818a1ecc3255e49d8b2eb60c7828bce3b8f2c0af3830cfff4fd6a782039deffe&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

[image](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/eeb33c7b-cda5-4422-8b4d-d6f7878332c2/SCR-20240814-hvwd.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662T6M64RV%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T232135Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCcnXuNyv1XLFoh1gOWp%2B6giD1dWCmleVO5DbuC%2BlBpgQIhAMco%2BWD8Z7nZly%2BqGu3EYjhOZ%2FXU5ZPA4UAKlzE1nY4fKogECMb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1Igzc3lAtZm7%2BAFKm0eAq3AN3iRhiMdFCYeJqM43VsXmFFCgtsXY%2F7HhoYOsvL5xSdpQn%2BZFav305zzvZtOarofjxGqarOODdaoeFFjCmnAfbox2OjMWQ3ER1T8vQrWdd39V5mOUui3Ep0CSVLEMquemMqRxVFIOXNsQXqnIUlHHUY0M39NNGhbc1a5d5f6%2BQpdk%2BH2O5fcCrRUs1Lw4sPQhkaAD%2BQa%2BjoIK8A0CUHmMiIzC1t0NJ4GnSsGH90b%2Fa%2FMC1wQNeauGhRywyy6x1i6OKvYT7DuTK3RMDqYD85sJ7IG7Kwx8Buxo1MlaG3%2Fjyh7jo0%2FcJtz4M4GjjGcV%2B46OCw3urlp7WXhrfVvDCPtjgGTin21gICpV4HIin%2FUDJyj1WaV34JLPIIcaOvSQaqzAu0J1G2t6JlaQcwfjcW0hlcDdUukbBtTlWTt53vK2L7jHVP8DUce%2FG5wmPmVSxtbRHbk2S%2BJRslnS2DV%2F%2B2Q8HhtQBAF4YF7JmXhXnPI1ytfJdqc1%2ByLIMIEiuFxaHUlQYAHxYp5w2uWx%2BhxAtCIetq5BDrSFt%2FvciGaPA2Wc3OH5k362HlV54AI67J3UDPnZDBiTjUZSL3%2Bgf5Y5uJ7zQMKIpue3L9u46ezdl5A%2F%2BigQBdmaCPOq8Kg%2BsSjCjuP%2FSBjqkAeFoxbKahED%2BRcJ6H8Va3bEveyQXQl3hj%2BGlzyxvIs7UfXTEtTlS9CyIXbcLwE%2BrSJSV1Ev5QXlS9mJr5MerNr76P1i9R1V%2FJEqk8AVTfvfCgSm0HHIBP1vHQEUzKa7nnWTwI6CvIcmtrBxagZozu9LbZOcJNcr%2FLxFtBP9BOOuGLTBhTcO5Okl%2Fs7hkY6apM%2BpBk4Pir8PB%2BhFdzO9UqYIg62LR&X-Amz-Signature=7780618ee291b50fda8e97583c3f79dba07c6980683f6c798d16c79d0d5ef59f&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

我们看一下 spring did reset 它的一些执行流程，其实对于执行流程的话，我们知道对于 spring did RESET 它遵循了 Mac 的规范，它在里面也对于 spring Mac 进行了一个扩展，我们知道它里面会涉及到两个注解，一个是 base Paas aware Controller，一个是 reposure reset Controller。


基于 report RESET Controller，我们定义了这四个Controller，也就是这个关键的Controller。这里面我们会通过 report entity Controller 来进行一个 debug 的一个演示的一个过程，其他的人对应的 Repass 看出来它的逻辑其实类似的，那么这里面我们对于 MA seed 流程在这里面不会赘述了，所以说我们进行观察的一个起点，也就是通过我们的 control 作为我们观察的一个起点，那么对于 dispatcher 到 control 这个过程，其实我们知道它里面会涉及到一些参数的解析，我们的 request mapping 进行映射到对应的control。那么对于 string reset，它也定义了很多，我们的 handler mess 的 human 的resilver，也就是我们的参数解析器。这些参数解析器我们列出了几个比较关键的，这里面像 root resource information，我们通过这个插入解析器解析出我们的 root resource information 就是根的一些资源信息，同时我们还会解析对应的 resource Meta date 相关的信息，跟这个请求相关的一些资源的一些元信息。


后面我们可以看到这里面是 present entity resource，跟我们持久化实体相关的一些资源信息，后面是 present entity resource Assembler，那么对于它是一个什么样的一个工具？其实我们可以理解我们通过 control 进行构端的所有资源，这些资源最终我们要是渲染到前端，我们需要组装一下森brand，我们可以理解为它是一个装配工，把我们获取各种的 resource 资源装配成对应符合 title 规范的这样一个资源。


好，接下我们来看一下各个资源它一些具体的一些情况。首先我们看一下这个 root resource information，对， root resource inform mission 它里面包含的信息，比如像 resource metadata，我们的 reports invoker，对于 report invoker 我们大家应该还有印象，它可以去进行真正我们对于 report 操作的执行，这里面还会涉及到 present 的entity，就是说我们持久化实体对象的一些属性，包括里面的类型、我们的 ID 的情况等等。


对于这里面的 person entity resource，Blair，它里面也会包括像 source Metadata，我们的 report invoker 和我们的一些持久化实体的一些信息。这里面还有一个比较重要的就是我们的 person int resource，那么对于它是我们进行输入或输出进行转换的一个实体的一个资源类型，这个资源类型在我们的 person 的 entity source 还是比较重要的，这是我们在介绍了我们spin，did， reset 这些相关的一些执行的一些流程。其实我们可以关键的说了一下执行过程一些关键的一些属性，那么接下来我们会通过 debug 的方式去debug，跟一下我们真正执行的过程，包括我们的 showcase 的代码控件。


我们来看一下，这里面我们新建入了一个 reset 这样一个模块，这个模块里面我们可以看到它的代码内容，我们可以理解为跟 GPA 是一模一样的，只是我们在 pool 文件里面添加了一些跟我们 reset 相关的一些信息。这里面我们先看一下我们的 POM 配置文件，这里面 palm 配置文件我们重点关注的还是我们依赖的这些dependence。okay，这里面增加了 start date reset，也就是我们跟我们 spring date reset 相关的一些信息，同时我们这里面引入了 spring did reset 的 ICR explore，以及就是我们这个 UI 工程，后面的内容我们可以看笼book，这个我们就不去过多介绍了，我们可以看到这里面还会涉及到了一个，这里面会涉及到是 spring focus 的Swaga。我们这里面为了让大家更比较体现出这些 rerest u i 它里面暴露出哪些接口，我们通过 swagger 的方式暴露出我们这些 request Mapping 对应的API，这样方便大家去更直观的理解。这里面也是用到了 strong 对于 Swaga 它的一个 boot starter h 方式去自想当然，我们为了底层有数据的提供，我们这里面使用的是 stream boot starter， data GPT 这样一些信息。


好，后面的内容我们就不用过多的去介绍了。好，这是我们模块的信息，那么我们现在已经启动运行了，我们先看一下我们这个涉及到的一些界面的信息。首先这里面对于这个 SR explore，这个跟大家介绍过了，这个已经不用再说什么，我们可以看到通过我们的分页查询能获取到我们当前的信息对象，这里面会涉及到配置的这些知识，我们可以预备请求参数，这是我们请求参数是配置第一页，当前页的内容是5，一页的总量是5。


那么这里面我们可以看到获取的信息是当前页的页容量是5，它 total 的element，也就是我们的种的资源数，也就是词，我们分页分 10 页，我们当前页是第一页，这里面这些信息我们就不再一一介绍了。我们来看一下 Spark UI，当我们集成完 Spark UI 以后，我们可以访问对应的 Spark UI 这样一个URL，它会跳转到我们这样一个 UI 的效果。注意一下，这里面我们应该有一个后缀，一个撇。好，那么这里面我们看到它的一些信息。首先这里面做了一个分组，在这个分组里面我们看到 user entity，这里面是 simple GPT 的reportery，另外一个 basic error Controller 和我们的 SAL 的explore，也就是我们刚才这样的一个，还有涉及到 operation 的 handler 以及 profile Controller，以及我们 VC link 的handler。


那我们打开一个简单过一下，其实我们最重要的是 user entity 关注，那么我们的 showcase 功能里面我们定义了一个reporsory，这个 report 就是 user report，它的模型也就是我们的 user 模型。那么在这里面我们构建出的URL，我们可以看到它是urls，也就是复数的，我们可以从里面看一下。


对于 users 我们可以看到它执行的操作是 find our user，我们可以从这里面去看一下它执行的一些操作。在这里面我们也可以进行一个我们的一个 rush 的一个验证，我们可以在这里面去点一些 trade out，我们可以看到这里面我们可以输入一些信息，比如说我们是分页，是第一页，我们的 size 数我们还是5，我们排序时段我们留空，那么我们现在可以点执行。好，现在我们可以看到它生成一个对应的一个 care 的一个脚本，我们可以通过这样的方式进行一个执行，我们可以看到跟我们在这里面生成的效果其实是很类似的。


接下来我们来看一下我们请求的URL，是这样一个URL，它获取到的信息，这里面是响应的 SCP 的状态码是200，也就是我们 200 是正常成功，这是我们返回的一些响应一些信息，这里面还会包含一些 response 的一些 header 信息等等，这里面一些情况。好，那么这么里面这是我们执行的一个效果，这是200。我们接下来看一下它还会有一些状态码的一些说明，比如说 401403 或404，对于 240 一个正常401，我们可以理解是未登录， 403 是已登录，但是权限不足被禁止，那么 404 也就是 404 是最常见的，大家也非常知道 404 是找不到了。


寻人其次好，这是我们看到的是第一个我们的一个请求guide，我们获取一个 guide user 列表，那么我们第二个是 pose 的user， pose 的意思，我们看这里面的描述是save，也就是把一个用户进行保存。我们的 rest 风格里面 get 是获取 post 创建会议信息，那么 get 我们指定 ID 的话，就是指定我们具体的一个信息。 put 我们就是修改，我们对于一个对象进行修改的时候，我们通过 put 协议进行这里面 delete 相关的一些信息。好，下面有 pets 和 get 这些信息我们就不再一一去介绍了。


对于 PETS 和 put 其实是有一些区别的， put 是相当于是你把整个对象进行一个我们的 save 更新， PETS 你可以去更新你指定的传入的一些属性都，如果说有些属性你不关心，它是不会进行更新的这样一个道理。对于我们的一些查找的话，它还会有一些对于 search 的一些操作，比如说我们的 find by name，对于这个 find by name 是我们在这里面特意的自定义的一个方法，这里面 find by 是我们通过命名查询的方式去定义出来的，这里面我们可以看到它也是 find by name，我们是user，是设置 find by name 构建出这样一个操作，我们也可以通过 string 的 reset 方式去构建出来。这里面我们可以输入我们的内幕的名称，去查找我们关注的一些信息。


好，这是我们比较关注新的这个 user NT 的一些情况，那么我们其他的也可以简单过一下。首先是 basic error Controller，这是我们 Swift 给我们提供的一个 error Controller，你看它对于 error 支持了get、put、post、delete、OPS、 head 各种请求，也就是说各种协议的 l 它都会支持。


这里面还会涉及到我们看到是 SL explore，也就是我们这个 UI 所暴露的一些信息，这里面是有 index 和默认的，就是 PR 或 explyer 相关的一些信息，这里面还会涉及到一些 operation handler，我们可以看到它是我们 stream 部的提供的这些occur，这些 occur 的 in the point 就是像这里面 been cats 等等一些信息，这里面对于 cats 信息它可以进行删除操作。


这里面还有我们的一些条件的，我们肯定是你就是装配条件一些信息，这就是上下文环境的一些信息，这些我们都可以在这里面去自行去看，我们也可以通过浏览器在这里面执行 occur 相关的一些信息，这里面比如一些 Mapping 的相关的信息。下面是 profile 的Controller，我们对于 spring date、 GPA 或者 spring date 相关，它有一些 profile 相关的一些信息，后面是外表名词的 link handler，这里面是 occur s occur，也就是我们这样一个默认的 URR 的发文请求。那么现在我们已经知道了，对于我们使用 spring date reset，我们会暴露出哪些请求，就是主要是 user entity 下面这些蒸删改查和我们查找的一些信息。


到我们的程序模块儿，我们通过断点的方式去debug，跟进我们这些关键的一些执行节点。好在这里面我们看一下这里面是加了哪些断点，其实这些断点信息我们可以看一下，这里面首先我们是最重要的，也就是我们的 reposure entity Controller，在这里面是对应的一些断点析，还有是对我们参数解析的过程一些断点信息，因为我们这是一个 spring Mac 的工程，它在进入 control 之前首先要进行我们这些参数的解析。那么我们可以首先会进入到参数解析的一些执行过程，那么这里面我们现在可以去先进行一些字形，那我们发起一个请求，好，我们从这里面去发起请求。好，我们点go，现在已经进入我们的断点了。


首先我们可以看到现在进入我们的一个参数体系，就是 root resource information handler 的一个参数解析器，那么在这里面解析的过程中，我们可以看一下他关注的信息。首先在解析 root resource information 的过程中，它首先会解析我们的 resource metadata，那么我们可以看一下在这里面我们 debug 可以跟进去，里面我们是如何去解析我们的 resource metadata，好跟进来，我们看这里面是会有一个 base URI，从这里面去获取我们的一些Lookpass。


我们可以看一下我们查找的路径，查找路径我们可以看到它对应是users，也就是我们的一个 user 的复数，接下来会通过我们的 UI UTO 去通过我们的一些信息获取到我们的 repose rek，那么我们可以看一下它获取到的 report key 是什么，这里面获取到的 report key 也就是我们的users，就是跟我们 report 相关的信息。


这里面我们接着去查找这里面对应的 repository 的一些信息的一个迭代，我们去通过里面去查找是不是能 match 到，那么我们这里面可以看一下对于 report 里面它的一些情况，这里面我们可以看到是对于 reporsory 的一个 be name，它只有一个，那么我们可以从这里面去看一下它是当然是可以匹配得到的，我们可以看一下它的一个 Mapping get pets，再进行一个模式的一个匹配。


我们首先看一下这个 resource metadate 的 Mapping 的信息，我们可以在这里面去看这是 Mapping 信息，我们看到它里面的 get pass 信息去进行一个模式匹配。好，现在它已经就是我们匹配到匹配到完了以后，就把对应的这个 Mapping 去返回出来，这个 Mapping 信息就是我们实现的是 report aware resource metadate 信息，好，我们把这个信息返回过去，那么得到了这个信息以后，我们开始进行去通过我们的 resource metadata 里面获取我们的 DOM type 我们的类型。这个类的类型我们知道它是一个 user 类型，好， domain types 对应的是 model users，这里面我们再去通过我们的 invoke factory 去构建我们的invoke， invoke 的类型是对应的我们 user 信息，好，这样执行。


那么接下来再去通过我们的类型去获取我们的 process 引体的一个实体类型，其实这里面都是我们类似于一些元数据的一些信息组装，那么把这些元数据信息获取到以后，进行一个组装，一个 root resource information 这样一个对象把它去返回过去，同时这里面我们可以看到它会有一个后处理，对我们这些进行后处理的逻辑，其实也就是给我们留下了一些钩子，但它并没有做任何实现，它只是把我们有 worker 直接返回出去了。


好，我们执行完这个我们的参数解析器，那么下来我们跳过这个断点应该会到另一个，这里面是我们的一个 present into the resource，一个解析器资源，这里面是主要是对我们资源的一些我们的汇聚封装，这里面汇聚封装我们可以支持一些类似于投影的操作，或者是成为剪枝。也就是说我们对于我们这个对象我们不关心的这些属性可以让它不输出来。这里面会一次我们去通过去查一下我们的 protection 的parameter，也就是说我们对于哪些属性是不关心的，但是我们这里面我们因为没有去设置，所以说它默认获取的是一个空的一个对象。


接着我们去看一下，那么接下来会遇到这些信息，我们就构造出我们的 person 的 entity resource assembler，那么可以看到这里面的信息，我们的实体的相关信息，我们的 project 和相关的一些集合的一些属性。我们的 link 的一个 provide 就是我们如何构造我们 link 的信息。


好，我们现在跳过这个断点，我们到下一个，这里面我们可以看到是一个，我们这现在已经回到了我们的country，也就是我们 report entity country，那么到我们的 control 的方法，那么现在这里面是 base mapping，我们的 get 也就是获取我们的 get 列表。


在这里面它首先会做一个参数的一些校验，也就是我们的是否支持一个 get 方法的一个校验，我们这里面就跳过现在我们可以获取到我们的 repose 的invoker，那么如果说 invoker 为 null 的话，就可以人理解为我们 GM 值 net 也就 404 了，那我们这里面是存在的，这里面还会去判断一下我们这个 pythable 是否是进行分页的，如果进行分页的话，它就把我们的如果 pythable 不为 null 的话，我们进行通过分页的方式去查找。如果说为now，那么这里面这场 shot 也就是支持我们的一个排序。
好，我们具体的 invoke find all 我们可以跟进去这里面的操作其实就到了我们的 GPA 操作的一个过程，我们可以看一下通过我们 delegate 进行我们的一些执行。好，我们这是到我们的 JDK Dynamic 包 AOP 的process，这个大家就应该是比较清楚这个过程了。现在我们其实跳出我们的这个 debug 的一个，现在我们是看一下这里面我们通过我们获取到的 Meta date 信息，那么进行，我们现在已经得到了 result 信息，那么对于 result 的信息我们会进行一个组装，这个组装的过程我们首先会获取到我们当前默认的 self link，我们可以理解为它是一个URL。


首先去获取到我们当前这个请求对应的URL，我们可以看一下 base link 它的内容，那么对于 base link 的内容，我们可以看到这里面是对应的就是 local house 的8080，我们的users，同时我们的配置transfer，配置一我们的 size 5，当然这里面对应的别名也就是self。那么这个构建完成以后，它会去组装我们的 clicks 的一个model，当然把我们的结果，我们的组装器等等一些类型的组装起来，同时再会添加一些 collection 的 resource link，也就是跟极客相关的一个link。


那么我们简单跟进去看一下，先到我们的 collect model 操作，这里面会判断一下我们这个来源是否支持分页，当然它是支持分页的，那么支持分页，它会通过分页的方式把我们的 resource 组装成一个配置对象。好，我们可以看到这里面会进行一些操作，那么我们跳出了。


好，在这里面我们再进行一个添加一些其他的一些 resource link 信息，那么我们可以看一下这里面获取到的 link 信息是什么呢？这里面构建出来，我们看看一下这个 link 信息，这里面的 link 信息，我们看到它是里面涉及了两个对象，我们是对应的是 profile 和search，它会作为我们补充的一些 link 信息，会给我们装载到我们返回的这个对象里面。


好，现在我们返回，那我们现在跳过断点，那么整个请求就执行完成了，那我们跳过断点，那么请求完成，我们去看一下这里面请求返回的信息。首先这里面对于我们返回的内容，我们可以看到它这是我们的users，就是我们的一个clicks，也就是我们 user 列表。对于每一个 user 对象，这里面涉及到两个lynx，一个是我们的self，这个 self 是指当前这个对象的一个 self 信息，也就是说我们要访问当前这个对象，就通过这个 URL 访问就可以。


下面我们来看一下整体的，这里面是个 link 信息，也就是我们分页相关的信息，这里面是有，比如 fast 的，我们分到第一页，我们Pre，也就是我们前一页 self 当前的和 next 的last，以及我们的 profile 和search。这是我们在最后补充 link 的时候，补充的是这两个 link 的信息，但这里面还涉及到我们配置的一些元数据信息。好，这是我们对应这个我们 spring day RESET 一个查询的一个效果。那么关于 spring day 的 RESET 执行的流程我们就先介绍到这里，嗯，谢谢大家。

