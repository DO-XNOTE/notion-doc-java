---
title: 4-1 二次改造-自定义数据审计实现（1506）
---

# 4-1 二次改造-自定义数据审计实现（1506）

[image](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/972076d6-3f18-43dc-8625-b0b7a0110069/SCR-20240814-jmat.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UL74V5ZD%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T232145Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIBNJ2OVV1CWUvClOOSdB4Bz%2BuADsfupsBWehclvoNLmIAiEA0KwdDr1i%2Fvi5AKkImjDb3poDBMFcFMYdiagPE%2FoMFq4qiAQIxv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDKaVvScIAAEf8BzFlSrcAwG46e%2FEzxZFI7OfPZeKvbSi%2BsVMLKbk9IxF8QyMWK58CNA%2Bp0pplQOsI%2BUCqwGJu%2FCw41EyhZ2MLtlsW0pGDr02HBih082mqpORDFh3ttQ6eWeNZ9%2FxbLM2S5Dwj7th8pRWIgUhpQSaZ8DZxxW1ll%2FedW3ghzX0AuSmZuTSyqssVtQhU6T%2BvWOU7lmJvr%2F2FoRjz7%2Bu6QX%2BSZcaE5lLlSaeThHvDaCVN1T%2BgXOJvtXQeOcPLq35XyGWmr2LWMKSgOL%2B7SQmpv00nXn8iRAqQSEJEgmRvS84Zgj1nbIJFPVRFhImg7FVZCTQ6Uc0E5dOURLlDm7iktFBD7SxaT1%2BqF80BRnboBD24fUn3ijEInkgJjwcbSn9%2FlbN4k8JolrzndNiF4wJaMCWPdNHVmimaLbDxQzkW4rpqHuLHmVTfEGR8dWLthOGv2zJLDG5Z8u38m%2Bm3imwD9cjzBmpQgX%2BgyVQgmnPPDTw2GfpSDHgErHnUYmdBIcljse7yWQG8kFFMWssJaLfld1wNmf1O47BfnvMrWJfXtvCxwhaJYlFHR2P9VGT8cnio25kPg%2Bf648FT%2B%2FCJ1ajYv%2Bn3B59YRNIT5%2B5be8wA3i0SoH0w7usYobrUqwN%2Bga5%2Fp%2BsD1rPMKe3%2F9IGOqUBUIgAG2D0pxUBT9E4u3mXbp4dTP89GRUI%2B8qAG%2FB8n3KxFzKil4OIlvH53okBiTb5EsjyEiM60EZueTveniQWhZ1zd7o213nHwbMQW8i6z0SkVrjBmgBXKnYfcFewcKF%2FSuAustT6uaINrq%2BoU1s9A7rpOmRvP6s9JE0KvipgOkZimi6qm%2BH%2FxxdnHsTkDNk1EhCS4Ooj4djcjrXjpjGYTxOE4g7a&X-Amz-Signature=0680219a5ca7fb6dcc18baf202b85d3c4b72d80e3ef4d0c4158c0c5d1a1d97a1&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

大家好，这一章节我们来介绍一下二次改造里面的自定义数据审计实现。我们在介绍 spring day 的 JPA 和Mongo，我以及以来色词的时候都提到过它们基于 spring date 的实现，都是支持审计功能，也就是 auditing 这个功能。那么我们首先来了解一下什么是 spring data 它的一个审计功能，这里面我们看一下如果说我们想发挥对应 spring date 它审计功能，我们要做哪些事情。


首先我们可以看到对于审计的操作，也就是说当我们的实体对象在创建的过程中，我们要指定一下 trade by，也就是说我们指定是被谁创建的，以及我们的创建时间是什么时候。那么假如一个对象被修改了，那我们应该去标明一下这个对象最后的修改人是谁，以及我们这个对象最后的修改时间。


基于这两点我们知道如果说我们的创建和修改都能标记上对应的修改人和修改时间，创建人和创建时间，那么我们可以理解为这个模型具有一个审计功能，那么 spring date 的 auditing 就是为了解决这个事儿去介绍的。对于我们在模型的构建过程，我们在模型对应的属性上标记上我们这几个注解，也就是我们的 create by create date，我们的 loss modify loss motive date。这里面我们可以通过我们 GPA 模块，我们的 user 模型来看一下，在这里面我们构建了一个 user 对象，那么 user 对象我们看里面我们有 create by 这样一个属性， create byte 属性也就是我们的创建人，这里面有 create date，也就是我们的创建时间。


下面还有我们的最后修改时间和最后修改人，我们这里面可以看到我们对应的这几个注解，在我们的属性上都有体现。这里面我们通过 add create by 修饰我们的 create by 这样一个属性，其他的也是同理。对应的 create data 修饰我们的 create data 我们可以看一下，比如说这个 create by 这个注解它是在什么位置，它是在我们对应的 spring framework date 的Alpaca，也就是说这个注解它其实是基于我们的 spring date common 来构建的，也就是我们 spring day 的定义的标准，这个跟我们 GPT 的标准就要区分出来，它并不是 GPT 的标准，它是我们 spring date 的标准。


那么我们回到 PPT 看一下，当我们知道对于我们所被审计的这个对象有了这几个注解修饰以后，我们还需要做什么事？首先我们如需要开启我们的 GPT 的editing，当然既至于 Mongo 的或登了它也是类似的，比如 enable Mongo editing，那么我们开启了 editing 以后，他要做的事情就相当于是我们会在 string 容器启动的过程去做一些后处理，对我们所管理的这些bin，或者说我们管理这些实体进行一些注解扫描，看我们是不是法扫描到对应的 create by create date 这样这些注解，那么当我们在进行 save 和update，当然对于 GPT 来说我们都可以理解为它是save。


如果说 ID 不存在的话，我们认为它是创建新对象，如果 ID 存在的 save 它，我们认为是update，那么这个过程的话就会调用到对应的 create by 或者是 lost multiple 这样一个操作，那么这个只是我们开启了我们的 DP 奥迪艇，那么如果说能让这个对象也就是创建过程或修改过程中去生效，去我们对应的创建人创建时间，我们的修改人修改时间。


我们还需要做的一件事是需要加载我们的一个监听，这里面的监听也是在我们的优势对象去加的，我们这里面去看一下我们这里面优势对象的一个例子，这里面我们看到我们在这个 user 的 class 下面加了一个注解。首先是 Internet listener，也就是说作为一个实体，它监听的内容就是一个 auditing Internet listener，也就是监听了我们一个审计的一个司机listener，这里面我们需要注意一下这个阴气的listener，它并不是我们 spring date common 的标准，它其实是 JPA 的标准，这个大家要来理解，那么我们这块理解了我们的 auditing integration 的。但还有一点我们需要去想，也就是说这里面要创建人和创建时间。


通常我们知道当我们系统登录完成以后，我们通常会把我们的创建人去作为一个会话标记存在我们的 session 里面，当然现在我们分布式架构，我们不支持单机sets，我们更多的是把我们的当前登录对象通过一个 token 的方式存储到 Redis 里面，我们可以通过token，通过基于我们 SSO 的这样一个登录的字来获取我们的用户信息。
那么如果说我们使用了 spring secret 的话，它里面可以有一个静态的方法，也就是 spring context 去 get user，也就是获取到我们当前的一个登录与对象，那么这里面我们并没有去依赖这种secret，那么我们这里面去自己实现的一个 Audit where，也就是说 customer Audit where，通过它来去获取我们当前登录的上下文对象，也就是我们当前的登录者，我们可以看一下这里面我们是怎么去实现的。


对于我们实现的过程相对来说是比较简单的，我们的 cosmoaudit where 它是首先是实现了 Audio where 这个接口，对于这个接口的话它提供一个泛型的支持，我们去获取当前的审计对象，那么当前的审计对象也通常就是我们当前的操作人，当前操作人也就是我们当前的登录对象。
那么通过这里面我们可以看一下，我们在这里面去定义了一个属性，这个属性我们采用的是一个静态的操作，这里面当然我们静态的操作这个应该是受控的，它不应该被任何人进行一个无意思的一个修改，我们可以在这里面我们看到对应的一个 login user，当我们去获取它的时候，我们把当前的 login user 获取出来，就是说我们实现了一个 get concurrent editor 这样一个方法。


那么如果说我们想去设置我们修改的一个用户对象的话，我们可以调用 set locking user，我们把这个用户重新设置一下，我们再进行我们的修改的操作，那么这样就完成了我们修改的过程中，把我们最后修改人带进去的这样一个实现，那么我们完成了我们的 customer edited aware，就是说它能获取到我们当前的登录对象。那么什么时候去执行我们对象的修改呢？我们知道我们其实自己实现的对象千差万别，所有的这些操作的属性都跟我们这里面的注解相关，那么我们如何去真正在执行的时候修改我们这个对象？比如说把当前时间赋给我们的创建时间，在。


修改最后修改的时候，也把我们当前时间赋给我们的最后修改时间，它的完成就是需要依赖我们这里面的是 auditing 的handler，也就是说我们真正审计的一个 handler 操作，它其实可以找到。


我们对应被 create by 修饰的这些注解，进行我们在执行对应的时间点进行一些修改。这里面我们来去看一下 auditing handler 它做了哪些事情。我们可以看到这里面的 Audio Handler。


它其实是也是继承了 auditing 的 handler support。我们看在上面这样一个结构的一个内容，首先我们可以看到这里面有涉及到一个 auditor aware，也就是说我们需要获取到当前 Adidas where，我们的一个死线，我们基于 ADID aware 来去找我们对应的当前的我们的一个审计人。我们对于 editing handler 我们可以看到这里面有几个关键的方法，这里面是我们可以看到这是 mock create，也就是说它就是来去标记我们的创建人。


我们创建人是怎么去操作的话，首先它会去获取到我们的audit，也就是获取到我们当前操作人。我们看一下 auditor 它是怎么去获取的，它是通过我们的 auditor where，也就是我们刚才在这里面创建的 COS Audio where 去获取到当前的登录人。


那么获取到当前登录人以后，我们需要怎么去操作？这里面我们可以看一下，我们跟进去在这里面是设计一个TOS，这里面涉及到一些反射的操作，会把我们当前这个操作对象复制到这指定的一个属性里面，这里面的操作是 tos 奥didate，我们跟进去看一下，这里面首先看一下当前这个奥 did 的是如果说不存在的话直接就 return 了。


那么首先我们再看一下它当前这个对象是不是一个 new 对象，判断 new 对象通常是判断对应的 ID 是否存在，那么我们如果看如果是它是一个新的对象，那我们这里面是 side create by，也就是我们 seed 我们的一个创建人，创建人就是通过我们 Audit 获取到我们当前 Audit 的对象，那么如果说它不是 new 对象，同时我们看一下也就是这个 modify on Christine，也就是说如果说它不是新创建的，我们看一下它的修改，也就是说它最后的修改对象是谁？这里面的是 multiple on Christine，也就是说当前这个对象有没有被修改过，如果说它有被修改过的话，我们才会去执行这个设置我们这个修改人的操作，那么这样的话，在执行的过程中我们就看到其实它是通过反思的pass，把我们这个当前的登录对象设置到我们对应的属性里面。


对于我们这是 mock crazy 的，这是 mock modify，其实效果其实是一样的，那么我们关于这个 auditing 的整个这个执行的过程，我们是跟大家去简单去介绍了一下，那么我们现在通过单元测试来去体验一下这个数据审计的这样一个过程。


我们现在到我们对应的单元测试这里面，我们看到我们这里面定义那个 user report auditor 的一个test，那么在这里面我们还是基于单元测试的方式进行一个初始化操作。那么首先我们看这里面使用到的内容，这里面我们还是去会 import 我们的 init date，会在启动的过程中首先初始化我们的数据库，那么这里面我们首先去 get user，那我们 get user 的话，我们获取到一个 user 对象，那么在 user 对象里面我们看一下对应 user 对象里面它的创建时间和创建人是否已经更新上去，那么这里面我们再通过一个 update 操作。


那么通过 update 的操作来看一下我们获取到，当根据 ID 获取到当前这个对象，这里面我们同时在 customer audit aware 里面去设置我们的 locking user，我们是 log in user，设置为当前的登录用户Jimmy，接着我们去修改一下我们的用户名称，把用户名称设置为原来名称，后面加上下划线updated。那么这样的话我们就进行一个 report 的 save 操作，那么 save 操作在这个过程它就会触发我们这些刚才我们介绍到的 Audit handler spot 相关做的一些事情，也就是把我们那个最后修改时间去更新进去，接着我们再通过我们的 repose 库里面去查找这个指定的对象，查找到这个指定的对象以后，我们去判断一下连这个被修改的对象，它的最后修改人是不是我们刚才的登录用户。那么基于这一点我们去判断一下我们这个审进的是否生效。


首先来我们去看一下我们的 get user，也就是说因为我们在初始化的过程中已经触发了数据的初始化，在初始化的时候过程中会触发我们的创建的审计工作，也就是我们的创建人和创建时间。那么这里面我们就是查询出来，我们去关键去跟踪一个对象，有对象的创建人和注意创建时间是不是已经被赋上值了？我们现在去执行，我们通过 debug 的方式可以运行，我们可以看到现在我们获取到了 user 对象，那么在 user 对象里面我们可以看到这里面我们设置的一些信息。


这里面我们可以看到 create by 是我们的 test user，当前的 lost multiple by 也是 test user。我们现在知道当我们在创建一个对象的时候，我们的创建人和之后修改人是相同的一个人，这就说明我们当前的创建对象已经设置完成。为了为说明一下我们当前的最后修改的人和我们的创建人都是 test user，为了避免我们确认是不是在初始化的时候把对象true，我们可以看到这里面的 init date，我们在初始化的过程中，我们并没有在创建人和最后修改人里面设置值，那么我们可以看到那么我们这个 test user 是从哪里过来的？我们可以看到我们的 customer audit aware，也就是获取我们登录用户，这里面我们默认的登录用户是 test user，因为我们作为一个测试的模块是 test 的user，那么我们可以看到其实可以说明我们的程序是在保存的过程中，通过我们的 custom 的 edit where 去获取到我们当前的登录用户，进行了操作。


那么现在我们去跳过断点，我们快速的执行，现在我们程序执行完成，我们也可以在我们的日志里面去简单的看一下输出的一些信息，这里面的用户对应的我们这里面的 create by test user，这里面有 loss modify，也就是 test user，这是我们在创建的过程中获取到的对象。


那么现在我们进行一个更新操作，那么这里面我们去执行我们的 update 优势，这里面也是加上断点，我们首先在这里面加上断点，在这里面我们在 save 的过程中，我们在这里面也加上一个断点，我们现在执行，我们现在已经执行到断掉。我们可以看一下在这里面我们看到对应的 user 对象，那么 user 对象跟我们刚才看到的效果是一样的，这里面也是当前对象是 test user，最后修改对象 yes 态的优势，现在我们做的事情是什么呢？我们去首先我们设置一下当前的登录对象，我们设置成Jimmy，那么接下来我们去看一下，再对这个用户名称进行修改，修改完成以后我们进行一个 SIP 操作，当然我们是 test 的情况去操作，最终我们的四五会回滚。


所以说如果基于数据库去看的话，这里面对于数据库是一个不可见的，我们这里面去专门手工的 repose Flash 刷新一下，保证它可以进行一个更新的操作。那么接下来我们再去库里面把这个对象获取出来，我们可以看到现在我们是得到的是 update user，那么我们可以看一下我们是更新过的user，这里面我们看名称，对于这个用户名称已经修改了，后面加了一个下划线 update 的这样一个后缀。同时我们可以看一下它的创建人还是 test 优势，但是它的最后的修改人已经变成金。这样我们可以看到当我们修改的过程中，整个这个它的最后修改人和最后修改时间其实也生效了。


现在我们这里面会通过断言去校验一下我们的 login user，也就是我们这个 log user 跟我们当前用户的最后修改人是不是相同的一个对象，如果是相同，那么我们可以认为我们是执行 EGO 以及说 ECO 的一个过程，它并不是相同的对象，它是 string 的， ECO 是相等的。


这样我们去做一个断点，如果说它没有抛出异常，那说明我们的断言是成功的，我们现在跳过断点，现在我们可以应该看到我们执行的结果，我们执行结果是正常通过，也就是我们可以看到这里面涉及到一个查询语句，一个 update 该语句。通过这两个单元测试的话，我们已经明白了基于 GPT 的一些审计的效果，才我们通过 Sprint JB 的奥迪艇实现了。我们在创建和修改的过程中，把我们的创建人和最后修改人和创建时间和最后修改时间进行一个同步的一个更新。那么如果同学们对感兴趣的话，可以参考一下代码如何去进行实现，这里面切记我们不要丢掉里面的步骤，如果丢掉里面的某个步骤的话，它可能会引起我们这个审计信息不生效，同学们，我们下一章节再见。

