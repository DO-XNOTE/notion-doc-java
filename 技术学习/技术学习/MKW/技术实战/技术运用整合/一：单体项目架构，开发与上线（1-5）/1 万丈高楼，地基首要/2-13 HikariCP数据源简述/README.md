---
title: 2-13 HikariCP数据源简述
---

# 2-13 HikariCP数据源简述

[image](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/0fe9d277-8a7c-49d2-9b7d-767ccf67d9d1/SCR-20240816-pkup.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RZOFEDH2%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T224608Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDEzuUCS6%2FvazfhG%2BNebzi%2BfZTk8ep5yE0PIqC%2FS%2FTuxAIhANslRNnvSgowX0sGfh%2BXDcib52bpMHxArT4ad51av39oKogECMb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1Igz7Uvm5w3qYe7biPrAq3APExRZdfcXyjRUVALNiWYku%2F8C1hxU23fBIfbv7MMMR5MfgolVFSKcJiVwyoiJhJllHzffdzKX%2BxixNEEE3epH%2BWeiAg99rnUthSM7KQ1PRXIRUf%2FjbQiMim73ZJSW8vHh%2FOxz%2BHNMCbg0j0VuTo%2FDowivGWuGb7aR%2BLTJn1GKuPi2hK7Qg1idY3kW0BUwYAxIA7k%2BLCcn7Q4OeeeY6fSp19g4yuHs03Gz7OlxRUhpcc%2BSqJPUELxherd37ORehDyVZVCDyBfnCYL5wLmV1HuLo99%2B%2F6ynl6RxrBELwOfL12AEY20yA0EavwUorxN4pmK1rCXXQvpV5PQlJS3DCdCNtTnF2SHQRaZfaJKBE%2FasfvXCr3%2FrQYUJsCuJgi%2BoN%2FjqJIFF8rFxd3lWcTA3voYri1U6F%2F%2BGLf%2B3GcwzDJd5bPMQbkfHsSggOzdFrJYBoMzK%2Bp2%2Bn5AFm7iKOwnl0Qb6axpsoudrmOR2TnWLQINFotaBV3pzuhKNjkm14LyCZH0ZZWOHoFBlOjLFp12t8XsBV8XFCcuB0u7vyozhSj8P%2Boj8xCS9pPvB5nRIGH9rUhE55HKnsmzFimsc3IoPE9T8mLs6PCjC4QLicxXksuP8IJKadEOshL2KMYm6pHzCiuP%2FSBjqkAajB2aSuOm%2BsguLOMLBa7qQCFKwKHC68r4pQ6GEU0t5eIEDTElDbn3bNfm1%2BylQCfQzVsn7H025nHn9kFW7ZnwtrWy7GKGPXSf5rlcq46%2BPKxA6Brmllh4l%2Fl%2FALt5wQumTpP53TZUxcd3e1jjcp%2FdMyu%2FajoytnjiL90s6zl8Ref77nhJYCk5SzM0aaEk%2BhJ3JADfe3XKEr7jj41OrvuAIffa9O&X-Amz-Signature=0c38eb4039d578c9e656ccdf848f3946b886ecaf073f561759915e1697d37fd8&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

[image](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/08128f8c-30aa-4a81-b4f5-e880ebf0ebf4/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RZOFEDH2%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T224608Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDEzuUCS6%2FvazfhG%2BNebzi%2BfZTk8ep5yE0PIqC%2FS%2FTuxAIhANslRNnvSgowX0sGfh%2BXDcib52bpMHxArT4ad51av39oKogECMb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1Igz7Uvm5w3qYe7biPrAq3APExRZdfcXyjRUVALNiWYku%2F8C1hxU23fBIfbv7MMMR5MfgolVFSKcJiVwyoiJhJllHzffdzKX%2BxixNEEE3epH%2BWeiAg99rnUthSM7KQ1PRXIRUf%2FjbQiMim73ZJSW8vHh%2FOxz%2BHNMCbg0j0VuTo%2FDowivGWuGb7aR%2BLTJn1GKuPi2hK7Qg1idY3kW0BUwYAxIA7k%2BLCcn7Q4OeeeY6fSp19g4yuHs03Gz7OlxRUhpcc%2BSqJPUELxherd37ORehDyVZVCDyBfnCYL5wLmV1HuLo99%2B%2F6ynl6RxrBELwOfL12AEY20yA0EavwUorxN4pmK1rCXXQvpV5PQlJS3DCdCNtTnF2SHQRaZfaJKBE%2FasfvXCr3%2FrQYUJsCuJgi%2BoN%2FjqJIFF8rFxd3lWcTA3voYri1U6F%2F%2BGLf%2B3GcwzDJd5bPMQbkfHsSggOzdFrJYBoMzK%2Bp2%2Bn5AFm7iKOwnl0Qb6axpsoudrmOR2TnWLQINFotaBV3pzuhKNjkm14LyCZH0ZZWOHoFBlOjLFp12t8XsBV8XFCcuB0u7vyozhSj8P%2Boj8xCS9pPvB5nRIGH9rUhE55HKnsmzFimsc3IoPE9T8mLs6PCjC4QLicxXksuP8IJKadEOshL2KMYm6pHzCiuP%2FSBjqkAajB2aSuOm%2BsguLOMLBa7qQCFKwKHC68r4pQ6GEU0t5eIEDTElDbn3bNfm1%2BylQCfQzVsn7H025nHn9kFW7ZnwtrWy7GKGPXSf5rlcq46%2BPKxA6Brmllh4l%2Fl%2FALt5wQumTpP53TZUxcd3e1jjcp%2FdMyu%2FajoytnjiL90s6zl8Ref77nhJYCk5SzM0aaEk%2BhJ3JADfe3XKEr7jj41OrvuAIffa9O&X-Amz-Signature=634e690a5b8be77e30498315b73fcbe0df8a015bb943afb021196334f1ee3e9b&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

现在我们的一个项目是可以通过 spring boot 去运行的，只不过我们还没有去结合数据层，要结合数据层做整合。首先第一个我们要想到的就应该是数据源。在数据源我们在这里会选择铁卡里CP，当前这个网页就是关于数据源的提卡里CP。其实它在 spring boot 里面，当 spring boot 由 1 点叉升值为 2 点叉的时候，默认的数据源就发生了一个更改。


 spring boot 官方就选择了  HikariCP  作为它的默认数据源了，主要是因为这个数据源是非常的快。对于 Hikari 来讲，这是一个日文的发音，光速的意思也写了叫光。它下面也说了 high-performance JDBC conection pool，它是一个非常高性能的 jdbc 连接池，这也是为什么 SpringBoot 官方会采取它的一个原因。它下面也说了它是 its faster，非常快。它要比其他的数据源都要快。


我们来看一下有两张图。

[image](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/f965fe34-b2fd-4e40-8f2b-9da807fbb7a6/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RZOFEDH2%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T224608Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDEzuUCS6%2FvazfhG%2BNebzi%2BfZTk8ep5yE0PIqC%2FS%2FTuxAIhANslRNnvSgowX0sGfh%2BXDcib52bpMHxArT4ad51av39oKogECMb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1Igz7Uvm5w3qYe7biPrAq3APExRZdfcXyjRUVALNiWYku%2F8C1hxU23fBIfbv7MMMR5MfgolVFSKcJiVwyoiJhJllHzffdzKX%2BxixNEEE3epH%2BWeiAg99rnUthSM7KQ1PRXIRUf%2FjbQiMim73ZJSW8vHh%2FOxz%2BHNMCbg0j0VuTo%2FDowivGWuGb7aR%2BLTJn1GKuPi2hK7Qg1idY3kW0BUwYAxIA7k%2BLCcn7Q4OeeeY6fSp19g4yuHs03Gz7OlxRUhpcc%2BSqJPUELxherd37ORehDyVZVCDyBfnCYL5wLmV1HuLo99%2B%2F6ynl6RxrBELwOfL12AEY20yA0EavwUorxN4pmK1rCXXQvpV5PQlJS3DCdCNtTnF2SHQRaZfaJKBE%2FasfvXCr3%2FrQYUJsCuJgi%2BoN%2FjqJIFF8rFxd3lWcTA3voYri1U6F%2F%2BGLf%2B3GcwzDJd5bPMQbkfHsSggOzdFrJYBoMzK%2Bp2%2Bn5AFm7iKOwnl0Qb6axpsoudrmOR2TnWLQINFotaBV3pzuhKNjkm14LyCZH0ZZWOHoFBlOjLFp12t8XsBV8XFCcuB0u7vyozhSj8P%2Boj8xCS9pPvB5nRIGH9rUhE55HKnsmzFimsc3IoPE9T8mLs6PCjC4QLicxXksuP8IJKadEOshL2KMYm6pHzCiuP%2FSBjqkAajB2aSuOm%2BsguLOMLBa7qQCFKwKHC68r4pQ6GEU0t5eIEDTElDbn3bNfm1%2BylQCfQzVsn7H025nHn9kFW7ZnwtrWy7GKGPXSf5rlcq46%2BPKxA6Brmllh4l%2Fl%2FALt5wQumTpP53TZUxcd3e1jjcp%2FdMyu%2FajoytnjiL90s6zl8Ref77nhJYCk5SzM0aaEk%2BhJ3JADfe3XKEr7jj41OrvuAIffa9O&X-Amz-Signature=2d0fc59a26f8afb898b362107b6ac4e6b391d388998702e58769598960d75d9b&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

在这两张图里面粗略的就可以看得到，这一侧有两个绿色的，还有这一侧有一个红色的柱子，非常的高。这两根柱子其实就是皮卡里。我们可以来看一下它的一个对比。下面包含了其他的一些比较流行的数据源。 C3P0, DBCP2,Tomcat ，也就是vibe。这个比较冷门，我个人其实也没用过。从这里面看得出来，咱们的  HikariCP  要比多了将近 10 倍。在我们的一个右边的这张图，这边是 Tomcat 和 HicriCP 的一个对比，它们相差将近两倍的数值，所以 Hikri 它是性能非常高的。



下面是要去使用美稳的一个依赖，它是最低 JDK 是从 6 就可以了， 678 都可以去使用。当然，我们在使用 spring boot 的时候，我们是没有必要再额外的引入依赖了，因为它默认就已经帮你去整合了。如果你在某一些项目里面使的是 spring MVC ，想要去进行一个数据源的切换，就可以使用HikriCP，通过这种方式去引入它的一个相应的依赖就可以了。


OK，这是它的一个官网，官网其实现在我是打不开来，但是如果你翻一下，你是可以去访问的。但是没有关系，它其实也有github，github  地址大家也可以去访问一下。到github  上去搜一下，也会有。在这里面它在下方的图。这是它一些相应的代码。它的一些解释和它的官网其实都是一模一样的。它是这么说的，它很快，它也非常简单，也是一个非常授信的。为什么会这么牛，在这边给了一个解释。会有一个文档。在这里可以看得出来它的一个大小只有是 130 k， b 非常小。它也是一个轻量级的。有一个文档可以点击读一下。点进来以后有一大堆的英文。可以来看一下。


Arelis，其实它并没有去使用，它使用的是一个FastListt。原先像有一些 statement 是放到 a realist 里面，它 was replaced 已经被替换成了自定义的一个FastListt。里面它的一个速度要比 releast 更快。随后它有一个 concurrentbag。这个 concurrent 其实看得出来它是和并发相关的。并发的时候，它的一个性能效率会非常高。从它的英文看得出来，它是一种自定义的无锁的一个集合，它就称之为是 concurrentbag。这种想法它其实是从 C#.NET  里面所借鉴的，因为在 C#.NET  里面也包含了这样的一个class。它提供了一些相应的功能，比方是一个无锁的设计。其次是一个 three local catching，这个是用去存数据的。随后是一个 queue stealing 取数据。最后一个是 hand off 这样的一个优化，这时候是并发集合性能非常高。在高并发的时候，其实如果从监控曲线图可以看得出来，我们整体的一个HikriCP 的稳定性也是非常高的。


下一个是 invoke virtual 和 invoke static，目前是使用 static 替换掉了virtual。下面有一个简单的对比来看一下。首先一个替换掉了以后，有一个 getstatic 这样的一个 call 就是回调，这样已经是没有了，直接是去掉了。从我们代码里面就可以看得出来，原先它在这里是有一个 getstatic 的，现在在这里就已经是没有了。 getstatic 这是第一点。


最后第三点，也是最后一点来看一下现在其实如果我们使用了 invokestatic 以后，它的堆栈的一个大小从 5 减少到了4。从对比里面可以看得出来，最新的是4，原来的这里是一个5。OK，他也说了一个原因，主要是因为当我们使用 EMOCK photo 的时候，它会有一个相应的 instance 实例。这是一个代理工厂 proxy factory 在 static 上，所以它在 b 站上会比较大，会多了 1 这两者简单的一个对比。


OK，其实我们也是和 spring boot 官方一样，我们会追随他的脚步，使用 HikariCP   作为我们的一个数据源去进行使用。当然肯定也会有一部分同学会问能不能使用 Druid ，也就是阿里的数据源德鲁伊数据源。这个数据源在老外的官网上并没有去对比，主要是因为老外对比的时候选取了一些国外比较流行的，比较常用的一些数据源，所以其实在我们国内用的是比较多的。我们曾经在 spring VC 项目里面使用的大多都是主语的数据源，当然在 SpringBoot 1点叉里面我们也是使用的数据的。


在我们的一个项目里面，我还是尽量的建议使用 HikariCP ，因为 HikariCP 其实要比主语的性能相对来说还是要更加好一些，足以的和 HikariCP   在网上也是有一些相应的对比的。评论在这里我就不去多说了，大家有兴趣可以去找一下，或者问老师说一下。我们在课程里面就不去专门针对这两者做过多的一些对比的。OK，我们下一节课也会使用我们的项目来整合HikriCP，OK。

