---
title: 2-10 【Demo】改造项目结构-2
---

# 2-10 【Demo】改造项目结构-2

[image](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/7104de2c-bec2-455e-bbf0-af00549687ed/SCR-20240718-rcsh.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QSDYTQ6H%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T225625Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDKOEgnzWf8nSCmlUKsxv6w5w8MxHGqz3Zr1EOEksKtowIgJhq8mYNBa6%2BQ3Pq72QY0ONNAvgFMQf4EHFGzNW%2FUqKQqiAQIxv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDFboLLko0z0IfTo0ESrcA3fXL3kcDsk5RBAhL3o3xdPBspSr5oI3OUVE9bHAbavyzoiDOAKqbHv4U1rQr2qN3qcijbw%2BTIiJ4FzeXe0gYujs0guUH48WneeSC2kiLv9C%2FnObrfZZ3fKlSfpnssg2jyZS9Qg5kCqLYJBa44XgPkbJU7dOWGLy8ZaADEIWFpN5jkOl%2FDvXgHn%2Ft3GvvF8EFWX0kuoDhtKKewhcslnfXHKsahoT4AhkV0%2FWXO%2FYY27xj9tDEe%2F6EeDb94B1ky%2FPmPIZXFoS9961NhVMGguRqY2mKgEe0rwYsM1MJ6dk%2B%2BFtAhfxm7m5dYLPYMtET18rIh7Z%2FCCNWFGwNHEsC%2BN8BwDbRoLkIrMwh7tenGtbLwne4gkBqoSVEkqNLuzxi9fRsGnZtYC48aGkCD3Ql%2FyuFgcK6JzLzwIYPCCYdXPH45UnR8m8eUW7egYhrnxb9aVy7U7%2FVVmjvAt4WxTvFZJYtJ3Ut9S%2F9b%2FES%2BBbq9iUbxgy6qgwRaiaiyg7%2F%2F8hpMPSuDlIeC6X36PH5tRCKxlr%2BxyceQIM0j6DKT1GCNqARUJQ7YEcYv1F0azYE28CEIQzbEej7Q7P%2B2k%2BfiVsPOUnTo0dBXqPxinBiBsEImuO7ScOrsGDF5%2Bw3IdojJYNMJ63%2F9IGOqUB36Y1VD0cR0yP0Gdzf98%2B%2BI7ck938FJg2by%2B3NedPLEf7Rih1nGs4sEjattI27LvJCb%2BPwtDEIDhx%2BbwHNp5XFx6GZB%2Bj65%2F5Y8Sr1tV07%2BJwWW0YtIua5rGOYjvE3NLWcmBwlrUEXGe56rxlwogCOIdsE3PaiqAYTBWcYNOAvMPgN9tK03Qrb5EnIG6XY33Mgw800iRlcLwWvmsSJwOt5OStSvuf&X-Amz-Signature=38e6d588ba29598ac85f956634a31fe8202ece8fa5afbf810efd414315b1c2e9&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

[image](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/801c8aed-c0b6-4366-8f83-8d815a023f3d/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QSDYTQ6H%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T225625Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDKOEgnzWf8nSCmlUKsxv6w5w8MxHGqz3Zr1EOEksKtowIgJhq8mYNBa6%2BQ3Pq72QY0ONNAvgFMQf4EHFGzNW%2FUqKQqiAQIxv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDFboLLko0z0IfTo0ESrcA3fXL3kcDsk5RBAhL3o3xdPBspSr5oI3OUVE9bHAbavyzoiDOAKqbHv4U1rQr2qN3qcijbw%2BTIiJ4FzeXe0gYujs0guUH48WneeSC2kiLv9C%2FnObrfZZ3fKlSfpnssg2jyZS9Qg5kCqLYJBa44XgPkbJU7dOWGLy8ZaADEIWFpN5jkOl%2FDvXgHn%2Ft3GvvF8EFWX0kuoDhtKKewhcslnfXHKsahoT4AhkV0%2FWXO%2FYY27xj9tDEe%2F6EeDb94B1ky%2FPmPIZXFoS9961NhVMGguRqY2mKgEe0rwYsM1MJ6dk%2B%2BFtAhfxm7m5dYLPYMtET18rIh7Z%2FCCNWFGwNHEsC%2BN8BwDbRoLkIrMwh7tenGtbLwne4gkBqoSVEkqNLuzxi9fRsGnZtYC48aGkCD3Ql%2FyuFgcK6JzLzwIYPCCYdXPH45UnR8m8eUW7egYhrnxb9aVy7U7%2FVVmjvAt4WxTvFZJYtJ3Ut9S%2F9b%2FES%2BBbq9iUbxgy6qgwRaiaiyg7%2F%2F8hpMPSuDlIeC6X36PH5tRCKxlr%2BxyceQIM0j6DKT1GCNqARUJQ7YEcYv1F0azYE28CEIQzbEej7Q7P%2B2k%2BfiVsPOUnTo0dBXqPxinBiBsEImuO7ScOrsGDF5%2Bw3IdojJYNMJ63%2F9IGOqUB36Y1VD0cR0yP0Gdzf98%2B%2BI7ck938FJg2by%2B3NedPLEf7Rih1nGs4sEjattI27LvJCb%2BPwtDEIDhx%2BbwHNp5XFx6GZB%2Bj65%2F5Y8Sr1tV07%2BJwWW0YtIua5rGOYjvE3NLWcmBwlrUEXGe56rxlwogCOIdsE3PaiqAYTBWcYNOAvMPgN9tK03Qrb5EnIG6XY33Mgw800iRlcLwWvmsSJwOt5OStSvuf&X-Amz-Signature=1bf008098eb87e06173f18cc3afdcfd88b1070f8fe7041208a62b34a927695cf&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

[image](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/4009a2dd-6a9e-4e3c-b8c6-28bc56de11d7/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QSDYTQ6H%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T225625Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDKOEgnzWf8nSCmlUKsxv6w5w8MxHGqz3Zr1EOEksKtowIgJhq8mYNBa6%2BQ3Pq72QY0ONNAvgFMQf4EHFGzNW%2FUqKQqiAQIxv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDFboLLko0z0IfTo0ESrcA3fXL3kcDsk5RBAhL3o3xdPBspSr5oI3OUVE9bHAbavyzoiDOAKqbHv4U1rQr2qN3qcijbw%2BTIiJ4FzeXe0gYujs0guUH48WneeSC2kiLv9C%2FnObrfZZ3fKlSfpnssg2jyZS9Qg5kCqLYJBa44XgPkbJU7dOWGLy8ZaADEIWFpN5jkOl%2FDvXgHn%2Ft3GvvF8EFWX0kuoDhtKKewhcslnfXHKsahoT4AhkV0%2FWXO%2FYY27xj9tDEe%2F6EeDb94B1ky%2FPmPIZXFoS9961NhVMGguRqY2mKgEe0rwYsM1MJ6dk%2B%2BFtAhfxm7m5dYLPYMtET18rIh7Z%2FCCNWFGwNHEsC%2BN8BwDbRoLkIrMwh7tenGtbLwne4gkBqoSVEkqNLuzxi9fRsGnZtYC48aGkCD3Ql%2FyuFgcK6JzLzwIYPCCYdXPH45UnR8m8eUW7egYhrnxb9aVy7U7%2FVVmjvAt4WxTvFZJYtJ3Ut9S%2F9b%2FES%2BBbq9iUbxgy6qgwRaiaiyg7%2F%2F8hpMPSuDlIeC6X36PH5tRCKxlr%2BxyceQIM0j6DKT1GCNqARUJQ7YEcYv1F0azYE28CEIQzbEej7Q7P%2B2k%2BfiVsPOUnTo0dBXqPxinBiBsEImuO7ScOrsGDF5%2Bw3IdojJYNMJ63%2F9IGOqUB36Y1VD0cR0yP0Gdzf98%2B%2BI7ck938FJg2by%2B3NedPLEf7Rih1nGs4sEjattI27LvJCb%2BPwtDEIDhx%2BbwHNp5XFx6GZB%2Bj65%2F5Y8Sr1tV07%2BJwWW0YtIua5rGOYjvE3NLWcmBwlrUEXGe56rxlwogCOIdsE3PaiqAYTBWcYNOAvMPgN9tK03Qrb5EnIG6XY33Mgw800iRlcLwWvmsSJwOt5OStSvuf&X-Amz-Signature=1788a047282fc64b71e9cf92b65c43fb9700b304710d86a801295e1843301a67&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

[image](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/7afd2232-0d93-4e25-b6c3-1d741e36ce55/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QSDYTQ6H%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T225625Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDKOEgnzWf8nSCmlUKsxv6w5w8MxHGqz3Zr1EOEksKtowIgJhq8mYNBa6%2BQ3Pq72QY0ONNAvgFMQf4EHFGzNW%2FUqKQqiAQIxv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDFboLLko0z0IfTo0ESrcA3fXL3kcDsk5RBAhL3o3xdPBspSr5oI3OUVE9bHAbavyzoiDOAKqbHv4U1rQr2qN3qcijbw%2BTIiJ4FzeXe0gYujs0guUH48WneeSC2kiLv9C%2FnObrfZZ3fKlSfpnssg2jyZS9Qg5kCqLYJBa44XgPkbJU7dOWGLy8ZaADEIWFpN5jkOl%2FDvXgHn%2Ft3GvvF8EFWX0kuoDhtKKewhcslnfXHKsahoT4AhkV0%2FWXO%2FYY27xj9tDEe%2F6EeDb94B1ky%2FPmPIZXFoS9961NhVMGguRqY2mKgEe0rwYsM1MJ6dk%2B%2BFtAhfxm7m5dYLPYMtET18rIh7Z%2FCCNWFGwNHEsC%2BN8BwDbRoLkIrMwh7tenGtbLwne4gkBqoSVEkqNLuzxi9fRsGnZtYC48aGkCD3Ql%2FyuFgcK6JzLzwIYPCCYdXPH45UnR8m8eUW7egYhrnxb9aVy7U7%2FVVmjvAt4WxTvFZJYtJ3Ut9S%2F9b%2FES%2BBbq9iUbxgy6qgwRaiaiyg7%2F%2F8hpMPSuDlIeC6X36PH5tRCKxlr%2BxyceQIM0j6DKT1GCNqARUJQ7YEcYv1F0azYE28CEIQzbEej7Q7P%2B2k%2BfiVsPOUnTo0dBXqPxinBiBsEImuO7ScOrsGDF5%2Bw3IdojJYNMJ63%2F9IGOqUB36Y1VD0cR0yP0Gdzf98%2B%2BI7ck938FJg2by%2B3NedPLEf7Rih1nGs4sEjattI27LvJCb%2BPwtDEIDhx%2BbwHNp5XFx6GZB%2Bj65%2F5Y8Sr1tV07%2BJwWW0YtIua5rGOYjvE3NLWcmBwlrUEXGe56rxlwogCOIdsE3PaiqAYTBWcYNOAvMPgN9tK03Qrb5EnIG6XY33Mgw800iRlcLwWvmsSJwOt5OStSvuf&X-Amz-Signature=d36b05afa5b823c1314e0b9ca4351436f86e1e5d909b1a0c6628190ff4740a81&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

hello 慕课网的各位同学们，大家好，眼保健操作完了没有？那我们开始进入下半场的课程了，下半场比上半场简单太多了。这里我们用超快猛的方式创建一个毛九，大家跟上我的节奏，不要眨眼，左手右手一个慢动作，右手左手慢动作回旋。它的 artifact 叫 thing consumer 后面还要再加一个对不对？我们已经有一个 consumer 了，我们给它叫 advanced 改进版的 consumer 好不好听，接下来名字和前面保持好一致。然后把这个项目依然放到 fin 的文件夹下。


好，点击 next 这个 pom 配置起来，那就相当简单了，我们只用 copy 就好。找到 client 我们把 client 里面已经写好的内容给它 copy 进来，这些 dependency 我全要 all in 除了这些，还有些没有额外的dependency ，没有了，同学们这些就是全部的 dependency 了。


我这里再提一个小的tips ，也就是说如果你引用了的这个分 client 它的版本怎么样呢？它的分版本比你要高或者比你要低，导致你这里不兼容。有什么办法呢？大家应该都非常熟悉了，exclusion把他的份依赖从这里面剔除出去，然后怎么样呢？然后自己重新引入一个新的份依赖。也就是说你在接口中假如你像我们这个接口一样引入了 fin 的依赖。那么你要想到这样一种情况，你引入了这个份依赖不一定和客户端的版本一致。它有可能高有可能低，如果你都在一个公司，那是很好解决。


那假如你是提供给外部的第三方用户来访问，我建议大家怎么样呢？要么把份依赖从接口层删除，要么让客户端使用我前面说到的那种方式，把这个份依赖从你的依赖项目中给他 exclude 出去，再重新引入一个自己的依赖。 OK 好，我们接下来就进去写代码。一个如雷贯耳的包名叫什么？大家要记住这里面的关键词 I mock.spring clotok 一个入口类，它的名字我们依然给它起名叫做 thin 


consumer application 前面说到我想让他名字变得短一点，太长了就叫 App 好了，然后它的内容我们怎么样从别的地方 copy 过来？好，这里直接把它 copy 过来。除了这个内容以外，上面三个注解应该也是完全相同的。这哥仨三个注解我全要同样给它 copy 过来。好，这入口类就超快猛地创建好了，紧接着我们要创建一个 controller 对不对？大家看 controller 可不一样了，这个 controller 相当的简便。起名 controller 同样要怎么样？ rest controller 对不对？这些 innovation 的名字大家应该都可以背下来的。


剩下一步，这里要继承谁呢？他不是光杆司令，他此刻不是一个人，他要继承谁大家被我忽悠住了，他谁都不要继承前面继承的是谁是 service provider 对不对？我一个调用方，我干嘛要继承你的接口层，我直接把它引入进来。好嘞对不对？它的 private 类型的 iservice 然后给他 annotation auto wired 进来。


这里为什么可以 out wider 它进来？大家有没有思考过这样一个问题，因为我的 I service 看它的包名是谁，come.i mock.spring cloud 对不对？前面我们学到了 fen 的加载方式，那大家还记得吗？这个 fen 当你没有指定后面的参数的时候，它会怎么加载？它会尝试把你当前的闷方法所在的包路径下的类扫包加载进来。那你这相当于正好赶了一个巧，你的接口层正好也在同一个包下。那假如说你的接口层是另外一家公司提供的，怎么办呢？两个方法，要么你在这里把扫包路径给它配上，让其他的包也能被粪扫到。


要么我们怎么样？我们用这种方法新建一个 public interface 叫 my service extend eye service 好用这种方式我们在上面加上一个份注解，然后给好 value 等等，也可以将第三方的粪接口引入进来。两种方式都可以扫包可以添加注解，我个人偏向于添加一个分 client 注解，因为这样相对来说更灵活。后面我们将学习到 high streaks 的容错服务降级。那这种方式配置起来比上面扫包的灵活性可要更高了，你可以随意控制很多不同的参数。


那我这里要提醒大家一个可能会遇到的小坑，如果你在我们 spring cloud 最新的 G 版上面声明了这样一顿操作，一顿猛如虎的操作它会报错。因为为什么你的 I service 是不是已经被扫包扫进来了？但是你扫进来之后，它这个上面有一个分 client 注解，你在它的子类接口上又生命一个分 client 注解。那你在 spring 的上下文当中就有两个 iservice 类型，out wide 的，他知道 out wide 的谁吗？不知道。而且你在子类中覆盖了父类中的注解。在最新的 G 版里面，这种做法是不被允许的。那 F 版里我们怎么来解决呢？ F 版里我们用 primary 等于 true 告诉他什么，我是带头大哥， my service 是老大，下次如果谁要 out wide I service 类型的，那就是我 my service 但是在 G 班里面这一套行不通，大家可以尝试着去启动项目，看一下它的报错。


那 G 班里面怎么办呢？等于我们来看有一个配置文件可以包治百病，这个配置文件它的属性就是允许注解的重载，它叫什么呢？ spring man.all of a bean definition over riding 两个 R OK 那它的值是什么？我既然允许重载，它的值就是 true or false 那你声明了这样一个属性之后，你上面的这段代码在 App 中声明的这段代码就可以正常的工作了。那这是 G 版里面的一个坑，大家要注意。所以很多同学从 F 版升级到 G 版的时候，会发现有些 fin 它会启动报错，大概率可能就是这个原因导致的。
好踩坑指南说完了，那我们就继续后面的内容喽。 OK 那这里我什么都不要 control 了，层注解进来，你总要用对不对？不能把它干放着资源浪费。我们借鉴一下现有的分 consumer 好了，非常简单， copy 过来，再把它粘贴过去，这样一个方法就创建完成了。我这里为什么需要 annotation 大家知道虽然也是 say hi 但是和刚才的 service provider 也就是分 client 是完全不同的含义。我这里是作为服务调用方，也没有继承自拟的接口，所以我当然需要配置一个 get mapins 喽。有了第一个，我们再给它配置一个 post 形式的 toast mapping 依然也叫 say hi 那它返回一个 friend 返回 friend 当然是要调用 service 的 see high post 这个接口同时传入一个 friendfriend 朋友一生都离不开的人，恋人，最后也会成为朋友的同学们。 Set name test. Alright, but I'll try and ship.


好静候佳印。那 ctrl 的层已经写好了，接下来写谁配置文件对不对？好，我这次换个方式，把 copy paste 做到底，从前面把这个 application properties 也给它 copy 进来。那我的端口号给它起名叫40,003，它的 name 叫分 consumer advanced advanced 是高级版的意思。那我接下来还等什么呢？可以直接启动了对不对？好到闷方法里把它启动起来。 spring 标签成功了，一半往下走走 321 出来成功完美。接下来的剧情大家应该都知道了。打开 postman 把端口换成40,003，一个深情的问候。


Get how are you.
你看他返回了 this is 40,002 说明什么，说明整个链路是完全通畅的。那 post 这里我们要把前面的请求都给删掉，发送一个 name 是 test 也就是我们传给他的 name 那整个链路都已经搭建完成了，同学们有没有觉得跟前面相比方便了很多我的 controller 层清清爽爽。那反观前面我们的分consumer ，你看它的 service 好臃肿，它不光要定义每个 service 还要定义它的 get mapping 那我这里烦恼都没有了，用起来简直就像 rp C 框架一样清清爽爽，赏心悦目。


好。那到这里，我们整个的分项目改造环节就宣布结束了，老城区改造计划圆满成功。那下一个课程老师要还一些旧账了，什么旧账，还记得瑞本里面我们落下的虫是吗？好，接下来就让大家通过图文还有小 demo 了解一下怎么在 fin 中配置重试策略。同学们，我们下期节目再见。



