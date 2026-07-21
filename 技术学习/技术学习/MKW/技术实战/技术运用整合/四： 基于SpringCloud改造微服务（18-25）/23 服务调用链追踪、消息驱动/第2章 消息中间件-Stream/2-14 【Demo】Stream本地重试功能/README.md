---
title: 2-14 【Demo】Stream本地重试功能
---

# 2-14 【Demo】Stream本地重试功能

[image](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/a7d4c12b-13e0-4c3b-b662-dbd84521f5e1/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SI3KBPCM%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T225819Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIB5Kuq5QqgWjOnoSK%2BZqViyv%2BXJaBSdJzK9w5py7rBvFAiBNxnQalikf31VZ6d%2BRPa1LEOSrAc5ul3TtdsFGN6BkaCqIBAjG%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMV0y6R5wDSc28KKLVKtwDMenGMn0atyMbUL9Kau6tqSFZY0wzjpTl3%2BD6VYLTKDdwfbUa27HkfzVm%2FIUqaSZP3fvmsCkRdpCZOdBgFAbJSrsiaTJvz90rbnqHd3SbXOj7z87u8AeALUz3XoiKIJcYmwR3h9vo0m%2FFr9FNZg6HM8h1vqnnepIPqUkUaEr4p8iaPsi7RM%2BKad7N6%2Fsm7Gr15DfLhW36FCiroF7DHMmyMoyX%2B2kpAV7c484jiEkGbCEK3V43auQqXGokuviTu0YBMHynbbdW1QjW6YG8F1wpomayCvwGzU%2Fj9DjxR%2BHwDdyQ0y1gaDHRMQwf8vbNA4RzcS%2B8MU%2Fz8H3MBbthmIxmCjpbLXLTZPa8MS4KLxu9uXGTGIMnOIWvIuvtZ9XNr0nXUyIW%2BfQpS6CtCxfmjCXRKQWE3y6WA1cuQVjRASnJ77yTMp1sqCZKXbvKzzwFV8F1J6QJVnGj9SNI2AseLY%2BxuHiOYI2F3p%2FRXUIOEfNhgrkvkfku2eT1cuR9aoajU9EJGoh8iGblGsLdn3ZScvEM%2BjdA%2FCViuDz5rpqgiv5r7HEHXuhHu0xP4R6E%2FdhwdSZ13JXkxqYUPoqyQNmDMGw2lPshKqFy1ZfnSN5cLqiIdMPubBY9%2BcuujV7Pz4Iwu7j%2F0gY6pgEgvReu9UBnVa%2Fw0Rw7n1ia0Dwczdxtc4zaPpILDnAfNlLFBBPpXCSovE5e6pcUVG1aKX2ekyxYfW9AvCDW7dM1NOOCeT%2BBG5aRixKCtRiFNeAEb3XvD%2BJzHn5wiEovYt%2Fxt8Y7Ba%2FaB71sgPlToDBp5LjbqP50N9VHvitE%2FXu4cQ8b8oyIfmvfT5OJH7uLJjaY7lNSN9%2FXY%2FxFfI8iHTiUf2h2CWS8&X-Amz-Signature=998912b210dd2e29e2638b2add02515ad0b99297fc620437a0a77efe4642b248&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

[image](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/ea8bc3f6-5c5b-4a40-8b2f-fdad38bc621b/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SI3KBPCM%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T225819Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIB5Kuq5QqgWjOnoSK%2BZqViyv%2BXJaBSdJzK9w5py7rBvFAiBNxnQalikf31VZ6d%2BRPa1LEOSrAc5ul3TtdsFGN6BkaCqIBAjG%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMV0y6R5wDSc28KKLVKtwDMenGMn0atyMbUL9Kau6tqSFZY0wzjpTl3%2BD6VYLTKDdwfbUa27HkfzVm%2FIUqaSZP3fvmsCkRdpCZOdBgFAbJSrsiaTJvz90rbnqHd3SbXOj7z87u8AeALUz3XoiKIJcYmwR3h9vo0m%2FFr9FNZg6HM8h1vqnnepIPqUkUaEr4p8iaPsi7RM%2BKad7N6%2Fsm7Gr15DfLhW36FCiroF7DHMmyMoyX%2B2kpAV7c484jiEkGbCEK3V43auQqXGokuviTu0YBMHynbbdW1QjW6YG8F1wpomayCvwGzU%2Fj9DjxR%2BHwDdyQ0y1gaDHRMQwf8vbNA4RzcS%2B8MU%2Fz8H3MBbthmIxmCjpbLXLTZPa8MS4KLxu9uXGTGIMnOIWvIuvtZ9XNr0nXUyIW%2BfQpS6CtCxfmjCXRKQWE3y6WA1cuQVjRASnJ77yTMp1sqCZKXbvKzzwFV8F1J6QJVnGj9SNI2AseLY%2BxuHiOYI2F3p%2FRXUIOEfNhgrkvkfku2eT1cuR9aoajU9EJGoh8iGblGsLdn3ZScvEM%2BjdA%2FCViuDz5rpqgiv5r7HEHXuhHu0xP4R6E%2FdhwdSZ13JXkxqYUPoqyQNmDMGw2lPshKqFy1ZfnSN5cLqiIdMPubBY9%2BcuujV7Pz4Iwu7j%2F0gY6pgEgvReu9UBnVa%2Fw0Rw7n1ia0Dwczdxtc4zaPpILDnAfNlLFBBPpXCSovE5e6pcUVG1aKX2ekyxYfW9AvCDW7dM1NOOCeT%2BBG5aRixKCtRiFNeAEb3XvD%2BJzHn5wiEovYt%2Fxt8Y7Ba%2FaB71sgPlToDBp5LjbqP50N9VHvitE%2FXu4cQ8b8oyIfmvfT5OJH7uLJjaY7lNSN9%2FXY%2FxFfI8iHTiUf2h2CWS8&X-Amz-Signature=b9c49501dbe5a3a87feee05468bc3b5287630b6cf15d7b4d802955eb0f41c73e&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

[image](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/a814803c-92f7-444a-a23f-1f3b7166ba80/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SI3KBPCM%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T225819Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIB5Kuq5QqgWjOnoSK%2BZqViyv%2BXJaBSdJzK9w5py7rBvFAiBNxnQalikf31VZ6d%2BRPa1LEOSrAc5ul3TtdsFGN6BkaCqIBAjG%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMV0y6R5wDSc28KKLVKtwDMenGMn0atyMbUL9Kau6tqSFZY0wzjpTl3%2BD6VYLTKDdwfbUa27HkfzVm%2FIUqaSZP3fvmsCkRdpCZOdBgFAbJSrsiaTJvz90rbnqHd3SbXOj7z87u8AeALUz3XoiKIJcYmwR3h9vo0m%2FFr9FNZg6HM8h1vqnnepIPqUkUaEr4p8iaPsi7RM%2BKad7N6%2Fsm7Gr15DfLhW36FCiroF7DHMmyMoyX%2B2kpAV7c484jiEkGbCEK3V43auQqXGokuviTu0YBMHynbbdW1QjW6YG8F1wpomayCvwGzU%2Fj9DjxR%2BHwDdyQ0y1gaDHRMQwf8vbNA4RzcS%2B8MU%2Fz8H3MBbthmIxmCjpbLXLTZPa8MS4KLxu9uXGTGIMnOIWvIuvtZ9XNr0nXUyIW%2BfQpS6CtCxfmjCXRKQWE3y6WA1cuQVjRASnJ77yTMp1sqCZKXbvKzzwFV8F1J6QJVnGj9SNI2AseLY%2BxuHiOYI2F3p%2FRXUIOEfNhgrkvkfku2eT1cuR9aoajU9EJGoh8iGblGsLdn3ZScvEM%2BjdA%2FCViuDz5rpqgiv5r7HEHXuhHu0xP4R6E%2FdhwdSZ13JXkxqYUPoqyQNmDMGw2lPshKqFy1ZfnSN5cLqiIdMPubBY9%2BcuujV7Pz4Iwu7j%2F0gY6pgEgvReu9UBnVa%2Fw0Rw7n1ia0Dwczdxtc4zaPpILDnAfNlLFBBPpXCSovE5e6pcUVG1aKX2ekyxYfW9AvCDW7dM1NOOCeT%2BBG5aRixKCtRiFNeAEb3XvD%2BJzHn5wiEovYt%2Fxt8Y7Ba%2FaB71sgPlToDBp5LjbqP50N9VHvitE%2FXu4cQ8b8oyIfmvfT5OJH7uLJjaY7lNSN9%2FXY%2FxFfI8iHTiUf2h2CWS8&X-Amz-Signature=384650153e0a732b91a3c6aea8592da0979dba0826ce980ece871cc5a91f8c46&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

[image](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/da476e47-e490-439e-b6ba-49d6ba87b2df/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SI3KBPCM%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T225819Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIB5Kuq5QqgWjOnoSK%2BZqViyv%2BXJaBSdJzK9w5py7rBvFAiBNxnQalikf31VZ6d%2BRPa1LEOSrAc5ul3TtdsFGN6BkaCqIBAjG%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMV0y6R5wDSc28KKLVKtwDMenGMn0atyMbUL9Kau6tqSFZY0wzjpTl3%2BD6VYLTKDdwfbUa27HkfzVm%2FIUqaSZP3fvmsCkRdpCZOdBgFAbJSrsiaTJvz90rbnqHd3SbXOj7z87u8AeALUz3XoiKIJcYmwR3h9vo0m%2FFr9FNZg6HM8h1vqnnepIPqUkUaEr4p8iaPsi7RM%2BKad7N6%2Fsm7Gr15DfLhW36FCiroF7DHMmyMoyX%2B2kpAV7c484jiEkGbCEK3V43auQqXGokuviTu0YBMHynbbdW1QjW6YG8F1wpomayCvwGzU%2Fj9DjxR%2BHwDdyQ0y1gaDHRMQwf8vbNA4RzcS%2B8MU%2Fz8H3MBbthmIxmCjpbLXLTZPa8MS4KLxu9uXGTGIMnOIWvIuvtZ9XNr0nXUyIW%2BfQpS6CtCxfmjCXRKQWE3y6WA1cuQVjRASnJ77yTMp1sqCZKXbvKzzwFV8F1J6QJVnGj9SNI2AseLY%2BxuHiOYI2F3p%2FRXUIOEfNhgrkvkfku2eT1cuR9aoajU9EJGoh8iGblGsLdn3ZScvEM%2BjdA%2FCViuDz5rpqgiv5r7HEHXuhHu0xP4R6E%2FdhwdSZ13JXkxqYUPoqyQNmDMGw2lPshKqFy1ZfnSN5cLqiIdMPubBY9%2BcuujV7Pz4Iwu7j%2F0gY6pgEgvReu9UBnVa%2Fw0Rw7n1ia0Dwczdxtc4zaPpILDnAfNlLFBBPpXCSovE5e6pcUVG1aKX2ekyxYfW9AvCDW7dM1NOOCeT%2BBG5aRixKCtRiFNeAEb3XvD%2BJzHn5wiEovYt%2Fxt8Y7Ba%2FaB71sgPlToDBp5LjbqP50N9VHvitE%2FXu4cQ8b8oyIfmvfT5OJH7uLJjaY7lNSN9%2FXY%2FxFfI8iHTiUf2h2CWS8&X-Amz-Signature=f219496424c3aaf725e3a678125364f495e80a9776cf17d47c17ff0c2c616d32&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

hello 慕课网的各位同学们，大家好，咱中国有句老话，叫人非圣贤孰能无过，你有过我有过。咱接下来就看一看 stream 面对各种各样的异常情况，它都有哪些处理的方法手段？咱先从简单的异常处理方法开始看起。那这第一种方法就是简单的异常重试。我们看一看本节的主要内容。第一部分咱依然是创建一对 consumer 和 producer 在 consumer 里面，我们刻意的抛出一个运行器异常。接下来咱要对配置文件做一点修改，在配置文件中引入重试次数。接下来咱观察重试成功和重试失败分别都有哪些不同的表现？ OK 同学们，咱抄起家伙 intelligi 走起，编程是我快乐 996 是我的福报。


咱今天这个 topic 文件夹下又要添新丁了，随便复制一个topic ，咱给它先创建一个新的专门处理异常重试的topic ，就给它起名叫 error topic 好了，那这个 topic 的 input 和output ，咱给它改一个名字，不要叫 delay consumer 了，叫 error consumer 然后还有 error producer 那添加完了 topic 以后，咱就要去创建 controller 里的方法了，我们移步到 controller 当中。首先咱要把刚才创建的这个 topic 给它在这里 out wired 进来，加上它的名字叫eratopic。 Eratopic ok. 变量名，就给它起名叫 eratopic producerok 我们可以滚啦往下滚滚到这。好，那这里复制之前的一个方法，然后把它添加到这里，来改一下上面的注释。


这个示例应该是叫异常重试，括弧单击重试叫单机版。为什么叫它单机版呢？因为咱这次的异常重试它只会在本机重试，也就是说是在 consumer 这个范围内的重试。咱接下来在后面还会学习那种联机对战的异常重试策略。 OK 那咱这个单机版给它把方法 controller 的名称给它改为 sand error message。 Okay. 同样发送 message 的方法，咱不直接发送body ，咱也发送个 big 好了，把这个 producer 大家记得要改成 error topic 前面有的同学问我就是他的 delay Q 怎么都不起作用。


后来排查下来发现为什么他发送消息的时候，这里忘了把 delay 的 producer 替换过来了，他还是发到原先的 group topic producer 所以怎么发现老是不起作用。那同学们也要注意在这里 copy 抄作业的时候，别把名字也给抄错了这个名字咱要给它替换成 error topic producer 那还有其他要改动的吗？那就是方法的路径了，这个 HTTP 的路径叫 stand error 好了，改完路径以后，再把发送的消息体传入进去。


Message. OK 到这里就大功告成了，我们现在可以去修改 consumer 了，大家随我一步到 consumer 这里的consumer ，我们要动一动歪点子，给它故意抛错。但是这个抛错的姿势还有点特殊，我们看一下，先把这个 error topic 加到 annotation 上面，把这个信道绑定好。


OK 绑定完信道，咱把上面的一个 consumer 给它借鉴一下， copy 过来，然后注释改一下。咱是异常重试括弧还是单机版。他的 topic 也给替换成刚才创建的这个 error topic 方法名改成 consumer error message 这个 message 它传递过来的时候还不是 error 那我们要给它人造一个 error 怎么造呢？我们来开始搞破坏了。在创建 error message 之前咱要打一行 log 就是你这个 message 进来之前还是好的，进来之后就坏了。走着走着就瘸了。咱开始在他还脑袋清醒的时候给他打一行log。


Are you ok.这是谁的名言啊？雷布斯的名言对吧？ RU OK 完了以后，他听了这句话之后整个人就不好了，怎么不好的？咱打一个 if 先把它空在这整个人不好了，这里就要抛异常了，抛一个什么异常呢？咱 new 一个 runtime exception 然后 runtime exception 里面打上 IM not OK OK 光抛异常还不够，咱要打一行 log 这样待会儿方便查看异常情况。雷布斯问你了， are you okay 你怎么回答啊？你这行 log 怎么回答？你只能回答 whats your problem 这又是谁的名言。这句话在 19 年的时候蛮火的有一个专门为莆田系医院代言的企业老总在发布会现场被人头上浇了一瓶水，他这样说道。


Whats your problem.那咱犯了错，抛出一个 runtime exception 咱不怕，咱关键是要能把它改正过来，怎么改正？我们给他一个机会，给他一个纠错的机会。在这个 consumer 上面，咱定义这样一个类，他它叫 atomic integer 类型的，一个线程安全的变量。那给它起名叫计数器。Ok，atomic.它的起始值是谁？我们给它设置成 E 好了，起始值是 E 那这个计数器我们将要用在方法的改错上，怎么改错？我们来一个比较好玩的玩法。当你这个计数器每次运行到 consumer 方法的时候，你都要加一自增一。自增一了以后，如果你能被 3 整除，怎么办？我就放你过去，把你从错误异常中拯救回来，就说明这个消息被 consumer 消费成功了。那咱也打一行log ，人家又问了 are you OK 你怎么回答？咱教科书式的回答应该是 fine thank you 后面还有 and you OK 那咱一切恢复正常以后，接下来把计数器 count 给它清零 set 成0。就是说这个计数器只有能被 3 整除的时候才会成功消费这条消息。而且每次成功消费以后都会把它清零。


如果没有成功消费消息，下面就会 through 出这个异常，大家要记得加上through ，把这个异常抛出去，这里再跟大家多闲扯两句。咱从小学的这个教科书里面的回答其实都是很刻板很错误的。一般别人问你 how are you 或者 are you。Ok.我们不用回答这么啰嗦，直接回答 IM good 就可以了。或者比较熟悉的朋友就说 not bad 也可以说 same old same old 就是老样子了。


OK 那咱这边的 consumer 也已经配置完成了，接下来最后一步就是要修改配置文件，配置文件这里又有一个新的属性要引入进来，我们一起去看一下。打开 application DM properties 我们从上面 copy 这个延迟消息的配置，把它 copy 一下。这个 delayed exchange 不用 copy 了，咱只用 copy 前面的两行，然后把注释改一下，这是异常消息括弧单机版重试。好嘞，把消息的信道名称从 delay 的 consumer 改成 error consumer 并且它的 topic 我们把它定向到 error topic 叫 error out topic 好了， error out 就是出局犯错了。


OK 那这两个信息配置完，咱还有一个很关键的属性，它要配置什么呢？我们看，它要配置的是重试次数。也就是说当你 consumer 消费了这条消息以后，假如它在消费过程中抛出了异常，那么它最多可以重试几次。大家记住，这个重试是怎么样？是本机重试，它是在当前的 consumer 当中不断的重试消息，而不会把消息再重新发回给 rabmq 大家记住了，是在客户端消费者这里本机重试的，所以咱说它是一个单机版自娱自乐。那好这个属性它怎么配置呢？我们来看，它前面依然是 spring cloud stream bindings 然后后面跟是谁是 producer 还是 consumer 咱前面说了他是本机重试在消费者端，所以这里自然而然就是 consumer 了，consumer后面再跟一个 consumer 然后这里是关键的一个步骤 max attempt 就是最大常试次数，咱这里设置成几设置成1。


同学们觉得会生效吗？不会生效，因为为什么？ 1 相当于没有重试它消费这条消息的档次。其实就算是第一次了，那如果你想让它重试一次，那这里我们要配置成2。OK ，我这里注释再多加一句，次数等于 1 相当于不重试。 OK 咱的配置文件也已经改好了，那我们可以把项目启动起来看一下效果了。我们找到 stream application 直接把它跑起来，稍等那么半炷香的时间。然后我们去 postman 里尝试着调用方法，看一看它在出错和不抛出异常两种情况下，它的 log 上会有什么不同之处。


OK 这里已经启动好了，我们转战到 postman 里。好，在 postman 这里，我已经创建好了一个 URL 这个 URL 是采用 post 然后 post 到哪里呢？咱的端口63,002，其中的 controller 方法是 send error 好，我们尝试调用。


第一次。走。你好，第一次调用已经发起了，我们回到 lock 里面看一下。OK ，我们看这个 log 轨迹，同学们看，它第一次调用就是这一行。 are you OK 然后走进了哪里，走进了异常方法里。 Whats your problem.但是大家注意到没有异常方法咋扔出了一个 runtime exception 到哪里去了？是不是没有打印出来啊？那为什么它没有打印出来呢？同学们，我们接下来往下看，你看这边是不是有一个重试 are you okay 它是我们的第一次重试。在这次重试过后，它打印出了一行 log fine thank you 那说明重试成功了，大家有没有得出一个结论，如果你在重试过程中抛出了异常，假如经过咱消费者的不断重试，这条消息最终被成功消费了。那么这个异常是不会抛出的， stream 会把它抑制住，甚至这个异常都完全不会出现在咱的 lock 当中。


那既然这次消息被成功消费了，它的计数器应该归零了，对不对？那我们再尝试调用一下。 OK 我们回到 postman 里，点击 send 再回来看一下它出现什么log 。这里已经看到有异常了，我们往上看走到接收方法的地方。第一行同样一句 ruk 接收到了第一次方法，然后走到了异常逻辑。此时的计数器数值应该是几啊？应该是一对不对？由于我们配置了最大常试次数为2，那最大次数为2，代表着重试次数为1，所以它进行了第二次的本地重试。那在第二次重试完了以后，它依然走到了错误逻辑里面。因为咱的计数系数值在这里变为了2，依然不能被 3 整除。所以它这里抛出了异常。那么往下看，这个异常就被打印到了 log 里面。也就是说抛到了最外层。那么从这个现象里咱可以看出，如果你的消息经过不断的重试，最终在重试次数用完了以后依然不能被成功消费。那么 stream 就忍无可忍，无需再忍了，把你的错误一查，全部一股脑抛到最外层，这里在 lock 中也会有所体现。


OK 同学们到这里，咱这一小节的 demo 就结束了，我来带大家稍微回顾一下本节的几个重点。在这一节当中，我们创建了一个新的 topic 并且在 consumer 里故意抛出了一段异常，验证它的异常处理流程。然后它最关键的一点实际上是在 application properties 中的配置。咱这里引入了一个新的配置项，也就是说最大尝试次数。那这里强调一点，当咱的 consumer 对消息进行第一次消费的时候，实际上他已经尝试了一次了。也就是说如果我们想让它失败之后多尝试一次，那么这里应该配置成 1 加 1 等于2。同理如果重试两次，那这里就应该配置成3。那么以上内容就是基于 consumer 的单机版重试的全部内容了。在接下来的小节里，我将带大家去解锁更多的异常重试策略，把异常重试的玩法从单机版升级为联机版。 OK 同学们，那我们接下来的课程里再见。


