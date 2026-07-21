---
title: 2-10 远程连接2-基于JMX实现远程
---

# 2-10 远程连接2-基于JMX实现远程

[image](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/df3afb66-3bd7-4dfd-9f2a-c9f66407de50/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466Q63B52UF%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T230148Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIBqU2803IGTyokFj8lcgSoX582sXBJVmuDxg2Xa%2FjbUyAiEApFU7S20UZk%2FAo8l0pqrGSvzfoEUEg5Di90gES5bBrS0qiAQIxv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDJyfs9L3nh1gKoHxOSrcA7Z6RwCETZ4l3MWDNi8pjjNuUtjFpnSoABrXxN4tkhpbGShc93HFr3pPP9Ltf1pMaMN76uxrpe9PxS0Lh5HBz%2BwcgCY8dFcf1pYCjV0xoZ7iK6sz2PpexP0LGx3%2BDYLV44%2FZDc9BNkP7L8vCuoU3paZXZajyYZpV8tEBaOWrxW840uYeegSMcEzZav4ZvyiBtGycyH5L2%2F%2F34fkCUHjxL5ogLgY%2BmvjcwTngKCo3MnK3kE5l7LMO40XJCTKzjEcd2m5z0JCvComxflrJ0HoYoc4hqiDhUKxeZzqx3IdTX9xCSqlQ3kPQJNyugqGZScm9mQwt9fJQuAl%2BjslL%2FOkb07rhhv0F%2BhTq0VUjyVUjq8HBk9MTzAmq0wTqSNe0iqkUESfpBvtk15zsysav6NLQ4L2lisgOAg5RJ6KVPxpBci1xtQRK%2F1r%2F7jRRAmn6CBp85DA%2Bs9i3A5BSIO0BMQoKtQioHFNQJTMr2ZBjcfX9pWYDKmkieNIYDLjVzDepXpDSfTpWFKppglfOx7VeMTS50eS672EUf5Ucb98jL4m4vZ31mUcMZlD%2BYgk0xYW3AcRYfnJ8CYa65Dl7V9Kax6lLh3IRho%2BmwMJPfPzlNkLFJ2TMecG7xAWXl6udaa5TMNy3%2F9IGOqUBqF%2FAWPiHZz0WojqLTGNuUrp9hwcUiFPWos0LiKzn773jyDY%2FZuKd4Hn0h52tEvt%2BOnWFrQHspkursDmGkqORzKfyxzh4Qqo7BE47XrL38KCFEVWewSxJdWS8f8s3AdjfwGVKOFRx2a04VeunvohJiXA7k9P2S%2B1ctwRaIksT%2FD%2F7xAqWpU2l9HEP%2Fa9gz7HmopiWfx6oxVUaXKR%2F9eBmgAfH%2B31e&X-Amz-Signature=1d75bd49c6141c146a7c1550e1bcc7b8b51296063804821cb48cf15ccf7349b3&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

[image](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/c033c8aa-7878-4743-b857-3a371c2eec00/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466Q63B52UF%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T230148Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIBqU2803IGTyokFj8lcgSoX582sXBJVmuDxg2Xa%2FjbUyAiEApFU7S20UZk%2FAo8l0pqrGSvzfoEUEg5Di90gES5bBrS0qiAQIxv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDJyfs9L3nh1gKoHxOSrcA7Z6RwCETZ4l3MWDNi8pjjNuUtjFpnSoABrXxN4tkhpbGShc93HFr3pPP9Ltf1pMaMN76uxrpe9PxS0Lh5HBz%2BwcgCY8dFcf1pYCjV0xoZ7iK6sz2PpexP0LGx3%2BDYLV44%2FZDc9BNkP7L8vCuoU3paZXZajyYZpV8tEBaOWrxW840uYeegSMcEzZav4ZvyiBtGycyH5L2%2F%2F34fkCUHjxL5ogLgY%2BmvjcwTngKCo3MnK3kE5l7LMO40XJCTKzjEcd2m5z0JCvComxflrJ0HoYoc4hqiDhUKxeZzqx3IdTX9xCSqlQ3kPQJNyugqGZScm9mQwt9fJQuAl%2BjslL%2FOkb07rhhv0F%2BhTq0VUjyVUjq8HBk9MTzAmq0wTqSNe0iqkUESfpBvtk15zsysav6NLQ4L2lisgOAg5RJ6KVPxpBci1xtQRK%2F1r%2F7jRRAmn6CBp85DA%2Bs9i3A5BSIO0BMQoKtQioHFNQJTMr2ZBjcfX9pWYDKmkieNIYDLjVzDepXpDSfTpWFKppglfOx7VeMTS50eS672EUf5Ucb98jL4m4vZ31mUcMZlD%2BYgk0xYW3AcRYfnJ8CYa65Dl7V9Kax6lLh3IRho%2BmwMJPfPzlNkLFJ2TMecG7xAWXl6udaa5TMNy3%2F9IGOqUBqF%2FAWPiHZz0WojqLTGNuUrp9hwcUiFPWos0LiKzn773jyDY%2FZuKd4Hn0h52tEvt%2BOnWFrQHspkursDmGkqORzKfyxzh4Qqo7BE47XrL38KCFEVWewSxJdWS8f8s3AdjfwGVKOFRx2a04VeunvohJiXA7k9P2S%2B1ctwRaIksT%2FD%2F7xAqWpU2l9HEP%2Fa9gz7HmopiWfx6oxVUaXKR%2F9eBmgAfH%2B31e&X-Amz-Signature=747d162e690acd8e488824efdb8643a29a268ef1ff8afffcf66d3d9c85218dd5&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

下面来探讨如何。基于 GMX 实现远程连接。有很多的姿势，我们来逐个探讨。先来探讨匿名访问的模式，这种模式下需要远程应用。在启动的时候添加这 5 个参数。我们先 copy 把服务器上的 59579 进程先停掉， 579 粘贴命令，再跟上下包去重启一下应用。每个参数表达的含义，同学们也可以看一下。


启动完应用之后也是配置防火墙规则。由于这里我们已经使用 RMI port 指定了 RMI 的通信端口，所以我们只需要开放 1232 端口以及 1240 端口就 OK 了。 copy 新开一个窗口，粘贴同理开放 1240 端口。再使用 Reload 重载一下防火墙规则。


最后用 Easter pots 查看一下端口是不是确实开放好了？12401232，假设你的项目没有去人工指定 r m i port，也会使用一个随机端口。这样你也得用 net state a n t p 去拿到指定技能所使用的端口，把这些端口全部开放掉。和前面的 j state d 基本上是一样的。开发完成之后就可以远程连接了。我们依然使用 visual VM 来玩儿bin。


打开 V10 VM，点击 file add GMAX connection。在这里 connection 的格式是这样子的我们写上3W，点 it match . com 1232 就 OK 了。然后勾选 do not require SSL connection。这是因为在目前这个例子里面，我们把 SSL 给关闭掉了。点击OK，可以看到已经连接上了。


双击打开，现在 sampler 里面 CPU 和 memory 都可以正常使用了。对于远程连接，我们依然没有办法使用 which of m 去实现profile。回到手机，目前来说，我们使用了authenticate，等于 force 强行关闭了 GMX 的用户认证。这种匿名访问的方式对于生产环境来说是不够安全的。下面我们就来看一下如何为 g m x 开启用户登录认证。首先需要准备一个账号文件，名字可以随便起。这里我们叫做 g m x remote。 access 内容写成这样子，其中的 admin 就是你所设置的账号， read write 则是这个账号所拥有的权限。我们来处理一下copy。把目录切换到 test 目录，创建一个文件叫 j m x remote，点access，爱粘贴。需要再创建一个文件，名称也是随意。内容是这种格式， admin 表示账号， admin 123 则是 admin 账号的密码。我们 happy 创建一个文件 j n m x remote password， i 粘贴。


创建好 password 这个文件之后，我们需要设置账号和密码文件的权限，注意权限一定要设成600，你设置成 777 或者是 755 之类的是不行的。这样准备工作就完成了。之后在启动应用的时候把 authenticate 设成true，然后用 access file 去指定我们的账号文件。 password file 去指定我们的密码文件。启动应用就可以开启用户登录认证了。我们 copy 切换到tab，把之前的应用给停掉，粘贴，跟上价包的名称输入回车，启动应用，切换到 VCVM 界面。这个时候我们发现之前的连接已经断开了。


点击 file add gmax connection 3 w 点 Itmash . com 冒号 1232 账号 admin 密码 admin 123。你可以保存密码，也可以不保存，我们就保存一下。yes，可以发现已经连上了，双击可以看到，使用也没有问题。


回到手机。 GMX 还支持开启SSL，这样可以进一步的提升安全性。开启 SSL 的步骤稍微有点多，不过我把手机搞成手把手的了，下面我们一起来操作一下。首先第一步需要生成 Wechat VM 的 key store 命令，里面的坚括号都是变量，你在实际项目里面使用的时候，一定要把这里的坚括号替换成你希望的值。这里为了节约课上的时间，我已经事先填好了这些值。所以我们就可以 copy 到服务器里面粘贴。我们也在 test 目录里面去创建粘贴。查查目录可以看到现在生成了一个叫 visual VM Keystore 的文件。


第二步导出 cert 文件 copy 粘贴。又创建了一个 Visham third 的文件。第三步甚至 trust store copy 粘贴。第四步生成 Java 应用的 key store， kiss 的就是给我们的价包去使用的。第5步导出加白应用的cert，这个文件也是给我们价包去使用的粘贴。第六步，把 shirt 文件导入到 trust store 里面 happy 粘贴。最后我们就生成了 6 个文件，最后就可以启动远程应用了。
在这里，为了简单，我们把用户的认证给关掉了，但事实上你也可以把它设成true。再去指定账号文件是什么？密码文件是什么。这里 Keystore password、 trust store password 都需要根据你的实际情况去修改。 copy 切换到 tab 停止掉原先的应用粘贴。跟上下发的名称。


下了。我们使用 secure FX 去下载一下 root test 目录里面的证书文件。需要用到的文件有两个，一个是 visual Vim trust store，另一个是 visual Vim kiss store。保存到本地，需要重启一下 Wechat VM。跟上这么一堆的参数，我们把这堆参数 copy 出来，用 VS code 去编辑。


Keystore，指定成 Keystore 的全路径。新开一个终端，拖动拿到全路径。 trust the store。使用 trust store 的全路径copy，粘贴，退出 Wechat VM，同时切换到tab。把这里必须要标完的全路径 copy 粘贴到这里来。替换掉 j v 10 v m 这个命令。也就是我们需要使用。


which of m 可执行文件。跟上这一堆的参数去执行 which of m Puppy 执行，可以发现已经能够监控到远程服务器上的进程了。双击使用没有问题。回答手机不难发现 j m x 使用起来比 j state 的 d 要复杂一些，参数有好多。而匿名访问，开启用户认证以及开启 SSL 又要额外添加一系列的参数，操作起来也比 j state 的 d 要繁琐不少。但是基于 j Max 的连接方式，比 j state 的 d 要完备一些，相对来说也要更加陈述意见。

[image](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/5c10af17-fdcc-4026-a5c4-0c928f61c9f5/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466Q63B52UF%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T230148Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIBqU2803IGTyokFj8lcgSoX582sXBJVmuDxg2Xa%2FjbUyAiEApFU7S20UZk%2FAo8l0pqrGSvzfoEUEg5Di90gES5bBrS0qiAQIxv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDJyfs9L3nh1gKoHxOSrcA7Z6RwCETZ4l3MWDNi8pjjNuUtjFpnSoABrXxN4tkhpbGShc93HFr3pPP9Ltf1pMaMN76uxrpe9PxS0Lh5HBz%2BwcgCY8dFcf1pYCjV0xoZ7iK6sz2PpexP0LGx3%2BDYLV44%2FZDc9BNkP7L8vCuoU3paZXZajyYZpV8tEBaOWrxW840uYeegSMcEzZav4ZvyiBtGycyH5L2%2F%2F34fkCUHjxL5ogLgY%2BmvjcwTngKCo3MnK3kE5l7LMO40XJCTKzjEcd2m5z0JCvComxflrJ0HoYoc4hqiDhUKxeZzqx3IdTX9xCSqlQ3kPQJNyugqGZScm9mQwt9fJQuAl%2BjslL%2FOkb07rhhv0F%2BhTq0VUjyVUjq8HBk9MTzAmq0wTqSNe0iqkUESfpBvtk15zsysav6NLQ4L2lisgOAg5RJ6KVPxpBci1xtQRK%2F1r%2F7jRRAmn6CBp85DA%2Bs9i3A5BSIO0BMQoKtQioHFNQJTMr2ZBjcfX9pWYDKmkieNIYDLjVzDepXpDSfTpWFKppglfOx7VeMTS50eS672EUf5Ucb98jL4m4vZ31mUcMZlD%2BYgk0xYW3AcRYfnJ8CYa65Dl7V9Kax6lLh3IRho%2BmwMJPfPzlNkLFJ2TMecG7xAWXl6udaa5TMNy3%2F9IGOqUBqF%2FAWPiHZz0WojqLTGNuUrp9hwcUiFPWos0LiKzn773jyDY%2FZuKd4Hn0h52tEvt%2BOnWFrQHspkursDmGkqORzKfyxzh4Qqo7BE47XrL38KCFEVWewSxJdWS8f8s3AdjfwGVKOFRx2a04VeunvohJiXA7k9P2S%2B1ctwRaIksT%2FD%2F7xAqWpU2l9HEP%2Fa9gz7HmopiWfx6oxVUaXKR%2F9eBmgAfH%2B31e&X-Amz-Signature=03d09a7a2a9248f8910ae5eaa017375214f5ec0d496cc077d0749fc144e1108a&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)


