---
title: 2-4 【Demo】Stream快速入门-集成MQ消费
---

# 2-4 【Demo】Stream快速入门-集成MQ消费

[image](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/ccefa890-e600-4422-a053-d6d2984c0d31/SCR-20240721-snqb.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RPX3YAKE%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T225812Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDpcMvuwp49PhrVObgfuIrXIl2SpFtNGmCnabK45G792QIgS0SnY0zcxIsDfX9kDc%2FrJvop3l6493WzXej83A%2FtoIYqiAQIxv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDPSJfqPuEqZxP%2B3MoyrcA70uBngSMYwh3U3fSQRkxlvXehxVF%2BCxr%2FTEfPM0FGX2QdnbCzKpzR7zA6tQW6zt6ppLXu%2B3hadH13FWHrqVjHe2BR4h%2FPlFdws0kQvURedvzsqUUbI0RyYDMJwlsEZIeBLIFetTN4cpkDuoqNbZzswlZ2nKkHMggOWxvZvpfNMlAay4Hogf9xzp4%2FlzCsCb6e7Fdyf4I8wcXsjp%2FLfyewRrQkSh0%2ByYucMghNrKAg2TVFKQnVj%2FvoL7mFUapZ7juIaWLQU0OsV48d7uSmxmSpKkRzsL1CO3WZ0tcJongmQNfu3c54W7fqzXJVjhsf%2FPFtCppFdqJpNblyL2b8r2F64Xmy%2Bz1SJWayKscgjXncMzskZB8x%2FnzphV3yQbg3xH7YDdCepXUL6Vf8SAOWx7VimyqJDNXNP2jhm4IljOW3VXPY0KeMJFARtZKg1zSDgqTkcqkDrjMGuFiSt5wO3ugAXnQa%2B%2F3CsawPbftErQIuXKs2cYiyk4Y0W9T19ltFTKpNSIzKkNgeLtpMcsvVFBzVAKUZG84Ew9GT8RuEAV8Lp42kS2HxX5IG5ysW4YsZ6s72yCO11K83Z3XfqYmZF99NodOJbYq0q9bEFW1RQSgJEEsubunsDZwWQO6ZYTMMW5%2F9IGOqUBpeq1gFKY3E9Q7mYhTOHLdhgX5h1fN5fJGP%2BVeUzJ4Wcuu9tl3l9VOyUv5ucAMyXbO2WNtRyhQlwNRupCE0%2B4EZhvxQbLzT6vb6kb3lSbEratkdGGT5BwHGjRetU5tqa0D10WwIA%2FRrjxM2p6LJOAl22RL4yPjHTM2Ovhu%2BB7ZAAZ69zGdwqZVB%2FXR6%2BIQ1CkGPITXhllnto6aMKqz%2FwV3r3C7O1b&X-Amz-Signature=a869cfb11b36371b1cf32b952890e4e655b065aa9f533c8705a392aceb950bb4&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

[image](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/c1aa7c0d-3618-4b95-9ea4-a31379e1b966/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RPX3YAKE%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T225812Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDpcMvuwp49PhrVObgfuIrXIl2SpFtNGmCnabK45G792QIgS0SnY0zcxIsDfX9kDc%2FrJvop3l6493WzXej83A%2FtoIYqiAQIxv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDPSJfqPuEqZxP%2B3MoyrcA70uBngSMYwh3U3fSQRkxlvXehxVF%2BCxr%2FTEfPM0FGX2QdnbCzKpzR7zA6tQW6zt6ppLXu%2B3hadH13FWHrqVjHe2BR4h%2FPlFdws0kQvURedvzsqUUbI0RyYDMJwlsEZIeBLIFetTN4cpkDuoqNbZzswlZ2nKkHMggOWxvZvpfNMlAay4Hogf9xzp4%2FlzCsCb6e7Fdyf4I8wcXsjp%2FLfyewRrQkSh0%2ByYucMghNrKAg2TVFKQnVj%2FvoL7mFUapZ7juIaWLQU0OsV48d7uSmxmSpKkRzsL1CO3WZ0tcJongmQNfu3c54W7fqzXJVjhsf%2FPFtCppFdqJpNblyL2b8r2F64Xmy%2Bz1SJWayKscgjXncMzskZB8x%2FnzphV3yQbg3xH7YDdCepXUL6Vf8SAOWx7VimyqJDNXNP2jhm4IljOW3VXPY0KeMJFARtZKg1zSDgqTkcqkDrjMGuFiSt5wO3ugAXnQa%2B%2F3CsawPbftErQIuXKs2cYiyk4Y0W9T19ltFTKpNSIzKkNgeLtpMcsvVFBzVAKUZG84Ew9GT8RuEAV8Lp42kS2HxX5IG5ysW4YsZ6s72yCO11K83Z3XfqYmZF99NodOJbYq0q9bEFW1RQSgJEEsubunsDZwWQO6ZYTMMW5%2F9IGOqUBpeq1gFKY3E9Q7mYhTOHLdhgX5h1fN5fJGP%2BVeUzJ4Wcuu9tl3l9VOyUv5ucAMyXbO2WNtRyhQlwNRupCE0%2B4EZhvxQbLzT6vb6kb3lSbEratkdGGT5BwHGjRetU5tqa0D10WwIA%2FRrjxM2p6LJOAl22RL4yPjHTM2Ovhu%2BB7ZAAZ69zGdwqZVB%2FXR6%2BIQ1CkGPITXhllnto6aMKqz%2FwV3r3C7O1b&X-Amz-Signature=3fa6def850ed7b15cfbf98311c64bb6a5782157364cca34a31b1d87ddb616693&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

[image](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/37df38cd-2372-48b6-a0d8-d2ebb7034d47/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RPX3YAKE%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T225812Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDpcMvuwp49PhrVObgfuIrXIl2SpFtNGmCnabK45G792QIgS0SnY0zcxIsDfX9kDc%2FrJvop3l6493WzXej83A%2FtoIYqiAQIxv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDPSJfqPuEqZxP%2B3MoyrcA70uBngSMYwh3U3fSQRkxlvXehxVF%2BCxr%2FTEfPM0FGX2QdnbCzKpzR7zA6tQW6zt6ppLXu%2B3hadH13FWHrqVjHe2BR4h%2FPlFdws0kQvURedvzsqUUbI0RyYDMJwlsEZIeBLIFetTN4cpkDuoqNbZzswlZ2nKkHMggOWxvZvpfNMlAay4Hogf9xzp4%2FlzCsCb6e7Fdyf4I8wcXsjp%2FLfyewRrQkSh0%2ByYucMghNrKAg2TVFKQnVj%2FvoL7mFUapZ7juIaWLQU0OsV48d7uSmxmSpKkRzsL1CO3WZ0tcJongmQNfu3c54W7fqzXJVjhsf%2FPFtCppFdqJpNblyL2b8r2F64Xmy%2Bz1SJWayKscgjXncMzskZB8x%2FnzphV3yQbg3xH7YDdCepXUL6Vf8SAOWx7VimyqJDNXNP2jhm4IljOW3VXPY0KeMJFARtZKg1zSDgqTkcqkDrjMGuFiSt5wO3ugAXnQa%2B%2F3CsawPbftErQIuXKs2cYiyk4Y0W9T19ltFTKpNSIzKkNgeLtpMcsvVFBzVAKUZG84Ew9GT8RuEAV8Lp42kS2HxX5IG5ysW4YsZ6s72yCO11K83Z3XfqYmZF99NodOJbYq0q9bEFW1RQSgJEEsubunsDZwWQO6ZYTMMW5%2F9IGOqUBpeq1gFKY3E9Q7mYhTOHLdhgX5h1fN5fJGP%2BVeUzJ4Wcuu9tl3l9VOyUv5ucAMyXbO2WNtRyhQlwNRupCE0%2B4EZhvxQbLzT6vb6kb3lSbEratkdGGT5BwHGjRetU5tqa0D10WwIA%2FRrjxM2p6LJOAl22RL4yPjHTM2Ovhu%2BB7ZAAZ69zGdwqZVB%2FXR6%2BIQ1CkGPITXhllnto6aMKqz%2FwV3r3C7O1b&X-Amz-Signature=1595ca44c105b810ad5f2dd3f32e3714332b746099589ca96d5f40cac46e016d&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

hello 慕课网的各位同学们，大家好，这一节咱来做一个 stream 的极速落地。这个极速有多急速要多快有多快，咱这是乱拳打死老师傅的玩法，不管他三七二十一，先把这个应用最快速度跑起来。


那本节的主要内容有三点，首先咱创建一个 stream sample 项目，然后引入必要的依赖。接下来就创建一个监听器。这里我会跟大家讲如何来声明和绑定一个信道。在最后我们从 rabbi MQ 里面触发一条消息，看咱刚才创建的监听器能不能正确的来消费这个消息。 OK 同学们准备好的话跟我一起 intelligi 咱开拔编程，使我快乐，996是我的福报，咱在新一章的第一个福报，我们来创建一个项目的文件夹，给 stream 搭一个目录。好它就叫stream 。

[image](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/26f66a76-1a72-4d46-aab8-33c5dc8d14b2/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RPX3YAKE%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T225812Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDpcMvuwp49PhrVObgfuIrXIl2SpFtNGmCnabK45G792QIgS0SnY0zcxIsDfX9kDc%2FrJvop3l6493WzXej83A%2FtoIYqiAQIxv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDPSJfqPuEqZxP%2B3MoyrcA70uBngSMYwh3U3fSQRkxlvXehxVF%2BCxr%2FTEfPM0FGX2QdnbCzKpzR7zA6tQW6zt6ppLXu%2B3hadH13FWHrqVjHe2BR4h%2FPlFdws0kQvURedvzsqUUbI0RyYDMJwlsEZIeBLIFetTN4cpkDuoqNbZzswlZ2nKkHMggOWxvZvpfNMlAay4Hogf9xzp4%2FlzCsCb6e7Fdyf4I8wcXsjp%2FLfyewRrQkSh0%2ByYucMghNrKAg2TVFKQnVj%2FvoL7mFUapZ7juIaWLQU0OsV48d7uSmxmSpKkRzsL1CO3WZ0tcJongmQNfu3c54W7fqzXJVjhsf%2FPFtCppFdqJpNblyL2b8r2F64Xmy%2Bz1SJWayKscgjXncMzskZB8x%2FnzphV3yQbg3xH7YDdCepXUL6Vf8SAOWx7VimyqJDNXNP2jhm4IljOW3VXPY0KeMJFARtZKg1zSDgqTkcqkDrjMGuFiSt5wO3ugAXnQa%2B%2F3CsawPbftErQIuXKs2cYiyk4Y0W9T19ltFTKpNSIzKkNgeLtpMcsvVFBzVAKUZG84Ew9GT8RuEAV8Lp42kS2HxX5IG5ysW4YsZ6s72yCO11K83Z3XfqYmZF99NodOJbYq0q9bEFW1RQSgJEEsubunsDZwWQO6ZYTMMW5%2F9IGOqUBpeq1gFKY3E9Q7mYhTOHLdhgX5h1fN5fJGP%2BVeUzJ4Wcuu9tl3l9VOyUv5ucAMyXbO2WNtRyhQlwNRupCE0%2B4EZhvxQbLzT6vb6kb3lSbEratkdGGT5BwHGjRetU5tqa0D10WwIA%2FRrjxM2p6LJOAl22RL4yPjHTM2Ovhu%2BB7ZAAZ69zGdwqZVB%2FXR6%2BIQ1CkGPITXhllnto6aMKqz%2FwV3r3C7O1b&X-Amz-Signature=c22b94f93fd3aab81c2cb54f8565be242f0cab67befcb423ec4273e83e7acb90&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

紧接着咱来创建第一个 module stream 的 dependency 相对来说非常非常简单，我们甚至连 eureka 都不用引用。它的 artifact ID 是 stream sampleok 毛球 name 保持一致，把它放到 stream 文件夹下面。好三二出来了。好，咱来手撸它的依赖，先给创建一个 dependencies 节点。那它下面咱这一节只用添加两个 dependency 第一个，dependency ，我们从其他地方 copy 过来，随便从 sloose 的下面把 activator 还有 web 引入进来。


接下来咱就要添加 stream 它自己的 dependency 独门秘籍了，它的 group ID 依然是 org supremer cloud okay artifact 是 spring 杠 cloud 再杠 starter 然后后面跟 stream rabbit OK 同学们可以看到这里咱引入的是一个 rabbit MQ 的 dependency 如果你底层使用的是 Kafka 这边只要把它替换一下就可以了，非常方便。好，咱顺手再给它指定一个 packaging 是加的类型。


好嘞，到这里 stream 就已经把 dependency 给创建好了，我们接下来创建一个启动类。首先咱要创建一个包名，这个包名就是由我们的赞助商慕课网独家冠名的 com.imock.spring cloud 回车。那接下来咱就要创建闷方法了，给它起名叫 stream application 这个闷方法咱就不去从其他地方抄袭了，这个抄袭一时抄袭一时爽抄袭，他一直爽，不能这么纵容自己，我们有时候要手打一下。


OK 它的启动方式跟其他类我们有一点那么不一样，这里不是用 server let 作为启动参数，我们直接打 spring application 然后调用的 run 方法直接跑起来就可以了，参数传入进去。 OK 那这个类它的绿帽子没有那么多，只有一顶就是 spring boot applicationok eureka 需要吗？不需要，咱这一节不集成 eureka 只通过 stream application 做 demo 就可以了。那咱的慢方法创建完了以后，大家可以跟着我一起去创建业务类了，我们给这个慕课网冠名的文件夹下面再创建一层文件夹叫 business logic 就直接起名叫base 。


OK 在这里面咱先来创建一个普通的 Java 对象，push这个类是用来做什么的呢？它就是 message bin 用来接收消息的，咱做一个非常简单的消息接收体它只有那么一个字段，叫什么叫 payload 这个 payload 是生产者在发布消息的时候生成的消息一体，那咱就原封不动地接收传递给消费者就可以了。 OK 那我们要给它生成一些 get setter 方法，就直接加上 long book 的 data 就可以。


OK 那消息体我们创建完了，接下来我早上就给他创建一个 listener 创建 listener 非常非常简单。咱先来创建一个class ， class 的名称就把它叫做 stream consumerok 回车。那在 stream consumer 里，我们定义一个方法来接收上游的消息，这个方法就叫 consumeconsume 就是消费的意思。那有什么东西让咱消费呢？这里还真有叫 payload 这就是咱刚才创建的那个 message bin 了。好，我们把它声明出来。那咱消费者接收到了上游的指令，咱总要干点什么事对吧，好歹有个响应。所以我们在这个上面给它加一个 sl four G 那加入 log 组件，就是让大家在接收到上游消息的时候，在这好歹吱一声，告诉大家我接收到消息了，咱在这里打一行 log 叫 message consumed successfully okay 然后咱再把后面的 payload 给它打印出来，这样 payload 好嘞，作为参数传递进来，这就可以了。那这个方法孤 00 助力在这，他怎么知道该去 rabbit MQ 里面拿哪一个消息信道中的消息，咱也要给它一点指示。


好，我这就给它添加一个标签，叫 stream listener 这是 stream 特有的标签。它用来做什么呢？它传入一个信道的名称。信道名称是谁呢？那就是 think 我们先把它进来，引入这一个 messaging 中的 think 使用它的 input 这个 input 疑神疑鬼的是什么意思啊？咱点进去看一下。


我们看这个类一个 interface sink 它是咱 messaging 给我们提供的一个默认的信道，大家可以用它进行简单的测试。它的主要核心链路是在这里，你看到这一个 input 标签吗？使用 input 标签，那么它就会自动为我们创建一个 subscriber channel 一个可被订阅的 channel 通信通道。那这个通道的名称是谁呢？就是在上面指定的这个 input 了。 OK 那咱这里在代码里面使用 stream listener 将信道绑定到当前的这个 consume 方法上。那我们的方法体也就能够去监听这个信道生成的消息去进行消费。


除此以外，咱仔细观察这个信道声明时候给的方法注释，你看它叫 bundable interface with one input channel 注意这个 bundable 这里面咱可以做些文章了。因此我们这里再引入一个注解，什么叫bendable ，那你看，这就叫 bendable enable bending 绑定性道。


在这一节当中，我们采用的是 stream 默认替我们声明的一个 interface 那么在稍后我会创建一个自定义的 interface 也就是自定义信道，通过这种方式把信道加载到上下文当中。哪种方式呢？我们在这声明一个 value value 等于谁，我们把 value 放到上面这一行，这样看起来好看一些。 value 就是我们可以绑定的信道的名称。比方说咱这里是 think.classok 那 stream 的上下文就会把这个类当做一个可绑定的信道加入进初始化的流程当中。


如果在后面咱自己声明了一个信道，其实我们也可以说叫 topic 因为本质上信道和 topic 都是类似的功能，我们就可以在后面添加 my topic.class 通过这种方式，我们可以自定义一个 channel 并且把它加入到上下文当中。这里我跟大家描述一下 channel 信道  还有 topic 实际上对我们来说可以看成同一种概念，我在后面的视频当中尽量都使用同一种表述，这样避免大家引起歧义咱就采用 topic 好了，主题。 OK 那我们绑定了这一个信道以后，接下来就去创建配置文件了。好，我们的配置文件是在 resources 下面想要新建一个 properties 文件。 OK 那同学们如果习惯使用 YAML 的话，可以在网上找一些很方便的 YAML properties 转化工具，把这个 properties 转化成 YAML 咱先给这个应用起一个名字 [string.application.name](http://string.application.name/) 我们就管它叫 stream sample。


Okay. 接下来当然是要给他声明 pot 了，咱前面 pot 用的太铺张浪费了。所以我们后面的几个 demo pot 都蜗居在 6 万这一个范围段里面混了，早上给它起名叫63,000。好了，除了 pot 以外，我们再给它声明 rabbit MQ 的连接方式。这一个配置项咱之前没有配置过，我们在这里加一个注释，这是 rabbit MQ 连接字符串。好，它的声明是通过 spring 后面加 rabbit MQ 这个 M 是小写，大家不要把它写成大写了，rabbit MQ host 咱的 host 就采用默认的 local host 然后后面我们把这一串的 spring rabbit MQ 复制下来，同样的给它加一个 POD 大家如果安装 rabbit MQ 的时候更改过端口，这个 pot 要写成你对应的更改过后的端口。老师这里是默认端口，就是5672。


OK 那接下来就要定义它的访问的 username 和 password 了。我们这里同样的都采用默认的 guest 接下来是 password 也等于 guest 好嘞，除了这几个以外，我想想还有没有其他的？好像就只剩 accurator 了。对不对？那咱随便挑一个项目，把 activator 给它复制过来。好，就挑你了。 sloose 我们把它直接拿到，然后复制下来。 OK 那这样的话我们的项目就已经声明好了。


OK 那到这里咱的项目就已经创建完毕了，我们接下来先来启动 rabi MQ 然后回过头再来启动这个项目。那我们打开 terminal 命令行，这里直接去调用 rabbit MQ 的启动方法，它的名字叫 rabbit MQ 杠 server 因为老师已经把这行命令都加到了 source 文件夹下的 bash profile 文件，所以我在 Mac 系统中可以直接来启动。那如果是 Windows 的同学就去找对应的启动命令。如果不记得的话，可以去回顾一下分布式章节中有关 rabbit MQ 的相应部分。那咱这里把它启动起来，稍等片刻，它这里显示已经加载成功，并且加载了 6 个 plugin 好我们这时候到页面上看一下这个 rabi MQ 有没有启动起来。好，走到浏览器中，我们打开 rabbit MQ 的 15672 默认端口。好回撤。它这里要登录。那 username 和 password 都是 guestokay 那这里已经登录进去了，同学们看到老师在这边已经创建了很多信道 exchange 和Q ，大家不用管，这都是后面课程的内容了。


好，那既然这个 rabmq 已经启动成功了，那接下来咱就要去启动项目了，我们把 man 方法找到 stream application 们方法我们走起，稍等半炷香的时间，待它启动完成，看到 spring 成功一半，这里已经开始在连接 rabbit MQ 了，你看它这里已经打出了一些 log registering message handler okay 那这里已经去连接 rabbit MQ 尝试去创建一些信道了。


topic 好，我们把 log 清空，然后到 rabbit MQ 页面看它发生了什么事情。 rabmq 这么多 tab 我们看哪一个呢？那就是这个 Q 了，我们点击一下。 OK 在 Q 里大家看到眼花缭乱非常非常多的 Q name ，咱这里用关注哪一个呢？那就是这一个，你看它的名称，input点匿名点巴拉巴拉一串乱七八糟的数字。这个就是咱刚才默认去给它创建的 input channel 那我们点击进去。好，在这个页面，我们尝试给这个 channel 发送一条消息，怎么发呢？我们往下滚好。走到这里有一个 publish message 咱给它添加一个 payload hello stream 好，把它推送出去。走，你这里显示 message published 好，那我们回到 intelligent 里面看一看。


同学们看，这里有一行 log message consumed successfully 它的 payload 正是从前端传入的 hellostream 那实际上这里咱大家也可以写中文，都是可以传递过去的。是的吗？走你后台也是的吗？ OK 那一个简单的极速落地的通道就已经创建完成了。那本小节的快速落地到这里就结束了。同学们可能会想，咱这里只是创建了一个 consumer 那 producer 还没有创建，不着急，这是下一小节的内容了。


那我这里再带大家快速回顾一下本小节学习的内容。首先我们创建了 pump 文件引入了 stream 的特殊依赖。这个依赖项会根据咱底层使用的中间件不同有所区别。比如咱使用的是 rabbit MQ 所以 artifact ID 也是对应到 rabbit MQ 的实现。接着我们创建了一个 stream consumer 用来作为消息的消费者。这个 consumer 方法通过一个 stream listener 标签和 rabbit MQ 中的 topic 进行关联。这个 stream listener 我们是采用的 stream 给我们提供的默认信道，只是为了方便大家进行测试。那在下一个小节里我们还会声明自己的 topic 然后将咱自定义的 topic 绑定在 enable binding 这个注解的下面。这样我们就可以通过一个 controller 触发生产者的消息发送，然后在观察消费者是如何消费这个消息的。


在下一个视频小结之前，我会带大家通过图文的形式看一下 banner 的底层作用机制，然后去复习一下发布订阅的模型。 OK 同学们，那这一节的内容就到这里结束了，我们下一个小节再见。




