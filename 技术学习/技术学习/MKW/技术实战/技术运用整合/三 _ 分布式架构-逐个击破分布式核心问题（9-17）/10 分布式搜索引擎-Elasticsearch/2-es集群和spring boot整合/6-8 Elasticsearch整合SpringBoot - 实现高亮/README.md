---
title: 6-8 Elasticsearch整合SpringBoot - 实现高亮
---

# 6-8 Elasticsearch整合SpringBoot - 实现高亮

[image](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/3fe10c6c-e560-477f-ab56-899b96d790de/SCR-20240806-glez.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466Y4MRFTQP%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T225203Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDA2MY%2BxlYPaTLE6VDL5GevIf6ifauxwLQWck39TY9qUwIgXaiRNzs0AuBa%2FnUh3Ud%2FScjNMdfJ1ZpWAWcOMObV3pYqiAQIxv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDBuXHqWeIJOsZkzvfircAzPPaEzy%2FOXEAeEF9lhvYAB8qQssQ2SKi%2B0vApJBwBWdHjbp3Twm9jnCysu6DOUORDBra%2BtR8E49fIVddtIeGToFY1E5IaweqO79BP2L1C%2Fd8ErB9KTY5e%2FNPLxzXT0f5m53JmRxQ5J0bX%2Ft9spFtu%2BaaaJhyw0ilvqOM%2BqPv77%2F2LCXxbtzVFzpZG52tv4r4pXpbjUq6ECbzW1SoRAIxGJ%2FCzsYXYZpFEkCOgbvBFhVqlEvo2JUPiZ0kuvhhHgvki2tP4Uq1Bm%2BlluvcBUmXLM0j2PPRAVOJYVx98lDGFRwtZzCC25%2FnWJXCZzJq0X8U5pn3eIpHZud5dznLDngNuutqt7gzFwCrqRsYqt0jLX8BIRdbG2DYuu%2FlKOAcf9haagyL1yBaVExOIiq38edwG7G1K06hiGMwHD6Aw0YPsB68cih0KX8BLA%2BtE4smOq3bLEJWllxjusw1Kwh%2BPe1BIhrpLQ1zxled7d7VGDy0bflu3QmDQEIMLqMyY0vLzZwyDe6F6vYagcpfRH%2Bv0vYwJTWXKIjqasqJKELGXqqGBP85k%2FADeOcsGVd%2F4hz6cZ2hJd3p3SsmdrYWwSSiRxcxyBOLBeuYlSunxppSyj94Uo50iEpn6%2Bfaxo1WUWVMOO3%2F9IGOqUBjMi1J0w7dzzWFvFusujcuUiqNXj%2BmUd595eLGQJJCh0vOmm%2Frv8%2B5Eir70g5ntD5iaU6ZGovvczsA8a8C4VCe0mwwGQ35iqcSNckZv4SlAZ1eTaAKIg0ISD0Rp8NAenpx6Xh5aZM3BMd7iUKfjotyeKGnRhqA0N6GU88XvHiHy9aTRKuCsZ%2BSDN8LSnjI8I2PqZmAxA57DS6HzZRpyWbg%2B%2BbCynh&X-Amz-Signature=acedf506300c5d7b5589e34633a43ae47de2e7c475769fac7a890690a43a3fad&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

[image](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/144ddc9a-44fc-4e0f-b1e2-736b86f73b18/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466Y4MRFTQP%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T225203Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDA2MY%2BxlYPaTLE6VDL5GevIf6ifauxwLQWck39TY9qUwIgXaiRNzs0AuBa%2FnUh3Ud%2FScjNMdfJ1ZpWAWcOMObV3pYqiAQIxv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDBuXHqWeIJOsZkzvfircAzPPaEzy%2FOXEAeEF9lhvYAB8qQssQ2SKi%2B0vApJBwBWdHjbp3Twm9jnCysu6DOUORDBra%2BtR8E49fIVddtIeGToFY1E5IaweqO79BP2L1C%2Fd8ErB9KTY5e%2FNPLxzXT0f5m53JmRxQ5J0bX%2Ft9spFtu%2BaaaJhyw0ilvqOM%2BqPv77%2F2LCXxbtzVFzpZG52tv4r4pXpbjUq6ECbzW1SoRAIxGJ%2FCzsYXYZpFEkCOgbvBFhVqlEvo2JUPiZ0kuvhhHgvki2tP4Uq1Bm%2BlluvcBUmXLM0j2PPRAVOJYVx98lDGFRwtZzCC25%2FnWJXCZzJq0X8U5pn3eIpHZud5dznLDngNuutqt7gzFwCrqRsYqt0jLX8BIRdbG2DYuu%2FlKOAcf9haagyL1yBaVExOIiq38edwG7G1K06hiGMwHD6Aw0YPsB68cih0KX8BLA%2BtE4smOq3bLEJWllxjusw1Kwh%2BPe1BIhrpLQ1zxled7d7VGDy0bflu3QmDQEIMLqMyY0vLzZwyDe6F6vYagcpfRH%2Bv0vYwJTWXKIjqasqJKELGXqqGBP85k%2FADeOcsGVd%2F4hz6cZ2hJd3p3SsmdrYWwSSiRxcxyBOLBeuYlSunxppSyj94Uo50iEpn6%2Bfaxo1WUWVMOO3%2F9IGOqUBjMi1J0w7dzzWFvFusujcuUiqNXj%2BmUd595eLGQJJCh0vOmm%2Frv8%2B5Eir70g5ntD5iaU6ZGovvczsA8a8C4VCe0mwwGQ35iqcSNckZv4SlAZ1eTaAKIg0ISD0Rp8NAenpx6Xh5aZM3BMd7iUKfjotyeKGnRhqA0N6GU88XvHiHy9aTRKuCsZ%2BSDN8LSnjI8I2PqZmAxA57DS6HzZRpyWbg%2B%2BbCynh&X-Amz-Signature=9fc2233d0112360791651059213940e823f759616a3af1bcdbc3cbab81bacb88&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

那么上一节我们是写了一个 much query 也就是一个全文检索。那么这节我们来看一下这个高亮如何去实现。我们把这个直接拷贝一份，拷贝一份之后我们修改一下，改一下 highlight 好OK ，我们就使用这个去进行咱们的一个解锁。然后那么解锁的话在这里我们来看一下，在这个无意思 Q 的后方，我们可以去额外的再去加一下，有一个叫做 with highlight 那么这个其实就是可以让我们去构建一个高亮显示的。


OK 使用这个 highlight fuse 那么在这里面我们就要去使用咱们的一个构建构造器了。那么构建器的话其实也就是这个 builders 我们点进去看一下，它里面有一个 highlight builder 。OK ，我们使用这个就可以了，这是一个 highlight build.field 拷贝一下，然后直接贴到这个部位，我们直接可以把它给 new 一下给 new 出来。那么 new 出来以后，那么 field 里面你是需要去加上一个相应的高亮的一个属性表。那么这个属性对应的是什么呢？我们现在查询是description ，所以直接把这个丢进来就可以了。那么这样子就可以针对这个 discrepting 去做一个高亮的显示。那么然后在这个后方你还可以去为它增加一些额外的参数。比方说点它有一个叫做它有一个前缀和后缀的一个 tags 我们是可以去自定义的。所以我们可以使用这个 protects 在这里我们是可以去做一个定义。那么定义的话我们在上方，我们在这个上面去定义一下，定一下一个叫做普 tag 干预。


这个其实就是咱们的一个前端代码了，写一下使用phone ，使用 phone 然后来一个颜色卡拉等于 red 好，然后我们再来一个结尾的结尾的，在这里面来看一下，结尾的话叫做点有一个 post tax 好，然后我们在这边我们再去写一下，就是 post 直接把这个 font 结尾就可以了。


那么这样子我们只需要把这个传过来，然后当我们进行解锁的时候，查询出来高亮的内容，那么就会以这样的一个 tag 进行一个给我们做一个展示。Ok 。好OK ，那么这样子的话我们这样的一个高亮其实就已经是设置好了。那么设置好了以后，那么现在我们可以去做一个解锁，去做一个查询，我们一起来看一下能不能够显示出来要见预计一下。


Ok 。那么在这里来看一下解锁，因为我们目前是带有分页，我们恢复成 10 条，因为我们是带有分页的，所以我们这边是显示了两条数据，然后在这里面显示的数据我们来看一下 description 那么这个 description 里面其实它还是一个普通的字符串，他们并没有把高亮的内容给我们进行一个展示。那么这个主要是因为我们在进行一个检索的时候，如果说我们是使用的 postman 那么高亮的部分其实并不是展示在我们的 source 里面。那么这个其实相当于是我们的一个 source 数据。所以对于我们的一个高亮的部分的话，那么我们在这里面是拿不到的，我们应该要通过另外一种方式去获取，也就是一个自定义映射的一种方式。那么如何去使用呢？那么我们可以在这里面去我们在设置 query for 配置的时候额外去增加一个参数去做一个映射就可以了。那么这个时候我们在这个里面点，我们可以这样子进去看一下。这里面其实还会有一个参数，我们 ctrl 加 f12 在这里面看一下。其中有一个叫做在这里 query for page 然后有一个 search result map 那么这个就是我们搜索结果之后的一个映射，我们是可以去修改它的一个映射的。OK ，点一下进去。那么重新再来一次，点一下在这个部位也就是这个东西 search results map 我们可以传入这样的一个参数来写一下，我们把它拷贝出来贴到这个部位。好，OK那么这就是我们的一个 map 那么这个 map 在这边我们是可以这样子，我们直


接可以，我们可以在这个参数可以去直接给 6 出来也可以吧，你这样子 new 一下，把这个参数可以 new 一下。好， new 一下了以后，那么你会发现他帮我们生成了一个方法，那么这个方法是需要我们去实现的。那么这个其实就是我们的一个 map results 它是一个映射的结果集，我们是可以去做一些相应的设置的。那么其中在这里面我们主要要去使用的就是一个叫做 response 这个就是我们的一个响应。在这里面我们可以去写一下，在这里有一个 response 对吧，我们可以这样子给大家看一下，我们打一个断点，然后我们在这边去做一个运行，我们 run S 跑一下。我们使用 debug 使用 debug 去跑。好OK ， debug 已经是进来了。然后我们在这边可以看一下有一个 response 吧，


 response 点一下，我们可以拉起来。那么在这里面的话其实会包含一些相应的一个内容的。那么我们的一个主要的内容其实都是通过我们这这个 response 去获取的。那么在这里我们可以做一个展开，把这个 response 给展开一下。展开之后在这边有一个 hit piece 就是命中我们查询的一些数据，双记一下。那么你会发现在这里面它其实总共是包含了 hit 它是一个 search hit 14 条，这是一个数组，包含了四个数据。在这里的话有一个 total hits ，就是总共检索出来命中的一个数据。那么现在就是符合我们的一个内容，就是 4 条数据，然后双击一下。那么你会发现就是数组里面每一项内容全部都会有，这是第零个数组，这是第一个数组，那么都是可以去看的。那么其中的话就会包含一些相应的内容，我们可以往后边转到往后面转，然后你会发现它会有一个 highlight 那么这个 


highlight 其实就是我们所要去高亮的一部分的内容。那么这部分内容和我们前面的这个 list 是不一样的吧，因为这个前面的一个 list 它其实就是我们的一个sauceok ，这是我们查询出来的一个结果集。那么对于我们来讲的一个 highlight 其实是包含在另外的一个部分，在这里有一个 highlight fields 这才是我们的一个高亮的内容。那么这个就是我们的一个 description 然后我们可以往里面去看。那么在这里面你可以发现在这个 save 的一个左右两边，那么其实就是加上了一个 phone 字，那么这个是我们自己去加的。 OK 吧，那么当然我们也可以去看别的记录，我们找下面的第三条，其实也就是第四条数据往下面去看找到 height 找到这个 highlight fields 也是 description 在这里面的话找到看一下。那么在这边， I wish I am a spider man 在这个 man 的左右两边加上了一个 phone 标记。那么这样子其实就是我们的一个高亮，然后我们在这里面是可以去注意一下，它是包含在了我们的 fragments 里面。然后这个 fragments 它其实是一个数组，对吧，我们再去获取的时候，我们通


过这个数组那第零个就可以获取它里面真实的一个内容。这真实的内容其实就是我们所要去展示到页面里面的一个数据，也就是高浪的一部分的内容。Ok 。好OK ，随后我们这个断点就直接过去。那么接下来我们就可以去做自己的一个映射。我们自己的一个映射主要就是把我们高昂的部分全部都拿出来，然后去做一个替换，替换我们原有的一部分的内容就可以了。那么如何去做呢？我们先去写一下，我们先把这个 response 先拿到 response 里面，其实是咱们的一个点 get kids ，就是我们的一个命中的 get hits 那么这拿到以后它其实是一个 search hits 这个我们之前也是打断点的时候是看到的，它是一个 hits 那么 hits 里面每一个命中它其实本身就是一个集合，我们针对它去做一个循环，在这里写一下每一个它单独的是一个 search hit 我们命名为H 。 H 然后 hits 好 OK for 循环 for 循环的时候去进行相应的一个获取。那么在这里面，首先第一个我们通过 h.get highlight fields 那么这个我们是可以通过这个去拿到我们高亮的一部分的一个内容的。只不过我们在这个后方我们要去指明一下他拿到的一个内容的名称是什么，也就是我们的一个 field 点有一个 get 我们的 field 名称，是这个 description 直接拷贝贴过来。那么贴过来以后，随后我们在这个下方。那么这个拿到了以后是我们的 string 写一下，这是一个 highlight fields field 拷贝，把它给拷贝出来，这是一个 H 这样子。
Highlight field ok 。
好，拿到了以后，那么我们通过它再去拿到叉里面的一部分的数据，它里面之前有一个叫


做 fragment 这个是我们打到点看到的。那么拿到以后它的数组中的第零个。那么第零个就是我们的一个真实的一部分的内容点 to string 那么这样子我们就可以去获取整个底斯 Q 品的一个高亮的字符串数据了。定一下，这是一个 string description。好，那么这样子当我们拿到了这个数据以后，那么其实这个就是我们的一个高亮的数据。好随后我们就要去定义一下我们要去返回出去的内容了。那么返回出去的内容其实也就是这个 return 这里面的这个 now 我们要去做一个修改。



那么在这里面我们由于是一个循环，我们在这个外面我们去定一下，定一个 list 那么它也是一个 stu 好叫做 stu list 然后写一下，这个是 highlight 好，有了这个以后，那么在循环去做一个处理的时候，那么我们其实是可以一个一个去添加点艾特去添加我们的 student 然后咱们的这个 student 我们在这里面要去把它给 new 一下，你有一个 stustu 我们定一下 stu 等于，这边我们也是加一个，加一个 highlight HL 等于 new student 随后点 set 那么这样子我们就可以去设置我们的 discussion 了吧。设置一下，然后把这个 description 给设置进去就可以了，然后最终把这个 student 添加到我们这个 highlight 里面去，那么这样子其实就可以了。



那么最后的话我们在这边就要去做一个返回，返回的话我们来可以做一个判断。如果说因为我们在查询数据的时候，它有可能是会为一个空的。所以我们在这里我们是需要去针对于这样的一个 list 去做一个判断。我们去判断一下它的 size 是否是大于0。如果说是大于 0 的话，那么我们就可以 return 把这个是可以去 return 出去。但是我们在这里是需要去注意这个东西我们是不能够直接 return 出去的。


我们在之前通过这个 ES template 去做查询的时候，它其实是这个这样的一个 aggregate 的配置。就这个东西。那么这个的话我们在这边也是要以类似的一个形式要以相同形式给返还出去。那么在这里的话我们就需要去 new 一下，把这个给 new 出来拷贝一下 aggregate 的配置，它有一个实现。那么这个实现的话在这里面你是需要去放入一个相应的 concern 展。那么这个其实就是一个list 。 OK 吧，也就是一个 list 这个 T 我们在这边写一下，你直接把这个放进去是不行的，你是需要去做一个转换的 list T 这样子把它括号给括出来。OK ，那么这样子的话我们的一个数据它才能够被返回到外面。那么这样子的话我们整体的信息在这个 page 的 student 里面就可以通过点 get container 就可以获得。我们在这里面所拿到的所包装过后的一个高亮的 list 了。


好，然后我们再来做一个丰富，就是说我们在这边仅仅只是把这个 discussion 给放进去，但是我们其他的数据其实都是没有的。所以当我们进行一个检索的时候，如果说我们仅仅只是这样的一种方式的话，它只能够显示这个 description 里面的高亮数据， student 里面的数据是拿不到的。所以我们在这里还是需要去做一个额外的操作。那么这个额外的操作就是要把它其他的数据给拿出来。比方说我们来点 set 它有一个组件 ID 对吧，这个你得去设置。这个设置的话我们写在这个上方，它是一个 int stui D 等于如何去拿，我们也是通过这个 search hit 我们的一个每一项所命中的一个数据，通过这个 H 也就是 hit 去获取。


点 get 它其中有一个叫做 source as map 那么这个 source 其实就是我们的一个文档数据，就是source 。然后可以 S map 因为它本身就是一个舰子队，它是一个 GS 的形式，它可以把它转换成一个 map 所以我们可以通过这种方式去进行一个获取。那么获取以后那么它就是一个map 。随后我们点 get 通过它的 key 去获取它的一个值，那么 K 的话是 student ID 贴过来。那么这样子就OK ，在这里边我们通过这个去获取的时候，它是一个V ，所以我们在这里还要去做一个转换，这个 student 我们转换一下，这个应该是个浪，所以写一下。那么这样子我们这个 ID 就已经是有了。


好，随后我们再来。下一个的话点 set 下一个的话，我们来拿一个name ，把这个 name 给拿出来。那么其实也是同样的一个道理，在这里我们直接去获取咱们的一个 name 那么 name 是一个字符串，所以我们在这个地方写一下 string 这里是一个 nameok 拿到之后直接做一个 set 好，随后我们再来下一个，下一个我们可以来一个 H 年龄，那么年龄的话我们在这里也是选一下这边点 get age 那么 age 年龄的话我们定义的是一个病情，所以我们使用这个 H 好。


OK 随后我们再来下一个。那么下一个我们可以去获取一个 sign 这是一个签名，那么签名的话和我们的这个和 name 其实是一样，它也是一个字符串。所以我们把这个拷贝过来写一下 sign 好。 OK 然后在这里把这个给复制 copy 过来。好，随后下最后一个。那么最后一个是我们的 money 金额，它是一个 float 在这里写一下这是一个 money OK 。


那么这样子的话我们所有的数据全部都已经是设置好了，设置好以后全部都放到了我们的 student 然后每一次循环它都会添加到我们的这个 student highlight 里面。那么这个目的主要是用于去做一个映射，其实就是这两行代码要把我们高亮的部分给拿出来，然后再返回出去就行了。


那么这样子的话我们在这个最后在最后的话在这里我们又一次针对了这个配置的 sto 去做一个拿到的分页数的展示，以及是它的一个循环。随后我们就可以来做一个测试了。好，然后我们选中一下跑一下直接 run 好。 OK 那么在这里报了一个错，来看一下。这里有一个转换错误，有一个 int 和 long 那么这个是我们的ID ，对吧，来看一下。在这个部位我们在这里他报了一个错，转换是有问题。那么这样子我们直接把这个改掉改成 object 那么改成这个以后我们再来做一个修改，在这里直接使用这个 long.value [of.to](http://of.to/) street 那么这样子去做一个相应的转换。好。然后我们再来再次预警一下。
好，OK然后我们再来看一下，又报了一个错，这个时候我们错误是换了吧，这边这里是一个 double 和这个 floats 对吧。那么这样子我们也这样子把这个改成 object 随后我们再来做一个转换使用这个 float.value [of.to](http://of.to/) street OK 。


最后我们再来试一下，看一下能不能成功。OK ，那么这个时候我们是成功的运行了。然后这是 student 所打印出来的一个数据，总共是四条。然后我们往后面，看一下我们的高亮。那么在这边我们 Disco 评的部分，那么一个是 save 这个是 save 的，它是可以帮我们做了一个高亮的处理。然后是这个面这个面的话也一样，帮我们做了一个高亮的处理。那么这样子的话我那我们其实就是实现了一个高亮，也就是 highlight 什么这个 with highlight fields 那么就可以达到我们高亮的一个效果了 OK 吧。

