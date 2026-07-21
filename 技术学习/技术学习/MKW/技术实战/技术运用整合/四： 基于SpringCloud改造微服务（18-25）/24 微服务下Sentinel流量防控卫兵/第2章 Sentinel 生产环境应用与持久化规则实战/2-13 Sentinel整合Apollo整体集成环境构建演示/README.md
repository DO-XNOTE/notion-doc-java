---
title: 2-13 Sentinel整合Apollo整体集成环境构建演示
---

# 2-13 Sentinel整合Apollo整体集成环境构建演示

[image](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/904475b1-2c65-4682-a43d-2fb94548cbbb/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WK43YS74%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T225849Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQC10VE2JylrOM5HARwYIHxtf4xCa2s5v6pfuRBkdPLyygIhAICBwXgFk%2BFxtodPYf47XM7A4uoK1YEu8r5cKAyXEJoSKogECMb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgyQBNtX7FxJ%2FXFLh7Yq3AO0BwtC%2FGOzindZe30SCg04o0CYswwWBdSoJvTU2IwNlAbS9h0530EyHCTPyScRL6uyYV%2F0Vxg%2Fd02nHMWq%2FNP9DOc6N%2FqxE7rqESM5JB%2Ft1LxtRaWjPjwPT%2BGM%2Fb8bHLu7RZJC3x%2BugOP0BwgG0cwURqRNZ7L8nOSWuxpL6H33dbd0fXv659LcHvjgxCwyhqiDNyWYoWB58g1RUXIWpIPEphqvkrOnat0652j8ONpAfUscCPneywLCXpzNHz5c9eJsuXqwv6CcU%2Fkz7GsRT%2BbSzio5q8nG4UPIcdKtEkpLWBsHBSvthpqiz7wyANJXrF9nOIPAj3h3LramQyv0w9mJjTgjOBysDkknEeTflFdZputO3KUsoNis96mV6pVC2WDqLn57f7pjlqjr%2FaSKpcN5NRlo%2FyaWIG6H4E%2F%2FFDwEP%2FRvT21dZZyrMoPtZ2BZMMQ2BQ%2FVQJEyiifIWpp2frZal63AEvvlLOjYRigffjmPpmp2bxZ9C8zVfKB8rIVq6Fim3dNfAeTemXNu567rSmrNyk0yCpMsewsUeEAgDkSrwXOiJ52bVOgMtkGFADpVOPBBG4BL7gpFR7Iart2NyEFVe0hbCgUaXZfv1AAxUmyS%2BFo6u5MOBvrm83U1XjCYt%2F%2FSBjqkATGXW%2BY2WBYhUSHFB741y3vULR05XPxaKJcdKfO4EFkxlUq6RRVK4i9%2FrDxDkuPHp620hwRFFxEcb8Vpj56QWad7ubVjrTE46P9LS%2F6%2FHjaFpYLYdvzD8sVv8VP1pNPpQKuCpa2T4eNidPBH3g46wRnHaT4wrr87fAnOvfLWYw1nznAjtCZIQWVLVvxXiC22K4tmv0d0AEYX2oTaJG%2FCJB2HlDEX&X-Amz-Signature=0eb9e8bc24486667d67adc84af98ad6c9f678b55dfe32ff4e1f77e57c2d22d48&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

[image](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/86555c1a-f873-401a-8c06-c6f6b43641e9/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WK43YS74%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T225849Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQC10VE2JylrOM5HARwYIHxtf4xCa2s5v6pfuRBkdPLyygIhAICBwXgFk%2BFxtodPYf47XM7A4uoK1YEu8r5cKAyXEJoSKogECMb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgyQBNtX7FxJ%2FXFLh7Yq3AO0BwtC%2FGOzindZe30SCg04o0CYswwWBdSoJvTU2IwNlAbS9h0530EyHCTPyScRL6uyYV%2F0Vxg%2Fd02nHMWq%2FNP9DOc6N%2FqxE7rqESM5JB%2Ft1LxtRaWjPjwPT%2BGM%2Fb8bHLu7RZJC3x%2BugOP0BwgG0cwURqRNZ7L8nOSWuxpL6H33dbd0fXv659LcHvjgxCwyhqiDNyWYoWB58g1RUXIWpIPEphqvkrOnat0652j8ONpAfUscCPneywLCXpzNHz5c9eJsuXqwv6CcU%2Fkz7GsRT%2BbSzio5q8nG4UPIcdKtEkpLWBsHBSvthpqiz7wyANJXrF9nOIPAj3h3LramQyv0w9mJjTgjOBysDkknEeTflFdZputO3KUsoNis96mV6pVC2WDqLn57f7pjlqjr%2FaSKpcN5NRlo%2FyaWIG6H4E%2F%2FFDwEP%2FRvT21dZZyrMoPtZ2BZMMQ2BQ%2FVQJEyiifIWpp2frZal63AEvvlLOjYRigffjmPpmp2bxZ9C8zVfKB8rIVq6Fim3dNfAeTemXNu567rSmrNyk0yCpMsewsUeEAgDkSrwXOiJ52bVOgMtkGFADpVOPBBG4BL7gpFR7Iart2NyEFVe0hbCgUaXZfv1AAxUmyS%2BFo6u5MOBvrm83U1XjCYt%2F%2FSBjqkATGXW%2BY2WBYhUSHFB741y3vULR05XPxaKJcdKfO4EFkxlUq6RRVK4i9%2FrDxDkuPHp620hwRFFxEcb8Vpj56QWad7ubVjrTE46P9LS%2F6%2FHjaFpYLYdvzD8sVv8VP1pNPpQKuCpa2T4eNidPBH3g46wRnHaT4wrr87fAnOvfLWYw1nznAjtCZIQWVLVvxXiC22K4tmv0d0AEYX2oTaJG%2FCJB2HlDEX&X-Amz-Signature=3f408f15d3704b6f3f397101c1ad5f7e79af4d0f42b2851a63b5f07a215ed281&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

那么上节课我们已经对应的这个客户端，然后怎么去跟我们自己扩展的这个 dashboard 集成整搞定了。那么这节课我们就来做一个测试，来看一看我们现在做的这些事情到底 O 不 OK 能不能实现我们的这个最初的想法。


好了，现在我们就打开我们自己的这个阿波罗杠 test 它就是一个客户端对吧。然后我们来写一个小程序来测试一下。好了，首先我们现在比如说我们加一个新的 service 第二 service 然后这个 service 我们给它起个名字。因为我们现在目前只是实现了这个流控的策略，所以说我们写一个 follow service 可以吧，那 follow service ，然后就 at service 然后在这里面我们写一个方法叫做 public 然后返回值比如说是子类型叫做 test 反正就是测试我们需要 test at sentence resource 然后这个资源它里边有一个这个 value 然后还有一个比较关键的就是降级的策略对吧，就是我们的这个 block handlerblock handler 我们叫做 test block handler 可以吧，我都小写了。


然后现在这个资源名字，我就给它起一个比较简单的名字，咱们就叫做它的这个包的权限命名，然后加上这个类名点方法名 test 可以吧。 OK 那这个就是我的资源名字为什么我这样去写，因为这样的话才不会冲突？如果你说你自己就定义一个这个就是比如说我定义一个 test 就直接取方法名 test 的话，那这样的话后面你其他类的资源可能也叫 test 那这样就冲突了。所以说为了避免这个资源冲突的问题，解决资源的唯一性的问题，我们一定要用这个比较标准的写法，这是官方推荐的。


好了，那接下来我们在这里边我就打印一句话，比如说叫 system 的 out brain 叫做正常执行。可以吧。在最后我们返回一个就 return 一个字符串，就叫做 test 可以。好，然后这是正常执行的时候，然后异常异常执行肯定会走。这个 block handler 就是降级流控的时候，那这个方法名是一样的， string 返回值类型也是一样的。方法名要跟定义的 block handler 一样。然后这里边可以加一个额外的参数，就是异常 block exception 然后我写 bex 或者是 ex 吧，然后我在这里边 return 一个叫做流控执行，然后我再打印一句话可以吧，流控执行可以吧。然后再加上一个逗号，把我们的 ex 也打印一下。


好了，那这样的话我们整个的这个 follow service 它的代码就写完了。然后我们在这个 ctrl 里边我们做一下测试。比如说我们把这个东西粘过来，粘过来之后我们再写一个 test 对不对？然后把这个都去掉。返回值类型是什么呢？就是把我们刚才所定义的这个 service 给它注入进来， all to weird 我们的 private 我们的 follow service 对吧？然后 follow service 然后我们调这个 follow service 的 test 方法就可以了。对不对？好了，那这样的话我们整个的这个测试的代码就搞定了，然后我们紧接着就开始进入测试。


那进入测试首先第一点就是我们要启动我们的 dashboard 然后我们的阿波罗注意老师那个阿波罗一直是开启的状态，它一直是起来的状态，看见了吧。然后我们的 dashboard 我们先把它运行在这里，当然我不确定她能不能一次成功，可能会遇到一些小问题。不过我们到时候根据他的这个报错信息，我们就能找到最终的结论，然后把它修改过来就好。因为我封装好了这个 dashboard 我也一直没做测试，所以说我们要现在正好趁着这个机会做一下测试。


接下来启动我们的这个自己的客户端程序 test 服务是吧，把它启动起来。然后最后我们都启动起来之后，它的端口号应该是8001，我们来看一看。然后我们去访问下面的这个 test 服务可以了，然后在这里我们开启两个窗口，第一个窗口先让它懒加载 8001 test 对不对？回车。


OK 这是没问题的。好了，然后接下来我们这个窗口就访问我们的 hdp 冒号8080，就是我们的 dashboard 服务。好登录一下。 OK 现在是没问题对吧，就是我们自己的可量端这个应用服务已经完美的集成到我们的控台上了。然后我们看看触点链路，也有资源链路，就是我们已经显示出来一条资源了，就是我们 com.bfxy 点阿波罗，点 service.follow service 冒号。然后 test 接下来我们就来验证一下，我们加一下流控策略，看看。 O 不 OK 我们比如说单局阈值设置成5，然后点。这个新增失败了，看见了吧。 OK 那失败了，我们怎么去找问题呢？那我们来看一下它的这个报错。


当然这个报错肯定是 dashboard 报错，因为跟我们的这个 client 端没关系，我们看它报错是什么报错原因说你在创建这个新的资源的时候，也就是说我们的阿波罗的 client 他去访问这个阿波罗的时候，他出现了一个问题，主要的问题是说这个规则。


然后 for App ID 在 create 的时候 failed 对吧？那你要检查一下你的这个 name space 我的 name space 默认是什么？ name service 应该是 application 然后我们不着急往下去找看一下。 cospact 就是原因引起于它这里边会报一个 404 的错误，看见了 request to 阿波罗 open apf file 的，然后 states 404。然后原因是什么呢？就说 message 他说 not font exception 说资源没有找到说 name space not font for 阿波罗 test 这个应用，然后 default default 这可有问题，是不是？因为我们的默认的内部 CS 不是default ？我们来看一看我们默认的内部 case 是不是我配错了，如果不是我们配错了，就是我们写错了。


在我们的 dashboard 里边，我们找到我们的 application.parties 我们默认的 namespace 应该是 application 但是现在的 namespace 竟然是 default 这个原因大家看到好了吗？其实，像阿波罗在集成的时候，调用 Open API 的时候肯定会出现这样那样的问题，它有一些报错信息，我们怎么去找呢？在这里老师教给大家一个简单的方法，我们打开阿波罗的开放平台，然后拉到最后。就如果说你出现她访问出现异常报错，他肯定会有一些错误的原因。扣的码，我们来看一看。


错误码如果是 400 就是 bad request 401 就是没有过期了， token 过期了对吧，或者 token 传的错误，就是你连错了 402 就是访问没有被授权或者是你的 name says 管理权限没有得到，这是403。然后 404 就是资源不存在或者是 URL 参数错误 405 就是什么呢？这个不正确调 pose 方法，你用 get 方法那肯定不行，500就是服务器内部错误，那大体上已经其实这几个错误已经说得很清楚了。


那我个人觉得我们现在把这个服务都停掉，我个人觉得肯定是我们代码哪个写错了，可能我们要设置 name space 的时候，我们设置的是 class name 变成 default 了，我们来检查一下代码就好了。好了，现在我的服务都停掉了，然后我们现在来检查一下代码在哪里去设置的，就在我们自己的这个，我们来看一下这个 name space 是 application 没问题对吧，应该是在发布的时候，我们刚才是点击 dashboard 的流控去新加规则的时候。所以说我们应该找到这个 controller 找到 controller 里边的新加规则。那对应着这个 provider 他做什么事情？我们来先点开。


provider 是获取规则对不对？我们来看一看获取规则里边传递的几个参数，这个应该是没问题的。我们来看一下。第一个 App name 然后 ENV 环境，然后 cluster name 然后 name space name 对吧，这个都是对的，也就是说获取规则应该是没问题的。好，那除了获取规则，我们还有去 push 就是 publish 发布规则的时候，我们来看一下这个规则对不对。首先我们找到具体的这个方法，因为刚才报错就是这个方法出现问题的，我们来看一下这个规则方法。 OK 我们已经看到问题了，是不是？这是可能之前老师写代码的时候有点疏忽。我们第一个，第二个，第三个，第四个参数的时候阿波罗肯菲格点 cluster name 是对的对吧，你看他第三个参数是 close 但第四个是 name space name 但我们第四个还是写成了 default 了，对不对？写成了这个 class 里面我们应该变成 name space 所以说这块有一点小错误，我们把它纠正过来，修正过来。这样的话一会我们再做测试，然后真正发布的时候也是一样的，是不是我们都是这块写错了对吧，我们变成 namespace name 好了，我们来看一看是不是这样的。


namespace cluster namespace 最后是一个人力 CTO 好，这回应该是没问题了。然后我们把我们的整体的项目再重新启动一下，来再做一次测试。 S 报的这块我现在再重新骑起来。骑起来了之后，我们继续重启我们的这个开暗端。好继续重启我们的客单段。等遇到问题不着急，我们一定要看这个原因，然后去分析这个原因，再去精准的去定位问题就可以了。我们来看看试试这回到底 O 不 OK 好了，那接下来我们再次的去访问一下 test 访问这是没问题的。然后我们再次去访问一下 dashboard f5，然后点击登录出点链路对吧？还是到这里边？我们加一个规则 5 点新增。好。同学们请看这回已经成功了对不对？这回我的规则成功了，看见了吗？我看到了这个添加了。那这个添加从哪取的呢？比如说我们点到这我们一点流控规则的时候，为什么能取到这个规则，这个是从阿波罗里去取的，小伙伴们你一定要知道，而不是说再次去通过 dashboard 去调用我们的 client 端到 client 端内存里去取得了。不是这样的，现在是直接从阿波罗里去取的了，可以验证一下。


我们看一看我们阿波罗的配置中心在这里边，我们刷新一下这个规则，我们直接点到阿波罗 test 我们来看一看这里边已经有了我们自己的规则，看见了，把它打开这里边就是我们我把这个放大一点，我们来看一下这规则就是我们的 App 是什么？是阿波罗杠 test 我们应用服务，然后这是 config 配置，这是具体的。


其他的这是我们刚才设置这个流控策略对吧？然后我们具体的 resource 资源这些内容都已经更新到阿波罗上了，它是一个数组，对不对？它是一个 list 数组，如果你有多个规则，它肯定是逗号分隔的对吧？好了，现在我们的资源已经成功的到阿波罗上了，然后我们现在可以做一下测试对不对？这个 test 我去多访问几下他我设置流控是5，然后我再访问执行流控了，看见了，这样就已经执行流控了。那我们来看一下后台。你看正常的流控，已经执行了正常执行，然后流控执行。流控执行无非就是已经走到了我们的具体的代码里的下面这一块是吧，这是正常执行，这是流控执行好了，第一步我们验证完了，然后我们再紧接着验证。第二步怎么去验证？第二步，比如说我现在把它规则再改了可不可以？这个规则我们是不是可以做修改？就直接在这点编辑。比如说开始 15 我设置成 3 可不可以？然后点保存好没问题。然后我们实时我们再去刷新，再点一下留空规则，看这是阈值是3，我们到阿波罗里边我们来看一下这个配置来刷新一下，我们再点开。好，同学们请看这个 count 现在是几了，现在是3，也就是说我们 dashboard 跟我们的阿波罗做新增修改，甚至说删除操作应该都是好使的。


然后我们再测试，我们这回稍微这个我多点击几次就能看到这个流控规则了对不对？所以说现在也是没问题的，基本上执行三次它就会被流控看见了，之前是得执行 5 次才被流控，现在我点的频率再稍微快一点点，它就出现流控的这个降级的了，也就是说现在它能够动态修改，这是第一点。


好，那现在我们想要的第二点是什么呢？就是我们的这个阿波罗 test 服务，我把它停掉，这些规则不会丢失，这些规则还是保存到阿波罗里边，然后它能够再帮我们去加载，这是我想要的一个结果。所以说现在我的 dashboard 服务我不停，我把我的这个服务你给它停掉，就是我们的这个客户端程序，我把客户端程序停掉，我点停掉，就把这个稍微耐心等待一下。


好了，现在我们的客户端程序已经停掉了，我们的 dashboard 程序还是在起着的，对不对？好，那这个规则我能不能取到了呢？我们来看一下就好了，现在就相当于你现在访问肯定不行了，因为我们的这个 test 服务已经停了，对不对？所以说在这一直等待，但是大气报的我们来刷新一下，触点链路是没有的，因为这个触点链路现在确实是没有的，但是我们流控规则你看流控规则还是有，因为流控规则它是从阿波罗里边取的，是不是从阿波罗里边取的？那我们再刷新几次，等它服务发现那个超时就是这块，这现在是一杠一，就证明有一个服务都有，等什么时候变成零杠一的时候就证明这个服务就确实没了，我们再去点的时候它会报异常，对它会报异常。看见了吧，因为我们那个服务都没起来。


那现在我们怎么去做呢？我们现在直接再重启一下我们这个 test 服务，重启直接启动，我重启来以后，然后我再去访问一下这个界面。有了 test 之前我们重启的时候规则也都没了，这回我们来看一看，我们重启的时候规则还在不在，小伙伴们来看看见了吗？这回重启的时候我们规则既然是还在的，然后我们再次刷新几次也能够执行留空。我看见了吧。也就是说这种方式才是一个规则的持久化的方式，就是我们的 dashboard 跟我们的这个阿波罗能够完美的集成在一起，把这些我们已经配置好的规则都持久化到阿波罗上。这样的话我们本地的应用程序一重启的时候，它的规则也能加载进来。对不对？它的规则就是从阿波罗上去加载的。说白了就是我们之前的那个监听，它能够先第一步在做阿波罗 date source listener 的时候，就是我们之前写的代码，直接监听到，然后刷新到本地内存了，它就这么一个逻辑，所以说这是一个完整的集成方案。


好了，那基本上剩下的内容比如说我们现在只是针对于流控规则做了一个这个设置。再比如说相机规则，因为降级规则我现在没写，所以说你现在点肯定它会报错不好使对吧，你比如说我针对它再设一个降级规则，我怎么去设它都不好使。因为它现在用的还是最原始的模式，就是 dashboard 直接跟控制台交互了，所以说我在这就不做测试了，你可以去试一下。


当然这样你肯定是有的，比如说我设置异常数，我设置 4 个，然后一秒钟我点新增，那有肯定是有，但是这个规则它可没持久化到阿波罗上，不信我们再刷新一下配置 f5 你看它现在就一个规则，就是我们的流控的规则，针对于这个服务的对吧，你应用程序只要一重启，那么对应着你的那个内存里边的就是 dashboard 里边的这个降级规则也就没了，这个我就不演示了。 OK 那其实我们整个的这个萨特斯哨兵在实际工作中怎么去使用以及这个持久化的这件事情就已经大功告成了。好了，感谢小伙伴们收看。



