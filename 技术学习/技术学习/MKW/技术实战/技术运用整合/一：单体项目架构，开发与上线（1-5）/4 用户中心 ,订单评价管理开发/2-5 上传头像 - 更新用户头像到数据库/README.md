---
title: 2-5 上传头像 - 更新用户头像到数据库
---

# 2-5 上传头像 - 更新用户头像到数据库

[image](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/66b77300-852f-456d-b9af-da28fb59d0a5/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VSSK6XKQ%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T224727Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDGE3r28r7tF1gcxc3RuUVI8GdKefYPqrrDozCc04OG2QIgQKotpymTcSFkf0Lpws8nwPTEWNboYl60eGu6e8qu7eMqiAQIxv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDFmwpznQpOYappv1ayrcAyhQrEEI845rcBUE1TJUeU0JHsOUuHJUG11Ricox4N7mKY5gSGBs6GMpCafdn2t6T7cDK%2FExx%2BpG7Ydyw9oJlThUOFnD2Hw%2B8jqFbZRqUlUmzbGpINzykC6b4PFCNIlsm0O0znOLMBpVrejhbFeEPc7NOf6EwVL3mK8TdT02d1YilBGVeyiK5yzA7rYTm9bvvKzhTySYl%2FmkgTW87I%2BrI1x83wkjDgYiCtHNC2KmUbwCtReBGdLnSxQJiNjjqvFxsrRzu2hGCyhQqoCjZ4CHx3XX6D7dOa0yzFQMd9r2htcXJvjW16V6%2FdgsjlLuY0FPx6sJ0vWGttwnIG3oO1z7pFsNlf6JohTYQqQJTE4dMGNML8HoiC6iI1P%2B29ICvl25YqQlB9w18M8s1NuoPYB3Z0FPYNKhkplYcV5pJJUd%2Fw8Rt3AI6FQNc7FwShaKvOEyYdHbHQ3UUfxeLWWpAbO%2BxO7oikH5dvM5YBHCxvAiQvhAyY6bVFILYzb%2BFOszmnkj%2F1akCXDnUonNH1T1kqP1AX9Ep8pAXoxpDjmxP%2BRKU11YlzurLuoSAjO%2BlVQHosOmULlaGoVmUoxTdu2OkHq0vsXvbxFLWIl3IIyy%2Fzvz9j3Axe2RZZfDOckZfIzxMNe6%2F9IGOqUBj%2FxZV7HJInKWzBBUnycbIJhUd9OlM8kUMuIlx5ocdgWdj2074c9TFbaqMRCESIxyCl4SSGsR2I%2FR64z9sIcrS0FuBo%2BV6%2Bqx8yHwIh9dRWBVOqIx6HLEbOsd5DE7lVzWNO6vvcrahw00kUMxp2oyREt9gr5jaayjDTvfOQiE%2FcXK8%2BgeHWStrRYyhN6DDTovsVgpZ2rspHStchYzbokD1UAWme1u&X-Amz-Signature=de9709972b00a2c8badba842a4b35dfd62efa69af9912af0e0b716abfc8dbfc5&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

图片是上传到了服务器，并且我们也可以通过浏览器去访问这张图片了，因为我们已经是配置了映射服务。接下来所要做的就是应该要把这一张所更新好的。一个图片的路径地址要更新到我们的数据库，所以相应的我们应该要把它的用户信息也要去做一个更新的。所以这一节我们把内容可以去写一下。


首先我们应该要去写一下service，在这里去定义一下，拷贝一个方法。 update user 这边是写一个face，传入一个是用户的ID，另外一个是用户的头像。 face u r l 加上一个注释，用户头像更新好。随后我们到实现类里面去把这个方法实现一下，数不要忘记去加一下，在这里面我们就可以去做一个更新的操作了。


更新操作由于我们之前是做了，其实也是类似的，把之前的方法拷贝过来，拷贝过来以后我们去做一个修改。首先在这里是创建了一个新的用户 update user，设置用户的组件。在这里又是设置了用户的一个信息更新的时间。当然我们在这里面是需要去放入一个 set 图片，也就是face，把 face u l 给贴进来，这样子我们就可以去执行一个更新了。


更新完毕以后，把用户的新的信息再查询一遍给返回出来，这样子我们 service 就已经是写好了。回到 Ctrl 了以后，在这里下方我们就可以去写了。写一个user，这是一个 user results，加个注释，这是更新用户头像到数据库短语 user service。


点有一个 update user face。把用户的组件 ID 以及是用户的头像给放进去，我们就可以放一个用户保存的一个地址了。但是用户的保存地址是在本地的路径，你去存肯定是不对的。所以在这个地方我们应该要去填写一个我要把服务的地址，也就是这个地址。我们应该要把地址更新到数据库。这个地址如何去更新到数据库，我们可以来看一下。


在这里其实我们可以把前面一部分，从我们的访问的域名到 foodie 到 faces 这一块内容，就可以作为我们图片访问的一个服务地址。后方由于用户他的 ID 不同，所以后方的一个地址它其实是会一直变的。我们可以把前面这一部分作为我们公共的一个资源可以写一下。在这里我们就可以写到之前的一个 practice 里面去了。


写上一个 file 点，我们在这边就可以定义为一个 image server URL，就是图片地址，图片服务地址。把路径直接在这边写一下，这样子就 OK 了。斜杠我们去掉，斜杠去掉好。写了之后我们需要到他自己的一个订车类里面，在这边是需要去完善一下的，生成一下 get set，这样子我们才能够去使用。


好。生成 OK 之后，我们就可以去拿到相应的图片服务的 URL 地址了。在这里去写一下 stream image server URL，等于 file upload，点 get 获取一下获得图片服务地址。获得以后咱们就可以去做一个拼接了。拼接由于我们在这里面每一个用户都是不一样的，所以我们是从 user ID 往后去进行拼接。 user ID 其实我们在代码里面是有写的。在我们当前这个类的方法上方有一个 upload pass fix，这个是定义了每一个用户的留在IT，所以我们只要把获取就可以了。获取以后在这个位置在这里上传的头像，最终保存的一个位置在它的后方。你可以去做一个加短语拼接，可以把 file space 应该这样子。不需要去使用。


file separate art 是不需要去使用的，直接在这边使用一个正斜杠就可以了，因为我们这个地址是一个可以在浏览器访问的一个地址，使用就可以去做添加。注意一下我括号，括号一定要使用英文的括号，我在这里使用的是中文的括号，很明显是不可以的，一定要去注意一下。


斜杠。在这里面再去拼接一下它的一个 new file name，比如是写进来，这样子就已经是有了具体的一个值了。用于提供给无外包服务的。写一下用于提供给无外包服务访问的地址。好，拿到了以后，在这个下方我们就可以去做拼接了。在这个地方来定一下string， final user， face u，r， l 等于应该是服务地址。在外加 upload Firepass， upload pass， fix 做一个拼接。


好了以后，这个地址其实就是我们的一个真实地址，真实地址往这边一写，这样子他就可以去做一个更新了。OK，千万不要忘记，在这个地方我们是需要和之前更新用户信息要保持一致，把这一块内容拷贝一下，因为我们会涉及到一个前端用户信息的一覆盖， Todo 也要去加上，因为后续我们也要把 token 给加进去了。这样子其实用户的头像就可以更新到数据库了。但是有一个地方我们还是需要去注意的，也是这个地址。这个地址当我们覆盖到前端之后，前端信息是可以去从 cookie 里头获取的。但是这个地址我们目前拿到了以后，由于我们的前端浏览器，它可能会存在缓存，一旦存在缓存了以后，头像是不能够及时的在前端进行更新的，所以我们在这里应该要加上一个时间戳。加上了一个时间戳以后，前端浏览器会发现我们这个地址发生了一个变化，它就可以把我们在浏览器上的前一张图片更新为现有的一张新的图片，所以这一点是需要去注意的。加一个注释，由于浏览器可能存在缓存的情况，所以在这里我们需要加上时间戳来保证更新后的图片可以及时刷新。


OK，这个时间戳如何去加？我们在后方只需要为它加上一个参数就可以了。加上使用一个问号 t 代表 time 时间戳，这个就是一个路径中的请求参数，在后方我们就可以再去拼接一个时间戳了。通过 date 有跳点， get current 有一个 current date string，这是获得当前的一个时间。当前时间在后面会有一个pattern，也就是它的一个格式化。格式化到这里面去看一下。我们可以使用这个方式，年月日时分秒把直接拷贝一下，拷贝贴到这里使用 date 有跳点，这样子它就可以在我们的路径的后方加上一个时间戳了。


好。现在其实我们保存到数据库里面的方法就已经是做完以后，我们可以到前端去测试一下。需要进行一个install，因为我们添加了一个service。好，启动成功，再来一个重启。 install 成功再重启。好。OK。完了以后我们到页面里面去刷新一下，刷新完毕，在我们点击上传某一个头像，打开上传头像，成功进行了一个刷新。这个时候你就可以发现我们这张图片就已经是在我们的前端页面上进行了一个展示，我们在这里可以检查一下它的源码。在这里咱们就可以看到在这个图片的后方，我们加上了一个时间戳，大家其实可以在课后去试一下，你把时间戳给去掉，你多次去进行刷新，在有些情况下就可以发现它的图片是不能够及时的刷新的，你只能够通过一个浏览器的强制刷新才能够把它的一个新的图片给展示出来。会有这种情况的大家在写代码的时候去注意一下就 OK 了。

