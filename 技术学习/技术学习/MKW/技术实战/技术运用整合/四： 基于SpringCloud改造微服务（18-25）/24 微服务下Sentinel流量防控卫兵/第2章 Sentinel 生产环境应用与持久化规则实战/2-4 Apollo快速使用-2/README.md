---
title: 2-4 Apollo快速使用-2
---

# 2-4 Apollo快速使用-2

[image](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/c9220a88-52e2-4834-8ef9-b4b0b2cbadf7/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SNE4PU62%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T225842Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDXeTnCio9WV9Z9QGqiBKyjs5OxrVtbM4vFuJtkBKmk5gIhAK2A7UV5rwJVzJoKaFUOiTWmJgMf2HlyE0asF4gqlyOlKogECMb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgyDfOPtm0qrKf9pK38q3AM3eQ5nuZ896%2FHHcrh%2BmN668bmhFUCOGbdQjyA97L7SNu4hacJQKHgHkYAGdyXzFxUja863wGmD%2FF713AFPoMpHqcA8ofJ6SuxM558fupSxG3hGYjm1ZyLHZe1N7MyL%2Fn9OxFWfAisx9CgetSkmqh4DOnen1WiSJdjd6ZI%2ByCmEg9vfE0hIWQjEOZh9hZt2dW0gn3JlB4NsL6tSzq7reek6IWWpuHlwNq5Rn8DWMFU6SrFyNt0vBebs5hJWSiKMkX0pPtBchgc7PXXKeW8V0tjO7N4lW35%2FMISz7qbiyPN1YG5LHq2mT86Bxf9XUQjsJC85J%2FrypS%2BTH4NNrXsj8ld63fauxCmEOXJ5o8NV3hPgJzzlKgu5b20L%2BuMtYrx%2FWCBscw%2BOBXvPL0QNfHUhlafv1338dyKj7ASQx4Yd7tp8hwDgA42NL1n2llyGsPf3Rg2Tf3t4Cr00b8YALfajYg%2BWeOV2JzI7ava%2F%2BaIwNvx4Yx4c9LWiBuTgBDhrtAkk%2FQW47X4ZoCCPvU%2B1EkFqMJGI7Alt3hJlHHzIAW3vRogFA%2FXx68cv8ks2rjgTa0OjJeEcfttojr3tJb84cyN3%2FxmNzmEWErjxrs5yrH1hAC9CNEnLpYcUzS3qrjFIpzDCt%2F%2FSBjqkAVo%2FMUye8pGrowpxx68I6ekjUKXtl9kmDxK7XJzBwE5GrkBtaFqaLVpUAu0wGr%2FBXiZSd3fOBzgX3nIMc3o5ftCI4nINTkFL12KV6NHtlN9lNDg3OUz8Cv%2BGwhJKWKZeTcQfzNAoe9FghWHA6pY926KbsJ10Ny%2B2sXJVIXCQz7gk60ZGFFakXO8MrWJeHecuIlwJsNmJiz99JZXa1M2lN%2FtM6WE5&X-Amz-Signature=70ad364ded93ddffd78248ef868a8255dbb5372976dac052fb65a6f67edcdd59&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

[image](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/05042fef-adf4-4b7a-acf3-3bc6664b3c77/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SNE4PU62%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T225842Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDXeTnCio9WV9Z9QGqiBKyjs5OxrVtbM4vFuJtkBKmk5gIhAK2A7UV5rwJVzJoKaFUOiTWmJgMf2HlyE0asF4gqlyOlKogECMb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgyDfOPtm0qrKf9pK38q3AM3eQ5nuZ896%2FHHcrh%2BmN668bmhFUCOGbdQjyA97L7SNu4hacJQKHgHkYAGdyXzFxUja863wGmD%2FF713AFPoMpHqcA8ofJ6SuxM558fupSxG3hGYjm1ZyLHZe1N7MyL%2Fn9OxFWfAisx9CgetSkmqh4DOnen1WiSJdjd6ZI%2ByCmEg9vfE0hIWQjEOZh9hZt2dW0gn3JlB4NsL6tSzq7reek6IWWpuHlwNq5Rn8DWMFU6SrFyNt0vBebs5hJWSiKMkX0pPtBchgc7PXXKeW8V0tjO7N4lW35%2FMISz7qbiyPN1YG5LHq2mT86Bxf9XUQjsJC85J%2FrypS%2BTH4NNrXsj8ld63fauxCmEOXJ5o8NV3hPgJzzlKgu5b20L%2BuMtYrx%2FWCBscw%2BOBXvPL0QNfHUhlafv1338dyKj7ASQx4Yd7tp8hwDgA42NL1n2llyGsPf3Rg2Tf3t4Cr00b8YALfajYg%2BWeOV2JzI7ava%2F%2BaIwNvx4Yx4c9LWiBuTgBDhrtAkk%2FQW47X4ZoCCPvU%2B1EkFqMJGI7Alt3hJlHHzIAW3vRogFA%2FXx68cv8ks2rjgTa0OjJeEcfttojr3tJb84cyN3%2FxmNzmEWErjxrs5yrH1hAC9CNEnLpYcUzS3qrjFIpzDCt%2F%2FSBjqkAVo%2FMUye8pGrowpxx68I6ekjUKXtl9kmDxK7XJzBwE5GrkBtaFqaLVpUAu0wGr%2FBXiZSd3fOBzgX3nIMc3o5ftCI4nINTkFL12KV6NHtlN9lNDg3OUz8Cv%2BGwhJKWKZeTcQfzNAoe9FghWHA6pY926KbsJ10Ny%2B2sXJVIXCQz7gk60ZGFFakXO8MrWJeHecuIlwJsNmJiz99JZXa1M2lN%2FtM6WE5&X-Amz-Signature=1d240a83c59d3cf018bf7b96d3ef43af28c0d3a15799486520b135adf237380b&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

老师再次新建一个项目，在这里边我右键去 new 一个新的 man project 然后这个名字我就起阿波罗点test ，用这个 group ID 知道这个名字。然后 artifact ID 叫做阿波罗让 test 好，然后其他的我就不去修改了，直接点 finish 然后创建一个新的项目。


我们看到了在我们最上面有一个阿波罗 test 好，这个项目我们想让它是一个 spring boot 工程。在这里我把一些关键的这个一些依赖包我们先引进来，我们就 copy 之前的这个 test 这里边的依赖，比如说他的这个 parent 还有一些 dependence 我们都给他 copy 过来就可以了。好在这里我们直接粘过来，粘过来之后我们去大化看一看哪些需要修改。


首先我们来看一下我们当前用的是这个 spring boot 215 这个版本 release 版本。然后接下来我们是一个 one project 看见了吧，这是没什么可说的。然后 sentence 哨兵我也引进来了，是不是？并且这个 HD DP 的 transfer simple HD PP 这个东西我也有无所谓。 annotation 这些都是哨兵的东西了，我留着和不留着其实都无所谓。


当然最后最重要的一点是什么呢？你自己是不是要把阿波罗的这个东西就是需要的配置呢？至于这个依赖也要引起来，这是最关键的。所以说在这里我们现在用的阿波罗版本，老师用的是幺点四点零，这是一个比较新的版本了，140版本然后保存。这样的话我们基本上目前的第一步已经做完了，我是一个 spring boot 工程，然后在这里我去建一个目录，叫做 com.bfxy 点阿波罗。好了，然后在这里边他搞定了之后去 update 一下 project 更新一下，可能它需要一个主函数对吧。因为它是一个 spring boot 工程，所以说我把它直接粘过来，application直接粘过来。

[image](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/5c571a47-16c6-424f-8774-6359f9701d5d/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SNE4PU62%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T225842Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDXeTnCio9WV9Z9QGqiBKyjs5OxrVtbM4vFuJtkBKmk5gIhAK2A7UV5rwJVzJoKaFUOiTWmJgMf2HlyE0asF4gqlyOlKogECMb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgyDfOPtm0qrKf9pK38q3AM3eQ5nuZ896%2FHHcrh%2BmN668bmhFUCOGbdQjyA97L7SNu4hacJQKHgHkYAGdyXzFxUja863wGmD%2FF713AFPoMpHqcA8ofJ6SuxM558fupSxG3hGYjm1ZyLHZe1N7MyL%2Fn9OxFWfAisx9CgetSkmqh4DOnen1WiSJdjd6ZI%2ByCmEg9vfE0hIWQjEOZh9hZt2dW0gn3JlB4NsL6tSzq7reek6IWWpuHlwNq5Rn8DWMFU6SrFyNt0vBebs5hJWSiKMkX0pPtBchgc7PXXKeW8V0tjO7N4lW35%2FMISz7qbiyPN1YG5LHq2mT86Bxf9XUQjsJC85J%2FrypS%2BTH4NNrXsj8ld63fauxCmEOXJ5o8NV3hPgJzzlKgu5b20L%2BuMtYrx%2FWCBscw%2BOBXvPL0QNfHUhlafv1338dyKj7ASQx4Yd7tp8hwDgA42NL1n2llyGsPf3Rg2Tf3t4Cr00b8YALfajYg%2BWeOV2JzI7ava%2F%2BaIwNvx4Yx4c9LWiBuTgBDhrtAkk%2FQW47X4ZoCCPvU%2B1EkFqMJGI7Alt3hJlHHzIAW3vRogFA%2FXx68cv8ks2rjgTa0OjJeEcfttojr3tJb84cyN3%2FxmNzmEWErjxrs5yrH1hAC9CNEnLpYcUzS3qrjFIpzDCt%2F%2FSBjqkAVo%2FMUye8pGrowpxx68I6ekjUKXtl9kmDxK7XJzBwE5GrkBtaFqaLVpUAu0wGr%2FBXiZSd3fOBzgX3nIMc3o5ftCI4nINTkFL12KV6NHtlN9lNDg3OUz8Cv%2BGwhJKWKZeTcQfzNAoe9FghWHA6pY926KbsJ10Ny%2B2sXJVIXCQz7gk60ZGFFakXO8MrWJeHecuIlwJsNmJiz99JZXa1M2lN%2FtM6WE5&X-Amz-Signature=5a38d4998bad7f61a129c216dde05b01087f6e21dcced5e8cdb4e0b775a41674&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)


好了，搞定了这件事情之后，这里边有一些没有意义的东西，我都先去掉，都不要这个也不要让它变成一个非常纯粹的 spring boot 工程。好了，那现在我们差什么步骤呢？我们现在还差一步，这一步很简单就是什么就是你自己怎么去跟阿波罗集成。我们首先要加这个注解，叫做 enable 阿波罗 config 在项目中开启阿波罗的客户端，这是第一步要做的事情，就表示开启阿波罗的客户端注解。当然除了这种方式，你还可以使用配置文件的方式去在你的这个 class pass 下写一个这个配置文件，然后定义好也可以，这都行。

```java
package com.bfxy.apollo;

import com.ctrip.framework.apollo.spring.annotation.EnableApolloConfig;
import org.springframework.boot.SpringApplication;
import org.springframework.boot.autoconfigure.SpringBootApplication;

/**
 * <h1></h1>
 */
@EnableApolloConfig   // 开启 apollo 的客户端注解
@SpringBootApplication
public class ApplicationApolloSentinel {

    public static void main(String[] args) {
        SpringApplication.run(ApplicationApolloSentinel.class, args);
    }
}
```

好了，我们现在就用注解方式就好了。接下来我们需要建一个 practice 就是一个配置文件，我们来建一个 application 点儿 purpose application 点儿 properties 建立好这个配置文件之后，把它字符集做一个修改，字符集默认肯定不是u8，我们改成 u8 就好了。


好了，然后接下来我们来看一看我们具体需要做哪些配置，这个做配置也是比较关键的。我们来看一下。首先对于我们基础的这个 spring 的配置，比如说我们当前的这个项目，它的端口就叫 8001 可以吧，它的名字叫做阿波罗杠 test 好。8001，这是关于我们自己的这个服务自身的 spring boot 的一些配置和 spring 的一些配置。然后比较关键的就是阿波罗的配置。阿波罗需要配置哪些呢？首先它要配置。


第一个就是它的 App ID 就是它的应用 ID 是什么，阿波罗的服务应用 ID 这个应用 ID 说的什么意思呢？就是我们自己现在这个阿波罗 test 就每一个服务它自己都有一个英语 ID 说白了就叫 [app.id](http://app.id/) 这个 ID 我们需要跟一会儿我们配阿波罗的需要进行一个一致。在这里我直接写上了，我说我现在这个 App ID 我给它起个名字叫什么？我们就叫做跟这个项目名一致，叫做阿波罗杠 test 然后接下来还有一点就是你要配置一个 app.meta 然后这个它就是你自己访问的端口 portal 的端口号幺九二点幺六八点点幺幺，然后冒号 8080 就可以了。


就配置这两个东西，我们的阿波罗就已经跟我们的这个阿波罗的杠config ， config 杠 service 的地址，这是配置，配置如下，好了，就配置这么两行就可以了，其实后面你这些东西你完全都可以放到阿波罗上，他直接帮你加载。并且其实说白了，像这两个东西就是你整个没有这个 application.proxy 文件，这都行，你只需要在 class pass 下建一个目录就可以搞定，所以说它其实是非常非常简单的。


那我们现在搞定完这个事情以后，那接下来我们看看我们怎么去配置一下我们自己的这个阿波罗工程这个 App ID 我们先 control C 先粘贴一下，先复制一下，因为我后面要去怎么去用来我们一起来做，我们看到这个控制台了，那我们应该怎么去做呢？我们刚才新建了一个项目叫做阿波罗杠 test 对吧，所以说也是一样的。


我们在这里看这有一个新建项目，我点一下，新建这个部门，我们就随便选一个部门就可以了。比如说样例部门 1 英文 ID 就是你自己的 [app.id](http://app.id/) 那它的名字就叫做阿波罗杠 test 然后英文名称我也叫阿波罗 test 可不可以呢？可以没问题责任人。目前我们没有用户管理，我们就一个用户就是阿波罗就可以了。然后点提交搞定创建成功。
创建成功以后，小伙伴们可以看它这里边会有一个红色的这个 title 表示说当前的 namespace 没有发布过任何的这个配置，刚建项目肯定没有配置。然后我们点这个就是左上角的这个阿波罗图标，你可以回到首页，你会发现有两个项目了，是不是后面是收藏的项目，然后是最近浏览的项目。

[image](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/218fc520-e6e5-4431-a146-64cee703413d/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SNE4PU62%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T225842Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDXeTnCio9WV9Z9QGqiBKyjs5OxrVtbM4vFuJtkBKmk5gIhAK2A7UV5rwJVzJoKaFUOiTWmJgMf2HlyE0asF4gqlyOlKogECMb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgyDfOPtm0qrKf9pK38q3AM3eQ5nuZ896%2FHHcrh%2BmN668bmhFUCOGbdQjyA97L7SNu4hacJQKHgHkYAGdyXzFxUja863wGmD%2FF713AFPoMpHqcA8ofJ6SuxM558fupSxG3hGYjm1ZyLHZe1N7MyL%2Fn9OxFWfAisx9CgetSkmqh4DOnen1WiSJdjd6ZI%2ByCmEg9vfE0hIWQjEOZh9hZt2dW0gn3JlB4NsL6tSzq7reek6IWWpuHlwNq5Rn8DWMFU6SrFyNt0vBebs5hJWSiKMkX0pPtBchgc7PXXKeW8V0tjO7N4lW35%2FMISz7qbiyPN1YG5LHq2mT86Bxf9XUQjsJC85J%2FrypS%2BTH4NNrXsj8ld63fauxCmEOXJ5o8NV3hPgJzzlKgu5b20L%2BuMtYrx%2FWCBscw%2BOBXvPL0QNfHUhlafv1338dyKj7ASQx4Yd7tp8hwDgA42NL1n2llyGsPf3Rg2Tf3t4Cr00b8YALfajYg%2BWeOV2JzI7ava%2F%2BaIwNvx4Yx4c9LWiBuTgBDhrtAkk%2FQW47X4ZoCCPvU%2B1EkFqMJGI7Alt3hJlHHzIAW3vRogFA%2FXx68cv8ks2rjgTa0OjJeEcfttojr3tJb84cyN3%2FxmNzmEWErjxrs5yrH1hAC9CNEnLpYcUzS3qrjFIpzDCt%2F%2FSBjqkAVo%2FMUye8pGrowpxx68I6ekjUKXtl9kmDxK7XJzBwE5GrkBtaFqaLVpUAu0wGr%2FBXiZSd3fOBzgX3nIMc3o5ftCI4nINTkFL12KV6NHtlN9lNDg3OUz8Cv%2BGwhJKWKZeTcQfzNAoe9FghWHA6pY926KbsJ10Ny%2B2sXJVIXCQz7gk60ZGFFakXO8MrWJeHecuIlwJsNmJiz99JZXa1M2lN%2FtM6WE5&X-Amz-Signature=ba3587abd1b7efa74c07ba8932b4fc327713f7b4f82536c1d8d888255e0ed18c&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)


这里面这个阿波罗泰斯就是我们刚才跟大家看到的这个一个新的项目对吧，我们点开你会发现这个项目里面发布的状态，这些 key value 配置项我们现在啥都没有，那我们是不是可以去写一些配置这些是完全可以的。好了，那我们现在用最简单的 Java 的原生的方式去加几个属性，怎么去加属性呢？比如说在这里我说新增配置，我一点一下，这里边新增配置有一个界面，就是 key value 然后以及描述。然后什么环境我现在就是在 DEV 环境就好了，这个 key 我给它一个 time out 这个字段可以吧，然后 value 多少？比如 time out 调试时间是 20 毫秒。

[image](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/9cb34ba4-38d4-468a-b11a-493093f00b76/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SNE4PU62%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T225842Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDXeTnCio9WV9Z9QGqiBKyjs5OxrVtbM4vFuJtkBKmk5gIhAK2A7UV5rwJVzJoKaFUOiTWmJgMf2HlyE0asF4gqlyOlKogECMb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgyDfOPtm0qrKf9pK38q3AM3eQ5nuZ896%2FHHcrh%2BmN668bmhFUCOGbdQjyA97L7SNu4hacJQKHgHkYAGdyXzFxUja863wGmD%2FF713AFPoMpHqcA8ofJ6SuxM558fupSxG3hGYjm1ZyLHZe1N7MyL%2Fn9OxFWfAisx9CgetSkmqh4DOnen1WiSJdjd6ZI%2ByCmEg9vfE0hIWQjEOZh9hZt2dW0gn3JlB4NsL6tSzq7reek6IWWpuHlwNq5Rn8DWMFU6SrFyNt0vBebs5hJWSiKMkX0pPtBchgc7PXXKeW8V0tjO7N4lW35%2FMISz7qbiyPN1YG5LHq2mT86Bxf9XUQjsJC85J%2FrypS%2BTH4NNrXsj8ld63fauxCmEOXJ5o8NV3hPgJzzlKgu5b20L%2BuMtYrx%2FWCBscw%2BOBXvPL0QNfHUhlafv1338dyKj7ASQx4Yd7tp8hwDgA42NL1n2llyGsPf3Rg2Tf3t4Cr00b8YALfajYg%2BWeOV2JzI7ava%2F%2BaIwNvx4Yx4c9LWiBuTgBDhrtAkk%2FQW47X4ZoCCPvU%2B1EkFqMJGI7Alt3hJlHHzIAW3vRogFA%2FXx68cv8ks2rjgTa0OjJeEcfttojr3tJb84cyN3%2FxmNzmEWErjxrs5yrH1hAC9CNEnLpYcUzS3qrjFIpzDCt%2F%2FSBjqkAVo%2FMUye8pGrowpxx68I6ekjUKXtl9kmDxK7XJzBwE5GrkBtaFqaLVpUAu0wGr%2FBXiZSd3fOBzgX3nIMc3o5ftCI4nINTkFL12KV6NHtlN9lNDg3OUz8Cv%2BGwhJKWKZeTcQfzNAoe9FghWHA6pY926KbsJ10Ny%2B2sXJVIXCQz7gk60ZGFFakXO8MrWJeHecuIlwJsNmJiz99JZXa1M2lN%2FtM6WE5&X-Amz-Signature=c905aea7991de32b313e617494de052ab22f338555062209468b047a9287dad1&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

OK 然后我去点提交看见了吗？点提交了之后，同学们请看已经新加一个配置成功，如需生效请发布看见了吗？这里边在右上角里面有一个绿色的这个小框。那什么意思？你看这里边当前这个配置项有一个修改，阿波罗，它其实什么的，你添加完配置项了之后，我们的项目其实感知不到。首先第一点我们项目没有连第二点就是说我这些配置必须要点发布才能够计时的生效，这是第二点。好了，那现在接下来我们再加一个属性，比如说我再新增一个配置，比如说我们现在新增一个叫做 new key ，就是一个新的 key 这个新的 key 叫做 hello 就可以了。然后点提交。好，同学们请看。我现在有两个新的配置项，一个是 time out 一个是 new key 它们都是状态，都属于没有发布的状态的。当然我也可以做修改对不对？我可以点这个叉修改，然后我还可以点这个删除去把它这个删掉我可以点删除对吧，然后我可以取消都可以。


好了，现在我们的这配置中心里边有两个配置，当然这是以表格的形式，你也可以以什么文本的形式，文本形式就是说你只要点这是复制文本，这是 editor 你可以直接修改吗？你可以加新的 key 都可以，这是非常非常的好用的。然后你可以看一下修改历史，这都是新增的操作。然后实例列表现在目前我没有实例。好，我们回到表格当前，我已经建好了这个项目了，App ID 叫做阿波罗杠 test 然后现在有两个新的 key 但这两个新的 key 没有发布没关系。那我们现在要做的事情很简单，把我们刚才写的这个应用程序我把它启动起来。当然在启动之前，我们来说一说它怎么去做热更新。我们用最简单的方式，比如说我们叫一个 Java 就是用阿莫罗原生的 Java config 的方式。 config bin 就这种，比如说它是一个配置的一个 bin 它里边肯定会提供 get set 方法。当然在这里有一个 configuration 这个 configuration 是我们的 spring from mock 的对吧，就让它去加载它。


然后我们刚才有了两个，第一个叫做 time out 这个属性，然后我们可以给它一个 at value 比如说 at value 初始值我自己可以随便用 Dora 大括号去表示。当然要双引号引起来。比如说这个 time out 它的初始值是多少呢？比如说是20。然后第二个我们再来一个死圈类型的那个是我们的 new key 这个叫做 new key 这个 new key 它的值比如说我们可以给它单引号表示字符串叫做 hello 现在你看我都保持一致是吧。然后我可以去给他提供对应的这个 get set 方法。我们现在没有用 long book 就是那个 date 注解没有，我就不去引那个包了。我用最简单的方式就是给它声明了两个属性。然后我们这两个属性我应该怎么去玩它，既然它是一个 configuration 了，那我就可以注入了呗。比如说在这里边我们再新建一个 web 应用，我们来叫做搞一个 controller 叫做 index 的controller。


Index controller. 这个 index controller 它是一个 rest controller 然后我们直接首先 all to where 进来我们 private 我们刚才 Java config bin 我们就叫做 Java config bin ，有了它之后，那这里边的属性是不是我们都可以用没问题的。然后接下来我写一个 request mapping request mapping 就叫做index 。 okay 然后我写 public string 类型的，然后返回支持 string 我就随便打印一句话叫做 index 可以了。


好，现在我想访问属性，那怎么访问，直接调它的这个方法去 get 它的属性就可以了。比如说在这里老师就是很简单的去做一个输出，比如说 new key 就加上它点儿 get new key 然后再复制一份儿还有一个叫做什么 time out 那就它点儿 get time out 就好啦。


好了，那我们现在基本上这个 hello world 的程序就已经写完了，我们现在直接运行直接右键 run ADS spring boot application 我们来关注一下它这个已经启动了，是不是我们网上去找你看到它的 starting application 然后 start 之后它的 App ID is set to upload test by App ID properties from the system party 然后现在用的 environment 是 DEV 的环境。


其实你看到这句话你就知道现在你的应用程序已经跟阿波罗有连接了。那你看幺九二点幺六八点幺幺八零八零，这就是我们的这个阿波罗的一个 config server 的地址。现在已经连上了然后我现在通过浏览器去访问一下 HT TP 冒号杠杠 local house 8001 是不是 index 回车 index 已经访问了这个界面，我们看一下这个控制台输出的 20 hello 那现在我想要更新怎么办？我们的配置项我来刷一下。


f5 刷新一下。现在我想去改一下这两个属性，这两个属性我怎么去改？比如现在 20 我改成40，点提交。这个 new key 原先是 hello 我现在变成 hello 2019，然后点提交。好，现在我只是修改了内容，但是我要想生效，必须得点一下发布才行。对不对？我现在，没点发布。我现在再看一下控制台，我把这个先 clear 清空，然后再次去刷一下回车。 OK 我们还看到是 20 跟 hello 那接下来我们点一下发布试一下。


点一下发布，点开发布是否需要进行发布呢？你就点一下 release 点一下发布就好了。点发布看见了吗？已经发布成功。发布成功之后它这里边就是变成灰色的，表示已发布看见了吗？已发布了以后，我们再看一下控制台。同学们请看这个控制台里面打印出了日志。看见吗？他说阿波罗 config 1，然后叫做 all to update config change listener 看见了吗？你看的是正确似的。说 all to update 阿波罗 change 的 value successfully 已经成功了，修改了配置了，然后一个是 new value 等于40，还有一个是 hello 等于 2019 对吧，这就证明什么呢？我们现在的应用服务已经第一时间的感知到了这个配置的更新。


那我们再次访问一下 index 同学们，刷新，再次访问一下 index 你看现在就变成 40 hello 2019 了。看见了吧。这就是一个阿波罗最简单的一个功能，就是能实现这个热更新。然后我再去修改，比如说点修改，我说这个 hello 2019 改成 word 变成 word 然后这个 40 改成80。然后我去点一下提交，他说修改有修改。现在还是那一句话，你再刷新f5，它的结果一样的不变还是40，因为你没发布，你只有去点了发布以后它的结果才能更新过来。这个就是最简单的一个阿波罗的使用。小伙伴们看到了吧，我刚才点了发布，它才能变成了 80 和 wordok 那这个就是一个简单的阿波罗的一个 hello word 示例。好了，这节课我们就先讲到这，感谢小伙伴们收看。


