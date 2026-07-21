---
title: 3-1 FastDFS整合SpringBoot - 实现service
---

# 3-1 FastDFS整合SpringBoot - 实现service

[image](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/cf1687fc-057e-44b5-a3f4-840a29a5639e/SCR-20240806-jvnw.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WNIR6RTN%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T225223Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIB%2BoGg5%2Fx8rIC4jraDE2ljAy77GXfIU2zCQGcVH6Qb8EAiB8qvP0jes3NnWnApnYArjlBdlm37WYnBBK0vO44CHJMSqIBAjG%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIM3bqDO44sBGjSbumvKtwDhwX3XCZo0PoSaZfigRSZJIfDv%2B0wVWMs7LmKMWifXiDbQcLbu%2FJrhNeg1%2ByVHN46X888RQkrPVyEBKxPZ4kmeI27GIuJro8X%2F%2B%2BCwJ6B0Zut5K82J1pkY%2BO8z%2FJJ0OMyHURWKXWbRTfvQZT1HZzbTXn%2BoSiQJVHh2hhYFteyHLBgp0XHIsLaAeaNBWYh9l4wuPEM9r0YMrnsOkZFVEZVusoLjb9p4%2BR48ctRYvpf0l9mNc2At1uE735YtKWhoesawUwebw6d1QmwuKmFDQBlaZuMzVRIUeNRzwLVXsjjEpUf3nbKCzvIA%2F4Qus8XJDkwnN8a8GfhmrqnxGPkh0%2FnanNKvzotsclrGFsKOqDp2RrggncSGMWDzVEolPD97TgxVAEGdgkAgwoglBv2S29nTGDo3A%2FQ62eJYaYYXH6sngUCxVQyZqelkayVA7eafemAWw8N3Keg8Eg7Lzu9KlFnBmT%2BYZoL9hnJ%2B9ub36ZahXw%2BZtjL3OuiM66Q7c%2FJR5NkVBjqp%2FVu0l2QlpCeI8fBkOZD1i3tRQUrOYv4AiRbYAewcgo27dBZc0FjnNEmW5MJ1%2BWa7M%2B466zwaTuU8YO35SfN%2FKh92W0KRQ9qCbX9x02ZTdi9v2Fg4y6HbQcwwLn%2F0gY6pgGM45wLeZ%2B2uzXPqQ9LxbDbsAq8KDzrWYXSVvMy5KA%2BoLQ1Cs47LCRytBpr0MWzfZD5xKjDhhkv339PzxF4RLtcahRdYSEF0xPmklfaWSsE5ApFBLRvycRPjqutwTXP8BuybaU3Y4NkNXO7WWVkvu5HEjJgSfG6oXQLjYJbzt9qr3Y%2Fc%2FYqYfFd9qyLJhTlLEqmVQsbdwb9ysPnOniMt1cocTAcy7SA&X-Amz-Signature=85e5f8ccf92bbb1ad1434d3833eff8de479eaad2aabb88295fab00537fdf6c84&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

那么上一节我们是通过结合了engines，目前的话我们使两者进行了一个结合，使得我们现在已经是可以来使用浏览器来访问我们具体的一个文件服务，那么现在其实我们所搭建的一个文件服务器就已经是 OK 了。


接下来我们所要去做的就应该要去把我们原先我们再进行一个用户头像上传的地方给替换掉，使用我们现在的一种新的方式去做，也就是我们要把 fast DFS 整合到咱们的一个项目里面去，那么打开我们的这个开发工具来看一下。

[image](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/51ce53e5-b66b-480d-b748-58d05a688d27/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WNIR6RTN%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T225223Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIB%2BoGg5%2Fx8rIC4jraDE2ljAy77GXfIU2zCQGcVH6Qb8EAiB8qvP0jes3NnWnApnYArjlBdlm37WYnBBK0vO44CHJMSqIBAjG%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIM3bqDO44sBGjSbumvKtwDhwX3XCZo0PoSaZfigRSZJIfDv%2B0wVWMs7LmKMWifXiDbQcLbu%2FJrhNeg1%2ByVHN46X888RQkrPVyEBKxPZ4kmeI27GIuJro8X%2F%2B%2BCwJ6B0Zut5K82J1pkY%2BO8z%2FJJ0OMyHURWKXWbRTfvQZT1HZzbTXn%2BoSiQJVHh2hhYFteyHLBgp0XHIsLaAeaNBWYh9l4wuPEM9r0YMrnsOkZFVEZVusoLjb9p4%2BR48ctRYvpf0l9mNc2At1uE735YtKWhoesawUwebw6d1QmwuKmFDQBlaZuMzVRIUeNRzwLVXsjjEpUf3nbKCzvIA%2F4Qus8XJDkwnN8a8GfhmrqnxGPkh0%2FnanNKvzotsclrGFsKOqDp2RrggncSGMWDzVEolPD97TgxVAEGdgkAgwoglBv2S29nTGDo3A%2FQ62eJYaYYXH6sngUCxVQyZqelkayVA7eafemAWw8N3Keg8Eg7Lzu9KlFnBmT%2BYZoL9hnJ%2B9ub36ZahXw%2BZtjL3OuiM66Q7c%2FJR5NkVBjqp%2FVu0l2QlpCeI8fBkOZD1i3tRQUrOYv4AiRbYAewcgo27dBZc0FjnNEmW5MJ1%2BWa7M%2B466zwaTuU8YO35SfN%2FKh92W0KRQ9qCbX9x02ZTdi9v2Fg4y6HbQcwwLn%2F0gY6pgGM45wLeZ%2B2uzXPqQ9LxbDbsAq8KDzrWYXSVvMy5KA%2BoLQ1Cs47LCRytBpr0MWzfZD5xKjDhhkv339PzxF4RLtcahRdYSEF0xPmklfaWSsE5ApFBLRvycRPjqutwTXP8BuybaU3Y4NkNXO7WWVkvu5HEjJgSfG6oXQLjYJbzt9qr3Y%2Fc%2FYqYfFd9qyLJhTlLEqmVQsbdwb9ysPnOniMt1cocTAcy7SA&X-Amz-Signature=2e002ff42a8036aa6b67ed4986a91f39079133ac402fc41ff86196f2a050f05b&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

目前我已经是新创建了一个项目，也是在我们当前这个项目里面的一个子工程，那么在这个工程里面的话，我目前也已经是创建了一些基本的一个文件的一个结构，那么这个是 com 点 i mock，对吧？这是启动类，以及是这个是跨域的。另外我们的 yaml 文件以及是这个 log for j，此外还要是一个 palm 文件，那么分别我们来看一下。


先来看这个 palm 文件，那么在 palm 文件里面的话，那么我们在这里边主要是引入了两个依赖，其中一个依赖我们会依赖一个service，因为我们的一个文件上传，上传完毕之后我们是需要去更新到咱们的数据库里面去。那么还有一个就是我们的一个 fast DFS client，这个的话你也是可以通过咱们的这个结合我们的一个眉文库去做一个查找，这个是可以去搜的，就是 fast d f s client，然后拿到以后那么直接可以去拷贝，这个是目前最新的一个依赖的版本。


OK，拷贝过来，然后去做一个下载，那么就是 POM 文件，另外在我们的 yaml 文件里面，那么这个我们就不去多说了，也是和我们之前的也是差不多的。OK，那么在这里面我们是需要去做一个配置的地方，那么就是针对于 fast d f s，我们来写一下，就是 f d f s 的配置，那么它的一个前缀就叫做 f d f s。


点我们来看一下，首先我们来敲一个，有一个叫做 time out，那么这个，那么这个格式化有点小问题，我们把它给贴到下面啊。这个意思其实是它的一个连接的超时间，我们去设计一下，设置为30，那么随后我们后面加一个注释，就是连接的超时间。此外它还有一个叫做读取时间搜 time out，那么我们也去设计一下，这是读取的超时间。


此外还有一个最重要的就是 check list，那么这个的话就是我们的 check 服务所在的一个地址，在你这里我们要去写的话，直接去写上它的一个IP，外加它的一个端口号就可以了。192.168.1.155，这是我们的一个地址吧。另外 IP 不要忘记好，OK。加上注释。


Tracker 服务所在的 IP 地址和端口号，那么这样子的话，我们的 fast d f s 的一个基本配置在这里我们就已经是配置好了，配置好了以后，那么接下来我们所需要去做的就应该要去做一个上传的这个动作，这个操作的话我们会放到 service 里面去做一个相应的构建，我们把这个打开一下，我们创建一个新的package，举一个名字叫做service。好，然后我们在这里边去创建一个新的一个接口，取个名字，这边我们就叫作为faster，叫 f d f s service。好，OK，在这里面我们去创建一个方法，我们返回的话是一个pass，所以我们这样子写一个 string 作为返回，名字叫做upload。然后参数我们先不写，另外的话我们先使用一个 exception 好，OK，然后我们再去创建它的实现。先把这个包给构建，然后再去构建一个新的类。把这个拷贝一下，然后我们再去创建。我们这样子，我们稍微放大一下这个字体，好，OK，然后在这里面我们就要去做一个实现。


control 加 enter overwriter，把 upload 给加进来，在这里面我们就要去写咱们的一个业务，那么我们要去实现咱们的一个文件上传的话，那么在这个地方其实我们就会使用到它的一个客户端，那么这个客户端的话叫做 fast file storage client，这是针对 storage 的，OK，因为我们的文件都是存储在 storage 这个节点，存储到我们的一个 storage 服务之上的，所以我们把它给注进来。好，OK，然后不要忘记我们加上一个service，OK，那么这样子的话我们就可以使用这个客户端了。


然后这个客户端的话我们来看一下，点有一个 upload file，第一个，然后在这里面会涉及到一些相应的参数，我们点进去看一下啊。那么首先第一个参数是 input stream，那么这个的话我们是可以通过 multipot file 去获取的。然后下一个是 file size，这个我们也可以通过它的 file 去获得。另外在后面它有一个 file exname，那么这是它的一个后缀的话，我们是可以通过咱们获取到 original file name，获得它的一个原文件的名称之后，然后再去获得它的一个后缀，再传入进来也可以，那么随后还有是一个set，就是它的一个 Meta data。


那么这个东西你不传也可以，你可以设置为空，因为在这个地方可以看到它的一个源码里面会做一个判断，如果说这个为空的话，那么它的一个 fast file 在这边，他就不会把这个 Meta data 给放进去。OK，所以我们直接可以传一个空，那么也是可以的。那么在这里的话，我们就可以去把这个 upload 里面去放入相应的参数，那么第一个是一个 Multi part file 把它给传入进来，随后第二个是它的一个后缀，对吧？那么后缀的话我们使用这个名称一样的 file e x t name。好，然后我们这样子，第一个是file，点 get input stream，这是第一个参数，第二个参数是 file 点 get size 获得它的大小。第三个参数就是把这个后缀名给放进来，那么最后一个直接放一个now，那么这样子就OK，那么这样子的话其实就会去做一个上传的动作，然后我们的参数到 gecko 里面去放一下。


好，然后当我们上传在这边上传成功之后，他会拿到一个叫做 store pass，我们可以去获取一下。那么这个也就是从它的这个 storage 里面获取的，随后我们就可以通过这个 pass 去获得相应的内容，我们来看一下它有哪些内容。那么第一个点它有一个 get for pass，那么它是一个完整的一个路径，是包含了 group 和它的文件名。如果说你不想要的话，可以使用下面两个，一个是单独获得group，另外一个是可以获得它的一个pass，都可以，那么在这里的话我们使用这个 get for pass，然后定一下 string pass，这样子的话我们就能够获得这个上传之后的一个路径，然后我们再 return 返回到咱们的 controller 里面去就可以了。OK，那么这一块就是我们上传的一块业务。

