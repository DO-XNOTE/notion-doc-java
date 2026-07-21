---
title: 1-2 Spring家族生态介绍（0730）
---

# 1-2 Spring家族生态介绍（0730）

[image](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/695baaaa-790f-4791-ad59-bcf2c7bf3329/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466Z6E67F3K%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T231944Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIAJItenJaw8B9CJvFSeQdmkTHLEd1ghJSBQhujCvh5v%2BAiEArYDlKEfb0Yy3VAuj2zP%2Byfq%2F9m3pbU%2FWy4jqA8wOf40qiAQIxv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDJW7AiPN%2FxgnNOoD1SrcA152S32UGuNO%2FRtaN2mHTxC2kAPN0UOtSPnZjo%2B5OK1B8VF9kzM9tRUJv7BDwRYLXZIKmEKgTyTZf6iyIsm%2FZgDEcqy2NzMkP1zfnWT1JMurI1h6WK3Xn%2Bf9MBaRTqOJfz97A9OvtRgKwd5OdW13OxEPznQBVymEytpB%2BA3X6CUZHLVoiDXKY1%2Bbdyox00ILiAyAKbpwiTEorlycaX6YDOmaiRCQk4D6hTtvSkZyUR%2B3g7%2BrgGt2dLzobIA8bFT7f%2FrWLUJBJ3gS8oiV7JUtBAitga05RbMbTaP4Z%2BPyo0HTrLs7m%2FFPJVuS4ZJlO1LlhFUeZKCl9N2qABWWJ5trVe5fcb33lhC06g%2FZdTP0%2BqehsQhJvJ8cbtMwaAX%2Fv16pQVJzLNa4jo88L4N7Qm1BQcl12ZGidBGv1EsK6%2FXPrDha%2FrcN7xOqaFeldDCLfds4oSm%2FyKxEx%2BsMl8dZ%2Bh4LWlNTel9OB6Rsw6BaXDbwi5QkLpn7KkCaMOeXFT5QEHVmGslZ6gdqWisp0kpLXbA%2BREfLBDmWv6MMZaxm0YhxEUV27QAjqzhOhus33krgq0x%2BN03Hf%2BZhBGMBdRdIacm4Prhu6d2YsZNCwRkHul63D%2F4OOekBE9s5aXSkTe7gMK%2B3%2F9IGOqUBILzNzvpAz2pW2vT5ffejT6uzPmjRIkSJVXwRNhxakmogzuhFBfh6f8oDgsMiTDXJbgv%2BdjfyhaoCTP3j441Cb%2F3GbRt5wSPlA8Ybl5IRJtPo8%2F7sXqufHo2xknfStlLA%2FGhpt8av5MKQOiTOmfTnhitdaz%2FxMQlqPzA1HrLMJv6WqvdzoW7xSndv09nwrJ6NSKIbj8uM6fwOqbBCBoMhaATRCIYt&X-Amz-Signature=e63e5ca3dd35f356210d4201e24ca38028b27060581ec822a97259046c7177aa&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

大家好，现在我们来了解 spring 家族生态，介绍 spring 家族生态，我们从三个角度入手，分别是 spring 是什么， spring 的发展历史， spring 的家族曾代这三部分。

[image](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/3cabc865-89cc-4108-8260-e5ed7725a793/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466Z6E67F3K%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T231944Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIAJItenJaw8B9CJvFSeQdmkTHLEd1ghJSBQhujCvh5v%2BAiEArYDlKEfb0Yy3VAuj2zP%2Byfq%2F9m3pbU%2FWy4jqA8wOf40qiAQIxv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDJW7AiPN%2FxgnNOoD1SrcA152S32UGuNO%2FRtaN2mHTxC2kAPN0UOtSPnZjo%2B5OK1B8VF9kzM9tRUJv7BDwRYLXZIKmEKgTyTZf6iyIsm%2FZgDEcqy2NzMkP1zfnWT1JMurI1h6WK3Xn%2Bf9MBaRTqOJfz97A9OvtRgKwd5OdW13OxEPznQBVymEytpB%2BA3X6CUZHLVoiDXKY1%2Bbdyox00ILiAyAKbpwiTEorlycaX6YDOmaiRCQk4D6hTtvSkZyUR%2B3g7%2BrgGt2dLzobIA8bFT7f%2FrWLUJBJ3gS8oiV7JUtBAitga05RbMbTaP4Z%2BPyo0HTrLs7m%2FFPJVuS4ZJlO1LlhFUeZKCl9N2qABWWJ5trVe5fcb33lhC06g%2FZdTP0%2BqehsQhJvJ8cbtMwaAX%2Fv16pQVJzLNa4jo88L4N7Qm1BQcl12ZGidBGv1EsK6%2FXPrDha%2FrcN7xOqaFeldDCLfds4oSm%2FyKxEx%2BsMl8dZ%2Bh4LWlNTel9OB6Rsw6BaXDbwi5QkLpn7KkCaMOeXFT5QEHVmGslZ6gdqWisp0kpLXbA%2BREfLBDmWv6MMZaxm0YhxEUV27QAjqzhOhus33krgq0x%2BN03Hf%2BZhBGMBdRdIacm4Prhu6d2YsZNCwRkHul63D%2F4OOekBE9s5aXSkTe7gMK%2B3%2F9IGOqUBILzNzvpAz2pW2vT5ffejT6uzPmjRIkSJVXwRNhxakmogzuhFBfh6f8oDgsMiTDXJbgv%2BdjfyhaoCTP3j441Cb%2F3GbRt5wSPlA8Ybl5IRJtPo8%2F7sXqufHo2xknfStlLA%2FGhpt8av5MKQOiTOmfTnhitdaz%2FxMQlqPzA1HrLMJv6WqvdzoW7xSndv09nwrJ6NSKIbj8uM6fwOqbBCBoMhaATRCIYt&X-Amz-Signature=9d451dcca70c8a6bd7f5c347605e240c59ffb7432d2b8e3f36ab2b1c9397741d&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

那么首先我们看 spring 是什么呢？面对如此直接的问题，大家怎么想？如果面试官抛出这样个问题，大家会怎么说？


这其实也是面试常见题，大多数同学会背课文一样说 spring 4，一个实现了 IOC 和 AOP 的容器框架，可以简化企业应用的开发，巴拉可以说很多，这样当然没错，但是亮点不足，我们怎么去解释呢？我们可以这样看，早期说 spring 是指 spring framework，


单纯的说 spring 框架发展到现在也包含了 spring core， spring context、 spring AOP、 spring MVC 等模块，当时 spring 框架就是 spring 的全部加大，所以大多数同学对 spring 的理解，或者说很多博客文章孩子基于早期的 spring 的概念在做传播。


现在 spring 包含了 spring io 下面所有的项目模块儿，我们可以打开 spring io 的官方网站，比如比较大的一些模块儿，如 spring m boot， spring Claude， spring date，这些项目都是基于 spring 核心容器为基础发展的。现在单独说 spring 更大的概念是在说 spring 这一系列的项目，这一系列项目逐步构成了 spring 的家族生态，所以现在建议细化为 spring boot， spring AC 等等。也就是说因为我们每一个模块都足够聊半天，所以说我们不要单纯的去说 spring 是什么，我们更建议大家说 spring 的具体某个模块儿，它解决了什么问题。

[image](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/8df2cac4-5f0b-42b2-be35-d49ebf3ed764/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466Z6E67F3K%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T231944Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIAJItenJaw8B9CJvFSeQdmkTHLEd1ghJSBQhujCvh5v%2BAiEArYDlKEfb0Yy3VAuj2zP%2Byfq%2F9m3pbU%2FWy4jqA8wOf40qiAQIxv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDJW7AiPN%2FxgnNOoD1SrcA152S32UGuNO%2FRtaN2mHTxC2kAPN0UOtSPnZjo%2B5OK1B8VF9kzM9tRUJv7BDwRYLXZIKmEKgTyTZf6iyIsm%2FZgDEcqy2NzMkP1zfnWT1JMurI1h6WK3Xn%2Bf9MBaRTqOJfz97A9OvtRgKwd5OdW13OxEPznQBVymEytpB%2BA3X6CUZHLVoiDXKY1%2Bbdyox00ILiAyAKbpwiTEorlycaX6YDOmaiRCQk4D6hTtvSkZyUR%2B3g7%2BrgGt2dLzobIA8bFT7f%2FrWLUJBJ3gS8oiV7JUtBAitga05RbMbTaP4Z%2BPyo0HTrLs7m%2FFPJVuS4ZJlO1LlhFUeZKCl9N2qABWWJ5trVe5fcb33lhC06g%2FZdTP0%2BqehsQhJvJ8cbtMwaAX%2Fv16pQVJzLNa4jo88L4N7Qm1BQcl12ZGidBGv1EsK6%2FXPrDha%2FrcN7xOqaFeldDCLfds4oSm%2FyKxEx%2BsMl8dZ%2Bh4LWlNTel9OB6Rsw6BaXDbwi5QkLpn7KkCaMOeXFT5QEHVmGslZ6gdqWisp0kpLXbA%2BREfLBDmWv6MMZaxm0YhxEUV27QAjqzhOhus33krgq0x%2BN03Hf%2BZhBGMBdRdIacm4Prhu6d2YsZNCwRkHul63D%2F4OOekBE9s5aXSkTe7gMK%2B3%2F9IGOqUBILzNzvpAz2pW2vT5ffejT6uzPmjRIkSJVXwRNhxakmogzuhFBfh6f8oDgsMiTDXJbgv%2BdjfyhaoCTP3j441Cb%2F3GbRt5wSPlA8Ybl5IRJtPo8%2F7sXqufHo2xknfStlLA%2FGhpt8av5MKQOiTOmfTnhitdaz%2FxMQlqPzA1HrLMJv6WqvdzoW7xSndv09nwrJ6NSKIbj8uM6fwOqbBCBoMhaATRCIYt&X-Amz-Signature=88d501f8ec1971627ccaa2573d167d1be936d2c22417a659661c325c59d9483c&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)


好，下面我们看 spring 的发展历史。按基础使用角度来说，我们不关心 spring 过去是什么，更关心 spring 现在能做什么。出于尊重，以自瞻仰，我们来了解一下 spring 发展的历史，也感受一下软件企业的发展变迁。


首先， spring 的起点。 2002 年 10 月， 

[image](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/a2a5b769-7f77-486e-9647-39e1877106ba/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466Z6E67F3K%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T231944Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIAJItenJaw8B9CJvFSeQdmkTHLEd1ghJSBQhujCvh5v%2BAiEArYDlKEfb0Yy3VAuj2zP%2Byfq%2F9m3pbU%2FWy4jqA8wOf40qiAQIxv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDJW7AiPN%2FxgnNOoD1SrcA152S32UGuNO%2FRtaN2mHTxC2kAPN0UOtSPnZjo%2B5OK1B8VF9kzM9tRUJv7BDwRYLXZIKmEKgTyTZf6iyIsm%2FZgDEcqy2NzMkP1zfnWT1JMurI1h6WK3Xn%2Bf9MBaRTqOJfz97A9OvtRgKwd5OdW13OxEPznQBVymEytpB%2BA3X6CUZHLVoiDXKY1%2Bbdyox00ILiAyAKbpwiTEorlycaX6YDOmaiRCQk4D6hTtvSkZyUR%2B3g7%2BrgGt2dLzobIA8bFT7f%2FrWLUJBJ3gS8oiV7JUtBAitga05RbMbTaP4Z%2BPyo0HTrLs7m%2FFPJVuS4ZJlO1LlhFUeZKCl9N2qABWWJ5trVe5fcb33lhC06g%2FZdTP0%2BqehsQhJvJ8cbtMwaAX%2Fv16pQVJzLNa4jo88L4N7Qm1BQcl12ZGidBGv1EsK6%2FXPrDha%2FrcN7xOqaFeldDCLfds4oSm%2FyKxEx%2BsMl8dZ%2Bh4LWlNTel9OB6Rsw6BaXDbwi5QkLpn7KkCaMOeXFT5QEHVmGslZ6gdqWisp0kpLXbA%2BREfLBDmWv6MMZaxm0YhxEUV27QAjqzhOhus33krgq0x%2BN03Hf%2BZhBGMBdRdIacm4Prhu6d2YsZNCwRkHul63D%2F4OOekBE9s5aXSkTe7gMK%2B3%2F9IGOqUBILzNzvpAz2pW2vT5ffejT6uzPmjRIkSJVXwRNhxakmogzuhFBfh6f8oDgsMiTDXJbgv%2BdjfyhaoCTP3j441Cb%2F3GbRt5wSPlA8Ybl5IRJtPo8%2F7sXqufHo2xknfStlLA%2FGhpt8av5MKQOiTOmfTnhitdaz%2FxMQlqPzA1HrLMJv6WqvdzoW7xSndv09nwrJ6NSKIbj8uM6fwOqbBCBoMhaATRCIYt&X-Amz-Signature=d30aa794c7e0b706665f437e7bfcb6bbd812b48b3f62993480775b9da6ae1348&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

[image](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/012d2733-77a9-44c0-970f-288aef7a0939/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466Z6E67F3K%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T231944Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIAJItenJaw8B9CJvFSeQdmkTHLEd1ghJSBQhujCvh5v%2BAiEArYDlKEfb0Yy3VAuj2zP%2Byfq%2F9m3pbU%2FWy4jqA8wOf40qiAQIxv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDJW7AiPN%2FxgnNOoD1SrcA152S32UGuNO%2FRtaN2mHTxC2kAPN0UOtSPnZjo%2B5OK1B8VF9kzM9tRUJv7BDwRYLXZIKmEKgTyTZf6iyIsm%2FZgDEcqy2NzMkP1zfnWT1JMurI1h6WK3Xn%2Bf9MBaRTqOJfz97A9OvtRgKwd5OdW13OxEPznQBVymEytpB%2BA3X6CUZHLVoiDXKY1%2Bbdyox00ILiAyAKbpwiTEorlycaX6YDOmaiRCQk4D6hTtvSkZyUR%2B3g7%2BrgGt2dLzobIA8bFT7f%2FrWLUJBJ3gS8oiV7JUtBAitga05RbMbTaP4Z%2BPyo0HTrLs7m%2FFPJVuS4ZJlO1LlhFUeZKCl9N2qABWWJ5trVe5fcb33lhC06g%2FZdTP0%2BqehsQhJvJ8cbtMwaAX%2Fv16pQVJzLNa4jo88L4N7Qm1BQcl12ZGidBGv1EsK6%2FXPrDha%2FrcN7xOqaFeldDCLfds4oSm%2FyKxEx%2BsMl8dZ%2Bh4LWlNTel9OB6Rsw6BaXDbwi5QkLpn7KkCaMOeXFT5QEHVmGslZ6gdqWisp0kpLXbA%2BREfLBDmWv6MMZaxm0YhxEUV27QAjqzhOhus33krgq0x%2BN03Hf%2BZhBGMBdRdIacm4Prhu6d2YsZNCwRkHul63D%2F4OOekBE9s5aXSkTe7gMK%2B3%2F9IGOqUBILzNzvpAz2pW2vT5ffejT6uzPmjRIkSJVXwRNhxakmogzuhFBfh6f8oDgsMiTDXJbgv%2BdjfyhaoCTP3j441Cb%2F3GbRt5wSPlA8Ybl5IRJtPo8%2F7sXqufHo2xknfStlLA%2FGhpt8av5MKQOiTOmfTnhitdaz%2FxMQlqPzA1HrLMJv6WqvdzoW7xSndv09nwrJ6NSKIbj8uM6fwOqbBCBoMhaATRCIYt&X-Amz-Signature=826788b4c8d5f8ec1c1172389710de6a003b4a08456faacce374ba5cac322d32&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

road Jason 写一本 Java EE 设计和开发的书，这个数涵盖了当时 Java 企业应用程序开发的状态，并指出 Java e 和 EJB 组件框架的一些主要缺陷。在书中，他提出了一个基于普通 Java 类 PORTAL 和依赖注屋的简单解决方案，它包括许多可重用的 Java 接口和类比，如 application context 和 be infactory 则最早出现在 2003 年2月。 road Urgan 一样，它们创建了开源项目。


spring 之所以叫 spring 这个名字，它的寓意是 spring 在传统的 j to e 的冬天之后，代表了一个新的开始。在 2004 年3月， spring 1. 0 发布，当时归属 INTERFACE 21，公司在这个期间进行。 spring 框架发生了快速的增长，很快它的下载量超过 100 万。在 2007 年 11 月， spring 2. 5 发布，它的历史价值就是在支持了注解配置，同时公司更名为 spring source。



2009 年 12 月， spring 3. 0 发布。 string 3. 0 具有许多主要功能，包括支持 string 的表达式语言，也就是 string e r 基于 Java 的 bin 配置，单词的归属公式是 warm where，也就是著名的虚拟机软件厂商。


2013 年 12 月， spring 4. 0 发布，公司为 Preto 4. 0，主要支持加8。 2014 年4月，发布了 spring boot 1. 0，同年 10 月发布了 spring Claude。这两个项目的发布跟 spring 家族带来了新的篇章，稳固了 spring 的生态体系 Java 4G 的地位。 2017 年9月， spring 5. 0 发布，同时支持了显扬寺编程。 2018 年3月， spring 部的 2. 0 发布，它是基于 spring 构建的，同时升级了一下依赖的软件版本。


到目前为止， spring 的子项目依然在如火如荼的发展，尤其是近两年， spring Booth 和 spring Claude 成为了面试必选题，也有一些项目由于各种原因停止维护了， spring 的归属公司也几经变化，经历搜购和被搜购，包括创始人 Rod 的离开都没有影响 spring 的快速发展。我们不得不感慨， spring 的基因真的很强大。



好，我们接下来看 spring 的家族生态。看到这个图，感觉还是有点震撼。 spring 项目已经覆盖到开发的各个层级，从左到右分别是 Web 层、 common 层、 survey 层、 date 层，四个层级都有覆盖中心是我们的 spring framework。 

[image](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/191ad28a-9a16-4c62-92c9-53d9ed858ed9/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466Z6E67F3K%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T231944Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIAJItenJaw8B9CJvFSeQdmkTHLEd1ghJSBQhujCvh5v%2BAiEArYDlKEfb0Yy3VAuj2zP%2Byfq%2F9m3pbU%2FWy4jqA8wOf40qiAQIxv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDJW7AiPN%2FxgnNOoD1SrcA152S32UGuNO%2FRtaN2mHTxC2kAPN0UOtSPnZjo%2B5OK1B8VF9kzM9tRUJv7BDwRYLXZIKmEKgTyTZf6iyIsm%2FZgDEcqy2NzMkP1zfnWT1JMurI1h6WK3Xn%2Bf9MBaRTqOJfz97A9OvtRgKwd5OdW13OxEPznQBVymEytpB%2BA3X6CUZHLVoiDXKY1%2Bbdyox00ILiAyAKbpwiTEorlycaX6YDOmaiRCQk4D6hTtvSkZyUR%2B3g7%2BrgGt2dLzobIA8bFT7f%2FrWLUJBJ3gS8oiV7JUtBAitga05RbMbTaP4Z%2BPyo0HTrLs7m%2FFPJVuS4ZJlO1LlhFUeZKCl9N2qABWWJ5trVe5fcb33lhC06g%2FZdTP0%2BqehsQhJvJ8cbtMwaAX%2Fv16pQVJzLNa4jo88L4N7Qm1BQcl12ZGidBGv1EsK6%2FXPrDha%2FrcN7xOqaFeldDCLfds4oSm%2FyKxEx%2BsMl8dZ%2Bh4LWlNTel9OB6Rsw6BaXDbwi5QkLpn7KkCaMOeXFT5QEHVmGslZ6gdqWisp0kpLXbA%2BREfLBDmWv6MMZaxm0YhxEUV27QAjqzhOhus33krgq0x%2BN03Hf%2BZhBGMBdRdIacm4Prhu6d2YsZNCwRkHul63D%2F4OOekBE9s5aXSkTe7gMK%2B3%2F9IGOqUBILzNzvpAz2pW2vT5ffejT6uzPmjRIkSJVXwRNhxakmogzuhFBfh6f8oDgsMiTDXJbgv%2BdjfyhaoCTP3j441Cb%2F3GbRt5wSPlA8Ybl5IRJtPo8%2F7sXqufHo2xknfStlLA%2FGhpt8av5MKQOiTOmfTnhitdaz%2FxMQlqPzA1HrLMJv6WqvdzoW7xSndv09nwrJ6NSKIbj8uM6fwOqbBCBoMhaATRCIYt&X-Amz-Signature=0fe3b27a9e5895d5c94c80e642b8723aaca853207d66054b218759c98648de9f&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

spring framework 是整个 spring 生态的基础，它包含了 spring 最核心的功能，比如说LCAOP、 spring VC、 spring test 等等。下面的 spring boot 的 logo 看起来像个电源按钮。


spring boot 是一个开发基于 spring 的脚手架项目，它默认集成了嵌入式的 Tom cat，支持配字注解化，支持快速集成第三方开发组件，比如 my Betas 等等，大大降低了 spring 的门槛，而且内置了许多可以直接使用于生产环境的功能，是目前用于开发微服务架构项目的不二选择。


这边的 spring Claude，它作为开发基于微服务架构的软件系统，提供了一整套工具集合，其中包含了开发各种微服务组件的具体项目，比如配置中心、服务注册中心、服务调度、监控服务网关等等。 spring close 的基础是 spring boot，基于 spring boot 可以大大简化开发各种微服务组件的流程。右边的 spring data 自带提供一套基于 spring 编程模型的数据访问API，是一个数据访问框架集合，其中包含了多个具体的支持不同方式访问特定数据库类型的子模块，如 spring day 的DDBC， spring date JPA， spring date MongoDB， spring date Redis 等等。这个模块的功能类似于 Mybetty 字样专门的 OIM 框架，在实际开发中可以根据需求进行灵活选择。同时这边的 spring integration，它的目的是提供一个简单的模型，用于构建企业级应用的集成方案。另外注意前面这个圆环的中心，也就是 strong secured，它实现了认证和授权以及访问控制的安全框架。


spring security 提供了非常丰富的安全控制功能，在这里作为所有数据的入口的核心控制，真是具有一副党官万夫莫开的气势，像 map 层里面设计的 spring for Android、 spring for Ketos、 spring Mobile， spring Wiveflow，这些它都可以理解为我们 spring 提供的一些数据入口，它跟 spring security 关联起来，也就是做到我们权限控制的同义。


当然，这里还有 spring or depth 轻型目录访问协议，主要是适用于跟企业预账户单点登录信息的读取，另外 spring bytes 是用于批处理任务。其他模块我们就不一一介绍了。看到这里，大家应该是能充分感受到 spring 生态的强大，这一节我们就介绍到这里，再见。


