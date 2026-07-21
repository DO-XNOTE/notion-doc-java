---
title: 1-3 用户中心 - 修改用户信息
---

# 1-3 用户中心 - 修改用户信息

[image](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/a110befb-ca5b-489c-b58d-b3cb48dbe381/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YXRTLXLY%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T224723Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIFw2%2BxKKR%2BHe%2BVivsryrWlGQMbvYexOJ5nizCblV0bS9AiBbeWof1tIUT6q3z89PuJjwFMYt40ZgxpMNW81IoZhEvSqIBAjG%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMiRp%2FRTVTFjWaQdNXKtwD%2BALQUMY1i1c3TX6UXWqy4QQWG9siOsrpLNc4zECdmhXAI%2B2e1oS2tcfUXhB7V3nCG9c%2BvBngUhXQWIeQfGhswZb8XDiQRk8SA9Kc1jnHdeD6DaZPgUQpoJGUmfnrLPB51OqUANCjC7DIPf3uN01BRXF4F6xZVoS%2BHSi7ez2JxF42fMUC68nuFdM67rCbkHTvx7vj3lDE3OKj4knQMhw%2Fk0pPW7hetvtSRW8RXa2wPo8UZNuYSybPXZOkTNjv%2FGoXKPbOnOGAeJt5ABgoPBp8vK2TICDEStuycyprQRYqXbv8hbFnFTpbZNKl1a6DMRWdA4I75GX5dswgwD61SF4hPd4vqnbIS8XRJaq84vN%2Ffsf9bzGEftacP4gOo%2BsFqxmRbqSdRFxJuFTfqM%2BSCoHlqw3ov3Yqy%2FtdkokijbtiVgLUlVGH22O4mCn9ow%2FjJ7WiYm42bwZ5dkoKiBdRfeJmQqDIk2yOmidQhCrtCt0qg9H5K2KXUr2rFO7oX38B%2B4xmsglc7SjHgDIOh8O%2B5HdNqotmkMwtENeKj22X5g14c1CPolRLSbfPbNk4c16rk3q%2B84p813IryzTAxivqYgms4Vy5zOwNE4y%2FA%2FaiNGScEG6o%2BJoGh6uOBK8cVQcwo7j%2F0gY6pgEHjm5kbIg4xqjRr2hIcCnbQgEJR3JNVAhB5rP0YkGRHONeSnK43DE4Oe59dH7RBX%2FbJe3mZrUlwRciquyW3et9Ahny0Ekk1TLr128qNse5%2BJLovYSJCtwcgI3R%2BLo59oROmsaQRv27DNQOr0mfii2vVYQ5BbOrTKerq5Px5ouffWTDSnZsHC%2FA78tZQ49PAjRfhPDjDdQ12PT59XiQMNZ%2Fom%2FB3Euu&X-Amz-Signature=4a42d664b9669939be7ac87a8ec354a0bb1d4c35d19169cc54978c066b3f157d&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

用户信息查询出来以后，我们所需要去做的应该是点击保存修改按钮，把相应的一些信息发送到后端，再去做一个更新操作。所以我们这节课会来讲一下这一步的内容。首先在我们当前的表单里面，其实相应的内容都是默认的必填的，比方昵称是必须要有的。如果我们把删掉，直接点击保存修改，它会提示昵称不能为空，因为每个人的昵称都是必须要有的。我们可以先来看一下咱们的前端，在前端里面我们可以先来搜一下，搜一个保存修改，在这里会有一个相应的按钮，这个按钮里面点击之后就会触发 click 事件，搜一下 save user info。首先我们肯定要做的就是针对于表单里面的每一个属性元素做一些判断，比方昵称不能为空，昵称的长度也是需要去控制的，不能够超过 12 位。其次，如果你写了一个真实姓名，真实姓名的长度也不能够太长。随后，下方就是针对手机号做的一个验证。手机号的验证方式我们之前其实也说了，在这里会有一个 APP 点 check mobile，这里面其实是根据手机号的一个有效性去做的一个验证。下方还会有一个email， email 其实也是一样，在这里面也会对应有一个 email 邮箱的有效性验证。


可以看到，其实这两个不管是 check mobile 还是 check email，这两个都是涉及到正则表达式的一个验证。OK。好。如果这些信息全部都验证OK，没有问题。在我们就可以去发起一个请求。首先我们是一个post，请求信息发送到后端，相应的一个用户对象要去修改的信息，其实我们就会把它包装成一个用户对象来，其实也就是一个 Bo 传递到后端。在后端接收到以后就可以去做一个相应的处理。除了一个对象以外，用户的一个 ID 也是需要传过去的。如果我们的操作成功，在我们的当前页面，当前页面会提示用户的信息就修改成功了。


OK，好，接下来我们就可以去写一下咱们的后端。首先我们先把接口先去定一下，借口的内容可以先不做，先去定义，把这一段内容。这当前是一个 center controller，是用户中心的一个，我们就需要去创建一个新的 controller 了。在这里我们取一个名字，取一个名字就叫做 center User。恳求的OK，我们使用这个名字。首先我们还是一样是需要去在这里去定一个 rest 狠出来。随后 a p i 也要去定义的， a p i value，这是用户信息用户信息接口，再加一个是 tax 用户信息相关接口。


好。另外再加上一个对应的路由 request mapping。我们要和前端保持一致，在前端里面所设置的是一个 user info，所以在我们的后端也是需要去设置为 user info 的。好，在这里面我们就可以去把对应的一个 Ctrl 了去写一下了。我们直接把 center Ctrl 了这一部分的内容我们贴过来，贴到这个位置。贴过来以后，我们就要去做一定的修改。首先我们的一个Mapping，这里应该是 post Mapping，路由地址改为update，方法名也对应的改为update。在这里就是修改用户信息了。要传进来的一个参数。第一个是一个请求，参数是 user ID，我们保持默认放出去就可以了。下一个，下一个，我们就需要去构建一个 bo 对象了，是传一个 request body，好写一下，我们要写一个 users Bo Bo，目前我已经是预先写了。


进来看一下，这个名字叫做叫做 users b o，这个和我们之前在天天吃货它的一个门户端的 b o 明确有点类似，在我们做一个修改，把他的名字改成 center user b。 o 点击 effect 不要忘记，最后还有一个确定 do reflect 点一下，这样子他才能够重命名。打开看一下。


在这里面其实我已经是写了一些相应的属性了，这些属性的名称其实全部都是和前端一一对应的。OK，只不过像一个密码确认密码我们是用不到也无所谓，其他的内容我们都是会使用到的。这个是 slack two 针对于我们属性的一个诠释。其他的一些属性都是对应的就不去多说了。对应到了以后在我们的 Ctrl 是可以获得的。


OK，写一下 center user Bo 传进来。好，传进来了以后在我们就可以去做一个修改操作，我们先保持这样子，直接给他一个OK。好。随后我们去编写一下咱们的service。 service 也是会在 center user service 里面去做到的。一个编写写一下，取一个名字。 public fried updates user info 传入的参数第一个是用户的 user ID，第二个是 center user Bo。把 Bo 业务对象需要传入进来，加一个注释，修改用户信息。好，把这个方法我们来实现一下。先把事物加上，由于是修改，所以这里要使用required。好在这里面就可以去做相应的内容了。


我们传入进来的是一个user，比 o user bo 其实和我们的用户对象其实是一样的，有些属性 soul 角users。可以看到这里面的一些属性是 Ctrl 加F12。来看一下这里面的大部分的属性，其实我们都是一模一样的。这个下方是定义的是有的。所以既然它是一个 user b o，我们会使用到。我们之前所使用的一个方法，叫做being。有一个叫做 b utils。点 copy parties 属性拷贝属性拷贝是把我们的center，user， Bo source 拷贝到一个target。在这里我们来定义一下第一个users，这是 updates user，把它给 u 出来， u 了以后把新的目标对象写过来。这样子由于属性名称一样，就会把 Bo 里面的属性的一些值拷贝到新创建的 users 对象里面去了。


OK，只不过我们要在 update user 里面需要去设置一个ID，也就是用户组件 user ID 写进去，写进去了以后还有一个用户，其实它会有一个更新的时间，我们也是需要去设置的。 set update time，把当前的一个时间我们要去写一下，因为你要去做一个更新的。随后我们就可以使用 user map 点 update 来搜一下，我们在这边会使用一个。

Update by primary key selected.


使用把对象直接给丢进去，他就可以去做一个更新的操作了。更新完毕以后，由于我们的信息是更新过了，所以我们在这边要去重新的再去查询一下。使用 query user info，这个是我们上一节讲的方法。直接把 user ID 给丢进来，我们查询到一个新的用户对象以后，在这边我们做一个，也称，有衬出去就可以了。在 forward 我们是需要去修改，改成users，在接口里面对应的也要改成users。OK，这个 service 我们就已经是写好了。写好以后我们就需要到 Ctrl 的把相应的代码去完善一下。也是一样。使用 center service 点 update user info，把 user ID 以及是 b o 给传进去，传进去以后我们会得到一个新的更新过的一个用户，取名为 user result。

