---
title: 3-6 搭建注册中心 
---

# 3-6 搭建注册中心 

[image](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/4060bac6-eff0-49f8-b060-cfc1d53c08aa/SCR-20240820-oncl.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666U7A6WTZ%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T225537Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIFapYQQ5IW7yQoiGCoI9EjSngn8N60rFmhxbTS3o0wo1AiAilw8P2FiUvWghWBYodM8tlGo3uJv3ylyAt2m5XwBhyiqIBAjG%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMHhVD7ZtFwGr6ynCDKtwDmMhUaM3TIJF8%2B8RKra6LPQTyUn2g2yY%2B7hy0mDHlm2M0FGL4Ps7i70Gy3GIEqz605bZs0OR6qflEO%2Fjb1AX0MlzQqlqBZAQ0nO9ixQC3kwbdUIqN34DfBqQg245M%2B9EUOgP47aAUs7bwjkaeyKvCNC3J8ZDub%2BHKzfiBdnB7LfMujlYmP9eySnYk6lxSh8r1HDrHg8hT7oeZKWiYyX1ifGvmKDLdT%2Bwnn8cEJl9NFv%2Bvnh0sWoy4vH%2FVT%2BtvW3l%2Bb1HnQQq4MWFW84qwHMGDWzYBZM5HEH3dwXl6My9tsKxw3SkvAa5LLTCWkbsOErQ4fdEUwfHHGgh85AF8L2zT4HxOgKsuwfB%2FWFW4vL%2B5GPOhA76LBNYhUU9XaefKd4khFLQaWGrcXpFpiNnsCEzaJUcGHq6%2FWcgtz1k2AltZEGhMREPPAWKlTXBfGw0z%2BfabW5z8GHspVHfZ9rhhb9cADRlfA3cJLx8a1y8v49E7987vd48qyrZJbobiHTrrVWUTZxU7IZGqekykjCELAnTHJ2SR0XhWL21boK7b4BEMAXixkRk3qHiskfk6sDNRNagOdP79ha9w7OF4GEBMDWyUlEDs8cmlhPgNC5ApKTmDk9FJTEvucl0CMF93wA4wlrj%2F0gY6pgHbMI1DmixtYiGnBNCzXJ%2FP4%2BaGm3Z1Ph5yO9qp6mVZO8tS64ACu3KUQUJN6UNmQz6NKNpoQOxH0JoDGi%2B2KbkWPAxp0Z%2BKsk04D8CZzWU3Wbnj%2B5woZnBO%2FDOG9Kw%2FXHEapqwEfLfkg0wovLKNH41MJ%2FOUaRsd3HNEu96AvCTKk87IYS2xV0ur62uMWss%2FmmlW8XuZ9PiM8d%2BA%2BBrs%2FzRoz1D86pBC&X-Amz-Signature=d551cecdbd374a28ec43e1bb4d06b0f559f562656492b9ae772070fa4eb5ba62&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

[image](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/a6025f29-d64c-4f30-9be4-230c27551e4b/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666U7A6WTZ%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T225537Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIFapYQQ5IW7yQoiGCoI9EjSngn8N60rFmhxbTS3o0wo1AiAilw8P2FiUvWghWBYodM8tlGo3uJv3ylyAt2m5XwBhyiqIBAjG%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMHhVD7ZtFwGr6ynCDKtwDmMhUaM3TIJF8%2B8RKra6LPQTyUn2g2yY%2B7hy0mDHlm2M0FGL4Ps7i70Gy3GIEqz605bZs0OR6qflEO%2Fjb1AX0MlzQqlqBZAQ0nO9ixQC3kwbdUIqN34DfBqQg245M%2B9EUOgP47aAUs7bwjkaeyKvCNC3J8ZDub%2BHKzfiBdnB7LfMujlYmP9eySnYk6lxSh8r1HDrHg8hT7oeZKWiYyX1ifGvmKDLdT%2Bwnn8cEJl9NFv%2Bvnh0sWoy4vH%2FVT%2BtvW3l%2Bb1HnQQq4MWFW84qwHMGDWzYBZM5HEH3dwXl6My9tsKxw3SkvAa5LLTCWkbsOErQ4fdEUwfHHGgh85AF8L2zT4HxOgKsuwfB%2FWFW4vL%2B5GPOhA76LBNYhUU9XaefKd4khFLQaWGrcXpFpiNnsCEzaJUcGHq6%2FWcgtz1k2AltZEGhMREPPAWKlTXBfGw0z%2BfabW5z8GHspVHfZ9rhhb9cADRlfA3cJLx8a1y8v49E7987vd48qyrZJbobiHTrrVWUTZxU7IZGqekykjCELAnTHJ2SR0XhWL21boK7b4BEMAXixkRk3qHiskfk6sDNRNagOdP79ha9w7OF4GEBMDWyUlEDs8cmlhPgNC5ApKTmDk9FJTEvucl0CMF93wA4wlrj%2F0gY6pgHbMI1DmixtYiGnBNCzXJ%2FP4%2BaGm3Z1Ph5yO9qp6mVZO8tS64ACu3KUQUJN6UNmQz6NKNpoQOxH0JoDGi%2B2KbkWPAxp0Z%2BKsk04D8CZzWU3Wbnj%2B5woZnBO%2FDOG9Kw%2FXHEapqwEfLfkg0wovLKNH41MJ%2FOUaRsd3HNEu96AvCTKk87IYS2xV0ur62uMWss%2FmmlW8XuZ9PiM8d%2BA%2BBrs%2FzRoz1D86pBC&X-Amz-Signature=671796c3bf7c00d2fd6d23bfbbae28317588fff45489da548ef40ef52bbfc393&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

今天我们终于到了尤维卡章节第一个代码实战环节。接下来我就带大家看一下今天课程的内容都有哪些。第一步，我们先来创建一个 demo 的顶层项目，在这个项目之下再创建一个子项目 eurika servereurika server 就是我们放注册中心代码的地方。我们要依次向顶层项目的 pump 文件以及子项目 eureka server 的 pub 文件中添加依赖，让大家明白搭建一个服务注册中心都需要哪些？ Maven dependency. 第三步，设置启动类。

[image](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/ce97d722-eb3f-44f3-9620-5cba545caaa5/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666U7A6WTZ%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T225537Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIFapYQQ5IW7yQoiGCoI9EjSngn8N60rFmhxbTS3o0wo1AiAilw8P2FiUvWghWBYodM8tlGo3uJv3ylyAt2m5XwBhyiqIBAjG%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMHhVD7ZtFwGr6ynCDKtwDmMhUaM3TIJF8%2B8RKra6LPQTyUn2g2yY%2B7hy0mDHlm2M0FGL4Ps7i70Gy3GIEqz605bZs0OR6qflEO%2Fjb1AX0MlzQqlqBZAQ0nO9ixQC3kwbdUIqN34DfBqQg245M%2B9EUOgP47aAUs7bwjkaeyKvCNC3J8ZDub%2BHKzfiBdnB7LfMujlYmP9eySnYk6lxSh8r1HDrHg8hT7oeZKWiYyX1ifGvmKDLdT%2Bwnn8cEJl9NFv%2Bvnh0sWoy4vH%2FVT%2BtvW3l%2Bb1HnQQq4MWFW84qwHMGDWzYBZM5HEH3dwXl6My9tsKxw3SkvAa5LLTCWkbsOErQ4fdEUwfHHGgh85AF8L2zT4HxOgKsuwfB%2FWFW4vL%2B5GPOhA76LBNYhUU9XaefKd4khFLQaWGrcXpFpiNnsCEzaJUcGHq6%2FWcgtz1k2AltZEGhMREPPAWKlTXBfGw0z%2BfabW5z8GHspVHfZ9rhhb9cADRlfA3cJLx8a1y8v49E7987vd48qyrZJbobiHTrrVWUTZxU7IZGqekykjCELAnTHJ2SR0XhWL21boK7b4BEMAXixkRk3qHiskfk6sDNRNagOdP79ha9w7OF4GEBMDWyUlEDs8cmlhPgNC5ApKTmDk9FJTEvucl0CMF93wA4wlrj%2F0gY6pgHbMI1DmixtYiGnBNCzXJ%2FP4%2BaGm3Z1Ph5yO9qp6mVZO8tS64ACu3KUQUJN6UNmQz6NKNpoQOxH0JoDGi%2B2KbkWPAxp0Z%2BKsk04D8CZzWU3Wbnj%2B5woZnBO%2FDOG9Kw%2FXHEapqwEfLfkg0wovLKNH41MJ%2FOUaRsd3HNEu96AvCTKk87IYS2xV0ur62uMWss%2FmmlW8XuZ9PiM8d%2BA%2BBrs%2FzRoz1D86pBC&X-Amz-Signature=2d70c32c2e81a763056909eb94814bb8e13eb7a875d73de6f22fd7b33c364468&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

启动类就是我们启动 eureka server 也就是我们注册中心的地方，它和普通的 spring boot 应用启动闷方法的方式是一致的，但是需要加一些额外的注解。最后一步当然就是运行起这个闷方法，我们 start 走起，看一看项目的效果。为了加深同学们的理解，我这里不采用自动化的组件或者插件自动生成 pump 而是采用手打我们自己来创建手工 pom 文件。这样同学们能清楚地了解到都有哪些 dependency 需要加入每一个梅文， dependency 都是什么含义，起到什么作用。



OK 话不多说，我们抄起家伙准备开拔这里已经创建好了一个项目叫 spring cloud demo 因为在 intelligj 里面创建一个项目非常简单，我这里就不浪费时间给大家 demo 这一个步骤了。下面我们先来在这个顶层的 palm 中定义一些节点。


那第一个节点是什么？ Dependency management. 大家知道 dependency management 和 dependency 有什么区别吗？ dependency management 并不是真实的引入一个dependency ，而是把这个依赖包的 version 给它管理起来。这样的话，我们在此项目当中如果用到对应的 dependency 不用指定 version 它会直接从父类项目或者当前项目 pump 文件当中的 dependency management 里面读取version。


Ok.第一个 dependency 大家知道是什么吗？当然是我们的 spring cloud 了对不对？它的 version 是 oig spend framework.cloudok 那它的 artifact 是什么？ spring cloud dependencies 大家看它不叫 dependency 而叫 dependencies 说明他这里面加了很多很多的依赖。接下来我们给他指定一个 version 我们开发人员都是喜新厌旧的。对不对？所以我这里选用了 2019 年 spring cloud 出品的最新的 greenwich sr one 版本。 OK 在定义好这几步知识后，我们还要指定一个 type 指引入 pon 并且它的 in scope 是 import 级别，这样的话我们的 spring cloud 就已经引入完成了。接下来我们引入第二个 dependency 这个 dependency 是什么？ spring boot 对不对？ how the group ID 依然是 spring framework boot 然后 artifact ID 呢，spring boot starter parent 这 version 它已经自动提示出来了。


no no no 这个 version 太老了，我们年轻人当然要用最新的了二点一点五 release 版本。同样的它的 scope 还有 type 我们从上面 copy 过来。 OK 那我们定义完了这两个 dependency management 之后，我们再把 lombbook 引入进来。


在前面的应用中，大家应该已经了解了 long book 的功能了，它是一个非常小小的插件，但是能帮你自动生成一部分代码，让你的代码变得非常的整洁。它的 group ID 是 orgdn projectloan book artifact 就是 loan book version ，大家可以选择更新的版本，我这边就引用了一个1.18，因为我用这个版本相对来说比较顺手了。


好，定义完了这两项之后，大家觉得还缺什么吗？还缺一个 build 对不对？没错，那我们在 build 里面，要把没问的 plugin 给它加进来，定义 group ID orgi patch Maven plugin 下面是它的 artifact ID Maven compiler plugging OK 那它的 version 大家引入 version 的时候，如果你不习惯这样直接写 version 也可以把 version 定义在 property 里面，然后通过画括号在这里引用进来。两种方式都可以看个人喜好。那这里我直接把这 version 定义在这个节点下，三点六点零定义好 version 之后，我们还要给它定义一些配置项行为 configuration 节点。这里我要指定一些 gdk 的版本以及运行期版本，它有两个标签，一个是 source 一个是 target 这两个版本我都指定成1.8。这样一来大家把这个 palm 加入到自己的开发环境当中，就不需要再翻来覆去的改各种版本，也不会爆出版本不一致的错误来了。


OK ，我们顺手再把 encoding 指定到 UTF 杠8，这样一来，整个 palm 就定义完成了。同学们可能有一点疑问，通常来说，我们之前的项目不是直接继承自 spring boost doctor parent 这个项目吗？没错，也可以这样做。但是实际上，在大型互联网公司的一些企业级应用中，我们很少直接去继承自一个开源项目的泡沫依赖。通常来说，我们会把它作为一个 dependency 项加入到 dependency management 节点中，这样配置起来更加灵活。


OK 在进入下一个章节之前，我来带大伙一起去跟 spring cloud 打一个亲切的照面。我们点进 spring cloud dependency 这个项目，看看里面都有什么内容。哇密密麻麻的版本，大家看这些都是什么，好像都是 spring cloud 的组件是不是 bus config 还有 gateway 我们在后面的章节将对这些组件进行系统的学习。


那在这里大家知道为什么把这个项目作为 dependency management 加入进来吗？因为我们在子项目中如果引用了相同的 dependency 的话，其实是不用指定 version 的。那这个 version 从哪里获取呢？没错，就是从我们引入的这个 spring cloud dependency 文件当中获取到正确的 versionok 那现在返回到顶层的 pump 文件。


接下来我们就带大家创建一个子 module 这个 module 的名字就叫 spring eureka 也就是注册中心，说干就干。打开菜单，选中顶层项目，弹开弹窗，新建一个 directory 也就是目录。这个目录我们给它起名叫 eureka 后续的 demo 我们都会放到这个文件夹当中，这样方便大家管理查看。
创建好之后，再次点击顶层项目，选择新建一个 module 还是使用 Maven 类型，在 artifact ID 上面给它起名叫 eureka server 把这个复制一下，后面会有用的点击 next 这里 module name 我们跟前面的 artifact ID 保持一致。


eurika 横杠 server 至于文件的内容存放的目录，刚才大家不是创建了一个有瑞卡的文件夹，对吧，那我们这里就把它写上。好勒，点击 finish 那我们倒数三个数 32 出来的有点快好，开发工具已经创建好了紫毛球的泡沫文件，它的 parent 指向刚才大家一起创建的外层的顶层泡沫文件。 OK 那接下来我们就把需要的依赖添加进这个子 module 的 pump 文件当中。


第一步我们先来定义打包类型。那这里的 packaging 我们选择类型是 job 不同于它的负例 palm 负例 palm 里面这个 packaging 类型是 palm 类型我们这里是这样类型。接下来声明 eureka 的 dependency group ID 同样是 orig.spring framework in cloud 那 artifact ID 会稍微有那么点长，它是 spring clock doctor Netflix 公司。 eureka 是 Netflix 公司出品的组件，所以它也被包含在了 spring cloud Netflix 组件库当中。这里会看到 artifactor 里面有个 Netflix 公司的名字。


OK 还没完，后面是 eurika 杠 server 那这里是不是还要定义 version 呢？其实没必要，那它从哪里获取 version 大家还记得吗？在它的顶层泡沫中，我们引入到 dependency management 节点下的 spring cloud dependency 项目中读取正确的 version 对不对？ OK 接下来就去创建一个有瑞卡 server 的启动类。我们点开菜单找到当前的应用，在 Java 这个文件夹下新建一个 package 一切从简。以后大家的 demo 都使用 com.imock.spring cloud 作为路径。好创建好文件夹之后再来创建一个 Java class 加油。 class 的名字就叫 eureka server application。创建完了，收起弹窗在这个 server 里面我们要做什么？给它加一个嫩函数，是不是实际上启动一个 spring cloud 应用和启动一个 spring boot 它方式是一样的，都是通过 main 方法。那接下来我们要跟它加几个注解了。


第一个注解就是 sprint boot 那大家应该相当熟悉啦，来 sprint boot application 好。第二个注解可能大家之前没有用过它跟 eurika 有关是什么？ Enable eurika server. 那加上这个注解以后，这个 eurika server application 启动类就会被识别为一个 eurika 的注册中心。接下来就要给这个启动类添加一个启动方法。


怎么做呢？我们来 new 一个 spring application builder 通过 spring application builder 去构造一个启动类。在 builder 里面的第一个参数，我们把当前类的名字给它传进去，调用点 class 传入一个 class 名字。第二个方法，我们要定义它的启动方式，那当然是 web 了，对不对？那 web 里面的参数是 web application type application type 中的 serve let 形式。


好。那第三个最后一个参数，我们调用 run 方法把参数传进去之后一个分号结束。好，到此为止整个入口函数就已经编写完成了，那有人卡就可以启动了吗？我们还需要去添加一些配置文件。打开菜单栏，我们将目光聚焦到 resources 文件夹。在这里。创建一个文件叫什么名字 application properties 对不对？那大家如果对 problems 这种 K value 形式的配置方式，觉得不如 YAML 格式直观的话也可以创建 application.yaml 它们起到的效果其实是一样的，只不过可能加载顺序会有一些不同。


OK 我们这里先第一个属性叫什么？自报家门对不对？我要告诉别人我这个 application 叫什么名字 [spring.application.name](http://spring.application.name/) 那我的名字就叫 eureka 杠 server 那第二个参数啦是端口，如果不指定端口，这个应用将会以 80 默认的端口来启动。那大家知道很多中间件或者其他应用也有可能占用这个端口对不对？所以我们干脆给它移到一个谁也不会用的端口。 2 万。好了，还像打麻将一样对吧，两万三万糊了。接下来三个参数就跟 eureka 自己相关了。


第一个参数， eureka instance host name 那它的值是什么？ Local host. 那因为我们是本地测试，大家在使用 local host 的时候，要记得把本地的 host 文件。如果你是 Mac 系统，把 host 文件中的 local host 绑定到 12 七零点零点幺好。


第二个参数 eureka client register with the eureka 这是什么意思？这是服务注册的意思，是否发起服务注册？那我作为一个注册中心来说，那只有别人到我这里注册，哪有我去注册自己的道理是吧。所以这里先把它暂行关闭。第三个参数是什么？也跟服务注册和服务拉取有点关系。
Eureka client fetch registry.


那这是什么意思啊？它的意思是说我是否去拉取服务注册表？我作为服务中心是吧？注册中心本身它就是保有一个服务注册列表，所以也没必要去拉取了。那定义了这五个属性以后，我们就可以去尝试着启动慢方法，看能不能把 eureka 注册中心成功启动起来。打开菜单栏，大家转移到刚才创建的慢方法里，我们就直接跑这个慢放法，右键直接 run 弹出一个窗口，大家静候佳音。这里看到一开始就打出了一个 spring 的大标签，大家下次看到这个大标签，心里一定要默念一下，成功了一半。这就像小时候我们飞纸飞机，要一口气，这样会飞得更远，是一个心理暗示，可以给你带来好运。


OK 我们往下翻，看到最后一行 log 是什么 started 那它的意思就是 urea 注册中心已经成功启动了。接下来就打开浏览器，看一下注册中心长什么样子。切换到浏览器打开一个空白页面 shoe local host 端口，就是刚才定义的 2 万回撤。好勒。看到这个页面大家就知道我们的服务注册中心已经成功开启了。在接下来一小节，我将带大家去阅读注册中心中的信息，让大家知道每一块 section 究竟包含了哪一个维度的信息，它们都有什么业务含义。




