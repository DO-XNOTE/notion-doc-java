---
title: 2-14 Spring MVC源码解析-1（1521）
---

# 2-14 Spring MVC源码解析-1（1521）

[image](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/7f4286d4-c4c6-4fca-a8ef-4085cdb834b8/SCR-20240803-nsrz.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666ONIUXSW%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T232014Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQD5zoSC%2FgM%2FniCjnxEFPbKp2WJni39nwvyOPMZJmsZO6wIgYMAqOereJOPzFKXFaG3AJL0cK3mHhIcDxfhjfR3HmNIqiAQIxv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDMnqjrN9fA2PD6%2FzJyrcA9RtFuyMV%2Fszc6t%2B7pUBzBGPnNSZTgVj87Lvs2sPBY0sW8YQCOKVMYPlwePNt7xxiP58e7dwB9V1fPYHh%2B5xtXNcWgoSeMfkfk4Dbot2A8L5bXPrAVFzVWt7IEz78oreRaQJj0RYym%2B2cNAfTjN9EUez4g1KiV5jX%2B9nnqdpkt9F57MdF1vCjAaSnNee9tRUthwa4zj6XstqCd06Y8rS%2Bj%2FlbL4Z3RVuk1Yc6%2BBnUV5dNKkNGXY1Bo9LAccj4Yw0jHvzHrcGaw449IrKxI3wWBT74PDRH%2BM1yPoNO5i1d3sLtNtZEZQpOpcDH1FIznllKx09g899%2FsR1ZTz09ZoxkVDhc8C%2FO57LmY4EtvRUVR4zN1Nege813etsIOqEvZDwjFz1ywQUKggnR%2Bqgv559kV%2BANl9ScI8%2Fv6JIYx3BjusyOyrEF9EIb%2B5kffvnpoI%2B8FbqC7567983u4d0u7YACa8WHpShgJLAvCPX%2FjSYaFSLjJ2y6pvKFKL9%2B0XnZDadHGUsBQqw14ese5GSc6%2FbscHsV8e460ZOdiXoSW4nRshQ6lWFp4e%2FyqCwnYGCoLVegchMeVJWagh6ExIKwo%2BtGDG64U6QZenagGPxOcudZO0x1jK5n%2BFtsfIopsngMPC4%2F9IGOqUBW8u%2F8UjTRb%2BHmRhoWcxclQAc96Ov15Jt%2Fync7mu%2B9Fg0%2B0itc%2FHoKBXdFh6yVPuqMo7Y%2FC9F9T29CGfrjcsTGgXwbGptyQvk5zPvv7RsAIcHy0bRVY5hAzX8ORUVsNYOu03EqYpDzazV3WfqoDpb%2FLcYlg0ly1FS3%2BpL87RbtZxizUDi1Z9Oasaa0R3sq4MyD%2BGUP9Sfi1AbZKz1ugcQrIG1GIB%2F&X-Amz-Signature=7fc9d51e797fe11a5161089e8aa49304389a3e15427c17458060447a8a721a92&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

同学们大家好，这章节我们来学习 spring MA seed 源码解析。大家知道 spring m a C 是加 Web 开发的标配，在面试过程中 MA seed 执行流程也是必考题。学习好词表 Mac 底层源码及它的设计原理，对我们进行系统设计有很好的参考价值。我们通过三方面来学习 cm h 的源码内容，首先我们来学习 SMS 的核心注解，第二我们来学习 MA seed 核心API。


最后我们来介绍 SMM seed 执行流程。好，我们首先来看一下 CMA seed 注解。我们在做 m a C 开发的过程，给大家印象最深刻的就是 spring 提供的跟 m a C 相关的注解，大家用的最多的应该就是 request Mapping 和像 RESET Controller 这样的注解，在这里面我们区分了几类。首先我们开启 spring MC 这个功能，我们需要使用到 enable Web Mac 这样一个注解，那么在使用过程中我们需要对应的 control 去做一些标注，那么我们会用到 RESET control 或普通的 control 来标明一下。整个这个类是为了跟 spram AC 提供我们的消息入口。那么对于一个返回值内容，我们会用到 response body 这样一个注解，表明一下它返回的内容会基于我们 JSON 序列化的方式去解析渲染。


相比上面的 reset control，下面这个 control device 大家可能用的比较少。其实 Ctrl advice 它提供的功能是非常强大的，它可以基于在通过 Ctrl advise 修饰的类下面去定义我们的 exception handler 和引起的banner。他能做的事情就是定义一个全局的可以供所有 Ctrl 使用的异常处理器，或者是一个数据绑定。


接下来就是 request Mapping，对于 request Mapping 的话，这个就不用过多的介绍，像它是我们使用最多的，因为我们所有的方法 URL 都需要通过 request Mapping 去做映射。但是 spring 在后来的版本提供了像 get Mapping， post Mapping， put Mapping 这样一个基于 restful 方法的一个 Mapping 的扩展，这样的话我们在使用的过程中会更简洁易懂的去看到我们这个 Mapping 对应的 mast 方法内容是什么。


好，我们接下来看后面的是 request parameter 相关的，像这里面定义的这些注解，一般都会用到 control 对应的方法里面对参数进行修辞。首先 request Pre meter 是使用最多的，我们对于我们 URL 或者说 request body 里面传的一些数据进行一个命名的修饰。同时我们还可以提供 request header，也就是说我们通过 HCB 请求 handle 里面的内容取出来，去进行我们参数的传递，同时还支持像 cookie 或者是我们的 model attribute，我们的 pass variable，也就是说我们的路径变量，我们对于 URL 符合某种规则的一些通配符，我们把这个对应的值域取出来。像我们 rush 的 API 里面经常会用到对于我们一个 user ID 或者一个操作的时候，我们可以把 ID 的内容通过 pass 里面取出来。


下面是这里面向我们的 session re attribute 和我们的 request tribute，也就是通过我们的请求或会话的属性信息里面取出一些对应的值。 request body 是我们在传输数据的过程中，通常通过 json 的方法把它放到 request body 里面，我们在这里面去反序列化解析出来去使用。


我们看一下在 spring 框架源码里面这些注解的位置，其实我们虽然讲解的是 spring Mac，但是我们应该注意一下，对于我们这些注解的内容，它其实是放在 spring Web 模块下面，其次它并没有在 spring Web IVC 模块儿，在这里面我们可以看到它是对应的我们的 spring Web。下面这里面的 annotation 这样模块儿，这里面定义了很多注解，在这里面我们可以重点关注几个注解，就是我们首先最重要的，也就是 request mapping 和我们的 request parameter。单纯去说这个注解的话，注解的内容相对是比较简洁的，也使用起来也比较简单。那么我们对于这些注解可以到它的源码里面去看一下这个注解的定义方式，以及这个注解它支持的一些配子参数。比如像这里面的 request mapping，我们可以看到它对应的这些参数，这里面支持的一些我们的注解类型。consumer，也就是说我们消费的 miss type 类型，以及我们的 head 斯的指定name，parameter，pass， produce 等等这些内容。


对于这些内容，就是我们跟这个 request mapping，也就是对应那个请求类型的定义了一些对它进行一些筛选的一些策略，比如说对于pass，也就是说满足这个路径的，我们可能会映射到对应的 request mapping。同时我们还可以支持一些其他的一些更多的一些限制，比如说我们要求它对应的方法，比如 request must，它是要求 get 方法还是 post 方法？同时我对于 parameter 里面和它的一些请求类型，像，比如说我们支持的一些 media type，比如说我这个请求只支持 json 类型的，或者我只能返回 json 类型的。如果说你请求的参数，它是想期望通过 x mirror pause 去返回的吗？这里面就是不支持的。那么对于我们这里面的 request Pre meter，对于 request p 的 meter 是更简单一些，我们可以在这里面指定一个name，去标明一下我们对于这个参数所关心的它参数的名称是什么。


下面像这里面孩子使用比较多的是有 response body，它并没有什么特殊的属性，但是它去用来标明一下，我对应这个返回值会直接通过 XT master 方式去序列化，通过 response body 去修饰的这些响应内容，它不会去构造 model 的 view 这样的对象，大家在深入源码里面去看它的实现的过程中也会关注一下它的设计细节。
那么为什么这些 MVC 相关的注解是放到了我们的 Web 模块，而并没有放到 MVC 模块？这里面有一个解释的原因就是我们可以看到在spring，它在 5. 0 提供的 Web Flex，它也是支持我们的一种异步的请求。对于 Web Flex，它对于这些 MVC 相关的注解，它也是完全支持的。


所以说对于我们这个程序，我们可以看到在我们的 Web MVC，它依赖了AOP， being context 和 spring Web，对于我们的 Web flags，它也是依赖了 being core 和Web。那么所以说对于我们在 spring Web 里面它定义的这些注解，它同时可以为 spring 提供服务，也可以同时为 Web Flex 提供服务。这样的话，我们看到对于 Web m a C 和 Web Flex 作为一个并列的两个加 Web 模块，它同时可以依赖 spring Web 里面提供的这些功能和特性。我们回到PPT，那么接下来我们来给大家介绍一下 SPAM AC 的核心API。


对于 SPRAM AC 来说最重要的也就是 despite Server Lite，那么对于 discussion 失败的相关的 API 是非常多的，我们可以一块集中性的去看一下，另一方面就看对于 dispatch 失败的进行我们的 control 对应方法的处理过程，也就是包装为一个 surlight invocable handler method，它在处理的过程中，包括对于参数接收和我们的返回值的一些处理的过程都是非常重要的。


好，我们先来看一下 departure survive 相关的API，在这里面有一些概念大家应该比较清楚，也借认识过一些，像 handler Mapping 和 handle Adapter，这是使用比较多的，同时像还有 handle intercept，也就是我们 spell MVC 拦截器，这也是大家应用可能会比较多一些的。


下面这里面有 handler acceptance resolver，也就是对我们异常的一个统一的解析器，后面还有 model 的view，对于 model 的view，我们早期做一些视图操作的话，大家用的比较多，现在我们的操作大多是前后端分离，我们后端只会返回 JSON 数据，所以说现在对 model 的 view 的概念可能就不是那么强烈了。


下面这些内容，像 wheel resolver 和这些比如说我们的皮肤相关的 local resolver，因为我们在返回 json 阶段的这些东西是用的相对比较少了，就是不作为我们的重点，我们来去看哪些像这里面的 handler Mapping 对应它的一个实现就是 request Mapping， handler Mapping，这是我们基于注解的方式去进行 m a C 开发，使用最多的一个 handler Mapping。同时 handler Adapter 也就是跟我们这里面对应的是 request Mapping，我们看一下它们前缀是一样的， request Mapping， handler Mapping， request Mapping， handle Adapter，也就是说都是以 request Mapping 注前缀跟我们这个接口的一个拼装。同时在 handle Adapter 和 handler Mapping 它也有沼气在支持注解之前提供的一些支持，比如说这里面是 b name URL Handler Mapping，也就是我可以根据在容器里面 BN 的名称进行我们的映射。同时对于 handle Adapter 它也提供了一些方法，比如说 i t p request handle Adapter，其实这个过程也就是简单的把我们原来 serverless 的 a p i 转化成了一个 handle adapter API，其实这样的实现的意义其实对于现在来说其实并不是很大。


现在你一个比较重要的项目，我们这个 handle Adapter 对应的是 handle FAX Adapter 这种基于函数式编程的方式，我们这里面这个是比较重要的。好，我们看在对于 handling example 的，它作为一个拦截器的话，拦截器其实在使不用 dispators 处理的过程中，它是把我们的 handler intercept 和 handle adapt 共同包装成一个 handler exclusive chain each 一个执行链。在这个执行链执行的过程中，首先执行拦截器的 Pre 操作，同时执行 handler 对应的 handler 操作，然后去执行我们拦截器的一些后处理相关的操作。好，这是我们对于 departure letter 里面这些常用的 API 的一些简单的一个过程介绍。


那么大家有没有想过我们在使用最广泛的 request Mapping handle Adapter，它在真正的去执行我们 control 对应的这个方法的过程中，肯定它是用到了反射，那么具体反射的执行是怎么做的？我们接下来看这一件，对于这里面它都会去包装成一个 handler mess 的，也就是说把我们 control 里面对应的执行方法包装成一个 handler messed，去统一的用反次的胖子 be 执行。


对于 handler method，它并不是接口，它是一个实现类，对于这个实现类，它底下有它对应的子类，它的子类我们用的直接用使用的就是 surlight in vocabelle handler messed。对于这个，也就是它提供了我们相关的一些在参数的处理和我们返回值的处理的一些操作。


对于这个 Handler master，它在执行方法之前会通过 Handler master argument resolver，也就是我们的参数解析器解析一下我们请求里面所对应的参数和我们这个方法所支持的参数去进行匹配。这里面的解析器它提供了很多这里面最常用的，像 request parameter map mass accumate，也就是说我们对于一个参数 e 映射成一个map，或者说我们的 request head，也就是我们在基于注解的获取我们请求 head 信息的一些方式，都是通过对应的这个解析去解析。


如果我们在解析完成我们对应的参数跟我们的方法的参数匹配上以后，我们就可以去执行我们对应的方法了，那么执行这个过程就是我们对应的业务逻辑，我们自行完成以后会对应有相应的返回值，那么我们返回的内容还会通过这个 handler master return value handler，也就是说我们返回的这些值它会被这个 return value handler 所接收，我们对于这个返回值进行一些处理，这里面最重要的就比如说我们会去判断一下，如果当前这个方法被 response 的 response body，也就是 response body 这个注意修饰的话，那么它处理的逻辑就跟我们其他的方式就不一样了。如果说是它通过 response body 修饰的这个注解，它就会最终通过 XC message converse 的方式去进行我们的一些消息转换，同时渲染到我们的响应请求里面。在这里面我们使用最多的也就是 Mapping Jackson to HCP master convert，也就是说我们这个对象会把它映射成json，再转化到我们响应信息里面。同时对于 return value handler 也提供了很多实现，这里面像 model 的 view 的一些实现或等等其他的一些实现。好，这是我们能看到跟 string m a C 核心 API 相关的一些内容。


来看一下 spring 框架源码它的实现过程，在这里我们可以看到在 spring Web VC 这个模块下面，我们能看到 Dispatch THREAD，同时可以对应的这里面有 Handler Adapter， Handler Mapping 和 Handler incept。这里面最重要的我们的处理器和我们的映射器以及我们的拦截器都可以在这里面看到这些类，它是相对比较重要。在 spring Maca 的设计过程中，也就是在 Web Sert 这样的，我们可以理解一个 base 派case，也就是说它是相对来说比较基础重要的一个根结构。那么下面我们可以看到像 modern 的 view 还有view，这里面是 view resolver 与一些解析器也是相对比较重要的一些内容。我们可以看到在 disorder 舌歪的过程中，这个类的实现还是比较复杂的， 1000 多行对于 spin 来说是比较多的一个内容。


我们可以看一下这个 dispatch 10 来的它提供的一些方法。在这里面我们可以看到它提供了很多跟 init 相关的一些内容，也就是说它会通过 init 方式的方式去执行我们的操作。同时它还有一些跟 do 相关的，这里面 do dispartifly 的和 do service 这些就是真正在处理执行流程的过程用到的方法。


我们看一下 handler mess 的它，这里面我们要注意一下这个 handler mess 它其实是在 spring Web 工程下面，对于 handler mess 它是真正的去对于我们提供的这些内容进行包装。看这个类里面提供了像对应的 bin 和 bin factory 以及我们的 Mesh 的类型，这里面还包括我们对应这个 Mesh 的方法里面支持的这些参数，同时还有一些像这个方法它基于的一些注解有哪些等等这些描述信息。


好，对于这个 handler master，它的一个几个死线令我们可以看一下我们这里面使用比较多的，也就是 THREAD incredible，像这个对于我们可以看到它这里面提供相对于我们的父类，它多了几个，一个是我们的 handler Mesh 的 return value handler，一个是也就是处理我们返回词的一些内容，同时这个类它还继承。我们看这里面有一个said，我们这里面是对应的 Handler mass argument resolver，也就是对于参数处理的内容，它对应的类也就是 invoke Handler mess 的这样一个类。好，这是我们对于 SMIC 几个常见的 API 的一些内容。好，接下来我们来看一下 smart RV seed 执行流程。

