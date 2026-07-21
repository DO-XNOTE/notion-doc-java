---
title: 1-17 哨兵SpringAOP注解方式应用-2
---

# 1-17 哨兵SpringAOP注解方式应用-2

[image](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/1b455b0f-7c26-417e-a407-b50edd764073/SCR-20240722-sdad.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666RPASHH2%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T225837Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDoOnl4OObQMxr00mrtANNDjfw050CgBcq0qw5vTAvG2QIgMnIV9MQoCX0I12prF78a5NDBXMROGq7%2BtM0TvNglHKsqiAQIxv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDAIaZwNYkGpl99Z8RircA2v3UpGjQ%2BCxI3SNZGpUAO4r6W3Z0JdYrqEOKgDIXiUFusjldCcSLIy%2Bd9aPGe40H9ueq%2Fo8frQZrsHE1U6H7hCWxrdIra1aH20MFj8Q8TIadasSBqpTzStBiKGZBB%2FzSSVjTI%2Fpd2ntA2ArBxEt3uvWKCmzTnRCVdvYPbuRQRB58gn1WDjWvuIDe0qi7SdyMuolg6st0YtBfy49MdQ8ojpZgo23YykZ1y4NUknkVgo%2BlBvccfC%2FuaJR86aI19O7813owOMH3Jgj6O2lfNTiHc%2FFLyZipqfVaylW4yJD4uBxkEiQksEtnLfo9zOOW4YSaBEEcyi58KF5fYlKB62UCNhV7e7pTclPbx0nIRrYfx%2BaXOY36dIvJHrs0rDd8xHjTiR5Yg6bGvcb1prlg5O%2FuaaXUSa1GitBsIsgG77HBL4pKJn9OAvTC9PqucG08z9qIL9WjMhQfSprXQ8PSf5GKxKWgM4UIAzek3xSQeTFLCieJKUCkCSI6kGtb228ga4iWHS6z%2Fjxf7DPEdejOJb3na5I6RX9qWbxh7BZcXkmjJO%2BvXeLf5e259KC%2BHchWcmy%2BfP0l9%2BsyL1hGS8u6sE8Yar0Mi1S6GrhgNhhS5GSM1W9R3LmEJKrr%2BWQssE6MIe3%2F9IGOqUBb5NrVt%2Fv71tOZd1ETJZRvgMcwPXIBoYTe4rzqkysEw4Do8C5nZIBZmH50kAUuKLwipyIiP1sSrHwJnlZYxTDTqGaZh0q8YN5amg1t9a%2FaKOTG5e5pGq6As2cvI8dGCBBACH23G%2Beunf2R8ce%2FK%2BSlFfo7V%2BUfGdHaQjuXOaoHtvuHEx5jY%2FjPRtWqSl5A3RZpvwemkKlmWpgqQbQ5%2BIb0NCVHaN3&X-Amz-Signature=52de538a7feff06475cfd2f16af4724d4bdf83595e438c16b4ffa7314d157f97&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

[image](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/1b50dfda-3e34-45f9-886e-3b71fbf70c85/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666RPASHH2%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T225837Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDoOnl4OObQMxr00mrtANNDjfw050CgBcq0qw5vTAvG2QIgMnIV9MQoCX0I12prF78a5NDBXMROGq7%2BtM0TvNglHKsqiAQIxv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDAIaZwNYkGpl99Z8RircA2v3UpGjQ%2BCxI3SNZGpUAO4r6W3Z0JdYrqEOKgDIXiUFusjldCcSLIy%2Bd9aPGe40H9ueq%2Fo8frQZrsHE1U6H7hCWxrdIra1aH20MFj8Q8TIadasSBqpTzStBiKGZBB%2FzSSVjTI%2Fpd2ntA2ArBxEt3uvWKCmzTnRCVdvYPbuRQRB58gn1WDjWvuIDe0qi7SdyMuolg6st0YtBfy49MdQ8ojpZgo23YykZ1y4NUknkVgo%2BlBvccfC%2FuaJR86aI19O7813owOMH3Jgj6O2lfNTiHc%2FFLyZipqfVaylW4yJD4uBxkEiQksEtnLfo9zOOW4YSaBEEcyi58KF5fYlKB62UCNhV7e7pTclPbx0nIRrYfx%2BaXOY36dIvJHrs0rDd8xHjTiR5Yg6bGvcb1prlg5O%2FuaaXUSa1GitBsIsgG77HBL4pKJn9OAvTC9PqucG08z9qIL9WjMhQfSprXQ8PSf5GKxKWgM4UIAzek3xSQeTFLCieJKUCkCSI6kGtb228ga4iWHS6z%2Fjxf7DPEdejOJb3na5I6RX9qWbxh7BZcXkmjJO%2BvXeLf5e259KC%2BHchWcmy%2BfP0l9%2BsyL1hGS8u6sE8Yar0Mi1S6GrhgNhhS5GSM1W9R3LmEJKrr%2BWQssE6MIe3%2F9IGOqUBb5NrVt%2Fv71tOZd1ETJZRvgMcwPXIBoYTe4rzqkysEw4Do8C5nZIBZmH50kAUuKLwipyIiP1sSrHwJnlZYxTDTqGaZh0q8YN5amg1t9a%2FaKOTG5e5pGq6As2cvI8dGCBBACH23G%2Beunf2R8ce%2FK%2BSlFfo7V%2BUfGdHaQjuXOaoHtvuHEx5jY%2FjPRtWqSl5A3RZpvwemkKlmWpgqQbQ5%2BIb0NCVHaN3&X-Amz-Signature=9575994509ef50c983699a4872e2f7d41f5f194cbc83f0943252d41f16ab8f3e&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

那它不是把异常放到另外的一个类里了，它都是在本类里的。我们看一下这种形式，代码比较多。好，我们首先来看它是 at sentinel resource 它的 value 是 hello 然后它的 fail back 叫做 hello fail back 然后它这里边说如果 S 小于 0 的时候，然后我去 throws 一个非法的参数异常，它说 invalidate X 然后要不然的话就可以去解析。




那么来看看这个东西是什么意思吗？正常逻辑我肯定是直接 return 了，如果抛异常了会往这抛异常。但是如果降级了，降级了的话它就会走 fail bix 对应的函数，这个名字一定要一致，我们 ctrl C control V 找到。好，就这个函数，同学们请看这个函数叫做 hello feel back 跟我这个名字一定要保证一致，并且它里边的参数类型看见了吗？方法的这个权限都是 public 返回值类型都是 string 并且参数也必须要一致。你这里边有一个参数浪 S 我这里边也必须要有一个浪 S 我把这个方法提到前面去就搞得太后面了，看就别扭，我们这样去对比了。


好，这个就是对应的这个 feel back 降级的函数，看见了吧，它只允许多一个参数，就是说你降级的时候如果抛异常了，那我是不是可以把 exception 给你带过来，这是可以的。然后我在这里可以做一些降级的手段看见了吧，这是其中的一种用法，只用 fail back 的时候，当然它告诉你还有其他用法，比如说这里边叫做 hello another hello another ，我们来看一看。它有一个 default fail back 这个 default fail back 名称一定要跟它是一致的，但是 default fell back 我可以不写那个传的参数，这是可以的。然后这里边也是对应着给你个例子，就是 exceptions to excellent 就是忽略的一场，就是说我可以忽略这种非法的状态这种 exception 如果说抛出这种异常的时候，我可以忽略我不计入我的这个失败，就是我的降级的时候，我忽略这种 exception 这是可以去做到的，它里边可以多一个这种参数配置，这是 1.6 以后给我们提供的。

```java
@Configuration
public class AopConfiguration {

    @Bean
    public SentinelResourceAspect sentinelResourceAspect() {
        return new SentinelResourceAspect();
    }
}
```

[image](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/0119900a-c62a-4df5-a153-7a80a310ef83/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666RPASHH2%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T225837Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDoOnl4OObQMxr00mrtANNDjfw050CgBcq0qw5vTAvG2QIgMnIV9MQoCX0I12prF78a5NDBXMROGq7%2BtM0TvNglHKsqiAQIxv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDAIaZwNYkGpl99Z8RircA2v3UpGjQ%2BCxI3SNZGpUAO4r6W3Z0JdYrqEOKgDIXiUFusjldCcSLIy%2Bd9aPGe40H9ueq%2Fo8frQZrsHE1U6H7hCWxrdIra1aH20MFj8Q8TIadasSBqpTzStBiKGZBB%2FzSSVjTI%2Fpd2ntA2ArBxEt3uvWKCmzTnRCVdvYPbuRQRB58gn1WDjWvuIDe0qi7SdyMuolg6st0YtBfy49MdQ8ojpZgo23YykZ1y4NUknkVgo%2BlBvccfC%2FuaJR86aI19O7813owOMH3Jgj6O2lfNTiHc%2FFLyZipqfVaylW4yJD4uBxkEiQksEtnLfo9zOOW4YSaBEEcyi58KF5fYlKB62UCNhV7e7pTclPbx0nIRrYfx%2BaXOY36dIvJHrs0rDd8xHjTiR5Yg6bGvcb1prlg5O%2FuaaXUSa1GitBsIsgG77HBL4pKJn9OAvTC9PqucG08z9qIL9WjMhQfSprXQ8PSf5GKxKWgM4UIAzek3xSQeTFLCieJKUCkCSI6kGtb228ga4iWHS6z%2Fjxf7DPEdejOJb3na5I6RX9qWbxh7BZcXkmjJO%2BvXeLf5e259KC%2BHchWcmy%2BfP0l9%2BsyL1hGS8u6sE8Yar0Mi1S6GrhgNhhS5GSM1W9R3LmEJKrr%2BWQssE6MIe3%2F9IGOqUBb5NrVt%2Fv71tOZd1ETJZRvgMcwPXIBoYTe4rzqkysEw4Do8C5nZIBZmH50kAUuKLwipyIiP1sSrHwJnlZYxTDTqGaZh0q8YN5amg1t9a%2FaKOTG5e5pGq6As2cvI8dGCBBACH23G%2Beunf2R8ce%2FK%2BSlFfo7V%2BUfGdHaQjuXOaoHtvuHEx5jY%2FjPRtWqSl5A3RZpvwemkKlmWpgqQbQ5%2BIb0NCVHaN3&X-Amz-Signature=987aa7d08273f51f9f6cf79cc3ad5594ed92a1f28f5d73c10f6915097d7fb426&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
package com.alibaba.csp.sentinel.annotation.aspectj;

import com.alibaba.csp.sentinel.Entry;
import com.alibaba.csp.sentinel.EntryType;
import com.alibaba.csp.sentinel.SphU;
import com.alibaba.csp.sentinel.annotation.SentinelResource;
import com.alibaba.csp.sentinel.slots.block.BlockException;
import org.aspectj.lang.ProceedingJoinPoint;
import org.aspectj.lang.annotation.Around;
import org.aspectj.lang.annotation.Aspect;
import org.aspectj.lang.annotation.Pointcut;

import java.lang.reflect.Method;

/**
 * Aspect for methods with {@link SentinelResource} annotation.
 *
 * @author Eric Zhao
 */
@Aspect
public class SentinelResourceAspect extends AbstractSentinelAspectSupport {

    @Pointcut("@annotation(com.alibaba.csp.sentinel.annotation.SentinelResource)")
    public void sentinelResourceAnnotationPointcut() {
    }

    @Around("sentinelResourceAnnotationPointcut()")
    public Object invokeResourceWithSentinel(ProceedingJoinPoint pjp) throws Throwable {
        Method originMethod = resolveMethod(pjp);

        SentinelResource annotation = originMethod.getAnnotation(SentinelResource.class);
        if (annotation == null) {
            // Should not go through here.
            throw new IllegalStateException("Wrong state for SentinelResource annotation");
        }
        String resourceName = getResourceName(annotation.value(), originMethod);
        EntryType entryType = annotation.entryType();
        int resourceType = annotation.resourceType();
        Entry entry = null;
        try {
            entry = SphU.entry(resourceName, resourceType, entryType, pjp.getArgs());
            return pjp.proceed();
        } catch (BlockException ex) {
            return handleBlockException(pjp, annotation, ex);
        } catch (Throwable ex) {
            Class<? extends Throwable>[] exceptionsToIgnore = annotation.exceptionsToIgnore();
            // The ignore list will be checked first.
            if (exceptionsToIgnore.length > 0 && exceptionBelongsTo(ex, exceptionsToIgnore)) {
                throw ex;
            }
            if (exceptionBelongsTo(ex, annotation.exceptionsToTrace())) {
                traceException(ex);
                return handleFallback(pjp, annotation, ex);
            }

            // No fallback function can handle the exception, so throw it out.
            throw ex;
        } finally {
            if (entry != null) {
                entry.exit(1, pjp.getArgs());
            }
        }
    }
}
```

好了，大体上小伙伴们就明白它的这个最基本的注解使用了是它最基本的一个使用的方式。那么我们现在是不是也可以去按照这种东西自己去写一写呢？没问题，我们现在就是按照它的这规则我们自己来写一写。这里边这个 lop config ，我完全把它 copy 过来就可以了没什么可说的。当然它官网已经告诉你了，你只要把这段代码 copy 过来就可以了。 lop 的方式，我们自己的这个 demo test 那我在这里可以直接 control V 粘进来。有了这个类之后，我们 control U 加 O 把对应的包都导进来。第一件事情，引入对应的依赖，引完对应的依赖之后马上把这个引进来。只有引进来，它才有切面的植入点。那我们来看看这个东西底层怎么实现的，这底层怎么实现的？我们来点进去。

[image](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/335d3ca9-ba38-4a5a-b69e-2fa2a746aa5d/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666RPASHH2%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T225837Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDoOnl4OObQMxr00mrtANNDjfw050CgBcq0qw5vTAvG2QIgMnIV9MQoCX0I12prF78a5NDBXMROGq7%2BtM0TvNglHKsqiAQIxv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDAIaZwNYkGpl99Z8RircA2v3UpGjQ%2BCxI3SNZGpUAO4r6W3Z0JdYrqEOKgDIXiUFusjldCcSLIy%2Bd9aPGe40H9ueq%2Fo8frQZrsHE1U6H7hCWxrdIra1aH20MFj8Q8TIadasSBqpTzStBiKGZBB%2FzSSVjTI%2Fpd2ntA2ArBxEt3uvWKCmzTnRCVdvYPbuRQRB58gn1WDjWvuIDe0qi7SdyMuolg6st0YtBfy49MdQ8ojpZgo23YykZ1y4NUknkVgo%2BlBvccfC%2FuaJR86aI19O7813owOMH3Jgj6O2lfNTiHc%2FFLyZipqfVaylW4yJD4uBxkEiQksEtnLfo9zOOW4YSaBEEcyi58KF5fYlKB62UCNhV7e7pTclPbx0nIRrYfx%2BaXOY36dIvJHrs0rDd8xHjTiR5Yg6bGvcb1prlg5O%2FuaaXUSa1GitBsIsgG77HBL4pKJn9OAvTC9PqucG08z9qIL9WjMhQfSprXQ8PSf5GKxKWgM4UIAzek3xSQeTFLCieJKUCkCSI6kGtb228ga4iWHS6z%2Fjxf7DPEdejOJb3na5I6RX9qWbxh7BZcXkmjJO%2BvXeLf5e259KC%2BHchWcmy%2BfP0l9%2BsyL1hGS8u6sE8Yar0Mi1S6GrhgNhhS5GSM1W9R3LmEJKrr%2BWQssE6MIe3%2F9IGOqUBb5NrVt%2Fv71tOZd1ETJZRvgMcwPXIBoYTe4rzqkysEw4Do8C5nZIBZmH50kAUuKLwipyIiP1sSrHwJnlZYxTDTqGaZh0q8YN5amg1t9a%2FaKOTG5e5pGq6As2cvI8dGCBBACH23G%2Beunf2R8ce%2FK%2BSlFfo7V%2BUfGdHaQjuXOaoHtvuHEx5jY%2FjPRtWqSl5A3RZpvwemkKlmWpgqQbQ5%2BIb0NCVHaN3&X-Amz-Signature=90d3b569b45af981e21808fa078892940a98d0c1479659e6f7bacf51d7c9b96f&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)


这个注解叫做 at sentinel resource 它这个里边叫做 com 点阿里巴巴点 csp.sentinel.annotation.sentinel resource 我们直接找到这个类，它是在铐包下的，它自己声明定义了一个这个自定义的注解，然后里边有一些对应的属性，大家都可以看到有这么多。然后它对应的这个切面就是对于这个注解的切面就是在我们的扩展类里边，也就是说这个 annotation 杠 sxg 这个扩展类里边有的它直接做了一个 point cut 这么一个切面。然后有一个这个环绕式的这种，在前方法后做一些自己的 LP 处理，怎么去做的呢？我们来最大化来看一下这里边首先它会做的一件事情，就是叫做 receiver method 就是方法。

[image](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/a511a182-cb3e-4632-88e5-a3582890e518/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666RPASHH2%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T225837Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDoOnl4OObQMxr00mrtANNDjfw050CgBcq0qw5vTAvG2QIgMnIV9MQoCX0I12prF78a5NDBXMROGq7%2BtM0TvNglHKsqiAQIxv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDAIaZwNYkGpl99Z8RircA2v3UpGjQ%2BCxI3SNZGpUAO4r6W3Z0JdYrqEOKgDIXiUFusjldCcSLIy%2Bd9aPGe40H9ueq%2Fo8frQZrsHE1U6H7hCWxrdIra1aH20MFj8Q8TIadasSBqpTzStBiKGZBB%2FzSSVjTI%2Fpd2ntA2ArBxEt3uvWKCmzTnRCVdvYPbuRQRB58gn1WDjWvuIDe0qi7SdyMuolg6st0YtBfy49MdQ8ojpZgo23YykZ1y4NUknkVgo%2BlBvccfC%2FuaJR86aI19O7813owOMH3Jgj6O2lfNTiHc%2FFLyZipqfVaylW4yJD4uBxkEiQksEtnLfo9zOOW4YSaBEEcyi58KF5fYlKB62UCNhV7e7pTclPbx0nIRrYfx%2BaXOY36dIvJHrs0rDd8xHjTiR5Yg6bGvcb1prlg5O%2FuaaXUSa1GitBsIsgG77HBL4pKJn9OAvTC9PqucG08z9qIL9WjMhQfSprXQ8PSf5GKxKWgM4UIAzek3xSQeTFLCieJKUCkCSI6kGtb228ga4iWHS6z%2Fjxf7DPEdejOJb3na5I6RX9qWbxh7BZcXkmjJO%2BvXeLf5e259KC%2BHchWcmy%2BfP0l9%2BsyL1hGS8u6sE8Yar0Mi1S6GrhgNhhS5GSM1W9R3LmEJKrr%2BWQssE6MIe3%2F9IGOqUBb5NrVt%2Fv71tOZd1ETJZRvgMcwPXIBoYTe4rzqkysEw4Do8C5nZIBZmH50kAUuKLwipyIiP1sSrHwJnlZYxTDTqGaZh0q8YN5amg1t9a%2FaKOTG5e5pGq6As2cvI8dGCBBACH23G%2Beunf2R8ce%2FK%2BSlFfo7V%2BUfGdHaQjuXOaoHtvuHEx5jY%2FjPRtWqSl5A3RZpvwemkKlmWpgqQbQ5%2BIb0NCVHaN3&X-Amz-Signature=eb34b198ddd5241759fde576b758eacdf9bdc136673cb0f07c0992e1ea2c0276&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)


解析什么方法呢？我们看一看，这个 PGP 给我传进来了之后，我去解析方法返回一个叫做原方法，这个方法其实就是通过反射去做的，大家可以有兴趣可以看一看，这都是最简单的什么 declare method for 然后这里边你可以看到这个方法做什么事情，直接通过反射取到它的这个 declare method 然后把它的这个具体的 method 返回回去了。这块就是获取方法。然后获取这个方法上所对应的这个 annotation 取到这个 sentinel resource 然后判断这个 annotation 是否为空。如果为空的话，那我就直接抛异常了。如果不为空，我去 get resource name 获取资源的这个 value 这个 value 不就说了，就是那个资源。然后你看这个里面的写法这个里边的写法之前他说如果 is not blank 直接返回，就是说你的这个 value 那块它那个文档上说就不允许为空。我们来看一看。就在这说不能为空，其实也可以为空。因为什么呢？如果不为空的话，直接把资源名称返回，就变成我们的资源名了。


如果为空怎么做的？它是调用这个 reserver method name 去的，就做一个，使用反射的方式去把那个在得到的 declare class get name 什么的，就是说这个是非常非常浪费我们的性能的。所以说官方它取的就是那个方法那个名字，就是你加上那个艾特 sentence resource 之后，那个方法的名字是什么，它就是什么。但一般来讲千万不要走到这，走到这儿它的性能会很受影响。所以一般来讲我们都是建议大家一定要在这个 y6 上去配好资源的名词，在这配好就好了。


然后取到这个资源名称之后，接下来的事情你看这个代码是不是一样的，就是调用它的这个 sphu.entry 然后把资源名称什么的都放进里边，然后把它对应声明的这个我的 entry type 到底是 in 还是 out 取到。然后这个 1 就是它的这个说白了，就是它的 count 每次去加多少也写到这。然后最后一个参数就是我们的这个其他的额外参数就是 p2p.get X 当然这是一个 object 的数组。然后接下来就执行这个方法看见了吧，就是在方法执行之前加了一个统计，然后执行方法返回结果。然后在 block 的时候，在出现异常的时候， catch 住我们的最大的异常就是 block exception 然后在 block exception 的时候去做回调，做 handler block exception 的回调。这个 handler block exception 其实它就是我们之前所说的就是我们在那个注解上声明的，你看他这个 inwork 就是一个回调，我在这里就不领着小伙伴们详细去看了。


然后再往下看，就是在 catch throttle 的时候，当然这是我正常的的逻辑，流控，它肯定会走这个然后去调降级的策略。然后如果抛这个 throbe 的时候，它需要判断。你看从你的这个 annotation 的注解里去取出来。你忽略的所有的 annotation 的数组，你忽略的哪些异常我都会把你取出来。然后这个忽略的 Lens 大于零，并且它就是什么 belong 就是 exception belongs to 这个时候他说我直接 return ex 要不然的话干什么我直接去调用，就是说忽略的话我就直接抛异常，忽略的话我就直接你该什么异常，我就抛什么异常。但如果，不忽略的时候他做的事情就是掉 fell back 就是直接走降级策略。在这里，所以说它这是 1.6 之后新加的一段逻辑。

[image](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/b9deb60b-110e-4af1-aa57-4d8a3609e1f6/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666RPASHH2%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T225837Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDoOnl4OObQMxr00mrtANNDjfw050CgBcq0qw5vTAvG2QIgMnIV9MQoCX0I12prF78a5NDBXMROGq7%2BtM0TvNglHKsqiAQIxv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDAIaZwNYkGpl99Z8RircA2v3UpGjQ%2BCxI3SNZGpUAO4r6W3Z0JdYrqEOKgDIXiUFusjldCcSLIy%2Bd9aPGe40H9ueq%2Fo8frQZrsHE1U6H7hCWxrdIra1aH20MFj8Q8TIadasSBqpTzStBiKGZBB%2FzSSVjTI%2Fpd2ntA2ArBxEt3uvWKCmzTnRCVdvYPbuRQRB58gn1WDjWvuIDe0qi7SdyMuolg6st0YtBfy49MdQ8ojpZgo23YykZ1y4NUknkVgo%2BlBvccfC%2FuaJR86aI19O7813owOMH3Jgj6O2lfNTiHc%2FFLyZipqfVaylW4yJD4uBxkEiQksEtnLfo9zOOW4YSaBEEcyi58KF5fYlKB62UCNhV7e7pTclPbx0nIRrYfx%2BaXOY36dIvJHrs0rDd8xHjTiR5Yg6bGvcb1prlg5O%2FuaaXUSa1GitBsIsgG77HBL4pKJn9OAvTC9PqucG08z9qIL9WjMhQfSprXQ8PSf5GKxKWgM4UIAzek3xSQeTFLCieJKUCkCSI6kGtb228ga4iWHS6z%2Fjxf7DPEdejOJb3na5I6RX9qWbxh7BZcXkmjJO%2BvXeLf5e259KC%2BHchWcmy%2BfP0l9%2BsyL1hGS8u6sE8Yar0Mi1S6GrhgNhhS5GSM1W9R3LmEJKrr%2BWQssE6MIe3%2F9IGOqUBb5NrVt%2Fv71tOZd1ETJZRvgMcwPXIBoYTe4rzqkysEw4Do8C5nZIBZmH50kAUuKLwipyIiP1sSrHwJnlZYxTDTqGaZh0q8YN5amg1t9a%2FaKOTG5e5pGq6As2cvI8dGCBBACH23G%2Beunf2R8ce%2FK%2BSlFfo7V%2BUfGdHaQjuXOaoHtvuHEx5jY%2FjPRtWqSl5A3RZpvwemkKlmWpgqQbQ5%2BIb0NCVHaN3&X-Amz-Signature=4aa8d93fa92a5f1605414c3d212e2c45abdb8c91daff2442e9a861249eda571a&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)


当你排除这个异常，那我就直接把这个异常抛出就好了，你抛多少次我都不管你，我认为你这是你业务的一场。当然如果你不排除的话，那你抛的次数多了，我可以选择降级走到降级的这个 feel back handler 就这么一个事情好了，然后最后 finally 的时候去做退出，这就是它核心的 aspect G 的切面的这么一个核心的逻辑，其实非常简单。


然后其实你可以看到它其它的，比如说 abstract sentence 这个 support 可以看到它的这个对应的一些这些。怎么说，这些就是对于那个类的一些支持，它们两个是一个父子关系。 Ok. 然后这是对应的 method wiper 就是对方法进行包裹的这么一个类。然后在这里边有一个叫做 resource metadata registry 就我们自己所声明的什么 fail back 就是异常信息，包括这个 block handler 那些东西，它都会帮我们去做一个缓存，缓存到一个 concurrent map 中 concurrent map 里边。然后把对应的你的资源以及这个资源所对应的 feel back 的 method 进行一个什么进行一个 KV 的这么一个存储。然后在抛出异常的时候，我去获取指定的你的哪个资源，下面的哪个方法，然后去做一个回调，就这么一个事情。


其实这个就是把你所定义的一些异常的内容帮你去缓存起来了。就是我没必要说每次我初始化的时候，我就通过反射都已经把降级的方法都已经缓存到 map 中了。然后你出现降级的异常的时候，直接从 map 里边取直接 execute 执行或者是 inwork 执行一下就好了，没必要说在线通过反射去做，这样的话它也浪费性能。


OK 那这就是大体它的这个 aspect G 它那个扩展的点的这么一个源码分析。我现在就以我们的我再加一个叫做service 。再加一个 service 这个 service 比如说我们就叫做什么流控的 service follow service 好了，我也不说不写那个接口了，我就认为它是一个 at service 就好了，就是一个 sprint service。 Ok. 然后里边有什么方法先不关注，我们先把这个 controller 先写好，在这里我们再来一个新的什么新的controller 。这个 controller 我们叫做 sentence annotation 


controller 这样的话小伙伴在复习的时候或者是在看老师的代码的时候，你一直直接知道，这就是关于 annotation 的一个小练习了。然后 rest controller 在这里边我们写 public 然后 string 返回的我们给一个咱们叫做 follow test 。好，这里边我的 value 就叫什么，就叫做 follow guard test 这样就可以了。然后我去调具体的那个 service 是哪个 service 叫 follow service 把它直接引进来，在这里边直接 out wired 然后 follow service 直接引进来声明成 private 好，然后我想直接调它的一个方法，然后最后返回结果就好了，直接点 follow 这个方法就叫follow 。然后把它这个 great method 。
创建好了 method 之后，我们现在怎么去做？第一步就是 at sentinel resource resource 然后去加我们自己的注解就好了。首先第一个最关键的是 value 这个 y6 属性应该怎么去叫呢？一般来讲就是权限命名看见了吗？权限命名，然后加上你的方法名字叫做 follow 就可以了。


好了，搞定第一个，参数搞定之后，接下来我们再看我们还缺哪些，比如说它的 entry type 是什么？它是 in 还是out ？我们可以写 entry.type 我可以写out。 Okay. 然后接下来它的这个降级策略它应该怎么去做，如果是降级的话就是 block handler 当然这个 block handler 你可以去起个名字叫做什么叫做 follow block handler 这你自己随便去起就可以了，我们就叫做 follow block handler 然后当然这个方法你可以用一个它里边所说的叫做 block handler class 你可以把这个方法自己再定义一个类，用静态的这个 static 关键字去修饰这个方法。当然你也可以不这样去写，你可以直接就写到这里边，是不是也可以。没关系，就之后我在这里边我再写一个类，我说我再写一个叫做 public 返回值，类型包括权限都应该一样的。


然后这个名字叫做 follow block handler 然后它可以额外多传一个参数，就是你的 exception 我们可以有一个叫做 block 的 exception 我们叫做 ex 可以去拿过来。然后在这里边降级的时候可以打印一句话，我说触发流控策略，然后进行降级。触发流控策略之后我把对应的这个 ex 打印一下，然后我在这里可以直接返回处罚流控就可以了。


Or return. 说执行流控方法就执行流控方法了吗？那什么现象情况下被流控多少呢？我这里边没说是不是。那正常情况下，我就说执行 follow 方法，正常执行 follow 方法。 OK 就打印一句话，然后这边是处罚流控的时候打印的，这句话它们两个返回的不一样，这个 follow 的时候我就返回 follow 搞定了。
现在我就已经写完了一个最简单的 demo 然后有同学说老师，那规则规则我还需要写吗？规则你不需要写打一个斜线，就是 follow test 规则我们可以通过 dashboard 去配，所以说我们不需要去写。好了，我们现在要做的事情很简单，就是把我们的但是 Bob 先起来，把我们的 dashboard run ADS Java application 就可以先起来我们的 dashboard 起来。


dashboard 以后，你看到它的所有的类都加载了之后，然后我们再启动这个 demo test 把它直接 spring boot application 就好了，加载完毕。这里边有好多规则，老师，其实想把以前的那些规则都给它删掉，我们先不要了，就是以前我们在哪里？我们在 index controller 的时候，我们在初始化的时候，在 application 的时候，我们之前的规则都是这样去写死的，我们说的都不要了，先注释掉，包括这两行先都注掉，就是说我先别搞那么多复杂的规则，我们现在就关注我们这节课所讲的这个注解方式的就好了。
好，我再次去启动起来，他虽然说执行了这个规则，下载完毕了，但是他这个里边应该是什么也没有的，因为我们这里边他什么也没有，就打印了一句话了。然后我们再回到我们这个 follow test 现在我们来观察一下这个控制台。 HTTP 冒号杠杠 local host 然后是 8080 回车，我们点登录，现在你是看不到新的这个服务，它对应的这个 dashboard 对应的这个像这样的就是这个列表的。为什么呢？因为你没访问，所以你访问一下叫 HTTP 冒号杠杠 local host 8001。然后我们访问 follow test 来回车一下。好。没问题。然后在这里我们再刷的时候你就看到了 demo test 有了，然后触点电路。你会看到直接就帮你有了这个触点电路了。


这就是它的这个是权限命名，就是这个 service.follow 当然我这个权限命名写得不太正确，因为我们要做什么？我们要做 follow test 里边的 follow 其实就是类名，这个类名还没写上去，我在这里就不重新做演示了，就你要把这个权限命名加上类名，然后冒号 follow 写上去，这才是最正确的。


OK 然后我们来看看这个我是不是可以去加一些规则，他能不能及时感知到。比如说现在我给它加一个流控策略，我说我这个单机 QPS 最多到 5 可以吧，然后点新增好了，那这样的话它这个流控已经有了，有了这个流控以后我们就可以去做测试，这里边我就多访问几次1234。我这里边就是只要我的这个刷的快一点，就能看到对应的直升流控方法了。它有返回结果吗？你会看到最多的 QPS 是5，然后它就会，触发流控它就会抛这个 follow exception 这是没问题，这是我们对应的一个 sentence resource 最简单的一个应用。 OK 那么对应着剩下的这个就简单啦。比如说我想去做降级，那你就可以写一个降级的逻辑。当然这里边除了写这个 block handler 以外，它还有一个参数是什么叫做 fail back 它还有一个 default fail backfail back 是什么意思呢？ fail back 是做降级的时候你也可以去写一个降级的方法是什么？在这里去写一样的。那他们两个谁的优先级高呢？就是如果你同时配了以后到底先走哪一个呢？那我们来看一看之前我们已经读过文档了，当这个 feel back 跟那个 handler 里边同时去都配上的时候，在这里边它有专门的这个说明。


就如果说这个 block handler 跟这个 fail back 这两个都配置了，则被限流降级，而抛出 block exception 时只会进入这个，就是你被限流了，然后导致降级的时候， block handler 它只会进入 block handler 然后去做处理。那如果没有配置 block handler fail back 和 default fail back 那则被限流降级的时候会直接抛出这个异常，抛出这个异常的时候你可以去统计，统计错的时候它肯定也是进这个 fail back 了。然后并且这有一个特殊的说明说什么说一点，6之前这个 fail back 这个函数只是针对降级它里边这个 degree 的 exception 进行处理的，不能针对于业务异常做处理。Ok.然后这里边有专门对 fail back 的说明，就是用于在抛出异常的时候提供 fail back 的逻辑处理。那之前我们说的那个 block handler 它就是针对于做降级的，比如说流控直接降级了，但是它就是针对抛出异常的时候做 fail back 处理的。
大家一定要对这两个函数它们的使用场景一定要做一个区别。在这里老师也打一个注释， do log handler 就是这个流控被降级的时候去用的流控降级的时候进入的兜底函数。这么去说。而这个什么 fail back 它是在什么在抛出异常的时候进入的兜底函数。然后同理你注意这里边有一个问题，如果你现在使用的是 1.6 之前的话，它这里面特殊有个说明，在 160 版本之前，这个 fail back 函数只针对于降级就是 degree 的 exception 进行处理，它不能针对于业务异常进行处理。但是在新版本的时候，它是针对于所有抛出的异常都可以去做兜底处理的，这是一个重要的区别。好了，那我们就是对于这个整个注解这块儿都已经讲完了。然后我们这节课先到这儿，下节课的时候我们再针对于这个 feel back 这块儿跟大家做一个讲解。感谢小伙伴们收看这节课先到这儿。


```java
<?xml version="1.0" encoding="UTF-8"?>
<project xmlns="http://maven.apache.org/POM/4.0.0"
         xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
         xsi:schemaLocation="http://maven.apache.org/POM/4.0.0 http://maven.apache.org/xsd/maven-4.0.0.xsd">
    <modelVersion>4.0.0</modelVersion>

    <groupId>com.bfxy.test</groupId>
    <artifactId>sentinel-demo-test</artifactId>
    <version>1.0-SNAPSHOT</version>

    <parent>
        <groupId>org.springframework.boot</groupId>
        <artifactId>spring-boot-starter-parent</artifactId>
        <version>2.1.5.RELEASE</version>
    </parent>

    <properties>
        <maven.compiler.source>8</maven.compiler.source>
        <maven.compiler.target>8</maven.compiler.target>
        <java.encoding>UTF-8</java.encoding>
    </properties>

    <dependencies>

        <dependency>
            <groupId>org.springframework.boot</groupId>
            <artifactId>spring-boot-starter-web</artifactId>
        </dependency>

        <dependency>
            <groupId>org.springframework.boot</groupId>
            <artifactId>spring-boot-starter-test</artifactId>
        </dependency>


        <dependency>
            <groupId>com.alibaba.csp</groupId>
            <artifactId>sentinel-core</artifactId>
            <version>1.8.6</version>
        </dependency>

        <dependency>
            <groupId>com.alibaba.csp</groupId>
            <artifactId>sentinel-transport-simple-http</artifactId>
            <version>1.8.6</version>
        </dependency>



        <dependency>
            <groupId>com.alibaba.csp</groupId>
            <artifactId>sentinel-annotation-aspectj</artifactId>
            <version>1.8.6</version>
        </dependency>

    </dependencies>

</project>
```

[image](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/f6961cc8-6df8-4974-9506-33fd92e516d0/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666RPASHH2%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T225837Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDoOnl4OObQMxr00mrtANNDjfw050CgBcq0qw5vTAvG2QIgMnIV9MQoCX0I12prF78a5NDBXMROGq7%2BtM0TvNglHKsqiAQIxv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDAIaZwNYkGpl99Z8RircA2v3UpGjQ%2BCxI3SNZGpUAO4r6W3Z0JdYrqEOKgDIXiUFusjldCcSLIy%2Bd9aPGe40H9ueq%2Fo8frQZrsHE1U6H7hCWxrdIra1aH20MFj8Q8TIadasSBqpTzStBiKGZBB%2FzSSVjTI%2Fpd2ntA2ArBxEt3uvWKCmzTnRCVdvYPbuRQRB58gn1WDjWvuIDe0qi7SdyMuolg6st0YtBfy49MdQ8ojpZgo23YykZ1y4NUknkVgo%2BlBvccfC%2FuaJR86aI19O7813owOMH3Jgj6O2lfNTiHc%2FFLyZipqfVaylW4yJD4uBxkEiQksEtnLfo9zOOW4YSaBEEcyi58KF5fYlKB62UCNhV7e7pTclPbx0nIRrYfx%2BaXOY36dIvJHrs0rDd8xHjTiR5Yg6bGvcb1prlg5O%2FuaaXUSa1GitBsIsgG77HBL4pKJn9OAvTC9PqucG08z9qIL9WjMhQfSprXQ8PSf5GKxKWgM4UIAzek3xSQeTFLCieJKUCkCSI6kGtb228ga4iWHS6z%2Fjxf7DPEdejOJb3na5I6RX9qWbxh7BZcXkmjJO%2BvXeLf5e259KC%2BHchWcmy%2BfP0l9%2BsyL1hGS8u6sE8Yar0Mi1S6GrhgNhhS5GSM1W9R3LmEJKrr%2BWQssE6MIe3%2F9IGOqUBb5NrVt%2Fv71tOZd1ETJZRvgMcwPXIBoYTe4rzqkysEw4Do8C5nZIBZmH50kAUuKLwipyIiP1sSrHwJnlZYxTDTqGaZh0q8YN5amg1t9a%2FaKOTG5e5pGq6As2cvI8dGCBBACH23G%2Beunf2R8ce%2FK%2BSlFfo7V%2BUfGdHaQjuXOaoHtvuHEx5jY%2FjPRtWqSl5A3RZpvwemkKlmWpgqQbQ5%2BIb0NCVHaN3&X-Amz-Signature=74be766fdc90853970ead20121a408e5165af6fb4d8665c6175228e74a9ea045&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

