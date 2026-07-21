---
title: 2-8  【Demo】利用Path断言实现URL映射
---

# 2-8  【Demo】利用Path断言实现URL映射

[image](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/e936e4b1-9142-4c62-93a0-6612c6988a41/SCR-20240721-eohv.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466R2SPW3DQ%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T225735Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDfnbjkuSaQzdoIb0UvEYdD421pAQcs4coTbQc9J2ycgQIhAJ53fipRDCOctKYRdhOvTYtmjDt%2BXPiL%2F0FJJjisn6buKogECMb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1Igyu%2Bvl4sR8hQk8ETGIq3AOln0ADqx%2FHN44UFQbDihMEkAKjhkC%2F1m7NF%2BmPW3gosXqR4H%2BfqkoidCGWRBZ7ZfRtcZM8CZ73vftQhavojwRrYBmqgLBoJSMcV5G6ECbvObW1o1RryLWeIYnqJ0VwdB4TY0nTeyObkRVGH%2BZVqxxwywbtAef1y%2B5dTmuNwvHGeBTVnfNIYUsgUa9TId9FAJ4WMUfNBlRZXKdgf0VetoXVymBLB7cSqFdMKTFuGMSY5sZ1YbBaFV5%2F6jk2xNSNJ3OD6EUlyBs73r0Qr%2Bc9HyGO0oy4E4xPgHoyrtRE1vTbQcl5x%2FlnFp%2F2bRQnL8CV5kn8C0sqY%2FdIGkuvXfWaLWbL%2FbT3UzbhbkpVyEXkrpWgymYHkkOsCrVojON4MAYjofDanlFIbWbaTyv%2BV43nuT6l%2FIfxEhh9%2BpwnSQQwXtRAoI9e7WfEgFWbwwaVPQqMXX3IlCGGsKJXt0gBKacaF0rvf2wQ3RSM8YgZPG7Mg9AckKDY41VMVOmhQsRc4FTdnb7IhW%2FaTfCTYvjDSHK3QSd%2FD2VyzfYNtBmaOxMINs9SYiifIpJmUb56ZxLKJkTOgEECInhpfavLFqdJLdhQPRwlvFn3ryOHlrYaxDQKBKI3pOisP7hXLfXjBHtyCTCWt%2F%2FSBjqkAaFbdBFhzg8xJTxbErwKoa5rr3sGVdfK4TXQCY0xD0x5nPFF6HQII%2BKQ7g86KGVERxB7LCfxG9F51v6ShxjfZNo2dESkFYFwsWsDJ9ti5%2Fklz9Vqu%2F3BLcO9%2FGoBw0ayT5Xk2a1nvJLKfaTU4ZVp%2F3hgzls%2Fv34NCpcSM3wgmadc7Y9gvrNGI7%2Fx5%2FuFebNIZMLuV1U1TtybP2yc6gSOa9cjWmwa&X-Amz-Signature=b37c9f4af0548e91b59b363f03d66f480e54b3a546037c0c2b2dfd73f21f5291&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

[image](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/3e3adb81-f520-4e47-ba84-350641b13975/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466R2SPW3DQ%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T225735Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDfnbjkuSaQzdoIb0UvEYdD421pAQcs4coTbQc9J2ycgQIhAJ53fipRDCOctKYRdhOvTYtmjDt%2BXPiL%2F0FJJjisn6buKogECMb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1Igyu%2Bvl4sR8hQk8ETGIq3AOln0ADqx%2FHN44UFQbDihMEkAKjhkC%2F1m7NF%2BmPW3gosXqR4H%2BfqkoidCGWRBZ7ZfRtcZM8CZ73vftQhavojwRrYBmqgLBoJSMcV5G6ECbvObW1o1RryLWeIYnqJ0VwdB4TY0nTeyObkRVGH%2BZVqxxwywbtAef1y%2B5dTmuNwvHGeBTVnfNIYUsgUa9TId9FAJ4WMUfNBlRZXKdgf0VetoXVymBLB7cSqFdMKTFuGMSY5sZ1YbBaFV5%2F6jk2xNSNJ3OD6EUlyBs73r0Qr%2Bc9HyGO0oy4E4xPgHoyrtRE1vTbQcl5x%2FlnFp%2F2bRQnL8CV5kn8C0sqY%2FdIGkuvXfWaLWbL%2FbT3UzbhbkpVyEXkrpWgymYHkkOsCrVojON4MAYjofDanlFIbWbaTyv%2BV43nuT6l%2FIfxEhh9%2BpwnSQQwXtRAoI9e7WfEgFWbwwaVPQqMXX3IlCGGsKJXt0gBKacaF0rvf2wQ3RSM8YgZPG7Mg9AckKDY41VMVOmhQsRc4FTdnb7IhW%2FaTfCTYvjDSHK3QSd%2FD2VyzfYNtBmaOxMINs9SYiifIpJmUb56ZxLKJkTOgEECInhpfavLFqdJLdhQPRwlvFn3ryOHlrYaxDQKBKI3pOisP7hXLfXjBHtyCTCWt%2F%2FSBjqkAaFbdBFhzg8xJTxbErwKoa5rr3sGVdfK4TXQCY0xD0x5nPFF6HQII%2BKQ7g86KGVERxB7LCfxG9F51v6ShxjfZNo2dESkFYFwsWsDJ9ti5%2Fklz9Vqu%2F3BLcO9%2FGoBw0ayT5Xk2a1nvJLKfaTU4ZVp%2F3hgzls%2Fv34NCpcSM3wgmadc7Y9gvrNGI7%2Fx5%2FuFebNIZMLuV1U1TtybP2yc6gSOa9cjWmwa&X-Amz-Signature=88143de8fb2c6599092b3ab8f26a91571b7224ea1a11b9c722051c4cfef3636b&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

[image](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/b7cb7e93-1a66-46a6-8215-0a315c2b6ca5/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466R2SPW3DQ%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T225735Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDfnbjkuSaQzdoIb0UvEYdD421pAQcs4coTbQc9J2ycgQIhAJ53fipRDCOctKYRdhOvTYtmjDt%2BXPiL%2F0FJJjisn6buKogECMb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1Igyu%2Bvl4sR8hQk8ETGIq3AOln0ADqx%2FHN44UFQbDihMEkAKjhkC%2F1m7NF%2BmPW3gosXqR4H%2BfqkoidCGWRBZ7ZfRtcZM8CZ73vftQhavojwRrYBmqgLBoJSMcV5G6ECbvObW1o1RryLWeIYnqJ0VwdB4TY0nTeyObkRVGH%2BZVqxxwywbtAef1y%2B5dTmuNwvHGeBTVnfNIYUsgUa9TId9FAJ4WMUfNBlRZXKdgf0VetoXVymBLB7cSqFdMKTFuGMSY5sZ1YbBaFV5%2F6jk2xNSNJ3OD6EUlyBs73r0Qr%2Bc9HyGO0oy4E4xPgHoyrtRE1vTbQcl5x%2FlnFp%2F2bRQnL8CV5kn8C0sqY%2FdIGkuvXfWaLWbL%2FbT3UzbhbkpVyEXkrpWgymYHkkOsCrVojON4MAYjofDanlFIbWbaTyv%2BV43nuT6l%2FIfxEhh9%2BpwnSQQwXtRAoI9e7WfEgFWbwwaVPQqMXX3IlCGGsKJXt0gBKacaF0rvf2wQ3RSM8YgZPG7Mg9AckKDY41VMVOmhQsRc4FTdnb7IhW%2FaTfCTYvjDSHK3QSd%2FD2VyzfYNtBmaOxMINs9SYiifIpJmUb56ZxLKJkTOgEECInhpfavLFqdJLdhQPRwlvFn3ryOHlrYaxDQKBKI3pOisP7hXLfXjBHtyCTCWt%2F%2FSBjqkAaFbdBFhzg8xJTxbErwKoa5rr3sGVdfK4TXQCY0xD0x5nPFF6HQII%2BKQ7g86KGVERxB7LCfxG9F51v6ShxjfZNo2dESkFYFwsWsDJ9ti5%2Fklz9Vqu%2F3BLcO9%2FGoBw0ayT5Xk2a1nvJLKfaTU4ZVp%2F3hgzls%2Fv34NCpcSM3wgmadc7Y9gvrNGI7%2Fx5%2FuFebNIZMLuV1U1TtybP2yc6gSOa9cjWmwa&X-Amz-Signature=af6d11baefa47b9f5cd99b424607cf4405ab005801ad7406f91ca51256b6272b&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

hello 慕课网的各位同学们，大家好，这节咱来介绍整个 gateway 章节中一个比较重要的部分，它是负责路由规则的，也就是路径的断音。大家还记得咱在上一个 demo 环节里，使用艾特瑞特的接口动态的添加了一个路由规则。在这个路由规则里，大家肯定看到了路径的断言，但是不知道它具体是什么含义对吧？那么这一节里咱就把它一五一十的说明白。


这第一个部分就是使用 pass 断言来转发用户的请求。这里咱使出一招，双刀流咱不止在 YAML 里面可以配置路径断言，在 Java 代码里面也是可以配置的。那这个双刀流跟大家展示两种不同的流派。 OK 实际上 pass 断也只是一个非常非常简单的功能了，在整个 gateway 里面有很多很多种断言，那咱就买一送一。好了，再跟大家看一下这个 method 的断言是怎么来使用的，把 pass 断言和 method 断言合在一起，二合一搭配使用。当然了咱就像做电视广告一样，买一送一还不够，今天还要送厂家大酬宾。在这个小节里，咱还要跟大家连带着说一下如何配置一个简单的 filter 来结合 pass 断言进行用户请求的转发。哇。这个内容简直是优惠多多，诚意满满。

[image](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/9cf05b5f-1bda-46e1-955b-1ef6edc2b346/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466R2SPW3DQ%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T225735Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDfnbjkuSaQzdoIb0UvEYdD421pAQcs4coTbQc9J2ycgQIhAJ53fipRDCOctKYRdhOvTYtmjDt%2BXPiL%2F0FJJjisn6buKogECMb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1Igyu%2Bvl4sR8hQk8ETGIq3AOln0ADqx%2FHN44UFQbDihMEkAKjhkC%2F1m7NF%2BmPW3gosXqR4H%2BfqkoidCGWRBZ7ZfRtcZM8CZ73vftQhavojwRrYBmqgLBoJSMcV5G6ECbvObW1o1RryLWeIYnqJ0VwdB4TY0nTeyObkRVGH%2BZVqxxwywbtAef1y%2B5dTmuNwvHGeBTVnfNIYUsgUa9TId9FAJ4WMUfNBlRZXKdgf0VetoXVymBLB7cSqFdMKTFuGMSY5sZ1YbBaFV5%2F6jk2xNSNJ3OD6EUlyBs73r0Qr%2Bc9HyGO0oy4E4xPgHoyrtRE1vTbQcl5x%2FlnFp%2F2bRQnL8CV5kn8C0sqY%2FdIGkuvXfWaLWbL%2FbT3UzbhbkpVyEXkrpWgymYHkkOsCrVojON4MAYjofDanlFIbWbaTyv%2BV43nuT6l%2FIfxEhh9%2BpwnSQQwXtRAoI9e7WfEgFWbwwaVPQqMXX3IlCGGsKJXt0gBKacaF0rvf2wQ3RSM8YgZPG7Mg9AckKDY41VMVOmhQsRc4FTdnb7IhW%2FaTfCTYvjDSHK3QSd%2FD2VyzfYNtBmaOxMINs9SYiifIpJmUb56ZxLKJkTOgEECInhpfavLFqdJLdhQPRwlvFn3ryOHlrYaxDQKBKI3pOisP7hXLfXjBHtyCTCWt%2F%2FSBjqkAaFbdBFhzg8xJTxbErwKoa5rr3sGVdfK4TXQCY0xD0x5nPFF6HQII%2BKQ7g86KGVERxB7LCfxG9F51v6ShxjfZNo2dESkFYFwsWsDJ9ti5%2Fklz9Vqu%2F3BLcO9%2FGoBw0ayT5Xk2a1nvJLKfaTU4ZVp%2F3hgzls%2Fv34NCpcSM3wgmadc7Y9gvrNGI7%2Fx5%2FuFebNIZMLuV1U1TtybP2yc6gSOa9cjWmwa&X-Amz-Signature=999a3a5a61332e2d8f72aaeb3d6a3ea680d4bb54ee5b560cfc1aa8e554ebcc7b&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

那还不赶紧抄起家伙，咱到影泰 dj 里面开拔编程，使我快乐 996 是我的福报，又到了享受福报的时候。老师这段时间真的是天天享受福报，每天大清早 7 点起来开会跟老外开完回到公司再跟中国人开，开完一天回家，到了晚上再跟老外开，把这个福报享受着昏天暗地。所以同学们赶紧珍惜眼下还可以努力写代码的时光。


那回到主线上来，咱说了要配置路径断言对不对？其实 predicate 这个单词很多的地方也把它谓词，叫做什么路由谓词，我个人更喜欢把它叫做断言，我觉得把它叫为谓词，搞得很玄乎似的，还是断言比较接地气。那咱先来看一下如何在 YAML 文件中配置一个断言。好了，这里要先给它创建一个节点，这个节点要放在哪里呢？大家看好，它跟 discovery 是在同一级的，这个叠节点就叫 roots 这里是它的路由的集合，那每一个 roots 其中会包含一个或者是多个短页，也会包含一些过滤器。那在这里如此。首先咱要知道它的数据结构是一个数组或者叫一个 list 那在 YAML 格式中，一个 list 的元素应该以什么开头呢？同学们应该知道的吧，是以一个短横杠开头的。


好，那咱这里就开始定义路由集合中的第一个元素，首先给他一个 ID 这个 ID 就是当前路由的唯一标识，咱给它起名就叫宾 client 好了，那有好奇心的同学可能会问，如果我定义了两个不同的 element 它的 ID 都是叫芬克兰特，会出现什么情况？说实话我老师还没有试过，我没有那个闲工夫闹着玩了。不过有这种好奇心是非常鼓励的，好奇心可以造就科学家和诗人，哪位同学如果测试了，可以把结果告诉老师，看他会报什么。
错。这里 ID 设置好了以后，接下来咱要设置一个 URI URI 可是很重要的，大家还记得他是做什么的吗？他就是告诉你如果匹配上了所有的断言，那么这个用户请求将要转发到哪里？好，咱这里把它转发到 LB 后面跟的是大写 fin 然后一个横杠格兰特。好这两个部分定义好以后，咱就开始定义后面的主线了。这里紧接着跟一个 predict 就是咱的断言部分了。这里大家注意，它也是一个集合，就是说咱不仅可以配置路径的断音，也可以配置很多其他的断音。那我这里配置一个最简单的 pass 断音。


好，它是大写的 P 一个 pass 然后后面跟什么呢？这就是你要匹配的路径了，我这里给它匹配一个斜杠 YAML 因为它是在 YAML 中定义的，所以咱就给它匹配一个 YAML 好了，但是后面要跟一个通配符告诉gateway ，所有以 YAML 开头的访问请求都转发到我这里。


OK 那当前的断言只有他一个，那么也就是说只要你的用户请求满足了这一个条件，它就可以被转发到后面的 URI 了。那在实际项目中，咱可能不止一个 pass 断言，还会有什么 header perimeter 什么之类各种各样的断言。同学们如果想熟悉这些断言，有两个途径，一个最简单的途径可以看老师的图文教程，在那里面跟大家总结了一些比较常见而且常用的断言。那么还有一个途径，当然是最推荐的了，直接去阅读官方文档，或者在代码里面横冲直撞摸索一番就可以。


OK 那 predicate 定义好了以后，咱在这个场景下还要再多定义一个跟它搭配使用的叫 filter 后面也有 S 因为它也是一个数组。好 filter 做什么用呢？我们先来定义这样一个filter ，它叫 strip pre prefix OK prefix 大家知道是什么意思吗？像前沿前缀的。那 strip 就是只切断它的前缀也就是说如果你的请求是长这个样子的，

```java
spring:
  application:
    name: gateway-service
  cloud:
    gateway:
      discovery:
        locator:    # 定位注册早eureka上的服务开关
          enabled: true
          lower-case-service-id: true
     routes:
     - id: feignclient
       uri: lb://FEIGN-CLIENT
       predicates:
       - Path=/yml/**
       filters:
#      //localhost:9000/yml/sayHi
       - StripPrefix=1

server:
  port: 65000


eureka:
  client:
    service-url:
      defaultZone: http://peer1:20000/eureka/



management:
  security:
    enabled: false
  endpoints:
    web:
      exposure:
        include: "*"
  endpoint:
    health:
      show-details: always
```

我来跟大家打一下是 local host 然后后面跟个端口号，然后 LY ML YAML 后面跟 say hi 那经过这个 filter 以后他会做什么事？它会把你当前的访问路径中的第一个 prefix 也就是 YAML 给它这样删掉它的请求就会变成了这个样子。同时转发到的地址会被替换成这个 think client OK 那这就是 filter 起的作用了。


当然 filter 还不止这一个，远远不止这一个同样也有两种学习的方式，一个是老师的图文教程里面会给出一些另外一个，咱再待会使用 Java 配置路由规则的时候，也会跟大家看几个常见的 filter 那这里第一个基于 YAML 配置的场景就跟大家介绍到这里了。之所以我先跟大家介绍基于 YAML 的配置，是因为我个人比较喜欢基于 Java 的配置，我觉得 Java 的配置不光打起来得心应手，那看起来也很顺眼。那咱接下来就看一看，在 Java 中如果想配置这套同样的路由规则，应该怎么来做。


Java 中的配置本质上是一个 configuration， 那么我们先在代码里面创建一个新的类，就给它起名叫做 gateway configuration 好创建好。然后在这个类上面，咱要把它作为一个配置项把它加载。应该怎么样？给这个类的头上戴一顶绿帽子，它的名字叫 configuration 好勒。带完以后咱在这里初始化一个 bin 这个 bin 的名称叫做我们先来打这个方法。 bin 的名称叫 root locator 从这个名字就可以看到它是一个地址定位的功能。那么这个方法咱可以随便给它起名字，比如叫 customized routes okay 在这个接收参数里，我们要接收一个 root locator builder 那么它的名称我们给它声明为 builder 把小桌板收起来。 OK 大家会问这个 builder 从哪传进来。这个不用大家担心了，我们给这个类上面加一个并注解，那么它就会作为初始化的一部分，自然有一个在当前上下文中已经出示好的 builder 传给你。那咱在这里给这个 builder 加一个 order 也是一个注解，在这里就不给 order 指定具体的加载顺序，使用它默认的 lowerest persensance 就可以了。


OK 那咱这里开始写主题方法了，首先给他来一个锐腾。呦第一行就起锐腾了。没错，因为他这个有build ，是一个方法链编程的形式，咱不用在前面哼哧写一大堆的代码，直接 return 好就好了。 builder 这里给它调用 roots 方法，你调用了 roots 方法，这个 builder 模式就开始飞起了，咱们接下面就可以一个一个添加的 root 那每一个 root 都是外面 YAML 文件中配置的一个 element 同样的，你一个 root 后面还可以跟另一个 root 另一个后面还可以再跟 root 那咱这里就用最简单的只添加一个 root 就好了。

```java
package com.imooc.springcloud;

import org.springframework.cloud.gateway.route.RouteLocator;
import org.springframework.cloud.gateway.route.builder.RouteLocatorBuilder;
import org.springframework.context.annotation.Bean;
import org.springframework.context.annotation.Configuration;
import org.springframework.core.annotation.Order;
import org.springframework.http.HttpMethod;

/**
 * <h1></h1>
 */
@Configuration
public class GatewayConfiguration {

    @Bean
    @Order // 加载顺序
    public RouteLocator customiaedRoutes(RouteLocatorBuilder builder) {
        return builder.routes()
                .route(r -> r.path("/java/**")
                        .and().method(HttpMethod.GET)
                        .and().header("name")

                        .filters( f -> f.stripPrefix(1)
                                .addRequestHeader("java-param", "gateway-config")
//                                .
                        )

                        .uri("lb://FEIGN-CLIENT")
                )
                .build();
    }

}
```


好，那我接下来要定义这个第一个 root 里面的具体内容了声明一个 R 变量。而变量的第一个属性，我就给他立一些规矩。什么规矩就是你接收的地址匹配模式，也就是咱在前面配置的 pass 断言。对不对？这个 pass 断言咱给它叫做 Java 因为前面是在 YAML 模式定义的，咱叫了 YAML 那这里在 Java 模式咱就把它叫 Java 好了。


OK 这第一个断言定义好以后，咱前面说了它其实可以定义很多很多个不同的断言。那怎么来定义？大家看好，这里有一个 and 方法，我们把它放上来，当你有多个断言共同使用的时候，你可以使用 and 把它给关联起来。否则的话如果你不加and ，你是找不到你想用的那些断言的。比如 method 你看它是提示不出来的，而你加了一个 and 好，后面跟一个新的断言，我们这里打一个 method 它指定了什么？它指定了你即使地址匹配上了，那你也要满足我的 HTTP master 的要求才能转发到相应的目标地址。那咱这里给这个 HDD 没 master 指定成 get 断言。那咱这里看着红字看着不舒服，我们把这个红字先给去掉，返回一个 buildbuild 是什么意思啊？就是把当前这个 build 所有的属性全部组装，最终返回一个完整的 root locator 对象。


Ok. 紧接着这个里面的红字咱要怎么消除呢？在这后面定义这样一个叫 URI 指定它的目标地址就好了。我们这里依然把它指定到分。 client 以 LB 开头使用了负载均衡技术。 OK 分 client 那好，除了这个麦斯尔断言，咱前面课程介绍说了，咱不止要买一送一还有丰厚大礼相赠。咱这后面其实可以加很多 and 大家看，这里不光有 master 的断言，还有 cookie after 什么 before between 这各种各样的断言，比如说咱甚至可以怎么样呢？要求你的 header 中必须有指定的值，比方说咱这个 header 值叫 name 那你必须有一个叫 name 的值放在 header 里面，那才能通过我的锻炼。那咱这一节课程就送这两个断言。好勒，剩下的断言反正都在里面，大家自己去把玩就可以了。


OK 断言配置好以后是不是还少一个 filter 呢？我们这里把 filter 给定义出来，那同样它是一个数组 filters 那这里我们来定义第一个filter ，使用 strip 的方法， strip prefix 方法传入一个 1 那它和外面配置的 YAML 它和这个 YAML 文件中的这一段 filter strip prefix 是有异曲同工之妙。实际上两个就是相同的了。从这里配置完 strip prefix ，实际还可以配置很多个不同的filter 。我们这里再尝试着给它添加几个新的 filter 好了，比如说我是用 add response header 我想在 response 里面随便的动一动手脚。怎么动手脚呢？我给它的 response header 里面添加一个 parameter 它叫 Java parent OK 那它的值是什么呢？值我这里就可以随便指定了。比如说 gateway configuration。


Gateway config ok. 咱 filter 也远远不止这一种，它和断言都是一样丰富的。大家可以看到这里这里还可以像 request 里面加header ，甚至还可以修改这些 body 非常非常多。那这里还有 redirect 方法可以进行转发。所以说咱的 pass 主要是匹配这个路由规则，把你的应用请求导向正确的 URI 但是 filter 这里就跟逻辑部分相关了。那它可不像前面的断言没有什么对参数的修改，对咱的用户请求是只可远观不可亵玩这个 filter 是又能看又能玩，它可以随意的更改你请求中的各种参数。 OK 那在这里要不就先指定一个 add response header 好了，其他的就留给同学们自己把玩自己摸索了。好，那到这里整个配置就结束了吗？没错，就结束了，非常的简单。对不对？那接下来咱把 gateway 给启动起来，看一下这两个配置是否都可以正常的生效。


在启动 gateway 之前，我们有几个前置的应用需要启动，我先跟大家说一下。第一个， eureka 的 server 一定要启动起来。紧接着分 client application 1 和分 client application2 把它启动两个不同的 instance 改一下端口号启动两次，因为咱在路由规则中都需要调用分 client 来发起目标服务。好，那咱现在把 gateway 启动起来，好，看到 spring 成功一半。好勒已经启动起来了。那咱现在转到 pose 曼里，发几个请求试一试。 OK 那我 postman 的请求发送到 local host65,000，也就是 gateway 的地址，咱先尝试一下去调用 YAML 文件配置的路由，那它的路由转发规则是 yml 雅某。后面我们调用分 client 的 C hi 方法直接打 C hi 好了，OK我发起调用了走。你好，你看这里正确返回了，结果类似这 40,005 这个端口号，再调用一下变成了40,006，那说明负载均衡也生效了。


好， YAML 测试完，咱来测试在 Java 文件中配置到把这个 YAML 改成 Java 好，我们发起一次调用看。你看他说 not found 这是为什么？同学们能不能想起来，咱也是 get 请求，给同学 5 秒钟时间回忆，咱在断言里面还配置了什么额外的属性。


54321 好揭晓答案吧。咱看这个断言里面是不是还配置了一个 header 那咱自己的 header 我们看看是不是空空如也，什么都没有。当然是过不了了。咱把断言中药的那个 name 属性，给它配置上就可以了。它的 value 就是 IMock 好再发送一次调用试一下。果然获得了正确的反馈结果。


OK 那我们这样验证一下 filter 是不是生效，咱在这个 filter 里面是不是像 responseheader 里面加了一个新的参数叫 Java param 来到 postman 里，这下面就是它的 response 我们走到 header 这里看一下， header 里面有1234，第四个 parameter 它正是 Java param ，那这个 value 也是 gateway config 那这正正好好就是咱添加进来的，那说明咱在 YAML 文件中的路由规则以及在 Java 文件的路由规则全部都完美生效。


好。那到这里，本节内容就到此结束了，我跟大家总结一下。在本节当中咱们使的是双刀流的风格，不仅在 Java 文件中跟大家展示了如何配置一个路由规则以及如何使用 pass 还有 filter 同样的，在 YAML 文件中也给大家展示了一个 sample 同样的在 YAML 文件中也跟大家展示了一个 sample 通过这一节的学习，大家应该对 predicates 中的 pass 断言以及 filter 还有 UR I 有了一定的了解。


那这里大家有没有注意到一个小细节， yamo 配置文件和咱 Java 配置文件中有个什么不同啊？是不是发现这个 ID 没有配置啊？没关系的。如果咱在 Java 文件中没有配置 ID 那么 gateway 会为我们自动生成一串 ID 不信咱到 postman 里瞧一眼在 postman 里咱调用了 actuator 的 roots 列表方法。那看到这第一个吗？ root 这一个路由规则就是雅某为我们自动生成的 root ID 那它是怎么在 Java 中配置的那个路由规则？因此它的 predicate 和 futures 方法，这里打印出来的实际上都是 Java 类的 to string 方法打出来的内容。 OK 那么到这里这一节的内容就结束了，在下一节当中咱要玩一点花头啦。怎么说？那就是使用 party kiss 中的 after 断音，咱来设计一个简单的简易秒杀场景。也就是说利用网关层来限制这个秒杀场景 API 的访问。那同学，我们下一节再见。



