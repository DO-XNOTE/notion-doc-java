---
title: 4-2 二次改造-自定义Repository实例（1148）
---

# 4-2 二次改造-自定义Repository实例（1148）

[image](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/6a840722-10e0-4315-951f-1c79ab3234f9/SCR-20240814-jolk.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46664LHAZ64%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T232146Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQC%2Bw3yaYf5JUXJ8ajhn5jwq9e2OJuU2Ruzks5W2yIUSZQIgYXt3u5i3X2kN%2BJ1g%2B%2FmbF%2Fboe0vbGhhdvPy4PSa0QpEqiAQIxv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDJ%2FHtuOtnEBz5NCMUCrcA9hP5Z%2F61dHGQTnVEXIUWzP9h7umzJUJTcbUE4N8%2BucUOir4yBj3es5xZi14Ob0TbFJoqphvkganz639F%2BAN8ziuSd5vUA7BpvDFoIW65OfVPMT37jPvpDWVQ%2FivNLmxSOj75eFv0K4%2F69p7zw7j2pC0TiazBnM3MRNywqyUYnGenkBVnSYWGcFqzTYu3fnXrNwqYQ0jVpI7QyL3K4y1k54d0O%2Fq8VbDSNht0aNSGusUE2sWgluxyNWBzsvqqFVd6rFKoECGtdXvrUocPObEOfLSBy8%2B3qa0UT5peOOxmcLgE2eO6IM8%2FSnAhCMl8sF%2B4A60vR7%2B%2BnVNdOtegAd%2BoQnN3KXJtXe6x3RF1lGhUzn5kwlVcEId6ooNa%2B33cJWU8uzSlqXWNNfBzaSFFfWm6gsNTCGJ847Ww6EjxTtQqH8CxOo7fCn2vBLKek1mQm2VXHHVviD3llhhOUlILjIwNlOUu54Hn%2B16a6G1Zlw7nub24dA%2BNfULlkTaCt2RdRdU4zk4hRzYypUvHtSmCQ%2FZ7eAM4rjqQ7s5JwPGfirv3ZpWPQ1mzyxF8Dv28Butn7Vb48nCbcwpzuiHcEhmt%2Fr6c6JR7Nzn%2BmRUW1P1suIrQVt4B2N5L%2BFaAYHtBw8%2BMIa3%2F9IGOqUBao4I1NTg3LieLVI%2Bvt7v5YTCVC8sonqC1HbqFvw5bJf43f3KFYP04ktWeV9FkeUZIzz%2B5HaIDDHUKURiBqtSSK0Gj%2B1D29esGJCdThfI7Po1s6pnWcetcr%2FnSxTz%2BPlnTbDV52DzM7DZkXnyRllf5Ts3qZzUzTt4F0N5P2Kx8IPQrSRciQXhV5PyUw8%2F6suE4ezTaxyEeqRF8lGRLlYaaEOps%2FrF&X-Amz-Signature=8a69ec29d88cb01156da8766f80134c9ef06827d1cee04546c88576b8395047e&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

同学们大家好，这一章节我们来介绍 spring date 的二次改造，自定义 REPORTS 的实例。这次二次改造还是基于 JP 来实现。我们知道 JP reporter 它已经实现了很丰富的蒸三改偿的功能，同时也支持方法命名的查询，以及基于 add query 注解的方式，手动拼写 GPAQR 语句来制定一些特殊的查询。


随着我们业务复杂性的增加，总会碰到一些情况，我们的使命 d 的GPT，它不满足我们的要求。这种情况下我们需要怎么去制定与扩展？比如说我们需要依赖 GPA 的 entity manager 来去完成我们自己的实例，我们怎么去做？通常如果说我们不使用 spring day 的GPA，只使用 GPA 的话，也可以通过 entity manager 来完成我们基于 GPT 实现 have net 操作的一些工作。这里面我们既要满足我们特殊的需求，我们还是想使用 spring day 的 GPT report 这种优雅的接口命名的方式来去查找。那怎么办呢？这里面带给大家一个实例来跟大家去演示一下我们怎么去自定义report。实例还切换到我们的 showcase j p a 这个模块儿。这里面跟大家去演示一下我们如何去定义一个 customer report。这里面通常我们使用 user report，它是extense，也是继承我们的 JPA reportery。既然继承了我们的 JPA reportery， JPA reporter 以及它所继承的像 pacing and sorting 的report，以及我们向更上一层的 CRUD 的report，也就是它把这些方法都积累起来，它拥有这些所有的方法。
从这里面我们可以看到这些方法其实已经很丰富了，对于比如说count，delete， all by，ID，invats，就是批量相关的一些操作，这里面还涉及到一些查询操作， find all 以及根据 example 的查询条件来去查询等等。从这里面去看，我们这些方法其实已经非常丰富了。


如果说即便这里面方法不能满足我们的需求，可以在 user reporter 里面我们基于一键名称查询。比如这里面是 find by name，我们会生成对应的 select 形 user select from user，对应 where name 是指定参数的一个查询条件，以及我们是 find by states 也会生成类似于的查询条件。


对于这些简单的查询条件，我们可以基于方法的命运查找生成对应的 SQL 语句去执行。如果对于一些比较复杂的 SQL 语句，我们也可以基于注解 at query 的方式来去完成。通常对于 at query 我们理解为是一个读的操作，假如说我们需要执行一些写的操作，这里面我们可以通过 at query 和 at modifying 去组合起来进行这样相关的一些处理。其实即便我们有了这么丰富的功能，可能还是有一些同学他不满足当前的一些应用场景怎么办？我们需要制定一些查询操作，这里面其实我很难去跟大家去拓展更多的例子，比如说我们希望在执行的过程中增加一些日志类的操作，或者说进行一些计时监控相关的操作等等，这都是我们可能去发挥的一些场景。所以说这里面我们可能需要根据我们自己的业务需求制定义的方法。比如说我们可以看这里面需要定一个 customer save 以及一个 customer find all，当然因为它默认的场景不满足我们的需求，我们需要自定义开发。


具体我们自定义的逻辑怎么写其实关系不大，需要关注的是什么呢？可以在这里面写我们自定义的实现，而不是直接依赖我们对应的 simple GP reporting 它默认的实现，也就是说我们可以支持一些自定义的改造的操作，所以说既然能支持这样，通常如果说我们直接依赖我们的 entity manager 是可以做这样操作的。


这里面我们还是期望能优雅地使用我们 report 这样的接口，比如说我们可以看到这里面我们在这里面定一个 customer user reporsely，那么我们可以基于 customer user reporting 来进行我们相关的一些操作，这样的话对于我们自定义的方法的实现也能非常好的去运行起来。这里面我们看一下是怎么实现的。


首先我们在这里面定义我们 customer user repository 这样一个接口，接口儿里面定义了两个方法，一个方法是 customer save，引用我们自定义的一个 save 方法，另一个是我们的 customer find out 支持一个分页儿查找的方法，在这里面其实它具体的实现逻辑是怎样的，我们并不关心，我们关心的是我们可以自定义实现。只要我们能做到自定义实现，那么我们就可以发挥我们自己的天马行空来满足我们自己业务的场景。当然如果说我们能基于我们 add query 注解或者我们的方法命名去满足的话，这样是最简洁的。


首先我们看到这个 customer user report，这里面我们定义对应的一个实现，对于这里面 custom user reporter，我们可以看一下。我们先不关心它继承了，我们这里面 simple GPT reporter，当然这个继承不是必须的，但如果说我们想去制定实现，我们首先定义一个实现，我们这是 customer user reports MPL，它实现了我们这样的接口，也就是 customer user report 这个接口词。


建完这个接口，这里面因为我们是继承了 simple GPT reporsory，需要去满足 simple GPT reports，它的构造方法，我们可以看到在这里面它涉及到两个构造方法，可以看一下这里面两个构造方法，第一个是支持一个 domain class，另一个是 entity manager。也就是说我们在构建的 simple GPT 是我们首先要指明一下我们操作的领域，对象以及实体类是什么。另一个是我们需要跟 GPT 关联的 entity manager 对象需要传入进去，因为我们注重所有的操作都是基于 entity manager 进行代理GPA，这里面进行一些对应 GDP seed 操作，另一个方法我们可以看到它是用的是 GPT information，这里面含有是 entity manager，也就是说我们可以基于 GPT information 来去完成这样的跳转。


其实大家可以明白，也就是一个参数，来说明一下我这个 simple GP reporter 是操作哪个类，它就是解决这个问题，一个是通过 GPT information 来描述，一个是通过一个 domain class 来描述，最终它们的结果是一样的。


理解了这一点，那么我们在构建我们自己 customer user report 实现的过程中，我们需要满足我们 simple GPT report 构造方法，这里面我们调用了 super 指定了一下user，另一个是我们的 entity manager，这里面我们可以看到我们这是 customer user reports MPR，因为我们这里面所有的操作都是针对 user 对象进行操作的，所以说我们这里面可以理解为我们是写死了一个 user class，标明这个死线类，它只能对我们的 user 对象进行正态改造的操作。


另一个是 entity manager 这个对象，我们应该知道在我们 string day 的 GPA auto configuration 初始化的过程中，它会把我们 GPA 相关的一些利益的初始化完成，其中的 entity manager 就是 z p 需要强制依赖的这样一个b。所以说我们在这里面构造方法的时候，当我们的 string 构造这个 customer user reporter MPL 这个实例必应的过程中，它会自动的把我们的 into manager 这个 b 注入进去，所以说我们这样的话，我们 add out where 或 add resource 的方式引入一下，所以在这里面我们同时我们把这个参数赋予我们的Instagram，这样的话我们可以在customer。


user 对应的 report MPR 的过程中实现依赖 int manager 来实现我们的内容。首先我们看一下 customer save，对于 customer SIM 的话，我们这里面是参考了对应simple，我们这里面是 simple GPT reporsory 它默认的实现。首先判断一下我们的 user ID，对应 user ID 如果说等于 null 的话，也就是我们理解为它是新增的话，我们执行 preset 就是持久化的操作，如果它的 ID 不等于now，也就是它 ID 是存在的，那么我们就执行更新的操作。这里面是merge，也就是把变更的数据 merge 到我们的实体对象，更新到数据库里面，这就是我们 cost receive 实现的一个内容。这里面我们同时打印日志，可以加入一些监控来满足我们的实际场景需求，也就是说我们通过这种方式就能实现。


对于我们 repository 调用方法里面的内容由我们自己来定义，自己来实现。同时我们来看一下 customer find all，甚至我们可以直接调用我们 super 相关的一些方法，或者说我们调用指定的一些方法。对于 custom find all，我们这里面并没有说做什么特殊的逻辑，只是打印行日志，同时调用了 this 的 find all，把我们的配置对象传入进去，这样就能满足复写默认的 simple GPT 里面实现的一些内容，这样的话我们就能做到。所以看一下我们做了几件事情。


首先我们需要定义我们的 customer user repository，定义出我们这个接口，通过方法命名来去描述我们这个接口做什么事情。另外我们去实现我们的实现类，我们的实现类是customer，我们的 user report MPL。至于它是怎么实现的，其实我们不用具体的去关心是怎么实现的，只要是我们能理解它能自己实现就行。


通常这个实现它会依赖 entity manager 进行一些操作，但如果说我们对于修改的更加保守的话，我们甚至可以依赖 GDVC template 进行一些操作，操作完成对于我们的一些数据进行一些序列化或反序量的一些包装的一个过程。同时如果我们这样的话，其实已经能做到我们基于 customer user REPORTS 来进行一些操作，但我们这里面可以使用的更加畅通。我们可以看到我们对于 user report 的扩展的一些方法。扩展方法，我们怎么通过 user reporter 使用一个比较好的方式是我们 user reporter。方法除了继承 JP reporter，同时也让它继承了我们的 customer user reporter。当我们的 user report 继承了 customer user reporsory，我们的 user report 它也具有了我们这里面 customer user report MPL 它构建的这些功能，这样我们怎么去看？我们可以看一下我们单元测试，在这里面我们看到我们是 customer user report test，在这个 report test 里面我们引入了我们的 user report，基于 user report，其实我们知道我们要测试的是 customer user report，直接命名是 customer user report，在这里面我们执行 cost find all 或者我们执行 cost seal 都可以能执行我们正常的操作。


通过这样一种构造的话，我们发现我们完成了基于 user reporsory 自定义扩展方法的功能，也就是说我们虽然是继承了 JP repolicy，可以通过我们接口扩展的方式扩展它的一些实现类的方式，其实这样还是很方便的，这里面我们执行一下单元测试，看一下它的结果，我们看这里面很快执行完成。


这里面我们可以看到它执行的词口语句，也就是我们这里面的select，这里面 select count，因为我们要分页查询，我们一定要查询出它的总数以及它的 count 数。结果我们可以看到这里面我们打印出度迭代的情况，这里面我们的优势对象通过 ID 为 12345 去把我们的信息打印出来，那么这样的话就完成了我们这个自定义的操作。那么我们通过 string t 的 GPT report 制定实例的方式来跟大家去介绍对于 string t 的 GPT 的扩展是多么的方，便，我们也可以通过这种方式去依赖 GPT manager 去做一些更灵活的操作。当然，我们甚至可以在同样一个 report 里面操作多张表也是可以的。关于自定义 report 实例的内容我们就介绍到这里，同学们，我们下一集再见。

