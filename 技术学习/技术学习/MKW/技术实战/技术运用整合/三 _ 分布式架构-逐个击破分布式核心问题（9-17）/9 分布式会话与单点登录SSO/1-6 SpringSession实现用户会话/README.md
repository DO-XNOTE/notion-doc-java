---
title: 1-6 SpringSession实现用户会话
---

# 1-6 SpringSession实现用户会话

[image](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/e77b0805-70fe-4232-8cec-0b2f8bfbfe1e/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TJKC3JJ7%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T225107Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIDnzsX%2FlB%2BFwkYwtC03i7M%2FwDwH7mlF9FwGlcAUXAZDSAiA8fsVCJwhudReNvORCwGR%2FzEo18KNYNXStqSa72wkCNSqIBAjG%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMuwev504HQKIH8gkmKtwDdbig6ums7ogaFXwt41RmxexLDT0NVsMGcz8FmZxZiPYq7jIeNEHEs4juqLiXMl2A%2BiNexoGfRZzL%2FxVOtGYZTiBftWDDkgKeEyZGiKhn2flT3jGa%2FGoiBTkia8i7GGj8KodlBTWxcEZOzRJqGtWfa4wigZWQTQ7jNgzVfAOdKQb%2FboVuX54tOlgfffwwZDIHOOKILM9TKCbnyTXHfGdISViuB%2Ba4LxSMZA1hENzJJ%2FyGE%2FhIFRqc6zpgeNrDUAQQYjA%2B4fUZOx6d2bpPJhfp8PbBw70%2Bsa2Mm3eTzMfWM%2BC5%2BocTLjdZCmVNi7GLU98dmrUW1tAW0zNeXYdHxYGhIyIfgZXrb%2FoqBENnu93gCc%2BUwxDUfF0HFsDFYrq0o8Bq9aWq7KcVA6f1cniebIg0H0S9ojAIvuS2aAjBEX0T%2BFAQxkg48TINSMyeOQqu7cO5hea%2BL3G1%2BUKeP3%2Bz5lk8hb05ShISG12QTBCnqWst6X8qdzoR%2FhxisiqF3%2BRZqMlr%2FOaSkX0C9PLeSe2cSYDn8CzQxCb8ZFfgU%2BjXdBz8vwRcx4gJ4vqfypem0lla%2F3lmKxJfjv%2BiIk6d8mvdECSzuRAHySRh2nolwMF52O0XxZWY8%2BY6Qy743uKXjDgwmbf%2F0gY6pgFVdBXr5qMoF5i4SdNg%2FmeTXsa37zLMLXFXOvNNrgYvuNb8GcaBmLL4bBeWudV48RA55avIHNSu4E1RJYfH4ZBhosP6Uu00WvZoDUlGbze%2BOlDlKfjB8XPMbXMiba80334cRpeJ06EUlaDN6AFYOC0oYDWZFxkx6qPP%2BmjASDpCO9wKM%2F3cP0GKQ04O1pTPyAtx9HHj8MR%2B4CHqaDxsH48raQ9QKch6&X-Amz-Signature=41673c025d3f8f8026d1caf1b94be7a1472c0ef69d1975f975b9170bdc1b40cd&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

[image](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/ad62b0d8-37c5-4f51-86bd-e3f09b842966/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TJKC3JJ7%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T225107Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIDnzsX%2FlB%2BFwkYwtC03i7M%2FwDwH7mlF9FwGlcAUXAZDSAiA8fsVCJwhudReNvORCwGR%2FzEo18KNYNXStqSa72wkCNSqIBAjG%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMuwev504HQKIH8gkmKtwDdbig6ums7ogaFXwt41RmxexLDT0NVsMGcz8FmZxZiPYq7jIeNEHEs4juqLiXMl2A%2BiNexoGfRZzL%2FxVOtGYZTiBftWDDkgKeEyZGiKhn2flT3jGa%2FGoiBTkia8i7GGj8KodlBTWxcEZOzRJqGtWfa4wigZWQTQ7jNgzVfAOdKQb%2FboVuX54tOlgfffwwZDIHOOKILM9TKCbnyTXHfGdISViuB%2Ba4LxSMZA1hENzJJ%2FyGE%2FhIFRqc6zpgeNrDUAQQYjA%2B4fUZOx6d2bpPJhfp8PbBw70%2Bsa2Mm3eTzMfWM%2BC5%2BocTLjdZCmVNi7GLU98dmrUW1tAW0zNeXYdHxYGhIyIfgZXrb%2FoqBENnu93gCc%2BUwxDUfF0HFsDFYrq0o8Bq9aWq7KcVA6f1cniebIg0H0S9ojAIvuS2aAjBEX0T%2BFAQxkg48TINSMyeOQqu7cO5hea%2BL3G1%2BUKeP3%2Bz5lk8hb05ShISG12QTBCnqWst6X8qdzoR%2FhxisiqF3%2BRZqMlr%2FOaSkX0C9PLeSe2cSYDn8CzQxCb8ZFfgU%2BjXdBz8vwRcx4gJ4vqfypem0lla%2F3lmKxJfjv%2BiIk6d8mvdECSzuRAHySRh2nolwMF52O0XxZWY8%2BY6Qy743uKXjDgwmbf%2F0gY6pgFVdBXr5qMoF5i4SdNg%2FmeTXsa37zLMLXFXOvNNrgYvuNb8GcaBmLL4bBeWudV48RA55avIHNSu4E1RJYfH4ZBhosP6Uu00WvZoDUlGbze%2BOlDlKfjB8XPMbXMiba80334cRpeJ06EUlaDN6AFYOC0oYDWZFxkx6qPP%2BmjASDpCO9wKM%2F3cP0GKQ04O1pTPyAtx9HHj8MR%2B4CHqaDxsH48raQ9QKch6&X-Amz-Signature=5fedb33ea1c7a20048393bd6c86b24442b6272995c866161738a00f03151bba3&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

那么前面几节课我们是通过 Redis 来实现了对针对用户的一个绘画的管理，那么这个其实就是用户的一个分布式绘画。除了我们单个单独去使用 Redis 的话，那么其实我们也可以借助 spring 来提供的一个 session 去进行一个绘画的管理，那么在 spring 里面其实它称之为叫做 spring session，我们是可以通过它来也可以去实现用户绘画的一个共享，用户绘画的一个分布式的一个目的。


那么如何去使用？那么很明显我们是需要去引入相应的包了，那么在这里我们来找一下，找到这个Redis，在 Redis 的这个上方，我们在这边我们可以去引入一个对应的一个依赖，这个我就直接给贴过来就行了，然后把这个 import change 给导入一下。需要注意就是说你在进行下载的时候，如果说你不是国内的镜像的话，那么它是会到国外去下载的，会比较慢，所以我也是推荐使用阿里云的一个美本的镜像就可以了。然后在这里我们去加上一个对应的注释，这个是引入 spring session，依赖。

好。OK。随后我们就可以去做一个install，把它给进行一个安装，等到它安装好了以后，我们再去做一个启动。好，点击运行，启动一下咱们的服务器，来看一下会不会报什么错。那么这个时候报了一个错来看一下，这边提示说，就是说有一个 class not found，就说我们有一个类找不到，那么这个类是什么呢？在这里叫做 remember me service，那么这是记住我这样的一个service，其实这个类的话，它是存在于 spring framework 点security，也就是说它是存在于 spring 的一个安全框架里面的，叫做 spring security。


那么这个其实是在一个新版本的 spring port 中所需要去依赖的一个价包，你是需要去把它给导入进来的，那么这一块内容我们也是需要把它们提前的放到这个部分，也就是这个 spring boot start security，你要把它给依赖进来。然后我也在这里加上一个注释，引入 spring 安全框架，随后 import change 给导入进来。那么这样子导入进来以后，我们再来做一个install。好，然后我们再来做一个运行，看一下这个时候会不会报错。


好，OK，这个时候没有报任何的错，说明其实我们这个包依赖现在是 OK 的，没有任何问题。那么随后我们就可以去做一个相应的配置了。对于咱们的一个 spring session 来讲的话，我们呢先打开一下，找到这个application，点 y m l 这个配置文件，在这里面我们是需要去做一个配置的。那么找到spring，在这个里面它其实会有一个内容，然后你可以来一个 option 斜杠，或者说是 or 斜杠来看一下它。


其中会有一个 spring 来看一下，搜一下，有一个叫做 spring session，在这里有一个叫做 store-type，那么这是什么意思？这个其实就是 spring session，它所存储的一个类型，或者说的它所存储的一个位置，那么在这里的话，其实有 Redis jdbc，MongoDB 这些都是绘画所保存的一个介质，你是可以去设置的。那么在这里很明显我们就使用 Redis 就可以了。


OK，双击一下Redis，那么这样子的话，咱们的一个 spring session 它的配置就已经是 OK 了。随后我们还是需要去做一个开启，开启咱们的一个 h t p session，使用 Redis 这个的话，在咱们的这个启动类里面，在这个 application 我们呢启动一下叫做enable，有一个 h t t p，在这里有一个叫做 Redis h t t p session。从这个字面意思上我们就能够看出来，它是用于去开启Redis，这个也就是基于 Redis 的一个 h t p session。OK，那么加一个注释，开启使用 Redis 作为spring。筛选好 OK 开启了以后，那么接下来我们就可以去使用了。那么如何去使用？那么使用的时候直接这个是我们之前在单体部分所使用的一个方法，你要去使用的话，那么直接就是使用 h t p server it request，这里面直接通过 request 点 get session 就可以获得到一个 session 的，这个其实就是 spring session，然后也是一样，在这里面我们是设置了一些对应的数据，像 user info 等等的一些内容，你都可以去操作去设置取值的。那么在这边的话，我们现在是可以去先去启动一下，因为我们修改了一些类，先重新的去启动，然后启动完了以后的话，我们可以先来看一下咱们的 r d m。


打开，我们先来刷新一下，那么目前其实当我们启动了以后，你会发现在这里面其实它默认的已经是帮我们给设置了一些相关的内容，那么这些其实都是 spring session 版，这是由 spring 容器来帮我们做的一个操作，我们并没有自己去做，是由他来帮我们去做的对应的操作。


OK，好，随后我们来看一下，那么这个时候我们就需要来访问一下对应的一个方法。打开一下，那么这是一个 locahost 冒号 8088 杠login，那么这个时候它会提示说请输入一个用户名和密码。这个主要是因为当我们在使用 SspringSession 的时候，你是强制的是需要去使用这个它的用户名和密码去进行一个登录的。


OK，它**默认的用户名叫做user，然后还会有一个password，那么这个 password 在哪里？在咱们的控制台，在这个地方就说使用这个安全的密码去进行登录，也就是这一行字符串，把它拷贝一下**，然后你贴到这个里面来点击登录，那么这个时候你就能够登录进去。这个 setsession 其实就可以被我们给设置进去的。OK，然后我们打开rdm 来进行一个刷新，然后我们到这个里面来看一下，咱们的一个session，在这里面找到往下面找，然后随后在这个地方那么这个其实就是咱们的一个手动设置的一个内容。


在这边有一个叫做 session h build 冒号 user info，那么这个 user info 其实就是咱们所设置的一个key，内容其实就是这个 new user，这个就是在我们代码块里面，在咱们的代码里面所设置的这个 new user OK。然后需要注意，就是说咱们的这个 spring session 在进行一个相应的操作的设置的时候，其实它本身它使用的是一个 hash 这个类型，那么注意一下这里面所有的 key 其实都是一个一个的failed，OK，那么这是一个它外部的一个完整的一个key，你也可以通过 Redis client 在命令行里面去敲一下，可以去看一下这里面相关的数据，其实它的数据其实也是比较多，看上去也是比较的复杂的。OK，好OK。那么这个就是它的一个 news user。

随后我们再来看一个问题，那么现在我刷新页面是没有任何的问题，因为我当前用户其实刚刚做了一个登录，如果说我现在把这个 cookie clear 清掉，刷新一下，它又会让我们再去做一个登录，那么其实在有些情况下这种其实并不是很好。我们不想要这样的一个登录，可不可以？也可以，我们是可以去除的，因为这个是 spring query 安全框架的一个安全机制。


那么如何去除呢？那么我们打开这个 application 启动类，在这里面找到这个 spring boot application。那么我们在之前讲单体部分，其实我们有提到过一个自动装配的一个过程，在 spring boot 池中的时候，会有一部分的内容类会自动的被我们的容器给加载，这个其实就是一个自动装配的一个过程。当我们在使用了 spring security，也就是安全框架的时候，那么它其实本身也会有相应的一个自动装配。

自动配置的一个类有一个class，我们只需要把它给排除就可以去使用了。那么怎么去做？其实在这里面你可以点进去看，在这里面会有一个叫做exclude，这个其实就是干嘛，就是排除的意思来看一下，就是说你可以去具体的去定义一个自动装配的一个类，当我们去配置了以后，那么他们。


Such that they will never be applied.

也就是说他们一旦被使用了，在这里边被配置了，那么他们就不会被自动装备了，那么这样子其实也就是排除在外了。那么在这里面我们只需要去加一下，把这个 exclude 学过来。随后在这里面其实有一个叫做security，搜一下在这里叫做 security or to configuration，那么这个其实就是权限的自动装配，把它给拆过来点class。好，OK，那么这样子其实就 OK 了。然后呢，我们再来做一个重启，重启服务器，然后在这里的话，我把这个 session 给把这个 cookie 中的这个 session 给去掉。好，启动成功了。成功以后你会发现在这个控制台里面没有刚刚的一个密码了，对吧？好，然后我们在页面里面，这个时候我来做一个刷新，应该说这样子 set session 直接敲一下，然后你会发现这样的一个登录的界面，它没有显示，也就是直接跳过了。

那么这样子其实我们当前的一个设置，也就是 security 自动装配的一个类，我们其实是成功的排除在外了。那么这样子就是不管我们每一次去访问哪一个用户，去访问就不会跳出那个登录框了，那么这样子就比较好了。OK，那么如此一来的话，其实我们在这一节就已经是把 spring session 整合到我们的一个项目里面来了。那么如果说就是说你想去使用这个我们前面几刻使用的一个 Redis 去做用户的绘画是可以的，那么如果说你想要使用这种基于 spring session，其实也就是这个 h t p server it request，通过这个获得了一个session，其实也是可以，因为这个其实它就是一个 supersession 的，它包含了一些相应的会话机制，它是由 spring 来帮我们进行的一个管理。那么你是可以这样子去做的。


可能有同学会问，在平时的使用过程中使用哪种比较好？那么其实在这里我会建议使用我们之前面几节课所使用的一个Redis，那么是可以的，这种方式也可以。但是使用 spring session 以后，那么其实它的一个耦合度会比较高，它是会和咱们的一个 Spring 耦合在一起。**就说你不可以单独的脱离，直接去使用Redis**，因为在这个 Redis 里面，其实你也能够看得出来，这里面相应的一个数据结构是比较的复杂的。那么假设现在我们在进行一个团队开发的时候，某一个产品它可能它不仅仅只是由 Java 开发的。如果说是由 Java 开发，我们完全可以去使用 spring 里面的 SpringSession，但是如果说现在还有一个其他的模块，可能是由 PHP 或者说是由 GO 语言去做开发的，那么这个时候想他想要去通过我们的一个 Redis 要去获得 SpringSesion的话，那么可能就会比较的麻烦，可能会稍微的复杂一些了。所以如果说我们在使用前面几节课的一种方式的话，对于其他的一些语言来讲的话，他们再去调用 Redis 里面的一些值的话，存取就会来的更加的方便一些。

OK，所以这两种方式的话，其实都是可以的。不管你是使用 Redis 单独去实现用户的会话，还是使用 SpringSesion  这两者都是可以的。根据自己的一个实际情况，采取不同的一个策略都是没有任何问题的。OK？

[image](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/cca36c46-34fa-48c6-8c8e-34f3ad184e7c/2020-09-17_180050.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TJKC3JJ7%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T225107Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIDnzsX%2FlB%2BFwkYwtC03i7M%2FwDwH7mlF9FwGlcAUXAZDSAiA8fsVCJwhudReNvORCwGR%2FzEo18KNYNXStqSa72wkCNSqIBAjG%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMuwev504HQKIH8gkmKtwDdbig6ums7ogaFXwt41RmxexLDT0NVsMGcz8FmZxZiPYq7jIeNEHEs4juqLiXMl2A%2BiNexoGfRZzL%2FxVOtGYZTiBftWDDkgKeEyZGiKhn2flT3jGa%2FGoiBTkia8i7GGj8KodlBTWxcEZOzRJqGtWfa4wigZWQTQ7jNgzVfAOdKQb%2FboVuX54tOlgfffwwZDIHOOKILM9TKCbnyTXHfGdISViuB%2Ba4LxSMZA1hENzJJ%2FyGE%2FhIFRqc6zpgeNrDUAQQYjA%2B4fUZOx6d2bpPJhfp8PbBw70%2Bsa2Mm3eTzMfWM%2BC5%2BocTLjdZCmVNi7GLU98dmrUW1tAW0zNeXYdHxYGhIyIfgZXrb%2FoqBENnu93gCc%2BUwxDUfF0HFsDFYrq0o8Bq9aWq7KcVA6f1cniebIg0H0S9ojAIvuS2aAjBEX0T%2BFAQxkg48TINSMyeOQqu7cO5hea%2BL3G1%2BUKeP3%2Bz5lk8hb05ShISG12QTBCnqWst6X8qdzoR%2FhxisiqF3%2BRZqMlr%2FOaSkX0C9PLeSe2cSYDn8CzQxCb8ZFfgU%2BjXdBz8vwRcx4gJ4vqfypem0lla%2F3lmKxJfjv%2BiIk6d8mvdECSzuRAHySRh2nolwMF52O0XxZWY8%2BY6Qy743uKXjDgwmbf%2F0gY6pgFVdBXr5qMoF5i4SdNg%2FmeTXsa37zLMLXFXOvNNrgYvuNb8GcaBmLL4bBeWudV48RA55avIHNSu4E1RJYfH4ZBhosP6Uu00WvZoDUlGbze%2BOlDlKfjB8XPMbXMiba80334cRpeJ06EUlaDN6AFYOC0oYDWZFxkx6qPP%2BmjASDpCO9wKM%2F3cP0GKQ04O1pTPyAtx9HHj8MR%2B4CHqaDxsH48raQ9QKch6&X-Amz-Signature=c44930ed8e4e21b9cc7c69a6590893de060f7efbac0cf82a080ca72354f58953&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

以下是根据文本内容生成的提纲：

