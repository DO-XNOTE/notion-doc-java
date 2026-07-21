---
title: 1-2 收货地址 - 查询收货地址列表
---

# 1-2 收货地址 - 查询收货地址列表

[image](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/0541f9c3-8b98-45d1-b8c9-025add2a1ce8/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46662RBGXT5%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T224657Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCICaa1JJ5ijBHzTy212dkess36YeZ15WafX9venv7zpPZAiEAp%2F8QsHJZ0nPp9qs3xLzHwQNebKNUCJJEZu%2Bubf5lqvkqiAQIxv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDEed8UInaGXDTufy5CrcAxoB1espKeQx2XxjcoEj0pyf7ZPrMhqSKh7UA6LNMFexkHH0BXhBXQbYk%2BbPOkWl%2Ban%2Brl3BKhVMo7Nx5xGNBW84kbKfa%2B1Myq31a8nusS%2FG20FmAOYEDWU6xkkriXvD9egvQFE%2BkPZFKgwthgaNpnj6xhH6waz1T7hkp9RBze2dmjPTmWX6YWHPKoMUTAwVS%2Fd%2Bty4WYghGsna1vGJRRNSbYhIECe7eLP1Tc4cbaUjjZnfsvEOYIiXp90iSvoOjpT4VjIrlEo0pLgQcuEX4RGHQZ6U7bTA1ENk8e3YsNnPTjCrreDoyLZO7FMpbr9%2BjmtDcHovRdiutIsj62gTnNjL9YPtyLAyv8L28uZGjR8fJfeITm5Iydvto016dY0cWKccozrxzyKtlufpM4ObbrAY4s5NYPy5UNMUM609Qz5toNLg0bfV7MCzt6w%2FipxQHJua%2FaPI%2F4of8b4kHPg0S3v%2Bxr6KslS%2FxLLlIblFL%2FxRDLw4rNa9CbFznpHrAAWxlN0s3VidRV2cDfndY5QvXjISMS%2FBa0dG496zY1NBSQoVAbZRqcuFddc3lGXz3SkTVTJQzAkR4F9TSeI7uFwaq2GDuEA5XS0JCQ4C5Er7zaImc3fJ7xgjWV0YKcsxQMJ66%2F9IGOqUB%2FWO2O8jeQu6DBa2dV3nTzkZXGYqlEw7teHRaerpwi64QFQuURYC0WgBV%2FUlquVKERYGnOABPbpXAE9IX7kKgl1udIeLVyyp5dy8UPPP95GYOMP0ri%2BeU7ca7lCplPuNQ9kfqau3LwcyChb%2BZe1hIn5zuJg7aEWwmOcBtYqv03XDkSj00xA3QMSRZ26zfr3SR%2Fj2q8JStdqNIbqCJ%2ByS4S1ZEFTBc&X-Amz-Signature=a2d40e315d80024f691c91c713b1f6c623c2580e5218dbae7e8703cf0f353dc7&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

上一节课我们是把用户的收货地址几个相关的功能梳理了一下，并且我们也去看了一下数据库的表设计。这一节开始我们会针对这些功能一个一个的进行相应的代码的编写和讲解。第一个应该是查询用户的所有收货地址列表，打开数据库，在我们的数据库里面，其实在这一张表里面现在没有任何的数据，所以我们查询出来，在页面里面展示的时候其实也是没有的。但是没有关系接口我们还是需要去做的。我们可以先来看一下咱们的前端，在前端页面里面，我们可以先去看一下，我们可以先来搜一下有一个 credit 的，这是我们的生命周期函数开始就会运行的。先找到渲染地址信息， JS 找一下这个方法我们看一下。在这个里面，它主要是发起了一个请求的路由为 address 杠list，它会截断一个 user ID。 user ID 其实就是用户登录以后的 user ID，因为既然是用户已经到确认订单页面了，用户就必须要登录，所以 ID 要携带过去。并且后端也是根据 user ID 去获得用户的所有的收货地址。随后它还会有一个海德斯，其实我们暂时还没有用到，我们在后面用到的时候会跟大家去说一下。虽然前端有，但是后端不用其实也是无所谓的。


好。随后在这个下方是用户的一个调用成功，如果用户调用成功，我们只需要关注200。在这里面会拿到一个 address list，随后在页面上去进行一个渲染，通过 this 点 address list 就可以达到相应的效果。在页面上肯定也是通过 feel 的 feed 杠 full 标签去进行一个渲染的。随后在下方。因为我们在页面里面，其实之前也说了，它会有一个默认的收货地址在页面进行加载，只要是它有地址，肯定会有默认地址。默认地址在一开始进入的时候，默认的帮我们选中，所以相应的脚本在这里可以去搜一下。在这里可以来看一下。


传入进来一个 address list， address list 里面其中肯定是有一项，有一项地址，它的 is default 是唯一的，判断是 1 了。以后我们可以在页面上做一个标记，我们可以设定为一个变量，叫做 choose 的 address ID，在页面里面这个 ID 就已经是有了。随后我们可以到页面里面去搜一下 address list。在这个部位可以看一下有一个循环， figure for 的一个循环，选中的它其实是会有对应的一个class，它是一个样式，在这里它会有一个表达式，这是一个 default address。在这里它还会有一个判断当前这一项的地址，它是否和默认需要选中的地址的 ID 相等。如果相等class，它的样式是可以去进行一个显示的。OK。当然在这里面它还会有一个 click 事件，因为用户是可以在这里面去进行点击的。


如果触发click，可以来看一下有一个 choose address，它其实就是切换选中的效果，把 choose 的 address ID 重新的去进行赋值就可以了。


OK，好，现在我们就可以来看一下我们对应的list。我们要去把路由所对应的接口去进行一个实现。好打开我们的后端，我们先在这里面我们得把 request my pin 先去写。好吧，这是一个 address 写好了以后，对应的我们的一个接口就可以去写了。首先我们还是要先写一下service，先写service，再写 control 了。这里面目前没有address。其实 address 可以写到 user 里面。但是我们为了区分一下，我们还是新建一个拷贝一下，把凯尔斯尔轮播图去拷贝。轮播图里面的内容比较少。 address service 好，我们再到这里面把实现再去重新的写一个。好，有了在改掉改成 address 的。 service 在这里面相关的 Mapper 应该是 user address Mapper 吧，把改掉好，OK。相应的在这里面所涉及到的一个方法名，我们应该也可以叫做 query or 返回的内容应该是 user address。


OK 这个注释重新去生成一下。先把改掉传入进来的是一个 user ID，根据用户 ID 查询用户的收货地址列表。在这里面。在实现里面就把这个方法去进行一个重写。这样子咱们去完善一下就 OK 了。写一个 user address，我们以一个对象的形式去做一个查询，定义为UA，把它给用出来，在 UA 里点 set 一个 user ID 好，这个对象就已经是有了。以后我们就可以直接通过 user address map 点select，它有一个 select 方法。在这里面只需要把这个对象传入进去可以了，它会发现这个对象里面它包含了一个 user ID， user ID 是有值的，它就会增加一个 user ID 的条件去进行查询。好，我们只要把 UA 传入进来就可以了。很简单，这个 service 其实我们就已经是写好了。随后我们在前端只需要去编写一下调用的接口就 OK 了。这个接口我们找一下以前的，直接拷贝一份就可以了。


贴一份过来，主要是把这些有一个架子，以后我们就可以去做一些修改了。这是 slack two，根据用户 ID 查询收货地址列表，拷贝一下，在这里进行一个覆盖。随后 method 其实我们刚刚看到了，在前端我们定义为一个post，所以我们在后端也要把它改为post。收货地址其实我们是可以把它作为是一个比较隐私的一些信息，所以我们可以把它定义为post。当然你定义为 get 其实也是没有问题的，我们在这里边统一设定为post。

好。路由地址在这边是一个list，好 list 写过来传入进来的参数在这里就不是一个 pass 的参数，它是request。 Tom 传入的是一个 string 类型的 user ID。好OK， user ID 其实我们也要去判空一下 string you 跳点 is blank，如果为空，我们就直接返回一个空字符串吧。错误的空字不算。在我们要引入一个 service private address service 把它给注进来，使用 address 点 query all user ID 传入进去。好，随后我们就可以得到一个 user address 的list，再把这个 list 直接给丢出去，这样子前端就可以获得相应的一个 list 数据了。

我们现在就可以去进行测试了，只不过我们测试其实是空的数据，空的数据也没有关系，等到我们做完添加地址接口，把相应的数据给展现出来就可以了。在这边只要我们通过 swag to 去测试，只要接口可以被调用，并且返回的是一个空的 list 也就没有问题了。


好，运行成功，我们到咱们自己页面来刷新一下。刷新很显然是没有任何效果，因为它本身就是一个空数据。我们到 swag to 刷新一下，找到我们的收货地址相关的接口，在这里面点击一下在线调试，填入一个 user ID。我们到数据库里面去搜一下，搜一个就选第一项，选和我们当前登录用户是一样的。 m k 123 填入过来，点击发送。它的状态是200，只不过它的 data 是一个空的数组，所以我们接口可以成功了。我们后边再把新的地址添加以后，我们再来进行一个查询就 OK 了。因为在添加完毕以后，它会有一个回调，会重新的去进行地址的渲染的。OK。

