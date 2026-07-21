---
title: 1-7 附流量控制（flow+control）文档说明
---

# 1-7 附流量控制（flow+control）文档说明

[image](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/16bda01b-4366-46b6-95b5-7ac0350634d6/SCR-20240722-pvyr.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XTLHBHTJ%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T225830Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIHTLngrsmE87Bxeh2JDZX14iT8nNgJxmV010cF5RpXO4AiA2Oscn6wv%2FOTGAeexYVarkF3ZUqW%2FsnLG6uHqcTs7SfyqIBAjG%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMrkUd8UxZAs3FZe63KtwD2desvAlotKHDGDq1Cgwmrv7PwE81g0sYzv2ehHoGoDhgW0YLsClClymEEyRymYY3joI32IcyfaOZYi1eK2rSDruEiOU49tV16pcEGQR%2BVxLA4VRsIpbGU6Sp0aEdzhW%2B33ah6GoFYqoo%2BmftHgfZ5CoFDcMXT7MjoWWrw32c66FG%2FgkHaqn%2FuZnRkeMhouhxUy0JHcQxFNve5CWhgRnQasABiwazNIr121JJMlleiiHUQke12YG7MDEXWBHTmxr2gt3xJSqid85ueTxqSfM2FQWaZVTGZddl4KqGKHgtnQHUKrKcWj30o3iJ0DY0Xm%2F7Fp43mfFb6d6J898LlFx31jULrlODYso%2BiVNAfu%2BLr9FX3egohvoobDrH5DGrp%2Bt%2Fh9rzukVMe6Ez9zyyN6M8%2BlieB2T0Kw%2FxHoGIi1HPYrpb1w6wBZB9Zm6eSba66q%2B%2FGoD%2FxtpaWZCVda7PT3NEH%2F4Gez1wUAY81IVJXVITOdFKssHlN3QuKtMzZ1JmJ0Ij6Uk5Zk9k44TCufNENTNN6BV355u8UJdqIKZUzJvOsBuAvJTFaTE2UH3IL90vjuk2dFQVcxk6GnIAVLZ3%2Bc6nVviH6uw1WMzusHOnAKTsBaJHjHwpMtBSA36X%2BS4worj%2F0gY6pgHCWjvv%2FOOLmmcL3avJ9i2x3JK1dZ94%2FZMoKWODkGkEb%2BKGc3bHiG1%2FmBIM8j%2FUgyVFx0sA5Pzn7%2BHG4WKaKXuYFSgG5E3iygDsjhL4VOLZYoFvA%2FyEe2uF%2BodPS0RH55is6RXirJQ4fUQKC3FcxMcTMG8DftdOdJfbypOfSqau6oR6eMlOcpaPJyb0WwIZNzRaqKhJt1T0D35%2FRPYhmx4%2FFFlloZvy&X-Amz-Signature=595950f22a58e849dcd4ed5f7b4754f64059b35e5a91941a93fe674544fa2710&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

[image](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/6de8f52e-8068-4fe9-8f2f-d8f5fd7f74ca/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XTLHBHTJ%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T225830Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIHTLngrsmE87Bxeh2JDZX14iT8nNgJxmV010cF5RpXO4AiA2Oscn6wv%2FOTGAeexYVarkF3ZUqW%2FsnLG6uHqcTs7SfyqIBAjG%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMrkUd8UxZAs3FZe63KtwD2desvAlotKHDGDq1Cgwmrv7PwE81g0sYzv2ehHoGoDhgW0YLsClClymEEyRymYY3joI32IcyfaOZYi1eK2rSDruEiOU49tV16pcEGQR%2BVxLA4VRsIpbGU6Sp0aEdzhW%2B33ah6GoFYqoo%2BmftHgfZ5CoFDcMXT7MjoWWrw32c66FG%2FgkHaqn%2FuZnRkeMhouhxUy0JHcQxFNve5CWhgRnQasABiwazNIr121JJMlleiiHUQke12YG7MDEXWBHTmxr2gt3xJSqid85ueTxqSfM2FQWaZVTGZddl4KqGKHgtnQHUKrKcWj30o3iJ0DY0Xm%2F7Fp43mfFb6d6J898LlFx31jULrlODYso%2BiVNAfu%2BLr9FX3egohvoobDrH5DGrp%2Bt%2Fh9rzukVMe6Ez9zyyN6M8%2BlieB2T0Kw%2FxHoGIi1HPYrpb1w6wBZB9Zm6eSba66q%2B%2FGoD%2FxtpaWZCVda7PT3NEH%2F4Gez1wUAY81IVJXVITOdFKssHlN3QuKtMzZ1JmJ0Ij6Uk5Zk9k44TCufNENTNN6BV355u8UJdqIKZUzJvOsBuAvJTFaTE2UH3IL90vjuk2dFQVcxk6GnIAVLZ3%2Bc6nVviH6uw1WMzusHOnAKTsBaJHjHwpMtBSA36X%2BS4worj%2F0gY6pgHCWjvv%2FOOLmmcL3avJ9i2x3JK1dZ94%2FZMoKWODkGkEb%2BKGc3bHiG1%2FmBIM8j%2FUgyVFx0sA5Pzn7%2BHG4WKaKXuYFSgG5E3iygDsjhL4VOLZYoFvA%2FyEe2uF%2BodPS0RH55is6RXirJQ4fUQKC3FcxMcTMG8DftdOdJfbypOfSqau6oR6eMlOcpaPJyb0WwIZNzRaqKhJt1T0D35%2FRPYhmx4%2FFFlloZvy&X-Amz-Signature=f12c8ce4b1947124c52c58d6c3700dd49282a8cda26345d00076ed5a69bdd12d&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

**概述**

流量控制（flow control），其原理是监控应用流量的 QPS 或并发线程数等指标，当达到指定的阈值时对流量进行控制，以避免被瞬时的流量高峰冲垮，从而保障应用的高可用性。FlowSlot 会根据预设的规则，结合前面 NodeSelectorSlot、ClusterNodeBuilderSlot、StatisticSlot 统计出来的实时信息进行流量控制。限流的直接表现是在执行 Entry nodeA = SphU.entry(resourceName) 的时候抛出 FlowException 异常。FlowException 是 BlockException 的子类，您可以捕捉 BlockException 来自定义被限流之后的处理逻辑。同一个资源可以创建多条限流规则。FlowSlot 会对该资源的所有限流规则依次遍历，直到有规则触发限流或者所有规则遍历完毕。一条限流规则主要由下面几个因素组成，我们可以组合这些元素来实现不同的限流效果：

```java
resource：资源名，即限流规则的作用对象

count: 限流阈值

grade: 限流阈值类型（QPS 或并发线程数）

limitApp: 流控针对的调用来源，若为 default 则不区分调用来源

strategy: 调用关系限流策略

controlBehavior: 流量控制效果（直接拒绝、Warm Up、匀速排队）
```

流量控制主要有两种统计类型，一种是统计并发线程数，另外一种则是统计 QPS。类型由 FlowRule 的 grade 字段来定义。其中，0 代表根据并发数量来限流，1 代表根据 QPS 来进行流量控制。其中线程数、QPS 值，都是由 StatisticSlot 实时统计获取的。我们可以通过下面的命令查看实时统计信息：

```java
curl http://localhost:8719/cnode?id=resourceName

输出内容格式如下：

idx id thread pass blocked success total Rt 1m-pass 1m-block 1m-all exception

2 abc647 0 46 0 46 46 1 2763 0 2763 0

其中：

thread： 代表当前处理该资源的线程数；

pass： 代表一秒内到来到的请求；

blocked： 代表一秒内被流量控制的请求数量；

success： 代表一秒内成功处理完的请求；

total： 代表到一秒内到来的请求以及被阻止的请求总和；

RT： 代表一秒内该资源的平均响应时间；

1m-pass： 则是一分钟内到来的请求；

1m-block： 则是一分钟内被阻止的请求；

1m-all： 则是一分钟内到来的请求和被阻止的请求的总和；

exception： 则是一秒内业务本身异常的总和。
```

**QPS流量控制**

当 QPS 超过某个阈值的时候，则采取措施进行流量控制。流量控制的手段包括以下几种：直接拒绝、Warm Up、匀速排队。对应 FlowRule 中的 controlBehavior 字段。

**直接拒绝**

直接拒绝（RuleConstant.CONTROL_BEHAVIOR_DEFAULT）方式是默认的流量控制方式，当QPS超过任意规则的阈值后，新的请求就会被立即拒绝，拒绝方式为抛出FlowException。这种方式适用于对系统处理能力确切已知的情况下，比如通过压测确定了系统的准确水位时。以下代码是根据官方demo修改而来，源代码参见 [FlowQpsDemo](https://github.com/alibaba/Sentinel/blob/master/sentinel-demo/sentinel-demo-basic/src/main/java/com/alibaba/csp/sentinel/demo/flow/FlowQpsDemo.java)。

```java
public class FlowQpsDemo {
                         // 资源名称
        private static final String KEY = "abc";
                         // 统计执行通过的总数
        private static AtomicInteger pass = new AtomicInteger();
                         // 统计执行限制的总数
        private static AtomicInteger block = new AtomicInteger();
                         // 统计所有执行总数
        private static AtomicInteger total = new AtomicInteger();
        private static volatile boolean stop = false;
                         // 启动的线程数
        private static final int threadCount = 32;
                         // 执行时间单位为秒(s)
        private static int seconds = 60 + 40;
        public static void main(String[] args) throws Exception {
                         // 初始化流控规则
            initFlowQpsRule();
                         // 启动统计线程
            tick();
                         // 启动业务线程
            simulateTraffic();
            System.out.println("===== begin to do flow control");
            System.out.println("only 20 requests per second can pass");
        }
        private static void initFlowQpsRule() {
            List<FlowRule> rules = new ArrayList<FlowRule>();
            FlowRule rule1 = new FlowRule();
                         // 资源名，即限流规则的作用对象
            rule1.setResource(KEY);
                         // set limit qps to 20 限流阈值
            rule1.setCount(20);
                         // 限流阈值类型（QPS 或并发线程数）
            rule1.setGrade(RuleConstant.FLOW_GRADE_QPS);
                         // 流控针对的调用来源，若为 default 则不区分调用来源
            rule1.setLimitApp("default");
                         // 调用关系限流策略
                         // rule1.setStrategy(RuleConstant.STRATEGY_DIRECT);
                         // 流量控制效果（直接拒绝、Warm Up、匀速排队）
                         // rule1.setControlBehavior(RuleConstant.CONTROL_BEHAVIOR_DEFAULT);
            rules.add(rule1);
                         // 加载限流的规则
            FlowRuleManager.loadRules(rules);
        }
        private static void simulateTraffic() {
            for (int i = 0; i < threadCount; i++) {
                Thread t = new Thread(new RunTask());
                t.setName("simulate-traffic-Task");
                t.start();
            }
        }

        private static void tick() {
            Thread timer = new Thread(new TimerTask());
            timer.setName("sentinel-timer-task");
            timer.start();
        }
        static class TimerTask implements Runnable {
            @Override
            public void run() {
                long start = System.currentTimeMillis();
                System.out.println("begin to statistic!!!");
                long oldTotal = 0;
                long oldPass = 0;
                long oldBlock = 0;
                while (!stop) {
                    try {
                        TimeUnit.SECONDS.sleep(1);
                    } catch (InterruptedException e) {
                        
                    }
                    long globalTotal = total.get();
                    long oneSecondTotal = globalTotal - oldTotal;
                    oldTotal = globalTotal;
                    long globalPass = pass.get();
                    long oneSecondPass = globalPass - oldPass;
                    oldPass = globalPass;
                    long globalBlock = block.get();
                    long oneSecondBlock = globalBlock - oldBlock;
                    oldBlock = globalBlock;
                    System.out.println(seconds + " send qps is: " + oneSecondTotal);
                    System.out.println(TimeUtil.currentTimeMillis() + ", total:" + oneSecondTotal + ", pass:" + oneSecondPass + ", block:" + oneSecondBlock);
                    if (seconds-- <= 0) {
                        stop = true;
                    }
                }
                long cost = System.currentTimeMillis() - start;
                System.out.println("time cost: " + cost + " ms");
                System.out.println("total:" + total.get() + ", pass:" + pass.get()+ ", block:" + block.get());
                System.exit(0);
            }
        }

        static class RunTask implements Runnable {
            @Override
            public void run() {
                while (!stop) {
                    ContextUtil.enter("entrancel", "appA");
                    try (Entry entry = SphU.entry(KEY)) {
                         // token acquired, means pass
                        pass.addAndGet(1);
                    } catch (BlockException e1) {
                        block.incrementAndGet();
                    } catch (Exception e2) {
                         // biz exception
                    } finally {
                        total.incrementAndGet();
                    }
                    ContextUtil.exit();
                    Random random2 = new Random();
                    try {
                        TimeUnit.MILLISECONDS.sleep(random2.nextInt(50));
                    } catch (InterruptedException e) 
                         // ignore
                    }
                }
            }
        }
    }
```

执行结果：

可以看到pass数基本上维持在20，但是第一次统计的pass值还是超过了20。这是由于Demo中的代码模拟请求是用的一个线程，统计结果是用的另外一个线程，统计线程每1秒钟统计一次结果，这两个线程之间是有时间上的误差的。从TimeTicker线程打印出来的时间戳可以看出来，虽然每隔一秒进行统计，但是当前打印时的时间和上一次的时间还是有误差的，不完全是1000ms的间隔。但是后续请求也出现了21的情况。这是由于统计使用的是LongAddr，在于高并发时将对单一变量的CAS操作分散为对数组cells中多个元素的CAS操作，取值时进行求和；而在并发较低时仅对base变量进行CAS操作。因此会有一些微小的偏差。

**Warm Up**

Warm Up（RuleConstant.CONTROL_BEHAVIOR_WARM_UP）方式，即预热/冷启动方式。当系统长期处于低水位的情况下，当流量突然增加时，直接把系统拉升到高水位可能瞬间把系统压垮。通过"冷启动"，让通过的流量缓慢增加，在一定时间内逐渐增加到阈值上限，给冷系统一个预热的时间，避免冷系统被压垮。详细文档可以参考 [流量控制 - Warm Up 文档](https://github.com/alibaba/Sentinel/wiki/%E9%99%90%E6%B5%81---%E5%86%B7%E5%90%AF%E5%8A%A8)，具体的例子可以参见 [WarmUpFlowDemo](https://github.com/alibaba/Sentinel/blob/master/sentinel-demo/sentinel-demo-basic/src/main/java/com/alibaba/csp/sentinel/demo/flow/WarmUpFlowDemo.java)。通常冷启动的过程系统允许通过的 QPS 曲线如下图所示：

[image](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/dd791a0f-bee5-40e4-8628-43cee89eedc4/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XTLHBHTJ%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T225830Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIHTLngrsmE87Bxeh2JDZX14iT8nNgJxmV010cF5RpXO4AiA2Oscn6wv%2FOTGAeexYVarkF3ZUqW%2FsnLG6uHqcTs7SfyqIBAjG%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMrkUd8UxZAs3FZe63KtwD2desvAlotKHDGDq1Cgwmrv7PwE81g0sYzv2ehHoGoDhgW0YLsClClymEEyRymYY3joI32IcyfaOZYi1eK2rSDruEiOU49tV16pcEGQR%2BVxLA4VRsIpbGU6Sp0aEdzhW%2B33ah6GoFYqoo%2BmftHgfZ5CoFDcMXT7MjoWWrw32c66FG%2FgkHaqn%2FuZnRkeMhouhxUy0JHcQxFNve5CWhgRnQasABiwazNIr121JJMlleiiHUQke12YG7MDEXWBHTmxr2gt3xJSqid85ueTxqSfM2FQWaZVTGZddl4KqGKHgtnQHUKrKcWj30o3iJ0DY0Xm%2F7Fp43mfFb6d6J898LlFx31jULrlODYso%2BiVNAfu%2BLr9FX3egohvoobDrH5DGrp%2Bt%2Fh9rzukVMe6Ez9zyyN6M8%2BlieB2T0Kw%2FxHoGIi1HPYrpb1w6wBZB9Zm6eSba66q%2B%2FGoD%2FxtpaWZCVda7PT3NEH%2F4Gez1wUAY81IVJXVITOdFKssHlN3QuKtMzZ1JmJ0Ij6Uk5Zk9k44TCufNENTNN6BV355u8UJdqIKZUzJvOsBuAvJTFaTE2UH3IL90vjuk2dFQVcxk6GnIAVLZ3%2Bc6nVviH6uw1WMzusHOnAKTsBaJHjHwpMtBSA36X%2BS4worj%2F0gY6pgHCWjvv%2FOOLmmcL3avJ9i2x3JK1dZ94%2FZMoKWODkGkEb%2BKGc3bHiG1%2FmBIM8j%2FUgyVFx0sA5Pzn7%2BHG4WKaKXuYFSgG5E3iygDsjhL4VOLZYoFvA%2FyEe2uF%2BodPS0RH55is6RXirJQ4fUQKC3FcxMcTMG8DftdOdJfbypOfSqau6oR6eMlOcpaPJyb0WwIZNzRaqKhJt1T0D35%2FRPYhmx4%2FFFlloZvy&X-Amz-Signature=3aaad26c5c4ffea12dc8c35a3b38d6e6efcb68e17b451bcc23d13ee2fad6b86b&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

```java
private static void initFlowRule() {

List<FlowRule> rules = new ArrayList<FlowRule>();

FlowRule rule1 = new FlowRule();

rule1.setResource(KEY);

rule1.setCount(20);

rule1.setGrade(RuleConstant.FLOW_GRADE_QPS);

rule1.setLimitApp("default");

rule1.setControlBehavior(RuleConstant.CONTROL_BEHAVIOR_WARM_UP);

rule1.setWarmUpPeriodSec(10);

rules.add(rule1);

FlowRuleManager.loadRules(rules);

}
```

CONTROL_BEHAVIOR_WARM_UP 表示启用冷启动模式，warmUpPeriodSec 代表期待系统进入稳定状态的时间（即预热时长）。

```java
Large amount of traffic is coming

88 send qps is: 2061

1528883307808,total:2061, pass:9, block:2053

87 send qps is: 3699

1528883308808,total:3699, pass:7, block:3692

86 send qps is: 3898

1528883309808,total:3898, pass:7, block:3893

85 send qps is: 3713

1528883310808,total:3713, pass:7, block:3708

84 send qps is: 3756

1528883311808,total:3756, pass:8, block:3749

83 send qps is: 3750

1528883312808,total:3750, pass:9, block:3741

82 send qps is: 3492

1528883313806,total:3492, pass:10, block:3482

81 send qps is: 3923

1528883314808,total:3923, pass:11, block:3913

80 send qps is: 3176

1528883315820,total:3176, pass:13, block:3163

79 send qps is: 3729

1528883316821,total:3729, pass:22, block:3708

78 send qps is: 3534

1528883317820,total:3534, pass:20, block:3514
```

可以看到第 10 秒的时候，系统开始稳定的接受 20 个请求。

**匀速排队**

匀速排队（RuleConstant.CONTROL_BEHAVIOR_RATE_LIMITER）方式会严格控制请求通过的间隔时间，也即是让请求以均匀的速度通过，对应的是漏桶算法。详细文档可以参考 [流量控制 - 匀速器模式](https://github.com/alibaba/Sentinel/wiki/%E6%B5%81%E9%87%8F%E6%8E%A7%E5%88%B6-%E5%8C%80%E9%80%9F%E6%8E%92%E9%98%9F%E6%A8%A1%E5%BC%8F)，具体的例子可以参见 [PaceFlowDemo](https://github.com/alibaba/Sentinel/blob/master/sentinel-demo/sentinel-demo-basic/src/main/java/com/alibaba/csp/sentinel/demo/flow/PaceFlowDemo.java)。

该方式的作用如下图所示：

[image](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/c6ed8264-16d5-4a93-b7e5-3a53e25e8182/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XTLHBHTJ%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T225830Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIHTLngrsmE87Bxeh2JDZX14iT8nNgJxmV010cF5RpXO4AiA2Oscn6wv%2FOTGAeexYVarkF3ZUqW%2FsnLG6uHqcTs7SfyqIBAjG%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMrkUd8UxZAs3FZe63KtwD2desvAlotKHDGDq1Cgwmrv7PwE81g0sYzv2ehHoGoDhgW0YLsClClymEEyRymYY3joI32IcyfaOZYi1eK2rSDruEiOU49tV16pcEGQR%2BVxLA4VRsIpbGU6Sp0aEdzhW%2B33ah6GoFYqoo%2BmftHgfZ5CoFDcMXT7MjoWWrw32c66FG%2FgkHaqn%2FuZnRkeMhouhxUy0JHcQxFNve5CWhgRnQasABiwazNIr121JJMlleiiHUQke12YG7MDEXWBHTmxr2gt3xJSqid85ueTxqSfM2FQWaZVTGZddl4KqGKHgtnQHUKrKcWj30o3iJ0DY0Xm%2F7Fp43mfFb6d6J898LlFx31jULrlODYso%2BiVNAfu%2BLr9FX3egohvoobDrH5DGrp%2Bt%2Fh9rzukVMe6Ez9zyyN6M8%2BlieB2T0Kw%2FxHoGIi1HPYrpb1w6wBZB9Zm6eSba66q%2B%2FGoD%2FxtpaWZCVda7PT3NEH%2F4Gez1wUAY81IVJXVITOdFKssHlN3QuKtMzZ1JmJ0Ij6Uk5Zk9k44TCufNENTNN6BV355u8UJdqIKZUzJvOsBuAvJTFaTE2UH3IL90vjuk2dFQVcxk6GnIAVLZ3%2Bc6nVviH6uw1WMzusHOnAKTsBaJHjHwpMtBSA36X%2BS4worj%2F0gY6pgHCWjvv%2FOOLmmcL3avJ9i2x3JK1dZ94%2FZMoKWODkGkEb%2BKGc3bHiG1%2FmBIM8j%2FUgyVFx0sA5Pzn7%2BHG4WKaKXuYFSgG5E3iygDsjhL4VOLZYoFvA%2FyEe2uF%2BodPS0RH55is6RXirJQ4fUQKC3FcxMcTMG8DftdOdJfbypOfSqau6oR6eMlOcpaPJyb0WwIZNzRaqKhJt1T0D35%2FRPYhmx4%2FFFlloZvy&X-Amz-Signature=cec9e8f7dfaa95332f30a4b7ad44f13d2c01a0e2f6924432840fb1277f5dd688&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

这种方式主要用于处理间隔性突发的流量，例如消息队列。想象一下这样的场景，在某一秒有大量的请求到来，而接下来的几秒则处于空闲状态，我们希望系统能够在接下来的空闲期间逐渐处理这些请求，而不是在第一秒直接拒绝多余的请求。

它的中心思想是，以固定的间隔时间让请求通过。当请求到来的时候，如果当前请求距离上个通过的请求通过的时间间隔不小于预设值，则让当前请求通过；否则，计算当前请求的预期通过时间，如果该请求的预期通过时间小于规则预设的 timeout 时间，则该请求会等待直到预设时间到来通过（排队等待处理）；若预期的通过时间超出最大排队时长，则直接拒接这个请求。

```java
private static void initPaceFlowRule() {

List<FlowRule> rules = new ArrayList<FlowRule>();

FlowRule rule1 = new FlowRule();

rule1.setResource(KEY);

rule1.setCount(count);

rule1.setGrade(RuleConstant.FLOW_GRADE_QPS);

rule1.setLimitApp("default");

/*

- CONTROL_BEHAVIOR_RATE_LIMITER means requests more than threshold will be queueing in the queue,
- until the queueing time is more than {@link FlowRule#maxQueueingTimeMs}, the requests will be rejected.
- /

// 流控效果：匀速排队模式

rule1.setControlBehavior(RuleConstant.CONTROL_BEHAVIOR_RATE_LIMITER);

// 最长排队等待时间：20s

rule1.setMaxQueueingTimeMs(20 * 1000);

rules.add(rule1);

FlowRuleManager.loadRules(rules);

}
```

当匀速器生效的时候，规则的限流类型一定是 RuleConstant.GRADE_QPS，否则该规则将不生效。当 count 设为 10 的时候，则代表一秒匀速的通过 10 个请求，也就是每个请求平均间隔恒定为 1000 / 10 = 100 ms，每一个请求的最长等待时间（maxQueueingTimeMs）为 20 * 1000ms = 20s。我们来看一下运行结果:下面的输出以逗号分隔，第一栏位通过的时间，第二栏为等待的时间

```java
…

1528872403887 pass, cost 9348

1528872403986 pass, cost 9469

1528872404087 pass, cost 9570

1528872404187 pass, cost 9642

1528872404287 pass, cost 9770

1528872404387 pass, cost 9848

1528872404487 pass, cost 9970

done

pass:100 block:0
```

我们可以看到，这 100 个请求，都以匀速 100 ms 的速度依次通过，并且没有阻塞。

**并发线程数流量控制**

并发线程数限流用于保护业务线程数不被耗尽。例如，当应用所依赖的下游应用由于某种原因导致服务不稳定、响应延迟增加，对于调用者来说，意味着吞吐量下降和更多的线程数占用，极端情况下甚至导致线程池耗尽。为应对太多线程占用的情况，业内有使用隔离的方案，比如通过不同业务逻辑使用不同线程池来隔离业务自身之间的资源争抢（线程池隔离）。这种隔离方案虽然隔离性比较好，但是代价就是线程数目太多，线程上下文切换的 overhead 比较大，特别是对低延时的调用有比较大的影响。Sentinel 并发线程数限流不负责创建和管理线程池，而是简单统计当前请求上下文的线程数目，如果超出阈值，新的请求会被立即拒绝，效果类似于信号量隔离。

例子参见：[ThreadDemo](https://github.com/alibaba/Sentinel/blob/master/sentinel-demo/sentinel-demo-basic/src/main/java/com/alibaba/csp/sentinel/demo/flow/FlowThreadDemo.java)

[image](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/d4ad27b9-e406-4413-8dcd-105f5897ee01/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XTLHBHTJ%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T225830Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIHTLngrsmE87Bxeh2JDZX14iT8nNgJxmV010cF5RpXO4AiA2Oscn6wv%2FOTGAeexYVarkF3ZUqW%2FsnLG6uHqcTs7SfyqIBAjG%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMrkUd8UxZAs3FZe63KtwD2desvAlotKHDGDq1Cgwmrv7PwE81g0sYzv2ehHoGoDhgW0YLsClClymEEyRymYY3joI32IcyfaOZYi1eK2rSDruEiOU49tV16pcEGQR%2BVxLA4VRsIpbGU6Sp0aEdzhW%2B33ah6GoFYqoo%2BmftHgfZ5CoFDcMXT7MjoWWrw32c66FG%2FgkHaqn%2FuZnRkeMhouhxUy0JHcQxFNve5CWhgRnQasABiwazNIr121JJMlleiiHUQke12YG7MDEXWBHTmxr2gt3xJSqid85ueTxqSfM2FQWaZVTGZddl4KqGKHgtnQHUKrKcWj30o3iJ0DY0Xm%2F7Fp43mfFb6d6J898LlFx31jULrlODYso%2BiVNAfu%2BLr9FX3egohvoobDrH5DGrp%2Bt%2Fh9rzukVMe6Ez9zyyN6M8%2BlieB2T0Kw%2FxHoGIi1HPYrpb1w6wBZB9Zm6eSba66q%2B%2FGoD%2FxtpaWZCVda7PT3NEH%2F4Gez1wUAY81IVJXVITOdFKssHlN3QuKtMzZ1JmJ0Ij6Uk5Zk9k44TCufNENTNN6BV355u8UJdqIKZUzJvOsBuAvJTFaTE2UH3IL90vjuk2dFQVcxk6GnIAVLZ3%2Bc6nVviH6uw1WMzusHOnAKTsBaJHjHwpMtBSA36X%2BS4worj%2F0gY6pgHCWjvv%2FOOLmmcL3avJ9i2x3JK1dZ94%2FZMoKWODkGkEb%2BKGc3bHiG1%2FmBIM8j%2FUgyVFx0sA5Pzn7%2BHG4WKaKXuYFSgG5E3iygDsjhL4VOLZYoFvA%2FyEe2uF%2BodPS0RH55is6RXirJQ4fUQKC3FcxMcTMG8DftdOdJfbypOfSqau6oR6eMlOcpaPJyb0WwIZNzRaqKhJt1T0D35%2FRPYhmx4%2FFFlloZvy&X-Amz-Signature=8388363a617ba81fd9b93615cb87c0f8936490dc46818c81298793dc895eb595&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

[image](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/7ea7d5a9-71e4-422f-9b81-28fee270d0a7/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XTLHBHTJ%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T225830Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIHTLngrsmE87Bxeh2JDZX14iT8nNgJxmV010cF5RpXO4AiA2Oscn6wv%2FOTGAeexYVarkF3ZUqW%2FsnLG6uHqcTs7SfyqIBAjG%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMrkUd8UxZAs3FZe63KtwD2desvAlotKHDGDq1Cgwmrv7PwE81g0sYzv2ehHoGoDhgW0YLsClClymEEyRymYY3joI32IcyfaOZYi1eK2rSDruEiOU49tV16pcEGQR%2BVxLA4VRsIpbGU6Sp0aEdzhW%2B33ah6GoFYqoo%2BmftHgfZ5CoFDcMXT7MjoWWrw32c66FG%2FgkHaqn%2FuZnRkeMhouhxUy0JHcQxFNve5CWhgRnQasABiwazNIr121JJMlleiiHUQke12YG7MDEXWBHTmxr2gt3xJSqid85ueTxqSfM2FQWaZVTGZddl4KqGKHgtnQHUKrKcWj30o3iJ0DY0Xm%2F7Fp43mfFb6d6J898LlFx31jULrlODYso%2BiVNAfu%2BLr9FX3egohvoobDrH5DGrp%2Bt%2Fh9rzukVMe6Ez9zyyN6M8%2BlieB2T0Kw%2FxHoGIi1HPYrpb1w6wBZB9Zm6eSba66q%2B%2FGoD%2FxtpaWZCVda7PT3NEH%2F4Gez1wUAY81IVJXVITOdFKssHlN3QuKtMzZ1JmJ0Ij6Uk5Zk9k44TCufNENTNN6BV355u8UJdqIKZUzJvOsBuAvJTFaTE2UH3IL90vjuk2dFQVcxk6GnIAVLZ3%2Bc6nVviH6uw1WMzusHOnAKTsBaJHjHwpMtBSA36X%2BS4worj%2F0gY6pgHCWjvv%2FOOLmmcL3avJ9i2x3JK1dZ94%2FZMoKWODkGkEb%2BKGc3bHiG1%2FmBIM8j%2FUgyVFx0sA5Pzn7%2BHG4WKaKXuYFSgG5E3iygDsjhL4VOLZYoFvA%2FyEe2uF%2BodPS0RH55is6RXirJQ4fUQKC3FcxMcTMG8DftdOdJfbypOfSqau6oR6eMlOcpaPJyb0WwIZNzRaqKhJt1T0D35%2FRPYhmx4%2FFFlloZvy&X-Amz-Signature=9f2524f88c158df81e8c0f49303652600825e6417d7f9966b87cd1adb62f9b4d&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)






## 

