---
title: 2-3 RPC通信编解码_编解码器实现
---

# 2-3 RPC通信编解码_编解码器实现

[image](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/3bff55ab-5cc5-4e35-9b54-24301965fdc9/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466332LMOHQ%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T230035Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCi85DcXh2OBHS7JFRR%2FUxb63bohdk4yOxPgmr9C6mgbQIgeqSO%2FhAwaVaQGeyOL2lclGYnbgLjieM9REYAvTf06HYqiAQIxv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDFXnRrTj9Yk0hFmwOyrcA9gGEUWqF4GmZlyikpg1I%2B79C9XDeJ13%2BaC%2BQZO8RhKzsrAkTql9rVnvqtUpmFewy46o9ycz4%2F83wj90mGmTZB2yKJIyteIS%2FeVOuwFv%2FbsWzBkSQ22B%2BQGWE%2FrDsLqNrriaTxA2%2BAUlwbVN1Jud1lAlZJKXt2Aux82n62nLyK%2Bz2Qjh9zlqQ19wds9KRwtpm%2BzI0uIjy8MXr2aqZLN73Vc43if0kq4AUkP2nPw6kktDE2FlrN4KQ5FuQfSVUDqNDIis2ir%2Fphi04w5fiFlEwOs1cm4TmIICflOaRP01BE46d6fX59SUiqptdm53xLpg0%2BPKtspR66NwRjXakGqKqcvPIuW97Zu1n8ZD3v42PahFm7En0UlDvtKW0wFoTkqJezPD3Z6G8qsEKNKFfHijw%2FfNLfksZfujLkPvugStxjZYMz5zdIRXG6S0uuJ8a1S6qFUnEsFGc4phmYJ6rjGfje7JTbykB74C%2BQIYBAdi286AzVpyv5%2BRLqvcoDq8TDoSM9jSMeHltnySPtU%2FhibUYqw1i2hHZ4%2BnYvYYHT04KtU7rclglBSyOgPZ0eeCdEggXcdpO6CcepQtgRoEFpS3PTrfUfpdivfoG%2BM5uSjXFxbHFia8EQLamo%2BSVCsZMKW3%2F9IGOqUBvXBkroEf9vEEjvDC8hlUFxgJTYf%2BWaIcw8s%2FyEfuwV%2FarqinqH9e3O5XzewFLLooACZoDebsuwNr0v2go2zLJCwOwM%2Fh4K%2F3ePK4F7U8FLpaMFM3EsVcdFABtg1AwIG4%2B9b23JC1TN6cMHsrjxKVZ3oDVXZs4HBDdRt7Jq04pNmVOG68cit1P8smtBbJo48ZjJitl2Ksay7cqMwJ8qgmwlw4EkTt&X-Amz-Signature=31b82b0fd48a1a56b199b33559a97dbf5bbf0ec0e6980e2f87a0b56f358915c6&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

hello，小伙伴们大家好，这节课我们继续往下讲。我们上节课对普吐莎 fer 已经有了了解了，我们接下来肯定是基于普通 suffer 做一个我们对应的 encoder 跟 decode 这么一件事情。我们看另外一幅图，就是在这幅图中，我们 RPC init leather，他要做的事情首先初始化，漂亮，我们做完了。接下来做的事情是什么？编解码的定义跟初始化。我们之前已经把 RPC request 跟 RPC response 协议已经搞定了。接下来的事情后面两块怎么去对它做编码和解码。

基于我们的这种普通suffer，下面还有一个叫做 lens filled base 的 frame decoder。这个东西是一个什么东西？我们现在一起就把后面的来学习一下。好，我们废话不多说，直接进入编码。接下来其实我们应该去定义两个编解码器了。这两个编解码器其实就是我们对应的 encoder 跟decoder。如果想自己去写编解码器，我先写一个编码器，我们的 RPC encoder 是我们的编码器对吧？ RPC encoder 再来一个 RPC decoder 对吧？ RPC decoder r p c d code 就是我们对应的解码器。

[image](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/a7f4aaf6-95e6-475b-85a5-ba274d2b1692/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466332LMOHQ%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T230035Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCi85DcXh2OBHS7JFRR%2FUxb63bohdk4yOxPgmr9C6mgbQIgeqSO%2FhAwaVaQGeyOL2lclGYnbgLjieM9REYAvTf06HYqiAQIxv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDFXnRrTj9Yk0hFmwOyrcA9gGEUWqF4GmZlyikpg1I%2B79C9XDeJ13%2BaC%2BQZO8RhKzsrAkTql9rVnvqtUpmFewy46o9ycz4%2F83wj90mGmTZB2yKJIyteIS%2FeVOuwFv%2FbsWzBkSQ22B%2BQGWE%2FrDsLqNrriaTxA2%2BAUlwbVN1Jud1lAlZJKXt2Aux82n62nLyK%2Bz2Qjh9zlqQ19wds9KRwtpm%2BzI0uIjy8MXr2aqZLN73Vc43if0kq4AUkP2nPw6kktDE2FlrN4KQ5FuQfSVUDqNDIis2ir%2Fphi04w5fiFlEwOs1cm4TmIICflOaRP01BE46d6fX59SUiqptdm53xLpg0%2BPKtspR66NwRjXakGqKqcvPIuW97Zu1n8ZD3v42PahFm7En0UlDvtKW0wFoTkqJezPD3Z6G8qsEKNKFfHijw%2FfNLfksZfujLkPvugStxjZYMz5zdIRXG6S0uuJ8a1S6qFUnEsFGc4phmYJ6rjGfje7JTbykB74C%2BQIYBAdi286AzVpyv5%2BRLqvcoDq8TDoSM9jSMeHltnySPtU%2FhibUYqw1i2hHZ4%2BnYvYYHT04KtU7rclglBSyOgPZ0eeCdEggXcdpO6CcepQtgRoEFpS3PTrfUfpdivfoG%2BM5uSjXFxbHFia8EQLamo%2BSVCsZMKW3%2F9IGOqUBvXBkroEf9vEEjvDC8hlUFxgJTYf%2BWaIcw8s%2FyEfuwV%2FarqinqH9e3O5XzewFLLooACZoDebsuwNr0v2go2zLJCwOwM%2Fh4K%2F3ePK4F7U8FLpaMFM3EsVcdFABtg1AwIG4%2B9b23JC1TN6cMHsrjxKVZ3oDVXZs4HBDdRt7Jq04pNmVOG68cit1P8smtBbJo48ZjJitl2Ksay7cqMwJ8qgmwlw4EkTt&X-Amz-Signature=7f53390b7f48d0ce796f6b4393261dc87a7903a6378232e19590754b4020fe25&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

[image](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/4ca698d0-2ca2-4a93-a0d4-7141452df46f/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466332LMOHQ%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T230035Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCi85DcXh2OBHS7JFRR%2FUxb63bohdk4yOxPgmr9C6mgbQIgeqSO%2FhAwaVaQGeyOL2lclGYnbgLjieM9REYAvTf06HYqiAQIxv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDFXnRrTj9Yk0hFmwOyrcA9gGEUWqF4GmZlyikpg1I%2B79C9XDeJ13%2BaC%2BQZO8RhKzsrAkTql9rVnvqtUpmFewy46o9ycz4%2F83wj90mGmTZB2yKJIyteIS%2FeVOuwFv%2FbsWzBkSQ22B%2BQGWE%2FrDsLqNrriaTxA2%2BAUlwbVN1Jud1lAlZJKXt2Aux82n62nLyK%2Bz2Qjh9zlqQ19wds9KRwtpm%2BzI0uIjy8MXr2aqZLN73Vc43if0kq4AUkP2nPw6kktDE2FlrN4KQ5FuQfSVUDqNDIis2ir%2Fphi04w5fiFlEwOs1cm4TmIICflOaRP01BE46d6fX59SUiqptdm53xLpg0%2BPKtspR66NwRjXakGqKqcvPIuW97Zu1n8ZD3v42PahFm7En0UlDvtKW0wFoTkqJezPD3Z6G8qsEKNKFfHijw%2FfNLfksZfujLkPvugStxjZYMz5zdIRXG6S0uuJ8a1S6qFUnEsFGc4phmYJ6rjGfje7JTbykB74C%2BQIYBAdi286AzVpyv5%2BRLqvcoDq8TDoSM9jSMeHltnySPtU%2FhibUYqw1i2hHZ4%2BnYvYYHT04KtU7rclglBSyOgPZ0eeCdEggXcdpO6CcepQtgRoEFpS3PTrfUfpdivfoG%2BM5uSjXFxbHFia8EQLamo%2BSVCsZMKW3%2F9IGOqUBvXBkroEf9vEEjvDC8hlUFxgJTYf%2BWaIcw8s%2FyEfuwV%2FarqinqH9e3O5XzewFLLooACZoDebsuwNr0v2go2zLJCwOwM%2Fh4K%2F3ePK4F7U8FLpaMFM3EsVcdFABtg1AwIG4%2B9b23JC1TN6cMHsrjxKVZ3oDVXZs4HBDdRt7Jq04pNmVOG68cit1P8smtBbJo48ZjJitl2Ksay7cqMwJ8qgmwlw4EkTt&X-Amz-Signature=59ec62ea992858ad4d493ae2360134bf4c461a6c266d6e29c93c86306772db6d&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

好了，我们肯定是要从编码器开始才能去再写解码器，所以你都不知道你码流怎么去编辑的，你肯定不知道怎么去解出来的对吧？在这里边注意我们的编码器，我们去继承 message to beat in Cola 这么一个编码器，哈，这个是一个最基本的。好，我们来看一看。咱们叫做 message to b y t e beat 这么一个encoder，我们编码的对象肯定是一个object。好了，我们实现了它之后，我们应该把它两个具体的一个方法，就是 encode 这个方法重写一下。好了，我们接下来打不出去。这就是我们的编码器。


编码器怎么去做？首先我编码器初始化的时候，我应该知道我编码的对象是什么，你编码的对象是什么？你基于什么去做编码？我们基于 Java 的对象对吧？因为我们做的是 RPC 框架。 RPC 框架它并不关心底层数据怎么去传输的，它只需要知道这个类是什么，调用这个类的某一个方法就可以去实现远程通信了。就跟我们 double 一样，给我提供接口跟方法，名字参数类型就可以了。我们首先就应该知道 encode 需要知道的类。编码器的类是什么？我们就写 go 的方法就好了。它是一个 class 类型，我们暂时可以给它一个不确定的东西，因为在这里你肯定能不能说把它写死成 request 对吧。
咱们叫做 Jana 瑞克 class glass，这是我们的要编码的一个类。好，它是类型的。我们用一个变量 private generic a class 来赋一下值。 this 点 generic class generator class 等于 generate class。有了它之后就简单了。


我们在写 encode 的时候来我们来看看直接判断什么？判断 if 当前的message，说白了就是编码进来的message。我们编码器主要是做什么事情？无非就两件事情。第一件事情就是把对应的 Java 对象进行编码，之后把内容填充到 buffer 中去。最后第三步写出到 server 端。就是这么三件事情。这个就是我们要编码的一个 Java 对象对不对？我要把 Java 对象进行编码，编码之后我要把它写到 buffer 中，我用 CTX 点 out 把 buffer 写到我们的另外一端。这么一个简单的事情就很简单了，我们 if 首先判断一下我的 generic class。


第二， is instance of 是不是 is instance？如果跟我这个 message 它们是同一种类型的，对不对？你不能说，你给我传进一个user，你说你编码对象是一个 user 对象，你给我来一个 group 肯定不好使，对吧？本来我编码的对象是一个request，你给我编进去一个 response 肯定不行。所以我要判断一下，如果是instance，我再进行编码。 else 你可以去搞一个异常，或者是直接抛出一个异常都可以。接下来你就进行编码了。编码就是一个 Java 对象怎么去变成序列化的一个data。在这里老师提前已经写好了。我们有一个 Siri lesson 这么一个工具类，当然这个工具类就是我们之前的 Pro to suffer util，它俩是一样的。我其实为了区分一下，上节课我们做测试代码都是没改变的。我为了区分一下别我使用错工具类了，他们两个类代码都是一样，我就把它 copy 过来改一下名字。大家可以看到基本上是一样的。
首先就是一个编码，一个解码对吧？它是工具类，都是 stack 的。我直接拿它的编码就可以了。 serializer 一个扎好对象，我给你返回一个贝特字节数组对不对？我们的 encode 就好办了。我直接调用它的什么 Co lesser 就可以了。把我们的 message 放进来，说白了，他放进来直接返回一个贝塔字节数组。


d y t e 技术，我们叫data。好了。这是第一件事情做完了，进行编码了，变成一个data，直接数组了。第二件事情很简单，是不是直接是把它填充到我们的buffer，我们就right。什么 right data 吗？直接这样去写可以吗？直接 right data 可不可以？其实也可以。


当然更好的方式是做什么？其实小伙伴们应该知道一个概念，叫做我们的消息体分整个消息网络传输的消息分为两种，一种是我们的包头，还有一种是包体，对吧？简单来说，我可以自己去指定包头跟包体，比如我的包头是什么包头？我们整个数据到底是多少长度？我最简单的去定义可不可以先把长度给它 right 出去，可不可以 right 进去？ get Int 这个 Int 是什么？你自己编码之后的 data lens。我不知道小伙伴们能不能看懂我这个意思。我的包头就是我们数据包长度。当然这是我自己所定义的哈数据包长度。当然其实你的包头里面可以加一些其他的信息，比如一些 c r， c code 或者一些其他的任何的信息。你可以把 header 去做一个封装成一个对象。


我在这里简写我的包头，里面的信息就是我们整个数据包的大小。对，包体就是数据包的内容。我这数据包内容就是字节数组。好，我这样去做定义，小伙伴们能不能理解对吧？我编码是按照这种方式去编码的。首先前面 4 个字节，因为 Int 类型，它是 4 个字节，前面 4 个字节输出的是它整个这次请求数据包的长度，后面的内容跟着的它的包体。我解码的时候我怎么去判断多长？我怎么判断它是一个请求过来的，是不是我首先得解码的时候，先取出前四个长度，读出前四个长度是多少个字节，比如 128 个字节，我再往下去数 128 个字节，把这 128 个字节拿出来，再做一个反序列化才知道具体的内容对吧？所以怎么编码的？你对应的应该怎么解码？就这么一回事儿。


好了，现在我的编码器已经写完了，我们来一起看一看解码。解码器也是一样的，对不对？我们编码器是什么？是实现了那个类，叫做 message to beta encoder。解码器肯定是 message to bait decoder 就可以了对吧？它也是 NET 给我们提供的，我们去继承制。我刚才已经复制了。


wait to message decoder，因为解码的时候是一个二进制的字节数组，转成一个对象 to message，抵扣的这个东西，你是不需要知道它具体是什么内容的，你把这个东西重写一下 decode 就可以了。解码的时候我们应该做什么事情？解码的时候我们需要知道这个对象是什么吗？肯定的。首先 private class 我们还是对应的，把编码的时候 copy 过来就可以了。把换一下，这就是我们的 RPC decode 进行解码的时候我们要做的事情。怎么去解码？小伙伴们想不想解码就简单了，按照编码的规则进行解码就可以了。我们来看一看。


解码器的时候，我直接判断一下。我说 in 就是 buffer 里的内容，我去点 readable base，我去读一下它当前的产生度到底是多长。它 buffer 里边可读的信息如果小于 4 个长度，就认为它压根就没传完，有问题我就直接 return 就可以了。


我不知道小伙伴们能不能理解，因为我们在编码的时候，在 encode 的时候起码会有 4 个长度，起码包头里边是占 4 个长度的， 4 个字节对不对？你即使你给我传个空的东西，你包头里边 4 个长度肯定是4，这肯定的。后面 date 内容是0，这里边你给我传个空的信息，起码这里边是个 0 对不对？ 0 它也是占 4 个字节数字组，你不给我传空的东西也是肯定有的。 OK 这是一个最基本的。所以这里边小于 4 就 return 就好了，不需要做其他事情。接下来的事情你要做一个叫做in，它是一个buffer，它是一个 net 的buffer。我不知道小伙伴对这个熟不熟悉，叫做 mark read index。就来做个标记。这个标记以后，接下来我们要做的事情就是来假设他没有return，应该是 readable dates，就是可读的哈。如果小于4，我就 return 就好了。


我记得小于 4 之后，我还要做个标记，做个记号对不对？就从这个位置开始读。我要把当前的数据的长度，我要知道是多少长。数据长度不在我 read Int 对不对？我肯定要先读一个点。 Read Int。 read Int 肯定就是我们最开始编码的时候，前四个字节肯定就是一个数据包的大小。我在做个标记，我要知道我当前的数据大小是多少，是不是我再去判断。我说 if in 点 readable 这个base，如果你小于我实际的date。nice，好，我问你，小伙伴们就说明什么。前面我在这打注释，如果请求数据包不足 4 个字节，直接返回对吧？ OK 如果在这里说，哈，如果大于等于 4 个字节，程序继续执行。


OK，这是第一点。第二点。首先记录一下当前的位置对吧？当前的我读的位置是什么？因为 net 的buffer，它有两个指针，一个是读指针，一个是写指针。OK，进入一下当前的位置，从当前的位置开始，我去往下读 4 个字节。说白了就是把数据包当前请求数据包的大小读取出来。我们编码的时候是按照这种方式编码，解码的时候也是一样的。如果我取出来的数据包是 128 个字节，但你实际情况下它可读的字节不是 128 个字节，证明可能你还没传完。这里有说意思。没传完怎么办？没传完了之后，我就印点 reset 去做一个重置， read next return 就可以了。他没唱完的是吧？如果相等或者是大于等于相等了怎么办？比如你实际上是 128 个字节，你给我传了 200 多个字节，我大于我只读 128 个字节，后面的我不读，我下一次过来的时候再读就好了。 OK 接下来很简单，我们就直接把这个东西我们想读多大，我们就取出来。先把它预先生成一个 b y t， e 直接数组。我想读 date line 这么大，我去读出来是不是？我就 in 点 readable base，我就想读这么大的内容，我就把它读出来，放到 data 里边就可以了。好，现在你已经调用 read base，已经相当于把内容从缓存 buffer 里边读到了 data 贝特字节数组里了。是不是这是真正读取需要长度的数据包内容？好了，接下来的事情不是好做了吗？我们知道我们编码的时候是用它去编码，解码的时候很显然拿它做解码就好了。


第二， disaalizer 把 data 传进来。我解码的对象到底是什么？我解码的对象我这里已经告诉你了。是不是我构造解码器的时候，我就知道我解码的对象是什么？所以在这里边直接拿过来就好了。拿过来干什么？我要写出去。最后一步是不是我编解码的过程？解码了之后，我要把它变成一个 buffer 去 out 出去，是不是我编解码器？大家都知道 night 它的里内特 handler channel 这个东西，它是一个传播的过程，它的pipeline。它走完编码器解码器之后，它继续往下，一定会流转到我们的实际业务定义的执行器中，是不是它会往下传，但是它到业务执行器中，它是什么东西？它是一个buffer，所以你应该还有一个out，这么一个东西应该给它写出去，是不是后来给他加进去了？我就直接点 at 就可以了， at 一个object，我的 object 就是在这里返回的码。我们解码的时候，解出来的时候就反序列化的时候，到底这个对象是什么？我不知道，我直接给他加进去就好了。这边就是一个解码操作，返回指定的对象。


OK 填充到 2 号洲传播给下游 handler 做实际的业务处理。因为编辑码可能就实际的处理它，不一定是业务处理，可能在这之中可能还有一些其他的handler，这都不一定。好了。 OK 我问你，现在我们的 encoder 跟 decoder 代码已经写完了，好办了是不是？接下来我们回看我们的 init leather 是不是我们刚才自己定义的一些协议。我们上几节课，还有我们自己的一些编解码器都已经搞定了。接下来我们的事情就简单了。接下来我们就开始去往 paper line 中去加入我们刚才所定义的一些内容。


at last 首先我们可以 new 一个我们的 RPC encoder 编码器。 RPC encoder 编码它是应该把 request 进行编码，所以 RPC request 对象几个类加class。这得需要接下来。解码器是我们需要 RPC 抵扣的解码。解码它肯定得需要一个具体实际的解码的内容。肯定是我们的 response 对象需要解码对不对？ R p c。我们的 response 就是一个解码器。 sorry 调 class 哈。好了，这是在 decode 的时候，我们 client 端是这样的，我们的 server 端肯定就反过来了是不是？当然，我们 server 端现在编解码我还没去写，我们到时候去写的时候你肯定还得加上哈。我不知道小伙伴们能不能理解哈，我现在只是写的可烂的端的编码器这块编解码。


clang 端，它编码肯定是对应的是 request 进行编码了，对不对？它解码的时候肯定得是服务端给我的响应，如果它响应，它肯定是response，解码的时候肯定是这样的，但是这是对应着客户端，服务端肯定得反过来。服务端去解码的时候肯定解码的是request，编码的时候编码的是response。 OK 但是我们现在还没有去写服务端代码，我们现在只是写客户端的对吧？所以小伙伴们你一定要对整个编解码的一个思路，整体的逻辑应该非常清晰哈，这就对了。 OK 我们现在写的是客户端的编解码器。


好了，接下来我们做的事情最后一步，我们应该加上 RPC 的 client handler，这是实际的业务处理器对不对？好在这我可以把注释放到这。实际的编解码动作，实际的业务处理。好了。在这里边我们还需要最后一件事情。最后一件事情是非常重要的，我们写到哪都行，写到中间，写到前面后面都可以，因为它这个东西无所谓的。我们再加一个爱的last，我先把它写完，然后再跟小伙伴们去讲清楚这是一个什么东西。哈，咱们叫做 new lens Lance。什么叫做 failed Lance， filled base 的，然后叫做 frame decoder。这是一个 net 给我们提供的一个解码器。哈，nice，写错了，没有迪克，它首先有好多参数，我们就选一个最全的全一点了。如果选一个 5 个参数的，哈，这是两个参数， 3 个参数，选一个长一点的 5 个参数。好，就这个。好了。我们来说一说每个参数代表什么意义？第一个就是什么。第一个整个数据包的大小是多大？我们认为 65535 其实就差不多了，跟 535 跟 536 差不多了。


lens field offset 起始位置从 0 开始，这里边有一个叫做 lens filled。 lens 什么意思？我写成4，后面 just 我就写成0，后面我就不管了。 OK 我加上一个东西。这个东西啥意思？首先我们来看一看这里边的说明。他说 Max frame says the Max is the length of the 什么frame？ if the length of the frame is 什么什么什么？ then this value 我们看这个，其实最关键的就是这两个东西。他说 lens filled our set，还有一个 lens filled lens。我把这两个 copy 过来，我们放到这里面跟大家简单说一下，这两个是非常关键的。 offset 是什么意思？就是你数据包的起始位置是什么？然后 lens fail 的 lens 是什么意思？你的第一个关键的位置是多大？我为什么这里边是0？这是4。我用一个图跟大家来画一下，大家就知道了。我们重新再来一个画图工具。


再来一个流程图，跟大家说一下。这个东西是一个decoder，是一个相当于解码的时候要做的一个事情。我们回忆一下我们在编码的时候我们做了什么事情？同学们想一想在编码的时候我们做了一个什么事情？在编码的时候我们做的一个事情是我们看一下编码，哈。编码的时候，我们做的事情很简单，前四个长度认为是包头，后面是消息体对不对？所以我一个数据发出的时候，前四个字节就是一个包头，后面就是一个消息体。我在底 code 的时候也是这么去做的。前四个字节我读出来就认为是消息体。消息头的大小，这个消息头里边包含的是消息体的大小，再真正去根据 lens 去取到消息体，去读出来做序列化操作，这是一套的。


这个东西是一个辅助的 nice field basic frame decoder，它也是一样的，它告诉你最大的数据包大小是这么大，它第一个参数0，还有第二参数4。它这两个表示的这是我整个数据包，是不是数据包？这个数据包我用一个竖线表示哈，你用一个竖线放大一点哈。假设这是我们一次数据包。


这个数据包开始的第一个 lens offset 就表示从哪个位置开始，这个位置是多少，这个位置一定是0。这个位置下面就是从 0 到多少个长度，多少个字节。长度表示你是属于一个包头的内容，我们四个长度，后面的内容就是实际的从到我们实际的消息体了。这个就是消息体。可能消息体是 128128 个长度，里边 0 到 4 之间。它是一个 Int 类型，它里边表示了整个包体是 128 个长度，它把 128 数值 c 到了 0 到 4 之间，刚才我们看到的这个东西，它表示的是什么？数据包的起始长度从 0 开始，到第四个字节表示的长度是我们的包头。你可以认为他可以去帮你去快速的去解析出来，后面的内容不怎么关键了，你可以不用去关注了他。


其实做一个辅助的工作，帮你去做一个数据包的解析。哪怕你在真正去做解码的时候，抵扣的时候，你这逻辑你写的不是那么好，他也会帮你去解析。现在我们看到我们的 RPC client init leather 类对应的编解码的逻辑已经完成了。好了，我们这节课就讲到这，谢谢小伙伴们收看。

