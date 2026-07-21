---
title: 3-3 dsl搜索 - 入门语法
---

# 3-3 dsl搜索 - 入门语法

[image](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/5204effe-0351-4bbb-8ac1-64e47310a961/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666MJ6NIT4%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T225137Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQD1Rdw9JgsksMLFhEK5J7j3bgwkBCffTfLnDzdE8yefswIgRBHWGMhwQKT1dQAfqUssps51HD5B4dnpAZvIno%2F4npcqiAQIxv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDILh1cYhoi8Bf%2F4LsCrcA4A73AhIj5F0yGbItSOkUTYjjWqkt4v2CbCRIYrz%2FpMrpfstj3Jkh3rfGe5icF8E7%2Bs%2FGF6PDTwcvlHVrXElpqgiYFXAyBXNSuXjD%2BuPTMC%2Fc%2BHIOu4qXB%2BKe04tJMRln4%2FzN6g3wGk3S%2BLGvczibBXmssiVPK3G39VANqnL2FYQnTkxCxXtD40qGO73OjXr0cQWmbivpWlZlC8erRbXGRAHuLs4hxhRwj%2F2C%2BEKad6FdZfMa2rKE6z%2Be8KknP15v%2B%2B2EkyjXq%2BWOErSaqrlK0pu67uxt3SuZJEkimb0vZxsBp7pl6BQe3w793%2B%2Fj96ozHvZ%2FWHuPrIZgAkkhUQJGzTp%2FUKIPRI0px5PT6120EZ%2BUN%2F9I25lfGg2QrlS4aaandC3UIDGyble78lnoDpSiVVjvHEJuHlGSeIdd6YOpGrd4LvJkC7L6wJeXiTE%2FexvSfJXHCFL%2BLrZB%2FZcH3uWhR1f%2FvEnmgkAS6wCUCU8tCr7crEylnW4Pgag7K4bbdqds4hzulr%2FwYXHm5mPeqHJer5qJhaxuz0Q35EkeSH8J6no1Kl%2F5ZTpLWngwE9Lw7BSkREhtimGrKCa88Ezvb4J2ZJkd6YpYxbh6fspCGywYLKN4IdDqdXo5qfScgxLMJm3%2F9IGOqUBfu0yqmbY0kNesPSUElP8Y3jdGFPwF3otNtFjpAaJ8l3MH1O2Pst19uncNvHk2cfvb6vWcAuiwh4R7ebX9bjvoaUl3UonFX1NpU5hGJ4dnbpOZgRuz13B7h7RbgTrpki1wSebVQIUH12jRSW3FHXn5s%2BwV8EQ3xdKpnqivxuPx0wOyBz8wHR5O2jZCHIYDNe6bixjcKdtYR2%2Bv03Q8bDcyFR1X%2Bn1&X-Amz-Signature=45776c03059e6a993a29a0a28680fe14ec9c7ed771e6ef923b29abdd5a17c1b1&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

[image](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/6bd7ac8f-5ac4-4b06-86b1-7cc22554686f/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666MJ6NIT4%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T225137Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQD1Rdw9JgsksMLFhEK5J7j3bgwkBCffTfLnDzdE8yefswIgRBHWGMhwQKT1dQAfqUssps51HD5B4dnpAZvIno%2F4npcqiAQIxv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDILh1cYhoi8Bf%2F4LsCrcA4A73AhIj5F0yGbItSOkUTYjjWqkt4v2CbCRIYrz%2FpMrpfstj3Jkh3rfGe5icF8E7%2Bs%2FGF6PDTwcvlHVrXElpqgiYFXAyBXNSuXjD%2BuPTMC%2Fc%2BHIOu4qXB%2BKe04tJMRln4%2FzN6g3wGk3S%2BLGvczibBXmssiVPK3G39VANqnL2FYQnTkxCxXtD40qGO73OjXr0cQWmbivpWlZlC8erRbXGRAHuLs4hxhRwj%2F2C%2BEKad6FdZfMa2rKE6z%2Be8KknP15v%2B%2B2EkyjXq%2BWOErSaqrlK0pu67uxt3SuZJEkimb0vZxsBp7pl6BQe3w793%2B%2Fj96ozHvZ%2FWHuPrIZgAkkhUQJGzTp%2FUKIPRI0px5PT6120EZ%2BUN%2F9I25lfGg2QrlS4aaandC3UIDGyble78lnoDpSiVVjvHEJuHlGSeIdd6YOpGrd4LvJkC7L6wJeXiTE%2FexvSfJXHCFL%2BLrZB%2FZcH3uWhR1f%2FvEnmgkAS6wCUCU8tCr7crEylnW4Pgag7K4bbdqds4hzulr%2FwYXHm5mPeqHJer5qJhaxuz0Q35EkeSH8J6no1Kl%2F5ZTpLWngwE9Lw7BSkREhtimGrKCa88Ezvb4J2ZJkd6YpYxbh6fspCGywYLKN4IdDqdXo5qfScgxLMJm3%2F9IGOqUBfu0yqmbY0kNesPSUElP8Y3jdGFPwF3otNtFjpAaJ8l3MH1O2Pst19uncNvHk2cfvb6vWcAuiwh4R7ebX9bjvoaUl3UonFX1NpU5hGJ4dnbpOZgRuz13B7h7RbgTrpki1wSebVQIUH12jRSW3FHXn5s%2BwV8EQ3xdKpnqivxuPx0wOyBz8wHR5O2jZCHIYDNe6bixjcKdtYR2%2Bv03Q8bDcyFR1X%2Bn1&X-Amz-Signature=a80b855a81ea4053009ced51a348bfad79fee923153b42510406cc0e54e7e7d3&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

那么当我们准备了这样的一些数据以后，那么我们就可以去做一些相应的搜索了。那么我们可以先来看一下。我们先来根据我们的一个幕后网，也就是在我们的 description 简介里面，其实在这里面包含了很多慕课网的一些内容，主要是有三条数据都包含了慕课。那么我们在这边我们就可以去做一个搜索。那么如何去搜呢？我们在这个 URL 中去构建我们的一个请求，在这边使用 get 这样，我在这里重新再开一个使用 get 然后把这个地址拷贝过来，请求的是在 shop 这个索引中。


然后我们要去搜索。搜索的话其实要指明一定要加上一个 search 那么这个就相当于是它的一种搜索的规范，指定了收取以后，那么我们就可以根据一些组合的条件去查询去解锁我们的一些数据。然后在这边我们通过 URL 去构建我们的一个数据。的搜索的话，在这个后方加上一个问号，然后写一个 Q 代表是 query 等于。那么现在我们要去查询的话，其实是要去基于我们的一个 description 去做一个查询，所以在这后方你加上 desc 那么要去检索的一个内容的话，那么在它的后方去加上一个冒号，随后写上一个慕课网。那么这样子的话其实就代表我们要去做一个查询。那么这个查询的一个属性，它的 field 叫做 description 检验锁的内容叫做慕课网，然后 Q 的话是代表一个检索，要去通过这样的一个字段外加它的一个值，其实也就是一个QL ，去做一个查询，点击 send 一下。那么这个时候在这边我们就能够查询出来相应的内容，在这边看一下。


总共是有三条数据，这边有一个慕课网，然后在这里我在慕课网学习，这是他的一个 description 随后在这里又有一个慕课网，再然后还有一个那么在这里的话总共是有三条数据， OK 吧，那么三条数据的话，那么其实我们现在是通过这种基于 y2 的形式去进行的一个搜索。


好，然后我们再来换一个条件。那么这个时候如果说我要增加一个额外的条件，那么可以来看一下，在这边我们有一个以这个 age 为例，这边这个 age 他是 18 岁，然后其他的还会有一个 22 岁以及是这个 20 岁。所以我们可以进行一个多条件的搜索，在这个后方加上一个并且这样的一个符号。随后那么还是一样，我把这前面的拷贝一下，把这个拷贝过来。那么前面的这个拷贝过来以后，那么其实这个东西我们也说了，它就是一个键值，对吗？写上一个 H 然后你再去写上一个，比方说 20 岁来做一个搜索。那么这个时候在这里 peace 它总共就只有一条数据的这个 eq 代表是等于总共是有一条数据是被命中的。那么然后在这里的话它就只有是一个 20 岁在这边吗？那么这是它的一个底斯科学。


好。那么这样子的话其实我们就是做到了一个，在我们的这个 URL 里面，通过我们的两个参数进行了一个拼接，做了一个查询。那么这种方式的话其实我们是称之为是叫做 query stream 格尔斯俊其实就是在我们的这个 URL 里面去构建一些相应的搜索的条件，把一些查询的参数等等都是构建在这个 URL 里面去进行搜索的。那么我们可以称之为是一个叫做 query string 那么 query 斯俊怎么写就这样子， query string 就是请求的一些字符串。那么因为本身我们写在这个 URL 里面，它就是一个字符串，所以就是一种会不会实现的一种方式。


好随后我们再来看一下，我们来验证一下我们之前所说的一个叫做 keyword 就是一个 text 那么在这里面我们还是以这种 query 咨询的方式去做一个相应的查询。在这里 Q 然后我们来写一个叫做 nike name 我们来先看一下这里边有一个 super hero ，这个 super hero 有一个 user name 和一个尼克 name 我都叫做 super hero 可以搜一下 super 空格 Q 这两个都是匹配的。那么然后在我们的这个索引的信息里面，那么这两个其中一个叫做听我的 user name 它是一个 keyword 另外一个尼克 name 它是会做一个倒排索引的，那么它是一个 text 随后我们就可以来做一个相应的测试了。测试的话，那么在这里面我们还是一样使用科瑞斯俊的方式，我们先去解锁这个尼克内冒号 super 搜索一下查询。那么这个时候我们在这边能够查询出来一个数据，在这里有一个尼克 name 它是一个 super hero 因为这个 super hero 的话其实由于它是使用的是 text 它会做一个倒排索引，他会把这个数据做一个分词，有一个 super 还有一个是 fail 所以当我们去进行搜索的时候，这个 super 就可以把这里面的这个数据给搜索出来。


好，然后我们再把这个改一下，把这个 nike name 改掉改成 user name 随后我们再来去做一个搜索，那么你会发现它搜索不了任何的内容。那么这个就是因为我们的这个 user name 。其实我们在之前把数据做一个新增，添加的时候，由于它是一个 Q 的，所以西方 Q 它是不会帮我们去做一个分词的，它会把这个 super Q 作为一整个关键的词汇，它本身的 cql 就是一个单词，你要去查询的话，其实就应该要做一个精确的匹配，你要把整个 cvq 给输入进去，那么它才会把相应的数据给你拉出来。


那么这样子的话，比方说我们在这边我们写上一个 hero 点线的，那么它其实也是搜不了的，你要这样子你要去写上一个 super 空格，再来一个 cue 点击 send 查询，那么这样子的话它才能够做一个完全的匹配，把这个数据给查取出来。OK ，那么这个其实就是一个 keyword 那么这样子我们就验证了我们在之前讲 keyword 以及是 text 它们之间的一个区别。那么在这里我们就临时通过这样的一个操作做了一个相应的讲解。那么这个其实就是他们之间的一个区别，需要注意，那么就可以了。


Ok 。那么这样子就是我们现在其实我们所做的一个操作都是基于这种使用 get 请求，然后都是在这个 URL 中去构建的。那么这个其实就是科尔斯俊。那么这种科尔斯俊的话就是这种使用的方式，其实我们比较少不太会使用这种方式去做，因为一旦我们的一个参数复杂了，那么其实就会比较难以去进行一个构建。所以这种查询的方式我们用的不会很多，除非是一些非常简单的这种查询方式你才会这样子去做。那么所以我们在企业里面大部分查询的话，我们会使用一种叫做结构化搜索的这种方式去做。那么这种方式的话我们称之为是 DSL 这种查询的方式。 gsl 是什么意思？其实就是这样子 gslgsl 这样子去写的。那么这个 gsl 全称的话其实是称之为叫做左面是 basic 连位置，那么它是一种特定领域的一种查询语言，它是使用 JS 的格式去构建，是去查询数据的。所以像我们之前在这个 URL 里面去构建的这种参数的话，在我们使用 GS 幺以后，那么我们的所有的数据其实我们全部都会去使用一个 JS 的方式去做一个查询，那么它其实就是一种结构化的一个查询方式。那么使用这种方式的话，那么查询的话它会更加的灵活，更加的方便，更加的有利于去做一些复杂的查询。因为我们在后面我们会涉及到像一些高亮查询、分页，还有是一些多条件的去查询搜索。那么其实我们都可以把它构建在一起，通过一个 JSON 就可以去做了。


那么在这边的话我们可以来看一下如何去通过这个 DSL 去做一个相应的查询。那么由于要使用这个杰森，所以我们在这边改成 post 这种请求方式。那么在这个前面都是一样 shop 下划线，然后在这边你还要这样子加上一个 Doc 就是我们的一个 Doc 再来一个下划线 search 那么这个就是代表我们要在这个 shop 下方要去查询我们的一些相应的文档了。所以我们在这个杰森先去到这个 body 里面去找一下，把这个 JSON 先去写好，先来看一下它的一个搜索方式。


首先你要去构建一个 JS 这样的一个 JSON 体，随后我们要去做一个查询，比方说我们现在要做一个 query query 就是一个查询。最后再来一个 match 先不用管这个 match 是什么意思，因为我们在后面会去说的。那么这一节我们仅仅是讲这个 zsl 这种结构化搜索的一种使用方式，JSON体以及是它的一个基本的操作的语法。那么其实本质上就是一个 JSON 体，好使用这个 match 然后再来做一个搜索。那么 match 的话我们是要去做一个匹配求解锁。然后我们要去搜索哪个内容，其实就是比方说搜一个迪斯科皮，然后再来加上一个叫做慕课网，随后我们就可以去发起一个请求了。
然后看一下这边我们的查询的这个 header 设置错了，这是一个 javascript 其实我们要去杰斯，使用这个杰斯。那么其实我们在进行一些搜索的时候，往往会出一些小的一些细节的小问题。那么像现在就是他就把这个错误的信息反馈给我们了。也就是说当我们做一些检索查询，出现一些不规范的、不合格的一些语法错误的话，那么 ES 它会报一些相应的异常，会把这些异常信息给抛出来。Ok 。那么像现在就是我们的一个设置的开表是错误的，你只要把它改成这个 JS 那么你就可以去做一个查询点击线的。然后在这边你又会发现报了一个错。在这边说我们这个杰森在进行一个格式化的时候会发生一个错误，来看一下。


其实我们在这里面我只是发现有错误，但是在这边他还是会说 N expected 有一个字符，不是他所期待的。也就是在这里这边打了个叉的位置。那么其实很明显这边是少了一个冒号，把这个冒号给加上。注意要使用英文的这个冒号再次点击线的。那么这个时候我们的数据就能够被我们给查出来。那么在这里我们搜索这个 description 是慕课网的时候，那么他会把我们这些内容全部都给搜出来。慕课网，那么他会帮我们做到一个相应的匹配，总共是命中了有三条数据。那么如果说你在这里边，比方说像这个 match 值是 ES 中的一个关键字，你写一上一个1，那么很明显它还会报错。说我们这个进行解析的时候是解析不了，他会发现说 no query Redis 也就是说我们这个 match 1 match 1 是它的一个关键词，在我们的 ES 中没有被注册，所以你这种方式是不对的，那么你把这个给改掉就可以了。


所以说当我们在出现一些查询上，不管是你的结构出现问题，还是你查询的语法出现问题，或者说某一个字漏写了，他都会帮我们提示说我们的这个查询出现了一些问题，你是需要去做一些检查，那么这个就是发生一些这种相应的查询的一些问题。那么 ES 帮我们做了一个解锁的过程，他会帮我们把这些错误的信息给反馈出来，随后你再去根据他的一些错误去把我们的这些数据不管是我们的一个语法错误还是什么错误去做一个相应的调整，那么最终的话他就可以把我们所期待的一个结果给搜出来。那么这个其实就是他的一种自己的方式。好那么这个其实我们就实现了这种使用 JS 格式去做了一个查询。那么这种方式的话其实就相当于是在我们的这个浏览器的一个里面去写，那么就相当于是一个 Q 然后短语 description 冒号默克网其实就类似于这种方式去做的一个查询，只不过我们现在使用这种 JS 的方式去做了。


那么除了这种 match 这种方式的话，那么其实还能够再去做一个相应的测试。我们把这个迪斯科技给改掉，改成了这个 user name 也是演示一下之前科瑞斯基的一种方式，搜一个 super 远致 send OK 查询出来是零条数据，因为我们也说了它是一个 keyword 好我们把它改成这个尼克宁，我们再去做一个查询。那么这是可以的，它是可以把相应的数据给查出来。随后我们再把这个娱乐内容恢复成这个，我们修普尔空格 Q 再去做一个查询。那么这样子的话他做了一个完全匹配，因为他是 Q 的，所以他可以把这样的一个数据给解锁出来。


好，随后我们再来讲另外的一个关键字，这个关键字叫做自动存在 exist 然后是让我们去做一个判断，判断某一个字段是否存在这个字段，如果存在的话会把相应的数据给解锁出来，那么这个字段其实就是属性也都是这个 field 在这里面，这边我们就可以写这个 description 或者你可以去写一个 user name 这个东西，只要是对应在我们这个里面存在于这些列的话，那么其实它都可以帮我们给搜出来。现在查询一下。


在这边可以看到总共是有 12 条数据， kit 命中了 12 条，随后这个下方就会包含一些相应的数据，因为这些数据的话它是包含了这个 feel 的，你就是 user name 是有的。如果说我们来一个 user name 1 这个属性是不存在的点击 send 那么在这里面 hit 0 条数据，是没有任何数据查询出来的。 OK 吧，那么这个其实就是我们的一个 DSL 的一个搜索方式。那么 DSL 的话那么它的一个基本语法其实就是一个 JSON 那么 JSON 的格式是一定要去匹配的，所以如果说有 Jason 的语法错误的话，那么肯定是会报错的。另外的话对于我们的一个关键字，那么其实这里面就是一些相应的 kpl 的一些舰队，它其实也是包含了一些杰森的奥布点。像这个 query query 它是一个 key 然后 fail 的话它是一个 JSON object 另外它是可以做一个嵌套的。然后在这里面又可以是包含了一个 KB 楼，但是这个 KB 楼的话就是一个 K 也就是它的一个字符串配合一个字符串，那么这个就不再是一个 S object 那么这一点是需要去注意的。


另外作为我们 K 的话，这个 K 它可以是 ES ST 设置它所包含的一些关键字，它也可以是某一个字段。因为刚刚我们也写了，你可以写上一个 discussion 或者说你可以去写上某一个 user name nickname 那么这个本身就是我们的一些 feel 的一些属性，你也可以去写。那么这个其实就是作为我们这个 GS 2 基本使用一种格式，基本使用的一种语法。那么一定要注意，它是一个 GS object OK 吧。

[image](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/9cedc024-271c-4c8a-bc1f-e33c1a02dd41/2020-09-17_174738.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666MJ6NIT4%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T225137Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQD1Rdw9JgsksMLFhEK5J7j3bgwkBCffTfLnDzdE8yefswIgRBHWGMhwQKT1dQAfqUssps51HD5B4dnpAZvIno%2F4npcqiAQIxv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDILh1cYhoi8Bf%2F4LsCrcA4A73AhIj5F0yGbItSOkUTYjjWqkt4v2CbCRIYrz%2FpMrpfstj3Jkh3rfGe5icF8E7%2Bs%2FGF6PDTwcvlHVrXElpqgiYFXAyBXNSuXjD%2BuPTMC%2Fc%2BHIOu4qXB%2BKe04tJMRln4%2FzN6g3wGk3S%2BLGvczibBXmssiVPK3G39VANqnL2FYQnTkxCxXtD40qGO73OjXr0cQWmbivpWlZlC8erRbXGRAHuLs4hxhRwj%2F2C%2BEKad6FdZfMa2rKE6z%2Be8KknP15v%2B%2B2EkyjXq%2BWOErSaqrlK0pu67uxt3SuZJEkimb0vZxsBp7pl6BQe3w793%2B%2Fj96ozHvZ%2FWHuPrIZgAkkhUQJGzTp%2FUKIPRI0px5PT6120EZ%2BUN%2F9I25lfGg2QrlS4aaandC3UIDGyble78lnoDpSiVVjvHEJuHlGSeIdd6YOpGrd4LvJkC7L6wJeXiTE%2FexvSfJXHCFL%2BLrZB%2FZcH3uWhR1f%2FvEnmgkAS6wCUCU8tCr7crEylnW4Pgag7K4bbdqds4hzulr%2FwYXHm5mPeqHJer5qJhaxuz0Q35EkeSH8J6no1Kl%2F5ZTpLWngwE9Lw7BSkREhtimGrKCa88Ezvb4J2ZJkd6YpYxbh6fspCGywYLKN4IdDqdXo5qfScgxLMJm3%2F9IGOqUBfu0yqmbY0kNesPSUElP8Y3jdGFPwF3otNtFjpAaJ8l3MH1O2Pst19uncNvHk2cfvb6vWcAuiwh4R7ebX9bjvoaUl3UonFX1NpU5hGJ4dnbpOZgRuz13B7h7RbgTrpki1wSebVQIUH12jRSW3FHXn5s%2BwV8EQ3xdKpnqivxuPx0wOyBz8wHR5O2jZCHIYDNe6bixjcKdtYR2%2Bv03Q8bDcyFR1X%2Bn1&X-Amz-Signature=ed8abf9231696f377271b5600725ed1b4920469021c7667ea15c948cf8984134&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

