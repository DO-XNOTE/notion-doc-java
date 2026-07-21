---
title: 1-22 【案例解析】敏捷项目管理系统-EventStorming事件风暴（五）
---

# 1-22 【案例解析】敏捷项目管理系统-EventStorming事件风暴（五）

[image](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/90f8c48e-7e02-4f2f-ae74-99c88fa5d180/SCR-20240801-fwht.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XVPFP7AN%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T230922Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIDQZvGZgtojV79IRDYp%2FSOKRRupW9zDZApEbWA4dGYYuAiEA3YmB8y5aq7ROCWwa%2FDnAAjWIGQ0QZd8HWOVElN6WEvQqiAQIxv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDAN8Qh25elZQnHaqDircA2Wo%2FVRV%2BTRUxRO4xNqEXKmseT0L3BGMBBFil3SosscXM8jijJ9kYXr1o9FJ%2BLhYtROK7DfFd7ASfYr3diSjT34Y%2BYdxIuhLntwb2JIIPLzCkJ9oNwbbURByrvrCFEKc%2FpXf1WHa8nDcTdq82eV6vYSDbovsa5m5M%2Fjmk4FcolrtuIDonwhogUkxQf72iaXd0OUKbm9Z3SgIbXAz%2BZgi1Wc5vfn3XVcfIJjb8Kvi2z9VDHuK6NIuc8JXrdfUH8TahpvajykUieX1o%2FJvBmt7C7xQeqqikE68BCD5Sf2RqPrYKM4v8fnbqIi8PMcI95T3PBxIyztCEFoNcy39XexVQtSb%2FaCAjhJ306XmvmbBi3cCCNb3toCUwh1VbODG5vc%2F9Rt0F3Xw6Unwd56sEiyvsyqbs2RVVU5OEi%2BvUc7P4vT0b4Rq8c%2BgQNvfs4VwM1QiTbtTAdrDNZ09gYtRfqFrAAz8x70iSDVmwQcNPyCWv8I52md0Ti2zSu%2BMtMIsZzeljWDKSp5FQrETtli6oxmjD%2BuAqxCgXI1RgGWnSBlEYupSOaXr0zWQC7J86QFEVLtPXaAMeOVwVmIruttW3kqGtzIN77xqa9r4%2BaYNsurBmpg7inIkTLwnzsuwF5u%2FMLS4%2F9IGOqUBrx5Ea1fV%2BS1ONV5gocOluE%2FgfIN99gDAjLT16cuFsQc0bHYWCWn1V%2FPzJt0xwuFqNrw9l1aKIcNjTlHUDKYlpG0oY7jIsy5xWEypK94eyrRaP3s7w1wnApAjlMvoyH%2BDs%2FeWuFUSi066A26ncXO9Me57IP4TLBEr4B09JP%2FkHYqGooVQf3paE4s0zWAzSWvm%2FJ9J1JE%2BLiy19ZEbqmw8riNUVFlx&X-Amz-Signature=f5be7d6e0990e56eecda9279f96b72b843971fc7728cf384c4a8c2676fab346d&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

需求到落地的桥梁，构建 it 新蓝图，我是张飞扬，那前两节我们看了看，发现聚合和蛛网模型，那这节开始我们要根据前面的内容创建出类图，找出应该开发出的一个一个的领域事件，具体该如何落地，如何关联这些聚合。好，那到这一节开始，我们不需要我们的业务人员和产品经理介入了，因为什么所有的微服的拆分，聚合的拆分以及聚合的关系，我们在前面玩小蔫子的过程当中，在互相侃大山的过程当中，把所有问题都已经解决了，所以整个架构的框架其实已经出来了。下面指示什么把中文变成英文，把什么把蔫纸变成架构图而已。


好，我们就看一看，发现聚合里面最复杂的这个任务应该怎么样处理？我们把任务在代码里面可以用一个类图的方法来表示，比如像这样我们拖一个类图，我们假设我们把这个任务叫成我们待办任务，通常叫 backlog item 这样一个英文名称，我们就取这个名称 backlog item。


好，下面有哪些成员变量？其实我们可以想一想，这里面分配优先级是不是就是有一个成员变量叫 business priority，对吧？这就是分配优先级这个成员变量，然后分配故事点是不是就是 story point？还有什么？还有打标签，对吧？就label，还有我们跟什么？跟发布相关，跟冲刺相关，但这个时候发布和冲刺可是独立的聚合，要引用别的聚合，最简单的方法是什么？用它的 ID 你就写上 spring 的 ID 以及我们的 release 的ID。除此以外可能还有一些成员变量，比如像是状态， datas 等等。


有这些成员变量以后，我们还要准备很多的方法，自然首先有一个什么我们的构造的方法，除此以外还有什么方法？还有我们这个分配优先级要写成什么通俗易懂的英文？就比如 a sign，然后是 business priority，是不是这里是通俗易懂的英文？另外分配什么故事点，我们可以写成 assign story point，全部就是什么把中文变成英文，那自动就生成出了类图。


还有什么？还有很多，比如像 change label，然后比如像是我们要把一个任务变成一个冲刺，我通常叫什么？叫 commit 承诺它，我们保证在这段时间之内完成，对吧？ meet two，这是一个常用的，这个把一个任务承诺发布到某一个冲刺，那发布成一个真正的这个实际的这个软件部署叫 schedule for 的，当然大家也可以用其他的英文表示。还有什么我们不承诺发布了，我们也不承诺开发了，我们有 n commit from 或者有 unschedule from 等等的方法，它取消这个什么发布和冲刺。


还有什么比较关键的内容跟讨论有关的？比如我们创建一个讨论，这也是在我们任务里面跟讨论相关的地方，我们可以来一个start，一个discussion，然后去跟讨论创建出一些的关联关系。除此以外，我们还有什么安排？一些这个负责人、写作人员，我们可以来一个 assign task 的 volunteer 的这种方式。好，这样一堆的这个什么这样一堆的成员变量和方法，我们就什么中文翻英文，把动词来源的动词变成动，把其中的一些关键名词变成成员变量，这种方法就很快的基本上把我们的类图准备好了。


那除此以外，我们再看一看蛛网模型里面，我们还是看任务，蛛网模型里面比较关键的几个任务，比如像关键的比较重要的几个那个领域事件，比如像任务冲刺，已安排这个什么具体的这个 schedule 的一个冲刺。还有我们的任务发布，已安排我们 schedule 的一个什么一个release，一个Sprint，一个release，这两个事件是关键的，除此以外还有想讨论与创建等等事件。


我们来看一看这几个事件，还有前面说到的成员变量和方法，是不是在我们的实际代码中，你是类似的？我们切到我们的 IDE 的平台，然后我们继续看 backlog item，好，拉到顶上，好，我们从上往下看，是不是确实有成员变量，像是优先级，像是讨论，像是产品的ID， release ID Sprint ID 还有状态以及相对应的 story point 等等这些实际的这些类。


然后这些类通常都是什么？都是值对象，然后这些值对象的这个具体的对象就变成了我们的什么我们的成员变量，逐一把这些成员变量给准备好，然后也有它对应的构造函数，也有它那些，比如像是我们很关键的，像这种看名称就能非常之清楚地了解他在干什么的。 assign billions， priority 这种什么领域事件里面什么充血的方法，可不是贫血的settle，是 assign off，然后 assign storypoint 等等大量的方法。除了这些方法以外，我们看一看我们再怎么聚合，我们往左边看，我们在 backlog item 聚合底下是不是确实有我们刚刚说的叫什么这样一个领域事件，叫 bug lock item committed，这对应哪一个？就对应我们前面的架构设计图里面的蛛网模型里面的这个任务冲刺已安排，那有没有任务发布已安排，我们切回去看任务发布已安排就叫 backlog item scheduled，就是印好了什么时候把这个什么代码给发布出去？这也就是一个什么领域事件，我们可以标注一下，这又是一个领域事件。


好，还有没有什么领域事件讨论与创建？我们瞅瞅看有没有讨论与创建。 bug log item 有什么讨论吗？ discussion initiated 是不是也是一个领域事件？领域事件，我们逐一地把这些什么能考虑到的领域事件黄色的内容，逐一地通过各种各样的方法，或者说各种各样的类来实现。它们都是什么？都是实现一个抽象的这个接口，这个 domain event 就可以了。


domain event 里面我们跟之前聊的一样，它自然会记录下它的时间 occurred on 对不对？然后每个领域事件有它自身的特点，比如说你这个领域事件什么直接是在我们的班级里面就直接进行处理了，还是需要通过王大妈，通过校领导，通过传达式代言传给其他的院？其他的校不同的领域事件有不同的处理方法，那我们这里这张图里面列出来的什么领域事件，都是需要传到其他班级的，至少是在其他班级才有处理。同时有一部分领域事件，我们看看像这种什么 status change 的这些领域事件，什么是在我们事件风暴里记过的，但这个领域事件并不需要通过我们的消息队列传给其他的班级，传给其他的学校，所以是可有可无，甚至是什么可内部吸收消化的领域世界。


聊完了，蛛网模型也聊完了，前面的发现我们的聚合以及和代码之间的关系，那基本上大家是不是已经清楚了？完全无所知的状态，很找到产品经理开始进行事件风暴，以及到我们的命令风暴，再到我们真真正正的发现聚合和蛛网模型，最终到内裤和什么一个一个的值对象，我们的这个实体和聚合根把它开发准备出来，那基本上就完成了我们主体里面要说到的整个事件风暴的核心内容了。那我这里总结一下世界风暴有三大核心思想。
第一条思想就是由下而上更快。所谓由下而上就是我们平时的这个很多拆分都是什么？是通过上层，比如说什么首席架构师，我们的这个 CTO 进行总的模块的拆分，然后再分到每一个模块里面，而世界风暴不是这样，时间风暴是我假设用户体验是这样，然后就由我们的小架构师、我们的小研发、我们的小产品经理和我们的小业务人员就开展了事件风暴了，从一个事件开始从下往上的来考虑，那这样其实出手更快。


那另外一种情况就是事件风暴是事件驱动的，我们是很容易更新的。当我们整个架构定下来以后，一旦用户体验有所变化，那必然什么每一个具体的操作的状态有所变化，在这种情况下事件有变化，这时候你只要改变那些黄颜色标签，改变蓝颜色标签，进而去改变那些紫颜色的聚合的标签，就可以逐一从下而上的去改变整个架构，使它能够迭代、能够演进。


另外最关键的是，整个事件风暴其实是一个很好的团队破冰过程，当你的团队产品经理不认识架构师，不认识研发人员的时候，为什么大家不一起坐在一张白墙前面，贴一张白纸，边喝茶边喝咖啡边聊天边完成微服务的拆分？通过这样的交流，我们不聊细节，我们没有很多的争执和冲突，我们可以心平气和地把微服务拆分给拆解得非常之完美和漂亮。好到这节为止，我们的事件风暴这个大难题就解决了。那下一节我们会聊一聊领域驱动设计的后续的一些残留的问题，比如说是我们的代码结构，或者比如说是我们通常电商平台会有哪些常见的领域子域聚合，大家敬请期待。

