---
title: 3-8 优化Swagger2显示
---

# 3-8 优化Swagger2显示

[image](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/0d3d59a5-b039-4267-bbf9-309a666af8e9/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WUXHESQT%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T224627Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDlZtd0YiergKR27Dp0J1DGNi3akb%2F6SwnhSTavAuflLwIhAIVFezG4gouaKY5BSmzR1U2Skf1xG25XA99cnwOl9oTdKogECMb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgxsN1nvNU%2Fgpcdv7tsq3AOHoJJduNgCUIBa91pXbV13aIH4nCFq%2FwJY%2B7fB%2FYc7LdCozMI8Q2M2TX4zAhwc0ETfXKLfd%2FwkX2bkzMFFalfYz%2F9FhooJ%2FR%2FuwMYZyRBFNZizukXexqMAYW%2BBqjd25bECPG2gtRow5CHX7tKYGMoYOzO7YAxxhYTxDqPdxtxXdF06w0X%2BVmUR%2Bj8k%2BNpUUI1u0b6SmKQfbGGLBnSuMxUx1tJVxhmL9t%2BTtPZFlkJgzdgFVQt8IxLbgguVU%2BiDUPk8NyqudIIVfHGugEaER0gYqdzU%2FA%2FhQNwF59Ygm6zkwYItbVS4SAOAsPcMByU84doVE67msDfK%2BGtYXPfeoVxKC9ZteFR%2BqY9xVQGNbdSjWU3HRVi176GIv2eiZEporQ2g7DjOAM5qyj0jHF7XT2on%2FKYB56TrZON8EGnAzcZaasVxp6MeIoTxf0mqRqJsOXvwQskQw7ttZvprtNJLF7gYlyNXoDJeDwywqslyGQ%2F2Vy9wLYiYWBf7htl22PzNMB5TN5YaMqrxWVx6%2FaS4X9luet4yGqJllcEObHSpYuY6OyhXcOgwjO4ypxw4ASLVK3jrAhphQzXBYvHZdpjOIhpKbLJCcZ4Rg5iB76nTs1CkVvam2w3oxCekryoxjjDht%2F%2FSBjqkAbs5hv3swctNyhY54NG%2FWyTDBnxuej%2Fs0bZJ5kfRJWQECBwZOVYuTTgEE7DSjquiQFIVVAlmm3KxMJrESOJA%2Fc3z6xBwe966qg6DHEfu4hGeUkcPw%2BKRgnRlVlQVDV7NvxGVg6t6D7rGlPNFH82KkielRVEzK%2BRKokWxpr7sa5S0JIbW7KEZPKDqjpdSrExO84a6Ng00gm7N13DMXnhP%2Bdr2Kkin&X-Amz-Signature=f3006cb74fa07dea78c95be5c5ef515373c2fd6c1d488236476e669dad098c52&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

现在我们就已经整合完毕 Swagger2 文档 API 了，接下来我们来看一下我们能不能针对文档 API 做一些相应的优化。比方我们来看一下在它的一个左侧，其实左侧的这些内容，如果和如果是你正在和其他人员做对接，或者和第三方的一些公司在做对接，对接人看到你写的这些英文的名称，可能会封掉对吧，因为我们毕竟要看的是中文对吧。如果这些内容是以一个中文的形式存在，这个是最好不过了。其实这些我们都是可以针对每一个不同的 Ctrl 的去做配置的。另外像有一些像比方 hello control 了，这是我们去做测试的。当然也有可能像是一些可能比较隐私性的，比较密性的一些 control 了，我们是需要去隐藏掉的。这些其实我们都是可以去做配置的。好，我们回到咱们的代码，可以来看一下。比方我们可以先打开 hello control 了， hello control 了。还有是我们之前用做测试的s，t， u 这两个 Ctrl 了，假设我现在不想给其他人看到怎么办？能不能忽略？很明显是可以的，在只要在它 Ctrl 了的上方，我们可以去加上一个at，有一个 API ignore 看一下。 ignore 其实就是忽略的意思。


使用了注解了以后，在我们当前这个方法里面，应该说是当前类里面所有的方法，当前 controller 是绝对不会显示的。OK，我们把复制一下放到 hello 里面，重启以后我们刷新一下页面，我们去看一下 hello 和 Stu 会不会再存在了。好，现在是启动成功，刷新一下咱们的页面。刷新你会看到就只剩下一个了，另外两个就不再会被显示了。


这个是一个非常好用的功能， API 的一个 ignore 忽略好。随后我们针对passport，也就是我们用户注册登录的 control 了，我们去做一定的修改和编辑。我们打开 Ctrl 了，在它的上方我们是需要去加上 API ignore 吗？很明显是不需要。


现在我们所需要去加载，应该要是针对我们当前这一份文档，当前的接口做的一定的文字性的解释。比方我们可以在它的头部 class 的上方加上一个 a p i，这个 a p i 就代表我们是可以在这里面去输入一些相应的内容的。我们其实可以展开，可以发现它是一个接口，它是一个interface。我们来看一下它有 value 以及是tags。 tags 它是一个数组。在这里我们先带着大家来写一下。先写一个 value 等于什么？我们直接在这边写注册登录，后方我们去加上一个tags。在这个里面我们只需要去写上一个，其实就相当于是一个解释。这个是 text 用于注册登录的相关接口。我们先这么写，写好之后我们来再来重启一下。好，重启成功。随后我们来刷新。这个时候刷新了以后，你会发现当前这样的一个接口就不再是一个英文了，它显示的就是一个用于注册登录的相关接口了。这个是我们编写在 text 里面。对其实 OK 好展开以后展开，展开了以后它里面的方法。这里面的方法要比外面可能看上去更加的让人抓狂了。因为在这里面可能就是一个一个的路由的地址了。路由的地址直接去这么看实在是让人有点摸不着头脑。所以我们也是可以通过类似的方式去进行一个修改的。怎么去修改，我们可以找到比方，我们可以先修改一下 your name is exist。在它的方法名的上方我们也是可以去加的，比方可以加上一个API，它有一个注解叫做 a p i operation。


看一下person，其实就是用于去阐述我们当前所需要提供的方法的一个详细的含义。在它的里面也包含了一些内容。首先一个有一个value，另外它还有一个是notes，这个就是我们所需要训的。当然在当前的方法里面是包含了很多的内容的。比方还会有一个method，有一个 h t t p。method，这个是用于去指明我们的一个请求。方式是什么，比方 get 还是 post 都可以去进行指明的。但是需要去注意，你要指明必须里面的方法名是大写的，不能写小写。OK，所以我们在这里面也是可以去写一下的。咱们先来写一个value，写上一个用户名是否存在。后面还会有一个notes， notes 保持和斐乐一样贴过来。


还有一个是 h t d p master 的，写一下。由于我们现在使用的是 get mopping，所以我们在这里要保持一致，使用 get get 大写就可以了。相应的我们把当前的这一行代码我们拷贝放到下方，这个是用于去做注册的，所以我们在写一下用户注册，在这个地方我们也写好用户注册。只不过在这个地方你是需要改为post，因为你是需要和前面 post mapping 要一一对应的。OK，现在我们写完了以后，我们就可以来做一个相应的测试了。重新启动一下。好，启动成功以后我们再一次刷新，我们把展开。这个时候你会发现之前我们在这个下方其实显示的并不是中文，对吧？现在很明显我们就可以从导航的一个展开，我们就可以看到对接人员想要什么，直接看中文就可以了，这样子会更加的人性化。这也是一种人性化的设计，像要去找到用户注册用户名是否存在，直接一个去这样子去看就可以了。


另外在我们展开文档以后，相应的接口名称，接口说明，其实在这边也都会有接口，用户名是否存在，还有实际的说明也都会有。另外它还会有一个请求方式是get，这里也是我们去进行编写的。当然我们的一个请求传输的方式，我们的数据格式，也就是 consumers 都是 JS 格式，这一点需要去注意一下就 OK 了。


好，随后除了这个以外，其实我们还有一点我们也能去进行优化的。优化的地方在用户注册里面会有一个请求参数。前面我们第一个接口请求参数其实比较简单，就是一个 user name，在这里有一个 user Bo，这个 user Bo 其实我们也能够对它做一定的优化，可以让它显示的更加好。因为像这里面 confirm password your name，可能一开始这样子提供的时候，让其他的对接人看上去会有点不太的友好。如果你能够加入一些相应的中文，那就更好了。对像比方说明一看是 user Bo，可能会让人觉得什么是 user Bo 对吧？所以我们能够去写一下。回到代码找到 user Bo 其实也是一样，我们在它的上方加上一个API，它有一个注解叫做model。看到它有一个model，还有是一个 model pop。 POP 是一个属性，我们使用 model 就可以了。在它的里面我们可以去看一下，点进去它也会有一个failure，还有是一个description。这两个也是主要我们所需要去写的。我们回过头来写一下。先写一个value，这个 value 是什么？其实就是一个用户对象， b o，或者是一个业务型的对象。随后在后方我们可以去加上一个 disk p，详细的内容可以写一下。这个是指从客户端，由用户传入的数据封装在此 entity 中。这样子就比较的一目了然了。


随后针对于我们这些属性，也是可以去加的，写上一个 a p i model，它是一个 property 属性，进去可以也是一样，进到它源码里面去看一下，这个时候它的源码里面会有一个value，这个 value 就是它的一个阐述。另外还有是一个name，这个 name 其实和我们的属性名属性的名称一模一样就可以了。当然你也可以去重写，可以看到吧，它是允许我们自由的，自定义的去重写这个名称的。这个名称其实也就是和我们叫 user name，这个名字是一模一样，是需要一一对应的。另外它还会有一些像，比方看一下它还会有一个example， example 是一个示例，你可以去写一个，随意的去写一个值，让其他的人去看。


还有一个是required，看一下， required 是指我们当前的一个属性是否是必填的。如果你设置的是true，其实我们的文档它也能够间接的为我们提供一个判断，这也是非常不错的。所以我们在这里面可以去进行相应的编写。我们先写一个value，这个 value 是针对于 user name 的一个阐述，它就是用户名。随后下一个我们来写一个name，这个 name 其实我们只要把复制过来就可以了。当然你也可以随便去写一个名字也可以，但是我们要和保持一致就可以了。


写一个example， example 默认为空，我们可以写一个，比方我们就写一个 m k，再来一个request，很明显，我们要去执行用户注册的时候，这个是一个必填项对吧？所以你可以在这里面加上一个true，可以这样子去写。随后下一个用户名和下面一个是密码，我们直接把复制过来。以后我们再去做一个相应的编写。其实也是可以的。快速的拷贝一下。他说的确认密码都写一下。确认密码，这个是密码，然后example，比方123456，下方我们就写一个，也要一样123456， request 可以保持 true 就可以了。


好，随后我们就可以来进行一个运行。我们修改了 b o， b o 是在 Polo 的子工程，所以我们要进行一个install。安装。好。安装成功以后，我们再去重新的启动一下项目，重新的去运行。好，运行成功，我们来刷新一下。好，刷新，点击register。


这个时候我们再来看的时候，你会发现这里面相应的内容其实全部都把我们写进去了。比方 user bo，它是干嘛的？它是一个用户对象的b、o。另外下方像 confirm password， user name，它们都是什么意思？也帮我们在这边编辑好了。只不过它的一个排序方式是不一样。它的排序方式是根据首字母c、p、 u 进行一个排序的。对于我们自己来讲，我们在代码里面它的一个顺序是不一样的，但我们代码里是这样子的对吧？但是也没有关系，根据它的一个字母排序去看这种文档，提供给其他人员去调用也是没有问题的。



以下是 `3-8 优化Swagger2显示` 的提纲：

- Swagger2显示优化
