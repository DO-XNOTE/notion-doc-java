---
title: 2-1 head与postman基于索引的基本操
---

# 2-1 head与postman基于索引的基本操

[image](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/b1991972-06f2-4001-9c47-77e3b95317e5/SCR-20240805-onyo.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WB7FS5DF%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T225129Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIGn7pqlf6JE%2BppH83tto4motGM1ZZQ%2FhrWZ%2BXIBvXcnBAiEAh2%2B%2Fryh0EBtPqcdEROLdGmolj2BzL%2BjNj%2FAXartg6hQqiAQIxv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDP1iHD3ewyxxNOwKGyrcA5bntRcUYAgaI0Cl3igpexCZYhpjFXW8FNzUmGcEIaTOejIJoOAbUEL5nXwdQlAyGwdzsjdvPr%2BhfeQWDsrD8fNsCpSqBcWd6eFF5ztF68Pe5sc00gPtAtj6Z%2BarSnA9cPTILA1Sz5FuAbrZfa4z0Zeap6gHImWHCCS7qnQpReUjc3DFYKm%2Fa51Tgv%2F7eFyueVTY6qAaN6JAkRAxn3omEtI3fkwFZXR3W94H%2BMVTIhoZyOcIzG3PxDk9Q8ThihrjKhAXfLge99%2FMBb0nHFBk9g0l99d6IX3SEUTHjmWy7iDWCsc%2BG7zVQVAByv7pRRpFhA3ACIMqbNZP0%2FC2obXz2S2qSttH%2B7MgloihNT%2BfHp%2F9A38%2Ft8sHx6ZRUSxdph%2FKhK%2Bu9uC3k71S0OrPxrsMga%2BRTQKKvVvFJt0H9IWpGhIkZbh11lHnEY%2By8dVZXbLu%2FKgIbA5wBL0awTJb%2FO4wuzN2l8p3ddckvVMdzEWSaSETn0w%2Bwk1Y3oNaTZVeEmK7yP7wIpplDNJAKs%2FOoIKQev%2B0qOjIWE1Zb8U1b%2Bl%2F8N5qYrkyAcI%2FDp8IP3rRI82KD9XXnnejjaZK%2BX5klszuUE21nS1bNyfVVimJPX7GqLcEaz%2BWJi0uK1IkPKa6MKS3%2F9IGOqUBe7CFuosG4Td8P4vv%2FzDm9X54J9o8uoHjeeWSqyfesKEz8Q82%2B4IzDj%2BWZWcOrM%2BOgwUkCXYrFPAXtYUib1uy7iqCsV6flzcPaZZ5I0xulsV87E%2BQiqGLCqFo3R4rnJkyiJt0bH%2FMAOVQMhBp7vwiYo1F985FMoF2PjbdZE10pSLz0F5fnQqL1XVHsfqmiOP1Wn1ZpbJIebOqA0qYrEa4BLmMEqcu&X-Amz-Signature=404bcb29945706e566f210f99712e49288f3f02231b539fb584138fd193691ab&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

[image](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/4185ea6a-a314-4e1f-82ea-552293494aca/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WB7FS5DF%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T225129Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIGn7pqlf6JE%2BppH83tto4motGM1ZZQ%2FhrWZ%2BXIBvXcnBAiEAh2%2B%2Fryh0EBtPqcdEROLdGmolj2BzL%2BjNj%2FAXartg6hQqiAQIxv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDP1iHD3ewyxxNOwKGyrcA5bntRcUYAgaI0Cl3igpexCZYhpjFXW8FNzUmGcEIaTOejIJoOAbUEL5nXwdQlAyGwdzsjdvPr%2BhfeQWDsrD8fNsCpSqBcWd6eFF5ztF68Pe5sc00gPtAtj6Z%2BarSnA9cPTILA1Sz5FuAbrZfa4z0Zeap6gHImWHCCS7qnQpReUjc3DFYKm%2Fa51Tgv%2F7eFyueVTY6qAaN6JAkRAxn3omEtI3fkwFZXR3W94H%2BMVTIhoZyOcIzG3PxDk9Q8ThihrjKhAXfLge99%2FMBb0nHFBk9g0l99d6IX3SEUTHjmWy7iDWCsc%2BG7zVQVAByv7pRRpFhA3ACIMqbNZP0%2FC2obXz2S2qSttH%2B7MgloihNT%2BfHp%2F9A38%2Ft8sHx6ZRUSxdph%2FKhK%2Bu9uC3k71S0OrPxrsMga%2BRTQKKvVvFJt0H9IWpGhIkZbh11lHnEY%2By8dVZXbLu%2FKgIbA5wBL0awTJb%2FO4wuzN2l8p3ddckvVMdzEWSaSETn0w%2Bwk1Y3oNaTZVeEmK7yP7wIpplDNJAKs%2FOoIKQev%2B0qOjIWE1Zb8U1b%2Bl%2F8N5qYrkyAcI%2FDp8IP3rRI82KD9XXnnejjaZK%2BX5klszuUE21nS1bNyfVVimJPX7GqLcEaz%2BWJi0uK1IkPKa6MKS3%2F9IGOqUBe7CFuosG4Td8P4vv%2FzDm9X54J9o8uoHjeeWSqyfesKEz8Q82%2B4IzDj%2BWZWcOrM%2BOgwUkCXYrFPAXtYUib1uy7iqCsV6flzcPaZZ5I0xulsV87E%2BQiqGLCqFo3R4rnJkyiJt0bH%2FMAOVQMhBp7vwiYo1F985FMoF2PjbdZE10pSLz0F5fnQqL1XVHsfqmiOP1Wn1ZpbJIebOqA0qYrEa4BLmMEqcu&X-Amz-Signature=216bf272ebd3f6b47f53b8621545b272c7a17793f58cb24b5b71d999d34708f4&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

那么现在我们这个 ES 的一个 header 插件安装好了之后，我们就可以来做一些基本的操作，就可以去开始玩一下在这里的 tab 项其中有一个叫做复合查询。那么这个复合查询的话，这个其实就是我们可以去发起一些相应的 restful 的请求。因为之前我们在介绍的时候其实也说了，因为本身 ES 的话它是提供了一些 Resso 风格的一些接口，可以提供给任何的语言去做一些调用。所以像我们之前请求的这个，我们可以把这个地址直接的拷贝贴到我们这个地方来贴到复合查询往这边粘贴，然后它是一个 get 请求。


随后在这里点击提交请求，在这个地方展现出来的一部分内容和我们在这个网页端请求所得到的一个数据是全部都一模一样的。所以在这个地方你完全可以使用这种方式去做一些 rest for 风格的一些数据的请求都是可以的。那么此外除了这种方式的话，那么我们也可以通过这个 post man 因为 post man 的话它本身也是可以专门去测试，去调用一些接口的。所以我们可以把这样的一个地址直接给贴过来，然后是使用 get 请求去访问，随后我们直接点击 send 好然后相应的一些数据在这个下方全部都会展示这个和我们在网页端所展示的内容是一模一样的。


好，随后我们来看一下，点击一下索引。在这个地方，目前其实可以看到我们有了这样的一个 no 的节点，但是我们并没有相应的一些索引库，所以这个索引我们是可以去创建一下的。我们先点击创建，然后在这边跳出一个弹窗。这个弹窗的话首先一个让我们去创建一个索引的名称。比方说我写上一个 index demo 然后下方会有一个分片数以及是副本数，因为它本身是可以以一个集群的方式去存在的。那么虽然我们是单个节点，我们也是可以这样子去做。然后我们这边的副本我们先不需要改为 0 点击。


OK 好，随后是创建成功，那么创建成功之后，在我们的概览这个部位当前这个节点之下，现在我们可以看到有一个 index demo 这就是我们的一个索引库。然后这个索引库的话我们由于是进行了一个分片，所以它会有01234，总共是有五个下的，只不过它是没有 rapid 它是没有备份的。


所以现在是 OK 然后注意看一下，在这里它会有一个集群的健康值 green five of five 那么这个是什么意思？那么这个是用于去显示它整个集群整个 ES 的一个状态的。它的一个健康如果说发生了一些改动变化的话，它的颜色是会有不同的变化。那么正常健康的情况之下是绿色，另外还会有黄色以及是红色。这个其实我们也可以来看。比方说现在我们可以这样子，我们再来创建一个索引，取一个名字叫 index123 分片数，五个副本数我们为每一个下的都提供一个 rapid 然后点击 OK 好，现在创建成功。


随后我们来到概览。那么这个时候我们来看一下，在我们新创建的这个索引之下，它的下的其实是没有问题，只不过在这里会有一个 N asset 那么这个就是指未分配的一些副本未分配的一些 replica 那么这些就是出了问题。然后来看一下在这个部分集群的健康值。目前是 yellow 也就是黄色，这里有个十二五十五也就是说照理说我们应该要有 15 个节点，5个是我们之前一开始的 index demo 这个索引库，它是没有问题。另外还有 10 个是我们刚刚所分配的其中 5 个厦子是 OK 另外还有是 5 个 replica 那么这五个它是未分配的。所以正确的情况来讲的话，目前我们是只有 10 个可用。但是这十个里面由于我们十个都是一些主分片，那么这些主分片的话全部都是 OK 都是可以去使用的，所以它是会呈现一个黄色 yellow 的一个状态。也就是说只要有至少一个副本，至少有一个 rap 它没有被分配，那么在这里它就会出现一个黄色的情况了。


那么关于这一点的话，其实大家也是可以去看一下官方的文档，那么这是官方文档的地址。然后看一下集群的健康。在这个下方有一个 green yellow redgreen 就是指我们的所有的主分片和副本。其实也就是我们所有的 shared 以及是所有的 rapid 全部都是分配，我们的集群是 100% 是可用的，所以它是一个国运的状态。如果说是 yellow 的话，就是说我们的主分片全部都是 OK 都是分片了，都是被分配了。但是至少还有一个副本是缺失的，有一个至少是没有被分配到的。在这种情况之下，我们的数据是不会丢失，我们还是可以正常的工作的，只不过我们的副本发生了一些问题。所以在这个 yellow 的状态下，其实它就是一种警告。


那么随后还有是一个 ride 那么 ride 就是说我们的一个主分片发生了问题，我们至少有一个主分片是缺失的，或者说是这一台节点宕机的出现了问题，所以我们的数据的完整性，那么这个时候是有问题的。所以在这种情况之下的话，那么我们的运维就要去排查一下问题，要去把这个 ES 恢复到至少是yellow 。


好，那么这就是它的一个集群的健康的状态。那么当然除了从我们当前这个 head 插件里面去看的话，它其实也可以发送一个 API 那么这是它 restful 的一个 API 你是可以去发起请求的，然后再看一下使用的是 get 请求。然后我们发起的一个请求是下划线 cluster 然后再来一个斜杠 house 就是它的一个集群的状态。然后我们直接拷贝一下可以打开这个 post 面。


那么在这个地方你是需要去把他的 IP 外加突然口号去写上的，把这个给贴过来，点击 send 然后你就可以发现这里面的一些信息。就是说这些信息的话其实目前是以这种 GS 的形式反馈出来的。那么如果我们是使用的 head 插件，其实它是帮我们做到了一些可视化的操作。


那么在这里可以看到这边目前的斯特斯是一个yellow ，也就是一个黄色出了一些问题。然后在这个下方看一下。有一个 nascent SARS 总共是有 5 个，然后 active 就是说真实可以用的是 10 个，然后 active primary 吓死，总共是一个 10 个，那么这是数分片，然后这是激活的一个分片数，这是一个未分配的。所以在这种情况之下也就是十二五十五，那么它就是一个 yellow OK ，那么这种情况其实还是可以去使用的。那么这个就是我们的一个集群，就是我们 ES 的一个健康状态的一个查看。好。然后我们再来看一下。就是说如果说我们这个时候我们其实对于这样的一个 index 13，我们可以，不去使用的话我们是可以去删除的。那么如何去删呢？我们可以这样子，这里有一个动作对吧动作，这里面有一个删除，你是可以把这个节点直接去删掉，然后在这里有一个删除啊，看一下，你要输入删除两个字，点击确定，那么它就可以被我们给删除除了。


这种方式啊这个其实是一种所见即所得的一种可视化操作，我们呢也可以通过它的一个 rest for 的一个脚本去做，那么其实也是可以的。那么如何去操作呢？在这里把这个 get 改成 delete 然后这里面的一些玻璃这个 Jason 数据是返回出来的，没有用的。那么我们直接这样子，把这个改成迪丽洁，注意是迪丽洁，然后在这个后方把你所要去删除的这个索引会的名称，我复制一下贴过来。那么这样子直接我再点击一个发送，然后这里有一个 true 那么就代表我们这个是被删掉了。


回到我们的浏览器，我们现在直接可以刷新一下刷新，然后你会发现那么刚刚的这样的一个节点其实就被我们给删掉了，就是我们的一个有问题分片，就是说下子有几个没有分配的删掉了。删掉以后，那么目前我们是只有五个节点，这五个节点它都是一些主动片，所以它的一个集群的健康值目前就是 green five O five 是 OK 没有任何的问题的。那么在我们创建索引的时候，之前其实我们这样子其实也是通过它的一种可视化的一个操作。那么除了这种方式，那么我们也可以通过 restful 的一个接口去调用，那么也是可以的。那么怎么去操作呢？首先在这里把它的一个 method 改成 put 那么随后的话我们在它的后方，在这里你要去给它指定一个 index 下划线，取一个名字叫做倩倩，那么这个就是作为它的一个所有的名称。然后你要去发起一个请求的话，那么它是包含在这个写一下，我们要使用一个 JS 的形式去发送，在这里面是包含一些相应的内容。那么这一块内容我就直接可以拷贝过来来看一下。


那么这里面主要是 setting next 这两个其实就是对应在我们的一个界面上，我们刚刚其实输入的一个是我们的主分片的数量，另外一个就是我们的副本数 shots 和 rapex 那么在这边比方说我一个输入是3，另外一个就是0，我来点击一下 send 好，随后在这个下方看一下 true true 然后 index 那么这个指明的就是 index champ 随后回到我们的页面，我们来刷新一下。这个时候你能够发现我们的 index tap 就已经是成功的创建了。那么这个其实就是我们的一个通过它的一个 rest for 的接口去创建这样的一个动作。其实这两个索引我们都已经是 OK 都已经是有了。


好，那么随后我们再来看一下，就说它除了这个索引的一些删除还有是新增以外，你还能够去做一个简单的查看。那么现在我们查看其实也是在这个界面里面可视化的查看，如果说这个界面没有的话，那么你完全可以通过这个我们也能够来发起一个请求。那么发起请求的话由于去查询使用 get 然后在这边我们可以去看一下它的一个查看的话，其实就是刚刚我们所说的 index camp 就是这个点击线的。然后在这里它会有一些相应的内容可以展示出来。那么这个其实就是它的一个 number O 下子总共是有三个主分片，然后副本是有零个这是它的一个基本信息。然后除了这个以外的话，你还能够去查询所有的。那么在这里你直接去写上一个下划线 cat 再来拼上一个 india kiss 发起请求 send 然后你会发现他会把我们目前这两个索引库全部都给拉出来。


这两个目前都是 green 的状态，你可以在这个后方加上一个问号 Z 点击发送，然后上面会有一些列名，我们，缩小一下它就可以展现的比较全。那么一个是 house 状态，就是它的集群的健康状态是 open 打开的 index 名称，这是它的一个 UID 在这里这个是它的 primary 晒的，也就是主分片，这个是它的副本，5和 3 这边是00，然后 document 在目前其实我们并没有包含任何的文档数据，所以全部都是0。那么这个是它的一个存储所占的一个空间，这主要是看它前面这部分内容。OK ，那么这个就是针对于我们的一个索引库索引的一些基本的一个操作。

