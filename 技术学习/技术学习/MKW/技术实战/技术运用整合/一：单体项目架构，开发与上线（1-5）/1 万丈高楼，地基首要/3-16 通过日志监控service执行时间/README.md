---
title: 3-16 通过日志监控service执行时间
---

# 3-16 通过日志监控service执行时间

[image](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/cd7dde33-4b6b-4f60-be46-fa5fd74af5ee/SCR-20240816-uhjv.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SHKNXDQM%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T224633Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIFdp2WMhMOzzDtcCny%2BB95NZBSfk%2FDGtfIoNkfbxbD50AiEAsMTa1F5MOGMoCnaS1HkJ0ywDtwASWd426P%2FgdUeihDkqiAQIxv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDBBShSyDPD0oGfzA2SrcAxtxf8pLmRgkVJzUF16O%2FdsKH0kFqtQSMZGH7jxTurVNpXvKxkQ10lyOH%2F%2BMqFZlrCd%2BPcUHsWJpwaPeqRSFyaQlLgR438c%2FOoAxd%2Bh5N8Dtbjcb5oLrl%2FCmTEFyFZVCXueegFXnbw2ZcXRgdrbkc42HHIQbnCwWlt3FxR4lYoATDrqzu1kRcWfMRY6NCRX4IJaEyprgCljzDwLFEGgWtb2zAIf1rRdnObZgslF4rwLw65R5rGYLBjT%2FAp%2BI%2FWR2xWc%2Ba%2F74taAOdXhg3nVjMMEZNTnJeQdAOHVijWzYu6qERF6bNHcmXBJNKRrX9Q2%2FX0MNvQrgighvNfuNg49tozRixJv4oFIHFcdaj6qJZIUxZzx1oMcsy6UiMkrnRcmcIzpRgODLojh3bxLG142vqhcefb8IQAWdJ6L4pD1jKnDknGxgxNj18pzKlHRvAfRe%2BwRTVwdGio0O2DeyWpK%2FyFFZOAGoqnZkmvvayB8lbjIrJFcnERuw%2FyAAeJY5JHib58xFZJXNWUoAWpZJ0nwSPee3%2BvzSsj%2BKH0xIoudCtpcVs%2FkgT62M2gvK%2Fo1rlUEPmhVm9EuS5MTefGV9RCdO%2F6kMHQYApaq%2B2Z4fTbLkVQIi%2BU0qSkqZDVrlqCCGMOu4%2F9IGOqUBxIicryMTkgGI12VRZhKUJ9G0PVPg7azvQ7PBZrbOazOKRaiMms6czHPikEXralfrLBZE85mkenZpzFxrFjAyE8H3CoJmTfsUu3802JULPwDXIounbIr3VDTiP1%2BXxPczFNpPt%2FEhGzRvhUOOLH5EeUMPnkPzDEyvF6r0niZERxDdCwWIMiLEQ5fnd9XxQRDAgzqsv6GCBU2prFk4tiQLCIZMDjNE&X-Amz-Signature=76245990b3066084129f5bba63c2fdba8d0332befcd30cc871baf7b22e4ede0c&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

在项目里面，其实我们本身也已经是实现了注册和登录这两个接口，并且相应的 service 也已经是有 3 个。来看一下。要创建用户查询用户用于登录的。此外还有是根据用户名去查询用户名是否是存在的。接下来我们就可以通过日志来搞一些事情。主要我们来做什么？我们可以通过日志的不同的级别来监测每一个 service 所执行的时间。比方当一个 service 执行的时间超过了 3 秒或者更长，我们就可以打印一个 l 级别的。如果 service 运行的时间比较中等，可能会 2 秒，我们就可能报一个one。


警告一下，如果当 service 在运行的时候，它比较一般在 2 秒以下，我们可能会直接让它输出一个 infor 级别的时间就可以了。所以我们完全可以通过日志来辅助我们去记录一下每一个 service 所执行的时间。接下来我们就来实现一下。我们在这里会借助于 spring 的AOP，也就是面向切面的一个功能。好，一起来实现一下。 AOP 其实是属于 spring 部分的一个基础功能，也是 spring 的一个核心功能。要来实现AOP，其实我们就要去编写相应的切面，也就是一个切入点。


首先我们在 API 工程里面，我们先去创建一个包，招包的名称叫做aspect。好。随后在 aspect 包里面，我们再去创建一个用于辅助我们去监测日志的 aspect 切面。 service LOG。 aspect 好创建成功。创建成功以后，首先我们是需要在它的上方加上一个component，这是一个组件的注解，是需要去被扫描。此外，由于它是一个切面，我们在这个上方应该要定一个 aspect 注解。但是在我们的项目里面还没有引入相应的AOP，所以我们打开我们聚合工程的POM，我们到位置来一起引入一下。拷贝一份依赖，随后把删掉，直接可以使用一个代码补全。


来找一下有一个 a o p spring boot start a OP 双击好。

[image](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/75c50294-4aad-4bd9-883d-6a25c96cb1c3/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SHKNXDQM%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T224633Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIFdp2WMhMOzzDtcCny%2BB95NZBSfk%2FDGtfIoNkfbxbD50AiEAsMTa1F5MOGMoCnaS1HkJ0ywDtwASWd426P%2FgdUeihDkqiAQIxv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDBBShSyDPD0oGfzA2SrcAxtxf8pLmRgkVJzUF16O%2FdsKH0kFqtQSMZGH7jxTurVNpXvKxkQ10lyOH%2F%2BMqFZlrCd%2BPcUHsWJpwaPeqRSFyaQlLgR438c%2FOoAxd%2Bh5N8Dtbjcb5oLrl%2FCmTEFyFZVCXueegFXnbw2ZcXRgdrbkc42HHIQbnCwWlt3FxR4lYoATDrqzu1kRcWfMRY6NCRX4IJaEyprgCljzDwLFEGgWtb2zAIf1rRdnObZgslF4rwLw65R5rGYLBjT%2FAp%2BI%2FWR2xWc%2Ba%2F74taAOdXhg3nVjMMEZNTnJeQdAOHVijWzYu6qERF6bNHcmXBJNKRrX9Q2%2FX0MNvQrgighvNfuNg49tozRixJv4oFIHFcdaj6qJZIUxZzx1oMcsy6UiMkrnRcmcIzpRgODLojh3bxLG142vqhcefb8IQAWdJ6L4pD1jKnDknGxgxNj18pzKlHRvAfRe%2BwRTVwdGio0O2DeyWpK%2FyFFZOAGoqnZkmvvayB8lbjIrJFcnERuw%2FyAAeJY5JHib58xFZJXNWUoAWpZJ0nwSPee3%2BvzSsj%2BKH0xIoudCtpcVs%2FkgT62M2gvK%2Fo1rlUEPmhVm9EuS5MTefGV9RCdO%2F6kMHQYApaq%2B2Z4fTbLkVQIi%2BU0qSkqZDVrlqCCGMOu4%2F9IGOqUBxIicryMTkgGI12VRZhKUJ9G0PVPg7azvQ7PBZrbOazOKRaiMms6czHPikEXralfrLBZE85mkenZpzFxrFjAyE8H3CoJmTfsUu3802JULPwDXIounbIr3VDTiP1%2BXxPczFNpPt%2FEhGzRvhUOOLH5EeUMPnkPzDEyvF6r0niZERxDdCwWIMiLEQ5fnd9XxQRDAgzqsv6GCBU2prFk4tiQLCIZMDjNE&X-Amz-Signature=023ee820ba8a9e0d95f670cc4be76c0b715de486f7fd72de31877842c5b8e017&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

随后我们把相应的依赖可以导入到项目里面，这个过程会进行一个下载，我本地已经是预先下载好了，比较快。好导入进来以后，相应的注解在这边就可以去使用了。 aspect 注解好，随后在这里我们就可以去编写相应的方法。

[image](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/df77bea2-14e3-40d9-b6a4-1977b604e87b/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SHKNXDQM%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T224633Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIFdp2WMhMOzzDtcCny%2BB95NZBSfk%2FDGtfIoNkfbxbD50AiEAsMTa1F5MOGMoCnaS1HkJ0ywDtwASWd426P%2FgdUeihDkqiAQIxv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDBBShSyDPD0oGfzA2SrcAxtxf8pLmRgkVJzUF16O%2FdsKH0kFqtQSMZGH7jxTurVNpXvKxkQ10lyOH%2F%2BMqFZlrCd%2BPcUHsWJpwaPeqRSFyaQlLgR438c%2FOoAxd%2Bh5N8Dtbjcb5oLrl%2FCmTEFyFZVCXueegFXnbw2ZcXRgdrbkc42HHIQbnCwWlt3FxR4lYoATDrqzu1kRcWfMRY6NCRX4IJaEyprgCljzDwLFEGgWtb2zAIf1rRdnObZgslF4rwLw65R5rGYLBjT%2FAp%2BI%2FWR2xWc%2Ba%2F74taAOdXhg3nVjMMEZNTnJeQdAOHVijWzYu6qERF6bNHcmXBJNKRrX9Q2%2FX0MNvQrgighvNfuNg49tozRixJv4oFIHFcdaj6qJZIUxZzx1oMcsy6UiMkrnRcmcIzpRgODLojh3bxLG142vqhcefb8IQAWdJ6L4pD1jKnDknGxgxNj18pzKlHRvAfRe%2BwRTVwdGio0O2DeyWpK%2FyFFZOAGoqnZkmvvayB8lbjIrJFcnERuw%2FyAAeJY5JHib58xFZJXNWUoAWpZJ0nwSPee3%2BvzSsj%2BKH0xIoudCtpcVs%2FkgT62M2gvK%2Fo1rlUEPmhVm9EuS5MTefGV9RCdO%2F6kMHQYApaq%2B2Z4fTbLkVQIi%2BU0qSkqZDVrlqCCGMOu4%2F9IGOqUBxIicryMTkgGI12VRZhKUJ9G0PVPg7azvQ7PBZrbOazOKRaiMms6czHPikEXralfrLBZE85mkenZpzFxrFjAyE8H3CoJmTfsUu3802JULPwDXIounbIr3VDTiP1%2BXxPczFNpPt%2FEhGzRvhUOOLH5EeUMPnkPzDEyvF6r0niZERxDdCwWIMiLEQ5fnd9XxQRDAgzqsv6GCBU2prFk4tiQLCIZMDjNE&X-Amz-Signature=954cc9fc15ea360963b59d654e6685533bbde27c74c2a6c1d5cb90e53dab477c&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

可以先来回顾一下 AOP 的几种通知类型。其实 AOP 它总共有 5 种类型。第是一个前置通知，前置主要是在方法调用之前执行，是这样的一个通知和前置相互对应的。还有一个后置通知，这个是在方法调用之后执行，准确来说应该是在正常调用，如果发生异常，这个方法是不正常的。这一点是需要去区别的，因为在后面还有一个最终通知。好写一下。在我们要什么是一个环绕通知，其实就是around，这个是指在方法调用之前和之后都分别可以执行的通知，在通知里面是在开头和结尾都可以让我们去执行一次。


第四一个，这是异常通知，如果在方法调用过程中发生异常，则通知好。第5一点。第5一点其实最终通知任何是在方法调用之后执行。这一点第五个和第二个是需要去区别的。第二个是在方法正常调用之后不能报异常，如果报一场通知是执行不了的。如果报了异常，其实在最终通知里面是可以去执行最终通知，又可以把它理解为是一个拆开去里面的final。


OK，好，这个是我们复习了一下，总共是有 5 种通知在我们所需要去使用的。环绕通知，它的注解对应的其实是一个 at around。好。随后我们就可以编写相应的方法。在这里我们可以来写一下。先写一个 public object 来写一个方法名叫做 record time log，在这个参数里面，它会有一个 proceeding join point 写上。在这里面我们就可以去写相应的一个内容了。首先我们可以先来写一上一个日志，日志我们在当前的类里面还没有，所以我们可以在这里面先去加上一个 public static final log，这个是在 cell for j 里面，第一个 log 等于 log factory，点 get log，把这个类放进来。


好，我们换一行这个 log 我们就定义好了。我们先在这个地方我们先可以去打印一下。我们直接使用 in for 的级别去打印。这个其实主要就是用于去输出当前。我们代表这个方法是开始执行了。我们在这里可以写一下，开始执行要执行哪里？因为我们后面会有很多的 service 类，以及是相应的方法，所以我们尽量的要把相应的一个 service 的类名称，以及是它所调用的某一个 service 的方法名，在这里都是需要去进行一个展示的。在这里面其实由于我们使用的是 self for j，所以我们是可以去加上这两个大括号，代表是一个占位符。中间我们可以使用一个点，这个点就代表某一个类的某一个方法。后面就使用一个逗号建科就可以了。


我们都换行是 join point 点，有一个 get target，这个就是目标，它的目标是哪一个 class get plus。随后下一个占位符使用 join point 点 get 有一个，这是代表签名的意思点，再 get name，这个就是一个方法名。好，我们多按一下tab。


这个是我们所记录的第一行，用于去记录执行正在开始执行某一个 service 所对应的某一个方法。好，随后我们在这里就要来记录一下我们最先开始的一个时间，因为我们要去监控某一个 service 的时间。其实应该是在执行之前和执行之后相互的进行一个时间记录，并且在最后进行一个减法来获得一个时间差。这个时间差就是我们的 service 它自己执行的一个时间。我们在这里可以来一个定一个落马。 begin time。通过 system 点有一个current，这是获得当前的一个时间的。是记录开始时间。好，我们在中间就要去执行我们的一个目标方法了。目标方法直接使用 join point 点proceed，这样子就 OK 了，它会执行对应的方法的。在这边加个注释执行目标service。在这边有一个object，这个 object 是我们要返回出去的，定义为result，拼错了 u l，t。最后这个是用于去 return 的。

```java
package com.imooc.aspect;

import org.aspectj.lang.ProceedingJoinPoint;
import org.aspectj.lang.annotation.Around;
import org.aspectj.lang.annotation.Aspect;
import org.slf4j.Logger;
import org.slf4j.LoggerFactory;
import org.springframework.stereotype.Component;

/**
 * <h1></h1>
 */
@SuppressWarnings("all")
@Aspect
@Component
public class ServiceLogAspect {

    public static Logger logger = LoggerFactory.getLogger(ServiceLogAspect.class);
    /**
     * AOP通知：
     * 1：前置通知：在方法调用通知
     * 2：后置通知：在方法调用之后通知
     * 3：环绕通知：在方法调用之前和之后，都可以分别执行的通知
     * 4：异常通知：如果在方法执行调用过程中发生异常，则通知
     * 5：最终通知：在方法调用之后执行
     */
    /**
     * 切面表达式
     * 第一处： 防范返回的类型， * 代表所有的类型
     * 第二处： 报名代表 aop 监控的的类所在的包
     * 第三处：..  代表该包以及其子包下面所有类方法
     * 第四处： * 代表类名， * 代表所有的类
     * 第五处：*(..) *代表类中的方法名，（..）表示方法中的任何参数
     *
     * @param joinPoint
     * @return
     * @throws Throwable
     */
    @Around("execution(* com.imooc.service.impl..*.*(..))")
    public Object recordTimeLog(ProceedingJoinPoint joinPoint) throws Throwable {
        logger.info("========== 开始执行 ==========", joinPoint.getTarget().getClass(),  joinPoint.getSignature().getName());

        // 记录开始时间
        long begin = System.currentTimeMillis();

        // 执行Service
        Object result = joinPoint.proceed();

        // 执行结束时间
        long end = System.currentTimeMillis();

        long takeTime = end - begin;

        if (takeTime > 3000) {
            logger.error("========== 执行结束， 耗时 ：{} =======", takeTime);
        } else if (takeTime > 2000) {
            logger.error("========== 执行结束， 耗时 ：{} =======", takeTime);
        } else {
            logger.info("========== 执行结束， 耗时 ：{} =======", takeTime);
        }
        return result;
    }


}
```

在执行完毕之后，我们要来记录一个结束时间，把拷贝一下，定义为 and 记录结束时间。好。拿到结束时间以后，我们就来获得一个时间差。先写一个名字 take time 等于 and 减去笔记好。这个时候当我们拿到时间差了以后，随后我们就可以去做一个判断了。这个判断在这里可以去写一下，比方我们以 3 秒为一个最大，如果超过 300 毫秒，我们就可以使用 error 的级别。 log 点era。好，开始记录。在这边里面我们写上执行结束耗时多少，通过战略服务来记录一下。传入的是 1 个毫秒，只要把 take time 传进去就可以了。这里是一个 l 的级别，如果它时间又很长，比方是 2 秒， 2 秒比 3 秒稍微小一些。它是有一个区间。在这里使用一个警告的日志级别。


好。最后否则我们就可以使用一个 input 的级别，把它作为是一个最低的级别。这样子三种级别我们在这里就进行了一个输出了。好，这个是我们所需要去执行的一个方法。在这里有一个红线，这个红线有一个 throttle 是需要让我们去处理的，在当前这个方法我们其实是可以直接把它给撕绕出去。


好，OK，这个方法around，其实我们的一个环绕通知所要去执行的方法是写好了。接下来我们既然是要利用AOP，在它的上方我们要加上一个注解around。在注解里面要写上相应的一个表达式，这个表达式就是切面表达式。好，可以直接通过代码补全就可以看到有一个叫做excuse，这就是执行你所要的一个表达式。在表达式里面其实是包含有相应的含义的。这个其实是可以去写的通用的表达式。首先我们先写一个星号，在这里加上一个注释，这个是切面表达式。首先是一个excuse，这个是代表所要执行的表达式主体。随后第一处有一个星号代表方法返回类型，星号代表所有类型，一般来说我们使用星号就可以了。


好，随后下一个我们要去切哪一个service，这个 service 在哪一个包里面？来看一下。目前我们的 service 其实全部都是在工程里面，其实可以看得出来所有的 service 都是在这里面。在实现类里面，所以直接拷贝一下他的包，直接贴到这里了。以后其实就是写一下。


第二处包名代表 AOP 监控的类所在的包。好所在的包了以后，其实在包的后方我们还能去加上一些后缀，比方我们在后面可以再加两个点。加两个点是什么意思？写一下这是第三处点代表该包以及其子包下的所有类。方法就是当前i、m、p、 l 包以及是它的子包下所有的类。就是这个意思。点代表所有。好。随后在点点的后方，我们又可以去加上一个星号，这个时候的星号代表什么？是代表在包和它所有子包下的类，星号就代表所有的类。写一下这是第四处，这是一个新号，代表类名，我们以星号代替。星代表所有类。好。下一个我们要去切的是某一个 service 的方法。所以这个类的下方有哪些方法？我们在这里面也是需要去写上的。我们要贴所有的方法。所以这个类的方法就是心点。心就这意思。下面写一下。其实我们可以这样子去心点心，在这里面我们加上一个括号，再来一个点点，我们应该要来看一下这个意思。


这是第五处，新来一个括号点，这个是代表什么？我们可以进行一个拆分。首先第一个新代表类中的方法名是什么？在新就代表我们当前在这个类里面的所有的方法。随后后方又有了一个括号，这个括号又是什么意思？这个括号是指每一个方法的参数，方法里面是可以包含参数，也可以不包含参数。所以我们在这里其实可以两个点来进行一个表达式，这两个点就代表可以是任何的参数。 OK 表示方法中的任何参数。


现在其实我们这样的一个切面的表达式就已经是写好了，一般来说表达式写的比较通用化一点会比较好，而且这个东西是不需要去死记背的。根据这样的一个 12345 处地方，再跟着自己所要去切的那些内容，可以去自定义自己的一些切入点，因为在一个项目里面，切入点可能会有很多，根据这样的一个形式，这样的表达式就可以去自己定义了。


好，随后我们就可以来进行一个测试了。来看一下我们执行的时间。好，我们来先 install 一下我们的项目，现在 install 成功，随后重启一下我们的整个工程。主要它的日志时间，我们是在控制台里面会去进行展示的，所以我们在运行完毕以后， Cleo 把日志清空一下。之后，我们可以打开我们的网站，我们到注册里面，我们可以通过一个监测，因为它会根据用户名去查询是否存在。比方我们来敲一个i，来看一下我们的控制台，这个时候你会发现我们的日志已经是开始在记录了。因为我们有一个方法来看一下。


首先一个开始执行，执行是什么？是执行某一个class，这个 class 是在哪里？是在 user service i m P2。在这个方法里面会有一个 query user name is exist，就是判断用户名是否存在。其实也就是在我们当前类里面的方法，他已经是找到了这个方法。所以我们在切面里面是通过一个是target，一个是 signature 签名可以去获得的。这个时间比较短，是 238 毫秒，所以它是一个 info 的级别。如果假设现在我们可以在注册里面，我们可以把 create user 我们在这里面。我们来通过 sleep 一个 3 秒以上来看一下它的一个时间。 three 的点 sleep 比方 3500 毫秒，这里面会有一个异常，我们叉开去一下。随后我们再拷贝一下，把它放到它的一个登录里面，登录在下方有一个这里，放在这个部位我们可以记住它为 2500 毫秒。

好。随后我们就可以来做一个测试了。由于我们修改了 service 层的方法，我们可以在这里面全局的去进行一个install，当然也可以去直接 install service 包也可以好 install 一下。好， install 成功。随后我们再来一个重启。


好，OK，没有，我们到咱们的项目里面去，我们首先一个我们还是一样，我们写一个 imock i m，这个时候在控制台里面是没有问题，是依附。因为我们没有去 sleep 一个时间， 240 毫秒执行。OK，下一个我们来一个真正的注册，来一个 m 可比方 m 可123，密码 123123 点击注册。这个时候他注册的时间耗时是比较久的，因为我们是 sleep 了一下。随后回到我们的控制台来看一下，这个时候当我们在执行的时候，你会发现它耗时了多久，它耗时了 3517 毫秒，也就是 3 秒多，所以它报了一个级别，是 l 的级别。


好，随后我们再来做一个登陆，登陆，我们现在还没有做退出，我们F12，把 cookies 清通一下，退出登录。我们在下一节，下一节我们可以去做一下刷新一下进行登录。使用 Imock 去登录，点击登录。好，现在是登录成功了。这个时候是跳转，稍微有一些慢，没有关系。


回到我们控制台再来看一下。在我们使用登录的时候，其实登录接口耗时了 2500 毫秒， 2 秒多，所以它报了一个级别，是往往的这样的一个级别。所以我们根据一个不同的日志级别，就可以监控到每一个 service 所记录的时间。都可以通过日志来进行一个记录。


这个其实是非常有助于我们在生产环境里面去进行监控的。有些方法内容执行的比较慢，当达到了一定程度，其实都可以会由运维的人员提交给我们开发团队，随后就会由开发团队针对不同的情况去做一些优化等等，都是非常有必要去做的一个手段。另外我们在这里可以附带一提，现在其实我们是一个单起的项目，如果我们是在一个非常庞大的集群分布式系统、微服务系统，可能我们会有上百台，上千上万台节点。这个时候我们的日志其实会有很多，日志会有分散在不同的节点，有几万个节点，几千个节点，这个时候我们使用这种方式去做可能会不太好。所以我们在后续的课程里面会有一个日志收集，日志监控的功能。这个时候我们会依靠卡斯卡相应的内容会有相关的老师会具体的去说一下。所以我们在这里会跟大家可以先提一下，大家也可以去思考一下以上我们本节所涉及到的一个相应的内容，大家在课后根据代码去实现一下。如果有遇到问题，也欢迎大家在留言区去留言，也可以在群里和老师们一起交流。OK？


