---
title: 2-10 面试指导-1
---

# 2-10 面试指导-1

前面我们刚刚说到学以致用，那么面试自然是一个不可回避的环节。就分层架构来说，有很多种面试的方法，因为它本身这种分层架构已经相当普及，其背后的很多理论都是思想，也是被很多精简软件采用。所以我们要像分成架构一样来设计我们的面试题目，从具体的技术问题到相对抽象的开放式设计题目。在具体技术问题时，我们假设都是针对 Java 生态的提问，因为这样子可以缩小于我们的范围，否则这个回答起来实在是太困难了。


好吧，那我们下面来看看我们的第一道题，讲解一下 HTCP 和底层 TCP IP 的连接的关系。

[image](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/20853ad0-ba09-473a-923c-3615d59aed3c/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TA4ZODC5%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T230546Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQD%2FpBmjed6PVsNDqZ8xyuwN3GlAym0jTr%2BK5rVuRhSJiwIhAMjH5IPh78GPjAFYDGedgWlW8tMR9P%2Fw%2BoknnOC2%2BbjOKogECMb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgwhZD3NtsNhU7bydG8q3ANj9R4ZIlp0c%2BTvJEsELh%2BGdMAirWt60DbW%2B8NBYZLWpdGoZoRzNiSO9%2BXlC0rRneDXVChuqpTs7HumGbBAyKdorfIkNS9hrVlEB%2BvxbjQLKhN8qUqJxlwPCK2fyPlX2Yl2Lg3H2rgnvYCe6tOTBzv95YTZyRr%2Bz7nmN2K7onNb7PkoP481i43l6mN6ZshTJxJse%2FfLMTbA42Z24Ord5p4gaM%2F6lOiV9qw37Jy1txX1OpaY0%2FAeMHwl4BuN2Nh2NS%2Biu34mQGPPF6TCmLE%2FJXjlNR%2BfthiF4fsvwb2AYWc5GkmmAelBPfLopchBPOvRIi%2FmA5ZgcvsvJD7dbLFgFVHJSZg1W1LG%2B323BTvx9vZSSbStkKBT36mZTQXVd040zppu2PFc4Jo1sUAak%2BIi7JQuOHYlhoH2GQK35upeJEV6Ks2OYjdxL7LHaHJ9%2B1s8Ic%2FVMfge1dl68bCeU%2F9oTawnt98JmfzHCrbYYY6SOdZtU2Vl1%2FTyU8mtaVUTopcJmOs4sG9rqLegSNvewZS7nZKjfv3y6XMqONMkUcopTQCkca%2F6CrXZmAEj3mkVnUZw4gLk%2BmW09wuVanDzob23FWFPqhpyxm1uZ6NTkMb%2BSmVquCffhIFD%2B6ZJRaIF%2FjDauv%2FSBjqkAd7H6uFpcMN%2Bgadv2nyOWViW7PWFO51Ngx4Bju07LLopVY%2BMQWXiPn%2B88qOh1RMKjXCg1REALuXEhwieqeyy8fzn0Igmev3ekHWWHY1%2BzTxQAXsUzbEktMf7PzWPfXe4DyipeMVv86AgKoTrw%2BXSlpqfUk6hwZWhN0sdvzbtUlULkLCoIjEB0oduPO%2FXj9axIJczOIbTIzIS6bAbSzxXjPH3vFPQ&X-Amz-Signature=85cb3125bd4ee5e0e113308578f17a5fc20b87ea5ba9dd65e3deeb33f44e352f&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

可能大家看到这个题目出现在这个地方，觉得有点偏题，实话说这并不算是一个真正的和分层架构非常强的关联的题目，但是其实我们在课程中也有提到说，因为这个分层架构和这 OSI 的这个网络的七层协议之间，其实都是一个分层架构模式的经典应用，而那所以对于我们来讲的话它也是分层架构，它也是网络。


但是实际工作中可能其实被问到的可能性对于网络工程师来说相对会多一些，对我们这种做口顶或者做 design 的相对来说会少一点。但是因为网络协议它是作为一个基础的存在，那所以说是每个人必不可少的这一个基本功，所以其实我觉得问的这个问题也无可厚非，在这里我也不会告诉大家答案，因为这个还是一句话答案，有些东西是绝对答案，有的是一个相对来说是比较开放的这些答案。比如问你什么是HCP，什么是TCIP，这个其实很好回答，但是讲一讲他们的关系，这就是说我们讲的层与层之间的依赖关系，或者他们之间的这个交流怎么交流的？它的依赖是什么？它们的通信方式是什么？这个对于我们来讲就是我们跟分层架构两个有关联的地方，那看到这个地方我们就要了解一下你怎么来回答这种题。


这个地方首先有标准答案，可能就是相对像这么讲，比如说你把完整的 HTTP 协议给背一背，当然只是背一下要点， DCPIP 的这些最主要的一些点要注意事项什么之类的，你也给它讲一讲，这样子讲完之后再讲一讲这两者之间的联系。就 h t p 是跟 TCP IP 的这个 connection 是怎么关联起来的？就我们如果只从程序员的角度，就不是从这个网络课程师的角度来看这个问题的话，那对于我们来讲，那肯定就是操作了各种对象。比如说我们先用 TCP i p 打开一个连接，而从连接当中读到的内容，然后怎么这个内容东西可能比如是一个假如说是一个流，或是一个字符串什么之类的，如何把它 convert 成一个HCP，这是一种对不对？就是从 TCP IP 形成的这样一个socket，或者是一个什么连接，然后把它读到 HTTP 的内容，因为 HTTP 层前面有讲过，它是一个相对说比较高层次的这样一个应用层，对于我们来讲的话，它更多的是程序员可能面对的比较多一点，底层的这种怎么建立连接？这些其实在很多的编程员的中，大部分的复杂逻辑怎么三层握手，这些东西都应该是不需要再做的，你都已经是可以拿到一个完整的链接，再根据这个链接得到的字符串或者流什么之类的来构成一个HTCP，再根据 HTTP 来做各种相应的操作。


对于我们来讲的话，你要回答这个问题，那就相对来说有很多种办法，前面就讲过了已经，比如说 HTTP 怎么从 TCPIP 的连接中得到了什么东西，它怎么依赖于这个 TCP IP 的连接？ CPCIP 本身又是一个什么样的连接方式？在你的这个熟悉的语言当中，不管是 Java 还是NODE， Jesse 还是whatever，你是怎么来利用这些相应的 API 或者底层这个操作方式来建立一个连接？根据这个连接怎么为上传的 HTP 来提供服务？当你在使用 HTP 这种东西的时候，比如说你要发起一个请求，你要读到一些参数，你又是怎么能利用底层网络协议？比如说你的网络层这个 connection 是不是能复用？是不是长连接？每一个 Server 与 Server 之间保持多少个长连接，有没有连接池？这些东西其实都是非常非常重要的，特别是像比如说你熟悉一点的 Java 来讲， Java 的话它有各种各样的 HTP 的 connection 的连接池，这个连接池的实现它有很多种参数的，你怎么来调整一些参数？这些参数是怎么影响 h t p？其实这都是我们这些回答问题的关键，这里我就不一一列举，反正大家就知道这个意思，朝着这个方向去回答好了。


最重要的就是前面讲到的这些 TCP IP，这个连接池也罢，单个连接也罢，它是怎么来影响了我们 HTTP 整个调用的一些性能问题，这个可能是比较重点考察的，如果能回答比较好一点的话，可能会得到很多加分项。前面我们讲到的这个 HTTP 和 TCPIP 这样连接的这种分层，这个架构里面的一些应用或者是什么的关联性，我看你架构相对来说，唉，不是那么定性紧密。所以说下面我们就拿一道架构体，或者说是一个相对来说跟我们分层架构本身比较接近的这样一个题目，就是大家看一下你对 MV seed 这样一个架构的了解程度有多深。当然诚实的说，现在如果直接问 MA seed 可能不是那么多，但是我觉得因为这个 MVC 架构它是一个怎么讲就是一个比较基础的，而且是一个最原始的这个很经典的技术架构。对，我们理解分层架构也罢，还是现在的你去看这些市面上主要的开源，这样也罢，其实都还是有很好很好的指导意义的。


所以说我觉得 MVC 呢，是看一个人的基本功力这样一个东西，所以说我还是希望大家能够好好去深入的了解一下 MVC 到底是讲了什么东西。特别如果你是字是用 Java 为主要的编程语言的话，那 spring 里面的一些东西跟 MVC 其实有很紧密的绑定的。那这个地方就是说首先问了两个问题，一般来讲都会联系问什么是 MVC 架构，这个东西我就不解释了，大家相信自己有自己的答案，对于 MVC 本身而简单，这个答案是非常简单的。


再讲一讲它的概念之间， MVC 三层互相的关系什么之类的，这个很容易的，那后面就是问你采用何种技术实现的MVC，这个答案就因人而异了，当然我这个地方举的例子都是以 Java 这个角度来分享的，一般来说就是相对比较老一点的这个技术框架里面很多人都会讲到我们使用什么 SNH 的方式来完成这个东西，这个地方就是s，第一个 s 可能是一般都是指spring，第二个 s 一般都是trust， h 是指hybrid。


这个相对来说是在一些比较怎么讲传统型企业里面使用的比较多的，因为他们的技术架构升级换得相对于比较缓慢，所以说大家听这个 trust 这个不要觉得惊讶，因为这个东西出现的时间是非常早的，现在年轻一点的在 Java 生态里面很多都不再用trust。


但是我要说一个，但是在一些老的这种 ERP 系统里面，大量的这个 strust 还存在着，这些很少升级换代的系统里面它还是存在着，所以说你一了解 trust 对你也不是什么坏处，反正你说我因为现在觉得这个太过时了，这个东西没什么，但是我还是觉得思想永远是第一位，它是相通的技术细节这个可以后面要慢慢学。但是你一定要了解这个思想，通过阅读 strust 这个代码了解它的设计架构。


其实对于你了解分层架构也罢，还是后面的比较先进的 MV seed 技术实践，包括什么MOV、 MMVP 这种东西都是应该是有一些帮助的，因为这个技术的进步都不是一蹴而就的，最初它出现了一种形态，后面被更先进的形态给替代，这个是技术的潮流，但是还这句话思想是永远相通的。


好，前面讲了这个 trust 是这个 MV seed 一种实现，这个实现的具体的方式是怎么样？大家可以通过阅读源代码或者找一些相关的资料书来看一下。这个东西我肯定不会讲细节的，大家反正就知个方向。然后再讲讲这个现代，可能在这个 Java 生态当中，如果说离室使用 MVC 比较多一点的，那可能更多的是这种 spring 的MVC，因为它整个首先 spring 的整个架构，不管你现在是用 spring crowd 还是 spring booter at my favor，或者直接用 spring MVC，这个都是很正常的。但是他们的思想包括前面讲的叫 spring MVC 单独作为一个模块存在，那同时如果说你是跟 spring boot 这些东西，包括 spring cloud 这种东西结合在一起，澄清一个新的架构，但是它的底层其实是跟 spring c 都是密不可分的。


在 spring AVC 里面为什么就说是比 trust 先进的？当然 spring 本身是一个胶水式的，这样一个框架，什么都能跟你粘在一起，什么都能让你 work 的很好。当然相对来说这些 trust 因为毕竟说实话真的有点太古老了，可能相对于 spring 它的支持可能就没有自身提供了。


spring VC 这么优秀， spring VC 跟 trust 的区别你说特别大的区别，但也不至于，但是唯一的不同的就是说 MVC 架构在 spring 当中的这种 spring v seed 实现，让你作为 spring 的这种比较熟悉的人用起来会比较怎么讲？顺手用起来比较经典，它的那个 annotation 驱动，还有包括说你这个代码的这种默认大于配置，约定俗成比较重要的这个东西，比如说你的参数里面是怎么样的取值，这个映射关系是怎么建立的？其实这个就是 spring VC 做的比较好的 this trust，跟它比可能是相对要弱一点，所以说我们使用 spring v seed 话，你可以大胆的减少你这个代码开发量，这样就是说跟 trust 相比，那其他的就到底怎么实现的？这个 MVCO 还真有点，请大家自己去看一下 spring MVC 相关的一些资料，去了解一下它的源代码，也可以来通过这种方式来学习，自己再做几个 demo 可能也能够更好地来回答这个问题。


其实这个地方面试官一般问这种问题相对来说是还是提升这初级的终极这样一个了解，来看一下你的基本功是怎么样的。这里大家就因人而异，你自己回答到可以深可以浅，自己去了解一下这些框架里面各自讲些什么东西，你可以讲一下它发展历史，各自的优缺点，你去怎么来配套。特别是如果你在 Java 生态里面，那跟 spring 的这个结合肯定是一个很重要的东西，它到底怎么跟 spring 这个框架融合在一起的，这一点可以作为一个比较重要的点。另外就是可能你比标一下什么认为 c 跟 trust 这个东西它的各自的优点在哪里？为什么会有这样的一个变化？这个我觉得也是一个加分项吧，大家反正就是好好的去看一下它源代码一版，还参考资料一版。对，你的这个回答问题应该说是易主反掌。


