---
title: 3-5 用户注册 - 创建用户controller与测试
---

# 3-5 用户注册 - 创建用户controller与测试

[image](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/baa2cc0f-8f2a-4180-9baf-c2b1c209d232/SCR-20240816-tlxd.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TDAVR7QD%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T224626Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCICviMPKsIOIWhnmWPgkCZWHL8SQVVV1jY%2F%2FcLC7nF6UGAiAsMAT8Td9ZSIqSoIK38rmFLBC9OeCX3x6zyhRQgUPKmyqIBAjG%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMi0jzjqikyeJofSitKtwDWUef7tNRGEHTwyoJ5RU7U75BcYGkDpnumoQSeda%2FvL%2FfUE%2B7mZLX4ki9JL7IqjQrg4IwGoJueTLBxMxf4fyusjp2T6slwpwRdA4HHtG%2BKUQKzoSGkFIWDSqInjaEslCVwDnznGtXHd7xJBzPH03FPq93EF2pm8HcF2rEzVcce4SwLFI50ieBOsI%2BE2YcPQRfvbU%2FXJBBigphERvFaSPmqxGy4%2B2FTHOkTvYCMUQBycm2lUE0aETMLNwZIOH5ADJjmI7o7mXRpVb2rypFK79pRPkEOOXTnRGCxB8IeKjRjm49psFoC%2BYzrqkYXekgM4VzjyGxFN251y3kGQXiOAwyZ%2BvEtRN%2FDdCZ2P%2FrA95t37JIcMkTzNZtW2fkAF3W%2BDhbt4P30uwsOl26lgkN%2BWaGZ2VKvlRPSoHKWnNwiS4jsqJRePHI%2B2LyuNh%2FbDsYvBpBH5Zhd%2BFRjBLGJob8HyLtsBVaY1QEmxpnSikBEkXju5PyJGlv07%2B3DQMIK873hYvLQXGwV9rPUVQuy%2B%2FU9n%2BK7X%2Bjx%2FAekKWxBod%2B4I8YBpp4NGm0HxP5E4GjWmFmGeu%2BdLXEE8PyepJ3tUuVFL8%2Bl0dKTE3IKAPf7Q7KndfVaYmAB2mSoIBTzkLIQtowtbj%2F0gY6pgH%2ByygWPw3vcUZ1dHIvOw9TMmcPJtZgTXZ5Fc4RLoAayZQOPBqCauOj6CgC%2FiZbR6Fs2cj4XNN0ecvFoLqDrdYsuAcUiGP9jOc9uWPIAjWWS%2FL8w%2FDp3xNahevNudbzis%2F2Kmc8Tnwgwqx2BON7kWYEItRHmxGyrcuP8wXv%2F3D%2FRq14ZxIiyF68coX4zSTPSVTH%2BOIqurnmGH9duZlXK3%2BI3W3CAGAB&X-Amz-Signature=71fc2580b1f5d4964cc85afa3e8a91e32c5a85e1e02f81f808b38fdf01a33c2f&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

[image](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/55c45d93-f6d7-4e9c-b875-1b5061a36f8a/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TDAVR7QD%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T224626Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCICviMPKsIOIWhnmWPgkCZWHL8SQVVV1jY%2F%2FcLC7nF6UGAiAsMAT8Td9ZSIqSoIK38rmFLBC9OeCX3x6zyhRQgUPKmyqIBAjG%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMi0jzjqikyeJofSitKtwDWUef7tNRGEHTwyoJ5RU7U75BcYGkDpnumoQSeda%2FvL%2FfUE%2B7mZLX4ki9JL7IqjQrg4IwGoJueTLBxMxf4fyusjp2T6slwpwRdA4HHtG%2BKUQKzoSGkFIWDSqInjaEslCVwDnznGtXHd7xJBzPH03FPq93EF2pm8HcF2rEzVcce4SwLFI50ieBOsI%2BE2YcPQRfvbU%2FXJBBigphERvFaSPmqxGy4%2B2FTHOkTvYCMUQBycm2lUE0aETMLNwZIOH5ADJjmI7o7mXRpVb2rypFK79pRPkEOOXTnRGCxB8IeKjRjm49psFoC%2BYzrqkYXekgM4VzjyGxFN251y3kGQXiOAwyZ%2BvEtRN%2FDdCZ2P%2FrA95t37JIcMkTzNZtW2fkAF3W%2BDhbt4P30uwsOl26lgkN%2BWaGZ2VKvlRPSoHKWnNwiS4jsqJRePHI%2B2LyuNh%2FbDsYvBpBH5Zhd%2BFRjBLGJob8HyLtsBVaY1QEmxpnSikBEkXju5PyJGlv07%2B3DQMIK873hYvLQXGwV9rPUVQuy%2B%2FU9n%2BK7X%2Bjx%2FAekKWxBod%2B4I8YBpp4NGm0HxP5E4GjWmFmGeu%2BdLXEE8PyepJ3tUuVFL8%2Bl0dKTE3IKAPf7Q7KndfVaYmAB2mSoIBTzkLIQtowtbj%2F0gY6pgH%2ByygWPw3vcUZ1dHIvOw9TMmcPJtZgTXZ5Fc4RLoAayZQOPBqCauOj6CgC%2FiZbR6Fs2cj4XNN0ecvFoLqDrdYsuAcUiGP9jOc9uWPIAjWWS%2FL8w%2FDp3xNahevNudbzis%2F2Kmc8Tnwgwqx2BON7kWYEItRHmxGyrcuP8wXv%2F3D%2FRq14ZxIiyF68coX4zSTPSVTH%2BOIqurnmGH9duZlXK3%2BI3W3CAGAB&X-Amz-Signature=3945bfd2f31e8341010278c94ec4a90ba77f7047935f5b7e148e0204d1f2ae45&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

上一节我们是把创建用户的 service 这整个方法我们是写好了，随后我们就应该要去把它的一个接口去进行一个实现它的接口。我们回到passport， Ctrl 了拷贝一下。拷贝之前的一个方法，我们在这里面去做一些修改。首先一个我们由于是保存，所以我们在这里不再使用get，我们会使用 post mapping，这里面的路由写上一个register。另外下方我们的方法名也称之为是register。好。


随后是我们的参数，在上一节课里面，其实我们也已经是说了，在前端传过来的参数我们会放在 user b o 里面传过来。所以在这个地方我们只需要把 user b o 贴过来就可以了。由于前端传过来 b o，它对象是一个 JSON 对象，我们在这边我们要去接收它，所以我们会加上一个 request body。


OK，拿到了读者 Bo 以后，其实我们在接口里面，我们也应该要去针对这里面的信，相应的信息去做一个校验。用户名密码，两次密码是否一致等等，这些我们都要去做一次校验的。因为校验不仅是在前端做，在后端也要去做，我们在之前已经是提过了。OK，好。我们可以先把 v o 里面的内容，我们可以先可以去获取一下。


下一个是 password get password 好，最后一个。第三个是 confirm p w d get 一下好，参数已经是获得，所以我们就要去做一些判断，比方第一个写 010 万，第零个适用于去判断用户名和密码，必须不为空。随后下一个我们要去查询用户名是否存在。这个方法我们在前方其实已经是用过了，这个是用于去在前端去做校验的，后端其实在保存之前我们也应该要去做一次校验。第三一个判断用户名应该是判断密码，判断两次密码是否一致好。随后下一个我们应该要去设置一下密码的长度，密码长度一般来说我们不能太短，所以密码长度不能少于 6 位，一般是 6 位。好，再下一个我们顺序换一下。一般来说我们是先判断密码的长度，再判断密码的一个两次是否一致的。如果判断都 OK 了以后，我们接下来所需要去做的应该要去实现一个注册了，写一下。


第四一个，这个是实现注册好，我们就根据顺序，我们就可以去编写相应的代码。其实在开发过程中，我也是建议大家可以去多写一些注释，因为多写一些注释，一方面是帮助我们去理解业务，也方便其他的开发人员去看。另外一个，有了相应的注释的步骤了以后，你自己的一个业务逻辑就可以理得更加的清晰。这一点我是比较推荐去做的。OK，好，我们先来做第一个判断，判断为空还是一样使用 string 与test。我们之前有用过点 b s， blank 判断是不是为空，如果是为空，我们就直接抛出。随后在这边我们或者这三项内容，只要有一个是为空了，我们判断校验就不让他过。今天我们换行。下面是 password 以及是 confirm password，这几个只要有一个是 blank 是空了，我们就直接 return 一个 imock result。点使用 error message 写一下用户名或密码不能为空。这样子前端就可以去进行接收了。下一个判断用户名是否存在，直接拷贝上方的方法就可以了。把直接拷贝一下贴到这个里，考过了就可以了。


随后再来判断一下密码的长度，也就是 password 写过来，点less，如果它的长度是小于6，在这边我们直接也续称一下，密码长度不能少于6。好，下一个我们要判断两次密码是否要一致了，应该是passport，点equals，把 confirm 写过来，应该要加一个感叹号，代表是不一致。不一致。在这边写一下。两次密码输入不一致。OK。当我们这些内容全部都通过了，我们就可以在这边直接可以通过 user service 点 create user，再把 user bo 传进去，这样子就 OK 了。好，写完了以后，其实我们现在就可以去做一个测试了。我们来测试一下我们的数据 o 不 OK 对不对？使用这个 POS 面，我们可以先去 install 一下，好，安装成功，我们再一次启动一下我们的群内。启动成功以后，我们就可以来做一个测试。我们还是使用postman。在这里面我们写一下 password passport，使用 register 后方我们就不需要有额外的参数了，我们这样子光溜溜的一个路由就可以了。OK。随后在下方会有一个 body 点一下。


我们之前说了，我们在进行一些参数传过去的时候，我们实际是在前端通过波点塞纸的。在通过前端波点塞纸的时候，我们是以一个结算对象。在这里面会有很多种类型，我们选择一下r，a， w 选择一下。在这边又会有一些相应的内容。这个其实就是一个格式，我们在可以选择 Jason 点一下。我们在这里就可以去构建一个相应的内容了。我们先构体一个空对象，点击send。很明显我们是会报错的，来看一下，他会报一个 method not allowed，这个是一个，应该是post。再来 send 一下。这个时候其实已经是进入到我们的后端了。我们现在用户名或密码不能为空的对吧？所以我们在这里要把相应的属性字段我们都要去写好。第一个是username，随后我们是要定义的一个名称，比方来一个imock，再来password，来一个123123。随后是 confirm pas，索的太长了，我们就直接拷贝一下吧。在这里 confirm password 贴过来，123456。好。Jason。我们是构建好了点击线的，发送一下。这个时候其实可以看得出来我们请求是肯定到达后端了。这个错误发生的不一样。现在是两司密码输入不一致。好，我们只要把密码再改一下，改成123123。点击send。这个时候会发现传过来是 OK 了对吧？没有问题。我们可以到咱们的数据库里面去刷新一下，这个时候其实我们的数据其实就入库了。


来看一下ID， ID 是我们通过 Sid 所生成的，这是我们的一个用户名，密码是加过密的 nickname 保持和 user name 一致， UI name 可以为空。真实姓名我们一开始是没有的，随后在后方还有是face，这张 face 其实也是使用默认的就可以了，后面可以去修改。随后邮箱还有是某票手机号可以保持默认为空。另外性别是 2 也没有保密。对于后面的三个日期，这个是birthday，这个是我们使用的默认的是创建时间以及是更新时间，都是使用当前默认的一个时间就可以了。好，现在其实我们的第二个接口应该说用户的注册其实就已经是做好了。OK。

