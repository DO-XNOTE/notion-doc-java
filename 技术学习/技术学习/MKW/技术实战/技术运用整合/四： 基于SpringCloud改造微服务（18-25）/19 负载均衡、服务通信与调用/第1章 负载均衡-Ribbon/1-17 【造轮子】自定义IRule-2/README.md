---
title: 1-17 【造轮子】自定义IRule-2
---

# 1-17 【造轮子】自定义IRule-2

[image](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/42db0475-a9fa-4ab0-abef-1dcce75976e6/SCR-20240718-hogl.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SRQF6MQJ%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T225616Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIEZsrNUwIUod67LHrYZ%2BDKy398V0RQqPmYA6U2cKBtrOAiAizp6vjrOC22HfXZxo%2FBFUWqwg7BprZm5kNcu3l5IpOiqIBAjG%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMOO8CnT%2B3gzxqL7l8KtwDVabZTONLNbYyv2NWRSdsnaLBx3uZHiOvSWjqqW88bRLtu8pXQq8F1%2BBJrwk34qyArED0rJimW%2Fo4%2FSOk4F6xF4SH0IbIdY01G1X9p%2Fi070SYreuEF2inRqPkJWizgP%2FTnLG1SCCufDPXGJ8KwYgcuui7vRyuEhRk17zcuJzYr%2FCW%2FiI6DyfLS2aEbmEdh6gbHRAbDO30VgCs%2BIAhwyxv%2BcMtzToYeZuGtoBg%2BfF%2BlV9tJjUy5keHZ1I9fmxrdEnW9mY%2BoEs3%2Bt8MEy2VgMZhlBPcKB3BDa1cyiaweAf0NQHb4jHde5EhcAtpSU8atP%2FvID7kiQ1tmMXggdpF6HM7IzbEycLZhad1raRFMiuYRh4OuvFxpfMqvuDfiB4q3mHtQBQmsoblox1xKXUxbaWjOuJlfJ6j6hXnZbbTnT2VptK7T0B4LoNOmVFXSpOq7aarfSY6Yf4B2qUaqVz%2B3vP5Jj50eJutSIolim4Wm3hJ8IVLPNFrPJsoVNUYFkk9IRtLPDqszewLZoIPBDX5ZC4yp88q%2BJPx87WGgAsuw05S%2BtC2TYbpk5c9dNM20%2B1Ci3KJpALm422pOTU2cGYAq5wh0moyQ8cnLiSrVhc9lUgeV4tyEIfeNaebZnfZTNcwybj%2F0gY6pgHmYyDYSeKFUlio7pLLC1cUYf2%2BUIwQugIVX%2FxIlCEbIG3iEB9c283uEycUKN%2FXnqJy6B51UUAK7qllKHCiXdOCk6Wrt6XeJWUxV6j9HZBBKRGsuFpdQPXjfD4iqOCwvcTllEXvGCnj8ZsItIKruGyt5lz6WOOqRPx6Pi5e%2Bc43o%2BMmBeTnllT7CNoVxfc%2Bi%2FlQQSJXgdOJ5mq3thTJSmmnwZe52B8L&X-Amz-Signature=32eeb8616f3374d28a24372335343c204f8be72de139a3592c825fc3d61db87f&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

[image](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/78216cae-731e-40eb-8931-f3a69e5600cd/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SRQF6MQJ%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T225616Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIEZsrNUwIUod67LHrYZ%2BDKy398V0RQqPmYA6U2cKBtrOAiAizp6vjrOC22HfXZxo%2FBFUWqwg7BprZm5kNcu3l5IpOiqIBAjG%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMOO8CnT%2B3gzxqL7l8KtwDVabZTONLNbYyv2NWRSdsnaLBx3uZHiOvSWjqqW88bRLtu8pXQq8F1%2BBJrwk34qyArED0rJimW%2Fo4%2FSOk4F6xF4SH0IbIdY01G1X9p%2Fi070SYreuEF2inRqPkJWizgP%2FTnLG1SCCufDPXGJ8KwYgcuui7vRyuEhRk17zcuJzYr%2FCW%2FiI6DyfLS2aEbmEdh6gbHRAbDO30VgCs%2BIAhwyxv%2BcMtzToYeZuGtoBg%2BfF%2BlV9tJjUy5keHZ1I9fmxrdEnW9mY%2BoEs3%2Bt8MEy2VgMZhlBPcKB3BDa1cyiaweAf0NQHb4jHde5EhcAtpSU8atP%2FvID7kiQ1tmMXggdpF6HM7IzbEycLZhad1raRFMiuYRh4OuvFxpfMqvuDfiB4q3mHtQBQmsoblox1xKXUxbaWjOuJlfJ6j6hXnZbbTnT2VptK7T0B4LoNOmVFXSpOq7aarfSY6Yf4B2qUaqVz%2B3vP5Jj50eJutSIolim4Wm3hJ8IVLPNFrPJsoVNUYFkk9IRtLPDqszewLZoIPBDX5ZC4yp88q%2BJPx87WGgAsuw05S%2BtC2TYbpk5c9dNM20%2B1Ci3KJpALm422pOTU2cGYAq5wh0moyQ8cnLiSrVhc9lUgeV4tyEIfeNaebZnfZTNcwybj%2F0gY6pgHmYyDYSeKFUlio7pLLC1cUYf2%2BUIwQugIVX%2FxIlCEbIG3iEB9c283uEycUKN%2FXnqJy6B51UUAK7qllKHCiXdOCk6Wrt6XeJWUxV6j9HZBBKRGsuFpdQPXjfD4iqOCwvcTllEXvGCnj8ZsItIKruGyt5lz6WOOqRPx6Pi5e%2Bc43o%2BMmBeTnllT7CNoVxfc%2Bi%2FlQQSJXgdOJ5mq3thTJSmmnwZe52B8L&X-Amz-Signature=2c67ff8fd29f461ca0f6dec529261561a7280bbafa72927cd1d8e0e8ff5647e7&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

慕课网的同学们，大家好，欢迎来到下半场。 OK 我们接着上半场的内容继续创建一致性哈希的负载均衡策略，我这里给大家打一些注释，这里循环每一个 address list 是虚化若干个服务节点到哪里到环上上环下环这个跟上环取环可不一样。


好，到环上。然后我们就开始走正戏了。当我们拿到了这个 tree map 以后，我们就要想从 tree map 里怎么获得到一个 key 呢？那既然想要获得一个 K 我们就要先有一个 K 对不对？那这里来了，我们通过还是算法把什么传入进去呢？把这个 hash ID 传入进去，通过这个 hash 算法来一把。好，它是一个 int 值，我们就用 string.value off 把它改成一个非 int 这个 hash ID 是前面算出来的，对不对？是前面这一步通过 UR I 算出来的。那我这里并不把它打算直接使用，而是通过这个 hash 再算一遍，得到最终的 launch 然后拿到浪形以后，我们从 ij S 里面顺时针的方式找到这个服务，它的数参是什么？就是 hash OK 拿到 hash 以后把它给接收 sorted map 因为它这个 tail map 会拿到所有比它大的这些节点。那我接下来从它的返回值中直接取第一个节点。


好了，first key 那就是离它最近的那个节点了，非常简便。这个 tree map 还有其他非常好用的方法。我以前在刷题的时候，经常使用 tree map 解决一些写代码会很复杂的问题，用 tree map 的一个方法就迎刃而解。 OK 所以我们这里先判断什么呢？如果你的 last 是 empty 你要是 empty 那我不能从你这里拿了对不对？你没有找到节点，那我只好曲线救国，从这个 ajax 里面拿出它的 first entry 再 get 它的 value 把这个服务返回。那假设你不为空怎么办呢？那你不为空，我当然是要取你性命，怎么取你性命，我拿到它的第一个 first key 就来取对不对？ get first key 好，我拿到了 first key 从这里面 get 到的 server 也就是 first key 指定的 server 那同学们知道这里为什么它有可能为空吗？为什么？当有一种情况的时候会发生，也就是说当 request UL 里面的这个 K 它所生成的 hash code 大于你任何一个在前面初始化的 address 也就是说你走到尽头了，没有比你这个 key 更大的节点。
那这种情况怎么样呢？我就把它认为这个 tree set 是个首尾相接的环，你的 request 已经到了尾环的最后一个节点，你没有比它再大的了，所以那就怎么样重新来过，那就把这个 address 里面的第一个节点当做你的上游，所以它这里会从这个 address 里面取第一个节点，我们把它看成了一个首尾相接的环状。 OK 那我这里把注释补全，当 request uio 的还是值大于任意一个服务器对应的 key 这时候怎么办？这时候就取这个 address 中的第一个节点。


OK 那这一步完成了，这一步完成以后我们要怎么办？我们是不是要实现 hash 方法了？因为走到现在只剩 hash 没有实施了。那么首先第一步我要做的是声明一个 message digest 它是 security 包下的一个类。好生命完了以后，我们将要用 MD 5 给它做初始化。因为 MD 5 它会有一个必须要检查的异常抛出，所以我们这里要用 try catch 这个 trackache 里面我们采用 MD 5 等于谁等于 message digest get instance 这里不要打错，这个 instance 的名字就叫 MD 5。 OK 那我们把这个异常给它捕捉住，不要扔出去，自己的事儿不要给别人添麻烦，我们把它给捕捉上。然后这里直接给它 through 出去。 through 出去之前，用 new runtime exception 把它封装一下，这是一个未检查的错误。


OK 好，接下来我们声明一个 bites 这个 bytes 是做什么事的呢？我们接下来往后看，我们要把这个 key 生成成一个二进制的 bytes 数组，怎么来做 keybytes 等于谁呢？等于这个 key get bytes 指定一个 encoding URL UTF 杠 8 想起刚学编程的时候， decode encode 一直是一个很麻烦的事情。当时还在写 PHP 那时候我就记得要把数据库页面还有程序代码，所有 D code encode 全部改写成同一个，这样的话一定就不会出现乱码问题。我觉得很多程序员在一开始刚学编程的时候，第一个所要处理的可能都是乱码问题，对新人来说还是蛮头疼的。那我这里依然选用上面的一样的做法，把它采取用 runtime exception 给包装一层再扔出去的方式。好，那这里就把这个 key 通过 UTF 杠 8 读到了，对不对？那读完以后，我们这要做什么呢？我们要把 MD 5 给它更新到这个 K 里面去，更新完以后我需要把它的摘要做出来。所以大家看清楚这里面的运作方式了吗？这个update ，相当于把 key 塞到了 MD 5 这个算法里。然后 digest 相当于利用这个算法输出一串正儿八经的 bite 数组，这个 byte 数组就是我们最终的摘要。那大家知道这个摘要它的大小有多大吗？它的 byte 有 16 位。


所以接下来的一步我们就是要生成 hash code 根据谁正式根据这个摘要来生成好怎么生成？相信大家自己一定手写过 hash code 函数对不对？那大家学了这么长时间的 Java 一定知道 equals 和 hashcode 这两个函数之间有什么关系，为什么改写一个，另一个也要改写？相信大家这么长的工作时间，肯定也亲自改写过 hashcode 我们这里既然知道带 jest 是 16 位怎么来做呢？我们不用按部就班，把这 16 位全部写上去，也太费事了，我们就挑其中的几个来写好了。比如说我们从它的第三位开始，第三位是谁，第三位它的下标应该是 2 对不对？好，我们渠道 digest 2，然后这个 digest 是 byte 数组，我们需要把它转成 launch 这里用一个语把它转成 launch 接下来做一位操作。第二位我们往前移 16 位好，移完以后我们通过复制粘贴，用同样的方式把前面的数字也都给它补全。接下来要补全的是第一位它应该是 8 位 1 位，最后一个是什么？是第零位，第零个位还要一位吗？还不需要了，一位 0 等于没1。 OK 就这样直接就可以了。


好，这个 long 其实也是可以去掉的，我们这里先放在这，完了以后这就搞定了吗？还没有 not yet 我们需要对它做一个 trunk 也就是 hashcode 还要与 oxfff F1 支 F 总共有几个 F 呢？大家记住，总共有 8 个 F 我们这里数一下 12345678 还多了一个。好去掉。那这就 OK 了，我们把这个数字作为浪行返回。


好，我们的 hash 写好了， root 写好了， truth 写好了，整个 Mirror 也就搞定了。那接下来大家知道要做什么吗？给它声明一个没有构造器的构造方法，然后我们就可以大显身手了。打开小桌板，把我们默认的负载均衡策略改成谁，这还是 random row ，我们不用它改成自己的 Mirror 好，这一步改好之后，我们就紧接着来测试一把。


怎么测试很简单， eurika server 骑起来，接着把 eureka client 也给起来起几个，因为我们是一致性的哈希策略验证，所以一个节点肯定不够。我们像之前一样，其他三大炮三个节点一起跑起来来。第一个节点跑起来，改一下端口，紧接着跑第二个节点，我再改一下端口，接着跑第三个节点。这三个节点都启动完以后，我们接着把 ribbon client 也启动起来，找到它的慢函数直接跑起来。等瑞本启动起来以后，我们到 postman 里实际的去调用一把。


按照之前的说法，如果我们这个一致性希实现的正确，它会有什么行为呢？针对同一个 URL 它所负载均衡选择的机器应该总是同一个，对不对？好，我们这里访问 local host31,000，然后它的端口后面的 URL 紧跟着是 say hi 我们后面加一些测试参数，这个参数实际上并没有用到，我字写的比较小，这个参数是 test 等于32123。这个参数还没有用，我们只把它写在这里，用来验证服务请求是否被转发正确。


好，我们看到日本已经启动起来了，发第一个服务请求，大家看到是谁响应的 30,001 我们再发一次还是三万零一一直都是30,001，看起来完美无缺。对不对？我们把这个 test 等于 32123 给它改一下，等于多少呢？等于108，看是谁？也是 30,001 响应的。看样子这两个哈希值落在了同一块。那这里把 108 换成一再试一下。看到吗？它的 port 改到了 3 万，你不管怎么点，只要你的 URL 保持不变，那它的 port 永远都是 3 万。好，那我这里把这个一再改成 21 下看到吗？又跑到了30,002。


那说明什么？说明我们的一致性希算法已经正常的运作了。当然这只是一个非常非常简易版的算法，它后面肯定还有非常非常多需要改进的地方。如果有兴趣的同学，可以在网上查阅一些语句性哈希的标准做法，然后把我们的算法改成一个绝对平均公平的一致性哈希算法。Ok.这一节的内容就到此为止了。我们这一小节下半场和上半场合起来，总共学习了两个知识。第一个知识是一致性哈希的做法。第二个知识是如何自定义一个负载均衡策略，并且应用到我们的服务当中。 OK 那到此为止，瑞本章节就算告一段落了，在接下来的复习小结，我将带大家回顾一下整个章节的内容，然后再分享一些自己的学习工作中心得感悟。好同学们，那我们下一小节再见。

```java
@NoArgsConstructor
public class MyRule extends AbstractLoadBalancerRule implements IRule {
    @Override
    public void initWithNiwsConfig(IClientConfig clientConfig) {

    }

    @Override
    public Server choose(Object key) {
        // 强转
        HttpServletRequest request = ((ServletRequestAttributes) RequestContextHolder.getRequestAttributes()).getRequest();
        // 获取用户的请求 url 来自作摘要（hash算法）
        String uri = request.getServletPath() + "?" + request.getQueryString();

        return route(uri.hashCode(), getLoadBalancer().getAllServers());
    }

    public Server route(int hashId, List<Server> addressList) {
        if (CollectionUtils.isEmpty(addressList)) {
            return null;
        }

        TreeMap<Long, Server> address = new TreeMap<>();
        addressList.stream().forEach(e -> {
            // 虚化若干个服务节点，到环上
            for (int i = 0; i < 8; i++) {
                long hash = hash(e.getId() + i);
                address.put(hash, e);
            }
        });

        long hash = hash(String.valueOf(hashId));
        // tailMap 能获取到 8 个服务节点中最近的那个一个, tailMap返回所有比他大的节点,去他的第一个 first
        // 当request URL 的hash值大于任意一个服务器对应的hashKey
        // 取 address 中的第一个节点
        SortedMap<Long, Server> last = address.tailMap(hash);

        return last.get(last.firstKey());
    }

    public long hash(String key) {
        MessageDigest md5;
        try {
            md5 = MessageDigest.getInstance("MD5");
        } catch (NoSuchAlgorithmException e) {
            throw new RuntimeException(e);
        }

        byte[] keyByte = null;
        try {
            keyByte = key.getBytes("UTF-8");
        } catch (UnsupportedEncodingException e) {
            throw new RuntimeException(e);
        }

        md5.update(keyByte);
        byte[] digest = md5.digest();
//        hashCode 是 16 位,  取几位就行了   digest是数组-》转成long
                                              // 第二位往前移动16位置          // 第一位往前移动8位，    // 第一位往前移动0位置（没有移动）
        long hashCode = ((long) (digest[2] & 0xFF << 16)) |
                            ((long) (digest[1] & 0xFF << 8)) |
                            ((long) (digest[0] & 0xFF));

        return hashCode & 0xffffffff;  // 8个 f
    }
}
```

```java
package com.imooc.springcloud;

import com.imooc.springcloud.rules.MyRule;
import com.netflix.loadbalancer.IRule;
import com.netflix.loadbalancer.RandomRule;
import org.springframework.cloud.client.loadbalancer.LoadBalanced;
import org.springframework.cloud.netflix.ribbon.RibbonClient;
import org.springframework.context.annotation.Bean;
import org.springframework.context.annotation.Configuration;

/**
 * <h1></h1>
 */
@Configuration
//@RibbonClient(name = "eureka-client", configuration = com.netflix.loadbalancer.RandomRule.class)
@RibbonClient(name = "eureka-client", configuration =  MyRule.class)
public class RibbonConfiguration {

    @Bean
    @LoadBalanced
    public IRule defalutLBStrategy() {
        return new RandomRule();
    }

}
```


