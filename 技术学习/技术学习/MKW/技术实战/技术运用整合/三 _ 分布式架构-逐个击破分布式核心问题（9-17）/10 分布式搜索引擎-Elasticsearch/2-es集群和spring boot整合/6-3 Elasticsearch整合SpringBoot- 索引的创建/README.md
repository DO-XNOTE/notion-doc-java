---
title: 6-3 Elasticsearch整合SpringBoot- 索引的创建
---

# 6-3 Elasticsearch整合SpringBoot- 索引的创建

[image](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/a90b41ad-a434-4ea2-b789-3bdfab56d28c/SCR-20240806-gamv.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466R5EQZP7A%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T225158Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQD%2FiH37BU0NVsKitQx03Wspvmy%2F3YJ6KPhhpeSnzZa3pQIgVqbRxViCdlWUmgqYlDqHi0AeDJVTRj9RwC%2Fhs6tw9ZwqiAQIxv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDIz3kwt6m9j5StsA%2BircA0lmD73qeY19UYPQl7T5OuX4%2B7EBxgCCpa9oaPCHOvKeOzC1ZHptOZHCIkUgZCI9nZMvOTCafmUAuvTF6HamCWwlGEIV%2FE52KWwKgr76XvSbxYWQb55sQepT2gAGdSaJnjZY7FdB0iiL%2B82YlrYU%2FrQxuc2t0XgoZFDoNwTTyBsPRyf4zPT4QmNhdS0FzsOn5tvwUqrA5NX0zhi5TVjq6MLAeKm3gYWXqHyFdVUMsgaHQh7laNvpxA0EVF3SciAADuKaQHT22BL7GjtkAh0ew%2F0FO6RnPQ0YzCDPG77ZJFpZpKbZ7ZQX6uT4nVFFdLxmOCAP2lPwK8oh2NqmBbBA30BPWc%2Fa3AifgIgJ%2BcGj2OHc2moEkmwFVmz18ZJqXcLiyNP2QdpH2QdW2HZYKkrfSdHuJ8zjDCbaKxhYiPUBpOVkQZRKbEBUcS02OXq%2FJesTCOKSF2LOyFlbGcL1DrGofaBbIS6yzr%2BS2wWbucMseS482I03cGVU%2FxNM3ISA71tPT8XtlNtbM46g%2FKTxk9RiZkQWGNUTTfqgeBXRQl1nmxn608u0Aj1w9LJJ1x3SNna3MS9f3WCuRFrqRDkwPvw1N0qdYY6xfDQtD21XPzWAM4ssYq%2FuXan%2BCCILQqW3MP23%2F9IGOqUBr01d5lNWaqgkjxda9urbP5dG57Id4S1d1PJOy9KYOE46RekRitEBfs7B83gWTRZ7%2BlZG872n%2FUz8yQ94BKWK7S67XokgpeUXEFk7cBmFEf3nsziGIR1f42lc%2F%2B9iZxe7kN6mOiipPF0oGrmhhFCDLzTn5A0ml%2FfPEVPJs6kSezFbq8rHEEeOdBl7zywVWY%2FDSXVCqHKH2VNp3%2BHkW0EJz7d6ueZ6&X-Amz-Signature=97f588fea737823043d96cb2cb0b9c455a27d37b2170a9967c4d87d1662b222c&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

[image](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/e7d7c06a-b20f-4737-a7d0-c2d3d7d868a6/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466R5EQZP7A%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T225158Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQD%2FiH37BU0NVsKitQx03Wspvmy%2F3YJ6KPhhpeSnzZa3pQIgVqbRxViCdlWUmgqYlDqHi0AeDJVTRj9RwC%2Fhs6tw9ZwqiAQIxv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDIz3kwt6m9j5StsA%2BircA0lmD73qeY19UYPQl7T5OuX4%2B7EBxgCCpa9oaPCHOvKeOzC1ZHptOZHCIkUgZCI9nZMvOTCafmUAuvTF6HamCWwlGEIV%2FE52KWwKgr76XvSbxYWQb55sQepT2gAGdSaJnjZY7FdB0iiL%2B82YlrYU%2FrQxuc2t0XgoZFDoNwTTyBsPRyf4zPT4QmNhdS0FzsOn5tvwUqrA5NX0zhi5TVjq6MLAeKm3gYWXqHyFdVUMsgaHQh7laNvpxA0EVF3SciAADuKaQHT22BL7GjtkAh0ew%2F0FO6RnPQ0YzCDPG77ZJFpZpKbZ7ZQX6uT4nVFFdLxmOCAP2lPwK8oh2NqmBbBA30BPWc%2Fa3AifgIgJ%2BcGj2OHc2moEkmwFVmz18ZJqXcLiyNP2QdpH2QdW2HZYKkrfSdHuJ8zjDCbaKxhYiPUBpOVkQZRKbEBUcS02OXq%2FJesTCOKSF2LOyFlbGcL1DrGofaBbIS6yzr%2BS2wWbucMseS482I03cGVU%2FxNM3ISA71tPT8XtlNtbM46g%2FKTxk9RiZkQWGNUTTfqgeBXRQl1nmxn608u0Aj1w9LJJ1x3SNna3MS9f3WCuRFrqRDkwPvw1N0qdYY6xfDQtD21XPzWAM4ssYq%2FuXan%2BCCILQqW3MP23%2F9IGOqUBr01d5lNWaqgkjxda9urbP5dG57Id4S1d1PJOy9KYOE46RekRitEBfs7B83gWTRZ7%2BlZG872n%2FUz8yQ94BKWK7S67XokgpeUXEFk7cBmFEf3nsziGIR1f42lc%2F%2B9iZxe7kN6mOiipPF0oGrmhhFCDLzTn5A0ml%2FfPEVPJs6kSezFbq8rHEEeOdBl7zywVWY%2FDSXVCqHKH2VNp3%2BHkW0EJz7d6ueZ6&X-Amz-Signature=6665f69335852161ac13d7b8eb69ad9928a40245a4cdec09902a8310424c444c&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

当我们把这个整个 ES 的一个环境配置好了以后，接下来我们就可以去针对于咱们的一个 ES 库去做一些相应的操作。那么比方说我们现在可以去创建一个索引，索引的话我们来看一下，目前我们在这个 header 里面是没有任何的索引的，然后我们可以去创建一个索引。那么创建索引的话，在我们这里的话这样子我们写一个 J unit test 来做一个相应的操作。我们 new 一个 class 这边写一下 ES test 创建一下。好，然后在这里面我们加一个包，这里面没有包创建一个 package come.test 把这个移进去。

[image](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/607e3a53-efa9-4413-8d47-7c7734b73be7/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466R5EQZP7A%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T225158Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQD%2FiH37BU0NVsKitQx03Wspvmy%2F3YJ6KPhhpeSnzZa3pQIgVqbRxViCdlWUmgqYlDqHi0AeDJVTRj9RwC%2Fhs6tw9ZwqiAQIxv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDIz3kwt6m9j5StsA%2BircA0lmD73qeY19UYPQl7T5OuX4%2B7EBxgCCpa9oaPCHOvKeOzC1ZHptOZHCIkUgZCI9nZMvOTCafmUAuvTF6HamCWwlGEIV%2FE52KWwKgr76XvSbxYWQb55sQepT2gAGdSaJnjZY7FdB0iiL%2B82YlrYU%2FrQxuc2t0XgoZFDoNwTTyBsPRyf4zPT4QmNhdS0FzsOn5tvwUqrA5NX0zhi5TVjq6MLAeKm3gYWXqHyFdVUMsgaHQh7laNvpxA0EVF3SciAADuKaQHT22BL7GjtkAh0ew%2F0FO6RnPQ0YzCDPG77ZJFpZpKbZ7ZQX6uT4nVFFdLxmOCAP2lPwK8oh2NqmBbBA30BPWc%2Fa3AifgIgJ%2BcGj2OHc2moEkmwFVmz18ZJqXcLiyNP2QdpH2QdW2HZYKkrfSdHuJ8zjDCbaKxhYiPUBpOVkQZRKbEBUcS02OXq%2FJesTCOKSF2LOyFlbGcL1DrGofaBbIS6yzr%2BS2wWbucMseS482I03cGVU%2FxNM3ISA71tPT8XtlNtbM46g%2FKTxk9RiZkQWGNUTTfqgeBXRQl1nmxn608u0Aj1w9LJJ1x3SNna3MS9f3WCuRFrqRDkwPvw1N0qdYY6xfDQtD21XPzWAM4ssYq%2FuXan%2BCCILQqW3MP23%2F9IGOqUBr01d5lNWaqgkjxda9urbP5dG57Id4S1d1PJOy9KYOE46RekRitEBfs7B83gWTRZ7%2BlZG872n%2FUz8yQ94BKWK7S67XokgpeUXEFk7cBmFEf3nsziGIR1f42lc%2F%2B9iZxe7kN6mOiipPF0oGrmhhFCDLzTn5A0ml%2FfPEVPJs6kSezFbq8rHEEeOdBl7zywVWY%2FDSXVCqHKH2VNp3%2BHkW0EJz7d6ueZ6&X-Amz-Signature=1c8498d71f688939b4cdf1bb9c8bb0c9a0bef3a7aeab12180b3850c0ae238ec4&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

好。随后我们在这里首先我们要去加上一个相应的内容，那么这个内容的话其实主要是为了便于我们去跑对吧。所以我们在这边加上一个 run with 在这里要指明我们的 spring 有一个 runner.class 随后再来一个我们是 spring boot test 那么我们的一个指明一下咱们的一个启动类，启动类使用这个 application 这边应该有一个叫做 class application yet plus。Ok 。那么然后我们就可以去使用这个 spring data 里面的一个 ES 了。那么这个其实是由 spring boost 来帮我们实现的。


我们先写一个 private 然后有一个叫做 elastic search template 它是一个模板类。那么其实我们在使用这个 Redis 的时候其实也是类似，那么 Redis 它有一个 Redis template 那么其实道理都是一样的。


写一下，这边我改成ES 。 ES template 这个 elasticsearch 英文单词还是比较长的。然后 out where 的好。 Ok. 那么这样子我们就可以去基于这个 ES template 去做一些相应的操作了。那么在这里我们可以去写一个 test 方法 public void 那么现在我们是针对于咱们的一个索引，我们要去创建索引。这样子 create index 我们来个stu 。


Student. 这边标上一个 test 那么对于这个 studentstu 索引，我们要去创建的。创建的话其实它相当于是有一个映射，就是说 ES 的话其实本身相当于是数据库对吧，那么它里面的一些数据它是一个的 Jason 那么 Jason 对应到实体的一个对象，它是一个 pojo 也是一个 entity 所以我们在这个里面去创建一个包，创建一个 ES PO 9 先创建一下 es.po 9，然后在这边我们再去创建一个 class 取名字 student 好，随后这个 stu 就是相当于是我们在这个 ES 中的一个文档。然后我们在这边我们就可以去指明了。比方说现在我们要去创建它的像映射关系，以及是它的一个 index 索引的名称，还有是它的一个菜粉等等。其实我们都可以在这个里面去做好相应的一个映射的。那么我们在这里写一下，写上一个 document 那么这个其实就是代表是我们的一个文档数据。随后在这里面你可以去指明一下它有一个 index name 那么这个就是我们索引的名称，我们取名叫做 stu 随后它还会有一个 type 在这里要去注意一下，如果说你是 ES 7 的话，那么这个 type 你可以不去写。但是我们现在是在这个 ES 6，所以你这个 type 要去指明一下，我们统一的使用这个下划线 Doc 那么这个就是我们索引的一个创建，就是这样子。随后在我们的这个索引库里面，也就是对应的我们文档数据，它会有很多的一些属性。 field 我们在这里面也可以去写一下。


首先我们先来定一个ID ， ID 我们使用浪这边是 stu ID students ID 随后在这里我们可以为他去加上一个 ID 这边使用这个是在 spring boot spring data 里面的一个 ID 那么这个你如果说写了之后，那么假设我们现在 student 这个 ID 设置为 1001 那么他会同步的为我们去创建一个就是说和我们对等的相等的一个文档的 ID 如果说这个东西你不设置的话，他会帮我们去做相应的操作，一会我们可以去演示一下的。


好这是我们第一个属性，随后我们再来一个来一个 private 来一个名称。学生的姓名在这里我们指明一下它是一个 field 一定要注意就是说当我们在使用的时候，在这里有一个 field 它是在 elasticsearch 下面的，然后这个已经是过时了，一定要注意需要的。然后在这个里面其实它也会有一些相应的内容，在这里边看一下。其实这些内容其实我觉得大家都应该熟悉，如果不熟悉的话回去看一下，或者说你百度一下都能够知道里面相应的一个意义。


比方说我们在这边我们来写一个这个 store 存储，它默认是 true 它默认是 false 我们的使用处我们当然如果说你要使用这个index ，它有一个是否要索引，也就是倒排索引，那么它默认是true ，可以把它设置为 force 也可以，我们在这里使用默认的 true 就可以了。


好，这是我们的一个 name 最后我们再来一个年龄，private拉一个 H 这边 field 加一下 store 存储处设置一下。 OK 吧，这是我们的一个年龄。好。那么这样子的话我们就设置这几个最基本的一些字段，随后我们再来一个 get set 去生成一下。好 OK 生成一下。那么当然如果说你不使用这种方式，你使用其他的一个注解，他会帮我们去生成 get set 其实也是可以的。


好。Ok 。那么这个就是我们最简单的一个 document 文档，这个是和我们 ES 中的一个文档，数据是对应的，那么它就是一个对象。好，随后我们就回到 test 里面去做一个创建，那么我们要去创建一个相应的索引的话，那么应该如何去做呢？其实我们可以这样子，使用 ES template 写一下点它里面会有一个叫做 index 来看一下有一个这个东西，那么这个就是代表我们去创建一个索引，那么创建索引的时候同时会帮我们把相应的数据给进行一个插入。那么这个就是 index 的一个部门，当然它还会有差的，像 index exist 判断这个索引是否存在删除，还有这个是bot ，这是批量的意思。


另外还有是使用这个单独去创建我们的一个索引，其实也是可以的。那么在这里我们使用这个 index 我们可以进去看一下。这里面它其实我们要传入一个参数叫做 index query 。那么这个的话传进来以后，其实它里面包含了我们的一个 stu 它的一个对象，它是可以帮我们去创建的。如果说我们叫索引，没有它是可以帮我们去创建。另外对于我们 saro 的一个文档数据，有数据的话它也会帮我们去做一个相应的新增。所以我们在这里可以去写一下，它是通过一个 new index query 有一个 build.result 写一下 with 不是 result with object 这个就是我们的一个对象。那么这个对象就是我们的 stu 你把这个 stu 给写进来。那么目前 stu 还没有，我们先把这个注释，然后 stu 写一下 new 一个 student 那么这样子可以把这个 object 给放进去。然后点有一个方法叫做 build 去构建我们这样的一个索引。那么它其实是返回一个叫做 index query IQ 这样子定义一下。好，随后再把这个给丢进去，那么这样子的话就可以做相应的一个操作了。


那么现在我们这个对象是空的，我们塞入一些数据，比方说我们的 ID 来一个1001，它是一个浪。好，随后我们再来一个 stu.set 设置一个 name 比方说来一个 bat man 再来一个 stu.set 一个 H 年龄来一个 18 岁。那么这个是我们的一些基本的数据。随后我们就可以跑一下 wrong 现在我们是一个这个 J unit test ，考试成功的。那么这个时候我们打开这个浏览器，我们到这里面我们刷新一下。你会发现我们这个 student 他已经是帮我们给创建了。因为我们是一个节点，只有一个节点不是集群，所以它的一个副本是没有的。然后它的一个总共的分片是有五个。那么对于我们的数据，来看一下数据浏览来这里， student ID 有了1001，然后我们的 name batman age 是18，数据可以帮我们新增到咱们的这个 ES 里面去的。那么对于我们的一个分片来讲的话，它其实也是有一个默认值的。这个我们在这里面是我们进入到 student document 来看一下，它会有一个 shots 和 rabix 这就是我们的主分片，这个就是我们的一个副本分片。


OK ，总共是有五个分片，每个分片是对应有一个。好。 OK 那么这样子的话，我们现在就已经是通过这个 spring boot data ES 来把我们的一个索引以及是相应的数据做了一个构建。那么另外这个 ID 你是可以去不写的，你不写的话其实也可以。假设我们现在没有写的时候，我们在这边改成1002，然后我们数据做一个修改这边是 22 岁，随便来一个 spider man 好OK ，再来运行一下。随后我们可以去观察一下我们文档的一个ID 。好OK ，运行成功。到这里面，数据刷新一下。那么刷新以后你会发现咱们这个数据我们放大一下这个1001。


之前我们在使用艾特 ID 这个注解的时候，由于我们是设置的，所以当我们的这个 student 就是说我们的这个文档具体数据中的一个 ID 有了以后，那么我们文档它自己本身在 ES 库中的一个组件 ID 会保持同步会一致的。那么如果说你没有设置，那么它的一个 ID 它会帮我们去做一个生成，那么这一点是需要去注意的。那么在我们一般的一个设置过程中，我们其实往往可以把它设置为同步，就是说我们的这个 ID 我们这样子就可以了。

