---
title: 4-3 OSS的基本配置
---

# 4-3 OSS的基本配置

[image](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/5489b46f-4d75-4c9d-a0be-3c94086dc4be/SCR-20240806-klrc.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665EVIZYOD%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T225227Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIEruZre9AO08wTJwwRq2VutUmmHaVZ2m0OPsV1Yl00vAAiEAmjcaqMJHqxd91m7Do1VJJlifceDn7j4%2BrTFp9Z5LBa0qiAQIxv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDPi46CcF0xDInAEAGircAwCwbRVF1JoeGWrQRmE%2FYS%2B8ZXNe8C8Z4NP%2B4JzemKr8rXW2aBg2VDya1VKG8VdRCFpYp7sOdqUhfsW5x9eeqbzhGDgaAHW7NxNr3B%2F%2FpjTUHytKSjTDKlXSBIChmApD0%2B9lflqhqQA4pW51LrKU1FIr7IC3RryFs5ZGasIqRVg7cmIGUHkm5F5Z8wlnl35%2FdVh7s%2BtoJl7y%2FeRi%2FWe%2FTYT8hG73HdplVBFt6k%2FfiVDYysCjmMsG7tciakqS%2Bi90k40nJyw25aPxWK0gdAg2CNKUUpEP5Pp6wkd1i8%2BxUeeZEFAqz9ZJ3J0NU%2FmS199oURQFGfSmjhW%2Bll7%2FepnkbPazCxNuPjr3ZEDIrxYec4GZqnNnd0L95ZsC4mLbDE%2BA6pDUE3qQp6FFPWtgJx9vJhMZLOADnAvOgQ2R%2B3ymKZup7Zbbz3TuAhdx3x4QcIMolEm6HP3Y0az5Tq%2FOTOPZGzuNuK3HDnatX3UHsIh1PGs3ftU4QJfgAePBR6yG7SPvNPopYHHVAKg35yqVwWPHFL0rdq1a%2F40%2BLaU%2BngsX4CbFY16fK6Yu8%2FZMRVITrkVfZ71jVyv6O8KUGdqnqpx25BsC0IQHTaYAFhYkfPfrZeHGOM9DQrmqaaTrPMiIMP23%2F9IGOqUB%2F060skZKT1Yqv6bVCfTD0R8MT78DAWZKhTzy2Cq57NmSSCnqfpClQ5mk8s5JRik471sJ%2FXSwahlOU%2FOHIvF30tlkES3pv%2BhkNUwz14zTAplvSNSBmn1%2FsN4uYLawb51acWSPJaJPv6ucmBZoRPumWb90IrWn6mh7t78i8lSPgDvjURYmHxLp5BUpn9YOIjlFnS575EdBxPAc%2BEI%2BaLmmLmPYdcdm&X-Amz-Signature=93f6e86ef9c6848578f0b568e9199699fd7eff6b0b0345eb007a02ce276f825b&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

那么接下来我们就来一起看一下阿里云 OSS 云存储的一个后台，这个后台首先我们先看这个最左边，这是你的一个存储空间，存储空间叫做bucket，在这个位置，在它的一个右侧，在这里有一个 bucket 管理，这个其实就是你的一个存储空间，也就是说我们所有的图片其实全部都是存储到这 market 里面去的，你也可以把这个理解为是一个项目的工作空间。


我们在进行平时项目开发的时候，会把一些相对应的项目统一的放到某一个特定的工作空间里面去，这个在我们的一个图片文件云存储里面其实也是有这样的一个概念。比方说在这里我们开发慕课网相关的一些文件资源，我们会上传到这个，在这里我是取了一个名字叫做ITIMK，是存储到这个 bucket 里面去。如果说我们要有一些其他的，比方说有像物流一些环保项目的业务在这边你再去创建一些其他的 bucket 就可以了，不同的存储空间去负责给不同的一些项目去做对接就可以了。


这个就是一个bucket，在这里你也可以去创建一个，比方说像这个要注意它是一个全局的名称，这个 ID 是唯一的，像这个 imock 就已经是被其他的账号给注册了。那么在这里你可以来一个 i look test，然后有一个区域，那么这个区域随便选，比方说我选择北京，对吧？打个勾，然后在下边这边会有一个endpoint，这个的话我们在项目里也会使用到的，它是一个外链的一个链接，在下面还会有一些存储类型。那么我们使用这个标准就可以了，另外还会有一个同城的冗余存储，这个的话应该是要付费的，在这里我们就直接关闭。

[image](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/1636812c-c222-4b6f-b77b-cbbd220b5591/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665EVIZYOD%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T225227Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIEruZre9AO08wTJwwRq2VutUmmHaVZ2m0OPsV1Yl00vAAiEAmjcaqMJHqxd91m7Do1VJJlifceDn7j4%2BrTFp9Z5LBa0qiAQIxv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDPi46CcF0xDInAEAGircAwCwbRVF1JoeGWrQRmE%2FYS%2B8ZXNe8C8Z4NP%2B4JzemKr8rXW2aBg2VDya1VKG8VdRCFpYp7sOdqUhfsW5x9eeqbzhGDgaAHW7NxNr3B%2F%2FpjTUHytKSjTDKlXSBIChmApD0%2B9lflqhqQA4pW51LrKU1FIr7IC3RryFs5ZGasIqRVg7cmIGUHkm5F5Z8wlnl35%2FdVh7s%2BtoJl7y%2FeRi%2FWe%2FTYT8hG73HdplVBFt6k%2FfiVDYysCjmMsG7tciakqS%2Bi90k40nJyw25aPxWK0gdAg2CNKUUpEP5Pp6wkd1i8%2BxUeeZEFAqz9ZJ3J0NU%2FmS199oURQFGfSmjhW%2Bll7%2FepnkbPazCxNuPjr3ZEDIrxYec4GZqnNnd0L95ZsC4mLbDE%2BA6pDUE3qQp6FFPWtgJx9vJhMZLOADnAvOgQ2R%2B3ymKZup7Zbbz3TuAhdx3x4QcIMolEm6HP3Y0az5Tq%2FOTOPZGzuNuK3HDnatX3UHsIh1PGs3ftU4QJfgAePBR6yG7SPvNPopYHHVAKg35yqVwWPHFL0rdq1a%2F40%2BLaU%2BngsX4CbFY16fK6Yu8%2FZMRVITrkVfZ71jVyv6O8KUGdqnqpx25BsC0IQHTaYAFhYkfPfrZeHGOM9DQrmqaaTrPMiIMP23%2F9IGOqUB%2F060skZKT1Yqv6bVCfTD0R8MT78DAWZKhTzy2Cq57NmSSCnqfpClQ5mk8s5JRik471sJ%2FXSwahlOU%2FOHIvF30tlkES3pv%2BhkNUwz14zTAplvSNSBmn1%2FsN4uYLawb51acWSPJaJPv6ucmBZoRPumWb90IrWn6mh7t78i8lSPgDvjURYmHxLp5BUpn9YOIjlFnS575EdBxPAc%2BEI%2BaLmmLmPYdcdm&X-Amz-Signature=619c1383f3e27cdb6f910f245e128a3e9bbd1e9d8a4d813d28b7787f068b3a53&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

随后下面就是a、C、l，也就是文件的一些权限，那么在这里会有私有、公有读和公共读写，那么我们一般来说写的话我们是自己由程序去写，读的话我们是要对所有的外网的一些用户 l 开放，所以我们会使用这个公共读，OK，使用公共读就可以了，公共读写的话，那么我们这个写的话不要公共使用公共读。然后在这里还会有一个服务端加密，这边没有必要，我们就不加密了，这边还会有一个实时日志的查询，那么你也可以去开通，或者说是不开通的话会提供免费的 7 天服务。OK，然后的话我们点击确定，那么这个时候在这里就会创建，就会多出来一个新的bucket，可以点进去，点进去的话就会有相关的一些内容。当前这个其实就是归属于我们的 imock test 这个存储空间的，像之前这个之前是有，我是用去做测试的，像你的一个存储的用量，本月流量、本月请求次数，在这里其实都可以去查看的，OK，这里面其实也都会包含。


其中还有一个就是文件管理，这个文件管理的话在这边你是如果说我们在后续用户上传到文件以后，在这里我们都能够看得到，比方说点击上传文件在这里，那么它就会有相应的一个上传文件的 VIP 层。然后我在这里比方说我来选一张照片，写一张图片，直接往这边一拖就可以了，拖了以后，那么它会做一个上传。好以后，那么在这里就会有一张图片，你可以点开来，以后它会包含一个图片的详情，文件名 e tag 是否要使用HTTPS，还有是文件类型 ACL 等等，其实全部都有。然后你也可以右键，然后转到，那么它会去做一个下载，以后在这里相应的这张图片它就会有了。


OK，那么这是下载到本地的，这个是我们手动的去上传，那么当然过我们程序上传也可以，程序上传以后，那么最终也会在这个目录之下的。OK，好，然后我们这样子，我接下来的话，其实我们就可以去把相应的内容整合一下，整合到我们的一个项目里面去。那么先来看一下，在这个地方有一个叫做 x s k，这个是用于去生成我们的一个ID，所以只是一个密钥的，先点一下，点一下以后有这样的一个界面，那么它会有一个安全提示的话，一个是使用子账号，另外一个是使用当前账号。子账号的话就是子用户，我们在这边使用当前的账号去创建，那么在这里我已经是预先创建了一个 access key 了。OK，当然我再创建一下也可以。那么大家其实可以自己去创建，我在这里就不去创建了，然后有这样的一个 access key ID，还有是一个 key secret，就是 ID 和密钥，这两个我们在集成的时候都会使用到这一点，大家自己去创建一下。


OK，好，然后我们在这里，在这个地方有一个常用入口，其中有一个开发者指南，在这个里面其实就是包含了我们使用 OSS 的一个常用功能，比方说最常用的有上传，那么其他的也会有搜索、查看、删除等等版本控制，其实在这里面全部都有吧。对于我们来讲的话，那么我们会使用到这个上传文件，然后在这边在帮助文档中心打开点一下，在这一块就是它的一个功能的概览，非常的丰富。


在这边菜单里会有很多很多的内容在这里是上传，然后可以来看一下，在这边有一个 SDK 的参考，点击一下，这边包含了很多的语言吧。我们点击Java，然后有一个安装来看一下，其中就包含了我们的 SDK 的一个安装，它有相应的一些方式。那么 j d k 的版本是要在 1.7 或者以上，然后在这边它贴出来一个 Maven 的EI，你可以把这个直接复制，复制以后到我们的这个项目里面拷贝就可以了。然后我们可以一起来先做一下，把这个拷贝一下，然后点开你的项目，在 palm 里面打开一下，那么在它的最下方贴一下。


在这里我跟大家先说一下，这个 3.8.0 在我本地是下不了的，但是 3.7.0 是可以去下载的，所以我在这里会使用 3.7.0 去进行使用。如果说大家在使用 3.8 的时候可以下载，那么你就使用3.8，OK， 3.7 也可以达到我们的一个效果。好，然后点击保存，然后import，这样子的话依赖就可以导入到我们这个项目里面来。这个就是你 SDK 的一个安装，使用起来会比较的方便，如果说你没有使用每本库的话，那你就需要自己去下载，自己下载之后再导入到你自己的项目里面去就可以了，这个就是它 SDK 的一个使用，随后在这里它会有一个上传文件，在这边点一下点进去。


那么在上传文件里面就是它会包含了很多的一些方式，比方说有简单上传表单上传、追加断点续传，还有是分片。其实对于我们来讲，我们现在其实是一些小图片的话，使用简单上传就可以了，它最大是不能够超过 5 个 GB 的，这一点注意一下。那么在这边我们点一下简单上传，点进去以后在这里面会包含了很多的一些方式，在这里有一个流式上传，还有在下方这边是有一个上传的字符串，还有是上传的 bug 数组，此外还有是上传网络流。另外再往下这边是上传文件流，OK，然后是文件上传，那么这个文件上传在这里的话，其实也是贴了出来这一块内容，其实它里面的一些代码基本上都是差不多的啊。都是差不多，那我们会使用这个，我们使用网络流去进行一个上传，其实你只要把这一块代码拷贝到自己的项目里面去就可以使用了，使用起来也是非常的简单的。


好，OK，然后我们先来看一下，如果说你要使用的话，它会有一个叫做 OSS client，我们是通过这个客户端去发起一个请求调用的，然后在这里会有一个 input stream。那么这个 input stream 我们拿到以后会去进行一个上传，然后这边是直接放到 put object 放到这个里面的，然后再去做一个执行，在这里面他用这个尖括号所括出来的地方，其实我们都是需要去做修改的。


OK，先这样子，我们先来把这些内容基本的先去设置一下，比方说第一个有一个 and point，我们的先拷贝一下到自己的项目里面先去做一个设置，因为我们毕竟会使用到先把项目打开，找到这个 file practice，在这个里面去使用，我们去加上一个，有一个 and point，这个 and point 其实就是在我们网页端，在这个里面点击某一个bucket，这个里面有一个外网访问，在这里有一个地域节点，那么这个就是当前的一个endpoints。我把这个拷贝一下，然后贴到我们的项目里面来贴过来。OK，这个就是我们要做的第一个配置，随后下一个，下一个的话是包含了我们的，来看一下啊。和你的 secret ID 和 VR 都去拿一下这两个，我们拷贝一下，先把这个短语先设置好，还有是 secret 也拿过来。好，OK，那么这两个从哪里拿？我在这里我就直接去拷贝了啊。


那么就是这两个东西，这就是我的 ID 和这个就是我的一个密钥，大家根据自己的一个情况去做相应的设计就可以了，不建议使用我的，因为我这个可能过段时间就会到期绩效。OK，好，那么这是两个 KID 和 k secret，那么这个是在你自己的这个密钥里面，就这个东西去拿一下就可以了。好，然后下一个下面还会有一个 your bucket name，你的存储空间的一个名称，把这个拷贝一下，接过来。把这个改掉。那么这个名称就是我们之前所见的，就是在这里 i mock test，把这个拷贝一下贴过来就行了，这就是我们的文件存储的一个存储空间，然后下一个，下一个我们再来看一下，下一个是 your object name，这个是什么意思呢？这个其实是你的文件的一个路径名，应该说是相对的一个路径名。当我们在文件上传以后，那么这个文件名的话会我们会有的。所以我们在这边的话，我们可以去设置一下，在这边设置一个路径，比方说在这里举个例子，进入到这个 bucket 里面文件管理，在这边我们是可以去新建目录的，比方说我们来一个a、b、 c 点确定，对吧？那么这个其实就是我们在这个文档里面所提供的一个 object name，这个 name 的话还包含了我们的一个文件名，在这一块的话我们会去做一个拼接的。


OK，我们先不管，先来做一个设置，我们先把它给设置进去，我们先拷贝，把这个名字拷贝一下。这是 object name，等于比方说我们来定义一下叫蝴蝶杠 d v，来一个斜杠Images，我们可以统一的放在这个里面，当然我们后面还可以去拼接这个用户的ID，用户的文件名都有。


好，OK，那么有了以后的话，我们暂时就这样子，我们现在打开咱们的 file resource，这里面之前有一个host，那么现在我们就可以针对刚刚所添加的内容去做一个相应的设置吧。我们多拷贝几个，然后把之前设置的全部都拿进来，那么第一个endpoint，第二个 access ID，第三个我们的 secret 密钥，随后这是 bucket name，另外还有是我们的 object name。好，OK，那么我们先这样子，然后把 get 和 set 生成一下。好，OK，那么这样子的话，我们这个基本的这些配置现在就已经是放到咱们的一个项目里面去了。OK，也就是针对于这个文档里面这一段内容的一个 endpoint ID 密钥， bucket name object name。


