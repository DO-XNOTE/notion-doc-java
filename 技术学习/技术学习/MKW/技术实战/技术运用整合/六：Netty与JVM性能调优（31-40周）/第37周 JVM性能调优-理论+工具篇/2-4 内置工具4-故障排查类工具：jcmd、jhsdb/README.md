---
title: 2-4 内置工具4-故障排查类工具：jcmd、jhsdb
---

# 2-4 内置工具4-故障排查类工具：jcmd、jhsdb

[image](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/2851444f-9ee3-40b8-9dbb-06b4fdd013b0/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662KWZCOGP%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T230143Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQC6cUhihx1BxH7D20qQrUyb6Zn3esWvRmWbMVp1%2BF2QZQIhALSPgv0yOm24BV5yK%2BCqGL72xVBbPFw3mxBPGrYxNFkAKogECMb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgxUeBFHGQ550QIluTcq3AMKGYwlzXZxxdSoGwgR35Fc6IFeJFJjW2CcGIZI40wTJeR20stWZahN%2B2jS47ese0bOrEw5WkHwY%2FO5BXZ9jQpTx3q1jadTT89K19EjNZF8cxJCPFXHgw%2FrkD1YBX4blJJQkgeRDzeru56tbZdfv6ONd%2B1vsPCAPeUyCz8gtXVenjM%2F6pWn8cQJKbkrLEJHDHOp%2BHNL9Ai9J%2FbmiLLMBaX%2F3qzO1c9mW9fZ2gfNwTdL2m3lrREFKS5nBbOxFlkGPoQgVvWEqyKvii8pYWte%2BT58DEZMKhfZSMg0RNtT2sSPvPcY7ruaZPq0UKAjcNbM0BAYvTpUKEubtgIV6x5a8GIKXAhH5RV5lYbnThxyngM9F3tmILHZ1ziFB1nGRJwrh7HaRn4iW62SUqgq0MB43F3iztNHaYejQTbqy0X68amj1m8X0JyxsxKxr4eVkwK4UHNLnSeFBHW3mMn3L9sgjcAECUawE7%2Fu9WT83VdBTVORblOlNDI%2Fx8j8V6hKnQKaM9shRugBR0Hkguo9LcubMLQ1pVoPDfKLTeo3OEnNLUAL7gIobgn0wwDXGcyMGKW5mRZeUJl2n85EvnPmsZwCuVGW%2F57ZiU7SjvIDeEOB8fmfRCg9H1iina2sHABw9TDut%2F%2FSBjqkAcsB8xlcBJPEWoBr7I1aYBs1zObXPRKahVDTrZ3%2FneHqUIortQLaDkZbs7Gvc9CwD7TXLueWV46k4%2BCd%2BvYmgTiiNt0fZSiceUlmopSq%2Br9i5aFBtQhqNKwatErOl%2FGhpQAvWbQ4254TMLjN%2BAqSfVU9dDgNkE0QmAxrqzPsHlssWDHXNC4HxuzMUKiyflBBb2FEYNHJk3XaREwPYLF4duj%2F1qoh&X-Amz-Signature=a7207d00a3207b3dda303660b8093912245229d8df43d194f1eb0f30edcc8d9e&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

[image](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/e7f857e2-18ad-4d75-9b71-dcfb1ada33bc/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662KWZCOGP%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T230143Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQC6cUhihx1BxH7D20qQrUyb6Zn3esWvRmWbMVp1%2BF2QZQIhALSPgv0yOm24BV5yK%2BCqGL72xVBbPFw3mxBPGrYxNFkAKogECMb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgxUeBFHGQ550QIluTcq3AMKGYwlzXZxxdSoGwgR35Fc6IFeJFJjW2CcGIZI40wTJeR20stWZahN%2B2jS47ese0bOrEw5WkHwY%2FO5BXZ9jQpTx3q1jadTT89K19EjNZF8cxJCPFXHgw%2FrkD1YBX4blJJQkgeRDzeru56tbZdfv6ONd%2B1vsPCAPeUyCz8gtXVenjM%2F6pWn8cQJKbkrLEJHDHOp%2BHNL9Ai9J%2FbmiLLMBaX%2F3qzO1c9mW9fZ2gfNwTdL2m3lrREFKS5nBbOxFlkGPoQgVvWEqyKvii8pYWte%2BT58DEZMKhfZSMg0RNtT2sSPvPcY7ruaZPq0UKAjcNbM0BAYvTpUKEubtgIV6x5a8GIKXAhH5RV5lYbnThxyngM9F3tmILHZ1ziFB1nGRJwrh7HaRn4iW62SUqgq0MB43F3iztNHaYejQTbqy0X68amj1m8X0JyxsxKxr4eVkwK4UHNLnSeFBHW3mMn3L9sgjcAECUawE7%2Fu9WT83VdBTVORblOlNDI%2Fx8j8V6hKnQKaM9shRugBR0Hkguo9LcubMLQ1pVoPDfKLTeo3OEnNLUAL7gIobgn0wwDXGcyMGKW5mRZeUJl2n85EvnPmsZwCuVGW%2F57ZiU7SjvIDeEOB8fmfRCg9H1iina2sHABw9TDut%2F%2FSBjqkAcsB8xlcBJPEWoBr7I1aYBs1zObXPRKahVDTrZ3%2FneHqUIortQLaDkZbs7Gvc9CwD7TXLueWV46k4%2BCd%2BvYmgTiiNt0fZSiceUlmopSq%2Br9i5aFBtQhqNKwatErOl%2FGhpQAvWbQ4254TMLjN%2BAqSfVU9dDgNkE0QmAxrqzPsHlssWDHXNC4HxuzMUKiyflBBb2FEYNHJk3XaREwPYLF4duj%2F1qoh&X-Amz-Signature=1a81fd1611d027a93cd4c83d4a33ebeb64fcf64601a397b9babdeadb349cd3be&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

[image](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/d5bc9746-2916-4c71-ad89-81f0df28e47c/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662KWZCOGP%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T230143Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQC6cUhihx1BxH7D20qQrUyb6Zn3esWvRmWbMVp1%2BF2QZQIhALSPgv0yOm24BV5yK%2BCqGL72xVBbPFw3mxBPGrYxNFkAKogECMb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgxUeBFHGQ550QIluTcq3AMKGYwlzXZxxdSoGwgR35Fc6IFeJFJjW2CcGIZI40wTJeR20stWZahN%2B2jS47ese0bOrEw5WkHwY%2FO5BXZ9jQpTx3q1jadTT89K19EjNZF8cxJCPFXHgw%2FrkD1YBX4blJJQkgeRDzeru56tbZdfv6ONd%2B1vsPCAPeUyCz8gtXVenjM%2F6pWn8cQJKbkrLEJHDHOp%2BHNL9Ai9J%2FbmiLLMBaX%2F3qzO1c9mW9fZ2gfNwTdL2m3lrREFKS5nBbOxFlkGPoQgVvWEqyKvii8pYWte%2BT58DEZMKhfZSMg0RNtT2sSPvPcY7ruaZPq0UKAjcNbM0BAYvTpUKEubtgIV6x5a8GIKXAhH5RV5lYbnThxyngM9F3tmILHZ1ziFB1nGRJwrh7HaRn4iW62SUqgq0MB43F3iztNHaYejQTbqy0X68amj1m8X0JyxsxKxr4eVkwK4UHNLnSeFBHW3mMn3L9sgjcAECUawE7%2Fu9WT83VdBTVORblOlNDI%2Fx8j8V6hKnQKaM9shRugBR0Hkguo9LcubMLQ1pVoPDfKLTeo3OEnNLUAL7gIobgn0wwDXGcyMGKW5mRZeUJl2n85EvnPmsZwCuVGW%2F57ZiU7SjvIDeEOB8fmfRCg9H1iina2sHABw9TDut%2F%2FSBjqkAcsB8xlcBJPEWoBr7I1aYBs1zObXPRKahVDTrZ3%2FneHqUIortQLaDkZbs7Gvc9CwD7TXLueWV46k4%2BCd%2BvYmgTiiNt0fZSiceUlmopSq%2Br9i5aFBtQhqNKwatErOl%2FGhpQAvWbQ4254TMLjN%2BAqSfVU9dDgNkE0QmAxrqzPsHlssWDHXNC4HxuzMUKiyflBBb2FEYNHJk3XaREwPYLF4duj%2F1qoh&X-Amz-Signature=9b776e41c977056de00ae53cee586d838df5d07e4064f4ddefe6ccfac98166ae&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

好，下面来看一下第5款故障排查工具 j c m d。 g s m d 是一款正式支持的工具，主要用来将诊断命令发送给虚拟机。 g s m d 的功能非常的强大，支持的诊断命令非常的多。对于 Jessica 11 有这么多的诊断命令， 45 个，所以可想而知 j c m d 使用起来也要稍微复杂一点。


下面我们来看一下 j c m d 是怎么玩的。它的命令格式有三种。我们先看最简单的 j c m d 杠l，可以查看当前正在运行的所有 j v m 进程，和 g p s 有点类似。第二种格式 g s m d 杠 h 可以查看 g c、 m d 的帮助文档。关键是这种格式。可以看到这种格式有好些参数，同时还有多种组合，下面来详细探讨。


我们先输入g、s、m、d。第二个参数可以输入进程号，也可以指定一个启动类。我们先指定一个进程号26089。第三个参数可以传入command，也就是诊断命令，或者是 perf counter print 这样的一个固定值。或者还可以传入杠 f 跟上一个文件。我们先用 perf count print copy 粘贴，这样就可以查看 26089 进程的性能计数器。我们换一种玩法，先用 GPS 加 l 获得启动类，用j、c、m、 d 跟上启动类。


再来一个 perf counter，可以发现也可以正常获得结果。下面我们先回到这种格式，然后把第二个参数的 perf counterprint 改成诊断命令。比方，我们来使用 compiler code cache，这样就可以查看 26089 进程代码缓存的布局。比方进程代码缓存最大有这么大？使用了这么大，曾经最多使用了这么多，当前还剩这么多可用。第二行展示了代码缓存的边界，有关代码缓存的后面一点的章节会详细探讨。


其他的诊断命令也是类似的玩法。我们挑几个典型的玩一玩。比方 g c hip dump 诊断命令可以生成 Java 堆 dump 文件，同时它还有一些可选项和子参数。玩一下。歼 c m d 26089 g c keep a dump 杠 all 跟上文件，比如 my heap dump 点 h p r o f，就创建这样的一个文件。不难发现 g c keep dump 诊断命令可以达到前面建 map dump 的一个效果，对吧？好。


接着看第二个。比较有意思的是 g c run 这个参数，它会去调用 system g c，从而去通知 g v m 做一次垃圾回收。这个命令比较简单，这里就不演示了。接着看 thread print，可以查看所有带有堆栈跟踪的线程。摆一下 j s m d 二六零八九 copy 粘贴，可以发现它和前面讲的 jeystack 比较类似。此外，你还可以杠l，这样可以在原先的基础上额外打印加y，有条 concurrent 锁的信息，其他的命令同学们可以试一试，玩一玩都不是很复杂，在用到的时候记得到手机里面查询就可以了。


好，有关 j c m d，我们就探讨到这里，


下面来探讨最后一款内置的故障排查工具 jhsdb。 j h s d b 是一款功能非常强大的 hot spot 虚拟机的进程调试器。这款工具是从 jdk9 才开始引入的。不过对于 jdk 8 以及更早的版本，要想使用 j h s d b 也是有办法的。这是因为在 jdk 8 以及更早的版本里面， Java home 的 library 目录，有一个价包，叫做 s a j d i 点价？这个价包可以理解为 j h s d b 的原型，所以对于 j d k 8 以及更早的版本，要想使用 j h s d b，只要把价包启动起来就可以了。

[image](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/c98004cf-d1c9-45fb-b910-6f1de2d739f7/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662KWZCOGP%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T230143Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQC6cUhihx1BxH7D20qQrUyb6Zn3esWvRmWbMVp1%2BF2QZQIhALSPgv0yOm24BV5yK%2BCqGL72xVBbPFw3mxBPGrYxNFkAKogECMb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgxUeBFHGQ550QIluTcq3AMKGYwlzXZxxdSoGwgR35Fc6IFeJFJjW2CcGIZI40wTJeR20stWZahN%2B2jS47ese0bOrEw5WkHwY%2FO5BXZ9jQpTx3q1jadTT89K19EjNZF8cxJCPFXHgw%2FrkD1YBX4blJJQkgeRDzeru56tbZdfv6ONd%2B1vsPCAPeUyCz8gtXVenjM%2F6pWn8cQJKbkrLEJHDHOp%2BHNL9Ai9J%2FbmiLLMBaX%2F3qzO1c9mW9fZ2gfNwTdL2m3lrREFKS5nBbOxFlkGPoQgVvWEqyKvii8pYWte%2BT58DEZMKhfZSMg0RNtT2sSPvPcY7ruaZPq0UKAjcNbM0BAYvTpUKEubtgIV6x5a8GIKXAhH5RV5lYbnThxyngM9F3tmILHZ1ziFB1nGRJwrh7HaRn4iW62SUqgq0MB43F3iztNHaYejQTbqy0X68amj1m8X0JyxsxKxr4eVkwK4UHNLnSeFBHW3mMn3L9sgjcAECUawE7%2Fu9WT83VdBTVORblOlNDI%2Fx8j8V6hKnQKaM9shRugBR0Hkguo9LcubMLQ1pVoPDfKLTeo3OEnNLUAL7gIobgn0wwDXGcyMGKW5mRZeUJl2n85EvnPmsZwCuVGW%2F57ZiU7SjvIDeEOB8fmfRCg9H1iina2sHABw9TDut%2F%2FSBjqkAcsB8xlcBJPEWoBr7I1aYBs1zObXPRKahVDTrZ3%2FneHqUIortQLaDkZbs7Gvc9CwD7TXLueWV46k4%2BCd%2BvYmgTiiNt0fZSiceUlmopSq%2Br9i5aFBtQhqNKwatErOl%2FGhpQAvWbQ4254TMLjN%2BAqSfVU9dDgNkE0QmAxrqzPsHlssWDHXNC4HxuzMUKiyflBBb2FEYNHJk3XaREwPYLF4duj%2F1qoh&X-Amz-Signature=31ac1690ba0c1969a563234bc9177555ef368db6a327ca3d27bdc23ef0ee2bf5&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

下面我们来对照文档操作一下。首先使用 export 临时修改一下 Java home 环境变量，把 Java 版本切换到 jacket 8， copy 粘贴，为 s a j d a 点价，授予执行权限。接着启动这个价包，就可以运行 j h s d b 了。可以发现已经进入 j h s d b 了。输入 help 可以看到 j h s d b 的子命令，输入 control c 退出。


好，下面我们来看一下 j d k 9 以及更高的版本里面的 j h s d b 是怎么玩的。不难发现， j h s d b 这个工具还是比较有特色的，因为它和其它的工具都不一样，它有很多的子命令，什么 c l h s d b debug， d h s d b j stack 等等。这是我们前面讲到的工具都没有的。再一个，不同的子兵领用法还略有差异。有的子命令是用杠杠 p i d 去指定一个进程号，有的子命令又是直接指定进程号的。所以这些命令不建议同学们去记忆，而是在用到的时候回来查文档。好，下面我们来玩一玩。
g h s d b。



第一个字命令接 h s d b c r h s d b 对照文档copy。因为在窗口下，我们刚刚已经用 export 把 Java 版本设成了 JDK8 了，对吧？所以我们需要新开一个窗口，可以发现这个窗口是 jdk 11 的。 copy 粘贴26089，发现报错了。这是因为我们所使用的 j d k 版本十一点零点七。
对 macos 版本的 j d k 是没有办法使用 j h s d b 的。我在文章里面也写了解决方案，解决方案也比较简单，把版本降级降到十一点零点四。同学们如果使用的是macos，并且安装的是 jdk 十一点零点七，可以到地址下载一下 jdk 十一点零点四，或者也可以在百度盘去下载。下载完成之后安装一下。



我已经安装好了。我们依然使用 export 加了 home 去临时修改环境变量。 copy 粘贴引号，把版本改一下。 11 点 0. 4，输入 Java 杠version。可以看到现在版本已经切到 10 一点零点四了。但是当我们去使用 j h s d b c r h s d b 26089 的时候，依然会报错。这是因为我们的 26089 进程是用 j d k 十一点零点七启动的， j d k 十一点零点四里面的 j h s d b 没有办法连接 j d k 十一点零点七里面的Java、进程，所以我们需要把 26089 进程给杀掉。
到福地 DV 这个项目执行 Maven clean install 构建假包，切换了 target 目录 p w d，展示目录，详情 copy 到终端，切换到 target 目录。再用 Java 杠架负 d v 启动。这个时候就是用 j d k 十一点零点四启动应用的了，对吧？



好，再开一个窗口，再次使用export，把窗口下面的 j d k 版本也设成 j d k 十一点零点四使用j、 p s 进程是37652，这个时候再次使用， j h s d b c r h s d b。跟上进程号3762，就可以正常执行了。到现在我们终于可以安心的玩 j h s d、 b 了对吧？可以发现使用 c r h、 s d、 b 这个子命令和刚刚我们启动c、a、j、d、 a 点价效果是一样的。都会进入到一个交互命令行界面。我们也输入 helper 命令，这样就可以看到 c r h、 s d、 b 的子命令。但是我们发现 helper 命令展示出来的帮助文档非常的简陋，每个子命令是做什么的都没有展示。这里弹幕把这些命令的作用也整理出来了，同学们可以看一看。


在这里比方使用 assert true 就可以打开assert，使用 assert force 就可以关闭assert。又比如像 flags 可以展示所有以叉叉开头的j、 v m 参数等等等。这里我们挑选两个玩一下。 Flags 可以看到这么多的结果。以叉叉开头的 g m m 参数以及它的值都会展示出来。你也可以使用 blacks 指定一个参数，这样就可以看到指定参数的值。


再比如 G1 region details 这样的一个子命令，可以查看 G1 垃圾收集器每一个 region 的起始值，结束指针，以及这个 region 是哪一个分代，是伊电源还是 survivor 还是老年代。其他的参数使用起来也是大同小异的，同学们可以自己玩一玩。


好。回答文档。 c r h s d b 是基于命令行的，而且 c r h s d b 的子命令又非常的多，所以在使用的时候相对复杂一些。 j h s d b 也考虑到了这一点，它提供了 h s d b 子命令功能。和 c r h s d b 基本上是等价的，但是有图形化的界面，使用起来相对直观一些，能够在一定程度上降低 j h s d b 的使用难度。来玩一下 control c 剔除，把 c r h s d b 改成 h s d b，可以发现会打开一个界面，然后再尝试连接 3762 进程。连接完成之后就可以看到界面了，大家可以操作。


有关图形化模式，我们将会在下一节详细探讨。这节我们先来过一下 j h s d b 的各个子命令。关掉第三个子命令 j info 子命令和前面讲解的 j info 命令功能上基本上是一致的，但是它没有办法动态修改。 j m 参数比较的简单。还有建 map 指命令，和前面讲解的建 map 功能基本上也是一致的。 jstack 指命令和前面的 jstack 功能基本上一致。 j snaps 命令可以打印性能计数器相关的信息。我们玩一下 happy 粘贴指令进程3762，可以发现 j snap 和前面的 j c、 m d perf counterprint 功能是一致的。



最后还有 debug d 字命令格式是这样子的，不需要杠杠 p i d。不过我在执行之后发现机器根本没有任何的反应，也不会报错。而且我搜遍了百度和谷歌，依然没有找到解决方案，甚至连讲 debug 地的文章都非常的少，所以课上就没有办法演示了。同学们可以试一试命令能不能正常执行。另外，如果能够找到解决办法，也请告诉一下大木。


再一个，经过讲解不难发现，要想实现相同的目标，我们常常有多种选择。比方想要 dump 加把堆，你可以使用j、h、s、d、 b 的 j map 子命令，也可以使用 j c、m、d，还可以使用 j map 弹幕。把相同的目标，不同的命令都整理出来了，同学们可以看一看，也希望这个表格能够帮助同学们增强记忆。这节课就到这里，谢谢大家。

[image](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/4326aa8e-00be-4eaf-9bbc-e6aeb56b3993/2020-09-17_193315.jpg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662KWZCOGP%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T230143Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQC6cUhihx1BxH7D20qQrUyb6Zn3esWvRmWbMVp1%2BF2QZQIhALSPgv0yOm24BV5yK%2BCqGL72xVBbPFw3mxBPGrYxNFkAKogECMb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgxUeBFHGQ550QIluTcq3AMKGYwlzXZxxdSoGwgR35Fc6IFeJFJjW2CcGIZI40wTJeR20stWZahN%2B2jS47ese0bOrEw5WkHwY%2FO5BXZ9jQpTx3q1jadTT89K19EjNZF8cxJCPFXHgw%2FrkD1YBX4blJJQkgeRDzeru56tbZdfv6ONd%2B1vsPCAPeUyCz8gtXVenjM%2F6pWn8cQJKbkrLEJHDHOp%2BHNL9Ai9J%2FbmiLLMBaX%2F3qzO1c9mW9fZ2gfNwTdL2m3lrREFKS5nBbOxFlkGPoQgVvWEqyKvii8pYWte%2BT58DEZMKhfZSMg0RNtT2sSPvPcY7ruaZPq0UKAjcNbM0BAYvTpUKEubtgIV6x5a8GIKXAhH5RV5lYbnThxyngM9F3tmILHZ1ziFB1nGRJwrh7HaRn4iW62SUqgq0MB43F3iztNHaYejQTbqy0X68amj1m8X0JyxsxKxr4eVkwK4UHNLnSeFBHW3mMn3L9sgjcAECUawE7%2Fu9WT83VdBTVORblOlNDI%2Fx8j8V6hKnQKaM9shRugBR0Hkguo9LcubMLQ1pVoPDfKLTeo3OEnNLUAL7gIobgn0wwDXGcyMGKW5mRZeUJl2n85EvnPmsZwCuVGW%2F57ZiU7SjvIDeEOB8fmfRCg9H1iina2sHABw9TDut%2F%2FSBjqkAcsB8xlcBJPEWoBr7I1aYBs1zObXPRKahVDTrZ3%2FneHqUIortQLaDkZbs7Gvc9CwD7TXLueWV46k4%2BCd%2BvYmgTiiNt0fZSiceUlmopSq%2Br9i5aFBtQhqNKwatErOl%2FGhpQAvWbQ4254TMLjN%2BAqSfVU9dDgNkE0QmAxrqzPsHlssWDHXNC4HxuzMUKiyflBBb2FEYNHJk3XaREwPYLF4duj%2F1qoh&X-Amz-Signature=868015aec2a52ef2a88a5e0954c08d0224f8002e875cbf03cf3e8d90d32a64a4&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)


[image](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/9c0e1b17-b529-4d9e-a079-6077e64905f8/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662KWZCOGP%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T230143Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQC6cUhihx1BxH7D20qQrUyb6Zn3esWvRmWbMVp1%2BF2QZQIhALSPgv0yOm24BV5yK%2BCqGL72xVBbPFw3mxBPGrYxNFkAKogECMb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgxUeBFHGQ550QIluTcq3AMKGYwlzXZxxdSoGwgR35Fc6IFeJFJjW2CcGIZI40wTJeR20stWZahN%2B2jS47ese0bOrEw5WkHwY%2FO5BXZ9jQpTx3q1jadTT89K19EjNZF8cxJCPFXHgw%2FrkD1YBX4blJJQkgeRDzeru56tbZdfv6ONd%2B1vsPCAPeUyCz8gtXVenjM%2F6pWn8cQJKbkrLEJHDHOp%2BHNL9Ai9J%2FbmiLLMBaX%2F3qzO1c9mW9fZ2gfNwTdL2m3lrREFKS5nBbOxFlkGPoQgVvWEqyKvii8pYWte%2BT58DEZMKhfZSMg0RNtT2sSPvPcY7ruaZPq0UKAjcNbM0BAYvTpUKEubtgIV6x5a8GIKXAhH5RV5lYbnThxyngM9F3tmILHZ1ziFB1nGRJwrh7HaRn4iW62SUqgq0MB43F3iztNHaYejQTbqy0X68amj1m8X0JyxsxKxr4eVkwK4UHNLnSeFBHW3mMn3L9sgjcAECUawE7%2Fu9WT83VdBTVORblOlNDI%2Fx8j8V6hKnQKaM9shRugBR0Hkguo9LcubMLQ1pVoPDfKLTeo3OEnNLUAL7gIobgn0wwDXGcyMGKW5mRZeUJl2n85EvnPmsZwCuVGW%2F57ZiU7SjvIDeEOB8fmfRCg9H1iina2sHABw9TDut%2F%2FSBjqkAcsB8xlcBJPEWoBr7I1aYBs1zObXPRKahVDTrZ3%2FneHqUIortQLaDkZbs7Gvc9CwD7TXLueWV46k4%2BCd%2BvYmgTiiNt0fZSiceUlmopSq%2Br9i5aFBtQhqNKwatErOl%2FGhpQAvWbQ4254TMLjN%2BAqSfVU9dDgNkE0QmAxrqzPsHlssWDHXNC4HxuzMUKiyflBBb2FEYNHJk3XaREwPYLF4duj%2F1qoh&X-Amz-Signature=9c17c88d8ab72fc6a663153c5945d56902565fd76d604a0936e80567b4914607&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)




