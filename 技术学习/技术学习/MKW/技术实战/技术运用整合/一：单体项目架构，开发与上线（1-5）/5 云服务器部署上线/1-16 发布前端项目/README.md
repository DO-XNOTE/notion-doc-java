---
title: 1-16 发布前端项目
---

# 1-16 发布前端项目

[image](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/b41e1f21-6ba4-4464-a096-7a7c36d79670/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TFBXOPAG%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T224756Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCaqFtV%2BVrBR5UxPIkm5R2MKK%2BGmBK7jg1hntjx%2BwTb3QIgR%2FQno41cD9AVh643ZVdXBh9DEb3xrn88WTHcb%2BTFwLsqiAQIxv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDK6f2SZD5gCBXXYR3ircA3TvbZ57i3LfSyZ%2BXvMpsQGwiV7naX1t8Hvq0hpI7ipU1PNa6N6XPKV9IYPvYMtl1R9UjCfj4ZfQWik2o42b806SLtMh1pCC3whLW0i22H9wVzWEKKzsO1ePGZjkvK5TZCenvyqFtcPCyCud3v2ig56BkMCSNpVb44yiWerWHOZWubfvqJcFBMjrO%2FYO2YD0uxkxMi%2Bd%2BfD6BTU24oh4lHIBOYJN%2FF4SYRZLbnEnCo1UBhQIwbul2PCU0eRHuXVdIWHGP4%2FDSY7P76ehl%2B%2BLMJvBMXoPh3NCLjg6rD9speN%2FIRjRF%2F1Sf7YSOIwgB%2FiWEMUsRPVp2qderiC42RTaUQR%2FtJIK%2Flf2eZdLZsOjynBQunpX3hSPaE3zXMsVGsnE3IK%2BMA8s1mUBCsv1CPs%2BPuy6e0Bm007Wqqr%2FhBRqSh278m020tlyCr9QeXyFL1nHPgj7pjLimTZzVx4Y8S8buhKrQ0vfHLDdi6GsXZxzZEcywZV76gNKmMANnsYbDis6C6L3xij1q9RWnMQNfzuoNVVWtDRRpQxoFQ9byRKOwrQ4qyk4cqdNk9vMqb0URcr9axOvmXXE%2B9HwUXmQWKgGyDp1TeXHLB0sITA23LtmHnBzbVMW8ltZ5s8UeVjHMKi3%2F9IGOqUBi8XdFR%2B5tK3wO0goUqkWY2jbjtIUiMNbZ%2F8%2Bzl0F6%2Bl00wb2xmFQA7DyVHmZSBpYIe5Rx4%2FPrrIidX%2Fwydzum9wbVr%2BC2Du8dpEQ2o1pKvmP89y3bd5btYDUYEFKAlohIUcbqFE7MBff43SClDRA1veYVkeL3UpjVI6q9b%2FODpK%2FFaO27ax76dISx%2FAktLYuQWRUCvVHFs9ut6XZskTT%2Bz%2Byd9kC&X-Amz-Signature=d9b842c11d95b01752639133a77729f88bc8aedb3d2b449fa179a3f4d5327b80&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

那么在我们的一个后端项目发布了以后，那么还需要去发布一下前端的项目，那么由于我们是前后端分离的，我们之前也说的，所以我们是分了两个窗 k 层，我们是需要到我们本地来找一下，把我们的一个找到我们的自己的项目，也就是这两个项目。这两个项目我们可以直接把它们丢到我们的一个服务器里面，但是在上传到服务器的过程中，我们有一点是需要去注意的，就是在这里面它的一个 URL 你也是需要去做一定的配置的。OK，我们先来改一下这个shop，我们右键 open with VS code 打开一下，打开了以后，那么在这里面我们是找到 APP 点JS，那么这一块内容我们是需要去做更改的，那么这个也就是我们在一开始在讲这个项目的时候所提到的一块内容，所有的这一块内容都是和我们的这个 URL 相关的，也就是一个开发环境以及是一个生产环境。那么这一点是需要去注意的。


那么首先在这里面我们的一个开发环境，这个我们就注释掉 server URL 先注释，然后下方这是我们的生产环境的话，这里应该是 c a p i 点 z 慕课网 .com，然后这边是一个 foodie 杠 d v 杠 a p i，那么这是我们的一个项目的地址，千万不要忘记要加上一个8088，这是我们的请求的端口。


好，下一个，那么下一个是一个 payment server URL，那么这个我们是不需要去动的，因为这个本身就是由老师提供给大家去调用的，那么直接保留放着就可以了。然后下一个，那么下一个是 shop server URL，那么在这里原先的我们要给注掉，那么在这里我们发布了以后，在这边我们很明显我们应该要去改掉，把这个改成z，然后后方你要加上我们项目的一个项目名，你要把这个福利 shop 给贴过来，贴到这个位置。


那么这样子就是我们的一个我们发布在生产环境上我们门户端的一个地址，那么也不要忘记端口号是要去加上的，那么它的端口是8080。好，随后下一个，那么下一个是用户中心，那么用户中心的话，那么上下两个其实主要是 center 的一个改动，把 shop 改成center，那么这是一个 z 点慕课网，那么后方你也应该要把它的一个项目名给加过来。


OK，那么这样子的话，我们这些生产环境的 URL 就已经是配置好了，然后它还会有一个就是一个 cookie 的组面，就是它的域，我们是需要去把这个域给加上的，把这个改成z，那么这两个开发环境的我们注释掉就可以了。那么这样子的话，针对于我们生产环境的配置就在这里就全部都配好了，一个是 server URL，一个是我们的 shop 门户端的URL，用户中心的 UI 以及是 cookie 的玉，那么大家在进行发布的时候一定要注意你自己的一个端口号，一个是 8080 一个是8088，然后这边漏掉了检查后贴过来，那么这样子的话就可以了。那么这个域名的话根据自己的一个情况可以去配的。


如果说你的域名是这样子的，回车一下，如果说你是 3W 点 a b c . com，那么你的 cookie 左面玉，那么在这边去填写的时候，那么就应该是这样子，以这种形式应该是这个以这种形式去进行一个填写就可以了。OK，好，那么保存一下，那么在这里我们把这一段内容我们全部都拷贝一下以后，那么我们是需要去把另外的一份给打开，另外一份是center，我们右键 open with VS code 打开一下，打开了以后在这边我们也是一样，应该要找到 APP 点JS。那么这一块内容我们应该我们直接把它给去掉删掉，然后把刚刚的全部都贴过来，那么这样子是可以直接去进行使用的。OK，那么这样子的话我们的两套前端的源码就已经是都准备好了以后，那么现在我们应该要把这两个内容去做一个上传吧。


打开 FTP 的工具，然后我们现在应该要去找到咱们的 8080 这个端口所对应的一个target，然后现在应该又是超时的，它的一个服务器的时间是比较少的，那么在这边我重新再去连接一下，重新去连了以后，好进来以后找到咱们的 Tom kit，找到在 user 下方有一个 Lo local，再找到我们的 Tom kit 方向的好进入。那么进来了以后，那么还是一样，我们应该要发布到 web apps，发布到这个里面，所以我们就应该要把这两个源码选中后，直接给拖过来，等待它的一个上传。那么这个包里面所上传的内容是比较多的，所以是需要去等待一会儿的。


那么等到上传完成以后，那么其实我们就可以通过通配台去进行一个访问了。这个访问的话，那么其实也是一样的，我们是通过这个 shop 点 z 点 mock 网 .com，冒号8080，然后后方你要去加上前端项目的一个对应的一个文件夹，也就是项目名称，那么一个是 shop 一个是center，也就是我们在这里面所配置的。我们是可以直接复制这个地址的，复制这个地址那么就可以去进行访问的，然后再看一下，这个文件数还是比较多的，所以上传会有些慢。如果说是一个压缩包上传的话，那么相对来说会快一些，因为文件多了，它就相当于是碎片化的东西，作用比较多。


好，OK，那么现在可以看到全部都是上传成功了，然后呢我们在这里再刷新一下。好，OK，那么回到我们的浏览器，那么在这里面我们就直接把它的地址给贴过来，贴过来 food shop 回车来看一下。那么回车了以后可以发现我们的项目是正常的，可以说我们页面是出来了，效果是出来了，但是你会发现它加载的时候，它里面的一些内容没有显示出来，这是为什么呢？我们按一下F12，我们来看一下，按 F12 在这里面有个 Cor 控制台，然后他会报错来看一下，那么报什么错？他会说在我们调用这个 a p i 点 z 莫狂 .com，这是我们的一个 a p i，也就是后台接口的一个服务地址。


在请求这个地址的时候，从这个 shop 点 z 从这个网站过来的，它出现了一个问题，那么这是什么问题？可以看到这是一个跨域的问题。

[image](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/705030b3-d5b7-4d87-a905-72af4d498d27/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TFBXOPAG%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T224756Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCaqFtV%2BVrBR5UxPIkm5R2MKK%2BGmBK7jg1hntjx%2BwTb3QIgR%2FQno41cD9AVh643ZVdXBh9DEb3xrn88WTHcb%2BTFwLsqiAQIxv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDK6f2SZD5gCBXXYR3ircA3TvbZ57i3LfSyZ%2BXvMpsQGwiV7naX1t8Hvq0hpI7ipU1PNa6N6XPKV9IYPvYMtl1R9UjCfj4ZfQWik2o42b806SLtMh1pCC3whLW0i22H9wVzWEKKzsO1ePGZjkvK5TZCenvyqFtcPCyCud3v2ig56BkMCSNpVb44yiWerWHOZWubfvqJcFBMjrO%2FYO2YD0uxkxMi%2Bd%2BfD6BTU24oh4lHIBOYJN%2FF4SYRZLbnEnCo1UBhQIwbul2PCU0eRHuXVdIWHGP4%2FDSY7P76ehl%2B%2BLMJvBMXoPh3NCLjg6rD9speN%2FIRjRF%2F1Sf7YSOIwgB%2FiWEMUsRPVp2qderiC42RTaUQR%2FtJIK%2Flf2eZdLZsOjynBQunpX3hSPaE3zXMsVGsnE3IK%2BMA8s1mUBCsv1CPs%2BPuy6e0Bm007Wqqr%2FhBRqSh278m020tlyCr9QeXyFL1nHPgj7pjLimTZzVx4Y8S8buhKrQ0vfHLDdi6GsXZxzZEcywZV76gNKmMANnsYbDis6C6L3xij1q9RWnMQNfzuoNVVWtDRRpQxoFQ9byRKOwrQ4qyk4cqdNk9vMqb0URcr9axOvmXXE%2B9HwUXmQWKgGyDp1TeXHLB0sITA23LtmHnBzbVMW8ltZ5s8UeVjHMKi3%2F9IGOqUBi8XdFR%2B5tK3wO0goUqkWY2jbjtIUiMNbZ%2F8%2Bzl0F6%2Bl00wb2xmFQA7DyVHmZSBpYIe5Rx4%2FPrrIidX%2Fwydzum9wbVr%2BC2Du8dpEQ2o1pKvmP89y3bd5btYDUYEFKAlohIUcbqFE7MBff43SClDRA1veYVkeL3UpjVI6q9b%2FODpK%2FFaO27ax76dISx%2FAktLYuQWRUCvVHFs9ut6XZskTT%2Bz%2Byd9kC&X-Amz-Signature=0a525293187c2f2c8e5aa347dad0af075eeff9b343209a9deb8928b9aa504a59&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

OK，因为我们是其实是发布到两个不同的 term torque，它肯定会存在一个跨域的问题。那么这个我们在之前在做开发的时候其实也是遇到过的，所以我们应该要相应的去把这个跨域的问题也要去解决一下。


那么打开我们的这个idea，那么我们之前是写了一个 Cos config，在这个里面我们是增加了一个 local host，这个8080，那么在这里面其实我们也是可以去添加相应的额外的一个域，我们呢把这个拷贝一份，再额外的去添加一个，那么你所要去添加的那个就是你请求的那一端。


我们找到咱们的这个，我们把这个 CS code 打开，那么其实总共是 2 块，那么一个是这个地址，这是我们的 shop 点z，你需要把这个复制一下贴过来，贴到我们的 idea 这个部位。好，这是第一个地址，随后你还需要再复制一个地址，那么下一个是Santa，因为我们在 Santa 里面，其实它也会发起相应的请求的，拷贝一下，然后我们也要贴过来。


猜到 idea 这个部位，一个是shop，一个是center，那么这两个写了之后，我们再去额外的去再去贴两个。我们把这个 8080 这个端口去掉，我们可以通过这种方式也可以。那么这个的话是为我们以后做一个准备，因为我们在以后去请求的时候，我们是不会携带这个 8080 端口的，我们都会通过 engines 去规避。那么这样子的话我们就可以直接把这个 config 去上传，并且覆盖我们本地的一个源码就可以了。

[image](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/2eca8471-461d-4c1b-8b61-9477cb4137b1/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TFBXOPAG%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T224757Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCaqFtV%2BVrBR5UxPIkm5R2MKK%2BGmBK7jg1hntjx%2BwTb3QIgR%2FQno41cD9AVh643ZVdXBh9DEb3xrn88WTHcb%2BTFwLsqiAQIxv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDK6f2SZD5gCBXXYR3ircA3TvbZ57i3LfSyZ%2BXvMpsQGwiV7naX1t8Hvq0hpI7ipU1PNa6N6XPKV9IYPvYMtl1R9UjCfj4ZfQWik2o42b806SLtMh1pCC3whLW0i22H9wVzWEKKzsO1ePGZjkvK5TZCenvyqFtcPCyCud3v2ig56BkMCSNpVb44yiWerWHOZWubfvqJcFBMjrO%2FYO2YD0uxkxMi%2Bd%2BfD6BTU24oh4lHIBOYJN%2FF4SYRZLbnEnCo1UBhQIwbul2PCU0eRHuXVdIWHGP4%2FDSY7P76ehl%2B%2BLMJvBMXoPh3NCLjg6rD9speN%2FIRjRF%2F1Sf7YSOIwgB%2FiWEMUsRPVp2qderiC42RTaUQR%2FtJIK%2Flf2eZdLZsOjynBQunpX3hSPaE3zXMsVGsnE3IK%2BMA8s1mUBCsv1CPs%2BPuy6e0Bm007Wqqr%2FhBRqSh278m020tlyCr9QeXyFL1nHPgj7pjLimTZzVx4Y8S8buhKrQ0vfHLDdi6GsXZxzZEcywZV76gNKmMANnsYbDis6C6L3xij1q9RWnMQNfzuoNVVWtDRRpQxoFQ9byRKOwrQ4qyk4cqdNk9vMqb0URcr9axOvmXXE%2B9HwUXmQWKgGyDp1TeXHLB0sITA23LtmHnBzbVMW8ltZ5s8UeVjHMKi3%2F9IGOqUBi8XdFR%2B5tK3wO0goUqkWY2jbjtIUiMNbZ%2F8%2Bzl0F6%2Bl00wb2xmFQA7DyVHmZSBpYIe5Rx4%2FPrrIidX%2Fwydzum9wbVr%2BC2Du8dpEQ2o1pKvmP89y3bd5btYDUYEFKAlohIUcbqFE7MBff43SClDRA1veYVkeL3UpjVI6q9b%2FODpK%2FFaO27ax76dISx%2FAktLYuQWRUCvVHFs9ut6XZskTT%2Bz%2Byd9kC&X-Amz-Signature=dee06c8e2f6641b65c40f38478149dbab025c95d33aa5229f4042166ab990623&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)


```java
/**
 * <h1>配置跨域</h1>
 */
@SuppressWarnings("all")
@Configuration
public class CorsConfig {
    public CorsConfig() {
    }

    @Bean
    public CorsFilter corsFilter() {
        // 1：添加cors配置信息
        CorsConfiguration cors = new CorsConfiguration();
//        cors.addAllowedOrigin("http://localhost:8080");
        cors.addAllowedOrigin("http://localhost:8080");
        cors.addAllowedOrigin("http://172.16.136.223:8080"); // foodie-shop    http://172.16.136.130:8080/foodie-shop
//        cors.addAllowedOrigin("http://172.16.136.130:8080"); // foodie-center, 如配置域名这里还需要一个  http://172.16.136.130:8080/foodie-center
        // 如果使用nginx不会使用 端口号了 只有ip地址或者域名

        cors.setAllowCredentials(true); // 是否允许发送cookie

        cors.addAllowedMethod("*"); // 设置允许的方法
        cors.addAllowedHeader("*"); // 设置允许的头

        UrlBasedCorsConfigurationSource corsSource = new UrlBasedCorsConfigurationSource();
        corsSource.registerCorsConfiguration("/**", cors);

        return new CorsFilter(corsSource);
    }
}
```

那么这样子的话我们还要不要去做一个打包呢？那么肯定是需要去做打包的，也是需要去做的，在这边我们重新的先去clean，然后再去 install 好，肯定成功，然后再来一个install，好， install 成功了。成功以后，那么我们和之前一样，把这个从我们本地打开，打开以后我们是需要找到咱们自己的一个 targets，然后把这个包我们是需要去拿过来，贴到这里，那么在这里面的话，我们原来的这个包可以去删除，把这个他的名字要去改掉，改成这个。那么这样子我们可以直接把这个外包上传到咱们的服务器，或者你可以在本地解压，把 class 文件直接给放到我们的远程服务器做一个替换。这两种方式其实都是没有问题的，那么在这边的话我就演示一下新的，那么在这边我双击一下，我们做一个解压。好，现在是解压成功了，解压成功以后，那么我们可以进入到这个文件里面，一层一层去找，那么这个就是他帮我们做一个压缩后，也就是打包后的一个目录层级。

我们所有的一个 Java 类全部都会编译成class，都会放到这里面，然后找到 Com imock，再找到configure，下面会有一个 Cos 


configure 对吧。那么 idea 其实它支持我们 class 的一个反编译，我们是可以把它丢到我们的 idea 里面来，拿过来，拿过来以后，那么这是一个 class 文件，那么你会发现在这边它会那么这是我们之前所写的代码吧，那么在这里它全部都会有，说明我们的一个打包是成功是没有问题的。


好，那么接下来的话我们就需要把这份文件放到要上传到我们的这个 f t p 的这个工具里面，那么这现在它的服务器又断开了，我们再重新的去连一下，然后还是一样，我们要去找到 user local，再找到我们的 front end。错了，应该是在 a p i，再找到 web apps，那么一层一层往里面去找，再找到咱们的一个解压后的这个文件夹，也就是咱们的项目层级是一样的。


找到 class Com，点imock，点config，其实也就是这个文件，我们要把它进行一个替换，那么现在它的一个文件大小是1445，那么在我们本地把这个文件来选择，我们是需要去移过来，我们直接覆盖好了以后做一个刷新。那么现在它的文件大小是1627，那么上传完毕以后，那么我们还是不能够去使用的，因为这个 class 你是需要去重启一下咱们的服饰，所以你需要去把我们的命令行工具进行一个打开，打开以后那么是需要去进入到我们的 Tom kit a p i，然后进入到 being 做一个重启点。


斜杠 shut them down 好，这是一个关闭，然后关闭了以后我们要重新的 start up 回收一下，那么这是一个重启好了以后回到我们的一个站点刷新一下，那么刷新了以后，那么你会发现现在在我们的控制台这一块内容就没有任何的错误了，然后呢我们的数据是不是可以成功的拉出来了？OK，然后在这边它也是一个懒，加载都是没有问题的，然后这边是我们的分类，所有的数据全部都可以拿到。OK，那么这样子的话，我们这个网站前端源码就已经是成功的发布了。

