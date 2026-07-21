---
title: 1-8 【技术落地】接口幂等性方案落地与测试
---

# 1-8 【技术落地】接口幂等性方案落地与测试

[image](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/3d47a421-3b10-4909-94f2-742839aaf3dc/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZMVKODRR%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T225448Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDxb3qlq4MOCpsrcvacyX0OfOKYiV9xfpltIRobbM3onQIhAPJKjLn3Jw1y1cS4YeJY1GEYJF7MtFoY4E2yjnfJ3r5ZKogECMb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1Igx%2BiB3URq54EGeq68Iq3AOTUXN2dtLAMJxJrDBycCrQi3tWVoCpwQ85jMK9RHtm5JJNtjwSec3jA19%2BXKZzWyn4aPKXpSI%2Bp87VR66B25vJy3euVdp%2FvQiVbVFKekcgULRVB40zFbQwtq8X%2BEp8HQMF90TSrWTloasI93WKATTq2uY2u2xu8eMvpfA6ur%2FMLkfhEIIJ5oHSJ2TtHE0RVEvwJ%2F6dF%2BoMTQZ1DU8lDfSnH%2FiIzomgXCRkL%2BDDcpVKsCw95Na6eDF9GRGQ8BB0EQo6iAfYkehQ8dpNSeTT92uKcexoYSOEfarSFjyRHS7In32eUVNeLlOmq9DqmNHjlznWcIIZHbR0PrK4lrMblOL8GCnxlOn1GFXHi2U6i9fLQiXNKpjbfB%2BmsB1sWaziXcmkalkyivdaBGVruNeULE0PDS48bHhdcwpNwSZjZS%2FhqnfDed5IfJMJZgWiroQ5EjEAndHeIL6NHK0TufV2tnrTLzdMe%2F%2BByXs9N1tO45L2CWQvrktGJMEevAJenAYMoAWz6RGgXBle39t2CHxvUlqSUkc9mdBpMzay2XG3NW%2FiNFXto9FGkRLNPZZKOxu4z9MQk9k9rANlAUytm%2FuB0ufLpHIB%2B%2FzfaPOV%2FYO9IFwXE7tvdm3nFNYHC0dIsjDauv%2FSBjqkAQq44EqQsMIWjZUDvuTVXQLBvqTUmtRkDD1Na6KAzA0ir8jOYcXR4sJNbqQ00uQmav9iqi2ypTHlATLBv2byOIE4RSOMRYlFj0BfAN1WiUtc5MavlSTLfOtyd7MIO2GKrzyIJKDRbybZDFR10qsRUABWBv1SmvDBed1D4FbpmsB4w5fuEy%2B3DyXn1DMMvzxdLlIyFFl0bFn8CLBH6iaNhkaasyQY&X-Amz-Signature=d3478d4b2ea6ebc2492e73ff466b28e25a7adfa4437ff26589e088e408faaa73&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

在代码之前，咱们再看看这段逻辑，感觉上还是有问题是吧，这问题是什么呢？就是在重复提交的时候，第一次正常的提交走到咱们的这个创建订单的方法，去 Redis 当中获取这个 token 这个 token 是存在的，并且也是正确的。第一次请求就会执行后边创建订单的方法。这个重复提交的第二次请求过来以后，他还会去 Redis 当中获取这个 token 那么这个 token 是不是也存在啊？那么后边是不是也能执行创建订单的方法？是不是这条逻辑就有问题了。


这块咱们要在判断 token 正确之后，要把这个 token 给它删除掉。那么删除掉以后，第二次请求过来以后，这个 token 就获取不到了，咱们只能保证这个 token 被消费一次。这块咱们还是使用 Redis operator.delete 然后把咱们的这个奥德 token key 给它删除掉，这样是不是就 OK 了。第一次请求这个 token 存在并且正确对吧？然后咱们创建订单，并且把这个 token 给删除掉了。那么重复提交的第二次请求过来以后，再获取这个 token 的时候就获取不到了，那么异常就抛出来了，这个没有问题。那么咱们再考虑一种情况，就是在创建订单的时候，如果你第一次请求就并发的过来会是什么情况？两个请求同时去外地词当中去获取这个 token 都获取到了 token 并且 token 存在并且正确。


那么后边是不是又是能够创建订单了？在并发的时候还是不可以对吧？那么这块咱们要加上一个分布式锁，咱们把 radiation client 引入到这个 order controller 当中， private ready 是 client 是吧，然后自动注入这块，咱们使用它的分布式锁对吧？第二 get lock 这个 key 的名字咱们使用什么呢？也使用这个 order to 跟 key 都可以是吧？咱们保证了是一次会话要加上这个锁对不对？在同一浏览器，如果你多次提交并且是并发的提交，那么只有一个请求能够执行下面的这段逻辑对不对？所以咱们把这个 order to 跟 key 给它挪到前边来，然后获取这个锁。


获取锁之后咱们 lock 一下是吧。然后传入一个这个锁的有效期是吧？有效期，咱们这个创建订单的方法怎么 5 秒也应该能够结束了？这个锁的有效期是 5 秒，然后后边 time unit.second 没有问题是吧？这块是加锁对吧？那么咱们这个释放锁是在哪里释放呢？是不是？在进行这个 token 判断之后，咱们就可以去释放那个锁了对吧？那么前面那个时间 5 秒，那么显然是绰绰有余的对不对？然后这块咱们不管他怎么样加上一个踹，不管它执行结果如何，最后咱们都要去把这个锁给它释放掉，这样是不是就 OK 了？咱们再捋一下这个逻辑，并发的去请求下订单的接口，然后咱们先要对这个 old token 去进行加锁对吧。


锁住之后，咱们去 Redis 当中去判断 token 是不是存在是不是正确。如果存在并且正确，那么咱们就可以去执行后边下订单的操作，如果不存在不正确，咱们就直接抛出异常了。那么并发来的第二个请求在这里边会给它锁住对吧？锁住之后，等待前一个请求执行完以后，它才能去执行这一段代码。他在执行这一段代码的时候，在 Redis 当中去获取这个 token 是获取不到的，那么异常抛出来后边创建的订单的方法也就不会去执行了，是不是这样是不是就能够保证接口的幂等性了？咱们再 review 一下这段代码。


这个在获取锁的方法的时候，这个是不是咱们怎么传进来一个字符串是吧，咱们应该用它对吧，这样是不是就 OK 了，咱们来看看，在这里边你的这个锁的 key 和你这个 token 的 key 使用一个这个是不是也有点问题。那么你的锁的 key 和这个 token 的 key 使用一个，那是不是就混淆了？那这块咱们还是要改一下，这个咱们叫做什么呢？叫做 lock key 。


好吧， lock key 然后加上 session ID 对吧，把它传到这个 ready 申 lock 当中，这样是不是 OK 了？下面咱们再去看看，前端的代码咱们直接在这个 term cat 当中去修改，进入到 web App 进入到 for day shop 咱们看看这个页面是哪一个页面，咱们把这个后端的项目给它启动一下，然后前端咱们找到这个订单结算页是吧。这个是购物车页，咱们选中商品，点击去结算，看看前面的链接。显然它是配点 HTML 是吧，咱们在这个团木开头当中找到配点 HTML 我这里边也没有装什么前端的开发工具，咱们就使用 note pad 去改一下。


好，这个就是咱们的结算页，它也是使用 VOE 去做的对吧，咱们看看这个提交订单是在哪块去进行的。然后咱们主要看一下 Vue 的这段 GS GS 里边这个 date 就是需要传递的参数对吧，然后 watch 是一个观察器，这个咱们也不用管它后边跟着 create 是吧，就是页面加载成功之后，咱们要执行的一些方法。咱们看看这块有渲染订单的信息渲染订单的地址是吧，都在这里边。那么在这个页面咱们要获取一个 token 那么这块是不是咱们要加一个方法获取订单 token 是吧，这个方法咱们也照着前面去写一下 get order token 对不对？这个方法还没有，咱们也是参照前面的方法是吧，写一下这个获取挺难 token 的方法，这个方法就是渲染收货地址的，咱们同样写上一个 get order token 是吧，在这里边咱们也有一个请求的地址是吧，咱们就直接把后边的这一段给它复制过来。首先是一个 server 的 uil 是吧，然后后边跟上一个 pose 的请求咱们把这段直接复制过来。这个 pose 的请求咱们是不需要 header 的，后边这个参数咱们是不需要的。后边的这个逗号咱们也给它删一下，这块咱们只留一个链接是不是就可以了？这个链接咱们再回到 idea 当中，把这个点击复制一下，再回到 node pad 这个地址是 orders 是吧。


然后 list 咱们给它改成 get order token 后边的参数不需要对吧？然后就是这个镇执行成功以后，咱们要把它存到一个变量当中是吧，咱们先把这个给它补全，要给它存到一个变量当中。这块咱们也是参照后边的写法去写一下，如果 redis.date.status 等于200，咱们再去进行这个 token 的存储。 else 这块咱们直接写个alert 。 order token 获取失败成功之后咱们要进行赋值。这块咱们这个还没有存这个 token 的地方是吧，咱们再往上看，看到这个 date 这一段，这个是不是就是 VOE 存储它的值的地方。这块咱们要加一个参数，这个参数要和咱们后边 submit order BO 里边的这个名称要对应起来是吧。它叫 token 咱们复制一下回到 note pad 这块叫做 token 然后它的初始值没有就是一个空对吧？然后咱们再回到获取订单 token 的这个方法这块，咱们就使用 this.token 等于 rise.date 后边跟它变量名是什么？咱们再回来看一眼，咱们这个 get auto token 的方法直接是 jcn result.ok 是吧，咱们点进这个。 OK 看一眼这个 OK 是不是就是这个里边的 date 字段对吧，咱们复制一下再回到前边这样是不是就可以了？ this.token 等于 res date.date 对吧。


好了，这个 token 值获取成功了，然后咱们再看提交订单的方法，搜一下。 great 好找到了，这个就是提交订单的方法。 submit order 然后咱们看看他传参的时候传了哪些参数，这个是订单的地址，然后这一块就是他传递的向后台传递的参数是吧。这块咱们要把这个 token 给它加上对吧，看看这个变量是从哪来的，这个变量在前面都有定义是吧。那么咱们这个 token 也在这里边定义一下，哇， token 等于 this 点 2 token 这样是不是就 OK 了，一会咱们试一下。好，这块咱们还是写上 token 保存一下是吧。


好，这块应该咱们整个的逻辑就写好了，咱们回到浏览器 ctrl f5 强刷一下。嘿报错了是吧，这个肯定是有错误的，咱们看一下，看一下报错看一下这个 control 看看报什么？错。 855 行这块少了一个单引号是吧，再回到这个 notepad 再找到这个 get token 这个方法。 get token 这块，把这个单引号咱们给它补上，再保存一下。回到浏览器，这回咱们再请刷一下，这回没有问题了是吧。然后咱们查看一下这个页面的 token 存的到底是多少，咱们还是进入到这个 console 里面，这块咱们怎么查呢？使用 this 点后边，跟着这个变量，咱们再回到 waterpad 看看这段 Vue 它起的是什么变量这块。哇。 index 点牛 UE 是吧，那它的这个变量就叫做 index 咱们回到浏览器 G 四点 index.token 咱们看到，有值了是吧，这个值已经带到了前端的页面，对不对？然后咱们再点击提交订单，咱们在后端打一个断点，回到 idea 咱们在这个创建订单的方法这里边打上一个断点，然后再回到浏览器点击一下提交订单。好，这个断点断住了是吧，然后咱们一步一步的往下走。


第一步获取的是 order to 跟 key 对吧？这个是用咱们的 session ID 没有问题，然后继续往下走。 log key 也是 log key 的一个前缀，加上一个 session ID 没有问题对吧，然后获取锁的时间是 5 秒钟对吧，然后咱们再继续往下走。奥德托肯获取到了，然后继续判断是不是为 true 那么和前端提交过来的这个 token 的值是一致的对吧？然后咱们把这个值给它删除掉。


最后 unlock unlock 这块报错了是吧，咱们，看看报什么错，咱们把这个错误给它放过去看看报什么错？咱们来看一下。他说这个锁并不是当前线程锁住的，那是不是这块这块这块咱们的这个锁的有效期是 5 秒，因为刚才咱们使用了断点，所以在 5 秒之内并没有走完这一段程序，那么它释放锁的时候就报错。
那么这一块是不是咱们在这 final 里里边也要加一个 try catch 对吧，再加一个 try unlock 然后 catch exception E 这块咱们开始数异常以后就不往外抛了是吧，因为它是释放锁的时候出现了异常，这个咱们就不用去管它了。


好吧，通过咱们前面打断点看，这段逻辑是没有问题的对吧。然后咱们现在再重新下一单，看看能不能正常的去生成订单，刷新一下这个结算页，然后点击提交订单，选一个支付方式提交订单没有问题是吧，正常的下到订单了，怎么把这个页面再给它关上，再重新选择一个商品。


这次咱们还是，快速的去点击这个提交订单，看看这个接口发送了几次请求是吧，咱们先把这个控制台先准备好，然后再回到 idea 当中，把这个日志咱们也统一的给它清一下好，都准备好了是吧，然后快速的点击提交订单，回到这个控制台咱们看看。一共发送了三次请求对吧，咱们再回到 idea 里边，咱们先把这个页面先给它关掉，看看前面报的错都是什么错误。


看看报错了是吧，奥德 token 不存在，再看看第二个请求也是奥德 token 不存在，说明了咱们这段逻辑是没有问题的对吧，从而保证了接口的逆等性。好了，到这里，咱们这块密斗性就已经整合到了咱们天天吃货的项目当中。好，这次的视频就先告一段落。







