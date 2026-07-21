---
title: 1-4 Spring Data Commons架构设计-2（0759）
---

# 1-4 Spring Data Commons架构设计-2（0759）

[image](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/71719dcd-d1db-4560-85ae-859672456e11/SCR-20240814-hnho.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YFYWQYEZ%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T232131Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIDxroTLRdQ1%2B4CL0uoowmVbu9JG8MZd2dUneHeV81QCQAiEAo8QojZObKUCbBYCbUSXkZ%2BsdKMA4pb511y%2BWZahlExoqiAQIxv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDKqF%2BuRFRXJq2D0COircA8f9LZ4OGLszfU5LPX01DIJ0Vh8g78M9F0s9ysmQ2zI4uc2qLNPPNwIoG3LZOkk8orPlpcuzTfa7qx9Op2OHSSjBoHQikkxAC7Xmoga9clLMjQWwPqE%2Bj37al3xodlxE%2FZMNBMG18vMZFe8pkyBHDFyTV4B6XfzHQOO9tJVmxml1mlsaa2XSzBAmt6fBJJkw54lVaOgDWyjfQDqcL7PM%2FCuB2oQaeiYufMx4%2BfRW3crtJg6uDWABUfACPmP3UgTDbAyRb9fZPKThW0xG1IrXt3jgtH3%2B6nppHMzeudBL9kumbcTlGK1WwrbLd%2Bwazo7PJw6P%2FB42mZ3MGPWSF7eZ%2BMP9SLGLuU%2Bwc0xL3ARUZPmNN%2BmvtRInr7vBBWoGqe4E2oqjVF6T4xrVmjReREHpwEkxId1Hwueblcxeq8hTjpXRp04HaBCtoIkPxGwhk6zp7TTUwr%2FtVgivcsBBFV7vyklrecmi98ad0COS4SWITybI%2BcMquqOMFU0MqiDBvF%2Bo%2BfM0zskyNqsQR3hqlkymGD3QcsF8b7ZiGhlZ9jBPbZAgSsDwfs7y9qAZwHqdYXtDoi80Ouu2huCQ05Bq0kW3Thy7vwkUJeiV7Jo7wdBvrwplqtlunijguxH5ME52ML67%2F9IGOqUB9iI2PNfNZkJN1x9sXwiWzNnLF9l0gUTcK46hSofeMHVmXmYy4xGxv4ziIT3O29ZTI9PP8Kel5Vi%2BSnb%2BwzK0lfEVzd71%2FMstrEg6mMh9OTaFx9YwolfX2vQq19UZ4ZN%2FXuGwT49ayDzhmR5xrg5vVCLsGAPFkfUxWywZpgzVmCe8lxL%2F4rcEc5xqb6ray6S0%2B0xkLc%2BEAEqNjQzQjfaaZ%2FbqbHTm&X-Amz-Signature=69f55d2745fa84a00b3cc58b99e78b73fe0f390d4b3cefc8c7d32cd1ed116d74&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

某人认识完我们的 Comos 源码，接下来我们来看一下是斯平地的 GP 的一些演示，我们基于斯平地的 JP 完成一个公众模块的增删改查，这样的话让大家去方便理解 spring date GPT 给我们带来了哪些方便。现在我们切到我们的公众模块，在这里面我们基于 spring date，我们新建的一个功能模块是 spring date study，也是我们对应的 so case 模块，里面有对应的各个模块的实现，这里面像 index 和DPA，下面还有 MongoDB 和 Redis 等等。我们重点来看一下GTA。


如果说大家对于 string 部的课程还有印象的话，其实这个模块跟我们在 string 部的工程一个 model 模块是非常相似的，在这里面我们首先看一下我们的 palm 文件， point 文件里面第一个引入的也就是我们的 spring store 的 date JPA，基于 spring put 的 starter 来引入 date JPA，当然也可以直接引入 spring date JPA 来手工实现。
我们对 spring boot 已经比较熟悉了，所以说我们还是推荐使用 spring boot starter 来引入。底下是我们对应的数据库，这样使用内存数据库HR，下面是我们用的数据库连接词是阿里巴巴的德路。一。底下我们看我们引用的是 spring boot 十大的 did rest，也就是我们对应的 string did rest，它底层的一些依赖，这里面会有 string star start Web，这个其实会被 string the rest 间接的去依赖进去，这里面我们注意一下引用的是 string date， rest SLX pllora，它就是给我们提供这个 web UI 的一个操作。
好，下面是我们的AQ，ator，朗 book 等等这些常规的一些内容，这些我们就不用再一一介绍了，现在我们可以看一下我们程序的一些信息。我们知道我们引入了 Sprint 的GPA，可以看到我们首先我们的用户对象，也就是user，对于这个优势对象，我们定义了常规的一些属性，比如像 ID name， lucky name 和一些状态等等，就是我们模型的一些概况。大家要注意一下，这里面我们使用的像 entity table 和ID，它都是对应的我们的 Java persons 下面的规范的一些注解，这里面也就是 GPT 的一些注解。


我们接下来看 report 对reports，这里面的实现非常简单，这里面我们只是定义了一个空的 user report，它继承了我们的 DPA report 这样一个接口以及这个接口。这里面我们需要指定一下我们的对象和这个对象对应的 ID 的类型，我们可以看一下对应这里面的构造的方式。 t 是对于我们的 user 返回一个 user 类型ID，也就是当我们 find all by ID 的过程中，指定这个 ID 的结合或者是 find by ID 都会指定对应 ID 的一个类型。这里面我们回到我们 user positive，我们可以看到整个这个过程是非常简单的，那么这里面我们还是指定一个注解，就是 positive 注解就说明这是一个对于数据库相关操作的一些内容。


后面是我们电影的一个 user service，这个 user service 跟我们整个隐私其实没有多大关系，通常我们来设计一个功能模块的时候，我们会进行分成，这里面我们有我们的 DEO 层和我们的思维层，对外层，还有我们的一些 Controller 层或者是 Web 层。那么这里面对于 user service 我们的一个实现，也就是 user service 的 m p l，它依赖了 user report，实现了 find by ID 的一个功能。


好，这样我们去看到整个这个工程的一个简单的结构，这里面是我们 spon 布的项目的基础的一个启动类，这里面也是实现的非常简单，大家注意一下，这里面我特意定义了一个config，也就是我们初始化数据，因为我们系统启动完成以后，如果没有数据演示起来的体验会差很多。


我们在启动的过程中是指定了一下初始化数据，比如一些 init date，我们在执行的过程中，也就是我 after property set 这个 bin 设置属性完成以后，它会进行一些初始化数据的操作。现在我们大概了解了我们这个工程的一些情况，那么我们可以看一下它的执行的一些效果。


首先我们对于一个 spring 步的工程，可以先通过 accuator 来了解系统的一些情况，那么我们通过 accuator 找到了我们对应的 Mapping 操作，这里面执行我们的 Mapping 操作。在 Mapping 操作里面我们看到它里面有很多URL，其实我们更关心的是我们的 SAL explore 这个 UI 它执行的情况，那我们怎么找它？可以我们在这里面去一个全局的一个搜索，在这里面搜到对应的 ICL explore 这样一个包，对应的一个x，对于这个 x 的control，我们可以看到对应的 patterner 和我们对应的或者是Mapping，也可以这样理解。


对于找到这个pattern，我们又找到了些访问入口，我们通过对应的 explore 访问入口可以找到我们对应的操作，这是它默认登录的入口，那么在这个默认登录入口就是这样一个UI，在这个 UI 它还可以设置一些皮肤物等等一些信息，我们可以看到可以给我们切换一些效果，这是我们的黑色的一个效果或者一些其他的一些效果。如果说对哪个比较感兴趣的话，大家可以期望切换到我们的默认的 Leo 的，我们支持是两列或 3 列等等。


接下来我们怎么去演示这个效果呢？现在我们要操作的也就是在这里面去输入 h GPT local host 8080 users，我们简单解释一下，对于前面的我们就不用解释了，大家应该是比较容易理解的，对于 users 这个是怎么去理解？我们可以看到定义的一个对象是 user 对象，对于 user 对象，在 repository 它向外暴露，也就是我们实现 restable API 的过程中，它把我们的user，我们对于列表的查询统一对应成一个复数，也就是users。


我们现在查询我们看得到的内容是，首先我们的参数的内容，这里面是，嗯，配置，这里面的 size 20，我们的 total element，这是50，也就是说我们处死了 50 个对象。我们现在获取的当前页数是 20 页，我们总共的页数是 3 页，可以看到这里面是我们响应回来的一个 response body 信息，可以看到我们简单过一下，这是我们得到一个 json 的一个结构，每一个结构就是一个我们的一个 user 对象，这个我们了解了，我们再看一下，我们这里面可以点击一些分析者的信息。比如说 fast 的是第一页， self 是当前页， next 是下一页， last 的是最后一页，那我们这里面我们可以点击 last 页 last 得到最后一页，可以看到我们当前的对象的数量的一些情况，我们可以看到一些信息，这里面应该是对应的是 10 条记录，因为我们一共50。


第三也就是我们的配置，它是从 0 开始， 0122 就是我们的第三页，它只有 10 条记录。那么同时我们可以在这里面去修改一下分页的数量，比如说我们把它修改为 5 页，修改为每页 5 条记录的话，这样我们的页数就会增多，那页数会变成 10 页。我们可以去演示一下我们分析的效果，比如说现在我们是直接我们执行下一页，我们执行next，下一页我们看刚才是10，现在15，再点下一页，现在变成对应的20，我们再点下一页，那么是25，或者我们是上一页也是对应的减的一个过程。


这里面 self 就是也就是我们当前页的一个操作，可以点一下self，其实这里面数据内容并没有排上变化，这里面我们可以看到它里面有 last 和fast，也就是说我们回到第一页，也就是 name 0，我们到最后一页，这里面是第 45 和也就是第 46 个对象给大家演示了一些毒相关的一些操作。


其实这个 UI 是止血操作的，但是这里面可能因为这个 UI 的效果我们可能不是很明显，我们切换一个皮肤，切换一个深颜色的皮肤，我们看到其实这里面有对应的正三改相关的一些条件，因为这是个列表，在列表里面我们不能对于对象进行一些操作。关于这个 UI 的更多的一些功能可以下面同学再去探索一下。其实这个 UI 我们主要是为了去说明一下，通过 report 直接暴露这些 API 可以进行相关的一些操作。现在关于我们 string seed GPA 演示的部分我们先介绍到这里，同学们，我们下一章节再见。

