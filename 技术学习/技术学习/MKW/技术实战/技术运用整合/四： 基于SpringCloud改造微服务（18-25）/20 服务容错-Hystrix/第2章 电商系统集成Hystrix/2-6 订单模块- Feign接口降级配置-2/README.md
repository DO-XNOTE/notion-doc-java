---
title: 2-6 订单模块- Feign接口降级配置-2 
---

# 2-6 订单模块- Feign接口降级配置-2 

[image](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/3fc10e73-e0ce-4558-9bbf-cc6ad32aba23/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UYA2CFQP%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T225658Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDgtnULKs3Sk5eqsjkUzYf0DCj42bZ0OlIN8BOYcSeIMgIhALG0eJJF8G%2B2ZZ2buvDRjiYQY9unOhBcwMp1VD6eSDqGKogECMb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgxbyeTs5gTIH7RzwDAq3AOzRluRCTsBSzRlBDx3nJCvCT0KS8GUy%2Bp3yX%2FRkbYOvNbUvDBYe2GIwcmRprz5bt3hnSTYsSsLF%2Btz3qOyOf%2Bh6wvvxbyXpQqv8A5Uvdis9Fmo59nsWrRuB%2BI%2BBIxyUutyf6z0DZeS1i17keuRpOvWLAeXJXXZCmEIpL6hqPKkLS1q6SlO4c%2Fspb8TJZjKgeGoQ%2FtXrYCRj%2B6DweZwdor8vQy4e%2BtbdcvCIys2XA7Z8%2BMi%2B2JkvFmhQvrSvXWCYGfU04mAFMz5Wxvcc22jfo8ugOBrF5a1yGSuj%2FVlKyH2dhbkBIy%2F3E6uAJfA0qjhWYGx1j9%2B2hk94ZNbUZl4fB9RJg3DbdStAUQWeR4Kd4Lq0ncFoHXA9jmMkJg47lk0%2BqwdAou%2B%2BPD%2Bmbp1yDfjpjE7qFFhC7d2kVyftF2z2bptVK1KFgbojCug0rhovlhWsZ%2BFSTcH35duwsH0047PdhmZr5%2BmFYIiR5h0dnhXpK3zRUtQGYUbyaeRPRTCejC0fUpD8DBGShyReZZSz6Z3ObxDNm1t2IEn3qvti%2Bovt%2B0wLajsinZHGOaxGZ3%2FFTLAWJ2L5cMVxYX1HyMj2dOoodYS4lfO63%2F%2BFCyrAvgGTbDrUMt5QMVhnhKeM6c89DD%2Fuf%2FSBjqkAfmSQ4acoA7oEY6azRAB9LnB7HyvYB1SpF8JTJLQ1E7IXqQS1yJF55Le5xm0zYZ7MOAD6L3qF2zyStEDXDr99zBRhYB8AFekfUNHbXlViDKdnk6lDMguebmdYk7ssst%2FYXExMf45ssiHjYXecnGMHDLOPyJvSnWlRk5fFvpydaGsz5wYUqiKSaJKmzKH5c3yM%2B5MSuKnfZPjQA0eXbRaLk48fW2r&X-Amz-Signature=d4b1698c05307cd1e2e269a1170373de553cdd0b80ae27a713a49b63d20da4f4&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

[image](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/08494c17-5570-4dcf-b1c1-f17c5c8353e8/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UYA2CFQP%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T225658Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDgtnULKs3Sk5eqsjkUzYf0DCj42bZ0OlIN8BOYcSeIMgIhALG0eJJF8G%2B2ZZ2buvDRjiYQY9unOhBcwMp1VD6eSDqGKogECMb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgxbyeTs5gTIH7RzwDAq3AOzRluRCTsBSzRlBDx3nJCvCT0KS8GUy%2Bp3yX%2FRkbYOvNbUvDBYe2GIwcmRprz5bt3hnSTYsSsLF%2Btz3qOyOf%2Bh6wvvxbyXpQqv8A5Uvdis9Fmo59nsWrRuB%2BI%2BBIxyUutyf6z0DZeS1i17keuRpOvWLAeXJXXZCmEIpL6hqPKkLS1q6SlO4c%2Fspb8TJZjKgeGoQ%2FtXrYCRj%2B6DweZwdor8vQy4e%2BtbdcvCIys2XA7Z8%2BMi%2B2JkvFmhQvrSvXWCYGfU04mAFMz5Wxvcc22jfo8ugOBrF5a1yGSuj%2FVlKyH2dhbkBIy%2F3E6uAJfA0qjhWYGx1j9%2B2hk94ZNbUZl4fB9RJg3DbdStAUQWeR4Kd4Lq0ncFoHXA9jmMkJg47lk0%2BqwdAou%2B%2BPD%2Bmbp1yDfjpjE7qFFhC7d2kVyftF2z2bptVK1KFgbojCug0rhovlhWsZ%2BFSTcH35duwsH0047PdhmZr5%2BmFYIiR5h0dnhXpK3zRUtQGYUbyaeRPRTCejC0fUpD8DBGShyReZZSz6Z3ObxDNm1t2IEn3qvti%2Bovt%2B0wLajsinZHGOaxGZ3%2FFTLAWJ2L5cMVxYX1HyMj2dOoodYS4lfO63%2F%2BFCyrAvgGTbDrUMt5QMVhnhKeM6c89DD%2Fuf%2FSBjqkAfmSQ4acoA7oEY6azRAB9LnB7HyvYB1SpF8JTJLQ1E7IXqQS1yJF55Le5xm0zYZ7MOAD6L3qF2zyStEDXDr99zBRhYB8AFekfUNHbXlViDKdnk6lDMguebmdYk7ssst%2FYXExMf45ssiHjYXecnGMHDLOPyJvSnWlRk5fFvpydaGsz5wYUqiKSaJKmzKH5c3yM%2B5MSuKnfZPjQA0eXbRaLk48fW2r&X-Amz-Signature=483d6e7099258464f57a4c1cbae94632146a738af47377b0f47516e943ae82d7&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

hello 慕课网的各位同学们，大家好，这一节我们继续来配置分接口的降级逻辑。好，咱的分 client 这里可以通过两种方式来指定降级的逻辑。第一种是通过 fallback 的方式，第二种是 fallback factory 的方式。那咱这里就都给大家演示一下呗。那我们首先来看一下大家都最熟悉的这种 fallback 的方式。其实这种方式在配置的时候有一个要绕过去的坑，什么坑我们往下看就知道了。
好，这里创建一个叫 item comments fall back delayok 那让这个类我给它继承字实现这个接口，哪个接口呢？当然是 item comments 咱的 phone client 好，继承完之后要实现它的默认方法。好临末了，我们别忘了给它添加一个 component 然后把这个类名 copy 一下，再返回到咱的分 client 上面，把这个 fallback 指定上去，看起来是不是如行云流水，无丝毫障碍。但是咱不信，启动起来看一下。


这里面有一个小细节需要注意一下。那这个细节引发的问题和上一节当中跟大家说的启动类 ambitions mapping 是一样的，他这边又爆出了一个 ambitions mapping 那相信经过上一节的学习，同学们应该比较了解了，因为为什么咱的 item comments 上的这个 request mapping 注解的经过一系列的继承，那也同样的继承到了这个 fallback 上面。所以这个 item comments fallback 和咱的 thin client 这两个类同时都被加载到 spring 的上下文当中。然后也有了同样的方法 request mapping 的匹配路径。那解决方案非常非常简单，咱的这个 item fall back 它只不过是一个本地方法，对不对？它并不需要真正的发起远程调用。所以说有一个最轻松的解决方案，直接跟他造一个假的 request mapping 这个名称就给它叫做 joke joke 好了，因为反正它发起不了远程调用，所以咱用这种方式把 spring 蒙混过关。

```java
@Component
@RequestMapping("JokeJoke")
public class ItemCommentsFallback implements ItemCommentsFeignClient {

    @Override
    public PagedGridResult queryMyComment(String userId, Integer page, Integer pageSize) {
        return null;
    }

    @Override
    public void saveComments(Map<String, Object> map) {

    }
}
```

好，那咱接下来这里可以去指定降级的具体逻辑了，这些 request mapping 都可以给它统统拿掉。好，那我这里就示范性质的跟大家随便写一个，比如 query my comments 那如果咱的这个 item comments 它的服务抛出了异常，那这种情况下有个非常简单的方式静默降级就是最好的处理方式。那我们可以添加一个 item comment VO 这个 VO 我们给它加一些可以让人心情极度愉悦的降级话术。比方说我告诉他 set comments 我说正在加载中好不好啦，给人一种正在疯狂加载的假象。那我就把这个默认值给它返回回去，把它包装在这个 page 的 grade result 当中。那我看这里，把这个 result 的 set set she set rose 把 target 放进去，这里要把它包装成一个 list 的对象，好把它塞进去。然后我们把它的总页数给它设置成 1 还有它的总条数，我也给它设置成一好直接把它返回，就可以了。


前面在课程 demo 的时候，我们还讲过，一个降级流程中可以嵌套多级降级对不对？我们这里可以通过添加 high strikes command 这个注解来实现多级降级，你想实现几级，那就实现几级降级。 OK 那这种方式跟大家 demo 完之后，我来再带大家去看一下另外一种方式，也就是通过 fall back factory 配置的方式。好，我们把这行注解给它 copy 一下，在下面另起一行。好嘞，然后把这后面的这个 fall back 给它替换成 fall back factoryok 后面的这个类给它去掉。


咱这里要创建一个新的工厂类。话说工厂这种设计模式应该是所有的开源项目当中应用最广泛的。其实这些设计模式它原理都非常非常简单的，像设计模式那本书里面介绍到 23 种设计模式，其实有很多个设计模式都是浑水摸鱼，其实类似的都是通过一种在这之上经过一些变形得出来的。大部分的设计模式其实就是围绕着继承和多态，超简单的。好，我们这里创建好了一个 factory 类，它叫 item comments fallback factory 然后我这里要给它继承一个接口，继承自 fallback factory 好，它这还有个泛型，直接把它的 create 方法给它实现了。 OK 那这个工厂类咱跟它也扣上一个大绿帽子 component 注解扣上去。


OK 它 create 的什么类型呢？我们这里可以给它指定好一个类型，是咱前面创建的这个分 client 好，我们把这个类型给它写上，同学们也可以在继承接口的时候把这个泛型给它加上，都一样的。好，那这里创建方式非常的简单，我们这里直接来一个匿名内部类，把它给搞定好了，这里实现掉。然后它没有实现的接口，咱这里都给它添加上来，和前面的方法处理方式一样。那这个用不到的一些注解，咱就给它清理掉就好了，这三个家伙都给它拿掉。 OK 那剩下的逻辑，我们可以从刚才咱创建的这个 fallback 类里面，直接把它给 copy 过来，然后粘贴到工厂类里面。好嘞，这就大功告成了。然后在这个 client 上面，咱把刚才创建的这个工厂类给它写上去。

```java
/**
 * <h1></h1>
 */
@Component
public class ItemCommentsFallbackFactory implements FallbackFactory<ItemCommentsFeignClient> {


    @Override
    public ItemCommentsFeignClient create(Throwable cause) {
        return new ItemCommentsFeignClient() {

            @Override
            public PagedGridResult queryMyComment(String userId, Integer page, Integer pageSize) {
                MyCommentVO commentVO = new MyCommentVO();
                commentVO.setContent("正在加载中");

                PagedGridResult result = new PagedGridResult();
                result.setRows(Lists.newArrayList(commentVO));
                result.setTotal(1);
                result.setRecords(1);
                return result;
            }

            @Override
            public void saveComments(Map<String, Object> map) {

            }
        };
    }
}
```

```java
package com.imooc.order.fallback.itemservice;

import com.imooc.item.service.ItemCommentService;
import org.springframework.cloud.openfeign.FeignClient;

/**
 * <h1></h1>
 */
//@FeignClient(value = "foodie-item-service", fallback = ItemCommentsFallback.class)
@FeignClient(value = "foodie-item-service", fallbackFactory = ItemCommentsFallbackFactory.class)
public interface ItemCommentsFeignClient extends ItemCommentService {
}
```

item comments fall back factoryok 那同学们可以去测试一下，我这里直接把 order application 给它启动起来。那在启动 order application 的时候，我没有启动 item application 所以如果我们调用了 fall back controller 的这个方法，我们看一下这个查询订单评价的这个方法。那由于咱的商品中心没有启动起来，所以这个方法肯定会报出错误的对不对？我们只用去观察一下这个方法它的分 client 在报出错误之后，远程方法调用失败之后，它会不会导向 fall back factory 当中的这一个咱指定的降级流程里面来？那我们把 log 给它清空一下，然后转粘到 postman 里。好，我这里直接发起了一个方法调用，它的地址就是指向咱刚才看的 my comments 这个 controller 好，这里直接点击发送。


OK 等了片刻之后，我们看它这里返回了结果，这个返回的结果的 content 是谁呢？正在加载中来说明，她已经拐到了我们的降级流程当中来。 OK 那这里两种通过分 client 指定降级流程的配置方式就已经跟大家展示到这里了。那剩下的舞台就统统交给同学们了。咱这里这么多服务，同学们可以充分发挥自己的想象力，应用咱前面学到的各种降级手段，来给咱这里面这么多的微服务指定合理的降级措施。


我这里只是 demo 的一种非常简单的静默处理，那同学们可以合理运用咱前面学到的各种中间件，Redis elastic searchkafkarabbitmq 把它们尽量的揉在自己的降级流程当中。比方说我可以给不同品类的商品在 Redis 当中配置不同的默认主图。当我商品的主图加载失败之后，我这里可以去在降级流程中尝试从 Redis 当中获取这个商品品类它的默认主图，或者我们这里自行创建一个商品发布的接口。那这个商品发布就是用来添加新的商品，它是以同步阻塞的方式来添加商品，添加成功了之后返回一个成功。


那如果在创建商品的所有数据校验这里已经通过的情况下，它依然因为某个微服务的错误发生了异常情况，那我们可以把这个商品创建请求直接去塞到 rabbit MQ 那等待一段时间之后，从这个消息队列当中拿到消息，再重试这个商品创建过程。再比方说用户注册，那一段时间内，如果新用户注册非常多，导致接口超时，那我们可以返回一个静默降级，告诉大家现在注册人数正多，请稍后再试。好嘞，那这里咱 high streaks 的部分就玩的差不多了，剩下的部分就留给同学们课后通过作业来好好把玩了。那小伙伴们，我们这一章就到这里结束了，我们下一堂课程再见。


