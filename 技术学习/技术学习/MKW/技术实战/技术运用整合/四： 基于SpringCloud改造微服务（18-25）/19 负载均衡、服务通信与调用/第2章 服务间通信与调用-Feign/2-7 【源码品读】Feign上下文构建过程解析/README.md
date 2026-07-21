---
title: 2-7 【源码品读】Feign上下文构建过程解析
---

# 2-7 【源码品读】Feign上下文构建过程解析

[image](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/12433ab0-84f3-4782-a723-9f0a9351d787/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RUT5OTAH%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T225623Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDPxnMuJtp5CN3uNdy4mZgM5UJdaZul2rt1XE6AYHtDjwIgQZTg%2BEqBNE8zNymJFCR1jGkYI6JG%2FN%2BLU0zt9qci5wsqiAQIxv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDO1ndPTYm6Gm%2FCzX1CrcAyi0e6M3QTDfP77QQfcARuo3h4KGM%2F86zjQZKEH58p1TTN1ql31LWetSKOJG443ORx65YcG6mCuWWPPt9At%2FH3H5UJ4VbvJeW3%2BmiRyx1HQXQg0jq4FhqSQxYsq7dfMPeSHJewRYZHdZ7LNuUdpB3BSfTnWcmSUZ57w4hla%2B2s3QTYiF%2BgtVXrFUZoQEHj6kqB1b9VQyeJqVwuozSmw268u%2BT5NfxXCd4B7NMdStsdK5zPedJswn0StV4PTuBOGUkSezQsORUccEU6NnEIipebL%2B%2BxoaMXHXWUtq%2BGYgGHtaENRkLl1L7PZxEu9Tqb562Fj0Aj5d8lEBoBl7U0N1QsDFZcnQmklzuGD2gHjBGrBhIlsPysgOHRfVGW9aZv5HH4MSqV9bGoV2wT0No9ShOr2zCgrf91hrWkQsRvPYG5D37sy69iRGWkVhYwjj7oWTXSq9m659G3yonupgZwF%2ByDt11bmLyNSiXpdi9PxK1GJoPxwqB26RCpCxtU0DH%2BePnJCMQrutlYjiGMtRNgUKuUccsigZL5AKTVkmqgjvonPDlB64xboDm7a%2FpzP8WmxhIyF7FfFR7800idCZO%2BQ0okyw40mUC5Y%2FxqPw9tqA7E5Z2lhMaYRpDHHCKgxlMNW5%2F9IGOqUBQYvD%2FubVIJc74z4HfdwCEQiAfTo%2FG%2FqOT092TmiHpQ3bU4QDPnM5cmfQeQnaf8BLq01rKyTJ8AGMCyzOujNksaAc4VpH0MtvTFIjnJSKuszpHCw7gMZyUE8vzt2LbyNt%2F8cJnaBwq3dD9lB5O7olKPah1VXv9K%2BZiosrhK3W5%2Fm0R7zcwL6pRB%2BLOwB4kjWhQo5eLFzJE9Guy%2Fm%2BDMn9LE2xb8mB&X-Amz-Signature=b7f9e97d6711c5d14cfb586e47de6c146cad910e2dc51721bc3af4b3b96bd3fc&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

[image](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/67bb3802-ce44-4c1c-a74f-71b96fcd718d/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RUT5OTAH%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T225623Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDPxnMuJtp5CN3uNdy4mZgM5UJdaZul2rt1XE6AYHtDjwIgQZTg%2BEqBNE8zNymJFCR1jGkYI6JG%2FN%2BLU0zt9qci5wsqiAQIxv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDO1ndPTYm6Gm%2FCzX1CrcAyi0e6M3QTDfP77QQfcARuo3h4KGM%2F86zjQZKEH58p1TTN1ql31LWetSKOJG443ORx65YcG6mCuWWPPt9At%2FH3H5UJ4VbvJeW3%2BmiRyx1HQXQg0jq4FhqSQxYsq7dfMPeSHJewRYZHdZ7LNuUdpB3BSfTnWcmSUZ57w4hla%2B2s3QTYiF%2BgtVXrFUZoQEHj6kqB1b9VQyeJqVwuozSmw268u%2BT5NfxXCd4B7NMdStsdK5zPedJswn0StV4PTuBOGUkSezQsORUccEU6NnEIipebL%2B%2BxoaMXHXWUtq%2BGYgGHtaENRkLl1L7PZxEu9Tqb562Fj0Aj5d8lEBoBl7U0N1QsDFZcnQmklzuGD2gHjBGrBhIlsPysgOHRfVGW9aZv5HH4MSqV9bGoV2wT0No9ShOr2zCgrf91hrWkQsRvPYG5D37sy69iRGWkVhYwjj7oWTXSq9m659G3yonupgZwF%2ByDt11bmLyNSiXpdi9PxK1GJoPxwqB26RCpCxtU0DH%2BePnJCMQrutlYjiGMtRNgUKuUccsigZL5AKTVkmqgjvonPDlB64xboDm7a%2FpzP8WmxhIyF7FfFR7800idCZO%2BQ0okyw40mUC5Y%2FxqPw9tqA7E5Z2lhMaYRpDHHCKgxlMNW5%2F9IGOqUBQYvD%2FubVIJc74z4HfdwCEQiAfTo%2FG%2FqOT092TmiHpQ3bU4QDPnM5cmfQeQnaf8BLq01rKyTJ8AGMCyzOujNksaAc4VpH0MtvTFIjnJSKuszpHCw7gMZyUE8vzt2LbyNt%2F8cJnaBwq3dD9lB5O7olKPah1VXv9K%2BZiosrhK3W5%2Fm0R7zcwL6pRB%2BLOwB4kjWhQo5eLFzJE9Guy%2Fm%2BDMn9LE2xb8mB&X-Amz-Signature=07712519973428f940c8cf8c0bdf0484496345f67d169b56937d7653c705a0e9&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

[image](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/13682bba-a77f-495d-b88e-0238e823e72d/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RUT5OTAH%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T225623Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDPxnMuJtp5CN3uNdy4mZgM5UJdaZul2rt1XE6AYHtDjwIgQZTg%2BEqBNE8zNymJFCR1jGkYI6JG%2FN%2BLU0zt9qci5wsqiAQIxv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDO1ndPTYm6Gm%2FCzX1CrcAyi0e6M3QTDfP77QQfcARuo3h4KGM%2F86zjQZKEH58p1TTN1ql31LWetSKOJG443ORx65YcG6mCuWWPPt9At%2FH3H5UJ4VbvJeW3%2BmiRyx1HQXQg0jq4FhqSQxYsq7dfMPeSHJewRYZHdZ7LNuUdpB3BSfTnWcmSUZ57w4hla%2B2s3QTYiF%2BgtVXrFUZoQEHj6kqB1b9VQyeJqVwuozSmw268u%2BT5NfxXCd4B7NMdStsdK5zPedJswn0StV4PTuBOGUkSezQsORUccEU6NnEIipebL%2B%2BxoaMXHXWUtq%2BGYgGHtaENRkLl1L7PZxEu9Tqb562Fj0Aj5d8lEBoBl7U0N1QsDFZcnQmklzuGD2gHjBGrBhIlsPysgOHRfVGW9aZv5HH4MSqV9bGoV2wT0No9ShOr2zCgrf91hrWkQsRvPYG5D37sy69iRGWkVhYwjj7oWTXSq9m659G3yonupgZwF%2ByDt11bmLyNSiXpdi9PxK1GJoPxwqB26RCpCxtU0DH%2BePnJCMQrutlYjiGMtRNgUKuUccsigZL5AKTVkmqgjvonPDlB64xboDm7a%2FpzP8WmxhIyF7FfFR7800idCZO%2BQ0okyw40mUC5Y%2FxqPw9tqA7E5Z2lhMaYRpDHHCKgxlMNW5%2F9IGOqUBQYvD%2FubVIJc74z4HfdwCEQiAfTo%2FG%2FqOT092TmiHpQ3bU4QDPnM5cmfQeQnaf8BLq01rKyTJ8AGMCyzOujNksaAc4VpH0MtvTFIjnJSKuszpHCw7gMZyUE8vzt2LbyNt%2F8cJnaBwq3dD9lB5O7olKPah1VXv9K%2BZiosrhK3W5%2Fm0R7zcwL6pRB%2BLOwB4kjWhQo5eLFzJE9Guy%2Fm%2BDMn9LE2xb8mB&X-Amz-Signature=d7c5bb856e74b77d0970e2f3d1fe70a29c67e73113e37915133a27e85d0c8eb7&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

hello 慕课网的各位同学们，大家好，下半场的哨声响起了，开始哨声，我们紧接着上半场讨论什么内容呢？ fin 的 context 也就是上下文的构造。大家先来看一下这个上下文是说谁这货 thin context 它就是上下文，但是它只是狭义的。这个上下文怎么还有狭义广义之分吗？没错，那广义的上下文又是指谁呢？大家应该看过前一小节图文课程中的动态代理了，对不对，整个份上下文的构造过程包括动态代理对象的创建，这边是广义上的上下文了。


好，那我们这里还是用最快最省事多快好省的方式打一个断点，启动项目从头到尾跟一遍，没事走两步。 OK 这里我们启动谁呢？ fin consumer application 以什么方式启动呢？ debug 方式走起，看到图标成功一半，待一会儿断点就会过来了。好，那这就是万物开始的起点。 think client factory being 看到这个名字了吗？我拉到上面看得清楚一点。 think client factory being 好，它的 get object 方法就是开始构造上下文创建动态代理对象的起点，我们往进去跟一遍，走第一步，上下文直接被构造出来了。


是的吗？其实未必，这里构造出来的只是一个半空壳，我们不信进去看一下看到吗？这里进到了 fincontext 的方法中，它只是调用负列的构造函数装入一些装配对象的名称，也就是一些属性名而已了。所以真正的构造流程在哪在后面我们先把它跳回返回到上一层再返回，不管它把它晾在这。好，这里接下来就开始正儿八经的构造过程了。


同学们注意，前面说到所有的 fin 它都是在哪里构建的？大家看这一个字 fin.builder 那这个份就是为了生成 httpap I 所用到的代码非常的长，一半都是注释。好，我们这里跳回去不看它，一个 builder 没什么好看的。接下来进到这个份方法里，看它是如何结合这个上下文 context 进行构造的。
好。第一步，获取一个 logger factory 这个没什么好看的，是初始化一些 log 对不对？所有组件都有这一步的初始化 log 以后，我这里声明了一个 builder 那这个 builder 做哪些事情呢？先创建一个空 builder 然后把这个 logger 组件给塞进去。


你看它这是一个方法链的编程风格，大家使用 lombok 的 build 注解也能达到类似的效果。大家要记得常在项目中使用这种很方便的注解，你像这个 builder 我们看它是怎么写的，看它这里还都是一些 get setter get a setter 很碍一眼。
对不对？这个方法其实并不太建议了，大家应该用哪种方式啊？没错， long book loan book 插件有一个 at builder 你在类上面一加这个 at builder 它自动帮你生成这些 builder 方法，你不用写一行代码，非常方便的。


接下来几步是什么呢？先是创建 encoder 再是 decoder 因为我们这个 fin 往大了说可是一套通信协议，那它自然有 decode encode 这些组件。再往下这个 contract 可就有学问了。我们这里不做深究，后面会安排一个篇幅来让大家看一看 fin 的 contract 是怎么样运作的。
这一步看 config thing 你 config 什么东西呢？无非是一些注解密密麻麻的注解，我们先不看它，这里不是主要剧情，要抓大放小返回。那这个 builder 构造好了，builder到现在为止构造出来。分对象没有 HTTP API 的分对象还没有构造出来，那只是一个构造器。接下来我们看这个 if 条件会走进去。为什么呢？你大家看这个 URL 就知道了，是空对不对？如果没有指定 URL 那我这里走进来会根据这个 name 做判断 name 是谁 eureka client 这是我们 fin API 指定的 nameok 那如果它不是以 HT DP 开头，那我这里会把它自动的 pre append 一个 HTTP 标签上去。因为份它底层也是基于尤瑞卡的 HTTP 接口对不对？那所以它的通信协议自然也是基于 HTTP 的。


我这里前面的 HTTP 不能漏掉，下面这个 URL 做了一个叫 clean path 你可令什么东西给你的前路扫清障碍。我们来看一下它首先把你这个 pass 怎么样给它 trim 一下，我们这个 pass 本身就是空你 trim 完了它还是空。 OK 那就是没有作用了。那假设你 pass 不为空，你前面已经在里面配置上了，那他这里会给你的 pass 加一些反斜杠之类的标签，相当于一个规范化。并且如果你的 path 不注意一个斜杠结尾了，但是后面又没有跟任何其他的单词，他会怎么样？它会把你最后一个斜杠给截断还是规范化？好，那这个名字不叫 clean pass 那这个感觉叫 reformat pass 似乎更加合适一点。 OK 我们继续往下走一步。好，走到这里。大巨变就要发生了。我们在故事开始之前打一个断点这里就是构造动态代理对象的地方了。那前面我们说到，在图文教程里构造动态对象的地方是哪里？我们说到是这里，那什么情况下她才会走到这里呢？那大家看这个 if 条件喽，如果你指定了 URL 的情况下，那他这个衣服条件不进去，那依然会往下走走，一直走到这里。


实际上同学们这个 load balance 里面调用的方法和下面这个 target 是一模一样的，只不过是调用方法的位置不同。所以流程是一个流程，只是放的地方不同，当英雄不问出处，先看 load balance 走进去。好， load balancer 里面，我这里在开头的地方打一个断点，它第一步做什么呢？构造一个 client 这个 client 就在上面。老邻居就排在你上面，那这里就不用看了，它实际上就是从你 context 中拿到一个指定类型的 class 那拿到哪个 class 呢？ I service.谁是 I service 还记得吗？前面我们创建的接口对不对？添加了分 client 的接口。


那这里从上下文中拿到这个接口以后，我们来看，如果它不为空，把这个接口塞到 builder 里面，然后这里就是关键了这个 target 是什么东西呢？它其实不是什么东西，它就是一个 target 类你从上下文中获得一个 target 类，但是这个 target 目前还没有做出什么样的举动。我们往下走一步，看这个 target 类的名称叫什么。


同学们跟我大声念出来 high strikes target 那我们用到 high streaks 的内容了吗？暂时还没用到，但是这里就埋下了一个伏笔，也就是说 fin 和 high streaks 有千丝万缕的关系。我们在下一小节将详细的介绍如何在 fin 中使用 high strikes 的内容。 OK 那这里拿到 high strikes 的 target 大家不要被这个名字给迷惑了，咱就把它当成一个工具类。好了，接下来这里的 target.target 才是构造动态代理对象的地方。


我们跟进去。同学们有时候 debug 断点会乱跳对不对？那尽量。如果 debug 用的不习惯的同学，在他这一行的前后多打几个断点，他即使乱跳，你直接把它用这个方法 resume resume program 用这个方法直接跳到下一个断点，很方便的。那因为我不太习惯按钮，都是使用快捷键。
OK 那这一步 if 条件判断它的结果是 true 因为当前这个对象 fin 它的 builder 是谁？是 fin 的 builder 它并不是 high streaks fin 的 builder 大家注意，所以这里直接使用这个 fin 对象的 target 方法对我外面传入的 target 进行改造。念起来好像顺口溜。那往下多看两步。假如你这是 high streaks 的分，那么这个流程可就不同了，那你这里要构造什么？要构造 fall back 还要构造 fall back factory 但是最终它依然会走到 feed target 方法中。好，我们这里继续跟进去，是打一个断点放过来。Ok.那这个 build 是谁？往下看，往下看。


在这里那 build 的 new instance 也就是 fin 的 new instance 方法。我们在前面图文教程中跟大家说过一个什么？是不是所有的 fin 的动态代理对象都是通过 new instance 生成的，大家如果还记得的话，可以直接走到这个 new instance 的地方看核心流程。好，我们走进去，一二三来了。
小桌板忘了收起来了。那大家到现在也看了不少代码了，我这里跟大家讲一个看代码的禁忌。大家一定要记住，这是有血的教训的是什么呢？就是我们程序员都觉得别人写的代码就是 shit 是不是跟屎一样，但是你心里这样觉得可千万不要说出来，因为很多屎是按历史遗留代码，你真的不知道什么写的。


我当时刚毕业的时候去的第一家公司，也是一家 500 强的外企。我旁边一位刚入职的小伙伴在看代码的时候说了一句，这哪个傻叉二百五写的代码跟屎一样，他这样说倒没关系，关键他把这个项目的名字还有这个方法这个类都给说出来了，结果这个小伙伴试用期过了就被开除了。


因为为什么呢？因为那个代码是我们大老板写的，我们大老板就坐在他后面，听到别人说他写的代码像屎一样。所以高调做事，低调做人。好，那我们到了这个 new instance 你看代码非常。对不对？短小精悍。好，这里我们先来看第一个方法是什么 name to handle 的，不管往下走。第二个方法是什么 method to handler 不管后面再看好这里 for 循环，for循环的是谁，大家看 target type 是谁，123说出答案。 I service 对不对？ I service 的所有 method 反射到那往后走。每一个 method 我们只要声明了 HTTP 的标签，那么它就要有戏份了。这里往后走。好，走到了最后。


前面两个方法为什么没进去啊？大家看这个条件， if declaring class 等于 object 那肯定进不去了。想也知道。那这里如果是个 default method 这个 default 是做什么含义呢？你看它这里要求你这个方法的 modifier 是什么，abstract public 等等，并且你的这个 method declaring class 要是一个 interface 看到吗？所以它进不去，到了这里要做什么事情呢？看这个 method 把它塞到 map 中，这个 map 是哪一个？是在我们上面跳过的这个 method to handle 的，你把人家的 master 放进去，那你要给人家什么handler ？这里就是个学问了，这个 name to handle 的从这边 get 到了一个 key 这个 key 是谁呢？我们把它 copy 下来，看一看这个 K 会返回什么。


你看，这个 key 返回了一个 iservice 一个星号加上 say hi 方法，它是什么？它是你的 class name 再加上你的方法名，最后还要跟上你的方法签名。我们的 say hi 他没有方法签名，因为是个空方法。那通过这一串的字符串把它作为一个 key 从这个 name to handler 里拿到了谁拿到了一个 handler 准确的说是一个 method handler 这是不是同学们已经感觉到预示后来将会发生什么事了？没错，你所有调用到接口对应的 method 的请求都会转发到谁转发到对应的 handler 也就是说这个接口虽然没有实现类，但是它却可以处理方法，为什么？因为它的请求被转发到了其他的实现类中？这个实现类是谁？我们往后看走到这里，大家看这个方法吗？很经典。


invocation handler 让你对 invocation handler 发表一个五分钟的演讲，你要是扯不过 5 分钟，那是不合格的。同学们，这个面试官你非常喜欢考到，不过相对来说应该是比较初级的面试官会考这些动态代理，我一般不太喜欢考这些纯理论的。因为我认为像五年以上工作经验的同学，对这一部分应该都相当熟悉了。那如果你被我考察到不熟悉，那我干脆就直接把这个面试咔掉了，节省大家的时间。所以说这些知识高频率的问题大家，一定要去看。


我并不是说让你在什么网上面试宝典看还是那句话纸上得来终觉浅，觉知此事要躬行，大家要去躬行的知道吧。躬行的意思就是说到代码里面 debug sprint 框架从头到尾把它 debug 一番，你比这里书上看来的印象都要深刻很多面试官他自己没有 debug 过的真的，但是就怕你真的碰到一个 debug 的面试官，那就不好糊弄了，他肯定会问你书上考察不到的问题的。


OK 那这里拿到 handler 以后怎么办呢？看到这里 proxy 这个 proxy 是谁？大家觉得是哪里出来的嘞？如果你说是 spring 里出来的嘞，那说明你对这个 Java call 要补一补知识了，这个是 reflect ，Java的 reflect 包中鼎鼎大名的泪在以前1.7， Java 1.7 以前都是吸引火力的地方面试经常会问到的。
那像 1.7 以后，因为 Java 里面的内容日渐丰富了，所以说大家都会把注意力转向一些像 concurrent 里面的底层机制，包括 1.8 中 lambda 函数，它是怎么来实现的？底层机制是什么？如果让你自己设计一套 lambda 你打算怎么来设计，那可能都会转向这种问题。


那反射曾经是早些年经常会问到的问题。那我这里拿 proxy 做什么事，拿 proxy 创建一个 proxy 了还能做什么事啊？但是创建 proxy 的时候我要传入什么？我要传入 handler 为什么？因为你是一个代理对不对？你要把请求委托给另一个实体类来处理，你自己这个空代理是个空架子，就像你 A 股的股票你是个壳公司对吧，你里面没有东西。那你要把投资者的价值转向到后面一个真实的资产。这个 handler 就是这么一个真实的资产，所有对这个 proxy 调用的请求都会绕地球三圈转到了 handler 的这个类里。


OK 最后一个循环通常来讲进不去。那如果你设置了一些 default method handler 那它会怎么样啊？它会把它绑定到这个 proxy 里，就是我们刚才创建这个代理对象。不过这里既然没有设置，那就返回。 OK 那走到这里，大家拿着这个proxy ，这就是这个 fin 的精华部分所在精华之一。那我们返回，返回，返回到最顶点。那他所有请求都已经处理完了，这个 load balancer 也可以返回了。


好， get object 宣告结束。恭喜同学们取到真经。那在结束之前，我还想问同学一个问题，你觉得写代码有趣还是阅读源码有趣哪一个更有趣一点？我觉得是 code review 最有趣。一个团队汇集在一个会议室里。像开批斗大会一样，一个成员把自己代码投到屏幕上，其他人七嘴八舌。你这里不能这样写，那里不能这样写，这个批斗大会很有意思的。当然在外企里面可能常见一些互联网公司哪有那功夫给你开这种批斗大会对？不过这样也是一种快速学习积累经验，做思维碰撞的一种好的方式。


所以对于同学们来说，如果没有这种批头大会的机会，尽量的多看源码，尽可能多的涉猎这些鼎鼎大名的开源项目的源码。当然了，尽信书不如无书，开源项目的源码也不是都是好的，也有史山，也有写的非常杂乱无章的地方这个都要辩证的来去看。总之读万卷书，行万里路，多读代码总是好的，开卷有益啦。同学们好，这一章我们就到此为止了。那么下一章带同学们换个口味，我带大家看一下 fin 项目，还有另外一种构建风格。呦用了这个风格之后，你的代码量还可以进一步的减少。很期待，那我们就下一节再见



