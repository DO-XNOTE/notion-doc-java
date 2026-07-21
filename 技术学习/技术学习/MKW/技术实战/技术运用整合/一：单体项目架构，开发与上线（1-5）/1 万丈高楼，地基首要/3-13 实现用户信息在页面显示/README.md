---
title: 3-13 实现用户信息在页面显示
---

# 3-13 实现用户信息在页面显示

[image](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/612cda74-4f52-4345-babf-8b8f35c8f528/SCR-20240816-ubzh.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UEJX7AJL%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T224631Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDyMICiPQn6ol88dzjb%2FuyKN5TJEdKwd4mZ3E8K9ySSfgIhAPvT8Wk9GPIj%2BWnWXMfvgC4JpzDxL5%2F6q997GAFR2dtqKogECMb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgzuCJ5WZJmgJwxlcwcq3APo7FVuFfRPp1Mk%2BRIhc9NKKOYH924pj3zTnfSVDVYAAQKEog5p%2FrlyzNDYguO2oGW5CzMu58xvwroyX856Hn4NKnb%2F9zim32JH7gRoHdgC5%2FdKmST%2FIJny1RGNnaE6iJwAcfb6xIG3SrjSdeUsJQT2hF6TaUm8%2BulQCCMzKlEbEkBniKzDlRFfyVDzSPZhq5x5%2BVx74E1xMxYxx6XlrP6BK7r0KHGZx%2BshNXsgoBcKJAvfrJXSKH1bCjUNHqBe5MqR7FSXL8AkUpy1jNLF2GGBl9hPOCWN7qKt2rYZH9347dIN1tdYOqc9yeCuIS7Oc2oA8n1HTiGP5eyP9uAYFR5JNu%2BX0ryUNLix8al%2FTyU%2Fv2BzZMDArmDON%2FnrRgL2M3CBC320ZMU63qPBE5hgID06XCxLSMox8zyxGwwXXA3044ckga3CXIp22bkOkInOXQh01VY%2B1oy79ZLszjzLhTyYR1AL8Q8kD2r98dfg%2Fal4VMl0DoVfgJD3XFL1dnZEVlEADCBemx4qZcybY9oXTxAaPvLvHCXZb%2BzpAvytkeD492oS4SclUr%2BSenYWT5bcjRVw6YzQavPm46d2R4Fa1w5lIBoyp79%2BaAEH2nZfOIrqAi5tcZx6dzW5oBZSEzCvt%2F%2FSBjqkAeCAYIIIGgh66ElyDbFSbJ%2FVivw1ttVgOxwuegeSj1oNEJwqinAA5guVLfjnJBqmz7hRRfBG2g6KlD1fTTJgD6fOwjp%2FiE7%2FyhJGlpsJppgWBVNcx1RVM8kBqLQc%2FIqLAZlpAAS2A1LXfCN1o7qJyeWIyzQ3pskbJGoFrCiaLQNaLqb%2B0GUKisFQVP35dQpQGqXowneqDoTRmHbF%2BoJNa9g4ZT92&X-Amz-Signature=137f23835f4eadd956abb2257eb355b6689d019d9bb0ab917a2c7f9be0d784dd&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

[image](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/d3bc7c5a-6e61-4cc4-ba4c-a119b3cace79/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UEJX7AJL%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T224632Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDyMICiPQn6ol88dzjb%2FuyKN5TJEdKwd4mZ3E8K9ySSfgIhAPvT8Wk9GPIj%2BWnWXMfvgC4JpzDxL5%2F6q997GAFR2dtqKogECMb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgzuCJ5WZJmgJwxlcwcq3APo7FVuFfRPp1Mk%2BRIhc9NKKOYH924pj3zTnfSVDVYAAQKEog5p%2FrlyzNDYguO2oGW5CzMu58xvwroyX856Hn4NKnb%2F9zim32JH7gRoHdgC5%2FdKmST%2FIJny1RGNnaE6iJwAcfb6xIG3SrjSdeUsJQT2hF6TaUm8%2BulQCCMzKlEbEkBniKzDlRFfyVDzSPZhq5x5%2BVx74E1xMxYxx6XlrP6BK7r0KHGZx%2BshNXsgoBcKJAvfrJXSKH1bCjUNHqBe5MqR7FSXL8AkUpy1jNLF2GGBl9hPOCWN7qKt2rYZH9347dIN1tdYOqc9yeCuIS7Oc2oA8n1HTiGP5eyP9uAYFR5JNu%2BX0ryUNLix8al%2FTyU%2Fv2BzZMDArmDON%2FnrRgL2M3CBC320ZMU63qPBE5hgID06XCxLSMox8zyxGwwXXA3044ckga3CXIp22bkOkInOXQh01VY%2B1oy79ZLszjzLhTyYR1AL8Q8kD2r98dfg%2Fal4VMl0DoVfgJD3XFL1dnZEVlEADCBemx4qZcybY9oXTxAaPvLvHCXZb%2BzpAvytkeD492oS4SclUr%2BSenYWT5bcjRVw6YzQavPm46d2R4Fa1w5lIBoyp79%2BaAEH2nZfOIrqAi5tcZx6dzW5oBZSEzCvt%2F%2FSBjqkAeCAYIIIGgh66ElyDbFSbJ%2FVivw1ttVgOxwuegeSj1oNEJwqinAA5guVLfjnJBqmz7hRRfBG2g6KlD1fTTJgD6fOwjp%2FiE7%2FyhJGlpsJppgWBVNcx1RVM8kBqLQc%2FIqLAZlpAAS2A1LXfCN1o7qJyeWIyzQ3pskbJGoFrCiaLQNaLqb%2B0GUKisFQVP35dQpQGqXowneqDoTRmHbF%2BoJNa9g4ZT92&X-Amz-Signature=40b2389d3349e4ad6f7be3afae9764681dd305ae9d8a3d446ad92b8b2ce75ff6&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

上一节我们回顾了 cookie 和 session 的一部分内容，这一节我们来看一下如何来实现我们的用户信息，在咱们的页面里面进行一个展示。其实我们上一节也说了 session 在 HTML 里面是获得不了的。我们可以来先看一下京东，京东我目前是一个未登录的状态，如果没有登录，很明显在这个部分会显示一个免费注册和请登录。当然我的订单也是不能够查看的。我们在这里点击登录，随后我可以通过微信去扫码登录，扫一下就登录了。登录了以后很明显来看一下，在我们的头部，我的一个昵称，还有是用户的头像都可以去进行展示。当然其他的信息也都可以去点，我们就来看一下它的这些信息其实是保存到哪里？其实它是放在 cookie 里面的。我们来按一下F12，按了 F12 以后，其实在这里边会有一堆的信息，里面会有一堆的信息，当然是加过密的，我们也不知道具体的是什么内容。假设我们现在在这里，可以右键拉一个clear，这是清除所有的cookie。


好，所有的清除成功，我们再来刷新一下当前的页面。刷新以后你会发现现在这两个链接又重新的展示了。也。其实我们就可以证明，京东的一些用户信息，在你登录了以后，它其实是加密以后放在 cookie 里面的。其实这么做的对于我们来讲，我们也是可以通过这种方式去做的。所以我们就可以不再使用 session 去做。当然 session 很重要，我们会在后面使用 Redis 来实现分布式会话。好回到我们的代码，我们来看一下。


我们先来看登录。在登录以后，我们会拿到一个 user result 这个信息，这个信息我们是直接可以保存到咱们的 cookie 里面去就可以了。只不过会有一个问题，因为 cookie 是保存在浏览器的，也就是客户端，你的电脑有可能是共享的。不管是你在家里还是你在公司或者是在网吧。浏览器里面信息一旦保存了以后，其实可以涉及到用户的信息，一般来说都是比较私密的，所以在这个地方往往我们会去除一部分的信息。


我们来看一下，在 user 这里面，其实像 password 还有是 real name 这些内容我们都不应该进行一个显示吧？所以其实我们在这里可以加一个JS，有一个 ignore 进行一个忽略。我们使用注解了以后，当我们再把这样的一个实体类封装为一个 JSON object 返回到前端了，它是不会显示 password 和 real name 的。它是可以这么去做的。但是在这里会有一个小问题。我们当前的 users 是从数据库逆向生成的一个实体类，它相当于它其实就是一个 d o 类。对于这种原始的类，其实我们不应该或者不介意去进行修改，去进行一些额外代码的增加，我们应该要保留它初始的一个样子。


所以在这里我们会怎么去做？我们在这边我们可以使用 user result 是获得的值，然后我们只需要这样子，它可以点set，比方 set password，直接设置为空就可以了。当然它的信息我们也都可以去设置。 set mobile，然后设置为空。再来一个可以 set 有一个email，虽然我们现在用户的这些信息都还没有，但是修改完以后这个信息是可以取到的。所以在这里我们都要去设置。像注册时间，其实我们也可以去设置为空。好。还有是一个 update 更新时间，我们也设置为好。此外应该还有是一个生日对吧？ set birthday 设置为空。这样的一段代码太冗余了，我们在它的下方再定一个新的方法来 set move， set 空属性，我们只需要把 user result 传进来就可以了，把代码推进来，设置完之后直接 return 一个 user result，这样子就行了。在这一侧，我们只需要去重新的进行一个调用。 user result 等于 set not property 把 user result 传进来。这个时候的 user result 其实就是有些属性设置为空了。


好，设置为空以后，在我们的服务端其实就可以去设置一下咱们的整个用户的信息，把它放到 cookie 里面去的。我们可以在服务端去做。当然在前端去做也是没有问题的。


我们在服务端可以来设置一下要使用cookie。其实在咱们课程里面，我预先也是已经为大家提供了一个封装好的 cookie utils 这样的一个工具类，在这个工具类里面其实会有很多的一些方法，来看一下。有很多像删除，设置，获得等等相应的方法，其实都是在这里面。 cookie 的一个工具类其实也是比较通用的。好，我们来设计一下。使用 cookie 有跳丝，有一个方法叫做点 set cookie，在这里面其实会有很多，来看一下。其中像它前面的两个参数都是 request 和response。所以既然如此，在我们的方法的地方进来的时候，其实我们应该要去为它增加一下 HTTP server it request 以及是 HTTP serve it response，这两个我们都是需要去设置的。当前这一行太长了，我们来换行。这是一个spouse，拿到了以后，在我们的 cookie utils 里面就可以去设置咱们具体的一个 cookie 的值了。我们先可以把 request 以及是 response 写进去，在它的后方其实还有一些额外的参数，比方下一个参数，我们直接点进去看 set cookie，还有中间这个其实是它的key， key 我们设置为 user 就可以了。后方还有是它的值， string 其实就是它具体的值。这两个就是一个键值。对。OK，先来写一下。


写一个user，可以看到它是一个 cookie name，后方是一个 user result，把它给写过来。但是这个 user result 是一个对象。我们可以看一下它的里面的代码，它里面的代码其实看得出来它是一个 cookie value，它是一个字符串类型的。


字符串类型很明显，我们是需要去做一个转换的，在这里既然涉及到转换，但是它又是一个对象，所以我们会使用到 Jason 的工具类去进行转换。 Jason 的工具类在咱们课程里面，其实我也已经是预先提供了，来看一下。在这里有一个杰森有特斯，大家在使用的时候直接拷贝过去就可以了，使用起来相对来说也是比较简单的。在这里我们可以来写一下。写一个杰森，有一个 Jason 与 tells 点。这里面有几个方法，有三个比较简单。第一个是 object to JSON，就是把一个对象转换成一个JSON。下面两个是把 Jason 转换出来，原来是使用 object 形式去转的。现在我们把 Jason 字符串转换成一个list，或者是转换成一个Podro，转换成一个 entity 这样的实体类。在这里我们使用这个就可以了。 object to JSON，随后把 user result 丢进去。现在这样子。


一个最基础的cookie，其实我们就已经是可以设置好了。但是其实它还有一个方法，它后方还可以去加一个参数。这是一个什么参数？我们加上一个true。再来看一下。加了 true 以后可以看得出来，它上面写的是 is in code。你是否要对它进行一个加密？加密一下，在我们的一个前端就不会看到里面具体的值了。这一点是需要去注意的。在源码里面，在这个地方有一个 is in code，随后其实我们还会有一个 set pass，这个 set pass 是什么？我们在上节也说了我们 set pass，其实所有的我们都是设置为斜杠的，可以一步一步去看一下它的源码，往下面走可以看到它有一个 cookie 点。 set pass 我们都是直接设置为斜杠就 OK 了。好，既然在我们的后端设置好 cookie 了，以后我们只需要去测试一下咱们的前端就可以了。好，重新的去运行一下。先 install 一下，因为我们已经是引入了两个工具类，一个是cookie，一个是Jason。好，我们安装成功。随后我们重启一下。好，启动成功。


我们现在回到咱们的页面，我们来登录一下。登录使用 Imock 123123 登录。登录以后这个时候我们可以发现当前在页面里面，我们的顶部显示了欢迎某某某，随后在我们的侧边来看一下，这个头像是不是已经是显示了，我们的 m 可也能够显示了。OK，这个其实就是把信息放到了 cookie 里面，我们也可以通过源码来看一下。源码我们可以打开咱们的首页，这是前端源码index，我们来看一下，在 index 里面，其实应该每一个页面里面都会有相应的一部分内容，它会有一个，先看它的生命周期有一个 create 的。在这里面来看一下。


首先我们可以通过 APP 点 get cookie，这个 APP 是咱们的APP，点JS，它其实就是一个对象。首先去获得一个user，这个 user 可以看到这个就是在我们后端所定义的，在后端我们定义的也叫做user，所以这个值一定要写成user。如果你不写user，写其他的键，对应的在前端的源码，你也是需要去进行修改的。获得到了 user cookie 以后，你就要去进行一个判断，当它不为空的时候，即便是不为空，再对它去进行一个转换。因为我们是使用了一个加密encode，所以在前端是需要去进行一个抵扣的。随后你就拿到了一个 user 的字符串，这个字符串拿到了以后，你还要再一次的进行一个判断，判断不能为空，你就可以拿到了是一个对象了。但是我们要严格一点，我们要判断它是不是一个object。如果是在我们前端，其实就可以赋值了。


首先来设置一下 user is lowing，设置为true，代表我们的用户在前端其实是一个登录的状态。随后我们就可以拿到用户的信息了。用户的信息放到咱们的 user info 里面， user info 以及是 user is logging，其实是在这个里面它会有一个data，这个是 fill 里面做数据绑定的，这就是它的数据。其中就有一个 user is logging 以及是 user info，这两个值在最一开始其实默认的都是没有的，用户是没有登录，用户信息也是没有的。OK，所以在我们的前端目前就已经是实现了。大家在课后也是可以试着去把 cookie utils 去写一下，把相应的信息放进去就可以了。


在这个地方我们所用到的是一个登录，其实在注册也会有，所以我们把这一段内容拷贝一下，放到注册的地方，放到这个位置，相应的我们的 request response，其实我们也应该要写到这个地方。切过来。在这里面会有一个 user result，看一下，它是会返回一个 user 的，所以在它的前方我们可以去定一下users。好，OK。这个时候就在注册的时候，其实也要亏了，我们也来测试一下，重新再运行一下。


好，现在我们是成功的，已经是运行了。我们刷新一下页面以后，我们来看一下，会有一个退出登录点击没有用的，因为我们退出登录功能还没有做。但是为了要重新再去做注册和登录功能，我们只需要这样子，按 F12 把 cookie 里面的内容给清空，直接右键 clear 清除一下就可以了。


清除一下以后，我们再刷新一下页面，点击注册。在这个位置我们可以重新去输一下，比方来一个 a b c 123123，点击注册，随后成功了。来看一下吧。这边我们的 a b、 c 默认的昵称，还有是默认的头像，全部都会有，当然在我们的 cookie 里面也会有。这就是一个加过密的 user 的信息。这一块内容我们就已经是成功的实现了


