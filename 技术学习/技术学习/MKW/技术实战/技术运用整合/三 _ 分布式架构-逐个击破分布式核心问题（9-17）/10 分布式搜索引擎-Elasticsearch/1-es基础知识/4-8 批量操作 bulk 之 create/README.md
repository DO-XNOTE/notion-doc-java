---
title: 4-8 批量操作 bulk 之 create
---

# 4-8 批量操作 bulk 之 create

[image](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/965ec677-4be4-48c5-81e2-61adc7b4055d/SCR-20240806-feft.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466R66Q4PSG%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T225148Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQC7UMRmrx1c6M1PZlbFA9xIiC0jAPJQZVJyqikGCjIq%2FwIhAPvnCnbWAbW0Fuvdw1lkPQKZxapite6HWdmmR%2FpPOEjjKogECMb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgzqPwuWyIdtWvk6ttUq3APs9cipipZcOAruDLhXtIGbMl7t%2FAjngVUZa%2BDcH%2FY2QValTq7EY%2FPPZqA1ilv3c27lEA8%2Bc%2B3GxxOLYPefn9%2BeJB1%2BecQRa2ZA%2BLV%2Fch01vTgsFg13N4qyj7BSD7czWDrBoKDgPzKYUUkFwnsCFxbZy02%2Bc%2BmU%2BTggiDJ97Qhu%2BH%2BD5bzIEMSdb7%2FNjjoeYWKVDKptrQhUq18MVlr1%2FKi0gaJ3FDXCCoQbkuXyhvWRATfXpBeCTWMBPDZMClpUQwR225Y9QDubfb8l7LglGWtdwfiJdPp1HP%2BbvFUYYNnNRJNzfbfEpid3NiiYdOmZ8AiYTXRaU3%2B72i799pdBF9yST80vKCK6p9UvkMNDHCX0mUmYQi7Nl7XlcrWPjGRphn%2FGekx%2FgRZMYnNSkxfAA2e%2F8c5rjI4ZHJB47KcZkODpf%2BO9ko2PJtkvMBYutdCvn%2FKdaDqLZ1gUey%2F5SGgNXIiUnO07K9T5hrMrXx6%2BWp0NX0i9zMzaXiljb5UO%2Bj0STypW53YjvfsS0aK8hnCR3CyEI3zqb6gtF9FTbNSnubfzbKx%2BEFrsFsEoe7DJC5M%2BgCFggkk2RP5bA5vagLMtgqIyjzX8kpWfJYw9tLo4Jw25R33RNkm3YbsRVThrOjDAuf%2FSBjqkAZx6XDhaMClvcNnSmBmCKHz0O7u0%2BBDdi9EFQUcHy3%2B5FXkuFVGSxaS4IeiWLz0yWJJqJdN%2F9R6HHnYrdbMUWfeCY%2FWbT9xrrPhQzsYbU1keMiviJ7mRo8BwVvn6y2qArtiPxRgZt6yjcMTNwO0wEypNZOnxv8wtfas3WT06WM%2F7w%2Fev%2B3Tp%2FFvhlUkemS7D%2FDxcEoxgADDgly6KtiRZOm2tFEe%2F&X-Amz-Signature=0e3bcb5a1233be2af5f8425fb42b93a907f2527ad587c379d7e6d291aadd7448&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

[image](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/c87771f7-3e6d-4074-a2fa-7d6558e60600/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466R66Q4PSG%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T225148Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQC7UMRmrx1c6M1PZlbFA9xIiC0jAPJQZVJyqikGCjIq%2FwIhAPvnCnbWAbW0Fuvdw1lkPQKZxapite6HWdmmR%2FpPOEjjKogECMb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgzqPwuWyIdtWvk6ttUq3APs9cipipZcOAruDLhXtIGbMl7t%2FAjngVUZa%2BDcH%2FY2QValTq7EY%2FPPZqA1ilv3c27lEA8%2Bc%2B3GxxOLYPefn9%2BeJB1%2BecQRa2ZA%2BLV%2Fch01vTgsFg13N4qyj7BSD7czWDrBoKDgPzKYUUkFwnsCFxbZy02%2Bc%2BmU%2BTggiDJ97Qhu%2BH%2BD5bzIEMSdb7%2FNjjoeYWKVDKptrQhUq18MVlr1%2FKi0gaJ3FDXCCoQbkuXyhvWRATfXpBeCTWMBPDZMClpUQwR225Y9QDubfb8l7LglGWtdwfiJdPp1HP%2BbvFUYYNnNRJNzfbfEpid3NiiYdOmZ8AiYTXRaU3%2B72i799pdBF9yST80vKCK6p9UvkMNDHCX0mUmYQi7Nl7XlcrWPjGRphn%2FGekx%2FgRZMYnNSkxfAA2e%2F8c5rjI4ZHJB47KcZkODpf%2BO9ko2PJtkvMBYutdCvn%2FKdaDqLZ1gUey%2F5SGgNXIiUnO07K9T5hrMrXx6%2BWp0NX0i9zMzaXiljb5UO%2Bj0STypW53YjvfsS0aK8hnCR3CyEI3zqb6gtF9FTbNSnubfzbKx%2BEFrsFsEoe7DJC5M%2BgCFggkk2RP5bA5vagLMtgqIyjzX8kpWfJYw9tLo4Jw25R33RNkm3YbsRVThrOjDAuf%2FSBjqkAZx6XDhaMClvcNnSmBmCKHz0O7u0%2BBDdi9EFQUcHy3%2B5FXkuFVGSxaS4IeiWLz0yWJJqJdN%2F9R6HHnYrdbMUWfeCY%2FWbT9xrrPhQzsYbU1keMiviJ7mRo8BwVvn6y2qArtiPxRgZt6yjcMTNwO0wEypNZOnxv8wtfas3WT06WM%2F7w%2Fev%2B3Tp%2FFvhlUkemS7D%2FDxcEoxgADDgly6KtiRZOm2tFEe%2F&X-Amz-Signature=815f160365a5e95d1160c2c0fadc639b161f4c72b5a84f753f82257765cd84cf&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

那么上一则我们是通过 M get 来实现了我们针对于 ID 的一些批量的查询。那么其实除了批量查询以外，那么我们还有其他的一些批量的操作，比方说我们有批量的去新增，批量的删除，批量的修改。那么这些都有这个的话，那么我们在 ES 中我们会称之为叫做 rock 可以来看一下。


在这里我准备了一份文档，这个文档叫做批量操作 block 然后在这里会有它的一个基本的语法，先来看一下。那么关于这个基本语法的话，其实在这里贴了出来。那么这个是从官网所摘敲的，然后在这里这一段内容选中的是一段请求。然后下面这一段又是第二段请求。那么这两个其实是两个不同的个体。那么在我们的这个语法里面可以包含多段的内容，那么其中它有一个 X 那么这个 X 是指的我们的一个操作的类型。那么我们可以有批量删除，批量的修改，批量的新增都是这个 action 那么在这个后方我已经是指明了它包含有 createindex update 以及是 delete 那么这个我们一会再说。


那么随后在这里还有是一个斜杠 N 那么这个其实是一个回车，就是说只要你去通过这种格式这种语法去使用我们的批量操作 bot 那么就必须要有一个回车。那么一定要注意，它的这个回车在每一行的结尾都有包括它的最后一行。那么你也要有一个回车，这个一定要去注意。


那么随后还会有一个 request body 那么这个其实就是我们一个请求题。那么请求体的话来看一下，其实就是我们在之前做一些相应的查询操作，其实就是这一段内容。那么这个就是我们的一个请求体，只不过他现在做了一个整合，为了来符合我们的一个批量的操作，所以它是会和我们的每一个 action 整合到一起，放在同一段内容里面去使用的。然后它还会有一个 meta data 那么这个是什么意思往下面看。


那么 meta data 它其实就是指我们要去操作文档的一个 enx type 以及是 ID 那么这个是我们的索引，这个是下划线 Doc 然后 ID 就是我们的某一个文档数据在我们索引中的一个组件的 ID 那么需要注意这个 index 和这个菜板，那么它其实可以去省略不写，然后在我们的 URL 中去指定也可以。那么这个我们后面会在这个下方的实操中去进行相应的一个演示。


好，然后我们再来看。那么既然我们有了这样的一个语法之后，那么其实我们就可以去操作，可以去批量的操作我们的一个相应的内容。那么对于我们的一个批量操作来讲的话，其实我们在这边我贴了很多的一些内容，那么大家可以去看。那么在这里我们采用手敲的形式方案你也可以去使用复制，那么手敲会更好，所以我们来敲一下。


那么在这里首先一个我们可以先去进行一个批量的新增，也就是创建咱们的一个文档数据。那么在这里使用是 post 在这个部分，在我们的 URL 在这里的话，那么我们直接使用下划线 buck 那么这样子就可以了。然后我们要去操作的一个文档，也就是我们的一个索引以及是类型的话，那么我们是在咱们的一个 meta data 里面去进行一个指定的。我们首先我们来一下，先写一个大括号，就代表是我们第一段的内容。随后第一个是咱们的一个 X 动作。那么第一个我们先来讲一个合一层，那么这个是代表新增，如果说这个文档它不存在，会创建。如果说这个文档它存在了，也就是它的一个组件 ID 存在了，那么你再去做一个创建，点击这个 send 发送请求的话，那么它会报错，会报一个异常，但是这个异常是不会影响其他的批量操作的。
好，然后我们先来写一下克瑞特创建。随后我们要去定一下我们的美卡内展，它其中包含了三个属性。那么第一个属性是咱们的一个索引下划线 index 随后我们要指定一下我们的索引的名称。那么在这里我们可以去看一下咱们的 header 我们使用这个 shop 2，因为这个 shop 2 的话，它其实本身里面包含的一个 mapping 映射比较简单，那么只包含了一个尼克 name 也就是一个ID ，我们选这个来操作。我们来看一下目前它的数据其实是它里面只有这五条数据，这个是我们之前用于去做测试的，那么这个我们今天不用管好。然后我们记一下，一个是 ID 一个是 nike name 这个是我们所需要去做新增的时候要用到的两个属性。那么在这里我们指一下指名叫做需要帮，这是我们的一个索引。好随后我们下一个属性。那么下一个属性的话在这里我们要指明一下我们的太太，那么 tap 其实统一的，那么我们都是下划线 Doc 好，然后再来指定一下我们的 ID 那么这个 ID 其实也就是我们创建新的文档，它的一个 ID 在这里我们可以去使用写一下，比方说来一个2001。


好，随后这是我们的第一段内容。那么有了第一段内容之后，这个时候来一个回车，我们要来第二段内容。那么第二段内容就是我们要去创建的一个文档的具体的数据。那么首先是 ID 我们可以和这个 2001 样。那么再来一个是我们的 nike name 写一下，这是 name 杠2001，那么这其实就是我们所创建的第一条数据。那么随后我们来一个回车，把这里的内容我们一下，一份，再拷贝一份。然后在这里现在我还没有坐回车，一会，我们可以来看一下她有没有报错。我们把这里面的数据做一个修改。那么先改这里，改成2002，这里是2003，然后我们点击 send 那么这个时候会报一个错说以 legal 不合法的参数这个异常。然后在这里有一个提示说我们在这边有一个 new nine 有一个斜杠 N 也就其实是我们最后一行。那么最后一行的话我们没有做一个回车，我们应该在这里回车一下。然后我们再来发起一个请求，点击 sendok 你会发现我们这个时候是运行成功的，它错可耗费了 20 毫秒。然后艾尔斯据说没有任何错误，艾特斯就说我们所创建的一个结果，在这里 results 都是可瑞奇的，都是成功的。


然后我们打开咱们的这个 header 把这个打开来做一个刷新。那么看一下数据浏览，这个时候你会发现这个 20010302 这三条数据在这里我们是批量的做了一个插入。那么这个其实就是咱们的一个克瑞斯，它可以用于去做批量的一个新增。那么在这里我们要去注意，就是说一方面我们的一个回车你是需要去注意的。虽然我们在看它的语法的时候，它有一个斜杠 N 但是在我们去写的时候，其实我们的一个操作就是一个回车一定要去按一下。那么另外我们在这里你会发现它有一个大叉，这里有一个大叉，那么这个大叉是咱们这个 postman 它的一个语法，就是说当我们在运行 postman 的时候，其实它的一个格式化。


在这里波典其实是放入一个 JS object 但是我们现在这段内容的话，它其实是可以被咱们的 ES 去解析的，所以我们在这里的话可以去不用管。那么这个就是我们的一个批量的新增，那么批量新增，那么在这里的话其实我们是指明了一个具体的 ID 那么我们再来做一次。那么在这边的话我们把这个改成200，我们这样子这个 2003 我们就是保持就不动了，我们再去把这个其他的再去做一个新增。我们可以拿一个 2004 再来一个2005，这两条数据我们改了。那么最后这一条我们并没有改，然后我们点击 send 那么这个时候的话其实它会在最后报一个异常，在这里是409。那么你会发现这个 2003 all ready exist 已经是存在了，所以它抛了一个异常，但是它并不会影响我们其他的一些数据。我们的 2005 即使 2004 都能够被正常的批量的给新增。那么可以来看一下浏览数据，这个数据有点混在一起的，你看到 24205 这两条数据，那么我们在这边就已经是批量的插入了。那么这个其实就是我们的一个，在这个 X 星中指明指定咱们的一个克瑞斯就能够达到的一个效。

