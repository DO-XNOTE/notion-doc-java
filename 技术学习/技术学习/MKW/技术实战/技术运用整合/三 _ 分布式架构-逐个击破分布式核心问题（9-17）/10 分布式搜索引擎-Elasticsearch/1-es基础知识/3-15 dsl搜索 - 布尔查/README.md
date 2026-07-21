---
title: 3-15 dsl搜索 - 布尔查
---

# 3-15 dsl搜索 - 布尔查

[image](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/e8cf2f76-0be6-4289-a869-19724f5c753d/SCR-20240806-eebb.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665GAKOR34%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T225141Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCXGiVHZbhNHGWDdvm3psIt0wCkD2mpPfZuH4uz4zpzZgIgfMo9NGFnp24I17IPNJ5JB9axpFkMH3U28%2BvnmiUM0bYqiAQIxv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDP33EOOLF8CtzdOfpyrcA9AUwcITOm7CkoRyw1qNf7Ot5QsUQbiW%2F6xBN2cwCmYNzmMWQYJzG28zN54qYaizN1en0QeC1%2Fwtd2Qa4kG4fd1fUiBvWYnvco2HbrWkfgKDbAkDt%2BIDBQUnU9LDl5ZivDSzY%2FrgiNTFQis%2BFp0YXSuDEQNw1cOVra5xTZjWQJBIYoFM6sMjBrObUbxfX7mSJKzTiggwcbVhCTfIWSYyLTAQmQzIUqWBSwiZyZaEEKJeXeWtoSGlxP%2FhdnX1qSvVvz4yDAe2THvuhxWLAEi4JHz1QZzZ3i5vRRNi%2B2PNDDnbHs1kzuYDP6kQKOKJiKLT4Rm1IjX2zGZHMvjC0TcfOaWvDW3g%2Ba7oIzmXqxLSetq%2Byq9Unzz5SupxbFHWZJtNCvFR6YfwxjBjkdq3tZ4Ogjjtmbo1oHUOot2%2F%2Br%2FCBB6GNutNAB6u1esi9quDdD4kRzjt4MY36wl4OzGzFkbn%2BenrV8Ez7G3ee%2FtSlEiCkzez1Ny0tIKr4JdOU4EuYCAzBRBckUhkbeISuIp8kzaIJ%2Funebodw4af2XpnYeCE7y2GHiXzTm5oTH54BGVp4jmGheZTXoyYhSGvERnmn6pA3%2BV0s4sCSBwMV8Rfr9k%2BXaidQKfeIvkRfAJBrnXWMMu3%2F9IGOqUBEzsq7l9HpDbvkKQEAN659V3e2K6KPHRl5mA%2BQyIrUobyxWQXY7hzCtLOBOwAJM3VDb4w0u63YXLfGoEa7pWBdKJJwKgGVzWerNjKFTPwQm8uylxIdBDUdLFsjByrCmI9JQt2e%2B1lTKXmnpZtMfcROfpeby6JES1cRVlVSnkZj%2BlWfS%2BP4QCa1DmRNPr9UgXqeh7XfyUZJpETGC6EBDJ46M152cIS&X-Amz-Signature=5f8292e6a6a556b64ae569083d539d014bc8ab6da6b428963880ff24904ba09e&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

[image](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/c3cf09c9-becc-414d-8664-9f219781247c/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665GAKOR34%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T225141Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCXGiVHZbhNHGWDdvm3psIt0wCkD2mpPfZuH4uz4zpzZgIgfMo9NGFnp24I17IPNJ5JB9axpFkMH3U28%2BvnmiUM0bYqiAQIxv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDP33EOOLF8CtzdOfpyrcA9AUwcITOm7CkoRyw1qNf7Ot5QsUQbiW%2F6xBN2cwCmYNzmMWQYJzG28zN54qYaizN1en0QeC1%2Fwtd2Qa4kG4fd1fUiBvWYnvco2HbrWkfgKDbAkDt%2BIDBQUnU9LDl5ZivDSzY%2FrgiNTFQis%2BFp0YXSuDEQNw1cOVra5xTZjWQJBIYoFM6sMjBrObUbxfX7mSJKzTiggwcbVhCTfIWSYyLTAQmQzIUqWBSwiZyZaEEKJeXeWtoSGlxP%2FhdnX1qSvVvz4yDAe2THvuhxWLAEi4JHz1QZzZ3i5vRRNi%2B2PNDDnbHs1kzuYDP6kQKOKJiKLT4Rm1IjX2zGZHMvjC0TcfOaWvDW3g%2Ba7oIzmXqxLSetq%2Byq9Unzz5SupxbFHWZJtNCvFR6YfwxjBjkdq3tZ4Ogjjtmbo1oHUOot2%2F%2Br%2FCBB6GNutNAB6u1esi9quDdD4kRzjt4MY36wl4OzGzFkbn%2BenrV8Ez7G3ee%2FtSlEiCkzez1Ny0tIKr4JdOU4EuYCAzBRBckUhkbeISuIp8kzaIJ%2Funebodw4af2XpnYeCE7y2GHiXzTm5oTH54BGVp4jmGheZTXoyYhSGvERnmn6pA3%2BV0s4sCSBwMV8Rfr9k%2BXaidQKfeIvkRfAJBrnXWMMu3%2F9IGOqUBEzsq7l9HpDbvkKQEAN659V3e2K6KPHRl5mA%2BQyIrUobyxWQXY7hzCtLOBOwAJM3VDb4w0u63YXLfGoEa7pWBdKJJwKgGVzWerNjKFTPwQm8uylxIdBDUdLFsjByrCmI9JQt2e%2B1lTKXmnpZtMfcROfpeby6JES1cRVlVSnkZj%2BlWfS%2BP4QCa1DmRNPr9UgXqeh7XfyUZJpETGC6EBDJ46M152cIS&X-Amz-Signature=320b2e7aa1c1c3218974a3a432ec53ff6dfb35bd7d1805dd70febee145f88c88&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

我们一起来看一下 gsl 的一个布偶查询，也就是多重组合查询是什么意思呢？我们可以来看一下。就是我们之前在使用 head 插电的时候，其实在这个地方有 must must not 以及是树的。那么这个东西其实就是一种组合的查询方式，它就是一个布偶。什么是布偶？我们可以来随便先写一下我们展示一下它的查询的一个语句。这个杰森来看一下这个布尔其实就是 BOOL 那么它就是一个布尔查询。你可以发现其实这个 must must not 以及是树的。那么这几个其实它都是包含在这个布偶之下的。OK ，你展开以后其实它就会包含了这几项内容。所以这个其实就是一种组合的查询方式。


在这个查询方式里面不管是哪一个像 must not 和数字的话，其实里面都可以包含多个组合去进行查的。因为你可以看到其实它每一个里面这都是一个数组，然后这下面两个是空数组。那么对于这三个关键字是什么意思呢？像这个 must must 就是代表当我们去做查询的时候，这里面是一个数组。然后这里面的一个条件其实你都是必须要去做匹配的，那么它就相当于是一个 and 对于这个数的来讲的话，数的就相当于是一个 or 相应的一些条件数据在这个的数组里面的话，它只要是符合 or 就是说或者只要是满足条件的话，它就能够被查询出来。就说条件的话只要是一个以上就 OK 了。


对于这个 must not 来讲的话，那么它其实就是不匹配你的一个搜索条件，你把相应的搜索条件里面放到这个输出里面的话，它是取反一个都不要满足，把不满足的内容给查询出来。这个其实就是布偶查询，当这几个又放到了一起了以后，那么其实这又是一种布偶的组合查询。Ok 。所以我们这节课就针对这个布网，我们就一起来写一下。那么现在我们就直接来打开这个 postman 作为相应的一个实操。比方说现在我们先去使用这个 must 那么这先这样子，我们把这个先改掉，你要去使用布尔的话，你得先定一下这个布尔。那么随后你在这个里面的话，那么你就可以去写上一些相应的一个 master 或者说是竖的。所以先把它的一个基本的一个框架先写好，这是一个 must 那么这个就是一个基本的框架。然后在这个 must 里面你就可以去写一些相应的内容了。比方说我现在的话，那么要注意这边写错了，这是一个数组，数组的话是一个中括号。好。那么随后我就可以去写我相应的条件，每一个条件它都是一个 Jason 的 object 所以它也是一个大括号。那在这里比方说我可以去写一下，我可以去写一个 multmatch 你可以你使用 match 都行。那么这个时候我想要去做一个匹配，我想要去查一个先写好 query 我想去查慕课网。 OK 然后我在这个下方我再去加上一个叫做需要纸，注意不要拼错必要纸，它是一个宿主。


然后我要查询的内容是基于这个 description 以及是它的一个叫做尼克 name 这边我们把这个拉过来一点拉过来。 OK 那么这是我在 master 里面的一个条件。那么我先点击这个搜索。OK ，相应的数据是可以被搜出来了，总共是有五条数据在 description 和这个尼克列里面，只要包含慕课网，那么它就可以给搜出来就是慕课网。然后这里边也有一个慕课网，然后这边往下面看都有吧，就是一个学习的慕，就是在 make name 里面的，另外这边都有。好。那么随后我在这里面，现在我可以去追加一些额外多的一个条件。比方说我们现在这里面，在这边我们加一下这个我们加一个 H 年龄，来看一下，这个年龄的话其实也是有零一之分的。


对吧，像这个应该是 sex 我们写一个sex ，因为 sex 的话是只有01，来看一下这个 sex 01 这边你要么就是01，要么就是 1 如果说写一个 H 的话，它这个年龄就比较少，因为我们本身数据量比较少，所以我们就使用 sex 如果说你的数据要多的话，那么你使用 H 也没问题。


我们以 sex 为例，在这边我想再多追加一个条件，比方说我们在这个下方，因为它是一个数组对吧，所以在这个下方我再去加上一个对象去做一个查询。这个它本身 sex 的话就只有一项，你可以使用 match 也可以使用称都行，写一个称。现在我要去查咱们这个 sex 比方说我要查一点击搜索。那么现在我搜索出来的数据的话刚刚是有五条，现在是只有 3 条了，因为它相当于是做了一个额外的条件，也就是这个尼克 name 和 description 要等于要包含这个墨库网 and sex 唯一。所以我们查询出来的话所有的数据它的 sex 都是 1 OK 。那么你把这个改为 0 的话也行，改为 0 的话，那么在这里面的话就只有两条数据了，那么这就是 0 对吧和这个0。 OK 好，除此以外，那么我们还能够再去追加条件，你可以在这个下方我可以再去加对吧。


比方说我们现在可以再去加一个 birthday 啦，然后把这个拷贝一下贴过来贴到这里，这边我们别形成，因为它本身是一个 datebirthday 在这里我们指定一个值，我们到这里面去随便找一个。你们比方说找这个。这个有一个 92 年 12 月 24 号拷贝一下贴过来做一个搜索。那么现在你会发现它里面的记录是 1 吧。OK ，相当于是又多了一个条件吗？多了个条件，你的一个搜索的精确度又提高了。那么在这里面写这一条数据，它的 birthday 是一个12，所以这里面是都包含这个条件的，都是必须满足的。


如果说我把这个 sex 改为 1 你再去搜索的话，那么这个时候它匹配 hits 其实就是命中了 0 条，它查询不了任何内容，因为我们的这个数据我们是不包含这个 sex 唯一的。OK ，这点需要注意的。好，OK那么这就是我们的这个查询。然后我们再来看一下我们下一个我们可以使用这个数的，那么数的其实就是或者的意思吗？直接点击 send 发送，你会发现刚刚其实是查询不了任何内容的对吧？当我们使用数得了以后，现在我们数据瞬间可以去查询五条了。那么也就是说这个条件满足，然后这个条件满足或者这个条件只要其中一个条件你满足的话，它都可以帮我们去查询出来。


OK 吧，那现在是五条，然后我们可以把这个 birth 我们可以去。我们挑一个这边有一条英文的这条记录，把这个 80 年的 8 月 14 号拷贝过来贴到这里。然后我们查询一下，你会发现这边又多了一条，现在是六条记录。那么这个最后刚刚我们加的一条这个英文的这条数据是可以被我们加入进来，因为这里面这条记录它只有这个 breath 是满足的，是它的条件它不满足。所以只要一个以上的条件满足的话，那么这个数据就能够被我们给搜出来。Ok 。好，那么现在我们是一个序的，如果说我们再来一个 must not 我们来进行一个搜索的话，点击 send 那么你会发现这边还是六条记录，我们这样子把这个恢复一下，把这个恢复成 92 年的 12 月 24 号。那么现在我们这样子查是只有五条对吧，这是一个序的。然后我们把这个再改为 must not 点击 send 这个时候它是一个 7 条，那这个 7 条和我们刚刚的五条加起来，正好是 12 条。那么也就是说这里面的条件都不满足的其他的一些内容，只要是和它相反的那些条件的话，它就能够被我们给查理出来。也就是说这里面的条件都不能够满足。就比方说在这里面可以看一下我们的数据里面其实是不包含慕课网这三个字的对吧，都是没有的。另外这个 sex 你可以看一下，它其实取反了之后，它所有的 sex 在这里面你去看的时候，它全部都是唯一。


OK ，全部都是一另外这个生日如果说是有一个数据的生日是 92 年的 12 月 24 号，它是肯定不会被我们的这个记录里面所包含的，它都是取了一个反的意思。Ok 。那么所以这个其实就是我们的一个布尔查询 must must not 以及是它的一个数的。那么当然除了这个以外的话，我们还能够再去做一个组合。组合的话就是把我们的这三项 must should 和 must note 都把它们给结合起来去做一个使用。那么也是可以的，我们也来做一个相应的演示，把这个都删掉。


然后我们新来一个 must 那么 must 的话我们先可以去做一个搜索，搜索的话首先我们就使用这个 match 去做匹配。那么为了我们匹配的一个，因为我们数据量本身就不多，这个数据的话我们在这里就写一个单个文字，比方说我们就写一个慕课网的慕就是匹配我们的 description OK 。好，我们先来查询一下，我们这是可以去查询出来 4 条数据，随后我们再来做一个匹配。那么你可以在这边我们可以再去匹配一个，比方说我们在这里写上一个尼克 name 去点击 send 现在是只有两条数据，这个就是代表我们去做搜索的时候，首先我们这个也是科普写，你里面要包含一个木，然后同时你的一个尼克 name 里面又要包含一个木。所以在我们的刚刚的一个四条记录里面又筛选了两条出来，变成了只剩下两条了。


OK 吧。那么这两条的话，那么它里面是尼克 name 是包含木的， discussion 也是包含木下一条数据。那么其实也是一样。 OK 吧。好，那么这是一个 must 那么随后我们在这个下方，我们再可以去做额外的一个添加。现在我们可以来一个竖的，这个我们也来做一个条件的写入。比方说我们在这边 match 使用这个sex ， sex 唯一。那么这里其实也就是或者你或者的话，你在这边你去进行一个搜索，这边有个逗号去掉。好。现在我们是又多了一个或者的一个条件，在这里面的话其实就是说你可以让你的某一个其他的条件再去多追加一个或者这样的一个条件的匹配。那么就是前面两个是 must 下面一个是竖的，你是可以做到一个相应的匹配的。OK ，只不过我们这个 sex 在这里面本身就包含了，所以它其实或者的话它是可以把它其实就是融入进去的对吧，虽然这个数据在这边是没有什么变化，但是其实它是符合这样的一种条件的。


OK ，随后我们再可以来追加一个 master 就说我们再来做一个排除。可以来看一下，在这边写一下 must not 在这边我们可以来一个 match 比方说我们可以写一个我们这样子写一个称我们在这边改用这个 birthday 那么现在的话我们来看一下，目前其实有两条数据的话，有两个生意，一个生日是 93 年，另外一个是 92 年。那么我们把这个写过来，那么写过来的话由于它是一个 must note 所以它会把这条记录给排除。这样子的话就是当我们在搜索以后就不会是两条，它只会命中一条了点一下。然后看一下这边就只有一条数据了。那么在这边我们的一个 birthday 现在就是一个 93 年的，OK ，他把刚刚的 92 年给排除在外了。所以这样子的话其实我们就可以做到了一个组合的这种查询的。Ok 。那么如果说你数据量多的话，这个使用这种方式去搜的话，那么是可以达到一个非常不错的一个效果。当然我们在这里数据量比较少，只有 12 条。那么其实我们也是达到了一种组合查询的一个目的了。Ok 。然后我们还可以再来看一下这个 happy 插件。


这个其实里面我们尝试使用这个来做，因为你使用布偶查询去写的话，其实他写的一个内容是比较多的，很多时候可能会写错，你也可以使用这种 pad 它所提供的一种方式去做，它本身也是提供了布尔的组合查询。那比方说在这里，我们可以使用这个 description 去查一个 match 来一个木做搜索，它是可以搜索出来 4 条数据，和我们刚刚一样，点击这里的加号，它可以去做一个追加。那么在这边我们可以来赛可以去搜一个尼克宁对吧，尼克宁我们也一样去搜一个木。那么这样子由于它是一个 must 所以这个时候在这边所进行一个展示的时候是只有两条了。


另外在这个地方其实它的一个查询语句其实和我们刚刚所写的是差不多的，然后你还能够再去加一个数的，这个时候其实就是一种组合了，我们可以使用这个 sex 1 点击搜索。那么这样子这个本身就匹配对吧，数的有一个一好，然后我们再来追加一个，我们来一个 must note 这里面匹配一个 birthday 我们到这边，我们可以来把这 92 年排除贴过来点击搜索。那么这个时候就只有一条数据了。


OK ，这个其实就是一种基于布偶的一个组合查询。然后这里面的这个这一长串的一个查询语句，它的一个 JSON object 是和我们刚刚所属的可以说是一模一样的。那么你也可以把这个直接你要去使用的话，你可以把这个拷贝一下，你把这整个直接拷贝贴到我们的这个部位来直接贴过来点击查询搜索。 OK 吧，这个数据是可以被查询出来的，是一模一样的。那么这样子其实我们就已经是实现了这个布尔的一个组合查询。OK ，在实现了这个布尔组合查询的时候，其实还有一点我们是可以去设置的。就是说我们之前其实是讲了针对于某一个特定的字段去做了一个加权，其实就是一个向上的监控号，我们不仅可以针对某一个字段，我们还能够针对用户的一个搜索的数据，也可以去做同样的一个 boost 那么也就是加权为指定的一些词语去做加权，在这里我们可以来做一下。在这边。好我们使用把这个改成竖的，我们用竖的来做，这样子它的一个条件可以多一些，然后这个下方这个我们就可以都删掉了。


那么目前我们说的话是一个 match 一个是 description 一个 match 是一个 nike name 对吧？那么我们是搜同一个，我们都搜一个 description 所以我们这样子这个时候我们就要使用一个 JSON 的，因为它其实是有一个 boost 这样的一个加权的数值，我们要去配的它是作为我们的一个 BS caption 作为它的一个属性去做的。所以我们在这里去写一下我们接起他所要去查询的内容。


query 比方说我们在这里面我们去搜一下，看一下数据浏览。我们比方说可以拿一个像这个律师律师比较少，出生的律师再来一个慕课网，这样子先写一个慕课网，随后我们在这边 match 还是使用把这个直接拷贝下来拷贝一下。在这边。这个时候去搜的话，我直接去使用这个律师。律师点击 send 搜索。好，那么这个时候我是搜出来有四条数据，然后我们往下面找，在这里有一个律师对吧，律师就只有这一个。那么很明显，律师他的一个相关的分数是两分两点一分非常低。那么现在假设我能不能让我们在进行搜索的时候，如果说用户搜索匹配到，如果说包含律师的话，我想把这条记录往上排到最上可不可以？其实也是可以做的。所以我们在这里，也可以去加一个 boost 加权加一个属性叫做 boost 然后这个分数的话应该是一个数值，不是一个字符算。比方说木库网木库网的话我给她两分。然后这个律师律师的话我们现在可以把这个拷贝一下。律师这个时候分数我想给他多一点，比方说十分贬值线的。然后我们来看一下，这个时候我律师还是在这个下方，但是它的一个相关分数其实已经是逐渐提高了对吧，我们这个时候再来，现在是 12 对吧，那么我在这边我们再加个再来一个设置为20。


随后我们再来看，现在最后一个就已经不再是律师了，我们律师的话现在就已经是排在了，看一下排在了第一位，这是我们的第一位，OK ，它的分数是 23 分了。那么这样子其实我们就通过了 boost 加权为指定的一些关键词做了一个这种分数的一个加权，加权以后它就能够排在更前面。
其实它的一个道理就相当于是一种竞价排名对吧？如果说你某些用户想输入特定那些词汇，想要在你的首页去展示的话，其实也可以通过类似的一种方式做到你排名的一个顺序的一个调动榜，你可以把它排在你的首页的顶端，都是没有问题的，甚至你直接可以给他来一个 1000 分也可以。因为这个人这个律师他可能付的一个钱比较多。金主爸爸，那么你直接让他放到最开始也是没有问题的。那么这个其实就是我们在这里所讲到的针对某一个词汇的加权。


那么这样子我们这一节就讲了咱们的一个基于布偶的一种搜索，一个是树的 must 还有一个是 must 另外这三个之间他们是可以去做到一种组合查询的。那么大家在课后可以去根据这种方式多去做一个操练。那么当然你也可以去结合咱们的这个 head 去做也是可以的，因为 head 它其实它也是帮我们提供了一种可视化的操作，通过这种方式可以减少我们的一个手写手抄的一个失误率。Ok 。

[image](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/f7c0c336-afbe-4090-9777-82bd59d8d1db/2020-09-17_175439.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665GAKOR34%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T225141Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCXGiVHZbhNHGWDdvm3psIt0wCkD2mpPfZuH4uz4zpzZgIgfMo9NGFnp24I17IPNJ5JB9axpFkMH3U28%2BvnmiUM0bYqiAQIxv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDP33EOOLF8CtzdOfpyrcA9AUwcITOm7CkoRyw1qNf7Ot5QsUQbiW%2F6xBN2cwCmYNzmMWQYJzG28zN54qYaizN1en0QeC1%2Fwtd2Qa4kG4fd1fUiBvWYnvco2HbrWkfgKDbAkDt%2BIDBQUnU9LDl5ZivDSzY%2FrgiNTFQis%2BFp0YXSuDEQNw1cOVra5xTZjWQJBIYoFM6sMjBrObUbxfX7mSJKzTiggwcbVhCTfIWSYyLTAQmQzIUqWBSwiZyZaEEKJeXeWtoSGlxP%2FhdnX1qSvVvz4yDAe2THvuhxWLAEi4JHz1QZzZ3i5vRRNi%2B2PNDDnbHs1kzuYDP6kQKOKJiKLT4Rm1IjX2zGZHMvjC0TcfOaWvDW3g%2Ba7oIzmXqxLSetq%2Byq9Unzz5SupxbFHWZJtNCvFR6YfwxjBjkdq3tZ4Ogjjtmbo1oHUOot2%2F%2Br%2FCBB6GNutNAB6u1esi9quDdD4kRzjt4MY36wl4OzGzFkbn%2BenrV8Ez7G3ee%2FtSlEiCkzez1Ny0tIKr4JdOU4EuYCAzBRBckUhkbeISuIp8kzaIJ%2Funebodw4af2XpnYeCE7y2GHiXzTm5oTH54BGVp4jmGheZTXoyYhSGvERnmn6pA3%2BV0s4sCSBwMV8Rfr9k%2BXaidQKfeIvkRfAJBrnXWMMu3%2F9IGOqUBEzsq7l9HpDbvkKQEAN659V3e2K6KPHRl5mA%2BQyIrUobyxWQXY7hzCtLOBOwAJM3VDb4w0u63YXLfGoEa7pWBdKJJwKgGVzWerNjKFTPwQm8uylxIdBDUdLFsjByrCmI9JQt2e%2B1lTKXmnpZtMfcROfpeby6JES1cRVlVSnkZj%2BlWfS%2BP4QCa1DmRNPr9UgXqeh7XfyUZJpETGC6EBDJ46M152cIS&X-Amz-Signature=7fba1bbd11c91173687b6f3259ad14b284c136e64f130e4d7f4429cd7a6ca48d&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

