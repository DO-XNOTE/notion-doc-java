---
title: 2-3 搜索 - 商品详情功能分析
---

# 2-3 搜索 - 商品详情功能分析

[image](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/1962d9ec-7b47-4dcd-8823-64cabe04f08c/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466X3ZNAAO5%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T224641Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIQC7auZVnyvZZ32ABcxcC448TzsYfEbtqOvjv9CmbaJN%2FgIfX5s%2Fat6z%2B5Yj9AvpMMNwqi7mTzCeUwleEQs%2FqEUNbyqIBAjG%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMMIrDWTROXnJ3LuIhKtwDZtOCRvcleMpNjbBDC%2FcUXLzu%2BTukq8FfVRIEIm9l6oBGUlEEpwJDmqOtIMUNDmzBXYnV06Y031Xw8bXW5ld44PS%2BozcGm366vB8lbfhY18VsfqBu%2BuFN3SqqthlK95tUV9zaMMgSVKTavwHpb8YANlyBjOmJZ2H7DfWTHzFo7OsHXj%2BmgkhpAfarNaas%2FhfButuUBzQdjSAHH5dkhZL5V7hELBeehJqfRsX7EqQgmFjNzXXyF6VE43ql4s59zqKRwf139BiXQFRp2ITVFtkPRfzKtCEUAbgvehpq8tsBIorHtepD%2F8NKrhiLMVQ%2FAM%2F%2FDi1gbmNuS5RPiKcc5RqGiiXbkYZee8z59eA9ZbITSd42XZGH%2FqRct8y%2FuIyAGm3tT9C6aurdM3DFg%2B%2BuiGAWVp0wprIsrYVLsWYRpDFr550ln6e5lA95LFphN%2BPr3pVnA7Ry7mFQ582EqEPe%2BJbu8WnHCN7HU3lUOP6iB9dB9CnO3zCqUcqc%2Fh5gjxChjG9BMFAqJ2kFUwsZnOcuZhxWC2efT%2BubB8b5eolYu3OY7uqpK25w7sCm3Funi4alEMWfx5pKkh87yJ3FT%2BdnnckSFCVbgY7xLq4KLnqX5vhbFPXhCNlbm74EGujg0Qswmbf%2F0gY6pgGiFQdeaD0DTBdNJdjaPq%2FXh%2Fefym6dkVacMcBCVb8G9IdvzL%2B5F7FOL%2BPaflPEZ00auFWskoJ7Y3%2F93i0s8j7M4lOUzVMC9YY6bhitf638heDBxURS0OCThDtaziruj0X%2BVHXk9VxCiUvR10Sm0l9xMXciMW4nR51%2BqJZOdvbXqEL6qY%2B3%2FG%2BSallp3b7cvi0Oj8EahaI4v20xsoBZJFjxGTL1tPSE&X-Amz-Signature=5475b58842323cbfb84dcef32f5083704fc46c0111ef809c0884bed9c0ed16d1&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

到这里我们在首页上所涉及到的相关的功能，其实我们都已经是开发完毕了，包括了分类，还有是轮播图，还有下方的一个根据我们不同的一级分类，查询出它最新的几个商品，下方可以根据懒加载去进行相应的展示。接下来我们所要去做的就涉及到商品了。涉及到商品我们可以先来看一下，比方在这里面我们可以随便的去点击某一张图片，这个时候页面会发生一个跳转，其实就是根据上一个页面传过来的一个ID，这个 ID 就是商品的组件，在这个位置它会有一个 item ID，叫做 cake 1001。这个就是在数据库里面商品所对应的组件。我们拿到了这个组件以后会传递到后端，传递到后端了以后，我们就可以去做一个相应的查询了。好在我们后端要有哪些的操作。


我们先来看一下当前的页面，我们可以切分为多块。首先看这一块其实是一个图片，商品相关的图片，其实我们在这里都有一个展示，其实我们在之前的课时里面已经是有提到了，其实就是这个图片有一个 items image，我们前面有已经是说过了，所以在我们就过一下不去试。是单独的一张表，在我们页面里面会使用到的。所以我们会根据当前的商品 ID 把相应的图片都拿出来。当然第一张图片就是我们的一个主图。


好。随后这是第一块内容，第二块内容就是我们的商品基本信息，商品基本信息其实也就是对应着我们的商品表，在商品表里面，在页面里面目前所涉及到要去显示的主要是一个累计销售，以及是一个商品内容，我们可以来看一下。累计销售是在这个部位，在这里会有一个累计销售，目前是有1003。下面会有很多种的口味，其实是不管你是什么口味，卖出去多少件，我统一的都会在当前的整个商品里面，作为它的一个累计的销售量。此外，下方它会有一个宝贝详情，也就是商品详情。


在这里会有一个细节，在这里面其实涉及到了图片以及是文字，其实就是一个图文，一段 HTML 的富文本代码。在这里我们只需要从后端从数据库里面拿出来，在这边进行一个展示就可以了，所以这一块就是商品的细节。OK，好。随后我们来看一下，在这个部位，其实每一个商品它可能有多种不同的规格。在我们目前的平台里面来讲，其实设置的会相对来说比较简单，因为商品其实就是吃的东西，它的口味会有多种，比方有原味的、草莓味的和香草味的是当前商品。如果我再换一个商品，比方我随便挑一个肉松，在肉松里面其实也会有，它会有鸡肉的、猪肉的和猪肉的。不同的口味，不同的规格，它所对应的一个价格等等信息都是不一样的。


这个其实就是一个商品的规格信息，在我们的数据库里面，我们称之为是规格表，可以来看一下。在这里有一个 items s，p，e， c 就是代表规格的意思。我来看一下，首先它会有自己这张表的组件ID，会有一个商品ID，这是它的外键。随后就会有它的一个具体的规格名称了， name 规格名称，其实鸡肉，牛肉，猪肉这些就是它的一个规格的名称。随后下一个是一个库存，库存是每因为我们用户要去购买，可能会选择不同的口味，有些口味比较热销，它的库存卖的就比较快了，相应的库存肯定也是不一样。还有是折扣力度，优惠价以及是原价。我们可以到咱们页面里面来看。比方我选择不同的口味，它的一个优惠是不一样的，这是它的优惠力度。比方我们默认选择鸡肉，它是 9 折，牛肉就是八折，猪肉它就没有优惠，当没有优惠的时候，它的促销价和原价都是 108 元，全部都是一样的。如果是鸡肉牛肉，相应它有折扣，是需要去进行一个计算的。计算完毕之后，相应的在这里是需要去进行一个展示的，它的一个原价，促销价以及是优惠力度了。


OK，这些内容就是我们当前商品的一个规格信息。好，随后我们再往下面看。下方它还会有一个产品的参数来看一下。产品参数。比方它会有产地、生产厂址、规格、重量、品牌名称、包装方式、储存方式，还有是厂名、保质期和实用的方式。这些内容其实在我们的数据库里面也会对应的，有相应的一张表叫做产品参数表，我们来看一下。在这里会有一个 items palm，其实就是parameter。商品参数表，在这里面包含了很多的信息。首先一个是商品的参数ID，这是它的当前这张表组件。还有是一个 item ID，这是它所对应的商品的外键下方像产地、保质期等等。


这些内容其实都是一个一个的属性，这些属性都是分别为我们的一个商品去提供的。现在其实我们的属性是比较少的，如果属性有很多，可以自己去添加。当然每一种商品它的属性可能会有参差不同，如果不需要去显示，直接针对某一个列或者某一个属性设置为空，不要去显示就可以了。 OK 好。

这些内容在我们数据库里面，现在其实也已经是生成了，分别对应到这里有items，还有是 image 图片，这是商品参数以及是商品规格。在我们的钢琴这张页面，如果一开始用户进来的时候，我们该如何去查询？其实我们可以考虑到有两种方式。第一种方式是我们用户在前端的浏览器只发起一次请求，一次请求发送到后端的时候，相应的查询操作我们都会在一个 Ctrl 里面去执行，也就是他会查询一个商品的基本信息，商品的图片列表，商品的规格列表以及是商品的参数。这些信息都统一的只在一次请求里面完成。这样做的目的是可以让用户避免过多的重复刷新页面，导致后端可能会有很多的请求，这样子其实就可以让用户在一次请求里面把相应的信息全部都查询出来，随后在页面进行一个渲染，这是一种方式。


另外还有一种方式把相应的信息分开去查询。比方在这里我们有商品列表，商品图片的列表，商品参数列表，商品规格列表以及是商品基本信息。有 4 种，有 4 类信息。这 4 类信息在用户请求到当前页面的时候，可以发送 4 次请求到后端，在后端有 4 次请求，就会有对应的 4 个 Ctrl 了去进行接收。这样子做的目的其实就是不要把鸡蛋放在同一个篮子里面。我们把请求分散开来，这样子可能在页面加载的时候就可以比单词请求会更加的快一些，局部会优先把相应的信息优先的给显示出来。用户的体验其实相对来说要比一次请求会更加的好一些。我在课程里面，我会采用一次请求的方式，主要是为了图方便，我们只需要写一个 Ctrl 了，对接 4 个 service 就可以了。如果你要分为 4 次请求，写上 4 个 Ctrl 了也是没有问题的。在这里我们就这样子跟大家说一下。

