---
title: 2-2 【快速上手Demo】Docker快速搭建
---

# 2-2 【快速上手Demo】Docker快速搭建

[image](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/442b3f4d-d350-41f7-b943-a318a07a9d82/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466Y6EBPSPO%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T225917Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCICsEYZHhPamX3ukYaykTYQhWLOh5wJ%2FJ26UWUaBXX9IdAiAymUZ7oMNYpWWURh3jwlyuvK6W4OmCszUbqpOVEx4HcSqIBAjG%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMGlYDqWVuQRJWDuprKtwDjtZyr0i4FEDM4W9cIga7nvj5mpA%2Bw1IC6pxYXfnz7d8GYggL0ITZ9OUpVzksRoXFpw6pbmi8PHH7%2BVrEms%2F0a9KiCFCMTm73%2FT%2BiPheMeRG1nj9AFa5BT8kL6orsIPj68MBFvWSPwMxXkzbhyG5K0YeT34bm8KKXIQrRuvYy%2Fgh3mDG9AsMIARnJts2zbugO%2FC6RUfqkTn4dMuhXpBNDX5djW1vKlsYc%2FmpaG6fbT0xUA%2BByWZjUeVopeqf8fDuXbbxFanBo%2FkIjJb9a21dfjBHKl1sVOdUMY6CcLnAFXHxlSOl%2FbI0PvJReGb7DvnqzRrPOZQNRHoNe%2FBfjptU4s79Q5v4nS%2FsMW6qI1gwn5VHVsD79OB2K%2B8i%2B%2B3wP8QQUiMQY%2BXZdOm5GaQGWaWuKimlWyFYR3211UUcMcmFr4TKqYl04k%2Bqdvl%2B94BZPVryeYgeWnt1cuYKqnvsYErldExndrLDog%2FBH9seA9m1wsCdiYI5ZAZnwP6nJMmNxDPi2LecppaYWSnU4I1zn6em9%2FPcK501HJag3wYtzP%2F3Uo5A9t%2B3m2ObJ6N9%2BEWoEpN%2Fn%2FmZzlSDH3JtATJve2BVCniQ7zKhIaJ42Q4RQY4eAckggjwqc57gR3wr7BbEwobj%2F0gY6pgHvhd7Kz6nBCz%2B1fRJgFCTAETIktXHWltDl9NDegcbtMA2UmylsAdfuRR0prrIV57L%2FQ7Weoo1%2BeSJA5F4h%2BN2fGf2hxhIptWdCvxcS59epmVV7hWmzQLIYjZF13njb%2BXc8p61w1v6tsrmVJsnLp%2FW%2FdY2gCI5cViL4%2BipgqmPFzPxOplwBcM3mKbdIbrvwPNpQxpK8wSdar9VPYU9utJekbbc7pROB&X-Amz-Signature=7e9b56caf49723bd962cf5543c5a0edf148e8c167aea921ff2b7a1578a6cbe24&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

[image](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/d888a3cc-1872-4698-80f9-c7ccbce43f0c/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466Y6EBPSPO%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T225917Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCICsEYZHhPamX3ukYaykTYQhWLOh5wJ%2FJ26UWUaBXX9IdAiAymUZ7oMNYpWWURh3jwlyuvK6W4OmCszUbqpOVEx4HcSqIBAjG%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMGlYDqWVuQRJWDuprKtwDjtZyr0i4FEDM4W9cIga7nvj5mpA%2Bw1IC6pxYXfnz7d8GYggL0ITZ9OUpVzksRoXFpw6pbmi8PHH7%2BVrEms%2F0a9KiCFCMTm73%2FT%2BiPheMeRG1nj9AFa5BT8kL6orsIPj68MBFvWSPwMxXkzbhyG5K0YeT34bm8KKXIQrRuvYy%2Fgh3mDG9AsMIARnJts2zbugO%2FC6RUfqkTn4dMuhXpBNDX5djW1vKlsYc%2FmpaG6fbT0xUA%2BByWZjUeVopeqf8fDuXbbxFanBo%2FkIjJb9a21dfjBHKl1sVOdUMY6CcLnAFXHxlSOl%2FbI0PvJReGb7DvnqzRrPOZQNRHoNe%2FBfjptU4s79Q5v4nS%2FsMW6qI1gwn5VHVsD79OB2K%2B8i%2B%2B3wP8QQUiMQY%2BXZdOm5GaQGWaWuKimlWyFYR3211UUcMcmFr4TKqYl04k%2Bqdvl%2B94BZPVryeYgeWnt1cuYKqnvsYErldExndrLDog%2FBH9seA9m1wsCdiYI5ZAZnwP6nJMmNxDPi2LecppaYWSnU4I1zn6em9%2FPcK501HJag3wYtzP%2F3Uo5A9t%2B3m2ObJ6N9%2BEWoEpN%2Fn%2FmZzlSDH3JtATJve2BVCniQ7zKhIaJ42Q4RQY4eAckggjwqc57gR3wr7BbEwobj%2F0gY6pgHvhd7Kz6nBCz%2B1fRJgFCTAETIktXHWltDl9NDegcbtMA2UmylsAdfuRR0prrIV57L%2FQ7Weoo1%2BeSJA5F4h%2BN2fGf2hxhIptWdCvxcS59epmVV7hWmzQLIYjZF13njb%2BXc8p61w1v6tsrmVJsnLp%2FW%2FdY2gCI5cViL4%2BipgqmPFzPxOplwBcM3mKbdIbrvwPNpQxpK8wSdar9VPYU9utJekbbc7pROB&X-Amz-Signature=b51f88e7a1f6c95c836ee5b91971597783c613d4ed67a8d9099b3f0357243753&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

上一节我们做了 Doc 的概述，那从这季节开始，我们将进入 Doc 的实战，相信所有的架构师都来自于程序员和工程师，大家都有共通的这个爱好就是什么。实战为先，学的知识学的再多，不如什么动手来试一把。那我们也一样先来实战一下 Doc 的真正的感觉。那在实战 Doc 的时候，我们回顾一下上一个大的章节容器章节。


其实我们提到了 Doc 的一些优秀的本质微小化，

[image](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/61f950b8-213e-400e-a86d-4bf5692d82f1/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466Y6EBPSPO%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T225917Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCICsEYZHhPamX3ukYaykTYQhWLOh5wJ%2FJ26UWUaBXX9IdAiAymUZ7oMNYpWWURh3jwlyuvK6W4OmCszUbqpOVEx4HcSqIBAjG%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMGlYDqWVuQRJWDuprKtwDjtZyr0i4FEDM4W9cIga7nvj5mpA%2Bw1IC6pxYXfnz7d8GYggL0ITZ9OUpVzksRoXFpw6pbmi8PHH7%2BVrEms%2F0a9KiCFCMTm73%2FT%2BiPheMeRG1nj9AFa5BT8kL6orsIPj68MBFvWSPwMxXkzbhyG5K0YeT34bm8KKXIQrRuvYy%2Fgh3mDG9AsMIARnJts2zbugO%2FC6RUfqkTn4dMuhXpBNDX5djW1vKlsYc%2FmpaG6fbT0xUA%2BByWZjUeVopeqf8fDuXbbxFanBo%2FkIjJb9a21dfjBHKl1sVOdUMY6CcLnAFXHxlSOl%2FbI0PvJReGb7DvnqzRrPOZQNRHoNe%2FBfjptU4s79Q5v4nS%2FsMW6qI1gwn5VHVsD79OB2K%2B8i%2B%2B3wP8QQUiMQY%2BXZdOm5GaQGWaWuKimlWyFYR3211UUcMcmFr4TKqYl04k%2Bqdvl%2B94BZPVryeYgeWnt1cuYKqnvsYErldExndrLDog%2FBH9seA9m1wsCdiYI5ZAZnwP6nJMmNxDPi2LecppaYWSnU4I1zn6em9%2FPcK501HJag3wYtzP%2F3Uo5A9t%2B3m2ObJ6N9%2BEWoEpN%2Fn%2FmZzlSDH3JtATJve2BVCniQ7zKhIaJ42Q4RQY4eAckggjwqc57gR3wr7BbEwobj%2F0gY6pgHvhd7Kz6nBCz%2B1fRJgFCTAETIktXHWltDl9NDegcbtMA2UmylsAdfuRR0prrIV57L%2FQ7Weoo1%2BeSJA5F4h%2BN2fGf2hxhIptWdCvxcS59epmVV7hWmzQLIYjZF13njb%2BXc8p61w1v6tsrmVJsnLp%2FW%2FdY2gCI5cViL4%2BipgqmPFzPxOplwBcM3mKbdIbrvwPNpQxpK8wSdar9VPYU9utJekbbc7pROB&X-Amz-Signature=75726079b55448517da4f511ed61f802d77c95be03f180b4e8194d35b445c143&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

是不是就是所有的镜像都非常小，所以我们基于很小的镜像几兆几 K 的镜像来启动。那同时 Doc 的启和停管理都非常快捷，以秒为单位，最多也就个把分钟的时间就能完成什么正常业务的启停应用的这种处理增删改查实际的生产过程当中所有的变化对不对？那我们会以三个实例感受一下不同复杂度的实例当中， Doc 是怎么样进行快速启停，怎么样进行快速下载的。
那除此以外， Doc 是一个集装箱，它是有一个标准化的，不管你是需要这种键值，对缓存服务，还是需要数据库服务还是反向代理服，你都能找到一个很通用的这样一个环境，基于这样一个环境进行少量的改变来符合你的这个业务需求。那我们也会这样以三个不同的业务场景。
第一个业务场景是说 hello 对吧，这是所有这个加班工程师第一个上手起步的这件事情，写个 hello world 那我们 Doc 也一样，

[image](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/de37a93a-1700-44d8-a682-a3386647b714/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466Y6EBPSPO%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T225917Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCICsEYZHhPamX3ukYaykTYQhWLOh5wJ%2FJ26UWUaBXX9IdAiAymUZ7oMNYpWWURh3jwlyuvK6W4OmCszUbqpOVEx4HcSqIBAjG%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMGlYDqWVuQRJWDuprKtwDjtZyr0i4FEDM4W9cIga7nvj5mpA%2Bw1IC6pxYXfnz7d8GYggL0ITZ9OUpVzksRoXFpw6pbmi8PHH7%2BVrEms%2F0a9KiCFCMTm73%2FT%2BiPheMeRG1nj9AFa5BT8kL6orsIPj68MBFvWSPwMxXkzbhyG5K0YeT34bm8KKXIQrRuvYy%2Fgh3mDG9AsMIARnJts2zbugO%2FC6RUfqkTn4dMuhXpBNDX5djW1vKlsYc%2FmpaG6fbT0xUA%2BByWZjUeVopeqf8fDuXbbxFanBo%2FkIjJb9a21dfjBHKl1sVOdUMY6CcLnAFXHxlSOl%2FbI0PvJReGb7DvnqzRrPOZQNRHoNe%2FBfjptU4s79Q5v4nS%2FsMW6qI1gwn5VHVsD79OB2K%2B8i%2B%2B3wP8QQUiMQY%2BXZdOm5GaQGWaWuKimlWyFYR3211UUcMcmFr4TKqYl04k%2Bqdvl%2B94BZPVryeYgeWnt1cuYKqnvsYErldExndrLDog%2FBH9seA9m1wsCdiYI5ZAZnwP6nJMmNxDPi2LecppaYWSnU4I1zn6em9%2FPcK501HJag3wYtzP%2F3Uo5A9t%2B3m2ObJ6N9%2BEWoEpN%2Fn%2FmZzlSDH3JtATJve2BVCniQ7zKhIaJ42Q4RQY4eAckggjwqc57gR3wr7BbEwobj%2F0gY6pgHvhd7Kz6nBCz%2B1fRJgFCTAETIktXHWltDl9NDegcbtMA2UmylsAdfuRR0prrIV57L%2FQ7Weoo1%2BeSJA5F4h%2BN2fGf2hxhIptWdCvxcS59epmVV7hWmzQLIYjZF13njb%2BXc8p61w1v6tsrmVJsnLp%2FW%2FdY2gCI5cViL4%2BipgqmPFzPxOplwBcM3mKbdIbrvwPNpQxpK8wSdar9VPYU9utJekbbc7pROB&X-Amz-Signature=a8cbb115f74e1d9dfffa51696b75b72c864e9a22f5cee639e365ec8cca6d181d&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

给大家展示一下一个 hello 的容器只会说 hello 的容器。那第二个任务是我们会尝试去运行一个高速的舰支队服务 Redis 那这个舰只对就可以在内存里面运行取一个键和值的读写的功能。那我们会尝试给这个 Redis 里面 set 一些键值的内容，从中再读取出来。那第三个任务就是我们尝试运行一个 web 服务器安静克斯反向代理。
通过这个安静克斯跟大家说一声 welcome 好不好？这样三个 demo 我们会快小在标准化这三个角度，给大家感觉一下 Doc 是怎么样很快速的运行起来的？好，我们回到这个运行环境，这个环境我已经把 doctor 迪蒙和他的那个 command line 安装好了，我们看一下 doctor 的这个迪蒙和 command 安装完以后，我们就可以运行 Doc 的命令了。 Doc PS 查询一下当前没有任何容器，PS就是在 Linux 里面查进程，这是在 Doc 后面的查容器。有没有当前运行的容器没有另外一个命令，Doc image 看一下 Doc 下面有多少的 image 已经被下载了，也没有很干净的一个环境。
好，我们对这个环境尝试做第一件事情，起一个 hello world 大家可以想象一下起 hello world 一般是什么样过程，下载代码编译测试运行、查看状态这样一些事情。那实际 Docker 过程当中就一个命令， Docker run 我们希望跑什么，你就说一声我要跑什么就好了。所有这些过程会全自动的在 Doc 里自动的被运行到。那我们希望跑一个 hello world 很简单的，你说 Docker run hello world 就可以了。
好，我们看一下跑的结果如何，它会尝试从本地直接去找这样一个 image 找不到，它就会从网上去破的过程当中，它一层一层的我们可以看到它很快就刷过了，就是它一层一层的下载。因为 hello world 非常小，他只要在第一层的 image 里面就已经下载完成了。那下载完成以后，他就会在整个过程当中打一个行字， hello from Doc 这就是整个 hello world 要干的事情。他说完这句话，自动就退出历史舞台，也就是说他所有的任务完成了。那我们来看一下效果怎么样。
Doc PS 你可以看到了吗？如刚刚所说的，只要他这个 Doc 说完这个 hello world 以后，它就自动退出了，所以根本就查询不到这样一个占用 CPU 内存的这个容器的存在。但是我们可以用 Doc PS 杠 A 查询曾经存留过的容器以及这个容器所有的这种运行状态的一些结果。
你可以看到什么？ hello world 这个 images 曾经在我们的这个环境当中运行过，它的容器名叫这个。那它当前状态是什么样的？当前状态是 exit 退出了的，就已经退出历史舞台了。对不对？这样一个非常快捷的起停打印一段话，在我们的终端界面完成任务。还有还包含内部偷偷的去下载一个对不对？我们从这个 [doc.io](http://doc.io/) 或者是docker.hum ，他这里是找的是 [docker.com](http://docker.com/) [hub.docker.com](http://hub.docker.com/) 的网上去下载了这样一个镜像。那这整个过程全自动，而且是秒击完成，我们来感受一下另外一个标准化的服务。


好吧，我们去下载一个 Redis a Redis 下载过程当中我们也不需要说下载，我们只要去说要 run 要以什么样形式run ，这次我们希望 Redis 是一个后台的进程，它会以一个 demo 的形式运行起来。它的 run 后面加了一个杠 D 然后就是我们的 Redis 同时我们希望指定某一个版本，就它有一个在下载过程当中，可以通过一个 tag 指定它的 pitch 的版本号，那我们这里希望下载一个叫 3.2 的版本。那下载完以后，我也希望 Redis 是以一个 server 的形式能够运行起来。那为什么说要加一个 server 呢？因为只有加了这个 server 以后它才是什么会是一个启动进程的过程。如果你没有加一个 ready server ，它只是下载完了整个这个容器的运行起来了，但是它的主进程并没有运行起来，这样你就没法通过 command line 跟它进行交互。


好我们来看一下它还是尝试从我们本地去找这样一个 image 没有它从网上去下载，因为我们连接的是什么是 [doc.com](http://doc.com/) 所以整个过程会稍微慢一些。如果我们把目标指向什么，比如像阿里的镜像、时速云的镜像，那些就是代理服务器，会更快。也已经下载完了，我们看一下。


Doc PS 看一下看到没有容器的短名。在这里下载完成的时候，它会告诉你一个容器的长名，你可以用长名代表这个容器的 ID 做任何操作。那同时你也可以用一个短名，相对来说短名好记在命令行输出的过程当中，它也不会太长太占空间，所以我们优选短名。那同时 Doc PS 也告诉我们什么，它已经跑起来了，而且跑起来 5 秒钟了，是不是很快非常快的下载，非常快的运行，同时它的状态已经可以正常的交互了。那我们怎么去跟已经运行在后台的 Doc demo 进行交互呢？用 Doc exact 去跑一个命令。那这个命令过程当中希望是跟终端有交互的，就是杠 it 那表示跟终端有交互，然后就指定我们刚刚的那个短名，然后后面跟我们希望交互的什么呢？如果你后面写的是 bash 那就是用 best 形式跟他交互。
我们这里用 Redis 的那 cri 进行交互好不好？好回车看到大箭头了吗？那个箭头表示什么？我们已经跟他用一个命令行方式进行了沟通。现在我们可以解释那个 Redis 命令了，常见命令有什么呢？ S 一个 key 假设我们查一个舰只。对，这个键叫 name 我们看有没有没有。好吧，我们查一个颜色有没有也没有。那我们可以通过什么 set key 跟 value 它都有提示，比如说 set key value 的形式展现。比如我把我的名字张飞扬 set 进去 set name kesh name value 了。张飞扬同时我们 set 一个 color 好不好？我是比较喜欢 blue 的，所以我们 set 一个颜色叫 blueset color 空格 blue 好，set完了我们看一下能不能拿到我的名字 get name 已经有了，刚刚是没有是吧，现在我们 set 完了就有了，那我们可以不可以拿到我喜欢的颜色呢？ get color 也能拿到。


那这个 demo 其实就做完了，我们退出 commander 来，然后再看一下我们退出 commander 会不会影响 Doc 容器运行呢？不会，因为他还在那里，他已经运行了，两分钟了他还是 ready3.2 这样一个 image 拉出来的容器，它的名称也没有变化。因为它是一个 demo 的容器，所以它可以很方便的跟终端用户进行交互，很方便能够接受外面的这个业务请求是吧，对它进行响应。


好，那我们进入第三个小 demo 的环节。好吧，尝试去运行一个 endyx 然后我们从网页上去访问它。那一样的，我们 Doc wrong 以 demo 的形式，这个 endings 是一个 demo 是要长期运行的。那这里有一个稍微的区别，就是我们要以网易形式对外输出，所以需要有在什么？对服务器上面有占用一个端口，我们占用服务器端口是80。那同时把这个端零端口映射到映射到容器里面的这个 NGINX 的服务器的业务端口也是80。然后我们指定需要起的什么 NGINX 这里我们不指定版本号了，那它就会自动去下载一个 latest 版本的 tag 的这样一个 NGINX 从我们的 [doc.com](http://doc.com/) 上下载。


好下载。下载第一步当然也是尝试从本地去找 image 没有找到他就开始从我们的 [docker.com](http://docker.com/) 的 library 目录底下去找这样一个 endings 同时他会去尝试找那最新的 latest 那这个过程会稍微有点长，因为那个 angst 比 Redis 要大一些，同时也不像 hello world 这样的，是一个非常非常小几 K 几的，它到了兆七几十兆起是有一个过程。等它下载完以后，我们来比较一下这三个 image 不同的尺寸，不同的感觉，用哪个命令呢？ Docker image 来比较一下，那我们安心的等待一下它的下载。


接下来过程它是分几层的，你可以看到第一层就是 NX 最底层是这样一个层，那这个层没有下载完的过程当中，它却把它上一层下载完了，也把它的上层下载完了。那这就是 Doc image 后面的所有的这个镜像章节里，我们会详细讲的就是容器下载的时候，每层是可以独立下载独立管理的。那在整个容器真正运行起来时候，它会把镜像这些层层堆叠起来，就像搭积木一样，每个积木的模块你可以单独的购买。但是在搭建过程当中，你会按顺序进行搭建。那最后在这顶上一层会搭建一个可读写层，这样就实现了从镜像到容器的转变，从一个静态状态到一个运行时状态的转变。这里可以看到已经快下载完成了。那下载完成以后，它也会在这个打印过程当中会提示你说我层层堆叠完成了，最后的容器起来了，待会我们看一下它是怎么样展示这样一个堆叠的完成的过程的。好还有几十 K 几百 K 的下载。


好，全部下载完成可以看到什么？它这里有个消化，就是我做了一个哈市，我认为我前面的所有队列完成，然后它会提示个状态，我所有的页面就下载完成。然后这也会告诉你说我真正启动的这个容器是这样的，你这个容器里面除了上面的 image 以外，会自动的增加一层容易器的可读写层。


我们用 Docker PS 命令来查询一下，应该有两个在运行了，对不对？刚刚这个 Redis 这是它的镜像， Redis 它的 content name 是这个没有改变。在这个基础上，我们起另外一个 image 叫 endings 他的那个 container ID 是这个。为什么这个会比刚刚下载的慢呢？我们用 Docker images 看一下这几个 image 的大小。好，最早下载的 hello world 它的 image 有多大呢？一点几 K 对不对？输入容器可以做得很小，非常非常微小。那它的 tag 它自动就是 latest 而 Redis 我们下载的它是几十兆的一个大小。那它的 tag 是我们指定的 3.2 版本，NGINX我没有指定，所以它是 latest 下载时间有点长是因为什么它有 100 多兆的空间。这就是我们刚刚说的通常一个应用在容器上起来是 K 几十 K 几百 K 几兆几十兆几百兆千万不要到 G G 就太大了，可能你的微服务就没有改造足够好，或者你下载的这个就是镜像源。比如你想起这个业务的基础的这个镜像选太大了，你可以找一个更合适你的镜像来进行运行。


好，我们来看一下实际的运行结果，切换到这个网页，因为它已经在 80 端口提供作为服务了，我已经提前把这个 IP 地址输入到我们这个网页里面了。所以我们现在要做的是什么呢？是按一个回撤看一下 default 这个 hdp 防版灯可不可以啊？ welcome to end 是吧，已经正常运行了，那这个输完地址以后它会自动对吧？浏览器会补存什么 HTTP 冒号了？霸凌端口就证明我们这个 entences 服务也能够正常的运行起来了。
整个过程当中大家再回顾一下，我们起了哪三个应用呢？我们先起了一个 hello world 它是一个临时打印的任务，所以它没有 demo 所以它完成以后自动退出了。然后我们起了一个指定版本的 Redis 通过一个 Redis command line 跟它进行交互。


最后我们启动了一个比较大的 endings 服务，把它的容器的 80 端口的那个应用映射到了我们服务器的 80 端口，所以我用服务器的 IP 地址和 80 端口就能正常的访问 NGINX 了。这三个 demo 其实给大家感受一下它是什么？容器是相对微小的，是非常之快速的，同时也是一个很标准的是吧。你可以找到 hello world 做进行剪裁，你也可以在 engine 上进行定制化。后面的章节我们会从整个 Doc 的基本的框架、它的功能以及它怎么样制作镜像，怎么样去管理端口，怎么样去管理视角化层。当全部做完以后，大家再回过头来看看其实发现什么。
engaging Redis 其实我们刚刚操作并不完整，我们并没有跟持有化对接，并没有做复杂的端口映射，但是这三个 demo 足以给他以自信，我们可以很快的上手我们的 Doc 对不对？这也就到此结束，敬请大家期待后面整体架构和功能模块来沟通。


