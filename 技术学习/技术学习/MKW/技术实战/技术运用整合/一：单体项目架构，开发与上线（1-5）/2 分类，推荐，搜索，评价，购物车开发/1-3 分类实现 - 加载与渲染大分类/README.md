---
title: 1-3 分类实现 - 加载与渲染大分类
---

# 1-3 分类实现 - 加载与渲染大分类

[image](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/daf9df86-9a59-423c-96a7-5ed3c57d26bc/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664CC6U2VY%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T224638Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIGVhUvFxgxEJ41FVP%2BFnShIIsKWspgwALt5SQRf3KEObAiEAxS2Q0chiOYI7MEMsADCu9PjqNhyfAxy3U9RjF3IighUqiAQIxv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDE0h8ni%2BQDblXZGPRircA0kc3lAthIqw39d0MgBesCotpyA8nmnt3mkgyymD4fz8qSKWIeKEyEWZ60BW7leISXX1qsCPLwzqDqEEUyYwOxFhG15OgRDHg%2B67U6AsbE6%2F0Y5gu7A%2FK1xSqmqiZF0QDS2Fk0f3e9%2BSM%2FNXNqKf0JZUWk0v1mjiq6flwW2GuE3rXAg1Z890vwNKymUtpuUPYGJ%2FxQyKxCB2h1EcEDS8OT0tbBAGD09L2JGsZDPIdTD0ia76ypVW1EpZL4sLm%2BwIedZBLCwH0uJkpLRxK2f5vZ6hLS7dBoqqVax3w6AvNcJhMNU8z4TsZU2XtzIJj2BYpb%2BRrb4jH5CWAimO8dYelzD9FgURG%2BUDbT8zII3llDJ%2BZPv36%2B2SpO6HSxoAKwys7koQiARVW21FEPK7821Xz2XOzqMU%2BcfWleQCO9hUpId6STJGhk2hitvCgn9JNzbZcwqmIf5Ogxi7Az80R0Zx9mtf%2BdEnE7DMzYhtgQYN4vnAA1%2F%2B9AX7ASXqQNfb6%2BWt%2BpLkZ5tb67FF2e1ygZSXCaLpd5%2BOjyfj%2BjfQTX5mYhT0TUaKSE0ebaRmc3YVNZySAKLuPpgP8aJXiWp0khtw3I7SvrqmC6F84VBEwohwKDW7Z2w4Ykz%2ByR7jCBVnMLG6%2F9IGOqUBqgxebiWKMifHK%2FXJBhelesqZ5l3Kgg0yZ0PmaFTeAdAv4a7ZOFkX6xu6UC375msg1fKMFBZb6zqgPBRj0rRNLC%2Bm8AuC%2BXGQc4F7HxiUrGonMuQRyM30zUMdGdyh0XdJn6%2FYkeWJidlKYTWoT4D2Q%2Fi5LEl82H5nykKYWoJr9OjquMPbN5b%2Fhh7c2%2BlSBJSSezMI2WCBcfiwyd78r5hZC%2FF9KEJo&X-Amz-Signature=5df4216b62026e0201a3a41852729dd0abcdb8f2a399b578e79a7915b1436bc5&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

上节我们分析了在首页上分类加载的一个需求，这节我们就可以来实现一下。我们在第一次的一个分类加载。我们可以先来看一下咱们的前端源码。在前端源码里面，我们可以先来搜一下。先搜到一开始定义 view 的地方，然后有一个 create 的，就是生命周期函数。找到有一个渲染分类 render categories。 category 其实就是分类的意思。我们来往下面搜， Ctrl f 搜一下。搜到在这个地方。也就是我们在一开始页面要初次渲染的时候，会调用这样的一个方法。这个就是查询大分类。 cats 不是猫的意思，是分类的意思，也就是 category 它的一个缩写叫 cats index。 cats 就是它的一个路由，没有带任何的参数直接去调用。如果查询成功，我们就会获得相应的数据，定义为 category list。这就是一个大分类的list。OK。随后拿到了相应的数据以后，就进行一次循环的渲染。循环信源在里面，包含了很多一堆的HTML。这个是使用的 inner HTML 的方式去进行一个赋值的。赋值完了以后会给他附上一个事件。这个事件也只要是在这边，应该会有一个解释。来看一下，这个事件是干嘛。


如果当前这个节点下没有内容，也没有子分类，则会发起请求去查询子分类，并且渲染到页面。如果有内容也有子分类，就不去进行查询了。懒加载模式。它的子分类其实就是一个 sub cat HTML，就是一段静态的h、t、 y 代码，如果没有发起一个查询，这个查询也就是 index subcat。这个就是第二次查询。第二次查询它会携带一个 root cat ID。这个就是一级分类的ID。根据一级分类的 ID 去查询 root 分类下所有的一些子分类。OK。拿到子分类之后，在下方又会去进行一个循环的渲染拼接。第三级分类，一级往下去拼接，再放到页面里面，这个时候就可以进行一个渲染了。OK。这是前端的一部分的源码。

好，我们可以来看一下咱们的数据库。在数据库里面在这边已经是有了这张表，这张表叫做 category 分类。我们先可以进来看一下它的数据。之前我们已经是说了它会有一个类别type， type 为 1 就代表它是一级分类。一级分类我们在这里总共是有 10 条，所以我们在一开始去进行查询的时候，只要根据 type 唯一就可以查询到这几个大分类的内容了。


OK，好，现在我们就可以着手去把这一块的代码先去写上。打开idea，我们也是一样，从下往上写。我们的service，来找一下。 service 应该还没有category，所以我们应该要去创建一个。在这边我们直接复制一份，直接取名为 category service。这个是我们复制过来的，所以这里面的方法我们是不需要的，我们要直接给拿掉。我们可以这样子重新取个名字叫 query roots level cat。查询根值目录下根值的 cat 编辑分类，不需要有任何参数。这个返回的也不对，返回的应该是category。写个注释。查询所有一级分类。OK，好，下方我们 service 直接也拷贝一份。我们懒得去再重新创建了。


category service，不要拼错 category 好，在这里面它要去实现的接口。 category service 好。这边的内容不需要 command 加i，直接导入抽象的方法。在这里 map 我们也不需要了，使用 category map。好，OK，现在我们只需要去把这个方法里面的内容去实现一下就可以了。相对来说也不难。我们只需要传入一个 tap 它的类型值就可以了。也是一样。我们在这里使用example，我们拷贝一下，速度更加快一些。我们前面已经是写了，直接把这一段代码可以拷贝，随后贴过来。在这里面，我们只需要把 category 给贴进来，我们不需要 order by。在这个地方，我们会有一个 equal to 育发兔。很显然，我们应该使用的是 type 类型。写一下，写在这里我就直接写 1 了。大家可以自己去写一个枚举，我节省一下时间，直接把写死为 1 就可以了。一般来说，其实对于我们的一个分类，它的 123 这种具体的值也不会去有过多的一个变动的。


下一个在这里使用 category map select by example。在这里拿到的一个 list 是 category 的类型。这个时候其实我们就完成了查询。完成查询以后，直接把 result 给 return 出去就可以了。这样子我们的一个查询大分类查询一级分类的 service 就已经是写好了。写好以后我们只需要再去完善一下。我们的一个接口到 index Ctrl，直接在这个地方去写。我们复制一下。在这边我们先把 slack two 先写好，这个是用于获取商品分类，加个括号。一级分类直接拷贝，把后面的 notes 给粘贴掉。


最后的一个 h t t p method。因为我们是查询，所以我们使用 get 就可以了。在这里是 get map 路由的地址。我们是cats， cats 我们在我们必须要和前端对应，叫前端，如果不对应，查询是查询不了的。方法名我们也叫做 cats service。我们就需要在这个地方，我们要去把 category service 给引入进来。好，OK。引入进来以后，我们在就可以发起一个查询，直接可以 query all root level cat。好，OK，拿到一个list，这个 list 就是 category 这个类型list，直接可以就丢出去了。


OK，好。现在我们就可以来做一个测试了，还是一样。我们是需要 install 一下，因为我们对 service 进行了变更，我们要安装以后才能够使用它的代码。 install 成功以后，我们重新去运行一下。好，现在启动成功了。好。打开浏览器，其实我们可以通过 SWAG 去进行一个测试，在这边也有。我们放大一下。首页展示相关的接口，在这边有一个获取商品分类，一级分类直接点发送成功，在这里面我们就可以获得所有的一级分类的内容了。OK，好，回到我们的首页，现在我们来刷新一下，看一下它的一个渲染的结果。刷新OK。刷新以后可以看到我们在所有的大分类一级分类在这边进行了一个展示。现在我们第一步骤把大分类加载实现，就已经是 OK 了。

