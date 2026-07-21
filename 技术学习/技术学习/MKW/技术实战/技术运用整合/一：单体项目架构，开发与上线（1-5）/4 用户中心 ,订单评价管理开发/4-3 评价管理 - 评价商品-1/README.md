---
title: 4-3 评价管理 - 评价商品-1
---

# 4-3 评价管理 - 评价商品-1

[image](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/6d712c75-a957-4f14-928c-7e03d34dc306/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466Z4XA5U6F%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T224738Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIDvbhjmLJiSIfpJvomZruzjbCnSrFIfdrGvTwnZoTmNOAiEApp%2FyIHTYapmjZp%2FP9ip9Ll8PBU7%2FxczMxX3KDZmWQRoqiAQIxv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDM3a0j23XanH%2BXeyryrcA6kAGR0KvjkMekdokxOyPE4snxDkV2nRiCAH%2B8dua5OC8SRogtc%2FP8oQfFPkc21CQe0Kc2eO8QXmiwP6nf4bf6DZke%2FCpbU1J91L4fniIuRdD4SNAUOwSlVGc%2Bq%2F96u%2BBO2w9laIV0QZxM%2BsEknLu0fkJfMJDVQiliy%2Bw4XWisZzsQc%2Fa3dm6dJQgyEJ9Nh4pJV9z4pwqIGgQrDZzAOcvkyip9nst%2BMZ0wQCdSAFrTYtUdeqTj7reRgG457J0w1SjycdNYtB7otg1VQddCPHFJluWng8XAdDqbj8ZuUGfATSTVu5pYDvl%2Fzc1%2FS%2BGdeJmlNPK6mqDc54q32msqPhurUcFjvOcUN9xfeH2zoD9kfWbH%2Bv%2Fmb834l%2BAgP7CHddbM0ZuLohIQiax8QZgSvWMzDHI7kEPTz6JOvOfC2%2FnR46b1Cz326mA9PimMVCDMdNjEwNT8B%2BnEoupFZF4fh7Lh9xCTQLbruTUgNtRVkpWpealVP%2BZiNEFXDbcamI3o%2FcC2tHvCvEPXsuzIXVeTCgF6AJHwbl9sJhki3dsh%2BFQIDhS%2BFW7jrqSoj1aO7iDR8Hqmd0U8UhzFwlLqVDpm%2FZryL3T3jqYbADA8eJXLkk8wU5apyntAYmeWh%2F6fXzMNe4%2F9IGOqUB0FW5y%2BrOfRb1a4mmDYkgvyZWPovq9btviBJvWXNaYjtEQzvgS8OFOLjbGfjEzW%2FeEc4by4acj2ZEXrvyxYntIf5DGC6%2Fd49veNZi6905Vp%2FLY%2FTgH%2BIE2baIbBZ2DAY5avfKto6d%2BHIwVcp9MokoIpBY1q3RFaQyLhuljcyquCdfLafrBkDmsexsqichS8y8W9YELlFSU2uiSYdpv82EUsTj5dXk&X-Amz-Signature=02e39c0ef0d489de3ba19c45d45470f2936680adc34e0a0b5bb94554b415ce70&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

上一节我们是把评论页它的商品有几个，我们是进行了一个渲染，只不过这一条订单只有一个商品，我们换一个商品，订单里面就包含了两个商品。既然是两个商品，它肯定是在一个 list 里面，因为我们是通过一个 list 去做的循环和渲染。在页面的右侧是我们用户要去发表评论的内容，以及是评论的等级来看一下，这些都是可以去点的。另外内容也是可以去做一定的。


输入了以后，其实评论的内容也相应的是一个list，所以在前端我们是可以把评论的一个 list 和我们查询出来的 list 是可以放在一起的。放在一起等以后，在用户点击发表评论的时候，是可以把评论的等级以及是评论的内容一起以一个 list 的形式发到后端，后端是可以去接收到的。接收到这个 list 以后，我们再去做一个解析，再去做一个保存。我们可以先来看一下前端的内容。前端这是我们之前所讲的一个渲染我们的页面的过程，在这里会有一个 order item list 在页面上，也就是根据这个 list 去做的一个渲染。是在这个位置我们往下面找到有一个 text error，这个是输入评论的内容。在有一个叫做 free model 这样的属性，这个是只有这个框架里面的，只要是使用 form 表单元素，我们就可以使用这个属性来实现数据的双向绑定。我们绑定了一个叫做 content 内容这个字段，这个字段我们是放在了 order item 里面， order item 又是属于我们当前这个 list 的。我们为这个 list 是定义了一个相当于是每一项的元素，这个元素你只要在它里面，附上了一个相应的属性值，在我们数组里面，每一项它都会多了一个很简单的字段。这是因为双向的数据绑定。除了内容以外，还会有一个评价的等级，在下方可以看一下。


在这里会有一个 make comments，这个是点击三朵花，好评，中评，差评，你点击了以后会去触发的一个事件，往下面看一下。在这个位置会有一个 make comment，其中在这个部位，用户点击了好中差，不管是哪一项，它都可以获得当前的等级，获得不同的等级了以后，它会附给一个叫做 comment level，这个就是评论的等级。在这里它会做一个循环。可以看到如果用户点击的这一项 order item ID 是等于我们循环的某一项。在我们的数组里面，你直接可以为他去附上一个新的属性字段，把这个 level 的评价等级附给他。这样子在我们 list 里面也会包含一个相应的新的资料。


属性的这一块内容。 for 循环就是用于去做这样的一个目的的。OK，好，随后再下面一部分。下面一部分是和我们的c、s， s 相关的，主要的目的是用于去实现在页面上一个颜色就是三朵小花。颜色的更改是需要有一定的前端的基础，有兴趣的同学可以把这一块内容去读一下。我们就在这里不去过多的去讲解前端c、 s s 的一个样式了。OK。好。当我们的一个整个 list OK 了以后，用户点击发表评论，我们来看一下。发表评论是在上方有一个叫做 save comments。首先我们是需要去获得一个 list 的，这个 list 里面就包含了用户评论的内容，这个内容是包含了评价内容，以及是评价等级的，这两个都会有。随后在这里面可以看一下。在发表评论之前，你必须要去判断一下。首先你必须要判断用户是点击了哪一朵小花，你的好中差是哪一个，是需要去进行点击的，要做判断。其次，对于用户，你每一个商品你都需要去评价一下，OK，所以我们这两项都是必填的。符合这个条件了以后，我们就可以去和后端进行一个联调了。


这是后端的一个路由，是 save list 要传过去的数据。首先一个是用户的 ID 以及是订单的ID，这两个是必须要有的，因为我们的评论本身和订单和用户都是相关的。除了这两个参数以外，还有一个就是我们的一个list，你是需要把这个 list 给传过去，因为它是一个评论的list，包含了相应的内容。传过去了以后，在后端我们就可以去做一些相应的处理。处理完毕以后，在我们前端它会获得一个 200 的状态，获得 200 以后，我们的在前端就可以提示一下评论成功。


在我们的一个页面进行一个跳转，跳转到order，点HTML，也就是订单管理页。OK，好，现在我们就可以先到后端，我们先写一下 Ctrl 了。我们先接受一下list，把这个 list 接受以后，我们可以打印输出一下。我们到自己的 Ctrl 了。在这边我们可以去写一下拷贝一份。把拷贝一个新的方法在这里面去做修改。首先我们先把这个方法名改掉。方法名使用 save list 改掉。 swag to 接口方法我们修改成保存。评论列表。调用的时候使用的是post。


随后传入进来的两个参数，一个是用户ID，一个是订单ID，这两个都必须要传的好。除了这两个以外，随后在下面我们就来再新增一个新的参数，这个参数就应该是一个list。这个 list 其实它本身也是一个 JSON array，所以我们在这里是需要使用 request body 来写一下，写一个list，定句为 comment list，这样子就 OK 了。


对于我们传过来的一个类型，由于它是一个Bo，是一个业务级对象，所以我们在这边是需要去给它加上一个类型的。有了类型更方便我们的一个使用和解析。 Bo 在这里我预先也已经是创建了，在这里有一个 order items comments b o，这个是我先创建的。


b o 是放在了 center 里面，它是一个业务层的对象，因为 b 就是business，所以我们是放到了center，因为 BU 我们分为了一个原先的一层和 center 用户中心的一层。 BU 我们并没有分Fu，大家也可以去分一下。在这里我就不去分了。


好，双击来看一下。在这里面其中我们就包含了一个叫做comment， level 以及是content，这个就是和我们前端的 list 所对应的，拿到了以后这里面是会有相应的值的。OK，在这个下方我们可以去生成一下。我们可以这样子生成一个 to string，我们太多了，我们这样子我们只把我们只生成一下comment， level 以及是 comment 这两项。把这两个我们做一个输出，其他我们无所谓。好，在这里就可以去写一下order，item，comment，Bo，这样子我们就可以获得到这样的一个list，所以在这里我们来做一个打印，直接把在这里进行一个输出。好，这个是用于去测试我们所接收到的一个list。除了这个以外，在下方我们是需要有一定的判断的。首先这一步骤也是需要去做的，是要判断用户和订单是否关联，如果不关联，我不会让你去做保存的。这一步是需要去做的。


最后，对于我们的 comments list，我们在这里也要去判断一下，写一下判断评论内容 list 不能为空，你传过来是一个空的list，我就没有必要再去做保存了。在这里写一下判断，判断它，如果它等于null，如果为空，又或者这个。

The comment list in is empty.


视为空，又或者点它有一个size，判断是不是等于0。这三个里面满足其一就可以了。一般来说写前面这里两个判断就行，后面一个其实也可以。在这里面符合这个条件说明它 list 为空。在这里我们就可以直接 return 了。 return m Jason result 点 error message 返回。说一下评论内容不能为空。好，OK。在这里我们不需要service，我们现在还没有去写。现在我们就可以来。先来测试一下。先测试一下我们获得的 list o 不OK，我们能不能够通过验证，对吧？好，在这里我们可以我们来 install 一下。好， install 成功之后再来一个重启。好，OK。到我们的前端页面，我们先刷新一下。以后在这里我们先第一项点一个好评，第二个我们点一个中评来做一个留言。第一个写上一个马卡龙很好吃，下一个。下是一个饼干，写上一个一般般。随后点击发表评论。我们先把后端的日志先清空一下。先清空，我们再来点击发表评论，点一下。好，在这里提示是评论成功。评论成功就说明我们的一个判断是通过了。回到我们的控制台，现在我们可以来看一下。我们把日志跳到在这里。第一行就是我们所打印的内容。先看到这里有一个 comment level，它的一个 level 等级是1。最后一个是 comment 内容，这是它的一个评论内容。好，没问题。再看我们数组，我们 list 第二项在这里 comments level 评价的等级12，说明它是一个中评，内容是一般般。OK，现在其实我们就可以在咱们的前端，我们就已经是可以实现了评价，评价的内容我们是可以在后端拿到的，OK。

