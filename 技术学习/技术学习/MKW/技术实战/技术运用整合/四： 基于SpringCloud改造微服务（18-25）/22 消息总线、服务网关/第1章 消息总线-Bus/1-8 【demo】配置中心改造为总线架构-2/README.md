---
title: 1-8 【demo】配置中心改造为总线架构-2
---

# 1-8 【demo】配置中心改造为总线架构-2

[image](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/6b77536c-640f-4d82-a4fb-ecef9cb343d3/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SXXMFQKM%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T225725Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIGLo3JVXlfQe4ZPMyERrA6BOYwTokwfrOiudw93T98NDAiEAzvhebgwrg92gmfumNrovtGGNcPfHgRVvaBL9c6LuZiQqiAQIxv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDFOPKo2s8fvqzbU%2FXCrcA0SiQISbdesRC3Jzycr2mWnmksuMnQYqmJXymF2RS%2FTILLJdu%2BmwJkgPf9ymqlaOufbVTBZCM2tJGzyaG%2BwAF%2FoZow0ruCkWVjExw%2BDREk0y9EBqQGDHnQFmkfDS0MYCDIIOnuKvoRq6YEIwA0crlo9N0OZ2POPrD%2F7tGKURjbplQukIIeS0vOFqcsSIaVrilCVQlzwwzbBIU0ryRn40N52TSp74MfO6zYTftUj8qq%2BtNuFS7HqvwqaoCJjQu14wwHBDvxnyam4ab037NdRqM4fx8IUpGgHs6FFk3VNUc%2Bl9J0prMNtHOtsBOC9jCOa7B6oTvJUNpgIGfFlyGwHkj7N2iKcL6s6XmQcRvC9R2Gexvb6EB0%2B5jDnyFqTEaUGAFDl2VISl1%2B6p6FJORt%2FBfA9KHklmSV59NZ%2Brcko9jkapGKVOngqUIO6KFr2QcogBzXYOyIypcH1UbxZD9nnMhpCjwimyO93TAImfueNlqM78rTIXvkBw8tLCY4BDYIMVJjdmY49fc5n6fmvtHbbWCvGCYf2fUJLsnqjAx3FzqL%2BbwwJ1Fl0d6oPDgzEVUUic8R3X%2BnO18EUHQPQ4pR5yYMTMol7gnoApaxnLOqDIjhwUHaGQHme1AVcuU8JCMKG6%2F9IGOqUB4lk5y8PGn12rSR%2B0Qz%2FwluY8tCQg3wPrCzRQ5zY3dThf6ICbGB0MPn8zbb%2FAHqw%2F%2FMMk%2F6CGqmlaRG4p%2FYY8IRsY5woeorZX1sR0dvTf8uy9ioofCZR%2Fej5HtgjxvHYiAIda8GHhTcmVrFNqpq1dC8%2F25jPXUhr4JkC2snO%2Bdrh2wXzTtSFYePL37onxYDxxR9xJjp0e7heESEfCoSXKp4e0Iw9u&X-Amz-Signature=4d734380e197009c968d78a14a8bc147aa33efa5ef834bf0e5f1d781efe0ead2&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

[image](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/e9ad2a92-1c67-48f4-86e5-fc20376ecbe0/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SXXMFQKM%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T225725Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIGLo3JVXlfQe4ZPMyERrA6BOYwTokwfrOiudw93T98NDAiEAzvhebgwrg92gmfumNrovtGGNcPfHgRVvaBL9c6LuZiQqiAQIxv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDFOPKo2s8fvqzbU%2FXCrcA0SiQISbdesRC3Jzycr2mWnmksuMnQYqmJXymF2RS%2FTILLJdu%2BmwJkgPf9ymqlaOufbVTBZCM2tJGzyaG%2BwAF%2FoZow0ruCkWVjExw%2BDREk0y9EBqQGDHnQFmkfDS0MYCDIIOnuKvoRq6YEIwA0crlo9N0OZ2POPrD%2F7tGKURjbplQukIIeS0vOFqcsSIaVrilCVQlzwwzbBIU0ryRn40N52TSp74MfO6zYTftUj8qq%2BtNuFS7HqvwqaoCJjQu14wwHBDvxnyam4ab037NdRqM4fx8IUpGgHs6FFk3VNUc%2Bl9J0prMNtHOtsBOC9jCOa7B6oTvJUNpgIGfFlyGwHkj7N2iKcL6s6XmQcRvC9R2Gexvb6EB0%2B5jDnyFqTEaUGAFDl2VISl1%2B6p6FJORt%2FBfA9KHklmSV59NZ%2Brcko9jkapGKVOngqUIO6KFr2QcogBzXYOyIypcH1UbxZD9nnMhpCjwimyO93TAImfueNlqM78rTIXvkBw8tLCY4BDYIMVJjdmY49fc5n6fmvtHbbWCvGCYf2fUJLsnqjAx3FzqL%2BbwwJ1Fl0d6oPDgzEVUUic8R3X%2BnO18EUHQPQ4pR5yYMTMol7gnoApaxnLOqDIjhwUHaGQHme1AVcuU8JCMKG6%2F9IGOqUB4lk5y8PGn12rSR%2B0Qz%2FwluY8tCQg3wPrCzRQ5zY3dThf6ICbGB0MPn8zbb%2FAHqw%2F%2FMMk%2F6CGqmlaRG4p%2FYY8IRsY5woeorZX1sR0dvTf8uy9ioofCZR%2Fej5HtgjxvHYiAIda8GHhTcmVrFNqpq1dC8%2F25jPXUhr4JkC2snO%2Bdrh2wXzTtSFYePL37onxYDxxR9xJjp0e7heESEfCoSXKp4e0Iw9u&X-Amz-Signature=b862ff2e033b775b4a155fe5015f3d47c9721c1fceb353fbd95578a2a50450ce&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

[image](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/a5738eb5-e083-4407-badc-d70a4202fd36/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SXXMFQKM%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T225725Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIGLo3JVXlfQe4ZPMyERrA6BOYwTokwfrOiudw93T98NDAiEAzvhebgwrg92gmfumNrovtGGNcPfHgRVvaBL9c6LuZiQqiAQIxv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDFOPKo2s8fvqzbU%2FXCrcA0SiQISbdesRC3Jzycr2mWnmksuMnQYqmJXymF2RS%2FTILLJdu%2BmwJkgPf9ymqlaOufbVTBZCM2tJGzyaG%2BwAF%2FoZow0ruCkWVjExw%2BDREk0y9EBqQGDHnQFmkfDS0MYCDIIOnuKvoRq6YEIwA0crlo9N0OZ2POPrD%2F7tGKURjbplQukIIeS0vOFqcsSIaVrilCVQlzwwzbBIU0ryRn40N52TSp74MfO6zYTftUj8qq%2BtNuFS7HqvwqaoCJjQu14wwHBDvxnyam4ab037NdRqM4fx8IUpGgHs6FFk3VNUc%2Bl9J0prMNtHOtsBOC9jCOa7B6oTvJUNpgIGfFlyGwHkj7N2iKcL6s6XmQcRvC9R2Gexvb6EB0%2B5jDnyFqTEaUGAFDl2VISl1%2B6p6FJORt%2FBfA9KHklmSV59NZ%2Brcko9jkapGKVOngqUIO6KFr2QcogBzXYOyIypcH1UbxZD9nnMhpCjwimyO93TAImfueNlqM78rTIXvkBw8tLCY4BDYIMVJjdmY49fc5n6fmvtHbbWCvGCYf2fUJLsnqjAx3FzqL%2BbwwJ1Fl0d6oPDgzEVUUic8R3X%2BnO18EUHQPQ4pR5yYMTMol7gnoApaxnLOqDIjhwUHaGQHme1AVcuU8JCMKG6%2F9IGOqUB4lk5y8PGn12rSR%2B0Qz%2FwluY8tCQg3wPrCzRQ5zY3dThf6ICbGB0MPn8zbb%2FAHqw%2F%2FMMk%2F6CGqmlaRG4p%2FYY8IRsY5woeorZX1sR0dvTf8uy9ioofCZR%2Fej5HtgjxvHYiAIda8GHhTcmVrFNqpq1dC8%2F25jPXUhr4JkC2snO%2Bdrh2wXzTtSFYePL37onxYDxxR9xJjp0e7heESEfCoSXKp4e0Iw9u&X-Amz-Signature=c5d1d1a53d648afb3ad8a7ec20e30d1c359819dae04e3389d0517a21578b55c8&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

嗨慕课网的各位同学们，大家好，很少有机会在印胎里 G 里面跟大家第一句打招呼，那我们喊出自己的口号，编程使我快乐。 996 是我的福报，咱接着上一节的福报继续来享受。上一节创建了一个 config bus server 那我接下来要创建一个 client 从 config server 里面拉取配置，咱们给这个 client 起名叫 config 杠 bus clientok 点击下一步毛球内幕依然和前面保持一致，然后把它扔到 bus 这个文件夹下面，点击 finish 321 走 OK 它的 dependency 我们依然从其他地方借鉴回来。比如从 config client 这里，我们悉数的把这些 dependency 全部 copy 过来。


copy paste 所谓天下文章一大抄。现在很多在 it 界的代码，尤其是开源项目总会被抄来抄去。之前还爆出过阿里的团队，剽窃别人的开源代码，连变量名都不带修改的，只是把作者给抹掉了。真是大跌眼镜。所以说把价值观挂到嘴上的公司，那确实没太有底线。


早上现在创建了 12344 个 dependency 还缺一个，大家知道是谁吗？那就是我们前面引入的 bus 的 dependency 我们到 config bus server 里面，把它给 copy 过来。好，找到了是这个 bus amqp 好，我们把它拷贝到这里。这里补充一句，咱引入的这个 amqp 它是专门给 rabbit MQ 来做适配的。那如果大家想使用 Kafka 怎么办呢？ Kafka 的配置是另外一个了，只要把这个 copy 一下，然后粘贴把最后的 amqp 改成 Kafka 就可以了，非常简单啊。啊我这里再给它添加一个注释。 Kafka 实际上对咱写代码是完全没感知的。所以你看 bus 的设计里面真是非常非常好，它对你系统应用的侵入性已经尽可能的降低到最低了。我特别喜欢这种风格的插件，你引入一个dependency ，加一个 rab MQ 的配置，那它就自动生效了。这个组件用起来是方便，但是咱学习技术可不能浮于表面，只会用。那可不行，咱后面章节还要去深入代码里面研究一下他为什么这么方便，他是怎么实现这个广播消息的通知的。那我这里先把卡夫卡的注掉，

```java
<dependencies>
        <dependency>
            <groupId>org.springframework.cloud</groupId>
            <artifactId>spring-cloud-config-server</artifactId>
        </dependency>

        <dependency>
            <groupId>org.springframework.cloud</groupId>
            <artifactId>spring-cloud-starter-netflix-eureka-client</artifactId>
        </dependency>

        <dependency>
            <groupId>org.springframework.boot</groupId>
            <artifactId>spring-boot-starter-actuator</artifactId>
        </dependency>


        <!--Rabbit MQ 做适配的-->
        <dependency>
            <groupId>org.springframework.cloud</groupId>
            <artifactId>spring-cloud-starter-bus-amqp</artifactId>
        </dependency>

       <!-- Kafka 做适配的  -->
      <!--  <dependency>
            <groupId>org.springframework.cloud</groupId>
            <artifactId>spring-cloud-starter-bus-kafka</artifactId>
        </dependency>-->

    </dependencies>
```

因为我们暂时还用不上它。那 123455 个 dependency 完成以后给它加一个 packaging 指定成价。其实如果大家都是在 tanij 里面直接运行的，这一个不加也是没问题的。


OK palm 指定好了以后，咱接着要把代码给迁移过来了，首先要在你的夹板文件夹下面创建一个路径，我们依然叫 com.imock.spring cloud 回车。那这里面都有哪些类呢？我们原封不动的照抄好了，变量名也不用改，甚至类的名字都不用改，一股脑的把它 copy 过来。


the paste OK 这个 application 类，咱适当的意思，改一个名字叫 config bus client applicationok 好，剩下的代码还用动吗？完全不用动包括这些 ctrl 和 refresh ctrl 的这所有的代码我们都不要动这个 bus 推送的通知。记住对代码是无感知的，它只在乎咱的 YAML 配置上会体现出略微的不同。既然咱提到了 YAML 配置，那接下来我们就来创建 YAML 文件，我们依然选择从 config client 这里把 YAML 文件 copy 过来，然后改改就可以了。
OK 改哪些内容呢？我们依次来看一下，收集小桌板，首先这个 application name 咱是不是要把它改掉原先叫 config client 那咱把它改成 config bus clientok 接下来的这里的配置，我带大家顺带复习一下，当你的 application name 和 get hub 文件中配置的文件名称不一致的时候，我们可以通过 config 节点下的 name 强制指定一个 application name 那所以在这里咱实际上是把 config consumer 作为了 application name 来向 github 上面拉取文件的。


OK 那接下来往下看，discovery enable true 没问题，这个 service ID 是不是咱要改一下，要保持跟最新的 config server 保持一致。咱这里要使用的 config server 是谁？是这个 config bus server 对不对？那所以我们需要从这里面把它的 application name 也就是 config bus server copy 过来，然后替换掉这个 config server eureka OK 那这一步配置完了，接下来 server 的 port 那我把它配置成61,001，这样不会和以前的酒冲突。往下看，这都不用更改。尤瑞卡这里也配置好了，不用更改。




Ok.那同样的，在 client 这里，我也需要把所有的 actuator and points 全部打开。 OK 这里看上去一切都已经配置妥当了，但是还差两个配置。这两个配置，同学们应该是只知其一不知其二。什么意思呢？其中一个配置，大家应该很容易就能猜到是我们 rabbit MQ 的连接字符串，对不对？那剩下的一个配置，那也就是我们说的不知其二中的其二，那待会我再来揭晓，咱先把 rabmq 的配置给加上，我选择依然从康菲格 bus server 这里把 rabmq 的连接字符串 copy 过来，我这里 copy 一下。大家记住是在 spring 节点下的，不要放错地方了。好，在这里把它添加过来。 OK 这样 client 和 server 就会连接到同一个 rab MQ instance 上。


OK 咱接下来要说那个大家不知道的配置，同学们还记得咱前面提到过，在 pom 文件当中，如果你想使用 Kafka 的话，那需要加入一个新的 dependency 叫 bus Kafka 那在某些项目当中，有可能你既使用了 rabi MQ 也使用了卡夫卡。那这两个 dependency 同时存在的情况下，咱要对巴斯做一些额外的配置才能让它生效。因为为什么呢？那咱不妨以身试法一番。怎么说？把这个 dependency 给它打开。然后尝试启动这个项目，看看它会出什么幺蛾子，直接点击 run 项目面板弹出来。好，看到 spring 成功一半。好他开始继续加载 fetching config from server 开始尝试拉取配置文件了。但是在这个过程中平地一声惊雷怎么说？好像报错了，然后项目没有启动起来，出师未捷身先死。哇，我们来看一下这个死因何在。好定格在这里。他这里报错是说有一个 bin 没有加载起来，叫 output binding life cycle 这个 bin 没有加载。 OK 那它的原因是什么呢？你看它的报错信息也非常明确。


the error message saying that a default bunder has been requested but there is more than one binder available for for this channel 所以他这边提示信息给的很明确了，我要使用一个 default 的 banner 但是在这个上下文中有两个 banner 都是可用的，分别是 rabbit 和 Kafka 那就是咱前面引入的两个 dependency 了。所以它的关键在这一句，要让大家怎么样 set up 一个 default bend 一个默认的 banner 来供他使用。否则的话这个 channel 他就不知道该加载 rab MQ 还是使用卡夫卡。


OK 那咱这里就给他指定一个 banner 好了，怎么指定找到 boot strap 文件在 cloud 下面，另起一行和这个 config 保持同级然后写 stream 其实 stream 是另外一个组件了它并不是 bus 也不是 config 而是 spring cloudstream 是一个独立的组件。只不过咱的 bus 在底层实际上是引用了 stream 来完成和消息中间件的对接。



那所以咱这里给 stream 要配置一个什么呢？ Default bonder. OK 那它的值就是 rabbit 同学们记着，如果咱引入了多个班的，这里一定要给 stream 设置一个 default 班的，否则它是启动不起来的。

```java
spring:
  application:
    name: config-bus-client
  rabbitmq:
    host: 172.16.136.223
    #    host: 172.16.136.226  两个都可以用
    port: 5672
    username: admin
    password: 123456
  cloud:
    stream:
      default-binder: rabbit
    config:
      name: config-consumer
#      uri: http://localhost:60000
      discovery:
        enabled: true
        service-id: config-bus-server
      profile: prod
      label: master


server:
  port: 61001


myWords: ${words}  # words 是github上的属性


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

那如果咱们并没有多个引用，咱只使用了 rab MQ 把卡夫卡的引用直接给他注释掉了。
那这种情况下还需要 default banner 吗？那其实就不需要了，这只是一个扩展的小知识点，让大家对 bus 和 stream 的 channel 加载有这么一个印象。 OK 障碍已经扫除了，咱这次可以正儿八经的把这个项目启动起来了。好，我们现在启动一个 config bus client 紧接着我们不是要做批量的推送消息变更吗？那我这里把端口号给他改。那么一下，把六万零一千零一改成61,002，然后再启动一个 instance 好把它跑起来。现在咱就有两个 client 节点了。那我看到前一个 client 节点已经是处于 start 的状态了。 OK 我们把它的 log 清空一下，第二个节点也正在启动当中。好，这里看到他正在拉取配置信息，然后到这里也启动起来了。我们把 log 都清空，现在我们做什么呢？转移到 POS 曼当中。我先来调用一下 61,001 这个 POD 下的动态属性。好，我们把请求发送到 refresh ctrl 的下面的 words 方法中，好发送一个。那看到它的返回值是 god bless you and me 再看看 1002 这个节点上发送一下。好是一样的，也是 god bless you and me 接下来我们要到浏览器里面，把这个属性值给它改掉。


好我们点击编辑 god bless you and me 改成 god bless you 逗号 my darlingok 然后把它提交一下。
Keep it my darling.


好，那接下来再回到 POS 曼当中。那目前来说这两个节点的属性依然是嘎布莱斯 UME 咱要开始触发刷新了怎么触发？跟前面 config 章节中的姿势可不一样了，我们换个什么姿势呢？我这里已经提前创建好了一个 host 曼的链接，那他的请求发送到哪里呢？发送到端口为 60,002 的机器上。这个就是咱创建的 config bus server 也就是配置中心。那它后面的路径是 accurator 斜杠 buzz refresh 它的 HDD 并 method 是 postok 我们直接点击散的，看看会有什么事情发生。好，他会花相当长的一段时间来好吧，太不给面子了，这么快就返回了，只能说我机器性能好棒。那他这里返回的 status 是 204 no content 这可不是错误，这说明批量刷新动作已经完成了，那咱再回到前面的 client 上面，我再来调用一把，看看它的属性是不是已经被更改了。
我发送 send 同学们看到吗？这里已经更改成 god bless you my darling 那换一个节点，换成1001，这个节点再发送一下。依然是 god bless you my darlingok bus 推送圆满成功。同学们以为到这里故事就结束了吗？其实还没有 84 推送，还有第三种姿势，不信我们来看。回到浏览器里面，咱再点击一下 edit 把这个 god bless you my darling 改成 my baby 反正都是肉麻情话了，直接提交到 master 里面。好，这里文件已经编辑好了，咱再回到 postman 里。


刚才说的还有一种姿势是什么姿势呢？大家看到，咱这里推送的目标服务器是谁？是 config server bus 是配置中心对不对？假如我这个请求不推送到配置中心，我推送到其中的一个 client 节点可不可以？我们试一下，把端口改成了61,001，它是 config bus client 中的一个节点。好，我们点击 send 好，结果也返回了。那这个推送会生效吗？我们来看一下。好了，现在从 61,001 获取属性，看看它变成了。果然 god bless you my baby 那 60,002 是不是也依然变动了呢？ OK 那这里可以看到，1001和 1002 这两台 client 的全部被刷新过了，所以证明了咱的刷新请求不管是发送到配置中心还是发送到配置中心下面的节点，它都会完美触发刷新动作。


OK 那到这里，本节的 demo 就快要结束了，我来跟大家总结一下。在这个环节当中，我们配置了一个 config bus client 连接到 rabbit MQ 从 rabbit MQ 当中消费这个广播消息来进行节点的刷新。这里咱穿插讲到了一个小的知识点，就是关于 stream default banner 的配置。假如我们在 dependency 同时引用了 rabbit MQ 还有卡夫卡组件。那么在这里要给 stream 指定一个 default bend 否则我们 bus 启动的时候会报错。然后我们启动了多个 client 节点，模拟了一个小集群。然后我们在 postman 当中向配置管理中心发送了批量刷新请求。同时我们也尝试了另外一种方式，向配置中心下面挂载的节点发送批量刷新请求。这两种方式都可以触发整个集群的批量刷新。也就是说只要发送一次请求就可以刷新整个集群。这就是我要跟大家展示的总线式架构的配置管理中心同样的属性。批量刷新也是 bus 组件最核心的一个功能，也是它应用最广泛的一个点。


OK 到这里，整个 demo 环节就结束了。在下一节当中，我们将要进行源码部分的学习，看一看 bus refresh 背后都发生了哪些事情。同学们，那我们下期再见。




