---
title: 2-4 Netty编解码技术之Protobuf基础应用（上）
---

# 2-4 Netty编解码技术之Protobuf基础应用（上）

[image](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/a9115497-ea5e-464e-9ef5-bad04c16b762/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662LZRBBDL%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T230010Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIEhMcL%2FzUNoY3ZY6FxgBghP2Us0YNUBLoCKyZl5k7M6nAiEAhKR5N%2FzPMGu8dS8INC%2BPuOlXNpMCbWBAH6SDmpkz4t8qiAQIxv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDG2HlF33mCP3k0tY9CrcA18toZj6gI5Cnr71W5ArXYUOA%2B5vNZGdWnk0tFymrU%2BfC%2BtCspLfxX%2FVarOgRIjAsSxJ1xPptcCOorIS2bT3VB57yZBEnpfB06zjv0qYf5Ep09tz685YDx%2F%2BTfNh4VNeLAWd1APz%2BvHXFZFrtb60wLAmqZQoxuRFa6LHToegyIMB%2FtZu5pHgvJxbsfkbov4bpo5Egs%2FVYb%2BlT5lfIfVTiykrBkZTXKZkeOi22tZejPU0573Ie%2F274Dmerap5XuH74AxVZ86BByBCiAXLLziV%2FC3nyar%2Bo4PcEZ3kIYfYW6V1KASbZKUFBw4g9WvEiOgXIaqVMwFyVpZ4bPzSdUjOMAKqFddVDAkrYOi6ZE1sGdOmXNC8tqrnd3ylLxqmi2%2FoOojuN99vXnMVyPnI9If6VSqLXu0M0yNTZ2rNhx1evBCS1M75VMhi1aDedXWPDvq2JdshLvm1X5MPP4WRW9DJAUtMrJejagKdOGf0%2Faue82xntjsai8ue1NKfI6cVZ0eRkDCSsTZYW8hyE0HMdrR3oYoZU27a%2FJYNzU7APNKblDE6GAlO6lG0kDVSTiWxaoP2Vzl2ACjg7OutFC4Oaob8ClSxCrVC30H%2F2uXNi4MRGt5jmwcbxqzWm%2F8LX7N%2FMJq6%2F9IGOqUB9yxU7JpM2UBVEJNjgCpgF15B6PxOJvuXUwzDeXE%2BikwNTvd0Y4ghP3%2FFh8x3CtHRLFb1SOCtjW%2F%2FP4iv1Pg%2F2bt3L6ySh1lac4A%2ByQp%2FyDRnj9PwA4DAhge6VVAhBnE3ZZF8dNKZCuYEflMTevhgQMlXqRiZPoBEoakRR1uDLD9FC8P35DFvgLY2dMfb5q7vtQcCxMUR5DVR4yxmTYryvf4NXHpN&X-Amz-Signature=71099b7ad719935ebf3420488ffe32226d5abf2929ae8df1bae4d595995faaf8&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

小伙伴们大家好，这节课我们继续往下来学习。学习 Google Protobuffer 基于 Nitty 的编解码。首先我们先简单的把 to buffer 了解一下，当然老师在这里面打开的是官方的普通 buffer 的文档，我们来一起看一看。官方的普通 buffer 文档其实里边有非常非常多的demo，因为我们是用 Java 去做普通巴夫，它是一个什么东西，就是一个序列化，把我们的一些 Java 的对象转成一些二进制的数据，或者是它能够跨语言，把一些 C + +、 c sharp，包括第二次以及go、 Python 等等都可以去支持这么多种语言。所以它是一个非常非常好的跨平台，跨语言的这种序列化的技术。我们的 Java 它一个最大的硬伤就是不能跨语言，这是我们 Java realizable 序列化框架原生的。

[image](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/1057c691-4862-4b5a-a9dd-d8651da73b64/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662LZRBBDL%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T230010Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIEhMcL%2FzUNoY3ZY6FxgBghP2Us0YNUBLoCKyZl5k7M6nAiEAhKR5N%2FzPMGu8dS8INC%2BPuOlXNpMCbWBAH6SDmpkz4t8qiAQIxv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDG2HlF33mCP3k0tY9CrcA18toZj6gI5Cnr71W5ArXYUOA%2B5vNZGdWnk0tFymrU%2BfC%2BtCspLfxX%2FVarOgRIjAsSxJ1xPptcCOorIS2bT3VB57yZBEnpfB06zjv0qYf5Ep09tz685YDx%2F%2BTfNh4VNeLAWd1APz%2BvHXFZFrtb60wLAmqZQoxuRFa6LHToegyIMB%2FtZu5pHgvJxbsfkbov4bpo5Egs%2FVYb%2BlT5lfIfVTiykrBkZTXKZkeOi22tZejPU0573Ie%2F274Dmerap5XuH74AxVZ86BByBCiAXLLziV%2FC3nyar%2Bo4PcEZ3kIYfYW6V1KASbZKUFBw4g9WvEiOgXIaqVMwFyVpZ4bPzSdUjOMAKqFddVDAkrYOi6ZE1sGdOmXNC8tqrnd3ylLxqmi2%2FoOojuN99vXnMVyPnI9If6VSqLXu0M0yNTZ2rNhx1evBCS1M75VMhi1aDedXWPDvq2JdshLvm1X5MPP4WRW9DJAUtMrJejagKdOGf0%2Faue82xntjsai8ue1NKfI6cVZ0eRkDCSsTZYW8hyE0HMdrR3oYoZU27a%2FJYNzU7APNKblDE6GAlO6lG0kDVSTiWxaoP2Vzl2ACjg7OutFC4Oaob8ClSxCrVC30H%2F2uXNi4MRGt5jmwcbxqzWm%2F8LX7N%2FMJq6%2F9IGOqUB9yxU7JpM2UBVEJNjgCpgF15B6PxOJvuXUwzDeXE%2BikwNTvd0Y4ghP3%2FFh8x3CtHRLFb1SOCtjW%2F%2FP4iv1Pg%2F2bt3L6ySh1lac4A%2ByQp%2FyDRnj9PwA4DAhge6VVAhBnE3ZZF8dNKZCuYEflMTevhgQMlXqRiZPoBEoakRR1uDLD9FC8P35DFvgLY2dMfb5q7vtQcCxMUR5DVR4yxmTYryvf4NXHpN&X-Amz-Signature=666ebf5f0583701b79888e387bc3b9442543b34dd36ed1a1c03f58e50dcdc013&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

好了，其实对于Protobuffer，现在目前有 Protobuffer two 跟 Protobuffer three，就是 Protobuf 3 和2。我们现在跟小伙伴们讲的肯定是 probuffer 3，大家一起来看一看左边3。其实 protobuffer 怎么去used，怎么去使用？这里边有官方的一些说明，我就不再去详细的跟小伙伴去读了，其实大家可以快。 might 来定义你的普通发布格式，我的普通发布格式是什么？你看这里边有一个，如果你是普通发货to，首先在文件里面加一个前缀，当然它都是以 d r Pro to 文件。 buffer 这个东西本质上是一个什么？我们要先定义一个数据格式文件，用 Java 去把数据格式进行序列化成 Java 的代码。如果是 c shark 或者是 C + +，也是要按照文件去把它序列化成对应的 c sharp 或者 C + + 的文件，进行二进制的传输。好了，基本上这就是关于我们最简单的一个普通 buffer 的介绍。在这里我们肯定得选择buffer。

[image](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/dcc5f043-5fc8-4e2d-aa6b-53c0bd4af371/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662LZRBBDL%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T230010Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIEhMcL%2FzUNoY3ZY6FxgBghP2Us0YNUBLoCKyZl5k7M6nAiEAhKR5N%2FzPMGu8dS8INC%2BPuOlXNpMCbWBAH6SDmpkz4t8qiAQIxv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDG2HlF33mCP3k0tY9CrcA18toZj6gI5Cnr71W5ArXYUOA%2B5vNZGdWnk0tFymrU%2BfC%2BtCspLfxX%2FVarOgRIjAsSxJ1xPptcCOorIS2bT3VB57yZBEnpfB06zjv0qYf5Ep09tz685YDx%2F%2BTfNh4VNeLAWd1APz%2BvHXFZFrtb60wLAmqZQoxuRFa6LHToegyIMB%2FtZu5pHgvJxbsfkbov4bpo5Egs%2FVYb%2BlT5lfIfVTiykrBkZTXKZkeOi22tZejPU0573Ie%2F274Dmerap5XuH74AxVZ86BByBCiAXLLziV%2FC3nyar%2Bo4PcEZ3kIYfYW6V1KASbZKUFBw4g9WvEiOgXIaqVMwFyVpZ4bPzSdUjOMAKqFddVDAkrYOi6ZE1sGdOmXNC8tqrnd3ylLxqmi2%2FoOojuN99vXnMVyPnI9If6VSqLXu0M0yNTZ2rNhx1evBCS1M75VMhi1aDedXWPDvq2JdshLvm1X5MPP4WRW9DJAUtMrJejagKdOGf0%2Faue82xntjsai8ue1NKfI6cVZ0eRkDCSsTZYW8hyE0HMdrR3oYoZU27a%2FJYNzU7APNKblDE6GAlO6lG0kDVSTiWxaoP2Vzl2ACjg7OutFC4Oaob8ClSxCrVC30H%2F2uXNi4MRGt5jmwcbxqzWm%2F8LX7N%2FMJq6%2F9IGOqUB9yxU7JpM2UBVEJNjgCpgF15B6PxOJvuXUwzDeXE%2BikwNTvd0Y4ghP3%2FFh8x3CtHRLFb1SOCtjW%2F%2FP4iv1Pg%2F2bt3L6ySh1lac4A%2ByQp%2FyDRnj9PwA4DAhge6VVAhBnE3ZZF8dNKZCuYEflMTevhgQMlXqRiZPoBEoakRR1uDLD9FC8P35DFvgLY2dMfb5q7vtQcCxMUR5DVR4yxmTYryvf4NXHpN&X-Amz-Signature=d2f023ffa4d6f3c06c49710063c51265823f5004ec4485dbd150db4acbdbf313&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)


3 红包三这里边有一个指南，当然也有中文的，也有英文的。如果小伙伴们想去学习最佳的学习方式，我还是建议大家去官网看英文的。它必须在最开始文件的开头加一个s，y，n，t，a， x 这么一个标记，标记成括号。3、我自己如果想序列化一个package，在这里就不能叫做 object 了，就不能叫做对象了。我们叫做package，这里面叫做message，叫做 searching request。里边有对应的什么，有对应的 string 类型的 INT32 的，还有一个INT32。
其实普特巴虎给对应着。每一种语言都是有对应的对照。我们其实可以看一下点到 basic Java，点到 basic Java，或者其实你往下拉，你也可以看到这里边有对应的Java，我应该怎么去做。你看这里边就是一个的属性，对应的我们的一些原生的 probuffer 的实现。我们再回过头来往下看后面你看我在最下面。它有各种各样的语言的定义。比如我们这是 buffer 的对应的数据格式像 double 的float，INT64， unit 3264， Saint 32 和 64 以及 fixed 64。
布尔类型包括 string 类型， beta 类型。对应着不同的语言，它有不同的表示。比如我们 Java 里边，我们 Java type 里边， double 对应的就是double， INT32 对应的是Int， INT64 肯定是对应的是 long 就不用说了。这有其他的一些东西哈。往下再走。

[image](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/d1558dd7-2347-45bb-b009-e9408a32e66b/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662LZRBBDL%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T230010Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIEhMcL%2FzUNoY3ZY6FxgBghP2Us0YNUBLoCKyZl5k7M6nAiEAhKR5N%2FzPMGu8dS8INC%2BPuOlXNpMCbWBAH6SDmpkz4t8qiAQIxv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDG2HlF33mCP3k0tY9CrcA18toZj6gI5Cnr71W5ArXYUOA%2B5vNZGdWnk0tFymrU%2BfC%2BtCspLfxX%2FVarOgRIjAsSxJ1xPptcCOorIS2bT3VB57yZBEnpfB06zjv0qYf5Ep09tz685YDx%2F%2BTfNh4VNeLAWd1APz%2BvHXFZFrtb60wLAmqZQoxuRFa6LHToegyIMB%2FtZu5pHgvJxbsfkbov4bpo5Egs%2FVYb%2BlT5lfIfVTiykrBkZTXKZkeOi22tZejPU0573Ie%2F274Dmerap5XuH74AxVZ86BByBCiAXLLziV%2FC3nyar%2Bo4PcEZ3kIYfYW6V1KASbZKUFBw4g9WvEiOgXIaqVMwFyVpZ4bPzSdUjOMAKqFddVDAkrYOi6ZE1sGdOmXNC8tqrnd3ylLxqmi2%2FoOojuN99vXnMVyPnI9If6VSqLXu0M0yNTZ2rNhx1evBCS1M75VMhi1aDedXWPDvq2JdshLvm1X5MPP4WRW9DJAUtMrJejagKdOGf0%2Faue82xntjsai8ue1NKfI6cVZ0eRkDCSsTZYW8hyE0HMdrR3oYoZU27a%2FJYNzU7APNKblDE6GAlO6lG0kDVSTiWxaoP2Vzl2ACjg7OutFC4Oaob8ClSxCrVC30H%2F2uXNi4MRGt5jmwcbxqzWm%2F8LX7N%2FMJq6%2F9IGOqUB9yxU7JpM2UBVEJNjgCpgF15B6PxOJvuXUwzDeXE%2BikwNTvd0Y4ghP3%2FFh8x3CtHRLFb1SOCtjW%2F%2FP4iv1Pg%2F2bt3L6ySh1lac4A%2ByQp%2FyDRnj9PwA4DAhge6VVAhBnE3ZZF8dNKZCuYEflMTevhgQMlXqRiZPoBEoakRR1uDLD9FC8P35DFvgLY2dMfb5q7vtQcCxMUR5DVR4yxmTYryvf4NXHpN&X-Amz-Signature=b26fbd163dea53247a42838ed6ab4df40e5773fd062a8c3a4375210e2ecaf670&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

[image](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/eed0df46-69a6-4c1a-be10-ad5907d2a3d2/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662LZRBBDL%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T230010Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIEhMcL%2FzUNoY3ZY6FxgBghP2Us0YNUBLoCKyZl5k7M6nAiEAhKR5N%2FzPMGu8dS8INC%2BPuOlXNpMCbWBAH6SDmpkz4t8qiAQIxv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDG2HlF33mCP3k0tY9CrcA18toZj6gI5Cnr71W5ArXYUOA%2B5vNZGdWnk0tFymrU%2BfC%2BtCspLfxX%2FVarOgRIjAsSxJ1xPptcCOorIS2bT3VB57yZBEnpfB06zjv0qYf5Ep09tz685YDx%2F%2BTfNh4VNeLAWd1APz%2BvHXFZFrtb60wLAmqZQoxuRFa6LHToegyIMB%2FtZu5pHgvJxbsfkbov4bpo5Egs%2FVYb%2BlT5lfIfVTiykrBkZTXKZkeOi22tZejPU0573Ie%2F274Dmerap5XuH74AxVZ86BByBCiAXLLziV%2FC3nyar%2Bo4PcEZ3kIYfYW6V1KASbZKUFBw4g9WvEiOgXIaqVMwFyVpZ4bPzSdUjOMAKqFddVDAkrYOi6ZE1sGdOmXNC8tqrnd3ylLxqmi2%2FoOojuN99vXnMVyPnI9If6VSqLXu0M0yNTZ2rNhx1evBCS1M75VMhi1aDedXWPDvq2JdshLvm1X5MPP4WRW9DJAUtMrJejagKdOGf0%2Faue82xntjsai8ue1NKfI6cVZ0eRkDCSsTZYW8hyE0HMdrR3oYoZU27a%2FJYNzU7APNKblDE6GAlO6lG0kDVSTiWxaoP2Vzl2ACjg7OutFC4Oaob8ClSxCrVC30H%2F2uXNi4MRGt5jmwcbxqzWm%2F8LX7N%2FMJq6%2F9IGOqUB9yxU7JpM2UBVEJNjgCpgF15B6PxOJvuXUwzDeXE%2BikwNTvd0Y4ghP3%2FFh8x3CtHRLFb1SOCtjW%2F%2FP4iv1Pg%2F2bt3L6ySh1lac4A%2ByQp%2FyDRnj9PwA4DAhge6VVAhBnE3ZZF8dNKZCuYEflMTevhgQMlXqRiZPoBEoakRR1uDLD9FC8P35DFvgLY2dMfb5q7vtQcCxMUR5DVR4yxmTYryvf4NXHpN&X-Amz-Signature=87176e804b591ccc0ed43e4768f4a129ce033b024c64872dbba7fcce4cb24dee&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

比较常见的我们看到布尔类型对不对，对应 Java 里的布尔类型。 string 是对应的 Java 里string。 bits 对应的是一个叫做 bits string，这是普 BUG 3 里边新提出来的一个叫做 bits string。好了，基本上这就是一个格式的对照。我们在编码的时候，我们的 probuffer 文件应该跟你的 Java 实际的类型应该匹配。比如你现在想要一个 Int 32 的，你是一个普通的 Int 类型，但是你定义的时候，你定义的是一个 Int 64 的，可能就会有问题。我举个例子，一定要把图 buffer 的数据跟我们的 Java 一定要对应上。这是提前跟小伙伴们说好的。我们怎么去使用。很简单，在这里边我们首先在我们的 NET 杠 001 项目里边，我们引入对应的 Java 的 buffer 的 Pom Depen 依赖在我们看到这里边。在这我们现在用的是 blue buffer，用的是 371 版本。有了它之后，接下来我们看一看我们怎么去使用 pre buffer。在这里老师已经给出小伙伴们一个文档。我们现在老师用的是 windows 平台，如果是 Linux 小伙伴，你自己去到你是 Mac 你去下载 Linux 就用的包，它里边会有一些，你把它解压开。我现在用的是BUFFER，三点七点幺，我把它解压开之后，其实你会看到 371 下面有这么一些东西，它有一个bin，有一个include，在 bin 下面有一个 Pro to c。


Pro to c 这个就是一个执行文件，就是我们把我们的 pre buffer 所定义的点 Pro to 文件，帮我们去实现这种 Java 的代码，它会帮我们直接生成 Java 的编码，所以工具还是非常有用的，一定要去使用include。下面就不用看了哈。


一些文档。好了，接下来跟小伙伴们一起实际的去操作一下，看看到底应该怎么去学习它。在这里老师有一个示例。首先我们 TOC 文件哈，一般来讲，老师在这里是直接把它 copy 到我们的项目的。根目录下，我把你看，我把它直接 copy 到真泡沫，其实是平级的哈，看见了，跟 Pom 是平级的。根目下 Pro to c。现在我把它 copy 到我们项目里。接下来老师做的事情是，比如我们在 windows 下，我们怎么去运行脚本让它去生成。你肯定得选择一个 b a t 文件，我们在这里可以把b、a、 t 文件也 copy 过来。放到这里。我们用 eclipse 的 open 的方式把它打开。
Open with text editor。
好了，现在我们来看一看这个东西里边这张单。这是我之前写的。这其实就是我们正常的 windows 的执行。点什么什么？这应该是点星点 Pro two 的一个文件。我要执行把它执行完了之后运行到什么目录下，安装到哪儿。其实我是想这么去做，我是想说我想把它帮我去运行到我们的s、r、c，因为我们目录 man 杠加 2 下就可以了。
好了，我文件起个名字。起什么？我们来看一看。比如现在我文件叫做很简单哈，我们就给它叫做user。我在这里边叫做user。我现在想定义一个 user 点 pull 文件，可以吧，这是没问题的。好了， user 点 Pro 文件，我们来看一看我怎么去建。比如如果我想带一个目录，就加一个目录就好了。比如 Pro to 文件夹，我在这里边再新建一个folder，叫做 Pro to，有了 Pro to，我再创建一个 user 点 Pro to 这么一个 file 文件。注意看， user 点 Pro to 接下来就应该编写我们的格式了。现在编写格式的时候一定要参考官方的文档。


首先第一句话一定要带上的就是你的版本，我的普通 buffer 的版本是什么？肯定是 3 版本。接下来我的 put buffer 它应该怎么去定义它自己的格式，就是你的 packing 格式，这个看你自己实际的需求。其实在 put buffer two 跟 put buffer three 3 的时候，它前面省略了一个叫做 require 的。其实大家可以看看。我们在 3 的时候直接写的，非常简单，就是 string 类型，加上名字123，表示占位的第一个位置，第二个位置，第三个位置。它并不是负值。我们看一看普通 buffer two 第二版本的时候可能需要什么。 required optional 就是必须的，可选的，可操作的。就是 2 的时候它在变量前面，它有一个这种修饰服务， 3 的时候它已经完全把变量修饰这块给去掉了。这个是需要小伙伴们一定要注意的一点，对它有一个修饰的。


好了，我们再回到普巴夫3，我们回到这个demo，比如现在我有几个数据，比如我有一个 string 类型的，比如像个 user ID，对不对？我就可以直接。当然我最开始的时候肯定要给这个人，我把它直接 copy 过来。比如我们现在定义的是user，我们在这里边可以有一个什么，咱们叫做user。


写完了之后，第一个数据我们叫做 string 类型的，咱们叫做 user ID，可以，这是第一位。第二个 INS 32，我们可以给他一个，叫做 age 这个年龄。第三个我们再给它一个，比如它是一个四川的小的，我们叫做username，可以吧，username。第三个是这样的。第四个比如我们再给它一个数组类型，可不可以数组类型叫做repeating， repay dead，每个数组也是string，比如我们叫做一个爱好，叫做favorite， favorite 爱好它就是一个数组。


搞定这件事情之后完了吗？其实小伙伴们你要注意搞定这件事情，你现在只是定义一个结构，你的我们来想一想我们差什么。现在是我要执行刚才我们写的点 pull 文件，就是user，点 pull 文件帮我输出到目录下。但是你是不是应该有一个具体的格式的定义你的到底输出到目录下哪一个，包括文件名称叫什么。
所以在这里边普通 buffer 给你提供了两个option，就是一个选项，一个叫做 Java package，还有一个叫做 Java outer class name。这个是小伙伴们一定要注意的，在 Java 的代码里边，你去点到 Java 里面，它也会有。


我在这里就不详细的领小伙伴们看了。比如我们现在再创建一个新的package，叫做 Com 点 e f x y 点 net step buffer protein buffer。可以了。就这样现在我就整个在这个目录下，我把它 copy 过来。我在这其实我一样带上一个什么东西叫做 option 杠 Java sorry option 选项 Java 杠什么？Package？ Java 杠 package 是等于什么？我们可以把我们刚才所定义的目录我们 user 文件对应的数据包就是 message 数据包。


我要放到目录下对不对？给我生成它输出的 class name 叫什么？我还要有一个叫做 option 杠 Java 杠 alter 杠 class 小写的哈，注意 name 我们比如在这里面我们可以给它叫做 user modular，可以modular，这是一个模块。 User modular。


现在我编写完了以后，现在基本上我们都已经搞定了，我就直接可以进行运行了。因为我的 PUC 文件和 build 文件都已经搞定了，都已经写完了，包括我的格式已经定义好了。接下来剩下一个问题就是什么我们要去做一个什么输出。我现在直接点到我的项目里，我的项目现在是第 1V 001004，找到我们刚才的 NET 001，看见了吗？ BAT 文件我们直接现在直接可以双击运行，直接双击运行这里边回车就可以了，因为它有一个暂停，现在我去刷新一下。


OK 同学们，请看我刚才定义的空的包，下面肯定有东西了。多了一个叫做 user modular。点 Java 这么一个文件，我们把它打开它其实它特别的多哈代码，因为它里边是帮你做了复杂的序列化。这种转码工作基本上差不多。我们刚才定义的这么小的东西，在 1000 行左右，如果你里边的属性或者是句子数据多一些，可能会上几千行。
我们现在已经做完的一个准备工作，我们首先第一点把普度 c 跟 build 点 bat 创建好，这个路径一定要写对。接下来的一件事情就是我们要定义自己的点 pull 文件。我们的公用格式Java，我们就用 Java 去把它生成，按照普通 c 把它生成对应的 Java 文件，刚才 user module 了就好了，接下来你就可以去使用它了。怎么去使用？我们来一起简单的去做一做使用。当然这个使用其实也是非常简单的。


我们再来一个test，我们在普通 buffer 下面，我们再建一个类，叫做 test user test pro to buffer，可以吧。 test to buffer for 就这么写了。 OK 所以我建议一个测试文件对 user mode，让咱们小伙伴们看一看我生成了这个东西，我怎么去用？我怎么去做序列化跟反序列化。既然我现在要做序列化跟反序列化，所以我现在应该定义两个方法，一个是序列化方法，还有一个是反序列化方法。我们现在直接在这里边先写一个主函数。先写一个主函数，我们去定义两个方法，一个叫做序列化方法，在这里sorry，在这里我直接叫做 public static。比如序列化方法一般是一个 object 去转成一个 beta 字节数组，是不是？所以我们就来一个二进制，因为网络传输肯定是二进制的字节数组，我们叫做 zero object to。


对此，t，y，t，e， s 有这么一个方法对不对？将我的对象转成什么？转成具体的什么？一个贝塔职业数组老师在这里就不用传这个类型了，因为我们都知道我们肯定是针对于我们刚才所写的 user 去做的。怎么去用？很简单，我们不是有 user model 了吗？我们直接把它拿过来说。


user module 的，你能直接点？下面我们使用的就是我们刚才序列化生成的 Java 文件，我们点 user 取到真实的对象，调一个方法叫做 new builder，创建出来一个 build 对象。这个 build 对象有了之后，我们取到 build 对象一定是什么？一定是 probuffer 的build，然后叫做 user build，把它搞出来。我最大化一下哈。
有了 user build 之后，接下来是做什么事情？你现在已经有 build 了，大家都知道建造者模式。我有了 build 以后，接下来的事情就是对它进行一些设置。比如我们 user 里面有什么属性， set user ID 是不是， user ID 是多少，我们随便给他一个就可以了。比如 user ID 叫做1001，可以继续去set。它其实是支持链式变成的。比如我把它这么去写一下，然后点在 set age a 值，比如是 30 岁，再往下去点set。我们有三个属性，是不是还有一个 user name， user name 在这里边，我们叫做装修。


再来一个。第二 set favorite 看见了吗？favorite，它里边有两个，有一个value，你可以去，当然这个是 value 的 index 方式去set。还有一种方式叫做add，我们看 add all favorite 看见了，还可以单一个的add，比如 add 一个内容对不对？因为它是一个什么？刚才我说它是一个数组。我们所看到的我们刚才所定义的那种类型，就叫做repeated，它是一个数组，是一个字符串数组，所以我们可以一个一个的去进行设置，比如 add favorite。数组，我们比如随便去写它的爱好是什么，比如足球，善爱的一个favorite，比如乌马。
好了，我就可以创建完了。是不是我的 build 搞定了之后，最后当然有了 build 之后，最后你应该调一下build，其实可以直接返回了哈。我在这里就是为了让大家看清楚，我把步骤分着去写。我可以这是第二 build 方法去创建它，真正创建就会返回一个真的 user 对象。当然这个 user 是 put buffer 的user。我定义好的 user 是这个user，我们叫做user。这个是一个什么？前面就是我创建一个对象的过程，我怎么去做序列化？是不是我的序列化是一个什么概念？我们在这里简单回顾一下我的序列。话说白了，我非常简单。我先把结果写完哈。我们直接吐一个贝特瑞看，直接就转成一个数组了对不对？我们可以打印一下。希特瑞打印一下。我说打印一下。怎么打印？叫做我就直接用我们 Java 里边的尔瑞斯点 to spin，直接把一个字节数组。当然我接收一下哈。
B y t e。


咱们叫做 data 来接收一下。放在这里。其实这种方式跟我们原生的 Java 序列化有什么区别？老师在这里。当然最后你应该把 data 去返回哈。我只不过是多了一个打印。这个序列化方法其实就做完了。我们在这里打一下注释。


序列化机制我们原生的 Java 的序列化。我们都知道原生的 Java 的序列化机制，它是使用 Java 的，你要实现 Siri 来接口。比如一个 Int 类型，我们应该知道 Int 类型在我们的内存中是占多少个长度，是占 4 个字节长度。如果是 Java 的序列化，它就会按照类似这种。怎么说？类似于这种大端小端的序列化的方法，把数据写到内存中。这个时候，因此我们真正的一个数值。比如我举个例子哈，我现在这个数值就是因为我们知道 Int 的取值范围是很大的，对不对？是比较大的你。比如一个非常小的数，比如我 Int a 等于 10 和 Int a 等于这个数，这是两个 Int 值，比如 a 等于1，不是 10 了，或者等于2，随便搞一个值。和我们 Int a 等于这个数。这是很长的对不对？如果你想想我们Java，虽然它就是四个长度，它有最大的范围。你想想像这两个数字，他们在做序列化的时候，肯定序列化的大小是不一样的。肯定有的是确实占满了 32 位。四个字节长度 32 位。有的像这种2，它是非常小的一个数据，它可能占不了实际的那么大，它可能就占几个。所以我们 Java 的序列化方式就是按照你数据类型的长度去匹配的。无论你这个数字到底是 2 还是这么大一个数，它都会去占四个字节 32 位。在这里是我要跟小伙伴们说的，谢谢。


扎瓦德序列化无论真实的 Int 类型，数值大小，实际占用多少个字节，在内存中，都是以什么以四个长度，也就是我们的比如 32 位来去放的，说白了什么就浪费了。你大的可以占四个字节 3. 21，但是你小的它本身实际没有那么大。所以我们的 Google 它的普buffer，它其实为什么序列化之后的码流特别小，序列化之后马刘晓在网络传输它的性能就高它。
我们来说一说普通 buffer 序列化积累，他是怎么去做的。他是按照实际的数据大小去动态伸缩的，它可以做一个动态的伸缩，你比如我 20 进可能就占不满四个字节长度，它就会帮你去做一个实际的算法，它这个算法伸缩就是在我们刚才所声称的 user modular 里边它去做的事情。然后因此很多时候我可以说我们的 INT 数据并没有占用，并没有实际占用到 4 个世界，对不对？所以我们普通 buffer 序列化后，一般都会比 Int 类型的占用长度要小很多。


比 Int 类型的长度，我指的是比 Java 的序列化，所以我们会选择 Google 的普通buffer。这是跟大家简单说一下普通 buffer 为什么他这么流行，他原因就是因为他自己做了一些动态的算法。好了，接下来我们做好了序列化之后，比如我们现在想去做反序列化，反序列化就很简单了，就更简单了。我在这里打一个注释，这是序列化。我们再写一个反序列化对不对？把一个贝特字约数组去帮我去变成一个实际的 Java 里的对象。我们在这里把它 copy 过来改一下，是不是叫做 serializable bait to object？直接这样去改造就好了。给我进来一个贝特字节数组，哈，比如叫data。当我把它变成一个 Java 类型，在反序的时候，其实是非常简单的，它直接可以做return，直接可以写，直接用我们的modular，第二user，第二format。


我记得是 pass match。你看它其实支持很多，比如支持一个贝特斯数组，支持一个 buffer 类型，还支持像贝特string，还有一些其他的，像我们的 input stream 都可以。所以它其实是不能非常强大的哈。我们现在之前是序列化成了一个字节数组，所以反序列化的时候直接拿过来就好了。当然它这里面需要抛一异常，我们的序列化失败的 invited exception，我们直接在筛开始也可以哈，都可以。比如序列化失败的时候，我们 return 一个null，可以吧，这是没问题的。现在我们的序列化跟反序列化方法都已经写完了哈。
序列化这个是反序列化好，其实我们现在做一个小的测试。这个测试其实很简单，我们现在先因为我们的运作对象已经写到这了，我们直接调一下就好了，对吧？很简单，我直接调一下这个方法，它是静态的，他帮我返回一个贝特基数组，就是data。接下来我们再做一件事情，调下就好了。我们来做一次转换。这里边返回的是一个 user u，等于叫做 serizable bait to object。我们序列化跟反序化完了之后，我再把这个东西还原回来，我打印一下，我看看到底是不是我想要的结果。比如我在这里说现在我们叫做 user ID，是不是 user ID？它是什么？它就是我们的 user 点 get id。你可以把它当成一个普通的 Java 对象去用。


这个user。它其实是在我们 module 的里边内置的一个，看见了吗？它是在我们整个叫做我们之前生成的，叫做 user module 里边帮我们去内置的一个 user 类。看见了。它既承自 Google to buffer，我们 generator message V3。注意这个也我们普通 buffer 它第三个版本有的改进的地方就是它。一般来讲要用这个类叫做 generator generated message。这里有没有V3，我们再打印一下。把我们那几个属性都打印出来就好了。
一共 4 个属性，是不是 user age，咱们叫 get age name。还有一个叫做favorite，在这里边直接还有一个是favorite。 favorite 其实它是一个list，它从 Java 转出来的时候就是一个list。你看get，咱们叫做 favorite list。看到吧，它就是一个list，我们在这里边 at the name。


现在搞定了之后，我们来一起运行一下。我们直接 run ads， Java application 去运行一下它就好了。右键 run ads Java application 来运行一下。同学们，请看现在我把它改出来的。你看序列化的码流其实就特别少，如果小伙伴们你要不信，你可以用原生的。什么原生的serious，就 Java 的 object input out of stream 序列化，你来试一试。你看一看它序列化的大小是多大。刚才我们打印出来的结果这么长，看见了这么长一个数组。序列化之后，反序列化成不成功？肯定成功了，必然成功了，对吧？因为我们看到 user ID 是 100130 张三足球路曼。这是我们打印出来的序列化跟反序列化。这也就是我们的普通 buffer 的一个学习。好了，我希望小伙伴如果没接触过普通 buffer 的你，课下一定要把这个 demo 去做出来，跟着老师的节奏一点点去走就好了。我们这节课先讲到这，感谢小伙伴们。

