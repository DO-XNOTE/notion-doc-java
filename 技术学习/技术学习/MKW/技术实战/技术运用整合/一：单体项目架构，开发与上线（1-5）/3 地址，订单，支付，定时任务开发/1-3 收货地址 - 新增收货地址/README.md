---
title: 1-3 收货地址 - 新增收货地址
---

# 1-3 收货地址 - 新增收货地址

[image](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/070b2a26-c9d4-4d9a-805e-4e3bce7bba5f/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664PKVHBBX%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T224658Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDKUwXjV9Hva6WYayrb3Lg6AA0NcCMchUSckAot1y8cjgIgUopcy4OFRNiUM3xojZJ2yMeILgrzecjxnEoxE9ReWF0qiAQIxv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDEd4%2FAh3MW0gc7wQvSrcA69ms%2FLyDCaB4mirsSAC4UPCxrCZuzbRFl2ohd90ndMTZ8KwMTEeP2npnEAWhzIO%2FO0Kbf3NTro2lJEHA6V2QVJdnTix2NOrH4P7fhgCRkMK8eDeEmpfsnkysIiSI4GvREM0FUX1hXIkrtKDsRvufhp3csxgNB7uZpHsuNwB5zE%2FH8gBWRbP4seGh6HvV36gNDdfGWZhAKfC5%2BWA8zGrvFWeq5bjLkVqojSoweXnThsWI2LoGh9heZ8QmBw89z6YnhsKRrxSgirzI60d6X4nownwlf%2BhZP%2FskMeldVw9IyMrceWZoRIl24%2FVm4XZcWwrTn07nACu52FujyEfmwBUA4PkPAxKelyMPeCV3TwBC%2BL9v8auvi7fSWfyU49kPByxSm1nmLH9zGY0W8U1TEMOJevca9OuknBa4%2FgqIksKc4EQqzhdnJD3bUBS%2F79HfnJDWSpWvsrsKewJASCjBx7TqdtsNs5KXV2zjAwgWojSnWRV9wZ9u7dqa28Q0IwqsOfhB7PjI18QbqUMBQFokfnAAmnAaie3DgLxtnTC2mvjGMELUeq9X5pvt95BQToeqzdRoYXTHoBosqFxYr0Vgzjv%2FkpNTVpdC9u9mkE%2FwAZjahl%2Bat6mwD3VXPVOlPTYMJu6%2F9IGOqUBKjoQLDUf%2Br3yZHB3pW8GO7blncyLAuqdMMdK8J54NXhpq%2BCmWWtbUUr%2BCST3E895UtVnnnCz6u%2B9FTL6fMcIPVMKiEstH9lDTdIAIvQcwq5nBjXKRNF7rBvp%2FEeoNuNSWFgxB%2BWC4ko7oSETJP2iTF4j%2FMScztMa5XEMxabN0bGQCDBfeg8CjOF8ruo5ih8JadlOH6Ri%2FOR%2FiqZgM4v%2Fh%2B36YX6t&X-Amz-Signature=4d8b2320a317747c27bf7209fc2270b2fa4203f7f0dcd42c71fbbeae5b0fbc48&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

查询收货地址的接口写完以后，我们就需要编写下一个是新增收货地址，我们还是一样先看一下前端，在前端我们可以来搜一下。先送一个保存，保存在这里。其实这个按钮就是在我们的 form 表单里面可以看到，这就是一个收货人的相关信息，点击以后它会触发一个方法，叫做 save new address or update。从这个意思上就可以看得出来它这个方法点击以后，它其实是可以用于去新增，也可以用于去进行保存更新的。我们可以搜一下。


在这个地方。首先一开始我们肯定是要针对表单里面的元素去做一个判断，这些都是在前端的判断，包括到这里都是一些前端的判断，前端有判断对应的，我们在后端的接口里面，这些判断我们也要去编写的好。往下在下方它会有一个 address ID，这个 address ID 其实用于去判断它是更新还是新增的。如果它为空，在这里它就是一个新增地址。否则更新地址新增和更新这两个接口，为了避免耦合，所以在后端我们是定义为两个不同的接口。在这里去注意一下，如果你要把它们进行合并也是没有问题的。


OK，来看一下。在这里会包装一个 JSON 的 object 发送到后端，在后端接口里面去接受它。肯定是一个 b o address， b o 这是它的路由。 address 杠 add 下方我们也可以先来看一下它的更新，更新其实也是一样的，只不过它多了一项，多了一个 address ID。在新增里面，它没有 address ID 的。OK。如果更新和新增都成功了以后，首先一个它会关闭当前的窗口，就进行一个重新的地址渲染。这两个方法都是一样的。OK。好。接下来我们就可以去把Bo，先把 Bo 我们到后端去编写一下，随后再编写 service 以及是 control 了。先拷贝。随后我们到后端里面，我们找一下。找到Pojo，新增一个 b o， new 一个class，它就是一个address， the o。好在这里面写一下。先把我们拷贝的贴过来，我们加一个注释，用于新增或修改地址的 d o。好，在这里面我们把这些属性参数一个都去写一下。第一个是地址的ID，随后是用户的ID， user ID 把直接拷贝一下。 user id receiver mobile 省市区 province city。最后一个district。好，还有一项，还有是一个详细地址是底跳好。OK。这几项内容我们都已经是好了。 get set 我们也可以去生成一下。好生成OK。


Bo 其实是可以在接口里面接收，验证完毕以后再把 Bo 传到service，在 service 里面去进行一个保存。我们到 service 里面可以来写一下。先把它的方法名在这里面，我们可以去定义一下。

Public void add new user.


address 添加新的地址，在这里 user address Bo 写进来，加个注释。用户新增地址好，我们就要到 service 里面去把这个方法去实现一下。方法重写事物，我们要去声明一下。在这里面我们就需要使用一个required。好。在这里面其实我们在保存应该在新增地址的时候，应该分为两个步骤。第一个步骤其实应该要去判断一下，判断当前用户是否存在地址，如果没有，则新增为默认地址，我们是需要去做一个判断的，我们把给破起来好。第二步就是保存地址到数据库，在这里我们就可以先去做一个判断，判断我们上一个其实已经是有一个 query all 了，所以我们可以通过 this 点 query all 把 user ID 给传进去， user ID 是在 b o 里面的，通过 b o 点 get user ID，就可以去做一个查询了。

查询出来以后，我们判断一下，这是一个 address list，判断这个 list 它是不是为空。如果为空，又或者它 is empty，又或者它有一个点size，判断它的大小是不是为0。如果只要符合其中一个条件，就代表 list 或者我们的用户，它是不存在任何现有的地址的，所以我们就可以为它去赋一个值，赋为默认的地址。在这里我们可以定一个变量，定义一个参数，我们定义为 is default，默认我们设置为0。如果在这里面它是为空，也是default，就可以设定为 1 了，因为 1 就代表它是唯一的。


第一个新增的地址是一个默认地址。OK，好，下面我们就可以去做一个保存的操作了。首先我们应该要去把 user address 这个对象，也就是泡酒，我们先可以去 new 出来，这是一个 new address 新地址。在 iOS 里面，我们可以先点进来看一下在这里面所包含的一系列的参数。其实来看一下这里面我们定义的一些绝大多数的参数，其实和我们的 Bo 里面都是一模一样的，所以我们就不需要一个一个的在 address 里面去进行 set 了。


其实会有一个方法叫做 bean 与tells，它有一个方法叫做 copy practice，这个就是把属性进行拷贝，可以从一个类拷贝到另外一个目标对象里面去，只要它的属性是匹配的就可以了。好，第一个是 source 原，就是一个原来的对象，原来的对象是Adsbo，把它给写过来。 target 目标对象是 new address，贴过来就可以了。只不过我们还有一部分的属性并没有。比方它会有一个 set ID。这是新增加的一个组件。组件我们在之前已经是提到了一个唯一组件，也就是Sid。所以我们在这里是需要把 Sid 给引入进来的。 private Sid。好住进来。我们在这个地方，我们就这样子在前方，在这里就定入一个 string address ID，等于 Sid 点 next short。这样子它的组件 ID 我们就为它生成了。再来一个 set is default 是 0 还是1？是由上一个条件这里去进行判断的，所以把参数以 default 给传进来。


最后两个，一个是创建的时间，我们只叫 new 一个 date 就行了。另外一个是 set up date 一个时间，也是一个 new date。这两个一样就可以了。当对象里面的一些属性都 OK 了。以后通过 user address Mapper 点 insert 一个对象，把 new address 给进行一个插入，这样子其实就 OK 了。好，我们回到 Ctrl 了，在 Ctrl 里面再去完善一些相应的内容，把拷贝一下，再去做一个修改。


slack two 文档，它的接口名，用户新增地址把改掉，对应的现在是新增，肯定是一个post。好。随后再把路由给改掉，路由是 add 好。再来一个，这是传入的参数。传入参数是一个 request body，是一个 JS 对象，也就是一个 address b o。好，我们就不需要换行，这样子就行。 h s b o 里面包含了很多的内容，这些属性字段我们都需要去进行判断的。虽然前端判断了，后端我们也应该要去判断一下。OK，所以在这边会有一段相应的判断的方法。这一段判断的方法其实也是一些比较简单的判断方法，在这里我就直接拷贝过来看一下。


首先看一下这是一个 check address 参数，就是把 Bo 给传进来。首先要判断一下收货人不能为空，并且收货人的长度也不能够大于12，和前端是对应的。当然，如果在特定情况下，它的一个用户名的长度实在是很长，它可能会超过12。自己去改一下就可以了。因为像一些我们的少数民族，它的名字姓名都是比较长的。OK，这一点去注意一下就可以了。


最后是一个手机号的验证，手机号不能为空，手机号的长度是需要等于 11 位。另外手机号的一个格式在这里有一个类，这个类叫做 mobile email，有跳死，把这个类先导入进来。这个类已经是预先，我们在项目里面就已经是放进去的。可以看一下，其中一个是 check mobile，另外一个是 check email。现在我们邮箱没有，这个是没用到，只要使用 check 就可以了。好，这些都是一些基本的验证。随后下方是要验证一下省市区，以及是详细的地址，都必须不能为空。如果为空就要 return error message。如果都没有问题，直接一个 OK 就可以 return 了。


好。在这个地方我们如何去进行调用？很明显我们接收会使用一个，因为它返回的是一个 m 可折层result，所以我们接收也是使用去进行接收的。写一下，这是一个 check r e s 返回的对象，来一个 check address，把 b o 给传进去。在这里面我们只需要进行一个判断 check i s，点 get status。只要判断它是不是200，如果它不为200，就代表我们的判断内容是有问题的。所以直接在这个地方来一个 return return check is，把这个结果给 return 出去就行了。好，如果没有问题，在这边我们就可以直接去做一个 service 的调用，把改掉address， service 点 add new user address，把 Bo 给传入进去。好。在这边我们是不需要返回任何的list，只要返回一个 OK 这样的状态， 200 在前端接收就可以了。好，现在其实我们新增用户地址的接口，其实我们就写好了。好，我们就要来测试了。先进行一个install，成功以后我们再来进行一个服务器的重启。


好，OK，启动我们成功。我们到页面里面去测试一下。先刷新一下页面。刷新页面没有任何问题，点击使用新地址。来，我们来写一下 Jack 手机号，随便写，所在的地址我们随便说省市区，详细地址随便说一些内容，点击保存，OK。点击保存以后，我们可以看到我们新输入的内容，在这里进行了一个重新的展示，因为我们会有一个回调，回调是用于重新的去进行查询的。很显然，我们的一个添加接口已经是写好了，并且我们也已经是可以测试了上一节课的一个查询接口。


我们再可以来看一下咱们的一个数据库，我们刷新一下，可以看到地址ID，用户ID，收货人，手机号，省市区地址。另外还有一个是扩展字段，我们没有使用一个空，可以看到这是一个 is default，只有一条它默认的一个地址，它本身就是一个默认地址。OK，好。随后我们再来新增加一个地址。我们来一个 Lucy 手机号，随便填。点击保存。OK。保存成功了以后我们来看一下。这是我们刚刚所保存的，它是一个默认地址。这个是我们现在保存的一个地址，它在这里没有默认地址。来看一下我们的数据库，主要是比对一下字段，刷新一下。来看一下。可以看到第一条数据 is default，它是唯一。第二条它以后，也就是用户以后再去新增地址的时候，它的一个 is default 就永远都是 0 了。除非你手动的在页面里面把它设置为默认的，它的 is default 才会发生一个更改。OK，好。这节课我们就已经是把新增地址功能已经是写完了。

