---
title: 3-3 自定义响应数据结构
---

# 3-3 自定义响应数据结构

[image](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/28e23a8f-f26e-457f-9940-2240d9a82678/SCR-20240816-tijt.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667KHN6ASG%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T224623Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDRSwE51E26542mHFt8Cy1KQjpSkzEpuLvCZERPFwub8AIhAJUalnfuGFyzLcF1JCmfHSMEzqatpanbiHXpyJwfqHTxKogECMb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgzduCqZLNWXFIONsicq3AOtxb44agX7UY4UvGoBIIWUTeRGmYo%2FLOsV7kv8%2B4cR%2Fzvi6O8fgpEGIPAOL0DYA%2FALuVKBpCmrnc%2FnCXQstKia2lYJJXzdYfH%2BboL5KcYtPPi4d%2Fz1G84Ts%2BsZVnbgr1ikfQ6DmdXWk%2BwCodC%2BCCxuJQg8VMWmjKMIk%2BcFhM%2FkE8ELiwv8aWVI1RzrdB6A7Ac0xlyWdK8xRMNMQUvHk5fKRVArFQyADqVyrTOQ0uVkrK7DRiJ2NGK0EMuYUNWVtypxhpkVQUv0JsDzZ41%2BhbYxRIzgLUfTaQvkA8GLT%2F24P25bFvTVjFjxH4EzKTSwQ0tK4qVoLT0wtHVSZjctBJ3W41BOJUKZGhF0eE%2B4GuMyYEbLDgprz4WzQmdQUWfCXGzXFXcaVU%2BL6vwEgVVwgVyryz%2B7%2Ff873C21Bhf4SweACMDo%2FxgWz%2FyGHHB56WnwYmTD%2Fq8epXdwCbS807fhsi0zAmZOzqKM8na1sIkJtSkI%2F%2F%2FFIBb8Lv4e6K3RigSqGJaLLdFN%2B%2F3VtjJzpMReJ%2B0K7e82YjkjBBHkWnUemiQFFdaXE1soY9edRfI8WBbvMQ%2FpajHEsYdiMwM4PgYuE0t8JAHztmXcFjy3XTUIq9pVf%2B73L5Jy6ioXiumgZjCDuf%2FSBjqkAbcyriBEBeHhlStRZ6nW2qD98ny1LwDxld9UM3dGJhK0uudOHic30MKcVKXO06QJYSaHtrjTU21SbJ2wacH%2BdNuCrw%2FlBkzXHj6iZEW2aViqDo2WDLozp50jxakwp767kR8ggnz5CUsgSP77ZzOAnuXgSgxxddNX6p0D5LbN933KZwkrSJFIQGpjuNaap7yFC%2B%2FzgxKlMhX95asAD471zdEqX9sN&X-Amz-Signature=7fb511aa51303a853e3a8b13d0752500078192625a7cef8c78b95dda3c9a9eea&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

[image](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/14ce6215-77e4-406b-b4e9-8547e19c4eda/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667KHN6ASG%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T224623Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDRSwE51E26542mHFt8Cy1KQjpSkzEpuLvCZERPFwub8AIhAJUalnfuGFyzLcF1JCmfHSMEzqatpanbiHXpyJwfqHTxKogECMb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgzduCqZLNWXFIONsicq3AOtxb44agX7UY4UvGoBIIWUTeRGmYo%2FLOsV7kv8%2B4cR%2Fzvi6O8fgpEGIPAOL0DYA%2FALuVKBpCmrnc%2FnCXQstKia2lYJJXzdYfH%2BboL5KcYtPPi4d%2Fz1G84Ts%2BsZVnbgr1ikfQ6DmdXWk%2BwCodC%2BCCxuJQg8VMWmjKMIk%2BcFhM%2FkE8ELiwv8aWVI1RzrdB6A7Ac0xlyWdK8xRMNMQUvHk5fKRVArFQyADqVyrTOQ0uVkrK7DRiJ2NGK0EMuYUNWVtypxhpkVQUv0JsDzZ41%2BhbYxRIzgLUfTaQvkA8GLT%2F24P25bFvTVjFjxH4EzKTSwQ0tK4qVoLT0wtHVSZjctBJ3W41BOJUKZGhF0eE%2B4GuMyYEbLDgprz4WzQmdQUWfCXGzXFXcaVU%2BL6vwEgVVwgVyryz%2B7%2Ff873C21Bhf4SweACMDo%2FxgWz%2FyGHHB56WnwYmTD%2Fq8epXdwCbS807fhsi0zAmZOzqKM8na1sIkJtSkI%2F%2F%2FFIBb8Lv4e6K3RigSqGJaLLdFN%2B%2F3VtjJzpMReJ%2B0K7e82YjkjBBHkWnUemiQFFdaXE1soY9edRfI8WBbvMQ%2FpajHEsYdiMwM4PgYuE0t8JAHztmXcFjy3XTUIq9pVf%2B73L5Jy6ioXiumgZjCDuf%2FSBjqkAbcyriBEBeHhlStRZ6nW2qD98ny1LwDxld9UM3dGJhK0uudOHic30MKcVKXO06QJYSaHtrjTU21SbJ2wacH%2BdNuCrw%2FlBkzXHj6iZEW2aViqDo2WDLozp50jxakwp767kR8ggnz5CUsgSP77ZzOAnuXgSgxxddNX6p0D5LbN933KZwkrSJFIQGpjuNaap7yFC%2B%2FzgxKlMhX95asAD471zdEqX9sN&X-Amz-Signature=addaca1c753b5b91c6716b33db036040f3b540d74a6773ce0c3e70e16f634736&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

现在咱们第一个接口写完以后，我们是需要去进行测试的，由于我们是修改了service，所以我们是需要去安装 service 的。在这里我们进行一个全局的安装，直接把眉本里面 install 双击。我们来看一下，这个时候当我们在进行安装的时候，它其实是会报一个错的。我们来看一下，这个时候他报了一个错。 build failure 是在我们的 a p i 这一层，为什么会报错？其实主要是因为我们的测试，在这里面其实看得出来他会跑一个测试的。在这里我们可以往上面找，可以看到 my test 报了一个错。这个为什么会报错？因为在我们进行一个 install 安装的时候，其实它也会帮我们去辅助的去把 test 所有的折 unit test 去进行一个去跑一下。其实我们是可以通过每本去忽略的。在这里为了方便，我们直接把 j unit test 把这些内容，这些注解全部都注释掉，它就可以去进行安装和使用了。我们再来 install 一下。这一次我们 install 其实就可以不用success。


成功了，我们就可以启动一下我们的启动内。启动类成功以后，我们就可以去进行一个调试了。好，启动成功，我们可以打开 post 面去进行一个调试。我们看一下。在这里我们先是我预先写好的一个 URL 地址。

passport user name is exist。


这个名称我们可以定义为 mbook 的一个post。我们要改成get，我们来进行一个 send 查询一下，现在我们得到的一个状态码是200，代表是OK，没有问题的。我们来看一下后端，在后端也就是我们请求成功了m，可它不为空，并且在我们数据库里面也是没有存在的。数据库表。看一下这张 user 表，里面没有任何的记录，代表我们验证是通过的。


现在我们来看一下这个时候我们所返回的状态其实都是写死的。其实我们在之前提过，在 west for web service 里面，它其实会返回一些相应的状态码，这个状态码其实在这地方我们比方200，可以通过 HTTP status 有一个状态点，里面会有一个OK，再点击进去你会发现这个 OK 其实它相当于是一个。这些内容其实都是一个的枚举，每一个状态它都是由一个 h t t p status 所构成的。所以我们又可以在这里这样子写一个 h t t p status 500。我们直接可以通过这里面其实会有，使用的时候可以到这边去找一下。比方根据这里面的一些不同的内容，我们可以找 soldier 50 开头，我们就可以以 500 为例。使用 server error 写到这里。很简单，下一个我们也可以写到这里。 h t b status 也写好了，我们进行一个重启。好，重启成功。随后我们到 Postman 再来发送一次请求，这个时候你会得到一个OK。这个 OK 其实就是由后端所提供的。后端我们在这里是提供的一个 h t p status，OK，这种方式其实是 rest for web service 的一种返回的规范，它的这种规范其实也是比较强，是一种强规范。我们能不能去把这种状态和我们的一些业务参数，业务的一些内容我们可以封装到一起，包裹在一起，传到前端。


答案肯定是可以的。在这里我们可以来参考一下京东是怎么做的。我们在这里打开京东的某一个商品，这是他的商品详情页，刷新一下。刷新一下了以后，在这个下方会有很多的一些内容去进行加载。其实这里面的内容包含了像图片，HTML，杰森，像 base 64 的图片等等，会有很多。我们到这里面我们可以来找一下，找一个内容有一个叫做recommend，我们可以点击来看一下。点击看一下以后在这一端你会发现这边会有一个 handle table call back，这个其实就是一个参数，这个参数你会发现它有一个 status 是200200，看到200。我们应该要想到它是一个接口调用的成功状态码。我们是可以把这里面的内容是去拷贝一下的，比方我们就可以从这边开始拷贝，一直拷贝到最后面，我们来看一下，一直到到这里到部位拷贝一下。拷贝了以后我们可以放到杰森的校验里面，可以打开网址，可以通过百度去搜的，直接敲一个杰森就会有很多的网站去让我们验证，节省格式。


拷贝过来，我们格式化进行校验，现在我们验证以后，它是一个政策的JSON，放大看一下，点这边会有一个提示。这个其实就是我们拿到的一个相应的内容。由京东里面的。首先来看一下，这个是一个status，是一个状态码，随后下方又有一个data。 data 其实就是一堆数据，又可以把它作为是一种业务型的一些参数。反参的返回的一些数据都可以放到 data 里面去，又会有很多的一些内容。其实它本身就是一个实体类，会包含一些相应的属性，比方有一个transform，还有name，这个应该是商品名w，i，d，还有是图片。另外下方还包含了一个list，这个 list 它也是一个 JS 对象。


OK，其实这里面包含了很多的内容，我们能不能根据这样的内容去进行一个封装，我们在前端接受的时候，也可以通过这种形式去拿到相应的数据。对于前端来讲，我们后端所提供的内容就比较的丰富了，我们可以把状态码是否成功的，还有一些业务型的内容，我们都可以封装到一起。OK，我们是可以这么做的。我们可以来看一下。


在这里其实我已经是预先为大家提供了这样的一个封装的类。我们来看一下。在这个部位，在common，也就是我们的一些通用的工具类，参数等等都是放在这里面的，包括枚举，我们也可以放到这里面。我们在这边我们可以先创建一个package，我们定义为 Com 点m，可点 util utils。随后我直接把这个类拷贝过来。这个类的名称叫做 m Jason result。在其他的一些实战课程中，老师我也是使用的这种方式，封装了一些内容提供到前端的。点 OK 拷贝过来，大家直接可以把拿过去拷贝到自己的项目里面去，也是没有问题的。


放大看一下这一类主要是用于干嘛？它是一个自定义的响应数据结构，这个类是可以提供给像 H5L s，安卓公众号以及是小程序，只要是前端都可以调用。当然以后可能会有更多的一些前端，你都可以使用这个类去使用。前端。拿到这样的数据以后，其实它本身当前数据拿到了以后，它是一个 JSON object，拿到以后可以根据自己的一些业务去实现相应的功能。都可以在我们当前类里面。


我目前是封装了一些长尾的状态，两版是表示成功，这个就是对应到 h t d p 的一个success，也就是 OK 状态。另外还有是 5005015025556 这些其实我们都可以去使用。掏出鱼箱可以使用55。另外像 500 验证错误等等都可以放在这里面。这个里面会包含了一个 message 的字段。


另外还有是 501 和502，这个我用的暂时不是很多，如果要一次性的，要校验多个不同的一个数据错误，可以使用501501，它本身是以一个 map 形式放进去的，都以都是一个一个的舰只对。另外还有 502502 是我们后面会使用到拦截器，当我们在使用到拦截器了以后，我们会使用到 502 状态OK，在下方会有很多的一些内容，比方这个就是status，这个 status 其实就是对应到 status 200。还有是一个data，是，在这里我们的一些响应的数据是可以放到数据里面去的。另外还有是message，如果我们发生了一些错误，我们可以在 message 里面直接塞入错误的内容。如果我们的是一个正常是OK，是 200 状态，在 message 里面我们就可以放入一个OK，放入一个字符串，下方还有一个OK，这个是我暂时没有用到，我直接使用了 Jessie Ignore 忽略了。所以我们只需要关注前面这几个就可以了。


在这里面会有很多的一些内容，比方我们会最使用到最常用的，会有一个 OK 当前的类点OK，直接就返回一个 200 状态出去了。如果你要返回一些业务型的内容，直接把业务的参数放到这里面。 object 你可以塞一个list，也可以是一个对象，都是没有问题的。当然如果是一些错误比方，我们会使用到 l message， l map 一一的都会对应到相应的内容的。比方我们可以点一个 message message，它其实就是 return 的一个 m 可 result 状态会放入200，这是这个 message 就是一个消息的错误。我们没有额外的一些 data data，我们的业务参数设置为空就可以了。


OK，接下来我们就可以来使用一下 m 可result，拷贝一下，贴到我们这个地方，使用 m result 就可以了。随后在这里现在我们是发生了一个错误，我们在直接可以使用 return 一个 m 可result，随后我们应该要去怎么去使用它？其实会有一个点，我们来看一下它有一个点，点一下会有一个error，可以看到会有很多，这些都是我们可以自去自定义的。如果以后你有更多的一些错误，你可以自己去扩展是没问题的。在这边我们比较简单使用 error message，随后在这边传入一个内容，比方用户名不能为空。


OK，下方我们可以来一个 imock result，点 error message 可以传入一个用户名已经存在。OK，这两个都是错误，成功我们只需要通过 m 可 JSON result 点OK，有一个 OK 这样的方法，点进去看一下，其实他就直接 return 了一个 new imock result，这里面是放入了一个空的 data 数据。再点一下可以看到它是为我们当前付了一个 200 状态 message 是OK，当然 data 是为空的OK。好，现在我们当前参数反参，其实我们就已经是设置好了。我们重新的再来跑一下。我们是需要去 install 一下，因为我们在有跳，也就是 common 子工程里面，我们是加入了一个 m result，重新 install 以后我们再来跑一下。


好，现在是运行成功了。随后我们来看一下 post name 里面，现在我们再来一次点击send，随后我们在拿到的这些内容就比较丰富了。来看一下。我们现在状态是200，代表我们接口请求是成功的。我们的 user name 用户名是可用的，又会有一个message，这个代表是我们的一个消息，传过来的消息是 OK 的。就是这样子的示意 data 就不用管了，没有用。如果我们 user name 设置为空，我们可以把 imock 删掉。


点击 send 发送，随后我们拿到的一个内容是500。我们的一个业务是什么？也就是错误的内容是用户名不能为空。OK。现在我们就已经是正常的 OK 了。如果我们当前 m 可注册成功了，你再一次再去请求，会提示用户名已经存在OK。这个就是我们这一节所讲的一个封装的results，这个是用处比较好的，相应的内容你都可以往这里面去塞。OK？



