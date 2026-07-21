---
title: 2-18 【Demo】借助死信队列实现异常处理
---

# 2-18 【Demo】借助死信队列实现异常处理

[image](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/f490ee3a-48fe-4d2d-b1fd-4ffaa30da968/SCR-20240722-dtxs.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZDCMLPE6%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T225821Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIAuL5j%2B5sGETVVGhZYXp1Qg37ZEzIAk2olvya30978vlAiBlYzkh8MOLI%2Blv2X%2BQ7yWE0pfAVUTVABMJ7lhokrdQkiqIBAjG%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMoeI8rTQbomCw0YuQKtwDOBEU5MouoJ5Pos3WCpF3APnsi%2B5qRUZI%2BX7y6txZGOGbFDNlYu8uIlgpsHXaSOYQu5X9CYGTLFOxV3k8OSSyTFQ77oBAkMOKRC9c8FxXwwYHy4QYhpN%2Bhf9diFNIp61Rtm7IrRBIQ%2F6RdFRJ5snJfbjNfVzI7us1daPDJrRjA%2F8pf5pS%2BzH2Yc%2FT1u1NNylJYNSjoama2GFo%2B0uFUmzgaBDzyclylsYtP1a8xsHZI0F0e8VptVm3LTf%2FLFZR2pS7JDuGIaixyZbwqtLhHliOU1d9I8zveWA6VbFV%2FfQbeckDEh5Mj15Dio25UBCJ22dpyLmsF6q49S5u4ccNahWr9L1A%2F5fTIJ73zXf%2Fp7uQF43nYx6M0Bo8ZcnUFATp9n9XUkKrtYCQNzxVGid3xx%2B44QXPxDX1I1eNHRbzdAErutRQ%2FEgsvVc3dH8HsW1hG1iL9CR%2BqcAl5%2BT2XWuFxcAfbb1K%2F19XYINTsiZyuZu%2FEXa6k26Pf0l9ykMzcDzNhTMCIsaaxqhMi%2FuRMCPlf7TAhVchlBYWvwC3BX5cXTsPLg4b%2B6lU9L6LFhO5Fp4cBQdrNkI8h%2FWTNVkC3r%2BhO17BrP8YwsdU0FfWlnA%2BPtU4fsu%2Bu%2FZyn%2FlXDKmaFOswy7f%2F0gY6pgEs3tL7eHPNumeqFTBrJzf4EaAauAoTXDDz56K9eXTDznRAINj2evyogo7sDnbcPbDRwHZ7INrl0cme1f1o3SQ8sb9%2FwjNlDCilJAE34%2Ba%2FKxDN1IQYWo0tsh%2BgkF7fLPLpu%2F%2FN8V1jl7xLiPEFCV%2FB%2BhjEYEi%2Bnl%2BjA5zf0Qk3bQwAZqHSxsoqcMkfCO%2Bb19CiZLKYjBjPAmxFdkgTLP0lyIWDKkIn&X-Amz-Signature=a10b67065609112f675df8979a4cb8576c8eeb003ed0ed9ef6bb6ac5e590f502&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

[image](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/bc2b5e10-f92b-455d-8469-557a9c2a87f0/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZDCMLPE6%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T225821Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIAuL5j%2B5sGETVVGhZYXp1Qg37ZEzIAk2olvya30978vlAiBlYzkh8MOLI%2Blv2X%2BQ7yWE0pfAVUTVABMJ7lhokrdQkiqIBAjG%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMoeI8rTQbomCw0YuQKtwDOBEU5MouoJ5Pos3WCpF3APnsi%2B5qRUZI%2BX7y6txZGOGbFDNlYu8uIlgpsHXaSOYQu5X9CYGTLFOxV3k8OSSyTFQ77oBAkMOKRC9c8FxXwwYHy4QYhpN%2Bhf9diFNIp61Rtm7IrRBIQ%2F6RdFRJ5snJfbjNfVzI7us1daPDJrRjA%2F8pf5pS%2BzH2Yc%2FT1u1NNylJYNSjoama2GFo%2B0uFUmzgaBDzyclylsYtP1a8xsHZI0F0e8VptVm3LTf%2FLFZR2pS7JDuGIaixyZbwqtLhHliOU1d9I8zveWA6VbFV%2FfQbeckDEh5Mj15Dio25UBCJ22dpyLmsF6q49S5u4ccNahWr9L1A%2F5fTIJ73zXf%2Fp7uQF43nYx6M0Bo8ZcnUFATp9n9XUkKrtYCQNzxVGid3xx%2B44QXPxDX1I1eNHRbzdAErutRQ%2FEgsvVc3dH8HsW1hG1iL9CR%2BqcAl5%2BT2XWuFxcAfbb1K%2F19XYINTsiZyuZu%2FEXa6k26Pf0l9ykMzcDzNhTMCIsaaxqhMi%2FuRMCPlf7TAhVchlBYWvwC3BX5cXTsPLg4b%2B6lU9L6LFhO5Fp4cBQdrNkI8h%2FWTNVkC3r%2BhO17BrP8YwsdU0FfWlnA%2BPtU4fsu%2Bu%2FZyn%2FlXDKmaFOswy7f%2F0gY6pgEs3tL7eHPNumeqFTBrJzf4EaAauAoTXDDz56K9eXTDznRAINj2evyogo7sDnbcPbDRwHZ7INrl0cme1f1o3SQ8sb9%2FwjNlDCilJAE34%2Ba%2FKxDN1IQYWo0tsh%2BgkF7fLPLpu%2F%2FN8V1jl7xLiPEFCV%2FB%2BhjEYEi%2Bnl%2BjA5zf0Qk3bQwAZqHSxsoqcMkfCO%2Bb19CiZLKYjBjPAmxFdkgTLP0lyIWDKkIn&X-Amz-Signature=acceedb7d08391021f009ae54d474d78aa26c9b155be43b027fa474a5316d0f3&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

[image](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/a16aa753-b7a7-461e-b0fa-332e0f419bf7/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZDCMLPE6%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T225821Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIAuL5j%2B5sGETVVGhZYXp1Qg37ZEzIAk2olvya30978vlAiBlYzkh8MOLI%2Blv2X%2BQ7yWE0pfAVUTVABMJ7lhokrdQkiqIBAjG%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMoeI8rTQbomCw0YuQKtwDOBEU5MouoJ5Pos3WCpF3APnsi%2B5qRUZI%2BX7y6txZGOGbFDNlYu8uIlgpsHXaSOYQu5X9CYGTLFOxV3k8OSSyTFQ77oBAkMOKRC9c8FxXwwYHy4QYhpN%2Bhf9diFNIp61Rtm7IrRBIQ%2F6RdFRJ5snJfbjNfVzI7us1daPDJrRjA%2F8pf5pS%2BzH2Yc%2FT1u1NNylJYNSjoama2GFo%2B0uFUmzgaBDzyclylsYtP1a8xsHZI0F0e8VptVm3LTf%2FLFZR2pS7JDuGIaixyZbwqtLhHliOU1d9I8zveWA6VbFV%2FfQbeckDEh5Mj15Dio25UBCJ22dpyLmsF6q49S5u4ccNahWr9L1A%2F5fTIJ73zXf%2Fp7uQF43nYx6M0Bo8ZcnUFATp9n9XUkKrtYCQNzxVGid3xx%2B44QXPxDX1I1eNHRbzdAErutRQ%2FEgsvVc3dH8HsW1hG1iL9CR%2BqcAl5%2BT2XWuFxcAfbb1K%2F19XYINTsiZyuZu%2FEXa6k26Pf0l9ykMzcDzNhTMCIsaaxqhMi%2FuRMCPlf7TAhVchlBYWvwC3BX5cXTsPLg4b%2B6lU9L6LFhO5Fp4cBQdrNkI8h%2FWTNVkC3r%2BhO17BrP8YwsdU0FfWlnA%2BPtU4fsu%2Bu%2FZyn%2FlXDKmaFOswy7f%2F0gY6pgEs3tL7eHPNumeqFTBrJzf4EaAauAoTXDDz56K9eXTDznRAINj2evyogo7sDnbcPbDRwHZ7INrl0cme1f1o3SQ8sb9%2FwjNlDCilJAE34%2Ba%2FKxDN1IQYWo0tsh%2BgkF7fLPLpu%2F%2FN8V1jl7xLiPEFCV%2FB%2BhjEYEi%2Bnl%2BjA5zf0Qk3bQwAZqHSxsoqcMkfCO%2Bb19CiZLKYjBjPAmxFdkgTLP0lyIWDKkIn&X-Amz-Signature=159af3ebedb8101107502d78f7546a72f2c16becd2652f382f0fd309f09c3c44&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

[image](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/5c11fa8d-024f-441c-8d7e-f7ec92b7cc95/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZDCMLPE6%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T225821Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIAuL5j%2B5sGETVVGhZYXp1Qg37ZEzIAk2olvya30978vlAiBlYzkh8MOLI%2Blv2X%2BQ7yWE0pfAVUTVABMJ7lhokrdQkiqIBAjG%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMoeI8rTQbomCw0YuQKtwDOBEU5MouoJ5Pos3WCpF3APnsi%2B5qRUZI%2BX7y6txZGOGbFDNlYu8uIlgpsHXaSOYQu5X9CYGTLFOxV3k8OSSyTFQ77oBAkMOKRC9c8FxXwwYHy4QYhpN%2Bhf9diFNIp61Rtm7IrRBIQ%2F6RdFRJ5snJfbjNfVzI7us1daPDJrRjA%2F8pf5pS%2BzH2Yc%2FT1u1NNylJYNSjoama2GFo%2B0uFUmzgaBDzyclylsYtP1a8xsHZI0F0e8VptVm3LTf%2FLFZR2pS7JDuGIaixyZbwqtLhHliOU1d9I8zveWA6VbFV%2FfQbeckDEh5Mj15Dio25UBCJ22dpyLmsF6q49S5u4ccNahWr9L1A%2F5fTIJ73zXf%2Fp7uQF43nYx6M0Bo8ZcnUFATp9n9XUkKrtYCQNzxVGid3xx%2B44QXPxDX1I1eNHRbzdAErutRQ%2FEgsvVc3dH8HsW1hG1iL9CR%2BqcAl5%2BT2XWuFxcAfbb1K%2F19XYINTsiZyuZu%2FEXa6k26Pf0l9ykMzcDzNhTMCIsaaxqhMi%2FuRMCPlf7TAhVchlBYWvwC3BX5cXTsPLg4b%2B6lU9L6LFhO5Fp4cBQdrNkI8h%2FWTNVkC3r%2BhO17BrP8YwsdU0FfWlnA%2BPtU4fsu%2Bu%2FZyn%2FlXDKmaFOswy7f%2F0gY6pgEs3tL7eHPNumeqFTBrJzf4EaAauAoTXDDz56K9eXTDznRAINj2evyogo7sDnbcPbDRwHZ7INrl0cme1f1o3SQ8sb9%2FwjNlDCilJAE34%2Ba%2FKxDN1IQYWo0tsh%2BgkF7fLPLpu%2F%2FN8V1jl7xLiPEFCV%2FB%2BhjEYEi%2Bnl%2BjA5zf0Qk3bQwAZqHSxsoqcMkfCO%2Bb19CiZLKYjBjPAmxFdkgTLP0lyIWDKkIn&X-Amz-Signature=c6a7c79502a3b91495b9546f90ccbc2b851b42680cfd0e42993b1212fa09722d&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

hello 慕课网的各位同学们，大家好，在这一节当中，老师带大家一起去搭建一个死信队列的程序，处理咱 consumer 抛出的异常。那咱来看一下本节的主要内容都有哪些。第一步，我们要先安装两个插件，就是使用像 delay Q 里面一样的方式，通过 rabbit MQ 的 plugins 指令开启 rabmq 插件。这里不同之处是这两个插件应该是已经内置好的，我们只用把功能开启就好了，并不需要去页面上下载。如果同学们本地的 rabmq 版本过低，无法安装这些插件。那老师建议大家去网上下载一个最新版本插件。


安装好了以后，咱就进入了代码环节，这个环节和前面几节的内容是一样的，我们创建一个 producer 和 consumer 然后在配置文件当中引入新的配置项，将死信队列的功能开启。接下来我们把应用启动起来，让生产者在 rabmq 中创建好死信队列。然后我们登录 rabmq 的管理界面，看一看这个死信队列长什么样子。最后一步，我们就要去测试死信队列了。这个测试环节包含两个用例，第一个测试用例是去看一下 consumer 会不会在重试的阈值达到预定值以后，把这条消息添加到死信队列当中。


第二个测试用例，咱尝试在 rabmq 的管理界面中把死信队列中的消息移回到正常的队列当中，让他进行重新的消费。 OK 同学们，大家准备好的话跟我抄起家伙，咱 intelligi 开拔编程，使我快乐，996是我的福报。我们接下来再给 stream 的 topic 里面添加一个新成员，这是倒数第二个新成员了，咱后面还有一个就快要走到尽头了。好，我们复制任意一个 topic 把它粘贴过来，同时给它改名字叫谁呢？叫 dlqdlq 是什么意思啊？ dad letter Q 死信队列的意思 LQ OK 那剩下的流程大家非常熟悉了，咱把 delay 的 consumer 都给它改成 dlq consumer 起两个不同的名字。同理下面改成 dlq producer 这两个信道，创建完了以后，咱就可以转站到 controller 里面。好，我们在 controller 里第一步是什么，先把刚才创建的 topic 引入进来，它叫 dlq topic 然后变量的名称就叫 dlq topic producerokay 那往下滚滚到最下面以后呢，咱 copy 上一个方法，把它复制粘贴一下。 stream 这一张，不用抄别人的作业，只用抄自己的作业。这挺好的，注释里面给它写上死信队列测试死信队列。 OK 那咱从上往下开始一点点改。 post mapping 这里我们把它改成 dlq 然后方法名是 send message to UD LQ 其实理论上命名的时候，像这种缩写字母应该三个都大写的，这里就不深究了。


接下来还有一个改动是哪里是这个 producer 怎样把它替换过来，把它替换成刚才创建的 dlq topic producerokay 那 controller 创建完了以后，咱移步到 consumer 里面，三下 5 除2，把这个例子给它搞定。


这里在最上面，我们把刚创建的 dlq 引入进来。实际上这个 enable bending 同学们如果不定义在 stream consumer 上面，你定义在其他地方可以吗？完全没问题，它实际上就是一个单纯的配置项而已。你看它点进去里面，这里有一个什么标签 configuration 对不对，咱甚至可以把它定义到启动类里面都可以，只不过一顶绿帽子给谁戴，不是戴是不是咱就放到 consumer 这里，戴起来比较方便。


好，咱把 drq 引入进来了以后，往下滚了。滚滚到哪滚到这里。我们把这个单机版的异常重试给它 copy 一下，大家记着 copy 单机版的。其他的不停用咱这个测试，就要我们把它复制到最后，然后依然从上往下改起来，这个注释给它改一下，叫死信队列。然后下面的 stream listener 这里把它替换成 dlq 的 topic 再往下把 consume error message 改成 consumer dlq message 实际上这个 message 并不是直接来自于 dlq 咱这样命名有那么一点歧义，不过大家心里明白就好，那他的业务流程依然是第一句见面一声，雷布斯问候。


are you okay 下面我们还是使用计数器，如果你可以被 3 整除，那我就把你放行过去。如果不能被 3 整除，那么我就抛出异常。但是咱这里要改一个地方，把这个计数器清零的动作给它去掉，待一会是有用的。那接下来在 log 里面，我们要把 dlq 的防伪标志给它打上每一行 log 让大家知道这是 dlq 的命令里面发出的。


OK 那到这里，咱的代码部分就写好了，同学们都创建这么多 topic 了，所以手撸一个 producer consumer 这个过程简直如行云流水了。对不对？好，我们接下来可以去到 properties 里面更改配置了，这里依然会引入一个新的配置。关于死信队列的，我们来看是什么配置。打开 resources 下面的 application DIM properties 咱这里先给它留出一块空地，然后添加上死信队列配置。


OK 接下来 copy 哪里的呢？咱去 copy 这一串这个单机版的重试，咱把它给 copy 下来，上面这些都不用变，那唯一要变的是它的 consumer 我们把 consumer 改成 dlq 同理 producer 也都改成 dmq 然后后面的这个 topic 咱也改成 dlq topic。 Ok. 这三样配置好以后，咱再给它添加一个消息组， copy 一下，往这放下来，把消息组的 consumer 改成 dlq 然后他的 group 也叫 dlq group。 Ok. 好啦，这里可以记出咱们的独门秘籍，专门给死信队列的一个配置。那我们把这个配置项的前半段给它 copy 上 cream cloud stream rabbit bindingsokay 那后面是谁呢？后面是我们的 dlq consumer 添加上去，紧接着再跟一个 consumer 再往后就是画龙点睛了，它叫 auto bind dlq 好，如果咱把这个属性给添加上去，在初始化项目的时候，咱的 stream 就会向 rabmq 里面添加一个死信队列。


这个死信队列的名称默认就是咱的 topic 然后后面跟一个点 dlq 那如果大家想指定一个已经存在的topic ，可以在这下面添加其他的配置，咱这里就不展开说了，因为 dlq 的配置项还是蛮多的，咱这里就用最简单的方式跟大家把死信队列的功能说清楚就可以了。所以这一行配置的作用是开启死信队列。然后这个时候它会创建一个默认的死信队列，它的名称就是 topic.dlq 好，我们把这个项目保存好以后，接下来就可以启动 application 来看一下效果了。我们找到它的慢函数，然后把它跑起来，稍等半炷香的时间。等这个项目启动成功以后，咱就去 rabbit MQ 的管理界面看一看这个死信队列长什么样子。 OK 我们把 log 清空一下，啊转战到浏览器里面。 OK 咱在这个 queues 这一个 tab 下面把它刷新一下，然后看咱刚才创建的 dlq topic 在哪。在这里。


OK 同学们看到这两行，第一行是我们创建的正常的 topic 正儿八经的 topic 它旁边有两个 tag 打上了两个标签，一个是 dlx 和 dlq 说明它是一个可以往死信队列中转发 message 的 Q 那如果同学们在启动项目后看到自己对应的 Q 里面没有加上这两个 tag 那可能就是启动的参数配置的不对或者某个配置项出错了，也有可能是咱前面提到的插件没有被开启。理论上这个插件是不需要重启的，只要打上了 enable 那个指令就可以自动开启。


那我们接着看下面的一个 Q 你看它跟上面一个长得是一模一样的，就最后多了一个小尾巴。 Dlq. 它就是咱自动创建出来的。同学们可能奇怪，怎么下面还有个 topic two 这两个是乱入的，大家不用管它，这是我其它的测试程序，不用管。 OK 那咱看完了死信队列长什么样子？接下来就到 postman 里发起一个调用。我们打开 postman 我这里已经添加好了一个URL ，它是发送到端口号为63033，然后访问路径为 dlq 的。好，我们尝试发送。第一次走你，我们回到 log 里面看看这个 Q 有没有被消费掉。 OK 同学们看这里有了两个 ruk 为什么？因为咱前面在配置项的时候，我们来看一下配置项中我们配置它的 max attempts 重试次数是2，这个属性把它解释成常式次数，可能更容易理解。咱这里配置的是 2 说明，他在接收完消息消费了一次以后，还会重新尝试 retry 一次。那么他这里 retry 以后正好被成功消费了。所以他很幸运的没有被加到 dlq 里面。那我们把 log 清空再来一发，看一看它还会不会像这次一样幸运，我们点击 send 走，你我们再回到 log 里面，你看已经抛出异常来了。那我们翻上来看，原始的 log 依然尝试了两次，只不过这一次不太幸运，没有被成功消费。


好，我们把 log 清空掉，回到浏览器里面看一看死信队列有没有什么变化？ OK 我们刷新一下。好，刷新以后往下走。 topic 依然还是那个 topic 大家看到哪里有不同了吗？大家来找茬。细心的同学可能发现了，后面这个数字变了，对不对。这个数字增长了一位，这是谁啊？死信队列的数字增长了 1 为什么？因为咱刚才把这个消息转发到了死信队列，所以它在队列中的消息总数增加了 1ok 那咱接下来尝试着把这条消息给它重新发到一个新的 Q 里面。那就在这里，我把页面放大一下。


同学们在点击进去这个死信队列的 topic 以后，可以看到有 move message 这个选项。在这个选项里，我们可以把死信队列中的消息移到其他的队列中进行重新消费。假如大家在 move message 这里并没有看到这个按钮，也没有看到当前的输入框，而是看到了一行错误提示。


是什么？错误提示我给大家打下来看一下这一行错误记是，他说如果你要动我，那先要怎么样？先要把这个插件给他开启什么插件？就是咱刚开始上课之前跟大家讲的需要安装的两个插件，那同学们就可以用下面这个命令先把两个插件打开就可以了。 OK 那我们再回到浏览器里面，那这里 destination Q 就是你的 Q 的名称。那我们填写 destination Q 的时候应该填写谁呢？如果填 dlq 点杠 topic 是不是正确的呢？其实不是的。我们回到前一个界面，我跟大家讲怎么找正确的 Q 那在 Q4 这个页面，咱往下滑滑滑到这里。 OK 我们看到这个 Q 的name ，实际上不光是 dlq 杠 topic 它后面还跟了一个 group 也就是组。对不对？好，我们把这一行都给它 copy 下来，然后回到刚才的页面，那这才是你正儿八经的 destination 那我们准备点按钮喽。


点完以后我们回到 consumer 里看一看这条消息是不是被正确的消费了。好，回到 intelligiok 同学们看，就在刚刚这条消息被移动到正确的 Q 以后，它就被我们的消费者给拿到，然后消费成功了。 OK 那到这里，咱这一节的内容就结束了，我跟大家回顾一下，在这一节当中，其实主要的一个核心点就在这里。那这一行配置是开启整个 D LQ 死信队列的核心配置。但是大家要知道死信队列的配置可远远不止这一个，咱这里是用的最简单的方式开启了默认的配置。如果同学们想做更细致的配置，比方说我想让私信发到一个指定的 Q 而不是它自动创建的 Q 或者我想指定死信的 routine key 等等，那就需要借助其他的参数来搞定它了。


死信队列在真正的生产环境里，咱的真实项目里应用还是很广泛的。但是并不是所有的中间件都有死信队列。大家如果需要死信队列认准 rabbit MQ 就行了。 OK 那这一节的内容就到这里结束了。在下一节当中，我将带大家一起创建一个自定义的异常处理规则，它是咱 stream 章节中最后一个知识点了。同学们打起精神，一鼓作气，我们下一节再见。





