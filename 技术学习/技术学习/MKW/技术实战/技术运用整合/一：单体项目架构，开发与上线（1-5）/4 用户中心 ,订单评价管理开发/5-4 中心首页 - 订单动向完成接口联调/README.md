---
title: 5-4 中心首页 - 订单动向完成接口联调
---

# 5-4 中心首页 - 订单动向完成接口联调

[image](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/ea589c33-e6cc-417f-9a17-95a0483831b3/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663DGTRYES%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T224743Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQD9RnlKRxtAyBuI0jfc4%2FZcvNwfJhCgf18smgKGoxDmFQIgdKhDJoA0WjhPpa%2BInBaicQm8yBtCEj3nI7H2MFoRKOMqiAQIxv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDLsnsNYMWzyNn2eM1yrcA2MGDxyJyhJJOGhodfUhL%2FrwT70Pevrrne3lKt0Hl4VpdNDdDG%2FNni%2FZvw6ea7KBP63VPx1cHAVui7KYW%2BjmYw9x1XsdKe%2FBaeXALe4uqbKiYkpsgXIxU%2FbDtYk524LoFANJd19nM1TfP4lTz9F%2BfjzRWBNStQWvyBhL170SoVyC2PjYe3%2Bh7TLNkQ0P7%2F%2Fe8k49VJa2UI5nJNk3L%2Bp1E5ENv4XqyiXdEXXiCtsoca1UKfEUA2xskaNIK5pvezfm3C5C5%2FtgPo0f32y49nl2Cl1RuqUOQu4AQLgQK5lSu62wJpAEoatG8D7ATON85DxqYL3LkOMs0iAGB5Vp%2ByhKih9DFgChN9o5IdOS%2FrcnK2EHqnn%2BwhGjHHH7JVCJlJAa3srWEdC6acYBoAjY8hZfIQlusXtGRmWwU7UJ67jQ4APhjSMaLaJXWng7TZom23FZv2a7puVLUxW2JlJlxXP1dvbN9ajbIxNVJYHkniwjImSF%2FR64rbXP1u91cpg1%2F59ju%2B7EYFBgAJUVQOZsPg2TytCDxlqhC4Y240LWuSfmUqpUqW%2BfAb2sj8EogEzb26x3fMq7T1INXr7yBk9Guv87U%2FJXucfPyVI%2BR5EjQr5qzGnJBdCbFEPX%2BRp8FC3SMKW3%2F9IGOqUBlw3Lb5rn0noVQx8OmhGTd%2BQnPI6u%2F1vOl6DXrtSwSIseYI6xqc7MK%2BuJaZxzIFMT7iGtC6eFKbZjnJTML5jLOOkamYzP9aufYEslXb2QoibSwpYriaWTxqF8CaUVruP7PP98Elyvz9UVhEZznT%2FREUhMTgM3TbYeD1EL2JkkmwRetsbPc%2BN1Ts%2FgEBd8OkdiOlx1kv8h8OKupNGnU4DLj3FKDJgp&X-Amz-Signature=8279103a41594566d25e4c1343d3d455c7da9daa0c8a530e64086c045248ed25&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

写完了 map 以后，我们就应该要去写一下 service 以及是 Ctrl 了。这个是和分页查询有关的，所以分页我相信大家应该写的也是。老铁都出来了。先写一下方法。 public page 的 great results，我们当前其实写过，搜一下把直接拷贝过来。拷贝过来以后做一些修改。这个是 get orders trend 传入的参数。一个是用户 ID 分页的配置和配置size，这个不需要了，这样子就行了。好，加一个注释，获得分页的订单。动效。好。OK。随后我们到 service 里面去把去实现一下。不要忘记还是一样这个事物得加上使用supports。好，在这里面就可以去写上相应的内容了。


首先我们还是一样要去构建一个map，这个 map 里面我们所放入的一个参数就是一个用户ID。好，我们就可以去做一个分页了。分页 page helper 点 start page，把参数给放进去，一个是第一个是page，第二个是 page size。好。开始分页以后，我们就要去做一个查询。 order map custom 点 get 一个trend，把 map 给传进去，这样子我们就可以获得对应的一个list，我们是定义的为 order status。好，OK，拿到一个list，随后我们要 return 出去。


在这里我们由于之前写了一个set，把对应的 list 以及是配置给放进去。当我们拿到了一个 grade 以后， grade 我们就可以直接给抛出去了。这里其实我们是把在这边其实我们之前写了一个 extend base service，这是我们之前所写的，所以写了以后这个方法我们就可以去掉了。这样子在我们刚刚所写的这里调用的 set up page group，就可以直接去调用 base service 里面这个方法了。OK，好，这样子我们 service 就已经是 OK 了。接下来要去写 Ctrl 了。写 Ctrl 了之前我们就应该要去先看一下前端，前端还是一样找到科瑞奇的，这里面有一个订单的动效 render order trend，搜一下。


在这里这边是执行的一个路由，取的名字就叫做是券的。传过去的参数只需要传一个用户 ID 就行了。这个配置是常规的参数，拿到了以后，在这边就可以去做一个循环的展示了。循环完毕以后，有一步操作是针对它的时间。时间我们也说了，我们传到前端的时候是一个 date 数据类型，它是需要做一个 format 格式化的，格式化了以后，它才会在页面上去做到一个效应的渲染和展示。在前端页面里面，在这边可以看一下，这是它的一个循环循环。


每一项拿到了以后，在这里边它会把相应的内容去做一个判断，它是针对状态去判断的。首先是2020，在这里它所要去显示的一个付款时间就是一个 pay time，如果是30，就是一个 deliver time，如果是一个40，发现一个bug， 40 应该是时间交易成功的时间。在我们的后端 CEO 里面，后端的 status 里面我们可以去看一下，这个是我们发现的一个小bug，我们可以改掉。


这个应该是一个 success time 40 交易成功的一个时间，所以我们要到前端把刚刚写的给改一下，这样子我们会显示一个成功的时间了。OK，在是一个 2030 和40。其实我们在一个做查询的时候，我们把关闭的时间，还有是一个下单时间我们也写了。当然如果你要去修改一下自定义的 SQL 语句，可以把额外的 10 和 50 的状态都可以加进去，这样子你可以去把前端代码再去扩展一下，显示的一个订单动向就会额外的增加两个状态 10 和50。OK，大家是可以自己去扩展的。随后我们就可以到后端去把对应的接口方法去写一下了。


到 Ctrl 里面，这个其实也是分页，你们拷贝一份，最快直接拷贝到我们的最下方。在这里就要去做一个相应的修改。这里是一个券的改一下。 spark to 接口名字就是查询订单动向，相应的它的一个 method 也应该是一个post，好传入过来。一个是 user ID，这个是需要的。另外订单状态是不需要，好配置和 page size 也是要的。下方这些内容，这些我们就保持不变，都要用的。在这里会发起一个请求，请求是 get order trend，传入进去一个 user ID。订单状态不需要，这两个也是要的。查询完毕以后，把 grade 直接丢给前端，前端就可以去做一个渲染了。


OK，好。这样子我们 Ctrl 的就已经是写好了。 install 一下，好因素成功。随后再要做一个重启。好，OK，到我们前端去测试一下。刷新一下。刷新一下以后可以看到相应的一些订单的动向，它的内容在这里全部都有了。以后我们是可以去做分页的。第二页是订单交易成功的，这里是订单发货的。等等这些信息都有了。第三页，OK，这样子我们订单动向就已经是做完了。


