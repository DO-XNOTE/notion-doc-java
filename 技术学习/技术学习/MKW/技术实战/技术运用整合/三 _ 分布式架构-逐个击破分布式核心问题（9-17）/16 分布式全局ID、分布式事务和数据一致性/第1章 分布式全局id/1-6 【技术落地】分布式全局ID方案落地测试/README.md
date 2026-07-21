---
title: 1-6 【技术落地】分布式全局ID方案落地测试
---

# 1-6 【技术落地】分布式全局ID方案落地测试

[image](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/8373b51e-fec0-4859-bd50-ba3d39472422/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664AZYZKZT%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T225426Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIBYsc3bi6YUwx%2BI1TlFXer855%2FPf%2BBJKi6TRo9gbqprMAiA7YNtbWMQI%2Fn1m6t8Y6Soe5us5SkgJEjQLEiHAaDF7BSqIBAjG%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMRccBYJZkxiZ1LiRUKtwDOBnx0Zcwu2DbHRBWcUTe6eNWyTN%2FKvmr93n%2BT1c8yRfdq9uGnwLzwJP%2F0aY65hdsD%2BTS7ghkZgDbHz%2BZkBhCbw8vSsQVUItZSCienjKuWGfCixeoq7N11dKQd1RqnL91XUUGTmucfTIRTnsprIdmB1jjXwsVUxlh%2BrMGMdaCk9mVnQsAr0wqseATjZZhMIpPHNpRerg0KdIfP0rRvkbTn0%2BYto73GsUNvIhRYjgiyawELcyM0bwcEZwCTqV4PKwwNX0ws%2FjlK8dV2%2BNz7smZKuSBiQNEIz97EWeoxgrDjV%2BR9tjgVA9Y%2BhLYW1hvIE7Inp99U1XMI8jQwzb%2B2AuA4G4vTyZKgQYdF6yHR%2B69uU05DCPzsr2%2FfXztdYkNPO0Al7WVED9bQ3f5vdrI0nEzOV1vn3DO8v%2FGu9ZqjzzhZh7Dc3NcQky3cXX1P0Ezw2dp%2FZ8tk%2BkgGpATYZTFust99zh41x5ShhkqtW1P5upMYqwF3pQvvuhr5YYBqhCYFkT2IGjRWcBUxTE74tGK9ppKcOH7mkp2alcXs0nG5WqWhQMTNwvJTLuqOLPFaB%2BH5cWaoIbKN5FlWHfHnbgjN9Rlztz9H%2BYlFn2Y1PIK7%2BLOwTEmKjtDKDGgWr7JPjAwtLr%2F0gY6pgFrkRFtENB4fAQbBJUW6pJnAHEuS6IQt9mWWqGED%2BKK2X7Xbu78LWZZMxI0Mrx4yotvKwBirq7hntPMrN9SBd%2FMNu9l5e7OtokAxggqO8dI4mrEY8R8%2FfeqViz2twkiV%2FykixQbSCgBqa46cz%2B3VmZIoVvt%2F0ylhlhM5GfxQskLe6xzFHJNElAX6pykDmwKMo%2FsRNNz9prk6Pq4W9yCObuyO755kyKp&X-Amz-Signature=4d3004153e80427a08967fe7efd744e06e0fe339645f8671c238bda76b5279dd&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

[image](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/6d6cf8bd-1416-4582-a847-c91d69aed427/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664AZYZKZT%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T225426Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIBYsc3bi6YUwx%2BI1TlFXer855%2FPf%2BBJKi6TRo9gbqprMAiA7YNtbWMQI%2Fn1m6t8Y6Soe5us5SkgJEjQLEiHAaDF7BSqIBAjG%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMRccBYJZkxiZ1LiRUKtwDOBnx0Zcwu2DbHRBWcUTe6eNWyTN%2FKvmr93n%2BT1c8yRfdq9uGnwLzwJP%2F0aY65hdsD%2BTS7ghkZgDbHz%2BZkBhCbw8vSsQVUItZSCienjKuWGfCixeoq7N11dKQd1RqnL91XUUGTmucfTIRTnsprIdmB1jjXwsVUxlh%2BrMGMdaCk9mVnQsAr0wqseATjZZhMIpPHNpRerg0KdIfP0rRvkbTn0%2BYto73GsUNvIhRYjgiyawELcyM0bwcEZwCTqV4PKwwNX0ws%2FjlK8dV2%2BNz7smZKuSBiQNEIz97EWeoxgrDjV%2BR9tjgVA9Y%2BhLYW1hvIE7Inp99U1XMI8jQwzb%2B2AuA4G4vTyZKgQYdF6yHR%2B69uU05DCPzsr2%2FfXztdYkNPO0Al7WVED9bQ3f5vdrI0nEzOV1vn3DO8v%2FGu9ZqjzzhZh7Dc3NcQky3cXX1P0Ezw2dp%2FZ8tk%2BkgGpATYZTFust99zh41x5ShhkqtW1P5upMYqwF3pQvvuhr5YYBqhCYFkT2IGjRWcBUxTE74tGK9ppKcOH7mkp2alcXs0nG5WqWhQMTNwvJTLuqOLPFaB%2BH5cWaoIbKN5FlWHfHnbgjN9Rlztz9H%2BYlFn2Y1PIK7%2BLOwTEmKjtDKDGgWr7JPjAwtLr%2F0gY6pgFrkRFtENB4fAQbBJUW6pJnAHEuS6IQt9mWWqGED%2BKK2X7Xbu78LWZZMxI0Mrx4yotvKwBirq7hntPMrN9SBd%2FMNu9l5e7OtokAxggqO8dI4mrEY8R8%2FfeqViz2twkiV%2FykixQbSCgBqa46cz%2B3VmZIoVvt%2F0ylhlhM5GfxQskLe6xzFHJNElAX6pykDmwKMo%2FsRNNz9prk6Pq4W9yCObuyO755kyKp&X-Amz-Signature=5382c4a5b2771c0ea3e8e37988bb388865bf477ee9a0faebfed306edf34c05d1&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

那么要保证你部署多台机器以后，这个 ID 也不重复，咱们关键就要看这个沃克 ID 了是吧，咱们看看这个沃克 ID 它是在哪定义的 worker ID 在这里定义是吧，然后这块通过构造函数把这个 worker ID 给传进来的对吧。


那么咱们看一下这个构造函数，它是在这个 SID 这个方法里边，SID这个方法里边在这儿的是吧，传入了一个 available work ID 是吧，咱们再看一下 configure 这个方法是在这里边传入一个 default book ID strategy 是吧，然后这块去调用 available work ID 那么这个 available work ID 它等于多少呢？咱们看看这块直接返回了一个 work ID ，这个 work ID 它在哪定义的？在这是吧，那么默认它就是 0 是不是0？咱们这块写个测试程序测试一下，咱们看看这块进入到这个 test 的目录，打开这个 test 的类是吧，咱们写一个这个 SID 的测试程序。那么前边这两个注解咱们给它放开，然后后边写一个测试程序 public word test ID 是吧，然后上面打上一个 test 注解，然后再把 SID 给它注入进来 private SID 对吧，然后上面打上一个注解 o2y 这里边咱们 sid.next shot 是吧，然后 sout 打印对不对？这里边咱们打个断点，咱们在这个 ID 沃克这块打上一个断点，然后咱们调试一下程序 debug 断点断住了是吧，咱们执行一下这个 work id.available work ID 是吧，运行一下。是零是吧。


因为这个里边 available work ID 它直接就返回了这个 work ID 了是吧？这个 work ID 也没有给它赋值，对不对？就直接返回了，返回的肯定是一个0。那么当我们部署多台服务器的话，如果同一时刻把两个请求分配到了不同的机器上，那么他得到的这个 ID 就是相同的了。那么没有办法保证它是唯一的。


这块咱们再看看这个默认的 work ID 的这个策略，他只是调了一个 available work ID 其他的方法都没有调用。看看写了这么多方法是吧。咱们来看看，这个接口有三个方法，其中有一个初始化的方法，这个方法是不是没在咱们的程序当中没有用到对不对？咱们看看里边的实现。首先看看它有没有初始化对吧，这个就是一个布尔类型，那默认是 false 是吧，false的话它会进行初始化，初始化以后再把它变成 true 咱们现在就重点的要看一下这个 init 了，看一下 init 这个就是沃克 ID 的这么一个方法对吧，咱们快速的看一下。


一开始这个沃克 ID 他要找放的 vivo work ID 他要调用这个方法。那么这块咱们也打断点调试一下，咱们在这块打一个断点，然后回到 SID 的这个方法。在这里边咱们调用一下这个 worker ID strategy.init 是吧，要给它先初始化一下。然后咱们再看看这个沃克 ID 到底是什么，咱们再重新的去执行一下。好，到了这个初始化的方法里边了是吧，已经过来了，然后咱们去执行下一步得到的 work ID 是负1，这个肯定也不是一个正常的结果。 work ID 负1，然后往下走到 else 里边，然后后边又有一个 work ID 他又去寻找这个 work ID 了，咱们再看还是负 1 以后然后又调用了一个 increase 咱们再往下接着走看看默克 ID 还是负1。韩式服役以后他要调用一个 try to create on IP 那么从这个名字就可以看出，他要根据你的 IP 去生成一个沃克 ID 了对不对？那么咱们继续往下走。


这个沃克 ID 生成成功了，那么咱们现在就可以推断了它在不同的机器上去部署的话，因为你不同的机器肯定 IP 是不相同的，然后你的 work ID 也是不相同的。那么到最后咱们在调用这个 next shot 的时候，通过这个 next ID 这个方法最后去返回，那么这个 return 那它就可以保证是唯一的了对吧，因为 diff 加 sequence 在同一时刻有可能相同。然后咱们如果这个应用需部署在不同的服务上，那么这个 work ID 是不同的，是不是就可以保证它是全局的唯一了？咱们把这个方法走完。


到了这个 encode 这个方法了，咱们也跳过得到一个唯一的 ID 了是吧，那么这个是不是就可以保证我们在部署多台服务器的话也能够得到这个全局唯一的 ID 那么就可以证明在咱们的这个天天吃货的项目当中使用这个 ID 沃克是可以产生全局唯一的 ID 的对吧？咱们只需要在这一块把这个初始化的这一个过程给它加上就 OK 了。对不对？那么分布式全局 ID 咱们天天吃货这个项目是已经满足的，那么咱们分库分表的时候就可以大胆的去使用这个分布式的全局 ID 了。好了，那么本次的课程到这里就先告一段落了。


