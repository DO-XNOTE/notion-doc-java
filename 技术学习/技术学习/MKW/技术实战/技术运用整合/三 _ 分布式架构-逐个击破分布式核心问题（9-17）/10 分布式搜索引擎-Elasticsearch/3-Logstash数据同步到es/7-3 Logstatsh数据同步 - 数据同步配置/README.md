---
title: 7-3 Logstatsh数据同步 - 数据同步配置
---

# 7-3 Logstatsh数据同步 - 数据同步配置

[image](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/19cf3c64-a87b-4eda-bc08-38fe922bf0db/SCR-20240806-gwbh.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663ZKCX2D3%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T225209Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIBWD58pIgB3IYjt7bJOEYYJzYUNh3nsmnC9EUebY3N%2F8AiAZ9n%2BEcHrjGNwIUPSf%2F5c5e0H9nHU794Rsm0EbIbYG5iqIBAjG%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMlKxdWXJWWlwww6FQKtwDKn3AxzDQz2FAqLiqeLycBnCq%2BwIaYX%2BCrTaZi9iIxpnYDJRQnjjIzILgGSG9ySFLuwHhXh2wvkRBrfSD74OqGqijsvI5uzyKccdkM8vVtJ%2BhgUbDpVLsxvGI1jp0cDxEIye%2BzKmNDnYT3KkG%2FaIEx4TOkGzhiZ4KOMTnH1nSlyAVA6YrWhuz3XBwV7TagT3yQLok%2Fxbu3UvGKsLA6f25YEQb7WwaTXWGx9%2BHWTZbjN855zwvxsg%2BGJYn%2FmGfz526IF3j%2BDPlF3a3F%2BZkNKZgT5aYZjebEqGPoibVkA0dQRYl2mdMyhdWD%2Fqxz7rGbvkgW5jOC5Cj1UWrqXaam%2F9KuXpvFrKDkhCbNKK1A%2B%2FeZtVp0R4Uont2NKLLU47lb51Mo1HLFLl5uxBNnUdHkfoK5nv0ic%2BXLQXDWoBe%2BfUzmFp7GMtBhM%2BBFcVJj64HGFOzix8e79GkOqTfCd%2FU2zLp3GeNWAXcg6HX2Alg8vyZNp2szBM5%2F7d5hEtZ1MDmIyGErGmzF51FlSTH%2FzVHAO2%2BGuF1hEz777Tk6DoJn%2B3nGFhG6YfZncspnyQQr5h%2BsaBGHs4IJHWZKN0LIWkr1cb9CVAbOx1NvoQn%2FEVv8J9TA2WX3TsBlkxactvUoREwtbj%2F0gY6pgFGkNi4Aexv7Ws2L6MGiV16GphMvNU6ZBL9yg64Djwx6dIk%2BjpqWGfVZMTFzcpmEtLMyCacms%2B3aarkPc5Df3b0fc3j%2Fv3EDjgds%2FMS6U9RGowHry2V4BQvXfVzJ6PwhZnHjYIi35zwx37iFRzRGihKhuCVdVrM7PaGwf3XFezuQq5tttTTjWF7KUYm1kiHXSDN0kfEp0ik%2FVBROqy%2FNzJhN%2FQiSf%2FR&X-Amz-Signature=3ae464aaa22b6bb7380e6e06fb28c4d4d621e7f3d97e0224ce6196c9fa956fb0&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

[image](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/f249c1db-4d2a-4de6-aa93-48596b7c88d4/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663ZKCX2D3%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T225209Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIBWD58pIgB3IYjt7bJOEYYJzYUNh3nsmnC9EUebY3N%2F8AiAZ9n%2BEcHrjGNwIUPSf%2F5c5e0H9nHU794Rsm0EbIbYG5iqIBAjG%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMlKxdWXJWWlwww6FQKtwDKn3AxzDQz2FAqLiqeLycBnCq%2BwIaYX%2BCrTaZi9iIxpnYDJRQnjjIzILgGSG9ySFLuwHhXh2wvkRBrfSD74OqGqijsvI5uzyKccdkM8vVtJ%2BhgUbDpVLsxvGI1jp0cDxEIye%2BzKmNDnYT3KkG%2FaIEx4TOkGzhiZ4KOMTnH1nSlyAVA6YrWhuz3XBwV7TagT3yQLok%2Fxbu3UvGKsLA6f25YEQb7WwaTXWGx9%2BHWTZbjN855zwvxsg%2BGJYn%2FmGfz526IF3j%2BDPlF3a3F%2BZkNKZgT5aYZjebEqGPoibVkA0dQRYl2mdMyhdWD%2Fqxz7rGbvkgW5jOC5Cj1UWrqXaam%2F9KuXpvFrKDkhCbNKK1A%2B%2FeZtVp0R4Uont2NKLLU47lb51Mo1HLFLl5uxBNnUdHkfoK5nv0ic%2BXLQXDWoBe%2BfUzmFp7GMtBhM%2BBFcVJj64HGFOzix8e79GkOqTfCd%2FU2zLp3GeNWAXcg6HX2Alg8vyZNp2szBM5%2F7d5hEtZ1MDmIyGErGmzF51FlSTH%2FzVHAO2%2BGuF1hEz777Tk6DoJn%2B3nGFhG6YfZncspnyQQr5h%2BsaBGHs4IJHWZKN0LIWkr1cb9CVAbOx1NvoQn%2FEVv8J9TA2WX3TsBlkxactvUoREwtbj%2F0gY6pgFGkNi4Aexv7Ws2L6MGiV16GphMvNU6ZBL9yg64Djwx6dIk%2BjpqWGfVZMTFzcpmEtLMyCacms%2B3aarkPc5Df3b0fc3j%2Fv3EDjgds%2FMS6U9RGowHry2V4BQvXfVzJ6PwhZnHjYIi35zwx37iFRzRGihKhuCVdVrM7PaGwf3XFezuQq5tttTTjWF7KUYm1kiHXSDN0kfEp0ik%2FVBROqy%2FNzJhN%2FQiSf%2FR&X-Amz-Signature=12c6aaebf0fe60071aa9c1fe0d93fe825e71b3e8017d011c5135edecf9f6552a&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

那么上一节我们是介绍了一下这个 logo stash ，这节我们就来做一个数据的同步。好。那么首先我们先要去做一个解压，把这个 low stash 这个包做一个解压。好。OK ，解压好之后我们把它做一个移动，把它放到 user local 的里面。


好。 OK 那么这个时候我们的这个 low stash 已经是放到我们当前这个路径里面来的。随后我们进入到这个目录里面，进入到这里面来了之后，这里面一些文件其实我们可以先不用去管，因为我们主要是用于去做一个数据同步。那么数据同步的话在这里面我们会使用到这个 bin 在这个 bin 里面会有一个 log sash ，我们会去通过它去做一个运行和执行，那么就可以了。


Ok 。好，随后的话我们就要去做一些相应的一个同步的配置了。这样子我们在当前的文件夹里面我们创建一个叫做 think 那么这个就是代表咱们同步的一个意思，创建这样的一个目录。好，创建这个目录以后我们进入一下。那么我们相关的一些配置我们都会放在当前这个文件夹里面。


Ok 。那么首先我们先来创建一个文件，这个文件就是用去作为我们的一个同步数据采集的一个配置文件，随便取一个名字叫做 log stash 来一个杠 DB 杠 sink 然后它的后缀是 config CONF 一定要注意是这个后缀。好，然后回车一下。那么在这里面的话我们会去做一些相应的配置的内容。 OK 吧，那么我现在什么都不做，直接我先保存一下。好，这个配置文件我们就已经是有了。那么对于这样的一个配置文件来讲的话，我们一会儿再去做相应的配置。Ok 。好，随后我们再来做数据库驱动的一个拷贝，我们拷贝一下，在 home software 里面有一个 MySQL 这个驱动对吧，我们拷贝到当前的一个目录里面，直接写一个点就可以了，回撤一下。好。 OK 那么这个文件我们就已经是拷贝了过来。好，接下来我们就要去做我们的一个配置了，我们要去配置咱们的这个 log stash DB 杠 think.config 我把这个名称先复制一下。随后来看一下。在我目前本地，我在这里创建了一个 logstash 这个文件夹，这里面其实就包含了这样的一个配置文件，这个名称我来看一下是否一致，应该是一样的。好，随后我可以打开一下，使用你一些相应的开发工具去打开。在这里我直接使用这个 facecode 去打开了，打开这个 ES code 来看一下，这里面其实就是包含了一些相应的配置了。那么这些配置有很多，我们一个一个来看一下。


我先放大。首先第一个段的内容，我们都是放在这个 input 里面。那么这个 input 是什么意思？ input 就是我们的一个数据是从哪里来的，然后再往下它会有一个 output 就是我们的数据的输出，我们要输出到哪个位置，我们是放到 ES 里面去的。


首先我们先来看 input 里面，我们首先的配置是 JDBC 这个就是和我们数据库相关的。那么第一个是 jdb C connect string 那么这个就是我们的一个数据库的 URL 以及是数据库的名称的一个配置，那么在这里去做一个配置就可以了。那么这是我本地目前的一个配置来看一下。


我本地目前是安装在我的 mico S 里面，所以我的内网 IP 是点幺点六三三零六是它的端口号，这是你的数据库的一个名称。那么当然这一段内容的话，你也可以打开你自己的 idea 你可以从我们项目里面去拿，也可以把这个展开一下，到这里面去拿一下。其实就是这一段的内容，对吧，就是这段内容你可以直接去拷贝的。


好。最后下一个，那么下一个是我们的一个数据库，我们的一个两个路程，一个是用户名，一个是密码，这个不需要去多说了。那么随后再下一个，下一个是我们的数据库驱动所在的一个位置。 Jdbc driver library. 那么这个是可以你去设置一个绝对路径，也可以是一个相对路径。那么目前我是配置在的这个路径来看一下，在我们 pwd 看一下是在这个路径之下，把这个路径拷贝一下，然后放到咱们这个位置贴过来放到这个位置，然后我们的驱动的名称拷贝一下，把这个后方我应该是一模一样的一个名称，直接粘贴一下。那么这样子你的一个路径就已经设置好了，我在这里采用的是一个绝对路径。那么随后下一个是你的驱动的一个类名，在这里直接这样子去配就可以了。


然后下面是一个分页的配置，那么这个分页是数据采集过程中的设置为 true 然后这里的一个分页每页的一个数量，你可以去自己去设置，比方说我们在这边可以设置为1000，当然你一万五万都可以。好。 OK 那么这是一个分页，那么然后再下一个。那么下就是一个statement。 Five pass. 那么这是执行 SQL 文件的一个路径。那么这个是什么意思？就是说我们在进行一个数据采集的时候，其实我们会去做一个数据的查询。那么这个数据查询的话就是从我们的马收口或者说是门外 DB 中来的对吧？所以你是要去定一个 SQL 语句的，这个 SQL 语句你可以直接写在这个里面，直接写在这个里面的话，那么你就是一个 statement 但是我们往往会把它作为一个解耦。因为我们的一个 SQL 语句可能会比较长，所以我们会把它单独的拎出来放到某一个文件里面去。OK ，来看一下。那么在这里面我是配置在了 food 杠 items.circle 这个文件拷贝一下，这个路径和我们这个上方是一模一样的，我们直接把这个 SQL 文件名拷贝一下，然后到我们当前这个路径里面来创建一下，在这里面你就需要去写一个 SQL 的脚本。那么 SQL 的脚本怎么写？来看一下。


打开 idea 然后我们可以来一下。搜一个叫做我们以前应该是定义叫做 items 星号来一个 mapper 星号，custom应该是在 all 里面有一个叉庙，这是我们自定义的。找一下，往下面找。有一个 search items 这个其实就是我们用于去做一个检索查询的。我们把这一段内容我们拷贝一下，拷贝到这里有一个 where 这边有一个 is man 拷贝一下。然后打开咱们的数据库，打开 name cats 这边我预先创建了一个劳斯莱斯这个脚本，然后在这查询文件里面把这个粘过来。粘过来之后我们可以先去做一个测试点击查询，总共查出来在这里是有 174 条数据。那么这个和我们的数据商品我全选一下应该也是一样的OK ，总共是 174 条数据。这个是 OK 的，没有任何问题。


好，然后我们在这里面我们就要去要去加一个内容，我们再去加一个 update time 这个是在 item.update time 这个我们给加一下，这是更新的时间。另外我们这里边，在这个下方你还要再去加一个 and update time 那么这个时候你要去写一下，写一下大于等于冒号，有一个叫做 circle last 然后下划线 value 那么这个是什么意思？这个其实是一个变量。那么这个就是我们的 low stash 在每一次同步完毕以后，它会有这样的一个边界值，这个边界值的话其实就是在我们这里所设置的一个时间。OK ，那么这个是给 low stash 去看的，所以这个我们在这边要去加一下。随后我们。拷贝一下以后，我们打开这个命令行工具，直接贴过来就可以了。那么这样子我们的这个 SQL 在这边我们就已经是写好了。好，随后我们保存一下。好，OK这样子我们这个 SQL 文件有了吧。好，这个 SQL 文件我们把这个名称拷贝一下贴到咱们的这里，回到我们的备注文件在这里形成是一样的。OK ，在这里也是一个绝对的路径。那么这样子对于我们的这个 circle 文件，我们这样就已经是配置好了。


Ok 。好，最后在这里它有一个设置你的一个定时任务的一个间隔。那么这个间隔就是让我们 love stash ，然后它会每一次定时的去进行一个处理，去看一下我们的这个 circle 里面的一个时间有没有变更。如果说有一些新的 update time 那么他就会帮我们做一个数据的同步。所以在这里的这个 schedule 是需要去做一个配置的。然后这个指的是每分钟，那么总共是有五项，是分钟，小时天尼月年。那么这个我们就不去细说了OK ，全部维星的话是代表每分钟。


然后下面一个是索引的类型，那么我们统一是下划线 Doc 好最后下一个，那么这个我们是否要去开启，我们要去记录上一次追踪的一个结果，就是我们要去追踪的这个更新时间 update time 那么这个是会记录的这个记录到哪里？在这里有一个 last run meta data pass 这样的一个文件。那么来看一下，在这里的话我们可以去定义一下，在这边我也是定义了一个绝对的路径，是放在了这个 think 下方有一个 check time 那么这个文件我们不需要去手动的创建，我们交给他去管理就可以了。所以这个位置我就直接这样子去写好就行了。Ok 。那么这个是用于去记录上一次追踪的一个结果值，后续我们可以去看一下这个文件里面它保存的是一个什么内容。然后再下一个。下一个是我们的一个 tracking column 就是你要去追踪的那一列，在我们数据库里面叫做 update time 所以在这边写一下就可以了。OK ，那么这个是配置的这个参数，然后注意一下，你是可以去写一个 ID 自增的或者说是一个时间都行。


好，然后下一个下一个是我们这个类型，这个类型的话也就是 up day 的 time 它的一个数据类型。在数据库里面，我们来看一下，数据库里面的话其实我们应该是一个 dead time 。在这里我们设置的是一个 date time 但是在我们的 ES 里面其实我们要使用 time stand 所以写好这个就可以了。


好，然后再下一个，下一个是否要清除我们这个 last round meta data pass 的一个记录值，这里的话我们不要去清，如果说你写成 true 的话，那么你每一次都是从头开始去查询的。所以说这个我们设置为 force 另外下面一个是一个就是我们数据库，就是说字段名它会有一个大小写的一个转换，我们不用去进行转换，直接设置为 false 就行了。


OK ，这样子一来，我们这一整块这个 input 其实我们就设置好了。好，随后我们再来看下一块 output output 就是我们的输出，当我们的数据全部都采集了以后，我们要把它输出到某一个位置。那么这个位置就是 elastic search 所以在这里做一个配置。首先一个是我们的 host 也就是所有 us 的一个地址。那么在这里我们现在是只有一台，我在这里是187，所以这个 9200 去写一下。如果说是一个集群的话，那么在这个里面的话是一个数组的形式去存在的。然后下面一个是同步的索引的名称，索引名称我们这个，是福迪艾特斯，拷贝一下看一下。


OK 就这个。好，然后下一个，那么这个你是可以设置，也是可以不去设置，这个就是要保持我们文档 ID 和我们数据库的 ID 的一个值的相同。 OK 吧，那么在这边你去这样子去配就可以了，如果说你注视掉的话，那就没有。那么这个我们之前其实也已经是说过类似的。


那么最后一个这个就是我们的日志的输出，可以输出在控制台，我们可以去看一下这样子我们整个配置文件就已经是好了，我直接拷贝一下大家拿到这个配置文件以后的话，那么你根据自己的一个情况去做一个修改，有些地方去修改一下就可以了。好，拷贝一下。然后我到另一行听一下，我们打开这个 config 文件直接贴过来。OK ，那么这样子就可以了。
好，那么当我们的这些内容全部都配置好了以后，现在我们要去做一个了，启动的话我们到这个鼻影目录。好，随后我们点斜杠 logstash 杠 F 代表我们的文件是在我们的 user local logstash 下有一个 think 我们找到刚刚的配置文件叫做 logstashdb think.copy 文件，点击回车。这个时候的话我们就是启动 logstash 要去做一些相应的同步的一个操作了。那么在启动的时候它其实会比较的慢，所以要等待一段时间。


另外在启动完毕以后，那么由于我们的一个定时任务它是要有一个时间对吧，我们是一分钟，所以的话我们要等待最大一分钟的时间。然后我们再去看一下它的一个日志，就是说在这里会有一个控材的日志会打印出来相应的一些数据。另外我们在同步完毕以后，我们也是可以去测试一下我们在数据库中的一个数据能不能够被同步到咱们的 ES 里面来。那么这个时候的日志已经开始输出了OK ，基本上没什么问题这边是我们的一个 mapping 映射的看到吧。 mapping 这边是一个映射的创建在这个上方一开始是一个启动有一个启动的过程，有一个 starting stash 这是一个启动，然后再往下这边就是我们的 mapping 然后再等待个差不多一分钟的时间那么它的一个数据会做一个同步。


OK ，这边是做了一个查询，刚刚是做了一个查询，然后这边每一条数据在这边其实都进行了一个展示。好，然后我们回到咱们的这个，我们来看一下，看一下我们这yes ，这个 head 刷新，来看一下我们的索引的信息。这个时候你会发现这个映射 mapping 它已经是帮我们做了一个相应的设置了。OK ，它是自动帮我们做了一个映射的。好，然后我们再来我们来找一下数据浏览，数据浏览到这个福利 iPhone 然后在这里面我们可以看到目前我们数据只有一条数据来看一下。


我们先来看一下这个 ID 文档的 ID 在这里是一个占位符，这个占位符很明显有问题，所以我们要去改另外一个我们的时间，来看一下我们目前这条数据里面，你会发现就只有一条数据。照理说我们同步成功以后应该是有很多很多的数据，但是在这里只有一条，所以这两个问题我们要去解决。


首先我们先来解决这个 ID 这个 ID 的话来看一下。我们在数据库里面先来看一下我们的 circle 当我们去进行搜索的时候，其实我们会有一个组件的 ID 组件的 ID 我们在这里是进行了一个重命名，把它 S 改成了 item ID 这样的一个别名。所以这个其实是不对的，我们要去做一个修改，我们先把这个 ctrl C 先停掉，然后我们回到 sink 再去做一个修改，修改 long stash 这个配置文件找一下。我们在这里面有一个 ID 在下方同步设置里面，在这个位置你要改成 item ID 这是主键。 OK 吧。好，保存一下以后的话我们在这个文件里面我们也去修改一下，这个后续会给到大家的。我这样子我写两行，那么这个也是根据自己的一个情况去做相应的一个调整。


OK 好，然后我们再来看一下咱们的一个时间，我们再来打开这个 header 在这里面的话其实会有一个时间的，在这个时间里面看一下这个 update time 这个时间是我们自己的一个时间是自己数据库里面的时间，在这里它还会有一个 time stamp 这个 time stamp 是我们的 log stash 他自己去记录的一个时间。那么这个时间的话因为我在本地之前是操作过的，那么如果说我操作过的话，他其实是会帮我去记录这样的一个时间的。所以这个的话我们要去把我们的时间去做一个修改。就是说我们现在在数据库里面所有的一些记录的时间其实都是小于这个时间的，所以它是同步不了的。我们的数据的一个时间一定要比这个心，它才能够去做一个相应同步，这个是要去注意的。


如果说你的一个 logo stash 你是初次使用初次安装的话，它的一个时间是在 1970 年，是从那个时间开始的，所以这个时间的话要去注意一下 OK 吧。那么在我这里的话我这样子我们把这个时间可以去做一个调整。那么目前其实我们这里面可以看到，所有的时间所有的 up time 其实全部都是在 19 年 9 月份。那么我们这样子我们去做一个调整，update更新我们的一个 items 然后 set 去设置我们的 update time 设置这个时间，然后等于我们换一行使用有一个叫做 date 下划线 at 使用这个函数来为它进行一个累加。那么这个时间就是 update time 。 updates time 这个好，这边有一个interval ，写一下每家四个月 four months 好，OK最后我们把这个去执行一下运行。好。OK ，这个应该是运行成功了，总共是影响了 174 行，我们到这里面我们刷新一下。好，那么我们所有的时间全部都已经是更新了，更新了以后，那么我们到这里返回我们的命令行。现在我们再一次要去做一个启动，我们来到 bin 点斜杠 logstash 杠 F user local logstash 然后 sink logstash 这个 config 文件回车。然后这个时候我们再来做一个观察。那么目前我们这里面还是一样，我们这个数据是只有一条，这个数据我们就不管了。最后我们来看一下这里面数据会不会有一些新增的。


好，OK那么到这里我们来检查一下，刷新来看一下我们的数据。很明显，现在我们数据已经是全部都进来了。OK ，我们使用基本查询到这里面来看，我们可以看多一些。 250 条，点击搜索。 OK 在这里总共是命中了一百七十五条，那么其中有一条是我们之前的一条数据，这条数据我们不管其他的 174 条都 OK 没有问题。那么这样子我们一次性的就全部都同步了进来。Ok 

[image](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/66708d12-01c1-47d8-b6ba-21743519eecd/2020-09-17_175816.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663ZKCX2D3%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T225209Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIBWD58pIgB3IYjt7bJOEYYJzYUNh3nsmnC9EUebY3N%2F8AiAZ9n%2BEcHrjGNwIUPSf%2F5c5e0H9nHU794Rsm0EbIbYG5iqIBAjG%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMlKxdWXJWWlwww6FQKtwDKn3AxzDQz2FAqLiqeLycBnCq%2BwIaYX%2BCrTaZi9iIxpnYDJRQnjjIzILgGSG9ySFLuwHhXh2wvkRBrfSD74OqGqijsvI5uzyKccdkM8vVtJ%2BhgUbDpVLsxvGI1jp0cDxEIye%2BzKmNDnYT3KkG%2FaIEx4TOkGzhiZ4KOMTnH1nSlyAVA6YrWhuz3XBwV7TagT3yQLok%2Fxbu3UvGKsLA6f25YEQb7WwaTXWGx9%2BHWTZbjN855zwvxsg%2BGJYn%2FmGfz526IF3j%2BDPlF3a3F%2BZkNKZgT5aYZjebEqGPoibVkA0dQRYl2mdMyhdWD%2Fqxz7rGbvkgW5jOC5Cj1UWrqXaam%2F9KuXpvFrKDkhCbNKK1A%2B%2FeZtVp0R4Uont2NKLLU47lb51Mo1HLFLl5uxBNnUdHkfoK5nv0ic%2BXLQXDWoBe%2BfUzmFp7GMtBhM%2BBFcVJj64HGFOzix8e79GkOqTfCd%2FU2zLp3GeNWAXcg6HX2Alg8vyZNp2szBM5%2F7d5hEtZ1MDmIyGErGmzF51FlSTH%2FzVHAO2%2BGuF1hEz777Tk6DoJn%2B3nGFhG6YfZncspnyQQr5h%2BsaBGHs4IJHWZKN0LIWkr1cb9CVAbOx1NvoQn%2FEVv8J9TA2WX3TsBlkxactvUoREwtbj%2F0gY6pgFGkNi4Aexv7Ws2L6MGiV16GphMvNU6ZBL9yg64Djwx6dIk%2BjpqWGfVZMTFzcpmEtLMyCacms%2B3aarkPc5Df3b0fc3j%2Fv3EDjgds%2FMS6U9RGowHry2V4BQvXfVzJ6PwhZnHjYIi35zwx37iFRzRGihKhuCVdVrM7PaGwf3XFezuQq5tttTTjWF7KUYm1kiHXSDN0kfEp0ik%2FVBROqy%2FNzJhN%2FQiSf%2FR&X-Amz-Signature=c67510f65fad2d1e8c9d8ccccc470f6fe7bf9dc29de9ac7cb0db105b8c4a6a45&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)





