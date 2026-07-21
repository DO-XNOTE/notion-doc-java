---
title: 2-7 Sentinel整合Apollo持久化规则扩展思路详解
---

# 2-7 Sentinel整合Apollo持久化规则扩展思路详解

[image](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/e725339a-52d9-4449-92ca-1d9c3cdad021/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46674T3OZJQ%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T225845Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIDqazaoclSxHwudsChbf4cKzznKgId19U3Kie5a4179dAiARufFGduXQvSABdYfdETBC8yZ1poGPoJrllnIOGReBtSqIBAjG%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMpGKLT8PGYAoulTbmKtwDrUUgpa2bgglpEoN4WLDNQq%2FpHs7aNPVZDMhJryyjcrXgMvZtCGOkgax5MXP7UQxG19Pg9k7xFeTVekuVPtbnPXzGslji%2BLDNUOgNV7jtix2eHPHqdvLeaOfrDmzv9H%2BvjlqZuNWtPiRkdbvQBi5yD0GmmjaX%2BlhsTnU5eqpyhd%2ByXa53xY0lRwxk6pFefUtqaOfXj962EqCUrsLOEJ034yReiSUzEyqYC6bc2VmmGCFxkburtyAhCJ09pfcoosvDt8yJneNziBhk%2BWlD7GIRePz%2FUMwyG%2FUOSmYjLywlku%2BN4FNKe4YrfZlGzKGSHPCTVgCbrUEqVxuyGKFXhSf%2B6MR7IL9edTYLviBeK3cZg1Hydb9KYY5Nm0rCZNajxxIt0S51U4PcoxPpZP1tKNy%2BMOvystQPvOpsNdm3YhGz%2BHCt2zeaTqvKms9NNd0p2s2npXvY6JdxJh0goopCEhZAkKzi5mSivKGyl44O88SF%2BM74JQrnl8fTwwtvEIZx1wWSAL5%2BWKnukcAvluem3n1XwPoin3beQ75ELH4aYqw8MlwwhngSfgtJ9%2Bt%2F%2B6ZRBs%2BZ8jd%2FtIganVbMo3sS1Zn5DsgyPdU3duVAbCiM1oRmyTTa15wJJ2AFWZ%2Bya4Ywobr%2F0gY6pgEuk07mfLh4E0Pc%2FB9oh1oxxtpubRXaL6jEjUVU1wSLrlhxlnLax13OAY4MKgZOfk2rgBIb5V4yf2iwMgPhJATKDxZwmkT24EZJ7hKLl9ErxoUgLQ%2BAKlwDiqgsBMLLTG3M3wzAKcg%2FOJDlC15yFBs8Ff0E2L2F4yut98Od%2BWnv6NllqhQ6bOe%2Be4HH3uEDR2DmRf%2FqRN3Os%2Fjc68UYmlw5N99j7owB&X-Amz-Signature=9c1a281e866ae2a18243ade0ede0beddf11e6f7874c84fcc3cffb8216870113a&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

[image](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/235e1d75-9a43-4569-8d7f-4185e98258bb/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46674T3OZJQ%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T225845Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIDqazaoclSxHwudsChbf4cKzznKgId19U3Kie5a4179dAiARufFGduXQvSABdYfdETBC8yZ1poGPoJrllnIOGReBtSqIBAjG%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMpGKLT8PGYAoulTbmKtwDrUUgpa2bgglpEoN4WLDNQq%2FpHs7aNPVZDMhJryyjcrXgMvZtCGOkgax5MXP7UQxG19Pg9k7xFeTVekuVPtbnPXzGslji%2BLDNUOgNV7jtix2eHPHqdvLeaOfrDmzv9H%2BvjlqZuNWtPiRkdbvQBi5yD0GmmjaX%2BlhsTnU5eqpyhd%2ByXa53xY0lRwxk6pFefUtqaOfXj962EqCUrsLOEJ034yReiSUzEyqYC6bc2VmmGCFxkburtyAhCJ09pfcoosvDt8yJneNziBhk%2BWlD7GIRePz%2FUMwyG%2FUOSmYjLywlku%2BN4FNKe4YrfZlGzKGSHPCTVgCbrUEqVxuyGKFXhSf%2B6MR7IL9edTYLviBeK3cZg1Hydb9KYY5Nm0rCZNajxxIt0S51U4PcoxPpZP1tKNy%2BMOvystQPvOpsNdm3YhGz%2BHCt2zeaTqvKms9NNd0p2s2npXvY6JdxJh0goopCEhZAkKzi5mSivKGyl44O88SF%2BM74JQrnl8fTwwtvEIZx1wWSAL5%2BWKnukcAvluem3n1XwPoin3beQ75ELH4aYqw8MlwwhngSfgtJ9%2Bt%2F%2B6ZRBs%2BZ8jd%2FtIganVbMo3sS1Zn5DsgyPdU3duVAbCiM1oRmyTTa15wJJ2AFWZ%2Bya4Ywobr%2F0gY6pgEuk07mfLh4E0Pc%2FB9oh1oxxtpubRXaL6jEjUVU1wSLrlhxlnLax13OAY4MKgZOfk2rgBIb5V4yf2iwMgPhJATKDxZwmkT24EZJ7hKLl9ErxoUgLQ%2BAKlwDiqgsBMLLTG3M3wzAKcg%2FOJDlC15yFBs8Ff0E2L2F4yut98Od%2BWnv6NllqhQ6bOe%2Be4HH3uEDR2DmRf%2FqRN3Os%2Fjc68UYmlw5N99j7owB&X-Amz-Signature=dbafafba8bbab0db1444d99767da321cabad3062a4e55ff0bc3d1c2d248f66ec&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

大家好，这节课我们开始进入 sentence 整合我们阿波罗的这个 OpenAPI 这么一个扩展主要做的事情，就是这个规则持久化的事情。好，那在此之前，我们先把我们之前的这个 demo 运行一下，我们在这里采用 debug as 的方式去启动 debug 艾子我们的这个 spring boot application 为什么说非得采用 debug 的方式呢？因为我们要跟一些断点好了，启动起来之后，现在把我们之前所做的那个 demo test 这个应用程序也启动起来，demo test 里边我们就直接也是 spring boot application 在这里就 run ADS 就可以了。启动起来以后规则加载完毕对吧。


好，现在我们就可以直接通过浏览器我们去做几个访问，在这里边我先把这个没有用的东西我关掉。好，我们现在先访问 HTTP 冒号 local host 8001 访问我们自己正常 8001 的这个，比如说随便访问一个流控或者访问一个降级是吧，我们访问一个流控杠 test 这个还记得吗？流控杠 test 这个是我们用 annotation 注解去做的。然后还有一个 degree 就是我们的 degree 的高 test 对吧。都成功了。然后紧接着接下来我们再打开一个窗口， HTTP 冒号杠杠 local house 8080 访问我们控台大字报的，因为它是预加载，但是我都已经访问了，所以说你已经看到了这个 demo test 程序，然后我们看它的实时监控触点链路。


现在有两个触点链路，一个是我们的这个 follow service 的 follow 方法，还有一个是 grade service 它的这个 degree 的方法。然后它的规则你会看到流控和降级规则什么都没有。好。那现在比如说我想给它加一个流控规则可以吗？这是没问题的。比如说我想给它加一个流控规则，说 QPS 单机阈值最多是每秒钟 5 次，然后点新增搞定了。好，现在有这个单机的阈值是 5 次了。当然这个五次是在内存里的同学们还记得吗？我现在比如说我去定义我说 follow test 我刷新是不是 follow 然后我快速的去摁几次，你看快速的摁几次它就可能就被流控了。对不对？执行流控方法了对吧？这是我们之前的 demook 这是没问题的。我们通过这个界面后面的控制台输出，你也能看到同理 degree 的降级也是一样的。但是小伙伴们还记得吗？比如说我把这个 demo test 停掉以后，这个 demo test 我停掉了，我直接停掉。停掉了之后，小伙伴们我再刷新一下我们的 dashboard 上 f5 刷新一下，你看现在才会显示0，它不是马上剔除的。


然后同学们请看这个触点链路，包括我的服务，我再次去启动一下，我们看一下，我再次去启动一下这个 test 服务对吧，我去启动我再次启动的时候，小伙伴们发现了一点，就是之前我配置的那个流控规则没了对吧？比如说我懒加载一次，我还是访问一下流控，再访问一下。


great 好，然后这回我们再刷一下dashboard ，然后我们再看素材链路是不是还有这两个。但是流通规则，我之前所设置那个 5 都没了对吧，这就是一个问题，就是说我们现在 dashboard 直接是跟我们的这个 client 端进行 HTTP 传输的。那现在我们要做的事情是什么呢？我们要做的事情让 dashboard 不去对我们的 client 端去发 App 请求去操作，而是直接去更新我们的配置中心阿波罗。把刚才我们所做的规则都给它持久化到阿波罗上，我不知道小伙伴们能听懂这个意思吗？那就是要做这个事情。 OK 好，那我们现在怎么办呢？我们现在对于这个流控的，它这个流控有降级，有热点对不对？我们先以流控为主。我们先看一下这个流控规则它对应的源码是怎么去做的。

[image](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/746e7752-a438-4cef-a47d-0d77da91c143/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46674T3OZJQ%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T225845Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIDqazaoclSxHwudsChbf4cKzznKgId19U3Kie5a4179dAiARufFGduXQvSABdYfdETBC8yZ1poGPoJrllnIOGReBtSqIBAjG%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMpGKLT8PGYAoulTbmKtwDrUUgpa2bgglpEoN4WLDNQq%2FpHs7aNPVZDMhJryyjcrXgMvZtCGOkgax5MXP7UQxG19Pg9k7xFeTVekuVPtbnPXzGslji%2BLDNUOgNV7jtix2eHPHqdvLeaOfrDmzv9H%2BvjlqZuNWtPiRkdbvQBi5yD0GmmjaX%2BlhsTnU5eqpyhd%2ByXa53xY0lRwxk6pFefUtqaOfXj962EqCUrsLOEJ034yReiSUzEyqYC6bc2VmmGCFxkburtyAhCJ09pfcoosvDt8yJneNziBhk%2BWlD7GIRePz%2FUMwyG%2FUOSmYjLywlku%2BN4FNKe4YrfZlGzKGSHPCTVgCbrUEqVxuyGKFXhSf%2B6MR7IL9edTYLviBeK3cZg1Hydb9KYY5Nm0rCZNajxxIt0S51U4PcoxPpZP1tKNy%2BMOvystQPvOpsNdm3YhGz%2BHCt2zeaTqvKms9NNd0p2s2npXvY6JdxJh0goopCEhZAkKzi5mSivKGyl44O88SF%2BM74JQrnl8fTwwtvEIZx1wWSAL5%2BWKnukcAvluem3n1XwPoin3beQ75ELH4aYqw8MlwwhngSfgtJ9%2Bt%2F%2B6ZRBs%2BZ8jd%2FtIganVbMo3sS1Zn5DsgyPdU3duVAbCiM1oRmyTTa15wJJ2AFWZ%2Bya4Ywobr%2F0gY6pgEuk07mfLh4E0Pc%2FB9oh1oxxtpubRXaL6jEjUVU1wSLrlhxlnLax13OAY4MKgZOfk2rgBIb5V4yf2iwMgPhJATKDxZwmkT24EZJ7hKLl9ErxoUgLQ%2BAKlwDiqgsBMLLTG3M3wzAKcg%2FOJDlC15yFBs8Ff0E2L2F4yut98Od%2BWnv6NllqhQ6bOe%2Be4HH3uEDR2DmRf%2FqRN3Os%2Fjc68UYmlw5N99j7owB&X-Amz-Signature=1e5be803e604db2ed66dcd49f6f845b6cbbba62b7bb079e151bf006cf921e66f&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

我们来打开我们 dashboard 源码，来我们找到 dashboard 在这里，这个它就是一个 supreme boot 的工程对吧，我们看到它的里边 application.properties 里边有一些配置，这些配置都相对来讲比较简单，是不是对应着就是 spring 的配置，然后 log 的一日志的一些配置，然后安全认证的一些配置就没了。
好了，现在我们直接就找到这里面 control 了有两个，一个是 V2 版本，还有一个是 V1 版本。那我们现在默认使用的都是这个 follow controller 的 V1 版本。在这里我就直接定位到了，不去看那个界面，他发的请求是什么了。老师直接给你找到 follow control 了。


follow control 了就是专门对流的流控了之后，这里边有一个方法叫做 ruler 丝卢尔斯，很简单就是获取所有的流控规则。那我们在这里打个问点，然后我们实时监控点一下流程规则，看断点直接进来，断点进来之后，我们来跟一下这个断点来看一看。
f6 下一步，首先它有一个认证叫做 author service 就是我需要认证的。拿到认证之后，我们看一下这个 variable 认证是没问题对象，然后他做了一些判断，就非空的一些判断。他给我传的是一个 App 还有 IP 跟 point 这些东西是哪来的？还有 AG D solid request 我们看这几个它给我传来的参数是什么，对不对？我们通过 variable 里边来看一下 request 里边有一些属性。


然后我们主要看 App App 叫什么，名字叫做 sentence 杠 demo 杠 test 看到了吧，这个是我们的 App 应用名字。那这个名字是怎么去配置的呢？我在这里很简单，因为我在这里保持的都是一致，我们不用 debug 模式，回到正常的模式，刚才启动的这个应用就现在还起着这个应用，就是 sentence demo 杠 test 然后它在里边我们右键 run ADS 我们找到 configuration 还记得我们在这里配置的这个 arguments 参数吗？这里边有一个 D [project.name](http://project.name/) 我配置的，这个名称就是你自己克兰端的 App 它的名称就 sentence 杠 demo 杠 test 对吧。所以说它在这里边首先我们再回到 debug 所以说这个 App 那个名称就是你在 arguments 启动的时候添加的配置。你要知道 IP 就是你当前 client 它的 IP 是什么？ point 也是一样的。 author user 这是认证的 userok 我们知道这几个参数之后，看一下这个 ruler 到底是怎么去做的。我们来看一下这个规则从哪来？点点点进去之后，我们发现有一个什么呀？有一个叫做 sentinel API client.fetch follow ruler off machine 这个方法做的是什么呢？我还不知道。然后我下一步我们看它的返回是空，对不对？ OK 我们就停掉不管了，现在这是没有的，对不对？没有任何规则。


那我们现在来加一个规则试试，我们在触点链路里边还是把这个流控的规则加一个，我说这个流控规则单机的 QPS 我设置成5，然后点添加，点添加之后我们直接结束，其实它直接就会跳到流控规则这个里边，你看这个流控规则就有了，单击 QPS 5，然后我们重新再访问一下流控规则。


又进来了对吧，还是进这个 rules 这个接口。这一回我们往下去点，我们看这个 API client 其实你可以跟进去代码 f5 跟进去，然后 f7 回来，然后再 f5 进去。好同学们请看这里边到他的这个 fetch rules 这个 fetch ruler 是从哪里去调的呢？它的规则是叫做 follow 然后 IP 是什么 IP 是我们之前的幺九二点幺六八在 11 点二端口是 8720 对吧。然后我们再点 fetch 点进去 f5 进去，然后 fetch items 我们再点进去。


好再往下 F F f6 我们直接走到这个 fetch items a single 就叫做异步的去 fetch 然后最后就是一个 get 这就是一个典型的 future 模式，我们 f5 点到这个方法好，然后看一下他怎么去做的， f6 怎么去根断点，然后你会看到 excuse command.then play 那这个是什么？这个不就是我们的这个 complete table future 也是一个异步的请求，对不对？然后我们再看看它异步请求做了什么事情，其实你可以点到它具体的这个执行的方法里边。当然这里边他就调了什么 execute command 在 f5 进去。
然后同学们请看你再往这儿看，基本上就知道他是怎么去做的了。你看这是拼一个 htp 请求，然后我再往下走，叫 htp post 还是这个 sport 就不管了。好在这儿同学们请看他真正的发起了一个 htp get 请求，那也就是说我现在在干什么？现在在请求，你看这个 UL builder 它是向这台服务器的 8720 端口取掉 get ruler 然后 tap 等于 follower 说白了什么意思呢？我现在的 dashboard 正在向我们具体的这个 IP 的 client 端去拿他本地 ruler 的规则列表，我不知道小伙伴们能不能理解。
那也就是说我现在应用服务起的是两个看见了，一个是什么？一个是这个 sentence demo test 一个是 dashboard 刚才我那个请求是我通过 dashboard 向我们的 sentence demo 杠 test 发送 HTTP 请求，然后去拿 ruler 流控的一个规则列表。说白了就是去它内存里去拿对吧？ OK 这样的话小伙伴们就懂了。


那么也就是说每次我在列表里展示的这些规则是从哪来的？它就是从我们自己的这个 sentence 杠 demo test 那个服务的内存里边去抓过来的，这回小伙伴们能懂了。所以说当我们什么呢？当我们具体的这个 sentence 杠 demo 杠 test 这服务停了以后，这就拿不到规则了，再重启这规则都没有意义了。所以说我们现在要做的事情就是这个规则要做一个持久化的策略。那对应着的我们怎么去做持久化呢？现在我们看一下，再回到这个源码之前， V1 的这个 ruler 它最终调的是这个 sentence API client 那 sentence API client 它做的是什么事情呢？它完完全全就是一个 HTTP 的请求，它就是一个 closible HT PA single client 然后无论你做什么操作，比如说刚才我们去获取规则对吧？然后你比如说我们再换一个，那我这个获取规则列表我们知道了，添加规则我们来找添加规则肯定就是比如说 add user 或者是 save ruler 这个是 API add follow ruler 对不对？你看它调的完完全全是一个 save 方法，我们断点导到这儿，现在我们先把这个规则删除，直接。


OK 删除了以后，然后我们再到处理内容里面，我再重新加一次。我76，然后点添加进来了，进到这个入了方法里了，我们来看一下怎么去加的 my f6。下一步直接它是相当于把我们的一些规则什么的都生成一个对象，就是 entry 对象。然后你看这个安全对象里边有哪些，一会我们来看一看。


然后这个 repository 的 save 是什么鬼，先不用管，我们先看一下这个 entity 到底是什么内容，这个 entity 里边的属性是不是就是我们自己的一个规则？就是我们自己之前原生的 Java 的这个 API 初始化规则的一个对象。接下来这个 repository 它是什么？它是基于内存的持久化。我们看一下这个 repository 叫 in memory ruler repository adapter 然后叫 follow ruler entity 对不对？所以说这个 repository 它本身来讲它就是一个内存级别的 save 就我自己 dashboard 在我自己本地内存存了一份 f6 搞定存完了之后，最关键的点搞定完这个事情之后最关键的点。其实我们结束之后你往里边去点这个 save 方法，你会看到它在内存里存了一份之后，他又做了什么事情，这叫做什么？母性 rulers 特姆利特 F set 其实我们内存里存完了之后，我肯定要把我之前的那个规则去发送到哪里，叫做 set follow machine 其实你看一下这个方法到底是哪掉的，我们来找一下 ctrl C 来点一下。就是刚才我们的入漏规则，就是刚才我们的 c5 方法，它在这里边，会调这个方法看见了，然后我们在这里也打个断点，刚才可能没进来。好，我们把之前的这个规则删掉。


对，你看删掉的时候她也会走这个 public surest 那你其实你就应该知道这个 publish 螺丝到底干的什么，我重新加一次，我再加离婚规则，给它变成 7 点添加点添加之后，小伙伴们来看一下添加都做了哪些工作，还是走这个入了方法，然后往下走保存内存对不对？保存内存之后看到这儿，他说如果这个东西是等于 true 的话，就相当于等于 false 还要打个 log error 他说 public 是 fail 的对不对？然后我们再直接到这，他肯定会走这个方法。


这个方法做什么事情？首先 find all by 母性，就找到所有的 appip point 下对应的这个魔性泛的奥戴姆逊，找到他所有的规则f6，我们取一下看一下这个规则是什么。找到 wearable 好这个规则，它就一个规则对吧，然后这是我们之前的，这就相当于找到之前的规则，然后去调用什么，相当于调用 HT client 请求了，直接去 set follow of machine 那我们来 f5 进去看一下 f5 进去，然后 f7 出来再 f5 进去。然后我们来看 set rules 对不对？ set ruler 我们 f5 再进去，再往下 f6 下一步你往后看还是这个 command 对不对？还是这个 command 我们在 f5 进到 command 里边。然后你看还是这个拼接 HTTP 请求，然后执行 command 就发送请求结束。说白了，无论我添加规则也好，还是修改规则也好，还是删除规则也好。


我们的 dashboard 先在本地内存里先存一份，然后本地内存存完了之后，紧接着就发送 HTTP 请求到我们具体的应用 client 端，就是我们具体的那个应用服务器叫做什么呢？叫做 sentence 杠 demo 杠 test 就是到我们具体的这个 sentence 配置 client 端，就是把所有的请求再发到对应的 client 端里边，然后让它去更新内存，现在应该能理解了吧？那现在我们所有的规则都是通过大气报的直接发送 AHT 请求到具体的参端的。


那我们现在要跟阿波罗进行集成的话，我们应该怎么做？首先第一点我们要做的事情就应该改很多内容。我现在简单跟大家说一下，我现在先把这两个服务暂时都停掉，大体上整个的这个逻辑大家懂了。那我们应该怎么去做？我们先不考虑其他的，我们就先考虑 VE 版本的这个 follow 对不对？那我要做什么呢？其实这个东西完全就把它注释掉以后，我们去扩展的时候我就不要它了，因为我现在带时报的规则根本就不需要去做推送了，而是我们要把我们的规则直接持久化到我们的阿波罗里边。所以说在这里边我们就需要阿波罗的一个规则。


做这个事情我们获取列表的时候，再不是从我们具体的可看端去取到，然后去展示了，而是你要调阿波罗的那个 Open API 找到它的方法，从阿波罗里边的配置里面取到，如勒斯展示出来对吧，包括后面的一系列的所有发布。我们要直接操作阿波罗了，而不是操作我们具体的这个 sentence 克拉特 API 好了，那基本上我已经把整体的这个思路，还有这个控制台跟这个我们克兰端交互的这块讲明白了，也说清楚了我们要做什么事情，我们直接再做一个持久化的 service 然后是跟阿波罗打交道的就可以了，把原来直接通过 hdp 请求跟我们克兰端打交道的这一块给他干掉，就这么一个事情。 OK 那么这节课我们就先讲到这儿，感谢小伙伴们收看。



