---
title: 6-4 Elasticsearch整合SpringBoot - 索引的删除与mappings更新
---

# 6-4 Elasticsearch整合SpringBoot - 索引的删除与mappings更新

[image](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/494df4cf-11c8-4b71-993d-99b9f24c6408/SCR-20240806-gcuz.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46675N5NRWX%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T225159Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCyP4IqtcSz00FqqNrbMgIbeplzmP79DGIqLIr%2BfZyEMgIgfTm5T2LjnZpNKZg0W0fNBc3t5uspAIsNdFUCO3fPsEwqiAQIxv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDBSyRIvV4lOtEKZI4SrcAyzdnDTT%2F89xdBEliGrhnF4CyPiSB7B9NP4%2B6H485hEfw1vixAw9z5%2FLJwRcXbHYE1jHxNngyPh3wixnrYsTPEr8oLHpiZ%2BpDtNsxlH7FnXPpkPD7fzaF4VYQJ2FQTdJtPX2JjgrlzYn2a8Wy2QZX7vDrrmNODLOPLnzIK6Y%2BrdnkYHC7Z%2B3D%2Bc4tEZ8gfLR1hfPNXdWSzhAwAXeHveu6XbNLPVtOJ7BxgYZEI9qFp6k2KsItzPNSB1BJyO1zSkJG%2FWjtFdaxvwjoiynRBK3%2FbZdxo6oAweRU3KaMhgwioWe30MmIJ4Ny%2F5koVwh%2FdR%2BTM0BdRwEJ7%2FNkvKXkZUDlCxY1EVrSWAPQ%2FwCN16yUBALziCkrUoLV2J%2FM1Rubwdd6oOnSrRlIrDkoIdgt086DQ2b2YHrrhu4NyzOP0Ws075lEUp39OInfx1uyZ0UntzJm6IAba662DoSjv9VBMiv%2FcjEcOKPFN16%2BPS1nVaGVgCqy6ETN9w3TwmgWkgcuj2d5BEsilhcfoBIhY2o6IxtVv%2F9kvRypqKWi3ckePrGJQtUGltQsuI0TG2olEum1TXuxkA2UUzomF9pN5YW%2F6UyeyWspNX7xKZAOD08IQvcyZPi3ANNsHMwnw5sxgZxMIC4%2F9IGOqUBCTEXgcZZ%2FvC3m9BgnI815YZ1daa%2BQY77dHfJyLa%2BTQbr2Lqsa%2B2cLEWO8zpYCkEgR0y%2Bh3czvCUonWoj66IyBLjR%2FLj%2BDus67LExVa8bOMohvdI7B53JN9XN6dymYYLt32y20UNbALVZJb0Rvp%2BRQ6zgOwOog94ftHMzYMjAyeFA6vKeq6a9PJ0O%2FQ2Wok9QEnqeAEnfnXwMMx%2BvWax%2B2T0ohNlV&X-Amz-Signature=b753148f39735c63b0690849538febf2d12807f5e01221f85a09e7f1fad8a2b0&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

[image](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/9daf6122-4ffb-4751-b4d8-08f12ff8baba/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46675N5NRWX%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T225159Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCyP4IqtcSz00FqqNrbMgIbeplzmP79DGIqLIr%2BfZyEMgIgfTm5T2LjnZpNKZg0W0fNBc3t5uspAIsNdFUCO3fPsEwqiAQIxv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDBSyRIvV4lOtEKZI4SrcAyzdnDTT%2F89xdBEliGrhnF4CyPiSB7B9NP4%2B6H485hEfw1vixAw9z5%2FLJwRcXbHYE1jHxNngyPh3wixnrYsTPEr8oLHpiZ%2BpDtNsxlH7FnXPpkPD7fzaF4VYQJ2FQTdJtPX2JjgrlzYn2a8Wy2QZX7vDrrmNODLOPLnzIK6Y%2BrdnkYHC7Z%2B3D%2Bc4tEZ8gfLR1hfPNXdWSzhAwAXeHveu6XbNLPVtOJ7BxgYZEI9qFp6k2KsItzPNSB1BJyO1zSkJG%2FWjtFdaxvwjoiynRBK3%2FbZdxo6oAweRU3KaMhgwioWe30MmIJ4Ny%2F5koVwh%2FdR%2BTM0BdRwEJ7%2FNkvKXkZUDlCxY1EVrSWAPQ%2FwCN16yUBALziCkrUoLV2J%2FM1Rubwdd6oOnSrRlIrDkoIdgt086DQ2b2YHrrhu4NyzOP0Ws075lEUp39OInfx1uyZ0UntzJm6IAba662DoSjv9VBMiv%2FcjEcOKPFN16%2BPS1nVaGVgCqy6ETN9w3TwmgWkgcuj2d5BEsilhcfoBIhY2o6IxtVv%2F9kvRypqKWi3ckePrGJQtUGltQsuI0TG2olEum1TXuxkA2UUzomF9pN5YW%2F6UyeyWspNX7xKZAOD08IQvcyZPi3ANNsHMwnw5sxgZxMIC4%2F9IGOqUBCTEXgcZZ%2FvC3m9BgnI815YZ1daa%2BQY77dHfJyLa%2BTQbr2Lqsa%2B2cLEWO8zpYCkEgR0y%2Bh3czvCUonWoj66IyBLjR%2FLj%2BDus67LExVa8bOMohvdI7B53JN9XN6dymYYLt32y20UNbALVZJb0Rvp%2BRQ6zgOwOog94ftHMzYMjAyeFA6vKeq6a9PJ0O%2FQ2Wok9QEnqeAEnfnXwMMx%2BvWax%2B2T0ohNlV&X-Amz-Signature=699c8b68e54474684fb38a720bb5f4f1620f35b5c9584630c6649a13bba9c4e1&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

上一节我们是把这个索引做了一个创建，另外同时它也可以帮我们把这个数据做一个插入文档数据。那么如果说这个索引它已经是存在了，那么当我们再一次的去进行一个数据的插入的话，那么它就仅仅只是数据的一个新增，它就不会有索引的一个创建了。好，那么这个是我们上一节的内容，有了这样的一个创建以外，那么我们能不能去做一个更新呢？就是说其实在我们的这个映射里面，我们是可以去看一下，在我们这个映射里面是包含了相应的一个内容，来看一下它有 students ID 、name以及是相应的一个 age 那么这些内容其实它是帮我们做了一个自动的 mapping 映射。


那么其实我们也是可以去做一个修改。那么在这边我们所说的一个修改并不是修改它现有的一个映射，而是做一个新增。就是说我们还可以去做一些额外的字段的一个新增也是可以的。比方说我们来看一下，我们回到开发工具在我们的 student 里面。那么现在我们可以这样子，我们可以去新增几个。比方说我们来一个stream 。在这里我们来一个叫做 description ，dgs C 再来一个我们这个叫son ， son 签名这边有一个 description 我们拼音全一些。然后在这里，你也要去指明它的一个 field 都是 true 好，随后有了这些以后，我们，再来一个money ，金额。


好。 Ok. 然后针对于这些设置我们的一个 sign 在这边我们来一个 type 我们可以去为它做一个设置，使用这个 field type 那注意一下，这个是在我们的 spring frame work yes 下边的有一个可以看到吧，这里面有很多的一些类型，在这边我们为它设置为 Q 或者这仅仅只是一个 Q 或者。好，随后我们其他的其他的我们就保持不断。随后我们在这边生成一下 get 和 set 好。然后我们回到咱们的这个 ES test 来尝试做一个其他的操作。 student set 点，我们来 set 一个 money 比方说我们来一个 18.8 好，再来一个点 set set 一个 sign 这边比方说 in spider man 好。 OK 然后我们再来一个 set description 这边，我们也用这个。 I wish ima spider man X 掉就这样子好OK 。那么这样子的话我们可以来再一次做一个更新，来做一个创建，看一下我们这个更新能不能更新进去。


好OK ，现在已经是运行成功了，成功之后我们，来看一下我们的数据。可以看到在这里我们新插入了一条数据，这条数据里面其实就包含了我们刚刚所新设置的一些内容，像 money sign description 全部都有。


然后我们再来看一下咱们的一个概览，在信息里面来看一下我们的一个 sign description 以及还有是一个 money money 的话在这个上方可以看到吧，它全部都有，只不过你会发现它的一个 sign 我们在设置的时候其实是设置为了 Q word 但是他在这里的话他没有帮我们设置为 Q word 那么这是他自己的一个问题，这个我们暂时先不管。好。 OK 那么这样子的话其实我们就可以做到一个相应的设置，我们是扩展了新增了我们的一个 mapping 然后数据也是可以做了一个插入。那么随后我们可以在这样子我们可以再来做一个操作，这个时候我们来做一个删除的操作。那么删除的话其实也可以，在这里我们直接把这些内容全部都删掉，删的话我们来去删一个索引，就说我们来 delete delete next student 那么要去删索引的话，那么在这里通过 ES template 它有一个 delete 来看一下，不是这个在下方有一个 delete index 这个就是删除我们的一个索引，你只需要把这个 student 放进去就可以了。


student.class 那么它会自己去识别到。在这里面有一个 index name 以及是 tab 会根据这个去做一个删除的。好，然后我们来做一个运行。
好OK ，运行成功。然后我们来到我们的这个 ES 里面，回到海德刷新一下。那么你会发现我们这个索引就会被删掉了。那么这个其实就是基于我们这个索引的一些操作，一个是创建更新它的一个映射，另外是删除它的一个索引。那么在这里我们要提一点就是说其实我们的一个规范的话，我们是不介意去通过这种 Java 的客户端或者说是 spring boot 他所提供的这个 ES tablet 去做一个相应的索引管理写一下不建议使用这个东西对索引进行管理。那么这里的一个索引管理指的是新增创建索引，更新绿色以及是删除索引，这个我们是不建议去这么做的。


那么这个其实为什么要这样子说，主要就是因为其实我们的索引其实它就类似于是数据库或者说是数据表，我们平时是不可能也不会去通过我们的一个代码去频繁的去修改创建我们的数据库和表，我们只会针对于数据库中表里面的一些数据去做相应的一个操作。那么其实在 ES 里面的话其实也是同样的一个道理，写一下。那么所以就像是数据库或者数据库中的表，我们平时是不会去通过 Java 代码频繁的去创建修改删除数据库或者表达，我们只会针对数据做 cru D 的操作。


那么在我们的 E S 中也是同样，在 E S 中也是同理我们尽量使用这个 ES template 对文档数据做 cru D 的操作，那么这一点我们是需要去注意的。那么这是我们最主要的功能，其实也就是使用它来针对于我们的一个文档数据做一个全文解锁。那么其次在我们使用这个 template 针对于我们索引的一个创建或者说是更新一个映射的时候，其实它显得有一些不太灵活，就像我们刚刚所看到的。那么在我们这里其实我们的一个，年龄当我们在这里设置的是一个 int 类型的时候，其实它在我们的一个 ES 中，它其实是一个浪。另外对于我们的这个 sign 其实我们在这里指明是一个 Q 的但是它是帮我们设置了一个 text 也就是说其实它的一个 field 属性，它会不是特别的一个灵活，这边已经删掉了，看不了了就说显得不会特别灵活。


另外还有一点它其实也是不灵活的一个地方，就是说它在这个 document 这里面，它默认设置为是下子和 rapid 分别是五合一。对吧？这个我们之前上一节是讲过了，但是如果说你想要对它去做一个更改的话，它其实也会有问题。比方说现在我的一个下子我就只想设置为三个，然后副本数我不想要设置，那么它是不会帮我们去生成的它还是五合一。


那么这可能是它内部的一个小 bug 所以他这个东西其实并不是特别的灵活，在这里我们是需要去注意一下的，我们来演示一下。在这里演示一下，一个是 shots 我们设置为3，另外一个是 replicas 我们设置为0。随后我们来做一个运行，来看一下。我们创建 wrong 跑一下，好运行成功。然后我们到 head 刷新一下。那么你会发现它其实没有我们期待的一个效果。照理说我们现在就只有三个主分片副本是没有的，但是它其实是不支持，就是说它可能是它内部的一个小 bug 所以我们一般就不会使用这个 ES template 针对于我们所有的一个创建。在这里我们补一下就说我们的一个属性属性类型需要这菜谱不灵活。第二个，主分片与副本分片数无法设置，那么这个你也要去注意的好，所以我们会尽量的使用这个 template 针对于我们的一个文档数据做一些相应的操作。那么这个我们会在下面几节课来做一个讲解。

