---
title: 1-25 【K8S技术落地实战】部署微服务-3
---

# 1-25 【K8S技术落地实战】部署微服务-3

[image](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/075a4898-1f90-4ce6-a234-d9ebcb7be096/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666S3CYBX7%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T225949Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDaXHpaHXGOjX2ntm6v8ziPPZgx9vT8sovJvmR7Rd13PQIgSy5XrDDohswbk%2FDe%2BQDIeDryvOnl1oCA%2BQn4dFhE7UQqiAQIxv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDEP0Yd1AUHQZSGzMBCrcA3H3%2BfZ3rK%2Fta5Icj4anq%2FtNE48T7LHBkp6UhK0BpxKV3WjkKUeXT2Z6jQfa8xifJG1yJyfSCF9X4UcM3YaCx%2F8WX7rSUE29iF%2BF3vi8JqsGbHyWvqmDzWZjJqjbmyI1ta8Hups6itx6NMch3GNgnfY9FYxzlWI8Nsa56S2qHuvT5ddw%2B7jj6yMBRoTte2LpgRN4sx7fkimYARCw%2BGlkQG6ZDv6J48lmY2uGHUGCpqTuedSU9aFFArWTFcxUK3sgvOKVMEZODnTPGpRjW7HKyGRYtBgClzZH6yqQBxC2sN7qBZu2xt6kx8a6dXz9VvQCDSzIpoS4mP297WBzLytf9BOajaxPkjcPrGn593TMcCyd8Mx4sf8tM%2FT%2FxUwXIz50baLoQFHpp6%2BCLGRtxO4JxShxMu6Mg2R0kXtivZpkVq3Kfh%2BbfI6nqBW%2BJ8UJiuxXHZijWPr31JJ%2F0jkCTs72Ij%2FKmJM5zoLSKgh3DrfPUW9NzHJiyz2eLeqSeAJvepTb6tub3nHDRUm3%2F1misDSuWdUtza8rLJN9lLqkwRlkN4l0lWE6AZgKie0LegwCgwi6FSV7X4RQ6YuzYXjPs2Cl5XPuMxcfdWeXiwxSTTg76Sc9mG5EvHCqjVHXUyczMI24%2F9IGOqUBaWDkw5n8lGXLQmhLJFxSTTpdQquZw26pc%2FXxU6a2xw6nQAkMxVzEPcMCyC0MDP2%2Befq6JASatgtVhom4FBzdm1l%2FjpNYkhMfb1Ez21TOLkAiRp7OylnxwGiD55uc5SB3zVchj0DEFsoRW5hBPXL1LRYsYpJA4eQmILF60SbjhNvFDo%2FpdfrWckAZOviMf79Dp3eYr%2FmIFUX0AKNOL%2B%2BJlz47JLVK&X-Amz-Signature=d4c83f99dd57dd97259d6f136af9d75faa0b892fb926826a47c0e2a49d015446&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

[image](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/6e12b9a9-d302-4a16-8783-f20f2e6b4fa9/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666S3CYBX7%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T225949Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDaXHpaHXGOjX2ntm6v8ziPPZgx9vT8sovJvmR7Rd13PQIgSy5XrDDohswbk%2FDe%2BQDIeDryvOnl1oCA%2BQn4dFhE7UQqiAQIxv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDEP0Yd1AUHQZSGzMBCrcA3H3%2BfZ3rK%2Fta5Icj4anq%2FtNE48T7LHBkp6UhK0BpxKV3WjkKUeXT2Z6jQfa8xifJG1yJyfSCF9X4UcM3YaCx%2F8WX7rSUE29iF%2BF3vi8JqsGbHyWvqmDzWZjJqjbmyI1ta8Hups6itx6NMch3GNgnfY9FYxzlWI8Nsa56S2qHuvT5ddw%2B7jj6yMBRoTte2LpgRN4sx7fkimYARCw%2BGlkQG6ZDv6J48lmY2uGHUGCpqTuedSU9aFFArWTFcxUK3sgvOKVMEZODnTPGpRjW7HKyGRYtBgClzZH6yqQBxC2sN7qBZu2xt6kx8a6dXz9VvQCDSzIpoS4mP297WBzLytf9BOajaxPkjcPrGn593TMcCyd8Mx4sf8tM%2FT%2FxUwXIz50baLoQFHpp6%2BCLGRtxO4JxShxMu6Mg2R0kXtivZpkVq3Kfh%2BbfI6nqBW%2BJ8UJiuxXHZijWPr31JJ%2F0jkCTs72Ij%2FKmJM5zoLSKgh3DrfPUW9NzHJiyz2eLeqSeAJvepTb6tub3nHDRUm3%2F1misDSuWdUtza8rLJN9lLqkwRlkN4l0lWE6AZgKie0LegwCgwi6FSV7X4RQ6YuzYXjPs2Cl5XPuMxcfdWeXiwxSTTg76Sc9mG5EvHCqjVHXUyczMI24%2F9IGOqUBaWDkw5n8lGXLQmhLJFxSTTpdQquZw26pc%2FXxU6a2xw6nQAkMxVzEPcMCyC0MDP2%2Befq6JASatgtVhom4FBzdm1l%2FjpNYkhMfb1Ez21TOLkAiRp7OylnxwGiD55uc5SB3zVchj0DEFsoRW5hBPXL1LRYsYpJA4eQmILF60SbjhNvFDo%2FpdfrWckAZOviMf79Dp3eYr%2FmIFUX0AKNOL%2B%2BJlz47JLVK&X-Amz-Signature=d34c74741ff2bdf564f441f12be9e717826900dc8a3cf7d4a4061c721abba775&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

[image](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/d4e1c441-1cda-4e1a-9b56-4814c961b2e6/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666S3CYBX7%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T225949Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDaXHpaHXGOjX2ntm6v8ziPPZgx9vT8sovJvmR7Rd13PQIgSy5XrDDohswbk%2FDe%2BQDIeDryvOnl1oCA%2BQn4dFhE7UQqiAQIxv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDEP0Yd1AUHQZSGzMBCrcA3H3%2BfZ3rK%2Fta5Icj4anq%2FtNE48T7LHBkp6UhK0BpxKV3WjkKUeXT2Z6jQfa8xifJG1yJyfSCF9X4UcM3YaCx%2F8WX7rSUE29iF%2BF3vi8JqsGbHyWvqmDzWZjJqjbmyI1ta8Hups6itx6NMch3GNgnfY9FYxzlWI8Nsa56S2qHuvT5ddw%2B7jj6yMBRoTte2LpgRN4sx7fkimYARCw%2BGlkQG6ZDv6J48lmY2uGHUGCpqTuedSU9aFFArWTFcxUK3sgvOKVMEZODnTPGpRjW7HKyGRYtBgClzZH6yqQBxC2sN7qBZu2xt6kx8a6dXz9VvQCDSzIpoS4mP297WBzLytf9BOajaxPkjcPrGn593TMcCyd8Mx4sf8tM%2FT%2FxUwXIz50baLoQFHpp6%2BCLGRtxO4JxShxMu6Mg2R0kXtivZpkVq3Kfh%2BbfI6nqBW%2BJ8UJiuxXHZijWPr31JJ%2F0jkCTs72Ij%2FKmJM5zoLSKgh3DrfPUW9NzHJiyz2eLeqSeAJvepTb6tub3nHDRUm3%2F1misDSuWdUtza8rLJN9lLqkwRlkN4l0lWE6AZgKie0LegwCgwi6FSV7X4RQ6YuzYXjPs2Cl5XPuMxcfdWeXiwxSTTg76Sc9mG5EvHCqjVHXUyczMI24%2F9IGOqUBaWDkw5n8lGXLQmhLJFxSTTpdQquZw26pc%2FXxU6a2xw6nQAkMxVzEPcMCyC0MDP2%2Befq6JASatgtVhom4FBzdm1l%2FjpNYkhMfb1Ez21TOLkAiRp7OylnxwGiD55uc5SB3zVchj0DEFsoRW5hBPXL1LRYsYpJA4eQmILF60SbjhNvFDo%2FpdfrWckAZOviMf79Dp3eYr%2FmIFUX0AKNOL%2B%2BJlz47JLVK&X-Amz-Signature=5009bb110e84d41eab9100d7295ce20971c24725e43a9f431c238b9b306972ff&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

[image](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/cc9cab4f-f2e8-4217-af52-04489497a0bf/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666S3CYBX7%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T225949Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDaXHpaHXGOjX2ntm6v8ziPPZgx9vT8sovJvmR7Rd13PQIgSy5XrDDohswbk%2FDe%2BQDIeDryvOnl1oCA%2BQn4dFhE7UQqiAQIxv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDEP0Yd1AUHQZSGzMBCrcA3H3%2BfZ3rK%2Fta5Icj4anq%2FtNE48T7LHBkp6UhK0BpxKV3WjkKUeXT2Z6jQfa8xifJG1yJyfSCF9X4UcM3YaCx%2F8WX7rSUE29iF%2BF3vi8JqsGbHyWvqmDzWZjJqjbmyI1ta8Hups6itx6NMch3GNgnfY9FYxzlWI8Nsa56S2qHuvT5ddw%2B7jj6yMBRoTte2LpgRN4sx7fkimYARCw%2BGlkQG6ZDv6J48lmY2uGHUGCpqTuedSU9aFFArWTFcxUK3sgvOKVMEZODnTPGpRjW7HKyGRYtBgClzZH6yqQBxC2sN7qBZu2xt6kx8a6dXz9VvQCDSzIpoS4mP297WBzLytf9BOajaxPkjcPrGn593TMcCyd8Mx4sf8tM%2FT%2FxUwXIz50baLoQFHpp6%2BCLGRtxO4JxShxMu6Mg2R0kXtivZpkVq3Kfh%2BbfI6nqBW%2BJ8UJiuxXHZijWPr31JJ%2F0jkCTs72Ij%2FKmJM5zoLSKgh3DrfPUW9NzHJiyz2eLeqSeAJvepTb6tub3nHDRUm3%2F1misDSuWdUtza8rLJN9lLqkwRlkN4l0lWE6AZgKie0LegwCgwi6FSV7X4RQ6YuzYXjPs2Cl5XPuMxcfdWeXiwxSTTg76Sc9mG5EvHCqjVHXUyczMI24%2F9IGOqUBaWDkw5n8lGXLQmhLJFxSTTpdQquZw26pc%2FXxU6a2xw6nQAkMxVzEPcMCyC0MDP2%2Befq6JASatgtVhom4FBzdm1l%2FjpNYkhMfb1Ez21TOLkAiRp7OylnxwGiD55uc5SB3zVchj0DEFsoRW5hBPXL1LRYsYpJA4eQmILF60SbjhNvFDo%2FpdfrWckAZOviMf79Dp3eYr%2FmIFUX0AKNOL%2B%2BJlz47JLVK&X-Amz-Signature=52a63d99a735ded29c202e4f9d8b65ecb8713c6d8ee1b90c2152caaab9d74acb&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

[image](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/e4391511-4560-419b-a52d-83ad51e9482b/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666S3CYBX7%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T225949Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDaXHpaHXGOjX2ntm6v8ziPPZgx9vT8sovJvmR7Rd13PQIgSy5XrDDohswbk%2FDe%2BQDIeDryvOnl1oCA%2BQn4dFhE7UQqiAQIxv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDEP0Yd1AUHQZSGzMBCrcA3H3%2BfZ3rK%2Fta5Icj4anq%2FtNE48T7LHBkp6UhK0BpxKV3WjkKUeXT2Z6jQfa8xifJG1yJyfSCF9X4UcM3YaCx%2F8WX7rSUE29iF%2BF3vi8JqsGbHyWvqmDzWZjJqjbmyI1ta8Hups6itx6NMch3GNgnfY9FYxzlWI8Nsa56S2qHuvT5ddw%2B7jj6yMBRoTte2LpgRN4sx7fkimYARCw%2BGlkQG6ZDv6J48lmY2uGHUGCpqTuedSU9aFFArWTFcxUK3sgvOKVMEZODnTPGpRjW7HKyGRYtBgClzZH6yqQBxC2sN7qBZu2xt6kx8a6dXz9VvQCDSzIpoS4mP297WBzLytf9BOajaxPkjcPrGn593TMcCyd8Mx4sf8tM%2FT%2FxUwXIz50baLoQFHpp6%2BCLGRtxO4JxShxMu6Mg2R0kXtivZpkVq3Kfh%2BbfI6nqBW%2BJ8UJiuxXHZijWPr31JJ%2F0jkCTs72Ij%2FKmJM5zoLSKgh3DrfPUW9NzHJiyz2eLeqSeAJvepTb6tub3nHDRUm3%2F1misDSuWdUtza8rLJN9lLqkwRlkN4l0lWE6AZgKie0LegwCgwi6FSV7X4RQ6YuzYXjPs2Cl5XPuMxcfdWeXiwxSTTg76Sc9mG5EvHCqjVHXUyczMI24%2F9IGOqUBaWDkw5n8lGXLQmhLJFxSTTpdQquZw26pc%2FXxU6a2xw6nQAkMxVzEPcMCyC0MDP2%2Befq6JASatgtVhom4FBzdm1l%2FjpNYkhMfb1Ez21TOLkAiRp7OylnxwGiD55uc5SB3zVchj0DEFsoRW5hBPXL1LRYsYpJA4eQmILF60SbjhNvFDo%2FpdfrWckAZOviMf79Dp3eYr%2FmIFUX0AKNOL%2B%2BJlz47JLVK&X-Amz-Signature=9e9362bb142eede6c9300121a97de04d13cdf0fee0d35df6099f9206b99e3b03&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

回到我们的intellij里面来，把这些参数值通通写进去。我这里是之前我们半仙老师的代码，我从这个网上克隆了一份出来。克隆完了以后，我在这里加两个目录，一个叫 CI CD 目录。那正常情况，我们应该在每一个应用它都自己有一个什么，在 get up 上应该有一个这个 Repo 独立的 Repo 对吧？像 authcallcutitemorder user 都是应该有独立的 Repo 甚至于 config gateway 都有它自己的 Repo 但在每一个 Repo 底下照的应该都有一个 CI 目录，就跟我们的什么 API service web 平级的。


这个里面专门是写一些比如像我们的 YAML 文件，这个文件可以写我们的古尼提斯部署的 YAML 文件，也可以写一些 CICD 工具部署的，比如你用 Jenkins 你用 concus 或者你用一些其他的这个 travis 等等各种各样的 CICD 工具，它的这些什么样貌文件。同时你也可以写一些你自己特有的配置文件，让这个一些工具去读取或甚至一些脚本。


CI CD 的脚本都应该准备在每一个 Repo 底下。那我们因为现在这个整个 demo 是一个 Repo 那我也方便，期间我就独立各个应用节点，各个目录以外，建了一个单独的叫 cic D 目录。那这里面建了几个内容，我给大家看一下。比如你部署有 record 你可以写一段这种就是deployment ，你可以人工写一段 deployment service 这我只写一个 zamp 他到时候可以去操作一下。就这这可能有些小 bug 大家可以改一下，然后去尝试一下。但是我们这次不会用写这个我们直接是什么在图形化界面点。那除此以外，比如像 rabda MQ 的刚刚我们什么我们是点生成的。如果你不点，你也可以写断这个羊毛文件。然后呢把它什么用 coupctrue 命令发布上去，或者在图形化界面里我待会带着大家看一下怎么在图形化界面里也可以把一段羊毛贴进去，然后直接把它一键生成。


好。那除此以外，我这里还写两关键信息，只是用来记录这个亚马文件完全不是为了代码的运行，只是相当于一个文本文件来记录我们 MySQL 的是不是 rm KT 的 URL 端口是不是在这里。然后我们的 Redis 开头的 URL 端口是不是在这里，这就是一些记录，只是做一些记录功能的。


那真正我们的代码，最后什么会放在这个目录？就 CICD 目录是由我建出来的目录拍个节目录，什么是我所有要上传的价包，甚至于像买 CQ 的这个 CQ 的这些我们的包，就是说就是相当于这个命令集，我们统一会放在一个目录，把这个目录可以很方便地整体用 SCP 命令去传到我们的什么一个一台虚拟机上，然后在上面制作一些镜像，甚至于是改变一些数据库的这个底层结构是吧，修改一些 

schema 等等，都是可以提前在一个目录底下准备的。
那这个目录我命名成 packages 好，那我们具体来看，我们实际改的代码不在这里对吧？不在 packages 也不在这个 cic D 目录。好，我们就把它关掉，我们要改的代码在 domain 目录底下是吧。有这么多 use order item cut 跟 auth 好。 platform 底下有这么多，其中 zip cancer 我说了其实我们可以用什么，我们可以用阿里云的，所以我们这里就不做改造。那 config gateway 都要做的 his tricks 两个我们暂时也是这样，我们没有做改造，相信大家也可以通过各种各样的方式可以搭建起来。那我这就偷懒了，readycenter肯定是要做的。


好，我们分别来看，我们就先从这个，先从 registry center 我们的友瑞卡开始来看，打开打开。

好，我们在这个最主要改变我们代码其实不怎么需要改变，但是我们的 yar 文件是重点需要改变的。改变在哪里呢？改完了这里就是我们 host name 通常本来选 local host 这里我们可以给自己取名叫尤瑞卡，那其实也无所谓。所以这里就是我们可改可不改，我建议大家改一下，就表示我是尤瑞卡，其他内容都不变。我们端口要记住是 2 万端口。


好，这就是友瑞卡的服务对不对？它的整体的这个配置文件都在这里了，那没有太大的改动，但是我们仍然是需要在这个右边 Maven 里面找到我们的什么我们的这个 register 然后我们用一个 Maven clean and install 的方式把它给真正的编译好。那编译完了以后，它会在这个 target 的这个目录底集底下。那我都喜欢把所有这些价包统一 copy 一份，复制到什么复制到我们的这个 practice 目录底下。


好，这里其实准备好编译好是吧，复制过来就是 registry center 好，这个变动其实并不大，那我们大的变动开始了，我们逐一来讲解有瑞卡自身变化不大对吧，但是用友瑞卡的这些端口，所谓的这些地方变化都非常大。好，我们看 config center config center 里面一样，我们也打开什么？我们打开这个主应用的下面的 resource 文件。我们先看 boot strapboot strap 这一句话不用变对吧，我们看 application application 这里什么。记住，这是 2003 端口。好同时它是什么？它调用的 rabbit MQ 凤凰大家看清楚，不是什么，不是原来的 local host 也不是某个什么，都是在这个 Doc 章节里面讲到一个我们直接用什么我们刚刚的那个什么内部可用的这个服务名 rab MQ 杠 SVC 所有在容器里面，如果你一旦互相之间通讯不采用尤瑞卡，那都可以用服务名，这就是什么。


这是服务端负载均衡方式对吧？我们前一节介绍了我们用 ribbon 的客户端负载均衡方式，这是跟友瑞卡配合的，还有直接用我们 kubernetes 的 service name 的服务端负载均衡方式，哪些要用我们的什么我们的这个服务端负载均衡呢？所有不在有瑞卡，在半新老师章节里，不在有瑞卡注册的那些应用。
rapid MQ 其实就是它不是在这个我们的有人可以注册的，它只是直接用 URL 访问的。那这个 UI 就是 rabbit MQ 杠 SVC DNS 解析会自动解析出来的。 kubernetes 的 kubernetes DNS 会帮你解析，然后端口 5672 用户为密码。因为刚刚我们起的时候没有额外就设那个 config map 也没有去设那个 secret 所以这里就注掉就是没有用户名密码，直接可以访问 rap MQ 好，那 config 底下不变对吧，还是去访问我们什么半仙老师的这个 github 可以的。


然后另外关键点就在这里，这个也是要反复强调的一个点，我们放大，越是重要越放大，我们把这个拉到右边去。好，我们看一下，在这里我们可以看到什么？

[image](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/dc5e973a-aaa6-4906-b436-f72e04fdc061/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666S3CYBX7%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T225949Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDaXHpaHXGOjX2ntm6v8ziPPZgx9vT8sovJvmR7Rd13PQIgSy5XrDDohswbk%2FDe%2BQDIeDryvOnl1oCA%2BQn4dFhE7UQqiAQIxv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDEP0Yd1AUHQZSGzMBCrcA3H3%2BfZ3rK%2Fta5Icj4anq%2FtNE48T7LHBkp6UhK0BpxKV3WjkKUeXT2Z6jQfa8xifJG1yJyfSCF9X4UcM3YaCx%2F8WX7rSUE29iF%2BF3vi8JqsGbHyWvqmDzWZjJqjbmyI1ta8Hups6itx6NMch3GNgnfY9FYxzlWI8Nsa56S2qHuvT5ddw%2B7jj6yMBRoTte2LpgRN4sx7fkimYARCw%2BGlkQG6ZDv6J48lmY2uGHUGCpqTuedSU9aFFArWTFcxUK3sgvOKVMEZODnTPGpRjW7HKyGRYtBgClzZH6yqQBxC2sN7qBZu2xt6kx8a6dXz9VvQCDSzIpoS4mP297WBzLytf9BOajaxPkjcPrGn593TMcCyd8Mx4sf8tM%2FT%2FxUwXIz50baLoQFHpp6%2BCLGRtxO4JxShxMu6Mg2R0kXtivZpkVq3Kfh%2BbfI6nqBW%2BJ8UJiuxXHZijWPr31JJ%2F0jkCTs72Ij%2FKmJM5zoLSKgh3DrfPUW9NzHJiyz2eLeqSeAJvepTb6tub3nHDRUm3%2F1misDSuWdUtza8rLJN9lLqkwRlkN4l0lWE6AZgKie0LegwCgwi6FSV7X4RQ6YuzYXjPs2Cl5XPuMxcfdWeXiwxSTTg76Sc9mG5EvHCqjVHXUyczMI24%2F9IGOqUBaWDkw5n8lGXLQmhLJFxSTTpdQquZw26pc%2FXxU6a2xw6nQAkMxVzEPcMCyC0MDP2%2Befq6JASatgtVhom4FBzdm1l%2FjpNYkhMfb1Ez21TOLkAiRp7OylnxwGiD55uc5SB3zVchj0DEFsoRW5hBPXL1LRYsYpJA4eQmILF60SbjhNvFDo%2FpdfrWckAZOviMf79Dp3eYr%2FmIFUX0AKNOL%2B%2BJlz47JLVK&X-Amz-Signature=73a14a0640c2bd81144307bc1e855a849da0f5659e590c739e882d7398d641dd&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

上面一段是不是不变。幽瑞卡那唯一区别是什么？是我在这里把 my registry 杠 SVC 给写进去了，这就意味着什么，也就意味着到时候取其我们的什么比瑞卡的时候我会有一个 service 的 name 这个 sales name 就叫 my registry 杠 SVC 然后端口也是 2 万映射 2 万。以这种方式来映们的 euroka 服务。


映射完了以后，其他所有应用去访问，就是用它的 service name 是一种服务端的负载均衡方式。那这里因为我只起一个有瑞卡的实例，所以其实就是没有负载均衡，就是服务端的网络发现方式。好，下面是一个关键点对吧，也要写个 instance 如果你不写instance ，你其实默认就是什么用 host name host name 容器里面 host name 都是千奇百怪的，这是很随意的，所以这个是完全不行的，必须你要有 IP 地址的形式来注册。


然后这里 instance 杠 IP 大家记住不是什么，在 eureka 和 instance 下面自己编一个 IP 地址，然后用什么 eureka instance IP 的，这是我们在容器内接改造方式。而在我们 spring cloud 的真正落到 kubernetes 里面，我们可以支持这种方式，叫做 spring.cloud.client IP 杠 address 在老的版本可能叫 IP address 直接就是一个 A 大写。新的版本就是用这样一个方式， spring cloud client IP address 这种方式可以直接获取到每一个容器的实际 IP 地址。一个 POD 里面任何容器是共享 IP 地址，所以它相当于是获取到了 POD 的内部 IP 地址，就是内网地址。它的端口这个端口其实就是什么？上面这个端口是吧？ server.pod 20003，这也就意味着什么，我们的这个应用它可以访问到自己的 POD 的 IP 地址和端口，那这个 IP 地址端口它会把这个值直接注册 uric 上面，所以不会再需要什么 config server 不需要再起 service 了，它是直接在 eureka 上注册自己。然后所有人要来访问我们的 config server 是通过 ribbon 的方式，然后去 eureka 上找到很多很多个后台的实例。我们 demo 里面两个实例，它会找任何其中一个，然后来进行访问。那这里要让整个界面显得比较漂亮，所以 prefer IP address 为 true 既能看得清楚， instant 的注册也会成功。

[image](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/abdf63aa-42b8-4b6a-b6e7-7bd16c684b10/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666S3CYBX7%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T225949Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDaXHpaHXGOjX2ntm6v8ziPPZgx9vT8sovJvmR7Rd13PQIgSy5XrDDohswbk%2FDe%2BQDIeDryvOnl1oCA%2BQn4dFhE7UQqiAQIxv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDEP0Yd1AUHQZSGzMBCrcA3H3%2BfZ3rK%2Fta5Icj4anq%2FtNE48T7LHBkp6UhK0BpxKV3WjkKUeXT2Z6jQfa8xifJG1yJyfSCF9X4UcM3YaCx%2F8WX7rSUE29iF%2BF3vi8JqsGbHyWvqmDzWZjJqjbmyI1ta8Hups6itx6NMch3GNgnfY9FYxzlWI8Nsa56S2qHuvT5ddw%2B7jj6yMBRoTte2LpgRN4sx7fkimYARCw%2BGlkQG6ZDv6J48lmY2uGHUGCpqTuedSU9aFFArWTFcxUK3sgvOKVMEZODnTPGpRjW7HKyGRYtBgClzZH6yqQBxC2sN7qBZu2xt6kx8a6dXz9VvQCDSzIpoS4mP297WBzLytf9BOajaxPkjcPrGn593TMcCyd8Mx4sf8tM%2FT%2FxUwXIz50baLoQFHpp6%2BCLGRtxO4JxShxMu6Mg2R0kXtivZpkVq3Kfh%2BbfI6nqBW%2BJ8UJiuxXHZijWPr31JJ%2F0jkCTs72Ij%2FKmJM5zoLSKgh3DrfPUW9NzHJiyz2eLeqSeAJvepTb6tub3nHDRUm3%2F1misDSuWdUtza8rLJN9lLqkwRlkN4l0lWE6AZgKie0LegwCgwi6FSV7X4RQ6YuzYXjPs2Cl5XPuMxcfdWeXiwxSTTg76Sc9mG5EvHCqjVHXUyczMI24%2F9IGOqUBaWDkw5n8lGXLQmhLJFxSTTpdQquZw26pc%2FXxU6a2xw6nQAkMxVzEPcMCyC0MDP2%2Befq6JASatgtVhom4FBzdm1l%2FjpNYkhMfb1Ez21TOLkAiRp7OylnxwGiD55uc5SB3zVchj0DEFsoRW5hBPXL1LRYsYpJA4eQmILF60SbjhNvFDo%2FpdfrWckAZOviMf79Dp3eYr%2FmIFUX0AKNOL%2B%2BJlz47JLVK&X-Amz-Signature=a9bb35d3ba1a55bf963a14b67ccd3de9cd20823b1ce45290b072e5549d874aef&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

好，下面就不需要改动，然后也是一样道理。我们 Maven clean 然后 install 装完以后把它复制到这个 package 目录，准备向上面云上进行上传，准备制作 1 米的镜像。好这是 platform 的这个 config 我们配置完了， platform 还漏了一个是不是 get away 对， config 相当于是基础，eureka也是核心对吧。


gateway 是外网访问的，主要的这个我们的进来的网关。好我们打开这个代码，然后代码不需要比如做变化，唯一需要的也是改我们的 application.yaml 我们把 gateway 的 application 的羊毛放大。我们仔细来看一下，上面内容其实都不变，Redis请记住是不是把这个刚刚给大家看的杠就算内容 call 过来，因为它是有什么？它是有 URL 的，它不是个 IP 地址，它是一个公网的服务。那它的端口又379，是一个正常的端口，那数据库就默认就是 0 密码，IM004。


怎么把密码明文写在这里多不好啊？那应该怎么样？应该是通过外网来传哪种方式好用我们的 config 的这个 map 用 secret 还是用我们的 spring cloud config 其实前前面已经聊过了，其实很好的方式是 spring cloud config 在 spring cloud config 从我们的 git 上面拿密码好不好？其实并不好，是不是？那最正常的情况是用 spring cloud  config 去跟第三方什么密钥服务对接，就既去 get up 去拿那些明文数据，比如像这种比如说什么这种 raise URL 完全你可以通过 get up 去拿。那密码千万不要从 github 拿，你应该对接，比如说我们的 hash cup hash cup what 这种最知名的什么密钥管理系统，密码管理系统，它完全可以跟 spring card 对接。


那有兴趣可以看一下这些网上的这些篇章，怎么样去对接来实现生产中间的中的什么数据加密传输，数据加密存储，但是在内存里面明文进行展现和使用。这样用完以后，它的值其实就可以传到我们的应用里面来。但是而且这种传法你不需要额外去像 kubernetes 一样，你要去读一个卷或读一个环境变量，相对来说编码还有点奇怪了，所以更建议用 spring car config 来传这些 password 我们这里简单执行就不做改造了。


下面的这个有有变化的地方是我把 zipkin 关掉，因为 zipkin 其实也会用到一些消息队列什么的，但是我们这里就不做demo 。好，除此以外几乎是不变，一路不动，甚至于自己端口也是20004，这也是我们最后 postman 要靠到的端口，全部不动。好，这里怎么样？我们把刚刚的什么在我们的 config server 里面的内容 call 过来，一模一样，不用改动的，因为 instance ID 它会自动去找到。我自己的这个实例。什么是 gateway 我会把我自己的 IP 地址找出来的。而端口也就是这会继承这里的 20004 是吧，从这个参数这里读取出来，所以这段是到哪里都可以通用的，所以也是叫 my registry 杠 SVC 一定要记住，我们到时候建这个服务的时候不要建错名字，其他值都不变，然后mvn clean install 好，这个就把我们整个 platform 全部准备完成了。


platform 准备完成以后，我们就开始进行什么真正的 domain 的准备一个来，我们从上往下好。 domain 里面我们打开第一个的 service 的下面的 resource 的 application 回放大好。 foodie auth 这个 service 对外是什么？ 10,006 这种端口其实是不用记的。为什么？因为有人卡帮我们记对不对？那刚刚要记的端口有两个，一个是什么？一个是我们 rabbit MQ 这个服务都起了一个端口对吧？这就是标准端口。那另外一个是什么？是的什么？我们的这个实际使用到的这个有瑞卡的对外端口。那什么 2 万这两个是要记的。


好，我们这个 auth 里面 10,006 端口下面的应用名都不变，唯一改变还是这里。把 Redis 的新的这个我们公有云生成这个 IP URL 写在这里，端口不变，密码可要改。对不对？ zipkin 注释掉。然后 eurika 如法炮制 call 过来即可。好没问 clean install 搞定它 copy 到我们的 package 目录看，抛弃目录有这么多，那其他都如法炮制。我们这里简单起见，就快速带大家来过一遍。好一个来，不要急 cart  我们的这个购物车它在里面，在 source 底下 resources 有好几个，我们一个一个看 boot strap 这里首先就是要把刚刚的什么 config 那个 server 的这个地方的内容完全一模一样拷过来即可。 application 这里我们要改动什么？有一处要改动最关键的一处，千万不要忘我们在创建数据库的时候放大选的什么用户名叫 IMock 这里就完完全全一样。在那边就是数据库 MySQL 用户注册的时候，注册管理里面我们会设过一套用户密码，那这里要无法炮制你叫 IMock 那其他的改动不需要。


那好我们具体的内容它是在 profile 的 DEV 里面对吧，它选的什么 profile active DEV 好，我们在 DEV 里面去改什么改数据库的 UR LR 数据库我叫连什么 icq 然后我这里的 demo 我最近的叫 food 下划线 shop 下划线 demo 我的数据库名是这样的，因为买 CQ 好像对这个支持的更好， UTF 8 这样的形式更好。


所以我就是把我的数据灌到了这台我们刚刚准备好的数据库里面，过量方法很多了对吧，可以用什么 MySQL 的什么 work bench navicat ，甚至于像我一样什么我跑个 Linux 的 MySQL client 然后跑一个 source 一个 script 都可以把数据给灌进去。就是把之前我们的这个风间老师那套对吧，我们的基本的这个 DDL 的数据全部给灌进去。好，那密码不要忘了，改成合适的密码。好，Redis也一样， URL 换掉，把它的密码注掉对吧。下面什么 Redis 照片模式什么都不用。好，我们不需要那么复杂，就一个简单的小 Redis 即可，谁不可以注掉其他不变好。然后右边这里对吧，Maven这里处理一下， install 一下。


好 cut 搞完我们看下一个服务 item 到 item 的 web 里面，看它的几个从 bootstrap 开始看一样 eureka 是吧，如法炮制拷过来。好， application 这里 application 这里有什么区别呢？也没什么区别，也是把数据库的 IMock 这个用户名 call 过来，如果你不叫 M 和你的用户名，反正不要忘了 call 过来就可以了。然后在 DEV 这个 active 的 profile 里面也是一样的。改动端口要记吗？这种都不用记，都是内部应用是吧，它会自动什么在 uroc 上被发现的，所以不用管这里把 uil 改掉，把数据库名改掉，密码改掉， Redis 改掉，所以改来改去就是什么 uil 密码。那唯一要注意就是什么？


就是我们的 eureka 这里对吧，要选用什么 instance IP 的形式来进行注册。好，改完以后再是没问 install 一下，就把 item 搞定了。好，大家是不是有点累了？好， all 的有一个小区别，我差一点就漏了，自己做的时候我都漏了，然后跑的不通过。这要讲一讲，有点意思。好先讲一下。 put strap 不变的地方对吧，call过来。 application application 不变的，就改个数据库名。好，这都没有什么问题，难点在这里。 application dial 如果大家直接上手做，看完我课的前面章节，其实这些东西也能推导出来。然后在这里做的时候会遇到坑的，我们看看坑在哪里？端口不用记对吧。


URL 改一改， MySQL 的 URL 改，我们的数据库名改一改都不错，密码改一改， Redis 改都没问题。好走走这里我们用什么？我们 cloud streams rain cloudstream 用到了什么？用到了一些内容，哪些内容用到了一个叫 rabbit 然后他是用 rabbit binings 的，这个方式是没法去配用户名密码。而我们的 rabbit MQ 是不是有一套自己的这个用户名密码其实没有，但是我们有什么我们有自己的 URL 和端口，我们的 UL 还是一个什么？我们是一个 service 所以我们用原来的这个方法不行，这时候就要把原来的注掉，然后又换一个方法。



除了 bindings 以外，其实 cloud streams 还有一个 binorsbinance 就是说我用怎么样的一个实例来实现我的什么我的 color stream 这里要写binance ，随便取个名字，我就选个 test 然后类型关键就是 rabbit 然后你就可以把具体的那个 rabbit MQ 的值用 invite spring 形式写了。
写的内容具体值是这样的，两个值是要我们改变的，其他就是默认的，其实真正要改变的端口都不改变，真正要改变就是这个 address 其实就是 URL 或者 IP 地址。那我们这里什么会用到这个 URL 这 UI 会自动迭代解析到我们的什么我们的这个后台的 service IP 然后通过 service IP 来指定我们的后台的 POD 唯一的那个 rapid MQ 的这个 IP 地址。好，就是这样，重点就是要把原来那段注掉，然后写一个 bindust 然后把具体的 rabbit MQ 的 U rl 通过这种方式给展现出来，这时候你才能跑通，否则以后就会被这个坑给拦住了。


好， order 弄完以后 user 也是有坑的，我们来看一看。 user 打开 board strap 上面一段是什么如法炮制下面一段 spring cloud config 你可以看到这里关键点什么，这个要不要改，要不要更改。为什么？因为我们 ring cloud config 在有瑞卡里注册的名称就叫这个 config server 它这里 service 的 discovery 这个名称就是用 eureka 的名称那边注册什么，我们这里就写什么，对不用改好，我们进到 application 这里，进到 application 这里我们打开看一下是不是也是一样。数据库它这里是说用户名我换成什么 IMock 其他，一路都不变。


好。 DEV 里面是有坑的，我们看一下坑在哪里？ DEV 里面，这里就是选择之前什么是半仙老师是说建议大家是对吧，用什么概念，这就是用到了 spring cloud config 去我们的 get up 去拿这个纸，他拿了好几个值，既有拿了一个迈瑞 DB URL 迈瑞 DB password 还拿了一个是不是要做一部分操作？是不是允许用户注册？这些指函都写在那个 github 里面，那这两个值千万不能拿了怎么样？拿了就会把上面的值给盖掉，是不是？如果你把这个上面值注释掉，下面值写在这里，那你就会去拿半新老师那个 local host 了，这个时候你永远是找不到我们 merry DB 的。


所以你要在这里我们只能不好意思了，我们不去改保险老师 get up 代码，保证就是有些同学在做前一个实验不会做崩掉。那在做我们的实验时候，我们把这段注释掉，我们什么？把上面一段打开，还是用传统的在这里写 URL 的 IP 地址 URL 端口数据库名以及我们的密码 IMock IMock 同样道理， Redis 也是这样改对吧，他们的坑主要就在这里，就是一定要把上面的那个 merry DB 这端通过这个 sprinkle config 通过 github 拿到这个注掉好， merritus 一样。


改完以后，rabbit MQ 也要注意，这也是一个语文容易弄错的地方。 host name 就是按照我们之前说的写 rabbit MQ 杠 SVC 这个 service 的名称是在集群里，我们是可以内部沟通的。端客 5672 不变，然后下面密码注掉，那其他的几乎都不变。弄完以后，然后底下这些常常的配置都不用变好两大坑 order 1 坑对吧。还有 user 一个坑，这两坑弄完全部 Maven 编译完，我们就把所有的包都准备好了。然后很简单的用什么 SCP 命令或什么命令想方设法传到某一个什么服务器上。那在这个服务器上面我装了一个我们的 Docker 我在这里装了一个我们的 Docker 所以它在这里能起 Docker 命令。


如果我们的 Mac 电脑我其实是没有装的，所以没发起。如果大家说自己 Mac 电脑已经装上 Doc 了，也可以在自己 Mac 电脑这里我可以看一下。这就是我上传了一些包对吧，这些价包，就是我们刚刚 package 里面价包。那 MySQL 的代码也是我上传到这里，然后通过 MySQL client 注入到我们数据库里面的。这个是装 Docker 的一个脚本，所以一个 Doc 有关文权在这里。然后我们重点看一下 Doc 法，这个再回忆一下我们 Doc 章节是不是套路不变，一切来自于 from 之后，往这个里面加一个我们的价包名称都不变。加完以后用 entry point 起一个命令。起命令这个命令叫什么叫 Java 第一个船参叫杠，加第二个船参就把这个价包的名字传给他，然后他就会跑起来，而且跑得很嗨。


那这个弄完以后跑什么命令呢？ Docker build 是吧，编一个，然后打个 tag 打 tag 比如说我们喜欢叫什么叫 my user 然后我们就几个点，就是当前 dog far 去 build 一下，就会花一点时间。那通常第一次花时间非常非常长，因为你要从 [github.io](http://github.io/) 上面去下一个夹了对吧，要下很长时间。如果你做了镜像就会快一些，比如镜像就长一些。那做完以后下次就很快。


弄完以后，你这个名称叫什么？ Docker images 如果我们 grap 一下什么，我们 grap 叫 myuser 你就能找到你这个名称就叫什么叫 my user 对不对？你这个 image 但这个 image 并不是能上传到云上的 image 所以我们要上传到云上必须什么把 imag 名称给换一下。换完以后，就往云上去传好，具体怎么换名称、怎么上传以及怎么部署，我们就留在下一节。

