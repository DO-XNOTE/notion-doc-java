---
title: 1-8 热点参数限流文档说明
---

# 1-8 热点参数限流文档说明

[image](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/74aa62a2-c683-440e-89ed-e37bd71fe1af/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YNPDM6WY%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T225831Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDoYh%2Flg6E4XajN1b13EfXcMxWNbqQXe9i%2BvH71GePW6AIgKHvgePrPk5Aw5a6CMlDJEQRioJscjWgxFa%2B7uId7%2BU8qiAQIxv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDNpltXqIqYlDj4eVJyrcA9GIZ4HwCk7bdm4wKlEbnXM33ZyIMwRuxGeOjXeQh%2FSLGzDlqRjxcCXZ04VHTs07OPE%2B3GOfD%2FsLXd7L%2BZ7t7YNjXX2zt%2FY9attFsxA5zBFT6rmUpukRb1Y1vGJNzHDskygdwu56iQdyPjsq%2BkcIbtX4HdF2cEcOjpEp6U6HCShd98nnUnw4OASFQwzDv%2BZT%2BxrGidzNpoHXlRTk078f%2Bm7kQRJhOSTHG6AgNO2VdlZqbu9BXTiEPXBoEOAUIjiuFsGFoPyviyJEjR7LcdinqXuaBrbT6P%2FV1L6nkJVubOm2Yp%2BbGscoz4IlSJBhJ9qr67SEsT9LvNwWUAUw7qkcspiiciV1o6FdODBVWFDQ%2F%2FzKdTEP3K5Cz2tyffSjvmdmYF2HOCuFsn8CdO7Z0nAPoh6vhMfprwgxa5J5k1RQnd2Hb0xfcisRPKnbJsYwTea%2BWWSezjteJAiOlLXk68srybtQZCOpB9POQU0wKFgWcE7pby1L8DmZHSe9OotUjO4igWQlFaiuY%2FwoZs%2BrDzW5MiNO9tlGSp0CcRX7QRYh6jsk53yu5Nx9MwW4D5%2BETcnDYZ%2BEtIIj%2BgUmV3n88PbWhyO5pFTVcTDVpV6rLa%2Bjh8kca8T4Ozyipu43QzaCMM%2B3%2F9IGOqUBIVbhMKHLyVhO8tytTLdKQ4RoO0LAF4vgx3C2RGmePB5g0AZIw3bw7Dy0VgxoP%2FMB7C2G%2FENcPKua%2BUnq7MOWvUnz8Dx90njBL2HEmuiOygaZh8AgIfWFax8rBi18SemulmJ46ZR1u4Shm8IgCOGfrlkFOIWD0hq8D8du8RVxkmnaA17AlLmGrGseohggyOXd1QXEZ2rm9oCwEeYOy8mgozH0%2BRpM&X-Amz-Signature=1157f706efad68aa5d9379314cbb2a20556a7e8ba2a11be4ff85af91036128b0&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

[image](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/e97e5e52-c0fc-466f-a9f1-722afe0c2c66/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YNPDM6WY%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T225831Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDoYh%2Flg6E4XajN1b13EfXcMxWNbqQXe9i%2BvH71GePW6AIgKHvgePrPk5Aw5a6CMlDJEQRioJscjWgxFa%2B7uId7%2BU8qiAQIxv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDNpltXqIqYlDj4eVJyrcA9GIZ4HwCk7bdm4wKlEbnXM33ZyIMwRuxGeOjXeQh%2FSLGzDlqRjxcCXZ04VHTs07OPE%2B3GOfD%2FsLXd7L%2BZ7t7YNjXX2zt%2FY9attFsxA5zBFT6rmUpukRb1Y1vGJNzHDskygdwu56iQdyPjsq%2BkcIbtX4HdF2cEcOjpEp6U6HCShd98nnUnw4OASFQwzDv%2BZT%2BxrGidzNpoHXlRTk078f%2Bm7kQRJhOSTHG6AgNO2VdlZqbu9BXTiEPXBoEOAUIjiuFsGFoPyviyJEjR7LcdinqXuaBrbT6P%2FV1L6nkJVubOm2Yp%2BbGscoz4IlSJBhJ9qr67SEsT9LvNwWUAUw7qkcspiiciV1o6FdODBVWFDQ%2F%2FzKdTEP3K5Cz2tyffSjvmdmYF2HOCuFsn8CdO7Z0nAPoh6vhMfprwgxa5J5k1RQnd2Hb0xfcisRPKnbJsYwTea%2BWWSezjteJAiOlLXk68srybtQZCOpB9POQU0wKFgWcE7pby1L8DmZHSe9OotUjO4igWQlFaiuY%2FwoZs%2BrDzW5MiNO9tlGSp0CcRX7QRYh6jsk53yu5Nx9MwW4D5%2BETcnDYZ%2BEtIIj%2BgUmV3n88PbWhyO5pFTVcTDVpV6rLa%2Bjh8kca8T4Ozyipu43QzaCMM%2B3%2F9IGOqUBIVbhMKHLyVhO8tytTLdKQ4RoO0LAF4vgx3C2RGmePB5g0AZIw3bw7Dy0VgxoP%2FMB7C2G%2FENcPKua%2BUnq7MOWvUnz8Dx90njBL2HEmuiOygaZh8AgIfWFax8rBi18SemulmJ46ZR1u4Shm8IgCOGfrlkFOIWD0hq8D8du8RVxkmnaA17AlLmGrGseohggyOXd1QXEZ2rm9oCwEeYOy8mgozH0%2BRpM&X-Amz-Signature=e24e12705fd93728b77dc3438b6965f57ac8e0f103d6db9448f99ebdb8a8af7f&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

**概述**

何为热点？热点即经常访问的数据。很多时候我们希望统计某个热点数据中访问频次最高的 Top K 数据，并对其访问进行限制。比如：

商品 ID 为参数，统计一段时间内最常购买的商品 ID 并进行限制

用户 ID 为参数，针对一段时间内频繁访问的用户 ID 进行限制

热点参数限流会统计传入参数中的热点参数，并根据配置的限流阈值与模式，对包含热点参数的资源调用进行限流。热点参数限流可以看做是一种特殊的流量控制，仅对包含热点参数的资源调用生效。

Sentinel 利用 LRU 策略统计最近最常访问的热点参数，结合令牌桶算法来进行参数级别的流控。

**基本使用**

要使用热点参数限流功能，需要引入以下依赖：

```java
<dependency>
					<groupId>com.alibaba.csp</groupId>
					<artifactId>sentinel-parameter-flow-control</artifactId>
					<version>x.y.z</version>
</dependency>
```


然后为对应的资源配置热点参数限流规则，并在 entry 的时候传入相应的参数，即可使热点参数限流生效。

注：若自行扩展并注册了自己实现的 SlotChainBuilder，并希望使用热点参数限流功能，则可以在 chain 里面合适的地方插入 ParamFlowSlot。

那么如何传入对应的参数以便 Sentinel 统计呢？我们可以通过 SphU 类里面几个 entry 重载方法来传入：

```java
public static Entry entry(String name, EntryType type, int count, Object... args) throws BlockException

public static Entry entry(Method method, EntryType type, int count, Object... args) throws BlockException
```

其中最后的一串 args 就是要传入的参数，有多个就按照次序依次传入。比如要传入两个参数 paramA 和 paramB，则可以：

```java
// paramA in index 0, paramB in index 1.

// 若需要配置例外项或者使用集群维度流控，则传入的参数只支持基本类型。

SphU.entry(resourceName, EntryType.IN, 1, paramA, paramB);
```


注意：若 entry 的时候传入了热点参数，那么 exit 的时候也一定要带上对应的参数（exit(count, args)），否则可能会有统计错误。正确的示例：

```java
Entry entry = null;

try {

				entry = SphU.entry(resourceName, EntryType.IN, 1, paramA, paramB);

					// Your logic here.
					
					} catch (BlockException ex) {
					
					// Handle request rejection.
					
					} finally {
					
					if (entry != null) {
					
					entry.exit(1, paramA, paramB);
					
					}
					
}
```

对于 @SentinelResource 注解方式定义的资源，若注解作用的方法上有参数，Sentinel 会将它们作为参数传入 SphU.entry(res, args)。比如以下的方法里面 uid 和 type 会分别作为第一个和第二个参数传入 Sentinel API，从而可以用于热点规则判断：

```java
@SentinelResource("myMethod")

public Result doSomething(String uid, int type) {

     // some logic here...

}
```


**热点参数规则**

热点参数规则（ParamFlowRule）类似于流量控制规则（FlowRule）：

属性 说明 默认值

我们可以通过 ParamFlowRuleManager 的 loadRules 方法更新热点参数规则，下面是一个热点流控规则：

```java
ParamFlowRule rule = new ParamFlowRule(resourceName)

.setParamIdx(0)

.setCount(5);

// 针对 int 类型的参数 PARAM_B，单独设置限流 QPS 阈值为 10，而不是全局的阈值 5.

ParamFlowItem item = new ParamFlowItem().setObject(String.valueOf(PARAM_B))

.setClassType(int.class.getName())

.setCount(10);

rule.setParamFlowItemList(Collections.singletonList(item));

ParamFlowRuleManager.loadRules(Collections.singletonList(rule));
```

示例

示例可参见 [sentinel-demo-parameter-flow-control](https://github.com/alibaba/Sentinel/blob/master/sentinel-demo/sentinel-demo-parameter-flow-control/src/main/java/com/alibaba/csp/sentinel/demo/flow/param/ParamFlowQpsDemo.java)。

输出结果：

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
package com.alibaba.csp.sentinel.demo.flow.param;

import java.util.Collections;

import com.alibaba.csp.sentinel.slots.block.RuleConstant;
import com.alibaba.csp.sentinel.slots.block.flow.param.ParamFlowItem;
import com.alibaba.csp.sentinel.slots.block.flow.param.ParamFlowRule;
import com.alibaba.csp.sentinel.slots.block.flow.param.ParamFlowRuleManager;

/**
 * This demo demonstrates flow control by frequent ("hot spot") parameters.
 *
 * @author Eric Zhao
 * @since 0.2.0
 */
public class ParamFlowQpsDemo {

    private static final int PARAM_A = 1;
    private static final int PARAM_B = 2;
    private static final int PARAM_C = 3;
    private static final int PARAM_D = 4;

    /**
     * Here we prepare different parameters to validate flow control by parameters.
     */
    private static final Integer[] PARAMS = new Integer[] {PARAM_A, PARAM_B, PARAM_C, PARAM_D};

    private static final String RESOURCE_KEY = "resA";

    public static void main(String[] args) throws Exception {
        initParamFlowRules();

        final int threadCount = 20;
        ParamFlowQpsRunner<Integer> runner = new ParamFlowQpsRunner<>(PARAMS, RESOURCE_KEY, threadCount, 120);
        runner.tick();

        Thread.sleep(1000);
        runner.simulateTraffic();
    }

    private static void initParamFlowRules() {
        // QPS mode, threshold is 5 for every frequent "hot spot" parameter in index 0 (the first arg).
        ParamFlowRule rule = new ParamFlowRule(RESOURCE_KEY)
            .setParamIdx(0)
            .setGrade(RuleConstant.FLOW_GRADE_QPS)
            //.setDurationInSec(3)
            //.setControlBehavior(RuleConstant.CONTROL_BEHAVIOR_RATE_LIMITER)
            //.setMaxQueueingTimeMs(600)
            .setCount(5);

        // We can set threshold count for specific parameter value individually.
        // Here we add an exception item. That means: QPS threshold of entries with parameter `PARAM_B` (type: int)
        // in index 0 will be 10, rather than the global threshold (5).
        ParamFlowItem item = new ParamFlowItem().setObject(String.valueOf(PARAM_B))
            .setClassType(int.class.getName())
            .setCount(10);
        rule.setParamFlowItemList(Collections.singletonList(item));
        ParamFlowRuleManager.loadRules(Collections.singletonList(rule));
    }
}
```

[image](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/126287f6-ac08-4de0-ba04-d53c0eb21377/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YNPDM6WY%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T225831Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDoYh%2Flg6E4XajN1b13EfXcMxWNbqQXe9i%2BvH71GePW6AIgKHvgePrPk5Aw5a6CMlDJEQRioJscjWgxFa%2B7uId7%2BU8qiAQIxv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDNpltXqIqYlDj4eVJyrcA9GIZ4HwCk7bdm4wKlEbnXM33ZyIMwRuxGeOjXeQh%2FSLGzDlqRjxcCXZ04VHTs07OPE%2B3GOfD%2FsLXd7L%2BZ7t7YNjXX2zt%2FY9attFsxA5zBFT6rmUpukRb1Y1vGJNzHDskygdwu56iQdyPjsq%2BkcIbtX4HdF2cEcOjpEp6U6HCShd98nnUnw4OASFQwzDv%2BZT%2BxrGidzNpoHXlRTk078f%2Bm7kQRJhOSTHG6AgNO2VdlZqbu9BXTiEPXBoEOAUIjiuFsGFoPyviyJEjR7LcdinqXuaBrbT6P%2FV1L6nkJVubOm2Yp%2BbGscoz4IlSJBhJ9qr67SEsT9LvNwWUAUw7qkcspiiciV1o6FdODBVWFDQ%2F%2FzKdTEP3K5Cz2tyffSjvmdmYF2HOCuFsn8CdO7Z0nAPoh6vhMfprwgxa5J5k1RQnd2Hb0xfcisRPKnbJsYwTea%2BWWSezjteJAiOlLXk68srybtQZCOpB9POQU0wKFgWcE7pby1L8DmZHSe9OotUjO4igWQlFaiuY%2FwoZs%2BrDzW5MiNO9tlGSp0CcRX7QRYh6jsk53yu5Nx9MwW4D5%2BETcnDYZ%2BEtIIj%2BgUmV3n88PbWhyO5pFTVcTDVpV6rLa%2Bjh8kca8T4Ozyipu43QzaCMM%2B3%2F9IGOqUBIVbhMKHLyVhO8tytTLdKQ4RoO0LAF4vgx3C2RGmePB5g0AZIw3bw7Dy0VgxoP%2FMB7C2G%2FENcPKua%2BUnq7MOWvUnz8Dx90njBL2HEmuiOygaZh8AgIfWFax8rBi18SemulmJ46ZR1u4Shm8IgCOGfrlkFOIWD0hq8D8du8RVxkmnaA17AlLmGrGseohggyOXd1QXEZ2rm9oCwEeYOy8mgozH0%2BRpM&X-Amz-Signature=f1db3018d32309c3577a7632d33d52e57b90f38015ffe4f8b5201c85e93fdfd9&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)


