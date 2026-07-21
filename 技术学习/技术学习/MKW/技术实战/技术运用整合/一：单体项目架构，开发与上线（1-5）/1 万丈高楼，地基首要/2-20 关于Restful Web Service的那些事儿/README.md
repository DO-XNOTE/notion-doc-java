---
title: 2-20 关于Restful Web Service的那些事儿
---

# 2-20 关于Restful Web Service的那些事儿

[image](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/42057b8f-5e1a-4bfa-9b60-87983ba7b7cc/SCR-20240816-qdxn.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466U6D2V7PS%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T224614Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIEG9griMFTkg%2BPjUinmWY7dHv3KwfupgrXeAMrZHOeAZAiAk4MOMBmtwZXklRr2gqDcKbJxQWObHRLWIq5JaeMriDSqIBAjG%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMsE2jDXNMYyQ0A9s5KtwDZHg%2BMlggngmvK05%2F5lXleeJNR5LDaGWSq22ZStht190rgDMlbnBsM6zeiiXbqHfMQvp0rhEVCQhcv29s3NxcKNOxZ8ClUHM9u4vOjQCOmYN9O3ecTFS2aTEvMadDie1p%2BC6Um8vsoCdAVx1LRLnJUoJzQqE7ij8u4bDHQivOa1MSAZiMwb1Ym9%2BK%2FKdDVdlGn%2Bg9aP0FEDCMY6jlx%2Fez5LxdlctGl4PpHqhgb66wKkAfshxlb8tlmoK%2BmxMmQvA9V3Vfgtnutio8X9L%2F8ZVatvwjEzrpVrTPM0aq3nGILLE3XWqVE%2FEJw4qCkK%2BcyyaqpH51tkmfZKdwFw9ntpVELjXSPpAgicHh9D4I1q0ROB2UDtQibbzrid88Ok18I7%2Fiy%2FZq8sD5R8I%2FGYBYfsTASPtweG312zUu%2BkAwK4byhEVGxXv7q%2BWt3EWaGPE1W90eJCurztHc6isWgk%2BRUReVLyLEPXJrNmC3Bl3F%2BBnYY8gUyWKBrezkvHFU1WvN%2BZk52KtSou5X60OPY2E5fdNMVlPvUl5sA%2Bl793QxwOlUE3mQ6HTqiz5e935kG%2F1%2B4uuM8l%2BEg5DuFITcSh9NsVxNpXBhStsazmG0ttvSbkWy8217RGNUodQaXyKo7tYwgbf%2F0gY6pgHaTFtGgmI9kxhKU4E%2Fbfk2rLbxto9dywJLimGKdVKctf5Mo0ofxtYaEG%2BahgAp1U9B0Y4fcGvgnie5xPZ8kSLbpLXQUVk8zhlIBcWij7nL%2BNVP5sogpPxPw1rimuoL3si8TT9dS7RDEkwk%2BYIKuZtzRuYqKi8Y0n2cx2JdmzjtPy2xJaOXrbqj%2FC5MrW4c6h5zlsTL8LW6gEPY9wPiRZTAZwxOCPAE&X-Amz-Signature=60ffa411c54c0996d2eaed7cfdda4761d4f977a36b5304f8437a77906ded1c54&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

前面几小节我们是针对咱们的数据层做了一个整合，接下来我们来聊一下 Restful web service。其实是在接口层，也就是对外提供 API 的所涉及到的内容。为什么要来聊一下 Restful ,因为其实主要在绝大部分的一些互联网企业里面都会使用 rest of web service，但是有一部分小伙伴其实都是在一些传统的企业里面在做，所以 restful 可能用的并不会很多。在我们正式的开始咱们的项目之前，我们也是需要针对 restful 来简单的过一下。因为我们在后续所有的一些接口层，我们所对外暴露的一些接口全部都是 restful web service。

[image](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/97e36e99-de70-4910-ab0d-ff81a68abb41/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466U6D2V7PS%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T224614Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIEG9griMFTkg%2BPjUinmWY7dHv3KwfupgrXeAMrZHOeAZAiAk4MOMBmtwZXklRr2gqDcKbJxQWObHRLWIq5JaeMriDSqIBAjG%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMsE2jDXNMYyQ0A9s5KtwDZHg%2BMlggngmvK05%2F5lXleeJNR5LDaGWSq22ZStht190rgDMlbnBsM6zeiiXbqHfMQvp0rhEVCQhcv29s3NxcKNOxZ8ClUHM9u4vOjQCOmYN9O3ecTFS2aTEvMadDie1p%2BC6Um8vsoCdAVx1LRLnJUoJzQqE7ij8u4bDHQivOa1MSAZiMwb1Ym9%2BK%2FKdDVdlGn%2Bg9aP0FEDCMY6jlx%2Fez5LxdlctGl4PpHqhgb66wKkAfshxlb8tlmoK%2BmxMmQvA9V3Vfgtnutio8X9L%2F8ZVatvwjEzrpVrTPM0aq3nGILLE3XWqVE%2FEJw4qCkK%2BcyyaqpH51tkmfZKdwFw9ntpVELjXSPpAgicHh9D4I1q0ROB2UDtQibbzrid88Ok18I7%2Fiy%2FZq8sD5R8I%2FGYBYfsTASPtweG312zUu%2BkAwK4byhEVGxXv7q%2BWt3EWaGPE1W90eJCurztHc6isWgk%2BRUReVLyLEPXJrNmC3Bl3F%2BBnYY8gUyWKBrezkvHFU1WvN%2BZk52KtSou5X60OPY2E5fdNMVlPvUl5sA%2Bl793QxwOlUE3mQ6HTqiz5e935kG%2F1%2B4uuM8l%2BEg5DuFITcSh9NsVxNpXBhStsazmG0ttvSbkWy8217RGNUodQaXyKo7tYwgbf%2F0gY6pgHaTFtGgmI9kxhKU4E%2Fbfk2rLbxto9dywJLimGKdVKctf5Mo0ofxtYaEG%2BahgAp1U9B0Y4fcGvgnie5xPZ8kSLbpLXQUVk8zhlIBcWij7nL%2BNVP5sogpPxPw1rimuoL3si8TT9dS7RDEkwk%2BYIKuZtzRuYqKi8Y0n2cx2JdmzjtPy2xJaOXrbqj%2FC5MrW4c6h5zlsTL8LW6gEPY9wPiRZTAZwxOCPAE&X-Amz-Signature=bae3277f4278a1236f7fc0ba3dcf0ec9d9c8c8ac500f91f3c837ee5a0297aa29&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

首先来看一下什么是restful，其实它是一个通讯方式，通讯方式其实是有很多，其实最常见的有一个 RPC  通讯。在我们的 web service 里面，其实还有一种叫做 restful 这种风格的。在很早以前，其实还有一种 web service，这种 web service 调用起来其实相对来说会比较重，所以又出现了一种新的形式，叫做restful。它在系统和系统之间其实是可以相互传递相应的消息的。比方有系统 a 和系统 b 和系统c，它们之间是可以通过 restful 相互通信。


此外，像我们现在主流的一些手机端，不管像是iOS、安卓还是小程序，另外还有是H5，其实相对来说，这些内容我们可以统称为客户端，客户端和我们的服务端在去进行通信的时候，我们也是可以使用 restful web service 的。通信的时候不仅仅只是通信和调用，我们必然会有一种信息的传递，会有一些相应的载体，这些内容。这些形式在很早以前是叉Mar，也有一些文本 text 在我们现在最流行，最主流的都是一些 JSON 的文本，我们是使用 JSON 进行传输。当然回调有一些通知过来的时候，我们获得的一些信息也都是JSON。


OK，下一个是一个无状态，其实是 restful web service。它的一个特点。服务器在接收客户端的一些请求的时候，其实对于我服务器来讲，我是没有必要去了解 request 之前所做过什么，它将来可能做什么，其实我是没有必要去制造它的一些以前或未来的信息的。所以也就是我们所请求的一些内容，对于接口来讲，它是一种无状态的，OK。


在我们后面的课程里面，我们会讲到分布式绘画，也就是无状态绘画。这这个 session 其实也都是一些无状态的。因为在我们的一个默认的单体单机环境里面， session 会话它是存在的，存在就代表它是有状态的。所以在这里我们是需要去进行一个区分，只要是 restful web Service，我们所有的请求都是无状态的，OK。


最后一个动画是一个独立性，当我们的系统使用 Restful 以后，其实也就是间接的代表。我们当前有很多的系统都进行了一个拆分，拆分以后，系统和系统之间首先一个是解耦了，并且它们系统之间是相互独立的，所以这就是一种独立性。当系统之间是需要去进行调用，我们就可以使用 restful 这种形式的 web service 去进行相互调用了。有些系统之间通过 RPC 通讯也是没有问题的。


OK，随后我们再来看一下 restful web service 的一个设计规范。

[image](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/8fca5c25-5bd4-4909-994a-2d64bfd8267c/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466U6D2V7PS%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T224614Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIEG9griMFTkg%2BPjUinmWY7dHv3KwfupgrXeAMrZHOeAZAiAk4MOMBmtwZXklRr2gqDcKbJxQWObHRLWIq5JaeMriDSqIBAjG%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMsE2jDXNMYyQ0A9s5KtwDZHg%2BMlggngmvK05%2F5lXleeJNR5LDaGWSq22ZStht190rgDMlbnBsM6zeiiXbqHfMQvp0rhEVCQhcv29s3NxcKNOxZ8ClUHM9u4vOjQCOmYN9O3ecTFS2aTEvMadDie1p%2BC6Um8vsoCdAVx1LRLnJUoJzQqE7ij8u4bDHQivOa1MSAZiMwb1Ym9%2BK%2FKdDVdlGn%2Bg9aP0FEDCMY6jlx%2Fez5LxdlctGl4PpHqhgb66wKkAfshxlb8tlmoK%2BmxMmQvA9V3Vfgtnutio8X9L%2F8ZVatvwjEzrpVrTPM0aq3nGILLE3XWqVE%2FEJw4qCkK%2BcyyaqpH51tkmfZKdwFw9ntpVELjXSPpAgicHh9D4I1q0ROB2UDtQibbzrid88Ok18I7%2Fiy%2FZq8sD5R8I%2FGYBYfsTASPtweG312zUu%2BkAwK4byhEVGxXv7q%2BWt3EWaGPE1W90eJCurztHc6isWgk%2BRUReVLyLEPXJrNmC3Bl3F%2BBnYY8gUyWKBrezkvHFU1WvN%2BZk52KtSou5X60OPY2E5fdNMVlPvUl5sA%2Bl793QxwOlUE3mQ6HTqiz5e935kG%2F1%2B4uuM8l%2BEg5DuFITcSh9NsVxNpXBhStsazmG0ttvSbkWy8217RGNUodQaXyKo7tYwgbf%2F0gY6pgHaTFtGgmI9kxhKU4E%2Fbfk2rLbxto9dywJLimGKdVKctf5Mo0ofxtYaEG%2BahgAp1U9B0Y4fcGvgnie5xPZ8kSLbpLXQUVk8zhlIBcWij7nL%2BNVP5sogpPxPw1rimuoL3si8TT9dS7RDEkwk%2BYIKuZtzRuYqKi8Y0n2cx2JdmzjtPy2xJaOXrbqj%2FC5MrW4c6h5zlsTL8LW6gEPY9wPiRZTAZwxOCPAE&X-Amz-Signature=933241587874a2474937aac2759a0096b6556b4bca75feaa9837289797d92be5&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

首先看一下 get get 其实我们在很早以前，在单体或者是一些传统项目里面， form 提交里面有一个method，就是get。此外还有是一个post，这两个其实我相信大家用的是最多的。或者在 url 里面进行请求就是一个get。通过 form 提交，我们可以把请求改为post，是两种不同的方式。在 restful 里面，其实 get 它的意义主要是用于去代表是获取资源信息的，去获取一些相应资源的内容，也就是一个查询的操作。对于 post 来讲，它其实是应用于去保存或者是更新一些资源的信息，也就是保存信息和更新资源。当然它也可以去处理一些批量的操作。


随后是一个put， put 主要是用于去做更新资源的。另外还有 delete, delete 从字面意思上就能看得出来它是做删除操作的。随后我们再来看一下，当我们要去使用这些不管是 get post 还是 put delete 这样的一些请求的时候，我们要去定义一下它的一个请求路由的规范，比方 get 我要去获得一个资源，我们就以 o 的订单为例，我们就会在 URL 里面这个路径，我们会写上一个 o 的斜杠ID，用于去代表请求与资源信息。随后  Post 我们就直接写一个斜杠order，相应的一些订单信息，我们会构建一个 JS 对象，把 JS 对象传递到后端，让后端接收到以后再去进行一个处理，这个可以用于去做一个保存的操作。


随后第三个是更新，更新我们从 UI 看得出来，和 get 其实是一样的，它就是根据 ID 把当前订单的一些信息做一个更新。当然还有delete，删除，根据 ID 去进行删除。从这里面看得出来，get、 put 和 delete 它们三者的 URL 其实都是一模一样的。


OK，这个是 restful 的一个规范，要尽量设计的简洁。并且它还有另外一个规范，就是在我们的 url 里面，我们是不能够出现一些动词的，需要出现一些名词。可能我们在平时的开发过程中会遇到一些像pay、 refund 付款，还有是退款这种操作，但是对于它的规范来讲，你需要把这些动词改成名词。


都是 restful 里面的一些设计规范，我们会有一个。但是在我们自己开发过程中，我们以我自己所在的一个企业为例，其实我们的一个平时的程序员比较忙，不仅要去思考代码，写代码，还要去思考业务。在这里，当我们如果现在有这几个 URL 拿过来，我们要去跟前端人员进行对接。对于他们来讲，当他们看到这样的一个 url，肯定不可能知道你  url 是用来干嘛的，因为你没有提供市面上的一些内容。比方我就以一个配来讲，斜杠 o 的斜杠 pay 就代表我当前要去做一个订单的支付。我们没有这种情况，没有这种 URL 和任何人去对接的。你必须要提供一份文档。如果你没有文档，就必须要去看一下代码。你要去看一下代码是 get 还是post，还是 put 还是 delete 是哪一种请求。如果从请求里面看不出来，你甚至还要去看一下代码。当这种情况发生了以后，就会影响到我们的一个开发效率。


OK，所以我们并没有十分的去遵守 Restful 的规范，我们只要保证自己写的接口是 Restful 形式的接口就行了。规范不规范是人可以去控制的。OK。所以对于这样的规范，你是否要真正的执行去遵守并无大碍。所以我们在这边又会有另外的一种风格。比方我们来看一下。当我们要去请求一个订单的信息去做查询，对于订单的接口，我们会写成 get all 的问号 ID 等于多少。当然这个 ID 我们改成一个斜杠，以一个 ID 的占位符去请求，作为一个路径参数也没有问题。这样子其实我们就可以从当前的 URL 里面看得出来，这个接口是用来干嘛的，一目了然的。所以你再去把这样的一个接口提供给其他人员去做开发的时候，就可以减少很多的沟通成本了，这个是非常有必要的。


只有第二个是保存一个订单。现在我们就不是直接去写一个 order 了，你直接写一个 order 可能会对一些人造成一些困扰。你这个 order 到底是一个什么意思？尤其是一些新人，有一些新入职的小伙伴，刚刚接触这种restful，其实会非常的困扰，很多时候会写错。但我们现在在这里写了一个 saveOrder  的，我直接一目了然，就知道这个就是用于去做保存的。

随后 put , put在这里我们就直接写上一个 modify order，修改订单，随后传一个 JS 对象就可以了。当然我们的 delete 删除操作就可以通过 delete order 来一个问号 ID 等于多少就可以了。这些其实我们从最右边的  url 就可以非常的直观，非常的一目了然了。


OK。所以在我们后续的一些 API 结构请求里面，我们大多都会是以这种形式这种风格去写。并且我们绝大部分都只写 get 和 post 这两种请求。 put 和 delete 其实我们也可以自己去斟酌，你可以去写，你可以不写，都没有问题。对于所有的查询操作来讲，你都可以写get，对于所有的保存、删除、更新操作都可以写post，放到 post 里面也是没有问题的。OK，以上这一节就是我们针对 restful web service 所做的一些相应的讲解，另外还包含了一些设置规范。如果你一定要使用非常强的规范来讲，就使用中间的URL，如果你要使用弱规范，使用右边的 URL 也就可以了。OK？




