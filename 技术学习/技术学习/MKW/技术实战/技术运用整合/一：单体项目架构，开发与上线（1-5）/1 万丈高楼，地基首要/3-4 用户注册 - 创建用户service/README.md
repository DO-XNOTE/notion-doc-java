---
title: 3-4 用户注册 - 创建用户service
---

# 3-4 用户注册 - 创建用户service

[image](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/abf670de-d4aa-4aae-858d-016cf051036f/SCR-20240816-tkjv.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WLNKLBXJ%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T224624Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQC%2FdeiC8S5Kwcx94fRGQHkylk7QsXFFT2Rj4GwdYky6IAIhAPqWZA15wrWqEtPpE4GIKpjmh83TXMZQ5ADSQG2Cr%2FtOKogECMb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1Igx9O%2FJ22W4gCqMiBQoq3AMM8FimB3pT3jUfq%2BM3fBR86kVxeAxCROVtKI58%2FayKubZLyelljulguaWap2VypaV0rmDUcicp0pb%2BWXlObh087UUmCXUvNC2Tk6murSg1hj6CknS3rw8ByQfGp1Per3cP7AETC98GzZbsE6aslSOhfkAU7%2FsUoHq3ZwPwbk8VGcYT8h8qaZS3ElwFKYJOnRixyxzikh0FG155msLB4kTGi2dSF8J63dwGQh6sVquc2ji3xomk2%2FFNIVJ8rC5FXLIxP2PEcHAb9y8GOfamFuOBhBQvM9hdPMyfrxJKCbi4Ng67jtPcrHo4lYaZEeBF%2BjsSynNqoUHHNvCKzID7MVQR4Fa1oSED1s9bEtQQp2h3nZPFov3vLFeLEIZ%2B3WUq2CVrg3w8mKB0ix20Myv30LKMoO9rpH83AVaNPuZdARw%2B1Y%2FS6wtojnVPm3JJg%2B7zmwnN8ahD4H9FD0aQoXZS%2FK5zM9LiCoh70weG96L1iNgSgS2i28HdGOOQZWcGpk6pOOfskyXTE7ELS1p0rUnDZdEBLM3yBI64x8yYPcszJhSjyDB3rhisg1R3X%2BDBRaTM9PgutPq3Kp6Ar8ntogsYQo7pqJmKD2l1AW4tzD07%2F8wpLbN2r5Hce7QMVPKwoDDbt%2F%2FSBjqkAQzANtfmwHuS6PvzQAJFeCTZMa%2FXmMZWvmctgL7J4MUeYkZCZ5zHOfOT2lP%2BzGIgTpvg4vXEM3AZ4%2B0cAN8%2BK1RK3TDLkBMsbNtYthLIl91DGTcAgW5yurket9wH8%2FrLNIlD1vrrUFxZ75vP5VSqEjlAoqX4VOdPUwXr%2FIe%2BrUmMKrwMsqMND7%2B8Et6O%2BBiCKfKC3MAoPtwIHXOkmXNt7iKuQUYU&X-Amz-Signature=0b662d2d3f0e06372991ec544684b974cd817777a74d1a4cc62b5b7568fc7ac5&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

[image](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/f81ac013-20f1-45fe-ab4b-8b11d991bbab/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WLNKLBXJ%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T224624Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQC%2FdeiC8S5Kwcx94fRGQHkylk7QsXFFT2Rj4GwdYky6IAIhAPqWZA15wrWqEtPpE4GIKpjmh83TXMZQ5ADSQG2Cr%2FtOKogECMb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1Igx9O%2FJ22W4gCqMiBQoq3AMM8FimB3pT3jUfq%2BM3fBR86kVxeAxCROVtKI58%2FayKubZLyelljulguaWap2VypaV0rmDUcicp0pb%2BWXlObh087UUmCXUvNC2Tk6murSg1hj6CknS3rw8ByQfGp1Per3cP7AETC98GzZbsE6aslSOhfkAU7%2FsUoHq3ZwPwbk8VGcYT8h8qaZS3ElwFKYJOnRixyxzikh0FG155msLB4kTGi2dSF8J63dwGQh6sVquc2ji3xomk2%2FFNIVJ8rC5FXLIxP2PEcHAb9y8GOfamFuOBhBQvM9hdPMyfrxJKCbi4Ng67jtPcrHo4lYaZEeBF%2BjsSynNqoUHHNvCKzID7MVQR4Fa1oSED1s9bEtQQp2h3nZPFov3vLFeLEIZ%2B3WUq2CVrg3w8mKB0ix20Myv30LKMoO9rpH83AVaNPuZdARw%2B1Y%2FS6wtojnVPm3JJg%2B7zmwnN8ahD4H9FD0aQoXZS%2FK5zM9LiCoh70weG96L1iNgSgS2i28HdGOOQZWcGpk6pOOfskyXTE7ELS1p0rUnDZdEBLM3yBI64x8yYPcszJhSjyDB3rhisg1R3X%2BDBRaTM9PgutPq3Kp6Ar8ntogsYQo7pqJmKD2l1AW4tzD07%2F8wpLbN2r5Hce7QMVPKwoDDbt%2F%2FSBjqkAQzANtfmwHuS6PvzQAJFeCTZMa%2FXmMZWvmctgL7J4MUeYkZCZ5zHOfOT2lP%2BzGIgTpvg4vXEM3AZ4%2B0cAN8%2BK1RK3TDLkBMsbNtYthLIl91DGTcAgW5yurket9wH8%2FrLNIlD1vrrUFxZ75vP5VSqEjlAoqX4VOdPUwXr%2FIe%2BrUmMKrwMsqMND7%2B8Et6O%2BBiCKfKC3MAoPtwIHXOkmXNt7iKuQUYU&X-Amz-Signature=2f07f6f659ac9fe09798e6d6265d1843cd9fb938ff4b98707bc021ede8eb5136&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

在注册里面，我们所使用到的第一个接口API，判断用户名是否存在，其实接口我们就已经是写完了。接下来其实我们应该要去写一下注册的用于去创建用户的一个接口了。好回到我们开发工具还是一样，我们最一开始应该要去编写一下我们的service，我们来到service，我们可以在这里面去写一个方法，写一个public。用户创建完毕以后，在我们是需要去把当前用户我们在返回一下，返回出去定义为users。随后我们创建一个用户，取名为 create user。


我们是需要传入一些相应的内容的，用户要去注册保存到数据库。其实在最一开始我们所需要去使用到的就是用户名和密码，这些内容其实是在我们的前端，在前端里面，在这一块内容，其实它是一张表单，它一个表单提交的时候会把这三个参数用户名，密码以及是确认密码包装到一个 JSON object 传到我们的后端的。传入到后端以后，它其实是属于一种偏向于业务类型的一个数据包，或者是一个 JSON object。这个我们统一的可以把它定义为是一个 b o，也就是 b o 对象。写一下user。


b o。这个主要就是用于去接收前端所传过来的。其实我们可以去这样理解，只要是前端传入到我们后端，用人去接收的一些数据体，不管是 list 还是一些object，其实我们都可以统一的定义为是叉叉XBO，比方在这里是 user b o。以后像购物车有 shopping cart b o，还有是 order b o，统一定的是一个 b o OK。好。针对于这样的一个 b o，我们就需要去创建一下bo，我们是统一的，会放在 polo 这一层。我们在这里直接可以右键去 new 一个package，这样子我们直接来一个 Bo 就可以了。


看一下在 POS 的后方，我们在这里面去创建一个 Java 的class，写一下 user b o OK，创建了。在这里面去填入一些我们在前端所需要去传入过来的一些属性，这个属性我们刚刚其实也说了写一下，第一个是一个 user name，第二个，第二个是password，随后还有就是一个确认密码是 confirm password。好，随后我们再可以去生成一下，生成 get 和set，这样子相应的内容全部都有了。


user 比 o 在我们的 service 就不会再报错了，只要把这个包倒入进来。好，我们把当前为它加一个注释，创建用户。好。随后我们来到它的实现类，在实现类里面我们先把这个方法先实现重写，我们在它的上方加上一个事物。现在其实我们的事物是用于去创建用户的，所以我们在这边就会使用到有快的。OK，你必须要有一个事物，如果出错是可以用去回滚的。好。随后现在我们就可以去把 user b o 里面相应的内容拿出来，放到 losers 里面去，在这边我们可以新创建一个用户，把它给扭一下。随后在 user 这里面，我们就可以去塞入一些相应的值。


首先第一个我们可以 set 一个 user name，这个 user name 是从 user Bo 过来的，所以直接通过 b o 点 get user name 就可以了。随后下一个我们就可以去设置一下它的一个用户名。好，应该是设置一下它的一个password。 set password 从 use a bill 拿过来，可以来点 get password。


这边我们要注意一下，之前其实我们在前面几节课里面说了， password 我们肯定是不可能明文的保存到数据库里面去的，我们是必须要去进行一个加密的，加密主要也是以防万一数据库被黑客攻破，用户的用户名、密码等等信息遭到泄露，所以我们在这边必须要去做一个加密。


关于加密，在 utils 里面，预先我也是引入了一个 m d 5 utils，可以来看一下。在这边我们其实主要的方式是通过 MD5 去进行一个加密。加密完了之后，我们再通过 base 64 进行了一个encode。OK，可以来做一个测试，比方来一个Imock，我们可以右键跑一下。当我们的一个运行完毕以后，这个就是我们的一个加密的最终的一个密文。 OK 好。随后我们就可以来进行一个使用了。在这个地方我们只要通过MD。


You tells the end. Get a. 第5 string 把明文的密码放进去就 OK 了，只不过它会有一个异常，我们可以在这里对它进行一个 try catch，把它给包起来，这样子就 OK 了。好。随后下一个我们 user 用户是需要去设置一个 nickname 用户的昵称。用户的昵称一开始其实是可以默认和我们的 user name 一致，所以我们在这个地方把它给设置进去就可以了。最后下一个我们加一个注释，默认用户昵称。从用户名。下一个我们就应该要去 set 一下，它有一个face，这个就是一个用户的头像，其实和昵称也是一样的，我们是需要去为它设置一个默认的头像的。


通常网站在新用户注册以后，你肯定会有一个头像，如果没有头像显示为空了，所以在这里我提供了一个默认的图，大家也可以根据自己的一个情况去进行一个使用。 URL 地址大家可以保持和我使用的是一致。或者你自己到网上去随便找一个头像也没有问题。作为你自己的一个默认的头像，我们可以在这个上方我们可以来加上一个 public aesthetic，来一个 final user face，我们可以来定一下，把这个地址给贴进来，把它再加上一个string。漏掉了。 user face，由于它是 static final 命名规范，我们需要去把从小写改为大写。在当前的里面，其实我们可以把作为一个 private 也是没有问题的。 user face 我们就直接可以贴到咱们的部位，让它作为一个默认的头像就可以了。好，这是我们的一个头像。随后继续下一个，我们来看一下。下一个 user 点set，我们可以来找一个它的birthday。对于日期，其实我们可以一般来说可以使用为 1900 杠。 01 可以作为我们用户的一个末日生日，因为你没有，所以我们可以使用这样的一个日期。或者可以使用1970，其实也是都可以。很多的一个网站默认都会使用这种方式去做。在这边我们又会涉及到一个时间日期的一个转换。对于这样的一个时间日期的转换类，其实我们也会有。在这里我们也是提供给大家，因为现在我们直接这样子去手输，它仅仅只是一个字符串，所以我们在这里我们可以来看一下，在有 TOS 里面，我们粘贴一下这个类，到时候大家拿到工程以后直接到里面去拿就可以了。这是一个用去处理一些基本的时间预期的OK，怎么去使用？比方我们在直接可以来一个date，有跳，这个是在我们的 imock utils 里面，它有一个方法叫做 string to date，我们只要把放进去就可以了，把 string 会转换成一个 date 类型，OK。这里面是一个string，所以两边的引号是需要去加一下，可以点进去看一下它的一个源码。在这边其实也有传进来一个字符串的日期以后，它是会根据一定的格式去进行转换的，转换就是根据这样的格式去转的。OK。随后我们再回到前面，继续是设置，设置默认的声音，需要加上之后还有 user 点set。还有性别。性别其实我们是一般来说可以给他来一个保密，这边有对吧，在这里面会有注释，注释是性别， 1 是男， 0 是女， 2 是保密。其实我们在这边我们可以比方写一个2，这样子就是保密了。但是我们往往是不推荐直接去写死数据的，所以我们在这里会使用一个枚举。使用枚举我们就可以在这边可以显得更加的公用化了。


我们来创建一个枚举，在这个里面其实也是在 common 工程里面，我们可以去右键先新建一个包package。 come 点 imock 点。这个枚举其实它是一个关键字，所以它不推荐使用关键字。作为我们的一个包名，我们在后方加上一个 s 就可以了，这样子就成功的创建了一个这样的包了。随后在这里面我们再去创建一个 Java class，这个其实就是作为我们的一个枚举的，定义为sex，把 class 改为枚举就行了。在这边加上一个注释，这个注释就表明当前是属于性别媒体。好，我们可以把三项分别都加入进来。首先第一个，我们是可以从 0 一号开始，woman， man 以及是 secret 保密。第一个是0，给它赋一个值为女。下一个我们直接把拷贝，下一个是1，这个是2，难，这是保密。好，这三个我们都已经是有了，有了以后我们要去根据这里面的内容去设置 0 和这个女，其实就类似于可以理解为是一种键值队的存在，其实它们也是属于枚举的属性，我们是需要去定义的。


我们来一个 public final，它是一个Int，使用 Int 去type，第一个是类型，第二个是一个string，我们把它设置为value。OK。好了以后，我们针对于当前这个类，其实我们也是需要去设置一个类似于构造函数的，我们可以来生成一下，使用第一个 contract 就可以去生成了。把这两项全部都选择进去。


OK。对于我们这样子来讲，其实最简单的一个 sex 枚举类，我们就已经是创建好了。随后我们把 sex 直接可以复制，复制到这个部位，通过sex，我们要先把包导进来， sex 点找到默认的 secret 点，使用tap，这个球就是它真正的一个数值为2，直接可以拿到了。这样子我们就可以做到一个通用化。对于这种数据，我们尽量使用枚举来进行操作，这个是默认性别为保密好，OK。随后还有两个，这两个是create，就是创建的时间，也就是注册时间，我们直接可以你有一个 date 就可以了。当然下方还有一个把直接拷贝，这个是 set update，这样子我们的用户就已经是 OK 了。但是还有一个，千万不要忘记，每一个用户其实都是有主线的，我们在这边其实一直都贯穿着。我们要保证我们的一些表的主线 ID 要全局共用化文化，


在我们前期我们也会做到这样的一种全局文化。在后续也会有相应的老师具体的去给大家去说一下里面其中的奥妙。时钟的原理会具体的去是，并且还有其他的方式去生成，它是有多种形式的。在这里我们预先我已经是把这样的一个组件先引入了进来，大家是可以直接去使用的。看一下这个包，我预先是放在了这里。在这里这几个就是用于去生成的。它的原理其实是一个 ID work 原理，由后面的老师具体去跟大家会说一下的。这里面会有一个 s r d，这个 s r d 其实就相当于是一个工具类。展开看一下，这里面会有一个 next shot 以及是next，这个就是我们会使用到的一个相应的 IT 生成器。所有我们在最端要去使用它，我们就需要把 ID 给注入进来了。来一个 provide Sid，定义为Sid，来一个 all to where 的给加进来。


包加入s、r、d。其实我们可以看得出来这个是处于在o、r、g、 n 32 点i、 d worker 包之下。其实就是这三个包的，可以是一个主包或者是一个root。随后会有两个子包， utils 和strategy。这两这个的包我们要想注入到我们这里面去使用。首先这个包其实应该要被我们的容器所扫描到吧，要去扫描到我们应该要把我们的启动类打开，我们启动类找到有一个，这里边我们现在还并没有加它里面有一个包，叫做 component scan，这个包其实它默认会扫描我们 COM 点m，可我们之前就已经是提过了。现在我们又多了一个包，这个包其实就应该要被我们的容器去扫描到吧，所以我们要把这个包我们是需要去进行拷贝的。OK，拷贝一下放到这里边，它有一个属性，我们可以看一下它的源码，它源码里面其实会有一个 base packages 这个东西，并且它其实是一个数组，是一个 string 数组。所以我们可以在这里面放入多个，写一下 base package，写一下我们就可以把加进来。首先一个默认的是 Com 点Imok，这是第一个也是默认的。随后第二个，第二个其实就应该是这个拷贝错了，我们应该要去右键 copy pass，应该是右键拷贝它的一个reference，它的完全限定的一个路径拷贝。再贴过来，


这个包就可以全部都贴过来了。贴过来以后，其实我们的 component scan 在这边就已经是配好。我们在这边也是加上一个注释，扫描所有包以及相关组件包做好配置，这样子我们的启动类就已经是配置好了。好，s，r， d 在我们的 service 里面现在就已经是住进去并且可以用了。我们在创建用户的头部，在一开始我们通过 Sid 点 next short 就可以去获得到一个 ID 了，直接可以来定一下 string user ID，然后把 user ID 丢到这个 user 里面， set 一个 ID 放进去，这样子就可以了。 OK 吧，我们没有去做过保存，其实也可以预先的到这里面去测试一下。我们可以把这里面的一个内方法打开，我们可以去跑一下。一个使用的是next，一个是使用的是 next shot，我们可以右键来运行一下，在控制台里面打印的这样的一个效果。使用 short 短ID，长 ID 是下面。OK。其实我以前也关注过腾讯的天天快报，以及是腾讯新闻，他们的一些新闻的一些文章。它的 ID 其实就是类似这样子的，前面的数值和后面的这一部分总共加起来的位数，它的规则和几乎是差不多的。


OK，好，我们还是恢复注释好。现在接下来就是我们这样的service。基础部分为 user 填充的值就已经示意好了。接下来我们就应该要去做一个保存。保存是通过 user Mapper，点 insert 插入一条用户记录，把 user 往这里面一丢就可以了。随后我们再把 user 给返回出去。返回出去的目的是干嘛？返回出去主要是用于我们要在页面里面显示一些用户的基本信息的。OK，这样其实我们对于用户创建保存用户注册信息的，这样的一个 service 就已经是写完了。

