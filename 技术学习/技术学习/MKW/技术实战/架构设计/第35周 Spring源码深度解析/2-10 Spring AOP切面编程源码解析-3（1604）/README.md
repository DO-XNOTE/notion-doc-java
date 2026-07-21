---
title: 2-10 Spring AOP切面编程源码解析-3（1604）
---

# 2-10 Spring AOP切面编程源码解析-3（1604）

[image](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/b4cd3207-bd35-4568-9c84-dd21c53a2f46/SCR-20240803-myhq.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662WPARSRH%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T232012Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIBUA88LMdl0PUGH8MGOfgr%2BHjouWYcQyOJy0h7wQD2ZAAiAJ5dVbG8G1T6QKLtvs2%2FQVAk6K8opJJziBok%2BDlflGRSqIBAjG%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIM4LBF5MiDgCcb9tnzKtwDouzjzLLbbYiDahjukVDqQiNoT0xhPvBUrAOcR%2FTGqjGB2J5%2F%2FeGD6rvZKKXuj13vQdWbtLr9lEtgeCMq4TTa065Tnwzp0FvVsYhm9ZASKabqli24KDZThZCzEAsK%2BmVYNT8w6P0GG%2Bp2XHZPq1ubK0ux%2FynZiuopf4PO4ofX%2F7zXoMIw8FOVFd9fdZEbyj4voZBnWtm8MlJtcUfj0xOzBPYLFk1dg0JB0l3ZX%2BqEJc%2BmdQzqA5P4ZQp8HUT%2BHuv3%2FNuFUQ5NRXq%2FYtirYOVmGjQgJ3CTf63c%2FLML9E%2BFzNDT6UHifAlH7j24zFUh9k7%2B2da%2FLjQX%2B%2FOzMEegM%2F9jrUBqDq6epUirrc3%2FCV8hs8WjFx5Qaqr1sz1eJjGMYz4Wo81kYQy6R5tUNpshhOaB6c3PSMOJAoQOUOm%2FtiDcMqVvh6wEDS3jyThN85R4xgTHKhbRCYTsGmax2GlZ7UK35qwYZj7RT1r4i3jAw9bQ6ZxdUZp7pVvACTAVeZbJIdq0ku9nvng3%2BYlmZj33lm29xhP7NB%2B9qaQ%2Bk%2BnzCTSEXdhOVfNasx%2FNzZ4lWfywn2vKK2vVU0Mt8KOsnhEYNfeIbrnmi7YuYOk5xq3Z7gXjY6Y0xlJBAZynQhMPsRww17r%2F0gY6pgEZVHKTgqwnE1Gyw%2F0tIX6xqN1N%2BCOh7A0kJfsWGpu6vIAE2xCyw%2B0R76vZ38grjBb1fBINBq8XfWwvHe3LKW%2BXBFOOdSFlXiEDrwPdaimwYZUuF2GvS7KLzIdiQM4uN6OykjNe4JEt0YJNi6vu%2Bp0F7xO8pLFy0btGFvcCLqaVc7CHGtoFqbGAiO%2BCnTRPQzFwbJJqZ9lautmrh%2B5XtfMe8uI60Nkd&X-Amz-Signature=dac589d93952351705f81fa335ab92ed0b1c53355483471f1f53efbde954207b&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

其实我们刚才看到其他这个handler，其他地方也有，比如说 spins 和 context 到，包括我们第三方的，像德鲁伊，它也会定义一些这样的一个 name space，这里面还有 mybadcase 相关的一些内容。那么我们看一下 beans 它里面定义的是什么呢？比如说 beans 定义的像 schema c， schema p 和 schema utos，跟我们这里面可以看到定义的一些对应关系。 Scammer p 那个就是 simple property name space handler utils 对应的是 UTO name spray handler，它是通过这个 spin handler 去定义完成的。


那么我们回到我们的断点，我们继续执行，我们知道了从这里面获取到了我们的 AOP name space handler，那么我们继续，在这里面我们获取到 name space handler 以后，要做的事情是什么呢？我们可以看到这是 AOP name space handler，它要做的事是 init 方法，那么我们跟进去隐匿的方法，这是一个比较重要的操作。


我们在这里面可以看到，当我们在初始化这个 name space handler 的过程中，它做的一件事情就是 register being depending pass，也就是说它会把我们这个宾语定义文件的一个解析器注册进来，它注册的方式也是一种 KV 的结构，它的 k 就是我们的 element name，也就是我们这个 Xmail 标签的元素，它的 value 就是对应的一个解析器的一个实例。我们在这里面通过 new 的方式构建出这个 configure being dependent pause，我们看这里其实是比较容易理解的，我们通过 AOP configure 去定义这个 x mail 的时候，我们可以从这里面去看一下。


我们通过 AOP configure 定义这个 x mal 的时候，它会指定一个解析器，就是 configure being depending pass，也就是我们这个 being 定义文件的一个解析器，那么我们这个对应关系知道了，那么 x 庙在解析的时候，如果碰到configure，也就是说碰到这个 u p configure 这个节点，那么它解析的方式就是通过这个 configure being definition pause 去解析的。


像这一点大家记清楚，那么好，那么我们继续这是config，那么下一步这是 SPCAT 接autopress，也就是说这是我们的自动代理的一个配置，那么碰到这个配置的话，我们会通过这样一个对应的一个鼻音低频的解析器，也就是说它会碰到这样一个元素的时候，对应的解析器就是这个解析器。


下面也是相同的道理，这个就不用一一再去介绍了，那么我们在这里面的隐匿的方法去执行，执行完成以后他就开始进行对于我们这个 x 秒去解析了，那么我们跳过在这里面我们可以看到我们获取到了 name space handler，在 handler 里面我们要做的事情，我们跳过我们获取到这个handler，那么我们要对用通过 name space handler，也就是我们这里面是对应的是 AOP name space handler 进行 press 解析，这个解析的过程就开始对于 x SML 的节点去进行加载去解析这样一个过程。好，我们跟进去看一下，在这里面解析的时候，我们可以看到它是通过name， space handler support 这个的类去执行的，在执行的过程中我们看到它是通过 find a pros for element，也就是找这个映色关系，通过对应的 element 找到对应的解析器。


我们看一下这个，我们现在这个 element 它是 AOP configure，那么对应 AOP configure 这个element，它能找到的解析器是什么呢？它能找到的解析器就是我们刚才注册的，我们已经看到我们找到的process，我们找到的protest，这里面我们看 protest 就是 configure being definition process，这个 process 就是我们刚才在 OP name space handler 里面去注册的这样一个process。好，那么我们可以跟进去看一下它做了哪些处理。


在这里面是 configure being depending process，就是我们解析 AOP configure 标签儿的主要的解析器。在这里面我们可以看到首先它会定义一个 composite component definition，这就是一个组合的一个圆，我们可以理解为一个主键的一个定义器，那么通过它我们看到它会把解析的一些 being definition 的都会注册到这个里面，那么我们跳过像这里面看，这里面是我们刚才提到比较重要的一项，就是 configure auto process Creator，它是注册一个 being post process，也就是说当我们的容器在初始化的过程中对我们的 b 隐进行初始化的一个后处理和实例化的一个前处理，保证我们的 b 隐私通过代理进行包装过的。


那么我们看一下这里面注的事情是什么呢？我们可以跟进去看一下。好，我们跟进去，在这里面我们可以看到，在这里面我们看到它是调用了 AOP configure utos 去注撤一个 aspect 接 auto price Creator。那么我们再跟一下看一下它注册的是用的是哪个类，在这里面我可以看到它其实注册的是这样一个类， aspect 接 aware Advisor to Procast Creator。


注意一下，如果说我们通过 XL 去注入的话，我们用的是这样一个类，那么如果通过注解的话，它是配置的是一个基于注解的 auto process，其实是它的一个子类，那么我们看这个注册完成以后，我们可以到这个类里面看一下，看一下它实现的方法。我们可以看到它有很多跟 post process 相关的方法，这里面有 off 的insulation。和我们这里面比较关心的是初始化之后和我们的 before incident，也就是在实例化之前的方法。那么我们待会儿执行到，我们再去看一下它的过程。好，我们还是回到我们断点执行的位置。好，我们继续，回到了我们这里面是 press 解析的过程，那么接下来我们看一下它是如何去对我们这些内容去做解析的。


我们可以看到在这里面它会获取通过 DOM UTOS 去获取我们的一些子的 element 节点，在这里面它会获取到对应的 element 一些信息，我们可以从这里面看一下在这里面获取的子的element，它是有一个，这是一个 AOP aspect，那么通过 aspect 来进行解析，它会走到哪个步骤？我们看一下，首先它会判断一下这个当前的对应 element 它的名称，我们看到 local names 在这里面是aspect，那么 aspect 它最终会跟我们这里面的 aspect 请一口子匹配上，那么它会通过 pause aspects 的方式去解析我们那个配置的内容。


好，我们看一下，好，在这里面我们可以跟进去看一下，它会解析 aspect 键它对应的一个操作，它会首先取出 ID 和 REF 这些常规的属性，那么我们跟进来看一下，后面我们主要关心的是看它如何去获取我们的一些信息。这里面是 PROS advice，这是相对比较关键的一点，它是在 aspect 里面去解析出跟 advice 相关的内容，我们可以看一下，在我们的 AOP 的这个文件里面，我们看一下，在这里面跟 advice 相关的内容就是around，因为 around 它是一个环绕通知，就是对应的一个advice。我们可以看到在这里面去进行解析，它会得到一个 around 相关的一个 being definition。


好，我们在这里面我们可以跟进去简单看一下，嗯，在这里面它是解析我们的 advice 相关的内容，它也是 advice 解析的过程中，首先这里面会定义一个 mass 的 location factory bin，这里面是定义这个方法指定一下我们对应的 bin 和 Mesh 的name。


好，我们继续跳过去，我们看接下来会执行一个叫 simple be infect where aspect 接 instance factory，也就是构造我们的一个工厂类，也就是获取我们的 aspect 的一些实例的一个工厂类。我们继续接下来我们看一下这里面去注册这 Puna cat，首先它要创建这个 advice 的 being definition，我们看一下它是如何去创建 advise being definition，在这里我们可以看到在这里面创建的方法里面，首先这里面是定义了一个 root being definition，但是它的 class 类型其实不确定，它 class 类型是什么呢？是通过 element 去获取到的，那么我们可以看一下，我们先跟进来，我们跟进来看一下在这里面 Advise 的 limit 它是什么呢？这里面我们可以看到对应 advise 的 limit 是一个 around advice，那么我们跟进来去看一下这个方法它是怎么处理的。


好，我们到这里面，它是通过 advice 获取到，也就是通过这个 element 去获取对应的 class 类，我们可以看到在这里面我们获取到的 element name 是什么呢？ limit name 是around，那么通过 round 我们看一下，它会进行去比较，如果比如说 before 的话，它会 return aspect 接 mess before advise，如果是 off 的话，是 aspect 接 off 的advice。


相同的道理，对应的每一个 advice 都有对应的一个 advice 的实现，那么对应我们是 around 呢？它肯定是有对应的这样一个aspect，即 around advice，那么我们跟进来看一下，它会去匹配到我们的 around advice，那么好，它得到这个 advice 也要构建这个 being demination，那么后面就是顺水的一个过程，就是把对应的一些属性去解析赋值进去。


好，后面的内容就我们就可以快速的跳过，在这里面我们判断一下我们获取到的我们的 point cut，对应解析完 point cut 的一些属性，对它进行一些赋值，如果不满足的话我们就可以跳过。好，我们构建就是这个 advise 的definition，以后我们看一下，我们要构建这个 the version，这里面 the version 我们是使用的是 object 接 point 的 version 这样一个类，那么我们看在构建它的过程中，它是需要传入一个参数的，我们可以看一下它的构造方法。


对于这个类的构造方法，它是需要一个device，这个 advice 是也是基于 obstack 接的一个advice。那么在这里面我们可以看到我们刚刚是通过这种方式构建了一个advice，在这里面我们可以看到对于这个 Advisor deepness，它需要在构造方法添加一个参数，也就是我们刚才构建的我们那个 being division，把他们的关系构建出来。
好，我们自相我们下去，这样的话我们整个这个过程就会解析完成，那么我们跳出，好，接下来我们看一下，这里面是解析我们的 point cut， point cut 我们跟进去看一下解析的内容是什么。在这里面我们可以首先看一下这个element，这 element 是我们的 AOP point cut 这样一个 element 的一个属性对应，我们可以看一下对应我们的 XML 的操作，也就是我们这样一个 a o p point cat 这一行记录的内容。


那么通过这一行记录的内容，我们先获取 i p 和它的表达式，其实对于 pound can 的话，它最重要的就是它的表达式，我们可以看到这里面我们获取到的表达式的信息，表达式的信息也就是我们这里面配置的是 showcase bin 下面所有的方法去拦截，它们通过这个表达式去构建这个 pond cut，我们看这里面是通过这个表达式去构建这个 panic definition，我们可以跟进去看一下。


这里面就比较简单，我们可以通过 root being definition 构建 as pack 接 expression point cut 这样一个类，构建完成返回。好，这样的话我们的 pending cut 的类也是构建完成了。好，它出站，我们跳出，这样的话整个我们一个解析的过程也就完成了。


AOP 的解析过程完成以后，接下来就应该对于 BN 的实例化了，那么我们看一下它是如何通过在实例化过程中，通过 pose process 的方式把我们的 AOP 代理类包装进来。好，我们跳过这个断点，在这里面我们可以看到它是在这里面是对应的是 abstract AOP process Creator，在这个类里面它去实现了 post process of 的indlation，也就是说在我们 bin 初始化完成以后，我进行对它进行一个包装，在这里面包装的过程中我们可以看一下。


首先我们观察一下这 bin 的名称，这 bin 的名称是什么呢？ bin name，这是一个内部类，那么我们可以看一下，我们可以快速获取，这样这个不是我们关注的这个类。好，我们跳过，那么好，下一个我们看一下这个类也不是我们关注的，我们关注的是 hello bean，我们看一下这个 Hallobin 这个类它是怎么去处理的，我们第一步首先是看一下它去代理引用的去做一个关系比较，如果是匹配的话，我们去进行对它的一个包装。


这个包装的操作我们可以进来看一下，在这个包装的过程中，首先看一下 b name，首先 b name 它不为空，并且我们判断一下这个 b n name 它在这个，如果说它并不在这个 target source bins，如果说它在里面包含的话，它就直接把这个对应的 bin 呢返回了。


那么接下来我们再看一下后面的逻辑，这里面也是一个逻辑的判断，我们继续我们在这里面是整个我们创建这个代理的关键，我们看一下我们跟进去看一下这个操作，我们这里面是创建代理类的过程，在这里面是最关键的过程，我们可以看到这里面是 Procast factory，这里面主要我们在手工创建这个代理的过程了。在这里面就是我们真正在死病 AOP 创建必应的过程中，它的代理类就是通过这个方式去创建的。那么我们接下来看一下，他去注了一些操作组件，自 copy from Morris，就是当前这个类型 copy 过来，这里面判断一下它是不代理这个 target class，如果是的话去做一些参数的设置，这里面主要是 set focus target class。


好，我们接下来看一下它是去构建这个 build advice，就是跟我们这个 BA name 相关的一些advice，我们可以看到在这里面这个 advice 它有两个，这里面一个是 expose invitation 对应的一个拦截器，另一个是我们关注的 aspect 接 point adversion，我们可以看到它是一个 point cat true，也就是它永远是返回真的下面这个 point cat，其实这里面可以通过这个表达式能看到它是我们对应的比较关心的这个拦截 so case bin。


下面的方法的拦截器，好，我们继续好，在这里面我们去做了一些操作，我们会通过这里面对 POX factory get press，通过它去真正的去创建我们的代理类。那么执行到这一步的话，跟我们在手工创建代理类的过程已经接壤起来了，那么好我们这就不进入了，我们去推出在这里面我们的代理类创建完成以后，它会把这些状态去标志一下，这样的话我们对于一个代理类的包装也就完成了。


好，这样的话我们可以看到它是通过我们的 pose 的 process 的方式去执行的。好，我们这样一个对象 bin 可以返回过去，整个这个过程就完成了。那么好，我们现在去退出断点，好，整个过程执行完成。好，那么这样的话我们对于通过 XL 的方式去构建 AOP 的方式，我们就介绍完成，那么接下来我们来看一下通过注解的方式来声明AOP。

