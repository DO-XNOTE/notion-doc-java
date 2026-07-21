---
title: 3-2 RabbitMQ基础组件模块划分
---

# 3-2 RabbitMQ基础组件模块划分

[image](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/697979aa-98e3-4bc9-b123-0929abfb8b94/SCR-20240806-ojfm.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662TCXUE6J%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T225258Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCW1K1gyqKYM53Wj2n0Dz7WkCRWR9KBaSdYMz77ObV1LwIhAPKbhfXMNkoyxk8%2F6NWhkoaNRz0jPFPoBb4r7dgXgdo8KogECMb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgyGJvNXgeA5rXbAmOYq3ANRVi1xMuyyLmrnMLqexDDOAYQ40XgDS85khLJN9VXx4Qz3lTsf6GHEv2qYudeURYjqAZtGWrVKKddXF2ru5UGJXPbAkTSF8jMXQaiHoT9oxDUb5zWct0KzRB8b%2Ftvf1GcAaUxcUW9mCil08TfFMTt47yPek5TXDd%2FbyCyaY2V03ISNic54iqPfAJtCgpxRL0X%2F8j%2BBTLTRMyPqaYFfGjl1mI01%2FZa6zmYzssD1zfSaFwzQH%2F2Is%2F7xSOJbTQdgtU3NIcrttR6xPGMbqzstVdt1PK1dY96osK0jFhWCMm%2F%2FqGejxMnlUNsBrL3ElsnJNQIbA288gLNTydaGzCfosSBN9uWLh2BsW6ktoKk4%2Brj73Z4yjiaxv9PuyTnSueJtKhlSL2FYfKIzhbDQyNMIs4nuOPNSQJvTBo0dHX3wY%2B69OTS6DLhpJ8NeGUBIFlBkwuamliAaoPbGNVgJ0nzUkm6kAG%2Fn3qIPTjqRzyIZXWbdyS2uzXbD7v7kjVUYCk4G6ux0ETFIBdz4MWpTXX80vcGvMfg88%2F%2FyyW%2FqZ7hsuVqNyW%2F02K%2FZeXf94hM7wvov524Z4KTHw%2FlyXBlGY4%2Bu4cVJg6nFJQx2soIiXQ5xN21LcXU8gM5ymc2CCfeSaDC8uP%2FSBjqkAXwBvxjdjZmjJUbeuk9iiBZhfW5qpg5vB1%2F%2Bse9alnxiFje4sgMgX%2FvcfaKcCi6Wf2jA%2BvOtDHcVb6PUf73MWfFPSsKkxajeY%2FvVdodS6gCcJQC93XbCvZP5srRXF6zyOE6V2CWw5Ykc956au7ZIRrcH5AWvVYIGHl%2FmHgBPZL%2FDOwpNMvYAu6NNlk%2FLM8MQbt8uHoLNWblRaaBNGUuU%2BUmu%2Fn9u&X-Amz-Signature=eeca0231603605bb586475f57beb3f818328f6fe3b7aa18c4ebf45c636758acb&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

[image](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/47ac9e23-a1db-4f46-bc91-30ee45f641f5/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662TCXUE6J%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T225258Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCW1K1gyqKYM53Wj2n0Dz7WkCRWR9KBaSdYMz77ObV1LwIhAPKbhfXMNkoyxk8%2F6NWhkoaNRz0jPFPoBb4r7dgXgdo8KogECMb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgyGJvNXgeA5rXbAmOYq3ANRVi1xMuyyLmrnMLqexDDOAYQ40XgDS85khLJN9VXx4Qz3lTsf6GHEv2qYudeURYjqAZtGWrVKKddXF2ru5UGJXPbAkTSF8jMXQaiHoT9oxDUb5zWct0KzRB8b%2Ftvf1GcAaUxcUW9mCil08TfFMTt47yPek5TXDd%2FbyCyaY2V03ISNic54iqPfAJtCgpxRL0X%2F8j%2BBTLTRMyPqaYFfGjl1mI01%2FZa6zmYzssD1zfSaFwzQH%2F2Is%2F7xSOJbTQdgtU3NIcrttR6xPGMbqzstVdt1PK1dY96osK0jFhWCMm%2F%2FqGejxMnlUNsBrL3ElsnJNQIbA288gLNTydaGzCfosSBN9uWLh2BsW6ktoKk4%2Brj73Z4yjiaxv9PuyTnSueJtKhlSL2FYfKIzhbDQyNMIs4nuOPNSQJvTBo0dHX3wY%2B69OTS6DLhpJ8NeGUBIFlBkwuamliAaoPbGNVgJ0nzUkm6kAG%2Fn3qIPTjqRzyIZXWbdyS2uzXbD7v7kjVUYCk4G6ux0ETFIBdz4MWpTXX80vcGvMfg88%2F%2FyyW%2FqZ7hsuVqNyW%2F02K%2FZeXf94hM7wvov524Z4KTHw%2FlyXBlGY4%2Bu4cVJg6nFJQx2soIiXQ5xN21LcXU8gM5ymc2CCfeSaDC8uP%2FSBjqkAXwBvxjdjZmjJUbeuk9iiBZhfW5qpg5vB1%2F%2Bse9alnxiFje4sgMgX%2FvcfaKcCi6Wf2jA%2BvOtDHcVb6PUf73MWfFPSsKkxajeY%2FvVdodS6gCcJQC93XbCvZP5srRXF6zyOE6V2CWw5Ykc956au7ZIRrcH5AWvVYIGHl%2FmHgBPZL%2FDOwpNMvYAu6NNlk%2FLM8MQbt8uHoLNWblRaaBNGUuU%2BUmu%2Fn9u&X-Amz-Signature=302221dcebad5282241f98f37284626be4c0687fac0a43159f305552e4b001b6&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

OK，小伙伴们，那么这节课呢？我们就开始真正的去进入基础组件封装的一个环节了。那首先我们还是来看一看上节课这个图吧，其实整个的需求就是我这一幅图。首先我要保证什么呀？保障迅速的。迅速这是什么概念？也就是说低延迟的，那迅速的是不是要保障我们的这个消息一定要可靠性？这个不一定，其实我们只要保障你有些不太重要的消息，是不是即使是偶尔丢了一条也无所谓。所以说我们首先要满足迅速低延迟这个需求。

[image](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/92eb1f03-371f-48ad-90db-b7bab3f88e88/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662TCXUE6J%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T225258Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCW1K1gyqKYM53Wj2n0Dz7WkCRWR9KBaSdYMz77ObV1LwIhAPKbhfXMNkoyxk8%2F6NWhkoaNRz0jPFPoBb4r7dgXgdo8KogECMb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgyGJvNXgeA5rXbAmOYq3ANRVi1xMuyyLmrnMLqexDDOAYQ40XgDS85khLJN9VXx4Qz3lTsf6GHEv2qYudeURYjqAZtGWrVKKddXF2ru5UGJXPbAkTSF8jMXQaiHoT9oxDUb5zWct0KzRB8b%2Ftvf1GcAaUxcUW9mCil08TfFMTt47yPek5TXDd%2FbyCyaY2V03ISNic54iqPfAJtCgpxRL0X%2F8j%2BBTLTRMyPqaYFfGjl1mI01%2FZa6zmYzssD1zfSaFwzQH%2F2Is%2F7xSOJbTQdgtU3NIcrttR6xPGMbqzstVdt1PK1dY96osK0jFhWCMm%2F%2FqGejxMnlUNsBrL3ElsnJNQIbA288gLNTydaGzCfosSBN9uWLh2BsW6ktoKk4%2Brj73Z4yjiaxv9PuyTnSueJtKhlSL2FYfKIzhbDQyNMIs4nuOPNSQJvTBo0dHX3wY%2B69OTS6DLhpJ8NeGUBIFlBkwuamliAaoPbGNVgJ0nzUkm6kAG%2Fn3qIPTjqRzyIZXWbdyS2uzXbD7v7kjVUYCk4G6ux0ETFIBdz4MWpTXX80vcGvMfg88%2F%2FyyW%2FqZ7hsuVqNyW%2F02K%2FZeXf94hM7wvov524Z4KTHw%2FlyXBlGY4%2Bu4cVJg6nFJQx2soIiXQ5xN21LcXU8gM5ymc2CCfeSaDC8uP%2FSBjqkAXwBvxjdjZmjJUbeuk9iiBZhfW5qpg5vB1%2F%2Bse9alnxiFje4sgMgX%2FvcfaKcCi6Wf2jA%2BvOtDHcVb6PUf73MWfFPSsKkxajeY%2FvVdodS6gCcJQC93XbCvZP5srRXF6zyOE6V2CWw5Ykc956au7ZIRrcH5AWvVYIGHl%2FmHgBPZL%2FDOwpNMvYAu6NNlk%2FLM8MQbt8uHoLNWblRaaBNGUuU%2BUmu%2Fn9u&X-Amz-Signature=b66bedae36e3c401af0ee196eec88eb24f9fc8e674765b6e283d5b34432a8fd6&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

第二一个它叫延迟，跟刚才那个低延迟不一样，就是说我的消息可以支持，比如说把消息发出去五分钟之后那边再收到，这可不可以？这也是可以的。还有第三点要保证一个消息的可靠性，那我希望我的生产端发出去的每一条消息，那我一定要保证它在我们的 RABMQ broker 上，那这三个特点其实就是三个功能点。然后接下来我们看我们的左侧说消息异步化，消息可以去变成这种异步的方式去发送，没必要去同步，对吧？以及也可以支持这种消息的序列化的机制，那这个就相当于去优化我们的这个消息的这个编解码或者序列化一个性能，对不对？我们是不是可以去按照自己的这种序列化手段对消息进行一个序列化？这个曾经现在是可以的。


接下来第三条就是我们的下面这块连接的池化，我们可以做一个连接池，类似于我们 connection 一样让它提高我们的这个性能，没必要说新来的一条消息，我们就需要创建一个 connection 去做一个连接，这个很明显是比较低效的。还有就提升我们的性能，那最后一个就是完备的补偿机制。


那对于 MQ 而言，其实有两个非常非常关键的概念，第一个就是可靠性，第二个就是我们的这个，比如说我们怎么去做幂等，那这个可能是后面的事情好了，我们就围绕着这个基础组件的功能呢，接下来我们去来做一做我们整体的架构设计和实现。打开我们的这个 idea 哈，老师用的是 s t s 哈，那我们记得我们最开始的时候已经讲了这个 red m q 跟 spring boot 整合了，哈，那接下来我们看一看我们怎么去做基础组件的封装。


首先你要考虑一点，就是现在我们要作为一个基础组件去开发那基础组件，其实我们在这里就创建一个 POM 这个工程，对不对？我们 6 件又建 6 一个我们的 Maven 项目，那我在这里就 6 一个 Maven project 就可以了。然后 great 在这里我可以给它起个名字，比如说咱们叫做Com，点 b f x y，点儿face，点儿Rabbit，可以，OK。然后 artifactor ID 我们可以给它起个名字叫做 Rabbit 杠parent，OK，然后下面我就直接就 finish 了，那这个就作为一个什么啊？作为一个不碰，然后我们把它去创建好，当然这个 producer 还有这个 consumer 我们其实可以暂时把它关掉了，它 close 掉，现在就一个。然后其实这个作为一个 POM 文件，它这里边可能都不需要了，把它都 delay 掉，也都删掉。然后这个 SRC 也不需要了，我都 delay 掉，然后我们只需要我们修改我们自己的 Pom 文件就可以了。


然后这个 Pom 文件其实老师之前已经有了，那我在这里直接就把它 copy 过来，然后跟着大家一起修改一下就可以了， over right，然后我们现在用的版本现在是二点幺点五，我记得我们的 group 是叫做Com，点 b x f y，点face，然后点什么Rabbit，然后他的这个 artifact ID 就叫做 Rabbit 杠 terrant OK。然后这个 name 其实无所谓了，我们都拿过来，然后以及 description 我们都不需要，把它这个都变成 copy 过来就行了。然后 version 呢？就是我们的零点一杠 snapshot 就可以了。

```java
<?xml version="1.0" encoding="UTF-8"?>
<project xmlns="http://maven.apache.org/POM/4.0.0"
         xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
         xsi:schemaLocation="http://maven.apache.org/POM/4.0.0 http://maven.apache.org/xsd/maven-4.0.0.xsd">
    <modelVersion>4.0.0</modelVersion>

    <groupId>com.bfxy.base.rabbit</groupId>
    <artifactId>rabbit-parent</artifactId>
    <version>1.0-SNAPSHOT</version>

    <modules>
        <module>rabbit-task</module>
        <module>rabbit-api</module>
        <module>rabbit-common</module>
        <module>rabbit-core-producer</module>
    </modules>

    <parent>
        <groupId>org.springframework.boot</groupId>
        <artifactId>spring-boot-starter-parent</artifactId>
        <version>2.1.5.RELEASE</version>
        <relativePath/>
    </parent>

    <properties>
        <project.build.sourceEncoding>UTF-8</project.build.sourceEncoding>
        <java.version>8</java.version>
        <fasterxml.uuid.version>3.1.4</fasterxml.uuid.version>
        <org.codehaus.jackson.version>1.9.13</org.codehaus.jackson.version>
        <druid.version>1.0.24</druid.version>
        <elastic-job.version>2.1.4</elastic-job.version>
        <guava.version>20.0</guava.version>
        <commons-lang3.version>3.3.1</commons-lang3.version>
        <commons-io.version>2.4</commons-io.version>
        <commons-collections.version>3.2.2</commons-collections.version>
        <curator.version>2.11.0</curator.version>
        <fastjson.version>1.1.26</fastjson.version>
    </properties>

    <dependencies>
        <dependency>
            <groupId>org.springframework.boot</groupId>
            <artifactId>spring-boot-starter</artifactId>
        </dependency>
        <dependency>
            <groupId>org.springframework.boot</groupId>
            <artifactId>spring-boot-starter-test</artifactId>
            <scope>test</scope>
        </dependency>
        <dependency>
            <groupId>org.projectlombok</groupId>
            <artifactId>lombok</artifactId>
            <scope>provided</scope>
        </dependency>
        <dependency>
            <groupId>com.google.guava</groupId>
            <artifactId>guava</artifactId>
            <version>${guava.version}</version>
        </dependency>
        <dependency>
            <groupId>org.apache.commons</groupId>
            <artifactId>commons-lang3</artifactId>
        </dependency>
        <dependency>
            <groupId>commons-io</groupId>
            <artifactId>commons-io</artifactId>
            <version>${commons-io.version}</version>
        </dependency>
        <dependency>
            <groupId>com.alibaba</groupId>
            <artifactId>fastjson</artifactId>
            <version>${fastjson.version}</version>
        </dependency>
        <!--对json格式的支持 -->
        <dependency>
            <groupId>org.codehaus.jackson</groupId>
            <artifactId>jackson-mapper-asl</artifactId>
            <version>${org.codehaus.jackson.version}</version>
        </dependency>
        <dependency>
            <groupId>com.fasterxml.jackson.core</groupId>
            <artifactId>jackson-databind</artifactId>
        </dependency>
        <dependency>
            <groupId>com.fasterxml.uuid</groupId>
            <artifactId>java-uuid-generator</artifactId>
            <version>${fasterxml.uuid.version}</version>
        </dependency>
    </dependencies>
</project>
```

好，基本上这个就 OK 了，保存一下，耐心等待一下他去下载相应的这个依赖，OK，现在我已经下完了，我们来打开这个 Pom 文件，简单浏览一下。首先我们用的是 2. 15 这个最新的这个 spring boot starter，就 parent 版本。然后接下来我们的这个一些 properties 配置，我们用到的一些常用，比如像 GA 瓦，包括这个我们后面可能会用到。这个 elected job，就是分布式定时任务当网的那个，OK，还有包括我们可能会，后面可能会用到我们这个一些这个 ZK 相关的，比如说阿帕奇的这个creator，我们都提前把它引进来了。


然后我们看一看它对应的一些dependency，其实在这里老师没有去做 dependency 那个management，我直接这样去做，因为其实我们为了就快速做一个项目，我就没必要说把这个东西都搞得特别正式。首先它有一些依赖，我就强制的把它依赖进来，比如说我们的 spring boot starter，还有我们这个 long book，以及我们的这个Gaia，包括我们的这个一些文件上传下载的，包括其实这个都无所谓了，可以不要了，好把它去掉。因为我们可能没有什么对于文件上传下载的需求。


OK，有 fail upload 去掉，然后关于IO，包括浪 3 包，这个是我们经常会去用的一些工具，包括我们的这个 fast JSON 以及我们的Jackson，这就是一些普通的一些炸包，我们都把基础的东西直接引进来好了。那接下来我们看一看我们怎么去分我们的模块，那这个是非常重要的，那这个 parent 它就是一个palm，一个空壳。那接下来我们就要做的一件事情就是我们要分哪些？我们右键把它maven，我们用一个这个module，对吧？首先我们看一看，我们 create 一个 simple project，然后这个 name 我们叫做 Rabbit girl，我们在这里叫什么呢？首先你最开始你想的就是可能我有一些公共的模块，对不对？比如说一些通用的工具类，那这些我们是需要一个common，可以我们有一个 common 模块需要引进来，大家可能都需要引的一些基础的，OK，next，然后 finish 第一个包有了，就是我们的common。然后第二个包我们再去看，我们再去进行分包。比如说我们有一个Rabbit，杠什么呢？因为我们这个是属于基础组件，是要提供给第三方去使用的，那其实我们应该给它通用的提供一套 API 出来，那这个很明显我相信大家都应该能想到，所以说我们有一个 API 包，然后接下来我们再看一看我们还需要哪些，然后剩下的就比较核心的了。


那我们这个组件我们要做哪些东西？我们首先最关键的一点就是说我们要对发送消息，比如说迅速的，还有带有延迟消息的，还有带有可靠性消息的这么几种模式。所以说我们解决的根本问题是对消息的这个发送类型做一个封装。OK，接下来我就写个名字叫做Rabbit，杠 how 杠producer，也就是说我们真正发消息，我们可以给他提供真正发消息的这个包。OK，然后我们finish，接下来在这里老师提前的去做一个简单的规划，那这个简单的规划我们在这里给它起个名字，这个名字我们就叫做它，为什么呢？我们叫做它为Rabbit，它是通用的，比如说我们的一些定时任务，我们一些对于可靠性投递，那你肯定得需要定时任务了，这是毋庸置疑的，那我们在这里我们写一个叫做task，或者是一个 worker 都可以。


那老师在这里就简写为task，就是用于做可靠性处理的一个包，到时候老师会跟大家一起讲一讲当当网的 elected job，然后讲完了之后我们再结合着 spring boot，对不对？其实就是结合着 spring framework，然后进行一个封装。那当然这个封装你现在用到 Rabbit 上面也可以，后面其实可以扩展到任何的你的业务上。比如说其实我现在起这个名字起的并不是特别好，因为我把它限制到什么了？我把它限制到这个 Rabbit 这个通用组件里了，后面完全我可以把它放到任何的组件里，它本身就是一个当网实现的 ES job 的一个封装。


OK，在这里我提前跟小伙伴们说清楚，我们只是说由于因为这个项目的演示，因为我们要做这个技术组件，所以说我把它名字归化为 Rabbit 杠task，后面这个 task 其实完全可以公共出来所有的组件去使用。好，我们去finish。OK，那其实我们现在整体的大模块已经定好了，就一共 4 个模块，API、common、 producer 以及task，对吧？那我们来看一下 parent 下面应该 modules 后面有 4 个，一个是 common API，包括 producer 以及task，对吧？好了，那这样的话我们整体的分包就已经搞定了。

```java
    <modules>
        <module>rabbit-task</module>
        <module>rabbit-api</module>
        <module>rabbit-common</module>
        <module>rabbit-core-producer</module>
    </modules>
```

那么我们再回忆一下这四个包主要都要做什么呢？首先 API 对外提供的统一的 API 接口，然后 common 就是一些公共的大家可能都需要用的。然后接下来这个producer，那就是我们的核心了， core producer，这是我们最核心的东西task，这个后面我们会讲 ES job 的时候会跟大家去把它封装一下。OK，那这节课主要就是跟大家把包分好，感谢小伙伴们收。


## 

