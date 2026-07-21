---
title: 3-3 软件安全-数据库安全
---

# 3-3 软件安全-数据库安全

架起需求到落地的桥梁，构建 it 新蓝图。我是张飞扬，上一章节我们聊了聊操作系统的安全，看了看如何实现杀毒。那这个章节我们来说一说数据库安全。好，要说到数据库安全，首先会想到 Oausp 的十大恶人之手， CQ 注入好，

[image](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/76a1c683-d5f9-4d61-961b-7b30ab8993ff/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663ZKCX2D3%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T231041Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIBWD58pIgB3IYjt7bJOEYYJzYUNh3nsmnC9EUebY3N%2F8AiAZ9n%2BEcHrjGNwIUPSf%2F5c5e0H9nHU794Rsm0EbIbYG5iqIBAjG%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMlKxdWXJWWlwww6FQKtwDKn3AxzDQz2FAqLiqeLycBnCq%2BwIaYX%2BCrTaZi9iIxpnYDJRQnjjIzILgGSG9ySFLuwHhXh2wvkRBrfSD74OqGqijsvI5uzyKccdkM8vVtJ%2BhgUbDpVLsxvGI1jp0cDxEIye%2BzKmNDnYT3KkG%2FaIEx4TOkGzhiZ4KOMTnH1nSlyAVA6YrWhuz3XBwV7TagT3yQLok%2Fxbu3UvGKsLA6f25YEQb7WwaTXWGx9%2BHWTZbjN855zwvxsg%2BGJYn%2FmGfz526IF3j%2BDPlF3a3F%2BZkNKZgT5aYZjebEqGPoibVkA0dQRYl2mdMyhdWD%2Fqxz7rGbvkgW5jOC5Cj1UWrqXaam%2F9KuXpvFrKDkhCbNKK1A%2B%2FeZtVp0R4Uont2NKLLU47lb51Mo1HLFLl5uxBNnUdHkfoK5nv0ic%2BXLQXDWoBe%2BfUzmFp7GMtBhM%2BBFcVJj64HGFOzix8e79GkOqTfCd%2FU2zLp3GeNWAXcg6HX2Alg8vyZNp2szBM5%2F7d5hEtZ1MDmIyGErGmzF51FlSTH%2FzVHAO2%2BGuF1hEz777Tk6DoJn%2B3nGFhG6YfZncspnyQQr5h%2BsaBGHs4IJHWZKN0LIWkr1cb9CVAbOx1NvoQn%2FEVv8J9TA2WX3TsBlkxactvUoREwtbj%2F0gY6pgFGkNi4Aexv7Ws2L6MGiV16GphMvNU6ZBL9yg64Djwx6dIk%2BjpqWGfVZMTFzcpmEtLMyCacms%2B3aarkPc5Df3b0fc3j%2Fv3EDjgds%2FMS6U9RGowHry2V4BQvXfVzJ6PwhZnHjYIi35zwx37iFRzRGihKhuCVdVrM7PaGwf3XFezuQq5tttTTjWF7KUYm1kiHXSDN0kfEp0ik%2FVBROqy%2FNzJhN%2FQiSf%2FR&X-Amz-Signature=36dc70546342cd7ac9bc7e2bf94762c7ad86b87ad8349dc3eb1ddb3980def68f&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

这里阜阳老师要给一个免责声明。本章节所说内容仅限白客技术，不能用于黑客技术，否则一切与飞扬老师无关。那什么是黑客？什么是白客？要再强调一下，所有没有经过官方授权的行为都是黑客行为，比如你对生产系统开发测试系统尝试 CQ 注入，一旦你开始尝试没有拿到 CXXO 的允许，那你就是黑客了。好，濮阳老师再告诉大家一次，千万不要用这套路来走黑客攻击，因为什么大部分我们的数据库系统，我们的应用系统都会被这套玩法给玩崩刀？好，我们来看一看，这倒是，什么玩法这么夸张，这么厉害？ CQ 注入第一招，联合注入之前其实我们在瓦佛应用防火墙已经聊到过，通过一些 and 跟all，对吧？通过一些什么 1 = 11 = 2 这种方法可以揣测我们数据库的内部行为，但这只是第一步，还有什么？还有很多第二步、第三步，比如通过一些 order by 进行一些什么数据库的内部的侦测等等。


但是真正的注入行为通常有这样几个特征，一是联合注入，所谓联合注入，这里是这个URL，然后问号 ID 等于-1，在后台我们会变成什么？select，对吧？ ID 什么等于-1，也就是意味着我们 ID 是不存在的，也就意味着这条记录什么是没有内容的，没有返回的，但是我们通过 union select 导致什么这条内容会跟一个什么，一个另外的记录进行叠加，那这个记录重点就是要展现一下我当前整个调用所针对的数据库的数据库的名称，这样的结果是什么？这样结果很容易把我们当前所操作的数据库的名称完完整整的在界面上展现出来，一旦展现出来就证明什么？证明你的数据库设计应用设计的 CQ 防注入很糟糕，这时候黑客可以了解你的数据库，了解那表，了解你的用户，甚至用户的密码。


通过同样一个套路， union select 可以完全公摊你的数据库，这是 c 库注入最常见的第一招，联合注入。一旦联合注入不成功，黑客就会想一些其他的变种。比如我上面的 UIL 简写了，直接从问号开始， ID 等于一，然后给个单引号，单引号在我们什么 seed select 里面，通常就是一个字段结束的标志，当这个字段结束以后加上一个and，然后再加上一个判断的这个内容，这个判断内容会有一个布尔值的返回。


通过这样一个执行，然后去调整我们什么大于一、大于2、大于3、大于4，反复在URL，我们在界面里面去跟我们的后台应用进行沟通，看看它的返回值，当出现返回值变化的时候，那我们就会大致揣测出来整个数据库的名称，它的长度是多少。用同样的方法，我们可以揣测出数据库的每一个字，第一位是什么？第二位是什么？最后把整个数据库名称给揣测出来，然后表名称、用户密码，最后完全公摊数据库啊。


这是第二种常用的我们的注入方法，那第三种常用注入方法就是时间注入，一旦我们的整个应用对联合注入和布尔注入有很强的防御，那我们就会尝试在整个过程当中加一些slip，那这个 sleep 怎么样被触发呢？是这样被触发的，首先是个 select 语句，碰到单引号结束，然后它会后面的一条执行语句进行 and 那这个执行语句里面干什么事啊？又做了一个判断，如果你的数据库的名的长度大于一，我就停 5 秒钟，否则我就直接返回一个一。那通过这种方式我们可以发现在某些情况下也许会触发一个延迟几秒钟，那这个延迟几秒是不是就导致我们什么 see sleep 触发了？原因肯定是我们的正则表达式匹配成功了，也就通过这种方法我们可以间接的揣测出一个数据库的名称的长度。


那我们把 Lens 换成什么？换成字符操作，我们就能揣测出数据库名称的每一个字节的内容。同样道理，表结构，我们的用户信息、我们的密码信息都能够通过什么？我们在图形化界面里采用时间注入依次揣测出来，最终完全掌控你的整个数据库的所有结构，然后进行内容的偷取，这就是 CQ 注入的强大之处。


除了以上三种注入手段，还有比如像报错注入、堆叠注入、二次注入等等其他的变种攻击手段，本质上它是尝试绕过应用层去获取后台的数据信息，怎样防止它呢？当然是采用应用防火墙 Wolf 来进行我们的 CQ 注入的防御。 wolf 的防御方法很简单，防御union，select，防御 sleep 等等关键词通过对什么关键词的匹配就可以基本上精准防御 CQ 注入。但是很不幸，



道高一尺魔高一丈，我们的什么黑客可不会就此为止，

[image](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/93e45246-355c-4a10-b446-caf5297c6394/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663ZKCX2D3%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T231041Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIBWD58pIgB3IYjt7bJOEYYJzYUNh3nsmnC9EUebY3N%2F8AiAZ9n%2BEcHrjGNwIUPSf%2F5c5e0H9nHU794Rsm0EbIbYG5iqIBAjG%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMlKxdWXJWWlwww6FQKtwDKn3AxzDQz2FAqLiqeLycBnCq%2BwIaYX%2BCrTaZi9iIxpnYDJRQnjjIzILgGSG9ySFLuwHhXh2wvkRBrfSD74OqGqijsvI5uzyKccdkM8vVtJ%2BhgUbDpVLsxvGI1jp0cDxEIye%2BzKmNDnYT3KkG%2FaIEx4TOkGzhiZ4KOMTnH1nSlyAVA6YrWhuz3XBwV7TagT3yQLok%2Fxbu3UvGKsLA6f25YEQb7WwaTXWGx9%2BHWTZbjN855zwvxsg%2BGJYn%2FmGfz526IF3j%2BDPlF3a3F%2BZkNKZgT5aYZjebEqGPoibVkA0dQRYl2mdMyhdWD%2Fqxz7rGbvkgW5jOC5Cj1UWrqXaam%2F9KuXpvFrKDkhCbNKK1A%2B%2FeZtVp0R4Uont2NKLLU47lb51Mo1HLFLl5uxBNnUdHkfoK5nv0ic%2BXLQXDWoBe%2BfUzmFp7GMtBhM%2BBFcVJj64HGFOzix8e79GkOqTfCd%2FU2zLp3GeNWAXcg6HX2Alg8vyZNp2szBM5%2F7d5hEtZ1MDmIyGErGmzF51FlSTH%2FzVHAO2%2BGuF1hEz777Tk6DoJn%2B3nGFhG6YfZncspnyQQr5h%2BsaBGHs4IJHWZKN0LIWkr1cb9CVAbOx1NvoQn%2FEVv8J9TA2WX3TsBlkxactvUoREwtbj%2F0gY6pgFGkNi4Aexv7Ws2L6MGiV16GphMvNU6ZBL9yg64Djwx6dIk%2BjpqWGfVZMTFzcpmEtLMyCacms%2B3aarkPc5Df3b0fc3j%2Fv3EDjgds%2FMS6U9RGowHry2V4BQvXfVzJ6PwhZnHjYIi35zwx37iFRzRGihKhuCVdVrM7PaGwf3XFezuQq5tttTTjWF7KUYm1kiHXSDN0kfEp0ik%2FVBROqy%2FNzJhN%2FQiSf%2FR&X-Amz-Signature=e69c8ba9ee229c1a455ccfd6f44b947a736ec0cc30f7a1695f701b9397400d54&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

就此止步哦。他们有什么套路啊？嗯，好几种不同的变种套路来实现最终的 CQ 注入，常见的比如像大小写变换，因为我们什么，我们的 CQ 语句的关键词其实是不区分大小写的，所以我们在什么？我们在用户的界面端 URL 上面会尝试用一些大小写的特殊变换，从而绕过 WAF 的匹配功能，最终实现 c q 注入。


还有什么套路啊？有些 WAF 是进行叫字节删除，比如说我看到 and 我就把 and 删掉，我看到 union select，我就把 union select 删掉。一旦碰到此类瓦夫，我们黑客会这样做，我们在什么？我们 URL 里面不写个 and 写什么ANANDD？叫双写的内容，一旦发给我们的应用程序，我们应用程序一看，其中好像蕴含了一个蓝颜色的字and，对吧？我就把这三个字符给删掉。


相关以后，最后骑士留下来什么红颜色字组织起来还是a，n， d AND 仍然什么？对 c q 来说还是存在这个and，然后依然是联合注入，依然是可以实现什么布尔注入完全仍然可以实现 c q 柱的所有套路，所以这是一种破坏 WAF 的套路。


除此以外还有什么？还有编码来捣乱，我们有中文编码、欧式编码、美式编码、阿斯克编码等等。比如说空格，我们阿斯克玛里面的什么百分和 20 经常会用这个方式在 URL 里面来代替空格。我们甚至于可以把空格先用阿斯克玛变换，用中文编码变换，再用欧式编码变换，再用英文编码变换，变得面目全非。


这种方式仍然在后台应用的解析过程当中会有编码转换，层层转换，转完以后依然会转成最终的空格，那一样的道理，我们的and，我们的sleep，还有我们的 union select 也可以通过变码来捣乱，最终实现逃过挖福的监测，最终破坏我们的整个的什么后台数据的结构。


好，聊完了这个魔膏一丈，那到底对于这些魔头我们应该如何来处理呢？ CQ 注入有一套整体防御策略，我们来跟大家分享一下。

[image](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/e255d7c2-7da9-4381-b641-98dab0f5d0f8/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663ZKCX2D3%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T231041Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIBWD58pIgB3IYjt7bJOEYYJzYUNh3nsmnC9EUebY3N%2F8AiAZ9n%2BEcHrjGNwIUPSf%2F5c5e0H9nHU794Rsm0EbIbYG5iqIBAjG%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMlKxdWXJWWlwww6FQKtwDKn3AxzDQz2FAqLiqeLycBnCq%2BwIaYX%2BCrTaZi9iIxpnYDJRQnjjIzILgGSG9ySFLuwHhXh2wvkRBrfSD74OqGqijsvI5uzyKccdkM8vVtJ%2BhgUbDpVLsxvGI1jp0cDxEIye%2BzKmNDnYT3KkG%2FaIEx4TOkGzhiZ4KOMTnH1nSlyAVA6YrWhuz3XBwV7TagT3yQLok%2Fxbu3UvGKsLA6f25YEQb7WwaTXWGx9%2BHWTZbjN855zwvxsg%2BGJYn%2FmGfz526IF3j%2BDPlF3a3F%2BZkNKZgT5aYZjebEqGPoibVkA0dQRYl2mdMyhdWD%2Fqxz7rGbvkgW5jOC5Cj1UWrqXaam%2F9KuXpvFrKDkhCbNKK1A%2B%2FeZtVp0R4Uont2NKLLU47lb51Mo1HLFLl5uxBNnUdHkfoK5nv0ic%2BXLQXDWoBe%2BfUzmFp7GMtBhM%2BBFcVJj64HGFOzix8e79GkOqTfCd%2FU2zLp3GeNWAXcg6HX2Alg8vyZNp2szBM5%2F7d5hEtZ1MDmIyGErGmzF51FlSTH%2FzVHAO2%2BGuF1hEz777Tk6DoJn%2B3nGFhG6YfZncspnyQQr5h%2BsaBGHs4IJHWZKN0LIWkr1cb9CVAbOx1NvoQn%2FEVv8J9TA2WX3TsBlkxactvUoREwtbj%2F0gY6pgFGkNi4Aexv7Ws2L6MGiV16GphMvNU6ZBL9yg64Djwx6dIk%2BjpqWGfVZMTFzcpmEtLMyCacms%2B3aarkPc5Df3b0fc3j%2Fv3EDjgds%2FMS6U9RGowHry2V4BQvXfVzJ6PwhZnHjYIi35zwx37iFRzRGihKhuCVdVrM7PaGwf3XFezuQq5tttTTjWF7KUYm1kiHXSDN0kfEp0ik%2FVBROqy%2FNzJhN%2FQiSf%2FR&X-Amz-Signature=32e18a3893559bf0c6b844a93676aa99ff3315700d4000d59919d7a583d12d13&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

第一条策略就是过滤危险字，包括像 union sleep 这些字叫冯林末路，碰到这些字符不要去删除字符，而把整条 CQ 语句给停止掉，然后实现报警，因为他们很可能存在安全隐患。另外，不管是大小写还是一些特殊的编码处理，我们都应该能够让我们的过滤器能够增强，能够应对什么编码处理的转换，以及很多的大小写的字符的调整好。


除此以外还有一个很关键的点，就是我们要通过一些预编译语句，不要让所有的 CQ 语句是什么由用户输入，而应该由什么由我们后台准备。怎么准备传统的数据库，比如像Oracle、 DB two 都支持存储过程，所有那些复杂查询都是会在什么存储过程里面预编译完成？我们的 GDBC 也提供了一样的功能， prepare statement 就是实现预编译的一套解决方案。


如何来触发预编译呢？我们只要选用参数化查询就可以了，对吧？我们的很多的 o r 买品工具，像 Hive net my Betas 都支持参数化查询，它会把什么所有参数对应的这些 SQL 实现预编译、预准备，所以也可以有效的防止什么 CQ 注入。


最后，如果你实在是防不住 CQ 注入，我们还可以用一套标准的安全套路。什么呀？防不住就减少损失。怎么减少呢？我把所有的 CQ 语句和应用程序的级别降低。我尽量去减少用户，减少应用，减少 CQ 的这个权限，使得权限降低以后可以有效的防止什么我被你暴露或者我被你篡改的数据的范围。当你是低权限用户的时候，你是没法改什么高级表的，没法改那种系统表的，通过这样的方式依然可以保护我的数据，我既然不能防御，我就什么减少被破坏的风险和被破坏的范围，这也是 CQ 注入的一种防御思路。


好，聊完了， CQ 的注入是不是只有这种套路来进行数据库的攻防准备呢？当然不是，我们还有更多的数据库攻防手段要跟大家交流。其中一项叫什么推理供给，

[image](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/6a3580c0-0761-428b-981e-f117da5b2f7a/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663ZKCX2D3%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T231041Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIBWD58pIgB3IYjt7bJOEYYJzYUNh3nsmnC9EUebY3N%2F8AiAZ9n%2BEcHrjGNwIUPSf%2F5c5e0H9nHU794Rsm0EbIbYG5iqIBAjG%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMlKxdWXJWWlwww6FQKtwDKn3AxzDQz2FAqLiqeLycBnCq%2BwIaYX%2BCrTaZi9iIxpnYDJRQnjjIzILgGSG9ySFLuwHhXh2wvkRBrfSD74OqGqijsvI5uzyKccdkM8vVtJ%2BhgUbDpVLsxvGI1jp0cDxEIye%2BzKmNDnYT3KkG%2FaIEx4TOkGzhiZ4KOMTnH1nSlyAVA6YrWhuz3XBwV7TagT3yQLok%2Fxbu3UvGKsLA6f25YEQb7WwaTXWGx9%2BHWTZbjN855zwvxsg%2BGJYn%2FmGfz526IF3j%2BDPlF3a3F%2BZkNKZgT5aYZjebEqGPoibVkA0dQRYl2mdMyhdWD%2Fqxz7rGbvkgW5jOC5Cj1UWrqXaam%2F9KuXpvFrKDkhCbNKK1A%2B%2FeZtVp0R4Uont2NKLLU47lb51Mo1HLFLl5uxBNnUdHkfoK5nv0ic%2BXLQXDWoBe%2BfUzmFp7GMtBhM%2BBFcVJj64HGFOzix8e79GkOqTfCd%2FU2zLp3GeNWAXcg6HX2Alg8vyZNp2szBM5%2F7d5hEtZ1MDmIyGErGmzF51FlSTH%2FzVHAO2%2BGuF1hEz777Tk6DoJn%2B3nGFhG6YfZncspnyQQr5h%2BsaBGHs4IJHWZKN0LIWkr1cb9CVAbOx1NvoQn%2FEVv8J9TA2WX3TsBlkxactvUoREwtbj%2F0gY6pgFGkNi4Aexv7Ws2L6MGiV16GphMvNU6ZBL9yg64Djwx6dIk%2BjpqWGfVZMTFzcpmEtLMyCacms%2B3aarkPc5Df3b0fc3j%2Fv3EDjgds%2FMS6U9RGowHry2V4BQvXfVzJ6PwhZnHjYIi35zwx37iFRzRGihKhuCVdVrM7PaGwf3XFezuQq5tttTTjWF7KUYm1kiHXSDN0kfEp0ik%2FVBROqy%2FNzJhN%2FQiSf%2FR&X-Amz-Signature=ad0d6d96630ba21ff09dfffe35efc48043b8dd568768971f9b5d8d1622ed00a7&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

如果我能了解用户库的行为，也能了解订单库的行为，我可以揣测一下，也许有一个用户订单历史这样的库或者表，它的大致行为是什么？这种推理攻击其实防不胜防，那怎么样防御？它有些不同的手段，我们以军方，美国军方为例，美国军方的航母库它是怎样来防御的呢？它会有个叫欺骗实力，当军方的官员去查航母的时候，能看到夏威夷出动了一辆航母。


他去哪？他去中东了，准备发起一场战争，但是当黑客去查这条记录的时候，他能查到有一艘货轮从什么夏威夷出发了，他去哪里呢？他去了洛杉矶，准备干嘛？准备进行一次货物的交易。当你从雷达上确实看到有一个大型船只移动的时候，然后你去对黑客所查到的数据库货轮出发。很好，完全符合情况，但实际情况航母已经准备就绪，准备开始一场大型战争喽。


这就是防御推理工具的一种手段，让不同的用户那返回不同的数据实例。那除此以外还有一些隔离和分隔的手段，比如把数据库分成一个区，通过一些不同的这个 CQ 查询，能够返回不同的内容的这个范围来进行单元的移植。令或同样一条 CQ 语句，每次查询的时候反馈的结果会不一样，在之间加入一些盐，加入一些噪声，加入一些扰动来防止推理攻击。


除了这种经典推理攻击以外，我们还有一种攻击叫聚合攻击，那聚合攻击就是聚合好几个信息源，比如说数据库，我们能拿到一些大概信息，交易信息。然后我还是一个企业的，可能是一些什么风控系统，在那边我也从风控系统里拿到这个企业信息，然后我再从这个企业的一些广告系统，他怎么跟谷歌，怎么跟百度沟通的那边拿到一些信息，然后我把多个信息聚合出来，揣测出整个企业后台数据库的长相和它的数据流的情况，怎么样防止这些攻击呢？比较好的方法就是我在数据库的后台也进行很多的分区，我不同的分区只会暴露什么不同时间、不同场景下的数据。


另外我对不同的用户采取不同的仕途，这样最后的聚合攻击也许能攻破你的一个分区，也许能攻破你的一个仕途，但是不能攻破你所有的数据，整个数据库依然能够保持完整。好，这是防止推理和聚合，那除了这些基本攻击以外，还有一些野蛮的攻击方法， d DOS 拒绝服务攻击，大量的压力过来压碳的数据库，怎么样防止这种情况呢？当然是什么增加节点，我们通过数据库的扩容，通过数据库的集群化能够防止还有数据流控，我们可以在应用层做流控，也可以加一些什么缓存。


在缓存里面我们可以再加一些，比如像布隆过滤器等等方法来防止什么数据的击穿，那通过这种防御我们减少真正达到数据库的流量，同时增强我们数据库本身的吞吐量，来防止对数据库进行核心的打压性的拒绝服务攻击。好，聊完了，数据库的攻防，基本上我们大家已经对什么 CQ 注入的防御，对推理、聚合和拒绝服务的防御有了一定的了解。那下一个章节我们就来聊一聊 Web 应用的攻击和防御。大家敬请期待。

