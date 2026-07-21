---
title: 2-9  [demo】利用After断言实现简易的定时秒杀场景
---

# 2-9  [demo】利用After断言实现简易的定时秒杀场景

[image](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/27439e62-a700-4347-a15a-b3cc0fb13637/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TKW2PBGE%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T225736Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDUbjyjq8tLBPFl%2FjF1mjlG3RUrIke%2Fc%2BjsqOyuWeE5vAIgA7qRxvffBdHPynoVdVck%2FRJJbrJTz3OdHdRBF4iZJLwqiAQIxv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDGur5Xdg4j5YtKbFpircA8vmrfjFdTQjlkSI2ZB3snj%2FQnoFPIyx2jNppmBG%2BRNbExCL8K4S8g5PSsO1W98Yp35NSo8vF30ep36%2FB0Ps%2B4nwNyHZ5mjhWLitIilb%2FLO4o4ksfhk3Qd%2BHJcg1tjiiOD9BZGo1sjFmKX1yZsj7OBgzloW0Ke3rA3IaL%2BKCSys%2BBFRHkWVxNAuZ1GNxIg%2BSUWFmSZ1EUh42IusJCCSZ36Hk40lq14M%2FfiEoeEE4%2BlBKfaA8Xjrp7SxNAxNh5eR8QhrkBiTsq0sNn%2BE9TA7B4z2fJDKb7gibv9gswTKw4DhIlOYAme1MY6TTghELKICe2JbePV1ICBj91oG8wJot5Gnc5fb5pKPUmN1r8JDd%2FB7h9SXmJB2cK2Nx49SAZ2HRaR39MQvf7s0iZLjIkZRjWFIizmy8AdNKkWx78lv0FaVjEBfyTPT%2BpqTu1qzHeuf7E8A8Cv%2Bdy0FIsRL7BG0hSgWZ7QFFeOllpmU2xpfCe4j4AeNWfH97Mk7t00ne4REuqaaMuD3ZTYObUua2nYVPeP5bwySoIMuLIAzBz1o10ReFbMo2XUM2n%2FUqNoPdlycqiTr9EaHKpWEQUIGhaMCbfykKakjYMy1iES9QNVfpWb0PqE7%2FxjJ%2BC8KdHbVUMOy3%2F9IGOqUBwTbF5J4uQVBLbZ9CHRYqiE3MSGi2yrDfZPbkxV10Fa4g5J5fHEJezp0HR5FeZ4yJNQY32nSkkkmJFtZJsH8TpLzjOO%2FOHdW13vuDO51VeZDIkMLoqJD9lQWKJUsT1HW0fHWnV3eTUqMqb22Dhnc0pMp1Va5LxhtEGFUFBy54vJrBi9M7e1oI9XIyZ49GrjhglwVD%2BO6bhA%2BVLjaUHzZYCi%2BW%2FeQQ&X-Amz-Signature=8ef5fb18174ce6864c569b977ada653f18ac295a937e85db47c94fcc2aec0eca&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

[image](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/7a2ff164-1942-46ca-8fad-f19e75f502d9/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TKW2PBGE%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T225736Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDUbjyjq8tLBPFl%2FjF1mjlG3RUrIke%2Fc%2BjsqOyuWeE5vAIgA7qRxvffBdHPynoVdVck%2FRJJbrJTz3OdHdRBF4iZJLwqiAQIxv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDGur5Xdg4j5YtKbFpircA8vmrfjFdTQjlkSI2ZB3snj%2FQnoFPIyx2jNppmBG%2BRNbExCL8K4S8g5PSsO1W98Yp35NSo8vF30ep36%2FB0Ps%2B4nwNyHZ5mjhWLitIilb%2FLO4o4ksfhk3Qd%2BHJcg1tjiiOD9BZGo1sjFmKX1yZsj7OBgzloW0Ke3rA3IaL%2BKCSys%2BBFRHkWVxNAuZ1GNxIg%2BSUWFmSZ1EUh42IusJCCSZ36Hk40lq14M%2FfiEoeEE4%2BlBKfaA8Xjrp7SxNAxNh5eR8QhrkBiTsq0sNn%2BE9TA7B4z2fJDKb7gibv9gswTKw4DhIlOYAme1MY6TTghELKICe2JbePV1ICBj91oG8wJot5Gnc5fb5pKPUmN1r8JDd%2FB7h9SXmJB2cK2Nx49SAZ2HRaR39MQvf7s0iZLjIkZRjWFIizmy8AdNKkWx78lv0FaVjEBfyTPT%2BpqTu1qzHeuf7E8A8Cv%2Bdy0FIsRL7BG0hSgWZ7QFFeOllpmU2xpfCe4j4AeNWfH97Mk7t00ne4REuqaaMuD3ZTYObUua2nYVPeP5bwySoIMuLIAzBz1o10ReFbMo2XUM2n%2FUqNoPdlycqiTr9EaHKpWEQUIGhaMCbfykKakjYMy1iES9QNVfpWb0PqE7%2FxjJ%2BC8KdHbVUMOy3%2F9IGOqUBwTbF5J4uQVBLbZ9CHRYqiE3MSGi2yrDfZPbkxV10Fa4g5J5fHEJezp0HR5FeZ4yJNQY32nSkkkmJFtZJsH8TpLzjOO%2FOHdW13vuDO51VeZDIkMLoqJD9lQWKJUsT1HW0fHWnV3eTUqMqb22Dhnc0pMp1Va5LxhtEGFUFBy54vJrBi9M7e1oI9XIyZ49GrjhglwVD%2BO6bhA%2BVLjaUHzZYCi%2BW%2FeQQ&X-Amz-Signature=2b3bf1261e264bbd7a9af477cc64374512a91be0b734a999a1483740b9783044&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

[image](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/39830853-5634-459c-8626-e585284ad19c/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TKW2PBGE%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T225736Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDUbjyjq8tLBPFl%2FjF1mjlG3RUrIke%2Fc%2BjsqOyuWeE5vAIgA7qRxvffBdHPynoVdVck%2FRJJbrJTz3OdHdRBF4iZJLwqiAQIxv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDGur5Xdg4j5YtKbFpircA8vmrfjFdTQjlkSI2ZB3snj%2FQnoFPIyx2jNppmBG%2BRNbExCL8K4S8g5PSsO1W98Yp35NSo8vF30ep36%2FB0Ps%2B4nwNyHZ5mjhWLitIilb%2FLO4o4ksfhk3Qd%2BHJcg1tjiiOD9BZGo1sjFmKX1yZsj7OBgzloW0Ke3rA3IaL%2BKCSys%2BBFRHkWVxNAuZ1GNxIg%2BSUWFmSZ1EUh42IusJCCSZ36Hk40lq14M%2FfiEoeEE4%2BlBKfaA8Xjrp7SxNAxNh5eR8QhrkBiTsq0sNn%2BE9TA7B4z2fJDKb7gibv9gswTKw4DhIlOYAme1MY6TTghELKICe2JbePV1ICBj91oG8wJot5Gnc5fb5pKPUmN1r8JDd%2FB7h9SXmJB2cK2Nx49SAZ2HRaR39MQvf7s0iZLjIkZRjWFIizmy8AdNKkWx78lv0FaVjEBfyTPT%2BpqTu1qzHeuf7E8A8Cv%2Bdy0FIsRL7BG0hSgWZ7QFFeOllpmU2xpfCe4j4AeNWfH97Mk7t00ne4REuqaaMuD3ZTYObUua2nYVPeP5bwySoIMuLIAzBz1o10ReFbMo2XUM2n%2FUqNoPdlycqiTr9EaHKpWEQUIGhaMCbfykKakjYMy1iES9QNVfpWb0PqE7%2FxjJ%2BC8KdHbVUMOy3%2F9IGOqUBwTbF5J4uQVBLbZ9CHRYqiE3MSGi2yrDfZPbkxV10Fa4g5J5fHEJezp0HR5FeZ4yJNQY32nSkkkmJFtZJsH8TpLzjOO%2FOHdW13vuDO51VeZDIkMLoqJD9lQWKJUsT1HW0fHWnV3eTUqMqb22Dhnc0pMp1Va5LxhtEGFUFBy54vJrBi9M7e1oI9XIyZ49GrjhglwVD%2BO6bhA%2BVLjaUHzZYCi%2BW%2FeQQ&X-Amz-Signature=0479db069ce5944b4955b4ae75fe88789347e8d68750c71a145ff58daed27585&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

[image](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/e426d7f9-3588-412d-8c33-d1f75182aa5d/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TKW2PBGE%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T225736Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDUbjyjq8tLBPFl%2FjF1mjlG3RUrIke%2Fc%2BjsqOyuWeE5vAIgA7qRxvffBdHPynoVdVck%2FRJJbrJTz3OdHdRBF4iZJLwqiAQIxv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDGur5Xdg4j5YtKbFpircA8vmrfjFdTQjlkSI2ZB3snj%2FQnoFPIyx2jNppmBG%2BRNbExCL8K4S8g5PSsO1W98Yp35NSo8vF30ep36%2FB0Ps%2B4nwNyHZ5mjhWLitIilb%2FLO4o4ksfhk3Qd%2BHJcg1tjiiOD9BZGo1sjFmKX1yZsj7OBgzloW0Ke3rA3IaL%2BKCSys%2BBFRHkWVxNAuZ1GNxIg%2BSUWFmSZ1EUh42IusJCCSZ36Hk40lq14M%2FfiEoeEE4%2BlBKfaA8Xjrp7SxNAxNh5eR8QhrkBiTsq0sNn%2BE9TA7B4z2fJDKb7gibv9gswTKw4DhIlOYAme1MY6TTghELKICe2JbePV1ICBj91oG8wJot5Gnc5fb5pKPUmN1r8JDd%2FB7h9SXmJB2cK2Nx49SAZ2HRaR39MQvf7s0iZLjIkZRjWFIizmy8AdNKkWx78lv0FaVjEBfyTPT%2BpqTu1qzHeuf7E8A8Cv%2Bdy0FIsRL7BG0hSgWZ7QFFeOllpmU2xpfCe4j4AeNWfH97Mk7t00ne4REuqaaMuD3ZTYObUua2nYVPeP5bwySoIMuLIAzBz1o10ReFbMo2XUM2n%2FUqNoPdlycqiTr9EaHKpWEQUIGhaMCbfykKakjYMy1iES9QNVfpWb0PqE7%2FxjJ%2BC8KdHbVUMOy3%2F9IGOqUBwTbF5J4uQVBLbZ9CHRYqiE3MSGi2yrDfZPbkxV10Fa4g5J5fHEJezp0HR5FeZ4yJNQY32nSkkkmJFtZJsH8TpLzjOO%2FOHdW13vuDO51VeZDIkMLoqJD9lQWKJUsT1HW0fHWnV3eTUqMqb22Dhnc0pMp1Va5LxhtEGFUFBy54vJrBi9M7e1oI9XIyZ49GrjhglwVD%2BO6bhA%2BVLjaUHzZYCi%2BW%2FeQQ&X-Amz-Signature=bf7f865ce1ce5b4c8185f71553950afc85a42005243937195318febe054a10f5&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

hello 慕课网的位同学们，大家好，这一节当中，我来给大家创造一个买的机会。不过呢不是让大家去当剁手作案，而是让大家实现一个买的场景。就是说使用 after 这个断言来实现一个简易的秒杀场景，我们先来看看它都要做哪些内容。第一点，我们要创建一个模拟下单的接口，这个接口非常简单，并不会包含太多的业务逻辑，只是为了配合我们的 after 断言实现这样一个场景。接下来第二步，咱就利用 after 断言的特性在网关层设置一个生效时间。所以这里大家看出来了，这个简易秒杀场景是在网关层实现秒杀时间判断的，所以咱说它是一个简易的秒杀场景。因为在真正的电商系统的业务中，秒杀场景在下单时间的判断上，可不仅仅依靠网关层，它在后台业务中都有大量的配置以及校验检查。所以咱这次的小 demo 只是让大家明白 after 断言的应用场景。那么大家在自己以后的工作中，**如果需要在网关层对某些时间敏感的业务场景做限制的话，那么就可以使用 after 断言**。其实这个时间断言也有三兄弟的， after 只是其中的一个。那么剩下两个咱就到 demo 的场景里面再跟大家介绍。 OK 同学们抄起家伙，印太 dj 走起编程，使我快乐 996 是我的福报。

[image](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/086ba87c-91ba-44f5-82f6-40f979d4656a/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TKW2PBGE%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T225736Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDUbjyjq8tLBPFl%2FjF1mjlG3RUrIke%2Fc%2BjsqOyuWeE5vAIgA7qRxvffBdHPynoVdVck%2FRJJbrJTz3OdHdRBF4iZJLwqiAQIxv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDGur5Xdg4j5YtKbFpircA8vmrfjFdTQjlkSI2ZB3snj%2FQnoFPIyx2jNppmBG%2BRNbExCL8K4S8g5PSsO1W98Yp35NSo8vF30ep36%2FB0Ps%2B4nwNyHZ5mjhWLitIilb%2FLO4o4ksfhk3Qd%2BHJcg1tjiiOD9BZGo1sjFmKX1yZsj7OBgzloW0Ke3rA3IaL%2BKCSys%2BBFRHkWVxNAuZ1GNxIg%2BSUWFmSZ1EUh42IusJCCSZ36Hk40lq14M%2FfiEoeEE4%2BlBKfaA8Xjrp7SxNAxNh5eR8QhrkBiTsq0sNn%2BE9TA7B4z2fJDKb7gibv9gswTKw4DhIlOYAme1MY6TTghELKICe2JbePV1ICBj91oG8wJot5Gnc5fb5pKPUmN1r8JDd%2FB7h9SXmJB2cK2Nx49SAZ2HRaR39MQvf7s0iZLjIkZRjWFIizmy8AdNKkWx78lv0FaVjEBfyTPT%2BpqTu1qzHeuf7E8A8Cv%2Bdy0FIsRL7BG0hSgWZ7QFFeOllpmU2xpfCe4j4AeNWfH97Mk7t00ne4REuqaaMuD3ZTYObUua2nYVPeP5bwySoIMuLIAzBz1o10ReFbMo2XUM2n%2FUqNoPdlycqiTr9EaHKpWEQUIGhaMCbfykKakjYMy1iES9QNVfpWb0PqE7%2FxjJ%2BC8KdHbVUMOy3%2F9IGOqUBwTbF5J4uQVBLbZ9CHRYqiE3MSGi2yrDfZPbkxV10Fa4g5J5fHEJezp0HR5FeZ4yJNQY32nSkkkmJFtZJsH8TpLzjOO%2FOHdW13vuDO51VeZDIkMLoqJD9lQWKJUsT1HW0fHWnV3eTUqMqb22Dhnc0pMp1Va5LxhtEGFUFBy54vJrBi9M7e1oI9XIyZ49GrjhglwVD%2BO6bhA%2BVLjaUHzZYCi%2BW%2FeQQ&X-Amz-Signature=c6285f3951b7bb74e3da919bdcfb63924f79671cb7c3197cce5dfce388b4cb61&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

前面咱说到要实现一个买买的场景。那咱先抛掉断言不谈，先把这个买给它实现了。咱们的 gateway 实际上是调用的分 client 的方法，那咱就在

feign client 里面实现一个简易的或者咱可以说简陋的秒杀业务。我这里首先给它创建一个新的 controller 咱来一个快速极速落地。 controller 的名称叫 gateway controllerok 回车。第一步先一顶大大的绿帽子戴上去，给他一个 annotation 叫 rest 看出了好像一顶绿帽子还不够，我这边还要再给他加一个 sl four G 打印 log 用的两点好像还是不够嘛，我这里还要给它加一个 request mapping 它 request mapping 里面指定了 gateway 也就是说你的访问请求要先带上 gateway 才能到这里，这样的话便于区分它已经存在的这个 ctrl 了。


OK 那我们开始写代码了，咱虽然是个简易而又简陋的秒杀场景，但是麻雀虽小，五脏要俱全。我们这里稍微的对这个多线程加一点小小的控制。咱的货物存储结构，我们就直接用一个当前的 map 来。好了，那这里声明了一个 map 它的 key 是个 long 型，代表着商品 ID 那么它的货物类型应该是一个 product 这个类咱还没有定义这个 product 要在哪定义，同学们当然是到我们的接口层了，因为咱们的费用方法是用了一种接口抽出的层次结构，我们当然要在接口层定义 product 的对象了。抽出接口层是一种非常好的习惯，像以前阿里里面他们会用 hsf 也是一种 RPC 框架，那我们通常就是暴露一个接口层给对方调用。那么在接口层里面，把所有的 entity 也就是业务对象全部抽取出来。


当然这些业务对象并不是那种充血模型的对象，它不会包含任何的业务方法，只是一个 pojo pure Java objectok 那我们 product 里面就声明简单的三个属性，一个是 product ID 另外一个是它的 description 我们把它声明成一个 string 这个商品叫什么？怎么来吸引顾客来买你的东西要吹得天花乱坠，剩下的一个属性。那在电商场景里面也很重要了，叫 stock 咱都简单起见，就定义成个浪形就可以了。忘了问大家了， stock 是什么含义？大伙都知道吧。也就是当前的库存了，你库存为0，那就不能卖了。咱的 product 的定义好之后，这里接着返回来写这个买买买的接口。下面定义它的这个存储商品的结构叫 itemsitems 直接 new 一个 concurrent hash map 就可以了。


其实咱这里也可以用什么呢？如果你引用了像阿帕奇的 collection 组件或者是 Google 的组件，那大家可以用很方便的形式，比如 maps 点你用 concurrent hashmap 这种形式来声明，咱这里没有引用，就给它声明一个 concurrent hashmap 就可以了。然后这里先来定义一个查询的接口，这个查询就是获得商品信息的一个接口。那它要是一个 get 形式的，然后传入的那应该是一个浪形的 product ID 也就是商品 ID 咱给它就叫 PID 好嘞，简洁明了，看着舒服。


好，我们给它起一个 request paramrequest param 因为它是 get 形式的方法。那咱这个参数就自然而然地添加到了访问路径的末尾。那它这里返回的类型应该是个 response bodyresponse body 打上去 request 也给它指定好 request mappingrequest mapping 这里指定两个属性，一个是它的访问路径，我们把它叫做什么叫 details 好了，其实有些同学们在 rest 接口里喜欢叫 get details 如果按照严格的 rest 接口定义规范，他是不建议把动词加进去了，动词把它放在 HTTP method 这里。 get post put delete ，把这个语境的意思下放到 HTTP method 那在 URL 里面尽量是以名词来定义。


好了，那这里定义了它的 URL mapping 以后，我们给它的 method 指定成 get 形式。那接下来这个查询接口的请求，我们把它一切从简。怎么从简呢？嘿嘿不怕大家笑话，这个从简简的是非常厉害。我们先来判断，如果 items 包含了这个 PID 那这里就会直接返回 PID 但是当你不包含的时候，我们来做一个手脚。我声明一个 product 好不好，我怎么声明呢？我这里构造一个新的 product 我们顺带在 product 里面再给它加一个构造器模式，这样说明起来会比较方便。
好，那我这里调用 product 的 builder 然后怎么创建？咱先给他创建一个 product ID 就是说如果你的商品集合里面不存在这个 product 那我就偷偷的给你塞一个好了，这样咱就少写了一个商品发布的接口。那它的 description 我们怎么添加呢？就叫好吃不贵。好了好吃不贵，最后它的库存这个好吃不贵的东西，可以卖多少个 100 个不多不少。定义完这些以后，直接把这个对象给 build 出来，把它塞到 items 里面。但是能直接塞吗？千万不要直接破头，因为咱没有同步的控制，所以这里要用 put if absent 也就是说当你不存在的时候才 put 至于为什么这样做，同学们应该很容易就能猜到有可能两个方法同时执行到了这


里。那大家往里面先后 put 这里会产生一些线程不安全的操作。尽管这个 map 是线程安全的，但是在业务层次上这可不是线程安全。所以咱要在这里避免一下，添加完货物之后，我们就可以直接 return 了 return 谁 return 他的 get PID 那这个商品查询接口身兼两职，一个是返回商品的信息，另一个在背后偷偷搞了些鬼，发布了一个商品，商品已经发布了，那我们接下来就要去正儿八经的买了，我们给这个买买买接口定义一个简单的返回格式，就叫 string 好了，来告诉你有没有买成功，它同样的接收一个 PID 我们把这一段 copy 下来。


Product id. 那他每次买几个，我们就把他想象成这是一个非常非常抢手的货，1元卖苹果手机，你每个用户他只能买一个。那这个 request 我把上面的给它 copy 下来，request的 value 我们把它改成 place order 这是下单的意思。 HTTP method 咱就要改成 post 了。按照 rest 的规范，这是一个 post 的接口，现在开始剁手了，怎么来买呢？在买之前咱得看这个商品存不存在，我们从上面的 items 里面把商品先给它拿出来。拿出来以后这里做一个简单的判断。如果商品等于空，那我直接 return 一个什么东西叫 product not foundproduct not found 商品不存在。


那假设商品不为空，那我要检查一下库存，你的 1 元 iPhone 手机有没有被人抢光？他 get stock 如果你的 stock 小于等于零了，那么证明你没货了，那我这里给他 return 一个 sold out 好，清仓了，没货了，这里还缺了一个 if 好，那这两个声明完了以后，方法逻辑走到这里，就是证明你一定有货了。
酒香不怕轿子深，咱有货就要卖。卖货之前，咱要先把这个货给它锁定起来，然后在里面再判断一下你当前是不是有货。为什么？同学们这个还用我说吗？大家应该都非常明白了，如果你没有货，那我 return 一个 sold out 也就是说假设有两行代码同时执行到了这里。那他接下来在执行 SQL nice 的时候，这两个代码如果不加 if 判断，那可能都会处于有货状态。

[image](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/8a5f2d5e-08a4-4b01-93bb-6fbbdef959e8/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TKW2PBGE%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T225736Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDUbjyjq8tLBPFl%2FjF1mjlG3RUrIke%2Fc%2BjsqOyuWeE5vAIgA7qRxvffBdHPynoVdVck%2FRJJbrJTz3OdHdRBF4iZJLwqiAQIxv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDGur5Xdg4j5YtKbFpircA8vmrfjFdTQjlkSI2ZB3snj%2FQnoFPIyx2jNppmBG%2BRNbExCL8K4S8g5PSsO1W98Yp35NSo8vF30ep36%2FB0Ps%2B4nwNyHZ5mjhWLitIilb%2FLO4o4ksfhk3Qd%2BHJcg1tjiiOD9BZGo1sjFmKX1yZsj7OBgzloW0Ke3rA3IaL%2BKCSys%2BBFRHkWVxNAuZ1GNxIg%2BSUWFmSZ1EUh42IusJCCSZ36Hk40lq14M%2FfiEoeEE4%2BlBKfaA8Xjrp7SxNAxNh5eR8QhrkBiTsq0sNn%2BE9TA7B4z2fJDKb7gibv9gswTKw4DhIlOYAme1MY6TTghELKICe2JbePV1ICBj91oG8wJot5Gnc5fb5pKPUmN1r8JDd%2FB7h9SXmJB2cK2Nx49SAZ2HRaR39MQvf7s0iZLjIkZRjWFIizmy8AdNKkWx78lv0FaVjEBfyTPT%2BpqTu1qzHeuf7E8A8Cv%2Bdy0FIsRL7BG0hSgWZ7QFFeOllpmU2xpfCe4j4AeNWfH97Mk7t00ne4REuqaaMuD3ZTYObUua2nYVPeP5bwySoIMuLIAzBz1o10ReFbMo2XUM2n%2FUqNoPdlycqiTr9EaHKpWEQUIGhaMCbfykKakjYMy1iES9QNVfpWb0PqE7%2FxjJ%2BC8KdHbVUMOy3%2F9IGOqUBwTbF5J4uQVBLbZ9CHRYqiE3MSGi2yrDfZPbkxV10Fa4g5J5fHEJezp0HR5FeZ4yJNQY32nSkkkmJFtZJsH8TpLzjOO%2FOHdW13vuDO51VeZDIkMLoqJD9lQWKJUsT1HW0fHWnV3eTUqMqb22Dhnc0pMp1Va5LxhtEGFUFBy54vJrBi9M7e1oI9XIyZ49GrjhglwVD%2BO6bhA%2BVLjaUHzZYCi%2BW%2FeQQ&X-Amz-Signature=272154a11b6900b108c2d9769ccfb2ab3f3a15efaef3d99736a6ebbe33d069a5&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

```java
package com.imooc.springcloud;

import lombok.extern.slf4j.Slf4j;
import org.springframework.web.bind.annotation.*;

import java.util.Map;
import java.util.concurrent.ConcurrentHashMap;

/**
 * <h1></h1>
 */
@RestController
@Slf4j
@RequestMapping("gateway")
public class GatewayController {

    public static final Map<Long, Product> items = new ConcurrentHashMap<>();

    @RequestMapping(value = "details", method = RequestMethod.GET)
    @ResponseBody
    public Product get(@RequestParam("pid") Long pid) {
        if (items.containsKey(pid)) {
            Product prod = Product.builder()
                    .productId(pid)
                    .description("好吃不贵")
                    .stock(100L)
                    .build();
            items.putIfAbsent(pid, prod);
        }
        return items.get(pid);
    }

    @RequestMapping(value = "placeOrder", method = RequestMethod.POST)
    public String buy(@RequestParam("pid") Long pid) {
        Product prod = items.get(pid);
        if (prod == null) {
            return "Product not Found";
        } else if (prod.getStock() < 0L) {
            return "Sold out";
        }

        synchronized (prod) {
            if (prod.getStock() < 0L) {
                return "Sold out";
            }
            return "Order Placed";
        }
    }
}
```

这样的话我们在电商场景中叫做超卖，你的库存可能会减为负 1 所以这里才需要对它做一个额外检查，把它放在同步代码块里。额外检查完以后，咱就可以正儿八经放心的去给它减库存了。朋友们知道，在电商里面这个减库存操作可远远没有这么简单都非常非常复杂的。尤其是在那种全民秒杀的场景，比如 12306 抢票包括淘宝的秒杀。实际上 12306 里面的秒杀的业务复杂度可真的比淘宝里面的秒杀场景要难得多喽。大家不要小看 12306 还是真的很有技术含量的。
那你库存减完了，一走到这里，那它应该是成功的 check out 了，我们这里打一个 log 叫 order placed 那我们的业务方法处理完了，接下来咱就要到 gateway 里进行主线任务了，也就是通过 after 断言来实现这个秒杀场景。括弧简易的打开小桌板，我们转战到 gateway 项目。好，我们这里打开前面做好的 gateway configuration 我们这次在 Java 代码里面添加一个路由。


好，前面说过，这个 roots 节点下咱可以添加多个路由，这里已经有一个存在的元素了，我们紧接着它可以秒杀场景，做一个新的路由配置。那同样的也是使用 root 开头。好， root 完了以后。那第一个我们要给它设置一个 pass 断言，既然这个秒杀场景，那它的 pass 就叫 SEC Q 秒杀的意思， SEC 就是 seconds 的意思，后面也添加一个通配符。就是说如果你满足了这个 pass 断言以后，接下来它会返回到哪里？给它配置一个 URI 同样的也返回到上面指定。好的这个分 client 方法，咱把它 copy 一下拿下来。这里故事还没有结束，添加了 pass 还不够，我们的 filter 这里把它给 copy 下来，咱要把前面的这串 SEC Q 给去掉的。所以咱这里要务必添加一个 filter strip prefix 把这一段第一个 pass 中的节点给它删除掉。
接下来就到了配置 after 断言的时候了，养兵千日，用兵一时，咱前面做了这么多的铺垫，这里终于要派上大用场了。好，我这里给他再添加一个断言，大家看他叫 after 他的意思是什么呢？他的意思是告诉 gateway 当前的这个路由规则，只在某个时间点以后生效。


这个时间点怎么定义呢？我们在 after 里面使用这个类 zoned zone the date time 这个类它相当好用，同学们可能平时只会用 date date time 还有像 calendar 之类的类，它可是 Java 原装出品的一个 zone 的 day time 也蛮好用的。咱这里调用 zone day time 的 now 也就是当前的这个时间点，但是只在当前时间点生效。那这不是废话吗？你这个服务一启动的时候，当前时间点就已经生成了，那这个路由规则也就生效了。别急，我们这后面还有给它加一个 plus minutes 这个意思是什么呢？他是说当你的服务启动加载完成以后，往后推迟一分钟生效。那这样咱是不是就构建了一个一分钟后才生效的秒杀场景？非常简单。


那除了after ，咱还可以连带着附送你几个断言，这个大家就看作是赠品了。

```java
@Configuration
public class GatewayConfiguration {

    @Bean
    @Order // 加载顺序
    public RouteLocator customiaedRoutes(RouteLocatorBuilder builder) {
        return builder.routes()
                .route(r -> r.path("/java/**")
                        .and().method(HttpMethod.GET)
                        .and().header("name")

                        .filters( f -> f.stripPrefix(1)
                                .addRequestHeader("java-param", "gateway-config")
//                                .
                        )

                        .uri("lb://FEIGN-CLIENT")
                )

                .route(r -> r.path("seckill/**")
                        .and().after(ZonedDateTime.now().plusMinutes(1))
//                        .and().before()
//                        .and().between()

                        .filters(f -> f.stripPrefix(1))
                        .uri("lb://FEIGN-CLIENT")
                )
                .build();
    }

}
```

[image](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/e59b6fdb-b0c6-4bd1-a234-da2b71228435/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TKW2PBGE%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T225736Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDUbjyjq8tLBPFl%2FjF1mjlG3RUrIke%2Fc%2BjsqOyuWeE5vAIgA7qRxvffBdHPynoVdVck%2FRJJbrJTz3OdHdRBF4iZJLwqiAQIxv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDGur5Xdg4j5YtKbFpircA8vmrfjFdTQjlkSI2ZB3snj%2FQnoFPIyx2jNppmBG%2BRNbExCL8K4S8g5PSsO1W98Yp35NSo8vF30ep36%2FB0Ps%2B4nwNyHZ5mjhWLitIilb%2FLO4o4ksfhk3Qd%2BHJcg1tjiiOD9BZGo1sjFmKX1yZsj7OBgzloW0Ke3rA3IaL%2BKCSys%2BBFRHkWVxNAuZ1GNxIg%2BSUWFmSZ1EUh42IusJCCSZ36Hk40lq14M%2FfiEoeEE4%2BlBKfaA8Xjrp7SxNAxNh5eR8QhrkBiTsq0sNn%2BE9TA7B4z2fJDKb7gibv9gswTKw4DhIlOYAme1MY6TTghELKICe2JbePV1ICBj91oG8wJot5Gnc5fb5pKPUmN1r8JDd%2FB7h9SXmJB2cK2Nx49SAZ2HRaR39MQvf7s0iZLjIkZRjWFIizmy8AdNKkWx78lv0FaVjEBfyTPT%2BpqTu1qzHeuf7E8A8Cv%2Bdy0FIsRL7BG0hSgWZ7QFFeOllpmU2xpfCe4j4AeNWfH97Mk7t00ne4REuqaaMuD3ZTYObUua2nYVPeP5bwySoIMuLIAzBz1o10ReFbMo2XUM2n%2FUqNoPdlycqiTr9EaHKpWEQUIGhaMCbfykKakjYMy1iES9QNVfpWb0PqE7%2FxjJ%2BC8KdHbVUMOy3%2F9IGOqUBwTbF5J4uQVBLbZ9CHRYqiE3MSGi2yrDfZPbkxV10Fa4g5J5fHEJezp0HR5FeZ4yJNQY32nSkkkmJFtZJsH8TpLzjOO%2FOHdW13vuDO51VeZDIkMLoqJD9lQWKJUsT1HW0fHWnV3eTUqMqb22Dhnc0pMp1Va5LxhtEGFUFBy54vJrBi9M7e1oI9XIyZ49GrjhglwVD%2BO6bhA%2BVLjaUHzZYCi%2BW%2FeQQ&X-Amz-Signature=bd7b7ab044251c2dcba1f83fcb384101b33af729b90b97a7e3b02c70bc90b65b&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

比如说它除了 after 当然还有 before 它跟 after 的功能截然相反，after是在某个时间点以后，路由规则才生效。那么 before 是说在某个时间点以前，路由规则才会生效，过了这个时间点过期不后。那除了 before 实际上咱还有接着往下看咱还有一个 between 你看它关于时间的断言做得非常非常的精致。这个 between 断言里面是有两个 daytime 的，也就是说这个路由规则会在这两个 daytime 之间的时间段来生效。好这个学起来都非常容易。


同学们举一反三，一看就知道了。我们把这个保存一下启动项目来验证一下。在启动项目之前，我们先要把 eureka server 给它启动起来。然后我们连带着把 thin client application 同事也给启动起来。这两个应用都启动起来以后，我们可以把 gateway application 最后给它启动起来，看到 spring 成功一半。


好嘞，接下来咱到 postman 里尝试着调用一番，咱先来尝试直接调用份方法，这里传入它的 controller 叫 gateway 然后调用它的 details 方法，先获取一个，咱的商品 ID 传入叫10086。好了，点击 send 这里已经出现了一个好吃不贵的商品，它的库存数量是 100 个。那紧接着咱把它给下个单买它几件转移到 place order 方法，这也是咱创建好的发送，把他的 PID product ID 改成 10086 走一个。你看这里显示，订单下单成功，再走一个又成功了。
好，那我们刚才下了 3 次单，回到商品详情页看一看，他现在的库存数量已经变成 97 了，那咱这是直接调用的分 client 接下来我们要通过 gateway 里这里来调用一番了。在这里直接把 local host 从 40,006 改成65,000。然后把这个 gateway 前面加一段叫 `seckill` 那这就是咱的路由规则，我们直接点击散达，看它能不能返回，结果看也是返回了，说明路由规则生效了。那下单下单是不是也可以呢？好在前面再加三个 Q 走，你也是下单成功了。 OK 那咱这里看的是它路由生效的规则。我们来看一下如果你的时间不满足这个 after 断音，那么会出现什么样的错误场景好，我们刚才把 gateway application 给它关掉，然后重新启动一下。


接下来大家有一分钟的时间来进行这个测试。走快马加鞭跑到 postman 里，咱调用一下 details 方法。朋友们看这里的报错非常的简单粗暴，直接给你回一个404。所以这里大家可以看出，如果你的 root 匹配没有匹配上，那么他可是 6 亲不认的，他直接告诉你 not found 好，那我们稍等片刻，等待路由规则生效。一炷香的时间已经过去了，我们再点击一下，好，顺利获得了结果。那说明咱的 after 断言已经完美生效了。同学们在这个 gateway 的断言库中能找到很多非常丰富的断言，可以助力你的各种业务场景。比如咱刚才设置的剪映秒杀是一个场景，也可以设置什么比如说定点抢红包，午夜的 12 点，到了某个时间点以后，咱在后台的抢红包接口就可以开放到路由规则中供他人访问。除了这些场景以外，所有的跟时间敏感的场景，但凡你只要遇到这种场景，它需要在某个时间点以后做那么些不同的事儿，那大家可以在心里考虑一下。


after 但是我这里要跟大家提醒一个点，就是从我们架构的角度来说，咱现在做的是什么？是网关层，尽量要保证它的纯洁性，怎么让它纯洁莫装纯咱是真的纯怎么个意思呢？就是说把业务的代码咱尽量不要放到网关层来实现。这里把网关层保持一个纯粹的路由转发，或者说给它加一些限流也是可以的。对于一些业务代码，尽量不要放在网关侧，把这些业务代码下沉到各自的业务流程里面来控制。那本小节到这里就要告一段落了，我来跟大家总结一下。在这一节当中，我们利用 after 断言构造了一个非常简单的简易秒杀场景。那么这里旨在让大家认识断言的丰富特性。除此之外，咱还附送了两个断言当做赠品，买一送二，一个是 before 一个是 between 其实 gateway 组件是我接触过的所有网关层组件里面最亲民最接地气的一种对从事 Java 的技术人员，他的编程体验非常非常的友好。而且 gateway 的强大功能可不远远仅限于断言。


那么在下一小节我要带大家一起看一下过滤器的生命周期以及它的工作原理。然后带大家实现一个自定义的过滤器实现接口的计时功能。 OK 同学们，那我们下一期再见。




