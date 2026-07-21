---
title: 3-4 表达式SpEL（1435）
---

# 3-4 表达式SpEL（1435）

[image](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/890e7318-f93a-4559-a1c0-3c25bfcc917d/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YKSBFSXV%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T232021Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDDhflgnlQGLzDCYtn2xALBMCco%2BvvINcOfKI0ldHjS9QIgPCGCBQ1rW2bTYf%2B%2BH3XUulZ2ZRn1CEK6DU%2BwJpQm3goqiAQIxv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDBDkX49uDdCY%2Fm42CyrcA2rUIxq6y%2Bd%2BAUbCSA%2BG8Aoa6kHg%2FkqxUTwptI7NYg8s%2FS0vJBNPLafyAQXGntxQzXpgsA3%2FlthW4X8w%2Fxd27MIiZqLHfyqIrTZBnglX4uhy0S3P%2F3a%2FpO9zbKNAHH7MVpbn5gg6rqnrOXy8awz5HLkahxMY8wLLjKaatth%2FI1yMeBKI1R%2FQJGY2B5ya7m%2FC3xn7I%2BXJYv3hr3nIwrDLmuTvb%2FoeeO23jBmSbyHl29H5wZGCIXrae44L8yUkCTrnRtb5nPLqrTSclI6l4KgA5lbQOfkCCVdpQMT8fFCmzA7NwL3ndMhv1%2FWg3QpPbodtgv788t39rtbq%2F9PRlCX4ilxdNpmLgl4hwteGF9%2FIlMrcVOAkzgvo3SseTXR0wvgGk5Me%2FR4OcFt2wy8zdTHHnHY%2FnbTDVElViBvnT%2B%2BorG7wAJWJsPVF71xTjqWsMOyfZurxsctcYc0WLbc4I4EBPw6IDCk3P%2B%2Bjp0jqj1QnubceZnYsHe6ikjIq2DQAccr3wXTm2JY0%2BcZ4h5baKDfeG65ufUH9oCl7UgF%2FM2gTKLj7XKxLkQ0e50WiorIQ2N%2F0YJsBAUyQV6LYWRUiJp1QJ5kuwRphEZJwSSUcEmJpa6fP0i6riLVE5XUAy6tNMPC3%2F9IGOqUBc2RZElUUe6JjK5yvAz3RyYJo7CCpiZfr5hH7EG0OoUjv92IwUsaJv8uFbfLXtfQ8Gw7msfgQOuW3C9l3nAaA56GsmkbPBXL%2B%2Fjf137svO1jZS%2BYFS4hyINx%2FYigzJPExqf77L80LjT53Izv0D138DG2RHY%2BKoqchAK4ZpsVAzajY8Td037DxWjt%2FNEq4tMcVSy01tKoQXUrenUXgUTcYhLq5LsP5&X-Amz-Signature=f0ab74c44234a190b417200e6b2dc8272be14945b72d78be7ba3094f4c3568cf&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

同学们大家好，这一章节我们来介绍 spring 的表达式语言。 spring 表达式语言全称为 spring expression language，缩写为S，p，e，l。它类似于 GSTLOGNL 这一类的表达词语言，能在运行时构建复杂的表达式，存取对象的映射属性对象的方法调用并并且当然 spring 咬它跟 spring 的功能完美整合，它可以用来去配置定义 bin 的定义，也可以读取 bin 相关的一些操作。


那么在我们介绍 spring 1R 表达式，我们首先来去介绍一下 spring expression 的工作原理，其次我们来介绍一下 spring experience 一些核心的API。最后我们来去介绍一下 spring URL 表的是一页应用实践。接下来我们首先来看一下 stream 表达式的工作原理，在这里面 stream 表达式它提供了一些简单的接口来简化用户的使用。我们在介绍原理之前的话，我们先学习一下几个概念。首先就是合法的一个 spin ER 表达式，它可以以井号或 at 符的方式去表达一个表达式的内容，那么同时它是需要一个与 spring 的一个表达式语言解析器去解析这个表达词，那么在解析的过程中，这些通配符的占用的一些上下文环境的一些属性是需要一个 context 变量，也就是我们的上下文信息去对于子去做一个替换的一个填充。


那么我们经过表达式，我们表达式解析器以及我们的三下轮信息，那么它执行的结果就是对应的我们的结果的输出，我们可以看一下在这里面我们通过这个合法的 SPER 表达四去，比如井号我们的username，那么在去解析它的过程中我们的上下文信息，在这里面我们定义一个map，像 username 对应的Jenny，那么它结果输出我们得到的这个表达式的结果就是我们这里面输出的几米。它的内容我们可以比较容易的明白对应我们这个表达式的值，它相当于从我们这个 map 里面的 KV 里面我们的表达式对应的k，我们的结果输出对应一个value，这在其他的一些表达式的逻辑处理上也是一致的。


所以说我们首先一定要清楚对于表达式它几个比较重要的概念，首先是一个表达式内容，其次是一个表达式解析器，另外也就是我们的三下轮信息在执行的过程中输出我们的结果，这就是整个我们表达式一个工作的原理。那么我们来看一下对于这些表达式哪些属于一个合法的表达式，我们可以看一下。


首先我们应该有一些是基本表达式，它是指比如说一些字面常量的一些表达式，像一些关系以及逻辑的一些运算符表达式，还有包括到字符串联它的一些计算或者一些截取的表达式，包括我们计算的一些三木运算符，正则表达式，还有一些括号优先级，这些都可以理解为是我们基本表达式所覆盖的内容。


另一个人是可以理解为是类相关的表达式，那么对于加 2 语言里面类似比较多的，我们可以比如说是类的实例化，包括我们 new 一个对象，或者说是我们判断这个类的属性，我们比如说以 sum off 表达词判断一下这个类是否是某个接口的一个实现，以及定义一些变量或者一些语音，还有一些赋值表达式。我们自定义函数或者一些静态类的方法的读取调用，以及对象属性的一些安全导航的一些表达式，像对象方法的调用以及 bin 的引用，这些都是我们跟类相关的一些表达式。另外还有一些是跟我们的集合相关的表达式，这里面集合相关的表达式，比如说一些内敛的 list 或一些数组集合，比如说一些字典，访问列表等等，包括集合的投影，集合选择。当然这里面是并不支持一些多维的数组初始化。


好，这是我们可以理解为我们常见的这些表达式的类型。那么接下来我们来看一下 spring express，它一些核心的API，在这里面我们可以看到在嗯最重要的表达式，一个核心API，也就是expression，这就是我们通过表达式文本解析生成来那个解表达式内容。这里面我们可以看它里面有两个比较常用的实现。对于我们的表达式解析器，这里面最常用的也就是 SPER express Pros，它作为我们表达式解析的内容。同时这里面我们需要的一些上下文信息的一个包装，这里面 evolution context 的，这里面有 simple evaluation context 和我们的一个标准的 evelution context 的，作为我们 3L 解析的一个过程，那么对于我们这个表达式解析器，它支持一些自定义的配置，也就是通过 SPL press configuration 这种方式去配置我们的表达式解析器执行的工作原理。


我们来看一下 spring 源码里面关于表达式实现模块儿的定义，在这里面整个我们 spring 的官方源码里面， spring express 是一个独立的一个模块儿，并且这个独立模块它是相对比较基础的，我们可以从这里面看一下，对于这个 spring er 表达式，它只依赖了 spring 的一个核心模块，所以充分说明它更多的是被其他模块儿所依赖。在这里面它的实现的包结构是 spring framework is present。


在这里面最重要的，我们看几个相关的我们的比较关注的，这里面是我们的表达式的解析器，对于表达式解析器，它提供了两个解析的方法，我们可以从这里面看一下它的结构。在这里面一个词，我们直接解析这个表达式，也就是表达式的文本。另一行，我们在解析的过程中，我们支持我们一个 plus context，嗯，也就是传入我们解析的定义的一个上下文取空间。但是注意一下，这里面并不是我们刚才提供的上下文信息的类。


我们再接着看它其实解析的结果，它解析出一个表达式对象，这个表达式对象也就是它可以理解为我们对于一个原生的表达式，经过编译后的一个可计算的一个表达式对象。对于这个表达式对象，它里面的方法这里面是会比较多了，如果说它不需要上下文空间的话，我们可以直接通过 get value 获取到这个表达式的值，那么我们在普通情况下定义的这些变量，我们可以通过 get value 的方式去获取这个值，它不需要其他上下空间一些填充。


那么对于一个需要做占位替换的这些内容，我们可以使用 get value，我们传入一个 evalucase context，也就是我们的上下文信息来去计算它里面的内容，其他的这些值我们可以跟这里面的简单的去除对比，我们就不再一一的介绍了，嗯，下面我们可以看到这里面还有一些对于一些枚举，比如说它支持的一些操作符，在操作符里我们可以看到它这里面是一切是加减乘除相关的一些内容。


其实 spin 医疗表达式它作为一个语法树的解析是非常复杂的，在这里面我们可以看到在 SPR 里面它一些实现，我们就不一一的去翻代码去看了，我们可以重点在这面看一下。对于一个标准的实现，这里面有一个，也就是我们在语法处解析过程中一个token，也就是切割的一些关键值，我们可以看到这里面涉及到一些大括号、小括号、一些警符号等等，包括一些我们的计算、运算服务等等，这里面我们可以看到还有一些比较的一些运算服务在下面有，这是跟我们的 Java 实现相关的。


这里面是像 external 和 mass between 等等，这里面还有一些边界的一些运算，我们可以看到在这里面是有一些 bin 的，也就是我们在如果涉及到容器里面 bin 读取的话，我们看这里面是 at 开作为我们的前缀，如果是我们的factory，也就是我们这里面是有我们的语符号等等这样一些操作。其实在这里面还有涉及定义了 three 一二表示的一个语法树，这里面解析来说是相对比较复杂的，这个我们就不去详细介绍了。


那么回到我们PPT，接下来我们来看一下 stream 表达式的一些使用实践，好，我们切换到我们的工程模块，嗯，在这里面我可以看到我们在还是 spin scale，在这个工程模块里面我们在单元这 4 里面我们加了一个 string EX scale test。在这里面我们可以看一下这个单元词的实现内容。


首先我们定义一个表达式的一个解析器，这个表达式解析器我们就用默认的构造方法解析完成。那么在这里面我们通过这个解析器解析我们这里面构造的这个字符串表达式，也就是这个内容是我们那个表达式的内容，这个表达式的内容我们可以简单解释一下。首先是这个表达式虽然是一个字符串，但是它里面也有一个字符串对应的变量，这个字符串作用变量就是end，那么字符串对应的常量也就是这个字符串，就是像 hello world 这个我们可以理解为文本的内容，它通过一个加符号作为一个字符的一个连接符，把 hello 沃尔连接起来，同时又调用了我们 Java 里面 string 的 contact 的方法，就隐私的调用 contact 的方法把这个变量 end 去连接起来。


那么在连接的这个过程也就构成了我们这个表达式的解析内容，我们解析得到这个表达式内容以后，就可以通过不同的上下文信息去解析不同的变量，那么我们看这里面，在这里面我们定义了一个 evaluation context，对于这个 context 我们设置了一个变量，这个变量的 case end 对应的它的结果是一个感叹号。在这里面我们可以看到对应这个 end 和这个是一个对应关系，也就是它作为一个k，它作为一个value，在解析的过程中会把 end 取出来替换成百分号这样一个值，那么我们接下来去看一下它去真正解析的过程。


我们这里面通过一个 present get value，同时把我们的 3M 信息作为参数传入，那么在执行结果就得到一个value，这个 value 的内容我们刚才介绍的是 hello world 对应的是百分号，我们去跟它去做一个断言的执行，那么现在我们可以执行一下，看一下它的结果。


好，如果执行正常，我们断言断校验成功，也就说明它现在可以就是正常执行成功了，那么这是我们第一个我们可以用来去解析的这个表达式的使用案例。那么接下来我们看下面这个对于一些简单的变量的一些表达式，在这里面首先我们来看一下，这里面我们定义一个也是一个普通的表达式解析器，这个表单式解析器，嗯，我们可以看到这是作为一个普通的字符串，作为解析的话我们得到的内容也就是 Hover word 对于我们是一个 double 类型，我们看这里面是 1. 024，我们这里面 1 + 3，这是作为一个 double 数值。我们去解析的过程中我们得到一个 double 的value，这个 double value 的值跟我们正常这样书写的值是一致的，下面我们可以定义了一个是一个 integer 类型，也就是一个 int 常量，对， int 常量，这时我们可以看到这是我们的 int 一个嗯，值。我们在这里面去执行它的值的话，也可以跟我们的字符串的这个值一一对应。


上，接下来我们对于一个布尔类型的操作，也可以用，这里面我们定义true，那么我们通过 get value 得到的值就是布尔类型的一个 true 值。下面我们在这里面定了一个 null 值，对于 null 值，我们 get value 我们得到的对象就是我们 Java 里面的null，这个值它并没有得到，一个是真正的对象得到是个 null 值，这是对于变量的一些描述的方式。


接下来我们来看一下对于一些可替换的变量的一些操作，在这里面是跟我们第一个用例是类似的，我们在这里面是定义了一个 my name，这里面我们把 my name 的作为构建成一个是一个 context 的去展示出来，我们在这里面执行的过程中，可以把这个 my name 通过对应的机密替换完成，这样也就做到了一个表达式值的一个替换。
我们看下一步在这里面我们定义的是 new string，我们在这里面注意一下这是一个单引号，我们这里面构建出这个表达式，其实跟我们这里写的 Java 语法是一致的，相当于这个表达式语言可以去解析我们 Java 语言的一些内容，在这里面我们可获取到的内容也是对应的机密，这是我们介绍的这种方子，也就是我们可以支持类似于 Java 语法的一些书写。我们接下来看一下可以去获取避孕容器的一些场景。


在这里面我们首先来看这个表达式，我们在这每次构造了一个宾容器，这个宾容器它的一些构造的来源是configure，这个 config 内容对于这里面我们只定义了一个bin，这个 bin 就是我们的 user view，对 user VO 进行了一个重用，在定义这个 user VO 的时候，我们定义它的 name 是 Jimmy is 是18，也就是说它的姓名和年龄。在这边定义完成以后，我们在这里面构建这个标准的一个 evalucation context，也就是我们执行的 3F 信息，在这个 3F 信息里面，我们设置了一个 bin resolver，也就是我们的 bin 解析器。


这个必应解析器是怎么构建出来的？这必应解析器是通过 bin factory slower 作为构造方法，它传入了我们当前这个容器信息，就是 application context，或者说是一个 being factory 都可以传入进去，那么就可以去获取我们这个容器里面的必应信息了。我们在这里面去构建一个表达式的解析器，这个表达式解析器也要解析的表达式就是艾特 user name。我们刚才有印象，我们取 bin 里面的容器里面的 bin 的时候，我们通过 at 作为我们的参照符，那么 at username 其实相当于是获取了我们当前这个容器里面的 user 对象，获取完 user 的对象以后，点 name 相当于是我们对象的一个图形映射，我们是映射到 user VO 里面它的一个 name 属性，也就是我们这里面定义的机密。那么我们通过这样的话执行完成以后，我们去 get value 去获取这个值。我们定义了我们的 3L 环境，是这个 context 的同时获到一个 stream 类型的一个值，这里面我们能得到对应这个机米的类型。


好，我们可以执行一下，看一下效果，在这里面我们也得到了正常的我们所期望的这个值。好，回到我们的PPT，在这里面我们跟大家介绍了一下 string 表达式的一些用法。好，这一节我们就先介绍到这里，同学们，我们下一节再见。

