---
title: 3-2 Spring Data REST应用技巧（1123）
---

# 3-2 Spring Data REST应用技巧（1123）

[image](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/e1234d12-2154-4d3b-869f-9a97a60e6d71/SCR-20240814-ispi.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466T4QAAQLL%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T232142Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDwoOJ5a5XRU1U3EFybPDjUr8S2%2FihkPy3QwJ1xUfLoDwIhANi2YCxlXT55rdaWGcogWHP5CCmtVXIQRlVlBrtNQZAZKogECMb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgyKet70DOg5WYgV8iQq3ANr8udk2F9Bu%2FihCgq14F5cgZUfpXntSxZUCgDkj4MB1Q%2BfjA96ZE7Yne%2B9b6xGxuzujYD1IMDxKCfmUjXlTfr5%2Bza7lpZO4elcQbAipoZO%2F1SR2mLRFI5YO4m14L%2FrptS0HGRUytqk1t5nTOE4DSmUcnspCAEM%2FOwV7op8Z%2FduGd7eHmleEZOWEHcgwryJCfQQGbaWNzJ8UvrMQszCUfLtDe1QBh1VzE0nP976uB1UfLZUtfInP%2FfBj40eM4fDfvbPPlV7xxJiJC7bYqWE6pNxLQRCWOKYOwFxlDA3j2Ap4szLhAHCVsEMy1LM5f0Bd%2BIERDfyHuVwIwlrOo1tsCSi9xc42Yr3bhEb%2BHGn9m%2F%2FIyRAeSahRFL24yCCdWbtIFvwJ%2BBgC%2FfJCunSvwqv7%2F6%2FzP6eqOpoKLTHrQlxSuYHGGynKAWcavMaHLbdHaC5YbVN5AHLintVkgAljq%2BTHw%2BpQEHkMsmgy9PdeTJnTWb1mFJEwH7WOEvWGSrx4nKCYMzA8MSJfouYMctFGv61SRpiaL1BOiJDVtTMyuBFJdHskj153XyDcrePXEgMGZb0iskEo82V7AMItgE%2BCsfkguVbBmAWKJe6zIGQOfxnUdllal%2FCHSkENcx%2BpUe77DCZuv%2FSBjqkAayW0VzOH%2B5u1y339ouDq6koNBEKMf3%2FvZdaxQLBkw9crCN9SUJry3EXj5LqTKfuEgpIhtDJmS04tZLlAQr1%2BM3DhK1BLcQheMAl9cP%2BNzhKMJxm0hbIN86z6%2F7hCHpx16PRCmGjoUdPHEN%2FXoLXi3z%2F9Ns16jmxZvLlNqzyKHGQ1kPWLHCyKibJSBBZ1e%2BlV9bAYgI%2Feb5M6SpH%2F7VS218%2F6vQG&X-Amz-Signature=fef74674fb49a4000f7e696aa43fc2d6411ce152bfec4769b69b351ec2bda46b&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

[image](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/7b63b3e7-88f5-44d3-8727-78c2c625af7b/SCR-20240814-iqyr.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466T4QAAQLL%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T232142Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDwoOJ5a5XRU1U3EFybPDjUr8S2%2FihkPy3QwJ1xUfLoDwIhANi2YCxlXT55rdaWGcogWHP5CCmtVXIQRlVlBrtNQZAZKogECMb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgyKet70DOg5WYgV8iQq3ANr8udk2F9Bu%2FihCgq14F5cgZUfpXntSxZUCgDkj4MB1Q%2BfjA96ZE7Yne%2B9b6xGxuzujYD1IMDxKCfmUjXlTfr5%2Bza7lpZO4elcQbAipoZO%2F1SR2mLRFI5YO4m14L%2FrptS0HGRUytqk1t5nTOE4DSmUcnspCAEM%2FOwV7op8Z%2FduGd7eHmleEZOWEHcgwryJCfQQGbaWNzJ8UvrMQszCUfLtDe1QBh1VzE0nP976uB1UfLZUtfInP%2FfBj40eM4fDfvbPPlV7xxJiJC7bYqWE6pNxLQRCWOKYOwFxlDA3j2Ap4szLhAHCVsEMy1LM5f0Bd%2BIERDfyHuVwIwlrOo1tsCSi9xc42Yr3bhEb%2BHGn9m%2F%2FIyRAeSahRFL24yCCdWbtIFvwJ%2BBgC%2FfJCunSvwqv7%2F6%2FzP6eqOpoKLTHrQlxSuYHGGynKAWcavMaHLbdHaC5YbVN5AHLintVkgAljq%2BTHw%2BpQEHkMsmgy9PdeTJnTWb1mFJEwH7WOEvWGSrx4nKCYMzA8MSJfouYMctFGv61SRpiaL1BOiJDVtTMyuBFJdHskj153XyDcrePXEgMGZb0iskEo82V7AMItgE%2BCsfkguVbBmAWKJe6zIGQOfxnUdllal%2FCHSkENcx%2BpUe77DCZuv%2FSBjqkAayW0VzOH%2B5u1y339ouDq6koNBEKMf3%2FvZdaxQLBkw9crCN9SUJry3EXj5LqTKfuEgpIhtDJmS04tZLlAQr1%2BM3DhK1BLcQheMAl9cP%2BNzhKMJxm0hbIN86z6%2F7hCHpx16PRCmGjoUdPHEN%2FXoLXi3z%2F9Ns16jmxZvLlNqzyKHGQ1kPWLHCyKibJSBBZ1e%2BlV9bAYgI%2Feb5M6SpH%2F7VS218%2F6vQG&X-Amz-Signature=95b383df92a5a7650d00a55dafd779e5c8c483d8cb21e064ae3e33862bc83ad1&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

同学们大家好，这一章节我们来介绍一下 spring day 的 rest 应用技巧解析。那么介绍 spring day 的 rest 呢？我们主要还是基于我们 Web 层 rest 的接口来去介绍。首先我们来认识一下这样一个注解， positive rest 的resource，也就是这个注解是把我们的 repository 映射成一个 rest 的一个资源，我们通过 rest 资源在 Web 层暴露出来访问，我们可以基于一些自定义完成我们的一些功能。


那么另一个注解就是我们使用 rest resource，我们可以看到这两个注解非常相似，第一个注解是 repository 的 reset resource，那么第二个注解是 reset resource，这两个注解使用的位置不是一样的，对于这个 repose reset resource 它是用在我们对应 repose 的这个接口上，那么 rest results 它是用在我们 reports 对应的方法上。那么我们可以基于这两个注解去完成一些特殊的一些功能。我们自定义，比如说修改一下我们暴露的URL，修改我们对应的一些配置，比如还有另外一个注解，我们可以跟大家介绍一下，这是一个对象投影，是个protection。


在前面介绍的过程中，我们提到通常我们在访问过程中会有这样的一个需求，比如说我们通过 reposure 暴露出来的对象，也就是我们注意原生跟数据库映射的一个对象，比如说这个对象它的内容字段是非常多的，像 user 对象，我们会放我们的 login ID，我们的 poster name 或我们的 name 等等的一些信息，那么我们如果说把这个对象直接暴露出来，其实有很多信息我们是并不想直接暴露给用户的。


比如说用户的创建时间，这用户的password，当然 Passport 是绝对不能暴露出来的，或者等等的一些我们认为是一些敏感的信息，我们应该把它给去掉，那么这种去掉的方式我们就可以组合使用我们的 report result resource 和我们的 rest resource，以及我们的 protection 进行一个组合去完成我们对于这个，也就是说对于我们接口信息的一个脱敏。


通常如果说我们在定义我们的用户对象，我们知道我们在定义的一个 user 对象，那么默认它的路径就是我们的users，那么如果说我们在其次，我们在定义我们的表结构，我们对象的过程中，我们通常是见名字义，我们通过见名字义的方式方便我们进行后面的一些维护工作。


那么如果说我们对于外界用户来说，我们可以通过 URL 去分析我们的系统，那么这又不是一个好的事情。因为如果说能把我们的 URL 分析得非常透彻的话，可能对于一些黑客攻击我们的时候对带来一些便利，所以通常我们在暴露 URL 的时候又不希望他那么见名字义，所以说我们更希望把我们的 URL 整体的去改变一下，也就是说原来我们是直接是我们的色子范的，嗯， user by name 我们可能去想改善其他的一个名称，以避免了容易被我们的普通用户也或者是一些黑客他们去拆除我们这个操作的一些行为。所以说我们基于这三个注解来完成这样一件事情。


首先我们来看一下我们的 report resource，对应 report resource 我们是放在对应的，我们的 user report 基于一个类的注解，我们可以在这里面看一下，这里面 report resource 它逃给等的是一个type，也就是它只能放在接口和类上面，那么这里面的一些属性我们这里面是exported，也就是说它是否我要把这个资源暴露出来，它默认是true。


如果说我们压根不想把我们的 user report 相关的这些操作暴露出来，那么我们在这里面配置为 false 就可以了，这里面还有我们的指定的pass。指定的 pass 是什么呢？默认我们会对我们这样的一个 user reporter 暴露出一个users，作为我们的默认的一个 base 目录，也就是我们的请求路径。当然我们这里面提到了，如果说我们把这个路径直接暴露出来，会容易让用户拆出我们这个长句的结构，所以这里面我们可以根据我们自己的一些混淆的特征，我们可以跟他指定一个pass，比如说我们这里面是指定是EU，那么还有另一个操作，也就是我们的 reset resource，我们可以看到它是放到我们这个接口对应的方法上面，我们切进来可以看到 reset resource 它支持的 element type。


这里面可以看到是 field must 和type，它既可以支持放到我们的方法上属性，也可以支持放到我们的类上面，这里面也是有对应的操作，这里面是给 part 的意思，不是这个资源是不是要暴露出来，我们可以看到它跟我们的 report resource 有很多功能是类似的，也就是它们之间可以有一个数的一个层级关系。


report result 在 resource 它是对整个接口进行一个 pass 的一个配置，那么对于 result resource，如果说它是在方法上，那么它就对针对这个方法的路径进行一个设置，这里面同时还支持对于 REL 相关的一些特殊的一个设置，后面是支持一些描述的一些信息，那么对于 report reset resource 它也是支持这些内容，但这里面会多了几个。比如说像我们的 collection resource REL，也就是我们访问列表请求它对应的一个 REL 信息，这里面有对应它相关的一些描述信息，包括item，这我们可以看到 item 和 clacson item 是针对一个对象plexin，它是支持一个集合。


最后面我们可以看到这里面是 part protection，就是说我们的一些摘要的映射信息，它默认是null，那么这里面我们也特意，我们这里面也特意去注入了一个。我们可以看到在这里面我们的pass，我们定义为EO，我们的 x part protection，我们指定了一个 user VO，那么其实我们可以对 user 各种的一个扩展，那么 user VO 就是我们基于我们的 user 对象作为参考，我们抽象出了我们比较关心的几个字段，那么我们给你切进来去看一下，注意到几个特征。


首先这个 user VO 它是个接口，那么对于这个接口它通过 projection 这个注解进行修饰，这里面指定了一下我一个 name 和这里面对应的type，也就是说我们当前这个 user v o 它映射的对象是什么？那么映射对象就是我们的user，那么对于 user 来说，我们可以看到对应它的这些属性都会生成对应的 get 筛的方法，那么我们 user v o 这里面保留了几个 get 方法，也就是 get name，我们的 get login name 和 get states，也就是说我们想暴露出来的属性，那么我们在这里面把它对应的 get 方法放到这里面。
那么在执行的过程中，我们会基于 user vo 生成我们的一个代理类，那么我们通过 user VO 暴露这操作，可以把我们这些属 3 个属性暴露出来。从这样去看的话，我们大概已经明白了，如果说我们去实现我们这个去修改URL，去修改我们这些输出属性的一些隐藏，我们可以用这种方式去完成。那么好，现在我们这个配置工作已经完成，现在我们要做的是什么呢？现在我们去请求访问一下，看一下能不能达到我们想要的效果，首先我们还是基于我们的 Spark UI 去看一下我们的结果，我们在这里面去刷新一下，我们先打开我们的 user entity，那么我们可以看一下我们的 UR 发生变化了，原来我们的 u r 是对应的users，现在我们是 e u，那么比如说这里面是 get 对应的是 find our user 方法，那么 post 对应的是 save user。


这里面含有我们对应的一个查询方法，我们可以看到这里面原来我们是通过 users search 是 find by name 这样一个操作，现在我们可以看到是我们的查询方法变成 EU search name，那么这里面也就是我们通过对应相关的一些操作，我们可以看到在这里面我们对于 find by name 这个操作，我们通过了 reset resource 这样一个注解进行修辞，我们把它 pass 路径来进行了一些修改，那么这样我们能得到这样一个请求路径，那么我们也可以通过我们的 SL 我们的这个 explore UI 去看一下我们的结果。
那么我们这里面去访问我们的请求数据，我们可以看到得到数据的内容，这里面数据的内容原来是属性会非常多的，现在我们可以看到它只包含了，比如像这里面是 lucky name，我们的普通 name 和我们的 states 只保留了这三个属性，那么这三个属性就是我们这里面对应的我们 user VO 所暴露的这三个属性。


这样看的话大家应该是比较明白我们如何通过这几个注解去简化我们，也就是做一些我们自定义输出的一些改造。那这里可能会有同学会去有一些疑惑，也就是说为什么我们通过这个注解它就能达到这样的效果？或者说另一个问法就是说我们的 repository set resource 它是如何生效的？你看我们这里面是配了我们的EO，这跟我们对应的 control 对应的 part 是不是类似的？其实想一下它可以这样去理解，它的操作逻辑是很相似的，我们可以看一下。


如果说我们想去深究一下我们的 report reslide resource 它是如何生效，我们可以看一下它在什么地方使用了？通常我们基于注解，那么注解在运行解析的过程中，相当于是对这个注解的 Meta day 的信息进行获取的，在进行我们逻辑上的处理，我们可以看一下 reports 的 resource reset 它在什么地方使用了，那么我们可以看到这里面会涉及到了我们的 report reset configuration，那么在这里面的配置的话，我们可以看到它只是一个引入或者是基于一个注解的一些信息。


那我们再看这里面是 reporsory context resource Mapping，也就是说这 Mapping 的信息比较重要，那我们看这是也是import，我们可以忽略，那么我们接下来去看在这里面会涉及到了我们对于这个 report resource reset 这个类注解的引入，那么基于这个引入的话，我们可以猜测到它可能在这里面去做一些业务的处理，我们可以跟进去看一下。


那么在这里面我们可以看到对于我们这里面会定义对应的一些查找规则，这里面我们查找我们当前这个类型是不是被 repose resource 这个注解学优势。如果是的话，我们可以看到下面会这里面同时会去查找我们的 reset resource 和 repository reset resource，基于这里面去查找这个规则，查找完成以后会对它进行一些处理，我们可以看到在这里面处理的过程中，我们看它会去在构建我们的这个 link Relix，也就是说构建我们这个 URL 的过程中，它会去参照我们当前有没有找到我们特殊自定义的？我们看这里面是 collection resource REL，如果有的话我们采用它默认的规则，如果没有的话我们就忽略我们通过这样的话，我们就大概去能去分析，我们可以看到后面是对于 pass 路径的一些处理，看到这里面处理的过程中，它是跟我们 reports 相关的一些注解。


对应寻找对应的 pass 属性，这里面是我们寻找 rest resource pass 属性，这里面我们去查找第一个不为空的对象，这里面同时进行我们判断一下，如果说这个 pass 路径不为空，那么会进行我们对于这个 URL 的处理，我们可以看到这里面如果说 URL 它包含了我们的这个选，就会直接抛出一个异常，所以说我们在设置的时候我们只设置我们的名称，不要去加我们这个反斜杠。


从这里面我们去看它的处理的逻辑，我们大概已经清楚了我们是如何在实现我们定义这个 report resource reset 的自定义的一些操作，也就是我们通过我们的 pass 信息在这里面配置，那么它在这里面我们的 repose collection resource Mapping 的过程中会获取我们这些配置属性，进行我们一个映射，得到我们想希望的一个效果。我们 spring did reside 应用技巧解析的内容就先介绍这里，同学们听到这里一定是很辛苦了，感谢大家，我们下一章节再见。


