---
title: 1-26 【K8S技术落地实战】部署微服务-4
---

# 1-26 【K8S技术落地实战】部署微服务-4

[image](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/94f5cac6-4819-4c74-a9ae-1ffc84466e78/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RPNQGPN5%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T225950Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIC6HN90XNMVJeBYmHG60fauzQZqhFSxB55lh7d8o1%2FbiAiEAhN4g0mCFQfcEwg0DRqFrbsApOTOv7c8w3bLJPTp4rHsqiAQIxv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDL41T51kv6sh1mPRgyrcA08o3og00FbvVLMrzFjNKZeZnZ%2FGVx%2Bk8sW2GAP4kRqPZg8WmJHjVlEje6v7y4TiJxaaa9CdkNxvzNTlOy%2FaRrCVNQMrZD117asgNb337TDehDyn6mHddLvjWGgXWZ98%2BJmQQ0PFPxJ0Q8sLnHRZxU9qgCTSNCeKPUT5IjFvbODKlTkxDO8kF6l7HogizUJmJvGzh33ZkA%2FLxldWibS90PZdntjUFgbLiHteqv7jDPV%2FRHvWSuTLPWzQho8MQPgNnjQnjRRX1gXd0446TQruk2cejFFREW0tvNFarUcExs1VKzAy6rnBpNRPZpY7ebRS%2Fua39TmUWG0r23Yl6toJaepX1EpPDOh8ozb9yhJP3qyFQHWfbTEBoJ7BaiGG2XFj364Y8SLwzYTh%2BPpUTO%2By9GImDOnD6XJBZ3M59ob7qXBlZ7yIAkLmPGbpUrNKAQeEQdxDZLpHhE%2F8YjHEPKn8kt%2FBowPL0SPTMHF1LK4mlOexq0gmiMM%2FQ86YImcDuKRYmxpeT%2FFm6VnbBAUmOyVoJpviX3NJA6sQHrU3d3LipkENXWvnfVvv8dVI%2FC1P36lfYY3CVkoZk%2Bjq5CCZDBhOxO6G1L%2BkWQH0mPhNoevpGMCGpSOCTfd%2Bvvbw%2B%2FvFMIe4%2F9IGOqUBEZIo9ZzOROxcLSYTlOIcdDFvwiCFsizxvuKU%2Fq0zw3iYw24THduJC7ba8buc2eKDHVJB8nyLq9ZvfSYcRzPlQOgd7boXrR06KIaH9EbJZ2C3ZQ2W%2FRs8sCjWaclVZ7MBAyPPE%2FXYHdlpag8oCMW8Kfe6bRlN2BY2n5W5jiCvWYNOwRDpIPLPnD09%2FneBrKRfRVaHRMZ1w3%2FrPlFaUvB0Qn3IpGUb&X-Amz-Signature=dd1f4a53926a666f3aa7d0e8b79ee8d9b73fddcbce37c884d4d7fa0629673240&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

[image](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/9accbb8a-c9fb-4c54-96ed-3e64b6b9f402/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RPNQGPN5%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T225950Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIC6HN90XNMVJeBYmHG60fauzQZqhFSxB55lh7d8o1%2FbiAiEAhN4g0mCFQfcEwg0DRqFrbsApOTOv7c8w3bLJPTp4rHsqiAQIxv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDL41T51kv6sh1mPRgyrcA08o3og00FbvVLMrzFjNKZeZnZ%2FGVx%2Bk8sW2GAP4kRqPZg8WmJHjVlEje6v7y4TiJxaaa9CdkNxvzNTlOy%2FaRrCVNQMrZD117asgNb337TDehDyn6mHddLvjWGgXWZ98%2BJmQQ0PFPxJ0Q8sLnHRZxU9qgCTSNCeKPUT5IjFvbODKlTkxDO8kF6l7HogizUJmJvGzh33ZkA%2FLxldWibS90PZdntjUFgbLiHteqv7jDPV%2FRHvWSuTLPWzQho8MQPgNnjQnjRRX1gXd0446TQruk2cejFFREW0tvNFarUcExs1VKzAy6rnBpNRPZpY7ebRS%2Fua39TmUWG0r23Yl6toJaepX1EpPDOh8ozb9yhJP3qyFQHWfbTEBoJ7BaiGG2XFj364Y8SLwzYTh%2BPpUTO%2By9GImDOnD6XJBZ3M59ob7qXBlZ7yIAkLmPGbpUrNKAQeEQdxDZLpHhE%2F8YjHEPKn8kt%2FBowPL0SPTMHF1LK4mlOexq0gmiMM%2FQ86YImcDuKRYmxpeT%2FFm6VnbBAUmOyVoJpviX3NJA6sQHrU3d3LipkENXWvnfVvv8dVI%2FC1P36lfYY3CVkoZk%2Bjq5CCZDBhOxO6G1L%2BkWQH0mPhNoevpGMCGpSOCTfd%2Bvvbw%2B%2FvFMIe4%2F9IGOqUBEZIo9ZzOROxcLSYTlOIcdDFvwiCFsizxvuKU%2Fq0zw3iYw24THduJC7ba8buc2eKDHVJB8nyLq9ZvfSYcRzPlQOgd7boXrR06KIaH9EbJZ2C3ZQ2W%2FRs8sCjWaclVZ7MBAyPPE%2FXYHdlpag8oCMW8Kfe6bRlN2BY2n5W5jiCvWYNOwRDpIPLPnD09%2FneBrKRfRVaHRMZ1w3%2FrPlFaUvB0Qn3IpGUb&X-Amz-Signature=bacd85ccecb1bf261b86e2e55ea9e60f12def2ffbaaef30dfcee969ab26fefe8&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

好，喝了两口水休息一下以后，我们回过来继续我们的库伯内蒂斯部署。刚刚，其实已经是把什么把我们这些无状态的所有应用的价包都准备完成，包括友瑞卡也已经准备完毕。那同时我们把 rapid MQ 已经以一个什么容器加服务的形式给起来了。那另外，像 mycq 对吧， Redis 都在外网准备好了， github 也是指向原有的那个 github 服务器，这些全部做完以后，就是要开始什么制作镜像，上传镜像，最后开始部署了。


那在制作镜像那里，刚刚我故意把它停了一下，那河南我们来看一下，如果我们要制作镜像，那我们首先要什么知道我们会从哪里去使用这个镜像？那还是回到阿里云的界面，在容器服务这里，我们要往下去看。在这里我很下面有个市场，这里有个什么有个镜像，我们看一下，

[image](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/10665fe8-efb4-46ea-ad76-8ae553c67b36/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RPNQGPN5%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T225950Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIC6HN90XNMVJeBYmHG60fauzQZqhFSxB55lh7d8o1%2FbiAiEAhN4g0mCFQfcEwg0DRqFrbsApOTOv7c8w3bLJPTp4rHsqiAQIxv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDL41T51kv6sh1mPRgyrcA08o3og00FbvVLMrzFjNKZeZnZ%2FGVx%2Bk8sW2GAP4kRqPZg8WmJHjVlEje6v7y4TiJxaaa9CdkNxvzNTlOy%2FaRrCVNQMrZD117asgNb337TDehDyn6mHddLvjWGgXWZ98%2BJmQQ0PFPxJ0Q8sLnHRZxU9qgCTSNCeKPUT5IjFvbODKlTkxDO8kF6l7HogizUJmJvGzh33ZkA%2FLxldWibS90PZdntjUFgbLiHteqv7jDPV%2FRHvWSuTLPWzQho8MQPgNnjQnjRRX1gXd0446TQruk2cejFFREW0tvNFarUcExs1VKzAy6rnBpNRPZpY7ebRS%2Fua39TmUWG0r23Yl6toJaepX1EpPDOh8ozb9yhJP3qyFQHWfbTEBoJ7BaiGG2XFj364Y8SLwzYTh%2BPpUTO%2By9GImDOnD6XJBZ3M59ob7qXBlZ7yIAkLmPGbpUrNKAQeEQdxDZLpHhE%2F8YjHEPKn8kt%2FBowPL0SPTMHF1LK4mlOexq0gmiMM%2FQ86YImcDuKRYmxpeT%2FFm6VnbBAUmOyVoJpviX3NJA6sQHrU3d3LipkENXWvnfVvv8dVI%2FC1P36lfYY3CVkoZk%2Bjq5CCZDBhOxO6G1L%2BkWQH0mPhNoevpGMCGpSOCTfd%2Bvvbw%2B%2FvFMIe4%2F9IGOqUBEZIo9ZzOROxcLSYTlOIcdDFvwiCFsizxvuKU%2Fq0zw3iYw24THduJC7ba8buc2eKDHVJB8nyLq9ZvfSYcRzPlQOgd7boXrR06KIaH9EbJZ2C3ZQ2W%2FRs8sCjWaclVZ7MBAyPPE%2FXYHdlpag8oCMW8Kfe6bRlN2BY2n5W5jiCvWYNOwRDpIPLPnD09%2FneBrKRfRVaHRMZ1w3%2FrPlFaUvB0Qn3IpGUb&X-Amz-Signature=12d814df6dae861872961adb4efa9f70fb5df2aed6aa0bf17185a029300a6639&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

这里面有支持哪些镜像？有我自己已经准备好了镜像，你也可以用其他镜像，然后在右上角有个什么就溶质镜像服务控制台，这才是镜像管理的。阿里的就是在镜像服务。在这里正常我们放大骑手，不是创造仓库，而是创造一个 registry 我这里已经庆了一个叫飞扬的 registry 那其实大家正常应该是点这个创建，然后起一个名称，然后点个确定。就像我这样就很方便的创建了一个，同时把这个打开，要是允许自动创建仓库，什么叫仓库呢？其实就是某一个镜像具体的名称，也就是说我们允许用什么用我们的这个 


Docker push 的方式，很方便的往你的这个命名空间里面去 push 同时我把这个仓库变成什么一个公开的或私有的，可以自己随便选择。选择完了以后还可以做一定的授权。如果大家是这个测试，就锁定公开，开启完全没有关系，因为没有什么业务代码对吧，然后再往它上面不停地进行上传。
那具体怎么上传呢？大家在上传第一个之前有可能不知道怎么上传，这个时候你就可以点一个这个信息键，或者你可以人工的随便来一个什么创建镜像仓库，点一个这个，然后随便瞎填一段信息。那不管你填的是什么，最后它都会指引你到这个地方来。就是你创建完了这个仓库，你点进去它会告诉你怎么进行上传，要这样的处理方式。


我的阿里云账号是这个叫 triple 章。好使用方法就是你要用速度 Docker login 的方式在这里注册一下，你就在你的这个服务器，比如在我的这个我的这台服务器就曾经跑过这个命令。我给大家看一下，我的 history history 我跑过一个叫 dog lot 你可能在哪？对不对？我就跑过一个这样的命令是吧，把我的什么我的 user name 然后 registry 的这个地址指过，然后他会说让我输入密码，这个时候我输入一串密码，这时候就 log in 成功了，劳给你成功以后，这个密码是阿里云的注册密码，就是你在阿里云上注册用户，你的用户名是什么，就在这里填什么密码就是什么。然后你就可以从上面去拉，也可以向上推。

[image](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/e011332f-3e0b-4418-b4f1-83ad7561328d/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RPNQGPN5%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T225950Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIC6HN90XNMVJeBYmHG60fauzQZqhFSxB55lh7d8o1%2FbiAiEAhN4g0mCFQfcEwg0DRqFrbsApOTOv7c8w3bLJPTp4rHsqiAQIxv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDL41T51kv6sh1mPRgyrcA08o3og00FbvVLMrzFjNKZeZnZ%2FGVx%2Bk8sW2GAP4kRqPZg8WmJHjVlEje6v7y4TiJxaaa9CdkNxvzNTlOy%2FaRrCVNQMrZD117asgNb337TDehDyn6mHddLvjWGgXWZ98%2BJmQQ0PFPxJ0Q8sLnHRZxU9qgCTSNCeKPUT5IjFvbODKlTkxDO8kF6l7HogizUJmJvGzh33ZkA%2FLxldWibS90PZdntjUFgbLiHteqv7jDPV%2FRHvWSuTLPWzQho8MQPgNnjQnjRRX1gXd0446TQruk2cejFFREW0tvNFarUcExs1VKzAy6rnBpNRPZpY7ebRS%2Fua39TmUWG0r23Yl6toJaepX1EpPDOh8ozb9yhJP3qyFQHWfbTEBoJ7BaiGG2XFj364Y8SLwzYTh%2BPpUTO%2By9GImDOnD6XJBZ3M59ob7qXBlZ7yIAkLmPGbpUrNKAQeEQdxDZLpHhE%2F8YjHEPKn8kt%2FBowPL0SPTMHF1LK4mlOexq0gmiMM%2FQ86YImcDuKRYmxpeT%2FFm6VnbBAUmOyVoJpviX3NJA6sQHrU3d3LipkENXWvnfVvv8dVI%2FC1P36lfYY3CVkoZk%2Bjq5CCZDBhOxO6G1L%2BkWQH0mPhNoevpGMCGpSOCTfd%2Bvvbw%2B%2FvFMIe4%2F9IGOqUBEZIo9ZzOROxcLSYTlOIcdDFvwiCFsizxvuKU%2Fq0zw3iYw24THduJC7ba8buc2eKDHVJB8nyLq9ZvfSYcRzPlQOgd7boXrR06KIaH9EbJZ2C3ZQ2W%2FRs8sCjWaclVZ7MBAyPPE%2FXYHdlpag8oCMW8Kfe6bRlN2BY2n5W5jiCvWYNOwRDpIPLPnD09%2FneBrKRfRVaHRMZ1w3%2FrPlFaUvB0Qn3IpGUb&X-Amz-Signature=5a128d316f51332aa66bd0381929a085d551835f4dda21d6c217281b1d05b4c6&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

那我们这里其实不需要拉对不对？我们需要推，他就会告诉你推之前请做这个事情，打一个 tag 把你自己的那个 image 我们刚刚叫什么叫 my user 对吧？转成 [registry.cn](http://registry.cn/) 杠上海点阿里云点 com 为什么会上海？因为我刚刚选那个 registry 我自己选那个 name space 时候我选了上海，大家如果随便选，比如选下去，反正选完以后你就会有一个专门的这个相对 registry 就那个名称。


然后底下这个什么飞扬是 register 真正的这个就我们自己的一个类似于仓库名，类似于是什么叫仓库的管理的这个环境的名称。具体这个仓库就是 my auth 是吧，然后加一个版本号，我这里都喜欢用1.0。好我们看一下我们怎么 tag tag 完了以后把它 push 一把就可以上传了，也就完全可以参照阿里云的方式。任何的这个公有云的这个仓库，或者说是镜像的这个服务中心，都会提供你一个它的 URL 它也会告诉你所在的这个分支的名称，然后你就把你的 URL 跟分支名称弄好以后，后面都是一样的。


好，我们来看一下。回到命令行，我们已经其实之前跑过一个类似的命令了，查 tag 再查一下 U 的。我们居然没有 tag user 的命令吗？那我们就来人工来一个。好不好？我知道了，我登错机器了。好，真的是这台机器。对了。好，我们看一下我们有没有什么 Docker 一下，我们直接看我们 Doc images ，看一下有没有一个叫 my user 的 Doc image 是不是已经有了。 my user 其实我之前已经创建过一个叫什么叫做这个 tag 的名称。然后我们如法炮制，我们看一下，完全走完，我们刚刚是不是 build 了一个 my user 好，下一步是 Docker tag tag 就打个标签，把我们的马优的这个 image 打成什么呢？打成刚刚说的registry ，我记不住可以借鉴一下上面的内容。


CN 到上海是吧，是不是上海点阿里云 [cs.com](http://cs.com/) 下面的飞扬这个 registration 名以下具体的这个 representation 叫 my user 然后我它给名叫1.0。好不好？我先打成这个名称，然后就可以用 doctor push 上传，以本地的这个名称。上传的时候它就会上传的时候它就会自动去找一个同名的这个 URL 的服务器的同样的路径名就叫飞扬，然后 my user 然后它的那个 tag 就是1.0。所以我们就是这样完全把刚刚那段内容复制一下。然后我们在这里选择黏贴，我们就往爱旅游上重新上传一份。


这个很快为什么？很快？因为我上次强过了，它有一个这个 digest 对吧？有一个这个校验说，你跟上次传的一模一样，很快。那如果是自己传的特别第一次，第一个镜像，在第一个镜像里面，它会有一个层叫做 Java 层，那可是个几百兆的内容，所以它传得非常非常慢，10分钟 5 分钟都有可能 15 分钟都有可能。在第一个 Email 传完以后，后面每个 Email 就会快点两三分钟三四分钟。那只有完全一样，就是你一个字都不改的时候。这种情况下它每一层都没有变对吧，她要重新去看 Doc 1 米9，那一层就知道一层接一层，一层接一层，你每层都不变它所以它只是上传一个什么类似于一个这种校验池，我发现完全不变就结束了。很快传完以后再回到界面上来看。在这里，你重新去回到这个什么整个这个什么命名空间底下，也就是那个 registry 底下，你会看到有什么有 my user 所有这些都是我提前已经花了大概有快一个小时，把它一个一个的镜像制作好， tag 好，上传好，全部都准备完毕了，都叫1.0。好吧，都是这样。然后这一片所以所有的 Email 都完成了所有这些操作是不是有点烦？对，感觉烦就对了。


如果大家是经常要制作镜像，或者是说我们企业规则是这样，代码发布，以价包发布不行，必须要以镜像发布。那很多用户会在这个比如说 intelligent 或者 eclipse 会在这里装插件，装一个 plugin 在什么 preference 里面，你们去找找看能不能找到一个插件，这个插件把它相关的内容给装好，装好以后的或者 settings 或者 preference 里面去找装个插件。同时你要求你在电脑肯定要把 Docker 装好了，因为插件是要调后台的 Docker 然后什么制作 Doc image 就这个时候你编的时候你的这个 pom 文件也会有略有不同，你照你的所在的 IDE 工具以及插件的说明来改。改完以后，它会根据你配置的一个 Doc file 文件，把你的价包按照 Doc file 打成一个镜像。然后同时它会让你指定一个叫 register 的 URL 如果你要指定，你就请指定这里这边点开名称，请指定这里你就要选这个 URL 一直到下面这个最后那个应秘诀的名称之前，我请把它输在你的 ID 这里，然后你就可以变成一个什么。我只要代码写完以后，点一个什么 Maven install 这个时候它会触发一个打灯架包，然后用 doctor far 生成一个 dog image 上传到我们的这个镜像服务器。


如果你选阿里云，就是阿里云容器镜像这里这全过程是完全透明好，全部弄完以后，你再回到我们什么阿里云这里，再去点所在区域的时候，因为你的用户名和飞扬的那个 register 用户名是同一个，你可以看到自己上传的所有 image 都在这里了，所以我的内容都已经准备完成，我们用了最原始的方法人工打造 image 人工上传，你也可以用 IDE 的方法来节省这部分时间。


image 完成以后，我们就开始真正的制作应用了，点回来应用无状态大片的无状态应用逐一开始。借两种方法，之前我们是选的什么制作镜像，我给大家看一看另外一个好玩的方法，景点模板创建。这是什么内容，这不就是我们的什么 YAML 范。所以我们刚刚的代码里面，我们如也可以人工去写一些什么。我们的这个 deployment YAML 是吧，先写一段 deployment 的羊毛，再写一段底下的这个什么。 service 的羊毛。 service 羊毛在另外一边。写完以后，你可以在这里点一个什么添加部署或者把什么调出原有模板或者说保存新建模板等方式来进行部署。


那我这边会推荐什么推荐？既然你已经用了图形化界面，证明你其实是一个很感性的人，而不是很理性的人，不是很喜欢自动化的人，请就不要那么繁琐了。就这你喜欢自动化的，那请用 kubernetes 命令或者用 CICD 工具。然后传输 YAML 文件来进行快速自动化部署。


好，我们这里就是一个很感性的很喜欢用图形化界面的这个用户的情况形式。点一个创建镜像，我们逐一完成了，前面 rabbit MQ 完成了。那现在我们来搞一个有瑞卡，叫 my registry 应用名。好副本我们之前说过了， rabbit MQ都只起一个好也叫 default 因为只有在同一个命名空间里面才能互相沟通对吧，无状态也不用打什么标签，它会自动帮我加一些最基本的标签了，请点下一步。


下一步，这里找镜像。好，我们来找找镜像。在这个容器镜像服务这里，华东是不是就能找到我们自己的镜像 my register tree 请出来，在这里双击它。然后版本 1.0 刚刚我们上传的时候是不是选1.0？ user 是1.0， Redis 其实也是1.0，不用选，总是拉取，反正就拉取一次就够了。 CPU 内存就默认 0.255 百一十二兆，反正我们配置比较低了，其他那些其实都不那么关键，都忽略先点下一步。


好，这里有个关键点，service不要忘了，因为什么前面说过 my registry 要建立 service 而且它的名字叫 my registry 杠 service 一点。是不是名称就跟刚刚我们一样。对，通常就是这样，通常一个应用名就叫应用名。然后后面如果你就上面绑服务都会写杠 SVC 这是一个最常见的部署方式。所以阿里云就帮你推荐这样。


对，我们代码里继承这个风格，这里选什么？选虚拟集群就是 class IP 可不可以可以内部沟通，也不需要出去。好端口呢，我们先取名字吧，这个名字其实也用不到。那无所谓写不写怎么取，都所谓我的习惯就是取同名，跟应用取同名也不用取 service 名。然后这里要记住两万对不对？ TCP 2 万端口好的请创建 service 创建准备完成，点最后的总的创建两个一起建 service 跟 deployment 都建完了，回来看应用，我们回来看那个应用有没有跑起来，怎么样呢？先去看 POD 点进去对吧。


POD 里面是容器好，容器直接看容器的 log 然后自动刷新老 party 的 eureka 好了， eureka 起来了，起的是什么呢？你知道吗？我们回来看服务好不好？服务有人看起的是一个什么，我起的是一个叫做这个 my register SVC 幺七二点二幺点零点七六就是有点尴尬。因为我们选的什么是 class 的 IP 所以你要再起个容器在集群里面，然后才能登他去看图形化界面。有点烦是不是？没关系，我们来个更新，换一个模式换成负载均衡会收费。


lord balance 在阿里云上是单独收费，而且公网访问的话费用还有那么一点点高，而且我要选择集群是很高级的模式。好，不管怎么高级，因为我们时间比较短，所以费用还可以接受的等。他正在创建 loadbalanceloadbalance 什么？是一个类似于 NGINX 的这个网络负载均衡器，但它是一个偏底层一点，就是 NGINX 特别偏应用层，它稍微底层，它也不像 f5 是完全底层，它是一个比较中间的，这个也是属于 4 层的这个负载竞争器，我们等一会，等它创建出来。它创建完了以后，我们就可以用 UL 外网的 UR 去访问它了。


好吧，在等的过程当中，我们朋友完全可以什么创下一个应用对不对？这不影响。我们想想看，我们有了这个 rabbitmq 有了这个有 record 对吧，也有了两个数据库， Redis ，MySQL那我们下面还有什么平台没做 gateway 没做对不对？ config 没做。那 gateway 通常最后做，因为对外服务，我们把 configure 准备好，使用镜像创建一个 config 叫 my config 好，这里面 config 就可以两个了对不对？无状态的，而且我们也不准备搞一些酷炫的东西，走两台足矣。


好。下一步两台，选镜像请找我们的 my config 好，找到了 1.0 版本，然后其他都不变，没有什么特别要注意的。然后点，你下一步要不要进 service 呢？还不用对吧？ config 通过友锐卡来提供服务，我们是客户端 ribbon 的方式附带均衡。


那请毫不犹豫的点创建，我们，看看应用怎么样了这一点应用就进到 POD 是不是两个实例，我们看第一个这是什么？这是两个的，这个 POD 对不对？每个 POD 里面一个容器。好，我们看一下这个容器的日志是什么，也选择自动刷新，很快的刷刷他尝试去连 rabbit MQ 对哟， rabbit MQ 我们已经起来喽，所以应该是能连上的。我们看有没有报错，有没有报错呢？似乎是连上了对不对？似乎是连上。好，我们再去看下面的服务有没有什么问题。他说 broker not available 看一看 infer 好也没什么大问题。我们不管它，我们先往下看，但是好像 rapid MQ 的 suc 还就是没有完全连上，不停在那里报错。


bit MQ 杠 SVC 我们去看一下是不是这个名下我们是不是取的这框的名？ my rabbit mqs 取错了多了个 my 对不对？没关系，我们来改一下这里什么，这里名称不能改。给上面有用没用。那怎么办？删了重建。好吧，别折腾了，但我们不是什么，我们不是删应用，我们应用就 miq 没问题了，我们只是什么服务对吧？我们服务的这个地方为什么我们会叫这个呢？是因为什么我们的服务这里我们就看我们刚刚起步来肯定看这就是一个 debug 过程。


这到底什么提法改？其实就是这样地方，看看日志你也不用登进去看，在图形化界面你就能看到日志。对不对？是不是 rabbit mqkssvc 可没有霾，只有应用才叫埋好。我们把 service 重建一下就好，删掉删什么 merry big service 对吧？ service 不好取得不成功。我们在这里让大家看一下怎么建 service 不要从那个 deployment 这里点，从这里也可以。点就叫 rapid MQ service 对不对？这也就对了吧，还是要用这个什么虚拟 IP 的形式让提供服务。然后关联 my my rabbit MQ 好随便去哪，这不影响 rabbit MQ 那 rabbit MQ 的地址还记住吗？不是 5672 是吧，这是这个常用地址吗？好5672。那我们就写一下好吧，5672好勒，我看你还报错不，我们回过来看。好在看之前，其实我们看一下，怎么外部端口还没建完这么慢还真的有点慢。这个罗列巴斯有点慢。过完我们先回过来看一下，看一下它这个应用是不是正常起来了。我们回到这个无状态无状态，看看我们的这个 mike big 到底能不能起来？日志对不对？自动刷新 attempt attempt attempt 好像成功了。


 simple connection 好像成功了。 amqp 貌似成功了。下面是什么？ it will be declared a broker is restarted 好连上了，但是结果还没出来。
那在这个等的期间，我们看看另外一个实例好不好？我们回到无状态再去 my config 我们看另外一个 POD 下面那个 POD 我们不是两个POD ，在一个 depot 建两个 POD 这个 POD 里面也有一个容器。


好，我们看一下那边也是这样，是不是比如说 it be will be declared 那他是不是还没有注册到友瑞卡里面？是不是有点这个感觉？所以我们还要等友瑞卡也起来，然后注册进去，这个时候应该就能显示什么，完全正常这个状态。好，我们来看一下。有人卡服务期待没？你不会还在创建中吗？好，还真的是还在创建中还真的够慢，那我们就再喝一小杯茶，稍等片刻。


