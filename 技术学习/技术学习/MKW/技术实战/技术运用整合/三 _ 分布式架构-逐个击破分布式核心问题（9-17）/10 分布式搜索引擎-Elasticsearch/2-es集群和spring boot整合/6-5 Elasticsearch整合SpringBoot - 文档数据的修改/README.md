---
title: 6-5 Elasticsearch整合SpringBoot - 文档数据的修改
---

# 6-5 Elasticsearch整合SpringBoot - 文档数据的修改

[image](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/92c72fed-7357-4f3a-a2ad-274f15a7cdd8/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WWR3FEYE%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T225200Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIEmhZmQcjgkPXDwQiF3aXNANzOqF6%2FEbUxfKNdGSdSSSAiEA2lIGdpCF%2Fm0%2BHoz1V0dmAqaVDdykSlJTWfPUo2Q5a5EqiAQIxv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDDNXgh5RwwFGA54JsCrcA7IeBBASpYyvbHyYZ%2BUmrcPOONdA34hW9nVBi6tfri4DbStetVKPVQ%2FixzYOOwOzzOL4FFe0b2PVC%2BeJ3lj5ybMhOh1T4JjC5D0k9RNnichPIkxvZrV6gbvq8rxL8zy49JXAKvk%2FhAyqH7aExn68qGOBoQUx7cq73lxqrpAP9vu6YxgqJ4uOXZhJHnOFAC%2FAuc7vzvXU4zPXKeU45%2BDDX478n7EQhxZkCn7Ly%2BC78SsvhHvd1NgCnNr4ezWvFs58E9huTCEFEuA6tFFxLhBJJRoUb6KgzFpH2PdxTQ0caj%2B%2B9rRW3T0zJ2L28vkQfIqzf1fyi6Wq0eZPAgZPXpEtP4LPu8z01Plm3SAnUQLVkVYMDOydsBuE0VYn11HfWfVIIMP6bBdbaUkVYWWOMW4UP2YD3WlIArAKtFoR2d%2F66z5mTpYkhPlqxUkvc%2BTWXpAetEDGpch7SapXuswm1AHyO%2FoX3KjvAhcWaMwgI9g06vl7Be2JDJ%2BsmdgTXRUeoJLNhaG%2Bk%2F7DZ20fFiwhcOk4pVC7O6PynNjKkjkLr06XFwsiXbSMXGKb0Rq1i2I5ZeSzromUaLdallwnNqSyJLEzonTmrLceJuTyQmstfsPg8vn5yq75mLPDxkUr0wjkMIW3%2F9IGOqUB1sxAA7zixSbzZt7IUP0ldF2%2FMlmZrj2DOi%2BOISUg8NDCK4BeNT22LIHCQIroVvmT9id6ItEGAIWNehKocAsCaDmS2mQwJz%2FqREba4ZsVDGbJB9bUf%2FYtqTrS2nknOns%2BAedZAuAjQXjTvVH041LjY2Z1SYwWZVn2V%2BiK4i1VybXHCfLTo%2FVnwCJSCm8NHUosQ1tcoKXuSB0NzPRSLnVVdQv2pc7g&X-Amz-Signature=a4fb04113f6c56a46749db3688ca99f9d9c49d01e46282779022189cdd915b68&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

[image](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/70f213b3-5e18-4cfe-81e4-ad30b7ffd938/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WWR3FEYE%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T225200Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIEmhZmQcjgkPXDwQiF3aXNANzOqF6%2FEbUxfKNdGSdSSSAiEA2lIGdpCF%2Fm0%2BHoz1V0dmAqaVDdykSlJTWfPUo2Q5a5EqiAQIxv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDDNXgh5RwwFGA54JsCrcA7IeBBASpYyvbHyYZ%2BUmrcPOONdA34hW9nVBi6tfri4DbStetVKPVQ%2FixzYOOwOzzOL4FFe0b2PVC%2BeJ3lj5ybMhOh1T4JjC5D0k9RNnichPIkxvZrV6gbvq8rxL8zy49JXAKvk%2FhAyqH7aExn68qGOBoQUx7cq73lxqrpAP9vu6YxgqJ4uOXZhJHnOFAC%2FAuc7vzvXU4zPXKeU45%2BDDX478n7EQhxZkCn7Ly%2BC78SsvhHvd1NgCnNr4ezWvFs58E9huTCEFEuA6tFFxLhBJJRoUb6KgzFpH2PdxTQ0caj%2B%2B9rRW3T0zJ2L28vkQfIqzf1fyi6Wq0eZPAgZPXpEtP4LPu8z01Plm3SAnUQLVkVYMDOydsBuE0VYn11HfWfVIIMP6bBdbaUkVYWWOMW4UP2YD3WlIArAKtFoR2d%2F66z5mTpYkhPlqxUkvc%2BTWXpAetEDGpch7SapXuswm1AHyO%2FoX3KjvAhcWaMwgI9g06vl7Be2JDJ%2BsmdgTXRUeoJLNhaG%2Bk%2F7DZ20fFiwhcOk4pVC7O6PynNjKkjkLr06XFwsiXbSMXGKb0Rq1i2I5ZeSzromUaLdallwnNqSyJLEzonTmrLceJuTyQmstfsPg8vn5yq75mLPDxkUr0wjkMIW3%2F9IGOqUB1sxAA7zixSbzZt7IUP0ldF2%2FMlmZrj2DOi%2BOISUg8NDCK4BeNT22LIHCQIroVvmT9id6ItEGAIWNehKocAsCaDmS2mQwJz%2FqREba4ZsVDGbJB9bUf%2FYtqTrS2nknOns%2BAedZAuAjQXjTvVH041LjY2Z1SYwWZVn2V%2BiK4i1VybXHCfLTo%2FVnwCJSCm8NHUosQ1tcoKXuSB0NzPRSLnVVdQv2pc7g&X-Amz-Signature=28297c8a22cb98322b87d07256fb379f526222e7068f5c362e24a049d87c7aa2&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

那么前面两节课我们是针对了一个索引做的一个相应的操作。那么接下来我们一起来看一下如何来针对我们的文档数据做一些相应的一个操作。我们这样子我们在这里加一个注释，我是风格性。那么下面的一些内容的话我们就主要是针对于文档数据的一些操作了，我们先来写一个方法，那么新增其实是有了吧，那么直接运行这个东西其实就是一个新增，那么在这里我们直接来做一个更新操作，update studoc 在这边来看一下，我们有一个 ES template.update 那么这个就是我们执行的一个更新的操作，那么它是更新我们的文档数据在这里面，其中包含了一个 up date query 我们先把它给写好点进去。在这里你需要有这样的一个参数，那么这个我们得自己去构建一下。


所以我们在这里我们就要去构建一个 up date query 那么如何去构建呢？那么其实这种方式和我们之前在进行一个索引的构建是一样的，这里是一个 index query 那么对应的它是使用的是一个 build 在我们这里其实也是一样的道理，我们使用这个 up date query 有一个 build 去通过它来进行一个构建好。然后我们通过有一个点我们换行一下。点无意思，我们要去指定一下指明我们要去更新的这个文档数据在哪个地方，也就是它所在的一个索引库的位置。在这里我们使用这个 race class 也就是我们的 stu.cos 指明一下这个就是我们的一个索引的位置数据所在的一个索引库。


好，随后我们再来一个点。那么下一个我们要去做更新的话，肯定是根据我们的一个 ID 文档 ID 所以它有一个 with with ID 在这里写一下。那么这个 ID 我们现在使用的是来看一下我们在 pad 里面使用这个1002。注意它是一个字符串，写一下1002。


好，那么现在我们 ID 有了它的一个索引库的一个位置了以后，那么接下来我们就要去把我们的一个索引的内容给放进去了，也就是文档数据点 with 有一个 index request 这个就是我们的一个请求，这个请求里面包含了我们的一个文档数据，好写一下。那么最后最后的话是点 build 做一个构建，然后把这个 update query 给放进去，那么这样子它可以去做一个更新。那么现在我们是缺少了一个request ，那么这个 index request 我们也是需要去做一个构建的。那么我们点一下进来，这里有一个 index request ，拷贝一下。然后这个东西我们是也要去把它给拗出来。拗出来以后，我们在这里面你是需要去放入一个相应的具体的数据。那么这个数据就是我们要去更新的数据 index request 点，它有一个方法来看一下，叫做 sourceok 吧。 source 就是我们的一个数据。那么我们其实在进行 ES 全文检索的时候，我们就会有一个下滑线，source就是它的一个元数据，就是它其中的一个元素，这个 source 就是代表它的一个数据的意思。


好，那么在这里面你可以看到它传入的是一个map ，在这里面有一个 map 这个位置，这个 map 我们就可以去做一个构建了。写上一个 map 等于我们先为它定义一个类型，另行是 string 然后 object 好，这是它的kb6。你又一下针对于我们这个 SaaS 我们定义为 SaaS map ，点 push 我们要去更新的那些数据，我们是可以在这里面去写入的。比方说我们现在来看一下，我想把这个散这个签名做一个更新。所以我在这里写一下 value 就是我们的一个具体的值，我们来这样子设， I am not superman 好，随后我们再来一个我们把他的这个 money 去改掉，这是他的 money 我们改成 88.6 对吧，然后再来一个改一下他的年龄，年龄目前是 22 岁，我们改成 33 岁。


好。 OK 那么这样子这个就是我们的 source map 随后把这个丢进咱们的 index request 里面。 OK 吧。那么这样子的话其实我们在这里就可以把这个 index request 它的一个请求给放进来，我们的一个具体的位置就已经是有了，就是说根据 ID 去进行一个查询，查询到我们的位置是在 student 这个索引里面，然后再去把这个文档数据也就是更新的内容给放进去。那么这个其实也就相当于是你去写一条 SQL 语句，做一个更新也可以对吧。


比方说来写一个 update student 我们 set 设置一下我们的一个具体要去修改的内容。比方说这个 sun set 等于我们就来一个 abc 好了这边就是大致的写一下。然后下一个就是我们的 H 年龄等于33，再来一个 money 短语设置为88.6，再来一个肯定是 well 这是我们的文档ID ，又是 Doc ID 等于1002。那么其实就是类似于这样的一个操作。那么这个 student update 这个表名其实就是我们的 S tu 这个 class 然后在这里 set 所设置的一些内容就是我们的 index request 另外我们的 where where 条件就是这个无意思 ID 也就是1002。所以这个其实我们在进行使用这个 ES template 的时候，它其实就类似于我们在使用这个买贝蒂斯的封装的通用 map 工具，相当于是帮我们做了很多的 API 的一个封装，所以当我们去使用的时候就比较的方便了。


那么这样子其实我们就能够做到相应的一个更新的一个操作了，我们可以来 run 盘一下。好 OK 吧，那么现在是运行成功了，然后我们来刷新一下。那么这个时候可以看到就是说我们的年龄发生了一个更改，年龄是33， money 改掉了。然后这个 sign 签名 I am not superman OK 。那么这样子我们就可以通过这个 lasting search template 这个模板，通过它的一个 update 就能够来把我们的这个相应的一个文档数据做到一个更新了。

