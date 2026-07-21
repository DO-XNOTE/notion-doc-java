---
title: 2-17 MyCat的HA-keepalived（下）
---

# 2-17 MyCat的HA-keepalived（下）

[image](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/55e12157-708a-490e-8250-62a879ebaacd/SCR-20240807-rupl.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UQBTQDCD%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T225415Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDUQ1dKWsK%2FT6WdC%2BZj1HWqqPBvtblgDNeZmq4flpBtsQIhAIC7uWEHcwp0ZYXOEkqXCckxK6Nh00NDJvOJAZV1wmRoKogECMb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgwZHIa%2BLJGMeK3Sf%2BEq3APLiJ3gjBJu%2BSf7eFtiNQ4nnIDQqZ1c%2BgUXumaDj1HkRfW3OeowZMh5NL2YUxcEvKmtKcmr1dO3e1p61VoQYCuvzbLFtdSJPN31AnfXuw0veMFd5RZNkc7u6UeLswfMMF5VDoRq2N%2F1RO8rxBdDuVP%2Fss1ypCwku1FK0eVGX00InMWLlst3OcYwNFAymwfPAiJ7tWC7wuQ15dCZ%2FbD1K%2BawHprcVbG4Fczi92jvGVNDgjxef%2FyDhR5MJhXV1zDpd3UfL6lAE2MgZYx9Rzyl%2B50IggP%2FYfJi23bkt%2FYukZK5EDw6rAQEWffQMQO%2BaU6X7Anj%2Fa6TUgGaQ1zUcVreGi9ahUNN7PFBtMVZ0qRSOOvC6TxBZTj%2FMIy99rWJGj%2BHeiM718qqHouFBiOBf8ye7YejzuiafU9UqC3H4wMlOJnr1nQRpjQDqSxVOtVNjuIrNV9G3gi%2B7IciDV%2B9ZVYQL0z6f5Ir7W7fFgooWV37TJ3pr%2BbeR6MG6zwQTY%2B8ZmtgmioFGxli6vSdBrwF19Mw%2BFWrDUfDaoWpoDSHgUhZft3qnDUJ7iXzVYVk5CdV9TqZVPAZvzvbRpAuPpip7sYE0GBfpCexrkVwYE9Umn8peKM8LYDbFHrtsuaDWjvSgTC3uP%2FSBjqkAUECNg%2BAHaKh7aHKctg0C3602Vs0M5P6xV%2BXtU2GYUzBM0BWHt2GMBC%2FY%2BEBW7I50GN%2BtNNmXo88jC%2FLqad1TtnyWpAl7WkY4w7j5QthcISMN8hjcEzxMXqjBvUV8%2FyhJHkgj1APAGi7%2FydYdMVUr12IBkfh%2BOLJiPTAqWnFxb0SRMyAPY3%2B8mHKOKDlyfRFunTLsMhD9Oc4XdnSFqAoukmWGZVs&X-Amz-Signature=c8a45ae9e96ade43177cddba88240eacfc7b891ced991742f0a2c8fbf9c9bc2a&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

[image](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/b7ffca2e-35dd-4ff6-88a2-81436f400834/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UQBTQDCD%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T225415Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDUQ1dKWsK%2FT6WdC%2BZj1HWqqPBvtblgDNeZmq4flpBtsQIhAIC7uWEHcwp0ZYXOEkqXCckxK6Nh00NDJvOJAZV1wmRoKogECMb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgwZHIa%2BLJGMeK3Sf%2BEq3APLiJ3gjBJu%2BSf7eFtiNQ4nnIDQqZ1c%2BgUXumaDj1HkRfW3OeowZMh5NL2YUxcEvKmtKcmr1dO3e1p61VoQYCuvzbLFtdSJPN31AnfXuw0veMFd5RZNkc7u6UeLswfMMF5VDoRq2N%2F1RO8rxBdDuVP%2Fss1ypCwku1FK0eVGX00InMWLlst3OcYwNFAymwfPAiJ7tWC7wuQ15dCZ%2FbD1K%2BawHprcVbG4Fczi92jvGVNDgjxef%2FyDhR5MJhXV1zDpd3UfL6lAE2MgZYx9Rzyl%2B50IggP%2FYfJi23bkt%2FYukZK5EDw6rAQEWffQMQO%2BaU6X7Anj%2Fa6TUgGaQ1zUcVreGi9ahUNN7PFBtMVZ0qRSOOvC6TxBZTj%2FMIy99rWJGj%2BHeiM718qqHouFBiOBf8ye7YejzuiafU9UqC3H4wMlOJnr1nQRpjQDqSxVOtVNjuIrNV9G3gi%2B7IciDV%2B9ZVYQL0z6f5Ir7W7fFgooWV37TJ3pr%2BbeR6MG6zwQTY%2B8ZmtgmioFGxli6vSdBrwF19Mw%2BFWrDUfDaoWpoDSHgUhZft3qnDUJ7iXzVYVk5CdV9TqZVPAZvzvbRpAuPpip7sYE0GBfpCexrkVwYE9Umn8peKM8LYDbFHrtsuaDWjvSgTC3uP%2FSBjqkAUECNg%2BAHaKh7aHKctg0C3602Vs0M5P6xV%2BXtU2GYUzBM0BWHt2GMBC%2FY%2BEBW7I50GN%2BtNNmXo88jC%2FLqad1TtnyWpAl7WkY4w7j5QthcISMN8hjcEzxMXqjBvUV8%2FyhJHkgj1APAGi7%2FydYdMVUr12IBkfh%2BOLJiPTAqWnFxb0SRMyAPY3%2B8mHKOKDlyfRFunTLsMhD9Oc4XdnSFqAoukmWGZVs&X-Amz-Signature=e04b02f4030b92b02b174c15de085d3f5c78129c395714a227cef553dfa96bbd&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

[image](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/92e475f0-5fd2-4b69-b129-bd8ec7e0f899/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UQBTQDCD%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T225415Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDUQ1dKWsK%2FT6WdC%2BZj1HWqqPBvtblgDNeZmq4flpBtsQIhAIC7uWEHcwp0ZYXOEkqXCckxK6Nh00NDJvOJAZV1wmRoKogECMb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgwZHIa%2BLJGMeK3Sf%2BEq3APLiJ3gjBJu%2BSf7eFtiNQ4nnIDQqZ1c%2BgUXumaDj1HkRfW3OeowZMh5NL2YUxcEvKmtKcmr1dO3e1p61VoQYCuvzbLFtdSJPN31AnfXuw0veMFd5RZNkc7u6UeLswfMMF5VDoRq2N%2F1RO8rxBdDuVP%2Fss1ypCwku1FK0eVGX00InMWLlst3OcYwNFAymwfPAiJ7tWC7wuQ15dCZ%2FbD1K%2BawHprcVbG4Fczi92jvGVNDgjxef%2FyDhR5MJhXV1zDpd3UfL6lAE2MgZYx9Rzyl%2B50IggP%2FYfJi23bkt%2FYukZK5EDw6rAQEWffQMQO%2BaU6X7Anj%2Fa6TUgGaQ1zUcVreGi9ahUNN7PFBtMVZ0qRSOOvC6TxBZTj%2FMIy99rWJGj%2BHeiM718qqHouFBiOBf8ye7YejzuiafU9UqC3H4wMlOJnr1nQRpjQDqSxVOtVNjuIrNV9G3gi%2B7IciDV%2B9ZVYQL0z6f5Ir7W7fFgooWV37TJ3pr%2BbeR6MG6zwQTY%2B8ZmtgmioFGxli6vSdBrwF19Mw%2BFWrDUfDaoWpoDSHgUhZft3qnDUJ7iXzVYVk5CdV9TqZVPAZvzvbRpAuPpip7sYE0GBfpCexrkVwYE9Umn8peKM8LYDbFHrtsuaDWjvSgTC3uP%2FSBjqkAUECNg%2BAHaKh7aHKctg0C3602Vs0M5P6xV%2BXtU2GYUzBM0BWHt2GMBC%2FY%2BEBW7I50GN%2BtNNmXo88jC%2FLqad1TtnyWpAl7WkY4w7j5QthcISMN8hjcEzxMXqjBvUV8%2FyhJHkgj1APAGi7%2FydYdMVUr12IBkfh%2BOLJiPTAqWnFxb0SRMyAPY3%2B8mHKOKDlyfRFunTLsMhD9Oc4XdnSFqAoukmWGZVs&X-Amz-Signature=beaf37825ef2a999328fb63396df3311db8e0b52f49577c84df0d1b143977a23&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

在上一节的内容当中，咱们模拟了 HA proxy 宕机的情况。假如我的 HA proxy down 掉了这个 keyboard live 的并没有自动的切换，这个是一个失败的案例。咱们还是要看一看它的配置文件到底哪里有问题。咱们首先看一下 130 这台机器，看一下这个 people live 的配置文件。那么既然这一段配置这个 TCP 的这个配置没有作用是吧，那么一会咱们把这个 TCP check 给它删掉，这一段是干什么用的咱们也可以再说一下， TCP 这个 check 其实是 keep alive 的，他自己在做负载均衡的时候，要检查一下你的这个 real server 是吧。如果你的 real server 挂掉了，那么它会把你的这个服务从它的列表当中剔除掉。其实这个热 server 在这里也可以配置多个，它会在多个之间进行负载均衡是吧。但是咱们这里边只，配置了一个以后，你的这个如果 server 如果 down 掉了的话，那么它里边就没有真正的日用 server 了，那么这个时候这个请求就分发不下去了，这个咱们只是在这里边提一下这个 TCP check 咱们先给它删掉好删掉了是吧。


然后这块咱们要怎么做？咱们的目的是什么？目的是如果你监测到了 HA proxy 挂掉了是吧，然后我要把这个 keep live 的给它切换是吧？咱们之前做的那个案例是吧，直接把 people love 的给它 down 掉了，它是可以自动切换的是吧？咱们就是利用这么一个特点，在这里边咱们先写一个 vrrp script 这个就是监测 HA proxy 是否宕机的这么一个脚本。咱们起一个名字叫做chk 。 check hne proxy 是吧，然后里边要写他的脚本 script 然后是一个双引号，里边是你执行的这个脚本咱们要执行什么脚本呢？这里边咱们要给大家介绍一个命令，就是这个 qo qo 给他传一个参数0，然后后边跟你的要监测进程的名称，也就是咱们这里边的 HA proxy 如果你的 HA proxy 是正常的，那么它返回的值就是0。


如果 HA proxy down 掉了，那么它的返回值就是 1 咱们先给大家演示一下，这一段咱们先给它保存咱们执行的命令是 qo 是吧，然后杠 0 后面接你的 HA foxy 咱们看看现在是没有 qo 这个命令是吧，咱们还要把 qo 这个命令给它装一下，咱们还是使用 YARN 先搜索一下 to 大家看到搜索出来这么一个东西是吧，咱们要安装它安装这个软件 YARN install 是吧杠 Y 然后粘贴一下。


好，安装成功了是吧，咱们再执行一下 to 可以看到，现在这个使用的方法已经给咱们列出来了，咱们使用的是 to 杠 0 是吧。然后 HA proxy 看到，他给了一个提示叫做 HA proxy 也没有这个进程是吧？没有这个进程，咱们看一下它的返回值。 Echo. 然后 dollar 问号没有这个进程，它返回的值是 1 现在咱们把 HA proxy 给它启动起来杠 FE TC 下的 HA proxy HA proxy.config 现在咱们再执行 Q 杠 0ha proxy 这个 Q 并不是杀掉这个进程，它只是探测一下你的这个进程是否存在。


然后咱们再执行一下 echo 看看它的返回值百分之是0，咱们再用 PS 查看一下这个 HA proxy 它的进程并没有杀掉是吧，咱们可以放心大胆的用这个 to 杠 0 这个命令，咱们把这一段给它复制一下，然后给它粘贴到 people live 的配置文件当中 scrap 的对吧，然后粘贴一下，然后给他配置一个第二个参数 interval 它监测的这个时间咱们给它设置一下，设置成两秒钟执行一次对吧，这个脚本 check HA proxy 的这个脚本我们就已经写好了，然后要在这个 vrrp instance 当中要配置这个脚本是吧，让它去执行这个怎么配置？咱们要在这里边再新加一个叫做 track script 是吧。 track script 里边就是咱们写的这个 chk 杠 HA proxy 这样就可以了是吧。


这样这个需 IP 这个 199199 的这个需 IP 会执行 check HA proxy 的这个脚本是吧，这个脚本在上面，它每隔两秒钟去执行一次 Q 杠 0 这个命令，如果它得到的是 1q 杠 0 aja proxy 的结果，如果是 1 的话，那么说明这个 aja box 也挂掉了是吧。然后它会触发 130 的 keep a love 的去进行 IP 的切换。


这个就是这么一段配置，咱们把这个先给它保存一下，然后再配置 132 的这台机器。这台机器同样咱们要先安装 Q 这个命令，咱们先搜索一下，然后安装 install 是吧。杠 Y 复制，然后再粘贴一下，没有问题了是吧，然后实行一下，看看效果。 to 杠 0 HA proxy 没有这个进程是吧，然后把 HA proxy 给它启动起来再去执行。然后看一下结果，dollar问号返回的是0，没有问题是吧。然后咱们要改一下 people live 的配置文件，既然这个 TCP check 不管用，咱们就给它删掉。然后前边要给他加一个 vrrp script VRP script 是吧。然后里边 scrap 的脚本 to 杠0， HA proxy 英特尔间隔两秒钟执行一次，这块咱们也需要改一下。


这个 keep life 的当中没有死 live 这个状态，它叫做 backup 这个咱们也改一下。好，这样这个脚本就已经配置完了，然后还要在这个 instance 里边要加一个 track script 是吧，然后里边是执行的上面的脚本，这个脚本咱们忘了起名字了是吧，就发现了一个错误。
chkha proxy 是吧，咱们要执行这个脚本。 Chkha proxy. 这样这个 keep alive 的配置文件就已经修改好了。然后咱们启动一下，启动下 keyboard service keep alive 的 start 是吧，咱们查看一下进程，看看 keep alive 的到底起没起来，没有问题是吧。然后 132 咱们也启动一下苹果 live 的 star 查看一下进程， keep alive 的是吧，没有问题。


然后咱们要查看一下 IP 看看这个 199 的这个 IP 在哪台机器上。咱们现在 130 这台机器上是行一下 IP 和 dress 可以看到 199 在这个 130 的这个这台机器上。然后再看 132 IP dress 这里边是没有 199 的这个 IP 的。所以现在咱们通过 navicate 连接 199 的这个虚IP ，它会把请求转发到 130 的这台机器上，然后通过 130 连接 130 的这个 HA proxy 再去分发到两个 mycat 上，咱们执行一下199，咱们刷新一下，看看这两条记录能不能出来没有问题是吧。然后现在咱们把 130 这台机器的 HA proxy 给它刹到是吧，把它停掉。咱们先查看一下 HA proxy 的这个进程 16630 是吧，然后给它杀掉 16630 回车。然后咱们再查看一下 IP 地址没有生效是吧，没有生效。


然后咱们再看看这个配置文件，应该还是配置文件里边的问题，咱们看看配置文件里边大括号后边都没有跟空格是吧，这块咱们把这空格都给它加上。看来这个配置文件的语法要求还是比较严格的，咱们都检查一下，看看这块这个大括号也没有加这个空格，好保存一下。然后再检查一下 132 的这台机器，看看有什么地方没有加这个空格。看看这块没有加空格是吧，那空格加一下。再看看上边这块是有空格的。这个配置文件都已经检查完了。然后咱们把这个提过完 live 的给它重启一下提过 live 的 restart 对吧。 132 同样执行一下 service keep alive 的 restart 然后看一下 130 的这台机器的 ip199 是吧，咱们在 navik 的当中查询也是没有问题的。现在咱们把这个 130 这台机器的 HA proxy 给他杀得到 17576 是吧。q17576，然后再执行一下 IP address 咱们看看 199 的这个 IP 不在 130 这台机器上了。然后咱们再看看 132 ipso 可以看到这块 199 出现在了 132 的这台机器上，然后前端咱们再刷新一下没有问题是吧，不影响咱们前端的查询。现在咱们再把 130 的 HA proxy 给它启动起来。 etc 下边的 HA proxyha proxy.config 现在咱们再查一下 IP IP 还是没有变化，然后咱们再把 132 这台机器的 HA box 也给他删掉。


8803q8803 是吧，咱们再查看一下 132 这台机器的 IP 地址。 IP 要 dress119 已经从这台机器上消失了，在 130 里边咱们再执行一下看看。 119 又回到了 130 的这台机器，咱们前端 navik 的再去查询也没有问题是吧。好，那么到现在咱们就通过 people love 的做了一个 HA proxy 的热备是吧，不管这两个 HA proxy 哪个挂了，都会迅速的切换到另外一台机器上。在前端咱们连接这个虚 IP 是不受任何影响的，对后边的查询也没有任何的干扰。


好了，到这里这一节的内容就告一段落了。而且整个买 cat 的这一部分的内容也已经给大家介绍完了，这一部分的内容还是比较多的，大家课后一定要去多的消化，把每一个知识点都给它吃透。然后在项目当中咱们要多多的运用这些知识点，争取把 my cat 熟练地运用到自己的项目当中，解决一些项目当中实际的问题。谢谢大家。




