---
title: 1-14 【技术改造】电商项系统集成Sleuth- 全面集成Sleuth+Zipkin
---

# 1-14 【技术改造】电商项系统集成Sleuth- 全面集成Sleuth+Zipkin

[image](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/90b94e3e-d15c-4565-8cb2-93c574fd3479/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TO7CXWGX%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T225805Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCW7lPn6yfibVN4UyaLW413F5hzxMiyD7eCTwJtuGz3eQIhAMuoiOMhS1asqFPvTQhiIFCWe1ww65N6jcrt67E0Fo89KogECMb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1Igy1kQGXQkBYFK0J0b8q3AOFhsOjpFyafau9%2FCCKspmyM8hybQ1byRfJZP3OVLK6POmQH2cHfn062iLmzKw%2FNEqK3aGizo3XQqEfOZzqSS%2FvejbjEh75xKrfcbbrkZUsbWhS9P0obJCx0lkSq%2F9ZNowfVv%2FYL7lHEOz%2By9I%2FWhBr4%2BQpP0zTAtj1%2BRblxkNYvQ5eT0wERGJxiNaz8xXK3BHBQZjY%2FxOIXjXrrskc3XymUmP05R9hRn6M0FrzZFieN1Vqss5N75%2Bn47mxhDD7L%2BBshGdpiddE61TS6a2SJFN%2FUK8nPwuRbfH7%2B1cXvz5QUJCdF4P9B3Zq8TyRsy6KvFlpfl6Cb2jXxUBfivwrM1aftlNNqO%2B6R8ldxLk%2Bw2AohNhdwhaB9mDLYAu8VFYUsFzY8P7xcmvIreddJEDtVy57ovrrUErLtBcdmk37p9DzXPRHzIM0%2BjjRHDzl5p4nyUlWaMsBW%2BBewGeBJrKTcqTuKuVmuXquOpv9bUF2UhNc9pT3mB3X3KcYwMJTWRR8QMuHmNin0TEnLUliaEVIZCCFgqn%2FHGiNd2xDOYYhssx7D2HgkoYMraWgG1%2FltQKvvyXwAMdX2sqp47JdviVcus%2BrHth1Bo5qmnXiRJj71Qo8SkC5niadK39T3A%2BHRTDxt%2F%2FSBjqkAetoCdaSDtjcRdeV1IGWra5RmVlwUrx98pPqQ0kqx86NjaYwx5HSDhom7EQDzyU1GMCT%2Fw%2F1aa%2BAohfpOVkL8IPrp8ecUs%2BhkhoEwQ9rs7rhVmNN0Ig8gU%2FddeZg1BQ245Z4S0U5FDCRne%2FJgu84ixoj37X%2BiP7NL9CAwyzSgiOQZYS2Z%2BeLC1S4my1%2BB%2FvWAnnRQHq2Bmhw%2BiACgO5Q5ocrI9Gb&X-Amz-Signature=b35c567fc0e719c2cf1519d3143821b9ff50674c0700976cc2eebd9d7d159078&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

hello 木客网的各位小伙伴大家好，我是姚半仙，咱这一节当中将要全面集成 sleutha 和 zip king 了。那咱挑选了三个模块来做集成。是哪三个模块呢？我们先不剧透，跟着导演的剧本往下走。在这个集成过程中有一些坑还需要趟的。我们挨个走起看。好。那这第一个服务，你看我这都打开了，就是 authentication 咱的 auth API 那我们找准 off API 的 service 层，打开它的 palm 文件。在这个 palm 里，我们先把这两个 dependency 给它加上来。那当然就是这两个了。


一个是 sleeves 另一个是咱的 zip king 好，那添加完了依赖项，接下来我们要去改一下配置文件。那这个步骤和咱前面的 demo 非常相似，找到它的配置文件。在这里，我们把这个小桌板给收起来，然后找一块空地在哪里在 spring 下面，现在打一个 zip king 接下来配置和 demo 里面相似，但是不是百分之百一样。


那哪里不一样呢？我们来看咱的这个 base URL 以前是怎么样的？以前是这样配的 HD DP 后面跟 local host 再跟个端口 1234 之类的端口。咱这里逼格高了，咱前面不是配了高可用对不对，那接下来这个 base URL 我们配一个 eureka 里面的地址 zip king server 好嘞，那这就 OK 了。那从这里面我们可以看到它启用了一种什么呢？它是用了一种服务发现的机制。

```shell
server:
  port: 10006

spring:
  application:
    name: foodie-auth-service
  redis:
    database: 8
    host: 172.16.136.222
    port: 6379
#    password:
  zipkin:
    discoveryClientEnabled: true
    base-url: http://ZIPKIN-SERVER/
    locator:
      discovery:
        enabled: true
  sleuth:
    sampler:
      probability: 1

eureka:
  client:
    serviceUrl:
      defaultZone: http://localhost:20000/eureka/
  instance:
    instance-id: ${spring.cloud.client.ip-address}.${server.port}
    prefer-ip-address: true

management:
  endpoint:
    health:
      show-details: always
  endpoints:
    web:
      exposure:
        include: '*'
  security:
    enabled: false
```


好， eureka client enable shoot **那同学们看老师打这些属性，是不是不晓得这些 zipkin 之类的组件它都有哪些可用的 property 如果你有同样的问题，我教给大家一个非常简单的方法，咱的 spring cloud 下面的组件都非常的守规矩。**


如果你想查找某个组件下面的 property 比如 zip king 那很简单，你就这样搜好了 zipkin 后面跟什么呢？ a practice 好，这一搜你就可以搜到 zipkin 的这个 properties 类。

[image](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/b6e9f691-3fef-4831-8459-59022b4092ff/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TO7CXWGX%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T225805Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCW7lPn6yfibVN4UyaLW413F5hzxMiyD7eCTwJtuGz3eQIhAMuoiOMhS1asqFPvTQhiIFCWe1ww65N6jcrt67E0Fo89KogECMb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1Igy1kQGXQkBYFK0J0b8q3AOFhsOjpFyafau9%2FCCKspmyM8hybQ1byRfJZP3OVLK6POmQH2cHfn062iLmzKw%2FNEqK3aGizo3XQqEfOZzqSS%2FvejbjEh75xKrfcbbrkZUsbWhS9P0obJCx0lkSq%2F9ZNowfVv%2FYL7lHEOz%2By9I%2FWhBr4%2BQpP0zTAtj1%2BRblxkNYvQ5eT0wERGJxiNaz8xXK3BHBQZjY%2FxOIXjXrrskc3XymUmP05R9hRn6M0FrzZFieN1Vqss5N75%2Bn47mxhDD7L%2BBshGdpiddE61TS6a2SJFN%2FUK8nPwuRbfH7%2B1cXvz5QUJCdF4P9B3Zq8TyRsy6KvFlpfl6Cb2jXxUBfivwrM1aftlNNqO%2B6R8ldxLk%2Bw2AohNhdwhaB9mDLYAu8VFYUsFzY8P7xcmvIreddJEDtVy57ovrrUErLtBcdmk37p9DzXPRHzIM0%2BjjRHDzl5p4nyUlWaMsBW%2BBewGeBJrKTcqTuKuVmuXquOpv9bUF2UhNc9pT3mB3X3KcYwMJTWRR8QMuHmNin0TEnLUliaEVIZCCFgqn%2FHGiNd2xDOYYhssx7D2HgkoYMraWgG1%2FltQKvvyXwAMdX2sqp47JdviVcus%2BrHth1Bo5qmnXiRJj71Qo8SkC5niadK39T3A%2BHRTDxt%2F%2FSBjqkAetoCdaSDtjcRdeV1IGWra5RmVlwUrx98pPqQ0kqx86NjaYwx5HSDhom7EQDzyU1GMCT%2Fw%2F1aa%2BAohfpOVkL8IPrp8ecUs%2BhkhoEwQ9rs7rhVmNN0Ig8gU%2FddeZg1BQ245Z4S0U5FDCRne%2FJgu84ixoj37X%2BiP7NL9CAwyzSgiOQZYS2Z%2BeLC1S4my1%2BB%2FvWAnnRQHq2Bmhw%2BiACgO5Q5ocrI9Gb&X-Amz-Signature=33fcd490a82828d6afa7a0c127f0ab1f3fdfe689c81d1b9d504a6b171c68e45d&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

那你从这里面就可以看到它的各个属性都是怎么配置的。

[image](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/362868a2-2a7a-47f5-9493-fc85f00971df/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TO7CXWGX%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T225805Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCW7lPn6yfibVN4UyaLW413F5hzxMiyD7eCTwJtuGz3eQIhAMuoiOMhS1asqFPvTQhiIFCWe1ww65N6jcrt67E0Fo89KogECMb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1Igy1kQGXQkBYFK0J0b8q3AOFhsOjpFyafau9%2FCCKspmyM8hybQ1byRfJZP3OVLK6POmQH2cHfn062iLmzKw%2FNEqK3aGizo3XQqEfOZzqSS%2FvejbjEh75xKrfcbbrkZUsbWhS9P0obJCx0lkSq%2F9ZNowfVv%2FYL7lHEOz%2By9I%2FWhBr4%2BQpP0zTAtj1%2BRblxkNYvQ5eT0wERGJxiNaz8xXK3BHBQZjY%2FxOIXjXrrskc3XymUmP05R9hRn6M0FrzZFieN1Vqss5N75%2Bn47mxhDD7L%2BBshGdpiddE61TS6a2SJFN%2FUK8nPwuRbfH7%2B1cXvz5QUJCdF4P9B3Zq8TyRsy6KvFlpfl6Cb2jXxUBfivwrM1aftlNNqO%2B6R8ldxLk%2Bw2AohNhdwhaB9mDLYAu8VFYUsFzY8P7xcmvIreddJEDtVy57ovrrUErLtBcdmk37p9DzXPRHzIM0%2BjjRHDzl5p4nyUlWaMsBW%2BBewGeBJrKTcqTuKuVmuXquOpv9bUF2UhNc9pT3mB3X3KcYwMJTWRR8QMuHmNin0TEnLUliaEVIZCCFgqn%2FHGiNd2xDOYYhssx7D2HgkoYMraWgG1%2FltQKvvyXwAMdX2sqp47JdviVcus%2BrHth1Bo5qmnXiRJj71Qo8SkC5niadK39T3A%2BHRTDxt%2F%2FSBjqkAetoCdaSDtjcRdeV1IGWra5RmVlwUrx98pPqQ0kqx86NjaYwx5HSDhom7EQDzyU1GMCT%2Fw%2F1aa%2BAohfpOVkL8IPrp8ecUs%2BhkhoEwQ9rs7rhVmNN0Ig8gU%2FddeZg1BQ245Z4S0U5FDCRne%2FJgu84ixoj37X%2BiP7NL9CAwyzSgiOQZYS2Z%2BeLC1S4my1%2BB%2FvWAnnRQHq2Bmhw%2BiACgO5Q5ocrI9Gb&X-Amz-Signature=9e2a40e1f71c00f2906dfb3013a7055f60ee77c4cd3c7ca739829c2d5e865091&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

比方说咱前面配置的这个 base URL 那你这里就可以看到它源码，它这里有个默认的basel ，那咱前面把它给覆盖掉了，同时我们还配置了 discovery client enabled 那从这里面我们还可以看到其他的几个属性，比方说这个属性 enabled 它默认是 true 如果我们给它设置成 false 比如在这里当头一棒 enable 的给它设成 false 那不管你后面怎么配置，

[image](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/860df2c7-bd77-42b0-b4d3-4aae9a0bbbac/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TO7CXWGX%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T225805Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCW7lPn6yfibVN4UyaLW413F5hzxMiyD7eCTwJtuGz3eQIhAMuoiOMhS1asqFPvTQhiIFCWe1ww65N6jcrt67E0Fo89KogECMb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1Igy1kQGXQkBYFK0J0b8q3AOFhsOjpFyafau9%2FCCKspmyM8hybQ1byRfJZP3OVLK6POmQH2cHfn062iLmzKw%2FNEqK3aGizo3XQqEfOZzqSS%2FvejbjEh75xKrfcbbrkZUsbWhS9P0obJCx0lkSq%2F9ZNowfVv%2FYL7lHEOz%2By9I%2FWhBr4%2BQpP0zTAtj1%2BRblxkNYvQ5eT0wERGJxiNaz8xXK3BHBQZjY%2FxOIXjXrrskc3XymUmP05R9hRn6M0FrzZFieN1Vqss5N75%2Bn47mxhDD7L%2BBshGdpiddE61TS6a2SJFN%2FUK8nPwuRbfH7%2B1cXvz5QUJCdF4P9B3Zq8TyRsy6KvFlpfl6Cb2jXxUBfivwrM1aftlNNqO%2B6R8ldxLk%2Bw2AohNhdwhaB9mDLYAu8VFYUsFzY8P7xcmvIreddJEDtVy57ovrrUErLtBcdmk37p9DzXPRHzIM0%2BjjRHDzl5p4nyUlWaMsBW%2BBewGeBJrKTcqTuKuVmuXquOpv9bUF2UhNc9pT3mB3X3KcYwMJTWRR8QMuHmNin0TEnLUliaEVIZCCFgqn%2FHGiNd2xDOYYhssx7D2HgkoYMraWgG1%2FltQKvvyXwAMdX2sqp47JdviVcus%2BrHth1Bo5qmnXiRJj71Qo8SkC5niadK39T3A%2BHRTDxt%2F%2FSBjqkAetoCdaSDtjcRdeV1IGWra5RmVlwUrx98pPqQ0kqx86NjaYwx5HSDhom7EQDzyU1GMCT%2Fw%2F1aa%2BAohfpOVkL8IPrp8ecUs%2BhkhoEwQ9rs7rhVmNN0Ig8gU%2FddeZg1BQ245Z4S0U5FDCRne%2FJgu84ixoj37X%2BiP7NL9CAwyzSgiOQZYS2Z%2BeLC1S4my1%2BB%2FvWAnnRQHq2Bmhw%2BiACgO5Q5ocrI9Gb&X-Amz-Signature=ae3f7df375666654efb18ef8bcf1aedab3bbc21ff52fbea41c0eabf52d92b18b&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

这个 zip care 都不会生效了。

[image](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/8901cd20-f627-44b0-82dd-720c9eff678f/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TO7CXWGX%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T225805Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCW7lPn6yfibVN4UyaLW413F5hzxMiyD7eCTwJtuGz3eQIhAMuoiOMhS1asqFPvTQhiIFCWe1ww65N6jcrt67E0Fo89KogECMb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1Igy1kQGXQkBYFK0J0b8q3AOFhsOjpFyafau9%2FCCKspmyM8hybQ1byRfJZP3OVLK6POmQH2cHfn062iLmzKw%2FNEqK3aGizo3XQqEfOZzqSS%2FvejbjEh75xKrfcbbrkZUsbWhS9P0obJCx0lkSq%2F9ZNowfVv%2FYL7lHEOz%2By9I%2FWhBr4%2BQpP0zTAtj1%2BRblxkNYvQ5eT0wERGJxiNaz8xXK3BHBQZjY%2FxOIXjXrrskc3XymUmP05R9hRn6M0FrzZFieN1Vqss5N75%2Bn47mxhDD7L%2BBshGdpiddE61TS6a2SJFN%2FUK8nPwuRbfH7%2B1cXvz5QUJCdF4P9B3Zq8TyRsy6KvFlpfl6Cb2jXxUBfivwrM1aftlNNqO%2B6R8ldxLk%2Bw2AohNhdwhaB9mDLYAu8VFYUsFzY8P7xcmvIreddJEDtVy57ovrrUErLtBcdmk37p9DzXPRHzIM0%2BjjRHDzl5p4nyUlWaMsBW%2BBewGeBJrKTcqTuKuVmuXquOpv9bUF2UhNc9pT3mB3X3KcYwMJTWRR8QMuHmNin0TEnLUliaEVIZCCFgqn%2FHGiNd2xDOYYhssx7D2HgkoYMraWgG1%2FltQKvvyXwAMdX2sqp47JdviVcus%2BrHth1Bo5qmnXiRJj71Qo8SkC5niadK39T3A%2BHRTDxt%2F%2FSBjqkAetoCdaSDtjcRdeV1IGWra5RmVlwUrx98pPqQ0kqx86NjaYwx5HSDhom7EQDzyU1GMCT%2Fw%2F1aa%2BAohfpOVkL8IPrp8ecUs%2BhkhoEwQ9rs7rhVmNN0Ig8gU%2FddeZg1BQ245Z4S0U5FDCRne%2FJgu84ixoj37X%2BiP7NL9CAwyzSgiOQZYS2Z%2BeLC1S4my1%2BB%2FvWAnnRQHq2Bmhw%2BiACgO5Q5ocrI9Gb&X-Amz-Signature=2d3b9f611458e468904f893017d340008a45a497224ede41a718530fda55c43a&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)


那从下面这些属性中，比方说这个locator ，这下面我们可以看到 locator 下面还有一个配置 discovery 下面还有个 enabled 那这里其实就是一个层次结构，像这一类的配置项，我们这里还有一个 locator 还有一个 compression 那如果咱想在自己的配置文件中配置这样一个层次结构，非常简单，我们只有模仿它这个源代码里的这个层次。

[image](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/af61016a-91ec-4330-8b0c-2a89844b687e/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TO7CXWGX%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T225805Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCW7lPn6yfibVN4UyaLW413F5hzxMiyD7eCTwJtuGz3eQIhAMuoiOMhS1asqFPvTQhiIFCWe1ww65N6jcrt67E0Fo89KogECMb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1Igy1kQGXQkBYFK0J0b8q3AOFhsOjpFyafau9%2FCCKspmyM8hybQ1byRfJZP3OVLK6POmQH2cHfn062iLmzKw%2FNEqK3aGizo3XQqEfOZzqSS%2FvejbjEh75xKrfcbbrkZUsbWhS9P0obJCx0lkSq%2F9ZNowfVv%2FYL7lHEOz%2By9I%2FWhBr4%2BQpP0zTAtj1%2BRblxkNYvQ5eT0wERGJxiNaz8xXK3BHBQZjY%2FxOIXjXrrskc3XymUmP05R9hRn6M0FrzZFieN1Vqss5N75%2Bn47mxhDD7L%2BBshGdpiddE61TS6a2SJFN%2FUK8nPwuRbfH7%2B1cXvz5QUJCdF4P9B3Zq8TyRsy6KvFlpfl6Cb2jXxUBfivwrM1aftlNNqO%2B6R8ldxLk%2Bw2AohNhdwhaB9mDLYAu8VFYUsFzY8P7xcmvIreddJEDtVy57ovrrUErLtBcdmk37p9DzXPRHzIM0%2BjjRHDzl5p4nyUlWaMsBW%2BBewGeBJrKTcqTuKuVmuXquOpv9bUF2UhNc9pT3mB3X3KcYwMJTWRR8QMuHmNin0TEnLUliaEVIZCCFgqn%2FHGiNd2xDOYYhssx7D2HgkoYMraWgG1%2FltQKvvyXwAMdX2sqp47JdviVcus%2BrHth1Bo5qmnXiRJj71Qo8SkC5niadK39T3A%2BHRTDxt%2F%2FSBjqkAetoCdaSDtjcRdeV1IGWra5RmVlwUrx98pPqQ0kqx86NjaYwx5HSDhom7EQDzyU1GMCT%2Fw%2F1aa%2BAohfpOVkL8IPrp8ecUs%2BhkhoEwQ9rs7rhVmNN0Ig8gU%2FddeZg1BQ245Z4S0U5FDCRne%2FJgu84ixoj37X%2BiP7NL9CAwyzSgiOQZYS2Z%2BeLC1S4my1%2BB%2FvWAnnRQHq2Bmhw%2BiACgO5Q5ocrI9Gb&X-Amz-Signature=e8cbff8de299e08ead57ac3dc7fa32739ff69f240fcf987020ecf512e711422f&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

比如说 locator 好，我这里也配一个 locator 那 locator 下面是什么是 discovery discovery 后面 enable 通过服务发现来定位它的 host name 好，那这三层结构就对应了 zip king properties 里面的 locator 下面 discovery 在下面的 enable 那非常简单对不对？ OK 那咱配置完了 zip king ，接下来我们要去配置 smooth 我们的 sleutha 下面配置一个什么属性呢？它前面在随堂 demo 里面配置过怎么样采样率，采样率里面这个属性的名称，大家要注意，它可不叫 percentage 那咱的这个新版本里面应该是叫 probability 很容易拼错。好，我这里设置成一百分之百的采样率。前一句还说很容易拼错，我自己就拼错了 probabilityok 这样就对了。那我们这一个 authentication 的服务就已经配置好了，我们可以把它给启动起来，在启动的同时，我们可以去接下来配置。


第二个需要配置 sleast 和 zip king 的服务是谁呢？同学们可以猜一猜 outer 服务 item user no 我们这次配置的是一个中间件服务是谁呢？网关层。同学们不要以为咱的 zip king 和 sluza 只能配置在微服务里边，在这种中间件网关里面依然可以配置的。因为理论上来说咱的网关层其实就是一个微服务，它同样的也要注册在咱的注册中心上面。 OK 那咱们给网关层配置的这个手法是一样的，我们先把这两个链路追踪和 zip king 它俩的 dependency 加到网关层这里。


好嘞，那加完之后，同样的，我们到 application YAML 里面，把这个给复制过来，复制到哪去复制到网关层的 application YAML 里面，网关层这个有点乱，我配置在上面。好了，这样看起来比较清爽一点，再给它加个小标题叫链路追踪，然后再把它和下面的路由规则划清界限。
那下面这是什么？这叫跨域配置，这样一看就显得清晰多了。对不对？ OK 那咱前面说这次要配置三个模块，其中还有一个模块有一点坑，那我们已经配置好了两个。那下面一个汤坑的模块是谁呢？那就是咱的 user 用户为服务模块，这里面都有什么坑呢？我们一边来配一边再来说我们打开 Tom 文件，在这里面有坑吗？当然没坑了，咱的这个开局还是很顺利的，没有开局被压。好，我们把这两个属性同样的配置在 user web 当中。


好了，现在坑来了。同学们如果尝试着用同样的方式在这个 resources 下面，我们找是哪个 resources 在这个 application DEV 里，我们如果用同样的方式把 zip king 和 sluice 配置过来复制，然后粘贴过来粘贴到这里。


好了，在 Redis 下面。那这样会不会起作用呢？同学们猜一猜，坑就在此，你这种方式启动，你会发现你的 zip king 根本收不到任何消息。这很奇怪，对不对？咱的同样的这套配置，在 off 服务和 gateway 里面，那都可以顺利的向 zipking 发送消息。但是在咱的 user web 当中就不一样。同学们知道这是为什么呢？这个其实跟咱的 spring cloud 太过于智能化有关。怎么说我们想一想，咱在前面的章节当中是不是学过一个非常智能化的组件叫什么呢？我们到 palm 里面一探究竟。我们看，往上走。


这里看到吗？ bus 推送为什么说它比较智能呢？因为咱集成了这个 bus 推送以后，我们的配置中心不用做任何多余的配置，你只用在自己的这个启动文件当中，配置好 rabbit MQ 的连接串，那就可以自动的使用 bus 组件来推送，是不是非常的智能呢？但是咱们说这个智能是一把双刃剑。怎么说，因为我们的这个 bus amqb 这一个dependency ，它多余的引入了咱 rabbit MQ 的依赖。这一引入可不要紧。这个 zipkin 看到可欢脱了。好，以前咱 zipking 是使用最简单的那种 web 接收的方式。那好家伙一看，你引入了这个 rabi MQ 好了，它就在底层，非常智能的，并且偷偷摸摸的把你像 zip king 推送数据的方式变成了基于 rap MQ 这一改不要紧，这 zipking 可接受不了了，两头不匹配。那我们要改的话怎么来改呢？两种方式，你要么让两头匹配起来，一端用 rabbit MQ 发另一端同样也用 rabbit MQ 来收。那如果你想让配置尽可能的简单，就像老师这样，两端都是使用 web 方式来传送数据。

```java
# 链路追踪
  zipkin:
    discoveryClientEnabled: true
    base-url: http://ZIPKIN-SERVER/
    locator:
      discovery:
        enabled: true
    # 以 http 上传数据到 Zipkin
    # WHY？ bus 依赖项导入了 rabbitmq 的依赖项，Zipkin 会默认使用 rabbitmq,所以改成 web 然后就是可以使用 http
    sender:
      type: web
  sleuth:
    sampler:
      probability: 1
```

```java
      <!--配置中心 + BUS 推送-->
        <dependency>
            <groupId>org.springframework.cloud</groupId>
            <artifactId>spring-cloud-starter-config</artifactId>
        </dependency>
        <dependency>
            <groupId>org.springframework.cloud</groupId>
            <artifactId>spring-cloud-starter-bus-amqp</artifactId>
        </dependency>


        <dependency>
            <groupId>com.imooc</groupId>
            <artifactId>foodie-auth-api</artifactId>
            <version>${project.version}</version>
        </dependency>

        <!--链路追踪-->
        <dependency>
            <groupId>org.springframework.cloud</groupId>
            <artifactId>spring-cloud-starter-sleuth</artifactId>
        </dependency>
        <!--ZipKin-->
        <dependency>
            <groupId>org.springframework.cloud</groupId>
            <artifactId>spring-cloud-starter-zipkin</artifactId>
        </dependency>
```


那怎么办呢？来这也有个办法，我们来到 application dev 当中找到咱 zipking 的配置，只要在这里小小的动一番，手脚在哪里呢？我们下面加一个配置叫 sender, sender  什么呢？ sender  type. 它的类型，我们给它指定成 web 那它表示以 HTTP 的形式上传数据到 zip king 那我这里再补充一下，为什么要这样做呢？ why 因为我们的 bus 依赖项，它会导入 rabbit MQ 的依赖项。如此一人，SIP king 会默认使用 MQ 的形式来传送数据。那经过咱这样一改，咱的 zipking 又可以去自由地收发数据了。那我们这一节要配置的三个模块都已经配置好了，接下来我们就把它挨个启动一番。


刚才咱已经启动了 authentication 的服务。那接下来咱把这个 user application 启动起来。在启动 user application 的同时，我们去找到网关层 gateway 也把 gateway 给启动起来。好你哪里在这里找到它的闷方法，我们给他来一发走。你 OK 那接下来我们就去尝试调用一个服务，让这个服务可以一键穿三。怎么说，就是说它先调用到 gateway 然后 gateway 在调用 authentication 的鉴权服务，最终通过了登录校验之后再转到 user 服务，来看一下这个链路是不是可以追踪到上下游的这三个服务。


那先转移到浏览器，我们来看一下当前都有哪些服务呢？好 find trees okay 我们这里看到，它总共有 9 条服务调用链路。（我这里 6 条)

[image](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/98fe18bf-2031-4f09-bda2-85d4b68e8811/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TO7CXWGX%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T225805Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCW7lPn6yfibVN4UyaLW413F5hzxMiyD7eCTwJtuGz3eQIhAMuoiOMhS1asqFPvTQhiIFCWe1ww65N6jcrt67E0Fo89KogECMb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1Igy1kQGXQkBYFK0J0b8q3AOFhsOjpFyafau9%2FCCKspmyM8hybQ1byRfJZP3OVLK6POmQH2cHfn062iLmzKw%2FNEqK3aGizo3XQqEfOZzqSS%2FvejbjEh75xKrfcbbrkZUsbWhS9P0obJCx0lkSq%2F9ZNowfVv%2FYL7lHEOz%2By9I%2FWhBr4%2BQpP0zTAtj1%2BRblxkNYvQ5eT0wERGJxiNaz8xXK3BHBQZjY%2FxOIXjXrrskc3XymUmP05R9hRn6M0FrzZFieN1Vqss5N75%2Bn47mxhDD7L%2BBshGdpiddE61TS6a2SJFN%2FUK8nPwuRbfH7%2B1cXvz5QUJCdF4P9B3Zq8TyRsy6KvFlpfl6Cb2jXxUBfivwrM1aftlNNqO%2B6R8ldxLk%2Bw2AohNhdwhaB9mDLYAu8VFYUsFzY8P7xcmvIreddJEDtVy57ovrrUErLtBcdmk37p9DzXPRHzIM0%2BjjRHDzl5p4nyUlWaMsBW%2BBewGeBJrKTcqTuKuVmuXquOpv9bUF2UhNc9pT3mB3X3KcYwMJTWRR8QMuHmNin0TEnLUliaEVIZCCFgqn%2FHGiNd2xDOYYhssx7D2HgkoYMraWgG1%2FltQKvvyXwAMdX2sqp47JdviVcus%2BrHth1Bo5qmnXiRJj71Qo8SkC5niadK39T3A%2BHRTDxt%2F%2FSBjqkAetoCdaSDtjcRdeV1IGWra5RmVlwUrx98pPqQ0kqx86NjaYwx5HSDhom7EQDzyU1GMCT%2Fw%2F1aa%2BAohfpOVkL8IPrp8ecUs%2BhkhoEwQ9rs7rhVmNN0Ig8gU%2FddeZg1BQ245Z4S0U5FDCRne%2FJgu84ixoj37X%2BiP7NL9CAwyzSgiOQZYS2Z%2BeLC1S4my1%2BB%2FvWAnnRQHq2Bmhw%2BiACgO5Q5ocrI9Gb&X-Amz-Signature=c492106702049fb2190706a43d0a0d4a5cb1820f04e11842f280c3d46601833f&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

那我们接下来要去转移到 postman 去发起一个真实的调用。好，我这里发起哪个调用呢？我把调用发送到 local host 20,004，也就是网关层调用哪个服务调用咱的用户地址模块的服务，所以它的后面的路径是 address 杠 list 后面跟着 user ID 不过我在这个用户微服务的这个调用请求里，我加上了一个 header authorization 还有 IMock user ID 那这两个都是互相匹配的，是我刚才调用咱的登录鉴权服务生成的一个 token 好，我们这里点击一下 send 走。你 OK 那它这里返回了一个200，说明调用已经成功了，接下来再回到浏览器当中去看一下。


那这里是 9 个服务，我们再点一下 find 看是不是会多出一个。果然你看多出了一个服务，这个服务不出意外，就是上面的这一个调用链路最长的服务了。你看它这里显示有三个 span 我们点进去看一眼。好，你看它这里分别列出了这三个 span 的顺序，那我把屏幕放大一些。

[image](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/9e11cb0e-7036-4299-90fa-601e56162b99/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TO7CXWGX%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T225805Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCW7lPn6yfibVN4UyaLW413F5hzxMiyD7eCTwJtuGz3eQIhAMuoiOMhS1asqFPvTQhiIFCWe1ww65N6jcrt67E0Fo89KogECMb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1Igy1kQGXQkBYFK0J0b8q3AOFhsOjpFyafau9%2FCCKspmyM8hybQ1byRfJZP3OVLK6POmQH2cHfn062iLmzKw%2FNEqK3aGizo3XQqEfOZzqSS%2FvejbjEh75xKrfcbbrkZUsbWhS9P0obJCx0lkSq%2F9ZNowfVv%2FYL7lHEOz%2By9I%2FWhBr4%2BQpP0zTAtj1%2BRblxkNYvQ5eT0wERGJxiNaz8xXK3BHBQZjY%2FxOIXjXrrskc3XymUmP05R9hRn6M0FrzZFieN1Vqss5N75%2Bn47mxhDD7L%2BBshGdpiddE61TS6a2SJFN%2FUK8nPwuRbfH7%2B1cXvz5QUJCdF4P9B3Zq8TyRsy6KvFlpfl6Cb2jXxUBfivwrM1aftlNNqO%2B6R8ldxLk%2Bw2AohNhdwhaB9mDLYAu8VFYUsFzY8P7xcmvIreddJEDtVy57ovrrUErLtBcdmk37p9DzXPRHzIM0%2BjjRHDzl5p4nyUlWaMsBW%2BBewGeBJrKTcqTuKuVmuXquOpv9bUF2UhNc9pT3mB3X3KcYwMJTWRR8QMuHmNin0TEnLUliaEVIZCCFgqn%2FHGiNd2xDOYYhssx7D2HgkoYMraWgG1%2FltQKvvyXwAMdX2sqp47JdviVcus%2BrHth1Bo5qmnXiRJj71Qo8SkC5niadK39T3A%2BHRTDxt%2F%2FSBjqkAetoCdaSDtjcRdeV1IGWra5RmVlwUrx98pPqQ0kqx86NjaYwx5HSDhom7EQDzyU1GMCT%2Fw%2F1aa%2BAohfpOVkL8IPrp8ecUs%2BhkhoEwQ9rs7rhVmNN0Ig8gU%2FddeZg1BQ245Z4S0U5FDCRne%2FJgu84ixoj37X%2BiP7NL9CAwyzSgiOQZYS2Z%2BeLC1S4my1%2BB%2FvWAnnRQHq2Bmhw%2BiACgO5Q5ocrI9Gb&X-Amz-Signature=6138d70e5495bf2de792ce0ce44c840fb8c770c707a64d50a99ca497f069d3e4&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

第一个是 platform gateway 第二个，你看它这个页面显示还有些问题会有元素重叠。第二个是咱的福地 off service 那通过了 auth 检测之后，他才来到了 foodie user 这个上面列出了他所花费的时间 1.6 秒，然后调用了三个 service 它的层级深度是2，并且产生了几个 span3 个 spanok 那到这里，咱的 zip king 和 sleutha 就已经完整地集成到了这三个模块当中。


好，同学们看这里还有剩下的几个模块是 carter itemorder 还有搜索 search 模块。那这里老师也用同样的方式，把这剩下的几个模块都已经改造好了，比如它的 palm 里面加入了斯鲁斯的 zipkin 的依赖项，然后在 resources 里面的 application DEV 里面，把这个 zipkin 和 slutha 的配置给它加入进来。


同学们这里要特别留意一下，如果你的应用也使用了 buzz 要记得确保你的 zipking 发送端和接收端都可以使用 rabmq 作为通信中间件。或者我们就要在 zipkin 的配置项里面，把它的发送方式指定成web。 Ok. 那这一节的内容就到这里结束了，同学们可以去好好把玩一下 zip king 和 smooth 的顺带，锻炼一下动手能力，看能不能把咱的 zip king 改成基于 rab MQ 做通信。 Ok. 同学们，那这一小节到这里就结束了，我们下一个小节再见。


