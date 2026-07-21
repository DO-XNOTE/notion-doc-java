---
title: 1-19 哨兵与主流框架的适配使用dubbo
---

# 1-19 哨兵与主流框架的适配使用dubbo

[image](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/0795cff1-7a1e-4a0d-b13d-1d1d8e67cc41/SCR-20240722-snau.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WQELZTWF%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T225838Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCC%2FH%2B2YusxQSqx8ZsYf9M%2FrdZ98BJDw5UvKjc2KZYimAIhAKoUgi4Mie%2FzlT9BBOtG8nf3IJ1xbPC4CdqQCNc7PdooKogECMb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgxXN6a9yr4l8myWDi4q3AN5CjT6yOyW6upLV3eITt%2FfZhSq8zj7JWz6wY3LLNyVOCoEthsEcVrcXQF7BD2wiDc72RFB%2FM9radF%2BgTAfNjkwQCrPZMGOhMHgk56h2waPXXflUPU8B3Xf99akpe0mGN8nPCnQ%2Fb8GKZOcX%2BEhHZJyK3vM83CNvHIk%2FVS5zvmi7Sef5Rjio98ivI1tFs5p6%2F8buru%2BGIy9yxpsZJHgsyFgmOjgwUi%2BflnG64kDnCPwhGHPhk2nfX0onicxTE3L%2BPheYscIRQErffMIbMYp3%2FmJZVgic2ktCoM%2BC1IAaSj3QwZGPCtrxkH68UwbqZnvBrcUPE92tbnBYEGHYr57Vthc32wNsQAilzU6PDGbQAEsIxZguBXFsMLTlmArugIUT%2BH%2FFz7DFX%2FYVVBdufYnTm9aa3B%2FAUizpSdDn3%2FSMKnvDyk4Eo2%2BIRvc3z2uVyIbbwIRV5Ge5wjJQtvFUF0PNstXutVau%2FNKsaZuDxYbD6nsmtOcIQqzNl%2FbllsLEATJOzc%2BzevMbuPKkL%2Bs8YVpWqmTNvHJsMIrQ9MG3zlxsEDAsGsEfphMwHz9Gw9GcrhZvd6iFg8UAd9dPYUz4Ir6fThD%2BrF%2Fpj1MelGrK1SnDhJlN9ghQI7q5VlOSK4nATDHuP%2FSBjqkAeWwnAS7PUzTzp0ERKAvR9Z4fD%2F8p9dCWpt4K22gCgF2sEofMVP0GTCC28RYc2o6JooEGQFuk7plNfIpq2KZ1q53bhk8I0ImwcEfHko634QefCf474U6yh0nlAFq1irnt5mAa8ce6iKAa%2BrpAPhb2ii3dEHnzg9A2HdNUPAfsixD%2B5ICwJtzsv90K72weCb2N3zRtDpjoI7WwN9f4xxij81whtPj&X-Amz-Signature=7c419331f10c56cb891b163ba4d2294966f7272d7d033a7e7ff77db5e6baf740&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

[image](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/9c984a47-d2a3-4df1-a78b-0c158d664331/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WQELZTWF%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T225838Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCC%2FH%2B2YusxQSqx8ZsYf9M%2FrdZ98BJDw5UvKjc2KZYimAIhAKoUgi4Mie%2FzlT9BBOtG8nf3IJ1xbPC4CdqQCNc7PdooKogECMb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgxXN6a9yr4l8myWDi4q3AN5CjT6yOyW6upLV3eITt%2FfZhSq8zj7JWz6wY3LLNyVOCoEthsEcVrcXQF7BD2wiDc72RFB%2FM9radF%2BgTAfNjkwQCrPZMGOhMHgk56h2waPXXflUPU8B3Xf99akpe0mGN8nPCnQ%2Fb8GKZOcX%2BEhHZJyK3vM83CNvHIk%2FVS5zvmi7Sef5Rjio98ivI1tFs5p6%2F8buru%2BGIy9yxpsZJHgsyFgmOjgwUi%2BflnG64kDnCPwhGHPhk2nfX0onicxTE3L%2BPheYscIRQErffMIbMYp3%2FmJZVgic2ktCoM%2BC1IAaSj3QwZGPCtrxkH68UwbqZnvBrcUPE92tbnBYEGHYr57Vthc32wNsQAilzU6PDGbQAEsIxZguBXFsMLTlmArugIUT%2BH%2FFz7DFX%2FYVVBdufYnTm9aa3B%2FAUizpSdDn3%2FSMKnvDyk4Eo2%2BIRvc3z2uVyIbbwIRV5Ge5wjJQtvFUF0PNstXutVau%2FNKsaZuDxYbD6nsmtOcIQqzNl%2FbllsLEATJOzc%2BzevMbuPKkL%2Bs8YVpWqmTNvHJsMIrQ9MG3zlxsEDAsGsEfphMwHz9Gw9GcrhZvd6iFg8UAd9dPYUz4Ir6fThD%2BrF%2Fpj1MelGrK1SnDhJlN9ghQI7q5VlOSK4nATDHuP%2FSBjqkAeWwnAS7PUzTzp0ERKAvR9Z4fD%2F8p9dCWpt4K22gCgF2sEofMVP0GTCC28RYc2o6JooEGQFuk7plNfIpq2KZ1q53bhk8I0ImwcEfHko634QefCf474U6yh0nlAFq1irnt5mAa8ce6iKAa%2BrpAPhb2ii3dEHnzg9A2HdNUPAfsixD%2B5ICwJtzsv90K72weCb2N3zRtDpjoI7WwN9f4xxij81whtPj&X-Amz-Signature=0dad648e59eb9cdae0f293b4a6fe5eb52d507ea325c92bb81220db7bc37c34de&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

节课我们继续往下去讲我们的这个sentence 。那这一节课我们主要讲的是 sentence 跟我们主流框架的一个适配。那 sentence 它的这个生态圈非常的强大，看到它可以去跟我们的这个 web swolate 包括 double 包括 spring boot spring cloud 以及 web flex 以及 jrpc reactive 适配，以及也可以跟我们的这个 API get away 像我们 spring cloud 的这个 get away 以及这个注意 Netflix 的注意包括绕开 MQ 等等这些开源的比较优秀的框架做一个适配。那老师在这里主要就是讲两个比较主要的，一个是跟 double 进行一个整合，还有一个是跟绕开 Q 做一个适配。然后对应着其他的比如说小伙伴们对 web flex 或者是 grpc 以及 get way 就是比如说 spring cloud 这一套。还有兴趣的话你可以看一看它的一些适配的一些这个核心思路和这个圆满。然后去分析去使用官方给出的 demo 其实是非常的全面的。那接下来我们直接进入跟 double 怎么去适配，我们点进去。那我们的这个sentinel ，它提供了 double 相关的这个适配的一个 adapter 主要针对于我们的 service provider 以及 service consumer 的一个 filter 的这么一个实现。那我们知道 double 其实它非常关键的几个概念。

[image](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/e5c4f041-cd7d-49fe-8c25-160f83f00037/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WQELZTWF%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T225838Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCC%2FH%2B2YusxQSqx8ZsYf9M%2FrdZ98BJDw5UvKjc2KZYimAIhAKoUgi4Mie%2FzlT9BBOtG8nf3IJ1xbPC4CdqQCNc7PdooKogECMb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgxXN6a9yr4l8myWDi4q3AN5CjT6yOyW6upLV3eITt%2FfZhSq8zj7JWz6wY3LLNyVOCoEthsEcVrcXQF7BD2wiDc72RFB%2FM9radF%2BgTAfNjkwQCrPZMGOhMHgk56h2waPXXflUPU8B3Xf99akpe0mGN8nPCnQ%2Fb8GKZOcX%2BEhHZJyK3vM83CNvHIk%2FVS5zvmi7Sef5Rjio98ivI1tFs5p6%2F8buru%2BGIy9yxpsZJHgsyFgmOjgwUi%2BflnG64kDnCPwhGHPhk2nfX0onicxTE3L%2BPheYscIRQErffMIbMYp3%2FmJZVgic2ktCoM%2BC1IAaSj3QwZGPCtrxkH68UwbqZnvBrcUPE92tbnBYEGHYr57Vthc32wNsQAilzU6PDGbQAEsIxZguBXFsMLTlmArugIUT%2BH%2FFz7DFX%2FYVVBdufYnTm9aa3B%2FAUizpSdDn3%2FSMKnvDyk4Eo2%2BIRvc3z2uVyIbbwIRV5Ge5wjJQtvFUF0PNstXutVau%2FNKsaZuDxYbD6nsmtOcIQqzNl%2FbllsLEATJOzc%2BzevMbuPKkL%2Bs8YVpWqmTNvHJsMIrQ9MG3zlxsEDAsGsEfphMwHz9Gw9GcrhZvd6iFg8UAd9dPYUz4Ir6fThD%2BrF%2Fpj1MelGrK1SnDhJlN9ghQI7q5VlOSK4nATDHuP%2FSBjqkAeWwnAS7PUzTzp0ERKAvR9Z4fD%2F8p9dCWpt4K22gCgF2sEofMVP0GTCC28RYc2o6JooEGQFuk7plNfIpq2KZ1q53bhk8I0ImwcEfHko634QefCf474U6yh0nlAFq1irnt5mAa8ce6iKAa%2BrpAPhb2ii3dEHnzg9A2HdNUPAfsixD%2B5ICwJtzsv90K72weCb2N3zRtDpjoI7WwN9f4xxij81whtPj&X-Amz-Signature=750fb8dc3dd601c66d9168d267b3d8bb0230a723b1165f27c3bf664254bd701d&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

第一个就是 SPI 扩展点对吧一些什么？艾特 SPI 艾特 active 激活艾特 doctor 对不对？适配的工作除了跨年以外，剩下的就是它的最关键的核心。比如说它的 filter double 里面好多好多 filter 我们可以去针对于 filter 的扩展点做一系列的事情。当然我们的那个 santa 哨兵也是基于 filter 扩展点去实现的。然后在这里小伙伴们要注意，我们现在目前阿帕奇的阿里巴巴的double ，现在目前是在二点七点 X 版本以上的时候，你要使用这个就是 sentinel 阿帕奇 double adapter 然后你用的如果是二点六点 X 文本，那你就用这个森特斯杠 double 杠 adapter 它们两个之间有了一个阿帕奇的这么一个区别。所以说你在使用 sentence 的时候，你要考虑到目前你们公司所用的大波框架到底是 2.7 还是2.6。那目前老师的公司的框架是 2.6 的X 。

```java
Dubbo
Sentinel 提供 Dubbo 的相关适配 Sentinel Dubbo Adapter，主要包括针对 Service Provider 和 Service Consumer 实现的 Filter。相关模块：

sentinel-apache-dubbo3-adapter（兼容 Apache Dubbo 3.0.5 及以上版本，自 Sentinel 1.8.5 开始支持）
sentinel-apache-dubbo-adapter（兼容 Apache Dubbo 2.7.x 及以上版本，自 Sentinel 1.5.1 开始支持）
sentinel-dubbo-adapter（兼容 Dubbo 2.6.x 版本）
对于 Apache Dubbo 3.0.5 及以上版本，使用时需引入以下模块（以 Maven 为例）：

<dependency>
    <groupId>com.alibaba.csp</groupId>
    <artifactId>sentinel-apache-dubbo3-adapter</artifactId>
    <version>x.y.z</version>
</dependency>
对于 Apache Dubbo 2.7.x 及以上版本，使用时需引入以下模块（以 Maven 为例）：

<dependency>
    <groupId>com.alibaba.csp</groupId>
    <artifactId>sentinel-apache-dubbo-adapter</artifactId>
    <version>x.y.z</version>
</dependency>
对于 Dubbo 2.6.x 及以下版本，使用时需引入以下模块（以 Maven 为例）：

<dependency>
    <groupId>com.alibaba.csp</groupId>
    <artifactId>sentinel-dubbo-adapter</artifactId>
    <version>x.y.z</version>
</dependency>
```


2.7 可能第一是比较新，我们在进行这个还没有去做整体的升级，那我们要做整体的升级，可能就是对于我们的成本来讲非常大，所以说也看了参考了一下 2.7 的一个新的性确实比较不错，我们后面可能会有一些升级的事情。那我在这里就跟大家主要去讲一下这个 2.6 的 X 那你看到 2.7 版本，它主要有这个包，2.6这个包 OK 它们中间差一个阿帕奇的一个一字之差。


引入了之后，那你的 double 的所有的这个服务的接口跟方法就是服务的调用端跟这个提供服务的那个 provider 那端就会成为我们 sentence 中的资源，然后在配置规则之后，就可以去自动的去享受到 sentence 的一个防护能力。


那这个其实它是**针对于一个通用的资源去做，说白了就是把这个 provider 跟这个filter ，利用这个 provider 跟这个 consumer 利用了这个 filter 的机制去做一个全面的这么一个接入。但是其实这种方式并不满足我们的需求，因为我们所有的方法不一定全都需要做流控，我们只是一些核心的方法，并发高频的访问的方法去做一些流控。本身来讲一些低频的访问的一些请求根本就没有必要流控。所以说那我个人觉得其实再去使用这个 double 去整合三层的时候，那我个人觉得还是你自己写原生的代码或者是应用这个注解，我觉得更好一些。**然后在这里面，如果不希望开启 sentinel adapter 中的某个 filter 可以去手工去关闭它，这个很简单对吧，其实它里边带了就是这个我们可以去配置。


那 double 它可以流控的力度可以是两种力度。第一种是以服务接口的维度去做整个服务内部。比如这个服务下面有好多个接口，十多个接口，我可以以服务的维度去做流控，还可以这个服务中方法的违规思路。当然这个不是硬性的规定，这只是一个资源的名称，他说接口的权限命名，就是什么 com 点阿里巴巴点这什么点 double.service 针对于这个 for service 下面所有的方法做一个流控。还有一个就是针对于某一个方法签名做流控，比如说 for service 下面有一个冒号 hello 然后它的这个参数比如说一个参数加五点零点四追，可以针对于这个方法做优困。


当然我们的 sentence 它还支持这个全局的 fail back 全局的 fail back 什么意思呢？这个其实我觉得一般来讲用不到，就是说你 double 里边所有的服务如果出现错误的时候，它可以统一的去走到一个 fail byte 函数中。但我觉得这个不太契合于我们自己实际的这个工作的业务。


那可能我们工作业务有一些 double 接口，比如说支付如果失败了，有支付降级的一些手段。比如说我可以再去调第三方，另外的一些其他的一方去做支付或者是怎么样。那比如说我的订单失败了，我们可以延迟做本地的做一个记录，然后异步的去投递到 MQ 然后再做重试等等一些策略。也就是说针对于某一种服务，你如果提供一个全局的这个处理的话觉得不太合适。但是他还给你提供了全局的失败的一个 feel back 的统一的支持。


当然这个一般来讲我不太去用，那用户你只需要实现 double fail back 这个接口，然后去重写就可以了。重写这个接口里面的方法。当然重写之前你要把这个东西通过加 double feel back 去注册可以的时候，那情况下会直接将这个 block exception 然后包装后进行一个 slow 抛出。基本上这就是关于我们 double 的一个说明。
当然它下面有一些具体的例子，比如说我们可以看这个 demo 然后我们如果小伙伴们有兴趣的话，你可以看大 double 它最佳实践。这个连接就是老师现在打开的这个连接，它写得非常详细，小伙伴们感兴趣，可以去把这个从 0 开始读一读。读了之后，然后你对应着去配一下看一下。你基本上就对这个 double 跟三碳做整合，就有一个非常清楚明白的一个认知和了解了，然后就会应用了。那我们在这里就是直接领大家去做一个官方 demo 的一个演示就可以了。打开我们自己的源码包，我们来看一下。


那当前老师在这里边，我这个 sentinel 我的这个 dashboard 还起着，dashboard这个服务还没有停，但是我现在我们找到 double 的 demo 看一看这里边 sentinel 杠这个 demo double 好了，我们 163 这个版本，我们看一看它需要引入哪些依赖我们最大化我们的这个配置看到了最核心的就是我们的这个三层楼杠 double 杠 adapter 还有就是传输的这种 transport simple HTTP 然后基本上就没有其他的了。怎么去使用呢？很简单。


首先你要去用的话，我们随便找一个例子，比如说这个 demo 1，当然这个是一个普通的 double configuration consumer 的，基本上这些都是原生的 double 自己，你看这些都是 double 参观的，比如说注册一个 application config 然后搞一个注册中心 registry 这里边我它这里面就用了一个这个 multi cast 方式进行一个注册，当成注册中心了。然后下面还有比如说 consumer 的配置，还有这个 consumer 对应的这个service ，然后这里边对应 service 什么，它是采用这个 URL 直连的方式去这个调用的。

[image](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/48892b95-48d3-4599-848b-88e5eac7ec5f/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WQELZTWF%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T225838Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCC%2FH%2B2YusxQSqx8ZsYf9M%2FrdZ98BJDw5UvKjc2KZYimAIhAKoUgi4Mie%2FzlT9BBOtG8nf3IJ1xbPC4CdqQCNc7PdooKogECMb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgxXN6a9yr4l8myWDi4q3AN5CjT6yOyW6upLV3eITt%2FfZhSq8zj7JWz6wY3LLNyVOCoEthsEcVrcXQF7BD2wiDc72RFB%2FM9radF%2BgTAfNjkwQCrPZMGOhMHgk56h2waPXXflUPU8B3Xf99akpe0mGN8nPCnQ%2Fb8GKZOcX%2BEhHZJyK3vM83CNvHIk%2FVS5zvmi7Sef5Rjio98ivI1tFs5p6%2F8buru%2BGIy9yxpsZJHgsyFgmOjgwUi%2BflnG64kDnCPwhGHPhk2nfX0onicxTE3L%2BPheYscIRQErffMIbMYp3%2FmJZVgic2ktCoM%2BC1IAaSj3QwZGPCtrxkH68UwbqZnvBrcUPE92tbnBYEGHYr57Vthc32wNsQAilzU6PDGbQAEsIxZguBXFsMLTlmArugIUT%2BH%2FFz7DFX%2FYVVBdufYnTm9aa3B%2FAUizpSdDn3%2FSMKnvDyk4Eo2%2BIRvc3z2uVyIbbwIRV5Ge5wjJQtvFUF0PNstXutVau%2FNKsaZuDxYbD6nsmtOcIQqzNl%2FbllsLEATJOzc%2BzevMbuPKkL%2Bs8YVpWqmTNvHJsMIrQ9MG3zlxsEDAsGsEfphMwHz9Gw9GcrhZvd6iFg8UAd9dPYUz4Ir6fThD%2BrF%2Fpj1MelGrK1SnDhJlN9ghQI7q5VlOSK4nATDHuP%2FSBjqkAeWwnAS7PUzTzp0ERKAvR9Z4fD%2F8p9dCWpt4K22gCgF2sEofMVP0GTCC28RYc2o6JooEGQFuk7plNfIpq2KZ1q53bhk8I0ImwcEfHko634QefCf474U6yh0nlAFq1irnt5mAa8ce6iKAa%2BrpAPhb2ii3dEHnzg9A2HdNUPAfsixD%2B5ICwJtzsv90K72weCb2N3zRtDpjoI7WwN9f4xxij81whtPj&X-Amz-Signature=84ddbd36473812267b07e0370d1aacce42010f93f14ea9972a38c3bd1b9c644a&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

然后我们再看这里边有两个 boost shop 类。首先我们一般是先要启动服务的提供者，也就是 provider boost 那 provider boost up 它做了什么事情呢？同学看一下它。第一步先要 init 这个它其实是什么呢？他说 user dont need to menu call this master 就是说用户其实你不需要手工的去调这个方法，其实你使用 double 的时候，你只需要做这个 init rolls 就可以了，你不需要调这个方法，因为跟 double 集成了之后，他自己会帮你去调这个对应用的方法。好吧，你不行，但是他这个 demo 就是完全纯粹的一个，他没有 sprint 工程对吧，他就是一个 double 的这个 Java 的 class 所以说他自己就掉了一下，初始化了一下。


那我们去加载规则，你看加载的什么规则，这个规则就在下面对吧，叫做 follow 流控规则。流控规则 resource 什么是不是？然后这个流控是10，就是说我的 QPS 最大是10。然后把这个规则加载到内存中。很简单，就是 collections.single connect list 然后菠萝菠萝可以了。然后这个 resp 是什么呢？我们点到这里看到了，就是我们 com 点全线匿名，加上冒号、方法名以及参数，她以这个当成他的这个资源名称。当然也可以用实例，他可以用一个包名加类名权限命名，这是服务的权限命名，这是服务的全命名，加上方法签名，就是两种力度都看到了。那这个目前来讲它还没有用，就是说你想去用的话好，你就把这个代码把这个替换一下，你们这个就可以了。


这意思这是对应的这个 provider 在启动 provider 的时候，你要加上这几个配置，这几个配置老师都提前配好了，然后我们的控制台也启动好了对吧。那现在你去启动的时候，你会把这三个配置 copy 过来，右键 run ADS 启动之前先看一下配置参数。


我们现在看的是 provider 老师加了几个配置，看阿克木斯里面老师加的配置是有了那三个，然后还有控制台的地址我也配了一下看见了吧。因为我们要把就是对应的流控的一些资源一些这个日志什么的去收集到控制台，让控制台感知到。好了，那我现在把它 run 起来，就是说这些配置都要配对应的控制台，配置也要配。你看到这个 service provider is already 就相当于他已经准备好了。然后准备好了以后，我们其实可以通过控台看一下。 HTTP 账号杠杠 local house 8080 后台是8080。
好了，我们看到这个 provider 已经有了，provider有了之后，它的这个触点链路什么也没有，因为什么它的规则是有，因为它是初始化的时候加进来的，这个规则就已经有了，就不需要你去做什么其他的事情，它帮你直接集成。好了，QPS是 10 单击快速失败的策略，看到了。


好了，然后我们直接把这个 consumer 骑起来。目前我们 consumer 实力是0，这证明什么证明这个之前注册过，之前老师启动过，但是现在还没起来，所以说是0。那我们来起一下。 consumer 起来也是一样的，很深入的。代码是怎么去做的呢？我们先看一下。首先第一点是也要加这三个配置，启动的时候，然后以及加上你自己的这个控制台的地址。然后他是调这个方法盖在 B 然后后循环了 15 次调 say 喽方法，15次调 say 哈喽方法。然后呢它流控是10，理论上来讲应该 10 次通过 5 次被拒绝。那我们直接运行一下还是右键。


在运行之前，我们先看一下配置，这个配置在这里已经有了，是不是他给我提的这三个以及对应的控制台的这个带时报的 IP 端口号有了之后转起来。启动起来之后，你会看到他最终抛了一堆异常，知道吧，他 success 基本上成功了 10 次，剩下的就被 block 了，就被流控了。因为看到他会流控的这个 follow exception 已经有了，然后 push by 都会有后面五次都被流控了。然后我们通过什么呢？我们通过 dashboard 就可以看到，在这里我还是要刷一下，刷一下之后你就会看到了。这个实时的流控看一下他这个没有那么特别实时。但是我们看到这个额外的是有规则的，这是一个流通规则，降级是没有的，这个实时的链路都看不到的。原因很简单，我把这个东西，consumer我把它停掉。停掉 consumer 以后我再起来一次，我再起来一次这个 server 看能不能看到对应的效果图。它还是应该访问了 10 次之后，后面的全都降级了，全都被流控了。


好，我们来说一下。 OK 同学们一起看这回，因为你的 consumer 是没有任何规则的，所以说你看不到，但是 provider 是有流控的。我们看到里边绿色的就表示通过了 10 次拒绝了 5 次看见了吗？也就是说其实我们使用 double 跟我们的这个就是我们三层的跟这个 double 整合的起来还是非常非常简单的。就是说很多东西他都帮你去封装好了，你自己不需要写太复杂的东西，包括规则什么的，他都帮你定义好，你看就是权限命名，这个是服务。然后这是服务下面的具体的一个方法。然后它是针对于这个方法加了一个流通策略了，针对这个方法加了一个流程策略。所以说只要是阿里系的东西，它都是集成的，非常方便。


好了，在这里老师就不做过多演示了，小伙伴们可以自己课下去运行一下这个例子，然后去体会一下它的源码其实也非常的简单，在这里我先把这个整个整体的先都停掉，包括 dashboard 我也先停掉。源码主要就是你只需要看到他跟这个 double 整合的一个 adapter 就可以了。


整合的 adapter 就是它是吧，它里边最核心的点就是在于这两个，一个叫做 sentence sentinel double consumer 一个叫 sentinel double 额外的。那你会看到在这个里边最大化，它基本上就是 active 做一个激活一个 group 的方式激活，然后去在 inwork 方法里边做什么事情就是开始对于 interface 级别，你看它有一个就是负 context entry 然后子 context 最接口级别的，还有这个方法级别的都是做了流控了，都是做了这个相当于最开始的埋点就是原生的 API 然后再去做 inwork 调完了之后， catch 的时候， block 的时候看它会统一的去访问 double go back registry 里边它会获取具体的 fail back 方法的 handler 然后再去做回调 inwork 然后会把 invocation 传进去。也就是说你注册的时候你必须得你自己如果有那种全局失败策略，你必须要注册到这个类上是这意思，所以你可通过代码就一目了然了。
在 finally 的时候做释放做突出，这是对应的这个 provider 他怎么去做的？ consumer 也是一样的， consumer 也是一样，就是一个 filter 的机制。然后在 inwork 方法里边还是去做原生的这个 sph 5 比 5 好，我们非常熟悉了，对它做一个统计分析，这是入口，然后把我们对应的资源流控的地方给它包裹起来，然后最终异常的时候去调异常的方法，然后 final 类的数据结束。


那我相信这个小伙伴们应该是没什么太大问题，包括这个全局的 feel back 怎么去做的，是不是全局的 fail back registry 就在这里，它里边默认都有一个 default double 的一个 fail backdefault double fail back 就是默认执行的降级的策略是吧，就是它。然后你只需要比如说继承它，然后去重新再写一个就可以了。你如果不想用 default 了对吧，我不想用 default 那我就自己实现这个 double file 接口，把这个 handler 重新重复载重写一下就可以了，就是实现这个接口就搞定了。


好了，那这就是关于我们的 sentence 怎么去适配 double 其实很多开源框架都有了一些优秀的扩展点，然后你再去实现就简单了。然后接下来我们再去跟大家一起来学习另外的一个组件。看看怎么继承的。那在这里我们挑选是绕开MQ 。那绕开 MQ 我们都知道它是一个开源的消息中间件，也是阿帕奇的一个主题项目，其实说白了也是阿里系的。


好。那在绕开 MQ 中，我们来看，消费者去消费消息的时候，无论是破的方式就是拉的方式还是 push 的方式，破的方式是推，但是 RocketMQ 里面用的是 long pool 查询的机制去做的。然后都可能会出现这种大批量消息消费的时候一个突刺的这么一个概念，就是可能某一瞬间我有一堆的请求过来，导致我们销售端可能会挂掉。就是说你的在处理消息的时候很可能会导致这个系统资产不高，影响我们系统的稳定性。那可能几秒之后就没这个问题了就是消息的尖刺。


说白了，那我们怎么去解决呢？那我希望解决的方式就是把多余的消息给做一个平均的分摊。说白了就是把高的地方消下去，然后低的地方填上，这个就是所谓的什么萧风千古。说白了之后，你看就是在这里边，比如这个时间点它的这个流量特别高，然后这个时间点流量也特别高，我们能不能把它都均匀的填充起来，就让它平均就是绿色这条线就是削峰填谷的这个事情，超过处理能力的消息，我把它就延迟一下，让它过一会再去执行，就是一个相互评估。


那怎么去做呢？标 kmq 其实可以做到标 kmq 里边，它可以配置这种匀速模式，比如说每秒钟 QPS 就只处理 5 个，然后你每 200 毫秒就会处理一条消息，多余的将会做一个排队处理，超时会被做一个这个拒绝。然后这里边也有对应的 demo 这个 demo 其实我们可以对应着看官网这个 demo 就看我们这个源码里面 demo 这个更清晰一些。我们看到 demo rock MQ 当然这个 demo rock MQ 它里边确实是没有针对于 rock MQ 的 adapter 因为 rock MQ 这个东西其实在最新版本的四点五点二以后，内部本身就做了一些比较好的流控的这个策略。就即使是你不用 sentence 它也可以帮你设置一些流控的这个属性什么的，包括一些水位线，对应的阀值，在 consumer 消费的时候里边都有相对应的这个配置。


但是如果你想用 santa 去做也可以，但是他没有去写适配器，因为它内部已经有了，你要非得想用他给你一个 demo 看见了吗？给你个demo ，就是有一个新客 producer 同步发消息，我们来看一下这代码就是创建生产者之后，然后去把生产者启动，发 1000 条消息去散的出去，然后最后把它关掉。
那消费者怎么去做它的这个消风处理是在消费者去做，他做的用的是 pool consumer demo 拉取消息标 MQ 拉取消息采用的是定时拉取，然后更新本地 offset 或者是远程 offset 机制去做的。然后我们看到他是把 offset 存储到了本地，他只是写了一个 demo 当然你的 offset 可能要做一个，比如说存到 Redis 缓存中或者存到 DB 里都可以，这是一个 offset 就是拼音量。然后接下来我们看他用的是定时拉取。当然第一步先初始化我们自己的这个拉取的规则，然后他调用这个 default M 就 pull consumer 去创建 consumer 去启动。


启动了之后，然后我们的这个 consumer 去 fetch subscribe 的 message case 就是去拉取我订阅的消息的主题的里面的对应的 pin 就是 rocky MQ 有一个物理跟逻辑的概念，它的 topic 其实是一个逻辑的概念，它 topic 下面主题下面可能对应的是队列的概念，默认是 16 个，现在都改了。


其实源代码这个东西，你自己应该经常去更新或者是有版本的这个递增，你经常的去看一下它的一些新的 future 然后自己去看代码，慢慢的去看它有哪些变化，时常的去关注一下新技术。然后这就是他自己从这个 topic 里边拉取的队列有多少个，这是返回的一堆队列集合，然后对每个队列做消费，比如说我在 VR 处的时候，我怎么去做消费，具体的消费逻辑就在这他把循环了消息之后，然后去度相信就对每条消息做处理。然后其他的机制可能就是更新一下 offset 或者是一些其他的 not front 包括没有找到消息，就各种各样的这个case ，你可以理解。我们简单看一下他做商项的时候他怎么去做的，就是说他这个代码给你的，就是说异步的去提交到一个线程里，说把任务异步的去扔到这个 pool 里面。所以这个 pool 是一个 fix slide pool 是一个 32 个线程容量的一个固定的线程池。然后在提交线程池的时候，他自己的去对。


我们的 sentence 逻辑就有了，就是它有 entry 然后这个 entry 它会做流控，你看这个代码一样的，这是具体的你的 your business logic here 就是你自己的这个业务处理完了之后，如果发生流控，那就 catch block session 对吧，如果 final 类的时候我们就退出，它就是这么一个简单的代码，这是他给你提供的一种手段，然后他自己怎么去做的呢？就是 init follow rules control ，然后以内的 follow control 就是我做一个流控。我说我对资源 copy 的这个资源做一个流控手段，说每秒钟我允许并发数就是与一个匀速消费。那么其实说白了就是官方文档说的 200 毫秒处理一条消息，处理不过来的，那我们拒绝就好了。


然后这也是使用什么 QPS 的方式，然后在这里边去添加这种 set control behavior control behavior 就是 1.6 之后新特性，它做的是什么？做的是这个 limit ctrl behave 然后 read limit 百分比。说白了就是一个匀速的策略，你会看到它是这种方式。然后 one up 就是什么 one up 就是一个预热的方式。然后在这里它设置这个一些其他的参数下载规则。 OK 这个就是一个对应着绕开 MQ consumer 跟我们哨兵 sentino 集成的一个 demo 大家可以看看。当然还有一些其他的，比如说刚才我说的跟 spring cloud get way 跟 GR PC ，还有跟我们的这个我们的 so late web 应用，都有一些集成的 demo 都在这里，那 demo 里面都会有好多。所以说小伙伴们想要去学习，一定要去把这个源码下载下来，然后自取看看官方的 demo 这样的话你才能更清楚更明白配合着文档。好了，那么这节课我们就讲到这，感谢小伙伴们收看。


**Sentinel 和 **Dubbo的最佳实践

[https://cn.dubbo.apache.org/zh-cn/blog/2018/07/27/sentinel-为-dubbo-服务保驾护航/](https://cn.dubbo.apache.org/zh-cn/blog/2018/07/27/sentinel-为-dubbo-服务保驾护航/)

[image](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/f18638bf-0276-4cad-aedd-9bae620026e8/Sentinel-pom-xml-at-master--alibaba-Sentinel-Sentinel-pom-xml-at-master--alibaba-Sentinel.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WQELZTWF%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T225838Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCC%2FH%2B2YusxQSqx8ZsYf9M%2FrdZ98BJDw5UvKjc2KZYimAIhAKoUgi4Mie%2FzlT9BBOtG8nf3IJ1xbPC4CdqQCNc7PdooKogECMb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgxXN6a9yr4l8myWDi4q3AN5CjT6yOyW6upLV3eITt%2FfZhSq8zj7JWz6wY3LLNyVOCoEthsEcVrcXQF7BD2wiDc72RFB%2FM9radF%2BgTAfNjkwQCrPZMGOhMHgk56h2waPXXflUPU8B3Xf99akpe0mGN8nPCnQ%2Fb8GKZOcX%2BEhHZJyK3vM83CNvHIk%2FVS5zvmi7Sef5Rjio98ivI1tFs5p6%2F8buru%2BGIy9yxpsZJHgsyFgmOjgwUi%2BflnG64kDnCPwhGHPhk2nfX0onicxTE3L%2BPheYscIRQErffMIbMYp3%2FmJZVgic2ktCoM%2BC1IAaSj3QwZGPCtrxkH68UwbqZnvBrcUPE92tbnBYEGHYr57Vthc32wNsQAilzU6PDGbQAEsIxZguBXFsMLTlmArugIUT%2BH%2FFz7DFX%2FYVVBdufYnTm9aa3B%2FAUizpSdDn3%2FSMKnvDyk4Eo2%2BIRvc3z2uVyIbbwIRV5Ge5wjJQtvFUF0PNstXutVau%2FNKsaZuDxYbD6nsmtOcIQqzNl%2FbllsLEATJOzc%2BzevMbuPKkL%2Bs8YVpWqmTNvHJsMIrQ9MG3zlxsEDAsGsEfphMwHz9Gw9GcrhZvd6iFg8UAd9dPYUz4Ir6fThD%2BrF%2Fpj1MelGrK1SnDhJlN9ghQI7q5VlOSK4nATDHuP%2FSBjqkAeWwnAS7PUzTzp0ERKAvR9Z4fD%2F8p9dCWpt4K22gCgF2sEofMVP0GTCC28RYc2o6JooEGQFuk7plNfIpq2KZ1q53bhk8I0ImwcEfHko634QefCf474U6yh0nlAFq1irnt5mAa8ce6iKAa%2BrpAPhb2ii3dEHnzg9A2HdNUPAfsixD%2B5ICwJtzsv90K72weCb2N3zRtDpjoI7WwN9f4xxij81whtPj&X-Amz-Signature=b299c718a3ce57023680c6ceb6cb9ba04866accc47078ce1dce0fac976800151&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)






