---
title: 2-1 上传头像 - 定义文件保存位置
---

# 2-1 上传头像 - 定义文件保存位置

[image](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/d2727cf1-3c7e-48d2-99bc-73977fd0dbb1/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46676GMERLV%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T224724Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCICRnSlfXCEbnH65oC9V6w4FWMcniefSaDnTo%2FtTgZFdQAiEA0L9XYyumZQVnHxmL%2B%2FYhepN2g91vY1CGnKCiWzgIc8kqiAQIxv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDA6iEiNknHCKbFl0xircA7MrbYLHyipp0jGGjPPzLyP6FqMPtsLl13%2FpQj9teUEF9ANt5BcYuLfkEOjo14Y1ZktFGnYIQV5BS4JCAYLrSRzo%2FXZoZ3fnB0k7F6YpAQArqr4d%2BOd%2B6YGAOcNQhLXdUcPofb%2BPcVTd7Mw3YynQs7gm%2BvW%2BUFByFuZudxQfTUujz4ed40JxlttL1UKGs1zTM6w%2BABVg5yWwKAp%2BaHp2voAFQCh6QodOWGAMcjRvELgX1Vz66gya76sL8lAU4jW%2BkPcAV%2Bdyvu8Jal0KGQ3AapVggmKApHk0HX2rQldtJMoLo2%2Bu%2Bg1ViiyRW%2BfAeOm8x2Nr%2BoZWZ%2BmM407nWgjktsChnXcdowaSkQvJh8Cxn4cPyCaRohe0GDkk2WDwMfAPwg7n37gC3LICagOpPYiC1YnwQntbO0xJHKqlmxwAemHcp66d0fxeHB5NhwFqBrP40PGbJsDoGCWM3%2FpI7eJlZ8lnH%2BmRG2eBBD9F4d51yMJ%2FJD3KOBAn6ygV8%2B%2BPbbI67zqvatBqvU53hqTdA%2B3%2F5zKbkWU4Yt3wfjQ0ARaYjSXiB9eEcGpqW%2Ff0%2FXNLCodJLldfizy3l4%2Fde8xwE1elT2Mf2OZ%2B4qZ3LzXYY9GRvs0yqZxgbqMMA7onW9cUMJy6%2F9IGOqUBzk4JLUriPvjN83wtxjl1DSyvKn4Jvw9mdnOphUmXmW965u7K4zxJfMLEbQed3l0MXcubVy9Y4XbjFUjII1%2BjTuGe%2BstqIO86UP%2BassR1ItCUjKbR%2B2tc9wUoNBm8kMHNCFzBZ0Ukh2fmNiSlWPmhLYZHNjAoEgRyzJ05O7ZJuRuTWKyvxClpHxRm2gvrpcijlg8Xhv5AK3Me592tEBpXEjqzxxtt&X-Amz-Signature=f09e65b2c741a5a311a3103a0696b3288c3189405e0a0602a448e225b395e29d&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

上节我们是完成了用户信息的修改，它本身在前端我们就包含了一些验证，这个是写在前端的。其实不仅是在前端要有这些验证，在我们的后端其实也应该有，但是我们后端暂时先没有写。如果按照之前在天天吃货门户端所对应的后台接口里面，我们可能会在这里把 Bo 里面一些属性参数都拿出来一个去做验证，做判断。如果判断某一个字段有错有问题，我们就可以 return 一个。


前面几节我们是完成了用户基本信息的一个修改，在这个页面其实还包含了一个用户头像的上传，在这里这个图片可以点击一下，点击一下以后就可以打开我们当前电脑的某一个文件夹，去选择某些图片去进行一个上传。在这里点击打开，这样子它其实就可以去做到一个上传的操作了。上传其实就是把我们当前电脑的某一个文件上传到服务器里面，这个过程是需要有相应的接口来完成的。


我们首先来看一下前端，这是前端的一个修改用户信息的页面，在这里面我们可以先搜一下，会有一个头像的，叫做 user face。就在这里来看一下，它是一个input，并且它的一个 type 类型就是file，它的 ID 是 user face。当我们的一个图片里面的内容发生了一个改变的时候，会触发一个 on change 事件。我们在这里面就可以来看一下。搜一下在这里有一个 upload face 这样的脚本代码，在这里其实就是用于去处理我们的一个文件上传的。既然我们是使用的 JS 去做上传，所以我们在这里使用的是异步的方式去进行上传的。


首先来看一下，我们会先获得一个文件，这个文件就是通过 user face 去获得的。拿到了以后，在这里我们还会构建一个 form data，这是创建一个 form 对象。创建了 form 对象了以后，在我们的 form 对象里面，我们就去放入一个 file f， f 就是一个文件的内容，把文件放到 form 里面去。随后在下方我们在做提交的时候就可以发起一个post。这样的异步请求form，我们会放到请求里面，携带到后端。这个是请求到后端的一个路由地址。在这里我们来注意一下，它会有一个 content type，这个是设置到 pedas 里面去的。在这里面其实就是内容的类型。我们使用的是 mount part form data。 form data 很明显就是我们在这里所构造的一个 form data 榜表单数据。另外前方是一个multpart，这个是代表我们要做文件上传。我们涉及到文件就必须要使用Multipass，其实是在我们很早以前。如果是写 j s p，我们在页面上我们会这么去写。我们会写一个 form 标签，在 form 里面我们会写一个有一个叫做 x type，在这里面可以看到它会有三种不同的类型。在这里我们会使用Multpass，这样子我们 form 表单在进行提交的时候，如果里面有文件，这个文件我们就可以在后端去进行提交了。其实它是这样的一个原理，好没用，我们就重视掉了。一旦我们的一个请求发送到后端，在这边会进行一个判断，判断我们的响应是不是OK。如果OK，没有问题，提示一下头像上传成功，并且当前页面重新再刷新一下，把新的图片去进行一个展示。


好。随后我们就要来开始编写一下我们后端的代码了。来写一下在后端代码。我们在这里就直接去写一下我们的 Ctrl 了就可以了。因为现在我们先来完成一个文件的上传，文件的一个头像要保存到数据库，我们后面再写进去。我们先来写一下，先拷贝一个方法，把这个方法拷贝一份，好备一份以后做一些修改。


首先 swag to 的接口名称修改一下，叫做用户头像修改，它的一个方式，在这里应该是 post map 码，之前我们应该是写错了吧。 post 下方在这里在做用户信息修改的时候怎么写错了，应该是 post 好，我们在再来做一些修改。前端所传递过来会有一个 user ID，这个 user ID 我们放置就可以了，因为肯定是需要去接收的。


随后下一个就是我们的一个文件文件，我们先把这些内容先删掉。文件其实我们也说了，它是一个 multi part，所以在我们后端其实我们会有一个类型，叫做 multi part file。可以看到这个文件是在 spring frame work 里面，是在 spring 里面的一个文件类型。好在这边我们可以来一个 file 定一下，这样子这个文件其实我们就可以以一个参数的形式去进行接收了。好，同样我们在这边也写一下，把接口文档参数写一下，这是一个file。这个 file 是什么意思？是一个用户头像有块的，肯定是要一填。下面两个是一个 request 和response，这个我们就直接放就好了，随后下面的这部分内容我们就全部都删掉。


好，随后我们可以在这里去定一下。定一个，头像保存的地址。虽然我们现在写的是当前电脑的一个位置，但是其实我们在发布了以后，其实具体是保存到服务器的某个特定的位置，写一下它具体的位置，我们这样子我们可以记性一下。贝斯很错了。写到这里面去写某一个特定的例子。用户上传头像的地址应该其实准确一些，叫做位置定。 public static final string 取一个名字，叫做 image user face，再加一个location，在于某一个特定的地址，把转换为大写。这个地址我们怎么去写？打开我的电脑来看一下，在这里我会保存到 work space，再找到有一个image，这个是我预先创建的。再到foodie，再到faces。我会保存到文件夹里面去。会保存到这里面。我来把地址拷贝一下。好，拷贝了以后我在这里贴过来。就可以看到它的一个文件路径是一个斜杠来进行一个分割的。

[image](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/d37a8ce9-23a3-4fa1-aaeb-3ae6d642308b/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46676GMERLV%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T224724Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCICRnSlfXCEbnH65oC9V6w4FWMcniefSaDnTo%2FtTgZFdQAiEA0L9XYyumZQVnHxmL%2B%2FYhepN2g91vY1CGnKCiWzgIc8kqiAQIxv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDA6iEiNknHCKbFl0xircA7MrbYLHyipp0jGGjPPzLyP6FqMPtsLl13%2FpQj9teUEF9ANt5BcYuLfkEOjo14Y1ZktFGnYIQV5BS4JCAYLrSRzo%2FXZoZ3fnB0k7F6YpAQArqr4d%2BOd%2B6YGAOcNQhLXdUcPofb%2BPcVTd7Mw3YynQs7gm%2BvW%2BUFByFuZudxQfTUujz4ed40JxlttL1UKGs1zTM6w%2BABVg5yWwKAp%2BaHp2voAFQCh6QodOWGAMcjRvELgX1Vz66gya76sL8lAU4jW%2BkPcAV%2Bdyvu8Jal0KGQ3AapVggmKApHk0HX2rQldtJMoLo2%2Bu%2Bg1ViiyRW%2BfAeOm8x2Nr%2BoZWZ%2BmM407nWgjktsChnXcdowaSkQvJh8Cxn4cPyCaRohe0GDkk2WDwMfAPwg7n37gC3LICagOpPYiC1YnwQntbO0xJHKqlmxwAemHcp66d0fxeHB5NhwFqBrP40PGbJsDoGCWM3%2FpI7eJlZ8lnH%2BmRG2eBBD9F4d51yMJ%2FJD3KOBAn6ygV8%2B%2BPbbI67zqvatBqvU53hqTdA%2B3%2F5zKbkWU4Yt3wfjQ0ARaYjSXiB9eEcGpqW%2Ff0%2FXNLCodJLldfizy3l4%2Fde8xwE1elT2Mf2OZ%2B4qZ3LzXYY9GRvs0yqZxgbqMMA7onW9cUMJy6%2F9IGOqUBzk4JLUriPvjN83wtxjl1DSyvKn4Jvw9mdnOphUmXmW965u7K4zxJfMLEbQed3l0MXcubVy9Y4XbjFUjII1%2BjTuGe%2BstqIO86UP%2BassR1ItCUjKbR%2B2tc9wUoNBm8kMHNCFzBZ0Ukh2fmNiSlWPmhLYZHNjAoEgRyzJ05O7ZJuRuTWKyvxClpHxRm2gvrpcijlg8Xhv5AK3Me592tEBpXEjqzxxtt&X-Amz-Signature=51d578e807a6370c72043db895243d2026803f02ba22ff5fbb673c60dcad7401&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

斜杠其实在 windows 和Mac，另外是Lux，它其实符号是不一样的。分割符我们是需要去写得更加的兼容一些，怎么去写会更加的好。在这里我们可以这样子写，使用file，这是文件点有一个叫做separate， separate 它的意思就是一个分割符，使用来替代斜杠就可以了。所以在这个后方我们来写一个加号就可以了，再把斜杠给去掉。在这里每一行我们都可以这样子去写就行了。随后把每一行我们都可以来写一下。


OK，这个路径我们就在这里写好了。我们再来看一个。这个其实就是一个斜杠 block space，斜杠image。在斜杠foodie，再到斜杠faces。其实我们可以进去看一下它的一个源码。在这里看一下它其实是使用的是一个separate，等于号，再加上 separate 差。在这里我们再点一下 separate 叉。在这边可以看到它是通过FS，点 get separate。


FS 其实是一个当前操作，是什么意思？在这里有它是一个 file system，是一个 default file system。可以看到是 default file system。点 get system 获得当前的一个默认操作系统，它的注释在这边也会写。如果是在 Unix 系统，其实就是 Linux 和 Michael s，它的值取值就会是一个斜杠。如果是在 windows 操作系统，是两个反斜杠。OK，好，大家去注意一下。有知道这样的一个使用方式就可以了。随后我们再把直接就可以在这里去使用了，因为我们是直接定义好的写一下。在这边我们就直接定义为 file space，作为我们文件上传的一个命名空间，直接就可以等于这个地址就行了。


好，随后我们再来一个。每一个用户在上传的时候，它其实都会有不同的用户ID，所以我们不能够把每一个用户上传的头像都统一的放在同一个文件夹，所以在这里我们应该要区分一下。在路径上为每一个用户增加一个 user ID，用于区分不同用户上传。写一下string，在我们取个名字叫做 upload pass，他 fix 就是他的前缀。短语。在这里也是使用 file 点separate，再加上这个， user ID 是从我们的参数里面获得。这样子这两个路径我们就定义好了。


以后。随后我们其实就可以去做一个具体的文件上传了。写一下开始文件上传。文件上传的时候肯定要去判断一下咱们 file 是不能够为空的，如果为空肯定是不可以去做上传，否则就可以直接 return 一个错误的消息， error message 文件不能为空。大图。

