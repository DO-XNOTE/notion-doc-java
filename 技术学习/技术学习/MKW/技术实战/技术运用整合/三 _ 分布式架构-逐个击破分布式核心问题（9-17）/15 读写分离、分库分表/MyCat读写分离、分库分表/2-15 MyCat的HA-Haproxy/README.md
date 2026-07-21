---
title: 2-15 MyCat的HA-Haproxy
---

# 2-15 MyCat的HA-Haproxy

[image](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/b7758933-1069-45e6-ab47-d72670937487/SCR-20240807-rnal.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UL74V5ZD%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T225413Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIBNJ2OVV1CWUvClOOSdB4Bz%2BuADsfupsBWehclvoNLmIAiEA0KwdDr1i%2Fvi5AKkImjDb3poDBMFcFMYdiagPE%2FoMFq4qiAQIxv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDKaVvScIAAEf8BzFlSrcAwG46e%2FEzxZFI7OfPZeKvbSi%2BsVMLKbk9IxF8QyMWK58CNA%2Bp0pplQOsI%2BUCqwGJu%2FCw41EyhZ2MLtlsW0pGDr02HBih082mqpORDFh3ttQ6eWeNZ9%2FxbLM2S5Dwj7th8pRWIgUhpQSaZ8DZxxW1ll%2FedW3ghzX0AuSmZuTSyqssVtQhU6T%2BvWOU7lmJvr%2F2FoRjz7%2Bu6QX%2BSZcaE5lLlSaeThHvDaCVN1T%2BgXOJvtXQeOcPLq35XyGWmr2LWMKSgOL%2B7SQmpv00nXn8iRAqQSEJEgmRvS84Zgj1nbIJFPVRFhImg7FVZCTQ6Uc0E5dOURLlDm7iktFBD7SxaT1%2BqF80BRnboBD24fUn3ijEInkgJjwcbSn9%2FlbN4k8JolrzndNiF4wJaMCWPdNHVmimaLbDxQzkW4rpqHuLHmVTfEGR8dWLthOGv2zJLDG5Z8u38m%2Bm3imwD9cjzBmpQgX%2BgyVQgmnPPDTw2GfpSDHgErHnUYmdBIcljse7yWQG8kFFMWssJaLfld1wNmf1O47BfnvMrWJfXtvCxwhaJYlFHR2P9VGT8cnio25kPg%2Bf648FT%2B%2FCJ1ajYv%2Bn3B59YRNIT5%2B5be8wA3i0SoH0w7usYobrUqwN%2Bga5%2Fp%2BsD1rPMKe3%2F9IGOqUBUIgAG2D0pxUBT9E4u3mXbp4dTP89GRUI%2B8qAG%2FB8n3KxFzKil4OIlvH53okBiTb5EsjyEiM60EZueTveniQWhZ1zd7o213nHwbMQW8i6z0SkVrjBmgBXKnYfcFewcKF%2FSuAustT6uaINrq%2BoU1s9A7rpOmRvP6s9JE0KvipgOkZimi6qm%2BH%2FxxdnHsTkDNk1EhCS4Ooj4djcjrXjpjGYTxOE4g7a&X-Amz-Signature=adbfbee9eb0ee69f42681689e4c3ea76c53b79287b52fe5c9afc048d6a2b8400&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

[image](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/6a4cc463-8b22-4190-acb1-5add3f08c010/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UL74V5ZD%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T225413Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIBNJ2OVV1CWUvClOOSdB4Bz%2BuADsfupsBWehclvoNLmIAiEA0KwdDr1i%2Fvi5AKkImjDb3poDBMFcFMYdiagPE%2FoMFq4qiAQIxv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDKaVvScIAAEf8BzFlSrcAwG46e%2FEzxZFI7OfPZeKvbSi%2BsVMLKbk9IxF8QyMWK58CNA%2Bp0pplQOsI%2BUCqwGJu%2FCw41EyhZ2MLtlsW0pGDr02HBih082mqpORDFh3ttQ6eWeNZ9%2FxbLM2S5Dwj7th8pRWIgUhpQSaZ8DZxxW1ll%2FedW3ghzX0AuSmZuTSyqssVtQhU6T%2BvWOU7lmJvr%2F2FoRjz7%2Bu6QX%2BSZcaE5lLlSaeThHvDaCVN1T%2BgXOJvtXQeOcPLq35XyGWmr2LWMKSgOL%2B7SQmpv00nXn8iRAqQSEJEgmRvS84Zgj1nbIJFPVRFhImg7FVZCTQ6Uc0E5dOURLlDm7iktFBD7SxaT1%2BqF80BRnboBD24fUn3ijEInkgJjwcbSn9%2FlbN4k8JolrzndNiF4wJaMCWPdNHVmimaLbDxQzkW4rpqHuLHmVTfEGR8dWLthOGv2zJLDG5Z8u38m%2Bm3imwD9cjzBmpQgX%2BgyVQgmnPPDTw2GfpSDHgErHnUYmdBIcljse7yWQG8kFFMWssJaLfld1wNmf1O47BfnvMrWJfXtvCxwhaJYlFHR2P9VGT8cnio25kPg%2Bf648FT%2B%2FCJ1ajYv%2Bn3B59YRNIT5%2B5be8wA3i0SoH0w7usYobrUqwN%2Bga5%2Fp%2BsD1rPMKe3%2F9IGOqUBUIgAG2D0pxUBT9E4u3mXbp4dTP89GRUI%2B8qAG%2FB8n3KxFzKil4OIlvH53okBiTb5EsjyEiM60EZueTveniQWhZ1zd7o213nHwbMQW8i6z0SkVrjBmgBXKnYfcFewcKF%2FSuAustT6uaINrq%2BoU1s9A7rpOmRvP6s9JE0KvipgOkZimi6qm%2BH%2FxxdnHsTkDNk1EhCS4Ooj4djcjrXjpjGYTxOE4g7a&X-Amz-Signature=e2da7bcf015af8d1e56cd4f243372d43e5f24145c2a2f4e518f11da73a680460&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

咱们先打开这个 navicate 看一下目前的这个链接。 131 和 132 都是买 SQL 数据库，咱们把这个名称先给它改一下。一会咱们在 131 和 132 上了，还要去装这个 HA proxy 这块咱们要区分开，咱们把名称给他改一下，叫做 mysql132 也要给他来一下，也叫做 MySQL 这个 130 是买 cat 对吧，后边给他备注一下，这样就没有问题了是吧，一目了然。然后买 cat manager 是 130 这台买 cat 的管理端口，这个咱们也改一下，一会可能还会有一个买菜的130。


好吧，这样咱们现在所有的这个组件包括数据库和买 K 等都已经备注好了。那么现在咱们还要再安装第二个买 K 的是吧。这第二个买 K 的咱们安装在哪台机上啊？安装在 131 上，咱们还是进入到 131 这台机器，然后再进入到 obt 这个目录，咱们把这个 130 上面的买 cat 给他复制过来，跨机器复制咱们用什么命令用 SCP 是吧？ SCP 然后 130 这台机器的用户 root 对吧，艾特后边跟 IP 19 二点幺六八点七三点幺三零后边跟冒号，然后后边跟你的目录对吧，OPT下边的 my cat 对吧，复制到当前目录这里面，咱们复制还是要用杠 R 是吧，就是递归要把你所有的 my cat 目录下的所有的文件都复制到，当前目录咱们用一个点去表示是吧，然后回车。这个时候让咱们去输入 130 这台机器的密码，咱们输入一下。


好，现在已经开始复制了是吧，把所有的这个文件都已经复制过来了，咱们进入到这个 my cat ，然后看一下让他，配置文件也已经复制过来了是吧。可以看到这块咱们上一节课做的一些子表，包括 province 全局表都在这里边。然后咱们把 131 和 130 这个两台机器的买 cat 给它启动一下，咱们直接用 star 然后 130 也启动一下 stat 对吧。好，这个时候咱们再进入到 navik 130 是吧，连接应该是没有问题的。好咱们再点开这个user ，查看一下这个order ，两条数据没有问题是吧，然后咱们再创建一个链接链接，131买 cat 咱们再试一下，咱们直接拿这个 130 的买 cat 给它复制一下对吧，改个名字 131 后边连接的地址也是 131 我们先测试一下，没有问题是吧，这个咱们连接打开这个 order 也没有问题是吧，咱们两个买 Kite 就都已经配置好了，然后再去配置这个 HA proxy HA proxy 咱们安装在哪台机器上？咱们安装在 132 上。
好吧，因为 130 和 131 都有买 cat 了，咱们安装在 132 上，咱们进入到 132 这台机器怎么去安装，其实也是非常的简单。使用这个亚木命令，咱们先搜索一下亚木色指 HA proxy 对吧，咱们看看搜索到了这个是吧。 Ha proxy. 咱们看一下它的这个说明。


Tcp http proxy and load balancer or high availability environment.
它是支持 TCP 和 HTTP 协议的。看来这个 HA proxy 要比 NGINX 要强大， NGINX 只支持 HTTP 协议，它是不支持 TCP 的。所以这块咱们要安装一下这个 H 1 proxy 使用 YAML 杠 Y install HA 咱们直接把这段复制一下。复制粘贴回车一下可以看到现在已经开始安装了。现在已经开始安装了是吧，这个下载的过程比较慢，到这里这个 HA proxy 已经安装完了。


那么下一步咱们就是要配置它配置这个 HA proxy 它的配置文件在什么位置呢？它的配置文件在这个 etc 目录下， etc 目录下边有一个 HA proxy 目录，走一个 HA proxy.config 这么一个文件，咱们先进入到这个文件，看一下它里边有什么内容，咱们看看。从头开始他的注释也已经写得很全了。这个是一个配置文件的一个示例是吧，它是针对一个外部应用的。咱们接着往下看 global global 的配置，它是一个全局的配置，配置了它的 log 包括最大连接数，这里面写的是 4000 用户组，这些咱们基本上就不用动它就可以了。然后接着往下看。这里边咱们要改一下。这里边写了一个默认的配置，默认的配置里边第一行， mode 模式，这里边写的是 HTTP 这个咱们要给它改一下改成 TCP 因为咱们连接买 cat 通过 HTTP 协议是不行的，咱们要通过 TCP 协议这块。所以这个 mode 咱们要给它改成 TCP 后边其他的东西咱们也暂时不用动。


然后再看看后边的这个配置。 front endfront end 是你前端的配置，它的这个前端是什么意思呢？就是你连接这个 HA proxy 这一段的配置，咱们看看它配置的是什么内容。这块可以看到它的端口是5000，咱们记住这个端口，然后后边配置的是一些静态文件。静态文件包括 pass depping 和 pass 摁的这个主要还是针对 HTTP 协议的这块，咱们就不用管它了。包括后边的这一段配置。可以看到他写的是 if URL static 就是说如果你的这个访问的链接是上面的这两段，他要使用 steady 和这个 second 是吧，就是要走这段配置，它去连接你后边的这个应用和服务是吧。然后还有一段 default 其他的这些链接都要走 default 咱们来接着往下看。可以看到这个 daca 它配置了两段，一个是 static 是吧，一个是 App 咱们就用默认的这个 App 就可以了。因为咱们是 TCP 连接连接过来以后，要走到这个 default bacon 的对吧。 default bacon 的后边连接的是 App 也就是后边的这一段，这一段咱们给他改一下，因为咱们只有两个来开的是吧，这块咱们把后两行先给它注释掉。


第一行配置是吧，balance负载均衡的策略这块写的是轮询，咱们也不用动，然后改一下后边的这两个 server 第一个咱们连接的是130，这个买 K 的是吧，幺九二点幺六八点七三点幺三零端口，8066。然后第二个服务是幺九二点幺六八点七三点，131端口也是8066。后边 check 它都会定时的去检查后边的服务是否可用。


好到这里，这个 HA prophecy 这个配置就配置完了，大家看到这块也不是那么难理解，如果大家想深入理解的话，可以看这个 HA proxy 的官方的文档，它里面还有一些每一个字段的这些解释都给标注的非常的清楚。咱们这里边只是简单的配置了一下它的整个的请求的路由，咱们配置完以后保存一下。然后要启动 HA proxy 是吧，启动咱们怎么启动？咱们先查，查一下现在有没有 HA proxy 的这么这个进程，没有这个进程是吧，然后启动咱们直接 HA proxy 这个命令后边跟 F 杠 F 是接你的。


配置文件咱们是在 BTC 下边配置 a proxy 然后 HA proxy.config 咱们敲一下回车，它这里边报了一些警告是吧，报了一些警告，咱们可以先忽略，因为前面它默认的配置是 HTTP 所以后边大家看了，这个 front end 和 back end 都是这个 htt 模式的，咱们这块先不用管，这回咱们再，看一下它的进程到底也起没起来。 HA proxy 这个镜头已经起来了是吧。然后咱们去通过 navicat 去连接这个 HA proxy 看看它能不能访问到后边的数据库。咱们还记得 HA proxy 它的端口是多少吗？ 5000 对吧，刚才咱们已在这个配置文件当中已经看到了，咱们再看一遍，就是在这个 front end front end 里边这块配置了一个5000。


咱们记住这个端口下面回到那位 K 的当中再创建一个链接，这个链接幺九二点幺六八点七三点幺三二对吧，这个是 HA proxy 对吧，咱们复制一下端口是 5000 用户名密码，这个就要输入你买 cat 的用户名密码了是吧，来开个咱们配置的是 root 然后用户名是123456，咱们先测试一下没有问题对吧，确定。


双击一下 user 这个库当中，咱们进入到 order 表，看看数据能不能正常查询没有问题是吧？能正常查询了咱们再多刷新几遍，因为毕竟它是负载到了两个买 Kite 上对吧？那么频繁的去刷新一下没有问题是吧。那么这个时候如果我有一个买 K 的挂了，它会出现什么情况？还能不能正常的去查询？咱们模拟一下，咱们把 130 这台机器的买 cat 给它停一下，进入到130，然后咱们把这个买 cat 给它关掉，咱们再查一下进程，看看还有没有这个买 cat 的进程没有了是吧。那么这个时候 132 的 HA proxy 只代理到了 131 这个买 cat 上，其实对咱们前端的这个查询应该是不影响的，咱们还是再刷新一下。 132 这个 HA proxy 没有问题是吧，咱们还是把这个 130 买 cat 给它启动起来。好到这里咱们这个 HA proxy 已经成功的安装好了，并且成功的代理到了 130 和 131 这两个买开的上对不对？咱们也模拟了，当有一个买开的挂了的情况下， HA proxy 还能不能进行查询。那么咱们再试试，咱们还是把这个两个把两个买开的都给它停掉，看他是什么情况，130给它关掉，131咱们也给它停掉，两缸埋开的都关了是吧。咱们再进行查询。可以看到，连接不了了，不能够读取到 MySQL 的连接了，咱们还是给它启动起来再试一下，再刷新一下。还没有反应过来是吧。好没有问题了是吧，又出来了这两条数据。
好。那么到这里，这个 HA proxy 搭建这个负载均衡，就先给大家介绍到这下一节，咱们要使用 people alive 了，再去避免 HA property 成为系统当中的单点。




## 

