---
title: 3-7 订单管理 - 确认收货与删除订单
---

# 3-7 订单管理 - 确认收货与删除订单

[image](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/0b9db863-4314-4296-a637-891b670bc460/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TA4WAQGM%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T224736Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDod1NEwYrDVQm2Y92JIHDZ71qhr1UXdoKuVq%2BHd7Q%2FJAIhALlSU8uzxG9HaOQsQqLWhPKNLklJIQ25yYAhthK%2FHzFYKogECMb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgxcAaRv%2BX%2FquuzMx%2FEq3ANkS3ZONsQA%2F45mWxUha5PrlYgH81WoCjTzJKCWQtpJ2%2FjGj1HszxRKV0EGhmOsounHDIDJHnnbvti%2BZekcJh5eql1s7zQsEsFyidYduDp7sztj3YDcqXxf7dxfLwo9Dk2qefRW9hhPvL93w2lLrj1fsWiOCyvuAijTEp4%2FHdjIcJuuE%2Fk%2BjCvgeGe0kTh8Z7z2FFM3MgMpcmZwhUMkk6niiA20XA5MLlIUVkOplnuGiX5ONKK%2BGiKxg1r%2FTD96ziql2f1PQLtZdSkwPo5zqauVcyHG3FGkzmJg%2Fho3VZhtEEVLH8o8l5akJvFlWYJbLYm1EYnFmd4bb9tsBqml54i7Ld4EmNJogyGRN9L88UUbxDL3CJFJgDMttsdWRMEC7Pms3RbmsPsk3NemCjTI8cmPkaOCKf2YkXDrjSIpmN1TTDeiD8tjYL0kFIlNxFiXudI4vZwmvVuTtSf1DiWAsYsNrhpkVehluQpl%2BrCfWA4s61HdVbtBybtiI4stzuWQS2GAszz5lNKockcN%2F%2FeANUWZlmedKierLwQOsge3aKQ0d4wHvtjnfVGOOcIbqY33UxD08siOxKQsWj6KYIskHM09uCqE43AFv7HAGuEXH3myPukRBRHQVVJhoF%2BU%2FTDzuv%2FSBjqkAbJdijipqc7y9yWqWEZCDBz8%2ByOG7neygINagnmVuIWqyeVJohMRU9Wx52juGYMgq6pumBnb%2B6%2BdXkK1Wff92yOkdKPUkrv0wAaTb8neOPpttJHh%2BpiOOhUGkNyBtZ5988mqV6XpJSpVqRJIFH48HrqYJPH%2BSYZefqroOH0HrhSGmhk7CU8Y8VVERWgf3nBofdtmWbDb0TAFPY40Ec3ISZZzjfoE&X-Amz-Signature=ca9bd2d4ba9505662669630ba9a44ee8dc6b8ddd5507ce35c62d36e58d7a19fa&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

确认收货和删除订单的第一个验证的步骤，在这里写完之后，我们就可以去编写一下咱们的 service 了。在这里面我们可以去写一下 public boys。写一个不好值，因为我们的一个确认收货以及是删除订单，我们都会有一个更新的操作，所以是否更新成功，我们以一个布尔值的形式返回一下。


updateReceiveOrderStatus，传入的是一个的订单号，这里 string 类型的写一下，这是更新订单状态。确认收货。好，我们再来写一个删除。删除，我们是从订单里面去做一个删除，所以我们是在这里需要去加上一个用户的 ID 的。更新。它其实是更新订单状态表里面它是没有关联用户ID，所以在这里只要传一个 order ID，这样子就 OK 了。这是删除订单，一定要注意这是一个逻辑，删除是使用的   isDelete，改一下叫做 delete order。好。随后我们到 service 把这两个方法去实现一下。不要忘记还是一样的，我们的事物一定要去加上，并且我们的事物在这里都应该使用required。好。OK。在我们再把相应的内容去完善一下。首先确认订单是更改订单的状态，所以我们在这里你有一个  


orderStatus，我们把它作为我们的条件去做一个更新。 update order 声明一下。好。在订单里面我们要塞入相应的值， set 一个  orderStatus。在这里我们是需要去放入一个订单的成功状态。确认收货就代表我们的订单是交易成功了对吧？写一下order，它的一个枚举点success，这是交易成功点type，这是他所设置的。随后我们还是需要再设置一个额外的有一个状态，这个状态的时间是一个 success time，交易成功的时间。在这里我们直接把它 new 一下就行了。好，这是我们所要去更新的一两个值。


最后在这里我们使用 example 来做一个条件，把它给弄出来，再把定义为  orderStatus 这个类型的example。随后再通过 example 去把它的条件去创建一下。great，创建一个 could you app，在这里它是一个。我们要去把声明一下拿出来。条件。好。条件。在这里我们要去设置一下它的订单 ID and equal to 第一个属性，在订单状态里面有一个 order ID，你是需要拿过来的。参数，把订单号拿过来。好，这是第一个条件。随后第二个条件我们应该去设置一下它的订单状态。对于订单状态来讲，我们现在只有是处于一个 30 状态，也就是一个待收货状态，它才能够让用户去点击成为一个交易成功。所以状态我们也应该要去作为一个条件给它去加一下，去限制一下。


好在这边是要再设计一下它的属性，  orderStatus 加进来。好，这样子这两个条件就已经是 OK 了，下面我们就可以去做一个执行了。通过  orderStatus Mapper 点update。在这里我们使用 example selective 传入的参数第一个是对象，第二个是example。好，OK，这样子他就可以到数据库里面做一个执行。我们会拿到一个更新的记录集，我们定义为results。在这边如果是更新成功，拿到的 result 应该就是1。所以我们在这边再做一个返回的时候，应该要根据 result 去做一个判断了，判断一下这个值是不是1，如果是1，我们返回一个true，否则我们就返回一个force，这样子就OK。好，这是更新我们的一个订单状态，是确认收货，随后下一个是删除订单。和我们的一个更新。


上面的步骤其实也是类似的，在这里我们也去写一下。首先我们先要去把我们的订单 new 一下， orders 写一下 updates order new 出来，把我们要去更新的值去写上。第一个是 set   isDelete，因为我们要去做删除了，所以我们使用的是逻辑删除，设置为 yes 点type。好，这是第一个要去更新的。随后第二个我们要去设置一下它的订单更新的时间，在这里你用一下就行了。好，你用完了以后，这是我们的一个订单所要去更新的值使用。下一个我们也是使用example。把这一段内容我们拷贝过来以后，在这里我们把它改为orders，不用动条件。第一个条件首先应该是订单ID，注意这个属性，要改掉这个属性，在这里就应该写上一个ID，把 ID 写过来，而不是 order ID。如果是 order ID 肯定的是更新不了的。

最后第二个，在订单表里面其实还会有一个 userId，用户的编号来看一下。 userId 在这里把属性的值你也需要拿过来作为一个条件，这样子就可以去以一个关联的形式去把对应的订单给删掉。在这里我们也是一样。在更新完毕以后是需要去做一个判断。先来通过 o 的map。

updateByExampleSelected.


把订单放进去， example 放进去。好。随后我们就可以拿到一个result。这个步骤和我们上一步骤是一样的，在这里 return 也是一样。好。OK。这样子删除订单内容， service 就已经是写好了。好。随后我们到上面的两个 controller 了，去把相应的代码去完善一下。首先是确认收货，写一下。先拿到一个不好值，这是一个result，等于 myOrderService 点 update receive。把订单 ID 传进去获得的一个result。之后在这里我们是需要去做一个判断的，如果它是一个force，就代表它没有更新成功。在这里我们就直接 return 一个m。

Results again error message.


提示订单确认收货失败。好，OK。下一个是删除，写一下，这里应该是 deleteOrder 传入的第一个参数是订单的订单ID，第二个是 userId，看一下顺序对不对。第一个是 userId 写反了，这两个要注意顺序，因为他们这两个都是编号，都是字符串。好，这样子是做的一个删除，如果删除有问题，在这里写一下。写订单删除失败。好，OK。这样子我们两个肯出了。两个 service 都已经是写好了。随后我们就可以到前端页面去进行一个测试了。首先还是一样是需要去进行 install 的，因为我们修改了service。好，再来一个重启。


好，重启成功。回到咱们的页面，我们先刷新一下。我们先到待收货，把这条订单去确认收货一下，在这里订单编号，我们先拷贝，点击确认收货。在这里确认收货吗？我们点击确定好，你会发现这条订单没有了，我们到这里有一个已完成，点击一下来搜一下，你会发现这一条订单编号所对应的这条订单现在的交易状态已经是发生了变化，现在已经是交易成功了。OK，没有问题。好说，下一个，下一个我们是要去找一下交易失败的，要去删除的。在这里有一个这条订单，这条订单我们是直接可以删除的，点击删除。我们先在这里拷贝一下订单编号，来注意一下。在这里目前我们总共是有 27 条记录。在这里，我们把这一条订单去删除一下，点击删除。确定好，现在是删掉了。删掉以后我们在当前页面是没有这条订单了，搜不到。再来看一下咱们的记录，这里很明显减少了一条，因为我们的   isDelete 是做了一个更新。好OK。这样子，对于用户的一个删除订单，以及是确认收货这两个节点的操作，我们就已经是 OK 了。

