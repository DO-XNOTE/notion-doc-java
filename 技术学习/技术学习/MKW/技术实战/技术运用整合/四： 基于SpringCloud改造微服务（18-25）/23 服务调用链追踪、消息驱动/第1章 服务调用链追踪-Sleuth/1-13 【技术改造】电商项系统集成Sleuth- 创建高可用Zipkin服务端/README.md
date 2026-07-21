---
title: 1-13 【技术改造】电商项系统集成Sleuth- 创建高可用Zipkin服务端
---

# 1-13 【技术改造】电商项系统集成Sleuth- 创建高可用Zipkin服务端

[image](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/db121ec2-70ef-4dc4-b055-eede20b11c53/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SS5FCSLA%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T225804Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIAvTFe2TtWhOKNpDmOBYz5IW%2BqU2%2FeeKeqUiZxh2AvfoAiAL2Z11fyEnXrC9AYe9YdsAut12NQpqsqmaayptFAkOsiqIBAjG%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMEvw5Ajh4gEFyk6CEKtwDHqwhBHQkXablCrjI0SOoELWwhXB%2F8o779P13pBbSV4LccIMDoGqZmskfnBENkch3M7HkwpSge2BwdfRx4zKFDhf0RK8ZETVyZEQPVNcRSkVOxJnJNuyoMWNvdoehO%2BAK2ZoYTKX%2F9B%2BoShZn4LcxMXoXProZrdW1pKHnYF448P0tkmO5tzDkk1VqnHtRpJat3Ws4Xv3hfipMbOsFMmGJQt2vBshNC3E96Jdir4x5PXVE3hNhMEol4WRIwBVDgyMxDp%2BKyX9c1bgWcQKMg7vlkyr6y%2Bq4I5wHd%2FAFy4axT72jmlKw3gNhgUM%2Bks%2Fc0JkfPuHgh3KLPKNxSVCB8mbcWl8E5pPZI4UuYt02%2F6VfqOWC6ddzyVi16hm9FlZ%2FySRiYsGUMBgiHIl5joh%2BP4NhHmSz4uWFCTUWF5icmp%2Fwcsq7diz559zpsBHRee%2BnKG51S2yaegywygB7jVw2B933CVyi3dUpvYMUFb1qEtZZDvUTAYVBqUFDSYzdZwagj7Nn4DsLICt2EYTALd7bJSTkuDHBWB7ZCSBBaLnI2sVcmidHNHf9FEjIrdU3MuvcFVfUnKw5cNnpI%2FVWfTjf8V4Ylgu7cdajoDUSUv%2B5Sx44BFWVqOCVZEoNC%2FS5T7kw77r%2F0gY6pgHxdBLv2GZ6YeGh2hXpXOWtWeJMHbjTlZAZAWiP3aWLvZc6kWTlRV5jSo0b0w3THIyfsV4TYXooib1B5m%2BI9GNnq32WriXVv4T65hgzWA2v2yDBLTZJohqHAaXjCl6uID4iVw9YHdiPe6BQdDmVPO3niVavXm06Il4a1Umb9xicbJrerEm3wldkLgUmXCe2tP1NWjwAFPD2VROJiRZroRxUkDdKmLm9&X-Amz-Signature=2d531bc047f6a5dd55dd10936372acd2171b7595648c7646f4eaaf362558dace&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

hello 慕课网的各位同学们，大家好，我是小半仙，咱这一节开始就要做 sleutha 和我们的电商项目的集成工作了。那集成工作的第一步就是我们要创建一个 zipking 的服务端，那咱把目光移到这个 platform 文件夹下。咱在这个文件夹下要创建一个子的毛 9 okay 咱边说边创建。
那这一次的 zipking server 和之前咱创建的 zipking 有什么不同吗？大家注意到本节的题目它叫高可用的 zipkin server 那所谓高可用，不就是说一个 zipking 倒掉了千千万万个 zipkin 起来了。那我们在 spring cloud 当中的哪一个组件可以完成这个高可用的使命呢？同学们学完前面的章节可以举一反三啊。


啊我们在配置中心的时候，那是利用谁做高可用的 eureka 对不对？那我们这里也一样，通过 eureka 来完成 zipking server 的高可用改造。那我们在这个 palm 文件当中，把之前随堂练习里的 palm 配置还有依赖项都给它 copy 过来走。你好，我们来看一下。这里就是引用了一个 zipking server 还有 zipkin auto configuration uiok 那咱既然说到要用 eureka 来做高可用，那所以这里我们跟之前的 demo 不同的地方是要在依赖项的列表当中，把 eureka 给它引用进来。


好，咱注意，咱引用的是 eureka client 别大家不要引用成了 eureka server 好，那我们接着往下看，那这个 build 节点下面，我们把它的主类给它打上 come.eye mock.zip king applicationokay 好，那咱这个抛母键创建完了，接下来我们打开这个源码目录来创建它的启动类了。好，这里先给它打上 package 咱的独家冠名商 com.imock 点什么没有点了走。你好，在这里我们直接 copy 之前随堂 demo 里的启动类，原封不动地copy 。好过来的宁卫。 OK 那这里我们也要加一个注解，因为咱用 eureka 做高可用改造，所以这里要把 eureka 给它加入进来。 enable eureka client 好。


启动类配置好了之后，我们接下来就去创建一个配置文件。那这个配置文件和之前的随堂 demo 不同，我们这一次采用 YAML 格式来配置 YAML OK 那前面第一个自然是 spring 的 application 的名称。那我这里还是把它叫做谁叫做 zip king serverok 那接下来我们把这个 spring 里面允许并存在的配置给它加上。


好，那后面我们这里就可以去声明它的 server port 了。那我数一下，咱这个 platform 下面有 123456 已经有 6 个应用了，那他排老六老六的座次是20,005，咱是从 0 开始数的。 OK 那配置完这里，接下来就是谁咱 eureka 的配置，咱这个 eureka 我可以从其他应用当中把它 copy 一段。好，我们就选这个 user 应用，把 user domain 里的 eureka 配置在哪？在这里。好，我们把它给 copy 过来，然后放到 zip king 里面。好，那 eurika 添加完了之后，我们切换到之前的 demo 项目 zip king server 的这个随堂 demo 项目，再把它最后一个配置也给它移除过来。好，这里把它改成 YAML 的形式挨个缩进好，然后把这里改成冒号。 OK 那这里改好之后，咱的这个 zip king 就算已经是搭建完成了，不过咱这里采用的是一种最简单的方式。


怎么说最简单呢？咱 zipking 大家知道是接收你客户端发来的信息的对不对？那他接收的方式是什么呢？我们来看这个 pom 配置文件，你看这里没有引入任何其他的依赖对不对？所以咱的 zipkin 其实是采用这种形式来接收你的客户端发来的信息，什么形式呢？ web 也就是说客户端通过 http 这种方式把自己的链路信息发送给 zipkin 但是我们 zipkin 不仅支持 web 还支持什么呢？也可以支持这种方式 rabbitMQ 那使用咱的消息队列也是一种可以用来接收客户端信息的一种方式。


OK 如果同学们想使用 rabi MQ 来结束，那可以引用这样一个依赖，它开头也是叫 zip king auto configuration 那后面是叫 collector， collector 什么呢？ rabbitMQ 那同样的你接收到信息的，那你自然要把信息保存下来对不对？那咱这里除了使用默认的保存方式，我们也可以借助另外一种组件来保存信息。是谁呢？ ES 使用 elecstics search 来保存信息。那同样的 zip king ，对，它也有一个支持的 artifact 那我们相应的需要引入 auto configuration 下面叫 storage storage 后面是叫 elastic search http OK 那前面同学们已经系统地学过了 rabbitMQ 以及 elastic search 的用法。

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

    <artifactId>zipkin-server</artifactId>不够完整和具体

    <dependencies>
        <dependency>
            <groupId>io.zipkin.java</groupId>
            <artifactId>zipkin-server</artifactId>
            <version>2.8.4</version>
            <exclusions>
                <exclusion>
                    <groupId>org.apache.logging.log4j</groupId>
                    <artifactId>log4j-slf4j-impl</artifactId>
                </exclusion>
            </exclusions>
        </dependency>

        <dependency>
            <groupId>io.zipkin.java</groupId>
            <artifactId>zipkin-autoconfigure-ui</artifactId>
            <version>2.8.4</version>
            <exclusions>
                <exclusion>
                    <groupId>org.apache.logging.log4j</groupId>
                    <artifactId>log4j-slf4j-impl</artifactId>
                </exclusion>
            </exclusions>
        </dependency>

        <!--高可用-->
        <dependency>
            <groupId>org.springframework.cloud</groupId>
            <artifactId>spring-cloud-starter-netflix-eureka-client</artifactId>
        </dependency>

        <!-- WEB -->
        <!-- 也可以使用 Rabbitmq 节后客户端的信息 -->
        <!-- zipkin-autoconfigure-collector-rabbitmq -->
        <!-- 也可以借助 ES 来保存信息 -->
        <!-- zipkin-autoconfigure-storage-elasticsearch-http -->
    </dependencies>

    <build>
        <plugins>
            <plugin>
                <groupId>org.springframework.boot</groupId>
                <artifactId>spring-boot-maven-plugin</artifactId>
                <configuration>
                    <mainClass>com.imooc.ZipkinApplication</mainClass>
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

**如果您感兴趣，可以将它们应用到 zip kin 中，使我们的链路收集功能更加完备、高可用和健壮。因为这里只是接收和存储信息的方式不同，但道理是一样的，所以我们不采用这种复杂的配置方式，而是采用最简单的通过 HTTP 方式来接收信息，然后默认保存的方式。**

好的，到这里我们的 zipkin 就已经创建完毕了。我们启动它看看。将启动类拉出来，看到这里，zipkin 特有的丘比特射箭小人已经冒出来了。接下来，我们去浏览器里看一下我们的注册中心，刷新一下页面。zipkin 出现在了列表的最下端，我们一起去点击一下它后面的地址，看它是否可以将页面渲染出来。好的，我们可以去掉浏览器地址后面的 actuator 端点，非常完美。


我们可以完美收工了。在后面的小节里，我们将继续致力于电商项目的改造，将 smooth 的 zipkin 集成到我们的电商平台中。好的，同学们，我们下一个小节再见。






