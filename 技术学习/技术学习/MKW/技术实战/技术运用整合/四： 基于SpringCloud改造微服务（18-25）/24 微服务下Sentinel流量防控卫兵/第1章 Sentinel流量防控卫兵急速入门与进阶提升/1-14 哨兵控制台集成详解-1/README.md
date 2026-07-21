---
title: 1-14 哨兵控制台集成详解-1
---

# 1-14 哨兵控制台集成详解-1

[image](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/9b55349f-d9df-4ee6-bd90-4133a7aa0115/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46656PIXBPI%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T225835Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQD44lfnPGXrwlGFJVP5iEg%2BXNKPM1sOqtgI49KNxbggxgIgKTOBkmTtGI6jqU4Huz8tkDC3oNK%2FNpXVekClSp3YuCkqiAQIxv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDJMBxnz%2FCj24Yy8YcCrcAyzjT0oCo4YmFn%2BHo4TS%2B0GkYnwsjt4lM4d5xVtIhyjZ3zX0w8FjE8xLxUM5HE7Pyevpi0bixdkr3%2FTbtkUR9rMlePYnIZHL251gdi6NdCj5WwKML4aNooU%2FLR5ufgTa61UDc74DA2V0XaUKXc2WpxSrP%2BMUEKtlcLBGgsUjiiS75tR1g24KAq5PCtIkyuFRX9NPMfvvtcHsMxzT7%2F8l%2B0eyRxSz9xrWh0XXpy7j7yDpIYjXSwjx8I32yUdgOZpuT2HkUb4cyKg2%2Bbwr9R4KN1hWxMnZ6DXiL8M41%2B4THBcNcuAoKKbyFLbvljvyMRgUb1lDNCE8h%2BFtSQ1MyhUS3kxCSma759yXISOMNV6gx0ZLyrQ6BXel%2FT08AMI%2BlGmIo721DJPlRgJ8RbxLRTuClS9uwlzG46%2BhjhTAV9o7Bb63hPTf%2FV89dtp0R0s0WFUua18%2BHIpiOznRthTsii%2BnlTMD68eE%2BRotOC3aaD1PIBslxf4CWetoSwSfWiZRRQ4FXnOW%2FtLBRbWlzG4%2F0VhE%2BmClHhinodFy93m10yWKCdHx569esBbe%2B82oJNX8kj2ntoY%2B6WnOt3k%2Fdh8SjL6ltC6riWp5o6mVaHbHQ8IjcTH39Vb%2BcLQjjNREh%2BQ1MJm3%2F9IGOqUB0FZ6N3iZi62S8aDfhWHB40EZy2LUPtZso1EvoPc3YFv%2FQojnx1%2BJux%2BOP44zdUy5PP21QNgbNEHoBZ0ganz0l4hZkSEex8t1H4nRZ82axnaXZKmeuNmMdlJrLIXqnRaOsy3fKJFace5JY8nxGSaHNj7JnbcRj3NGZBb0RFxa9qQ5A%2BL%2FllpNYSYEZi%2F3gRCA6y%2FT03E%2Bym%2BqHu8NdPPjIFZkYgas&X-Amz-Signature=7573010c7a01d35d0c3eac068b36e8d2e58671920f21d40feb75bd7cf369b4d4&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

这节课我们来学习 dashboard 哨兵的这个控制台。那在这里首先我们来看一下这个文档控台应该怎么去学习和使用。控制台，它是提供了一个轻量级的开源的控台。那主要作用就是为了健康情况的管理以及监控，包括单机和集群，最重要的就是规则管理以及规则推送的功能。另外鉴权在生产环境中也是必不可少的。那在 sentence 里边也会有对应的直线。那在这里边我们使用的肯定是 sentence 他自己这个源码包里面的 dashboard 那当然在阿里云上他也提供这个 ahas 的这个三次控制台。如果你实际的工作中你是阿里云服务的话，那你也可以去用这个阿里云的控制台，这可能作用会更强大一些。然后下面来说一说这个森特斯控制台基本的功能，比如说可以收集客户端的一些发送的心跳包，然后用于判断这个客户端的机器是否在线。


第二点就是做监控，它可以通过这个 sentence 暴露出来的这个监控 API 定区的去拉取和聚合一些监控信息，最终可以实现这个秒级的实时的应用监控。后面会跟大家演示一下，然后以及这个规则管理。那这个规则管理其实是最重要的。最后就是鉴权，大体上它有这么几个功能。然后我们来看一看控制台怎么去做。你可以去点击这个 release 界面去下载最新版本的炸包，当然你也可以从这个源码包自己去构建。那我们当然是选择源码包是共建，然后共建使用的主要特点是启动的时候注意你的 gk 一定是 1.8 版本或者是以上。然后控制台启动命令是 Java 杠 D server point 然后这是8080，当然这个端口号你自己去指定就好了。然后 CSP sentence 然后 dashboard server 你自己的控制台 IP 端口以及 dashboard 它的这个 project name 就是我们叫三次 dashboard 可以了，然后最后把这个价包提起来就好了，这是它对应的一个控制台所需要配置的参数。


杠 D 就是优先级最高的，然后再往下看，它这里边做了一个说明。然后他说从我们 sentence 1.6 版本之后，他多了一个登录的功能。 1.5 之前是没有登录界面的 1.6 版本，他终于画了一个登录界面，写了一个简单的验证用户的密码都是sentence。


Ok. 然后可以参考鉴权模块文档中的这个用户名密码配置。比如说当你配置了用户密码，你的客户端想连接 dashboard 的时候，你也要配置对应的用户密码，要配置对，这是肯定的。然后我们看一看客户端如何接入我们的客户台。首先第一点就是说你要引入这个炸包就是 sentence 然后叫做 transport single App 也就是说在我们实际进行通信的时候，它其实是采用了这个包进行一个数据传输的。说白了就是 HTTP 方式。


好了，然后再往下看启动参数在控制台的 client 端， client 需要加两个参数，一个是你的 dashboard 是 server 是哪？还有一个是，你的 API point 是什么，默认是 8719 这个端口。从 163 版本，它也支持网关，你可以去做自动注册网关，可以去做这个网关规则和 IP 分组了，这是 1.6 版本的新特性。然后这里边你也可以修改 gvm 参数，可以得到相同的结果就是你可以点到这个启动配置箱里去看一看。然后这下面的事情就是处罚的这个控制台的界面了，在这里我就不领着小伙伴们一个一个去读了，因为一会我们马上就开始去做这个事情。最后在这一块鉴权这块我再特殊提一下，就是说你要是 dashboard 的这个用户名跟密码，你要配的不是默认的话，要注意你在连的时候也要加上这样的东西。如果你说这两项都省略，默认的用户密码都是 sentence 如果你配好了你自己的用户能密码，那你最好这两项在 K 三端接入的时候也都需要配置。


当然它还有另外一个配置叫做 so late session turn out 超时时间用于 spring boot 服务端 session 的过去时间。比如说 7200 秒表示 60m 表示 60 分钟，默认是 30 分钟。 OK 同样，你也可以在 spring boot practice 文件里边去进行配置。 OK 那文档说得非常非常的详细。那我们就按照这个步骤一点点来。首先我们打开我们自己的这个 dashboard 源码，找到 163 的 dashboard 在这里 163 的 dashboard 同学们请看它就是一个 spring boot 工程。我们来看一看它的这个最开始它叫做 dashboard application 那 dashboard application 就是一个普通的 spring boot 工程，然后我们直接启动就好了。


当然在启动之前，我们看一看它最关键的 practice 配置。 practice 点开我们看到什么呢？这个 practice 里边有 author 对不对？默认用户密码都是 sentence 我们可以不用去关注。好了关于日志输出的目录日志的这个 pattern 在这里。那现在我们其实直接就可以启动。当然在启动之前我们右键 ys Java application 或者 spring boot 都可以 application 但是我在启动之前我要加一个配置项，比如说老师，现在在这里 dashboard application 对于这个启动的时候加一些配置项，刚才已经分配好了，多口号 dashboard 服务以及 dashboard 这个 project name 对吧，我们都有了之后我们去 apply 然后把它 run 起来。启动了之后，我们来看一看它对应的这个日志输出。如果你看到它里边 control 涨生效了，就说明它这个下面加载的这些服务列表这些 UL 都已经加载好了，就相当于映射已经搞定了。


handler mapping 对不对？这就是我们 spring VC 的， request mapping handler magic OK 好了，你看到这个就证明你的 sentence 已经启动成功了，就对应的 dashboard 端口号是8080，然后就可以访问了。有的时候可能你直接启动的时候你不帮你加载这鞋，那你就多启动几次好了，在这里我们的该事报的控制台启动。


好了，那我们通过浏览器去访问一下，在这里我们直接敲 logo host 2080 登口号，然后回车就可以了。这里边它首先让你输入用户名密码，这是 160 版本带的sentence 。好了，然后点登录。 OK 然后密码保存。好了，同学们请看。现在我已经看到了这个 dashboard 控制台，但是这个 dashboard 控制台它里边没有连任何科普段，所以说我只能看到我自己的 dashboard 就是现在这个展示出来这个界面就是我自己的节点本身，这实时的请求数它都会有 QPS 通过什么的。这个就是实时监控，它只是统计前一分钟的数据。然后它这个绿色的表示通过的。然后如果有蓝色的线就表示拒绝的。你看其实我把鼠标移到这，你可以看到通过是1，然后拒绝是 0 蓝色的这种是拒绝。当然它的时间总会在变。然后这边有对应的这个图表，你会看到当前这个时间是不是通过了多少个，拒绝了多少次响应时间，rt是什么。

```shell
<dependencies>

    <dependency>
        <groupId>org.springframework.boot</groupId>
        <artifactId>spring-boot-starter-web</artifactId>
    </dependency>

    <dependency>
        <groupId>org.springframework.boot</groupId>
        <artifactId>spring-boot-starter-test</artifactId>
    </dependency>


    <dependency>
        <groupId>com.alibaba.csp</groupId>
        <artifactId>sentinel-core</artifactId>
        <version>1.8.6</version>
    </dependency>
    <dependency>
        <groupId>com.alibaba.csp</groupId>
        <artifactId>sentinel-transport-simple-http</artifactId>
        <version>1.8.6</version>
    </dependency>
</dependencies>
```


然后下面也是具体的这个 metrics 这有一个叫做 query top resource metric 的 JSON 就它可以去统计 top 10 或者 top 几等等。要说它这个控制台在我们 1.5 点X ，它还不是特别全的，但是在我们的这个 1.6 的时候，它的功能逐渐就强大了。

[image](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/1a9825bf-5766-4a8f-a9cd-12e2f8784cf8/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46656PIXBPI%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T225835Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQD44lfnPGXrwlGFJVP5iEg%2BXNKPM1sOqtgI49KNxbggxgIgKTOBkmTtGI6jqU4Huz8tkDC3oNK%2FNpXVekClSp3YuCkqiAQIxv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDJMBxnz%2FCj24Yy8YcCrcAyzjT0oCo4YmFn%2BHo4TS%2B0GkYnwsjt4lM4d5xVtIhyjZ3zX0w8FjE8xLxUM5HE7Pyevpi0bixdkr3%2FTbtkUR9rMlePYnIZHL251gdi6NdCj5WwKML4aNooU%2FLR5ufgTa61UDc74DA2V0XaUKXc2WpxSrP%2BMUEKtlcLBGgsUjiiS75tR1g24KAq5PCtIkyuFRX9NPMfvvtcHsMxzT7%2F8l%2B0eyRxSz9xrWh0XXpy7j7yDpIYjXSwjx8I32yUdgOZpuT2HkUb4cyKg2%2Bbwr9R4KN1hWxMnZ6DXiL8M41%2B4THBcNcuAoKKbyFLbvljvyMRgUb1lDNCE8h%2BFtSQ1MyhUS3kxCSma759yXISOMNV6gx0ZLyrQ6BXel%2FT08AMI%2BlGmIo721DJPlRgJ8RbxLRTuClS9uwlzG46%2BhjhTAV9o7Bb63hPTf%2FV89dtp0R0s0WFUua18%2BHIpiOznRthTsii%2BnlTMD68eE%2BRotOC3aaD1PIBslxf4CWetoSwSfWiZRRQ4FXnOW%2FtLBRbWlzG4%2F0VhE%2BmClHhinodFy93m10yWKCdHx569esBbe%2B82oJNX8kj2ntoY%2B6WnOt3k%2Fdh8SjL6ltC6riWp5o6mVaHbHQ8IjcTH39Vb%2BcLQjjNREh%2BQ1MJm3%2F9IGOqUB0FZ6N3iZi62S8aDfhWHB40EZy2LUPtZso1EvoPc3YFv%2FQojnx1%2BJux%2BOP44zdUy5PP21QNgbNEHoBZ0ganz0l4hZkSEex8t1H4nRZ82axnaXZKmeuNmMdlJrLIXqnRaOsy3fKJFace5JY8nxGSaHNj7JnbcRj3NGZBb0RFxa9qQ5A%2BL%2FllpNYSYEZi%2F3gRCA6y%2FT03E%2Bym%2BqHu8NdPPjIFZkYgas&X-Amz-Signature=dd753f7b0f6abf53511c84beabfc20e44e84d462800b5a714d7a657cde832993&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

```shell
java -Dserver.port=8080  -Dcsp.sentinel.dashboard.server=localhost:8080  -Dproject.name=sentinel-dashboard  -jar target/sentinel-dashboard.jar

http://192.168.13.204:8080/#/dashboard/identity/sentinel-dashboard

sentinel-demo-test工程内部也是可以直接启动里面的 jar 包

```

[image](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/889999ee-9205-485a-8484-fbd1674034f4/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46656PIXBPI%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T225835Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQD44lfnPGXrwlGFJVP5iEg%2BXNKPM1sOqtgI49KNxbggxgIgKTOBkmTtGI6jqU4Huz8tkDC3oNK%2FNpXVekClSp3YuCkqiAQIxv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDJMBxnz%2FCj24Yy8YcCrcAyzjT0oCo4YmFn%2BHo4TS%2B0GkYnwsjt4lM4d5xVtIhyjZ3zX0w8FjE8xLxUM5HE7Pyevpi0bixdkr3%2FTbtkUR9rMlePYnIZHL251gdi6NdCj5WwKML4aNooU%2FLR5ufgTa61UDc74DA2V0XaUKXc2WpxSrP%2BMUEKtlcLBGgsUjiiS75tR1g24KAq5PCtIkyuFRX9NPMfvvtcHsMxzT7%2F8l%2B0eyRxSz9xrWh0XXpy7j7yDpIYjXSwjx8I32yUdgOZpuT2HkUb4cyKg2%2Bbwr9R4KN1hWxMnZ6DXiL8M41%2B4THBcNcuAoKKbyFLbvljvyMRgUb1lDNCE8h%2BFtSQ1MyhUS3kxCSma759yXISOMNV6gx0ZLyrQ6BXel%2FT08AMI%2BlGmIo721DJPlRgJ8RbxLRTuClS9uwlzG46%2BhjhTAV9o7Bb63hPTf%2FV89dtp0R0s0WFUua18%2BHIpiOznRthTsii%2BnlTMD68eE%2BRotOC3aaD1PIBslxf4CWetoSwSfWiZRRQ4FXnOW%2FtLBRbWlzG4%2F0VhE%2BmClHhinodFy93m10yWKCdHx569esBbe%2B82oJNX8kj2ntoY%2B6WnOt3k%2Fdh8SjL6ltC6riWp5o6mVaHbHQ8IjcTH39Vb%2BcLQjjNREh%2BQ1MJm3%2F9IGOqUB0FZ6N3iZi62S8aDfhWHB40EZy2LUPtZso1EvoPc3YFv%2FQojnx1%2BJux%2BOP44zdUy5PP21QNgbNEHoBZ0ganz0l4hZkSEex8t1H4nRZ82axnaXZKmeuNmMdlJrLIXqnRaOsy3fKJFace5JY8nxGSaHNj7JnbcRj3NGZBb0RFxa9qQ5A%2BL%2FllpNYSYEZi%2F3gRCA6y%2FT03E%2Bym%2BqHu8NdPPjIFZkYgas&X-Amz-Signature=d423ea597f8a5b8b9d883a4f031815f7ef87a185cc5ae1573bb266f6d29474c4&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

然后触点链路触点链路，你看我这个触点链路很多是不是这些触点链路你不用关注，因为这些资质让你也不需要去管它。后面我们去集成的时候你就需要管它。比如说这些流控规则、降级规则、热点、系统自适应、授权，急需流控，包括急需列表。 OK 那这些我们现在只是识别我们当前这台服务器自己本身。 OK 你会看到。那现在我们控制台真的是启动起来了以后，接下来我们要做什么事情？这控台主要是干什么？就是我们自己的 Java 应用要接哨兵对不对？要接哨兵，要给他去配置一些流控策略。然后我想通过控制台去进行一个可视化的监控，做一个可视化的可动态配置的规则的这一系列的东西。所以说我们必须要集成控制台，我们的应用服务也要集成控制台。好了，在这里废话不多说，我们先自己做一个应用，我还是以最开始的那个 demo 我们来找到我们最开始的这个 sentence 杠 demo 杠 test 那这个工程老师简单的把它改造了一下，然后剩下的我们自己去实现代码。



来首先看一下我们 pom pom 文件很简单，目前我们用的是 215 这个 spring boot 然后引入了我们的这个 web 跟这个 test 其实我刚才都引入了一个包，就是我们的下面这个 sentence transport 然后 single HTTP 这个包这是必须要有的，版本都是要对应上 163 号包肯定是有。现在我引入了这两个包，然后加上 spring 的最基础 spring boot 的包对吧，其他的没有。 Ok. 那这样的话，我们当前这个服务的端口我设置的是8001，因为 8080 已经被戴世博的占用了。 Ok. 好了，其他的需要做什么呢？其他的也需要做一些相关的设施。比如说我们在运行起来的同时，我们要 one as Java application 我们先做一下配置，做哪些配置呢？注意，现在我们用的是 Java application 我先把它运行起来 run 一下，不运行的话它可能看不到。 8001 启动了是不是。然后启动了之后我可以把这个关掉了，我现在就把它关掉，控制台还保留的。然后这回我去 run ADS config 因为这样的话我就有 application 了，是不是 application 之后我就可以改这个参数了，来看一看我们需要改哪些参数，看他的官网文档。


首先我们接入控制台的时候你找到引这个包没问题，然后修改配置。第一个配置，然后第二个配置 API point 第一个配置我们先粘过来是 local host 冒号，8080是吧，我们直接写好 local house 冒号，就是我们的8080。然后下一个配置是什么呢？我们来看一下下一个配置，就是我们的杠 D 它的这个 API point 默认是什么呢？是8719。好，这两个都需要有 8769 搞定了，这两个之后我 apply 一下，然后我先不关注其他的，我们先直接 close 掉。


好了，现在你的应用服务现在为止已经与控制台就是相当于建立了关系了，你可以认为是建立的关系了。当然其实你启动也可以能看到，我们来试一下我们来 Java application ，因为我刚才是在 Java application 里配置好了，我的服务已经起来了，8001对吧？ 8001 也起了。然后现在我再来刷一下我的控制台，我们直接回过来，2080。



如果说现在你没看到任何数据的话，配置的有问题，其实我们可以看对应的文档。你看控制台配置，我们看一下这个 sentence call 它的配置项有哪些，你看还有这么多配置项。那其实我们比较关注的是什么呢？比如说当前我的 project name 是什么？然后我的应用是什么？我其实可以都加上。那我先不用太着急，我们先比如说写个小例子，看看行不行。好我们来一点点写。这个它其实有一个问题，就是它的一个延迟加载的问题，所以说我们必须得给小伙伴把这个说清楚。


好。首先我们来看一看他这个我建立一个 web 包，然后我写一个简单的 controller 比如说叫做 index controller index controller 然后在这里我们写 rest controller 然后在这里边我们去加上我们的这个 request mapping request mapping 在这里边我就写高尔波罗吧。波罗好，然后写一个方法叫做 public 返回值时间，然后叫做波罗流控。对吧。好在这里面怎么去写？比如说返回值是一个 polo 好，写完了。但是在这之前我说老师现在我应该怎么去集成我的哨兵，很简单，你想怎么去做，就把之前 hello world 的代码 copy 过来都可以没问题，但是你要 copy 过来有意义的地方。你看我之前已经把它注释了，我现在我要把哪个地方 copy 过来呢？我说我要把 try catch 的地方包括规则 copy 过来，看我们线下我把这个地方 copy 过来。然后把这个东西就是放开，然后 control shift 加 O 把我们对应的该导的包都导进来。然后这里边我就往出死肉。好同学们请看现在我已经有了一个 risk control 了，然后他是 follow 我访问这个方法的时候他会执行这个，但是这个规则现在目前还没有。你看 hello world 的。

```shell
package com.bfxy.test;

import com.alibaba.csp.sentinel.slots.block.RuleConstant;
import com.alibaba.csp.sentinel.slots.block.flow.FlowRule;
import com.alibaba.csp.sentinel.slots.block.flow.FlowRuleManager;
import org.springframework.boot.SpringApplication;
import org.springframework.boot.autoconfigure.SpringBootApplication;

import java.util.ArrayList;
import java.util.List;

/**
 * <h1></h1>
 */
@SpringBootApplication
public class ApplicationSentinel {

    public static void initFlowRules() {
        List<FlowRule> ruleList = new ArrayList<>();
        FlowRule rule = new FlowRule();
        // 注意：我们的规则一定要绑定对应的资源上， 通过资源名称进行绑定
        rule.setResource("SentinelHelloWorld");
        rule.setGrade(RuleConstant.FLOW_GRADE_QPS);
        rule.setCount(20);
        ruleList.add(rule);
        // 规则管理器
        FlowRuleManager.loadRules(ruleList);
    }

    public static void main(String[] args) {
        SpringApplication.run(ApplicationSentinel.class, args);
        initFlowRules();
        System.out.println("规则加载完毕");
    }
}
```


那这规则从哪加载？我们之前是在静态的代码块只加载了一次。那其实你也可以这样去做。你比如说你把这个方法放到应用服务启动的时候，然后加载一下规则，这也可以。没问题。比如说我就放到这里，然后我最后去 init 一下规则。没问题。好在我的应用服务启动的时候，启动之后，然后我去加载一下规则，然后打印一句话，规则加载完毕。
好，同学们请看现在我的 test 应用服务已经有一个最简单的 controller 了，叫做 index controller 就一个 follow 的一个 URL 对外暴露。然后我现在也有了对应的这个要访问的这个属于之前 hello world 的这个代码，然后我就再次把它。

```shell
package com.bfxy.test.controller;

import com.alibaba.csp.sentinel.Entry;
import com.alibaba.csp.sentinel.SphU;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RestController;

/**
 * <h1></h1>
 */
@RestController
public class IndexController {

    @RequestMapping("/flow")
    public String flow() throws InterruptedException {

        // 0: 引入依赖==============>使用 Sentinel 步骤

        // 初始话规则

        // 1: 定义资源
        while (true) {
            Entry entry = null;
            try {
                // 2.1 定义资源名称
                entry = SphU.entry("SentinelHelloWorld");

                // 2.2 执行职员逻辑代码
                System.out.println("SentinelHelloWorld: 访问数据库");
                System.out.println("SentinelHelloWorld: 访问远程 redis");
                System.out.println("SentinelHelloWorld: 数据库持久化操作");

                Thread.sleep(20);

            } catch (Exception e) {
                System.out.println("要访问的资源被流控了, 执行流控逻辑");
            } finally {
                if (entry != null) {
                    entry.exit();
                }
            }
            return "flow";
        }
        // 2: 定义规则

        // 3: 查看结果

        // 4：控制台

    }

}
```


这回启动的时候我来看一下配置一下，我把该配的都配上，比如说怎么到这里了，就是这是以 spring boot 的工程去启动。然后我可以以 Java application 的方式启动去改这个配置，也可以以 sprint boot 的工厂去启动。当然你自己要注意你到底是在哪个启动的，我在这里边，我这里面也有我的配置项对吧，我的 dashboard 的 server 的 IP 端口。然后这个是我自己应用名称应用服务名称我叫 sentence 杠 demo 杠 test 那我也可以这样去写。（也可以通过配置文件的方式配置，但是优先级低于 JVM 参数

[https://sentinelguard.io/zh-cn/docs/startup-configuration.html](https://sentinelguard.io/zh-cn/docs/startup-configuration.html)

）

```shell

=====================官方文档====================================
-Dcsp.sentinel.dashboard.server=localhost:8080 
-Dcsp.sentinel.api.port=8001

3.2 配置启动参数
启动时加入 JVM 参数 -Dcsp.sentinel.dashboard.server=consoleIp:port 指定控制台地址和端口。若启动多个应用，则需要通过 -Dcsp.sentinel.api.port=xxxx 指定客户端监控 API 的端口（默认是 8719）。

除了修改 JVM 参数，也可以通过配置文件取得同样的效果。更详细的信息可以参考 启动配置项。
```

[image](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/89816785-e15d-4e74-9845-143ce35af3a5/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46656PIXBPI%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T225835Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQD44lfnPGXrwlGFJVP5iEg%2BXNKPM1sOqtgI49KNxbggxgIgKTOBkmTtGI6jqU4Huz8tkDC3oNK%2FNpXVekClSp3YuCkqiAQIxv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDJMBxnz%2FCj24Yy8YcCrcAyzjT0oCo4YmFn%2BHo4TS%2B0GkYnwsjt4lM4d5xVtIhyjZ3zX0w8FjE8xLxUM5HE7Pyevpi0bixdkr3%2FTbtkUR9rMlePYnIZHL251gdi6NdCj5WwKML4aNooU%2FLR5ufgTa61UDc74DA2V0XaUKXc2WpxSrP%2BMUEKtlcLBGgsUjiiS75tR1g24KAq5PCtIkyuFRX9NPMfvvtcHsMxzT7%2F8l%2B0eyRxSz9xrWh0XXpy7j7yDpIYjXSwjx8I32yUdgOZpuT2HkUb4cyKg2%2Bbwr9R4KN1hWxMnZ6DXiL8M41%2B4THBcNcuAoKKbyFLbvljvyMRgUb1lDNCE8h%2BFtSQ1MyhUS3kxCSma759yXISOMNV6gx0ZLyrQ6BXel%2FT08AMI%2BlGmIo721DJPlRgJ8RbxLRTuClS9uwlzG46%2BhjhTAV9o7Bb63hPTf%2FV89dtp0R0s0WFUua18%2BHIpiOznRthTsii%2BnlTMD68eE%2BRotOC3aaD1PIBslxf4CWetoSwSfWiZRRQ4FXnOW%2FtLBRbWlzG4%2F0VhE%2BmClHhinodFy93m10yWKCdHx569esBbe%2B82oJNX8kj2ntoY%2B6WnOt3k%2Fdh8SjL6ltC6riWp5o6mVaHbHQ8IjcTH39Vb%2BcLQjjNREh%2BQ1MJm3%2F9IGOqUB0FZ6N3iZi62S8aDfhWHB40EZy2LUPtZso1EvoPc3YFv%2FQojnx1%2BJux%2BOP44zdUy5PP21QNgbNEHoBZ0ganz0l4hZkSEex8t1H4nRZ82axnaXZKmeuNmMdlJrLIXqnRaOsy3fKJFace5JY8nxGSaHNj7JnbcRj3NGZBb0RFxa9qQ5A%2BL%2FllpNYSYEZi%2F3gRCA6y%2FT03E%2Bym%2BqHu8NdPPjIFZkYgas&X-Amz-Signature=c96096677723584e03d3dc3f494633596a4aa1f20fa8894b97d2279fcf4a0069&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

杠 demo 杠 test 可以吧，然后以及对应的监听端口是不是 8719 我都可以。写完了之后我 apply 然后再点 run 去运行起来，这个服务是8001。你看规则加载完毕看见了吧，它都启动了，然后规则也加载完了。


规则加载完了之后，我们现在你要去刷的话，其实你不一定能刷出来，还是刚才那个问题你刷出来你只能看到我自己的 dashboard 怎么办？现在我们去访问一下 HTTP 冒号杠 local house 这回就是 8001 了，然后访问 solo 会说访问 follow 他给我返回了一个 follow 证明什么？证明我们刚才的这个 test demo 的一个 URL 就是我们看到的 index controller 已经访问成功了，对不对？已经访问成功了。那开始在我们 application 启动的时候，他就调了 init follow ruler 就把这个规则加载进去了。那现在他也做了一件事情干什么？他做的事情就是已经访问了这个资源了，就是我调这个 API 他肯定进到这里边，然后打印了这三句话，看见了吧。


我的数据是那这样的话，我们再去看一下这双写，同学们一起看你，这回你才能看到你自己的这什么 sentence 杠 demo 杠 test 所以说你千万你在学习的时候，你要注意，你最开始启动起来的时候，你最开始你应用服务启动起来跟 dashboard 跟控制台连的时候，你如果不访问，你是啥结果都看不到的，你的工作台你是看不到这个项的。有的时候这个官方文档说的不是那么特别详细。那这个是一个小的坑，只有你第一次请求访问了之后，它才相当于把规则加载到，但是标准上它是一个懒加载的机制。然后你看这个戴诗帽子跟这个 demo 这其实就是我们自己的服务看见了吗？我的机器列表，我点一下当前我的机器列表，我当前就一个服务器，所以说我机器列表是一个。然后我们看这个实时的监控，实时监控你啥也没有，你怎么样能让它变得有点东西。很简单。

[image](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/d2ea24d0-9f41-445d-a8b2-7506dc5bebbf/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46656PIXBPI%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T225835Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQD44lfnPGXrwlGFJVP5iEg%2BXNKPM1sOqtgI49KNxbggxgIgKTOBkmTtGI6jqU4Huz8tkDC3oNK%2FNpXVekClSp3YuCkqiAQIxv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDJMBxnz%2FCj24Yy8YcCrcAyzjT0oCo4YmFn%2BHo4TS%2B0GkYnwsjt4lM4d5xVtIhyjZ3zX0w8FjE8xLxUM5HE7Pyevpi0bixdkr3%2FTbtkUR9rMlePYnIZHL251gdi6NdCj5WwKML4aNooU%2FLR5ufgTa61UDc74DA2V0XaUKXc2WpxSrP%2BMUEKtlcLBGgsUjiiS75tR1g24KAq5PCtIkyuFRX9NPMfvvtcHsMxzT7%2F8l%2B0eyRxSz9xrWh0XXpy7j7yDpIYjXSwjx8I32yUdgOZpuT2HkUb4cyKg2%2Bbwr9R4KN1hWxMnZ6DXiL8M41%2B4THBcNcuAoKKbyFLbvljvyMRgUb1lDNCE8h%2BFtSQ1MyhUS3kxCSma759yXISOMNV6gx0ZLyrQ6BXel%2FT08AMI%2BlGmIo721DJPlRgJ8RbxLRTuClS9uwlzG46%2BhjhTAV9o7Bb63hPTf%2FV89dtp0R0s0WFUua18%2BHIpiOznRthTsii%2BnlTMD68eE%2BRotOC3aaD1PIBslxf4CWetoSwSfWiZRRQ4FXnOW%2FtLBRbWlzG4%2F0VhE%2BmClHhinodFy93m10yWKCdHx569esBbe%2B82oJNX8kj2ntoY%2B6WnOt3k%2Fdh8SjL6ltC6riWp5o6mVaHbHQ8IjcTH39Vb%2BcLQjjNREh%2BQ1MJm3%2F9IGOqUB0FZ6N3iZi62S8aDfhWHB40EZy2LUPtZso1EvoPc3YFv%2FQojnx1%2BJux%2BOP44zdUy5PP21QNgbNEHoBZ0ganz0l4hZkSEex8t1H4nRZ82axnaXZKmeuNmMdlJrLIXqnRaOsy3fKJFace5JY8nxGSaHNj7JnbcRj3NGZBb0RFxa9qQ5A%2BL%2FllpNYSYEZi%2F3gRCA6y%2FT03E%2Bym%2BqHu8NdPPjIFZkYgas&X-Amz-Signature=cf7022d998355f780ab5c9ad9bb68e0ebb6d4fbe0026a4b1dddaef967dcbae58&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)


就这样我 fff 刷新了好多次，看见了吧，这回我再来通过请求 5 次，我再刷一次，那我再刷一下，你看每秒钟通过请求是 5 次，然后这是 5 次 3 次，刚才我刷了好多次，我再刷几次。我 f5f5 刷了好多次，我们再看我这里边就是 6 次，它只能统计你一分钟之内的实时的这个链路，然后它的资源名称叫做 hello word 是不是？然后它这里边会有一些实时的统计的看板，你会看到。然后这个粗点链路是什么呢？你看它这里边有一个叫做 sentence default context 其实我们每一个资源它都有一个负类，就是有有一个负的资源。这个负的资源是一个 style local 去做的，你不需要关注它，只是下面有一个树状的这个链路用来串起来。


它有一个子节点 hello world 这个 hello world 代表着谁，就代表刚才你的那个资源。然后你可以对这个资源做你的流控规则。比如说你可以对这个资源做一系列的流控规则，我们看一下可以做降级规则，看见了吗？这是降级规则也可以做什么呢？热点参数，包括可以做黑白名单的授权都可以去做。

[image](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/3ca385cf-9844-4b2a-9c45-8f38287783ec/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46656PIXBPI%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T225835Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQD44lfnPGXrwlGFJVP5iEg%2BXNKPM1sOqtgI49KNxbggxgIgKTOBkmTtGI6jqU4Huz8tkDC3oNK%2FNpXVekClSp3YuCkqiAQIxv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDJMBxnz%2FCj24Yy8YcCrcAyzjT0oCo4YmFn%2BHo4TS%2B0GkYnwsjt4lM4d5xVtIhyjZ3zX0w8FjE8xLxUM5HE7Pyevpi0bixdkr3%2FTbtkUR9rMlePYnIZHL251gdi6NdCj5WwKML4aNooU%2FLR5ufgTa61UDc74DA2V0XaUKXc2WpxSrP%2BMUEKtlcLBGgsUjiiS75tR1g24KAq5PCtIkyuFRX9NPMfvvtcHsMxzT7%2F8l%2B0eyRxSz9xrWh0XXpy7j7yDpIYjXSwjx8I32yUdgOZpuT2HkUb4cyKg2%2Bbwr9R4KN1hWxMnZ6DXiL8M41%2B4THBcNcuAoKKbyFLbvljvyMRgUb1lDNCE8h%2BFtSQ1MyhUS3kxCSma759yXISOMNV6gx0ZLyrQ6BXel%2FT08AMI%2BlGmIo721DJPlRgJ8RbxLRTuClS9uwlzG46%2BhjhTAV9o7Bb63hPTf%2FV89dtp0R0s0WFUua18%2BHIpiOznRthTsii%2BnlTMD68eE%2BRotOC3aaD1PIBslxf4CWetoSwSfWiZRRQ4FXnOW%2FtLBRbWlzG4%2F0VhE%2BmClHhinodFy93m10yWKCdHx569esBbe%2B82oJNX8kj2ntoY%2B6WnOt3k%2Fdh8SjL6ltC6riWp5o6mVaHbHQ8IjcTH39Vb%2BcLQjjNREh%2BQ1MJm3%2F9IGOqUB0FZ6N3iZi62S8aDfhWHB40EZy2LUPtZso1EvoPc3YFv%2FQojnx1%2BJux%2BOP44zdUy5PP21QNgbNEHoBZ0ganz0l4hZkSEex8t1H4nRZ82axnaXZKmeuNmMdlJrLIXqnRaOsy3fKJFace5JY8nxGSaHNj7JnbcRj3NGZBb0RFxa9qQ5A%2BL%2FllpNYSYEZi%2F3gRCA6y%2FT03E%2Bym%2BqHu8NdPPjIFZkYgas&X-Amz-Signature=ecf07d2ac2109abd3c88b074230fbd9e98ee177d4c82eeafff0010e6be3879dc&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

Ok.然后这个就是流控降级热点授权。那对应的流控规则是什么？现在我们默认我最开始第一次加载的时候，我的流控规则是 QPS 的方式，然后阈值是 20 单击。当然我没有其他的机器，所以说就一台机器。 OK 看到了。然后我的降级规则，现在我们还没有任何降级规则，所以说是空的热点规则没有。然后他说 sentence 版本不支持热点，因为什么不支持热点呢？其实是因为我们没有去添加这个叫做 sentence 杠 param 杠 follow control 的依赖。如果你的应用程序加上这个依赖包，他是支持热点。


OK 这是我们之前跟大家文档的时候就已经提过了的或者是你看咱们的这个 sentence 官方文档也知道了，然后系统自适应这也是没有的，然后授权也是没有的，然后集群流控都是没有的机器列表。好了，比如说我现在就把它删除可不可以没问题，我把它删除，你看我的删除没了之后相当于什么呢？相当于你之前在代码里边，在你的应用程序启动之前，你去加载的 init QQ 就已经丢失了。因为它是内存的，就是你在但是报的时候去修改，它会通过 HTTP 方式去到我们的这个克兰德发请求，然后把这个规则从 follow manager 中给它干掉。它就是这么一个逻辑。


我们先我说我还想去加一个规则，很简单，在 hello 的中之前是因为线程数我们可以去模拟并发QPS 。比如说我 QPS 最大我认为是 3 可以，就是每秒 QPS 最大允许 3 个，然后我去添加，添加成功之后我自动的就会切到流控规则这块，我的流控规则看什么单机最大的 QPS 3。


好了，那这样的话我流控我会有什么效果呢？流控的效果我们打开代码你就看到了。我们的流控效果是，如果说触发流控的话，我们找到统筹了处罚流控的话肯定会打印这句话对不对？你要访问的资源被流控了，继续执行流控逻辑对吧，肯定会打印这一句话。所以说我们来看一看这句话，我在这里就不起 jemate 了 f5 一秒钟我访问了好多次，来看一下有没有这个效果，看背流控了吧，是不是这个资源就被流控了。


那这样的话你通过这个戴世贸的控制台，你也能看到这个蓝色的上来是不是就是通过三次，然后拒绝是几次？五次对不对？

[image](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/6176b22d-fb6b-4599-a8b1-aa2e5d43ef70/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46656PIXBPI%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T225835Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQD44lfnPGXrwlGFJVP5iEg%2BXNKPM1sOqtgI49KNxbggxgIgKTOBkmTtGI6jqU4Huz8tkDC3oNK%2FNpXVekClSp3YuCkqiAQIxv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDJMBxnz%2FCj24Yy8YcCrcAyzjT0oCo4YmFn%2BHo4TS%2B0GkYnwsjt4lM4d5xVtIhyjZ3zX0w8FjE8xLxUM5HE7Pyevpi0bixdkr3%2FTbtkUR9rMlePYnIZHL251gdi6NdCj5WwKML4aNooU%2FLR5ufgTa61UDc74DA2V0XaUKXc2WpxSrP%2BMUEKtlcLBGgsUjiiS75tR1g24KAq5PCtIkyuFRX9NPMfvvtcHsMxzT7%2F8l%2B0eyRxSz9xrWh0XXpy7j7yDpIYjXSwjx8I32yUdgOZpuT2HkUb4cyKg2%2Bbwr9R4KN1hWxMnZ6DXiL8M41%2B4THBcNcuAoKKbyFLbvljvyMRgUb1lDNCE8h%2BFtSQ1MyhUS3kxCSma759yXISOMNV6gx0ZLyrQ6BXel%2FT08AMI%2BlGmIo721DJPlRgJ8RbxLRTuClS9uwlzG46%2BhjhTAV9o7Bb63hPTf%2FV89dtp0R0s0WFUua18%2BHIpiOznRthTsii%2BnlTMD68eE%2BRotOC3aaD1PIBslxf4CWetoSwSfWiZRRQ4FXnOW%2FtLBRbWlzG4%2F0VhE%2BmClHhinodFy93m10yWKCdHx569esBbe%2B82oJNX8kj2ntoY%2B6WnOt3k%2Fdh8SjL6ltC6riWp5o6mVaHbHQ8IjcTH39Vb%2BcLQjjNREh%2BQ1MJm3%2F9IGOqUB0FZ6N3iZi62S8aDfhWHB40EZy2LUPtZso1EvoPc3YFv%2FQojnx1%2BJux%2BOP44zdUy5PP21QNgbNEHoBZ0ganz0l4hZkSEex8t1H4nRZ82axnaXZKmeuNmMdlJrLIXqnRaOsy3fKJFace5JY8nxGSaHNj7JnbcRj3NGZBb0RFxa9qQ5A%2BL%2FllpNYSYEZi%2F3gRCA6y%2FT03E%2Bym%2BqHu8NdPPjIFZkYgas&X-Amz-Signature=d7a4f2fc7644b65a7bd902bb83d203adc7b1d511c8ea10abe15e92455c99be02&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

看见了吧，这个蓝色的就表示拒绝，然后绿色的表示通过就是拒绝五次，通过三次看到那这个东西就是实时的，我们再点推荐链路是吧，那我是不是可以修改啊？我这规则我能修改吗？我说我再加流控规则行不行也可以。比如说我对这个资源再加一个线程数的限制没问题。但是我现在如果想修改的话，那我就点到我们的流控规则这块，然后把它进行编辑，说之前这个 3 太小了，我把它改成 6 之前是 3 吧保存一下，改成 6 的话它也会实时发请求。然后我们再次把我们之前的那个打印出来的这个东西没事掉，然后我重新再靠手速，我就直接 f5 刷新，我们看看我能不能处罚这个流控有流控了，是不是？当然这个那这个手速肯定没有那个线程运行的快，所以说你会发现它那通过这个 dashboard 我们再看一下。每秒钟通过的就变成六次了。然后我一秒钟我们最多也就是摁个七八次，所以说他只是拒绝了一次，看见了，拒绝一次，通过了六次大家都能看到，这还挺好玩的。好，那这也就说明什么，我通过控制台去改这个阈值，他会通过 HTTP 方式主动的去把这个结果传输给 IP 和端口号是对应的那个 client 然后会更新那个 client 就我们自己的应用服务的内存，把内存刷新一下，这就是控制台。

[image](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/75eff56e-3053-4dca-8c68-b6dea1d675bd/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46656PIXBPI%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T225835Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQD44lfnPGXrwlGFJVP5iEg%2BXNKPM1sOqtgI49KNxbggxgIgKTOBkmTtGI6jqU4Huz8tkDC3oNK%2FNpXVekClSp3YuCkqiAQIxv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDJMBxnz%2FCj24Yy8YcCrcAyzjT0oCo4YmFn%2BHo4TS%2B0GkYnwsjt4lM4d5xVtIhyjZ3zX0w8FjE8xLxUM5HE7Pyevpi0bixdkr3%2FTbtkUR9rMlePYnIZHL251gdi6NdCj5WwKML4aNooU%2FLR5ufgTa61UDc74DA2V0XaUKXc2WpxSrP%2BMUEKtlcLBGgsUjiiS75tR1g24KAq5PCtIkyuFRX9NPMfvvtcHsMxzT7%2F8l%2B0eyRxSz9xrWh0XXpy7j7yDpIYjXSwjx8I32yUdgOZpuT2HkUb4cyKg2%2Bbwr9R4KN1hWxMnZ6DXiL8M41%2B4THBcNcuAoKKbyFLbvljvyMRgUb1lDNCE8h%2BFtSQ1MyhUS3kxCSma759yXISOMNV6gx0ZLyrQ6BXel%2FT08AMI%2BlGmIo721DJPlRgJ8RbxLRTuClS9uwlzG46%2BhjhTAV9o7Bb63hPTf%2FV89dtp0R0s0WFUua18%2BHIpiOznRthTsii%2BnlTMD68eE%2BRotOC3aaD1PIBslxf4CWetoSwSfWiZRRQ4FXnOW%2FtLBRbWlzG4%2F0VhE%2BmClHhinodFy93m10yWKCdHx569esBbe%2B82oJNX8kj2ntoY%2B6WnOt3k%2Fdh8SjL6ltC6riWp5o6mVaHbHQ8IjcTH39Vb%2BcLQjjNREh%2BQ1MJm3%2F9IGOqUB0FZ6N3iZi62S8aDfhWHB40EZy2LUPtZso1EvoPc3YFv%2FQojnx1%2BJux%2BOP44zdUy5PP21QNgbNEHoBZ0ganz0l4hZkSEex8t1H4nRZ82axnaXZKmeuNmMdlJrLIXqnRaOsy3fKJFace5JY8nxGSaHNj7JnbcRj3NGZBb0RFxa9qQ5A%2BL%2FllpNYSYEZi%2F3gRCA6y%2FT03E%2Bym%2BqHu8NdPPjIFZkYgas&X-Amz-Signature=31841409c1eb2df187338ec194b3c39d425ddba0226391a3502e0ba61c3c5dd0&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

[image](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/6fe88190-8832-4072-b133-ea2d2cf11e48/dashboard-Sentinel.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46656PIXBPI%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T225835Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQD44lfnPGXrwlGFJVP5iEg%2BXNKPM1sOqtgI49KNxbggxgIgKTOBkmTtGI6jqU4Huz8tkDC3oNK%2FNpXVekClSp3YuCkqiAQIxv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDJMBxnz%2FCj24Yy8YcCrcAyzjT0oCo4YmFn%2BHo4TS%2B0GkYnwsjt4lM4d5xVtIhyjZ3zX0w8FjE8xLxUM5HE7Pyevpi0bixdkr3%2FTbtkUR9rMlePYnIZHL251gdi6NdCj5WwKML4aNooU%2FLR5ufgTa61UDc74DA2V0XaUKXc2WpxSrP%2BMUEKtlcLBGgsUjiiS75tR1g24KAq5PCtIkyuFRX9NPMfvvtcHsMxzT7%2F8l%2B0eyRxSz9xrWh0XXpy7j7yDpIYjXSwjx8I32yUdgOZpuT2HkUb4cyKg2%2Bbwr9R4KN1hWxMnZ6DXiL8M41%2B4THBcNcuAoKKbyFLbvljvyMRgUb1lDNCE8h%2BFtSQ1MyhUS3kxCSma759yXISOMNV6gx0ZLyrQ6BXel%2FT08AMI%2BlGmIo721DJPlRgJ8RbxLRTuClS9uwlzG46%2BhjhTAV9o7Bb63hPTf%2FV89dtp0R0s0WFUua18%2BHIpiOznRthTsii%2BnlTMD68eE%2BRotOC3aaD1PIBslxf4CWetoSwSfWiZRRQ4FXnOW%2FtLBRbWlzG4%2F0VhE%2BmClHhinodFy93m10yWKCdHx569esBbe%2B82oJNX8kj2ntoY%2B6WnOt3k%2Fdh8SjL6ltC6riWp5o6mVaHbHQ8IjcTH39Vb%2BcLQjjNREh%2BQ1MJm3%2F9IGOqUB0FZ6N3iZi62S8aDfhWHB40EZy2LUPtZso1EvoPc3YFv%2FQojnx1%2BJux%2BOP44zdUy5PP21QNgbNEHoBZ0ganz0l4hZkSEex8t1H4nRZ82axnaXZKmeuNmMdlJrLIXqnRaOsy3fKJFace5JY8nxGSaHNj7JnbcRj3NGZBb0RFxa9qQ5A%2BL%2FllpNYSYEZi%2F3gRCA6y%2FT03E%2Bym%2BqHu8NdPPjIFZkYgas&X-Amz-Signature=892e7dcdfbe0eb07240c784f5effb5d36c422b45a9c9bda178d8db150cfe4ffd&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)


