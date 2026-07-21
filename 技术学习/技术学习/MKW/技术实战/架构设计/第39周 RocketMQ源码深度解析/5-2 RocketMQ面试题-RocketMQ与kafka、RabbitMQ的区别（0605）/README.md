---
title: 5-2 RocketMQ面试题-RocketMQ与kafka、RabbitMQ的区别（0605）
---

# 5-2 RocketMQ面试题-RocketMQ与kafka、RabbitMQ的区别（0605）

[image](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/bd48b621-35a8-4f0d-b6f9-ab95778897cb/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663AFYZK7L%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T232234Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCrCc1VvBZpi6fZQSHlF2QJCUTohi4cPDh7Jizc4FO8cQIhANBAb9kmd6VLX%2FxombcqlWEpXqmup3OBLUe6ndNFYRJqKogECMb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1Igxc8849nMGZ%2B2bwgjsq3AP8sgwT4GdiWkqpiF007%2BCpNuRJFnD0bKn7bFadOP1OPdHtA7KBQj%2B1hHidSeS%2BN5tGIDzfgCK4M0SCt2SY6a3WS7atFFSFYm3GyoufJBp9I%2F1pPp4fwCwMDPZXVrGGPKOd%2Fmb9Zf5Hi6kBoVx223%2FrPYTM6FtydOMC%2F98Pa%2BH4Vq0rhPuYffZQ0dAwKEeN3EeFxhhywXBBFaq3P6yaO8V8TjdJYoeXh4g2iYh%2BmibFFmmIwhFcTBDwSqgQTY%2F164qXlnb9%2B%2F0dbrXprbVMLzqmL3%2FdpmwX9k4QAoHcs0WcoArPTMAQb9mnF8oP4Jl42R2RvHdlkVQ%2BARMEfWtzEiI9oW7wGku1YaNqjnNtF3gKLV7mHZzfrNv6n9Lc6rapTJIOJS443s9LrOyQ%2FVP8mgyu%2BN6D6WzRI93KKzRp8coR0Em%2BWryeBxyxr42yj63%2FJaLrNYoJZONjb0szfkg5TBDk6YbfVLtUuRInBxX3Ul0%2FMEC8eqtshVCafd106CugaxH0%2FIGjGXdKH6QnsJHi5zxpSXm4TFynpiWR4F1YkqnBhCP8N1oQCbQ4dWnDXkWcmB4pyndImIkzvJoZRAWiLGRcbH6xrtWYv5GEdVg7RMMClvjhnrvqbL8BpdNxXDDOt%2F%2FSBjqkAayPHLG7tKUT1Me3su2addhcwOCQiH%2BLYZ9P1sTgBp%2FtYap7ZNuw69vQJCuN28OOv20cg%2BIU8n8%2BLol8M1mp3Tj3KfOL%2Fnk8WacjADaS5%2FJxXBWGI%2Bpmku1S%2FI2g4gkFAMKNo3cMFFFqNiAvSxMWbA2trB77fd8TCCC2bxP%2F0bDu%2FbiBZ0w5kjtN0xn3mjCMGvEY%2FIotRsPUrjcDYhMyHhi1q5m5&X-Amz-Signature=b36df4fa909169ad71f63af2c7f927b7fb9365251f709068c2dc6271c1ce0523&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

接下来我们介绍一下 rock MQ 常见面试题， rock MQ、卡巴卡、 rapid 卡 MQ 的区别。其实因为 MQ 它一些市场上可选的产品非常多，那么对于他们进行一个功能的比较也是常见的。那么面试官通常问你这几个 MQ 的一个区别，其实说你在开发过程中也会涉及到一个技术选型，那么基础选型应该去分析我们当前的业务场景，以及各个不同产品它的一个特性，找一个匹配关系，那么基于这个匹配关系找到我们最合适的一个产品，那么我们要对它进行一个区别的一些分析，我们可以基于哪几方面？对于他们，我们可以基于他们，比如说这个产品的背景，比如说 rock MQ，他是阿里做一个背书，那么 Kafka 最早是领英出来的这样一种背书，还有就是它开发语言。我们可以知道对于 rock MQ 它是Java，那么引沐与 Java 的受众非常多，所以说 rock MQ 现在我们，尤其是交易领域非常受欢迎。


另外就是说它的受欢迎程度，当然是我们通常我们能听到的，这些产品一般是受欢迎非常高的，比如说像 rock MQ、 Kafka 或Rubmq，他们都非常受欢迎，以及他们的文档丰富度，这里面的文档丰富度也就是说我们有充分的文档，所以说我们上手也比较容易碰到问题有方法进行解决。


当然我们基于国情还可以补充，那么中文档的丰富度，或者说是这个产品是否符合中国的国情等等。当然对于一些我们这些软件的开源产品跟我们符合国情，这个可能我们关注度会比较少，但由于现在的这些政治原因，我们选国产的一些产品可能会更受欢迎一些。另外还有就是这个产品的具体的一些功能的future，那么我们来具体来说，比如说 rock MQ，它是我们知道是阿里开源的，它在阿里的整体的一些各个业务线做了大量的验证以后，它后面相当于是贡献给阿巴奇，作为一个支持我们金融级交易的一个消息产品Kafka，其实 Kafka 它的特性非常鲜明， Kafka 就是说它的吞吐量非常高，它是领英的开源的分布式的一个订阅消息组件 Kafka 因为它的吞吐量非常高，经常用于在一个日志的收集的一些场景。但是它因为不支持事务，对消息的一些重复丢失错误并没有严格的要求。所以说通常在交易环节我们会选 rap m q，很少选Kafka。


那么另外我们来介绍一下 rap MQ RABMQ 它是用阿尔兰语言开发的一个消息队列，它是基于 AMQP 协议来实现这个其实 string 对于 string 的message，它集成了比较早。对于 AMQP 的主要特征是它面向消息，面向队列路由，包括点对点的发布，订阅，可靠，安全性都非常好。


MQB 协议更多的在一些企业系统对数据的一致性、稳定性和可靠性的要求比较高的一个场景对性能和吞吐量的要求其实相对比较低，所以说对于 Rabi MQ，因为它对于可靠性要求比较高，所以说它也比较适合用于在一些金融交易的场景。另外还有一些其他的一些可比较的一些端，比如说我们对于这消息它是否支持一些事务消息，是否支持一些延迟队列等等这些特性。


那么基于各种特性的一些比较的话，其实我们最终在选择的过程中，我们选择 rock MQ，另外 rock MQ 它的受宽程度的增长曲线也非常好。那么做完这些介绍以后，我们可以总结一下各个产品它的一些优点，这样的话基本上能命中面试官他臆想的内容。比如说像 rock MQ 我们可以这样去想，它的模型非常简单，接口比较易用，也在阿里中大规模应用，所以说它的可信性，也就是可靠性，或者说受信的程度会比较高一些。比如说在支付宝、余额宝这些产品中都在使用 rock MQ，那么集群规模可能比较大，它有几十台或上百台等等，单日的处理消息上百亿，基于这些背景的话，它的性能比较好，也可以进行对于大量堆积消息，在 broker 中进行一个快速消费。同时它也支持像一些集群负载惊鸿的消费模式，也支持一个广播消费模式，开发也比较活跃，尤其是版本更新会非常快。


这是我们可以理解为是 rock MQ 的一些优点。那么它有没有哪些缺点？这里面的缺点，其实我们优点介绍很多，如果真的要说它的缺点，我们可以举其他产品的优势跟它比较，那么当然像 kafka 它的吞吐量比较大，那么 rock m q 与 kafka 比吞吐量的话，那就是 rockmq 它的缺点了。


那么接下来我们来看看一下 rapid MQ，那么 rapid MQ 它是 Allen 语言的一个特性， MQ 它的性能非常好，那么管理界面也得到大家的认可，互联网公司也有大功能应用，支持 MQP 等等这些协议，那么它的缺点也比较明显，因为尔兰语言的话它的难度相对比较大，也不能说难度比较大，就是它的受众少。


因为你看我们现在对于像 c 语言，或者说是我们的 Java 这些是受众量比较多的，那么对于像 go 语言现在也越来越受欢迎，但是像 Allen 语言其实并没有那些受欢迎度增长的一个迹象，所以说大家用这种方式进行扩展会比较稍微比较受受制一些。对于 Kafka 的话，其实这个 Kafka 我们了解的比较多，通常刚才也跟大家介绍Kafka，它最大的优点就是它的吞吐量比较大，它的缺点也是对于它并不适合交易环境，它其实对于这些对于 MQ 的重复，或者说是它的一些准确性其实要求并不是很高，所以说我们基于这几点把他们的特性介绍出来，通常也就达到我们的目的了。


