---
title: 4-4 商品搜索- 实现分类搜索商品查询
---

# 4-4 商品搜索- 实现分类搜索商品查询

[image](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/4a165521-7c72-43cf-a7f7-8ca2c1136943/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XEAUXT6L%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T224649Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCetw54p8UChoBc2K%2Bs7GJ5OOlVniBrvzNL6GLr0C2tSAIhAOBZYIaH12VaFz9CokQxf8B1ViY%2BmCBI8MdwHq7PyeAzKogECMb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1Igz%2Fmy%2F9jM3FahsGbssq3AONZu%2Fxdu6m1ryB9Sayjc9tW0p1EofOmLqcRH32EIRTD4OQJezn%2Bax0RG1sa2jJwDE4QjAL0HCFED9Duyms%2FbxnnJQzHqwxqC7n7v8uTg9AADMuAMZkQGdw4hmbQl7cqpcKw8sKFGlmh%2FBc05G9IIau0VzEcu1kprVJd3fVxByQ%2BbXyyk7%2BpJMrKO1l7rCdrpqSn5PiaIrqKQG6rQTEPHIzWUYu%2FZj8hyJ2id8IoNZBGeD5ckA5jSqmJmkqCxyV53gh3l%2BttRybTT2Tl0casDC6u2XYE7K1xOaTUT3%2BtB5YikVoxmxLFL%2FE9fFNXup%2FRtOQT%2BX2pCg2BAxBXbVnhHATa1ZwjMt4ttftlm9n8AzEzzlohfNPMVHHSlWA5OO9VJx3Ik%2FgPDPfyBFD9fPsI71eBuWUgzLuBx248tTTohInvEiWjzPaSsxxCchQy0DzUVXAZwRmtXJYQHhV3BcAvFozAiJ0s1G9263h%2FT9sdWX5xksCf0T6U9zpepGYbgz9T%2BnE1UPkbHhekifljUjniL2P9Ycf3cAUpyMB1HByznrTbiq0nY6VSbV9Y1DEif7XYJYNYlAs%2FJgCmgWvPWSnIlPank%2BoimqRSjdglpWwue9kLdJm24%2BuWffBcEbpFjCCt%2F%2FSBjqkAeq53f9B9IP%2BCePKHyG0c%2BeAb2adtyNNccaUbpnheJZiMUXlEoHqCpWsrOAuUXU2SjayqGUP7kAx0EGLxzJYkLpNg5jBe8s9aMNiZUXeAcMWTCNMcmChCb%2FbsyiNBtH7OnIaA5YKJWk1Tr%2BWAloDOuG2z0yUMhlzi5GapimQbMXJboL7HUiU3PS7rp5YlMpzP86Q0yXZ29DxVkX9Yd588xkjQnfu&X-Amz-Signature=d08626f3a725460b660771e7531a2272e80799e7dadbc3913ba53645eb613f9a&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

根据分类 ID 去进行搜索。map，我们已经是写完了。随后我们快速的把 service 和 controller 来写一下，因为他们的代码其实也是差不多的。


先来把这个方法我们先写一下。这个方法是查询商品，它是 by third cat，写一下。其余的我们就不需要去改动了，因为都是返回的类型，以及是传入参数都是一模一样的。好，我们就要来定一下我们的service。在这个 service 里面，我们也可以把这一段内容拷贝一下，拷贝一下。在这边我们所要传进来的一个参数就不再是 q word，而是一个 cat ID，是商品分类的一个ID，它是一个 Int 类型。好，写一下。其余的我们就不需要去改动了。好，OK，写一下。这是根据分类 ID 搜索商品列表，我们接下来就要把 service 方法去进行一个实现。写一下。先把这个事物贴过来。在这里面的内容其实和上面是一样的，只要做一些修改， keywords 改成 cat ID 就可以了。调用的方法在这个后方，我们是需要去加上一个 by third cat，OK。其他的我们就不需要去多动了。这一块内容写完之后，接下来把我们的 Ctrl 去修改一下，复制一份，在这里面去做修改。在这边它的一个路由是 cat items 切过来。


好，OK。其他的内容比方像搜索商品列表就是 swag two。我们改一下。通过分类 ID 搜索商品列表，好，OK。在这里传入的内容也应该是一个 cat ID，直接可以写过来就可以了。 cat ID 类型改一下， value 也改一下，它是一个分类ID，应该说是三级分类的ID。


OK，在这边判断。我们就不应该判断一个keywords，应该要判断KXD，判断它是不是为空。如果为空，我们直接返回一个空信息。或者你在这里写上一个分类，不能为空也可以。接下来判断配置以及是 page size，我们留着就可以了。在这个地方改一下，应该是 search items， cat ID 是 buy item service。我们看一下这两个方法其实是可以一样的。这样子其实是一个重载，如果你要去在后方去加上一个 by third cat 也可以，我们就这样子 cat ID 传进来，这样子也没有问题。OK，现在我们的 Ctrl 了，这样子就写好了，是 OK 了。好，现在我们来进行一个install。好，install，现在是成功了。成功以后我们重启服务器，好，启动成功。


我们先通过 swig two 来进行一个测试。现在新增加了一个接口。在这里面我们可以传入一个分类的ID，这个分类 ID 我们可以到首页去搜一下。比方我们随便挑一个，这是一个猪肉脯，猪肉肠，对吧？我们挑一个73，把 73 拷贝过来，目前生产环境上卡住了。没关系，不影响我们在本地做测试。把 73 贴过来，排序配置这些内容。这是第一页，这些不填也无所谓。


点击发送可以看到我们一些相应的信息都查询出来，只不过它的总共的记录数只有 6 条，所以它并没有分页。OK，这个接口我们是通过 swag two 测试是成功了。接下来我们可以回到咱们自己的首页，我们的通过 local host 去访问的。在这里我们可以来随便挑一个凤梨苏分类，在这里面没有任何内容，所以季度是为0。随后我们再可以挑一个猪肉脯，查询出来以后总共是有 6 条记录，相应的内容全部都有。


OK，现在我们可以通过分类 ID 就可以去实现了。然后我们来一个排序，点击这里的默认排序，销量排序和价格排序都没有问题，相应的一些数据也能够正常的去进行排列。OK，现在其实我们两种搜索方式，通过关键字去搜索，通过商品的分类 ID 去搜索。这两个我们都已经是完成了，只不过我们是使用了两个不同的接口。OK。

