---
title: 2-14 【Demo】基于jwt实现用户鉴权-1
---

# 2-14 【Demo】基于jwt实现用户鉴权-1

[image](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/49190c44-4259-438a-aa1f-b75d1175d45a/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WB7FS5DF%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T225741Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIGn7pqlf6JE%2BppH83tto4motGM1ZZQ%2FhrWZ%2BXIBvXcnBAiEAh2%2B%2Fryh0EBtPqcdEROLdGmolj2BzL%2BjNj%2FAXartg6hQqiAQIxv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDP1iHD3ewyxxNOwKGyrcA5bntRcUYAgaI0Cl3igpexCZYhpjFXW8FNzUmGcEIaTOejIJoOAbUEL5nXwdQlAyGwdzsjdvPr%2BhfeQWDsrD8fNsCpSqBcWd6eFF5ztF68Pe5sc00gPtAtj6Z%2BarSnA9cPTILA1Sz5FuAbrZfa4z0Zeap6gHImWHCCS7qnQpReUjc3DFYKm%2Fa51Tgv%2F7eFyueVTY6qAaN6JAkRAxn3omEtI3fkwFZXR3W94H%2BMVTIhoZyOcIzG3PxDk9Q8ThihrjKhAXfLge99%2FMBb0nHFBk9g0l99d6IX3SEUTHjmWy7iDWCsc%2BG7zVQVAByv7pRRpFhA3ACIMqbNZP0%2FC2obXz2S2qSttH%2B7MgloihNT%2BfHp%2F9A38%2Ft8sHx6ZRUSxdph%2FKhK%2Bu9uC3k71S0OrPxrsMga%2BRTQKKvVvFJt0H9IWpGhIkZbh11lHnEY%2By8dVZXbLu%2FKgIbA5wBL0awTJb%2FO4wuzN2l8p3ddckvVMdzEWSaSETn0w%2Bwk1Y3oNaTZVeEmK7yP7wIpplDNJAKs%2FOoIKQev%2B0qOjIWE1Zb8U1b%2Bl%2F8N5qYrkyAcI%2FDp8IP3rRI82KD9XXnnejjaZK%2BX5klszuUE21nS1bNyfVVimJPX7GqLcEaz%2BWJi0uK1IkPKa6MKS3%2F9IGOqUBe7CFuosG4Td8P4vv%2FzDm9X54J9o8uoHjeeWSqyfesKEz8Q82%2B4IzDj%2BWZWcOrM%2BOgwUkCXYrFPAXtYUib1uy7iqCsV6flzcPaZZ5I0xulsV87E%2BQiqGLCqFo3R4rnJkyiJt0bH%2FMAOVQMhBp7vwiYo1F985FMoF2PjbdZE10pSLz0F5fnQqL1XVHsfqmiOP1Wn1ZpbJIebOqA0qYrEa4BLmMEqcu&X-Amz-Signature=f767448e3e480fd4f2cbbe8a3c0b10d93aad221e6243adf17e5efdcb4cf2297f&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

[image](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/7cf63da3-9227-4783-a4f4-2a51efb6185a/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WB7FS5DF%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T225741Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIGn7pqlf6JE%2BppH83tto4motGM1ZZQ%2FhrWZ%2BXIBvXcnBAiEAh2%2B%2Fryh0EBtPqcdEROLdGmolj2BzL%2BjNj%2FAXartg6hQqiAQIxv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDP1iHD3ewyxxNOwKGyrcA5bntRcUYAgaI0Cl3igpexCZYhpjFXW8FNzUmGcEIaTOejIJoOAbUEL5nXwdQlAyGwdzsjdvPr%2BhfeQWDsrD8fNsCpSqBcWd6eFF5ztF68Pe5sc00gPtAtj6Z%2BarSnA9cPTILA1Sz5FuAbrZfa4z0Zeap6gHImWHCCS7qnQpReUjc3DFYKm%2Fa51Tgv%2F7eFyueVTY6qAaN6JAkRAxn3omEtI3fkwFZXR3W94H%2BMVTIhoZyOcIzG3PxDk9Q8ThihrjKhAXfLge99%2FMBb0nHFBk9g0l99d6IX3SEUTHjmWy7iDWCsc%2BG7zVQVAByv7pRRpFhA3ACIMqbNZP0%2FC2obXz2S2qSttH%2B7MgloihNT%2BfHp%2F9A38%2Ft8sHx6ZRUSxdph%2FKhK%2Bu9uC3k71S0OrPxrsMga%2BRTQKKvVvFJt0H9IWpGhIkZbh11lHnEY%2By8dVZXbLu%2FKgIbA5wBL0awTJb%2FO4wuzN2l8p3ddckvVMdzEWSaSETn0w%2Bwk1Y3oNaTZVeEmK7yP7wIpplDNJAKs%2FOoIKQev%2B0qOjIWE1Zb8U1b%2Bl%2F8N5qYrkyAcI%2FDp8IP3rRI82KD9XXnnejjaZK%2BX5klszuUE21nS1bNyfVVimJPX7GqLcEaz%2BWJi0uK1IkPKa6MKS3%2F9IGOqUBe7CFuosG4Td8P4vv%2FzDm9X54J9o8uoHjeeWSqyfesKEz8Q82%2B4IzDj%2BWZWcOrM%2BOgwUkCXYrFPAXtYUib1uy7iqCsV6flzcPaZZ5I0xulsV87E%2BQiqGLCqFo3R4rnJkyiJt0bH%2FMAOVQMhBp7vwiYo1F985FMoF2PjbdZE10pSLz0F5fnQqL1XVHsfqmiOP1Wn1ZpbJIebOqA0qYrEa4BLmMEqcu&X-Amz-Signature=8423fca5f274b19f09435ea8041019d89bb6f7987f7ffeb13662fac38e7e5382&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

[image](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/8541b629-a331-4698-b0b3-a0fcfb03ed5c/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WB7FS5DF%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T225741Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIGn7pqlf6JE%2BppH83tto4motGM1ZZQ%2FhrWZ%2BXIBvXcnBAiEAh2%2B%2Fryh0EBtPqcdEROLdGmolj2BzL%2BjNj%2FAXartg6hQqiAQIxv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDP1iHD3ewyxxNOwKGyrcA5bntRcUYAgaI0Cl3igpexCZYhpjFXW8FNzUmGcEIaTOejIJoOAbUEL5nXwdQlAyGwdzsjdvPr%2BhfeQWDsrD8fNsCpSqBcWd6eFF5ztF68Pe5sc00gPtAtj6Z%2BarSnA9cPTILA1Sz5FuAbrZfa4z0Zeap6gHImWHCCS7qnQpReUjc3DFYKm%2Fa51Tgv%2F7eFyueVTY6qAaN6JAkRAxn3omEtI3fkwFZXR3W94H%2BMVTIhoZyOcIzG3PxDk9Q8ThihrjKhAXfLge99%2FMBb0nHFBk9g0l99d6IX3SEUTHjmWy7iDWCsc%2BG7zVQVAByv7pRRpFhA3ACIMqbNZP0%2FC2obXz2S2qSttH%2B7MgloihNT%2BfHp%2F9A38%2Ft8sHx6ZRUSxdph%2FKhK%2Bu9uC3k71S0OrPxrsMga%2BRTQKKvVvFJt0H9IWpGhIkZbh11lHnEY%2By8dVZXbLu%2FKgIbA5wBL0awTJb%2FO4wuzN2l8p3ddckvVMdzEWSaSETn0w%2Bwk1Y3oNaTZVeEmK7yP7wIpplDNJAKs%2FOoIKQev%2B0qOjIWE1Zb8U1b%2Bl%2F8N5qYrkyAcI%2FDp8IP3rRI82KD9XXnnejjaZK%2BX5klszuUE21nS1bNyfVVimJPX7GqLcEaz%2BWJi0uK1IkPKa6MKS3%2F9IGOqUBe7CFuosG4Td8P4vv%2FzDm9X54J9o8uoHjeeWSqyfesKEz8Q82%2B4IzDj%2BWZWcOrM%2BOgwUkCXYrFPAXtYUib1uy7iqCsV6flzcPaZZ5I0xulsV87E%2BQiqGLCqFo3R4rnJkyiJt0bH%2FMAOVQMhBp7vwiYo1F985FMoF2PjbdZE10pSLz0F5fnQqL1XVHsfqmiOP1Wn1ZpbJIebOqA0qYrEa4BLmMEqcu&X-Amz-Signature=b86dbff89c905318a299899f3712afa44d4db61ce2297411d9b8bd1fbe91dd07&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

嗨慕课网的各位同学们，大家好，所有的业务系统中有一个功能，它是必不可少的是鉴权服务。什么是鉴权呢？简单来说它就是登录以及用户的权限验证等等。在业界，对用户鉴权这一块来说，咱也有很多成熟的解决方案，说 spring security 还有 iPad shero 我个人用下来来说还是蛮喜欢 sharo 这种解决方案的。我们在现在的大型互联网应用中，经常听到这样一个词叫 to FA 或者叫 O auth 2.0。本质上它们都是基于一个 token 来做用户访问的。这个图肯我们可以把它理解成一个打开自己应用的钥匙。那在这一节里我也跟大家介绍一个简单的基于 token 的权限验证方案，它就是咱常说的 gwt 鉴权，把这个鉴权服务集成在网关层面，也就是说由服务网关来负责用户的鉴权。


OK 咱来看一下本节当中涉及的三个主要内容部分，咱先创建一个独立的微服务，这个服务的名称就是 of service 可以把用户登录以及用户的权限认证，包括 token 的刷新等等服务集成到这个 service 中。紧接着第二步是添加 gwt service 实现 token 的创建和验证的 token 创建，也就是用户登录过后给你分发一个新的访问。


token 验证指的就是当用户使用这个 token 去访问远程服务的时候，我要对你的 token 还有用户名进行验证，看他是不是一个有效的 token 最后一个部分就是在网关层集成 auth service 我们这里通过一种简单的方式，也就是在网关层添加一个 auth filter filter 会过滤所有用户的访问请求，如果它没有验证，则返回一个特定的 status 比如 403 forbiddenok 这一节， coding 的任务还是蛮重的，同学们有的福报来享受了。

[image](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/abd5d86f-9ff7-4605-b72e-a9a2168618a6/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WB7FS5DF%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T225741Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIGn7pqlf6JE%2BppH83tto4motGM1ZZQ%2FhrWZ%2BXIBvXcnBAiEAh2%2B%2Fryh0EBtPqcdEROLdGmolj2BzL%2BjNj%2FAXartg6hQqiAQIxv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDP1iHD3ewyxxNOwKGyrcA5bntRcUYAgaI0Cl3igpexCZYhpjFXW8FNzUmGcEIaTOejIJoOAbUEL5nXwdQlAyGwdzsjdvPr%2BhfeQWDsrD8fNsCpSqBcWd6eFF5ztF68Pe5sc00gPtAtj6Z%2BarSnA9cPTILA1Sz5FuAbrZfa4z0Zeap6gHImWHCCS7qnQpReUjc3DFYKm%2Fa51Tgv%2F7eFyueVTY6qAaN6JAkRAxn3omEtI3fkwFZXR3W94H%2BMVTIhoZyOcIzG3PxDk9Q8ThihrjKhAXfLge99%2FMBb0nHFBk9g0l99d6IX3SEUTHjmWy7iDWCsc%2BG7zVQVAByv7pRRpFhA3ACIMqbNZP0%2FC2obXz2S2qSttH%2B7MgloihNT%2BfHp%2F9A38%2Ft8sHx6ZRUSxdph%2FKhK%2Bu9uC3k71S0OrPxrsMga%2BRTQKKvVvFJt0H9IWpGhIkZbh11lHnEY%2By8dVZXbLu%2FKgIbA5wBL0awTJb%2FO4wuzN2l8p3ddckvVMdzEWSaSETn0w%2Bwk1Y3oNaTZVeEmK7yP7wIpplDNJAKs%2FOoIKQev%2B0qOjIWE1Zb8U1b%2Bl%2F8N5qYrkyAcI%2FDp8IP3rRI82KD9XXnnejjaZK%2BX5klszuUE21nS1bNyfVVimJPX7GqLcEaz%2BWJi0uK1IkPKa6MKS3%2F9IGOqUBe7CFuosG4Td8P4vv%2FzDm9X54J9o8uoHjeeWSqyfesKEz8Q82%2B4IzDj%2BWZWcOrM%2BOgwUkCXYrFPAXtYUib1uy7iqCsV6flzcPaZZ5I0xulsV87E%2BQiqGLCqFo3R4rnJkyiJt0bH%2FMAOVQMhBp7vwiYo1F985FMoF2PjbdZE10pSLz0F5fnQqL1XVHsfqmiOP1Wn1ZpbJIebOqA0qYrEa4BLmMEqcu&X-Amz-Signature=53295ad2abffaea17dc80cbc15f581ac4160dda3ae50d4a9b3016be3b257ac4f&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

OK 同学们准备好的话跟我到银泰 dj 里面，我们开动起来编程是我快乐 996 是我的福报。咱这一节的内容比较多，还要分上半场下半场。所以咱废话少说，直接一个字就是干B ，我们先要创建一个新的项目。就是 off service 的接口层，前面咱不是学了phone ，对不对？咱要把接口层单独给它抽出来，这样的话方便其他业务方进行调用。那咱给接口整起的名字叫 of service apiok 一个回车。这里的 module name 还依然和前面保持一致，把它放在哪个文件夹，咱就不单独创建文件夹了，给它扔到 gateway 里面，因为咱是 gateway 这一节中的一部分。


点击 finish 321 处好，接下来咱给它添加 dependency 是接口层，所以 dependency 当然是越少越好了。从其他的项目里面，先把这两个需要的 dependency copy 过来，随便找一个我们 copy 谁呢？第一个， I spring boot a web starter 是咱其中的一个需要的模块给它 copy 过来。模块咱需要 open feed dependency ，因为我们要发起远程调用这里需要借助 fin 我们在 fin consumer 里面找到 open fin 的 dependency 给它 copy 过来，然后复制到这里来，顺手把 package 类型改成价 servicecpi 的 dependency 就已经做好了。那接下来给它定义一些我们需要用到的 entity 在定义之前创建一个 com.imock.spend cloud 的文件夹。


那么接下来定义第一个 entity 咱能想到的需要用到的第一个 entity 应该是叫 accountcounts 是什么意思呢？啊它呢就相当于是一个封装啊什么内容呢？唉我们这里来看，第一个封装的内容当然是 username 了，它还可以把它写成叫 user ID 因为假设 user name 是一个微信的 wechat ID 一样的唯一用户 ID 那么我们就使用它来标示这个用户。


除了 user name 以外，我们当然还要再封装一个 token 也就是生成的访问密钥对不对？还有一个跟 token 息息相关的东西，我们叫它 refresh tokenfresh token 是什么意思呢？也就是说当你的 token 接近过期时效的时候，通过 refresh token 可以生成一个新的 tokenok 定义了这三个属性以后，我们把 long book 的 annotation 加上去 data 使它自动生成 get set 方法，然后把 build 也塞上去。这个龙book ，一用就上瘾。


这个 annotation 加个没完下这两个注解分别是生成一个包含全部属性的构造器，以及一个不包含任何属性的空构造器。好， account 定义完成以后，咱再来尝试定义一个 error code。Ok. L code 是什么含义呢？它定义了咱在访问过程中产生了一系列的异常 code 比如说我们可以一个 success code 对不对？也就是说权限验证完全正确，token也正常返回了这个类型，我们给它定义成 long 型叫什么名字就叫success 。简单粗暴，success代表着成功。那你的成功是建立在别人的什么痛苦之上，这些痛苦的 error code 我们也把它定义起来。 final 这些痛苦都有哪些呢？分别是 incorrect password ，我们随便定义一些错误或接下来再定义一个 user not founduser not found 。也就是你尝试用不存在的用户名来进行访问。上有些带有恶意行为的人，他会使用类似撞库的方式来访问你。如果你给他返回 incorrect password 那么就潜意思的告诉他了什么？告诉他你访问的用户名是对的，只是密码不对。那咱不能告诉他这个用户名存不存在。


所以说通常不管用户名错误还是密码错误，我们都给他返回一个统一的错误提示，叫用户名或密码错误。那这里只是一个简化版的权限验证，就暂时定义这三个 L code 了。好， L code 定义完之后，我们还要再包装一个叫 responseresponse 这又是个什么鬼 boss response 是当你调用我的鉴权服务或者是生成 token 的服务，总归会给你返回一个处理结果。对不对？这个处理结果包含两部分，一个就是它的 error code 实际上咱 error code 也可以定义成一个枚举类。在这里蓝省市了就不把它定义成枚举了，直接返回一个 stagers code 除了 error code 以外，把 account 要给加上。 OK 那 account 里面就包含了新生成的 token 和 refresh token 等等。


好，我们这里再给它添加一个 data 一个 builder 剩下两个构造器。方法，咱从前面创建的 count 里面把它 copy 过来。那定义到这儿，我们需要用到的所有 entity 都已经定义完成了。


接下来定义一个主角接口层，创建一个 class 记得把它的类型选成 interface 有的同学喜欢命名成 I 开头的 I of service 也有的同学喜欢把 I 去掉成 of service 然后在最终的实现类后面加上 implementation impl 实际以上两种方式都可以，我个人比较喜欢定义成 I 开头的接口类型。那我这次非要反其道而行之，我把它定义成 auth service 。创建完 service 以后，我们给它添加几个方法，先一顶绿帽子给它扣上 client 你的分 client 是提供了什么服务呢？我们叫 auth serviceok 那它这就是服务名。除了服务名以外，我们要提供一个 lock in 的服务对不对？ locking 的服务也返回一个 response 它的方法名我们叫 login 或者叫 create token 两种方式都可以上都是一样的，就把它叫 login 好了，locking in 服务，它传入的一个 request param 是用户名，这是不可或缺的。


User name. 除了用户名，相应的还应该有一个什么？密码对不对？那我再传入一个 request era 把密码也给它塞进来。 Password. 实际上咱应该还有个类似验证码的东西对不对？咱这里就不管它了这个服务的路径是什么 the mapping 给它添加上去，它的路径我们就使用跟方法一样的名称。好了，login然后返回类型，这里要给它加一个 response body 一个 JSON 字符串。


好勒。 login 写完了，接下来咱写第二个方法。第二个方法也是非常重要的，你既然能生成图坑，那么你自然而然的要可以检验这个用户的 token 是不是一个正确的 token 就是咱第二个接口要做的事情。验证 token 同样咱也给它传入两个验证参数，一个自然而然就是token ，这一个 token 光明正大的过来访问了，我总要验证一下你对不对？那这个 token 跟什么结合起来一起验证了？当然是你的用户名了，我们把用户名也给他拿到 usernameok 其实有些 token 的方案并不会验证你的用户名，也就是说你的 token 一旦被别人盗用了会产生什么后果呢？那别人拿到这个 token 用来访问系统，就等同于你自己来访问，不会做任何的验证。


那有有些鉴权服务，会对 token 做一些额外的校验，比如说他会联合 username 进行测试这 user ID 等等。那这样别人即使拿到你的token ，他也必须知道一些额外的信息。我们后台服务这里加了这么一道安全措施，不过用的是最简单的使用验证一下用户名称 username 就好了。同样，那咱要给他添加一个访问路径，他不用对任何后台服务做更改，所以给他创建一个 map 请求就可以了。那他的路径是就叫 very fine。


Ok. 用了 login 用了 verify 接下来要做什么呢？不可或缺的就是一个 refresh 我们把方法 copy 一下。 fresh 前面讲过它主要做一件什么事呢？就是说当你的 token 在签发的时候，会给你一个有效期，比如说一年太长了，通常来说是两天三天，你的 token 到了过期时间，那自然而然就不能再使用了。这时候怎么办呢？如果不想重新登录获取一个新的 token 的话，可以使用 refresh 方法用你 token 中的另一半也就是 refresh token 传给鉴权服务。通过验证你的 refresh token ，我们可以为它生成一个新的 token 也就是说 token 是一把敲开服务大门的钥匙。


refresh token 替换这把钥匙的备用钥匙。当你的前面一个钥匙快要失效的时候，就使用 refresh 重新申请一把。那他还能是 get 类型吗？当然不了，因为他做了一些修改了，我们可以用 put 或者是 post 这里把它定义成 post 好了。 OK 到这里为止，接口层就定义完毕了，我们接下来再来定义它的业务实现层，这里好像还露了一个小尾巴，把 response body 给它写上。 OK 咱业务实现层的代码有点多，我们马不停蹄，快马加鞭骑手给他创建一个新的茅酒，这个茅酒的名称咋给他起叫 of serviceok 点击下一步。这里的 module name 跟前面保持一致，也把它一股脑的扔到 gateway 这个文件夹下面走，你 321 出来。


好，这里的 dependency 稍微有那么点多，我们先来看看都有哪些 dependencies 节点加上 OK 开始系数，这里面需要添加的项目了。好，除了这个注解以外，咱接下来要引入一个特殊的注解，我先给他注释一下这个注解是谁呢？ Redis 那为什么要用到 Redis 同学们知道吗？ Redis 用来存放谁的？用来存放我们生成了这些 token 还有 refresh token 的它的 group ID 是 orgspring framework 看又是 spring framework 的出品，真的是一统江湖啦。


spring effect 叫 spring boot starter data 然后后面跟 Redis 除了 Redis 注解以外，我们这里还要一个特殊注解。大家可能前面没见过的，那就是 JWT 网上开源的 gwt 项目包有非常多的，随便挑一个自己是用的得心应手的或者是如果大家对算法比较熟练的话，也可以自己手撸一个 gwt 算法包吗？只要能完成 gwt 的加解密，这些算法就可以了。咱这里就用一个网上能找到的一个比较轻量级的，而且用起来蛮方便的。包它叫 com.auth 0。


下面的阿里法克的 ID 是 Java 杠 gwt 我们的 version 就在这里直接指定好了，用在前面单独配置了。 OK 它的 version 是3.7，我们用一个瑞丽斯版本三点七点零。好，gwt处理完了以后，接下来咱要把这个方法接口给引入进来了。对不对？我们把这个 dependency 加上 dependency 它的 group ID 就是 come.imock 实际上可以用那个通配符把它直接引入进来啊。啊这里懒省市了。 artifact ID 是 of service API 然后它的 version 跟当前版本是保持一致的 project 然后点 versionok 咱就把接口层引入了进来，同时 fin 也被加捞进来。那咱现在的 dependency 都已经配置完成了吗？没有，还缺一个是谁。


尤瑞卡，我们可不能把这个最关键的有瑞卡给漏掉，好到项目里面 copy 过来加进来。 OK 那顺手的再把 X rate 给添加进来，这也是个好习惯了。实际上大家可以把 X rate 放到顶层项目中，自动为每一个紫毛酒都把它引入进来。全部都引入进来以后，我们创建一个顶层的项目包，它的名字 com.imock.spring cloud 又开始撸代码了，代码量会略那么大一些。好，咱起手给它添加一个新的启动方法叫 of applicationok 然后闷函数咱就从其他地方 copy 过来。好了，走，你拿过来。以前小时候抄作业都不说抄叫借鉴一下哟借鉴错了，把闷方法给漏掉了，抄作业可不能少抄咱要把全部的都给抄下来。除了名字以外多少抄多少。


OK 再来给这个闷函数添加几顶绿帽子，以顶带上 spring boot application 带上另外一顶是 enable you 瑞卡 client 好，定义完这两个类以后，咱来定义底层的核心流程。这里在下面创建一个类，给大家起名叫 gwt service 我们就不创建接口层了，一切从简。好收集小桌板。咱正儿八经摆正姿势写代码。这个类上面给它添加一个 loglog 下面再给它定义成 service 把它初始化起来。


OK 好勒，定义完注解咱来开始。欢脱的定义方法体。方法总共有两个方法不多。第一个方法是生成 token 根据谁来生成 token 呢？当然是外面传入的 account 对象了，看对象里面会包含用户名啦或者是其他的某些属性，咱就放这不管了。先来看下面一个方法。第二个方法定义的是谁呢？他是 verify 方法 verify 是什么意思也就是说我要验证你的 token 是不是属于当前用户的，也就是 token 的验证服务。 OK 它返回一个 true 或者 false 证明你的 token 验证有没有过。我们挨个方法先写起，先写哪一个。


第一个，先写 token 的方法，但凡调用到这个方法，说明他的 login 都已经成功了。那么这里就直接给它生成一个 token 就好了。把 login 也就是验证用户名和密码的环节省掉了。这里直接来生成一个 token 生成 token 之前，我要知道当前是什么时候，来看看是不是良辰吉日。好勒，纵使它是良辰吉日又何妨？我们先把它放这不用待会，再来看它有什么用处。二个属性我们要声明一个算法，algorithm这个算法顶什么用。这个算法就是生成 token 所要用到了的很关键了。然后这个算法其中也有一个很关键的参数是它的 key 我们先把它打进来。你采用哪种算法类型呢？不用采用太高级的算法，我们用 hma 256。


OK 这里 256 要求输入一个什么？ Secret. secret 是一个很关键的 kill 这里用一个简单的方式直接指定好这个 K 的名称就叫 change it 是，在生产环境里面就是大而加正儿八经的线上环境千万不能这样配置。通常来讲，咱生产环境上的 K 都是在外部加密好再传入到系统中的。也就是说我们的开发人员实际上是接触不到这个 K 的开发人员获得这个 K 它的危害程度不亚于山库跑路，所以咱给它起名字叫 change it 就是说务必要记得更换一下，我需要不要加一行注解，告诉她们生产环境不能这么用，要不然大家得说老师用的方法真是low 。


好，您声明好了，以后算法也指定了。那么咱接下来生成 K 楼，同学们看这里怎么来生成使用 JWT 的方法。一个 createcreate 什么内容呢？这里有很多个属性，我们先来看看 issueissue 是什么鬼 issue 就是它的发行方。我的 issue 咱在这边声明一个 final 的变量叫 issue 发行者是谁那就是姚老师了，我们把这个 issue 传入进去，因为咱待会在 WiFi 的时候也会验证这个 issue 所以它在某种程度上可以加强你的健壮性。即便外面某些途径获取到你的 key 那么依然不能破解你的算法。为什么，因为他不知道你的 issue 是谁。 OK 好，咱的医师在生产环境里面也需要做加密的。


issue 以外还有一个 with the issue at 这是什么意思啊？这就是告诉大家这个 key 是在什么时间点生成的？咱前面算好的这个良辰吉日。 date 老黄历说了，此时特别适宜生成 jwtok 那咱生成完了前面两个以后，我们要生成一个关键属性，we的 expires at 它是什么？它是过期时间。 OK 我们这里声明一个 new day new day 采用当前的这个生成时间，再加上一段时间加上什么？上一个过期时间，咱把过期时间在上面定义好。 OK 它应该是一个 long 型，我们给它起名叫 tokenaxp 是 expiration 的意思。 time 给它多少的过期时间呢？ 18 个十百千，这是 60 秒。好勒，把这个时间传入进去。 OK 船跑偏了，咱应该把它传到里面的括号里。好勒，过期时间传好以后，接下来咱添加几个很特殊的属性，为 claim 类目，就是一些小机关了，我们可以把自己想添加的任何自定义的属性给它添加进来。我说我这里想添加 user name 咱还是在上面定义好一个变量，这样也好方便。


在下面的 verify 里面使用 user name 好给这个 username 起名就叫username。 Claim. username 里面传入谁呢？我们这里就要传入 account 的。 Get username. 待会儿讲 verify 的时候，可是要用到它的同学们如果有其他的属性需要传入。比方说我需要传入一个 role 对不对？咱要获得这个用户有么样的权限？通常在企业级应用里面，这个 role 会从 LDAP 的等服务里面传入进来。那同学们知道这个点就好。


OK 那咱的所有的属性都已经塞入完毕了，最后一步要干什么？要签发签发总统令用谁来签发？前面生成的这个算法好搞定，你签发完成以后，我们要把这个 token 给他 return 回去。同时这里打一行 log 咱做事有始有终已经办完了，要给上面的人一个交代，叫 gwt generatedgenerated 给谁呢？我要给一个用户 generate 拼错了，generated这个用户名咱在这里传入进来，从 account get 到用户名，然后传入的这个 token 要不要打印出来啊？同学们算了吧，还是不要打印出来。他在写代码的时候要有一个安全的意识，有些东西是不能打印到 log 里面的。很多同学现在写一些自己的小项目的时候，把用户名和密码全部打印进去了。我的天哪这个被公司查到，可是要背锅的。


生成了密钥以后，我们接下来要验证它怎么个验证法，我们来看，在一开始打一行 log 告诉大家，我要干什么事了，我要干什么？ verifying gwt 好，给谁？ verify JWT ，咱要把它的用户名称给打出来，use a name 把 user name 传入进来。


好嘞，这里一个 try catch，因为人生总有各种的意外发生，你不保证它是直发生还是待会发生，我们先把这个 exception 全部给它 catch 起来。 exception 如果看识到了异常，同样的，我们打一行 log 告诉他 off build 然后把他的异常信息给他打印出来就好了。


好，到此结束，我们给他 return 一个 force 那在 try 里面怎么来写这个验证的逻辑，同样也要说明一个算法，把上面的这个算法给 copy 下来，你加密用了同一套算法，自然而然的解密也要用同一套算法对不对？那接下来我们声明一个类叫 gwt very fire 他的专门用来验证 gwt 的内容。


好， gwt verify 我们给它起名也叫verifier ，它怎么来验证法呢？我们同样的用 gwt 的 static 方法生成一个验证器，验证器怎么来生成？第一步它需要算法，告诉他怎么来加解密。除去算法以后我们要验证哪些内容？同学们前面在你生成阶段添加的所有内容咱都可以去验证。好，那我这里先点名，我要验证发行者，我看是不是姚老师发行的。如果是其他黄老师李老师，那咱不管张老师发行的也不行。


好。验证完了 issue 以后，我们还要验证一个 M 是谁？咱前面创建的 username 对不对？把它塞入进来，看看你这个 token 里面的 user name 是不是你传入进来这个 user nameok 那我们只验证这两个信息，其他信息就得过且过，把它放过去。好了，怎么来验证非常简单，只要这样就好。 verify.verify 把 token 传进去，万事俱备。那同学们可能疑问了，为什么不 return 他呢？爱卿们多虑了，不用 return 他，如果你其中有任何错误，在这个方法中他直接抛出一场。也就是说当你方法安然无恙的走到这个 return 这一步的时候，那就是一切验证都通过了。


OK 那咱这个类就宣告完成了，在这边添加一个注释。其实同学们写代码，即使你写得再烂，只要注释齐全，没人会说什么话的。也叫态度要端正对吧。能力是一方面，态度也要端正。这里给它写叫生成 token 下面给他写校验 token 感觉这两个注解相当于没写。校验 token 好勒由总比没有。好嘛，咱生成了 JWT service 接下来要去创建真正的 ctrl 了。同学们，那咱现在开启一段中场休息时刻，广告过后再继续接下来的精彩内容。下半场我们再见。

[image](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/2c46281a-1a20-46b7-b3ca-987b75de1dac/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WB7FS5DF%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T225741Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIGn7pqlf6JE%2BppH83tto4motGM1ZZQ%2FhrWZ%2BXIBvXcnBAiEAh2%2B%2Fryh0EBtPqcdEROLdGmolj2BzL%2BjNj%2FAXartg6hQqiAQIxv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDP1iHD3ewyxxNOwKGyrcA5bntRcUYAgaI0Cl3igpexCZYhpjFXW8FNzUmGcEIaTOejIJoOAbUEL5nXwdQlAyGwdzsjdvPr%2BhfeQWDsrD8fNsCpSqBcWd6eFF5ztF68Pe5sc00gPtAtj6Z%2BarSnA9cPTILA1Sz5FuAbrZfa4z0Zeap6gHImWHCCS7qnQpReUjc3DFYKm%2Fa51Tgv%2F7eFyueVTY6qAaN6JAkRAxn3omEtI3fkwFZXR3W94H%2BMVTIhoZyOcIzG3PxDk9Q8ThihrjKhAXfLge99%2FMBb0nHFBk9g0l99d6IX3SEUTHjmWy7iDWCsc%2BG7zVQVAByv7pRRpFhA3ACIMqbNZP0%2FC2obXz2S2qSttH%2B7MgloihNT%2BfHp%2F9A38%2Ft8sHx6ZRUSxdph%2FKhK%2Bu9uC3k71S0OrPxrsMga%2BRTQKKvVvFJt0H9IWpGhIkZbh11lHnEY%2By8dVZXbLu%2FKgIbA5wBL0awTJb%2FO4wuzN2l8p3ddckvVMdzEWSaSETn0w%2Bwk1Y3oNaTZVeEmK7yP7wIpplDNJAKs%2FOoIKQev%2B0qOjIWE1Zb8U1b%2Bl%2F8N5qYrkyAcI%2FDp8IP3rRI82KD9XXnnejjaZK%2BX5klszuUE21nS1bNyfVVimJPX7GqLcEaz%2BWJi0uK1IkPKa6MKS3%2F9IGOqUBe7CFuosG4Td8P4vv%2FzDm9X54J9o8uoHjeeWSqyfesKEz8Q82%2B4IzDj%2BWZWcOrM%2BOgwUkCXYrFPAXtYUib1uy7iqCsV6flzcPaZZ5I0xulsV87E%2BQiqGLCqFo3R4rnJkyiJt0bH%2FMAOVQMhBp7vwiYo1F985FMoF2PjbdZE10pSLz0F5fnQqL1XVHsfqmiOP1Wn1ZpbJIebOqA0qYrEa4BLmMEqcu&X-Amz-Signature=b6e543da06b5594d33247ae06d9b0092a3086985b945e95544015e96dad61e15&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)


