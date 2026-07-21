---
title: 3-17 【源码品读】心跳和服务续约-2 
---

# 3-17 【源码品读】心跳和服务续约-2 

[image](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/3f9e69ea-de44-4ae6-a059-be721dd88d01/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SMLDFHS3%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T225546Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIBRuMWmIE7BLwAB%2FcQrAZuA0hg%2F%2BbggVx3eDAqavhCYOAiEAlIsl9QImF2%2FKRnpiptmUty%2B6JDMUnMbAHTeTwJReN5oqiAQIxv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDHBSDTsEB2rvia95YSrcA9w9TZ%2BdOGw%2B1c7GPUQMuhVSHaIUIULYX7sh2VNqsp01u7HPV3EVIVKyd5NXnKXg%2FBp%2FCDwTIPpeh%2B0LZU0hpEOWhR2QqF3eToHVrLcUpF563sWWti2JoQW9sWU%2FR%2Fa1ROKv3XS6MYnpBo9Ju0RzrRadVbavShKN0xOpFP7Kq9oUoCvte0TCuejvbLC2oZhNt1TnY4sw134hOzbE912oTsbq3SXFNsw0EdtqtYyxTNxnvmVmD7sw0xmsYgKdXNsAzVMyR8EW%2BxG%2FbMeFENaVH0DfOsG4lDZx1cb9SQZacpWUz%2FBzde7NW1y1O6rrwG77SowSIMRlZ9iuytAnAuuvEDGYlf2UgdTE7qHjJ7RWaITNtLQXHcwiqPHYobXZNToDppRFFtfpUWy3BXQbxAvQ2hTpEesiRRRZfZHQoFoutZRjiB8uW4BQQU7%2BDC5il%2B5ISID9irdbzPJ462WeRckcj9nPEEvaUq0NMG%2FLHjgyJ%2BkOQK1zugA2HutUetUyeD2IY6FO0U%2Bd9oV9xQiBBYDYjaUwZK91dmR%2BLLX8pYlJrXuC1GAexVC%2B8YuM6sGpfWTpFSlUD9WjnoU6QOP2wGBODYtQpqh9bA1RVR8kr4U9XlqGrD3j6Vl1y%2FOMSuOqMLu4%2F9IGOqUBDnwzjOs%2FoAV9SKu8iV1kw%2BsHCEZbwccHjV8fzeaaNZAbgPgkUCdQltTSjzl3i0oVT4TQouzOvDOs8EkEXvd%2FdfboL%2BibytWnsw7cNjyNyd%2BCvvRN1%2Fwi63ekaShmmT5GWR0iyt1D%2BSLzsC2otrcz9oJLw6odvixdl0Cug9Yyo9NklJy0J24Qez1ikKzfJnXQOF%2BPsubcFcI4Fhan8v7XULR83q0c&X-Amz-Signature=01783c6e61ea066c5cfae1dd447028dd6b67c6262d3d912ee4a60a8d2bd4afc7&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

二步，看到 its success 那就知道这里是正儿八经进行服务续约的地方了。那我这里放开断点，让他继续往下走一步。好，下面到了下一层的 renew 方法，那这里有三个入参，第一个入参是 App name 这里是有 recar client 没错，后面一个是 server idserver ID 是什么？是端口号和 IP 地址以及 App name 的组合。所以说这个 server ID 在服务治理的生命周期中是唯一的。对不对？你即使提供了同一种服务，那你在不同的机器上发过来，那它这个 server ID 是完全不一样的，你要么是端口不同，要么是 IP 端口不同。那总之它一定是个唯一的 server ID 第三个属性， its replication 前面讲过了，它这里是 false 因为它是由一个服务提供者发送过来的。
第一行，我们往下走打一个 log 那第二个方法这里是什么？ get sorted application 我们先不管它往下看，这个 application 列表里面，目前只有一个服务对不对？我这里只注册了一个服务，那假设我们的注册中心对接了很多服务方，那有成千上百个服务，那这个 list 的 size 会变得非常大。


OK 那它这里挑选application ，就是挑选你应该为哪一个应用做续约的时候，其实这方法蛮笨的，你看它怎么做的，它是一个 for 循环所有的 list 对不对？当这个 list 中的 application 的 name 和你传入的这个 name 相等的时候，好，那接下来再把这个 application 下面的所有 instance 全部拿到。这个 instance 就是每一个服务提供者。


假设我这个 eureka client 下面有 5 台机器对吧？那它的 instance 获得的就是五个 instance 那它 for 循环每一个instance ，比对你这个 instance 的 ID 和我的 server ID 是不是相同，如果相同好，那我就知道该为哪一个具体的 instance 进行续约了。


这个方法看起来大家觉得是不是蛮笨的，他这里其实可用一些 map 之类的方法提升一下效率因为我们的服务集群假设非常非常庞大的时候，那实际上你保存一个 list 这 list 中有几千上万台，这种机器还是会多额外消耗一些资源和时间的。那后面它就是 publish event 发布一个什么？发布一个 eureka instance renew the event 发布一个已经续约成功的 event 已经被续约了，但是成不成功还不知道。 OK 我们这一步先不看先跳到哪里，先跳到这个 return 这里看一下它 renew 中后续的一些逻辑。好，它到了负类方法我们跟进来，那负类方法中又到了负类方法对不对？那我们先不看这个if ，先看这个 if 条件里面这一步是什么？ replicate to pierce 那这里 replicate to pierce 什么含义？就是说你高可用注册中心，你有多个中心节点，那我需要向我的皮尔同步对不对？那这里就是这个含义，我们这一节先不看这部分代码，我们接着跟进去。这个 if 条件。


好，那这就是 renew 的一些逻辑了。第一步，做一个 increase 这个流程，我们可以先不看，因为它这是 false 然后 renew increase falseok 下一步这是什么？这是从 registry 里面通过 App name get 到所有的租约对不对？ G map 这里是租约，因为我们现在只注册了一个节点，所以这个租约也只有几台，只有一台对不对？好，如果租约不等于空，那怎么样？通过这个 ID 这个 ID 是什么？ server ID 我们前面说的那个唯一的 server ID 对不对？把它租约拿到。


好，如果租约为空怎么样？那租约 not found 要 increase 一把，这是一个计数器，那我们这里其实作业部为空，他已经拿到了对不对？那这时候先获得到 get holder get holder 就是你这个 instance 的信息，这个 instance 的 IP 地址等等这些信息。那如果 instance 可以拿到，就接下来往后走。


这里是从这个三个状态 instance list to renew her is replication 这三个属性中判断它是不是要 overrideninstance status 就是要重载这个 instance status 我们这里获得了一个 up up 就是说最新的 instance status 那我看接下来就需不需要重载呢？如果你的这个 instance status 是 unknown 也就是你接下来 unknown 情况下，它就要把这个 renew not found 再 increase 加 E 因为你都不知道你这个 instance 的信息了，那所以说它其实就是类比一种 not found 的状态，所以说要加一第二个情况是什么呢？如果你的这个 instance 和当前的这个 instance 是不相同的，也就是说假设你之前是 down 那你现在发来一个心跳包，它的 instance 变成了 up 那就是不相同的了。


那这种情况下它只需要怎么样？需要把这个 instance info set status without dirty 那这个方法是什么？我们点进去看一下，它这里你看 without dirty 一个 synchronize 修饰的方法，它这里把一个 in status 给设置到 instance 这个节点下。 Instance info ok. 因为我们这里这个 instance 之前就是 up 的状态，我们现在最新的状态也是 up 所以这个 if 方法没有进去，那大家知道一下它的作用就可以。


OK 那接下来我们这是什么？ renew last minute 加1，这是什么含义啊？ renew last minute 大家还记得在服务注册中心的页面上有一个 last minute renewal 这个属性对不对？就是过去一分钟它都有多少的租约被成功更新了，那就是从这些属性里面获得的。那我这里把这个属性值加1，就说明在过去的一分钟中，我又多了一个接收到的服务续约请求。 OK 这一步属性是什么？我这里打一个断点 list renew 我们到这个里面看一下它的租约是如何更新的。非常简单，跟进去它的 renew 只是更新一个 last update time step 具体是怎么样呢？当前的系统时间 system time step 加一个 duration 这个 duration 是什么？是 90 秒钟。对不对？它只是更新一个 last update time step 那这个属性后面会有用到的，我们退出来 return true 那 return true 了以后，接下来就是 replicate to pierce 我们这里就不看了，因为可实际上注册中心没有 pierce 我们这里只起了一个注册中心，那 return true 再往后走一步。


好，走到这一步，我们看 its success 就是 true 了，也就是说它的 renew 的流程已经成功了。但是照理说，走到这里只成功了一半，它并没有完全成功。我们接下来往后看。那假设不成功的情况下怎么办？不成功的情况下打一行 log 对不对？接下来怎么？接下来给客户端返回一个 not found 这个 status 由客户端处理后面的容错流程。那我们这里接着往下走。


好，这里就到了 last dirty time step 的地方了。这上面有一行注释， check if we need to synchronize based on dirty time step 我们是否需要针对于这个 dirty time step 做同步？ OK 那这里看一下这个 dirty time step 究竟是什么个用处。它这个判断条件是，如果 dirty time step 不等于空，那大家知道这个 dirty time step 从哪来的吗？是从客户端刚才我们的服务发送方来发送过来的。对不对？它这里可以揭晓它的含义了，它是说 last dirty time 也就是上最近一次和服务端出现脏数据的时间戳。这个脏数据什么意思啊？也就是说服务不同步，你跟服务中心之间可能有一些不管什么原因，它导致了产生了脏数据，也就是一段时间的数据没有同步。那这个不同步的是发生的最近的一次时间是什么？那就是这个 last dirty time step 的含义。那假设你客户端传来的 last dirty time step 不等于空，并且我在 server 端配置了什么？配置了这个属性，它叫什么？


Should synchronize when time step differs.
就是如果你这个 dirty time step 不等于空的情况下，我们定义了这个属性是不是需要做同步，那假设这个属性是，那接下来走后面的流程进来看一下。好，这个 response 在返回之前我需要怎么样？ validate dirty time step 我就要根据这个 dirty time step 做一个验证。什么验证呢？我们进去这里也是一段相对核心的一点的逻辑。那进去以后第一步是怎么是获取到 instance info 这个 instance info 大家都很熟悉啦，根据 App name 还有这个 server 的唯一性的 ID 来获取这个 instance name。


OK 接下来伊斯特斯 info 往后走，如果获取到了不等于空并且怎么样？并且你传入的 last dirty time 不等于空，而且这个传入的 last dirty time step 和当前在服务端保存的这个 instance info 中的 last dirty time 是不一样的。那这种情况说明怎么样，说明产生了一段时间的不同步的情况。那在这种情况下进去。它这直接返回了。为什么？看，因为我们传入的这个 last dirty time step 和服务端保存的是一致的，所以它没有走后续的流程。 OK 那假设它不一致会怎么样？我们来看一下。好。
接下来的情况有点稍微那么绕人，逻辑不复杂，理解起来有点绕两个 if 条件。第一个 if 条件是指客户端发来的脏数据时间，晚于服务端保存的脏数据时间，也就是说客户端的这个脏数据时间更新。那说明什么问题啊？说明客户端那边发生了某些事情，但是没有通知到服务端，它有可能是网络之间通信切断了等等原因，但服务端没有获知全量的服务数据。这种情况下，服务端能允许吗？不能允许。你产生哪怕一点点不同步，那都会由这个 dirty time step 反应过来。
服务端，通过一比较发现你 dirtytimestep 更新，那我不行。


我要让你怎么样？我要让你重新注册。那怎么重新注册呢？返回一个 not found 的指令，作为 response 客户端收到这个 not found 的 response 以后，它会重新启动注册流程。所以说因为 last dirty time step 导致的服务续约失败，那客户端需要重新启动服务注册。


OK 这是第一个条件。第二个条件是什么？是当服务端保存的 dirty time step 比客户端发来的 dirty time step 更新。那这种情况服务端笑了。没问题。对不对？因为我保存的是更新的数据，你发来的更晚。那这个时候有两个判断，如果你是由其他注册中心同步回来的，我会给你返回一个 conflict response 那如果你不是其他注册中心同步过来，你是由客户端直接发送过来的，那我完全 OK 什么都不用做。 OK 我接受你，但是我不会对我目前的服务造成什么影响，因为我是更新的数据，你发来的反而更老。对不对？ OK 接下来往后走，换掉断点回到了外层。那革命即将胜利。


好看到 response 已经构造出来了，它是什么？是 OK 那这个整个流程就要接近尾声了。在这之前还有一个 if 条件，那我们会不会进去并不会为什么，因为这个 if 条件它是跟什么有关？跟服务注册中心和其他注册中心之间的数据同步有关。那这有个属性 is from replicate node 在后面章节我们将讲到服务注册中心的高可用架构，同学学完相应的章节以后，可以再回过头来在这边打个断点，回流程是怎么进行操作的？ OK 那在打完最后一行 debug log 以后，我们就正儿八经营，完成了整个服务靴的流程，返回给客户端一个 status 等于 OK 的 response 请求。那这一节的内容就到这里了。下一节将用图文的形式跟大家介绍一下服务自保机制是如何运作的。同学们下期再见。



