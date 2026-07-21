---
title: 1-12 哨兵核心源码主流程分析-2
---

# 1-12 哨兵核心源码主流程分析-2

[image](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/08e10d43-4f5c-4eec-af04-a81c9e34c086/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667T6MSSYR%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T225834Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCICRR%2BAqi5YFfrL7Ss5iJlSBgGuI9VstBzUO4xoRRuIPRAiAfhq%2B1PT5J%2BxDsI9aCHTGWhlsp4wC07cX85Ze8gIZKUiqIBAjG%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMYuuVzIOVkuCBtMFjKtwDQRt%2B1Ptp9lRFtQjSZREjYtMhWS%2BcC1GPMWC6c1hjg0XsJxXggXyBFtD51ZgHH2X4hffBBR1G5JII44zJzSCiAAKNwn1IiaOlB44APc9R%2F143XiYMaoXVA7XRuW%2F7HB4fBSVFdN%2BbKxeQtj%2BdsldX%2BAOcGNBZqtOt6tFYcpZZCiPWJKpRLbyru26HfpYLpg01Zuqh0XM%2BCOOFysJ3dmJV9rpSW1AYpSzUtU4bP0PMgJhmW%2BwIvkbQOpTDWjJqXq%2FkyNcsY%2F5SZzFd4gne0Bd6GFRgsGOazti57Da%2Fuhbx3Z6IpbZfWwnjY2FF8z3dKBoHnFUJZAg9hSWLQQHdF6eOrcW2c%2BXZYH4iPIHrYvnfbKJeD%2F2Tum8FuCWPpc0whE%2B4Pb%2FYxJLcWJvzgIvLEhdDM9%2B5G%2BkWR2Vk3MObhfOt5f1AHjKqBp2VvfQc5lmbtuajquUmXnxL31a4vipLo8VNlheW7BWp7VigtnBaeOsKoSefspokQ%2BeL10oJasqgqmvuQu46c5Pgv3JrCFg3Y6xJtXDYIf9zFBwn0O0V3Dak77T4GsVlx7QRfRJ8MqKLmzXuN9LYizsAE6VRSbQrI6%2BUeRyQFjm%2F2zscFHV59ctCeMxX7pTPKU%2Fm%2BihGfnwwrrr%2F0gY6pgEXPg0lHJ83ebZLBLmkl7WZl2fHs4NXsN0er62HLEvrh94GDv4plEnO1undbguib2BMtSmXYnCZEKmNN19FuYGK7L0a8fSPaYGdHdoRXcjc7uyBiaEOv6GehC9nsuqNXiYjDN3mGC6e9E4pfePx3Mr%2FYJ37nH8E%2FJnssOxqBlVOXeefjpry3Izf%2Bqi0o%2FlvDVb3dqmMt4%2BzcKtuPrd60jgi%2BfjdpV%2Fn&X-Amz-Signature=5d7056242bd4630a3183ed9051ac1f104f23fa774efdd5a93fab97935a49ec99&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

[image](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/84a03dad-7643-468a-adff-c14c085ba24e/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667T6MSSYR%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T225834Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCICRR%2BAqi5YFfrL7Ss5iJlSBgGuI9VstBzUO4xoRRuIPRAiAfhq%2B1PT5J%2BxDsI9aCHTGWhlsp4wC07cX85Ze8gIZKUiqIBAjG%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMYuuVzIOVkuCBtMFjKtwDQRt%2B1Ptp9lRFtQjSZREjYtMhWS%2BcC1GPMWC6c1hjg0XsJxXggXyBFtD51ZgHH2X4hffBBR1G5JII44zJzSCiAAKNwn1IiaOlB44APc9R%2F143XiYMaoXVA7XRuW%2F7HB4fBSVFdN%2BbKxeQtj%2BdsldX%2BAOcGNBZqtOt6tFYcpZZCiPWJKpRLbyru26HfpYLpg01Zuqh0XM%2BCOOFysJ3dmJV9rpSW1AYpSzUtU4bP0PMgJhmW%2BwIvkbQOpTDWjJqXq%2FkyNcsY%2F5SZzFd4gne0Bd6GFRgsGOazti57Da%2Fuhbx3Z6IpbZfWwnjY2FF8z3dKBoHnFUJZAg9hSWLQQHdF6eOrcW2c%2BXZYH4iPIHrYvnfbKJeD%2F2Tum8FuCWPpc0whE%2B4Pb%2FYxJLcWJvzgIvLEhdDM9%2B5G%2BkWR2Vk3MObhfOt5f1AHjKqBp2VvfQc5lmbtuajquUmXnxL31a4vipLo8VNlheW7BWp7VigtnBaeOsKoSefspokQ%2BeL10oJasqgqmvuQu46c5Pgv3JrCFg3Y6xJtXDYIf9zFBwn0O0V3Dak77T4GsVlx7QRfRJ8MqKLmzXuN9LYizsAE6VRSbQrI6%2BUeRyQFjm%2F2zscFHV59ctCeMxX7pTPKU%2Fm%2BihGfnwwrrr%2F0gY6pgEXPg0lHJ83ebZLBLmkl7WZl2fHs4NXsN0er62HLEvrh94GDv4plEnO1undbguib2BMtSmXYnCZEKmNN19FuYGK7L0a8fSPaYGdHdoRXcjc7uyBiaEOv6GehC9nsuqNXiYjDN3mGC6e9E4pfePx3Mr%2FYJ37nH8E%2FJnssOxqBlVOXeefjpry3Izf%2Bqi0o%2FlvDVb3dqmMt4%2BzcKtuPrd60jgi%2BfjdpV%2Fn&X-Amz-Signature=1cc75b98d01a01b724b8fb7987433ad2eb275a7840adefc0ddde6534a659c3aa&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

那主要就是说 context 他去获取我们的这个上下文的 context context util 的 get context 如果说这个 context 他 instance of long context 他说 16 init 的 entry only not rule attack will be done 就是说我只是初始化这个 entry 但是我并不做任何的这个规则检查。就是说当我们的 context 这个上下文超过一个限制的，它这个限制多大是2000。其实小伙伴们你感兴趣的话可以跟一跟这个里边的代码，它里边有一个限制。


当然这个上下文肯定是一个 slide local 就是一个 slide local holder 然后这个 slide local 它的限制你要去找这个叫做 to enter 最初 enter 它是从上下文里边去获取这个 context context 如果等于空的话，帮你去 new 出来一个。


当然 new 的前提是什么呢？ new 的前提是你一个 node 必须等于空，并且你不能超过它的限制。它有两个限制，一个是 max count context size 这个最大的是2000。 OK 然后还有一个限制就是 slot chat 这个是在后面做限制的，我们不去说了。 OK 我们继续回过来。就是说如果你的 context 不超过限制的话，那你就可以正常去做。但是如果你超过了限制，那我只把这个鹌鹑 new 出来，但是我不做任何规则检查，就直接 return 了，这个方法直接 return 了之后，后面逻辑都不走了对吧？那很明显，规则检查肯定是在后面的逻辑去走的，我们继续往下看。

```shell
private Entry entryWithPriority(ResourceWrapper resourceWrapper, int count, boolean prioritized, Object... args)
        throws BlockException {
        Context context = ContextUtil.getContext();
        if (context instanceof NullContext) {
            // The {@link NullContext} indicates that the amount of context has exceeded the threshold,
            // so here init the entry only. No rule checking will be done.
            return new CtEntry(resourceWrapper, null, context);
        }

        if (context == null) {
            // Using default context.
            context = InternalContextUtil.internalEnter(Constants.CONTEXT_DEFAULT_NAME);
        }

        // Global switch is close, no rule checking will do.
        if (!Constants.ON) {
            return new CtEntry(resourceWrapper, null, context);
        }

        ProcessorSlot<Object> chain = lookProcessChain(resourceWrapper);

        /*
         * Means amount of resources (slot chain) exceeds {@link Constants.MAX_SLOT_CHAIN_SIZE},
         * so no rule checking will be done.
         */
        if (chain == null) {
            return new CtEntry(resourceWrapper, null, context);
        }

        Entry e = new CtEntry(resourceWrapper, chain, context);
        try {
            chain.entry(context, resourceWrapper, null, count, prioritized, args);
        } catch (BlockException e1) {
            e.exit(count, args);
            throw e1;
        } catch (Throwable e1) {
            // This should not happen, unless there are errors existing in Sentinel internal.
            RecordLog.info("Sentinel unexpected exception", e1);
        }
        return e;
    }
```


第二个，if他说 context 等于空，但如果说我在这取出来 context 并且 context 还是个空，怎么办呢？那我也是一样的，use default context 就是 my context [youtube.my](http://youtube.my/) entry 然后他使用他自己的再往下看。
这里面有个 global 的 switch is close 就是说有一个全局的开关。这个全局开关如果关掉了，那我也不做任何规则的检查。这里面 on 就是开着的，这肯定是一个布尔类型对吧，我们点进去看一下。这个里面有一个 public static volletel volatile 声明的这个布尔类型的 on 去开关。他说的 global switch for sentence 就是说一个全局的哨兵的开关。为什么这里边用 volatile 很简单，因为多线程会去访问修改这个布尔类型的 on 或者是其他的 off 这个字段对吧？如果它等于 false 的法证明关掉了，关掉了就是所有都不做流程检查了。


Ok.所以说其实小伙伴们你在实际的工作中怎么去使用这个 water 就看别人源码里边怎么去用的，你要学着点看看怎么用。 OK 这样往下看，回过来开关我们肯定是开着的对吧，除非你把它手工关掉，然后再往下看。这里边有一个非常非常重要的方法叫做 look process chain 字面意义上就是去循环 process chain 最终拿到了一个 chan 这个 chan 它的接口是 processor slot 拿到了这个东西之后，我做什么事情呢？我说判断如果等于空的话也是一样的，我就不做任何规则检查。如果拿到了怎么办？我在这里边做的方式就是说我去 entry.ct entry 就相当于真正去拗出来一个 entry 当然这个 CT entry 是一个子类了，然后用 entry 这个类去用 chan.entry 这个方法去进行调用，调用完了之后最后返回抛异常的时候就退出。 OK 这个代码就是最核心。


好这个代码到底是什么意思呢？我们先看一看这个鹌鹑，我们可以去记一下，看到它是一个抽象的，你看到了吗？

[image](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/21a540d6-eed0-4a90-abab-67433d330656/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667T6MSSYR%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T225834Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCICRR%2BAqi5YFfrL7Ss5iJlSBgGuI9VstBzUO4xoRRuIPRAiAfhq%2B1PT5J%2BxDsI9aCHTGWhlsp4wC07cX85Ze8gIZKUiqIBAjG%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMYuuVzIOVkuCBtMFjKtwDQRt%2B1Ptp9lRFtQjSZREjYtMhWS%2BcC1GPMWC6c1hjg0XsJxXggXyBFtD51ZgHH2X4hffBBR1G5JII44zJzSCiAAKNwn1IiaOlB44APc9R%2F143XiYMaoXVA7XRuW%2F7HB4fBSVFdN%2BbKxeQtj%2BdsldX%2BAOcGNBZqtOt6tFYcpZZCiPWJKpRLbyru26HfpYLpg01Zuqh0XM%2BCOOFysJ3dmJV9rpSW1AYpSzUtU4bP0PMgJhmW%2BwIvkbQOpTDWjJqXq%2FkyNcsY%2F5SZzFd4gne0Bd6GFRgsGOazti57Da%2Fuhbx3Z6IpbZfWwnjY2FF8z3dKBoHnFUJZAg9hSWLQQHdF6eOrcW2c%2BXZYH4iPIHrYvnfbKJeD%2F2Tum8FuCWPpc0whE%2B4Pb%2FYxJLcWJvzgIvLEhdDM9%2B5G%2BkWR2Vk3MObhfOt5f1AHjKqBp2VvfQc5lmbtuajquUmXnxL31a4vipLo8VNlheW7BWp7VigtnBaeOsKoSefspokQ%2BeL10oJasqgqmvuQu46c5Pgv3JrCFg3Y6xJtXDYIf9zFBwn0O0V3Dak77T4GsVlx7QRfRJ8MqKLmzXuN9LYizsAE6VRSbQrI6%2BUeRyQFjm%2F2zscFHV59ctCeMxX7pTPKU%2Fm%2BihGfnwwrrr%2F0gY6pgEXPg0lHJ83ebZLBLmkl7WZl2fHs4NXsN0er62HLEvrh94GDv4plEnO1undbguib2BMtSmXYnCZEKmNN19FuYGK7L0a8fSPaYGdHdoRXcjc7uyBiaEOv6GehC9nsuqNXiYjDN3mGC6e9E4pfePx3Mr%2FYJ37nH8E%2FJnssOxqBlVOXeefjpry3Izf%2Bqi0o%2FlvDVb3dqmMt4%2BzcKtuPrd60jgi%2BfjdpV%2Fn&X-Amz-Signature=20e6aa8876ec7362b726b21c7bd60fe073949e8690da9bd91b41338002ceb70b&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

这个东西它返回的是一个接口，叫做 processor slot 接口。谁调的鹌鹑肯定是这个接口。下面具体的时间类调的明确这有多少个时间类？同学们请看，比如说 author 类 slots close the builder slot degrade slot demo slot follow slot get away follow slot log slot 还有 must block slot 以及 node selector slot 以及 paramefollow slot 后面还有很多比如说 statics slot system slot 这些东西都是什么？这些东西就是我们之前所看到的这一堆的 slot 这一堆的 slot 都放到了一个数据结构里面，这个数据结构叫什么？这个数据结构就叫做 slot chan。

[image](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/35695ecf-deb0-4def-95c6-393ec6dba52d/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667T6MSSYR%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T225834Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCICRR%2BAqi5YFfrL7Ss5iJlSBgGuI9VstBzUO4xoRRuIPRAiAfhq%2B1PT5J%2BxDsI9aCHTGWhlsp4wC07cX85Ze8gIZKUiqIBAjG%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMYuuVzIOVkuCBtMFjKtwDQRt%2B1Ptp9lRFtQjSZREjYtMhWS%2BcC1GPMWC6c1hjg0XsJxXggXyBFtD51ZgHH2X4hffBBR1G5JII44zJzSCiAAKNwn1IiaOlB44APc9R%2F143XiYMaoXVA7XRuW%2F7HB4fBSVFdN%2BbKxeQtj%2BdsldX%2BAOcGNBZqtOt6tFYcpZZCiPWJKpRLbyru26HfpYLpg01Zuqh0XM%2BCOOFysJ3dmJV9rpSW1AYpSzUtU4bP0PMgJhmW%2BwIvkbQOpTDWjJqXq%2FkyNcsY%2F5SZzFd4gne0Bd6GFRgsGOazti57Da%2Fuhbx3Z6IpbZfWwnjY2FF8z3dKBoHnFUJZAg9hSWLQQHdF6eOrcW2c%2BXZYH4iPIHrYvnfbKJeD%2F2Tum8FuCWPpc0whE%2B4Pb%2FYxJLcWJvzgIvLEhdDM9%2B5G%2BkWR2Vk3MObhfOt5f1AHjKqBp2VvfQc5lmbtuajquUmXnxL31a4vipLo8VNlheW7BWp7VigtnBaeOsKoSefspokQ%2BeL10oJasqgqmvuQu46c5Pgv3JrCFg3Y6xJtXDYIf9zFBwn0O0V3Dak77T4GsVlx7QRfRJ8MqKLmzXuN9LYizsAE6VRSbQrI6%2BUeRyQFjm%2F2zscFHV59ctCeMxX7pTPKU%2Fm%2BihGfnwwrrr%2F0gY6pgEXPg0lHJ83ebZLBLmkl7WZl2fHs4NXsN0er62HLEvrh94GDv4plEnO1undbguib2BMtSmXYnCZEKmNN19FuYGK7L0a8fSPaYGdHdoRXcjc7uyBiaEOv6GehC9nsuqNXiYjDN3mGC6e9E4pfePx3Mr%2FYJ37nH8E%2FJnssOxqBlVOXeefjpry3Izf%2Bqi0o%2FlvDVb3dqmMt4%2BzcKtuPrd60jgi%2BfjdpV%2Fn&X-Amz-Signature=ebe84ce1da22ef97bc02c37e1cfba78d89fa387b0561a5d150101c29caad0e22&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

Ok.如果这个 slot chain 没有，那对应着 ruler 就没有作用，能理解说意思吗？我如果没有 slot 的话，那我要不就有什么用呢？所以这代码说得很明确对吧？就是说如果你的这个 slot 是空，说白了就是你这个 chan 是空，那我就不需要规则，那规则没有意义。


那我们重点来看一看吧，这个东西到底是怎么去实现的？我们先不用去太关注这个 entry 你先看一看这个 look process chan 查找俄罗斯的 chan 能不能找到这个 chan 能找到这个 chan 并且它有值肯定会执行鹌鹑，这个鹌鹑就是一个一个的去处罚，这个就有点像我们的这个怎么说一种面试的这种驱动调用的模式。


好看一下这个 look process chan 怎么去做的，把资源传进去对吧，我们点进来看，这个还是在 C TS PH 这个类里边有一个 protected 的方法，它返回的是一个 process slot 对吧。 OK 叫做 look process chan 然后怎么做？他说先从这个 map 里边去取就是这个 chan map 那这个 chan map 是什么东西？我们点进去看，它是一个 private static volatile 声明的一个 map 并且这个 map 它是一个哈希 map 好，现在问题就来了一个 map 你为什么用 volletal 修饰啊？如果说大家对于 Java 基础比较不错的话，你就会想这个问题，就是我 map 这个东西本身就是一个存储，要么 put 要么 remove 要么去 be effect 就是添加和修改元素，删除元素。
我一个 map 有必要去用 wallet 修饰吗？既然这么修饰，那肯定是有它的意义，意义何在呢？那现在我想问你个问题，如果说两个线程去访问同一个集合，无论是 list 还是 map 去访问这个集合。比如说我第一时间往 map 里面 put 一个元素，然后另外一个线程去拿，这个元素能不能拿到肯定能拿到。我去删除一个元素，另外一个去循环能不能拿到肯定也能拿到。因为这种 map 的这种 put 就是增删改，这种操作肯定都是纪实性的，割线程都可见。


为什么你还要声明一个 what time 咱们带着这个问题回过头来再看那个方法。在这里先从缓存里去取，看看对应的这个 resource VIP 之则它有没有一个资源的链条，就是我们的 process slot chan 这个链条如果没有的话，那我就创建。当然这种创建的写法看到了吗？他是怎么去做的？首先判断为空，然后加锁，加锁完了之后再从缓存里去取，然后判断是否为空。对吧，两次判断中间加锁。这种方式就是一个典型的 double check 的方式，用于高并发音的下面去做数据的一致性。 OK 所以说小伙伴们在去读源码的时候，其实你能 get 到很多优秀的写法，在你自己实际的工作中，你把它尝试应用起来，慢慢的你用习惯了，那你也就成为高手。


好了，我们不做过多废话了，他这种 double check 的方式从 map 里面去检查到底有没有这个 process check 。如果说还是等于空的话怎么办？他做一个限制，他说 entry size limit 到底超不超过上限。再往下看。在这里边有一个类叫做 slot chan provider 然后点 new 一个 slot chan 把这个 chan 如果，确实等于空，也没超过上限，把它弄出来，把它救出来之后给它 put 到我的新的 map 里面，就是用一个转换的角色。这个 map 是一个 template 的角色，是一个临时的 template 就是相当于把 new map 我加完的这个缓存里的 map 给它 put 倒进去，然后再 put 倒进去。


我当前的这个 chat 它也 put 到这个 new map 里，然后把它们两个引用再转换一下，把老的静态的这个 walle tell 的这个引用指向这个 new map 对吧？那这种形式首先第一点，引用发生改变的时候，其实也没有必要用到了 tell 就我之前这个 chan map 它的引用是谁呢？最开始他实际 new 这个对象的时候，我这里面已经初始化了，就是一个哈希 map 现在我把它的这个引用指向一个新的 map 多线程之间肯定也是及时感知的。对不对？所以说你在这里用 water 其实说白了也没有意义。


那到底这个 volcano 的含义在哪里呢？注意就在这里，这句话叫做欠 map.size 当你去判断这个 map.size 的时候，因为我是通过这个 map.size 看看它超没超过我的阈值，这个是6000。我们之前看到了就是说你 slot chan 最大的 size 是6000，如果超过 6000 的话，我就 RE 寸空对吧。那这种东西，多线程并发来的时候可能会出现这种超过极限的情况。那么你就必须要用 want 修饰一下这个脉，原因是因为你要访问里边的再次属性。 OK 好了，这是一点非常关键的。所以说在这里你又 get 到了这个 wallet 怎么去用以及又 get 到了这种 double check 的方式对吧？所以说通过读这么一小段带，你就收获了两个小知识点。


再往下看，它就是一个转换最关键的这个 new stop chan 这个代码，它是帮我真正创建一个 chat 出来。那这个 chan 到底怎么去创建呢？你要看 slow 的 chat provider 了点去这个 new slow chat 这个 new slow chat 他怎么去做的？他说如果 build 不等于空的话，我就 build build 出来，返回。我做了一个叫做 reserver slot charm builder 做什么呢？我们先不用去管他。如果说 build 还等于空的话，那我去 new 出了一个 default builder 出来之后， build.build 返回。整个这个逻辑就是帮我去创建一个slot ，那帮我去创建 slot chat 有个前提什么呢？是我到底应该用哪个 slot chat 我们来看一看这个 Resso chat 做了什么事情。好，我们把这个左侧数打开。


同学们请看这个 reserver slow time builder 它首先有一个 list 元素 list 列表，然后有一个孩子 other 电量是不是默认是 false 然后这里边他帮我去 loader build 对象看见了吧。这个 loader 是什么？看这个 service loader 那这个 service loader 是什么呢？我们看一看这个 service loader 就是 service loader.load slot builder 这个是一个什么？这明显是一个 SPI 的加载。


如果说小伙伴们对 SPI 熟悉的话，你肯定第一眼就知道了这个 SPI 它去加载这个接口下面的实现类，它到底有多少个帮我去初始化注入进来。那这个就是我们可以看到了，它就是一个接口，SPI叫做 store chan build 它里边有一个 build 方法返回一个 processor chain 那这个 SPI 其实我们通过号包下，它一定有对应的扩展点。我们看在 resource 下有一个 mate info 这样你看有个 service 对吧？在 service 里边我们看到 com 阿里巴巴，点 csp.sentence.slow chen.slow chen build 点看到了吗？这个类对吧？所以说看到这个类了，那你就明白了，这个它就是作为一个扩展点可以动态去改的。它默认的实现是什么呢？默认的实现是 default builder。
Ok.那如果你想自己去扩展，是不是也可以去扩展没问题，因为什么呢？因为我们自己之前 orwell 的时候我们看到了这个东西，我们可以自己家这个扩展点，自己家自己的这个槽是吧，然后我们再回过头来，这里面说的是什么回事？我们把这个关掉，还回到这个 provider 这个 provider 我们看到了它用 SPI 的方式去加载这个 slot builder 他说 slot builder 如果点 get class 如果不等于 default slot chain builder 的话，就相当于他不用我自己的。因为 default slot builder 不就是我 SB I 扩展点里面默认的那个实现，就是 default slot builder 就默认的实现。


如果你不用默认的实现的话，那我怎么去做的？那我在这里边就是说还是 other 等于 true 就是说你用其他的我给你是整处。然后把所有加载过来的 builder 全都装到一个 list 里边。就刚才所说明那个 list 然后 has other 那我就取第 0 个看见了吗？就取 list 中第一个，假设说你这突然点里面有比如说 default EE 就是你自己定义的，比如说 my slot chan 比如说举个例子，有一个 my 1 slot chain builder 然后有一个 my 2 slot builder 那不两个对不对？然后他进行扩展点加载的时候，他把这个 my 1 跟 my 2 都放到这个集合里了，但是他取的时候他只取第一个。


OK 在这里小伙伴我们要注意一下我们的还原。好好的还原之后，我们回过头来，他取第零了之后就是孩子阿拉基本等于数了，然后就返回了没了。如果说你没有用自己的，那就是 else 孩子阿拉肯定等于 false 对不对？等于 false 的话就会 new 一个 default style 出来。然后把 build 对象返回，就这么一个简单的逻辑。 Ok. 好了，那这里边非就是去解析到底是用你自己的扩展点，还是用人家哨兵给你提供的默认扩展点，是这么一个非常简单的游戏。


好，再往下，解析完了之后判断 build 是否为空，因为这个 build 它是一个静态的赋值的过程。对吧，肯定是静态的一个属性。你看它是一个 private static volleyta 叫做 stop builderok 当然这里面加 voltail 关键字，它多线程可能会发生引用的这个改变。 Ok. 然后这里边如果还等于空，那我就再帮你去用一下。然后他打一个 warning 他说 slot chan provider 然后叫做 wrong states when receive a slot chain builder using depot 这啥意思。本身来讲我在 reserver 的时候，我其实就应该能够帮你正确的去做到能够去 new 出来。


这个 builder 是底部特斯拉陈 builder 但是如果我解析出来失败了，那就证明也没。取出来 get 0 的时候，它竟然是一个空都有可能。他说如果还等于空，那怎么办？他说证明你在做解析的时候， receiving slot build 的时候出错了。那我会帮你说 use default ，这是他自己做了一个兜底，其实没有什么必要，还是 new 出来一个 default stop chan builder 跟下面这个代码一样的。 OK 整个这个逻辑 new stop chan 就完事了。


那我们看一看 new star chan 这个东西，最后就返回了，他调用 build 方法就返回了这个 process chan 那我们看一看这个 build 方法它做了什么，或者是说它这个 default slot.build 方法，我们点到这个类里面看一下，这里面就一个被 all right 被负载的一个这个 build 方法，它 implements builder 对吧，这里边很简单。
首先初始化了一个 processor chain 这是一个接口，它用到的是一个 default process 这个 default process chain 之后它 add last at last at last at last at last 最后是降级。第一个是什么呢？就在 node selector slot 然后是 cluster slot 然后是 lock slot statics slot system slot 还有 outlet follows lot degree slotok 那这个它是一个链条，它也有 at first 也是一个双链表。只不过我们用的时候可能用其中一个把 add last 就好，它把所有的槽都扔到这个 slot chan 里。那我们来分析一下这个 default slot chat 它到底是一个什么东西。


default slot chat 我们点进去，这个 default 我们点到 sentence 源码的这个里边了 store chan 里了。 Ok. 然后我最大化它有一个层次结构，它的父类 exist success 然后这个 process slow chat 它是一个 abstract 抽象的，然后它帮我实现了 add last 跟 add first 对吧？那我的负例肯定是没有这两个方法。
所以说我的 abstract linked process slot 的话，那你看到这个单词是不是 abstract 抽象的 linked 链表形式的 processor slot 对吧？ OK 我们点进去它，那你会看到它在网上还有一个分类，就是我们的 process slot process lot 有哪些方法呢？我们看这个 interface 这个 interface 里边算形式，一个 T 里边是一个 entry 方法，这个 entry 就是一个触发的动作， entries of this slot 就触发当前的 slot 然后还有一个叫做 fire entry 对不对？表示 care 我。然后这里边有 exist 退出，还有一个 fair exist 群发退出。 OK 它实现了这四个方法。它的子类是谁呢？我们来看一下它的结构，它的子类是 abstract link 的 processor slot 它是一个抽象的链表形式的程序的槽，我们看到它里边有一个 next 属性对吧，这种明显是一个链表。然然后我怎么去处罚 entry 也就处罚下一个。如果下一个不等于空的话，我去调下一个方法的 transfer entry 方法。然后这个 transfer 做什么事情呢？我们点进去就是它调 entry 那这个 entry 又是什么呢？这个 entry 回过头来发现它又是最负类的一个 process slot 的安全方法。说白了就是我们所有的 slot 都应该实现，这个接口都应该重写这个安全方法和 fire 安全方法，以及 exist 和 fire exist 方法这么一个事。


好了，说白了，我们回过头来，它的触发的逻辑就是以链表的形式去判断下一个有没有有的话，就是调下一个元素的安全方法去做处罚就好了。同理 exist 也是一样的，你知道它是一个链表了。那你再看它的子类，它的子类其实就是它了。对不对？就是 abstract link 的 processor 它的子类就是我们的 process chat 他说我给这个抽象的链表加两个方法，一个是 at first 还有一个是 at last 那这两个方法它的子链是谁呢？就是 default process slot 对吧？你看这个东西，他说 default process slot chain ，它既纯自 process slot chat 然后它里面有个 first 这个 first 表示第一个元素还帮你实现了 abstract linked process slaughter 它帮你去 new 出来了，重写了 entry 跟这个 exist 方法。 entry 方法直接是内部调用了 fair entry 触发下一个退出的方法，也是直接调用了处罚下一个退出的方法。这个东西是什么？你看到这个代码，他说 and 等于 first add first 的时候，它是做一个引用，是不是这个代码 add last 就是相当于给我加一个元素，我把它 set 成这个，然后把 and 又设置成最后的一个节点，and last 是往后添加。


那我一个链表给我加一个元素，肯定是 end.set next 对不对？当前我的链表上有三个元素，现在新加了一个元素就变成第四个元素，第三个元素的下一个元素肯定是新加的这个元素 upset next 最后我们再把 and 指成我最后那个元素就完了，就是 at first 也是一样的做一个转换。 OK 这就是一个链表操作。那这个第一个节点帮你说明出来了，这个就类似于我们的一个虚拟头节点的概念，就是在列表操作的。 OK 非常简单。那大家看完这个代码是不是已经了如指掌了？对于这个数据结构然后对这个chain ，它一个加，一个槽，一个槽一个槽往里加加。拆完了之后组成一个链表，再往回来看，我们把这都关掉，我们就找他了这个 look process chan 他最终帮我们返回了一个链表。


当我们返回链表之后，我们做什么事情？同学们请看直接我们做的是拿到 chan 如果 chan 不等于空，直接调他的 entry 默认来讲它会调 6 abstract lift processor slot 的 first 方法。这是第一个对吧，因为我们刚才看到了 default processor chat 它就是相当于我触发安驰的时候直接触发 first 虚拟头节点，然后虚拟头节点再点到下一个节点，就是塞尔安垂触发，在安垂触发会点到 next 我第一个是一个头节点，在这里边我们来看一下。就第一个是一个头节点，头节点的下一个元素不就是我们正常真正的下一个元素，说白了就是我们在这里按照什么样的形式去装的，我们得点到这个 new 的方法里，还得回过头来，不能把直接关掉。


其实这个 default process 它里边有一个虚拟头节点对不对？它在 entry 的时候触发的就是 first.entry 然后它会调这个 fire entry fire entry 触发的时候会找到 next 节点不等于空肯定不等于空。因为我的 next 节点除了虚拟图节点以外，next节点不就是叫做 node select slot ，就是处罚它了，它里边肯定有安全方法。


我们看到是不是它里边有安全方法？它的安全方法做完了以后，它又调用菲尔安垂触发它自己的下一个节点。那它下一个节点是谁呢？就是 next 如果不等于空的话再调它，然后再调安全方法。说白了就是以链表的形式去触发下一个元素去执行，并且是一个顺序的出发。 OK 好了，那我相信小伙伴们对于这个源码应该是没有什么太大的难度了。

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


