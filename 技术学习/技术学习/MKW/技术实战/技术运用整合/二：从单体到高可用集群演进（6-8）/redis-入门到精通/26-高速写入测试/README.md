---
title: 26-高速写入测试
---

# 26-高速写入测试

[image](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/e6dc7bf4-4722-48be-bb4c-77eba7696d23/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WSXMVK7B%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T225101Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCg7uykvGizYtLrnxLHY7L6JFPgtAH%2BTzcY0o7J%2BhRUfgIgM3sCRWGxWAC6GbZOv06bIA1czyYVfp96oC%2FHei1ic0wqiAQIxv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDMLkPZckzZM72aZjTyrcA8SOOAhKIgoy%2FOaZs4yotqRfEC4wJiapIsx6EFg6aHet0fIof3q%2BPEkvQG45VPtncYbY0yzs0hooZGY2G9FxlTvF5SCjF%2FlZ2%2B1hw3ViTgmhLixUyEvoUKZ0wQU3WNOt6Gdj6aGWIB1YONSpmx%2FgX7EhQ%2FqZDXkdd53ktuH3ZZxLjT7PQ5%2FHL1Ns124kBVpMpR6LfvfFVXR1wLAS3oiG1emcr8jww%2BYJhKN23pS%2Fy2OSmm2xZrbPuhtEh9Mizq%2FZugftI7r2A4Rvqtgp3yHObzEWA7M3ulcgaG%2BxgM7lB9VEOEfoDYxB3WYvTa6uRVce36Zv1KgiLtMa5OP0TRqlW0%2B01SWMWQxzXsJwhMYVdxkjqvxK0vjSD8gnHQzbIoLWXBFIL02BzOi%2BJrsL%2BDBPiW8u2JxksQk3w9o6P4KVYAYY%2FslTGD3H2UkcM2phErRkKucB%2BHbQ%2BzaIf5SlSBnNn58S6BDzpYiMmWztdVMNbiPMI85kmUgmqRnZFpBrd6rSBce9OBgfmv%2BSfwdZ12MnQsSG7kM3rKOxqKRBH8CxBMMdvCqr%2BGKEfo9tTJMU6l9MGwqozWygfWFqh1gh0TLvW9NzxYVoV5bsVl4d5U9i3FV0kuMMI2jVAovcEaSoMLe4%2F9IGOqUBI9bk%2Fc01sqZZjExerSfOt01lEWhrP9qDJvvrobOlkGQyApa%2F1lf3pV32seYguCso7j5Q2KXYnGFdKIeT%2BSmIvWq5tEGPVoaIkkL6f%2FRhyuFzp2qbk%2FP8PF%2BZXbwbKf86mExx5zNuTpqYw2%2FPjOXr6DEc0x80NIeIpAz516vkZJ81cMs%2BAwNl04qvwfxU%2FcPmetebJJ9GC7y9d5rmvMxwC6jZ5bbV&X-Amz-Signature=aeb453231459a4ce23d672eb9a123b40840f3412a850679e1ee0218d49bb4816&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

[image](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/bbd09d32-5da7-4b46-bb07-65df344474cd/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WSXMVK7B%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T225101Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCg7uykvGizYtLrnxLHY7L6JFPgtAH%2BTzcY0o7J%2BhRUfgIgM3sCRWGxWAC6GbZOv06bIA1czyYVfp96oC%2FHei1ic0wqiAQIxv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDMLkPZckzZM72aZjTyrcA8SOOAhKIgoy%2FOaZs4yotqRfEC4wJiapIsx6EFg6aHet0fIof3q%2BPEkvQG45VPtncYbY0yzs0hooZGY2G9FxlTvF5SCjF%2FlZ2%2B1hw3ViTgmhLixUyEvoUKZ0wQU3WNOt6Gdj6aGWIB1YONSpmx%2FgX7EhQ%2FqZDXkdd53ktuH3ZZxLjT7PQ5%2FHL1Ns124kBVpMpR6LfvfFVXR1wLAS3oiG1emcr8jww%2BYJhKN23pS%2Fy2OSmm2xZrbPuhtEh9Mizq%2FZugftI7r2A4Rvqtgp3yHObzEWA7M3ulcgaG%2BxgM7lB9VEOEfoDYxB3WYvTa6uRVce36Zv1KgiLtMa5OP0TRqlW0%2B01SWMWQxzXsJwhMYVdxkjqvxK0vjSD8gnHQzbIoLWXBFIL02BzOi%2BJrsL%2BDBPiW8u2JxksQk3w9o6P4KVYAYY%2FslTGD3H2UkcM2phErRkKucB%2BHbQ%2BzaIf5SlSBnNn58S6BDzpYiMmWztdVMNbiPMI85kmUgmqRnZFpBrd6rSBce9OBgfmv%2BSfwdZ12MnQsSG7kM3rKOxqKRBH8CxBMMdvCqr%2BGKEfo9tTJMU6l9MGwqozWygfWFqh1gh0TLvW9NzxYVoV5bsVl4d5U9i3FV0kuMMI2jVAovcEaSoMLe4%2F9IGOqUBI9bk%2Fc01sqZZjExerSfOt01lEWhrP9qDJvvrobOlkGQyApa%2F1lf3pV32seYguCso7j5Q2KXYnGFdKIeT%2BSmIvWq5tEGPVoaIkkL6f%2FRhyuFzp2qbk%2FP8PF%2BZXbwbKf86mExx5zNuTpqYw2%2FPjOXr6DEc0x80NIeIpAz516vkZJ81cMs%2BAwNl04qvwfxU%2FcPmetebJJ9GC7y9d5rmvMxwC6jZ5bbV&X-Amz-Signature=9328e23df76496c9898e0ce08b26b731ed8e056de23f5508a0184db8d4ce612f&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

咱们继续看这个微博项目，刚才我们是已经把这个什么呢？把这个微博就是写入到这个数据库，写入到数据库就是旧一点的微博给它写到数据库里面去，新的存在这个 Redis 里面。那么接下来我们看一看用 Redis 的这个写的性能怎么样啊？我们可以来做一个测试，嗯，当然了，我们需要这个 CRN to MySQL 点PIP，我们让它干什么呢？我们让它那个就是自动运行，自动运行。好，那我们来一个那个。 CRN table 杠e，我们来一个定时任务，那么这是之前咱们曾经写过的这个关于，噢，咱们这是学斯芬克斯时写的定时任务，这个是fence，这个规律是这个是分钟，对吧？分钟小时，然后这个是啥玩意儿？先，然后这个是月，这个是周几，对吧？噢，那也就是说最小单位是分钟，分钟，最小单位是分钟，那一分钟肯定不止 1, 000 条微博。


好，那我们这样来写每一分钟执行一下，执行什么呢？ user local PIP binary 下面的 PIPP IP，然后执行user。有点 local 下面的 I T D B I T D O C S 然后 C R O N 微博二 C R O N 点来执行一下，试一试 no job 执行正常。好，我们把这个语句给它拿过来。第一。


来，这是我们的自动入库的这个脚本，我们给他来个定时任务，每分钟执行一下子。好。再然后我们，嗯， CD 到 user logo 下面去。我们要模拟这个 pose 的数据，还得模拟cookie，因此我们看看啊。来test，走。我们把这个头信息给它截下来。把 post 的这个头信息我们给它截下来。 header request、 header cookie，好在这里。所以这一次我们发送的头信息啊。是要带 cookie 过去的，我们用 AB 测试的时候发送的头信息是要带 cookie 过去的，因此我们要设计一下这个 AB a b 的用法，也是 a b，就这么着这么着来用了啊。嗯，比如说杠n，我们说来 50 个并发，然后嗯，杠 c 50 个并发，杠 n 我们让他查个 1, 000 条，比如说 1, 000 条， 1, 000 条，这一次我们不能不是 get 了，我们这一次我们是post， post 还不行，还得，或者还不够，还得有那什么，还得有那个 cookie 信息，也就是头信息，还得里边还得有cookie，所以还得写那个杠 h 选项加上，再然后还不够，还得有那个，说明我们是要 post 啊，还要说明我们是要post。


好，再来加一个 user a 点儿post。嗯，杠 p 好 get so easy，直接 U2O post 它这个是干什么的？杠 p 后边这这这是要干嘛啊？这个没看明白，来测一下，看看一下 A b 的那个说明。 CD user local HDP binary，然后 a B 杠 h 一下，我们看看杠 p put a file。 remember file container data to post 说我需要去 post 数据 remember also to set 杠 t 杠 t 是干什么的，可能还能 type 直接照抄他的还真不对。那就得这么着来操作，这么着来操作还得来一个杠p，然后杠 t 往哪发？往哪发？往那个 i t d p 然后冒号是 1 local host，然后是微 52 下面的 post 点 pap 来试一试。


先试试，试一试能发。发什么内容？发什么内容啊？发什么内容？看看 poster 内容，我们 post 的那个内容在这 to provide headers request or status status 等于什么？问号 status 等于，哈哈， from AB 好了，这个先用一个链接先跑 5 次，先试成功再说啊。


来试一试，看看这个命令可不可以，如果可以，我们就可以批量的来让他测试。 a b command not find 而忘了加一个东西，当前目录下，当前的 b 目录下就是当前的 b 目录下，当前目录下就可以了。好，看看能不能帮我们 post 的数据加 cookie 来传统成功走。唉，好了，成功啊。嗯，然后我们应该得到一个最新的那个from，很可惜很可惜没有status。 S T a T U S 我再发一个，咱们抓一下它的包。S，T，a，T， O S，没问题，这个没错，来看一看怎么回事，怎么能看它的返回值。


这里有提示 logo schedules from a b could not open poster data file 杠 t no such file 杠 t 被理解成什么了啊？来我们看看。他让我加了这个杠t，哦，手嘎。他让我加杠t，后边还得加这玩意儿啊。好了，来，杠t，再加上这个玩意儿，走啊。再然后我们看看刚才的那个杠 p 还要不要加其他的杠 p put file 哈，欧了，来，我们现在再让他测一下，看看能不能帮我们 Pod 的成功，连 cookie 也给我们 Pod 成功。摇摇摇，这是干啥呦？说我不对杠 p 杠 t file containing data to put or remember also to set oh 明白 p 后边是个文件，那这个文件我怎么写它的格式呢？不知道它的格式，这还怪麻烦。 5 for the file 是这么列，杠 sheet 杠 p 是他的这个文件。没错，确实是个文件。那这个文件怎么来写？


pot file connecting data 包含了需要 put 的数据的。我念没错，格式是个啥样的呢？一行一个，还先随便写一个试试。好，那我就 VI temp，然后 post 微博post。我觉得这样来写一行一个试一试，咱们就一个 status 等于 test 好保存走。唉，再来这个杠 t 文件在哪啊？文件在 time 下面的那个微博post。好，再来一试，粘上。走，这次没有发生错误。唉，看一看有木油，有木有？太好了，有，要的就是它，要的就是它。那我现在让他，让这个雨俊把我们哎批量化的来进行，来个 50 个并发，我请求 5, 000 次， 5, 000 次，我们看看它的这个时间上怎么样走，总共是 5, 000 次请求， 5, 000 次请求，我要一刷新。哇塞，很好，都发布成功还不够啊？我们发布了 5, 000 条，我们还得看一看这里。唉呦，这不能是来回希望得控制一下了啊，说不定里边已经有 5, 000 条了，慎重一点。好，现在还没来。没关系，因为我们是设的那个 1 分钟执行一下，我们等一会，然后说有我的信，我看看是不是报错的信。
fatal error？ core to undefined function c o n Redis 在 CRN 这个地方啊。我知道这个错误。


这个错误在那个定时任务的时候也经常见，这个应该请王胜解答比较专业，就是你写了一个命令能正常执行，放到那个那里边，比如说是放那个啊。不是，就是说我刚才用命令行下，我直接调用这个命令是可以执行的，然后我把它放在定时任务里，他就说找不到什么文件或者是这个那个的。对，就是这个，就是因为他那个用定时任务执行的时候，他那个环境变量和我们对不一样造成的，用绝对的啊。行，咱们给他换一下，换成绝对路径 CED 微博 2 iOS 这么多，让我如何是好？好，不用，我就换一个就行了。 VIM 那个 CRON 就这个地方，我用我这个地方我用绝对的就可以了，我就这样用那个 user local 下面的 itpd 下面的 itdoc s 下面的微博 2 下面的lab，再会就 OK 了啊。好，然后我们等着他，一分钟过后看他是不是能帮我们。嗯，好，写入完毕啊。好，数数有多少条 flag 靠的星 from host 表 1, 002 条啊。可以的，那再过一分钟他又会给我们入库 1, 000 条啊。


好，那我们继续来测试这个数据，我感觉一分钟执行一下还是有点慢，要不然让他一次 1, 000 条，还是有点慢。嗯，来检查检查他，再想一想办法啊。林国娜，你说我们可以怎么办？


我觉得我那个蛙有循环可以变一变，就是只要它还有数据，我们就不断的把这个蛙有循环，是吧？把它当成一个内层循环，在不断的循环它，这样应该就可以了啊。


一直循环是一直循环。或者就开一个进程，让他始终跑，永不停啊。让他在后台进程跑，反正这样的话一分钟运行一下确实太慢了啊。发布a，发布就发布在这个地方，就业务上我感觉不是很合适。你这个一次性，是吧？咱突出的是一次性一下批量，咱又不是说追求它的实时性，这个地方看看怎么样让他一下多搞点数据过去啊。


嗯，说的太远了，这一分钟来一下确实是有点慢，当然了，也要实际的过程中，这也不应该是由一个 pip 在那跑后台进程，肯定得有一个专门的程序来跑这个后台进程，咱这个地方谨慎模拟啊。好，那这个地方我们来看看，再来一个，哇，有循环，再来一个哇，有刀了，耳 l l 烂。只要他大于等于 1, 000，咱们再给它包一层循环包一层。只要它大于 1, 000，就是 global 冒号到还是大于 1, 000 的话。好，那我就先产生一个 SQL i 以及内层。有循环，来一起审核一下这个逻辑有没有问题啊。如果大于等于 1, 000，好，走着走，形成一个 SQL i 等于零，一个新的任务开始了啊。那要是这样的话，里边这个就没必要， YO 这个里边这个就没必要了，因为都大于 1, 000 了，对不对啊？这个就没必要了，你就光跑一个 i 就可以了。好， i 加小于等于 1, 000，然后这个 if i 等于 0 是不是也就不必要了？因为只要能来到这个网友里面，那他肯定就有人物了，是吧？
好嘞。 D4D 删掉。粘上来。


把这一行。由 D4D 把这一行我们给它，不妨给它拿到最上面去，连上来。好，整理一下现在的思路啊。这个这一行拿到这来，好，现在来看一下当前的这个思路，就是先判断待入库的是不是大于 1, 000 条，我再动手。要是大于 1, 000 条，我先形成一个基本SQL，再形成 r a 等于0， YY 小 i 加小于等于 1, 000，然后我就啊。不断的泡不出来，取出形成 c 扣， 1, 000 条 c 扣绑定成一个大的 C 1000 条，这个数据绑定成一个大的SQL，然后 Echo OK，执行所有执行完毕了， Echo OK，那如果压根就没走这个while，就直接走了这一步，那你不还 Echo OK 吗？还，还 OK 啊，好，可以啊，没问题。


欧了，来我们看一看。好，这里边已经有 4, 900 多条数据了啊。 4, 900 多条好语法也没有问题。那现在咱们再过来做测试啊，我们这次多发一点。唉呦，这个速度太大了啊，速度太大了啊。速度太大了，我们给他那个改小一点 VIM home 点PIP，把它刚才是为了做测试，我们便于观察，我们把它打印出来了啊。在这个地方我给它打印出来了，现在我们有必要把它去掉了，好保存，走好刷新没了，然后我们再一次的来观察一下，我们观察一下这个post。


VIM post，我们观察一下这个post，就是我们每发送一个页面的话，我们需要读几次Redis，写几次Redis？来咱们看一看，每发送一次post，我们需要读，写一次、写一次，对吧？来，咱们看好了，写一次，写两次，然后写三次，然后删除，也是写操作，四次、五次、六次、六次。我们这一个页面上发一条微博，我们写 Redis 写了 6 次，其中还包含还得有读的操作，因为你有的值，你肯定得先读出来才音科瑞，来我们看一看这个性能。六次啊。


这是第二次 from AB。 second from AB 第二次做测试。然后这一次我们给他，为了看看他的这个效果，我们不妨给他来多发个十多分钟，让他稳定一下。比如说发个各十百、千万、二万条，你看请求二万次的话，那就要写十二万次的东西，写十二万次，写十二万字。
好，写。sorry，我已经走走到别的地方去了。 CD user local i TTP D I T D O C S binary 走唉呦等等，是不是又出错了啊？又给我发了一封信 Malroot 又跟我说啥？OK，你跟我说什么呀？是谁跟我说好了，咱们测他个二万次啊？2万次走，这回来二万次 ah ha ha。速度还是受到影响。这个影响未必是 Redis 的。影响是在这个 ITDP 系的 ITDP 的这个连接上啊。


因为是在虚拟机中，然后装的这个阿帕奇效率不是很乐观，你看发完了来我们看一看从哪看时间。哎，我请求了2万次，按照刚才我们统计，平均每一次写一条微博，发一条微博就要写一次Redis， 6 次 Redis 总共是花了 30 秒。 30 除 22, 000 除以 3 一秒钟是写 600 条微博。 6636 就是相当于一秒钟写了是 3, 600 次。 3, 600 次。注意， 3, 600 次绝对不是 Redis 的这个极限啊。


绝对不是 Redis 的极限，是谁的极限呢？是因为受到我们这个阿帕奇这个性能，我们并没有给它做任何优化。我们我的这台虚拟机上是我本地的测试机，并没有给它做任何优化。之前我们做 NGX 的时候被优化到每秒 1, 500 次。那么我们这个 Redis 每秒之前是写，是可以达到是3万次的，3万次就是在那个，嗯纸册 Redis 的它的写瓶颈的情况下是能达到3万次，也就是说其实这个写入速度根本没有受到 Redis 的限制，其实受到的限制还是在于我们的这个阿帕奇上。但即便如此的话，平均每秒钟是写 600 次， 600 次，准确的说是每秒发 600 条微博，那就是产生了 3, 600 次写入， 3, 600 次写入啊。这 24, 000 千多已经在这了。很好，2万条已经过来了。
from post 那三五，这，这是我们最新发布的啊。


好，我把 test 2 的这个数据我给他清一下。 task 2C user local ITP，这样不用太快了，换一个用户，换个太子，换一个用户。 test 21 幺 1 幺 login 现在我没有关注任何人，我去关注一下燕十八。关注他了之后，我来到自己的主页来，我们数一数这个速度为什么效率为什么这么低？这地方肯定有问题。


一12345，这怎么会取出来这么多呢？按照我们正常的设计，它这个顶多能取多少条来着？一个人用户里边顶不是顶多取他总的来说，比如说他有 1, 000 个追星，他追了 1, 000 个星，总的来说能取出 1, 000 条来，这没问题。但是如果你好久没登录了，取某一个具体的这个，你的那个粉丝偶像的话，只能顶多取出来 20 个才对，所以这地方有问题，只能取出来 20 个才对的。


我们来看一看问题出在哪？业务逻辑哪出了问题？ CD user local CD 微博2。好，再把问这个问题给它解决掉，再把这个问题给它解决掉，我们来到这个 home 里面去看一看霍姆里 last pole，你到哪去拉的这个数据？拉取的这个数据获取关注的人，然后拉取 then run 你 by score，你以前从来没有 star poster。好，我们去找 star post 有问题， VIM post 就在这看看这个 star post str post u 的 ID 好，如果大于 20 我们干什么？


the RIM range by rank。
那有必要测试一下咱们这个语句了。这说明这个语句根本就没把它正常的删掉，没把它正常删掉。这个语句有问题来测试一下。我们测试一个有序集合。


刚才那个游戏集合有问题， user local redis binary redis CLI 进来，我 SELECT 1 作词， SELECT 1 在一里边做测试，然后我那个 ZAZ either z either ZI 的谁，我随便定一个，比如说就叫个news。或者是学生 175 身高175，李四身高180，王五身高190，赵六照 6AT 3 没问题 z RAM。 z 瑞姆软件 by rank STU 我要删除第0名到第0名 z 瑞姆 running by rank 删掉一个没问题，然后 z either。 z range still 0- 1，然后 0- 1，然后是那个 with score。你看 175 删掉了，没有问题。唉，那详细的细，再来细细的检查他一下。那这个代码大家已经过亲测，是能够删掉最旧的那一行微博的。但是在 pot 里面，似乎我们要只要保留 20 个他没有给我们搞成功，来 z 瑞姆 range by rank 没有问题。


然后 STR pose 的是不是？冒号这里有吗？你看多混蛋，看到没有？这个键错了，键错了，它永远都是0，对吧？取出来的那个数永远都是0，因为没有这个键，它取出来的值肯定永远都是 0 了，圆轴 0 它永远也算不上了啊。这地方又少了个冒号，这个冒号这个错误发生第三次了啊。好勒，保存，把它保存下来。


好的，下来我重新操作它一下，我给它删一删 z trim 删一下，删那个谁？删那个13，删那个star。冒号叫什么来着？ star 记性怎么这么差呢？叫 start post u 的 i user ID 哎，我给你粘过来啊。好，我们刚才因为少了一个这冒号，导致这个 k 它就不对了啊。不对，所以他没有删除成功，那现在我们手工的给他删一下，那就是这样， z either 手工清除一下，嗯， z trim。 star poster 冒号 user ID，冒号一燕 18 所发的那个账号，所发的第0个到第 19 个。z。
游戏集合 they 挨着 they RIM they RIM。
they run in this car。


那 run 你我要删或者说保留。累润。
算了，直接删掉你 delete star post 冒号 user ID 冒号一好了，删掉这个键。
delete my receive 冒号 user ID 冒号一。
receive。


把数据清一清，重来再来做一个测试。
叫 last Pope last Pope latest。 last pool user ID 不是这个 receive post delete receive poster 冒号一 user ID 冒号 123 咦，这记性怎么这么差？这边打开，那边忘 home IP 好，我们把每个人中心的那个 1, 000 条微博也给他删了，也要给他删了。 receive post 没问题。delete。receive。case， receive 星好，找到了。 delete receive post 冒号 e 嗯，删掉好了，那都让他们这个主页都给他们恢复成空啊。恢复成功。
好了，现在再一次的做这个测试，我们就是说我这个已经发了一万多条了，但是你很久没登录，你也只是收前 20 条，我们再过来做一次测试，好，再来做测试啊。就是他这是第三次测试， third 好，又是往里边写2万请求2万次总的写总的，这个 Redis 写入过程持续得 12 万次，持续 12 万次 CD user local i t d p b 好，持续 12 万字写入啊。这是我的微博，我也来发一条。
好，没经过优化的情况下， 50 个并发，这个阿帕奇就不太能顶得住。


这是我获取的这个微博，然后我已经发了我这个地方我已经发了2万条，这里边已经已经有 4 万多条了，四万多条了，这四万多条。我要是很久没登录，我是一个关注，我关注了刚才那个发微博的账号，我来刷新一下。咦，这么气人啊？这个地方应该是只得到 20 条才对的啊。只得到 20 条，谢谢啊。


一起来观察一下，一起观察 VIM post 点 PIP 观察观察到底咋回事。来把自己发到微博，维护到一个有序集合里都不满足20，明白写了 50 多个，是吧啊？一瞬间写了 50 多个。写了50，那咱这个他是，他不可能太离谱，应该是，那要照你这个思路，就是他只要有订单，嗯。然后 22: 1 这样，然后都不满足他们跳过去了，然后接着再有两个类似的，然后超过。噢噢，那这样好办啊，想测这个原因。好办，我先把他们粉丝的那 20 个给拿掉，那个给清空数据给清空，再开一个来回。切太麻烦，我先把他粉丝来 CD user local redis binary redis COI。 case receive receive receive 冒号 receive 星冒号 case Ray sale。


来 r e c i v e 行好了，我先把这个 3 号用户他的你看 z card receive post 冒号 3 wrong value z color receive。冒号3。 error the against the key 固定一个 wrong card or value z card。


z 软件 receive poster 冒号 3 然后 with scarce with course z range z 自己卡着 k 返回原组轴数量 z card receive poster 冒号 3 怎么回事？这是 error operation against receive sorry 它是一个链表，不是有序集合，它是一个链表。 l range z receive 冒号 poster 冒号 3 到底是个什么类型？ receive post 这么简，是个list。


l 软件 l range？是啊， l range，而且它是个链表类型。 l range 好， 0- 10- 1 l range 你看取出来了是 1, 000 个，这和你说的那个猜想就不大一致，对吧？不大一致，那我们先把这 1, 000 个我先给他清了，是吧？我先给它清了。给它清空。 ill dream，我给他清了，清 receive post。


冒号 3 啊。现在把它清了之后，我这个地方，我把那个并发搞小一点。行，我把并发搞小一点，然后请求 1, 000 次试试现在的结果。比如说我就两个兵法够小了，请求 1, 000 次。 user local i TTP binary a b 行，这次请求 1, 000 次，刚才我已经清空了，对吧？然后这个 1, 000 次，我们来看看啊。你要是 TAT2 来刷新，那又得到了 1, 000 条的这个样子，这个就显然有问题了，唉，再来看就是说你这个 Redis 里面到底是存了多少条现在有问题？就这个 star post 里面。


case star post 我看看到底怎么回事啊？就是他发的，是吧？就是他，然后看它的类型， type star post 冒号 user ID 冒号一就是 1 号还是 z set 好 z card star poster，冒号 user ID 冒号一 2 万多了都，这压根就没删除成功是吧？都 2 万多了，这太离谱了啊，怪不得我们那个速度那么慢啊， 2 万多条拖住了。好，来来来，我们再看 VIM post。


这，那业务逻辑肯定要是有问题，肯定就是在这句话有问题了，无非是核对一下。 K1 不一致来 supports 冒号， user ID 没问题，然后 subpost user ID 冒号没问题，大于20，业务逻辑就在这有了一点点问题，因为我们第一次的时候没加冒号，导致 k 出错，所以有2万条没删掉。


现在问题就在这上，大家想一想为什么？你看现在，比如说里边是 20, 001 条，对吧？ 20, 001 条你又新增一条，是不是 20, 002 条了？ 20, 002 条，它不大于20。不成立吗？成立就成立呗，我把你删掉最尾巴上的那一条，你不还是又 20, 001 条吗？所以我们一开始的时候不是出过一次错误吗？就因为那次错误导致的就是里边那2万条脑积水始终就没排出来，所以我们现在怎么办呢？我们给他手工的，给他初始化一下，手工给它初始化一下就可以了。


好，那把它给清一下，把它清一下。直接delete，直接 delete 的来给。清掉，他这 2 万多条，一下给他删了，删了之后当然这个数据还在，我们把数据在各自都给它初始化一遍，该删的都给它删掉，都先清一清，每个人接收的请一下。好，直接找 kiss 叫做麦。叫做什么来着？姓麦。好， my post。不是，这个是叫 receive 之类的。 receive 清好，我们把个人接收的东西再给他删一下，再给他删一删。 l 软件 receive post 冒号 110 清了 ill trim 删了， 3 号的也给删了。


好了，来再次刷新初始化一下，现在这个人取得的东西是空的了啊。然后再来这里他个人取得的这个也是空的，然后他刚才发布的所有的这个微博也都给他清掉了，也都给他清掉了。也就是那 20 个缓冲区也给它清掉了，所以再做一次测试，我们看看能不能满足啊。就是我要给他。


发2万条微博，一个是观察它的速度，一个是观察后来这个人是不是只取前 20 条，取前 20 条就是对的啊。好，再来意思 test 一下，这个问题还真顽固，真怪有意思。来来来，来来来，今天整一整他case。 case 谁？我们刚才那个剑是叫 case star，来找 z card star pose 冒号 user ID 冒号一。这什么情况？


华区又是 2 万多条，这没有道理呀。又是 2 万多条，那一下取 2 万多条，那谁受得了啊？这个问题到底出在哪？是二万零一条。噢，这样，我先看看我们这个删一条，他删一条就是每次超过 20 的时候你再发，他就删那么一条，到底这一个语句行不行？唉，我再发一个，如果还是二万零一，就说明这个语句是行的，对吧？语句是行，那确实就可能是，那我们就猜测就应该是在这个并发上的时候出了问题了，再发一个来看看，这里 20, 002，这说明这个语句就没起什么作用嘛？好，那病根找到了啊。唉，这就好办了，生这个混蛋语句，什么破玩意儿？这个语句 z cut。仔细对比。 dollar user ID 大于20。然后这个语句，唉，这样啊，我看看啊。就这三行代码之内就有问题，我们就要来调试它，走，yeah。
post。


来，再保存，再测试看到底是谁的原因？走好，原因出现了啊。这就说明这个 icon s s 你看都没有 Echo 出来，就说明这个 if 语句压根就没走好。那问题越来越近了，离答案越来越近了。那好办，那好办，我把它复制下来，看到底是谁，什么症状啊。这个症状还真怪隐蔽。呵呵，我看出来了。


仔细看， ZI 的是一个，在这里是 PIP 的一个函数，传一个 k 做参数，对吧？传一个 k 做参数，返回值跟 20 比较，但是你看看我们把 20 写哪去了，是吧？呵呵，这错误挺气人的，这就相当于拿这个字符串和 20 比较，返回的是一个布尔值false，也就是 0 做当 0 处理，也就是他去找 z 卡的 0 去了哈。那当然永远不成立了，这怪不得在这里出了问题。 Echo 来再试，再保存，然后再发。好 SA 要的就是它，就是它啊。然后我们再一次的初始化一下环境，我们把该删的删一删，好。 l trim receive post 冒号一 103 了 3 三了，然后 delete star poster 冒号 user ID 冒号一神调冒号 3 删掉冒号 2 删掉走好了，这一次把问题终于给他找到了。好，那因此这个 IQS 我就可以把它删了来再次保存，再次测试那2万条数据主页 altrim receive post 0 个没问题， receive poster receive post 0 个没问题。


它的数据综合而来的为什么还没有清掉好 case 2 的清掉了， case raise 又变成 revise 了。 receive post 冒号一走。对了，删掉它，删掉它。 io trim receive post 冒号 110 OK，receive。这次没错。


3 receive 好了再来刷新 case receive 轻信了还打不对它 l trim re C5 post 冒号 1103 再来刷新好了，先来看这个人，主页收到的这个东西都给它清空了，然后我们再看看那个。明星发布的，也就是你粉主发布的那些东西里边还有没有内容也是空的？好，都是空的，现在又初始化了一遍，现在我们操作继续来再做一次测试，还是 50 个并发，然后2万个请求，总共是对于 Redis 来说是写了 12 万次，写了 12 万字，这次我们应该只看到 20 条才应该。唉，好了，速度还不赖呢。刚才速度之所以慢，是因为我们一下子取了多少条？一下子取了两三万条，所以那个速度慢。huh，现在是 20 条吗？我怎么感觉又变多了呢？


来看，一二三四五六七八九十一二三四五六七八九十，已经 20 个了，这严重超过 20 了，目测已经超过。好，但是没关系，我们看一看这次它的那个长度。 20 个没问题， 20 个，所以我们来到这个TAT2，他粉了燕十八，得到是 20 个，没问题，得到 20 个没问题，他得到 20 个没问题。但为什么我本人的主页得到了超过了 20 条呢？好，再把这个小问题再给它解决掉。这是神马情况啊？


那里边只有 20 条任你拉取，也只有 20 条任你拉取。只有 20 条？好，没问题啊。我们看一看。 receive poster 这导致的。保持个人主页 receive post 这个地方咱是 1, 000 条，那这就是对的，因为你很久没有登录了，那一次取是取 20 条啊。如果你一直保持在刷新状态，它就一直接到 1, 000 条，那这样的话咱们的这个测试就是成功的。这个地方最多 1, 000 条，但是你说这个地方还是不太好， 1, 000 条我感觉还是挺夸张的。干什么呢啊？我想让他加一个分页功能，可不可以加一个分页功能啊？比如说我每页我就显示 10 条，这个功能也很简单啊。但是我们首先来分析一下，就是我们的这个功能，目前所做的这个功能，来回头看一看我们的数据库里已经有多少条了？已经有 8 万多条。那么可以看得到，在 50 个并发2万次请求的情况下， Redis 撑起来还是一点问题，没什么压力的啊。每秒是来看一看啊。


一共是 30 多秒， 30 多秒2万条微博，一平均是一秒是发660，将近 700 条微博，每秒 700 条啊。在一个虚拟机下，这个速度还是不错的。平均写是每秒是写了 6742 四千多次， Redis 每秒写四千多次，没有感到压力啊。你要是用 MySQL 的话，每秒写这个次数，那已经早已顶不住了，然后 MySQL 也并没有感觉到压力。为什么呢？因为我们是批量的，一千次、一千条、一千条集中往 market 库里面写，所以我们这一会增加了 8 万多条，没什么压力，也没什么压力。


那这就是我们用这个Redis，嗯，加这个 MySQL 来完成这个热数据的这个写入，热数据写在 Redis 里面，冷数据写在这个 MySQL 里面啊。那么接下来咱们还要再给它完善一点，我们再给它加一个分页功能，比如说我们再给它加一个分页功能，嗯，加个分页。好，那咱们休息一会再来给它加分页功能啊。

