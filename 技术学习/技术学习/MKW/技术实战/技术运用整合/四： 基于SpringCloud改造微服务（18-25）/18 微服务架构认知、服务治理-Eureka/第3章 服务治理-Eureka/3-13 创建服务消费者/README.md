---
title: 3-13 创建服务消费者 
---

# 3-13 创建服务消费者 

[image](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/bcb99948-4d16-4669-bd07-c45347da35af/SCR-20240820-owky.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664VHNIHMH%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T225543Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDc7QeoCtspcEn5azqQ296v%2FBV6LaLeLn57jYb%2FS9Hc7AIgLwT87thmlU5WoIRxw3TPKMOhZDW9kDvyRrAiEEVQ7gcqiAQIxv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDHlEzFMt4v5JDBzFqyrcA9O%2FmQrjeYroJt5eERf%2BEmbVAgRF166u7zXcDuJcdB2r0hPdYczQ8kUyGIH%2FfU5x9HqmzmMU5kIwyzb8tKwdjdG1A4Qb5C17ioQxtgBEQQ%2BEGe1daEWMappmVcYKj7Ijy5RBY9gs4%2FQk8cytisd6znXiwOBzHP2KS08dKz%2BfBDDC1%2FulYtvqnMpc97%2Fle84Na6GsZTBYEMS%2BXfWhIZltJ1hOCx02e%2F0FTrHCOCkvL8Wv4GwuNX12E1lssTFbFjS%2F5wnMiyk0YUQ%2BUziFy7YWMKAcM6Zd0nk33IKL8IN5oLRforkhzoogjz6qZf9zfckZi2KjnqjSLJKuOZChZDiq0mL1X8z9Owrp%2Bg1DhCX%2FiKiwNH8fwa0Zc9oG2EaoUSH%2FoFAbw4QU%2FYTaLVnRN72i%2F9bk6NQYZcJHJscJg1pS9l4dCueYhKNeDAEG0kqO4LcXCP8%2B8gqJF7rg13XL35V5%2Fk6k%2B0hVwcwqYKZ%2FvqEQRrl0mD5uHGA0lxSQm%2FaFg1KF2GuZziGvM0DYqWrBd14Kge07WRYOJ6%2BzIt7ox%2BhBTfujRiatT1ZLSDXncQFgUXCXxC%2FZ9sATE20fGrf%2FOXBWY6owGeukJWvBJVqPENWI7%2F5Vm5ivi7oDZ9%2BxQyt2MJa3%2F9IGOqUB%2BEqzmhUP33Fw8utyH58GwRA77bVgbInAhiSab4FcOXIekGsRaaWBS9nd%2FfJtxCyGaKgRbIfpEirnfPMBvF7J7lNpIgJJIBxBYC5Bvwlxarrf7L%2FTcbZ6XNDNaFlazO%2F3oqql0g4leYLegBvcSysf54M1OBQ4%2Bx%2FilqASkOUPrm7n4EFnnjpfR9wvtHzuEZictXkHw387UflSUHXdsON4W%2F4SDVon&X-Amz-Signature=3a45498f0f0c06bed50e97d381b5e79caa572615b9155da70d688dbda4b881b2&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

[image](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/abece22c-caea-46aa-b85c-8b3b7f8844b2/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664VHNIHMH%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T225543Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDc7QeoCtspcEn5azqQ296v%2FBV6LaLeLn57jYb%2FS9Hc7AIgLwT87thmlU5WoIRxw3TPKMOhZDW9kDvyRrAiEEVQ7gcqiAQIxv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDHlEzFMt4v5JDBzFqyrcA9O%2FmQrjeYroJt5eERf%2BEmbVAgRF166u7zXcDuJcdB2r0hPdYczQ8kUyGIH%2FfU5x9HqmzmMU5kIwyzb8tKwdjdG1A4Qb5C17ioQxtgBEQQ%2BEGe1daEWMappmVcYKj7Ijy5RBY9gs4%2FQk8cytisd6znXiwOBzHP2KS08dKz%2BfBDDC1%2FulYtvqnMpc97%2Fle84Na6GsZTBYEMS%2BXfWhIZltJ1hOCx02e%2F0FTrHCOCkvL8Wv4GwuNX12E1lssTFbFjS%2F5wnMiyk0YUQ%2BUziFy7YWMKAcM6Zd0nk33IKL8IN5oLRforkhzoogjz6qZf9zfckZi2KjnqjSLJKuOZChZDiq0mL1X8z9Owrp%2Bg1DhCX%2FiKiwNH8fwa0Zc9oG2EaoUSH%2FoFAbw4QU%2FYTaLVnRN72i%2F9bk6NQYZcJHJscJg1pS9l4dCueYhKNeDAEG0kqO4LcXCP8%2B8gqJF7rg13XL35V5%2Fk6k%2B0hVwcwqYKZ%2FvqEQRrl0mD5uHGA0lxSQm%2FaFg1KF2GuZziGvM0DYqWrBd14Kge07WRYOJ6%2BzIt7ox%2BhBTfujRiatT1ZLSDXncQFgUXCXxC%2FZ9sATE20fGrf%2FOXBWY6owGeukJWvBJVqPENWI7%2F5Vm5ivi7oDZ9%2BxQyt2MJa3%2F9IGOqUB%2BEqzmhUP33Fw8utyH58GwRA77bVgbInAhiSab4FcOXIekGsRaaWBS9nd%2FfJtxCyGaKgRbIfpEirnfPMBvF7J7lNpIgJJIBxBYC5Bvwlxarrf7L%2FTcbZ6XNDNaFlazO%2F3oqql0g4leYLegBvcSysf54M1OBQ4%2Bx%2FilqASkOUPrm7n4EFnnjpfR9wvtHzuEZictXkHw387UflSUHXdsON4W%2F4SDVon&X-Amz-Signature=3ceb3c79b0b922db6730414265ebe7d870c6dc4d95b98b39585ba73d4f6b39f8&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

这一节，我们就带大家一起创建一个 eureka 中的服务消费者。这一小节的主要内容有，第一条，我们创建一个 eureka consumers 项目，

[image](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/d4cb7f4a-bc85-4cd1-bd0f-da7c43d7eb88/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664VHNIHMH%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T225543Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDc7QeoCtspcEn5azqQ296v%2FBV6LaLeLn57jYb%2FS9Hc7AIgLwT87thmlU5WoIRxw3TPKMOhZDW9kDvyRrAiEEVQ7gcqiAQIxv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDHlEzFMt4v5JDBzFqyrcA9O%2FmQrjeYroJt5eERf%2BEmbVAgRF166u7zXcDuJcdB2r0hPdYczQ8kUyGIH%2FfU5x9HqmzmMU5kIwyzb8tKwdjdG1A4Qb5C17ioQxtgBEQQ%2BEGe1daEWMappmVcYKj7Ijy5RBY9gs4%2FQk8cytisd6znXiwOBzHP2KS08dKz%2BfBDDC1%2FulYtvqnMpc97%2Fle84Na6GsZTBYEMS%2BXfWhIZltJ1hOCx02e%2F0FTrHCOCkvL8Wv4GwuNX12E1lssTFbFjS%2F5wnMiyk0YUQ%2BUziFy7YWMKAcM6Zd0nk33IKL8IN5oLRforkhzoogjz6qZf9zfckZi2KjnqjSLJKuOZChZDiq0mL1X8z9Owrp%2Bg1DhCX%2FiKiwNH8fwa0Zc9oG2EaoUSH%2FoFAbw4QU%2FYTaLVnRN72i%2F9bk6NQYZcJHJscJg1pS9l4dCueYhKNeDAEG0kqO4LcXCP8%2B8gqJF7rg13XL35V5%2Fk6k%2B0hVwcwqYKZ%2FvqEQRrl0mD5uHGA0lxSQm%2FaFg1KF2GuZziGvM0DYqWrBd14Kge07WRYOJ6%2BzIt7ox%2BhBTfujRiatT1ZLSDXncQFgUXCXxC%2FZ9sATE20fGrf%2FOXBWY6owGeukJWvBJVqPENWI7%2F5Vm5ivi7oDZ9%2BxQyt2MJa3%2F9IGOqUB%2BEqzmhUP33Fw8utyH58GwRA77bVgbInAhiSab4FcOXIekGsRaaWBS9nd%2FfJtxCyGaKgRbIfpEirnfPMBvF7J7lNpIgJJIBxBYC5Bvwlxarrf7L%2FTcbZ6XNDNaFlazO%2F3oqql0g4leYLegBvcSysf54M1OBQ4%2Bx%2FilqASkOUPrm7n4EFnnjpfR9wvtHzuEZictXkHw387UflSUHXdsON4W%2F4SDVon&X-Amz-Signature=307b7c4be6d0c8e729f6e013688a8f4294abffec3fdb755f2ff39b4244b9f9b7&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

紧接着向这个项目中的 palm 文件添加必要的依赖。第三步，创建一个慢方法，也就是启动类，并且创建相应的 controller 层。最后一步就是在我们的 controller 里利用默认的负载均衡器，像 eureka client 也就是尤瑞卡的服务提供方发起真正的服务调用。


大家准备好了吗？拿起东西，我们开拔又来到了熟悉的开发环境当中，选中 spring cloud 的 demo 项目，点击 new new 一个什么 module 对不对？一个 Maven 的 module 那它的 artifact ID 是 eureka 杠 consumer 我们把它复制一下。那 module name 这里粘贴和前面的 artifact ID 保持一致，这个源码的存放路径我们依然把它放在尤瑞卡下面，点击 finish 出来。好勒。那这个泡姆文件这次就不一个一个手打了，直接借鉴自由瑞卡 client 把这个内容 copy 过来。那大家知道程序员最擅长的两件事是什么吗？ copy and paste 对不对天下文章一大抄，看你会抄不会抄，这个 name 改一下变成 eureka consumer 再顺手把 packaging 指定成这。


好了，那接下来我还想再引入一个依赖是什么？是 springboot 包下的一个内容， spring framework.boot 是它的 group ID 然后 artifact 是 actuator 大家知道这个类是干什么的吗？应该也有用过。 act to reader 好了，把 version 删掉。 OK 这个类是 sprint boot 下面用来做一些注入健康检查、审计统计或者监控的方法。 OK 到这里，我们的 Tom 就定义完了，接下来要去创建入口的慢方法以及 ctrl 类。


好，点开 Java 文件夹，在这下面创建一个路径，那路径我们还叫 come.imock.spring cloud 老样子。接下来新建一个闷方法，它的名称就叫 eureka consumer consumer application 我大家觉得名字太长了，可以也把 application 简写成 App freestyle 好在这个嫩方法里面，我们先把它声明出来。


public static white man string 在这里面的启动方式和之前的服务提供者是一样的。我们 new 一个 spring application 的 builder 作为启动类，把当前类的名字传进去。它的启动方式是什么呢？ web application 中的 server light 类型对不对？然后执行 run 把参数放进去。好勒到这里，启动部分完成了，它的 annotation 都有什么？和之前是不是应该是一样的？那就是 springboot application 下面一个也是 eurika enable discovery client eurika 的注解，大家发现 consumer 服务调用者和服务提供者的全套注解，包括启动方式其实都是一样的。


好，创建完了闷方法以后，我们接下来就去创建一个 ctrl 了，对服务提供者发起真实的调用，弹开小桌板，在刚才创建的文件夹下面再来创建一个 controller 这个类的名字依然把它叫做 controller 收起小桌板。那 ctrl 的抬头先给他来一个 rest ctrl 的注解。


接下来我们调用 service provider 的哪个方法、物提供者的哪个方法是不是第一个 get 方法。我们现在声明一个同样的 get 叫 hello 它的 uro mapping 是什么？跟它保持一致我们也叫 hello 这相当于一个 hello world 接下来要干什么？要去知道该调用哪个服务对不对？因为我现在丈二和尚摸不着头脑，我不知道有哪些服务提供着。那这时候我们需要一个额外的组件，这组件是什么呢？大家看 private load balancer client 好嘞，这是一个简易的 load balancer client 我们在后面的章节将介绍一个专业选手 raben 也是 spring cloud 中的一个组件。


在这一节我们先勉强用一下这个简易组件，我们把它 out wire 的进来，大家觉得是不是缺少了什么东西对不对？我们光把它 out wire 的进来好像还没有声明它，那需要在哪里声明它吗？其实这里并不需要。当我们把整个 spring eureka 加载进来的时候，这个 load balancer 也已经完成了初始化，我们这里并不要单独来声明。 OK 那大家继续写 ctrl 中的方法。


第一个，我们先要拿到各服务提供者的实例，这时候我们用一个什么类结束 service instance 对不对？一个 service instance 就是服务提供者的实例，那怎么会来获取，当然是从 client 来获取了。作为一个负载均衡简单的负载均衡器，它会帮我们从注册中心拉取到的服务列表中挑选一个可用的 service providerok 那这里使用它的 choose 方法对不对？数字方法提供的参数是什么？参数就是你的服务名称，那服务名称是 eureka clientok 我们把它放到上一行可以显示下。


好的，那这里做一个防御性编程好不好？什么叫防御性编程？就是我假定所有的输入都是不安全的，你这个 instance 有可能 get 到空对不对？我做一个防御性的编程，这里如果是空的话，我就 return 一个 no available instance 那如果不为空，我是不是就要发起调用了？调用的之前，我先要知道访问哪个地址对不对 target 我们把它叫做 target 在这里我们拼接一个地址，用 string 的 format 方法。
这个地址是什么类型的？ HTTP 类型对不对？然后接收两个 string 大家看到这个 URL 的形式应该就能 89 不离 10 猜到这两个 string 都是什么类型的，一个是它的 IP 另一个就是它的端口对不对？紧接着后面我们调用 say hi 还记得前面我们在创建服务提供者的时候创建了一个 get 方法一个 pose 的方法对不对？全部都是say 。


接下来把他的 pot 给塞进去，pot从哪里来？ pot 和 IP 从 instance 里面来，对不对？看到这里 get host 吗？这里就是他的 IP 相应的 pot 就是 get pot 好勒，拿到 target 以后，我们在这里把它打印出来，这里引入一个 sl four G 这样我们就可以用 log 把它很轻松地打印出来。 uil is 加上 target 打印完之后我们好像什么都获取到了。对不对？有了目标地址。


接下来就是发起真实的服务，调用了真实的服务调用怎么发起？我们这边需要借助一个 rest template 的类 rest template 好我们先把它声明出来，再把它注入进来。 rest template 有一些替我们写好的 get setter 之类的方法，我们可以直接使用。因为我们访问的是一个 get 请求对不对？所以这里使用 get for object 这个类。 OK 他的访问地址是什么？是不是target ？然后是 string 类型 string.class 好的，那这里就发起了一个调用，接着我要把调用的结果给它 return 回去。对不对？这样的话整个 get 方法就完成了。但是其实这里还缺了一步，大家知道是哪一步吗？这个 rest template 我们把它 out wide 进来，是不是？那需要在哪里声明它一下。没错，这个可就需要单独声明一下了。我们摊开小桌板走到最外层的闷方法中，那用一个简单的方式来声明。在这里我直接使用 public rest template 直接声明一个这个方法， return 一个 new arrest template 好什么都不做。在这个方法中头顶上加上一个 bin 这样 spring 就在初始化的时候会把这个方法加入到上下文，从而我们在自己的 controller 里就可以得到这个方法了。


OK 那既然有了 get 方法，大家知道在之前的服务提供者里面，我们还创建了一个 post 对不对，那这里也同样的写一个 post 形式的方法。好了，post方法和 get 方法基本上一致。那我们这里直接把它 copy paste 过来。大家知道程序员为什么这么喜欢 copy paste 吗？都是有原因的。这个 mapping 把它改成 post mapping 还是使用 hello 方法名防止重复改一下下面的内容。


get instance 是一样的一套防御性编程，如果没有就返回空，那么再往下它的 target 也是一样的，因为我们访问的是同一个 controller 对不对？它的服务地址也是 say hi 接下来在后面这里就不同了，我们的 get 方法中是用的 get for object 那 post 方法自然是要使用 post for object 对不对？大家还记得在我们的服务提供者中，它的 post 方法接受的参数是什么吗？是一个 friend 的对象对不对？所以我们这里在这个项目中也同样的创建一个 friend 对象，弹开小桌板直接到 eureka client 里面，把这个对象偷过来 copy paste。那我们现在也有一个 friend 对象了，回到 controller 里收起小桌板。那这个 friend 对象怎么用呢？在这里先把它声明出来。你有一个 friend 对象，这个 friend 的名称，我们给它起一个就叫 eureka consumer 好了，最后啊我们要把这个对象传出出去，调用的方法是 post for object 然后它的地址是 target 没错，参数呢就是 friend 参数类型，这里我也要帮它改一下，改成 friend 的类型。


好，大家看这里出了一个红框，对不对一条红线哪里出错了？方法类型的返回值不匹配对不对？ copy 把我们这个 hello post 的方法同样的改成 friend 这个防御性编程，这里我们就返回一个空号了。到这里， get 和 post 都已经完成了，接下来大家要去做一个步骤是什么？初始化文件配置对不对，说走就走。


打开小说版，把目光聚焦到 resources 文件夹 eureka consumer 下的 resources 文件夹下面。我们做什么？创建一个 application properties 对不对？ properties 那这里面的内容，我们直接从 eureka client 里面把它 copy 过来。大家看这又是 copy paste 所以很多技术人员他们的一生 50% 的时间都是 copy paste 好，这里我们把 application name 改成 eureka consumer consumerok 它的端口现在就不能 13 万了。对不对？这样的话它就会跟服务提供者有冲突，我们把它改成31,000。然后下面的有瑞卡注册中心的地址保持不变。那保存好了之后，我们现在万事俱备，只要把这三个应用全部启动起来就好了。对不对？按照一个顺序，先把尤瑞卡 server 启动起来，再启动服务提供者，再启动消费者。就如果大家启动完注册中心以后，先启动了 consumer 再启动 client 这时候发起调用可能会失败。


为什么？因为在你的 consumer 启动好的时候，他尝试从注册中心拉取服务注册表。那在这个时刻克莱恩特可能还没有注册，所以说他拉取到的列表是一个空。那这种情况下，大家只要等几分钟，等它的服务发现机制，再次刷新服务列表的时候，就可以获取到注册好的 client 了。


好，我们这里看到服务注册中心以及 service provider 全部注册成功了。那接下来到有瑞卡 consumer 的闷方法中，我们直接把消费者也可以启动起来，看到 spring 大标签应该默念什么，成功一半对不对？给我们带来一个好运。好， started 我们三个应用到现在全部启动起来了。接下来我们去注册中心的页面上看一下，注册好的应用是不是都可以显示在上面。好，现在是服务注册中心的页面，在这里看 application 有几个？怎么只有一个尤瑞卡 client 好像少了点什么？对不对？那是我还没有刷新，我们点一下刷新按钮。咦这里就出现了两个服务，分别是我们的服务提供者以及服务消费者看一下他们的状态都是 up 也就是都是可用状态，IP地址是相同的，因为我们都是本机应用，不同的地方是端口一个31,000。那可以看到服务消费者和服务提供者都已经正确的注册到了注册中心上。接下来我们就使用 postman 向 eureka consumer 也就是服务消费者发起一个调用，看它在背后能否通过注册中心拉取到的服务列表，找到对应的服务提供者。


好，我们打开 postman 这里我已经写好了一个 get 方法，这个 get 方法向 local host 31,000 发起一个 get 请求，它的路径是 hello 这个是发到服务消费者上的，我们调用一下，很快返回了结果，看结果是什么。 this is 3 万对不对？ 3 万是谁 3 万就是服务提供方，这说明了服务提供方已经正确的响应到了请求，那服务消费者也找到了正确的服务提供方的地址。


get 试玩。我们是一把 post ghost 这里没有 body 我可以把它删掉，因为我们在 controller 里没有接受 body 它的 header 依然是发到 JSON 这里试一下，也很快地收到了响应。那它的 name 是什么？ eureka consumer 对不对？这是在哪设置的？在我们的服务消费者的 controller 里传入过去的。那 potpot 就是服务提供者在它具体的逻辑端把这个 pot 替换成了自己的端口号 3 万。


通过上面两个例子说明 get POS 的请求都在尤瑞卡的架构下面完整的运行了，我们的 eureka consumer eureka client 还有注册中心，三个角色之间的通路也是完全正确的。接下来就让我们一起通过图文教程去看一下服务续约、服务心跳和服务剔除背后的原理，以及他们之间是怎么互相运作的。




