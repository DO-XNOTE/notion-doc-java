---
title: 1-6 【demo】搭建配置中心 Config-Server
---

# 1-6 【demo】搭建配置中心 Config-Server

[image](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/6b65b2ae-ebbe-4e72-bbcb-dd7544437587/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YNCKXZLB%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T225706Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCYkxKMk2LaJ2FIDBE1YSYTxDga%2FcTf4kW%2BPXPxZZ3EgQIgdBVv4F%2BA87eovQHrQ5UX%2BfG8zpNsf%2BTQytllBobdSTcqiAQIxv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDPr7yNvacHHsYQgQ7CrcA0QAQwAPgLcvFsE3tCyH2u1TMxy%2FNyp8lI7vQdKNU%2FuEwbWykSbFTkK%2FrxAMiS45njNsuxBdNLehC1FmTxiaNKlDPKlKePd2GU3XGbZA5r3ouHdAroWK%2FYgovb3%2B%2Bujw4F7fUUPcSMwjwYW84ASXfQwpByuwH9QiV2Tb6AZycJe%2BiKVhzr4QFzboUmk7jCAsExPNO6F88y5Ekp6WIpkyigU9aObt%2BPgiggEXcQf%2BYw32rPBc5rycL%2BVsnprnsxlW6jPdGxuuFc7vvJAty2JGBTDeWennCYqk4y4PooByCZKFWuG%2FjiBAiIi4PRCjuiWc5syfAFHC583j6LNsMqAc%2BlvNZUOpn%2FJcvlMwOdv4Qb3Y28b8nHcV7nJPn4GnIgW91loNp0thI6u1%2FgG%2BsdgyKF6TgFmkyvGN%2FdhrBAy61d2C89xLqLPQHCUOB8OVktQwQBX2hW1Gygxdfsk%2BQbR94E1O0u%2FFjgzVuQgQxrzyoUomrhVDIx3Gtuuc3keTpSzXAJwUMJBj8t7IjgznVPPbmqA58BZTyjXC4221yEpOwj0r8EaCUCttK5MCoIyIjw8R0v7NulBIPd0Ya8qRy8A%2F19PcAq3imX4bKh9jM%2BMBWJj1JQ4OSbdlCJjujwFcML%2B7%2F9IGOqUBnkTb0R5eIJ3eyFYrtw0TH%2BEGr9fts1yjvGYp6EaCbT86LZIOXJeJq9Lg1EMsc0XBnaPF0r3Jn4v52z6XA%2BQTy3BBawmHcLT2ZKJMBuGD1dyayV3b%2BT82Urmuvc%2F8YOqon7SSy19yYYTM1FhfWskRMX6BHdvfSkj3mOdX%2F4UDk9kuIjAp2YySUFgZ%2Fps0el4t8RmRg8dmbUj9MELYKMfk0tR9yxW6&X-Amz-Signature=98bf1b669563c5d90aab882ef91ef6d4db89ea68553d43aee69ced14c84c89b4&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

[image](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/7f81086a-52ae-4813-9185-c6a070648b00/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YNCKXZLB%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T225706Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCYkxKMk2LaJ2FIDBE1YSYTxDga%2FcTf4kW%2BPXPxZZ3EgQIgdBVv4F%2BA87eovQHrQ5UX%2BfG8zpNsf%2BTQytllBobdSTcqiAQIxv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDPr7yNvacHHsYQgQ7CrcA0QAQwAPgLcvFsE3tCyH2u1TMxy%2FNyp8lI7vQdKNU%2FuEwbWykSbFTkK%2FrxAMiS45njNsuxBdNLehC1FmTxiaNKlDPKlKePd2GU3XGbZA5r3ouHdAroWK%2FYgovb3%2B%2Bujw4F7fUUPcSMwjwYW84ASXfQwpByuwH9QiV2Tb6AZycJe%2BiKVhzr4QFzboUmk7jCAsExPNO6F88y5Ekp6WIpkyigU9aObt%2BPgiggEXcQf%2BYw32rPBc5rycL%2BVsnprnsxlW6jPdGxuuFc7vvJAty2JGBTDeWennCYqk4y4PooByCZKFWuG%2FjiBAiIi4PRCjuiWc5syfAFHC583j6LNsMqAc%2BlvNZUOpn%2FJcvlMwOdv4Qb3Y28b8nHcV7nJPn4GnIgW91loNp0thI6u1%2FgG%2BsdgyKF6TgFmkyvGN%2FdhrBAy61d2C89xLqLPQHCUOB8OVktQwQBX2hW1Gygxdfsk%2BQbR94E1O0u%2FFjgzVuQgQxrzyoUomrhVDIx3Gtuuc3keTpSzXAJwUMJBj8t7IjgznVPPbmqA58BZTyjXC4221yEpOwj0r8EaCUCttK5MCoIyIjw8R0v7NulBIPd0Ya8qRy8A%2F19PcAq3imX4bKh9jM%2BMBWJj1JQ4OSbdlCJjujwFcML%2B7%2F9IGOqUBnkTb0R5eIJ3eyFYrtw0TH%2BEGr9fts1yjvGYp6EaCbT86LZIOXJeJq9Lg1EMsc0XBnaPF0r3Jn4v52z6XA%2BQTy3BBawmHcLT2ZKJMBuGD1dyayV3b%2BT82Urmuvc%2F8YOqon7SSy19yYYTM1FhfWskRMX6BHdvfSkj3mOdX%2F4UDk9kuIjAp2YySUFgZ%2Fps0el4t8RmRg8dmbUj9MELYKMfk0tR9yxW6&X-Amz-Signature=8db86ccc9fa4342a9c48f97e283b4b0bea9bbdbdad74027bf19c7ceb5bbc4999&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

[image](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/9236ff57-405d-4cbe-85ae-d50f0dc0c4b6/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YNCKXZLB%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T225706Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCYkxKMk2LaJ2FIDBE1YSYTxDga%2FcTf4kW%2BPXPxZZ3EgQIgdBVv4F%2BA87eovQHrQ5UX%2BfG8zpNsf%2BTQytllBobdSTcqiAQIxv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDPr7yNvacHHsYQgQ7CrcA0QAQwAPgLcvFsE3tCyH2u1TMxy%2FNyp8lI7vQdKNU%2FuEwbWykSbFTkK%2FrxAMiS45njNsuxBdNLehC1FmTxiaNKlDPKlKePd2GU3XGbZA5r3ouHdAroWK%2FYgovb3%2B%2Bujw4F7fUUPcSMwjwYW84ASXfQwpByuwH9QiV2Tb6AZycJe%2BiKVhzr4QFzboUmk7jCAsExPNO6F88y5Ekp6WIpkyigU9aObt%2BPgiggEXcQf%2BYw32rPBc5rycL%2BVsnprnsxlW6jPdGxuuFc7vvJAty2JGBTDeWennCYqk4y4PooByCZKFWuG%2FjiBAiIi4PRCjuiWc5syfAFHC583j6LNsMqAc%2BlvNZUOpn%2FJcvlMwOdv4Qb3Y28b8nHcV7nJPn4GnIgW91loNp0thI6u1%2FgG%2BsdgyKF6TgFmkyvGN%2FdhrBAy61d2C89xLqLPQHCUOB8OVktQwQBX2hW1Gygxdfsk%2BQbR94E1O0u%2FFjgzVuQgQxrzyoUomrhVDIx3Gtuuc3keTpSzXAJwUMJBj8t7IjgznVPPbmqA58BZTyjXC4221yEpOwj0r8EaCUCttK5MCoIyIjw8R0v7NulBIPd0Ya8qRy8A%2F19PcAq3imX4bKh9jM%2BMBWJj1JQ4OSbdlCJjujwFcML%2B7%2F9IGOqUBnkTb0R5eIJ3eyFYrtw0TH%2BEGr9fts1yjvGYp6EaCbT86LZIOXJeJq9Lg1EMsc0XBnaPF0r3Jn4v52z6XA%2BQTy3BBawmHcLT2ZKJMBuGD1dyayV3b%2BT82Urmuvc%2F8YOqon7SSy19yYYTM1FhfWskRMX6BHdvfSkj3mOdX%2F4UDk9kuIjAp2YySUFgZ%2Fps0el4t8RmRg8dmbUj9MELYKMfk0tR9yxW6&X-Amz-Signature=f68cd0b09c5aa4cb6061616ddfbf59f928a4ab8e36f37d5f046cb965fad4b50c&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

慕课网的各位同学们，大家好，前面一节我们创建了 git Repo 也配置了属性的文件，一切都已准备妥当。接下来我带大家一起搭建一个 config server 尝试着从注册中心拉取文件，看能不能获取正确的结果。本节的主要内容主要有三点，第一点，创建一个 config server 的 module 然后引入必要的依赖项，这一步和前面的 demo 章节都大同小异了。


那接下来的一步就是添加参数和启动类，这里我打算稍微引入一点变化，咱以前都是用的 application properties 配置参数。那像我这种上了年纪的技术人就喜欢用 properties 年轻人都会用什么？ YAML 对不对？所以我们这一节也尝试改用 YAML 配置项目的启动文件，最后一步就是把这个项目启动起来，然后发送 get 请求拉取配置文件。这里的 get 请求也不是乱给的，咱也要顺应 github 上配置文件的生辰 8 字，和它对应起来才能拿得到数据。


好同学们，接下来我们转战 intelligi 开工新章节的第一个 demo 咋喊出口号？每天扣订 1 小时，健康工作 50 年，我们马上就要开启 config 的打怪升级之路了。我现在在干什么呢？给 config 创建一个父类的目录。创建完以后，咱的所有项目都会添加到这个 config 目录下面了。 OK 那我们现在创建第一个 module 一个没问 module 它的 artifact 就给它起名叫 config gun server 把它复制一下，点击下一步。在这个 module name 上保持跟前面一致，同时文件路径写成 config 杠。 ok321 出。好嘞，咱这一张的配置非常非常简单。 dependency 就是一个光杆司令，我们来看是哪个光杆司令添加一个 dependencies 添加唯一的一个 dependency 它的 group ID 是 org spring framework in cloud artifact 就跟我们的 config 有关。 string cloud 杠 config server 大家看它后面跟了一个 config server 是不是看起来和 eureka 非常相像？没错，我们的这个应用就是作为一个中心化的 config server 来拉取服务的配置文件的。

```java
spring:
  application:
    name: config-consumer
  cloud:
    config:
      server:
        git:
          uri: https://github.com/DO-XNOTE/config-repo.git
          force-pull: true  # 强制拉去文件
#          search-paths:  有多个项目的配置文件可以使用 search-path来指定
#            -
#          username:    现在是 public 的， 如果是线上的就需要把他们填上了
#          password:



server:
  port: 60000
```


好，那这里已经配置完毕了，咱这个项目只有这一个 dependency guzhou 梭利翁读掉寒江雪，那再给他顺手指定一个 packaging 的类型是 jar 好完事收工。接下来咱去给它创建一个启动类启动类的包名就是 com.imock.spring cloud 点击。 OK 接着来它一个闷函数叫 config server application 那么骑手给他一个闷方法，public static void man 每次打这一串数字啊真是如行云流水，无丝毫障碍，总有一种莫名的快感。


快感。这个词用的地方好像不太对。 never mind 我们 man 函数里面的内容咱还是从其他地方 copy 一下，老师也背不下来。 OK 随便找了一个项目把它 copy 下来类名给他换一下，偷天换日完了以后要给他戴高帽了，咱以后还是说戴绿帽，这样说起来生动形象，对不对？Ok.第一顶绿帽子， spring boot application 带上来。好，这一顶绿帽子是别人送给他的，和他自己的应用无关。那么接着他自己又要给自己戴一顶，这个叫 enable config server 这个就跟他自己的业务功能息息相关了。


那咱现在启动类也已经配置好了。接下来一步就是去 resources 里面创建一个配置文件。咱前面说了要创建一个年轻人用的配置文件，可不能用像我这种奔四的老头子喜欢用的 properties 了。我们要向年轻人靠拢了，那给它赐名 application.yaml 了。


OK 点击回车。大家知道除了application.yaml ，还有一个配置文件叫 bootstrap.yaml 那这两个配置文件之间的加载顺序其实是有区别的，同学们可以课后自己去了解一下 application.yaml bootstrap.yaml application.properties bootstrap properties 这些配置文件之间它的加载顺序是怎么样的？就像梁山好汉排座次，咱知道谁是大哥才好安排这些配置属性的先后顺序如果你尝试从先加载的文件中读取后加载的配置文件中的属性，那可是要报错的。 OK 我们收起小弱版回到主线上来。 YAML 形式的配置文件大家应该都非常熟悉了。


第一个属性，起手节点，给它打上一个 spring OK 接着是谁是 applicationapplication 往后是什么？每次都想呼喊你的名字，你叫什么 config server 其实这个词不是 config 是 config 重音符号在 F 上面。好，往后这个属性咱大家就没见过了，cloud冒号再退一格 config 那这是这一章的主角，咱所有的跟 config 有关的属性都会放到这下面来。 OK 那咱看下面都有哪些属性啊？咱这个 config server 是什么？是中心化的节点，所以我的所有属性都要放在这下面是吧。 server 下面。


OK server 下面都有哪些属性呢？我们的配置文件存放在哪里？存放在 gate 上面。那实际上 config 不仅支持 gate 它还支持本地存储，也支持基于数据库的存储。那咱这里既然是用 git 所以这里要把所有的属性都放置在 git 节点下面。
git 有哪些属性呢？第一个就是最重要的，它叫 URI 不叫 URL 叫 uriok 这就是我们的 git 文件它的 Repo 目录。那我们到浏览器里面，把这个目录复制下来。好，点击 clone or download 在这个 HT TBS 路径把它复制下来。


接着回到 intelligi 把这一行 copy 过来。那假如这个 URL 需要登录之后才能访问，怎么办呢？那我们这里就给它添加上 username 冒号还有 passwordpassword 咱可以不用写明文，可以写密文把它加密。 okay 那咱这个项目里有没有用到 username password 咱是不是一个公开的 public Repo 也没有需要访问权限，所以说这两个属性暂时把它注掉。如果同学们在自己的线上项目中还是要把这个验证给加上的。
除了这个属性以外，咱们前面提到过，你的配置文件有可能是放在某一个路径下面的。什么意思啊？就是说你的 git 下面有可能存放的一个子目录。那么在这个子目录下才是你存放配置文件的地方，这是为了解决什么问题呢？比如说你有很多个项目共用同一个代码仓库来管理配置文件，那么每一个项目就可以使用不同的 folder 把自己的配置文件存到对应的 folder 里面。


所以在这里如果你用到了子目录，你这边要写一个额外的属性，属性名叫什么？ search 杠 cut this OK 那咱这里都是把所有配置文件放到了项目的根目录所以这一个属性同样也不需要了这里要提醒大家一下，我们的 search path 是可以配置多个路径的，比如说我们可以配置 AB C 逗号 def 那么 config server 会尝试从三个地方获取配置文件，一个是直接放到 git Repo 下的文件，另外是分别放在 AB C 或者 DE F 这两个文件夹下的文件。 OK 不仅如此，它还可以支持通配符，我们可以配置星号等等。那咱这个项目中没有 search path 所以这个环节就略过了。
除此之外，我们还要再多加一个配置，它叫什么呢？ False pull okay. 从名字我们就可以看出来，它叫强制拉取，默认是 false 我们给它指定一个 true 我这边跟它加一个注解强制拉取资源文件，这就是所有的配置了吗？ no 好像还缺了一个。是谁 server 冒号 hot 对不对？前面 high streaks 的 port 排到几了 5 万了，那咱就给 config 指定 6 万。好嘞，定义完这个属性，我们就万事俱备了。 Were all set. 那接下来就要到 config server application 里面把这个闷函数启动起来。我们这里不用 debug 模式，直接把它 run 起来启动。看到 spring 标签成功一半往下，很快的它显示已经启动成功了。


那么接下来我们要做什么？到 postman 里教大家怎么用对应的 UR L 和我们 get 上的文件，匹配上生辰 8 字，拉取到正确的文件。好，我们转战postman ，在这之前先把 log 清掉。好，我们到 postman 来学习第一个召唤术，看怎么来召唤出这个配置文件。字有点小，跟大家念一下。前面是 local host 6 万。


后面咱可以用这样的模式，先打上 confax consumer 这是我们配置的 application 对不对？然后加一个斜杠，打上 devdev 是什么？咱们配置的 profileok 我们先调用一下，看它返回什么内容，我把这个内容复制一下，放到记事板上跟大家看一下，我们看到它返回的是一个 JSON 格式的数据，这里面有几个关键信息，你看 name 是 configconsumer profile 是 DEV 这都是我们传入进去的。其中 label 是空。那这个 label 是什么？默认情况下就是 master 目录。


OK 下面是一个类似版本控制的 version 然后咱需要的属性都放在哪里？放到这个 sauce 下面了，大家还记得咱定义的是谁 DEV 环境下它的名字叫扫罗，然后它说的话是 god bless meok 那我们再来看一下log ，我们项目打印出了一行 log 看这最后一行 log 他说添加了属性源文件是什么？这里是一个文件路径，那说明 config server 在拉取到远程的 git 目录下的文件以后会怎么样？把它存到本地。对不对？那我们再回到 postman 里。你看在这个 uil 中咱们包含了 application 也包含了 profile 那如果要包含一个 label 在哪里写呢？跟在它的后面 profile 后面默认情况下是 master label 我们点击一下 searchok 依然获得了正确的结果。那如果它不是 master 是其它类型的 label 比方说我们随便填一个不存在的 label 叫 nothing 点击 send 它会告诉你 label not found 那这种情况下就说明你 label 给错了。
OK 咱这只是 config server 提供的一种 URL mapping 的方式。那还有其他的类型吗？当然有了，我们可以，把这些斜杠都去掉，咱可以直接写 config 杠 server 杠 dev.yamlok 再点击 send 它会获取到一个 YAML 格式的源文件，这个文件中的字段和 github 上面的属性文件是一模一样的。


那同学们这里 config server 还有一道机关，什么机关呢？大家看这个 URL 是不是以为老师就是把这个文件的名称复制上去了？其实不是，它这也是一种通配符，只不过这个通配符正巧长得跟我们的文件是一样的。那我这里跟大家变个魔术。我把后面的 YAML 给它改成 properties 这个文件咋定义过吗？没有对不对？那我们再来试一下 sand 看它会获取什么内容。


看到吗？这里不同了，前面是 YAML 格式的文件。那么我把这个后缀改成了 proplex 以后，它返回的是一个 proplex 的 key value 的格式，只不过这之间是用冒号，而不是用的等于号来匹配的。那还有没有其他格式呢？当然有，我把这个后缀再改一下，改成 JSON 同学们应该已经可以猜到了它会返回什么？一个 JSON 格式的文件对不对？ OK 那说明在这个 uro 匹配模式下，它的后缀是什么？是指定了你想获得的文件类型，它并不要求你在 github 上同样创建一个相应后缀的文件，我们的 config server 会自动的帮你把对应的属性文件转成你想要的格式。


那如果我想在这种 URL 下面添加上 label 怎么办呢？很简单，我在这个路径最前面，也就是紧接着端口号，我打上 label 的名称，这里是 master 我们来尝试一下。 OK 可以获得正确的结果。那同样的，如果我随便打一个不存在的label ，那相信应该也会获得 label not found 的错误对吧？果然我收获了一个 404 的 error 那好，因为 postman 上字比较小，我们把这两种不同类型的 URL copy 到代码里面，跟大家注释一下，方便回头再来查看其中这个通配符，我们把它打上 label 然后这里通配符是 application 杠 profile 大家记着后面的这个点JSON ，你还可以把它替换成点 YAML 或者是点 properties 这是一个文件格式。 OK 那除了这种格式以外，咱还可以用另外一种通配符，把这个 label 放到了后面的位置加上一个斜杠，然后把中间的横线都换成斜杠。


从这里可以看出， config server 提供出来的服务是不是非常非常的灵活啊？ OK 讲到，咱这一小节的内容就快结束了。那我来总结一下，这一小节我们主要做了两件微小的事情。第一件事情我们搭建了一个 config server 的应用，而且它需要的依赖非常非常少，然后在 YAML 的配置文件中配置了远程 git 的访问路径等等。


第二件事我们学习了如何通过 config server 暴露出来的服务，通过发送一个 get 请求来获取指定目录指定名称的 practice 文件。在这个过程中，我们还学习了两种调用 get 接口的不同姿势。那这一节的内容到这里就结束了。在下一节当中，我们将搭建一个新的应用，并且让这个新的应用连接上 config server 从 config server 中获取指定的配置属性。 OK 同学们，那我们下一节再见。


```java
package com.imooc.springcloud;

import org.springframework.boot.WebApplicationType;
import org.springframework.boot.autoconfigure.SpringBootApplication;
import org.springframework.boot.builder.SpringApplicationBuilder;
import org.springframework.cloud.config.server.EnableConfigServer;

/**
 * <h1></h1>
 */
@SpringBootApplication
@EnableConfigServer
public class ConfigApplication {

    public static void main(String[] args) {
        new SpringApplicationBuilder(ConfigApplication.class)
                .web(WebApplicationType.SERVLET)
                .run(args);
    }

    // 通配符啊-获取某种类型配置文件， github上并不是指定了什么类型的文件，在拉取的时候就一定按照他原本的类型是什么就一定是什么
    // http://localhost:60000/{label}/{application}-{profile}.json (.yml, yaml)
    // http://localhost:60000/{application}/{profile}/{label}

}
```



