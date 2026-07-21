---
title: 1-10 MariaDB - 离线安装MariaDB
---

# 1-10 MariaDB - 离线安装MariaDB

[image](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/58f4158a-bb41-4b45-9590-e8bbc0db401d/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466V7JGZXXA%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T224750Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCuR1Lpf538B%2FAk%2FCvytyU7K0Wl79oQJeiiO7MBhQ9thgIgNtfnUTp%2FxXfEIBehEBlKYuSW%2BkrA7dYvVLoINkB4OYIqiAQIxv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDK%2BF8p3SzVd1%2BNGPTCrcAyScKi6nirpJW9Lyl%2BsnknZ5vgYP9ozTC2rqZGehslGRer6BOYGQVQ%2F6rsJF7074dX8NeLmC4WPn3Kazlt%2BLcuSpg1kMz0F5JrNCAKu1FPdriciWo8Uyd19jUPdcgVti4FfmM2KzAq730cP68mx12DA3QXwWU4KHk88%2FCp7PIjUtB%2B%2BfVXP5lJ%2F2WGfprv%2Ff7vfu8zFUNzamTKh0L815fBNGotvNgEs5uy3hdOEZte0EYSU7N65aTHHSbIUVoriYm3vq4U2D5irOq6H%2B3JuNiEJJAyJXyj5uaWXGPf1F%2FGgP2L%2FpZ7S8E3gZQoLCT7RopiMpwAp%2BZUidmiBaYhtbCyKEqQ%2BK8Vjhm1Q7OiW0dZEkxNAa6yv9ZRCZH7Idif4W%2FwlraJoc3FUPl2Q3LhvtPHW5NOp%2Bj6ogfvLDKFAYqoeEMZKh%2F%2F%2FaxAKYPrDUdpakYV%2BL%2BS0Qz2q5zu%2BFJSnlL6EUNzwqW9U2bPyJAhkwIlN8EoQE3J6PwSSdVZdJJ%2F9b1GMnuGnktyey%2Bh%2FIbL157toXBFE2AnhE66NkHulxRuv9cgJegPe1Rm9IZAttCPdxzp0a5jzXnl7ihDVg1G6Twysf%2FtJOitwdF3lIwIukLuBdC3TRC%2B7efyDkcPlGMIu6%2F9IGOqUBQK0D1DqEeXc51NYngeZyCooyyf1X1Yv7PlFI9WrlAtaCu81O%2Bbw2C0xDyiU%2BxEAz6FZrKdloWvbsKPfKhUaH6R1z9t1pvSq6ewU9B9HA77I0nYWMSBb4d2iVKyACjXBNIznJicPWh1Memtkuds6TtqF6j3Ad7QxFUb1BmWYQ%2BoZz%2F7IlFM1n%2F4DO7Txwpbe2ZLqyureafq3sVoGj27DwNGNsfwSN&X-Amz-Signature=566dd07028e79d54ae7f59a99042c0b7f393cdc5920250d226a151ee9558f734&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

[https://mariadb.com/downloads/](https://mariadb.com/downloads/)

那么这几个离线的每日 d b 的安装包，当我们全部下载完毕以后，我们就可以去做一个安装了。关于这些包的话，我其实现在已经是预先的进行了一个上传，看一下，我已经是上传到了 Tom software 下，那么大家也可以事先去上传一下，上传的时候还是比较耗时的，总共是有这 7 个包。好，随后我们就可以来做一个安装了，那我们会跟着官方的文档去做。首先在这里有一个 step by step，这是一步一步的去安装的一个步骤。首先要去进行安装数据库的话，你是需要去安装它的依赖，也就是一个dependencies，有一些很多的依赖。那么在这里有一个云install，把这一条命令在这里拷贝一下，我们今天可以再放大一下，有一条这个我们直接把它拷贝以后，直接贴到你的命令行，拷贝过来做一个安装回收一下，在这里他会问你是不是要去安装，是否OK。点一下写一个 y 回收一下，那么这个时候他就可以去安装了，这个环境已经是 complete 安装成功。

[https://mariadb.com/kb/en/mariadb-installation-version-10121-via-rpms-on-centos-7/](https://mariadb.com/kb/en/mariadb-installation-version-10121-via-rpms-on-centos-7/)

[image](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/4773119a-45cb-482c-ba61-ea98089a45a8/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466V7JGZXXA%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T224750Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCuR1Lpf538B%2FAk%2FCvytyU7K0Wl79oQJeiiO7MBhQ9thgIgNtfnUTp%2FxXfEIBehEBlKYuSW%2BkrA7dYvVLoINkB4OYIqiAQIxv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDK%2BF8p3SzVd1%2BNGPTCrcAyScKi6nirpJW9Lyl%2BsnknZ5vgYP9ozTC2rqZGehslGRer6BOYGQVQ%2F6rsJF7074dX8NeLmC4WPn3Kazlt%2BLcuSpg1kMz0F5JrNCAKu1FPdriciWo8Uyd19jUPdcgVti4FfmM2KzAq730cP68mx12DA3QXwWU4KHk88%2FCp7PIjUtB%2B%2BfVXP5lJ%2F2WGfprv%2Ff7vfu8zFUNzamTKh0L815fBNGotvNgEs5uy3hdOEZte0EYSU7N65aTHHSbIUVoriYm3vq4U2D5irOq6H%2B3JuNiEJJAyJXyj5uaWXGPf1F%2FGgP2L%2FpZ7S8E3gZQoLCT7RopiMpwAp%2BZUidmiBaYhtbCyKEqQ%2BK8Vjhm1Q7OiW0dZEkxNAa6yv9ZRCZH7Idif4W%2FwlraJoc3FUPl2Q3LhvtPHW5NOp%2Bj6ogfvLDKFAYqoeEMZKh%2F%2F%2FaxAKYPrDUdpakYV%2BL%2BS0Qz2q5zu%2BFJSnlL6EUNzwqW9U2bPyJAhkwIlN8EoQE3J6PwSSdVZdJJ%2F9b1GMnuGnktyey%2Bh%2FIbL157toXBFE2AnhE66NkHulxRuv9cgJegPe1Rm9IZAttCPdxzp0a5jzXnl7ihDVg1G6Twysf%2FtJOitwdF3lIwIukLuBdC3TRC%2B7efyDkcPlGMIu6%2F9IGOqUBQK0D1DqEeXc51NYngeZyCooyyf1X1Yv7PlFI9WrlAtaCu81O%2Bbw2C0xDyiU%2BxEAz6FZrKdloWvbsKPfKhUaH6R1z9t1pvSq6ewU9B9HA77I0nYWMSBb4d2iVKyACjXBNIznJicPWh1Memtkuds6TtqF6j3Ad7QxFUb1BmWYQ%2BoZz%2F7IlFM1n%2F4DO7Txwpbe2ZLqyureafq3sVoGj27DwNGNsfwSN&X-Amz-Signature=248ace3604e05182e2448c62fdda6b583bb86a6450a05ff9f479441fd8b3c9c3&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

好，随后下一个你是需要去安装这两个，那么这两个其实都是我们刚刚所下载的，其实也就是这一项以及是这一项，我们可以这样子拷贝它的一个命令，拷贝到这个部位，然后后方的版本我们不用去加，因为后方其实这两边有两个不一样的。我们呢直接贴到咱们的命令行，贴过来之后，那么我们在这里可以看到有一个是 3. 0 的，先安装这个，那么看到 100% 安装成功，随后我们再去安装下一个，是 level 开头的，把这个命令直接一贴，按一个回车。好，OK，那么这两个包安装成功，都是 100% 好。再回到咱们的文档。123。这三步我们都已经是做完了，这是第四步。


第四步的话，其实也就是在这里最后一个步骤，通过这个r、p、m、杠、i、b、 h 去安装我们蒙瑞亚d、 b 相关的一些核心包的话，它是有按照一些相应的顺序的，第一个是common，第二个是一个compact，随后是一个gallery。在最后一个往后面看是一个server，总共是有这一些，它还有一个client，总共是有好几个包，那么这几个包我们按照它的顺序去做一个安装就可以了，在这边我们直接把这一段拷贝，然后根据它的顺序一个一个把包的内容给贴进去，那么我们推到命令行。


好，那么先来安装第一个的话，它是一个 common 包，所以我们要把 common 包给写进去，我们的 common 包是在我们这样子，我们先写一个，把它的列表先列出来，然后再把这个给拷贝。那么先安装common，也就是这个，把这个 common 给贴过来，那么这是第一个包。


好，随后再看第二个包，那么第二个包是一个combat，把 combat 再拷贝过来，找到我们的 combat 是这个，好，那么这是第二个。随后再看下一个，下一个的话是从这里一直到这里是 client 包，所以我们要去把 client 再进行一个拷贝，找到 client 在这里。


好，随后下一个，下一个是它的依赖包，我们回到文档，依赖包是一个 gallery 对吧，所以我们把这个直接拷贝一下贴过来，那么这是它的依赖包。那么还剩下最后一个就是 server 了，看一下后面就只剩下一个 server 包，那么我们再把这个给贴一下，那么在这里面总共是包含了 5 个包。


我们直接按一下回车，看一下会不会报错，按一下回车，按了回车之后你会发现其实他在这里 fail 的，他安装失败了，这是为什么呢？那么在官方的文档里面其实也有，**当你再去操作一些命令的时候，你发现了一些错误，发生了一些异常，千万不要怕，其实会有文档，有了文档之后就可以很好的去进行解决了。**

[image](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/0f0cb923-dcdd-4965-ac02-688ab3035009/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466V7JGZXXA%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T224750Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCuR1Lpf538B%2FAk%2FCvytyU7K0Wl79oQJeiiO7MBhQ9thgIgNtfnUTp%2FxXfEIBehEBlKYuSW%2BkrA7dYvVLoINkB4OYIqiAQIxv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDK%2BF8p3SzVd1%2BNGPTCrcAyScKi6nirpJW9Lyl%2BsnknZ5vgYP9ozTC2rqZGehslGRer6BOYGQVQ%2F6rsJF7074dX8NeLmC4WPn3Kazlt%2BLcuSpg1kMz0F5JrNCAKu1FPdriciWo8Uyd19jUPdcgVti4FfmM2KzAq730cP68mx12DA3QXwWU4KHk88%2FCp7PIjUtB%2B%2BfVXP5lJ%2F2WGfprv%2Ff7vfu8zFUNzamTKh0L815fBNGotvNgEs5uy3hdOEZte0EYSU7N65aTHHSbIUVoriYm3vq4U2D5irOq6H%2B3JuNiEJJAyJXyj5uaWXGPf1F%2FGgP2L%2FpZ7S8E3gZQoLCT7RopiMpwAp%2BZUidmiBaYhtbCyKEqQ%2BK8Vjhm1Q7OiW0dZEkxNAa6yv9ZRCZH7Idif4W%2FwlraJoc3FUPl2Q3LhvtPHW5NOp%2Bj6ogfvLDKFAYqoeEMZKh%2F%2F%2FaxAKYPrDUdpakYV%2BL%2BS0Qz2q5zu%2BFJSnlL6EUNzwqW9U2bPyJAhkwIlN8EoQE3J6PwSSdVZdJJ%2F9b1GMnuGnktyey%2Bh%2FIbL157toXBFE2AnhE66NkHulxRuv9cgJegPe1Rm9IZAttCPdxzp0a5jzXnl7ihDVg1G6Twysf%2FtJOitwdF3lIwIukLuBdC3TRC%2B7efyDkcPlGMIu6%2F9IGOqUBQK0D1DqEeXc51NYngeZyCooyyf1X1Yv7PlFI9WrlAtaCu81O%2Bbw2C0xDyiU%2BxEAz6FZrKdloWvbsKPfKhUaH6R1z9t1pvSq6ewU9B9HA77I0nYWMSBb4d2iVKyACjXBNIznJicPWh1Memtkuds6TtqF6j3Ad7QxFUb1BmWYQ%2BoZz%2F7IlFM1n%2F4DO7Txwpbe2ZLqyureafq3sVoGj27DwNGNsfwSN&X-Amz-Signature=a41ffd010fc34daf50ea41da475b03b56912a98ac292994d809dc68184a4a04b&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

那么首先在这里它会有一个 Mario DB lips，那么这个是一个冲突了，和我们的 compat 包冲突。我们可以来看一下官方的文档，在这里那么他说当我们正在安装我们一些相应的包的时候，它会出现一些相应的问题，比方说在这里有一个Libs，那么这个就是代表它是冲突了。如何去解决它的解决方案？在这里我们是需要去把原来的一些r，p， m 要去进行一个 remove and install，先要去做的一个步骤是先删除后安装，所以他在这里给了一个步骤，我们要先去查询一下，把这个命令拷贝一下。在我们的一个本地，它会有一个 Margp lips，它会有这样的一个包，我们要去检测一下。把这个直接拷贝贴到咱们的命令行，贴过来回收一下，你会发现在这里它列出了相应的版本号码，这就是雷克斯。这个包我们是需要去做一个移除的，移除的话怎么做？它的下方也有 remove this package，把这个包给移除，使用这个命令。


其实我们之前有讲过，在安装 JDK 的时候，如果发现你本地有一些JDK， open JDK 的话，你要去移除的话也是使用这个。把这个直接拷贝贴过来，再把这个包的名称复制到这个后方，然后注意一下这个里面会有一个空格一下，再做一个回车，那么这样子他就会把你这个包给移除，你可以再去检测一下，使用这个命令再一次的去检测，你会发现检测之后没有任何内容，所以我们是删除成功了。


OK，回到文档，那么这是我们的第一个步骤，其实你还可以再往下看的话，它还会有一些相应的内容，相应的依赖，我们是需要去做的。在这里它会有一个依赖的环境，那么这个依赖的环境是为我们 gallery 做一个准备的，也就是这个有一个叫做 boost Devil，把这个去做一个拷贝对吧，我们也是使用语音 install 去进行安装的。拷贝一下，命令推到我们自己的命令行，贴过来，回车一下。


好，那么还是一样在这边我们要选择安装，写一个yes， why 回车，好，看到 complete 就代表我们是安装成功了，总共是安装了这些内容，都是它的一些依赖。好，随后下一个再往下看，那么在这里的话它会有一个warning，有一个警告，这个警告是指我们没有做一个相应的签名，以及我们没有导入一个key，那么这个是美瑞亚 DB 所安装的时候要去提供的一个key。在这个地方有一个 solution 解决方案是说我们要去把这个 key 做一个相应的导入。那么怎么去导的话，在这里它其实也是贴了出来，有一个 IPM import，你需要把这个拷贝一下之后再贴到我们自己的命令行贴过来，那么这个就是导入美锐 DB 安装的时候的一个key，回撤一下。好，那么没有出任何问题，表示我们导入成功，回到咱们的文档。那么回过来以后再往下看的话，其实我们已经是安装好了，下面就不需要再做了。


现在的话，当我们前面的这些依赖的一些操作做完之后，我们需要回到原先的第四步，把第四步再去做一个安装对吧？回过来我们可以按一下这个键盘，箭头朝上的，在这里重新把这几个这一段内容给贴过来。总共是有 5 个包，第一个是common，第二个compact，第三个client，随后是 gallery 以及是server，总共是 5 个。好，回撤一下，那么这个时候他失败了，他报了一个错。我们在安装 client 以及是 server 的时候，是需要有一个额外的依赖包，它每一行错都是同一个依赖包，并且它是一个 64 位的，那么这个包的话其实我们可以来搜一下，我们到这个文档里面 Ctrl f 贴过来搜一下，没有搜到，那么这个其实很明显是官方文档的一个缺失。


这块内容如果说当我们在安装之前的一个版本，也就是十点四点七的时候，那么这个是不需要的，但是从十点四点八开始的时候，那么这个包我们是需要去依赖的。如何去进行一个安装，那么在文档里面其实我也已经是贴了一下，我们到文档里面去找一下，它会有一个安装包，这个包的话，那么在这里它会有一段代码，这段代码是用于做一个下载的，到这边我们直接可以贴过来，贴过来做一个下载。下载完了以后，那么我们就可以去做一个相应的安装。


这边我们可以来看一下，在这里有一个包已经是下载好了，那么如何去进行安装，在我们的文档里面也有，在这个下方还是使用这个 IPM 杠 IBX 贴一下，再把这个依赖包给贴过来。回车进行一个安装。好。OK，那么现在已经是安装成功，那么接下来我们还是一样吧，我们要安装之前的这 5 个包，回车一下，这个时候你会发现它已经是成功的，正在进行安装了。那么一个包在这里总共是有12345，有五个包执行到刚刚是100%，然后等待片刻，这个时候它内部正在做一些相应的配置。好，OK，那么没有报任何的错，当我们新的空的命令行弹出以后，就表示我们当前的马瑞亚 TB 所涉及到的相应的包全部都已经是正常的安装到我们的系统里面去了。OK？

[image](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/7f882172-30b2-4a2b-bf85-d466ef50712d/2020-09-17_205724.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466V7JGZXXA%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T224750Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCuR1Lpf538B%2FAk%2FCvytyU7K0Wl79oQJeiiO7MBhQ9thgIgNtfnUTp%2FxXfEIBehEBlKYuSW%2BkrA7dYvVLoINkB4OYIqiAQIxv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDK%2BF8p3SzVd1%2BNGPTCrcAyScKi6nirpJW9Lyl%2BsnknZ5vgYP9ozTC2rqZGehslGRer6BOYGQVQ%2F6rsJF7074dX8NeLmC4WPn3Kazlt%2BLcuSpg1kMz0F5JrNCAKu1FPdriciWo8Uyd19jUPdcgVti4FfmM2KzAq730cP68mx12DA3QXwWU4KHk88%2FCp7PIjUtB%2B%2BfVXP5lJ%2F2WGfprv%2Ff7vfu8zFUNzamTKh0L815fBNGotvNgEs5uy3hdOEZte0EYSU7N65aTHHSbIUVoriYm3vq4U2D5irOq6H%2B3JuNiEJJAyJXyj5uaWXGPf1F%2FGgP2L%2FpZ7S8E3gZQoLCT7RopiMpwAp%2BZUidmiBaYhtbCyKEqQ%2BK8Vjhm1Q7OiW0dZEkxNAa6yv9ZRCZH7Idif4W%2FwlraJoc3FUPl2Q3LhvtPHW5NOp%2Bj6ogfvLDKFAYqoeEMZKh%2F%2F%2FaxAKYPrDUdpakYV%2BL%2BS0Qz2q5zu%2BFJSnlL6EUNzwqW9U2bPyJAhkwIlN8EoQE3J6PwSSdVZdJJ%2F9b1GMnuGnktyey%2Bh%2FIbL157toXBFE2AnhE66NkHulxRuv9cgJegPe1Rm9IZAttCPdxzp0a5jzXnl7ihDVg1G6Twysf%2FtJOitwdF3lIwIukLuBdC3TRC%2B7efyDkcPlGMIu6%2F9IGOqUBQK0D1DqEeXc51NYngeZyCooyyf1X1Yv7PlFI9WrlAtaCu81O%2Bbw2C0xDyiU%2BxEAz6FZrKdloWvbsKPfKhUaH6R1z9t1pvSq6ewU9B9HA77I0nYWMSBb4d2iVKyACjXBNIznJicPWh1Memtkuds6TtqF6j3Ad7QxFUb1BmWYQ%2BoZz%2F7IlFM1n%2F4DO7Txwpbe2ZLqyureafq3sVoGj27DwNGNsfwSN&X-Amz-Signature=2f89f672387ba7d06e1ed7174749108494ee23921580c546c52fbf46bc53795c&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)


