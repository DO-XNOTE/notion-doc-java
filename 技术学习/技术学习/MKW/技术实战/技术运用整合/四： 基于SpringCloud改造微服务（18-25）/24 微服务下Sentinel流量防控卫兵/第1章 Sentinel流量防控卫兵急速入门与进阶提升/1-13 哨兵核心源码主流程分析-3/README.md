---
title: 1-13 哨兵核心源码主流程分析-3
---

# 1-13 哨兵核心源码主流程分析-3

[image](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/ada6a9b1-a7f2-4189-b744-6b42727cb264/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XODOGPY5%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T225834Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCCQOV9Er20ZuzBTfMtjkSxnRealbd2Jo3dbuMSrqzrkAIhAOUmpmpee4lkL7XB%2Bwil%2FCRhD30WSC3soFb70Fw238xVKogECMb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1Igxb1Ml4H1v8vCKhOyMq3AMv0WbnE2R1yTeRgcVCZMnYsgJn6qKhzd3a29Cz2k2wLyb1wwI63%2FDxriSZgBHRTi1DgWMeX0wxCZGgqE0J3Sfp4hsu%2FDyde%2BfmqRGOzRJWKa2uclmd%2FzOB6dBrNKiEbx%2FUk51rWjxdyuw2Fyig2mqmOK%2FAJk2XEvuLVcDn33bMux4UApBTG4Aq8FVWO2aQbTazSKMr8EoF59CiJADze34TrZUOsNB3uM7b9kLt8vR0lyDGENYWQKHRfpYDENHr24W9D6RD7m2Ut6SZNm9MYBAPYhkA5Yyy%2BaOjbHJDKDXZfc%2B1lZVhkDe5%2Byx4eynFRp8K%2F3ruzJt4KfN70Owu79dn5U%2BT21IEs7Roi5DjM%2FRf407EtHYCYPL%2BRWbfkQo%2Fyw1Bn1XbYk%2FMyDIXscFYILd%2BoaBN7DJXiBWBErxwrAz6Z4%2BziXBlUKyi6M1de1%2F%2BeRJmJYSGxqMZk9iRT9C8UjA60TRSgWAUsswZuy1r1HAbcDERYKZvp3JXkuWM8pj%2Bo9AUaQ56InEtGZatFg%2FNih9NbfwZgJmyYuFaHBMtXmxrnx9Dj7Ncj9YB9LAzLWiRnJ1UcXYDA9VKrmrGRmLMVs%2FUzTyeCSGd%2FDNwKTfQlPPY5CfFNK%2FruzaeYr5JlDDCuv%2FSBjqkAXH7p7kAIvh0kL8fGE0ko%2BCvkRYUFVlzDjNCxOO9FwR1De8BwbiHzW8Nz76%2FSdl%2B28Qw1CdjxDoe4TeRa4xwAfK7p%2Fa5SK93Fw9gAGNsvGi1iMoSpVyD5ipvo3YJmQYGbxaO85iqCn0RRWEFedLx98IRLrYLKDxMQB1Epyd6bgLuVd83CojDIrcDT0fNnwF7KM7rG7%2BGzxlJTHUIoRzkF47Gu1bZ&X-Amz-Signature=e589bfc87966dda8845147d3beec273faf6f5daafe01c649a3d95d69bba1d1ab&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

[image](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/cd0429cb-a6d6-4b5d-9cf0-e6f48fcecdd6/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XODOGPY5%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T225834Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCCQOV9Er20ZuzBTfMtjkSxnRealbd2Jo3dbuMSrqzrkAIhAOUmpmpee4lkL7XB%2Bwil%2FCRhD30WSC3soFb70Fw238xVKogECMb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1Igxb1Ml4H1v8vCKhOyMq3AMv0WbnE2R1yTeRgcVCZMnYsgJn6qKhzd3a29Cz2k2wLyb1wwI63%2FDxriSZgBHRTi1DgWMeX0wxCZGgqE0J3Sfp4hsu%2FDyde%2BfmqRGOzRJWKa2uclmd%2FzOB6dBrNKiEbx%2FUk51rWjxdyuw2Fyig2mqmOK%2FAJk2XEvuLVcDn33bMux4UApBTG4Aq8FVWO2aQbTazSKMr8EoF59CiJADze34TrZUOsNB3uM7b9kLt8vR0lyDGENYWQKHRfpYDENHr24W9D6RD7m2Ut6SZNm9MYBAPYhkA5Yyy%2BaOjbHJDKDXZfc%2B1lZVhkDe5%2Byx4eynFRp8K%2F3ruzJt4KfN70Owu79dn5U%2BT21IEs7Roi5DjM%2FRf407EtHYCYPL%2BRWbfkQo%2Fyw1Bn1XbYk%2FMyDIXscFYILd%2BoaBN7DJXiBWBErxwrAz6Z4%2BziXBlUKyi6M1de1%2F%2BeRJmJYSGxqMZk9iRT9C8UjA60TRSgWAUsswZuy1r1HAbcDERYKZvp3JXkuWM8pj%2Bo9AUaQ56InEtGZatFg%2FNih9NbfwZgJmyYuFaHBMtXmxrnx9Dj7Ncj9YB9LAzLWiRnJ1UcXYDA9VKrmrGRmLMVs%2FUzTyeCSGd%2FDNwKTfQlPPY5CfFNK%2FruzaeYr5JlDDCuv%2FSBjqkAXH7p7kAIvh0kL8fGE0ko%2BCvkRYUFVlzDjNCxOO9FwR1De8BwbiHzW8Nz76%2FSdl%2B28Qw1CdjxDoe4TeRa4xwAfK7p%2Fa5SK93Fw9gAGNsvGi1iMoSpVyD5ipvo3YJmQYGbxaO85iqCn0RRWEFedLx98IRLrYLKDxMQB1Epyd6bgLuVd83CojDIrcDT0fNnwF7KM7rG7%2BGzxlJTHUIoRzkF47Gu1bZ&X-Amz-Signature=b29c336cb61568c11910e0a615fe0b98bc8a9be29a501ce451d320fb66b323a0&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

我先处罚他，然后处罚他处罚他。 OK 那我们随便点一个，比如说我们看一下 node select slot 里边做了什么事情，我们来点到 node select 里边，我们看到这里边做了什么事情，你会看到这里边它安全方法的时候，他做的事情。首先是有一个 default node 来先把它搞出来，先判断等不对空，如果等于空加锁，加完锁之后再判断怎么对空，如果还等于空的话，一样的去把它铺得进去。 OK 然后他再调下一个节点，其实你会看到它就是一个组织，这也是一个树形的拼装，我就不往里去点这个源码，我们回过头来再看下一个叫做 cluster builder slot 我们点它看它里面的 entry 这里面的安全方法也是一样的 double check 然后，把它弄出来之后再把它扔到这个 new map 里面。 OK 然后再去做一些相关的操作，然后再触发下一个节点。那下一点又做什么事情呢？这个 log 就没什么可说要记录日志了。那这个是比较核心的，叫做 statics slot 这里边我们来点进去看它的安全。

```shell
@Spi(isDefault = true)
public class DefaultSlotChainBuilder implements SlotChainBuilder {

    @Override
    public ProcessorSlotChain build() {
        ProcessorSlotChain chain = new DefaultProcessorSlotChain();

        List<ProcessorSlot> sortedSlotList = SpiLoader.of(ProcessorSlot.class).loadInstanceListSorted();
        for (ProcessorSlot slot : sortedSlotList) {
            if (!(slot instanceof AbstractLinkedProcessorSlot)) {
                RecordLog.warn("The ProcessorSlot(" + slot.getClass().getCanonicalName() + ") is not an instance of AbstractLinkedProcessorSlot, can't be added into ProcessorSlotChain");
                continue;
            }

            chain.addLast((AbstractLinkedProcessorSlot<?>) slot);
        }

        return chain;
    }
}
```


首先在 fire entry 的时候做哪些事情，它这里边 node node 上面已经生成的节点，对这个节点做什么呢？做一个 increase thread number 就是添加线程数量，添加通过的这个 pass request 数量。 Count. 这个 count 就是1，每次进来我就加1，每次进来我就加1。那这个东西是一个什么东西？ debot load 它的 pass 这个 count 是，它有一个 node cluster 有一个 add pass quest 再点到它的父类这个分类里边其实很抽象，里面好多大家其实可以看到源码里面有描述的很清楚，就是说它这里面就是针对于好多个信息进行统计，比如说总的，阻塞的请求，还有这个阻塞的 QPS 等等，这些东西它都是帮你去做一个统计。


但这些统计指标其实还有一个比较关键的概念叫做 metricmetric 是一个什么东西，你马上看这个叫做 array metricarray metric 又是一个什么东西呢？你再点它这个东西就比较深了。 array metric 这里边还有一个关键的模型叫做利普瑞这个利普尔瑞我不知道小伙伴们有没有印象，在之前的课程中，老师跟小伙伴们已经接触过了，它是一个滑动窗口的实现。我们先不看那么清楚，我们回过头来，也就是说当前这个 stay dex slot 你只需要知道他帮我们去统计 QPS 统计、线程的数量统计等等的一些指标。那你看它里边都是做统计，包括 catch 异常的时候也是做各种各样线程的统计技术，然后做节点的统计，包括这里边都有好多好多 set error 这个设置， block 的 QPS 这里边都是做一些流控的统计。


说白了，这个 static slot 他专门就去做统计分析的，他最底层的是什么呢？最底层的刚才我们其实看到最底层的就是我们刚才点过去了，点到这个 metric 这个 metric 它其实是一个 array metric 这个 metric 你再点一句，它最终真正的数据结构是一个利普瑞。


好，这个利润位到底是一个什么东西？点进来，这是我们整个哨兵核心的数据结构。好，我们看到这个利普尔瑞，这个利普尔瑞，它里边有三个属性，我们最大化一下。首先第一个叫做 window less minutes 这个我就可以表示说每一个小窗口的时间的长度或者叫做跨度。然后这个音透音 MS 它表示窗口的总跨度。你可以这么去理解，我在这打个注释。比如说我们按照 60 秒一个窗口，那这个它就表示 60 秒。那这个 sample count 什么意思？就表示你把这个 60 秒分成几个窗口。说白了，我把它分成六个窗口可不可以？那一个窗口是多长时间呢？一个窗口，每个窗口不就是 10 秒吗？好，就是说前面两个参数乘起来就等于它的总窗口以 60 秒为一个时间周期。我去计算这个窗口的跨度他就帮你这么去做。那不信，我们来看一看它就代码就知道了。


你看它最核心的就是在这初始化的时候，我们刚才说了 sum count 如果等于 6 的话，然后 interval 这个总窗口如果是 60 秒的话，你看他怎么去做的对不对？这是6，这是 60 秒他做的方式，这都是 assess 就是做判断的。你看这个总窗口除以这个 sample cup 就是 60 除以 6 等于多少 Windows 每个窗口就 10 秒。 OK 然后，把它赋值。然后最后把它去创建一个叫做 atonic reference array 上不看的放进去。就是说我现在有 6 个窗口，就每一个小窗口是 10 秒钟，就是一个元素周期，总窗口是 60 秒。你可以参考什么呢？你可以参考我们之前所看到那个滑梢。在这我都按照他这个来好了，比如说现在我是 1000 毫秒1000，然后我把它分成了 5 个窗口，那每个窗口肯定是 200 毫秒。 OK 就这么回事，那 1000 除以5，这个 Windows nice in minutes 就等于 200 了。然后在这里同学们请看它把它整个这个模型抽象成了我们的 Java 的一个数组，只不过它变成一个原子的 reference array 那也就是说我们现在有一个数组，这个数组它一共里边就有五个元素，分别是 0 到 200 到400，400到 600 到 800 以及 800 到1000。


好了，然后我要针对于每一个小窗口我进行统计。那怎么去统计的？你会看到它除了有这几个核心参数以外，还有一个就是 update lock 这个 update lock 主要是做悲观锁做锁的。那其实我们可以看到这里边还有一些具体的细节，比如说 current window 怎么去获取？当前窗口它有一个 time util 就 time util 是单线程去实现了一个唯一的这个时间。我们看 time util 里面很简单，就是一个单线程，然后每次都会去获取单线程中的实践。他这么做的目的是为了干什么。所以你想一想就是为了单个应用中这个时间，我要是唯一准确的就是所有的时间都是从一个线程里边去获取当前的时间，他就这么去来，所以说他有一个 time mute 当然它也是一个被沃利泰修饰看到了。那这个逻辑就是每次都是获取当前时间，每次修炼 1 毫秒获取当前时间。好了，那既然是这样的话，那我们获取当前时间，根据当前时间得到当前窗口，它到底是哪一个？它每次都是拿当前时间，然后获取当前窗口返回的就是一个叫做 window wrapper 这个 window wrapper 就是很简单当前的窗口，它的这个总的时长，因为我们之前用的是这个 200 毫秒为一个窗口，所以说它的总时长就是 200 毫秒。然后它这个时长开始走到这个窗口的起始时间是什么？然后这个 T 叫做 static state 就是完全做统计分析的。这个里边就是我把窗口里边从我窗口开始的记录时间以及我窗口的总时长。然后还有我在这个窗口内我要统计什么信息，它都是放到这个 static state 里边了。好了，然后我们再往下看。
接下来这东西怎么去取到当前窗口呢？其实它里面有一个非常简单的公式，你会看到了它就做一个取鱼的很简单很精巧的一个操作，就是拿这个 cataler time idx 拿索引去做的，他把当前时间传进来，然后走到这个取到当前时间的索引。当前时间索引要么你就取6，要么是等于01234，因为一共就 5 个，这方法怎么去做的，你看他直接就是拿什么呢？当前时间除以整个这个小窗口的这个什么？这是 window length 1 minuteswindow less minutes 就是小窗口是 200 毫秒，走过一个布场就是拿总的时间除以这个 200 毫秒，那取剩下那个就是一个 index 拿这个 index 再取于整个数组的长度。


当前我取余过来的时间，在我的这个数组中，数组的下标到底是哪个？它直接取出下标了。看见了吧。他取出来下标之后，然后怎么做？在下面他就直接从数组里面取出来当前下标所对应的这个窗口，然后判断这个窗口是不是等于空。如果等于空的话，他干什么？他去用 CS 给他弄出来，然后如果不行的话干什么？我就是做 eo 的线程的让步，这个线程 CS 不行了，那我就换另外一个线程去做。


总之就是这么一个循环的过程，其实它这里边说的非常清楚，假设说我的前面的那个 0 到 200 走完了，那我后面是不是得增加一小块，那我就把之前的删掉，把后面的 1000 到 1200 的这一块加上。然后当前我如果 time 是888，那我肯定是在这个里边。如果这个里边为空的话，那我要把它弄出来，把它弄出来之后我还要干什么？这是一个 compare 操作看见了吗？如果我期望它是一个空，并且它也确实是空的话，那我就把它这个新的对象给它设置到这里边，这是一个 CS 操作。好这是 old 的情况。然后如果 else if 当前的时间它等于 oldstart 是什么意思？就证明当前的这个 start 时间就是我窗口开启的时间跟你当前窗口开启时间相等，那说明我这个数组里边是有这个窗口的，所以我直接返回 word 就可以了。


else 的情况，else情况就是如果当前的 start 开始时间大于 old 的时间。那这个时候说明什么？说明我要往后面新加窗口了。我当前的这个窗口起始时间已经大于最大的窗口的 old 的开始时间了，那我一定要往后面去新加。那我新加我怎么去做呢？同学们请看。


比如说我新加我要做的事情很简单，它这里边用一个悲观锁，为什么要用悲观锁呢？也就是说 atomic refers 本身来讲就是原子性的，你为什么要做这个事情呢？因为其实他做的是一个复合性操作。他做了哪一个复合性操作呢？你会看到 successfully get the update log 然后 no we reset the bucket 什么意思？你就看这个方法里边做了什么事情就好了。点进去。这个方法它是一个抽象的 abstract 叫做 reset window to 方法。然后其实正常来讲，大家去使用的时候都使用了这个叫做 bucket lift ray 巴克特利特尔瑞。他做的事情其实做了两件事情。


第一件事情是我新的时间传进来，新的时间传进来之后，我要把窗口做一个重置，这是一步操作。然后我还要把当前的 y6 做一个重置，就是窗口的起始时间给它重新赋值。然后 value 里边的这个统计分析的内容，我要重新做一个控制。那刚才老师说了，那这个 window VIP 它是我们整个利普尔瑞里边每一个元素，window VIP 里边就那几个属性。刚才我们看到了一个是步长，还有一个是这个窗口起始的时间以及 T 这个 T 就是实际统计的数据。那所以刚才我们真正去做 reset window to 的时候，第一步改变步长，第二步把里边之前统计的数量都清空，那这两个操作是一个。复合性操作你在并发的时候你要保证一个原子性，那你必须要加锁。所以说我们对于这个复合性操作这里边是用一个锁去控制的，看见了。


最后 else if 如果小的话，他说基本上永远都不会走的，就是 should not go through here 就永远都不会走的，你不用考虑了。所以说我们具体关注一下这个方法，看看里边的参数是什么。我们来看一下这个 window viper 里边它有个泛型是不是刚才我们看到这泛型 T 就是我们去统计的东西，我们统计的东西到底是啥？我们来看一看统计的东西，就是一个叫做 metric bucket 这个 metric bucket 这里边有一个数组用一个 line either 实现的，大家对于 line either 熟悉吗？这个 line either 这个东西，说白了它是一个 atomic 浪的一个升级版，用于做这个在高并发的情况下，它的性能会比这个阿托米克浪还要好得多。


如果小伙伴们有兴趣的话，可以看看这个浪埃的底层的实现，就是道格里在 1.8 之后新加的做技术的一个性能更好的一个这个技术器。冷爱的可以看一下，它本质上就是开始是一个技术的，然后我把它分成多个 care 最后进行就是 get 值的时候，它其实做一个 sum 操作，所以我就不做过多赘述了，你可以把它认为是一个阿汤米克浪就可以了。暂时这么认为你只需要知道他是一个更高性能的阿汤米克浪。


然后我对这里边做一个指标的统计，我统计好多种指标，所以说是一个什么呢？是一个这个康特斯。然后这里面我初始化的时候，我先初始化了一个叫做 metric event 的 values 这个是一个枚举类，他说通过的请求数、阻塞的请求数、异常数，还有成功的请求数响应时间，还有一个 accounting pass 等等。那我们看，他把这几个都当成我要统计的指标了，他把这几个负循环，然后从 0 开始，每一个指标都把它对应了一个什么一个狼爱的对象了，然后做每一种指标的统计。对每一种指标，比如说对他的这个加1，减 1 pass ，他都会去做各种各样的统计。你会看到这里边，说白了就是对那几种指标的一个技术。所以说这个 metric bucket 它就是一个技术桶对象，做一次封装。


那我们再回过头来，你会发现那这个 window VIP 里面存的东西到底是什么呢？说白了，就是我们刚才说的整个这个窗口的小窗口的步长，假设说它是 200 毫秒，然后这个就是当前窗口的起始时间，这个当前窗口起始时间肯定是 time step 时间戳。当前窗口的起始时间比如说是一个时间，然后它再加上 200 毫秒，是不是这个窗口就过期了？这窗口过期了之后是不是时间再往前走？就是我的统计分析是需要进入到下一个窗口了。就这么一个意思。然后这个元素的意思就是说在这个 200 毫秒的时间窗口内，我各项指标到底 qpstpsrtblocking 到底每一个指标是什么样子？这就是一个统计数字集合对象。然后它的底层刚才我们看到了就是我们的这个叫做 metric bucket 好了，那整体上来讲，已经把我们的 santa 哨兵他的最核心的这一个部分分析完了。那我期望小伙伴们对这个哨兵他的核心的机制应该有一个初步的了解。后面感兴趣的话可以跟老师一起去讨论，去交流它的这个 sentence 里面的核心代码，包括它的这种滑床实现，我没有去特别详细去讲。当然老师在这里只是起到一个这个抛砖引玉的这么一个过程。


具体的细节，我们的课上可能时间没有那么多，我只是想通过这次源码课程跟小伙伴们去分享一下哨兵，让小伙伴们在今后阅读哨兵的时候起码对他原来感兴趣，这样的话你才能够更好的去使用好这个哨兵。Ok.那么这节课我们先讲到这，感谢小伙伴们收看。


