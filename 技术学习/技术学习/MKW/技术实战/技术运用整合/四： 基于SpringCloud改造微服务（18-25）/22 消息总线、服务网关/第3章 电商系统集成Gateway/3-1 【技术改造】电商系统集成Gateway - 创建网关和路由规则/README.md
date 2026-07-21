---
title: 3-1 【技术改造】电商系统集成Gateway - 创建网关和路由规则
---

# 3-1 【技术改造】电商系统集成Gateway - 创建网关和路由规则

[image](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/bc98aba2-177a-4104-8b53-9bf7042527d4/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WTWWBXQM%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T225746Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDfzEzOt%2FeJzN8wRAtiKcYl5SD0LwPW4riYxE%2FE6hCL%2BgIgNtZjDoHbRhWBUyEO5gI4zTU74sb9jxdTPwx7uBE2mHgqiAQIxv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDPSNrTxpNO31a4CvAyrcA2HNdQCHDt70pb764NxnhQBt%2FZuN7nfVwviKYLiH2zySrcpWP4WLpgQODobAaZidWZYP8jTbYSAhyudARLmf4xFdDbvLd6%2BnNlkfKiEaHU8bM9uauvitYZv%2BpmRJzy2HHCZtJmco7Zj9xc1Gqw%2FQfTquuTz59VWNXYozx0Ohwmat2xQVY9Q42e8XuUUV0dhLXpykILsUQSw1akCAQ2Oh6cpie24luhsbaGuk%2FGXnCmB2RwxcyEVeeEBEJ5GCNXUmxrCqcwrYMlk13OmVHjQKKrUvQJA85W7zuFOh4teozZHrKzmCfwwbsVxcxJ6Xq6v3ZGLH7etb%2FrD6FJtC1Z%2F0ixoHqmiBTEHp63%2B1%2FR3Op8D3kMDwmn7423KVaHL8mbNyv5%2FoLuYmt0RbSl32Yd1cp0S18ULjg9GjW%2FUTF3HBbZURL5KCy7Pn%2F3ZK3fNg37U99Q0vkWisFpihbHTLBQGtoQfVHE%2BdTtca775wL2KBcPR5Qnk%2FdJjlpH%2FgTLGfwa7wP6N1e4pgS29y5XzKbKSVYD3fGZie8R9vxmFMIXjRfZvfOsFac7WRTBVAQjlVLAiULbuQurUjhESsd%2FbeRU9B2OnnwK2l5mn7DCgBFHOw3s%2B1x2Gu6WAcPUSeW%2BYXMNq3%2F9IGOqUBUtcaRSe26nQA1dly4n1kLNoM4504Vz6y0MO1VKGobVv2Wz%2BPCvPqEcQgZa2QmRvx2CsdHOQzK3JVp2Q55K0spcvLGUXefUgLmdAGoljXFYrsO8i9ilE%2F6xRQRTj8awIpXjcGVGM8t7Va2uvy8GZi02lI58aAfCcMvEXGtS%2B1c6KhKm235Z%2FRNsbEvQCnXBgbBoxMbUwP6f0c6m7oPVYZ8v2K54s%2F&X-Amz-Signature=0b2aa32cd3fd73093596cfdd362eada74ca177d1859d3c608b2b7986d929a7b6&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

[image](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/d69cb7f6-5a6f-4335-b4c3-1698e9f8ad16/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WTWWBXQM%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T225746Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDfzEzOt%2FeJzN8wRAtiKcYl5SD0LwPW4riYxE%2FE6hCL%2BgIgNtZjDoHbRhWBUyEO5gI4zTU74sb9jxdTPwx7uBE2mHgqiAQIxv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDPSNrTxpNO31a4CvAyrcA2HNdQCHDt70pb764NxnhQBt%2FZuN7nfVwviKYLiH2zySrcpWP4WLpgQODobAaZidWZYP8jTbYSAhyudARLmf4xFdDbvLd6%2BnNlkfKiEaHU8bM9uauvitYZv%2BpmRJzy2HHCZtJmco7Zj9xc1Gqw%2FQfTquuTz59VWNXYozx0Ohwmat2xQVY9Q42e8XuUUV0dhLXpykILsUQSw1akCAQ2Oh6cpie24luhsbaGuk%2FGXnCmB2RwxcyEVeeEBEJ5GCNXUmxrCqcwrYMlk13OmVHjQKKrUvQJA85W7zuFOh4teozZHrKzmCfwwbsVxcxJ6Xq6v3ZGLH7etb%2FrD6FJtC1Z%2F0ixoHqmiBTEHp63%2B1%2FR3Op8D3kMDwmn7423KVaHL8mbNyv5%2FoLuYmt0RbSl32Yd1cp0S18ULjg9GjW%2FUTF3HBbZURL5KCy7Pn%2F3ZK3fNg37U99Q0vkWisFpihbHTLBQGtoQfVHE%2BdTtca775wL2KBcPR5Qnk%2FdJjlpH%2FgTLGfwa7wP6N1e4pgS29y5XzKbKSVYD3fGZie8R9vxmFMIXjRfZvfOsFac7WRTBVAQjlVLAiULbuQurUjhESsd%2FbeRU9B2OnnwK2l5mn7DCgBFHOw3s%2B1x2Gu6WAcPUSeW%2BYXMNq3%2F9IGOqUBUtcaRSe26nQA1dly4n1kLNoM4504Vz6y0MO1VKGobVv2Wz%2BPCvPqEcQgZa2QmRvx2CsdHOQzK3JVp2Q55K0spcvLGUXefUgLmdAGoljXFYrsO8i9ilE%2F6xRQRTj8awIpXjcGVGM8t7Va2uvy8GZi02lI58aAfCcMvEXGtS%2B1c6KhKm235Z%2FRNsbEvQCnXBgbBoxMbUwP6f0c6m7oPVYZ8v2K54s%2F&X-Amz-Signature=f354a52fe4c7b396a5531cd4af7b4129162f67bee2ab25810f9e768470a1dca7&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

hello 慕课网的各位同学们大家好，又到了这一周的电商系统改造环节了。那在这个环节的第一节里，我们做一点简单。
部分。首先为咱的 foodie 项目创建一个 gateway 组件，添加到 platform 这一个文件夹下面。接着咱在 gateway 里面配置一些简单的路由规则，将用户请求路由到各个微服务组件当中。 OK 同学们，那我们 entireJ 走起，我们下面来创建一个新的茅酒。那给这个毛就起名就叫 gateway 好，点击 next 把它放到哪里呢？放到 platform 下面，咱的 platform 将迎来第五个组件，网关层 321 出来。那咱的网关层里面都有哪些 dependency 需要添加呢？我们挨个把它给加进来。第一个组件是咱网关层它自个的依赖项就是 gateway 那第二个依赖，因为咱的网关层需要到 eureka 注册中心那里拉取已经注册的微服列表。所以这第二个依赖是尤瑞卡的 client 依赖。好，那第三个依赖是咱的 X ritter 还记得前面我们在 demo 环节当中，通过服务端点这里，对网关层的路由规则进行了增加和删除操作。那最后一个依赖，我们把 sprint data 对 Redis 的支持给它加上，这是 spring data Redis reactive 这个依赖项给它添加进来，待会会有用到的。


OK 那这四项添加进来之后，最后一个步骤，我们这里要给它添加上 U 的节点，因为网关层我同样也要把它放在外面，用价包的形式来启动。所以我们这里把 build 节点给它 copy 过来。好， copy 过来以后咱把这个名称给它改一下，叫 gateway application 好，那咱既然这个名字已经给起好了，我们接下来就来创建这个 gateway application 也就是启动类。那我们首先在这个包下面把包名创建出来，com.imock点击回车。好勒。在这个新建的报名下面，我们把刚才创建的这个类 gateway application 给它添加进来。那现在扣大帽子。第一个大帽子是 enable discovery client 把它作为一个服务提供者到注册中心上。

```java
<?xml version="1.0" encoding="UTF-8"?>
<project xmlns="http://maven.apache.org/POM/4.0.0"
         xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
         xsi:schemaLocation="http://maven.apache.org/POM/4.0.0 http://maven.apache.org/xsd/maven-4.0.0.xsd">
    <parent>
        <artifactId>foodie-cloud</artifactId>
        <groupId>com.imooc</groupId>
        <version>1.0-SNAPSHOT</version>
        <relativePath>../../pom.xml</relativePath>
    </parent>
    <modelVersion>4.0.0</modelVersion>

    <artifactId>gateway</artifactId>
    <packaging>jar</packaging>

    <dependencies>
        <dependency>
            <groupId>org.springframework.cloud</groupId>
            <artifactId>spring-cloud-starter-gateway</artifactId>
        </dependency>

        <dependency>
            <groupId>org.springframework.cloud</groupId>
            <artifactId>spring-cloud-starter-netflix-eureka-client</artifactId>
        </dependency>

        <dependency>
            <groupId>org.springframework.boot</groupId>
            <artifactId>spring-boot-starter-actuator</artifactId>
        </dependency>

        <dependency>
            <groupId>org.springframework.boot</groupId>
            <artifactId>spring-boot-starter-data-redis-reactive</artifactId>
        </dependency>
    </dependencies>

    <build>
        <plugins>
            <plugin>
                <groupId>org.springframework.boot</groupId>
                <artifactId>spring-boot-maven-plugin</artifactId>
                <configuration>
                    <mainClass></mainClass>
                </configuration>
                <executions>
                    <execution>
                        <goals>
                            <goal>repackage</goal>
                        </goals>
                    </execution>
                </executions>
            </plugin>
        </plugins>
    </build>

</project>
```


那第二个。 Spring boot application. 好嘞，那最后一步，咱把这个 public 的慢方法给它添加进去，不管外面的逻辑代码怎么变这个闷方法永远不变的。就像说你大爷永远是你大爷 spring application wrong 好，我们把这个类名称直接给它塞进去点 class 好勒完事。


那咱的启动类创建好了之后，接下来我们是先来配置配置项还是先来创建路由规则？那咱还是先从简单的做起，咱先来配置一个配置项，在 resources 文件夹下面，我们创建一个 application.yamlok 那这里我们开始依葫芦画瓢开始去创建它的配置内容。这里面第一个是自报家门 spring application 来。你叫啥叫 gateway 有点光板，我们不能把它称作光板。 gateway 要加一个 platform gateway 平台，你看任何组件加上平台两个字修饰就显得高大上了。对不对？咱不能叫商品中心，咱要叫商品平台。营销优惠计算服务咱也叫营销优惠计算平台。所以起项目名很有学问的。


好，那咱接下来配置什么呢？咱配置 cloud gateway 相关的一个属性是哪一个属性？ Locator. 还记得前面咱是怎么配置locator ，咱是把这个 enabled 配置成 true 这样的情况下，咱的 gateway 会去注册中心上拉取所有已经注册的服务，并且为他创建一个默认的路由规则。对不对？那与此同时，这个默认的路由规则还有一个属性，控制它的路由规则中的路径是大写还是小写叫什么呢？ lower case service ID 对不对？好，那老师在这里要把这个 enable 的给它关掉。因为为什么呢？因为在生产环境中我们一般不会为一个服务创建默认的路由规则。所以这个配置项一般就是大家在本地做测试可以用，但是在生产环境，我们一般会把这个 enable 的给它关停掉。


OK 好，那接下来配置谁？ roots 这里要配置吗？不要老师这里，把所有的路由规则都放到代码当中配置，其实咱放配置文件和放代码中。那这两种方式，同学们按个人喜好其实都是可以的。不过我个人更推荐在代码当中，这样控制力更强。而且从表现形式上来说，你在代码中去声明一个类，可读性我觉得也会更好一点。


OK 那咱接着往下分，这里声明完了，我们给他声明一个 serverserver port 这边排座次， get 位排老几。我看 platform 下面有 123455 个，那你 gateway 排在204，咱是从 0 开始算作 4 的 20,004 这两个配置好了，咱还缺一个 eureka 的配置。对不对？我们随便从配置中心这里 copy 一段，我们把 eureka 这段配置给它 copy 过来，好勒放到 gateway 当中来，就在这走。你 OK 那除了这个配置，剩下的还有什么？ actiator 端点，服务端点咱这里要把它给开启，那再去抄一把作业，走到 config server 这里。好，把这个 actiator 端点全部给他拿过来。


其实我们看到咱的 gateway 这里，所有配置项都是，老老实实规规矩矩的方式来声明的对不对？咱没有用到前面学习的黑科技 config 配置中心。那么这里加一行注释，咱以下写的这些配置项有一些我们可以去尝试着集成配置中心 config server 来配置。所以咱微复阶段的课程，给同学们留的创作空间是非常大的。舞台很广阔，咱学了一门技术，可以把它用在各个的 platform 组件当中，各个的微服务组件当中。


OK 那我这里留一行配置，可以尝试集成 config server 来进行配置。好，那咱配置文件也搞定了，接下来可以杀个回马枪回来去。怎么样呢？去配置咱的路由规则，我这里新建一个 Java class 把它起名叫做 roots configurations configuration 好嘞。 OK 好，那咱这个类我们把它声明成一个 configuration 的类，把它加载进来。那接下来就要开始去声明病了，我们来一个 public 方法，然后它返回的类型是谁？是 root locator 对不对？因为我们要定位一个路由器方法名称就叫 roots 好了，接受了参数。那跟前面的 demo 环节一样，是一个 builder 是哪个 builderroot locator 的 builder 好嘞，接下来，我们就配置一些最简单的路由规则，好骑手一个。 Return. return 什么呢？咱 builder 的 roots 构造起来。好，那么这里开始从咱的用户微服务 user 微服务开始构建。那这第一个 root 我们尝试把所有发向用户模块的微服务的 URL pattern 给它去构造出来。


那我们这里可以去参考什么呢？参考咱 user domain 中的 controller 代码，咱在 user web 当中有暴露给前端页面的这些 controller 方法。同时在 user service 当中也有暴露给后台所有微服务的 user service 代码。


那这两部分，同学们觉得是不是都要暴露给前端呢？不用，咱跟前端直接交互的是 web controller 里面的这些 controller 方法，那我们只用把它们暴露给前端用户就行了。所以咱在 gateway 这里，只用配置在 web 这一个子模块当中的所有 controller 的 URL 就可以了。因为咱的前端页面是一定不会直接发送请求到后台的 user service 这个服务里的。那咱的这个 web controller 有几个呢？ 1234 有四个，咱要把这四个 controller 中的 request mapping 这一段，每个应用请求全部都给它抓出来配置到这里。


好，那咱在一个 root 中配置多个 URL mapping 是怎么配置的呢？很简单。第一个，把它的 pass 给它加进去，比方说我这里用户模块，那地址匹配，我这里给它加上后面用通配符来结束。好，那我这里配置了其中的一个 uipad 那剩下的几个怎么配置？咱看它这个 pass 里面参数的名称叫什么叫 patents 对不对？那我们点进去看。不定长的参数，它可以接收多个 pattern 所以在后面的这些 URL 只用根逗号把它 tend 到这一个结尾处就可以了。


那剩下的都有谁呢？ passport 对不对啊？好，除了 passport 那我们应该还有用户中心的这个 user info 好，我们把 user info 给它打印过来。同学们注意，这个 I 要大写，user info 的 I 是大写的。好，那除了 user info 最后一个是谁？是咱的 center 我们把这四个配上，然后他们通通的要转发到哪里呢？转发到 URI 好他的 URL 是谁？我们打上 LB foodie user service ，就是这么简单到这里就完成了第一个的配置。那我们接下来就依葫芦画瓢，把剩下的几个 root 全部配置好就可以了。那第二个 root 是谁的？咱 user 创建完了，第二个该轮到 item 了。 item 这里非常简单，什么都没有，它只有一个地址是在 ctrl 里面配置的，就叫items。那我们继续往后。


第三个我们配置 card 购物车，那购物车这里也非常简单，就叫 shop card 购物车。完了这回总轮到我们的订单中心了。对不对？ order 这里会稍微多那么一点，咱的订单中心有一个是叫 orders 好，那接着还有一个叫什么叫 my orders 那注意，这个 O 它的大小写你要对应上，那它这里是小写。那第三个路径就是 my comments 我们把它也给添加上去。


OK 那这里面还缺少什么，还缺少一个 search 对不对？那 search 老师这里留给同学们，当着自己的作业，我们把它往上放到上面。 OK 那我这里竖一个 flag 提醒大家去这边把这个 search 模块给它改成自己创建的应用中的 URL pattern 好，那我这里先给他几个默认的治好了。咱前面说过， search 模块是主搜，那么我们把所有跟搜索相关的内容全部放到了 search 它的 URL pattern 这一个 search 是少不了的。那第二个 pattern 我们还记不记得有那个首页的主图轮播图这里，那它的 controller 是发到 index 下面的。那后面还有两个很特殊的 URL 是哪两个呢？我们看一下 item control 了。同学们在这个商品中心的 item controller 下面往下走，发现我们在微服务改造过后的这个 item controller 是不是少了几个方法啊？对不对这个搜索商品的方法都去哪了呢？没错，我们把这些方法按照计划都要把它移到主搜，也就是搜索模块。
所以我们在这里要额外配置哪些内容呢？那就是原先咱放在 items 下面的搜索商品列表是谁？ search OK 那这后面还要跟通配符吗？不用了，这就是它末尾的 URL 就是以色值结尾的。好，那除了这个URL ，还有一个，那就是 items 斜杠 cart itemsok 好，我们把这四个服务全部都配到了 foodie search service 当中。不过我建议同学们，把后面两个服务把它的路径地址重构一下，最好把它在前面再加上这样一个 search 那老师这里依然保持原汁原味的风格，是为了和前面的系统做一个向前兼容。通过这种配置，我原先的前端页面依然可以访问到这两个接口。好，那同学们这里要记得，把 40 幅自己实现掉。那么这里加上一个注释去提醒大家把这个 40 服务给它实现了，不要漏掉了。好，那咱的基础配置部分到这里就结束了。但是在结束之前，我要提醒大家一个非常容易被遗漏的地方。咱这一个如此声明了之后还没有加这个 bin 同学们在自己写代码的时候千万不要忘了加上 bin 那这样的一个病住检是很多同学们在实际的项目当中很容易把它遗漏掉的地方。


那如果你漏掉了之后，你会发现怎么回事啊？我配置的路由规则怎么不起作用了？然后就到提问区域里面去问老师啦。我的路由规则为什么没有生效啊？其实路由规则没生效，它原因有很多。那同学们第一个排查的是你这个 roots 有没有被声明成病？那还有一种很方便的方式就是什么呢？前面我们在课程 demo 当中是不是教过大家使用 activator 的 roots 端点来查看所有已配置的路由规则。首先我们来看一下你在这里面配置的规则能不能透过 activator 的端点把它暴露出来。如果在上面你没有发现这个配置的规则，要么是你的这个方法没有加上 bin 或者你的这个 rules configuration 没有加上这个 annotation 那各种原因导致你这个声明的路由规则没有被咱的 gateway 给识别出来。那如果配置规则都是好的，那同学们就要两个方向排查。


第一个，你的 URL mapping 是否正确，包括大小写，包括它的路径层级等等都要完全一致。接下来要注意的就是你这个 service name 是不是和咱在 U 瑞卡注册中心上面已经发布出来的服务名称是一样的，如果不一样，那自然是找不到对应的服务了。好，如果到这一步还没有发现问题，教同学们一个能解决 99% 的问题的方式，那就是把所有服务关掉，然后重启一遍。往往重启能解决 99% 的问题，剩下1%，那就来找老师问。好，同学们，那这节内容就到这里结束了，我们创建了一个 gateway 的组件，然后配置了最基础的简单的路由规则。那接下来的小节中，我们再逐步完善咱的 gateway 持续的添砖加瓦，把接下来的用户登录状态检查，也给它继承到咱的 gateway 当中。
那在最后，老师这里要给大家揭晓一个彩蛋，我在配置路径的时候，这里故意给大家留了一个坑。那大家能看出这些所有路径当中有哪些路径长得比较特殊吗？如果没有发现没有关系，等同学们启动项目去调用服务的时候，就会发现某些服务似乎调不通。这就是咱在配置路径匹配规则的时候非常容易犯的一个小错误，相信很多同学们一定也会遇到过的。那正确答案就在老师的源码里面，同学们就去源代码里面找答案。 OK 同学们，那下一小节我们再见

```java
package com.imooc;

import org.springframework.cloud.gateway.route.RouteLocator;
import org.springframework.cloud.gateway.route.builder.RouteLocatorBuilder;
import org.springframework.context.annotation.Bean;
import org.springframework.context.annotation.Configuration;

/**
 * <h1></h1>
 */
@Configuration
public class RoutesConfiguration {

    @Bean
    public RouteLocator routes(RouteLocatorBuilder builder) {
        return builder.routes()
                //  FIXME 添加好这个（作业） search 服务自己实现掉
                .route(r -> r.path("/search/**", "/index/**", "/items/search","/items/catItems")
                        .uri("lb://FOODIE-SEARCH-SERVICE")
                )

                .route(r -> r.path("/address/**", "/password/**", "/userInfo/**", "/center/**")
                        .uri("lb://FOODIE-USER-SERVICE")
                )

                .route(r -> r.path("/items/**")
                        .uri("lb://FOODIE-ITEM-SERVICE")
                )

                .route(r -> r.path("/shopcart/**")
                        .uri("lb://FOODIE-CART-SERVICE")
                )

                .route(r -> r.path("/orders/**", "/myorders/**", "/mycomments/**")
                        .uri("lb://FOODIE-ORDER-SERVICE")
                )
                
                .build();
    }

}
```




