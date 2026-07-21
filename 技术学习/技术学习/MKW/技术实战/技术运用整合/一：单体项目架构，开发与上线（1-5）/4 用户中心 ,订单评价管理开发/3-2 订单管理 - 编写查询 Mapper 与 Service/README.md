---
title: 3-2 订单管理 - 编写查询 Mapper 与 Service
---

# 3-2 订单管理 - 编写查询 Mapper 与 Service

[image](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/0fc92d8c-9d93-4941-921f-2d69b566b3fd/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SKHHXGF4%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T224730Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQClikljmc22vtHK8u6gMVC3T0k5uDsoB60jchNbdTjX%2FwIgMoOWqe66qFzXkGF0uVP0i89jcGSXDVU8Z27y%2FTGxDxwqiAQIxv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDDi5UNZBSfxZyS%2FTgCrcAzleIQKv8Nh7pxKGBK8wujDvXQpcj5puXsyvaCa75n5sN0X2OfJtInoLtHbsNJZCxZGQUDB7yoq0o8xS9U%2FpRZsg17bz8%2Fi2kcQroFsG3BBoNJrfs5Hi78kZ6oclZ1JWuuoa4JWuE%2Fxa2s693sgr72M%2F%2BTyxlwryGmQ%2FEKt9p%2Fl8PQ0tdRAIK1n8Buxdk%2FU4JXqzuqoDghXA8iIOfN%2BdZb6UVK8JGCNltn7JsyjQv2agEztJBOUwh%2FE66420lxZ6by5UO8pP3uM%2FnY%2BYaJikEyAMYAiTWnWLs2Pf5mVy34hYnGl3url%2BQ%2BGxebamF76qAhx0fJj%2BibE3xdZvI9QYcR5rFDgB7xrGciCPNpiW3HHEj1K7u%2FTavR6I4dLI0oTnJWtfQHKK5UJJ0hu0UMAXhdvt0TzsRYt2YwF5syNLhvP0UviHJTk8TYlkoHXmG6ixdwEZoOvgraUQ4BfxzsSS5%2Fni2Gk1VR9o4kduKhNc1VVpILsHe1cdy40cyV42I5YqzbeBxx7NMT2%2FvR4AWdRtE8UnKf3AZauU35O%2FNJKWvmxmL3HunExI23d4c4nbW3QV9PXEM1zGQ3O34Nd3wbfXwHriB%2FG15wPwjuypubyvrMIQOHPiqMBu9vSXO6lGMMy3%2F9IGOqUBfIUD5Stfp5OXNEEeSgthf6YPapmzBeliqO2q4gON4uxlfsCFyGPizLry9T0iRIabCyxW5XfIQ1aBbFxDSW4GxedN3ca1s8W9NPqN6Z1yZC5REHNWYoSDyGjfgTZMriCZjMo6Tqhr6jmVnuG6oDE2JD4KVWISnxSs0S2MMBszY9dQNnE%2FqMtmBL%2BW034IbHgydXXCEm5hIDhBaTRIZKzL1IQqlN5L&X-Amz-Signature=fad80b78da7a798f386caa11d9c5965720c303721932300ed9ca8d7c7b7e55be&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

这个就是我们上一节所写的一个查询订单信息的 SQL 语句，需要注意订单表和订单状态表，他们是一对一的。订单表和订单商品信息它是一对多的关系，这样是一对多。所以在我们编写 map 层的时候， map 里面的自定义的 SQL 语句，相应的，它查询出来的一个对象其实是包含嵌套的 list 的，所以这个是需要去注意的。

[image](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/597507e8-4c9c-450c-89f4-1086f5feea48/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SKHHXGF4%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T224730Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQClikljmc22vtHK8u6gMVC3T0k5uDsoB60jchNbdTjX%2FwIgMoOWqe66qFzXkGF0uVP0i89jcGSXDVU8Z27y%2FTGxDxwqiAQIxv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDDi5UNZBSfxZyS%2FTgCrcAzleIQKv8Nh7pxKGBK8wujDvXQpcj5puXsyvaCa75n5sN0X2OfJtInoLtHbsNJZCxZGQUDB7yoq0o8xS9U%2FpRZsg17bz8%2Fi2kcQroFsG3BBoNJrfs5Hi78kZ6oclZ1JWuuoa4JWuE%2Fxa2s693sgr72M%2F%2BTyxlwryGmQ%2FEKt9p%2Fl8PQ0tdRAIK1n8Buxdk%2FU4JXqzuqoDghXA8iIOfN%2BdZb6UVK8JGCNltn7JsyjQv2agEztJBOUwh%2FE66420lxZ6by5UO8pP3uM%2FnY%2BYaJikEyAMYAiTWnWLs2Pf5mVy34hYnGl3url%2BQ%2BGxebamF76qAhx0fJj%2BibE3xdZvI9QYcR5rFDgB7xrGciCPNpiW3HHEj1K7u%2FTavR6I4dLI0oTnJWtfQHKK5UJJ0hu0UMAXhdvt0TzsRYt2YwF5syNLhvP0UviHJTk8TYlkoHXmG6ixdwEZoOvgraUQ4BfxzsSS5%2Fni2Gk1VR9o4kduKhNc1VVpILsHe1cdy40cyV42I5YqzbeBxx7NMT2%2FvR4AWdRtE8UnKf3AZauU35O%2FNJKWvmxmL3HunExI23d4c4nbW3QV9PXEM1zGQ3O34Nd3wbfXwHriB%2FG15wPwjuypubyvrMIQOHPiqMBu9vSXO6lGMMy3%2F9IGOqUBfIUD5Stfp5OXNEEeSgthf6YPapmzBeliqO2q4gON4uxlfsCFyGPizLry9T0iRIabCyxW5XfIQ1aBbFxDSW4GxedN3ca1s8W9NPqN6Z1yZC5REHNWYoSDyGjfgTZMriCZjMo6Tqhr6jmVnuG6oDE2JD4KVWISnxSs0S2MMBszY9dQNnE%2FqMtmBL%2BW034IbHgydXXCEm5hIDhBaTRIZKzL1IQqlN5L&X-Amz-Signature=b486f22bd6203093dcc9f67784f92304a1242459f9c07f993c30db598989f992&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

[image](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/982b1a9b-0518-436c-a4eb-7f455bad9bf7/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SKHHXGF4%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T224730Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQClikljmc22vtHK8u6gMVC3T0k5uDsoB60jchNbdTjX%2FwIgMoOWqe66qFzXkGF0uVP0i89jcGSXDVU8Z27y%2FTGxDxwqiAQIxv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDDi5UNZBSfxZyS%2FTgCrcAzleIQKv8Nh7pxKGBK8wujDvXQpcj5puXsyvaCa75n5sN0X2OfJtInoLtHbsNJZCxZGQUDB7yoq0o8xS9U%2FpRZsg17bz8%2Fi2kcQroFsG3BBoNJrfs5Hi78kZ6oclZ1JWuuoa4JWuE%2Fxa2s693sgr72M%2F%2BTyxlwryGmQ%2FEKt9p%2Fl8PQ0tdRAIK1n8Buxdk%2FU4JXqzuqoDghXA8iIOfN%2BdZb6UVK8JGCNltn7JsyjQv2agEztJBOUwh%2FE66420lxZ6by5UO8pP3uM%2FnY%2BYaJikEyAMYAiTWnWLs2Pf5mVy34hYnGl3url%2BQ%2BGxebamF76qAhx0fJj%2BibE3xdZvI9QYcR5rFDgB7xrGciCPNpiW3HHEj1K7u%2FTavR6I4dLI0oTnJWtfQHKK5UJJ0hu0UMAXhdvt0TzsRYt2YwF5syNLhvP0UviHJTk8TYlkoHXmG6ixdwEZoOvgraUQ4BfxzsSS5%2Fni2Gk1VR9o4kduKhNc1VVpILsHe1cdy40cyV42I5YqzbeBxx7NMT2%2FvR4AWdRtE8UnKf3AZauU35O%2FNJKWvmxmL3HunExI23d4c4nbW3QV9PXEM1zGQ3O34Nd3wbfXwHriB%2FG15wPwjuypubyvrMIQOHPiqMBu9vSXO6lGMMy3%2F9IGOqUBfIUD5Stfp5OXNEEeSgthf6YPapmzBeliqO2q4gON4uxlfsCFyGPizLry9T0iRIabCyxW5XfIQ1aBbFxDSW4GxedN3ca1s8W9NPqN6Z1yZC5REHNWYoSDyGjfgTZMriCZjMo6Tqhr6jmVnuG6oDE2JD4KVWISnxSs0S2MMBszY9dQNnE%2FqMtmBL%2BW034IbHgydXXCEm5hIDhBaTRIZKzL1IQqlN5L&X-Amz-Signature=cb54a5a78b90ae014dbd85318c0b390fd5d6031475b86cd02b106b43a25c5ad8&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

好，回到咱们的代码，在这里面我们先来把 map 创建一下。目前其实我们并没有订单的自定义map，所以我们创建一下。我们拷贝一个category，因为我们之前在做分类的时候，其实会涉及到一个嵌套，所以我们直接在这边拷贝一份，取一个名字，叫做 orders map custom，取这个名称好。OK。随后我们还是需要去创建它的一个接口，在这边创建一个 Java class，选择一下，选择 interface 好，创建一下好，OK。在这里面我们就可以去编写相应的代码。


首先我们先要去定一下调用 map 层的一个方法的名称，取个名字叫做 public board，它会有返回的list，我们写上一个 list 类型，我们先不写，取一个名称，叫做 query my orders。好。在这里面你是需要去传入相应的一个 map 的，这个 map 我们找一下以前所写的，用这个把直接贴过来就行了，因为我们直接也可以传一个map，把参数放到 map 里面去也是可以的。


随后我们就需要来完善一下咱们的一个 circle 了。在这个里面，我们先去把一些没有用的先删掉，先没有用的这些都拿掉。这是 SQL 语句。 circle 先删掉，它会包含一个result， map 写过，不需要了。好，就保留这些。随后在这里面去做一个修改。先来改我们的 Mapper custom，这是命名空间，你是需要去贴过来的。贴过来之后，在这里我们先把思考语句可以先拷贝过来。把这里全部都拷贝。贴过来之后格式化，我们按一个 tab 键。好。OK。这就是我们的一个 SQL 语句。其中在这里 user ID 是需要去传进来的。所以我们在这个地方应该要这样子写一个参数 pubs map，点 user ID，这个是作为 map 里面的一个key。


好，除了以外，我们在下方应该还要再去追加一个条件，这个条件是订单状态。因为其实在我们的页面里面，其实看得出来，我们在一开始默认的时候是查询所有的订单所有状态的一个订单。除了这样子的查询方式以外，还可以通过它的不同的订单状态去查询，也是没有问题的。所以在我们的代码里面，在下方我们是需要去加上一个 if 判断。


我们要判断一下传入进来的一个订单状态有没有这个key，就叫做 order status。我们要判断不等于null，不为空。如果不为空，在这里我们可以来追加一个条件， and 追加一个 order status，应该是OS，就是 o s 点 order status 拷贝一下。这个状态要等于传入进来的订单状态，也就是根据订单状态的一个值去做相应的查询。好，这个就是判断语句好。


写好了以后来看一下它的一个ID，这个 ID 的名称是需要和我们 map 里面的命名空间是需要一致的方法。另外我们传入进来的一个参数应该是一个map，所以我们在这边要改一下，改成map。另外还有一个对应的是 result map，这个是结果值，在我们取一个名称，就叫做 my order 买欧的CPU，这个就是会提供到前端，让前端去进行一个渲染的。在这里我们的 result map 其实要和这里对应，所以 ID 要保持一致。另外 results map 需要映射到某一个entity，这个 entity 在这里，其实我们是需要去创建一个，其实我预先已经是创建好了，未来方便可以来看一下。在这里找一下。有一个 pojo 子工程，在这里面会有一个 my orders 双进一下。此外还有是一个 my subs order item，这是一个嵌套的list，我也是预先的创建好了，可以来看一下。


这个是用户中心我的订单列表的Bo，这里面的一些相关的属性，其实和我们在这边所查询的一些属性都是一一的映射好的。除了以外，我们还有是一个嵌套的VO，这个 VO 是作为一个list，是放到了 my orders VO 里面去，可以看到这个其实就是订单的基本信息和订单商品，这两个是一对多的关系，那么多的一方就会以一个 list 的提示存在。它就是一个嵌套的。好在这里面我们把写一下，只需要把这个名称写过来就行了。买 orders u 好。随后下面要去做一个映射的。


第一个是 order ID，这是它的组件，写过来。随后是 create time 创建的时间。下一个是支付的方式，随后实际支付的金额写过来。再来一个邮费，下面不够了，拷贝一下，邮费 post amounts。再下一个是订单的状态，OK，这些就是我们订单的一些姓氏。


随后就是一个嵌套了。嵌套。在这里我们先把嵌套所定义的一个属性名称写过来，它的类，把它的类名贴过来，这是 of type。好在这里面我们就需要去设置它的 result 了，它是没有 ID 的，它是没有组件的，所以我们直接就可以把它的一个 item ID 一个一个的贴过来， item name 以及是 item image。好。随后我们还要去设计它的一个规格，规格是涉及到 ID 规格的名称，以及是购买的数量，还有是一个 price 价格。好。OK，这样子已经是印制好了。一定要注意这里面所涉及到的这些内容是column，是我们的一个查询 SQL 语句里面所对应的一个别名。


property 的属性是需要和我们的一个 view 里面的属性是需要一一的去做好对应的，一定要注意好，这样子我们的 map 就已经是 OK 了。 map 写好以后，再把它的命名空间所对应的接口方法，它的一个 list 返回的一个 list 的类型，对应应该是买orders，你需要把它写过来，写过来之后 map 就已经是写好了。写好了以后我们还需要去创建一个对应的 service service，我们来找到service，全部展开。在这边我们可以去创建一个，我们拷贝一份，取一个名字叫做 my orders，service。在我们会有一个实现，直接拷贝一下买 orders service 时间好。在这里面我们直接就去做一些相应的修改。首先我们应该要去把它的 service 改一下，这里面的方法我们全部都拿掉，重新的。我们写一个方法，叫做 public 返回的一个参数，使用 page 的 grid result。因为我们的是涉及到分页的，所以配置的 grade 这个类型是需要去写一下的。


学名字 query my orders，传入相应的参数。首先第一个用户的 ID 是需要去传入的，第二个是订单查询的一个状态 order status。我们换一下行。随后下一个参数，应该说是下面两个参数。下面两个参数都是和我们分页相关的，一定要去写。所以一个是配置。再来一遍是 page size。好。OK，这个方法写好了，加上一个注释，查询我的订单列表。好，这是我们的接口。随后来到service，我们把它的实现去进行一个修改。先把下面的没用的先全部都删掉，删掉以后在我们要去实现的应该是一个接口 my order service，在这边它所涉及到的一个map，我们注入的时候应该要注入一个我们刚刚定的 order map custom，注意一下好实现。我们重新的去写一下，把实现给导进来。现在我们就可以去把这个方法去进行一个完善了。


首先我们是需要去构建一个 map 版，也就是我们的一个传入的一个参数，写一下，把 map 要去进行一个定义，直接可以直接把它用一下。在 map 里面点put，第一个参数就是用户的ID，需要去写一下。第二个参数，点put，一个订单的状态写进来。好，两个参数都已经是 OK 了，但是需要注意订单状态它是有可能会为空的，所以我们在这边要去加上一个判断。只有订单状态不为空的情况下，我们才会在 map 里面去放一下我们的订单状态，所以要去加一下不等于空，所以我们才会把这个给加进去。


好。参数有了之后，随后我们就可以去做一个查询了。查询通过 map custom 点 query 买orders。把 map 给传进去了以后，在我们会接收到一个list，取一下它的类型是买 orders e o，这是一个结果集，是list。好，这是普通的一个查询，要去实现分页。在这里我们要去加上一个配置。 help 点 start page 开始分页。第一个是参数去配置，第二个是 page size 需要传入进去。好，OK，拿到的一个 list 了，以后我们要去做一个设置，这个我们拷贝一下。以前的以前我们是写过的。在一个商品里面会有一个分页，其实也就是这一块内容有一个 set 配置的great。把这一段的方法我们拷贝一下，贴过来。贴过来以后在这里我们就直接可以 return 了。有证的时候第一个我们把 list 我们要去传进去，下一个是配置，直接把第几页的写进去，这样子就 OK 了。


这个其实大家可以在统一的去写一个 base service 来做一个制成，通用的一些方法可以写进去。在这里我就直接偷一个懒，把这一段代码贴过来。好，这样子我们的 service 就已经是写好了。

