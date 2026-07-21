---
title: 3-11 【源码品读】服务注册源码探秘-2 
---

# 3-11 【源码品读】服务注册源码探秘-2 

[image](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/1056f88e-da61-448c-b108-5df4e14765b7/SCR-20240717-drgv.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WK6AOVKQ%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T225541Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIA26fHa0CEU6DlK4%2FOoJzz2DjBlypcOTTGo5SbwBPSruAiEA9GJ9G6Ql7kyEeI3hGt1P97bUkbRFFe8lewqnEdDV5AkqiAQIxv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDDB60sYevbPi7O8JXSrcA6ahFVP0FvQGIvJnD0mDJbNrfgZVX2R%2FKFuYWtAjQRJsnUJ9XfbdeW4gywiQRXAmGbabUVPvj8zHMFGnb8fAA54564NbRRhRzzGfJY2FU2lNMjad9uVcUDRMblJEum%2B1T0X%2B7DqHDxrFX%2BLkEdz0gK1Nyy3Fl54hRo0D%2BklaI2xGP0vX8GqIpdjJeMKH1i%2BImjCVcZNYhpsh%2FMXP4%2BT7aWkZA4tffgarylP6zU6RK8quPnaS%2FjtEXm%2Bxlia707GJAmDd2327CbAKi35VisqO%2Bdq1Ti1eFG9DD3cTS0VeUqSCruIg%2BJuo4FvxqTRnpaPuAMjdPLfPR2kkNqi3%2FaDmK6YUR1D41gWByfZPB%2FuDZTuQHv%2BlfbVdZVwLVU5WUKyFil7MyTrayx1uXSa4tSkl8G2hBORF7HEdnp8t0JCZ5F4T6Sf75rgoj4GUsA1CijSnBgr1Go6MbGQntQXnmIIA48bKV7LFky%2B1gkSflmcyGW%2BK1xnxpDzWCS6ngre23N%2FlX1ZWqyvkcr6w%2F9ykHFY5uYnA7aUFjw9AqdVFwOupqNkKJEbiYEtvy5HtgG2bdt%2BGMhd6jVg2UBpztcRmwmfBVEvFEb91276h%2BoE8R%2FDoXvCAK8HVYIetl2khYw3TMJy6%2F9IGOqUBL48NQ3pH5VTMQeEskncAVNSC%2FDAGsxPpYy%2BcfyCxZg2BaTUqE76Rk3Kr3mpwRa6epnaSWPiXu1pe%2BBMcivN2fQvr1%2BQbX67YIzA7fvCN0n6%2BNv%2Fpf0VxUR6SCO9u1kcRlDB8%2BmY7AzBpSfZ1EGhq%2BBCaFV%2BIH%2FfHn2DhXL7s%2FYNQ08Nn94%2BjESIyb8QCHWhn1xMQF3OdYVk4IdmrvnZJhEm5l2Nb&X-Amz-Signature=3786d1a59f7804ed1368bc88b22cd5881ad2a5141479bd614da5277a92f9d390&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

[image](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/07a11663-1957-408d-92e6-168dde68b77d/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WK6AOVKQ%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T225541Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIA26fHa0CEU6DlK4%2FOoJzz2DjBlypcOTTGo5SbwBPSruAiEA9GJ9G6Ql7kyEeI3hGt1P97bUkbRFFe8lewqnEdDV5AkqiAQIxv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDDB60sYevbPi7O8JXSrcA6ahFVP0FvQGIvJnD0mDJbNrfgZVX2R%2FKFuYWtAjQRJsnUJ9XfbdeW4gywiQRXAmGbabUVPvj8zHMFGnb8fAA54564NbRRhRzzGfJY2FU2lNMjad9uVcUDRMblJEum%2B1T0X%2B7DqHDxrFX%2BLkEdz0gK1Nyy3Fl54hRo0D%2BklaI2xGP0vX8GqIpdjJeMKH1i%2BImjCVcZNYhpsh%2FMXP4%2BT7aWkZA4tffgarylP6zU6RK8quPnaS%2FjtEXm%2Bxlia707GJAmDd2327CbAKi35VisqO%2Bdq1Ti1eFG9DD3cTS0VeUqSCruIg%2BJuo4FvxqTRnpaPuAMjdPLfPR2kkNqi3%2FaDmK6YUR1D41gWByfZPB%2FuDZTuQHv%2BlfbVdZVwLVU5WUKyFil7MyTrayx1uXSa4tSkl8G2hBORF7HEdnp8t0JCZ5F4T6Sf75rgoj4GUsA1CijSnBgr1Go6MbGQntQXnmIIA48bKV7LFky%2B1gkSflmcyGW%2BK1xnxpDzWCS6ngre23N%2FlX1ZWqyvkcr6w%2F9ykHFY5uYnA7aUFjw9AqdVFwOupqNkKJEbiYEtvy5HtgG2bdt%2BGMhd6jVg2UBpztcRmwmfBVEvFEb91276h%2BoE8R%2FDoXvCAK8HVYIetl2khYw3TMJy6%2F9IGOqUBL48NQ3pH5VTMQeEskncAVNSC%2FDAGsxPpYy%2BcfyCxZg2BaTUqE76Rk3Kr3mpwRa6epnaSWPiXu1pe%2BBMcivN2fQvr1%2BQbX67YIzA7fvCN0n6%2BNv%2Fpf0VxUR6SCO9u1kcRlDB8%2BmY7AzBpSfZ1EGhq%2BBCaFV%2BIH%2FfHn2DhXL7s%2FYNQ08Nn94%2BjESIyb8QCHWhn1xMQF3OdYVk4IdmrvnZJhEm5l2Nb&X-Amz-Signature=328f49b862e05d2e894dfac2b8ab3050717e50d7c64cc086fc5fcd0f46333309&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

下来我们看这个类的名称叫什么叫 decorator 一个装饰器。那我们现在就插播一条广告，就是先来介绍一下 decorator 装饰器还有代理模式究竟是什么东西，代理模式这个大家都非常熟悉了，一变而过有一个接口层对不对？

[image](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/c7770474-0e5f-418f-a5ae-92ff19d30b28/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WK6AOVKQ%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T225541Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIA26fHa0CEU6DlK4%2FOoJzz2DjBlypcOTTGo5SbwBPSruAiEA9GJ9G6Ql7kyEeI3hGt1P97bUkbRFFe8lewqnEdDV5AkqiAQIxv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDDB60sYevbPi7O8JXSrcA6ahFVP0FvQGIvJnD0mDJbNrfgZVX2R%2FKFuYWtAjQRJsnUJ9XfbdeW4gywiQRXAmGbabUVPvj8zHMFGnb8fAA54564NbRRhRzzGfJY2FU2lNMjad9uVcUDRMblJEum%2B1T0X%2B7DqHDxrFX%2BLkEdz0gK1Nyy3Fl54hRo0D%2BklaI2xGP0vX8GqIpdjJeMKH1i%2BImjCVcZNYhpsh%2FMXP4%2BT7aWkZA4tffgarylP6zU6RK8quPnaS%2FjtEXm%2Bxlia707GJAmDd2327CbAKi35VisqO%2Bdq1Ti1eFG9DD3cTS0VeUqSCruIg%2BJuo4FvxqTRnpaPuAMjdPLfPR2kkNqi3%2FaDmK6YUR1D41gWByfZPB%2FuDZTuQHv%2BlfbVdZVwLVU5WUKyFil7MyTrayx1uXSa4tSkl8G2hBORF7HEdnp8t0JCZ5F4T6Sf75rgoj4GUsA1CijSnBgr1Go6MbGQntQXnmIIA48bKV7LFky%2B1gkSflmcyGW%2BK1xnxpDzWCS6ngre23N%2FlX1ZWqyvkcr6w%2F9ykHFY5uYnA7aUFjw9AqdVFwOupqNkKJEbiYEtvy5HtgG2bdt%2BGMhd6jVg2UBpztcRmwmfBVEvFEb91276h%2BoE8R%2FDoXvCAK8HVYIetl2khYw3TMJy6%2F9IGOqUBL48NQ3pH5VTMQeEskncAVNSC%2FDAGsxPpYy%2BcfyCxZg2BaTUqE76Rk3Kr3mpwRa6epnaSWPiXu1pe%2BBMcivN2fQvr1%2BQbX67YIzA7fvCN0n6%2BNv%2Fpf0VxUR6SCO9u1kcRlDB8%2BmY7AzBpSfZ1EGhq%2BBCaFV%2BIH%2FfHn2DhXL7s%2FYNQ08Nn94%2BjESIyb8QCHWhn1xMQF3OdYVk4IdmrvnZJhEm5l2Nb&X-Amz-Signature=1a1504f651b77abdbe87be58e89d7a6bb94578bee443ab26b2baebcb17058c36&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

一个委托代理，那同时继承了同一个接口，当我方调用这个接口的时候，实际上是委托给代理类来进行调用的，对不对？非常简单，我们直接过好第二段广告装饰器模式同样的有一个新的接口叫 draw decorator 那它有三个实现，分别是 red decorator arrow decorator 和 clear UI decorate 这三个实现，它可以通过某种形式相互注入，怎么这样注入呢？我们接着往下看。
一个调用方调用的时候在我声明戴克瑞特的时候，比方说我可以把一个新的戴克瑞特通过构造器注入到当前戴克瑞特中间。那这样做有什么作用呢？也就是说比方我的 draw decorator 定义的一个方法叫 draw 对不对？那我每一个 decorator 都有自己特殊的行为，red decorator 给它描绘成红色，那 clear UI decorator 就是把整个页面清空，那在每一个 decorator 实现 draw 方法之前或者之后，我们可以调用这个构造参数中传入的另一个 decorate 这样就相当于怎么样，相当于我给上一个 decorate 加了一层特效对不对？

[image](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/34d16ea3-4a62-4214-bf96-b4c300a7d058/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WK6AOVKQ%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T225541Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIA26fHa0CEU6DlK4%2FOoJzz2DjBlypcOTTGo5SbwBPSruAiEA9GJ9G6Ql7kyEeI3hGt1P97bUkbRFFe8lewqnEdDV5AkqiAQIxv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDDB60sYevbPi7O8JXSrcA6ahFVP0FvQGIvJnD0mDJbNrfgZVX2R%2FKFuYWtAjQRJsnUJ9XfbdeW4gywiQRXAmGbabUVPvj8zHMFGnb8fAA54564NbRRhRzzGfJY2FU2lNMjad9uVcUDRMblJEum%2B1T0X%2B7DqHDxrFX%2BLkEdz0gK1Nyy3Fl54hRo0D%2BklaI2xGP0vX8GqIpdjJeMKH1i%2BImjCVcZNYhpsh%2FMXP4%2BT7aWkZA4tffgarylP6zU6RK8quPnaS%2FjtEXm%2Bxlia707GJAmDd2327CbAKi35VisqO%2Bdq1Ti1eFG9DD3cTS0VeUqSCruIg%2BJuo4FvxqTRnpaPuAMjdPLfPR2kkNqi3%2FaDmK6YUR1D41gWByfZPB%2FuDZTuQHv%2BlfbVdZVwLVU5WUKyFil7MyTrayx1uXSa4tSkl8G2hBORF7HEdnp8t0JCZ5F4T6Sf75rgoj4GUsA1CijSnBgr1Go6MbGQntQXnmIIA48bKV7LFky%2B1gkSflmcyGW%2BK1xnxpDzWCS6ngre23N%2FlX1ZWqyvkcr6w%2F9ykHFY5uYnA7aUFjw9AqdVFwOupqNkKJEbiYEtvy5HtgG2bdt%2BGMhd6jVg2UBpztcRmwmfBVEvFEb91276h%2BoE8R%2FDoXvCAK8HVYIetl2khYw3TMJy6%2F9IGOqUBL48NQ3pH5VTMQeEskncAVNSC%2FDAGsxPpYy%2BcfyCxZg2BaTUqE76Rk3Kr3mpwRa6epnaSWPiXu1pe%2BBMcivN2fQvr1%2BQbX67YIzA7fvCN0n6%2BNv%2Fpf0VxUR6SCO9u1kcRlDB8%2BmY7AzBpSfZ1EGhq%2BBCaFV%2BIH%2FfHn2DhXL7s%2FYNQ08Nn94%2BjESIyb8QCHWhn1xMQF3OdYVk4IdmrvnZJhEm5l2Nb&X-Amz-Signature=3632d9b1c80e20e99a9e896e8819db8820650ad4ac9c31c0dfd126c6830471b6&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

而实际上装饰器模式也有很多变种，我不一定非要通过构造器传入对不对？我可以通过其他方式。那我们的广告时间就到这里结束。好，看完广告我们再回到了这个 decorator 类里面。接下来看断点在哪断点，我们回顾一下，在 discovery client 这里准备注册了。好，我们在这个注册方法里打上一个断点。
Eureka ht tb client decorator.


OK 我们在这里打一个断点，然后看它会不会进来。好，往下走一步。果然进来了对不对？它这执行那个 executor 刚才我们说这是子类实现的内容，它是用哪个子类的？是不是由这个 session eureka HD TP client 实现的？那我们在这个类第一行也打一个断点进来。好，我们把屏幕放大一下，小桌板收起来，一起来浏览一下这里面的内容。
第一步是什么？第一步获得系统时间对不对？非常简单。那第二步是系统时间减去上次连接的时间，这是之间的一个差值，我们叫它 delay 那 delay 这里是0。对不对？因为为什么？因为这个系统的当前时间在这之前并没有连接过服务器，那所以说它这两个时间是完全相同的，所以它没有 delayok 那这一步，if我们接着往下走。


那这里做了一个什么？这里从 HTTP client 里面拿到了一个实例，如果实例为空怎么样？如果实例为空的话，它这里会调用一个工具类的方法去 get 一个新的实例。那我们看这个 get 到的新的实例是什么？点开 expression.get class 好，我们看到了它的名称，这是一个 atomic reference 那要先 get 以后再 get class 好，大家看到这里，我把这个字给大家念一下，因为字比较小，那它这里注入的新的 client 是什么？ retrievable eureka HD DB client 也就是说我当前的这个类，它在底层通过代理调用了什么，调用了另一个 HD TB clientok 那这里接着往下看。我们已经获取到了 HTTP client 然后再调用 execute 的方法。


execute 的方法在哪定义的？是不是？刚才我们看到的 decreator 里面对不对？大家这里看到这个是个，类似回调的函数，这里非常绕人，它是调用到了 executor 的这里。这个方法 gator 对不对？ delegate 是谁传入的？又在子类传入了一个 delegate 给父类，就是他这几个代理对象总是在父类子类传来传去。而且 execute 的方法在父类子类之间也是各种穿插。所以从代码结构角度来说，说实在的 eurika 的源码可读性啊并不那么非常高。你跟 spring 的源码比，相对来说那代码水平确实是差了一截。


OK 那我们言归正传，再回来，刚才我们看到它的类型是 retriable 好，那我这里尽到 retria 不 OK 那我们到这里同样的在 execute 的方法上打一个断点，看它会不会进来接着回到断点的所在处。好，那在进入下一个类之前，我们先来看看当前的这个 session 的 eurika HT TB client 它是有什么功能？前面不是说每一层包装器都是一层特效，对不对？那它这里特效是什么？看到吗？它这里特效的逻辑实际上就分布在这里。他说如果你的 delay 时间大于 current session duration 这个时间的话，那它怎么样？它会 stop 一个当前的 session 然后 start a new one 就是说结束当前的 session 并且重新启动一个新的。那这跟它的名字也比较贴合，叫 session 的 eureka HD DB client 对吧？当你 delay 时间过长的时候，它就重新启动一个赛事。


OK 看完了这一层的特效，那我们可以顺理成章的放掉断点，让它走到下一层。你看我这里放到断点，它是不是就走到了 retriableeureka HD DB client 那大家能猜到它的特效是什么吗？这层包装器特效是什么？是不是跟它名字一样，retriable就是可以 retry 那我们接着往下走 and point 这里不用管，再往下。


好，大家看到这里有个 number of retrice 那这是可以重试的次数，它默认是几三对不对？如果你不设置的话，它默认是3，那第一次重试，我们走到这里看，他从 delegate 的对象里面又拿到了一个 eureka client 你看这就是一层，一层套一层。那他目前来说 delegate 还没有设置，所以说他拿到的应该是空对不对？那如果拿到是空，并且它的 current and point 也是空，它的 candidate host 也是空号。


那接下来怎么办？这一步是什么？ get candidate host 对不对？进去看一下它 get 什么 host 这一步获取了一个 candidate host 那大家知道 candidate host 是什么吗？我们往下走一步，走一步之后再把 candidate host 打开看一下。它这里面有一个元素，它是什么？是一个 aw S and point 那字比较小，跟大家念一下，这听起来像是亚马逊云 amazon cloud 的东西，但是它的 URL 是 local host 的二万。那我们就瞬间明白了，它是注册中心对不对？这 candidates 就是当前的注册中心数量我们只配置了一个，所以这里只有一个节点，往下再走一步。


那上一步这个是什么含义啊？大家看这一句，这句意思是什么？就是在你的这个 set 当中只保留所有传入的 candidates 相同的节点。也就是说你这个 set 如果是空经过 return all 之后它还是空。假设你这有一个节点，并且这个节点都在这个传入的 list 当中，那么你这个节点就会继续保留在 set 里面。如果你这个节点它不在这个传入的 list 当中，那它就会被删除。 OK 所以我们看这个节点目前是0，也就是一个都没有是空的。好我们继续往下走。这里到了这一行，我们把屏幕稍微缩小一点，看一下这一行是做什么，它计算虽然 hold 是什么意思。


我们看上面这行注释。他说如果足够多的节点是坏的，那坏的什么意思也就是不起作用对不对？它可能宕机了或者任何原因他不响应请求了。那我们不得不去重新重试一把。重试一把是什么？就是 retry 对不对？ OK 那我们看这个 threat hold 是怎么是由你当前节点的数量总数服务注册中心的总数乘以一个什么？这后面是一个系数，那这个系数我们打开 expression 看一下，它是0.66，那就是说你的 candidate host 如果有 100 个乘以系数，0.66之后，这个 straight hole 就是 66 个。对不对？ OK 那如果你再往下走，如果 threat hold 大于 candidate 的数量，那这里一般很难进去。对不对？那它是相当于一个防御性编程，防止有些人把这个后面的系数配置的过大，配置个一百两百之类的。 OK 往下走。到这一步，因为它的 set 是空，那所以没有任何的 operation 那它他就直接越过所有的判断条件，直接到了 candidate host 对不对？ OK 这里 if else 条件虽然没有进去，我们还是来读一下。


大家看了一圈之后，还不知道这个 set 什么业务含义，对不对？那他的意思是说失败的注册中心什么意思啊？你发送一个注册请求，假设它失败了，那么这个注册中心的信息会被添加到这个 set 当中。 OK 我们来看这个 LC 法。如果你的 set 数量也就是失败的注册中心的数量大于了这个阀值，那么怎么样？把它全部清空，重新来过。那如如果小于阀值怎么办？小于阀值，我们这里声明了一个 remaining hostremaining 是什么意思？是剩下的，也就是说剩下的 host 含义在业务上是指不在失败列表中的host。那反过来说，它不就是意味着成功的 host 吗？可能成功的 host 对不对？ OK 看他怎么做的，他把所有的注册中心循环。


如果当前的注册中心的 end point 它不在这个失败列表中，那就把它放到 remaining host 中，那这个 remaining host 在最后把它赋值给 candidates host 那这个 candidate host 就是我们需要发起服务注册的目标地址，对不对？我们的目标节点就从这里面选择一个。


好，我们 return 回去继续往下走。 OK 继续 execute 的方法往下走。那你的 candidate 列表如果是空，那什么含义啊？就是说没有任何一个注册中心可供我们注册，那它就抛出异常。接下来这里是什么意思？这个 end point index 是啥？ endpoint index 就是我们不停重试对不对？我们重试每次发起的请求都会把这个 and point index 加1。那如果它的 index 的下标已经大于可用的 candidates 的数量了，那你觉得还用再试吗？因为它已经从头试到尾了。对不对？所以说它这里也抛出了一个错误叫什么 cannot execute request on any no server 就是已知的所有注册中心都不能去处理我的注册请求。 OK 那我们没有这么背，这里不用进去。
好，那这里到了，下一步，你看他怎么选择注册中心，他这是怎么选我们这么多 candidate 他从 0 到1，从第一个下标开始依次往后选，看到了没有在这里你 retry 几次，那它这里就会往后移几个 index 好，因为我们这里注册中心数量只有一个。那这里就选择到了第一个注册中心。


OK 那选择到第一个注册中心以后，我这里 new 了一个新的 client 这个 client 的入参是什么？ endpoint 这 endpoint 就是注册中心的服务地址。 OK 我们往下走看到这里又是一层洋娃娃，又是一个 request executor 那进入之前，我们先往下走一下逻辑，假设我发起了服务注册请求，也成功返回了 response 在下一步。
如果这个 response 是成功的，是被 accept 了对不对？那他把 delegator 设置成当前的 client 那什么意思啊？就是说当你成功了之后，往后的操作、注册什么之类操作它都会用。上一次已经成功的这个 client 大家看明白没有。在 delegator 里面，如果你失败了，那当然不会用你了。但是如果你成功了，他会把你设置到 delegator 里面，下一次也会继续用。


你。 OK 这里如果 retry 次数大于0，那打一行 log 证明什么证明它是经过 retry 以后才成功的，并且返回 responseok 那如果不成功，那这里看不成功就把这个 delegate 设置成空，那它是怎么设置的？通过一个 comparing swap 对不对？那就是 cast 操作。
而很熟悉的 cats 操作。大家注意，在 spring cloud 里面，这个 cats 操作是大量应用的大规模大范围的应用 cats 操作，这也是面试中经常会问到的一个问题， cats 操作是如何保证一致性的？然后他在哪些条件下可能不适用？这是面试中经常问的，我也经常问，但是我会根据面试者的这个对知识的了解程度决定问的是由险到深。那最底层当然是问到操作系统层面它是怎么实现的？ OK 所以大家对这个 case 操作有必要去了解一下。


OK 那既然不成功了，怎么办？它要放到一个 set 里。我们前面看到了这个 set 是保存什么，所有不成功的节点，对不对？你不成功的 client 下次我不会调用，所以我要把这个 client 加到 set 里面。 OK 那最后看到这里有个 through exception 对不对？它在什么情况下 through 我们往上看这个 for 循环的 retry 对不对？那你 retry 次数都用完了，你还是没成功，那他这里就会 through 一个 exception 那这里的流程看完了之后，我们接着走主线剧情，这里我给同学布置一个作业，接下来大家猜还有几层养娃娃，也就是还有几层带 create 装饰器，告诉大家还有好多层的。


那我们这里为了怎么样节省时间，就不带大家一层一层的去分析源码了。我这里留给同学的作业，就是大家通过这种 debug 的手段自己去研究一下，把这每一层从前到后就像洋葱一样，一层一层拨开你的心对不对？我这里怎么样？直接到最后一层带大家看一下大结局好不好？剩下的情节我们自己去来挖掘。
最后一层是什么？ jersey client Jessie application client 好。发现它是一个子类，那它的 register 方法就应该在哪里？在它的顶层类 abstract 里对不对？这里给它打上一个断点，直接把请求放到这里，把页面拉大，直接把请求放过来。嘿好嘞，过来了。好，我们这里看最终的大结局。


第一个参数是什么？ uro pass 那是什么东西？ App 杠 eureka client 这里我们不管，先往后看，创建了一个 results builder 这个 builder 里面放什么一个 service uil service uil 就是我们注册中心的地址。然后 uil passed 是什么？是在注册中心后面跟的一个 uil 那它是指向什么？它指向 App 指向 App 这个 end point 后面再跟了一个参数。这个参数是什么？是当前我们这个应用的名称对不对？叫 eureka client 也就是说他注册的应用名称是通过类似这种参数的形式传入进去的。创建了 builder 以后，往下它是 add 了一些 header 点进去看一下。好一个 abstract 方法，那我们到子类里面看一下，看它这里面做什么内容，把 additional header 加进去，那也就是往 header 里面无非是加一些内容，我们这也就不跟进去看了。回到最外层，在这里拼接 header 它的 set 类型是 G zip 然后以及它接受参数的类型。


好到最后一步，看我们跟到最后，这一步是什么？就是 post 了它 post 什么内容。看有一个 client response 这是介绍来的 response 那它 post 的内容是什么？看它后面有一个 info 这个 info 是什么内容啊？就是 instance info 这个类对不对？它是当前这台 instance 它的信息比方说 instance ID 是幺九二点幺六八点幺的100，这是我们的 IP 地址后面跟 eureka client 3000 端口，比如 App 的 name 还有当前 IP address 这些都是我们当前这台 instance 的信息，我要把它注册上去。那这时候我们看一下浏览器里服务注册界面，它是不是有 instance 没有对不对？我们刷新一下还没有好，回来这一步以后应该就会有了。


好，我们再到页面上看一下。看到吗？这里已经有了一个尤瑞卡 client 那说明刚才这一步已经注册成功了。好的，后面这里对 response 的处理我们就不跟进去看了。有兴趣的同学课后可以自己去研究一下。通过今天的源码阅读，同学们是不是感觉到独源码还是一件稍微有那么点费力费眼神而且又略显枯燥的事情？没错，那阅读开源项目源码学习源码的过程确实需要大家真的耐得住寂寞。


OK 我这里就给大家布置一点小作业，让大家练习练习。今天我们学习了服务注册上半场，什么是上半场内容？也就是从服务的提供者到服务注册中心，这条链路被打通了对不对？那接下来还有后半场，后半场在哪里？后半场就是说注册中心接收到一个服务注册请求以后后续的流程。 OK 大家可以利用今天课程中学到了一些小技巧或者小方法去实际，那这一节的内容就到这里了，同学们下期再见。




