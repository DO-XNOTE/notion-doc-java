---
title: 1-12 【源码品读】LoadBalanced底层机制解析
---

# 1-12 【源码品读】LoadBalanced底层机制解析

[image](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/50d3d64e-50fc-4e85-880f-8f5815d9afaf/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XEYJZSTZ%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T225611Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIAnl5wJoNvxluc3dTL%2BFH0DdQ7vEB1VIQ8yjcHt1llacAiEAgiSDUFq601T4v4W6YhCLnkDa2oSZ4hJQLIgcxDpCNMQqiAQIxv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDEGuGc5xX4ab8zPS8CrcAyNEne7ydndk7GTcWjUqhykDNLXeulyGdZVTQ87IQhaR2woLEsAOhC3gKXDdXjOiX4TUXB3OJkkl9pxkaeUCrT1v%2Fu0s0aU6gGKycb2RA%2FWNwqXgyEbYEh%2BWQ%2BOTy5Olnu4BKy3MpIOC8EJzBF6QHY6v63kKaMcDNYOaCA3LhRQEjKOcZpLdZnALb8wLoPeWt0sJprCajjW7lMXuunZmxrxfohPCpBwaOgDuVHiLZKFVnXwIMHWpgdzMPZbieq0ZPV9psgQ2nLWmemmzPD405M4jyHQ%2FFaj9wVNt2Rl2npfSRfidHYIFaeHimABmdFTsm8UeIglDYbSLeznSpKHZYXAqDqNANKBt8wPCtqM%2BrmThxxDm3nkcttMCDGwDt16sHCC39b%2BVGPp0dIZpv8ocFl%2FWwq0xqhENaj71cXEbGnOGaKhUR5t4gcKNpygXwmkhZjfn9BpUBv5186brjpVpR1IHXoYRvwhsJ9ZrrHgwNHqODnF1Cg%2FSi2UkDxzOKtYx4X%2BXyypGgmB%2B2QpZDRMqFloR9ut6MlR%2BJf1%2BVQf7r9RenrpTB%2BFcJ27u%2FqSXkbys1Yuy7%2F3ikjfzXopTtJhiKfu5JP5f1Tjx81GkBGI5FVWgOr6p1UVFNzGEifkRMJ%2B6%2F9IGOqUBQlllArJPJN9fLoEHSY0fM9qYcff%2BeUUtSXcXwSMF8dali%2BTDrcH%2BwozfQj1IP3wnM3ca%2BqVQnQ9t6o9Dbz6A3AsPNQ6d0z618FdrjCjB9CkmSShvV3tQ8w9e5g1m17NQ0PnDKicpvNrEGYyHmYGlAYh%2F28ve6ZIDIr0wGfTRnqRvTV5Dw07U6TEMX6ZBAnExFwi9nvSIFZLk%2BMl3LKvALqf0DBkE&X-Amz-Signature=08b7d91afcc0c3135b65d51ab0e87f3def4d113648c708d5a9b51f3ad5ef9bc7&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

[image](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/e252340f-3609-4e0e-b82b-016fc518bf17/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XEYJZSTZ%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T225611Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIAnl5wJoNvxluc3dTL%2BFH0DdQ7vEB1VIQ8yjcHt1llacAiEAgiSDUFq601T4v4W6YhCLnkDa2oSZ4hJQLIgcxDpCNMQqiAQIxv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDEGuGc5xX4ab8zPS8CrcAyNEne7ydndk7GTcWjUqhykDNLXeulyGdZVTQ87IQhaR2woLEsAOhC3gKXDdXjOiX4TUXB3OJkkl9pxkaeUCrT1v%2Fu0s0aU6gGKycb2RA%2FWNwqXgyEbYEh%2BWQ%2BOTy5Olnu4BKy3MpIOC8EJzBF6QHY6v63kKaMcDNYOaCA3LhRQEjKOcZpLdZnALb8wLoPeWt0sJprCajjW7lMXuunZmxrxfohPCpBwaOgDuVHiLZKFVnXwIMHWpgdzMPZbieq0ZPV9psgQ2nLWmemmzPD405M4jyHQ%2FFaj9wVNt2Rl2npfSRfidHYIFaeHimABmdFTsm8UeIglDYbSLeznSpKHZYXAqDqNANKBt8wPCtqM%2BrmThxxDm3nkcttMCDGwDt16sHCC39b%2BVGPp0dIZpv8ocFl%2FWwq0xqhENaj71cXEbGnOGaKhUR5t4gcKNpygXwmkhZjfn9BpUBv5186brjpVpR1IHXoYRvwhsJ9ZrrHgwNHqODnF1Cg%2FSi2UkDxzOKtYx4X%2BXyypGgmB%2B2QpZDRMqFloR9ut6MlR%2BJf1%2BVQf7r9RenrpTB%2BFcJ27u%2FqSXkbys1Yuy7%2F3ikjfzXopTtJhiKfu5JP5f1Tjx81GkBGI5FVWgOr6p1UVFNzGEifkRMJ%2B6%2F9IGOqUBQlllArJPJN9fLoEHSY0fM9qYcff%2BeUUtSXcXwSMF8dali%2BTDrcH%2BwozfQj1IP3wnM3ca%2BqVQnQ9t6o9Dbz6A3AsPNQ6d0z618FdrjCjB9CkmSShvV3tQ8w9e5g1m17NQ0PnDKicpvNrEGYyHmYGlAYh%2F28ve6ZIDIr0wGfTRnqRvTV5Dw07U6TEMX6ZBAnExFwi9nvSIFZLk%2BMl3LKvALqf0DBkE&X-Amz-Signature=ed6081ab257d51c0852181fa8b49684868d8347a576cc776d47567643c24a920&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

[image](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/d7fddb36-4012-4bac-ad8d-c27b6339de60/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XEYJZSTZ%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T225611Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIAnl5wJoNvxluc3dTL%2BFH0DdQ7vEB1VIQ8yjcHt1llacAiEAgiSDUFq601T4v4W6YhCLnkDa2oSZ4hJQLIgcxDpCNMQqiAQIxv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDEGuGc5xX4ab8zPS8CrcAyNEne7ydndk7GTcWjUqhykDNLXeulyGdZVTQ87IQhaR2woLEsAOhC3gKXDdXjOiX4TUXB3OJkkl9pxkaeUCrT1v%2Fu0s0aU6gGKycb2RA%2FWNwqXgyEbYEh%2BWQ%2BOTy5Olnu4BKy3MpIOC8EJzBF6QHY6v63kKaMcDNYOaCA3LhRQEjKOcZpLdZnALb8wLoPeWt0sJprCajjW7lMXuunZmxrxfohPCpBwaOgDuVHiLZKFVnXwIMHWpgdzMPZbieq0ZPV9psgQ2nLWmemmzPD405M4jyHQ%2FFaj9wVNt2Rl2npfSRfidHYIFaeHimABmdFTsm8UeIglDYbSLeznSpKHZYXAqDqNANKBt8wPCtqM%2BrmThxxDm3nkcttMCDGwDt16sHCC39b%2BVGPp0dIZpv8ocFl%2FWwq0xqhENaj71cXEbGnOGaKhUR5t4gcKNpygXwmkhZjfn9BpUBv5186brjpVpR1IHXoYRvwhsJ9ZrrHgwNHqODnF1Cg%2FSi2UkDxzOKtYx4X%2BXyypGgmB%2B2QpZDRMqFloR9ut6MlR%2BJf1%2BVQf7r9RenrpTB%2BFcJ27u%2FqSXkbys1Yuy7%2F3ikjfzXopTtJhiKfu5JP5f1Tjx81GkBGI5FVWgOr6p1UVFNzGEifkRMJ%2B6%2F9IGOqUBQlllArJPJN9fLoEHSY0fM9qYcff%2BeUUtSXcXwSMF8dali%2BTDrcH%2BwozfQj1IP3wnM3ca%2BqVQnQ9t6o9Dbz6A3AsPNQ6d0z618FdrjCjB9CkmSShvV3tQ8w9e5g1m17NQ0PnDKicpvNrEGYyHmYGlAYh%2F28ve6ZIDIr0wGfTRnqRvTV5Dw07U6TEMX6ZBAnExFwi9nvSIFZLk%2BMl3LKvALqf0DBkE&X-Amz-Signature=c8ac6ab25cd3f80fa5c27f29501ee80927ba6e1823018aeee641a2de89fba61b&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

[image](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/7a4b0706-1035-4c53-abe3-d04a35ad8661/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XEYJZSTZ%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T225611Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIAnl5wJoNvxluc3dTL%2BFH0DdQ7vEB1VIQ8yjcHt1llacAiEAgiSDUFq601T4v4W6YhCLnkDa2oSZ4hJQLIgcxDpCNMQqiAQIxv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDEGuGc5xX4ab8zPS8CrcAyNEne7ydndk7GTcWjUqhykDNLXeulyGdZVTQ87IQhaR2woLEsAOhC3gKXDdXjOiX4TUXB3OJkkl9pxkaeUCrT1v%2Fu0s0aU6gGKycb2RA%2FWNwqXgyEbYEh%2BWQ%2BOTy5Olnu4BKy3MpIOC8EJzBF6QHY6v63kKaMcDNYOaCA3LhRQEjKOcZpLdZnALb8wLoPeWt0sJprCajjW7lMXuunZmxrxfohPCpBwaOgDuVHiLZKFVnXwIMHWpgdzMPZbieq0ZPV9psgQ2nLWmemmzPD405M4jyHQ%2FFaj9wVNt2Rl2npfSRfidHYIFaeHimABmdFTsm8UeIglDYbSLeznSpKHZYXAqDqNANKBt8wPCtqM%2BrmThxxDm3nkcttMCDGwDt16sHCC39b%2BVGPp0dIZpv8ocFl%2FWwq0xqhENaj71cXEbGnOGaKhUR5t4gcKNpygXwmkhZjfn9BpUBv5186brjpVpR1IHXoYRvwhsJ9ZrrHgwNHqODnF1Cg%2FSi2UkDxzOKtYx4X%2BXyypGgmB%2B2QpZDRMqFloR9ut6MlR%2BJf1%2BVQf7r9RenrpTB%2BFcJ27u%2FqSXkbys1Yuy7%2F3ikjfzXopTtJhiKfu5JP5f1Tjx81GkBGI5FVWgOr6p1UVFNzGEifkRMJ%2B6%2F9IGOqUBQlllArJPJN9fLoEHSY0fM9qYcff%2BeUUtSXcXwSMF8dali%2BTDrcH%2BwozfQj1IP3wnM3ca%2BqVQnQ9t6o9Dbz6A3AsPNQ6d0z618FdrjCjB9CkmSShvV3tQ8w9e5g1m17NQ0PnDKicpvNrEGYyHmYGlAYh%2F28ve6ZIDIr0wGfTRnqRvTV5Dw07U6TEMX6ZBAnExFwi9nvSIFZLk%2BMl3LKvALqf0DBkE&X-Amz-Signature=c7949de0a4d8e34167c0de47fb17b96bd2f39058153cab5d766cd3ac91737471&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

llo 慕课网的各位同学们，大家好，这一节又到了我们源码探秘的环节了。探谁呢？楼的 balance 注解好，这一节主要内容有三块，第一块我们先来看一下 load balance 的作用原理。前面大家在图文教程中已经对 load balance 的底层机制略知12，那我们这次再稍微深入那么一点。 OK 第二部分是我们来一起研究一下拦截器到 irose 的调用链路，那拦截器实际上也是瑞本的一部分，那它会把你的请求分发到对应的 I row 进行负载均衡。
最后一个部分我们看一下 IP in 机制。前面我们图文中跟大家展示了什么？隔山打牛这些 IP in 的策略，我们这就到代码里面实际的看一看它是怎么来实现的。好，超级家伙准备出发，每天扣定 1 小时，健康工作 50 年，看别人写出来的代码也能健康工作 50 年。

[image](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/b14fb86a-9a54-49b9-adca-e6467ba4b227/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XEYJZSTZ%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T225611Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIAnl5wJoNvxluc3dTL%2BFH0DdQ7vEB1VIQ8yjcHt1llacAiEAgiSDUFq601T4v4W6YhCLnkDa2oSZ4hJQLIgcxDpCNMQqiAQIxv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDEGuGc5xX4ab8zPS8CrcAyNEne7ydndk7GTcWjUqhykDNLXeulyGdZVTQ87IQhaR2woLEsAOhC3gKXDdXjOiX4TUXB3OJkkl9pxkaeUCrT1v%2Fu0s0aU6gGKycb2RA%2FWNwqXgyEbYEh%2BWQ%2BOTy5Olnu4BKy3MpIOC8EJzBF6QHY6v63kKaMcDNYOaCA3LhRQEjKOcZpLdZnALb8wLoPeWt0sJprCajjW7lMXuunZmxrxfohPCpBwaOgDuVHiLZKFVnXwIMHWpgdzMPZbieq0ZPV9psgQ2nLWmemmzPD405M4jyHQ%2FFaj9wVNt2Rl2npfSRfidHYIFaeHimABmdFTsm8UeIglDYbSLeznSpKHZYXAqDqNANKBt8wPCtqM%2BrmThxxDm3nkcttMCDGwDt16sHCC39b%2BVGPp0dIZpv8ocFl%2FWwq0xqhENaj71cXEbGnOGaKhUR5t4gcKNpygXwmkhZjfn9BpUBv5186brjpVpR1IHXoYRvwhsJ9ZrrHgwNHqODnF1Cg%2FSi2UkDxzOKtYx4X%2BXyypGgmB%2B2QpZDRMqFloR9ut6MlR%2BJf1%2BVQf7r9RenrpTB%2BFcJ27u%2FqSXkbys1Yuy7%2F3ikjfzXopTtJhiKfu5JP5f1Tjx81GkBGI5FVWgOr6p1UVFNzGEifkRMJ%2B6%2F9IGOqUBQlllArJPJN9fLoEHSY0fM9qYcff%2BeUUtSXcXwSMF8dali%2BTDrcH%2BwozfQj1IP3wnM3ca%2BqVQnQ9t6o9Dbz6A3AsPNQ6d0z618FdrjCjB9CkmSShvV3tQ8w9e5g1m17NQ0PnDKicpvNrEGYyHmYGlAYh%2F28ve6ZIDIr0wGfTRnqRvTV5Dw07U6TEMX6ZBAnExFwi9nvSIFZLk%2BMl3LKvALqf0DBkE&X-Amz-Signature=edb7d413d84ef89ff6dd702b8d19fb085182710078bc82efbf15a1d0114852fd&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

这一节我们先来关注一下 raben 的 load balance 注解。好，我这里打开哪个文件？ raben consumer 对不对？到它的 application 也就是闷函数里。好，我们把屏幕放大，那这个注解里面有什么玄机呢？我们在图文里面应该有学到过，点进去像大侦探探案一样，看看它的蛛丝马迹是怎么样启动起来的。 OK 那从这里大家能看到什么线索？没有没什么注解对不对？它上面 qualifierinherited documentary 都是非常平常的注解。那这个时候怎么办呢？从哪里入手啊？我们就看一下它的引用，这里调出来它的引用来看 auto configuration 大家记住， spring cloud 里面所有的组件你找它的注解的起始点，都从 auto configuration 里面来找，都能找到它的圆起圆面的开头。


那这里大家看到吗？它通过注解注入了什么？ rest templates 你定义了几个 templates 它这边就会有几个 templates 那他怎么知道这个 template 是我们想要的呢？你看到这里吗？这个 template 有点特殊了，它上面加了一个 load balance 的注解，大家看到吗？也就是说你通过里面 load balance 还有 qualifier 这些注解共同作用。假如你在前面的 application 里面类没定义这个 load balance 注解，那它在这里绝对不会把它注入进来。所以我们说这个 load balance 的注解就像一个传送门一样。


对不对？把你在外面配置的 load balance 注解的 rest template 给它怎么样？传送到我的 auto configuration 下面。那大家知道 rest templates 在这里面它怎么用不妨再看一下它的引诱。这里只有一处地方，非常省心。所以我说瑞本它真的是一个相当简单的组件。
很多工作十几年的程序员，那大家自己写折腾，折腾也是可以写出来的。那我们这里看它的方法叫什么？ lower balanced rest template initializer deprecated 好这么长的名字。那它跟这个缘起缘灭的故事开头一定有所关系了，我们这里不妨怎么样呢？不用再跟进去看，而是在这边打一个断点，把项目启动起来，一路跟下去。


实际上摸清一个项目，你通过注解的方式找到它的起始点以后，打上一个断点，一路走下来，一马平川，后面全部都明白了。但是这里有一个反例，当你碰到非常非常复杂的项目，比方说我们接下来在下一个大章节要学习的 high streaks 我天哪那个代码反正很绕，他用了类似函数式编程的方式。大家如果之前没有接触过那种方式，很容易蒙圈。知道吗？没关系，这是下一章我们需要面对的问题。
启动启有瑞卡 server 接下来给 ribbon 再启动一个 eureka client 这次我们不用启动很多 eureka client 啦，不用启动三大炮就一个就可以了。然后 ribbon consumer 以什么模式启动，以 debug 模式启动走起倒数 5 个数 54321 我这个 17 年的顶配 Mac 性能不行。看断点已经走进来了对不对？好，我把这屏幕稍微缩小那么一点。


大家看这里，它循环的这个 rest templates 是什么？就是上面我们注入的对不对？那它 size 是几一个，那是是哪一个？是我们前面在 application 这个类里面定义的这个对不对？ OK 我们看它接下来对，这个 template 做了什么？手脚好 for 循环。


走到这里，大家看这里有个 customizer 这个就是给我们做手脚的地方了，他这边的 customizer 是哪里注入的呢？是这个方法的入参对不对？方法的入参 rest template customizers 这个 customizer 从哪里来？又要到哪里去呢？好，我们看一下。它是 rest template customizers 这个注释进来的。那这个类大家知道它在哪吗？是在哪初始化的很简单，点进去是一个接口，对不对？看一下它的引用就得了。好，大家看这些 public 方法吗？这些方法都是生成 rest template customizer 的类。那我们这里就不用再继续深究了，知道它是由外面初始化的病注入进来的就可以了。


我们回到当前的 debug 端点这里看一看 customizer 对我们的 rest template 做了什么，手脚点进去发现是个接口，看一下它的引用。好就在这里。我们找到它在这边打一个断点，在这边打一个断点，你看他待会就会进来。好，我们这直接往后跟一步。没错，进来了对不对？他进来了做什么事呢？你看这里。


第一步，先从 rest template 里面 get the inceptors 我们看这个 inceptor size 是什么？是0，我们的 rest template 里面没有注入任何的 inceptors 对不对？接下来他这边安排了一个内应是什么？ Load balancer inceptor. 这个就是关键所在了。


大家知道这个 load balancer inceptor 是在哪里声明的吗？我们往上走两步，没事两步走两步停。看到吗？这个 static 类中做了两个事情，第一个事情就是声明了一个 interceptor 那它的入参是 load balancer client 和 request factory 那它用在哪里呢？没错，大家猜对了，就用在这里。那我 set the interceptors 这事就完了吗？还没有再点进去看一下这边怎么样，把 interceptor 和本地自己保存的成员变量做了一个比较，如果不一样，本地的 interceptor 全部清空。


引狼入室，把你给接进来，把你传入来的 intersept 替换回去，然后再 sort 一把。这个 sort 是根据什么逻辑来 sort 来我们就不管了英雄不问出处。好，那把它退回来。到了尽头，那这里就完了吗？没错，真的完了。好，接下来我们知道了 load balancer auto configuration 对我们的 rest template 做了什么手脚。那么这个手脚有没有起作用啊？ not yet 还没有，我们接下来就到它起作用的地方再来看一把。好嘞，这里我们先打到 load balancer interceptor 这个类里面，它起作用的位置，就在 interceptor 这个方法上，我们在旁边打一个断点，现在怎么办呢？现在就用 postman 实际的掉一把瑞本 consumer 走起。


好，这里来到了，那我们看第一步步骤是什么，往后走一步，从 request 里面 get 到 URI 然后从 URI 里面 get 到一个 service name 好，我们这里拿到了一个 service name 叫什么 eureka client 所以说这个 service name 并不是我本机的 service name 而是我要去访问的那台服务的 service nameok 那接下来往后走，这里有一个 assert state 那这个 assert 如果没过，会怎么样？会直接报错对不对？然后报出一个错误的提示是你的 UI L 并不存在一个合理的正确的 host name 那假设你这个 host 


name 都是合理的正确的。那接下来我会调用 load balancer 的 executor 方法，对不对？我们看它这个 load balancer 那叫什么名字。打开 expression get a class name okay 看它的名字是 ribbon load balancer client OK 那我们这里走到 execute 的方法里面，打一行断点跟进来，再往里跟一步，这里就到了正常执行任务的时候了。好，我们这里看到它根据 service ID 获取了一个 load balance 这个 service ID 是什么？就是你的服务名称对不对？要调用的服务名称。好，我们跟进去。那这里是从哪里获取到的？从 client factory 里面获取到的？好，拿到了负载均衡策略以后，我们通过这个 get server 来获取到一个真正的 serverok 往下走一步。


大家这里，看到 load balance 的 true server 没有，我们先不跟进去，直接点看一下。 OK load balancer 实际上这里就有三种实现。那我们到其中的 zone aware load balancer 里面，它的 true server 这里打一个断点，我们让它跟进来。那第一步是看你的 zone aware 是不是开启状态。 okay 那它这里说什么。


Zone aware logic disabled or there is only one zone.
你如果没有开启多个 zone 你的注册中心它就一个 default zone 那实际上这里不会给你自动的应用 zone aware load balancer 而是会怎么样呢？调用 super 的 true server 方法，我们到这里面先看一下，这里到了顶层的类 base load balancer OK 它的 key 是什么？ default okay 那这里往后走一步，counter increment 那我调用的次数加一对不对？如果当前的 row 是空，那么就直接 return 空，因为我们没有配置负载均衡策略，如果不是空的话，大家看这个 row 是什么，默认的 row 好看到吗？ 


random row 这就是我们给这个服务指定的默认的负载均衡策略，就叫 random row 那大家通过这个例子看到了什么？ ribbon 的结构是不是非常非常简单？我这里再给大家稍微的再理一下，从 interceptor 的 intercept 方法进来，然后怎么选择一个具体的服务呢？通过 load balancer 这个 load balancer 是什么呢？它的实现类就是 zone aware load balancer 而在这个实现的过程中，因为我们


只有一个 default zone 所以说它这边并不会启动中 aware 的功能，而是走到里面，通过它内置的一个 role 这也是我们在外面用配置文件指定的一个负载均衡策略，让他选择一个物理机器进行访问。
好，这个 choose 我们就不看了，前面已经读过他们的源码了。返回高高兴兴地拿到了一个服务器，可以给大王交差了。大王，大王，这是你的 server 不为空，那不为空怎么样呢？构造一个瑞本 server 对象，我们这里就先不用管它了，这都是支线剧情，大家感兴趣的同学可以进去研究研究瑞本 server 提供了什么功能？ OK 在最后一步的 execute 的方法里面这里就是真正的发起请求了。对不对？我们稍微跟一下，构造 ribbon 的上下文context ，这都非常非常简单。


OK 这一步往后，它的 return value 拿到好走到这里整个瑞本的链路在调用端以及瑞本如何初始化的这部分的知识就带大家过了一遍了，是不是觉得非常非常简单没错，瑞本真的是没有什么看头，非常非常简单。大家如果觉得稍微有那么一点困难，恐怕是平时阅读源码的经验并不足。那没关系，跟着老师把 spring cloud 的所有组件的源码撸一遍，你就顿时直升 100 级。以后阅读其他的源码真的轻轻松松，一目十行。好，那这一节我们就暂时先讲到这里，同学们是不是觉得漏了点什么？我大纲里面是不是还说了 I pin 这个机制。没错，我们把它分成两个小节，下一小节就带大家去仔细品味 I pin 机制。好，同学们我们下一期再见。


