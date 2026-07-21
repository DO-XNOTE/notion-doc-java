---
title: 1-2 案例实战-阿里云认证实战
---

# 1-2 案例实战-阿里云认证实战

[image](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/65498404-101f-4016-b115-ecef1848ab56/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466R66Q4PSG%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T231113Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQC7UMRmrx1c6M1PZlbFA9xIiC0jAPJQZVJyqikGCjIq%2FwIhAPvnCnbWAbW0Fuvdw1lkPQKZxapite6HWdmmR%2FpPOEjjKogECMb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgzqPwuWyIdtWvk6ttUq3APs9cipipZcOAruDLhXtIGbMl7t%2FAjngVUZa%2BDcH%2FY2QValTq7EY%2FPPZqA1ilv3c27lEA8%2Bc%2B3GxxOLYPefn9%2BeJB1%2BecQRa2ZA%2BLV%2Fch01vTgsFg13N4qyj7BSD7czWDrBoKDgPzKYUUkFwnsCFxbZy02%2Bc%2BmU%2BTggiDJ97Qhu%2BH%2BD5bzIEMSdb7%2FNjjoeYWKVDKptrQhUq18MVlr1%2FKi0gaJ3FDXCCoQbkuXyhvWRATfXpBeCTWMBPDZMClpUQwR225Y9QDubfb8l7LglGWtdwfiJdPp1HP%2BbvFUYYNnNRJNzfbfEpid3NiiYdOmZ8AiYTXRaU3%2B72i799pdBF9yST80vKCK6p9UvkMNDHCX0mUmYQi7Nl7XlcrWPjGRphn%2FGekx%2FgRZMYnNSkxfAA2e%2F8c5rjI4ZHJB47KcZkODpf%2BO9ko2PJtkvMBYutdCvn%2FKdaDqLZ1gUey%2F5SGgNXIiUnO07K9T5hrMrXx6%2BWp0NX0i9zMzaXiljb5UO%2Bj0STypW53YjvfsS0aK8hnCR3CyEI3zqb6gtF9FTbNSnubfzbKx%2BEFrsFsEoe7DJC5M%2BgCFggkk2RP5bA5vagLMtgqIyjzX8kpWfJYw9tLo4Jw25R33RNkm3YbsRVThrOjDAuf%2FSBjqkAZx6XDhaMClvcNnSmBmCKHz0O7u0%2BBDdi9EFQUcHy3%2B5FXkuFVGSxaS4IeiWLz0yWJJqJdN%2F9R6HHnYrdbMUWfeCY%2FWbT9xrrPhQzsYbU1keMiviJ7mRo8BwVvn6y2qArtiPxRgZt6yjcMTNwO0wEypNZOnxv8wtfas3WT06WM%2F7w%2Fev%2B3Tp%2FFvhlUkemS7D%2FDxcEoxgADDgly6KtiRZOm2tFEe%2F&X-Amz-Signature=c0e2b6a2e21d70bbe1777096eb589be741004c272206516bdbb0872292bf2f7e&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

架起需求到落地的桥梁，构建 IT 新蓝图。我是张飞扬。上一个章节我们聊了聊安全的认证和授权。这一节我们就在阿里云进行一个实操。首先我们看一看还是登录阿里云的控制台界面。我登录的操作方法是什么？采用主账号登录，也就是作为 CTO 或者 CIO 方言老师亲自用个人账号或者是一个最高级的账号登录了阿里云系统。

[image](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/39667eca-ba21-4935-bc28-9c9daf714531/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466R66Q4PSG%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T231113Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQC7UMRmrx1c6M1PZlbFA9xIiC0jAPJQZVJyqikGCjIq%2FwIhAPvnCnbWAbW0Fuvdw1lkPQKZxapite6HWdmmR%2FpPOEjjKogECMb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgzqPwuWyIdtWvk6ttUq3APs9cipipZcOAruDLhXtIGbMl7t%2FAjngVUZa%2BDcH%2FY2QValTq7EY%2FPPZqA1ilv3c27lEA8%2Bc%2B3GxxOLYPefn9%2BeJB1%2BecQRa2ZA%2BLV%2Fch01vTgsFg13N4qyj7BSD7czWDrBoKDgPzKYUUkFwnsCFxbZy02%2Bc%2BmU%2BTggiDJ97Qhu%2BH%2BD5bzIEMSdb7%2FNjjoeYWKVDKptrQhUq18MVlr1%2FKi0gaJ3FDXCCoQbkuXyhvWRATfXpBeCTWMBPDZMClpUQwR225Y9QDubfb8l7LglGWtdwfiJdPp1HP%2BbvFUYYNnNRJNzfbfEpid3NiiYdOmZ8AiYTXRaU3%2B72i799pdBF9yST80vKCK6p9UvkMNDHCX0mUmYQi7Nl7XlcrWPjGRphn%2FGekx%2FgRZMYnNSkxfAA2e%2F8c5rjI4ZHJB47KcZkODpf%2BO9ko2PJtkvMBYutdCvn%2FKdaDqLZ1gUey%2F5SGgNXIiUnO07K9T5hrMrXx6%2BWp0NX0i9zMzaXiljb5UO%2Bj0STypW53YjvfsS0aK8hnCR3CyEI3zqb6gtF9FTbNSnubfzbKx%2BEFrsFsEoe7DJC5M%2BgCFggkk2RP5bA5vagLMtgqIyjzX8kpWfJYw9tLo4Jw25R33RNkm3YbsRVThrOjDAuf%2FSBjqkAZx6XDhaMClvcNnSmBmCKHz0O7u0%2BBDdi9EFQUcHy3%2B5FXkuFVGSxaS4IeiWLz0yWJJqJdN%2F9R6HHnYrdbMUWfeCY%2FWbT9xrrPhQzsYbU1keMiviJ7mRo8BwVvn6y2qArtiPxRgZt6yjcMTNwO0wEypNZOnxv8wtfas3WT06WM%2F7w%2Fev%2B3Tp%2FFvhlUkemS7D%2FDxcEoxgADDgly6KtiRZOm2tFEe%2F&X-Amz-Signature=45de7d3588b9ee410e0cd31236b02a0b7717f8df5e91604574e32dd8403f5603&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

这次我要按照前面课程内容一样，看一看怎么样实现跟企业内部 AD 进行互通。也要看一看怎么样把我的阿里云的服务对 mock 网提供一个什么远程的授权和资源访问的，怎么样来做这些基本内容。需要采用什么叫 r a m 模块，这也可以看到我们搜索一下 IM 模块，叫 r a m 访问控制，这套全名我们点击一下。


好，这里就打开了 i m 访问控制的整个主页。这个主页里面可以看到好多事情都没有做， CTO 不是很合格，很多事情都没有干，我们就依次来干一下。 SSO 这里我可以尝试选择角色SSO。这里说了角色SSO，就是跟什么企业内部的IDP，通常就是 AD 或者 LDAP 对接实现，根据 AD 或者 LDAP 来完成用户认证。授权却是什么，采用云平台的授权管理机制，也就是组人对应相关的角色，从而访问相关的资源。这样的一套授权机制来访问语音平台。我这里可以创建一个身份提供者，比如要什么飞扬老师的企业等等。上传一些源文件，点确认，最后完成一系列后续的操作，从而对接企业内部的 AD held up。这里因为我们没有一个对应的系统，所以这里就跳过跟大家讲一下整体思路是什么样好。


另外一个情况就是什么我要让慕课能访问什么我们企业内部的对象，存储其中的一些照片，从而把我们公司内部的很多的讲师通过慕课展现给大家。怎么做就用到这里。 Oauth 应用管理我要什么创建一个应用，这个应用就是慕课王填写他的名称，把他的什么慕课的 native app 的名称以及对应的回调信息填在这里，然后在慕课那里做 Oauth 相对应的处理。这样慕课就跟 Oauth 对接起来。可以授权访问菲亚老师的 GCS bucket，从而了解覆盖老师的长相照片。


好，这是 Oauth 的应用场景。聊完这两个，我们其实没有真正实战。如果大家想真正实战，可以不妨在阿里云上跟自己的应用系统来自完美的亲密接触。好，我这里重点给大家看一看日常更常见的是什么。在这里管理组合用户。假设我没有和 l Dev 对接，假设我希望亲自来管理组合用户。怎么样创建组？怎么样创建用户？我可以先创建一个 SRE 的组织点。创建组叫 SRE，让他们来管理我的什么 ECS。服务器显示名称也叫 SRE。好，双月完成了 SRE 这个组对吧，有一定的权限，假设我们可以给它加个权限，像什么样的权限？整个云平台里面所有的我们的 ECS 都让他们可读。也就是所有的 SRE 的成员都可以访问所有 ECS 的机器，但是不一定能够修改，不一定能够删除。好，我们点一个确认好就完成了授权。所以组里面的所有用户都可以进行正常的读和访问了。


我们再找一个用户，这个用户就是我们刚刚说的，我们要创建一个 s i 的总监，他可以完全代表我来管理所有的服务器。同时他还可以什么授权给他一些能够在服务器上设置动态角色的，这样他就可以访问后台的数据库了。我这里演示只演示一个，能登录服务器好不好。

取什么名字，就叫 SRE director，加个下划线 SRE 下划线director。好，这是 SRE 的总结了。显示名称也是这样。这叫 s i direct，它的全名是at，然后是我的账号，这个账号就串数字，就代表非老师的企业在阿里云的注册。点 on 阿里云 .com。总监可以用命令行，也可以用控制台。上面是控制台，下面是命令行。用命令行都通常需要有一个 ID 和它的secret。


这里我可以强调一下，我建议通常大部分的用户开启MFA，防止是个总结的密码管理的不当，对吧，被别的什么用户给串去了，或者黑客给破译出来了。 MFA 前面在安全的章节已经聊过多因素，可以有虹膜，指纹或者是一些其他的 auth 工具。好，我们这里点击确认。确认完了以后，我们就创立了一个叫 SRE 下划线 director 总监这样的一个角色。我们可以给总监进行一个授权，添加一些权限对吧？当前可能还是在创建过程当中创建完成了对吧？我们可以给他添加一些权限。可以看到我们在添加权限之前先往下滚，这里它默认其实就会有一个叫主权限的，我们先不管，先给它添加一个叫 ECS 完全掌控权限，完全授权它来帮我管理所有的服务器。


好，点击确认。点击完了以后，我们再重新点进去，看一下他现在具有什么样的权限。我点进去看一下好点。他权限管理可以看到什么？他个人有什么样的权限。它是整个阿里云 ECS 的总控人员对吧？ for access。同时它还继承了组里面的成员的权限，没有继承到组权限。原因是什么？原因是我们没有把 s i director 加到 s i e 组是不是？好，我们添加个组，我们把它加到 SRE 组是吧？作为 SRE 组的成员之一。


点击确认加完组以后，我们可以看看权限里面多了个叫继承权限。重新刷新一下。此页面要刷新一下好，还是点到这个权限里面。我们看继承权限诶，是不是继承了？它可以继承什么ECS 的可读权限，这里看上去有些多余，它已经完全是什么 full access 了，还需要继承吗？有些时候就不多余了。比如我给主权限加一个对象存储的访问权限，这个时候它就可以通过继承来访问对象存储了，而不需要给总监个人单独再创建什么对象存储的访问权限。通过这种继承，能够很好地处理大部分用户的权限授权。


在飞燕老师真正使用的不管是什么亚马逊云、谷歌云等等云平台的生产系统里面，几乎没有个人授权的情况，都是以组授权，甚至是比如像 SRE 总监，我也创建一个组，叫什么叫运维总监组，而里面授权一个人叫 SRE 总监，他的副手可能也放在这个组里面。他们都具有什么相对应的或者相类似的权限。


通过主授权能够更好的管理什么不同的角色，而不是针对某一个人。你这个人可能今天是 SRE 总结，明年就是什么是支付系统的什么研发总监。当你的个人角色替换的时候，尽量把你从这个组移到另外一个组，就可以完成权限的更替，而不老是针对某一个人来进行反复的授权。


好，聊完了组用户，我们下面就要实战一下，看看刚刚已经完成了这 SRE 总监这个组到底该怎么样玩溜达，使他能够真真正正的什么实现用户的登录。好，我们还是回到用户，在用户里面其实是没有设置过他的密码，是不是我们这里要好好的设置一下他的用户登录密码。


自定义一个用户密码。好，复研老师给总监定义一个密码。好，定义完了以后，总监下次来访问他的时候就必须要使用这个密码。同时他还要把多因素用户认证这套流程给走完，使得他以后每次登录可以正常的通过密码加上一个多因素其他的因素，来完成整个令牌的获取，从而能够接入我们的控制台，完成真正的用户访问。


好，我们回到概览。普通用户登录的不是在这里，不是在什么 console 点阿里云 . com 来登录服务器，而是采用这样的链接，我们快速的打开一个这样的链接。好，我们打开了链接，输入刚刚复制下的用户名，叫 SRE，下划线 direct at，就是整个我们企业的ID。点了 on 阿里云 .com，我们点击下一步。所以输入密码就是输入我刚刚设计的一个密码，点击登录。它说什么不能直接登录，因为我们企业已经规定了必须要多因素的，你 SRE 总监也不例外。怎么样第一次设置多因素？很简单，他推荐你，我放大一点，他推荐你是用阿里云APP，其实无所谓，你是百度云 APP 或者是什么谷歌云 APP 都可以。


飞扬老师平时用的比较多的叫 Google Auth 这样APP。任何一个支持多音素登录的小软件，其实都能完成扫码，自动的创建出或者是识别出对应的安全码输入。在这里大家可以挑一个第三方的任何的这种多维身份认证的小工具去扫描一下。二维码，我们来扫一下，扫完了以后自动它就会在小的 APP 里面注册一个新的账号，它的用户名就叫 SRE director at。刚刚大数字这里面第一次动态生成了一个码，叫101793。这一段我没法录屏给大家，因为我装了 APP 在手机端。它要求什么？隔一段时间 30 秒以后要生成第二个数字，我们要再输入一遍。已经过了 30 秒，我拿到了第二个数字，叫689328。我要确认完成第一次绑定。他说什么？作为 SRE 总监，你可以不要按富阳老师 CTO 这样诡异的密码，你可以定一套自己的密码。好，作为 s i 总监，这是我们来定义自己的密码。定义完成了，设置一下，这样就完成了。什么 SRE 总监对于自身多因素认证以及密码的管理。你自己定义了密码，同时你自己绑定了一个经常使用的多因素用户认证系统，也叫 o t p one time password 系统，在不管是我们 apple 的 APP 或者是各种安卓系统上，都能下载到很多很多的多因素 APP 工具。它通常都能生成一个六维的密码，而这个六维的密码其实就是通过刚刚读的什么二维的这个 QR 码转换出来的。


好，完成了以后，我们现在登录账号已经不是 CTO 了，不是飞扬老师了，是一位总监的，叫 SRE direct 这样的一个用户。我们看一看他能访问些什么资源。 like is this。诶，仍然看到了我们四台机器，大家可以尝试一下。如果不让 SRE 总监享有 SRE 的权限，也不享有自身独有的对 ECS 的总控权限。你不仅不能登录，你连看都看不到这 4 台机器。我们点击实例，你可以看到菲亚老师作为 CTO 当时创立的机器，你还可以把 CTO 创立的机器给删除掉，给停止掉，给回收掉是吧？或者启动都可以，可以，释放都可以。


这就是什么？这就是 CTO 向 SRE 的总监授权，不光是读取，而且是全权掌控所有服务器的权限。好了解了如何登录一套系统，作为一个普通用户登录什么系统？登录刚刚那种是吧，一串数字的系统，而不是直接是 console 点。阿里云 . com 也了解了作为CTO，应该如何授权组，授权用户，如何去跟自己的 LDAP 对接，以及如何把整个企业内部的资源提供给第三方。像是慕课之类的应用来读取内部的资源。或者是作为一个普通的计算资源，应该怎么样通过 API 的方式获取到ECS 的资源里面的token。


这种动态形式虽然我们这里没有在实战当中跟大家讲了，但是大家可以想象到，如果我们设计好了动态 token 的获取，就可以让每台 ECS 登录完以后， ECS 本身都可以获取到动态token。在上面跑的每个应用也都可以通过 SDK 从 ECS 所对应的 row 上获取到相关的权限。这里我还是点进去给大家看一下。


如果要这样做，我作为 SRE 总监，其实需要做一个事情，我要给每一台我创建的机器绑定一个 r a m 角色。看到没有，这里没有绑定。如果是要完成前面 PPT 说的事情，先让 CTO 的创建一个角色。我 s i e 总结应该把这个角色创建高级角色，跟它绑定起来。这个时候在这台机器上跑的任何的应用，就是 Docker host 跑的任何的应用，只要采用SDK，它就会自动从这台机器获取到对应的角色的token。这个 token 是实时获取的。拿着这个 token 就去看这个 token 能访问是RDS 还是 OSS 还是NAS，就可以访问对应的资源了。好，聊完我们的 i m 权限访问和控制，以及做了一个简单的实战。大家是不是对云平台的用户登录、账号管理权限规范有了一定的了解？下一章节我们来聊一聊其他的平台性的内容数据库系统，大家敬请期待。


## 前因

本文主要介绍阿里云的 IAM 权限访问和控制系统。在云计算时代，云平台扮演着越来越重要的角色，如何管理云平台上的权限访问和控制，成为了一个必须解决的问题。

## 后果和影响

IAM 权限访问和控制系统的出现，使得云平台的权限管理更加灵活和高效，也提高了安全性。通过对用户进行分组和授权，可以更好地控制用户对不同资源的访问权限，从而避免了不必要的安全风险。同时，IAM 系统还为企业内部资源的管理提供了便利和规范，使得内部资源共享和开发更加方便和高效。

## 目录树

- 阿里云认证实战
- 数据库系统
- 总结

