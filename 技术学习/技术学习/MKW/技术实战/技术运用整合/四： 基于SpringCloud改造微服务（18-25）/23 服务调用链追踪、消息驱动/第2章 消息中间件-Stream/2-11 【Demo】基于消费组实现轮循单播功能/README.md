---
title: 2-11 【Demo】基于消费组实现轮循单播功能
---

# 2-11 【Demo】基于消费组实现轮循单播功能

[image](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/1cff5eab-e1f3-4de0-9c76-5de096b70ce1/SCR-20240722-clni.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YFJNOV2M%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T225817Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIBmIMutuxuljqZIWHvmhvTQbL3NAFqFxHrSfeB2ew932AiBON1581I%2Bo2pwuVQblrCW9aenL1qwLMl8FIuZKr%2BR8TSqIBAjG%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMI6z6TrL2QpWL0OqzKtwDK%2BYRSR%2Bs8L8wACtb0hlUzWyJ6Ii5KkwRD0xRvWfKMgpzTGUqG23KGbMbmMZfwW3vEyzsTIICTpv7Y5ldzK6FFE5vFPymcdwN%2F9e3%2F7kUN74eNuQpdqEZVZ7ybMy6OLq5VcK6XrTEgMsrK6n3Xw8dUAHtd9uYNJyo%2FNe%2F9EDbVsXTAzmkVfKAr5d%2Fg3w9tJ5oUkSupy%2F2ca5ihpp19ch%2F2Aag6%2B2zb5qOaudE1t0ZMJxjmcpPZZRJD3v8%2Bzp8G2KcguvoI0FUEYFnjjlDNpQLWSRDgl6PDj7ClevdeRxtUgD%2FdHEqEJJdYAJUllMBDoUiQdpAx9UsTP%2FuTh%2BlEgvgLBJLSEIXFfStsVDA1w8WgA%2FA%2BKogU3ToqHn9SPZP%2Fy2c8i8FlO9L8XLJY3du%2FHDRn05agrssRtffeyL5uSAwIE3sDhzJjZJE4T10vYwDqPSE39rrF6weHO%2F%2FDRNPLdBZARVEfXqTm1Jh%2BO2HcCqDbqoHmI4we8hE%2Fv1IlRlCloGDJ72Q%2Bgc7VlOyD2zmJGzzOneYWJfoDVcwRkW7hbrkQx6r%2Fmgxm3EuHXnVRADHDNJqHVxbeOQLmz7xdyxul5CzxEw47gHqybTvHWrobXxFQwYfQIeqXbxOiPtUU7gwsbf%2F0gY6pgG%2Fmvfni8oPN5HbhJ%2FxVATT%2FMN47xBX05NDz8rDhw1whmv%2F5iLYhrQ41UweqgqKRgQeY7JMKIJ4Lj3F8TJjgw1fo%2FFwkrf1VFviI82itj7dG%2FPFZB9iDxmgfnGV7is9pPOeJQc494LXMXMhr0dUpMLQaGYniPph%2B5CNOisrWqzovdxLFIBr3x5l0RrEsbp2549rIlgqK7aCj92gdsoozlCqltx1PmJx&X-Amz-Signature=824d541d47ae3ce50fa8274856ef6465ce4f6fa3e464400b6bca50db065a319b&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

[image](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/b126aced-5311-4931-b779-0b08c9ed7591/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YFJNOV2M%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T225817Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIBmIMutuxuljqZIWHvmhvTQbL3NAFqFxHrSfeB2ew932AiBON1581I%2Bo2pwuVQblrCW9aenL1qwLMl8FIuZKr%2BR8TSqIBAjG%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMI6z6TrL2QpWL0OqzKtwDK%2BYRSR%2Bs8L8wACtb0hlUzWyJ6Ii5KkwRD0xRvWfKMgpzTGUqG23KGbMbmMZfwW3vEyzsTIICTpv7Y5ldzK6FFE5vFPymcdwN%2F9e3%2F7kUN74eNuQpdqEZVZ7ybMy6OLq5VcK6XrTEgMsrK6n3Xw8dUAHtd9uYNJyo%2FNe%2F9EDbVsXTAzmkVfKAr5d%2Fg3w9tJ5oUkSupy%2F2ca5ihpp19ch%2F2Aag6%2B2zb5qOaudE1t0ZMJxjmcpPZZRJD3v8%2Bzp8G2KcguvoI0FUEYFnjjlDNpQLWSRDgl6PDj7ClevdeRxtUgD%2FdHEqEJJdYAJUllMBDoUiQdpAx9UsTP%2FuTh%2BlEgvgLBJLSEIXFfStsVDA1w8WgA%2FA%2BKogU3ToqHn9SPZP%2Fy2c8i8FlO9L8XLJY3du%2FHDRn05agrssRtffeyL5uSAwIE3sDhzJjZJE4T10vYwDqPSE39rrF6weHO%2F%2FDRNPLdBZARVEfXqTm1Jh%2BO2HcCqDbqoHmI4we8hE%2Fv1IlRlCloGDJ72Q%2Bgc7VlOyD2zmJGzzOneYWJfoDVcwRkW7hbrkQx6r%2Fmgxm3EuHXnVRADHDNJqHVxbeOQLmz7xdyxul5CzxEw47gHqybTvHWrobXxFQwYfQIeqXbxOiPtUU7gwsbf%2F0gY6pgG%2Fmvfni8oPN5HbhJ%2FxVATT%2FMN47xBX05NDz8rDhw1whmv%2F5iLYhrQ41UweqgqKRgQeY7JMKIJ4Lj3F8TJjgw1fo%2FFwkrf1VFviI82itj7dG%2FPFZB9iDxmgfnGV7is9pPOeJQc494LXMXMhr0dUpMLQaGYniPph%2B5CNOisrWqzovdxLFIBr3x5l0RrEsbp2549rIlgqK7aCj92gdsoozlCqltx1PmJx&X-Amz-Signature=48d53ddf05cea4c60613b9a66fef47be7de1fb8dc10a152b6cec363a396d15c8&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

[image](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/049c1190-1541-4ea9-9c4e-f8913d555f7c/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YFJNOV2M%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T225817Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIBmIMutuxuljqZIWHvmhvTQbL3NAFqFxHrSfeB2ew932AiBON1581I%2Bo2pwuVQblrCW9aenL1qwLMl8FIuZKr%2BR8TSqIBAjG%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMI6z6TrL2QpWL0OqzKtwDK%2BYRSR%2Bs8L8wACtb0hlUzWyJ6Ii5KkwRD0xRvWfKMgpzTGUqG23KGbMbmMZfwW3vEyzsTIICTpv7Y5ldzK6FFE5vFPymcdwN%2F9e3%2F7kUN74eNuQpdqEZVZ7ybMy6OLq5VcK6XrTEgMsrK6n3Xw8dUAHtd9uYNJyo%2FNe%2F9EDbVsXTAzmkVfKAr5d%2Fg3w9tJ5oUkSupy%2F2ca5ihpp19ch%2F2Aag6%2B2zb5qOaudE1t0ZMJxjmcpPZZRJD3v8%2Bzp8G2KcguvoI0FUEYFnjjlDNpQLWSRDgl6PDj7ClevdeRxtUgD%2FdHEqEJJdYAJUllMBDoUiQdpAx9UsTP%2FuTh%2BlEgvgLBJLSEIXFfStsVDA1w8WgA%2FA%2BKogU3ToqHn9SPZP%2Fy2c8i8FlO9L8XLJY3du%2FHDRn05agrssRtffeyL5uSAwIE3sDhzJjZJE4T10vYwDqPSE39rrF6weHO%2F%2FDRNPLdBZARVEfXqTm1Jh%2BO2HcCqDbqoHmI4we8hE%2Fv1IlRlCloGDJ72Q%2Bgc7VlOyD2zmJGzzOneYWJfoDVcwRkW7hbrkQx6r%2Fmgxm3EuHXnVRADHDNJqHVxbeOQLmz7xdyxul5CzxEw47gHqybTvHWrobXxFQwYfQIeqXbxOiPtUU7gwsbf%2F0gY6pgG%2Fmvfni8oPN5HbhJ%2FxVATT%2FMN47xBX05NDz8rDhw1whmv%2F5iLYhrQ41UweqgqKRgQeY7JMKIJ4Lj3F8TJjgw1fo%2FFwkrf1VFviI82itj7dG%2FPFZB9iDxmgfnGV7is9pPOeJQc494LXMXMhr0dUpMLQaGYniPph%2B5CNOisrWqzovdxLFIBr3x5l0RrEsbp2549rIlgqK7aCj92gdsoozlCqltx1PmJx&X-Amz-Signature=0f1bf8f2beafc886fcf76d489ddd816e32889b2af4bc40b378706edc953e2c1b&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

[image](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/0d6050dd-3b55-4d98-81e7-8c91380f78c3/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YFJNOV2M%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T225817Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIBmIMutuxuljqZIWHvmhvTQbL3NAFqFxHrSfeB2ew932AiBON1581I%2Bo2pwuVQblrCW9aenL1qwLMl8FIuZKr%2BR8TSqIBAjG%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMI6z6TrL2QpWL0OqzKtwDK%2BYRSR%2Bs8L8wACtb0hlUzWyJ6Ii5KkwRD0xRvWfKMgpzTGUqG23KGbMbmMZfwW3vEyzsTIICTpv7Y5ldzK6FFE5vFPymcdwN%2F9e3%2F7kUN74eNuQpdqEZVZ7ybMy6OLq5VcK6XrTEgMsrK6n3Xw8dUAHtd9uYNJyo%2FNe%2F9EDbVsXTAzmkVfKAr5d%2Fg3w9tJ5oUkSupy%2F2ca5ihpp19ch%2F2Aag6%2B2zb5qOaudE1t0ZMJxjmcpPZZRJD3v8%2Bzp8G2KcguvoI0FUEYFnjjlDNpQLWSRDgl6PDj7ClevdeRxtUgD%2FdHEqEJJdYAJUllMBDoUiQdpAx9UsTP%2FuTh%2BlEgvgLBJLSEIXFfStsVDA1w8WgA%2FA%2BKogU3ToqHn9SPZP%2Fy2c8i8FlO9L8XLJY3du%2FHDRn05agrssRtffeyL5uSAwIE3sDhzJjZJE4T10vYwDqPSE39rrF6weHO%2F%2FDRNPLdBZARVEfXqTm1Jh%2BO2HcCqDbqoHmI4we8hE%2Fv1IlRlCloGDJ72Q%2Bgc7VlOyD2zmJGzzOneYWJfoDVcwRkW7hbrkQx6r%2Fmgxm3EuHXnVRADHDNJqHVxbeOQLmz7xdyxul5CzxEw47gHqybTvHWrobXxFQwYfQIeqXbxOiPtUU7gwsbf%2F0gY6pgG%2Fmvfni8oPN5HbhJ%2FxVATT%2FMN47xBX05NDz8rDhw1whmv%2F5iLYhrQ41UweqgqKRgQeY7JMKIJ4Lj3F8TJjgw1fo%2FFwkrf1VFviI82itj7dG%2FPFZB9iDxmgfnGV7is9pPOeJQc494LXMXMhr0dUpMLQaGYniPph%2B5CNOisrWqzovdxLFIBr3x5l0RrEsbp2549rIlgqK7aCj92gdsoozlCqltx1PmJx&X-Amz-Signature=ca57d6787c606e6c0804382daa6e79b4acead47a3f6bed4fea21b3f7cc6492d8&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

网的各位同学们，大家好，在之前的视频章节里，咱学了如何使用 stream 进行消息的广播。在这一节里我们来看看轮询单薄是如何来实现的。这个单薄的意思就是说同一个组内只有一台机器会去消费这个消息。那咱接下来看一看本节的主要内容有，第一步，我们创建一个 consumer 和 producer 这里其实是指一个新的 topic 接下来配置一个消费组，启动多个节点进行测试，看一看这个消费组中的每一个节点是如何来轮询处理消息的。然后我要带大家去 rabbit MQ 的界面看一看单播和广播在 exchange 中都有哪些不同的表现。


那么在本章的最后，我们还要搭建一个消费分区的示例程序，它是基于轮询单波的基础上，对不同的 consumer 组进行一个分区。这个消费组和消费分区可是两个不同的概念。如果大家对这两个概念已经印象模糊了，赶紧回到最近的一个图文教程里面去好好复习一下。

[image](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/562ea26f-c44f-49e5-b4da-3953de327dca/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YFJNOV2M%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T225817Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIBmIMutuxuljqZIWHvmhvTQbL3NAFqFxHrSfeB2ew932AiBON1581I%2Bo2pwuVQblrCW9aenL1qwLMl8FIuZKr%2BR8TSqIBAjG%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMI6z6TrL2QpWL0OqzKtwDK%2BYRSR%2Bs8L8wACtb0hlUzWyJ6Ii5KkwRD0xRvWfKMgpzTGUqG23KGbMbmMZfwW3vEyzsTIICTpv7Y5ldzK6FFE5vFPymcdwN%2F9e3%2F7kUN74eNuQpdqEZVZ7ybMy6OLq5VcK6XrTEgMsrK6n3Xw8dUAHtd9uYNJyo%2FNe%2F9EDbVsXTAzmkVfKAr5d%2Fg3w9tJ5oUkSupy%2F2ca5ihpp19ch%2F2Aag6%2B2zb5qOaudE1t0ZMJxjmcpPZZRJD3v8%2Bzp8G2KcguvoI0FUEYFnjjlDNpQLWSRDgl6PDj7ClevdeRxtUgD%2FdHEqEJJdYAJUllMBDoUiQdpAx9UsTP%2FuTh%2BlEgvgLBJLSEIXFfStsVDA1w8WgA%2FA%2BKogU3ToqHn9SPZP%2Fy2c8i8FlO9L8XLJY3du%2FHDRn05agrssRtffeyL5uSAwIE3sDhzJjZJE4T10vYwDqPSE39rrF6weHO%2F%2FDRNPLdBZARVEfXqTm1Jh%2BO2HcCqDbqoHmI4we8hE%2Fv1IlRlCloGDJ72Q%2Bgc7VlOyD2zmJGzzOneYWJfoDVcwRkW7hbrkQx6r%2Fmgxm3EuHXnVRADHDNJqHVxbeOQLmz7xdyxul5CzxEw47gHqybTvHWrobXxFQwYfQIeqXbxOiPtUU7gwsbf%2F0gY6pgG%2Fmvfni8oPN5HbhJ%2FxVATT%2FMN47xBX05NDz8rDhw1whmv%2F5iLYhrQ41UweqgqKRgQeY7JMKIJ4Lj3F8TJjgw1fo%2FFwkrf1VFviI82itj7dG%2FPFZB9iDxmgfnGV7is9pPOeJQc494LXMXMhr0dUpMLQaGYniPph%2B5CNOisrWqzovdxLFIBr3x5l0RrEsbp2549rIlgqK7aCj92gdsoozlCqltx1PmJx&X-Amz-Signature=005a189ced80785a63a6e67c63efe187a889486be6c24c2f491464c8661cf00a&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

同学们，那跟我一起抄起家伙开赴 intelligi 编程，是我快乐 996 是我的福报，整个 stream 的福报真是不少，好多 demo 我们这里从哪开始呢？从这个 topic 开始，咱不是要创建一个轮询单波的 topic 吗？我们把它复制下来，就是把 my topic 复制一下，然后创建一个新的 topic 就给它起名叫 group topic 好了，因为咱今天的 demo 涉及到消费组，消费分区都是和分组有关的。


咱的 group topic 里面， input 和 output 我们把它改一下，就叫 group consumer 和 group producer 那接下来 topic 创建好了以后，咱要在 controller 里面操作一番，怎么操作呢？首先咱把刚才创建的新的 topic 给它引入进来，它的名称叫 group topic 把它叫做 group a topic producer 好。引入进来以后，咱就可以创建一个 controller 的方法来向这个 topic 里面发送一条消息。那这个 controller 的方法我们要把它的方法名给改一下，叫 send a message to group 同时它的访问路径咱也给它改一下叫 send to group 那剩下还有一个小尾巴要改一下，就是把 producer 替换成这个咱刚创建引入进来的 producer 通过访问这个方法，我们就可以往消费组里面发送一条消息了。此时此刻他还并不是一个消费组，我们还要等后面配置好之后，他才会成为完全体。那这个消息的生产者已经写好了，接下来咱要去 consumer 这里把消费者也给添加进来。首先咱要把信道给绑定上，这里把咱们刚才创建的 group topic 给它引入进来。
Class. 引入进来以后，咱这里声明一个对应的消费者的方法。那把上面一个给复制一下，抄自己以前的作业，把方法名改成 consume group message 同样的 stream listener 中的类，咱也把它更改成 group topic 中的 input log 自然也要改一下啦。


改成 group a message consumed successfully 到这里，咱离消息分组的完全体又近了一步，还剩。那最后一点点距离是在哪里呢？那就是在配置文件里了，我们到达配置文件，我们这里加一行注释，这是给消息分组用的消息分组示例程序。那继续抄自己的作业，把上面这两行 copy 一下。咱不是前面说，这两个信道咱们要绑定到同一个地址上。那它绑定的 topic 的名称就叫 group consumer 和 group producer 我想想让我们绑定到哪，我们给它创建一个新的 topic 这个 topic 的名称就叫 group topic 上下保持一致。


那到这里它还仅仅只是一个广播消息，变身为消息分组，最后的那临门一脚就在这里了，我们要把它放大一下，大家关注重点，咱要开始配置消息分组怎么来？配置前缀是 spring 上面这行现成的，咱给它 copy 下来。好 copy 到这里。接下来消息分组，大家想想是对于生产者来说还是消费者来说，当然是对于消费者来说了。为什么呢？因为消息的生产者来自五湖四海，四面八方，每一个应用都可以往我的 rabbit MQ 的 topic 里发送消息。但是我们要控制的是处理这个消息的地方，也就是消费者。所以说这个分组的对象其实是消费者。好，我们把这个消费者的名字给它 copy 下来放到这里。


然后后面我们要给它指定组了 group 等于 group A 那从这里来看，已经全部被划归到了组 A 当中。我们这时候尝试着来启动两个应用，看一看发送一条消息以后，究竟是两个应用同时响应，还是只有组内的一个应用来响应？我们直接启动起 dream 的 application 紧接着回过头来把 server port 改动一下，从 63,000 改动到63,001，然后再启动第二个 instance 我们等待这两个 instance 启动完毕。


第一个已经启动好了，接着第二个也已经启动起来了，咱到 postman 里发起一个调用，那咱切换到分组单波的消息体里面，我们这里向 local host 63,000 的 send to group 这个方法发送一个调用。咱的 body 就传入一个 test 我们点击 123 发送，这里已经发送成功了，我们回过头来看一下，看到当前的 stream application 没有任何 log 打印出来。那我们切换到另一个 tab 看一下。同学们看这里是不是打印出了一行 log group a message consume the successfully 说明这个消息被组内的一台服务器给消费掉了。那我们接着再发一次，它应该会转换到另一台服务器来消费。果然上一回合消费这个消息的 consumer 这一回合没动静了，那另一个 consumer 消费了这个消息，那我们顺水推舟，再做一个简单的测试。


咱前面不是给消费组指定了它的 group 是 group A 吗？那我们这里再给它改成 group B 然后怎么样啊？然后把端口号改成63,002，再启动一个 instance 这样的话我们就由来自于两个用户组的三台机器共同监听这个 topic 那我们说到每个消费组只会有一台机器来处理这个消息，但是这并不代表着消息只能被一个消费组来消费。事实上，咱的一条消息将会被所有的消费组消费，只不过每一组只能消费一次。这里再到 postman 里发送一个请求，看一看消费组 A 和消费组 B 是不是同事都能消费这条消息发送过来，我们回到 intelligent 里看一下。


同学们看到这一行 log topic.group B 那说明当前的 group B 这个消费组已经成功的消费了。这条消息再来观察一下 group A 是不是也消费了，这台机器没有，那另一台机器一定有了。 OK 咱这里看到 group A 也成功地消费了消息。同学，我们刚才的消费组实例就已经测试完毕了，关停了所有启动好的应用，然后复原到了原始的状态。
我们接下来要去看消费分区如何设置了，消费分区的概念大家都清楚。不清楚的同学回到前面的图文教程里面去复习一下。我们这里要开始创建消费分区喽，我这里先打一行注释消费分区配置。首先咱要把消费分区给它开启开来，怎么开启？把上面这行配置 copy 一下，后面跟的参数是什么呢？是消费者的名字，也就是 group consumer 因为消费分区最终会落实到哪里，就是落实到 consumer 这里。


所以咱先要把 consumer 的消费分区功能给打开，partition等于 true 这一句就是我们注释一下开消费者的消费分区 owner 那咱把消费分区功能打开了以后，我们接下来要去对生产者做一番配置了，看生产者的配置是什么，还是这一行开头万年不变，后面跟的是生产者的名字，我们把它复制一下，自然而然的后面一个属性是谁是 producer 了。


producer 后面跟 partition 杠 count 这是什么意思呢？代表着两个消费分区，两个消息分去，这个配置还远远没有结束，我们再把这一行配置给它 copy 下来。既然咱有了消费分区，那如何来识别消费分区呢？这就要靠接下来的这个属性叫 partition 杠 key expression 那这个表达式实际上就是 spe L 表达式，咱前面应该有用过，它是什么？ key resolver 是不是有用过 resolver 那咱这里给它一个简单的值，给它一写死一个 expression 这个 1 是什么意思呢？它的意思是只有索引参数为一的节点才能消费消息。


这个节点实际上指的是消费者配置完这个属性以后，咱接下来还要配置两个属性，分别是谁呢？分别是，第一个属性是当前的 instance 数量， instance count 咱给它配置成2。好了，咱加一个注释，当前消费者实力总量其实这个并不重要了，咱接下来重要的是下面的一个参数喽，索引参数。什么叫索引参数呢？我们来看 index 给它设置成0，它就是跟上面一个搭配使用的，它的最大值是什么呢？我们标记一下，最大值是这个 instance count 大家记住是 instance count 减1，它表示当前实例的索引号这几个配置中实际上只有两个非常非常关键的信息，一个信息是生产者的 key expression 这里咱们配置的 key expression 是1，也就是只有参数为 1 的节点才能接收到数据。


第二个重要的属性就是它的索引参数。咱现在尝试启动这个当前的实例，把它的 application 方法跑起来，想让它双兔傍地走安能变，我是雄雌再跑一个实例。这个实例的索引号咱要把它变一下，把它变成 1 改成 1 之后要把端口号改成63,001。那运行起闷方法，让这两个实例同时抛起来。然后咱把 log 给它依次清空掉。
接下来咱就去 postman 里发起一个调用，这个函数调用依然发送到咱们这一节前面配置的 controller 当中。我们点击发送，同学们猜后台是哪个实例响应了请求。我们看一下果然是后启动的那个示例，因为咱在配置文件中配置了，只有当前的 index 索引是 1 的机器才能接收到这个消息。不信我们再发送几个请求，我们再发送一条两条三条。那么我们回到 intelligi 里面，我们看到这几条消息通通都被当前 index 唯一的机器给消费了。那 index 为 0 的机器，没有事情做什么 log 都没有，我们再来做一个测试。什么测试呢？同学们看，把这个 index 唯一的机器再给它启动一台，同时把端口号改成63,002，我们看看会有什么事情发生。同学们举一反三，想一想会有什么事情发生，他们都是在一个 user group 里。咱前面配置了 group 都是 A 他们的下标索引都是一说明都能 consume 这个消息。
那同学们猜想一下，趁老师在这边启动项目的时候，猜想一下会有什么效果？我们把 log 都清空收到 postman 里，咱发起一次调用回来看一看，被其中一台下标唯一的机器给处理了。那咱再发送一次消息好，再回头看一看这个消息跑到哪儿去了，跑到另一台下边唯一的机器处理了。
所以从这个现象里我们可以找到什么规律呢？如果我再发送一条消息，再发一个两条不够，再来一条三条，再来一条四角。大家可以看到，这两台下标为 1 的机器它们是轮询交替的来处理数据的。这个事实告诉我们什么呢？就是说消费分区和消费组可以合起来共同作用。同学们你们 get 到了吗？到这里，这一节的 demo 内容就结束了，我来跟大家简单回顾一下。


在这一节当中，我们学习了消息分组的配置，它的核心配置点只有这一条，就是给 consumer 上面配置一个 group 那么同一个分组只能有一台机器去 consume 这个消息。不过这个消息会传达给不同的分组，也就是说每一个分组都会把这条消息消费一次。

```docker
# 消息分组示例
spring.cloud.stream.bindings.group-consumer.destination=group-topic
spring.cloud.stream.bindings.group-producer.destination=group-topic
spring.cloud.stream.bindings.group-consumer.group=Group-A
## 消息分区配置
## 打开消费者的消费分区功能
spring.cloud.stream.bindings.group-consumer.partitioned=true
## 两个消费分区
spring.cloud.stream.bindings.group-producer.partition-count=2
## Spel (key resolver)
## 1 只有索引参数为 1 的节点（消费者），才能消费消息
spring.cloud.stream.bindings.group-producer.partition-key-expression=1
## 当前消费者的实例总数
spring.cloud.stream.instance-count=2
## (instance-count)  - 1 当前实例的索引号
spring.cloud.stream.instance-index=0
```


那接下来我们又学习了消息分区的配置。在消息分区里面，我们测试了启动两个分区，并且指定了 producer 的 partition key expression 属性，让所有的消息只能被特定的 consumer group 来消费。同时我们又测试了在消费分区内启动多台机器，并且这多台机器又同属同一个 group 通过把消息分区和消息分组的混搭，咱发现这两个概念功能实际上是可以相互作用的，这就是本小节的全部内容了。那么在接下来的小结当中，我将跟大家介绍一个经典的业务场景，那就是延迟消息。延迟消息是指可以被延迟到未来的某个时间点进行消费的消息。那么同学们，我们就下一小节再见。




