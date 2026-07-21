---
title: 2-16 【Demo】Stream实现Requeue操作
---

# 2-16 【Demo】Stream实现Requeue操作

[image](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/e550c899-afed-4b8e-a043-a6a1c2c72062/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667G5P3YFI%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T225820Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDAKnh8klk4W6vLhi%2BbIYvdbl2ZvL5Qe%2B%2BTCdhUedH%2FEAIgAr%2BmSG2hloXoWU9FNLvl30L0D%2BdfXFm5NCsKkUhdH%2FQqiAQIxv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDKMtW995sG7Eu9jU4CrcA9y1lcOvUg2HXOdo3kJygwAgeN7IzfUIp3bdZLjdUnqaT94MiRabhLE%2FMyG6xvSSTEeWzXW%2FOHchNMYia9ytrL6cVSG5IDp03CG%2BXcXeZ9sjoqK%2FQEMoOEsFAjVSvR5P2eVlao5xhSw5P59USj7I0xtITqbk%2FAFyyKOlKP%2BAwDW5tkI1Ym88Tbo5cxCMlSUmxBrnFIZJxYddoTsqljFWvdBJomyjgfw9%2B4AMzj%2B8UeOg5sG7eZgGrv8JKhkDSymauX%2BObSvKXf4D9ZxiZb6YZFd9G7UPCXby1idI4ArRemXUd0bkzNC%2B359g45%2FXeDrkixOZZ2y%2Fw5JcgPyzFWlFcyeMsgMbqbAYWp8eAIEfXaRpfubciQDRQBf6zeEhzPYlx62qoNeyS5LpwV5tkRWIXqRuA%2BExHZqVoDlQh5A7lDo49qnUYprBF0IvToPesnjWrLQ3dxlXVddFzQt6Zv2xEi2rrDEvzTI0TIOwxA7TN0YdxZ1X2RZQG66O1aT5zecRGF9z2fgIpgKusZxGg2Y%2B3Ea0R9LfNjL2RzBU8V26iiVXvkoK0MM4UHJNMrgj6%2FgzDiXmcQ4MJ3WH2QQRuDGDYhg3J1giljoETCK15t1QmLK7%2BYLiAuXF5J3peGfBMNe6%2F9IGOqUB7NYSNMbDfyhJTPCEZ78wYfrMr23O2GsMEaOpat%2FDPqoz0Jue%2BQVIuPGJGcjlS8m7iL4KrUgloSJtywPg9vBmMmEgxibrSgpZWB1p8iDsEtXnaLjaYgeQbG3BybtOaZcLx8l%2FcCYf1p1zqEmhbMe7pMNAaYuj7utU0qUVpVqHc8nawZ%2BKfTCdKw0RG0E0xbpQT%2FZWuQfquZw84BgOP4wuHP4RnNXy&X-Amz-Signature=65eb681297cc8ecccd397ea9f033a14869330e83793115e49e712088547941ed&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

[image](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/a5ae4720-8487-437d-a202-57351a45e358/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667G5P3YFI%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T225820Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDAKnh8klk4W6vLhi%2BbIYvdbl2ZvL5Qe%2B%2BTCdhUedH%2FEAIgAr%2BmSG2hloXoWU9FNLvl30L0D%2BdfXFm5NCsKkUhdH%2FQqiAQIxv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDKMtW995sG7Eu9jU4CrcA9y1lcOvUg2HXOdo3kJygwAgeN7IzfUIp3bdZLjdUnqaT94MiRabhLE%2FMyG6xvSSTEeWzXW%2FOHchNMYia9ytrL6cVSG5IDp03CG%2BXcXeZ9sjoqK%2FQEMoOEsFAjVSvR5P2eVlao5xhSw5P59USj7I0xtITqbk%2FAFyyKOlKP%2BAwDW5tkI1Ym88Tbo5cxCMlSUmxBrnFIZJxYddoTsqljFWvdBJomyjgfw9%2B4AMzj%2B8UeOg5sG7eZgGrv8JKhkDSymauX%2BObSvKXf4D9ZxiZb6YZFd9G7UPCXby1idI4ArRemXUd0bkzNC%2B359g45%2FXeDrkixOZZ2y%2Fw5JcgPyzFWlFcyeMsgMbqbAYWp8eAIEfXaRpfubciQDRQBf6zeEhzPYlx62qoNeyS5LpwV5tkRWIXqRuA%2BExHZqVoDlQh5A7lDo49qnUYprBF0IvToPesnjWrLQ3dxlXVddFzQt6Zv2xEi2rrDEvzTI0TIOwxA7TN0YdxZ1X2RZQG66O1aT5zecRGF9z2fgIpgKusZxGg2Y%2B3Ea0R9LfNjL2RzBU8V26iiVXvkoK0MM4UHJNMrgj6%2FgzDiXmcQ4MJ3WH2QQRuDGDYhg3J1giljoETCK15t1QmLK7%2BYLiAuXF5J3peGfBMNe6%2F9IGOqUB7NYSNMbDfyhJTPCEZ78wYfrMr23O2GsMEaOpat%2FDPqoz0Jue%2BQVIuPGJGcjlS8m7iL4KrUgloSJtywPg9vBmMmEgxibrSgpZWB1p8iDsEtXnaLjaYgeQbG3BybtOaZcLx8l%2FcCYf1p1zqEmhbMe7pMNAaYuj7utU0qUVpVqHc8nawZ%2BKfTCdKw0RG0E0xbpQT%2FZWuQfquZw84BgOP4wuHP4RnNXy&X-Amz-Signature=86ccc1146df7e33a26e7d64a081b2d3095e2011a1b0e1bfcfe9405b022ed2bdb&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

[image](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/52012003-ea7e-4e32-8fd5-38ac8219b01b/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667G5P3YFI%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T225820Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDAKnh8klk4W6vLhi%2BbIYvdbl2ZvL5Qe%2B%2BTCdhUedH%2FEAIgAr%2BmSG2hloXoWU9FNLvl30L0D%2BdfXFm5NCsKkUhdH%2FQqiAQIxv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDKMtW995sG7Eu9jU4CrcA9y1lcOvUg2HXOdo3kJygwAgeN7IzfUIp3bdZLjdUnqaT94MiRabhLE%2FMyG6xvSSTEeWzXW%2FOHchNMYia9ytrL6cVSG5IDp03CG%2BXcXeZ9sjoqK%2FQEMoOEsFAjVSvR5P2eVlao5xhSw5P59USj7I0xtITqbk%2FAFyyKOlKP%2BAwDW5tkI1Ym88Tbo5cxCMlSUmxBrnFIZJxYddoTsqljFWvdBJomyjgfw9%2B4AMzj%2B8UeOg5sG7eZgGrv8JKhkDSymauX%2BObSvKXf4D9ZxiZb6YZFd9G7UPCXby1idI4ArRemXUd0bkzNC%2B359g45%2FXeDrkixOZZ2y%2Fw5JcgPyzFWlFcyeMsgMbqbAYWp8eAIEfXaRpfubciQDRQBf6zeEhzPYlx62qoNeyS5LpwV5tkRWIXqRuA%2BExHZqVoDlQh5A7lDo49qnUYprBF0IvToPesnjWrLQ3dxlXVddFzQt6Zv2xEi2rrDEvzTI0TIOwxA7TN0YdxZ1X2RZQG66O1aT5zecRGF9z2fgIpgKusZxGg2Y%2B3Ea0R9LfNjL2RzBU8V26iiVXvkoK0MM4UHJNMrgj6%2FgzDiXmcQ4MJ3WH2QQRuDGDYhg3J1giljoETCK15t1QmLK7%2BYLiAuXF5J3peGfBMNe6%2F9IGOqUB7NYSNMbDfyhJTPCEZ78wYfrMr23O2GsMEaOpat%2FDPqoz0Jue%2BQVIuPGJGcjlS8m7iL4KrUgloSJtywPg9vBmMmEgxibrSgpZWB1p8iDsEtXnaLjaYgeQbG3BybtOaZcLx8l%2FcCYf1p1zqEmhbMe7pMNAaYuj7utU0qUVpVqHc8nawZ%2BKfTCdKw0RG0E0xbpQT%2FZWuQfquZw84BgOP4wuHP4RnNXy&X-Amz-Signature=f5fec9a154756d8d5f077f3b3c942eecce03684eb5e491af1231a988fc9ec13e&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

慕课网的各位同学们，大家好，在上一小节，咱学习了 stream 的单机版重试策略，这一节咱把它升级一下，变成联机对抗式的重试。我们来学习如何在 stream 中通过 requeue 也就是重新入队来进行消息的失败重试。这里的重新入队实际上指的是将失败的消息重新放回到 rebmq 中，然后让消费者的集群重新拉取消息进行处理。

[image](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/262c74cc-55f5-4ed3-9c0a-302ff7215f09/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667G5P3YFI%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T225820Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDAKnh8klk4W6vLhi%2BbIYvdbl2ZvL5Qe%2B%2BTCdhUedH%2FEAIgAr%2BmSG2hloXoWU9FNLvl30L0D%2BdfXFm5NCsKkUhdH%2FQqiAQIxv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDKMtW995sG7Eu9jU4CrcA9y1lcOvUg2HXOdo3kJygwAgeN7IzfUIp3bdZLjdUnqaT94MiRabhLE%2FMyG6xvSSTEeWzXW%2FOHchNMYia9ytrL6cVSG5IDp03CG%2BXcXeZ9sjoqK%2FQEMoOEsFAjVSvR5P2eVlao5xhSw5P59USj7I0xtITqbk%2FAFyyKOlKP%2BAwDW5tkI1Ym88Tbo5cxCMlSUmxBrnFIZJxYddoTsqljFWvdBJomyjgfw9%2B4AMzj%2B8UeOg5sG7eZgGrv8JKhkDSymauX%2BObSvKXf4D9ZxiZb6YZFd9G7UPCXby1idI4ArRemXUd0bkzNC%2B359g45%2FXeDrkixOZZ2y%2Fw5JcgPyzFWlFcyeMsgMbqbAYWp8eAIEfXaRpfubciQDRQBf6zeEhzPYlx62qoNeyS5LpwV5tkRWIXqRuA%2BExHZqVoDlQh5A7lDo49qnUYprBF0IvToPesnjWrLQ3dxlXVddFzQt6Zv2xEi2rrDEvzTI0TIOwxA7TN0YdxZ1X2RZQG66O1aT5zecRGF9z2fgIpgKusZxGg2Y%2B3Ea0R9LfNjL2RzBU8V26iiVXvkoK0MM4UHJNMrgj6%2FgzDiXmcQ4MJ3WH2QQRuDGDYhg3J1giljoETCK15t1QmLK7%2BYLiAuXF5J3peGfBMNe6%2F9IGOqUB7NYSNMbDfyhJTPCEZ78wYfrMr23O2GsMEaOpat%2FDPqoz0Jue%2BQVIuPGJGcjlS8m7iL4KrUgloSJtywPg9vBmMmEgxibrSgpZWB1p8iDsEtXnaLjaYgeQbG3BybtOaZcLx8l%2FcCYf1p1zqEmhbMe7pMNAaYuj7utU0qUVpVqHc8nawZ%2BKfTCdKw0RG0E0xbpQT%2FZWuQfquZw84BgOP4wuHP4RnNXy&X-Amz-Signature=6617a2e48a14c2d5ed3680a83b4228edcfc05c3c2ce724061f79307d3cab967c&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

OK 咱来看一下这一节的主要内容。分为三个部分。首先还是老生常谈的，咱创建一个 producer 和 consumer 专门用来测试 requeue 的这个示例。紧接着我们在 properties 文件中开启 requeue 重新入队的功能。


这里有一个需要注意的点， requeue 和咱前面配置的 retry 是有冲突的。在有些情况下，如果你配置了 retry 以后， requeue 是不会生效的。那最后一个部分我们把 requeue 的应用启动起来。这里咱启动多个 instance 然后测试 requeue 在不同节点之间是如何消费的。


那咱前面说过它不再是一个单机版的重试玩法了。为什么？因为你消息重新入队了以后，它就可以在整个的 consumer 集群中有任意一台服务器来进行消费了，不会像之前的重拾势力一样仅在一台 consumer 上消费。所以咱说它是一个联机版的游戏。那同学们准备好的话跟我一起开赴 intelligi 编程，是我快乐 996 是我的福报。我们的 topic 大军中又要再添一个新丁了，我们依然选择复制任意一个 topic 创建一个新的。这个新的 topic 我们是专门测试 recue 的，所以给它起名就叫 recue topic 剩下的步骤大家应该都轻车熟路了是吧。


把 input 和 output 的名称改一下，分别改成 requeue consumer 以及 recue producer OK 这两个改完以后，咱去更改一下 controller 好，我们在 controller 的头顶，先把刚才创建的 topic 给它引入进来，同样也是 out wide 的注解进来。 recue topic 这个 recue cue 特别容易拼错 recue topic 然后它的名称 recue topic producer OK 添加完 topic 又可以滚啦啊往下滚到最下面咱把上一个 controller 方法给它 copy 一下。


上面是单机版，咱这里叫联机版，然后他是重新入列。好了，这个 controller 的方法名，我们把它改成 send error message to mqok 那它的路径我们就叫 recue 这里改完之后，咱们千万别忘了这个小尾巴这里要改的，咱们把这里的 eratopic producer 要给它改成新创建的 requeue 不然的话你这个 message 就发错地方了，遁入空门无处寻了。


OK 咱 controller 配置好了以后，我们打开 consumer 然后在 consumer 的头顶，咱把这个新添加的类给它加进去，叫 recue topicok 那往下滚到最下面，我们把这个单机版的异常重试依然选择 copy 一下，然后在这里给它添加一个联机版重新入列。这里注释打全一些。在这个连击版方法中，咱不像这个单击版这么虐，OK一会儿又不 OK 的，咱把它改的简单一些咱永远都不 OK 只要你过来了，我就给你发 runtime exception 让你这条 message 一旦被生成出来，就永远在 consumer 这里不断地轮回，永世不得翻身。那 consumer 的名称我们要改一下，改成 requeue error message 重新入列。


然后把这里的 topic 名称改成新创建的 recue topic 除此以外，咱这里还想用线程停顿的方式把当前线程挂起，几秒以后再抛出异常。因为如果不停顿线程的话，那你接收到消息立马就抛出异常。这个速度就像脱缰的野狗一样，一直往 rabmq 里面插，重试的消息一秒钟可能就能怼出去几百个，log里面也看不清楚。所以咱这里给它来一个 try catchtry catch 什么内容线程停顿，我们把当前线程让它睡几秒钟 thread sleep 3 秒钟。好了，这样当咱每次收到消息以后会停顿 3 秒钟，然后再发出一个异常。 OK 那咱的消费者也写好了，接下来就剩最后一步了。


修改配置文件，咱每一个小节都能往配置文件中发现几个新的属性。这一小节也不例外，咱也有专门的新属性要跟大家介绍。我们打开 application.properties 我们选择把上面的异常消息这里的配置 copy 一下 hop 1 份之后在这边粘贴，然后把注释改一下。前面是异常消息单机版重试，咱给它改成 requeue 重试。
然后剩下的步骤大家应该非常熟悉了。我们把 topic 的名称改成 recure consumer 和 recure producer 并且它的 destination 属性咱也要把它改成一个新的叫 recue topicok 改完这两个以后，咱要开启 recue 的功能，这是一个新的属性，我们来看它是怎么来开启这个属性的。开头部分是叫 spring cloud stream rabbit bundings 我们从这个延迟消息配置这里把它的开头 copy 下来。然后后面要跟 requeue consumer 接着再来一个 consumer 后面跟 requeue rejected 这个 R 大写， recure rejected 后面的属性我们给它写明是 true 那这个属性是什么意思呢？它的意思是说仅对当前的这个 recue consumer 开启重新入队。仅对当前我们把它添加上注释。


那如果大家想在全局范围内开启重新入队，那是怎么个配置法呢？这里有一个默认配置，我们打开注释叫默认全局开启 requeue 那它的属性长得有那么点不一样，它叫 string.rabbit MQ 再点 listeners 后面跟着点 default 默认 rekill rejected 等于 true 如果你把这个属性打开了，那它这 req 操作就可以在全局生效，咱先把它给注释掉。


同学们以为这样它的 req 就会生效了吗？实际上，前面在小学开始的时候我们提到过 requeue 它和 retry 在某个配置上有冲突，大家能猜想是哪个配置吗？那我们回过头看一下 retry 的配置，你看它这里有这样一个配置，叫 retry 的次数。
那同学们想一下，如果咱配置了 retry 次数，也就是指定了它在原地 retry 那么失败以后它还会把它添加到 Q 里面吗？不会了，所以这里咱要强制的怎么样，强制的把它的 retry 次数指定成1，也就是说我不让你在原地 retry 你失败了，就立马把这个失败消息退回到 rebmq 中，重新添加进去，让其他的 consumer 可以消费它。 OK 除了这个配置以外，我还要再添加一个配置，咱把前面用到的知识都给它加入进来。


这个配置是消费组，因为咱待一会儿要启动多个节点进行测试。咱不是说 recue 是种连接的异常处理方案吗？所以我们要看 recue 进到 rabi MQ 的消息，是否会被其他的消费端来消费。那为了保证可以观测到这种消费者之间的切换，那我们要把这些所有的消费者添加到同一个消费组里，这样的话每个消息就只会被消费一次。那咱给他指定的 group 就叫 recue group 好了，recue it 咦我这里好像看到了一处拼写错误，咱前面还说 recue 特别特别容易拼错。好，大家看。好，不要把这个拼错，要不这个配置文件不起作用的。咱现在配置文件都已经配置好了，咱们可以去 main 方法里启动示例来进行测试了。我们打开 string application 的 main 方法启动第一个 instance 然后回过来 application 里面的端口话从 63,002 再改到63,003，然后再启动一次。好，我们大概等个半柱箱的时间，等这两个 instance 启动好，就可以到 postman 里发起一个调用，去查看一下结果了。好，我们看到第一个和第二个应用都已经启动好了，咱把 log 全部清空掉。


接下来转战到 postman 里，我们这里已经创建好了一个专门用来做 requeue 消息发送的 HTTP 请求，那它是 post 发送到端口号是 63,003 的机器上，然后它的 controller 的地址是 recue 好，我们这里要点击send ，大家记住，每隔 3 秒钟我们的消费者就会抛出异常，然后这个消息就会被重新放回到 Q 里面。好，我们点击 send 走起。接下来咱回到 intelligent 里面看一看效果。好，你看这里已经有异常打出了，滑到最下面，看它的异常是怎么样打印的。


OK 大家看到这里，在 22 秒的时候，它收到了一个消息，然后在 3 秒钟以后它抛出了异常，也就是 25 秒的时候抛出一个异常，紧接着把这个滑到下面。到这里。他在第 28 秒的时候又接到了一条消息，咦同学们，为什么我在 25 秒抛出的这个异常？那他的 message 应该是被已经加回到 rabmq 了，可是我在第 28 秒才去再次的消费了这条消息。
那这中间的三秒钟去哪了呢？我想同学们应该已经知道答案了，这消失的 3 秒钟就跑到了它的邻居这里另外一台 stream application 的服务器上。我们可以看到它这里打印出了log，你看这里接收了一条消息，在这边睡了 3 秒钟以后，抛出了一条异常。不过紧接着这个异常以后，他并没有立即消费另一条消息，而是又过了 3 秒钟，在第 49 秒的时候才消费到了下一条消息。所以他们每次把异常消息重新加回到 rabmq 以后，这条消息都会被另外一台机器所消费。


如果咱是一个集群的话，那么这台集群中的每一台机器都有机会参与这条信息的消费。所以它和前面的 retry 模式最大的不同就是 retry 只在当前这台 consumer 上面 retry 它并不会把消息重新加回到 rabmq 而 recue 它是把消息加回到 rabmq 让整个集群中的任意一个 consumer 都可以去消费这条消息。因此我们才把 recue 称作为联机版的异常处理。


OK 那讲到这，整个小节的内容就结束了，我来带大家简单的回顾一下。在本小节中，咱创建了一个新的 requeue 重新入队的 topic 并且在它对应的 consumer 里设置了每次接到消息之后，将线程挂起 3 秒后抛出一个异常。那一场消息是如何重新被加入到 rabmq 呢？这里的玄机就在 application.properties 里面。咱在这里面学习了两个新的配置。其中一个配置，它可以指定某个 consumer 将它的重新入队功能打开。咱还学习了一个全局的配置，可以默认在全局范围内开启 requeue 还有一个功能相当重要，就是 retry 和 requeue 之间的一个冲突。我们这里要加一行注释，必须把 max attempts 设置为1，否则这个 recue 功能就不能生效。


OK 那到这里，整个小节的内容就结束了。不过同学们看，刚才抛出的这个 req 操作好像还在一直跑，跑个没完了怎么办？他一直在 consumer 这边轮回，永世不得翻身，这也不是个办法。那我们有什么彻底的办法可以解决这种异常情况吗？这就是咱下一节要讨论的内容了，我们将要去探讨如何在技术层面解决这种情况。同时我们还会引入一个新的法宝，叫做死信队列。那预知里面详情如何呢？且听老师下回分解了同学们，那我们下一期的课程再见。




