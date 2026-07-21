---
title: 2-14 【技术改造】电商系统用户模块集成Feign-1
---

# 2-14 【技术改造】电商系统用户模块集成Feign-1

[image](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/6e1df246-b45c-412d-ad58-16dd1572cb9a/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VTONEK4V%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T225628Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIBIyehUBj7eN41%2BIAY%2BNqPosAb6EGyvluK9MPBYBEX8gAiA5X27we3k1SG%2B1%2BsNI9L7c9FByHmKXN59YPCRAuveY9yqIBAjG%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMnBiHIfQcq9xIQxgNKtwDO1hljGirRaKdEPVQwn5GenuE4QTUmQXeaN%2FISNhRggHQ4vNZhdkqKm0WWycegwxHl6x7gYSHQTHv5FnGNrU7tY5K2RPH9RZFnkfFRyYCmh%2Fuwo66mNFy%2BiwjI2EK2rjAA2K0bopSegCTO5VCLlJtdSkELnEf0VnijD6kNk3w%2B9vEJuME62Z3nhwuMkgdndSWISsfkaekFNaSpic3fGIoQ%2B6JzvYTd49fG%2F2ilbM5UpihaAS9QT6LqL9ZTCVst33L%2B5oZ9wh8XCqDBxJQRSltCh15UvDxULxFg8MfrPgARqFFuZthQrWkwqTagmLhUoVnXRWJbLLHvVDdsIp4Hq6jn80kmJD4y%2FniahxQkzqVpVfPTKKKl66K4ROq0sXzXPlUUk1mCsRTpagGrWZj9Edb4r8SyhGUj5yyYuMjWX%2FiWBGK3NBTS5JZ8PYgJf%2BJjQh9WPKpeE%2B2gwIPV17ORsAS6WzPn0n0bm3lRVEBfr19BeT%2Fzg%2Bi%2B4l0v5N78aoYlH%2BEnK0r3Zp7r7W6TgdA7CKPed1EE04%2BNWJnAOiTKOIYWAhonS%2FgEiH936EL3FAqLHM7Wem%2BBqC%2FjW7zZrieP0ernIWxS822Lz5UXnoAo2bPKXN%2FTZH8Gsw2Bv6DXmcwgbf%2F0gY6pgHKerkGfR9%2Bez6GTCrrWe9EgNkZt6%2FL4MKXr11fUls6wrcuK8x9qJGW9AOjqPkdviKnPqYNamDlul85ZUOPkTqSR1djRJYBZlftadd%2Fp%2FiYjVU0LZUA4XvTL6P93xKaAbG4kyigsRy1h2NHLjIkyTwvrRl0t9FLS3kwcCX%2FoZetgmW4vcrgevjYEMTNuzac9%2BjqtirqhwQNCMlapYP4sG22QZtO1NTz&X-Amz-Signature=27582e0aa26463d49e3863d1feabb7e6e9a7b2cc76c41caa3604b6cf3afe54e3&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

[image](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/2c099532-fa02-4f39-a72f-0691c864e805/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VTONEK4V%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T225628Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIBIyehUBj7eN41%2BIAY%2BNqPosAb6EGyvluK9MPBYBEX8gAiA5X27we3k1SG%2B1%2BsNI9L7c9FByHmKXN59YPCRAuveY9yqIBAjG%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMnBiHIfQcq9xIQxgNKtwDO1hljGirRaKdEPVQwn5GenuE4QTUmQXeaN%2FISNhRggHQ4vNZhdkqKm0WWycegwxHl6x7gYSHQTHv5FnGNrU7tY5K2RPH9RZFnkfFRyYCmh%2Fuwo66mNFy%2BiwjI2EK2rjAA2K0bopSegCTO5VCLlJtdSkELnEf0VnijD6kNk3w%2B9vEJuME62Z3nhwuMkgdndSWISsfkaekFNaSpic3fGIoQ%2B6JzvYTd49fG%2F2ilbM5UpihaAS9QT6LqL9ZTCVst33L%2B5oZ9wh8XCqDBxJQRSltCh15UvDxULxFg8MfrPgARqFFuZthQrWkwqTagmLhUoVnXRWJbLLHvVDdsIp4Hq6jn80kmJD4y%2FniahxQkzqVpVfPTKKKl66K4ROq0sXzXPlUUk1mCsRTpagGrWZj9Edb4r8SyhGUj5yyYuMjWX%2FiWBGK3NBTS5JZ8PYgJf%2BJjQh9WPKpeE%2B2gwIPV17ORsAS6WzPn0n0bm3lRVEBfr19BeT%2Fzg%2Bi%2B4l0v5N78aoYlH%2BEnK0r3Zp7r7W6TgdA7CKPed1EE04%2BNWJnAOiTKOIYWAhonS%2FgEiH936EL3FAqLHM7Wem%2BBqC%2FjW7zZrieP0ernIWxS822Lz5UXnoAo2bPKXN%2FTZH8Gsw2Bv6DXmcwgbf%2F0gY6pgHKerkGfR9%2Bez6GTCrrWe9EgNkZt6%2FL4MKXr11fUls6wrcuK8x9qJGW9AOjqPkdviKnPqYNamDlul85ZUOPkTqSR1djRJYBZlftadd%2Fp%2FiYjVU0LZUA4XvTL6P93xKaAbG4kyigsRy1h2NHLjIkyTwvrRl0t9FLS3kwcCX%2FoZetgmW4vcrgevjYEMTNuzac9%2BjqtirqhwQNCMlapYP4sG22QZtO1NTz&X-Amz-Signature=add3cec9448261d520bd50cb38c15fc3996f85240b268f6c3781f8d893ff0f2d&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

[image](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/5ea5c54b-1a3a-4dc7-b502-0cf9af20e74f/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VTONEK4V%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T225628Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIBIyehUBj7eN41%2BIAY%2BNqPosAb6EGyvluK9MPBYBEX8gAiA5X27we3k1SG%2B1%2BsNI9L7c9FByHmKXN59YPCRAuveY9yqIBAjG%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMnBiHIfQcq9xIQxgNKtwDO1hljGirRaKdEPVQwn5GenuE4QTUmQXeaN%2FISNhRggHQ4vNZhdkqKm0WWycegwxHl6x7gYSHQTHv5FnGNrU7tY5K2RPH9RZFnkfFRyYCmh%2Fuwo66mNFy%2BiwjI2EK2rjAA2K0bopSegCTO5VCLlJtdSkELnEf0VnijD6kNk3w%2B9vEJuME62Z3nhwuMkgdndSWISsfkaekFNaSpic3fGIoQ%2B6JzvYTd49fG%2F2ilbM5UpihaAS9QT6LqL9ZTCVst33L%2B5oZ9wh8XCqDBxJQRSltCh15UvDxULxFg8MfrPgARqFFuZthQrWkwqTagmLhUoVnXRWJbLLHvVDdsIp4Hq6jn80kmJD4y%2FniahxQkzqVpVfPTKKKl66K4ROq0sXzXPlUUk1mCsRTpagGrWZj9Edb4r8SyhGUj5yyYuMjWX%2FiWBGK3NBTS5JZ8PYgJf%2BJjQh9WPKpeE%2B2gwIPV17ORsAS6WzPn0n0bm3lRVEBfr19BeT%2Fzg%2Bi%2B4l0v5N78aoYlH%2BEnK0r3Zp7r7W6TgdA7CKPed1EE04%2BNWJnAOiTKOIYWAhonS%2FgEiH936EL3FAqLHM7Wem%2BBqC%2FjW7zZrieP0ernIWxS822Lz5UXnoAo2bPKXN%2FTZH8Gsw2Bv6DXmcwgbf%2F0gY6pgHKerkGfR9%2Bez6GTCrrWe9EgNkZt6%2FL4MKXr11fUls6wrcuK8x9qJGW9AOjqPkdviKnPqYNamDlul85ZUOPkTqSR1djRJYBZlftadd%2Fp%2FiYjVU0LZUA4XvTL6P93xKaAbG4kyigsRy1h2NHLjIkyTwvrRl0t9FLS3kwcCX%2FoZetgmW4vcrgevjYEMTNuzac9%2BjqtirqhwQNCMlapYP4sG22QZtO1NTz&X-Amz-Signature=d7ba63c931dd0cb64ae03005cbbf537389018ee417e3042e37144b0ab5dc44fc&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

hello 我们课网的各位同学们，大家好，这一节咱终于等到了电商项目改造的环节，我们要对前面基于有瑞卡搭建的这个项目结构做一个整容。这里面主要包含两个步骤，第一个步骤， all in finn 我们把这些类接口通通加上分的注解以及配置一些分的配置项。第二步就是我们整容环节的主要过程，把之前基于尤瑞卡那种非常纷繁复杂的服务调用全部改成基于接口调用的风格。好同学们抄起家伙 in 泰利杰里走起，每天扣丁 1 小时，健康工作 50 年。

[image](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/5b0968b2-8351-47b9-959b-cc49b7d97073/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VTONEK4V%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T225628Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIBIyehUBj7eN41%2BIAY%2BNqPosAb6EGyvluK9MPBYBEX8gAiA5X27we3k1SG%2B1%2BsNI9L7c9FByHmKXN59YPCRAuveY9yqIBAjG%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMnBiHIfQcq9xIQxgNKtwDO1hljGirRaKdEPVQwn5GenuE4QTUmQXeaN%2FISNhRggHQ4vNZhdkqKm0WWycegwxHl6x7gYSHQTHv5FnGNrU7tY5K2RPH9RZFnkfFRyYCmh%2Fuwo66mNFy%2BiwjI2EK2rjAA2K0bopSegCTO5VCLlJtdSkELnEf0VnijD6kNk3w%2B9vEJuME62Z3nhwuMkgdndSWISsfkaekFNaSpic3fGIoQ%2B6JzvYTd49fG%2F2ilbM5UpihaAS9QT6LqL9ZTCVst33L%2B5oZ9wh8XCqDBxJQRSltCh15UvDxULxFg8MfrPgARqFFuZthQrWkwqTagmLhUoVnXRWJbLLHvVDdsIp4Hq6jn80kmJD4y%2FniahxQkzqVpVfPTKKKl66K4ROq0sXzXPlUUk1mCsRTpagGrWZj9Edb4r8SyhGUj5yyYuMjWX%2FiWBGK3NBTS5JZ8PYgJf%2BJjQh9WPKpeE%2B2gwIPV17ORsAS6WzPn0n0bm3lRVEBfr19BeT%2Fzg%2Bi%2B4l0v5N78aoYlH%2BEnK0r3Zp7r7W6TgdA7CKPed1EE04%2BNWJnAOiTKOIYWAhonS%2FgEiH936EL3FAqLHM7Wem%2BBqC%2FjW7zZrieP0ernIWxS822Lz5UXnoAo2bPKXN%2FTZH8Gsw2Bv6DXmcwgbf%2F0gY6pgHKerkGfR9%2Bez6GTCrrWe9EgNkZt6%2FL4MKXr11fUls6wrcuK8x9qJGW9AOjqPkdviKnPqYNamDlul85ZUOPkTqSR1djRJYBZlftadd%2Fp%2FiYjVU0LZUA4XvTL6P93xKaAbG4kyigsRy1h2NHLjIkyTwvrRl0t9FLS3kwcCX%2FoZetgmW4vcrgevjYEMTNuzac9%2BjqtirqhwQNCMlapYP4sG22QZtO1NTz&X-Amz-Signature=59ad60f5d98766fe8ace627e15e17f458ec9a690791cc963a14beb8da5425eee&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

那咱这里就按照之前有瑞卡改造微服务的顺序，先从 user 模块开始动刀子。 OK 那这里第一步就要把分的注解可以引入进来。在这引入注解之前，我们先要把它的依赖项引入。好这里我们先挑选 food user API 因为这个 user API 层是最早开始接触 phone 的，所以我们把 phone 的依赖在这里添加进去。好，那我们 copy 一下前面的模板，好把这个 todo 给它去掉，然后它的 group ID 这里不是 boot 是 cloud 后面跟 spring cloud 之后是 starter open 其实同学们如果看这个 phone 组件的发家史，你会发现它最早并不是在 open phone 这样的一个文件夹结构。下面它最早是在 Netflix 的组件库下。


如果你回看一些早期版本的 spring cloud ，它这里有一个包叫 Netflix call 那 then 就是在那个包下面，等到后面的版本才把份从 Netflix call 当中给它抽取出来，组建了 open fan 项目。所以这个份和 Netflix 500 年前是一家了。


好，那这里依赖项加入好了之后，我们打开代码，然后在这些 service 上面，那同学们应该都非常熟悉，我添加一个 ben client 好，然后后面给谁的名字呢？当前这个服务是谁提供的？它的 application name 是 foodie 杠 user serviceok 我们把这个注解给它复制一下，然后剩下的小伙伴头上都给戴上这顶绿帽子。


OK 老师为什么说是绿帽子呢？看字体的颜色这什么色，这不绿色吗？他扣上一个注解的大帽子，这不是绿帽子是什么？那接下来我们来看一下这个 user 杜曼他有没有调到其他服务的 service 没有，因为它相对独立对不对？把接口提供给别人调用，那它这里不需要调用别人的服务。所以我们在这个闷函数上，user application 里面就不用配置份的扫包路径了。


我们这里在 application YAML 里面添加这样一行配置，我们在 spring 的这个下面，就在 main 函数下面在这里添加一个注释。那它的节点是 men 那后面同学们应该都非常熟悉了，是否允许并覆盖 all been definition over riding 那它的值我们给它 true 这个意思大家应该还记得吧，当 in 名字一样的时候，允许覆盖注册。


OK 那好到这里，咱这个 user 就已经改造完成了，是不是非常方便啊？那这个方便姓氏提供给谁？是给那些需要调用我服务的人提供方便。所以待会我们改造到 order 的时候就可以发现，从 order 调用到 user 这个调用方式会比以前方便很多。好接下来我们去改造一下 item 组件，这里用同样的方式在 item API 这里找到它的 pom 文件，然后在下面加入 fend 依赖。好我们把 user API 下面的份依赖给它 copy 过来。好把这个 todo 给它去掉。


OK 那 copy 完成以后，剩下的事情和 user API 是一样的。我们把这个分 client 注解给它拷贝一下，然后找到 item API 下面所有的接口类，只有这两个，我们先在 item service 上面把它添加上去。但这里同学们要记得把这个名称改了，你这里的名称要和你在 web 应用当中声明的这个 application name 保持吻合。比如你这里 application name 是 food item service 那这里名称也给它写成同样的。 OK 这里拼错的话会有问题的。好我们把这个分 client 再给 copy 一下，同样的把它也放到我们新添加的这个 item comments 评论模块的服务上。 OK 那咱这两个应用改好了以后，我们这里转移到 item web 当中，在他的 YAML 文件里 copy 上同样一段话。哪一段话就是我们前面刚刚在 user 外部应用里添加的这一行配置 override 允许 bin 的 name 重在。


好，我们把 item web 的样本文件同样加上这样一句缩进行。同学们注意，这缩进经常会打错，那你缩进错误，这个 YAML 文件解析会有问题。那么现在转战到 order 模块，我们接下来用同样的方式把这个分的依赖项添加到 order API 这里。然后同样的在 order API 的三个 service 上面添加上分的注解，这里放上一个注解，然后它的名称是 for day order service 那同样的把这个注解也放在其他的接口层上面。


OK 放上之后，接下来我们要去改造代码了，从哪里先从他的 service 里面下手？好，我们在 service 里面打开哪一个呢？打开 my comments service OK 那这里同学们看到，我加了一些 to do 那这个 to do 就是说我们要把这一段给他用份替换掉。好，我们接下来看怎么来替换，我们往上走。这两个注解，client和 template 我们可以把它给去掉了，说拜拜再也用不到了。 OK 那接下来我们在份章节里要把它改成 item API 怎么改？那么这里首先要引入一个 service 它是 item comments service OK 这里给他用 out wire 的加进来。我们看这个 service 你看这上面已经被声明成了 think client 接下来我们只用在它的启动函数里配上一个扫包路径就可以了。


好，我们这里先继续往下看。那这几行同学们通通都不要了，接下来我们怎么办？我们只用调用它的 save 方法把 map 给它传进去。同学们看这样的代码风格体验和你直接调用一个本地的服务是不是一模一样的，但是不同之处是哪我们这个服务只是把接口层引入了进来，并没有引入它的实现类。那就像前面所说的这个实现类是委托给谁了呢？委托给了分 client 那分 client 会生成一个代理的 proxy service 用这个 proxy service 发起远程调用。


好，那咱这里已经改造完了。接下来我们看剩下的几个接口层是不是也有需要改动的地方。 my order service 这里看上去是没有呢？我们往下看，order service 这里怎么样是个重灾区怎么说重灾区朋友们你看这里有多少 today 和 fix me 非常多。 OK 那接下来我们要挨个把它改造一下。好，首先这里放到最上面，把这两个 out wire 的全部给它去掉，同时把上面这两个打开在冷宫里面关了很久了，现在可以释放出来。好，它分别是 service address service 和 item service 一个是 user 


domain 下的，一个是 item domain 下的。好，我们往下看。那这里怎么改？很简单，之前咱在尤瑞卡章节加入的所有代码统统删除掉，并且把之前我们注释掉的这个访问调用给它打开。好，就是这么简单，那这里已经改好了，再往下看。同样的方式，这两行怎么样呢？给它删掉，把这个打开。这跟之前的服务看起来一点变化都没有对不对？好，我们这个打开在接下来的 URL 也给它打开。 OK 还有没有漏掉的？这里，那我们把这一个最后一行也给它打开。


好，那我们代码级别的改动就到这里结束了，接下来我们去更改一些配置项，更看哪里呢？好，我们往下走一步到福地 order web 那这里有一个很重要的地方需要改的是哪里呢？ order application 好， order application 这里我们要添加分担。


扫包路径怎么配呢？跟之前咱在 demo 环节中写的一样，第一个是要 enable thin clients 好，它既然叫 clients 说明它有可以配置多个分的扫描路径。那咱接下来去指定 base package 那我们可以有两种方式， base package 和 base package classes 我们这里使用 base package 的方式，我这要配置两个小包路径，第一个是 com.imock 点，谁 user service 好，这是第一个。那第二个 


com.imock.item service 配置好这两个扫包路径。那我们的这个 order 微服务就能顺理成章地使用咱引入的 user API 和 item API 好，那咱这里的配置改完之后，还有一个小尾巴需要去收拾一下。
在这些 controller 里面我们看 my comments controller 好，收起小说吧，咱在这里面看，还有一个 to do 前方施工，学完份再来改造。那咱学完了，我们这里开始要动手了，怎么改？非常简单，咱把这里添加的很丑的这些代码全部给它删掉走，你那然后下面几行之前注释掉的代码给大家重获自由。
那这段代码被放出来之后怎么回事啊？时过境迁，咱这个函数是不是已经不存在了啊？在 my comments service 中找不到了，那它到哪里了呢？到 item common service 里面了？好，把这里给它复制一下，我们把接下来需要用到的 item comments service 给它引入进来，同样起名 item common service 这两个家伙怎么还在这呢？删掉删掉用不着了，斩草要除根。


好，我们走到下面，这个方法调用里的 service name 咱把它一下，替换成 item service name 好顿时怎么样呢？世界清净了。 OK 那这个 controller 改完了，还有没有其他 controller 需要改呢？同学们看这里 orders controller 我们打开看一看，这里有一个游离于三界之外的部分，哪一部分咱前面说过支付中心对不对？咱支付中心的代码其实是在另一个 RIP 里的，咱在改造过程中一直没有涉及，所以同学们可以去做一个这样的作业。


咱把支付中心改成微服之后，把它的接口层用同样的方式给它抽取出来，然后引入到 order 这一个微服务当中，把这里使用 rest template 发起调用的方式改造成通过分接口来调用的方式。除此以外，是不是大部分改动都已经改完了。 OK 那接下来还有哪里啊？还有最后一步对不对？我们要在 application YAML 这里添加上允许并重在的这一个配置项在哪里也好，就在这给它安插进去。 OK 那改到这里，这三个配置就已经算是基本完工了。那如果同学们要验证的话，那我们就按顺序启动。那先启动 user application 在 user application 启动的同时，我们选中 item application 也把它给启动起来。那老师都是在本机来测试这些部署环境的，所以它的 IP 地址都是一样的。对不对？比如说我现在转移到浏览器，再看注册中心，这里我刷新一下你这两个服务，如果在生产环境上来说，它的 IP 地址肯定是不同的，因为它会部署到不同的实例当中。


那咱在这里是本期部署，你看到它前面的 IP 地址全部都是相同的。咱在前面学过尤瑞卡的高可用对不对？咱在高可用里面是怎么配的呢？高可用里面是不是把这个 URL 配成了 host name 咱叫 PR 1p2 对不对那这个 IP 和 host name 之间的关系其实有两个隐藏的知识点。第一个隐藏知识点，同学们可以做这样一个尝试，怎么尝试呢？咱们把尤瑞卡高可用配置过程中的 pear 1 pear two 把它替换成 IP address 也就是说咱不要用 pear one pear two 来注册，而是把它替换成 IP 地址。


你注册上去看一看，这里下面这个服务列表会有什么变化？那像咱这里的双备份注册中心，如果你在 eurika 的配置文件当中开启了自己注册，那咱这里是关闭掉的。如果你开启了自动拉取注册信息以及服务注册，那么你这两个注册中心它会出现在哪里呢？它会出现在这个已注册列表当中。
当你不使用 host name 而是使用 ipig S 进行注册的时候，那咱双备份的注册中心在这个列表当中，它有时候会怎么样呢？它不仅显示在 available 的分区当中，同时也会出现在 unavailable 的分区当中。那可能大家会感到很奇怪，我怎么会同一个实例，它既出现在可用又出现在不可用呢？其实这个情况跟 IP 和 host name 有那么一点的关系，那我这里建议同学们自己去手把手的试一下，先去观察一下问题，然后再深入代码里面看一下为什么会有这样一个问题。


那咱前面在 demo 的时候也是为了避免歧义，所以采用了这种以 host name 形式来搭建的双倍份注册中心，让友瑞克可以将这两台注册中心识别为不同的实力。 OK 点到即止。那咱前面说了有两个隐藏的知识点这里说了第一个，第二个如果我想控制是通过 IP 注册还是通过它的这个 host name 注册，怎么办呢？其实在配置文件当中有这样一个属性，它叫 prefer IP address 那我们可以选择以 IP 地址注册还是 host name 注册。


那怎么办啊？在这个 instance 节点下面有这样一个配置项，它叫什么呢？ Prefer ip address. OK 这个配置项的 value 就是 true 或者 false 顾名思义，我是不是倾向于使用 IP 地址注册？那同学们其实看这里面很多配置项只是知道它怎么用，但是不知道它为什么这么用，或者说你配置不同的值。那它在整个注册中心运作过程中哪个阶段起作用啊？我建议同学们一定要深入代码去研究，研究每一个属性它的作用。如果同学们想把一个功能点一个配置项吃透，最简单的方式是什么？那就是通过代码查找一下每个配置项它都是在哪里起作用的。那比方说咱刚才说到了 prefer ipi dress 它是在哪里起作用呢？非常简单，咱 eureka instance 的配置都是隐藏在这个 bin 里面的，非常简单叫 eureka config Bee instance config Bee OK 我们进来看一下好，走到它这个 Java 类里面。那这里面有一个方法，你看它这里 configuration properties 以什么打头 eureka instance 打头。


那这里咱就找到了它的入口对不对？其实很多同学特别依赖于教程，来教大家怎么来看代码比如我需要学习 spring boat ，我总要去网上找一找有什么 spring boat 的源码导读，其实说实在的需要吗，真的没有那么大的必要，咱读代码都是有一些特定的招式套路的。


那咱开源软件都有一个特点叫什么呢？神龙见首不见尾什么意思呢？什么叫见首，什么又叫不见尾呢？这个见首意思就是说这些开源软件你要想找到一个方法起作用的入口处，那非常好找，但是出口处你可能就找不着北了。那怎么办呢？就是从入口处一点点跟进去，通过 debug 的模式走一遍，这个顺理成章，全套流程全部打通，所以真的非常非常简单。


就像咱刚才顺带提到的这一个配置项，那咱接下来 prefer iph S 怎么找呢？我们看这里面有很多的配置项，这些属性咱在这里面属性里面就很轻松的找这个 prefer IP address 在哪就可以了，看在这里是不是非常简单，那我去查找一下它都用在哪些地方。好，主要我这打眼一看主要用在哪里。
Get host name ok.


get host name 如果你 prefer IP address 那返回 IP address 否则返回谁 host name 就这么简单。所以学习一个项目框架，你只要两步，第一步，把源码下载下来。第二步怎么样呢？去从这个框架中找一个突破口，这个突破口可以是某一个核心的配置属性，也可以是某一个使框架起作用的功能。
注解。从这一个突破口下去，这就是神龙见首了。对不对？我们下去钻进去 debug 的方式，从头到尾走一遍，走两遍走三遍。不同的分支咱跟进去多来这么几遍就怎么样呢？打通任督二脉了。所以说阅读这些开源软件软码真的就是非常简单的一件事情，你只要肯花点功夫，找到正确的方法技巧，你读起来非常非常通畅。好，咱刚才开车带大家兜了一阵风，那咱现在再兜回来，前面启动的两个项目怎么样了？ user application item application 好嘞，都启动起来了。那最后一个启动谁呢？ order application 因为咱引用了 user 还有 item 的微服务，所以我们启动 order application 之后尝试调用某个方法。那看一看这个方法是否能正确的返回结果。 OK 我们稍等片刻。好，你看这里， started 没有报错，这就说明成功了一大半。那我接下来随便的调用一个服务。


好了，我调用个最简单的服务，那就他了，你 my comments control 了。那前面改动了哪个方法呢？ save list 保存评论列表的方法当中，在这里做了一个修改，在哪里修改的？ my comment service 里的 save comments 。在保存评价里面，咱调用了谁呢？ item comments 好，这是一个 order 到 item 服务的远程调用。那好嘞，我们现在转战到 postman 用一个最简单的方式，咱把这个 URL 给打上。 my comments save listsave list 当中传入一个 order ID 还有一个 user ID 那这里大家找一个 order 然后把它对应的这一个 user 的 ID 给它 copy 过来就可以了。剩下的方法那就是构造一个原始的 body 那我这里非常简单，传了一个 item ID 一个 content 还有一个什么呢？评论等级， comment level 那咱现在发起一个调用走，你很快返回了。


OK 我们先看一下 order 这里。好方法已经顺利结束，它执行了 65 秒。那咱看看 item 这里是不是接收到了调用。 OK 看到这里，同样的接收到了一个调用。到这里，我们就验证了咱前面做的微服务改造已经可以从 order 这个微服务通过粪接口这种代理调用的形式，向咱的 item 微服务当中发起一个远程方法调用。


OK 那这里同学们还要去多多注意一个小的细节，什么细节这也是同学们在微服改造过程中非常容易遗漏的地方。如果你是重新创建一个新的微服务，那未必会遗漏。但是如果你是从一个单体应用改过来，非常容易漏是哪里呢？那就是这里，同学们看到，咱这个注解还是谁还是 service 而不是 rest 看出了对不对？咱为什么写成 service 依然可以运行呢？因为咱的这个 my comments service 并没有作为一个微服务提供给其他方法调用，咱只是在订单微服务中来进行注入调用。


那如果这个 service 需要对外提供服务，就像咱的这个 item comments service 一样，如果你需要把当前的这个服务也提供给外部，这种情况下咱就不能用 at service 了，就要把它替换成 rest control 了，这是非常容易遗漏的一个地方。这里给同学们提个醒。


好注意事项。交代完毕了之后，咱这一节的内容就到这里结束了，跟同学们稍微总结一下，在这一节当中，把份注解应用到了 item user 还有 order 这三个微服务项，并且把 order 里那些非常丑的。以前遗留下来的有瑞卡代码调用全部替换成了基于接口形式的 phone 风格的方法调用。在这个过程中，我们还做了一些小科普，比如之前我们使用双倍份的注册中心做高可用架构。为什么以 PR one PR two 这种 host name 来进行服务注册。并且我们还介绍了一个配置项 prefer IP address 就是告诉大家如果想通过 IP 注册，我要怎么来改配置。


在这个过程中，我们又稍微做了那么一点引申，从这一个配置项出发，带大家看了一下阅读源码的一种，非常高效简洁容易入手的做法。所以这一节的内容是五花八门还是比较多的啦。那总结起来就一句话，微服务大法。好，同学们学完了分，改造好了商城应用。同学们现在已经是有了微服务阶段接近三成的功力了。到这里同学们总可以相信了。微服务就像老师说的真的就是这么简单的一件事情好同学们，那这一节我们就先讲到这里了，半仙老师，就先去下一章等你们啦。同学们，下章我们再见。


