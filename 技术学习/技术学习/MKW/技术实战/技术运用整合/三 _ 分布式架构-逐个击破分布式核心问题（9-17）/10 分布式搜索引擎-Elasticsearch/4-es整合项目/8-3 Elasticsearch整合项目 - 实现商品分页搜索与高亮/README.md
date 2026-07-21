---
title: 8-3 Elasticsearch整合项目 - 实现商品分页搜索与高亮
---

# 8-3 Elasticsearch整合项目 - 实现商品分页搜索与高亮

[image](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/63615216-d41b-4a79-8051-378ec414e366/SCR-20240806-hidr.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XRDPEKY4%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T225214Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDti%2Fm5hWiYlKG58x%2BOIFhnDqxRzKDGbYl8yMEeI9LKIgIhAOAENhAd2t91LfrONJeZ3yJNFl%2BLyGJgNLbBaHSNoaWiKogECMb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1Igy%2BkTOrauhX3Rl7VyMq3AOc12Fsq4UkcyijlFPOwHYj7pXOsRT%2BnTid4gMdlDn8cVJ4Kz4iJyQZ%2FpEm7Ec48TgfP3wuAbXXN%2B9jR1sp81p7Yre%2FPGylp7cA2Emt5oH9fD8%2BpfGj6kV3Iz%2F%2FLtLH1Yrky7TqgHGq1wDEYGDCN31WDdL0OOL6fbdKGygakqTBkVFcmzh%2FrAlfLf%2BmKFnGR%2B7TPBGkugSyo%2B124MtBaNE8NcNMbygCXkg826YlLreL3bZN12k71kcOWtD%2BJfHtfYEAfIvg3uIimwaBVwkszFnmvTxeDZg8SfXcS9R6Px8xQlJQOLd8I%2BxLp1pibjiKrquXKsuChUF1e3agFTZ33icd2wC01xzc4R8FYqeCUh4frHa%2B2xMczV2YqUGnjzkWIkKb5TZJfbRbDJsHyD8G4vnm%2BSe5q%2Fgj4mw9Rhcrft5t6pd5GIU4Pp3hH%2BT2K3Z6IhikUbCSpzJQ5kslPOuw5UzPkhMufEPFkhW0g%2B63rFvqx2m3jViiuiFXeCwpVxusZCshHQ3K3%2FRGKt19W14DcaNQcvd0xKJzNsgq1GEe1AXdtvyFJZ2T5l9pFcUku7bNU1eZVmpv6KvHUWsIO%2BjvUbLfN22bt7rpPErDj1XN6TjFSdGTYgRIf0rghzzODDDFuP%2FSBjqkAcSOBvhhJJcSrUf2g3rwsiCHoRqdTcqeQ8d1%2Fu6WbFrr6nq%2BXG0AKo0V47RaAb%2FlU1RGKtEqOLhefZ%2FvwK6MICrCLMzYTG%2BVzDCq65D0H1JF60%2BksvGlxAi8UZwf2ksn%2FshG%2FeB%2FPbEHBxSPxcpKNfZDhkQ8VI7JYY9DzUDHd39cFC9lnFIllPVlL5%2BZNkcQzqmFHBSuNfqPWYrk0J72X12Hpfog&X-Amz-Signature=bd076b7d388b53a602cd21051a9fa4aa078735e570877990b600e592a398c9f9&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

[image](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/4f88294d-1f72-415f-b407-d62d1a65af7d/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XRDPEKY4%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T225214Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDti%2Fm5hWiYlKG58x%2BOIFhnDqxRzKDGbYl8yMEeI9LKIgIhAOAENhAd2t91LfrONJeZ3yJNFl%2BLyGJgNLbBaHSNoaWiKogECMb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1Igy%2BkTOrauhX3Rl7VyMq3AOc12Fsq4UkcyijlFPOwHYj7pXOsRT%2BnTid4gMdlDn8cVJ4Kz4iJyQZ%2FpEm7Ec48TgfP3wuAbXXN%2B9jR1sp81p7Yre%2FPGylp7cA2Emt5oH9fD8%2BpfGj6kV3Iz%2F%2FLtLH1Yrky7TqgHGq1wDEYGDCN31WDdL0OOL6fbdKGygakqTBkVFcmzh%2FrAlfLf%2BmKFnGR%2B7TPBGkugSyo%2B124MtBaNE8NcNMbygCXkg826YlLreL3bZN12k71kcOWtD%2BJfHtfYEAfIvg3uIimwaBVwkszFnmvTxeDZg8SfXcS9R6Px8xQlJQOLd8I%2BxLp1pibjiKrquXKsuChUF1e3agFTZ33icd2wC01xzc4R8FYqeCUh4frHa%2B2xMczV2YqUGnjzkWIkKb5TZJfbRbDJsHyD8G4vnm%2BSe5q%2Fgj4mw9Rhcrft5t6pd5GIU4Pp3hH%2BT2K3Z6IhikUbCSpzJQ5kslPOuw5UzPkhMufEPFkhW0g%2B63rFvqx2m3jViiuiFXeCwpVxusZCshHQ3K3%2FRGKt19W14DcaNQcvd0xKJzNsgq1GEe1AXdtvyFJZ2T5l9pFcUku7bNU1eZVmpv6KvHUWsIO%2BjvUbLfN22bt7rpPErDj1XN6TjFSdGTYgRIf0rghzzODDDFuP%2FSBjqkAcSOBvhhJJcSrUf2g3rwsiCHoRqdTcqeQ8d1%2Fu6WbFrr6nq%2BXG0AKo0V47RaAb%2FlU1RGKtEqOLhefZ%2FvwK6MICrCLMzYTG%2BVzDCq65D0H1JF60%2BksvGlxAi8UZwf2ksn%2FshG%2FeB%2FPbEHBxSPxcpKNfZDhkQ8VI7JYY9DzUDHd39cFC9lnFIllPVlL5%2BZNkcQzqmFHBSuNfqPWYrk0J72X12Hpfog&X-Amz-Signature=9e76271618cd9489db88ae7bddec5b944814ff3a7d9540150bbdfa40f2fe5257&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

上一节我们是把这个 service 还有咱们这个 ctrl 这个架子我们搭了一下，那么接下来我们就可以把这个 service 去做一个完善了。好，那么我们来看一下，我们之前其实是写了一个 test 那么在这里面的话我们本身其实就已经是实现了咱们的一个高亮以及是分页还有是排序相关的内容。那么我们其实可以直接把这里面的代码拷贝过去，然后再去做一些相应的修改，我们找一下在这里。那么我们直接把这里面的这一堆的代码我们拷贝一下。然后我们再贴过来做一个修改，配到这个位置。好。 OK 然后我们在这里面有一个 template 我们也去拷贝一下。


好，然后我们在这里面再去做一些相应的一个修改。首先一个我们的这是咱们所定义的一个高亮。然后这里是我们的一个分页，分页的话我们直接把配置和配置 size 给引入进来。 OK 那么这样子就行了。然后下面一个这是这个排序，排序我们先不用先注释掉。好。随后下方这边我们是使用这个 native search builder 那么在这里面我们使用的是 much cure 那么在这边我们就应该去把咱们的一个它的内容去做一个修改。在这边其实我们是基于它的一个 item name 去做一个全文检索的。所以在这个地方我们把这个 item name 拷贝过来，我们在这边直接可以去定一下，定一下它的一个field。好，OK那么这样子就行了，直接把这个贴过来贴到这个位置。另外这边 text 是我们所需要去搜索的检索的内容，我们把 keywords 直接放进去就行了。那么再下一个这边是我们的高亮的一个field ，所以直接再把这个贴过来。那么这样子的话我们就不需要在这里面去写死了，万一你写错的话可能就会引发一个 bug 所以我们把这个单独提取出来，在外面定义一个变量，这样子就行了。


好。随后下面两个这边是两个 text 是高亮的。再往下这个是 page EVO 给传进去，最后来一个 build 好，随后我们就要去做一个 query for page 作为一个检索。那么这个检索的过程肯定很明显，由于我们是使用了高亮，所以我们这个它的一个其中的映射，它的一个我们是需要自己去做一层封装的。那么在这边它的这个配置，然后它的这个泛型我们要改掉改成我们是 items 好 OK 就要去修改的，这边也要改这个是索引，根据 items class 去搜，然后再往下这一行，这一行。 OK 没有问题。好在这里是我们的一个 list 也要使用我们items ，随后这里。那么到这里的话是我们去获取这个高亮的一个内容。那么很明显，这边我们也要改。 item name field 好写过来。然后在这里面我们获取一个高亮的数据，高亮的一个文本。那么其实也就是这个 items name 好写一下。好。那么这样子其实我们高亮的这部分内容有了之后，我们就可以去做一些其他内容的一个映射。


首先一个我们的我们是需要去从这里面一个一个去获取。那么我们来，第一个是 item ID 写过来，第二个 item name 有了，随后是 image URL 再往下是 price 再来一个是 salcats 好 OK 总共是四项。那么随后在我们这里面的一个值，我们是需要去做一个相应的修改。对于 item ID 来讲的话，那么在这里我们直接使用 string 就可以了。那么下一个 image U URL 也是一个 string 好，再往下是 price 和塞康斯。那么这两个的话其实都是 int 类型，所以类型稍微去做一个修改，好。


Ok. 那么这样子的话，我们这四个数据我们都可以去获取到了。那么随后在这里的话我们就需要去创建，需要去 new 一个新的 items 去溜一下，定一个名称叫 item 然后在这里面一个去做数据的一个设置 item.set item ID 说下一个 item name 再下一个 set 我们的 image uir 好，再来一个 set price 再来一个 set sales 好。 Ok. 那么这几项内容我们就已经是设计好了。最后我们把这个 item 往它的这个 list 里面一丢就行了。做 list 改个名字，改一个 item highlight list 打开这个。好。那么这样子的话在这个位置我们就已经是这一块的映射，放到 list 里面就已经是 K 了。


那么最后再下一个。那么到这里的话其实它会去做一个判断。那么这个判断我们在这里我们就不需要。因为如果说我们进行搜索的时候，那么这边是一个 null 的话，那么前端前端会获取一个 null 的空数据会不太好？在这边我们直接返回一个空的 list 就可以了。所以我们使用这一行就可以使用这一行，然后 list 去修改一下。


那么这样子的话我们是可以去拿到相应的一些数据的。但是会有一个问题，就是说这边的话我们仅仅只是把这个 list 放了进去，但是和分页相关的一些信息都没有。比方说比如我们这里的它会有一个叫做 payjable 这个我们没有放进去。另外在 response 里面，其实我们可以获得咱们命中的总的数据，其实就是我们分页里面的所有的一些数据其实我们都可以放到这里面去的。那么其实它本身的话也会有相应的一个方法。我们可以看一下 ctrl 加f12，我们目前使用的是第一项对吧，那么它其实还会有，我们往上面看的话，有有一个 page EVO 还有一个浪就这个。那么这个的话我们是需要把一个分页的一个 page over 另外是我们的总部记录数的 total 我们要往这里面一传。那么这样子我们在使用分页的时候，分页信息在我们前端就可以拿到了，因为这个数据是需要去传给前端，前端要去计算它会有一个分页的插件的。好，随后我们在这里面我们去设计一下。那么第一个第一个就是配置 able 传进来。


第二个的话是我们的 response response.get hits 点有一个 total hits 那么这个就是总的命中的一个数量，你是需要去往这边做一个设置的。那么这样子的话对于我们分页来讲的话其实就可以 OK 了。好，那么这个是我们在这里一段的自定义的一个封装的信息。那么现在当我们的一个查询都 OK 结束了以后，那么在这个部位我们还要去做一些相应的一个修改。我们的修改主要是要用于，要去返回一个配置的 grade result 这个是我们自己去封装的对吧。所以我们在这里这样子，我们先把这段内容我们注释掉，其实也不需要，我们把这个 page 的 grade results 我们去把它给 new 出来，随后在这里面去设置一些相应的信息，这些信息的话都是前端所需要去使用的。


首先第一个 set rose 那么这个是我们的 list 那么这个 list 直接从这个配置的我们前面定义的叫什么名字，看一下这个改一下叫做配置的 items 我们拿到这个以后在这个下方去做一个获取，点 get content 就这个。那么这个就是我们所拿到的一个 list 就说每一页所展示的一个数据。好说下一个。
那么下一个的话点 set 我们的一个配置，这个就是我们当前是第几页，我们把这个配置给放进去，只不过在这里我们是需要去加1，因为在 ctrl 里面我们是做了一个减减，然后我们再，下一个的话我们点 set 我们要去设置一下我们的 total 那么这 total 如果说你不知道什么意思，点击进去它会有相应的内容。那么这个就是总的页数，总的记录数。所以在这边使用 page 的 items.get 有一个 total pages 你可以直接去获取再放进去。


那么如果说在这个地方我们没有传 page able 也没有传入这个 response.get hints.total hints 这个两个都没有放进去的话，那么这个 total 它的总列数以及是总记录数，在这边我们是获取不了的。好，然后再下一个点 set 一下我们的 your course ，这是我们总的记录数。通过这个点 get total 有一个 total elements 这个是总的一个记录条数。那么这样子我们设置进去以后，那么我们的数据其实就可以直接 return 给外层，那么这样子的话其实就 OK 了。那么这样子的话就是我们当前这个 service 其实我们就已经是写好了，写好之后我们就可以来做一个相应的测试了。我们回到咱们的 ctrl 了 ctrl 了，在这里我们可以直接去访问 items ES search 然后传入一个 keywords 重新去运行一下。好运行现在是 OK 了。那么我们，打开浏览器，我们在这边我们去输入一下请求 items 斜杠 ES 斜杠 search 我们直接搜好吃的吃货 OK 吧，然后我们回撤一下。


那么可以看到其实我们的数据都已经是有了。那么在这里面来看一下。我们当前是第一页 total 总共会有 4 页，因为我们默认是 20 条数据，总的制度数是 61 条，命中了六十一个。 Rose. 就是我们当前第一页所展示的一些相应的内容，当然你也可以在这里面去加，比方说我可以再加一个配置，配置等于3，然后直接按回车。那么这是我们的第三页，第三页的话总共也是有 20 条数据，如果说我把这个改成 4 的话，那么我们就只有 1 条数据了。那么这样子其实我们全文检索这一块其实就已经是 OK 了。


那么在这边还会有一个高亮的话在这里，这个吃它是被这个 font 所进行的一个包裹，我们返回上一页，返回后退我们来搜一个好吃查一下好吃。当前没有，我们再回到第二页搜一下，也没有第一页，来看一下第一页有没有第一页是有好吃的。那么这个好吃的话它也是会被这个 font 所进行一个包裹。


那么这样子其实我们当前这个全文解锁的一个 control 了，service那么都已经是实现了。然后我们也可以通过咱们的 head 插件去做一个检索，我们来检索一下。当前我们可以去看一下，我们找到 item name 我们也可以来做一个相应的测试去搜一下。 match 我们是好吃的吃货，好吃的吃货搜索总共也是有 61 条数据。那么这样子的话其实我们现在这样子的一个解锁其实就OK。

