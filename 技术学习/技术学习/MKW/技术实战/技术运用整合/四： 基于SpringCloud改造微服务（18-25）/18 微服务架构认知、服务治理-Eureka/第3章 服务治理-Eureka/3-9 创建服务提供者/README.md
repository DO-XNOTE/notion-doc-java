---
title: 3-9 创建服务提供者 
---

# 3-9 创建服务提供者 

[image](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/d929f4f9-6147-49fe-9977-681d1945c5c6/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TA4ZODC5%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T225539Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQD%2FpBmjed6PVsNDqZ8xyuwN3GlAym0jTr%2BK5rVuRhSJiwIhAMjH5IPh78GPjAFYDGedgWlW8tMR9P%2Fw%2BoknnOC2%2BbjOKogECMb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgwhZD3NtsNhU7bydG8q3ANj9R4ZIlp0c%2BTvJEsELh%2BGdMAirWt60DbW%2B8NBYZLWpdGoZoRzNiSO9%2BXlC0rRneDXVChuqpTs7HumGbBAyKdorfIkNS9hrVlEB%2BvxbjQLKhN8qUqJxlwPCK2fyPlX2Yl2Lg3H2rgnvYCe6tOTBzv95YTZyRr%2Bz7nmN2K7onNb7PkoP481i43l6mN6ZshTJxJse%2FfLMTbA42Z24Ord5p4gaM%2F6lOiV9qw37Jy1txX1OpaY0%2FAeMHwl4BuN2Nh2NS%2Biu34mQGPPF6TCmLE%2FJXjlNR%2BfthiF4fsvwb2AYWc5GkmmAelBPfLopchBPOvRIi%2FmA5ZgcvsvJD7dbLFgFVHJSZg1W1LG%2B323BTvx9vZSSbStkKBT36mZTQXVd040zppu2PFc4Jo1sUAak%2BIi7JQuOHYlhoH2GQK35upeJEV6Ks2OYjdxL7LHaHJ9%2B1s8Ic%2FVMfge1dl68bCeU%2F9oTawnt98JmfzHCrbYYY6SOdZtU2Vl1%2FTyU8mtaVUTopcJmOs4sG9rqLegSNvewZS7nZKjfv3y6XMqONMkUcopTQCkca%2F6CrXZmAEj3mkVnUZw4gLk%2BmW09wuVanDzob23FWFPqhpyxm1uZ6NTkMb%2BSmVquCffhIFD%2B6ZJRaIF%2FjDauv%2FSBjqkAd7H6uFpcMN%2Bgadv2nyOWViW7PWFO51Ngx4Bju07LLopVY%2BMQWXiPn%2B88qOh1RMKjXCg1REALuXEhwieqeyy8fzn0Igmev3ekHWWHY1%2BzTxQAXsUzbEktMf7PzWPfXe4DyipeMVv86AgKoTrw%2BXSlpqfUk6hwZWhN0sdvzbtUlULkLCoIjEB0oduPO%2FXj9axIJczOIbTIzIS6bAbSzxXjPH3vFPQ&X-Amz-Signature=9719a40f52968dd160388044b26da0d3ee35b1b317f87b15e277627451cac43b&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

[image](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/2925687f-de89-4399-86f2-71039b8c7c6e/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TA4ZODC5%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T225539Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQD%2FpBmjed6PVsNDqZ8xyuwN3GlAym0jTr%2BK5rVuRhSJiwIhAMjH5IPh78GPjAFYDGedgWlW8tMR9P%2Fw%2BoknnOC2%2BbjOKogECMb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgwhZD3NtsNhU7bydG8q3ANj9R4ZIlp0c%2BTvJEsELh%2BGdMAirWt60DbW%2B8NBYZLWpdGoZoRzNiSO9%2BXlC0rRneDXVChuqpTs7HumGbBAyKdorfIkNS9hrVlEB%2BvxbjQLKhN8qUqJxlwPCK2fyPlX2Yl2Lg3H2rgnvYCe6tOTBzv95YTZyRr%2Bz7nmN2K7onNb7PkoP481i43l6mN6ZshTJxJse%2FfLMTbA42Z24Ord5p4gaM%2F6lOiV9qw37Jy1txX1OpaY0%2FAeMHwl4BuN2Nh2NS%2Biu34mQGPPF6TCmLE%2FJXjlNR%2BfthiF4fsvwb2AYWc5GkmmAelBPfLopchBPOvRIi%2FmA5ZgcvsvJD7dbLFgFVHJSZg1W1LG%2B323BTvx9vZSSbStkKBT36mZTQXVd040zppu2PFc4Jo1sUAak%2BIi7JQuOHYlhoH2GQK35upeJEV6Ks2OYjdxL7LHaHJ9%2B1s8Ic%2FVMfge1dl68bCeU%2F9oTawnt98JmfzHCrbYYY6SOdZtU2Vl1%2FTyU8mtaVUTopcJmOs4sG9rqLegSNvewZS7nZKjfv3y6XMqONMkUcopTQCkca%2F6CrXZmAEj3mkVnUZw4gLk%2BmW09wuVanDzob23FWFPqhpyxm1uZ6NTkMb%2BSmVquCffhIFD%2B6ZJRaIF%2FjDauv%2FSBjqkAd7H6uFpcMN%2Bgadv2nyOWViW7PWFO51Ngx4Bju07LLopVY%2BMQWXiPn%2B88qOh1RMKjXCg1REALuXEhwieqeyy8fzn0Igmev3ekHWWHY1%2BzTxQAXsUzbEktMf7PzWPfXe4DyipeMVv86AgKoTrw%2BXSlpqfUk6hwZWhN0sdvzbtUlULkLCoIjEB0oduPO%2FXj9axIJczOIbTIzIS6bAbSzxXjPH3vFPQ&X-Amz-Signature=b8da93587764cd93528ec2a5acb56e747e359e55c5e01197d81d2f9bdae28174&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

这一节，我们来学习如何在 ure 卡中注册一个服务提供方。那今天课程的主要内容有第一条，先来创建一个 eureka client 子项目，接着在项目中添加 pom 依赖项，让大家看一下作为一个服务提供方，他所需要的依赖项与刚才我们创建的注册中心都有哪些不同之处。再往后是创建启动类和服务内容。这里就是创建一个闷函数，接着就是 controller 层的编写。最后一条就是瞅瞅你在注册中心页面长啥样。


好，以上就是本节课程的主要提纲，接下来我们就进入实战 coding 阶段。好，大家找到上一次我们创建好的项目，在这个项目基础上，

[image](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/3aea6f01-9bb1-4e67-b562-652355134ffc/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TA4ZODC5%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T225539Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQD%2FpBmjed6PVsNDqZ8xyuwN3GlAym0jTr%2BK5rVuRhSJiwIhAMjH5IPh78GPjAFYDGedgWlW8tMR9P%2Fw%2BoknnOC2%2BbjOKogECMb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgwhZD3NtsNhU7bydG8q3ANj9R4ZIlp0c%2BTvJEsELh%2BGdMAirWt60DbW%2B8NBYZLWpdGoZoRzNiSO9%2BXlC0rRneDXVChuqpTs7HumGbBAyKdorfIkNS9hrVlEB%2BvxbjQLKhN8qUqJxlwPCK2fyPlX2Yl2Lg3H2rgnvYCe6tOTBzv95YTZyRr%2Bz7nmN2K7onNb7PkoP481i43l6mN6ZshTJxJse%2FfLMTbA42Z24Ord5p4gaM%2F6lOiV9qw37Jy1txX1OpaY0%2FAeMHwl4BuN2Nh2NS%2Biu34mQGPPF6TCmLE%2FJXjlNR%2BfthiF4fsvwb2AYWc5GkmmAelBPfLopchBPOvRIi%2FmA5ZgcvsvJD7dbLFgFVHJSZg1W1LG%2B323BTvx9vZSSbStkKBT36mZTQXVd040zppu2PFc4Jo1sUAak%2BIi7JQuOHYlhoH2GQK35upeJEV6Ks2OYjdxL7LHaHJ9%2B1s8Ic%2FVMfge1dl68bCeU%2F9oTawnt98JmfzHCrbYYY6SOdZtU2Vl1%2FTyU8mtaVUTopcJmOs4sG9rqLegSNvewZS7nZKjfv3y6XMqONMkUcopTQCkca%2F6CrXZmAEj3mkVnUZw4gLk%2BmW09wuVanDzob23FWFPqhpyxm1uZ6NTkMb%2BSmVquCffhIFD%2B6ZJRaIF%2FjDauv%2FSBjqkAd7H6uFpcMN%2Bgadv2nyOWViW7PWFO51Ngx4Bju07LLopVY%2BMQWXiPn%2B88qOh1RMKjXCg1REALuXEhwieqeyy8fzn0Igmev3ekHWWHY1%2BzTxQAXsUzbEktMf7PzWPfXe4DyipeMVv86AgKoTrw%2BXSlpqfUk6hwZWhN0sdvzbtUlULkLCoIjEB0oduPO%2FXj9axIJczOIbTIzIS6bAbSzxXjPH3vFPQ&X-Amz-Signature=e531db651dd9bfe940cd0e9d5a5a5ca30db0fef924f7ebabd407e8eb67132c43&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

点击 new 再创建一个 module 这个 module 还是使用门美文格式。 OK 它的 artifact ID 我们把它叫做 eureka 杠 client 也就是服务提供者的意思了。 next 这里 module name 依然和前面的 artifact ID 保持一致。然后存放的路径我们还把它放在 eurika 这个 folder 下面。


好，点击 finish 倒数一个数一嘿出来了，我们收起小菜单。这里我们添加必要的依赖项。第一个依赖项是什么？ eureka 对不对？但是这次的 U 瑞卡跟前面我们在注册中心里面添加的 URI 卡依赖有那么一点点不同，我们来看一下。这里先来填写它的 group ID 这个部分都是相同的 spring framework cloud 那 artifact ID 相同的地方是它们一样长，不同的地方是最后一个单词不同。我们来看 artifact ID 是 spring 杠 cloud starter 杠 Netflix 马上就要到不同的地方了尤瑞卡。前面我们在注册中心这里添加是 server 对不对？那我作为一个 client 我作为一个服务提供者，这里我要添加的依赖项是 



clientok 那添加好 cloud 以后，我这边比注册中心还要再多添加一个依赖是什么呢？大家来看，大家可以猜一下，因为我要写 controller 对不对？我写 controller 自然需要什么组件 spring web 对不对？ spring boot 里面的 web 组件。 OK 它的 artifact ID 是 spring boot [starter.web](http://starter.web/) 好嘞到这里我需要的两个组件就都添加进来了。那还有一个地方，我们把它的 name 给指定一下，这样我们做 name 编译的时候，它可能打出一些更友好的信息


name 是 eureka client。 Package. 驾暴到这里，我们这个 palm 文件就已经改写完成了，接下来进入 coding 阶段，创建 controller 创建入口类提供服务。我们弹开小桌板，在这下面继续走到 Java 文件夹下，我们先来建一个 package 前面一张我们说到一切从简，对不对都从 come.imock.spring cloud 这个路径开始。 OK 接下来创建入口的方法，这个入口的方法我们把它叫做 eureka client application 收起小桌板。跟往常一样，我们在这里先创建一个 man 函数， public static man 大家打闷函数的时候是不是有种愉悦的快感，噼里啪啦不用思考。


OK 在这里需要创建一个启动类，和之前的方式一样，创建一个 spring application builder 把当前的类 class 文件放入进来指定它的启动方式。是 web application 中的 serve light 类型。好，一个 run 方法参数传进来。 OK 那这两个注解其中有一个跟上一次相同，是哪一个？ spring boot 对不对？ spring boot application 接下来一个注解稍微有那么点不同，它虽然也是有瑞卡，但是换了个名字，它叫 enable discovery client 这个是个什么含义啊？ 


discovery client 也就是发现服务的意思，意思是它需要到注册中心拉取服务注册列表。
到此为止我们的入口类就已经编写好了，是不是非常简单？接下来我们一起去创建一个 controller 对外提供某些 service 弹开小桌板，找到刚才创建的路径。在这个路径下面创建一个 controller 它的名字同样也叫 controller 好在这个 controller 里面第一件事是什么？给它加一个 annotation 对不对？我们先把小桌板收起来，这个 annotation 就是 rest controller 除此以外，我还给它额外加一个 S L four G 的标签。那这个标签是什么？轮 book 提供的一个标签，它可以方便的生成 logger 属性。这样的话我们就不用在类里面声明一个什么 logger factory get logger 之类的这一行代码了，非常简洁。


接下来声明一个 private 的变量，它是

什么呢？ port port 是什么？端口的意思是不是？我们每个服务启动起来之后，对外提供服务的端口是什么？ OK 它来自于哪里？我们用 value 注解把它从哪里拉过来，大家知道吗？从配置文件对不对？待会儿我们就去配置文件里面加上这样一个属性 server portok 有了 POD 以后，我们接下来提


供一个 private public 的对外提供服务的方法叫 say hi 因为这就是我们 eurika 中的 hello world 所以我们给它使用最简单的 get 形式的 htt 变 method 来传递它的路径。我们同样的也叫 say hi 那返回什么呢？返回一句自报家门，this is A 加上我自己的 pot 好了，既然我有了 get 方法，我不知道有瑞卡是不是也可以很方便的接受 post 对不对？那我这里还想创建一个 post 的方法，摊开小桌板，我给我的 post 加一个 entity 叫什么 friends friend 好不好？这个 friend 里面我给它添加两个简单的属性，一个是 name 属性叫什么名字，第二个属性是 pot 我想把我自己的 pot 写入到这个 friend 对象里面。 OK 在这里加上一个 long book 的 data annotation 它有什么作用呢？大家应该比较清楚了，它就会把这个类中的声明的变量给它生成 get a set to string 之类的方法，非常简洁。



好，我们回到 controller 在这里面，我们有了 friend 接下来就声明一个 host 类型的方法，他返回一个 friend 然后也接收一个 friend 好我们把这个 friend 参数加上来。那再给大家一个 annotation request request body how 他的 URL 是什么？它的URL mapping 路径为了简单，我这边同样给它食指上 say hi 因为这两个方法虽然路径相同，但是 htd P method 都是不一样的，所以也不会产生冲突。那我接收到了 friend 以后，我先打一行 log you are 我把他的名字打出来 get name 好勒。然后我要对这个方法中的属性做一点小小的修改，我把 port 替换成我自己的 port 接下来把它 return 回去。这样的话我的 controller 既有了一个 get 一个 post 接下来我们就去创建一个 properties 文件。


打开小桌板，目光移交到 resources 文件夹，在这里创建一个新的文件名次依然还叫 application properties 第一个属性，我们给它起一个应用的名称， spring [application.name](http://application.name/) 它叫什么呢？ eureka client 第二步和之前注册中心的时候是一样的，我给它指定一个 port 那这个 port 要是所有人都没有访问过的，给它指定个 3 万。
好了，前面一个是 2 万，这个是 3 万，然后我就要指定一个注册中心的地址，那它的属性名称是什么？ eureka.client service URL 这个 U 大写 url.default zone 那它的地址是什么？我们以 HT TB 打头，接下来是 local host 冒号 2 万，这个 2 万就是之前注册中心写上的注册 pot 后面再跟上 eureka 好，我们的服务提供者只需要这三个参数就可以运行了，要弹开小桌板。
那我们接下来就要运行服务提供者了，在运行服务提供者之前，是不是要先把注册中心启动起来？好，我们现在到注册中心的闷函数里直接点击运行这个闷函数，大家稍等片刻，看到注册中心已经 started 以后。好，这里最后一行 lock startedok 那接下来到我们刚才创建的服务提供者的 main 方法里面，同样的方式直接运行这个闷函数，稍等片刻，它会出现一个成功的标志。好，这里看到同样的有一个 started 说明它已经启动成功了。然后接下来它是 UI L 还有端口都打印在这里。那大家看到这里多余有一行叫什么 registration status 20204 是什么含义啊？ no content 是不是？它并不是一个错误的 H ddb status code 那说明你的注册实际上是已经成功了。


OK 接下来大家一起到注册中心的页面上看一下我们刚刚注册上的服务是长得什么样子。我们在新窗口中打开尤维卡注册中心，然后看到这里 instances currently registered with the eureka 那这里是所有的服务列表。在 application 里面我们看到了一个新面孔是谁？ eureka client 对不对？它就是我们刚才注册的服务提供者。那往后看，这里有一个 available zones 那是默认的 default zone 那 status 是什么？ up 说明他现在运行良好，后面是他的 IP 地址端口。那我们这里因为采用的 local host 和 IP 形式的注册，所以说这里有一个小坑。


同学们有可能会发现我的 IP 地址在办公室的时候运行这一套程序都是好的，consumer也能连接上 service provider 那把它带到家里突然就连不通了，这是为什么？因为他的 IP 地址有可能产生变化。那他注册的时候有可能没有用本机的地址，而是用网络分配给他的 IP 地址来进行注册的。那所以这种情况大家不用急，我们现在先把他的注册中心还有服务全部关掉，再重启一下就可以了，这是一个非常简单的做法。


OK 接下来我们到 postman 里看一下刚才启动的服务是不是能够运行成功。好，我这里已经创建了一个 local host3 万的 get URL 那我们发送一个 get 请求，很快就返回了。这是什么？这是我们刚才创建的自报家门的服务，对不对？那接下来还有一个 post 我们把这个 method 改成 post 那这里 header 我们给它指定一个 content type 那应该是什么 value 杰森对不对好，接下来 body 给它指定一个 name 就叫 eureka 然后 pot 我给他写上 1 万，如果他运行正确，他会把我这个 1 万替换成他自己的 3 万。对不对？那如果直接运行会不会有错误呢？我们看一下。果然报了一个错 media type 不支持。为什么我们的 header 这里大家要记得把它勾上，这样的话它才会用 JSON 形式来传输，那再来调用一次。


好嘞，看这里很快调用成功了，它的 name 依然是 eureka port 变成了 3 万。同样的在程序里面也打出了这样一行 lock you are eureka okay 到这里，我们的服务提供者就已经开发完成了。那后面的小结，我会带大家一起创建一个服务消费者 consumer 通过注册中心拉取到的服务注册列表，调用服务提供者的服务。我们下一期再见。





