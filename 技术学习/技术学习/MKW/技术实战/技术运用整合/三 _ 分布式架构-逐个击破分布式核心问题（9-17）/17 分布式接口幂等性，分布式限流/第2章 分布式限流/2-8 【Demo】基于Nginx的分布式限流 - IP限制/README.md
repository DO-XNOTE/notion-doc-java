---
title: 2-8 【Demo】基于Nginx的分布式限流 - IP限制
---

# 2-8 【Demo】基于Nginx的分布式限流 - IP限制

[image](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/d8859706-1311-4382-8bab-64abba89a486/SCR-20240808-iaym.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QYLET3HT%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T225458Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIEwQt8l5kbJdfDxUnDZfYkCQ94Vuhra5rPqJ2epvtSQsAiB%2BB3rsRHl7yglS4lj5tTGsTcZkA77P3N%2FynDfPIh9tiyqIBAjG%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMaquPkhc5CedDMGmgKtwDDOpvW6GoIQ63ct6%2Foh%2F0tAIz32nFMdgcDtI80Aoz6QfcXi6%2F%2FHVdX2E%2FYXvErZ4FkWnT6mMM6T561gZ%2BORcxXTZASoag16OiZDdxnSRaEHTuqVM8Gj5TW8OX2R%2FT%2BcIAX1XHHYaN64PVh%2FukJhxFQktc8XcLW41yMdCwHWaB6A5CsMHRAMPjwGPsBUP7UW4b%2FbTZaoiExlV4RJ%2Bkf%2B%2BOWA8PrVTlwvf7sIXGDgNgMjEGBpmpcvUjzPELFO%2FB%2BfaJkZ8jZds5XXoMKBZGS8F78Qu8SJ47ylY%2BTxOafWT72qKouJCj8w1c94L1ub0SmCX%2F8nmM1xCIf698ioWJ6T2t8NkIZe3TO2vh8%2BnRQKwmG55N6JuEb9Wsill4b9XueqxDxhULbzUMS5brrSmkZqkJxITH8XVbNelPWQ25t7wAwNenopLiIZOcgdcpmODgB4HfUerw0pMMsmPY3Imt3Xq9RaFluX7n8b9UH2juJi0e7%2FxmzvAAXGWVtSejW0HYs%2BRj0GetVT4oOSJFhUzS5yVNac9EkucHn6XKNLq1k6gk0%2BfnP3La81DQB1PApYf%2BQn3avoElf8tgBB8Gfdyr1LAXKCkBu4%2Bp49eJwqkL1xnt4oKXOa9HlAOevmXm6vMwt7%2F%2F0gY6pgGrXUSr55iJTTlGOP1Ri8LFQY%2FwRhXyybjomWs7yhPMqJ%2F43CxoaUaQGlcIR0EpXxCKxuyhXzAdu24ZA%2BOj%2BQ2%2F%2BBBbrIj5nMo58lWSMnW86fOahu0IFLvLzPGNgKY4MzLFhfr%2FfLOugBURPdDdBJ%2FRopZQxaxsvXglPtmG5Xn83Mb%2BEzOEyA1BRbauZZbQ%2BEM1CIWqMRWf17ZtueVj0ezuxkL2tuqc&X-Amz-Signature=9081a63f7f74373e936da0482545a40232989a7020f639bfb2fa7709ff7c5383&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

[image](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/7f2c7748-8f7f-4465-9a5c-7d625b422197/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QYLET3HT%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T225458Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIEwQt8l5kbJdfDxUnDZfYkCQ94Vuhra5rPqJ2epvtSQsAiB%2BB3rsRHl7yglS4lj5tTGsTcZkA77P3N%2FynDfPIh9tiyqIBAjG%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMaquPkhc5CedDMGmgKtwDDOpvW6GoIQ63ct6%2Foh%2F0tAIz32nFMdgcDtI80Aoz6QfcXi6%2F%2FHVdX2E%2FYXvErZ4FkWnT6mMM6T561gZ%2BORcxXTZASoag16OiZDdxnSRaEHTuqVM8Gj5TW8OX2R%2FT%2BcIAX1XHHYaN64PVh%2FukJhxFQktc8XcLW41yMdCwHWaB6A5CsMHRAMPjwGPsBUP7UW4b%2FbTZaoiExlV4RJ%2Bkf%2B%2BOWA8PrVTlwvf7sIXGDgNgMjEGBpmpcvUjzPELFO%2FB%2BfaJkZ8jZds5XXoMKBZGS8F78Qu8SJ47ylY%2BTxOafWT72qKouJCj8w1c94L1ub0SmCX%2F8nmM1xCIf698ioWJ6T2t8NkIZe3TO2vh8%2BnRQKwmG55N6JuEb9Wsill4b9XueqxDxhULbzUMS5brrSmkZqkJxITH8XVbNelPWQ25t7wAwNenopLiIZOcgdcpmODgB4HfUerw0pMMsmPY3Imt3Xq9RaFluX7n8b9UH2juJi0e7%2FxmzvAAXGWVtSejW0HYs%2BRj0GetVT4oOSJFhUzS5yVNac9EkucHn6XKNLq1k6gk0%2BfnP3La81DQB1PApYf%2BQn3avoElf8tgBB8Gfdyr1LAXKCkBu4%2Bp49eJwqkL1xnt4oKXOa9HlAOevmXm6vMwt7%2F%2F0gY6pgGrXUSr55iJTTlGOP1Ri8LFQY%2FwRhXyybjomWs7yhPMqJ%2F43CxoaUaQGlcIR0EpXxCKxuyhXzAdu24ZA%2BOj%2BQ2%2F%2BBBbrIj5nMo58lWSMnW86fOahu0IFLvLzPGNgKY4MzLFhfr%2FfLOugBURPdDdBJ%2FRopZQxaxsvXglPtmG5Xn83Mb%2BEzOEyA1BRbauZZbQ%2BEM1CIWqMRWf17ZtueVj0ezuxkL2tuqc&X-Amz-Signature=d6153850278db77fb302c3e45dc900d33fb7c5724d15747c0601b5d8eac2b8a9&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

[image](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/20c40e92-11e1-42cc-9032-f0559f32cd88/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QYLET3HT%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T225458Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIEwQt8l5kbJdfDxUnDZfYkCQ94Vuhra5rPqJ2epvtSQsAiB%2BB3rsRHl7yglS4lj5tTGsTcZkA77P3N%2FynDfPIh9tiyqIBAjG%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMaquPkhc5CedDMGmgKtwDDOpvW6GoIQ63ct6%2Foh%2F0tAIz32nFMdgcDtI80Aoz6QfcXi6%2F%2FHVdX2E%2FYXvErZ4FkWnT6mMM6T561gZ%2BORcxXTZASoag16OiZDdxnSRaEHTuqVM8Gj5TW8OX2R%2FT%2BcIAX1XHHYaN64PVh%2FukJhxFQktc8XcLW41yMdCwHWaB6A5CsMHRAMPjwGPsBUP7UW4b%2FbTZaoiExlV4RJ%2Bkf%2B%2BOWA8PrVTlwvf7sIXGDgNgMjEGBpmpcvUjzPELFO%2FB%2BfaJkZ8jZds5XXoMKBZGS8F78Qu8SJ47ylY%2BTxOafWT72qKouJCj8w1c94L1ub0SmCX%2F8nmM1xCIf698ioWJ6T2t8NkIZe3TO2vh8%2BnRQKwmG55N6JuEb9Wsill4b9XueqxDxhULbzUMS5brrSmkZqkJxITH8XVbNelPWQ25t7wAwNenopLiIZOcgdcpmODgB4HfUerw0pMMsmPY3Imt3Xq9RaFluX7n8b9UH2juJi0e7%2FxmzvAAXGWVtSejW0HYs%2BRj0GetVT4oOSJFhUzS5yVNac9EkucHn6XKNLq1k6gk0%2BfnP3La81DQB1PApYf%2BQn3avoElf8tgBB8Gfdyr1LAXKCkBu4%2Bp49eJwqkL1xnt4oKXOa9HlAOevmXm6vMwt7%2F%2F0gY6pgGrXUSr55iJTTlGOP1Ri8LFQY%2FwRhXyybjomWs7yhPMqJ%2F43CxoaUaQGlcIR0EpXxCKxuyhXzAdu24ZA%2BOj%2BQ2%2F%2BBBbrIj5nMo58lWSMnW86fOahu0IFLvLzPGNgKY4MzLFhfr%2FfLOugBURPdDdBJ%2FRopZQxaxsvXglPtmG5Xn83Mb%2BEzOEyA1BRbauZZbQ%2BEM1CIWqMRWf17ZtueVj0ezuxkL2tuqc&X-Amz-Signature=1c73b340e9f87442554fa5178f261c495aec39bcee69dea3b6c51226a357b351&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

hello 慕课网的各位同学们，大家好，这一节里老师将跟大家介绍一个正经的分布式限流方案。那这个方案有多正经呢？嘿我们就来看一看他的课程内容。咱这一节介绍的是基于 ngx 的 IP 限流课程则分为三个部分。首先我们要添加一个 ctrl 的方法，这个 ctrl 的方法中的业务逻辑是专门给 ngx 来调用的。紧接着我们要修改网关层的配置，这里面包含了两个部分，第一先要修改 host 文件给我们指定的一个域名导向到咱的 127 零点零点幺也就是本机的 local host 地址。紧接着在 NGINX 的 config 文件下面，把前面修改的 host 地址映射进去。

[image](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/07fefcb0-9132-4fcb-a91a-32272cfbaa0e/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QYLET3HT%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T225458Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIEwQt8l5kbJdfDxUnDZfYkCQ94Vuhra5rPqJ2epvtSQsAiB%2BB3rsRHl7yglS4lj5tTGsTcZkA77P3N%2FynDfPIh9tiyqIBAjG%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMaquPkhc5CedDMGmgKtwDDOpvW6GoIQ63ct6%2Foh%2F0tAIz32nFMdgcDtI80Aoz6QfcXi6%2F%2FHVdX2E%2FYXvErZ4FkWnT6mMM6T561gZ%2BORcxXTZASoag16OiZDdxnSRaEHTuqVM8Gj5TW8OX2R%2FT%2BcIAX1XHHYaN64PVh%2FukJhxFQktc8XcLW41yMdCwHWaB6A5CsMHRAMPjwGPsBUP7UW4b%2FbTZaoiExlV4RJ%2Bkf%2B%2BOWA8PrVTlwvf7sIXGDgNgMjEGBpmpcvUjzPELFO%2FB%2BfaJkZ8jZds5XXoMKBZGS8F78Qu8SJ47ylY%2BTxOafWT72qKouJCj8w1c94L1ub0SmCX%2F8nmM1xCIf698ioWJ6T2t8NkIZe3TO2vh8%2BnRQKwmG55N6JuEb9Wsill4b9XueqxDxhULbzUMS5brrSmkZqkJxITH8XVbNelPWQ25t7wAwNenopLiIZOcgdcpmODgB4HfUerw0pMMsmPY3Imt3Xq9RaFluX7n8b9UH2juJi0e7%2FxmzvAAXGWVtSejW0HYs%2BRj0GetVT4oOSJFhUzS5yVNac9EkucHn6XKNLq1k6gk0%2BfnP3La81DQB1PApYf%2BQn3avoElf8tgBB8Gfdyr1LAXKCkBu4%2Bp49eJwqkL1xnt4oKXOa9HlAOevmXm6vMwt7%2F%2F0gY6pgGrXUSr55iJTTlGOP1Ri8LFQY%2FwRhXyybjomWs7yhPMqJ%2F43CxoaUaQGlcIR0EpXxCKxuyhXzAdu24ZA%2BOj%2BQ2%2F%2BBBbrIj5nMo58lWSMnW86fOahu0IFLvLzPGNgKY4MzLFhfr%2FfLOugBURPdDdBJ%2FRopZQxaxsvXglPtmG5Xn83Mb%2BEzOEyA1BRbauZZbQ%2BEM1CIWqMRWf17ZtueVj0ezuxkL2tuqc&X-Amz-Signature=1f9a35f064549ba649fb2b992f96d881f86650e1b62d904327e1d0b15732103d&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

最后一步我们就要在 NGINX 里面配置限流规则，并且让 NGINX 重新加载配置，使之生效。以上就是这节课程的内容了，同学们快跟我奔赴 intelligi 我们开拔每天扣订 1 小时，健康工作 50 年。咱接下来要给自己的应用添加一个 controller 方法的。这个 controller 方法非常的轻便灵巧，就打一行 log 什么都不干。那咱还是回到 rate limit 这个项目里面，打开这个 controller 然后在这下面添加上这样一个方法，给它来一个注释，叫 NGINX 专用 OK 这个方法的名称，咱就给它叫做 ngx 好了，ngx什么入参都没有，就干这么一件事儿，打一行 log antics successok 然后 return 一个 success 搞定了。


这个方法的开头要有一个 get mapping S 我们依然给它起名叫做 ngx 这个方法好了以后，我们接下来还有几个要改动的地方，我在这里把这几个步骤跟大家写一下。咱首先是要怎么样修改 host 文件。好，我们每写一步就去跟着手把手的做一步。这里我来把 host 文件的地址给它打开，修改。 host 文件中什么内容呢？我们这样把 3w.imock 杠 chiming 指向哪里呢？指向咱的 local host 幺 27 零点零点幺。 OK 那我们每打一个步骤，就去实际的手把手做一个打，打开 banner 里面找到 host 这个文件，跟大家看一下老师这里是怎么配置的。我们把这个文件放大，同学们可以看到这么一行，它这里面这行配置是 12 七零点零点幺。然后怎么样把后面的这个 IMock 群里这个网址域名定向到了当前的 local host 我们把这一行复制下来，回到以太 dj 里面。 OK 我们把这个示例给它 copy 下来。
那接下来这个文件添加好了以后，我们怎么样？我们要去修改 NGINX 修改 ngx 的什么内容呢？将上一步也就是步骤一中的域名添加到路由规则当中。


恩杰克斯相信大家在前面的分布式章节已经学得滚瓜烂熟了，老师这里就不跟大家从头到尾在检视安装的过程了，我们直接拿来就用这里给大家看一下我本地的 NGINX 的版本，我是把这个 NGINX 安装在了 USR 然后是 local local 下面的 ngxok 我们调用它 sbn 方法中的 ngx 然后版本号的命令是杠 V 看一下老师这里的版本号是 ngx 的一点六点二这个版本。好，那我们接下来就去对 ngx 动动刀子了，去改一下它的。配置文件它坐落在哪里呢？配置文件地址，比方说老师这里是 USR 然后在它下面的 local 后面再跟 NGINX 然后在哪里在 CONF config 这个文件夹下，我们找哪一个文件呢？咱就找这个文件 ngx.conf 好，我们接下来就去配置文件夹中把这家伙给揪过来。看到这里就是他了，咱为什么要把它揪出来呢？因为我是 Mac 系统，在这个文件夹下我是不能直接更改文件的，有一些公司的限制。那我们把这个文件给放到哪里呢？我们来看，就把它扔到这个 resources 文件夹下面。
好了，OK那我们收集小桌板可以来进行配置啦，我们把这个浏览器滚滚到最下面。打住到这里。好了。好，那我们就从这一行开始配置了，咱先来配置一个 server 的 node NGINX 的配置，相信前面大家都学得滚瓜烂熟，我们这里就用最简单的配置先让它跑起来。


OK 那这个 server 节点下面的 server name 是谁呢？咱刚才在前面已经配置过了，它的 server name 是 3w.imock 我们的独家冠名商 IMock 然后杠 training 再一个点 com com 那这后面加上一个分号好，定义完这个以后，咱再给它添加一个 location 我们要在前面添加一串独立的一个短路径，这个路径我们就叫它 access limit 好了，也就是访问限制。那 location 里面跟谁呢？我们在这里把它标注下来。好，我们使用 proxy pass 然后把它定向到 HTTP 冒号幺二七点零点零点幺后面跟谁呢？端口号10086。


好，大家记住，后边这里有一个斜杠，这个斜杠很关键，大家一定要把它给打上。好我们这里再加一个分号，那么到这咱的 ngx 初步配置就完成了。这里咱还没给他添加限流规则，不用急，面包会有的，限流规则也会有的。那接下来我们先把这个改好的 ngx config 文件，我们找到这个文件所在的路径就在这里了，把这个 NGINX config 文件 copy 一下，复制到当前的 NGINX CONF 下面，然后点击 replace 那这里需要输入我的高级权限， Mac 系统真是限制多。好，我们看这里应该已经被改掉了。


OK 那咱现在可以启动一下 NGINX 做一下测试，看它是不是生效。好，就在这把 NGINX 给它启动起来怎么运行从 USR local ngxsb 这个文件夹当中直接运行 ngx 大家运行的时候可以尝试着使用 stool 来运行。 OK 好，那咱到浏览器里面看一下，先打 local host 的端口，如果是默认的 ngx 配置，这里应该会输出一个 welcome 页面。果然那接下来我们测试一下刚才添加的路由规则会不会生效，我这里调用一个什么呢？ 3w.imock 杠 training com 然后后面跟一串路径，这个路径是 access limit 就是咱在 ngx 当中配置的这一项。大家看还记得吗这一项。 OK 那接下来他谁呢？访问一个 ngx 的方法，这就是咱在 ctrl 里定义的方法，我们点击一下调用，看它是不是能成功的把请求发送过去。好，果然生效了。这里返回了 success 那咱这一步配置好了以后，我们再回到 intelligent 里面继续咱的文案工作。什么文案？在这里，要把步骤给同学们都给写上。


第三步怎么样？添加配置项，然后这个配置项咱都把它放在哪了？我们把 NGINX 的 config 文件 copy 到这，同学们一定要记得到 resources 下面，把它拿过去，然后放到本地就可以生效了。这里也可以看到本节课程包括下一节课程，所有的配置以及它相关的注释我都会放在这里。所以我这里会记这样一句参考 resources 文件夹下面的 ngxconf 文案工作已经搞定了，接下来我们就到配置文件当中大改一番。接下来咱在这个 server 的头顶给他声明这样一个方法，我们加一行注释，叫根据 IP 地址限制速度。这就是本节内容的主线了。好，我们这里直接先把这一行给它打印出来，再挨个跟大家解释这一行里面都代表着什么内容。好，我们首先打这样一个关键字， limit request zone 这个 zone 实际上就是我们给定的接下来的这个参数，大家看叫什么叫 binary 下划线 remote 在下划线 addressok 那接着往后打，大家先不要管这是什么好读书不求甚解，等我全部打完再跟大家一一解释。


好，我们接下来要声明这样的一个变量，zonezone等于什么等于 IP limit 这个名字大家可以随便起，放飞自我随便起，但是只要不要起中文就好了。同学们，咱这又不是中文编程语言，后面跟着一个冒号 20m 这 20m 可不是 20 分钟的意思，待会跟大家揭晓。


最后一个属性是一个 rate 咱给它定义成 one R per second 这里大家应该可以很容易的猜到它是限流的速率，对不对？每秒钟一个 request 好勒。这接下来我就要跟大家挨个解释，这里一行当中的每一个字段都是代表着什么含义了，那我先从哪个开始啊？从第一个参数开始，这个参数是什么呢？就是它了，我们先把它复制起来，代码写的烂没关系，咱这个文档工作要做的好，输人不能输装备要开始跟大家解释这第一个参数。其中我们可以看前面这个 binary 这个 binary 是比较特殊的一个相当于关键字的东西，它代表着什么呢？它的意思就是有一个特殊的目的是缩写内存占用量。


这后面的 remote address 代表着什么？表示通过 IP 地址来限流大家，并不用给 remote address 进行赋值，你可以把它理解成是 NGINX 当中的一个什么？一个系统变量恩杰克斯看到这一行字就会自动的使用访问者，也就是来访者的这个 IP 地址，并且把它缩写一下，降低内存的占用。 OK 那接下来咱第一个参数看完了以后，看。


第二个参数那是谁呢？是这个 zone 等于 IP limit 20。这里要跟大家解释两个内容。首先第一个是什么是 IP limit 这是什么意思呢？这个代表着一块内存区域，我们就把它当做是这项内存区域的一个变量名。那后面的这个 20 是什么含义呢？它是指这块内存区域的大小。那把整句话连接起来就是什么？就是我定义了一个 zone 这个 zone 是什么呢？是一个以 IP limit 作为名字的一块 20 兆大小的内存区域。那这块内存区域是用来做什么用的呢？它是用来专门记录什么，记录你的访问频率信息。好，我们这里把这行注释打全叫记录访问频率信息，这是这块内存区域做的事情。


OK 那第二个参数看完了，我们接下来看第三个参数。但是第三个参数大家应该从字面意思上就很好理解它代表着什么，每秒放行一个请求，这 R 就是 request 了，S就可以把它理解成 seconds 其实就是seconds 。但是我这里要跟同学说一下，它还有其他很多种不同的配置，比如什么呢？比如这里我配置 100 杠 M 是什么意思啊？每分钟每个 minutes 有 100 个请求可以把你给放过去。


那关于 rate 的其他表达式，同学们可以到网上去搜索相应的配置项，我这里给他注释一下，标识访问的限流频率。 OK 那咱上面的这个变量定义好了，咱接下来就要看怎么在这个 server 里面把这个配置给它应用起来，非常非常的简单。我们把这个定义在哪了？定义在咱刚才创建的这个 location 里面。


我们另起一行怎么来限定呢？还是用一个关键字叫 limit request 通过这个关键字大家可以知道是什么。跟前面这个 limit request zone 是不是非常像，limit request 是应用在具体的限流规则当中对你的访问频率做限制的。


那它后面跟什么呢？跟一个 zone 这里要指定一个 zone 的名称指定谁，大家看上面这一行当中，哪一个属性要放在这里，这这这在哪在哪在哪，再往后到了就在这里。 IP limit 把这一行 copy 一下扔在这个 zone 这里。接下来我这里还要再声明一个变量，我想展现一些高级用法，burst first 给它设置成几设置成2。 OK 然后我还想再秀一下操作，这个最后秀的一个操作是叫 no delayok 一个分号。同学们看不懂什么意思，我这里要跟大家解释一下。同样的，我这里要跟大家说这是基于 IP 地址的限制，那他这里依然有三个配置项，我们来跟大家挨个解释一下。


第一个参数，这个 zone 等于 IP limit 这是什么含义呢？这是引用前面的这个 limit request zone 中的 zone 信息，它是一个变量。 OK 那第二个属性又是什么含义呢？第二个参数是谁？是 burst 咱秀的第一把操作 burst 等于2。那 burst 是什么含义呢？爆发的意思，这个配置项意思是设置一个大小为 2 的缓冲区域。这个缓冲区域是什么意思呢？就是说当你有大量的请求过来的时候，当大量请求到来，然后怎么样呢？咋说了，缓冲去云，自然就是说当你的请求数量超过了你限流的频率以后，超过限流频率10，将其怎么样呢？放入缓冲区域。


OK 这个缓冲区域可不是个无底洞，它是有大小的，咱这里设置的是2。那接下来我们看第三个参数，第三个参数是谁呢？这是秀的最后一把操作。 no delayno delay 的意思是什么？就是缓冲区满了以后直接返回 5503 异常。 OK 那这里的配置就全部配置好了，给大家稍微总结一下。那这块区域是以 IP 地址作为限流的目标，然后给它这块地址 zone 起名叫 IP limit 它占用 20 兆的内存，并且限流的速率是每秒钟一个 request 然后我们将这里声明的 IP limit 应用在了当前的这个 location 里。 access limit 的 location 里给它指定了一个区域大小为 2 的缓冲区域。并且当缓冲区满了以后，直接返回 503 的异常。


好，我们仔细检查一下，发现好像漏了一个小尾巴在这里。有一个分号忘了，其实老师真的蛮讨厌这种编程语言，必须以分号结尾的。像近些年来一些大红大紫的新的编程语言，它其实可以什么符号都不声明，这种语法真的看起来蛮清爽的。不过因为 ngx 是一个非常非常非常老的技术了，所以还是把这个分号的习惯给它继承了下来。 OK 我们这里可以把刚才给他写好的 ngx config copy 一下，把它复制到 ngx 的 config 文件夹下。


好勒。然后咱这个配置文件变了，它需要在 ngx 中重新加载一下。我们直接跑起，在 stood 下面跑 ngx 的杠 S 后面跟一个空格，再加上 reload 我把这个命令行完整的给他 copy 一下，放到咱一台 dj 里面，在 ctrl 乐里的注解，这里跟大家说一下，重新加载 NGINX 它的命令是什么？就是这个。好，但如果大家的 ngx 没启动，你重新加载其实是不起作用的。要确保 ngx 处于启动，在这个状态下你才能运行 reload 我们这里跑一把，reload很快 angx 就已经刷新好了。


接下来我们走到 postman 里还是原先的味道还是原先的方法，我们这里发起调用，看它会不会被限流。现在调用速度很慢，我们要开始加快速度了。准备好了吗？走，你爬爬。同学们看到吗？这里返回了一个什么错误啊？ 503 series temporarily unavailable 暂时的服务不可用。那所以咱刚才配置的基于 IP 地址的限流已经完美生效了。 OK 那本节的内容就到这里结束了。


后面一个小节，我将跟大家介绍更多的 ngx 的限流方式。比如说我们不光可以根据他的 IP 地址做限流，咱还可以根据 server 做限流。也就是说在你的服务器这个级别，不管你有多少个 IP 地址来访问，我在全局控制一个总的每秒或者每分钟它的可允许访问的次数。除此以外，我们还可以对连接数加以限制。同学们预期还有哪些限流方式，且听老师下回分解。 OK 同学们，我们下一节课程再见。



