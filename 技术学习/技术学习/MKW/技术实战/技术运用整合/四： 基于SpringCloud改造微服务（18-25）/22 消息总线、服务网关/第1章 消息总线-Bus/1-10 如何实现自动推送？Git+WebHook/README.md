---
title: 1-10  如何实现自动推送？Git+WebHook
---

# 1-10  如何实现自动推送？Git+WebHook

[image](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/546efa62-5b49-40c1-8c62-dd3b4d39d03f/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QXPRKRT6%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T225727Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDKPyyAOSkbLV20YeznfyGpceMNjL0eL3%2B8ZVsQVQ5xeQIhAJ59xxKiwkJtsT54%2FNzxJcR64eNwvVRq%2BflTnvIIAiQUKogECMb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgyGpFrkE1o7h9V94Acq3APKe3FKZdBOJqsteYstBExjGUDqvx3Esqdwgc5k8g1xg6rBTX%2FV3p4qDsyFDcC00mUuiRkNKfRRCodzUnlp67wA%2FhSMnvv5bVP8WBOMCoTLBYCW7kCjBWiFM62FVAxe8K%2BsIE7AIpZ8WgXw4FA8wLJ2pXL2aYDSaD7G%2Btftiwep5RDFSWTcddmKrH1M03GtiKnoyCumUDz4w8MHUC%2FKQ4TIgweAfRBaizix%2FHN4HDZLggtaMb%2FFWaV370UP%2BkuaUbRfpc%2F8gq6M%2FBnNaeviwmkNgRV0tnvd%2Fk%2FQTbZsT9Y77afSWrQWMb4eIuCOI2yKAMSMsSWfZvdhbSoppIvOh0QNqPut%2FJRVA%2BBUZK6LAqZ7Bbl8BVuA2XUPbviSokzBUDy%2BlVb%2BxUVSsqH%2B2UIfDpAijXfD56Dt7Wr9CuuZVbgSgEhvAw%2FOrr7sa3mWeTtxCDmxiCQkJHuHVttoWQ8vrPJMuVgiC5b0FCvrPDUgW78byjGA%2FG%2BEhbWJty7j18wUZ4CNucfMUJ16CClsxnsKsTM%2BXn55OeDbDj3Lr0B64u1CYDekVxT0MVYbNzXHr9P4GbuMShYIIIUyhq3Vd2zYuEKjKdazWbWN7onF8VBZ93RS9ejEMRuqIhJlUJMbDzCWt%2F%2FSBjqkAVo%2FmNcIqsv8CmDGdB0GTEtKANqzqBZtavAKhbWyxFNjHoHnLpWHl9eBS2Ov%2F6pslPl%2BpnHL1L1k2nKb8aJ3JvA0loJbPcU1UvJ2Y7SqxbsHdEOTbT68c3llYKzpQ0enGDGmq5jdLjHfT0L2UVydeInTjWK%2FqNl2wV9HeRqpBGrL5UdphTNXz6iqQA1PR1jpv3TeuYpdVouEbTzak5gb0lxu%2BaNb&X-Amz-Signature=2a666e0fef82b53bead83970611890a6735c27d9fbc8c04d1922d802a055984e&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

**1-10 如何实现自动推送？Git WebHook**

**如何实现自动推送**

前面我们深入了解了BUS的底层原理，我想是时候解决本章节开场时候提的一个悬而未决的问题了，那就是由谁发起状态变更请求。

这问题不是解决了吗，使用/actuator/bus-refresh 随便调用一台机器就好了。话是没错，可这调用不是还得人工来触发吗？要是哪天做了变更却忘了推送，岂不是会闹出问题了。相信自己不如相信机器，接下来让我们看看如何通过GitHub的Webhook机制实现自动推送。

**Webhook？**

有的同学在想了，老夫用了这么多年的GitHub，咋没听说过Webhook这号人物？这是个什么东东？从字面意思上看，是个什么钩子？就是海盗手上戴着的那个铁钩子？说对了一半，这确实是个钩子，不过不是海盗手上那个。Webhook这个词是由Jeff Lindsay在2007年在计算机科学hook项目第一次提出的，指的是一种callback机制，去增加或者改变web page或者web app行为的方法。对于Git来说，Webhook是Git的一种机制，可以用于自动化的构建。举个例子来说，当每次提交代码到Git以后，会触发Webhook执行一段程序，来完成预定义的操作，比如让钩子通知CI/CD系统从GitHub拉取最新代码开始执行构建过程，或者执行其他操作。在这个小节，我们将试着借助Git的Webhook功能，实现提交变更后触发Bus的自动刷新。

**Webhook三步走**

配置Webhook只需要三步：

设置encrypt.key

将上一步中的key添加到GitHub仓库设置中

配置Webhook url

首先我们来看第一步，设置encrypt.key。这一步和之前我们做属性加密解密的方式一样，只要在application.yml中设置一个key就好了：

encrypt:

  key: yourKey

接下来，我们登录自己的GitHub，进入存放配置文件的Repository目录下

点击右上角的“Settings”，然后在左侧列表栏中选择“Webhooks”，进入下一个页面后，点击右上方的“Add Webhook”。由于添加钩子是一个很敏感的操作，所以GitHub会要求你输入一遍账号密码进行确认。验证完成后，接下来就是设置Webhook的过程了。

在Payload URL里我们要填上bus-refresh的刷新地址（比如 [http://190.1.1.1:9000/actuator/bus-refresh](http://190.1.1.1:9000/actuator/bus-refresh) ），这里的IP地址大家不能再填localhost了，否则Webhook调用不到你的机器，这里必须是一个公网上可以访问到的IP，比如托管到云上并且可被外部访问到的服务器。Payload URL填好以后，接下来把第一步中的Secret添加到Secret一栏，点击Add Webhook就好了。

如果同学有在本地自己尝试的话，可能会碰到Webhook不起作用的问题，hmm，这还真是bus的一个bug，开源软件也是挺不靠谱的。亲，这里建议您先试着尝试自己解决一下。老师这里提供两个解决方案，看聪明的小伙伴是否能够得到启发：

声东击西：不直接调用bus/refresh，我们自己向外部提供一个简单的POST接口，让Webhook将请求POST到接口，然后再从这个接口内部调用bus/refresh

求助官方：这不，有的国外小伙伴也发现了同样的问题，还给官方提了issue，同学们可以参考这里的解决方案。[https://github.com/spring-cloud/spring-cloud-bus/issues/124#issuecomment-423960553](https://github.com/spring-cloud/spring-cloud-bus/issues/124#issuecomment-423960553)

**自动推送要注意的问题**

自动推送不是万能药丸，因此也要留意一下可能会发生的问题，比如万一发生异常状况：

无法测试：改动只要一提交就被推送到所有机器，假如不小心修改错了属性，那所有服务器就要团灭了

定点推送：尽管Bus支持在URL中添加目标范围，定向推送到指定机器，但毕竟URL在Webhook里面是写死的，不方便我们根据实际情况做定点推送所以在项目中我们还是需要根据实际情况，谨慎使用Webhook功能。

**小结**

这一节我们学习了通过Webhook自动推送Bus刷新请求，下一节我们讲一讲如果利用消息总线助攻其他业务场景。


*学习Tips*：我们小时候学写字的时候，常常通过临摹别人的字帖来练字，其实我们也可以通过这种方式来提高技术能力。Spring Cloud就是一套很好的字帖，当我们深入学习了底层原理之后，可以尝试着用自己的方式来实现一套相应的功能，写完之后再和Spring的原生组件做一下对比，看看同样的业务自己用的技术和Spring有什么区别，为什么Spring这套实现方式更好。当然了，这种“临摹”练习对个人技术是有相当高的要求的，但在开始阶段，我们可以尝试找一些简单的组件试一下（比如说Ribbon）。

[image](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/e2a5bee3-1aa9-4720-9c66-84bc3babca4e/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QXPRKRT6%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T225728Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDKPyyAOSkbLV20YeznfyGpceMNjL0eL3%2B8ZVsQVQ5xeQIhAJ59xxKiwkJtsT54%2FNzxJcR64eNwvVRq%2BflTnvIIAiQUKogECMb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgyGpFrkE1o7h9V94Acq3APKe3FKZdBOJqsteYstBExjGUDqvx3Esqdwgc5k8g1xg6rBTX%2FV3p4qDsyFDcC00mUuiRkNKfRRCodzUnlp67wA%2FhSMnvv5bVP8WBOMCoTLBYCW7kCjBWiFM62FVAxe8K%2BsIE7AIpZ8WgXw4FA8wLJ2pXL2aYDSaD7G%2Btftiwep5RDFSWTcddmKrH1M03GtiKnoyCumUDz4w8MHUC%2FKQ4TIgweAfRBaizix%2FHN4HDZLggtaMb%2FFWaV370UP%2BkuaUbRfpc%2F8gq6M%2FBnNaeviwmkNgRV0tnvd%2Fk%2FQTbZsT9Y77afSWrQWMb4eIuCOI2yKAMSMsSWfZvdhbSoppIvOh0QNqPut%2FJRVA%2BBUZK6LAqZ7Bbl8BVuA2XUPbviSokzBUDy%2BlVb%2BxUVSsqH%2B2UIfDpAijXfD56Dt7Wr9CuuZVbgSgEhvAw%2FOrr7sa3mWeTtxCDmxiCQkJHuHVttoWQ8vrPJMuVgiC5b0FCvrPDUgW78byjGA%2FG%2BEhbWJty7j18wUZ4CNucfMUJ16CClsxnsKsTM%2BXn55OeDbDj3Lr0B64u1CYDekVxT0MVYbNzXHr9P4GbuMShYIIIUyhq3Vd2zYuEKjKdazWbWN7onF8VBZ93RS9ejEMRuqIhJlUJMbDzCWt%2F%2FSBjqkAVo%2FmNcIqsv8CmDGdB0GTEtKANqzqBZtavAKhbWyxFNjHoHnLpWHl9eBS2Ov%2F6pslPl%2BpnHL1L1k2nKb8aJ3JvA0loJbPcU1UvJ2Y7SqxbsHdEOTbT68c3llYKzpQ0enGDGmq5jdLjHfT0L2UVydeInTjWK%2FqNl2wV9HeRqpBGrL5UdphTNXz6iqQA1PR1jpv3TeuYpdVouEbTzak5gb0lxu%2BaNb&X-Amz-Signature=bf6a1d148f570f785df9dcab0dd678709fa2d3891f15e5ca8d035d070d487b34&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)




## 


