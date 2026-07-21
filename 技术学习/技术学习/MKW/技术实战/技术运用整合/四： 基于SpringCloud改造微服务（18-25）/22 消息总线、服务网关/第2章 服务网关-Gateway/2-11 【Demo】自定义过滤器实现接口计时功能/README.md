---
title: 2-11 【Demo】自定义过滤器实现接口计时功能
---

# 2-11 【Demo】自定义过滤器实现接口计时功能

[image](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/e886120d-e52e-4ee6-931d-9a4a9b7b965b/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666XHXXSDH%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T225738Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIFoeitmcHHkRPy91y4VN29ZvCUrSnVCOVAt%2FKY79An1cAiAllc0G3qH%2FwzyExKc1k%2FYwJxNrpP2M6jA%2BoCr7vzXi1yqIBAjG%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMIWtq6uzYtCs5hqNJKtwDEsB%2FsD%2BciqM0%2B%2FxCjWhsWYT%2BOZTIJNjnDyo2uKlUrbIXIjIlsAyTfGwnR4rYQp%2BEWuBKsn2UlgZoSruc%2FLiTKJy%2FtsOlrM9fvyIvqxMA%2FSP8X%2B3NYPsKU5d%2FAG4NlliUtDRb6xCjLjVUcb5yjVB80gPseQcV22uQex0N7M5I8Eo%2BHQqaRzRHV%2BIDi1g97lstm7MeTYUmxas%2Fcje2FizATplroOx41TMpYgSA1PgiOyR1RpDR62f5piybcEECIQBhiBjNFCM%2BMdbtQwRLrxp3JDTDF8188X7D1CqZmP%2BTN4nLw4X4YsZ%2F45HbBJJUZspAhHLRxQROxheF8orLHYvsMTHy8cXuB8TEDfFS32Ai1eygfbIEV0Rt2E%2FF7poGbferyKOg%2FCV2pLx%2BttbkGK2YpXT8WDKxdDpF5IqiDrkRutRDScrRmlJo0DGoXPKX2Hx%2B8sAtH%2FPMl6kaEnsHNlgQ%2Bmaica1tCYwvfvr0ao%2BNstVcdbIIUUF1%2B12AdWRT2yXKGG87IG2NjI%2BlmkKQbW%2F%2F4U%2B2GIp4XIyBfzgme0pPSvDbXdYzzua7modyfTNOPulot1B45h6M6NhAxXLlfqGltvMkm%2FzKYdoQHEPIfLfUYDkX6GB16j4AssXueNUwn7r%2F0gY6pgGUGtfsnB0knPZIpZ%2F7ELezZwy2hIytG6JB8MvepxYjhJ5U5DaG1xpZwUUgs0F%2B2xbWp0Hc1ydaVDemuuNzSo1ydwohTWEg%2Fqp%2BAj9qKmzkYRuekKjDnKRzxsiPbk5zf%2FO%2BcB6USPMVMRO%2B3ldnDlq6x5NTB0rfoxBj9bP43ikuzkuOUh0JgotmTceQRjsO7h29kgg06tinQVGx1Hnp6XQ5BH2KAPJA&X-Amz-Signature=a54df81e350c6ee74ea58f2197ff914b235b8f2b868773f60dbf8fa08206db09&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

[image](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/ef43559f-41f8-401e-bf69-35b02efa452b/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666XHXXSDH%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T225738Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIFoeitmcHHkRPy91y4VN29ZvCUrSnVCOVAt%2FKY79An1cAiAllc0G3qH%2FwzyExKc1k%2FYwJxNrpP2M6jA%2BoCr7vzXi1yqIBAjG%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMIWtq6uzYtCs5hqNJKtwDEsB%2FsD%2BciqM0%2B%2FxCjWhsWYT%2BOZTIJNjnDyo2uKlUrbIXIjIlsAyTfGwnR4rYQp%2BEWuBKsn2UlgZoSruc%2FLiTKJy%2FtsOlrM9fvyIvqxMA%2FSP8X%2B3NYPsKU5d%2FAG4NlliUtDRb6xCjLjVUcb5yjVB80gPseQcV22uQex0N7M5I8Eo%2BHQqaRzRHV%2BIDi1g97lstm7MeTYUmxas%2Fcje2FizATplroOx41TMpYgSA1PgiOyR1RpDR62f5piybcEECIQBhiBjNFCM%2BMdbtQwRLrxp3JDTDF8188X7D1CqZmP%2BTN4nLw4X4YsZ%2F45HbBJJUZspAhHLRxQROxheF8orLHYvsMTHy8cXuB8TEDfFS32Ai1eygfbIEV0Rt2E%2FF7poGbferyKOg%2FCV2pLx%2BttbkGK2YpXT8WDKxdDpF5IqiDrkRutRDScrRmlJo0DGoXPKX2Hx%2B8sAtH%2FPMl6kaEnsHNlgQ%2Bmaica1tCYwvfvr0ao%2BNstVcdbIIUUF1%2B12AdWRT2yXKGG87IG2NjI%2BlmkKQbW%2F%2F4U%2B2GIp4XIyBfzgme0pPSvDbXdYzzua7modyfTNOPulot1B45h6M6NhAxXLlfqGltvMkm%2FzKYdoQHEPIfLfUYDkX6GB16j4AssXueNUwn7r%2F0gY6pgGUGtfsnB0knPZIpZ%2F7ELezZwy2hIytG6JB8MvepxYjhJ5U5DaG1xpZwUUgs0F%2B2xbWp0Hc1ydaVDemuuNzSo1ydwohTWEg%2Fqp%2BAj9qKmzkYRuekKjDnKRzxsiPbk5zf%2FO%2BcB6USPMVMRO%2B3ldnDlq6x5NTB0rfoxBj9bP43ikuzkuOUh0JgotmTceQRjsO7h29kgg06tinQVGx1Hnp6XQ5BH2KAPJA&X-Amz-Signature=f57462f60a0b1351997ae23a549c107f78269a1948203905bc4c95d5b5ce966a&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

[image](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/e15ddad7-5ce3-4149-8c3b-caa2000b1862/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666XHXXSDH%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T225738Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIFoeitmcHHkRPy91y4VN29ZvCUrSnVCOVAt%2FKY79An1cAiAllc0G3qH%2FwzyExKc1k%2FYwJxNrpP2M6jA%2BoCr7vzXi1yqIBAjG%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMIWtq6uzYtCs5hqNJKtwDEsB%2FsD%2BciqM0%2B%2FxCjWhsWYT%2BOZTIJNjnDyo2uKlUrbIXIjIlsAyTfGwnR4rYQp%2BEWuBKsn2UlgZoSruc%2FLiTKJy%2FtsOlrM9fvyIvqxMA%2FSP8X%2B3NYPsKU5d%2FAG4NlliUtDRb6xCjLjVUcb5yjVB80gPseQcV22uQex0N7M5I8Eo%2BHQqaRzRHV%2BIDi1g97lstm7MeTYUmxas%2Fcje2FizATplroOx41TMpYgSA1PgiOyR1RpDR62f5piybcEECIQBhiBjNFCM%2BMdbtQwRLrxp3JDTDF8188X7D1CqZmP%2BTN4nLw4X4YsZ%2F45HbBJJUZspAhHLRxQROxheF8orLHYvsMTHy8cXuB8TEDfFS32Ai1eygfbIEV0Rt2E%2FF7poGbferyKOg%2FCV2pLx%2BttbkGK2YpXT8WDKxdDpF5IqiDrkRutRDScrRmlJo0DGoXPKX2Hx%2B8sAtH%2FPMl6kaEnsHNlgQ%2Bmaica1tCYwvfvr0ao%2BNstVcdbIIUUF1%2B12AdWRT2yXKGG87IG2NjI%2BlmkKQbW%2F%2F4U%2B2GIp4XIyBfzgme0pPSvDbXdYzzua7modyfTNOPulot1B45h6M6NhAxXLlfqGltvMkm%2FzKYdoQHEPIfLfUYDkX6GB16j4AssXueNUwn7r%2F0gY6pgGUGtfsnB0knPZIpZ%2F7ELezZwy2hIytG6JB8MvepxYjhJ5U5DaG1xpZwUUgs0F%2B2xbWp0Hc1ydaVDemuuNzSo1ydwohTWEg%2Fqp%2BAj9qKmzkYRuekKjDnKRzxsiPbk5zf%2FO%2BcB6USPMVMRO%2B3ldnDlq6x5NTB0rfoxBj9bP43ikuzkuOUh0JgotmTceQRjsO7h29kgg06tinQVGx1Hnp6XQ5BH2KAPJA&X-Amz-Signature=5ac00481577a61654351aab9088beb834797e1ef1bc996f60c64c1cbf86e4a93&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

[image](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/a67c1c7b-283d-4e70-b283-5e0f98c913b1/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666XHXXSDH%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T225738Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIFoeitmcHHkRPy91y4VN29ZvCUrSnVCOVAt%2FKY79An1cAiAllc0G3qH%2FwzyExKc1k%2FYwJxNrpP2M6jA%2BoCr7vzXi1yqIBAjG%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMIWtq6uzYtCs5hqNJKtwDEsB%2FsD%2BciqM0%2B%2FxCjWhsWYT%2BOZTIJNjnDyo2uKlUrbIXIjIlsAyTfGwnR4rYQp%2BEWuBKsn2UlgZoSruc%2FLiTKJy%2FtsOlrM9fvyIvqxMA%2FSP8X%2B3NYPsKU5d%2FAG4NlliUtDRb6xCjLjVUcb5yjVB80gPseQcV22uQex0N7M5I8Eo%2BHQqaRzRHV%2BIDi1g97lstm7MeTYUmxas%2Fcje2FizATplroOx41TMpYgSA1PgiOyR1RpDR62f5piybcEECIQBhiBjNFCM%2BMdbtQwRLrxp3JDTDF8188X7D1CqZmP%2BTN4nLw4X4YsZ%2F45HbBJJUZspAhHLRxQROxheF8orLHYvsMTHy8cXuB8TEDfFS32Ai1eygfbIEV0Rt2E%2FF7poGbferyKOg%2FCV2pLx%2BttbkGK2YpXT8WDKxdDpF5IqiDrkRutRDScrRmlJo0DGoXPKX2Hx%2B8sAtH%2FPMl6kaEnsHNlgQ%2Bmaica1tCYwvfvr0ao%2BNstVcdbIIUUF1%2B12AdWRT2yXKGG87IG2NjI%2BlmkKQbW%2F%2F4U%2B2GIp4XIyBfzgme0pPSvDbXdYzzua7modyfTNOPulot1B45h6M6NhAxXLlfqGltvMkm%2FzKYdoQHEPIfLfUYDkX6GB16j4AssXueNUwn7r%2F0gY6pgGUGtfsnB0knPZIpZ%2F7ELezZwy2hIytG6JB8MvepxYjhJ5U5DaG1xpZwUUgs0F%2B2xbWp0Hc1ydaVDemuuNzSo1ydwohTWEg%2Fqp%2BAj9qKmzkYRuekKjDnKRzxsiPbk5zf%2FO%2BcB6USPMVMRO%2B3ldnDlq6x5NTB0rfoxBj9bP43ikuzkuOUh0JgotmTceQRjsO7h29kgg06tinQVGx1Hnp6XQ5BH2KAPJA&X-Amz-Signature=c9e891f9abbc686a3845596e682131e9a695845af0a9852a7a46cd5e15b54660&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

嗨慕课网的各位同学们，大家好，前面几个小节，咱学习了很多 gateway 中内置的 predicates 还有它的 filter 那么假如咱有一些特定的需求点需要扩展，而 gateway 提供出来的这些默认组件又不能满足要求，这个时候咱就要自己动手，丰衣足食，我们来 DIY 一个自定义的过滤器，这就是咱这节课程需要做的事情了。


首先我们创建一个 time filter 来实现一个计时功能。在这个计时功能中，我将跟大家展示如何在 gateway 的 filter 中实现类似 zoom filter 里的 after filter 功能。这句话听起来非常绕，也就是说如何利用回调函数在后续的调用链路完成以后执行一段自己的逻辑。那这个 filter 定义完成以后，我们来看一下如何将 filter 指定到咱已经创建好的路由规则中。咱这一节的示例只是说实现一个简单的计时功能，这里只是为了展示 filter 的可扩展点。那么同学们如果在自己的项目中需要用到其他的功能，那么可以用同样的方式 copy 不走样，创建自己的自定义过滤器，实现自己的业务逻辑。

[image](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/92c191fd-8499-4e9c-9815-1c0358058a79/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666XHXXSDH%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T225738Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIFoeitmcHHkRPy91y4VN29ZvCUrSnVCOVAt%2FKY79An1cAiAllc0G3qH%2FwzyExKc1k%2FYwJxNrpP2M6jA%2BoCr7vzXi1yqIBAjG%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMIWtq6uzYtCs5hqNJKtwDEsB%2FsD%2BciqM0%2B%2FxCjWhsWYT%2BOZTIJNjnDyo2uKlUrbIXIjIlsAyTfGwnR4rYQp%2BEWuBKsn2UlgZoSruc%2FLiTKJy%2FtsOlrM9fvyIvqxMA%2FSP8X%2B3NYPsKU5d%2FAG4NlliUtDRb6xCjLjVUcb5yjVB80gPseQcV22uQex0N7M5I8Eo%2BHQqaRzRHV%2BIDi1g97lstm7MeTYUmxas%2Fcje2FizATplroOx41TMpYgSA1PgiOyR1RpDR62f5piybcEECIQBhiBjNFCM%2BMdbtQwRLrxp3JDTDF8188X7D1CqZmP%2BTN4nLw4X4YsZ%2F45HbBJJUZspAhHLRxQROxheF8orLHYvsMTHy8cXuB8TEDfFS32Ai1eygfbIEV0Rt2E%2FF7poGbferyKOg%2FCV2pLx%2BttbkGK2YpXT8WDKxdDpF5IqiDrkRutRDScrRmlJo0DGoXPKX2Hx%2B8sAtH%2FPMl6kaEnsHNlgQ%2Bmaica1tCYwvfvr0ao%2BNstVcdbIIUUF1%2B12AdWRT2yXKGG87IG2NjI%2BlmkKQbW%2F%2F4U%2B2GIp4XIyBfzgme0pPSvDbXdYzzua7modyfTNOPulot1B45h6M6NhAxXLlfqGltvMkm%2FzKYdoQHEPIfLfUYDkX6GB16j4AssXueNUwn7r%2F0gY6pgGUGtfsnB0knPZIpZ%2F7ELezZwy2hIytG6JB8MvepxYjhJ5U5DaG1xpZwUUgs0F%2B2xbWp0Hc1ydaVDemuuNzSo1ydwohTWEg%2Fqp%2BAj9qKmzkYRuekKjDnKRzxsiPbk5zf%2FO%2BcB6USPMVMRO%2B3ldnDlq6x5NTB0rfoxBj9bP43ikuzkuOUh0JgotmTceQRjsO7h29kgg06tinQVGx1Hnp6XQ5BH2KAPJA&X-Amz-Signature=9def0fca333881e5a88db78757d2a9a13fbb687c57808e077d842a9256660863&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

OK 同学们准备好的话抄起家伙给你泰利 J 开拔编程使我快乐。 996 是我的福报，我们的微服务课程已经过半，看着 spring cloud demo 下面这么多的文件夹，高喷满座，甚是欣慰。好，我们找到这一节张中香修改的gateway ，万花丛中一点绿就是它了。 gateway 那我们骑手就在 gateway 的 Java 文件夹中创建一个类，因为咱要实现的是一个计时的 filter 所以它的名称就给它起名叫 timer filtertimer 就是计时器的意思。 OK 好，这里创建好之后，收集小桌板开始码代码了。咱既然说了这个 timer filter 是扩展 gateway 的 filter 接口，那它自然要继承那么几个其他接口了。咱的一个 timer filter 继承两个接口，一仆二主。 OK 这两个主第一个是 gateway filter 把它加上。第二个叫 ordered 其中一个就是 gateway 的 filter 接口，另外一个是指定执行顺序的一个 order 接口。好，我们这里把它的默认方法都给打出来走。你 OK 你这里看到， get order 它默认返回的是0。


同学们知道，这个 order 是越大越优先还是越小越优先它跟我们平常理解的这个优先级顺序是不一样的。我们点进去 order 的接口看一眼。同学们看，这里首先定义了两个参数，第一个叫 highest precedence 第二个是 lowest precedence 然后我们看它的高优先级实际上是指向的 integer 类型的 main value 也就是它的最小值。那么第一优先级反倒指向了最大值，说明这里你的优先级越高，那你就要把对应的值定义的越低。



那咱在 timer 接口里定义个什么数呢？同学们，我们无欲无求好不好就定一个零默认就好，顺其自然，道法自然。 Ok. 这里这个 filter 就是我们的主要的核心业务流程了。同学们可以看到它返回的这个类是不是以前没有见过呢？ mono 它是一个异步式编程的模型框架，我们点进去看出自哪 a reactor 所以这几年这种回调函数异步编程的方式在 Java 界越来越流行。你看像 spring cloud 中不光 high streaks ，很多组件都用到了这种函数式异步式调用的编程模型。这个体验和前端加入 script 非常相像。有的时候在有些场景下应用会非常非常简单。但是如果你过多的应用在项目里面，就像 high streaks 一样，你在 debug 或者跳转梳理这个业务流程的时候会感到非常困难。所以说东西是好东西，但是咱在使用的时候可不能纵浴适可而止。



同学们好，我们这里开始写它的计时器的核心流程了。这里一开始骑手给它定义一个塔 stop watch。 Stop watch. 这里有两个实现，我们就采用 spin framework 的实现。 OK 这是什么大家在项目中应该也经常用到吧，它就是给你的接口计时，而且能打出一种非常漂亮的 log 的组件。好，我们这里把它声明开来，生命完了以后，在方法开始的时候，是不是要把这个 timer 先给它开启，我们调用一个 start 方法， start 传入什么？我们这里就要用到了 exchange 把它 copy 一下。



那你从我这里想要得到什么？你是要钱还是要命啊？我哪个都不要，我就要你的 request 你 request 中的什么内容呢？你的 URI URI 这么长，说具体点要什么？要你的 raw pass ，也就是咱的访问路径同学们实际上这里可以把它打得更细致一些，我这里只不过简单的获取了一个访问路径，那么你们还可以从 request 当中挖掘更多的东西。这些东西是用在何处？当然是用到计时器打印出的 log 中。只有把信息给的全，那么你在 log 中才能看到哪一步，花费了多少时间。 OK 那这里 start 了以后要做一个手脚，什么手脚呢？咱知道这个 filter 是异步编程模型对不对？那在你结束的时候这个 return 实际上会是一个异步调用的函数一个回调函数在回调函数中，我们要把 timer 中的 log 给它输出。


```java
package com.imooc.springcloud;

import lombok.extern.slf4j.Slf4j;
import org.springframework.cloud.gateway.filter.GatewayFilter;
import org.springframework.cloud.gateway.filter.GatewayFilterChain;
import org.springframework.core.Ordered;
import org.springframework.stereotype.Component;
import org.springframework.util.StopWatch;
import org.springframework.web.server.ServerWebExchange;
import reactor.core.publisher.Mono;

/**
 * <h1>接口记时</h1>
 */
@Slf4j
@Component
public class TimerFilter implements GatewayFilter, Ordered {

    @Override
    public Mono<Void> filter(ServerWebExchange exchange, GatewayFilterChain chain) {
        StopWatch timer = new StopWatch();
        timer.start(exchange.getRequest().getURI().getRawPath());

//        exchange.getAttributes().put("requetsTimeBegin", System.currentTimeMillis());
        return chain.filter(exchange).then(
            Mono.fromRunnable(() -> {
                timer.stop();
                log.info(timer.prettyPrint());
            })

        );
    }

    @Override
    public int getOrder() {
        return 0;
    }
}
```

同学们以前有没有用过zoom ，就是这个也是 spring cloud 当中第一代的 gateway 组件。 zoo 里面有一个 filter 的类型，叫做 before filter。 After filter. 那在咱的 gateway 里面没有这种概念，所以我们如何来实现类似的 before after 的功能？那就是借助回调了你在回调业务中的逻辑，可以把它认为是 after 也就是后续的业务全部处理完以后才执行的流程。那么这就相当于用了另外一种形式曲线救国，实现了 zoo 当中的 after filter 的功能。我们接下来看怎么来实现。咱这边用到了 exchange 这不还有另外一个chair 。 OK 那把它拿出来，你又想从 chain 里面获得什么啥也不要，就要你的一个 then 方法。


then 方法在哪？我们来看，这里看到这个吗？ then then 的意思，就是说当你前面的方法全部处理完了，那么在最后能不能给我一首歌的时间让我说几句话，你说的话就在这里面。咱先把你说的话给它注释掉，先闭嘴。这里看到一个 filter 吗？这里 filter 要把 exchange 塞进去。 OK 剩下的事你就不用管了，全部交给 gateway 来完成。


你这边只用注意的是，这个 then 方法当中，你想让这个接口在完成了所有处理以后，接下来给你的这一首歌的时间你怎么发挥好？我打算这样发挥，先把 mano 拿出来， mano 然后调用它的什么方法呢？ from runable 实际上它的底层就是使用了一个钩子来做回调的，大家感兴趣的可以点进去看一看。
这个代码它的异步流程写的还是不错的，毕竟在 Java 后台代码里用函数式编程包括回调也是一个现在比较流行的大趋势，大家我觉得还是有必要进去了解一下它是怎么来实现的。好，我们这里创建了 from runnable 以后，在这里面要实现这样一个东西。Ok.好在这里面我们就可以开始自己的表演了，怎么演这个 timer 复制一下。咱前面不是已经把 timer start 了吗？那么这里要把它 stop 一下什么意思呢？就是说你的计时任务到这里就停止了秒表按下计时停止。


你停止了以后我们很简单，只要把你打印出来就行了在上面加一个 sl four G 的组件，这里运用 log 打一个 info 级别的 log 然后使用调用 timer 的 pretty print 名字起得非常自信。 pretty print 也就是说他会打印一串非常漂亮的 logok 其实咱在 filter 里面还能做些其他的操作。我们可以对 exchange 做非常非常细致的自定义。比如说我这里可以举一个例子，讲一个附赠的小知识点，exchange里面你可以拿到它的所有的 attributesget attribute 拿到 attributes 以后，我们其实也可以修改它往里面添加新的 attribute 属性。比如说我这里这样好了，定义一个 attribute name 它叫 request time begin 计时开始，然后把当前的系统时间给它怎么样打印出来。 current time minutes many seconds OK 那咱这里就向你的 H bills 列表中添加了一个新的属性，这里还有很多种其他不同的用法，你这个 exchange 里面真包罗万象，什么东西都可以拿到，get request get response 甚至 session 都可以。 OK 那我们这里先不去管它了，咱的主体业务逻辑都已经定义好了。


接下来就要看如何把这个 time filter 放到我们已经配置好的路由规则里面。在这之前我们还要做一个这个操作，把它声明成一个 component 这样的话就能加载到 spring 的上下文当中了。那打开小桌板，先把 timer filter 这名字给它复制下来。我们走到定义路由规则的地方，也就是 gateway configuration 在这节当中，我跟大家展示如何在 Java 文件中指定一个自定义的 filter 配置文件中的配置方式，就让大家自己去摸索了。
好，咱在这里要把这个 time filter 先给它引入进来，把这个类 copy 一下，给它起名 time filterok 使用 out why 的形式。实际上咱注入他们 filter 到路由规则中不止这一个形式，有很多种，大家可以去自己的摸索一下，我这里使用的是最简单的一种方式。


接下来同学们目光聚焦在这里，我现在要给第一个路由规则添加一个 filter 怎么添加呢？它的位置肯定是当前的这个 filters 好我们这样一个点，同学们这里看到，当你想添加 filter 的时候，有很多的方法，从上到下依次为添加一个 filter 和添加一个 filter 并且指定它的 order 再往下是添加多个 filterok 那咱这里选择添加单个 filter 好了，直接把它的实现类海马 filter 指定进来，就这样结束了吗？没错，就是这么简单，下面咱就可以去测试一把了。

[image](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/d2462da5-1085-4cf3-97a0-874b6acbbcd0/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666XHXXSDH%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T225738Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIFoeitmcHHkRPy91y4VN29ZvCUrSnVCOVAt%2FKY79An1cAiAllc0G3qH%2FwzyExKc1k%2FYwJxNrpP2M6jA%2BoCr7vzXi1yqIBAjG%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMIWtq6uzYtCs5hqNJKtwDEsB%2FsD%2BciqM0%2B%2FxCjWhsWYT%2BOZTIJNjnDyo2uKlUrbIXIjIlsAyTfGwnR4rYQp%2BEWuBKsn2UlgZoSruc%2FLiTKJy%2FtsOlrM9fvyIvqxMA%2FSP8X%2B3NYPsKU5d%2FAG4NlliUtDRb6xCjLjVUcb5yjVB80gPseQcV22uQex0N7M5I8Eo%2BHQqaRzRHV%2BIDi1g97lstm7MeTYUmxas%2Fcje2FizATplroOx41TMpYgSA1PgiOyR1RpDR62f5piybcEECIQBhiBjNFCM%2BMdbtQwRLrxp3JDTDF8188X7D1CqZmP%2BTN4nLw4X4YsZ%2F45HbBJJUZspAhHLRxQROxheF8orLHYvsMTHy8cXuB8TEDfFS32Ai1eygfbIEV0Rt2E%2FF7poGbferyKOg%2FCV2pLx%2BttbkGK2YpXT8WDKxdDpF5IqiDrkRutRDScrRmlJo0DGoXPKX2Hx%2B8sAtH%2FPMl6kaEnsHNlgQ%2Bmaica1tCYwvfvr0ao%2BNstVcdbIIUUF1%2B12AdWRT2yXKGG87IG2NjI%2BlmkKQbW%2F%2F4U%2B2GIp4XIyBfzgme0pPSvDbXdYzzua7modyfTNOPulot1B45h6M6NhAxXLlfqGltvMkm%2FzKYdoQHEPIfLfUYDkX6GB16j4AssXueNUwn7r%2F0gY6pgGUGtfsnB0knPZIpZ%2F7ELezZwy2hIytG6JB8MvepxYjhJ5U5DaG1xpZwUUgs0F%2B2xbWp0Hc1ydaVDemuuNzSo1ydwohTWEg%2Fqp%2BAj9qKmzkYRuekKjDnKRzxsiPbk5zf%2FO%2BcB6USPMVMRO%2B3ldnDlq6x5NTB0rfoxBj9bP43ikuzkuOUh0JgotmTceQRjsO7h29kgg06tinQVGx1Hnp6XQ5BH2KAPJA&X-Amz-Signature=8461cbf551fc3279cf8d088cae07555c5c6b87c296d2ed24b94b7a788b982113&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

别说话，快上车，咱开启测试。第一个，把尤瑞卡 server 先给启动起来，紧接着他后面分 client 当仁不让继续启动。 OK 等这前面两个应用全部启动好了以后，咱们再来启动 gateway applicationok 启动好以后，我们只要去调用一把它的 service 就能看到在 log 中打印出了接口的执行时间。 OK 咱这里看到整个服务已经启动起来了，我们先把它的 log 给清空好转战 postman 那我们这里依然调用 gateway 的 say hi 方法，使用的是哪个路由看这个路径里面写的是 Java 所以它会匹配到咱在后台中。这里设置的第一个 root 路由节点，它的接收请求是接收以 Java 开头的路径。


OK 到普斯曼里，我们发起一次调用，走你回到 gateway 的 log 里面，大家看这一行往下。这一行就叫做 pretty log 是不是非常的美丽。我觉得这个计时器组件有点夸大宣传，实际上也没有那么美丽。这里可以看到它前面的 MS 是所占用的毫秒数，它花了多少毫秒？那么 task name 实际上就是你调用的接口路径这个百分百什么意思呢？那在这个整个环节中，它会记录你每一次开始停止所的时间，占整个链路的时间比例。

```java
2022-11-13 09:54:12.071  INFO 2264 --- [ctor-http-nio-7] com.imooc.springcloud.TimerFilter        : StopWatch '': running time (millis) = 9
-----------------------------------------
ms     %     Task name
-----------------------------------------
00009  100%  /sayHi
```


好，那到这里整个课程就完了吗？还没有，咱刚才看的是一个 filter 那么实际上 gateway 还有另外一种 filter 叫什么？ global filter 全局 filter 它怎么来配置？同学们这里跟我看一下，咱先把这个应用给关掉。对全局配置，我这里依然采用基于 Java 的配置方式，把基于配置文件的全局 filter 的方式，留给大家来摸索。咱这里先把这一行给注释掉，让它不生效。然后在哪里配置 global filter 非常简单，我们点进去刚才定义的这个 timer filter 看这里 timer filter 侍奉的两个主是谁 gateway filter 和 ordered 那如果你想让它成为一个 global filter 一个最简单的方式， gateway filter 换成什么？ global filter 好， global filter 同样的也是 spring former gateway 组件中的一部分。

```java
*/
@Slf4j
@Component
//public class TimerFilter implements GatewayFilter, Ordered {
public class TimerFilter implements GlobalFilter, Ordered {

    @Override
    public Mono<Void> filter(ServerWebExchange exchange, GatewayFilterChain chain) {
        StopWatch timer = new StopWatch();
        timer.start(exchange.getRequest().getURI().getRawPath());

//        exchange.getAttributes().put("requetsTimeBegin", System.currentTimeMillis());
        return chain.filter(exchange).then(
            Mono.fromRunnable(() -> {
                timer.stop();
                log.info(timer.prettyPrint());
            })

        );
    }

    @Override
    public int getOrder() {
        return 0;
    }
}
```


OK 那咱这里其他方法流程都不用变方法签名，包括已经实现的方法都原封不动的放在这里，只用改一个继承类就好了。那接下来我们再次尝试着启动一下方法，看看刚才配置的 global filter 会不会生效，理论上它会作用于所有全局的路由规则当中。 OK 我们这里已经启动好了，把 log 清空一下，然后同样的发送一个 say hi 的方法。 OK 那这里已经打印出了，返回结果，我们回到 log 中看一下。同学们这里看到结果也已经正确被打印出来了，说明刚才的全局变量也依然生效了。但是同学们有没有发现一点非常细微的小差别。细心的同学可能会注意到，我们在不改动任何代码的情况下，如果你是全局的 filter 那这个 task name 会带上 Java 然后一个斜杠 say hi 那如果你不是全局 filter 你是一个普通的 gateway filter 那么这种情况下你的 task name 就不在前面的 Java 了。为什么会有这种区别呢？同学们这就留给大家在代码里面寻找答案了。好在本章快要结束的时候，我在这个类方面再加上这么一行注释，给大家说明一下 global filter 全局过滤器。 

```java
2022-11-13 09:59:48.279  INFO 2307 --- [ctor-http-nio-7] com.imooc.springcloud.TimerFilter        : StopWatch '': running time (millis) = 147
-----------------------------------------
ms     %     Task name
-----------------------------------------
00147  100%  /java/sayHi  
```

OK 那把它从 global filter 再替换成 gateway filter 我们保持原来的 demo 代码不变。同样的，在 configuration 里面，把这一步注释掉的给它还原过来。这样同学们可以方便回顾一个普通的 filter 和一个全局的 filter 都是怎么来定义的。


OK 那到这里整篇课程就结束了，我来带大家稍微回顾一下。在这篇课程中，我们主要学习了如何自定义一个 filter 那么它的步骤非常简单，声明一个 filter 然后继承 gateway filter 或者是 global filter 这个接口就可以了。但是在方法实现当中，它采用的是一种回调函数，也就是利用 hook 钩子在代码执行前后，调用自己的业务逻辑，函数式编程和回调也是近些年来的发展方向了。


老师鼓励大家去阅读一下玛瑙的代码，深入了解一下在 Java 中如何实现这种异步回调的方式。 OK 那么本小节到这里就结束了，在下一小节当中，我会带大家研究一下给它位中 filter 它的底层机制。相信这次的源码阅读应该是整个 spring cloud 章节有史以来最简单的了。 OK 那同学，我们下一小节再见。




