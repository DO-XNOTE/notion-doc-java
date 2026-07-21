---
title: 3-25 【技术改造】电商系统集成Eureka - 商品中心-1 
---

# 3-25 【技术改造】电商系统集成Eureka - 商品中心-1 

[image](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/e94a2a92-47c2-4168-9016-6110ca48a4b4/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466R7IGSJE5%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T225553Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIGhYAiqJDkVJWWbTv0rxXFtOBcjmlSVq%2FNmm2cAtJuJ%2FAiAcTHGbioEX2dcMyn9ckZFWJ7%2F0ZPuD38xtedmDpG3PYyqIBAjG%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMf8B2hv1d78SkIRpeKtwD3800qXFfDCDJpk12SNrel6VN3FVsonf5nTI27Se5WD9WxeTrMaTqYjsubxXMLUH0y%2Bnc7e4q6CwEVOCJHpKCLuZhwxIqZNbvNbpgHngw8AH8SGWAa4dJmr4Bd6imixknIqu%2BOeRoYxC8ExrksNLl5Q4pyiY%2FJMCb21mqBjFbhJlpSeiFkzD8uM%2FT7E8kH1ylKJrA0YRGN84OzveO7Ulb%2BEUegJcpZpQBORxfA6mJncJVVu%2BvSQkfRkvEaFD2Tk6TD4KI14V7NTm%2F%2FlDJDzgBu9ysaK1dFXw6q7UtB0LTF%2BEMC4QbTF3bvNgewwraPGminViRox7DpC7qByAR4LQXugRuGQZkL8CLCbEwSeY4yLu0TMW67DipatCKbqw%2BwOZKZkPwjsgzuA%2FDoyiVR7mWvo4g0otphYVLE8JBo6jBse9M0e9GKFRB1%2FgRg4qydypB4MeZeAqjBkdFtJMcItzUUocNHO5vfKQR5FOi5qU%2BznjyMQdmnm3SB7iPA6aQK99NT2mAXgYzO84lBvcEq%2BG04cYucnXtjoYicK%2BtiXwDkgGFAnIGibURWyI%2BUTy48qKUBMgEucUMDeMptfpk16ukxEnMxkTgy%2B81KaIjCVg9PAWxbJ%2FB3934b%2Ba%2BKYUw3rf%2F0gY6pgETINOL7wCVQfsII4tbb1b6dPWU0pjuMT6yu1SZrlCxUzvBVDBfgNstph9LH7e3csMp8OlQD%2FOWH0bqH8DQYzQfME4T74Tb%2BAoRBSdAJASfp1qmWxZzwmNLWo%2FH1fd%2Bx15x86HcrZCygqkwkVPSbSUilyEcwR5cVoCWoe%2FZ39PGO5U3Lgc6sBl5DtPcQGaulY%2BoffCxwLGrce4QGYHdo4CbtNdFm0D6&X-Amz-Signature=1f46e07778ee1b768b66cc79520286c36a24898f4720c42a1609268510254595&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

[image](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/8de5bf34-0233-4475-9e58-19c66996d970/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466R7IGSJE5%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T225553Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIGhYAiqJDkVJWWbTv0rxXFtOBcjmlSVq%2FNmm2cAtJuJ%2FAiAcTHGbioEX2dcMyn9ckZFWJ7%2F0ZPuD38xtedmDpG3PYyqIBAjG%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMf8B2hv1d78SkIRpeKtwD3800qXFfDCDJpk12SNrel6VN3FVsonf5nTI27Se5WD9WxeTrMaTqYjsubxXMLUH0y%2Bnc7e4q6CwEVOCJHpKCLuZhwxIqZNbvNbpgHngw8AH8SGWAa4dJmr4Bd6imixknIqu%2BOeRoYxC8ExrksNLl5Q4pyiY%2FJMCb21mqBjFbhJlpSeiFkzD8uM%2FT7E8kH1ylKJrA0YRGN84OzveO7Ulb%2BEUegJcpZpQBORxfA6mJncJVVu%2BvSQkfRkvEaFD2Tk6TD4KI14V7NTm%2F%2FlDJDzgBu9ysaK1dFXw6q7UtB0LTF%2BEMC4QbTF3bvNgewwraPGminViRox7DpC7qByAR4LQXugRuGQZkL8CLCbEwSeY4yLu0TMW67DipatCKbqw%2BwOZKZkPwjsgzuA%2FDoyiVR7mWvo4g0otphYVLE8JBo6jBse9M0e9GKFRB1%2FgRg4qydypB4MeZeAqjBkdFtJMcItzUUocNHO5vfKQR5FOi5qU%2BznjyMQdmnm3SB7iPA6aQK99NT2mAXgYzO84lBvcEq%2BG04cYucnXtjoYicK%2BtiXwDkgGFAnIGibURWyI%2BUTy48qKUBMgEucUMDeMptfpk16ukxEnMxkTgy%2B81KaIjCVg9PAWxbJ%2FB3934b%2Ba%2BKYUw3rf%2F0gY6pgETINOL7wCVQfsII4tbb1b6dPWU0pjuMT6yu1SZrlCxUzvBVDBfgNstph9LH7e3csMp8OlQD%2FOWH0bqH8DQYzQfME4T74Tb%2BAoRBSdAJASfp1qmWxZzwmNLWo%2FH1fd%2Bx15x86HcrZCygqkwkVPSbSUilyEcwR5cVoCWoe%2FZ39PGO5U3Lgc6sBl5DtPcQGaulY%2BoffCxwLGrce4QGYHdo4CbtNdFm0D6&X-Amz-Signature=bacc158eb085fbe4a257d0c862ab7969e3a3b117705384ee8d05fac0ba16c944&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

hello 我们课网的各位同学们，大家好，从这一节开始，我们就要牛刀小试，先来改造第一个商城阶段的微服务模块就是商品中心了。

[image](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/225ed3bb-b562-4eee-9c8f-bbf7022dcbdd/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466R7IGSJE5%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T225553Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIGhYAiqJDkVJWWbTv0rxXFtOBcjmlSVq%2FNmm2cAtJuJ%2FAiAcTHGbioEX2dcMyn9ckZFWJ7%2F0ZPuD38xtedmDpG3PYyqIBAjG%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMf8B2hv1d78SkIRpeKtwD3800qXFfDCDJpk12SNrel6VN3FVsonf5nTI27Se5WD9WxeTrMaTqYjsubxXMLUH0y%2Bnc7e4q6CwEVOCJHpKCLuZhwxIqZNbvNbpgHngw8AH8SGWAa4dJmr4Bd6imixknIqu%2BOeRoYxC8ExrksNLl5Q4pyiY%2FJMCb21mqBjFbhJlpSeiFkzD8uM%2FT7E8kH1ylKJrA0YRGN84OzveO7Ulb%2BEUegJcpZpQBORxfA6mJncJVVu%2BvSQkfRkvEaFD2Tk6TD4KI14V7NTm%2F%2FlDJDzgBu9ysaK1dFXw6q7UtB0LTF%2BEMC4QbTF3bvNgewwraPGminViRox7DpC7qByAR4LQXugRuGQZkL8CLCbEwSeY4yLu0TMW67DipatCKbqw%2BwOZKZkPwjsgzuA%2FDoyiVR7mWvo4g0otphYVLE8JBo6jBse9M0e9GKFRB1%2FgRg4qydypB4MeZeAqjBkdFtJMcItzUUocNHO5vfKQR5FOi5qU%2BznjyMQdmnm3SB7iPA6aQK99NT2mAXgYzO84lBvcEq%2BG04cYucnXtjoYicK%2BtiXwDkgGFAnIGibURWyI%2BUTy48qKUBMgEucUMDeMptfpk16ukxEnMxkTgy%2B81KaIjCVg9PAWxbJ%2FB3934b%2Ba%2BKYUw3rf%2F0gY6pgETINOL7wCVQfsII4tbb1b6dPWU0pjuMT6yu1SZrlCxUzvBVDBfgNstph9LH7e3csMp8OlQD%2FOWH0bqH8DQYzQfME4T74Tb%2BAoRBSdAJASfp1qmWxZzwmNLWo%2FH1fd%2Bx15x86HcrZCygqkwkVPSbSUilyEcwR5cVoCWoe%2FZ39PGO5U3Lgc6sBl5DtPcQGaulY%2BoffCxwLGrce4QGYHdo4CbtNdFm0D6&X-Amz-Signature=1cbce3bccbadf96addded7da0f8e4effe6c11466c25250e359b2774e3060c525&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

那这里其实内容很简单，我们就把商品域相关的业务模型服务还有 controller 等等一股脑的把它剥离出来就好了。那通过这一节大家就会领略到微服务改造是多么简单的一件事情。


好，我们 intelligi 开工小伙伴们找到 foodie cloud 当中的这个 domain 文件夹，在这里面，创建商品微服务的一个子文件夹，把它起名叫什么叫item。Ok.然后咱所有商品预相关的紫毛酒都会放到这个文件夹下。那我们从第一个开始创建这第一个模块，同学们能猜到是谁？那当然是从依赖最少的模块开始是哪个模块当然是 pojo 对不对？因为这个 pojo 模块存放的是 DAO 还有一些领域模型，那其他的模块对它都有依赖，所以它是处于相对上游的。那这里我们创建一个门文项目，把它的 artifact 起名叫福迪 item 杠 pojo 好把这个商品域微服务的名称给它嵌在福地泡酒当中。我们点击 next 毛九的名称和前面保持一致。然后这里的文件夹我们把它塞到 domain 然后再下面一层一个斜杠 item 下好准备 321 创建完成。那接下来我们往里面添加一些依赖项。


还有这里依赖项主要是为了支持 DAO 层，因为咱的整个 pojo 模块实际上不需要任何其他的依赖我们只用单纯的引入自己需要的依赖，我们需要哪些依赖呢？很简单，只用两个。第一个，我们引入jarx.persistence ，持久化的 apipersistence 很容易打错这个名字。好，它的 artifact 我们把这里写上是 persistence API 杠 API 那 version 我们这里给定一下，是给 1.0 的版本就可以了。而这里少打了一个 S 我们把它补上。


OK 那接下来去创建第二个 dependency 有的同学们可能会奇怪，为什么老师不打开 enable auto import 呢？因为老师这个电脑太挫了，你打开了 auto import 写几行代码就卡的实在不行了，所以还是喜欢手动的。好对吧。上了年纪的人都喜欢手工的对吧。手工水饺比机器水饺就感觉好吃。
接下来第二个 dependency 是谁啊？是咱的 Harbor net org hibernate hibernatship validation validator okay 它的 artifact 呢 hibernate validator 把它直接 copy 下来。好了，把中间这个点换成横杠。 OK 它这里为什么不用指定version ，因为它这个 version 在前面的 parent palm 的 dependency management 节点当中已经引入进来了。好，那咱这个项目只用到了这两个 


dependency 其他的不用多余引入。同学们在自己的项目中也要保持这样一种好习惯，我项目用到什么依赖，我再引入什么依赖，没用到的依赖，我们不要多余的把它引入进来。


OK pom 写好了，接下来去创建这里面需要用到的类同样的咱的冠名商是什么？把包名打开慕课网， com.imock 点后面跟一个谁呢？跟咱当前领域的模型是 item 好，我们把这个路径给它打上，再后面最后是咱的泡酒文件夹。好，那它的包路径就是 com.imock.item.pojo 那这里面有哪些商品域的对象需要引入进来呢？好，我们这里切换到 foodie DEV 打开 food DEV 当中的这个抛弃模块。好，我们看到这里有这么多 BO VO 还有这些持久化的模型，那我们把商品域的模型给它揪出来。


第一个， items 主商品的领域模型，那当然它是需要的。然后下面的 item comments 商品的评论。严格来说，商品的评论实际上是一个单独的微服务。但是这里我们的拆分力度不涉及这么细。那我们就把这个评论模块和商品域放在了一块儿。 Ok. 接下来商品的主图还有 item param 商品属性以及商品的规格。 Item spec. OK 那这 123455 个对象，我们把它 copy 一下，然后再切换回复地。好，这里把它全部 copy 过来。但是 copy 过来以后，我们有没有需要改动的地方啊？很幸运，没有，那这里只用 copy 就可以了。


接下来我们还有 VO BO 对象对不对？这里再创建一个 package 把谁拿过来呢？把 view 我前面看很多同学在群里讨论这个 view bodo 的划分，其实这就像拆分微服务一样，每个人有不同的观点和看法。那我们在不同的公司，它也有不同的分层的要求。但是大部分情况下，我们通常跟页面交互，不会把这个 do 直接传递，从前到后一次透传回来，这是为什么呢？而是为了屏蔽咱底层数据层的改动对上游的影响。那你数据层添加一个新字段，减少一个新字段。我不希望把这个影响引入到上层依赖或者是前端页面当中，所以这里往往需要 VO BO 这里来进行一个阻隔。


好，那接下来我们看一下咱这个 VO 层需要引入哪些对象切换到福地 DEV 当中。咱把福地 DEV 还是 poto 这个子模块，把它的 VO 这个对象给它打开。这个文件夹下面也有很多类，我们把商品域的给揪出来，非常简单，把 item 开头的给它拿出来就好了。这一个 item component 这还有一个叫 new items wheel 看起来也像商品域，对不对？但是咱先不碰它老师对它另有安排，待会咱会把它划分到其他的领域当中。


那剩下还有一个这个 comment 评论模块，我们也把它给包含进来。这里有个 comment level counts 评论数量。还有一个是谁是 my comment will 把它也给包含进来。那最后我们再把这个 shop card shopping card 一个购物车的一个 VO 对象给它 copy 过来，好切换到 item poseok 那同学们会问了，为什么购物车 shopping card 这个 VO 放到了商品域，而没有放到购物车这个领域当中。其实是因为在商品域的 service 当中有一个跟购物车相关的接口不是那么好拆。所以我就把它留在了商品域。如果严格按照微服的领域划分，这个 shopping card view 理应是放在购物车模块的。但是理想与现实之间我们有时候也要做妥协，为了方便，所以老师这里就演绎了一把理想和现实的平衡，把这个 shopping card VO 加在了商品域的模型当中，追求完美和极致的同学可以尝试手动的把它拆分到购物车模块。


那这些 VO 添加进来以后，同学们可以看到有些类已经标红了。那咱这里走进去，把他们一些依赖项给它改一下就可以了。你看这里的引入的这些类，它的包路径都已经改了。那我们在这边其实应该加上谁，把中间缺失的 item 给它补上就可以了。好，那我们再检查一下其他类有没有标红的情况。 OK 没有，那这里 food item pose 就已经创建完成了。


那接下来我们创建第二个模块是谁呢？谁会引用pojo ，同学们所有模块都会，但是咱挑一个最近的模块是谁，而当然是咱的 mapper 了。所以这里 artifact 是福地杠 item 杠后面跟 matter 好，我们点击 next 把 module name 替换好，然后这个文件夹路径也依然放到 domain 杠 item 点击 finish 好，同样，在它的汤姆文件当中，我们引入自己需要用到的依赖。这里面咱有两个依赖需要用到的。
第一个依赖就是咱前面创建好的谁就是刚刚创建好的那个 portal 对象。好，咱们的 artifact foodie item portal 把它引入进来。这个 version 不要写成一点零点 Snapshot 我们用变量名把它替代掉，是 project.versionok 那第二个依赖是谁也是咱的自己人。那就是前面在 common 包下创建的这个 common 字模块，那它的 artifact 的名称我们这里把它复制过来，少打几行字，他叫福迪杠 cloudcommonok 这两个依赖创建好了，那我们接下来怎么样去把代码给补齐？这里在 Java 文件夹下面创建一个子的文件，叫做 come.imock 再点 itemitem 后边我们再跟上点 mapper 好，这就齐活了。


那这个 mapper 里面我们引入哪些类呢？这时候切换到 foodie dive 当中，我们在 foodie dive 里找到哪个模块呢？找到 mapper 模块，把文件夹依次打开，然后在 mapper 里面把商品域的需要用到的 mapper 都给它揪出来。这里大部分都是以 item 开头的，我们来从第一个开始， item comments 要不要要？那接下来 comments mapper customization 的这一个 mapper 也把它拿到。


第三个 item image mapper item mapper 还有 item mapper custom 剩下两个以 item 开头的，一个是 parameter 还有一个是规格。那这几个 1234567 把这七个人 copy 一下。好， copy 完想把它拐卖到 food cloud 里面走，你我们看到通通都怎么样，标红了对不对？所以这里要对它的 import 和 package 做一点小改动。那它的 package 我们要把它转移到正确的 package 里面。因为咱们把这个名称中间加了一个领域模型微服务模块的名称 item 然后这个 item comments 它的 import 路径也变了。那这里实际上应该是点 item.pojo 我们把它重新引入进来。那如果同学们看到路径正确，但是它的 import 上面还标红，其实可以，在这里重新 ring port 1 把这个按钮点一下就可以了。


OK 那我们依次的检查一下其他的类，这每一个 mapper 它当中都有这样一种情况，就是说咱在里面需要用到的 poture 类，它的路径变掉了，同学们这里可以把它重新引入进来，或者你直接一键重新 ring port ，或者你自己手动的把这个 item 在这些 import 语句当中把它打上都是可以的。那剩下的几个类，我就不一个一个改了。同学们用相同的方式把这上面的 import 路径给更正过来就可以了。
但是在这所有 map 当中，有一个 map 要特别注意一下，就是它 items mapper custom 那哪里要注意呢？同学们看到这里，它调用了两个接口，分别是 search items 还有 search items by third categoryok 那这两个接口我们把它划分到主搜模块，因此需要把它从商品域的接口服务当中剔除掉。我们这里添加一个 todo 叫迁移到 foodie search 模块。 OK 只有这一个变化。 OK 那接下来我们要去移植谁移植 resources 咱要把这些 SQL mapper 同样的给它引入进来。好，这里在 resources 下面创建一个文件夹，这个文件夹同样的也叫 mapper 好，那咱接下来转移到福地 DEV 当中，把前面添加过来的几个 mapper 所对应的 xmail 文件给它拿过来，有哪些呢？一个 item comments mapper comments mapper custom 这两个往后剩下的 item image itemsmapper 还有这下面三个以 items 开头的，总共也是 7 个 mapper 文件，我们把它统统复制一下，再切换回 cloud 把它复制过来。


那这几个文件有很多地方需要改动的同学们看到这里，第一个改动的地方，我挑一个文件来简单说明一下 mapper namespace 这里咱已经把什么把这个 mapper 划分到了商品域。因此这个包路径后面是不是要跟上一个item ，把这个路径更正正确。这是第一点。第二点，这个 resort map 它的类型咱也把这个类移植到了商品域的包路径下，所以这里的路径也要把它更正过来。Ok.一二这两个路径。好，那同学们用这种方式依次把所有的 map 当中的路径都给它更正正确。我再带着大家做一个，然后剩下的大家自己来把它更正一下。


那咱这里有一个简单的方式是什么呢？同学们把这个包路径 com.imock 给它 copy 一下，然后用替换命令 by come.imock 改成 come.imock.item 好，我们点击 replace off 那这里可以看到整个文件夹所有需要更正的路径都已经更正过了。那同学们尝试的去点击这个类，发现下面可以去点进去，那说明路径已经更改正确了。 OK 那大家把剩下的几个类通通改。正好老师这里就不带着手把手做了。
但是这所有类当中有这样一个类，它需要特别注意一下是什么呢？是咱的 itemsmapper custom 这一个文件，因为我们在对应的 Java 类当中，这个 item mapper custom Java 类当中把两个方法注释掉了，这两个方法将移到 food search 模块。因此为了保持一致，咱要到 item mapper custom 当中把这两个方法对应的 SQL query 也给它找出来，把它删除掉。这两 query 在哪呢？是第二个 search items 再往下 search items by third category 好，这两个给它注释掉。 OK 那剩下的路径，我们就按照前面说的方法把它给替上替换好勒。那同学们依次用同样的方法把其他剩下的这几个文件中的路径改正正确。然后咱的这个 map 字模块就已经创建好了。


