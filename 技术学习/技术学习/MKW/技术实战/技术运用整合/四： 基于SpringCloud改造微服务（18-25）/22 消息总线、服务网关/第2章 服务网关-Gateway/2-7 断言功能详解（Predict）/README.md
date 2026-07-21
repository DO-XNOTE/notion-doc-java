---
title: 2-7  断言功能详解（Predict）
---

# 2-7  断言功能详解（Predict）

[image](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/bf92cab3-4460-481e-ad8c-53b0c9c526e3/SCR-20240721-eikl.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZJA33376%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T225735Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCI4SPV4CVcg8QphpNICuEN6DHrUdU7Bw7IUaZ8J1POqQIhANACh7Q2O1sdBoYK54u%2FQUU4W16LFUUYiJdlvE92yQUMKogECMb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgziVZxyIWuxQhd5tdEq3APSrv9L54%2BBb9AMFlj%2FRDh%2B%2BSxOhvSm84YrJxp6aMooGHAoZOJJ2uoYuwtVac71ONFRsHJOvxkFTvjiDNsotEB3g3iz7GaE77tpsWPMqGd7lz7Yp6vwfm%2B5NvFITjvrEF3rlqSZbSdvRRF6oZe8NDpSbHzWgtVMkRb6Bikwtbz93qNRm9qV%2FhkA8AKT3UWR4lhAWS5K68ePBZn4BHiEjhVCe%2BlsTguzxMLWei9UjEdRgsnUSJleIUftt9T5aN%2BGU8AIyGHwdkzDYO5wJftcsibRgQnSnCob61w%2BfvDq0D4RemgPqc6nIgg2EitJSoHVoCNtFe8%2BwefwyiL6DvQe%2Bj%2BMQsA%2BCVlgpSTb05YI0ewWvZph8ZvzmwN4EQAG%2BdJUCZ6kbizApQhDCHfV8pZUrPeqaANxYs0O%2F7uGLyCUneid3TlHjigf3Ujc4FgKKaWYHwC1a9Y6q02UUnOfXpx7BfvarDvPqS83vL1cYDWhHs3Cuvu8wXGLboEwT4NKWOKh2c63ipMhpsS48okc1%2BHMtsS3sVY%2B3B2uSW85qxI%2FAdodvPI4I7tquY%2FF6MG3JNdyLiNDftUMxnJxSI1u2SeSlDO4FInK5XnxTg8jETB2eE0mLViY%2FX9UUjOsRSS8CjCFt%2F%2FSBjqkAT7HhCckuNVtIipYAY9UYVEqySF0G%2FUtaRCzYl3CDculGI4ebqi4vocCp9hIKChrzYgIZ%2Ba6PrXsvMQ82FSuoETCrTmEJiAuLH0otk4bpBYS2yXP1ubtSf%2FldbCTkBhXdUovWPyFCbqDTOj9nk7GC2ylKiwLT5rUr6HxkA4WIG%2BU1KpRYSDjgmuKuUQByL3fsDh%2FJh7lhEfQknn5mFKpwDw617Oa&X-Amz-Signature=07212e3b68686f7041d783047459f8bce5e621ba3f9b9062dabf22c838c31cff&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

[image](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/50e9e98e-25d8-4bf6-987d-274fdb8efec4/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZJA33376%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T225735Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCI4SPV4CVcg8QphpNICuEN6DHrUdU7Bw7IUaZ8J1POqQIhANACh7Q2O1sdBoYK54u%2FQUU4W16LFUUYiJdlvE92yQUMKogECMb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgziVZxyIWuxQhd5tdEq3APSrv9L54%2BBb9AMFlj%2FRDh%2B%2BSxOhvSm84YrJxp6aMooGHAoZOJJ2uoYuwtVac71ONFRsHJOvxkFTvjiDNsotEB3g3iz7GaE77tpsWPMqGd7lz7Yp6vwfm%2B5NvFITjvrEF3rlqSZbSdvRRF6oZe8NDpSbHzWgtVMkRb6Bikwtbz93qNRm9qV%2FhkA8AKT3UWR4lhAWS5K68ePBZn4BHiEjhVCe%2BlsTguzxMLWei9UjEdRgsnUSJleIUftt9T5aN%2BGU8AIyGHwdkzDYO5wJftcsibRgQnSnCob61w%2BfvDq0D4RemgPqc6nIgg2EitJSoHVoCNtFe8%2BwefwyiL6DvQe%2Bj%2BMQsA%2BCVlgpSTb05YI0ewWvZph8ZvzmwN4EQAG%2BdJUCZ6kbizApQhDCHfV8pZUrPeqaANxYs0O%2F7uGLyCUneid3TlHjigf3Ujc4FgKKaWYHwC1a9Y6q02UUnOfXpx7BfvarDvPqS83vL1cYDWhHs3Cuvu8wXGLboEwT4NKWOKh2c63ipMhpsS48okc1%2BHMtsS3sVY%2B3B2uSW85qxI%2FAdodvPI4I7tquY%2FF6MG3JNdyLiNDftUMxnJxSI1u2SeSlDO4FInK5XnxTg8jETB2eE0mLViY%2FX9UUjOsRSS8CjCFt%2F%2FSBjqkAT7HhCckuNVtIipYAY9UYVEqySF0G%2FUtaRCzYl3CDculGI4ebqi4vocCp9hIKChrzYgIZ%2Ba6PrXsvMQ82FSuoETCrTmEJiAuLH0otk4bpBYS2yXP1ubtSf%2FldbCTkBhXdUovWPyFCbqDTOj9nk7GC2ylKiwLT5rUr6HxkA4WIG%2BU1KpRYSDjgmuKuUQByL3fsDh%2FJh7lhEfQknn5mFKpwDw617Oa&X-Amz-Signature=8552c3814c36f9610938bee8004400b13a783ed7ada8f950f507b51e22b7d08e&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

**2-7 断言功能详解（Predict）**

前面我们了解了Route的功能，这一节我们来看一下Gateway最重要的一个核心功能-断言，这个功能决定了一个HTTP请求应该由哪个Route来做路由。

**Predicate机制**

Predicate是Java 8中引入的一个新功能，就和我们平时在项目中写单元测试时用到的Assertion差不多，Predicate接收一个判断条件，返回一个ture或false的布尔值结果，告知调用方判断结果。你也可以通过and（与），or（或）和negative（非）三个操作符将多个Predicate串联在一块共同判断。前面说到Gateway是挡在微服务前面的传达室大爷，那这个Predicate就是和大爷的接头暗号。比如大爷可以要求你的Request中必须带有某个指定的参数叫name，对应的值必须是一个指定的人名“马冬梅”，如果你的Request中没有包含name，或者对应的人名给成了“马北梅”，那就是断言失败。只有当你的请求完全和接头暗号匹配的时候，大爷才能给你放行。

[image](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/675899ce-92fc-441b-a210-4c3f3b05c68a/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZJA33376%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T225735Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCI4SPV4CVcg8QphpNICuEN6DHrUdU7Bw7IUaZ8J1POqQIhANACh7Q2O1sdBoYK54u%2FQUU4W16LFUUYiJdlvE92yQUMKogECMb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgziVZxyIWuxQhd5tdEq3APSrv9L54%2BBb9AMFlj%2FRDh%2B%2BSxOhvSm84YrJxp6aMooGHAoZOJJ2uoYuwtVac71ONFRsHJOvxkFTvjiDNsotEB3g3iz7GaE77tpsWPMqGd7lz7Yp6vwfm%2B5NvFITjvrEF3rlqSZbSdvRRF6oZe8NDpSbHzWgtVMkRb6Bikwtbz93qNRm9qV%2FhkA8AKT3UWR4lhAWS5K68ePBZn4BHiEjhVCe%2BlsTguzxMLWei9UjEdRgsnUSJleIUftt9T5aN%2BGU8AIyGHwdkzDYO5wJftcsibRgQnSnCob61w%2BfvDq0D4RemgPqc6nIgg2EitJSoHVoCNtFe8%2BwefwyiL6DvQe%2Bj%2BMQsA%2BCVlgpSTb05YI0ewWvZph8ZvzmwN4EQAG%2BdJUCZ6kbizApQhDCHfV8pZUrPeqaANxYs0O%2F7uGLyCUneid3TlHjigf3Ujc4FgKKaWYHwC1a9Y6q02UUnOfXpx7BfvarDvPqS83vL1cYDWhHs3Cuvu8wXGLboEwT4NKWOKh2c63ipMhpsS48okc1%2BHMtsS3sVY%2B3B2uSW85qxI%2FAdodvPI4I7tquY%2FF6MG3JNdyLiNDftUMxnJxSI1u2SeSlDO4FInK5XnxTg8jETB2eE0mLViY%2FX9UUjOsRSS8CjCFt%2F%2FSBjqkAT7HhCckuNVtIipYAY9UYVEqySF0G%2FUtaRCzYl3CDculGI4ebqi4vocCp9hIKChrzYgIZ%2Ba6PrXsvMQ82FSuoETCrTmEJiAuLH0otk4bpBYS2yXP1ubtSf%2FldbCTkBhXdUovWPyFCbqDTOj9nk7GC2ylKiwLT5rUr6HxkA4WIG%2BU1KpRYSDjgmuKuUQByL3fsDh%2FJh7lhEfQknn5mFKpwDw617Oa&X-Amz-Signature=eadbabac50147f1ba762dfb543acc72535e489cf5364215a5d4fed2e2bb236e7&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

图片来源自电影《夏洛特烦恼》，原作者享有版权

说白了Predicate就是一种路由规则，通过Gateway中丰富的内置断言的组合，我们就能让一个请求找到对应的Route来处理。

**断言的作用阶段**

一个请求在抵达网关层后，首先就要进行断言匹配，在满足所有断言之后才会进入Filter阶段。有关Filter的内容将在接下来的小节内详细介绍。

**常用断言介绍**

Gateway提供了十多种内置断言，我们选几种常用的断言规则跟大家介绍下

**路径匹配**

Path断言是最常用的一个断言请求，几乎所有路由都要使用到它，我们来看一下它的例子

```java
.route(r -> r.path("/gateway/**")

.uri("lb://FEIGN-SERVICE-PROVIDER/")

)

.route(r -> r.path("/baidu")

.uri("http://baidu.com:80/")

)
```

Path断言的使用非常简单，就像我们在Controller中配置@RequestPath的方式一样，在Path断言中填上一段URL匹配规则，当实际请求的URL和断言中的规则相匹配的时候，就下发到该路由中URI指定的地址，这个地址可以是一个具体的HTTP地址，也可以是Eureka中注册的服务名称。在上面的例子中，如果我们访问“/gateway/test”，这个路径将匹配到第一个路由。

**Method断言**

这个断言是专门验证HTTP Method的，在下面的例子中，我们把Method断言和Path断言通过一个and连接符合并起来，共同作用于路由判断，当我们访问“/gateway/sample”并且HTTP Method是GET的时候，将适配下面的路由

```java
.route(r -> r.path("/gateway/**")

.and().method(HttpMethod.GET)

.uri("lb://FEIGN-SERVICE-PROVIDER/")

)
```

**RequestParam匹配**

请求断言也是在业务中经常使用的，它会从ServerHttpRequest中的Parameters列表中查询指定的属性，有如下两种不同的使用方式

```java
.route(r -> r.path("/gateway/**")

.and().method(HttpMethod.GET)

.and().query("name", "test")

.and().query("age")

.uri("lb://FEIGN-SERVICE-PROVIDER/")

)
```

属性名验证 如 query("age")，此时断言只会验证QueryPrameters列表中是否包含了一个叫age的属性，并不会验证它的值属性值验证 如query("name", "test")，它不仅会验证name属性是否存在，还会验证它的值是不是和断言相匹配，比如当前的断言会验证请求参数中的name属性值是不是test，第二个参数实际上是一个用作模式匹配的正则表达式

**Header断言**

这个断言会检查Header中是否包含了响应的属性，通常可以用来验证请求是否携带了访问令牌，比如如下设置：

```java
.route(r -> r.path("/gateway/**")

.and().header("Authorization")

.uri("lb://FEIGN-SERVICE-PROVIDER/")

)
```

上面的断言指定了Header中必须包含一个Authorization属性，Header断言和Query断言一样，也可以通过传入两个参数的形式对属性值进行检查

**Cookie断言**

顾名思义，Cookie验证的是Cookie中保存的信息，Cookie断言和上面介绍的两种断言使用方式大同小异，唯一的不同是它必须连同属性值一同验证，不能单独只验证属性是否存在，示例如下：

```java
.route(r -> r.path("/gateway/**")

.and().cookie("name", "test")

.uri("lb://FEIGN-SERVICE-PROVIDER/")

)
```

**时间片匹配**

时间匹配有三种模式，分别是Before、After和Between，这些断言指定了在什么时间范围内路由才会生效

```java
.route(r -> r.path("/gateway/**")

.and().before(ZonedDateTime.now().plusMinutes(1))

.uri("lb://FEIGN-SERVICE-PROVIDER/")

)
```

以Before断言为例，它接受的是一个ZonedDateTime参数，用来表示生效的时间。比如上面的例子中我们使用了 ZonedDateTime.now().plusMinutes(1)

表示当前时间的后一分钟，由于路由的规则是在项目启动时加载的，那么这里的当前时间也就是项目加载完成的时间，因此该路由的有效时间就是服务启动后的一分钟以内。

**自定义断言**

Gateway也提供了一个扩展方法，用来将自定义的断言应用到路由上。老师给出两点提示，希望同学们顺着这个方向来参考Gateway的源码，实现一个自定义断言，完成一个小功能：将所有请求参数大于5个的访问请求拦截掉，即RequestParam个数小于5个的请求才能被放行。

提示1 所有断言类都可以继承自AbstractRoutePredicateFactory

提示2 在路由配置时可以通过predicate或者asyncPredicate传入一个自定义断言

**小结**

这一节我们学习了Gateway最重要的功能“断言”，并且了解了几种常用断言的用法，下面我们就去做两个demo，创建自己的路由规则。希望同学们以练代学，看完demo以后，顺着上面给出的自定义断言的提示，完成这个小练习。

[image](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/1bf31aa9-356c-46b9-833d-698a66d28ed4/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZJA33376%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T225735Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCI4SPV4CVcg8QphpNICuEN6DHrUdU7Bw7IUaZ8J1POqQIhANACh7Q2O1sdBoYK54u%2FQUU4W16LFUUYiJdlvE92yQUMKogECMb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgziVZxyIWuxQhd5tdEq3APSrv9L54%2BBb9AMFlj%2FRDh%2B%2BSxOhvSm84YrJxp6aMooGHAoZOJJ2uoYuwtVac71ONFRsHJOvxkFTvjiDNsotEB3g3iz7GaE77tpsWPMqGd7lz7Yp6vwfm%2B5NvFITjvrEF3rlqSZbSdvRRF6oZe8NDpSbHzWgtVMkRb6Bikwtbz93qNRm9qV%2FhkA8AKT3UWR4lhAWS5K68ePBZn4BHiEjhVCe%2BlsTguzxMLWei9UjEdRgsnUSJleIUftt9T5aN%2BGU8AIyGHwdkzDYO5wJftcsibRgQnSnCob61w%2BfvDq0D4RemgPqc6nIgg2EitJSoHVoCNtFe8%2BwefwyiL6DvQe%2Bj%2BMQsA%2BCVlgpSTb05YI0ewWvZph8ZvzmwN4EQAG%2BdJUCZ6kbizApQhDCHfV8pZUrPeqaANxYs0O%2F7uGLyCUneid3TlHjigf3Ujc4FgKKaWYHwC1a9Y6q02UUnOfXpx7BfvarDvPqS83vL1cYDWhHs3Cuvu8wXGLboEwT4NKWOKh2c63ipMhpsS48okc1%2BHMtsS3sVY%2B3B2uSW85qxI%2FAdodvPI4I7tquY%2FF6MG3JNdyLiNDftUMxnJxSI1u2SeSlDO4FInK5XnxTg8jETB2eE0mLViY%2FX9UUjOsRSS8CjCFt%2F%2FSBjqkAT7HhCckuNVtIipYAY9UYVEqySF0G%2FUtaRCzYl3CDculGI4ebqi4vocCp9hIKChrzYgIZ%2Ba6PrXsvMQ82FSuoETCrTmEJiAuLH0otk4bpBYS2yXP1ubtSf%2FldbCTkBhXdUovWPyFCbqDTOj9nk7GC2ylKiwLT5rUr6HxkA4WIG%2BU1KpRYSDjgmuKuUQByL3fsDh%2FJh7lhEfQknn5mFKpwDw617Oa&X-Amz-Signature=dc29922facd704fc00b8b8c0160039c37813d287f48314cb1d2594ea9b67e4e4&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



