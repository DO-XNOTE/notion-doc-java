---
title: 1-12 【Demo】Sleuth集成ELK实现日志检索-2
---

# 1-12 【Demo】Sleuth集成ELK实现日志检索-2

[image](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/304beda2-7c84-496d-aa26-e24ceebdc55d/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666HUZUCKX%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T225803Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCfmAiHfcjuj1bbziDXLcpShD%2BjjQ25vNbLJsdvZRuUggIgNQ%2F3yk8mm1wt8jAl%2FNNXwXlCteiHq%2Box7%2F77XO7ekpAqiAQIxv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDHQ%2BVgcW1iqcfwDIeSrcA%2BnDh5KOYB0VcNkx%2Fjjhi0Z0U1NVKvca37i96W7ENZbmxsxmm5XHDM%2BA3yr0VaM1SwSI7H47kDDlhlcoOhtmaSi26TD%2Fqtxi579EiFysrwRRRjC%2BrH3iT5zujjVrGDQv9GJaVJ%2FEnwkOBtOQm%2Bi8yd783wkouw4crzhjRGXDpNlHCbJmjFUBafLDFykT4KyA%2BS3e9A7vETTYsuduwKNHc5uJtJxvDm4TW9FO59OsemHd1C2jgXBB%2BX%2FkTsMMVRawOyJpdz2bhIBbFfAuvydEuhUlNYdBbJCNbIZDuHyp5%2FYA1UUNtiIjRYOlaLI8ntcjYy2Pa4S1lWtpWbwDla9uSoBIALvXqPfOXHJHSaowYdhBlXMdogXCCgrnQ2l%2FJjlhhT4t2IwWy3JmmRLk5xFy1Mgcfo6XGNPl03ewXf73Qphzz7u0PrCgsYP5kdyqe95OokVVWLP0G2MBwETJiYC2qkezxLgnAPuZ%2BJxKy7tFIVnVU1pVrWCKJfKxPVTQPKkhHUPuVlfDldUDuC9%2B03pqHOfYz5HVc62ZCshzeY8wpbVcJtoGYaPQrHm0WfAqIdHXQlySKyDNeyjcOYnYVCKmfWwqHgyl0%2FKR1Bh0x6bq%2FlLJaCO747nRQurvzs4ZMIK4%2F9IGOqUBAtYtvL2hPJnpLtBGpvey%2BKFqtULZR58zpEHT0%2F7hNh6q7zDlNgDjiJvuXORrhyCJsIpALhGVRKwYJp0ncxCxJqLT3i1mepokJzusjIYv87jR8JzbDQ%2FMh%2FZMCp8MpvG9dwF8fc7V0KehTfEXK17Cu%2BhYawLArZyTfy3Fwp1R%2BTGZLaM06vJW2om%2FQY2qebJ5nQuCeqnrj57BCJYh0pfjV7oNSAl6&X-Amz-Signature=99d524ea4b4a71193c897ccb0cc098d8e06b602cbaeb70ce0e5254b72c67ddac&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

[image](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/8b8f7f42-3a0a-4baf-8025-9215a4e92484/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666HUZUCKX%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T225803Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCfmAiHfcjuj1bbziDXLcpShD%2BjjQ25vNbLJsdvZRuUggIgNQ%2F3yk8mm1wt8jAl%2FNNXwXlCteiHq%2Box7%2F77XO7ekpAqiAQIxv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDHQ%2BVgcW1iqcfwDIeSrcA%2BnDh5KOYB0VcNkx%2Fjjhi0Z0U1NVKvca37i96W7ENZbmxsxmm5XHDM%2BA3yr0VaM1SwSI7H47kDDlhlcoOhtmaSi26TD%2Fqtxi579EiFysrwRRRjC%2BrH3iT5zujjVrGDQv9GJaVJ%2FEnwkOBtOQm%2Bi8yd783wkouw4crzhjRGXDpNlHCbJmjFUBafLDFykT4KyA%2BS3e9A7vETTYsuduwKNHc5uJtJxvDm4TW9FO59OsemHd1C2jgXBB%2BX%2FkTsMMVRawOyJpdz2bhIBbFfAuvydEuhUlNYdBbJCNbIZDuHyp5%2FYA1UUNtiIjRYOlaLI8ntcjYy2Pa4S1lWtpWbwDla9uSoBIALvXqPfOXHJHSaowYdhBlXMdogXCCgrnQ2l%2FJjlhhT4t2IwWy3JmmRLk5xFy1Mgcfo6XGNPl03ewXf73Qphzz7u0PrCgsYP5kdyqe95OokVVWLP0G2MBwETJiYC2qkezxLgnAPuZ%2BJxKy7tFIVnVU1pVrWCKJfKxPVTQPKkhHUPuVlfDldUDuC9%2B03pqHOfYz5HVc62ZCshzeY8wpbVcJtoGYaPQrHm0WfAqIdHXQlySKyDNeyjcOYnYVCKmfWwqHgyl0%2FKR1Bh0x6bq%2FlLJaCO747nRQurvzs4ZMIK4%2F9IGOqUBAtYtvL2hPJnpLtBGpvey%2BKFqtULZR58zpEHT0%2F7hNh6q7zDlNgDjiJvuXORrhyCJsIpALhGVRKwYJp0ncxCxJqLT3i1mepokJzusjIYv87jR8JzbDQ%2FMh%2FZMCp8MpvG9dwF8fc7V0KehTfEXK17Cu%2BhYawLArZyTfy3Fwp1R%2BTGZLaM06vJW2om%2FQY2qebJ5nQuCeqnrj57BCJYh0pfjV7oNSAl6&X-Amz-Signature=4736d59afb563c7659cef15c15268f4ae3ae68414d6a7c437ba20d428c954aab&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

[image](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/5b9befe1-da4e-4729-8eda-00d6b9713490/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666HUZUCKX%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T225803Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCfmAiHfcjuj1bbziDXLcpShD%2BjjQ25vNbLJsdvZRuUggIgNQ%2F3yk8mm1wt8jAl%2FNNXwXlCteiHq%2Box7%2F77XO7ekpAqiAQIxv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDHQ%2BVgcW1iqcfwDIeSrcA%2BnDh5KOYB0VcNkx%2Fjjhi0Z0U1NVKvca37i96W7ENZbmxsxmm5XHDM%2BA3yr0VaM1SwSI7H47kDDlhlcoOhtmaSi26TD%2Fqtxi579EiFysrwRRRjC%2BrH3iT5zujjVrGDQv9GJaVJ%2FEnwkOBtOQm%2Bi8yd783wkouw4crzhjRGXDpNlHCbJmjFUBafLDFykT4KyA%2BS3e9A7vETTYsuduwKNHc5uJtJxvDm4TW9FO59OsemHd1C2jgXBB%2BX%2FkTsMMVRawOyJpdz2bhIBbFfAuvydEuhUlNYdBbJCNbIZDuHyp5%2FYA1UUNtiIjRYOlaLI8ntcjYy2Pa4S1lWtpWbwDla9uSoBIALvXqPfOXHJHSaowYdhBlXMdogXCCgrnQ2l%2FJjlhhT4t2IwWy3JmmRLk5xFy1Mgcfo6XGNPl03ewXf73Qphzz7u0PrCgsYP5kdyqe95OokVVWLP0G2MBwETJiYC2qkezxLgnAPuZ%2BJxKy7tFIVnVU1pVrWCKJfKxPVTQPKkhHUPuVlfDldUDuC9%2B03pqHOfYz5HVc62ZCshzeY8wpbVcJtoGYaPQrHm0WfAqIdHXQlySKyDNeyjcOYnYVCKmfWwqHgyl0%2FKR1Bh0x6bq%2FlLJaCO747nRQurvzs4ZMIK4%2F9IGOqUBAtYtvL2hPJnpLtBGpvey%2BKFqtULZR58zpEHT0%2F7hNh6q7zDlNgDjiJvuXORrhyCJsIpALhGVRKwYJp0ncxCxJqLT3i1mepokJzusjIYv87jR8JzbDQ%2FMh%2FZMCp8MpvG9dwF8fc7V0KehTfEXK17Cu%2BhYawLArZyTfy3Fwp1R%2BTGZLaM06vJW2om%2FQY2qebJ5nQuCeqnrj57BCJYh0pfjV7oNSAl6&X-Amz-Signature=a444a7fbe09db35d227b3cbd02987ed4f922aa4545f370f5c66a9007d0ad05be&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

慕课网的各位同学们，大家好，在这一小节里咱要进行 sleuth 的集成。 elk 的下半场，咱在上半场中已经搭建了 elk 的容器。那么接下来咱只用把 trace A 和 trace B 当中的日志推送给 el K 就可以了。 OK 我们看一下这一节的主要内容有哪些第一部分，我们先要引入 logstash 的依赖到 solution 项目中。那为什么是 logstash 而不是 elk 中的另外两面大将 elastic search 或者 kibana 因为 logstash 才是最终接收我们 logc 信息的终端。所以这里则要引入依赖，然后配置 logg 文件，将 logc 信息输出到 logstash 所以咱要把这个依赖项目引入到 sleuth 的项目中。


紧接着第二步我们就要配置日志文件，将所有的日志信息以 JSON 格式输出到 logstash 前面。大家还记得咱在配置容器的时候，更改了 logstash 的配置项，让它可以接收一个 JSON 格式的字符串。这个配置项的改动其实就对应着咱的日志文件中的格式。


OK 这一节咱轻轻松松不用写一行代码。同学们准备好的话，我们 intelligi 走起编程是我快乐，996是我的福报。前面一节，咱有些同学还是挣扎在 Docker 的泥沼中爬不出来了。没关系，大家就跟着这个步骤一步一步往下做。其中比较费脑子的有这么几步，我跟大家说一下。第一个，有的同学觉得下载速度实在太慢，其实没关系，有两个方案，大家可以去买一个 VPN 或者谷歌 cloud 是可以有免费一年使用的，大家可以去申请一年的 Google cloud 然后自己搭一个 VPN 这个其实并不难。除此以外，在第二步里面，有的同学创建了一次容器之后发现再次打这个命令的时候不生效了，因为咱这边提示过，它只有第一次使用的时候才会创建。也就是说你一旦执行了这个命令，你的容器 


container 也已经创建出来了。那么后面如果你再要继续使用，只用开启容器而不用再重新创建容器了。用 Docker 操作容器开启关闭。可以大家到网上去查一下命令，都是非常简单的。 OK 再提一点。


第四步，修改文件。这里涉及到 VI 或者 wim 操作。大家对 Linux 文件修改，如果命令不熟悉的话，可以到网上去了解一下 wim 的命令行，因为在 Linux 中修改文件毕竟不像 Windows 这样方便。 OK 这就是老师对上一节内容的心情嘱托了，那咱开始这一节的内容下半场。好，咱先要给 sluice A 和 sluice 的 trace B 添加 lock stash 的依赖，我们打开 pump 文件收集小桌板，在最后面添加一个新的 dependency 在添加之前，咱先给它注释一下，这个是 log stash 然后是 for alkok 添加一个节点，它的 group ID 是 net.logstash.logback 你看实际上它是一个 logback 组件。那接下来它的 artifact ID 是 logstash 杠 lockback got encoder 好，大家看到这里的 artifact 的 ID 的名字应该就豁然开了他就是一个中间人，一头连着你的 logback 一头连接你的 logstash 将 log 信息发送过去。 OK 那我们给它指定一个 version 我们用稳定版本 5.2 release 版本。


OK 那依赖项咱添加完毕了以后，接着要去给它创建一个 log 文件。 okay 咱点开之前的 resource 下面中添加的 logs back screen 在这里面我们只配置了一个控制台输出。对不对？咱要在下面添加 logstash 的输出，我们先把注释写上去。 logstash 这个配置可是相当长。老师也记不住。所以我又要抄作业了，我从自己的项目里面把 logstash 的配置项给它 copy 过来，我们来变魔术。1223。


好，就是这个东西了，它是什么意思呢？这是一个 appenda 大家知道在 log 文件中，每一个输出终端都是一个 appender 那这一个 appender 就是专门针对于 logstash 的。 OK 大家可以看到它这里面有一个 class 的类放在这儿，那这个类来自于哪呢？就来自于刚才咱引入的这个依赖项。 OK 那我们再看 destinationdestination 这个幺二七零点零点幺就是 local host5044 是谁呢？咱前面启动 Docker 的时候，是不是给 lokstash 指定了一个端口啊？就是5044。所以说它最终这一个 appender 的目标地址就是咱的 logstash 再往下看，这里是一个 encoder 它需要对咱的 log 信息做一个 encode 它的 timestep 是使用标准的 UTC time zone 然后关键的信息在下面。这个 pattern 在这个 pattern 里面，咱添加了很多的属性，比如说有 log 的级别，还有你的 service 的名称以及 trace ID span ID 然后是现成的名称以及你的正儿八经真实的 lock 信息。

```shell
logback-spring.xml
==========================================================================================================================================================================================
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
        <appender-ref ref="logstash"/>
    </root>

</configuration>
```


OK 这里如果大家觉得还不够，其实可以往后再添的，可以添加你自己需要的信息，把它传送给 logstashok 那咱这就写完了吗？还没有，咱只是声明了一个 appender 但是它还没有起作用。好，我们往下翻滚到页面最底部。 OK 把这个 appender 给它加入进来，咱 appender 的名字叫什么？就叫 logstash 那我们就把这个名称复制一下，然后输出到 root 节点下。


OK 那这就配置好了，咱把配置好的信息，从 trace A 这个项目中再给 copy 到 trace B 首先把 palm 给拿过来，然后放到 trace B 的 pump 文件中。改完 pump 以后，再把 logback 的文件这可以直接复制过来了，把 root 节点和这个新添加的 appenda 一起 copy 过来，然后到 treespeed lockback 里面把它一股脑地塞进去。


好嘞，那现在就可以启动项目了。不过在咱启动项目之前，先去看一眼 kibana 好，我们切换到浏览器，打开 kibana 的 search 页。好，你看发现 no results match your search criteria 现在还没有任何的数据返回。


OK 那咱启动一下项目，看接下来会有什么神奇的事情发生，咱依然是先启动 sleuth trace B 把它跑起来。等 trace B 启动完成以后，咱再启动 loose 的 trace A 好，到这里 trace B 已经启动。好了，我们转战到 tre C 把它启动一下。 OK 我们看到 trace B 这里实际上已经打出了一些log，这些启动 log 如果不出意外的话，肯定已经传送给 logstash 了。那咱先让 tre C 在一旁启动着，先到 kibana 上面去查看一下 trace B 的启动 log 那 trace B 有什么特征量呢？我们把这个 97573 给 copy 下来，它就像个代号，就像 9527 这种代号一样。好我们到浏览器当中，然后这个页面咱把它刷新一下。
Ok. 同学们看，这里是不是已经有了一些信息展示。那这个 log 就是我们刚才配置的 JSON 字符串，这里面有 service 有 span 还有 rest 这个 rest 就是咱打印的 log 具体信息了。Ok.刚才我们不是 copy 了一串 9527 的什么代号，这是什么？这是它的 PID 我们在 filter 上这样搜索，我们可以直接搜索 PID 同学们你看这里就过滤出了很多个 log 这些都是谁的这些 log 通通都是 trace B 的启动 log 好，咱回过头来看一看 Tracy 有没有启动完成。 OK Tracy 也启动完成了。那咱把 log 清空一下，然后走到 postman 里，调用一把 Tracy 看一看它的端口是62,000，我们点击 send 好嘞，这已经返回结果了。


那么我们回到 log 里面，抓谁呢？我们要抓他的 trace ID 同学们，你看这一行，看这个 trace ID 就是整条链路的调用链了，咱把它 copy 一下。然后你看 trace B 里面应该也有同样的一个ID ，我看一下它在哪了，它的 ID OK 在这也就是说这个调用链路从 trace A 调用到 trace B 那它的 trace ID 就是，咱把这一条复制出来，然后走到 kibana 里面搜索一下。


同样的两种方式，我们可以直接搜索这个 trace ID 点击回车，这里就已经可以看到结果了，它打印了很多很多 log 但是大家在搜索的时候可能会发现一个现象，就是说同一行 log 这里被显示了多次。为什么呢？大家要注意这里，在所有的链路追踪系统中有一个非常重要的属性叫做什么叫做 indexindex 是我们创建的搜索索引。那么你的一行 log 有可能被匹配到多个索引当中。所以通常来讲，大家使用这种 log 追查系统的时候要指定它的 indexok 咱刚才是直接搜索了这个 trace ID ，如果我们根据某个属性名来搜索是怎么搜索呢？我跟大家看一下。


OK 它的属性名称我们看一下它叫 trace 好在这里直接打上 trace 一个冒号把它打出来。我们再缩小一下看。 kibana 中的 filter 有一套自己的语法，比方说你如果想搜索某个属性等于谁，那就用这个冒号就可以了。然后它这里面还有其他的几个符号，比如说我们随便打一个打一个 type 然后你看这里，有冒号星还有雨或者是或。那大家如果需要进行复杂搜索，可以去参照一下 kibana 开源文档中关于 filter 的用法。


OK 这里还有一个关键的信息是时间，因为咱线上环境它的 log 非常非常多，如果不能指定到非常细的信息，比方说一个 trace ID 或者一个业务组件，像 order ID 那么咱单单的只是通过 log 打印出来的，具体信息来搜索的话可能会导致搜索效率非常低，时间非常慢。这时候其实我们可以缩短时间窗口，把咱这个时间搜索范围定位到几分钟以内甚至是几秒钟以内都是可以的。这里有非常丰富的时间选择框，我们可以选择过去 15 分钟 1 小时或者 90 天，甚至过去一年也可以定制一个非常具体的时间。


OK 如果你有常用的查询需求，其实也可以创建一个 dashboard 帮大家辅助查询。那往后还有很多很多其他稀奇古怪的按钮，就有带大家自己去一点点探索了。 kibana 还是一个功能相当丰富，而且这个画面也非常有科技感的开源组件了。我个人甚至觉得它比当前一些收费版的链路追踪系统还要好用多了。甚至说实在的，它这个应用性比阿里的鹰眼系统还要简单多了。 OK 那讲到这里，本节的内容就到此结束了，我来带大家回顾一下。在本节的下半场当中，我们为集成 elk 做了以下几个改动，第一步是在 palm 中加入了 logstash 的依赖。第二步是在 log 文件中添加了一个新的 appender 将咱需要的 log 信息转化成了 JSON 的格式，并最终发送给 logstash 最后我们在 cabana 页面上面通过 trace ID 定位到了咱应用系统打印出来的 logok 那本节的内容就是这些了，在后面的小节里，我们要把smooth 、 zip king 还有链路追踪系统集成到咱的电商项目当中。


然后在本章的最后给大家一个小彩蛋，带大家了解一下阿里系的链路追踪系统，这可是阿里系的王牌中间件。叫鹰眼。话说名字起的牛逼的项目其实都不咋地。不过鹰眼是个例外了。 OK 同学们到这里咱就下课了，我们在下一小节里再见。




