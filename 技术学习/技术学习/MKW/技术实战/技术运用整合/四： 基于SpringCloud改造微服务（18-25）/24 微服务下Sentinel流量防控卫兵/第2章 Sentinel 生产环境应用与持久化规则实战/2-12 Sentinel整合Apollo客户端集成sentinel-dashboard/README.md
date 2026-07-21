---
title: 2-12 Sentinel整合Apollo客户端集成sentinel-dashboard
---

# 2-12 Sentinel整合Apollo客户端集成sentinel-dashboard

[image](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/45091457-b64d-45b4-91e9-8aa04fa7eb7e/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46647YXTXHJ%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T225849Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIEkaLxLTOLXjBsa3g5XSC5kWUDJRcv04dC7qDDKmR%2BSiAiAocSgx73tzuoSQWMNIBRVxilWw4jvdmMertS7RixYMHCqIBAjG%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMS5pZkDkJU32CWP31KtwD4m7tCr3oZXgPlQuSMzo9PES65UDPRama7r460wjEzOk%2BvpPnw2YIZTZsgLT2XgiByCgVFGFJylNK88NlVn%2Fyzj1ugDxp63WScvanElbmeBObQPGDmP2fg%2BaHUmVOLEKqwK8DK1kf4XE1BtNtCjd73BjezhdfxaD5ep02wTsc48SrOyhWF0CWrDcxx24r8I23ZK8Xl3cZA1E%2BUkOyLjrB0ElFQyU72d68AWYbqT6OXlAFy79PpMll6NMJjc%2FLhCJI5z6zkL2gok%2Fem9kUKgM7S4XqsmN9yijbsQU7Cz%2BmC21S0266WVuS5rACIt9HcJyKPV67Eu4g%2BESqMosXEuJxStNCewMCC5TR8hKz5NSgPP4oa2Odv0lJ5mJYh%2Fql6UofIRT9Ip5amjVwjIyzMfH8bb2ovVhpvFt003g1dvVpI5XcvER88%2Bm3Ri%2F7vr4dCwJQn2hi7cyda0LYYcarKscqeBdPUKDRwiQsdC%2Fnm7oDcyjx6ODCBawErCUwFJHrwYTWPB3R6bUnkEGE1GCWobotFh9jujU73U5c8X2EQ8%2B41ZRM%2FRUFvcTG2EGwbtbwq2z73hnIsvXW9DU8rtju7JmUNSBD1bXO9wVZ8AGgSc5ae6TVjCgcsPkJ71aIuW4w2rr%2F0gY6pgEJ8egl6sgQVPBZILvPQ%2F7oSMC55y4GRxaxKqqf6mzIvTR7Aeskoaxsvv8nZuFsxEy3pWzn9SnXqrIQc4dbxNYeszc%2BezExpUmAaP8OA1TWtv1DlL5zY%2BM8w1bvOdswjtIxZYecEZWRg1hqsZA%2BiMuqtO6prhJSwK67JBfXu4Rc1YKI3cTBhzCMoObCXLxX6aCwwzjmZaE4PVSZ0fYnOympqV%2Fu7xpu&X-Amz-Signature=3f3ce5d92729f72d1a0e521419333a206f5378e44cb78f65486f2f848ee288e4&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

[image](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/cf2d6dd9-776b-44b1-9fa2-650bde346584/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46647YXTXHJ%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T225849Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIEkaLxLTOLXjBsa3g5XSC5kWUDJRcv04dC7qDDKmR%2BSiAiAocSgx73tzuoSQWMNIBRVxilWw4jvdmMertS7RixYMHCqIBAjG%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMS5pZkDkJU32CWP31KtwD4m7tCr3oZXgPlQuSMzo9PES65UDPRama7r460wjEzOk%2BvpPnw2YIZTZsgLT2XgiByCgVFGFJylNK88NlVn%2Fyzj1ugDxp63WScvanElbmeBObQPGDmP2fg%2BaHUmVOLEKqwK8DK1kf4XE1BtNtCjd73BjezhdfxaD5ep02wTsc48SrOyhWF0CWrDcxx24r8I23ZK8Xl3cZA1E%2BUkOyLjrB0ElFQyU72d68AWYbqT6OXlAFy79PpMll6NMJjc%2FLhCJI5z6zkL2gok%2Fem9kUKgM7S4XqsmN9yijbsQU7Cz%2BmC21S0266WVuS5rACIt9HcJyKPV67Eu4g%2BESqMosXEuJxStNCewMCC5TR8hKz5NSgPP4oa2Odv0lJ5mJYh%2Fql6UofIRT9Ip5amjVwjIyzMfH8bb2ovVhpvFt003g1dvVpI5XcvER88%2Bm3Ri%2F7vr4dCwJQn2hi7cyda0LYYcarKscqeBdPUKDRwiQsdC%2Fnm7oDcyjx6ODCBawErCUwFJHrwYTWPB3R6bUnkEGE1GCWobotFh9jujU73U5c8X2EQ8%2B41ZRM%2FRUFvcTG2EGwbtbwq2z73hnIsvXW9DU8rtju7JmUNSBD1bXO9wVZ8AGgSc5ae6TVjCgcsPkJ71aIuW4w2rr%2F0gY6pgEJ8egl6sgQVPBZILvPQ%2F7oSMC55y4GRxaxKqqf6mzIvTR7Aeskoaxsvv8nZuFsxEy3pWzn9SnXqrIQc4dbxNYeszc%2BezExpUmAaP8OA1TWtv1DlL5zY%2BM8w1bvOdswjtIxZYecEZWRg1hqsZA%2BiMuqtO6prhJSwK67JBfXu4Rc1YKI3cTBhzCMoObCXLxX6aCwwzjmZaE4PVSZ0fYnOympqV%2Fu7xpu&X-Amz-Signature=7a9e10c7288f61ca8078d520396f506a5a2da6b81deafe387dbcf9517fb26ad0&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

[image](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/3f818ad4-9c03-4f9c-a736-d5cee5ad388b/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46647YXTXHJ%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T225849Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIEkaLxLTOLXjBsa3g5XSC5kWUDJRcv04dC7qDDKmR%2BSiAiAocSgx73tzuoSQWMNIBRVxilWw4jvdmMertS7RixYMHCqIBAjG%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMS5pZkDkJU32CWP31KtwD4m7tCr3oZXgPlQuSMzo9PES65UDPRama7r460wjEzOk%2BvpPnw2YIZTZsgLT2XgiByCgVFGFJylNK88NlVn%2Fyzj1ugDxp63WScvanElbmeBObQPGDmP2fg%2BaHUmVOLEKqwK8DK1kf4XE1BtNtCjd73BjezhdfxaD5ep02wTsc48SrOyhWF0CWrDcxx24r8I23ZK8Xl3cZA1E%2BUkOyLjrB0ElFQyU72d68AWYbqT6OXlAFy79PpMll6NMJjc%2FLhCJI5z6zkL2gok%2Fem9kUKgM7S4XqsmN9yijbsQU7Cz%2BmC21S0266WVuS5rACIt9HcJyKPV67Eu4g%2BESqMosXEuJxStNCewMCC5TR8hKz5NSgPP4oa2Odv0lJ5mJYh%2Fql6UofIRT9Ip5amjVwjIyzMfH8bb2ovVhpvFt003g1dvVpI5XcvER88%2Bm3Ri%2F7vr4dCwJQn2hi7cyda0LYYcarKscqeBdPUKDRwiQsdC%2Fnm7oDcyjx6ODCBawErCUwFJHrwYTWPB3R6bUnkEGE1GCWobotFh9jujU73U5c8X2EQ8%2B41ZRM%2FRUFvcTG2EGwbtbwq2z73hnIsvXW9DU8rtju7JmUNSBD1bXO9wVZ8AGgSc5ae6TVjCgcsPkJ71aIuW4w2rr%2F0gY6pgEJ8egl6sgQVPBZILvPQ%2F7oSMC55y4GRxaxKqqf6mzIvTR7Aeskoaxsvv8nZuFsxEy3pWzn9SnXqrIQc4dbxNYeszc%2BezExpUmAaP8OA1TWtv1DlL5zY%2BM8w1bvOdswjtIxZYecEZWRg1hqsZA%2BiMuqtO6prhJSwK67JBfXu4Rc1YKI3cTBhzCMoObCXLxX6aCwwzjmZaE4PVSZ0fYnOympqV%2Fu7xpu&X-Amz-Signature=46b2b2d9fa40a14b83615bc1728fc4700d9e0cb370d4854c1df0de38f98b0bc3&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

我们已经对这个 sentence dashboard 进行了一个集成阿波罗的扩展。当然这些项目已经运行起来了，但是没有抛任何异常，但是我们也不能确定我们扩展的就是 100% 正确的，后面我们会做一个小的验证。那现在我们对于这个 dashboard 的已经扩展完了，接下来我们要做什么事情呢？那我们来看一看这个生产环境中对于 sentence 的一个使用还是回到我们的这种 push 模式，也就是生产环境中最常用的模式。我们来看一下这幅图，继续来看一下。

[image](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/bdfc47b6-0fbe-413f-841d-8bbbb8c30df0/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46647YXTXHJ%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T225849Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIEkaLxLTOLXjBsa3g5XSC5kWUDJRcv04dC7qDDKmR%2BSiAiAocSgx73tzuoSQWMNIBRVxilWw4jvdmMertS7RixYMHCqIBAjG%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMS5pZkDkJU32CWP31KtwD4m7tCr3oZXgPlQuSMzo9PES65UDPRama7r460wjEzOk%2BvpPnw2YIZTZsgLT2XgiByCgVFGFJylNK88NlVn%2Fyzj1ugDxp63WScvanElbmeBObQPGDmP2fg%2BaHUmVOLEKqwK8DK1kf4XE1BtNtCjd73BjezhdfxaD5ep02wTsc48SrOyhWF0CWrDcxx24r8I23ZK8Xl3cZA1E%2BUkOyLjrB0ElFQyU72d68AWYbqT6OXlAFy79PpMll6NMJjc%2FLhCJI5z6zkL2gok%2Fem9kUKgM7S4XqsmN9yijbsQU7Cz%2BmC21S0266WVuS5rACIt9HcJyKPV67Eu4g%2BESqMosXEuJxStNCewMCC5TR8hKz5NSgPP4oa2Odv0lJ5mJYh%2Fql6UofIRT9Ip5amjVwjIyzMfH8bb2ovVhpvFt003g1dvVpI5XcvER88%2Bm3Ri%2F7vr4dCwJQn2hi7cyda0LYYcarKscqeBdPUKDRwiQsdC%2Fnm7oDcyjx6ODCBawErCUwFJHrwYTWPB3R6bUnkEGE1GCWobotFh9jujU73U5c8X2EQ8%2B41ZRM%2FRUFvcTG2EGwbtbwq2z73hnIsvXW9DU8rtju7JmUNSBD1bXO9wVZ8AGgSc5ae6TVjCgcsPkJ71aIuW4w2rr%2F0gY6pgEJ8egl6sgQVPBZILvPQ%2F7oSMC55y4GRxaxKqqf6mzIvTR7Aeskoaxsvv8nZuFsxEy3pWzn9SnXqrIQc4dbxNYeszc%2BezExpUmAaP8OA1TWtv1DlL5zY%2BM8w1bvOdswjtIxZYecEZWRg1hqsZA%2BiMuqtO6prhJSwK67JBfXu4Rc1YKI3cTBhzCMoObCXLxX6aCwwzjmZaE4PVSZ0fYnOympqV%2Fu7xpu&X-Amz-Signature=2be9832ec2982e24a4ed54db0823a99676f28cf25ed0ecf8987f1b199eea16f3&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

其实我们的第一步骤就是我们的 dashboard 直接操作我们的这个配置中心，当然老师在这里用的就是阿波罗了对吧？那其实我们上节课一整节课做的事情，就是对于 dashboard 操作阿波罗使用它的第三方那个 Open API 也就是说 new 出来的那个阿波罗 client 然后去对它进行一些增删改的一些操作，包括一些这个更新、部署、发布等等的一些操作，那个 API 都是上节课的一些封装。那其实说白了，上节课只做完第一步，那这节课我们来做第二步。


第二步什么意思呢？就是说我们通过这个界面操作 dashboard 然后去更新阿波罗，阿波罗里的配置发生变更，我们是不是要及时的去通知到我们具体的某一个真正接入的客户端就是 client 端对吧？那么我们 client 端要知道具体哪一个 key 发生变化了，然后我应该去更新跟我没关的 key 发生变化，其实我是不需要更新的对吧。所以在这里我的 client 端肯定会有一个 listener 这个你可以理解为它跟 nuckles 和 zookeeper 一样，比如说阿波罗里的数据发生变化，那我们的对应的客户端写一个蕾丝去监听就好了，只要这个监听的 key 发生变化，我就可以及时感知，感知到了之后我就可以更新，把我自己本地内存做一次刷新就可以了。

```java
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

    <dependency>
        <groupId>com.alibaba.csp</groupId>
        <artifactId>sentinel-annotation-aspectj</artifactId>
        <version>1.8.6</version>
    </dependency>

        <!-- https://mvnrepository.com/artifact/com.ctrip.framework.apollo/apollo-client -->
        <dependency>
            <groupId>com.ctrip.framework.apollo</groupId>
            <artifactId>apollo-client</artifactId>
            <version>2.0.0</version>
        </dependency>

        <!-- https://mvnrepository.com/artifact/com.ctrip.framework.apollo/apollo-core -->
        <dependency>
            <groupId>com.ctrip.framework.apollo</groupId>
            <artifactId>apollo-core</artifactId>
            <version>2.0.0</version>
        </dependency>

        <!-- https://mvnrepository.com/artifact/com.alibaba.csp/sentinel-datasource-apollo -->
        <dependency>
            <groupId>com.alibaba.csp</groupId>
            <artifactId>sentinel-datasource-apollo</artifactId>
            <version>1.8.6</version>
        </dependency>

        <!-- https://mvnrepository.com/artifact/com.alibaba.csp/sentinel-datasource-extension -->
        <dependency>
            <groupId>com.alibaba.csp</groupId>
            <artifactId>sentinel-datasource-extension</artifactId>
            <version>1.8.6</version>
        </dependency>
```


好了，那这个就是我们接下来要做的事情。第二步好了，那我们来看一看第二步应该怎么去做，我们打开代码，那我们要做第二步，以这个阿波罗杠 test 为例，因为它是我们已经注册过的，并且已经在 dashboard 已经配置好。那我们接下来要做什么事情呢？第一步，你要加入对应的几个依赖，我们现在看看我们有几个依赖了，我们除了有对应的 spring 的依赖，还有这个阿波罗的 call 这是必须要有的。通信 HTTP simple 然后 aspect G 就是 AOP 的假设说我们要使用注解的话，你肯定得需要 aspect G 这个依赖。然后这个是协程的 clang 端对吧。现在我们要做的是再加两个服务，两个依赖。第一个依赖就是它的这个 sentence data source 的 extension 包，还有一个叫做 sentence date source 的阿波罗集成的包，就是说需要加这两个包进来，然后保存加这两个包进来之后我就能做我们想要做的事情了。那接下来我们继续往下看。


那我们要做什么事情？首先我们这个应用项目里边，现在它就是一个单纯的项目对吧？那其实我要做的事情很简单，就是两件事情。第一个就是我要写一个配置类，这个配置类做什么呢？配置类做的事情就是我们使用注解的时候，必须要有一个这个 aspect G 注入，就把那个切面注入进来这才行对不对？第二件事情是我们要写一个监听对不对？我们这个监听的目的就是干什么？监听阿波罗上我们感兴趣的那个 key 它如果发生变化了，我们直接及时的感知到，并且刷新到我们这个阿波罗杠 test 就这个 client 端的一个内存缓存中规则刷新到本地。


好，那我们现在就开始做这个事情。首先创建一个 class 这个 class 我们就叫做 sentence full 阿波罗 config 可以吧，我们把该大写的都大写好，那这个它顾名思义肯定是一个什么？肯定是一个 annotation 对吧？ Config ration. 然后比如说它这里边，我们看它的项目名称我们得取到对不对这个项目名称 application name 必须要取到。为什么呢？我们取到它了之后，然后后面我们做拼接的时候才能拼接出来我们感兴趣的 key 如果这块你不明白，一会我写完代码你就懂了，先把它拿出来冒号。好，这样我们先用一个字符串 private 的这个 Gin 的 application name 去接收一下，默认可以给它一个空串。


然后第二件事情就是我们要注入我们自己我们切面的一个 bin 就是我们想用那个注解 conditional on missing bin ，我们 public 然后那个 bin 的名称就是用 sentence 注解叫做 sentence exhaust 。 aspect 对，就是它因为你只有把这个 bin 注入到 spring 然后它才能帮你去做切面，这是必须要有的。然后我可以把首字母小写，就它然后 return new 一个出来就好了，非常简单。


第一件事情搞了，那就是咱们来搞第二件事情。第二件事是什么呢？就是我们自己要搞一个并出来，这个并出来做的目的是干什么呢？就在做监听的。那我们写一个 public 我们叫阿波罗。阿波罗什么呢？ data source source listener 可以吧。阿波罗 data source listener 这是我们自己定义的一个类，把这个类先弄出来，好就是它。然后这个类小写是不是也要把它交由 spring 去做管理？然后我们就 return 直接 return new 一个它出来 new 它出来我们可以给它传个参数，就我们要把这个 application name 传进去，因为我们后面要做这个我们感兴趣的 key 的一个拼接，在这里我们去创建构造方法。


OK 好，基本上我们现在已经完成了这个 configuration 的代码。那接下来剩下一件事情就是完成监听，就这个 listen 怎么去做？首先我们声明一个成员变量， private string 它叫做 application name 然后在这里边就是 this.application name 等于 application name 搞定了这个事情之后，由于它是一个普通的 Java 类，怎么去交给 spring 管理是我们在 config 里面去把它弄出来，然后把它注入到 spring 里的对吧，at bin 注解。然后名字这就叫做 apple loted source listen 这样的话，它什么时机去加载规则？说白了它要加载规则，而且是动态的去加载规则。动态的只要我们的这个阿波罗里边他感兴趣那个规则发生变化了，那我们就第一时间感知到，然后刷新就可以了。


那这怎么去做呢？很简单，我们比如说找一个这个类的比较恰当的生命周期。一般来讲很多时候其实你就用这个 init 来做并就够了。什么事情我们就加载规则，init现在先加载一个 follow ruler 是吧。 rulers 好，就加载它，然后它是一个 private 的方法可以了。这规则我们怎么去做？我们可以把之前的那个代码 copy 过来。之前我们写 dashboard 里边自己拼的那个规则字符串，如果记不住的话，我们就把它拿过来，我们来找一下，就在这里。记得就这个东西，这就是我们自己拼的东西拼的那个串，然后我们直接把它放到这里就好了，放到上面。好搞定。那现在已经有了它了，那我们要拼的规则是什么呢？就是我们自己的项目名称加上后面的后缀杠 polo 杠 rules 对吧，因为我们自己的 key 是这样保存的。那你前面这个项目名怎么去取出来啊？无非就是我们的 oblique name 我已经住进来了，它已经有了引用了。所以说现在这里边我们要实现这个动态监听阿波罗，我们就还是写一写，看看怎么去做。


首先第一件事情你要把你自己感兴趣的 key 拼出来，比如说我们叫做 follow rulerkey 是什么？很简单，就是你的 application name 加上拼好的这个 follow ruler ，这个后缀，它的这个拼出来的结果无非就是你的姓名加上后缀，姓名是我在这取的叫这个名字对吧，在这它拼出来就是这样的，把这个拿过来。好，它拼出来这个 key 就是这个对不对？这个 key 就是我们在 dashboard 中操作 follow 入了这种规则，做实际存储的时候，它的 key 也是这样的对吧。好了，那我们就只监听这一个 key 就够了。
对不对？ follow ruler 确实可以是多个的话，因为它是一个 list 集合。还记得吧，因为我们之前去对它的这个 service 去写 dashboard 扩展的时候，它有两个东西，一个叫做 follow ruler 阿波罗 provider 还有一个是 follow ruler 阿波罗 publisher 那他反正发布的内容就是这个东西对不对？就是一个 list 的 follow ruler entity 对吧？好，那这样的话我们来看看我们怎么去做。现在已经知道我们感兴趣的 key 了。接下来做的一件事情就是我们加一个动态的监听对不对？动态监听在这里边我们直接用 readable 阿波罗的一个叫做 readable data source 它是我们 sentence 跟阿波罗集成的时候，它自己帮我们去扩展的一个接口。 key 是什么？ key 其实就是 spring 就是你的这个 follow ruler keyvalue 在这里我们其实刚才已经有了，就是他 follow ruler 就是你对应的 value 一定是 follow ruler。为什么这么去说？因为我们在原生 API 的时候，因为你这是一个 clan 端对不对？回首一下我们自己的 client 端，我们来看一下这个 base demo 或者我们自己写的最开始的最简单的 demo 我们就看 colora 的小程序就好了。


自己的规则我们加载的时候是不是我们都是用这个 follow ruler manager.load rulersload rulers 做的事情是对，这个 follow ruler 它识别对不对？也就是说这个缓存里它存储的对象叫做 follow ruler 它不叫做 follow ruler entityfollow ruler entity 是 dashboard 就是我们 dashboard 里边使用的这个 provider 跟这个 publisher 它使用的是 follow roantity 如果你把它加进来，它肯定会报类型转换异常，不信小伙伴们可以去自己试一试。我在这里就不说了，直接给结果。也就是说我们在这里你要注意一点，这是我监听的 key 所对应的 value 它是一个 list follow ruler 而不是 list follow ruler entity 为什么？因为刚才我们看到了我们原生使用的时候就要用 follow ruler 所以说在这儿一定要强调一下，这个小伙伴们要注意。


然后接下来就简单了，接下来你就把这个 date source 给它弄出来就好了，我们就给它起个名字，叫做 follow date source 。 source 等于什么呢？等于我们 new 一个阿波罗贝塔source ，这个阿波罗 date source 也是哨兵给我们提供的这个类。我们看一下，只需要按照它的 API 去填充东西就好了。好，它需要填充这几个东西。那这几个东西分别代表什么意思呢？第一个， namespace namespace 其实我们可以写死了，如果你没有什么特殊的要求的话，我们就叫做 application 就好了。
这个 ruler key 就是我们自己感兴趣的规则，就是它是不是 follow 入了 T default 呢？就默认的情况下我们可以给它一个空串，因为它是一个 list 对不对？ list 转换成 JSON 之后就是一个空串对吧？空的 list 转换成 JSON 好了，最后一个 passer 这个 passer 是什么呢？说白了就是你要把一个 source 怎么去转成这个 listfor ruler 就是我们的一个 JSON 转换，可以用这个 limit 表达式去写。


我们对 source 做转换，怎么去转换 json.pass object gson.pass object pass object 怎么去转？首先语言数据就是肯定是source ，字符串转成什么样的数据呢？肯定要转成一个 fleet flow ruler 对不对？在这里面我们可以有一个类叫做 type referencetype reference 注意你在这里一定要选择自己的阿波罗的，我们找一找 type reference 这里有好多要找到，比如我们自己的这里边有几个在这儿 fast JSON 好了，然后这里边转的类型是什么呢？我们现在要转的类型肯定就是它了转成它了，把这个泛型替换过来好保存一下，最后它要实现一下。所以说我们来一个空实现，因为它是一个泛型，我们这样抠实线好了，具体什么也不用做。


这样的话，我们现在这个写法已经把我们自己的这个叫做 readable data source 这个东西已经搞定了，就是我们要读取这个内容，读取这个内容之后，然后干什么事情呢？就是我们把它监听动态变化以后，我们一定要把它刷到哪里呢？小伙伴们一定要把它刷到这个本地内存的 follow ruler manager 因为我们看一下我们原生最开始做的时候也是这样的，在写这个 demo test 的时候对不对？我们把规则搞定了之后，我们怎么去填充这个规则刷到内存轴，我们直接是弄出来一个规则，然后用 follow ruler manager load rules 对吧。所以说在这里边相当于你加好了 listener 就是你感性的 key 发生变化了。那我们取到了之后，你要把新的这个内容给它刷到 follow ruler manager 里就好了。


然后它除了有一个 load rulers 以外，还有一个叫做 register to property 当然你用它也可以，你用它的话你自己得把那个转过来，你用这个叫做 register to practice 这个更简单，你直接取到 property 就好了。这个 property 我们直接就可以通过 data source 就是我们阿波罗的这些 source 的 get from this 这样的话我们现在就已经完成了对阿波罗的一个动态监听。 OK 那其实简单说一下这个 init 方法是怎么做的。



第一件事情，对你感兴趣的 key 对不对？你拼出来。第二件事情进行监听。动态监听。今天出来之后你再把它刷新到自己的内存中就完了。好，就这么三步骤。当然老师现在写的是对于 follow ruler 的一个动态监听对吧，那后面你可能还要对什么呢？ degree 的也做一个监听。那这个我觉得小伙伴们就应该课下自己去完成了，包括一些其他的，比如说热点、黑白名单以及一些对应的自适应系统 system block ruler 对吧，其他的规则你就自己都可以去按照老师这几个模板的方式去写一写，包括我们最开始的时候自己写 dashboard 扩展的时候，老师只是给你扩展了 follow ruler 的阿波罗的 provider 跟这个 publish 那如果你想要再加上降级的规则，你是不是写 degree 的 ruler 阿波罗 provider degree 的 ruler 阿波罗 publisher 对吧？就这些都是成套的，对应着你也应该改对应的 controller 需要做修改。因为我们之前只改了 follow controller 你看对应的你要改的话你可能要改 degree 的 controller 或者是 authentic controller 以及对应的 paramfollow 入了 controller 比如说 system controller 比如说对应的营养扩展，那你就自己一个一个改，老师在这里把一套完整的这个扩展的方式跟你讲清楚，那基本上你自己来做就非常简单也会了。


好了，那这节课我们就是针对于现在自己的一个阿波罗杠 test 项目，我们怎么去跟 dashboard 就我们自己扩展的 dashboard 做一个集成，就是刚才这几步骤。那么这节课我们就讲到这，感谢小伙伴们收看。

```java
package com.bfxy.apollo;

import com.alibaba.csp.sentinel.datasource.ReadableDataSource;
import com.alibaba.csp.sentinel.datasource.apollo.ApolloDataSource;
import com.alibaba.csp.sentinel.slots.block.flow.FlowRule;
import com.alibaba.csp.sentinel.slots.block.flow.FlowRuleManager;
import com.alibaba.fastjson.JSON;
import com.alibaba.fastjson.TypeReference;
import org.springframework.beans.factory.InitializingBean;

import java.util.List;

/**
 * <h1></h1>
 */
public class ApolloDataSourceListener implements InitializingBean {

    private static final String FLOW_RULE_TYPE = "flow";

    private static final String DEGRADE_RULE_TYPE = "degrade";

    // *-flow-rules
    private static final String FLOW_DATA_ID_POSTFIX = "-" + "FLOW_RULE_TYPE" + "-rules";
    // *degrade-rules
    private static final String DEGRADE_DATA_ID_POSTFIX = "-" + "DEGRADE_RULE_TYPE" + "-rules";

    // apollo-test-flow-rules
    public static String getFlowDataId(String appName) {
        return String.format("%s%s" + appName, FLOW_DATA_ID_POSTFIX);
    }

    private String applicationName;

    public ApolloDataSourceListener(String applicationName) {
        this.applicationName = applicationName;
    }

    @Override
    public void afterPropertiesSet() throws Exception {
        initFlowRules();
    }

    private void initFlowRules() {
        //  apollo-test-flow-rules 就是拼接出来的 key
        String flowRuleKey = applicationName + FLOW_DATA_ID_POSTFIX;

        // 动态监听
        ReadableDataSource<String, List<FlowRule>> flowRuleDataSource = new ApolloDataSource<>("application", flowRuleKey, "[]",
        source -> JSON.parseObject(source, new TypeReference<List<FlowRule>>(){

        }));

        // 本地缓存起来
        FlowRuleManager.register2Property(flowRuleDataSource.getProperty());



    }
}
```



