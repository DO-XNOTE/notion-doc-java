---
title: 3-7 单元测试Testing（1658）
---

# 3-7 单元测试Testing（1658）

[image](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/3bf8d54d-5f13-4eea-a455-2e50947b17aa/SCR-20240803-ovza.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664ZDGJUGY%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T232023Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIAn64KqbFaeetkVtEYEN%2B5vPUxRjY9%2Bpahe3KbdihlT2AiArSJ4LUcVB6mbPUFvdR8BSAc1aUkyEN2pKs3EGJPMMSyqIBAjG%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMy2HlbmmMpkHgXZ4NKtwDEN7EhmejGE4WzFlTHV4vmButAbQSZTxUUW79D2bznOCXo2h4IjePG8PezuuCBTV%2Bhbp2LdkgV%2BbI37h9ckXoUAqKOxJpsme%2B6V3x382Q2OIN%2B6HI%2B9VWP9VPIrDryZzY2Cot6RJzagfgCo1yUn4f9WfRKGhZNleJcFf3IYoSNAbI6nFbcn9Kzv04DN8Ih3ZA%2FLNiQnG2HZflIlZkkIsQrIyF5k2JAGmnTal5sfmj8koI46c%2B%2FpEv9RErrsXCubCbjTGTF6ApbkEwX79MuJG8o7jbCKXACgka2RGb9patM4BsUtwI4GukuQk0d2uSouU8PF4QZ4Rxl%2Bq%2Bd2Q784vy5FXB2oTSD0syDf5dWnFP7KkqCPrN3MHJOE9b2YyvcUW4BzZmFe160vMZouJ7wlRH%2Fkj0YKr3hF710r6WKYW7KnAduc3YRnCSbzqHqmpTibB9YPyd0ugM5w3lPaWi%2F6HXJ3RcfYAJiMEordP3tsPa3aKvbgEhw%2Bu%2B7MQAOatbznxiLFNjKB1NgV4AYmV8nu8MIcCueA0ii9CuLAh0axmfdbxhBddrJQZ3Kur3kqfCJmRxnsxdtwhDef5NYGCsx%2Fzp7%2B33awoLCb8Vv2Ocoo2vq177he9W9OYnyTr%2FR6cwt7j%2F0gY6pgHpRpCGgCj03de206N5W5dX%2FJbQzsSUH27%2FcNTeFJ3kva1JKj8Fix6t9QNjUo1Zvn4eJ4%2BowfRK%2Fh9m0naeELFJv%2BZbgqVQcEn99DQeMInzDWlfJhNquYbHY4Qa%2F45Le1%2FmN4nM%2F4DhFpgqpsUTEukgYKvOjcl3zqlK4ftWHeh8H87G19fZmd0lVhI9FWswUs0XSmvDkmH%2BEulkP6Un91WulpyWhZMX&X-Amz-Signature=d7b9269312400cd726c523a49eeba406c673bb5d461f66f4f59f7ec9d9cb6e8b&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

同学们大家好，这一章节我们来介绍 spring 的单元测试部分。很多同学在开发过程中，单元测试写的比较少，认为单元测试是额外的控制投入，这一点希望可以调整一下大家对这个事情的理解。作为一个普通开发人员，交付的内容是验证通过的代码，这里面的验证通过如何理解？通常我们在代码上线前是要通过 QA 验收的，我们在提测之前通过自己的单元测试进行验证是最高效的一个验证方法。单元特色可以理解为周期短、见效快，它一方面可以减少了在 Beta 环境的一些部署成本，另一方面提高我们开发代码的提车质量，代码提升质量高 bug 扫乃是建立我们的团队影响力的一部分，单元测试它确实非常重要，写单元测试的技巧也非常多，尤其是 spring 跟我们提供了很多方便的单元测试工具。


接下来这一章节我们来介绍 spring test 的一个模块。介绍完 test 的模块，我们去重点了解一下 spring 基于 test 的一些常用的注解，以及。最后我们来介绍一下 spring 的一些 test 实践。首先我们来看一下 spring 的 test 模块介绍，在介绍 spring test 模块之前，我们主要介绍的内容是 spring 的一些 mock 对象与它一些测试的体系。另一方面就是我们介绍一下基于 spring 提供的一些测试注解，还有测试的一些工具类。


你现在切换到 spring 源码里面看一下 spring test 这个模块儿的结构，好，在这里面我们可以看这个 spring test 模块儿，它其实首先看一下 spring test 的一些依赖，这里面 spring test 里面的依赖只有这个 spring core，它是一个编译级的依赖，其他的都是optional。对于 spring test 它里面支持了各种第三方 test 的集成。其实我们在引用 spring test 的过程中，我们一般是使用 scope 为test，具体我们是基于 spring 的 Dunit 进行 test 或者 test ng 等等，这些都是我们一个可选的效果。


从这里面我们可以看到这里面有对应的丢你特和丢你的丘皮特以及 test NG 等等这些常用于单元测试的一些工具，下面还有一些基于我们测试使用的，像这里面是 ITPL unit，一次 Admil unit driver 以及我们对于页面解析的一些集成测试的操作，下面包括一些像 Jason pass 对于一些解析相关的一些内容。


这里面还有 react 的 test 相关的依据，就是我们在做一些显示编程的时候测试的一些方法等等，这是这里面的一些依赖效果。我们注意到就是说它都是一种 optional 的方式进行可选，它不会把这个依赖传递进去，只有我们在业务里面真正需要使用的时候，我们可以手动的去把这个引入进来。


好，接下来我们来看一下整个 test 模块，这里面它是在整个 spring framework 下面有两个报，一个是基于mock，一个是test，对于 mock 里面我们容易理解，它里面的内容主要就是我们用于模拟的一些对象。这些 mock 对象主要是为了在我们单元测试里面不容易构建真实的一个对象，我们就通过插桩 mock 的方式快速把对象构建出来，方便我们在测试的过程中运行。


首先 mock 里面几个比较重要的图片，就是我们跟环境相关的意思。首先这里面是 mock environment 构造我们的一些环境信息，这里面是 mock property source，也就是通过 mock 的 bus 构建属性文件的一些设置信息。我们可以看到在这个 mock 的环境信息，它是继承了 abstract 的 human 的，通过这里面我们看到它其实跟我们这里面正常的这个emotor，它是处于一个并列的关系，在这里面它是跟 stand in 的我这里面 mock in 的相关的一些信息，我们可以看到对于这个里面的它有哪些特殊的地方，我们可以从这里面去看一下。


首先它主要是继承父类的一些信息，这里面我们可以看到这里面它可以通过 waits property 进行对属性的一些设置，也就方便我们快速的去使用。下面我们看这里面还有 HTP 相关的，以及 GNDI 和 YY 相关的，对于 GNDI 相关的内容，它都已经标记为不推荐使用的状态，之所以不推荐使用的，是因为现在有一款更好的第三方的simple， GNDI 可以作为我们的测试使用。另一方面是 GNDI 在现代开发过程中其实使用已经非常少了。好，这里面 GNDI 我们就不再推荐使用，这里面是 LTP 的。对于 LTP 我们可以看到最明显的是跟 mock 相关的一些信息一样， mock ITP input message 和 mock ITP output message 也就是对我们的数据传输的输入输出的一个校验。


这里面我们可以看到这是跟 client 相关的，这里面是 mock client activity request 和 mock client activity response。当我们来构建 spring MA seed 一个请求的时候，我们可以通过 mock 相关的一些信息。这里面还要跟 reactive 相关的，也就是我们在做显示编程的时候，它对应的这个 request response 对象是有一些区分的，我们看 Web 里面，这里面我们可以看到它是跟我们在 Server light API 定义的这些 API 一个对应的关系。这里面我们可以看到跟 cookie 相关的body，我们的 mock body 以及异步相关的一些操作，都在这里面有一个对应 mock 的体现，包括这里面的 filter configure， filter chain 等等。


如果说我们涉及到对应的 Web 开发里面需要 mock 对象的一些内容，我们可以到这个包结构下面去找对应的一些信息。通常我们也可以通过在我们 idea 里面去输入 mock 的 EA 提示的话，找到我们对应的内容。


其实这里面我们会看到对于 mock 的ITD， serverless request 和 mock 的 serverless response 其实是我们使用最多的，下面我们再看这是我们整个在 mock 里面的一些信息，我们看到 event 和 HTTP 相关的以及 Web 相关的内容。我们打开这个 test 相关的内容，它其实这是跟 spring 单元测试里面扩展的一些 API 可以实现。这里面定义了些注解，可以看到这个注解，在这个报警下通用的一些注解，这里面有 copy 的 charge 跟我们事务是否提交相关的，这里面是比如说衣服 profile value 就是跟我们 spring 定义 profile 相关的一些信息。后面这里面我们可以看到它有一个 repeat 和rollback， rollback 跟 commit 是个对应的关系， repeat 是一个重复执行的效果，同时这里面 time 的结局就是我们在设置单元测试的时候，如果说执行超过某个时间的话，那就认为是失败。其实对于 time 的普通unit，它也定义了相关的这样的一些注解。下面我们来看 context 这个包下面里面有哪些内容。


对于 context 里面我们可以看到它有cats，event，g，d，b， c 等等，这是跟 spring 的特殊对应的测试的一些支持。这里面我们可以重点去说一下 event 里面定义这个event，我们可以看到它把整个单元测试区分了几个过程对应的创造几个 event 对象，在不同的时间阶段去触发一个对应的event。


次检，这里面像 off 的 test 卡死 event 和 off 的 test excuse event，这是我们可以进行更多地关注执行的一个时间阶段，这里面还要跟 before 相关的一些内容。同时跟这些 even 的对应的 spring 还定义了一些注解，可以看到这里面有 after test class 和 after test must 以及 before 相关的一些内容。


其实在 GNE 的定义注解的时候，也实现了跟 off 的 before 相关的一些信息，但这里面我们可以看到其实这些 spring 提供的注解，它是在 spring 5. 2 版本以后来提供的这些注解可以看到 spring 它是越来越不满足，只是作为对于第三方实现的一个集成，更多的它开始自己去实现这些功能了，也可能是因为在第三方使用这些注解的时候，有某些条件是不满足 spring 它的整个 TC 环境的一些要求。


好，这是一些疑问的，那么我们来看一下，这里面有跟 GDPC 相关的一些注解。对于j，d，b， c 相关的词，有socker， grabber 对应的，跟 J d，b、 c 数据库相关的。这里面还有对应的事物相关的。可以看到这句非常容易理解，这是 off 的 transex 和 before trans，也就是事物之前和之后相关的一些信息。跟 DUANIT 相关的一些内容，这里面有 DUANIT 4 和 Duani 的丘比特 do you need 丘比带，我们是对应 deal 5 的一些内容。


可以看到，对于这里面 spring 定义了一个叫 spring deal 的config，我们在单元测试的时候也经常会用到它，通过 spring deal 的 config 可以更简短的去配置我们单元测试的一些信息，同时对应的还有 spring do you need Web configure。如果说我们涉及到 Web 模块测试，也就是 spring MV seed 车次的时候，可以使用它。


spring IA during the Web 和 during the computer，它的区别主要就是在这里面我们可以看到它有一个对应的是 Web APP configuration，就是指定一下 resource POS，这里面我们使用基于 mail 的结构的开发的话， resource POS 指定的目录也就是 s r c main Web APP。通过这里面我们应该要理解其实这个 spring Jane 的 web config，它这个注解其实是跟 spring Jane 的 config 与 Web legacy configure 这两个注解的一个组合的。


注解。好，我们接下来看下面的这里面是跟我们 Web 相关的一些内容，对于 Web 相关的内容它提供的也是比较多的，我们刚才看到这里面是 Web APP configuration 这样一个组合，它也其实主要是说明一下我们当前测试的一个目录。好，我们跳出关闭这个 contact 包，下面我们能看到是 GDB CU to Web 相关的一些内容。
GDBC 下面有一个 GDB test utils，这里面它提供了一些，主要是我们在测试的时候可以了解一下这个表里面的一些信息，可以看到这里面有获取表的一些数据的信息，包括是删除表里面的信息等等。在 delete 或删除的过程中，我们还可以对应的查询的是支持一些表名和一些条件。下面是 DELETE 的信息，也是我们可以支持一些表名和表名的执行的一些条件。看到这里面 DELETE from table where，也就是支持我们的 where 条件语句。


下面 UTILS 提供了我们单元测试强化的UTO，我们可以看到这里面有 AOP 的一个 test UTO，可以通过这里面获取到当前对应的代理类一些信息。还有下面我们可以看到这里面一个 reflection test UTILS，主要是基于一些反射方式去执行的一些信息，我们可以对于属性进行一些设置，包括我们在执行一些 invoke 的master，也就是对于方法一些，执行一些操作。


下面是跟 dient Web 相关的内容。这里面是 model and view 类断言的一个类，一个工具类。因为现在我们基于 JSON 的话， model view 使用的也是比较少，这里面有跟 throughout 相关的一些信息，这是比较重要的。我们可以看到这里面有 mock m v c，也就是我们在做单元测试的时候，通常会需要这样一个 mock 对象，同时我们通过 mock m v seed builder 来构建我们的 MOS 对象，这里面是有 m a C result。当我们执行完成以后，会得到这样一个对象，这是我们跟我们单元母测试模块里面的一些内容。


好，我们回到PPT，接下来我们来看一下跟单元特斯常用的一些注解，这里面介绍的这些注解刚才我们也有一部分是体会到了，像 spring doing 的 config 和 spring doing 的 Web config，刚才我们在源码里面已经看到了下面还有一些 test contract，以及一些嵌套的这些 test configation，就是辅助我们在做单元测试的一些扩展。
这里面还有一些像 enable 的 if 和 disco if，也就是当我们在写单元测试的时候去做一些条件的表达式，就是说满足某些条件的时候，我们来进行单元测试，如果不满足的话，这个单元测试就忽略执行的情况。下面 activity profiles 则我们在单元测试环境可以快速的指定一下我们当前是环境的profile，下面是这里面介绍了几个只有你的丘比特的单元测试类。首先这里面这个 add test 是我们使用最多的，我们会在对应的 test 方法通过它进行注解。这里面有对应的 before all 和 before 一词，即 off 的 or 和 off 的意思，它是什么意思？这个 before all 是在我们执行所有之前需要执行的内容，对于 before all，它修饰的对应的执行的内容需要使用静态的方式去执行。


之所以需要静态的，是因为我们在 before 21 就是所有方法执行之前，我们在这种过程还没有对这个类进行一些实例化，也就是并没有构造它的对象，所以我们需要静态范围执行 before 意思，它的意思就是说在执行每一个单元测试之前要执行的内容，在这个阶段它是已经把我们代言测试类进行一些实例化了，所以说它可以不需要我们用静态方法来标志这里面的 off 的 or 和 off 的is。它的功能是跟 before 对应的，这里面的 time out 也是为了标明一下我们在执行的时候跟这个方法限定一个时长。
好，接下来我们来看一下 string test 实践的一些案例，还是主要的内容就是培养大家的一些单元测试的意思。另外就是说我们在写单元测试的过程中，很多情况下我们是输出我们的日志，去看我们的日志信息是不是满足我们整体的条件，但是更推荐大家使用断言，用断言的方式去校验我们的结果是否正确，因为我们如果说只是打印日志的话，是需要要求我们肉眼的去分析这个日志，证明我们的结果。那么推荐断言，它可以通过断言的执行结果来判断我们单元车是否符合。


我们来看几个单元测试的案例，因为我们在演示这些代码里面都会使用到我们的单元测试，所以说我们就不再单独为我们这个构造一个单元测试去出。大家演示我们可以看一下在 spram VC 这个模块里面有对应一个 Demo control test，可以看到这个单元测试，比如说我们在这里面，因为它是在做 m a C 测试的时候，我们首先是需要构建一个 mock m a C，这个构建 mock i m a C，它是在什么时间执行？就是我们在这里面是 before each，也就是说我们在执行每个方法之前，它会执行对应的方法构造我们的 mock IMC 对象。这个 mock MC 对象是通过 mock m a C builders 去通过 Web application context set up，指定当前的一个 Web application context 构建出我们这个 m a C 对象。对于我们这个 demo control 这个 test 类可以看到这里面我们使用了 spring during the configure，同时我们还引用了 Web Bison configure reason。根据我们刚才的介绍，我们可以通过一个注解，也就是 string during the web configure 来替换这两个注解的一个组合。


接下来我们来看一下我们在执行单元测试的过程中，我们首先是构造一个对象，这里面是 mock 出我们的 HTP Server LED request 的这个对象。在这里面我们在 mock 的过程中，我们用到了一个 mock m a C request builders，这里面我们通过 builder 去构造对应的一些属性，比如说我们首先要 get 指定的目录，指定的 URL 是 demo get 比 by name，同时配置了一下我们的一些参数，以及我们的对应的 media type 相关的信息。也就是我们构造出这个 mock 对象以后，通过我们的 mock Mac，这个 mock Mac 构建的平台去perform，也就执行我们的信息，也就是我们通过 mock Mac 这个对象执行我们对应的 mock 的一个 active survey request 的对象，得到一个 result accents，也就是得到我们的 result 结果。得到这个结果了以后，我们需要去做一些断言的操作，在这里面是因为 rest accents 对我们的断言做了一层封装。


我们在断言的过程中，首先是 result accents at accept，也就是说我们在执行的过程中我们期待的信息是什么呢？首先我们期待的返回状态码是states，一次OK，我们知道一次 OK 对应的 HTP 状态码就是200，同时我们还是期望返回的内容，它符合一个 JSON 格式，也就是 json 格子指定的 JSON pass 对应的是name，它进行对应的我们的机密的一个属性里程。同时我们满足这些断言信息以后，把我们的想要的内容进行一个print，也就是打印输出。


通过这里面我们可以看到这是我们常规在写 SPRAM v seed 单元测试的时候需要做的这些工作。通过这里面也就我们可以去跟大家介绍到我们在做单元测试的一些常用的信息。介绍这个 Demo control，它的演示的过程中相对比较简洁一些。我们通常在写 control 的时候，一个 control 它通常是依赖 service 的。如果说我们单元测试并不关心 service 它的情况，我们只是可以 mock 一下 service 的返回值，这里面我们可以看一下前面介绍的这个对应的这个 MVC 模块儿，这里面我们可以看到它在测试的过程中，我们对应的这个方法，也就是说我们的这个超重，它依赖到了service。


对于我们的 user control net 对于这里面的这个 welcome Controller，它是依赖的 user service 这样一个服务。那么我们在做 Controller 层的验证的时候，其实我们更多情况下并更不关心 user service 差返回的结果是什么，可以在这里面通过 mock 的方式去模拟。当我在执行 user service find by ID 这样一个方法的时候，我跟它固定的去让它 well return，也就是说把它执行的操作和返回值固定起来，这样的话我们就不关心 service 的内容了。


这种方式也称为插桩，也就是说对于我们在测试 welcome control 的过程中，把它的撤词范围定在这个 welcome control 里面。对于我们外部依赖的 service finder by idea 这些操作，我们通过插桩的方式把它拦截起来，也就是我并不关心 service 处理的内容，我只是把我依赖的这些内容都通过 mock 的方式去局限起来。这是介绍了我们在单元测试里面常用的一些方案。关于单元测试的内容我们就先介绍到这里，同学们，我们下一节再见。

