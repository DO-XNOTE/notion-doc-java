---
title: 2-6 落地Nacos服务发现 - 搭建toilet-center进行服务注册-1
---

# 2-6 落地Nacos服务发现 - 搭建toilet-center进行服务注册-1

[image](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/f623d46d-453d-4844-96bf-7eb5d24bfb19/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666FSXQKMF%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T231309Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIEbzo6KPzIR9WqgRuB67gEk3WU3v2KmKd%2BzYmvg81riCAiAr931HVwFedgCN4On5%2F6clEfPcdd6punMJFI2sy%2FLEwCqIBAjG%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMf3JQX5GJhg9dbOCrKtwDUmrBEUJLWkdjUBKZQPQBijz8HCSjJESFfMINK8uqCSF9fVWV8VY5x0aTusfBo%2FT2wMII7wTTOb6Ouh%2FeDLbs14%2FYXj1XppcYzFSvTpkHjdubcfSXwJ6qlO35c9bRg7UY6bAhcIEP63EPGSO4t3tgJ86n532IHHi%2FlItlzVkkpVCQwDKDJM%2BDLFKAnNPg8yH0pZiu6vLaldSz%2FsTumDgDDeMRyJA%2FeNm6LjufHpNvTIVEyE0wm%2FyE8GJg91rQ6TTn9BJbR7EM4chrflSc2DFI3pwC9%2ByTsVBxpAFdhS%2F1dcSTSVtQDxMozsqpdz2bh6dXVqclvcbWu726xp16WTeT0J3Eko6VPp15LGAyESVFODlu72K9uBkpztksWaa%2FEd8Y58ixCiClzzBSVul%2FSKg3GjKXWSJZ7Hc8E7VB16XDtpVQfZYW%2BEVm0t5jQ5vP04A76oSTjMrH9ieJYn5tior4%2Fg8D2VdyU5YHDCPOH2DFAWhA78E0fFLhWtRmaQyK5je%2F%2FQ9UbRzy3u2XG%2BL9BefMTpxKNdXZZ0m%2Byzsix0CGgVKa8hwlO3hG1ZvJgPt4a%2F1AgGfWMIZt6gffvDVF44km5bvjpzrVZ7uyo6H29ZrgWd2NXlT69zhF7HcVfj0wt7j%2F0gY6pgFynhrac8OlrLxYn9%2B15wEET0LNcDv%2Bk1DzudJ%2FTF6Y8myugXu49dqrRTiCIwmrlH%2BBLbOfVjYEvi25zWkOBZ5Lf661p%2BiAEnpjbPI9RN%2FNvmgUpg6GX17WxepDwVc0aS1LO0YKW4OusMAEDD2FJWZ0BdQXh5XjwYWIcugYjvX2UMfpjoP0soM7CaRhrGJBMbxmupBNIH5inAOxWY2OgCYJu84%2Bk773&X-Amz-Signature=126ac1bba92c30675f875797214a646f0bd7e8c994a9703c9e1acdab057eb566&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

[image](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/a10e7711-a3bf-4a91-96fe-747a5d621670/SCR-20240801-pcso.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666FSXQKMF%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T231309Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIEbzo6KPzIR9WqgRuB67gEk3WU3v2KmKd%2BzYmvg81riCAiAr931HVwFedgCN4On5%2F6clEfPcdd6punMJFI2sy%2FLEwCqIBAjG%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMf3JQX5GJhg9dbOCrKtwDUmrBEUJLWkdjUBKZQPQBijz8HCSjJESFfMINK8uqCSF9fVWV8VY5x0aTusfBo%2FT2wMII7wTTOb6Ouh%2FeDLbs14%2FYXj1XppcYzFSvTpkHjdubcfSXwJ6qlO35c9bRg7UY6bAhcIEP63EPGSO4t3tgJ86n532IHHi%2FlItlzVkkpVCQwDKDJM%2BDLFKAnNPg8yH0pZiu6vLaldSz%2FsTumDgDDeMRyJA%2FeNm6LjufHpNvTIVEyE0wm%2FyE8GJg91rQ6TTn9BJbR7EM4chrflSc2DFI3pwC9%2ByTsVBxpAFdhS%2F1dcSTSVtQDxMozsqpdz2bh6dXVqclvcbWu726xp16WTeT0J3Eko6VPp15LGAyESVFODlu72K9uBkpztksWaa%2FEd8Y58ixCiClzzBSVul%2FSKg3GjKXWSJZ7Hc8E7VB16XDtpVQfZYW%2BEVm0t5jQ5vP04A76oSTjMrH9ieJYn5tior4%2Fg8D2VdyU5YHDCPOH2DFAWhA78E0fFLhWtRmaQyK5je%2F%2FQ9UbRzy3u2XG%2BL9BefMTpxKNdXZZ0m%2Byzsix0CGgVKa8hwlO3hG1ZvJgPt4a%2F1AgGfWMIZt6gffvDVF44km5bvjpzrVZ7uyo6H29ZrgWd2NXlT69zhF7HcVfj0wt7j%2F0gY6pgFynhrac8OlrLxYn9%2B15wEET0LNcDv%2Bk1DzudJ%2FTF6Y8myugXu49dqrRTiCIwmrlH%2BBLbOfVjYEvi25zWkOBZ5Lf661p%2BiAEnpjbPI9RN%2FNvmgUpg6GX17WxepDwVc0aS1LO0YKW4OusMAEDD2FJWZ0BdQXh5XjwYWIcugYjvX2UMfpjoP0soM7CaRhrGJBMbxmupBNIH5inAOxWY2OgCYJu84%2Bk773&X-Amz-Signature=3a2dbc7a437ff0ba2a6a7442a1825a2eccb2e4abcdb3bae0c71a7c4a82aa1da1&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

[image](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/9142d2f4-e2f8-4470-b47d-15e5671b8c48/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666FSXQKMF%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T231309Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIEbzo6KPzIR9WqgRuB67gEk3WU3v2KmKd%2BzYmvg81riCAiAr931HVwFedgCN4On5%2F6clEfPcdd6punMJFI2sy%2FLEwCqIBAjG%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMf3JQX5GJhg9dbOCrKtwDUmrBEUJLWkdjUBKZQPQBijz8HCSjJESFfMINK8uqCSF9fVWV8VY5x0aTusfBo%2FT2wMII7wTTOb6Ouh%2FeDLbs14%2FYXj1XppcYzFSvTpkHjdubcfSXwJ6qlO35c9bRg7UY6bAhcIEP63EPGSO4t3tgJ86n532IHHi%2FlItlzVkkpVCQwDKDJM%2BDLFKAnNPg8yH0pZiu6vLaldSz%2FsTumDgDDeMRyJA%2FeNm6LjufHpNvTIVEyE0wm%2FyE8GJg91rQ6TTn9BJbR7EM4chrflSc2DFI3pwC9%2ByTsVBxpAFdhS%2F1dcSTSVtQDxMozsqpdz2bh6dXVqclvcbWu726xp16WTeT0J3Eko6VPp15LGAyESVFODlu72K9uBkpztksWaa%2FEd8Y58ixCiClzzBSVul%2FSKg3GjKXWSJZ7Hc8E7VB16XDtpVQfZYW%2BEVm0t5jQ5vP04A76oSTjMrH9ieJYn5tior4%2Fg8D2VdyU5YHDCPOH2DFAWhA78E0fFLhWtRmaQyK5je%2F%2FQ9UbRzy3u2XG%2BL9BefMTpxKNdXZZ0m%2Byzsix0CGgVKa8hwlO3hG1ZvJgPt4a%2F1AgGfWMIZt6gffvDVF44km5bvjpzrVZ7uyo6H29ZrgWd2NXlT69zhF7HcVfj0wt7j%2F0gY6pgFynhrac8OlrLxYn9%2B15wEET0LNcDv%2Bk1DzudJ%2FTF6Y8myugXu49dqrRTiCIwmrlH%2BBLbOfVjYEvi25zWkOBZ5Lf661p%2BiAEnpjbPI9RN%2FNvmgUpg6GX17WxepDwVc0aS1LO0YKW4OusMAEDD2FJWZ0BdQXh5XjwYWIcugYjvX2UMfpjoP0soM7CaRhrGJBMbxmupBNIH5inAOxWY2OgCYJu84%2Bk773&X-Amz-Signature=cec39a2eeabd5ccc1346a3a1c97de3aea2f8b002a309a6016627ca2fac5aad5f&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

hello，幕货网的各位同学们大家好，我是姚半县，那咱们这一节呢，开始正儿八经的写代码了，我们继续 Nacos 的落地案例之搭建 restroom service 进行服务注册。那这里我们将用最快的速度跟同学们去落地一个 spring cloud 应用。因为咱的主角是 spring cloud，所以对于 spring boot 相关的基础知识这里就不进行深入的介绍了。

不过老师这里跟同学们要演示的是咱 spring boot 当中使用的主流技术，那同学们看一看是否我的这种方式可以帮你节省开发工作量？好，那接下来我们就转移到 Intelligi 里面，走起，那每天 coding 一小时，健康工作 50 年。同学们，这里看到我已经创建出了一个 Maven 的项目，那这里是它的根目录，我们给它的 group ID 起名叫做 come 点 imock artifact， ID 叫 spring boot 杠 project OK，接下来我们引入项目的依赖项来，不要眨眼 321 走好。


咋看引入了哪几项？第一个， springboot spring boot，这里对应的 version 我们可以在 properties 这里指定，那也可以直接就懒省事儿，咱写死在这里好了。 spring boot 是二点三点二，后面是 release 叠 release OK，那接下来 spring cloud 这个版本我们前面说过，是谁？ hokstone 点S28，好，那最后一个阿里巴巴组件库，它的版本二点三点 release OK，那我们这里使用的是什么标签？ dependency management 同学们还记得这个标签不是说实打实的把你上面的依赖项加入到当前项目当中，而是说他把上面的这个依赖项的版本信息加入进来。

```java
<?xml version="1.0" encoding="UTF-8"?>
<project xmlns="http://maven.apache.org/POM/4.0.0"
         xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
         xsi:schemaLocation="http://maven.apache.org/POM/4.0.0 http://maven.apache.org/xsd/maven-4.0.0.xsd">
    <modelVersion>4.0.0</modelVersion>

    <groupId>com.imooc</groupId>
    <artifactId>spring-cloud-proj</artifactId>
    <version>1.0-SNAPSHOT</version>

    <properties>
        <maven.compiler.source>8</maven.compiler.source>
        <maven.compiler.target>8</maven.compiler.target>
        <java.encoding>utf-8</java.encoding>
    </properties>

    <dependencyManagement>
        <dependencies>
            <dependency>
                <groupId>org.springframework.boot</groupId>
                <artifactId>spring-boot-dependencies</artifactId>
                <version>2.3.2.RELEASE</version>
                <type>pom</type>
                <scope>import</scope>
            </dependency>

            <dependency>
                <groupId>org.springframework.cloud</groupId>
                <artifactId>spring-cloud-dependencies</artifactId>
                <version>Hoxton.SR8</version>
                <type>pom</type>
                <scope>import</scope>
            </dependency>

            <dependency>
                <groupId>com.alibaba.cloud</groupId>
                <artifactId>spring-cloud-alibaba-dependencies</artifactId>
                <version>2.2.3.RELEASE</version>
                <type>pom</type>
                <scope>import</scope>
            </dependency>
        </dependencies>
    </dependencyManagement>

    <dependencies>
        <dependency>
            <groupId>org.projectlombok</groupId>
            <artifactId>lombok</artifactId>
            <version>1.18.24</version>
        </dependency>

        <dependency>
            <groupId>org.springframework.boot</groupId>
            <artifactId>spring-boot-starter-test</artifactId>
            <scope>test</scope>
        </dependency>
    </dependencies>

</project>
```

如果我们在接下来的子项目当中引用了相应的组件，那么这些组件的 version 信息我不用去指定，它可以自动从你父级目录的 dependency management 节点当中定义的这些组件版本里继承开来。比如说我这里想依赖next，那很简单， next 的版本从哪来？从这里面来，同学们看这里，这就是已经预先指定好的版本信息。好，相当于我在负级项目当中，在这个 POM 里把你的版本都已经给定义好了。

[image](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/695d9c7f-1de7-42c5-8d75-6f664ee06cba/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666FSXQKMF%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T231309Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIEbzo6KPzIR9WqgRuB67gEk3WU3v2KmKd%2BzYmvg81riCAiAr931HVwFedgCN4On5%2F6clEfPcdd6punMJFI2sy%2FLEwCqIBAjG%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMf3JQX5GJhg9dbOCrKtwDUmrBEUJLWkdjUBKZQPQBijz8HCSjJESFfMINK8uqCSF9fVWV8VY5x0aTusfBo%2FT2wMII7wTTOb6Ouh%2FeDLbs14%2FYXj1XppcYzFSvTpkHjdubcfSXwJ6qlO35c9bRg7UY6bAhcIEP63EPGSO4t3tgJ86n532IHHi%2FlItlzVkkpVCQwDKDJM%2BDLFKAnNPg8yH0pZiu6vLaldSz%2FsTumDgDDeMRyJA%2FeNm6LjufHpNvTIVEyE0wm%2FyE8GJg91rQ6TTn9BJbR7EM4chrflSc2DFI3pwC9%2ByTsVBxpAFdhS%2F1dcSTSVtQDxMozsqpdz2bh6dXVqclvcbWu726xp16WTeT0J3Eko6VPp15LGAyESVFODlu72K9uBkpztksWaa%2FEd8Y58ixCiClzzBSVul%2FSKg3GjKXWSJZ7Hc8E7VB16XDtpVQfZYW%2BEVm0t5jQ5vP04A76oSTjMrH9ieJYn5tior4%2Fg8D2VdyU5YHDCPOH2DFAWhA78E0fFLhWtRmaQyK5je%2F%2FQ9UbRzy3u2XG%2BL9BefMTpxKNdXZZ0m%2Byzsix0CGgVKa8hwlO3hG1ZvJgPt4a%2F1AgGfWMIZt6gffvDVF44km5bvjpzrVZ7uyo6H29ZrgWd2NXlT69zhF7HcVfj0wt7j%2F0gY6pgFynhrac8OlrLxYn9%2B15wEET0LNcDv%2Bk1DzudJ%2FTF6Y8myugXu49dqrRTiCIwmrlH%2BBLbOfVjYEvi25zWkOBZ5Lf661p%2BiAEnpjbPI9RN%2FNvmgUpg6GX17WxepDwVc0aS1LO0YKW4OusMAEDD2FJWZ0BdQXh5XjwYWIcugYjvX2UMfpjoP0soM7CaRhrGJBMbxmupBNIH5inAOxWY2OgCYJu84%2Bk773&X-Amz-Signature=d70438c87865f75be4e2017187c6e1a9cb3731011710d814b2c76f28bbb5b510&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

接下来我们实打实的引入两个依赖项来。 321 走好。那这两个依赖项当中第一个 Lombbook 是一个代码生成插件，可以很方便的生成很多代码，它可以大大提高你的编程效率，以及降低代码的复杂度。那下一个插件是springboot，它自己的一个 test 插件。


OK，那好，我们接下来就去定义你当前项目的一些子项目。我们在这个根目录下面先给创建一个folder，这个 folder 文件名我就给它起名叫 service 好了。OK，那接下来我们在这个 service 当中，同学们看要去创建一个什么呀？创建一个子的 module ，那怎么快？OK，我们在创建的时候指定好它的文件夹路径，把它丢到刚才创建的 service 里。OK，给它起名叫什么呢？ A restroom 杠service，好，往下走，你，OK，这个项目我们并不会在这里面添加什么代码？它依然是作为一个什么呀？作为一个负向，我们添加进去，它这里还会进一步包含子项目。


什么子项目？我们这里依次创建 3 个子项目，那这三个子项目分别是对应着API，还有道层，还有 service 层。好，我们这里首先把这个 API 给它创建出来，同样的在这里点击创建一个module，它的名字就叫什么呀？ rest room 杠API。


OK，那这个 restroom 杠API，它这里存放什么内容？我们会把一个接口层，还有对外暴露的一些 p o g u 泡酒类把它放到这里面来。这是一个标准的微服务架构的项目结构，你的上下游依赖方，不用去依赖整个 restroom service，只用去依赖你的 restroom API 就可以获得他想要访问的公共类。

```java
package com.imooc.restroom.pojo;

import lombok.AllArgsConstructor;
import lombok.Builder;
import lombok.Data;
import lombok.NoArgsConstructor;

/**
 * <h1></h1>
 */
@Data
@Builder
@AllArgsConstructor
@NoArgsConstructor
public class Toilet {

    private Long id;

    private boolean clean;

    private boolean available;


}
```

好，那我们在这里面 Java 里创建一个directory，这个 directory 我们给它起名叫 Com 点 i mock，再一个点，点谁呢？Restroom，那这是一个当前的包名。好，OK，然后在这个项目夹下面再去创建一个 p u g u 抛 GIU 类是放一些公共的代码类的，比如说我接下来我就要在这边创建一个class，右键点击创建 class 创建的这个类的名字叫toilet，洗手间蹲坑又叫马桶。那这个 toilet 将会暴露给各个上下游的服务来进行调用。


我们给他声明这样几个属性，第一个是ID，你当前蹲坑的主键ID，第二个是 private 多少值clean，那你当前蹲坑是否已经被打扫干净了？最后一个是什么呀？available，证明你这个坑 win 当前是有人还是没人？好，那接下来我们就使用 Lombbook 给它自动的生成一些代码，比如说data，它可以生成对应的 get setter 方法以及 to string 方法。


builder 是相当于给当前的这个类自动引入了 builder 创建者模式，待会儿我们写代码的时候就能体会到这个优越性了，生成代码非常方便。以及我这边要给它声明的两个是什么呀？ no Arcs constructor 还有 all arguments constructor，那它们分别会为当前的类创建一个无参构造器，以及包含所有参数的构造器，不用写一行代码，全部通过注解搞定，非常的酷炫。


好，那这个类创建好了，我们接下来。哎，给它去定义一个 a p i 那路径是come，点 i mock，点restroom，点 a p i OK，那么在 a p i 里面，我们选择创建一个 Java 的接口类型是interface，给它起名叫 i rest room service OK service 好，走你。那这个service。我们声明这样的几个方法，第一个 public list，获取当前所有可用的 toilet 列表，那我给它起名叫 get available toilet OK，那它没有入参，只有一个返回值，去获取所有当前可用的toilet。

```java
package com.imooc.restroom.api;

import com.imooc.restroom.pojo.Toilet;

import java.util.List;

/**
 * <h1></h1>
 */
public interface IRestroomService {


    public List<Toilet> getAvailableToilet();

    public Toilet occupy(Long id);

    public Toilet release(Long id);

    public boolean checkAvailability(Long id);


}
```

好，接下来第二个方法，我给它声名叫什么？ public 返回值 toilet 名称叫 occupy OK， occupy 是什么意思？就是说我当前有一个人要开大号了，我要去占用你的蹲坑。那这是这个方法。再往后下一个方法是我结束了，完事了之后我要把你的蹲坑打扫干净，对吧？所以它叫release。

OK，那除了这几个方法以外，我还想定义一个方法，我要去查看当前的这个坑位是否可以被我占用，那叫 check availability，那传入的是一个当前坑位的ID。好，那到现在为止，你的这个 API 层就已经完全定义好了。那接下来我们去定义一个什么呀？定义一个Doc。


OK，那同样的创建一个module，给这个 module 起名叫做restroom，杠 d a o dot 层。好，那这个项目里我们直接去创建当前项目的数据库访问层，以及对应的数据库的 entity 对象，那么首先第一步我要把这个包路径给它创建出来，同样是 come 点imock，再一个点叫 rest room，后面跟 entity 证明它是一个数据库对象。那这个数据库对象和咱前面在 API 层里面创建的这个 p u g u toilet 非常像，我们直接把它 copy 过来好了，但是要给它改头换面叫 toilet entity，OK，那创建出来之后我要对它做一些修改改，比如说当前的这个 ID 字段，我要用咱的 spring GPA 的标签把它给标识出来。

加标签之前我们是不是要去加一些依赖？同学们，我们找到 restroom d e o 的palm，在这里引入两个依赖，同学们不要眨眼来 321 走，OK，那这两个依赖同学们看，分别是 spring boot starter data GP，那这个是它的核心 GP 访问注解。


OK，再下面一个是谁？ MySQL 的 g d b c driver，我们采用的 version 是八点零点二幺，OK，那这两个注解添加好了之后，我们再回到咱刚才创建的这个 toilet entity 里面，就可以放心大胆的给它添加注解了。给它添加的注解第一个是ID，这里我们来添加三个属性，第一个是 ID 那一个主键的annotation。第二个我这里要去指定什么呀？指定你这个主键，它的 value 对应的值怎么来生成？我可以使用 generated value，并且给它指定一个什么呀？strategy。这个 strategy 里面有很多不同的类型，那比方说使用 sequence 来去生成，或者使用数据库的自动组件等等。那我这里给它指定的是什么呀？我给它指定的叫identity。是这个类型是什么意思？就是说我把它全权交由 MySQL 自增主键来去生成它对应的ID，我不管它了。


好，最后一个注解，我给它指定一个column。 column 对应的 name 是什么呀？ID，那真实的对应到了数据库当中的一列。好，那下面的两个属性同学们应该知道该添加什么呀？同样的给它添加一个color。那有时候我们的GPA，即使你不定义这个column，那它默认依然会使用你当前的属性名称把它作为column，但是我这里建议从可读性的角度出发，我们还是尽可能的把每一个属性都给它，用这个 column 定义出来，这样的话以防万一以后不小心更改了属性名，那你和数据库当中对应的这个字段名有可能出现不一致。


OK，那这里我还要给它去加一个特殊的属性，叫knowable，这里默认是允许空的，我们这里给它设定为什么呀？false，也就是说非空。那 entity 这里已经创建完了，接下来要去创建谁了？还缺少一个 do 层对不对？好，那这个 do 层的路径，我们把它放到 COM 点imock，点restroom，再一个点谁DAO。


OK，那接下来我们就要去充分的展现 spring data 的优越性了，我们给当前的这个包路径下创建一个谁？一个interface。同学们，这就是我们的 d o 访问层，我给它起名叫 toilet d a o。好，这里有些文章可以做了。我们把当前的 interface 记成一个父类的interface，它的名称叫 g p a repostery。OK，这里的 repository 我们可以给它加一个泛型。当前 repository 对应的你的 entity 类是 toilet entity，同时这个类的主键是launch。

[image](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/6b16ff42-0ce4-4a93-a2d6-7dd1e0c2a53b/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666FSXQKMF%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T231310Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIEbzo6KPzIR9WqgRuB67gEk3WU3v2KmKd%2BzYmvg81riCAiAr931HVwFedgCN4On5%2F6clEfPcdd6punMJFI2sy%2FLEwCqIBAjG%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMf3JQX5GJhg9dbOCrKtwDUmrBEUJLWkdjUBKZQPQBijz8HCSjJESFfMINK8uqCSF9fVWV8VY5x0aTusfBo%2FT2wMII7wTTOb6Ouh%2FeDLbs14%2FYXj1XppcYzFSvTpkHjdubcfSXwJ6qlO35c9bRg7UY6bAhcIEP63EPGSO4t3tgJ86n532IHHi%2FlItlzVkkpVCQwDKDJM%2BDLFKAnNPg8yH0pZiu6vLaldSz%2FsTumDgDDeMRyJA%2FeNm6LjufHpNvTIVEyE0wm%2FyE8GJg91rQ6TTn9BJbR7EM4chrflSc2DFI3pwC9%2ByTsVBxpAFdhS%2F1dcSTSVtQDxMozsqpdz2bh6dXVqclvcbWu726xp16WTeT0J3Eko6VPp15LGAyESVFODlu72K9uBkpztksWaa%2FEd8Y58ixCiClzzBSVul%2FSKg3GjKXWSJZ7Hc8E7VB16XDtpVQfZYW%2BEVm0t5jQ5vP04A76oSTjMrH9ieJYn5tior4%2Fg8D2VdyU5YHDCPOH2DFAWhA78E0fFLhWtRmaQyK5je%2F%2FQ9UbRzy3u2XG%2BL9BefMTpxKNdXZZ0m%2Byzsix0CGgVKa8hwlO3hG1ZvJgPt4a%2F1AgGfWMIZt6gffvDVF44km5bvjpzrVZ7uyo6H29ZrgWd2NXlT69zhF7HcVfj0wt7j%2F0gY6pgFynhrac8OlrLxYn9%2B15wEET0LNcDv%2Bk1DzudJ%2FTF6Y8myugXu49dqrRTiCIwmrlH%2BBLbOfVjYEvi25zWkOBZ5Lf661p%2BiAEnpjbPI9RN%2FNvmgUpg6GX17WxepDwVc0aS1LO0YKW4OusMAEDD2FJWZ0BdQXh5XjwYWIcugYjvX2UMfpjoP0soM7CaRhrGJBMbxmupBNIH5inAOxWY2OgCYJu84%2Bk773&X-Amz-Signature=6b318b67156e0a7c86deff16797e909b69f32261b3bd17caf82cb40744e51666&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

*好，那这个 jpaReposter 有什么用？这里面它会自动的帮我们生成很多的接口查询，不用我们写任何的代码，你就可以做简单的查询，删除，修改，更新等等操作好*，

[image](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/302cdb1f-a137-4d79-9383-0a070e735d6f/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666FSXQKMF%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T231309Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIEbzo6KPzIR9WqgRuB67gEk3WU3v2KmKd%2BzYmvg81riCAiAr931HVwFedgCN4On5%2F6clEfPcdd6punMJFI2sy%2FLEwCqIBAjG%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMf3JQX5GJhg9dbOCrKtwDUmrBEUJLWkdjUBKZQPQBijz8HCSjJESFfMINK8uqCSF9fVWV8VY5x0aTusfBo%2FT2wMII7wTTOb6Ouh%2FeDLbs14%2FYXj1XppcYzFSvTpkHjdubcfSXwJ6qlO35c9bRg7UY6bAhcIEP63EPGSO4t3tgJ86n532IHHi%2FlItlzVkkpVCQwDKDJM%2BDLFKAnNPg8yH0pZiu6vLaldSz%2FsTumDgDDeMRyJA%2FeNm6LjufHpNvTIVEyE0wm%2FyE8GJg91rQ6TTn9BJbR7EM4chrflSc2DFI3pwC9%2ByTsVBxpAFdhS%2F1dcSTSVtQDxMozsqpdz2bh6dXVqclvcbWu726xp16WTeT0J3Eko6VPp15LGAyESVFODlu72K9uBkpztksWaa%2FEd8Y58ixCiClzzBSVul%2FSKg3GjKXWSJZ7Hc8E7VB16XDtpVQfZYW%2BEVm0t5jQ5vP04A76oSTjMrH9ieJYn5tior4%2Fg8D2VdyU5YHDCPOH2DFAWhA78E0fFLhWtRmaQyK5je%2F%2FQ9UbRzy3u2XG%2BL9BefMTpxKNdXZZ0m%2Byzsix0CGgVKa8hwlO3hG1ZvJgPt4a%2F1AgGfWMIZt6gffvDVF44km5bvjpzrVZ7uyo6H29ZrgWd2NXlT69zhF7HcVfj0wt7j%2F0gY6pgFynhrac8OlrLxYn9%2B15wEET0LNcDv%2Bk1DzudJ%2FTF6Y8myugXu49dqrRTiCIwmrlH%2BBLbOfVjYEvi25zWkOBZ5Lf661p%2BiAEnpjbPI9RN%2FNvmgUpg6GX17WxepDwVc0aS1LO0YKW4OusMAEDD2FJWZ0BdQXh5XjwYWIcugYjvX2UMfpjoP0soM7CaRhrGJBMbxmupBNIH5inAOxWY2OgCYJu84%2Bk773&X-Amz-Signature=d1d6b4a5d69380d8dede9d9c58dfd780c55d1c9eb85f23be9dc5fd2561623541&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

**非常的方便。那对于一些复杂的查询，我们这里怎么来做？有两种方法。**

**第一种方法非常的简单，比如说我现在想去查询所有当前可用的厕所。那怎么查？我们的查询的返回值应该是什么呀？一个 list 的 toilet entity。OK，那它的查询逻辑同学们，非常有意思，它的查询逻辑是写在方法名当中的。比方说我想根据前面创建的这个 entity 里面的两个字段来判断可用性，通过 clean 和 available 判断可用性。那怎么来判断？我们这里来写一个方法，这个名称我这样起find。诶，你看下面给出什么呀？给出提示来了，这都是 spring g p data 它提供的非常牛逼的特性。那我这里 find 谁 find all by 谁，这里就是你的字段名了，我这里 by clean，然后 and available，根据这两个属性，我来查询你当前厕所是否可用。**

[image](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/96d38b53-882a-40c3-aed9-02a430e70f37/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666FSXQKMF%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T231309Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIEbzo6KPzIR9WqgRuB67gEk3WU3v2KmKd%2BzYmvg81riCAiAr931HVwFedgCN4On5%2F6clEfPcdd6punMJFI2sy%2FLEwCqIBAjG%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMf3JQX5GJhg9dbOCrKtwDUmrBEUJLWkdjUBKZQPQBijz8HCSjJESFfMINK8uqCSF9fVWV8VY5x0aTusfBo%2FT2wMII7wTTOb6Ouh%2FeDLbs14%2FYXj1XppcYzFSvTpkHjdubcfSXwJ6qlO35c9bRg7UY6bAhcIEP63EPGSO4t3tgJ86n532IHHi%2FlItlzVkkpVCQwDKDJM%2BDLFKAnNPg8yH0pZiu6vLaldSz%2FsTumDgDDeMRyJA%2FeNm6LjufHpNvTIVEyE0wm%2FyE8GJg91rQ6TTn9BJbR7EM4chrflSc2DFI3pwC9%2ByTsVBxpAFdhS%2F1dcSTSVtQDxMozsqpdz2bh6dXVqclvcbWu726xp16WTeT0J3Eko6VPp15LGAyESVFODlu72K9uBkpztksWaa%2FEd8Y58ixCiClzzBSVul%2FSKg3GjKXWSJZ7Hc8E7VB16XDtpVQfZYW%2BEVm0t5jQ5vP04A76oSTjMrH9ieJYn5tior4%2Fg8D2VdyU5YHDCPOH2DFAWhA78E0fFLhWtRmaQyK5je%2F%2FQ9UbRzy3u2XG%2BL9BefMTpxKNdXZZ0m%2Byzsix0CGgVKa8hwlO3hG1ZvJgPt4a%2F1AgGfWMIZt6gffvDVF44km5bvjpzrVZ7uyo6H29ZrgWd2NXlT69zhF7HcVfj0wt7j%2F0gY6pgFynhrac8OlrLxYn9%2B15wEET0LNcDv%2Bk1DzudJ%2FTF6Y8myugXu49dqrRTiCIwmrlH%2BBLbOfVjYEvi25zWkOBZ5Lf661p%2BiAEnpjbPI9RN%2FNvmgUpg6GX17WxepDwVc0aS1LO0YKW4OusMAEDD2FJWZ0BdQXh5XjwYWIcugYjvX2UMfpjoP0soM7CaRhrGJBMbxmupBNIH5inAOxWY2OgCYJu84%2Bk773&X-Amz-Signature=d03f54b4512146bd746b80a257d08d9cf04129533b43307eed1d8b96ac753a7c&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

[image](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/c18f2433-1270-462d-ba2d-91d2e9f638dc/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666FSXQKMF%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T231309Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIEbzo6KPzIR9WqgRuB67gEk3WU3v2KmKd%2BzYmvg81riCAiAr931HVwFedgCN4On5%2F6clEfPcdd6punMJFI2sy%2FLEwCqIBAjG%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMf3JQX5GJhg9dbOCrKtwDUmrBEUJLWkdjUBKZQPQBijz8HCSjJESFfMINK8uqCSF9fVWV8VY5x0aTusfBo%2FT2wMII7wTTOb6Ouh%2FeDLbs14%2FYXj1XppcYzFSvTpkHjdubcfSXwJ6qlO35c9bRg7UY6bAhcIEP63EPGSO4t3tgJ86n532IHHi%2FlItlzVkkpVCQwDKDJM%2BDLFKAnNPg8yH0pZiu6vLaldSz%2FsTumDgDDeMRyJA%2FeNm6LjufHpNvTIVEyE0wm%2FyE8GJg91rQ6TTn9BJbR7EM4chrflSc2DFI3pwC9%2ByTsVBxpAFdhS%2F1dcSTSVtQDxMozsqpdz2bh6dXVqclvcbWu726xp16WTeT0J3Eko6VPp15LGAyESVFODlu72K9uBkpztksWaa%2FEd8Y58ixCiClzzBSVul%2FSKg3GjKXWSJZ7Hc8E7VB16XDtpVQfZYW%2BEVm0t5jQ5vP04A76oSTjMrH9ieJYn5tior4%2Fg8D2VdyU5YHDCPOH2DFAWhA78E0fFLhWtRmaQyK5je%2F%2FQ9UbRzy3u2XG%2BL9BefMTpxKNdXZZ0m%2Byzsix0CGgVKa8hwlO3hG1ZvJgPt4a%2F1AgGfWMIZt6gffvDVF44km5bvjpzrVZ7uyo6H29ZrgWd2NXlT69zhF7HcVfj0wt7j%2F0gY6pgFynhrac8OlrLxYn9%2B15wEET0LNcDv%2Bk1DzudJ%2FTF6Y8myugXu49dqrRTiCIwmrlH%2BBLbOfVjYEvi25zWkOBZ5Lf661p%2BiAEnpjbPI9RN%2FNvmgUpg6GX17WxepDwVc0aS1LO0YKW4OusMAEDD2FJWZ0BdQXh5XjwYWIcugYjvX2UMfpjoP0soM7CaRhrGJBMbxmupBNIH5inAOxWY2OgCYJu84%2Bk773&X-Amz-Signature=dc579c06f89d6e23239019f3f5757ba84813e533fe3c87797a1f0286befad032&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

[image](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/5a6b031a-5797-4cd3-8417-364860d9cab4/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666FSXQKMF%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T231309Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIEbzo6KPzIR9WqgRuB67gEk3WU3v2KmKd%2BzYmvg81riCAiAr931HVwFedgCN4On5%2F6clEfPcdd6punMJFI2sy%2FLEwCqIBAjG%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMf3JQX5GJhg9dbOCrKtwDUmrBEUJLWkdjUBKZQPQBijz8HCSjJESFfMINK8uqCSF9fVWV8VY5x0aTusfBo%2FT2wMII7wTTOb6Ouh%2FeDLbs14%2FYXj1XppcYzFSvTpkHjdubcfSXwJ6qlO35c9bRg7UY6bAhcIEP63EPGSO4t3tgJ86n532IHHi%2FlItlzVkkpVCQwDKDJM%2BDLFKAnNPg8yH0pZiu6vLaldSz%2FsTumDgDDeMRyJA%2FeNm6LjufHpNvTIVEyE0wm%2FyE8GJg91rQ6TTn9BJbR7EM4chrflSc2DFI3pwC9%2ByTsVBxpAFdhS%2F1dcSTSVtQDxMozsqpdz2bh6dXVqclvcbWu726xp16WTeT0J3Eko6VPp15LGAyESVFODlu72K9uBkpztksWaa%2FEd8Y58ixCiClzzBSVul%2FSKg3GjKXWSJZ7Hc8E7VB16XDtpVQfZYW%2BEVm0t5jQ5vP04A76oSTjMrH9ieJYn5tior4%2Fg8D2VdyU5YHDCPOH2DFAWhA78E0fFLhWtRmaQyK5je%2F%2FQ9UbRzy3u2XG%2BL9BefMTpxKNdXZZ0m%2Byzsix0CGgVKa8hwlO3hG1ZvJgPt4a%2F1AgGfWMIZt6gffvDVF44km5bvjpzrVZ7uyo6H29ZrgWd2NXlT69zhF7HcVfj0wt7j%2F0gY6pgFynhrac8OlrLxYn9%2B15wEET0LNcDv%2Bk1DzudJ%2FTF6Y8myugXu49dqrRTiCIwmrlH%2BBLbOfVjYEvi25zWkOBZ5Lf661p%2BiAEnpjbPI9RN%2FNvmgUpg6GX17WxepDwVc0aS1LO0YKW4OusMAEDD2FJWZ0BdQXh5XjwYWIcugYjvX2UMfpjoP0soM7CaRhrGJBMbxmupBNIH5inAOxWY2OgCYJu84%2Bk773&X-Amz-Signature=465eee837658f3708a70327a8258edecbc2693eee2f2d30bb5c90a74f70b61e2&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

**同学们看，这个查询条件全部写在了方法里面，你的方法名就是你的 SQL 语句，非常的方便。那你 SQL 语句的参数怎么传入进去？很简单，方法参数这里 clean 就是对应你相应的字段名称。 available OK，也是对应你的字段名称，这里要一一匹配。所以 spring data jpa 这里体现一个什么思想，约定大于配置，不用写任何代码，不要做配置，只要我们按照符合条件的约定来去声明你的方法，那么不要写一行代码，你就可以去生成Doc。**

[image](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/2bba2f9a-9721-4c3d-9286-4c1cdd4cdad1/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666FSXQKMF%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T231309Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIEbzo6KPzIR9WqgRuB67gEk3WU3v2KmKd%2BzYmvg81riCAiAr931HVwFedgCN4On5%2F6clEfPcdd6punMJFI2sy%2FLEwCqIBAjG%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMf3JQX5GJhg9dbOCrKtwDUmrBEUJLWkdjUBKZQPQBijz8HCSjJESFfMINK8uqCSF9fVWV8VY5x0aTusfBo%2FT2wMII7wTTOb6Ouh%2FeDLbs14%2FYXj1XppcYzFSvTpkHjdubcfSXwJ6qlO35c9bRg7UY6bAhcIEP63EPGSO4t3tgJ86n532IHHi%2FlItlzVkkpVCQwDKDJM%2BDLFKAnNPg8yH0pZiu6vLaldSz%2FsTumDgDDeMRyJA%2FeNm6LjufHpNvTIVEyE0wm%2FyE8GJg91rQ6TTn9BJbR7EM4chrflSc2DFI3pwC9%2ByTsVBxpAFdhS%2F1dcSTSVtQDxMozsqpdz2bh6dXVqclvcbWu726xp16WTeT0J3Eko6VPp15LGAyESVFODlu72K9uBkpztksWaa%2FEd8Y58ixCiClzzBSVul%2FSKg3GjKXWSJZ7Hc8E7VB16XDtpVQfZYW%2BEVm0t5jQ5vP04A76oSTjMrH9ieJYn5tior4%2Fg8D2VdyU5YHDCPOH2DFAWhA78E0fFLhWtRmaQyK5je%2F%2FQ9UbRzy3u2XG%2BL9BefMTpxKNdXZZ0m%2Byzsix0CGgVKa8hwlO3hG1ZvJgPt4a%2F1AgGfWMIZt6gffvDVF44km5bvjpzrVZ7uyo6H29ZrgWd2NXlT69zhF7HcVfj0wt7j%2F0gY6pgFynhrac8OlrLxYn9%2B15wEET0LNcDv%2Bk1DzudJ%2FTF6Y8myugXu49dqrRTiCIwmrlH%2BBLbOfVjYEvi25zWkOBZ5Lf661p%2BiAEnpjbPI9RN%2FNvmgUpg6GX17WxepDwVc0aS1LO0YKW4OusMAEDD2FJWZ0BdQXh5XjwYWIcugYjvX2UMfpjoP0soM7CaRhrGJBMbxmupBNIH5inAOxWY2OgCYJu84%2Bk773&X-Amz-Signature=0b7fa69f3d7b6b3076dd3044f636c14beec103e3c0db2c97d2d5cf45dde24927&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)


**OK，那对于一些复杂的需要定制的查询怎么办？我们这里还有很多其他的注解，你可以在上面自由的定制。比如你的 SQL 非常的复杂，无法体现在方法名上，或者说如果你写在方法名上，它可能变得非常长，不可阅读。那这种情况下，我们可以使用标签来人工的指定你想要查询的SQL，都是可以的，非常方便。**

[image](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/8b0ced10-3fd7-44ff-89dd-80e99461f82c/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666FSXQKMF%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T231310Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIEbzo6KPzIR9WqgRuB67gEk3WU3v2KmKd%2BzYmvg81riCAiAr931HVwFedgCN4On5%2F6clEfPcdd6punMJFI2sy%2FLEwCqIBAjG%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMf3JQX5GJhg9dbOCrKtwDUmrBEUJLWkdjUBKZQPQBijz8HCSjJESFfMINK8uqCSF9fVWV8VY5x0aTusfBo%2FT2wMII7wTTOb6Ouh%2FeDLbs14%2FYXj1XppcYzFSvTpkHjdubcfSXwJ6qlO35c9bRg7UY6bAhcIEP63EPGSO4t3tgJ86n532IHHi%2FlItlzVkkpVCQwDKDJM%2BDLFKAnNPg8yH0pZiu6vLaldSz%2FsTumDgDDeMRyJA%2FeNm6LjufHpNvTIVEyE0wm%2FyE8GJg91rQ6TTn9BJbR7EM4chrflSc2DFI3pwC9%2ByTsVBxpAFdhS%2F1dcSTSVtQDxMozsqpdz2bh6dXVqclvcbWu726xp16WTeT0J3Eko6VPp15LGAyESVFODlu72K9uBkpztksWaa%2FEd8Y58ixCiClzzBSVul%2FSKg3GjKXWSJZ7Hc8E7VB16XDtpVQfZYW%2BEVm0t5jQ5vP04A76oSTjMrH9ieJYn5tior4%2Fg8D2VdyU5YHDCPOH2DFAWhA78E0fFLhWtRmaQyK5je%2F%2FQ9UbRzy3u2XG%2BL9BefMTpxKNdXZZ0m%2Byzsix0CGgVKa8hwlO3hG1ZvJgPt4a%2F1AgGfWMIZt6gffvDVF44km5bvjpzrVZ7uyo6H29ZrgWd2NXlT69zhF7HcVfj0wt7j%2F0gY6pgFynhrac8OlrLxYn9%2B15wEET0LNcDv%2Bk1DzudJ%2FTF6Y8myugXu49dqrRTiCIwmrlH%2BBLbOfVjYEvi25zWkOBZ5Lf661p%2BiAEnpjbPI9RN%2FNvmgUpg6GX17WxepDwVc0aS1LO0YKW4OusMAEDD2FJWZ0BdQXh5XjwYWIcugYjvX2UMfpjoP0soM7CaRhrGJBMbxmupBNIH5inAOxWY2OgCYJu84%2Bk773&X-Amz-Signature=8380c256f26c9a327551f7c1e16acab70fb360b6f301add91587b2434159381b&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)


OK，那我们这个道层也已经声明好了，接下来我们应该去数据库里把这个数据表给它创建出来。好，我把这个建表语句直接放到这个 resources 文件夹下面。同学们看，我们这里创建了一张叫 toilet 表，那它包含前面咱定义的 3 个属性ID， clean 还有available。

[image](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/af3714fc-b4c9-4f7b-b0f7-c0d67a538729/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666FSXQKMF%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T231310Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIEbzo6KPzIR9WqgRuB67gEk3WU3v2KmKd%2BzYmvg81riCAiAr931HVwFedgCN4On5%2F6clEfPcdd6punMJFI2sy%2FLEwCqIBAjG%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMf3JQX5GJhg9dbOCrKtwDUmrBEUJLWkdjUBKZQPQBijz8HCSjJESFfMINK8uqCSF9fVWV8VY5x0aTusfBo%2FT2wMII7wTTOb6Ouh%2FeDLbs14%2FYXj1XppcYzFSvTpkHjdubcfSXwJ6qlO35c9bRg7UY6bAhcIEP63EPGSO4t3tgJ86n532IHHi%2FlItlzVkkpVCQwDKDJM%2BDLFKAnNPg8yH0pZiu6vLaldSz%2FsTumDgDDeMRyJA%2FeNm6LjufHpNvTIVEyE0wm%2FyE8GJg91rQ6TTn9BJbR7EM4chrflSc2DFI3pwC9%2ByTsVBxpAFdhS%2F1dcSTSVtQDxMozsqpdz2bh6dXVqclvcbWu726xp16WTeT0J3Eko6VPp15LGAyESVFODlu72K9uBkpztksWaa%2FEd8Y58ixCiClzzBSVul%2FSKg3GjKXWSJZ7Hc8E7VB16XDtpVQfZYW%2BEVm0t5jQ5vP04A76oSTjMrH9ieJYn5tior4%2Fg8D2VdyU5YHDCPOH2DFAWhA78E0fFLhWtRmaQyK5je%2F%2FQ9UbRzy3u2XG%2BL9BefMTpxKNdXZZ0m%2Byzsix0CGgVKa8hwlO3hG1ZvJgPt4a%2F1AgGfWMIZt6gffvDVF44km5bvjpzrVZ7uyo6H29ZrgWd2NXlT69zhF7HcVfj0wt7j%2F0gY6pgFynhrac8OlrLxYn9%2B15wEET0LNcDv%2Bk1DzudJ%2FTF6Y8myugXu49dqrRTiCIwmrlH%2BBLbOfVjYEvi25zWkOBZ5Lf661p%2BiAEnpjbPI9RN%2FNvmgUpg6GX17WxepDwVc0aS1LO0YKW4OusMAEDD2FJWZ0BdQXh5XjwYWIcugYjvX2UMfpjoP0soM7CaRhrGJBMbxmupBNIH5inAOxWY2OgCYJu84%2Bk773&X-Amz-Signature=08c12f601864c8a6d65573878f9cb8ddf7b1aba279de1b1ed568859174222e0e&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

与此同时，为了体现咱微服务架构的这种结构，我们把这个表单独的放到一个 schema 当中，这样一来就相当于我自己的微服务有一个独立的schema，就相当于是有一个独立的数据库，那这也是符合微服务设计理念的，每一个服务去控制自己的数据访问别的服务不能直接的访问你的数据。


OK，那咱的啊， a p i 还有道层都处理好了，接下来我们来写一些业务代码喽，那这个业务代码我们把它起名叫做什么呀？叫 restroom service scan core，这个是具体的业务逻辑核心了。好，我们在这个 service call 当中，我们打开它的这个 palm 文件，在 palm 文件里我们要引入很多的依赖项，同学们不要眨眼 321 走，OK，那么这里面同学们看我们引入了哪些依赖项？第一个依赖项我们把前面创建的 restroom API 把它添加进来。第二个我们把前面创建的 Doc 也同样的给它加了进来。

[image](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/b5ead047-356d-4392-8c80-b9c82b6a97d4/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666FSXQKMF%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T231310Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIEbzo6KPzIR9WqgRuB67gEk3WU3v2KmKd%2BzYmvg81riCAiAr931HVwFedgCN4On5%2F6clEfPcdd6punMJFI2sy%2FLEwCqIBAjG%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMf3JQX5GJhg9dbOCrKtwDUmrBEUJLWkdjUBKZQPQBijz8HCSjJESFfMINK8uqCSF9fVWV8VY5x0aTusfBo%2FT2wMII7wTTOb6Ouh%2FeDLbs14%2FYXj1XppcYzFSvTpkHjdubcfSXwJ6qlO35c9bRg7UY6bAhcIEP63EPGSO4t3tgJ86n532IHHi%2FlItlzVkkpVCQwDKDJM%2BDLFKAnNPg8yH0pZiu6vLaldSz%2FsTumDgDDeMRyJA%2FeNm6LjufHpNvTIVEyE0wm%2FyE8GJg91rQ6TTn9BJbR7EM4chrflSc2DFI3pwC9%2ByTsVBxpAFdhS%2F1dcSTSVtQDxMozsqpdz2bh6dXVqclvcbWu726xp16WTeT0J3Eko6VPp15LGAyESVFODlu72K9uBkpztksWaa%2FEd8Y58ixCiClzzBSVul%2FSKg3GjKXWSJZ7Hc8E7VB16XDtpVQfZYW%2BEVm0t5jQ5vP04A76oSTjMrH9ieJYn5tior4%2Fg8D2VdyU5YHDCPOH2DFAWhA78E0fFLhWtRmaQyK5je%2F%2FQ9UbRzy3u2XG%2BL9BefMTpxKNdXZZ0m%2Byzsix0CGgVKa8hwlO3hG1ZvJgPt4a%2F1AgGfWMIZt6gffvDVF44km5bvjpzrVZ7uyo6H29ZrgWd2NXlT69zhF7HcVfj0wt7j%2F0gY6pgFynhrac8OlrLxYn9%2B15wEET0LNcDv%2Bk1DzudJ%2FTF6Y8myugXu49dqrRTiCIwmrlH%2BBLbOfVjYEvi25zWkOBZ5Lf661p%2BiAEnpjbPI9RN%2FNvmgUpg6GX17WxepDwVc0aS1LO0YKW4OusMAEDD2FJWZ0BdQXh5XjwYWIcugYjvX2UMfpjoP0soM7CaRhrGJBMbxmupBNIH5inAOxWY2OgCYJu84%2Bk773&X-Amz-Signature=aa04af6e241f9c65cf224534237f3c523a268bc3bab5b17567a0fdba6b8b3b57&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

```java
<?xml version="1.0" encoding="UTF-8"?>
<project xmlns="http://maven.apache.org/POM/4.0.0"
         xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
         xsi:schemaLocation="http://maven.apache.org/POM/4.0.0 http://maven.apache.org/xsd/maven-4.0.0.xsd">
    <parent>
        <artifactId>spring-cloud-proj</artifactId>
        <groupId>com.imooc</groupId>
        <version>1.0-SNAPSHOT</version>
        <relativePath>../../pom.xml</relativePath>
    </parent>
    <modelVersion>4.0.0</modelVersion>

    <artifactId>restroom-service-core</artifactId>

    <properties>
        <maven.compiler.source>8</maven.compiler.source>
        <maven.compiler.target>8</maven.compiler.target>
    </properties>


    <dependencies>
        <dependency>
            <groupId>${project.groupId}</groupId>
            <artifactId>restroom-api</artifactId>
            <version>${project.version}</version>
        </dependency>

        <dependency>
            <groupId>${project.groupId}</groupId>
            <artifactId>restroom-dao</artifactId>
            <version>${project.version}</version>
        </dependency>

        <dependency>
            <groupId>org.springframework.boot</groupId>
            <artifactId>spring-boot-starter-actuator</artifactId>
        </dependency>

        <!-- spring boot 的支持 -->
        <dependency>
            <groupId>org.springframework.boot</groupId>
            <artifactId>spring-boot-starter-web</artifactId>
        </dependency>

        <!-- nacos 的支持 -->
        <dependency>
            <groupId>com.alibaba.cloud</groupId>
            <artifactId>spring-cloud-starter-alibaba-nacos-discovery</artifactId>
        </dependency>

    </dependencies>


</project>
```

好，那接下来的几个就是我们项目当中要使用的 spring cloud 的组件了，这里面最重要的是Neques，我们把 Neques discovery 这个依赖给它引入了进来。那再往上的两个依赖老生常谈，一个是 spring web 的支持依赖，第二个是 spring 的 activator 接口，那 activator 这里我们在后面的章节当中再去跟同学们见面，咱先把它给加在这边，先把这个坑给它占着。


好，那依赖项全部加入进来之后，我们这里去把相应的类给它创建出来。创建一个package，这个 package 它对应的名称，我们把它叫做Com，点imock，点restroom，OK，好，在这里我们选择创建一个启动类，叫兵马未动粮草先行。咱先把这个启动类给它创建出来，叫做 restroom application，OK，那这个类里面我们给它添加一个 public static void main 方法，作为一个启动方法，每次打这一行字，如行运流水，无丝毫障碍。刚学 Java 的时候就特别喜欢打这个闷方法，噼里啪啦乱打一通，宛如一个高手。


OK，我们采用 spring boot 点 run 的方法，我们把这个项目的类名给它 copy 进来，点 class 前面传入的这个 arguments 参数丢进来。好，那这就是标准的 spring boot 启动的方式。除此之外，我们还要去配置几个特殊的参数。第一个 component scan 这个参数是来做什么的？它是指定你当前 springboot 项目的扫包路径，那它会把这个路径下面的包给它加载到 springboot 的上下文当中。OK，这样的话你就可以在项目当中使用 auto wire 的之类的注解，把对应的依赖注入进来。


好，这是第一个，第二个最重要的注解是什么？ Enable discovery client. 这个是 spring cloud 做服务发现的核心配置，那么把它加入进来之后，不管你底层是使用的Eureka，还是使用的counsel，还是使用的我们的Nequos，那它这里都会去自动的启动服务注册功能以及服务发现功能。


OK，这是这个注解的作用。还有我们这里还要打开你 g p 的 auditing 功能，OK，这个注解以及什么呀？以及你 springboot application，把它当做一个 springboot 应用来把它启动起来。那早上创建好了启动类之后，接下来就要去写核心的上厕所的逻辑了，我们在这个 Com 点imock，点 restroom 下面继续创建一个package，这个包名就给它起叫service。

OK，那在这个 service 里我们继续创建一个类，这个类是 restroom service 的实现类，OK，同时它要去继承谁呢？继承前面咱去定义的 i restroom service，在实现对应的这 12344 个方法好，非常的简单，在实现之前我们要做一些小动作。


第一个是要去注入一个类，同学们能猜到注入谁吗？在前面定义了哪个类，需要注入的道层，对不对？ toilet d a o 我们把它给加入进来。好，加入进来以后，我们这个当前的 restrooms 上面是否还缺几个注解？我们给它戴几个大帽子，蓝的、绿的、黄的，把什么颜色的帽子给它扣上。第一个 s l four g，这是 Loom book 的一个非常非常方便的注解，可以自动的在你的类当中创建一个 logger 变量，非常的整洁。


第二个，我们添加一个 rest controller 这个注解，把它作为一个 controller 启动起来。同学们有没有觉得有点奇怪，在当前明明是service，为什么把它叫做controller？其实同学们在微服务架构领域当中， controller 这个概念已经非常弱化了，我们其实甚至并不需要 controller 通过 service 直接对外服务，因为你 controller 这里承担的责任是一个控制器，但是我们已经不是 MVC 架构形式了，同学们为什么还需要 control 了？比如在阿里系应用当中，其实我们都是直接对外暴露的service，然后 service 里面的这些返回值都是使用 JSON 来返回，那么再往后我这里还要给它定义一个什么呢？ request mapping 这里我要给它指定一个访问的路径，比如我就把它叫做 toilet 杠 service OK，那接下来我们开始写具体的代码，第一个代码 get available toilet。同学们这里睁大眼睛看一下 spring data 的优越性，我们直接去获取到 toilet entity。


怎么来获取？同学们看，我这里只用去通过 toilet d e， o 点使用这个 find all by clean and available 传入两个参数，两个 true 参数，获取到当前可用并且已经冲洗干净的洗手间。

[image](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/d97d6446-28bc-4fbe-b840-7fc5dadbee19/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666FSXQKMF%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T231310Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIEbzo6KPzIR9WqgRuB67gEk3WU3v2KmKd%2BzYmvg81riCAiAr931HVwFedgCN4On5%2F6clEfPcdd6punMJFI2sy%2FLEwCqIBAjG%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMf3JQX5GJhg9dbOCrKtwDUmrBEUJLWkdjUBKZQPQBijz8HCSjJESFfMINK8uqCSF9fVWV8VY5x0aTusfBo%2FT2wMII7wTTOb6Ouh%2FeDLbs14%2FYXj1XppcYzFSvTpkHjdubcfSXwJ6qlO35c9bRg7UY6bAhcIEP63EPGSO4t3tgJ86n532IHHi%2FlItlzVkkpVCQwDKDJM%2BDLFKAnNPg8yH0pZiu6vLaldSz%2FsTumDgDDeMRyJA%2FeNm6LjufHpNvTIVEyE0wm%2FyE8GJg91rQ6TTn9BJbR7EM4chrflSc2DFI3pwC9%2ByTsVBxpAFdhS%2F1dcSTSVtQDxMozsqpdz2bh6dXVqclvcbWu726xp16WTeT0J3Eko6VPp15LGAyESVFODlu72K9uBkpztksWaa%2FEd8Y58ixCiClzzBSVul%2FSKg3GjKXWSJZ7Hc8E7VB16XDtpVQfZYW%2BEVm0t5jQ5vP04A76oSTjMrH9ieJYn5tior4%2Fg8D2VdyU5YHDCPOH2DFAWhA78E0fFLhWtRmaQyK5je%2F%2FQ9UbRzy3u2XG%2BL9BefMTpxKNdXZZ0m%2Byzsix0CGgVKa8hwlO3hG1ZvJgPt4a%2F1AgGfWMIZt6gffvDVF44km5bvjpzrVZ7uyo6H29ZrgWd2NXlT69zhF7HcVfj0wt7j%2F0gY6pgFynhrac8OlrLxYn9%2B15wEET0LNcDv%2Bk1DzudJ%2FTF6Y8myugXu49dqrRTiCIwmrlH%2BBLbOfVjYEvi25zWkOBZ5Lf661p%2BiAEnpjbPI9RN%2FNvmgUpg6GX17WxepDwVc0aS1LO0YKW4OusMAEDD2FJWZ0BdQXh5XjwYWIcugYjvX2UMfpjoP0soM7CaRhrGJBMbxmupBNIH5inAOxWY2OgCYJu84%2Bk773&X-Amz-Signature=45e5fef32e35a4567947b249ef3f7d08a98e295be09fc097a581c70e5c574dba&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

接下来我们这里要把这个返回的值做一个处理。什么处理？把它 convert 一下，转换成我们可以对外直接提供的这个 toilet 对象，因为你的最后面的这个 DB 层对象，这对象我们内部使用就好了，不要把它暴露给外部。对于外部我们要做这么一层封装好，我们这里使用函数式编程的方式，给它调用 stream 点map，这里我们需要做一个什么呀？做一个对应的转换器，那这个转换器呢？我们对应的就要写一个方法，那接下来我们在这个包下面创建一个单独的目录，就叫converter， converter 这里咱去创建一个类，那这个类我们专门做什么呀？做这个 d o 和 v o 的转换，OK，所以他这边需要去声明一个 static 方法，那么它返回一个对外访问的 toilet 对象，那它接受的参数是谁？就是咱数据层的这个 toilet entity。


OK，那他这个逻辑，同学们看，这里又要给大家去 show 一下 long book 的优越性了，直接 return 谁啊？ toilet 点builder， builder 是怎么生成出来的？就是咱 toilet 上面的这个 builder 方法，看到吗？这里有一个注解， lombbook 的注解，可以自动的实现这个 builder 形式的设计模式。

[image](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/03375f88-4697-454e-87ec-ac54f6d2216a/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666FSXQKMF%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T231310Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIEbzo6KPzIR9WqgRuB67gEk3WU3v2KmKd%2BzYmvg81riCAiAr931HVwFedgCN4On5%2F6clEfPcdd6punMJFI2sy%2FLEwCqIBAjG%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMf3JQX5GJhg9dbOCrKtwDUmrBEUJLWkdjUBKZQPQBijz8HCSjJESFfMINK8uqCSF9fVWV8VY5x0aTusfBo%2FT2wMII7wTTOb6Ouh%2FeDLbs14%2FYXj1XppcYzFSvTpkHjdubcfSXwJ6qlO35c9bRg7UY6bAhcIEP63EPGSO4t3tgJ86n532IHHi%2FlItlzVkkpVCQwDKDJM%2BDLFKAnNPg8yH0pZiu6vLaldSz%2FsTumDgDDeMRyJA%2FeNm6LjufHpNvTIVEyE0wm%2FyE8GJg91rQ6TTn9BJbR7EM4chrflSc2DFI3pwC9%2ByTsVBxpAFdhS%2F1dcSTSVtQDxMozsqpdz2bh6dXVqclvcbWu726xp16WTeT0J3Eko6VPp15LGAyESVFODlu72K9uBkpztksWaa%2FEd8Y58ixCiClzzBSVul%2FSKg3GjKXWSJZ7Hc8E7VB16XDtpVQfZYW%2BEVm0t5jQ5vP04A76oSTjMrH9ieJYn5tior4%2Fg8D2VdyU5YHDCPOH2DFAWhA78E0fFLhWtRmaQyK5je%2F%2FQ9UbRzy3u2XG%2BL9BefMTpxKNdXZZ0m%2Byzsix0CGgVKa8hwlO3hG1ZvJgPt4a%2F1AgGfWMIZt6gffvDVF44km5bvjpzrVZ7uyo6H29ZrgWd2NXlT69zhF7HcVfj0wt7j%2F0gY6pgFynhrac8OlrLxYn9%2B15wEET0LNcDv%2Bk1DzudJ%2FTF6Y8myugXu49dqrRTiCIwmrlH%2BBLbOfVjYEvi25zWkOBZ5Lf661p%2BiAEnpjbPI9RN%2FNvmgUpg6GX17WxepDwVc0aS1LO0YKW4OusMAEDD2FJWZ0BdQXh5XjwYWIcugYjvX2UMfpjoP0soM7CaRhrGJBMbxmupBNIH5inAOxWY2OgCYJu84%2Bk773&X-Amz-Signature=f06d2bd90fa20aec352372789010d137fb25ff5715411477dba46a184656f93b&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

OK，我这里给它传入一个ID，那 entity 点 get ID，往后再传入一个clean，OK，把这每一个属性全部都通过这种方式挨个的塞入进去，那你通过 long book 可以节省大量的编码。OK，那这是一种方式，等后面我们会使用另外一种方式，另外一个也同样方便的工具类，给同学们展示这样的转化流程。OK，所以在这个项目当中，同学们应该可以学到很多代码上面偷懒省事的小技巧。


