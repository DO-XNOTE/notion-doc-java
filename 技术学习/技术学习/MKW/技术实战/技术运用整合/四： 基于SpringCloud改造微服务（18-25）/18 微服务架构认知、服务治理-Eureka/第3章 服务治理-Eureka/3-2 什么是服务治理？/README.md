---
title: 3-2 什么是服务治理？
---

# 3-2 什么是服务治理？

[image](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/2bf9656a-2e2e-4a74-99b9-a0ac07516d78/SCR-20240820-ojdg.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UMIDJ4MB%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T225529Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIGSCfcXKqUlNJxOfQVrKaFd%2B4bCBZalpLBaZGH5RCWo5AiEAzc7gNEgi6E1REsgqAhWBJEAmkFLF0lfja6x81FIZUawqiAQIxv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDL2h9RMUoyb5lHczXCrcA6dVhBQHZ5RIoJs%2FGIPALPkhI2zmf8B8HMmZhKrYc4kstn94UP4j%2BiGAqRizHPijVlgZlAEBAXXnUUeM%2FEbC9pjpDgtt8BT4cT4cTDA6qA%2Bo0E1ukGWQL15ZAgU0L%2B3h76%2BwVM9dqZfaEXe6JffPfPE9LyAN%2FXT3KWbJGZBZZhAjFcHBLXUQzqs4gNZIg1ZgJ4WYSeZD98V3gzPFJ1c37n1YfE91aG84UMAPYvZMJhsctu4MelQmoE7yB%2FptG%2Ff%2FjW%2FKjCwlqOAmOhGeI8GMGCCF4CyihOcwuX6HxXkaNn0bBjv0KrtpcmaQHcoXI9Cxhok0uy5%2F9VHKLDW5mc46pmfjqf3e2rH1sY71v1%2Ba7xGeDJyVfu7sGsKSFWiywMoc9RtyLrgZeCB4rGA%2BM4NzjiehIqGlzrTnlGlNGyqMjvDa%2FxFe0gFM488aSa93slCXIeI5A36KtZhta5XGxGBAZKpBexbU7Z5L1SS%2BPPDgzfF2VEedVksrAlctWUUzahh3pgNrB6i8Hmg0DWOTk5SGJXGFCGa1cLQvTf5Rw3HJ%2FWguej8CofKDJEZfGdGA4985Xl%2BwE8%2FnXeCMY%2FkM4BzJvDKBhrobGi64qL2fH4kyJXSO%2BhTiEcV4R%2BslfS1hMJ%2B4%2F9IGOqUB27PjBXnolAbCiJ%2BBu0K%2Fmg9uuJW6NnmBsMGPk%2FDb4KfMD3fVmQer88J96OKJmnpYpCLIrHuFs461zop%2BNJe0lixnaK3CuatN1a7OWXLyzPqjs308bxTRjuQ6D3OiaXw3TPMdh%2Fwh43v%2B3R0cXzoKNTVFaKAYYwRGlvj41vM6GiU5AFOGO0DugqfJdyuMBt9xIvLbSvc8YMkh3OAh9JByIv5po4Yo&X-Amz-Signature=fc204ccb9b4e0ed927a640145ce7531e28ac4ebd424d03539f339215729b53db&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

[image](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/64a535f1-aac4-4c79-aa4f-b4b7af68d07c/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UMIDJ4MB%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T225529Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIGSCfcXKqUlNJxOfQVrKaFd%2B4bCBZalpLBaZGH5RCWo5AiEAzc7gNEgi6E1REsgqAhWBJEAmkFLF0lfja6x81FIZUawqiAQIxv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDL2h9RMUoyb5lHczXCrcA6dVhBQHZ5RIoJs%2FGIPALPkhI2zmf8B8HMmZhKrYc4kstn94UP4j%2BiGAqRizHPijVlgZlAEBAXXnUUeM%2FEbC9pjpDgtt8BT4cT4cTDA6qA%2Bo0E1ukGWQL15ZAgU0L%2B3h76%2BwVM9dqZfaEXe6JffPfPE9LyAN%2FXT3KWbJGZBZZhAjFcHBLXUQzqs4gNZIg1ZgJ4WYSeZD98V3gzPFJ1c37n1YfE91aG84UMAPYvZMJhsctu4MelQmoE7yB%2FptG%2Ff%2FjW%2FKjCwlqOAmOhGeI8GMGCCF4CyihOcwuX6HxXkaNn0bBjv0KrtpcmaQHcoXI9Cxhok0uy5%2F9VHKLDW5mc46pmfjqf3e2rH1sY71v1%2Ba7xGeDJyVfu7sGsKSFWiywMoc9RtyLrgZeCB4rGA%2BM4NzjiehIqGlzrTnlGlNGyqMjvDa%2FxFe0gFM488aSa93slCXIeI5A36KtZhta5XGxGBAZKpBexbU7Z5L1SS%2BPPDgzfF2VEedVksrAlctWUUzahh3pgNrB6i8Hmg0DWOTk5SGJXGFCGa1cLQvTf5Rw3HJ%2FWguej8CofKDJEZfGdGA4985Xl%2BwE8%2FnXeCMY%2FkM4BzJvDKBhrobGi64qL2fH4kyJXSO%2BhTiEcV4R%2BslfS1hMJ%2B4%2F9IGOqUB27PjBXnolAbCiJ%2BBu0K%2Fmg9uuJW6NnmBsMGPk%2FDb4KfMD3fVmQer88J96OKJmnpYpCLIrHuFs461zop%2BNJe0lixnaK3CuatN1a7OWXLyzPqjs308bxTRjuQ6D3OiaXw3TPMdh%2Fwh43v%2B3R0cXzoKNTVFaKAYYwRGlvj41vM6GiU5AFOGO0DugqfJdyuMBt9xIvLbSvc8YMkh3OAh9JByIv5po4Yo&X-Amz-Signature=68a7f1440ad57310749a36d17552a12c8efb6643f475ba10f54fc9d7bd5db59c&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

**3-2 什么是服务治理？**

服务治理就像是白羊座宫殿，它是通向微服务架构圣殿的第一关，是所有微服务应用要考虑的第一个问题。本节将带大家深入浅出，从“提出问题-解决问题”的思路出发，让大家对服务治理领域的核心功能有个直观的感受。这就像相亲见姑娘的第一面，不求深入了解，但求心中有数，为后面的章节开一个好头。Let’s Go!

**服务治理的伟大目标**

服务治理这个名字乍一听很唬人，其实他很低调，能做的事情无非就是专治分布式系统各种不服。呦，你看这口气还挺大，既然牛已经吹出来了，那就先给自己定几个小目标吧！

高可用性:

 换成通俗易懂的说法就是**”当一只打不死的小强“**，在服务治理麾下的所有微服务节点，不论是被闪电击中还是被挖掘机铲断了电源，即使战至最后一个存活节点，服务治理框架也要保证服务的可用性。

分布式调用:

 微服务的节点通常散落在不同的网络环境中，大型互联网公司甚至会使用两地三机房或跨洲际机房做异地容灾。这就要求服务治理框架具备在复杂网络环境下准确获知服务节点网络地址（IP，端口以及服务名称）的能力。作为服务消费者，就可以借助服务治理框架的精准制导能力，向服务节点发起请求。一只穿云箭，千军万马来相见。

生命周期管理:

 万物都在轮回之中，在Spring的世界更是如此。微服务也把自己平凡而充实的一生，交给了服务治理框架，从服务上线、持续运行直到临终关怀，服务治理始终贯穿整个微服务生命周期。

健康度检查:

 微服务的节点都是任劳任怨的执行996，当然，如果一个节点因为任何原因不再能996的辛勤工作，那就不再是哥的兄弟了。服务治理框架要精准识别这些节点，将其从自己的兄弟会中剔除。

**实现目标要先解决问题**

目标和想法是美好的，但是现实里却没那么容易。为了实现这些小目标，我们必须解决眼前的几个大问题。

**四个问题（3W1H）**

假设我们把每个微服务集群比喻成一个武林门派，比如搜索服务就是“所罗门”，优惠券服务就是“卷莲门”，那么这个服务集群中的每个机器就相当于门下的一个弟子，而每个业务调用方就是一个前来踢馆的江湖高手。

中原武林浩如烟海，如何在茫茫人海中找到我想要挑战的那个人呢？服务治理框架，就是要帮这些踢馆的高手找到对应门派的精壮弟子进行切磋。在这个过程中服务治理要帮助踢馆高手翻过四座大山，实现最终目标，这就是四个需要服务治理框架来解决的问题，我们称之为3W1H。

图片来自于电影《羞羞的铁拳》，图片版权归属原作者

Who are you 作为服务治理框架，我如何知道中原武林各门各派的众弟子(服务提供者)的信息，这里面的信息是他们行走江湖的独一无二的标识，包含三个维度：a) 名号-敢问你的IP和端口是什么 b) 门派 - 报上你的服务名称 c) 身体状况 - 服务当前是可用or下线状态决定了你是能打还是不能打。

Where are you from 作为踢馆人（服务调用方），我如何知道这些武林人士（服务提供者）来自哪里？我又如何从服务治理框架手里拿到他们的地址，从而使我可以找到正确的人？

How are you doing 服务治理框架需要时刻甄别这些门派弟子的身体情况，一旦某个弟子断了气，就要做出相应标识，并告知踢馆人，以防别人走了冤枉路，找到了地方却找不见人。

When you die 有的门派弟子比较怂包，不敢应战，且主动请求下线。或者为了闭关修炼高级武功（系统升级重启），短时间内不在线，那么服务治理框架也要做出相应的回应，对主动下线的服务做清退处理。

**服务治理的解决方案**

为了解决前面提到的四个问题，服务治理领域祭出了六门独门武艺，用来解决这四个问题。在这一章节各位就当听个响，知道这些个武功路数的名称就好，后面的章节我们再来深入学习

Who are you - 服务注册 - 服务提供方自报家门

Where are you from - 服务发现 - 服务消费者拉取注册数据

How are you doing - 心跳检测，服务续约和服务剔除 一套由服务提供方和注册中心配合完成的去伪存真的过程

When you die - 服务下线 - 服务提供方发起主动下线

**寄语和展望**

自这节往后，大家将进入真正的Spring Cloud企业级开发的学习当中。也许现在的你是一张白纸般的学生，或是刚踏入Java领域的年轻人，又或是5年经验的老油条，总不会有10年经验的回锅老油条吧？！大家对Java，Spring或者Cloud应用或多或少有自己的理解和经验。在开始SpringCloud学习的时候，希望大家从心里和头脑里放空自己，把各种工作中学习中用到的框架暂且抛到脑后，让自己的思维像水一样浸润到SpringCloud的体系架构中，体会理解SpringCloud大道至简的设计理念。让这门课程带给你的不仅是一项技能（技），还有对系统设计、系统架构理念上的理解（术）。

学一门技术如同开始一门修行，在此我借用李小龙先生的一句话，与诸君共勉

放空头脑，似水不定，似水无形。引水入杯，即成杯形；倾水于瓶，即为瓶状；落入茶壶，即呈壶样。似潺潺流水，似湍湍急流，似水吧，吾友！



[image](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/2f13410d-27c1-4a9d-a1ac-5956912172f5/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UMIDJ4MB%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T225529Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIGSCfcXKqUlNJxOfQVrKaFd%2B4bCBZalpLBaZGH5RCWo5AiEAzc7gNEgi6E1REsgqAhWBJEAmkFLF0lfja6x81FIZUawqiAQIxv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDL2h9RMUoyb5lHczXCrcA6dVhBQHZ5RIoJs%2FGIPALPkhI2zmf8B8HMmZhKrYc4kstn94UP4j%2BiGAqRizHPijVlgZlAEBAXXnUUeM%2FEbC9pjpDgtt8BT4cT4cTDA6qA%2Bo0E1ukGWQL15ZAgU0L%2B3h76%2BwVM9dqZfaEXe6JffPfPE9LyAN%2FXT3KWbJGZBZZhAjFcHBLXUQzqs4gNZIg1ZgJ4WYSeZD98V3gzPFJ1c37n1YfE91aG84UMAPYvZMJhsctu4MelQmoE7yB%2FptG%2Ff%2FjW%2FKjCwlqOAmOhGeI8GMGCCF4CyihOcwuX6HxXkaNn0bBjv0KrtpcmaQHcoXI9Cxhok0uy5%2F9VHKLDW5mc46pmfjqf3e2rH1sY71v1%2Ba7xGeDJyVfu7sGsKSFWiywMoc9RtyLrgZeCB4rGA%2BM4NzjiehIqGlzrTnlGlNGyqMjvDa%2FxFe0gFM488aSa93slCXIeI5A36KtZhta5XGxGBAZKpBexbU7Z5L1SS%2BPPDgzfF2VEedVksrAlctWUUzahh3pgNrB6i8Hmg0DWOTk5SGJXGFCGa1cLQvTf5Rw3HJ%2FWguej8CofKDJEZfGdGA4985Xl%2BwE8%2FnXeCMY%2FkM4BzJvDKBhrobGi64qL2fH4kyJXSO%2BhTiEcV4R%2BslfS1hMJ%2B4%2F9IGOqUB27PjBXnolAbCiJ%2BBu0K%2Fmg9uuJW6NnmBsMGPk%2FDb4KfMD3fVmQer88J96OKJmnpYpCLIrHuFs461zop%2BNJe0lixnaK3CuatN1a7OWXLyzPqjs308bxTRjuQ6D3OiaXw3TPMdh%2Fwh43v%2B3R0cXzoKNTVFaKAYYwRGlvj41vM6GiU5AFOGO0DugqfJdyuMBt9xIvLbSvc8YMkh3OAh9JByIv5po4Yo&X-Amz-Signature=d0c8401e9a528d1a98357cffc908296a6e8b5d70f20f019bff88e348ecacee02&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

