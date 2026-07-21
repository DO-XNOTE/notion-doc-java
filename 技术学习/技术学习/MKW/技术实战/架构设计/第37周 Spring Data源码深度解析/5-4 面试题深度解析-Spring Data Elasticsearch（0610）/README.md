---
title: 5-4 面试题深度解析-Spring Data Elasticsearch（0610）
---

# 5-4 面试题深度解析-Spring Data Elasticsearch（0610）

[image](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/4a5c1321-a94e-42be-aaa6-75dc98f3469e/SCR-20240814-jwvy.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZM6X4Z4W%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T232149Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDeLKI%2FVedfMD5dKmjffvrlzwWilzRrFzBcqwUsus5IOQIhAKN8u0RaSx8oV11%2F8IBECGgEQ2S%2F1X67SEM3vBmPJDWIKogECMb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgwPp8j2lau7KPK8Hk0q3ANMh%2BgfgCmphAMycgvKm5aVznLYQLvb9iUrXZcj4Pw1XYHb%2FjPeIzjnfNvXWNKRBhnd%2BsBh7lWSfZzKzzJhUDLq4IehEm2px6qRFxHUtksEpE7VQl42XuxA2aX4PuukNnXgc9w8TjLpKTI4EpO6yRFiBTeOOi4RJ6KrB2T6%2FmPOfwBexWGnP64JFf1RONggtWEw82465k6l9X5qZsZO5HOkZjH4wufl1uDzrbqVat4aOSXB1yCfOf9mySTLi8yaVRyEF4ci7SHqiszpTVaatoZHLgbwhyADQPQvAMIJK6DnxWmjmpkghWzv7aSHOxCbVdL8lb%2F509u4uPRdhrj0NuRfspl0kc%2BND4k8Xu09jq0smSZKrQSci3ugKVp2a6w8ERwq16X11rsttiNp8gdX6VqC5mthLNK7xqDA54ZfaQLcXZc9AiV8B%2BAVwgYjkZh%2FPcQuU%2FDZ9Fc%2F3owduXaBGgNu%2FBawK2tPtP0KvckhQIM2y8%2BcgB%2BSu85fJxdAtUwJstNEDbxG%2BHLKkDmgBX%2Ft0W56bfbBEn8jC9tk7iaPpmzKE9uFZ5tQzEp7kT9dgHC4BvwOqB%2B3tAHsfuyPfCQ9Ph4K4N1zdQLXcE8BD%2BY3E29SMEI2KtPBZy%2FqdQuupDCNuv%2FSBjqkAbWsq%2BDRsgHDSmHlhWlt9fJ2zjSg1UP2Dam7ZMJ7m%2FrnyjFz7dj24Vi6BWv7Pue2IPLnKjUPfTNqgtTziyF12AMCaQeAVItQDzLyG1Azxg1pqZFRcLXC0Ubc9IErgnc3%2F1SrM7NC0QP%2FbbWTee5j6%2FYgP6%2FG3rY2tFI0Wh3bA4JyR10%2FUnGMbx1far1eOUII2%2FOjT2Y6D2I7evd0s4Hf8Gp%2Bqevl&X-Amz-Signature=4f400708e7e6f4f90b401f6b79ff52ad8989f5dd739025e5becf5c593543a525&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

同学们大家好，这一节我们来介绍一下面试题深度解析关于 string day 的依赖色词。这里面我们看我们并没有把 string day 的依赖色词作为一个面试题的问号。这里面如果说面词官说你能不能跟我介绍一下使命 d 的 e 加s，s，你对它的一个认识。通常不管是 e 加 s 还是Redis，或者说是我们这里面提的Mongo，我们学完以后一定要对整个这个主键的有一些印象，比如说让我介绍一下 three day 的 ES 是做什么的，那么我们可以这样去介绍。


首先 spring date 依赖测试，它是 spring date 模块的一部分，这里面我们可以先介绍一下 spring date 是干嘛的。 spring date 是一个用于简化数据库访问并支持一些云服务的一些开源框架，其中主要的目标是对于各种数据库的访问进行一个统一，这样的话我们去方便访问像关系型数据库、非关键数据库 map reduce 或者一些云计算的一些资源服务，非常方便，甚至比如说 spring date 可以比如说他其他情况的一些印象，比如说像 GPA 跟 spring date 关系，我们可能印象会更深刻一些，可以简单提一下。


里面还可以说一下 spring day 的rest。基于这些扩展的话，我们再去来介绍 spring day 的elensearch。 spring day 的 elansearch 它是基于 spring day 的 API 简化依赖测试操作的一种方式，它将原始的依赖测试的客户端和客户端对应的支持 rest client 和 high level rest client 的 API 进行一个封装，使用 leader 为一代设置项目提供一些搜索引擎一个集成的方式。


我们通常知道，对于我们要使用 Excel 设置，通常是我们的查询性能受到的限制，需要通过疑难 search 来解决我们查询的问题。如果说疑难search，它因为基于倒排索引，它在查询的过程中对我们这个索引的列是没有限制的。通常，如果说我们使用 MySQL 加 show in 的话，一个表里面的 show in 太多的话，会影响我们写入的性能。对于一段 search 的话，它其实就完全不用做这样的担心，我们在使用依赖测试的过程中，随意的去扩展我们的任意字段进行查询都是可以的。所以说为了方便我们去使用的话，使命 date 在统一项目的过程中构建了 spring day 的 events search 这样一个模块。但大家要知道， spring day elecserments 模块我们可以理解为它是一个社区的版本的贡献，最早并不是 string 项目主去发起的。


所以我们基于 Sprint 的 ES 在使用的过程，我们可以再详细介绍一下 Sprint 的 ES 舍庆过程的一些特征，比如说我们基于 at document 的注解去标明我们的实体，基于我们的 EDSS 对应的 template 进行一些操作。


这里面还要介绍一下我们的 ES reporsory，它是跟 GPT 类似的一个report，一个扩展。我们基于 deposit 完成对已在塞词正常改查的一些操作。我们几乎上很少写一些具体已在塞词 rest calendar 的一些构建的一种方式，这样方便我们对于 easiest 存储引擎进行一些数据的正常改查。你在自我介绍的过程中，面试官也会给你一定的反馈。如果说你发现面试官对你解答的内容感兴趣，你可以适当的引申一下。比如说我们在配置映射的时候怎么去配置？我们通过 add document 这个注解在我们的实体内标记。我们这个实体类就是一个 elect 的对应的一个文档，通常它会基于哪些属性？比如说我们的 index name，也就是我们这个对应数应库的名称，另外这个 type 对应的数应用库中的类型，我们知道在 EDS 新的版本里面，对于 Tab 的支持性能并不是很好，后面它就不太支持用 tap 这种方式进行区分。


另外它的 side as 也就是分片的数量，其实我们知道 Redis Sprint 的乙丹色时段的分片数量默认是5，分片还是比较多的。另外就是说它的副本数，副本数默认是一，这里面还要注意一下，涉及到对于每一个都平的对象，它又应该唯有一个唯一标字。


跟我们的关系型数据库里面的ID，我们的主键 ID 是一个类似，这里面也支持用注解 ID 的方式进行修饰。我们指定的一个成员变量，也就是我们的一个属性标明一下，对于这个实体里面这个对象，它就作为一个 it 的标记，也就是在库里面是具有唯一性的。


另外对于其他的一些属性，我们可以通过 i 的field，也就是进行一些羞涩，我们基于这些文档的字段来进行映射。比如说对于 at field，它支持的一些属性，首先是它的type，也就是它的字段类型是什么？通常对于这里面的字段类型是一个枚举类型，也就是跟我们依赖测试对应的数据类型有一个映射关系。另外就是说它是否支持索引，是个布尔类型，是否索引，也就是说这个属性是不是可以用来进行查询，它默认支持处，也就是默认我们所有的实体的对象都是支持查询的，另外还有是它是否存储，它默认是false。


也就是说通常我们的一代色词是跟 MySQL 进行一个组合，使用我们基于一带四词进行一个查询，查询完对应的 ID 以后，我们再从数据库里面获取这个真正的一个实体对象。通过这种方式组合能做到我们查询的性能和我们数据库操作的一致性，这样两方都可以做的做到一个均衡。


那我们知道像 spin day 的ES，它还支持一些透明的审计与工作，这里面跟斯伦斯的 GPA 的审计工程是类似的。当我们在创建和变更的时候，去补充一下我们的创建人创建时间最后更新人最后更新时间。其实对于此问题的依赖测试大概也是这些内容，通常在介绍的过程中，面试官会跟你交流对于某个细节的了解的话，这就看我们自己造化的过程。其实我们对于使用了解以及它的执行的一个原理会有一些介绍。其实此门店的 ES 还有很多很多的细节，可能我们在课程里面不会做到一一介绍。同学们，如果对此门店的 ES 有更深入的兴趣的话，可以大家看一下官方文档，或者说对源码进行一个更细致的一个跟踪，了解一下我们没有覆盖到的问题。同学们，我们这一章节就先介绍到这里，同学们，我们下一章节再见。

