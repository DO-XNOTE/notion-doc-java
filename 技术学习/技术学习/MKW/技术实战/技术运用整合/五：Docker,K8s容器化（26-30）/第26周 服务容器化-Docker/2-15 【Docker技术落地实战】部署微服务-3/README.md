---
title: 2-15 【Docker技术落地实战】部署微服务-3
---

# 2-15 【Docker技术落地实战】部署微服务-3

[image](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/d9f4cd77-d3ca-40d9-bf3b-774a4315d416/SCR-20240725-dlsh.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WAKYWUYC%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T225928Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIHP05B29brcA5lhPizWSjqcMdzU7gjaFnHtd8XGT3tERAiACUneC3pg%2B%2F4shXnXeKVXX%2BbIIJ8s%2B%2FX%2BD4us536A2FCqIBAjG%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIM2l8pAmL9ooVQ5yH3KtwDDqpmBwWs%2Ftl%2BZ4OeQJJLc8VqPuBUPvgxo%2B8nOEW88LmXNxUVUE6xQbBkrJ4hcJWcqSl%2Bx%2F%2B7RE3qtbe59mEcuFGccwjhwrTgHMViJADPA8%2BsZqhN23PYrHC8xa%2FFWPlB4PTW769KpJtDaBVxTSyRPQrURpSxvb%2Fah%2F0Ztpxj7C%2BfQWR3jGiYMT01udnLrTFMerlRS3tGp7yuNEjXOnFJHnKUSHKxW3Nmu3v3fvFnYjYhSJd75FPy9Q2RFHePuvFwkMbhws55RRiiOtmG%2FeSCgtfJ%2FRdPD250oRZ0bc1Crqa2bUm2bYgrKYm7dK6OWng2FdZbMt7Di0F6DVzPPUVLgI%2Fwado1kW%2BoDVjSyYsDJDYak3xHzT0qS9KmCk3fu4rdv9KfwwtcYB4NbuAqRUwMhqBfAWusbL53MWngZMaAlK2S9BaYRbiEtns9eYP4a%2BtXNL54UpvK%2BjqRG3hIZSn6KtPT6DIuA95A26Ro9d9AcoOk5ZoyruVSEEZUVGh%2FyrJFYtG1aWfYH5mTIIrQDaqlnax6NifFfXJamo3llPeOMDWYSZiWGy1hoIcV3t%2BH5RqVDY8tGjUklo0xdyWpjlIxUBiLzFGhBKomzaxPQ2IzCaFiVTa1d1eR2IaGNrQwsbf%2F0gY6pgHm382EikWOIBEEt6LbUQ%2Frzjr9nb%2FbNUfUnp5yRew1EwvBc7dT2Lj%2B7J2L1lpFPcQPv2Aj%2B%2BV5MdlB0YzCK6%2B%2FMo7V32xtwha7Vo3HOgZJjFAXsGl5W%2F0ctwIVHnhdGKDyKCs63DtDcsSZTuA%2BriU%2FsyXrHcx1ETHBA5QZOjO9XfaQYtZ3tvSOuZdmP7lRBuRevtKyqx4LTj7pxOaKQMOB5d5AIbog&X-Amz-Signature=6b2529424c176e8d25786ab66d1865f4dda549489aea3f95ad7e662637e60026&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

[image](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/0afa1458-7905-4505-85fa-27faa37b6484/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WAKYWUYC%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T225928Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIHP05B29brcA5lhPizWSjqcMdzU7gjaFnHtd8XGT3tERAiACUneC3pg%2B%2F4shXnXeKVXX%2BbIIJ8s%2B%2FX%2BD4us536A2FCqIBAjG%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIM2l8pAmL9ooVQ5yH3KtwDDqpmBwWs%2Ftl%2BZ4OeQJJLc8VqPuBUPvgxo%2B8nOEW88LmXNxUVUE6xQbBkrJ4hcJWcqSl%2Bx%2F%2B7RE3qtbe59mEcuFGccwjhwrTgHMViJADPA8%2BsZqhN23PYrHC8xa%2FFWPlB4PTW769KpJtDaBVxTSyRPQrURpSxvb%2Fah%2F0Ztpxj7C%2BfQWR3jGiYMT01udnLrTFMerlRS3tGp7yuNEjXOnFJHnKUSHKxW3Nmu3v3fvFnYjYhSJd75FPy9Q2RFHePuvFwkMbhws55RRiiOtmG%2FeSCgtfJ%2FRdPD250oRZ0bc1Crqa2bUm2bYgrKYm7dK6OWng2FdZbMt7Di0F6DVzPPUVLgI%2Fwado1kW%2BoDVjSyYsDJDYak3xHzT0qS9KmCk3fu4rdv9KfwwtcYB4NbuAqRUwMhqBfAWusbL53MWngZMaAlK2S9BaYRbiEtns9eYP4a%2BtXNL54UpvK%2BjqRG3hIZSn6KtPT6DIuA95A26Ro9d9AcoOk5ZoyruVSEEZUVGh%2FyrJFYtG1aWfYH5mTIIrQDaqlnax6NifFfXJamo3llPeOMDWYSZiWGy1hoIcV3t%2BH5RqVDY8tGjUklo0xdyWpjlIxUBiLzFGhBKomzaxPQ2IzCaFiVTa1d1eR2IaGNrQwsbf%2F0gY6pgHm382EikWOIBEEt6LbUQ%2Frzjr9nb%2FbNUfUnp5yRew1EwvBc7dT2Lj%2B7J2L1lpFPcQPv2Aj%2B%2BV5MdlB0YzCK6%2B%2FMo7V32xtwha7Vo3HOgZJjFAXsGl5W%2F0ctwIVHnhdGKDyKCs63DtDcsSZTuA%2BriU%2FsyXrHcx1ETHBA5QZOjO9XfaQYtZ3tvSOuZdmP7lRBuRevtKyqx4LTj7pxOaKQMOB5d5AIbog&X-Amz-Signature=2af3b140758f42c245c9f62accaa27303520ce8fef0f920926f6f8a2cc27c18e&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

好，前一节我们已经聊过了是吧，我们平台上起的那些基本功能，比如像 rabbitmq redis mariadb 然后基于此，我们把 eureka 我们把 spring cloud config 起来了。

[image](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/ae39fb96-097e-4254-9a8f-0ca078ef818b/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WAKYWUYC%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T225928Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIHP05B29brcA5lhPizWSjqcMdzU7gjaFnHtd8XGT3tERAiACUneC3pg%2B%2F4shXnXeKVXX%2BbIIJ8s%2B%2FX%2BD4us536A2FCqIBAjG%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIM2l8pAmL9ooVQ5yH3KtwDDqpmBwWs%2Ftl%2BZ4OeQJJLc8VqPuBUPvgxo%2B8nOEW88LmXNxUVUE6xQbBkrJ4hcJWcqSl%2Bx%2F%2B7RE3qtbe59mEcuFGccwjhwrTgHMViJADPA8%2BsZqhN23PYrHC8xa%2FFWPlB4PTW769KpJtDaBVxTSyRPQrURpSxvb%2Fah%2F0Ztpxj7C%2BfQWR3jGiYMT01udnLrTFMerlRS3tGp7yuNEjXOnFJHnKUSHKxW3Nmu3v3fvFnYjYhSJd75FPy9Q2RFHePuvFwkMbhws55RRiiOtmG%2FeSCgtfJ%2FRdPD250oRZ0bc1Crqa2bUm2bYgrKYm7dK6OWng2FdZbMt7Di0F6DVzPPUVLgI%2Fwado1kW%2BoDVjSyYsDJDYak3xHzT0qS9KmCk3fu4rdv9KfwwtcYB4NbuAqRUwMhqBfAWusbL53MWngZMaAlK2S9BaYRbiEtns9eYP4a%2BtXNL54UpvK%2BjqRG3hIZSn6KtPT6DIuA95A26Ro9d9AcoOk5ZoyruVSEEZUVGh%2FyrJFYtG1aWfYH5mTIIrQDaqlnax6NifFfXJamo3llPeOMDWYSZiWGy1hoIcV3t%2BH5RqVDY8tGjUklo0xdyWpjlIxUBiLzFGhBKomzaxPQ2IzCaFiVTa1d1eR2IaGNrQwsbf%2F0gY6pgHm382EikWOIBEEt6LbUQ%2Frzjr9nb%2FbNUfUnp5yRew1EwvBc7dT2Lj%2B7J2L1lpFPcQPv2Aj%2B%2BV5MdlB0YzCK6%2B%2FMo7V32xtwha7Vo3HOgZJjFAXsGl5W%2F0ctwIVHnhdGKDyKCs63DtDcsSZTuA%2BriU%2FsyXrHcx1ETHBA5QZOjO9XfaQYtZ3tvSOuZdmP7lRBuRevtKyqx4LTj7pxOaKQMOB5d5AIbog&X-Amz-Signature=ef097e18170ccd2b2f9e261b9750c65fad5d453b88561000cd17fc4d04d24d27&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

那除此以外，其实平台层还有一些比如像 physics 的那个 dashboardturbine 还比如像 zipking elk 这些服务，希望大家在课后自己去起一下，因为它不是后面所有起的应用服务的一个依赖，什么而是一些追加的服务。所以我在这里因为简化期间是以最小服务启动这样一个 demo 给大家来展示的，所以我就不起了。

[image](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/3a91d796-107d-4870-b703-6deea0c52353/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WAKYWUYC%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T225928Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIHP05B29brcA5lhPizWSjqcMdzU7gjaFnHtd8XGT3tERAiACUneC3pg%2B%2F4shXnXeKVXX%2BbIIJ8s%2B%2FX%2BD4us536A2FCqIBAjG%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIM2l8pAmL9ooVQ5yH3KtwDDqpmBwWs%2Ftl%2BZ4OeQJJLc8VqPuBUPvgxo%2B8nOEW88LmXNxUVUE6xQbBkrJ4hcJWcqSl%2Bx%2F%2B7RE3qtbe59mEcuFGccwjhwrTgHMViJADPA8%2BsZqhN23PYrHC8xa%2FFWPlB4PTW769KpJtDaBVxTSyRPQrURpSxvb%2Fah%2F0Ztpxj7C%2BfQWR3jGiYMT01udnLrTFMerlRS3tGp7yuNEjXOnFJHnKUSHKxW3Nmu3v3fvFnYjYhSJd75FPy9Q2RFHePuvFwkMbhws55RRiiOtmG%2FeSCgtfJ%2FRdPD250oRZ0bc1Crqa2bUm2bYgrKYm7dK6OWng2FdZbMt7Di0F6DVzPPUVLgI%2Fwado1kW%2BoDVjSyYsDJDYak3xHzT0qS9KmCk3fu4rdv9KfwwtcYB4NbuAqRUwMhqBfAWusbL53MWngZMaAlK2S9BaYRbiEtns9eYP4a%2BtXNL54UpvK%2BjqRG3hIZSn6KtPT6DIuA95A26Ro9d9AcoOk5ZoyruVSEEZUVGh%2FyrJFYtG1aWfYH5mTIIrQDaqlnax6NifFfXJamo3llPeOMDWYSZiWGy1hoIcV3t%2BH5RqVDY8tGjUklo0xdyWpjlIxUBiLzFGhBKomzaxPQ2IzCaFiVTa1d1eR2IaGNrQwsbf%2F0gY6pgHm382EikWOIBEEt6LbUQ%2Frzjr9nb%2FbNUfUnp5yRew1EwvBc7dT2Lj%2B7J2L1lpFPcQPv2Aj%2B%2BV5MdlB0YzCK6%2B%2FMo7V32xtwha7Vo3HOgZJjFAXsGl5W%2F0ctwIVHnhdGKDyKCs63DtDcsSZTuA%2BriU%2FsyXrHcx1ETHBA5QZOjO9XfaQYtZ3tvSOuZdmP7lRBuRevtKyqx4LTj7pxOaKQMOB5d5AIbog&X-Amz-Signature=32613dd3fb6602869ec7a6ac6d8925deda39e04b661fabd1fb808bfbb24b9262&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

那大家可以尝试去起来一下，起完以后我们进入什么实际应用的启动阶段。那实际应用我们需要起哪些呢？我们需要起我们的 authentication 这样一个 domain 的应用。那还有基本的一个 user 的应用。那我这里会起这两个课后，大家可以去尝试如法炮制，特别是模仿 user 这个 domain 来起我们的 item cut order 那甚至于还可以自己在什么上一节那个我们的微服改造的那个课程的作业里面，一样去把我们的 payment 给我们的 search 完备了，然后也以我们的 Doc 容器的方式启动起来。
好，那这里我带了大家来启一下，来编译下，来启动一下这些应用。那首先我们去看一下我们的 authentication 的代码，那我们切回我们的这个 IDE 平台。然后我们找到 domain 里面我们有个什么 auth 对吧就是 authentication 那这个 authentication 这个部分，我们会可以打开我们具体的这个 service 那这个核心的内容都在 service 底下。那重点这里要改的什么 resource 文件？ 


application.yaml 好，我们这里放大，放大以后我们可以看到什么这里面它自己对外提供的端口是10,006，这就是容器内它对外提供了一个端口。你待会我们要记住要把这个端口映射到我们的服务器的 10,006 端口。那除此以外还有我们的 Redis 的 server 那本来写的是 local host 我这里改成了我们实际的服务器 IP 地址。


然后端口就是默认的 Redis 什么 6379 端口。因为之前我们在起 Redis 的时候，也是以 6379 映射到我们服务区的 6379 端口。这里要注意，把 password 给注释掉。因为我们在起这个 Redis 的时候它没有指定 password 所以这里不需要 password 那 zip key 如果大家起了的话也是一样的，就是把它的这个 IP 地址和它的端口在这里进行修改。如果没有起，这里就可以跳过 eureka 这里跟上一节的这个介绍是一样的。因为我们的 eureka 什么是一个容器，所以我们这里要选什么把它转换成我们的 prefer IP 地址。然后同时我们把我们的具体的物理 IP 地址服务器的物理 IP 地址在这里进行替换。端口还是可以沿用原来 server port 的端口来进行注册。这样的话就是我们自己要用这个 IP 地址的和这个端口在哪个urec ，在这个幺七二零幺九零四六零幺八三二万端口上绑定的这个友锐卡夫进行注册，这里填的是 urea 的实际服务。而下面这里填的是我们在 urea 上注册的名称是什么？是以这个地址的 10,006 端口来进行注册。


注册完了以后，我们就会在 ureka 的界面里看到有这样一个服务，叫什么叫 auth 这样一个服务，让他的这个 IP 地址冒号端口就是他实际注册的访问地址。那真正的应用在调用这个我们的服务的时候，如果要去找这个服务，就会去找这个物理机的这个幺七二点幺九点四六零幺八三这个 IP 地址的什么 1006 这个端口来进行访问。因为整个 demo 过程当中全是我是单容器形式以运行的，所以全部是以这个物理机的地址和端口。你在后面的章节 called foundry masses 和 coconities 里面，我们会什么以服务的形式来进行运行，这时候要替换成我们服务的 IP 地址和端口又有点不同。这后面再章节我们再具体介绍这段内容。


改造完以后，其实主要的什么内容都已经改造完毕了。然后我们就可以进行我们的 Maven install 找到我们的这个 auth 这样一个 domain auth domain 然后它的这个 service 的 API 然后在这里我们去运行什么 Maven 的 install 那 install 完了以后，如果是 build 完毕成功的 build 出那个 package 以后，我们就把在我们 target 底下这个价包上传到我们的这个服务器。我这里是提前就是已经上传完毕。在这里名字叫什么叫这个 four D auth service 点价。


那对，这样一个文件，跟刚刚的操作其实是一致的，就是我们要什么开始去写一个 doctor 那这个 Doc 方案之前我们有一个我们可以直接你们采用这种全局替换的方式，把 config server 替换成 foodie auth service 这样一个内容。好，全球替换完以后，大家检查一下是 food or service 杠 1.0 Snapshot 点价，把它安装到容器的同样的同名的这个 route 目录底下，然后运行这个命令 Java 杠架，然后指定我们当前就是主根目录底下这个价包。


好我们来尝试去 build 一下 dockerbuild 取个名字买什么 auth 对吧。我的 auth indication 服务，在当前的目录底下找这个 Docker for 去把它给 build 出来。那因为我们之前那个整个 from Java 这个包是早就是已经是下载过你之前的版本都已经 build 过，所以很快他就会找到当前已经已存在这样一个 Java 的这个 image 然后很快的在上面安装一些这个额外的包。打成一个 image 之后它在启动的时候，它会以 entry 命令指定的形式把我们的 Java 给写起来。那怎么样去启动它就是还是这样， Docker around 要是以 demo 的形式去 run 这些应用。然后我们记得刚刚端口是什么，1003对吧 1003 这个端口。然后我们要把这个端口的应用同时映射到我们的什么我们的这个 10003 这个端口，我看一下是不是 1003 没有记错。好 1006 是吧是 1006 这个端口好映射到我们服务器同名的这个端口。然后我们可以取一个应用的名称就叫 my authentication 然后我们再去指定我们 image 的名称也是 my authentication 这样就 run 起来了，我们 Docker PS 看一下是不是又有一个新的 authentication 运行起来了。一样道理，我们把 user 服务也起来，然后我们再回去重启一下我们的 eureka 好我们切回 user 的，所以关掉 auth 打开 user 那 user 底下还是它的主服在 user web 底下。


然后我们去看一下它下面的话有哪些 resource 那它有一个 boot strap 就是启动时候首先是吧，首先会去寻找这个参数。这里把这个 eureka 原来的这个内容一下，替换成什么 default zone 里面指定我们实际 eureka 的服务器的 IP 地址，也就是我们这个阿里云这台服务器的内网地址，一台端口还不变 2 万。


而 instance 这里我们要指定什么？我们要在有热开注册。我要注册的时候是以什么样形式注册呢？我是以这样一个 IP 地址，就是服务器的内网 IP 地址的什么端口呢？就是刚刚看到那个什么刚刚看到那个 user domain 端口，那个 user domain 端口现在还没看到是吧，其实是我们待会看到以 U 的 domain 这个端口形式来注册。注册完了以后，你就可以在什么 UI card 进行访问了。
到底它的端口是多少呢？我们去 application 这里看能不能看得到？它注掉了，但它告诉我们它是选用 profile dive 所以在这里其实没有特别多实际有效的参数，我们直接看它什么指定的那个 profile dive 里面追加哪些值呢？追加这个值对吧？ 1002 也就是刚刚 bootstrap 这里其实缺的那个值，其实可以就是在这里获得，就是我会在我们的什么整个这个 euroka 服务里面，以这个物理机的 IP 地址和端口 1002 来作为我的什么注册的 URL 这个时候我要访问的数据库本来是这样一段数据库，我把它注释掉了，跟大家也一样。


注释掉以后换一个名称，换什么名称呢？要把这里 IP 地址换成我们当前服务器的 IP 地址，就是内网的地址就可以了。那端口 3306 不变，这里要稍微一个注意，小改动。 MySQL 其实对横杠知识比较差，比较可以支持 schema 是下划线。所以我把横杠统一替换成下划线，其他内容不变，改一下我们的 IP 地址。如果你用 MySQL 建议改成下划线。那同样道理，我们在我们的 SQL 的语句里面建库的时候，我们也不去建横杠那个库，建下划线那个库，密码还是选一个，比如选 IMock 好以这种形式我们联络我们的数据库，然后我们尝试去访问这样一个数据库的这个我们的是个 database 那这个 database 现在还没有，待会我们后一节我们会跑数据库命令。然后 SQL 语句把它给创建出来。在 Redis 访问这里呢也要做一定的修改。


Redis 什么服务器是我们的虚拟机机的内网地址，然后端口也是一样，6379不变 false 注掉。因为 Redis 我们这里其实在起 Redis 容器的时候没有指定过密码，那 zip key 如果有的话做相应的改动 IP 地址端口。那其他的内容还有包含 rabbit MQ 的 IP 地址做个改动。


端口不变， user 和 password 统一用 guest guest 那这样基本上就把我们这里所需要的 bootstrap.yaml application.yaml 和 application dev.yaml 的基本配置都配置好了，我们也检查了一遍，没有什么遗漏。这个时候我们就可以去对我们的这个 user 这个服务尝试进行我们的这个 Maven install 了，找到 user 这个什么 web 这个 service 这个主 service 直接对它进行 install 好。 Maven install 完了以后，我们就可以什么把生成的这个包。那这个包其实就是这里在 target 目录底下的一个什么 food user web 这样一个 step shot 的价包，然后把它复制到我们的这个生产服务器上。那这里其实就是这里 food user web 这样一个包之后是创建 Docker 你可以创建很多个 Docker file 然后在我们的 Docker build 时候指定。那以这里我对偷懒，就是只是生成一个 Docker file 然后快速的替换就不用写多个了。这里面把 auth service 替换成什么？替换成 user user 应该是 web 如果没有记错的话，我们再确认一下。替换成 user web 对没有错。好，然后 user 横杠 web 斜杠七好，这就全局替换完不成了，它就会把我们的当前这个 user web 这个价包放到容器里面同名。然后在启动的时候用 Java 杠架带这个参数来启动。


好。 save 完以后我们就可以用 Docker build 杠 T 取一个我们的这个 tag 我们去问问 my user ，在当前目录找个 dog farm 打包成一个 image 那打包完了以后也一样。 doctor wrong 杠 demo 端口是多少呢？我们再回过去看，自己检查一下它端口号幺零零零二一万零二服务器的 u202 到容器的u202。然后我们要去尝试把它的那个 name 写清楚。那我们 name 就取user ，简单一点好不好就取 name 就叫 my user 好，那刚刚 image 也叫 my user 我们 run 一下。这样的话我们相当于是把这个 U 的这个容器也已经起来了。那这个时候其实有瑞卡里面已经可以看到它，但是会有希望今日你会报一些错建议，我们什么 Docker restart 一下我的什么 my registry 这样一个我的这个服务注册中心，从启下以后，稍等一会，然后我们切回这个有瑞克的界面，我们重刷一下。


那今天还是在重启过程当中，服务还一个都没出来是吧，这也是 no instance available 等一会，出来了一个 config 又出来了一个 authentication 是不是跟刚刚指定的一样，我们强行把什么把它原来这个容器里面那个很奇怪的 host name 转成了一个 IP 地址，而且这个 ID 就是服务器 IP 地址的对应端口，还有一个出 user 没出来，我们等一下。好，又带出来了的 fully user services 也出来了，叫什么？ 1002 是吧？ auth 1006。然后是我们之前的 confuse 是20,003。好那这些应用服务都完了以后，那这一节其实就是告一段落了，大家可以如法炮制把 item cut order 甚至于 search 跟 pay pavement 就是我们的支付平台都以这种容器的形式一个起来，每一个微辅起一个容器。


在当前我们 Docker 这一章节是这样，那后面我们讲什么？我们的这个调度，我们讲这种大的 pass 平台的统一的编排管理的时候，以多容器会以更复杂的形式来运行。好的下一节我们会把前端和后端关联起来，真正打开页面来给大家感受一下实际这个应用跑起来会是什么样的情况。好，敬请期待。


