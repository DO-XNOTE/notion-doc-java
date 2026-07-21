---
title: 3-11 实现用户登录
---

# 3-11 实现用户登录

[image](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/d388e3bc-62be-4255-8596-877c861a20dd/SCR-20240816-tthc.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466S7V7GNNB%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T224630Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCa3CDC7gjoJ%2F4jgZHQWYyLrL4vm2OIWKDKFDu0BjCPgwIgRPVzInXu9XbEA6kW44MhxdyUwhxpuyv0PXjp1EE%2FbOAqiAQIxv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDK6xbtWOvnMIkxP5wircA9OYb826fSszef2G7prdLyUQx7rm6UEHNPWO9d%2BB9r92ynGZ8622u9%2BxLgWawcPN09rJ%2BBYV4gLgUAqyPfwtz15IXSYRJURwo2uEiztDo3VzRWydShhuXBJ%2BxNILhJUd2s5JDyaZJv2Y73amTYU5NpF%2Bd4%2BObN25%2FLx0lNvFxzL9P7%2FdBXrpEeBru5nwUqSB%2BoSCffmIgSZbs0htA%2F%2BQ%2FfUxgo%2Fh%2BZJAaSFepJ%2BbE263zX9Y5vUeJI%2FkhQDyHtFPLnYRTe54%2FXkcd%2F3zxCVCMJ5kGGbL%2BG5dm5RQQyILKgLKG9dcuRtrR2ULZwqFTjBygpviYLDroDxO3ZqPz0PO0geIBEtgo37hx0TbG1Dg2d55ZFiBInjywIvQWmaqJToLO61o0PPSD0Z%2FClfb7p%2BsRJVef86UlQW0Z8QHCnXot37J2N3gU2x4Njj1hwRZY5519JoHSnye8REbA6s2kr9Az8D5XNQjTGD78Hl9AY31Wc0sH8bLYazFYLABR9BuoAmlEr6ksIXw8urwtsBhLK4Q7%2F8TmrbEjtlGNlszKNnCSzn0OIrTsunvDV9Bb%2Bb02WIGPonZIOHn8lLDR5%2B%2BPosJwBmF8vdpTUxdgpIjfYdn6IdoEi%2FUFukaevwchT6NMMW3%2F9IGOqUBavEmuyg7uZ8%2FS4qVrzJC%2FNS789pzwvF4qZ36wDoX2bHh%2Fk1vxbGXNMZI6RgZrmo8kHn6FUesz72vg0DRHDxOxu34uRlsRNJsExX5WXc7bpAgxFcW2UFglSilSX2JYjxs%2FmfOf0lwxkTrlkWNNCJXzQfFKizJAlHcyljwiJGSyhFY%2FnF4a5y20La2fS9cD%2BvB3ZdCIuFMCHwPd%2FhRPCc%2FLpZmx9qH&X-Amz-Signature=e0f5503a5b9b79343a5ce0726459ef845aa1f6fe77c3a6b9df4151e6826cc58b&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

前几节我们把注册做完，并且联调完毕，接下来我们就要去做一下登录了。登录其实相对来说比较简单，其实就是在前端输入了内容了以后，点击会把用户名和密码传递到后端去做一个检索。如果你叫用户存在就登录成功，不存在相应的你就无法进行登录。OK，好，我们回到后端去编写一下相应的代码。我们还是一样。我们是从 service 再向 Ctrl 的这层去写。我们先打开service，可以找到 user service 以及是它的实现类。首先我们先把它的抽象方法先去写一下，我们就可以取一个名字。


public users query user for login。

在登录的时候去进行一个请求检索，传入两个参数，第一个是 user name，第二个是一个password。好，不要忘记把注释加一下。这也是规范，也是为了更好的在后续去进行一些维护。就是检索用户名和密码是否匹配，用于登录。可能会有同学会问，我们在进行注册和进行登录的时候，都会有 user 进行返回，但是现在我们还没有用到，对吧？没有关系，我们在后面是会用到的。用到的时候我们再来说一下。我们再到它的实现类，很明显在实现类里面我们是需要去进行实现的，你们可以按一下 command 加i，快速的进行导入。不要忘记由于它是一个查询查询，我们把这个事物给加上，使用 supports 就可以了。在这个地方我们也是一样，我们会参考之前的一个方式，我们使用 example 来进行一个检索，直接拷贝一下。


拷贝过来以后，我们首先第一个满足的条件是 user name 是否是要匹配，匹配好了以后它还会有第二个条件。所以你在后面可以再去加上一个 and equal to，这个是可以去写多个的，相当于是在写 SQL 脚本 where 条件语句后方可以and，可以多个条件多个判断。


我们再把 password 传过来，相应的我们要到油热子里面去把 passport 要贴过来。一定要注意写的内容是和我们的 Todo 类里面的属性对应的，而不是和我们的一个数据库所对应。因为数据库里面的字段拿过来以后，它有可能会变为驼峰式命名，所以在这边一定要注意好，这样子我们的这两个条件就已经是好了。随后我们就可以去做一个查询了。通过 users map。


Then select one by example.

直接把 user example 给拷贝进来，很明显它会返回一个 user 对象，它返回的是一个t，这个 t 就是我们在这边所设置的 user class。OK，加一下users，取个名字叫做result。等于这个查询完以后直接 return 出去就可以了。好，我们这个时候应该要去实现一下咱们的 Ctrl 了。找到 passport Ctrl 了。在这个里面我们可以去写一下相应的方法。我们拷贝一下。为了方便直接拷贝注册的方法。贴过来了以后，在这个部位我们是需要去修改的。很明显应该是用户登录修改一下它的一个 master 的请求方式。使用 post 在这里，我们就需要改为 love in。


好，OK，我们在这里所有写的路由大家务必要和老师的一模一样，因为路由我们在这边其实都是要统一要一致的。前端源码已经是写好了，前端源码所要去调用的，所有的接口都是跟着我们路由地址来的。如果你写的是一个，不是login，是一个 user login，可能接口就调用不了了。这一点是需要去注意的。


对于前端传过来也是一样，会传过来一个 user Bo 进去看一下，但是这个时候我们 user Bo 传过来了以后， user name 和 password 是必须要传过来的，但是登录它没有确认密码，所以在后方有一个 request 对吧？把它改为了force，我们并不是必填项。OK，好，下一个。在这里面会有相应的内容。

confirm password 我们是不需要的，在这边我们要进行一个判断，判断很明显 you name 和 password 不能为空。在这边如果为空了，相应的我们要提示一个错误，用户名或密码不能为空。在这边要查询用户名是否存在是没有必要了，拿掉这个判断也没有没必要的，可以全部都删掉。


好，到这里我们就可以直接去实现登录了。实现登录通过 user service，我们来一个 query user for loving user name 直接传过来，下一个把 passport 传过来，这样子其实我们就可以进行我们 service 的一个调用。随后我们可以拿到一个user，这是一个 user result，再把返回到的 user 其实可以放到我们的前端。


在这里 password 是需要去注意的，我们在这边拿到的是一个明文，明文和我们数据库是无法做到一个匹配的，因为数据库里面我们之前也说了，这个东西密码是加过密的，所以相应的我们在这个地方也要去做一个加密。加完密了以后，我们才可以去调用咱们的 service MD5 utter，点 get MD5 string 把 password 给传进来，这样子就 OK 了，只不过它会有一个异常，这个异常我们可以 track 取一下，或者直接在我们的外边直接 throw 可以 throw 一个CPT。


好，这样子其实就 OK 了。但是其实我们还是需要去注意的，我们查询出来的时候， user 有可能是会为空的，所以我们要在这边我们再应该要去判断一下，如果这个东西指出来是空的，我们就要 return 一个错误，我们要用户名或密码不正确，这种提示信息我们要返回出去的。


OK，现在我们登录的接口其实就做好了，我们可以来重新的进行一个install。 install 好了以后重启服务器。好，重启成功。重启成功以后我们可以来测试一下。我们打开咱们的 swag two 刷新一下，可以看到现在是多了一个接口是login，我们可以来测试一下。在这边会有一个 b o b o confirm pas 索的，我们不用管，可以保持它为空。


password 写一个123123， user name 写一个test，点击发送。我们得到一个200200，就是代表我们请求是成功，并且其实我们还带有了一些相应的数据，这个是要用户的一个信息，但是用户信息里面还有一部分内容，现在像密码还有是一些，后续我们还有真实的姓名，某贝尔 email 等等。其实我们后面会需要去做脱敏的，我们到后面再说。


现在我们暂时先不提接口，是调用是通的对吧？调用通了以后我们来看一下咱们的前端，前端在这个地方刷新一下，来一个test，来一个123，写456，点击登录。你会发现他报了一个错吧，用户名或密码不正确也我们填的内容是不对的。其实相应的信息，我们请求是到达了我们的后端了，再来填一个123123，再点一个登录。好。OK，你会发现我们是登录成功了，其实我们登录的接口就已经是做好了。随后我们可以来到咱们的前端的源码，我们连带着注册登录注册。我们一起来看一下它的一个基本的业务是怎么走的。先打开我们先看 log in 登录，这个是登录的注册是Redis。其实我们在页面里面写的所有的一些 JS 代码全部都是在页面的最底部，写在底部的可以看到在 body 的最下的一个部分。我们来看一下。


这里有一个 do in，这个就是用于做登录。首先是一些针对于我们 form 表单里面元素的一些。基本判断是包裹一个 user Bo，这个 Bo 的字段和我们后面是对应的。这个其实就是一个结层对象，这个结层对象会携带着放到这里，它会有一个 body 放到这里进行提交的。这个是组装的一个URL。请求的地址 post 是通过它的一个请求方式，如果是get，使用点 get 就可以了。在请求完毕以后会有一个stand。这里面是一个回调，使用 i s 这样的一个。这边的一个镜头函数，这个是 e s 6 里面的。这 e s 其实就是一个result。这个 result 我们来看一下。在我们后端其实是定义了一个 m 可杰森result。其实相应的一些信息内容其实都会放在 RS 里面所拿到的。在这边我们就需要去进行一个判断了，判断它的 200 状态是否是 OK 的。 200 就代表是请求承诺吧，会获得一个user，这个就是我们在后端请求到的一个 user 的一个信息。


在这边再会有一个判断，这个判断是判断这个回调是在有一些页面，比方购物车，在购物车页面你没有登录，会让你跳转到当前页面去进行一个登录，登录成功以后再会让你回跳到之前的上一个页面。这个就是用于去做回调的，但是其实我们现在用不到，在这边肯定会为空，所以在这边会进入到 else 这里面会发生页面跳转，进入到ENX，进入到我们的首页。这里就是我们成功的执行的一个基本业务。当然在注册里面其实也是类似，看一下注册在发送的一个请求，其实是和我们的内容其实差不多对吧？请求成功以后，在 RS 里面判断一下 200 状态，如果状态是成功，没有问题，再去拿到 user 这样的一个信息，很显然这边也会有一个 return 这样的回调。OK，没有问题，直接会跳转到我们的 index 点HTML。OK。为了演示一下它的效果，我们在前端打上一个断点，带着大家一起去看一下它的一个拿到的 RS 是个什么东西。我们只需要进入到登录页面，我们按一下F12，调起它的控制台，输入它的一个 test 用户名密码123123，点击登录。这个时候可以发现断点是进来了，看一下。


首先其实在这边其实已经是调用成功了，我们可以把鼠标移过来，可以看到它是一个object，它是一个对象is。其中我们所需要去拿到的内容。在 data 里面看一下。这个 data 有一个 status 200，这是我们自己的。当然它外部也有一个status，这个其实是它自己本身的。我们来看自己定义的就可以了。 status 是200，请求是成功的， message 没有问题是OK。这个 data 其实就是在我们的后端所塞进去的一个data，OK。所以我们可以往下面走。

按 F10 到这里会进行一个判断，很明显 status 是200，判断是200，会进入到这个判断，会拿到 user 这个对象，在这里会进行一个判断。当然回调的 return 为空，所以会进入到这里。直接就会跳转到 index 页面了。按一下F8，这个页面是会直接跳转到首页的。现在其实我们的第一部分的用户注册和登录接口带着大家一起去编写完毕了。我们的页面前后端也都是联调，没有问题，成功了。OK。




