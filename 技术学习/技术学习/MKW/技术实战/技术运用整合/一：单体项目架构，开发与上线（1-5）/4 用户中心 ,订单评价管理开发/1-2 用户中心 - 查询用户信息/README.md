---
title: 1-2 用户中心 - 查询用户信息
---

# 1-2 用户中心 - 查询用户信息

[image](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/30b6c8b0-eba3-4e4c-96d4-adf19813280e/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YNCAULRP%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T224722Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDWGFktsqpxzILMFYwOh4nzMT50zsOdsPoonmtqfgnPtwIhAIEADO3SokO9YBw2%2BLuK%2B9I5E3Ttog4mwtSb%2BFdEQ94qKogECMb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1Igzcy%2F7TgL%2BIj10azYsq3AM5PSM8WhxQq5Q6S54fEPrpPpRUOAXk7z7ZPHySyJ8AIfgfgSK0jcS%2FbbhD%2BdAMxuQAi%2FFzU8TipT2T%2FcAJ1HfnzXyrD932hq2oAPhLgRVS7KOjXBA9IZ1MpITaFEZwW3ODhxIO8r24Jf%2FiMmThEnqMN%2BbBGCQVAfDTR12GdCikAoZJCWTLCI83SUhMqHxk8vSrAZcXqVhpusP91Z4UI23myRMNqOYgRKSz6vTBJHlzQChei3Uc4gGiVl9QJ16dOCBa%2F%2FOYbm6v1r4df0uRV%2BMv36MUMmVx%2BerV1aWOHoyIeMpGejNavovnXRvCdIFWQf6mj3eCNy9WfhjUMSfSqPAv8y2zDirNzB%2BjpRC2FZjhNe1FLIbinIwbklQwr4I%2BeVZj0UqW%2F6y0zP2lWV0J4mnWAIOS%2FjgAsZsu7Qovzyo%2BMAMUZMFelhkc0CQL2MsB72ln5orrnTHZ8jwlW6mekfAgxZhYY03SMlu7YL0Cnkr%2FGUYLULvOgG1BJvrs6Hf6JhO%2BFLkv9q8e6nMw19a%2FC67V6j4LDBiYHsKINrX8eQURev5Y94XFlr0f1TBIiH8ZwSrRngkPMT%2FoDJgQhGQqZAMjHnGzeiYUxgIZowQ1kOlPF8xUDXUkUAXPxSAf%2BzDCt%2F%2FSBjqkAdAonkK%2BomPX18zz6vUek39DXZzJdpQhtJUkdNJwnsJvm4pthkUDG2NPSOV4mDDatmw3im3DtrExpGi6P1m6rz%2BEU67xPtWeijWOCSxt3vClhxzqhSjiRNF%2BDSSuLqgJ5tDZ0Cn1PmGDi5ZQ9OwNH%2FIhiG2DKKtyfYwoePj6jrLvkpUsFPrSYUZehgt2%2B7C%2FuopC43RDQGpRbBBfrPo8FzlAj11y&X-Amz-Signature=ba64c9a73b9dee71b4cb05097662b300bf90d5748c24e746216ab349a34d6593&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

接下来我们就可以一起来开发在用户中心里所涉及到的一些相应的接口。首先第一个我们来看一下在我的信息里面，我的信息进入到这个页面的时候，其实我们应该要把现有的用户信息进行一个展示，展示了以后再去做修改。所以肯定我们会涉及到一个查询用户信息的接口，所以我们可以先把这样的一个接口先来一起写一下。我们先打开开发工具，在开发工具里面我们先看一下我们之前所涉及到的所有的一些 controller 了，其实都是写在了 Com 点 m 点 Ctrl 了之下，这些我们都可以把它们当做是针对于门户的一些接口。现在我们所需要去做的是用户中心和门户，其实我们可以把它们理解成是两个不同的业务，或者是两个不同的服务模块，所以我们在这里我们尽量的要把它们去做一个分层。所以我们在它的后方我们再去创建一个package，取个名字就叫做 center。


接下来我们在用户中心里面所需要去开发的一些接口，我们都会放在这个包的下方，放到这个包里面去就可以了。如果你要放到 Ctrl 里面，虽然也可以，但是会有一种比较混乱的情况，因为不同的业务，你把不同的一些 Ctrl 都放在一起了，这样子会搞混。如果后续业务多了起来， Ctrl 了越来越多，这一层它会显得会比较杂乱，所以我们尽量的要把它们分开来。而且在前期分开来的好处是为了我们以后会做微服的时候去做好准备，因为你要去做微服务的时候，我是要根据业务去拆分的，所以要去拆的时候，你只要把这两个啃出来，直接拿出来就可以了，会更加的方便。OK。所以在这个地方我们来创建一个 Ctrl 了，来取一个名字，就叫做 center control 了，OK。这是我们的一个 control 了。 center control 了，其实就是针对于我们的首页在整个中心贯穿中心的一个 control 了。对于我们的一个用户信息来讲，其实用户信息也是贯穿于我们整个用户中心的，所以我们就直接可以把获取用户信息接口放到当前 center Ctrl 里面去，而不是我再去创建一个新的用户， Ctrl 了，OK，好。在这里面我们就可以去写一下了。


先写一个API，这是 10 万个处，我们接口肯定也是要去写好的，因为后端其实对应的也是要提供给前端人员去做一些对接工作的。 OK center 用户中心，加一个tags，用户中心展示的相关接口好，OK。首先我们就要来写我们的第一个接口，这样子我们也是一样，我们是从下往上去写，所以我们虽然是有了一个 control 了，我们先不是立即去写的。我们先去创建一下service，对应的。其实在我们的 service 里面我们也要去分了，对吧。是我们对应的一个前端门户里面的一个service，在我们去右键一下，右键你有一个package，取个名字就叫做center。好，OK，创建好了以后，其实对应的对于我们的一个实现也是有一个center，所以在这个后方我们也去创建一个 your package。后续我们所要去创建的一些新的service，我们都会放到center，以及是 IMP 2 点 center 里面一个是接口，一个是实现。


OK，好在我们就可以去创建一个用户了。在之前是有一个用户service，所以我们把它给拿过来，拿过来了以后，由于它的名称是一样的，但是我们尽量不要把它的名称设置成一样，会不太好。所以我们在它的前方加上一个前缀，这个前缀我们就可以一个 center 为前缀，这样子一看就知道这是一个用户中心里面所使用到的一个 user service 的OK，好重新的去修改一个名称。


双击打开。双击打开以后，在这里面会涉及到我们曾经写过的一些方法，这些方法很明显我们都是用不到了，所以我们去做一个修改改一下。这边是一个 query user info，传入的内容就是一个用户ID，根据用户的 ID 去做一个查询，把注释改掉，根据用户 ID 查询用户信息。好，这是我们的一个接口，有了接口以后再去把实现拷贝一下，推到这里面来改个名字叫做center。OK，好实现我们就已经是有了，只不过他所要去实现的一个接口，我们要改掉 center service。下方涉及到的一些内容，我们全部都可以删掉了，全部都删掉，再把抽象的方法去实现一下，相应的它的一个事物要加上它使用。既然是查询，使用 suppose 就 OK 了。下面也删掉。好。OK，在这边我们就可以根据用户的 user ID 去做一个查询就行了。我们在这边可以去写一下。既然是一个 user ID，其实也就是我们用户的一个主界，通过 user map，点 select by primary key，根据主键去查询。直接通过这样的一条语句就可以把相应的用户信息给查询出来了。


OK，查询出来其实会有一个密码的，对吧？密码我们重新的去设计一下。我们把用户去获得user，获得了以后，再把 user 点 set password，我们设置为一个空，这样子就行了。因为有蹭到前端的时候，其实会把所有的信息都会携带过去，密码我们不要带过去，这样子就 OK 了。好，这是咱们的一个service，回到我们的 center controller 里面，在这里面我们就需要去把对应的一个 service 给加入进来。

private center user service， or two words。


好。然后我们写一个接口。 public 返回的是 m Jason result 查询直接使用 user in for，写上对应的接口。第一个是API，这是 swag two 里面所对应的接口。这个接口我们的一个名称叫做获取用户信息。再来一个notes，直接拷贝过来，设置一下它的 HTTP method 获取，直接使用 get 就行了。好，加一个 get Mapping，写上路由对应的一个映射映射。在这里我们就直接使用 user info 就可以。相应的在我们的 Ctrl 的上方，你也应该要去家长。首先要写上一个rest，看错了。


再来一个是 request mapping。路由地址在这里使用的是Santa，这是用户中心。这些内容其实是和前端去对应的，因为前端也是根据这样的路由去请求的，所以我们必须得这样子去写好接口。其实我们就这样子写就 OK 了。再把这里面的内容我们要去丰富一下。不要忘记。


在这边我们是需要去传入一个参数的。传入的参数是一个 user ID 用户的组件。在这个地方我们也去加一下，加一个 swag two API palm，它传过来的参数是什么？名称是什么意思？我们都要去加一下。传过来的 name 是 user ID，这个 user ID 是用来干嘛的？ value 写上这是一个用户ID。好，再来一个request，这是一个必填项，所以我们是一个处在前边。我们有加这是一个request，看它是一个请求类型的参数。好，随后我们在这里就可以去做一个查询了。通过center， user service，点query，再把 user ID 传进去，拿到一个user，把包打入一下。拿到了以后我们就可以去做一个 return 了。


的等语号，不要忘记有称 m Jason result。点 OK 好，再把 user 返回出去。这样子我们后端的一个根据用户 ID 去获得用户的信息，这个接口其实我们就 OK 了。接下来我们就要去启动一下我们服务。首先一个不要忘记还是要 install 一下我们的一个所有的子模块，因为咱们在这里也已经是也会涉及到service，所以 install 一下 install 成功以后我们就可以来运行一下。


好。启动成功之后我们知识也是在 8088 端口好。现在我们就需要和前端去做一个联调了，我们这样子还是一样的。打开我们的在前端项目是在我们抛开的里面，所以我们会使用 g s code 打开 open with yes code 打开一下，或者你直接可以把这个项目拖进去也是没有问题的。

拖进去了以后在这里看一下这个项目和我们上一个门户端的一个前端源码相比，其实页面会比较少。在这里仅仅只涉及到了这几个页面，有 6 个，并不是很多。好，先来我们打开第一个页面，是在 user info 里面打开一下，打开以后在这里面我们往下面去查找一下。在这边会有一个用户的请求，是 render user info，查询一下，搜一下，搜到有一个请求的地址。路由 center user info， user ID 会传到我们的后端，我们目前在后端定义的接口其实就是以这样的形式去传的。


还有是一个凯德斯，这个其实是涉及到的是一个权限，我们现在都还没有涉及到，因为我们的一个用户会话我们之前也的是使用的Redis，所以前端写过写我们后端。我们在后续讲完了 Redis 以后，我们会把相应的拦截器权限，我们在这边会在后续再去给大家去说一下。所以我们一开始在做单体的时候，我们先可以不需要关注内容。


OK。好在这里我们是做一个判断，拿到了一个 result 以后去判断是不是200，是200，我们就可以拿到一些相应的用户信息了。拿到用户信息以后，在我们的前端去做一个渲染就 OK 了。下边是一个birthday，因为生日是一个时间，所以在前端这个时间会进行一个格式化的，它会格式化成一个年月日，放到一个 date pick 里面去做的一个渲染工作。OK。随后我们再来看一下这里的一个 server UI，这个是要和我们后端去联调的时候所对应的一个 URL 地址。服务端地址。其实在我们的一个在前端元网里面，其实也会涉及到一个 APP 点JS。来看一下。在这个 APP 点 JS 里面我们也是需要去配的的配置我们其实在之前是讲过的，所以我们直接拷贝过来使用就可以了。在这里 server UL 我们所使用的一个后端地址都是一模一样的。OK，随后我们在当前页面里面我们就可以去做一个测试。我们的直接现在我们就可以来做一个刷新了。刷新一下，刷新了以后发现页面上并没有什么显示，按一下 F12 到这里看一下。他报了一个 405 的错误，说是我们的一个后端项目，没有我们的 server 没有什么响应。


40 开头是代表我们的前端有问题，在这里它会有一个对应的请求地址，这个请求地址我们是可以点击打开的，点击打开以后你会发现我们的一个后端所响应的数据是有的，的确是200。所以我们现在是前端的一个问题，但是前端的问题没有任何关系，我们可以看一下的。在我们的前端来看一下，在这边是一个post，我们的后端写的是一个get，所以很明显我们的一个请求的方式不对，我们的 master 的要去修改一下，可以去改后端，也可以去改前端，都是可以的。在前端这里改成 get 就行了。我们再一次的做一个刷新，这个时候我们的一个控制台没有任何的问题是可以显示的。


OK，我们来看一下。在这里昵称是显示了对应的一个性别，在这里是保密，默认保密。最后还有是一个生日，生日默认 00 年， 1900 年的1月 1 号。OK，现在我们关于用户的信息查询，现在我们就临时可以拿到，并且渲染到我们当前页面里面的从我们表单里去的，OK。

