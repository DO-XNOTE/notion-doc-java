---
title: 2-2 电商系统集成Hystrix - 基础组件Dashboard+开放微服务端点 
---

# 2-2 电商系统集成Hystrix - 基础组件Dashboard+开放微服务端点 

[image](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/59274428-b680-47a0-ae81-2ad0d321e84f/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RCC5OZST%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T225654Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQC7qpvc4mLyXao4NduRnfyiiWsftnZiGk5OP%2Fm%2FlEMz5wIgbBtR3guCuetgDAIoxk1R%2FpbY1kVu%2FvZHlENjYTSSimYqiAQIxv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDFfHCpY1IFGnmEkPkSrcA6pRqkP%2F6vqucwkasuBrphSSnDbmcngPJBQuaI%2BbcmfZ8DMDBNZF3wHZGEmH9hm%2BPsi9O13bbcWOgt%2FoDH1mIae%2BbUo6mibeuUI6m8PKqBbuw6kRgis5g5wu7%2BxULPRwtgc96D55lNZ%2B0UJwsajpwlMojcKj9iOdbJ%2BzG70NRQPG10nbW14Bx4j73reE3Y5rpvLAw%2FpaW%2BD3MieYPdWJjZbzJAvGHzRoKUkrQmqYfe5IYOrhz%2B6HkfJmbQeJWH0vGloDQhI1pg58Pq12vgClqH8ScP%2Bc%2FO0YEmgZxDI2G1CdaHAWSOagr%2FwtwrTegRcyrkLW65EFtjDMUoMNozMbL3b5l8DRhEAw09Cg0UoiQ0b3t5abk%2BjADo1cFaQ%2BuFO2AEju0mXlgAyZpQrwrw1Q8jRi9UCxY4yPYXYRSgjwqPuyOOFXYcyHsxl3fhFD4W8NaQN3R%2FxlKjW5AZ2KuU6d8JqptD8rY5soHczJmOqV1PzIbCn5quvYhkcSeKsC6TMHa9E7lGRDTD%2FcwNDNQvTHUZTTInh4VSMQ%2BBNAOvFvERnOq39C4fDGV3Yv%2FCHmMybpH9PPwLdXkDUGblPanL%2BHyov77zlHhxm3YvLeXqfw1q%2FdHSMXAbXZw%2BSRk0tGMJO3%2F9IGOqUBRr0Q7n6bLdfBEgNMaZPFKRNreDCdpBkG9xaxJgzGOQ9mM%2FG9GSp5wkMX2VXiRIXaQz7OZYEdNoqL%2FYUsssuzdzo1%2BQ9J6YmEKDJy5n9DYaMrHabcLnoTd5FVYq7zz1QYIs1ZXbHcjriuFe2HiWk9lkD2X3DjZFmFPn%2FUhkntjJsYjac1w%2FnwHIChQYtDy2jll0E0cemcvvwpmfAna1u41VKqcK46&X-Amz-Signature=2088cf4615ddf19d79f7e6e262c73171f682389091204ffdeae30a498f7a5fb3&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

[image](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/1c8ce84a-0c14-4bbd-ac2d-e9063f5cea3c/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RCC5OZST%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T225654Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQC7qpvc4mLyXao4NduRnfyiiWsftnZiGk5OP%2Fm%2FlEMz5wIgbBtR3guCuetgDAIoxk1R%2FpbY1kVu%2FvZHlENjYTSSimYqiAQIxv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDFfHCpY1IFGnmEkPkSrcA6pRqkP%2F6vqucwkasuBrphSSnDbmcngPJBQuaI%2BbcmfZ8DMDBNZF3wHZGEmH9hm%2BPsi9O13bbcWOgt%2FoDH1mIae%2BbUo6mibeuUI6m8PKqBbuw6kRgis5g5wu7%2BxULPRwtgc96D55lNZ%2B0UJwsajpwlMojcKj9iOdbJ%2BzG70NRQPG10nbW14Bx4j73reE3Y5rpvLAw%2FpaW%2BD3MieYPdWJjZbzJAvGHzRoKUkrQmqYfe5IYOrhz%2B6HkfJmbQeJWH0vGloDQhI1pg58Pq12vgClqH8ScP%2Bc%2FO0YEmgZxDI2G1CdaHAWSOagr%2FwtwrTegRcyrkLW65EFtjDMUoMNozMbL3b5l8DRhEAw09Cg0UoiQ0b3t5abk%2BjADo1cFaQ%2BuFO2AEju0mXlgAyZpQrwrw1Q8jRi9UCxY4yPYXYRSgjwqPuyOOFXYcyHsxl3fhFD4W8NaQN3R%2FxlKjW5AZ2KuU6d8JqptD8rY5soHczJmOqV1PzIbCn5quvYhkcSeKsC6TMHa9E7lGRDTD%2FcwNDNQvTHUZTTInh4VSMQ%2BBNAOvFvERnOq39C4fDGV3Yv%2FCHmMybpH9PPwLdXkDUGblPanL%2BHyov77zlHhxm3YvLeXqfw1q%2FdHSMXAbXZw%2BSRk0tGMJO3%2F9IGOqUBRr0Q7n6bLdfBEgNMaZPFKRNreDCdpBkG9xaxJgzGOQ9mM%2FG9GSp5wkMX2VXiRIXaQz7OZYEdNoqL%2FYUsssuzdzo1%2BQ9J6YmEKDJy5n9DYaMrHabcLnoTd5FVYq7zz1QYIs1ZXbHcjriuFe2HiWk9lkD2X3DjZFmFPn%2FUhkntjJsYjac1w%2FnwHIChQYtDy2jll0E0cemcvvwpmfAna1u41VKqcK46&X-Amz-Signature=3e8b0adbcf44f28502c8ad34e09a5910f7239d09ade9f817306dd10ce6014875&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

hello 我们课旁的各位同学们，大家好，我是小半仙，这里我们接着上一节当中的内容继续往下走。咱这里去搭建一个 high streaks dashboard 然后再去几个微服务下面把需要做的一些 dependency 给它加上，并且把 high streaks 的监听端口给它打开。


好，那接下来我们这里创建一个 module 那这个 module 的名称和咱前面的 demo 是一样的，叫做 high streaks 杠 dashboard okay 点击 next 那这里的文件夹我们依然把它扔到 platform 下面。
好，三二一出来。好，那创建好了 pom 文件之后，在这里面需要添加的依赖项，就从前面的 demo 当中直接给它 copy 过来。好了我们看一下，这里的 dependency 总共有一二三三个，一个是 dashboard 它自己的注解。另外一个是 high strikes 最后一个 activator 端点。那咱这里还缺什么，还缺一个启动类。对不对好，我们这里去随便抄一个作业从哪里呢？就从 high streaks turban 这里把它的 pump 文件打开，把这个 build 节点给它原封不动地 copy 过来。那在作业抄过来之后，这个写作业的名字要记得改，com.imock点后面的这个名字，把 hi strix turban 给它改成 hi strix 。 Dashboard ok. 这下名字起得更长了。


好，那接下来我们在 dashboard 当中创建一个慕课网的地址 com 电 IMock 好，创建好之后咱去创建这个闷方法非常简单，给它起名 high strikes dashboard applicationok 那这里面就要给他去添加一些 annotation 比如我们这里第一个要添加的就是咱 spring cloud applicationok 那第二个也就是咱这一章的这一小节的主角是 high streaks 的 dashboard enablehigh streaks dashboard 好，那它的闷函数启动方法和前面是一样的，我们随便找一个就找 turbine 好了，把它直接 copy 过来。 OK 从这里打到这里，然后名字给他们改一下搞定。


那最后一个就是填写配置文件。咱的 dashboard 应该是整个 sprint cloud 所有组件当中配置文件最精简的了，这里只需要加入两个内容，一个是 sprint 的自报家门 spring application 好嘞，它的名称你叫啥嘞？ high strikes dashboard 报上名来，接下来是它的端口。你住哪嘞？那你这个 POD 我们给它指定到2002。


好了，咱先来后到，这个 platform 下面添加了几个中间平台组件，那么它这个端口号就自动往后移，注册中心是 2 万，然后特办是20,001，它是20,003。 OK 那到这里咱的 dashboard 就配置好了。那咱接下来就要去把微服务当中所有的 high streaks 的端点给它暴露出来，这个端点是通过谁通过 activator 来暴露的。那咱 act rate 的依赖已经加入到了 foodie cloud web components 这个里面的 pom 当中。你看，这里的依赖已经加入进去了，实际上来说，咱所有的微服务的这个 web 模块肯定是已经集成了 activator 服务的。


那我们这里首先从 user 这个应用开始去改起。好，我们既然已经有了 activator 这里只要做一个非常非常简单的操作是什么呢？那就是把它下面的这个 application deb YAML 给它打开，我们把端点在这里面开放出来。好，这里我直接复制前面应用的端点开放，直接把它 copy 过来。那我们通过这个通配符开启了所有 activate 的 endpoint 但是同学们注意，从安全的角度来考虑，我们通常在线上环境并不会把所有的全部开启。



我们这里通常只开放某些特殊服务。哪些特殊服务呢？那就是你用到的服务类，同学们是不是想多了？比方说我们有用到的 health info high strikes 这里都可以去配置。 OK 那我这里只在 application DEV 当中把这个所有端点给它打开。那在生产环境，同学们可以自己去配置一下。


好，打开了 active rate 之后，你启动起来会发现它并没有暴露 high strikes 的端点。那这里要怎么做呢？因为我们还没有把 high strikes 的依赖给它加入进去。这里我们可以选择把 high strikes 的依赖加入到 user web 当中，同时也可以把它加入到 user service 当中。那我这里是把它加入到了哪里，把它加入到了 user service 因为这样的话，那我不光可以在 web 应用当中使用hystrix ，在 user 里面也可以直接添加 hystrix 的注解。 OK 那同学们把这个配置同样的给它 copy 到其他的微服务当中。那我们这里选择 order service 在它的 palm 文件当中也把 hystrics 给它添加进去。


OK 那 order 加好之后，我们去 item 这三个微服务是比较核心的关键的微服务。我们把 item service 里面也在下面，把 high strikes 给它加入进去。 OK 那同样的，咱还要把 high streaks 它的这个 endpoint 也就是端叠也同样的复制到这几个微服务当中。好我们这里把刚才添加的 user 项目当中的这个端点给它 copy 一下，同样的复制到其他的微服务当中。那么这里先添加 order 好，在 order 下面开启所有端点，order添加完之后我们再移到 item 找到 item web 同样也是在 application DEV 下面把这个端点给它加上去。


OK 那加上去以后同学们如果想验证的话非常的方便，我们只要随便启动一个服务，比方说那我这里启动的是 user application 我把它给它直接启动起来，然后到浏览器当中去验证一下它的端点有没有开放成功。这就 OK 了。好，我们稍等半柱箱的时间，那这里显示应用已经启动起来了，我们转移到浏览器当中。好，开一个 tab 把 user 的这个 URL 给它打入进来。我们这里是 local hostuser 应该是10,002，后面直接跟 activator 好回车。那么看到这些所有的端点当中，只要搜 hystrixok 它在这里，那说明我们前面的配置就已经全部都生效了。那到这里，我们为电商项目集成 high streaks 所做的所有铺垫工作就已经全部完成了。那在接下来的一个小节里，我将带大家一起去写具体的熔断降级的业务代码，还有配置。 OK 同学们，那我们下一小节再见。

```java
foodie-user-web:
application.yml加入：

management:
   endpoint:
      health:
        show-details: always
   endpoints:
     web:
       exposure:
         include: "*"

   security:
      enabled: false
```

