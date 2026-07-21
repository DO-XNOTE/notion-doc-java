---
title: 1-3 【核心基本功】K8S基础集群搭建
---

# 1-3 【核心基本功】K8S基础集群搭建

[image](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/96620959-5570-4a0d-a4c6-7fbd59bf74c6/SCR-20240726-bnwj.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664VNZOGJ7%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T225934Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQC8AVLZgZBwqOUyfxMFpxz8IEBR16dEoYDNjj7uX1zvAwIgQK4gMkKhVAYcvpMC4icky9tmTTxIAaceuNNkiVSeVpkqiAQIxv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDMqH4Iht68%2FFQlUHeSrcA10E706KTujvnfOrCsrbQFTQ7NZYKZIMe5TmrNi6%2Fcyk2zZGi6WPv97fy%2Fo5rAQr0hTmQnc1KR9DIFFV9XgJPZ%2FHNA0F7K5QQvVHFI61SrTumJp4IDk7xYKW%2FuyUFpaCaCa4awP98gluGKuMnj9F%2FFfqFxfiVchq%2FED4xGdEXEmwYMP9fqWuSX0MQXxvo4Pr0bmn8EYGcWXMVGtXMBkm0ZTRxFKojH5Mmnk9TJzoxAQQHj0hIMz5htaSsKLwwzjJ4LE%2FPCTYtEYGX76Wj1Mo8CmJm9%2F1%2B40EQuTq9NeWZH3scmqYjfIjy3rh8WxxQDpBGNRwabjhsxxxT03EEJI4dL%2B2UUw9rQc0nH77ijzj3rIDusX2CG1SvtOqWm1xPYRksVXRJlB1Aiz73GaMTzqIOG7EBtt2H%2F8ncz8ZDIIuKL9%2BY1x58Vjjvlsput8r3BD0femIAcFMDXD%2BMJLo3mmTnSKwC6C3lUstlpn3wZdN6vobHbd95j%2BfkagwH6FyN2lQRNC%2FNYMDU8dDlMlJoTHfNGLcaXf76lB%2F9xHsE9eH2%2B0cDiPUriwzYR2OjDIAX%2FVtHgIUKncjUtSPOkVeZcI7DNUjGWCNm9pHnaxuIv9SKJ4d%2BKiDODWINyqcDaRTMMm4%2F9IGOqUByWKfb2YB9TJ8t9fSu7rHHYXKraXeURMnWuDj0hii93L8aUNjrdefspKifOiD6v0uL6KdOafdL9RSw7cGvalF3kWQVslGhSyVoqasKRb%2FtslRtUalG3T8aHjRCn1RNXRXD9dROqcjQ0CgIhMngneRpqBb4PfB%2BlafP5TJZABjGYtR6QDMpTujiotWTrI8Rap0eV4UqxtikATiaOWWzfmFTrVQhH5Z&X-Amz-Signature=fb6cf81cfab58ff3afae6771a493501c0a4b10e89b7044a850ea8021b5a03722&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

[image](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/231fffe2-01d5-4152-9ff6-5d8e3352d8e3/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664VNZOGJ7%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T225934Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQC8AVLZgZBwqOUyfxMFpxz8IEBR16dEoYDNjj7uX1zvAwIgQK4gMkKhVAYcvpMC4icky9tmTTxIAaceuNNkiVSeVpkqiAQIxv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDMqH4Iht68%2FFQlUHeSrcA10E706KTujvnfOrCsrbQFTQ7NZYKZIMe5TmrNi6%2Fcyk2zZGi6WPv97fy%2Fo5rAQr0hTmQnc1KR9DIFFV9XgJPZ%2FHNA0F7K5QQvVHFI61SrTumJp4IDk7xYKW%2FuyUFpaCaCa4awP98gluGKuMnj9F%2FFfqFxfiVchq%2FED4xGdEXEmwYMP9fqWuSX0MQXxvo4Pr0bmn8EYGcWXMVGtXMBkm0ZTRxFKojH5Mmnk9TJzoxAQQHj0hIMz5htaSsKLwwzjJ4LE%2FPCTYtEYGX76Wj1Mo8CmJm9%2F1%2B40EQuTq9NeWZH3scmqYjfIjy3rh8WxxQDpBGNRwabjhsxxxT03EEJI4dL%2B2UUw9rQc0nH77ijzj3rIDusX2CG1SvtOqWm1xPYRksVXRJlB1Aiz73GaMTzqIOG7EBtt2H%2F8ncz8ZDIIuKL9%2BY1x58Vjjvlsput8r3BD0femIAcFMDXD%2BMJLo3mmTnSKwC6C3lUstlpn3wZdN6vobHbd95j%2BfkagwH6FyN2lQRNC%2FNYMDU8dDlMlJoTHfNGLcaXf76lB%2F9xHsE9eH2%2B0cDiPUriwzYR2OjDIAX%2FVtHgIUKncjUtSPOkVeZcI7DNUjGWCNm9pHnaxuIv9SKJ4d%2BKiDODWINyqcDaRTMMm4%2F9IGOqUByWKfb2YB9TJ8t9fSu7rHHYXKraXeURMnWuDj0hii93L8aUNjrdefspKifOiD6v0uL6KdOafdL9RSw7cGvalF3kWQVslGhSyVoqasKRb%2FtslRtUalG3T8aHjRCn1RNXRXD9dROqcjQ0CgIhMngneRpqBb4PfB%2BlafP5TJZABjGYtR6QDMpTujiotWTrI8Rap0eV4UqxtikATiaOWWzfmFTrVQhH5Z&X-Amz-Signature=a6cb2eca29d176f4653b61e545f18ec073b722f7019ac7774d7e4480e896871d&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

前面一个章节我们介绍了kubernetes的整体架构，还有它主要的功能模块。那这里呢我们带领大家开始呢真正正进入 kubernetes的实战，先把环境搭起。你在搭环境之前，我先要介绍一下。我们这里会尝试用三个节点来部署我们的 kubernetes之后的所有的 lab 也都会基于这样三个节点。那第一个节点叫什么叫 training 3，那这个节点会作为我们 kubernetes 的 master 节点，就是大脑。

[image](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/07c96cd7-c11f-40ed-bc26-747adf8a5f98/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664VNZOGJ7%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T225934Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQC8AVLZgZBwqOUyfxMFpxz8IEBR16dEoYDNjj7uX1zvAwIgQK4gMkKhVAYcvpMC4icky9tmTTxIAaceuNNkiVSeVpkqiAQIxv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDMqH4Iht68%2FFQlUHeSrcA10E706KTujvnfOrCsrbQFTQ7NZYKZIMe5TmrNi6%2Fcyk2zZGi6WPv97fy%2Fo5rAQr0hTmQnc1KR9DIFFV9XgJPZ%2FHNA0F7K5QQvVHFI61SrTumJp4IDk7xYKW%2FuyUFpaCaCa4awP98gluGKuMnj9F%2FFfqFxfiVchq%2FED4xGdEXEmwYMP9fqWuSX0MQXxvo4Pr0bmn8EYGcWXMVGtXMBkm0ZTRxFKojH5Mmnk9TJzoxAQQHj0hIMz5htaSsKLwwzjJ4LE%2FPCTYtEYGX76Wj1Mo8CmJm9%2F1%2B40EQuTq9NeWZH3scmqYjfIjy3rh8WxxQDpBGNRwabjhsxxxT03EEJI4dL%2B2UUw9rQc0nH77ijzj3rIDusX2CG1SvtOqWm1xPYRksVXRJlB1Aiz73GaMTzqIOG7EBtt2H%2F8ncz8ZDIIuKL9%2BY1x58Vjjvlsput8r3BD0femIAcFMDXD%2BMJLo3mmTnSKwC6C3lUstlpn3wZdN6vobHbd95j%2BfkagwH6FyN2lQRNC%2FNYMDU8dDlMlJoTHfNGLcaXf76lB%2F9xHsE9eH2%2B0cDiPUriwzYR2OjDIAX%2FVtHgIUKncjUtSPOkVeZcI7DNUjGWCNm9pHnaxuIv9SKJ4d%2BKiDODWINyqcDaRTMMm4%2F9IGOqUByWKfb2YB9TJ8t9fSu7rHHYXKraXeURMnWuDj0hii93L8aUNjrdefspKifOiD6v0uL6KdOafdL9RSw7cGvalF3kWQVslGhSyVoqasKRb%2FtslRtUalG3T8aHjRCn1RNXRXD9dROqcjQ0CgIhMngneRpqBb4PfB%2BlafP5TJZABjGYtR6QDMpTujiotWTrI8Rap0eV4UqxtikATiaOWWzfmFTrVQhH5Z&X-Amz-Signature=a29428094d3fcf1a6728d739eeb055a4ab8a002359d80cf4ae6873b10d3be7a4&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

[image](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/6d59a342-1228-4b0d-ba58-1628ecede1d8/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664VNZOGJ7%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T225934Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQC8AVLZgZBwqOUyfxMFpxz8IEBR16dEoYDNjj7uX1zvAwIgQK4gMkKhVAYcvpMC4icky9tmTTxIAaceuNNkiVSeVpkqiAQIxv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDMqH4Iht68%2FFQlUHeSrcA10E706KTujvnfOrCsrbQFTQ7NZYKZIMe5TmrNi6%2Fcyk2zZGi6WPv97fy%2Fo5rAQr0hTmQnc1KR9DIFFV9XgJPZ%2FHNA0F7K5QQvVHFI61SrTumJp4IDk7xYKW%2FuyUFpaCaCa4awP98gluGKuMnj9F%2FFfqFxfiVchq%2FED4xGdEXEmwYMP9fqWuSX0MQXxvo4Pr0bmn8EYGcWXMVGtXMBkm0ZTRxFKojH5Mmnk9TJzoxAQQHj0hIMz5htaSsKLwwzjJ4LE%2FPCTYtEYGX76Wj1Mo8CmJm9%2F1%2B40EQuTq9NeWZH3scmqYjfIjy3rh8WxxQDpBGNRwabjhsxxxT03EEJI4dL%2B2UUw9rQc0nH77ijzj3rIDusX2CG1SvtOqWm1xPYRksVXRJlB1Aiz73GaMTzqIOG7EBtt2H%2F8ncz8ZDIIuKL9%2BY1x58Vjjvlsput8r3BD0femIAcFMDXD%2BMJLo3mmTnSKwC6C3lUstlpn3wZdN6vobHbd95j%2BfkagwH6FyN2lQRNC%2FNYMDU8dDlMlJoTHfNGLcaXf76lB%2F9xHsE9eH2%2B0cDiPUriwzYR2OjDIAX%2FVtHgIUKncjUtSPOkVeZcI7DNUjGWCNm9pHnaxuIv9SKJ4d%2BKiDODWINyqcDaRTMMm4%2F9IGOqUByWKfb2YB9TJ8t9fSu7rHHYXKraXeURMnWuDj0hii93L8aUNjrdefspKifOiD6v0uL6KdOafdL9RSw7cGvalF3kWQVslGhSyVoqasKRb%2FtslRtUalG3T8aHjRCn1RNXRXD9dROqcjQ0CgIhMngneRpqBb4PfB%2BlafP5TJZABjGYtR6QDMpTujiotWTrI8Rap0eV4UqxtikATiaOWWzfmFTrVQhH5Z&X-Amz-Signature=66d521ea4af49c82e755e10cfdf4e6c01fa9e4db36446bd18878929ad1a072be&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

[image](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/2edd2064-3136-4dbf-8dd2-34c1994e4206/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664VNZOGJ7%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T225934Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQC8AVLZgZBwqOUyfxMFpxz8IEBR16dEoYDNjj7uX1zvAwIgQK4gMkKhVAYcvpMC4icky9tmTTxIAaceuNNkiVSeVpkqiAQIxv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDMqH4Iht68%2FFQlUHeSrcA10E706KTujvnfOrCsrbQFTQ7NZYKZIMe5TmrNi6%2Fcyk2zZGi6WPv97fy%2Fo5rAQr0hTmQnc1KR9DIFFV9XgJPZ%2FHNA0F7K5QQvVHFI61SrTumJp4IDk7xYKW%2FuyUFpaCaCa4awP98gluGKuMnj9F%2FFfqFxfiVchq%2FED4xGdEXEmwYMP9fqWuSX0MQXxvo4Pr0bmn8EYGcWXMVGtXMBkm0ZTRxFKojH5Mmnk9TJzoxAQQHj0hIMz5htaSsKLwwzjJ4LE%2FPCTYtEYGX76Wj1Mo8CmJm9%2F1%2B40EQuTq9NeWZH3scmqYjfIjy3rh8WxxQDpBGNRwabjhsxxxT03EEJI4dL%2B2UUw9rQc0nH77ijzj3rIDusX2CG1SvtOqWm1xPYRksVXRJlB1Aiz73GaMTzqIOG7EBtt2H%2F8ncz8ZDIIuKL9%2BY1x58Vjjvlsput8r3BD0femIAcFMDXD%2BMJLo3mmTnSKwC6C3lUstlpn3wZdN6vobHbd95j%2BfkagwH6FyN2lQRNC%2FNYMDU8dDlMlJoTHfNGLcaXf76lB%2F9xHsE9eH2%2B0cDiPUriwzYR2OjDIAX%2FVtHgIUKncjUtSPOkVeZcI7DNUjGWCNm9pHnaxuIv9SKJ4d%2BKiDODWINyqcDaRTMMm4%2F9IGOqUByWKfb2YB9TJ8t9fSu7rHHYXKraXeURMnWuDj0hii93L8aUNjrdefspKifOiD6v0uL6KdOafdL9RSw7cGvalF3kWQVslGhSyVoqasKRb%2FtslRtUalG3T8aHjRCn1RNXRXD9dROqcjQ0CgIhMngneRpqBb4PfB%2BlafP5TJZABjGYtR6QDMpTujiotWTrI8Rap0eV4UqxtikATiaOWWzfmFTrVQhH5Z&X-Amz-Signature=7bc67b557f431b7696097303018b5b42b846f62b4045c2b55d989dc6c845d1d6&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

另外还有两个节点分别是我们的 training 4 这是其中一个 node 还有一个 training 5 是另外一个 node 那这两个 node 主要是用来做什么？真正容器的执行，容器软件的安装是在 4 和 5 上面。
3 作为 master 节点。这三个节点是有一个特点就是什么我是租的一个公有云环境，但是这三个节点所在的网络是美国的弯曲的网络，所以它很容易能够跟谷歌的 kubernetes 的我们的这个registry ，跟 kubernetes 相关的这个样本源进行很方便的沟通。


这三台机器现在我已经是把 Doc 装好了，具体 Doc 的安装方法可以参借 Doc 那个章节的 Doc 环境 install 那装完以后就进入了库伯内特斯的核心安装的过程。那主要要装三个软件，这里提到的 kubernetes 相当于什么 kubernetes 的核心，不管你是 master 还是 node 节点，都需要有个 kubernetes 来运行实际的容器的管理和处理。 kubeadmin 是集群的管理核心，那它会创建一个集群在 coupon 的 master 上。同时我们的每个 node 也用这个命令来加入和参加了集群，所以它实际上类似于集群的管理命令行。那kubectl 大家应该后面的内容，如果实战过以后会越来越熟悉kubectl是所有库命令的。什么是源头所有的库命令起头第一个单词都是 cupctrl 然后加上 apply 加上 get 等等，来实现我们整个 kubernetes 的命令行的操作和管理。



这三个软件装完以后，我们后面就会进入什么，我们在 master 节点上面去创建集群，用 coupadmin init 和 apply 建集群建网络，然后在各个 node 节点上选择 coupon admin join 去加入这个集群。那这样我们一个三节点的最简单的库博 latis 的整个集群环境就搭建好了，那我们来看一下实战。
真正装之前，我先打开一个网页。通常我们科普 natives 的安装都会kubernetes.[io](http://is.io/) 的文档，然后你一路点下去，你可以在 production 环境当中找到一个 coupe admin 的安装文档，这 guide 会告诉你说怎么样安装比较方便，那它这些会有些提示就是什么？

你需要有怎么样的一个网络预准准备环境？

其实我们最好的一个环境就是离我们的谷歌非常近，我们不希望有其他东西阻挡我们。
那如果你申请的是比如说自己机房的节点或者笔记本，你访问谷歌有点问题，你或者可以开通代理，或者可以通过其他的一些什么 Mirror 节点或者是外面找一个节点能够进行 Email 的下载， YAML 源的安装。那这个时候你可以把一部分的软件包复制到我们自己的节点上，或者通过类似于像阿里云镜像的方式把一些东西镜像过来。那最不麻烦的地方就是如果有些这种 Doc image 你可以在远端的那个 plus 能力上尝试去简单的下载。下载完了以后，把 image 导出，然后导入到自己的笔记本或者是自己数据中心里面，封闭式数据中心里面的这个机器上也可以完成整个集群的安装。所以如果你不能很方便的访问这个谷歌网络，你会稍微麻烦，但也不是那么麻烦。


为了简单起见，我这里就是直接是在能连谷歌网络的美国湾区的生态机器的为例，这个生态机器是 santa OS 操作系统，所以它会告诉你说你先要建一个什么建一个羊毛源。那我们在这里就是把这个羊毛源废置进去，就如法炮制，把这段内容复制在三台机器上，先挑一台 5 跑一下，然后我们再切换成一台 4 是吧，这三台机器是都要做类似步骤，所以我们可以同时做每一个步骤，然后再切换到3，我们去把这三个基本的这个配置样本源的步骤跑完。


那跑完以后我们再切回我们的网页它盖的说什么，他说 SE Linux 请关闭，它有些这个具体的关闭方法一样的。我们可以把这些方法在每台机器上面逐一执行是吧，这是一台 3 执行完了，然后我们可以在 4 和 5 上分别进行执行。这就是四好四月执行完了，我们可以再登到5，在 5 上也去执行这个内容。好也就执行完，那就是 s104 暂时关闭了，然后他就会说什么，他说。


那你就可以用一个 YAML 的 install 的命令，把最主要的三个软件 cooperate admin 和我们的什么 ctrl 这个命令行工具一起安装掉。好我们这里就按它的方法直接把它给装掉。那这安装过程稍微有一点点时间，其实你是在一个离谷歌很近的环境的网络，也会有点时间。那么我们陆续登到三台节点上去装一下，我们都在装好，犹太节已经装完了是吧，相对还是比较快的。


那装完以后，他下一步他说什么？他说是用一个命令来启动这个 couplet 另外两个工具一个是什么 control 还有一个是 admin 的都是工具。这个 couplet 其实是一个后台的进程。那我们其实更熟悉的是什么？在 center 里面一个 system ctl enable 是吧 couplet 用这个命令，然后再跑一个 C term ctl 是吧 restart 是吧 couplet 这两个命令是一个平时最常用的命令，我们可以按照我们的习惯跑这两个命令，我们看看 45 是不是已经装完了，45也装完了，先跑一个以内包，使它能够重启会生效。同时把这个进程如果没有启动，把它给启动起来，如果已经启动了以后，也可以让它重新启动一下。好同样道理，我们在五上也是一样，复制一下，再无上 enable 一下。然后在 5 上重启一下这个 corporate 复制一下，在第五台机上把我们的 couplet 重新的启动起来。


好，这样我们这个准备工作都完成了，就是这么三个节点共同的准备工作。那下一步就开始真正的什么去初始化我们的这个库博内特斯的集群，然后进行什么网络的整体配置。那在初始化的过程当中，大家可以想象，整初始化什么最核心的什么，其实不是简单的初始化，而是去我们的谷歌的这个相关的 Doc 的 image 的地方， registry 的地方去下载相关的 image 然后把这些 image 实际的部署到我们的主要就是这个 master 节点上，因为整个过程其实初始化的核心过程都是在 master 节点完成

的。
那这个过程当中，首先要求你 master 点能够很方便的跟我们的什么我们谷歌的这个 doctor registry 相沟通，我们现在会尝试怎么样去安装它，我们可以这样做。首先就是调一个命令叫 coupe admin 然后我们可以查一下 coupe admin 有哪些参数，然后如反了炮制一点。好，我们用 coupe admin 对吧，这个就是建立集群的那个命令。然后我们可以什么杠 help 去看一下它有哪些命令可以使用。那它这里可以简单看到它的有什么，它有个 init 命令，那这是我们需要的。


那我们可以看一下 kubeadm init 然后杠 help 看一下一定下面有些什么样的参数可以使用呢？好他这里提供了一些建议，就是离职的过程当中可以尝试一些各种各样的功能，比如像刚刚我们可以看到有什么 dry run 大家可以仔细看，就是说尝试一下。


如果你担心你自己的脚本有问题，你可以用 dry run 然后还有一个功能就是什么 API server advertise address 这是一个很关键的点，就是指明我这些机器用什么样的 API server 来提供服务，其实也就是指明我到底是用哪一个 IP 地址在这根集群当中，跟我们所有的 no 节点进行沟通。


那除此以外，还有一个很关键的参数是什么？我们再往下看是 port network cidi 就是我到底希望整个过程当中我用怎么样的网络来跟大家沟通。那我这里整个过程当中，在网络章节之前我都会尝试用什么用法兰戎这个网络，因为这个网络相对是最简单，虽然它不支持很多的ingress 、权限管理、访问管理，但是基本的网络配置都是通的。它通过大二层的这种思路，能实现所有的这个节点之间能够很方便的进行容器之间的沟通，它会默认什么？它如果前面一个容器降级还记得的话，它的默认网段是10:24，后面点 0.0 斜杠16，也就是五二五点零点零的这样一个网络，我们这种网段可以很方便的什么进行大而成的那种。



跨容器跨节点来访问。好，那我们就用这个方法，我们开始初始化我们的集群。 coupon admin in it 刚刚看了什么 API server advertise address 然后这等于什么呢？等于我们本地这个地址。我们本地的地址是什么地址呢？其实我之前已经是知道的是幺七二点二零点二三零点八零这样一个地址，这是我们本机的一个 IP 地址。然后这个地址其实如果你在公网上做机器，有可能你会拿到一个公有地址。一个私有地址，你就用那个私有地址，也就是你最方便跟另外两 no 的沟通的那个地址来作为本地的地址。然后你还有个参数，就是刚刚看的什么 POD network 然后它的 CI DR 它的这个网络 CI DR 那它是多少呢？


是十点二四四点零点零。这就是我们如果用法兰绒网络默认的一个地址。

[image](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/f79c92be-7fef-4fb3-9fe6-2583b677c41a/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664VNZOGJ7%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T225934Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQC8AVLZgZBwqOUyfxMFpxz8IEBR16dEoYDNjj7uX1zvAwIgQK4gMkKhVAYcvpMC4icky9tmTTxIAaceuNNkiVSeVpkqiAQIxv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDMqH4Iht68%2FFQlUHeSrcA10E706KTujvnfOrCsrbQFTQ7NZYKZIMe5TmrNi6%2Fcyk2zZGi6WPv97fy%2Fo5rAQr0hTmQnc1KR9DIFFV9XgJPZ%2FHNA0F7K5QQvVHFI61SrTumJp4IDk7xYKW%2FuyUFpaCaCa4awP98gluGKuMnj9F%2FFfqFxfiVchq%2FED4xGdEXEmwYMP9fqWuSX0MQXxvo4Pr0bmn8EYGcWXMVGtXMBkm0ZTRxFKojH5Mmnk9TJzoxAQQHj0hIMz5htaSsKLwwzjJ4LE%2FPCTYtEYGX76Wj1Mo8CmJm9%2F1%2B40EQuTq9NeWZH3scmqYjfIjy3rh8WxxQDpBGNRwabjhsxxxT03EEJI4dL%2B2UUw9rQc0nH77ijzj3rIDusX2CG1SvtOqWm1xPYRksVXRJlB1Aiz73GaMTzqIOG7EBtt2H%2F8ncz8ZDIIuKL9%2BY1x58Vjjvlsput8r3BD0femIAcFMDXD%2BMJLo3mmTnSKwC6C3lUstlpn3wZdN6vobHbd95j%2BfkagwH6FyN2lQRNC%2FNYMDU8dDlMlJoTHfNGLcaXf76lB%2F9xHsE9eH2%2B0cDiPUriwzYR2OjDIAX%2FVtHgIUKncjUtSPOkVeZcI7DNUjGWCNm9pHnaxuIv9SKJ4d%2BKiDODWINyqcDaRTMMm4%2F9IGOqUByWKfb2YB9TJ8t9fSu7rHHYXKraXeURMnWuDj0hii93L8aUNjrdefspKifOiD6v0uL6KdOafdL9RSw7cGvalF3kWQVslGhSyVoqasKRb%2FtslRtUalG3T8aHjRCn1RNXRXD9dROqcjQ0CgIhMngneRpqBb4PfB%2BlafP5TJZABjGYtR6QDMpTujiotWTrI8Rap0eV4UqxtikATiaOWWzfmFTrVQhH5Z&X-Amz-Signature=fe7120eb33b5c28237e83d8b9e50e0afe652afe94eacc47b5b98494de78be813&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

由于内网私网地址 10 开头的十点二十四点零点零十六这些输入完以后，我们再仔细检查一下 init API server advertise address 自己的 IP 地址好没有问题，那它这里会做一些什么？ preflight 所谓 preferred 就是什么？前面跑之前的一个检查，他也帮你检查一下你这个 IP 地址是不是你的对吧，你是不是真的拥有这个 IP 地址。


同时你这个网段试点 2244 这个网段是不是私有网段，他会做一些简单的检查，那之后他就会尝试什么？你看到这里有叫 image pool 就是真正的开始去我们谷歌对口的这个 doctor 的 registry 上面去下载相关需要的一些镜像，他会把这些镜像分别的安装上去。


刚刚看到有些过程是 cert 交互，我们公司要，那这里是拿一些货补的 config 拿些简单的配置文件。下面是做一什么 controller plan 就是控制层。我们通过一些控制层的方式，把很多的 API server ctrl manager schedule 我们最后要以这个实际的容器的形式启动，这 component 的配置文件都下到了，那之后才是真正开始。我们把容器真正按照当前配置文件的形式来进行起起来起在我们的 master 节点上。那下面是很多的启动增改修改的过程。


好他说什么我们已经主要内容都跑完了，它的提示你看到什么剩下什么，你还需要做一步两步三步的操作做。然后你还需要做一个把网络 apply 的操作，之后，你就可以让其他节点通过这个命令来 join 这段内容。其实大家可以如果当时在实战的过程中可以 copy 到一个文档，然后你就按这个文档来做。那我们这里也类似，我在这里建一个 text 文档编辑器。好，我们把这段内容拷贝出去，拷贝到这个文档编辑器里面，放大一点，拷贝到这个文档编辑器里面对吧，这个大家应该差不多够了。

然后就可以什么按照他的要求把前三步给做了，只需要在你的主节点做就可以了。 no 的节点就是其他节点只需要 join 就可以了。我们在主节点，那它也会提示你，就说你其实也可以建立一个新的账号来做这个事情，不一定用 root 但我们简单起见我们就用 root 好，我们 clear 一下屏幕，因为内容已经保存了。


好，第一条做完了对吧？第二条正在做是不是覆盖是？第三条应该已经做完了。好三条命令做完以后，你就可以尝试什么尝试进入 apply 这个网络的环境。那网络有很多很多的网络可选项，它这里有提示 concepts cluster admin 按照我这里会选择法兰绒。所以法兰绒的网络会在另外一个地方有我们打开一下网页，我这里提前就把法兰绒网络的地址已经输入了法兰绒。从 raw github user content 下面有个叫 call S 因为法兰绒的供应商是 call S 他会提供一个 documon 的说我的库布的法拉绒的配置羊毛文件是这样，你只要用库布 ctrl 去 apply 他就可以很方便的把法兰绒的网络给生效了。


那我们就来试一下指定这样一段内容，然后切回我们刚刚的地方，用 cooper CTR apply 一下。 apply 以后我们实际去生效这样一段配置文件，我们看一下它的效果会是如预期这样好吗？这个文件因为在 F 的时候是指定一个具体文件，我们这里其实是一个网络文件，所以需要什么？ HT BS 冒号把刚刚内容补全好，我们这里补全一下，这样就是。

[image](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/c98733c1-11c7-4087-8f72-694a1651356e/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664VNZOGJ7%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T225934Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQC8AVLZgZBwqOUyfxMFpxz8IEBR16dEoYDNjj7uX1zvAwIgQK4gMkKhVAYcvpMC4icky9tmTTxIAaceuNNkiVSeVpkqiAQIxv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDMqH4Iht68%2FFQlUHeSrcA10E706KTujvnfOrCsrbQFTQ7NZYKZIMe5TmrNi6%2Fcyk2zZGi6WPv97fy%2Fo5rAQr0hTmQnc1KR9DIFFV9XgJPZ%2FHNA0F7K5QQvVHFI61SrTumJp4IDk7xYKW%2FuyUFpaCaCa4awP98gluGKuMnj9F%2FFfqFxfiVchq%2FED4xGdEXEmwYMP9fqWuSX0MQXxvo4Pr0bmn8EYGcWXMVGtXMBkm0ZTRxFKojH5Mmnk9TJzoxAQQHj0hIMz5htaSsKLwwzjJ4LE%2FPCTYtEYGX76Wj1Mo8CmJm9%2F1%2B40EQuTq9NeWZH3scmqYjfIjy3rh8WxxQDpBGNRwabjhsxxxT03EEJI4dL%2B2UUw9rQc0nH77ijzj3rIDusX2CG1SvtOqWm1xPYRksVXRJlB1Aiz73GaMTzqIOG7EBtt2H%2F8ncz8ZDIIuKL9%2BY1x58Vjjvlsput8r3BD0femIAcFMDXD%2BMJLo3mmTnSKwC6C3lUstlpn3wZdN6vobHbd95j%2BfkagwH6FyN2lQRNC%2FNYMDU8dDlMlJoTHfNGLcaXf76lB%2F9xHsE9eH2%2B0cDiPUriwzYR2OjDIAX%2FVtHgIUKncjUtSPOkVeZcI7DNUjGWCNm9pHnaxuIv9SKJ4d%2BKiDODWINyqcDaRTMMm4%2F9IGOqUByWKfb2YB9TJ8t9fSu7rHHYXKraXeURMnWuDj0hii93L8aUNjrdefspKifOiD6v0uL6KdOafdL9RSw7cGvalF3kWQVslGhSyVoqasKRb%2FtslRtUalG3T8aHjRCn1RNXRXD9dROqcjQ0CgIhMngneRpqBb4PfB%2BlafP5TJZABjGYtR6QDMpTujiotWTrI8Rap0eV4UqxtikATiaOWWzfmFTrVQhH5Z&X-Amz-Signature=954a98c8f13f149457da57a8da4884dab75988ce435be5a30201a424669d02cd&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

他这其实已经是有了 HTTP 了，那就不用再额外补全了。我们刚复制下来的时候看到是没有，那其实后台的协议是 HTTPS 所以我们就不需要额外的补全，就需要指定一个网络文件。


通过指定这个网络文件，我们的 master 节点就可以把它给生效起来。我们稍微等一下它是什么？它会把相关的我们的什么 POD 的 security policy 可以创建好我们的 role 创建好 service account 创建好 config 创建好 config map 还有什么 demoset 这些内容在后续章节会详细讨论。


全部创建完以后，其实我们这个库普内提斯整个的这个集群已经搭好了，但它只有一个 note 节点。好我们可以看一下 coupct get 用这个命令。那之后所有的这个扩部的操作基本上都是通过命令行扩部 CTR 跟我们的集群进行沟通。 get 是查询的这个命令，node是当前节点信息，我们可以看一下是不是已经 ready 了。是的 ready 了， master 已经 ready 了，但它只有一个节点，这个节点就是 training 3，它是我们整个 quota 的 master 那另外几个节点怎么处理呢？处理过程，建物刚刚保测的内容，这个内容很重要。这里有一个 token 这个 token 其实就是什么，如果我要加到一个集群里，有首先要知道它是什么样 token 才能加入。我们把这串内容完完整整的复制下来， control C 下了。


然后到我们另外两个节点上分别是什么？ training 4 和 training 5 对不对？在 training 4 上我们就直接输入这个。因为之前我们的 coupe admin 已经安装过了，所以这条命令是可以正常执行的，但是能不能成功的加入，我们看一下效果，他这里说什么。我们开始执行库布雷特的 start 了，用 free preflight 了一把。


最后什么？ this node has joined the cluster 很成功，它加入进去了，你可以用 coup control get notes 来查看，但是你要在 control plan 层才能看到也就是说在这个节点上，虽然你即使装了 coupe control 你是看不到的，你应该在哪里看到呢？你应该退回我们的刚刚的那个 must note 然后用 coupon CTR get note 才能够真正的使得 ctrl 这个命令执行起来，才能真正的连到我的 master 节点去看。


是不是又有一个节点，这个节点是什么？是 no 的节点，它已经 ready 了，成功的加入到了我们的这个集群里，如法炮制，我们给第五台机器也跑刚刚那个一样的命令在所有的 no 节点上分别陆续跑。跑完以后，等她都报成功了，他就说什么成功了，你可以 get notes 了。


好，我们在这里不管你是 get node 还是 notes 有个特点，你的 get meaning upon 命令后面的名词可加复数，可不加复数都无所谓，它都可以辨认。比较简单了，你就不用加复数。好，三个节点， training 3 是 master 另外两个节点都是我们的什么 no 的节点，其中有个 5 还没有 ready not ready 我们等一下刷起来。是不是现在已经 ready 了？这三个节点都已经 ready 了。好这样的情况下，我们已经可以在这个集群里面做各种各样的后续的操作了。下一节我们就来拿这个环境小事。



以下是一个 CentOS 7 上 Nexus 3 开机启动的脚本。在使用前请根据实际情况修改脚本中的路径和用户名密码等参数。

```plain text
#!/bin/bash
#
# nexus3       Startup script for the nexus3 Server
#
# chkconfig: - 84 16
# description: nexus3 Server
# processname: nexus3
# pidfile: /opt/sonatype-work/nexus3/current/nexus.pid
#

# Source function library.
. /etc/rc.d/init.d/functions

# Path to the nexus3 script.
NEXUS3_SCRIPT="/opt/nexus3/bin/nexus3"

# Path to the nexus3 data directory.
NEXUS3_DATA_DIR="/opt/sonatype-work/nexus3"

# Nexus3 user
NEXUS3_USER="nexus"

# Nexus3 password
NEXUS3_PASS="password"

# Path to the pid file.
PID_FILE="$NEXUS3_DATA_DIR/current/nexus.pid"

# Check that the script exists.
if [ ! -f "$NEXUS3_SCRIPT" ]; then
    echo "ERROR: $NEXUS3_SCRIPT does not exist."
    exit 1
fi

# Check that the data directory exists.
if [ ! -d "$NEXUS3_DATA_DIR" ]; then
    echo "ERROR: $NEXUS3_DATA_DIR does not exist."
    exit 1
fi

# Check that the nexus user exists.
id $NEXUS3_USER >/dev/null 2>&1
if [ $? -ne 0 ]; then
    echo "ERROR: $NEXUS3_USER does not exist."
    exit 1
fi

start() {
    # Start nexus3.
    echo "Starting nexus3..."
    su - $NEXUS3_USER -c "$NEXUS3_SCRIPT start"
    RETVAL=$?
    PID=`cat $PID_FILE`
    echo "nexus3 Started with PID $PID"
    return $RETVAL
}

stop() {
    # Stop nexus3.
    echo "Stopping nexus3..."
    su - $NEXUS3_USER -c "$NEXUS3_SCRIPT stop"
    RETVAL=$?
    echo "nexus3 Stopped."
    return $RETVAL
}

status() {
    # Check the status of nexus3.
    echo "Checking the status of nexus3..."
    su - $NEXUS3_USER -c "$NEXUS3_SCRIPT status"
    return $?
}

case "$1" in
    start)
        start
        ;;
    stop)
        stop
        ;;
    restart)
        stop
        start
        ;;
    status)
        status
        ;;
    *)
        echo "Usage: $0 {start|stop|restart|status}"
        exit 1
esac

exit $?

```

将脚本保存为 `/etc/init.d/nexus3`，然后执行以下命令使其可执行：

```plain text
sudo chmod +x /etc/init.d/nexus3

```

最后，执行以下命令将 Nexus 3 加入到开机启动项中：

```plain text
sudo chkconfig --add nexus3
sudo chkconfig --level 345 nexus3 on

```

这样，每次系统启动时，Nexus 3 将自动启动。


