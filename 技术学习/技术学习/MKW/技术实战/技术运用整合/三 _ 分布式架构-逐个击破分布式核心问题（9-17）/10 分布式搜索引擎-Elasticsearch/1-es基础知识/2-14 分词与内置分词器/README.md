---
title: 2-14 分词与内置分词器
---

# 2-14 分词与内置分词器

[image](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/feeb08d3-5a1c-46f1-805e-ca129d8b9ce3/SCR-20240806-cmch.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665345FHSC%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T225134Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIHXeTrOEhjlec76M6ipatRkdmjPFiyDCj8uK3DJnkeC3AiEAieJA6a39RI0IpwpAPw8NJZmnbim5JL7qjexwnto1iCAqiAQIx%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDPRmBQ241ZI6MJ0%2F5SrcAwCdAJMuXYIgxw1PuuqRgllDokTt%2F0Eu9V%2F19ur4AcNbzea0mH1smZR46XtAbEWc91XAPp0CMj3oO9e9ZsPSdDzZJU1e6Pt%2FznC0yn%2FF43agxzWyC2nRWO3Q7ey74GCH%2BTGn1oN%2FhhaqnO%2Bwo%2Bh%2B163Ju2bb93l5Pu4268FNS%2BwSNbIWE%2FlR%2BMPeXp9DRkmh7IIrfcuf2TtYxKtcDsJxWNXlYsz%2FZfP94KW0gyZH3f2m2Cc8sqWKNKack%2FXbBVj6hK1S0LR3zsMouzY4SQB7XsGzAIVzhEeJqatnm2Gg8N%2BqXLHMRNwPZrmGdAkSAH8gM1fFWX1fBCyOtrdLBNH%2FtpqBC62zsNcYQssVpfDRBnJpZex%2Be5Ez6iIL2Kdsgw44e1EY9oj3ixgrXamRZHT%2B619tEvyJroOzIjRuPPFXnNtWz860Zr3L53Ft0icxIjcQkGMlojL2rCw29MFiNdZrnNUmGMCf7XMjinhckN1%2BmNENFAMAECpg5RDs1LX4OIPCWgC5lB64bOoK31W9KbSEl5QiOUZ1S%2BSuorerpXubRgfCGC%2Bx5jWMQP%2BsuSifm6KMu4pfJbJ7V%2BCQeyNM1NtrZL8vPjQr2EYP3tczj5xkh2vQ5c%2B%2FY3QRFpmKXatIMNbb%2F9IGOqUBRGvK2bN%2FQDRJGQ%2Fo6%2FqXp3P%2FtXaBkztVo19eIH%2BYxrHio0BzrwubSxF5BoYjX9%2F71DD%2BD5jt2Z8j8tPwXfBdlulz71ujv01iBHe5f41KghX2pFFuBAXx0P2KtSZqQg4xygNpovKfq5gKQl8ZCvvY52N9voe7yiB2omzFqFr7K41LnDTOgJ01frUZPzUwfCir4BCtQHhS0ZbSyLfJXv4kgI3q%2BlaA&X-Amz-Signature=e17f6414d95cb10d56b658222dd7258703390e130237aabe056ff61bd14af64e&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

[image](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/602e02dc-74ae-4f46-b0bd-d2ec13c3c88a/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665345FHSC%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T225134Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIHXeTrOEhjlec76M6ipatRkdmjPFiyDCj8uK3DJnkeC3AiEAieJA6a39RI0IpwpAPw8NJZmnbim5JL7qjexwnto1iCAqiAQIx%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDPRmBQ241ZI6MJ0%2F5SrcAwCdAJMuXYIgxw1PuuqRgllDokTt%2F0Eu9V%2F19ur4AcNbzea0mH1smZR46XtAbEWc91XAPp0CMj3oO9e9ZsPSdDzZJU1e6Pt%2FznC0yn%2FF43agxzWyC2nRWO3Q7ey74GCH%2BTGn1oN%2FhhaqnO%2Bwo%2Bh%2B163Ju2bb93l5Pu4268FNS%2BwSNbIWE%2FlR%2BMPeXp9DRkmh7IIrfcuf2TtYxKtcDsJxWNXlYsz%2FZfP94KW0gyZH3f2m2Cc8sqWKNKack%2FXbBVj6hK1S0LR3zsMouzY4SQB7XsGzAIVzhEeJqatnm2Gg8N%2BqXLHMRNwPZrmGdAkSAH8gM1fFWX1fBCyOtrdLBNH%2FtpqBC62zsNcYQssVpfDRBnJpZex%2Be5Ez6iIL2Kdsgw44e1EY9oj3ixgrXamRZHT%2B619tEvyJroOzIjRuPPFXnNtWz860Zr3L53Ft0icxIjcQkGMlojL2rCw29MFiNdZrnNUmGMCf7XMjinhckN1%2BmNENFAMAECpg5RDs1LX4OIPCWgC5lB64bOoK31W9KbSEl5QiOUZ1S%2BSuorerpXubRgfCGC%2Bx5jWMQP%2BsuSifm6KMu4pfJbJ7V%2BCQeyNM1NtrZL8vPjQr2EYP3tczj5xkh2vQ5c%2B%2FY3QRFpmKXatIMNbb%2F9IGOqUBRGvK2bN%2FQDRJGQ%2Fo6%2FqXp3P%2FtXaBkztVo19eIH%2BYxrHio0BzrwubSxF5BoYjX9%2F71DD%2BD5jt2Z8j8tPwXfBdlulz71ujv01iBHe5f41KghX2pFFuBAXx0P2KtSZqQg4xygNpovKfq5gKQl8ZCvvY52N9voe7yiB2omzFqFr7K41LnDTOgJ01frUZPzUwfCir4BCtQHhS0ZbSyLfJXv4kgI3q%2BlaA&X-Amz-Signature=ed8506654addc62fb8b40df09a62edb314b83eacbd8d9965601b6c8f08722bae&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

那么这一节课我们一起来讲一下这个 ES 中的一个分词。那么其实我们在之前就已经是涉及到过这个一些文本的分词了，那么在这里我们具体来说一下。那么分子的话，那么其实它就是把一整段的文本，那么要把它做一个切分，要把它做一个分析，把里面的一些词汇单词一个一个的给拎出来。那么这样子这整个过程其实就是称之为是分词，那么也就是称之为叫做 analysis 那么 ES 的话它默认只针对于一些英文的语句，英文的文本去做一些分析和分词，那么中文它是不会支持的。这个我们之前也是提过了。那么中文的话不管你是你的一个中文的语句有多长，或者说你包含了多少个整体的一些词汇词语，那么他都会把你的所有的中文的单个的**一个字**拆分为作为独立的一个词汇去处理的。所以它末日的话是不会识别中文的，它只支持英文。Ok 。那么不管是 ES 像solo ，如果说你用过 solo 的话，就是它默认的话它也是不会去支持这个中文的分词的。中文分词是需要我们后续自己去加入的。


那么我们先来看一下关于它分词的一些 API 那么比方说我们可以做一个全局的去分析。那么先这样子我们使用这个 post 因为我们会携带一些 Jason 的，这里指定一下 Jason 然后我们要去做一个分析分析的话那么其实就是使用下划线 analyse 那么这个就是它的一个关键字关键词语，随后你要去指定一个 JS 串。然后首先我们要去做一个分析的话，那么你肯定要使用某一个分时器，所以在这里我们可以去写一下 analyze 那么这个就是代表我们可以去指定某一个分子器的。那么分子器的话有多种，那么我们先使用它最基本的一个默认的分子器，这个是标准分词器。


好，随后我们要去分析一段文本，那么文本的话就是 text 随后在这里面我们可以去加入一些相应的内容，比方说 I study in [mk.com](http://mk.com/) 那么这一段语句这个时候我要来做一个分析，我们的点击 send 来看一下。那么可以看到他会把我们这里面的只要是每一个单词的话，他都会帮我们去做一个拆分。那么可以看到 I 是一个单词， study in [m.com](http://m.com/) 这些都是一个一个的单词，那么它会帮我们做一个拆分。Ok 。那么如果说我们是一段中文的话，写一下我在慕课网学习点击 send 那么这个就正如我们之前以前，我们所演示的每一个中文，它都会把它拆分为一个一个的个体。


Ok 。如果说我们使用了中文分词器的话，那么像学习它就是一个词语，它是会放在一起的。Ok 。那么除了像这种全局的一种分析的话，那么我们也可以去使用我们现有的一个索引库，那么可以来写一下。那么我们先找一下，在这里我们可以来看一下，我们可以使用像 name 或者说是 description 那么指定一下。那么在这里 body 里面我们也要写上一个相应的决策数据，把前面的这个拷贝过来。那么这两个其实都是一样的。就是说你要在某一个索引下去做一个分析的话，那么你是只要在这个里面你去加上一下，加上这个索引的名称买 Doc 然后这个 JSON 的话除了 analyst 以及是 text 那么你再去加上一个 field 那么这个就是你要去指定去分析的那一个字段的名称。你可以使用 name 或者说你可以使用 descriptiongs C 都可以。那么在这里我们也是使用英文 study in mk 点击线的。


OK study in M 可都会被我们做一个分析。那么这个是基于我们现有的一个索引库，那么当然把这里改成 name 也OK ，也是可以去做的，因为他们本身这两个他们都是 tax 的一个类型。那么这两种方式其实都是可以去做一个我们索引的一个分析的。Ok 。那么除了这种 standard 以外，那么其实还会有其他的一些内置的分子区的类型。那么 standard 那么其实它是默认的。那么默认的话，那么我们在这个里面的文本，只要是一些单词的话，它都会被我们进行一个拆分，都是会被 ES 去拆的。然后需要注意这里面的话如果说你使用到一些大写的话，那么它是也会被转换成一些小写的，我们来演示一下我们使用这个 stand 在这里我们可以先写一下写一段文本，比方说我们写长一点 my name ISP 车帕克。好，然后我们来一个逗号， I am a super file 好。 OK 随后来一个点号空格，再来一个 I dont like the criminals。好点击线的。


然后我们来看一下它的一个最终的结果，我们先把这个拉上来可以看到。首先我们的 my 那么这个的话其实我们本身是一个大写，它会帮我们转换成小写， my name is Peter parker 然后我们的这个帕克后面我是故意加上了一个逗号，再加上一个 I 那么他也会帮我们做一个切割，那么帕克和 I 会被分割开来。然后 am 一个单词也是一个单词 super hero 最后 I dont like the criminals OK ，然后这个 C 它也会被转换成一个小写。那么可以看到就是我们所有的内容这里面涉及到的这个 MI 然后又是一个 I 和 C 的话就是大写会被转换成小写。那么这个其实就是它默认的内置的一个标准分词器。那么除了这个以外的话，那么其实它还会有我们可以在这里写一个，它第二个叫做 simple 我们可以使用这个，这个也是它的其中的一种内置的分词器，我们先来执行一下。那么执行以后来看一下。


那么在这执行完毕以后里面，其实你会发现它会有一个 dont 那么 dont 它其实会有一个相当于是一个单引号，这个单引号的话其实会被进行一个拆分。那么 simple 的话其实它的意思其实就是它会按照一些非字母去进行一些分词进行一些拆分。此外它的大小写和我们的标准分词器也是一样的。那么大写会被转换为一个小写。那么在这里面，比方说在这边我们随便去加一些字符加一些非字符，就是说1，然后 2 在这里加上一个3，随后在其他地方再加上一个10，我们再来点击一个 send 随后我们还能够再来观察一下。那么你会发现在这个里面其实也是一样，它其实本质上就是按照一些非字母，如果说不是一些字母的话，它会帮我们给去除的。OK ，你会发现其实这里面分词过后的内容，它并不包含我们之间我们之前所加的一些相应的数值，这些数字头都会没有的。好我们都去掉。好。那么这个是一个simple ，除了 simple 的话，它还会有那么这个叫做空格 white space 线的看一下，那么这个是根据空格去做一个拆分。那么根据空格的话，那么很明显我们从这里其实我们就应该能够猜到，如果是空格的话，那么帕克逗号 I 那么这个的话其实它会归类为是一个单词，我们可以往下面看去做一个验证。


那么在这个地方，很明显这个帕克逗号 I 那么它是会放在一起的，它这个就会被认为是一个单词。Ok 。所以 white space 的话它是根据它的一个空格去进行拆分的。


另外需要注意就是说 Y space 的话由于它是根据空格，所以你可以发现这里面的一些单词，就是说它的大写其实还是包含的像这个 christmas 的 C 另外还有是像这个 super Q 大写的 S 和 H 其实它都会，它不会被转换成小写的。Ok 。那么这个其实就是根据空格也就是 white space 去做的一个拆分和分词。那么除了这个以外的话，那么它还会有一个叫做 stop 那么 stop 是什么意思？那么这个是指我们的一些单词，这里面其实这一整串里面的话，你会发现像这个还有是比方说找一下像这个词，那么这些其实都是一些没有意义的单词，它只不过是一些修饰词或者说是一些助词。那么在英文里面其实它本质上是没有任何的意义的，像 saran 意思等等，其实这些我们都是可以完全的去除的。那么如何去去除，如何去做拆分的话，那么就使用这个 stop 就可以了，我们可以来看一下。


点击 send 随后我们可以往下面看。在这个里面可以看到 like Sir 这个 Sir criminals 这个 Sir 已经是去掉了。那么随后我们再往上面看的话，像我们之前 IM 找一下 IM 修不修手，这边有一个对吧，这个也是被我们给去掉了。另外再往上面找 my name is 皮特帕克，这个意思也被去掉了。所以说所以像这种一些没有任何意义的这种单词的话使用 stop 那么这个分子器的话它是会帮我们做一个相应的拆分的，这些它直接会被去除。


好。那么除了这个以外，那么还有最后一个就叫做是 keyword 那么这个就是我们之前有过介绍，就说 Q 的，它是会把这一整段的文本作为一个关键字。那么关键字的话，那么它就是它不再会作为一个文本去对待了，它就是把它当做是一个词汇。所以当我们去运行的时候，那么这一段文本的话它就会被当作是一整段一个单个的单词，它是不会做任何的拆分的。点击 send 可以去看一下。


Ok 。在这里面这个就只有一项，这一整段的文本它就是一个 token 它就是一个词汇，它是不会帮我们去做任何的拆分的。Ok 。那么所以对于它内置的一些分词器的话，总共是有五种标准的 standard simple 简单的空格的 one space stop 是去除一些无意义的单词，另外还有是一个 keyword 关键字。Ok 。


那么这些我们这节课所讲的这些内容的话，我们后续也是会以一个文档的形式提供给大家可以看一下在这里这是，什么是分词器？ ES 内置的一些分词器在这里都会有。然后大家拿到这个文本以后，拿到这个笔记以后，那么可以去做一些相应的一个练习主要是这个 API 的使用。另外是我们涉及到这四种这五种五种内置的分词器可以去看一下。那么中文分词器的话，我们会在后两节去说一下。

[image](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/f659b6b5-0142-4076-9438-58453f513672/2020-09-17_174648.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665345FHSC%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T225134Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIHXeTrOEhjlec76M6ipatRkdmjPFiyDCj8uK3DJnkeC3AiEAieJA6a39RI0IpwpAPw8NJZmnbim5JL7qjexwnto1iCAqiAQIx%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDPRmBQ241ZI6MJ0%2F5SrcAwCdAJMuXYIgxw1PuuqRgllDokTt%2F0Eu9V%2F19ur4AcNbzea0mH1smZR46XtAbEWc91XAPp0CMj3oO9e9ZsPSdDzZJU1e6Pt%2FznC0yn%2FF43agxzWyC2nRWO3Q7ey74GCH%2BTGn1oN%2FhhaqnO%2Bwo%2Bh%2B163Ju2bb93l5Pu4268FNS%2BwSNbIWE%2FlR%2BMPeXp9DRkmh7IIrfcuf2TtYxKtcDsJxWNXlYsz%2FZfP94KW0gyZH3f2m2Cc8sqWKNKack%2FXbBVj6hK1S0LR3zsMouzY4SQB7XsGzAIVzhEeJqatnm2Gg8N%2BqXLHMRNwPZrmGdAkSAH8gM1fFWX1fBCyOtrdLBNH%2FtpqBC62zsNcYQssVpfDRBnJpZex%2Be5Ez6iIL2Kdsgw44e1EY9oj3ixgrXamRZHT%2B619tEvyJroOzIjRuPPFXnNtWz860Zr3L53Ft0icxIjcQkGMlojL2rCw29MFiNdZrnNUmGMCf7XMjinhckN1%2BmNENFAMAECpg5RDs1LX4OIPCWgC5lB64bOoK31W9KbSEl5QiOUZ1S%2BSuorerpXubRgfCGC%2Bx5jWMQP%2BsuSifm6KMu4pfJbJ7V%2BCQeyNM1NtrZL8vPjQr2EYP3tczj5xkh2vQ5c%2B%2FY3QRFpmKXatIMNbb%2F9IGOqUBRGvK2bN%2FQDRJGQ%2Fo6%2FqXp3P%2FtXaBkztVo19eIH%2BYxrHio0BzrwubSxF5BoYjX9%2F71DD%2BD5jt2Z8j8tPwXfBdlulz71ujv01iBHe5f41KghX2pFFuBAXx0P2KtSZqQg4xygNpovKfq5gKQl8ZCvvY52N9voe7yiB2omzFqFr7K41LnDTOgJ01frUZPzUwfCir4BCtQHhS0ZbSyLfJXv4kgI3q%2BlaA&X-Amz-Signature=a70723af4d6fe246bc67694d6648067b911ee69fafab2f2553878fa1e3993ab4&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

