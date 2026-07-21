---
title: 2-15 【Demo】基于jwt实现用户鉴权-2
---

# 2-15 【Demo】基于jwt实现用户鉴权-2

[image](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/61b4bd48-7732-4847-82ad-bb2bb9013011/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XCUQ324U%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T225742Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIAJzBwTsadUcRfiHIN1p2QpUpsxXhHV%2F6dWMRnjC%2BocMAiBiTZYGeuLhfxM8P9IWO%2BoEIG94blnqEjZ7G1b7GckmnyqIBAjG%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMR%2Ff1cSbGh3gWZHoFKtwD4mk2%2BxyDw%2FFkpKZqnutQgD66Li70xs%2F%2B2bMSuKmT2xUJqUKgJ3jKTzu63WYxNWAMM9xKCxWHLtiqH7QRY3WhgssnDSDltB2xivabYs%2F9ssJdT8k1MIB3PhpU4iOpdR2K%2FNXoS3y24ds6m30UcLZ54Dxvtd9OJdaASve8XffFkR1i991%2FN7PVu2108j7X7fXTK3qZFvR%2BNHUiEnKPuGn353P2ID75ITK%2BkeaL7kineJdeoVhBiYTYDRe4N0wmLRYr8w0HmcUpZAVWyUezcL8%2BAJkBcmqCIvRKWraN5DbXM%2B861D83zmzAoxeCL9tl5ncjjIHWVhwdRxDOz%2FGLq1i3vekxc7USiSx6OLnUVl2pxy659qGdoM57GwyAU078G2%2FhHMnnVuTkndMBPJDCfpQTOpE92OkqIMPmouBQw9uct%2FpNWkmN%2Fw6uX8wlSBgY3oIrnDXAWZ2B58LCVgZjnMScEpL5R8FDCabm5aGELqlIbKi%2BVhSW1wgG464Idly3cWTjFU3WTnfTVl%2FRyiPiHliMbXQfmXnXOy6FJUYgKa3PMWZtprlPTNWBN9bl%2FvoeYMXE%2BKaiAhK6mQWVBBQbyC0FxgD1OFkIR3RQNCUWCX352tndksh38yJqV4ueDWEwmrr%2F0gY6pgH4MGdYUnhhEdqzLirmiLgYoVJKRol8KmsvwGnEBWeOx%2BvH%2BqqMeX7fJGdEwbkuJ4w4ZUWh7iDiJEZqk1B0bCW2QzmbzcgKujjfqZF16IYTVgwttlkm9Db5Ip9eWPyISkNEDdbUkfrIM0icSV6EnqgrDmu45YVnvfs4xbiLdyKHR%2BuRS8bcQHyl%2F6Zm%2BBUQfHt8biHaxY5njIhmqNBc8uHAVGEAqNQb&X-Amz-Signature=1d8960829a7cd27d9ddb34bebd8716de94a9913fcdd91b3f3a0efd01b0ba7e6f&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

[image](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/4958a15f-9c3e-42ea-b048-29b9f5abb4d5/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XCUQ324U%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T225742Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIAJzBwTsadUcRfiHIN1p2QpUpsxXhHV%2F6dWMRnjC%2BocMAiBiTZYGeuLhfxM8P9IWO%2BoEIG94blnqEjZ7G1b7GckmnyqIBAjG%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMR%2Ff1cSbGh3gWZHoFKtwD4mk2%2BxyDw%2FFkpKZqnutQgD66Li70xs%2F%2B2bMSuKmT2xUJqUKgJ3jKTzu63WYxNWAMM9xKCxWHLtiqH7QRY3WhgssnDSDltB2xivabYs%2F9ssJdT8k1MIB3PhpU4iOpdR2K%2FNXoS3y24ds6m30UcLZ54Dxvtd9OJdaASve8XffFkR1i991%2FN7PVu2108j7X7fXTK3qZFvR%2BNHUiEnKPuGn353P2ID75ITK%2BkeaL7kineJdeoVhBiYTYDRe4N0wmLRYr8w0HmcUpZAVWyUezcL8%2BAJkBcmqCIvRKWraN5DbXM%2B861D83zmzAoxeCL9tl5ncjjIHWVhwdRxDOz%2FGLq1i3vekxc7USiSx6OLnUVl2pxy659qGdoM57GwyAU078G2%2FhHMnnVuTkndMBPJDCfpQTOpE92OkqIMPmouBQw9uct%2FpNWkmN%2Fw6uX8wlSBgY3oIrnDXAWZ2B58LCVgZjnMScEpL5R8FDCabm5aGELqlIbKi%2BVhSW1wgG464Idly3cWTjFU3WTnfTVl%2FRyiPiHliMbXQfmXnXOy6FJUYgKa3PMWZtprlPTNWBN9bl%2FvoeYMXE%2BKaiAhK6mQWVBBQbyC0FxgD1OFkIR3RQNCUWCX352tndksh38yJqV4ueDWEwmrr%2F0gY6pgH4MGdYUnhhEdqzLirmiLgYoVJKRol8KmsvwGnEBWeOx%2BvH%2BqqMeX7fJGdEwbkuJ4w4ZUWh7iDiJEZqk1B0bCW2QzmbzcgKujjfqZF16IYTVgwttlkm9Db5Ip9eWPyISkNEDdbUkfrIM0icSV6EnqgrDmu45YVnvfs4xbiLdyKHR%2BuRS8bcQHyl%2F6Zm%2BBUQfHt8biHaxY5njIhmqNBc8uHAVGEAqNQb&X-Amz-Signature=4990ecf39fd1adf3ee4985bcc02faf555bc2da66dacd0e50a62fd002db0656fc&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

[image](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/b3675a97-2d2c-4fed-b27f-5ff0614bdae7/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XCUQ324U%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T225742Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIAJzBwTsadUcRfiHIN1p2QpUpsxXhHV%2F6dWMRnjC%2BocMAiBiTZYGeuLhfxM8P9IWO%2BoEIG94blnqEjZ7G1b7GckmnyqIBAjG%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMR%2Ff1cSbGh3gWZHoFKtwD4mk2%2BxyDw%2FFkpKZqnutQgD66Li70xs%2F%2B2bMSuKmT2xUJqUKgJ3jKTzu63WYxNWAMM9xKCxWHLtiqH7QRY3WhgssnDSDltB2xivabYs%2F9ssJdT8k1MIB3PhpU4iOpdR2K%2FNXoS3y24ds6m30UcLZ54Dxvtd9OJdaASve8XffFkR1i991%2FN7PVu2108j7X7fXTK3qZFvR%2BNHUiEnKPuGn353P2ID75ITK%2BkeaL7kineJdeoVhBiYTYDRe4N0wmLRYr8w0HmcUpZAVWyUezcL8%2BAJkBcmqCIvRKWraN5DbXM%2B861D83zmzAoxeCL9tl5ncjjIHWVhwdRxDOz%2FGLq1i3vekxc7USiSx6OLnUVl2pxy659qGdoM57GwyAU078G2%2FhHMnnVuTkndMBPJDCfpQTOpE92OkqIMPmouBQw9uct%2FpNWkmN%2Fw6uX8wlSBgY3oIrnDXAWZ2B58LCVgZjnMScEpL5R8FDCabm5aGELqlIbKi%2BVhSW1wgG464Idly3cWTjFU3WTnfTVl%2FRyiPiHliMbXQfmXnXOy6FJUYgKa3PMWZtprlPTNWBN9bl%2FvoeYMXE%2BKaiAhK6mQWVBBQbyC0FxgD1OFkIR3RQNCUWCX352tndksh38yJqV4ueDWEwmrr%2F0gY6pgH4MGdYUnhhEdqzLirmiLgYoVJKRol8KmsvwGnEBWeOx%2BvH%2BqqMeX7fJGdEwbkuJ4w4ZUWh7iDiJEZqk1B0bCW2QzmbzcgKujjfqZF16IYTVgwttlkm9Db5Ip9eWPyISkNEDdbUkfrIM0icSV6EnqgrDmu45YVnvfs4xbiLdyKHR%2BuRS8bcQHyl%2F6Zm%2BBUQfHt8biHaxY5njIhmqNBc8uHAVGEAqNQb&X-Amz-Signature=8d9ecc716f895e72555c9efabc2467f11ca7fc0f65e4462b1a9b34e151b6d41e&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

hello 慕课网的各位同学们，大家好，咱又来到了下半场，口号我们就不喊了，时间紧，任务重，再喊口号要拖堂了。我们这里创建了 JWT service ，刚才说的还差一个 controller 好，我们这里给它新 new 一个 controller 的类，这个类里面都有什么方法呢？有三个，它分别对应了 login 还有 refresh token 以及 verify token 好，我们先来写第一个方法，收集小桌板，它的返回值是 of response 然后方法名就叫 login 那它就只接收两个参数，我们把一个流程简化一下，我们就只接受 username 和什么？ password 对不对？好都是 string 类型的。


然后这两个参数接收好了以后，我们的业务逻辑里面做一件什么事呢？我们先要拼装 account 对象，咱是一个 builder 类型的 con 对象，所以拼装起来非常的方便。直接调用 build 方法，在下面把 username 给它塞进去，在后面它给 build 出来，这个对象 build 完成以后，我们在接下来要调用 JWT 的方法了，所以在调用以前，咱要先把 JWT 的 service 给它在这注入进来。 JWT service OK auto wire 的进来。然后我们要申请 token 好把 token 给它塞入进去，account对象传入进去，这里应该就能获得了一个 token 那咱这里缺了一步，大家知道是哪一步吗？我这里加一个todo ，就是说验证 username 加 password 因为我们这个 user name 和 password 通常来说是用户存储在数据库里的东西，它还有一些撒盐什么之类的加密操作。那这里我们假定你的 user name 和 password 都已经验证完成了，然后才会进入到下面的 token 流程，所以咱们在这边加个提示，就把这一步先给省略过去了。


拿到 token 以后，要把它塞入到 account 对象里面。对不对？我们前面说到它还有一个 refresh token 是什么？是备用钥匙对不对？也就是说当你 token 快要失效的时候，使用 refresh token ，可以把它再给重新刷新一遍，获得一个新的 token 好，那咱这里 refresh token 怎么获取？就用 UUID 就好了，拿一串 UUID OK 那走到这整个 account 就已经生成完了，这里就可以直接返回最终的结果了。 OK 咱也调用它的 build 方法怎么来 build 传入一个 account 把它塞入进去就可以了。


OK 塞入完了以后要给它返回一个 status codeset code 好，code是多少呢？我们的 error code success 实际上这个 error code 名称起的并不那么好，我们把它重命名一下。好了，叫 response code auth response code 因为如果你起名叫 error code 的话，那可能大家觉得这里面全是错误的信息，但是实际上它还有包含成功信息的。 OK 那咱把它 build 出来就直接 return 回去了。但是在这之间还有一步操作，我们生成了 token 对不对？要把它存在咱系统中的某个地方，这样的话在后面 refresh 的时候才能找到应该 refresh 那个 token 对不对？也就是说我们要在系统中某个地方保存一组。关系关联谁呢？这个关系的一头是 refresh token 那另一头就是 token 他要把这两个值一一对应起来。


什么地方适合保存两个地方？如果咱是单机应用的话，就起一个测试节点，那直接声明一个 map 就好了。但是我们这里因为引入了Redis ，咱就用 Redis 的 template 来做这个操作了。 Redis template OK 怎么来存到 Redis 里面呢？我们直接使用它的 get for value ，其他就不开始什么都不用了，直接用 value 方法把它作为一整个对象给它传入进去。那它的 key 是什么？ key 就是刚刚生成的这个 refresh token 它的 value 是谁呢？ a value 就是 account 对象，把 account 对象完整地存进去，OK到这里就结束了。那这个 login 方法我们要给它声明一个路径，首先它要是 post 那他的路径名叫 locking 然后返回的是 response body。


Ok.同时方法上面这个 controller 上面也别忘了绿帽子给它戴上绿帽子是个好东西代表着你的这个人生经历比较丰富，就像挂科一样，没有挂过科，没有戴过绿帽子的人生那都不是完整的。当然了老师现在的人生也是不完整的。 logan 方法处理完了，接下来咱要处理一个叫什么方法 refresh 方法，我们把前面的方法名直接给它 copy 上来，把它改，给它起名叫 refresh 传入的东西那就少了一个了，不会传入 user name 这些信息了，它只会传入一个 refresh token okay 同样的，这个方法的路径，咱先给它贴上去，它的路径就是 refresh OK 和方法名保持一致。然后方法体咱来看看怎么来写法。
a refresh token 首先你要验证这个 token 是不是存在对不对啊？那我们依然要从 Redis template 里面用最简单的方式直接用 OPS for value 把这个对象给他拿到 refresh token 传入进去，把对象拿到。如果这个对象为空的话，那说明什么？说明这个 refresh token 压根就不存在。那咱可以直接返回一个错误的 response 对不对？说明一个 builder 然后把它的 code 设置成什么，设置成 user not found 然后 build 出来。好勒，这一行有点长，咱把它折一行。那如果你存在了，接下来就要把它给拿到更改一下，我们把上面这段逻辑抽一下，这样的话下面还能复用到这里替换一下。 OK 然后把结果需要做一个强制转换。


咱这里其实有一个注意点，在前面遗漏掉了是什么呢？就是说当你使用 Redis 的 UPS for value 来存储对象的时候，这个对象必须是一个可被序列化的对象。那我们进去看一下，缺了点什么，缺了一个序列化的接口，我们把它给补上。 implement serialize 这一个接口 serializable 就证明了对象是可被序列化的。否则当你去尝试着存储对象的时候， Redis 它这里会报一个错误。
OK 好，那在这里拿到了 account 以后怎么办呢？当然是要申请一个新的 token 了，怎么申请啊？ OK 我们这里先通过 JWT service 的 token 服务把 account 传入进去，然后获得一个新的 gwt 这个新的 gwt 我们把它接着塞回到炕台里面。从哪里来到哪里去 set token 塞回去以后咱还没有完，咱要再把它存入到 Redis 里面。


在存入以前，咱先要干一件事儿，要刷新一下它的 refresh token 因为咱前面 refresh token 已经用过一次了，对？不能再用第二次了，这是一次性的。好，我们这里生成了一个新的 refresh token 以后把上面的这一句给它 copy 下来，然后使用新的 token 把当前更改过后的 count 保存进去。但是咱这个新的 token 结识新朋友，不要忘记老朋友老朋友是谁，以前的那个 token 是不是还在 Redis 里面，那就顺势把它给删除好了。


OK 这两步操作完，咱就大功告成了，可以直接把 response 返回回去，我们这里 copy 一下啊，他的 response 依然在这里返回一个成功。 OK 那到这里 refresh token 也已经创建好了，我们把 URL 改短一下就叫 refresh 那还剩最后一个是谁呢？是我们的 verify 方法，verify方法它 verify 什么内容呢？第一个就是 token 紧接着后面的要跟一个 username 因为它要验证一下当前 token 中的 user name 和咱传入的 user name 也就是当前的使用用户是不是同一个人。 OK 那我们把它改成 get 方法好了，因为它实际上并不会更改什么内容，只不过是做一个只读的操作。那它的方法体也非常的简单，我们只用调用一下 gwt service 的 verify 把 token 还有 user name 统统传入进去也就好了。
OK 那它会返回一个布尔值，我们把它定义为叫 success 其实它并不是真的success ，我们这里还要判断一把的，那就是在返回值当中，我们对这个 success 方法进行一个判断，怎么判断？看这里我这个 account 还用返回吗？压根就不用返回，只要返回它一个成功还是失败就可以了。那如果成功返回 success 否则返回谁呢？返回这里面的 user not found ，这样简单一些实际上咱应该返回另外一个新的 status code 比方说 invalid token 之类的。 OK 我在这里记一个 todo 大家要保持一个好习惯，如果你在写代码的时候发现哪里看起来不顺眼，或者是说你认为还有改善的地方加一个 todo 这就能提醒自己哪天有空的时候再回来看一看，把它改掉。我这里加一个 todo 说此处最好用 invalid token 之类的错误信息。 OK 好，到这里，我们的 ctrl 也已经开发完成了。那剩下的还有谁啊？那就是配置文件，我们这里就不一行手打了，我给大家变了个魔术，凭空一声雷创造出了一个配置文件，我们来一行看一下。首先它的 application name 这里指定了叫 off service 然后端口拿65,100。这第四行是连接到友瑞卡注册中心，那剩下的都不重要。 OK 在第八九十行，大家看到这里是 Redis 的连接，我采用的是默认的端口。 OK 那我们的配置文件也已经配置妥当了，是不是可以尝试着跑一把看看了。那么这里就把它启动起来看一下。


当然啦，在启动这个方法以前，咱要确保有瑞卡注册中心已经启动起来了。那我们这里稍等片刻，等它启动好了之后，调它几个方法，看看它是不是可以生效好，加载得很顺利，它已经成功启动起来了。咱现在转战到 postman 里，尝试几个方法。我这里已经创建了好了很多个示例，我们先挑选这个注册示例看一下。这个注册里面我们选的 username 是 M E me 那 password 随便给了一个数字，反正咱后来也不会去验证数据库，你的 password 想写什么就写什么，早安来调用它的 login 方法看一下走你完美看到同学们这里已经返回回来了，它的 status code 1，也就是 success 那这返回的内容有一个 token 和一个 refresh token 好，我们先把这个 token 给它 copy 下来接下来干什么呢？接下来就去 verify 方法里面验证一下这个 tokenok 因为它是一个 get 请求，咱就把这串 token 粘贴到 URL 里面，然后 user name 在后面，这个很小的字还是 me me 好，我们 send 一把。 OK 你看它这里返回了 code 是一说明成功了对不对？我们拾点坏，把 username 改一下，改成 username 等于2。这里 status code 就返回了失败，所以 verify 方法也是生效的。再接下来我们还剩最后一个方法，好，把这个 refresh token copy 一下，然后粘贴过去。


OK 咱大家记住，这个 refresh token 是怎么样？是一次性的，只能用一次，如果你点击两次，它可能会失效喽。 OK 点击 send 这里已经获得了一个新的token ，如果大家再尝试点击 send 会发现他报了一个 1001 的错误。为什么呢？因为长在 refresh 接口里面啊。啊使用完了这个 token 以后，就把它在这里给删掉了。 OK 那到这里咱的 authorization service 就已经完成了，剩下的就是到 gateway 里把这个 authorization service 集成进来了。那咱这次使用一个省时省力又高效的方法，因为考虑到时间关系，我们不能拖堂，所以这里我就不跟大家一行手打代码了，我把所有的代码都已经准备好，在这里带大家从头到尾看一下 gateway 里究竟有哪些改动。


咱先从 palm 开始。这里 pump 文件有这么两处改动，第一处是引入了 auth service CPI 引入了它的依赖。但是大家注意到这下面它下面把 spring boot starter web 的应用给它剔除出去了。因为为什么上面有一行注释， spring cloud gateway 是一个很特殊的存在，它的底层并不是依赖于 springboot starter web 而是依赖于另一个组件 web flux 所以如果你把它的 web 依赖引入进来，那可能是会有报错的。所以这里我们把它剔除出去，只使用 sprint cloud 自带的 web flexok 这是其中的一个 dependency 另一个 dependency 是一个工具类，它里面有一些 stringut O 之类的方法可以帮我们判别字符串。所以把它引入了进来，只有这两处改动。


好，我们接下来走到它的代码层了，这里有一个新的类叫做 off filter 那它是专门做权限验证的，我们来看它有哪些内容把它放到最上面。这里它依然继承了 gateway filter 也就是说它并不是一个全局的 filter 好，我们来看它的核心方法，在第一行开门见山，一行 log 打出来。


off start 接下来咱从 exchange 对象中获取到了 request 并且从 request 当中获取到了 headerok 拿到 header 这个对象头有什么用？有两个人来送人头了哪两个 of 一个是 username 大家注意到，我这里把 authorization 也就是你访问用的 token 以及它的 user name 都放到了 header 里面，然后通过这种方式传到了 filter 中。


接下来是一段验证，如果你传来的 token 是空，那么你是没有权限来访问的我将会返回给你一个 unauthorizedok 这里直接调用 response 的 set complete 方法。你通过这样一次调用，整个 response 就结束了。那我们再往下看。假如你的 token 部为空，我需要调用 auth service 的 verify 方法，同时把 token 和 username 传入进来。那返回的结果中，如果它的 code 是1，那么相安无事，大家继续往下走。如果它不是1，说明这个 token 不是一个有效的 token 那么 response 的 status code 就会被设置为 forbidden 也就是说大家没有权限此处要中断访问。那接着往下走。既然大家走到这儿了，说明前面的验证都已经通过了。那么这里我们做这样一件事，把 username 再放到 header 当中，然后再往下走。走走走到这里。 OK 如果咱在 response 中需要添加新的 header 就可以通过这一行中体现出来的方式，我们把 username 也同样的放到 response 当中，并且给 response 设置 status 等于OK。


Ok. 那接下来往后走，这里的函数式异步编程，它会做这样一件事情，把我们自己构造的 response 还有 request 拼接起来，然后传递给下一个 filter chain 好这里就是整个 filter 的主体逻辑。我们再来看一下这个 filter 是怎么应用到路由规则中的目光现在转向 gateway configuration 这个类。 OK 收集小桌板，我们在它的 configuration 中注入了一个 auth filter 然后把它添加到了其中的一个路由。是哪个路由呢？就是咱以 Java 开头的访问路径所转发到的路由中。那大家看到这个路由当中有两个filter ，第一个 filter 是咱前面小节做的方法，计时器下面的一个 filter 才是真正做权限验证的。 OK 那这就是所有的改动了，同学们是不是觉得这种领着大家参观代码的方式更有效率呢？OK ，那我以后多多采用这种方式了。那我们现在不妨把所有的应用全部都启动起来看一下。


在启动 gateway application 之前，咱先要确保把 eureka server 启动起来，同时 authorization application 以及分 client 都要启动起来，最后再启动 gateway application 那如果这个启动顺序有偏差，可能大家会在 gateway 启动起来的头几分钟内访问不到服务，因为它所依赖的服务可能还没有及时注册到 eureka 注册中心上。


OK 咱那 gateway 已经启动起来了，我们转战到 postman 当中，我们这里调用 gateway 里的 Java 杠 say hi 方法。那么一开始的测试，我们先不传入这个用户名和 authorization 两个 header 我们把它勾掉，看会有什么效果发起访问。同学们看到这里，没有任何返回结果，但是它返回的 status 是 401 on auth rest 也就是它被咱的权限验证器拦截下来了。


OK 代码里的 log 我们看一下 log 爆出了一个什么 token not found 就是说你的 token 没有传递过来。那好你既然要token ，咱就把 token 传递给你。好了。 OK token 和 username 统统教给你调用一次。同学们发现这个 status 变了，变成了403。那我们再来看一下 log 你看它这里报了一个叫 invalid token 那说明你的 token 验证没有通过。好，我们这样去重新 request 一个新的 token 那这个 token 从哪里拿呢？从 authorization server 的 login 方法里面，我们点击一下。好，这里拿到了一个新的 token 我把它 copy 进来，再回到前面的方法中，我们使用这个最新的 token 试一下。走。你。同学们看这里已经获得了正确的结果。


那我们再试几个极端case ，我们把这个用户名改一下，本来是 me 我改成 me too 调用被拦截下来了。403。那把这个 token 中间随便加一个小字符添加一个，一再点击发送。也是403。 OK 说明我们的权限验证框架通过了所有的测试用例。


那么到这里，咱今天这一节小节的课程就到此结束了，我来帮大家回顾一下整个上下半场做了哪些事情。我们首先创建了一个 authorization service 并且抽取了它的 authorization service API 也就是它的接口层。在这个 service 中，我们利用 JW T 的算法，我们实现了 token 的生成以及 token 的验证，还有 token 刷新三个功能。并且咱将这个功能集成到了 gateway 当中，在 gateway 中通过 off filter 提供了一个权限验证的基本流程。 OK 那我们将在电商系统中借鉴这次的 gwt 权限验证，实现一个更精细力度的权限认证流程框架。Ok.同学们，那这一节课程到这里就结束了。在接下来的小节里，我将带大家一起看一下如何在网关层进行一个统一的异常处理。好。同学们，那我们下一小节再见。





