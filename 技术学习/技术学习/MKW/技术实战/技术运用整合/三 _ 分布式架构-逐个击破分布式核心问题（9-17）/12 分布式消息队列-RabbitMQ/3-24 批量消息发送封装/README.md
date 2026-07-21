---
title: 3-24 批量消息发送封装
---

# 3-24 批量消息发送封装

[image](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/e3c90fed-c34f-414c-8160-700a9c6e5301/SCR-20240807-fili.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466R3SMUUIO%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T225316Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDRZ0ZkFrFd7DpzQLtRMK%2FQ7NDdFF3c4L4YznSUPuWFbgIhAO3IIDryVSvV5PH%2FOYgUqJg2PK3MqrudQxroCcu2ZpVuKogECMb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgzCn%2BWsqE9gC%2B%2FiqOkq3AMxfe2C3UuGmjtTK3c1UdsMQEdNTCqezDPep0QIeLOqtin1N%2BC5eK8oAAl8VPDpmJm87apFrn6lxOQB8o%2FSBoY4T4xX%2Ba4MDQQEQTTjO2s6dyT2afLm5x4CEkYMtui9CdhpsYIlM8tjtL2UvHg50cPz4jaJ9XkQMPnM%2F8l1Xpi%2FcMHvI1iPf%2BOD8FoGYVjTYlGwIJMU3ZNI3KkG5pgTQJdjBGErewl%2BKibNbjloDaE0tlNf8UsPTx2nRoxGG%2BognGqlIWis%2BcVj36BHR%2BIyIpTjab1%2FZJ6tbfsk573%2FTNk%2BDBiTpumI9JpI8NRzMPANyGFrg9Nf4n57Kk3CFfeR2zlLd8OJMcv7uE3JuFpZK5oYrmJewOtyCemQb8GHMAr%2FlmuexgOHAdMfCelVcSBAYIfTL12nKKIvmSmuTUGrtreXarGaVhzFYieHPh9yNucl0bfXJkFmejJSq%2BpQL13bqbEhV%2F0x9QnjWwRe6QWjIRrUdi0HoIhaVqRDOIhJNZNNc%2BtnPOmsCYLTsR4n9W8w6rw2W7oklTYr27BDdzWq0Pi1uwIJNlUo9dlIDl1OYH1oRwHbJCuJ0ZUxp81Bxy0x2vjLNBsnlTs9TNDwEPnkIcURPglUaFlt6ns3v%2FXtQTCVt%2F%2FSBjqkAYMghMkwjFcnkyzTdb30ETY8kha9Lg0PCxfEIjAEWLzY6f4af1w2cdDNFN%2B82B1A0NapJTwGs27qxUapVto1roCrdIfjQmoAHAjawvcsmW5kj7%2Bmp7c1ikzzKfEY3f4XLNezRbLhMxkGFUAMn%2F%2BUeexl6TiuW0s0yt4OfupuhlM8XYaQ6ktHHrDlL5S7swKBHwjwkn0DcrbKYboc%2BFGApS%2F9H2xm&X-Amz-Signature=1c64473040cb0277b98ad72bed2818f97d8d367e31127b20a316cb9334eb4ee5&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

[image](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/ab386ad4-0e57-4502-8d46-2109dd28b3d4/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466R3SMUUIO%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T225316Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDRZ0ZkFrFd7DpzQLtRMK%2FQ7NDdFF3c4L4YznSUPuWFbgIhAO3IIDryVSvV5PH%2FOYgUqJg2PK3MqrudQxroCcu2ZpVuKogECMb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgzCn%2BWsqE9gC%2B%2FiqOkq3AMxfe2C3UuGmjtTK3c1UdsMQEdNTCqezDPep0QIeLOqtin1N%2BC5eK8oAAl8VPDpmJm87apFrn6lxOQB8o%2FSBoY4T4xX%2Ba4MDQQEQTTjO2s6dyT2afLm5x4CEkYMtui9CdhpsYIlM8tjtL2UvHg50cPz4jaJ9XkQMPnM%2F8l1Xpi%2FcMHvI1iPf%2BOD8FoGYVjTYlGwIJMU3ZNI3KkG5pgTQJdjBGErewl%2BKibNbjloDaE0tlNf8UsPTx2nRoxGG%2BognGqlIWis%2BcVj36BHR%2BIyIpTjab1%2FZJ6tbfsk573%2FTNk%2BDBiTpumI9JpI8NRzMPANyGFrg9Nf4n57Kk3CFfeR2zlLd8OJMcv7uE3JuFpZK5oYrmJewOtyCemQb8GHMAr%2FlmuexgOHAdMfCelVcSBAYIfTL12nKKIvmSmuTUGrtreXarGaVhzFYieHPh9yNucl0bfXJkFmejJSq%2BpQL13bqbEhV%2F0x9QnjWwRe6QWjIRrUdi0HoIhaVqRDOIhJNZNNc%2BtnPOmsCYLTsR4n9W8w6rw2W7oklTYr27BDdzWq0Pi1uwIJNlUo9dlIDl1OYH1oRwHbJCuJ0ZUxp81Bxy0x2vjLNBsnlTs9TNDwEPnkIcURPglUaFlt6ns3v%2FXtQTCVt%2F%2FSBjqkAYMghMkwjFcnkyzTdb30ETY8kha9Lg0PCxfEIjAEWLzY6f4af1w2cdDNFN%2B82B1A0NapJTwGs27qxUapVto1roCrdIfjQmoAHAjawvcsmW5kj7%2Bmp7c1ikzzKfEY3f4XLNezRbLhMxkGFUAMn%2F%2BUeexl6TiuW0s0yt4OfupuhlM8XYaQ6ktHHrDlL5S7swKBHwjwkn0DcrbKYboc%2BFGApS%2F9H2xm&X-Amz-Signature=c6f2304f54f68ca1c3cbfc96f9d4b88745b92e98c06a4cbf29704cdf321da6ca&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

那这节课我们来把关于整个这个基础组件剩余的一些小部分内容，跟大家一起来继续封装一下，那接下来我们来看一看我们差什么了。首先我们从这个 API 的角度上来考虑一下， message producer 的话，其实给我提供了 3 个方法，一个是带 call back 的，就是说带一个回调函数的，还有一个是正常发消息的，其实我们之前一直做的事情就是发消息的，因为这是最关键的，对吧？它相当于发消息根据 message 的 type 去发不同类型的消息，是迅速消息还是 config 消息以及 relight 消息。


那还有一个就是批量发送对不对？批量发送和这个发送带 call back，我们先把批量发送去拷定，然后对于 call back 这块，我到时候给小伙伴提示，看小伙伴能不能自己去封装一下。好了，我们来看一看这个批量发送应该怎么去做。首先批量发送呢？我们都知道批量发送就是要发一批消息嘛，是不是怎么样发一批消息，那这一批消息我们缓存到哪里？这是一个问题。总之这边前端给我传来一批消息，我对这一批消息做一些处理，比如说我做这个 for each 操作，我做复印环，每一次都是一个 message 4，然后去对这些 message 做处理。那批量消息我认为如果你都是批量去发消息了，那这些批量消息我可以直接把这个 


message 的 type 直接定义成我们自己的，这个迅速消息就是我们的 10P day，OK，那所以说我第一步做法就是把这些 message type 我都去给它设置成什么呢？设置成这种迅速，设置完迅速之后我要干什么？因为 ready time q 本身是不支持批量发消息的，那小伙伴们如何去做到批量发？我们认为当前这次请求其实我们要保存到一个地方，保存到哪？其实在这里这一批消息应对于这个请求，我把它放到这个 thread local 里是最合适的。当我提交的时候，我把 thread local 里边的这个内容都取出来，然后在 for 循环或者是循环着去发出去，这种是最合适的。所以说在这里我们需要有一个类似于索爱local，相当于一个实体。


那在这里我们来简单封装一下，那我们来创建一个class，咱们叫做 message holder， message m e s s h e holder，对吧？ message holder，那有了这个 message holder，我们应该怎么去做呢？首先它这个 message holder 肯定也要做一个缓存，是不是它要存什么东西？它就存我们一条一条的？这个 message 就是我们的private，我们的 list 它是一个记录。然后我们比如说叫做 message 撕，等于 list 4 点弄一个releast，是不是进入一个release，搞定了之后，那这个变量就是用来我们做缓存的。


接下来我刚才说了，**我们肯定得需要一个什么呀？一个类似于 thread local 的方式去存储这个线程里边所有批量发的数据，所以说在这里边我们去加一个 sorry local 变量线程局部变量，所以 local 底层是怎么去实现的？这个其实是一个很简单的面试题，对吧？所以 local 你可以认为它是一个类似于哈希 map 的这个二级map。**


**为什么说二级map？其实在老师实际面试的时候，经常会问到类似于 Java 基础的内容，斯埃洛克怎么跟当前现场绑定的？其实这些问题都是一些很简单的问题，但是我会发现很多在面试的候选人，他总是回答的不是特别理想，答的不太好，那其实说白了还是对这个 Si local 没有深入的去理解，所以说对于 Sri local 这个东西，小伙伴们一定要好好的去回忆一下，好好的去复习一下，就这个 thread local 到底是一个什么东西？然后它有一个初始化的值，叫做 init less value 方法， override return，就是我们这个 smart look 对象装的不就是这个 message holder，直接 new 出来就可以了。**


好，有了它之后，我们这里面这个异常直接把它应该是安柴的，好，搞定，嗯，这应该是个数字啊，搞定。OK，我们接下来要做什么事情？其实不就是往这个索拉 local map 里边这个对象里面去扔一个一个的元素？那其实我们可以提供方法，比如说叫 public static wide，我们叫做add，往里装一个 message 是不是message？然后这个 message 直接放到 holder 里，是不是？那我们在这里 hold 这个变量没有去声明。


Letter, author get. message 4 点 m 是不是直接把这个 message 放里边？我说我怎么去取？你可以有一个并行的方法，可以做一个这个复合性的操作，反正这个取我是取 list 里边的这个map，那我们可以叫一个 clear 方法，可不可以？就是你在 clear 的时候我直接把数据取出来了，这个可以吗？没问题，是不是很简单，我们直接 list message，咱们叫 tea tap 吧，用一个临时变量去保存一下list， 4 点 new 一个release，然后从 holder 里进去把这个 list 取出来。

```java
package com.bfxy.rabbit.producer.broker;

import com.bfxy.rabbit.api.Message;
import com.google.common.collect.Lists;

import java.util.List;

/**
 * <h1> RABBIT 本身不支持批量消息的，把消息保存到 threadlocal 类似的容器，然后取出来</h1>
 */
public class MessageHolder {


    private List<Message> messages = Lists.newArrayList();

    /**
     * TheadLocal 类似于 hashmap 的二级 map
     */
    @SuppressWarnings({"rawtypes", "uncheched"})
    public static final ThreadLocal<MessageHolder>  holder = new ThreadLocal() {

        @Override
        protected Object initialValue() {
            return new MessageHolder();
        }
    };

    public static void add(Message message) {
        holder.get().messages.add(message);
    }

    public static List<Message> clear() {
        List<Message>  tmp = Lists.newArrayList(holder.get().messages);
        holder.remove();
        return tmp;
    }
}
```

是不是 holder 点get，就是取到 thread local，然后再取到 thread local 里边的那个message，撕好取出来之后 return 我们的template，对不对？这不就是相当于取出来剩下的事情就把它删除，比方说remove，把这个 key 删除，对不对？那这个方法小的这个缓存位就已经写完了，就是针对于 thread local 的，对吧？所谓 local 它到底是什么？是不是？在这里我看一下嘛？是不是有兴趣的话，你可以去读一读 thread local 里边其实有一个数据结构，就是我们的 thread local map surred local map，那它是在这里面定义的一个对象，它是一个 wiki reference 就是一个弱引用。为什么它是弱引用？在这里其实你可以找一找相关的一些资料。


此外的 local 跟我们的当前线程是什么关系？其实是一个引用关系。其实大家可以去先看一下这个thread，比如说我们来看一下thread， thread 里面有一个引用叫做 thread local 4，看见了有一个引用，然后还有一个 inheritable thread local 4， inheritable thread local 是 thread local 的一个子类，它能够实现比如说所爱 local 里边的这个数据可以去向下传递到它的子类里。像这些知识其实面试的时候考的这个几率特别的大，所以说我在这里还是希望小伙伴们一定要把这些基础的概念要好好的去掌握一下。


在这里我就不过多去说这个斯拉洛克了，那我们既然用它之后存储这个message，那我们应该怎么去做呢？这里边很简单，我们取到的每一个对象把它设置成这个迅速消息，然后紧接着我们就把它放到 thread local 里，是不是就可以了？OK，那我们直接就这么做，说 message holder 点 add 嘛，是不是就完了？接下来放到这里边我去调散的方法，我怎么去调？这里边不有一个broker，是不是直接去调它的send？ Messages. 我们怎么去做？它还是一个空实现的？没有去做任何的实现，它还是空的。看见了，我们只是实现了，比如说发可靠性的，发迅速的，真正的发消息。克尔还有什么send， confirm send，然后剩下的这个 message send 这个我们还没有真正的去实现它。那这位小伙伴们想一想应该怎么去实现呀？你不是有 thread local 吗？是不是我想取数据？那就太简单了。


第二，可利尔方法是不是就把我们所有的数据从当前线程中取到了？就是 message 4。等于它接下来你要做的事情就是发送呗，是不是你要做的事情就是for，循环着去发送一条条的消息， message 4 点 for 一尺，我们就把遍历出来的一个message，然后去做一个异步的提交，对不对？我刚才说了这些提交其实还是上面这个逻辑，但是如果说这个队列，你说你想换一个没问题，你自己再换一个也行。


我们之前有一个叫做什么呢？叫做 a single basking。那是不是我们有一个，我们再来一个？如果你说批量的消息想跟它区分开，为什么要区分开？就是发送的时候让它更好一些，叫做 message holder，那么性能更好一些。 message holder a，s，y，n，c，然后 s k 直接叫 q 好，搞定了，然后把它里边代码完完全全的开。 OK 过来，就是说我们再换一个队列。所以说这个东西你可以用一个工厂模式去做，也可以搞定其他的有包异常的logger。好，我们加一个 s l f o g 注解就可以了。


好了，这个来了，那我们直接用它叫做 message holder Sup，那把我们之前的逻辑完全的粘过来就好了，就是他一条条的去发消息，只不过换了一个人。换了谁呢？换了我们的这个 message holder 了，叫做 message holder，对吧？点 summit 好搞定。


就这个逻辑，其实就是换了一个人帮我批量去发，批量发的内容也是一致的，跟我所有的这个逻辑都是保持一致的，然后都是一条条发。那其实真正它发送的时候它并不是批量的发，它也是 for 循环着这个索拉 local 麦克里面所有的这个message，这个变量里的message，然后一条一条的去后循环提交到异步队列去发的。OK，那我希望小伙伴们明白，那这里边我打个日志吧，这叫做 send message 4 改一下方法。OK，那这个也就是我们对于批量消息怎么去封装做一个简单的讲解。好，感谢小伙伴们。



