---
title: 2-23 使用PostMan调试Restful接口
---

# 2-23 使用PostMan调试Restful接口

[image](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/4578330f-c800-40fa-8b64-4b4d92950be6/SCR-20240816-qkja.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VBUURYZQ%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T224616Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQD2BIsNRRUmpfXv5TQw3QJu37r2RkuxGpKExbt8AxOe%2FQIhAIY5k3j1Mcp0zMaXKzwUUYq78nSJ1pDWQfiuQ0eVavVWKogECMb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1Igzs2344DOH1XmuzIKwq3AOwSc4%2BqijhxORnqEIff%2BsiGGFi4nzNcjSXd9uE9KVtYbtf6S8DeNcdLIq0%2FsgHlcPWkHZmYRZFlOmyJU2dU%2FYYoeF22rc9RVykcdUOJaC32BxhNqN%2BrNacLl4JN6VFXjw4RmZaXDm6xYtidM9DVM03kWupXDEgvJ8321Ol4q9guMuheDhbZNmHA42M0CMGepSoZec70OSqvXMCBbg9LyEdADezJBZ66uMamkloHUnpHIjNcTKY%2BEg6xFxZTiyypZuR%2FC7KY86nUbg6MKu4lgKp1QuUk100hvdu7s8cKIfeiwZ1E%2FErelUTdQo2E0WsZS1Kun05RlVwoix6BtIWBM1J5m97cKocOVPrSUyR0O7akYyNkmmpP%2BSX7o2S3wzboP8ggAXAomg8d4Kc90NmUWh%2F7p%2FrWlmTiN6lq8cHphVzgtWPs0flKAvLivuStP7kDuLaJP4wr%2BvGjw1lEify0W9tDErJWqzWdaHfck0%2FDArxevVNwjkYHITN4wYZlS1wKF40X7pzVhwolIstbhUp8TeKuBwdV%2BQ%2FJYIwA91EGztukwISek7KLnYeLwAjLOIDKeL%2FcJAn5I1cyzkkv%2BSdkRtDwgUUcUhC6peUQg6pYXgZXSln15z6kPe5BFRgazCEu%2F%2FSBjqkAZJ772jKnnl1Bzcvbuh0B0VtPyFF%2F93F6%2FaVF7WAxChl%2F2FFO8yVBg1lecyWHl3mIR2vBKWiHM4qFE4oxIHRGkvsUMLrhfwJt3VvgW4ri%2FmDL9XrHWpJ3ZuMwpXG42uqGaVMaLunm8gPTPXMrYTsZVXZ%2BiLv9QJXXouV78KulflVF92s5Bp%2F9%2FlbRjvxFz9ocf3XyVZew2G4tmVATGvO8I7yo2%2Fo&X-Amz-Signature=1448c027ab32055832b0b4fb566b3883e0ba76226fa1ec388d590777f119b2de&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

[image](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/2c77843f-fe81-4c17-b2ba-9c1607abc2ab/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VBUURYZQ%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T224616Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQD2BIsNRRUmpfXv5TQw3QJu37r2RkuxGpKExbt8AxOe%2FQIhAIY5k3j1Mcp0zMaXKzwUUYq78nSJ1pDWQfiuQ0eVavVWKogECMb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1Igzs2344DOH1XmuzIKwq3AOwSc4%2BqijhxORnqEIff%2BsiGGFi4nzNcjSXd9uE9KVtYbtf6S8DeNcdLIq0%2FsgHlcPWkHZmYRZFlOmyJU2dU%2FYYoeF22rc9RVykcdUOJaC32BxhNqN%2BrNacLl4JN6VFXjw4RmZaXDm6xYtidM9DVM03kWupXDEgvJ8321Ol4q9guMuheDhbZNmHA42M0CMGepSoZec70OSqvXMCBbg9LyEdADezJBZ66uMamkloHUnpHIjNcTKY%2BEg6xFxZTiyypZuR%2FC7KY86nUbg6MKu4lgKp1QuUk100hvdu7s8cKIfeiwZ1E%2FErelUTdQo2E0WsZS1Kun05RlVwoix6BtIWBM1J5m97cKocOVPrSUyR0O7akYyNkmmpP%2BSX7o2S3wzboP8ggAXAomg8d4Kc90NmUWh%2F7p%2FrWlmTiN6lq8cHphVzgtWPs0flKAvLivuStP7kDuLaJP4wr%2BvGjw1lEify0W9tDErJWqzWdaHfck0%2FDArxevVNwjkYHITN4wYZlS1wKF40X7pzVhwolIstbhUp8TeKuBwdV%2BQ%2FJYIwA91EGztukwISek7KLnYeLwAjLOIDKeL%2FcJAn5I1cyzkkv%2BSdkRtDwgUUcUhC6peUQg6pYXgZXSln15z6kPe5BFRgazCEu%2F%2FSBjqkAZJ772jKnnl1Bzcvbuh0B0VtPyFF%2F93F6%2FaVF7WAxChl%2F2FFO8yVBg1lecyWHl3mIR2vBKWiHM4qFE4oxIHRGkvsUMLrhfwJt3VvgW4ri%2FmDL9XrHWpJ3ZuMwpXG42uqGaVMaLunm8gPTPXMrYTsZVXZ%2BiLv9QJXXouV78KulflVF92s5Bp%2F9%2FlbRjvxFz9ocf3XyVZew2G4tmVATGvO8I7yo2%2Fo&X-Amz-Signature=8da7912c06f530a58a5377cf7557e7c7371f1840119a8977a351df14a4cfa229&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

现在我们已经是通过 restful web service 去创建了 4 个接口，这四个接口分别都是增、删、改、查、get、mapping。我们是可以通过浏览器 URL 去进行一个调试测试的，但是除了 get 以外，像 post put、 delete 类似这样的请求，我们是无法使用浏览器去进行测试的，所以就像浏览器不可以使用了。所以我们可以依靠旗下的一些调试工具。比方我们会使用Postman，这个是它的官方的地址，可以来看一下。


get postman . com 其实我相信有一部分同学可能会使用过，主要是用于去调试一些基于 restful well service 的一些 API 接口的，这个我们就可以去使用。打开当前的一个首页，在这里会有一个 get start，点击一下，随后根据自己的一个版本去下载。它也是一个跨平台，不管是Mac， windows 还是 Linux 都有。下载完毕之后就可以去进行安装了。来看一下。


安装完毕之后，它就是这样的一个logo，点击一下，点击一下以后，这个就是它的一个布局。简单的看一下，在它的一个左侧，其实都是一些相应的history，每次调用完毕之后的一些历史记录都会在这里。当然还有是collection，自己所创建的一些，相当于是收藏夹都可以往这边放。对于我们来讲，我们目前只是需要用于去调用我们的后端 API 就可以了。可以点击new，这个里面会有一些相应的选项。对于我们来讲，使用第一个就可以了，一个创建一个请求，低效不去选择。在这个位置有会有很多的一些请求。 tab 页点击加号也可以。随后在这里面就可以看到。我们就可以去填写一个请求的 URL 地址了。随后在这一块会有很多的一些请求的方法类型，像最常用的get， post 都有，还有put，delete，全部都有。这里面会有很多。比方我们可以先写一个get，随后我们再把之前所调用的地址，我们是可以去进行一个拷贝的，直接把地址拷贝一下，随后再放到 Postman URL 地址。 Ctrl v 贴过来。贴过来以后在它的后方，它的一个参数，其实它会作为一个 query pumps，作为一个请求参数放在这个下方的。如果我们以后还有一些其他的参数，都可以在这边去写的，比方我们可以来一个name，再来一个m，可这个时候你就可以看到他会帮我们在路径里面进行一个拼接，中间会有这样的一个宇号的。


好。随后我们来发起一个请求到咱们的后端，我们一起来看一下相应的结果。当然现在我们是一个 get 请求，点击，在这里有一个send，点击以后就可以看到。在我们的一个网页端所得到的一个结果是，现在它其实就是一个Jason。这个时候在我们的 post man 里面已经是打印了出来，看一下，有很多的一些格式，有杰森，叉庙， XT 庙等等。目前我们的格式就是一个 JSON object。


好，这个是一个查询。随后我们可以再来看一下保存的操作。把 save s t 5 拷贝一下，我们把这边的路径直接可以改掉，使用这个就可以了。随后再把我们的方法的请求改成post，我们可以再来执行一次send。点击会发现这里。这个时候返回给我们的是一个OK。这个 OK 其实就是在我们后端在这里所返回的OK，它是一个字符串。好，我们回忆来到我们的数据库来刷新一下，这个时候我们的数据就已经是有了。OK，这个是我们在 service 层是写死的，一个是Jack，一个是 19 岁。当然我们可以再来再次的点击send，我们可以点击多次。现在其实我们总共是有 5 条，我们再刷新一下数据库，这 5 条记录都是我们所新增的。现在我们新增的接口是 OK 的。再来看下一个接口，下一个接口就应该是一个更新的接口。我们直接把 1008 这条记录我们可以去修改一下。我们把 UI 里面的路由地址去修改，随后它的 ID 我们可以去加一个，是1008，点击 send 发送过去。好，这个时候返回到的是一个OK。我们可以来到数据库，看一下我们的数据有没有更改。刷新。改掉了，改成了 Lucy 以及是 20 岁。


好，我们再下一个。下一个应该是一个删除操作，把拷贝一下，接到我们的postman，可以直接把贴过来。ID，我们改成1007，把 1007 这条记录我们去删除，点击 send 发送过去。OK，完了以后我们可以再到数据库刷新一下。刷新以后可以发现 1007 一条记录就已经是成功的被我们删除了。现在我们就可以是通过 Postman 这样的一个工具来调试我们所有的一些 API 接口了。对于 Postman 工具来讲，很多公司都在使用，它是非常便于我们去调试一些 restful 形式的 web service 接口的。


