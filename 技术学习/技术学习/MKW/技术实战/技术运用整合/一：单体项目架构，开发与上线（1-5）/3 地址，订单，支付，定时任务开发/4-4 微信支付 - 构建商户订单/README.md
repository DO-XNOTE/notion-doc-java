---
title: 4-4 微信支付 - 构建商户订单
---

# 4-4 微信支付 - 构建商户订单

[image](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/f1bee10a-2a9b-4185-838b-04a6568d3182/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YFYWQYEZ%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T224709Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIDxroTLRdQ1%2B4CL0uoowmVbu9JG8MZd2dUneHeV81QCQAiEAo8QojZObKUCbBYCbUSXkZ%2BsdKMA4pb511y%2BWZahlExoqiAQIxv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDKqF%2BuRFRXJq2D0COircA8f9LZ4OGLszfU5LPX01DIJ0Vh8g78M9F0s9ysmQ2zI4uc2qLNPPNwIoG3LZOkk8orPlpcuzTfa7qx9Op2OHSSjBoHQikkxAC7Xmoga9clLMjQWwPqE%2Bj37al3xodlxE%2FZMNBMG18vMZFe8pkyBHDFyTV4B6XfzHQOO9tJVmxml1mlsaa2XSzBAmt6fBJJkw54lVaOgDWyjfQDqcL7PM%2FCuB2oQaeiYufMx4%2BfRW3crtJg6uDWABUfACPmP3UgTDbAyRb9fZPKThW0xG1IrXt3jgtH3%2B6nppHMzeudBL9kumbcTlGK1WwrbLd%2Bwazo7PJw6P%2FB42mZ3MGPWSF7eZ%2BMP9SLGLuU%2Bwc0xL3ARUZPmNN%2BmvtRInr7vBBWoGqe4E2oqjVF6T4xrVmjReREHpwEkxId1Hwueblcxeq8hTjpXRp04HaBCtoIkPxGwhk6zp7TTUwr%2FtVgivcsBBFV7vyklrecmi98ad0COS4SWITybI%2BcMquqOMFU0MqiDBvF%2Bo%2BfM0zskyNqsQR3hqlkymGD3QcsF8b7ZiGhlZ9jBPbZAgSsDwfs7y9qAZwHqdYXtDoi80Ouu2huCQ05Bq0kW3Thy7vwkUJeiV7Jo7wdBvrwplqtlunijguxH5ME52ML67%2F9IGOqUB9iI2PNfNZkJN1x9sXwiWzNnLF9l0gUTcK46hSofeMHVmXmYy4xGxv4ziIT3O29ZTI9PP8Kel5Vi%2BSnb%2BwzK0lfEVzd71%2FMstrEg6mMh9OTaFx9YwolfX2vQq19UZ4ZN%2FXuGwT49ayDzhmR5xrg5vVCLsGAPFkfUxWywZpgzVmCe8lxL%2F4rcEc5xqb6ray6S0%2B0xkLc%2BEAEqNjQzQjfaaZ%2FbqbHTm&X-Amz-Signature=758d82fe5e971585153fad2331f5ab99e98b30e8d2c74aff7da30bc92c5652d0&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

上一节课我们是写了一个通知的接口，这个接口主要就是用于提供给支付中心，让支付中心接收到微信支付成功的结果以后，随后再调用我们的一个这个接口，使得我们的订单的状态可以变更为已支付。OK。对于这样的一个接口，地址其实就是对应到我们在数据库里面，在支付中心的一个回调通知的自定义的return。对于这样的一个 u r，我们在这里可以先定一下，我们可以统一的写在 base Ctrl 里面写一下，写一个 string pay return URL 写好。这个是在 post man 里面，我们可以把这个地址直接给写一下，写到这个位置。随后我们加一个注释。


支付后，支付中心我们写一个简单的流程，微信支付成功通知到支付中心，再通知咱们的天天吃货平台，是这样的一个流程，所以这个就是提供给我们的一个回调通知的URL。写一下在这里，在这个部位，这就是回调通知的URL。好 OK 好 UL 写了以后，我们后续需要包装到一个商户订单里面，随后再让我们的支付中心去进行一个创建。现在我们来带着大家去看一下我们的支付中心。


支付中心目前是在另外的一个项目里面，给大家来看一下。其实我们的一个项目还有一个叫做payment，但由于这是部署在我们线上的，所以这一整个项目，这一整个工程的源码老师都会提供给大家，只不过我们就不在本地去进行相应的代码编写以及是部署了，直接去调用线上的一个环境就可以了。因为在本地去进行部署，大家是不能够去使用的，会使用到企业资质里面，涉及到相关的密钥等等的信息。


OK 来看一下。首先在 payment Ctrl 适用于去做支付的 Ctrl 里面会有一个方法，叫做 create material，是用于接收商户订单的信息，保存到自己的数据库。这里的自己的数据库，支付中心的数据库是在我们的这里所定义的有一个配数据库是对应到这里面的。OK，我们可以来看一下。在我们的参数里面会接收一个对象，这个对象就是一个 match order Bo。来看一下这里面包含了一些相应的数据，这些数据其实我们在讲数据库的时候都说过了。首先这两个是商户方的订单号以及是付款人的用户ID，另外是一个支付的总金额以及是支付方式微信或者是支付宝。还有一个就是return，这个是由大家去自定义的一个回调通知的地址，也就是我们刚刚所说的地址配 return UR OK。


好，再来看一下。拿到这样的一个对象以后，我们肯定是需要验证一下这个对象里面相应的属性，每个字段都是必须有值。首先要验证一下订单 ID 以及是 user ID。另外对于我们的金额肯定是要大于，首先不能为空，并且它要大于1。随后下面是一个支付方式，支付方式只能是 1 或者2，也就是微信或者是支付宝。另外一个对于我们的 return UL 就是回调的一个接口的地址是必须有值的。


好，当我们的验证都没有问题了以后，随后我们就可以去调用 service 创建我们的一个支付中心的订单了。 create payment order 可以进去看一下。在这里面其实也是非常简单，从 Bo 里面获得相应的一些数据，再填充到我们当前自己的订单。欧德斯。填充了以后，我们通过 Sid 去生成一个 ID 号，再往这里面去设置。随后当一些相应的数据全部都填充完毕以后，我们就可以直接去把这条数据插入到我们的数据库里面去了。


OK，这一整个业务执行完毕以后，我们在这边会也蹭一个 OK 的状态，这个 OK 的状态是返回到我们的天天之货的一个接口，也就是调用方。因为接口我们是要由我们自己的系统发送一个 rest 请求过来，以后，它肯定也是会发送一个相应的是否成功。它有一个 m 可 JSON results，我们也能够去进行接入的。所以我们在这里要来构建商户订单的一个对象，再传过来OK。好。现在回到我们自己的项目。商户订单相应的一些内容其实都是在我们操作订单在创建订单的时候去进行的。在创建订单的时候，我们先可以进入到service，在这里面我们可以找到它的最下方，在这个位置我们在这里可以去构建。这是写上第四步，这是构建商户订单，用于传给支付中心。OK，写一下 my chance。相应的它会有一个VO，也就是书传入过去的一个对象。这个对象我们到这里面直接可以拷贝一份。在这里他是接收的时候叫做我们唱子 o 的 b o。在这边我就直接拷贝了。我把直接拷贝一下。拷贝了以后贴到我们自己的项目。在这边我们会作为一个 CEO 传过去，我们推到这个位置，它是作为一个feel，然后把它进行一个重命名，改为 CEO 就行了。


好，现在是一个 VO 了。好，在我们的订单的 service 里面是需要把 VO 我们给 mue 一下。随后在这里面去塞入相应的内容。首先第一个要设置一下咱们的一个 o 的ID，订单ID，其实就是这个 order ID。随后再来一个 set 一下 user ID，用户 ID 在我们当前 service 里面本身也有。好。再下一个是一个总金额amount，总金额 amount 在这里我们就应该要去做两个累加了。找一下。在我们的当前这个方法里面其实有用到了一个 total amount，以及是 real pay amount 对吧？其实我们使用 real pay amount 就可以了，要去做一个累加。累加是加上它的一个运费，之前运费其实在这里我们写 s 为 0 了，所以我们在这里要去加一下。需要注意是 real pay amount 加上运费，而不是 real pay amount 去加上 total amount。这里注意一下，写错这个钱就会很多了。


好，再来设计一下。 set 一个 pay method，OK，总共是有 4 项属性，另外它还有一个属性是 set 一个return。但是这个我们是定义在了 base Ctrl 里面，所以我们到 Ctrl 里面去设置也可以。现在我们就需要把 machant order feel 给传入传回到 Ctrl 了。但是由于现在在这里我们有一个 order ID，怎么办？其实我们在这边可以去构建一个 order view，我们可以把 order ID 以及是 VO 统一的传入到 o 的 VO 里面去。在我们的 controller 接收了以后再进行相应的一个业务也可以，所以我们在这里写一下 order VO，我们现在还没有，所以我们去创建一下。在这里我们可以随便我们就挑这个拷贝一份，取一个名字叫做欧德福优。在欧德福欧里面我们就可以塞入相应的内容了。


首先第一个我们写一个 order ID，这是返回的一个订单的ID。另外一个我们要传出来商户订单的信息，所以我们在这边我们也要去写一下。其实就相当于是我们的一个嵌套VO，一个 VO 里面再嵌套一个VO，在这里面会有两个属性，有了这两个属性了以后，我们再去把 get 和 set 去生成一下，好 VO 就创建好了。在这边我们直接把它给诱出来，写个注释。这是第5步构建自定义。


订单。 CEO 在 order view 里面，点 set order，把订单 ID 放进去，然后再来一个set，点 set machant 订单，把它给放入进去，这样子就 OK 了。我们只需要在它返回的时候把原来的一个 order ID 改为一个 order VO 就可以了。当然我们当前 service 它的方法我们都要去改掉。另外在这里面也要去改，这是它的接口。OK，改完了以后，我们在我们当前 service 返回出去的内容 VO 里面就包含了订单的 ID 以及是商户订单的信息了。在我们的 Ctrl 了肯定也是需要去进行修改的，在这里改一下。


在这边我们创建完毕订单以后，在这里是通过一个订单的 VO 去接收，我们还会有一个 order ID， order ID 直接就可以通过 VO 里面去get， get 一下 order ID，这样子就可以了。下面的一些方法在下面会有一个返回，就可以拿到对应的 order ID 了。


最后还有一步没有做，在这里面的一个 machant order for you 写一下，这是通过 old of you 点get，拿到了以后， view 里面由于我们没有设置一个 return URL，所以我们应该要去拿一下，把配 return URL 给写过来。这样子我们商户订单的一个信息现在就已经是写好了，以后只需要在这边叫。第三步，我们之前写了一个注释，我们要把商户订单的信息发送给支付中心，让支付中心去进行一个保存就 OK 了。


