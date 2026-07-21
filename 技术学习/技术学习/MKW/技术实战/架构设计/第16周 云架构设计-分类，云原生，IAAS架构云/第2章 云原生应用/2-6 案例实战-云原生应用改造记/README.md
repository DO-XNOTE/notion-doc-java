---
title: 2-6 案例实战-云原生应用改造记
---

# 2-6 案例实战-云原生应用改造记

[image](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/49e26c91-8303-447f-9de7-91fe192341ad/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46675HGFQWW%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T231059Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDd5HL1OcvgrhpSFOjkbkXDiiGZzDAUdrSXuLgw0i2GswIhALN5DT3lWeVrr8PZFB9QFqSBqEZVUUH0OM3ni4%2F02ZGvKogECMb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgwjVMCAyM4aDlyiDtkq3AMf7mkxnCMOEUQQ8g0kZfDZLE7D6ryQ0H%2F9vJfipSWgOagWHLfZ4i%2BLhzov2g7fqaN49fSudK18ABlrur5nBTGsyNxc5BzzzgP2SJaWMWuWmuU7PmSjBzFD1K7TQP97XSTChhObnFHiG0hgvHHRVe8uT3MFMy9J%2BReluoMc13zoqyEgNMXYuD2uXB%2Fe3eCzIGYtkZpK9uN9PlVtMtZLt%2BDdfmvm4YH7bpFXJihxeBeK3LP2y6hDy66HUsHV6hJqKfcffeI%2BLt%2BoQpmxv980LYlTDz3pGo9jfmaEy7iaI0BckjLx4qtv5%2BQIPIWYG979S9oEkMVBXFW%2BStcLMicuwAHdM0id4gKOXuzv7Si%2F3IGbbr%2F7QiRXQklPly9Ooi7%2BxwhKoEhLsk1NVPxFgQi7rPinT2Mv%2BA8xi%2FiQZ8bV70JRs7fdsGDF%2FcEIAo9c0e8riAXDk6dw6kBs%2F7Qo%2Fg%2FEdBo%2BmP66r8pv0jiVE%2BnMmL%2B3z5PS7bxj%2BtYjZ2BWcly8GqAkcMQeN5Snj6j3RnkQAfpFNuCky70rtmhaIyt0LK8LuUfbXiitRQHm2RPfdRKByR%2BCMolPVDZDAjXE0w%2FOQbwC6SuiDKHXo%2FHNS%2BrgdLt32p92EuSrtgsjGIJH6DC0uP%2FSBjqkAeLS2jNoAmVm2%2FAk1Il1B879pWttmXpMkoKl7OQ1a%2BBsdkTbKlXan69bSltaaz4fMNUy%2FyVp8caFFgtPIYHeFl%2ByvwxJTZtUWHR0HHfPrwwVK7x%2FF1f8lfgA8UsuGqaLlPpzE7cIDTUf7fT8%2FTHe9lkRuViv9D0VKHrYn0uAgAH7jngraJYF7IMeDmfKEnjW%2FDo%2FdNQcjZfz5QZJ%2B0hYA0Qmv06d&X-Amz-Signature=820a7454af3e2ca429d07f14e6bd26048d21f20d4d6278cf539c761e73632f71&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

[image](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/7d7bb8bf-ad49-4141-9730-2a353ce3b3ec/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46675HGFQWW%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T231059Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDd5HL1OcvgrhpSFOjkbkXDiiGZzDAUdrSXuLgw0i2GswIhALN5DT3lWeVrr8PZFB9QFqSBqEZVUUH0OM3ni4%2F02ZGvKogECMb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgwjVMCAyM4aDlyiDtkq3AMf7mkxnCMOEUQQ8g0kZfDZLE7D6ryQ0H%2F9vJfipSWgOagWHLfZ4i%2BLhzov2g7fqaN49fSudK18ABlrur5nBTGsyNxc5BzzzgP2SJaWMWuWmuU7PmSjBzFD1K7TQP97XSTChhObnFHiG0hgvHHRVe8uT3MFMy9J%2BReluoMc13zoqyEgNMXYuD2uXB%2Fe3eCzIGYtkZpK9uN9PlVtMtZLt%2BDdfmvm4YH7bpFXJihxeBeK3LP2y6hDy66HUsHV6hJqKfcffeI%2BLt%2BoQpmxv980LYlTDz3pGo9jfmaEy7iaI0BckjLx4qtv5%2BQIPIWYG979S9oEkMVBXFW%2BStcLMicuwAHdM0id4gKOXuzv7Si%2F3IGbbr%2F7QiRXQklPly9Ooi7%2BxwhKoEhLsk1NVPxFgQi7rPinT2Mv%2BA8xi%2FiQZ8bV70JRs7fdsGDF%2FcEIAo9c0e8riAXDk6dw6kBs%2F7Qo%2Fg%2FEdBo%2BmP66r8pv0jiVE%2BnMmL%2B3z5PS7bxj%2BtYjZ2BWcly8GqAkcMQeN5Snj6j3RnkQAfpFNuCky70rtmhaIyt0LK8LuUfbXiitRQHm2RPfdRKByR%2BCMolPVDZDAjXE0w%2FOQbwC6SuiDKHXo%2FHNS%2BrgdLt32p92EuSrtgsjGIJH6DC0uP%2FSBjqkAeLS2jNoAmVm2%2FAk1Il1B879pWttmXpMkoKl7OQ1a%2BBsdkTbKlXan69bSltaaz4fMNUy%2FyVp8caFFgtPIYHeFl%2ByvwxJTZtUWHR0HHfPrwwVK7x%2FF1f8lfgA8UsuGqaLlPpzE7cIDTUf7fT8%2FTHe9lkRuViv9D0VKHrYn0uAgAH7jngraJYF7IMeDmfKEnjW%2FDo%2FdNQcjZfz5QZJ%2B0hYA0Qmv06d&X-Amz-Signature=a97c1fca2d12e3b9a557504ee659ca8b13f92dea01073ab49c56db8a16f3df1c&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

架起需求到落地的桥梁，构建 it 新蓝图。我是张飞扬，上一个章节我们聊了聊 15 个原则。哇，好多啊，好难记啊，那我们这里尝试拿一个非常简单的小应用改造的例子来跟大家分享一下这些原则该如何实战的。好，废话不多说，我们就拿实际案例开始，首先找了一个叫预定小程序，



或者叫预定小应用。什么是预定呢？可以是预定一个酒店的房间，可以是预定一杯咖啡，预定一个快餐、预定一个冰激凌都可以，就是一个很通用的预定小程序，那它重点是要保持什么？一份代码原则，我这一个应用就干一件事情，所以我就是一份代码，我在 Git Hub 上是占独立的一个repo，那同时我的应用写得非常小巧，可以快速启动，秒即关闭，我们看一下如何来完成这样一个应用，那这里在慕课的 Git Hub 上，

[image](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/aefc6cf0-28a2-4362-b4e5-e4be1e377eb9/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46675HGFQWW%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T231059Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDd5HL1OcvgrhpSFOjkbkXDiiGZzDAUdrSXuLgw0i2GswIhALN5DT3lWeVrr8PZFB9QFqSBqEZVUUH0OM3ni4%2F02ZGvKogECMb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgwjVMCAyM4aDlyiDtkq3AMf7mkxnCMOEUQQ8g0kZfDZLE7D6ryQ0H%2F9vJfipSWgOagWHLfZ4i%2BLhzov2g7fqaN49fSudK18ABlrur5nBTGsyNxc5BzzzgP2SJaWMWuWmuU7PmSjBzFD1K7TQP97XSTChhObnFHiG0hgvHHRVe8uT3MFMy9J%2BReluoMc13zoqyEgNMXYuD2uXB%2Fe3eCzIGYtkZpK9uN9PlVtMtZLt%2BDdfmvm4YH7bpFXJihxeBeK3LP2y6hDy66HUsHV6hJqKfcffeI%2BLt%2BoQpmxv980LYlTDz3pGo9jfmaEy7iaI0BckjLx4qtv5%2BQIPIWYG979S9oEkMVBXFW%2BStcLMicuwAHdM0id4gKOXuzv7Si%2F3IGbbr%2F7QiRXQklPly9Ooi7%2BxwhKoEhLsk1NVPxFgQi7rPinT2Mv%2BA8xi%2FiQZ8bV70JRs7fdsGDF%2FcEIAo9c0e8riAXDk6dw6kBs%2F7Qo%2Fg%2FEdBo%2BmP66r8pv0jiVE%2BnMmL%2B3z5PS7bxj%2BtYjZ2BWcly8GqAkcMQeN5Snj6j3RnkQAfpFNuCky70rtmhaIyt0LK8LuUfbXiitRQHm2RPfdRKByR%2BCMolPVDZDAjXE0w%2FOQbwC6SuiDKHXo%2FHNS%2BrgdLt32p92EuSrtgsjGIJH6DC0uP%2FSBjqkAeLS2jNoAmVm2%2FAk1Il1B879pWttmXpMkoKl7OQ1a%2BBsdkTbKlXan69bSltaaz4fMNUy%2FyVp8caFFgtPIYHeFl%2ByvwxJTZtUWHR0HHfPrwwVK7x%2FF1f8lfgA8UsuGqaLlPpzE7cIDTUf7fT8%2FTHe9lkRuViv9D0VKHrYn0uAgAH7jngraJYF7IMeDmfKEnjW%2FDo%2FdNQcjZfz5QZJ%2B0hYA0Qmv06d&X-Amz-Signature=cdaaadf543e02b45fafefe8149f317cc41020a00d9bd692069d8d7e1e15e6df7&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

福元老师上传了一套代码，你打开代码里面有什么？有最终版的代码， Kotlin 版、 Java 版，以及中间的 9 个过程，我们分别从 9 个过程一一来跟大家讲解啊。

[image](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/607fdcd2-44c6-4e4d-93a9-e05d3a38de2b/Google_Chrome_2025-05-14_16.51.20.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46675HGFQWW%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T231059Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDd5HL1OcvgrhpSFOjkbkXDiiGZzDAUdrSXuLgw0i2GswIhALN5DT3lWeVrr8PZFB9QFqSBqEZVUUH0OM3ni4%2F02ZGvKogECMb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgwjVMCAyM4aDlyiDtkq3AMf7mkxnCMOEUQQ8g0kZfDZLE7D6ryQ0H%2F9vJfipSWgOagWHLfZ4i%2BLhzov2g7fqaN49fSudK18ABlrur5nBTGsyNxc5BzzzgP2SJaWMWuWmuU7PmSjBzFD1K7TQP97XSTChhObnFHiG0hgvHHRVe8uT3MFMy9J%2BReluoMc13zoqyEgNMXYuD2uXB%2Fe3eCzIGYtkZpK9uN9PlVtMtZLt%2BDdfmvm4YH7bpFXJihxeBeK3LP2y6hDy66HUsHV6hJqKfcffeI%2BLt%2BoQpmxv980LYlTDz3pGo9jfmaEy7iaI0BckjLx4qtv5%2BQIPIWYG979S9oEkMVBXFW%2BStcLMicuwAHdM0id4gKOXuzv7Si%2F3IGbbr%2F7QiRXQklPly9Ooi7%2BxwhKoEhLsk1NVPxFgQi7rPinT2Mv%2BA8xi%2FiQZ8bV70JRs7fdsGDF%2FcEIAo9c0e8riAXDk6dw6kBs%2F7Qo%2Fg%2FEdBo%2BmP66r8pv0jiVE%2BnMmL%2B3z5PS7bxj%2BtYjZ2BWcly8GqAkcMQeN5Snj6j3RnkQAfpFNuCky70rtmhaIyt0LK8LuUfbXiitRQHm2RPfdRKByR%2BCMolPVDZDAjXE0w%2FOQbwC6SuiDKHXo%2FHNS%2BrgdLt32p92EuSrtgsjGIJH6DC0uP%2FSBjqkAeLS2jNoAmVm2%2FAk1Il1B879pWttmXpMkoKl7OQ1a%2BBsdkTbKlXan69bSltaaz4fMNUy%2FyVp8caFFgtPIYHeFl%2ByvwxJTZtUWHR0HHfPrwwVK7x%2FF1f8lfgA8UsuGqaLlPpzE7cIDTUf7fT8%2FTHe9lkRuViv9D0VKHrYn0uAgAH7jngraJYF7IMeDmfKEnjW%2FDo%2FdNQcjZfz5QZJ%2B0hYA0Qmv06d&X-Amz-Signature=14f3ef3de0d477585af3ef7cd5c2dbf790e3b03cdeb6b316c9c66ce7247f639e&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)


第一过程就是刚刚说的一个小程序，我们看一下这个小程序代码非常非常简单，一个标准的 spring boot application，然后它重点就是什么？去管理reservation，那这个 reservation 在 reservation 类里面定义好了，它其实就是有一个 reservation 相关的名称以及一个ID，也没什么具体内容。你可以是预定一个酒店，预定一个冰激凌，预定一个什么火锅什么大餐都可以。


好，就是这样一个很通用的小预定，然后它的芽帽文件或者 property 文件为空。也就是说什么没有任何的配置，非常干净，然后 palm 里面应该有标准的，比如说 spring boot 的starter，什么 starter Web 这样一些工件的依赖要写清楚就好了。


[image](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/0317c069-d062-4c0b-a672-3301f2731acb/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46675HGFQWW%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T231059Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDd5HL1OcvgrhpSFOjkbkXDiiGZzDAUdrSXuLgw0i2GswIhALN5DT3lWeVrr8PZFB9QFqSBqEZVUUH0OM3ni4%2F02ZGvKogECMb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgwjVMCAyM4aDlyiDtkq3AMf7mkxnCMOEUQQ8g0kZfDZLE7D6ryQ0H%2F9vJfipSWgOagWHLfZ4i%2BLhzov2g7fqaN49fSudK18ABlrur5nBTGsyNxc5BzzzgP2SJaWMWuWmuU7PmSjBzFD1K7TQP97XSTChhObnFHiG0hgvHHRVe8uT3MFMy9J%2BReluoMc13zoqyEgNMXYuD2uXB%2Fe3eCzIGYtkZpK9uN9PlVtMtZLt%2BDdfmvm4YH7bpFXJihxeBeK3LP2y6hDy66HUsHV6hJqKfcffeI%2BLt%2BoQpmxv980LYlTDz3pGo9jfmaEy7iaI0BckjLx4qtv5%2BQIPIWYG979S9oEkMVBXFW%2BStcLMicuwAHdM0id4gKOXuzv7Si%2F3IGbbr%2F7QiRXQklPly9Ooi7%2BxwhKoEhLsk1NVPxFgQi7rPinT2Mv%2BA8xi%2FiQZ8bV70JRs7fdsGDF%2FcEIAo9c0e8riAXDk6dw6kBs%2F7Qo%2Fg%2FEdBo%2BmP66r8pv0jiVE%2BnMmL%2B3z5PS7bxj%2BtYjZ2BWcly8GqAkcMQeN5Snj6j3RnkQAfpFNuCky70rtmhaIyt0LK8LuUfbXiitRQHm2RPfdRKByR%2BCMolPVDZDAjXE0w%2FOQbwC6SuiDKHXo%2FHNS%2BrgdLt32p92EuSrtgsjGIJH6DC0uP%2FSBjqkAeLS2jNoAmVm2%2FAk1Il1B879pWttmXpMkoKl7OQ1a%2BBsdkTbKlXan69bSltaaz4fMNUy%2FyVp8caFFgtPIYHeFl%2ByvwxJTZtUWHR0HHfPrwwVK7x%2FF1f8lfgA8UsuGqaLlPpzE7cIDTUf7fT8%2FTHe9lkRuViv9D0VKHrYn0uAgAH7jngraJYF7IMeDmfKEnjW%2FDo%2FdNQcjZfz5QZJ%2B0hYA0Qmv06d&X-Amz-Signature=885dfb2c013f26b21f03fb87badd3f7a63327f1815c502bd3a3c0c5c9848321a&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)


好，这就是非常简单快捷的秒级启动，秒级关闭的一个小程序就准备好了，这就是第一步，我们回过去 PPT 看。第一步完成以后我们就进入第二步，就是我刚刚这个应用其实只能在什么我的 IDE 环境能进行开发测试，但没法发布到生产环境。我需要把这个应用代码准备的能够发布到生产，同时整个代码的这个打包构建的过程要完全一致，不管你是在我的浏览器的这个本地访问，还是我采用一些基本的功能部署到 QA 环境，甚至又把它放到生产环境，都要能够正常地、一致性地进行访问，感觉上环境是几乎是一致的。那怎么样做到有几个关键的点，我来跟大家分享一下。


首先我刚刚这段代码有个大问题，它连基本的一些这种健康检查的功能都没有，那这没法发布到应用的，对不对？这个应用发布到生产是没法进行健康检查，而生产系统通常物理机或者虚拟机普通的开发人员没法登录访问。那这个时候我们应该怎么样？我们应该尝试在我们的 palm 里面，对吧？这就是阶段。


2 PALM 里面的尝试是追加一些基本功能，比如说这个 activator 的健康检查和一些简单的操作，虽然你不能通过 R2 端口去 SSH 物理机或者虚拟机，但是你可以通过什么服务的 activator 这样的什么 URL 去什么访问它的一些基本的健康检查、配置管理等等。


那除此以外我们应该什么？我们应该支持这个安装包是可以打包成一个架的，包可以变成一个可执行的，那这个时候我们应该什么在这里，对吧？在 plugin 里面，是吧？使用 springboot Maven 的 plugin 或者种种plugin，最后把它变成一个可执行的架包，那这样的情况下我就可以发布到生产了，而我希望我的整个发布环境可以看到这个 property 这里要保持一致，不管你是 DEV staging production，我总体来看就是基本上我的整个软件包的部署过程和源代码是完全一致的，在每个环境都互通。


好，那聊完了，步骤 2 我们回过去看步骤 3 进一步了，怎么进一步呢？我其实是每个环境当然会有一些不同的地方，对吧？我没法在我的这个 properly 文件或者是自身的这个配置文件这里把这个描述清楚，那我可以把这些不同的内容环境变量的内容抽取出来，抽到什么地方呢？这里采用 spring cloud config 做配置的统一管理。那这个时候你的整个编译发布和运行时，环境就分离了，所有跟环境相关的内容放在了 git up 上，通过 spring cloud config 来跟什么应用进行对接，实时的进行配置的刷新。


那另外因为用到了 spring cloud config 这样的服务，所以你的源代码必须要依赖明示明确写清楚我用到了这个服务，那这样的这个配置管理的方式，其实我们在后面，什么我们半仙老师的服务治理里。会详细来聊怎么样用它，我这里跟大家过一下，给大家感受一下在云原生改造过程当中大概是什么样一个过程。


好，我们看到这个步骤 3 这里就可以看到什么，我们有两个 Repo 了。第一个 Repo 是我们刚刚创建的叫 Reservation service 的什么？ Git Hub Repo，对吧？做什么应用代码？另外我们要建一个独立的repo，发布一套独立的代码或者独立的软件，做 spring cloud config 的部署。那这个部署其实非常简单，它的源代码几乎就几行字，哪几行字啊？一个普通的 spring boot 应用，然后加个 annotation enable config server 好就可以了，这就是 spring cloud config 了。然后 property 里面重点是什么？要写清楚两个内容，一个是我自己的服务启动在哪一个端口8888。还有一个是我是无状态的，所以我的所有配置信息都是从什么 git Hub 上拉取的，我具体访问的 git Hub 的 repo 在哪里，讲清楚就可以了。


当这些内容讲清楚以后，其实什么这个 config service 就作为一个独立的服务启动了，然后我的 reservation service 会用到它，所以我在 palm 里面会说我什么我要用到这个 config service，然后用它来进行什么配置的管理。另外我在我的主程序的 resource 里面也会说什么我用到了这个 service 在哪里啊？在同一台物理机的什么 8888 端口诶？是不是就找到了 config service 了？好，到了步骤 3 呢。其实我们已经实现了什么？一个应用变成两个应用，然后一个 repo 变成两个repo，把配置信息给剥离出去了，我们再继续看下一步。


到了第四步我们怎么改造，我们尝试把整个业务进行前后端分离，不同的功能放在不同的服务里面，这样服务之间需要有一个服务注册和发现的过程。我们这里用的是什么？是 spring cloud 的 Eureka 来进行服务的注册和发现一样的，在后面的服务治理章节会详细来聊怎么搭建，怎么使用Eureka。


这里只是提一下怎么样一个感觉，当你在改造的时候是什么样的一个感觉的？第四步，我们会创建一个 Uraka 的服务，那依然是非常简单，整个 Uraka 服务这个代码只有几行字？哪几行字啊？一个普通的 springboot 的 application 加个 annotation enable Uraka Server 就可以了，它就起来了，然后在它的这个 property 文件里面指定一下我这个服务自己有一个名称的，叫什么叫 Uraka service，而我这个服务需要拿的配置文件也是从什么 spring cloud config 来获取好了，如此简单，那应用如何要访问它呢？我们可以看一下当前我们把应用进行了前后拆分成两个应用，一个是对用户端访问叫client，还一个是后台做什么 domain Logic 领域逻辑的，我们领域逻辑这里面源代码你可以看到不变，全是之前的基本代码，那唯一区别是在这里加了个annotation，叫 enable discovery client。也就是说我要把我的这个服务注册在 Eureka 上，我只要加一个 annotation 就可以了。


那加完以后它就什么能够成功地注册到这个 Eureka 服务了？但它以什么样的名称来注册呢？在什么？在 property 文件里面进行指定，我们打开看一下它叫什么名称啊？它的名称叫 reservation service，好，这个应用叫这个名称。那它的前端应用大家猜一猜叫什么名称？是不是所见即所得？就叫做 reservation client？它们都注册在同一个 Uraka 上， Uraka 的服务可以当成一个我们的钥匙环，钥匙环上可以插很多把钥匙，每把钥匙之间都可以互通，对吧？可以互相接触，这就是插两把钥匙，一把叫 reservation client，一把叫 reservation service。


那 client 其实当前源代码几乎是空的，可以看一下，几乎是空的，其说白了就是它只是一个子程序，然后它去调用后台的什么 reservation service，好，到这第四步完成，我们其实已经完成了很多工作了，我们把服务前后分离了，我们把配置拉出去了，我们把整个开发、测试、生产的发布统一化了，同时我们把一个应用代码变成 4 个，对吧？既有注册服务，也有配置管理，还有什么前端和后端？好，到了第五步我们进一步进行什么云原生的改造？我们要加一个 API 网关，同时在网关上实现熔断，那这里用的是最老的这个 API 网关Zuul，以及用的是什么？是 histories 这样一个熔断机制。我们来看一看这两个功能配合起来如何来实现我们的 API 经济的原则，以及如何来实现监控和遥测的。


好，切回去我们看第五步里面，既然我们说到什么，我们有一个 API 网关必然是有所体现，在哪里体现？就在 reservation client 这里。好，我们首先看看它的palm，这里我们可以往下看，看到没有？他用了个叫Zoo， Zoo 就是一个什么比较传统的。一篇网关稍微老式一点了，我们在新的 spring cloud 里面叫 spring cloud Gateway。没有关系，那这是至少，反正它能实现一些基本的这个网关处理，包括认证，包括分流，包括一些这个跟什么 histories 配合起来实现一些熔断等等功能。


好，有网关，有 histories 熔断，那它怎么样真正去跟什么 reservation client 进行代码级的配合呢？我们打开它的源代码，我们看一下，诶，是不是有令大家非常熟悉的什么 Controller 了？ rest Controller，然后 rest Mapping，好，通过这样一个路径 reservations 就能够什么打到网关上，然后通过网关就能够发送到我们的应用的这个服务上。


而这个服务假设我们以这个 get reservation name 为例，它对外提供的什么子路径就是names，如果这个服务出错，怎么样呢？我们在 history command 里面可以设一个叫什么叫做 fall back 的方法，也就是熔断方法，或者叫什么或者叫回退的方法。那这个方法就会调用另外一个功能，那个功能相对来说更稳定，但是返回值更简单。


好，这就是一个基本的网关的套路，同时我们要声明一下，我们会使用网关，对，在这里加一个叫 enable Zoo proxy 就可以了，有了网关有了什么 rest API 对外的提供的服务，以及有了熔断，基本上这套服务就很完美了。也就是应用先打到网关，再打到什么 client 服务，如果认为OK，再打到后台什么真正执行逻辑的 reservation service 服务，那在整个过程当中你大家想一想，有这么多的调用链，是不是可能存在一些问题啊？我们要实现遥测，要监控怎么办呢？我们可以利用 histories 的本质监控功能。它会什么把所有我们加了 histories command 的这些API，在实际的这个 API 请求会记录下来，保存在本地。


如果你能起一个叫 histories dashboard 这样一个远端监控的仪表盘，它就会把这部分什么 API 的这个记录结果发给仪表盘，在仪表盘上进行图形化的展示。仪表盘其实代码也非常简单，几行代码，重点就是这里 enable Histrix dashboard，这样就跑起来了，轻轻松松地跑起来了，同时它也需要注册在 Eureka 上，作为一个服务，它的服务名也叫 Histrix dashboard。


好，大家回顾一下，我们现在有了Gateway，有了前端后端应用，对吧？有了 config service，有了 Uraka service，还多了一个外面遥测的监控service。是不是总共有了这样六个不同的服务，这些五个不同的服务，这些服务配合起来总体来看就基本上实现了一套完整的什么 cloud native application 好，到底完整不完整呢？我们看一看，其实还是可以有一些进一步的增强。比如说我们当前是不是所有的服务都跑在 local host 上？也就是什么我的生产节点只能是一台或者是有限台？如果我希望是 100 台、 1, 000 台、1万台，嗯，这样的机制可能不一定适合，因为什么每一个服务都要占一台物理机或者虚拟机，太浪费空间，太浪费资源了？那我们可以采用容器云。


说到容器云，大家又冒出了两个单词， doc Kubernetes。福燕老师要强调一遍，容器云不要只看 doc Kubernetes，容器云是一个泛泛的概念。我这里就跟大家举一个另外的例子，通过 runc 的 container 来代替Docker，通过 Calico Fundy 来代替Kubernetes。给大家感受一下其他的容器平台也能实现云原生。


在实现过程当中要实现三个关键点，这就是三大原则，端口绑定原则，所有的容器映射到物理机的端口都是不一样的，但是这些端口不需要人为记忆，完全什么有云平台、容器平台来帮大家搞定。另外更多的环境变量可以在容器云里面进行环境变量的注入和分离，使得每一个环境本身互通有无，但是不影响其他环境的发布，也就是我一套代码发布在 staging 环境和发布在生产环境完全一致，所有变量在发布过程当中由什么？由系统本身进行注入？好，最后一点就是要利用容器云的强大功能了。当你 5 个实例能运行的时候， 5, 000 个实例也能够在容器云上轻松运行。通常是一条命令就可以把 5 个实例或者说 5 个容器变成 5, 000 个，5万个，看一看如何来跑容器云吧。


我们把第五步数错，我们来看看第六步，第六步的关键就是这条命令，这是一个脚本，这个脚本里面其实已经表含了，我们到底怎么样去起这套容器技术呢？先起什么？先到 config service 里面来一个 CF push 一条命令实现了类似于 Docker 的 build 以及 Kubernetes 的 apply Kubectl apply 的命令把一个应用包架包变成一个什么 droplet 容器镜像，这个容器镜像不是 doc image，是另外一种叫 droplet 容器镜像，发布到 cloudfoundry 里面，然后弹性地伸缩到足够多的节点上。就是这样一步就。能把整个 spring cloud config 发布出去了，当发布出去完了以后，我们可以在命令行的回写里看到它告诉你，诶，我这个容器发布完了以后，所有的容器后台总共汇聚成这样一个URL。


当你访问这个 URI 的时候，它就会访问几十个不同物理节点的不同的端口，最终访问到什么 spring cloud config 那个小容器的指定容器内的端口上。整个过程当中你不用记物理节点在哪里，也不用记物理端口在哪里，只要访问这个 URL 就可以轻轻松松访问 spring cloud service。那怎么把这个 URL 记住呢？也很简单，在 mkcfunc 这里只有一条命令叫cups，创建一个用户定制化的服务，这个服务把后面一串很长的 URL 变成一个短名，叫做 config service。如法炮制，我们可以把 Uraka service 也建出来。怎么样进到 Uraka service 的这个目录里面跑一条 CF push，把整个架包发布到的 cloud function 上，然后把这个 Uraka service 的命名给建出来，建完以后我们看一个很轻松的例子，还是 reservation service，它要去绑定 Euraka service，它要去绑定 spring cloud config，只需要写一个压包文件，这个里面说什么？我需要绑定两个 service 的名称就好了，然后指定我的价包在哪里，然后也指定我的内存和CPU，默认内存就是一核， CPU 就是这里指定的 512 兆，通过这样一个羊毛文件，就把前面步骤 5 里面准备好了架包轻松地发布到云平台。


当然启动的时候是单实例，很小的CPU，很小的内存以及绑定好的服务，如果你要多实例怎么办？非常简单，在这里我再打个命令， CF scale，然后把这个服务名称，比如说这个，我希望后台的 service 不是一个，我希望是1万个，一条命令结束了，1万个容器就出来了，当发现这个资源消耗太多的时候，我甚至可以做一些什么 automation 的配置，比如在这里，杨茂这里我可以写一些这个最小一利用率多少，最大利用率多少，然后让它自动伸缩，它就会自动在一个和1万个之间进行伸缩，诶？是不是很酷炫啊？容器平台就是要实现这样的一些功能，这些功能能够并发，能够实现端口绑定的全自动化，以及能够实现环境变量和什么应用本身的隔离，好完成第六步。


其实是什么？一套很完整的平台化套路已经阐释出来，那我们下一步优化一下，中间是不是 client 端和 Server 端是用同步的 API 方式啊？那这个时候也许所有的方法都同步，可能有点浪费。比如说我们每一个小时要跑一个调度作业，创建一些 VIP 的用户，给这个 VIP 的用户定一个什么总统套房，每小时给他去定一个，但这个定的过程当中不需要怎么一定就要成功，我可以把这个定套房的命令发出去以后，等个两三分钟再成功也没有关系。因为什么 VIP 不是每时每刻都来？我们只要每时每刻帮他检查一下，确认一下他的套房保持在那里就可以了。


这个管理作业可以通过什么？可以通过外部的 API 经济来实现一个外部的定时器，比如云平台的定时器、百度云定时器、阿里云定时器，然后调用什么？调用前面的 reservation client 的API。这个 API 不用去，直接去调后台 service 的API，它完全可以发一条消息说我希望给某一个 VIP 用户订一个总统套房，之后等后台的 service 有时间了来处理这个消息就可以了。


来，我们来看一看如何用代码来实现这一套功能。好，我们回过去看到第七步里面，既然我们刚刚说有消息队列，所以我们在前端和后端在这 palm 里面要把消息队列选择好。这里选择什么是rabbitmq，加上了一个叫 stream rabbit 这样一个工具。好，那同样道理，这是前端代码，后端代码也作，为什么？作为这个消息队列的什么 consumer 消费者也要加上这一段叫。
Spring Cloud starter stream.


Rabbit，然后在源代码这里，我们的 Java 的这个代码这里也需要指定好我是什么，我是绑定在某一个消息队列上，那这是服务端，也就是我们的consumer。好，那我们看看 producer 生产者一样的道理，生产者拉到顶上是不是也要绑定同一个队列啊？这样我的这个 client 收到一个API，我就可以什么发出一个消息给后端的 Server 说，我要希望给这个 VIP 定一个特殊的总统套房，那这个 API 它本身它也又被一个什么一个定时器所调度，那这个定时器会调用一个API，这个 API 在哪里呢？我们可以看看啊。


好，找到了，在这里刚刚眼神不好， request mapping 底下选的是 post 方法，这个 API 就是专门给 VIP 来创建 reservation 的。好，有了这样的 API 以后，外部的定时器就会去定时 call 它会什么？创建一个 message 的这个什么一个消息，然后这个消息会发送到指定的队列。这就完成了 reservation client 被动什么作业调度，然后主动的发起一个消息，最后 reservation service 消费这个消息，完成指定任务。


好，回过头去看，已经做到这样是不是很完美了？既能够并发处理容器化的套路，同时还在我们同步的世界里面增加了消息队列，其实还有很多改进空间哦。我们来看一个改进空间，就是我们有了并发的处理，所以有很多的服务在那里面跑，那我们能不能在每一个服务里面把整个链路追踪清楚呢？不管你是从这个容器到那个容器，还是从这个服务到那个服务，不管你是经历的是 API 还是消息队列，有没有可能把 trace ID、 span ID 都记录下来，我们采用什么 zipkin 做链路追踪，那 zipkin 的激活也非常简单。


好，我们看到这个第八步里面起一个 zipkin 的服务就可以了，那这个服务也基本上是一行代码，重点加一个annotation，什么 enable zipkin Server。好，就把 zipkin Server 给起来了。那起来完了以后，同样道理，我把 zipkin Server 也注册在 Uraka 上，起一个名称。那注册完了以后，其他所有的服务要用到它怎么样？我只需要在这个服务里面，比如说我在 client 里面， palm 里面写一写，我要采用，或者说我要依赖于这样一个 zipkin 的这个构建包，诶，就好了。这样的套路非常轻松地就把 zipping 给集成进去。


好，有了这个 zipping 的集成，我们其实就已经实现了什么监控和遥测，对吧？我们不仅有了日志的收集能力，还有了很强的链路追踪能力，以及前面什么，前面的这个 histories 的这种出错熔断的追踪非常酷炫，还有什么可以增强安全性？是不是可以再加固一下？我们在整个环境当中，尤其是在什么 API 网关层，居然没有用到认证和授权，诶？这不应该，那我们呢？在最后一步我们可以尝试什么？在其中增加一个叫 authorization service，它具体实现什么样的功能呢？我们打开看一下，大家应该非常非常熟悉的功能了，然后顶上，诶 enable resource Server，这不是什么 spring cloud security oauth 的套路吗？就是这个套路，你看到什么令大家很熟悉的什么 authorization Server， configuration Adapter 这样一个接口，然后里面我们要什么，我们要重写它的 config 这样一个方法，以及非常经典的什么 user detail， service 这样的接口，要重写它什么load， user by name 方法好。


Cabinet must bring cloud security.
a 的 Oauth 里面其实讲到过类似功能，大家可以尝试回顾之前的功能，或者根据之前大家自己的 spring security 的经验，很方便搭建好一套 Oauth 的Server。有了 Oauth Server 以后，我们代码本身是不是也要激活这套oauth？我们可以在代码里面轻轻松松地来激活，比如说也 enable resource Server 等等等等。通过一些这个 palm 的加载，通过一些代码的改动，把什么，把刚刚用到的或搭建好的这个 Auth Server 给激活了，这样我们可以看到一个应用系统现在变成了好多个服务哦。

[image](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/506294a7-f227-462b-9c4b-0ab846d2360a/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46675HGFQWW%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T231100Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDd5HL1OcvgrhpSFOjkbkXDiiGZzDAUdrSXuLgw0i2GswIhALN5DT3lWeVrr8PZFB9QFqSBqEZVUUH0OM3ni4%2F02ZGvKogECMb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgwjVMCAyM4aDlyiDtkq3AMf7mkxnCMOEUQQ8g0kZfDZLE7D6ryQ0H%2F9vJfipSWgOagWHLfZ4i%2BLhzov2g7fqaN49fSudK18ABlrur5nBTGsyNxc5BzzzgP2SJaWMWuWmuU7PmSjBzFD1K7TQP97XSTChhObnFHiG0hgvHHRVe8uT3MFMy9J%2BReluoMc13zoqyEgNMXYuD2uXB%2Fe3eCzIGYtkZpK9uN9PlVtMtZLt%2BDdfmvm4YH7bpFXJihxeBeK3LP2y6hDy66HUsHV6hJqKfcffeI%2BLt%2BoQpmxv980LYlTDz3pGo9jfmaEy7iaI0BckjLx4qtv5%2BQIPIWYG979S9oEkMVBXFW%2BStcLMicuwAHdM0id4gKOXuzv7Si%2F3IGbbr%2F7QiRXQklPly9Ooi7%2BxwhKoEhLsk1NVPxFgQi7rPinT2Mv%2BA8xi%2FiQZ8bV70JRs7fdsGDF%2FcEIAo9c0e8riAXDk6dw6kBs%2F7Qo%2Fg%2FEdBo%2BmP66r8pv0jiVE%2BnMmL%2B3z5PS7bxj%2BtYjZ2BWcly8GqAkcMQeN5Snj6j3RnkQAfpFNuCky70rtmhaIyt0LK8LuUfbXiitRQHm2RPfdRKByR%2BCMolPVDZDAjXE0w%2FOQbwC6SuiDKHXo%2FHNS%2BrgdLt32p92EuSrtgsjGIJH6DC0uP%2FSBjqkAeLS2jNoAmVm2%2FAk1Il1B879pWttmXpMkoKl7OQ1a%2BBsdkTbKlXan69bSltaaz4fMNUy%2FyVp8caFFgtPIYHeFl%2ByvwxJTZtUWHR0HHfPrwwVK7x%2FF1f8lfgA8UsuGqaLlPpzE7cIDTUf7fT8%2FTHe9lkRuViv9D0VKHrYn0uAgAH7jngraJYF7IMeDmfKEnjW%2FDo%2FdNQcjZfz5QZJ%2B0hYA0Qmv06d&X-Amz-Signature=a3a54c132a43e14d050301a061a0bf89320e80e65465818d5d8e7d585a83dae9&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)


每个服务都有自己独立的repo，比如说这里安全配置、服务发现遥测、这里的前端后端，这里的链路追踪等等等等，以及通过 cloudfoundry 什么强大的容器化伸缩能力实现一个完整的平台。我们回过头去看一下，这里面用到了哪些技术啊？付阳老师之前已经数过了，已经用到了 12 个原则，还有 3 个原则这里没有用到，而那 3 个原则恰恰是最简单的原则。好，留一个 QQ 讨论题，另外 3 个原则大家能找出来吗？然后在什么样的情况下来改造它？应该如何对刚刚说的这个 reservation 小应用来进行另外 3 个原则的改造呢？好后面的面试环节和 QQ 讨论题就是下节的主体内容，大家敬请期待。

