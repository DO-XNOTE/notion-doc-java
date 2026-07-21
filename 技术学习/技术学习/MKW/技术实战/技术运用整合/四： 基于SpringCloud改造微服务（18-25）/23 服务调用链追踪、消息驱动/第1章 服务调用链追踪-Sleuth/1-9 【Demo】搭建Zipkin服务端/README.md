---
title: 1-9 【Demo】搭建Zipkin服务端
---

# 1-9 【Demo】搭建Zipkin服务端

[image](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/44333a28-defa-47ba-bf98-b08bf5178e77/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VTONEK4V%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T225759Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIBIyehUBj7eN41%2BIAY%2BNqPosAb6EGyvluK9MPBYBEX8gAiA5X27we3k1SG%2B1%2BsNI9L7c9FByHmKXN59YPCRAuveY9yqIBAjG%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMnBiHIfQcq9xIQxgNKtwDO1hljGirRaKdEPVQwn5GenuE4QTUmQXeaN%2FISNhRggHQ4vNZhdkqKm0WWycegwxHl6x7gYSHQTHv5FnGNrU7tY5K2RPH9RZFnkfFRyYCmh%2Fuwo66mNFy%2BiwjI2EK2rjAA2K0bopSegCTO5VCLlJtdSkELnEf0VnijD6kNk3w%2B9vEJuME62Z3nhwuMkgdndSWISsfkaekFNaSpic3fGIoQ%2B6JzvYTd49fG%2F2ilbM5UpihaAS9QT6LqL9ZTCVst33L%2B5oZ9wh8XCqDBxJQRSltCh15UvDxULxFg8MfrPgARqFFuZthQrWkwqTagmLhUoVnXRWJbLLHvVDdsIp4Hq6jn80kmJD4y%2FniahxQkzqVpVfPTKKKl66K4ROq0sXzXPlUUk1mCsRTpagGrWZj9Edb4r8SyhGUj5yyYuMjWX%2FiWBGK3NBTS5JZ8PYgJf%2BJjQh9WPKpeE%2B2gwIPV17ORsAS6WzPn0n0bm3lRVEBfr19BeT%2Fzg%2Bi%2B4l0v5N78aoYlH%2BEnK0r3Zp7r7W6TgdA7CKPed1EE04%2BNWJnAOiTKOIYWAhonS%2FgEiH936EL3FAqLHM7Wem%2BBqC%2FjW7zZrieP0ernIWxS822Lz5UXnoAo2bPKXN%2FTZH8Gsw2Bv6DXmcwgbf%2F0gY6pgHKerkGfR9%2Bez6GTCrrWe9EgNkZt6%2FL4MKXr11fUls6wrcuK8x9qJGW9AOjqPkdviKnPqYNamDlul85ZUOPkTqSR1djRJYBZlftadd%2Fp%2FiYjVU0LZUA4XvTL6P93xKaAbG4kyigsRy1h2NHLjIkyTwvrRl0t9FLS3kwcCX%2FoZetgmW4vcrgevjYEMTNuzac9%2BjqtirqhwQNCMlapYP4sG22QZtO1NTz&X-Amz-Signature=e6a67f6e8f5f95229f3d1eaac666c6d077a6b4e7d688f086299dcfdbe5da9ebc&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

[image](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/1d8693b7-cf51-4ab4-92df-d74db474b955/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VTONEK4V%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T225759Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIBIyehUBj7eN41%2BIAY%2BNqPosAb6EGyvluK9MPBYBEX8gAiA5X27we3k1SG%2B1%2BsNI9L7c9FByHmKXN59YPCRAuveY9yqIBAjG%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMnBiHIfQcq9xIQxgNKtwDO1hljGirRaKdEPVQwn5GenuE4QTUmQXeaN%2FISNhRggHQ4vNZhdkqKm0WWycegwxHl6x7gYSHQTHv5FnGNrU7tY5K2RPH9RZFnkfFRyYCmh%2Fuwo66mNFy%2BiwjI2EK2rjAA2K0bopSegCTO5VCLlJtdSkELnEf0VnijD6kNk3w%2B9vEJuME62Z3nhwuMkgdndSWISsfkaekFNaSpic3fGIoQ%2B6JzvYTd49fG%2F2ilbM5UpihaAS9QT6LqL9ZTCVst33L%2B5oZ9wh8XCqDBxJQRSltCh15UvDxULxFg8MfrPgARqFFuZthQrWkwqTagmLhUoVnXRWJbLLHvVDdsIp4Hq6jn80kmJD4y%2FniahxQkzqVpVfPTKKKl66K4ROq0sXzXPlUUk1mCsRTpagGrWZj9Edb4r8SyhGUj5yyYuMjWX%2FiWBGK3NBTS5JZ8PYgJf%2BJjQh9WPKpeE%2B2gwIPV17ORsAS6WzPn0n0bm3lRVEBfr19BeT%2Fzg%2Bi%2B4l0v5N78aoYlH%2BEnK0r3Zp7r7W6TgdA7CKPed1EE04%2BNWJnAOiTKOIYWAhonS%2FgEiH936EL3FAqLHM7Wem%2BBqC%2FjW7zZrieP0ernIWxS822Lz5UXnoAo2bPKXN%2FTZH8Gsw2Bv6DXmcwgbf%2F0gY6pgHKerkGfR9%2Bez6GTCrrWe9EgNkZt6%2FL4MKXr11fUls6wrcuK8x9qJGW9AOjqPkdviKnPqYNamDlul85ZUOPkTqSR1djRJYBZlftadd%2Fp%2FiYjVU0LZUA4XvTL6P93xKaAbG4kyigsRy1h2NHLjIkyTwvrRl0t9FLS3kwcCX%2FoZetgmW4vcrgevjYEMTNuzac9%2BjqtirqhwQNCMlapYP4sG22QZtO1NTz&X-Amz-Signature=c8218a07aab005c7f885ac56c21b22a7cf54f7c1adfe8554a05fc73b0c92a361&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

hey 慕课网的各位同学们，大家好，这一节当中咱终于要介绍到 sleuth 的好搭档 zip king 了 zipkin 的用途在前面的图文小结里已经跟大家介绍过了。我们这个 zipking 集成部分分为上半场和下半场。在上半场中咱的内容非常非常简单，就是搭建一个 zip king 的服务端。如果大家对 zip king 没有特殊的定制要求，其实是直接可以使用官方提供的价包来搭建这个服务端的。但是我们这里为了让大家更好的理解 zip king 的启动流程，我们就手把手的教大家来如何通过 palm 文件引入 zipking 依赖，然后启动 zipking 服务。 

[image](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/163e140e-d9b1-4e99-b39e-ae6d57998082/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VTONEK4V%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T225759Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIBIyehUBj7eN41%2BIAY%2BNqPosAb6EGyvluK9MPBYBEX8gAiA5X27we3k1SG%2B1%2BsNI9L7c9FByHmKXN59YPCRAuveY9yqIBAjG%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMnBiHIfQcq9xIQxgNKtwDO1hljGirRaKdEPVQwn5GenuE4QTUmQXeaN%2FISNhRggHQ4vNZhdkqKm0WWycegwxHl6x7gYSHQTHv5FnGNrU7tY5K2RPH9RZFnkfFRyYCmh%2Fuwo66mNFy%2BiwjI2EK2rjAA2K0bopSegCTO5VCLlJtdSkELnEf0VnijD6kNk3w%2B9vEJuME62Z3nhwuMkgdndSWISsfkaekFNaSpic3fGIoQ%2B6JzvYTd49fG%2F2ilbM5UpihaAS9QT6LqL9ZTCVst33L%2B5oZ9wh8XCqDBxJQRSltCh15UvDxULxFg8MfrPgARqFFuZthQrWkwqTagmLhUoVnXRWJbLLHvVDdsIp4Hq6jn80kmJD4y%2FniahxQkzqVpVfPTKKKl66K4ROq0sXzXPlUUk1mCsRTpagGrWZj9Edb4r8SyhGUj5yyYuMjWX%2FiWBGK3NBTS5JZ8PYgJf%2BJjQh9WPKpeE%2B2gwIPV17ORsAS6WzPn0n0bm3lRVEBfr19BeT%2Fzg%2Bi%2B4l0v5N78aoYlH%2BEnK0r3Zp7r7W6TgdA7CKPed1EE04%2BNWJnAOiTKOIYWAhonS%2FgEiH936EL3FAqLHM7Wem%2BBqC%2FjW7zZrieP0ernIWxS822Lz5UXnoAo2bPKXN%2FTZH8Gsw2Bv6DXmcwgbf%2F0gY6pgHKerkGfR9%2Bez6GTCrrWe9EgNkZt6%2FL4MKXr11fUls6wrcuK8x9qJGW9AOjqPkdviKnPqYNamDlul85ZUOPkTqSR1djRJYBZlftadd%2Fp%2FiYjVU0LZUA4XvTL6P93xKaAbG4kyigsRy1h2NHLjIkyTwvrRl0t9FLS3kwcCX%2FoZetgmW4vcrgevjYEMTNuzac9%2BjqtirqhwQNCMlapYP4sG22QZtO1NTz&X-Amz-Signature=bbf1b774338646b8cf7889e1508225b4075e8fddf79d9efdcdc44bf67821e06e&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

OK 这一节是一个短平快的章节，非常的简单轻松。同学们准备好的话就跟我一起开工吧。编程是我快乐 996 是我的福报。


又到了享受福报的时候啊，啊咱今天来创建一个 zip king 的服务端，我们先来创建这个 module 给它起名就叫做 zipking 杠 server okay next 然后把 zip king 也同样的放到 sloose 的文件夹下面。虽然它并不能说是 spring cloud 的一部分，但是毕竟考虑到它和斯鲁斯的好记有关系，咱就把这俩放一块了。


OK 好，我们这里来添加它的 dependency 很可惜这次不能抄作业了咱的 dependency 全是全新的，它不用依赖其他的 spring cloud 组件。好，我们这里添加第一个 dependency 它是 zip king 自己的后端服务的 dependency 它的 group ID 是 io.zipkin.java 然后 artifact 是 zipkin 杠 server 大家看这个 group ID 很少见有这样命名的。你从这 group ID 就能读出 zipking 的狼子野心，不仅想统治 Java 估计这后面还有什么点 php.python 之类的。那它的 version 咱这里给它指定一下使用一个二点八点四的稳定版本。 OK 那它的后端服务处理好了，接下来要添加一个前端的 uizip king 是包含前后端的服务 zipkin 的后端服务主要是用来做分析查找，然后接收 log 它的前端服务就是给用户提供一个页面来搜索。


```java
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
   </dependencies>

    <build>
        <plugins>
            <plugin>
                <groupId>org.springframework.boot</groupId>
                <artifactId>spring-boot-maven-plugin</artifactId>
                <configuration>
                    <mainClass>com.imooc.springcloud.ZipkinApplication</mainClass>
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
```

OK 它的 group ID 依然是 io.zipking.java 我们把上面复制下来，它的 artifact ID 是 zip king zip king 杠 auto configure 杠 uiok 那我们给它指定一个版本，它的版本同样的也和上面保持一致，是二点八点四这两个是搭配使用的。大家如果引入这两依赖可以使用相同的版本。
OK 那接下来咱还要给 zipking 做一个特殊的配置咱给它添加一个 build 因为 zipkin 其实是可以直接使用官方提供的价包的。所以我们既然这里把它封装了一层，那就要把它给重新的打一个 body package 一下。 OK 那这里引入了一个新的 plugins 这个 plugin 是谁呢？我们在这边添加上它的节点之后，给它添加一个 group idgroup ID 是 orgorg spring framework 然后 boot 它这里不是 cloud 了，这里是 boot 了，同样的 artifact ID 是 spring boot Maven plucking boot Maven 这里跳出来了，就是你了，接下来配置一个它的主要的配置项 configuration 这里面咱要指定自己的 main class 是谁，待会儿等创建好了，我们再来把它添加进去，然后在下面添加一个执行计划。 executions 好执行什么内容，你的目标 growth 就是 repackage 重新打包。


好嘞，实际上这种 XML 描述语言真的是蛮繁琐麻烦的。我其实虽然是从那个年代过来的人，但是特别不喜欢这种描述语言，太繁琐了，而且一点也不简洁高效。 OK 那这里定义完了以后，我们来创建一个启动的 main class 这个 main class 我们依然先给它创建一个如雷贯耳的包名， 

com.imock.spring cloud 好嘞，在这里面无中生有来它一个类名字就叫做 zip king applicationok 好，这里咱终于可以抄一次作业了，抄谁的？抄这个启动类的慢方法，咱随便挑一个类就 loose 了。好基友里面的 man 方法，把它给 copy 进来，放到 zipking application 里面。好嘞，把类名替换一下，然后开始最欢乐的章节给启动类戴绿帽子。


咱第一个帽是 spring boot application sprint boot application 好，这第二个冒就是 enable zip king server 大家看到这里有两个annotation ，其中一个被标记为 duplicate 也就是不建议大家使用了。那上面一个咱可以用进来。实际上这个 zip king 特别的矫情。你看这两个类。大家看这个没有被标记为 deprecator 的类，它也就 import 了一个 internal zip king configuration 咱们再看这个被标记成 duplicate 的类，你看它 import 的 configuration layer 和前面那个 zipkin server annotation 是一模一样的。那为什么长得一模一样的两个 annotation 啊？偏偏这一个被标记成了duplicate ，我们看一下，这个 zip king 非常的无聊，bae标记为 duplicate 的这个annotation ，它的位置是在 zipkin server 包下的最外层。而另外一个相同的annotation ，它在里面这个 internal 的文件夹里面就在这了。


你说 zip king 的那帮开发人员是不是非常的无聊啊？我们不管它了，咱在这里引入 enable zipking server 注解，然后就可以去创建配置文件了。咱的配置文件和其他的 spring cloud 项目比起来还非常的少。我们创建一个 application.properties 收起小桌板，咱接下来看看 properties 里面都有什么内容。内容着实不多，只有四项。第一个当然是咱应用的名称了，叫 sprint [application.name](http://application.name/) 我们给它依然起名叫 zip king server。 Ok. 第二个是 server port 端口号咱端口号用的太快了，要省着点用。还是，62,100。 OK 接下来再定义一个允许并重载的 annotation 咱之前在份章节里有定义过，sprint man.alabin definition got override overriding okay 这个是用来做什么作用呢？因为咱前面不是引入了两个依赖，一个是后台 server 一个是 UI 界面。这两个依赖加载的时候会有类冲突，所以啦会导致启动失败，咱把这个允许并重载的开关给它打开，那么这样的话就不会再启动报错了。
Ok. 除了这三个配置以外，还有一个它的名称叫做 management metrics metrics web server 然后再来一个点 auto time requestok 它的值是 false 这个属性其实咱大家不加的话，它也不会导致启动报错，业务也能正常运行。只不过在后台启动窗口的时候会看到一些错误日志。


咱现在四条属性都已经配置完了，万事俱备，我们可以去尝试着启动 zip king 了。 OK 打开小桌板找到闷方法，我们直接把它启动起来。 OK 稍等半柱香的时间。你看它这个启动界面非常酷炫啊一个小人啊丘比特之箭啊。Zipking.好，我们往下看，它这边已经显示启动起来了。我们到浏览器里面把 zpin 的主页打开，看它是不是可以正常的显示搜索界面。咱把 zipking 的地址打上 local host 端口号是 62,100 zipkin 点击回车。

```java
http://localhost:62100/zipkin/
```

[image](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/704028c5-85a7-4b7f-8a94-7ac3d0a41fc4/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VTONEK4V%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T225759Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIBIyehUBj7eN41%2BIAY%2BNqPosAb6EGyvluK9MPBYBEX8gAiA5X27we3k1SG%2B1%2BsNI9L7c9FByHmKXN59YPCRAuveY9yqIBAjG%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMnBiHIfQcq9xIQxgNKtwDO1hljGirRaKdEPVQwn5GenuE4QTUmQXeaN%2FISNhRggHQ4vNZhdkqKm0WWycegwxHl6x7gYSHQTHv5FnGNrU7tY5K2RPH9RZFnkfFRyYCmh%2Fuwo66mNFy%2BiwjI2EK2rjAA2K0bopSegCTO5VCLlJtdSkELnEf0VnijD6kNk3w%2B9vEJuME62Z3nhwuMkgdndSWISsfkaekFNaSpic3fGIoQ%2B6JzvYTd49fG%2F2ilbM5UpihaAS9QT6LqL9ZTCVst33L%2B5oZ9wh8XCqDBxJQRSltCh15UvDxULxFg8MfrPgARqFFuZthQrWkwqTagmLhUoVnXRWJbLLHvVDdsIp4Hq6jn80kmJD4y%2FniahxQkzqVpVfPTKKKl66K4ROq0sXzXPlUUk1mCsRTpagGrWZj9Edb4r8SyhGUj5yyYuMjWX%2FiWBGK3NBTS5JZ8PYgJf%2BJjQh9WPKpeE%2B2gwIPV17ORsAS6WzPn0n0bm3lRVEBfr19BeT%2Fzg%2Bi%2B4l0v5N78aoYlH%2BEnK0r3Zp7r7W6TgdA7CKPed1EE04%2BNWJnAOiTKOIYWAhonS%2FgEiH936EL3FAqLHM7Wem%2BBqC%2FjW7zZrieP0ernIWxS822Lz5UXnoAo2bPKXN%2FTZH8Gsw2Bv6DXmcwgbf%2F0gY6pgHKerkGfR9%2Bez6GTCrrWe9EgNkZt6%2FL4MKXr11fUls6wrcuK8x9qJGW9AOjqPkdviKnPqYNamDlul85ZUOPkTqSR1djRJYBZlftadd%2Fp%2FiYjVU0LZUA4XvTL6P93xKaAbG4kyigsRy1h2NHLjIkyTwvrRl0t9FLS3kwcCX%2FoZetgmW4vcrgevjYEMTNuzac9%2BjqtirqhwQNCMlapYP4sG22QZtO1NTz&X-Amz-Signature=24b250326615e5f2e345be31afbec0b79fccfbd44fa7483a538bf183d6262ac8&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

好嘞，这就是 zipkin 的主页面。那这页面上的搜索功能都有什么作用呢？比如说这个功能等等这个功能就是下一节课的内容了。


我们这一节也就是上半场的 zipking 集成就到这里结束了，咱已经动手搭建了一个 zipking server 那么在下半场里，我将带大家去改造咱前面创建的 sloose 项目，把生成的 log 统统都喂给 zipking 所以 zipking 系统的功能我们下一节再揭晓。好同学们，我们下一小节再见。



