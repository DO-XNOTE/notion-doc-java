---
title: 016.运营后台管理员模块（上）
---

# 016.运营后台管理员模块（上）

既然要实现我们对应的一个后台管理的 Web 界面，那自然而然要遵从 spring MVC 设计的一个方法。那我们先来看一下 bundle 结构，我们这边的 Controller 目前来说是对 c 端实现了一个 user 相关的一个用户的Controller。对于 admin 相关的一个Controller，我们有两种选择，第一种选择直接在这个 Controller 的帮助下去添加，第二种选择是我们新建一个 admin 的package。那其实为了之后统一的切面权限的一个管理，然后我们在这边新建一个 admin 的package，然后我们开始实现对应 admin 相关的一些请求功能。


首先 admin 用户需要有登录的操作仍然是一样，我们新建一个 admin 相关的一个Controller，然后我们开始编写对应的这个Controller。 user 相关的 Controller 我们之前已经有用到过，我们来看一下 user 相关的 Controller 并没有加对应的一个前缀，直接是user，那我们假设 admin 相关的一个 Controller 都必须要以对应的杠 admin 这样的方式开头。


那这边的话就有对应的两层 admin 的结构，第一层 admin 代表这是一个 admin 相关的URL，第二层 admin 代表它是一个 admin 相关的操作，也就是管理员相关的一个操作，这个代表管理员模块，这个代表管理员，那接下来我们来开始实现一下对应的一个功能。


首先我们先设置一下，由于是 admin 的后台管理，它就不再是遵从返回 response json 这种样子的一个方式，而是直接返回动态渲染的一个 seam lift template 的view。因此我们假设先实现首页，它返回的是一个 model and view 对应的这样的一个界面的功能。然后我们设置一个 request map。然后这个 request mapping 上来什么都不做，直接返回对应的 model and viewed。然后我们需要指定它返回的 model and view 的一个路径地址，那我们设置为 admin 杠index，我们直接返回 model and view。好，然后我们新建一个 admin 杠index，那我们到对应的 templates 下面新建一个admin。然后这个 admin 的 bundle 仍然一样，代表它是一个运营管理模块相关的一个页面。那接下来我们先在这个层级页面上建一个 index 点 html 占位。然后我们在这个 admin 下面再建一个admin，也就是表明它是一个管理员的一个模块，我们输入 index 点html，设置一个叫运营后台首页，好，启动一下我们对应的应用，看一下效果。


打开浏览器 local host 8010 admin 杠index。我们这边可以看到他目前报了一个错，找不到对应的执行操作路径。那我们需要检查一下我们这边的 request Mapping 没有填写。加一下杠 index 重新启动。


好，刷新一下对应的界面，我们可以看到运营后台首页这几个字就已经出现了。好，那我们先不去实现对应的一个运营后台首页。我们都说过 admin 的运营后台其实就代表了我们对应的一些操作后台管理的一些数据的权限，因此我们对应的 admin 界面必须得是强制 admin 官方登录的。也就是说若 admin 没有一个适合的权限账号登录它内部的所有的功能，包含对应的首页都是不能让它查看的。因此现在需要去实现 admin 的一个登录授权的功能，做一些企业级的应用。


一般来说的话会有一套 admin 账户体系的一个管理，那在这样的一个搜索推荐的项目当中，我们对运营后台的一个设置的要求就相对来说比较低。我们仅仅只需要支持单一账户的一个后台管理功能即可，也就是说我们仅仅只不过支持单一的admin，我们对应的 admin 也没有注册的权限。我们只有一个系统初始化的时候做在我们的配置文件里边的一个 admin 的管理员的一个初始的用户名跟密码，那然后我们就来实现一下，我们进入 application 点property，我们在配置文件当中直接存放官方账号的一个用户名和对应的密码。我们在这边直接写一个admin，官方账号的用户名和密码，然后我们写一个 admin email，我们假设是 admin IMOC . com。


然后我们需要存放一个 admin 的password，这个时候我来命一下名 encrypt password，那大家可以看到我没有直接存放对应的password，而是存放了一个 encrypt password，那这个就好比说我们将用户的一个密码以明文的方式存在数据库，还是以密文的方式存在数据库？效果是一样的，我们要预防开发人员作弊，因此我们直接在这边存放一个密文的数据库，即便我们的开发人员或者运维人员看到了这个密码，也仅仅只不过是一个加密后的密码，作为的用户他是无法感知的。
那这个 encrypt password 我们设置为多少呢？那我们直接将之前 user 对应的一个加密的密码拿出来，这个是 123456 加密后的这个密码，于是我们直接在这边 copy 过来，那这个 admin password 对应的一个明文密码，其实我们知道就是123456。然后回到我们对应的一个 admin Controller，然后我们需要在这个 admin Controller 当中拿到刚才注入在配置文件当中的一个密码以及邮箱。我们直接在这边使用 value 的方式得到对应的一个 application property 当中变量的一个注入。我们直接使用多了服务加大括号的方式， admin 杠email，然后我们 copy 一个encrypt，这个不能打错的话就直接找不到对应的变量了，那我们直接 copy 过来，防止出错。 encrypt password。然后我们在这边修改叫 increase 哈索。然后我们跟 user 相关的一样，我们需要一个 session 去管理对应的一个 admin 已经登录的一个状态，于是我设置一个 public static final string，叫 current 产。
The main session. Current admin session.


好，然后我们需要做两件事情，第一件事情是我们需要一个登录的页面，让其可以登录，那我们直接 copy 一个这个东西出来，把它叫做 login page，然后这个 login page 什么都不干，返回一个 login 即可。也就是说它只需要返回对应的一个登录的页面，然后我们需要第二个真正的登录的接口，那我们在这边直接 copy 一个出来，真正的一个 login 方法，它的 method 就不再是 get 了，它的 method 是一个post，因为一般登录的请求是一个 form 的 post 的操作。它接收两个参数，一个参数是 request param name 等于email，第一个接收的是你登录的一个邮箱，第二个还需要一个登录的密码password。好，这个时候我们开始书写对应的一个代码。首先我们做一次非空的校验，也就是说我们先用 string utils 去判断 is empty，对应的Email，对应的一个 password is empty。如果说两个有任何一个为空，不好意思抛错。


business error 这个我们已经很熟练了。我们设置一个 parameter validation error，然后抛出一个用户名密码，不能为空不通好。由于我们使用的是 MD 5 的一个加密方式，那因此我们直接在这边还是要使用对应的 user service 内部的之前实现的一个 MD 5 的一个 encode 方法，把它给 copy 过来，我们去做一次比较。


怎么比较 Email 点equals？如果说它和当前我们这边注入在配置文件当中的 email 相同，并且 end encoded by m d 5 传过来的这个 password 和对应的我们配置文件中的 encrypt password 相同，那这个状态其实就是一个登录成功的状态。在这边将异常抛出去，也就是一个登录成功，否则的话不好意思登录失败。我们直接使用 parameter validation error，叫用户名密码错误。好，就通过这种样子的一个方式，若登录成功的时候，我们在这边其实是需要一个重定向到首页的一个操作，然后我们用一个小tricky，我们这边不返回 model and view，直接返回一个string。使用 spring MV seed 一个 red direct admin index，通过这样的一个方法就将其重定向到了 index 对应的一个登录界面。


那在重定向之前，我们要做一个什么样的事情呢？我们需要将用户的一个 session 填上去，让我们跟之前用户操作一样，我们 auto wild 注入一个 HTP survey request。那这个 HTDP Server late request 是用来做对应的一个 session 存储用的，若在登录成功的情况下，我们直接使用对应的一个 get session set 一个attribute，然后将对应的一个 current admin session 将对应的 email 放入其中，代表其已经登录了即可。好，那这个 login 请求我们其实就算做完了，那接下来我们要将对应的这个 login 点 h 天猫页面给它建出来。

