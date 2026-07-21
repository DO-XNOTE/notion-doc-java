---
title: 2-14 【Docker技术落地实战】部署微服务-2
---

# 2-14 【Docker技术落地实战】部署微服务-2

[image](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/fccea0d2-e5ac-46ac-98e1-c691fc610a2a/SCR-20240725-dgte.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZT5Z32LD%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T225927Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDJfdrwjzfimWtiM4hS1V5%2B%2Fm7ryprFpyFsoWnkFoWLtAIgdYtne2C5LfHBc8U2t2nojW7ADEs0BbGYSMHbXuSZ9P0qiAQIxv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDLxqt7qBDDn4ppjgXircAzcUXsTAd%2FVLNakzkBNP51shFGlFzboMUFhk5z%2BGuzO5FmbGAFgiMCJMVbBm8ldrniPMD5XlQw%2F95TEtooFgOFnYnhPvtRTy0x5fjci1Uuf5gZYv2EnPfBogqEworED6vGlg9jNU%2BNdSpECOVdVQBlKUDQ3%2FrsPo%2BOYWNOlOJb7PfRuWgIx9HI%2BN5NH1V35unpp4QUubmfK5oR89AlU0K2V58Cc4lS9e0x3L3BuIbVn8nMFfTs3Hf%2FqKSC4DEyIoiGasuhMhgAMses4DoWfp2tLRK7WBvz9TxBR6gZ37ay1%2Bs%2BPREdMXAafYEhiQ6bfGuxH7YBd8JPdiosSm7S8jTjyR4i7FbFMfGS2GILAuZQSebdO2RP4BixTSO0I8NYUXrdX5gwBaWHt6kl4JjGil1Ef%2BN%2BnJfa5N55HNg9HfgYvT3Ce4YleEi%2FDVExEtpLRK45UP93prs4MUypEeSVDLVKiImvZxcLVY2zSDj9xknormZyC3wpXsudEIK81PXTAjvRzPmBpJeSoBPKVOLVWj4ohJOAiv72D8deMwfIBzieidtDqjKc1cwPGKTO%2FyYeS6USoAURQxqQMHpicqXwTSQ2sMVxV6XZZJPjBleIokIyc4wwV45Ag%2B7a2QEeFDMPK4%2F9IGOqUBhXe2aZm0JiCROAFKF7QFPkV54WR2Orwr%2B94GO8hO%2FnMu152YBi7jfNE1p3vJZ0pfL3eN2gfp3ha5fFdlhhkKWjdZOAPVbZAB2iyxoPqrki9KcJ59EQgWGgQXJ8z1%2FeebEFaCP%2BA4q419NTCYxXtDatHkJaj2U7Pm6TCRAG6TneKM64fOZ%2FoLz1wGDtMkA2BDsMBC3nD6cL9W19lt5JL9N8lo5LNz&X-Amz-Signature=b7b386d90e2d219d6a1b22e5aaf501688b17adc23cd8350354951b350dd298a7&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

[image](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/e9920524-0403-4c85-a018-1774e2c5685c/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZT5Z32LD%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T225927Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDJfdrwjzfimWtiM4hS1V5%2B%2Fm7ryprFpyFsoWnkFoWLtAIgdYtne2C5LfHBc8U2t2nojW7ADEs0BbGYSMHbXuSZ9P0qiAQIxv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDLxqt7qBDDn4ppjgXircAzcUXsTAd%2FVLNakzkBNP51shFGlFzboMUFhk5z%2BGuzO5FmbGAFgiMCJMVbBm8ldrniPMD5XlQw%2F95TEtooFgOFnYnhPvtRTy0x5fjci1Uuf5gZYv2EnPfBogqEworED6vGlg9jNU%2BNdSpECOVdVQBlKUDQ3%2FrsPo%2BOYWNOlOJb7PfRuWgIx9HI%2BN5NH1V35unpp4QUubmfK5oR89AlU0K2V58Cc4lS9e0x3L3BuIbVn8nMFfTs3Hf%2FqKSC4DEyIoiGasuhMhgAMses4DoWfp2tLRK7WBvz9TxBR6gZ37ay1%2Bs%2BPREdMXAafYEhiQ6bfGuxH7YBd8JPdiosSm7S8jTjyR4i7FbFMfGS2GILAuZQSebdO2RP4BixTSO0I8NYUXrdX5gwBaWHt6kl4JjGil1Ef%2BN%2BnJfa5N55HNg9HfgYvT3Ce4YleEi%2FDVExEtpLRK45UP93prs4MUypEeSVDLVKiImvZxcLVY2zSDj9xknormZyC3wpXsudEIK81PXTAjvRzPmBpJeSoBPKVOLVWj4ohJOAiv72D8deMwfIBzieidtDqjKc1cwPGKTO%2FyYeS6USoAURQxqQMHpicqXwTSQ2sMVxV6XZZJPjBleIokIyc4wwV45Ag%2B7a2QEeFDMPK4%2F9IGOqUBhXe2aZm0JiCROAFKF7QFPkV54WR2Orwr%2B94GO8hO%2FnMu152YBi7jfNE1p3vJZ0pfL3eN2gfp3ha5fFdlhhkKWjdZOAPVbZAB2iyxoPqrki9KcJ59EQgWGgQXJ8z1%2FeebEFaCP%2BA4q419NTCYxXtDatHkJaj2U7Pm6TCRAG6TneKM64fOZ%2FoLz1wGDtMkA2BDsMBC3nD6cL9W19lt5JL9N8lo5LNz&X-Amz-Signature=6e0e67905b9c21c13d6dc3555cafe53a8e9af2933fe018dfc20eeb5525006ab1&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

然后我们要把我们刚刚的上传的这个 registry 应用的 jar 包复制到哪里去呢？就复制到我们服务器的主目录，

[image](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/46d4e174-94f2-4abe-b3a3-5c4b3d0305f2/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZT5Z32LD%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T225927Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDJfdrwjzfimWtiM4hS1V5%2B%2Fm7ryprFpyFsoWnkFoWLtAIgdYtne2C5LfHBc8U2t2nojW7ADEs0BbGYSMHbXuSZ9P0qiAQIxv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDLxqt7qBDDn4ppjgXircAzcUXsTAd%2FVLNakzkBNP51shFGlFzboMUFhk5z%2BGuzO5FmbGAFgiMCJMVbBm8ldrniPMD5XlQw%2F95TEtooFgOFnYnhPvtRTy0x5fjci1Uuf5gZYv2EnPfBogqEworED6vGlg9jNU%2BNdSpECOVdVQBlKUDQ3%2FrsPo%2BOYWNOlOJb7PfRuWgIx9HI%2BN5NH1V35unpp4QUubmfK5oR89AlU0K2V58Cc4lS9e0x3L3BuIbVn8nMFfTs3Hf%2FqKSC4DEyIoiGasuhMhgAMses4DoWfp2tLRK7WBvz9TxBR6gZ37ay1%2Bs%2BPREdMXAafYEhiQ6bfGuxH7YBd8JPdiosSm7S8jTjyR4i7FbFMfGS2GILAuZQSebdO2RP4BixTSO0I8NYUXrdX5gwBaWHt6kl4JjGil1Ef%2BN%2BnJfa5N55HNg9HfgYvT3Ce4YleEi%2FDVExEtpLRK45UP93prs4MUypEeSVDLVKiImvZxcLVY2zSDj9xknormZyC3wpXsudEIK81PXTAjvRzPmBpJeSoBPKVOLVWj4ohJOAiv72D8deMwfIBzieidtDqjKc1cwPGKTO%2FyYeS6USoAURQxqQMHpicqXwTSQ2sMVxV6XZZJPjBleIokIyc4wwV45Ag%2B7a2QEeFDMPK4%2F9IGOqUBhXe2aZm0JiCROAFKF7QFPkV54WR2Orwr%2B94GO8hO%2FnMu152YBi7jfNE1p3vJZ0pfL3eN2gfp3ha5fFdlhhkKWjdZOAPVbZAB2iyxoPqrki9KcJ59EQgWGgQXJ8z1%2FeebEFaCP%2BA4q419NTCYxXtDatHkJaj2U7Pm6TCRAG6TneKM64fOZ%2FoLz1wGDtMkA2BDsMBC3nD6cL9W19lt5JL9N8lo5LNz&X-Amz-Signature=cd6e31a1e3f138514a6ec43d563f027aa99ca1e8042e6cf5d2cc20abd54c8f12&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

通常它的目录应该就是如此目录 follow 它的什么 root 目录是底下同名也不用换名字。那这个时候它们它的编译成我们 image 的时候或者说是打包成 image 的时候已经会完成。然后在启动的时候我们可以指定一个 entry point 大家应该通过前面的学习已经了解了 entry point 是否是启动时候的一个在容器里面的一个运行命令。那通常是用说方括号，然后传一堆的参数。首先要传的命令主命令名 Java 然后我们可以传一个叫做杠加这样一个参数，然后再传一个具体的这个参数的值。那这个值其实就是刚刚我们的文件的名字，然后把这些东西全部作为参数。传完以后，基本上我们的这个 Docker file 已经完成了，那我们保存一下。

[image](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/e986bb5a-cab6-45a1-9ffc-c6d73ec5d2a3/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZT5Z32LD%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T225927Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDJfdrwjzfimWtiM4hS1V5%2B%2Fm7ryprFpyFsoWnkFoWLtAIgdYtne2C5LfHBc8U2t2nojW7ADEs0BbGYSMHbXuSZ9P0qiAQIxv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDLxqt7qBDDn4ppjgXircAzcUXsTAd%2FVLNakzkBNP51shFGlFzboMUFhk5z%2BGuzO5FmbGAFgiMCJMVbBm8ldrniPMD5XlQw%2F95TEtooFgOFnYnhPvtRTy0x5fjci1Uuf5gZYv2EnPfBogqEworED6vGlg9jNU%2BNdSpECOVdVQBlKUDQ3%2FrsPo%2BOYWNOlOJb7PfRuWgIx9HI%2BN5NH1V35unpp4QUubmfK5oR89AlU0K2V58Cc4lS9e0x3L3BuIbVn8nMFfTs3Hf%2FqKSC4DEyIoiGasuhMhgAMses4DoWfp2tLRK7WBvz9TxBR6gZ37ay1%2Bs%2BPREdMXAafYEhiQ6bfGuxH7YBd8JPdiosSm7S8jTjyR4i7FbFMfGS2GILAuZQSebdO2RP4BixTSO0I8NYUXrdX5gwBaWHt6kl4JjGil1Ef%2BN%2BnJfa5N55HNg9HfgYvT3Ce4YleEi%2FDVExEtpLRK45UP93prs4MUypEeSVDLVKiImvZxcLVY2zSDj9xknormZyC3wpXsudEIK81PXTAjvRzPmBpJeSoBPKVOLVWj4ohJOAiv72D8deMwfIBzieidtDqjKc1cwPGKTO%2FyYeS6USoAURQxqQMHpicqXwTSQ2sMVxV6XZZJPjBleIokIyc4wwV45Ag%2B7a2QEeFDMPK4%2F9IGOqUBhXe2aZm0JiCROAFKF7QFPkV54WR2Orwr%2B94GO8hO%2FnMu152YBi7jfNE1p3vJZ0pfL3eN2gfp3ha5fFdlhhkKWjdZOAPVbZAB2iyxoPqrki9KcJ59EQgWGgQXJ8z1%2FeebEFaCP%2BA4q419NTCYxXtDatHkJaj2U7Pm6TCRAG6TneKM64fOZ%2FoLz1wGDtMkA2BDsMBC3nD6cL9W19lt5JL9N8lo5LNz&X-Amz-Signature=6cf6f83e44f4ca0f9df0ac83ca94ddda4f4e248fdcb702726462498058a12a70&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

好在这种全部 Docker file 完成以后，我们直接起个叫 Docker build 我们要起一个什么，我们域名就是名字，那我们这个名字叫 my 好了， my registry ，我的这个注册中心点就表示在当前环境，我去找我的 Docker 按照刀开发指定的形式进行 build 我们看一下能不能很方便的 build 出来，有没有什么语法错，他可以说好像有一个语法错，你用 build 那个 build 打错了，我们再跑一下，它已经在 build 了，它 build 过程是先从我们的公网上或者我们指向的那个 registry 里面去下载什么 Java 这样一个基本的镜像。那我这里其实已经是下载过的，所以下载完了以后，他很快的就能把我的这个价包塞到那个镜像里。然后把我的 command line 那个命令告知这个整个这个 image 当他 image 起的时候，他会知道要跑 Java 杠架，然后跑具体价包，这样我们整个包打完以后，这个什么 image 已经有了，比如用 Docker images 可以看到。


那我因为我这里有蛮多的那个 images 我可以直接看一下我们的 my registry 看得更详细的对不对？这样一个 my registry 已经有了，如果大家没有很多 images 直接用 Docker 空格 images 可以查看所有的我们 image 已经有了这个 image 以后，我们可以开始尝试去启动它了。


大家还记得吗？启动的时候要用什么端口啊？刚刚我们写的那个端口就是 2 万对吧，我们要把 2 万映射到服务器。那我建议就是服务器端口和容器端口一样，后面大家记忆。所以我们就选了 Docker wrong 杠 P2 万对 2 万服务器的 2 万对容器的我们应用服务的这个绑定的 2 万端口。然后我们容器名取一个也叫 my registry 就是 image 名和我们的容器名相同。然后我们再说一遍我们刚刚打过 image 的名称。好，你这个容器就尝试起来了。好，我刚刚所说了个 demo 所以它不是以这个 demo 形式，它是以这个前端形式起的。那我把它停掉，因为已经生成果了，我们要 Docker IM 这个 my registry 好，删除掉以后我们重新再加一个杠 D 就漏掉了一个杠D ，它就不是在一个后台形式，它占住了我们的主窗口，一个 demo 的形式，以端口 2 万对 2 万起来了。


我们可以看一下 Docker PS 里面又多了一个容器对吧，多了一个 my registry 就是名字在这里，那它的 image 恰好也叫这个名字。那同样的道理，我们要去起什么其他的服务？那我这里会去起一个叫 config 的服务。我们先看一下 config 代码。 my config 对吧，说我的那个 config server 这个代码是在这里，然后我们重点去看它几个 resources 那大家知道在应用启动的时候，先去会检查什么 board strap 对吧，这个羊毛文件看看要传一些参数。那之后会用新的这个 application 的羊毛文件的参数进行一部分的覆盖和追加。那这里会追加出什么启动端口？比如说我应用的绑定端口是 20,003 这个端口。


然后我的整个应用的服务，如果你是直接从我们的什么上一节课的代码，就是微服务改造的代码下载下来，那这里可能叫 local host 或者其他名字，那我这里已经改成了我们的内网地址，那这个内网地址就是我刚刚租赁的那台服务器插的什么？它上面写着的下面这个私有地址，内网地址，所有的应用之间的沟通都用内网地址，这样就不用经过阿里的那个 MIT 是转换了，速度会更快。所有的外部用户访问，比如笔记本用户访问都用他的公网地址，那这样才能保证我们真正能访问到这台服务器。
好，那这里就是我们应用之间调用采用内网地址。然后端口就是之前启动的时候容器里面选了个 


5672 用户密码，因为我们之前当时在启这个 rapid MQ 时候没选，所以默认是guest。 Guest. 那我们这里也一样。那如果大家在生产上是需要做改动的，那除此以外还有一些什么其他的参数？重点看这一段，这段是我改变过的，特别是这一段，这是我最佳的默认情况下，default zone 它本来写的可能是 local host 我们首先要知道我的 URI 卡刚刚起的那个服务器是一个容器，那这个容器会以这个 bridge 的形式映射到我们的私网地址和公网地址上。因为内部通讯我选用私网地址就是服务器的私网地址，然后映射端口是 2 万。如果大家对这还有疑问，可以回去看我们的网络章节，特别是 bridge 映射过来以后，这就是什么我们有瑞卡起的容器的实际的访问地址。


我的那个 config server 要注册到 ureka 里面。那我 config server 以什么样的形式来注册呢？那默认其实是一个 host name 的形式来注册的。那我这里希望不要是以 host name 而是以什么我 prefer IP 地址待会可以登录给大家看一下。有热课你们可以看一下。


我以 IP 地址注册完以后，整个这个最 endpoint 的显示，它除了一个大写的名字什么 config server 这样一个名字，具体它的这个什么实际的 endpoint 会以 IP 地址来显示。这个 IP 地址不是默认的容器的 IP 地址，容器会起一个它自己内部的自有的 IP 地址。那这个 IP 地址是什么外网不能访问的，所以我们要什么我们要给它指定服饰地址端口还是容器的端口，因为我们刚刚会把 2 万容器端口映射到服务器还是 2 万？对通过这样一段内容，这段内容时候大家追加的就是我希望我是以 IP 地址的形式在 URI 卡里面进行互通。那有瑞卡的时候，我用服务器的就是我用我的容器的默认端口，但是我的 IP 地址替换成下面的这个 18317 二零幺九点四二零幺八三的服务器的内网地址。


这样的配置完以后，基本上我们主要的这个 config server 的配置就已经完成了。那这个时候我们可以尝试去重新 build 一下。那在这个 build 这个 image 之前，我们首先要在我们的这个 config server 里面，那么用 main install 的方式重新去 run 一下，我们找一下会比较多。这里其实我刚刚已经跑过了对吧，没用 install 的形式把那个 config 给跑一下，因为 registry 其实是不需要额外的改动的。那 config 改完以后我们就应该在这里跑一下。


那跑完以后，我们把这个生成的这个就刚刚看到这种生成的这个价包，我这里其实都提前上传好了，上传到服务器，那这里上传完以后会成为这样一个 config 的这个价包。然后你就可以对这个 config 的价包做一样的处理。我们去写一个 Docker file 然后让生成我们对应的 package 然后生成我们这个镜像叫 image 那再用这个 image 去起一个容器，我们直接就修改我们的这个什么 registration center 把它改成我们的 config 就好了。大家再看一下名字名字就叫 config server 是吧。那这里我跟大家讲一个这个最常见的这个我们 VI 里面那个替换方法，冒号百分号 S 斜杠，你要把 Excel center 这样的东西替换成什么 config server 斜杠机 global 就是我能命中多少行，我就把每一行里面所有的这个 register center 都用什么 config seal 来进行替换，百分 S 级表示替换好回车。


你看到什么？这里 config seal ，这里替换掉，下面也替换掉，就是我要把我这个 config seal 的价包上传到我容器里面透明。同时我在启动容器的时候，我会以 Java 加的形式把这个架栏运行起来。好我们保存一下。那保存完了以后我们就可以用 Docker build 然后我们取个名字这个 image 取出 my config 然后点当前的 doctor fire 去找，然后进行 build 好。变完以后我们就可以跟刚刚一样，也是用刚刚类似的命令去起一个这个容器。但是这次我们端口有点不同了，那 config 的端口，其实我们回过头来再看一下，刚刚这里应该是已经有一个端口号了，叫什么20,003，我们这里就是一样的道理。我们会起的容器是其他的 20,003 端口。同时我也绑定服务器的也是 20,003 端口。然后名字不管是容器名还是我们 config 名都做一个替换。 my config 这是我们的容器名。那这里是 image 名字，就是把刚刚创建的 my config 这个 image 给创建起来。好我们再用 Doc PS 看一下，这不是有一个最新的名字叫 my config 的容器已经起来了，这时候我们再回过头去看 registry 应该能看到这个容器。


我们在图形化界面里采用公网 IP 对吧？它所谓的绑定，就是在服务器上绑定的端，可能都是既绑定公网 IP 也绑定私网 IP 因为公网 IP 其实是一个地址映射，有没有访问这个容器，就访问他官网 IP 访问端口，就是去访问 urea 打开 urea 以后他说什么？好像这个有些服务还不是完全的 ready 这里有两个方案，一个是等足够长的时间逐步会好。


还有方案比较简单，就是也是我通常推荐的，你先什么 stop 一下我的 register 就是我把我的这个 ereca 停一下，然后再起一下，或者你直接起 restart 也是一样。就是这样你可以 stop start 也可以 restart 都可以 view restart 就是这都是一样的，效果都是一样的，就是等一会。然后当它重新起来以后，它会重新再去刷新一下，跟它所有的这些服务，发现服务注册这个服务。然后这个页面我们再刷新一下，等一会应该就会出来，就会比较干净，就会没有刚刚的 error 了。同时还告诉你说 config server 就是我刚刚最新的一个应用。对这个应用它不会写一个 host name 这里会有什么具体的 IP 地址，因为我 prefer IP 同时我把我的 IP 地址是我人工注入的，否则它会把容器里面那个 IP 地址注在这里。


那给大家看一下容器里面 IP 地址到底是多少呢？我们可以用 Docker exact 是吧杠 it 然后可以取 ID 也可以取长 ID 我们这里因为有 container name 所以用 container name 相对是更简单一些。比如 my config 这是我的这个服务。然后我用 bin bash 如果它已经装了 bin bash 的话，就可以用这个 bin bash 命令去登录。它登录完了以后，你可以用 if config 来看，或者有 IP 这种命令来看。
IP 杠 a IP address 是吧这样的命令。来看看我的这个端口，它叫 ETH 0 这样一个 IP 的接口 


interface 那它的地址是幺七二点幺七点零点六是不是个内网地址对吧？那这个内网地址其实是不可达的，即使我们公网不可达成，我们容器和容器之间也是不能用这个地址来访问的。所以必须什么一定要在我们的这个整个这个过程当中，一定要把每一处 application 点压和 push strap 点压。
仔细看，一旦是有跟有瑞卡注册的时候，一定要把当前我们这个应用注册成一个服务器的 IP 地址，那这个 IP 地址才是可查的，通过 bridge 的方式进行端口映射，然后它这个端口还是可以沿用之前的，应用的这个端口 2003 是可以用的，没有问题。


有这样一个服务器的 IP 地址的端口映射以后，你才能真正的注册到有瑞卡，成为一个可访问可以被其他应用访问的这样一个服务。那这里 config server 就成功的注册到了 UI 卡。好，那这一节先告一段落，我们下一节具体来看我们怎么样把真正的应用注册到我们的整个环境当中，谢谢大家。


