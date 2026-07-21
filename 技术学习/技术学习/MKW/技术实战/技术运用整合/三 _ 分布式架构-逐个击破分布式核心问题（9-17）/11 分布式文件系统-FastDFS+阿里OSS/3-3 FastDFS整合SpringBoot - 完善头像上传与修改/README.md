---
title: 3-3 FastDFS整合SpringBoot - 完善头像上传与修改
---

# 3-3 FastDFS整合SpringBoot - 完善头像上传与修改

[image](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/50f8c95e-e67b-461b-81df-5afbca8404d6/SCR-20240806-kfpc.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663KLQJ557%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T225225Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDh5WyUgIwviQXre6FqhtaP3%2BZNl3QPyaB5D0b6gz9QmQIgfj22B4sw8wQEUAo1MhbfBjqOoJwctDNUmF72Tz500tQqiAQIxv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDLojvQL8x6v7JUJ43SrcA7LHexza58HKfmUujPh58ucyyrFT4plbE8GjPiiDvKt3EoziBeVwHBG7imLhBAQUE%2FkN0oiyVfq2sXUV%2BnmhLyL%2Fhtt2g7sR3t95bfpO%2FyCKPyC%2FuXUFzIZbo7w%2FFZJX3HW3qTVmRhQ1QE4%2B5JntBjrZDaJOC34oDHr7PA04yGQucOvVrguF12vmElmz%2BDiO0Kjiy7AhfaF5WGF8Hr27C3k1%2F5Sv9T8EN78BJLaNnFLOIqF%2FbzCYn%2F1UAVJ058xyivdpDW4idFhSskTcXL0u2aeKTD%2BzMld4q656VMOmaBSL752z0veA1nkTkRWePjiGJeaxNumLNEkqD0GlDqZnq0XTj02t7A3hEsPHFYk1Pbn7UVwrG6B6yV7YNXABNJdJzRNGhQ4ZrC62l%2Fefd0atvfBAZDCZ0U48bQmEiWX8OAL%2B1HXn1C9m3NqW47tTQ2kvaaQRIrDObu0a9tck8stkHu4c5t65xksfnvMVT%2B16RcYi1pxk%2BPY2KC4hD3r4sYrPTWM0mxiBlxo3fcDEMh%2F9u7jg%2BwDbDvY%2FBF7K1b%2BP3qDG30A%2BVJokFsqvibhQEND23XOmdDn8FU8OQZgOkzVXpeHERzCqqy5TDnKePiwcxo8CEGqseZ%2B7scP3rHRHMMS6%2F9IGOqUB8kYtUxxxQxR%2Frhix8waG4rbR%2BCyjpVVVj8xv0dNY7drd1%2BrlHe99apeRJ1ktvGibBcGUFDqwnwkWgfd7KjHYRCOBHFCCYoDnjcazVOyf6CeJSeMJt16FnjSXq14DQ4je39LoqyAU9xQLr2Z%2BHzReZJrxj7OwacvInzO%2BYaNl29aQlVou0KnyQbqf4FbSuw9x9Tolhs9PpfVeiD7RmhwBOvajvfLy&X-Amz-Signature=2353785d8962791fedda63f582ed9e486f9d829368a83f25dbe97ec64c4df79b&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

那么上一节我们是实现了用户头像的一个上传，使用的是 fast d f s 所提供的一个 storage client，那么接下来我们还是需要去做一个相应的完善，因为我们还没有把这个数据更新到咱们的一个数据库里面，那么这是我们之前注释的一段代码，我们把它给开放。然后我们来看一下，首先我们要去做一个拼接，那么在这里其实我们是拿到的是一个pass，所以这个 pass 的话，我们在这个地方我们是需要去拿一下，我们把这个 pass 提取到它的一个上方，定义是一个空的路径，在这边我们可以拿到，那么在这里我们就可以去做一个判断。 string utils。如果说它是不为空的，那么在这里我们就可以去做一些相应的处理，否则我们就提示一下说。


上传头像失败。好，然后我们把这下面的一段内容，我们直接拷贝推到这个里面了。这一段是不需要的，然后写一下，首先那么在这里是有一个拼接，拼接的话那么是要把我们的一个服务的地址，就是图片服务的地址，我们要去写上。那么在这里的话我们是需要去做一个定义，那么在这边我们使用一个资源文件的一个映射的方式去做一个相应的一个创建，我们在这里边我们去创建一个promise，我们你有一个file，取一个名字叫做 file practice 也OK。


好，然后我们在这里面去写上相应的内容，我们定义一下，比方说 file 点host，这是它的一个地址吗？短语我们写一个h，我们这样子直接拷贝一下，直接把前面的这一段内容拷贝回到我们这个部位，那么这个就是我们的host，我们的一个图片服务的一个地址，然后我们再去创建一个类，这个类的话是和我们当前这个 promise 做的一个资源的映射，我们去创建一个package，取一个名字，取名叫做resource。


在这里面我们新创建一个 class 类，这个其实我们之前是有讲过的，取个名字 file 有source，那么在这边我们就可以和咱们的智能文件去做一个预设了。首先我们把它定义为是一个component，好，然后再来一个我们注解是 configuration properties 是这个，那么这个是要和我们做到一个相应的一个映射，这个映射的话映射到我们的是file，有一个叫做 traffics 前缀，这个是file，也就是我们在这个资源文件里面所定义的这个file，这个前缀好，然后我们的这个文件的地址，它还有一个叫做property，有一个 property source，这是我们的一个文件的原地址，我们是需要去写进来。那么它是在我们的 class part 之下， class pass 冒号。然后 file 点 promise 直接拷贝一下。


OK，那么这个这样子的话，我们就已经是做好了配置，最后我们把属性去写一下， private string host get set 去生成一下，好，OK，那么这个我们就已经是装备好了，这个应该是错别字吧？拼错了， idea 帮我们做了一个提示，那么没有关系，我们可以去做一个修改 shift F6，那么这是可以去修改它的一个名称的，改成c。


好，OK，那么这样子就已经是修改好了，然后我们把这个放到我们的 Controller 里面，我们把它给注进来，注进来以后我们就可以去使用了，那么在我们的下方就可以去做一个拼接，通过这个 file resource 点 get host，然后就可以去拼接一下咱们的这个 URL 的一个pass，这个 pass 就这个直接去做一个拼接，拼接好了就可以了。


那么后面的话，后面这些内容我们就不需要了，这个是我们之前有讲过的，就是说增加一个时间戳，那么我们的浏览器就不会存在一个缓存的问题，它会帮我们去做一个刷新的。那么我们在这里就不需要，因为我们每次上传的话，其实文件的一个文件名是由 fast d f s 会帮我们去做的一个相应的处理，每次上传之后它的文件名肯定是不一样的，所以我们保持这样的一个拼接就可以了。


好，最后下一个，下一个是更新，更新头像到数据库，好，写一下这是users，然后这是这里有一个 center user service。那么这个我们直接可以从以前的里面拿过来，我们去找一下，对吧？在这个地方就是这一段的 service 直接给拷贝过来，拷贝到它的上方。好，OK，那么这样子，那么它就可以去做相应的一个调用了。好，然后这里是一个上传，然后这里还有一个 convert users VO，那么这个东西的话我们也去看一下，在我们以前的地方。那么如果说这些内容这个上传的操作你是放在以前的这个 Ctrl 里面，那么这些代码你是不需要再去拷贝来拷贝去的。我们在这边的话就直接可以去拿一下，在这里有一个 convert user VO 在 base Controller，在这里面我们直接我们把这个 base Controller 直接拷贝过来，然后在我们当前的这个 Controller 我们再去做一个extense。好，OK，那么这个就有了，然后 user view 把它的包给引入一下，然后在这里还有是 cookie 的一个写入，以及是一个 js utils，把它的这个类都倒一下。


那么这样子这一段内容我们其实就已经是 OK 了，随后我们就可以来做一个相应的测试，来看一下我们的这个数据，写入到我们的数据库里面，看一下头像的更新。那么我们重启一下当前的服务器，重启之后我们再来回到页面上去做一个相应的一个上传测试。


好，OK，那么重启成功，然后我们到页面，我们点击一下，选择任意一张头像上传，OK，头像上传成功，点击确定。然后你会发现我们这张图片在这个位置其实已经是变更了，成为了一张新的一个图片，新的一个头像。然后我们打开数据库，在数据库里面把这个 users 这张表双击一下刷新。那么你会发现在这里刚刚我的这个 ABC 这个用户，那么在这里的一个图片，这个目前就是我们最新上传的一个新的头像地址吧。那么拷贝一下贴到咱们的一个浏览器，那么可以去看一下它的一个效果，回收一下，OK，还是这张图片，那么当然我们可以选择的再去换一张，换一个 phase two，点击上传也可以，然后我们到数据库里面刷新一下，再把这个地址拷贝，然后贴到咱们的浏览器回车，OK，那么这样子的话我们就可以完成我们用户头像的一个上传，那么当然我们现在使用的方式是一个以 fast d f s 的一个形式去实现的我们的一个文件服务器。那么到这里的话，这一块内容，那么我们就已经是 OK 了。

