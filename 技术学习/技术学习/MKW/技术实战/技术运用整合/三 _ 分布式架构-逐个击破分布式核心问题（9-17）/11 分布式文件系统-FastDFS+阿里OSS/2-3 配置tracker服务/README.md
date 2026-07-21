---
title: 2-3 配置tracker服务
---

# 2-3 配置tracker服务

[image](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/01122995-d2bc-41bb-9150-57f81abdc636/SCR-20240806-imjc.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666SF5BCHI%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T225221Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIAqCD1klq056%2BVn9hj9kr28%2FI8mlH0HPlLdUJQsDAolMAiEA0E97rjMvtvY2Kv%2BkC683wcKndTwaPLQLqDi7FF6iBAAqiAQIxv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDI47CbCFYjXm8V%2BM0yrcA5Lm9fwv6qq2n2R3fgAzZT%2FmtQ%2FI7bvV3F2hf5dDEOOLUFVf1euOUPgnjwooebBBrbGH1w05bUaZ8XhiB8rfX4Yc2XU1v4%2Bu%2F4cjLYi6iN2zPgCO93rC1AEZPy9qMgKKTxfrief%2FqNIVdnTG57tZaWfljwZKrcc9P0rgKef%2BLviAwju0bJYuy%2BYQAovBmFBtKEh%2B%2FGibeCHWln641Zg07OdVsRYT3JD%2FNlYoRdbtx7DgAqwvBsSlJggngpSB3EpzQ1gpgw0bdRrKSaesbk8Xs3rq%2BgzsT3vkTbJMJhlfqGnnfljynDgHc2DqOBe72V%2B5moD1qKBINcpY%2FcBRl92frLOh4daOiQCKdTC7xpv%2BRT%2Fhqc1c7RLsrVd7u2GHuL8%2FpQ83CeVBqCTWdH7YHIAFppHmP%2FTkrMRa4eOPtBH1Jbo52tWci0KbK%2FulIptzmz2zqY2oyn4B16SPqhjd9Hz%2BHuZeKbrq2o32v1FNbJt8K0UTPVSrF5DY0ElDqQUC5Vo33%2FzSPS0SZW7XCGC49wIPZCPX1wPcnAY1h0cRbb3hli8pATL4eOamBZxUc%2B2CKok986Kc3vvJzJQ9M5p%2FZn%2FCAWMjhE%2FtGtiDsKptIYae105FqA6w7bj2Cxz71GWoMMW6%2F9IGOqUBET6OV%2BJJK7ZUjbG4IlOxadhyxlZtdIX5ZG%2BpP7PtrxMPjiWYfwvXDyubQBVZWusXX7Rr6q%2FUhV%2FlrD%2BcDli%2FZg7x5ssJCWEH52HBSJ8so%2FcHBf38DIYuBMzAxvpYLJWpgV2HfurlaB8gVeoNOGW%2FDMvwFSvAf3sAjLsP1EZl8s4C92xU0J%2BYhq4P8tpsIf5rgEoVeW8%2BkQExH8Pkt61Kb6v58Joq&X-Amz-Signature=f744f68f5263eb2f829c01f143db58dc0f8f336523b71ce2aa0ee312d98df7b2&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

那么上一节课我们是配置了 fast GFS 的一些基本的环境准备工作，我们都去做了一下，然后我们的这个准备工作你是需要在tracker，也就是 storage 上都要去做。那么我相信大家已经是在 storage 上也去做了一下，OK，好，随后接下来下一步这个时候我们要去配置一下咱们的checker，我们把当前 tracker 服务去做一个相应的配置，以及是一个启动。


OK，好，然后我们来看一下，首先我们进入到 etc 下 f d f s 进入一下来看一下，在这里面是包含了一些相应的内容，那么虽然我们在 Tracker 和 storage 上，我们刚刚在之前所做的两次准备用作其实都是一样的，那么我们在安装的时候又是同一个 faster DFS 的一个本体，对吧？那么我们如何去区分到底是 Tracker 还是storage？主要是根据它的一个配置文件。那么在这个里面其实是有 tracker 点config，所以我们只需要去修改这个配置文件，随后我们再去通过这个配置文件加载去启动当前这一台节点，那么它就是一个 tracker 服务了。同理 storage 其实也是同样的一个道理。OK，好，随后我们在这边去做一个修改，我们修改这个Tracker，点 configure 这个文件。


好，打开进来看一下，首先有一个port，那么这个 port 的话是它 Tracker 的一个地址，那么这个大家要记住，我们在整合到咱们的项目里面去的时候，这个端口号是需要去用的。在这里的话我们配置成它的一个默认的就可以了，我们不需要去改，不需要去动。


另外在这里有一个 bond address，这个就是和你的一个当前一个计算机节点的一个 IP 地址可以去做一个绑定。那么保持为空，相当于是我们在曾经所写的一个叫做0.0.0.0，这是同样的一个道理。往下面看，有些地方我们是需要去做修改的。其中在这里有一个叫做 base pass，那么这个地址的话是主要用于去 store data and log up，也就是用于去存一些数据文件以及是一些日志文件的。那么这个是他 Tracker 服务的一个工作空间，所以我在这里去做一个修改，在这边我使用这个user，然后来一个local，再来一个 fast d f s 拉一个斜杠check，我会使用这个地址作为咱们的一个 base pass。OK，然后我把这个拷贝一下，我先保存。那么当前这个目录其实是不存在的，所以 MKDIR 把它去做一个创建杠p，那么这个是可以把这后面的一些文件夹做递归的创建。


回车一下，随后我们再来进来，再进来的话那么在这里面，其实当前我们这里面的一些配置文件，有兴趣可以去看一下，因为它里面本身就包含了一些相应的一些英文的注释。那么目前的话我们只需要配置这样的一个 base pass。比如在这里我们只需要去配置一下这个 base pass，就已经是配置成功了。那么随后我们就只需要去启动一下咱们当前这个 track 这个服务就行了。那么如何去启动呢？我们使用这个 user 下，然后我们会有一个 bin 目录，使用 F DFS，然后有一个tract，那么这个就是它启动 tracker 服务的一个名称，使用这个去进行一个启动。


然后启动的时候，那么你是需要去把它当前的一个配置文件给加进去的，那么当前配置文件就叫做这个名称，这样子我喜欢用它完全的一个路径去做一个配置。那么这样子的话，你在任何的一个路径下都可以去做，然后呢？ e g c 下 f d， f s 然后 Tracker 点configure，使用这个命令去启动你的Tracker，那么这样子一旦启动以后，那么我们的 Tracker 服务其实就已经是使用成功之后，我们可以回车一下，回车之后，然后我们就可以去看一下它的一个进程。 PS 杠 e f，然后看一下我们的 fast UFS 的一个tracker。OK，那么在这里的话我们就多了一个 track 的这样的一个服务，那么这样子我们 track 其实就已经是启动成功了。OK。

[image](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/8029cfa3-d965-4a0d-884d-5a7d36b65077/2020-09-17_174111.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666SF5BCHI%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T225221Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIAqCD1klq056%2BVn9hj9kr28%2FI8mlH0HPlLdUJQsDAolMAiEA0E97rjMvtvY2Kv%2BkC683wcKndTwaPLQLqDi7FF6iBAAqiAQIxv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDI47CbCFYjXm8V%2BM0yrcA5Lm9fwv6qq2n2R3fgAzZT%2FmtQ%2FI7bvV3F2hf5dDEOOLUFVf1euOUPgnjwooebBBrbGH1w05bUaZ8XhiB8rfX4Yc2XU1v4%2Bu%2F4cjLYi6iN2zPgCO93rC1AEZPy9qMgKKTxfrief%2FqNIVdnTG57tZaWfljwZKrcc9P0rgKef%2BLviAwju0bJYuy%2BYQAovBmFBtKEh%2B%2FGibeCHWln641Zg07OdVsRYT3JD%2FNlYoRdbtx7DgAqwvBsSlJggngpSB3EpzQ1gpgw0bdRrKSaesbk8Xs3rq%2BgzsT3vkTbJMJhlfqGnnfljynDgHc2DqOBe72V%2B5moD1qKBINcpY%2FcBRl92frLOh4daOiQCKdTC7xpv%2BRT%2Fhqc1c7RLsrVd7u2GHuL8%2FpQ83CeVBqCTWdH7YHIAFppHmP%2FTkrMRa4eOPtBH1Jbo52tWci0KbK%2FulIptzmz2zqY2oyn4B16SPqhjd9Hz%2BHuZeKbrq2o32v1FNbJt8K0UTPVSrF5DY0ElDqQUC5Vo33%2FzSPS0SZW7XCGC49wIPZCPX1wPcnAY1h0cRbb3hli8pATL4eOamBZxUc%2B2CKok986Kc3vvJzJQ9M5p%2FZn%2FCAWMjhE%2FtGtiDsKptIYae105FqA6w7bj2Cxz71GWoMMW6%2F9IGOqUBET6OV%2BJJK7ZUjbG4IlOxadhyxlZtdIX5ZG%2BpP7PtrxMPjiWYfwvXDyubQBVZWusXX7Rr6q%2FUhV%2FlrD%2BcDli%2FZg7x5ssJCWEH52HBSJ8so%2FcHBf38DIYuBMzAxvpYLJWpgV2HfurlaB8gVeoNOGW%2FDMvwFSvAf3sAjLsP1EZl8s4C92xU0J%2BYhq4P8tpsIf5rgEoVeW8%2BkQExH8Pkt61Kb6v58Joq&X-Amz-Signature=599e582853cf6d90d5a0776ecd2dc6738e8e3343ea156f3011bf2b214764c0b2&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)


