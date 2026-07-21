---
title: 3-4 老牌监控工具：JavaMelody
---

# 3-4 老牌监控工具：JavaMelody

[image](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/aecca87b-9f52-42ec-9619-f2eef7b7c878/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665HRZYEZE%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T230103Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIFwXPnIQrwlzDAlUKkR3q06r3dR5ZXl6n0QXbtPunOPJAiEAkDcuMRDM6Rdhwv3rA%2B4Kiv7peACVV%2BiBcpXlXozACbEqiAQIxv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDHdQWPjVBv0Vom9omSrcA1UHbKaeadAeX%2BiXSkUHZac5vo2xoqARNCsVmKi%2FXzYfnN%2BjvtPxwRwVpqTkr5UnmooI%2FmlS8%2F4Qgxei9sm%2FXjK9scWZowGMksTVmRyJ2L4IvaVP%2BuvM42GcD75PdwKTdtDbtv1fDQHs9Rpf7t4NAYIush7XnXIEyW6bTbQvM6zfpXOHoV3juYkox1Z%2BtTHd7WgHqYy6v3z3DXvltiHOZx9hXybdH1pYlZFJdfJ6fImKl%2BjWnBmL7W5aldUm3XozWYJ3qzgoBqfRolIRO%2Ffk5NyoFbeV4PN7fGqEw4csx6gRckACURHpoTawsS61ye6PGWNNl5dV4Gf2C38uJ3iQa6bZCo8D5946bkyLIR31PA7yF6x0bz9yqF1xKIdWiOn25SKgnCIwacOQw%2BA8ztYX9KYp08dh8xx%2BDWrhZWpr4eBNTzxG%2Fyy7VtXx%2Fo0V9xSrhFuJ%2Bff%2FTLwHItF0C9SNFd7il39S%2FNHBx6JnbNV3hpKRjOueLuN370AFOtt2phLCZQw1IgKw%2Fy1TjoZNSM2JoHhBq0JnFw1mj%2BvN2DAVgXzJAY3dElfqdgmgZAT792mfPQTCIHSLbajK8mgxNgfOdsGXJEaAEYEtUh99z%2FHZbHeh3s9C%2B1SuboBb7ZFNMP27%2F9IGOqUBAvOHkyx4y0wzzV8gUDAALFrhZWNxXV2LY6fca1NZR0xK0egAMK3V7ybezXj0Gkv0GYyD1r9J7EQM0O8TB6Qefb3304O2IY8V1juafPbvEhKZ9zaHSmXoxqxeEjAgINGr4JdDm3iaaDasNyH8fwdQ7Q1LjEp6u0peHtc2jZsnjd89tzAepOt2kMl9MnQf7pRcNpjbKB7Pur8SWX4kGGLVHoWjarmR&X-Amz-Signature=8cd2dccf98a0a9d552326428ef0afe006d32547c199fbac93d0cf0b3c8a0cb11&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

[image](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/584b1890-e618-4a39-89d8-8a4b62d36a00/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665HRZYEZE%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T230103Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIFwXPnIQrwlzDAlUKkR3q06r3dR5ZXl6n0QXbtPunOPJAiEAkDcuMRDM6Rdhwv3rA%2B4Kiv7peACVV%2BiBcpXlXozACbEqiAQIxv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDHdQWPjVBv0Vom9omSrcA1UHbKaeadAeX%2BiXSkUHZac5vo2xoqARNCsVmKi%2FXzYfnN%2BjvtPxwRwVpqTkr5UnmooI%2FmlS8%2F4Qgxei9sm%2FXjK9scWZowGMksTVmRyJ2L4IvaVP%2BuvM42GcD75PdwKTdtDbtv1fDQHs9Rpf7t4NAYIush7XnXIEyW6bTbQvM6zfpXOHoV3juYkox1Z%2BtTHd7WgHqYy6v3z3DXvltiHOZx9hXybdH1pYlZFJdfJ6fImKl%2BjWnBmL7W5aldUm3XozWYJ3qzgoBqfRolIRO%2Ffk5NyoFbeV4PN7fGqEw4csx6gRckACURHpoTawsS61ye6PGWNNl5dV4Gf2C38uJ3iQa6bZCo8D5946bkyLIR31PA7yF6x0bz9yqF1xKIdWiOn25SKgnCIwacOQw%2BA8ztYX9KYp08dh8xx%2BDWrhZWpr4eBNTzxG%2Fyy7VtXx%2Fo0V9xSrhFuJ%2Bff%2FTLwHItF0C9SNFd7il39S%2FNHBx6JnbNV3hpKRjOueLuN370AFOtt2phLCZQw1IgKw%2Fy1TjoZNSM2JoHhBq0JnFw1mj%2BvN2DAVgXzJAY3dElfqdgmgZAT792mfPQTCIHSLbajK8mgxNgfOdsGXJEaAEYEtUh99z%2FHZbHeh3s9C%2B1SuboBb7ZFNMP27%2F9IGOqUBAvOHkyx4y0wzzV8gUDAALFrhZWNxXV2LY6fca1NZR0xK0egAMK3V7ybezXj0Gkv0GYyD1r9J7EQM0O8TB6Qefb3304O2IY8V1juafPbvEhKZ9zaHSmXoxqxeEjAgINGr4JdDm3iaaDasNyH8fwdQ7Q1LjEp6u0peHtc2jZsnjd89tzAepOt2kMl9MnQf7pRcNpjbKB7Pur8SWX4kGGLVHoWjarmR&X-Amz-Signature=1f3df934a62998dfe86d2a13c5a4c2d35b914bc31bbcb73040a7c005da5d098b&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

[image](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/fbde873a-2c84-425c-9133-5a016a2395f7/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665HRZYEZE%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T230103Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIFwXPnIQrwlzDAlUKkR3q06r3dR5ZXl6n0QXbtPunOPJAiEAkDcuMRDM6Rdhwv3rA%2B4Kiv7peACVV%2BiBcpXlXozACbEqiAQIxv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDHdQWPjVBv0Vom9omSrcA1UHbKaeadAeX%2BiXSkUHZac5vo2xoqARNCsVmKi%2FXzYfnN%2BjvtPxwRwVpqTkr5UnmooI%2FmlS8%2F4Qgxei9sm%2FXjK9scWZowGMksTVmRyJ2L4IvaVP%2BuvM42GcD75PdwKTdtDbtv1fDQHs9Rpf7t4NAYIush7XnXIEyW6bTbQvM6zfpXOHoV3juYkox1Z%2BtTHd7WgHqYy6v3z3DXvltiHOZx9hXybdH1pYlZFJdfJ6fImKl%2BjWnBmL7W5aldUm3XozWYJ3qzgoBqfRolIRO%2Ffk5NyoFbeV4PN7fGqEw4csx6gRckACURHpoTawsS61ye6PGWNNl5dV4Gf2C38uJ3iQa6bZCo8D5946bkyLIR31PA7yF6x0bz9yqF1xKIdWiOn25SKgnCIwacOQw%2BA8ztYX9KYp08dh8xx%2BDWrhZWpr4eBNTzxG%2Fyy7VtXx%2Fo0V9xSrhFuJ%2Bff%2FTLwHItF0C9SNFd7il39S%2FNHBx6JnbNV3hpKRjOueLuN370AFOtt2phLCZQw1IgKw%2Fy1TjoZNSM2JoHhBq0JnFw1mj%2BvN2DAVgXzJAY3dElfqdgmgZAT792mfPQTCIHSLbajK8mgxNgfOdsGXJEaAEYEtUh99z%2FHZbHeh3s9C%2B1SuboBb7ZFNMP27%2F9IGOqUBAvOHkyx4y0wzzV8gUDAALFrhZWNxXV2LY6fca1NZR0xK0egAMK3V7ybezXj0Gkv0GYyD1r9J7EQM0O8TB6Qefb3304O2IY8V1juafPbvEhKZ9zaHSmXoxqxeEjAgINGr4JdDm3iaaDasNyH8fwdQ7Q1LjEp6u0peHtc2jZsnjd89tzAepOt2kMl9MnQf7pRcNpjbKB7Pur8SWX4kGGLVHoWjarmR&X-Amz-Signature=01ffec071487e0f14f3e7670eb5ce925e52a7909bd9b6244ac79bac2985b1f3b&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

这节课来探讨一款老牌的监控工具，叫做加班melody。它的 get up 地址在这里，感兴趣的同学可以看看。 Java melody 功能比较的强大，它同时支持 Springboard 项目以及传统的外包工程。好来写代码。为负d、 dev 项目整合加白l、d。负d、 d v 项目是一个 spring 部的项目。来看看 spring 部的项目怎么使用加班麦乐迪文档在这里。

[image](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/821fc4cb-78cf-4570-9a70-3c6958363c9a/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665HRZYEZE%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T230103Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIFwXPnIQrwlzDAlUKkR3q06r3dR5ZXl6n0QXbtPunOPJAiEAkDcuMRDM6Rdhwv3rA%2B4Kiv7peACVV%2BiBcpXlXozACbEqiAQIxv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDHdQWPjVBv0Vom9omSrcA1UHbKaeadAeX%2BiXSkUHZac5vo2xoqARNCsVmKi%2FXzYfnN%2BjvtPxwRwVpqTkr5UnmooI%2FmlS8%2F4Qgxei9sm%2FXjK9scWZowGMksTVmRyJ2L4IvaVP%2BuvM42GcD75PdwKTdtDbtv1fDQHs9Rpf7t4NAYIush7XnXIEyW6bTbQvM6zfpXOHoV3juYkox1Z%2BtTHd7WgHqYy6v3z3DXvltiHOZx9hXybdH1pYlZFJdfJ6fImKl%2BjWnBmL7W5aldUm3XozWYJ3qzgoBqfRolIRO%2Ffk5NyoFbeV4PN7fGqEw4csx6gRckACURHpoTawsS61ye6PGWNNl5dV4Gf2C38uJ3iQa6bZCo8D5946bkyLIR31PA7yF6x0bz9yqF1xKIdWiOn25SKgnCIwacOQw%2BA8ztYX9KYp08dh8xx%2BDWrhZWpr4eBNTzxG%2Fyy7VtXx%2Fo0V9xSrhFuJ%2Bff%2FTLwHItF0C9SNFd7il39S%2FNHBx6JnbNV3hpKRjOueLuN370AFOtt2phLCZQw1IgKw%2Fy1TjoZNSM2JoHhBq0JnFw1mj%2BvN2DAVgXzJAY3dElfqdgmgZAT792mfPQTCIHSLbajK8mgxNgfOdsGXJEaAEYEtUh99z%2FHZbHeh3s9C%2B1SuboBb7ZFNMP27%2F9IGOqUBAvOHkyx4y0wzzV8gUDAALFrhZWNxXV2LY6fca1NZR0xK0egAMK3V7ybezXj0Gkv0GYyD1r9J7EQM0O8TB6Qefb3304O2IY8V1juafPbvEhKZ9zaHSmXoxqxeEjAgINGr4JdDm3iaaDasNyH8fwdQ7Q1LjEp6u0peHtc2jZsnjd89tzAepOt2kMl9MnQf7pRcNpjbKB7Pur8SWX4kGGLVHoWjarmR&X-Amz-Signature=f2a1cbd0f351d21ad796bf9f911663f848a10e365a9a6ad7cf1fb4e71a6b3bc4&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

第一步加依赖copy，粘贴。第二步写配置copy。
简单讲解一下加 YY lady 的配置。加 YY lady enabled 表示是否启用 Java melody，默认是 true 表示启用 excluded data sources。它表示如果这个项目里面有多个数据源，其中的某些数据源我们并不想让 Java Milety 监控，那么就可以排除掉多个数据源，用逗号分隔排除不想监控的数据源。这里我们的数据源是要被监控的，所以我们把这行配置注释掉。


spring monitoring enable 的表示是否启用 spring service 以及 controller 的监控，默认是true。在这里 ID 给我们报了一个警告，配置找不到。不过我定位了源码之后发现这个配置是可以生效的，只是 idea 不给我们提示而已。
下面 init pair meters 都是加 YY lady 启动时候的一些初始化配置项。其中 log 表示是否记录 HTTP 请求 URL exclude pattern 表示哪些路径不需要监控。这里配着的 pattern 是一些CSS，g， s 等等静态文件。


h，t，d， b transform pattern 这个配置的值是一个正则，它表示用来转换h，t， t p 请求的路径。将其中动态的部分删除。什么意思？我们举个例子，咱们的项目有一个路径叫USERS1，还有一个路径叫 USERS 杠2， 1 和 2 都是符合正则的，所以他就会把 1 和 2 给删掉，让加万麦雷迪认为这里的 1 和 2 是一个路径，从而把两个路径的监控信息汇总起来。 authorize 的 users 设置账号密码，我们可以解开账号 admin 密码就是 p w， d 了。 storage directory 这个配置也很有意思，加班 melody 会把监控数据存储在本地的文件，这个路径用来指定存储在哪个位置，建议配置一下，否则如果你的服务器运行多个微服务，而且存储在相同的目录，很可能造成数据错乱，甚至是数据丢失。个人建议配置成这样，这样即使你的服务器运行多个微服务，实例也不会有问题了。


最后， monitor pass 又来指定加班melody。访问路径默认是monitoring，也就是默认情况下，只要访问乐客 host 8 零 8 八杠monitoring，就可以看到加班麦莉迪的监控页面了。好，启动项目。我们发现项目启动失败了，报了一个很奇怪的异常，说 proxy 的类不能为转换成 hacker data source。这是什么问题？感兴趣的同学可以阅读一下。艺术简单来说是一位咱们课上使用的数据源是海克瑞，而价位 melody 和哈克瑞之间存在一定的兼容性关系。医术详细的描述了问题产生的原因以及解决方案。我们配置一下，添加。
Spring gear jmax enabled financial force.


不会报错了，重启。启动成功了。访问 Lark host 8088 monitoring，输入账号 admin 密码 p WD，登录，就可以看到加 YY 丽丽的监控页面了。好，回到 issue 这里。这个问题虽然解决起来很容易，但其实隐含着一个定位问题的小技巧，有必要普及一下。当你的项目报错，你也能够大致猜出来是哪个框架导致的。比如咱们这里就可以大致确定是整合加完麦丽迪所导致的。因为在没有整合之前，项目是能正常启动的。不妨在你怀疑出问题的框架的 Github 里面搜一下。比方我们这里在加完麦丽丽的 get hub 里面搜索一下，直接搜proxy、hickory，你就可以找到艺术了。对于咱们这里，已经能够找到答案了对吧？如果搜不到答案，但是又确实怀疑是在外卖力所导致的，该怎么办？我的做法是给官方提一个issue，点击issue，然后点击 new issue，就可以提艺术了。


有关提艺术也是有技巧的，我发现很多同学其实不太会提艺术，甚至不太会提问，这里也普及一下。首先，这里的 title 应该描述你遇到了什么问题。比如这里我们就可以写我们的项目整合加外卖 d 之后启动不起来了。当然了，你需要用英文对吧？内容怎么写？我个人提议序一般都会遵循一个四板斧的格式。首先会描述遇到的问题是什么，比方项目启动不起来了，报的异常是什么等等，把日志贴出来。


第二，我会提供完整的复现步骤，告诉别人怎么样才能遇到我这样的问题，方便别人去给我定位吗？第三，我会附带上代码。代码你可以打成压缩包，拖动过来就可以上传到 get up 了。你可以把代码托管到 get up 上面，在 get up 上面创建一个 get 仓库都是可以的。


做到这 3 步的话，你可能认为已经不错了，对吧？但是大漠要说的是，绝对不能只等人家回复，你得掌握主动。怎么样掌握主动呢？我们来到项目的首页，Github，它有一个艾特的功能，这样艾特跟上人员的 ID 就可以呼叫别人了。问题是应该艾特谁呢？我个人的玩法是找到项目的contributor，点进去找项目里面排名比较高的人去艾特。比方。如果我想给加班麦莉迪提醒的话，就艾特他以及他。当然了，排名第二和第三的人现在已经不怎么贡献了，对吧？好，这里还可以给大家看一个我提的艺术，做一个参考。可以看到我艺术基本是遵循四板斧的。首先，我描述了我遇到了什么问题，截图问题的现象。因为这个问题复现比较容易，所以我没有写步骤。再之后，附带上源码，并且艾特了三个人。事实上，我提的八九十个 issue 基本都遵循这个格式。希望大家也能养成良好的提问习惯。虽然你不一定要遵循我这里说的四板斧，但是问题描述的越清楚，你能够获得正确答案的几率就会越大。


好，回到正题，加班 melody 也可以和 spring boot x Ray 特配合使用，只要加上配置copy、粘贴，和 actreator 配合使用。加上配置之后会带来什么样的后果？会带来 3 点后果一点加完美里的会。路径挂到 x treater 下面。也就是一旦配置成 true 之后，我们就需要访问 x Ray 的杠monitor，才能够访问加外卖力的监控页面。


第 2 点如果 x radar 指定了独立的端口，比方 management server 点 pot 指定了一个独立的端口8089，这样我们的 x Ritter 就会使用一个独立的端口，叫8089。这个时候我们的项目要访问 local host 8 零 8 九杠 actuator monitoring 才可以访问。这里我们的 actuator 不需要使用独立的端口，所以我们就把它注释掉。不指定的时候他就直接用 server pot 了对吧？8088。


还有第三点，把配置设成去了之后，会导致设置的账号密码失效。好，我们先来重启一下试试看。笑了。刷新你发现变成 403 了。我们访问 actuator 杠monitory，这个时候就可以访问了，并且也没有让我们输入账号和密码。好，下面我们就来看一下加班麦莉莉的监控页面。这个页面稍微有点丑，而且有比较浓郁的年代感对吧？不过并不妨碍它功能强大。可以发现上面的图表是应用的一些概况信息，点击可以查看详情。下面则展示了 HTTP 的请求情况、 SQL 的执行情况、请求错误的情况以及错误日志，还有当前请求等等信息。在系统信息这一栏，还可以执行垃圾回收，生成一堆临时空间，访问内存的直方图，清理无效的session，查看g、m、 x 的数据，查看操作系统的进程，查看g、n、d、 i 的数以及查看 spring 容器里面的病。非常的实用。好。回到PPT，这是 spring boot 项目如何使用 Java melt？如果我们的项目是一个传统的外部工程，该怎么办？你可以参考这篇文章。你要做的其实就一步，就是在 web 叉庙里面添加这样的一段就 OK 了。考虑到现在传统的外包工程用的越来越少，所以我就不在课上展示了。不过本着尽职尽责的原则，对吧？我这里提供一个整合了加完麦丽迪的示例项目在这里。这个项目其实是我在 15 年前后业余时间做的一个快速开发平台，里面有整合加外卖了。底文档都在 DOC 目录下面。


好简单总结一下。 Java melody 是一款功能强大，使用简单、适用面广的监控工具。它既支持 spring board 项目，也支持传统的 web 工程。这节课希望同学们能够掌握两点，首先是加完麦迪如何整合，如何使用，更重要的是课上所普及的定位问题的思路和提问的技巧。好，这节课就到这里，谢谢大家。


