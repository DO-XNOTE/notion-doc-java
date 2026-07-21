---
title: 2-9 RabbitMQ 的核心API
---

# 2-9 RabbitMQ 的核心API

[image](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/af0c1116-2e23-44f5-b09a-2d9406ee986e/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YMCMOUEO%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T225245Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDvI5Ewym%2FACrIzZeSuQxo8qXhvdNxYQOPPTuIzO4cfmQIhANlYEDubOEkcj8fs6IIfzH4vkgsJ4D8M8nSZbEW3DinVKogECMb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgxIZKKD%2FJ%2BeTcANyrAq3AOcc30wHdZBIx5nG9iY%2Fpt0R4UXBJKmeB66vFPkteFc8fflSWTAR%2F%2Bz4pSs1lFr1ornK8BwaUlacBBRAfLM%2Bc2L2fHdLE6jgRP1CDBgFtwIz88i8kKQJU4KxEZBDOmkHxk%2BHXTUw4ie2hk9vbGwb7MSRuVkyqPkv2N3Owa0pL4lRAfEbCtYu%2B%2B5zUa1HUOeEIuDmAPYSNtwGX%2FAYzHcPMA8fRk%2Fgt7IkilNhq7S2%2B1uOiycTAWpdNKubvQYDvc8RetXeDVsEcRJ1R0tplsOzCn58K0FpSC6epBswRybUOOnlBK3xNUD9FdI5ZCUfSgoUfpjF%2FLYJyK%2B4q8d749SdYdXkWoLC4eDA2XM7z0HmCXkH6rTNVV5%2B6hk9exlB4VU%2B3kqUQ1Z5qe6at5kCus8DSPRcvqL2pXSkKqrNWBwQyvylRuQm40K5O9cBW0aD2OR0enlUwvrhOb8BdEi4Rop64u4nX3E6b0cPj7TCbCY9P%2F0tNZQH4jSFGeU9iOx4NcoTEg0dxFT5QQ4l2P4x7rgYr8mrVrmhDMX9vM8QLgiFXu5iCR0XoBhX5TqFufA%2BA3DVZAnvgOY1VKnSzODyMGn12xgmzo9tHMcOmjm0d8tGzzZzcpDfGANvjyLYeaCcDDBuv%2FSBjqkAS6Pa0Y%2BULqIako0l9DZg2f7oBMJ2i%2FkCJvX7mhoRmH7kq8416SXoWa90YkLnvL%2FyzuFe%2BgC%2B%2FSnthCJ%2FVCwiA%2FpTqGm%2BUZrWLCw%2FmEn3YTHYGrTr%2BVz%2BNRjCRuLjoFi9WOx4Q8nMlFDkB7iuUcfvx3iPyoteTetxpbekPwzaUVM9m88uffrCYqDuhpdIYaPNlZWtfIK1qZmZN6lcR42XFMsXfRx&X-Amz-Signature=81aaa937b126828a2a15e11f529d156f55a81310d8435fcefebebaf0ff1635ea&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

```javascript
2-9附：RabbitMQ核心API
核心APl-Exchange概念
Exchange：接收消息，并根据路由键转发消息到所绑定的队列。这是RabbitMQ（AMQP）非常重要的概念
     上幅图说明问题：黄色的部分就是Exchange和Queue的关系，可见他们是一个路由的关系
        
    Exchange（交换机）本身有很多属性和类型，接下来容我一一介绍
         Exchange（交换机）属性：
            Type：交换机类型direct、topic、fanout、headers
               Durability：是否需要持久化，默认为true表示持久化
            AutoDelete：当最后一个绑定到Exchange上的队列删除后，自动删除该Exchange
            Intemnal：当前Exchange是否用于RabbitMQ内部使用，默认为False
             Arguments：扩展参数，用于扩展AMQP协议自制定化使用Name：交换机名称
        Exchange（交换机）类型
              DirectExchange：所有发送到DirectExchange的消息被转发到Routekey中指定的Queue，如下图所示：
          
                TopicExchange：所有发送到TopicExchange的消息被转发到所有关心Routekey中指定Topic的Queue上，Exchange将Routekey和某Topi配，此时队列需要绑定一个Topic。注意点：可以使用通配符进行模糊匹配。符号“#”匹配一个或多个词，例如：“1og.#”能够匹配到“log.info.配不多不少一个词，例如：“1og.*只会匹配到“log.error”；如下图所示
```

[image](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/713be7a9-c2f3-4789-ad6d-4de8dbee23d8/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YMCMOUEO%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T225245Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDvI5Ewym%2FACrIzZeSuQxo8qXhvdNxYQOPPTuIzO4cfmQIhANlYEDubOEkcj8fs6IIfzH4vkgsJ4D8M8nSZbEW3DinVKogECMb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgxIZKKD%2FJ%2BeTcANyrAq3AOcc30wHdZBIx5nG9iY%2Fpt0R4UXBJKmeB66vFPkteFc8fflSWTAR%2F%2Bz4pSs1lFr1ornK8BwaUlacBBRAfLM%2Bc2L2fHdLE6jgRP1CDBgFtwIz88i8kKQJU4KxEZBDOmkHxk%2BHXTUw4ie2hk9vbGwb7MSRuVkyqPkv2N3Owa0pL4lRAfEbCtYu%2B%2B5zUa1HUOeEIuDmAPYSNtwGX%2FAYzHcPMA8fRk%2Fgt7IkilNhq7S2%2B1uOiycTAWpdNKubvQYDvc8RetXeDVsEcRJ1R0tplsOzCn58K0FpSC6epBswRybUOOnlBK3xNUD9FdI5ZCUfSgoUfpjF%2FLYJyK%2B4q8d749SdYdXkWoLC4eDA2XM7z0HmCXkH6rTNVV5%2B6hk9exlB4VU%2B3kqUQ1Z5qe6at5kCus8DSPRcvqL2pXSkKqrNWBwQyvylRuQm40K5O9cBW0aD2OR0enlUwvrhOb8BdEi4Rop64u4nX3E6b0cPj7TCbCY9P%2F0tNZQH4jSFGeU9iOx4NcoTEg0dxFT5QQ4l2P4x7rgYr8mrVrmhDMX9vM8QLgiFXu5iCR0XoBhX5TqFufA%2BA3DVZAnvgOY1VKnSzODyMGn12xgmzo9tHMcOmjm0d8tGzzZzcpDfGANvjyLYeaCcDDBuv%2FSBjqkAS6Pa0Y%2BULqIako0l9DZg2f7oBMJ2i%2FkCJvX7mhoRmH7kq8416SXoWa90YkLnvL%2FyzuFe%2BgC%2B%2FSnthCJ%2FVCwiA%2FpTqGm%2BUZrWLCw%2FmEn3YTHYGrTr%2BVz%2BNRjCRuLjoFi9WOx4Q8nMlFDkB7iuUcfvx3iPyoteTetxpbekPwzaUVM9m88uffrCYqDuhpdIYaPNlZWtfIK1qZmZN6lcR42XFMsXfRx&X-Amz-Signature=67ab1bbd154dddcba6568f3c808e924b76b5b37ca45dcdafa919961380dbbba2&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

