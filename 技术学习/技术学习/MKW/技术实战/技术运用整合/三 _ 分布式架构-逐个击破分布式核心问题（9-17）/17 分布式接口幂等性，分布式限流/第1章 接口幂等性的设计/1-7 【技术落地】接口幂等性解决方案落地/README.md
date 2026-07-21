---
title: 1-7 【技术落地】接口幂等性解决方案落地
---

# 1-7 【技术落地】接口幂等性解决方案落地

[image](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/a537e6fd-d3f1-4bb4-816f-246bc655515b/SCR-20240808-gttb.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RKYU4UFX%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T225448Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIHBaPbz70rEMbxYugeqcmePzJXih7%2BR8B%2BqYo0qQJ6ApAiEA8LDZ5Gi08dwbWHYoy1GcSor11SkVpbkgJEl%2FuBpIqt4qiAQIxv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDNFqz5QUsGOEtk6tcircA6WFMgYYcnyeOcz6mWZioggVTgzRc8ATQV2f7mBLcznNqhqC1bePcjR9l%2B%2BDnhH9TbFUikycSGq2hzf8Q5XBlxLdRzEP1Oneg557LAB9ltrebIFXcPkDiVlpc2NovAHNxDUXAFny353AfrM0%2BYTy3hUboEM4EGOHOCJLuLHsWrlqsdbod36Fc1ZduoqYHeopql57ljPF1p1G%2BLv4vEJWy8Ast5er%2BZ8UMOwLrsjqh9Mbp186NBsi9OgNHxqwN5p7%2BiY3uuAVRT3kb2rgVJRKcyfDuLUnKOK%2B5IKsc%2BQENIGa8jAOSGQFnWguqPelmnSQBjeeWmSabcpZusUlVu8Clf5eFpz%2BpbHHRXikdZlJz6nqcp4kAvV%2FSK%2BjbjKJDJKgHGB5uxpZJygtkEnppbVR8%2FcF9ahuR3sFlETGl5ma3EOHMnx8lwDPKSYoBLzo5HOb3qPEqrmLExkJJpnHYKyV8ReumwOhwgyLtNdiNKXk6G7vxS3NqCTWJF8raJPoIQUFgTDF2TWWbztK7gEF%2B3205DWQ00HujeUkUedrTryGTKQ66UGzFMlnpNpCQEWLeNIgL7ZTHznBct6NZVGDXLvnfI716JAVRbjuWIuF28rhT9wRoBbOttQQDaGlYjpVMLi4%2F9IGOqUB19stOzvcFdwZ1wPalYHBvS4yoqY8gvSiXs%2FkyBagJe61N1Pr4wdJV%2BXoF2Ny0sqpXInhrCY8A9IdWCPIGl1UhnfynYkewi9tkkuSXEkcQuRlNEe%2BZV0eIijsRP8HDHkWTUzuMjU%2FsT2pOQ2y7sSjfdLQh%2FITOVp38%2FFYy%2BASuscMZbfyelFTlv7Zn4i3GsdZVZp1qU9RqtCKjX2lz81%2FPEpINIVi&X-Amz-Signature=b2dcb68a83805317b902d6a581925a6e09f8463017ebca865b470b0e77a0294e&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

[image](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/59387c58-1b57-4eeb-8b78-8404563184bd/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RKYU4UFX%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T225448Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIHBaPbz70rEMbxYugeqcmePzJXih7%2BR8B%2BqYo0qQJ6ApAiEA8LDZ5Gi08dwbWHYoy1GcSor11SkVpbkgJEl%2FuBpIqt4qiAQIxv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDNFqz5QUsGOEtk6tcircA6WFMgYYcnyeOcz6mWZioggVTgzRc8ATQV2f7mBLcznNqhqC1bePcjR9l%2B%2BDnhH9TbFUikycSGq2hzf8Q5XBlxLdRzEP1Oneg557LAB9ltrebIFXcPkDiVlpc2NovAHNxDUXAFny353AfrM0%2BYTy3hUboEM4EGOHOCJLuLHsWrlqsdbod36Fc1ZduoqYHeopql57ljPF1p1G%2BLv4vEJWy8Ast5er%2BZ8UMOwLrsjqh9Mbp186NBsi9OgNHxqwN5p7%2BiY3uuAVRT3kb2rgVJRKcyfDuLUnKOK%2B5IKsc%2BQENIGa8jAOSGQFnWguqPelmnSQBjeeWmSabcpZusUlVu8Clf5eFpz%2BpbHHRXikdZlJz6nqcp4kAvV%2FSK%2BjbjKJDJKgHGB5uxpZJygtkEnppbVR8%2FcF9ahuR3sFlETGl5ma3EOHMnx8lwDPKSYoBLzo5HOb3qPEqrmLExkJJpnHYKyV8ReumwOhwgyLtNdiNKXk6G7vxS3NqCTWJF8raJPoIQUFgTDF2TWWbztK7gEF%2B3205DWQ00HujeUkUedrTryGTKQ66UGzFMlnpNpCQEWLeNIgL7ZTHznBct6NZVGDXLvnfI716JAVRbjuWIuF28rhT9wRoBbOttQQDaGlYjpVMLi4%2F9IGOqUB19stOzvcFdwZ1wPalYHBvS4yoqY8gvSiXs%2FkyBagJe61N1Pr4wdJV%2BXoF2Ny0sqpXInhrCY8A9IdWCPIGl1UhnfynYkewi9tkkuSXEkcQuRlNEe%2BZV0eIijsRP8HDHkWTUzuMjU%2FsT2pOQ2y7sSjfdLQh%2FITOVp38%2FFYy%2BASuscMZbfyelFTlv7Zn4i3GsdZVZp1qU9RqtCKjX2lz81%2FPEpINIVi&X-Amz-Signature=53120452f92ec170a39579d47f1f6f0b0f69b0ceffd640f620f79e36af49e213&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

[image](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/9ac543ed-3db5-4bc9-ac18-1f2f7f5c13a7/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RKYU4UFX%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T225448Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIHBaPbz70rEMbxYugeqcmePzJXih7%2BR8B%2BqYo0qQJ6ApAiEA8LDZ5Gi08dwbWHYoy1GcSor11SkVpbkgJEl%2FuBpIqt4qiAQIxv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDNFqz5QUsGOEtk6tcircA6WFMgYYcnyeOcz6mWZioggVTgzRc8ATQV2f7mBLcznNqhqC1bePcjR9l%2B%2BDnhH9TbFUikycSGq2hzf8Q5XBlxLdRzEP1Oneg557LAB9ltrebIFXcPkDiVlpc2NovAHNxDUXAFny353AfrM0%2BYTy3hUboEM4EGOHOCJLuLHsWrlqsdbod36Fc1ZduoqYHeopql57ljPF1p1G%2BLv4vEJWy8Ast5er%2BZ8UMOwLrsjqh9Mbp186NBsi9OgNHxqwN5p7%2BiY3uuAVRT3kb2rgVJRKcyfDuLUnKOK%2B5IKsc%2BQENIGa8jAOSGQFnWguqPelmnSQBjeeWmSabcpZusUlVu8Clf5eFpz%2BpbHHRXikdZlJz6nqcp4kAvV%2FSK%2BjbjKJDJKgHGB5uxpZJygtkEnppbVR8%2FcF9ahuR3sFlETGl5ma3EOHMnx8lwDPKSYoBLzo5HOb3qPEqrmLExkJJpnHYKyV8ReumwOhwgyLtNdiNKXk6G7vxS3NqCTWJF8raJPoIQUFgTDF2TWWbztK7gEF%2B3205DWQ00HujeUkUedrTryGTKQ66UGzFMlnpNpCQEWLeNIgL7ZTHznBct6NZVGDXLvnfI716JAVRbjuWIuF28rhT9wRoBbOttQQDaGlYjpVMLi4%2F9IGOqUB19stOzvcFdwZ1wPalYHBvS4yoqY8gvSiXs%2FkyBagJe61N1Pr4wdJV%2BXoF2Ny0sqpXInhrCY8A9IdWCPIGl1UhnfynYkewi9tkkuSXEkcQuRlNEe%2BZV0eIijsRP8HDHkWTUzuMjU%2FsT2pOQ2y7sSjfdLQh%2FITOVp38%2FFYy%2BASuscMZbfyelFTlv7Zn4i3GsdZVZp1qU9RqtCKjX2lz81%2FPEpINIVi&X-Amz-Signature=cc1bc363d4b278e8bc3624eee217e1793af57a09420d1a8af941447d4b94ac6e&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

hello 大家好，前面咱们已经学习了如何保证接口的幂等性对吧。然后咱们这节课看看如何在咱们的天天吃货的这个项目当中把接口幂等性的给它融入进来。咱们还是以订单这个接口作为实例。首先咱们看一下天天吃货的这个项目，它的订单接口有没有保证幂等性。好吧，咱们先进入 idea 然后把天天吃货的这个项目给它启动起来。启动成功了是吧？然后咱们再进入到 Tom cat 把前端的代码也启动一下，咱们选择 start up.bat 是吧。然后双击启动成功没有问题是吧。接着咱们打开浏览器，刷新一下天天吃货的这个首页。然后我们去登录，咱们还用这个泰斯的账号泰斯的账号去登陆登录，然后选择一件商品选择什么选择这个大龙虾，然后给他加入到购物车这块，有两个商品是吧，咱们删除一个，然后选中这个商品，点击去结算。


选中一个支付方式这块，一会咱们快速的去点击这个提交订单，看看后边他能够创建几个订单。咱们先把这个谷歌的调试模式给它打开，看一下它的网络请求。一会咱们抓一下这个创建订单的这个请求，看看它一共发送了多少个这块咱们快速的点击好成功了是吧。然后咱们看一下这个开发工具上面，咱们看看调用了两次 order create 是吧，那么它生成了两个订单是不是返回的斯蒂特斯都是二百，咱们再去数据库里边去。验证一下这两个订单，咱们还是进入到 navigate 打开132，132是 test 的这个账号是吧，咱们刷新一下这个数据库，咱们看看。这块是生成了两个订单是吧，咱们看一下订单的创建时间一模一样是吧，一模一样。看来咱们天天吃货的这个订单接口是不能够保证幂等性的。那么接下来咱们去看一看在程序当中如何去改造这个订单的接口。好，这个咱们浏览器就在这里边给关一下。


那么幂等性咱们怎么去保证呢？在前面咱们也已经提到过了，要在创建订单这个接口之前，也就是结算页咱们要返回一个 token 然后在提交订单的时候把这个 token 带上是吧，传到你的订单接口当中。然后我们再校验这个 token 确保这个偷看只能使用一次。


那么好现在咱们就去改造一下这块订单的这个接口，咱们还是进入到 order controller 那么在创建订单这个方法之前是吧，也就是结算页咱们要返回一个 token 是吧。那么这个返回 token 的这个接口还没有，咱们现在就在这个项目当中，可以写一下 public 返回的结果。


那么统一用这个慕课的反馈结果对吧？然后方法的名字叫做 get order token 是吧，然后注解加上这个链接咱们也叫做 get order token 好吧，注解的这个注释咱们也统一改一下，获取订单 token 他之前咱们课程当中给大家举的示例是前后端的页面是在一起的是吧，我返回这个 token 直接返回到页面。


那么有的小伙伴在看了这个视频以后，在问答区里给我读研说，如果前后端分离的项目，这个 token 我怎么去传？那么咱们天天吃货，它就是一个前后端分离的项目对吧？咱们就在这个项目当中，看看在前后端分离的这个场景下，怎么把这个偷看给它传到前端的页面获取。偷看咱们要怎么去写，咱们要保证这个 token 是唯一的是吧，那么这个唯一的 token 这块咱们也不用多考虑了，就使用 UUID 就可以了。


uuid.random [uuid.to](http://uuid.to/) string 是吧，然后咱们要把它存起来是吧。因为你前端在获取 token 的时候，我后端我要存一份，是不是说完以后呢？你在提交订单的时候把这个 token 带上，我在后端才能够去校验对不对？那么我这个 token 存在哪呢？咱们存在这个 Redis 里面， redis.set 那么这个 Redis 的 key 咱们用什么呢？那么这一块就要看你防这个接口的密导性，要防到一个什么力度是吧。


一般的情况下，我一个用户在一个浏览器当中登录，我就要防止我这一次会话，我用户在浏览器当中他创建订单的这个幂等性要保证就可以了。那么我如果一个用户在两个浏览器登录，在一个在火狐，一个在谷歌是吧，那么这个时候他们两个同时去点下订单，咱们应该是可以让他下的对吧？那么这个时候这个 key 咱们就是要使用 session ID 是吧，也是 TTP session 对不对？这样是不是就行了？我要防止的是一个用户在一个浏览器之内重复下单这个过程。如果你在多个浏览器，那认为是正常的对不对？这块就看你业务方去要求你实现的这个力度。


那么这个 K 咱们就用 session 的 ID 是吧，这块咱们这 Redis key 也要先加一个前缀，叫做 order token 好吧，下划线，然后接上咱们的 session ID 对吧，然后值就是咱们存的这个 token 这个重复提交，咱们防止住以后，那么这个 K 是不是就一直存在在这儿以后就用不到了。


那么这个时候怎么办？咱们这块给它设一个过期的时间，咱们设置成多少呢？设置成 30 秒，咱们点进这个 set 方法，看一下这个时间的单位是什么，看到这块写的注释时间是秒对吧，咱们传一个 30 是没有问题的。然后咱们把这个 token 要返回去返回给页面这块儿，咱们还统一用这个 JSON result return JSON result 点儿。 OK 然后传一个 token 这样就成功的返回给前端了是吧。然后咱们再去改造创建订单的接口。 token 返回去以后，用户在提交订单的时候要把这个 token 要带回来，他通过哪个参数去传呢？是不是要通过这个萨米的 order BO 对吧？那么咱们先在这个 semi 的 order BO 里边添加一个 private string token 是吧。


然后咱们生成 get set 方法，拿到这个 token 以后，咱们要去校验 Redis 里边有没有这个 token 先要拼这个 Redis 的 key 是吧，咱们这个变量叫做 order token key 好吧，它就等于 order token 加上一个 session ID session ID 呢 request.get session.get ID 对吧，然后咱们去 Redis 里面去拿它的值 Redis operator 第二 get get key 是吧，刚才咱们拼好的这个 key 传进来，前面接到的这个值就是这个 token 是吧，咱们这个名字叫做 order token 是吧，然后这里边咱们要去判断一下，先去判断一下这个 token 是不是为空是吧。例子 blank 如果 order 偷看等于空这块，咱们直接抛出一个异常 slow new run time exception 然后加上一个异常的信息。


order token 不存在。如果它不为空，咱们要比较一下 auto token 是不是等于 submit order BO 里边的 token 对吧。 get token 是吧。这个变量的名字我们叫什么？Correct 。 token 是吧，如果他不正确这块是不是咱们也不能让他去下订单？同样抛出异常 order token 这个错误信息不正确对吧？好，这一段的逻辑咱们再好好的看一下。


首先在结算页面，这个页面要获取这个奥德托肯是吧，这个奥德托肯咱们生成以后把它存在 Redis 当中，这个 Redis key 就用作 session ID 就保证这个浏览器的这一次话这个会话是不能够重复提交的对吧？然后咱们传了一个 30 秒对吧。然后用户去下订单，下订单的时候咱们也是根据这个绘画 ID 去拼出它在 Redis 当中的这个 key 对吧？然后我们把这个 key 取出来。那么如果这个 key 不存在的话，那么咱们抛出一个异常对吧？如果存在，咱们就要和前端页面传过来的这个 token 去比较一下，如果正确，咱们就能够去下订单。如果不正确，咱们再去抛出这个异常是吧。


抛出 order token 不正确对不对？这块咱们再看看，整个逻辑应该没问题，咱们再看看这个 30 秒是不是时间有点短？比如说我在结算页我停留超过了 30 秒，那么这个 Redis 当中的 key 就不存在了对吧？这个时候我再点击提交订单，就会走到这个 if 当中来。 water to 看不存在就抛出去了。这个时间咱们设长一点，咱们设置成多少甚至成 10 分钟。如果结算页你停留 10 分钟，再不提交警察，那么你只能再重新刷新这个结算页再去提交了是吧。我们把这个时间改成 10 分钟，10分钟就是 600 秒。那么这个后端的代码咱们就修正完成了是吧。接下来咱们再看看在前端的代码咱们要怎么去调整。



