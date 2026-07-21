---
title: 1-4 服务端处理器_RpcServer实现-4
---

# 1-4 服务端处理器_RpcServer实现-4

[image](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/c2939355-4b21-4a84-abbb-836fe538cee5/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466Z6ID5ADR%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T230042Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIEjbsGSWikKorgplB4Y9xO3NSQ9V2zHiHgdervoMBnGQAiEAp5nFmCQpqhauflz8HWwwBRX97u%2BUnjcPl%2FxULEhfe64qiAQIxv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDFUeQ10blzTIkOnNTyrcA0IjkyJD3d%2FqvVKnlF3aeTBjeWTyNCJVLOOapmFPZ%2BqDpzmEfNb51WmGN5g7HwrBYHAciot7sgzbNRMNVw0WAvmXkCjam2hkqMe1SWqKDY0lUP5g7ltxS8yNdXXNezc83vJTqO1c3dEoqTWmL%2BgFdhMpgQgeRS8rDxkyGQiRgjHtzzkhjCSgeRgh7r%2Btxp8Dq5tjC5HNhtHMOg%2B6DGSZ9gB5wbHkXySkcqw1CYRKXdRMlFizv5oB5YQZ6SrEJDQfed5NzJlZu%2FHf5GeACVqru2J4669v1CPnGopJ97VsVpd6V3uoe%2Bne5TA87iXTit93aP6rntTwmq79VnaZb1L6mWeRXVgEEZZI9NtngJ9nIIrD6w392iFHgA2fIcPMRZ0Q1ferFX%2FDEZMbsmwGTi0F9j4FTEcZWjT80usewwmPzffpICLKjH9GdvBiZV02cNWsXkNSelfL8V8kAVwpJk%2FnAyfFZikWP%2BVMMF%2BphtL9G0r4G3huUBA5dsMAnpdJHblFeSWAAQCSQmkIQtVJ9JAK9puephk5vRoIykCKS0cIGW5gO0Y1auF7DKRzYNe0qy9G91QRfrW8Bn5sGtkvbB0H2YIX5R8VEy7sE9b72%2FbZPMgJgJg79O5MS8QuzVuzMJy6%2F9IGOqUBYk6jr3F1rejbvQroOWWj6j1B55j9gQYx7caiyNigJSRDVD653cbxS1Xw5qXxtEFXJV03hv3vD4XpTdexM6wXhLZOEeBDP%2FTyTCX95Tz3nduSJ85gRThKULEdbrVYP%2B1ALWRhtPlGhiM4aB7Bzfsv4chNRpHfYkcRk0mgeamiKaiuiXkKqMWVP1URFLY0ZFNNtgPw89Tz1IEA5M%2BnFczTAJvuPSWU&X-Amz-Signature=2073c54b4e9a937306a4ee77a6fec23626324d2386cd1fd9eb00ea20ba73eddf&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

我们知道有一个什么，刚才我都说了有一个 provider config，还有一个consumer，对不对？在这两者之上，还要有一个更上层的。咱们叫做 config abstract，可以吧，我们给它起个类，叫做 config track，我们叫做 r p c config abstract。
R p c config abstract。
它不属于consumer，也不属于provider，它是更上层的。我把它move，我把它移动到我们Com，点 b f x y，点 repeat RPC 的config。这下面这是最上层的一个类。当然它也是一个抽象的abstract。好，不管我们的服务的提供方也好，还是服务的调用方也好，总之它肯定有一个东西，就是 i i d i d。我们在这里我就简单用一个 atomic integer 去做一个生成 atomic integer，我们叫 i d generator，我给他搞几个方法。当然这个是父类，所以我们用 protected 比较合适。 protected 的 string ID 好， protected 还有什么？String？我们叫 interface 特 last 等于 none 默认值，对吧？这些都是什么通用信息？无论我们是服务的提供方，还是服务的调用方，都需要有这两个东西吗？还有一些特殊的，比如我们 proxy class，我们的服务的 clan 端可能会有代理这个概念，我们在这里比如先加上后面不用就算了，它是一个 class 类类型。这个类到底是什么我也不知道，所以我用一个问号表示。

[image](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/fa3b2791-0050-4462-9ac4-bb19a524bd6e/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466Z6ID5ADR%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T230042Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIEjbsGSWikKorgplB4Y9xO3NSQ9V2zHiHgdervoMBnGQAiEAp5nFmCQpqhauflz8HWwwBRX97u%2BUnjcPl%2FxULEhfe64qiAQIxv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDFUeQ10blzTIkOnNTyrcA0IjkyJD3d%2FqvVKnlF3aeTBjeWTyNCJVLOOapmFPZ%2BqDpzmEfNb51WmGN5g7HwrBYHAciot7sgzbNRMNVw0WAvmXkCjam2hkqMe1SWqKDY0lUP5g7ltxS8yNdXXNezc83vJTqO1c3dEoqTWmL%2BgFdhMpgQgeRS8rDxkyGQiRgjHtzzkhjCSgeRgh7r%2Btxp8Dq5tjC5HNhtHMOg%2B6DGSZ9gB5wbHkXySkcqw1CYRKXdRMlFizv5oB5YQZ6SrEJDQfed5NzJlZu%2FHf5GeACVqru2J4669v1CPnGopJ97VsVpd6V3uoe%2Bne5TA87iXTit93aP6rntTwmq79VnaZb1L6mWeRXVgEEZZI9NtngJ9nIIrD6w392iFHgA2fIcPMRZ0Q1ferFX%2FDEZMbsmwGTi0F9j4FTEcZWjT80usewwmPzffpICLKjH9GdvBiZV02cNWsXkNSelfL8V8kAVwpJk%2FnAyfFZikWP%2BVMMF%2BphtL9G0r4G3huUBA5dsMAnpdJHblFeSWAAQCSQmkIQtVJ9JAK9puephk5vRoIykCKS0cIGW5gO0Y1auF7DKRzYNe0qy9G91QRfrW8Bn5sGtkvbB0H2YIX5R8VEy7sE9b72%2FbZPMgJgJg79O5MS8QuzVuzMJy6%2F9IGOqUBYk6jr3F1rejbvQroOWWj6j1B55j9gQYx7caiyNigJSRDVD653cbxS1Xw5qXxtEFXJV03hv3vD4XpTdexM6wXhLZOEeBDP%2FTyTCX95Tz3nduSJ85gRThKULEdbrVYP%2B1ALWRhtPlGhiM4aB7Bzfsv4chNRpHfYkcRk0mgeamiKaiuiXkKqMWVP1URFLY0ZFNNtgPw89Tz1IEA5M%2BnFczTAJvuPSWU&X-Amz-Signature=783bfb8e971fae64755c3af0d3126a0c646a9460b1ad86ee12f1cd557405cdb9&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

暂且写一个东西，叫做 proxy plus 等于什么？先不管它哈，备注一下服务的调用方，也就是 consumer 端特有的属性。后面其实你可以把它直接放到什么，放到我们的服务的 consumer 一端。在这里我再写一个叫做 consumer config 好了。 provider config 一定要继承我们刚才所写的 RPC config abstract，对吧？一定要继承一下，这是我们的服务的提供方，对应的调用方也是一样，都是要有一个负累。
好了，接下来我问你，我们现在普歪德，它应该有具体的方法，我们刚才通过父类里边哈我，比如我给它生成一些 get set 方法最简单的，比如我们给它生成一个ID，它去调 get ID 的时候，在这里可能要稍微改一下哈。 string 类型，返回 get ID 这里边 if 如果 string util 是第二意思。 blank 如果 ID 是空对吧？ ID 是空就没赋值吗？没赋值我就给它生成一个ID，等于我们的repeat。这个叫做什么？这里边我们叫做 config 詹姆瑞克不是什么ID，我们就直接加上 get and increment 就可以了。给他返回一个ID， return ID，然后 set ID。很简单。
public wide set ID 在这里边传进来的 ID 直接赋值 this 的it，等于 ID 可以了。是不是再给他一个 interface class？我是不是也可以去做get？ set 我可以去写一下哈。比如 public wide 咱们叫做 set interface，不搞那么复杂。 set interface 给我传一个 string 类型的 interface class 可以吧？那我就 diss 点 interface plus，等于 interface plus 可以了。然后再来一个 get interface public，返回是string，叫做 get into face 的方法。直接 return this，点 enter this class 好了，其实我已经写完了。这是不是很简单。这是我通用的一个最上层的东西，最上层的一个抽象类。我下面无论是 provider 也好，还是 consumer 也好，都是继承上层的抽象类。
我们来想一想我在 registry 的时候，我注册的时候我要做什么事情？回看一下哈。我们注册的时候，我们要有一个map，这个 map 就是注册程序的时候，它需要provider。 config 里边的 key 是接口名称， Y6 是程序对象。我们来写一写。我们来看一看 RPC 搜索端注册的时候，哈。
首先我们需要有一个 map 了，这个是毋庸置疑的。我们写一个private，比如它是一个volatile，普通的 map 就可以，它没必要非得是一个坦克人的map。哈，我们就一个普通的map。 string 类型。 key 就是 interface 对吧？ name 可以这么去理解 value value 是一个程序的引用逻辑，对吧？是一个引用逻辑程序。 value 是什么东西？ value 其实就是它具体的接口。下面的实现类对象实例就是一个object，我们给它起个名字，叫做handler。 map 等于 new 一个哈希 map 搞定。我注册的逻辑就很简单了，哈。注册逻辑就直接这样去写就完了。


第二 put 只要给我来一个叫做 provider config，我们叫做 provider config。我直接就这样去写。 key 就是 provider config 的 get interface value，就是 provider config 的 get r e、 f 对象。如果有引用对象就可以这么直接写。现在是不是在 provide config 里边有特殊的引用对象就可以了？ref，这个 ref 还不简单吗？我们直接可以去写protected，它是一个object，因为我不确定这段逻辑具体是什么实现，我就知道它是一个object，泛型就可以了。好，这样是不是就 OK 了。
好了，我们注册的时候，同学们请看是不是直接把我们注册的接口在这里，我再打注释哈，这个你就可以认为它就是一个叫做 user service 接口权限命名， key 就是我们的 provider config interface，它其实就是我们的对应的key。应该这样写， t 就是它，我打个括号指代我们。比如 user service 它的接口权限命名，我再来一个value，它就是一个 provider config ref，就是一个引用。它是接口下的具体实现类，比如是 user service implements 实例对象这样，只要注册的时候把接口跟实例对象做一个绑定，因为我们再去发起 RPC 调用的时候，我们是调用接口下面某一个方法，让我们远程的程序去执行。具体接口下面某一个实现类 user service implements。


它的比如像是爱的 user 的方法对不对，让它去真正的去执行，执行完了把结果再给我响应回来。所以我们只需要知道这个接口和哪一个。它具体的下面的实现类是有一个绑定关系的，我们把它去注册上去，让我们 RPC 程序调用的时候，能够从注册的容器中找到具体注册的类，找到具体的方法去调一下就好了。


好了，我们做完这个事情之后，这个 handle map 我们是不是应该把这个 handle 的 map 传进去？肯定的，因为我们真正去 read 的时候，我们真正必须要去传进去一个我们的map， string object 对应的 handle map，这是必须要去网上引用的，我们 dace 点它等于他就可以了。真正我去执行的时候是不是在里边， request 里边，当然第一步就是解析解析我的 RPC request 对象。从我们的 handler map 中找到具体的接口，当然这个接口就是我们的 key 下的所绑定的实例。


这个实例说白了，如果你是跟 spring 整合的，那就是 spring 的bin。比如你的实际的 service implements 是不是 spring 的 bin 对吧？比如你的 hello service implements 也是 spring 的bin。甚至你在服务的调用方，你的 invoke service a 和 invoke service b 其实也应该是 spring 的bin。因为你要跟 spring 整合，你必须要把它当成 bin 去注入到 spring 容器里去管理。


好了。其实你找到 bin 实例了之后，然后你是不是通过反射，通过反射或者是 c g lab 都行，是不是去调用什么？因为你都知道具体哪个病了。你 r p c request 里边还有具体什么方法调用？具体方法传递相关执行参数，执行逻辑即可。最后第四步，返回享用信息给我们调用方对不对？就是这么一个过程。我不知道小伙伴们能不能理解这么一个过程。这一块也是属于比较复杂的。为什么我给你讲了这么多，说有provider，还consumer，它上面还有一层父级，就这么一个意思。
好了，这节课其实并不难，非常简单。你看代码，它无非就是一个什么，无非就是这么几行。代码，无非就是一个启动 start 方法。一个注册也非常简单，就是一个 register processor，就这么一个方法。还有一个close，无非就是把注册好的map，你把它透传到 RPC server handler 里边，当成一个引用就可以了，代码就这么简单。但是实际上思想还有我们整体搭建的这几个框架，就是这几个 provider config， consumer config 以及上层的config。你要把它能够梳理清楚，其实不是容易的一件事情，起码你自己可能要对一些比如开源的像 double 这种RPC， Java 的 RPC 框架，你要很了解，你才知道它具体怎么去抽象负极，怎么抽象我们的服务的提供方，怎么抽象服务的调用方，怎么去把它跟我们的 net 去集成起来。

集成起来的最关键的方法就是 register processor。 OK 这节课我就讲到这，感谢小伙伴们收看。


