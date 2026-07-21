---
title: 2-10 本地消息表（数据库设计）
---

# 2-10 本地消息表（数据库设计）

[image](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/88ae676e-4bf4-4028-bfeb-d7d99759cf88/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XVOVVTJV%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T225434Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDvqDWQHXiSBXUkYkcn96s62GCDKkc%2BHxH%2FP69mTCpNZAIhAJUMZweEPe3skVehSSO88stshdWZ7oXj2eNDDwYUzutnKogECMb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgzUHreIOU1ER6a2we8q3APbA3rWJ9sD%2Fm479BWRBpGTDliKnU25Occ4O7lTxLjLYEGq9DxzDLREK1Qw2T9T3%2B0NVJn%2BRXH8pc0NODAFE9QvozUrwtQyfn76skWPmULI7kLZEgxVuDyFZEEP%2F7oIg7k33vz0tCAUJAeB3O35oLaWpFTpNFR9fjn3mTpHxs9EVoaPG9xRzIzabRdjvOoR2p8Z5WwJ7Vxx6k6DGRduEDUUhYmXry8a8iSNBtWg%2FPKt%2BMt19wUyxaD5zPNx0uk6NQHl5z%2B3dZ6gGJFWgXWGX5zvsA3Keh21PsZMIrzAQRtsxwOW3uytSl8A7962DYbHTDgKjsJcBIiw8XAGtgEYpbALF2pAm0MXpXpZgHNsFeSo%2Bc%2BZTdSG%2F829ggVIve7DHsHgTylxNow1CvQwaRq5jugeCt3%2B8KR6fct4ZQrbNwJjhByTAigiZ3DzureVt1%2B%2F6DNZwjfGiS08iZJ3c6GiWCYylKosd6mTFxV%2FzTiID6sOU%2Bt6d%2FpM8IO3BN1QeN%2Fj7%2FrX9Aq%2BrqhVjCmZmtr8MdbwVnTqSa2Q95K0ZnNGbaKs0RssiQAUzQWBYVK5tSNgUYzPYfEgRLGfunWNBDLiYL9rrQOs83Lc0K6JFmom23pv5HRMK65okIOmVBPpnTCsuf%2FSBjqkATN%2BCxQR1wzuZadpBgIOzhlPT%2Fs6c6Z5gzbwOjBr4rrRVQ6hoHwkJwcCU0xCXRqrpA1F96midkZgFptVzL%2BMtB7pXJJlxu85w0f%2BRvNs%2Bu6bkzwFs4yM3VgwAu4cAs7CLO2CTLR9z%2Fn3y5OYScfP7jQwjMt3C891iH6KZbR9fwzfA%2B4QxFFunlDqP6yYFtUyzhXQ2EFXVYniIBone988Q6JU9lUX&X-Amz-Signature=b7773ba5605f3a3317e78d9e7dcb18718e274df6138a045283ba295cd682afef&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

好在具体的编写代码之前，咱们还是规划一下这个数据库，咱们打开这个内微 case 还是看一下上一节的内容。上节当中咱们使用 131 和 132 对吧，咱们还是接着复用 131 和 132 这两个数据库。这个具体的 schema 咱们还是使用 xa 131 和 xa 132，咱们来看一下。


xa 131 这个数据库里边有一个 account A 了是吧，那么咱们就用这个 account A 作为一个业务表。那么 xa 131 咱们作为支付的数据库，一会咱们模拟一个例子，支付的时候要扣减，要看到 A 表当中的用户的余额，等于是他支付了用户 A 支付以后，我们要在这个消息表当中记录一条消息，咱们这个消息表现在还没有，咱们要给他创建一下。首先有一个 ID 字段类型， int 11 逐渐自动递增。然后这条消息它是哪一个订单 ID folder ID 他也是 int 型 11 位显示非空。然后这条消息的状态 status 才行，咱们用 1 位就可以了。默认是 00 代表什么代表未发送。然后一代表，发送成功。二代表超过最大发送次数。咱们有这三个状态就可以了。


这条记录进来以后，第一个状态是未发送，然后发送给这个操作的接口。操作接口如果返回成功，那么咱们把这个订单给它设置成为 1 是吧，把这个订单状态设置成为一代，表示它发送成功。如果超过了最大的这个失败的次数，咱们给它标记成为2，说明他需要等待人工的处理。咱们使用这三个状态就可以了。然后再加上一个失败的次数，failure countcn T 也是 int 型，咱们也是设置成 E 位就可以了。默认是零失败次数，最大五次。如果超过 5 次它还没有发送成功的话，咱们就把状态给它标记成为失败，需要等待人工的处理。


后边就是最基础的四个字段了，创建时间，创建人更新时间，更新人 create user 然后更新时间，更新人是吧就可以了是吧。咱们保存一下表的名字咱们叫做 payment message 保存一下 131 的这个数据库当中有了两张表是咱们操作的时候先要扣减。我看了 A 这个表当中的这个用户的钱是。然后往这个 payment message 这张表里边插入一条记录，然后定时任务轮询出这条消息，然后给操作接口去发送通知。操作接口接到这个通知，他操作 132 的这个数据库。


132 的这个数据库扮演的是一个订单数据库的角色。这里面咱们创建一个订单表，要更新订单表的这个订单的状态。咱们也是简单的创建一个订单表订单的 ID 然后订单的状态 0 未支付 1 已支付对吧，咱们就写这两个状态，然后其他的订单的金额 or the amount I see more 10 位两位小数。然后就是收货人的一些信息了是吧。


Receive user， receiver mobile.
有什么其他的信息吗？其他的信息咱们暂时先不写了是吧。最后四个常规的字段， create user create a time。


这个 user 还有一个 update time 我们保存一下名字咱们叫做 tea order 是不是就可以了？咱们一会要更新这张表的信息。好到这里数据库咱们就设计完了。然后咱们在项目当中要生成表的映射，咱们打开那个 idea 项目咱们还是复用上一节的内容。上一节内容当中咱们取了一个转账的操作是吧，转账的这个操作也是操作的 xa 131 和 xa 132 这两个数据库。咱们这一节的内容支付的这个示例，这些表也涉及到了 xa 131 和 xa 132 这两个数据库。所以这块咱们就直接复用上一节的项目。咱们还是打开这个 my business 的生成器，咱们把这个两个表给它映射一下。


首先咱们映射的是 132 的数据库，这个数据库当中咱们只有一个 O 的表，咱们再看一下只有一个 O 的表，咱们把这个给它复制到这个项目当中。 table name T order 映射成的实体类的名字叫做 order 然后咱们点击右侧的 Maven 选择插件，双击买 badcase 生成器，没有问题是吧。然后咱们要映射这个消息表，消息表在 131 这个数据库当中，这块咱们要统一的修改一下，所有涉及到 132 的地方，咱们都要给它改成131，我把这个表的名字给它复制一下 payment message 映射的实体写的 payment message 然后咱们生成一下。


好也没有问题是吧，咱们在项目当中检查一下 131 是吧，有一个 account A 有一个 payment 这个没有问题是吧，一会在 account A 里边去扣减这个用户的金额是然后在消息表当中创建一条消息，然后在 DB 132 当中去更新订单的状态。到这里这个数据库咱们就给大家设计完了。下一节咱们正式的进入到编码阶段，编写这个基于本地消息表的这么一个示例。好，谢谢大家的观看。


