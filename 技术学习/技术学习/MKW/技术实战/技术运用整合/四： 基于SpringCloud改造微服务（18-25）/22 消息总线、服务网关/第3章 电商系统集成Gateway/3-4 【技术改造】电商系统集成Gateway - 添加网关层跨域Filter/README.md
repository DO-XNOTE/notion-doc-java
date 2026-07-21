---
title: 3-4 【技术改造】电商系统集成Gateway - 添加网关层跨域Filter
---

# 3-4 【技术改造】电商系统集成Gateway - 添加网关层跨域Filter

[image](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/94e8ae5a-8521-4db6-9a4e-9cb8fea8b0f4/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666JASJKK3%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T225748Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDVn1O%2FhDxuxaaeEfw7RCkTZrOc8q%2FEvuuIEwUisoqnWAIhAObUo3CIocS2R7OK%2B5dnLA8W9thCGzqPRi1sip58fAxnKogECMb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1Igx%2BOXAgj7LiokIdJCEq3AOYqe4VRssE69usbJcXlqvBMTuWpfNszeHn8MU4B4A5UX7rDDb3I7pgP3nw1YH6p028aemjmQDg0LFGK%2FeGixgQofQ3EOpSocRPhsNp7vt33K1R1klyaunQTvOXQGKPucoAqZs9RjpkHL%2Bp1rbHsW%2FYDtfCViqTLq%2FE7noSBROfvZC7gZSt2XPTcMkIyCBw%2BgVMvha8Z4LqlrFApn2OVgHyyj3%2FIJJfbpUBo2GE270I7JKi3kbgjE0A0xIE%2BsRC7MnFnyvig60kVS5pwIzBLmjDGZwzDRovI8Hmvr83GWIfjo9B1TZsowHDBxwqvMS%2B7tsZQR%2BxQI8sfN1UODTZu7Ko1S5ZtVFv8KcOZv1r3rweNHcdGq7xKVecUjr03RRXTZsB%2B%2BjhoouhC9%2Fc28WxWVEnvaF0VLeTRffxNMdPrJ5ReT0qOhMNnvhlRdUCSbz4Mi%2Fx%2FuxZWOmkxHjnpKjpbo%2F%2BL6vcIvDfN3nib8uRbZrxV%2BIUXw%2B3WV3TtBZqukCCDDqoiAC94%2FqoyT3MdCbvChQS%2FKSQm2XT%2FKZFumjSl9zy4l7g0k8DznLVLKR7%2BDKLLYMcjfljaoWm6vpPEdQ59Yx72xfs%2BN%2FQrfHhP67l7RLvcuL7qhC08Vz5JfEXIjDWuv%2FSBjqkAQRVuRbFSAeOUUGeVIBntYMjSLQO4%2B%2BJDsMVkbhm%2Bg2epda59%2F88duwoel1ir9FRg0qJhiC2CqnKuLSZNRQ3fBSStxmMaMNSdK2asPvnuWIOiW%2FYursREARwyisqLYOSbpsNAlqgKQ57zL2aNAvdGAXHVXXsrUJM9KfmRB16RrXu3u5cyPdjgGbziJqhA8FDECUer%2F0ZuhXM28PNpOp%2B%2F202MVH7&X-Amz-Signature=026ca62e419bcd45de914888c882aa96f737ca5cfaded63b812ac0de09d755e5&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

[image](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/451d19ef-784f-44ac-a4b4-cc006f0567be/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666JASJKK3%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T225748Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDVn1O%2FhDxuxaaeEfw7RCkTZrOc8q%2FEvuuIEwUisoqnWAIhAObUo3CIocS2R7OK%2B5dnLA8W9thCGzqPRi1sip58fAxnKogECMb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1Igx%2BOXAgj7LiokIdJCEq3AOYqe4VRssE69usbJcXlqvBMTuWpfNszeHn8MU4B4A5UX7rDDb3I7pgP3nw1YH6p028aemjmQDg0LFGK%2FeGixgQofQ3EOpSocRPhsNp7vt33K1R1klyaunQTvOXQGKPucoAqZs9RjpkHL%2Bp1rbHsW%2FYDtfCViqTLq%2FE7noSBROfvZC7gZSt2XPTcMkIyCBw%2BgVMvha8Z4LqlrFApn2OVgHyyj3%2FIJJfbpUBo2GE270I7JKi3kbgjE0A0xIE%2BsRC7MnFnyvig60kVS5pwIzBLmjDGZwzDRovI8Hmvr83GWIfjo9B1TZsowHDBxwqvMS%2B7tsZQR%2BxQI8sfN1UODTZu7Ko1S5ZtVFv8KcOZv1r3rweNHcdGq7xKVecUjr03RRXTZsB%2B%2BjhoouhC9%2Fc28WxWVEnvaF0VLeTRffxNMdPrJ5ReT0qOhMNnvhlRdUCSbz4Mi%2Fx%2FuxZWOmkxHjnpKjpbo%2F%2BL6vcIvDfN3nib8uRbZrxV%2BIUXw%2B3WV3TtBZqukCCDDqoiAC94%2FqoyT3MdCbvChQS%2FKSQm2XT%2FKZFumjSl9zy4l7g0k8DznLVLKR7%2BDKLLYMcjfljaoWm6vpPEdQ59Yx72xfs%2BN%2FQrfHhP67l7RLvcuL7qhC08Vz5JfEXIjDWuv%2FSBjqkAQRVuRbFSAeOUUGeVIBntYMjSLQO4%2B%2BJDsMVkbhm%2Bg2epda59%2F88duwoel1ir9FRg0qJhiC2CqnKuLSZNRQ3fBSStxmMaMNSdK2asPvnuWIOiW%2FYursREARwyisqLYOSbpsNAlqgKQ57zL2aNAvdGAXHVXXsrUJM9KfmRB16RrXu3u5cyPdjgGbziJqhA8FDECUer%2F0ZuhXM28PNpOp%2B%2F202MVH7&X-Amz-Signature=180b6fb9aed60ea4491244488a6c983853c7b2e7c072493cecfb400514d0e76f&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

hello 慕课网的各位同学们，大家好，我是姚半仙，咱这一节当中给网关层加一个小 buff 那它是什么 buff 呢？就是跨域支持，咱要在网关层这里添加上跨域请求的知识。那么在添加之前，我们要先去翻一翻旧账。那这个旧账就是咱的 common 这一个文件夹下面有一个 foodie cloud web components 好，我们打开它去这里面去找一找，这个 config 文件夹下有一个 CORS config 那这一个类大家想必都非常熟悉了，它是咱之前配置的一个跨域请求的配置项。那我这里要跟它怎么算旧账呢？我们 ctrl 加 A 打一个注释好勒把它全部注释掉。


为什么？因为咱的这个客户端的每一个微服务都不再需要去做专门的跨域支持了，我们把这个跨域在整个网关层这一面给它搞定。那咱这里配置的跨域和咱网关层配置的跨域有一些冲突。所以我们把这个微服务里的所有跨域全给它关掉，只在网关层这里来处理。 OK 那改完当前这个跨域，我们还有一个地方需要也改一下，就是这个 cookie you choose 好，我们看一下这里，它首先在保存 cookie 的时候会调用一个 get domain name 方法拿到一个 domain name 那这个 domain 有可能是什么？有可能是 3w.foodie 之类这种 URL 也可能是什么呢？也可能是一个 IP 地址，幺九二点幺六八等等这个 IP 地址。


那如果我们在本地使用 local host 这种形式访问的话，为了防止咱前面浏览器的域名和最终经过网关转发到达咱后台微服务的这个 domain name 有不一致的情况。我们在本地测试的时候，可以把它改成什么呢？改成一个 local host 好，我们这里给他动一个手脚，把这个 domain name 直接就改成 local host 好了，那我们这里再加一个 fix me 提示大家怎么样要在上线之前改回来，并且这种情况下仅限在 local host 访问。那这里改好之后，我们接下来就继续回到前面的这个跨域的配置当中。


咱这里还有几个跨域的配置需要在网关层这里落地。那同学们知道在网关层处理跨域有很多种不同的方式，我们可以给它配置一个 filter 这个也是大家最常见的一种方式。那不过我们在 gateway 里有一种更加优雅的方式是什么呢？一行代码都不用写，我们通过配置的方式，咱 gateway 这里对跨域有天然的支持。


怎么来说？我们打开 gateway 这里的 application.yaml 那我们在这个文件夹里动一点手脚，怎么来动我们收集小桌板，找到这个 gateway 那在这个配置项下，我们另起一行，给它打上一个节点叫 global cos 这里就是全局跨域的配置了。那接下来我要配置另外一个节点叫 cos configurations 在这下面我们要配置各个不同的路径，比如说我这里配置的匹配路径是 all in 全部路径全都给他怼上去。


那在这个路径下面，我第一个要配置的是叫 all of all of 谁 origins 它是什么意思啊？那这个节点属性是指什么？是指我们要把返回的资源给他共享出去。那共享给谁呢？共享给请求来源。好，那这里我可以通过这样的斜杠一个杠配置多个属性，咱来看一下之前咱注释掉的这里，咱把它给 copy 过来，全都给它 copy 过来。那咱把它前面的这一串字符，咱就给它替换一下，替换成一个横杠。好我们全部替换，然后把这个缩进调整好，那最后的这个小尾巴也要给它去掉，那这里我们就配置好了。

[image](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/cd66524b-18ae-4e03-8fa8-0da8ec6b147d/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666JASJKK3%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T225748Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDVn1O%2FhDxuxaaeEfw7RCkTZrOc8q%2FEvuuIEwUisoqnWAIhAObUo3CIocS2R7OK%2B5dnLA8W9thCGzqPRi1sip58fAxnKogECMb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1Igx%2BOXAgj7LiokIdJCEq3AOYqe4VRssE69usbJcXlqvBMTuWpfNszeHn8MU4B4A5UX7rDDb3I7pgP3nw1YH6p028aemjmQDg0LFGK%2FeGixgQofQ3EOpSocRPhsNp7vt33K1R1klyaunQTvOXQGKPucoAqZs9RjpkHL%2Bp1rbHsW%2FYDtfCViqTLq%2FE7noSBROfvZC7gZSt2XPTcMkIyCBw%2BgVMvha8Z4LqlrFApn2OVgHyyj3%2FIJJfbpUBo2GE270I7JKi3kbgjE0A0xIE%2BsRC7MnFnyvig60kVS5pwIzBLmjDGZwzDRovI8Hmvr83GWIfjo9B1TZsowHDBxwqvMS%2B7tsZQR%2BxQI8sfN1UODTZu7Ko1S5ZtVFv8KcOZv1r3rweNHcdGq7xKVecUjr03RRXTZsB%2B%2BjhoouhC9%2Fc28WxWVEnvaF0VLeTRffxNMdPrJ5ReT0qOhMNnvhlRdUCSbz4Mi%2Fx%2FuxZWOmkxHjnpKjpbo%2F%2BL6vcIvDfN3nib8uRbZrxV%2BIUXw%2B3WV3TtBZqukCCDDqoiAC94%2FqoyT3MdCbvChQS%2FKSQm2XT%2FKZFumjSl9zy4l7g0k8DznLVLKR7%2BDKLLYMcjfljaoWm6vpPEdQ59Yx72xfs%2BN%2FQrfHhP67l7RLvcuL7qhC08Vz5JfEXIjDWuv%2FSBjqkAQRVuRbFSAeOUUGeVIBntYMjSLQO4%2B%2BJDsMVkbhm%2Bg2epda59%2F88duwoel1ir9FRg0qJhiC2CqnKuLSZNRQ3fBSStxmMaMNSdK2asPvnuWIOiW%2FYursREARwyisqLYOSbpsNAlqgKQ57zL2aNAvdGAXHVXXsrUJM9KfmRB16RrXu3u5cyPdjgGbziJqhA8FDECUer%2F0ZuhXM28PNpOp%2B%2F202MVH7&X-Amz-Signature=2d15d4b2747a23b08c50bb869369e5c619f93f5cb7b106c9134d412e1e3b380a&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

那咱接下来看第二个属性是什么，它叫做 all up credentials 那它的值就是 true 那它的含义，是让大家就是允许携带一些认证信息，比如谁，比如 cookies 对吧，还有 authorization 那比如像这之类的认证信息是否可以暴露给前端的页面？好勒。


那接下来的属性，我们配置这样一个叫熬了谁熬了 headers 那这个顾名思义，就是我可以允许接收的那些 header 那这里我给它配置了一个星是什么意思啊？所有 header 来者不拒，统统都给你接收掉。那往后配置下一个属性是 all of the 后面跟 methods 那咱这个 all of methods ，其实咱也可以通过这种形式配置一些指定的 HD DP matter 比如 options 再比如像 get 不过我这里也同样的使用一个通配符，把所有 master 全给它包含进去。


接下来的属性我再给他配置一个 expose headers 好嘞，那这里我也给他一个通配符，那这个属性和前面的 all of the headers 有什么不同啊？咱顾名思义 all of the headers 是可以接收的header 。那 expose headers 就自然而然的是可以暴露给前端用户给它返回回去的headers 。
最后一个属性，给大家设置一个 max H 单位是秒，我这里给它设置一个 600 毫秒 600 秒。好了，也就是 10 分钟。它表示什么含义，它表示你的 options 请求，那可以在浏览器缓存多长时间？那到这里，咱的快欲配置就已经完成了，那是不是非常简单就搞定了。

```java
spring:
  application:
    name: platform-gateway
  redis:
    host: 172.16.136.222
    port: 6379
    database: 10
  main:
    allow-bean-definition-overriding: true
  cloud:
    gateway:
      globalcors:
        '[/**]':
          # 返回的资源共享给请求的来源
          allowed-origins:
          - "http://localhost:8080"
          - "http://localhost:8080"
          - "http://172.16.136.223:8080"
          - "http://172.16.136.130:8080"
          allowed-credentials: true
          allowed-headers: "*"
          allowed-methods: "*"
          expose-headers: "*"
          # 表示Options请求可以在浏览器缓存的时间
          max-age: 600


#          cors.addAllowedOrigin("http://localhost:8080");
#          cors.addAllowedOrigin("http://localhost:8080");
#          cors.addAllowedOrigin("http://172.16.136.223:8080"); // foodie-shop    http://172.16.136.130:8080/foodie-shop
#          cors.addAllowedOrigin("http://172.16.136.130:8080"); // foodie-center, 如配置域名这里还需要一个  http://172.16.136.130:8080/foodie-center

      locator:
        enabled: false
        lower-case-service-id: true
#        routes:   在代码中去配置路由吧
```


其实咱 gateway 这里不光跨域配置还有很多其他的配置项。那同学们可以去研究代码，来找一下这里面隐藏的一些机关，咱们没有讲到的一些配置项去研究。那这里既然提到了跨域，我就再多说两句同学们知道这个跨域是谁的特殊技能吗？它其实是浏览器自带的一个保护技能天赋技能。其实我们在启动浏览器的时候，可以通过加入一些特殊的参数来关闭浏览器的这个跨域特性。这样一来，即使我们向不同的域发送请求，那么浏览器也不会先发送一个 options 预检指令到指定的服务器了。那具体怎么做？加哪些启动参数才能禁止浏览器的跨域检测呢？同学们可以去百度谷歌一下。



那这一节的内容短小精悍，咱到这里就结束了。在结束之前，老师再叮嘱大家一句，别忘了，咱把前面 food cloud web components 里面的这个跨域配置，它是加在每个微服务上面的，我们可以把它注释掉，不然的话你这里打开和前面咱的这个配置项有一些冲突，那会导致你的跨域请求虽然发到了后台服务，但是却不能被后台服务正确的响应。 OK 同学们，那这一节就到这里结束了。那我们在下一个小节里，打算把用户登录检测的部分给它集成到我们的 GTV 平台当中。同学们，那我们下一小节再见。





