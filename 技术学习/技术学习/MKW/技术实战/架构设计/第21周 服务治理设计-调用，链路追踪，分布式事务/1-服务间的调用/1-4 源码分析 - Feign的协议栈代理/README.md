---
title: 1-4 源码分析 - Feign的协议栈代理
---

# 1-4 源码分析 - Feign的协议栈代理

[image](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/d0e129bb-0499-461d-bc1f-dad33206565b/SCR-20240802-bvzo.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WTH6FVYZ%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T231335Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDipI0OT8JPX6w%2FZAUHdxNpQ9F5OPYu%2FVc970eMH9VuAQIhAP9Hyes2n0HwLqggsrKOt%2FtIBTU6Blrin7p1PRN%2B65%2BNKogECMb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1Igyn6WVz5L9Aq%2Bd4gckq3APW9XS5RsRksPH3Bsosx22GtyPXulfgkrYtgkzWpw8ymBxyBdDwfPJAR6sKav2YJ85L5Z2BkwEQloKjK8q33c6jRLu9Oc%2Bkjksa6OShuu3GwjSvlGIRjHZMyiXpkjPs5QWum9IoH8biM3GIBXhcbZGe%2FCBas2pStc91Jzj4YakYaCfMq3jxB85GF1oft4x%2FEgvRVBmLCr1mT24rMrRuXi3arsr1DMHG19ccCQOE3wy16x34XRlrSMuhDYaNm3BUxGYvjz1yipQjGSOHye8McLdndp4%2FZtai0WMD%2Ft9wIskWS8MC2WSotVPjVtW%2B6gfTGMfelJMGHKHlDl9bMHSI83vje06EHgXQk6Mats%2Fww8Na2QaYXhMTufAqBTaoB0K50BVyrI4BUVorApgGLggazw2vzJ9iN%2F%2BXSn5Qnr%2B2KUnKqav0puELSx3kuRiyTR1RnuEOIwug0Tbtg5rq04y56Bk934zLQnKndBKXtHBMpCWE%2FPzpmsseXpOz9zuNT%2F%2FIdfSX9EbLMhSofkuW0fRSf%2FGh7IfoYlpATVSXCKFBnl55W3Wyli8Tc6%2FCMbfWTCBcbNy%2F8fU9K%2F4KUAbo%2BpGw%2BNHe7U5M2SH94H8v9vg8Sgfvidpom7pdNstmT%2BHoRzDyuP%2FSBjqkARvlESebYo3yYTPRh29gFEDHdhKD6bE0QNCQGZOapVBszjLIuHhckDSighYEKFHRgTKfn7%2BO5C4IOMFDVuUQDWLjYCyyRV5K5F55queC0OWSwJCehzeZbBgYm%2FWmuW%2FNfObQtY07ia9okZ5FP1mQfC7XNpFh7N%2BfFkojO4eRd7P4qEzQQ8ayQMZTpcKmHXq6fvK7ywv5vfjp7blIglUb5XBczW4d&X-Amz-Signature=160e414062e91dffe2f125a13e0c46e0cf4f4abd23e803598d2506fcec113db7&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

[image](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/9efbe89a-1a94-4e05-93c7-ea6e68878b92/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WTH6FVYZ%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T231335Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDipI0OT8JPX6w%2FZAUHdxNpQ9F5OPYu%2FVc970eMH9VuAQIhAP9Hyes2n0HwLqggsrKOt%2FtIBTU6Blrin7p1PRN%2B65%2BNKogECMb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1Igyn6WVz5L9Aq%2Bd4gckq3APW9XS5RsRksPH3Bsosx22GtyPXulfgkrYtgkzWpw8ymBxyBdDwfPJAR6sKav2YJ85L5Z2BkwEQloKjK8q33c6jRLu9Oc%2Bkjksa6OShuu3GwjSvlGIRjHZMyiXpkjPs5QWum9IoH8biM3GIBXhcbZGe%2FCBas2pStc91Jzj4YakYaCfMq3jxB85GF1oft4x%2FEgvRVBmLCr1mT24rMrRuXi3arsr1DMHG19ccCQOE3wy16x34XRlrSMuhDYaNm3BUxGYvjz1yipQjGSOHye8McLdndp4%2FZtai0WMD%2Ft9wIskWS8MC2WSotVPjVtW%2B6gfTGMfelJMGHKHlDl9bMHSI83vje06EHgXQk6Mats%2Fww8Na2QaYXhMTufAqBTaoB0K50BVyrI4BUVorApgGLggazw2vzJ9iN%2F%2BXSn5Qnr%2B2KUnKqav0puELSx3kuRiyTR1RnuEOIwug0Tbtg5rq04y56Bk934zLQnKndBKXtHBMpCWE%2FPzpmsseXpOz9zuNT%2F%2FIdfSX9EbLMhSofkuW0fRSf%2FGh7IfoYlpATVSXCKFBnl55W3Wyli8Tc6%2FCMbfWTCBcbNy%2F8fU9K%2F4KUAbo%2BpGw%2BNHe7U5M2SH94H8v9vg8Sgfvidpom7pdNstmT%2BHoRzDyuP%2FSBjqkARvlESebYo3yYTPRh29gFEDHdhKD6bE0QNCQGZOapVBszjLIuHhckDSighYEKFHRgTKfn7%2BO5C4IOMFDVuUQDWLjYCyyRV5K5F55queC0OWSwJCehzeZbBgYm%2FWmuW%2FNfObQtY07ia9okZ5FP1mQfC7XNpFh7N%2BfFkojO4eRd7P4qEzQQ8ayQMZTpcKmHXq6fvK7ywv5vfjp7blIglUb5XBczW4d&X-Amz-Signature=87df9cbefab84bce1c0c65a1e3ea654c0bc05940aa283a6c829c69d2fdc5bb6b&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

hello，我们过往的各位同学们大家好，我是姚半仙，那我们这一节跟同学们来去讲一个严肃的课题，叫做 send 协议站代理。那我们这一章当中其实主要来去从源码层面来跟同学们过一下 phone 组件，它的 contract 就是协议是如何来加载的，那么我们奋组建代理协议的这个过程，我把它叫做祖孙三代齐心协力。


我们来看这个底层代码当中contract， base contract，还有最后一个 Sprint MVC contract，它们这个三层结构，老爷子爸爸、

[image](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/31b11cbf-1880-43c5-93b3-75035ea64be4/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WTH6FVYZ%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T231335Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDipI0OT8JPX6w%2FZAUHdxNpQ9F5OPYu%2FVc970eMH9VuAQIhAP9Hyes2n0HwLqggsrKOt%2FtIBTU6Blrin7p1PRN%2B65%2BNKogECMb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1Igyn6WVz5L9Aq%2Bd4gckq3APW9XS5RsRksPH3Bsosx22GtyPXulfgkrYtgkzWpw8ymBxyBdDwfPJAR6sKav2YJ85L5Z2BkwEQloKjK8q33c6jRLu9Oc%2Bkjksa6OShuu3GwjSvlGIRjHZMyiXpkjPs5QWum9IoH8biM3GIBXhcbZGe%2FCBas2pStc91Jzj4YakYaCfMq3jxB85GF1oft4x%2FEgvRVBmLCr1mT24rMrRuXi3arsr1DMHG19ccCQOE3wy16x34XRlrSMuhDYaNm3BUxGYvjz1yipQjGSOHye8McLdndp4%2FZtai0WMD%2Ft9wIskWS8MC2WSotVPjVtW%2B6gfTGMfelJMGHKHlDl9bMHSI83vje06EHgXQk6Mats%2Fww8Na2QaYXhMTufAqBTaoB0K50BVyrI4BUVorApgGLggazw2vzJ9iN%2F%2BXSn5Qnr%2B2KUnKqav0puELSx3kuRiyTR1RnuEOIwug0Tbtg5rq04y56Bk934zLQnKndBKXtHBMpCWE%2FPzpmsseXpOz9zuNT%2F%2FIdfSX9EbLMhSofkuW0fRSf%2FGh7IfoYlpATVSXCKFBnl55W3Wyli8Tc6%2FCMbfWTCBcbNy%2F8fU9K%2F4KUAbo%2BpGw%2BNHe7U5M2SH94H8v9vg8Sgfvidpom7pdNstmT%2BHoRzDyuP%2FSBjqkARvlESebYo3yYTPRh29gFEDHdhKD6bE0QNCQGZOapVBszjLIuHhckDSighYEKFHRgTKfn7%2BO5C4IOMFDVuUQDWLjYCyyRV5K5F55queC0OWSwJCehzeZbBgYm%2FWmuW%2FNfObQtY07ia9okZ5FP1mQfC7XNpFh7N%2BfFkojO4eRd7P4qEzQQ8ayQMZTpcKmHXq6fvK7ywv5vfjp7blIglUb5XBczW4d&X-Amz-Signature=a6120aaee8d0e4d0766df8d0e54a281ce00980cfaeb6b3808133e4587d9be59a&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

孙子这三代是如何来共同完成这个任务的？好，同学们准备好的话给我们 entirely jelly 走起，写 bug 的每一天都是超越自己。我们这一节当中时间会有点长，同学们跟我一块儿从 debug 的入手，来去了解一下份组件的协议站的代理。那咱这边前面说过祖孙乙儿三代，那他的这个孙子是谁？这个孙子就是 spring MVC contract。okay，那这个孙子它是最底层的一个类，我们使用的是谁？是 spring cloud 的 MVC 的方案，因为我们暴露出了是什么呀？ rest 接口，所以它底层其实实现是通过这个 spin MVC 实现的。那咱这边我们先把代码的断点打到谁？


同学们，从这个方法名当中可以看出来我们这个协议栈的解析过程是怎么来操作的，就是说这个方法名它会在你的项目启动的时候去扫描你这些份注解，然后把它转化成什么呀？metadata，把它转化成元数据，那这样一来我就能知道你的这个份组件，你创建的这些接口，它的底层方法将要调用哪些的远程服务，就是通过这样的一个机制来去完成的接口协议栈和代理解析。


那我们这里开门见山，在这个方法的一开始，咱打上的是一个断点，然后紧接着我们怎么来去让断点走到这很简单，咱把这个 employee application 给它启动起来。但同学们注意，在启动的过程当中，我应该以什么方式对 employee service 启动的过程当中，我们要以什么模式？ debug 模式启动，咱写 bug 自然要用debug。好，我们稍等片刻，等这个代码走到我们的断点的地方。32，你看它抢跑了，走到了，那我们这里就跟同学们放大来，去挨个地解释一下它这方法是干什么的。那我们一个正常的开局，首先要去验证你的参数，比如说它的方法，这里通过两个 check state 来去验证你的这个入参 target type，它有什么异常情况，我们看 target type 它这里实际上它的类型是什么呀？同学们，这个字有点小，跟大家说一下，它是 rest room FIN client，也就说明咱前面定义的这个 FIN 接口怎么样被他给抓到了。


抓到之后我要去验证你的接口的定义，比方说第一个我去验证你 type a parameter，那如果你的这个接口它在当中定义了一些泛型，这时候我们就会给它抛出一个错误， parameterized types unsupported，就是说你这个泛型类型我是不支持的，那我们接着从这里可以看出你去定义方法的过程当中要去遵循哪些的规则。那我们接下来往下走。


第二个验证是验证什么呀？你看它的 get INTERFACES，如果你的当前接口定义的 INTERFACE 继承的 INTERFACE 大于了一个，那么我们这里也会跑出一场。为什么呀？因为只有单继承这边是允许的，你不能去继承多个接口，那这两关过去了之后，它在下面又来了，就说你当前的这个方法，这个 phone client 如果它继承有接口，那么这种情况下它会走到下面一个验证去验证谁呀？去验证你所继承的这个接口，它是否还继承了其它接口，非常的啰嗦，对吧？但是在这个验证过程当中，份组件是为了保证什么呀？你整个继承链当中，份组件要求有，且只能存在单层继承，因为接口层面是可以支持多继承的，那它这边只允许你去做单继承。好，那再往下我们就开始正儿八经的拼它的核心参数了。那什么呀？method，把你这个接口当中每一个定义的方法给它轮一遍。轮的过程当中，我们来看它这里去 check 哪些内容。


第一个我去对你的方法的 declaring class，还有它的这些 modifier 做一些判定。如果你是 declaring class，定义的是 object 类型，或者说你这下面的两个方法满足歧义，比如说你的 modifier 是static，你方法生命成了static，或者说这个方法它是一个 default 方法，那 default 方法的定义实际上就是被抽象非static。还有这个关键词，这是加 2 当中一个很生僻的关键词，那这个就是判断你是否是一个 default 方法，如果它是 default 或者是static，那或者它是声明的 declaring class 是 object 时候，那我就直接忽略你这个方法。okay。那对于其他一般的方法来说，我们这里是怎么样去开始解析它的这个 metadata 了？同学们看这里就进入了下一个方法，这个 pass and validate matter。诶，怎么觉着似曾相识诶？我们往下走，往上走，你看同学们这两个名字是不是一样的？一样一样一样的。那我们点进去一层，看它这里是不是到了一个什么桃花源什么之类的。好，同学们看到这里吗？我进到哪个类了？这个爸爸把他儿子给叫了出来，我进到了 spring MVC contract，那在基层结构上面来说，这个类它继承的它爹是 base contract，也就是咱刚才看的那个类。


好，我们这里来看一下这个儿子具体的孙类，它这里面会做什么事情？那第一个事情很简单，它通过分的这样一个组件，把当前类的特征变量给它抽取出来。怎么抽取？同学们，看，它生成了一串份独一无二的标识，那就是 class name，加上井号，再加上方法名，再加上你方法的每一个入参，那它是生成了一个独一无二的分组件的这样一个标示。


那生成完标识之后，同学们看他又呼叫他 the 父类 base contract，他喊道，爸爸，爸爸，我这边工作做完了，您有啥吩咐？我们来进来看他，爸爸这里做什么呀？爸爸，这里继续来拼装 Meta data，那在这个过程当中，前面几步非常简单，我去定义这个 data 的 target type，也就是你当前 phone 接口是什么样的类型，还有它的这个 method 当前的方法把它给也塞到这个 metadata 里面。与此同时它的 return type，还有 config type， config key，咱刚才生成的这个独一无二的标识也一同地把它加到了。


谁呀？加到了这个 data 里边， Meta data，然后在下面这串很长的方法我们就不一一来过了，跟同学们大致的过这样几个很关键的地方，比如说你当前的这个接口，当前的这个份接口，如果他这里有继承的其他的interface，那么这种情况下它会怎么样？它就会去检查你所继承的那个接口上面的一些注解，那对于某些注解，它注解上的标签可以继承到我们声明的份接口当中。


为什么呀？同学们知道为什么吗？这个秘诀就在这里了，就是通过这一步来处理的。OK，那对于我们没有去继承结构的这种接口，它这里就要去解析我当前粪接口上面的一些annotation，我们看它是怎么解析的。我们点进去一行好，点进去这里非常简单，它这边就是定点找这个对象，我看你类上面是不是定义了这个 request 的mapping，那如果我发现了 request Mapping，然后我这里就要去相当于说把你的这个 mapping 上面的一些值都给它解析下来，比如说这个路径的拼装就是在这个过程当中完成的。


我们这里剪一些关键的部分跟同学们说一下。首先这个方法它实际上解析的也是咱的 request mapping，如果你没有声明 request mapping，那它这里就跳过，诶，同学们会想有没有发现一点异常？我们在这个 restroom client 里面分client，同学们看咱这里好像没几个 u request mapping，对吧？只有这一个有，那其他的都是 get post，那怎么办？点进去我们来看这是什么呀？ request Mapping 对不对？你的 post Mapping，实际上它这个里面就藏着一个 request Mapping，那是这样的一回事，好，我们回过来去看，这个方法是咱的 check availability 这个方法，我们拿到它的 request mapping，然后在这边去拼 request mapping 当中的一些参数，把它给它抽取出来，然后组成 metadate 对象。比如说这里我就会来判断你当前的 request mapping，它所定义的这个 method 它只有一种，然后我们再往下这里去 check 它的path，也就是路径，就是说路径，我最多只配置一个路径，然后接下来这一段都是对路径的处理做一些拼装。


那拼装完成之后，那我这里就把这个路径的 path value 给它拿了出来，你瞧咱这边定义的是什么呀？ toilet service，一个斜杠 check availability。那接下来的这一二三这三行实际上都是来去专门处理你的purse，produces，还有consumers，还有headers，这些都是可以通过你的 request mapping 做配置的地方，那它们分别把它抽取出来，然后放到了这个 data 里面，那这个 metadata 里面。


好，那我们接下来往下走回一步，好，回到这里之后，我们就把当前方法的所有 annotation 全部给它拼装到了元数据当中。那我们继续往下看，它这里面还做了一些其他什么事儿，这里也是一个拼装状态检查，我们再往下走，这里到了什么呀？去该检查你的 parameter annotations。


parameter annotation 是什么呀？咱在这个接口当中是不是声明了很多的入参，你的每一个入参实际上也可以去添加一些annotation。同学们到这里应该想到这添加的是什么？ annotation either request a param，那这种 annotation 是不是就是添加在属性入参上面的？那我们这里如果我发现你的这个入参属性上面的 parameter 不等于空，那么我这里就要对它做一个处理，那怎么处理去来判断你是不是 h t p annotation？那什么是 http annotation？我们点进去看一下，那这里就是它的主要的逻辑了，同学们可以去顺着这个代码逻辑把它通读一下，那我们这里就不仔细的过每一个环节了，不过这里跟同学们讲一个小的注意点，咱看这个方法看似是指判断 SHDDP annotation，但是在这个过程当中，实际上你看它的方法名吗？ process 它还做了一些手脚，它会对你的这个 metadata 做一些小的拼装，比方说像这里 index to expander，那这里会去把 expander 给它加入到当前的这个 index 的 map 对象里，所以它是一个判断加处理二合一的这样一个方法。okay，那我们就直接往后走，那它具体是否判断 HTB annotation 是根据每一个 processor 自己的这个 process arguments 个方法来去做具体的判断，那我们走到最下面，这个是构建元数据当中的 expander map 的。


好，我们直接返回HTTP， annotation 是true，那如果是个 HTB annotation，我在 Metadata 里面把这个 parameter 去标记为ignore，然后我们接下来往下走。你看实际上像开源软件，他做这个方法的时候，写代码的时候，同学们看这个逻辑也并不是很清晰，你会看到很多 if else，就像 Palo t 一样。那在很多大厂里面，我们在提交代码的时候，会使用 Sona 来去跑你的代码层级复杂度。如果我发现你的当前的一个分支当中，它的子分支过多，也就是说它的 if else 这种分支过多的话，我其实是禁止提交的，他需要把这个方法做进一步的拆分来提高可读性。


那么分组件在这个方向上其实做得并不能说非常好，你看他这个逻辑就非常的绕来绕去，那我们继续来往下。如果我当前它不是一个 h t b annotation，并且你这个对应的 parameter 的类型，它不是这个 request 点 options 这个类型，那么这种情况下我会去对它做一个判断。


当前下标已经被处理过了，那么我们只做一个状态检查，那如果没有被处理过，那我们这里就要怎么样？就要去对它做一个处理流程，那我们可以看这两个状态检查，其实检查的内容都在这个 error message 里面，描述得非常详细了。比如说它这里用在 body 里面的 parameter 不能再去用在表单当中作为parameter，以及下面一行去判断你当前 body parameter 的数量。


那最后一旦处理完成之后，我会在这个 data 元数据当中把这个 boarding index 的标签的下标给它置上，以及它对应的type，那使用这个工具类把这个 type 给反射到好，那么再继续往下走，基本上你的这个整个的 contract 的构建过程就快要完成了。


好，那这两步检查完之后，同学们看下一步就是 query Mac map index，上一步检查 header 当中的map，这一步去检查查询参数的map，那它具体的方式实际上都是接近的。那经过这一系列的过程之后，我这个祖孙三代就齐心协力把这个metadata，也就是当前的这个方法的元数据给它构建了出来。构建出来之后，这个接力棒就交到了孙子 spring MVC contract 手中，我们接下来看它这里去怎么样。 find a merged annotation，拿到这个 merged annotation 之后，它这下面有一段非常精妙的容错逻辑。


怎么说？如果你前面去构造的这个元数据的 header 里面，你没有去定义这个accept，这个 key accept 是什么东西？平时用postman，你发这种 HTTP 的这种请求，它实际上默认都会带 accept 还有 content type，那这就是 HTTP 协议当中的标准的header，那如果你没有带，那这种情况下它就会做这样一件事儿，去把你这一步 class annotation merged annotation 上面去定义的这些属性，把它的 accept 值给它放到你的这个元数据当中。


同理，如果你的元数据当中没有定义 content type，那么处理方式一样，把这个 class annotation 上面的 content type 给它拿下来，放到 Meta data 里面，那经过这样的一系列步骤，这个孙子类 spring MVC contract 就完成了，它这边构建补充源数据的这样的一个指令。


好，我们回到上一层，那上一层这里又回到了 base contract，这里的原始的入口方法，这一步已经构建出了一个非常完整的 metadata 的对象，那我们如果去打开这个 evaluate 的模式，我们往下走一步打开这个模式就可以看出来它这个对象当中去定义了这个 config key 独一无二的份的签名，以及 return type 对应的template，还有对应的这些method。


那当前咱去解析的这个 method 是 check availability，那这部分属性都已经把它构造出来了，也就是我循环到当前方法的对应的这个 method metadata 已经把它构造完成了，那咱这边经过几次循环，依次循环之后，我就可以把你当前的这个份组件下面的类里面定义的所有的method，全部一一给它全部构建完成。那我们这里直接跳到最后一步，再跳一下。


好，那在这最后一步里，我们来看这个result， result 里面包含的内容，同学们看它是以什么作为key？以当前份方法，咱前面说过，从工具类当中获取到的独一无二的签名类名，加上方法名，再加上方法的入参的类型来获取到的这个一串字符串，作为key，对应的你当前 method 它对应的这些 metadata 作为一个value。


那经过这样的一个处理之后，我就把你整个粪接口里的所有方法，哎，我都给它规整起来，全部都给它的源数据处理好了。那到这里我们就跟同学们完整的看了咱的这个协议站，祖孙三代接力代去完成这样的一个 contract 解析的这样过程。那如果感兴趣的同学们可以就继续这个方法继续往下来debug，那你会看到在这个协议栈解析前后，它都分别由上下游组件做了什么样的其他的操作。


那分组件的代理封装实际上也是一个蛮复杂的构建过程，它的底层的代理当然也是基于我们非常熟悉的鼎鼎大名的这个 method handler 机制。如果同学们对奋发起服务调用的过程也比较感兴趣，可以就着这个点来去做，顺藤摸瓜继续往下做debug，来去了解一下这个 method handler 它构建的过程，在你发起一个 fend 服务请求的时候，也可以采用类似的方法，那来观察份组件是如何来去代理你的服务请求调用的。OK，那这一节的内容就跟同学们先讲到这里，那我们接下来再跟同学们去了解一下分组件当中的超时判定，还有重试如何来去做配置。好，同学们，我们下一小节再见。


