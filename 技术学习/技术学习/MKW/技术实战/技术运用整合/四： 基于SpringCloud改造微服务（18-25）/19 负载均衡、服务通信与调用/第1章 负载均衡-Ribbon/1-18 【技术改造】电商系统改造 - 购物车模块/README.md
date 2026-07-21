---
title: 1-18 【技术改造】电商系统改造 - 购物车模块
---

# 1-18 【技术改造】电商系统改造 - 购物车模块

[image](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/0cb1621a-420c-4b63-84b1-95198b43d653/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TSFNHMSJ%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T225617Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIAP%2F0j8XIzDuF%2BdtKyVyAbOIrxqEBnQpv2X5U0PR5ZKZAiAZFEbOU9B1uaj0FGbo%2FrOw3F8m%2B7%2Bhf6GhFIOaTbDubiqIBAjG%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMzLHzM0TCKGwuEbLMKtwDdaA4joxcWiaBJQCuulnfWZVZ8ImBNWWPseqidZMFa1xxzIGRxKtGqmcEvGq7adt3nFw4nweSMMAZ05T58nyAtBZg37BDgyNtZ0Xhih9AHaEvEwR7NDCkMeHw3aBXODNEL3CDUtZSGBM%2F13zxVs19D%2BGWpt56%2F9cceC0TggjSi7v5tulEqIhAG58JujAI6tC4H2Cehu01GZ6w%2B1ZbrbgJ5gx12MTd9r6sIBhq7TZS925%2F6OA4%2FXR7royHdTJuSlQPUTIoVHNK57sUwxpYv0sBtYx5LZEwcGSj%2F%2FqKrpydBba%2FVutCYTijbprpsfIPl%2Bncl9O1LdlYFn0cOHE5DGP2uyKXNuzsV7AGlYGYIuz1Om2qFYdvBIZsKRD7fAw3DOplnj%2B3nAFdTxXPnBa6YXODw6WSkHu%2FyoMaoYW2vYCZTBTkfDsGDWKJQ9XNM4h1y5RdSXdeRxJSgRC06R04cRgZ13zup2Iguqk%2BGnpfgjwNHu%2Fs94xmanWvNWaMYpO3fO%2FKo48bxvNaT1prTwydNK62pAeMeyLpk2vRQJa2x8Git42OtR%2F3MNuxvkRTH261YcL1u5gubwIho2dZd8Ot7k3SfXgvOH3qn42SJ94CMfcf7sqT%2Bh3wb0ejXlgshQswlbj%2F0gY6pgFlUfgAa7GJWjspNbFwt%2F4zTxqRIyV8C%2BcMpSJfYHuEsPqzSfAAvMVz3u7nv%2FJ29450jjs%2BgztyhFU2rSEr44MCnYkQ30I7A0GAzmZFvXs%2FRxc%2B8b3eGbYLhAnFnDpgMGHrm3UezTkQAJSV6kDN%2BlplSmd0CgssVv1zjhfD0L54kve4ALmUCcIdjTLS6a8i%2BegVJ25iQfG6Epr%2Fp4aZgGrxk16I0o0K&X-Amz-Signature=95922ffb4a28c0462e86fb65302eca139739f8c88003f3baa5b8e8fb82882dbf&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

[image](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/7eed09c7-49a6-4f81-a9e9-4082d8cb7ac0/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TSFNHMSJ%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T225617Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIAP%2F0j8XIzDuF%2BdtKyVyAbOIrxqEBnQpv2X5U0PR5ZKZAiAZFEbOU9B1uaj0FGbo%2FrOw3F8m%2B7%2Bhf6GhFIOaTbDubiqIBAjG%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMzLHzM0TCKGwuEbLMKtwDdaA4joxcWiaBJQCuulnfWZVZ8ImBNWWPseqidZMFa1xxzIGRxKtGqmcEvGq7adt3nFw4nweSMMAZ05T58nyAtBZg37BDgyNtZ0Xhih9AHaEvEwR7NDCkMeHw3aBXODNEL3CDUtZSGBM%2F13zxVs19D%2BGWpt56%2F9cceC0TggjSi7v5tulEqIhAG58JujAI6tC4H2Cehu01GZ6w%2B1ZbrbgJ5gx12MTd9r6sIBhq7TZS925%2F6OA4%2FXR7royHdTJuSlQPUTIoVHNK57sUwxpYv0sBtYx5LZEwcGSj%2F%2FqKrpydBba%2FVutCYTijbprpsfIPl%2Bncl9O1LdlYFn0cOHE5DGP2uyKXNuzsV7AGlYGYIuz1Om2qFYdvBIZsKRD7fAw3DOplnj%2B3nAFdTxXPnBa6YXODw6WSkHu%2FyoMaoYW2vYCZTBTkfDsGDWKJQ9XNM4h1y5RdSXdeRxJSgRC06R04cRgZ13zup2Iguqk%2BGnpfgjwNHu%2Fs94xmanWvNWaMYpO3fO%2FKo48bxvNaT1prTwydNK62pAeMeyLpk2vRQJa2x8Git42OtR%2F3MNuxvkRTH261YcL1u5gubwIho2dZd8Ot7k3SfXgvOH3qn42SJ94CMfcf7sqT%2Bh3wb0ejXlgshQswlbj%2F0gY6pgFlUfgAa7GJWjspNbFwt%2F4zTxqRIyV8C%2BcMpSJfYHuEsPqzSfAAvMVz3u7nv%2FJ29450jjs%2BgztyhFU2rSEr44MCnYkQ30I7A0GAzmZFvXs%2FRxc%2B8b3eGbYLhAnFnDpgMGHrm3UezTkQAJSV6kDN%2BlplSmd0CgssVv1zjhfD0L54kve4ALmUCcIdjTLS6a8i%2BegVJ25iQfG6Epr%2Fp4aZgGrxk16I0o0K&X-Amz-Signature=38097498c495d43a88a21d38e20ed06d0af1d1a72451c13e7f662d29faea930e&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

[image](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/c0b18968-1b0f-459a-affb-e37961e59cde/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TSFNHMSJ%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T225617Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIAP%2F0j8XIzDuF%2BdtKyVyAbOIrxqEBnQpv2X5U0PR5ZKZAiAZFEbOU9B1uaj0FGbo%2FrOw3F8m%2B7%2Bhf6GhFIOaTbDubiqIBAjG%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMzLHzM0TCKGwuEbLMKtwDdaA4joxcWiaBJQCuulnfWZVZ8ImBNWWPseqidZMFa1xxzIGRxKtGqmcEvGq7adt3nFw4nweSMMAZ05T58nyAtBZg37BDgyNtZ0Xhih9AHaEvEwR7NDCkMeHw3aBXODNEL3CDUtZSGBM%2F13zxVs19D%2BGWpt56%2F9cceC0TggjSi7v5tulEqIhAG58JujAI6tC4H2Cehu01GZ6w%2B1ZbrbgJ5gx12MTd9r6sIBhq7TZS925%2F6OA4%2FXR7royHdTJuSlQPUTIoVHNK57sUwxpYv0sBtYx5LZEwcGSj%2F%2FqKrpydBba%2FVutCYTijbprpsfIPl%2Bncl9O1LdlYFn0cOHE5DGP2uyKXNuzsV7AGlYGYIuz1Om2qFYdvBIZsKRD7fAw3DOplnj%2B3nAFdTxXPnBa6YXODw6WSkHu%2FyoMaoYW2vYCZTBTkfDsGDWKJQ9XNM4h1y5RdSXdeRxJSgRC06R04cRgZ13zup2Iguqk%2BGnpfgjwNHu%2Fs94xmanWvNWaMYpO3fO%2FKo48bxvNaT1prTwydNK62pAeMeyLpk2vRQJa2x8Git42OtR%2F3MNuxvkRTH261YcL1u5gubwIho2dZd8Ot7k3SfXgvOH3qn42SJ94CMfcf7sqT%2Bh3wb0ejXlgshQswlbj%2F0gY6pgFlUfgAa7GJWjspNbFwt%2F4zTxqRIyV8C%2BcMpSJfYHuEsPqzSfAAvMVz3u7nv%2FJ29450jjs%2BgztyhFU2rSEr44MCnYkQ30I7A0GAzmZFvXs%2FRxc%2B8b3eGbYLhAnFnDpgMGHrm3UezTkQAJSV6kDN%2BlplSmd0CgssVv1zjhfD0L54kve4ALmUCcIdjTLS6a8i%2BegVJ25iQfG6Epr%2Fp4aZgGrxk16I0o0K&X-Amz-Signature=24645209b00b773b8abe0e8b597dcd0de31bd634a1ff9e431fdd7d813dcea1da&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

hello 我们课网的各位同学们，大家好，那咱这一节又到了电商项目改造，这次我们改什么啊？我们改购物车同学们可能会问了，今儿一节不是学瑞本吗？咱为什么去改造购物车来了？这第一个原因自然是瑞本实在是太简单了，真的没什么好改的。那第二个原因吗？咱前面改了三个模块，这不是购物车和主搜模块还没改吗？那老师闲着也是闲着，就陪大家一起把玩一下购物车。那我们继续发扬超快猛的开发模式，争取 10 分钟搞定购物车。同学们，你台里 J 里见下面我们就来创建购物车模块。
在抖们下面我们新添加一个路径叫做 cardok 在 cut 里，咱创建第一个购物车的模块从哪个开始呢？

[image](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/9d446abb-9992-4a1a-8870-f7bc7325fbfc/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TSFNHMSJ%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T225617Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIAP%2F0j8XIzDuF%2BdtKyVyAbOIrxqEBnQpv2X5U0PR5ZKZAiAZFEbOU9B1uaj0FGbo%2FrOw3F8m%2B7%2Bhf6GhFIOaTbDubiqIBAjG%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMzLHzM0TCKGwuEbLMKtwDdaA4joxcWiaBJQCuulnfWZVZ8ImBNWWPseqidZMFa1xxzIGRxKtGqmcEvGq7adt3nFw4nweSMMAZ05T58nyAtBZg37BDgyNtZ0Xhih9AHaEvEwR7NDCkMeHw3aBXODNEL3CDUtZSGBM%2F13zxVs19D%2BGWpt56%2F9cceC0TggjSi7v5tulEqIhAG58JujAI6tC4H2Cehu01GZ6w%2B1ZbrbgJ5gx12MTd9r6sIBhq7TZS925%2F6OA4%2FXR7royHdTJuSlQPUTIoVHNK57sUwxpYv0sBtYx5LZEwcGSj%2F%2FqKrpydBba%2FVutCYTijbprpsfIPl%2Bncl9O1LdlYFn0cOHE5DGP2uyKXNuzsV7AGlYGYIuz1Om2qFYdvBIZsKRD7fAw3DOplnj%2B3nAFdTxXPnBa6YXODw6WSkHu%2FyoMaoYW2vYCZTBTkfDsGDWKJQ9XNM4h1y5RdSXdeRxJSgRC06R04cRgZ13zup2Iguqk%2BGnpfgjwNHu%2Fs94xmanWvNWaMYpO3fO%2FKo48bxvNaT1prTwydNK62pAeMeyLpk2vRQJa2x8Git42OtR%2F3MNuxvkRTH261YcL1u5gubwIho2dZd8Ot7k3SfXgvOH3qn42SJ94CMfcf7sqT%2Bh3wb0ejXlgshQswlbj%2F0gY6pgFlUfgAa7GJWjspNbFwt%2F4zTxqRIyV8C%2BcMpSJfYHuEsPqzSfAAvMVz3u7nv%2FJ29450jjs%2BgztyhFU2rSEr44MCnYkQ30I7A0GAzmZFvXs%2FRxc%2B8b3eGbYLhAnFnDpgMGHrm3UezTkQAJSV6kDN%2BlplSmd0CgssVv1zjhfD0L54kve4ALmUCcIdjTLS6a8i%2BegVJ25iQfG6Epr%2Fp4aZgGrxk16I0o0K&X-Amz-Signature=5aac0fda2a98e88e3c6d902798f41a4f818b05a852f579a58160e42a92d442f6&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

同学们可能惯性的以为从 pool 开始。其实购物车它没有 pool 因为它唯一用到的那个 shopping card 泡酒放到哪了？放到咱的 common 包下的 share 的 polo 这一个子模块当中了。所以我们并不需要 polo 直接从什么开始创建呢？从 API 开始，那给它起名字叫 hoodie cart API 好，点击 next 那它的路径是 domain cart 321 好这里有哪些 dependency 只有两个，我们把它加进来分别是什么呢？分别是这个 share 的 portal 模块以及 spring boat starterok 那咱这样就开始直接定义 API 层了。
同学们可能有点奇怪，咱购物车的代码大部分都存放在哪里，全部都在 controller 里面。那何来 service 何来 API 呢？老师这里的这个改动实际上是想把 control 里的逻辑下放到 service 层。所以这里咱就定义了这么一个 API 的字母块。


好，这里重新新建一个class ，它是一个 interface 我们把它的名字叫做 card service 那我们在这个 card service 里面定义它的 request mapping 好把它的路径设定为 cart API 那他这里我打算给他三个方法哪三个方法我们来看第一个方法 public 那返回一个什么？那一个布尔值 add item to cart 添加商品到购物车。那它有什么参数呢？有一个 user ID 还有一个是谁是 shop card BO OK 好，那它既


然有添加，自然，这里我要给它加一个删除，叫 remove item from cartok 那最后一个我还想给它添加一个功能，叫什么？一键清空购物车 clear cart 那这里的参数就更简单了，它只有一个什么呢？一个 user ID 那咱接下来分别给这个参数加入 post mapping 第一个它的 mapping 叫添加 item 那第二个自然是删除 item 但是咱这里依然把它写成 post 就不写成 delete 了，因为它不是删除某一个指定的对象。那它这里相当于对购物车做一个修改操作，所以咱这里叫 remove item 最后一个就是星空购物车 clear heart 好，接下来我们给每一个入参添加一个 request param 我们这里复制一下。好，第二个添加上。第三个添加上。 OK 那接下来轮到这个 request body 了。 request body OK 那给下面这个接口的参数也添加上这样一个注解。


好，那咱的 card service 就已经定义完成了。接下来我们就去创建 card service 新建一个茅酒，它的名字起名叫 foodie 杠 card service 点击 next 把路径名指定好在抖 men card 下面点击 finish 321 那这个 service 层它有哪些依赖呢？只有一个，那我这里把它 copy 过来了，这一个就是前面创建好的福地 card apiok 那么这里直接去创建代码层新建冠名商，calm.imock.cart后面跟 series implementationok 那在这里面我们直接创建一个实现类，它的名字叫 cart service IM PL 好走，你那它继承自谁自然而然的它要去实现刚才咱创建的 card service 接口。那咱这里把没有完成的方法全部给添加上去。


OK 这上面添加一个 rest controller 的注解，说明它是一个 controller 然后我再给它加上 sl four G 这样的话方便我打印 log 好，那在这个方法题里面写什么呢？同学们先稍安勿躁，我们先暂时不动笔怎么样？等我们创建好了 controller 之后再回过头来写。因为咱 controller 里的内容同学们是要怎么样呢？添加到 service 里面的，就是把它下放到 service 层。


好，那我们这里再去创建最后一个 module 你看咱的这个 card 只有三个猫居非常少，非常清晰，而这个猫就给它起名福地杠 card 杠 web 点击 next 这里文件夹路径依然是 domain cart 创建完成。那它的泡沫里面都有哪些内容呢？那它的依赖项会稍微多一点。好，我们这里 123 粘贴过来。 OK 我们先来看一下都有哪些依赖。第一个， foodie card series 后面是 cloud common web components 还有咱的 eureka client 那这个启动的节点 build 节点，它的 main class 我们把它指向到了 card 点。 card application 这个类虽然还没创建，但是马上就会有的。 OK 那这里面有的依赖项，咱只是在这边借宿一下，待会还会把它们移地方的同学们往后看就知道了。


好，我们接下来到 SRC 里面，把咱冠名商给它先打上 come.imock 后面是跟 cart 好，这里咱创建一个启动类，我们从其他地方直接把这个启动类给它 copy 过来就把 item application 给它 copy 过来，但是要改一下名字改成 cart 那这里面有些内容需要改一下。


第一个，我们先把这个包扫描路径，它这里要扫谁扫 item.mapper 那实际上咱怎么样呢？咱其实没有任何 map 但是从扩展的角度来说，万一以后有了对不对事事难料。所以咱这里就暂且把它改为 card 店map ，以后有了也就能自动包含进来。那这是一个改变。下面把 card application 在启动的闷函数里替换掉，这就搞定了。


那接下来我们去移植 controller 这里创建一个 package 给它起名叫 controller 然后 car 的 controller 只有一个别无分店。那我们去 food DEV 当中，把这个真身给它揪出来，它的名字就叫 shop card 那我们把它复制到，然后揪回来。


好勒，这里大家首先要更正路径，对不对好，我们这里已经改好了，那咱同学们看一下，目前我们添加和删除，那这些操作的具体业务逻辑都是在 controller 这一层，我们想把它作为一个 service 提供出去。那这种情况，我们索性就把这里面的业务逻辑给它全部移过去，移到哪里移到它的实现类 card service 当中。 OK 那说改就改，我们从第一个接口开始改起。好，那咱接下来先把第一个接口这样从头到尾直接给它全部 copy 下来， copy 到这。好，把这个 copy 下来之后转移到 service 里面，把它扔进去，扔到第一个方法里面。


OK 那这里返回值改成去很简单，那同学们在这里还看到了几个红字，对不对？好，我们这里到 ctrl 里面，把这几个红字也给它 copy 过来。其中有些部分是需要引入 pom 的，我们到这里把这两个 pom 先他拿走，给他拿到哪里呢？拿到 card service 里面，这样的话我们就可以在 card 里面引入依赖了。 OK 那想引入哪些依赖呢？我们先从上往下看。第一个这里是 Redis operator 那我们到 shop car controller 里面，把这个 Redis operator 给它移到 cart 里面，很简单，一过来以后这消除了一个。那再接下来看第二个，好，把这一个也给它引入进来，最后一个工具类。


好，那到这里，第一个方法就移植到了 service 层里，那接下来我们来 controller 里，这个方法给它删掉，删掉以后改成调用我们的 service 层 card service auto wire 加上。那咱这个 service 直接在这里调用它的 add item to cart 把 user ID 给它传进去，后面是 shop card buok 那咱下面这个流程也跟上面保持一样，我们把这里 copy 过来直接扔到 service 层里面。


其实咱的返回时就不去验证了，永远都是 trueok 那咱这里看到还有一个红叉，那好像老师这里粗心了，把这个参数给写错了。好，我们这里把它稍微更正一下。 OK 那这里改成什么改成 item spec ID 然后把这一段代码在它的 API 层里面也同样的给改正一下。


好，就到这里。 OK 其实咱的这个返回值可以做什么样的改动呢？我们可以看，如果你购物车中有这件商品，那咱们把它成功移除之后可以返回一个去。如果这个商品没有找到，咱这个时候可以做一些逻辑判断最终返回 forceok 那么接下来往后看这个 clear cart。那这个方法就非常简单了，我们直接调用 ready separator 调用它的什么方法呢？直接 deleteok 那我们把这个参数给它拼上，用户购物车清空，就这么简单的完成了。


好，那我们走到 controller 里面，在 shopping card 这里，我们先把这个 delete 给它补全，咱把 card controller 的 service 给它添加上去， remove item from cart 好， user ID 和 sq ID 传入进去。然后接下来这里我加一个 to do ，同学们可以在这里添加一个功能，购物车清空功能。 OK 这是一个功能。那通常来讲咱的购物车还有什么其他功能啊？那咱们平时在购物车中还常见另外一个功能叫什么加减号？加减号是什么呢？是添加和减少购物车中的商品数量。 OK 那同学们可以在自己的页面上面添加这么一个功能点，然后把后台的 service 写好。


但是在这里老师给同学们提一个思考，就是说你添加加减号，假设我现在只有一件商品对不对？当我先把这件商品加以，然后再减 1 再减 1 的时候，那它的数量应该等于谁呢？等于 0 对不对？原先有一件加一之后变成两件再减一变成了一件再简易变成了零件。那如果我们前端有这样一个问题，什么问题？它的到达顺序发生了不一致，这个加 1 应该先到达。但是我们因为前端的网络问题导致这个加一请求在后面到达了，那它的这个顺序就变成什么呢？减1，然后再减 1 再加1。那这种情况下它数量是几？我们来算一下，一开始有一件商品，减了 1 之后变成几变成零件，那再减1。这个零件再减1，那还是零件，因为它不能乘负数，对不对？那到这里再加一，那就变成了一件。


好，那问题来了，我这里记一个问题叫什么？如何保证前端请求按顺序执行？也就是说咱前端的请求是以触发的顺序来执行，而不是怎么样？ L 不是以网络请求到达的顺序。那即使你这个加 1 比第二个请求晚了一秒钟到达。但是由于你在前端是先触发的，那所以在后端执行的时候，我依然可以把你这个顺序给它正过来。


这个是一个蛮常见的case ，那同学们可以自己发挥想象力去想一下怎么来实现，或者尝试去网上寻找一些答案。那这也是锻炼同学们去搜索问题、解决问题的一个方式。 OK 那咱这里 controller 就先说到这，我们接下来去移植 resources 文件夹。那 resources 这里也非常简单，我已经把 item web 当中的 resources 全部给他原封不动的 copy 过来了。那我们这里要改这样几个地方，大家应该都非常熟悉了。第一个 application 的名称，我们把它改成 food card service 那接下来往下走这里的 my baddest 的路径，我也把它改成 card 虽然咱还没有泡酒，不过我们先放在这 one 1 哪一天有了对不对好， IM the server port 现在排排坐，你分到老四了10004。


OK 那咱的 Redis 我暂时改成我本地的版本，那同学们到时候记得把它这个 host 改成你的集群。好，那做好这些改造之后，咱的这个购物车模块就算宣告已经完成改造了，那这里同学们可以把它启动起来，去调一些方法测试一下。那这一节瑞本章节，我们走了一下客串去做了一些服务的拆分。那接下来在分章节，我们就要把所有的微服务改成基于接口的调用。那下一章我们学习的这个分组件，从使用的角度来说，真的可以说是 20 分钟上手，非常非常的简单。但是从底层实现，我们可以去花点功夫研究一下它的源码，看一看它是如何通过一个接口可以去解析出这个服务的地址，进而发起远程服务的调用的。


那等到同学们学完分章节以后，凭借有瑞卡、瑞本和份这三个章节，基本上就可以说是打下了 spring cloud 的半壁江山。我们靠着这三板斧，就可以去迅速搭建一套低配版的 spring cloud 微服架构的应用。我说的没错吧，微服务架构就是这么简单。好同学们，那这一节就到这里结束了，我们下一节课程再见。



