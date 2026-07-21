---
title: 3-18+服务自保-心法总决
---

# 3-18+服务自保-心法总决

[image](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/0041cb9f-5186-4f0e-ba74-7b247204c134/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466V5ZZWI6H%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T225547Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIEFhm%2BdlGcgvFHP2nIv5WWViVneh0JaYD%2F31vw4%2B0kdCAiEA163QcT%2FqbMulEqP3512azLhe55x7LRuHd%2B2U%2BSPhUqUqiAQIxv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDElKwbcsa6s%2BUx%2B%2BICrcA7UEdh7d77FtDKOhCkh70y2HnqmRXHd939mbC2RGEKMH64vijDI%2FCcJ5zNq%2FV%2BEiEcs0jgnhrY66Ce727QUb3CpIKKGs%2FiymGT%2BL923anBzj8Jwc%2BcgPkRw7o9AcD6pxx3b51baQ13QGp2UzuEidtsYObBgpShS6rK%2FSKoTNefuzuEP2IKRYQ8at0GTdURidfGATYqlnTq%2B63yIj58oWDJd5EFmX8VxsMLNelawRidWsE4F8%2BwIKoYUycJ9sg0Z8uHtsyyKC2U5ahhDmtFQFdxMkEaRa%2Fxsx6TZCZMYOj2VomFvPUcfkPWmZ6ylW0SrN2hlOAEq1G9puadu%2BbA2%2BiIF7Kt1ttvmQmqf7ba1%2BxzYgfeshIy93OJ0c770KN%2F6oQSoEvtpTGqzAGI0B6qpdDg6fSR0vkFaoEjibxOMCakwOGMh9jHGS7xQ60ZSYlv5ovjEaeWqhIYlg7nBS2TYX%2BEGjgHT5OXmOJ4mSTrQ6dUESZt31LuCvT2xfUBDfEDQV6vcgAgZsdKAKYmhuk0BJ433cH72BmBbJIbuyyaszmEjMzsp7WRYheWsxV870ZGwl1nBktHiBpZEAJAu8tQXY9gSmHC0ZdVEpzNoRHqPuGJNt%2F4XZ8DytFBfZxEIkMKK4%2F9IGOqUBjJxD3r2cQAdlZmCm%2FAOGOrk94GphzmXo8Q5mjU%2BWWoOkoC%2B34jzEQNZBTTFD3flNd5ceuiRKuubzH2wmMmwCSRHT0qgWST2WK3Uu1K1N1UCPRByYyGkj6N1ei98waBJQSo2X9CTUvrt2U8KSW2YyBn%2FDjoYRHSVljnu8QaIm5UyqvjHGOwTv67nyokIQUlR7B7RpQHrJqnVyvg3Q6sJQs18kYq7d&X-Amz-Signature=051122190b58c7f61470fa1e009d01e47f5c7662f490ecac96d05ac2767c37b9&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

**3-18 服务自保-心法总决**

**服务自保**

服务剔除，服务自保，这两套功法一邪一正，俨然就是失传多年的上乘心法的上卷和下卷。但是往往你施展了服务剔除便无法施展服务自保，而施展了服务自保，便无法施展服务剔除。也就是说，注册中心在同一时刻，只能施展一种心法，不可两种同时施展。

**心法总决**

服务剔除 把服务节点果断剔除，即使你的续约请求晚了一步也毫不留情，招式凌厉，重在当断则断，忍痛割爱。心法总决简明扼要：

欲练此功，必先自宫

服务自保 把当前所有节点保留，一个都不能少，绝不放弃任何队友。心法的指导思想是，即便主动删除，也许并不能解决问题，且放之任之，以不变应万变。心法总决引人深思：

宫了以后，未必成功

如果不宫，或可成功

在实际应用里，并不是所有无心跳的服务都不可用，也许因为短暂的网络抖动等原因，导致服务节点与注册中心之间续约不上，但服务节点之间的调用还是属于可用状态，这时如果强行剔除服务节点，可能会造成大范围的业务停滞。

由此可见，这两套心法都是各走极端，只有相互搭配使用才能中和。大家用心体会就好，至于心法还是不要去身体力行照着修炼了。

**服务自保的触发机关**

服务自保由两个开关进行控制

**自动开关**

相信这几天同学们对注册中心的Portal已经很熟悉了，你们有没有注意到页面上出现了这么一行大红英文：

EMERGENCY! EUREKA MAY BE INCORRECTLY CLAIMING INSTANCES ARE UP WHEN THEY’RE NOT. RENEWALS ARE LESSER THAN THRESHOLD AND HENCE THE INSTANCES ARE NOT BEING EXPIRED JUST TO BE SAFE.

这就是服务自保开启后的警告，意思是说，挂掉的服务有可能会被错误的当做UP，（在一定时间内）续约成功的节点个数占已注册总服务的比值，已经低于限定值，因此所有节点都不会过期，服务自保开启。

这是一个服务自保的自动触发开关，简单来说，服务自保机制会检查过去15分钟以内，所有成功续约的节点，占所有注册节点的比例，如果低于一个限定值（比如85%）就开启服务自保模式。

服务自保模式往往是为了应对短暂的网络环境问题，在理想情况下服务节点的续约成功率应该接近100%，如果突然发生网络问题，比如一部分机房无法连接到注册中心，这时候续约成功率有可能大幅降低。但考虑到Eureka采用客户端的服务发现模式，客户端手里有所有节点的地址，如果服务节点只是因为网络原因无法续约但其自身服务是可用的，那么客户端仍然可以成功发起调用请求。这样就避免了被服务剔除给错杀。

**手动开关**

这是服务自保的总闸，以下配置将强制关闭服务自保，即便上面的自动开关被触发，也不能开启自保功能

eureka.server.enable-self-preservation=false

**小结**

本节带大家学习了关于服务自保的作用，以及控制开关。接下来，我们带大家手把手的做一番配置，体验一下心跳、续约、服务剔除和自保的整套流程。


[image](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/722f1e3e-08f5-4a01-864c-7729cf44ba69/2020-09-17_051826.jpg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466V5ZZWI6H%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T225547Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIEFhm%2BdlGcgvFHP2nIv5WWViVneh0JaYD%2F31vw4%2B0kdCAiEA163QcT%2FqbMulEqP3512azLhe55x7LRuHd%2B2U%2BSPhUqUqiAQIxv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDElKwbcsa6s%2BUx%2B%2BICrcA7UEdh7d77FtDKOhCkh70y2HnqmRXHd939mbC2RGEKMH64vijDI%2FCcJ5zNq%2FV%2BEiEcs0jgnhrY66Ce727QUb3CpIKKGs%2FiymGT%2BL923anBzj8Jwc%2BcgPkRw7o9AcD6pxx3b51baQ13QGp2UzuEidtsYObBgpShS6rK%2FSKoTNefuzuEP2IKRYQ8at0GTdURidfGATYqlnTq%2B63yIj58oWDJd5EFmX8VxsMLNelawRidWsE4F8%2BwIKoYUycJ9sg0Z8uHtsyyKC2U5ahhDmtFQFdxMkEaRa%2Fxsx6TZCZMYOj2VomFvPUcfkPWmZ6ylW0SrN2hlOAEq1G9puadu%2BbA2%2BiIF7Kt1ttvmQmqf7ba1%2BxzYgfeshIy93OJ0c770KN%2F6oQSoEvtpTGqzAGI0B6qpdDg6fSR0vkFaoEjibxOMCakwOGMh9jHGS7xQ60ZSYlv5ovjEaeWqhIYlg7nBS2TYX%2BEGjgHT5OXmOJ4mSTrQ6dUESZt31LuCvT2xfUBDfEDQV6vcgAgZsdKAKYmhuk0BJ433cH72BmBbJIbuyyaszmEjMzsp7WRYheWsxV870ZGwl1nBktHiBpZEAJAu8tQXY9gSmHC0ZdVEpzNoRHqPuGJNt%2F4XZ8DytFBfZxEIkMKK4%2F9IGOqUBjJxD3r2cQAdlZmCm%2FAOGOrk94GphzmXo8Q5mjU%2BWWoOkoC%2B34jzEQNZBTTFD3flNd5ceuiRKuubzH2wmMmwCSRHT0qgWST2WK3Uu1K1N1UCPRByYyGkj6N1ei98waBJQSo2X9CTUvrt2U8KSW2YyBn%2FDjoYRHSVljnu8QaIm5UyqvjHGOwTv67nyokIQUlR7B7RpQHrJqnVyvg3Q6sJQs18kYq7d&X-Amz-Signature=5eb528a7b9375d1628bfdb89a2c842f0ae3d8fdf689f0d96b57bca7b81d4f954&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)




