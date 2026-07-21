---
title: 5-2 支付宝支付 - 构建支付表单填并提交
---

# 5-2 支付宝支付 - 构建支付表单填并提交

[image](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/fd1f7c7d-ec57-41a5-b9de-a01b0511d175/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667VSKXMGS%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T224715Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIHpQj8m%2FSQyswlJnb1h48qztZsO1mjnPE8Se9V1IM3%2BLAiBELAdYOA0cxvklbpzqJ%2Fyg3ryDNNfU40md8e1qDiQ8HSqIBAjG%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMz6lR4cGF9cVU1%2FENKtwDzF%2B8oERicyUHdotXlUHMZgwcZod3KavLBNhW2Q3nkVcKlqJy85XOhd0X1wpAddXq9dr3Ih8nZv88LcQIVdHY6sPmhMSknnrMx4rml9TUVWXx0pTPY2yrdQKlRC8s2NhpsDX4TiVQCKTn3QigwDmj0iCE8yD5tZyG9XVa4G%2BIPBviFG0zs77t3h4nM80GyUytE%2BK6lokDPFnArsNtpO9eM%2FxI47nR20q8D5VMYgE%2FOOoRZf%2FZOxrbJorHXDnvsWyWytzPG9dxjnxCMs2N0PeYcyXrbCiox6Yy2NKpTrFe8AcVMzu67AGbNqJRVDDmVWDB7LpeRtKFUY9D72NOoe%2Bz2su6sNE00fDQBx5cVTNziOKiHK%2FKNBn9RvNR9JiGf7rCofdBFlEY%2BFRMRFjV3mAryemWgvhIHe8hZnirEST0IOip9gwwbvwEhZNENVKX11dowiS%2Fh7%2BMhzVcNWMONClvk4H2iKpn3cBk8d1bjPe6WZ%2BxQENN8DzYci45Jb0OojLl%2FSpX9nwdN9PsFzbont44uk3iulZodwCKvIpJfBXmw5l34q3Esg%2BXONQ4kzxj8fthgzvzjxDzEYI3YbI3yuR0oLUbGv0rnx%2BsopjvzZ0eVHfY3WIWQlSxao4d%2BV4w2rf%2F0gY6pgGyRucAkHi4psAtkZE63VXio6ZkVqUoknfg1LUytYj%2BytYSbedBojgIubv%2FxCk5E8MDXod2QEM7eAOAEEapQo4AFsr2xUtjxWCb4xKDUjfkAz%2BPu5ehsqSwcOH32KI%2BCIAjJx9bCCN91cqkjXpCyOkf57m4rCVEailP2WHPa6LPPxZTks9Ng2g5v5XnIz2VWcnIRo34bgkWMJTZYOVsoTLktSX7Ue0j&X-Amz-Signature=5645594a55a7647b668e7792be1ab1a6583a17365ecc17bfe66e40136171bec8&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

上节我们是讲了支付宝支付的一个时区图相关的一些流程。这一节我们就来看一下咱们的代码，

[https://opendocs.alipay.com/open/270/105899](https://opendocs.alipay.com/open/270/105899)

来看它是如何去发起请求，让我们的页面跳转到支付宝的。其实如果心系的同学，他可能会去尝试使用支付宝去做一个订单的提交。其实现有当我们的微信支付整合好了以后，由于我们已经是有了一个回调轮询的接口，用于查询我们订单有没有成功。当接口写完以后，

[image](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/64385c45-6172-4e3e-9533-1beff4015053/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667VSKXMGS%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T224715Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIHpQj8m%2FSQyswlJnb1h48qztZsO1mjnPE8Se9V1IM3%2BLAiBELAdYOA0cxvklbpzqJ%2Fyg3ryDNNfU40md8e1qDiQ8HSqIBAjG%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMz6lR4cGF9cVU1%2FENKtwDzF%2B8oERicyUHdotXlUHMZgwcZod3KavLBNhW2Q3nkVcKlqJy85XOhd0X1wpAddXq9dr3Ih8nZv88LcQIVdHY6sPmhMSknnrMx4rml9TUVWXx0pTPY2yrdQKlRC8s2NhpsDX4TiVQCKTn3QigwDmj0iCE8yD5tZyG9XVa4G%2BIPBviFG0zs77t3h4nM80GyUytE%2BK6lokDPFnArsNtpO9eM%2FxI47nR20q8D5VMYgE%2FOOoRZf%2FZOxrbJorHXDnvsWyWytzPG9dxjnxCMs2N0PeYcyXrbCiox6Yy2NKpTrFe8AcVMzu67AGbNqJRVDDmVWDB7LpeRtKFUY9D72NOoe%2Bz2su6sNE00fDQBx5cVTNziOKiHK%2FKNBn9RvNR9JiGf7rCofdBFlEY%2BFRMRFjV3mAryemWgvhIHe8hZnirEST0IOip9gwwbvwEhZNENVKX11dowiS%2Fh7%2BMhzVcNWMONClvk4H2iKpn3cBk8d1bjPe6WZ%2BxQENN8DzYci45Jb0OojLl%2FSpX9nwdN9PsFzbont44uk3iulZodwCKvIpJfBXmw5l34q3Esg%2BXONQ4kzxj8fthgzvzjxDzEYI3YbI3yuR0oLUbGv0rnx%2BsopjvzZ0eVHfY3WIWQlSxao4d%2BV4w2rf%2F0gY6pgGyRucAkHi4psAtkZE63VXio6ZkVqUoknfg1LUytYj%2BytYSbedBojgIubv%2FxCk5E8MDXod2QEM7eAOAEEapQo4AFsr2xUtjxWCb4xKDUjfkAz%2BPu5ehsqSwcOH32KI%2BCIAjJx9bCCN91cqkjXpCyOkf57m4rCVEailP2WHPa6LPPxZTks9Ng2g5v5XnIz2VWcnIRo34bgkWMJTZYOVsoTLktSX7Ue0j&X-Amz-Signature=451ab24a73bb31ca094268022b1df3914a6e220c6cba3f018b037f3281cf1925&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

支付宝其实在我们的系统里面就可以去使用了，但是我们还是要了解一下它的业务是如何去进行的。

[image](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/652aa789-a231-4ee9-96f1-9e67b7d7f357/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667VSKXMGS%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T224715Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIHpQj8m%2FSQyswlJnb1h48qztZsO1mjnPE8Se9V1IM3%2BLAiBELAdYOA0cxvklbpzqJ%2Fyg3ryDNNfU40md8e1qDiQ8HSqIBAjG%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMz6lR4cGF9cVU1%2FENKtwDzF%2B8oERicyUHdotXlUHMZgwcZod3KavLBNhW2Q3nkVcKlqJy85XOhd0X1wpAddXq9dr3Ih8nZv88LcQIVdHY6sPmhMSknnrMx4rml9TUVWXx0pTPY2yrdQKlRC8s2NhpsDX4TiVQCKTn3QigwDmj0iCE8yD5tZyG9XVa4G%2BIPBviFG0zs77t3h4nM80GyUytE%2BK6lokDPFnArsNtpO9eM%2FxI47nR20q8D5VMYgE%2FOOoRZf%2FZOxrbJorHXDnvsWyWytzPG9dxjnxCMs2N0PeYcyXrbCiox6Yy2NKpTrFe8AcVMzu67AGbNqJRVDDmVWDB7LpeRtKFUY9D72NOoe%2Bz2su6sNE00fDQBx5cVTNziOKiHK%2FKNBn9RvNR9JiGf7rCofdBFlEY%2BFRMRFjV3mAryemWgvhIHe8hZnirEST0IOip9gwwbvwEhZNENVKX11dowiS%2Fh7%2BMhzVcNWMONClvk4H2iKpn3cBk8d1bjPe6WZ%2BxQENN8DzYci45Jb0OojLl%2FSpX9nwdN9PsFzbont44uk3iulZodwCKvIpJfBXmw5l34q3Esg%2BXONQ4kzxj8fthgzvzjxDzEYI3YbI3yuR0oLUbGv0rnx%2BsopjvzZ0eVHfY3WIWQlSxao4d%2BV4w2rf%2F0gY6pgGyRucAkHi4psAtkZE63VXio6ZkVqUoknfg1LUytYj%2BytYSbedBojgIubv%2FxCk5E8MDXod2QEM7eAOAEEapQo4AFsr2xUtjxWCb4xKDUjfkAz%2BPu5ehsqSwcOH32KI%2BCIAjJx9bCCN91cqkjXpCyOkf57m4rCVEailP2WHPa6LPPxZTks9Ng2g5v5XnIz2VWcnIRo34bgkWMJTZYOVsoTLktSX7Ue0j&X-Amz-Signature=f58206b5987c8a497f230a97359970dc7b30af6c5adb21c9cb4aed7366ba34bb&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

OK 好，先来到我们的配点HTML，在这里接口是用于去创建我们订单的，创建订单完毕以后，会根据支付方式进行一个判断，如果是支付宝，在这里会有两个跳转。这两个页面我们都来看一下。其中一个是阿里 pay 点 html 我们可以先打开在这个页面里面，这个其实是支付宝的一个支付结果页，是用于去查询是否成功的。

[image](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/9675c718-0e31-4322-80d0-07d9b6586fff/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667VSKXMGS%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T224715Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIHpQj8m%2FSQyswlJnb1h48qztZsO1mjnPE8Se9V1IM3%2BLAiBELAdYOA0cxvklbpzqJ%2Fyg3ryDNNfU40md8e1qDiQ8HSqIBAjG%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMz6lR4cGF9cVU1%2FENKtwDzF%2B8oERicyUHdotXlUHMZgwcZod3KavLBNhW2Q3nkVcKlqJy85XOhd0X1wpAddXq9dr3Ih8nZv88LcQIVdHY6sPmhMSknnrMx4rml9TUVWXx0pTPY2yrdQKlRC8s2NhpsDX4TiVQCKTn3QigwDmj0iCE8yD5tZyG9XVa4G%2BIPBviFG0zs77t3h4nM80GyUytE%2BK6lokDPFnArsNtpO9eM%2FxI47nR20q8D5VMYgE%2FOOoRZf%2FZOxrbJorHXDnvsWyWytzPG9dxjnxCMs2N0PeYcyXrbCiox6Yy2NKpTrFe8AcVMzu67AGbNqJRVDDmVWDB7LpeRtKFUY9D72NOoe%2Bz2su6sNE00fDQBx5cVTNziOKiHK%2FKNBn9RvNR9JiGf7rCofdBFlEY%2BFRMRFjV3mAryemWgvhIHe8hZnirEST0IOip9gwwbvwEhZNENVKX11dowiS%2Fh7%2BMhzVcNWMONClvk4H2iKpn3cBk8d1bjPe6WZ%2BxQENN8DzYci45Jb0OojLl%2FSpX9nwdN9PsFzbont44uk3iulZodwCKvIpJfBXmw5l34q3Esg%2BXONQ4kzxj8fthgzvzjxDzEYI3YbI3yuR0oLUbGv0rnx%2BsopjvzZ0eVHfY3WIWQlSxao4d%2BV4w2rf%2F0gY6pgGyRucAkHi4psAtkZE63VXio6ZkVqUoknfg1LUytYj%2BytYSbedBojgIubv%2FxCk5E8MDXod2QEM7eAOAEEapQo4AFsr2xUtjxWCb4xKDUjfkAz%2BPu5ehsqSwcOH32KI%2BCIAjJx9bCCN91cqkjXpCyOkf57m4rCVEailP2WHPa6LPPxZTks9Ng2g5v5XnIz2VWcnIRo34bgkWMJTZYOVsoTLktSX7Ue0j&X-Amz-Signature=7cdec9f98cf905c9885e80fe6910167fa9613ff0b1643425a9de52aaf03581e4&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

在这里可以看到它也是一个轮询，和微信支付是一样的，它都会有一个结果，最终去进行一个查询。接口。其实我们在之前开发微信支付的时候，其实就已经是写好了，所以在这边去进行调用是没有问题的。 Alipay 点 HTML 这个页面就是用于去做一个支付结果的轮询和查询的。


好，我们再来看。另外一个页面，叫做。看一下是阿里 pay temp transit 点 HTML 这个页面其实用于去做一个跳转的，它其实是一个中间页，我们来看一下。进入到我们这个页面以后，在这里它会有一个方法叫做this。点 get 阿里 pay form 看一下这个是在这里，它其实主要是用于去获得支付宝，它所构建的一个支付表单，支付宝的一个支付形式。它其实是一个表单提交的形式，它是以一个表单把一些相应的数据以表单的形式提交到支付宝网关。支付宝网关接收到以后，随后再返回相应的一个页面。它其实是和微信不一样的，微信它是生成的一个二维码，让我们去扫描的。两种方式是有区别。在这边来看一下。


通过我们构建的一个路由地址，请求我们的支付中心，这个支付中心是一个 go 阿里pay，在这个后方你要和我们之前做的时候要一样，要传过去两个参数，一个是用户ID，一个是订单号，这两个都要有。当然由于是调用我们的一个支付中心，所以老师分配给你的这两个属性字段，也就是你的一个账号一定要去输，一个是 user ID m 可分配的一个账号，另外分配给你的一个密码，这两个输入一下，一定要去写的，写了之后才能够去调用。修复中心好发起请求了，以后来看一下。


在这边会获得一个 RD 配form， form 就是一个表单的属性，这个表单里面是一些什么内容，我们一会儿可以来看一下。在这里我打上了一个 debug 断点，OK，我们可以去看一下的。好，我们来看一下它。一个提交 go 阿里配打开我们的一个支付中心的源码，这个源码会提供给大家的。在讲它的一个方法之前，我们先来看一下。在我们当前支付中心里面，其实我们也是引用了一些相应的美本的依赖。来看一下。在美本的依赖里面，在这里有一个SDK，这个 SDK 其实就是社保的SDK，你是需要去引入的。在我们之前做微信支付的时候，和微信相关的这些是微信支付的一些美本依赖，是需要去加入进去的，参照一下就可以了。


好，回到我们的肯托了。在这里格偶阿里配前往支付宝进行支付。好，首先我们先来看一下，根据我们传过来的一个用户的 ID 以及是订单ID，我们要去拿到一个订单，这个订单就是支付中心的一个订单，你要去拿出来。随后我们要做一个初始化阿里 pay client，其实下面的这一些源码在支付宝的官方它其实都提供的，在这里我们也过一遍，因为一旦你这些代码有了之后，其实你只要整合到自己的项目里面去，就可以去实现一个支付请求的发送了。来看一下，这边是你有一个 default Artipay client，在这边要传入相应的一些参数，这些参数其实都是配置在阿里 pay resource 类里面。来看一下。之前我们有说过，微信也是使用的这种方式去获得的，相应的在我们的项目里面有一个叫做阿里 pay 点


practice，有一个属性资源文件，把属性资源文件我们直接打开就可以了。打开一下，首先看我们第一个要用到的，刚刚的是欧阿利佩，在这里第一个是要获取网关的一个地址 Gateway URL，这个应该是在我们的这里。支付宝网关。支付宝网关其实在官方的一个文档里面也都有，在文档里面可以搜一下的。我把拷贝我们到官方文档里面去搜一下，可以看到在这里这是一个接口调用的配置，在 SDK 调用前需要进行初始化。可以看到初始化和我们代码里面是一样的。阿里 pay client 我们要初始化，要传入相应的一些数据，这些数据像一个UL、 APP ID 等等都要传。其中第一个 UI 就是我们的支付宝网关，它是一个固定写死的，所以在这里有一个参考值，把这个参考值直接拷贝到咱们的项目里面去就可以了。


好，下一个是 APP ID 了，这里有一个 APP ID， APP ID 在这个地方有 APP ID。另外还有是商户的私钥以及是支付宝的公钥，这些内容其实都是由支付宝所提供的。所以一旦你用企业资质到支付宝去注册了一个企业账号以后，你要和支付宝进行一个签约，签约完毕之后，通过一些相应的配置，你就可以拿到你自己应用的 APP ID。


商户私钥以及是支付宝公钥，这些内容都可以去拿到的，或者去生成的，拿到了以后你再直接配置过来就可以了。微信支付其实也是一样的，微信它会有一个商户系统，你到商户系统里面去进行了一个认证，以后认证每年是 300 元。认证完毕以后，你要去创建相应的应用，你的支付随后就可以获得你对应的 APP ID 等等相应的内容。这些内容都是在你注册完毕相应的一个支付以后，签约以后才会有的。所以这些内容怎么来的，就是这么来的。 OK 好。这些 APP ID、私钥、公钥在我们这里都可以去配置到，这里是 APP ID 是私钥，会有一个format，这个 format 是一个传输 JSON 的格式，在我们的一个文档里面其实也有，在这边会有一个 format 参数返回的格式，它只支持JSON，所以固定写死就可以了。


好，下一个。下面一个是XSET，它的一个编码集，支持g、b、 k 以及是u、t、 f 杠8。在我们的项目里面看一下，我们在项目里面使用的是u、t、 f 杠8。OK，好，下一个。下一个要是一个支付宝的公钥，在这边传进去就可以了。最后一个参数就是一个 3 Type，它是一个签名。看一下是签名的方式，使用的是r、s、A2。其实有两种方式，一个是 RSA 和RSA。 2 有两种签名的方式，在它的官网文档这里也有。有一个 3 Type，是商户生成签名字符串所使用的一个签名的算法，它支持两种，一个是 r s a two 和 r s a，它推荐是 r s a two，使用这种方式就可以了。

OK，通过参数我们就可以获得一个 APP client 了。 OK client 我们就可以在这里引用出来了。 client 有了以后，接下来我们要构建一个 RD pay trade page pay request，这个是一个支付的请求，其实你就可以把它理解为一个request。在这个 request 里面，我们要设置两个 URL 地址来看一下，一个是 return URL，另外一个是 notify URL。这两个其实我们也有设置在支付中心里面。首先看一个return，这个是页面跳转的一个同步的地址路径，同步的地址路径也就是在你支付完毕以后，支付宝的网页，它会跳转的一个页面。它是一个同步的形式，它是一个 get 请求，它可以请求某一个 get 形式的 restful 接口，也可以直接返回到某一个具体的页面，其实都是可以的。


随后下一个是 notify well，这是一个异步通知。这个异步通知和我们在微信支付过后的一个异步通知其实是同一个道理，它都会有一个异步通知的，这一点要注意。只不过微信和支付宝，微信它少了一个return。OK。支付宝的一个同步通知地址是要我们自己去写的，这一点要去注意的。好，我们继续。


我们可以看文档，文档其实上面也有，在文档里面，在下方有一个接口调用可以点在这里面其实就会有两个参数，其中一个参数就是一个 return while，另外还有是一个 notifile while。其实这个参数在它的官网文档里面其实也有说明，只不过它的说明在这边写的比较的简单。


好，我们回到咱们的一个代码，下面我们要获得一个订单号。这个订单号直接有解释，是我们商户网站订单系统中的唯一的订单号，是必填项。商户网站里面其实就是天天吃货我们后台里面所对应的某一笔订单的订单ID，在这里我们是需要定义为一个 out trade number。商户订单号是需要去写的，订单号要传递给支付宝的下一个。在这里有一个支付的金额也是从 wait pay order 从订单里面去拿到的，我们之前其实已经是设了为 1 对吧？如果在你不设置为1，在这边也可以在支付中心里面去设置。只不过在支付宝里面，它的一个金额是 0. 01，是这样子去设置的，它的单位是圆，有点区别。


下面是一个subject，其实就是一个订单的名称，下方还有是一个body，这是订单的描述。这两个其实都可以设置为一样，都没有问题。再来一个就是一个 time out，你这笔订单在支付宝那一边，如果你一直没有支付过期，它会自动关闭交易。你可以去设置一个过期的时间，它会有相应的一个取值范围，取值范围是从一分钟到 15 d， d 就是day，也就是从一分钟到 15 天，它有一个区间， 15 天其实是比较长了。我接触过的应用一般来说是一天之内有一天的，也有半天，另外还有是七个小时，一个小时、半小时和 15 分钟。在这里我们所设置的是一天是它的一个取值的单位，大家都可以去进行设置的。好。下方在这里它会有一个b、 i c content，这是一个业务参数的内容，把上方在这里所设置的一些参数一个一个的去构建。可以看到它其实在这边构建的是一个 JSON 的参数，是一个字符串行的一个JSON。OK，好，构建完毕了，以后来看一下。


在这里我们就可以去执行了。它会通过 Alipay client 点 page execute，其实就是执行一个页面的请求了，在这里会把阿里 pay request 放进来，直接请求到支付宝那一端。随后请求完毕之后，我们会拿到由支付网关所传递过来的一些相应的内容，这些内容会放到 get body 里面，在这里我们就直接可以拿到了。body。其实它是一个字符串，字符串我们把它定义为 Alipay form，也就是一个支付参数支付数据所存在的表单。拿到了这个表单以后，我们会传递到前端的页面，这个方法其实我们就已经是 OK 了。传到页面了以后来看一下。我们在这里是接触到阿里form，我们在这边是打了一个 debug 断点，我们一起来看一下 form 里面拿到的数据是怎样的。


回到我们的页面，我们刷新一下，选择支付宝，点击订单，提交了以后，它已经是跳转到支付宝了，速度非常快。但是没有关系，我们这样子，我们前端把这一段内容我们可以注释掉，注释掉以后，它就不会去进行一个页面的跳转，只会在我们的一个控制台去打印参数， debug 去掉。重新再来一遍，把页面关掉，我们流过去，好刷新一下。


我们点支付宝，来一个订单的提交好订单现在其实已经是提交过来了，来看一下，会有一个相应的参数。参数在这里来看一下。这个就是我们所拿到的一段内容，这一段内容其实它就是一个 form 表单，这个 form 表单来看一下，会有一个action，这个就是支付宝网关，支付宝网关可以看到它就是一个 get away 点do，它后面会传过去相应的内容。其中我们在之前所设置的一些参数，其实它都会构建在点度的后方，这是一个编码集，后面是一个method，是调用它的一个支付网关。另外后面还有是一个时间戳。


另外再往后面看，其实会有很多，这个是阿里配的SDK，这个是它自带的一个。另外 format 是一个JSON。另外还有一些相应的参数数据，其实全部都是在 input 里面。 input 它是一个 hidden 隐藏框，它是一个 b i c content，它包含了一个 value fellow。看一下它是一个大括号开始的，也就是它其实本质上在 failure 里面是放的一串 JS 字符串，在这里面包含了 out trade number。来看一下。


有一个190829，其实就是我们商户的一个订单号，在天天吃货所生成的一个订单的ID。相应的所有的参数，它全部都构建的，放在了 heading 的文本框里面。随后在这边会有一个summit，输出了以后会有一个JS。这一段 JS 来看一下，它是通过 document 点form，这个是代表我们获得当前我们的一个文档里面所有的forms，所有的 forms 里面 form 其实只有一个。获得第0个点summarmit，直接去进行一个提交了。提交以后相应的数据就会提交到这个地址，提交到支付宝的一个支付网关了，随后他就可以去进行一个相应的处理了。


OK，好，我们回过来。我们在这里把这一段代码开放一下，以后，我们把页面关闭。关闭了以后我们再来测试。再一次，我们点击支付宝，我们点击提交订单，点击提交。随后你会发现我们的页面发生了一个提交了。首先看我们当前页面，当前的页面是跳转到了一个阿里pay，点h、 t m、 l 跳转到这个页面。这个页面是支付宝支付的一个结果页。刚刚我们也说了，在这个结果页里面，它其实主要只有一个操作，一个目的就是要进行一个轮询，要轮询我们当前的这笔订单有没有支付成功，如果支付成功，它的状态是20，就代表我们这笔订单已经是接收到了一个异步的回调了。接收到异步回调了以后，我们的一个订单就可以提示用户一下，我们订单已经是支付成功了，可以达到这样的一个操作。OK，好，我们再来看一下下一个页面。这个页面其实就是从我们的一个支付的中转页，也就是 temp transitter 页面所跳转过来以后，其实在这个地方我们就可以去进行相应的一个支付了。OK。

