---
title: 1-10 附系统自适应限流文档说明
---

# 1-10 附系统自适应限流文档说明

[image](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/9bf65200-8f85-4963-9eaa-8da6f77ca976/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TQYS2QYW%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T225832Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIB%2BRv8a3htggsKyMtgd0l%2FlCcgHWiNn5D6%2FyihMRUqMxAiEAkGVLgL9RnOwrzIxsEsLJ8sPFwakli04WIW%2B3TkqwxdUqiAQIxv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDOgKYs5MB69dK4n2XCrcA8JB2BdonpIwOx8cNFE5qBKDABsU3eZnfGlZiHvD06umlMFcJFoyYLDtkKWCv6DOWKH%2Fc3WrB38jGJfw9gX9%2F5KNoIv3XiulDL50NIpvngMv2YVCdHTlDqGs3OzdN7gV6W%2FqpfEDXx5kd%2F1NORWWwJnMxrvBlj6ywa3ClBkf%2F6lsOvOHDzMZ0SMFa97rwBWASLir77Ly5xW5HwJdU5McxARmG9iosAHWWZ3MYQXJo%2Fz9vgXtVJqWbHgq%2FeMb1e%2BWEx57qSMSSU5H62JifdAXLtEMOlOraMsjUbJ%2BicDIqoWaK3OdlTiLwh2VbFIQeSZvEZdxGAqezbyOUBFZWKEgEJjCAbd7tK%2FUWzFR%2FGiuUu6b43zUdsyyW7BWOthBt4PQnALFEwsWhHyO06Ut2%2FIsDaQftDPXI7cnz6YhJsS8MQx%2B95MuY9moeBQRNVqFMIHTL1Fv7GyWWnmuvOHmKFn7oY4wHRdGgOoeHVFSD5CYf3iHEGR8rT3AX6r%2Fw17aLhhiiqV7otg1GEQlC996TEpICymDBV64y3jHUfcI5yCiI5ZYDn5AqGiHwQ%2FuM%2BOQ%2BBvpYOeghUUO7ge7Oy3OIU8Mpa822vqyhPTwz7GfjjQw%2FISFG%2FsLJ42a1WVXNTaHMLO6%2F9IGOqUBda7rIMh1bm3GRAJaHOTTlp1DaPo9r106LkrTm1lxQcj8OsCWtqzYNhfMIpZS2XpyGSpskesiQCkwwBnLX5%2F5qB5n5dXiXbPvA%2FebCuaI%2Be0BcB5CtDdgu2zjkpG8aaeqsAd55Aj6X6lBVElSDcUSOv7KXZ91jVXJe1S%2FUcrutkuFmVAe8Ag0qnxRCXgjS%2Bt1nEyNZ%2B3Y8fTer1m%2BEz3Iq7UA3yIv&X-Amz-Signature=49117d08c811e24e1092a8d78228d418b7edb87b38473efc0521c5307df3a1e0&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

[image](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/fd4d7753-179a-4549-82e3-e7acbd0fe353/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TQYS2QYW%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T225832Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIB%2BRv8a3htggsKyMtgd0l%2FlCcgHWiNn5D6%2FyihMRUqMxAiEAkGVLgL9RnOwrzIxsEsLJ8sPFwakli04WIW%2B3TkqwxdUqiAQIxv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDOgKYs5MB69dK4n2XCrcA8JB2BdonpIwOx8cNFE5qBKDABsU3eZnfGlZiHvD06umlMFcJFoyYLDtkKWCv6DOWKH%2Fc3WrB38jGJfw9gX9%2F5KNoIv3XiulDL50NIpvngMv2YVCdHTlDqGs3OzdN7gV6W%2FqpfEDXx5kd%2F1NORWWwJnMxrvBlj6ywa3ClBkf%2F6lsOvOHDzMZ0SMFa97rwBWASLir77Ly5xW5HwJdU5McxARmG9iosAHWWZ3MYQXJo%2Fz9vgXtVJqWbHgq%2FeMb1e%2BWEx57qSMSSU5H62JifdAXLtEMOlOraMsjUbJ%2BicDIqoWaK3OdlTiLwh2VbFIQeSZvEZdxGAqezbyOUBFZWKEgEJjCAbd7tK%2FUWzFR%2FGiuUu6b43zUdsyyW7BWOthBt4PQnALFEwsWhHyO06Ut2%2FIsDaQftDPXI7cnz6YhJsS8MQx%2B95MuY9moeBQRNVqFMIHTL1Fv7GyWWnmuvOHmKFn7oY4wHRdGgOoeHVFSD5CYf3iHEGR8rT3AX6r%2Fw17aLhhiiqV7otg1GEQlC996TEpICymDBV64y3jHUfcI5yCiI5ZYDn5AqGiHwQ%2FuM%2BOQ%2BBvpYOeghUUO7ge7Oy3OIU8Mpa822vqyhPTwz7GfjjQw%2FISFG%2FsLJ42a1WVXNTaHMLO6%2F9IGOqUBda7rIMh1bm3GRAJaHOTTlp1DaPo9r106LkrTm1lxQcj8OsCWtqzYNhfMIpZS2XpyGSpskesiQCkwwBnLX5%2F5qB5n5dXiXbPvA%2FebCuaI%2Be0BcB5CtDdgu2zjkpG8aaeqsAd55Aj6X6lBVElSDcUSOv7KXZ91jVXJe1S%2FUcrutkuFmVAe8Ag0qnxRCXgjS%2Bt1nEyNZ%2B3Y8fTer1m%2BEz3Iq7UA3yIv&X-Amz-Signature=320cf4935a2d8984ac2b4dc160c3128f80becb44e20080463d3bd049eba0bba0&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

**概述**

Sentinel 系统自适应限流从整体维度对应用入口流量进行控制，结合应用的 Load、总体平均 RT、入口 QPS 和线程数等几个维度的监控指标，让系统的入口流量和系统的负载达到一个平衡，让系统尽可能跑在最大吞吐量的同时保证系统整体的稳定性。

**背景**

在开始之前，先回顾一下 Sentinel 做系统自适应限流的目的：

保证系统不被拖垮

在系统稳定的前提下，保持系统的吞吐量

长期以来，系统自适应保护的思路是根据硬指标，即系统的负载 (load1) 来做系统过载保护。当系统负载高于某个阈值，就禁止或者减少流量的进入；当 load 开始好转，则恢复流量的进入。这个思路给我们带来了不可避免的两个问题：

load 是一个“果”，如果根据 load 的情况来调节流量的通过率，那么就始终有延迟性。也就意味着通过率的任何调整，都会过一段时间才能看到效果。当前通过率是使 load 恶化的一个动作，那么也至少要过 1 秒之后才能观测到；同理，如果当前通过率调整是让 load 好转的一个动作，也需要 1 秒之后才能继续调整，这样就浪费了系统的处理能力。所以我们看到的曲线，总是会有抖动。

恢复慢。想象一下这样的一个场景（真实），出现了这样一个问题，下游应用不可靠，导致应用 RT 很高，从而 load 到了一个很高的点。过了一段时间之后下游应用恢复了，应用 RT 也相应减少。这个时候，其实应该大幅度增大流量的通过率；但是由于这个时候 load 仍然很高，通过率的恢复仍然不高。

TCP BBR 的思想给了我们一个很大的启发。我们应该根据系统能够处理的请求，和允许进来的请求，来做平衡，而不是根据一个间接的指标（系统 load）来做限流。最终我们追求的目标是 在系统不被拖垮的情况下，提高系统的吞吐率，而不是 load 一定要到低于某个阈值。如果我们还是按照固有的思维，超过特定的 load 就禁止流量进入，系统 load 恢复就放开流量，这样做的结果是无论我们怎么调参数，调比例，都是按照果来调节因，都无法取得良好的效果。

Sentinel 在系统自适应保护的做法是，用 load1 作为启动控制流量的值，而允许通过的流量由处理请求的能力，即请求的响应时间以及当前系统正在处理的请求速率来决定。

**系统规则**

系统保护规则是从应用级别的入口流量进行控制，从单台机器的总体 Load、RT、入口 QPS 和线程数四个维度监控应用数据，让系统尽可能跑在最大吞吐量的同时保证系统整体的稳定性。

系统保护规则是应用整体维度的，而不是资源维度的，并且仅对入口流量生效。入口流量指的是进入应用的流量（[EntryType.IN](http://entrytype.in/)），比如 Web 服务或 Dubbo 服务端接收的请求，都属于入口流量。

系统规则支持四种阈值类型：

Load（仅对 Linux/Unix-like 机器生效）：当系统 load1 超过阈值，且系统当前的并发线程数超过系统容量时才会触发系统保护。系统容量由系统的 maxQps * minRt 计算得出。设定参考值一般是 CPU cores * 2.5。

RT：当单台机器上所有入口流量的平均 RT 达到阈值即触发系统保护，单位是毫秒。

线程数：当单台机器上所有入口流量的并发线程数达到阈值即触发系统保护。

入口 QPS：当单台机器上所有入口流量的 QPS 达到阈值即触发系统保护。

**原理**

先用经典图来镇楼:

[image](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/20802b5e-59dd-4374-b0f7-76f81c05e7f0/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TQYS2QYW%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T225832Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIB%2BRv8a3htggsKyMtgd0l%2FlCcgHWiNn5D6%2FyihMRUqMxAiEAkGVLgL9RnOwrzIxsEsLJ8sPFwakli04WIW%2B3TkqwxdUqiAQIxv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDOgKYs5MB69dK4n2XCrcA8JB2BdonpIwOx8cNFE5qBKDABsU3eZnfGlZiHvD06umlMFcJFoyYLDtkKWCv6DOWKH%2Fc3WrB38jGJfw9gX9%2F5KNoIv3XiulDL50NIpvngMv2YVCdHTlDqGs3OzdN7gV6W%2FqpfEDXx5kd%2F1NORWWwJnMxrvBlj6ywa3ClBkf%2F6lsOvOHDzMZ0SMFa97rwBWASLir77Ly5xW5HwJdU5McxARmG9iosAHWWZ3MYQXJo%2Fz9vgXtVJqWbHgq%2FeMb1e%2BWEx57qSMSSU5H62JifdAXLtEMOlOraMsjUbJ%2BicDIqoWaK3OdlTiLwh2VbFIQeSZvEZdxGAqezbyOUBFZWKEgEJjCAbd7tK%2FUWzFR%2FGiuUu6b43zUdsyyW7BWOthBt4PQnALFEwsWhHyO06Ut2%2FIsDaQftDPXI7cnz6YhJsS8MQx%2B95MuY9moeBQRNVqFMIHTL1Fv7GyWWnmuvOHmKFn7oY4wHRdGgOoeHVFSD5CYf3iHEGR8rT3AX6r%2Fw17aLhhiiqV7otg1GEQlC996TEpICymDBV64y3jHUfcI5yCiI5ZYDn5AqGiHwQ%2FuM%2BOQ%2BBvpYOeghUUO7ge7Oy3OIU8Mpa822vqyhPTwz7GfjjQw%2FISFG%2FsLJ42a1WVXNTaHMLO6%2F9IGOqUBda7rIMh1bm3GRAJaHOTTlp1DaPo9r106LkrTm1lxQcj8OsCWtqzYNhfMIpZS2XpyGSpskesiQCkwwBnLX5%2F5qB5n5dXiXbPvA%2FebCuaI%2Be0BcB5CtDdgu2zjkpG8aaeqsAd55Aj6X6lBVElSDcUSOv7KXZ91jVXJe1S%2FUcrutkuFmVAe8Ag0qnxRCXgjS%2Bt1nEyNZ%2B3Y8fTer1m%2BEz3Iq7UA3yIv&X-Amz-Signature=e9c58102a3c62536fda5d83483c25b1ff017678621bdae119a8b57b825122bd8&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

我们把系统处理请求的过程想象为一个水管，到来的请求是往这个水管灌水，当系统处理顺畅的时候，请求不需要排队，直接从水管中穿过，这个请求的RT是最短的；反之，当请求堆积的时候，那么处理请求的时间则会变为：排队时间 + 最短处理时间。

推论一:如果我们能够保证水管里的水量，能够让水顺畅的流动，则不会增加排队的请求；也就是说，这个时候的系统负载不会进一步恶化。我们用 T 来表示(水管内部的水量)，用RT来表示请求的处理时间，用P来表示进来的请求数，那么一个请求从进入水管道到从水管出来，这个水管会存在 P * RT　个请求。换一句话来说，当 T ≈ QPS * Avg(RT) 的时候，我们可以认为系统的处理能力和允许进入的请求个数达到了平衡，系统的负载不会进一步恶化。


接下来的问题是，水管的水位是可以达到了一个平衡点，但是这个平衡点只能保证水管的水位不再继续增高，但是还面临一个问题，就是在达到平衡点之前，这个水管里已经堆积了多少水。如果之前水管的水已经在一个量级了，那么这个时候系统允许通过的水量可能只能缓慢通过，RT会大，之前堆积在水管里的水会滞留；反之，如果之前的水管水位偏低，那么又会浪费了系统的处理能力。

推论二:　当保持入口的流量是水管出来的流量的最大的值的时候，可以最大利用水管的处理能力。


然而，和 TCP BBR 的不一样的地方在于，还需要用一个系统负载的值（load1）来激发这套机制启动。

注：这种系统自适应算法对于低 load 的请求，它的效果是一个“兜底”的角色。对于不是应用本身造成的 load 高的情况（如其它进程导致的不稳定的情况），效果不明显。

**示例**

我们提供了系统自适应限流的示例：[SystemGuardDemo](https://github.com/alibaba/Sentinel/blob/master/sentinel-demo/sentinel-demo-basic/src/main/java/com/alibaba/csp/sentinel/demo/system/SystemGuardDemo.java)。

```java
/*
 * Copyright 1999-2018 Alibaba Group Holding Ltd.
 *
 * Licensed under the Apache License, Version 2.0 (the "License");
 * you may not use this file except in compliance with the License.
 * You may obtain a copy of the License at
 *
 *      http://www.apache.org/licenses/LICENSE-2.0
 *
 * Unless required by applicable law or agreed to in writing, software
 * distributed under the License is distributed on an "AS IS" BASIS,
 * WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
 * See the License for the specific language governing permissions and
 * limitations under the License.
 */
package com.alibaba.csp.sentinel.demo.system;

import java.util.ArrayList;
import java.util.Collections;
import java.util.List;
import java.util.concurrent.TimeUnit;
import java.util.concurrent.atomic.AtomicInteger;

import com.alibaba.csp.sentinel.util.TimeUtil;
import com.alibaba.csp.sentinel.Entry;
import com.alibaba.csp.sentinel.EntryType;
import com.alibaba.csp.sentinel.SphU;
import com.alibaba.csp.sentinel.slots.block.BlockException;
import com.alibaba.csp.sentinel.slots.system.SystemRule;
import com.alibaba.csp.sentinel.slots.system.SystemRuleManager;

/**
 * @author jialiang.linjl
 */
public class SystemGuardDemo {

    private static AtomicInteger pass = new AtomicInteger();
    private static AtomicInteger block = new AtomicInteger();
    private static AtomicInteger total = new AtomicInteger();

    private static volatile boolean stop = false;
    private static final int threadCount = 100;

    private static int seconds = 60 + 40;

    public static void main(String[] args) throws Exception {

        tick();
        initSystemRule();

        for (int i = 0; i < threadCount; i++) {
            Thread entryThread = new Thread(new Runnable() {
                @Override
                public void run() {
                    while (true) {
                        Entry entry = null;
                        try {
                            entry = SphU.entry("methodA", EntryType.IN);
                            pass.incrementAndGet();
                            try {
                                TimeUnit.MILLISECONDS.sleep(20);
                            } catch (InterruptedException e) {
                                // ignore
                            }
                        } catch (BlockException e1) {
                            block.incrementAndGet();
                            try {
                                TimeUnit.MILLISECONDS.sleep(20);
                            } catch (InterruptedException e) {
                                // ignore
                            }
                        } catch (Exception e2) {
                            // biz exception
                        } finally {
                            total.incrementAndGet();
                            if (entry != null) {
                                entry.exit();
                            }
                        }
                    }
                }

            });
            entryThread.setName("working-thread");
            entryThread.start();
        }
    }

    private static void initSystemRule() {
        List<SystemRule> rules = new ArrayList<SystemRule>();
        SystemRule rule = new SystemRule();
        // max load is 3
        rule.setHighestSystemLoad(3.0);
        // max cpu usage is 60%
        rule.setHighestCpuUsage(0.6);
        // max avg rt of all request is 10 ms
        rule.setAvgRt(10);
        // max total qps is 20
        rule.setQps(20);
        // max parallel working thread is 10
        rule.setMaxThread(10);

        rules.add(rule);
        SystemRuleManager.loadRules(Collections.singletonList(rule));
    }

    private static void tick() {
        Thread timer = new Thread(new TimerTask());
        timer.setName("sentinel-timer-task");
        timer.start();
    }

    static class TimerTask implements Runnable {
        @Override
        public void run() {
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

                System.out.println(seconds + ", " + TimeUtil.currentTimeMillis() + ", total:"
                    + oneSecondTotal + ", pass:"
                    + oneSecondPass + ", block:" + oneSecondBlock);
                if (seconds-- <= 0) {
                    stop = true;
                }
            }
            System.exit(0);
        }
    }
}
```

[image](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/5f305980-04db-4f42-aa89-cdcfa4d548d0/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TQYS2QYW%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T225832Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIB%2BRv8a3htggsKyMtgd0l%2FlCcgHWiNn5D6%2FyihMRUqMxAiEAkGVLgL9RnOwrzIxsEsLJ8sPFwakli04WIW%2B3TkqwxdUqiAQIxv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDOgKYs5MB69dK4n2XCrcA8JB2BdonpIwOx8cNFE5qBKDABsU3eZnfGlZiHvD06umlMFcJFoyYLDtkKWCv6DOWKH%2Fc3WrB38jGJfw9gX9%2F5KNoIv3XiulDL50NIpvngMv2YVCdHTlDqGs3OzdN7gV6W%2FqpfEDXx5kd%2F1NORWWwJnMxrvBlj6ywa3ClBkf%2F6lsOvOHDzMZ0SMFa97rwBWASLir77Ly5xW5HwJdU5McxARmG9iosAHWWZ3MYQXJo%2Fz9vgXtVJqWbHgq%2FeMb1e%2BWEx57qSMSSU5H62JifdAXLtEMOlOraMsjUbJ%2BicDIqoWaK3OdlTiLwh2VbFIQeSZvEZdxGAqezbyOUBFZWKEgEJjCAbd7tK%2FUWzFR%2FGiuUu6b43zUdsyyW7BWOthBt4PQnALFEwsWhHyO06Ut2%2FIsDaQftDPXI7cnz6YhJsS8MQx%2B95MuY9moeBQRNVqFMIHTL1Fv7GyWWnmuvOHmKFn7oY4wHRdGgOoeHVFSD5CYf3iHEGR8rT3AX6r%2Fw17aLhhiiqV7otg1GEQlC996TEpICymDBV64y3jHUfcI5yCiI5ZYDn5AqGiHwQ%2FuM%2BOQ%2BBvpYOeghUUO7ge7Oy3OIU8Mpa822vqyhPTwz7GfjjQw%2FISFG%2FsLJ42a1WVXNTaHMLO6%2F9IGOqUBda7rIMh1bm3GRAJaHOTTlp1DaPo9r106LkrTm1lxQcj8OsCWtqzYNhfMIpZS2XpyGSpskesiQCkwwBnLX5%2F5qB5n5dXiXbPvA%2FebCuaI%2Be0BcB5CtDdgu2zjkpG8aaeqsAd55Aj6X6lBVElSDcUSOv7KXZ91jVXJe1S%2FUcrutkuFmVAe8Ag0qnxRCXgjS%2Bt1nEyNZ%2B3Y8fTer1m%2BEz3Iq7UA3yIv&X-Amz-Signature=2c253ad0234d67e51c7d8b9b4626877a0d5db306fea9ed04dfe8e7a3fa81922d&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)





