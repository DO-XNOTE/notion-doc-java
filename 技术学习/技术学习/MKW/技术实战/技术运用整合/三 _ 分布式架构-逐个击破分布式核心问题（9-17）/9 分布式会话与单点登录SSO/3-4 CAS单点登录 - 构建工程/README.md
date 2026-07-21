---
title: 3-4 CAS单点登录 - 构建工程
---

# 3-4 CAS单点登录 - 构建工程

[image](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/773d6473-f782-4144-8458-3069bccb8692/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XG6WBPFW%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T225112Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDPK0QgRMBweASgeJ9zBFazbWtPbuUcb85FPW%2FawS9PUwIgDDOqY8YjAEp7iDDV6mvR2wXL92rxLXs8dvnCVhvPFyIqiAQIxv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDE%2F9zDIpxuKWT2eZ7yrcA1SAO0HkH8Ugkb%2BtaBSx%2FpYTprnPA44rRUvND6CD2ruzNa9Gbjs%2BcjPff%2ByHAOZSQcn8efqiFg8%2Bd3r25I8VgMgcxFUUGvVZnegGmHVEO4uT4DUZDiZ6xYjUlkjcH9xeEUdDZr%2BP%2B%2FG976bM%2FzU8RrhfTUbZ0npRm8f2i8cIMDng6OSDluWX8TXpuFGB5uiCi0cOd0JJoR5xCoGkSs2f9HVEB9uHRKuxzS6Zjw%2BJjZJa6pN7EvdAUGdtvgmXFbwHJfHmWD31vzlkRxfSJQixM7uQSU3tWV51JJzlGEZHPcC6ZsWNLO7uw%2FA02PKRySyqWVvX2ijNTFKrm9lPkqu7xjPIktEFh2%2B6bQnsj98R%2FrVg%2F9yD2dgRHWXod9J3n1MB0nh5i0%2BVb4XkHDU2zyVdz5BeTjNQ3hG%2Fl5pvibH2%2BlWELRsNnizWo7CDcaFH41oXsCZV9V0tNX4innVfzLrLbxg863T6JJ%2FYPoOtwvA4HUTz0oIkSsRZ%2BVwzhj7efkoOweGXHJOHsN5x%2BE2vv5WgHdnNBXhVZlPRAhDJF0NndfbLXutoBxwV9DZt5rCIxxtDTo2qyhqTVdIp%2BjT2KzXc2nPeS8a5TxIAdqlQSlE9wXkESrjFx2Rd%2FWIbzx%2BjMJm6%2F9IGOqUBfwiLKRdxh%2BhHDm%2FXbT9Z7goJm3vdOIgVH%2FnRvjCgE1tcMtZkNKSfThxN4OWKyOfyAPkYia%2FQ%2FGLUlwRRKL4OacrHjLCRM3EzJlpNfiEtTtbKa29RvjMubf1pusTyVvmqnKaQxJ4ajITdd05rZf8SjXvkwEX2qb3%2BbmY42lW3ReJ5sO1QAvvbGrt%2F5aTeXHCUFrEmZTJyTx9QGqrM0m%2FO70%2FGJEQq&X-Amz-Signature=ba7dbe727ff91cc7e6affed3d02a7eba304228799cc5ea0a242a6ad4d2ad3e3b&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

[image](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/e258ffd9-9431-416d-aa65-82b1fdf91c7e/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XG6WBPFW%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T225112Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDPK0QgRMBweASgeJ9zBFazbWtPbuUcb85FPW%2FawS9PUwIgDDOqY8YjAEp7iDDV6mvR2wXL92rxLXs8dvnCVhvPFyIqiAQIxv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDE%2F9zDIpxuKWT2eZ7yrcA1SAO0HkH8Ugkb%2BtaBSx%2FpYTprnPA44rRUvND6CD2ruzNa9Gbjs%2BcjPff%2ByHAOZSQcn8efqiFg8%2Bd3r25I8VgMgcxFUUGvVZnegGmHVEO4uT4DUZDiZ6xYjUlkjcH9xeEUdDZr%2BP%2B%2FG976bM%2FzU8RrhfTUbZ0npRm8f2i8cIMDng6OSDluWX8TXpuFGB5uiCi0cOd0JJoR5xCoGkSs2f9HVEB9uHRKuxzS6Zjw%2BJjZJa6pN7EvdAUGdtvgmXFbwHJfHmWD31vzlkRxfSJQixM7uQSU3tWV51JJzlGEZHPcC6ZsWNLO7uw%2FA02PKRySyqWVvX2ijNTFKrm9lPkqu7xjPIktEFh2%2B6bQnsj98R%2FrVg%2F9yD2dgRHWXod9J3n1MB0nh5i0%2BVb4XkHDU2zyVdz5BeTjNQ3hG%2Fl5pvibH2%2BlWELRsNnizWo7CDcaFH41oXsCZV9V0tNX4innVfzLrLbxg863T6JJ%2FYPoOtwvA4HUTz0oIkSsRZ%2BVwzhj7efkoOweGXHJOHsN5x%2BE2vv5WgHdnNBXhVZlPRAhDJF0NndfbLXutoBxwV9DZt5rCIxxtDTo2qyhqTVdIp%2BjT2KzXc2nPeS8a5TxIAdqlQSlE9wXkESrjFx2Rd%2FWIbzx%2BjMJm6%2F9IGOqUBfwiLKRdxh%2BhHDm%2FXbT9Z7goJm3vdOIgVH%2FnRvjCgE1tcMtZkNKSfThxN4OWKyOfyAPkYia%2FQ%2FGLUlwRRKL4OacrHjLCRM3EzJlpNfiEtTtbKa29RvjMubf1pusTyVvmqnKaQxJ4ajITdd05rZf8SjXvkwEX2qb3%2BbmY42lW3ReJ5sO1QAvvbGrt%2F5aTeXHCUFrEmZTJyTx9QGqrM0m%2FO70%2FGJEQq&X-Amz-Signature=e529406f9b40e59db170b0178ad75eca24b4f36332c31fa64c49494381c6ecb3&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

接下来我们就来根据咱们这一张时序图去构建一下咱们的一个系统，那么在这边主要是涉及到三块，那么第一块是MTV，第二块music，那么这两个其实都是前端的一个项目，最后就是咱们的一个 CAS 这样的一个系统。这个是一个后端的项目，我们是把它会整合到我们的项目里面去，把它作为我们的一个module，也就是其中的一个模块。


那么对于 MTV 和 music 来讲的话，那么在这里其实我们本身就是前后端分离，所以我们在这边其实是提供了两个工程，这两个工程也会提供给大家，一个是MTV，一个是music，那么这两个其实全部都是放在了 webapps 之下，和我们之前的 center 和 shop 都在同级目录。然后你只需要去运行一下就可以了，我们就可以去做一个对应的访问。


那么这个看一下，如果说你去访问的话，如果说一开始是未登录，那么就是欢迎陌生人，请登录。我们把这个前端的源码打开看一下，那么这是  mtv  的一个工程，在这里是未登录的情况下，在这里它会有一个判断， user login 。如果说他没有登录，那么就是欢迎陌生人。如果说是登录的情况下，就会把登录的一个人的姓名在这里做一个展示。当然他也可以去做一个退出。这一块的代码和我们在 music 里面其实是一模一样的，这一块都是一模一样。随后往下面看，这是一个created，也就是我们一开始记录，然后做一个初始化的过程，那么首先会进行一个判断，他要判断一下我们当前这个用户他有没有登录过。


如果说用户没有登录，然后这边还会有一个ticket，那么这是临时 ticket 的一个校验。如果说他也没有的话，那么其实在这里他会做一个相应的获取，就是说他要从我们的这个 s o，也就是  CAS  系统里面去验证一下。如果说我们这个 ticket 有的话，你要去做一个验证，如果说验证成功，那么我们就可以代表我们当前的用户是可以登录，它可以获得用户相应的一些信息。这一块我们先不管，我们先看下面这一块，如果说我们没有登录，用户未登录，并且他也没有验证，或者说是也没有这样的一个 ticket 的话，其实他就要去做一个跳转。


这里我是暂时先是注释掉了，因为如果说我开放的话，当我们在进入当前页面的话，会直接发生一个跳转，这个页面就看不到了，所以我们是暂时先注释掉的。在这里的话可以看到它其实是做了一个拼接的跳转，那么最终的一个地址其实就是在这里，它其实会跳转到我们的一个 log in 的页面。这个页面是什么呢？这个其实就是我们的  sso， CAS 这个系统的一个登录页，它会去做相应的校验和判断的。后面这个也称于y，就是你所携带的一个回跳地址，这个回跳地址其实就是在我们实施图里面的这一步，就是说携带 return u， l 跳转到 CAS 也就是第三步。那么第二步的话其实就是验证是否登录，这个过程其实就是在这里判断 is the win。OK，好，那么这个其实就是我们的一个前端的两个页面，前端的一个 MTV 和一个music，随后就可以到我们的后端去构建一下咱们的这个项目了。在后端我们其实也是一样，在这里的话右键新建一个子模块，然后在这里面的话直接可以点这个下一步就可以了。


在这边取一个名字，可以取名为  sso，或者你也可以取名为 CAS 其实都可以，那么我们在这里取名为 sso 就可以了。然后点击下一步，finish。随后这样的一个工程就已经是创建了。创建之后那么肯定我们是需要去做一些相应的构建，其实它本身对于我们来讲的话，它其实也是一个  spring  boot 工程，所以我们只需要去把里面的一些相应的依赖给拷贝进来就可以了。那么这个依赖我们从之前的 API 工程从这个里面去拷贝就行了，因为它里面包含了一些对应的依赖。在这里面找一下，我们把这个下方这些 dependence 全部都拷贝贴过来，然后这些没用的注释我们可以去删掉。


好，OK，那么这样子的话总共就是包含了这些内容，这个的话我们就不需要这个test，我们不需要直接给移除。这样子其实在我们当前这个 sso 工程里面，就是依赖了一个 service 工程，依赖 service 工程了以后，接下来的话我们就可以去它其实就是 Skyboot 的一个工程了。


然后的话我们再来就是说我们还是需要有一些其他的内容，我们也是需要去构建的。比方说我们得要把这个  imooc 这个application，也就是它的一个启动类，你得去构建一下，所以在这里面我们同样有事要去构建一下。创建一个包， come 点imock，把这个 application 给贴过来。好，贴过来以后我们去构建一个controller，这个包是需要去构建的， Ctrl 里面我们拷贝一个，把之前的 hello 给贴过来，然后把名字给改掉，改成 sso control 了。然后这里面有一些内容我们给我给去掉。在这里我们使用 Ctrl 了，我们不使用 rest Ctrl 了，因为我们在这里面会包含一个页面的，把其他的一些内容全部都清掉。在这里为了测试方便，我们就暂时先这样子。我们先要保证咱们的这个工程可以去运行，就说先把工程给初始化，初始化以后再去把我们的业务给停进去，这个就是我们的一个最基本的步骤。


随后我们再来把咱们的这个 resources 给构建一下，到这里面去找一下，有application，另外还有是一个 d b 拷贝一下，另外还包含了我们的 logo4j 的一个  properties  这样的属性文件，全部都给贴过来。好，贴过来以后，那么首先我们先把这个端口改一下，这个端口我们使用8090，在这个里面，在 dev 里面去做一个修改。 8090 然后下方的一些数据库的内容，这个数据库我们不需要去改变，还是连当前我们这个库，然后 Redis 我们是使用单支单实例的方式去做，然后这个是 my Redis，这些我们保持不变就可以了。那么对于我们原先这样的一个y，m， l 这样的文件来讲的话，其实这里面的一部分内容我们也不需要去做任何的修改，保持不变就可以了。


然后再来看一下我们的   log4j，在   log4j 里面其实可以不去做改变，但是在这边会有一个文件夹，你可以把它做一个修改，比方说把它改为 sso，这样子的话我们可以做一个区分也是可以的。好，那么这是我们基本的一些内容，然后我们还有一个 application 来看一下，那么在这里面我们先把一些没用的给声音删掉，那么在我们这里面的话，像这个是不需要开启定时任务，在我们钢琴 s o 里面是不包含的。除了这个以外的话，对于我们的一个包扫描，也就是在这一块这个我们可以保持不动。


另外这个是扫描我们的一个 mabetas 的文件，因为我们其实依赖了service，并且我们在当前这个  CAS 单点登录的工程里面，其实也包含了一个登录的操作，你是需要去进行一个和数据库的校验的，所以这个也是需要去保留，另外这是我们的一个标识，所以这个我们保持OK，保持这样子就可以了。


随后我们在这边测试一下，我们在这边启动一下，先保证我们这个项目启动起来。好，那么现在启动 OK 了，启动成功之后我们来测试一下，那么这个是我之前测试的一个网站，然后我把这个拷贝一下，直接贴过来，那么访问的时候那么只要  sso. com 8090 是我们的端口，再来一个 hello 回车。


那么这个时候没有显示任何的内容，咱们来看一下，那么这个其实主要是因为咱们的一个controller，在这边我们在设置的时候注解使用的是一个controller，我们之前是使用的是rest，所以说在这个地方它只是会把这个当做是一个页面去作为一个查找，所以你应该要在这里再去加上一个 response body，那么这样子衬出去的内容它就会作为是一个 JSON 或者说是一个字符串给传出去。随后你在页面上再去做一个刷新就可以了。当然我们在这里是需要去做一个重启的。


好， OK 啊，刷新一下我们的页面， hello world 就已经是出来了。这样子的话，其实对于我们一开始前期要做的一个准备工作，这三个系统现在都已经是 OK 了。第一步出自访问到我们的一个验证登录以及携带跳转，那么这个部分其实都是由咱们的前端来做控制的。接下来我们其实要做的就是在 CAS 系统里面的第一步，后续就是要去做一些其他的验证工作了。



