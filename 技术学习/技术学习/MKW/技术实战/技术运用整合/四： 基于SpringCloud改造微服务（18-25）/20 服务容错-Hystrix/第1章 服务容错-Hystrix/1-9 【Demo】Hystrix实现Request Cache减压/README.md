---
title: 1-9 【Demo】Hystrix实现Request Cache减压
---

# 1-9 【Demo】Hystrix实现Request Cache减压

[image](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/26d70218-7224-4dd7-b0a0-de4772f6d6ef/SCR-20240719-bmxc.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SFPKTHSP%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T225638Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCNHQJOCLSKJikXprN%2FLOqOtGxg2EeuE%2F2AuyE8QrFUfAIhAK9y6eOwOvdog8W7maXGY66dcgjE4wxopYMTm2Mg%2BqOmKogECMb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgyzWu3q0RBl2d%2FV3QQq3AN28jsNIs9d1b3tDtGMcRzSE3s7oKFAIp4jYWNXtqz8cdlOwT1bvEVedbXxfBj4Gcj0BKj5HWmRHlMUAfugJ%2FV2ElkZfhxph3ifl%2F6OUhhNzq%2B9hzuahxQUxOLLDyZX75FJr1f5wzUCTde05wmBSPbwlIzYqvz4jE9GsWWW1n3ay1%2B6nCSo%2BhxJ2EFywaSAAkVUjvPORUnsEy1b5yjPlIIWKzi1dtBqygjO7KVZ8%2F77pp4rPf%2BNnEti5ydSZO4dRS3w4OBwhH%2FNIhBuOhvbupWPiDLwq35fkBG2cPIZapLcf6xYo8yZKxHpuuz2wqdo4AKKzfiWYcX51rXDQ0IXsHWOxBF8Ym%2F66SzDOzlBj6S3aV1dd4PKJxy9xqXaFb4%2Ff%2FHdO584gtCKaUI0Uzib0IBkIzZo2iYBd5k5NPKjT2Sbodz5%2FsmwRYXd3g0aZUto6yNK4T9qu94NrvrobYaev2DI6gCFkMQbzFD9UwXbmMMMF6C84CbvlYlwTxjlBskBJzBtxrEX9Z1PZP8lBCzUpCsHSaD1j9B4bOiRPvHryU0YU%2FWI3iWkKDMajPvjPXlQQva9OZQLRgBDsjuBvzNqy%2FQc6oVV%2B8kKVzihaFSSD0WZk10KH9gsOhz41ADbnjChuv%2FSBjqkAVyiL0U2eHeUI0GS51sIiUYNq50qw1SPECuQHoTkTjh5t4DmrCfZZqfXBB1TJtKDJPgZL%2B%2BaBMSJJsPEWnVzYCs5l2jjn%2BOM2D3%2BT9UIAvrRfrvjhbLv8pEWvkrOFlCtTthsn%2B5Cl9jEI4eYAVyml94q1T8yhfAZVMt3kvHzuG%2BPukEbb6gkOIkMu5KeScNXdGkIWeN0%2BKmRbMIM%2FXsjGDs808Zu&X-Amz-Signature=b8536b6f604d842908631eff205c0ebc188ffcd07c664efb48a9f8bcd164a5da&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

[image](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/24bb3d21-dcc9-4d25-997e-fe86c8172208/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SFPKTHSP%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T225638Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCNHQJOCLSKJikXprN%2FLOqOtGxg2EeuE%2F2AuyE8QrFUfAIhAK9y6eOwOvdog8W7maXGY66dcgjE4wxopYMTm2Mg%2BqOmKogECMb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgyzWu3q0RBl2d%2FV3QQq3AN28jsNIs9d1b3tDtGMcRzSE3s7oKFAIp4jYWNXtqz8cdlOwT1bvEVedbXxfBj4Gcj0BKj5HWmRHlMUAfugJ%2FV2ElkZfhxph3ifl%2F6OUhhNzq%2B9hzuahxQUxOLLDyZX75FJr1f5wzUCTde05wmBSPbwlIzYqvz4jE9GsWWW1n3ay1%2B6nCSo%2BhxJ2EFywaSAAkVUjvPORUnsEy1b5yjPlIIWKzi1dtBqygjO7KVZ8%2F77pp4rPf%2BNnEti5ydSZO4dRS3w4OBwhH%2FNIhBuOhvbupWPiDLwq35fkBG2cPIZapLcf6xYo8yZKxHpuuz2wqdo4AKKzfiWYcX51rXDQ0IXsHWOxBF8Ym%2F66SzDOzlBj6S3aV1dd4PKJxy9xqXaFb4%2Ff%2FHdO584gtCKaUI0Uzib0IBkIzZo2iYBd5k5NPKjT2Sbodz5%2FsmwRYXd3g0aZUto6yNK4T9qu94NrvrobYaev2DI6gCFkMQbzFD9UwXbmMMMF6C84CbvlYlwTxjlBskBJzBtxrEX9Z1PZP8lBCzUpCsHSaD1j9B4bOiRPvHryU0YU%2FWI3iWkKDMajPvjPXlQQva9OZQLRgBDsjuBvzNqy%2FQc6oVV%2B8kKVzihaFSSD0WZk10KH9gsOhz41ADbnjChuv%2FSBjqkAVyiL0U2eHeUI0GS51sIiUYNq50qw1SPECuQHoTkTjh5t4DmrCfZZqfXBB1TJtKDJPgZL%2B%2BaBMSJJsPEWnVzYCs5l2jjn%2BOM2D3%2BT9UIAvrRfrvjhbLv8pEWvkrOFlCtTthsn%2B5Cl9jEI4eYAVyml94q1T8yhfAZVMt3kvHzuG%2BPukEbb6gkOIkMu5KeScNXdGkIWeN0%2BKmRbMIM%2FXsjGDs808Zu&X-Amz-Signature=7df218c15b3ecda18add639db4a8fac45f8e72b452e64c0f9961a105e10f4dbc&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

[image](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/f3b13cbc-b383-46fa-8daa-382742f4e19d/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SFPKTHSP%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T225638Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCNHQJOCLSKJikXprN%2FLOqOtGxg2EeuE%2F2AuyE8QrFUfAIhAK9y6eOwOvdog8W7maXGY66dcgjE4wxopYMTm2Mg%2BqOmKogECMb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgyzWu3q0RBl2d%2FV3QQq3AN28jsNIs9d1b3tDtGMcRzSE3s7oKFAIp4jYWNXtqz8cdlOwT1bvEVedbXxfBj4Gcj0BKj5HWmRHlMUAfugJ%2FV2ElkZfhxph3ifl%2F6OUhhNzq%2B9hzuahxQUxOLLDyZX75FJr1f5wzUCTde05wmBSPbwlIzYqvz4jE9GsWWW1n3ay1%2B6nCSo%2BhxJ2EFywaSAAkVUjvPORUnsEy1b5yjPlIIWKzi1dtBqygjO7KVZ8%2F77pp4rPf%2BNnEti5ydSZO4dRS3w4OBwhH%2FNIhBuOhvbupWPiDLwq35fkBG2cPIZapLcf6xYo8yZKxHpuuz2wqdo4AKKzfiWYcX51rXDQ0IXsHWOxBF8Ym%2F66SzDOzlBj6S3aV1dd4PKJxy9xqXaFb4%2Ff%2FHdO584gtCKaUI0Uzib0IBkIzZo2iYBd5k5NPKjT2Sbodz5%2FsmwRYXd3g0aZUto6yNK4T9qu94NrvrobYaev2DI6gCFkMQbzFD9UwXbmMMMF6C84CbvlYlwTxjlBskBJzBtxrEX9Z1PZP8lBCzUpCsHSaD1j9B4bOiRPvHryU0YU%2FWI3iWkKDMajPvjPXlQQva9OZQLRgBDsjuBvzNqy%2FQc6oVV%2B8kKVzihaFSSD0WZk10KH9gsOhz41ADbnjChuv%2FSBjqkAVyiL0U2eHeUI0GS51sIiUYNq50qw1SPECuQHoTkTjh5t4DmrCfZZqfXBB1TJtKDJPgZL%2B%2BaBMSJJsPEWnVzYCs5l2jjn%2BOM2D3%2BT9UIAvrRfrvjhbLv8pEWvkrOFlCtTthsn%2B5Cl9jEI4eYAVyml94q1T8yhfAZVMt3kvHzuG%2BPukEbb6gkOIkMu5KeScNXdGkIWeN0%2BKmRbMIM%2FXsjGDs808Zu&X-Amz-Signature=a845d303ad212cd328646da2317f51883d0260aaa4188e6628a090eec7b0ef4a&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

慕课网的各位同学们，大家好，这一节我将介绍一个 high streaks 的特有功能，你在其他框架中有可能看不到它叫什么？ Request catch. OK 这一章我们的主要内容有第一部分，关于这一点，我想先理清一个问题，就是说 request catch 它是一种降级手段吗？

[image](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/8f8c1a1a-bc31-4e46-91d0-731180429b81/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SFPKTHSP%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T225638Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCNHQJOCLSKJikXprN%2FLOqOtGxg2EeuE%2F2AuyE8QrFUfAIhAK9y6eOwOvdog8W7maXGY66dcgjE4wxopYMTm2Mg%2BqOmKogECMb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgyzWu3q0RBl2d%2FV3QQq3AN28jsNIs9d1b3tDtGMcRzSE3s7oKFAIp4jYWNXtqz8cdlOwT1bvEVedbXxfBj4Gcj0BKj5HWmRHlMUAfugJ%2FV2ElkZfhxph3ifl%2F6OUhhNzq%2B9hzuahxQUxOLLDyZX75FJr1f5wzUCTde05wmBSPbwlIzYqvz4jE9GsWWW1n3ay1%2B6nCSo%2BhxJ2EFywaSAAkVUjvPORUnsEy1b5yjPlIIWKzi1dtBqygjO7KVZ8%2F77pp4rPf%2BNnEti5ydSZO4dRS3w4OBwhH%2FNIhBuOhvbupWPiDLwq35fkBG2cPIZapLcf6xYo8yZKxHpuuz2wqdo4AKKzfiWYcX51rXDQ0IXsHWOxBF8Ym%2F66SzDOzlBj6S3aV1dd4PKJxy9xqXaFb4%2Ff%2FHdO584gtCKaUI0Uzib0IBkIzZo2iYBd5k5NPKjT2Sbodz5%2FsmwRYXd3g0aZUto6yNK4T9qu94NrvrobYaev2DI6gCFkMQbzFD9UwXbmMMMF6C84CbvlYlwTxjlBskBJzBtxrEX9Z1PZP8lBCzUpCsHSaD1j9B4bOiRPvHryU0YU%2FWI3iWkKDMajPvjPXlQQva9OZQLRgBDsjuBvzNqy%2FQc6oVV%2B8kKVzihaFSSD0WZk10KH9gsOhz41ADbnjChuv%2FSBjqkAVyiL0U2eHeUI0GS51sIiUYNq50qw1SPECuQHoTkTjh5t4DmrCfZZqfXBB1TJtKDJPgZL%2B%2BaBMSJJsPEWnVzYCs5l2jjn%2BOM2D3%2BT9UIAvrRfrvjhbLv8pEWvkrOFlCtTthsn%2B5Cl9jEI4eYAVyml94q1T8yhfAZVMt3kvHzuG%2BPukEbb6gkOIkMu5KeScNXdGkIWeN0%2BKmRbMIM%2FXsjGDs808Zu&X-Amz-Signature=e72a3627cd9de640623589dd61bd33514ec2d4766a316b3f83bf62331c7956bc&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

 no 其实未必。因为在 request cache 的过程中，它可能是什么错误都没有发生的。而 request 的 cache 相对于降级来说，它更像是一种减压手段。待会儿同学们到代码中看到了 request cache 的作用，就会明白这里面的门道了。


OK 第二点内容，我们要带大家使用 cage result 这个注解来缓存返回值。有些跟古奇加练武器材的同学可能这时候就顿悟了。 request cache 的缓存值应该保存在服务端还是客户端还是某个位置呢？相信同学们这时候已经有答案了最后一点带大家看一个异常的情况，那就是为何我的 request cache 配置好了，但是却不生效。那提纲中我们列出了好多问题，所以这一节大家就带着这些问题来深入到代码中寻找答案。


好，大家准备好的话，抄起家伙跟我到主场开工，每天扣丁 1 小时，健康工作 50 年。我们今天说干就干。 request cache 从字面意义上来说，大家应该很好理解它是什么，它叫访问缓存，对不对？那这个缓存在哪里？在我们的本地，我们这里默认把它放到本地缓存。那我们接下来怎么做呢？先创建一个 service 这个 service 我把它放在哪里，放在最外层， com.imoocspring cloud 里面创建一个 class 它就叫 request cage service 专门用来做这种测试。 OK service 创建好以后，我这里要给他注入一个对象叫什么？大家很熟悉了。 I service. 这个 I service 对象将在接下来的访问中用到。 OK 那我们这里再给 request cache service 创建一个函数，它的名称也就叫 request cache 那接下来变数就要开始喽，我先写方法体，把关子留到最后。


好了，这个 request cache 他做什么事情调用 service 调用 service 的哪一个方法呢？很简单，我们调用一个 say hi post 传入一个 friend 这个 friend 的对象我们这里要先给它定义一番喽。 OK 这个好基友，它叫什么名字，我们要给它传入一个名字对不对？那这个名字就从传入的 string name 开始，给它传入一个名字塞到 friend 的对象里。接下来我把这个对象传给 service 这就完事了吗？并没有，我想让这个对象最终返回出去。因为我 request cache 中这个 cache 返回的对象，我希望它是一个复杂类型。那这个 friend 那相对于 string 英特来说更符合我的要求。那么在接下来这一步，就把这个 friend 重新从 service 的 C high post 的方法中接过来 return 回去。这就完了吗？没有，做好事怎么能不留名，我们这里要打几行 log 什么地方打 log 入口打 log 出口打 log 入口这里就打一个 request cache 好了，然后我要把这个人名传入的这个 name 给他留下来。壮士请留步，敢问是从何方高人好名字留下来了，那返回之前也留个名，到此一游叫 after requesting cache 名字照样留下来。


好，这就完事了吗？没有，我们这里会多几个注解，是什么含义呢？这里看 cache 你看这里一打出 cache 有好多东西出来了，大家能猜到这个上面应该先写谁呢？先写 cache result 是什么含义就是说我要把这个 friend 给它当做 cache 的内容保存到我的本地 cache 当中。


但是问题又来了， friend 太多了，每个 friend 都有不同的名字。你怎么知道下一个请求来的这个 friend request 该从 cache 中取哪个对象呢？你说到点子上了这个问题 hystrix 已经给出了解决方案，大家看这里，我在这个属性列表中我还要加一个配置叫什么？ a cache key 这个很关键。它什么意思？它是说我把这个 service 的 string name 作为一个 cache key 假如我访问张3，你访问李4，那这个张 3 和李 4 所缓存的对象是不同的。如果你再次访问张 3 的时候，我会把你张 3 的 name 当做获取 cache 的 key 一个唯一的 keyok 看到这里是不是非常清晰明白了？别急，前面讲到我们还有两个彩蛋没讲对不对。


这里先跟大家贡献一个彩蛋叫什么？ hystrix comment 它是什么含义呢？这就要说到上一节中我们配置的 phone 上面的 fallback 方法了。这个份的 annotation 上面的 fallback 我们管它叫什么叫一篮子方案。这个 fallback 里面每一个函数都是一个降级流程。那么针对于你这个 myService 任何函数调用失败，他都会直接找到 fallback 里面的对应函数。所以我叫他一篮子计划。但是在现实情况下往往不可能给每一个方法都设置降级流程。


其实大部分方法并不需要降级。那怎么办呢？这里就是 hystrix common 就要解决的内容了。如果你只针对于一个服务要进行降级特定的服务降级，我们就可以直接在这个服务上面添加 hystrix comment 函数。那这里面还有很多内容，就是个很有料的人，这一定不是一个没有故事的女同学。你看这里面多少 K 非常多。比如说这里有几个关键的 K fallback method 它可以直接指定你当前的降级方案的方法名，我们可以在这边给出一个 method 等于 abc 那么你在你的同级的类中就要声明一个 abc 的函数，这个函数它接收的方法参数也要跟这个 request cache 保持一致的，不然会报错。好，我们这里先用不上 fallback method ，先把它给去掉。那我们用什么呢？我们再看另外一个属性 comment key 不妨先把它加上去，它用在什么内容上。


大家还记得前面的超时配置吗？是不是很麻烦的一项超时配置呢？那这个 command K 就是可以简化你超时配置的一种方式。我们这里给 comment key 声明了一个叫 cache key 的属性，我们到配置文件里转一圈。走好，这个配置文件里看到这个方法签名吗，我们怎么简化，把它替换成 commandKey 是不是这样？看起来就非常非常简单了。

[image](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/31501efa-230b-4914-ab19-2e27a0692880/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SFPKTHSP%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T225638Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCNHQJOCLSKJikXprN%2FLOqOtGxg2EeuE%2F2AuyE8QrFUfAIhAK9y6eOwOvdog8W7maXGY66dcgjE4wxopYMTm2Mg%2BqOmKogECMb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgyzWu3q0RBl2d%2FV3QQq3AN28jsNIs9d1b3tDtGMcRzSE3s7oKFAIp4jYWNXtqz8cdlOwT1bvEVedbXxfBj4Gcj0BKj5HWmRHlMUAfugJ%2FV2ElkZfhxph3ifl%2F6OUhhNzq%2B9hzuahxQUxOLLDyZX75FJr1f5wzUCTde05wmBSPbwlIzYqvz4jE9GsWWW1n3ay1%2B6nCSo%2BhxJ2EFywaSAAkVUjvPORUnsEy1b5yjPlIIWKzi1dtBqygjO7KVZ8%2F77pp4rPf%2BNnEti5ydSZO4dRS3w4OBwhH%2FNIhBuOhvbupWPiDLwq35fkBG2cPIZapLcf6xYo8yZKxHpuuz2wqdo4AKKzfiWYcX51rXDQ0IXsHWOxBF8Ym%2F66SzDOzlBj6S3aV1dd4PKJxy9xqXaFb4%2Ff%2FHdO584gtCKaUI0Uzib0IBkIzZo2iYBd5k5NPKjT2Sbodz5%2FsmwRYXd3g0aZUto6yNK4T9qu94NrvrobYaev2DI6gCFkMQbzFD9UwXbmMMMF6C84CbvlYlwTxjlBskBJzBtxrEX9Z1PZP8lBCzUpCsHSaD1j9B4bOiRPvHryU0YU%2FWI3iWkKDMajPvjPXlQQva9OZQLRgBDsjuBvzNqy%2FQc6oVV%2B8kKVzihaFSSD0WZk10KH9gsOhz41ADbnjChuv%2FSBjqkAVyiL0U2eHeUI0GS51sIiUYNq50qw1SPECuQHoTkTjh5t4DmrCfZZqfXBB1TJtKDJPgZL%2B%2BaBMSJJsPEWnVzYCs5l2jjn%2BOM2D3%2BT9UIAvrRfrvjhbLv8pEWvkrOFlCtTthsn%2B5Cl9jEI4eYAVyml94q1T8yhfAZVMt3kvHzuG%2BPukEbb6gkOIkMu5KeScNXdGkIWeN0%2BKmRbMIM%2FXsjGDs808Zu&X-Amz-Signature=79aabb70bc96f874001f6e2fac933ece2116fbb553edeb051287d6a2872473a3&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

同学们自己可以在本地起几个小 demo 尝试一下。现在一个彩蛋揭晓了。对不对剩下还有一个彩蛋，我们放到后面的章节再讲，大家放下对彩蛋的好奇，我们回到主线上来，有了服务以后要做什么？ controller 是不是还没有写啊？那我们这里给 controller 里写一个方法，给它起名就叫 request catch 好了，我这里把前面的方法 copy 一下，然后它的返回类型我给它定义成 friend 这里就要传入一个 friend 的名称了。对不对？你叫张三李四，东方吴彦祖，西方吴孟达的都给他叫过来。


好，那我的方法这里就不能调用 my service 了，我要调用谁？刚才创建的 request catch service 我们把它打出来，换个名字叫 request catch serviceok 复制一下，在这里给它调用一把，我为什么不直接把这个返回值 return 回去。这里因为要做一些手脚的，没有这么简单，没那么简单。在这最后我们可以把它 return 回去了。


Return friend. 这里跟大家讲一个程序界的小笑话，以前有一个程序员，他写程序保存一个方法，他怕一次保存，不过结果他放循环，保存 1000 次，就像我们平时 save 文件一样，总耗点 1000 次 save 对不对？那我们这里 cosplay 一下，我怕他取不到，我也再取一次。那么实际上这里就会对 request catch 发起几次调用两次对不对？那我们再看 request 的 catch 里面又调用了两次 service 就现在这个情景来看， service 的 see high 方法将会被调用几次。同样也是两次。
那么我们的 request catch 怎么解决这个问题呢？这里就要讲到正题了，通过 request catch 方法，我可以让它在同一个上下文当中只被调用一次。大家从我这句话中有没有读出一个关键信息，同一个上下文中只调用一次，因为我们的 annotation 是不是都写好了？万事俱备，只欠上下文了。对不对？上下文还没有定义。好，那这里就给他声明一个上下文。


怎么来声明这个上下文的名称叫 high streaksrequest context 是 request 的上下文，声明这样一个变量，怎么把它打开呢？它的打开方式是这样的，同样调用 high streaks context 方法，然后在这后面调用它的哪一个呢？ initialize context 调用这个方法，初始化一个上下文，这就完了吗？别急呀，这个上下文就像文件一样，你把它打开了，在最后还要怎么样，是不是要把它关闭。
那这里我们可以采用 try finally 的方法，在这 finally 里面把这个 context 给它 close 掉。就像这样，这是大家最常用的方法点 close 那还有没有其他方法？有没有更简单的方法？有咱不是引入了 long book 吗？轮不可有这么一个方法。 clean up clean up 它是做什么事呢？它会帮你调用 context 中的 close 方法。


大家如果把这个字节码编译出来，你查看他的点 class 文件，会发现这个 long book 会在编译期间往你的源代码中插入一些生成的语句，这样你就不用再写 final 类方法了。同样的，这个 long book 的小技巧还可以用在很多地方，比如说什么，我前面是不是提到文件的读写对不对？ input stream output stream 还有 file 文件，咱用完之后要把人家关上，有借有还再借不难吗？那这里都可以使用 clean up 来做。


同学们如果说了我想调用的方法，如果不是 close 怎么办呢？也有办法看这个 clean up 里面有一个 value 它的 default 值是 close 如果你想调用的方法不叫 close 比方叫 shut up 那你这里可以很方便的给他起一个叫 shut up 那么这个时候他就会尝试调用对象的 shut up 方法了。
OK 那 control 的定义完 service 定义完，我们去查漏补缺一下，哪些小漏被我们忽略掉了呢？第一个，这个方法名称，咱要给它起一个更贴切一点的名称，叫什么就叫cage ，也不要叫 request 它的 mapping 也是叫 catchok 这一步完了以后，咱再到 service 里面看。在 request catch service 里面咱漏了一个 service 的注解。好加上这个注解以后大家来找茬，在这个页面还能查到哪些错误吗？其实还有一个，我来这里标注一下，这是个 I service 对不对？前面咱注入了谁？前面的 controller 力咱注入的是 my service 那这两个类有什么共同之处吗？你看 my service 是继承自 I service 的。同时 I service 也是一个分 client 标注的注解。那么在这种情况下，假如咱在这个 request 开始方法中一意孤行要注入 iceres 那它是不是有两个实例类型了，spring它知道该注入哪一个吗？并不知道，所以这里就会报错了，而且是在启动的时候就报错。


这里跟大家提两个解决方案，一个解决方案就是把 I service 注入成 my service 这样它就只有一个实例了，100%可以成功。那第二个方案我们依然保留 I service 只不过在 my service 里面动那么一点手脚。


不知道大家还记得这样一个属性吗？前面我们提到过有一个属性叫 primary 对不对？这里派上用场了，我给他声明 primary 等于 true 也就是说但凡你要注解 I service 类型，那把我 my service 当做带头大哥舍我欺谁。但是光改 my service 还不够细心点的同学可能会发现，我们在改 my service 的时候，当指定 primary 等于 true 的时候，这个 true 变成了灰色。灰色是什么意思啊？灰色的意思就是说你即使不指定它也是 true 这是一个不用生命的语句。那我们点进 thin client 里面看一眼，你看它的 primary 默认就是 true 看到这里，同学们就明白了，也就是说给 my service 指定成 primary 等于 true 还不够，我还要把继承的 I service 这里的 primary 指定成什么呢？给它指定成 false 对不对？ OK 那除了 iservice 还有谁我看看，它的继承里面还有个 fallback ，fallback这里你也要把它指定成 false 所以改来改去蛮麻烦的。


我这里建议同学怎么做，采用第一种方案，不要管它的 primary 一切从简。咱就用第一种方案，最简单朴素的什么方案，也就是把这个注解类型从 I service 再换成 I service 就好了。当然前面跟同学介绍的 primary 等于 true 和 false 的设置，也是可以解决问题的。这里就要看同学们各自的喜好了，喜欢哪一种就可以用哪一种老师这里就直接使用 my service 了。最简单。
好，我们 code 部分都已经写完了，接下来要去做什么呢？是不是添加配置文件啦？我们打开 application properties 实际上同学们如果在这个时候直接开启项目，它的 request catch 功能就已经生效喽，那么说明它有一些默认配置是处于打开状态的。我这里为了给同学们做一些演示，所以就不辞辛劳的跟大家演示一下这都有哪些 practice 共同控制了这个功能。


第一个， properties 当然是和谁有关？ request catch 对不对，它是叫 high streaks comment default 前面三个注释打完了，后面不一样了，request catch 再点 enabled 我这里可以把它关闭，也可以把它打开，默认是打开还是关闭打开。好，这里我给它注释叫开启访问缓存功能。


OK 那我们做好了配置项以后，就可以启动项目来进行验证了。是不是我们回到自己的 controller 里面，调用这个 cache 方法需要你开启服务注册中心，我这里已经提前开启好了，然后再开启 final client 我这里也开启好了，最后一步就是把我们的 high streaks fall back application 给它启动起来。在启动之前大家注意把前面的分 client application 的 log 清一下，这样我们好回过头来检查 log 查看它到底发生了几次调用。

```java
spring.application.name=hystrix-consumer
server.port=50000
spring.main.allow-bean-definition-overriding=true
eureka.client.service-url.defaultZone=http://peer1:20000/eureka

# 开启 Feign 的 Hystrix 功能
feign.hystrix.enabled=true
# 是否开启服务降级
hystrix.command.default.fallback.enabled=true

# 全局超时
hystrix.command.default.execution.timeout.enabled=true
# 超时时间
hystrix.command.default.execution.isolation.thread.timeoutInMillisecond=2000
# 超时以后终止线程
hystrix.command.default.execution.isolation.thread.interruptOnTimeout=true
# 取消的时候终止线程
hystrix.command.default.execution.isolation.thread.interruptOnFutureCancle=true
# 开启访问缓存功能
hystrix.command.default.requestCache.enabled=true





#===============Ribbon=======
# 每台机器最大的重试次数
feign-client.ribbon.MaxAutoRetries=2
# 可以再充实几台机器
feign-client.ribbon.MaxAutoRetiresNextServer=2
# 连接超时
feign-client.ribbon.ConnectTimeout=10000
# 业务处理超时
feign-client.ribbon.ReadTimeout=2000
# 所有的Http Method进行重试
feign-client.ribbon.OkToRetryOnAllOprations=true
```


好，我们这里把 high streaks fallback application 启动起来，看到 spring 成功一半，紧接着往下走，很快就已经完全启动好了。那这时候转战到 post 慢里发起一次真实的调用清空 lock 这里 postman 我们向它的 catch 接口发起了一个调用，我先把接口的路径写好。 OK 这个 cache 接口传入的名称是什么呢？我们给它起一个名字，叫王老五不是王老吉王老五钻石的王老五点击 stand 奇迹会不会发生呢？你看，他已经正确的返回了结果。


那么接下来重要的是我们要验证一下这个结果被返回了几次对不对？好，这里转移到分 client application 看有几行log ，同学们是不是只有一行log 。硕大的一个王老五摆在眼前，只有一行 log 这个不失去的又蹦出了一行 log 这第二行可跟王老五没关系，这是友瑞卡服务发现的log ，我们不用去理他，也就是说我们当前的这个上下文当中对服务发起了两次调用，那实际上它在底层只调用了一次，对不对？为什么呢？因为这两个调用之间传入的 name 是不是完全一样的？那如果我把这个 name 在中间摆，那么一道怎么摆？那么一道来我们看，这里给 name 加一点戏，把它换个名字，偷梁换柱，狸猫换太子。


那在这种情况下，我是否还会只发生一次调用呢？我们不妨把当前的 high streaks fall back application 重启一把，看一看它究竟会发生几次调用。好，这个项目已经启动起来了，我们转战到外面 post man 依然是王老五，调用它一次。好，调用完成，我们回到 log 里看一下，在 thin client application 里面看到吗？同学们，这里发生了两次调用。一个是王老五，一个是王老五感叹号，他们的名字分别叫王老五，加上感叹号叫王老五。中文的读法加上一个标点就大不相同。在我们 high streak store 这个 K 也已是一样，你加上一个感叹号，说明它的 K 变了。对不对？我们在 request catch 当中这个标签看到吗？ catch key 它是一个唯一的访问 cache 的 key 在上一层调用里第一次调用的 name 和加上感叹号调用的 name 它属于两个不同的 key 因此它将要实际的发起两次调用。
讲到这里，今天的 request cache 方法就已经结束了，大家是不是有种意犹未尽的感觉啊？我这里给大家做一个总结， request catch 有几个要素分别是哪些呢？我这里有一个口号叫一二一起步走一二一。第一个一是什么呢？ context 也就是你 high strikes 的上下文。那在这里我们虽然是把上下文定义在了方法中，如果我现在出一个思考题 context 你怎么来把它给玩出花头？如果你不想只在方法中应用 request cache 你想把这个整个 context 扩展到更大的范围，你怎么来做好这个问题留给大家课后来思考。我们有很多种方式，包括你可以自定义一些filter 、listener ，甚至可以在容器级别建立这种 context 总之你可以扩大这个上下文的作用范围。这样的话缓存的范围也会扩大。


那刚才说了，一还有一个二是谁呢？我们点进去看这个2，2就是两个 annotation 分别是 catch result 标识了，这个返回的结果是需要加到缓存里的。第二个是什么 catch K 也就是我目前的这个 name 是作为一个 catch K 最后一个还有个一对不对？ 121 最后的这个 1 我就不说要添加 high streaks command 了，大家心里都有数，我来说一个其他的思路。剩下的那个 1 就是一个代码整洁性。比如说我在这里访问了一个 request catch service 对不对？那接下来我想调用另外一个方法，


比如这个方法的名称就叫 abcabc 中，我还想用这个 friend 怎么办呢？两种方式，要么你改方法的签名把 friend 传进去。第二种方法，你索性在下一层方法中再调用一次 request catch 接口。因为不管你发生几次，只要在一个 context 上下文当中，它并不会实际的发起远程调用，而是从缓存当中把这个对象拿出来。这样一来，我们就不必要声明一个接收的参数了，是不是能让你的方法签名看起来整洁一点，这是一个功能。那还有一些情况，可能你在这个方法内你连续调用了好几个本地的不同服务，这不同的服务中间都做了一个操作，那就是调用了某一个特定的服务。这时候我们可以在那个特定的服务上面把这个注解 catch result catch key 都给它加上去，让这个服务的返回值可以被缓存下来。那么你在整个方法的调用链路中，你将会节省非常非常多的资源消耗，你将节省好几次远程调用请求。


OK 那这节课的总结就到这里了，下一节课我们依然去来探讨服务降级中的另一个场景叫什么？多级降级，简单来说，一次降级不行再来一次。 OK 同学们起来做个眼保健操，我们下一节再见。


