---
title: 1-4 Update的幂等性示例
---

# 1-4 Update的幂等性示例

[image](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/a684f2ef-9648-4ad5-91fc-cc4d58abfaa2/SCR-20240808-gnti.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RYS6C6JO%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T225445Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIFqYJGBUqzINKehwaqpzmO9c2JmX47861D4xfaRpfFWPAiEA5NgeiSUTSRNspFMRMQ4oRTOuynlmqfZuv1FwDPzxs4YqiAQIxv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDPe0BOIuRAw2pxlAdyrcA%2BQ1bMyIIB4ZnPzveY6U6s4Akb9JFmMVuN9o314wTXmh5AUs9fuvKBaxbZSJmDyvUa%2B%2F6McoD50wigOQgFJVE3aH6Iq5KlDZp6H6V5UDcYozj%2BxGcCHeLnrKF4dnPGL2nkwpxafLulcv43O1JTv0c2%2F81ZF0nwxa71eim%2FlhWTiaXcNyZMUdFegnooPMUiu3a3cLrJdiNCl0kfZzh8vri1fuyciOq%2BjMltbASgwFihvKE8Xb0pW12%2F7dEqYAJcWbp7kV32CyDFv7Ipv4WeLVBSEZuRbUNQmyCk63ygyMvTJnQtT2rggr9D824RSvEjoDQhZB9NiHF9Ie95MdMobYqGMB8EIPIVhg9k0EMUhSXx6PWBXN%2F1Sa382ZD4nRDK66i%2FcAW9Bc6aAsNr%2F82Vpqw3ttrdEu%2BR43tD%2FQjCd24iKZn7mH3FRtdOZ5CNMCMVkWw%2FtA7YeMJlpzJ8wALz1nRLeh2e4ZR06Kp9uQcvG5UMwvZcXsTiZDl7O0DhI%2FP4j71%2BnhWkwKsNhmpQC7PoCiWoyQxjLpoU6xXJJ%2BBG%2FrodhYgqlRYlq8jmj3fhm0MeCNkrWWfn3iLgkm9bAMU%2FTTPxAiQmEZ5%2FZHTmU1dl%2BWf5IUq8cHcPXzn2g6GvZGMPK6%2F9IGOqUB5QTAWkgzEHcN7NGytP0Wr6mdsla1qO3fUFmsgFkkN7NlLi2erzjcOTgmeBjoY6nMDqvPXC2EVrJBWlF5OYOiglZLchuUtsTZP3RaFSVRBbTDukZMvigtLvl2rZnOcGdvMHrOtLHEor%2BXhe8p4kfqLwDbwmnl%2BVfVGBlY%2FGgAmjcZOymYwDPe32ec3hJtvQW8QedB4hhV66%2BBQTA0KQ4xM%2BtXbFtn&X-Amz-Signature=71906e735d1b8e0d5017861caac1d1399138d4dea43c3484c42af4f70c7c942f&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

[image](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/65a4046b-e115-4549-99de-9db947b9c80e/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RYS6C6JO%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T225445Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIFqYJGBUqzINKehwaqpzmO9c2JmX47861D4xfaRpfFWPAiEA5NgeiSUTSRNspFMRMQ4oRTOuynlmqfZuv1FwDPzxs4YqiAQIxv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDPe0BOIuRAw2pxlAdyrcA%2BQ1bMyIIB4ZnPzveY6U6s4Akb9JFmMVuN9o314wTXmh5AUs9fuvKBaxbZSJmDyvUa%2B%2F6McoD50wigOQgFJVE3aH6Iq5KlDZp6H6V5UDcYozj%2BxGcCHeLnrKF4dnPGL2nkwpxafLulcv43O1JTv0c2%2F81ZF0nwxa71eim%2FlhWTiaXcNyZMUdFegnooPMUiu3a3cLrJdiNCl0kfZzh8vri1fuyciOq%2BjMltbASgwFihvKE8Xb0pW12%2F7dEqYAJcWbp7kV32CyDFv7Ipv4WeLVBSEZuRbUNQmyCk63ygyMvTJnQtT2rggr9D824RSvEjoDQhZB9NiHF9Ie95MdMobYqGMB8EIPIVhg9k0EMUhSXx6PWBXN%2F1Sa382ZD4nRDK66i%2FcAW9Bc6aAsNr%2F82Vpqw3ttrdEu%2BR43tD%2FQjCd24iKZn7mH3FRtdOZ5CNMCMVkWw%2FtA7YeMJlpzJ8wALz1nRLeh2e4ZR06Kp9uQcvG5UMwvZcXsTiZDl7O0DhI%2FP4j71%2BnhWkwKsNhmpQC7PoCiWoyQxjLpoU6xXJJ%2BBG%2FrodhYgqlRYlq8jmj3fhm0MeCNkrWWfn3iLgkm9bAMU%2FTTPxAiQmEZ5%2FZHTmU1dl%2BWf5IUq8cHcPXzn2g6GvZGMPK6%2F9IGOqUB5QTAWkgzEHcN7NGytP0Wr6mdsla1qO3fUFmsgFkkN7NlLi2erzjcOTgmeBjoY6nMDqvPXC2EVrJBWlF5OYOiglZLchuUtsTZP3RaFSVRBbTDukZMvigtLvl2rZnOcGdvMHrOtLHEor%2BXhe8p4kfqLwDbwmnl%2BVfVGBlY%2FGgAmjcZOymYwDPe32ec3hJtvQW8QedB4hhV66%2BBQTA0KQ4xM%2BtXbFtn&X-Amz-Signature=90465bdee7d1a4d08e89bef7f76705dfe9fb7bf7ec930c9e89bbd47bb9f530e5&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

hello 大家好，咱们还是进入到之前的项目，咱们先运行一下。先来回顾一下前面的这个项目，它的这个页面是什么样子。好，这个项目已经启动成功了是吧，咱们打开这个浏览器，然后访问一下 local host 8080 杠 user 是吧。然后 user list 这个现在数据库里还没有这个用户的记录是吧，一会咱们造一条。首先咱们要在这个操作里边要加一个按钮是吧，咱们还是把这条记录先给他创建出来。打开 131 的数据库，进入到 xa 131，然后 T user 对吧，咱们里边创建一个创建一条记录，然后再刷新一下这个页面。有了这么一条记录是吧。然后咱们要在这个操作后边加上一个修改的按钮，然后点击修改按钮会进入到一个详情页是吧，这个页面一会咱们也再做一下，把这条记录给他按表单的形式展示出来。然后咱们修改其中的一个字段，点击提交，然后再跳回到列表页进行刷新。咱们先把这一步骤完成，完成以后咱们再着重再说一下 fz 的操作咱幂等性好吧。


首先咱们要在这个页面后边加上一个修改的按钮，咱们进入到项目，然后在这个 user list 这个 HTML 当中后边加上一个按钮是吧，这个按钮叫做修改。然后把它的内幕咱们也改一下，叫做 update 然后这里边再写一个方法是吧，这个方法他要监听的是 update 这个按钮 document.on 是吧。然后第一个参数 click 第二个参数，你要，监听的元素就是 W date 对吧，后边跟着 function 在这个 function 里边呢，咱们直接就是页面跳转了 location.hief 等于 user 然后后边跟什么跟 user detail 。好吧，然后再传入一个 user ID 等于这个 ucid 咱们也要取一下是吧，也在这个 ucid 的这个属性当中，VR user ID 等于当前的这个元素。


attr 取一下 user ID 对吧？是不是这样？加上一个 user ID 这样是不是就可以了？然后它会跳转到 user controller 是吧。然后咱们在 user controller 里边再写一个 request mapping 对应的是 user detailpublic string user detail 然后传入一个 user ID 对吧，这个 user ID 要求是必填的 request parameter 对吧。然后方法上打上一个注解 request mapping 对应的是 user detail 然后咱们要根据这个 user ID 把这条记录给它查询出来对吧，这个咱们还是调用一下这个 service.select ID 然后把 user ID 给它传出去。前面咱们要用这个 user 要接一下是吧。


目前这个 user service 里边还没有这个方法，咱们要创建一个方法对吧，这个直接 return return 一个 user mapper.select by primary key 是吧，反正我 user ID 这样是不是就可以了？再回到 controller 这一层，咱们还要把这个 user 给它放到 modemap 当中。


方法的入参咱们还要加上一个我的 map 然后 map.add attribute user 是吧，然后把这个 user 的变量传进来，最后返回的是页面页面的路径是吧，咱们还是参照上面的这个写 user 然后杠 user detail 这样是不是咱们的后台的方法就写完了是吧。写完以后咱们要写，这个页面咱们就直接复制，改一个名字 detail title 改一下改成 detail 这个表单是不是就没有了？这些后边的都没有了是吧，咱们直接给它删除掉了。然后里边咱们要加上一个 home 的表单是吧。 form 然后它的样式咱们也写一下，margin上下是0，左右是凹凸是吧。 method 这个 form 咱们修改完以后要统一的去提交是吧，这个提交的方法咱们使用 post 然后 action 这个都还没有定是吧，咱们暂时先随便写一个。


杠 user 杠 update user 好吧，咱们先暂定是这个链接，然后里边第一个我们放一个 input 标签是吧，它的类型咱们用作hidden ，这个咱们主要是存的它的 ID 是吧，这个 ID 一般是不会变的是吧，然后它的 value 它的 value 咱们赋值要用这个 TH 标签是吧？ TH 然后 attr 等于 value 等于后边跟一个花括号里边 [user.id](http://user.id/) 是吧，咱们把这个用户的 ID 放到了这个隐藏域当中，然后咱们点击提交按钮的时候，把这个 ID 是不是也带到后台了，咱们再根据这个 ID 去进行数据的更新。这个 ID 就是这个 update 操作的唯一的业务号是吧，这个是非常非常重要的。然后第二个字段 input type 它就应该是 text 这个字段咱们写的是 lose name 对吧。同样 TH attr value 等于，然后跟上一个花括号 user 点咱们看一下这个 user user name 是吧。


user.user name 用户名，咱们写好以后就要写这个性别了是吧，这个性别它是一个选项，咱们用 select 是吧，name等于 sex 是吧，然后里边有三个选项，option第一个 y6 等于 0 是吧，它是未填。


然后 11 它是男对吧二代表的是女这三个选项写好以后，咱们要把这个选中的状态给它加上是吧。就是这个 selected 同样对这个属性去赋值，咱们还用 TH 对吧。 thattr 等于 selected 是吧等于，然后跟上一个花括号 user.sex 等于 0 这样是不是就行了？咱们这个先这样写，一会不行的话咱们再进行调试。然后还有。
最后一个是年龄是吧 input 然后 type 年龄它是一个数字类型的是吧这块咱们就是 number 了，它的类型是 number name 等于 agevalue 同样使用 ATT R 等于 value 然后跟上一个括号 user.h 那么这几项咱们都已经列在这里面了，然后再加上一个提交按钮， button type 等于 submit 是吧？写上一个提交，这样是不是这个页面就写好了，咱们把这个项目重启一下，调试一下，看看咱们写的对不对？好。


项目冲击成功，咱们刷新一下这个列表页，多了一个修改是吧，咱们，点击一下修改。这个是不是都已经列在这了？这个样式还是有点问题是吧？咱们稍微改一下，这个咱们统一修改一下，把它居中，然后每一项咱们还要给它换行是吧，咱们这个标题也没有是吧，咱们统一加一下。


回到这个项目首先让它居中，咱们在这个 body 上边加上一个 style 然后 text align 是吧 center 这样它是不是就居中了？然后后边怎么样让她换行是吧这块咱们还要每一个输入项，前面要加上一个标签。第一个是用户 ID 是吧，它是隐藏的，咱们就不用加了。第二个用户名是吧。最后再来一个 BR 然后第二项是一个选项是吧，性别同样的咱们也加上一个BR 。最后一个年龄同样加上一个 DR 然后咱们重新构建一下，再回到浏览器刷新一下这个页面，这样是不是就可以了？这个还是有点丑是吧，应该让它居左居左是不是就可以了？咱们再改一下，统一的去左。然后这个 form 表单咱们统一改一下，它的外边距的顺序上右下左是吧，右边自动下也是0。然后左咱们给它写一个300。好吧，咱们刷新一下，看看效果如何。这样是不是好多了？咱们就先简单的这样看吧。好吧，现在用户名，然后性别年龄都已经有了。最后提交按钮是吧，然后咱们要写这个提交按钮咱们还是回到这个 idea 在这个 user controller 里边，咱们要写一个 update user public string 然后 update user 传入的就是咱们的这个 user 表单打上一个 request mapping 这个注解大卫的 user 对吧，然后咱们就要进行更新了是吧。


user service.update user 把这个 user 给它传进来对吧，创建一下这个方法，咱们直接 return user mapper 点儿 update primary key selective 是吧，我们用这个方法，更新完成以后咱们要进行跳转 return redirect 跳转到哪个方法，转到这个 user list 是吧，跳转到 user user list 这样是不是就可以了？这个更新的操作是不是就写完了？咱们重启一下看看效果。充气完成了是吧。


咱们回到浏览器刷新一下这个详情页什么呢？要把这个用户名给他改一下是吧，给他改成以4，然后点击一下提交是吧，看看他能不能完成更新。提交好，提交完成以后，他又回到了这个列表页对吧。列表页，然后再去检索这个用户，咱们可以看到这个用户名已经变成了第四了是吧。同样咱们现在就要模拟一下重复提交的问题，在这里边这个提交按钮如果没有及时的响应是吧，咱们点击了多次是吧，那么它对这个结果有没有什么影响呢？下面咱们就模拟一下咱们要点击这个提交要点击多次是吧，咱们刚才一点击提交是不是这个系统就有反应对吧，直接给咱们跳转到了列表页下面，咱们把更新的方法给它休眠一下，咱们回到这个项目当中。


在这块咱们给它休眠，就是模拟一下这个系统响应慢是吧。那么休眠 5 秒钟这块有一个异常是吧，咱们给它抛出去，然后把日志给大家打印一下更新用户是吧，然后咱们重启一下，咱们一会点击多次看看他是不是多次的访问了后台的 update 的 user 这个方法。然后再比较一下这个更新以后的这个结果，现在已经重启成功了是吧，咱们刷新一下这个表单页，然后咱们多次的点击这个提交。现在因为后台休眠了 5 秒，它没有及时的响应是吧。好这时候已经响应过来了，咱们再看一下后台总共访问了 7 次是吧。那么七次对咱们的这个用户数据有没有影响呢？咱们看看现在还是李四是吧，咱们刚才是不是没改这个用户名，咱们再重新改一下，给他改成张三，咱们还是点击多次提交，咱们看一下后台的日志。
现在咱们点击了 6 次提交是吧，然后前面的用户名还是改成了张三等于是说我虽然点击了 6 次提交，但是我的结果是没有任何影响的，我都是把用户名改成张三是吧。那么这个时候这个 update 的操作它本来就是幂等的，其实不需要咱们做什么处理。但是如果有另外一种情况就会有影响了。还是咱们在 PPT 当中举的这个例子，如果在这个用户表当中，有一个字段它叫做更新次数。那么这个时候咱们点击多次更新的话，它会是一种什么效果呢？咱们先把这个项目停一下，模拟一下这个有更新次数的这个字段像是什么样子？首先咱们回到这个数据库，在这个 T user 这张表当中增加一个字段，增加一个更新次数是吧？ Update count. 然后咱们再用那个乐观锁去解决这个逆等性的时候，还要有一个版本的字段是吧，有一个 version 他是 int 长度是1，非空默认值是 1 数据第一条进来，它的版本号就是1，然后这个 update count 它也是一个 in 才行。位数咱们给它设置长一点，设置 6 位。好吧，那么更新次数默认是0。好吧，那么保存一下。


然后接着咱们要修改项目当中的拜拜意思映射是吧，咱们还是回到项目？首先要修改这个 user user 里边增加了两个字段是吧，这个咱们统一修改是不是太麻烦了，咱们直接再重新生成一下。好吧，重新生成咱们要把之前写的这个方法咱们要先给它复制出来。咱们之前是不是只写了这么一个方法，咱们把这个复制一下复制一下。然后把这个三个 user 相关的这个类都给它删除掉。一个 user mapper NPS 后一个 user 一个 user example 最后还有一个叉 ML 配置文件对吧，总共这四个文件咱们统一的删除掉。然后点击右侧的 Maven 进入到 my baddies 的生成器的插件，双击一下生成完成了是吧。没有问题。然后再把刚才咱们复制好的这个方法在这里边给它粘贴好，这样是不是就没有问题了？然后咱们再回到这个 user controller 在 user controller 里边，咱们每更新一次，咱们要把这个更新的次数给它加 1 是吧。那么这个咱们要单写一个方法了是吧，咱们这块儿给他单写一个 update user 单写这么一个方法，咱们创建一下。那么这个方法咱们要在这个插满 2 文件里边重新定义一下，创建一个 update user 的。这个方法咱们可以参照这个 update by primary key selective 可以参照这个方法写是吧。那么直接把这一段给它复制下来。


复制下来以后这里面有一个字段，咱们要特殊处理一下，就是这个 update count 是吧，update count 咱们要给它设置成为 up count 等于 up day 的 count 加1，是不是这块咱们要写成这样，这个咱们还要在这个 user detail 里边，把这个 W 的 count 给它展示出来是吧，这块咱们加上一个字段，更新次数。
这个更新次数是在前面是不能修改了，咱们直接用一个 span 然后 TH text 等于后边跟咱们的这个画括号里边是 user.update count 是吧，然后这个 span 咱们给它关闭一下，这样这个详情页就增加了这个更新次数了是吧。后边还有一个 BR 详情页咱们加了这个更新次数相应的列表页，咱们也给它加一下。在这个年龄后边咱们给它加一个更新次数对吧，这块儿同样加上一个 user 点儿 update count 是吧，咱们先运行一下，刷新一下这个更新页。现在这个更新速度是 0 是吧。
咱们如果多次点击提交的话，咱们期望的结果是更新次数是 1 是吧。因为你的这个系统没有及时响应，所以我点击了多次提交，我的本意是只更新一次，但是我点击了多次，那你的更新次数会是什么样子？对吧？这块咱们模拟一下，点击多次，然后等待等待 5 秒钟。


咱们看一下咱们这块更新次数变成了 6 次了是吧，这个是不是就有影响了？那么说明咱们这个修改按钮的这个提交的方法，它是不满足幂等性的，所以这块咱们要修改一下，使它满足逆等性对吧？那么咱们怎么去修改呢？首先第一步要把咱们的版本号返回到页面当中来是吧，咱们这块还要再加一个隐藏域 input type 等于 hidden 内幕等于 version 是吧，然后它的值 thattr 等于 value 的跟上咱们的 user.version 是吧。然后更新的时候咱们要根据这个版本号去进行更新，把它传入到后台是吧，传入到后台实行这个 SQL 语句这个 version 字段咱们也要给它修改一下，给它改成和这个 update count 是一致的， version 等于 version 加1。然后这个 y2 条件咱们也要把这个 version 字段给它加进来是吧。 version 等于传入的。这个不说是这样，是不是就满足了。根据版本号去更新数据的要求了是吧，咱们再重新的捋一下。


在这块你在点击提交的时候，多次点击向后台发送了多次提交的请求。对吧，多次提交的请求。最后到 up 内的这一行的时候，它会由并行转化成为串行是吧。因为 update 它是有行锁的，所以你的这些 update 的语句都会进行串行的提交，也就是一行的去执行，一行一行的去执行。那么第一条记录，你执行执行的时候会根据 version 这个字段去判断是吧，因为当前的这个 version 的字段是 0 是吧，当前的 version 字段是0。那么咱们带着这个 version 等于 0 去更新这条记录更新完成以后，第二条记录再更新的时候，它传入的这个 version 字段还是 0 是吧。那么这个时候咱们当前的这个 version 字段已经变成 1 了，那么它不满足 y2 条件。所以第二次这个更新的 SQL 语句就是更新失败的。那么这个时候保证了咱们多次更新的时候只有第一条 update 的语句可以更新成功对吧，咱们试一下重启一下这个项目。


然后咱们刷新一下这个更新的页面，多次的点击这个提交按钮，咱们看看后台咱们是点击了 7 次是吧，7次如果按照上次咱们运行的结果应该是 6 加上 7 等于 13 是吧，咱们现在再看一下它的更新次数只增加了 1 次是吧。那么说明咱们这个乐观锁是有效果的对不对？咱们在更新的时候，根据 version 字段去更新这条记录，再加上 update 它本身有航锁，你第二条再进行更新的时候，这个 version 字段的值已经发生了变化，你的这个 y2 条件就不满足了对吧？所以它的更新是失败的。那么这个时候咱们虽然点击了多次提交按钮，那么只有第一次的更新是成功的，这样就保证了 update 操作的幂等性对吧。好了，这一节 update 操作的幂等性就给大家介绍到这。下一节咱们要给大家介绍 insert 这个接口的幂等性操作，感谢大家的观看。



