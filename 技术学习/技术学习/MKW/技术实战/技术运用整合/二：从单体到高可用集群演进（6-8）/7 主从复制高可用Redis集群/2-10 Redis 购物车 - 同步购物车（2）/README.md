---
title: 2-10 Redis 购物车 - 同步购物车（2）
---

# 2-10 Redis 购物车 - 同步购物车（2）

[image](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/4a7ef9f9-82bf-47d9-b4e3-e65edf3adf3e/SCR-20240805-ilwi.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663PDQ3QH6%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T224947Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQD4SFepraQQRiEjDO0lnGShFmZNcaPtwIuWeJvpRCoMEQIhAMQhnfgviAZpImBQy6LkTGMPI3gfkYOWxqm9u3ThSn9VKogECMb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1Igxg5DUZMThZxGTjoU4q3ANdIw3wREP6WnGIWIKYptxMcYCLf6tfrIossNI5UZWcHDCrw0MzAuGkOmkYitOPp8fUmLSG7xV5ztNWjowCUcEiTQFT%2BTcG3Dx94zxhjHycK3v9ztZhdBSj%2B%2BlreSflF4hqpgSUx3K6iGZgyk8KKANy62DDykS4E9Fw1Th%2B7aKaZJ5lfmz2UPNzV1xtO4tPrLxAUTsQiP5sR9A1dH8XAqMw3MxL7wc17VCSL4US8vi4b9yJeMHlEeV8NrPpx%2BWbKM1l012kmPPQGODh9vIHMVFMtLHFVtQCBdxlsKUIUPXwgq7TvMyCdncCY0HIXI1hIqzSrneHOFV48YGDfS919uDxfr1fnlczRN%2Fx8KgeWsHGgkJwS7Dt7Nzu3cj5w%2Fg1uEZRsQhAHL0EwDEdmP%2FiYA68ZDDI%2B3GYherpNgPi0FwfyipAC1gXgv3%2B8tEiwSRTPCW%2Fa4EShaFIsJsg1rL2NPOam64776dg8Lq6NmfUyTOuzAL%2BmYqsyVVUMeVO%2B%2F050FTbsV6fvuzATCNtM52QsMPByy0S%2FL2OXrmN8%2B37yB%2FMUGRFJIDR%2FJxp0KzSO4l7CjEF3VauiaOuEzVv4DCkRmkSRf1HyXm%2B2wPivj3oIztW7DeyRp%2B4AipLCt8diDCXuP%2FSBjqkAf5SyRvDAFV2ND%2F21JzEAGYyw%2BA0jcDXcd7k41DMs9mQCeuYsjCg73OkxesH%2Fwo%2FjyrNHX7iE5KnOIiEVl0N4hcSbUICZtQU6Co4s3x3iA9iztm%2F4h3vh8cfnJzVE7XNFK5p%2FpZjIZav3xVjqikT9AqpvwX3bhUREvLnwzdorl%2FBb9NHebNs583CCOKdO7MFHEaMb9nZ4aFjduXJ6iRB8eLjZW3k&X-Amz-Signature=1c15191d123b1254f2f8914fa0cd3cec5db683e99d1324282ec13d75c7b303a2&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

[image](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/2cda9880-5ae5-4643-8d7a-4c1250457e83/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663PDQ3QH6%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T224947Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQD4SFepraQQRiEjDO0lnGShFmZNcaPtwIuWeJvpRCoMEQIhAMQhnfgviAZpImBQy6LkTGMPI3gfkYOWxqm9u3ThSn9VKogECMb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1Igxg5DUZMThZxGTjoU4q3ANdIw3wREP6WnGIWIKYptxMcYCLf6tfrIossNI5UZWcHDCrw0MzAuGkOmkYitOPp8fUmLSG7xV5ztNWjowCUcEiTQFT%2BTcG3Dx94zxhjHycK3v9ztZhdBSj%2B%2BlreSflF4hqpgSUx3K6iGZgyk8KKANy62DDykS4E9Fw1Th%2B7aKaZJ5lfmz2UPNzV1xtO4tPrLxAUTsQiP5sR9A1dH8XAqMw3MxL7wc17VCSL4US8vi4b9yJeMHlEeV8NrPpx%2BWbKM1l012kmPPQGODh9vIHMVFMtLHFVtQCBdxlsKUIUPXwgq7TvMyCdncCY0HIXI1hIqzSrneHOFV48YGDfS919uDxfr1fnlczRN%2Fx8KgeWsHGgkJwS7Dt7Nzu3cj5w%2Fg1uEZRsQhAHL0EwDEdmP%2FiYA68ZDDI%2B3GYherpNgPi0FwfyipAC1gXgv3%2B8tEiwSRTPCW%2Fa4EShaFIsJsg1rL2NPOam64776dg8Lq6NmfUyTOuzAL%2BmYqsyVVUMeVO%2B%2F050FTbsV6fvuzATCNtM52QsMPByy0S%2FL2OXrmN8%2B37yB%2FMUGRFJIDR%2FJxp0KzSO4l7CjEF3VauiaOuEzVv4DCkRmkSRf1HyXm%2B2wPivj3oIztW7DeyRp%2B4AipLCt8diDCXuP%2FSBjqkAf5SyRvDAFV2ND%2F21JzEAGYyw%2BA0jcDXcd7k41DMs9mQCeuYsjCg73OkxesH%2Fwo%2FjyrNHX7iE5KnOIiEVl0N4hcSbUICZtQU6Co4s3x3iA9iztm%2F4h3vh8cfnJzVE7XNFK5p%2FpZjIZav3xVjqikT9AqpvwX3bhUREvLnwzdorl%2FBb9NHebNs583CCOKdO7MFHEaMb9nZ4aFjduXJ6iRB8eLjZW3k&X-Amz-Signature=2976f76c93ef22bbe6bb0f403dfd838c8b8e91d64f8801dda9e06cb94c222cd8&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

[image](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/5f305588-34f8-48d8-b622-d15f4959f8c1/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663PDQ3QH6%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T224947Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQD4SFepraQQRiEjDO0lnGShFmZNcaPtwIuWeJvpRCoMEQIhAMQhnfgviAZpImBQy6LkTGMPI3gfkYOWxqm9u3ThSn9VKogECMb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1Igxg5DUZMThZxGTjoU4q3ANdIw3wREP6WnGIWIKYptxMcYCLf6tfrIossNI5UZWcHDCrw0MzAuGkOmkYitOPp8fUmLSG7xV5ztNWjowCUcEiTQFT%2BTcG3Dx94zxhjHycK3v9ztZhdBSj%2B%2BlreSflF4hqpgSUx3K6iGZgyk8KKANy62DDykS4E9Fw1Th%2B7aKaZJ5lfmz2UPNzV1xtO4tPrLxAUTsQiP5sR9A1dH8XAqMw3MxL7wc17VCSL4US8vi4b9yJeMHlEeV8NrPpx%2BWbKM1l012kmPPQGODh9vIHMVFMtLHFVtQCBdxlsKUIUPXwgq7TvMyCdncCY0HIXI1hIqzSrneHOFV48YGDfS919uDxfr1fnlczRN%2Fx8KgeWsHGgkJwS7Dt7Nzu3cj5w%2Fg1uEZRsQhAHL0EwDEdmP%2FiYA68ZDDI%2B3GYherpNgPi0FwfyipAC1gXgv3%2B8tEiwSRTPCW%2Fa4EShaFIsJsg1rL2NPOam64776dg8Lq6NmfUyTOuzAL%2BmYqsyVVUMeVO%2B%2F050FTbsV6fvuzATCNtM52QsMPByy0S%2FL2OXrmN8%2B37yB%2FMUGRFJIDR%2FJxp0KzSO4l7CjEF3VauiaOuEzVv4DCkRmkSRf1HyXm%2B2wPivj3oIztW7DeyRp%2B4AipLCt8diDCXuP%2FSBjqkAf5SyRvDAFV2ND%2F21JzEAGYyw%2BA0jcDXcd7k41DMs9mQCeuYsjCg73OkxesH%2Fwo%2FjyrNHX7iE5KnOIiEVl0N4hcSbUICZtQU6Co4s3x3iA9iztm%2F4h3vh8cfnJzVE7XNFK5p%2FpZjIZav3xVjqikT9AqpvwX3bhUREvLnwzdorl%2FBb9NHebNs583CCOKdO7MFHEaMb9nZ4aFjduXJ6iRB8eLjZW3k&X-Amz-Signature=bd4204c3f9b1f67a890599857f29f45a26365fa147591a051421b5ed2c3ca800&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

那么接下来我们就可以来做一下，当 Redis 和 cookie 两者都不为空的一个情况下，我们应该要做的一个合并的处理。那么在这里面其实也是分为了几个步骤。第一步的话，已经存在的我们应该是要把， cookie 周对应的数量覆盖 Redis 中的，那么这个就是我们上面所说的参考京东，当然你也可以去做一个累加，这个都没有问题，因为这个毕竟都是由产品去提的。好。第二步，那么第二步的话，如果说对应的这样的一个数量是有一项商品的，该项商品那么应该要标记吧，标记为待删除，那么这个待删除的话，其实我们都可以统一放入一个待删除的 list 中。最后第三点的话，我们在这里肯定是会涉及到一个循环，那么如果我们这个循环现在已经是处理完毕以后，那么这个待删除的 list 他肯定会有，那么一旦会有的话，那么这个时候我们应该是要，从 cookie 中清理，所有的待删除 list 应该要清理，那么清理以后第四步这个时候那么在这里的话其实我们也是以原理为主的，所以我们应该要合并 Redis 和 cookie 中的数据，那么合并了以后就是一个最新的一个数据了。那么最终那么我们应该要更新到 Redis 和 cookie 中。


OK，那么主要是这 5 个步骤做好以后，那么这里的我们两者不为空的情况，我们就能够做到一个购物车数据的一个同步了。好，随后我们就可以来做了，那么首先的话在这里涉及到一个循环，既然是循环，我们就应该要把这两个 list 我们都应该要去做一个转化，写一下， list shortcut 比欧。随后这里写一下，这是 shop cut，list，标记为那是Redis，等于 Jason 与 test 进行一个转换。 Jason to list，那么这里面第一个，这是从 Redis 里面来的，所以把这个考虑过来。随后下一项是 shop cut b o 点class。好，OK，那么这是第一个list，随后第二个 list 就应该是一个cookie，把 cookie 拿过来，这里标记写一下。


这两个 cookie 我们都已经是准备好了，那么接下来的话我们就要去做一个相应的循环，循环的话我们是以 Redis 为主，所以把这个 Redis 的这个 list 给拿过来，在这里面我们是使用 for each，也就是这个 Bo 写一下，它是一个 Redis shop cut 冒号，然后这个 list 贴过来。那么在这里面其实我们已经是说了要有一个待删除的一个list，所以在它的外层我们可以去定义一下。第一个 list 写一下，这是一个判定 delete list，等待删除等待处理的一个 list 操作。那么在这里的话我们就直接可以把它给作为一个空的就可以了，这是定义一个待删除list。


好，OK。那么随后在这里面我们就应该要去做一个相应的循环了吧，那么这个时候循环的话，首先第一步我们应该要把它的一个 ID 给拿出来， string 写一下，就是 Redis 中商品，也就是商品规格所对应的一个ID，这是 string s t r 等于从这个里面你应该要拿出来吧。点 get 规格ID，那么这个它的目的拿出来是需要去做一个判断的。好，随后我们在这里面其实是一个双重循环，我把这个再写一下，这是一个双重循环，那么双重循环的时候，这里面这个时候第二重应该是循环它的一个 cookie list，然后在这里面这个我标记一下，这个应该要改为cookie。好，那么很显然这里面的这个 ID 我们也应该要去获取吧，所以这个标识写一下。好，OK，那么这是一个双重循环，然后在这个里面的话，我们就应该要去做一个判断了。


判断的话我们是已经说了，如果说两个商品是一模一样的，我们应该要把 cookie 中的覆盖掉。我们的一个 Redis 中的，所以在这里要判断一下我们的这个 Redis 的规格 ID 点ECOS，判断和我们的 cookie 是不是一样的。如果说是一样的，这个时候我们只需要去把这个 Redis 的 shop cut，也就是当前这个东西 Redis 的点 set by accounts，我们去做一个覆盖。覆盖的话只需要把这个 cookie 中的点 get by count 拿出来去做一个覆盖就可以了。加上注释，覆盖购买数量不累加参考京东，大家可以去试一下，京东的话就是这样子的。OK。那么这个时候的话，其实我们虽然是覆盖了以后的话，应该我们还要把这个当前这样的一个Redis，应该是 copy cookie 的 shop cut，我们应该要放入到这个等待删除的 list 里面去，把这个放入待删除列表，用于最后的删除与合并。那么在这里只需要把这个 pending list，然后艾特一下，把这个 cookie shop cut 添加进来，那么就可以了。


这样子我们循环了以后，我们的一个 Redis 里面的购物车，它的一个对应的数量会被覆盖，另外一个就是我们相同的一个数据在我们的 cookie 中的，那么会被删除，删除的话是放在这个等待删除的列表里面去的。好，那么时这个时候当我们的这个循环全部都结束了以后，此时此刻那么我们就要做一个删除了。删除的话我们是应该要删除咱们的cookie，把 cookie 里面的做一个删除，使用remove，然后再把这个排名这个 list 给写过来，写一下从现有 cookie 中删除对应的覆盖过的商品数据。


好。k。删除以后最后一步合并两个list，那么这样子的话我们之前也说了，我们是以 ID 所举的，所以我们就可以使用这个， Redis list 点 add or 再把我们的一个 cookie 的 list 给放进来，因为这个里面的一个 cookie 这个 list 的话，我们刚刚已经是 remove 了一部分的重复数据，那么这样子的话这两者的话现在我们就可以做一个合并了。


那么合并以后最终的这个Redis，这个 list 就是我们现有的最新的一个商品数据，商品的购物车数据了。OK，写一下更新到 Redis 和cookie，那么在这里面的话，我们就只需要这样子就可以了。先把这个写一下，这是 cookie 的接过来，那么这里面 set the spouse cookie，这是他的key，然后这是他的一个 Redis 这个列表，这是它的一个列表数据。那么在这里的话，很明显我们一定要把这个转换一下。


Jason retest 点 object to JSON。OK，这是 cookie 的设置，那么随后还会有一个 Redis 拷贝一下，在这里上面应该有，推到这个部位， user ID 不要忘记，然后这一部分那么其实也是一样，应该要把这个数据去做一个转换，转换以后再一次的放入到我们的 Redis 里面去，那么这样子的话他就可以去做到一个相应的一个更新了。


好，那么这样子的话，现在其实我们就可以来做一个测试了，我们还是要重启一下服务器。目前我们的这个 Redis 里面是有数据，一个是铜锣烧，一个是儿童早餐，然后看一下这个我们的首月进入到购物车，那么购物车里面现在是就有这两项东西，那么这样子我们把这个 cookie 清空一下， cookie 京东以后这个时候我们到这个首页里面去，我们先去随便的挑选一些相应的不同的商品，比方说我们来挑一个，找一个芒果干加入购物车。


好，随后我们再来看一下这个铜锣烧，以及是这个敖董早餐，是我们之前在咱们数据库里面本来就有的，然后我们在这边我们添加两个，另外一个我们的铜锣烧添加三个。好，来看一下。那么现在在购物车里面，那么这里面的一个数据的话，有两个商品在我们的一个缓存里面是有的，还有一个是没有。那么如果说我们现在要去做一个同步登录以后，那么相应的数据其实都会进行一个同步，会进行一个合并。那么也就是说我们现有的一个 Redis 的话，其实 Redis 上是有了这两个数据，那么我们在进行合并了以后，它的数量还是 2 和3，因为我们是直接做的是一个覆盖式的，那么此外它还会有一个芒果干，那么这个芒果干它并没有的话，那么它是还是会继续的合并，会放到我们的俄历斯里面去的。


好，那么现在我们就要可以来做一个测试，刷新一下没毛病，然后我们到咱们的页面，我们来立即登录一下，点击登录，OK。登录以后你会发现我们现有的一个购物车数据是没有任何的变化，因为这本身就没毛病。我们主要是来看一下我们的后端，我们来看一下Redis，刷新一下进来看一下，那么这个时候你会发现我们的一个儿童早餐和铜锣烧，一个是两份，一个是 3 份，那么这说明我们是在原有的基础上是做了一个覆盖，他没有去进行一个累加，那么这一块业务OK。另外一个这是我们新增加的一个，那么新增加的这一项的话，目前就已经是和我们当前这样的一个 Redis 里面的一个缓存数据做到了一个合并了。


那么现在这样子的话，其实我们就实现了这样的一块业务，不论是我们的 Redis 还是我们的一个cookie，它的购物车数据不管是哪一边为空，哪一边不为空，那么相应的一些情况下，我们都去进行了一个判断，并且最终也是达到了一个合并购物车数据的一个目的了。


OK，那么这一块的业务的话，代码也全部都有，那么大家课后可以根据这个代码去写一下，去看一下。然后我们在这个 Todo 里面的话，我们再来看一下在 Todo 里面，其实像这个是涉及到分布式规划，我们在下一个阶段会来说，那么这个其实也是。在这里还有一个用户退出登录需要清空购物车，这个清空购物车的话，其实是指的是我们要把一个在 cookie 中的数据去做一个清空，如果说不是我们的一个 cookie 的话，像 Redis 我们不要去清了，因为我们还是要保存在咱们的一个服务器端的，所以我们在这里加一下就是 delete cookie is boss request。


然后这里写一下这是一个foodie，我们直接去把这个对应的一个这个去删掉就可以了，然后我们再来做一个重启，重启之后我们再来做一个退出就可以了。退出主要是用于去看一下我们的一个在前端的一个cookie。好，OK，然后我们刷新一下，现在是购物车有数据，随后我们到前端去做一个退出登录，退出成功以后回到购物车，现在是没有任何的数据。另外在我们的远端，也就是服务端，我们的 shop cut 是有数据的。那么当然如果说用户这个时候他再一次的去做登录的话，那么很明显我们的这个数据还是能够同步过来的，这样子的话我们这一个同步的一个流程我们都已经是 OK 了。

以下是提纲：

