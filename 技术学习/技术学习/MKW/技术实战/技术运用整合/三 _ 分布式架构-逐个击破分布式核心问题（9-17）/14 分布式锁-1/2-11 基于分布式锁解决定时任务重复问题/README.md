---
title: 2-11 基于分布式锁解决定时任务重复问题
---

# 2-11 基于分布式锁解决定时任务重复问题

[image](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/ff3f25f6-c32c-4a27-ae21-dfe2eee47372/SCR-20240807-jvaz.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WQY6X7TK%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T225345Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQD%2B1bIm7QFFxjar%2Bn92p0e2G1UXZu6sql52logMgImQhwIhALtJQxlkzQhKxtxJqlRaFZPyDQ13KlyxK9w8IfXmzG34KogECMb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgzqnFAvVDpd7%2FwEM18q3ANeFBkISII9yJhnUK8M89%2BqZdSmzExvvvw6lr4dbeCZyOyV7%2FAr2V0P1bX92lmyw91xRYvsCSVwhb0L%2BwiV39i0JmdHPJLf0TgMwMjT2UgE3nM0z2DR4ZGKhTSjABkrvyIOzwNbnSJBfQe5dCcVoPIMpOx5qX5da8rGUaPKZlBUtm%2F%2Fw6ksOljcByuc96KVHlA5iJxr4wHqSnhW%2Bh1qACTlpjU0%2FJL7wYuAtO1kRJK5YMqQIKUDU4D5MmAG%2BPBs94NTe7i8o7NSE1yV437oZtbunBStD0N7W6%2BPTnGnhJP3OwhtGR0WH3z49akPVCCrlgh2gC3O%2B5%2B7ejGdWO%2Bs9voYfrrxbeQ0U6zd%2FnstBNpRAXIgqBfr2x0cuHLFRnPmNdJGb1mFP7NKbdKlTR38L90zs9EB2ZDruOL3bFChgrjKPyuQQknOqK4A%2BWDIUr9wzJoxFD69XyR4t%2B707dF2fiUYfRyyQcmicSd13itaOuz1vA%2F6ujMWCCXy3uSewWEn3vUOCPj4KAUbjm55CYhzr%2Bf8GbAAj%2F%2FlvWDps1DC9DSUtStM4SWck%2BcIoZTWACn4wcffx8VMN3c96gSkkDkv9tqhYCQByyo6oa%2F9BYIkjALqRLUzuSW%2B%2F7zGIHCElDCcuv%2FSBjqkAQSEfnhTudxWZnI3%2BOqBRlYejD3WalWQgTHJQv%2BP4ZYSpfusPblqYsQ6foJ6VIvgdzp4FBS%2B5kckRNZAllnHIM96jtMad65P7%2BWzMI1p4D8vZe7rWxMxgiW4t%2Bj3n%2FrCX42qEcBBhywyzIq420RHdvyGQ%2FhpVxB9uAzhCt6Hm0Bo5gfcnkTkomUSTXfNq4jYWIduEmDj3dWTcbYGDnai5AKDRDQU&X-Amz-Signature=e52b1907e45b5ed5a1ccd2d3f7bc00887496caaeff3c0420b281bd8c9047b513&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

[image](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/98ae57ff-b49f-4f8e-98f8-b5d44972848c/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WQY6X7TK%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T225345Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQD%2B1bIm7QFFxjar%2Bn92p0e2G1UXZu6sql52logMgImQhwIhALtJQxlkzQhKxtxJqlRaFZPyDQ13KlyxK9w8IfXmzG34KogECMb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgzqnFAvVDpd7%2FwEM18q3ANeFBkISII9yJhnUK8M89%2BqZdSmzExvvvw6lr4dbeCZyOyV7%2FAr2V0P1bX92lmyw91xRYvsCSVwhb0L%2BwiV39i0JmdHPJLf0TgMwMjT2UgE3nM0z2DR4ZGKhTSjABkrvyIOzwNbnSJBfQe5dCcVoPIMpOx5qX5da8rGUaPKZlBUtm%2F%2Fw6ksOljcByuc96KVHlA5iJxr4wHqSnhW%2Bh1qACTlpjU0%2FJL7wYuAtO1kRJK5YMqQIKUDU4D5MmAG%2BPBs94NTe7i8o7NSE1yV437oZtbunBStD0N7W6%2BPTnGnhJP3OwhtGR0WH3z49akPVCCrlgh2gC3O%2B5%2B7ejGdWO%2Bs9voYfrrxbeQ0U6zd%2FnstBNpRAXIgqBfr2x0cuHLFRnPmNdJGb1mFP7NKbdKlTR38L90zs9EB2ZDruOL3bFChgrjKPyuQQknOqK4A%2BWDIUr9wzJoxFD69XyR4t%2B707dF2fiUYfRyyQcmicSd13itaOuz1vA%2F6ujMWCCXy3uSewWEn3vUOCPj4KAUbjm55CYhzr%2Bf8GbAAj%2F%2FlvWDps1DC9DSUtStM4SWck%2BcIoZTWACn4wcffx8VMN3c96gSkkDkv9tqhYCQByyo6oa%2F9BYIkjALqRLUzuSW%2B%2F7zGIHCElDCcuv%2FSBjqkAQSEfnhTudxWZnI3%2BOqBRlYejD3WalWQgTHJQv%2BP4ZYSpfusPblqYsQ6foJ6VIvgdzp4FBS%2B5kckRNZAllnHIM96jtMad65P7%2BWzMI1p4D8vZe7rWxMxgiW4t%2Bj3n%2FrCX42qEcBBhywyzIq420RHdvyGQ%2FhpVxB9uAzhCt6Hm0Bo5gfcnkTkomUSTXfNq4jYWIduEmDj3dWTcbYGDnai5AKDRDQU&X-Amz-Signature=221b39967c5fa354c397a0e259a07c06039a976ee843bc6e16eea7d184544808&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

[image](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/20a1e131-d7fb-4baf-8227-736bfe6a4582/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WQY6X7TK%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T225345Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQD%2B1bIm7QFFxjar%2Bn92p0e2G1UXZu6sql52logMgImQhwIhALtJQxlkzQhKxtxJqlRaFZPyDQ13KlyxK9w8IfXmzG34KogECMb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgzqnFAvVDpd7%2FwEM18q3ANeFBkISII9yJhnUK8M89%2BqZdSmzExvvvw6lr4dbeCZyOyV7%2FAr2V0P1bX92lmyw91xRYvsCSVwhb0L%2BwiV39i0JmdHPJLf0TgMwMjT2UgE3nM0z2DR4ZGKhTSjABkrvyIOzwNbnSJBfQe5dCcVoPIMpOx5qX5da8rGUaPKZlBUtm%2F%2Fw6ksOljcByuc96KVHlA5iJxr4wHqSnhW%2Bh1qACTlpjU0%2FJL7wYuAtO1kRJK5YMqQIKUDU4D5MmAG%2BPBs94NTe7i8o7NSE1yV437oZtbunBStD0N7W6%2BPTnGnhJP3OwhtGR0WH3z49akPVCCrlgh2gC3O%2B5%2B7ejGdWO%2Bs9voYfrrxbeQ0U6zd%2FnstBNpRAXIgqBfr2x0cuHLFRnPmNdJGb1mFP7NKbdKlTR38L90zs9EB2ZDruOL3bFChgrjKPyuQQknOqK4A%2BWDIUr9wzJoxFD69XyR4t%2B707dF2fiUYfRyyQcmicSd13itaOuz1vA%2F6ujMWCCXy3uSewWEn3vUOCPj4KAUbjm55CYhzr%2Bf8GbAAj%2F%2FlvWDps1DC9DSUtStM4SWck%2BcIoZTWACn4wcffx8VMN3c96gSkkDkv9tqhYCQByyo6oa%2F9BYIkjALqRLUzuSW%2B%2F7zGIHCElDCcuv%2FSBjqkAQSEfnhTudxWZnI3%2BOqBRlYejD3WalWQgTHJQv%2BP4ZYSpfusPblqYsQ6foJ6VIvgdzp4FBS%2B5kckRNZAllnHIM96jtMad65P7%2BWzMI1p4D8vZe7rWxMxgiW4t%2Bj3n%2FrCX42qEcBBhywyzIq420RHdvyGQ%2FhpVxB9uAzhCt6Hm0Bo5gfcnkTkomUSTXfNq4jYWIduEmDj3dWTcbYGDnai5AKDRDQU&X-Amz-Signature=37352d606132fe9fbab23d797a3e52d3eb166809c52e09105b40bf8a0a05486d&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

咱们已经通过代码实现了 Redis 的分布式锁。然后咱们要从一个项目当中的实战案例去使用这个分布式锁解决一下这个定时任务集群部署的问题。如果你的定时任务使用 course 或者 elected job ，这个集群部署是没有问题的。那么比如说你的项目当中定时任务只是简单的使用了 spring task 那么你集群部署的时候就会出现任务重复执行的问题。那么咱们怎么解决就是使用分布式锁来解决这个重复执行的问题。咱们看一下整体的架构图。

[image](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/a876bf78-6d15-46a3-8147-ed713dfa0e6b/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WQY6X7TK%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T225345Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQD%2B1bIm7QFFxjar%2Bn92p0e2G1UXZu6sql52logMgImQhwIhALtJQxlkzQhKxtxJqlRaFZPyDQ13KlyxK9w8IfXmzG34KogECMb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgzqnFAvVDpd7%2FwEM18q3ANeFBkISII9yJhnUK8M89%2BqZdSmzExvvvw6lr4dbeCZyOyV7%2FAr2V0P1bX92lmyw91xRYvsCSVwhb0L%2BwiV39i0JmdHPJLf0TgMwMjT2UgE3nM0z2DR4ZGKhTSjABkrvyIOzwNbnSJBfQe5dCcVoPIMpOx5qX5da8rGUaPKZlBUtm%2F%2Fw6ksOljcByuc96KVHlA5iJxr4wHqSnhW%2Bh1qACTlpjU0%2FJL7wYuAtO1kRJK5YMqQIKUDU4D5MmAG%2BPBs94NTe7i8o7NSE1yV437oZtbunBStD0N7W6%2BPTnGnhJP3OwhtGR0WH3z49akPVCCrlgh2gC3O%2B5%2B7ejGdWO%2Bs9voYfrrxbeQ0U6zd%2FnstBNpRAXIgqBfr2x0cuHLFRnPmNdJGb1mFP7NKbdKlTR38L90zs9EB2ZDruOL3bFChgrjKPyuQQknOqK4A%2BWDIUr9wzJoxFD69XyR4t%2B707dF2fiUYfRyyQcmicSd13itaOuz1vA%2F6ujMWCCXy3uSewWEn3vUOCPj4KAUbjm55CYhzr%2Bf8GbAAj%2F%2FlvWDps1DC9DSUtStM4SWck%2BcIoZTWACn4wcffx8VMN3c96gSkkDkv9tqhYCQByyo6oa%2F9BYIkjALqRLUzuSW%2B%2F7zGIHCElDCcuv%2FSBjqkAQSEfnhTudxWZnI3%2BOqBRlYejD3WalWQgTHJQv%2BP4ZYSpfusPblqYsQ6foJ6VIvgdzp4FBS%2B5kckRNZAllnHIM96jtMad65P7%2BWzMI1p4D8vZe7rWxMxgiW4t%2Bj3n%2FrCX42qEcBBhywyzIq420RHdvyGQ%2FhpVxB9uAzhCt6Hm0Bo5gfcnkTkomUSTXfNq4jYWIduEmDj3dWTcbYGDnai5AKDRDQU&X-Amz-Signature=cfa2b16fa05cf987548aa22de4bdafc1eb93a616ed5fae532101ac3306d27b51&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

咱们可以看到这个定时任务服务是部署了两台，然后某一时刻任务 A 开始执行，由于你部署了两台，那么等于是同时运行了两个任务 A 那么这个时候任务 A 执行的就重复了。比如说咱们写了一个定时任务给某些用户定时的去发送短信，当你部署一台的时候是没有问题的，到了这个时间点就会给这个用户发送短信。那么如果你集群部署了两台，那么到了这个时间点了，会有两个任务开始执行，都给那一个用户去发送短信。


那么这个时候这个短信就发了两条对吧？那么我们怎么解决这个问题？用分布式锁在任务执行之前都去获取这个锁，哪个服务获得到了这个锁哪个服务去执行这个任务 A 没有获得锁的服务这个任务 A 就直接 return 了直接返回。我们就是通过这种方式去解决这个定时任务重复执行的这个问题。


好，咱们回到代码，咱们先看一看前面咱们写的这个 Redis 的分布式锁的这个例子，咱们看看这么长的一段代码，你分布式锁占的代码有多少，咱们看一下，从这个 stream key 开始一直往下一直到获取分布式锁。这一大段都是和业务内容没有关系的。然后后边 finally finally 里边写的都是释放锁的步骤，也和你的业务代码没有关系。咱们真正的业务代码只有这一小段，通过线程休眠模拟了一下业务的执行。那么有的同学可能就发现了，如果我使用 Redis 的这个分布式锁，我要写这么一大段和业务没有关系的代码。然后这个时候对于开发人员来说比较的啰嗦。那么咱们就要想一想了，能不能把 Redis 分布式锁给它封装一下。然后我们使用起来就会比较的方便，也不用每一个业务都写这么长一大段代码，开发效率比较低。好。那么咱们现在就给它封装一下，咱们再新建一个目录叫做 lock 然后再新建一个类叫做 Redis lock 咱们看一下封装这个类怎么封装。首先这个类要有获取锁的方法，然后还有一个释放锁的方法。那么这个获取锁和释放锁都使用到了 Redis template 所以咱们这个 Redis lock 里边先要写一个变量，叫做 Redis template 然后还有什么咱们看一下是吧，这个 key 是根据你不同的业务设置不同的值，不会像咱们这样直接写死。


所以这个 key 也是一个变量，private string key 对应 key 是 value value 咱们用不用把它作为一个变量传进来，这个是不用的，因为这个 value 是用 UUID 是吧，保证所有的线程传的这个 y6 都是不相同的。


如果你要是通过电量把它暴露出去，那么有可能在使用锁的这个开发人员不理解这块内容的东西，它传了一个固定的值，那么你的这个 Redis 锁就是有问题的。所以咱们这块这个 value 是不会暴露给，是不会向外暴露的。但是咱们这块也是先，写一个 value 然后咱们通过构造方法给这些变量赋值，咱们再看看有没有其他的变量。还有一个过期时间，过期时间咱们这里边写死了，是 30 秒。那么如果你要封装成一个类的话，你要给其他的人员去提供。那么这个时间还是让开发人员自己设置为好，因为他可能是写，不同的业务你的过期时间设置也不相同。所以这个过期时间咱们还是要暴露出去。


create 然后 int expire time 是吧。过期时间，这个咱们加个备注，单位是秒。好，咱们这个变量就已经写完了，看看有没有漏的，这个 NX 咱们就不用作为变量了，因为都都是这个 NX 操作。好，咱们现在写这个构造方法， public Redis lock 然后 Redis template 一个，然后 string key 最后 int expire timevalue 咱们是不会通过构造函数暴露出去的。然后第四点， registtemplate 等于 registtemplate 这次点儿 key 等于 key 这次点儿 expare time 等于 expire time 最后咱们要给这个 value 生成一个 UUID 虽然并没有暴露出去，并没有让开发人员去传这个值，但是咱们这个类自己要去生成那个值，uuid.random [uuid.to](http://uuid.to/) string 好，这样这四个关键的参数咱们就已经写好了。


然后咱们要写这个获取锁的方法 public 布尔 get lock 然后里边咱们写什么内容呢？就写这一段咱们给它复制过来，把这一段获取锁的内容给它复制进来，咱们看一下过期时间就不能写死了。写咱们的 expare time 然后 key value 都没有问题，最后执行获取锁的这个操作。最后给它 return return lock 咱们把注释给它加一下获取分布式锁，然后释放对吧。


同样 public 布尔 unlock 咱们也是仿照可重入所的那个方法命名 unlockunlock 咱们还是把前面的这一段给它复制过来，最后把这个结果给它返回，这样就没有问题了对吧，咱们还是试一下，咱们做个测试。前面的这一段咱们都不要这块儿 Redis 写个 Redis lock 等于 new Redis lock 然后里边传参数。第一个参数 Redis template 第二个参数， key 是吧， key 咱们还是用 Redis key 最后时间 30 这块儿咱们调用 Redis lock 点儿 get lock 获取锁，后边 finally 咱们也不用了， Redis lock.unlock 前面用变量接一下，这样咱们代码就简洁多了。


咱们看一下现在的代码就是创建了一个 Redis lock 的这么一个对象，传入了这个 key 的值，过期的时间。最后获取锁，释放锁，代码非常的简洁。咱们启动一下，启动一下服务，然后运行一下，看看有没有错误。咱们还是在 8080 这个端口启动好没有问题，咱们打开浏览器访问一下 8080 端口的请求。讲一下。
回车看看后台的日志，我进入了方法，我进入了锁，没有问题，再看看释放锁的过程，等待 15 秒释放，结果也是正常的，没有问题。看来咱们这个 Redis 封装是没有问题的。那么有的同学可能会问了，这块你所有写 try cache 的地方都要有一个 Redis unlock 但是有的同学可能就会说了，我写代码习惯可能不好，经常是忘了释放这个步骤。比如说关闭流的一些操作，我经常的忘记，那我怎么办呢？而且有的同学也可能说了，从 gdk 1.7 以后， gdk 官方是提供了自动关闭的这么一个功能，包括你的流是吧，HTTP client 都提供了自动关闭的这么一个功能。那么你的这个 Redis lock 威蒂斯锁能不能也提供一下自动释放锁的这个方法，其实是可以的，这个需要咱们把这个 Redis lock 给它改造一下这块。


可能有的同学不知道，这个自动关闭是 Redis 1.7 这个版本推出的，只需要咱们的类去实现凹凸 close able 这么一个接口，大家还是要多多的关注一下 gdk 官方的这个每一个版本的变化。比如说现在已经出到了 gdk 12 了是吧，那么它每一个版本它都有哪些更新呢？这个咱们都需要关注一下。尤其是在语法上。比如说 gdk 1.8，他出了拉门的表达式，你不能说只是知道了说这机配已经出到了哪一个版本。而且可能有的同学可能也炫耀我们这个项目使用的 gdk 的版本是 gdk 11， gdk 12。但是你的项目当中你真正用到了它的哪些特性呢？这个你可能并没有使用。那么你就等于使用了 gdk 1.5，1.4之前的版本是一样的。所以新的特性咱们要关注一下，而且在项目当中积极地去使用这些特性。
像 JDK 1.7 推出的这个 auto close able 咱们这块这个类要实现一下这个方法，实现 close 方法。在这个 close 方法里边咱们直接调用 unlock 就可以了。然后咱们这一块释放锁这个 final 类咱们就不用写了。但是这个 try catch 咱们也要改一下。这里边我写一下这个写法，看看大家见没见过，然后获取锁咱们就要在这个摔 cache 里边去执行了。我改造完了，大家看一下。这么写大家见过没见过，大家看看这个塞开始没见过，直接在踹后边加一个括号。这样的写法没见过？大家写 try 开始一般都是 try 然后直接就跟着大括号了。我这样的这种写法就是 JDK 1.7 以后这个新的特性所支持了这种写法，我直接在 try 里边加上了这个 Redis lock 这样在方法结束的时候会自动的去释放这个锁。咱们在这个 unlock 里边咱们加个日志，把之前释放锁的这个日志打到这个 unlock 里边来，咱们还是用这个劳动部我提供的这个方便的写法。这块儿 log 点儿 infer 释放锁是吧的结果。Without。这么写，咱们再重新运行一下。好，启动没有问题，咱们访问一下 8080 这个端口，咱们请求一下看看打印的日志。进入锁没有问题是吧，那么等待 15 秒钟，看看它释放锁的这个过程没有问题。这个乐迪斯 lock 里边这个日志也已经打印出来了，看来咱们的写法是没有问题的。那么这样就解决了这个有一些同学可能会忘记释放锁的这么一个过程，咱们只需要在 try 开始的时候这样写就可以了。好，这个 Redis 锁咱们也已经封装完成了。


下面咱们看看这个 spring taskspring task ，咱们要在这个启动类上面加上一个注解，叫做 enable scheduling 可以使用这个定时任务，也不需要引什么，像cos 、 elastic job 这些加班都不需要引。只要你使用了 spring boot 这个项目，你加上这个注解就可以使用定时任务。


然后咱们再创建一个service ，创建一个服务，新建一个包到 service 在这里边建一个 scheduler scheduler service 打一个注解 service 然后写一个方法叫做 public void sand SMS 发送短信。这么一个方法。这里边咱们就打印一下日志就可以了。落个点 infer 像 1381234 是吧叉叉 8 个叉向他发送短信。这个短信咱们是短信，咱们每 5 秒钟执行一次，这个扩张表达式就不给大家做介绍了，非常的基础，一共 6 位。现在咱们看一下，如果我不加分布式锁，咱们启动两个服务。现在 8080 这个服务重启一下，咱们先看看能不能。打印出来了，5秒钟执行一次，又打印出来了。现在咱们再把 8081 这个端口的服务再启动一下看到 45 分 20 秒，像 138 什么什么这个发送短信 45 分 20 秒 25 秒。咱们来看看 8080 这边的服务，45分 20 秒 25 秒也向这个手机发送了一条短信。那么这样两个服务就发送重了。


下面咱们用分布式锁解决这个重复发送的这个问题，咱们把服务先停一下。那么咱们在这个任务执行之前，在这里边先获取一下这个分布式锁哪个服务获取到这个分布式锁哪个服务执行下边的内容，咱们也是用这个 try catch 这种写法。


Redis lock 等于 new Redis block 咱们先把这个 Redis template 给它注入进来。下个 auto wire 第一个参数传入 Redis template 然后这个 key key 和业务相关，咱们随便起一个，叫做 all to SMS 过期时间也传一个30，30秒过期，然后加个 catch 在这里边 if Redis lock.get lock 获得到了锁，然后执行发送短信。这个咱们也不用手动关闭了，它会自动的去释放这个锁。咱们再执行一下，运行一下这个 8080 这个端口的服务，看看正常运行是没有问题的。释放锁也已经打印出了日志，咱们再把 8081 这个服务再启动一下。咱们对比的看一下两边的这个服务咱们都停一下，看一下时间，咱们找一个 20 秒的。 20 秒 8081 这个服务发送了短信，咱们来看巴婷巴婷这边。 20 秒的时候释放锁的结果等于 false 并没有打印出这个日志。这个 false 是什么意思呢？就是说你在 get lock 的时候没有获得到锁是吧？没有获得到锁以后，这一段内容就执行完了。 trackedge 已经结束了，结束以后它会自动的走。这个 close 方法合作的方法就是释放锁，你没有获取到锁的时候，你又去释放了锁，那结果肯定是返回 false 咱们再看看 25 秒，30秒，35秒，080这个服务都没有发送短信，再看看八零八一二十五秒，30秒，35秒都发送了短信。那么这个就说明什么咱们的分布式锁是有效果的。而且解决了这个使用 spring task 部署定时任务集群服务的时候，这个重复发送的问题。


那么好本节课的内容就全部给大家介绍完了，咱们还是快速的回顾一下。首先是这个 Redis 分布式锁的这个原理，咱们使用的是 Redis 的 set NX 。这个特性当你给一个 key 去赋值的时候，如果这个 key 存在对吧，如果这个 key 存在，那么赋值是不成功的。如果这个 key 不存在，那么赋值是成功的。咱们就是利用了 Redis 的这个特性来实现咱们的分布式锁。那么体现到程序当中，咱们这里边用到了 spring 给咱们提供的这个 Redis template 去实现分布式锁，并且已经给它封装成了一个比较完整的 Redis 锁，这么一个类可以供大家使用。随后咱们还使用 Redis 分布式锁，解决了定时任务集群部署的问题。这一章的内容还是挺多的，大家还要仔细的去消化。尤其是要理解 Redis 分布式锁，它的原理是什么，掌握了它的原理，咱们就可以自己去实现 Redis 的分布式锁。


如果大家感兴趣的话，课下可以使用另外一个 Redis 的客户端去实现这个分布式锁。在咱们的例子当中，使用到了 Redis template 它是 spring date 给咱们提供的，同学们还可以使用其他的客户端，比如比较流行的像 Jessie 我不通过 spring 我直接用 Jessie 我怎么封装成这么一个分布式锁，这个大家感兴趣的话，课下可以多多的练习好这一节的内容，就给大家介绍到这儿。下一节要给大家介绍如何使用组 keeper 去实现分布式锁。好，谢谢大家。

