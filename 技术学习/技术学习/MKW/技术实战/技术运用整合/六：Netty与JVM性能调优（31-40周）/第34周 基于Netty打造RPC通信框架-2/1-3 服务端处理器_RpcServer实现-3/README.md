---
title: 1-3 服务端处理器_RpcServer实现-3
---

# 1-3 服务端处理器_RpcServer实现-3

[image](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/f2e62a01-8844-4e3a-a60e-42b26d5a934c/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466T4QAAQLL%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T230038Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDwoOJ5a5XRU1U3EFybPDjUr8S2%2FihkPy3QwJ1xUfLoDwIhANi2YCxlXT55rdaWGcogWHP5CCmtVXIQRlVlBrtNQZAZKogECMb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgyKet70DOg5WYgV8iQq3ANr8udk2F9Bu%2FihCgq14F5cgZUfpXntSxZUCgDkj4MB1Q%2BfjA96ZE7Yne%2B9b6xGxuzujYD1IMDxKCfmUjXlTfr5%2Bza7lpZO4elcQbAipoZO%2F1SR2mLRFI5YO4m14L%2FrptS0HGRUytqk1t5nTOE4DSmUcnspCAEM%2FOwV7op8Z%2FduGd7eHmleEZOWEHcgwryJCfQQGbaWNzJ8UvrMQszCUfLtDe1QBh1VzE0nP976uB1UfLZUtfInP%2FfBj40eM4fDfvbPPlV7xxJiJC7bYqWE6pNxLQRCWOKYOwFxlDA3j2Ap4szLhAHCVsEMy1LM5f0Bd%2BIERDfyHuVwIwlrOo1tsCSi9xc42Yr3bhEb%2BHGn9m%2F%2FIyRAeSahRFL24yCCdWbtIFvwJ%2BBgC%2FfJCunSvwqv7%2F6%2FzP6eqOpoKLTHrQlxSuYHGGynKAWcavMaHLbdHaC5YbVN5AHLintVkgAljq%2BTHw%2BpQEHkMsmgy9PdeTJnTWb1mFJEwH7WOEvWGSrx4nKCYMzA8MSJfouYMctFGv61SRpiaL1BOiJDVtTMyuBFJdHskj153XyDcrePXEgMGZb0iskEo82V7AMItgE%2BCsfkguVbBmAWKJe6zIGQOfxnUdllal%2FCHSkENcx%2BpUe77DCZuv%2FSBjqkAayW0VzOH%2B5u1y339ouDq6koNBEKMf3%2FvZdaxQLBkw9crCN9SUJry3EXj5LqTKfuEgpIhtDJmS04tZLlAQr1%2BM3DhK1BLcQheMAl9cP%2BNzhKMJxm0hbIN86z6%2F7hCHpx16PRCmGjoUdPHEN%2FXoLXi3z%2F9Ns16jmxZvLlNqzyKHGQ1kPWLHCyKibJSBBZ1e%2BlV9bAYgI%2Feb5M6SpH%2F7VS218%2F6vQG&X-Amz-Signature=9f8634c745a4acf3736a41661d6db6a5add1ca07b602b0b6bea5bb91cdf31243&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

这个方法其实没多少行代码，但是它是属于最关键的，就是表示注册，叫做 registry processor，叫做程序注册器。这个东西主要是注册什么，跟大家去详细的讨论一下。来说一说这块内容。来，我们回过头来分析一下我们的 RPC 框架。在这里边我们看。


首先看一下这幅图程序注册的方法。首先它需要有一个map，它这个 map 里边它的 key 是什么？ key 是一个接口，名称value。什么？ value 是一个引用逻辑程序。首先有这么一个类，看见了吗？叫做 provider config。在这里我先把这个类先搞出来，我们再新建一个package，这叫 rpc，我们叫做config。

[image](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/e3bc3147-28d3-4cec-a715-5172d8f21978/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466T4QAAQLL%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T230038Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDwoOJ5a5XRU1U3EFybPDjUr8S2%2FihkPy3QwJ1xUfLoDwIhANi2YCxlXT55rdaWGcogWHP5CCmtVXIQRlVlBrtNQZAZKogECMb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgyKet70DOg5WYgV8iQq3ANr8udk2F9Bu%2FihCgq14F5cgZUfpXntSxZUCgDkj4MB1Q%2BfjA96ZE7Yne%2B9b6xGxuzujYD1IMDxKCfmUjXlTfr5%2Bza7lpZO4elcQbAipoZO%2F1SR2mLRFI5YO4m14L%2FrptS0HGRUytqk1t5nTOE4DSmUcnspCAEM%2FOwV7op8Z%2FduGd7eHmleEZOWEHcgwryJCfQQGbaWNzJ8UvrMQszCUfLtDe1QBh1VzE0nP976uB1UfLZUtfInP%2FfBj40eM4fDfvbPPlV7xxJiJC7bYqWE6pNxLQRCWOKYOwFxlDA3j2Ap4szLhAHCVsEMy1LM5f0Bd%2BIERDfyHuVwIwlrOo1tsCSi9xc42Yr3bhEb%2BHGn9m%2F%2FIyRAeSahRFL24yCCdWbtIFvwJ%2BBgC%2FfJCunSvwqv7%2F6%2FzP6eqOpoKLTHrQlxSuYHGGynKAWcavMaHLbdHaC5YbVN5AHLintVkgAljq%2BTHw%2BpQEHkMsmgy9PdeTJnTWb1mFJEwH7WOEvWGSrx4nKCYMzA8MSJfouYMctFGv61SRpiaL1BOiJDVtTMyuBFJdHskj153XyDcrePXEgMGZb0iskEo82V7AMItgE%2BCsfkguVbBmAWKJe6zIGQOfxnUdllal%2FCHSkENcx%2BpUe77DCZuv%2FSBjqkAayW0VzOH%2B5u1y339ouDq6koNBEKMf3%2FvZdaxQLBkw9crCN9SUJry3EXj5LqTKfuEgpIhtDJmS04tZLlAQr1%2BM3DhK1BLcQheMAl9cP%2BNzhKMJxm0hbIN86z6%2F7hCHpx16PRCmGjoUdPHEN%2FXoLXi3z%2F9Ns16jmxZvLlNqzyKHGQ1kPWLHCyKibJSBBZ1e%2BlV9bAYgI%2Feb5M6SpH%2F7VS218%2F6vQG&X-Amz-Signature=d23a2b2ea72c83f8e0842ca35b80050fa8647452ca1385a3335021162fda1fdd&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

第二 provider 好了，我把它创建出来，这是一个class，哈，咱们叫做 provider config。好， provide config 里边必然会有两个非常关键的内容，一个内容是什么？当前接口有两个比较关键的属性哈，一个是接口名称，还有一个是程序对象。为什么？我们来看一下引用逻辑程序哈，还有一个接口名称，因为我们在注册的时候必须 key 是接口名称，而且是 provider config 的，它的 key 接口名称 value 也是 provider config 下面里边所有的一个引用逻辑程序。所以不管怎么说，我 provide config 类里边必须有这两个属性。好了，现在我现在问同学，为什么我们现在需要这么一个类，其实需要它的原因，其实你可以不用它，但是后面如果小伙伴们想去说我 RPC 框架，想要跟我们的 spring 去整合的时候，你最好有这么一个 provide config 类就比较 easy 了，比较轻松了。


在这废话不多说，我们先画一幅图，帮助小伙伴们去理解我们的 provide config 到底是一个什么东西。还有帮助小伙伴们去理解 register processor 它到底要干什么事情。首先再新建一个流程图，这也是对应我们的 client 端程序，这边是我们的 server 端程序。现在我们当前要做的事情就是我们的 client 端肯定是发起一次 request 请求， request 请求发起到我们的 server 端，到 server 端谁去接收？当然这里我要写一下哈，这是我们的 client 端， client 端也相当于服务的调用方，就是我们的consumer，我们的是不相当于我们的服务提供方是我们的 server 端，也就是服务的provider。这里都毋庸置疑，对不对肯定都没问题哈。


好了，我把它字体大一点好了，我发起一个请求过去到 server 端，它要做什么事情，他肯定得去跟把请求解析，解析完了之后去调用对不对？我们知道 RPC 是做什么事情， RPC request，他要给我们什么样的信息？


小伙伴们还记得 request 对象里边的内容吗？我们之前已经封装过我们的协议，对不对？肯定有 request ID class， master name，包括 parameter types 以及 parameter 思对吧。请求里边肯定包含什么类信息，就是类名称的信息，还有方法名称参数列表的类型以及参数具体实际的参数列表。


我们的 RPC 是干什么事情？我们的 RPC 不就是把这些内容封装成一个 request 请求给我们的 server 端要做什么？我们 server 端其实就是这有一个执行器executor，执行器就需要过这些信息能知道我们要执行它。其实程序执行器要执行的一件事情是什么？无非他要做的事情就是我要知道你这个请求它到底是远程调用，执行哪一个类，下面的哪一个方法我把它最大化。


我根据他给我传的这些参数，我能找到是不是因为我是一个服务的提供方，是不是我提供了好多服务这里边比如我们提供了 user service 服务，我们提供了 hello service 服务等等是吧？好多 service 服务都是我们提供的。当然我们这些服务我们肯定在 server 端来讲，我们是有具体实现的，我们百分之百是有具体实现的。


我暴露给什么？我暴露给 client 端的只是我的接口对不对？我把 user service 它的接口以及我们的 hello service 它的接口，也就是我们后面可能会有注册中心对不对？我们再搞一个东西，是不是我们都知道学过 double 就学过 RPC 框架，你是肯定会知道一个 registry 这么一个鬼， registry center 这么一个东西。


注册中心，我们肯定是把我们所提供的 service 跟 hello service 他们的服务列表去 registry 去注册，对不对？或者你可以认为去 exporter 去做一个exporter，帮我们去导入到我们的注册中心上，对吧？我不知道小伙伴们能不能理解我们服务的 client 端，它其实是服务的调用方，他要做的事情是干什么？从注册中心去拉取，也就是去 import 去拉取我们的 registry list。我就简单去写哈。去拉取我们注册的一些列表，一些内容肯定是这样的。这 double 都是这么去玩的。是不是有一个什么注册，有一个拉取服务的提供方，肯定是把自己所提供的一些特有的服务去注册到注册中心。这样服务的调用方肯定去拉取服务列表，直接发起远程 RPC 用。

[image](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/d7e6dc22-b0ec-468f-bf7a-936d42ddd9c4/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466T4QAAQLL%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T230038Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDwoOJ5a5XRU1U3EFybPDjUr8S2%2FihkPy3QwJ1xUfLoDwIhANi2YCxlXT55rdaWGcogWHP5CCmtVXIQRlVlBrtNQZAZKogECMb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgyKet70DOg5WYgV8iQq3ANr8udk2F9Bu%2FihCgq14F5cgZUfpXntSxZUCgDkj4MB1Q%2BfjA96ZE7Yne%2B9b6xGxuzujYD1IMDxKCfmUjXlTfr5%2Bza7lpZO4elcQbAipoZO%2F1SR2mLRFI5YO4m14L%2FrptS0HGRUytqk1t5nTOE4DSmUcnspCAEM%2FOwV7op8Z%2FduGd7eHmleEZOWEHcgwryJCfQQGbaWNzJ8UvrMQszCUfLtDe1QBh1VzE0nP976uB1UfLZUtfInP%2FfBj40eM4fDfvbPPlV7xxJiJC7bYqWE6pNxLQRCWOKYOwFxlDA3j2Ap4szLhAHCVsEMy1LM5f0Bd%2BIERDfyHuVwIwlrOo1tsCSi9xc42Yr3bhEb%2BHGn9m%2F%2FIyRAeSahRFL24yCCdWbtIFvwJ%2BBgC%2FfJCunSvwqv7%2F6%2FzP6eqOpoKLTHrQlxSuYHGGynKAWcavMaHLbdHaC5YbVN5AHLintVkgAljq%2BTHw%2BpQEHkMsmgy9PdeTJnTWb1mFJEwH7WOEvWGSrx4nKCYMzA8MSJfouYMctFGv61SRpiaL1BOiJDVtTMyuBFJdHskj153XyDcrePXEgMGZb0iskEo82V7AMItgE%2BCsfkguVbBmAWKJe6zIGQOfxnUdllal%2FCHSkENcx%2BpUe77DCZuv%2FSBjqkAayW0VzOH%2B5u1y339ouDq6koNBEKMf3%2FvZdaxQLBkw9crCN9SUJry3EXj5LqTKfuEgpIhtDJmS04tZLlAQr1%2BM3DhK1BLcQheMAl9cP%2BNzhKMJxm0hbIN86z6%2F7hCHpx16PRCmGjoUdPHEN%2FXoLXi3z%2F9Ns16jmxZvLlNqzyKHGQ1kPWLHCyKibJSBBZ1e%2BlV9bAYgI%2Feb5M6SpH%2F7VS218%2F6vQG&X-Amz-Signature=1cc03f62d0ea50ae6259ef160ad4bb3c776732e8bbd45a3d745c39a5f0b7a41c&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

就这么一个事儿，我现在问你，我的request，其实我封装这些数据类的名称，方法名称，参数列表，参数类型主要干什么？主要想通过这个请求，它能够直接帮我去知道我到底这次远程调用的是我提供的 user service 还是 hello service，到底是调哪个服务，具体调哪个服务，下面的哪个方法？这里面方法名称有，是不是，是不是垂构传什么样的参数列表也有，类型也有。


通过这个请求，我是不是能知道什么？能知道我到底执行的是 user service 下的什么方法，或者是 hello service 下的什么方法就可以了，对吧？ OK 同学们，既然知道 r p c 请求要做的事情是这件事情好办。现在我再给提供一个什么，我再给提供一个刚才我们看到的这个东西叫做 provider 的config。 provider 的 config 是什么？我把它放大一点。小伙伴们，如果想要去跟 spring 整合，无论你的 user service 也好，还是你的 hello service 也好，你都应该起码是 provider service 的一个子类。 OK 也。这个类是一个更上层的类，我们把它用绿颜色表示这个类，它是具体的一个实现类，是一个子类，用粉颜色。


好了，我 provide config 里面是做一个通用化的配置，具体的服务的提供方，你都要对 provide config 做一些配置，才能去帮我去注册到 registry center 上。所以我需要有这么一个类，我具体的实现类。不管是 user service 也好，还是 hello service 也好，都必须要继承它的父类，肯定是 provider config。 provider config 里面肯定有一些通用的信息，比如像我们刚才说的类 user service，它可能是一个 implements 实现对不对？ hello service 也是一个 implements 实现。


我们说provider，它里边有具体的什么，有具体的一些信息，比如比较关键的信息，比如最关键的是什么？我的 interface name 是什么？还有我具体是哪个实例对象？说的是具体的实现类的实例。我现在要干什么？我说我在注册的时候，我一定要把接口和对应的实际的实现类，我应该做一个 11 的绑定的关系。我们就拿 user service 


implements 举例。 user service implements 这个是一个实例，它的接口肯定是 user service，如果它有接口，哈， user service implements 对象就是具体的这个类的实例对象，它就是一个具体的服务对象。我们再回过头来注册的时候我要干什么？我要把 provider config 里边它具体的接口名称是什么？就是 user service 对不对？接口名称。它具体的实现类是什么？它应该就是 user service implements 实例对象。我要把接口的当成key，具体接口下面的实现类的实例对象当成value，做一个绑定关系，放到我们的 handle map 里边对不对？

[image](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/fde7bfd0-57ca-41a1-886a-cdb9475383f2/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466T4QAAQLL%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T230038Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDwoOJ5a5XRU1U3EFybPDjUr8S2%2FihkPy3QwJ1xUfLoDwIhANi2YCxlXT55rdaWGcogWHP5CCmtVXIQRlVlBrtNQZAZKogECMb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgyKet70DOg5WYgV8iQq3ANr8udk2F9Bu%2FihCgq14F5cgZUfpXntSxZUCgDkj4MB1Q%2BfjA96ZE7Yne%2B9b6xGxuzujYD1IMDxKCfmUjXlTfr5%2Bza7lpZO4elcQbAipoZO%2F1SR2mLRFI5YO4m14L%2FrptS0HGRUytqk1t5nTOE4DSmUcnspCAEM%2FOwV7op8Z%2FduGd7eHmleEZOWEHcgwryJCfQQGbaWNzJ8UvrMQszCUfLtDe1QBh1VzE0nP976uB1UfLZUtfInP%2FfBj40eM4fDfvbPPlV7xxJiJC7bYqWE6pNxLQRCWOKYOwFxlDA3j2Ap4szLhAHCVsEMy1LM5f0Bd%2BIERDfyHuVwIwlrOo1tsCSi9xc42Yr3bhEb%2BHGn9m%2F%2FIyRAeSahRFL24yCCdWbtIFvwJ%2BBgC%2FfJCunSvwqv7%2F6%2FzP6eqOpoKLTHrQlxSuYHGGynKAWcavMaHLbdHaC5YbVN5AHLintVkgAljq%2BTHw%2BpQEHkMsmgy9PdeTJnTWb1mFJEwH7WOEvWGSrx4nKCYMzA8MSJfouYMctFGv61SRpiaL1BOiJDVtTMyuBFJdHskj153XyDcrePXEgMGZb0iskEo82V7AMItgE%2BCsfkguVbBmAWKJe6zIGQOfxnUdllal%2FCHSkENcx%2BpUe77DCZuv%2FSBjqkAayW0VzOH%2B5u1y339ouDq6koNBEKMf3%2FvZdaxQLBkw9crCN9SUJry3EXj5LqTKfuEgpIhtDJmS04tZLlAQr1%2BM3DhK1BLcQheMAl9cP%2BNzhKMJxm0hbIN86z6%2F7hCHpx16PRCmGjoUdPHEN%2FXoLXi3z%2F9Ns16jmxZvLlNqzyKHGQ1kPWLHCyKibJSBBZ1e%2BlV9bAYgI%2Feb5M6SpH%2F7VS218%2F6vQG&X-Amz-Signature=81984533e0996f0fbe77bfff388b88b488376e18e8d385d2d7011ba7b8b75dbd&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

我们有了 handler map，我们去发请求的时候是不是发出来？根据请求这些信息，我们从 handle map 里边我们能够找到它是哪个接口，它对应的实现类是什么？它这里边有方法，是不是我们可以通过反射的方式直接就能调到？我到底是调用哪个实现类的哪个方法通过反射是不是就直接能够执行本地的哪块逻辑了？执行完了之后给我返回，我去享用回去就可以了。其实就是这么简单的一件事情。


好了，我们来看一看我们具体怎么去实现，实现起来还是稍微有一点点麻烦的。当然我说的麻烦不是说代码麻烦，是有一点抽象。我们都知道，我们不管是我们的服务的提供方也好，就是 provider 端也好，还是服务的 consumer 端，就是引用方或者是调用方也好，我希望如果未来有一天跟 spring 整合的时候，

[image](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/457e286f-5ad7-4fa9-9bda-93f2654db838/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466T4QAAQLL%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T230038Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDwoOJ5a5XRU1U3EFybPDjUr8S2%2FihkPy3QwJ1xUfLoDwIhANi2YCxlXT55rdaWGcogWHP5CCmtVXIQRlVlBrtNQZAZKogECMb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgyKet70DOg5WYgV8iQq3ANr8udk2F9Bu%2FihCgq14F5cgZUfpXntSxZUCgDkj4MB1Q%2BfjA96ZE7Yne%2B9b6xGxuzujYD1IMDxKCfmUjXlTfr5%2Bza7lpZO4elcQbAipoZO%2F1SR2mLRFI5YO4m14L%2FrptS0HGRUytqk1t5nTOE4DSmUcnspCAEM%2FOwV7op8Z%2FduGd7eHmleEZOWEHcgwryJCfQQGbaWNzJ8UvrMQszCUfLtDe1QBh1VzE0nP976uB1UfLZUtfInP%2FfBj40eM4fDfvbPPlV7xxJiJC7bYqWE6pNxLQRCWOKYOwFxlDA3j2Ap4szLhAHCVsEMy1LM5f0Bd%2BIERDfyHuVwIwlrOo1tsCSi9xc42Yr3bhEb%2BHGn9m%2F%2FIyRAeSahRFL24yCCdWbtIFvwJ%2BBgC%2FfJCunSvwqv7%2F6%2FzP6eqOpoKLTHrQlxSuYHGGynKAWcavMaHLbdHaC5YbVN5AHLintVkgAljq%2BTHw%2BpQEHkMsmgy9PdeTJnTWb1mFJEwH7WOEvWGSrx4nKCYMzA8MSJfouYMctFGv61SRpiaL1BOiJDVtTMyuBFJdHskj153XyDcrePXEgMGZb0iskEo82V7AMItgE%2BCsfkguVbBmAWKJe6zIGQOfxnUdllal%2FCHSkENcx%2BpUe77DCZuv%2FSBjqkAayW0VzOH%2B5u1y339ouDq6koNBEKMf3%2FvZdaxQLBkw9crCN9SUJry3EXj5LqTKfuEgpIhtDJmS04tZLlAQr1%2BM3DhK1BLcQheMAl9cP%2BNzhKMJxm0hbIN86z6%2F7hCHpx16PRCmGjoUdPHEN%2FXoLXi3z%2F9Ns16jmxZvLlNqzyKHGQ1kPWLHCyKibJSBBZ1e%2BlV9bAYgI%2Feb5M6SpH%2F7VS218%2F6vQG&X-Amz-Signature=fc998d754f90cb7dbc7f4088a18f81e7496f1b12b17e458d5f762b5fd1e7ea45&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

我有一个 provider config，我是不是也应该有一个什么 consumer config 对吧？是不是有这个是最好的？不管是 provider config 还是 consumer config，我期望都有一个东西。这东西的目的是在什么？假设我这里边有一个 RPC 调用我的服务的调用方，比如有一个叫做 in work class 或者是 in work service a，我是不是可能还会有一个 inwork service b？这两个 inwork service a 和 b 是啥意思？就是真正的服务的调用方的实例对象。 a 和 b 是不是他们跟他也应该是一个什么关系？我觉得也应该是这样的一个关系。


这是我的consumer，他可能有好多个是不是？反正服务的调用方可能是 inwork service AA 去调远程的 service implements，它下面的某个接口，下面某个方法对吧？隐沃克 service b 可能调 hello service implements。
下面具体的方法，它是不是也应该有一些公用的属性？我是不是也可以去做一层抽象？说白了，这个类它应该是服务的调用方的一个父类对吧？我的 consumer config 应该是一个比较上级的类。我的 provider config 也是服务提供方的一个比较上级类。我觉得它们两个里边应该还有一些共同的属性。我为什么现在就把这个东西跟大家讲清楚？因为后面如果一旦我们想去跟 spring 集成的，我肯定有父类。个更上层的父类。它也不是服务的提供方， provider 也不是服务的调用方 consumer 它就是一个 bin 对吧？如果你跟 Supreme 整合在一起了，我现在问你更上层的负类，它肯定有一些通用的东西。比如我现在服务的提供方，它的 bin 的 ID 是什么？服务的调用方，它的 ID 是什么？这是不是是通用的？还有服务的提供方跟服务的调用方是不是都有？接口都有。


我的 interface 到底是什么？首先比如 user service implements，它是不是得暴露出来接口，比如接口是 user service，我用另外一个颜色去表述出来，哈，比如用蓝色 user service 接口是不是要去在子缝启动的时候，可能通过一个时机去 export 到我们的 user center？我们对应的我们的 RPC 框架是不是应该引入接口的包放到这里，对不对？我们去调用接口下面的什么方法？通过接口远程调用，把它封装成 request 对象，封装成这些最基本的类名称方法名称参数列表，去找到我具体的 user service 下面的实现类，在下面的哪个方法去执行，执行完了之后给我返回结果，对吧？所以不管怎么样，无不管是我们的 consumer config，还是我们的 provider config，它总是有一个更上层的类，更上层的类，它里边包含的一些通用信息，比如 bid 对不对？比如接口名称就是interface，你这两边都得需要用到。还有一些特殊的，比如我们的服务的 client 端，可能需要知道一个代理，是不是它有一个代理，像比如我们的 proxy class，代理的 class 是什么？还有一些其他的信息，总之它是这样的层次结构。


如果你把这个层次结构搞定了之后，以后跟 spring 去整合就非常简单了。即使是你不跟死神整合，你按这种方式也可以去把该 new 出来，对象 new 出来，也可以去做一个完整的这种r、p、 c 调用的这么一个过程。我现在只是跟大家去把未来如果跟 spring 集成，我们应该怎么去设计我们对应的 provide config 跟 consumer config，以及通用的更上层的config。我先把设计先写出来，后面就简单了，要不然可能我们实现完了，还得重新再改一版，就特别麻烦。我已经讲完了，接下来我们就开始去做实现。

