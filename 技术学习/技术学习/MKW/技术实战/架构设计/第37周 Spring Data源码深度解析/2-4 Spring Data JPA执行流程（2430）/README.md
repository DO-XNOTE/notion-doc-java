---
title: 2-4 Spring Data JPA执行流程（2430）
---

# 2-4 Spring Data JPA执行流程（2430）

[image](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/8566966a-8698-41e7-9e5a-2cde0e742c86/SCR-20240814-htkm.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664452TS2W%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T232135Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCpfy1E6NLbu0hHhZXGvE1q0vrprY%2B%2FDSEgQRWrjDXqngIgL5XT%2BGYrho0txHdtNJe87vyjIzs2iMiS5WfYDySfz%2B8qiAQIxv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDDHAFqyjC3%2BWG0YQDircA43y%2B2VkMObt6tAp3nS9VtIdLRFkX3e79u1YD%2F5U3gwu9af0B3WMlttrzftz7q1nrsFCc%2FhaIkjpgZTa5dPAebsDs6MDRYA7eW5B9YK%2FX33r7DiRuN7CixqmszJ9CYkffpJ%2BFlyYZChIpJyzvfO2FjTyU29M%2BzWA8QTwrMJM1jlsu0gj2Z7muvife5QmoTaG9otootvI67OdMBY7QzZoTng3qIYAwV70aMlTYnKC2Oc0XP6LPEv6McE6XGyeRBEoOcJb7ukLFS6FOJzvlu7vyf15GrLRtXcs%2B3FbKD3UYz6oILmBLVEQjTgmMDNsJIxiHPJU%2Fh%2BH7g%2FI1CU5F45pkLvw6nl6yfOvM7bXSMR6pWkXd26DqSwqFVYxzBvazp6F5NUDIMdESiHslmxAD5YUqgN1vQRdhJqRl9Dyv63JVKBtl%2FB7GFFgtNeZYj7RZL0Tv%2BSlw16sKXUVzCnPOB9xmkfyaSwjtT55%2FUheNi4t6X4jJCvn1v%2Bp4UaLfYw2XCVscPg1cszIKUySq7tB36Bc72IqDkdSC6qXsttRS5DYK5tg5dpZ8E6qZRtmO6Myohtgq4FL5I8lPpkxO1L7GvYQ0QhdccZIuqVTC2W9GUSic5J69gr1EKINw6KPDwYwMIu6%2F9IGOqUBbyn6ZkdC9Cm4EBC3B0aYWhBYYjmzQ6nVYyf%2Fuu6LkVuC8YIUtJoGoAGkwBQcibHco6H6kcFdkc6KKg7y%2FlL69GFZiylaYJG4WQ0y32FhYpnGAvYxtCL%2F0QmRL67zMgAVhUCumYwDy%2FKliPc%2BpE8dnjCAdl4Gay0MIJIIzT7LY2NMs08ZjnY7wnMkp7wWKlqGNL%2FRiFPbuG09fpVANzv1vJ0QR%2Ftn&X-Amz-Signature=b48907671fe10f4f64cb7febcaeab0a85ea6db8d5d7bbdacc596fd877036c114&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

[image](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/c36db053-e59c-40a0-ba74-9cfb2f8e4ee0/SCR-20240814-hrrw.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664452TS2W%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T232135Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCpfy1E6NLbu0hHhZXGvE1q0vrprY%2B%2FDSEgQRWrjDXqngIgL5XT%2BGYrho0txHdtNJe87vyjIzs2iMiS5WfYDySfz%2B8qiAQIxv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDDHAFqyjC3%2BWG0YQDircA43y%2B2VkMObt6tAp3nS9VtIdLRFkX3e79u1YD%2F5U3gwu9af0B3WMlttrzftz7q1nrsFCc%2FhaIkjpgZTa5dPAebsDs6MDRYA7eW5B9YK%2FX33r7DiRuN7CixqmszJ9CYkffpJ%2BFlyYZChIpJyzvfO2FjTyU29M%2BzWA8QTwrMJM1jlsu0gj2Z7muvife5QmoTaG9otootvI67OdMBY7QzZoTng3qIYAwV70aMlTYnKC2Oc0XP6LPEv6McE6XGyeRBEoOcJb7ukLFS6FOJzvlu7vyf15GrLRtXcs%2B3FbKD3UYz6oILmBLVEQjTgmMDNsJIxiHPJU%2Fh%2BH7g%2FI1CU5F45pkLvw6nl6yfOvM7bXSMR6pWkXd26DqSwqFVYxzBvazp6F5NUDIMdESiHslmxAD5YUqgN1vQRdhJqRl9Dyv63JVKBtl%2FB7GFFgtNeZYj7RZL0Tv%2BSlw16sKXUVzCnPOB9xmkfyaSwjtT55%2FUheNi4t6X4jJCvn1v%2Bp4UaLfYw2XCVscPg1cszIKUySq7tB36Bc72IqDkdSC6qXsttRS5DYK5tg5dpZ8E6qZRtmO6Myohtgq4FL5I8lPpkxO1L7GvYQ0QhdccZIuqVTC2W9GUSic5J69gr1EKINw6KPDwYwMIu6%2F9IGOqUBbyn6ZkdC9Cm4EBC3B0aYWhBYYjmzQ6nVYyf%2Fuu6LkVuC8YIUtJoGoAGkwBQcibHco6H6kcFdkc6KKg7y%2FlL69GFZiylaYJG4WQ0y32FhYpnGAvYxtCL%2F0QmRL67zMgAVhUCumYwDy%2FKliPc%2BpE8dnjCAdl4Gay0MIJIIzT7LY2NMs08ZjnY7wnMkp7wWKlqGNL%2FRiFPbuG09fpVANzv1vJ0QR%2Ftn&X-Amz-Signature=2bf4fcfc6b2e3e964b0e8ea63a4df8b6a93522f8ccf3858606b30d5e0ac60881&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

同学们大家好，刚才我们介绍了 spring day 的 JPA 它初始化的流程，那么这一章节呢？我们来介绍 spring day 的 JPA 的执行流程。那么首先来通过脑图来看一下 spring day 的 JPA 执行流程涉及到哪些关键的操作。在这里面我们看到当我们使用 spring day 的 JPA 执行我们的 CID 操作的时候，我们的handler，也就是我们的入口，也就是repository，我们都是通过我们实现的 repository 来去执行我们真正的正常改待操作。


那么在这里面我们知道，因为我们在程序里面定义的只是一个 repository 接口，那么其实在执行的过程中肯定是它执行对应的实现类，那么这里面的实现类我们也理解了，它是我们通过代理生成的一个代理类，通过代理类去执行我们对应的正常改查，那么这里面的代理类的原生的target，也就是 simple GP reportery。


这里面我们也看到 simple GPT reporting 里面有常规的蒸删改查，那么对于我们自己手写的一些，比如说 find by name 这样的查询方法，它是怎么执行的？其实它也是通过我们的 AOP 城的代理，通过代理拦截进行一些特殊的处理，在这里面我们进行生成的这个对应的 GDK Dynamic LP Parks，也就是我们 spring AOP 生成的这个代理内，那么这个代理类它里面的执行的拦截器，也就是我们执行拦截提炼整个我们能可以通过跟踪代码的时候，看到我们整个执行的拦截体，这它会涉及到这几个拦截器。


那么这几个其实我们比较关注的，首先我们看这里面是 expose invocation，也就是它首先会通过类似于缓存去看一下这里面暴露了哪些方法去可以去进行执行的。另外是这里面是 CIOD mass 的 Meta d 的，通过这里面我们可以看到它也是跟我们正常改查一些常规的一些元数据相关的一些信息，其实这里面是对于我们持久化的一个异常的一些转换，这是一个四五，我们这个比较容易明白，其实跟我们 spin 对的 GPA 真正操作相关，主要还是下面这三个，我们这里面是称之为 intership 的，也是我们 AOP 的拦截器。那么首先是 defailed match 的invoking，那么 defailed match 的是对应的我们 simple GPA reporter 实现的这些类，它都通过我们这里面是 debug master，它会真正执行到对应的 simple GPA，它这个 report 的实现来去执行。


另外一个是我们看 query executor master intercept，这是什么意思？我们看到这个命名也容易理解，其实它主要是讲我们手工定义的这些查询方法，怎么通过查询方法来进行一些真正的执行，这个待会我们通过 find by name 来跟踪看一下，我们看下底下还有一个，这里面是我们可以看到是 implement 对应的master，这是什么意思的？其实我们在使用 GPA 的过程中，如果说原生的这些命名查找或者说 simple DP report 实现的这些方法不能满足的话，我们可以自己实现一个类去满足我们对应的方法的实现。那么通过我们自己实现类的话，它会通过这样一个 execution intercept 来进行拦截进行操作。


大家了解完这些的话，我们去知道其实使不用对的这一批，它执行的过程中我们可以称之为三种方法，一种方法是比如说像我们的 find by ID 是，它是 simple GPA reporter 实现的这些方法，那么这些方法它会执行 debug master in looking。另一种是我们根据命名查询语言，也就是比如说 find by name，这个 name 是我们当前这个对象的一个属性，或者说 find by 其他的一些基于属性，这里面我们看到了它的一些支持的一些表达式，比如说listen，或者说是 between 等等的一些查询条件。那么大家都会通过我们这里面的 query excused master intercept 进行拦截定义的这些 report 对应的 CRV 的操作，它会通过 implementation mass 的 execution interstep 来去实现。那么现在我们还是通过我们 spring 对 JPA 的这个模块的单元测试来去跟大家验证这一点。


好。首先我们可以看到这里面是我们比较关注的是两个方法，一个是我们这里面调 reports find by ID，另外是 report find by name。如果单纯看 find by ID 和 name 的话，这两个方法很像，但实际它执行的过程是不一样的，就像我们这里面刚才提到的对应的 find by ID，它是 debug master invocation，也就是因为它这里面的 find by ID，它是在simple，也就是我们的 user reporser 里面去实现的，这里面有对应的发音ID。


我们可以从正面去看一下，我们可以看到这里面有 find by ID 的这个方法，因为它这里面有了这个 find by ID 的方法，所以说对应的 simple j p reports 里它可以进行实现。那么对于我们这里面的 find by user，他 find by name 这里面 find by name 就相对比较特殊一些，因为 find by name 是我们手工定义的这里面，所以说 simple GPA reporter 里面并不存在 find better name 这种方法，所以说它就需要我们依赖定义的，这里面的是 query executor，也就是我们定义的一些命名查询，或者说基于注解查询的这种特殊的查询方法来去实现我们查询的操作。那么这里面我们现在去通过我们单元测试进行一个简单的一个执行，看一下效果。


首先我们对于 reports find by ID 这个跟大家去刚才也演示过，它最终会执行到我们的 simple JPA reporter，我们可以从这里面看一下，它最终会执行到我们这里面对应的一些方法，这里面会执行到我们的 find by ID。


那么其实我们现在比较关心的是哪个？我们现在关心的是我们的 find by name 执行的操作，我们现在通过执行 find by name 这个单元测试来执行 reporser find by name，也就是我们自己手工实现的 find by name 这个命名查找的方法。


在这里面为了方便大家快速定位关键代码，这里面我定义了很多 debug 的一些断点，可以看到这里面的断点非常多，但是为了让我们尽快执行到我们关键所关注的代码，因为我们在执行的过程中会有一个初始化的过程，包括我们命名查询语言对象的一个构造。另外还有我们在执行完成会有一些数据初始化的操作，那么这些数据初始化的操作，比如我们调用save，调用count，它都会执行对 policy 相关的一些操作，所以说我们可以先在初始化阶段把这些断点跳过，所以说初始化阶段我们把断点勾掉。这里面我们只选中一个是 user repost retest 它下面对应的一些断点。好，那么我们现在关闭，那么现在我们可以去执行这个 find by name，我们开始执行debug。


好，我们可以看到它现在很快执行到我们关注的这个方法，那么现在它已经执行到这个方法，那么现在我们需要把我们的这些断点再打开。当然也有同学说我如果不操作这些关闭打开行不行？当然也可以，只是我们执行过程中断点非常多，你会受到一些干扰，那么其实我们不能很快地定义到我们 find by name 这个关注的方法里面。
好，那么现在我们开始进行执行。首先我们可以看到这里面的 report 这个对象， report 对象它是一个代理，但这里面是基于 spring 的 AOP 此前的一个代理。我们看 DDK Dynamic AUB，抛开丝，对于它里面的内容，我们看它最终是通过 perfect factory 去构造的。它构造关注的这些接口信息是哪些？我们可以看到它这里面有对应的三个，我们可以看它让它列表形式的方式展开。


好，我们可以看到他关注的这个INTERFACE。这里面首先是我们定义的是 user reportery 以及是我们这里面的对应的 spring date reportor，以及一个对应的 transaction process 这几个接口，其实我们更关注的是 user reporsory。


好，那么我们下一步继续执行。那这里面我们可以通过我们的 F7 可以进入断点，那么在这里面是我们会进到我们第一层的关键环节，我们就要关注一下它这里面对应的这些拦截器的这些链。好，我们在这里面看到它会做一些校验，我们可以看到首先它会找我们当前这个代理对象的target，那么代理对象的 target 是，我们可以从这里面看到它是 simple j p reposary。


好，我们继续这里面我们可以看到它通过 adviser 里面去获取我们这些 intercept 的一个拦截器链，在这里面这个拦截器链，我们可以看到对应这个链它里面的元素有 7 个，刚才我们的 PPT 里面已经有展示，我们可以看到这 7 个对象对应的内容跟我们这里面是一致的。接下来我们该去进行它真正的一些执行的操作。
首先我们可以看到这个 chain is empty 等于false，我们继续在这里面它去把我们执行的过程，我们可以看到这些信息，这里面有我们的代理和我们target，我们的 Max 的，我们的参数以及我们的代理的类型以及我们的拦截提炼。那么基于这个我们构造出一个 revelactive mass invocation，我们基于这个 invocation 来进行我们的执行处理。好，那么这里面我们进行治理。其实我们如果说大家没有这些断点的话，其实我们最好还是通过 F7 去一步跟下去，如果有这些断点的话，我可以通过 F9 快速跳过F9，就跳到下一个断点来进行执行。


没有我们关注的，我们可以看一下这里面对应的是 intercept or intercept advice，进行一个emock，那我们看一下它这个对象它的一些实际情况是怎样的。对于这个 intersect 也可以拦截器，它实际就是 expose invocation interceptor，也就是我们这里面对应的列表里面的第一个拦截器。那我们看一下这个拦截器它做了什么工作。好，我们现在通过 F7 input 跟进去，我们可以看它其实实现的逻辑非常简单，它其实就是通我们当前的 emojis 站里面获取我们的第一个对象，找到我们 old 对象，同时把当前的 master invocation，也就是我们当前要执行的 MI 进行一个存储。前提是我们这里面注个替换，就是说把我们的 old EMO case 暂存起来，把我们当前的 mass cation 进行一个设置，那么这样的话我们再进行我们真正的一个执行操作。好，我们现在进行，我们执行一个处理，那么现在又到了我们的 reflect mass emocation 的一个操作过程，这样它会接着从我们的拦截器链里面找下一个我们的拦截器。好，我们可以看到。嗯，它会获取下一个拦截器。


我们获取到的内容是什么呢？我们可以看到对应的，我们可以看到 intercept or intersebison，它的内容是换成 CIUD matched Meta data post process 对应的 CIUD math 的 Meta data 对应的一个Intershaft，就是我们的第二个一个拦截器。


好，我们可以向后看一下，从这里面我们去跟一下第二个拦截器它执行的内容，我们看一部 case 连进来，其实这里面我们看到其实会有一些关键的信息，首先它会获取到我们的 match 的方法，在这里 match 的方法里面我们看这里面有一点操作，我们需要注意一下这里面有一个具体的一些实现了的一些实现方法，这里面看它是一个哈希 set 的实现，它里面的 set 是 41 个。


首先我们看一下这些默认实现的实现方法里面是否包含这个 mess 的，我们可以看一下这里面默认实现方法是什么呢？打开这个大家应该就比较容易明白，我们可以看到这里面是对应的是 c r u d report 里面的 delete by id，我们这里面 c r u d report 里面的delete，我们可以看到还有我们其他的我们 GP reports 里面的 get one 和我们的 GP reports 里面的 find by ID，以及我们看根据 query by example excite 里面的执行的一些方法。


access 这里面我们总共可以看大概四十几个，所以说我们可以看到这里面的这些方法，我们可以理解为 spring day 的 JPA 给我们提供的默认方法。那么如果说我们调用的是默认方法，我们会通过 simple GPT 进行执行，如果说执行的方法不在这个里面，那么它会通过我们刚才这里面实现的对应的query， exult method， interstrupt 指向，或者说是下面我们具体实现的方法来指向这里面。


因为我们的 Mast 它是，我们可以看到这是我们进行的是 find by name，当然 find by name 是我们自定义的，它不会包含在我们的一些默认实现里面，所以说我们跟下去它应该是不匹配，所以说进行下一步的执行，那么可以下一步执行我们看到跳过下一个断点，那么下一步我们这里面也是他会跟着去找下一个拦截器，那么下一个拦截器也就是我们这里面的是一些持久化和我们的一些事物相关的内容，这个是其实在数据处理上它也是比较重要的。但是对于 spring day 的GPT，我们更关注的它命名查询和它的 CIU 列车相关的一些实现，那么我们也可以去看一下它的实现。


好，我们现在进入，那么这里面我们看这里面它这个实现相对来说就直接就进行 MI process 直接进行处理了，我们可以看到其他并没有执行其他的一些方法，我们接着去看。好，现在我们可以看到它执行了对应的是 debug method invocase method，也就是现在已经到了我们这里面的 debug method invocating method incept，我们跟进来F7，好，现在我们获取master，在这里面我们可以看到它会有一个校验，这校验是这个方法它是不是一个默认的方法？很显然这个 find by name 是我们自定义的方法，它当然不是默认方法，我们也可以看一下这个 match Defield 它的一个实现的情况。


在这里我们可以看到它首先会对于修辞符进一些判断，这里面对于抽象的，公共的和一个静态的，另外就是它不应该是对应的这些类型，另外可以说它也不应该是对应一个接口的方法。其实这里面对于这个 g dog 是有一个描述，我们可以看一下它对应的中文的一些解释，我们可以看到这里面是如果这方法默认返回子被true，这，否则返回false。默认方法是指哪些？就是一个公共的非抽象的实例方法，也就是说这个接口类型中声明带有主题的这个非静态方法，因为我们的 find by name 它是一个接口上，当然它不是一个默认方法。


好，我们回来这里面进行继续。好，这里面它会执行对应的 invoke process，这就是我们在执行的过程中，因为它不是默认的实现方法，所以说这里面在 debug 的 Meta EMO case 它并没有执行到，所以说它进行下一个我们的执行站的拦截。


好，我们现在看好现在对应我们得到的这个拦截提炼就是我们的 query execute match 的intercept，那么我们进入。嗯，在这里面我们可以看它处理的逻辑。首先我会获取到我们对应的master，这里面我们可以看到它会去构造一个是 equation 的一个Adapter，我们看一下 Excel Adapter 是否，当然它等于null，那么我们去需要经过我们的 result handler 进行处理，这里面的 result handler 其实它是对，我们可以看到它的命名就知道它其实对我们的返回结果进行一个处理。其实我们不管是 Excel Adapter 存在与不存在，最终它都会通过 research handler 对我们的结果进行一个包装，那么进行结果包装之前需要去生成我们的结果，这里面是有一个 do emocation，好，我们跟进去这里面我们到 do emocation，在 emocation 这里面我们可以看到它对这个方法进行一些校验，比如说 has query for，也就是说这个方法它是不是一个查询方法？这里面我们确认它是一个对应的查询方法。对，查询方法里面我们会通过 invocase mess 的 cats 去获取我们这个方法。


我们看一下这个 invocase math cats 就是一个缓存里面它的，我们可以看到现在这个对应的 master cache，它里面的内容是空的，所以说它并没有写，目前还没在管我们的缓存里面，所以说我们现在进行执行，那么这里面它会去判断如果是空的话去构造出来我们这个 EMO case Meta date，那么构造完成以后它把以 mess 为k，把 IMO case match date 缓缓存里面。这样的话当我们在下次执行的时候，可以快速的从我们 case 里面获取到这个 invocation 的对象，那么现在我们可以看到它是通过 invocase manddate 进行执行，它执行对应的参数是什么？首先我们这里面推通过 repost information 里面获取到我们这个 repository 的interface，这个对应的 interface 也就是我们的 user 人群。


reporsory 这里面还会有一 imvocation mask card，这是什么意思？当我们执行过程中需要广播一些信息，也就是广播出去，我执行了某个操作，我们可以监听这个广播消息，实现我们自己的一些逻辑。这里面还有我们一个 case 对应的一些参数，那么现在就进入到我们真正一个执行的一个操作。好，我们进到 EMO case，这里面有case，它也会进行一些判断，我们是基于 reactive 的还是非 reactive 的，我们自行，这里面我们可以看到真正是通过这个 invocable 进行 invoke 操作，那么它我们可以看一下它的实现是什么。


invocable 它是对应的一个，我们可以看到是 report require mass 的invocation，也就是真正的我们的 repose 的一个方法。执行好，我们也跟进去看一下它一些实现的逻辑，这里面去获取一个 get execution，其实这是比较重要的，就是它真正执行是通过这个 Excel 去执行的。我们看一下如何去获取的。


获取 exception 的过程我们可以看到它是在我们的 Pod tree GP query 里面去获取的。这里面只想首先去判断一下当前这个 port 我们应该还有印象，我们的 find by name 它会生成一个对应叫 port tree j p query 的一个对象，通过这个对象进行一个代理来进行间接的执行。


首先它是不是一个 DELETE 操作？它当然不是 DELETE 操作，它也不是一个 exsultion 的一个 protection 是否存在的一个映射，那么它会去找我们的 super 对应的修正，那么这样的话它就会看一下默认的 excellent 实现，那么如果说我们默认这个execution，它不为闹，那么就把我们的 excellent 返回过去。


好，我们接下来去看一下，在这里面我们进行我们的 do execution 的一些执行，我们也是通过 FG 跟进去，可以在这里面我们看到它获取到一些参数信息，首先会把 master 里面的这些 parameter 构造出一个访问器，也就是我们 JPA parameter 的一些访问器。那么现在进行 execution 的一些真正的执行，其实在这个执行的过程，它会通过我们的 Paas tree GPT query 进行我们 JP 构造，最终通过 Hive net 把我们的数据去获取出来。我们简单跟一下这个里面的内容，是啊，也就是它会渐渐的脱离 spend GPT 的内容，会嵌入到 Hypernet 的内容，我们到 hyperny 那一场我们就可以暂停了。


好，首先它会去进行一个执行操作，我们跟进来，在这里面会进行我们的crequery，就是创建我们的查询对象，创建完查询对象以后，我们这里面是 get result list，现在我们先看如何去创建我们的查询对象。好，这里面我们可以对应的一些操作。首先这里面它嵌套的层次比较多，其实这种代码风格是并不是很推荐的，我们可以看到这里面是首先是对应它的 OA apply lock model，也就是锁的模式。这里面我们看一下实体的 Grapper configuration，它的一些配置信息，这里面 i play hittas 就是否命中相关的内容，在这里面才是真正我们 do create query 操作。


所以说我们可以看到这一行代码里面写这么多嵌套，其实这个可读性是非常差的，并且我们可以看到下面的 Mesh 的注意参数传入了很多，整看着这个方法其实是非常不推荐的。好，那么我们现在需要关心的是我们需要进入我们的 do create 方法，我们 F7 在这里面我们选中对应的 do create 方法。


do create query，我们可以看到这里面的这个 query 是还是我们的 Pod tree DP query 的一个内部词，内部类就是 query paper 以及预处理的一个操作。好，我们现在我们进行给你解，我们到这里面的话，我们可以看到这是我们的一些命名查询的一些对象，这里面我们去创建我们查询的操作，在这里面创建我们的query，我们可以看到这里面会通过我们的 entity manager 去创建我们的 query 操作。对于 entity manager 它属于我们原生 GPA 的内容，我们跟进去看一下这里面 create query，在这里面我们可以看到它还是我们的 spring promo cor m GPT 的包装。这里面会判断一下我们方法的名称，会，通过我们的 entity manager factor UTOS 去获取对应的 entity manager，那么通过我们这个 entity manager 进行我们对象的查找。


好，那么在这里面我们看到我们的对应 Hypernet 对应的 query 方法，去获取执行我们的一个 result 对象，那么现在我们可以看到这个 result 它是不是我们一个 query 的实现，那么是的话它就把这个 query 对象返回出去。


好，我们现在已经得到了这个 query 对象，那么得到这个 query 对象，我们下一步要做的事情是什么呢？就应该 get 我们的一个result，也就是我们 get result list，我们获取我们真正的 restore 的数据，那么我们也充值名看到这里面，我们看它现在已经进入到我们的是哈尔 net query 的一包结构下的实现，我们现在去获取我们的list，这里面我们就不跟进下去了。因为 Hypernet 本身它对于这个 YM 框架实现的逻辑也是非常复杂的。如果说有对应 Hypernet 的课程，大家可以嗯，紧跟一下对应的一些源码的实现，那么这里面我们就已经获取到了我们的 result 结果，这里面 result 结果我们可以看一下 result 里面它也是 every list，里面只有一条记录我们的一个 user 对象。


好，现在我们可以跳过我们的断点了，好，现在我们执行完成，我们可以看一下对应这个 find by name 执行的操作。这里面我们首先是看这里面日志是打开15，这里面我们看，因为单元测试我们会最终会把四五给回款了。我们对应生成的 having net 查询方法，这里面select，这里面会跟我们所有的字段加一个别名以及我们 user 0。好，最终我们可以看到它查询的语句是 from t user，对应的 user 0，对应的name，这样一个操作，对，都要这样一个 SQL 语句。


好，那么我们可以通过我们 find by name 的操作过程，我们可以看到其实整个 report 只有一个代理类，它通过我们 AOP 这个拦截其链进行一个执行的处理。最终对于我们自己自定义的这些方法，它会通过 query cute master interact 进行执行。那么如果说 spin t 的GPT，它默认实现的方法，它会通过 debug mess 的 EMO case met intercept 来实现，那么我们关于 spring day 的 GPT 执行流程的内容就先介绍到这里，谢谢大家。

