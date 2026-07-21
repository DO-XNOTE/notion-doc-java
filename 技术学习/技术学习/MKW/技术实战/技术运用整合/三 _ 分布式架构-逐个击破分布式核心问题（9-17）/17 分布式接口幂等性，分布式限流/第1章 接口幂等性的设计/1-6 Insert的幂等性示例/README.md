---
title: 1-6 Insert的幂等性示例
---

# 1-6 Insert的幂等性示例

[image](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/5874f46f-4386-4a81-a3c1-cf83f9914640/SCR-20240808-gxal.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662SO4RQDJ%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T225447Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIDKmo9BnEQKEF6IjVsFk1W0u8yzKHaJ60%2FikoGtutZrEAiAUS1ZdXSEbbzO%2FH66%2FzhVR1vbAcpDYiWRAPZUITpSdMSqIBAjG%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMnRtdrUe9fem3sLbbKtwDCNLqWMbQ0%2BS%2FWUXlh2pTUJPgK2B6kZCrzx4jiD3VHrHwH%2FQO8%2FLhLzBJdNy%2Bieo48S6M9vXX9huPckUDxGkv7VDuNvcShMAcIWDldRfZNR9ZMl%2B%2Bey6p9qQc%2BL8NIxtgGt40kTyDYzvxsorTR96jNqs8BHaRl1ngqGdGOBEb0CtkliWmZheen%2B%2F44k3komitDFNno2w3t3mBbdSuVCx%2BcibXTCElacULwTyZtpxuyNyT9L86XTkYv0tAUM6PmpcI2MipFLVZO6WJbH5M35YUg%2Fhy0rJl4ZIGWMO3Qy5kICZ%2BhFl55mhXyAwP354sC%2BM6TdBGUUtf6HNk4wJZsK8fLx%2FAJ6g3g3NPaKmSNutgxasLvgfzZjDkooPNlU9BreQPZK924HL%2FA3fSpURg1EvuhcwRJKU4uiSaUQCNMzMv7731iHktyLqHNVBFM1J0MeIDRmmvI%2BriSmK3gDwlRAGQSa6yZpx5HFFZli4MB32XcGLvoVJWbcjxhAJ5CM1Gty%2Fd38e7UKD7vSEYpRP6SO7i53QyrhyNO0H3HDc8IBay453LGU%2FfJHNUvwa5BVxPO8ObJR9xUMJSpnVxko0MiumWUnjOi34uZU0Z4ZOqwQtl7vmdm5u2iXEqkrDSajgw7Lf%2F0gY6pgE%2FV4TyRoWLH6jw8hza%2FhcKrujzIPBNAq3FXXozOJZcl%2F6S5GjCLYbiYP9DRIhCMVhXMd3z3tcF0TOMuGMTCilJEOraCt0Ha6JI2grYltFRQgIwtwLMxY27MKRMvusBpaATH6eO0L1u3q1v65X7JIGuJHlJANaH%2F31QHo73E%2FV3x6yiLFrbQhc2Gt0PbYbxdTsQKs7FFtglb0FP%2F2O4JYg24RyPj0L9&X-Amz-Signature=33113c1399cc6c889427184d0f5c97ce434dff0e7bc096738d352bcf6f435cb6&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

[image](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/a7294125-0db7-4a9f-8de3-58534c61de39/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662SO4RQDJ%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T225447Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIDKmo9BnEQKEF6IjVsFk1W0u8yzKHaJ60%2FikoGtutZrEAiAUS1ZdXSEbbzO%2FH66%2FzhVR1vbAcpDYiWRAPZUITpSdMSqIBAjG%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMnRtdrUe9fem3sLbbKtwDCNLqWMbQ0%2BS%2FWUXlh2pTUJPgK2B6kZCrzx4jiD3VHrHwH%2FQO8%2FLhLzBJdNy%2Bieo48S6M9vXX9huPckUDxGkv7VDuNvcShMAcIWDldRfZNR9ZMl%2B%2Bey6p9qQc%2BL8NIxtgGt40kTyDYzvxsorTR96jNqs8BHaRl1ngqGdGOBEb0CtkliWmZheen%2B%2F44k3komitDFNno2w3t3mBbdSuVCx%2BcibXTCElacULwTyZtpxuyNyT9L86XTkYv0tAUM6PmpcI2MipFLVZO6WJbH5M35YUg%2Fhy0rJl4ZIGWMO3Qy5kICZ%2BhFl55mhXyAwP354sC%2BM6TdBGUUtf6HNk4wJZsK8fLx%2FAJ6g3g3NPaKmSNutgxasLvgfzZjDkooPNlU9BreQPZK924HL%2FA3fSpURg1EvuhcwRJKU4uiSaUQCNMzMv7731iHktyLqHNVBFM1J0MeIDRmmvI%2BriSmK3gDwlRAGQSa6yZpx5HFFZli4MB32XcGLvoVJWbcjxhAJ5CM1Gty%2Fd38e7UKD7vSEYpRP6SO7i53QyrhyNO0H3HDc8IBay453LGU%2FfJHNUvwa5BVxPO8ObJR9xUMJSpnVxko0MiumWUnjOi34uZU0Z4ZOqwQtl7vmdm5u2iXEqkrDSajgw7Lf%2F0gY6pgE%2FV4TyRoWLH6jw8hza%2FhcKrujzIPBNAq3FXXozOJZcl%2F6S5GjCLYbiYP9DRIhCMVhXMd3z3tcF0TOMuGMTCilJEOraCt0Ha6JI2grYltFRQgIwtwLMxY27MKRMvusBpaATH6eO0L1u3q1v65X7JIGuJHlJANaH%2F31QHo73E%2FV3x6yiLFrbQhc2Gt0PbYbxdTsQKs7FFtglb0FP%2F2O4JYg24RyPj0L9&X-Amz-Signature=fa899520766fcf0bc656e4927eeaf8f97791ce173cec753a1273b25a331236f7&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

[image](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/bce05d24-0b98-4812-89a5-3ae434e40b1e/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662SO4RQDJ%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T225447Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIDKmo9BnEQKEF6IjVsFk1W0u8yzKHaJ60%2FikoGtutZrEAiAUS1ZdXSEbbzO%2FH66%2FzhVR1vbAcpDYiWRAPZUITpSdMSqIBAjG%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMnRtdrUe9fem3sLbbKtwDCNLqWMbQ0%2BS%2FWUXlh2pTUJPgK2B6kZCrzx4jiD3VHrHwH%2FQO8%2FLhLzBJdNy%2Bieo48S6M9vXX9huPckUDxGkv7VDuNvcShMAcIWDldRfZNR9ZMl%2B%2Bey6p9qQc%2BL8NIxtgGt40kTyDYzvxsorTR96jNqs8BHaRl1ngqGdGOBEb0CtkliWmZheen%2B%2F44k3komitDFNno2w3t3mBbdSuVCx%2BcibXTCElacULwTyZtpxuyNyT9L86XTkYv0tAUM6PmpcI2MipFLVZO6WJbH5M35YUg%2Fhy0rJl4ZIGWMO3Qy5kICZ%2BhFl55mhXyAwP354sC%2BM6TdBGUUtf6HNk4wJZsK8fLx%2FAJ6g3g3NPaKmSNutgxasLvgfzZjDkooPNlU9BreQPZK924HL%2FA3fSpURg1EvuhcwRJKU4uiSaUQCNMzMv7731iHktyLqHNVBFM1J0MeIDRmmvI%2BriSmK3gDwlRAGQSa6yZpx5HFFZli4MB32XcGLvoVJWbcjxhAJ5CM1Gty%2Fd38e7UKD7vSEYpRP6SO7i53QyrhyNO0H3HDc8IBay453LGU%2FfJHNUvwa5BVxPO8ObJR9xUMJSpnVxko0MiumWUnjOi34uZU0Z4ZOqwQtl7vmdm5u2iXEqkrDSajgw7Lf%2F0gY6pgE%2FV4TyRoWLH6jw8hza%2FhcKrujzIPBNAq3FXXozOJZcl%2F6S5GjCLYbiYP9DRIhCMVhXMd3z3tcF0TOMuGMTCilJEOraCt0Ha6JI2grYltFRQgIwtwLMxY27MKRMvusBpaATH6eO0L1u3q1v65X7JIGuJHlJANaH%2F31QHo73E%2FV3x6yiLFrbQhc2Gt0PbYbxdTsQKs7FFtglb0FP%2F2O4JYg24RyPj0L9&X-Amz-Signature=40df1a125432a71a31787898c7317a27884e280025ba3d0d362174ef4439e57b&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

咱们还是复用上一节的这个事例，咱们还是进入到上一节的这个项目，咱们已经运行起来了，咱们提前运行起来了。然后咱们打开浏览器访问一下这个系统，咱们再熟悉一下。 localhost userlist 吧，是列表页对吧，咱们点击一下修改这个页面是它的修改的页面是吧，咱们可以理解为它是一个用户注册的页面。那么这个页面咱们是不是就可以复用了？复用以后，用户在这里边去进行注册，注册完了点击提交，完成这个用户的注册。


那么这里边这个唯一的业务号是谁呢？就是这个用户名是吧，因为用户名在一个系统里面是不唯一的，咱们可以把这个页面看成一个用户注册的页面。用户注册用户名不唯一，那么用户名就是唯一的业务号了。下面咱们就使用这个分布式锁来解决有唯一业务号的这种接口的幂等性。


首先咱们要复用这个页面，咱们后台要写一个 controller 是吧，咱们回到 idea 进入到 user controller 在这个 user controller 里边咱们要新写一个方法是吧。 public stream 叫做什么呢？叫做register 。 reject 用户注册。然后咱们就直接返回这个页面 return 杠 user 杠 user detail 然后加上一个 request mappingregister 咱们重新启动一下，然后进入到浏览器，咱们访问一下 rejust 报错了是吧，咱们进入到后台看看他报的什么错 ID 并没有找到。因为咱们之前这里边有一些属性的赋值，所以这块咱们要给他付一个空的，咱们这块给他加一个 model map 然后里边 map.add attribute user newuser 咱们试一下重启试一下。


启动成功了是吧，咱们再刷新一下这个页面，没有问题了是吧。然后咱们要在这里边填上你注册的信息性别、年龄。然后咱们点击提交，把整个表单提交到后台，然后后台去替 user 这张表当中去插入一条新的记录。咱们现在要保证这个接口要是幂等性的。那么既然这个页面咱们复用了之前的，那么这个提交按钮咱们是不是也可以复用复用之前的这个 update 复用这个 update 的 user 在这个 update user 里边咱们可以判断一下用户的 ID 因为你更新的时候这个页面的隐藏域当中的 user ID 是存在的，但是如果我是全新注册的话，这个 user ID 是不存在的。


咱们就以这个用户 ID 存在不存在去区分它是 update 的操作还是 insert 操作咱们还是回到程序当中这块，咱们加一个判断， if user.get ID 不等于 now 不等于now ，说明它是更新操作，咱们把这一段给它挪进来。如果是 now 等于说它是空的，那么它是一个全新的注册的操作。那么这个时候咱们就应该走到 iOS 当中来了。 else 当中来，咱们要新写一个方法 insert user 然后把这个 user 给它传进来，咱们在后台进行生成，返回一个 int 这个时候咱们要保证这个 insertUser 它是一个幂等的对吧。


那么这个时候怎么办呢？咱们要使使用分布式锁，使用分布式锁锁住你当前的这个唯一的业务号。那么当你多个请求过来的时候，只有获得了这把锁的这个请求，才能生成后台的用户。那么这个时候咱们要使用这个分布式锁。分布式锁咱们在前面的章节已经给大家介绍过了，这里边咱们采用一个基于主 keeper 的分布式锁了，基于祖 keeper 的，而且是库瑞特官方提供的这个方式。咱们又要回顾前面的内容了是吧，咱们直接打开前面的这个项目 distribute ZK lock 是吧，咱们看看之前是怎么使用的，开了是吧。


第一步咱们要看看这个 pom 文件咱们引入了哪些价包。其中有一个是组 keeper 是吧？然后还有一个 creator 咱们采用这个 creator 这个客户端是不是就可以了？咱们把下边的这一段给它复制过来。那下面的这一段复制到咱们的项目当中，打开 pom 文件，然后粘贴一下这个 create 客户端就已经引入成功了是吧，刷新一下Maven ，然后再看看前面的项目，引入这个依赖以后，咱们在这个项目的启动类当中增加了一个楚瑞特这么一段配置是吧，咱们同样的把这一段配置复制过来，这块咱们再新创建一个 config 类，叫做 ZK config 同样它也是一个配置类，打上一个注解 configuration 里边，咱们刚才复制的这一段给它粘贴过来。


第一段配置的是他的重试的策略。第二段就是他的客户端，客户端是 local host 2181。那么咱们也是把本地的这个主 keeper 给它启动一下，进入到 D 盘是吧。找到 ZK 三点四点一四进入到闭目录，然后双击 ZK server.cmd 这个主 K 班就启动成功了。然后咱们再回到项目这个分布式锁，咱们要在 user service 层使用是吧。第一步要把这个主 keeper 的客户端咱们要给它注入进来 private 然后 curate framework 注入进来， ZK client 加个奥特曼，然后回到这个 insert 的方法这块咱们要加分布式锁了是吧，这个 ZK 的分布式锁怎么用呢？咱们再回到之前的项目看一下这个 CK controller 这里面咱们使用 ZK 在这块是吧，把这段给大家复制一下，复制到咱们的项目当中。


这个 client 就是 ZK client 是吧，pass咱们一定要用这个唯一的业务号是吧。这个唯一的业务号呢就是 user.get user name 这个时候就比如说你写了一个用户名，然后后呢你点击了多次的提交按钮，那么后台接到了这些相同的注册用户名的这些请求，只有获得了分布式锁的这个请求，才能生成这个用户 Doc 点设置成为一个 30 秒。第二个参数是一个 time unit 选择second。


这块有错误，咱们给它直接抛出去。如果获得了这个锁 is lock 咱们执行 insert 的操作。 insert 操作咱们直接使用 user mapper.insert selective 传入一个 user 这个是不是咱们就直接返回就可以了？如果你没有获得到这个锁，那么我直接返回一个 0 这块这个异常咱们也是直接给他抛出去，这样是不是就可以了？这块咱们加上一个日志，在这一块咱们写上一个添加用户，咱们重启一下这个服务试一下。


这块同样咱们有一个休眠的线程是吧，休眠了 5 秒一会，咱们也是在这 5 秒之间点击多次添加用户，咱们看一下具体的结果。项目启动成功了，咱们回到浏览器刷新一下当前的这个用户注册的页面。下面咱们要写一个用户名是吧，用户名咱们写什么？写慕课。因为之前咱们把慕课的用户名改成了第四了是吧这块咱们还用慕课去进行注册，随便写一个年龄写一个16。下面咱们多次的点击这个提交的按钮，模拟它这个后台没有响应，咱们用户多次提交是吧，好多次点击了，然后咱们看一下后台的程序，这里边咱们也是了几次，点击了 7 次是吧，点击了 7 次。咱们看一下这块报错了是吧，在创建这个分布式锁的时候报错了，我们先把这个服务停一下。这个错误是因为咱们使用了这个 creator 的这个客户端，版本太高了，咱们的服务端的这个 ZK 它的版本又太低。咱们还是把这个之前老的这个 ZK 的客户端给它复制过来，进入到之前的项目，把 ZK 客户端给大家复制一下，粘贴到咱们的项目。咱们来看一下。之前这个 ctrl 的里边的日志有点不清晰是吧，这个更新用户咱们给它挪到下边来，这样整体的结构就比较清晰了。


后咱们再启动一下这个项目，启动成功了是吧？咱们还是刷新一下注册的这个页面，然后重新写一个木刻，选一个男年龄16，咱们这一块还是点击多次提交是吧，一会咱们来看一下后台的日志，咱们回到后台看看。现在的日志还没有打出来，现在打出来了是吧？总共是执行了五次添加用户。五次添加用户，如果你的接口不是幂等的，那么它会生成五个用户。但是咱们在这里边使用了分布式锁，使用分布式锁，使接口具有了逆等性。咱们再回到浏览器当中咱们看一下。现在只生成了一个用户，这个是不是就保证了咱们 insert 它是一个幂等的操作？这种情况是有唯一业务单号，也就是说这个用户名它是你整个系统当中的唯一业务号。这种情况下，咱们可以使用这个唯一的业务号去作为分布式锁的 key 来保障接口的幂等性。


那么如果你的隐私的操作没有这个唯一的业务号要怎么办呢？咱们的思路其实也是一样的，没有唯一的业务号，咱们要创建这个唯一的业务号，后续的步骤就是一样的了，咱们使用这个新创建出来的唯一的业务号去获取分布式锁，然后拿到锁的这个请求完成后续的处理。没有拿到锁的咱们就直接返回了。


咱们还是进入到注册的页面之前，咱们是把它看作一个用户注册的页，如果你是一个用户注册的页，那么你这个用户名它就要保证是唯一的了。咱们把这个用户名作为一个唯一的业务号。那么这个页面咱们现在如果把它看成一个用户的，收货地址提交的话，那么是不是他就没有这个唯一的业务号了？如果它作为一个用户的收货地址去提交的话，用户名它是可以重复的，你可以叫张三，我也可以叫张三，咱们两个的收货地址不一样就可以了。那么在这个页面当中就没有了唯一的业务号。
那么没有唯一的业务号怎么办呢？咱们要创建唯一业务号，也就是说创建这个 token 咱们再回忆一下这个 PPT 当中的步骤，这个 token 是在你访问这个页面的时候就已经生成好了。然后咱们在提交的时候会把这个 token 从页面当中，传到，咱们在后台去进行验证，验证你的这个请求，在后台能够找到这个唯一的业务号，我才进行后续的操作。如果你的这个请求没有找到唯一业务号，那么这个请求是不是就是伪造的？那么我就不进行后续的操作了。进行后续的操作的时候也要保证幂等我们同样要使用分布式锁。下面咱们就把这一块的流程再给大家演示一下。


首先要在这个用户注册，咱们现在要给他改名叫做添加收货地址是吧。在这个添加收货地址的页面先要生成一个 token 咱们回到这个项目当中，进入到这个 user controller 这个与 JS 的这个方法当中，要生成一个 token 这个 token 咱们就暂时使用 UUID 是这样 token 等于 uuid.random U [uid.to](http://uid.to/) string 然后这个 token 咱们在后台要统一的做一下记录是吧，这个咱们怎么办直接在这块写一个全局的变量。


create set string token set 对吧，你有韩信 set 这样是不是就行了？这块你使用全局变量的时候，一定要慎重的考虑，因为咱们在演示的过程当中只是一个单机的服务，我可以这样使用。如果在你的生产环境去部署你的项目，你可能要部署多台机器。那么你多台机器当中每一个 gv M 是不是都有一个这个哈希 set 都有一个 token set 是吧。那么这个时候当你的两个请求过来，打到了不同的服务器上。那么是不是这个 token set 就不是一个整体的了。那么这个时候你在后续进行判断的时候，你的 token set 是不是就有一台服务没有了？所以如果你考虑你的前端集群部署的话，这块这个 token set 还是使用 Redis 比较稳妥，把这个 token set 统一的放到 Redis 当中去。


这块就不过多的给大家介绍了，这块咱们就使用本地的全局的变量，把这个 token 给它 set 进来。 Get token. 同样要把这个 token 给它返回到前端的页面当中，加上一个 token 这样是不是就可以了？然后咱们再回到这个前端的页面， user detail 在这里边再新创建一个隐藏域名字叫做 token 对应的值 token 是吧，这样这个 token 是不是要带到前端的页面了？然后咱们再点击提交的时候，还要把这个 token 给它传回来，传到这个 user controller 当中。


这里边要再加上一个参数 string token 它是一个 insert 操作的时候，咱们在这里边希望判断一下这个哈希 set 有没有这个 tokenif token set.contents token 如果它包含了这个 token 说明这个请求是一个真实的请求，咱们要进行 insert 的操作。如果它不包含这个 token 这个时候咱们直接抛出一个异常，怀疑什么错，偷看不存在是吧，这样是不是要响了？然后这个 token 咱们还要传入到这个 insertuser 这个方法在这里边咱们要修改一下这个方法是吧，加上第二个参数，然后里边咱们要用这个 token 去获取分布式锁，因为 user name 已经不是这个唯一的了，说这个 token 咱们可以保障唯一，这样是不是就可以了？咱们重新启动一下这个项目，一会咱们模拟一下。
好，启动成功了是吧。咱们在这个浏览器当中刷新一下注册的页面，然后咱们再添加一个用户名，这个用户名咱们叫做2。慕课二。然后零十同样咱们为了演示它是不同的 token 咱们这里边打开两个页面，用户名咱们都注册成为慕克尔，这个用户名是不是要重复了？然后咱们区别一下，性别改成女年龄改成12，快速的点击第一个页面。


然后咱们再快速的点击第二个页面，看看它后台是生成一条记录还是生成两条记录或者是更多的记录，咱们快速点击一下，现在都还没有响应了是吧，看看后台的日志，添加用户点击了很多次是吧，咱们也不知道是哪一个页面的，不知道是哪一个 token 的。现在响应过来了是吧，咱们看一下这个生成的记录总共是生成了两条记录，一个性别是男，另外一个性别是女。再回到这个后台咱们总共是点击了多少次？一次两次，然后五次一共点击了 9 次。也就是说标签 1 和标签 2 咱们一共点击了 9 次生成用户，但是最终只生成了两个，这样也保证了咱们的接口是逆等性的。因为每一个这个页签它都是不同的 token 我们根据这个 token 去获取分布式锁，然后进行用户的创建。咱们两个页签有两个 token 所以咱们就会生成两个用户。


好了，到这里这个 insert 操作的这个幂等性就给大家介绍完了，包含两种情况，一种情况是有唯一业务单号是吧这种情况。另外一种就是没有唯一业务号，有唯一业务号的这种情况咱们要用这个唯一的业务号去获取分布式锁，然后获取锁的这个请求完成后续的操作。没有唯一业务号的这种情况，咱们要创建唯一业务号，怎么？就是创建那个 token 然后用那个 token 去获取分布式锁，获取锁的这个请求完成后续的操作。


通过 token 去保证接口幂等性的这种方式是在所有的操作当中都是适用的，包括你的 delete 操作包括 update 的操作。这两种操作咱们在前面都有没有唯一业务号的这种情况咱们都没给大家做具体的示例是吧，咱们统一放到了 insert 这个示例当中，都是使用这个 token 去作为唯一的业务号，包括后续的你有混合操作的，你的这个操作里边不只有 insert 操作，可能还会有其他的像delete 、update ，整个的这个业务的框架是不变的，都是用这个 token 去获取分布式锁，然后保证接口的幂等性。
好了，这一章的内容就给大家介绍完了，咱们还是快速的回顾一下。这一章的内容主要是给大家介绍了如何保证接口的幂等性。那么首先咱们要理解什么是幂等性？易等性的含义，就是说当我多次的去调用一个接口的时候，和我只调用一次接口，它的效果是一样的。这个就是你的接口具有了幂等性。另外有一条非常重要的一句话，不是所有的接口都要求幂等性，只有一些特殊的业务需求，比如说咱们的支付下单这些要求接口是幂等的。


那么幂等性的接口咱们怎么去做？它主要是分为两大块，一个是有业务单号，另外一个是没有业务单号。那么有业务单号里边咱们又分为了 delete update 和 insert 没有业务单号，虽然说也分为了这个 delete update 和 insert 但是它的整个的这个流程是一致的，都是生成这个 token 然后用这个 token 去获取分布式锁，然后获取锁的这个请求去执行后续的操作。这个就是一个咱们这一章的内容的整个的一个脉络，这一章的内容就全都给大家介绍完了，感谢大家的收看。




## 

