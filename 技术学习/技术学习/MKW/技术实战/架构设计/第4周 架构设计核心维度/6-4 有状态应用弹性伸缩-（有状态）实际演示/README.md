---
title: 6-4 有状态应用弹性伸缩-（有状态）实际演示
---

# 6-4 有状态应用弹性伸缩-（有状态）实际演示

[image](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/06b68064-20d6-4132-8831-db739769dd2b/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UDB6ZLEC%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T230446Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIETNSZvTU3iq5qfciqAESzJDE2IevFTtHr%2BpP5V5mNQHAiEAtrsXoFV%2FBmM3SjaTanj6FjTCRokHZW3ldbgT7%2FiUmYIqiAQIxv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDP4H%2Fu%2FhDWlDZpt0PircA5y%2BXIGtWj4z9Xrv2DK3h6qtozgoMhD%2FHJMqBc0NOMRONiUFmqTX8zC6ik9P6DDbJSOxyEDMs5vFPNM53fBUj%2FHbOZeWU8HqNNxP52GsL6fbMefaN3JR4RzIppvrVHVFy80hEGMltmxkVNgmOSoGN10i4n0Jntb1rNng6v2aV49BNRFejq8WPLUNUZ%2FLG5fngWwj111e30rKhynSQEFmnpIBjGta7OQsJaCI7lKm8%2B370KGDx%2B%2FDcqTljzkRsBTCO8geOeqd735grgD34J89uVTtRy36XPWbO1yLzpm9Wk1U9ajvp3k2pr6Y3jrMcDPZbbZ5IJLtUtCgOn02eTuhQYQQMfyZqmVNiO%2F97Y1Puc9WQv%2FFsbraB2%2BnXMMe0wRuec3dBp%2FHnXBBm1T61%2FILSIQj3Thwl7n4%2BfRChn%2Fg15tHQrv8KUk13ty%2FJb4vxcj%2B8ipJd7YR99txWHk4NTapE6Jmd7LlhgzLZ9A1AF6ofN4V10cu8mo1QxgGxONuFiiBDCi5vkZicFyNJPq%2FECv6%2F6uIZtYrxxOuXVlknpj2et6mrpXG8uKGrFo1%2BBtkAs2Sejo2rvrBdIwSuG3JjnD88hWSSdQhO0%2Bpnh8TiwvS07hxIsVhwW3cZpV6w28iMPC3%2F9IGOqUBq6rEWy%2BudV6%2FT5%2FOfXW7SKLwsQjdKcsLuilAvQFNcT11DABJhECBHJNJ5X8wWluoiU%2F4%2F02k3d0YoFlRRK6JTdgK38HdWog41wc596sHFsb2eYaXgk5o3CXdhnovXjXYq5NeUaa0qxHnp9llMemyHbOmLInsfLH7TCB%2Bh6V%2BuYy1RKsSaMwB0h5ryhI0AAyc2lYD7eLH9S2acXZz3qkiSZgxJ6OB&X-Amz-Signature=62e397c6302c0d806979cd1dad86bfe746bf07346b8eb497895c3290cbc16bc1&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

[image](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/1fcaa9ec-6a44-429d-8098-76325ad61ab3/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UDB6ZLEC%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T230446Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIETNSZvTU3iq5qfciqAESzJDE2IevFTtHr%2BpP5V5mNQHAiEAtrsXoFV%2FBmM3SjaTanj6FjTCRokHZW3ldbgT7%2FiUmYIqiAQIxv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDP4H%2Fu%2FhDWlDZpt0PircA5y%2BXIGtWj4z9Xrv2DK3h6qtozgoMhD%2FHJMqBc0NOMRONiUFmqTX8zC6ik9P6DDbJSOxyEDMs5vFPNM53fBUj%2FHbOZeWU8HqNNxP52GsL6fbMefaN3JR4RzIppvrVHVFy80hEGMltmxkVNgmOSoGN10i4n0Jntb1rNng6v2aV49BNRFejq8WPLUNUZ%2FLG5fngWwj111e30rKhynSQEFmnpIBjGta7OQsJaCI7lKm8%2B370KGDx%2B%2FDcqTljzkRsBTCO8geOeqd735grgD34J89uVTtRy36XPWbO1yLzpm9Wk1U9ajvp3k2pr6Y3jrMcDPZbbZ5IJLtUtCgOn02eTuhQYQQMfyZqmVNiO%2F97Y1Puc9WQv%2FFsbraB2%2BnXMMe0wRuec3dBp%2FHnXBBm1T61%2FILSIQj3Thwl7n4%2BfRChn%2Fg15tHQrv8KUk13ty%2FJb4vxcj%2B8ipJd7YR99txWHk4NTapE6Jmd7LlhgzLZ9A1AF6ofN4V10cu8mo1QxgGxONuFiiBDCi5vkZicFyNJPq%2FECv6%2F6uIZtYrxxOuXVlknpj2et6mrpXG8uKGrFo1%2BBtkAs2Sejo2rvrBdIwSuG3JjnD88hWSSdQhO0%2Bpnh8TiwvS07hxIsVhwW3cZpV6w28iMPC3%2F9IGOqUBq6rEWy%2BudV6%2FT5%2FOfXW7SKLwsQjdKcsLuilAvQFNcT11DABJhECBHJNJ5X8wWluoiU%2F4%2F02k3d0YoFlRRK6JTdgK38HdWog41wc596sHFsb2eYaXgk5o3CXdhnovXjXYq5NeUaa0qxHnp9llMemyHbOmLInsfLH7TCB%2Bh6V%2BuYy1RKsSaMwB0h5ryhI0AAyc2lYD7eLH9S2acXZz3qkiSZgxJ6OB&X-Amz-Signature=dee0375da4048c8b46c34025f172674e84568fd7760331eaf7050f1939280754&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

架起需求到落地的桥梁，构建 i t 新蓝图。我是张飞扬。上一节我们用阿里云实战了一下，看了下如何采用 Kubernetes 加以 steal 加 k native 实现应用从 0 到 1 的扩展，以及从 1 到 0 的收缩。当然，如果你这个应用是什么，是 CPU 内存消耗型，也很容易实现从 0 到n，从 n 到 0 的伸缩。
之所以我们能实现这样一个伪命题， 0 到 n 的转换，原因在于什么？**我们不是靠应用本身来进行监控，而是有独立的眼和独立的脑来进行观察和决策，最后通过 Kubernetes 实现底层的容器的扩展。但这一套应用，这套方案再强大，也只适合于无状态的应用的弹性伸缩，一旦碰到有状态应用，它就束手无措了，那我们如何来处理有状态应用？**这就是我们今天要聊的话题。


通常我们可以把有状态应用分成两个类，

[image](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/299d708e-a781-4ba3-bf0a-a32c2c248108/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UDB6ZLEC%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T230446Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIETNSZvTU3iq5qfciqAESzJDE2IevFTtHr%2BpP5V5mNQHAiEAtrsXoFV%2FBmM3SjaTanj6FjTCRokHZW3ldbgT7%2FiUmYIqiAQIxv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDP4H%2Fu%2FhDWlDZpt0PircA5y%2BXIGtWj4z9Xrv2DK3h6qtozgoMhD%2FHJMqBc0NOMRONiUFmqTX8zC6ik9P6DDbJSOxyEDMs5vFPNM53fBUj%2FHbOZeWU8HqNNxP52GsL6fbMefaN3JR4RzIppvrVHVFy80hEGMltmxkVNgmOSoGN10i4n0Jntb1rNng6v2aV49BNRFejq8WPLUNUZ%2FLG5fngWwj111e30rKhynSQEFmnpIBjGta7OQsJaCI7lKm8%2B370KGDx%2B%2FDcqTljzkRsBTCO8geOeqd735grgD34J89uVTtRy36XPWbO1yLzpm9Wk1U9ajvp3k2pr6Y3jrMcDPZbbZ5IJLtUtCgOn02eTuhQYQQMfyZqmVNiO%2F97Y1Puc9WQv%2FFsbraB2%2BnXMMe0wRuec3dBp%2FHnXBBm1T61%2FILSIQj3Thwl7n4%2BfRChn%2Fg15tHQrv8KUk13ty%2FJb4vxcj%2B8ipJd7YR99txWHk4NTapE6Jmd7LlhgzLZ9A1AF6ofN4V10cu8mo1QxgGxONuFiiBDCi5vkZicFyNJPq%2FECv6%2F6uIZtYrxxOuXVlknpj2et6mrpXG8uKGrFo1%2BBtkAs2Sejo2rvrBdIwSuG3JjnD88hWSSdQhO0%2Bpnh8TiwvS07hxIsVhwW3cZpV6w28iMPC3%2F9IGOqUBq6rEWy%2BudV6%2FT5%2FOfXW7SKLwsQjdKcsLuilAvQFNcT11DABJhECBHJNJ5X8wWluoiU%2F4%2F02k3d0YoFlRRK6JTdgK38HdWog41wc596sHFsb2eYaXgk5o3CXdhnovXjXYq5NeUaa0qxHnp9llMemyHbOmLInsfLH7TCB%2Bh6V%2BuYy1RKsSaMwB0h5ryhI0AAyc2lYD7eLH9S2acXZz3qkiSZgxJ6OB&X-Amz-Signature=34b99d7bfa4f69279c1f0cb86f9acb4889f2d8fb97502a8a2e1c47f31519d344&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

两类一类是类似于像 red height 的GFS，或者是类似于像 Oracle 的 ASM 这种什么集群式的共享磁盘系统，它的特点是它的应用后台一样读写硬盘，那这个硬盘呢？如果你是多节点的环境当中，它们是读写共同的，一个硬盘就变成一个节点在写，很多个节点在读。


这样的情况，它是硬盘，它可不是一个外部的服务，这是集群里面经常采用的共享磁盘方式，这个方式既能保证我们磁盘的 QUORUM 仲裁盘是什么共享的，也能保证它的数据是同时可以访问的。那另外一种很常见的场景，比如像Cassandra，Hadoop，甚至于各种各样的 no secure，都采用了 share nothing 的方式。也是很多个节点，它们依赖于硬盘里面的数据，但是每个节点的硬盘只是其中的一个分片，只有让多个节点它们的分片共同才能组合成应用的完整数据。这是一种 share nothing，但是仍然是有状态的应用。这两种应用它的伸缩方法各不相同，我们分别来看一下。


```java
Apache Cassandra 是一个高度可扩展的、分布式数据库系统，设计用来处理大量数据的写入和读取操作，而不牺牲性能。Cassandra 提供了一种无中心化的分布式数据模型，这意味着没有单一的控制点或瓶颈，所有的数据都可以在集群中的任何节点上访问。这使得 Cassandra 非常适合需要处理大量数据的应用程序，尤其是在那些对数据一致性要求较低，但对性能和可扩展性的需求较高的场景中。

### 为什么使用 Apache Cassandra？

1. **高可用性和容错性**：Cassandra 设计成能够自动检测和修复节点故障，无需人工干预。此外，它还具有数据复制和分片的能力，以确保数据的冗余和可用性。
2. **线性可扩展性**：Cassandra 可以通过添加更多的节点来水平扩展，以处理更多的数据和请求。这意味着应用程序可以随着数据增长而扩展，而不会影响性能。
3. **强大的写入性能**：Cassandra 的设计重点之一是优化写入性能，即使在大规模数据写入的情况下也能保持高性能。
4. **灵活的数据模型**：Cassandra 使用一种灵活的数据模型，允许开发者根据业务需求自定义数据模式，而不是受限于固定模式。
5. **跨地区部署**：由于其分布式特性，Cassandra 可以很容易地部署到不同的物理位置，从而提高数据的可用性和减少延迟。

### 场景下的使用

- **实时分析**：Cassandra 适合处理实时数据分析，因为它可以快速地处理大量的写入和读取操作。
- **日志聚合**：对于需要长期存储和分析大量日志数据的应用，如网络流量监控、安全事件记录等，Cassandra 提供了高效的存储和查询能力。
- **内容管理系统（CMS）**：CMS 需要处理大量的用户生成内容和访问请求，Cassandra 的高可用性和可扩展性使其成为理想的选择。
- **游戏服务器**：在线游戏需要处理大量的玩家数据和交互，Cassandra 的高性能和可扩展性可以帮助游戏服务器处理这些需求。
- **物联网（IoT）数据**：IoT 设备产生的数据量巨大，Cassandra 能够有效地存储和处理这种结构化和非结构化的数据。

总之，Apache Cassandra 是一个非常适合处理大规模数据和高并发读写操作的数据库系统，其高可用性、可扩展性和灵活性使其成为许多企业和应用程序的首选。

Citations:




------------------------------------------------------------
Hadoop是一个开源编程框架，用于在分布式计算环境中处理大型数据集。它允许用户轻松实现海量数据的分布式存储和分布式计算，可以部署在数以千计的普通计算机上，并且集群的规模可以方便地扩展[3]。

使用Hadoop的主要原因包括：

- **处理海量数据**：Hadoop特别适合处理TB级别或PB级别的大数据集，能够存储各种数据集并进行数据并行处理[1]。
- **成本效益**：Hadoop通过使用价格实惠的标准商业硬件提供计算和存储服务，使得每TB存储成本远低于传统的专有解决方案[1]。
- **容错性**：即使在大型集群上运行作业时单个节点可能会失败，Hadoop的设计允许数据在整个集群中复制，从而在发生磁盘、节点或机架故障时轻松恢复数据[1]。
- **开源框架的创新性**：Hadoop由全球社区支持，专业人员团结在一起，能够更快、更高效地引入新概念和功能，缩短产品上市时间[1]。
- **广泛的应用场景**：Hadoop被广泛应用于研究、生产数据处理和分析、AI和机器学习、云计算等多个领域，满足不同行业的需求[1]。

总之，Hadoop的出现是为了更快速、更可靠地处理海量大数据，它通过分布式计算和存储技术，为公司收集、处理和分析大数据提供了更高的速度和灵活性，同时降低了成本和提高了数据处理的可靠性。

Citations:
[1] https://cloud.google.com/learn/what-is-hadoop?hl=zh-cn#:~:text=Apache%20Hadoop%20%E8%BD%AF%E4%BB%B6%E6%98%AF%E4%B8%80%E4%B8%AA,%E7%BA%A7%E7%9A%84%E5%A4%A7%E5%9E%8B%E6%95%B0%E6%8D%AE%E9%9B%86%E3%80%82
[2] https://www.zhihu.com/question/333417513
[3] https://blog.csdn.net/qq_43842093/article/details/132131033
[4] https://blog.csdn.net/Shockang/article/details/117266918
[5] https://zhuanlan.zhihu.com/p/54994736
[6] https://www.51cto.com/article/601060.html
[7] https://www.dataapplab.com/a-beginners-guide-to-hadoop/
[8] https://chu888chu888.gitbooks.io/hadoopstudy/content/Content/3/chapter3.html
[9] https://www.cnblogs.com/binarylei/p/8903601.html
[10] https://thedatascientist.hedwig.pub/i/the-data-scientist-7-hadoop
```


对于第一种方法相对简单，如果你是共享磁盘，我们可以用 cloud native 12 原则里面的一个原则，把所有共享的都变成后台服务。这样一个原则，把之前共享磁盘变成一个共享的后台存储服务，这个服务可以是个API，可以是一个远程文件系统，也可以是其他的各种方式。不管哪种方式，只要你把硬盘变成一个服务，可以拉到远端，可以通过网络来传输。


这种情况下，其实你就变成了应用的无状态了。你本身应用是不是无状态了？通过这种方式你就解耦了你的应用和数据。所以一旦你的应用变成无状态，你很容易采用容器的沿挠手实现弹性的伸缩。如果是第二种情况就相对复杂了，你是什么？你的应用必须要有写一份数据，而且你这个数据还不够完整，那这时候你很难把你的数据剥离出去，必须还是在你应用本身在管理。比如像我们的什么MongoDB，你很难把芒果 DB 里面每个分片的数据剥离出去，形成一个独立的服务，让芒果 DB 变成无状态，那是很困难的。那这个时候我们要采用一些合适的方法，把我们的这种 no SQL 或者是我们的这种大数据的集群进行一个合理的管理，然后通过 cap 理论里面的少量的牺牲来就形成尽量的弹性伸缩的能力。


好，我们来仔细的看一看 share nothing 模式该如何做？先看一看共享磁盘模式，它的核心的话就是一句话，

[image](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/cb0047ca-4a03-4cfb-865a-3ddacd90723b/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UDB6ZLEC%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T230446Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIETNSZvTU3iq5qfciqAESzJDE2IevFTtHr%2BpP5V5mNQHAiEAtrsXoFV%2FBmM3SjaTanj6FjTCRokHZW3ldbgT7%2FiUmYIqiAQIxv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDP4H%2Fu%2FhDWlDZpt0PircA5y%2BXIGtWj4z9Xrv2DK3h6qtozgoMhD%2FHJMqBc0NOMRONiUFmqTX8zC6ik9P6DDbJSOxyEDMs5vFPNM53fBUj%2FHbOZeWU8HqNNxP52GsL6fbMefaN3JR4RzIppvrVHVFy80hEGMltmxkVNgmOSoGN10i4n0Jntb1rNng6v2aV49BNRFejq8WPLUNUZ%2FLG5fngWwj111e30rKhynSQEFmnpIBjGta7OQsJaCI7lKm8%2B370KGDx%2B%2FDcqTljzkRsBTCO8geOeqd735grgD34J89uVTtRy36XPWbO1yLzpm9Wk1U9ajvp3k2pr6Y3jrMcDPZbbZ5IJLtUtCgOn02eTuhQYQQMfyZqmVNiO%2F97Y1Puc9WQv%2FFsbraB2%2BnXMMe0wRuec3dBp%2FHnXBBm1T61%2FILSIQj3Thwl7n4%2BfRChn%2Fg15tHQrv8KUk13ty%2FJb4vxcj%2B8ipJd7YR99txWHk4NTapE6Jmd7LlhgzLZ9A1AF6ofN4V10cu8mo1QxgGxONuFiiBDCi5vkZicFyNJPq%2FECv6%2F6uIZtYrxxOuXVlknpj2et6mrpXG8uKGrFo1%2BBtkAs2Sejo2rvrBdIwSuG3JjnD88hWSSdQhO0%2Bpnh8TiwvS07hxIsVhwW3cZpV6w28iMPC3%2F9IGOqUBq6rEWy%2BudV6%2FT5%2FOfXW7SKLwsQjdKcsLuilAvQFNcT11DABJhECBHJNJ5X8wWluoiU%2F4%2F02k3d0YoFlRRK6JTdgK38HdWog41wc596sHFsb2eYaXgk5o3CXdhnovXjXYq5NeUaa0qxHnp9llMemyHbOmLInsfLH7TCB%2Bh6V%2BuYy1RKsSaMwB0h5ryhI0AAyc2lYD7eLH9S2acXZz3qkiSZgxJ6OB&X-Amz-Signature=8854cef70258f26a7bb898ee77518c8e162ed39b1409aa23a8ea373b60282f6c&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

向无状态应用转移，一旦你是共享磁盘，我们就有看一下你共享的磁盘到底是什么样的情况。如果你是完全是结构化数据，比如说共享一个硬盘，那这个时候你可以把你的硬盘里面的这些结构化数据转到数据库里，不管是传统的数据库，还是相对来说非传统的，比如文档数据库等等，一旦它是一种数据库形式的内容，它它就能比较好的支撑整个结构化的组织。同时你也可以把信息拉到远端，使你的应用变成什么完全的无状态。


但是如果你的磁盘里面的数据完全是非结构化的，比如说是我是很多的慕课的视频，也比如说是我是一些特殊的这个大型的照片，或者是一些工程的绘图，这个时候你就不适合用结构化的方法来管理。什么样的方法比较适合对象存储？就很适合，对象存储刚刚出现的时候，它一个对象不能超过1G，过了两年以后它有限制不能超过4G，而到了今天我们对象存储一个对象，完全可以放一张蓝光盘，你完全可以通过十几 g 的一个大文件放成一个对象。同时我们整个对象存储的大的存储空间也没有 1T 的要求，我们可以 10T 或者几十 t 来存放完整的一个对象的一个整个bucket。
那通过这种方式，你可以完全把非结构化的数据扔出去，通过对象存储的 API 来实现访问，你可以并发读并发泄，都没有问题，所有的应用的状态全部剥离到对象存储里面，就实现了你应用的无状态。同样道理，如果你不采用对象存储，你可以采取缓存，或者有些数据是偏搜索型的，你可以跟搜索引擎对接，最终实现你的应用变成无状态，所有的状态留存给其他的节点或者是对象存储，或者是搜索引擎来实现。那这样的情况下，你的逻辑复杂的应用一旦变成无状态，就很容易进行弹性伸缩喽，它的收益也非常大。


还有更进一步，有这样的情况就是一旦我们什么能够解耦文件系统，在新型的环境当中，尽量少用文件系统，多用对象存储这种 API 的访问方式，甚至于其他的一些网络存储方式，比如说一旦你的文件可以以对象的形式进行存储，它也能够什么？让 CDN 直接去跟对象存储沟通？ CDN 大家在前面付杨老师的课里已经反复提得到， CDN 是第一道缓存，最适合命中的一道缓存，一旦它命中以后，它可以减少我们整个数据中心，整个机房的数据流的压力，它离用户是最近的。


所以很多 CDN 的厂商直接提供对象存储的内容的进一步缓存，也就是当你要访问的这个对象一旦在 CDN 上被命中以后，后续你的应用不用管，后续你的对象存储也不用管，一切都在 CDN 这个网络缓存得以实现。好，这里我们看了一下对于什么共享存储、共享磁盘的解决方案，如何把它的结构化、非结构化数据进行剥离，或者剥离到后台的存储，或者甚至于剥离到前端的网络缓存来实现有状态向无状态的转移，那第二个场景就难很多了。实际上 nothing 没有一个最优解，

[image](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/f5c74447-5d69-4573-bb77-82463e403fd3/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UDB6ZLEC%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T230446Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIETNSZvTU3iq5qfciqAESzJDE2IevFTtHr%2BpP5V5mNQHAiEAtrsXoFV%2FBmM3SjaTanj6FjTCRokHZW3ldbgT7%2FiUmYIqiAQIxv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDP4H%2Fu%2FhDWlDZpt0PircA5y%2BXIGtWj4z9Xrv2DK3h6qtozgoMhD%2FHJMqBc0NOMRONiUFmqTX8zC6ik9P6DDbJSOxyEDMs5vFPNM53fBUj%2FHbOZeWU8HqNNxP52GsL6fbMefaN3JR4RzIppvrVHVFy80hEGMltmxkVNgmOSoGN10i4n0Jntb1rNng6v2aV49BNRFejq8WPLUNUZ%2FLG5fngWwj111e30rKhynSQEFmnpIBjGta7OQsJaCI7lKm8%2B370KGDx%2B%2FDcqTljzkRsBTCO8geOeqd735grgD34J89uVTtRy36XPWbO1yLzpm9Wk1U9ajvp3k2pr6Y3jrMcDPZbbZ5IJLtUtCgOn02eTuhQYQQMfyZqmVNiO%2F97Y1Puc9WQv%2FFsbraB2%2BnXMMe0wRuec3dBp%2FHnXBBm1T61%2FILSIQj3Thwl7n4%2BfRChn%2Fg15tHQrv8KUk13ty%2FJb4vxcj%2B8ipJd7YR99txWHk4NTapE6Jmd7LlhgzLZ9A1AF6ofN4V10cu8mo1QxgGxONuFiiBDCi5vkZicFyNJPq%2FECv6%2F6uIZtYrxxOuXVlknpj2et6mrpXG8uKGrFo1%2BBtkAs2Sejo2rvrBdIwSuG3JjnD88hWSSdQhO0%2Bpnh8TiwvS07hxIsVhwW3cZpV6w28iMPC3%2F9IGOqUBq6rEWy%2BudV6%2FT5%2FOfXW7SKLwsQjdKcsLuilAvQFNcT11DABJhECBHJNJ5X8wWluoiU%2F4%2F02k3d0YoFlRRK6JTdgK38HdWog41wc596sHFsb2eYaXgk5o3CXdhnovXjXYq5NeUaa0qxHnp9llMemyHbOmLInsfLH7TCB%2Bh6V%2BuYy1RKsSaMwB0h5ryhI0AAyc2lYD7eLH9S2acXZz3qkiSZgxJ6OB&X-Amz-Signature=590d880a691bb29102136e74799b7b8386952f27744f56cbbcb1bdbf2334f2dc&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

我们只能做一些牺牲和妥协。通常我们会用 cap 理论来实现。既然什么我们的伸缩性，就必然需要增加我们的分区数，所以分区性能这个 p 肯定是我们要优化的一个重点。那除此以外，可用性通常都是我们的一个目标之一，所以唯一能牺牲的就是什么。


我们把强一致性弱化成最终一致性。我们以 Kafka 集群为例，当我们是强一支少节点的 Kafka 集群的时候，有可能你要求每一个 Kafka 的 broker 都完成数据的接收，同时这个 BROKER 要把数据落到硬盘上才完成了 Kafka 消息的。


从什么我们的 producer 生产端到 Kafka BROKER 处理器端的这个完整的链路过程。如果是要增强伸缩性，我们就要做一些妥协，这妥协一点，一旦 Kafka 的这个 broker 就是处理器接收到内容到缓存，就算完成，不需要写到硬盘，这个时候已经回给我们的生产者 producer 说什么我完成了你的内容的接收。那同样道理，不是每一个 broker 都需要完成它的接收。虽然有可能你的 Kafka 集群里面写的什么 replica 是 2 或者3，但是只要任何一个节点完成了你的这个 topic 的接收，它就回给你说我已经接收完成了。


看上去很激进，但确实能很好的提高它的分区的扩展性以及它的可用性。好，这是 cap 理论里面，对于有状态的应用，我们可以尽量去牺牲它的一致性来完成比较强的伸缩性。那除此以外，对于很多的集群，我们可以通过集群的选举和仲裁的优化，使得我们在出现脑裂的时候，出现某些节点故障的时候，仍然能够对外提供一个很好的很快捷的应用响应。同时通过这样的一种比较简单的仲裁快速的选取机制实现我从 5 个节点到 50 个节点到 500 个节点，集群是从小集群到中集群到大集群的很好的弹性伸缩能力。


那除此以外，想二阶段提交，像多副本管理，这里面其实都有一些技巧，甚至于分片，当你的分片采用不合理的方式，比如是说传统哈希就是一个不合理的方式。一旦传统哈希，你的原来的节点是 10 个，一旦增加到 11 个的时候，会形成一个什么分片调整的风暴？这个风暴会明显的影响你的整个集群，而我们伸缩式的环境当中，集群的节点的数量 10 个到 15 个到 20 个经常会变，这个时候你每一次集群调整都会产生风暴，都会有大量的数据的 rebalance 重调整将会导致整个集群近乎瘫痪，没法进行正常操作，所以我们通常会采用一致性哈希。虽然每个节点上它的什么分片或者副本的压力不均衡，但是增加节点或减少节点并不会导致一些选取的风暴，也不会导致一些 rebalance 重分布的风暴，那这样的情况下才更适合于弹性的伸缩。


好，聊完了这两个思路以后，还有一个思路也是实验 nothing 里面经常采用的，那就是资源预配置，比如还是以秒杀系统为例，我们在 0 时零分零秒进行秒杀，为什么我们不提前半小时进行 share nothing 架构的预配置？要理解无状态应用，我们可以很快的在几秒之内实现什么快速的弹性伸缩，但是有状态应用，不管是它的选举仲裁还是它分片副本的重新的分配，都会花费几十分钟甚至于几小时的时间。


所以这也给我们一个警示，我们应该在秒杀抢购平台触发之前的几十分钟或者几小时左右的时间，提前对 CN nothing 的架构进行预配置，快速的去增加节点，让它完成在增加节点过程当中，所有的集群变动，风暴变动导致了各种各样的问题，把误这些问题解决在秒杀或者抢购发生之前，这才是一个合理的解决方案。


好，我们这里已经聊完了有状态应用的两个场景，一个是什么共享磁盘，一个是 share NASI，什么都不共享，这样两个架构以及它不同的实现方法。下一节就是我们的思维导图和一个小作业，在思维导图之后的下节就是令大家比较心动的面试回答环节，大家敬请期待。


