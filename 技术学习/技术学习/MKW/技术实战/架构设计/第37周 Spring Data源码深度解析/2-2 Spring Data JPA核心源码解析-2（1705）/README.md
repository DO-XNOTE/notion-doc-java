---
title: 2-2 Spring Data JPA核心源码解析-2（1705）
---

# 2-2 Spring Data JPA核心源码解析-2（1705）

[image](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/af1ebffc-dd95-432a-b0ab-dabf8cbcb527/SCR-20240814-hqeh.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YMVRW2LJ%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T232133Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDANxHumJVRLbaCKcLNepUwB4pi3XM7MjDg8tZoBpyzwwIhAKNixupFT3fphVmk2miq2kTlkwBGqQgZzU7ED2aN0xatKogECMb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgxNaBBXzqP8TQs%2F9f0q3AMETpkHoosr3%2BEgI9mZhJp8tbxLC%2FBXseZqIXGtrK0dVr1t1CvgLsCQDmt%2F8IgXhShQ5HJgAkEY9XFgaYpsQWIIfcrxIY2y60WvTcyewwHL%2FS9S%2FcLKHcoUdFXQNP0i757n8HMRICcxBPBxQq6y45zxoXf%2FrnJxr5QvdxmVw%2BUzGBi%2BD4%2FqMRGydsXOhQw%2Bm2XorIv6PgQGLPB1lX93HHYyFi8R2KMCMjykIVm0nh4DiILMv7LoNLcifx%2BwMLVaY5QBWCw8edTRsz8ZL6wehO%2FGb6SnFBAnCdYHUiLwjJ9ozhK7K9ZRUMXNdGfs5ec3FxXzprsPjjGHt%2BuL%2FwYe17XTZ5Qqhm2xK8NyschWoIMT1LSaieldpbxjnt3D5hHC5rNnoW9lvU7CFNB%2FcXDZHAsD3X5st4doBV09MVnbixkQ3Ghw0T8%2BMWTl%2FOiSFVwRYuxmg6ITPJpTuaHELWeFYYqLSUPeC8P589V6g%2Fk5J4Dhyw56RIntVynALxYm8PMdFfmLTvoHIHz6Zg8BQDFRvVMN4JKzdz1wSYcNITpiFs72c2%2FHw4u23yGDYKIle6%2FsuSIl6QC7310ata6y0hzix0rMD1nX2mbaRctvXSKPmnGatn9Riv1D6fUMrGRBxTC1uP%2FSBjqkAVCHy1MDC03cGD23YEGdpZa89quMOssilOg7vrONx51hrGKI%2FTMe3OLw2Q7ii5cVXyPebHZMgwALG8XK5L6wySXSIruLaa%2BCnD5PFIccvmpsRngYugJ3RaMKs6A%2FInAcGLcDYFoaNjSpLZtcMLp0SRcjJBTKFppItZHxdszBtpzAHxkWjjj4sXYTfUUmF9OyXoR2SW9K0dPXagcv%2FSQ3btXa538o&X-Amz-Signature=ccdd3b3d9c101373c7fb3a88200c28ba18f48c1e9c5447f60455c7b9972be212&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

这里面我们初始化流程，我们介绍基于 string boot data GPT during the starter 的初始化流程。首先第一步它是通过 GPA repository 的 auto configuration 作为初始化的条件，那么初始化的过程它对应的 auto competition，它依赖了一个register，也就是对应的 JPA reports register，那么这个 register 跟 string day 的 GPT 里面的那个同名的 register and 包不一样，它实现的逻辑也是有些区别的。


对于这个 rejection 里面，它定义了一个是我们的 GPT configure extension，这里面我们也理解 GPA report 有一个配置的扩展，另外它也用了也就是我们的 enable GPT report，其实我们通过 auto configuration 去实现了对于这个 enable GPT report 这个注解的开启，那么其实这个在执行的过程中，这里面的 GPT request 它是继承了这个 abstract reporser configuration support 这个 source support，其实这里面它会通过一个叫 repository configure 的一个delegate，所以我们可以立了一个代理这个delegate，我们进行委托给他去创造我们这个repository。那么这里面我们看它接下来会使用 repository being definition builder，我们可以看到它是 reporsterbeing definiter，通过这个 builder 构建一个对应的 repositer being definition，那么其实构建的过程中它最终是使用到了我们的这个 GPA report factor bin，再通过构建对于这个 GPA report factor bin，它也依赖到对应的 report effective being support 去进行后续的一些处理，其实在处理的过程中，对于我们常规的这些正常改查方法，它会使用 simple GPT。


对于一些比较特殊的一些，比如这些命名的查询方法，它会借助以 Pod tree 这批 query 里面的 Pod tree 进行我们对于方法名的解析出我们对应的，如果说它匹配到某一个正则表达式，也就是这里面，比如说我们是 find by 或者是 count by，或者说其他的一些我们约定的这些前缀，那么它就会解析成一个命名查询。


那么这样的话我们就会被把我们定义的这个 user reporthering 生成一个对应的代理，那么它根据这个代理和对应的方法去找不同的实现去执行。这里面就是指当我们调用这个 user report 它底下的一个代理类去执行。我们例如像简单的 save find by ID 这种简单的查询的时候，它会去通过 simple GPT 里面的实现去代理去执行。那么如果它去执行 find by name 这样一个操作的时候，它会通过我们的 name query 对应的属性去找到我们这个 name query，根据我们的 named query 生成的 SQL 来去进行执行我们这样一个查询语句。


好，现在我们来进入代码去看一下，代码是，嗯，一个我们通过 debug 一个看一下执行的过程，我们看一下这里面我们定义的这个单元测试类，对于这个 user repository test，我们其实就是去进行单元测试执行校验我们的 user repository，对于这个 user repository 我们是一个普通的继承了 GPA reposure 的一个report，一个 user report 的这样一个接口。那么这个接口就是我们去验证通过 GPA 进行 CID 超库的一个测试用例的一个reporter。那么对于它我们这里面实现了一个简单的查询方法，这个查询方法是 find by name，对于这个方案的 by name，我们它最终会生成一个命名的查询语句。


那么在这里面我们去看一下我们这个单元测试类的执行过程。我们看这里面的 user report test，它是使用了 did GPT test，其实这个 d 的 GPT test 它是使用了对于 string Boost 的方式进行启动，所以说最终我们这个单元测试类，它执行的过程中它是使用到了 GPT auto configuration。那么这里面我们去看一下 GPA repose auto complication，这是我们第一次去打开这个 GPT auto configuration，给大家去介绍一下。


对于这个 auto complication，它实现了一些条件，比如说首先它是需要我们的上下文依赖 data source，同时也需要出现 JPA reporter，也就是说我们需要有对应的数据源，也依赖了对应的 spring day 的JPA。同时我们看一下这里面有个unmissing，也就是说我们的 GPT positive taxi bin 并没有被实例化，也就是我们容器里面并不存在这个bin，以及对应的 GPT configure extension，这是什么意思？也就是说其实我们并没有手工的去通过 add enable GPT reposit 方式去初始化它，这样我们就会使用我们默认的 string date GPA 对应的这个 starter 去初始化。


后面我们可以看到这里面一些 property 的一些条件校验，这里面有 string d 的 GPT rate，这里面对应有一个属性是enable，那么这个 enable 的默认值它是true，也就是默认是打开的，如果说这个属性不存在，它也属于 true 的一个情况。同时这里面是有一个 import GPA reposer redesire，这就是我们一个关键的信息，待会我们点进去看一下。


同时我们可以对于 GPT rate auto configuration，它初始化的过程中它需要 off 的，也就是它需要在 Hypernet 这批 autocomicurring 之后，这里面以及是我们的一个任务执行器的 auto computer 之后，这里面它实现的逻辑是什么呢？如果说我们要是配置了是延迟加载或者是懒加载的话，我们这里面会构造出一个异步执行，也就是说我们的一个线程池去异步执行，这里面我们看到它去配置了，去判断我们当前的条件它是不是延迟加载，或者说是懒加载的模式，那么如果说它不是延迟加载和懒加载模式，那么它就会在我们容器执行的过程直接进行。


对于 reporter bin 的初始化，我们在正常开发情况下，其实我们没必要去开启这个对毕业实例化的栏目加载，只是我们把这个时间转移了而已，对于线上我们还是希望当我们程序启动完成以后，把我们所有的 b 都实例化完成，这是我们期望的一个效果。


那么在这里面，对于 auto comprecation 说 import GPT report just 我们可以看到这里面，大家切记一下，这里面有两个同名的类，一个是我们对应的是 spring date J p a 下面，另一个是 spring boot auto configuration date J p a 下面，所以我们这里面是用的是对应的 auto configuration，也就是 spring boot 自动装备的这个 j p 率好。
那么在这里面我们看到它其实也是继承了 abstract 这里面的 reporsory configuration source support，这个跟 string data GPT 它实现的逻辑是一样的，在这里面首先它有一个对应的我们启动的模式，其实我们重点关注的是什么呢？是这里面的是 GPA repository configure extension，也就是这里面这是个配置的，我们那个配置扩展的一个类。其实我们再向后看，这里面是我们比较关注的一点，也就是这里面定义了一个静态的 class 标记，也就是我们的 enable GPT competition。我们一个开启大家了解了我们的 GPA reposter 的 auto configuration 做的事情以后，我们还回到我们的单元测试类，那么在这里面我们通过启动我们单元测试类去先去感受一下我们初始化的一个过程，它都涉及到了哪些API。


那么好，我们现在我们这里面会两个单元test，它分别是调用的是 find by ID 和对应的是 find by name，当然 find by name 我们并没有传入参数，对于 find by ID 我们去验证，它最终会通过 simple ZP reporter 去执行。对于 find by name，它会通过我们的 name 的 query 去执行。那么这里面我们第一步先去验证它对应的初始化的逻辑，那么它查询的逻辑我们待会去介绍。那么现在我们开始进行通过 debug 的方式进行启动。好，我们看现在我们启动，在这里面我们看断点到哪儿，这是对应的是我们 GPA report config extends，这里面我们去 register bin for root，也就是说我们在这里面扩展配置是需要把我们的这些 bin 注册进去，那么注册这个 bin 的过程，也就是注册我们对应 reposure 的一个过程。好，那么我们现在这个断点我们跳过，现在我们执行来到了 repose reconfigure delegate，那么对于它就是我们初始化我们必应的一个关键的操作。那么在这里面我们可以看到这里面我们会定义一个configuration，那么这里面我们去下一步执行，那么执行在这里面我们会构造出一个 configsion by repose 的name，这里面会通过 for 循环的方式去获取我们对应的这些 repository 的信息。


好，那么我们现在去把这个 configuration 进行一个解析的一个执行，我们可以看到在这里面我们会通过这个configuration，它那个 reporsory interface，也就是说我们这个 reporsory 的接口名称去进行一个做一个k，同时这个 configuration 它作为我们的一个 value 进行一个存储。我们可以看一下对于 configuration 这样一个当前的这个对象里面的实体情况。


对于这个 configuration 我们可以看到它的信息，对于它的描述信息，这里面的定义信息，我们可以看到它的 Bing class 就是对应的是我们的 user reporter，这样我们知道其实它现在已经扫描出我们定义的这个reposure，那么得到这个 reposure 以后，我们可以看到现在要做的事情是进行一个通过 being declining builder 去构造我们这个 being tation。


这个构造的过程其实比较复杂，我们可以先跳过执行好，这里面会判断一下。嗯，这个 BD 它是基于 XL 定义的还是基于注解定义的？那么当然我们现在并没有用XL，所以它不是基于 XL 的，这里面会有一个后处理，那么我们可以看一下这个后处理的逻辑是怎样的。其实这个后处理比较简单，它只是在 builder 里面添加了一个 property 的 value 属性。好，我们跳出这里面会对于这个 Bing definition 进行一些 source description，也就是对于这个配置元数据的一些描述。现在它会通过 bin definition 生成我们对应的 bin name，那么 bin name 我们比较容易理解，我们可以看到对应的 bin name 就是 user reposer。


接下来我们来看一下对于这个 being tunation，它会设置一个对应的叫 extra being object type，我们可以看一下对于这个设置的过程，它会从这里面去获取到 configuration guide repository interface，这是说明什么意思？首先对于我们这个 being definition，它要返回的对象是因为它是通过一个 factor bin 去构造的，那么对于这个 factor bin object，它的类型是我们这里面指定的 report INTERFACE，也就是说 being definition 它对应的一个实例的类，就是我们的 report INTERFACE 的一个子类，也就是我们的 user report 的一个实现。好，那么我们继续。嗯，下一步这里面会把我们这个 Bing definition 注册到我们的容器里面，你就注册完成，那么完成这一步的话就其实是注册完成了，注册进去以后，其实后面还有很多事情要做，其次要做我们实例化的工作是最重要的。


那么好，我们现在去跳过这个断点，它会执行到我们实例化的一个断点，在这里面我们会看到现在已经执行到对应的 GPA positive factor b，也就是我们通过 GPA reposure factor b 构建我们这个对应的 GPA positive，那么这里面我们去也是跳过这个断点题型，下一步这一步到哪儿我们可以看到它是 GPT TAXI b，在这里面有对应的我们的一个叫 do create report factor，也就是说开始创建我们对应的这个 report factory。好，我们下一步我们也是跳过这个断点，我们直接到这个创建的逻辑里面，这里面我们看到在 ZPA reporter factor bin 的这个类里面，通过我们的 create report 创建出一个 GPA positive factory。我们注意一下这里面的命名，这是一个factory，这是一个 factor b。对于这个 factor b 它传入的参数就是我们 JPA 的一个关键的一个实体管理器，也就是 entity manager 这里面 entity manager 里面我们看它设置了一个像 entity Paas Resulver，这里面是一我们的一个路径的一个解析器。我们现在向下继续，这里面我们看它会去判断一下我们的 query master factory，如果说我们由自定义的话，它会把默认的覆盖掉，如果没有的话它就会跳过。


好，那么我们现在是咨询我们到下一个端点，在这个端点我们可以注意一下，其实这里面是做什么操作？这个操作是 look up query，也就是说去查找一下我们的这些对应的查询，我们的一些查询方法，这里面就是 name 的query，就是通过命名查询的方法，这里面我们可以看到它是一个pair，也就是一个我们可以视为两个值的一个对象，那么这里面那个 pair 这 pair 通常我们会分为第一个对象和第二个对象。第一个就是我们是must，这个mess，我们可以看到对应的就是 find by name 这样一个，就是这个方法。那么对于它的解析出来的内容是什么呢？我们可以跟进断点进去看一下，在这里面我们去跟进来，那么我们看一下这里面的两个现在还没有进去，那么我们现在继续跳出。


好，我们现在到这里面，我们现在去点进来，那我们看这个 fast 和 SE second 就是第一个对象和第二个，第一个参数和第二个参数，那么第一个参数是一个我们的这对象，也就是我们的方法的对象。那么第二个参数它是一个 part tree g p query，这里面我们可以看到其实它就是通过 Pod tree g p query 来进行对我们这个命名的进行解析。那我们可以去对应的这个方法里面看一下，看这个类里面看一下这个类里面是一些什么事情？这是 Pod tree GPT query，其实我们看到它是继承了 abstract GPT query，其实对于它的一个实现的过程，这里面最重要的一点也就是 port tree，那么通过它去真正解析我们这些命名参数，我们可以在这里面我们点进去 part tree，在这里面它是实现了一个stringle，也就是它可以支持一个流式处理。这里面默认是 all port，也就是它是一个或的关系。


那我们可以看到这里面的这些数据，我们就明白了这里面这些常量，首先我们可以看到它会做哪些事情，这里面像 find read guide，query， search stream，那么所有的这些前缀它都是对应的一个query，这就是我们的一个查询前缀的一个匹配模式，这里面还有个count，也就是我们获取我们 count 计数的一个体系。那么这里面是否存在，这里面还要 delete 和remove，所以说这是我们所有的这些命名参数所关键的一些信息。那么这样的话，我们就大概了解我们这个命名参数解析的逻辑是怎样的。我们可以看到下面会有一些真正解析的一些复杂的一些操作，那么这里我们就先不去细看这些内容了。


好，那么我们回到这里面，我们去执行跳过，那么执行完这一段儿的话，我们看它现在是执行到我们对应的一个 sample GPA reportery，这说明什么呢？我们当前的常用方法是对应的一个 find by ID，那么 find by ID 我们这里面是通过我们的单元测试的执行，执行到这里，好，我们可以看到这里面我们是用的是 find by ID 这样一个，我们可以理解为它是一个简单的一个方法，这个简单方法也就是指我们对应的是这里面是指 simple DP report 里面存在的方法。那么现在我们执行的过程，我们可以看到它就是一个普通的一个 DPA 操作了，最终它会调用我们这里面的对应的 entity manager 这里面的 Intel manager 去 find 我们指定的类型和ID，去把我们对应的对象获取完成。


那么我们现在跳过我们的单元测试，那么现在我们的执行单元测试进行执行完成，现在我们可以看到我们已经能获取到我们对应的 user 对象，这 user 对象也就是我们看到对应的是ID，是一，name，是 name 0 and 等等这些信息。好，我们在这是我们执行完成，那么这是我们可以理解为我们通过 spring d 的GPA，它启动跟执行的一个过程，那么对于它执行的过程，我们这里面对于这种简单方法执行是比较简单的，我们可以在这里面也简单地过了一下。


