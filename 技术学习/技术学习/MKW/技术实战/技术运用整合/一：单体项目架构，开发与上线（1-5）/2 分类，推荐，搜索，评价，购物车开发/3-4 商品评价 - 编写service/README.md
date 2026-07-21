---
title: 3-4 商品评价 - 编写service
---

# 3-4 商品评价 - 编写service

[image](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/42fd5ebe-eadc-4f0c-ac5c-97ca7df53f2c/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664452TS2W%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T224645Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCpfy1E6NLbu0hHhZXGvE1q0vrprY%2B%2FDSEgQRWrjDXqngIgL5XT%2BGYrho0txHdtNJe87vyjIzs2iMiS5WfYDySfz%2B8qiAQIxv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDDHAFqyjC3%2BWG0YQDircA43y%2B2VkMObt6tAp3nS9VtIdLRFkX3e79u1YD%2F5U3gwu9af0B3WMlttrzftz7q1nrsFCc%2FhaIkjpgZTa5dPAebsDs6MDRYA7eW5B9YK%2FX33r7DiRuN7CixqmszJ9CYkffpJ%2BFlyYZChIpJyzvfO2FjTyU29M%2BzWA8QTwrMJM1jlsu0gj2Z7muvife5QmoTaG9otootvI67OdMBY7QzZoTng3qIYAwV70aMlTYnKC2Oc0XP6LPEv6McE6XGyeRBEoOcJb7ukLFS6FOJzvlu7vyf15GrLRtXcs%2B3FbKD3UYz6oILmBLVEQjTgmMDNsJIxiHPJU%2Fh%2BH7g%2FI1CU5F45pkLvw6nl6yfOvM7bXSMR6pWkXd26DqSwqFVYxzBvazp6F5NUDIMdESiHslmxAD5YUqgN1vQRdhJqRl9Dyv63JVKBtl%2FB7GFFgtNeZYj7RZL0Tv%2BSlw16sKXUVzCnPOB9xmkfyaSwjtT55%2FUheNi4t6X4jJCvn1v%2Bp4UaLfYw2XCVscPg1cszIKUySq7tB36Bc72IqDkdSC6qXsttRS5DYK5tg5dpZ8E6qZRtmO6Myohtgq4FL5I8lPpkxO1L7GvYQ0QhdccZIuqVTC2W9GUSic5J69gr1EKINw6KPDwYwMIu6%2F9IGOqUBbyn6ZkdC9Cm4EBC3B0aYWhBYYjmzQ6nVYyf%2Fuu6LkVuC8YIUtJoGoAGkwBQcibHco6H6kcFdkc6KKg7y%2FlL69GFZiylaYJG4WQ0y32FhYpnGAvYxtCL%2F0QmRL67zMgAVhUCumYwDy%2FKliPc%2BpE8dnjCAdl4Gay0MIJIIzT7LY2NMs08ZjnY7wnMkp7wWKlqGNL%2FRiFPbuG09fpVANzv1vJ0QR%2Ftn&X-Amz-Signature=9e4e7a712b9371ca24dd325dc652ece5742721998ebab6aad04ba84e9b36d603&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

上节课我们是写了 SQL 语句，是可以去执行的，但是在我们的 map 里面，这一段代码我们还是需要去进行一个完善。比方我们的一个传进来的参数是一个Mapper，假设我们传进来的 Mapper 里面会有一个 item ID，在这里我们就需要写一个占位符了。写一下。我们可以通过 pump snap，我们就沿用我们之前一直使用的叫做 pump snap。也可以定义的时候，只要通过这样的一个 map 点 item ID，就可以拿到它对应里面具体的一个值了。


好，这是我们传进来第一个参数，传进来的第二个参数，我们就应该要去根据它的一个 level 去进行一个查询。传进来的 level 由于它可能会为空的，所以当且仅当这样的一个 level 它不为空的时候，我们才会去加上这样的一个 and 条件。所以在这里我们会使用 PUMS map 点。比方我们传进来的 k 值就叫做level。我们要判断它不为空，首先不为null，并且会使用 and 写一下，并且 pump map 点 level 也要不为空。字符串，这样子写就可以了。OK，好。这是我们的一个判断，如果符合它的条件，在这里我们就可以在它的后方把 level 给加进来。这样子我们把把占位写好参数放进去。


OK，好。现在其实我们在这里面写的，在 map 里面写的 circle 其实就已经是写好了，只不过我们的 result type 还没有去定义 result type 其实按照我们现有的一个情况来讲，它其实也是一个自定义的Polo，它是作为显示层的对象去展示的。所以我们又要去写一个 feel 了。OK，在这里我们来写一下。我们可以取一个名字叫做 item comment v，o。好，在这里面我们就要去写一下了。首先一个我们还是一样，在它的类的上方我们去加上一个注释，我们之前把之前的也是一样的把关掉写上，这是用于展示商品评价的。


d o 在这里相应的属性，也就是在我们的 map 里面。这些内容我们都要写过来，分别都去写一下。首先第一个，第一个是 comment level，它是一个 Int 类型。随后下一个是content，它是一个字符串。再下一个是规格名称。再来一个是创建的时间，应该说是留言的时间，它是一个 date 类型的好。最后两个是和用户相关的，一个是face，一个是nickname，它们都是 string 类型的。这些没用的删掉。最后生成一下 get 和set。好。OK。创建完了以后，我们就可以去使用了。直接把它贴到在这个位置，直接可以贴进来。我们在它的前方也是需要加上一个类的，需要加上一个包名的。在刚刚创建的 copy reference 好。OK。在这里好了以后，当前这样的一个 select 方法，我们是需要在它的 name space，也就是命名空间里面要去定义一下。在这里面还是一样写一个public，它是一个list，在这里面是一个方法，叫这个方法。另外它的返回的 list 类型是item， comment 比 o 好。传进来的参数参数。


其实我们跟之前一样，使用一个 map 就可以了。 key 是string，值是object，定义为map。它需要有一个注解，这个注解我们会使用 pump 取个名字，就叫做 Palms NAP，也就是我们在这里面所使用到的。写过来，这样子就会被我们的 map 里面所拿到了。好，现在我们自定义的 map 现在是写好了。写好了以后，我们就需要去到咱们的 service 里面去写，一层一层往上去写。打开咱们的service。现在还没有方法，我们先可以来定一个方法的名称，我们可以取个名字public，我们是要返回一个list，这个 list 就是item， comment view 这个类型的写过来好。请求的查询名称。


query page 的 comments 为什么要加 page 的代表是分页的意思，其实我们是需要在这里分页的。OK，所以我在这里取这样的一个名字。写错了，是抽象，并不是实现。在这里面我们就需要去加上相应的传参。第一个商品的 ID 肯定是需要的，另外商品的一个评价等级我们也要传label，直接写进来。好，OK，这两个参数是我们必须要去传的。当然我们的一个方法的注释千万不要忘记，我们还是要为了规范要去写一下，这是根据商品ID，查询商品的评价，加个括号，带有分页的。


好，回到我们的service，先把这个方法去生成一下。由于它是查询的，所以我们事物隔离 suppose 先把它给贴过来。好，在这里面我们就要去编写相应的一个代码了。首先我们在发起查询的时候，我们是使用了一个map，所以我们把 map 我们先给它写上去。好，写完以后相应的参数我们也应该要放进去。第一个是 map 点，我们要 put 一个key，这个 key 叫做 item ID。 item ID 看一下和我们在自定义里面所使用的 item ID 必须要保持一致。随后下一个是一个 level 老，先贴过来。好，这是两个 put key，有了之后，我们还需要把它的值也给放进来。好，第一个是 item ID，第二个是一个 level OK。现在参数 map 我们就已经是 OK 了。 OK 好了以后，接下来我们就要去做一个查询了。查询我们使用自定义 map item comments。 Mapper 是现有的，我们应该要把 map 给注进来吧。就这个我们到当前类的顶部，在这里写一下，是需要去注意一下的。好，OK，住进来以后，在这个方法里面可以直接通过 map 点 query item comments，把 map 给传进去，就可以做一个查询了。查询出来，他会获得到一个 list item comment view 这样的一个类型，定义为一个list。拿到了以后，这个 list 我们就直接可以 return 出去。


OK，这个其实我们是用于去做查询商品评价，并且数据是可以肯定可以拿到的。但是它会有一个问题，就是分页。关于分页，我们会在下一节我们来跟大家讲一下如何来使用 my Betis 的一个 page helper 这样的一个插件，整合到我们的 service 里面来，再去实现分页。OK。

