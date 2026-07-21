---
title:  3-5 注册中心知多少？
---

#  3-5 注册中心知多少？

[image](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/39e8d0e9-acc3-409b-8941-53229abdf361/SCR-20240716-gufa.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665345FHSC%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T225533Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIHXeTrOEhjlec76M6ipatRkdmjPFiyDCj8uK3DJnkeC3AiEAieJA6a39RI0IpwpAPw8NJZmnbim5JL7qjexwnto1iCAqiAQIx%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDPRmBQ241ZI6MJ0%2F5SrcAwCdAJMuXYIgxw1PuuqRgllDokTt%2F0Eu9V%2F19ur4AcNbzea0mH1smZR46XtAbEWc91XAPp0CMj3oO9e9ZsPSdDzZJU1e6Pt%2FznC0yn%2FF43agxzWyC2nRWO3Q7ey74GCH%2BTGn1oN%2FhhaqnO%2Bwo%2Bh%2B163Ju2bb93l5Pu4268FNS%2BwSNbIWE%2FlR%2BMPeXp9DRkmh7IIrfcuf2TtYxKtcDsJxWNXlYsz%2FZfP94KW0gyZH3f2m2Cc8sqWKNKack%2FXbBVj6hK1S0LR3zsMouzY4SQB7XsGzAIVzhEeJqatnm2Gg8N%2BqXLHMRNwPZrmGdAkSAH8gM1fFWX1fBCyOtrdLBNH%2FtpqBC62zsNcYQssVpfDRBnJpZex%2Be5Ez6iIL2Kdsgw44e1EY9oj3ixgrXamRZHT%2B619tEvyJroOzIjRuPPFXnNtWz860Zr3L53Ft0icxIjcQkGMlojL2rCw29MFiNdZrnNUmGMCf7XMjinhckN1%2BmNENFAMAECpg5RDs1LX4OIPCWgC5lB64bOoK31W9KbSEl5QiOUZ1S%2BSuorerpXubRgfCGC%2Bx5jWMQP%2BsuSifm6KMu4pfJbJ7V%2BCQeyNM1NtrZL8vPjQr2EYP3tczj5xkh2vQ5c%2B%2FY3QRFpmKXatIMNbb%2F9IGOqUBRGvK2bN%2FQDRJGQ%2Fo6%2FqXp3P%2FtXaBkztVo19eIH%2BYxrHio0BzrwubSxF5BoYjX9%2F71DD%2BD5jt2Z8j8tPwXfBdlulz71ujv01iBHe5f41KghX2pFFuBAXx0P2KtSZqQg4xygNpovKfq5gKQl8ZCvvY52N9voe7yiB2omzFqFr7K41LnDTOgJ01frUZPzUwfCir4BCtQHhS0ZbSyLfJXv4kgI3q%2BlaA&X-Amz-Signature=d06de20f6c1726e0354dfeb85c7ebd9d05e832a6b93aca797655ba75258a84ce&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

**3-5 注册中心知多少？**

古人说好的开始是成功的一半，古人又说千里之行始于足下，服务注册就是服务治理这台戏的开场和第一步。这一节，将向大家介绍注册中心的运作模式、任务，以及服务节点是如何找到注册中心的。

**注册中心漫谈**

前面我们讲到，服务注册是为了解决Who are you这个问题，即获取所有服务节点的身份信息和服务名称，从注册中心的角度来说我们有以下两种比较直观的解决方案:

三顾茅庐 由注册中心主动访问网络节点中所有机器

等待戈多 注册中心坐等服务节点上门注册

大家来思考一个问题，为什么目前主流的注册中心都选择第二种方案，而不是第一种呢？那我们先来看看三顾茅庐的方式有哪些弊端

图片来源自《三国演义》，原作者享有版权

模型复杂：网络环境浩如烟海，轮询每个节点的做法通常是注册中心发局域网广播，客户端响应的方式，这种方式就像你对着全世界喊我爱你，顿时感到有种无力感。现实中对于跨局域网的分布式系统来说，响应模型更加复杂

网络消耗大: 整个网络环境里会掺杂大量非服务节点，这些节点无需对送达的广播请求做出响应，这种广播的模式无疑增加了网络通信成本。

服务端压力增加: 不仅要求注册中心向网络中所有节点主动发送广播请求，还需要对客户端的应答做出响应，一个担子两头挑。考虑到注册中心的节点数远远少于服务节点，我们要尽可能地减轻服务中心承载的业务。

那么对于Eureka来说，他又会选择哪种服务注册方式是呢？

**等待戈多**

等待戈多是爱尔兰现代主义剧作家Samuel Beckett创作的荒诞派戏剧，整场戏只有两幕，两个流浪汉驻足在同一棵树下做一件事“等待戈多”，他们对戈多一无所知，戈多是谁？戈多住在哪里？戈多现在情况怎样？这些问题都没有答案，只有在戈多到来之后才能一一揭晓。

Eureka的服务注册就采用了这样一种“等待戈多”的注册模式。注册中心就像这棵老树下的流浪汉，我们的服务节点就像一个个的“戈多先生”。流浪汉不去搅扰其他的“哥多”、“哥少”先生，只静静等待那些真正的“戈多”来到他们面前，听戈多讲述自己的故事。

要说这种模式带来的好处那是相当的多

省心 对于网络中其它非服务节点来说不会产生任何无效请求

省时 省去了广播环节的时间，使注册效率大大提高

省力 节省了大量网络请求的开销

大家通过后面的学习会发现，不仅在服务注册方面，在其他服务治理的环节中，SpringCloud对注册中心可谓是优待有加，只接受服务节点上门服务，绝不主动出门联系。这便是SpringCloud大道至简的智慧所在，任何复杂的问题到了这里，都会通过最简单、最经济的方式来解决。

同学们你们一定还有个疑问，为什么我不使用守株待兔这个比喻，而使用等待戈多？那是因为后面一个高端大气上档次啊（语重心长.gif）

**注册中心的日常任务**

当我期盼的戈多到来了以后，他会告诉关于他的三件事情

他会的技能（所提供的微服务是什么，比如“洗剪吹”）

他住在哪里（IP地址+端口）

他的状态（通常注册完成时的服务状态就是UP）

在等待戈多的过程中，其实这两位流浪汉也没有那么闲，他在空余时间还是干了两件微小的事：

心跳检测和服务剔除 已经注册过的戈多们，会时不时来跟我打声招呼（心跳检测），如果隔段时间没见着他们了，我就只好从注册名单中把他们删除（服务剔除）。

注册信息同步 我们两个流浪汉分别接待不同的戈多，有的戈多在我这里注册，没有在他那里注册。我抽空就会把我这里的戈多名单和他做分享。

**戈多报道指南**

在茫茫世界中游荡的戈多，是如何找到流浪汉去报道的呢？当然是靠着我们开发人员作为上帝视角预先告诉了他们流浪汉的地址，这个地址包含了三个维度的信息，分别是Region, Zone和URL。

Region代表地理上的分区，而Zone则是这个分区下的机房。大多数情况下我们的配置中心只存在一个机房，这时配置URL就好了（比如http://localhost:20000/eureka/），这是注册中心的IP地址，同时Eureka会为我们指定一个默认的Region和Zone。某些情况下当开发人员主动指定了注册中心的region和zone，比如在多机房的网络环境中，我给上海机房的注册中心指定了region=east_china, zone=sh，这时候服务节点的配置文件就会有一些不同了，在稍后的demo中会讲到。

知道了地址以后，戈多也要准备下见了面告诉流浪汉什么，那就是：我会提供什么服务 spring.application.name=xijianchui

我住在哪里 - 物理地址如localhost:10000。还有很多絮絮叨叨的琐事，比如instanceId,leaseInfo以及等等，大家就一看而过吧

**小结**

在这节中，我们学习了以下内容

Eureka的注册模式（等待戈多）

服务节点注册信息包含的主要内容

注册中心的技能树（服务注册，心跳检测，服务剔除。 P.S. 注册中心还有其他技能加点，先不告诉你）

接下来让我们搭建一个自己的注册中心。



[image](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/89f07d1b-9964-44e3-a732-150e254beff3/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665345FHSC%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T225533Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIHXeTrOEhjlec76M6ipatRkdmjPFiyDCj8uK3DJnkeC3AiEAieJA6a39RI0IpwpAPw8NJZmnbim5JL7qjexwnto1iCAqiAQIx%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDPRmBQ241ZI6MJ0%2F5SrcAwCdAJMuXYIgxw1PuuqRgllDokTt%2F0Eu9V%2F19ur4AcNbzea0mH1smZR46XtAbEWc91XAPp0CMj3oO9e9ZsPSdDzZJU1e6Pt%2FznC0yn%2FF43agxzWyC2nRWO3Q7ey74GCH%2BTGn1oN%2FhhaqnO%2Bwo%2Bh%2B163Ju2bb93l5Pu4268FNS%2BwSNbIWE%2FlR%2BMPeXp9DRkmh7IIrfcuf2TtYxKtcDsJxWNXlYsz%2FZfP94KW0gyZH3f2m2Cc8sqWKNKack%2FXbBVj6hK1S0LR3zsMouzY4SQB7XsGzAIVzhEeJqatnm2Gg8N%2BqXLHMRNwPZrmGdAkSAH8gM1fFWX1fBCyOtrdLBNH%2FtpqBC62zsNcYQssVpfDRBnJpZex%2Be5Ez6iIL2Kdsgw44e1EY9oj3ixgrXamRZHT%2B619tEvyJroOzIjRuPPFXnNtWz860Zr3L53Ft0icxIjcQkGMlojL2rCw29MFiNdZrnNUmGMCf7XMjinhckN1%2BmNENFAMAECpg5RDs1LX4OIPCWgC5lB64bOoK31W9KbSEl5QiOUZ1S%2BSuorerpXubRgfCGC%2Bx5jWMQP%2BsuSifm6KMu4pfJbJ7V%2BCQeyNM1NtrZL8vPjQr2EYP3tczj5xkh2vQ5c%2B%2FY3QRFpmKXatIMNbb%2F9IGOqUBRGvK2bN%2FQDRJGQ%2Fo6%2FqXp3P%2FtXaBkztVo19eIH%2BYxrHio0BzrwubSxF5BoYjX9%2F71DD%2BD5jt2Z8j8tPwXfBdlulz71ujv01iBHe5f41KghX2pFFuBAXx0P2KtSZqQg4xygNpovKfq5gKQl8ZCvvY52N9voe7yiB2omzFqFr7K41LnDTOgJ01frUZPzUwfCir4BCtQHhS0ZbSyLfJXv4kgI3q%2BlaA&X-Amz-Signature=e748cdc24cd800a3e3362dda636d8460d5935d7cca51dac2b350500688c91b24&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)


