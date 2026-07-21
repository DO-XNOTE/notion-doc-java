---
title: 2-5 搜索 - 联调详情页与排查bug
---

# 2-5 搜索 - 联调详情页与排查bug

[image](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/a761cbcf-a622-4c3c-9483-dbeefe9d05b2/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XPJIQVUQ%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T224643Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCZBsX%2BBkRSKn%2FcAlu5HLT3nqrzv8HJsDMktvI2EGGicwIhAN33bvGWSx%2Fkxszl0WoSnQi60ed0lBzsK6BSky%2BWpBrYKogECMb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgwDPdDsUvGNXsRRQv0q3APO4sbMQl4kAMfFrrWVC8xM%2BmAPCtvkryd43dIXD42UJuvShTxqOXo1flt2TQFg3C1gj5tNoRK1Xc1KDL%2BC8mx%2FeRjcZyZs6gN%2B%2FqxYk3DIkiHO9s2RH4Mfcm4V5XfCIdtOJbRWlZUbiwhO49X7vmvFf7p3%2FutbdVpUnN3Dzba%2FcjPF15lWkWFduhnxuS2cg4Wu4u1tvJ6okr8MZ9Pd6FT%2BY1Q8pahI4Ut5jEM7z9eA1fuZPQHBlXeMKSqOKH58T1pUOUu0eng9sUDAwP3whFKycLIZpdXtt0w19blS1%2FkcE9D8fehj1aR9o1N5LXbvyVwi%2FEw%2B%2FaaO9Rn%2FbWhz6JTzkFcpLPKewO4mdAV4FmgTNHOwza67MJufaLa8Be2wS2xAU98ANbB4xn8AusATjDxi9%2BTJExbYA0tLygQcMnsMLOaeiOOPAgAF4fVLroASjJQ6hCZrZ0m%2B%2Bz08C1FK2e1o6t9fCR6xbMgHnC4RGoUeyaDAOYTwaK3N9pUYe%2BReIXV5heSPVUw2N2anuGesU8SO7mbyhuU8P5zxHufOxOB7b6chw9ZnPqwSt20wHYP0qiiIP58V49EtSyTxPvr3QVoyWIsyD9A20zVyfjeAHofla7JDY8vbNmZDqwa2hTDKt%2F%2FSBjqkATAce7EQileIT%2BdrBahnzg6DT%2BANh0l6Cv8pclWi4wWzY1p%2F1JHEeCfLkrEmHyk3Fh5GUu4c0CnTyqji0ldDUV5hxvcvg%2BVVCaLxrhHb6xUzNsDeZPsqdKxlqbzivJkqkOKGITZSFpsWx1J1ZyRE1XGCE74hsq7RUfi%2BLV7VvP5os3oMHFfNWWlHGuX%2FWKHDiJDTi5tkst3HGQ3xJLszhvaQLzhr&X-Amz-Signature=2fe460fdeb2417e562016a47ad3bb96edae90bf53f32da8b2d47b8db0a5e8dac&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

上一节我们是把 service 里面 4 个查询方法我们都已经是写好了，接下来我们所需要去做的就应该要去编写一个 Ctrl 了。 Ctrl 又是和我们前端要对应起来，所以我们可以先看一下咱们的前端。打开页面，里面有一个item，点h、t、m、l，这个就是商品的详情。找到最下部分的一个JS，这就是 few 相关的代码。我们可以先找到created，这是生命周期函数页面，一开始加载的时候，加载完毕它会进来。它会找到上一个页面传进来的 item ID，探空一下，如果这是为空的，就会跳转到一个报错的页面。报错页面是引用的咱们慕课网的一个页面。好拿到了 item ID 之后就可以去查询相应的信息，去做一个渲染。来看一下。


这里有一个 render item inform，搜一下OK，在这里有一个渲染商品信息。在这个里面可以看到发起了一个 get 请求 items 杠info，这是我们的路由，随后后方是一个 item ID 做一个拼接，它其实是一个路径参数。随后我们就可以到达后端去执行我们后端的链路了。拿到了相应的一个数据以后，要进行一个判断，是 200 就代表OK。就可以逐渐的去从我们的 data 里面去获得相应的信息的。有 item info，另外还有是一个 image 图片，还有是商品规格以及是商品参数等等。这些内容都可以通过 view 数据的双向绑定，在页面里面做到一个渲染。好，我们来看一下咱们的后端。在后端里面我们要去编写一下。现在我们 item Ctrl 还没有，所以我们可以来创建一下。我们找一个index，把 next 拷贝一份。items， Ctrl 好，点击OK。好，在这里面我们就可以去做一些相应的代码编辑了。


首先一个先把 swag to，也就是 API 先改掉，这里改成商品接口，这是商品展示，商品信息展示的相关接口。在这里它的路由改为 items okay service，很显然我们是需要使用 item service。好，后面打掉这个category，我们不需要。


好，我们把接口就去，需要去写一下。把我们没用的先删掉，下面的也都删掉，保留一个。在这里面去做一个修改。首先我们定义的一个接口的名称。 step two 写一下，这是查询商品详情， notes 直接贴过来。 h t d p method 使用 get 请求。在这里就需要和前端对应，前端是一个info，随后会传过来一个 item ID，它是一个路径参数，在这里我们要写好，并且它是一个 string 类型的。对于路径参数，我们是需要去做一个描述的。在这里 spark to 演示，写一下，它是一个商品ID。好，在这边我们就需要去做一个判断。如果从前端传过来是一个 item ID，是空的值，我们在这边是需要去判断的。因为如果你不去判断它，还是会到数据库里面去搜一下，这样子很显然不是特别好，所以在这里控制一下 string 与驾驶点 is blank，把 item IP 给放进来，判断是不是为空。如果是为空，我们直接在这边就返回一个空数据也可以。


好，我们就可以去发起相应的 service 请求了。通过 item service 点，第一个是查询我们的商品详情，把 item ID 给贴过来，返回的类型是items，在这里也是需要去写好的，直接定义为 item 包，要导进来。好。下一个应该是查询他的商品图片列表，拷贝一下。好。OK，我们再拷贝两份。一个是查询它的规格，另外一个是查询它的商品参数。它们相应的一个list，我们在前方都要去定义，这是 item image list。好，下面是一个 s p e，c，也就是规格list。再来一个参数。这个查询不是一个list，它是一个对象。导入写一下，好。OK。现在我们 4 个内容，有两个是对象，还有两个是list。这些内容我们是需要传递到前端。传递到前端，由于在这里是有 4 项内容在，我们使用 m just result，它只能够返回一个对象或者是一个list。


怎么办？很明显，这一次我们又需要和 FIO 打交道了。因为 FIO 是显示层用于去做展示的，所以我们是需要去构建一个 items info FIO 了。好，再一次的和 feel 来打交道。然后我们打开POJO，到这里面找到一个VO，我们用这个 simple item VO 拷贝一份，取一个名字叫做 ITEM info c o。好。在 in for FO 里面我们所涉及到的其实就是在 controller 里面，我们通过 service 所查询到的这几项内容。我们只要把这些拷贝贴到这里，先清空一下，注释改掉。这是商品详情。 VO 来定义一下 private 使用的是item，然后后面的删掉这些，后面的也全部都删掉。这种方式我们也是偷懒，我们不用再去手敲了。好 4 个属性我们就已经是构建好了。以后我们是需要去生成 get 和 set 好是吧。我们就只要把 FU 在 Ctrl 里面进行一个设置，直接把它给 new 出来。这是一个item， in for VO 等于 new 一下，然后把 feel 给丢出去。


在v， o 里面，我们分别去做一些设置一个设 image 好，下一个是规格list，再下一个是一个参数，它是一个对象。现在我们接口就已经是写好了info，这个方法名要统一叫做info。好，我们就需要去重新的再一次 install 一下我们的项目了。 install 成功，启动服务器。


好，启动成功。这个时候我们就可以来做一个测试了。我们先打开。我们可以先测试一下 swag two。这是 swag two 里面的有一个商品信息，在这里，我们是需要填入一个商品ID。如果我们随便填，点击发送，很显然是没有任何内容的。如果我们不填，直接点发送，它会提示 item ID 不能为空。这个是由 swag to 为我们所控制的，在这边我们可以去拿一个。我们可以使用 cake 1001 拷贝一下。


到 swag two 里面，可以来做一个测试，点击发送可以看到相应的数据。我们全部都可以拿到了，说明没有问题。在这里我们就可以通过这种方式去做测试了。大家也可以通过Postman，也就是 Postman 再可以去联调一下，做一个测试也是没有问题的。在这里我就简单一些了。随后打开我们的首页，刷新一下。我们现在就要来测试一下我们的商品详情页能不能正常的打开。我们来看一下。



我们可以找到一个秋葵，点击一下，随后他发现了一个错误，跳转到了404，也发生了一些异常。发生异常，我们先要看一下我们的后端，先看一下有没有一些错误，很明显没有任何错误。没有错误，我们就要来看一下前端了，这有可能是因为前端所引起的一个问题。好，我们打开上一个页面，我们可以把鼠标移过来以后，其实大家可以发现在状态栏出现了一个问题，它是一个undefined。由于它页面进行了一个跳转，其实页面是发生了一个重定向，会重定向另外一个页面。所以我们的商品 ID 参数我们是看不到具体的内容是多少，所以我们在当前的页面是可以看得到。或者我们可以右键来检查一下。


我们可以来看一下，在这边会有一个跳转的链接，你会发现 item ID 是一个undefined，没有取到。这个值是从后端拿到的。之前我们在使用 SQL 进行测试，其实是有值的，很明显现在是有问题，我们可以来看一下。我们来看一下我们的数据在前端拿到的时候是怎样的。其实这也是一些在开发过程中会遇到的一些问题，遇到问题不要怕，我们自己去解决就可以了。我们可以打开首页，在首页里面找到 six new items，在这里有一个 console 点log，这个是用于去在控制台上打印日志信息的。我们把 list 全部都打印出来看一下。好到我们的首页刷新一下。


点击CSO，就是在前端的一个控制台。在这里来看一下，这里面应该有一个 simple item list，它主要是看一下我们的 ID 有没有，在这里你会发现 ID 有值。再下一个，其实 ID 也有值，但是你会发现这个 item 是不是拼错了， m 和 e 写错了，所以写错了就会导致前端它取不到，前端取不到这个值，它就会变成 n defined。所以我们是需要去把属性的值去改掉。属性的值我们是在后端定义的，所以我们要回到后端去把相应的内容去改掉。我们来看一下，它的定义。我们是会有一个 FIO 的，这个 FIO 我们来找一下。这个是在 POJO 工程找到有一个 simple item， v o，双击打开看一下，你会发现在这里有一个 item ID 是打错了，所以你是需要去把它改掉，改成 item EM，不要打错。随后这个是需要去重新的生成 get 和set。好。改了以后还没完。因为它是对应到我们的circle，我们的 circle 是写到自定义 map 里面去的，所以去找一下。在这里 category map a custom 双击打开来看一下。


这里面我们之前是定义了有一个，来搜一下。在这里 simple item ve o。很明显在这里写错了。这样子写好以后，我们的 SQL 是在这里，所以源头就处在这里。一旦写错，我们一步一步后面的我们的属性名称都写错了。当然和前端对接的时候也会发生的错误，所以会导致一个 n defined，这就是我们平时开发过程中是需要去注意的，一旦粗心了就有可能会出现bug。好，重新的。 install 成功之后，我们再重启服务器。


好，重启成功。我们回到首页以后， console 点log，我们就可以去掉了。好，刷新一下，我们就可以再来看一下。这个时候我们可以右键检查，你会发现这个时候它的 item ID 就有值了。现在我们要去点击，其实就会有相应的内容了，我们可以找到。还是找秋葵。点击一下来看一下我们的搜索结果。点击看一下我们的查询。现在我们就不会再跳转到错误页面了。


相应的信息我们来看一下图片。没问题是有的，基本信息也有，累计销售也有，但是在这里其实应该会有一个规格，规格没有显示，我们再往下看。下面是一个产品我们的参数，参数你会发现它没有展示，所以也有问题。另外再来看一下我们的商品细节，也就是详情内容图文没问题，是可以展示的。唯一的两项就是参数和规格没有显示。我们在 swag two 里面，其实我们来看一下。在这里面其实我们能够找到相应的内容，一个是 items s p c list，另外一个是 items pump，这两个我们都有，但是为什么没有显示？很明显我们这个时候又要去做调试了。怎么调试？很显然我们可以通过前端去做调试，我们到前端里面，因为在前端里面它没有渲染，所以我们就需要去找到相应的内容了。打开当前 item 页面来看一下，找到渲染商品信息。商品的信息 item 是可以拿到了，没有问题。图片也可以拿到，没有问题。我们到这里来看一下规格，规格它是如何去取的。它是通过 item info，点 item s p c list 来注意一下这个属性。我们是怎么定义的。我们在文档里面，在 swag two 里面并没有这样子的，我们来看一下，搜一下搜不到。其实可以看得出来，我们在 d 的时候，它是多了一个s。所以这就是我们的一个问题。我们没有和前端去进行一个协调，一旦协调好了，你的参数都定义好是某一个名字的，这样子就可以去进行显示的。在我们后端，我们可以先打开我们的 d o c o，里面就是 s p c list。我们先把拷贝过来，很明显是有问题的。


再来看下一个。下一个是商品的参数信息，也是通过 item info 点 item pumps 拷贝一下。来看一下。在这里很明显不对，我们在后端定义的是 items come，所以把覆盖一下。这两处地方全部都覆盖一下，相应的，他们的 get 和 set 就需要重新的去生成了。


OK，好，重新的去生成一下。咱们再来 install 一下。好， install 成功重启服务器。在这里我们可以发现从此的时候在 controller 里面遇到问题了，因为他们的 get 和 set 发生了变化，所以我们重新的去写一下。这里应该是 set s p c list，在这里应该是 set item pumps。好，OK，再来重新启动。好，现在就已经是启动成功了。


我们回到咱们的页面，直接在这个页面进行一个刷新，你就可以发现规格显示了，参数也能够显示了。并且咱们的规格你会发现如果我们一个点击它，里面的数据是会发生变化的。巧克力，草莓，芒果他们的优惠促销价都会跟着发生变化。现在其实我们就已经是完成了商品详情页面的一个开发了。只不过我们在开发的过程中出现了两个BUG。一个 bug 是我们在之前做分类的时候出现的一个小bug，另外一个 bug 是我们的一个字段，属性有没有对应。所以我们在平时开发过程中遇到问题，遇到 BUG 不要怕，只要去细心地去排查就能够解决了。

