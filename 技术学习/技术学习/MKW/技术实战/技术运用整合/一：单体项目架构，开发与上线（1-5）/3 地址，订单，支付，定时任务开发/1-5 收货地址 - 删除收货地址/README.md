---
title: 1-5 收货地址 - 删除收货地址
---

# 1-5 收货地址 - 删除收货地址

[image](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/cd022adf-0c64-41ae-a53e-ef61511e584d/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466W4SIC767%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T224659Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIEAg1IjHe48JGCd4eayHYRIB0rc6FuT2e6yGGNQTx3J9AiAqUdR7q1H%2Br7DrAsR7X1qI9%2Fb221DLPF2y6sGPVVFfMCqIBAjG%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMpvNUFFrrzCON123TKtwDVPexn3iprr%2FpszOsrjQSWXViEIfmAezET24wo5KeaupWrHMLPmi%2BaAbJtDO6jbyD5lsgMBXUwoYW5h2SS7fo1y9sqDSSntklgMy5vYz7Eaq52IOx2lft5hP01FqcZcQztPmK5JcgbUawiDVwNV%2BalkwJQLQIpext6gj02P%2B6O4LLHnNaI9a%2BJsRAG44Lxp%2FbtrRFjQpciap%2FrtUf6GBvWTVAvJmz1cb6rK3Jjrvl1J%2BdyiecAJGvTf2nsM4HyiWiS6Beyig8CFdzjKQ8m96jrEbLjIazcy3s%2FibhNz%2B6JnwpEdbKjej05BkYo62lZ43Q7cc2ZLkezcQTiGh669G5uZcNjN8JOEvdwgkOPM8AyxE9osyDR%2BKFGs%2B9E%2B6BFTgD%2BP6N6j6hxExl0%2BfjCr%2BkzPYmnYSYi4r3DCg5GSCEqNIqArQvvQ4ndReo1pcbbB8iNF%2FHl938bHcwOIM7CU2bodi8QcNDf3W2D8qCV6%2FGpsrTS9qQBFc9wPjsCfnY1m3pViHQU8qW3rYz%2BteBMk1RfxXy2XFmcWNjOFnR69sy%2BebXJI9htMsM2qmH8wPNzsqH%2FiZXa4rg4QZP5q%2FDzOunpv22Tj27qihwAb3JWGAxkUpyWt%2Ffe%2BG%2Fkua%2Below%2FLf%2F0gY6pgG82g2JAzIAVXbSm%2FHm7hAugNsJ0VPKNsuA3t7n00YKxqlENIy63gc4Yu5azB4V0zRCraXuJqP5J8QWbe%2BnYtcIEgjVTmDwLeYN5CPWDzq6yOlexQCRkh3VllQnENj0PIc0BHAbKKL%2FxhQItSPcvlwFrhRhv%2Bwe6gvvU7x6UqycBsdYAGcj456TbPpX%2BbQyNXaHkQx8BL%2BkbjkoiuDUvSTmmqABW6zC&X-Amz-Signature=262e639396bd496b5712f1554f1b2dfbd1cafc280eb9e23521f9f136477e2a7b&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

用户的收货地址功能我们已经是做了查询、新增和修改，接下来我们来做一个删除。删除从前端到后端肯定是要有 user ID 的传递，并且是要删除哪一个对应的地址，它的地址 ID 也要传递过去。所以我们可以先来看一下前端。在前端找到一个方法，叫做 delete address，在这里面会传入一个 address ID 的，我们可以搜一下。在页面里面可以看到有一个link，这个地址 ID 是每一行你点击删除的时候，它其实都会有对应的一个 ID 的，因为这个是通过循环 for 循环里面输出的。所以我们可以把地址 ID 作为一个参数，传递到我们的 g s 里面去进行一个调用。


好回到我们的 g s，首先在这边要去进行一个判断是否要确认删除，确认就可以直接去删了。下方这里有两个判断。这个判断是用来如果我们是要去删除的地址，它本身就是一个默认的地址，或是一个选中的地址。 choose address ID 和 default address ID 这两个值要设置为默认的空，要，不然在页面里面所展示的一个选中效果会出现一个紊乱。所以这两个在前端所做的一个效果要去设定一下的，当然和我们后端没有什么关系。好，随后我们就可以发起一个请求了。通过 address delete 就可以去调用传入的两个参数，一个是用户ID，一个是 address ID 就可以了。删除成功以后判断如果是 2 版删除成功，做一个数据的重新的渲染就 OK 了。好，现在我们就可以来写一下咱们的后端了。在我们的后端先写service，写一下public， void delete user address 传入两个参数，一个是 user ID，另外一个就是 address id。加上注释，根据用户 ID 和地址 ID 删除对应的用户地址信息。好，我们要去实现一下这个方法。事物拷贝加一下。在这里面我们也是根据用户的一个对象 POJO 去进行一个删除。


user address，直接写一个address，把它给 new 出来。在这里面我们只需要去放入两个属性的值就可以了，其中一个就是它的组件地址。组件 address ID 下一个 address the assets user id，把 user ID 给写进来。这样子它其实就包含了两个条件，一个是地址的ID，一个是地址对象里面的用户 ID circle。它会去做一个拼接的。我们就直接可以通过 map 点 delete 就行了。只需要把 address 写进来，它可以通过一个对象去进行删除。这里面包含了两个条件。好，OK。


service。写完之后，写一下咱们的 Ctrl 接口，快速写一下。因为删除其实是比较简单的， swag two 的名字接口名。我们要改掉。用户删除地址， notes 也改为一样。传过来的方法都是 post 路由，地址应该是delete。找一下前端和前端，这里对应。把 delete 拷贝一下贴过来。

好，OK。会传入两个参数，第一个参数，这两个参数其实都是请求的，参数有 quest pump，第一个是 string 类型 user ID，第二个直接拷贝，第二个是 address ID。好，OK，在这里面我们是需要去判空的，把这两个进行一个判空。如果 user ID 为空，或者 address ID 也为空，我们要提示一下，直接我们直接返回一个空字符串就可以了。


可能有同学会问，这个判断能不能不加，如果你不加，其实虽然我们在数据库里面，它这两个值为空，它是删除不了任何内容的，但是这个时候其实你的数据库就会被用户请求到了。所以一旦我们加了一个空数据库，它的一个请求是不会被用户访问到，如果有大量的空的一些属性，直接访问到数据库，数据库肯定会受到一些系列的影响，万一被别人攻击也不太好。所以这两个参数还是要判一下空，尽量的不要让空的数据到达数据库。


好，通过 delete 一下address。好，这样子就 OK 了。好，我们就可以来 install 一下了。 install 成功，再来一个重启。好，重启成功，到咱们页面里面去测一下。先刷新，我们可以先删除这个，先把这个地址删掉，点击确定好。OK，删除了。到数据库里面去看一下，现在是有两条数据，刷新一下，其中一条就已经是删掉了。好，随后再来一个，我们把默认的地址，也就是唯一的一个地址也删掉，点击删除。OK，删掉了，我们到数据库再看一下，刷新一下，现在数据库里面的数据就没有了。

