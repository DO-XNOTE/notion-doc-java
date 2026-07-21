---
title: 1-14 【原理剖析】K8S认证授权原理剖析与实战
---

# 1-14 【原理剖析】K8S认证授权原理剖析与实战

[image](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/cda783df-1ace-4684-b85f-0b4ef07a9e5a/SCR-20240726-emij.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ULHNWXGD%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T225941Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQC62QCBvs0Y7vKw3fFl7zdkTWb1K4YiEY6aa917Y6yXIwIhANqYSxNTNxCxtVZ8RLtzFigAZZ9M7l4%2BDy7lmCVifE4hKogECMb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1Igw99hRHR9jDDUkMo%2BIq3AMS1keqErn4MgmA%2FVC9F%2FVQiYj4OhDMXefpnPb%2BrTw8n4jPuSCjWB9PXMrlh5n8EKiii%2FMa%2B8sgchr2yEATPtUpZbIU6nt6RsGVf%2BOXlqTRF0XkWnE8InrsLkikzTtssXOLWMdjTPchfrfqcseJH5SZ2iuTsWqDb9Y4egF11H7Ksv%2FDlYrsSNGqlAo4h1c6ZmQgEt6DGXcnVILqVOtZjZmWgytPCTOo0JjcFrAj3gFsytnGI2vxzdAIqnS4F8Zkxe%2B7cm%2F8qj0TWizSata1VeQtggcxQbUKJ8Igsk2%2FGgIly0gV%2BUkspxVn%2B2rIpHnkSh3o9n3ox1%2FyPqyNkmRnFtfbKre8Zh0u%2FZ3c9MxbfTAiznbJc2bWUwognuCiKAsZyEbOlffRUD6HUBoKQGBM7mWMMV5j6xBk%2BeTF4jLZlge0HBdAg5ljt9ju6PkhRnUnePK2vIZ4A1sQVm30Gzip0pABgCwJ2dlNm5jqlYvamZ%2B2mWID9nM1MS3E5EiszKubRaGUSs5qgIpvOTooqpmYeqlWU6DgIzmZGAjUaP%2FXHEzOMOplBG1HC3rWdtRIpppMjFcc9VFnspnyDg%2B0G4yZpmh11Py10nT4omyoTAbTElPwHdQ3WExf%2BPURFhVLGDDauv%2FSBjqkAX4yErcBFBxRpk0KZitTuLXclVMzZ%2BE9MWMtTJCKXl%2FNPpv2tpriy3busTVC1ouKmna4KwPJbwDaGgiMgIhmfMT69ADIv5TzFr4VYNDNvrvvUqrtPIVStQnBTppWA%2BJPRnLwI0aDZkKnDZGsYypvKoH7%2Flz25rcT9So%2BosJ2INtv6GC9nR%2FnqaUechZoySf90BWm4HYlcj3qpjvgv20SaWCTEZa7&X-Amz-Signature=d6243a13a46311c8fc228b584d5ecddb38363db2e7582a9322be8ff89e4592cb&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

[image](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/649f5fdf-e89e-4a89-a443-395bd435eae0/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ULHNWXGD%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T225941Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQC62QCBvs0Y7vKw3fFl7zdkTWb1K4YiEY6aa917Y6yXIwIhANqYSxNTNxCxtVZ8RLtzFigAZZ9M7l4%2BDy7lmCVifE4hKogECMb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1Igw99hRHR9jDDUkMo%2BIq3AMS1keqErn4MgmA%2FVC9F%2FVQiYj4OhDMXefpnPb%2BrTw8n4jPuSCjWB9PXMrlh5n8EKiii%2FMa%2B8sgchr2yEATPtUpZbIU6nt6RsGVf%2BOXlqTRF0XkWnE8InrsLkikzTtssXOLWMdjTPchfrfqcseJH5SZ2iuTsWqDb9Y4egF11H7Ksv%2FDlYrsSNGqlAo4h1c6ZmQgEt6DGXcnVILqVOtZjZmWgytPCTOo0JjcFrAj3gFsytnGI2vxzdAIqnS4F8Zkxe%2B7cm%2F8qj0TWizSata1VeQtggcxQbUKJ8Igsk2%2FGgIly0gV%2BUkspxVn%2B2rIpHnkSh3o9n3ox1%2FyPqyNkmRnFtfbKre8Zh0u%2FZ3c9MxbfTAiznbJc2bWUwognuCiKAsZyEbOlffRUD6HUBoKQGBM7mWMMV5j6xBk%2BeTF4jLZlge0HBdAg5ljt9ju6PkhRnUnePK2vIZ4A1sQVm30Gzip0pABgCwJ2dlNm5jqlYvamZ%2B2mWID9nM1MS3E5EiszKubRaGUSs5qgIpvOTooqpmYeqlWU6DgIzmZGAjUaP%2FXHEzOMOplBG1HC3rWdtRIpppMjFcc9VFnspnyDg%2B0G4yZpmh11Py10nT4omyoTAbTElPwHdQ3WExf%2BPURFhVLGDDauv%2FSBjqkAX4yErcBFBxRpk0KZitTuLXclVMzZ%2BE9MWMtTJCKXl%2FNPpv2tpriy3busTVC1ouKmna4KwPJbwDaGgiMgIhmfMT69ADIv5TzFr4VYNDNvrvvUqrtPIVStQnBTppWA%2BJPRnLwI0aDZkKnDZGsYypvKoH7%2Flz25rcT9So%2BosJ2INtv6GC9nR%2FnqaUechZoySf90BWm4HYlcj3qpjvgv20SaWCTEZa7&X-Amz-Signature=f600977a8a503095496026ed898aebaf0709ece936d6e3e21eb2f091eb4f3274&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

[image](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/1f779e48-62de-4f3b-a234-12005524d6f4/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ULHNWXGD%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T225941Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQC62QCBvs0Y7vKw3fFl7zdkTWb1K4YiEY6aa917Y6yXIwIhANqYSxNTNxCxtVZ8RLtzFigAZZ9M7l4%2BDy7lmCVifE4hKogECMb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1Igw99hRHR9jDDUkMo%2BIq3AMS1keqErn4MgmA%2FVC9F%2FVQiYj4OhDMXefpnPb%2BrTw8n4jPuSCjWB9PXMrlh5n8EKiii%2FMa%2B8sgchr2yEATPtUpZbIU6nt6RsGVf%2BOXlqTRF0XkWnE8InrsLkikzTtssXOLWMdjTPchfrfqcseJH5SZ2iuTsWqDb9Y4egF11H7Ksv%2FDlYrsSNGqlAo4h1c6ZmQgEt6DGXcnVILqVOtZjZmWgytPCTOo0JjcFrAj3gFsytnGI2vxzdAIqnS4F8Zkxe%2B7cm%2F8qj0TWizSata1VeQtggcxQbUKJ8Igsk2%2FGgIly0gV%2BUkspxVn%2B2rIpHnkSh3o9n3ox1%2FyPqyNkmRnFtfbKre8Zh0u%2FZ3c9MxbfTAiznbJc2bWUwognuCiKAsZyEbOlffRUD6HUBoKQGBM7mWMMV5j6xBk%2BeTF4jLZlge0HBdAg5ljt9ju6PkhRnUnePK2vIZ4A1sQVm30Gzip0pABgCwJ2dlNm5jqlYvamZ%2B2mWID9nM1MS3E5EiszKubRaGUSs5qgIpvOTooqpmYeqlWU6DgIzmZGAjUaP%2FXHEzOMOplBG1HC3rWdtRIpppMjFcc9VFnspnyDg%2B0G4yZpmh11Py10nT4omyoTAbTElPwHdQ3WExf%2BPURFhVLGDDauv%2FSBjqkAX4yErcBFBxRpk0KZitTuLXclVMzZ%2BE9MWMtTJCKXl%2FNPpv2tpriy3busTVC1ouKmna4KwPJbwDaGgiMgIhmfMT69ADIv5TzFr4VYNDNvrvvUqrtPIVStQnBTppWA%2BJPRnLwI0aDZkKnDZGsYypvKoH7%2Flz25rcT9So%2BosJ2INtv6GC9nR%2FnqaUechZoySf90BWm4HYlcj3qpjvgv20SaWCTEZa7&X-Amz-Signature=3925a66d136f60560a3ed6ea7ba70fe1fd549fc8a43d5e4e8d8dd8f4df042bb9&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

[image](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/8c7e4e7a-c087-4868-b35f-beea7fb4c7c2/SCR-20240726-epoc.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ULHNWXGD%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T225941Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQC62QCBvs0Y7vKw3fFl7zdkTWb1K4YiEY6aa917Y6yXIwIhANqYSxNTNxCxtVZ8RLtzFigAZZ9M7l4%2BDy7lmCVifE4hKogECMb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1Igw99hRHR9jDDUkMo%2BIq3AMS1keqErn4MgmA%2FVC9F%2FVQiYj4OhDMXefpnPb%2BrTw8n4jPuSCjWB9PXMrlh5n8EKiii%2FMa%2B8sgchr2yEATPtUpZbIU6nt6RsGVf%2BOXlqTRF0XkWnE8InrsLkikzTtssXOLWMdjTPchfrfqcseJH5SZ2iuTsWqDb9Y4egF11H7Ksv%2FDlYrsSNGqlAo4h1c6ZmQgEt6DGXcnVILqVOtZjZmWgytPCTOo0JjcFrAj3gFsytnGI2vxzdAIqnS4F8Zkxe%2B7cm%2F8qj0TWizSata1VeQtggcxQbUKJ8Igsk2%2FGgIly0gV%2BUkspxVn%2B2rIpHnkSh3o9n3ox1%2FyPqyNkmRnFtfbKre8Zh0u%2FZ3c9MxbfTAiznbJc2bWUwognuCiKAsZyEbOlffRUD6HUBoKQGBM7mWMMV5j6xBk%2BeTF4jLZlge0HBdAg5ljt9ju6PkhRnUnePK2vIZ4A1sQVm30Gzip0pABgCwJ2dlNm5jqlYvamZ%2B2mWID9nM1MS3E5EiszKubRaGUSs5qgIpvOTooqpmYeqlWU6DgIzmZGAjUaP%2FXHEzOMOplBG1HC3rWdtRIpppMjFcc9VFnspnyDg%2B0G4yZpmh11Py10nT4omyoTAbTElPwHdQ3WExf%2BPURFhVLGDDauv%2FSBjqkAX4yErcBFBxRpk0KZitTuLXclVMzZ%2BE9MWMtTJCKXl%2FNPpv2tpriy3busTVC1ouKmna4KwPJbwDaGgiMgIhmfMT69ADIv5TzFr4VYNDNvrvvUqrtPIVStQnBTppWA%2BJPRnLwI0aDZkKnDZGsYypvKoH7%2Flz25rcT9So%2BosJ2INtv6GC9nR%2FnqaUechZoySf90BWm4HYlcj3qpjvgv20SaWCTEZa7&X-Amz-Signature=0f65eb1fd664a7bd6cdb035677064f199809e5e8069dc2816619b6375faca537&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

好的，前面的章节我们介绍了库布内特斯的网络和它的存储。那这一章节我们重点介绍两个新的概念，一个叫认证，一个叫授权。同时我们还会有一部分实战来看一下。那库布内特斯它的很多的安全功能其实都来自于什么？来自于认证和授权。

[image](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/84388430-6c2b-4533-acdb-e29a692ed938/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ULHNWXGD%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T225941Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQC62QCBvs0Y7vKw3fFl7zdkTWb1K4YiEY6aa917Y6yXIwIhANqYSxNTNxCxtVZ8RLtzFigAZZ9M7l4%2BDy7lmCVifE4hKogECMb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1Igw99hRHR9jDDUkMo%2BIq3AMS1keqErn4MgmA%2FVC9F%2FVQiYj4OhDMXefpnPb%2BrTw8n4jPuSCjWB9PXMrlh5n8EKiii%2FMa%2B8sgchr2yEATPtUpZbIU6nt6RsGVf%2BOXlqTRF0XkWnE8InrsLkikzTtssXOLWMdjTPchfrfqcseJH5SZ2iuTsWqDb9Y4egF11H7Ksv%2FDlYrsSNGqlAo4h1c6ZmQgEt6DGXcnVILqVOtZjZmWgytPCTOo0JjcFrAj3gFsytnGI2vxzdAIqnS4F8Zkxe%2B7cm%2F8qj0TWizSata1VeQtggcxQbUKJ8Igsk2%2FGgIly0gV%2BUkspxVn%2B2rIpHnkSh3o9n3ox1%2FyPqyNkmRnFtfbKre8Zh0u%2FZ3c9MxbfTAiznbJc2bWUwognuCiKAsZyEbOlffRUD6HUBoKQGBM7mWMMV5j6xBk%2BeTF4jLZlge0HBdAg5ljt9ju6PkhRnUnePK2vIZ4A1sQVm30Gzip0pABgCwJ2dlNm5jqlYvamZ%2B2mWID9nM1MS3E5EiszKubRaGUSs5qgIpvOTooqpmYeqlWU6DgIzmZGAjUaP%2FXHEzOMOplBG1HC3rWdtRIpppMjFcc9VFnspnyDg%2B0G4yZpmh11Py10nT4omyoTAbTElPwHdQ3WExf%2BPURFhVLGDDauv%2FSBjqkAX4yErcBFBxRpk0KZitTuLXclVMzZ%2BE9MWMtTJCKXl%2FNPpv2tpriy3busTVC1ouKmna4KwPJbwDaGgiMgIhmfMT69ADIv5TzFr4VYNDNvrvvUqrtPIVStQnBTppWA%2BJPRnLwI0aDZkKnDZGsYypvKoH7%2Flz25rcT9So%2BosJ2INtv6GC9nR%2FnqaUechZoySf90BWm4HYlcj3qpjvgv20SaWCTEZa7&X-Amz-Signature=aea0ef56bd4d6796da7d0c9f65c0a14c0af997a112308ae48d9c9ebb4505ffea&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

大家记得前面介绍的几乎所有命令都是通过 coupe ctrl 我们的命令客户端把他的这个需求发送到我们的什么中间这个模块 coupon native 的 API server 来实现所有命令的解析。然后再转发给后面所有的那些调度模块，再转发给 no 的节点。 Couplet. 最后再实现我们容器的调度，对不对？是这样一套整个框架。那这样整个框架里面，其实什么整个这种命令的执行都会经过 API server 所以 API server 成为安全的一个最核心的模块，它来完成用户的认证和授权以及一部分的权限的额外的控制。


那我们首先来讲一讲什么叫认证，什么叫授权，这是安全领域两个非常重要的概念。认证就是说明你是谁，并且证明你是谁。那首先要说明你是谁，就是比如说我说我是张飞扬，然后你要证明你是谁，那证明你是谁呢？在安全领域通常有三个方法，一个方法是什么？一个方法是我特有的一些特征，比如说我这个脸型是怎么样，我的这个眼睛的虹膜是怎么样？这是你特有的特征，证明你是谁。
另外一个方法是我知道的一些信息。比如我知道我常用的密码是什么，我知道这个系统的密码是什么，它也能证明你是谁。另外还有一个信息是我拥有，就是比如我才有这个钥匙，我才有 RSA 的这个认证密钥，这套动态认证密钥或者是一个静态已经打磨好的一个金属钥匙，这些东西都能够只有我才拥有的，别人没法拥有或者说别人没法同时拥有。那这三点可以证明你是谁，加上你说明，再加上你是证明完成了，就是 authentication 左边的一个大块。那 authentication 完了以后，是不是我是张飞扬。然后我就可以把所有 coupon 集群随便重启，应用随便下载其实不是的。


还有一个 authorization 的过程，就是我知道你了以后，我来判断你应该拥有哪些权限。比如你可以管我们什么 cooker 集群对不对？但你不能管底下的虚拟机。这个虚拟机是由语音托管的，只有语音的管理员才能来管理，所以这就是 authorization 那后面的 admission control 其实是什么？是我们 coconities 额外增加的概念，它意思应它重要是强调说我们在资源管理上面还有更多的一种补丁式的方法，能够实现更灵活更随机的更 on demand 按需的一种操作。


那我们认证和授权的核心什么是两种用户群，一种叫普通的 user 还有一种叫什么 service account 好，那我们仔细来看一看这认证的这个最核心的点。认证最核心的点，就刚刚说的一个普通的用户 user 那什么是普通用户呢？其实就是 Linux 里面的系统用户，你这个系统用户可以是 root 吧，权限很高很高，你可以是一个很小的小用户。那这些用户其实我们在 coconities 里面什么并不理解它。所以如果要让这个用户能够访问口播 andes 或者说是能够实现一部分的具体的认证功能，我们的下一页会重点讲怎么样给这个用户实现一部分的认证，证明他是真的这个用户，然后再给这个用户进行授权。


除了这个用户以外，其实用的最多的什么是 service account 服务账号？那用户有个特点，什么？用户通常他的密码，他的一些信息是这个人所特有的，但它不是系统和系统之间沟通的一个好的方式，也不是一个职责的人员和系统之间沟通的一个好的方式。


通常系统和系统沟通是什么？我用一个特殊的 service account 来代表我这个系统，比如说我们有一个专门的云平台监控器，那这个监控器最好有一个 service account 来代表它。所有登录这个监控器的人都会用同样这一个 service account 来跟我们的 kubernetes 的集群的 API service 来进行沟通。这样就可以什么可以使用一套 service account 来给更多的用户实际操作用户来使用。因为当他登到这特殊的这个控制台的时候，它其实有一个相类似的职责，有个相类似的什么权限，所以对一个 service account 来授权会更加简单一些。所以后面我们的这个 demo 也会以这样，课程也会是以 service account 为主体来进行介绍。我们也希望其实在我们的生产中心尽量少用 root 少用普通用户，我要更多的用什么用我们的服务账号。


好。那下面第二个问题是什么？是认证过程当中是吧？你其实是说明了你通过 user 跟 service account 说明了什么，我是谁，但是怎么证明可以用什么客户锻炼这个证书，比如 x509 CI 认证这样一套这种资料。对的证书能证明，因为你有你的私钥，能证明你自身就是这样的一个人。另外还可以通过一些最简单的用户名密码放到一个文件里面做什么静态密码文件也能够勉强证明你是谁。那这个是很不安全的一个方法，通常不推荐。最推荐的是什么是 tokentoken 相当于什么是一个比较动态的证明方法，来一个信令或者说是一个特殊的小的密钥这种性质的东西来证明你是谁。 token 里面其实有很多很多种，而我们库珀莱特斯接收了大部分的不同的类型的 token 比如说有一个叫 token fun 这个文件里面你可以拿出什么从中提取出它动态的那个信息，这是支持的。另外你记住它的 token 然后你用什么 bearer token 进行传递，也是支持的。


还有就是 service count 最常用的什么 service count 会把它 token 记在一个叫 secret 里面。那这个这个 secret 文件就是之前我前面介绍过了存储里面什么存储信保密信息，通过我们的这个特殊编码方式编码以后的这个保存下来这个内容。这里我们可以把 token service account token 揣在它里面，对 service account token 也是我们后面实战里面会重点看的一个内容。


那除此以外，非常推荐用什么用 JWT jot Java web token 现在很多公司，比如像谷歌，我们像那个 Salesforce 他们都会推荐什么采用 open ID connect 方式进行 authentication 采用 O auth two 是吧 gwt 的方式进行 authorization 那这种一整套这种什么 open ID 加 O auth two 的方式已经越来越多的什么给我们的单点登录 SSO 使用给我们的多账号系统或者说多应用系统的这种账号统一管理或者说第三方认证登录等等功能使用越来越多的这个托克向 JWT 向靠拢。所以我们也建议我们在实际生产当中可以尝试去复杂化一些，把我们 JWT 的环境搭建起来，然后用它来完成我们 search count 的认证。除此以外还有一些比如其他的认证，比如像 web hook 这种就是靠客户端的服务器来完成 token 的认证。那我们这里就一带而过。


好，那假设证明完了以后，我们现在开始授权了，怎么样才能合理的授权呢？大家可以想象，我们要授权什么？我们要授权有一些 port 能不能启停，是不是我们要能授权一些 node 是不是能够被控制？同时我们要授权一个 name space 是不是能够被创建、被删除、被查询？我们要授权一个 deployment 能不能被修改？有很多很多的这个不同的资源要被管理，同时对这个资源有很多很多的操作方式，还有各种各样的 API 是吧。


我们有的 API 是 API version one 有的是 version two 有的是 batch vy 有不同的 API 那这么复杂的一个过程，是不是每个用户每个 service 杠都要这样授权呢？当然是否定的什么，因为我们授权的方式其实可以参考信息安全理论里面的。
你可以用什么？用强制安全授权管理 access control Mac 就 mandatory access control 也可以用什么民主安全控制？那更多的歧视什么是采用什么 row base access control 就是基于用户角色的方法来进行控制。


为什么这样一个好处呢？因为如果你有 100 个账号，然后你会登录不同的机器，这时候你会体现出很多很多复杂的 service count user account 但是我们其实就两个角色，一个比如说是管理员，一个是普通用户。那这个时候管理员可以定义我们管理员可以修改 POD 可以修改 deployment 但是不能删除 node 只能读 node 比如说这样一套功能。那我们普通用户全读它只能读 secret 只能读 name space 完全不能做修改。那这样很简单的配置两个人偶角色以后，那就把所有的其他各种账号一一和他们对应，就可以很方便的完成一大批的资源呐一大批的权限的管理。对 role base control 1 简化了我们的管理流程。


2 把更多的这种管理集中化到我们的统一的中心，来进行一个集中化的处理。那刚刚已经提到了 rowrow 是什么概念？ row 是一个角色，它是对一批资源的权限的一个统一的注解。比如说我们刚说 admin 就是对很多资源都有写权限，部分少数资源比如像 no 的资源才只有读权限，这样它是一个统一的整体。我们可以比较随意的定义我们的row。定义完了以后，我们就可以把一个 service count 或者一个 user 和这个 row 进行对应。但是这里要注意一点， row 什么一个 row 在我们 kubernetes 里是不能超过 name space 因为 namespace 是一个什么虚拟的我们 kubernetes 集群。而 row 是在一个虚拟 kubernetes 集群里面的。那前面刚刚忘了聊了，就是 service count 也是一样，当你建立一个 service count 的时候，你也不能超脱于我们的这个 name space 之外。但是我们为了简单起见，假设我们一个 connect crust 有 100 个这种 name space 但同时他们都非常接近。这时候其实我们建几个 cluster row 就可以了，不用每个 name space 都建 row 那右边这张图可以很好的说明这个问题。


那假设我们有一个用户，我们鼠标移除了，有用户他想让他绑定一个特殊的肉，那他就可以直接用什么 roll bound bending 的方法去跟这个肉绑定。当 roll bending 建立好以后，这个 user 就跟这个肉有一绑定关系，但它同时也可以建一个 cluster row 这 cluster row 就可以跨越很多很多个 name space 它就可以跟这个 class 的 row 绑定。如果有大量用户都想绑定同样一个级别的 row 那时候就不需要在每个 name space 里面都建这样一个 row 而可以什么集中化的建一个 class row 对 class row 可以理解为一个概念，简化管理 row 其实已经是对用户和权限的简化管理，让 class row 进一步简化了我们跨 name space 的重复，很多重复工作可以用卡死肉来代替。


好我们讲完这一些以后，下一节会讲什么？ CRA 的关键点就是机密管理、完整性管理和可用性管理。在讲下一章节之前，我希望我们把大部分的实战内容都在这一章节完成。下一章节我们可以有比较随心所欲的来介绍一些安全的理念好不好？那我们就进入实战环节了，看看怎么样去创建一个 search count 怎么样去创建一个 row 怎么样让 six count 跟 row 之间进行互通，同时怎么样我们来演示一下。


就如果已经创建好了这样一个有特定用户权限的 service account 怎么样去登录我们一个 dashboard 的系统，浏览我们整个库内 S 集群好不好？这是一个实际的小演示。那我们先切换到命令银行界面、运营行界面，我们在使用这个 row best control 之前，其实大家想一想，其实不是每一个应用或者说每一个 kubernetes 集群都会 enable 这个 role base control 所以我们首先要看一下我们这个集群有没有 enable 好不好？那么看是用这个命令，我们看一个文件就是 cut etc kubernetes 我们的那个整个 kubernetes 其实跑的是这 kubernetes 这个目录底下的一个 manifest 文件，下面有一堆的 manifest 我们重点看 API server 所以就是 coupe 稍等一下 API server 我们看一下它的羊毛文件，它原文件内容很多，它有点太多。


我们首先 grape 一下 auth authorization 这个部分。好，我们 grab 出来的结果是什么？ authorization mode moderation mode 什么是 node 就是由每个 node 来做 authorization 同时它 enable 了 IB AC role base access control 很好，那我们当前这个 kubernetes 已经可以做 role base control 了，通常我们用什么我们用 cube admin 这个命令也是我们之前介绍的集群搭建当中主推的这个方式，用全自动的方法创建出来的。这个 coupon net is 里面会自动激活我们的 role base control 会方便大家对什么安全的管理。那好我们现在开始要创建一个 source count 创建一个肉，然后把这 source 看跟肉绑定起来。因为相对内容比较多，所以我这里提前其实已经把我们的这个羊毛文件写好了，而且我这里要重点介绍一下这个羊毛文件叫 mysa.yaml 但它其实干的不是一件事，而是三件事来看一下。


这里我要重点介绍一下这个三横杠顶格。三横杠是个特殊的含义，表示什么？表示我其实把多个羊毛写在一个羊毛文件里面，然后把这些内容分隔开来。那比如看三横杠之前，第一段说什么？第一段说我要用调的 API version 是 V one 就是最基本的 API version 然后我要起一个什么叫 service account 我创建一个 service account 它的名字是什么？它的名字叫 mysa myservice account 的缩写，就是说我比较简单提前取的一个名字这个 mysa 就是一个 service account 如果你直接把这段小内容创建成一个 YAML 文件，然后去 apply 你就会创建一个 service account 他在我们这里会把三件事一起做。


通常我们其实可以看到很多的网上下载的一些大型项目里面都会这样，把紧密相关的几个牙保文件合成一个中间用三横杠，三个什么短的减号实现分隔。好，我们再看第二个部分第二部分是什么？他说我是 role best control authoration V one 这样一个 API 然后为了什么我要创建一个 row 这个 row 的名字叫 mysa 横杠 row 它下面有一堆的规则对吧，这 row 的规则首先对所有 API 它这里什么信号，信号这里是双引号表示什么，我不具体区分你到底是 apivyv 特什么，我不管这些都可以操作。然后我们看具体 sourcesource 里面。他说了，我先只能对 poll 进行合理的操作。对其他的一些 node 这种节点你可能还不一定有权限。然后它动作是什么？动作是可以读，可以查，可以仔细监控。说白了就是什么是一个读状态，我可以读很多信息。


我这个 account 刚刚这一段，上面一段是会什么？如果 apply 完以后会生成一个 service count 中间一段 apply 完以后会创建中的 row 但是 row 和 service count 间是怎么样对应关系呢？怎么把我们什么 mysa 这个 service count 和我们 mysa row 对应起来呢？就是下面那个内容往下翻页，我们就会看到最关键的那个内容就是什么？就是一个叫做 role binding 的类型，我们还是基于什么 RBAC 的 V one 这样一个 API group 里面，我们采用 role binding 的方式，或者说是这样一个类型的功能来把我们刚刚创建的这个对象是什么？是一个 service account 哪个 service account 呢？ mysa 这个 service account 和一个 row 一个什么在 API 国谱是 rbsa 里面定义的一个 row 这个 row 的名字叫什么叫 mysa row 是不是就上面那两个这两个子牙帽文件所生成的内容把它对应起来。


对应完了以后，我们把这个对应叫什么叫 mysa row binding 好，那这些名字其实只要上下对应就可以了，名字可以有出入就是这里可以不写 my SN body 你我可以写 my service account role body 完全可以，或者我这里就写 my service account 也可以。但是如果这样写，你上面那个地方 service count 就是这样往上走，你上面那个 service account 这里就也要 my service account 要一一对应。


好，我们这里不做修改整个内容。其实我们刚刚已经看过了，我们既建了 service count 也建了 row 也建了 road 跟 service count the binding 我们直接扩不 control apply 它 F my SA D 两毛。好可以看到什么。他做了三件事，他告诉你了，分别按顺序做 service count 下面的 my S A 创建出来，基于我们的这个 API group 下面的什么 mysa row 创建出来基于什么 role binding 很复杂，我们 API 底下的那个什么 mysa role binding 这个 role binding 建立出来。


那他们建立什么环境呢？它们今天在 default name space 因为我们没有指定 name space 所以它就是 default name space 那这个环境建完以后，我们查一下 group CT 2 对吧，我们 get 一下 service account 的缩写，然后不写 name space 就是 default 我们看一下是不是建出来了对不对？除了我们 default 的 service count 还建了一个新的叫 mysa service count 然后这个 service account 你要使用它，其实你可以想象到它可以对大部分 node 进行查询，对不对？我们这里其实起了一个特殊的 POD 叫 dashboard 它是一个图形化界面。我们就以这个图形化界面为例，我们去切过去看一下。


我这已经打开网页了，这已经登录到这个 dashboard 我们在下章节会详细讲怎么样安装个 dashboard 装完以后，你可以在公共网通过我们整个节点对外的这个公网地址和指定端口来访问。他访问完以后，他会首先让你说我这个 dashboard 你是默认有一个普通用户登录的，但这个用户登录的时候我不知道这个用户信息，我又不知道他的权限。那有两种方法传递，一个是传递一个 coupconfig 一个 config 文件过来。


另外一个，你给我个 token 就 token 里面会有什么？会有那个用户的 ID 对不对？或者是它的一个邮箱地址，同时也有它的一个基本的 road 信息。它是什么？它是一个专门的在 API server 上签名过 token 只要我们 resource server ，我们验证它用它的公钥来验证它具体机制包括 token 一些信息内容，我们会在后面的章节详细介绍。


根据这种 token 机制，只要你传这个 token 的具体值我就可以什么，我就可以知道你是哪个用户，你有什么样的权限，你是不是能查看我们检 coupness 集群。那我们现在就是尝试我们把这个 token 的值给找出来好不好？刚刚的那个什么？刚刚那个 count 是可以查各种 pot 的，所以完全可以执行相关的内容。我们现在只要能够找到他的这个 token 就跟我们之前介绍的一样，这个 token 会藏在哪里呢？会藏在一个叫 secret 的这样一个模块里面。我们看一下，不写 name space 就是什么，就是 default 我们找一下有没有找到一个样子很样像的 mysa token 对不对？我们刚刚整个 service account 不是就 mysa 嘛，它就会在 service account 后面补一个杠 token 然后再补一个随机的这个五个字符。


这个 secret 就是唯一的为我们的自己刚刚创建那个 service count 提供密钥的管理来提供 token 的管理。对，它是当我们创建 service account 的时候， secret 就会产生，当我们删除 service account 的时候，这个 secret 就会被自动删除。那怎么样呢？查询这个token ，我用这个 coupe ctrl describe 它去描述。这个时候我们要提示一下我们描述的是一个 secret 或者说我们查询的是 secret 然后这个内容的名称对不对？好，我说看到没有好长一串 token 已经自动跳出来了是吧，他告诉你什么它是一个 service count 的 token 我们直接把整个复制下来，这就是一个他的token ，我们把这个 token 填在我们的这个 talk 里面复制进去。好需要保存的我们等等，看看它能不能够。有点慢是吧，是不是了没有进去了？同时沃克搂的 status 都看到了，下面炮的信息都看到了。为什么？因为我们给他提供了一个什么能够查询我们 POD 资源的这样一个账号这样一个 service count 同时我们又通过这个 service account 的 token 输入到了我们这个 dashboard 里面，从而以这个 service account 的用户的这个状态经过了 authentication 的验证，最后采用 RBAC 的方式授权给他完成相应的操作。


好，回过我们的PPT ，我们这里刚刚介绍了什么，介绍了我们的什么 authentication 对吧，通过 token 的方式，通过我们的这个设计 count 方式实战了一把 authentication 也有 rb S 的 authoration 我们可以访问 POD 里面的什么 list 可以做什么 watch 我们可以查很多的信息。


最后其实定制化这部分 admin mission control 没有展现，其实也类似的，就是最主要的功能其实就是 authentic 和 authoration 最后实现了对所有资源、对 API 的合理的什么一些 behavior 一些操作。好，那这一段认证和授权就到此为止。后面我们会重点讲一讲我们在 kubernetes 上面去实现 CIA 安全三元素。好，谢谢大家。


