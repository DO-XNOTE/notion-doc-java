---
title: 4-4 OSS实现图片上传
---

# 4-4 OSS实现图片上传

[image](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/f97e58fb-583d-42b9-9ece-dc60736aa180/SCR-20240806-knhu.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46655DNMTDX%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T225228Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCI1sFA2utdxDhSoa9VUd82BTslLuAQQcL2IP36XNtm0AIgZENE8oJe1BhyLcWrcUci6zHzdsYUATNSM443Xjw8aGcqiAQIxv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDPBCwXi93gSWiooK7ircA9ffO3IGip8BnOh%2F8lLuK8d1XDz6NvpObWgBgAwQb6a3BY53GID4o1NIsrMLFwLi8qi3GV%2Bzh9GjmsVoR4zucLbQQAVV28%2FvIDunzqxg1vCi32de7%2F5wJKxeW%2B3rE6rmFWPN7%2BovqwHXQAwaKKQh0toSafOyw0oo2QP%2BkPFLggdbU9eEgl8tAgkNYSM%2FXcwszH%2FMCKjKR%2Fk7LO40Mo9VrZJObrsc%2FXBLN5OnntaXZWNOoZTGgl7lOuP9soJMlM7mF7R%2Bdw%2FkYRUzPm75bFkv4ACbWQdzU6eBLtayr3T1ddeK8DxpiW%2BsXdi0LORMWPU0rNXeSUg3e%2BTj%2BNniFHvfFHFF2xiCOEixgAj%2FNqZJcTNyE25JFfXlZgIAUvmM6wULbHdNPAqcIjH%2FdPQSs%2F%2B9fKBfp8p%2FCOew7OXiiglFg37HPlU8bLhJ0%2Bg7Fp59RzZkJ3kPoJNzWwWLb9g%2FstZHGsYHgObVAJWTV2UoGO%2FHf0xFSQF%2FVPLno2UAeWjoLxRFR14eFzQK7F9i3XoTT8MQyEhfBq1rzMYFw8SRmFdTXImO2hSWVql0LvHecH%2FrnOZnHna95vy%2BeK8giT7jNSJar9fGrSXejI8H99rGZk6r%2FR8ttZ8RsLvj%2FItMNFw%2BMKG6%2F9IGOqUBKVHFEv5RhRbAA%2FsTn6w008f7cOZXV58tjjZKcJZ5n49kSyvIQlCh0vVyVDx2FGEhXcFZtozy1gUSQ%2BfTr7UvU9z0DbJZnXrDHNcIXs3Dh57oY3dy4rPH8tZAcv%2BPS8iaHuYrxrGGRVObRA8D27uq8p09hUSdjFHDhCb7032dc76kfHOS62eTWGg87mH12M5ihKiGVLEjNdlRJTmYxm6fhsm1cR%2Fs&X-Amz-Signature=e9fb79f2bb45ed315152cc3bf2f0097764db20d17cfae1c6fc98ad01e44869bf&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

那么上节课我们是配置了 OSS 的一个SDK，以及是一些基本的参数，那么接下来的话我们就可以去完善这样的一段代码了，我们去实现一下打开我们的开发工具，那么我们可以使用之前我们的一个service，那么在这个 service 里面我们可以去创建一个，我们去创建一个新的方法。


那么这个改一下，改成 upload o s，那么传入会传进来一些相应的内容。首先第一个这个 multpot file，那么这个我们是需要去传进去的。此外这是它的一个后缀名，对于我们这个 o s 上传的话，这个东西其实可以不需要，那么在这里我们传一个 user ID，把这个传进去。然后到我们的 service 去把这个方法去实现一下。


然后我们在这里面去做相应的代码的编写，那么首先我们先把这一段内容直接拷贝过来，贴到这个位置，然后这些注释的话我就去掉了，我就不加了。那么这几个我们都已经在配置文件里面，所以我们全部都删掉这个注释，不需要上传网络流注释不需要关闭，我们就保持这样子。


然后这个 OSS 我们先把它给引入进来，我们这个 SDK 有了之后我们是可以拿到的。那么第一步这边是我们要去构建一个 OSS client，我们是通过这个 client 去做一个上传的，通过这个build，那么这个我们也要去引入一下，最后下一个下面，这在这里面要传入三个参数。那么这三个参数我们都是在配置文件里面所配置的，所以我们可以去加一下啊。在这里是 file resource，然后我们直接就可以去拿了。第一个是 get and point，我们把这个给获取一下，随后第二个，那么第二个是TID。随后下一个是这个 secret 拿到以后我们都能够传入到这个 build 里面去构建一个 OSS client。这个注释我们还是加一下吧，构建 OSS client，那么下面一个在这个位置是有一个 input stream，那么这个从哪里来？那么这个其实就是从我们这个 Multi part file 从这个里面来的。我们直接通过这个 file 点 get yet input stream 就可以拿到了，那么拿到以后这个就直接丢进这个 OSS client 里面做一个上传就行了。好，然后下面在这里有一个 bucket name，这个也是通过 file resource 去获取。


然后我们有了这个 bucket name 以后，那么接下来我们要去构建一个 object name，那么这个其实就是我们的一个文件上传路径，那么在这里面我们也能够去设置一下。我们先来写一个string，这是一个 my object name 等于，那么这个从哪里来？也是从这个 resource 里面去获取get，我们之前是设了一个，有一个 object name 先拿一下，拿到以后它仅仅只是一个路径，但是它并没有包含我们的一个图片的名称，或者一些其他的动态的路径，那么在我们这里也是可以去构建的，在这边在这个后面我们可以去加一下。那么加一个斜杠，就是它的一个上传的一个目录，我们使用这个 user ID 去加一下每一个用户的一些图片，都在这个用户 ID 的自身的一个文件夹之下。


然后我们再来加上一个斜杠，那么这个斜杠就是用于去拼接你的一个 ID 了，拼接你的 ID 以及是你的后缀，那么这个后缀的话，我们在这里可以直接去加一下，可以去加一个，比方说点 j p g，你可以自己去加，那么当然我们也可以去传，我们可以去修改我们的 gecko 接口，我们这个之前是去掉了，我们再去加一下，把它给加进来。那么这样我们的后缀就直接是有了，只需要在这个后面替换掉，那么这样子我们的一个路径就已经是设置好了，这个就是我们的 object name。等到上传以后你就会非常的清晰，能够看到这个图片所在的具体的一个路径，把这个贴过来。那么这样子的话，我们这个 object 就已经是放进去了，那么这样子其实就会做一个上传，那么上传完毕把这个 client shut down 去做一个关闭，那么这样子的话其实就 OK 了。


但是我们的这个图片的路径我们是要去存储，那么存储的话在这边如何去使用呢？那么在这个地方我们的这个 my object name 可以直接 return 出去。我们在这里可以去做一个拼接，就是说这个其实是存储在我们 OSS 中的一个路径，那么他要去对于公网，对于外网的用户来去进行一个展示的话，那么其实你也要去做一个构建，那么这个构建在 bucket 中的一个概览里面有一个 bucket 域名，有一个这个也是用于去外网访问的。有一个这个东西，把这个去拷贝一下， Ctrl c 拷贝，然后拷贝以后你也要去做一个设置到这个部位，把这个当做是我们的一个访问的路径，其实也就是我们的一个 host 的位置。
在这边写一下赛尔，我们取一个名字叫做 OSS host，取这个名字，那么前面加一下 h t t p，它是支持 h t t p s 的，对吧？使用这个就行了。那么这个就是它后面的一个URL，然后加一个斜杠，那么这个 host 和这个 object name 是需要去做一个拼接的，先把这个设计一下到我们的 resource 里面去做一个构建。


生成了，生成以后，那么在我们的 service 里面，在这个地方我们就可以去做一个拼接了，拼接的话直接使用 resource 点 get host，应该是 get o s 的host，这个再去做一个拼接，那么这样子就是相当于是我们的一个服务地址，外加我具体的一个路径，那么这样子拼接以后它就是真实的一个图片地址了。然后这一块业务的话，其实我们在这边就已经是写完了，那么写完之后在这个地方是咱们的service，那么我们还需要到 Controller 里面去完善一下，把这个 Controller 打开啊。那么在这边的话， Controller 其实我们就使用上一个，在这里面我们做一些小的修改就可以了，我们把这个给注释掉。
然后在这边有一个 file suffix，这边我们使用 upload o s 使用这个，然后呢你还要去传入一个 user ID。那么这样子的话就是 OOSS 的方式去做一个上传，然后会拿到一个 pass 路径，那么这个路径的话其实就是一个可以直接去访问的一个路径，在这边会进行一个判断，然后这边又有一个拼接，这边拼接我们不需要了，对吧？因为我们现在不是 fast d f s，所以我们在这个地方直接去展示就可以了。当然我们拿到一个 pass 之后，我们也可以在外部去进行一个拼接。那么我们把这一段内容放在外部，那么这样子可以统一一些，我们直接在它的外部，在这个地方加上这个pass。那么这样子就可以了，把上面这个直接给注释掉，使用下面这个。


那么这样子我们就是在原来的这个 Controller 里面去修改了两行代码，一行代码是我们使用了这个 apple 的 OSS 去做一个上传，然后下一个的话，当我们拿到了一个 pass 以后，我们是和这个 OSS host 去做一个拼接，会拿到一个可以在外网去访问的一个链接。好，然后我们来启动一下啊。启动，然后我们再把之前的API，我们把这个 API 工程也要去做一个启动。然后我们打开浏览器，在这边我们可以来测试一下这个上传，那么也是随机，我们选择一张图片，点击打开。


那么这个时候提示说文件头像上传成功，上传成功这边一张头像也会发生一个更改，我们可以检查一下右键检查，那么在这里面我们来看一下，你会发现在我们在这边所展示的一张图片，你们发现这个其实就是 OSS 的一个地址，阿里云的一个地址，这就是我们所上传的，然后这个也就是我们所拼接的这一段路径，我们拼接的时候，前面这一段是咱们的一个 OSS 的host，后面一段是 object name。也就是我们图片所在的一个路径，以及是它的一个文件名。


那么它的一个路径的话，前面这两个forty、d、e、 V 和 Images 这个是我们写死的一个配置，后面一个这是 user ID 和 user ID 的一个图片，那么这个的话其实我们也是，我们是动态的去写的。好，然后我们这样子，我们到它的一个管理平台去看一下文件管理，那么在这边你会发现有一个foodie，第一笔我们点击一下，然后 images 这边这是用户的一个名字ID，再点击一下，你会发现在这里有一张图片，然后点击一下，那么当前这边可以看到我们这个 PNG 其实有一些小问题，那么它的这个后缀名的话，在你要去进行一个使用的时候，你要去加上一个点的这个我们在程序里面没有加，我们去稍微做一个修改。我们找到之前的在这个位置，这里有一个后缀名，我们去加一下，去加一个点，然后我们再去重启一下，把当前这个服务重启一下。


然后我们再来测试一下，我们点击上传一下，这次选这张图片，打开。上传成功，然后再来看一下，我们刷新一下。这个时候可以看到这个时候我们这个点就已经是加进去了，然后点一下这张图片是可以去进行一个展示的。那么当然你也可以到咱们的数据库里面去刷新一下，来看一下我们数据库中的这一条记录。那么来看一下这个 ABC 这个用户，看一下这个地址也能够存到我们的数据库里面去的。那么这样子的话，就是我们现在就已经是通过了 OSS 的一个整合来实现了我们项目和第三方云存储的一个结合。那么当然如果说你使用过七牛云，或者说是腾讯云的一个文件存储的话，那么其实也可以达到同样的一个效果。

