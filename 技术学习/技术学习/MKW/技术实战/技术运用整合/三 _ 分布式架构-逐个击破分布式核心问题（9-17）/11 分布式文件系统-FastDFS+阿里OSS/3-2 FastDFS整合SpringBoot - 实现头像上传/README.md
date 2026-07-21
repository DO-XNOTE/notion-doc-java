---
title: 3-2 FastDFS整合SpringBoot - 实现头像上传
---

# 3-2 FastDFS整合SpringBoot - 实现头像上传

[image](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/d7ebb9e0-cd5a-449b-9c8c-71593d2f9cb6/SCR-20240806-kayg.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667OU56QUW%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T225224Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQClPAvi8f6ymRxwS4tpXsmmyr66MHVbsb%2B%2FF6yoYwDAggIgWG6ocYg5aYi0jresbzwUqSt7l%2F%2B8tUdyiHM4wsdxg6sqiAQIxv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDLpjDSQ9AhqzQVSfzCrcA9FxMM34h1Q4Pe1BiTrYSJOnQ%2BpfCKdLu2YrkhsCS%2B0WsQkEKxPsoGOTIFkd%2BuTgE7adr%2BDBPcG5Kv4kAiX5CHfLwh45jXUF02KIWJ9piNBjEAgkvxuspfKCevHRrMNstK4izXPOB0oPReayTBSSFBb2sCFvSZp%2BqAsILI8Ogvoq3lBf4LycGS8f2jqGPXiuGS2we91KtePS0%2BDomoDE25jRS8TjYJthuoitmmB4en2VeuRZrBkj0qVWpGvZuzLdyaIPdUzzmWVY5i5RUsgYJOnzgGjr2ejfUWsmdHqvLq5yHBwxq7BIg9ZgbZsvYRHVuTIuvo%2F5eY%2Fi%2BSjh5TiEJ2c6K%2FIHowqNGvqvKlkwHxjNguFQfimQo6Abwk0OF4COCSk2BJku90B%2BkgRzvZCNDTRS19CqwjxvbRucA6nUSSfs7ecVndHYGXEKf%2B20%2B9N5NjMa5L1pi1ocnmcyQwYvYbEHbgmGjVy8q72sbbooOuTU9ohWpDGDmYKQSQ0a5uCm3NmylRO%2BA25ilYeDMMOiO%2BfZdSIsRxp%2FRR2jSN25Rm9bR%2By0ZF9BRj3QrK0G5YVfKqfIi0t5tky5j2O4opge%2BdMOfbj6ohwOm1zusYHzsOZTXPIoxM6%2B4tkIkLISMJS3%2F9IGOqUBrwDm%2B0%2FamKpQUsoNSi3rdm949p99UpMl5Pa9Kg4fwNWZ1rJwA96jcIPJq5d3MwIkkNhD9y7sIkYd1ZISYRgsjC2YnPcxO9TsVGqOShekwKarofY%2FsVka5EkSfdnOHHf2rS2K36Hj%2FSpIV5rmhwMYJ06KvqZmElmaOdywmUEpzpBJkIUh1BAzYukYOMhLU06ocMDFAkk118gNeD2RGCYtAONJoOOg&X-Amz-Signature=38f6ce21a222af84bfc077c32a956d0bafb78b5fbc43e1c5959ff1a75c958379&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

上一节我们是把这个 service 写了一下，接下来我们去把咱们的 Controller 去解一下，然后我们再来发起一个调用，在这边我们先来创建一个package。然后 Controller 我们直接去拷贝一下，我们之前其实是使用的是 center user Controller。来看一下，在这里面其实是包含了一个上传，我们拷贝一下，我把这个 Controller 直接拷贝到我们现在的工程里面，然后再去做一个相应的一个修改。


那么在这里我们说一下，就是说像这个 service Controller，其实我们都是独立到了这个单独的一个工程里面去。大家在使用的时候可以参照我的这种方式去做，当然你也可以把这一部分的 service 和 control 来放到你自己的一个 API 项目里面去，都是可以的。那么我在这边单独拿出来的话，这样子它的一个看的会更加的清楚一些。好，然后我们拿出来以后，在这里面我们去做一些相应的修改。那么像这个 base Controller 这里拿掉，然后这个 slack two 相关的我们也不需要暂时先拿掉。那么这个我们改个名字， f d f s，我们叫这个名字。然后这些我们都不要了，这个也不要了，这是它的一个 slack to 的也不要，然后这个参数也不用，我们保留这些就可以了。


好，然后我们再往下，其余除了我们当前这个方法以外的，其他的我们也其实也都不需要我们往下面找，从这里开始到下面我们都不用，所以我就全部都删掉。好，OK，然后这里是更新的一部分内容，这个的话我暂时先注释掉，我先注掉，然后这边我全部都注掉。这个其实我们也不需要，这是获取图片服务器的地址，这里我们先不用了。好，OK，那么随后我们把其中这一部分的内容我们去做一个相应的完善。那么这个自定义头像保存的地址这个我们是用不着的，这是之前所使用的。然后这个也不用，然后这是它的一个前缀地址，不需要我们直接使用这里面的。首先是判断我们的这个 file Multi part file 是否是不为空才会进入。那么在这里会有一个 output stream，这个也用不到的，然后这边我们把这个 excepping 我们拿出提到外面去直接 slow 掉，那么从这里面到下方这一部分的内容我们就拿掉了。


OK，然后我们 Tab 往前面提一下，这边是文件写入磁盘，我们也不需要了，这个 output file 也不用，然后这里保存的最终地址也不需要，这是文精灵也不要，对吧？那么在这边我们只需要保留这一块内容，就说判断我们的这个 five name 这边是判断不能为空。


另外在这一部分要判断一下我们这个图片的后缀名，我们限制为这些后缀名。所以如果说我们要去做一个上传了以后，那么直接在这个地方，在这里去发起一个调用，去调用咱们的 service 就可以，那么在这里我们去把这个 service 给agenda。我们是 f d f s service。把它给加一下。


OK，然后我们在这个地方就直接可以去发起一个调用 service 点upload，那么第一个是我们的file，把这个文件拿到写过来。那么第二个参数是我们的后缀名在这里是suffix，直接写过来，那么这样子我们就可以拿到，然后我们直接string，等于，那么是获得它的一个pass，也就是它的一个路径。


OK，在这里可以获得到，然后获得以后我们可以在这里去做一个打印。OK，这样子的话，其实我们如果说能够打印出来，那就说明我们当前这个文件的话，是可以通过我们的这个 client 做到一个正确的一个上传的。OK，好，那么这样子的话我们先来做一个测试，来看一下我们这个步骤能不能够成功，那么我们先来 install 一下install，看一下它是不是成功的。


好，OK，那么这个是 build success，那么随后我们就可以来做一个启动，咱们先把当前这个FS，这个我们先去启动一下。
使动语后报错了，看一下这边在定义这些内容的时候，这边应该是没有扫描到的吧。我们这样子，我们的这个启动类里面我们有些东西没有完善，我们拷贝一下以前的，我们把以前这一段内容我们直接给拿过来贴到这个位置，那么稍微的精简一下，那么一个是我们的 Meta scan，就是我们刚刚的一个map，我们是需要去扫描的。那么另外一个就是我们扫描自己的 base packages，一个是抗比m，对吧？另外一个是这个是我们的 IB worker，好，OK，那么这样子我们再来做一个启动，我们右键运行一下。


OK，那么目前是启动成功了，然后我们再来启动我们的API，再把 API 里面这个去启动一下。
好，那么两边两个服务我们都已经是启动了，随后我们来看一下咱们的一个 BS code，打开一下，那么这是我们的 center 这个项目，我自己本地的 template 已经是预先的去启动了。然后打开这个 user info，点 html 这个文件，在这个文件里面我们来搜一下，搜一个upload。那么在这个位置这里是上传头像，那么上传头像的话，在这个位置，我预先是把这一段，这是他原来的一个UL，我是注释掉，然后提出来放到了这里啊。这是它原来的一个 file Server，然后在这边我是重新定义了一个新的，那么这是我当前的一个8066，这是我的一个路由 f d f s。


然后是 upload face，那么这个是对应到我们的一个后端的Controller，是在这个位置，这是所对应的，那么这里面的一些参数的话和我们以前是保持不变都是一样的，所以我们后续的参数是不需要去动。好，OK，那么然后我们打开浏览器，我们刷新一下，那么这个就是我们的一个后端，对吧？用户中心，然后点击一下以后我们随便的去上传一张图片，我们来上传一个face。一，那么在这里提示说头像上传成功，然后上传成功以后，那么我们没有去做一些额外的设置，所以这边的头像是不会有任何的改变的。


那么我们回到咱们的后端来看一下，打开咱们的控制台可以来看一下8066，那么在这里你可以看到有一个输出，那么这个输出其实就是我们的一个路径地址URL，我们直接把它给拿出来。我们拿到这里我们直接把这个路径去做一个覆盖，我们到这里。OK，那么这个其实就是 store pass 上传之后所拿到的，它包含了一个这个文件的一个文件名、路径，以及是它的一个组名。好，然后我们回撤一下，OK，那么你可以发现这一张图片目前我们就已经是成功的上传了。OK，那么这个其实就是我们目前所结合的一个 fast d f s 的一个 client 实现的一个文件的上传。那么这样子的话，我们这一块上传就已经是 OK 了吧。

