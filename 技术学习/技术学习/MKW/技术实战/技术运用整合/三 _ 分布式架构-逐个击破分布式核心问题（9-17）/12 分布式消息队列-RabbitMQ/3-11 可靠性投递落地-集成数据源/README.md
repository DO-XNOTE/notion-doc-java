---
title: 3-11 可靠性投递落地-集成数据源
---

# 3-11 可靠性投递落地-集成数据源

[image](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/3fd80892-d567-4549-8872-7626c0e58921/SCR-20240806-rtpz.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662Z6WHANW%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T225304Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIBSt%2BO0YcERoD6vSsmiwJQrIL39qBZuTt7dUu7y8FFabAiEAtUEPhwgwlvEKCK1AICQo4Pb3Ae%2FA6mtRaMQlo%2BjtH4MqiAQIxv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDM9FklCeH4jFXhdDYyrcA2uJ5dy2pvORSbannnIUq2emAoHkeZC6jpuyWRUEMci2yG6fxwjadbjj%2BaJ13JXwuC%2FTDASJK0MqvbFA%2F7N4cmQx3hCRzZ%2B56FjAjgYwbB0zdUOedabk6eOc1ItegCTq2hfhnkznitg8cpcFjs6hIaBWAFikw8HCMDmOtSwwU5aabRDtKGlaI26afc0IZH%2FeYxporQhhPlu0uqKnxsfm7bUqIOeachGpLyC9qZjuLCBAP1TRzjW%2FEtS4zUMEMumvFwdjvm%2BaNGeBqciF9lzIEhvHtVOm6zyiB7%2FZ%2BZMEq0cAIx3TQGguA5luYrjAAYn2iiRetyU53nj69nc7PGGMk0xVoQjCwGKK7DwAHa%2BR03jvESaXrerYPDyqrAIaAwOSAcVN97Qasle%2BSHipJNXh8QBZqRIUUjh%2F%2F14SPObEVLmRy4OGoLt75EoflgLS37daN3k3ailTS0p8EuaDpkbzVMueBIGkDD2V6Ws5hFroiXjF4Aym7hYJtcI7x9FRR0dSOohPg%2F2wlyce95faHSMx1nyoJN2yXI810U3a7F97H2WIuPekxT74u7Fuj2Utw5icnpJVyFos7zrt30Xt6lfRh1tROwjpUJWZp5RH4U%2BOnNJSXOd1QEl%2Ba8YH6fUlMIu4%2F9IGOqUBcA8F8EhUBp9W66%2FRotMhc0WPkVVbTUX0eXF6kaDkFcu9amLESdAl%2BK1AnYfF1USVSusM7VghB99zf%2Fz3HBudb07BcNKMPgwIAto5dAAx6O7L18YWwpo7zCtF18k3coYn6m4Bfpv8oFzM8TFdmTZxlkdMhh5xb8%2Fvhg6LvGjKAvQ4eXZzhs7jcjOduJkUB9oKka9PGuGWHG4T51lb%2B7reofzRAX0u&X-Amz-Signature=981c0a47787980a7f59450d6f913bf0acea988e77375a3cad1263b6c5fad2ee7&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

[image](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/920c32e1-a959-4f3a-9aa8-1e047f87b0bf/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662Z6WHANW%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T225304Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIBSt%2BO0YcERoD6vSsmiwJQrIL39qBZuTt7dUu7y8FFabAiEAtUEPhwgwlvEKCK1AICQo4Pb3Ae%2FA6mtRaMQlo%2BjtH4MqiAQIxv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDM9FklCeH4jFXhdDYyrcA2uJ5dy2pvORSbannnIUq2emAoHkeZC6jpuyWRUEMci2yG6fxwjadbjj%2BaJ13JXwuC%2FTDASJK0MqvbFA%2F7N4cmQx3hCRzZ%2B56FjAjgYwbB0zdUOedabk6eOc1ItegCTq2hfhnkznitg8cpcFjs6hIaBWAFikw8HCMDmOtSwwU5aabRDtKGlaI26afc0IZH%2FeYxporQhhPlu0uqKnxsfm7bUqIOeachGpLyC9qZjuLCBAP1TRzjW%2FEtS4zUMEMumvFwdjvm%2BaNGeBqciF9lzIEhvHtVOm6zyiB7%2FZ%2BZMEq0cAIx3TQGguA5luYrjAAYn2iiRetyU53nj69nc7PGGMk0xVoQjCwGKK7DwAHa%2BR03jvESaXrerYPDyqrAIaAwOSAcVN97Qasle%2BSHipJNXh8QBZqRIUUjh%2F%2F14SPObEVLmRy4OGoLt75EoflgLS37daN3k3ailTS0p8EuaDpkbzVMueBIGkDD2V6Ws5hFroiXjF4Aym7hYJtcI7x9FRR0dSOohPg%2F2wlyce95faHSMx1nyoJN2yXI810U3a7F97H2WIuPekxT74u7Fuj2Utw5icnpJVyFos7zrt30Xt6lfRh1tROwjpUJWZp5RH4U%2BOnNJSXOd1QEl%2Ba8YH6fUlMIu4%2F9IGOqUBcA8F8EhUBp9W66%2FRotMhc0WPkVVbTUX0eXF6kaDkFcu9amLESdAl%2BK1AnYfF1USVSusM7VghB99zf%2Fz3HBudb07BcNKMPgwIAto5dAAx6O7L18YWwpo7zCtF18k3coYn6m4Bfpv8oFzM8TFdmTZxlkdMhh5xb8%2Fvhg6LvGjKAvQ4eXZzhs7jcjOduJkUB9oKka9PGuGWHG4T51lb%2B7reofzRAX0u&X-Amz-Signature=db2c59171509a38b2282cd081cf2b06b7ac25b0e96eb085b9541a68072d95323&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

上节课我们已经对于可靠性投递的这个理论知识的讲解已经跟大家讲清楚了，那这节课呢？我们就来进入一些实现了。首先对于这个实现可能有一些基础的一些操作，比如说对数据库的操作，还有对一些连接池的配置，比如说 JDBC 连接池等等，那这些我个人觉得比较简单的，所以说老师就不再说一点点的，一行一行的去跟小伙伴们去手写了，核心逻辑还会去手写的。但是对于一些比较简单的这个 mybatis 操作，那我们就直接粘过来，然后跟小伙伴们把这个知识点讲清楚就可以了。

```java
        <dependency>
            <groupId>org.springframework.boot</groupId>
            <artifactId>spring-boot-starter-jdbc</artifactId>
            <version>1.5.6.RELEASE</version>
        </dependency>

        <dependency>
            <groupId>com.alibaba</groupId>
            <artifactId>druid</artifactId>
            <version>1.1.14</version>
        </dependency>

        <dependency>
            <groupId>mysql</groupId>
            <artifactId>mysql-connector-java</artifactId>
        </dependency>
```

首先我们可能需要用到数据库，那我们先引入相关的这个依赖，那我们再打开 common common 下面我们直接加入几个依赖在这里，老师把它直接粘过来就可以了。OK，加入这几个依赖，我们来看一下首先加入哪些。首先第一个就是我们的这个 JDBC 以及我们的这个Mybatis，接下来就是 druid 数据库连接池以及 MySQL 的这个 driver 驱动。OK，有了这几个包，我们对于这个数据库访问层就已经搞定了。然后接下来把它关闭，注意它是引到 common 了，然后 common 肯定是引到了这个 RabbitBrokerProducer 里边。


那接下来我们来看看它怎么去做嘛？首先第一点小伙伴们能够想到的就是说我们可能需要加一些配置，这些配置比如说配置我们的这个连接池配置一些这个 schema 就是我们的这个数据库的脚本，这些肯定都会有，那在这里我们直接把对应的配置跟小伙伴们说清楚。


第一个我们先把这个可靠性投递的语句跟小伙伴们来说一说，那在这里上节课老师已经说过了，我们除了有一个 biz 主表以外，我还是希望有一个这个专门存储消息投递的一个表，那么我直接就把这个文件 copy 过来，然后放到我们的这个 core-producer 它的 classpath 下，比如这个 resource 下，那我们之前有一个 mate infer 在这，我在 mate infer 评级粘过来一个SQL，那我们来打开看一下。


我们就用这个 text 方式打开，那这个就是一个数据库表结构在这里，这是老师之前导出来的，叫做 create table，然后这个 table 的名字叫做 broker 杠 message 什么意思？这就是记录我们的这个日志表，这里边有几个关键的字段，跟小伙伴们一起来说一说。

[image](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/87bc11bf-ebf2-4935-ad1e-927b738b98bc/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662Z6WHANW%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T225304Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIBSt%2BO0YcERoD6vSsmiwJQrIL39qBZuTt7dUu7y8FFabAiEAtUEPhwgwlvEKCK1AICQo4Pb3Ae%2FA6mtRaMQlo%2BjtH4MqiAQIxv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDM9FklCeH4jFXhdDYyrcA2uJ5dy2pvORSbannnIUq2emAoHkeZC6jpuyWRUEMci2yG6fxwjadbjj%2BaJ13JXwuC%2FTDASJK0MqvbFA%2F7N4cmQx3hCRzZ%2B56FjAjgYwbB0zdUOedabk6eOc1ItegCTq2hfhnkznitg8cpcFjs6hIaBWAFikw8HCMDmOtSwwU5aabRDtKGlaI26afc0IZH%2FeYxporQhhPlu0uqKnxsfm7bUqIOeachGpLyC9qZjuLCBAP1TRzjW%2FEtS4zUMEMumvFwdjvm%2BaNGeBqciF9lzIEhvHtVOm6zyiB7%2FZ%2BZMEq0cAIx3TQGguA5luYrjAAYn2iiRetyU53nj69nc7PGGMk0xVoQjCwGKK7DwAHa%2BR03jvESaXrerYPDyqrAIaAwOSAcVN97Qasle%2BSHipJNXh8QBZqRIUUjh%2F%2F14SPObEVLmRy4OGoLt75EoflgLS37daN3k3ailTS0p8EuaDpkbzVMueBIGkDD2V6Ws5hFroiXjF4Aym7hYJtcI7x9FRR0dSOohPg%2F2wlyce95faHSMx1nyoJN2yXI810U3a7F97H2WIuPekxT74u7Fuj2Utw5icnpJVyFos7zrt30Xt6lfRh1tROwjpUJWZp5RH4U%2BOnNJSXOd1QEl%2Ba8YH6fUlMIu4%2F9IGOqUBcA8F8EhUBp9W66%2FRotMhc0WPkVVbTUX0eXF6kaDkFcu9amLESdAl%2BK1AnYfF1USVSusM7VghB99zf%2Fz3HBudb07BcNKMPgwIAto5dAAx6O7L18YWwpo7zCtF18k3coYn6m4Bfpv8oFzM8TFdmTZxlkdMhh5xb8%2Fvhg6LvGjKAvQ4eXZzhs7jcjOduJkUB9oKka9PGuGWHG4T51lb%2B7reofzRAX0u&X-Amz-Signature=28e3fca20af9bb132982695a6bce8453af7249cefad3f6207a2ec517ed7799e4&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)


首先第一个关键字段就是我们的一个主键，就是 message 的ID，在这里看就是 message ID，主键 128 位，然后 none ，然后 message 是什么呢？这里边就是我们自己全量的消息的实际内容，我们可以缓存到这个 message 里，然后在这呢，这个 try_count 什么意思？就表示最大努力的尝试次数到底有几次？接下来就是这个state，那这个 state 说明的就是这个消息的状态，比如说我设置 0 表示待确认，就是相当于消息已经发出去了，但是我不知道到底有没有成功。 broker 给我返回  ACK 的时候，我再把 states 改成 1，表示已经证明投递成功。


然后如果说重试了多次，或者是说 Broker 返回失败了，那我可能不需要重试或者一些其他情况。根据业务需求，那我可能就是 state  给他更改为2，就表示已经投递失败，就是这条消息失败的时候，我们可能需要进行一个回滚。然后接下来下面这个三个字段都是跟日期有关的，我们来一点点说。首先第一个叫做 next_Retry，就表示下一次他应该尝试的时间。其实你叫 next Retry 也可以，或者叫做limit_next 都可以。 limit 的 try 什么意思？举个例子，比如说我当前 9 点一刻发了一条消息，然后我认为 5 分钟之后，如果这个消息的状态还是等于 0 的，就证明可能 ACK 没有回来，对吧？那么我是不是这个 next retry 就可以制成 9: 20 了？有 9: 20 的时候我发现他的 states 还是0，那证明什么呢？证明它是一个中间状态，没有回到ACK，那我们就应该把 states 等于0，并且它的时间大于 9: 20 的数据全抽取出来，这肯定是通过定时任务，然后我们再集体的去把这些数据再重新的去投递给我们的这个MQ，比如broker。


那这个就是关于重试的时候，我们需要用到两个比较关键的字段，就是我们的 next retry 跟这个space，那具体说重试了很多次，那我们总得有个上限，所以说如果重试三次或者重试五次以上还是失败的话，那我们就可以把这次制成为 2 了。就是已经确定失败了，然后我们要执行一些回滚逻辑了。


所以说这个 try count，这个state，以及这个 next retry 可能都需要 create_time，就是我们第一次入库的时间，每次我修改了，比如说我肯定会修改count，每次重新投递一次，我肯定改一下count，对吧？所以说针对于我每次修改我就有一个 update time，就是一个更新时间。


OK，那这个就是我们整个的这个数据库表结构了，那在这表结构搞定了之后，接下来的事情是什么呢？接下来这事情就是相当于我们需要用到 DB 存储，就是数据库，那首先我们都知道跟 mix 整合，那我们来一起写一写最好，其实后面我能够让他去做到这个语句，当我服务器一启动的时候，就我的应用程序一启动的时候，就会帮我去自动去创建这个 broke message 表，只要它没存在我们的指定的数据库中的时候就会帮我们创建。那如果说什么呢？如果说它已经存在了，那就不要帮我创建，那这个语句也是这样的， if not exist 才会去 create on the broker message。


OK，那对应着其实老师已经把数据库打开了，那我们现在有一个叫做 broker 杠 message 的这么一个数据库看见了，但是这里边没有任何表，这个表是空的。在这里后面我们通过这个 sprint boot 去写代码，让它自动的去帮我们 generator 这个表。


好，接下来我们来关注一下 producer 我们应该怎么去写。首先在这里我们继续去 producer 去写个代码，比如说写一个 common config，然后咱们叫做 database 嘛。好，然后接下来我肯定还会写一些具体的包，比如说 config database，就是关于数据库的一些配置了，比如说 spring boot 如何去跟 Mybatis 集成，然后它有实体，我们直接叫做entity。好，实体类entity，然后比如说它还有一些像 my voice，它肯定有do，就是一般就叫做map，所以说我们还会有一个Mapper。


然后如果你习惯什么呢？如果你习惯 Xmail 的方式的话，那是不是还会有一个 Mapping 在这里？这个 Mapping 其实我已经说过无数次了，一般来讲你可能会把它放到我们的 classpath 下去见，但是我们做测试我就把它都写到一起了，这样的话方便小伙伴们一起去看，只不过写到一起了，在你打包的时候，就是你打 maven 包的时候，你一定千万要记得把这个 Xml 的文件或者是 properties 文件都打进来，如果打不进来的话也会出异常。


虽然说运行能运行起来，就是你单独的通过这个 idea 或者是 eclipse 去运行是 OK 的，但是你打完包之后发现起不来缺少什么 Mapping 文件，就证明你打包的时候 Xmail 文件可能没有被打进来，这个是一个小细节点，希望小伙伴们注意。那其实我们建好了这几个包之后，接下来我们开始填内容了，我提前把它已经搞定了，所以说我们在这就是直接给小伙伴们来讲一下就可以了。


首先我举个例子，第一个就是我们的这个实体类，比如说我这个叫做 broker message，那它应该放到 entity 下面，在这里我已经把它粘过来，因为这个代码我觉得没必要去写，完全是浪费小伙伴们时间。我们看到了对应着跟数据库表是一样的，比如说我们的 message ID 主键全量的 message 信息，这个 message 信息看见了吗？就是我们最开始定义的这个rabbit，点 a p i 点 message 它的这个对象，我们后面会把它序列化，然后我们的try，count， integer 类型的，然后 state 就是我们的状态 next retry 下一次重试的时间，然后 create time 以及 update time。


OK，那这个数据结构已经 OK 了，就是我们的消息记录表已经搞定了。那接下来的事情是什么呢？接下来的事情就是我们的这个 map 以及mapping，那 map 在这里我也已经有了，把它直接粘过来。 map 我给它定义了几个。首先它肯定是用到了这个mabetas，所以说要声明一下 mabetas 的几个Mapper，其实你用什么？ at component，还有说 repository 或者 service 都可以。


OK，那既然数据库我们来用一下这个Mapper，然后它有几个关键的方法，我们看到了有这么多，后面这些，从这个 update by prime t 后面这几个可能都是我自己后来后加的一些对应的方法，那这个我们后面再讲的时候再跟小伙伴们说，我们暂时不去理会，往下走。


接下来就是Mapping，接下来 Mapping 的话我们来看一看，我把 Mapping 也拿过来。 Mapping 的话，那我在这里叫什么？叫做 broker message Mapper，只不过这个是什么？点 Xmail 了，或者叫 Mapping 点 Xmail 都可以。


OK，那这个同学们一起看啊，这个就是一个完全的 Xmail 文件了，然后它的 Mapper 是我们的这个 broker message Mapper，它的这个具体的实例类就是我们的这个producer，点 entity 点 broker message，然后还有一些其他相关的，这都是我们这工具帮我们去自动生成的，我们先不用去管它，然后后面有几个语句是我自己手写的。


OK，那我们后面再讲的时候再详细去说，我们暂时继续往下去走。现在我们关键不是去讲这个具体逻辑怎么实现，而是把我们整个的这个框架先搭好，后面我们一点一点去讲，然后主要就是这个 data base 了，就是GDBC，对吧？那既然有GDBC，是不是我们先应该想一想这个 GDBC 它的配置是什么？应该怎么去做？这是比较关键的。所以说在这里老师继续去来把 GDBC 相关的这个配置粘过来，那其实我们要连GDBC，那在这里我们把这个配置直接 copy 过来，叫做 rabbit 杠producer，杠message，点practice，那这个 purpose 呢？我们来看一下，打开看，首先我们用的是trade，就是阿里巴巴的这个 trade 数据源，然后它的这个 type 就是阿里巴巴的这个 trade data source，然后它的数据库连接叫GDBC，点MySQL，点 local host 3306。然后数据库名叫做 broker message，这个跟我在这里的是一致的，其实小伙伴们你在自己课下去做的时候，你要跟我保持一致就好了，你也建一个这样的数据库，因为数据库得提前去有。


然后接下来后面的事情就是对应的字符集，还有一些其他的东西了，那我们继续往下看，这是我们的 MySQL 的driver，然后我们的用户名密码都是root，以及一些坠的，它对应的一些配置，看到了吗？一些什么初始化的size，最小连接、最大连接、空闲连接、等待连接，一些其他的配置项，没什么可说的，那后面呢？其实我们就读取这个配置就可以了，对吧？这就是我们的这个关于数据库 GDBC 的一个配置项。那既然我们已经有配置项，有 schema 了，已经有映射，然后有 map 以及对应的 Xmail 文件，这些都准备好了，那最后一件事情是什么呢？最后一件事情无非就是我们要对 config date source 进行一个代码的讲解了，那关于这个就是整个的 config database，这个 database 我一共写了 4 个类，在这里我整体都粘过来，跟小伙伴一起说一说。

[file](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/4d897007-aa91-486a-8a6a-c57cda45e7d5/BrokerMessageConfiguration.java?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662Z6WHANW%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T225304Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIBSt%2BO0YcERoD6vSsmiwJQrIL39qBZuTt7dUu7y8FFabAiEAtUEPhwgwlvEKCK1AICQo4Pb3Ae%2FA6mtRaMQlo%2BjtH4MqiAQIxv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDM9FklCeH4jFXhdDYyrcA2uJ5dy2pvORSbannnIUq2emAoHkeZC6jpuyWRUEMci2yG6fxwjadbjj%2BaJ13JXwuC%2FTDASJK0MqvbFA%2F7N4cmQx3hCRzZ%2B56FjAjgYwbB0zdUOedabk6eOc1ItegCTq2hfhnkznitg8cpcFjs6hIaBWAFikw8HCMDmOtSwwU5aabRDtKGlaI26afc0IZH%2FeYxporQhhPlu0uqKnxsfm7bUqIOeachGpLyC9qZjuLCBAP1TRzjW%2FEtS4zUMEMumvFwdjvm%2BaNGeBqciF9lzIEhvHtVOm6zyiB7%2FZ%2BZMEq0cAIx3TQGguA5luYrjAAYn2iiRetyU53nj69nc7PGGMk0xVoQjCwGKK7DwAHa%2BR03jvESaXrerYPDyqrAIaAwOSAcVN97Qasle%2BSHipJNXh8QBZqRIUUjh%2F%2F14SPObEVLmRy4OGoLt75EoflgLS37daN3k3ailTS0p8EuaDpkbzVMueBIGkDD2V6Ws5hFroiXjF4Aym7hYJtcI7x9FRR0dSOohPg%2F2wlyce95faHSMx1nyoJN2yXI810U3a7F97H2WIuPekxT74u7Fuj2Utw5icnpJVyFos7zrt30Xt6lfRh1tROwjpUJWZp5RH4U%2BOnNJSXOd1QEl%2Ba8YH6fUlMIu4%2F9IGOqUBcA8F8EhUBp9W66%2FRotMhc0WPkVVbTUX0eXF6kaDkFcu9amLESdAl%2BK1AnYfF1USVSusM7VghB99zf%2Fz3HBudb07BcNKMPgwIAto5dAAx6O7L18YWwpo7zCtF18k3coYn6m4Bfpv8oFzM8TFdmTZxlkdMhh5xb8%2Fvhg6LvGjKAvQ4eXZzhs7jcjOduJkUB9oKka9PGuGWHG4T51lb%2B7reofzRAX0u&X-Amz-Signature=e04ee41ad2e729fba7eb0c107b95425ed0ff1bc48037f3a8693d3325d5723bf2&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

[file](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/2b234f47-546f-4f1e-8315-9e3cdd60b516/RabbitProducerDataSourceConfiguration.java?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662Z6WHANW%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T225304Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIBSt%2BO0YcERoD6vSsmiwJQrIL39qBZuTt7dUu7y8FFabAiEAtUEPhwgwlvEKCK1AICQo4Pb3Ae%2FA6mtRaMQlo%2BjtH4MqiAQIxv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDM9FklCeH4jFXhdDYyrcA2uJ5dy2pvORSbannnIUq2emAoHkeZC6jpuyWRUEMci2yG6fxwjadbjj%2BaJ13JXwuC%2FTDASJK0MqvbFA%2F7N4cmQx3hCRzZ%2B56FjAjgYwbB0zdUOedabk6eOc1ItegCTq2hfhnkznitg8cpcFjs6hIaBWAFikw8HCMDmOtSwwU5aabRDtKGlaI26afc0IZH%2FeYxporQhhPlu0uqKnxsfm7bUqIOeachGpLyC9qZjuLCBAP1TRzjW%2FEtS4zUMEMumvFwdjvm%2BaNGeBqciF9lzIEhvHtVOm6zyiB7%2FZ%2BZMEq0cAIx3TQGguA5luYrjAAYn2iiRetyU53nj69nc7PGGMk0xVoQjCwGKK7DwAHa%2BR03jvESaXrerYPDyqrAIaAwOSAcVN97Qasle%2BSHipJNXh8QBZqRIUUjh%2F%2F14SPObEVLmRy4OGoLt75EoflgLS37daN3k3ailTS0p8EuaDpkbzVMueBIGkDD2V6Ws5hFroiXjF4Aym7hYJtcI7x9FRR0dSOohPg%2F2wlyce95faHSMx1nyoJN2yXI810U3a7F97H2WIuPekxT74u7Fuj2Utw5icnpJVyFos7zrt30Xt6lfRh1tROwjpUJWZp5RH4U%2BOnNJSXOd1QEl%2Ba8YH6fUlMIu4%2F9IGOqUBcA8F8EhUBp9W66%2FRotMhc0WPkVVbTUX0eXF6kaDkFcu9amLESdAl%2BK1AnYfF1USVSusM7VghB99zf%2Fz3HBudb07BcNKMPgwIAto5dAAx6O7L18YWwpo7zCtF18k3coYn6m4Bfpv8oFzM8TFdmTZxlkdMhh5xb8%2Fvhg6LvGjKAvQ4eXZzhs7jcjOduJkUB9oKka9PGuGWHG4T51lb%2B7reofzRAX0u&X-Amz-Signature=c21d7533ef0659df2a8458b24815a664316d03b1c608504eda1cfa0233d67b7b&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

[file](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/e36015a9-8e2f-4427-b178-f3506672705a/RabbitProducerMyBatisConfiguration.java?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662Z6WHANW%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T225304Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIBSt%2BO0YcERoD6vSsmiwJQrIL39qBZuTt7dUu7y8FFabAiEAtUEPhwgwlvEKCK1AICQo4Pb3Ae%2FA6mtRaMQlo%2BjtH4MqiAQIxv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDM9FklCeH4jFXhdDYyrcA2uJ5dy2pvORSbannnIUq2emAoHkeZC6jpuyWRUEMci2yG6fxwjadbjj%2BaJ13JXwuC%2FTDASJK0MqvbFA%2F7N4cmQx3hCRzZ%2B56FjAjgYwbB0zdUOedabk6eOc1ItegCTq2hfhnkznitg8cpcFjs6hIaBWAFikw8HCMDmOtSwwU5aabRDtKGlaI26afc0IZH%2FeYxporQhhPlu0uqKnxsfm7bUqIOeachGpLyC9qZjuLCBAP1TRzjW%2FEtS4zUMEMumvFwdjvm%2BaNGeBqciF9lzIEhvHtVOm6zyiB7%2FZ%2BZMEq0cAIx3TQGguA5luYrjAAYn2iiRetyU53nj69nc7PGGMk0xVoQjCwGKK7DwAHa%2BR03jvESaXrerYPDyqrAIaAwOSAcVN97Qasle%2BSHipJNXh8QBZqRIUUjh%2F%2F14SPObEVLmRy4OGoLt75EoflgLS37daN3k3ailTS0p8EuaDpkbzVMueBIGkDD2V6Ws5hFroiXjF4Aym7hYJtcI7x9FRR0dSOohPg%2F2wlyce95faHSMx1nyoJN2yXI810U3a7F97H2WIuPekxT74u7Fuj2Utw5icnpJVyFos7zrt30Xt6lfRh1tROwjpUJWZp5RH4U%2BOnNJSXOd1QEl%2Ba8YH6fUlMIu4%2F9IGOqUBcA8F8EhUBp9W66%2FRotMhc0WPkVVbTUX0eXF6kaDkFcu9amLESdAl%2BK1AnYfF1USVSusM7VghB99zf%2Fz3HBudb07BcNKMPgwIAto5dAAx6O7L18YWwpo7zCtF18k3coYn6m4Bfpv8oFzM8TFdmTZxlkdMhh5xb8%2Fvhg6LvGjKAvQ4eXZzhs7jcjOduJkUB9oKka9PGuGWHG4T51lb%2B7reofzRAX0u&X-Amz-Signature=61b6f4ede076efdec2311d470692466cc8ff2e34e1720119a9516619c124cd2a&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

[file](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/8aa51d57-6b7e-4279-addd-88b8ef89f1de/RabbitProducerMybatisMapperScanerConfig.java?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662Z6WHANW%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T225304Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIBSt%2BO0YcERoD6vSsmiwJQrIL39qBZuTt7dUu7y8FFabAiEAtUEPhwgwlvEKCK1AICQo4Pb3Ae%2FA6mtRaMQlo%2BjtH4MqiAQIxv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDM9FklCeH4jFXhdDYyrcA2uJ5dy2pvORSbannnIUq2emAoHkeZC6jpuyWRUEMci2yG6fxwjadbjj%2BaJ13JXwuC%2FTDASJK0MqvbFA%2F7N4cmQx3hCRzZ%2B56FjAjgYwbB0zdUOedabk6eOc1ItegCTq2hfhnkznitg8cpcFjs6hIaBWAFikw8HCMDmOtSwwU5aabRDtKGlaI26afc0IZH%2FeYxporQhhPlu0uqKnxsfm7bUqIOeachGpLyC9qZjuLCBAP1TRzjW%2FEtS4zUMEMumvFwdjvm%2BaNGeBqciF9lzIEhvHtVOm6zyiB7%2FZ%2BZMEq0cAIx3TQGguA5luYrjAAYn2iiRetyU53nj69nc7PGGMk0xVoQjCwGKK7DwAHa%2BR03jvESaXrerYPDyqrAIaAwOSAcVN97Qasle%2BSHipJNXh8QBZqRIUUjh%2F%2F14SPObEVLmRy4OGoLt75EoflgLS37daN3k3ailTS0p8EuaDpkbzVMueBIGkDD2V6Ws5hFroiXjF4Aym7hYJtcI7x9FRR0dSOohPg%2F2wlyce95faHSMx1nyoJN2yXI810U3a7F97H2WIuPekxT74u7Fuj2Utw5icnpJVyFos7zrt30Xt6lfRh1tROwjpUJWZp5RH4U%2BOnNJSXOd1QEl%2Ba8YH6fUlMIu4%2F9IGOqUBcA8F8EhUBp9W66%2FRotMhc0WPkVVbTUX0eXF6kaDkFcu9amLESdAl%2BK1AnYfF1USVSusM7VghB99zf%2Fz3HBudb07BcNKMPgwIAto5dAAx6O7L18YWwpo7zCtF18k3coYn6m4Bfpv8oFzM8TFdmTZxlkdMhh5xb8%2Fvhg6LvGjKAvQ4eXZzhs7jcjOduJkUB9oKka9PGuGWHG4T51lb%2B7reofzRAX0u&X-Amz-Signature=61fe329790b29f68e6a12c66e3ffe09f69975acfc56af360db3693fe32bfaaa6&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

[file](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/c4874dd3-6a97-414c-ad7c-0be89e65c814/BrokerMessageMapper.xml?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662Z6WHANW%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T225304Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIBSt%2BO0YcERoD6vSsmiwJQrIL39qBZuTt7dUu7y8FFabAiEAtUEPhwgwlvEKCK1AICQo4Pb3Ae%2FA6mtRaMQlo%2BjtH4MqiAQIxv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDM9FklCeH4jFXhdDYyrcA2uJ5dy2pvORSbannnIUq2emAoHkeZC6jpuyWRUEMci2yG6fxwjadbjj%2BaJ13JXwuC%2FTDASJK0MqvbFA%2F7N4cmQx3hCRzZ%2B56FjAjgYwbB0zdUOedabk6eOc1ItegCTq2hfhnkznitg8cpcFjs6hIaBWAFikw8HCMDmOtSwwU5aabRDtKGlaI26afc0IZH%2FeYxporQhhPlu0uqKnxsfm7bUqIOeachGpLyC9qZjuLCBAP1TRzjW%2FEtS4zUMEMumvFwdjvm%2BaNGeBqciF9lzIEhvHtVOm6zyiB7%2FZ%2BZMEq0cAIx3TQGguA5luYrjAAYn2iiRetyU53nj69nc7PGGMk0xVoQjCwGKK7DwAHa%2BR03jvESaXrerYPDyqrAIaAwOSAcVN97Qasle%2BSHipJNXh8QBZqRIUUjh%2F%2F14SPObEVLmRy4OGoLt75EoflgLS37daN3k3ailTS0p8EuaDpkbzVMueBIGkDD2V6Ws5hFroiXjF4Aym7hYJtcI7x9FRR0dSOohPg%2F2wlyce95faHSMx1nyoJN2yXI810U3a7F97H2WIuPekxT74u7Fuj2Utw5icnpJVyFos7zrt30Xt6lfRh1tROwjpUJWZp5RH4U%2BOnNJSXOd1QEl%2Ba8YH6fUlMIu4%2F9IGOqUBcA8F8EhUBp9W66%2FRotMhc0WPkVVbTUX0eXF6kaDkFcu9amLESdAl%2BK1AnYfF1USVSusM7VghB99zf%2Fz3HBudb07BcNKMPgwIAto5dAAx6O7L18YWwpo7zCtF18k3coYn6m4Bfpv8oFzM8TFdmTZxlkdMhh5xb8%2Fvhg6LvGjKAvQ4eXZzhs7jcjOduJkUB9oKka9PGuGWHG4T51lb%2B7reofzRAX0u&X-Amz-Signature=7c7d0efb0cf8da2161c01990a934de3c896e4290518feafa88c1de2ebcc60d6e&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

[file](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/af402e69-a953-4989-ad1a-798bec639874/BrokerMessageMapper.java?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662Z6WHANW%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T225304Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIBSt%2BO0YcERoD6vSsmiwJQrIL39qBZuTt7dUu7y8FFabAiEAtUEPhwgwlvEKCK1AICQo4Pb3Ae%2FA6mtRaMQlo%2BjtH4MqiAQIxv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDM9FklCeH4jFXhdDYyrcA2uJ5dy2pvORSbannnIUq2emAoHkeZC6jpuyWRUEMci2yG6fxwjadbjj%2BaJ13JXwuC%2FTDASJK0MqvbFA%2F7N4cmQx3hCRzZ%2B56FjAjgYwbB0zdUOedabk6eOc1ItegCTq2hfhnkznitg8cpcFjs6hIaBWAFikw8HCMDmOtSwwU5aabRDtKGlaI26afc0IZH%2FeYxporQhhPlu0uqKnxsfm7bUqIOeachGpLyC9qZjuLCBAP1TRzjW%2FEtS4zUMEMumvFwdjvm%2BaNGeBqciF9lzIEhvHtVOm6zyiB7%2FZ%2BZMEq0cAIx3TQGguA5luYrjAAYn2iiRetyU53nj69nc7PGGMk0xVoQjCwGKK7DwAHa%2BR03jvESaXrerYPDyqrAIaAwOSAcVN97Qasle%2BSHipJNXh8QBZqRIUUjh%2F%2F14SPObEVLmRy4OGoLt75EoflgLS37daN3k3ailTS0p8EuaDpkbzVMueBIGkDD2V6Ws5hFroiXjF4Aym7hYJtcI7x9FRR0dSOohPg%2F2wlyce95faHSMx1nyoJN2yXI810U3a7F97H2WIuPekxT74u7Fuj2Utw5icnpJVyFos7zrt30Xt6lfRh1tROwjpUJWZp5RH4U%2BOnNJSXOd1QEl%2Ba8YH6fUlMIu4%2F9IGOqUBcA8F8EhUBp9W66%2FRotMhc0WPkVVbTUX0eXF6kaDkFcu9amLESdAl%2BK1AnYfF1USVSusM7VghB99zf%2Fz3HBudb07BcNKMPgwIAto5dAAx6O7L18YWwpo7zCtF18k3coYn6m4Bfpv8oFzM8TFdmTZxlkdMhh5xb8%2Fvhg6LvGjKAvQ4eXZzhs7jcjOduJkUB9oKka9PGuGWHG4T51lb%2B7reofzRAX0u&X-Amz-Signature=fa2adc56b999daf4426a99264fbf73767089bb9a46d8acbe4483f82c67e3cfb0&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

[file](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/db46206e-634d-4de9-97da-3fddc4a01451/BrokerMessage.java?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662Z6WHANW%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T225304Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIBSt%2BO0YcERoD6vSsmiwJQrIL39qBZuTt7dUu7y8FFabAiEAtUEPhwgwlvEKCK1AICQo4Pb3Ae%2FA6mtRaMQlo%2BjtH4MqiAQIxv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDM9FklCeH4jFXhdDYyrcA2uJ5dy2pvORSbannnIUq2emAoHkeZC6jpuyWRUEMci2yG6fxwjadbjj%2BaJ13JXwuC%2FTDASJK0MqvbFA%2F7N4cmQx3hCRzZ%2B56FjAjgYwbB0zdUOedabk6eOc1ItegCTq2hfhnkznitg8cpcFjs6hIaBWAFikw8HCMDmOtSwwU5aabRDtKGlaI26afc0IZH%2FeYxporQhhPlu0uqKnxsfm7bUqIOeachGpLyC9qZjuLCBAP1TRzjW%2FEtS4zUMEMumvFwdjvm%2BaNGeBqciF9lzIEhvHtVOm6zyiB7%2FZ%2BZMEq0cAIx3TQGguA5luYrjAAYn2iiRetyU53nj69nc7PGGMk0xVoQjCwGKK7DwAHa%2BR03jvESaXrerYPDyqrAIaAwOSAcVN97Qasle%2BSHipJNXh8QBZqRIUUjh%2F%2F14SPObEVLmRy4OGoLt75EoflgLS37daN3k3ailTS0p8EuaDpkbzVMueBIGkDD2V6Ws5hFroiXjF4Aym7hYJtcI7x9FRR0dSOohPg%2F2wlyce95faHSMx1nyoJN2yXI810U3a7F97H2WIuPekxT74u7Fuj2Utw5icnpJVyFos7zrt30Xt6lfRh1tROwjpUJWZp5RH4U%2BOnNJSXOd1QEl%2Ba8YH6fUlMIu4%2F9IGOqUBcA8F8EhUBp9W66%2FRotMhc0WPkVVbTUX0eXF6kaDkFcu9amLESdAl%2BK1AnYfF1USVSusM7VghB99zf%2Fz3HBudb07BcNKMPgwIAto5dAAx6O7L18YWwpo7zCtF18k3coYn6m4Bfpv8oFzM8TFdmTZxlkdMhh5xb8%2Fvhg6LvGjKAvQ4eXZzhs7jcjOduJkUB9oKka9PGuGWHG4T51lb%2B7reofzRAX0u&X-Amz-Signature=e62b9fe4bf6fd45a4b7f499a85730d85418a1ce42ea87e94ea5e2350a03c29b8&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)


首先我们来看一看这几个类，第一个叫做什么叫做 broker message configuration，然后第二一个叫做什么 Rabbit producer data source configuration，看见了，然后还有一个叫做。 Rabbit producer. My badges. Configuration. Gym. Rabbit producer. My badges. My personality. scanner config 这么几个配置，那从哪开始？我们先点开它之后，你发现这个肯定不是我们想要的，这个 data source 已经注入进来了，所以说它肯定是我们最后去看的。那我们第一个应该看哪个？很明显就是跟数据源相关的，是不是叫做 Rabbit producer data source configuration？那我们来看一看，我把它最大化。首先它加了一个这个 configuration 注解就不用过多说明了，它下面有一个叫做 property source。什么意思？我要加载哪一个文件，对吧？ class pass 下的 rabbit 杠 producer 杠 message 点practice，那这个文件是哪个？其实就是这个嘛，对不对？其实就是我刚才刚讲过的这个文件，他去把这里边的配置项都加载到我们的这个 Java 应用里边。


好，然后在这里我定义了一个 at value 属性，把 Rabbit 点 producer 点 trade 点 type 定义好数据源的这个类型，我们的这个 data source type OK，然后接下来我有一个叫做primary，就是我的主键，就是相当于它是我主数据库，那它叫做 Rabbit producer data source。


这个数据源，这个 data source 我给它起个名字，以 Rabbit 点 producer 点 trade 点 GDBC 为前缀的所有的属性，比如说基本上我们的配置里都是以这个缀的点g、d、b、 c 为前缀的。 user name、password、u、 l driver，包括这些配置项都是以这个 rabbit 点 producer 点 trade 点 GBC 为前缀的。然后都给它加到什么呀？都给它加到这个 data source 数据源上，那这个配置其实很简单，我们请看就是我们的 data source builder 点create，你的 data source type 是什么呢？就是你的这个 trade 的这个tap，然后去做一个 build 操作，其他的属性都会以这个前缀的属性都会帮我去直接注入到我们的这个 data source 里，叫做 Rabbit produce data source。然后最后为了看一下注入成功没有，在这里我会把这个东西打印一下，看到我会把这个数据源打印出来。然后接下来就是我们获取我们的 primary date source 的一些对应的这个概赛方法了，对不对？看到了获取 primary date source 的practice，然后OK，这些都有。好了，那这个类就是证明什么呢？它是帮我们去读那个配置文件，然后把数据源帮我们去生成。


有了 data source 之后，接下来我们要做什么事情？接下来事情就是第二件事情，就是我们的 broker message configuration，就是再过来才有它，对不对？再过来才有它，之后注意它是怎么去写的？首先把我们刚才的那个，就是我们的那个 data source 给它 out where 进来，那他已经有了吗？我们直接可以 out well，然后接下来干什么事情？接下来既然这个名字叫做什么叫做 broker message configuration，其实你要写得更好一点，你就可以写 broker message table configuration，它主要做的事情是什么呢？你看到这个了你就知道了，叫做 Rabbit 杠 producer 杠 message schema 杠SQL，这什么意思？ source resource 相当于我们要把我们自己的这个配置脚本，就是这个 SQL 的这个配置脚本，我们要把它找到，然后并让它执行，对不对？其实这里边就是一个建表语句，那刚才老师也说了，我期望什么呢？我希望我这个应用程序只要一运行起来，这个表如果不存在在数据库中的话，就会帮我们去创建这一张表。


首先我们来看，首先把这个 resource 加载到这个点， SQL 文件加载进来之后，然后在这里我也打一行日志，就是看一看这个数据源有没有，就只有数据源有了之后就相当于你的 GBC 连接才连上了，然后你才能操作数据库，对不对？那这个时候我们去调用我们的这个 data source init leather 的这个对象，然后去给他 set data source， set 我们的数据源，让他去创建 GDBC 连接，对吧？接下来我们让他去执行我们的 date base，我们的这个 popular 就相当于要执行这个 SQL 语句了，就是这个脚本，这个执行的智能化。


在后面就是 private 这个方法，它 resource database populator，然后去 add script，对不对？把我们的资源加载进来之后，然后 add 进去，然后最后让他去执行一下，就是这么一个目的，在这里老师打出是他的目的是干什么呢？他的目的就是帮我们进行数据库表结构的创建，帮我执行什么 CQ 脚本？那帮我执行 CQ 脚本以后就 OK 了。然后接下来后面这两个类完全都是跟我们的这个 Mybatis 整合 spring boot 相关的了。首先我们来看一看，第一个叫做 Rabbit producer mavitious configuration，那这个呢？看它有一些前置条件，叫做 all to config after，就是必须要等到这个 data source 做完了之后，然后它才能做。为什么呢？你 date source 如果还没做完你就做它了，那肯定会爆控指针，对不对？因为你的这个 source 这个对象还没初始化出来，那你就让这个类型执行了，那这肯定不行。


所以说在这里有一个这个约束条件，是必须等我们的数据源搞定了之后你才能去做，这样的话我把它注入进来，对不对？注入进来之后干什么呢？在这里我有一个叫做 sequel session factory 的东西，对吧？这就没什么可说的了，跟我们自己写我们的这个 my best 整合 spring boot 也都是一样的。那其实就是创建数，创建 CQ session factory，然后设置数据源，最后去做一些其他相关的，比如说在这里我去设置什么。

Resource, cover your bfs.


producer 点Mapping，看见了 Mapping 点Xmail，就是说只要是这个 Mapping 目录下星点 Xmail 的，我都把它当成，因为我要跟我的这个 map 跟 Mapping 它应该对应上，让 mams 去解析。 CQ session factory 搞定了之后，如果说你需要事务的话，你要加一个这个东西，就是我们的这是 CQC template，就是这个模板，那它的名字叫做 Rabbit producer CQ session template，当然要事物的话你也可以有，你可以去加上事物，那在这里我就没有去加事物，那对应着这个 sequel session factory 我们已经说完了。那接下来就是我们扫描了。


scanner 扫描很简单，那这个也是有一个依赖关系的，你必须要等到 data source 搞定了之后，然后你才能加载，因为这里边用到了，因为这是什么叫做 producer data source configuration，土 reducer data source configuration，或者你这样也行。你比如说我把这个叫做 Rabbit producer my bytest conservation，你把它这个逻辑放成这个也可以，当我们的这个 my Betis config 日程搞定之后，然后再执行 my Betis map standard config。但是其实也无所谓，你改回来也行，就是只要数据源搞定了，其实也就可以做了。


这个倒没有什么太多的这个限制约束，那这是干什么呢？就是做一个 config 相当于我们获取 cqsession factory，你看我就是直接的都是 set set session fashion name，这个我其实是不用这个 c sequel session factory 的，所以说我没必要说非得要等到 sequel session factory 那个 configuration 初始化完了之后，然后再初始化，我只要有数据源就行，因为这里边它仅仅做的是一个 set 方法，就是我要指定我的 session factory 以及指定我的 base scan package，就是我们当前的 Com 点 BFX y 点Rabbit，点producer、点Mapper。


其实类似于这个东西，包括刚才我们看到的关于这个配置，我们其实也都可以写到我们的什么呀？我们的 application 点 practice 里，以前我们都是写到 application 点 practice 里的，现在我们为什么不写？其实我要跟你说，我们其实应该有一个什么呀？应该有一个 plication 点practice，这是我们 super boot 的一个最大的特点，要么就是 application 点 yarn 配置文件，要么就是 application 点 practice 配置文件，对吧？但是那为什么你没有去把这些东西写到这里？原因很简单，原因我把它这里写死了，就是这个东西我不想让业务方去改，就是我要对业务没有感知。


所以说其实理论上来讲，就包括这个配置，我其实都写到 application 点 practice 里，也可以让它解析为什么我单独创建文件，还有为什么里边那些配置我都是单独去自己在代码里这样去写的，因为我就想对业务无感知，或者我们单独再搞一个文件，把这些配置都写到文件里，然后去读那个文件也可以。你如果想要对业务无感知的话，你最好尽量不要放到 application 点 practice 或者是 application 点yarn，就是这么一个目的。


OK，那其实这几件事情做完了之后，基本上来讲我就可以说我们当前的什么呢？我们当前的 producer 这个跟 Mybatis 整合的这件事情已经搞定了。那有同学说老师搞定了之后，我能不能自己测试一下音频起来？因为这个呢？你看最关键的是它是什么？ 

[image](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/7626f8d7-5261-4ea1-95f3-a135a541724f/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662Z6WHANW%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T225304Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIBSt%2BO0YcERoD6vSsmiwJQrIL39qBZuTt7dUu7y8FFabAiEAtUEPhwgwlvEKCK1AICQo4Pb3Ae%2FA6mtRaMQlo%2BjtH4MqiAQIxv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDM9FklCeH4jFXhdDYyrcA2uJ5dy2pvORSbannnIUq2emAoHkeZC6jpuyWRUEMci2yG6fxwjadbjj%2BaJ13JXwuC%2FTDASJK0MqvbFA%2F7N4cmQx3hCRzZ%2B56FjAjgYwbB0zdUOedabk6eOc1ItegCTq2hfhnkznitg8cpcFjs6hIaBWAFikw8HCMDmOtSwwU5aabRDtKGlaI26afc0IZH%2FeYxporQhhPlu0uqKnxsfm7bUqIOeachGpLyC9qZjuLCBAP1TRzjW%2FEtS4zUMEMumvFwdjvm%2BaNGeBqciF9lzIEhvHtVOm6zyiB7%2FZ%2BZMEq0cAIx3TQGguA5luYrjAAYn2iiRetyU53nj69nc7PGGMk0xVoQjCwGKK7DwAHa%2BR03jvESaXrerYPDyqrAIaAwOSAcVN97Qasle%2BSHipJNXh8QBZqRIUUjh%2F%2F14SPObEVLmRy4OGoLt75EoflgLS37daN3k3ailTS0p8EuaDpkbzVMueBIGkDD2V6Ws5hFroiXjF4Aym7hYJtcI7x9FRR0dSOohPg%2F2wlyce95faHSMx1nyoJN2yXI810U3a7F97H2WIuPekxT74u7Fuj2Utw5icnpJVyFos7zrt30Xt6lfRh1tROwjpUJWZp5RH4U%2BOnNJSXOd1QEl%2Ba8YH6fUlMIu4%2F9IGOqUBcA8F8EhUBp9W66%2FRotMhc0WPkVVbTUX0eXF6kaDkFcu9amLESdAl%2BK1AnYfF1USVSusM7VghB99zf%2Fz3HBudb07BcNKMPgwIAto5dAAx6O7L18YWwpo7zCtF18k3coYn6m4Bfpv8oFzM8TFdmTZxlkdMhh5xb8%2Fvhg6LvGjKAvQ4eXZzhs7jcjOduJkUB9oKka9PGuGWHG4T51lb%2B7reofzRAX0u&X-Amz-Signature=05cad6608298149aaf9ab5c54c865b726800725557239c87fcd0cdad0143ba28&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

auto configuration，就是它是被别人装配进来的，自动装配进来的。所以说就是说我们只能干什么呀？我们只能把它去帮我去注入到其他的应用服务里，当成一个自动装配的一个包，去给他去初始化，然后去做一些其他事情。如果你想去做的话，你完全现在可以随便建一个工程，然后把这个包引进去，然后那个工程肯定是一个 spring 的 boot 工程，启动一下，看一看启动有没有异常就可以了。那这个工作我觉得还是非常简单的，在这里我就不详细的跟大家去演示了。然后这节课呢，其实我们已经把对应的一些基础环境都已经搞定了，下节课我们再进行编码。那么感谢小伙伴们收看这节课，就先到这。



