---
title: 013.用户服务搭建（下）
---

# 013.用户服务搭建（下）

那这个接口算是写完了，但是活还没干完，那我们接下来实现了一个接口，好的习惯是使用对应的一个接口测试工具，测试一下接口的一个能力。当我们看到 user Controller，它其实接收的是一个 JSON 对应的一个对象，我们可以使用 postman 工具去测试一下这个接口，我们先把对应的服务启动一下， debug 启动，打开postman，我们这个 postman 可以直接书写想要测试的一个接口的能力。


我们来看一下，我们使用 local host 8010，然后是 user 杠register，我们实现的是一个 post 方法。我们在这边的 body 当中选择一个roll，可以切换成 application 杠json，然后它会默认帮我们这边的 type 加上一个 content type， application 杠 json 指定我们对应的这个 body 是一个 JSON 对象。好，我们直接在这边使用 JSON 对象即可。


iPhone 创建一个1312345678，我们对应的一个 password 是123456，然后 nickname 把它叫做小IMOCOOC。 sender 是个 intrigger 类型，责任定是一，然后我们 send 一下，我们可以看到这边已经非常完美的抛出了一个error，是一个用户已存在，那这个用户已存在就是我们在这边 register 方法当中定义的一个error，也就是这个 register duplicated fail。


那我们可以查看一下数据库之前其实已经为我们创建了一个 the user 对象， telephone 是一个这个样子，那我们可以直接先把对应的这条记录删除，因为毕竟这条记录是我们人工造了一下删除，然后重新 send 一把，我们其实可以看到这个用户其实已经创建成功了，并且密码也是经过 MD 5 加密。


我们来 refresh 一下，可以看到对应的这个用户以及加密后的密码 nickname 以及gender。那我们也可以验证一下 spring MVC 对应的一个 error binding。我们将这个 telephone 擦掉， send 一下，我们其实可以看到手机号不能为空，然后我们在这边可以将密码干掉，这边是密码不能为空。好，但是这边有个小小的bug，我们最后的这个逗号没有干掉，那我们打开 common util。原因是这个 substring 没有赋值，那我们可以直接将这个值返回出去，我们重新启动一下，我应用。
重新send，大家可以看到这个逗号已经没有了，也就是说我们有多少个error，那这边就有多少个对应的字符串，再加一个逗号的一个串接。那至此我们完成了第一个 user 注册接口的一个实现和对应的测试。


那接下来我们对应的 PRD 内有了解到，除了用户的注册行为之外，我们还需要一个用户的登录行为，接下来我们需要实现我们对应的一个用户的登录行为，那思路仍然是一样的，进入 user service，我们先将服务停止，进入我们对应的这个 user service，我们这边实现了一个 register 方法，那接下来我们要可以实现一个 login 方法，这个 login 方法的入参就相对来说比较简单，我设计成只有一个iPhone，然后再加一个password，好，我们去做对应的implements。这个 login 方法本身其实是一个只读的操作，那我们为了性能考虑，我们可以不加transactional。因为 login 方法当中并不会对数据库去做任何的一个写操作，我们直接实现对应的 login 方法即可。


那我们在这边需要在数据库层面开一个Mapper，是使用 telephone 和 password 去做对应的一个 user 的查询，那我们进入 user model Mapper。在这个 user model Mapper 内，我们需要实现对应的一个方法。之前的查询只有一个根据 ID 组件查询，那我们接下来需要另外开一个查询 user model 的 model 方法是 select by telephone and 哈索。然后我们需要定义一个iPhone，定义一个password。同时使用 Parama 的annotation，告诉我们对应的一个 mybadcase 我们使用什么样的名字去读取这两个字符串，一个叫 Tel 控，一个叫password。好，然后我们进入对应的一个 XML 文件，我们需要去实现对应的这个 select 的一个方法。


我们直接写在最后 select ID 是 select by cell phone and password，需要和 Java 文件当中对应的一致，否则它会找不到 result map，返回是一个 base result map。这个 base result map 其实就是我们在这边定义的一个 user 的一个 base result map。然后我们在这边写 CQ 语句即可，我们select。然后我们 include 一下 REF ID 是这个 base column list，也就是我们这个 base column list 是写在对应的一个 CQ 上的。我们可以看一下这个 base column list，其实就是这个 SQL I d select 出所有的这些字段，这样的话我们的 select 的地方就不用再反复的去写那么多字段。


然后我们 from user where telephone 等于一个我们一定要使用井号的telephone，因为对应的 dollar 符号的 telephone 是没有 biding results 这样一个功能的。它会引起 CQ 注入的问 telephone 和 password 相等，入参相等，并且使用 and 符号串接将对应的这个 user 查询出来。然后我们再次回到 user service 当中。我们在这边很简单接收一个 user model，然后使用 user model 的 Mapper select by telephone and password 将这个 telephone 传入。这个 password 我们不能直接传入，因为我们需要调用 MD 5 加密，将加密后的字符串传入，才可能做到完全意义上的比较相等。


抛出对应的一个算法的一个异常，如果说这个 user model 等于null，也就是没有查到这个 telephone 和这个 password 对应的一个 user 的对等关系，让我们不好意思将对应的一个异常抛出。这个异常我们自定义一把，之前是注册失败，表明用户已存在，然后我们这边要使用 login file，表名叫手机号或密码错误。然后我们直接将 login fail 给它抛出去，如果说能够查到的话，因为我们对 telephone 设了一个唯一的索引，所以这边就算能查到也最多只可能有一条。


所以说我们直接将这个 user model 返回即可，代表我们对应的就是这个用户登录成功，然后我们进入 user Controller，我们在 user Controller 当中需要集成一个login，我们直接使用 request mapping，然后注明把它叫 login 方法，返回一个 response body，然后它是返回一个 common 的results，叫做login，然后仍然一样，我们指明一个 request body requestbody，这个 request body 我们需要在对应的一个在 Web request 的对应的包里边新增一个叫 log in request。
这个 login request 其实相较这个 reject request 来说就只有这两个参数，一个 tail phone，一个password，我们简单一点 copy 过来，然后注明他们都是 not blank。然后我们只需要将这个 login 的 request 加上 valid 的标签，然后叫 login r e q。


然后指明一个 binding results，我们在这边仍然做一把入参的判断， binding results add errors 的话，那我就死肉一个 new 一个 business exception。我们把它叫做 parameter validation error，并且使用 common utile 对应的 process error message 将这个 binding result 传入。我们其实可以看到一旦封装好了对应的方法使用起来就非常的简便。 add 一个exception，然后我们接收一个 user model，使用 user service 的 login 方法，然后将 login request get cell phone， login request get password。


谈到 service 层，这个 login 方法会为我们解决所有的一个问题。当我们对应的这个 login 方法生效的时候，我们还需要做一个事情，就是使用 HTTP 的一个session，将这个用户的注册成功放到 HTTP session 内。那我们怎么集成对应的一个 HDB session 呢？也非常的简单，我们直接在 user Controller 内 autowild 出来一个 bring 的一个 HDDP servlet request 对象。


这个 h t d b subflict request 是一个 screen 的bin，在它内部使用 THREAD local 的机制，使得每一个用户的请求拿到的指向的这个 HDB Server late request 其实都是属于这个 THREAD local 内的一个 HDDB server late request。所以说只需要用一个 autowild 的一个 spring 的 HTTP solid request 的对应的一个对象，就可以拿到当前线程处理用户请求的一个 request 对象。


然后我们在这边新开一个 session 的key，我们把这个 session 的 key 定义为 current user 杠session，也就是说我们将对应的这个 session 定义为 current user session，那这个常量我们定义的有什么用呢？就在我们对应的这个 login 请求内，当用户登录成功之后，我们就需要将 SDB servator request 使用 get session 的方法将对应的一个 attribute 设置进去，也就是设置这样的一个 current user session 的 key value 是这个 use user model。当用户登录成功，我们就把这个 user model 对象放到用户对应的 HTTP 的 session 当中，并且 attribute name 是一个叫 current user session。然后我们返回一个登录成功的标识即可，那我们在这边可以直接返回一个null，告诉他登录成功，也可以返回对应的这个 user model。


那这个就是 login 方法，在设置对应的这个 HTDP 的 serviator request 当中做一个保险的起见，将这个 user model，我们需要实现一个 CI realizable 的方法，也就是可以序列化的，这样的话才可以真正意义上将这个 HDEP 的一个 session 做一次序列化的一个持久化。


那我们来启动一下应用。仍然可以使用 Postman 去调试一把用户的请求，我们刚才调试过了register，那我们调试 log in，将不必要的参数去掉。然后调用set，我们可以看到报错手机号不能为空，密码不能为空。OK，那我们输入手机号1312345678。好，这个时候我们输入一个错误的password，我们可以看到他报手机号或密码错误，验证我们的接口是 OK 的，输入正确的 password 123456 调用 send 我们其实可以看到登录已经成功。我们再调研一遍send，我们可以看到反复的登录也是可以成功的，我们只不过是将对应的这个 HTTP 的 session 给它重新设置了而已。


那我们在这边下个断点，我们可以再触发一次登录请求，然后我们去查看一下 H T E P Server data request better session，可以看到我们对应的这个 session 已经是存在的，可以 get 一下attributes，这个 attribute 就是这个，我们把这个东西抛过来。


current user session，我们可以看到这个 user model 的确是已经被存在了对应的这个 attribute session 当中，也就是我以同样的一个会话，对应的一个客户端的浏览器或者一个 HDB client，只要带上了对应的一个 session ID，就可以获得对应的一个请求的一个内容。


好，那我们实现了注册和登录之后，我们最后实现一把 user Controller 的一个注销操作，也就是说我们的用户有注册跟登录，那自然而然我们还需要一个登出的操作，其实就非常的简单，我们在这边直接 copy 一把。我们实现一个叫 logout 的操作。然后这个 logout 其实不用任何的入参logout，我们对应的 logout 的一个实现方案也非常的简单，我们直接使用一个 better session，点 invalidate 无效掉所有的session。


然后返回一个通时，那接下来我们就借着用户的这个 current user session 实现另一个服务，也就是获取当前用户信息，那我们之前是通过用户 ID 获取过对应用户的一个用户信息，那接下来我们要通过 current user 对应的一个 session ID 去获取用户的一个信息，那我们来看一下 get current user 可以直接通过一个 h t d p serbullet request get a session，然后 get attribute 直接通过对应的这个 current user session 就可以获得用户信息。 return 一个 common result，点create，然后 return 一个 user model，在这边我们需要做一下强转。然后在获取用户信息的时候，我们将对应的这个地方改成 get current user，那至此我们就实现了用户的注册、用户的登录以及对应的用户的登出，在登录态的情况下访问返回对应用户所有信息的这样的一个操作。

