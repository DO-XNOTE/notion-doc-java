---
title: 1-10 【demo】动态拉取参数
---

# 1-10 【demo】动态拉取参数

[image](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/12667d86-711d-4cc1-b9a8-941d95438eea/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666AFIKAST%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T225709Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCAKV0RaMbQ11Do4K%2BqFtQJp9956Fu596KhFPItCZ4wkwIhAIL9iQgl26w5qP6U7b16RcfxKxV9%2BW53kg4tz9DvxrGTKogECMb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgyEhg195pRpsBEz%2B%2F0q3ANqJnyF8wgZsSp6jHpfeUTqqu32AjP%2BZ9Nb40JWrg3Fc8xCcZBrdeyVkE3L9xcCRr4Ng%2BfcNO2qTsO1nCknwITfdbXLZFxknQ5CJ%2FZ7gtRj79GfvFOhYtPaCSIsUhHRweJFF%2FmsFX8AzVwEFrrJ%2B8WVauUgU11XwFcGhX%2FAlaiASAX2sdQfqyel7VSaeoTe1Iz1Al0d6vdc8LsOJcl73mYMNdXAMl8zafADy1%2BnBZMPJGCU4YxLAYymcyTyOUFiUhJTOOpQ3MavjBcRfC2OXFVMfLqfDPoUpD1jpEUaRy4nevstx7pl2lMrZ2FBLOvHE2S5aiSL4bcClt3AUXtt%2FNvhjdAAVWMpKZHXXRORE6og86RmXW1W3JsZxeKlt%2B9DwSKf1%2Fsc1BwcI33BVg69iFFO5gYizdwXH3loLlbhguX4eHiS569U05h9py2%2BipNRTiChCWW14qT319BKUFhQIlj5LqtgiEliUx12ZvptNFBsoIe0y7j8EK4Mqx8VxasKdJl7EhHpu3Fl1zx9o3s%2BkC3Poyrne2WUudDO3WkI1HCzCrfhjReijDGMV85fav6vAKXErFES37i3pbpU7QlLE%2BNtL%2FrOxTjVXH9%2F7CHkuVcp4dXBlrIlxC3H3mbsQDDbt%2F%2FSBjqkAUHpKEZ%2BPhwKe%2FNTmdsWUdxwRxtjkoYLiaTAoXNMuQYA03vYLyisI7UsL7DUQd%2FrketadlBYGBZVhn4%2BY8M37B0EJMxHf%2BqfzHIDzBuZYhon0H2Su7dPauUBU1QfroYzVINhHHA5wW81n1%2FoQC0lmJefZujnGOoDzwsb2Mk%2BF7geoAmayvF3gY%2Fj1jjFBYR6eT8fCodv4YUVkbZ5OAVSET5ycncZ&X-Amz-Signature=15a344f0780148f1b610adde3d4d724fca849fb9f176815134c7bea213937bab&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

[image](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/1788ce87-9685-41e8-8a98-9d00551c4198/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666AFIKAST%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T225709Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCAKV0RaMbQ11Do4K%2BqFtQJp9956Fu596KhFPItCZ4wkwIhAIL9iQgl26w5qP6U7b16RcfxKxV9%2BW53kg4tz9DvxrGTKogECMb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgyEhg195pRpsBEz%2B%2F0q3ANqJnyF8wgZsSp6jHpfeUTqqu32AjP%2BZ9Nb40JWrg3Fc8xCcZBrdeyVkE3L9xcCRr4Ng%2BfcNO2qTsO1nCknwITfdbXLZFxknQ5CJ%2FZ7gtRj79GfvFOhYtPaCSIsUhHRweJFF%2FmsFX8AzVwEFrrJ%2B8WVauUgU11XwFcGhX%2FAlaiASAX2sdQfqyel7VSaeoTe1Iz1Al0d6vdc8LsOJcl73mYMNdXAMl8zafADy1%2BnBZMPJGCU4YxLAYymcyTyOUFiUhJTOOpQ3MavjBcRfC2OXFVMfLqfDPoUpD1jpEUaRy4nevstx7pl2lMrZ2FBLOvHE2S5aiSL4bcClt3AUXtt%2FNvhjdAAVWMpKZHXXRORE6og86RmXW1W3JsZxeKlt%2B9DwSKf1%2Fsc1BwcI33BVg69iFFO5gYizdwXH3loLlbhguX4eHiS569U05h9py2%2BipNRTiChCWW14qT319BKUFhQIlj5LqtgiEliUx12ZvptNFBsoIe0y7j8EK4Mqx8VxasKdJl7EhHpu3Fl1zx9o3s%2BkC3Poyrne2WUudDO3WkI1HCzCrfhjReijDGMV85fav6vAKXErFES37i3pbpU7QlLE%2BNtL%2FrOxTjVXH9%2F7CHkuVcp4dXBlrIlxC3H3mbsQDDbt%2F%2FSBjqkAUHpKEZ%2BPhwKe%2FNTmdsWUdxwRxtjkoYLiaTAoXNMuQYA03vYLyisI7UsL7DUQd%2FrketadlBYGBZVhn4%2BY8M37B0EJMxHf%2BqfzHIDzBuZYhon0H2Su7dPauUBU1QfroYzVINhHHA5wW81n1%2FoQC0lmJefZujnGOoDzwsb2Mk%2BF7geoAmayvF3gY%2Fj1jjFBYR6eT8fCodv4YUVkbZ5OAVSET5ycncZ&X-Amz-Signature=df0c29062a9c2407ba1461be08dcc2e4045d65648e59d4cb759a62df2dce0e30&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

[image](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/0c5f135b-c2a0-49d3-ae1e-cfbe82f0598a/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666AFIKAST%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T225709Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCAKV0RaMbQ11Do4K%2BqFtQJp9956Fu596KhFPItCZ4wkwIhAIL9iQgl26w5qP6U7b16RcfxKxV9%2BW53kg4tz9DvxrGTKogECMb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgyEhg195pRpsBEz%2B%2F0q3ANqJnyF8wgZsSp6jHpfeUTqqu32AjP%2BZ9Nb40JWrg3Fc8xCcZBrdeyVkE3L9xcCRr4Ng%2BfcNO2qTsO1nCknwITfdbXLZFxknQ5CJ%2FZ7gtRj79GfvFOhYtPaCSIsUhHRweJFF%2FmsFX8AzVwEFrrJ%2B8WVauUgU11XwFcGhX%2FAlaiASAX2sdQfqyel7VSaeoTe1Iz1Al0d6vdc8LsOJcl73mYMNdXAMl8zafADy1%2BnBZMPJGCU4YxLAYymcyTyOUFiUhJTOOpQ3MavjBcRfC2OXFVMfLqfDPoUpD1jpEUaRy4nevstx7pl2lMrZ2FBLOvHE2S5aiSL4bcClt3AUXtt%2FNvhjdAAVWMpKZHXXRORE6og86RmXW1W3JsZxeKlt%2B9DwSKf1%2Fsc1BwcI33BVg69iFFO5gYizdwXH3loLlbhguX4eHiS569U05h9py2%2BipNRTiChCWW14qT319BKUFhQIlj5LqtgiEliUx12ZvptNFBsoIe0y7j8EK4Mqx8VxasKdJl7EhHpu3Fl1zx9o3s%2BkC3Poyrne2WUudDO3WkI1HCzCrfhjReijDGMV85fav6vAKXErFES37i3pbpU7QlLE%2BNtL%2FrOxTjVXH9%2F7CHkuVcp4dXBlrIlxC3H3mbsQDDbt%2F%2FSBjqkAUHpKEZ%2BPhwKe%2FNTmdsWUdxwRxtjkoYLiaTAoXNMuQYA03vYLyisI7UsL7DUQd%2FrketadlBYGBZVhn4%2BY8M37B0EJMxHf%2BqfzHIDzBuZYhon0H2Su7dPauUBU1QfroYzVINhHHA5wW81n1%2FoQC0lmJefZujnGOoDzwsb2Mk%2BF7geoAmayvF3gY%2Fj1jjFBYR6eT8fCodv4YUVkbZ5OAVSET5ycncZ&X-Amz-Signature=9c0abb814b3e27044b27c429b3c799f4635e6619e4432674e9798a11a743eb5d&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

慕课网的各位同学们大家好，近些年互联网行业有一个词出现的频率特别高，它叫拥抱变化。什么意思呢？就是说咱现在这个快速发展的节奏里，唯一不变的就是变化了。那作为适应快速迭代、快速开发的微服务架构来说，我们的配置管理也要拥抱变化才行。那具体怎么来拥抱变化呢？这一节我就带大家去了解一下如何通过配置中心拉取动态变化的属性文件。


这一节的内容主要分为两个部分。第一部分，首先我们需要引入一个特殊的依赖，这个特殊依赖不是新朋友，是大家以前用过的老朋友了，待会儿带大家去叙叙旧。第二部分就是对咱现有的 config client 项目做一番改造，让里面的服务可以去拉取动态变化的参数。 OK 这一节的内容其实非常简单，代码量也很少，大家准备好的话轻装上阵。 intelligj 走起编程使我快乐。


996 是我的福报，那享受福报的第一步就是先从 palm 文件开始。咱前面说到要添加一个特殊的

 dependency 他是咱的老朋友，大家能猜到他是谁吗？好，我一边打一边来揭晓，这个 dependency 的 group ID 是 org spring framework.boot 朋友们是不是已经猜到了，没猜到的同学继续往下听谜题，这个 dependency 曾经用在 high strikes 项目中，并且我们通过它集成了 turbine 利用它暴露出来的某些服务接口做了什么事情？大家还记得吗？那暴露服务接口的是哪一个组件呢？我们继续往下，同学们应该猜出来了吧，还没猜出来，那我只好揭晓答案了。
Activator. 我们这一节配置中心就要利用 activator 暴露出来的接口更改服务属性，具体怎么做？我们接下来往后看。 OK 这里咱 


dependency 都已经加好了，接下来走到 controller 层里面，咱这里已经有一个 controller 了对不对？我这里再给它添加一个新的 controller 叫什么名字呢？这里是说有动态刷新的功能集成进来。所以咱新的 controller 起名叫 refresh controller 这名字怎么起得不伦不类的，只要是被国外的同事看到，就要说我这个名字起得不规范了。有的公司有 code review 机制就是互相会检查你的代码。很多老外同事他水平不高，他就检查语法错误，很在行，会说你这个名字不对，不要叫 refresh controller 不够明显你应该叫 controller that could refresh a property holy shit 在我们中国人眼里，名字起的要言简意赅，只可意会不可言传。


对不对？我这里代码写到哪了？写到了 rest controller 好，添加完 rest controller 以后，咱在这里要添加一个属性了，这个属性依然要把它注入进来。属性叫什么呢？我们给它起名叫 words 那 words 就直接从配置文件当中的 words 里面读取好。我们注入 words 以后，那接下来写一个 public 的 get 方法，把这个 words 给它返回回去。 get words 返回回去之后，我们要把它的 get mapping 也给指定上，用最简单的方式。好了，就指定一个words。


Okay. 那咱新添加的这个 controller 在访问路径上是不是也要跟已有的这个 controller 做一个区分呢？没错，所以咱在这里要给它添加一个 request mapping 给大家加一个访问的前缀是谁？就叫 refresh 好了，当我们访问 refresh 路径下的 words 服务的时候，它就会返回当前配置文件中的 words 属性，到这里就结束了吗？还没我这里要添加一个非常关键的属性了。
新属性来认识新同学了，他叫 refresh scope。 Okay. 那这半路杀出的 refresh scope 它有什么作用？我们不妨点进去看一下。我们看这个类上面的注释实际上已经把它的作用还有它的底层原理说得非常非常明白了。它说 bin 如果被这个类给注解上了，那么它可以在运行期进行刷新。然后所有的其它 components 只要是用到了这个bin ，那么都会在下一个方法调用的时候会获得一个 new instance 那它后面还对这个 new instance 做了个解释，fully initialized and injected with all dependencies 你所有的上下游的依赖，它会完全的进行初始化，还有重新注入是不是有种黑魔法的感觉，这个注解可以怎么样？开天辟地，从此创建一个新的 component 然后注入到所有的上下游的 dependency 当中。


OK 那我们接下来把这个注解加上以后，咱还要去配置文件中动一番手脚。好咱的配置文件是 bootstrap.yaml 点进去。那咱这里动什么手脚呢？它跟 activator 有关，我们要把 activator 的端口相应的给它开放出来。好，第一个节点是 management 冒号，然后另起一行，咱先要把它的 security 给它关闭，security link 一行 enabled false 接下来要开放所有的端口，那这个节点和 security 是属于平级的，它叫 end points 大家要记着后面这个 S 不要漏了。

```java
spring:
  application:
    name: config-client
  cloud:
    config:
      name: config-consumer  # 它能覆盖掉你 application name 中声明的这个名称。那我们这里给它起名叫 config consumer
      uri: http://localhost:60000
      profile: prod
      label: master


server:
  port: 61000


myWords: ${words}  # words 是github上的属性
management:
  security:
    enabled: false
  endpoints:
    web:
      exposure:
        include: "*"
  endpoint:
    health:
      show-details: always
```


endpoints 下面是跟着 web exposure 好， exposure 下面是 include 然后它这是一个通配符，所有接口全部开放。不过在这里如果这样写会启动报错的。所以我们要对这个星号在 YAML 文件中加一个括号给它管起来。好，这样就 OK 了。那接下来我们再配置一个节点，它叫 end point 那跟前面一个节点比少了一个 S 这里很多同学会把它配置成一个节点，那这样的话是起不到效果的。大家要注意这是两个不同的节点 and points 下面另起一行跟谁跟 health health 接着下面是 show details detailsokay 那它的值可不是 true or false 啦，这里是 always 如果写 true or false ，启动还是会有问题的。到这里，配置文件也 OK 了，所有的改动都已经是万事俱备，可以尝试着启动项目了。我们首先把 config server 项目给它跑起来，跑起 config server 以后，咱再去把 config client 也同样的跑起来。稍等片刻，看到 spring 成功一半，正在努力拉取配置，好配置也已经拉取到了。


OK 接下来我们转战 postman 开始做测试喽。打开 postman 我们调用谁呢？ local host 61,000，并且它的路径是 refresh 再打一个杠 words 那我们先来看看这一个 URL 会返回什么内容呢？ OK 那我们看到这里，它返回了一个 god bless you 是正确的结果。对不对？好，那接下来我们尝试的在 github 上面把这个属性改掉。


OK 我们走到浏览器中，咱前面读取的是哪一个文件，是不是这个 config consumer gun product 我们打开这个文件。有的同学们在本地访问 github 会感觉到非常非常慢，因为毕竟 github 是境外服务器，我们也可以用一些国内的 github 的托管网站，或者咱可以用代理，这样的话你访问 github 会快很多。


好，那咱这里把这个文件进入。好编辑模式中，这个 words 我们把它更改一下，看它能不能获取到刷新后的内容。把它从 god bless you 改成 god bless you and meok 滑到页面最下方直接提交到 master branch 我们直接提交。好，提交成功，它的 words 已经被改掉了，我们接下来再回到 postman 中再尝试调用一把，看看会不会有奇迹发生。就要，奇迹果然没有那么容易发生。我们明明改了配置文件，它为什么没有动态刷新啊？我觉得此处事有蹊跷。元芳同学你怎么看？咱前面的 pump 文件中是不是加了一个 accurator 的 dependency 可是到现在为止都没用过。那我想这就是关键所在了，我们要借着 accurator 暴露出来的一个 endpoint 也就是服务的接口触发这个主动刷新的操作。


OK 那在触发之前，咱先回到 intelligi 里面做两件事儿，分别什么？分别是清空 config client log 以及清空 config server 的 log 因为待会儿咱要回来观察 log 通过 log 咱就可以看到触发了 actuator 的刷新接口以后，这两个小应用都在背后搞了什么事情。
好，那咱回到 postman 里，首先咱应该把这个请求发到哪里，是发到 config server 还是 config client 咱要更改的是 config client 里面的参数对不对？所以这个 refresh 请求应该是发向端口号为 61,000 的 config client 接下来它后面的路径我们要打上 accurator 再加上一个斜杠 refreshok 这个操作会导致属性的变更。因此按照 rest 接口的规范，它应该是一个 post 形式的接口。


好，那我这里要点击发送了三二一走，你稍等片刻。 OK 我们这里可以看到它返回的类型是什么。大家注意，这个 words 实际上你在配置文件中假设配置了 100 个属性，如果其中变化的只有一个，那么当你发送 activator refresh 接口调用以后，它这里只会列出你所变动过的那个属性。比如说在我们的配置文件当中，我们有一个 name 和一个 words 属性，但是其中只有 words 发生了变化。所以我们发送完请求以后，在这个列表中只看到了 wordsok 那我们接下来回到 intelligi 中看一看 log 有什么变化，我们先来看 config client 的 log 好，这里往下找。
在这一行，它这里已经触发了从 config server 中拉取文件的一个步骤。那么这里可以看到它的 words 已经变成了 god bless you and me 说明这是什么，这是拉取到的最新的文件。对不对？话说，这一步必须借助 config server 老大哥的帮助才可以获取到最新文件。那想必在 config server 这边也发生了什么事，你看这里有 log 打印出来了。 OK 我们把它放大。好，看到这里它触发了一次新的拉取操作。什么 adding property source 那它这里又重新添加了一个本地文件。那这个本地文件代表什么含义啊？代表着它从远端的 github 服务器上获取了最新的属性列表，并且保存到了一份新的本地文件当中。


照理说，如果一帆风顺的话，那我们的 config client 应该已经获取到了最新的 property 那我们尝试再调用一次 config client 的 controller 看一看是不是可以返回最新的结果。 OK 我们把后面的路径改成 refresh 斜杠 words 然后把 post 类型改成 getokay 我们就要发送了。三二一走。同学们看到这个属性已经发生了变化。对不对？它从 god bless you 变成了 god bless you and me。 Ok. 那么到这里，本节的内容就快要结束了，我这里跟大家总结一下，我们在这一节中学习了如何配置一个可供动态刷新的属性。那么它有这样几个改动的地方，第一步，要把 Actuator 的依赖注入到 pom 文件当中。然后大家要记住在 properties 文件里或者是在 YAML 文件里把 activator 的服务端口也就是 endpoints 依次打开。


如果大家漏掉了这一步，当你尝试调用 activator refresh 方法的时候，你会获得一个错误，**它会告诉你说方法不存在，实际上是不是存在的，只是我们没有暴露出来而已。对不对？** OK 那当你把这个都已经配置妥当以后，我们要把 refresh scope 这一个注解添加到咱的 controller 里。那我们说复唱复随，你的这个动态属性添加到哪个类里面？ the refresh scope 这顶大帽子就要扣在哪个类上面。这一切准备妥当以后，当你把 github 中文件的内容更改了以后，我们还要触发 accurator 的 refresh 方法来让你的 client 端从 config server 处重新拉取最新的文件。


实际上这是一个两方联动的操作，client尝试从 server 上拉取属性。那么 server 同样的也要去 github 上拉取属性，并且把这个变动过的属性文件存在本地。 OK 那这一节的内容到这里就结束了，我们在下一节当中将要探讨一下如何对 config server 进行高可用的改造。那同学，我们下一节再见。



