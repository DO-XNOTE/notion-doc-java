---
title: 1-15 【技术改造】电商项系统集成 Sleuth- 集成ELK
---

# 1-15 【技术改造】电商项系统集成 Sleuth- 集成ELK

[image](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/9dba02bc-a282-47c2-8dbe-c94c4d5a0b6b/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TSVJ4LSJ%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T225806Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIGMq7FFscnQdReeWPbf0gG%2BhDPw%2Bi1EkA7VbFlxCffBKAiEAhWf3TSt25%2BUlwEqHOGLF6XwqOdmgCZo%2BVBzE7uCzRfgqiAQIxv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDBLk%2BUSaFHHCsO4L0SrcA4fHSWt0lXwEsrXzYWN7XD7yDul551qi%2FhnwqgTKT5zIKP5%2FVLclA%2BTaO1XfJnAQQJbSzQDE%2Bgveiwv9cAhoGUVsM2IpHOujiUGQY0y%2BnCONB3yr9wMJwBeIUwyW%2FXqTTuu99XJJ2wwpIPeyBfjW3WaBh4vj%2FI%2FxoKpnFJi3NFVA9565RvYIFRMGCEWBtS8bL%2BkXTctFjQqiJsTKv7Vp%2BmZW7rzSwtKGOcGkCBksT8qpk%2BxCxnnXU0qGotqbf0ug8SnPj11RJENofijHjf61IGqwnkVqnHXheEeTrbeSOdDLhhyJe8RTAAADbjS2LBL0W0EQh3GkOwgqebOdyETZnOwvS%2BQCPNXU648jpCVD9AQGyHo21CVFeZwgzDyCVWaYuepYGrkw%2Fe6thrErtPPhaVlGPw6KKc2T%2FGY1kaf7UoSmFlWKG7ASgN3GfruQxMEQt9BHabIcQrgsXlsPRkcMRS19tIAs2uMH%2FAeA%2FYO4Z5MLzha%2BMyw7H0xErnxfRZVkusK8e9h%2FyMJPjw1gabYa%2BG7i5BY9aC%2BW5vatPRljRWJZJ1VtCoMDjwv0hNtQonVw3MnOFM5%2B27x2%2Fb0caxDNQD%2FkUe%2FUDSCPhApCfxD46ThRXdXsFAKFXqHeIdPIMJa3%2F9IGOqUBSI44Mh1b5iV0ieN%2Fve4mXzRHq%2FwvkI8p2Um9PLhM%2FYciZcgXA9zVj0I57KUaEe27c%2FnyTHgh0rzjZ1TCcdlLCWyCHdqUp11LImkWWEwXmc1Km%2FzrhqHD5UNdCGzoydhod2z2%2BsrKosYV1sj8ycApl3GiBVYnFy4kIvdS%2Fqgkz1CSjy6doP6I2PUViUj7hkccXnGJIwWDgwiuripzuMJHV6483ZVY&X-Amz-Signature=6d8b4e6328c12f1ded9a4833e9fc3f028643ccc9404631de9269592d9c78871e&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

[image](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/c402716f-295e-4edc-bf41-d815b09b7d53/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TSVJ4LSJ%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T225806Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIGMq7FFscnQdReeWPbf0gG%2BhDPw%2Bi1EkA7VbFlxCffBKAiEAhWf3TSt25%2BUlwEqHOGLF6XwqOdmgCZo%2BVBzE7uCzRfgqiAQIxv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDBLk%2BUSaFHHCsO4L0SrcA4fHSWt0lXwEsrXzYWN7XD7yDul551qi%2FhnwqgTKT5zIKP5%2FVLclA%2BTaO1XfJnAQQJbSzQDE%2Bgveiwv9cAhoGUVsM2IpHOujiUGQY0y%2BnCONB3yr9wMJwBeIUwyW%2FXqTTuu99XJJ2wwpIPeyBfjW3WaBh4vj%2FI%2FxoKpnFJi3NFVA9565RvYIFRMGCEWBtS8bL%2BkXTctFjQqiJsTKv7Vp%2BmZW7rzSwtKGOcGkCBksT8qpk%2BxCxnnXU0qGotqbf0ug8SnPj11RJENofijHjf61IGqwnkVqnHXheEeTrbeSOdDLhhyJe8RTAAADbjS2LBL0W0EQh3GkOwgqebOdyETZnOwvS%2BQCPNXU648jpCVD9AQGyHo21CVFeZwgzDyCVWaYuepYGrkw%2Fe6thrErtPPhaVlGPw6KKc2T%2FGY1kaf7UoSmFlWKG7ASgN3GfruQxMEQt9BHabIcQrgsXlsPRkcMRS19tIAs2uMH%2FAeA%2FYO4Z5MLzha%2BMyw7H0xErnxfRZVkusK8e9h%2FyMJPjw1gabYa%2BG7i5BY9aC%2BW5vatPRljRWJZJ1VtCoMDjwv0hNtQonVw3MnOFM5%2B27x2%2Fb0caxDNQD%2FkUe%2FUDSCPhApCfxD46ThRXdXsFAKFXqHeIdPIMJa3%2F9IGOqUBSI44Mh1b5iV0ieN%2Fve4mXzRHq%2FwvkI8p2Um9PLhM%2FYciZcgXA9zVj0I57KUaEe27c%2FnyTHgh0rzjZ1TCcdlLCWyCHdqUp11LImkWWEwXmc1Km%2FzrhqHD5UNdCGzoydhod2z2%2BsrKosYV1sj8ycApl3GiBVYnFy4kIvdS%2Fqgkz1CSjy6doP6I2PUViUj7hkccXnGJIwWDgwiuripzuMJHV6483ZVY&X-Amz-Signature=a7c6eba4c59f428204f7c40db5e95d5f7bfe569dafccd3cb259fc357d1269917&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

hello 我们课网的各位同学们，大家好，我是小半仙，咱这一节是整个 sleuth 章节的最后一节，我们来把 elk 给集成到咱的电商项目当中。 okay 那这里我们先从哪个服务动刀子，柿子要减软的捏，我们挑一个最简单的 authentication API 咱的 auth 服务。那在 auth 服务集成过程中，没有什么坑，我们就依葫芦画瓢，把之前随堂 demo 里的 elk 的 dependency 还有配置文件直接给 copy 过来就可以了。


好，那这是第一步，我们要把它的泡沫文件打开，把之前随堂练习里的 logstash encoder 给它 copy 过来。好，我们切到随堂练习里面，找到这个 through the tre C 或者 trace B 任意一个，把它的 palm 打开，就是要它了。你看 logstash for el keyokay 我们把它给拿过来。好，copy过来之后我们就要去更改一下配置文件 resources 下面的这个 logback string 好，我们打开它。接下来在这个 log 文件的配置当中，我们要添加一个新的 appender 好我们切换到之前的随堂demo ，在随堂 demo 里面，我们从它的 logback spring 里面找到咱为 logstash 专门添加了一个输送 log 数据的这样一个 panda 把它给 copy 过来。 Ok. 那 copy 过来之后，不要忘了在这里这最后咱的 logstash panda 添加到根节点下面。 OK 这个名字叫 logstash OK 好，这个项目已经改造完了，那我们可以直接把它给跑起来。好，然后在跑的同时，我们接下来改。


第二个项目有一点小坑，那我们就移步到这个 user 微服务当中。好同学们看到它的 log 配置文件会发现它这里面使用的是 log for G 那我们之前在 auth 服务中使用的是什么呢？是 log back 如果同学们尝试着把这个 log for jr 替换成 logback 会发现它根本不起作用。为什么呢？这就要从依赖项说起了。同学们看这个 auth 服务，因为它是新创建的这个微服务，所以它依赖的 dependency 非常的少，都是出自名门正儿八经的这些咱 spring cloud 下面的微服务组件。但是这个 user 微服务，我们点开它的泡沫文件看一下。这里我们往上走看到它依赖了一个什么呢？ foodie cloud web components 我们点进去。好，这里又依赖了 food cloud common 好，我们再点进去，玄机就在这里。好嘞，那这里就是这个坑所在的地方了，咱的项目依赖了 spring boot starter 但是我们把其中的 logging 这一个组件从这里面移除掉了。


所以如果我们在用户微服务里面仿照 of service 添加 logstash 的配置，那其实是不起作用的，因为它这个依赖项已经被排除掉了，要怎么办呢？我们把这个依赖项 copy 一下，把它的 group ID artifact ID 给它 copy 然后拿到哪里呢？**拿回到 foodie user web 当中，你这里不是把它剔除掉了吗？我再给它找回来，那我们把它复制过来**。

```java
<dependency>
    <groupId>org.springframework.boot</groupId>
    <artifactId>spring-boot-starter-logging</artifactId>
</dependency>
```


Ok.复制过来以后，我们再把前面添加的这个 logstash 的这个 dependency 也给它添加到 user 微服务当中。 OK 那这样一来，咱这个坑就被趟平了。那我们就可以把这个 log for G 的配置给它删除掉了，替换成 logback 如果同学们这里定义了一些 log 的文件格式，还有它存放的位置，我们可以把它移植到咱的 logback 配置当中。好我们从上面刚刚配置好的这个 logback 给它 copy 下来。然后大笔一挥，把咱的这个 lock four J 给它删除掉。那 lock four J 里面的内容，同学们如果想移植过去，可以自己把它改到咱的 logback 配置文件当中。

```shell
<?xml version="1.0" encoding="UTF-8" ?>
<configuration>

    <include resource="org/springframework/boot/logging/logback/defaults.xml" />

    <!--日志输出位置-->
    <property name="LOG_FILE" value="${BUILD_FOLDER:-build}/${springAppName}" source="spring.application.name"/>

    <!--日志格式-->
    <property name="CONSOLE_LOG_PATTERN" value="%clr(%d{yyyy-MM-dd HH:mm:ss.SSS}) %clr(${LOG_LEVEL_PATTERN:-%5p}) %clr(${PID:- }){magenta} %clr(---){faint} %clr([%15.5t]){faint} %m%n${LOG_EXCEPTION_CONVERSION_WORD:-%wEx}"/>

    <!--控制台输出-->
    <appender name="console" class="ch.qos.logback.core.ConsoleAppender">
        <filter class="ch.qos.logback.classic.filter.ThresholdFilter">
            <level>INFO</level>
        </filter>
        <!--日志输出编码-->
        <encoder>
            <pattern>${CONSOLE_LOG_PATTERN}</pattern>
            <charset>utf8</charset>
        </encoder>
    </appender>

    <appender name="fileLog" class="ch.qos.logback.core.rolling.RollingFileAppender">
        <encoder>
            <pattern>
                [%d{HH:mm:ss.SSS}] %-5level [%thread]%logger{15} - %msg%n
            </pattern>
        </encoder>
        <rollingPolicy class="ch.qos.logback.core.rolling.TimeBasedRollingPolicy">
            <fileNamePattern>logs/%d.log</fileNamePattern>
            <maxHistory>30</maxHistory>
        </rollingPolicy>
    </appender>


    <!-- Logstash -->
    <!-- 为logstash输出的JSON格式的Appender -->
    <appender name="logstash" class="net.logstash.logback.appender.LogstashTcpSocketAppender">
        <destination>192.168.13.249:5044</destination>
        <!-- 日志输出编码 -->
        <encoder class="net.logstash.logback.encoder.LoggingEventCompositeJsonEncoder">
            <providers>
                <timestamp>
                    <timeZone>UTC</timeZone>
                </timestamp>
                <pattern>
                    <pattern>
                        {
                        "severity": "%level",
                        "service": "${springAppName:-}",
                        "trace": "%X{X-B3-TraceId:-}",
                        "span": "%X{X-B3-SpanId:-}",
                        "exportable": "%X{X-Span-Export:-}",
                        "pid": "${PID:-}",
                        "thread": "%thread",
                        "class": "%logger{40}",
                        "rest": "%message"
                        }
                    </pattern>
                </pattern>
            </providers>
        </encoder>
    </appender>

    <root level="INFO">
        <appender-ref ref="console"/>
        <appender-ref ref="fileLog"/>
        <appender-ref ref="logstash"/>
    </root>

</configuration>
```


那咱这两个微服务改完了之后，我们还可以去把一些中间件给它改掉，比如谁比如咱的网关层。好，我前面咱说过，大家不用把这个网关层理解成中间件其实它就是一个正儿八经的微服务。那咱把这个网关层的 pump 文件当中同样的也可以加上 logstash 并且在它的 resources 下面，这里也有一个 logback spring 那我们就直接把前面的 logback spring 给它拿下来覆盖掉。


好，这就可以了。那这一节的内容真的是超快猛，咱迅雷不及掩耳盗铃之势已经风卷残云，把所有配置都搞定了。接下来我们就把这些应用给它启动起来看一下。好，前面我们已经把 author 为服务给它启动起来了。那接下来我们启动 user 为服务，在启动 user 维服务的档口，我们去到 terminal 里面，把咱的 elk 的 Docker 给它启动起来，命令是 Docker restart elk 那这个 elk 是 Docker 的名称。那这一步同学们需要稍微有点耐心，因为这个 Docker 启动过程非常的长，对，同学们要耐心等待它全部加载完成。你比如像这个情况，它返回了一个 elk 很多同学们以为它已经加载完了对不对？实际上还没有它在后台，还在持续不断的加载，我们稍微等个 5 到 10 分钟的时间。


接下来我们把这个 gateway 也给它启动起来，然后咱就静候加音，等待我们的 Docker 启动。好了之后，去 kibana 上面查一行 log 就可以了。 OK 那半炷香时间已过，咱应用启动起来了，doctor也已经启动。好了，我们转粘到浏览器里面。好，这是 kibana 的主页，我们这里点击一下它的 search refreshok 看到咱前面已经集成上来的几个微服务，这里都有 log 打印出来了。比如你看第一行 log 就是谁的是咱的 gateway platformgateway 做的服务，发现的一行。牢。
OK 我们转到 postman 里，尝试调用一把用户微服的地址模块，这里我们故意给定一个错误的 authentication 好，点击发送它，这里应该会返回一个 403 forbidden 好，我们这时候转战到 kibana 里面，点一下 refresh 看刚才的这个 log 请求能不能被捕捉到。


那茫茫多的 log 我们怎么选呢？好，我们找一下关键字，我们搜索一个网关层的关键字叫 off start ，点击 refresh 好，这里已经出来了，你看网关层的 log 都已经显示在这里面了。那通过这一行log ，我们找到它的trace ，然后直接通过 trace 来搜索一把，就能把这个上下游所有的链路上的 log 给它给揪出来。好，这里显示出来的就是这整个调用链上的所有的茫茫都的 log 了。


OK 那本章最后一个任务我们已经完成了。开始的时候老师就说过 sleutha 就是一个打辅助的角色，没有太多的难点。那相信同学们学起来也感觉到是如行云流水，无丝毫障碍。对不对？可能有的同学会卡在 Docker 这里，因为对 Docker 的操作可能不太熟悉。没关系，后面我们看张老师有 Docker 专题课，同学们可以在后面章节把 Docker 的技能点加上之后，再回过头来打这一张的副本。 OK 同学们，那我们这一章的内容就到这里结束了，我们下一周再见。


