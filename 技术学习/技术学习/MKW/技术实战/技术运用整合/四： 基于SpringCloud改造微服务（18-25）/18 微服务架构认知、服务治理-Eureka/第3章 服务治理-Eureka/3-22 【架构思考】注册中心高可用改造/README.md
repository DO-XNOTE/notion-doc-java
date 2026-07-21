---
title: 3-22 【架构思考】注册中心高可用改造
---

# 3-22 【架构思考】注册中心高可用改造

[image](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/93b9f3c5-5fd3-4657-a303-67c6ad675e5c/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YXV4TOJR%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T225551Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIFCojXdoGI3N8lOXUeyiyTRTDZGI5ix0%2B0EIjkv5rbmUAiEA5v4msyfqGn9M4B9qM6Ug7Rw6mfxX0U2%2B7gSnXJTgujAqiAQIxv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDFZNvL91uG%2BV521kfSrcA4jBwcc6iC4C16%2BklRAwVJlG3ha4ndVMfPtLkRxw2cXx5ZaFPEQxysoPdx5hRdoW4kwgoIxzPrfwefNHVm6%2B6GNUwtEwXkJfCseO0JkNooe3MZxXG7b%2FdfZKHUVbN1UQrHmWDnXDEGQES8ChDL4Ej6n0%2FnxwWRUME2BdD9Z%2FpbSKtajwqUttJGbuJwindzxFHzTtj6JtKkjWkjBQmJclQJlmd%2FFEgcC4zRiZiEd6dv5md0MiPnV8BbUW2kFLLdw7p8JcfhkEip5CTlcS7Wa26CIQaAXL%2BIx96leWW0jm8yptxIMRhhvYxWlJ3Mn0Uh7aouMVhT0YPXUc%2BT70UgbU1HVxwuKtzNpuVChbUeXeAeqzf77qgTX9FcimI3Z2AKLyuEkj4Wy4042m7PRRK0r35fECiLKArE7SZJDccvK0sMD1jL0XZUD8XC597cSgshYvzJx%2FKKSftQd8C%2FiLbWUcCpmEFF%2B8EsRu%2BMU6GlIFr6VS9%2ByDOktybGituBQQx8%2F9KqI%2FuIIrznI2AVwLqOGrdZXM3Tr2sUhsWoDaI%2FrmiFbsbMkPgbf4ALMoG6qrdifcSKYZietbFACTEGi%2F4%2F1zauppwT%2BPFDgwQ4vrJfOUsDyEAfiflAp2MUm8B3yQMJC7%2F9IGOqUB7uu5jLDFOw4X1UL%2BumFuNy0mN7AnZEWuypnjmmMKqH%2Fx55xKdBA6%2F0sVeQ5nElBIvR2QL3ujTwQLKs%2BtDZvH2GkonZmRLkPwQTQBQs8yDMqz%2Be7xKJRQyjzKdY9FT%2B7GF5skSJhjjX%2BTTKfchdSVT%2FImsQYpOKiKEr3d5a06hwqFs9MUU8F7bWWsowWkRSo6HRVkuNMzq3dKVzhvgndfdh6eRMrO&X-Amz-Signature=31d8b16ea17471b313ab58ab5716a5726f56a4896ebfb33babe87ee013d7e84b&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

[image](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/7d408e57-9c8e-4982-b4e8-6cc6e63dc19d/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YXV4TOJR%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T225551Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIFCojXdoGI3N8lOXUeyiyTRTDZGI5ix0%2B0EIjkv5rbmUAiEA5v4msyfqGn9M4B9qM6Ug7Rw6mfxX0U2%2B7gSnXJTgujAqiAQIxv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDFZNvL91uG%2BV521kfSrcA4jBwcc6iC4C16%2BklRAwVJlG3ha4ndVMfPtLkRxw2cXx5ZaFPEQxysoPdx5hRdoW4kwgoIxzPrfwefNHVm6%2B6GNUwtEwXkJfCseO0JkNooe3MZxXG7b%2FdfZKHUVbN1UQrHmWDnXDEGQES8ChDL4Ej6n0%2FnxwWRUME2BdD9Z%2FpbSKtajwqUttJGbuJwindzxFHzTtj6JtKkjWkjBQmJclQJlmd%2FFEgcC4zRiZiEd6dv5md0MiPnV8BbUW2kFLLdw7p8JcfhkEip5CTlcS7Wa26CIQaAXL%2BIx96leWW0jm8yptxIMRhhvYxWlJ3Mn0Uh7aouMVhT0YPXUc%2BT70UgbU1HVxwuKtzNpuVChbUeXeAeqzf77qgTX9FcimI3Z2AKLyuEkj4Wy4042m7PRRK0r35fECiLKArE7SZJDccvK0sMD1jL0XZUD8XC597cSgshYvzJx%2FKKSftQd8C%2FiLbWUcCpmEFF%2B8EsRu%2BMU6GlIFr6VS9%2ByDOktybGituBQQx8%2F9KqI%2FuIIrznI2AVwLqOGrdZXM3Tr2sUhsWoDaI%2FrmiFbsbMkPgbf4ALMoG6qrdifcSKYZietbFACTEGi%2F4%2F1zauppwT%2BPFDgwQ4vrJfOUsDyEAfiflAp2MUm8B3yQMJC7%2F9IGOqUB7uu5jLDFOw4X1UL%2BumFuNy0mN7AnZEWuypnjmmMKqH%2Fx55xKdBA6%2F0sVeQ5nElBIvR2QL3ujTwQLKs%2BtDZvH2GkonZmRLkPwQTQBQs8yDMqz%2Be7xKJRQyjzKdY9FT%2B7GF5skSJhjjX%2BTTKfchdSVT%2FImsQYpOKiKEr3d5a06hwqFs9MUU8F7bWWsowWkRSo6HRVkuNMzq3dKVzhvgndfdh6eRMrO&X-Amz-Signature=05442c97ef63b4dee27a965c29d91fd13a5eea9517b0b01d203de5e6c3b38254&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

[image](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/8aa65eb7-777c-42b4-8168-b9e29b118a2f/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YXV4TOJR%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T225551Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIFCojXdoGI3N8lOXUeyiyTRTDZGI5ix0%2B0EIjkv5rbmUAiEA5v4msyfqGn9M4B9qM6Ug7Rw6mfxX0U2%2B7gSnXJTgujAqiAQIxv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDFZNvL91uG%2BV521kfSrcA4jBwcc6iC4C16%2BklRAwVJlG3ha4ndVMfPtLkRxw2cXx5ZaFPEQxysoPdx5hRdoW4kwgoIxzPrfwefNHVm6%2B6GNUwtEwXkJfCseO0JkNooe3MZxXG7b%2FdfZKHUVbN1UQrHmWDnXDEGQES8ChDL4Ej6n0%2FnxwWRUME2BdD9Z%2FpbSKtajwqUttJGbuJwindzxFHzTtj6JtKkjWkjBQmJclQJlmd%2FFEgcC4zRiZiEd6dv5md0MiPnV8BbUW2kFLLdw7p8JcfhkEip5CTlcS7Wa26CIQaAXL%2BIx96leWW0jm8yptxIMRhhvYxWlJ3Mn0Uh7aouMVhT0YPXUc%2BT70UgbU1HVxwuKtzNpuVChbUeXeAeqzf77qgTX9FcimI3Z2AKLyuEkj4Wy4042m7PRRK0r35fECiLKArE7SZJDccvK0sMD1jL0XZUD8XC597cSgshYvzJx%2FKKSftQd8C%2FiLbWUcCpmEFF%2B8EsRu%2BMU6GlIFr6VS9%2ByDOktybGituBQQx8%2F9KqI%2FuIIrznI2AVwLqOGrdZXM3Tr2sUhsWoDaI%2FrmiFbsbMkPgbf4ALMoG6qrdifcSKYZietbFACTEGi%2F4%2F1zauppwT%2BPFDgwQ4vrJfOUsDyEAfiflAp2MUm8B3yQMJC7%2F9IGOqUB7uu5jLDFOw4X1UL%2BumFuNy0mN7AnZEWuypnjmmMKqH%2Fx55xKdBA6%2F0sVeQ5nElBIvR2QL3ujTwQLKs%2BtDZvH2GkonZmRLkPwQTQBQs8yDMqz%2Be7xKJRQyjzKdY9FT%2B7GF5skSJhjjX%2BTTKfchdSVT%2FImsQYpOKiKEr3d5a06hwqFs9MUU8F7bWWsowWkRSo6HRVkuNMzq3dKVzhvgndfdh6eRMrO&X-Amz-Signature=a8449b676d17a1241f5c9822a16e0cc4415b32140ad9759c63e276aeee35103a&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

Hello 慕课网的同学们，大家好，这一节我来带大家动手搭建一个高可用的注册中心集群。本节的主要内容有，第一条，我们先去 host 文件中动一动手脚，加一些 host name 和对应的 IP 地址的 mapping 第二条，我们从代码层面配置两个注册中心，然后在本地把两个注册中心启动起来，这两个注册中心之间可以相互同步数据。接下来我们把自己的服务提供者注册到单中心，看一看这两个中心之间的同步机制是不是起作用。

[image](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/0525c7a9-5e36-4858-82ad-e8d40ceb4f52/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YXV4TOJR%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T225551Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIFCojXdoGI3N8lOXUeyiyTRTDZGI5ix0%2B0EIjkv5rbmUAiEA5v4msyfqGn9M4B9qM6Ug7Rw6mfxX0U2%2B7gSnXJTgujAqiAQIxv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDFZNvL91uG%2BV521kfSrcA4jBwcc6iC4C16%2BklRAwVJlG3ha4ndVMfPtLkRxw2cXx5ZaFPEQxysoPdx5hRdoW4kwgoIxzPrfwefNHVm6%2B6GNUwtEwXkJfCseO0JkNooe3MZxXG7b%2FdfZKHUVbN1UQrHmWDnXDEGQES8ChDL4Ej6n0%2FnxwWRUME2BdD9Z%2FpbSKtajwqUttJGbuJwindzxFHzTtj6JtKkjWkjBQmJclQJlmd%2FFEgcC4zRiZiEd6dv5md0MiPnV8BbUW2kFLLdw7p8JcfhkEip5CTlcS7Wa26CIQaAXL%2BIx96leWW0jm8yptxIMRhhvYxWlJ3Mn0Uh7aouMVhT0YPXUc%2BT70UgbU1HVxwuKtzNpuVChbUeXeAeqzf77qgTX9FcimI3Z2AKLyuEkj4Wy4042m7PRRK0r35fECiLKArE7SZJDccvK0sMD1jL0XZUD8XC597cSgshYvzJx%2FKKSftQd8C%2FiLbWUcCpmEFF%2B8EsRu%2BMU6GlIFr6VS9%2ByDOktybGituBQQx8%2F9KqI%2FuIIrznI2AVwLqOGrdZXM3Tr2sUhsWoDaI%2FrmiFbsbMkPgbf4ALMoG6qrdifcSKYZietbFACTEGi%2F4%2F1zauppwT%2BPFDgwQ4vrJfOUsDyEAfiflAp2MUm8B3yQMJC7%2F9IGOqUB7uu5jLDFOw4X1UL%2BumFuNy0mN7AnZEWuypnjmmMKqH%2Fx55xKdBA6%2F0sVeQ5nElBIvR2QL3ujTwQLKs%2BtDZvH2GkonZmRLkPwQTQBQs8yDMqz%2Be7xKJRQyjzKdY9FT%2B7GF5skSJhjjX%2BTTKfchdSVT%2FImsQYpOKiKEr3d5a06hwqFs9MUU8F7bWWsowWkRSo6HRVkuNMzq3dKVzhvgndfdh6eRMrO&X-Amz-Signature=bce39bc45a4cf11e24445b4399c3cda7a3148a81933713180a28928c6a800d22&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

最后一点，我们在自己的服务提供者中把单节点注册改成双节点注册。 OK 下面我们就抄起家伙准备开拔。嘿，我们来到了 host 文件所在的 etc 目录。在 Mac 下面。我们直接进入 etc 就可以找到 Windows 的同学们要到网上先搜一下自己 host 文件所在的位置，因为不同的 Windows 系统它 host 文件所在的位置是不同的。 OK 在 Mac 里面，我们不能在这个文件夹下直接修改这个文件内容，把它复制出来。我这里已经复制到了一个文件夹下，我们把 host 打开来放大一点。好勒。这里我们添加两个 host name 分别是什么？我们先来添加 host name here a pair one 和 pair two 它是什么意思呢？碟机后面我们会说明的。

[image](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/db617ed8-45cc-483f-9429-9c8584896497/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YXV4TOJR%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T225551Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIFCojXdoGI3N8lOXUeyiyTRTDZGI5ix0%2B0EIjkv5rbmUAiEA5v4msyfqGn9M4B9qM6Ug7Rw6mfxX0U2%2B7gSnXJTgujAqiAQIxv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDFZNvL91uG%2BV521kfSrcA4jBwcc6iC4C16%2BklRAwVJlG3ha4ndVMfPtLkRxw2cXx5ZaFPEQxysoPdx5hRdoW4kwgoIxzPrfwefNHVm6%2B6GNUwtEwXkJfCseO0JkNooe3MZxXG7b%2FdfZKHUVbN1UQrHmWDnXDEGQES8ChDL4Ej6n0%2FnxwWRUME2BdD9Z%2FpbSKtajwqUttJGbuJwindzxFHzTtj6JtKkjWkjBQmJclQJlmd%2FFEgcC4zRiZiEd6dv5md0MiPnV8BbUW2kFLLdw7p8JcfhkEip5CTlcS7Wa26CIQaAXL%2BIx96leWW0jm8yptxIMRhhvYxWlJ3Mn0Uh7aouMVhT0YPXUc%2BT70UgbU1HVxwuKtzNpuVChbUeXeAeqzf77qgTX9FcimI3Z2AKLyuEkj4Wy4042m7PRRK0r35fECiLKArE7SZJDccvK0sMD1jL0XZUD8XC597cSgshYvzJx%2FKKSftQd8C%2FiLbWUcCpmEFF%2B8EsRu%2BMU6GlIFr6VS9%2ByDOktybGituBQQx8%2F9KqI%2FuIIrznI2AVwLqOGrdZXM3Tr2sUhsWoDaI%2FrmiFbsbMkPgbf4ALMoG6qrdifcSKYZietbFACTEGi%2F4%2F1zauppwT%2BPFDgwQ4vrJfOUsDyEAfiflAp2MUm8B3yQMJC7%2F9IGOqUB7uu5jLDFOw4X1UL%2BumFuNy0mN7AnZEWuypnjmmMKqH%2Fx55xKdBA6%2F0sVeQ5nElBIvR2QL3ujTwQLKs%2BtDZvH2GkonZmRLkPwQTQBQs8yDMqz%2Be7xKJRQyjzKdY9FT%2B7GF5skSJhjjX%2BTTKfchdSVT%2FImsQYpOKiKEr3d5a06hwqFs9MUU8F7bWWsowWkRSo6HRVkuNMzq3dKVzhvgndfdh6eRMrO&X-Amz-Signature=2038a1373f72d8a31a329420aca8291119c6fd5210f591f8f96d4560001a4efc&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

提起皮尔大家知道前几年有一款饮料也叫皮皮尔茶所是蛮火的，很多女生也喜欢喝，喝完之后给人说，我一次能吹三瓶，我又吓死了。你问这三瓶是茅台五粮液来说 PR 查说钱吃东西我当水喝，我都觉得。好了，这里定义了 PR one 和 PR two 分别指向哪里幺二七点零点零点幺相当于 local host 对不对？我们把这个保存一下关闭，然后把 host 文件再 copy 到 etc 下面。 replace 原因要确认一下管理员权限。好，我们打开这个验证一下。 OK 没问题，PR one 和 PR two 都在这里了。


第一步，修改 host 文件步骤我们就完成了。接下来让我们移步到 intellij 里面，开始撸代码。好，又到了大家的主战场，我们选中 sprint cloud demo 在这里新建一个 module 还是 Maven 类型，点击 next 它的 artifact ID 是 eurika 杠 server 杠 P 把它复制一下进入 next 这个 module name 还跟前面保持一致。然后文件存放的路径大家都很熟悉了。 error 卡。 OK 点击 finish 出来。


好的，这里泡沫我们就直接 copy 前面的一个项目，尤瑞卡 server 我们把它 copy 过来，原封不动的拷贝到当前项目中。好泡沫文件就这样了。然后启动类我们也依然是采用 copy 的形式。因为对这两个项目来说大部分都是相同的，不同的地方是哪里来配置对不对？好，我们把这个包给它重新命名一下。 come.imock.string cloudok 接下来就到了这两个项目不同的地方了。我这里建一个 application practice 大家可以看一看这里面有什么奥秘。双倍分的注册中心创建完，我们把这个屏幕拉大。第一个属性依然是自报家门，我的 application name 是什么？ eureka server 我们把它叫什么？ tier one 好不好？ tier one OK 那它的 server port 我们把它定义成 20,001 之前的注册中心，它的 server port 是 2 万对不对？我们这里不跟它冲突，变成20,001，给它配置一个什么呢？一个 host 


nameeureka.instance.host name 它的 host name 是什么？ PR one 对不对下面这个属性大家在注册中心上就没见过了，它是什么？ eureka.client 咦这看起来有点奇怪了。


service 杠 url.default zone 这个 Z 要大写，那它是什么意思呢？作为一个注册中心，它要向其他的注册中心同步数据。对不对？所以他这里要配一个兄弟节点。那这个兄弟节点是谁呢？就是 HTTP 双斜杠，他自己是 P2 万对不对？那我要把信息同步到 P2 two 上。 P2 two 的端口是多少啊？ P2 万是20,001，那 P2 two 就是二万。好了好不好？后面杠 U 瑞卡，那我这里加一个注释注册中心注册。好嘞，到这里为止我们的 PR one 就已经设置完成了，接下来是不是要设置一个 PR two 没错，考虑到 PR one 和 PR two 配置基本上相同，所以我这里就不再花时间跟大家 demo 了，给大家变个小魔术。


我们数到 123 这里创建一个皮尔图好不好？准备好了吗？ 1231 这边出现了一个 PR two 是不是？我们来看一下它的 palm 已经配置好了，然后启动类我们检查一下也已经在这了。还缺什么啊？万事俱备，是不是只差配置。 Are you resources.文件夹下的 application properties 创建出来。 


Properties. 好，我们关上小桌板把它放大。那当前这个应用是 P2 几 P2 two 对不对？所以说它的 spring application name 我们把它配置成 eureka 杠 server 杠 tear two 那它的 pot 是什么？ server.pot 刚才我们看到上一个 tier one 它的 server pot 是20,001，然后他指向皮尔兔的 2 万。那我在这里把皮尔兔的 pot 给它设置成 2 万，再往下是设置我的 host name eureka.instance.host name 是什么？是 pair two 对不对？最后是 eureka client service URL a four zone zone Z 大写这里啊指向谁？啊是不是指向 tier onetier one 的端口号是20,001，后缀是尤瑞卡。


好，这些配置完之后，那这样的话 PR two 也已经配置完成了。接下来我们就把 PR one 和 PR two 的应用全部启动起来，看一看相应的注册中心页面上面会发生什么变化。打开小桌板，我们找到 TR two 直接跑起这个慢函数，同时再把 PL Y 的内函数也给它跑起来。宝贝看看 PR two 是不是已经成功了，看到 started 成功了，那 PR one spring 大标签成功一半，再到下面正在跑 startedok 都成功了。那这时候切换到浏览器。好，我这边已经打开了一个注册中心的页面，2001把它刷新一下，这应该是 PR one 的刷新一下。


好，出来了，我们往上看这是什么？ Ds replicates. 我们看到在 P R one 的 DS replicates 列表中出现了 PR two 那我们接下来再到 PR two 上看一下它的端口是 2 万，看到吗？这里 DS replix 同样的也有 PR one 那说明什么？说明 PR one 和 PR two 之间的数据同步的通道已经是打通了。 OK 接下来我们要启动一个服务提供者，让它连接上 PR one 和 PR two 其中的一台机器，看看这台机器会不会将这个服务注册信息同步到另外一台机器上面去。


好，回到开发环境当中，我们找到服务提供者的入口方法。 eureka 下面的 eureka client Java 类中的尤瑞卡克兰的 application 在跑闷方法之前，我们先去看一下浏览器为什么以证清白，看一看 server two 上面现在有没有 instance 没有对不对？ server one 上也没有刷新一下对不对？也没有。
那好，我们再回到开发环境，再来瞄一眼 application property 看看这个 service provider 服务提供者，它只连接上一个对不对？ local host 2 万。那这里我用的是 local host 而不是 PR 其实效果是一样的，因为不管是 PR one year two 还是 local host 它在 hosts 词文件中都指向 12 七点零点零点幺这个 IP 地址，所以我这里用 local host 的效果也是没有区别的。好，我们现在就启动服务提供者的慢方法走起，看到 spring 的大标签成功一半。好嘞，这里我们看到他已经注册成功了，又 started 的 log 打出来。


接下来我们到浏览器上看一看，他注册上的是 logo host 的二万对不对？那我们先到这个 2 万的节点上刷新一下。 eureka client 出来了对不对？那接着下来我们到 20,001 上面再看一下刷新。好，这里也出来了，那它是怎么出来的？是不是我的服务提供者直接连上？他俩并不是我服务提供者是连上了 2 万。那这里的尤瑞卡克兰特是由 2 万这台机器同步到 20,001 上的。 OK 接下来我们再尝试一种不同的配置方式，同时将两个注册中心 PR one 和 PR two 同时配置在服务提供纸上，又回到了开发环境。我们在对 application properties 做变更之前，先把刚才启动的 eureka client 给关掉。关闭了之后，我们打开 application properties 第 5 行，看到吗？我们把它 copy 下来，然后粘贴粘贴一行一模一样的。同时第五行暂时给注释掉。为什么呢？因为我们做完这个 demo 还要把它还原回去。好在第 7 行我们把这个 local host 改成 pear to 转口号是 2 万。好，前面说，这里要配置两个注册中心，那这还只有，剩下一个怎么配置呢？这里加一个逗号就可以加个逗号，后面跟另外一个注册中心。那它是 pear one。


Pear one. 然后它的 pot 是20,001。好，我们保存好之后，我们到闷方法里把服务提供者创建一个实力跑起来看。接下来 started 已经成功了，切换到浏览器看一下效果是不是和之前一致。我们先到 2 万上面刷新一下，看到幽瑞卡 client 已经出现在这里，而且它的 status 是 up 那再到 20,001 上看一下，刷新一下。同样有瑞卡克莱恩特也注册成功了。


OK 前面我们提到这是一个高可用的改造，那我们不妨这样人为构造一个异常场景。是什么场景呢？我们不是连接上了两个注册中心吗？这时候在连接之前，我们把其中的一个注册中心给它下线掉，看一下服务提供者是否还能正常的注册到另一个注册中心上？我们先把服务提供者下线，看服务提供者这里配置的第一个连接上的是谁？是 PR two 对不对？ 2 万端口的。那我们不妨把这个 2 万端口的服务给下线掉。 2 万端口的应该是这个。


好，下线完了之后，我们再次启动 service client application 成功一半走往下走。好嘞，这里已经 started 接下来我们到浏览器上看一下，2万端口的已经是 does this site cannot be reached 已经是不可用了，这就是模拟了一个宕机状态，那我们到 20,001 上看一下，我们刷新一下看到吗？伊瑞卡克兰特还是完好无损的在这里，那它是什么机制呢？大家知道吗？前面是不是有读过服务注册的源码对不对？那它这里是一个轮询的机制，他会尝试从这边拿到一个可用的服务注册中心的 URL 来进行注册。如果第一个拿到的假设注册不成功，那他们会往后继续轮询，直到注册成功为止。但是同步的事情那就不是归他管了。对不对？同步是我们注册中心之间互相同步，而不是我们服务的节点替他们做这个同步的工作。好，那到这里为止，我们的注册中心高可用改造就已经完成了。在前面两节的架构思考课程即将结束的时候，我这边还有几个小想法想跟大家一起分享一下。


那这个标题叫 keep in mind 就是让我们在工作中时常回顾，时常温习的一些小点。第一点是什么？ server 固有意思，它的意思就是说你的服务器总归会挂的，它要么死于今天，要么死于明天。随着我们工作经历的增长，碰到的问题也会越来越多。有的时候导致 server 宕机的小故障往往是有一连串的问题，它巧合的放到了一起。比如说我们提交一个 hot fix 紧急补丁，这个补丁有可能有一些 bug 但是很难发现。那它随着系统的运行会消耗系统的资源，需要一定的时间积累才会导致问题的发生。


我们在本地测试的时候，没有发现日常环境，还是没有发现在预发测试在测试团队匆忙验证以后，直接发布到了生产环境，在生产环境又没有做好灰度部署，或者是说金丝雀测试等等，这一个问题就被一连串的疏忽放到了线上。我们在线上跑了一段时间，结果发现不对劲了，所有机器团灭了，这是我在实际工作中碰到的一个例子。所以你经历的越多，你见过的错误会越来越多。但是我们 KP 慢的什么呢？不要怕犯错，因为从错误中汲取经验，是印象最深刻的，最能学到东西的。但是一个错误一定不要犯两次。


Ok.第二点是什么？我想提醒大家警惕挖掘机什么意思。你们还记得前面分享过的支付宝被一铲子搞挂的事情是不是而且机把网线挖断了。我们为什么说在架构设计的时候一定要异地双火或者是异地多活？比如说阿里，它甚至要求你应用部署的这个机房中要有两个机房，它的距离超过一千千米。为什么他需要这么远？为了躲挖掘机跑很远是吗？不对，他其实是为了警惕像自然灾害之类的突发情况。那我打个比方，如果你的机器是部署在沿海，对不对？我们说极端天气海啸、台风，那有可能影响到你两个机房，两个机房都团灭了。


那我说这个概率小不小非常小，但是会不会发生？大家说有可能吗？是有可能的。没错，大家还记得这个墨菲定律是怎么说的吗？他说如果一个事情，它有一个变坏的方向，有变坏的可能性，不管它概率多小，她最后总会发守。所以说我们在做高可用架构的时候一定要有一个追求，那就是什么？考虑到所有异常情况，我们要确保万无一失。


还有第三点，latencylatency是什么？是说延迟？那比如说注册中心同步，它需要时间，对不对？它不是瞬间完成的。那目前大型的互联网应用我们都不可能做到全链路强一致性。那你做这种架构设计的话，对，这个雷特斯延迟有一个余量，也就是说确保核心主链路中不会因为这种最终一致性方案导致异常情况。


OK 最后一点想跟大家分享的是 brave 什么意思？勇敢打破保守，跳出舒适圈。我们不要只盯着自己熟悉的架构方案。 10 年前大家可能有用 struts 到了 10 年后的今天，我依然用struts。 No no no. 你的思维会怎么样？会固化，因为我们人本身就是偏向在什么舒适圈里面呆着，对不对？我们的脑子大脑都会去依赖不费力的这种选择。所以说平时在工作中一定要多向年轻人学习，你的年龄并不是你在这个架构领域或者权威领域的话语权，你在养老公司工作十年，做那种没有挑战的工作，你架构上的能力其实未必比得过在互联网行业捶打三年的年轻人。 OK 这就是想跟大家分享的内容。



