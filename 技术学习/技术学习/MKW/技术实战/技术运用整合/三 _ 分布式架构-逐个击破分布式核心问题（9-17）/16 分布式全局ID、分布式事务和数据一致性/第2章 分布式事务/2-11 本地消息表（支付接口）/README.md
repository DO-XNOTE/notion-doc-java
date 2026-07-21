---
title: 2-11 本地消息表（支付接口）
---

# 2-11 本地消息表（支付接口）

[image](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/ef3d6450-8425-4081-92ae-be693eb5c6a2/SCR-20240808-erxe.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665ECRDCZJ%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T225435Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIH4J7V%2FvKMt9nKQEKtV7jyRnlHKKPTwpNxuQiquCbRzxAiASPWhh8pRechT4Z8b8ZBy79HjHiwQGilU8AcfbWrUgMCqIBAjG%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMQFB0u5ipVf8n1mrOKtwD45HjICUXDjuH%2FF8uyj8zAJNhTdrmXsy6Cp%2BPoHVSwUTnA8Tw3HWYrNsZUhY6RUDHgAJNy1bl3puoVsnlIASdBVIsToje3GLF192hDG2JZyaC%2BLS24QMKu8NPPho6CPK70DvS%2Fb%2BI1jZv7U8D3E%2BrgOyBfEMMsqnHzpfJLrVw2aJtx0%2B%2FbYAYzazFvMr2q9fw8vUbefXypfrBkqypAVq2HygkRDfaw35PPLPkpDLnecxsspZYNafVJwouaC0DVlX7%2Bp9B%2Fuhxo42D%2FdbgUmklZIG7H1zkhPVRZnB4aArT4ds%2B%2BQW6glAzys3xYXtQfb2k358A2nByVdkNtQpPuc8WBuQeKzQGwevldo75QdGgIKxqcy%2FCuCmdDqPSXhCCcY%2BryOuMmSVuPvTlloJvR2Fi1kemknxwpeydHDIlaMgB9n0PT6%2FCvj6xdf5GekDXaddVMV558n7ztIOxZF2BcKlYzCAUfqGqeQZsMB19ASdqwGx3UHn1b3c6KyTeg%2FrdhGVi5nDDBVVDoucNqXk%2FXHrcRCAeVHnFGkUEklkI4jnmRRFUmpYZ34SKG%2BT%2B4ppnDwWXlPFMgDTT%2BCIJDyRgVP%2Few8550JDYzT9P1HDxaElIzlNbaAyTxXr9hZyP%2BjYw1Ln%2F0gY6pgFGHoY7LnMp9OV0KWQ2oAFYObzlE1fHiXTuVOdC%2BvwfsZfGSHSHmgnIoAldd8FXLDF0wiPRdVj3DKtCLQmUio4xxxIPwrVI5NQ5gYXmv6gw2V04bZXNC8CXtDwS5nM35978Xu9Bopp2ZC5ZTzIenaPxPMrQtoRlEGxa231Ygw7zBEzwW8wx9j%2FKbrjC3Lscg5vLDH9VZWU%2B00aYm%2FTKrOHFh5g3lxvy&X-Amz-Signature=bf554b6be4dde2c9dbad9d4dc7d71c7fff7a58c3e8b7634823718929cd720f88&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

好，接下来咱们就开始编写程序。第一步咱们要先编写这个支付的接口，这块咱们也还是先新建一个service ，叫做 women are source service 然后打上一个 service 的注解。 payment service 咱们主要是操作 131 的数据库，咱们要把这个 account A 这个 mapper 给它引入进来， a mapper 加个 resource 还要把这个消息表的 mapper 也要引入进来。消息表 payment message mapper 对吧，也给它注入进来。


然后咱们要写一个方法叫做 payment 支付，这个方法咱们返回一个int ，然后里边第一个用户的 ID 然后点赞的 ID 还有一个支付的金额，amount有这三个字段是不是就可以了？把这个方法咱们给它加上一个注释支付接口。第一步咱们要根据用户的 ID 把这个 account 这条记录给它检索出来。 account a map.select grammar key 咱们传入这个 user 的 ID 如果 count A 等于空，这条记录如果没有检索到，咱们直接返回一个。 1 这个一代表什么呢？咱们给他备注一下。 1 代表用户不存在。
如果我看了 A 不为空，咱们要扣减它的金额是吧，扣减金额之前咱们还要进行一个判断，如果 account A 减 get balance 咱们要和这个你扣减的这个钱要进行对比，和他比，如果小于 0 是说明什么余额不足了是吧，你的账户的余额小于你扣减的钱数，那么明显是余额不足，咱们也要给他直接返回。 2 这块备注一下。 2 余额不足，后边咱们是不是就直接扣减了？啊看了 a.set a balance can you account a.get balance 然后减去。


最后 account a mapper ，更新一下 account A 的这条记录，这些咱们给大家备注一下，叫做支付操作。好吧，支付操作后面就是往这个消息表里边存放一条消息 payment message 咱们新创建一个对象，然后设置订单 ID 是吧，订单 ID 就是传入的这个订单 ID 然后 status 0 是吧，未发送为发送，再设置一个 failure count 也是0，这个是失败次数，这样是不是就行了。然后最后这个创建时间把这个 date 给大家引入一下，创建人春联是不是就是这个 user ID ，我给大家写一下，最后还有更新时间和更新人，更新时间，更新人第一次咱们设置的是一致，然后 payment message mapper 咱们要 insert 一下，要 insert selective 这样是不是就可以了？最后返回一个 00 代表成功。这样是不是这个方法就写完了？咱们再快速的回顾一下。


这个方法首先要进行账户的扣减操作，然后往这个消息表当中存放一条记录，这个方法是不是要加上一个事务，再加上一个事物，因为这两个操作是在一个数据库当中，咱们要保证它一致。如果出现不一致的情况，比如说这个账户你的这个钱扣减了，但是这个消息表并没有这条记录，那么也会影响到后续的订单的支付状态。所以这块咱们给它加上一个事务这个事务要指定它的 transaction managertransition manager 是什么，咱们还是到这个 config 当中去看一下是 TM 131 是吧，因为它在 131 的数据库指定一下 TM 131。好，这个 service 层就要写好了。然后咱们再写一个 controller 层，通过 controller 调用这个 service 先创建一个目录 controller 再创建一个 


payment controller 打上一个注解叫做 restrest control up 里边有一个 payment 方法，它需要传入三个参数，把这三个参数咱们直接给它复制过来，再把 service 给它注入进来。 payment service 下个 all to Y 这里边调用 payment 方法 use ID order ID amount 最后是这个 result 返回的结果。咱们把这个返回的结果给它打印到前台，支付结果加上一个 result 咱们加上一个 request mapping 这个名字叫做 payment 这个 ctrl 是不是就写好了，咱们启动这个服务，然后测试一下进入到这个启动类当中，咱们 debug 一下启动成功了是吧。


然后咱们打开浏览器，咱们访问一下， local host 8080，然后 payment 后边跟参数 user ID 等于 1 后 order ID 这个咱们还没有规划是吧，咱们随便，写一个010，最后扣减的金额 amount 等于 200 指向一下支付结果 0 是不是代表着成功了？咱们到数据库当中去，先看一下 account A 咱们刷新一下变成了800，再看一下这个 message 打开这个 message 的这张表，好，也有了一条记录了是吧。订单 ID 是 010 状态 0 未发送，失败次数也是 0 还没有失败。后边创建时间创建人时间更新人就不用给大家做过多的介绍了。好到这里，咱们这个第一个接口，支付的接口就写完了。



## 

