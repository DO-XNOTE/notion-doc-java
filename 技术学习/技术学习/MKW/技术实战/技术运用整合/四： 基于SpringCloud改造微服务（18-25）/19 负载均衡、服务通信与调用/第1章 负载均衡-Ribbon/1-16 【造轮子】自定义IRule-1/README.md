---
title: 1-16 【造轮子】自定义IRule-1
---

# 1-16 【造轮子】自定义IRule-1

[image](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/641b34d9-57cd-42ce-a96d-9c4a379d0be4/SCR-20240820-pqkq.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666VJGGGK7%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T225615Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCXmJ7Y2%2BRxjBuhZifo4B8Z9Psk1IuWLrTtg10HLQdqxQIgLen%2FbqAOavy1iXOGtBmbhpmhPeY%2B0HZdYPE2Gnpx%2BREqiAQIxv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDJCrvjrgSiJgQ%2BTwQCrcA41jWTdB1JtUcftXBcQD%2BQJUfQPjdCiUZY6VKAWMnWMJDxV2RsV1yIZyatcsT%2B1rlXh2ekd5wzcaiP%2FFBg2yQXfOg5wkAxiEr97Mi3D93Voynd%2BpJvJErbvQjxAFuZZv%2FIJ0XrUKUw9UIDPfU68DYP3WA2L5%2BsZuvku14agi%2FU%2BaWifpiLvAl5eXc5%2BzNDX1quf2ukPWKzZHjuRrZo5PMMMEcAFep7t2TldKr4u3fONghrkAm7cY0DbOHOcF3Ug5bkIV5E3cad3TDfd3THC1l2%2Fj7RjNO7g%2BVKc0hxgid4RugiTguXcc6XrMAfYv27hwIxYjcYFMTumSxKkMaNslpMfxrf6Xyvs%2B1Iao5hT0iPPcObZQB%2Bb7ucxBqUZi6wsqunnOMWxk4%2F%2F0x9vkA30raRUkIC9roASHeJjo7GVUcGuRi%2FWapv1Le%2FftPCY9f3Tjwbt%2B0yn6x7V9UpGGSia9P9ME6yBZpXSZLaSU3Mpj0nPEmQCNT0hh6lhgISHr3NVsvTfiNHsq0odb%2Fq%2F2mfJjF1%2BhOdP1oH1faZ8eUyB88FF0A14N5ORc0l9VdsFRR8O0I8iW9MWbaJB%2FFIPlQ2UGen%2FwjpCDxkvUwXfZ%2BAHz4BU81Kxa6dA0LZ8t3tzpMMS6%2F9IGOqUBiTFy0zGizgvxeprslbVx%2Bbg5IfGAtGHFPnRydbAdfLuk9zImrIk84aOLObsc%2FlZoEM%2F9GtaFDhtGnu9YonwVtT08v1ljMRgv3AA5m9Da%2FFkSf%2FbPKjF91k1bOkR%2BP%2BSE0j%2FWd0m82TOVkuWCCfVc6%2FVTUtpMrlfRgFz39S83G%2BC%2BzmYwPbsnyzsuFUptsojGdtJ7osEMCqf3OI0AqCMe0fNM3PBR&X-Amz-Signature=e895b6e2e2f0e9c3cd7ead1f12e6eb5fcf28ae3b32de9ffeee131f92155e26e1&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

[image](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/842acd85-cc5f-453f-99ed-64c33c8e34c7/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666VJGGGK7%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T225615Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCXmJ7Y2%2BRxjBuhZifo4B8Z9Psk1IuWLrTtg10HLQdqxQIgLen%2FbqAOavy1iXOGtBmbhpmhPeY%2B0HZdYPE2Gnpx%2BREqiAQIxv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDJCrvjrgSiJgQ%2BTwQCrcA41jWTdB1JtUcftXBcQD%2BQJUfQPjdCiUZY6VKAWMnWMJDxV2RsV1yIZyatcsT%2B1rlXh2ekd5wzcaiP%2FFBg2yQXfOg5wkAxiEr97Mi3D93Voynd%2BpJvJErbvQjxAFuZZv%2FIJ0XrUKUw9UIDPfU68DYP3WA2L5%2BsZuvku14agi%2FU%2BaWifpiLvAl5eXc5%2BzNDX1quf2ukPWKzZHjuRrZo5PMMMEcAFep7t2TldKr4u3fONghrkAm7cY0DbOHOcF3Ug5bkIV5E3cad3TDfd3THC1l2%2Fj7RjNO7g%2BVKc0hxgid4RugiTguXcc6XrMAfYv27hwIxYjcYFMTumSxKkMaNslpMfxrf6Xyvs%2B1Iao5hT0iPPcObZQB%2Bb7ucxBqUZi6wsqunnOMWxk4%2F%2F0x9vkA30raRUkIC9roASHeJjo7GVUcGuRi%2FWapv1Le%2FftPCY9f3Tjwbt%2B0yn6x7V9UpGGSia9P9ME6yBZpXSZLaSU3Mpj0nPEmQCNT0hh6lhgISHr3NVsvTfiNHsq0odb%2Fq%2F2mfJjF1%2BhOdP1oH1faZ8eUyB88FF0A14N5ORc0l9VdsFRR8O0I8iW9MWbaJB%2FFIPlQ2UGen%2FwjpCDxkvUwXfZ%2BAHz4BU81Kxa6dA0LZ8t3tzpMMS6%2F9IGOqUBiTFy0zGizgvxeprslbVx%2Bbg5IfGAtGHFPnRydbAdfLuk9zImrIk84aOLObsc%2FlZoEM%2F9GtaFDhtGnu9YonwVtT08v1ljMRgv3AA5m9Da%2FFkSf%2FbPKjF91k1bOkR%2BP%2BSE0j%2FWd0m82TOVkuWCCfVc6%2FVTUtpMrlfRgFz39S83G%2BC%2BzmYwPbsnyzsuFUptsojGdtJ7osEMCqf3OI0AqCMe0fNM3PBR&X-Amz-Signature=dcbc305837ca9e11699fa3074a85971f26ced0f6cc324b68b5d935c666fd9f46&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

[image](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/e6862281-f0b1-4b13-bf26-39f6ab34f974/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666VJGGGK7%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T225615Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCXmJ7Y2%2BRxjBuhZifo4B8Z9Psk1IuWLrTtg10HLQdqxQIgLen%2FbqAOavy1iXOGtBmbhpmhPeY%2B0HZdYPE2Gnpx%2BREqiAQIxv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDJCrvjrgSiJgQ%2BTwQCrcA41jWTdB1JtUcftXBcQD%2BQJUfQPjdCiUZY6VKAWMnWMJDxV2RsV1yIZyatcsT%2B1rlXh2ekd5wzcaiP%2FFBg2yQXfOg5wkAxiEr97Mi3D93Voynd%2BpJvJErbvQjxAFuZZv%2FIJ0XrUKUw9UIDPfU68DYP3WA2L5%2BsZuvku14agi%2FU%2BaWifpiLvAl5eXc5%2BzNDX1quf2ukPWKzZHjuRrZo5PMMMEcAFep7t2TldKr4u3fONghrkAm7cY0DbOHOcF3Ug5bkIV5E3cad3TDfd3THC1l2%2Fj7RjNO7g%2BVKc0hxgid4RugiTguXcc6XrMAfYv27hwIxYjcYFMTumSxKkMaNslpMfxrf6Xyvs%2B1Iao5hT0iPPcObZQB%2Bb7ucxBqUZi6wsqunnOMWxk4%2F%2F0x9vkA30raRUkIC9roASHeJjo7GVUcGuRi%2FWapv1Le%2FftPCY9f3Tjwbt%2B0yn6x7V9UpGGSia9P9ME6yBZpXSZLaSU3Mpj0nPEmQCNT0hh6lhgISHr3NVsvTfiNHsq0odb%2Fq%2F2mfJjF1%2BhOdP1oH1faZ8eUyB88FF0A14N5ORc0l9VdsFRR8O0I8iW9MWbaJB%2FFIPlQ2UGen%2FwjpCDxkvUwXfZ%2BAHz4BU81Kxa6dA0LZ8t3tzpMMS6%2F9IGOqUBiTFy0zGizgvxeprslbVx%2Bbg5IfGAtGHFPnRydbAdfLuk9zImrIk84aOLObsc%2FlZoEM%2F9GtaFDhtGnu9YonwVtT08v1ljMRgv3AA5m9Da%2FFkSf%2FbPKjF91k1bOkR%2BP%2BSE0j%2FWd0m82TOVkuWCCfVc6%2FVTUtpMrlfRgFz39S83G%2BC%2BzmYwPbsnyzsuFUptsojGdtJ7osEMCqf3OI0AqCMe0fNM3PBR&X-Amz-Signature=b3ca9a26228ca66db1d0eba598ffbbe71b138e4a7d6de6c0606ff320d4e8a3e0&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

hello 慕课网的各位同学们，大家好，又跟大家见面了，这一节是我们动手造轮子的环节，历史的车轮再向前翻滚。我们这次造一个什么轮子呢？前面大家已经学习了 error 的机制，对不对？我们看了源代码，那这里就仿造 error 的机制，自己创建一个 error 但是我们想 ribbon 已经给我们提供了这么丰富的负载均衡组件库，我们造个什么 eiro 好，这个轮子不仅要弥补 ribbon 中的空白，还要怎么样，还要跟我们未来的工作有那么一点关系，甚至说跟面试中可能问到的问题都有点关系。

[image](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/54181e73-e25d-4f40-a99b-bc1c11042113/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666VJGGGK7%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T225615Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCXmJ7Y2%2BRxjBuhZifo4B8Z9Psk1IuWLrTtg10HLQdqxQIgLen%2FbqAOavy1iXOGtBmbhpmhPeY%2B0HZdYPE2Gnpx%2BREqiAQIxv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDJCrvjrgSiJgQ%2BTwQCrcA41jWTdB1JtUcftXBcQD%2BQJUfQPjdCiUZY6VKAWMnWMJDxV2RsV1yIZyatcsT%2B1rlXh2ekd5wzcaiP%2FFBg2yQXfOg5wkAxiEr97Mi3D93Voynd%2BpJvJErbvQjxAFuZZv%2FIJ0XrUKUw9UIDPfU68DYP3WA2L5%2BsZuvku14agi%2FU%2BaWifpiLvAl5eXc5%2BzNDX1quf2ukPWKzZHjuRrZo5PMMMEcAFep7t2TldKr4u3fONghrkAm7cY0DbOHOcF3Ug5bkIV5E3cad3TDfd3THC1l2%2Fj7RjNO7g%2BVKc0hxgid4RugiTguXcc6XrMAfYv27hwIxYjcYFMTumSxKkMaNslpMfxrf6Xyvs%2B1Iao5hT0iPPcObZQB%2Bb7ucxBqUZi6wsqunnOMWxk4%2F%2F0x9vkA30raRUkIC9roASHeJjo7GVUcGuRi%2FWapv1Le%2FftPCY9f3Tjwbt%2B0yn6x7V9UpGGSia9P9ME6yBZpXSZLaSU3Mpj0nPEmQCNT0hh6lhgISHr3NVsvTfiNHsq0odb%2Fq%2F2mfJjF1%2BhOdP1oH1faZ8eUyB88FF0A14N5ORc0l9VdsFRR8O0I8iW9MWbaJB%2FFIPlQ2UGen%2FwjpCDxkvUwXfZ%2BAHz4BU81Kxa6dA0LZ8t3tzpMMS6%2F9IGOqUBiTFy0zGizgvxeprslbVx%2Bbg5IfGAtGHFPnRydbAdfLuk9zImrIk84aOLObsc%2FlZoEM%2F9GtaFDhtGnu9YonwVtT08v1ljMRgv3AA5m9Da%2FFkSf%2FbPKjF91k1bOkR%2BP%2BSE0j%2FWd0m82TOVkuWCCfVc6%2FVTUtpMrlfRgFz39S83G%2BC%2BzmYwPbsnyzsuFUptsojGdtJ7osEMCqf3OI0AqCMe0fNM3PBR&X-Amz-Signature=98401eb60b873b3ce1a3de588471815b5b178c78570d9cc55f0be31c80e7e27c&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

当然这个问题是我比较喜欢问的，这是个什么轮子自定义一个基于一致性哈希的负载军方策略。所谓一致性哈希听上去有点蒙圈，但是实际上是一个非常简单的概念。我在接下来的其他章节将跟大家深入探讨一致性 IC 究竟是什么含义。那在这里我就点到即止，跟大家稍微提一提就可以了。我们主要关注什么呢？主要关注它是怎么来实现的。 OK 定义完这个一致性希，我们就把这个哈希策略应用到负载均衡指定的服务中，让这个服务的所有请求都通过我们自定义的这个 error 进行负载均衡。那大家二话不说抄起家伙开工。在开始以前，我先跟大家唠叨唠叨什么是一致性希。

[image](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/55b3bb0e-1dc2-440d-99a9-af517fac5c7a/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666VJGGGK7%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T225615Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCXmJ7Y2%2BRxjBuhZifo4B8Z9Psk1IuWLrTtg10HLQdqxQIgLen%2FbqAOavy1iXOGtBmbhpmhPeY%2B0HZdYPE2Gnpx%2BREqiAQIxv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDJCrvjrgSiJgQ%2BTwQCrcA41jWTdB1JtUcftXBcQD%2BQJUfQPjdCiUZY6VKAWMnWMJDxV2RsV1yIZyatcsT%2B1rlXh2ekd5wzcaiP%2FFBg2yQXfOg5wkAxiEr97Mi3D93Voynd%2BpJvJErbvQjxAFuZZv%2FIJ0XrUKUw9UIDPfU68DYP3WA2L5%2BsZuvku14agi%2FU%2BaWifpiLvAl5eXc5%2BzNDX1quf2ukPWKzZHjuRrZo5PMMMEcAFep7t2TldKr4u3fONghrkAm7cY0DbOHOcF3Ug5bkIV5E3cad3TDfd3THC1l2%2Fj7RjNO7g%2BVKc0hxgid4RugiTguXcc6XrMAfYv27hwIxYjcYFMTumSxKkMaNslpMfxrf6Xyvs%2B1Iao5hT0iPPcObZQB%2Bb7ucxBqUZi6wsqunnOMWxk4%2F%2F0x9vkA30raRUkIC9roASHeJjo7GVUcGuRi%2FWapv1Le%2FftPCY9f3Tjwbt%2B0yn6x7V9UpGGSia9P9ME6yBZpXSZLaSU3Mpj0nPEmQCNT0hh6lhgISHr3NVsvTfiNHsq0odb%2Fq%2F2mfJjF1%2BhOdP1oH1faZ8eUyB88FF0A14N5ORc0l9VdsFRR8O0I8iW9MWbaJB%2FFIPlQ2UGen%2FwjpCDxkvUwXfZ%2BAHz4BU81Kxa6dA0LZ8t3tzpMMS6%2F9IGOqUBiTFy0zGizgvxeprslbVx%2Bbg5IfGAtGHFPnRydbAdfLuk9zImrIk84aOLObsc%2FlZoEM%2F9GtaFDhtGnu9YonwVtT08v1ljMRgv3AA5m9Da%2FFkSf%2FbPKjF91k1bOkR%2BP%2BSE0j%2FWd0m82TOVkuWCCfVc6%2FVTUtpMrlfRgFz39S83G%2BC%2BzmYwPbsnyzsuFUptsojGdtJ7osEMCqf3OI0AqCMe0fNM3PBR&X-Amz-Signature=a2b907b11ab26602147f46a5ed3d3a3539eb078c860d30d499de860fd1ff8281&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

那这部分更详细的内容我将安排在后续的 double 章节中跟大家介绍，所以这里只是蜻蜓点水点倒计时，跟大家介绍一致性希最简单的应用场景，看一看它是在负载均衡策略中怎么来起作用的。
OK 那我这里标了五颜六色的四台服务器server1234，对不对？它们均匀地分布在一个环上，也就是这个蓝色的圆圈。那么来访的请求怎么找到对应的服务器呢？这里就是一致性哈希的精华所在了。我们把来访的请求中的某一个特征量给它找出来。这个特征量是什么含义呢？你可以是来访请求中的一个 request 的 parameter 也可以是 body 中的一个字段，或者是你 query string 的一部分，也可以是什么呢？也可以是你整个的 URL 总之八仙过海，各显神通。



你告诉我这个 request 中的一个特征量，我通过一定的算法把它做成一个摘要。那大家一提到摘要可能最熟悉的就是什么？ M d5 对不对？一个魔武摘要类似的形式。那我把它做成摘要以后，再把这个摘要通过 hash code 算法滤一遍，它就变成了一个 int 值。对不对？那这个 int 值我把它放在哪里呢？我把它映射到这个环上，接下来它就需要寻找离它最近的下一个节点的位置。



所谓下一个是什么意思呢？也就是说它寻找服务节点的方式只能是顺时针或者是逆时针，你只能选择一种方向。你比方说，我们看绿色的线最上面的这个绿色的点，离它最近的是不是 server one 也就是这个黄色节点。但是它并不会去寻找 server one 而是按照顺时针的方向向前寻找 server two 所以说当你的这个 request 请求它通过摘要落到这个环上以后，它一定只会寻找固定方向中离它最近的这台服务器。反过来，这说明了什么？这说明了这样一个问题，与同一个 request 它的特征量是相同的对不对？那么它每次获得的摘要也是相同的。那假如我的服务不下线，服务器不宕机，那它永远只能找到同一台服务器。为什么？因为它通过摘要算出来的 int 值映射到这条环上的位置永远是同一点。
对不对？那假设这台服务器宕机了怎么办呢？比方说 server 3，本来这些桃红色的线呢应该访问 


server 3，但是 server 3 不存在了宕机了，那么它将会访问到哪里呢？它会继续向前寻找下一个离它最近的节点，也就是 server 4 对不对？ OK 这就是一致性哈希的简单算法，通过一个摘要把这个请求定位到一个圆环上。接下来他只要去通过顺时针或者逆时针沿着一个方向寻找下一个他能找到的节点就 OK 了。


那一致性希不仅在负载均衡领域，在其他很多领域都有广泛的使用，这也是我面试中非常喜欢问的一个问题，大家课后可以去自己查阅一些一致性哈希的使用用例，去深入地理解一下这个算法背后的含义。 OK 我们了解了一次性哈希以后，接下来就可以去撸代码了，每天扣订 1 小时，健康工作 50 年。好，开始撸代码。那这里同学们找到 ribbon 这个项目。 Ribbon consumer. 我们在相应的 Java 目录下面，在 com.imock.spring cloud 这个文件夹下新建一个文件叫 rules 大家听清这个是 rules 不是 rose 不是泰坦尼克号那个 Jack rose 的rose。
Oh， jack you jump i jump.


这个叫 rule rules 专门存放我们将要新建的负载均衡策略。好，接下来在这里直接 new 一个 Java 方法，给它起名叫什么呢？一致性哈希。这个单词还蛮难拼的，不拼了我们就叫 my role 好了。 My role ok. 回车。好，接下来我要把这个类做什么手脚呢？它是不是要继承自一个 ira 呢？没错，我把它小说版先收起来，正儿八经写代码资质要正确。好，我们这里先给它继承自 ribbon 的一个官方出品的 abstract load balance ruleabstract load balance a row okay 寄生完之后再怎么样再 implements iro 好，这里就声明完了，那大家看这里冒了红线，说明有一些方法没有实现对不对两个方法。好，那我们把它实现好了。


下面一个方法，暂且不管，我们主要看下面的一个方法，按照刚才已知性哈希的第一步要拿到这个请求的什么？一个做摘要的 key 对不对？那你看这个 choose 这里天然传入了一个 key 这是什么东西啊？它能不能做摘要啊？

[image](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/0be9abbc-ebb1-4fde-bbef-7a7633cfa25c/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666VJGGGK7%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T225615Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCXmJ7Y2%2BRxjBuhZifo4B8Z9Psk1IuWLrTtg10HLQdqxQIgLen%2FbqAOavy1iXOGtBmbhpmhPeY%2B0HZdYPE2Gnpx%2BREqiAQIxv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDJCrvjrgSiJgQ%2BTwQCrcA41jWTdB1JtUcftXBcQD%2BQJUfQPjdCiUZY6VKAWMnWMJDxV2RsV1yIZyatcsT%2B1rlXh2ekd5wzcaiP%2FFBg2yQXfOg5wkAxiEr97Mi3D93Voynd%2BpJvJErbvQjxAFuZZv%2FIJ0XrUKUw9UIDPfU68DYP3WA2L5%2BsZuvku14agi%2FU%2BaWifpiLvAl5eXc5%2BzNDX1quf2ukPWKzZHjuRrZo5PMMMEcAFep7t2TldKr4u3fONghrkAm7cY0DbOHOcF3Ug5bkIV5E3cad3TDfd3THC1l2%2Fj7RjNO7g%2BVKc0hxgid4RugiTguXcc6XrMAfYv27hwIxYjcYFMTumSxKkMaNslpMfxrf6Xyvs%2B1Iao5hT0iPPcObZQB%2Bb7ucxBqUZi6wsqunnOMWxk4%2F%2F0x9vkA30raRUkIC9roASHeJjo7GVUcGuRi%2FWapv1Le%2FftPCY9f3Tjwbt%2B0yn6x7V9UpGGSia9P9ME6yBZpXSZLaSU3Mpj0nPEmQCNT0hh6lhgISHr3NVsvTfiNHsq0odb%2Fq%2F2mfJjF1%2BhOdP1oH1faZ8eUyB88FF0A14N5ORc0l9VdsFRR8O0I8iW9MWbaJB%2FFIPlQ2UGen%2FwjpCDxkvUwXfZ%2BAHz4BU81Kxa6dA0LZ8t3tzpMMS6%2F9IGOqUBiTFy0zGizgvxeprslbVx%2Bbg5IfGAtGHFPnRydbAdfLuk9zImrIk84aOLObsc%2FlZoEM%2F9GtaFDhtGnu9YonwVtT08v1ljMRgv3AA5m9Da%2FFkSf%2FbPKjF91k1bOkR%2BP%2BSE0j%2FWd0m82TOVkuWCCfVc6%2FVTUtpMrlfRgFz39S83G%2BC%2BzmYwPbsnyzsuFUptsojGdtJ7osEMCqf3OI0AqCMe0fNM3PBR&X-Amz-Signature=afb93072c44306a22cf618c1a68d5f05c55797187c55484268905c5e86496b01&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

完全不能。大家如果 debug 过来会发现这个 key 的值是什么？ key 的值就叫 default 它是一个默认的值，它的含义并不是跟你 HTTP request 有那么半毛钱关系，一点关系都没有。所以我们这里要先获取到 HTTP server let request 这个类 serverlet requestokay 我们看这一个 request 如何获取，什么入参都没有，所以我们就要采取什么样的方法，旱地拔葱的方法怎么来拔？我们来看这个葱怎么来拔这里使用官方出品的 request context holder 我们知道 HTTP request 肯定是存在在上下文当中的，对不对那我把这个 context 拿到就好嘞。


request context coder 它能做什么事呢？ get request attributes 大家看到这里，我 get attributes 和 request 有什么关系呢？它下面的方法好像也没有 get 什么 request 只有一个 get session ID 稍安勿躁，这里给它变一个魔术，我们把它加一个括号，给它做一个类型的强转。


强转成谁呢？强转成 serverlet request attribute 转成这个类以后，我们再来看这手脚就动得了点 get request 对不对？这就是通过一种旱地拔葱的方式，我们把这个 request 从上下文中给它拿到了。 OK 那葱拔出来了以后，这个 request 我们用什么方式来做摘要呢？我这里使用一个简单一点的方式，我们用 URI 来做摘要。那 URI 是什么东西呢？我们就往后看 request.get server let pass 大家看明白了吗？我是把它的路径获取到。这路径是什么？它可不是 HT DP 123456 点端口，这个路径它是在你主域路径以后的那些路径，也就是 query string 比方说 3w 点百度，你后面一个斜杠在后面跟的这些路径才是我们这里 request 获取到的。


Server let path. 然后还没完，还没完，我光获取到了 pass 还不对，我还需要获取到一个什么呢？一个 query string request.get query string 好嘞，这是一个相对简单的方式，同学们在自己的项目中一定要活学活用。


打个比方，有些访问请求是跟一个用户绑定的，对不对？你永远要绑定一个用户的 user ID 比如说添加购物车下单，这些请求都跟一个用户 ID 访问。而像在淘系链路中，你一个用户他如果是中心节点的用户，那他后续的所有请求都只会落在中心节点。他如果是单元用户，那他所有请求都会落在单元机房。所以他们的负载均衡策略，跟你的这个用户 ID 是强绑定的。


那这里如果让我们来应用这种策略会怎么样呢？要从你 request 中把这个用户的 ID 拿到对不对？作为它的 URI 那我这里只是简化了一种方式，只根据它的 URL 来做摘要。 OK 完了以后把这个 return none 先放着，我们先抛下它，不管接下来做一些其他的逻辑，其他逻辑是什么呢？这里就是我们的主逻辑啦。 public server 我要找 server 对不对？这是我最终需要返回的对象。那我这里给他新写一个 root 方法，他接受什么呢？他接受一个 hash ID 并且他还要传入一个 list 的 server 我们把它管叫 address list 好把这个 list 引入进来。 OK 那我这里先 return 一个，那让它编译，不要老报错了，看着神烦。好在上一步方法中，我们这个遗留的 none 现在我就要对它动一动手脚了，它不再是一个空，而是一个什么呢？我们的 UI 看到吗？我给他做一个 hash code。


那大家很多人不知道 hash code 返回的是什么，是个 int 如果你作为一个 5 年、六年甚至是七八年工作经验的程序员，你说不出这个 hashcode 具体在你项目中怎么用的，在你这个七八年职业生涯中也没改写过 hashcode 这个可不太合格。同学们。 OK 那我这里传入了 hashcode 以后，这个 


hashcode 的值就是将来需要映射到圆盘中某个节点的位置。 OK 那接下来我需要再传入这个 server list 对不对？那就很简单了。那我添加到 load balancer 中的 server list 我把它给拿出来好不好？ get all servers 我不 get reachable servers 我为了简化我 get all servers。Ok.那接下来这个核心逻辑就在哪了？就在 root 里面了，是不是我们来看这个 root 来怎么写。


第一步，我们这里声明一个 tree map 吹麦克，大家应该都相当熟悉，我这里就不多对它的底层的实现或者是机制来进行讲解了。我们这里声明一个 tree map 那它获取一个 address 先把它引用进来，这里把它 new 出来。


New tree map ok.
拿到 tree map 以后，我们接下来要怎么做呢？我们要循环这个 server list 对不对？我们把它循环掉 address list 怎么循环呢？直接用 stream 的方式，这里建议大家怎么样，再做一个防御性编程。如果它的 address 是空，那就返回空对不对？如果 collection utils 大家不要去傻不拉叽的直接去判断它是否为空，是不是等于 none 再判断一下它的 size 那直接用一些工具类来判断是会非常方便的，而且也相对来说比较美观。


如果是个空的 list 那就返回一个 null 如果不为空，我们再走 tree list stream 接下来是什么呢？ for each 我要挨个循环，它对不对？循环的时候怎么样呢？我假设这个圆环中有几个节点，我们想一个幸运数字，同学们的幸运数字是多少？我就给他说是八个。好了，我们中国人都喜欢八对不对？我给他记 8 个，一加 8 个。


八个完了以后我们需要拿到一个 hash 那这个 hash 是什么呢？我们先来这里写一个空的 hash 函数，这个 hash 函数它就是专门用来计算 hash 值的 public 这个 hash 它的入参是什么？入参是一个 string 然后返回的是一个 launch 入参 string key OK 然后返回一个，那我们这里给它加一个空实现了，先把这个算法的骨架给它搭配起来，然后再慢慢地填逻辑。当你这个骨架起来了以后，你这个逻辑就是顺理成章的事情了。


OK 我这里取一个亥时值，把这个 key 传入进去。 key 是什么呢？ key 我这里用什么？好呢？我要用一个 unique 的 key 对不对？那对于每一个 E 来说，这个 E 是什么？这个 E 是每一个 address list 中的 server elementok 它有哪个 unique ID 呢？我们看 get ID 看到吗？我们也可以通过 host 加 host POD 这样拼，但是如果直接用 ID 会相对方便一些。 OK 那我们这里再给它加入一些变数。变数是什么呢？是当前这个 I 那同学们知道这一步是来做什么的吗？算出了哈希以后，接下来要怎么样啊？要把这个哈希值加到 dress 里面对不对？我们通过 put 方法把这个 hash 作为 key 然后把这个 E 作为 value 这个 E 是什么？就是它的 server 对不对？好？那我这里做了一件什么事儿？我这里对每一个 server 都循环了 8 次，加入了 8 个节点，这相当于什么？相当于一个虚化对不对？这里的虚化是指我把每一个服务器通过 for 循环，算出 8 个不同的 hash 值，分散到这个圆环当中。那大家可以想到这个并不是很均匀的分布，同学们后面可以对这个算法进行改进，把它改成一个类似均匀分布的算法。我们这里只是为了配合一致性哈希的算法思想，做一个简单的例子。


Ok.那么这个 address 这个 tree map 实际上是什么含义呢？大家看它是 tree map 是一个排序的类型对不对？那它排序我们就可以按照 tree map 中的某些特殊的函数，谁，比方说 tail map 这个函数很有用啦，我通过 tail map 就可以找到一个对应哈希集离它最近的那一个 key 所对应的 server 是什么？Ok.所以说这个 address 就相当于一个目录结构，或者我们可以叫它花名册，根据你来访请求的是值，我可以找到离这个哈希值最近的这个 key 当然了，你从 tail map 中获取到的这个 key 虽然是最近的，但是它也是要比当前传入的这个 key 要大。也就是说你如果传入了一个3，那你这个 map 中既有 4 又有，那 4 和 2 到 3 都一样近。你传回哪个当然是传回 4 了，所以它会获得第一个比这个三大，而且离它最近的那么一个点。


找到这个 K 以后我顺理成章的就能拿到 server 也就是说我知道这个 request 该访问哪台 server 了。好，我们这一节暂时先讲到这里。上半场到此结束，大家起身喝杯咖啡，吃点小点心，做个中场休息。我们接下来看下半场。



