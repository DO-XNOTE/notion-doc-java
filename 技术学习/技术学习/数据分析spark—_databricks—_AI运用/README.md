---
title: 数据分析spark—>databricks—>AI运用
---

# 数据分析spark—>databricks—>AI运用

[image](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/0786d9aa-bd1b-4f72-bc47-0b33dd58ffff/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466X5Z6NANF%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T234418Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIAOB%2BDJM809cJzJx6W2XBmWnJBj1a2c3u5LZLdDeTFKkAiAHnPF%2FJgpumSwio643jZgHkmQJA8wHOfpxKIiTsxx5myqIBAjG%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMMbosq7Y7mrefrdE%2FKtwDXcDh4u%2Fty9X8Q9EVOMGJm%2F4iyPdFiQzcyFG5P23JL1O9YTj9QF4CZyA0suFM38csKgUUxjp2wpOAxXsqe7PJQAdyCgxsMCQrrdw9xe0LKIhBOJkAqOfX6O38dClrAwX7PUR3g%2BxL28uPd16zp4lKJjvUW%2BRggSlINTl8%2ByvHpn797cAcjyMgIgyyu06Xb1qlmEKFoaNhGO%2Fu7C6De6G52ZRxgIxxIIhh684HE3uZ%2FCE8DNlAz507t%2FnHLhB6DkdinKZryGieHsn6mNNEZaSYAzrVlTvi%2Fi3y5bKHpdnuqqSifR4IRf6SojjxlBRx6uWOgjQpH718Oiq7Y3c1BfVsVvdLZOh7s7uGiM%2FA%2By1N0%2FfcJ7dncCEz4niUzF7azLRossDBPMkoDyZaJQ9JNvMcw1SsKs6kiSctDo6e2034hhShg%2FTyn4jSAJUq%2Ba3mUQdhNvudGvGj%2Bt0lL4LLqnR%2F2r1a%2FqnBAE3rfMDOPl6fJg5NwRTYDYK9n6UwVic8GhqpiTMzAhoJ%2BmLSuqegG0QS%2BE1gISbxgVSxyzHz8e4K%2FfPp12RELYkdw2PaafzVNKVjVobgL8wUf%2BfY6Cwv%2BGn8vAFVj4jG8NBiVCYXVcm%2BxrcYlth74bptxhL5TzAw%2Fbn%2F0gY6pgHJ1%2BC5btVGpRAld5B986y7KIsWamntZlzoPejfX3TusarwtgC72SGqla6l9TLm5%2FyB2P%2BnByfeGwp97fq3bTZzv%2B7q6d%2BIaoR5T6IudqyzXBaNKmc6pjVMYwuaKXnduTViMtB2yqhJD91s6MppJZyPdetIPRSJ7imrMxHE1%2B42vMvTL7UjMt%2F3v8yCH0QqRpf1L7MstRtfwr8fuLJblYprt1GSoVUj&X-Amz-Signature=779977e7ef929bda632f4c1b5f3432f99bbb1e0ace9adda56ed66dc06e96b226&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

```shell
# 【人工智能】AI会吞噬所有软件 | Databricks CEO 阿里·戈德西最新访谈 | 数据的重力 | Spark | MosaicML | Data Lakehouse | 企业级模型

#### 阿里·戈德西（Ali Ghodsi）的背景与经历
- **个人背景**
  - 出生于1978年伊朗伊斯兰革命期间
  - 5岁逃离伊朗，成长于瑞典
- **教育与早期经历**
  - 在瑞典接触计算机，学习Pascal语言
  - 2009年前往美国，在加州大学伯克利分校进行研究

#### Apache Spark的起源与影响
- **Apache Spark的定义**
  - 开源分析引擎，用于大规模数据分析
- **Spark的创立**
  - Ghodsi与同事在伯克利分校创造
- **Spark的影响**
  - 推动了数据和人工智能时代的发展
  - 解决了如Twitter等公司的数据处理问题

#### Databricks的创立与成长
- **Databricks的定义**
  - 商业化Apache Spark技术
- **创立背景**
  - 2013年，Ghodsi和团队因研究未受关注而创立Databricks
- **商业化过程**
  - 最初缺乏商业化清晰想法，逐渐发展出成功的开源策略
  - 2015年收入150万美元，与亚马逊等公司形成对比

#### Databricks的技术革新
- **性能优势**
  - Spark在数据处理性能上远超竞争对手
- **数据湖仓（Lakehouse）概念**
  - 结合数据湖与数据仓库的特点，提出新的数据存储解决方案

#### Databricks的市场定位与竞争环境
- **竞争对手**
  - 面临云服务商（微软、Google、AWS）和Snowflake等的竞争
- **市场策略**
  - 通过开源与云服务结合，以及对AI的支持，确立市场地位

#### Databricks的AI与大数据结合
- **AI应用**
  - 支持AI和机器学习，从Spark早期用例到自然语言处理的应用
- **Mosaic ML收购**
  - 收购Mosaic ML以强化大语言模型能力

#### 企业大模型的需求与应用
- **定制化模型**
  - 提供定制化大模型技术，满足企业特定任务需求
- **计算资源**
  - 强调云上GPU方案，避免与客户本地基础设施混合

#### 数据安全与隐私
- **数据重力**
  - 数据沉淀后难以移动，强调数据安全与隐私保护
- **客户信任**
  - 通过保证数据安全和隐私来获取客户信任

#### 全球市场与监管环境
- **亚洲与拉丁美洲市场**
  - Databricks在亚洲和拉丁美洲市场增长迅速
- **监管差异**
  - 中国和亚洲其他国家监管较少，发展快速；欧洲监管较多，发展相对落后

#### 创办公司的经验与教训
- **领导力**
  - 寻找并信任优秀领导者，与人建立信任
- **竞争策略**
  - 即使面对大公司，保持专注和正确战略也能取得成功
- **产品与市场**
  - 产品制造与市场推广同等重要，需和谐统一

#### 访谈总结
- **Databricks的成就**
  - 成为世界上最有价值的私营公司之一
- **未来展望**
  - 软件自上而下的垂直化，AI重写所有SaaS，Databricks支持AI从成立之初

#### 梳理总结
- 通过对访谈内容的详细梳理，我们可以看到Databricks在阿里·戈德西的领导下，如何从一个学术项目发展成为全球领先的数据分析公司。
  公司通过技术创新，如Apache Spark和数据湖仓概念，以及对AI的早期支持，成功地在竞争激烈的市场中确立了自己的地位。
  同时，Databricks面临的挑战包括来自云服务商和其他竞争对手的压力，以及数据安全与隐私的保护。
  在全球市场，尤其是在亚洲和拉丁美洲，Databricks持续增长，展现了其强大的市场适应能力和技术实力。
  戈德西分享的创办公司经验强调了领导力、竞争策略和产品市场的重要性，为其他创业者提供了宝贵的参考。
```

[https://youtu.be/WV16tG3ktbU](https://youtu.be/WV16tG3ktbU)

```shell
大家好，这里是最佳拍档，我是大飞今天给大家分享一篇知名博客Stratechery
对Databricks的联合创始人兼CEO阿里·戈德西Ali Ghodsi的访谈我们先简单介绍一下Ali Ghodsi他曾经在加州大学伯克利分校担任教授
并且和同事们创造了Apache Spark这是一个用于大规模分析数据的开源分析引擎
随后Ghodsi创立了Databricks来商业化这项技术去年Databricks创造了16亿美元的收入最近一次估值为430亿美元已经成为世界上最有价值的私营公司之一
在这次访谈中Ghodsi重点讨论了他来到美国和创办Databricks的过程以及Databricks目前所面临的竞争环境
谈话的另一个焦点也跟AI有关包括ChatGPT的影响、MosaicML的收购

以及Databricks为何要发布自己的大语言模型为什么企业大模型的需求与我们看到的面向消费者的大模型根本不同等等等等
总之对于想要了解Databricks的朋友来说是一次不可多得的访谈
首先阿里介绍了一下自己的背景他出生于伊斯兰革命期间的伊朗准确来说是1978年的12月那时有很多孩子被命名为Ali

他在伊朗待了五年之后不得不逃离这个国家于是去了瑞典，在那里长大2009年之前瑞典在IT基础设施上投入了大量资金这也为他接触计算机打下了基础
所以当他上七年级的时候就开始接触到了Pascal语言2009年，阿里来到美国在加州大学伯克利分校进行研究如今图灵奖的获得者戴夫·帕特森Dave Patterson当时是加州大学伯克利分校的教授
他认为现代的计算机不会变得再快了不可能18个月速度再翻一倍了那么就需要新的计算机而新的计算机就是云它也需要新的软件
于是阿里他们就开始构建基于云的软件栈
启动了Apache Mesos和Apache Spark项目也见证了数据和人工智能时代的开启当时的Twitter还只在用一台大型机器来处理世界上所有的推文

你没听错就是一台计算机，Twitter的工程师说这台机器的内存要用完了得把这些推文放到一个集群中处理否则我们将无法处理地球上所有的推文现在看起来这是一件非常简单的事情

在当时却是个关键的难题而正好Mesos可以帮助他们运行这个集群虽然今天Mesos项目已经不存在了但是它影响了如今更受欢迎的Kubernetes
为了展示Mesos作为集群操作系统的价值阿里他们就想在上面做一个应用于是就打算开发一个叫做Spark的东西它可以进行机器学习、人工智能和预测

本来只是想做个演示的结果演示时发现Spark比Mesos的效果更好最终就把Spark作为主要开发的项目了那个时候Twitter、Uber、Airbnb等初创公司
以及一些像雅虎和Facebook这样的巨头已经在大规模地用人工智能技术来处理数据进行预测而世界上很多其他地方还非常落后
甚至不理解这些东西阿里他们当时想的是先发表一些研究成果创建一些开源项目然后全世界都会来读他们的论文采用他们发表的研究但是结果证明
人们根本不想读这些论文他们真的不在乎

所以当阿里他们试图去拜访这些公司

想要告诉它们

我们有人工智能

你可以在大数据上进行机器学习

而对方完全不感兴趣

所以直到2013年，出于沮丧

阿里他们创立了Databricks

其中有一些人，尤其是他自己

是很不情愿的

因为他们对创建一个企业并不感兴趣

他们真正想做的是研究，是发表论文

但是又无法产生任何的影响

现实告诉他们，如果没有一家公司

就不会有人接受他们的软件

所以这才是Databricks这家公司的起源

同样的，Spark项目从2009年就开始了

但是在2010年到14年期间

没有人关心Spark

只有在14年创建了公司之后

它才成为了一个全球性的轰动新闻

当时阿里他们并没有关于如何商业化的清晰想法

也不知道成功的开源策略需要什么

这些都是后来才逐渐发展出来的

彼得·蒂尔曾经说过

产品要想从零到一打开市场

需要做到比别人好10倍

而Spark不仅做到了10倍

有时是100倍

不仅更快，还更便宜

它可以进行AI运算、实时处理

甚至可以处理社交网络公司拥有的大型社交图

当它能够做到对1PB字节的数据排序的时候

之前大家对Spark的很多恐惧、不确定和怀疑就消失了

虽然之后开源项目开始起飞

但是Databricks这家公司还是没有什么收入

2015年仅仅收入了150万美元

而像亚马逊这样的公司

已经利用开源技术赚了数亿美元

接下来，阿里聊到了数据湖仓

也就是data lakehouse这个词的由来

早些年

企业里既有可以表示为行、列表格的结构化数据

存储在数仓中，适合查询过去的问题

也有各种文本、图像和非结构化数据

存储在数据湖中

可以询问关于未来的问题

但是这两套基本上都是完全独立的

阿里他们就在想，1、如何统一这一点

2、如何颠覆现有的生态系统

最终，他们构建了一个引擎

在一个开源格式中标准化了格式

让它几乎变成了像USB一样可以插入任何东西

这就是所谓的湖仓，lakehouse

一个混合了数据湖和数据仓库的词

当时所有人都认为

这是一个可怕的想法

但是Databricks最终还是坚持了下来

直到今天

所有同类厂家都在谷歌上买了这个词的广告位

回顾这个过程

阿里其实并不建议用开源的策略来做这件事

因为它太难了

之所以Databricks会选择开源

完全是因为他们的学术根源

阿里将它比作是打棒球

你需要连续击中两个本垒打

第一个本垒打是开源本垒打

你需要免费赠送软件

让全世界都喜欢并下载它

否则你就只是免费赠送了知识产权

什么也没完成

这第一个本垒打只是个必要条件

但是不足以成功

然后你需要按照彼得·蒂尔的话

再打出一个本垒打

打造一个从零到一、比开源项目好10倍的产品

因此

Databricks提出了一个Photon引擎

底层是完全重写的

它与Spark的API 100%兼容

所以对于Spark的用户来说开箱即用

但是Photon比Spark快10倍

在分布式并行处理的世界中

快10倍也就意味着便宜10倍

因为可以少用10倍的机器

于是商业价值就变成了如何向客户证明

可以把成本降低到十分之一

然后再从中分摊差额

而实际上这些策略其实都是事后才想出来的

如今

Databricks已经成为了处理超过2.5EB字节的杀手级应用

每天处理2500PB字节的数据

每天使用超过2500万个虚拟机

这里阿里提到了一个很关键的概念

就是数据是有重力的

一旦沉淀下来就很难移动了

所以很多合作的云服务商

会更加看重Databricks能够沉淀下来的数据

当然

现在Databricks面临的竞争也更加激烈

云服务商也在提供类似的产品

比如有微软的Fabric

Google的BigQuery

AWS的Redshift

还有直接竞争对手Snowflake

以及底层的Tabular或者MotherDuck

在阿里看来

Snowflake是一家很棒的公司

但是他们在人工智能这方面并不强

以至于现在要更换CEO来解决这个问题

另外就是

从一个可以处理各种非结构化和结构化数据的通用引擎

把它和数据仓库很好地集成

比反过来

把一个只支持特定结构化数据的引擎

推广到非结构化数据上，要容易的多

所以Snowflake现在面临着湖仓模式和人工智能的颠覆

而对于云服务商来说

最大的问题在于企业不想被困在一朵云上

所以在云服务上面一定会有一层

类似像Databricks、Snowflake和MongoDB这样的供应商

就像PC上面一定有操作系统一样

那么客户会不会觉得被Databricks锁住了呢？

阿里认为不会

因为有开源的替代方案

而且Databricks与开源方案兼容

所以他们锁定客户的力度其实比竞争对手都要小

阿里认为

未来软件会出现自上而下的垂直化

人工智能会重写所有的SaaS

并且将吞噬掉所有的软件

而Databricks从成立第一天起就支持了人工智能

或者说那个时候还主要叫做机器学习

实际上，2009年Spark的第一个用例

就是参加Netflix推荐最佳电影的比赛

获得了第二名

大约在2018年

Databricks开始看到自然语言处理在平台上获得越来越多的应用

比如保险公司用它来分析大量文本

评估风险

制药公司用它来分析大量书面的、非结构化的电子病历

在新冠大流行期间

有超过一千个客户使用了Transformer模型

而随后ChatGPT的出现

更是一次绝对的意识革命

于是

去年六月Databricks收购了Mosaic ML

当时的理由有三点，第一

大语言模型是数据提供商的底线

不过

大语言模型本身并不是长期的差异化因素

最重要的战略考虑是

数据是有粘性的和有重力的

第二点

Mosaic ML与Databricks很匹配

因为两家公司都对市场采取了同样方式

那就是提供工具和服务

而当时绝大多数的大语言模型公司

都是消费型公司

只有像Mosaic ML是少数在B2B企业领域做的很好的公司之一

第三点

Databricks解决了Mosaic ML构建销售力量的需求

而Mosaic ML解决了Databricks围绕开源项目

构建可持续差异化业务的需求

除此之外

Mosaic ML还拥有一个研究团队

他们对大语言模型和人工智能有很深入的研究

这在当时很难找到

他们的商业模式是帮助客户从头构建大语言模型

从而让客户的企业变成一家数据和人工智能公司

并且拥有自己的知识产权

因为现在很多客户都已经意识到

他们的数据是多么的有价值

以前

大家都非常专注在开放互联网上的数据

用它来训练大语言模型

但是忽略了企业中的专有数据

它们一直是被保护起来的

这些数据是以前训练的大语言模型所不理解的

比如它们不理解地球上任何组织中三个字母的缩写

Databricks有Mosaic ML缺少的数据和销售力量

而Mosaic团队知道如何去构建定制化的模型

这正是双方合作的基础

现在对于企业来说

Databricks已经研究出了一整套定制大模型的技术

从轻量级的微调开始

到最受欢迎的LoRA低秩适应训练

当然在定制的实际过程中

比方说

很多人想要得到像ChatGPT这样的东西

完全通用的、开放式的

可以回答任何问题

但是企业通常有非常明确的任务需求

其实小模型就足够了

而且也更加便宜

除此之外

企业其实非常关心回答的质量和准确性

对于特定任务并不需要给出开放性的回答

当然，也会有客户想要通用的模型

那么就必须选择一个更大的模型

但是通常也会更加昂贵

关于这方面

Databricks正在研究混合专家架构

以及Llama 3的密集模型

另一个跟企业模型有关的就是在哪里进行计算

Mosaic之前有两种模式

一种是用Mosaic自己的GPU

来自于云服务商

另一种是用客户自己的GPU

而Databricks收购Mosaic ML之后

第一件事就是停掉了后者的方案

只提供云上GPU的方案

这样既可以保证客户有最新的机器可以使用

也避免了和客户本地的基础设施混在一起

阿里回忆说

当年创办Databricks的时候

就有咨询公司说必须要做本地

但是如今任何一家大公司的CEO

都会认为未来在云上

另一方面，阿里认为

人工智能的出现

其实增加了数据的重力

现在

人们一方面对生成式AI和大语言模型非常兴奋

另一方面，他们又比以往任何时候

都更关心安全、隐私

想要确保他们的数据不会被别人拿来训练

并且不会被黑客攻击

这就是为什么不仅仅是人工智能公司

很多安全公司也活得很好

在过去的一年里

Databricks一直在获取客户的信任

告诉他们数据是安全的

隐私是被保护的

这样的话

客户就不会想要去移动数据了

因为那样可能需要花上半年或者一年的时间

来通过安全架构审查

对于全球的人工智能发展

阿里认为中国在人工智能方面的发展非常快

因为一些亚洲国家的监管比较少

而欧洲总是比美国落后几年

他们的监管更多

印度和巴西的发展也非常快

因此databricks在亚洲和拉丁美洲

也有一些不断增长的业务

最后

阿里谈了一些创办公司的经验和教训

首先第一件事情

就是要努力找到并且信任好的领导者

这些人呢可能一只手就数得过来

但是要一直努力去寻找

因为与人建立信任是需要时间的

这就像建立友谊一样

第二件事情是不要害怕大公司

如果你保持专注并且战略正确

是可以打败他们的

很多大公司呢更像是一群松散偶合的复杂的自适应系统

里边的人呢都在试图推进自己的利益

而不是像一个设定了战略之后

就一直向前推进的机器

所以不要低估自己的力量放手去做

第三点是你必须要销售产品

仅仅把产品制造出来放在那里是不够的

产品和市场两者都要做好

而且呢两者需要和谐

至少在B2B行业中是这样的

好了以上就是databricks CEO

阿里·戈德西这次访谈的主要内容

希望呢对大家有所启发

感谢大家观看本期视频

我们下期再见
```

[image](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/bcc38f62-6008-4158-be81-8650adb436b5/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466X5Z6NANF%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T234418Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIAOB%2BDJM809cJzJx6W2XBmWnJBj1a2c3u5LZLdDeTFKkAiAHnPF%2FJgpumSwio643jZgHkmQJA8wHOfpxKIiTsxx5myqIBAjG%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMMbosq7Y7mrefrdE%2FKtwDXcDh4u%2Fty9X8Q9EVOMGJm%2F4iyPdFiQzcyFG5P23JL1O9YTj9QF4CZyA0suFM38csKgUUxjp2wpOAxXsqe7PJQAdyCgxsMCQrrdw9xe0LKIhBOJkAqOfX6O38dClrAwX7PUR3g%2BxL28uPd16zp4lKJjvUW%2BRggSlINTl8%2ByvHpn797cAcjyMgIgyyu06Xb1qlmEKFoaNhGO%2Fu7C6De6G52ZRxgIxxIIhh684HE3uZ%2FCE8DNlAz507t%2FnHLhB6DkdinKZryGieHsn6mNNEZaSYAzrVlTvi%2Fi3y5bKHpdnuqqSifR4IRf6SojjxlBRx6uWOgjQpH718Oiq7Y3c1BfVsVvdLZOh7s7uGiM%2FA%2By1N0%2FfcJ7dncCEz4niUzF7azLRossDBPMkoDyZaJQ9JNvMcw1SsKs6kiSctDo6e2034hhShg%2FTyn4jSAJUq%2Ba3mUQdhNvudGvGj%2Bt0lL4LLqnR%2F2r1a%2FqnBAE3rfMDOPl6fJg5NwRTYDYK9n6UwVic8GhqpiTMzAhoJ%2BmLSuqegG0QS%2BE1gISbxgVSxyzHz8e4K%2FfPp12RELYkdw2PaafzVNKVjVobgL8wUf%2BfY6Cwv%2BGn8vAFVj4jG8NBiVCYXVcm%2BxrcYlth74bptxhL5TzAw%2Fbn%2F0gY6pgHJ1%2BC5btVGpRAld5B986y7KIsWamntZlzoPejfX3TusarwtgC72SGqla6l9TLm5%2FyB2P%2BnByfeGwp97fq3bTZzv%2B7q6d%2BIaoR5T6IudqyzXBaNKmc6pjVMYwuaKXnduTViMtB2yqhJD91s6MppJZyPdetIPRSJ7imrMxHE1%2B42vMvTL7UjMt%2F3v8yCH0QqRpf1L7MstRtfwr8fuLJblYprt1GSoVUj&X-Amz-Signature=2ac3fafdb18ab6e4ec949a52b30c4ca70be2f3d21cad7c224c0e6143a6116b30&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

