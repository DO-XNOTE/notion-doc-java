---
title: 3-26 【技术改造】电商系统集成Eureka - 商品中心-2 
---

# 3-26 【技术改造】电商系统集成Eureka - 商品中心-2 

[image](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/d80a0e79-9160-41bf-8fda-883b30570fbf/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WUDDJBOV%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T225553Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIAK4d0CECCeiP7uIM%2BL%2Bew5AjRfIoYYi2Zsdb6PRlB1nAiBQH9i4kG9nGoL6fXtRkVRqo%2Bqx%2BLJN2RaZD6cGYXjJgSqIBAjG%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIM5r3RpSopa7%2B4AFiZKtwD0xMSZsYDzxC%2FVwQTIrP1aRqNWkDqjHfwfCoSkwvcPJW%2BZbmOt7jKrBeske4u3iF56tXyZC7mMe6oCFwU96kj0Vxk2BAFMkzRt4H4BZztPIRANUYaVd%2BWllmkXSq%2BiffjYz4qaWfEipTEav5nMCXwr15ETxELwplo8igU7jEiGWIzdIuhOewXGE6vhI4jdSI3Fh2Do9yawvB0%2FdvYwcJxwflLAGbxuBN2iijr6zGXNhSaITRnkX7JlzWjRGCT5ONvwlBkJTq6N8tk8iT%2BHQDeu8Egsl88kAV%2FQAYPQQThUWRz7CyqfJXAij%2B95uUYyuoZF%2FjUxqmssstowohDExEWpZr4eSxDhkctZtEbdREWqrKQoMlQ3SVzqT%2FzADiFHGKIln9uezAyU3MUKVxZu1ivRdVI1Ym12FktCmnyqnVx62KXgLWms552RQghrotQa9k7ooN%2B7qJKyzmz2jISFDt2KhkbBkLvJPmY0rGg2TSl4dKfBH%2Ft5eFAr1BIZtuDiaSgEAxDJdk5k4KRwZB1N%2BoNz%2Bflv5V%2FjYlnb2GeSJkq2Hh41GAF%2By%2FlSF%2FxEIbvjQ5XyGTFpKugAQjjGvjlKARoqjVnCwNRJJRBZuJaXeuiOWxBMg28190vCOFoe2gwjrr%2F0gY6pgHzrrC0UPXmr9sVlbtcJ1Mt6ZSX6ouU4XQIlRfPowYd0SIY0%2FTJBJ0HC%2B37l6Q2j1awlC%2BaiUf693GrwTukqdu7TqU1uIlVzqs6hqI43T0IkEnIV1pnongxIB0R40QKmUXtQjAL%2FwJ%2FwLdiGUQaueNEF7DcKokj1l5sEprLhByQj04clC6NkEVYm7G43MJa%2B3wlN6tfBzfB6OGfqRgK9F7fCAdyaSp%2F&X-Amz-Signature=609de4c166cad9f72b0fe4b2e7e25b5c7f5866bbfb2598ca22b6eb0e2cfc2ba9&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

[image](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/d5418516-c02f-45b0-925e-becef55e4a22/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WUDDJBOV%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T225553Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIAK4d0CECCeiP7uIM%2BL%2Bew5AjRfIoYYi2Zsdb6PRlB1nAiBQH9i4kG9nGoL6fXtRkVRqo%2Bqx%2BLJN2RaZD6cGYXjJgSqIBAjG%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIM5r3RpSopa7%2B4AFiZKtwD0xMSZsYDzxC%2FVwQTIrP1aRqNWkDqjHfwfCoSkwvcPJW%2BZbmOt7jKrBeske4u3iF56tXyZC7mMe6oCFwU96kj0Vxk2BAFMkzRt4H4BZztPIRANUYaVd%2BWllmkXSq%2BiffjYz4qaWfEipTEav5nMCXwr15ETxELwplo8igU7jEiGWIzdIuhOewXGE6vhI4jdSI3Fh2Do9yawvB0%2FdvYwcJxwflLAGbxuBN2iijr6zGXNhSaITRnkX7JlzWjRGCT5ONvwlBkJTq6N8tk8iT%2BHQDeu8Egsl88kAV%2FQAYPQQThUWRz7CyqfJXAij%2B95uUYyuoZF%2FjUxqmssstowohDExEWpZr4eSxDhkctZtEbdREWqrKQoMlQ3SVzqT%2FzADiFHGKIln9uezAyU3MUKVxZu1ivRdVI1Ym12FktCmnyqnVx62KXgLWms552RQghrotQa9k7ooN%2B7qJKyzmz2jISFDt2KhkbBkLvJPmY0rGg2TSl4dKfBH%2Ft5eFAr1BIZtuDiaSgEAxDJdk5k4KRwZB1N%2BoNz%2Bflv5V%2FjYlnb2GeSJkq2Hh41GAF%2By%2FlSF%2FxEIbvjQ5XyGTFpKugAQjjGvjlKARoqjVnCwNRJJRBZuJaXeuiOWxBMg28190vCOFoe2gwjrr%2F0gY6pgHzrrC0UPXmr9sVlbtcJ1Mt6ZSX6ouU4XQIlRfPowYd0SIY0%2FTJBJ0HC%2B37l6Q2j1awlC%2BaiUf693GrwTukqdu7TqU1uIlVzqs6hqI43T0IkEnIV1pnongxIB0R40QKmUXtQjAL%2FwJ%2FwLdiGUQaueNEF7DcKokj1l5sEprLhByQj04clC6NkEVYm7G43MJa%2B3wlN6tfBzfB6OGfqRgK9F7fCAdyaSp%2F&X-Amz-Signature=6dfdea1d5117e8f5074c1e78a1040dabfe039a1cf4bbe24d62d2dc97999d2feb&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

慕课网的小伙伴们大家好，接下来咱继续改造商品中心，咱创建完了 food item por 酒和 mapper 这两个毛酒之后，接下来创建一个接口层。那这个接口层顾名思义，它里面只包含接口，其他没有任何业务逻辑，它叫 foodie 杠 item 杠 API 这个 API 可不是咱之前在 foodie DEV 项目中用的API ，它这里只是包含接口层。好点击 next 把它扔到哪里，依然是扔到 domain 杠 item 咱们商品域的这个文件夹当中。


那接下来，在接口层中我们引入 dependency 咱前面提到了接口层是用来做什么供其他微服务发起调用的。所以接口层的依赖尽可能要保持纯净单纯一点，不要引入过多依赖。这样的话别人在引用你这个接口层的时候就不会发生大量的依赖冲突。好，那我这里 dependency 里面要添加哪些内容呢？在这一节当中只用添加三个内容，其中两个是咱的自己人，就是说咱前面自己创建好的项目。那这里第一个项目我把它引入进来，它的 artifact 是咱前面创建的 foodie 杠 cloud shared 泡酒。那咱当前的这个 API 层也要用到一些公共的泡酒类。所以咱们把这个 artifact 引入进来，它的 version 我们指定好，同样的是 project.version 把它复制一下。


第二个依赖是咱前面创建的 item pojo 在 item 的 API 自然需要把 item 的 portal 也给引入进来。 OK 那接下来第三个 dependency 是谁呢？我们来看，这个 dependency 看起来和接口层无关他是 springboot 它的 artifact 是 spring boot starter 然后后面跟的是杠 web 咱为什么需要 web 呢？因为我们要提供一个基于 htd P 的，可以被注册到 eureka 服务中心的微服务。所以我们要把自己的 service 声明成一个个 controller 因此咱把这些 controller 的路径 request mapping 等等声明在哪呢？声明到接口层里。这样做的目的其实是简化服务间的调用等。


后面我们学到服务间调用分组件，大家就知道这个用意了，它在这个 dependency 里面，这里还需要再加入一个 dependency 他是谁的？咱还没有学到他是分的 dependency 所以我们这里加一个 to do 分 dependencies 等。后面学到这一章的时候，我们再把 fen 引入进来。 OK 那咱的依赖已经声明完了，接下来去创建代码，我们在 Java 文件夹下面创建一个 directory 这个 directory 的路径是 calm.eye mock.item.serviceok 回车。


好，咱在这个 service 里面要引入两个类，第一个类我们去到 foodie DEV 当中把它 copy 过来。哪一个类呢？我们搜索 item service 好，就是你了看这里有两个 item service ，一个是接口，一个是实现类，咋引入的是这个接口，把这个接口复制一下再切换回复 D DEV 当中砍微服务改造实际上就是一个复制粘贴抄作业的过程。


好，那咱把它复制过来以后有哪些需要改动的呢？当然了，因为我们的包路径都换掉了对不对？所以这里需要把包路径改成正确的路径。那它的 import 这里几个 VO 对象，我们要在前面加上 items 把这个路径配对我们这里要把它重新引入进来，因为它的包路径换了换到了 pool 下面。 OK 那这样一改是不是就不报错了？那还改完了吗？没有。我们这里要对 interface 层做一番前所未有的改造。什么改造呢？加上 request 因为我们的接口层要对外提供服务了，所以待会儿我们会把它声明成一种 controller 这些 controller 上面自然会有 request mapping 还有一些路径的配置。那么我们把这些路径配置在接口层，这样的话，你在接口上声明的这些注解就可以继承到你的实现类当中，这是其中一个好处。


第二个好处是，当以后学到服务间调用的时候，我作为一个下游服务调用你 item service 的时候，我通过 fin 组件来调用。那这时候如果你接口上已经声明了 request mapping 以及 get mapping 之类的路径信息，那我调用方直接拿到你这个接口就可以去做寻址了，这样的话就避免了我下游应用还需要再单独配置一套寻址路径。


好，那我这里 request mapping 给它起什么名字呢？我把它起名叫 item 杠 API OK 那这里起完名，下面的每一个服务我们都要给它配置不同的路径，同学们这里可以随心所欲地起名字。老师这里就按照 rest 接口的规范，比如这一个 query item by ID 那它看起来是一个 get mapping 对不对？这里把它起名 get mapping 它的路径就是 item 实际上咱在定义路径的时候，如果采用 rest API 的格式。那么通常来讲我们不用定义成 get item 不用定义成这种格式。因为什么呢？这个 get 这个语义已经被下放到了哪里的？被下放到了 HTTP method 这里讲是个 get mapping 本身就有这个 get 语义了，所以通常来讲这里直接是一个 item 就好。那如果是delete ，它的路径依然是 item 这个 delete 的语句就把它下放到了 delete mapping 当中。所以说这是 rest 命名的一个规范。


好，咱这里起名叫 get mapping 那接下来一个 query item image list 这给它起名什么呢？也给它叫一个 get 好了名字，大家随便起了叫 item images 这样就可以了，或者把它打全称叫 imagesok 那第三个也依然是 get 请求 query items back the list 那给它起名叫 item spect 是不是很简单啊？那第四个也是 query 你只要牵扯到查询语句，通常我们就用 get 就行了，遵循 post 的规范。


那这一个给它起名叫什么呢？它查询的是商品的属性，那就给它叫 item param 好嘞这一个根据商品 ID 查询商品的评价等级数量，给它起名叫 count commentsok 那再下面是根据商品 ID 查询商品的评价，那我们这里给它起名叫 paged comments 好，再往下到了搜索商品列表，这两个服务，咱前面提到了划归到哪里了，food search 搜索域里面，所以这里就把它直接注释掉就可以了。咱在商品域当中，不需要它。Ok.那这一个服务是根据 ID 搜索购物车中的商品数据。这个就是老师前面说的懒得动手往购物车模块拆分的那条服务。所以咱给它起名叫什么呢？ get cut my spec ID 给它起长一点。


好嘞，那接着往下这个 query item spec by ID 我们给它起名叫 item spec 大家起名时候注意一下，不要跟前面有重复。你看像这里 get mapping 咱起了一个叫 item spec 那下面也叫 item spec 那这两个就重复了。


所以咱们把下面这一个给它稍微改一下，可以去改成 single item spect 或者怎么样呢？或者把上面这个 item spec 的后面改成 list 两种方式都行。但如果你不想加 list 后面加个 S 都是可以的，只要保证它这个名称不重复就行了。


OK 那最后两个请求一个是获取商品的主图的，那我们给它起名就叫 primary image 好了，最后一个是减少库存的，咱终于可以用一个 post 了。 post 什么呢？就叫它 decorate stock 我们把中间这个 item spec 给它删除掉。


好，那咱定义完所有的路径之后，我们还要再回过头来定义什么呢？定义每一个 request parameter 它的属性名称。同学们如果不定义的话，它默认使用这个字段的名称来作为你的参数。但是如果同学们使用 sprint cloud fin 进行调用的话，并且这里入参没有给它指定 request param 的属性名，那它这里其实会报错的。所以说我们这里为每一个入参指定一个好听优雅美丽的名字。这一个 item ID 我们给它起名就叫做 item ID 那下面一个依然是 item ID 在下依然这个也是怎么全是 how old are you 怎么总是你？这里就不是它了。


我们看 item ID 是第一个参数，第二个参数我们给它起名就叫做 level 这个 level 它是不是一个必须的字段，它并不是一个必须字段。所以我们把这个 required 设置成 false 同样的分页信息也不是一个必须的字段。那我们也把 required 设置成 false 还有吗？这里还漏了一个 pitch size 每页的个数 H sizeok 它 required 也设置成 false 好，那我们接下来往后，这两个注释掉的接口不看好，这里把它的名称改成 spect ID 然后后面把这个 S 去掉，保持命名规范，再往下是 item ID 好嘞，再往下最后一个，这两个属性都是必填的参数，我们 required 的就不指定了，默认就是 required 好，OK那这一个 service 咱就已经定义完成了。


刚才同学们听到老师说这一个 service 定义完成，那还有第二个吗？当然有了，咱前面提到过，用户评论模块是不是被划分到商品域里面了？所以老师在这里偷偷摸摸的创建了一个接口，这个接口的名称叫做 item comments service 那接下来我们来到这个服务里面，把商品的评论服务给它，把接口添加上去。首先这里添加 request mapping 给它指定一个路径，把它叫做 item 杠 comments 再杠，然后后面跟 API 那这个服务里面其实只要添加两个接口就可以了。


其中一个接口，我们到福迪 DEV 当中把它 copy 过来，我们切换到福迪 DEV 找到哪个服务呢？找到这个服务 my comments serviceokay 大家看，这个 my comments service 里面有 123 有这三个接口，其中 query pending comments 那它是根据订单 ID 来查询你当前订单当中的关联商品，对不对啊？那所以这个接口我们会下放到订单领域的微服务当中来实现。那么另外一个服务，同样的它也是跟订单强绑定的。所以说以上两个服务全部下放到订单域。


最后一个服务，我的评论查询，那它是单纯的查询 item 也就是商品的评论的。那这里我们把它 copy 过来，只要 copy 这最后一个服务。 OK 我们引入 page result 然后把它的路径给它指定。好，它是一个查询服务，所以我们这里就是直接使用一个 get 路径就可以了。那 get 的路径名称我们给它打上叫 my comments 然后再为每一个属性指定什么呢？指定它的 request param 这第一个是 user ID 接下来每一个属性都是同样的方式，把它指定上 page 和 page size 这两个属性它不是一个 required 所以咱这里别忘了给它加上 required 等于 false 第二个属性也同样的是 required 等于 false 那名称记得要改。对，我这里把配置给它漏掉了，添加上去。


好，那接下来我们再添加一个第二个服务，这个服务我们就不从其他地方 copy 了，因为它是一个新的服务，我们把它叫做 save comments 那 save 什么 comments 第一个参数我们把它定义为一个 map 类型，这个 map 类型的入参是一个 string 它的 value 我们把它定义成 object 好它的名称就叫做 map 那这个方法我们给它指定是一个 post mapping 它的名称也叫 save comments 至于这个入参，那这里要用什么？要用 request body 给它修饰一下。


好嘞，那这个服务会被谁调用呢？会被订单中心调用，同学们看一下订单中心的源代码就知道了。 OK 那写到这里，整个 item API 也就写好了。那接下来我们创建 API 之上的一层是哪一层呢？ item service 好，我们这里选择梅文项目，然后这个梅文项目的名称叫做福迪杠 item 再一个杠后面跟 service 好，复制一下 next module name 这里 copy 过来，然后把它塞到文件夹里，塞到 domain 上。 item 这个文件夹点击分类是 321 出来泡母念当中添加两个依赖，哪两个依赖呢？这两个依赖都是自己人。


第一个 dependency 它的 group ID 我们把它添加过来是 project group ID 然后 artifact 是咱前面刚刚创建好的 body item API version ，这里依然是用变量名给它替换过来。 OK 那第二个 dependency 是 mapper 我们只用复制一下，然后把 for the item 杠 API 改成杠 mapper 好勒，这就齐活了。那接下来我们在 service 里面去做代码移植。在移动代码之前，我们先给它创建 com.imock 慕课网的大域名，后面再跟 item 咱的当前商品域的名称后面跟 [service.im](http://service.im/) PL implementation 所以它这是 service 的实现层。


点击。 OK 那这里我们要把商品域的服务给它从 food DEV 当中移植过来，我们切换到 foodie DEV 找到 item service 的实现类 item service implementation 把这个类直接拷贝过来走。你放眼望去，万里江山一片红，全是红字，怎么办呢？挨个改吗？咱这里要把包的路径首先给它更正过来。接下来这些 import 当中，很多类实际上只是缺少了一个 item 的路径前缀。那咱把这个 item 给它添加上去，重新引入进来就可以了。好 321 变好勒。


那看到这里的飘红的字是不是少了很多我们往下看，这里还有几道红色是什么呢？这个 search item 那它已经移到了主搜领域，所以我们这里只用把它给注释掉就可以了，删掉，眼前落得个清净。那这里还有一个很关键的改动，同学们，这里不要忘了，我们走上来。看到这里吗？咱把它声明成了谁声明成了 service 那咱说过 eureka 是基于什么 HD DP 的一个服务治理框架。所以我们的 service 提供的服务需要声明成什么呢？声明成一个 controller rest controller OK 在这里千万不要忘了，把 

service 这个注解也给它删掉，不然的话你这里启动的话会报出错误的。我们这个 service 注解不要。同学们。 OK 那其实这里我们还可以引入一个注解， sl four G 是轮播课的注解。那这样的话同学们在代码中可以很方便的打一些 log 通过龙博客的注解，[在这里直接使用log.info](http://xn--log-hb0e636ac0sw61ac9c0v1fuce.info/) ，都很方便的可以打。 OK 那我这里就不进行 log 方面的改造了，咱这一个服务已经改造好了，接下来我们改造另一个。


