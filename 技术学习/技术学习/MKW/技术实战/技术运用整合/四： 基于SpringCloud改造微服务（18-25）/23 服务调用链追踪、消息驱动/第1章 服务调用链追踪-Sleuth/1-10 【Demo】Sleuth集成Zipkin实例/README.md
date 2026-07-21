---
title: 1-10 【Demo】Sleuth集成Zipkin实例
---

# 1-10 【Demo】Sleuth集成Zipkin实例

[image](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/2474dd6d-87a7-4bf4-911d-9f0bde8a73cf/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46622BYEXNX%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T225800Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCFRr6Zpli3OhdqIRC9EtMXMQSTe81F3OQTPLv%2FoLhaNgIgfRyfUdaPYp3p2oe51OOc%2BFOilOS1eVWusEAkfO7DfH4qiAQIxv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDJgp5rLPF5LQdUCFgyrcA2kZKVx3pNMDpGoig5MhGSHF00VS2ZaRHYtwufAPkx7MFHWTXch27d5qeQh2W850t8VczHTTN%2B9AuL%2FdzU3tVER5fBdKaC17UgKYBMTY%2FJO3iicBYjbItMm4SoafiNhjPQXEAZ3rtdZowQ2gMQ6mbjfPrd40CARCPb66HRNyFRp36S704VFD1RzQcj6w72p0LS2b5%2BAlSR5z2hZtC8hf3s5LRnZjG2FvBTVGw1MOC83%2B%2BBVlx5KxFbsgwpnQ2mYpaDQpNz%2B5CK2Ttb4Gr205dbuvoWxjAhlNdltBuCnf9A%2F0eQ56q1LraQoeG3Tm17YN94cj8D%2FzQRdf%2FoWSca33dELAeOLhnN%2FTFQB5mA8Gz8W7Ea6n1eKlGA8VAkLyaTfAxz9QtlhgpfoPKKIN4bvZR0h0KXS%2FEbO0CzTB3lpnDZ9ibIwJUIitGMqcc2ksUr9ylFETMeZ8mpl%2BW%2FM%2BGQ%2FWAB7Pio%2B1Hb0gX5KbAwiWvkfKVl9yaG%2BtHmRipbWvUzs%2F%2BvkuBNbJvZKknlcCnKy0eG3vnayge2fM2BYPtVLcafg5kQ47ilEgBThKBS32JAuwxb6tmFOZhy%2Fw5N0hNa%2BFmhpVG3QBqPzdpxn%2FhErlXHTMOxPm%2BdeAbxxI6R73MMe6%2F9IGOqUBT7ZrSDFyNZNTe82oN1oTCYzq9G3wGVsQjnT5mkgwGpjj9Omf3hbOF9klz3YcxzHtOdb2%2F4w4Kwc0hm6Q7cqLJYXftqyea7p3UsGnajSMTTKPmKgAGOq%2FJ59msNgHuZDCT1TiFrQSqnlDcStdzEk5bSGDpEqLRl4ZUSLxyr0gIUs7Zry8NA2%2Bs3oJmI7Nv%2FDLGH5nHy0aV%2FVN99cim3ecYS4%2F%2BxHd&X-Amz-Signature=64d066dbfb8f8132e484cbc437cdb0968aedb5f32274eecdd6faedb152281fe4&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

[image](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/61d84042-2a89-4b1c-810a-c721bfa2ef8e/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46622BYEXNX%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T225800Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCFRr6Zpli3OhdqIRC9EtMXMQSTe81F3OQTPLv%2FoLhaNgIgfRyfUdaPYp3p2oe51OOc%2BFOilOS1eVWusEAkfO7DfH4qiAQIxv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDJgp5rLPF5LQdUCFgyrcA2kZKVx3pNMDpGoig5MhGSHF00VS2ZaRHYtwufAPkx7MFHWTXch27d5qeQh2W850t8VczHTTN%2B9AuL%2FdzU3tVER5fBdKaC17UgKYBMTY%2FJO3iicBYjbItMm4SoafiNhjPQXEAZ3rtdZowQ2gMQ6mbjfPrd40CARCPb66HRNyFRp36S704VFD1RzQcj6w72p0LS2b5%2BAlSR5z2hZtC8hf3s5LRnZjG2FvBTVGw1MOC83%2B%2BBVlx5KxFbsgwpnQ2mYpaDQpNz%2B5CK2Ttb4Gr205dbuvoWxjAhlNdltBuCnf9A%2F0eQ56q1LraQoeG3Tm17YN94cj8D%2FzQRdf%2FoWSca33dELAeOLhnN%2FTFQB5mA8Gz8W7Ea6n1eKlGA8VAkLyaTfAxz9QtlhgpfoPKKIN4bvZR0h0KXS%2FEbO0CzTB3lpnDZ9ibIwJUIitGMqcc2ksUr9ylFETMeZ8mpl%2BW%2FM%2BGQ%2FWAB7Pio%2B1Hb0gX5KbAwiWvkfKVl9yaG%2BtHmRipbWvUzs%2F%2BvkuBNbJvZKknlcCnKy0eG3vnayge2fM2BYPtVLcafg5kQ47ilEgBThKBS32JAuwxb6tmFOZhy%2Fw5N0hNa%2BFmhpVG3QBqPzdpxn%2FhErlXHTMOxPm%2BdeAbxxI6R73MMe6%2F9IGOqUBT7ZrSDFyNZNTe82oN1oTCYzq9G3wGVsQjnT5mkgwGpjj9Omf3hbOF9klz3YcxzHtOdb2%2F4w4Kwc0hm6Q7cqLJYXftqyea7p3UsGnajSMTTKPmKgAGOq%2FJ59msNgHuZDCT1TiFrQSqnlDcStdzEk5bSGDpEqLRl4ZUSLxyr0gIUs7Zry8NA2%2Bs3oJmI7Nv%2FDLGH5nHy0aV%2FVN99cim3ecYS4%2F%2BxHd&X-Amz-Signature=627bd648a61ca0fad20de34d6f9338c3f42ff6e057d7b973ff1307266089dd3f&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

[image](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/7bb3e7e9-2b9b-49d1-a087-a8ff51c23b46/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46622BYEXNX%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T225800Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCFRr6Zpli3OhdqIRC9EtMXMQSTe81F3OQTPLv%2FoLhaNgIgfRyfUdaPYp3p2oe51OOc%2BFOilOS1eVWusEAkfO7DfH4qiAQIxv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDJgp5rLPF5LQdUCFgyrcA2kZKVx3pNMDpGoig5MhGSHF00VS2ZaRHYtwufAPkx7MFHWTXch27d5qeQh2W850t8VczHTTN%2B9AuL%2FdzU3tVER5fBdKaC17UgKYBMTY%2FJO3iicBYjbItMm4SoafiNhjPQXEAZ3rtdZowQ2gMQ6mbjfPrd40CARCPb66HRNyFRp36S704VFD1RzQcj6w72p0LS2b5%2BAlSR5z2hZtC8hf3s5LRnZjG2FvBTVGw1MOC83%2B%2BBVlx5KxFbsgwpnQ2mYpaDQpNz%2B5CK2Ttb4Gr205dbuvoWxjAhlNdltBuCnf9A%2F0eQ56q1LraQoeG3Tm17YN94cj8D%2FzQRdf%2FoWSca33dELAeOLhnN%2FTFQB5mA8Gz8W7Ea6n1eKlGA8VAkLyaTfAxz9QtlhgpfoPKKIN4bvZR0h0KXS%2FEbO0CzTB3lpnDZ9ibIwJUIitGMqcc2ksUr9ylFETMeZ8mpl%2BW%2FM%2BGQ%2FWAB7Pio%2B1Hb0gX5KbAwiWvkfKVl9yaG%2BtHmRipbWvUzs%2F%2BvkuBNbJvZKknlcCnKy0eG3vnayge2fM2BYPtVLcafg5kQ47ilEgBThKBS32JAuwxb6tmFOZhy%2Fw5N0hNa%2BFmhpVG3QBqPzdpxn%2FhErlXHTMOxPm%2BdeAbxxI6R73MMe6%2F9IGOqUBT7ZrSDFyNZNTe82oN1oTCYzq9G3wGVsQjnT5mkgwGpjj9Omf3hbOF9klz3YcxzHtOdb2%2F4w4Kwc0hm6Q7cqLJYXftqyea7p3UsGnajSMTTKPmKgAGOq%2FJ59msNgHuZDCT1TiFrQSqnlDcStdzEk5bSGDpEqLRl4ZUSLxyr0gIUs7Zry8NA2%2Bs3oJmI7Nv%2FDLGH5nHy0aV%2FVN99cim3ecYS4%2F%2BxHd&X-Amz-Signature=9d0e451dd7854cca315bf2898101cfad414f7f989767c4e0bcdecb58c79cbdbb&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

hello 慕课网的各位同学们，大家好，咱中场休息时间已经过了，现在来到了下半场，我们继续来看在下半场当中咱要如何跟 zip king 做集成。这一小节，咱主要包含两个部分的内容。第一个部分我们将 zip king 集成到 trace A 和 trace B 两个项目当中，让咱的这两个项目可以把自己的 log 信息推送给 zipkin 接下来咱就可以从 zipkin 的 dashboard 里面搜索调用链路的时间维度的数据。

[image](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/86045423-0d76-4949-b1ae-b5226d9a194a/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46622BYEXNX%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T225800Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCFRr6Zpli3OhdqIRC9EtMXMQSTe81F3OQTPLv%2FoLhaNgIgfRyfUdaPYp3p2oe51OOc%2BFOilOS1eVWusEAkfO7DfH4qiAQIxv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDJgp5rLPF5LQdUCFgyrcA2kZKVx3pNMDpGoig5MhGSHF00VS2ZaRHYtwufAPkx7MFHWTXch27d5qeQh2W850t8VczHTTN%2B9AuL%2FdzU3tVER5fBdKaC17UgKYBMTY%2FJO3iicBYjbItMm4SoafiNhjPQXEAZ3rtdZowQ2gMQ6mbjfPrd40CARCPb66HRNyFRp36S704VFD1RzQcj6w72p0LS2b5%2BAlSR5z2hZtC8hf3s5LRnZjG2FvBTVGw1MOC83%2B%2BBVlx5KxFbsgwpnQ2mYpaDQpNz%2B5CK2Ttb4Gr205dbuvoWxjAhlNdltBuCnf9A%2F0eQ56q1LraQoeG3Tm17YN94cj8D%2FzQRdf%2FoWSca33dELAeOLhnN%2FTFQB5mA8Gz8W7Ea6n1eKlGA8VAkLyaTfAxz9QtlhgpfoPKKIN4bvZR0h0KXS%2FEbO0CzTB3lpnDZ9ibIwJUIitGMqcc2ksUr9ylFETMeZ8mpl%2BW%2FM%2BGQ%2FWAB7Pio%2B1Hb0gX5KbAwiWvkfKVl9yaG%2BtHmRipbWvUzs%2F%2BvkuBNbJvZKknlcCnKy0eG3vnayge2fM2BYPtVLcafg5kQ47ilEgBThKBS32JAuwxb6tmFOZhy%2Fw5N0hNa%2BFmhpVG3QBqPzdpxn%2FhErlXHTMOxPm%2BdeAbxxI6R73MMe6%2F9IGOqUBT7ZrSDFyNZNTe82oN1oTCYzq9G3wGVsQjnT5mkgwGpjj9Omf3hbOF9klz3YcxzHtOdb2%2F4w4Kwc0hm6Q7cqLJYXftqyea7p3UsGnajSMTTKPmKgAGOq%2FJ59msNgHuZDCT1TiFrQSqnlDcStdzEk5bSGDpEqLRl4ZUSLxyr0gIUs7Zry8NA2%2Bs3oJmI7Nv%2FDLGH5nHy0aV%2FVN99cim3ecYS4%2F%2BxHd&X-Amz-Signature=7c4317c30f124fb40addb0aa7eb6a1d3a18a17424d788d565a8a3cf57b38af41&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

这里为什么咱说它是时间维度的数据，而不是搜索具体的 log 内容呢？这个就要说到 **zipkin 的使用场景了，它更多的是分析调用链上下游的关系**，**以及在一整条调用链路中每个阶段它的时间花费以及它的先后顺序。所**以它并不是一个专业的 log 搜索工具，而是更像一个分析工具。我们在接下来的小节里会跟大家介绍一个专门用于搜索 log 内容的工具，那就是 elk 了。所以你看 sleuth 的好兄弟们真多，那咱先把这个 zip king 好兄弟先给搞定。同学们准备好的话跟我一起到 italy jelly 我们开工了编程使我快乐。


996 是我的福报，咱现在开始来正儿八经集成 zipkin 了。 OK 我们在集成以前先要把 zipking 的 dependency 给它加进来，我们先从 soluth trace B 来加起。 OK 这里添加一个新的 dependency 咱先给它标注一下，这是 for zip king 的。 OK 好，他的 group ID 是 org spring framework then cloud 它的 artifact 是 spring gun cloud gun starter 然后后面是 zip king 好的，看这一列队形多整齐，


```java
<dependencies>
        <dependency>
            <groupId>org.springframework.cloud</groupId>
            <artifactId>spring-cloud-starter-netflix-eureka-client</artifactId>
        </dependency>

        <dependency>
            <groupId>org.springframework.boot</groupId>
            <artifactId>spring-boot-starter-web</artifactId>
        </dependency>

        <dependency>
            <groupId>org.springframework.boot</groupId>
            <artifactId>spring-boot-starter-actuator</artifactId>
        </dependency>



        <dependency>
            <groupId>org.springframework.cloud</groupId>
            <artifactId>spring-cloud-starter-sleuth</artifactId>
        </dependency>

        <!-- ZipKin -->
        <dependency>
            <groupId>org.springframework.cloud</groupId>
            <artifactId>spring-cloud-starter-zipkin</artifactId>
        </dependency>


    </dependencies>
```


都是 spring cloud starter 开头的。咱把这个 dependency 给它复制一下，然后 copy 到 solution Tracy 当中。好嘞， dependency 加上了以后，咱接下来要去修改，在配置文件中添加一个 zip king 的属性。这样的话咱的 trace A 和 trace B 就能够把自己的 log 信息推送给 zip king 了。


OK 我们打开 application.properties 找个空地。摆开架室，多打几号。

这里给这边添加一个注释 zipking 的地址。这个 zipkin 的地址是怎么指定的呢？我们来看它是 spring.zipkin 然后 base URL 中间是有个横杠 base URL OK 然后它的地址就是 HTTP local host 咱的端口号是62,100。同学们，像这种配置尽量都不要使用 IP 来配置，都使用域名或者 DNS 的方式来配置。我们暂时先用 logo host ，等后面到了容器化的时候还需要做一些改动。咱配置完 trace B ，再把这一行配置给它 copy 到 trace A 里面，位置同样的地方 copy 一下。其实这个采样率跟这个 zipkin 是一对好搭档，待会儿咱就能看到当你配置了 zipking 以后，这个采样率就会自然而然生效了。假如咱没有zipking ，即便你指定了采样率是100%，那么 log 中打印出了采样标记依然会是 false 也就是说没有被采样。那咱把所有的配置都搞定了以后，就可以把应用都启动起来看一看效果了。

```java
spring.application.name=sleuth-traceB
server.port=62001

eureka.client.service-url.defaultZone=http://localhost:20000/eureka/

logging.file=${spring.application.name}.log

# zipkin的地址
spring.zipkin.base-url=http://localhost:62100
# 采样率
spring.sleuth.sampler.probability=1

info.app.name=sleuth-traceB
info.app.description=test


management.security.enabled=false
management.endpoint.health.show-details=always
management.endpoints.web.exposure.include=*
```


OK 我们在前面的上半场中已经把 zip king 启动起来了。那接下来把友瑞卡启动起来。在友瑞卡启动的过程中，我们要把 server 的 trace A 和 trace B 两个服务通通都给它启动起来。先从 trace B 开始启动。因为 trace B 没有其他的依赖，而 trace A 是依赖于 trace B 的这个服务，发现有个先后顺序。好把 trace B 启动的同时，咱到 trace A 里面把 QC 也给跑起来，好启动，看到 spring 成功一半。 OK 那咱接下来就去 postman 里发起一个真实的调用，咱先往 trace B 里发起一个调用，再往 trace A 里面发一个调用。这样的话 trace A 只会被调一次。但是 trace B 因为有一个 request 是来自于 trace A 的，所以会被调用两次。咱来看看这里面有什么不同。好，我们来到 postman 里，先给 trace B 来一发走。你 okay 那么回来 log 看一下， trace B 的 log 已经打出来了，刚才咱的调用是在这一个。


OK 同学们看它后面的这个标记位采样标记位已经变成 true 了。对不对？之前咱们配置 zip king 的时候，即使采样率是100%，也是英雄无用武之地，咱们配置好了 zip king 这个值立马变成了 trueok 那接下来咱来再调用一下 trace A 去 C 的端口是62,000，好钓一把。


OK 那咱再回来看一下，这个 traca 也已经调用成功了，这个采样标记也已经变成了 true 我们接下来到 Chrome 里面打开 zip king 的 dashboard 看一下搜索界面是如何展现这些数据的。走好嘞，接下来咱可以跟大家讲这个页面是怎么回事了，我们把页面稍微放大一点，看这里有很多的搜索框，假设咱什么都不选，直接默认搜索。啪。这里看到有 123455 个搜索结果出来了，那这些都是怎么回事呢？我们不妨在这边做一个过滤。


首先咱看 service name 我们把下拉框点出来，它这里列出了 solution trace A 和 solution trace B 那这就是我们注册到友瑞卡注册中心的服务我们这里可以选择 trace A 或者 trace B 来进行更细致的搜索。从这下面的搜索结果当中可以看到有很多次 trace B 的采样。然后后面这里这一行字是它的时间。那我们看到每一个采样它都有两行是什么意思啊？我把屏幕放大一点。第一行是这个请求花费的总时间，后面跟着 span 的个数。那同学们再看。第二行显示 slow trace b78% 是什么意思啊？就是说你的 slow trace B 它占了总采样时间 78% 的时间花费。那剩下 22% 是谁？

[image](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/036fd34b-8de7-4776-8c07-67f0704bcd27/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46622BYEXNX%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T225800Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCFRr6Zpli3OhdqIRC9EtMXMQSTe81F3OQTPLv%2FoLhaNgIgfRyfUdaPYp3p2oe51OOc%2BFOilOS1eVWusEAkfO7DfH4qiAQIxv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDJgp5rLPF5LQdUCFgyrcA2kZKVx3pNMDpGoig5MhGSHF00VS2ZaRHYtwufAPkx7MFHWTXch27d5qeQh2W850t8VczHTTN%2B9AuL%2FdzU3tVER5fBdKaC17UgKYBMTY%2FJO3iicBYjbItMm4SoafiNhjPQXEAZ3rtdZowQ2gMQ6mbjfPrd40CARCPb66HRNyFRp36S704VFD1RzQcj6w72p0LS2b5%2BAlSR5z2hZtC8hf3s5LRnZjG2FvBTVGw1MOC83%2B%2BBVlx5KxFbsgwpnQ2mYpaDQpNz%2B5CK2Ttb4Gr205dbuvoWxjAhlNdltBuCnf9A%2F0eQ56q1LraQoeG3Tm17YN94cj8D%2FzQRdf%2FoWSca33dELAeOLhnN%2FTFQB5mA8Gz8W7Ea6n1eKlGA8VAkLyaTfAxz9QtlhgpfoPKKIN4bvZR0h0KXS%2FEbO0CzTB3lpnDZ9ibIwJUIitGMqcc2ksUr9ylFETMeZ8mpl%2BW%2FM%2BGQ%2FWAB7Pio%2B1Hb0gX5KbAwiWvkfKVl9yaG%2BtHmRipbWvUzs%2F%2BvkuBNbJvZKknlcCnKy0eG3vnayge2fM2BYPtVLcafg5kQ47ilEgBThKBS32JAuwxb6tmFOZhy%2Fw5N0hNa%2BFmhpVG3QBqPzdpxn%2FhErlXHTMOxPm%2BdeAbxxI6R73MMe6%2F9IGOqUBT7ZrSDFyNZNTe82oN1oTCYzq9G3wGVsQjnT5mkgwGpjj9Omf3hbOF9klz3YcxzHtOdb2%2F4w4Kwc0hm6Q7cqLJYXftqyea7p3UsGnajSMTTKPmKgAGOq%2FJ59msNgHuZDCT1TiFrQSqnlDcStdzEk5bSGDpEqLRl4ZUSLxyr0gIUs7Zry8NA2%2Bs3oJmI7Nv%2FDLGH5nHy0aV%2FVN99cim3ecYS4%2F%2BxHd&X-Amz-Signature=180329e9f468a038bee3f9496dfae4bb0e96cd08790fa47acd1a6143005cf9ff&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

那就是咱的 trace A 了，因为 trace A 会在自己的服务中调用 trace B 那我们不妨点开 trace B 看一下这每一个调用里面都有哪些详细信息。比如说咱现在点击进去的是单独调用 trace B 的情况，在这里面它列出了 HT TP method 这里可以看到是一个 get 并且后面跟着是它的路径的名称。我们在点击这一行会有一个弹窗出来，而弹窗有点大。 OK 那这个弹窗中列出了三个维度的信息，咱把 more info 也给点出来。

[image](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/93ae3776-46ed-4712-b8cb-a75163d3108c/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46622BYEXNX%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T225800Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCFRr6Zpli3OhdqIRC9EtMXMQSTe81F3OQTPLv%2FoLhaNgIgfRyfUdaPYp3p2oe51OOc%2BFOilOS1eVWusEAkfO7DfH4qiAQIxv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDJgp5rLPF5LQdUCFgyrcA2kZKVx3pNMDpGoig5MhGSHF00VS2ZaRHYtwufAPkx7MFHWTXch27d5qeQh2W850t8VczHTTN%2B9AuL%2FdzU3tVER5fBdKaC17UgKYBMTY%2FJO3iicBYjbItMm4SoafiNhjPQXEAZ3rtdZowQ2gMQ6mbjfPrd40CARCPb66HRNyFRp36S704VFD1RzQcj6w72p0LS2b5%2BAlSR5z2hZtC8hf3s5LRnZjG2FvBTVGw1MOC83%2B%2BBVlx5KxFbsgwpnQ2mYpaDQpNz%2B5CK2Ttb4Gr205dbuvoWxjAhlNdltBuCnf9A%2F0eQ56q1LraQoeG3Tm17YN94cj8D%2FzQRdf%2FoWSca33dELAeOLhnN%2FTFQB5mA8Gz8W7Ea6n1eKlGA8VAkLyaTfAxz9QtlhgpfoPKKIN4bvZR0h0KXS%2FEbO0CzTB3lpnDZ9ibIwJUIitGMqcc2ksUr9ylFETMeZ8mpl%2BW%2FM%2BGQ%2FWAB7Pio%2B1Hb0gX5KbAwiWvkfKVl9yaG%2BtHmRipbWvUzs%2F%2BvkuBNbJvZKknlcCnKy0eG3vnayge2fM2BYPtVLcafg5kQ47ilEgBThKBS32JAuwxb6tmFOZhy%2Fw5N0hNa%2BFmhpVG3QBqPzdpxn%2FhErlXHTMOxPm%2BdeAbxxI6R73MMe6%2F9IGOqUBT7ZrSDFyNZNTe82oN1oTCYzq9G3wGVsQjnT5mkgwGpjj9Omf3hbOF9klz3YcxzHtOdb2%2F4w4Kwc0hm6Q7cqLJYXftqyea7p3UsGnajSMTTKPmKgAGOq%2FJ59msNgHuZDCT1TiFrQSqnlDcStdzEk5bSGDpEqLRl4ZUSLxyr0gIUs7Zry8NA2%2Bs3oJmI7Nv%2FDLGH5nHy0aV%2FVN99cim3ecYS4%2F%2BxHd&X-Amz-Signature=95d293c8e24d87ed5b6332aca30e9aace7fc041bd682d175f49dd0622bd2a3c0&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

OK 三个维度。首先在上面就是我们在图文中介绍的 annotation 这里面分为 server received 和 server send 两个部分。同学们从这里就可以看到在一个 span 当中不同的 annotation 之间的花费。那么再往下，这里就是它的调用情况，前面这是 client address 是它的 IP 地址，后面是 HTTP method 是 get 以及调用的路径。并且这里还会把 controller 的 class 给你列出来。列的相当详细。


往下，最后一个是 method 那最下面的两个信息，这就是 trace ID 和 span ID 了，那这个 trace ID 也是有用处的。我先把它复制一下。好，我们把窗口关上，看看这个 trace ID 如何来使用。咱看到页面上方，在这个点这个点看这里看这里这有一个 go to trace 那咱把 trace ID 输入进去，打一个回车。这就能搜到一个特定的 trace ID 了。我们不妨在 intelligi 里面打出的 log 里面，我们找一个 trace ID 就找它了。 trace aid okay 把它复制下来，回到浏览器当中走。


你同学们看到这里的页面展示有那么点不同了，因为咱刚才找的是 trace A 的一个 trace ID 那在 trace A 当中是不是要调用 trace B 从这个时间轴来看，上面的一行是 trace A 那它的花费是从这里直到尾巴总共 800 多毫秒，好长。那下面这一行是 trace B 的花费。所以咱从这个调用链路当中可以看到一个调用链的两个维度的信息，一个是它所花费的时间，第二个是它在这个调用链中所处的位置。


OK 咱看完这个页面再回到主页面里。我们刚才基于 server name 做了搜索，那后面还有 span name 这个 span 大家看到实际上就是调用的方法的 HD TP method 以及方法路径之间的一个组合。那么在旁边咱还可以选择 look back look back 是一个时间范围，我们选过后 1 小时之前 3 小时，6小时最长可以到 7 天

[image](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/9cc7b88a-13a7-4f34-a215-aef885446a05/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46622BYEXNX%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T225800Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCFRr6Zpli3OhdqIRC9EtMXMQSTe81F3OQTPLv%2FoLhaNgIgfRyfUdaPYp3p2oe51OOc%2BFOilOS1eVWusEAkfO7DfH4qiAQIxv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDJgp5rLPF5LQdUCFgyrcA2kZKVx3pNMDpGoig5MhGSHF00VS2ZaRHYtwufAPkx7MFHWTXch27d5qeQh2W850t8VczHTTN%2B9AuL%2FdzU3tVER5fBdKaC17UgKYBMTY%2FJO3iicBYjbItMm4SoafiNhjPQXEAZ3rtdZowQ2gMQ6mbjfPrd40CARCPb66HRNyFRp36S704VFD1RzQcj6w72p0LS2b5%2BAlSR5z2hZtC8hf3s5LRnZjG2FvBTVGw1MOC83%2B%2BBVlx5KxFbsgwpnQ2mYpaDQpNz%2B5CK2Ttb4Gr205dbuvoWxjAhlNdltBuCnf9A%2F0eQ56q1LraQoeG3Tm17YN94cj8D%2FzQRdf%2FoWSca33dELAeOLhnN%2FTFQB5mA8Gz8W7Ea6n1eKlGA8VAkLyaTfAxz9QtlhgpfoPKKIN4bvZR0h0KXS%2FEbO0CzTB3lpnDZ9ibIwJUIitGMqcc2ksUr9ylFETMeZ8mpl%2BW%2FM%2BGQ%2FWAB7Pio%2B1Hb0gX5KbAwiWvkfKVl9yaG%2BtHmRipbWvUzs%2F%2BvkuBNbJvZKknlcCnKy0eG3vnayge2fM2BYPtVLcafg5kQ47ilEgBThKBS32JAuwxb6tmFOZhy%2Fw5N0hNa%2BFmhpVG3QBqPzdpxn%2FhErlXHTMOxPm%2BdeAbxxI6R73MMe6%2F9IGOqUBT7ZrSDFyNZNTe82oN1oTCYzq9G3wGVsQjnT5mkgwGpjj9Omf3hbOF9klz3YcxzHtOdb2%2F4w4Kwc0hm6Q7cqLJYXftqyea7p3UsGnajSMTTKPmKgAGOq%2FJ59msNgHuZDCT1TiFrQSqnlDcStdzEk5bSGDpEqLRl4ZUSLxyr0gIUs7Zry8NA2%2Bs3oJmI7Nv%2FDLGH5nHy0aV%2FVN99cim3ecYS4%2F%2BxHd&X-Amz-Signature=ba9ad695b9730bea09c9e03c29140c1933cbb86b763a3961849d95248cbfcfc0&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

如果你觉得这个时间不够，还可以选择 custom 也就是自定制的一段时间。除了这部分的内容以外，咱还可以对页面显示的条数进行一个限制。并且还可以根据时间维度来查找信息。但是大家如果根据时间维度查找要注意这个时间单位是 us 不是 MS 它是微秒的意思。


除此以外，它还带了一个复杂搜索的功能，就是 annotations query。

[image](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/5b09fe44-ecea-40a2-9e60-113f415ecc0f/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46622BYEXNX%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T225800Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCFRr6Zpli3OhdqIRC9EtMXMQSTe81F3OQTPLv%2FoLhaNgIgfRyfUdaPYp3p2oe51OOc%2BFOilOS1eVWusEAkfO7DfH4qiAQIxv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDJgp5rLPF5LQdUCFgyrcA2kZKVx3pNMDpGoig5MhGSHF00VS2ZaRHYtwufAPkx7MFHWTXch27d5qeQh2W850t8VczHTTN%2B9AuL%2FdzU3tVER5fBdKaC17UgKYBMTY%2FJO3iicBYjbItMm4SoafiNhjPQXEAZ3rtdZowQ2gMQ6mbjfPrd40CARCPb66HRNyFRp36S704VFD1RzQcj6w72p0LS2b5%2BAlSR5z2hZtC8hf3s5LRnZjG2FvBTVGw1MOC83%2B%2BBVlx5KxFbsgwpnQ2mYpaDQpNz%2B5CK2Ttb4Gr205dbuvoWxjAhlNdltBuCnf9A%2F0eQ56q1LraQoeG3Tm17YN94cj8D%2FzQRdf%2FoWSca33dELAeOLhnN%2FTFQB5mA8Gz8W7Ea6n1eKlGA8VAkLyaTfAxz9QtlhgpfoPKKIN4bvZR0h0KXS%2FEbO0CzTB3lpnDZ9ibIwJUIitGMqcc2ksUr9ylFETMeZ8mpl%2BW%2FM%2BGQ%2FWAB7Pio%2B1Hb0gX5KbAwiWvkfKVl9yaG%2BtHmRipbWvUzs%2F%2BvkuBNbJvZKknlcCnKy0eG3vnayge2fM2BYPtVLcafg5kQ47ilEgBThKBS32JAuwxb6tmFOZhy%2Fw5N0hNa%2BFmhpVG3QBqPzdpxn%2FhErlXHTMOxPm%2BdeAbxxI6R73MMe6%2F9IGOqUBT7ZrSDFyNZNTe82oN1oTCYzq9G3wGVsQjnT5mkgwGpjj9Omf3hbOF9klz3YcxzHtOdb2%2F4w4Kwc0hm6Q7cqLJYXftqyea7p3UsGnajSMTTKPmKgAGOq%2FJ59msNgHuZDCT1TiFrQSqnlDcStdzEk5bSGDpEqLRl4ZUSLxyr0gIUs7Zry8NA2%2Bs3oJmI7Nv%2FDLGH5nHy0aV%2FVN99cim3ecYS4%2F%2BxHd&X-Amz-Signature=1ebbfe311ea5f8dd8c976eb7f8cfc188580e689d72f62d1b144969e52eeefec5&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

大家如果有用过其他的 log 组件，比如像 splunk 之类的 log 查询组件，它们都有这样一个服务，这个功能其实是非常非常重要的。当然了 zipking 里的 annotation query 相对来说比较初级，那像更厉害的商业软件，像 splunk 它这个 query 所支持的表达式非常非常丰富，你可以基于你的代码类型，包括你的服务器的地址以及非常非常复杂的查询语句来定位你的线上问题。
好，看到这个功能以后，咱再带大家看其他的几个功能。上面有四个按钮，其中 find trace 就是当前的这个页面了，咱不用看。然后后面一个按钮是 will save the trace 它允许大家上传一个文件，然后从文件中抽取数据。这个功能不太常用。然后再带大家看一个有点黑科技的功能 dependencies 这个功能是什么呢？呦你瞧还会变色。

[image](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/e811de64-2f9c-4265-9d16-ed47a0e74beb/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46622BYEXNX%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T225800Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCFRr6Zpli3OhdqIRC9EtMXMQSTe81F3OQTPLv%2FoLhaNgIgfRyfUdaPYp3p2oe51OOc%2BFOilOS1eVWusEAkfO7DfH4qiAQIxv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDJgp5rLPF5LQdUCFgyrcA2kZKVx3pNMDpGoig5MhGSHF00VS2ZaRHYtwufAPkx7MFHWTXch27d5qeQh2W850t8VczHTTN%2B9AuL%2FdzU3tVER5fBdKaC17UgKYBMTY%2FJO3iicBYjbItMm4SoafiNhjPQXEAZ3rtdZowQ2gMQ6mbjfPrd40CARCPb66HRNyFRp36S704VFD1RzQcj6w72p0LS2b5%2BAlSR5z2hZtC8hf3s5LRnZjG2FvBTVGw1MOC83%2B%2BBVlx5KxFbsgwpnQ2mYpaDQpNz%2B5CK2Ttb4Gr205dbuvoWxjAhlNdltBuCnf9A%2F0eQ56q1LraQoeG3Tm17YN94cj8D%2FzQRdf%2FoWSca33dELAeOLhnN%2FTFQB5mA8Gz8W7Ea6n1eKlGA8VAkLyaTfAxz9QtlhgpfoPKKIN4bvZR0h0KXS%2FEbO0CzTB3lpnDZ9ibIwJUIitGMqcc2ksUr9ylFETMeZ8mpl%2BW%2FM%2BGQ%2FWAB7Pio%2B1Hb0gX5KbAwiWvkfKVl9yaG%2BtHmRipbWvUzs%2F%2BvkuBNbJvZKknlcCnKy0eG3vnayge2fM2BYPtVLcafg5kQ47ilEgBThKBS32JAuwxb6tmFOZhy%2Fw5N0hNa%2BFmhpVG3QBqPzdpxn%2FhErlXHTMOxPm%2BdeAbxxI6R73MMe6%2F9IGOqUBT7ZrSDFyNZNTe82oN1oTCYzq9G3wGVsQjnT5mkgwGpjj9Omf3hbOF9klz3YcxzHtOdb2%2F4w4Kwc0hm6Q7cqLJYXftqyea7p3UsGnajSMTTKPmKgAGOq%2FJ59msNgHuZDCT1TiFrQSqnlDcStdzEk5bSGDpEqLRl4ZUSLxyr0gIUs7Zry8NA2%2Bs3oJmI7Nv%2FDLGH5nHy0aV%2FVN99cim3ecYS4%2F%2BxHd&X-Amz-Signature=01340d37b6eba9ef3c295184cd3d14d7c0dde1655ba956ff59fa317bdbcb3880&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

这个功能是梳理上下游调用链路的，咱把图片放大一些，好像不怎么听话。图片乱飘。大家可以看到图中有两个方框，分别是 sleuth 的 trace A 和 sleeper trace B 这里有一个非常非常不起眼的小箭头，哎呀我尝试把它放大。大家看到吗？这有个小箭头，单向箭头，它是从 trace A 指向 trace B 那说明这个调用链路是从 A 到 B 上面还有一串时间选择框，大家可以选择一个起始时间点击 analyze dependency 分析在这个时间段内的所有服务请求调用情况。并且从下面的图中可以梳理出一副微服务调用的全景。但是友情提示大家，如果你们的微服务组件拆得特别细，我个人建议密集恐惧症的同学，请速速回避这个功能 dependency 要盛典，不然你会看到一个密密麻麻像马蜂窝一样的图形。


讲到这里，相信大家对 zipkin 的功能也有一定的了解了。那所以大家应该也看到了，它并不是一个日志搜索的组件，而**是一个从时间维度上对调用链路进行分析的组件**。不过 zipking 也是可以集成 elk 的。我们对 zipking 的配置做一些定制，那么就可以在界面上售出一个新的按钮，然后通过这个按钮导向 elk 的功能。


OK 那讲到这里，整个 zip king 的下半场也就结束了。那我来带大家回顾一下，在下半场当中，我们首先给 trace A 和 trace B 添加了 zipkin 的美文依赖，然后在 properties 里面配置了 zipkin 的地址。这样一来，咱先前配置的采样率也就生效了。之后带大家浏览了 zipking 的 dashboard 熟悉了这里面的几个搜索，还有调用链路详情的功能。这里面其实还隐藏着一个小技巧是什么呢？咱在搜索出 zipkin 的 log 以后，可以点击这个 sort 按钮这里有一个下拉框，我们可以选择花费时间最长的服务，

[image](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/91cf015d-5d5b-4830-91fa-6b4e317c98f3/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46622BYEXNX%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T225800Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCFRr6Zpli3OhdqIRC9EtMXMQSTe81F3OQTPLv%2FoLhaNgIgfRyfUdaPYp3p2oe51OOc%2BFOilOS1eVWusEAkfO7DfH4qiAQIxv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDJgp5rLPF5LQdUCFgyrcA2kZKVx3pNMDpGoig5MhGSHF00VS2ZaRHYtwufAPkx7MFHWTXch27d5qeQh2W850t8VczHTTN%2B9AuL%2FdzU3tVER5fBdKaC17UgKYBMTY%2FJO3iicBYjbItMm4SoafiNhjPQXEAZ3rtdZowQ2gMQ6mbjfPrd40CARCPb66HRNyFRp36S704VFD1RzQcj6w72p0LS2b5%2BAlSR5z2hZtC8hf3s5LRnZjG2FvBTVGw1MOC83%2B%2BBVlx5KxFbsgwpnQ2mYpaDQpNz%2B5CK2Ttb4Gr205dbuvoWxjAhlNdltBuCnf9A%2F0eQ56q1LraQoeG3Tm17YN94cj8D%2FzQRdf%2FoWSca33dELAeOLhnN%2FTFQB5mA8Gz8W7Ea6n1eKlGA8VAkLyaTfAxz9QtlhgpfoPKKIN4bvZR0h0KXS%2FEbO0CzTB3lpnDZ9ibIwJUIitGMqcc2ksUr9ylFETMeZ8mpl%2BW%2FM%2BGQ%2FWAB7Pio%2B1Hb0gX5KbAwiWvkfKVl9yaG%2BtHmRipbWvUzs%2F%2BvkuBNbJvZKknlcCnKy0eG3vnayge2fM2BYPtVLcafg5kQ47ilEgBThKBS32JAuwxb6tmFOZhy%2Fw5N0hNa%2BFmhpVG3QBqPzdpxn%2FhErlXHTMOxPm%2BdeAbxxI6R73MMe6%2F9IGOqUBT7ZrSDFyNZNTe82oN1oTCYzq9G3wGVsQjnT5mkgwGpjj9Omf3hbOF9klz3YcxzHtOdb2%2F4w4Kwc0hm6Q7cqLJYXftqyea7p3UsGnajSMTTKPmKgAGOq%2FJ59msNgHuZDCT1TiFrQSqnlDcStdzEk5bSGDpEqLRl4ZUSLxyr0gIUs7Zry8NA2%2Bs3oJmI7Nv%2FDLGH5nHy0aV%2FVN99cim3ecYS4%2F%2BxHd&X-Amz-Signature=4f19d2ba568fcd49623660f0aae86596ee882d0eb214c41c32cece35b7603b48&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

然后点击搜索。这样的话能怎么样？能帮我们梳理出整个调用链路中有哪些可能发生了 timeout 或者因为任何情况导致调用时间特别长的那些调用链，这样大家就能深入问题并且最终解决问题了。 OK 那这一节的内容就到这里结束了。在下一节当中，我们趁热打铁，带大家再去学习一个 sloose 的好兄弟就是 elk 那它可是一个专业的 Lark 日志搜索组件。同学们，那我们下一节再见。



