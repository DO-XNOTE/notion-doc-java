---
title: 5-2 面试题深度解析-Spring Data JPA与Mybatis、JPA、Hibernate的关系（0505）
---

# 5-2 面试题深度解析-Spring Data JPA与Mybatis、JPA、Hibernate的关系（0505）

[image](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/8212d1a8-33bb-4f39-b3e3-fb3a2c7878bf/SCR-20240814-jtht.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YPNWLUX7%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T232147Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDh1Bndi%2Bz0elqMmP9Q%2B6DqE%2BxaFeiUdjYAxq46gCPcOwIgalxIR%2F44M6HdvDc%2FUWA6HnQWb4EEBdX3g%2BYI1gPRYwIqiAQIxv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDGkjkB7ltP1EqJL2SyrcA0YJNbDoKcumH3W6pu6G6e5QvFptro8m7c0eteRglRNAdR0zlzcbZxmG4CuTfJUxEywlxwXI2lL67rDS325FvWavRHTScCZH8UYLZN5otMURoLPCfAkRvZ9PIkAgMiMvrsg9do4O6Z3Gn5ZNu%2F%2F7dGsdWeoC%2BZ2E0rk6stGScztKFg7p0nnUVa8uWrf9OPT5EJAeZHSuhG8zQY8R1W3bN6O5ZdgQ6dgzYVrOmm7g%2FXXdhW%2F5G7qS%2FltbycOuz%2Fst7I%2BviYyLJ6yL808oHR%2FTlDfPFzc5u4dnbpdiw%2FcASck9%2BgjL3%2BPeeIyvLIwTES67cHohpIyRN4dPfICKdH4QOIPzfIEDR7udPkGajTG3mbke%2B7gFUmQD3N%2F%2F4On7ZrDoMt0wWBuCnyQ%2BpbAGXfNqK75a9I91Z03gjk6k7Xw9kpSfWsjrTH9ZtyGfBIDL20PMj6P4GEGfeNXwniy%2FeuYnhnFT6VFrQhEQr7A729LsmISr1KwS33riz4NI7km5b%2BHrOkQaiNSzh2L1xM3kHsLc12NuN%2FAhU2gKARRdZ3L7kouPZaIbh5ZgswZvpfblq3FsRb14t4gppc47qgcb63p0EAMSmOK4pBepou4JP6e%2FfudyUWzKRLJ3zYK2la74MJW4%2F9IGOqUBSmS4V%2BA3x1RfGcy5E89LKHDEbtADazhp2Ebb9L0FHN2eSaUtVnSeFejJNrRssdg38RUkwiOCZtBCWU4BiYiKao9GwphpYaF0xBvqkYOROf%2Fg1F%2FITZfMvGQ56p69I5wKE%2BvgJgCIewuqFoSvhzNj93grqUT3wN1QA74u0LrKpaPitefKfupfzCOhPbzAuNu0FtB%2F3qhzZ0QN%2FoW%2Bflu%2BguMiXyrx&X-Amz-Signature=77726be54ad95b252ea2c8d807a7f0451ed3731da6fdba64b8b3691bda41b277&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

同学们大家好，现在我们来介绍一下面斯提 spring date j p a 与mybadcase， j p Hypernet 之间的关系。其实这个问题也经常被问到，如果说你了解到你在用 j p Hypernet，也了解 microcase 的话，这个问题其实比较容易毁大。


首先我们知道我们抛开 spring day 的GPT，我们先去分析 mybettis' GPT 和 Havennet 的关系。对于mybadcase， JP habitat， my Betty 其实跟 g p highlight 没有什么直接的关系。其实对于他们来说，他们有一个共同的依赖，就是他们都依赖 TTP 协议。不管是 my Betas， GPT 还是 Hive net，他们底层都是基于 GDP CE 协议来跟我们的关系型数据库进行打交道。这里面我们再介绍一下 GP 和海布。


net 之间的关系。首先 GPA 是 Java 的持久化的一个协议，heronent，它是一个 Java 刺激化协议的一个实现。但是这里面的相互关系大家应该要清楚。首先是先有了 Hibernet 取得了一定的成功的条件下， Java 的他们的组织才定义出了 GPA 这个协议。其实定义 GPA 协议的这些工作人员有很大一部分就是海边。 net 它的开发人员。所以说我们知道 GPA 它是个规范，里面并没有具体的 GPA 的实现，它是基于 havenue 来实现的。


其实在早期的话，大家竞争的关系并不是说 spring t 的 GPT 与mybytes，更多的是 mybadcase 与 Hypernet 之间的竞争。其实我们知道 Hypernet 它是基于 ORM 的一个框架mybadcase，如果说是 OM 框架，那么它就是简化了一个 OM 框架，所以这里面说 my pattern，它是单纯的是一款相对还是比较优秀的持久化框架，因为毕竟在中国这些互联网公司使用的非常广。


它支持定制化的 SQL 存储过程以及高级的一些映射。买 Badcase 它能避免了几乎所有 GPT 代码和手工测试参数以及获取结果集的这种操作。它就是主要使用简单的 XML 或者注解来映射这些原生的这个 SQL 信息，它把接口的这些 Java 的 PORTAL 信息，它跟我们数据库的映射关系构建出来这个映射的情况，所以说我们基于 mybadcase 可以把数据库查询的这些表里面的数据直接映射成一个加码对象，通常是我们需要对应的 VIP 文件去做一个映射，这是mybadcase。


但是 mybadcase 在中国互联网公司的使用非常广泛。对于Hypernet， Hypernet 早期，其也就是几年前我们通常这互联网行业没有大规模起来的时候，通常一些企业级的应用软件会使用hapnet，因为 hapnet 确实可以能减少我们在写正常改查的花的时间。通常我们认为 Havennet 生成的收口可能是性能也好，或者其他问题会差一些，但这个观点其实是不正确的。大多数人没有选择 happy time 的原因，更多的是 happy ten 的上手会比较困难。这样的话，也就是说当我们这个互联网快速扩张的时候，对于 Hypernet 的储备人才并没有建立起来，所以说很多公司先入为主的选上了mybetis，但是其实通过 mybeta 在牵引 happen 的这个过程，大家可能没有太多的动力去做这个事情，所以说在 spring date GPT 出来以后，对于很多人是一个冲击。


我们 spring date GPT 它就把我们原来对于 happy night 这种偏见通过 GPT 的方式集成起来，对我们确实带来很大的一些方便。所以说目前来看的话，我们如果说在 spring day 的 GPA 与 Meta badcase 或者说 GPA Handler 之间选择的话，我们怎么选择呢？首先我是这样想的，对于我们这些查询，如果说你对哈班的 GPA 非常熟悉的话，就选死能力的 GPA 肯定是没问题的，不用担心生成的搜狗语有问题。如果说你发现了生成的SQL，它的性能有问题，此论 d 的 GPT 跟我们提供了那么多可介入的方式去制定你这些 SQL 语句，总能去把这个 SQL 优化去做好的，所以说不用担心这个问题。


另外一方面就是说如何去平衡现在大量使用买 Badcase 的这个业务场景，当然对于老系统的维护已经用上，买 Badcase 你很难去推动 mybadcase 切换成 spring seed JPA。这里面对于一些新的系统，尤其是腐化需要快速上线的这些系统，如果说我们有 Sprint GPT 的基础，那么就上 Sprint GPT 肯定是没问题的，当我们发现性能问题再进行优化，绝对不会因为使用了 GPA 让它的使用性能的低于埋Badcase。如果说我们使用的不好的技术没有积累到一定程度，使用 GPA 可能会比使用 mybadcase 给我们带来一定的困惑。


对于像 string day 的 GPA 与 mybadcase 它们之间的关系，我相信通过这样介绍大家已经比较清楚了，也就是说对于新项目，还是推荐大家使用 string day 的 GPA 的。对于 string day 的 GPT 和 my Betty 的 GPT 的关系，它们之间的选择，其实我们选择了 string day 的GPA，其实我们就需要依赖 GP 和 Hive net 这种技术栈，我们基于 spring seed GPT，在深入的去了解 GPT 的技术栈和海边。 net 的技术栈也是势在必行，所以希望大家在掌握 my badcase 基础的基础上，再去把死中 day 的 GPA 海边。 net 好好的学习一下。这个问题我们就先介绍到这里，同学们，我们下一章节再见。


