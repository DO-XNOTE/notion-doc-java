---
title: 1-6 逃逸分析、标量替换、栈上分配
---

# 1-6 逃逸分析、标量替换、栈上分配

[image](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/a4583363-cf08-45aa-bc8c-e353dad5d7d2/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466Q4L6X7O2%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T230134Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIC9kEPSgD%2FGGveTv%2FqLBkKhAXsKgmSqRRsAB%2FsYdG3grAiEAhC9lqJ42Nx7VsZ00X9Wtx8TbYp4ThhishcQ4jHVLJRQqiAQIxv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDITJ55ndP%2BXrNaPyVSrcA8OIGPmI4tFohtM23kTho5RscO%2Fp6QAKBlTUwRm6BwVFXUHPi6NmrXuICgpCeZxKn20GBCv%2FTWsV3D0BlJ6B4xS1lvdLs2OhjclgsBVddoeDuHddu5q4YmYJIoIp4aMN2XcCZybKOVkeZcj8aSNPtvNvh3WkBRFwb0%2FiomdT%2FKs4%2BeuOy1CeWdqzUyTrWHmLVMGtbsefUtRkKn0Keys7bg44%2FSg%2BaSjPd5%2BS60IZ9zaObit92CTL66K3QplTz0C7TypJeTcRNcKOg8Tpp4RcWTivfqYFSg%2FrI7exyX0ROttnlJ0LQ5QccJHun5BkSbHJqsnzCK%2FPsQUP1SVK4EoviZ8i7q%2F6NnS14gSBagOEArUJGRohugUlG4f3c6HqejaiRtICrA279ESv%2BuVj2OyUrGUxS8wQrSMe4sMBYW2EEEUZuO64xsS2ZmmVI%2FWMwfxgJtpHjDs3feWU5kROb1T3NxXajkOqDKBK%2BLwic7SkMB35GePQ9%2B47WV8IAZ77hATXOE4y0HJYRRnUDhwZrPQbdLa8mr5i0rv8U0JSupOh%2BQKrTRR%2F07v2ie%2BrQBN%2FVWdFS2XW4JO5URtpmtPDhFeDkXArUNYs8tTAonGXaAf3Sg6pI8ic4tVfTrhGzazXMIW3%2F9IGOqUBfejA2miwm%2FMTMwQZvsVQKCKwSeQkzzg3zF0cMbhhq0fCYnlJ2xB5RkBb9ifDxqL%2Bd%2BL%2FLAGFAkNstkIuy%2FPEHIkwFjflG%2BgVPKLaBMA9c4EvgBOI5TYceCWWP2CzUYBqWP6aHCOjUossedhxtbpXaDpncqxDiBiW7dQfEImPbNPSPZvxq5JPxDdMj%2Fs3mYq4UN49petVuGt2DxxGIm5z7Oxu9fXs&X-Amz-Signature=97ec19ff3b84a004f873ccadb8d3b754d1faa7a19ce90e0b29290f79171943e7&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

[image](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/9921d839-eef7-490b-bda0-8e32641f0d07/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466Q4L6X7O2%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T230134Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIC9kEPSgD%2FGGveTv%2FqLBkKhAXsKgmSqRRsAB%2FsYdG3grAiEAhC9lqJ42Nx7VsZ00X9Wtx8TbYp4ThhishcQ4jHVLJRQqiAQIxv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDITJ55ndP%2BXrNaPyVSrcA8OIGPmI4tFohtM23kTho5RscO%2Fp6QAKBlTUwRm6BwVFXUHPi6NmrXuICgpCeZxKn20GBCv%2FTWsV3D0BlJ6B4xS1lvdLs2OhjclgsBVddoeDuHddu5q4YmYJIoIp4aMN2XcCZybKOVkeZcj8aSNPtvNvh3WkBRFwb0%2FiomdT%2FKs4%2BeuOy1CeWdqzUyTrWHmLVMGtbsefUtRkKn0Keys7bg44%2FSg%2BaSjPd5%2BS60IZ9zaObit92CTL66K3QplTz0C7TypJeTcRNcKOg8Tpp4RcWTivfqYFSg%2FrI7exyX0ROttnlJ0LQ5QccJHun5BkSbHJqsnzCK%2FPsQUP1SVK4EoviZ8i7q%2F6NnS14gSBagOEArUJGRohugUlG4f3c6HqejaiRtICrA279ESv%2BuVj2OyUrGUxS8wQrSMe4sMBYW2EEEUZuO64xsS2ZmmVI%2FWMwfxgJtpHjDs3feWU5kROb1T3NxXajkOqDKBK%2BLwic7SkMB35GePQ9%2B47WV8IAZ77hATXOE4y0HJYRRnUDhwZrPQbdLa8mr5i0rv8U0JSupOh%2BQKrTRR%2F07v2ie%2BrQBN%2FVWdFS2XW4JO5URtpmtPDhFeDkXArUNYs8tTAonGXaAf3Sg6pI8ic4tVfTrhGzazXMIW3%2F9IGOqUBfejA2miwm%2FMTMwQZvsVQKCKwSeQkzzg3zF0cMbhhq0fCYnlJ2xB5RkBb9ifDxqL%2Bd%2BL%2FLAGFAkNstkIuy%2FPEHIkwFjflG%2BgVPKLaBMA9c4EvgBOI5TYceCWWP2CzUYBqWP6aHCOjUossedhxtbpXaDpncqxDiBiW7dQfEImPbNPSPZvxq5JPxDdMj%2Fs3mYq4UN49petVuGt2DxxGIm5z7Oxu9fXs&X-Amz-Signature=720246cf914c704df325b7a1cd7d2c0aa80e9796ac8523c2bbae7d87149e496d&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

大家好，我是大木。这节课来探讨逃逸分析，标量替换以及栈上分配。有关逃逸分析在讲 think next 的时候已经简单聊过了。这节课我们先来详细探讨一下逃逸分析，再来探讨编译器优化的两大措施，标量替换以及栈上分配。标量替换和栈上分配都是基于逃逸分析去做的。


好，下来探讨逃逸分析。逃逸分析指的是分析变量能不能逃出它的作用欲，前面已经讲过了。它可以细分为 4 种场景。第一是全局变量赋值逃逸，第二方法返回值逃逸，第三实例引用逃逸以及线程逃逸。这样讲比较的抽象，我们来看一段代码示例，这段代码演示了 3 种逃逸的场景。 global 这个方法里面我们把一个局部变量赋值给了一个静态变量，局部变量的作用域是在方法内部，类变量的作用域是在类里面，所以作用域被放大了，显然发生了逃逸。 method pointer escapes 方法里面，我们返回了一个对象，对象的作用域一开始也是在方法内部的，但是我们作为返回值返回了。这个时候假设有另外一个方法，比如这里的 some method 方法，调用了这里的 method pointer escaper 方法。 some class 的作用域是在 some method 的方法里面，所以这个变量的作用域就从 some partner escape 扩张到了 some method 的方法，所以也发生了逃逸。


instance pass pointer escape 这里的 this 传给了下面的 print class name 方法。 this 的作用域原先是在当前实例下的，但是现在扩张到了 some class 的实例下面去了，所以也发生了逃逸。


好回答 p p t 另外，我们这里还有一个线程逃逸，没有去做代码示例，限制套衣其实比较好。总结当复制给类变量，或者复制给其他线程里面可以访问的实例变量，就会发生线程逃逸。好。以上是对象逃逸的 4 种场景。 g v m 在做逃逸分析的时候，会针对这些场景进行分析，分析完成之后会为对象做一个逃逸状态标记。一个对象主要有三种逃逸状态标记。第一是全局级别逃逸，它表示一个对象可能从一个方法或者线程里面逃逸，也就是其它的方法或者其它的线程也能够访问到这个对象，主要有以下几种场景。第一是对象作为方法的返回值返回。第二，对象作为静态字段或者成员变量，可以命中到这里的两种场景对吧？第三，如果重写了某一个类的 finonize 方法，那么这个类的变量都会被标记为全局套一状态，并且一定会放在堆内存里面。


第二种状态参数级别逃逸。如果一个对象作为参数传给一个方法，但是除这个方法以外，其他的方法不能访问这个对象，其他的线程也不能访问这个对象，就说明是参数级别逃逸。像我们这里的实例引用传递参数级别逃逸。第三种状态无逃逸状态，指的是一个对象不会逃逸。好了解逃逸分析之后，再来聊聊标量替换。首先，什么是标量？所谓的标量，指的是不能进一步分解的量。像 Java 的基础数据类型以及对象的地址引用都是标量，因为它们是没有办法继续分解的。和标量对应的是聚合量。聚合量指的是可以进一步分解的量。比方字符串就是一个聚合量，因为字符串是用字节数组实现的，可以分解。又比如我们自己定义的变量也都是聚合量。什么是标量替换？来看一下。


标量替换指的是如果经过逃逸分析，可以确定这个对象不会被外部访问到，并且对象也可以进一步分解 jvm。它并不会创建这个对象，而是创建这个类的成员变量去代替。举个例子，假设有一个类叫 some test，里面有一些成员变量，这些成员变量都是基础类型的，也是标量。比如 Int i d， Int age。在这里我们有一个方法叫 public void some test，我们 new some test，用 some test 点 a 几。短语一 some test 点儿 ID 等于1。如果开启了标量替换，并不会直接创建 sum test 实例，而是创建 sum test 的成员变量去代替。也就是开启变量替换之后，这段代码就被优化成了 Int age 等于1， int i d 等于1。把对象进行标量替换之后，原本的对象就不需要分配内存空间了，可以使用 eliminate allocations 开启标量替换。这里可以把默认开启的好，下面再来聊聊栈向分配。



我们知道 Java 里面绝大多数对象都是存放在堆里面的，当对象没用的时候，靠垃圾回收器去回收对象对吧？什么是栈向分配？它指的是如果通过逃逸分析，任对象不会被外部访问到，就直接在站上分配对象。在站上分配对象，对象占用的空间就会在战争出战的时候被销毁了。所以通过栈上分配可以降低垃圾回收的压力，对吧？好简单总结一下这节课的内容。


这节课首先探讨了什么是逃逸分析。如果经过逃逸分析，发现变量不会被外部访问到，会有两种优化一是标量替换，可以把聚合量用若干个标量代替，从而结束内存。二是栈上分配，直接在栈上分配这个对象，这样可以降低垃圾回收的压力。相关的 j v m 参数有几个。开启逃逸分析开启标量替换。默认情况下都是开启的。此外，不要忘记基于逃逸分析可以实现锁消除。锁消除也可以认为是即时编译器的一种优化机制。有关锁消除。同学们如果感到陌生，可以复习一下 think nice 的相关的章节。好，这节课就到这里，谢谢大家。



