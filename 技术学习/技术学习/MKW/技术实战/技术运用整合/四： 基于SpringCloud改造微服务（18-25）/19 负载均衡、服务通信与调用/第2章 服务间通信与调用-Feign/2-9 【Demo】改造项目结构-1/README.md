---
title: 2-9 【Demo】改造项目结构-1
---

# 2-9 【Demo】改造项目结构-1

[image](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/c130509a-addb-415b-8fc8-78caf51a4b1c/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SOUAZ4FI%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T225624Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIE4HeFCxwQiwK0ya8Enbwq4AsY%2F12OHzQ1rdev4R8Fw7AiBhgDd2zFWS%2FCHbQj5swCY9gKftO6ZE5ljpXg4ih8h6ziqIBAjG%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMOWVz0KiW4remydkEKtwDk68NEpyRoJvgDiduTGJFHlEIeeV0fl26wV%2FsjFvy%2FidBsXiIiZwLwnWx2FwrvG0rX4cvyJ0D7vX6eD1BN2D4xX8snP73HtT2DU19FLotgadOOqg0J7dKLnwhdTOxZT7q%2BFhikXgFJI2K1ZRVlI2rv2WZEIS1U1gfO%2FUuX2U%2BbN%2BnMch5CEhfD3VSUFT9ZLjQLXHDnYDFtRP%2BT2hKipUEsC3S1ecyVX0izxTlRaJnAMbFtuiDHRi8OfaC%2BQhwMgQLZU0peQzAsaL29xM4Iai9qHLHN2mepFy7HiIKxBVH7L4bC%2B7CntV%2Bd1KJGi%2BcAceTPnU8Z3YVFZKe1UgcCC7tlATDTvGcESN3hqM8ogdglHXXSfjfN09j9KtNAow7A7JE4s9YILH%2BvKezxusNvd1UfX3xQ%2BEICUSN0NMe8gdxMHARuVZr2YJzSClsK356skh%2B4gXcJ%2FX1i5VeHmQSZ5FW35qDI9caGvFI%2FsG%2F4mn9XevsVgKfwLtaISCGU%2Fc2kwSjkXo5zhUVKx%2BW%2BnQYkggcMin%2Fs8dqSjzHN9Mj20p7Bh67WKC05lvKGzOaRe0RaJ3CZH5IkgFhzh3fMrZ94vCuVlYC9frXL12Au4dLZlI6OSJguRFez37s2yiVcTUw6Ln%2F0gY6pgEu%2B6PruSxmH4pPtA5M2N7I7E%2FUr2L9gyhBt08Pa4cvMe5EevlqpXZ9aorVRtYXYtkxulnk2exiiHs2YiPVfS43qos8pmSRVVTzxABvG4FaVAFY6rS6ORJUAbpfaMNBeIY6TIT7dqdx%2BJ%2FOZIRVRdrjk%2FW%2FVB1e2qhFM3TuCtWJUBl5XSQinohK6lkKGPB7O04cSalCFCS7gv4OD%2BPGXqlvJ384yjJJ&X-Amz-Signature=401eef8a0a00cda57f736414f75f2e27fc2eddb621c99e020c85e2e4c798989f&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

[image](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/2c64324d-3667-42f5-89a2-a8c17bd6e923/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SOUAZ4FI%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T225624Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIE4HeFCxwQiwK0ya8Enbwq4AsY%2F12OHzQ1rdev4R8Fw7AiBhgDd2zFWS%2FCHbQj5swCY9gKftO6ZE5ljpXg4ih8h6ziqIBAjG%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMOWVz0KiW4remydkEKtwDk68NEpyRoJvgDiduTGJFHlEIeeV0fl26wV%2FsjFvy%2FidBsXiIiZwLwnWx2FwrvG0rX4cvyJ0D7vX6eD1BN2D4xX8snP73HtT2DU19FLotgadOOqg0J7dKLnwhdTOxZT7q%2BFhikXgFJI2K1ZRVlI2rv2WZEIS1U1gfO%2FUuX2U%2BbN%2BnMch5CEhfD3VSUFT9ZLjQLXHDnYDFtRP%2BT2hKipUEsC3S1ecyVX0izxTlRaJnAMbFtuiDHRi8OfaC%2BQhwMgQLZU0peQzAsaL29xM4Iai9qHLHN2mepFy7HiIKxBVH7L4bC%2B7CntV%2Bd1KJGi%2BcAceTPnU8Z3YVFZKe1UgcCC7tlATDTvGcESN3hqM8ogdglHXXSfjfN09j9KtNAow7A7JE4s9YILH%2BvKezxusNvd1UfX3xQ%2BEICUSN0NMe8gdxMHARuVZr2YJzSClsK356skh%2B4gXcJ%2FX1i5VeHmQSZ5FW35qDI9caGvFI%2FsG%2F4mn9XevsVgKfwLtaISCGU%2Fc2kwSjkXo5zhUVKx%2BW%2BnQYkggcMin%2Fs8dqSjzHN9Mj20p7Bh67WKC05lvKGzOaRe0RaJ3CZH5IkgFhzh3fMrZ94vCuVlYC9frXL12Au4dLZlI6OSJguRFez37s2yiVcTUw6Ln%2F0gY6pgEu%2B6PruSxmH4pPtA5M2N7I7E%2FUr2L9gyhBt08Pa4cvMe5EevlqpXZ9aorVRtYXYtkxulnk2exiiHs2YiPVfS43qos8pmSRVVTzxABvG4FaVAFY6rS6ORJUAbpfaMNBeIY6TIT7dqdx%2BJ%2FOZIRVRdrjk%2FW%2FVB1e2qhFM3TuCtWJUBl5XSQinohK6lkKGPB7O04cSalCFCS7gv4OD%2BPGXqlvJ384yjJJ&X-Amz-Signature=c3c8d1d42f29cc7bc9d83cd81113e3775aa1afe44d56b2275c46ae8ca801d993&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

[image](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/c2ecbd7b-a31b-44cc-8d8a-491a44480a9e/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SOUAZ4FI%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T225624Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIE4HeFCxwQiwK0ya8Enbwq4AsY%2F12OHzQ1rdev4R8Fw7AiBhgDd2zFWS%2FCHbQj5swCY9gKftO6ZE5ljpXg4ih8h6ziqIBAjG%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMOWVz0KiW4remydkEKtwDk68NEpyRoJvgDiduTGJFHlEIeeV0fl26wV%2FsjFvy%2FidBsXiIiZwLwnWx2FwrvG0rX4cvyJ0D7vX6eD1BN2D4xX8snP73HtT2DU19FLotgadOOqg0J7dKLnwhdTOxZT7q%2BFhikXgFJI2K1ZRVlI2rv2WZEIS1U1gfO%2FUuX2U%2BbN%2BnMch5CEhfD3VSUFT9ZLjQLXHDnYDFtRP%2BT2hKipUEsC3S1ecyVX0izxTlRaJnAMbFtuiDHRi8OfaC%2BQhwMgQLZU0peQzAsaL29xM4Iai9qHLHN2mepFy7HiIKxBVH7L4bC%2B7CntV%2Bd1KJGi%2BcAceTPnU8Z3YVFZKe1UgcCC7tlATDTvGcESN3hqM8ogdglHXXSfjfN09j9KtNAow7A7JE4s9YILH%2BvKezxusNvd1UfX3xQ%2BEICUSN0NMe8gdxMHARuVZr2YJzSClsK356skh%2B4gXcJ%2FX1i5VeHmQSZ5FW35qDI9caGvFI%2FsG%2F4mn9XevsVgKfwLtaISCGU%2Fc2kwSjkXo5zhUVKx%2BW%2BnQYkggcMin%2Fs8dqSjzHN9Mj20p7Bh67WKC05lvKGzOaRe0RaJ3CZH5IkgFhzh3fMrZ94vCuVlYC9frXL12Au4dLZlI6OSJguRFez37s2yiVcTUw6Ln%2F0gY6pgEu%2B6PruSxmH4pPtA5M2N7I7E%2FUr2L9gyhBt08Pa4cvMe5EevlqpXZ9aorVRtYXYtkxulnk2exiiHs2YiPVfS43qos8pmSRVVTzxABvG4FaVAFY6rS6ORJUAbpfaMNBeIY6TIT7dqdx%2BJ%2FOZIRVRdrjk%2FW%2FVB1e2qhFM3TuCtWJUBl5XSQinohK6lkKGPB7O04cSalCFCS7gv4OD%2BPGXqlvJ384yjJJ&X-Amz-Signature=93047780da3fdab93f1f75d0a23e252b7b69e0e116311e84fa1f560c9d5c89ca&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

hello 慕课网的各位同学们，大家好，又见面了，这一节是我们代码实操环节来做什么呢？改造项目结构怎么？改造法，我们来看一下。第一部分，抽取一个公共的接口层，在这个接口层我们尽量保持它的纯洁性，不要引入过多的依赖项。第二部分，我们创建一个服务提供者，然后在服务提供者和接口层之间建立一种关联。最后一步就是创建基于公共接口层的服务消费者。然后把服务提供者和服务消费者全部启动起来，看一下新的项目结构有多么的清爽。

[image](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/c741c5d3-6b77-4abd-a0dd-f4c67951184c/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SOUAZ4FI%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T225624Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIE4HeFCxwQiwK0ya8Enbwq4AsY%2F12OHzQ1rdev4R8Fw7AiBhgDd2zFWS%2FCHbQj5swCY9gKftO6ZE5ljpXg4ih8h6ziqIBAjG%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMOWVz0KiW4remydkEKtwDk68NEpyRoJvgDiduTGJFHlEIeeV0fl26wV%2FsjFvy%2FidBsXiIiZwLwnWx2FwrvG0rX4cvyJ0D7vX6eD1BN2D4xX8snP73HtT2DU19FLotgadOOqg0J7dKLnwhdTOxZT7q%2BFhikXgFJI2K1ZRVlI2rv2WZEIS1U1gfO%2FUuX2U%2BbN%2BnMch5CEhfD3VSUFT9ZLjQLXHDnYDFtRP%2BT2hKipUEsC3S1ecyVX0izxTlRaJnAMbFtuiDHRi8OfaC%2BQhwMgQLZU0peQzAsaL29xM4Iai9qHLHN2mepFy7HiIKxBVH7L4bC%2B7CntV%2Bd1KJGi%2BcAceTPnU8Z3YVFZKe1UgcCC7tlATDTvGcESN3hqM8ogdglHXXSfjfN09j9KtNAow7A7JE4s9YILH%2BvKezxusNvd1UfX3xQ%2BEICUSN0NMe8gdxMHARuVZr2YJzSClsK356skh%2B4gXcJ%2FX1i5VeHmQSZ5FW35qDI9caGvFI%2FsG%2F4mn9XevsVgKfwLtaISCGU%2Fc2kwSjkXo5zhUVKx%2BW%2BnQYkggcMin%2Fs8dqSjzHN9Mj20p7Bh67WKC05lvKGzOaRe0RaJ3CZH5IkgFhzh3fMrZ94vCuVlYC9frXL12Au4dLZlI6OSJguRFez37s2yiVcTUw6Ln%2F0gY6pgEu%2B6PruSxmH4pPtA5M2N7I7E%2FUr2L9gyhBt08Pa4cvMe5EevlqpXZ9aorVRtYXYtkxulnk2exiiHs2YiPVfS43qos8pmSRVVTzxABvG4FaVAFY6rS6ORJUAbpfaMNBeIY6TIT7dqdx%2BJ%2FOZIRVRdrjk%2FW%2FVB1e2qhFM3TuCtWJUBl5XSQinohK6lkKGPB7O04cSalCFCS7gv4OD%2BPGXqlvJ384yjJJ&X-Amz-Signature=2d3f4d440fa645aa1d928be2e21816fe322f5f3532ece759bb78e547839c4948&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

好，接下来我们就抄起家伙准备开工，每天 coding 1 小时，健康工作 50 年。接下来我们就要对这个 fin 进行好的改造。好，谢谢你新建一个module ，我们这次改造涉及到三个模块，consumerclient还有 interface 第一个 module 我们新建一个谁当然是 interface 的对不对？我们给它起个名字叫 fin 杠 client 在杠 intf 证明它是什么，证明它是 think client 的 interface 层，待会儿我们再去创建一份 client 好，next这里保持 module name 和前面的 artifact ID 保持一致，然后依然把它放到 fin 文件夹下，点击 finish 出来。


好，这里我要添加一些 dependency 前面我们说过要保持它的这个纯洁性，它有多纯洁？仅保持它最低限度的功能，不要多添加依赖。我们这里先把 dependence 给加上去，这不仅仅是一个纯 Java 的代码，它还有一些 annotation 这个 annotation 可是必须要通过依赖来引入进来的。这里我打算到 fin consumer 里做个借鉴，从这里面 copy 一些依赖过来。


大家看这四个依赖我需要哪些，open fan 需不需要？当然需要了它是份接口的依赖。所以说这一个依赖我要了。第二个依赖，我们要给它指定一些 request mapping 对不对？所以它也需要 spring boot 的 starter 对不对？那我把这两个依赖 copy 过来。这中间还有个拦路虎，把它一起 copy 过来，到那边再给它干掉。好，中间这个 actuator 干掉。好，这里有两个依赖，添加进来以后，给它指定一个 package 类型是。这好，这就完工了。那么接下来就要去写几行代码了，我们依然在 Java 里面创建一个如雷贯玩的包名，大家大声的说出来叫什么？ com.imock.spring cloud。


Ok. 创建完以后，我们说它是一个接口层，那接口层要有什么？要有接口对不对？但是在创建接口以前，我还想创建一些泡酒类，我们这时候可以借鉴哪里啊？ eureka client 对不对？前面的 fin consumer 是调用的，谁调用的正是 eureka client 那我从 eureka client 里面，把需要的类给 copy 进来。好嘞，第一个类这有个 friend 而是那个 post 接口。大家还记得吗？它需要用到的返回值数参数，把它给 copy 过来，原封不动放到这里。


copy 了 friend 以后，接下来我创建一个 interface 叫什么名字呢？我们就给它起名就叫 I service ，一切从简。有了 I service 以后，我要定义方法了对不对？这个方法不想收的，我还是想偷偷懒从哪里 copy 过来呢？ eureka client the controller 里。这不线程有两个方法吗？
Say hi say hi.


多一声的问候，我把这两个问候都给 copy 过来， copy 到 I service 里面。那看这是方法，它当然不能有实现喽。接口层的实现我们把它删掉，下面一个实现也把它给删掉。好，那这里就结束了吗？当然没有，我们前面引入的 fin 依赖，这时候就派上用场了，对不对？给它加上一个 fin client 那它的值是什么？还是 ureka client 吗？ no no no 不是了，我们接下来要创建自己的 fin service provider 所以我们这个名称不再叫尤瑞卡了，还有自立门户，它叫 finklantok 这就结束了吗？似乎是结束了，但是还会不会有遗留的问题，等到待会我们启动项目的时候再来看。


那同学们可能会问了，你这个接口层你说引入的依赖尽量少，但是你引入了 fen 如果我给下游应用，它并不使用 fen 也不使用 spring cloud 怎么办呢？你这个 fin 的依赖岂不是污染人家的纯洁性了？你保持纯洁，人家这个纯洁性就保证不了了。


no worry 我们怎么办呢？我们把这个 fin 的 interface 提供给那些需要用到 fin 的服务方。对那些没有用到 fin 的同学们，我们什么都不加，我们这个依赖就给他提供一个简单的接口层，让他们自己来实现就好了。所以说很多上游应用通常都会打两个包什么意思啊？一个包专门给 sprint cloud 的接入方，另一个包专门给那些不用 spring cloud 的接入方，这样两全其美。Ok.那既然我们这套架构是基于 spring cloud 所以说我这里就不带大家创建另外一个包了，只用这一个 interface 从创建完了以后，接下来该创建谁了？按预定计划。


接下来应该是服务提供者，我们再创建一个 module 这个服务提供者咱是自立门户的，不再用 ureka client 了。这个服务提问者的 artifact 我们叫 fin client 回车下一步里面，把它依然放到 fin 文件夹下，大家可以看到 fin 里面发展壮大了是吧。有小伙伴们了，好，放进去以后这里该轮到给他添加，依赖了都添加谁呢？我们依然从 fin consumer 里把它借鉴回来一部分。


首先尤瑞卡需不需要？需要，因为你是一个服务提供者，要到服务中心注册对吧？那剩下的三个通通拷贝过来，我们都是需要的。但是其中最后一个我可以暂且不 copy 待会大家就知道了。好，把这三个给 copy 过来，在分 client 里面创建一个 dependencies123 排排坐排好之后为什么不要粪呢？大家知道吗？因为我要把接口层引入进来了，那粪从哪里引过来？当然是从接口层过来了。对不对？那他的 group ID 是什么？一家伟大的公司 come.imock group ID 定义完了。


artifact ID 是什么？我们刚才才写过的叫 thin client RN TF interface 而这个 version 已经弹出来了，但是我还不想这样写，我想让它根据我的主版本可以往上升级来自动升级。那这里我用占位符给它写上 project version 已经打印出来了，拷走了 project versionok 那我们的 fin 这坨 fin 就从这个接口层被引入进来了。所以我们在这里不用额外声明接下来是不是要写代码去啦。


我们到这个 Java 类里面创建一个package ，不用说大家都知道该创建什么类型的 package 啦。 imock.spring cloud 好，创建完以后要开始在里面撸代码了。先创建一个入口类，千里之行始于足下。这个入口类的名字就叫做 thin client application 我们的门户招牌接下来就要打一串很带感的 public staticok 我不想让这个赶来的这么快，我们直接 copy 好了，thin consumer 里把这一串字给 copy 过来，好，放到这里给他的 class 换一个名称。 OK 完美。接下来给他加哪些annotation 、友瑞卡要不要了？ enable eureka 当然需要还有什么呢？还有 sprint boot application 对不对？还有什么呢？ thin 有没有啊？小伙伴们，我们创建的是谁？ client 它并不需要调用粪接口，所以我们这个粪就先不要出头了，好不好？去掉入口类有了，接下来需要创建谁？ controller 是不是啊？我们这个 controller 可省事儿嘞，有多省事儿，大家来看。


好，收起小桌板，专心致志地创建 ctrl 的代码。首先顶头的谁 rest ctrl 这个不能少，给它加一个 log sl four G 好，那这里跟以前不一样了，我要实现一个接口，这个接口是谁 I service 既然实现了接口，我要实现接口里的方法对不对？好，这就完事了。那我这个方法体，从以前的代码里面把它直接 copy 过来，从谁 eureka client 里面把它给 copy 过来。第一个 say hi 第一声问候我们返回一个当前的端口，那这个端口我们再给 copy 过来。自曝门户这个端口。


Ok. 第二个方法依然选择 copy 所以说大家在程序员的代码库里经常发现一份代码，好几份 copy 这也是我们会加上一些 sona check 利用 sona 检查代码重复率，强迫你不要犯这种 copy pastecopy paste 的习惯，到这里是不是就完事了？还有什么？大家想想一想还有配置是不是？配置文件可少不了，在 resources 文件夹下创建一个 file 叫 application.properties 好，下面给它起一个如雷贯耳的名字，spring点什么 [application.name](http://application.name/) 它的名字就叫 fin client。


接下来要给他起端口了，实际上这个端口更像是一个名字，因为我们都是在本机做测试，每一个端口都要不能重复前面的分 consumer 是多少端口，同学们还记得吗？40,001，那我给他这个分 client 起40,002。好了，四万零二完事了之后还需要谁？尤瑞卡对不对？从前面给 copy 过来，好靠背上，那我们什么都已经创建好了对不对？接下来要测试一把，我先把注册中心给它搭起来，这里直接启动注册中心，接下来再启动当前的这个服务类，也就是 think client application 的闷方法，直接把它启动起来。


好走起 run 启动好之后，我们先尝试着调用它几个接口，看是不是都通的 spring 标签成功一半，走往下一切顺利。好，我们这里调用一下它的接口，试一下它的端口是40,002，我们这里调用一个 say hi 发过去成功了。 this is a40,002。好，接着再用 post 请求调用一把，它需要设置一个 header 了对不对？那它的 header 是什么？是 content type 然后 value 是 JSON 那包的，我们就给它随便添加一个就好了。好，包在这里我复制好了它的名称 name 我们给它传一个 fin 调用一把看一看。它已经返回了，非常成功。那说明我们这个接口已经生效了，大家再回到代码里看一下，我这个方法上面有没有加 get mapping 和 post mapping 并没有，那它加在哪里啊？加在 I service 上对不对？通过这个 get mapping 和 post mapping 是不是很省事，非常简便。对不对？那我这一步创建好了以后，我的 phone clan 塔就已经完整的搭建成功了。


接下来要改造谁了？改造分 consumer 了对不对？那大家是想创建一个新的分 consumer 还是直接在原来的这个上面动刀子？我建议新创建一个，因为原来的这个方便大家回顾我这里，新给他创建一个毛九这样分文件夹下的项目就更壮大了。对不对？说干就干。咦等一下，好像已经到了下课时间。那同学们一起做个眼保健操，等下一节我们再来进行下半场创建。 fin consumer 调用服务发起者。 OK 同学们，眼保健操现在开始，我们下一节再见。




