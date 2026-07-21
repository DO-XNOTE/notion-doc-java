---
title: 2-1 本章概述
---

# 2-1 本章概述

[image](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/1c5ffcf3-ef80-4454-8560-8751f859fde6/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZRY2YDYU%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T231056Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIGSxnI88a8BXzme7%2B4hMuEmA1o0IjUuk8LE9YX7ijb24AiAuzCV4dpxZVwxy6Qp5p9iBqWZTqJZPZut%2FLD0M4oSpciqIBAjG%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMcIiGmoAHe%2BYTI2yNKtwDKxmkWmI8HjEyxny9j560sCU%2B4oqx7xA%2Fyf9b65JuHG0YoXU6lQql4Ge%2FLY5tjtdV5lm%2FO5g0JDTUWaOzg9yG2VvysXhj5MRGe8RJQPtYLi5JryhyDP3I8meO1q9oqC8s9wa3tCceJRLIlIPSRzLa7ykHBY2vwJq%2FTv94EU1p360P1x%2FW2MWFrRgAhSgqCFBuMG8VwbbAmpJwXCBYtVDHRTd0OPAq8QWA7MOdgymJSVVkUyPXXvZ9eIs0aNs2Vruvk4w73%2F9iQWwwSH%2BFwiV7ubub1WdsOUdILoE%2BMe5lkxG63MSqupIBV3yt%2B4F7bsnfIeja4Sn4kr7nJ2GZcjXYSDeHlmVorTpZJCFuD95wYy9K2iK3r0wof9c3i%2BvXP1OBMLL7LY6qNE71a8SiQe%2FzYIEU2jGBByPivtzB7ahn8nWCmGw%2FzRwLun0aDJ8BEbQCH0uipCV5GAYctKhlYVQD1V9pDYMQyQdH7tOczDjbXiBuS0enplNaAknANmKZ1wWwypYq5yb6aXB1f%2FEtzYxrA8R78shSuc4fe88%2BF%2FCCxISjRa3M6tbXFmc0H3ij6Fcnnq6DOERU8TGYoCe5LLkipxkKTInqmRMbh061RjMYhXdyysKhcDLJqNc%2BmiUwzbf%2F0gY6pgGDdPpc%2FH1YNIpd5hSvXJGMRUDEoRg8stfTztojzkoiWoVHhAdkhKBWL0PkkV9Ti%2FcB9kMiQI3yRR45kx%2FTNnwqKc3cVkEQwsS%2FSV%2B6P8gOVNGJlxol9XzBXdK%2F%2B5uNsa3%2FZPgZOuXpRlEpo97oqyRAseQ%2Fveb61PcWz%2FIFOGsWzuPl%2BTMEQV90BLXblPdmkZGwR%2FQtfV7yLdWzP%2F6HHvsY66FktSEC&X-Amz-Signature=dfb68c86d7fc2cef4f5f17d7ce2dc6b213031c1946fca945a1eefc771bdc5f18&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

```javascript
总结
会议讨论了云原生应用的相关内容，具体如下：
云平台分类与思考：云平台分类有从底层向上层的IAS基础架构云、Pas平台云及SaaS软件云，以及由内向外的私有云、公有云和混合云，还探讨了混合云的优点和难点。
云原生应用的定义：云原生应用并非简单地将应用容器化或使用Kubernetes编排，其概念远超于此。
云原生的15原则：冯阳老师将15原则分为CICD、弹性、解耦、中台四类，满足这些原则才能认为是好的云原生应用。
云原生应用的误区：不能认为Kubernetes代表容器化，也不能因容器化就认为是云原生，同时12个factor已过时，当前是15原则。
云原生与相关概念的配合：云原生具备持续交付等能力，与Devops、微服务、康威定律等概念相配合。
云原生的形象定义：云原生如同自助冰激凌，自助满足云的需求，试错成本低，能快速调整。



云原生应用概述：定义、15原则分类及相关探讨
本章节从应用开发角度聚焦云原生。先回顾上一章节云平台分类等内容，接着阐述本章将阐明云原生定义，重点探讨云原生的15原则。还提及12要素与15原则的关系会后续交流。为便于记忆，冯阳老师将15原则分为CICD、弹性、解耦、中台四类，满足这些原则可认为是优秀云原生应用 。
收起
01:51
云原生15原则：理论与实战助力代码向云原生转型
本章节探讨详细聊云原生 15 原则的原因。很多人盲目上云，对云原生理解片面，认为只是容器相关。章节将理论结合案例实战，理论上讲解 15 原则及满足方式，实战中用简单应用代码改造向云原生靠拢。旨在为大家提供代码转型思路，使其能轻松上云并在不同平台流转 。
收起
03:07
云原生概念及相关误区探讨：Kubernetes与12因素演进为15原则
本章节围绕云原生（cloud native）展开讨论，指出常见误区。强调 Kubernetes 只是容器化编排环节的一个产品，并非容器化的全部，编排工具众多。还提到有人认为满足 Heroku 的 12 个 factor 就是云原生，但因其提出于 2012 年部分描述已不精准，如今演变为 15 原则，部分精髓仍保留 。
收起
05:12
Cloud Native 与微服务：CICD、Devops 及应用拆分
本章节主要探讨云上关键能力。提到 CICD 是云上关键能力，能实现应用快捷、全自动化流程处理。还介绍了 Devops 概念，即一人完成微服务全生命周期管理，与 cloud native 配合。指出当下微服务是主流，企业应用服务在拆分，cloud native 能满足微服务需求，符合其范畴的应用应是微服务。
收起
06:45
Devops、康威定律与cloud native相关探讨
本章节围绕Devops相关内容展开讨论，指出康威定律能将微服务和Devops串联起来，涉及小组织完成业务全流程管理。还提到希望代码写成cloud native的样子以满足微服务，并提及康威定律、Devops和CICD持续交付。之后以飞亚老师心目中的自助冰激凌图来形象解释cloud native 。
收起
07:58
Cloud Native：自助冰激凌式的定义与后续原则展望
本章节以自助冰激凌类比 cloud native。自助意味着在云平台按需租赁资源，双方都不能违约，否则有惩罚，体现弹性和按需自助；冰激凌表示其试错成本低、能快速自愈且无三高问题。最后提到聊完定义后，接下来将介绍 cloud native 的 15 个关键原则，部分简称 CICD 相关原则。

```

起需求到落地的桥梁，构建 it 新蓝图。我是张飞扬，好，上一个大的章，我们提纲挈领地看了看云平台的分类和一些思考。那这个思考其实是什么？重理论后实践这个分类有两个方向，一个是什么？是从底层向上层 IAS 基础架构云、 Pas 平台云以及 SaaS 软件云。另外一种是什么？由内向外，从内部的私有云到外部的公有云，以及两者之间的混合云，同时我们花了很多时间来聊一聊混合云的优点以及它的难点。
那这个章节我们更偏什么应用开发的角度，有一个名词大家应该很熟悉，叫云原生，或者叫云原生应用。那我们这个章节就来聊一聊这个应用什么才是云原生呢？我们讲云原生定义之前，首先把本章概述 what why how，跟大家阐述一下，我们会尝试去阐明什么是云原生，然后重点聊一聊云原生当中的 15 原则。

[image](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/b4f8ff10-f20c-416f-b3f2-c7238fbbeb56/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZRY2YDYU%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T231056Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIGSxnI88a8BXzme7%2B4hMuEmA1o0IjUuk8LE9YX7ijb24AiAuzCV4dpxZVwxy6Qp5p9iBqWZTqJZPZut%2FLD0M4oSpciqIBAjG%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMcIiGmoAHe%2BYTI2yNKtwDKxmkWmI8HjEyxny9j560sCU%2B4oqx7xA%2Fyf9b65JuHG0YoXU6lQql4Ge%2FLY5tjtdV5lm%2FO5g0JDTUWaOzg9yG2VvysXhj5MRGe8RJQPtYLi5JryhyDP3I8meO1q9oqC8s9wa3tCceJRLIlIPSRzLa7ykHBY2vwJq%2FTv94EU1p360P1x%2FW2MWFrRgAhSgqCFBuMG8VwbbAmpJwXCBYtVDHRTd0OPAq8QWA7MOdgymJSVVkUyPXXvZ9eIs0aNs2Vruvk4w73%2F9iQWwwSH%2BFwiV7ubub1WdsOUdILoE%2BMe5lkxG63MSqupIBV3yt%2B4F7bsnfIeja4Sn4kr7nJ2GZcjXYSDeHlmVorTpZJCFuD95wYy9K2iK3r0wof9c3i%2BvXP1OBMLL7LY6qNE71a8SiQe%2FzYIEU2jGBByPivtzB7ahn8nWCmGw%2FzRwLun0aDJ8BEbQCH0uipCV5GAYctKhlYVQD1V9pDYMQyQdH7tOczDjbXiBuS0enplNaAknANmKZ1wWwypYq5yb6aXB1f%2FEtzYxrA8R78shSuc4fe88%2BF%2FCCxISjRa3M6tbXFmc0H3ij6Fcnnq6DOERU8TGYoCe5LLkipxkKTInqmRMbh061RjMYhXdyysKhcDLJqNc%2BmiUwzbf%2F0gY6pgGDdPpc%2FH1YNIpd5hSvXJGMRUDEoRg8stfTztojzkoiWoVHhAdkhKBWL0PkkV9Ti%2FcB9kMiQI3yRR45kx%2FTNnwqKc3cVkEQwsS%2FSV%2B6P8gOVNGJlxol9XzBXdK%2F%2B5uNsa3%2FZPgZOuXpRlEpo97oqyRAseQ%2Fveb61PcWz%2FIFOGsWzuPl%2BTMEQV90BLXblPdmkZGwR%2FQtfV7yLdWzP%2F6HHvsY66FktSEC&X-Amz-Signature=a239acd290aeb2a230fb3dcc295105abc413854627418639ff65d25177853dfb&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)


也许很多小伙伴说，我其实听说过一个叫是 twelve factor 12 要素跟 15 原则有什么关系诶？后面会具体来交流，大家敬请期待。这里先卖一个小关子。好，那这 15 个原则太多了，对吧？不容易记忆，所以冯阳老师把这 15 个原则分成四类，一类叫CICD，跟什么软件的发布相关的。那第二类弹性是跟什么应用本身的特质相关？第三类是解耦是什么？应用和应用之间的关系？第四类中台体现的是应用的一种对外服务的形式。
好，这样四类包含了 15 原则，满足 15 原则其实就能认为是一个很好的云原生应用了。那为什么要这样详详细细来聊？ 15 原则来聊云原生，这是因为什么？很多人盲目的上云，不是所有应用都适合云的，也不是所有应用都能叫云原生，而现在在市面上有个很不好的习惯，说到云原生就是容器，我只要把我一个 springboot 容器打包成，打包成一个Docker，或者是用 Kubernetes 1 编排，我就是云原生平台了。其实远远不仅于此，云原生的概念远远不止于容器，远远不止于Kubernetes。
好，那这一章我们希望也是理论结合案例实战。所谓理论就是要聊一聊 15 原则，讲清楚该怎么样满足这些原则，从而实现真正的云原生。所谓实战，我们会尝试拿一个很简单的应用代码看一看，把这套传统代码的结构的架构怎样改造，逐步向云原生靠拢，逐步去满足云原生的 15 原则。那希望通过这样一个课程能给大家一个思路，当你拿到原有的代码，或者说当你要去搭建一套新的系统的时候，如何尽量去向云原生转型，使得它能够轻松地上云，也使得它能够很普适地在不同平台轻松地、快捷地流转？好，废话不多说，我们来看一看到底什么才是飞扬老师心目中的云原生英文单词叫 cloud native，这个 cloud native 其实大家首先容易想到的什么？是不是用 Kubernetes 做容器化部署啊？这里要阐明几个误区，一个是 Kubernetes 不代表容器化，它只是容器化过程当中的一个编排环节的一个产品。容器化有很多，有容器本身的隔离，对吧？也有容器的编排，还有容器的平台管理等等。编排只是其中的一项，而编排工具也有很多，Mesosphere，Swarm，cloudfoundry， Kubernetes 等等等等。

[image](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/f0dcef21-e72a-44af-807f-6b250d3acc03/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZRY2YDYU%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T231056Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIGSxnI88a8BXzme7%2B4hMuEmA1o0IjUuk8LE9YX7ijb24AiAuzCV4dpxZVwxy6Qp5p9iBqWZTqJZPZut%2FLD0M4oSpciqIBAjG%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMcIiGmoAHe%2BYTI2yNKtwDKxmkWmI8HjEyxny9j560sCU%2B4oqx7xA%2Fyf9b65JuHG0YoXU6lQql4Ge%2FLY5tjtdV5lm%2FO5g0JDTUWaOzg9yG2VvysXhj5MRGe8RJQPtYLi5JryhyDP3I8meO1q9oqC8s9wa3tCceJRLIlIPSRzLa7ykHBY2vwJq%2FTv94EU1p360P1x%2FW2MWFrRgAhSgqCFBuMG8VwbbAmpJwXCBYtVDHRTd0OPAq8QWA7MOdgymJSVVkUyPXXvZ9eIs0aNs2Vruvk4w73%2F9iQWwwSH%2BFwiV7ubub1WdsOUdILoE%2BMe5lkxG63MSqupIBV3yt%2B4F7bsnfIeja4Sn4kr7nJ2GZcjXYSDeHlmVorTpZJCFuD95wYy9K2iK3r0wof9c3i%2BvXP1OBMLL7LY6qNE71a8SiQe%2FzYIEU2jGBByPivtzB7ahn8nWCmGw%2FzRwLun0aDJ8BEbQCH0uipCV5GAYctKhlYVQD1V9pDYMQyQdH7tOczDjbXiBuS0enplNaAknANmKZ1wWwypYq5yb6aXB1f%2FEtzYxrA8R78shSuc4fe88%2BF%2FCCxISjRa3M6tbXFmc0H3ij6Fcnnq6DOERU8TGYoCe5LLkipxkKTInqmRMbh061RjMYhXdyysKhcDLJqNc%2BmiUwzbf%2F0gY6pgGDdPpc%2FH1YNIpd5hSvXJGMRUDEoRg8stfTztojzkoiWoVHhAdkhKBWL0PkkV9Ti%2FcB9kMiQI3yRR45kx%2FTNnwqKc3cVkEQwsS%2FSV%2B6P8gOVNGJlxol9XzBXdK%2F%2B5uNsa3%2FZPgZOuXpRlEpo97oqyRAseQ%2Fveb61PcWz%2FIFOGsWzuPl%2BTMEQV90BLXblPdmkZGwR%2FQtfV7yLdWzP%2F6HHvsY66FktSEC&X-Amz-Signature=1417f2fbbd5f6ecbd6fc502ef9092888c77dd7f330d4d71caeb869c84f91a3e1&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)


Kubernetes 指什么？当前的当红炸子鸡，对吧？这个当红小生其实只是当前时态，将来时和过去时未必都是Kubernetes。所以不能一叶障目，不能因为 Kubernetes 就认为什么所有容器都只能用Kubernetes，也不能因为用了容器化，我们就认为所有云原生都必须容器化，云原生有它自身的真正的定位。
好，那还有一些同学说，嗯，盲人怎么石像？你看错了，你把大象当成柱子，其实大象是一个动物，它更像一条蛇，对吧？我摸到了什么？象的尾巴，那这个象的腿可能就是 Kubernetes 容器化。而象的尾巴就是什么 Heroku 的 12 个factor，这些 Heroku 的 12 个 factor 的支持者会这样说， cloud native 这个名词就是这家公司提出的，那当然是要以它为准了。所以只要满足 12 个factor，就是 cloud native，非安老师也要跟大家交流了。
12 个 factor 固然很不错，但是那是什么？ 2012 年的概念，到现在 2021 年，付阳老师录课的时候可是 2021 年了，中间过了 9 年了。 12 个因素其实有点淘汰了其中个别。因素的描述已经不太精准了，所以当前我们不叫它 12 因素，而叫它 15 原则，增加了三个原则，同时调整了一些基本的因素，到底哪些精髓仍然保留了呢？那我们来看一看哪些精髓呢？其中有一个就是CICD，那么持续交付、持续集成、持续部署、持续交付的能力，那这种能力是云上的一个关键能力，当你上云的时候是不是希望你的应用快捷？是不是希望你的应用能够全自动化地、流程化地处理？所以这种能力是什么？是 cloud native 本身必须具备除此以外 Devops 这样的概念是什么？是一个团队从头到尾，什么从开发到测试到部署到运维，什么一人可以完成整个微服务的全盘管理？这种一人以贯之完全生命周期管理的形态就是Devops，它也是跟 cloud native 非常配合的一个名词。
那刚刚我们已经聊到了微服务当前的世界，是吧？所有的应用服务其实是什么都在做拆分的，对吧？就是有合必有分，有分必有合，之前我们很多的企业都是在做什么？做意大利面大泥团，尝试用一套很复杂的大泥团完成整个企业的业务改造。那在当今这个时代最近的这十年其实在做什么？在做拆分。我们希望把所有的应用服务变成一个一个的小的微服务，然后让微服务之间通过服务治理、通过服务发现等等功能互相关联起来，最终体现出一种平台化的特质。所以当今的时代微服务是主流，而 cloud native 恰恰可以满足微服务的需要。同时我们也希望你的应用能够变成微服务，这样的应用才是属于 cloud native 的范畴。
除了这个 Devops 除了微服务还有什么？还有一个纽带性的内容，就是康威定律微服务要求我们把服务做得足够小， Devops 又要求我们个人就可以完成整个服务的从前到后的完整流程，那这个时候康威定律可以把这两个串联起来，足够小的服务就希望我们也有什么足够小的组织，而 Devops 里面刚好是小组织少数人数完成整个业务的全流程管理，是不是就串联起来了这样的一个组织，这样的一个服务，这样的一个发布流程？希望你的代码怎么写成 cloud native 的样子，就刚好满足了微服务。
康威定律， Devops 和 CICD 持续交付。好，那到底什么是靠native？似乎还是那么朦朦胧胧，还是那么不够清晰。我们用飞亚老师心目中的一张图来跟大家说，就是这张图看到了没有？冰激凌诶？冰激凌就是 call native，那什么样的冰激凌呢？自助冰激凌。说到自助大家会想到什么？自助火锅，对吧？自助什么？这种海鲜自助什么烤肉？其实还有一个自助叫自助冰激凌。


自助冰激凌这五个字我们先分开来看，左边两个自助暗含什么意思啊？你有什么需求，

[image](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/4d67857e-a9ce-45e4-bfb8-8dc4c26a3ccd/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZRY2YDYU%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T231056Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIGSxnI88a8BXzme7%2B4hMuEmA1o0IjUuk8LE9YX7ijb24AiAuzCV4dpxZVwxy6Qp5p9iBqWZTqJZPZut%2FLD0M4oSpciqIBAjG%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMcIiGmoAHe%2BYTI2yNKtwDKxmkWmI8HjEyxny9j560sCU%2B4oqx7xA%2Fyf9b65JuHG0YoXU6lQql4Ge%2FLY5tjtdV5lm%2FO5g0JDTUWaOzg9yG2VvysXhj5MRGe8RJQPtYLi5JryhyDP3I8meO1q9oqC8s9wa3tCceJRLIlIPSRzLa7ykHBY2vwJq%2FTv94EU1p360P1x%2FW2MWFrRgAhSgqCFBuMG8VwbbAmpJwXCBYtVDHRTd0OPAq8QWA7MOdgymJSVVkUyPXXvZ9eIs0aNs2Vruvk4w73%2F9iQWwwSH%2BFwiV7ubub1WdsOUdILoE%2BMe5lkxG63MSqupIBV3yt%2B4F7bsnfIeja4Sn4kr7nJ2GZcjXYSDeHlmVorTpZJCFuD95wYy9K2iK3r0wof9c3i%2BvXP1OBMLL7LY6qNE71a8SiQe%2FzYIEU2jGBByPivtzB7ahn8nWCmGw%2FzRwLun0aDJ8BEbQCH0uipCV5GAYctKhlYVQD1V9pDYMQyQdH7tOczDjbXiBuS0enplNaAknANmKZ1wWwypYq5yb6aXB1f%2FEtzYxrA8R78shSuc4fe88%2BF%2FCCxISjRa3M6tbXFmc0H3ij6Fcnnq6DOERU8TGYoCe5LLkipxkKTInqmRMbh061RjMYhXdyysKhcDLJqNc%2BmiUwzbf%2F0gY6pgGDdPpc%2FH1YNIpd5hSvXJGMRUDEoRg8stfTztojzkoiWoVHhAdkhKBWL0PkkV9Ti%2FcB9kMiQI3yRR45kx%2FTNnwqKc3cVkEQwsS%2FSV%2B6P8gOVNGJlxol9XzBXdK%2F%2B5uNsa3%2FZPgZOuXpRlEpo97oqyRAseQ%2Fveb61PcWz%2FIFOGsWzuPl%2BTMEQV90BLXblPdmkZGwR%2FQtfV7yLdWzP%2F6HHvsY66FktSEC&X-Amz-Signature=6fec7c376caee9ec81b21eed41719f3222239f64a2d9a4bcce1ddc3034cf9f7d&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

你就按照需求去吃就好了，对吧？但是吃的过程当中又要注意一点，什么不能浪费，是有惩罚的，那一样的道理啊。我们在云平台上，云平台是你有什么样的需要，就租赁什么样的资源，但是你不能够违约，是吧？用户不能够违约，云平台也不能违约，一旦违约就会惩罚。比如云平台说我号称对你提供 5 个9，如果没做到，那云平台就要罚钱给你，那你一样的道理，是吧？你答应好云平台每月付多少钱？结果月底不支付，那下个月就有罚金到手。对，这就是一种弹性，一种按需，最终就实现自助，你需要吃多少，你就可以什么享用多少。
除了自助以外，另外三个字，什么叫冰激凌？冰淇淋什么样特征啊？冰激凌是不是很小的一口，入口即化？它的试错成本非常低，如果你去吃一个火锅，虽然也是自助，我先吃一个什么辣锅，吃辣得不行了，我要换一个锅，可不可以啊？你可以在里面换肉，但是换锅好像是不是要额外收费了？同时你去吃一个什么海鲜大餐，或者是吃一个牛肉，当你咬下一口牛肉的时候，这不是我要的。但你发现什么？你切得太大一块，你扔掉你就什么，你就违约了，对吧？你就浪费了。所以你必须把这么大一块牛肉给吃掉。嗯，味同嚼蜡。
那冰激凌不一样哦？冰激凌你可以吃一个球，也可以舀一勺吃一口，发现这个巧克力味。不行，我换一个香草味，发现香草味不够爽口，我换一个抹茶味。是不是试错很快，同时能够自愈，吃起来很快捷？另外不会引起三高。所以 cloud native 就是费洋老师心中的自助冰激凌。首先自助满足云的要求，你需要什么我就给你什么，而且非常快，非常舒服，想吃就吃，想放就放，想换就换，这就是 cloud native 的什么？飞老师心目中的最终定义，自助b。冰淇淋好，聊完了 cloud native 的定义，下一节我们来看一看 cloud native 的 15 个关键性的原则，其中的某些原则，我们把它简称 CICD 相关原则大家敬请期待。

