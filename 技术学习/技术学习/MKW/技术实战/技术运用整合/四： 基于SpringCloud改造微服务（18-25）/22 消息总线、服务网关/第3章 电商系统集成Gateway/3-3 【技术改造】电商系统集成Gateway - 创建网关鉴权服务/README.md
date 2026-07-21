---
title: 3-3 【技术改造】电商系统集成Gateway - 创建网关鉴权服务
---

# 3-3 【技术改造】电商系统集成Gateway - 创建网关鉴权服务

[image](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/e3756401-2d10-4a2d-ab7c-5ffe86fb49cf/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466U2VE3JGQ%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T225747Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCAVTbSuM7nsjpy8tKPBseW1eBx35kDjhF2dXkEkfwwjwIhAKLo7iY2%2FgmLPhjeMAMPHzaWqtl4pXOEt59PFlUAL3lPKogECMb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgyKtfVEmcPOALW5%2FN4q3APoHPMxQNfOmM3YO1d4RyoHJ%2B6xseKJrRsvVpO0ndrUDMYU6ZarUy2vZR5y5RlJnMLCtGKjr0fHyD2AlpAZzhD8NNNe5%2BwCsZrT8A2eqCIEHi6F4ojCGANanVzO6QJ3aIsk%2Bj2V1uOqiDeE0yYZp1M1XoOyxAEzvQrWOZLj9Z2vY27G7QnL701LRBu48Jtea7OXlvtUm7CeoH%2BpoaZpA4uC2axt8nNWotFzhnAl47O8M9VSXpcjwmmpYo3mSaCsctPGM8BYIuEVoaPcE7avIBJyMAk7%2FdC85w61rsdDpXfcSORs8faShVbepqWDVnuo5nmhDTUd1cpdrhpFBkAn1tTndyA7unskqSJTac2qPyTHnaJxQvd8kA0a8WS4jqnFt8%2FR4kOXuKLqPiuCETBfaxLRCnUcu4PUKVfhcepjFVvG4WfmnOzbX%2FkKnHkNIybQK9DU70erXcj7IPy5YmWRwJ8d6SrdfSTBI%2Fa7H08jFU7kP5S%2FXPBVuZfWP8mWg7Q089B8cKfAdm5UazffwnNgeod4usA254lPlcZXXb1nkz4jKpf8QvNeeBBCjyCu5Ak182KxcKtUh%2FGJj5NfXvJ5TkVBmkE0IDD%2BSYoQwNx5UMod0EmPcRbm%2Bnsv0GzgATCpu%2F%2FSBjqkAWoCZrT%2FqtJrGy4Q3e%2Fw%2BDrOKWWbW1A%2Fnjv39XjL3vjjA4%2BHK3M8z2DCPAjcLlCV7GGKLAa8ITt6ZXv%2B2bN2jSaF8M61SwponQAly1ZGv8CqYOk7uNVkLIR%2B43SCo23FzFusHMl28TYZKdbyksect4FbBQFV86Ph12FF6qLX5kijdxd7GxZXx%2FloaX3KPUnrlxkN%2BdnDfMvdEgcmc%2F2T3VvAsIQq&X-Amz-Signature=60681bf07b0962d788ee9767786c12e30e2b6ec977b496cfcd9a8576ba2146d5&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

[image](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/65084993-0920-45d3-98c3-6cf922a5e00f/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466U2VE3JGQ%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T225747Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCAVTbSuM7nsjpy8tKPBseW1eBx35kDjhF2dXkEkfwwjwIhAKLo7iY2%2FgmLPhjeMAMPHzaWqtl4pXOEt59PFlUAL3lPKogECMb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgyKtfVEmcPOALW5%2FN4q3APoHPMxQNfOmM3YO1d4RyoHJ%2B6xseKJrRsvVpO0ndrUDMYU6ZarUy2vZR5y5RlJnMLCtGKjr0fHyD2AlpAZzhD8NNNe5%2BwCsZrT8A2eqCIEHi6F4ojCGANanVzO6QJ3aIsk%2Bj2V1uOqiDeE0yYZp1M1XoOyxAEzvQrWOZLj9Z2vY27G7QnL701LRBu48Jtea7OXlvtUm7CeoH%2BpoaZpA4uC2axt8nNWotFzhnAl47O8M9VSXpcjwmmpYo3mSaCsctPGM8BYIuEVoaPcE7avIBJyMAk7%2FdC85w61rsdDpXfcSORs8faShVbepqWDVnuo5nmhDTUd1cpdrhpFBkAn1tTndyA7unskqSJTac2qPyTHnaJxQvd8kA0a8WS4jqnFt8%2FR4kOXuKLqPiuCETBfaxLRCnUcu4PUKVfhcepjFVvG4WfmnOzbX%2FkKnHkNIybQK9DU70erXcj7IPy5YmWRwJ8d6SrdfSTBI%2Fa7H08jFU7kP5S%2FXPBVuZfWP8mWg7Q089B8cKfAdm5UazffwnNgeod4usA254lPlcZXXb1nkz4jKpf8QvNeeBBCjyCu5Ak182KxcKtUh%2FGJj5NfXvJ5TkVBmkE0IDD%2BSYoQwNx5UMod0EmPcRbm%2Bnsv0GzgATCpu%2F%2FSBjqkAWoCZrT%2FqtJrGy4Q3e%2Fw%2BDrOKWWbW1A%2Fnjv39XjL3vjjA4%2BHK3M8z2DCPAjcLlCV7GGKLAa8ITt6ZXv%2B2bN2jSaF8M61SwponQAly1ZGv8CqYOk7uNVkLIR%2B43SCo23FzFusHMl28TYZKdbyksect4FbBQFV86Ph12FF6qLX5kijdxd7GxZXx%2FloaX3KPUnrlxkN%2BdnDfMvdEgcmc%2F2T3VvAsIQq&X-Amz-Signature=f9bd968c26c68762be5e9d20d7f868314329155a75a3b72bb9f688d01fed37a0&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

hello 慕课网的各位同学们，大家好，我是姚半仙，那咱这一节继续做网关层的改造，咱该改造到哪了？用户的鉴权模块对不对？咱前面已经通过随堂的小 demo 给大家去示范了，如何使用 jwt 来生成一个 token 然后做 token 的校验。那在网关这里的集成和前面的课程比较相似，所以我这里就不一步一步带大家来做了，我们把前面在课程 demo 当中做的网关层给它移植过来，然后在上面做一些必要的改造就可以了。


好，那我这里带同学们去回顾一下，咱的鉴权服务这里有两个模块，分别是 of API 还有 of service 那在 API 这里它的 pom 文件和前面的 demo 是一模一样的。这里引入了 spring boot starter 还有 spring cloud starter 的 open phone 接口。那在 Java 类里面，有一个小的变化，我们来看它的 pose 这里三个 pose 还是老三样，它的代码都没有变。然后这个 of service 那它这里我给它要添加一个新的方法叫什么呢？同学们想一想，咱前面有生成 token 校验 token 还有 refresh token 那还缺一个什么？还缺一个登出，在你去 logout 的时候，我怎么样呢？我要把你的当前的这个 token 给它删除掉，对不对？叫 delete 好，我们给它就起名叫 delete 那它接口的参数咱就把它 copy 过来。好，那它是一个什么类型呢？是一个 delete 类型，所以我们给它这里起一个注解叫 delete mapping 好，它的路径也把它叫做 delete 好，这就是咱的 fap I 这一层里所有的变化了。


好，我们接下来往下看，那下一个模块是 off service 那相应的它这里要做一个什么变化呢？没错，自然是把咱前面加的这个 delete 接口给它实现掉。我这里选择实现 delete 接口。那咱在删除一个 token 之前，我是不是要先校验一下你这个 token 是不是正确的？比如说你张三拿到了李四的 token 那你也能删吗？不可以。


所以我们这里需要先调用一个什么方法呢？先调用它的 verify 来去看一下，你接下来要删除了这个 token 是不是一个合法的 token 好，我们这里拿到 token 然后只要稍加判断什么呢？你的当前的 token 我 get code 那是不是和咱的这个 success 的 code 相等？好，我这里要判断一下，如果相等。那 OK 我们接下来就可以做删除操作。那如果不相等怎么办呢？那你这里就要返回一个错误。好，我们把这个方法给它补全。好，这是一个 response 那这里就直接给它 new 出来了，就不用 build 方式了，因为咱这个返回对象非常简单。那我这里如果成功了，给它 set 一个 code 那 code 的值就是success。 Ok. 反之不成功，那自然的就要给它的值设置成失败。失败是什么来着叫 user not fund 好，就你了。 Ok. 然后再把这个值 return 回去。那这就好了吗？好像还缺少点什么，对不对？那咱这里不能打空腔我们要在这里做点什么东西，把它从 Redis 当中也给它删除掉。那我们这首先要删除的是你的 refresh token 我把它找到。好从 Redis 当中删除你的 account 当中所待夹杂的这个 refresh token 除此以外，我还要再删除一个谁我们往上看，咱在登录的时候还设置了一个 user token 加 user ID 这样一种形式，我们这里也要把它也给删除掉。在这 user token 加 user ID 那这个 user ID 我们同样的从 account 当中把它给拿到。 OK 那这里这个类就写完了。


那最后一步，我们要在 resources 里面把它的这些端口都给它更正过来。那咱新的奥斯服务，我给他指定的这个端口号是幺零零零六一万零六号。 OK 那到这里，咱的这两个鉴权有关的微服务模块就很快的创建好了，那这里我们就要去把它集成到 git way 当中。不过在集成之前，我这里要提醒同学们一个业界约定俗成的一些用法啊。啊比方说这里，我们打开 auth API 这个接口，我们看一下这个服务想看到有一个叫 verify 那 verify 是什么呢？同学们应该非常清楚，他是去校验你这个 token 是不是正确的。那目前来说，咱的这个 verify 放到了哪里呢？它是放到了我们 auth 微服务当中。
那么如果每一个请求过来，你的网关层是不是都要发送一个 HTTP 调用来去访问 auth 服务的 verify 接口呢？那么这不光在无形当中，增加了你的网关层负担，同时也延长了你接口返回的 rt response timeok 那目前来说，业界通常用的做法是什么呢？我们业界是使用客户端验证 token 的方式，比如说怎么样呢？我们这个 off 服务只负责生成 token 在这里只负责生成 token 那校验 token 是在哪里呢？那就是在各自的网关层和服务端来校验 token 把这个 verify 下放到网关层或者是你的服务层来进行校验。


那这里有一个什么样的要求呢？我们看这个要求是在 gwt service 当中，我们打开这里来看一下。我这里加了一些注释，同学们看这个 token 这个 token 服务是根据你的用户 ID 再加上一些额外信息，最终生成一个 gwt token 我们看一下咱这里的加密方式，咱这里是使用的什么呢？ hmac 256 它是由一个密钥加上一个散列函数来做加密的，它的密钥只有这一个 K 所以在真正的生产环境中，我们通常不能使用这种方式。


那通常在正式的生产环境当中，我们采用哪种方式呢？包括老师现在的公司也都是采用这样一种非对称密钥加密的方式，那他就需要一对密钥对来进行加密，我们可以点进去看一下。那这个 auth zero 项目它提供的算法包里面其实有很多业界非常流行的方法，那比方说你看这个RSA ，那我们这里有可以使用 public key a private kid RC 算法，我们这里可以直接搜索一下。那如果大家使用这种算法或者是其他的也需要一对公钥密钥，对的算法，那情况就变得非常简单了。


对不对？我们可以用一个 key 在咱的这个 auth 服务当中做加密生成 gwt token 让咱的网关层或者是服务层使用自己手里的那个 K 来校验你的 gwt token 看是不是有一对 K 来生成的。这样的话有几个显而易见的优点。比方说第一个，它首先符合我们业界对 authentication 服务的一个约定速成的规范，并且在我们的这个服务体系当中，它节约了一次 HTTP call 否则我们在网关层都要发起一个服务调用来验证你的 token 这样的话无形之中大约增加了每个服务怎么样呢？大概 10 到 20 毫秒的处理时间。 OK 那感兴趣的同学可以试着把上面的场景给它实现一下。把咱服务的 token 校验这一步，就是这个 verify 怎么样，把它下放到你的微服务或者是你的网关层当中，这算是留给同学们的一个小练手作业了。那我们这里是从教学目的出发，所以就使用了简单的 token 生成方式。因此你要是需要校验 token 的话，那必须要发送一个 HDD B call 到咱的 auth service 当中去校验你的 token 是不是正确的？那我这里，把这个注释放到一个更加显眼的地方，就放到 auth application 这里。好提醒同学们去自己动手去尝试做一下改造。那我们的这两个 auth 模块已经创建完了，接下来我们转战到 platform 下面的这个网关层 gateway 里面来做一些改造。好像下课时间到了，那同学我们这堂课就先上到这里了，下一小节我们再回来做网关层的改造。 OK 同学们，我们下一小节再见。


