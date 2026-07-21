---
title: 3-30 【技术改造】电商系统集成Eureka - 订单中心-1
---

# 3-30 【技术改造】电商系统集成Eureka - 订单中心-1

[image](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/7b236f56-396a-443e-89a1-6c8281e9058f/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466Q5PUEFTI%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T225557Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIFKIpHrKu8nmcJl7g2nGwWLiyrO1gGLwRMpE5kZX%2F27UAiEAspq%2FbTTUdt%2FMlrZSaKtqrpVgiR4iboKNaxtKIL%2BYRcMqiAQIxv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDML0eEa2%2BYShwqq0JSrcA%2BqyHrvUiZCZluGFdMCt14pNdSdb8v3eXokCdnOioMQhsIDgzkm312x14Gz3KIrwuW0mWTh281xPOWOHfpdiFxKUEU%2B%2F19K0SQn4tko%2FNQ2nMuC9UG%2FQf%2BV%2BIPmEADnBkifD5sk8E5j4%2FRPpyxQ5WIXfOEgNIKtLYUET1dZS6dW4tuMmjSCj98KkwcMnopuPqca1tFs%2FxKLRizJpMEE0c2pe3kOy0ZCQSQHHXsj549wCs3JlN20mdSEN0AkM1vqZjxYDXD%2BngeW0RqIx0K7vU5MGyZ72y2oU8WAAkPuhwN2xW03478gcmeLYJHi8ef%2B4mvTqZXhQQi%2F8oE6nE4JDEc9P3NEJ8sRxWoINOrL7IwF3S3KpaRFM3uSpmYYHtm4hWLaGpWlzABLVSs6iLjuZzbQQ3zvziNuyebbbWEs2warOG5fkRMZryMSaA3EBsnv60%2FvslCHO7lelsS69losR2jHm4s4pqtGQNmTtOL01p9THtCByR7JDoIHdENA79KWlYZ4DT41Ml6h%2Fj1SFuNSviYZbVlNGWFpqTYtoF2CDVhUMxL1EH5vUYCMPoeT8HL687U%2B3pDkkpwn3WXsQhQKd2PRQ76RlX5eiySZUL2Yne2Hz1BUcnZugOPLVKTM4MMS6%2F9IGOqUBCCfMK1Sca4bV1TX2hNYrEbfWVU%2BRWHOGZnvtcL7Hh08%2Fox8uggr7YVoGMhpuPxfPWkEbf0%2B921MTkEGtYh6Q519j%2BChbW4nZ9I07AIL2a9pQwPJ1xSQGeE3RMfMRXNd3N7OXY274YJ62o1Lou1QqE5wHE6rsmjMKJitUkC%2F42bqrt1dF2x8eZEfkCC48tAfIeJWNTNgulaQwkzvZznKYwTW%2FFozG&X-Amz-Signature=49fc8fc63f8f17995e62f7c9ce7bbe009fe709439e973a88b6b002c9de6003b9&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

[image](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/0d2cbb69-2fb0-4045-a8ae-b39222cdb9a0/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466Q5PUEFTI%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T225557Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIFKIpHrKu8nmcJl7g2nGwWLiyrO1gGLwRMpE5kZX%2F27UAiEAspq%2FbTTUdt%2FMlrZSaKtqrpVgiR4iboKNaxtKIL%2BYRcMqiAQIxv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDML0eEa2%2BYShwqq0JSrcA%2BqyHrvUiZCZluGFdMCt14pNdSdb8v3eXokCdnOioMQhsIDgzkm312x14Gz3KIrwuW0mWTh281xPOWOHfpdiFxKUEU%2B%2F19K0SQn4tko%2FNQ2nMuC9UG%2FQf%2BV%2BIPmEADnBkifD5sk8E5j4%2FRPpyxQ5WIXfOEgNIKtLYUET1dZS6dW4tuMmjSCj98KkwcMnopuPqca1tFs%2FxKLRizJpMEE0c2pe3kOy0ZCQSQHHXsj549wCs3JlN20mdSEN0AkM1vqZjxYDXD%2BngeW0RqIx0K7vU5MGyZ72y2oU8WAAkPuhwN2xW03478gcmeLYJHi8ef%2B4mvTqZXhQQi%2F8oE6nE4JDEc9P3NEJ8sRxWoINOrL7IwF3S3KpaRFM3uSpmYYHtm4hWLaGpWlzABLVSs6iLjuZzbQQ3zvziNuyebbbWEs2warOG5fkRMZryMSaA3EBsnv60%2FvslCHO7lelsS69losR2jHm4s4pqtGQNmTtOL01p9THtCByR7JDoIHdENA79KWlYZ4DT41Ml6h%2Fj1SFuNSviYZbVlNGWFpqTYtoF2CDVhUMxL1EH5vUYCMPoeT8HL687U%2B3pDkkpwn3WXsQhQKd2PRQ76RlX5eiySZUL2Yne2Hz1BUcnZugOPLVKTM4MMS6%2F9IGOqUBCCfMK1Sca4bV1TX2hNYrEbfWVU%2BRWHOGZnvtcL7Hh08%2Fox8uggr7YVoGMhpuPxfPWkEbf0%2B921MTkEGtYh6Q519j%2BChbW4nZ9I07AIL2a9pQwPJ1xSQGeE3RMfMRXNd3N7OXY274YJ62o1Lou1QqE5wHE6rsmjMKJitUkC%2F42bqrt1dF2x8eZEfkCC48tAfIeJWNTNgulaQwkzvZznKYwTW%2FFozG&X-Amz-Signature=c03ed0d67eee950c8889722e06353903657dd2533d11097f76ebbf74c78aa426&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

ello 慕课网的各位同学们，大家好，我是小半仙。那咱这一节去改造整个尤瑞卡商城，改造环节中的最后一个微服务模块是订单中心。那还剩余的几个微服模块，就留给同学们当做作业，让大家自己去体验一把微服务的改造过程。

[image](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/a56bcac6-95e8-4aef-914e-722341770bb1/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466Q5PUEFTI%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T225557Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIFKIpHrKu8nmcJl7g2nGwWLiyrO1gGLwRMpE5kZX%2F27UAiEAspq%2FbTTUdt%2FMlrZSaKtqrpVgiR4iboKNaxtKIL%2BYRcMqiAQIxv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDML0eEa2%2BYShwqq0JSrcA%2BqyHrvUiZCZluGFdMCt14pNdSdb8v3eXokCdnOioMQhsIDgzkm312x14Gz3KIrwuW0mWTh281xPOWOHfpdiFxKUEU%2B%2F19K0SQn4tko%2FNQ2nMuC9UG%2FQf%2BV%2BIPmEADnBkifD5sk8E5j4%2FRPpyxQ5WIXfOEgNIKtLYUET1dZS6dW4tuMmjSCj98KkwcMnopuPqca1tFs%2FxKLRizJpMEE0c2pe3kOy0ZCQSQHHXsj549wCs3JlN20mdSEN0AkM1vqZjxYDXD%2BngeW0RqIx0K7vU5MGyZ72y2oU8WAAkPuhwN2xW03478gcmeLYJHi8ef%2B4mvTqZXhQQi%2F8oE6nE4JDEc9P3NEJ8sRxWoINOrL7IwF3S3KpaRFM3uSpmYYHtm4hWLaGpWlzABLVSs6iLjuZzbQQ3zvziNuyebbbWEs2warOG5fkRMZryMSaA3EBsnv60%2FvslCHO7lelsS69losR2jHm4s4pqtGQNmTtOL01p9THtCByR7JDoIHdENA79KWlYZ4DT41Ml6h%2Fj1SFuNSviYZbVlNGWFpqTYtoF2CDVhUMxL1EH5vUYCMPoeT8HL687U%2B3pDkkpwn3WXsQhQKd2PRQ76RlX5eiySZUL2Yne2Hz1BUcnZugOPLVKTM4MMS6%2F9IGOqUBCCfMK1Sca4bV1TX2hNYrEbfWVU%2BRWHOGZnvtcL7Hh08%2Fox8uggr7YVoGMhpuPxfPWkEbf0%2B921MTkEGtYh6Q519j%2BChbW4nZ9I07AIL2a9pQwPJ1xSQGeE3RMfMRXNd3N7OXY274YJ62o1Lou1QqE5wHE6rsmjMKJitUkC%2F42bqrt1dF2x8eZEfkCC48tAfIeJWNTNgulaQwkzvZznKYwTW%2FFozG&X-Amz-Signature=6e3f94f0a21b7813fbc9659d4b0a796a33bac1dcdb2845234affb7f36f7cdb30&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

好，咱订单中心这里主要要迁移的功能，就是订单的创建、查询，还有状态转移等等。除此以外，跟前面两个微付章节不同的地方是我们在订单中心里还要去集成用户模块，还有商品模块的微服务。 OK 那我们现在就转战 intelligi 好同学，我们在 foodie cloud 当中的 domain 这个文件夹下创建一个专门供订单中心使用的 order 文件夹，然后依然开始从 pool 9 开始创建。那第一个模块我们的名字叫做 food 杠 order 杠 pojo 好，这个步骤和前面都是一样的，我们把它放到 domain order 下面。那因为前面我们已经做过两个章节了两个微服改造非常熟悉了，所以这里我就加快进度。那细枝末节的细节我就不跟大家一一展示了。那这里的 food order por 酒这里我们仿照前面创建好的微服务，把它的 dependency 给它 copy 过来，好变魔术。



321 走依然是 persistence API 和 hibernate validator 那这两个 copy 过来以后，我们在 Java 里面创建慕课网的路径，com.imock后面跟点 order.pojo 那后面就到了喜闻乐见的抓壮丁环节了，咱转换到 food cloud 当中。好，我们这里打开 pojo 看哪些是咱订单域需要转移的。那这三个以 order 开头的 orderitem orders 还有 order status 这三个把它。好，转移过来先把它们晾在这儿，不用管我们继续创建 package 这里创建一个 BO 还有谁呢？还有一个 will 那我们先来从 BO 开始去copy 。好，我们转换到这里，我们 copy 哪些内容呢？只有一个 submit order BO 我们把它 copy 过来，划不到 BO 模块里面，然后这里在 BO 里面继续创建一个 center 好，这个 center 我们要把 foodie DEV 当中切换过去，找到它的 center 把谁把这个 order items comments 把它给 copy 一下，然后再给迁移过来。
OK 那待会儿我们等创建到具体服务的时候，还会新建一个BU ，等到时候我们再来给大家去一步步创建。好，那这里接下来轮到了谁 view 那 view 这里 copy 的内容比较多，我们切换到福地带。好 VO 这里和订单域相关的，我们从头到下看一下 merchant orders 这个是相关的，还有 my orders 以及 my sub order 还有跟订单状态相关的 order status 以及 order view 这五个类，我们 copy 一下。好，把它迁移过来。


同学们看到这里有个红叉，是什么？是 shop card BU 那它是在哪里呢？它被我们添加到了上面的 share 的 portal 这个类里面，所以我们在 order portal 里面，把这个 share 的 portal 同样的给它引入进来，这样的话就可以访问当前咱这个 shop card BO 这个累了，我们把 artifact 给它打上 foodie shared portual 那它的 version 用一个变量给它替换。好嘞， version OK 这里再重新 port 一下。然后我们把它的路径给改一下。好，这就不报错了。那咱 pose 就创建完成了这个模块。创建完成之后，我们继续创建下一个模块。是谁呢？是 mapper 那给它起名叫 foodie order mapper 好点击 next 我们把路径打上 order OK 点击 finish 那 mapper 的 palm 当中有哪些内容呢？我们直接复制过来。同学们看这里就是一个 order 的 pojo 还有 cloud common 这两个包。


好，那接下来我们去迁移代码部分，这里的包路径依然是 IMock come.imock.order.mapper 好，那这里有哪些内容需要拷贝过来呢？我们转移到福地 DEV 当中看这里在 mapper 下面有 12344 个以 order 开头的 mapper 我们把它 copy 一下，好，转移过来。那在转移过来之后，咱需要去更正 import 当中的路径。我这里就不一个一个改了，同学们去自己动手把路径四个类的路径给它更正过来。好，就像这样把路径全部更正过来以后，咱在 resources 下面去创建一个叫 mapper 的目录，然后去把 xmail 文件给它拷贝过来，我们切换到负 D DEV 当中。


x3l 文件和咱前面 copy 的 mapper 是对应的，就是头 4 的以 order 开头的 mapper 我们把它 copy 过回来。然后还要做一件生产线的流水线工作，就是把这里面的路径给它一一更正过来。好，就像这样，同学们自己动手把这四个 mapper 全部路径改成 com.imock.order 那这一步改完之后，咱整个 mapper 也已经创建完成了。
那接下来咱就去创建谁创建 API 那这个 API 里面我们将要引入一些不一样的东西，它的 artifact 叫 foodie order 杠 API API 好走，你那文件夹这里选中 domain.order 把它塞进去好勒。那创建好 order API 之后，它有哪些依赖项需要加入进来呢？好，那我们一键粘贴过来。


那这里我们看到和前面两个微服务模块的 API 层是一样的，这里有一个 share 的 portal 还有 order 的 portal 那以及 spring boot starterok 那我们接下来就去 API 里面创建接口其实这个过程相对来说比较机械性，如果基础比较好的同学，就不用去跟着老师这样一步步做，可以自己去发挥想象力，按照自己的理解去划分这些模块，也可以把某些模块拆分的更细。比如说什么呢？在商品中心对不对？商品中心里面有很多子模块，比如说营销优惠，那基础比较好的同学可以去尝试做一个什么呢？一个营销优惠的计算引擎，然后作为一个微服务和商品中心集成进来。


那接下来我们这个文件夹创建好了 order service 我们去到 foodie dive 当中，把这个 API 给他找到，然后迁移过来。是哪个 API 呢？ order service 好，就是你了，我们把它 copy 一下粘贴回来，先别急着改这里面的东西，我们紧接着再在它的这个文件夹里面创建 center 好回撤。那在 center 里面我们也要去移植两个服务，是谁呢？我们过了好，到 standard 里面找到这两个，一个是 my order service 还有 my comments 把这两个 copy 一下，然后复制回来。那咱排排坐，这三位大哥一个一个先来改造谁 order service 好，我们 order service 这里咱要把这些错误的路径给它重新 import 一把。


好，把这个 import 全部修正了以后，咱接下来给这个 order service 添加一个 request mappingrequest mapping a request mapping 到哪里呢？到 order API 然后接下来第一个 API 叫 create order 那这看起来是一个非常重要的 API 不过如果你想把它以 rest 形式的接口提供出来。那它这个入参前面一个 list 后面一个 response body 那咱尽量的怎么样呢？把它两个二合一，这样比较方便前端来构造这个参数。 OK 那咱怎么把它二合一呢？那我们这里就要做点不一样的东西了，点击进去 submit order BO 我们在这里给它创建一个好兄弟，这个好兄弟咱叫 place order 比 please order 就是下单的意思。


那这好兄弟里面有什么参数呢？我们来看第一个参数，我们就把这个 submit order BO 给它拿进来叫 order 那第二个参数是谁呢？就是咱的 list shop shopping carok 给它起叫 items 那咱接下来要用 long book 给它做一些修饰。第一个咱添加一个 data 这样的话我们就可以自动生成 get set 方法，然后我们再给它做一个无参构造器。无参构造器完了之后，咱再来一个有参构造器，把所有参数给它列取出来，这样的话我比较方便去构造这个对象。那其实 long book 注解非常方便的，这只是它其中几个小的功能点。那比如说你想实现 build 模式，我这里还可以使用 build 对吧。然后更有意思的是啥？ lombbook 注解里面它有一些experimental ，你看这个包看到吗？ experimental 这个包里面有很多非常有意思的特性龙 book 其实它这个里面的内容非常的庞大，那同学们如果有兴趣可以去看一看。我觉得这个短小精悍的工具类还是读起来蛮有意思的。


好我们回过头来，那咱创建了 place order BO 以后，在这里就要把它应用上怎么应用，我们的这个方法的入参，我把它替换掉就叫 place order BO 。它的名字也叫熬点 BO 好了，OK那接下来我要给它添加一个 post 因为它是创建订单，那自然而然是个 post mapping 那它的 URL 就叫 place order 同样的它的入参我给它叫 request bodyok 好，下面一个修改订单状态用 put post 还是用post 。那这里的路径我给它设置为 update status 好，前面的两个参数分别给它指定 request param 写上 order ID 这是第一个参数。那第二个参数我们给它写上叫 order status 那这两个都是必填的好，接下来是查询订单的状态，那咱这里给它改成 get mappingget mapping 谁路径就是 order status 同样的入参，给它限定好 order ID。 Ok. 那最后一个是叫关闭超时未支付订单。好这个方法大家不要轻易调用。好，我们这里给他提供一个路径叫 close handing ordersok 等。


后面我们学习到 stream 的时候 spring cloud 当中的 stream 那我们会尝试怎么样呢？尝试把这个关闭超时订单的流程加入到延迟队列当中。那我们在接下来的课程当中，也会逐步的把咱前面用到的某些组件替换为 spring cloud 的组件。所以说这也是我为什么选择一个相对比较早的版本一个腹地 DEV 的版本进行微服务改造的原因。因为早一些的版本比较纯净，像我这里选的就是基于 Redis 的版本。那后面我们添加了很多的内容，但是这部分有一些内容将要在微服务当中被微服务组件所替代，小伙伴们就等着慢往后学，慢慢看就可以了。


好，那咱这里去改造下一个 service center 里面的 service 好。第一步，咱先把这个 import 的路径给它更正过来。更正好了以后，我们在 my comments service 上面给它添加一个 request mapping 那它的路径叫什么呢？就叫 order comments API 好。那第一个方法是根据订单 ID 查询商品，我们给它一个 get 请求，那它的路径是 order items 它的入参我们给它限定上 request param order ID 好，那第二个第二个方法是保存用户评论，那这里保存自然是 post mapping 那我们叫 save order comments 那这里面我们将会调用到商品中心的一些服务。 OK 我们把 request param 从上面给它 copy 过来。第一个参数，第二个参数还有第三个参数。那这第二个参数我们把它改成 user ID 第三个参数就不是 request param 啦，我们给它改成 request bodyok 那接下来往下看，根据分页查询评论这一个是不是已经移到商品中心了？所以我们就不用管它了，把它给删除掉。因为咱这个服务它查询跟订单领域的关系并不太大，你看前面都是以 order ID 作为初始起点来查询评论的。那下面一个我们就从订单中心里面把它移植了出去。所以我们这里加一个comments ，叫移到了移到哪里呢？ item comments service the 那他也改好了。
最后一个我们找一下最后一个服务是谁？最后一个客观里面请 my order service 好，my order service 这里我们把 import 路径全部给它更正过来，头顶一顶大帽子，盖上 request mapping 路径是谁叫 my order API OK 那接下来第一个方法是一个查询请求，所以咱是 get mapping 路径，给它指定叫 order query 那 query 哪些内容呢？我们来看。


第一个， request param 那要 user ID 给出来，然后下面 all the status 还有 page page size 。我们把这里挨个分一个 request mapping 再把后面的字段名给它拷贝到前面。这个 page 和 page size 是必填的吗？我们以防万一，万一不是必填的对吧？所以给他加一个 require 等于 force 好，那接下来一个服务是什么？是订单状态商家发货，那它自然是一个修改订单状态的服务了。所以是一个怎么样 post 对不对？它的路径我们叫 order 后面商家发货了。那这是一个什么业务呢？这是 delivered 也就是说你的订单被 deliver 了。


好，那我们这里给他的入参叫 order ID 限定一个 request parentok 那第三个接口是什么？是查询我的订单，一看就知道是个 get 请求。这个 get 请求里我们给它限定叫路径是 order details 因为它是通过一个 order ID 来查询，所以肯定是怎么样获得一个独立的 order 它不会获得一个 list 那我们这里把它的入参给用 request pair 修饰起来。


OK 那接下来到了下一个，下一个是更新订单状态叫确认收货。 OK 那我给他指定一个 pose 的请求叫什么呢？它的路径叫 order 后面跟 received 被确认收货了，那 received 好，那接下来到最后一个删除订单。逻辑删除，这里又用到了 delete mapping delete mapping 这里我们给它的路径就叫 order 因为 delete 动作已经下放到了什么，下放到了这个 mapping HD DB master 这里，我们给它的入参修饰好，还有几个方法，还有最后两个。那接下来一个是查询用户的订单数，它是一个 get 请求，然后路径我们给到 order counts 啊统计的意思啊统计计数，把入参修饰好。
那到了最后一个了，这叫获取分页的订单动向，自然的也是一个 get mapping 它的路径是 order 后面跟什么好，订单动奖，那就跟李老师这个命名保持一致，叫 order trend 小写。那前面的这些字段入参我们给它修饰好，看起来一切都完事了。但是我这里还要给他加一个新的服务。谁呢？我们把目光转向这样一个类 controller 好，我们往下滑。


看到这里吗？同学们有个 fix mefix me 什么东西要 fix 呢？他说下面的逻辑移植到订单中心，也就是说咱 base controller 是一个在所有微服务中都需要去用到的一个 share 的 component 那既然是 shared 那我这里关于订单域的代码就不适合再放在这里了，所以咱把它 copy 一下，然后 copy 到哪里，copy到前面咱的 my order service 这里，把它复制过来。好复制我只要你的这个前面这一行方法声明就可以了。那它就作为一个独立的方法提供出去。它的作用就是 check user order 看你的 order 和这个 user 是不是同一个，那给它一个 get 请求，然后路径是 check user order 好入参，同样的，我们给它限定好，这里是 user ID 下一个参数是啥叫 order ID 那到这里，咱用迅雷不及掩耳盗铃之势，把 order 下面的 pojo mapper 和 API 三个模块都给创建好了。那早上半场就到这里结束了。下半场我们来继续完成订单中心的微服务改造。好，同学，我们下一节课程再见。

