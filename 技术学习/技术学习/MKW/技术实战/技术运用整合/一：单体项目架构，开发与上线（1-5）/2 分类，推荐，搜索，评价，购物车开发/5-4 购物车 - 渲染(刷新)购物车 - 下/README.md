---
title: 5-4 购物车 - 渲染(刷新)购物车 - 下
---

# 5-4 购物车 - 渲染(刷新)购物车 - 下

[image](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/df3af7ee-06b7-44d1-b0eb-062e1f93cd8d/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VFDSZWXK%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T224652Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIDRKfMtjx%2BO3IfTOHuKql6dr6vn4qxq9XTWX3uSu%2BY%2FQAiEA12BjcurDCuY9ke%2BDs1fDONq%2B8rRvhKJIHXwgCAZOjT0qiAQIxv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDJ18mmPvuLFT8fBe%2FircA8INXKY1UX%2Fb390gWBcJGTprsGxClBvB48%2BCh%2FX%2FPQWco1IfrTE9gXOCAwm2un7EC1iVU%2FMQkBfQFmwIWF5pID9I9IxjDjA9tzZiALnIG1fNPENCf%2FwEDONiIAMG7A3Sb%2FzsQb7snhxg%2F4vVKudxRAs0gOjRySq8zse0dQT%2Fnz9yiAr0bnSXAZPH%2BFdwLhA7GE%2FhSSGrI%2B%2BUNEUCkyGNAT4549VuoLIO90qeDPzjF%2BW48zZqu4kj9U6PE18uTn%2FJPQxAWht020duaqxcmmE54wnjoUhWWhy2mmY78gPJ5rRvAkKNEYnstSRbk5WutyeDKVxQxZYhKARJ%2B8CNw8oo65mZG0JO82MFT8EbbXiZAg9M6U%2Fm%2B040ns5ywTicr2hxYzlMrNnbY1bOyU5WndBJOgwgfCf3Z3i5WYtgQQTg4%2FhhpJkKHIIQ7oLGafVoIf20LeqksO9rjYiDi1ziwcacbWkNXrMhB0egfxcalOse07BIuKmEC8ToLelPLp4Hd79g4s4ybimOhSiAfHONUat5iVLmbXk9HD2hOIZSnjAJ1qSfQYq38JJveU8NBUvIu8ML2myI2gFnRLgvlpKr1rdkmHIJp3ZoG8vq68ZHx4hrgyukXYVrFel6DYIwElzgMI26%2F9IGOqUBTZJep0HYOigUetez49qkSt5nHpvw4sMsbBQiVQLIWkKFNXfKtU3evOD40TkxjMF9f5YhnETyu%2BMBwcDF5WQ%2B495eagLI0L0APwkyfEzdgXTMarL6fsPkyHwxovlKfgKcVZ5WfaURfcZw73xwVy99hK7Kc6TWnLQjJpwdkGp%2Bu0Vp78M2rI2NqKsDqaR9pWjXQHvfpiuC1sPpVLQljp2CKejPX55m&X-Amz-Signature=11cb6e6601d8b485b7f590166721428c5e5504d2372f2134c08eedebe3d6233e&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

上一节课我们把 SQL 语句写了一下，这节课我们继续来把渲染刷新购物车的功能实现一下。既然是有了 circle 对吧？我们先把这一段内容拷贝一下。拷贝贴到我们的自定义 map 里面。由于是和商品相关的，所以我们就直接放到商品的一些相关的文件里面。在这里找一下。在这边我们就可以直接找 items map custom，双击一下。这个是需要的，这是它的接口。另外还有是它所映射的 XMAIL items Mapper custom，双击一下。


好，在这里面我们可以先去写一下。我们先找到最后找到最后先写一个 select 标签，好ID，取一个名字，来一个 query items by。在这里是通过规格去查来一个 s p e c i d s 好，我们是需要有一个参数，这个参数在这里我们会传入一个list，我们以前都是使用的map，在这里我们会使用到一个list，它会有一个对应的result。type。返回的一个类型是一个VO，我们先不写，把这一段代码我们先贴过来，以后对它的格式我们来一个 tab 键按一下。好，这就是基本的一些 SQL 语句。在这边会有一个返回的内容。


其实返回出来的一个类型，在我们之前所涉及到的 shop card Bo 可以几乎是一模一样的，除了抗死没有，其他的都是需要有的。所以我们就直接把 Bo 复制一份。也可以。我们在这个里面找到Bo，把 Bo 贴到咱们的 VO 里面去复制一份，把它做一个更改。 shift 加F6，可以直接快速的重命名，把这个改为 v o。好，点击重命名，在这个下方会有一个确定，点一下 do reflect 点一下，好，在这里面 shop cut c o 找一下，在这里就有了。双击一下以后我们是需要去修改的。我们把这个 by count 给删掉以后我们就直接可以去使用了。在这里面还有是一个 get 和 set 删除。OK，在有个 to string，不要了。好， v o 类返回到显示层的就已经是有了。在这个部位我们的 result type 就可以去写一下了。直接拷贝它的reference，拷贝一下好贴过来，这样子就OK。现在我们就可以去把这一段的语句再去做一定的优化，主要是在这里对吧。


我们的一个传入参数，其实应该是一个一个的去进行拼接。如何去拼接？其实在买 Betis 里面，买 Betis 为我们提供了一个 for each，我们可以一起来写一下。在这边我们写一个标签，叫做 for Bitch。很明显看到这个标签，我们应该知道它其实就是一个 for 循环。首先它会有一个collection，这个 collection 其实就是传入进来的list，也就是这个list，我们要给它定义一个名称，比方我们定义为 pumps list，这个就是我们传入的list，它的一个名称。现在我们还没有等到要传进来的时候，我们是可以去定义的。OK，好。这是我们的collection，也就是一个集合，它是一个list。随后我们要去定义一下我们的一个循环，首先它会有一个index，这个 index 其实就是下标，直接使用index。另外还会有一个什么我们每一项循环的元素，我们要为它定义的一个名称，这个名称叫做什么？我们直接可以取名一下，来写一个 item 的名称，叫做s、p、e、c、i、 d 规格的ID，这个规格的 ID 我们在 for 循环体里面去使用的时候，就直接可以把s、p、c、i、 d 给拿出来，OK，好。


随后在我们做拼接的时候，在这里面我们之前写 s 的时候，其实是有一个左括号和一个右括号，这个括号其实 for each，它也可以为我们去提供这样的一种形式。它主要是让我们去做拼接的。所以在这里面我们又可以这样子选它。会有一个可以看到它有一个open， close 和一个separate。应该说 open 和 close 其实就是一个闭合。我们先写一个open，在 open 的里面我们写上一个左括号，我们再来写一个close， close 写上一个右括号，这样子它的一个区间就出来了，它整个的一个闭合。闭合里面还有一项一项的元素，它里面每一项的元素都是使用的逗号去进行间隔的。所以我们在这里我们又可以去加上一个separate。使用一个逗号。一定要注意括号和逗号一定要使用的是英文状态下的一符号，使用中文肯定会报错的。这一点要注意好。这些标签。这些属性写好了之后，我们来一个结尾符好，结尾服务写好以后。在这里面我们只要把相关的这些每一个元素，也就是 SPCID 做一个拼接就可以了。在这里面要做拼接，怎么拼？没关系，只要在这里加上一个井号，来一个大括号，再把s，p，c，i、 d 给拿进来就可以了。OK，我就直接删掉了。这样子它其实最终就会拼接成一个括号，里面都是一些相关的ID。拼接的操作我们就丢给了 for 阈值来做了。


OK，现在其实我们这样的一段代码，它的一个 map 自定义的SQL，我们就已经是写好了。好，随后我们要去完善一下它所对应的映射，也就是命令空间。在这里面 items map custom 在这里来写一下。我们拷贝一份，把名字改掉。VO，很明显我们也要改掉。这是 shop cut VO。好在这里我们传入。刚刚也说了我们应该常用一个list，所以我们在这里直接写一个 list 就可以了。取个名字 s p c i d s list。在这里会有一个注解。这就是我们在 my Betis circle 里面刚刚所写的 pumps list。把直接拷贝一下贴到这里。这样子两个映射就进行了一个关联了。


OK，写好 map 层以后，我们就要去写一下咱们的 service 了，找到我们的service，找一下在这里 service 层，展开的快捷键是在小键盘数字里面的一个星号，直接点星号，会把所有的目录层级一步一步的向下去进行展开的。在这里先打开它的接口 item service，再找到 item service i m p r，这是它的实现。先把它的方法去写一下，写上一个public，返回的是一个 v o，直接把拷贝 list shortcut v o 好贴进来。名字我们也和 map 保持一致。



好，我们要传入了，以及传入进来一些内容。这个内容就是从前端传过来的规格 ID 的一个拼接的字符串。好，我们为他加上一个注释，根据规格 i d s 这是拼接的。查询最新的购物车中商品数据情况。这是用于刷新渲染购物车中的商品数据。好，OK，关掉。我们到实现里面把这个方法去导一下。好导入进来以后，第一步不要忘记先把这个事物先写上。事务使用的是suppose，因为它是一个查询。在这里面首先的一个我们应该要把i、d， s 去进行一个拆分，写一下拆分出来，它其实是一个数组。使用i、d，s，由于它是一个字符串，所以它有一个split。这样的方法，按照逗号去进行分割。


分割好了以后，在这里我们就可以来做一个list，写上一个list，这里面是一个 string 类型，取一个名字，我们是需要把它给 new 出来的 new 一个 a list，OK。其实在 a list 里面，我们可以根据 string 去循环了，以后一步一步把每一个元素添加到 list 里面。但其实我们还会有一个方法，在 collection 里面， collection 看一下，它是一个有跳，所以它其实是一个工具类。utils。在 hatch 里面有一个 add all，这个 add all 是什么意思？其实它就是把一个原数据添加到目标的一个 list 里面去，它是一个这样的作用。


在这里会有一个c，c，其实就是一个 collection 集合。把这个list。现在。这个 list 其实是一个空的list，写过来它的元数据，也就是数组，直接把i，d， s 写过来就可以了，这样子它就可以把 i d s 里面所有的每一项的元素都全部的添加到 list 里面去了。


OK，好。既然有了一个 list 以后，随后我们在这里就可以去发起一个 map 的调用了。在这里应该有了有一个 items map custom 点 query by 这个规格的ID，只要把 list 传入进去就可以了。return，我们在这里直接 return 就可以了，因为它们的类型是一样的。


好，我们的 service 就已经是 OK 了。 service 写好之后，我们就应该要去写一下 Ctrl 了， Ctrl 了。我们在我们也是使用 items control 了。在这里面去写一个内容，我们一样拷贝一下之前的一段内容，贴过来再去做修改。首先我们先把 swag two 写好，这是根据商品规格 ID s 查找最新的商品数据。其实我们所要的最关心的就是商品的一个最新的价格，因为它可能是浮动的。好，拷贝一下。我们在上方加一个注释。它的目的写一下，用于用户长时间未登录网址，刷新购物车中的数据。主要是商品价格。其实它也是类似于京东的，京东其实也是这样子做的，类似京东淘宝。这个操作是有必要去做的。


好，这里的路由地址我们刚刚其实已经看了，是一个refresh，写一下。对于我们的参数来讲，总共只有一项，它是一个 string 类型的，我们拷贝一下。这是它的一个参数的名称，要和我们后端对应，拷贝一下它的名称，写掉它是拼接的规格。 i d s，它是一个必填项。它应该有一个example。看一下。这是一个example，就是一个示例。示例我们可以写一下，写了之后也是可以提供给对接的前端人员去看的。比方我们在这里就直接写一个1001，逗号1003，逗号 1005 这样子的形式example。在前端看到之后，他就知道该以一个怎样的形式传递给我们的后端了。


好，OK。随后我们就要去调用service。这一段内容不需要删掉，我们应该也要去做一个判断，判断它是不是为空。 string utils 点 is blank，如果为空，直接 return 一个m，可 result 点 error message 写上一个内容，说我们这样子直接返回一个OK，因为你传入过来的一个 IDS 为空，所以我就默认的提供给你一个最新的数据，就是为空。因为你没有传递给我正确的内容，所以你在购物车里面显示的内容直接显示为空就可以了。 OK 这样子也是可以的。好在这里我们就要发起一个items，点 item service，点查询我们的商品数据， by 规格的ID，把丢进去，随后再把它的类型取一下，拉一个值赋值为list。最终拿到的数据我们直接放到 OK 就行了。这样子其实我们在前端调用的时候，就可以拿到相应的一个最新的list，叫做 new item list。


来看一下我们拿到相应数据以后的一个业务，首先一个是需要删除现有购物车里面的cookie，你要去删掉，因为我们要去做一个更新的。随后我们就要去干嘛，要去拿到最新的商品。数据以后要重组，重组是为了要把我们的数量，也就是 by counts 进行一个组合，做一个拼接，所以每一项都单独拿出来。之后重新的又去 new 了一个 shop card item，主要是把 by COMS 给放进去，其他所有的内容都是从我们最新的 item 里面拿到的，所以这就是用于去拼接最新的一个购物车数据。


拼接完毕以后，再一个一个的添加到里面，通过 at item to shop cut 一个添加进去，最终我们就可以去把所有的数据再取出来，再赋值给我们的页面，我们通过VM，也就是 feel 去做的一个设置。 list 在我们页面里面拿到了以后，它是可以去做一个循环的渲染。我们搜一下，应该是在这个位置。在这里可以看到有一个 shop cut list， v four，用于去做一个循环，每一项都是一个 cut item。来看一下每一项的内容。主要是在这个部位，它涉及到了商品的图片，还有是商品的规格的一个名称。当然还有一个跳转，这个跳转主要是把一个商品的 ID 给放了过来，因为用户可能会再一次的通过购物车里面的商品数据。


点击以后再去看一下商品，它的具体的内容是什么，有没有发生一些相应的变化。随后在下方还有是一些价格，可以看到价格其实是除以100，因为我们之前也说了，所有的价格在我们数据库里面都是以分为单位去进行存储的，在前端你是需要去控制的，所以一定要这样子去做。OK。随后在这个地方这两个一个是普通价格，一个是优惠价格。另外还有我们重组后的一个 by comes，也就是一个数量。OK。好。现在我们可以来到咱们的前端去进行一个测试，但是测试之前不要忘记我们的后端是需要去进行一个 install 的，因为我们刚刚改了POJO，也改了map，还有是 service 好。 install 成功，重启服务器。好。现在是启动成功了。


启动成功以后，我们打开前端的页面，在这里当前这个页面其实我们就可以直接去做一个刷新了。我们先把控制台 F12 先打开，我们可以看一下，因为目前刚刚我们还没有后端的时候，它是会报一个 404 的，因为我们的一个 refresh 路由还没有，现在有。来看一下。先把控制台清空刷新以后我们在控制台里面的一些内容是没有 404 错误了。


随后来看一下，现在在我们的购物车里面可以看到，现在总共是有两个商品，这个时候我们在这里我们侧边栏上的 2 是一模一样的。随后我们再来随便的挑一个商品，我们来挑一个马卡龙，我们把一个芒果味的加入到购物车，随后我们只需要在购物车再刷新一下，可以看到新的一个商品就添加到了我们购物车里面来了，现在总共就是三项。OK。以上这一节就是我们所讲的在购物车里面渲染购物车的一个相关的业务以及代码，实现OK。

