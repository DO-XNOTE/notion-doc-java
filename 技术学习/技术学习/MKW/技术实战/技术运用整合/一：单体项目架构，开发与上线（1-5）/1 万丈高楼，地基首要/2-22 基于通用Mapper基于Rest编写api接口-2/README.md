---
title: 2-22 基于通用Mapper基于Rest编写api接口-2
---

# 2-22 基于通用Mapper基于Rest编写api接口-2

[image](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/bbc85fc2-773b-4bb2-9ee8-9e6d9b3506fb/SCR-20240816-qgrp.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466V2LHBWV2%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T224615Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCrKgQ7pCPjda2rHh4qEiWK42PUsqYA5WQLaoDa8%2BRNYwIhAM%2Fu8GxPiCgVaymjF%2BUkG8wwN4IGth%2FKRzW%2BP94%2FuNAHKogECMb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1Igz8ERZvNl3kZZH8spUq3AMFju6Ptqup7DzMJeDwwlIWmHYOl%2B%2F2a60JYtCzpN1mXxhgrO0LkF3hmO0I5xwgujh1RYFtw1dP8tRlv4eE9QtHtl4%2FOoJrP6OtwuLI87PFGz%2B%2BVJtGSYweggi2wt3ITBBEwGvfaF0tnYasA1Jf3TQcAICckD%2FEgiNfvl95x3MLG93ZVhfig1AMRqsHrYmlWfdp%2BVC8GbRkfkDWUTkOuFFO%2F1jgsp7QmFsXNw4dALUP%2F0bVF6ABO2mKjvxzeztxAJSudqJEYF9TKW1jNaMLfWgvUrg1QH7SO2V2ifamAeBH0%2BMvI8rjtM7sSXNU39ng6pNgoGPjFYd1t6TtqwoeugBpOP%2BCLlEGOqWabJ7gQGV0JMxUpV0NjkiNS%2FARedOge%2FNLccvmJnPiZQ86TwUY3fI9E0RqUFiuQArG1VI6YV4jzLzalahDW%2F5HF5qSI4s%2BPRJNYDqm%2F1wrAr7D20%2BCqJ5%2Bz7EzcuiMxn4zMBkbhhP%2BoK5jHHRXYqbvQ4HFs86hu99lv7QvHdgAW0XNBZxIvXKSm3rTUfB8OIi0kGpPWx%2FZeaeKJcDLjye3yCCungWLRjMIreHw9XkMIjDTShMwzKa37Oib35A3XnPomOO4NiwAUBcGQ7gNGoxk6ZqmkzCOuv%2FSBjqkAaOyP9Hz494gBIPBIMGu6lhKd%2BS7rE6LPkSUiZ%2B8463ZYC0Vb85nM%2BBvaBS%2F59T7gDtK1u8IAhR001SKhS%2BNJL0QB%2BvPwzJwtAoi2ic%2BAaLhjDh3cix0fv8nIOUjffMZaucGQ8pjpf5T72ECPIS7fbzxFAoMvnh1FTV4RPq4SrZG%2FjD7zPJHD1ESUVj0IDsRS5YL9HYMHAp8uz2%2BJUDtEWWqQLgq&X-Amz-Signature=20eabd447495ef32147862a3081abe26c509eb8aa532f0cbba2d02d83ad98f81&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

[image](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/6ff2aa44-d82c-4a7d-98f7-54fd26621c96/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466V2LHBWV2%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T224615Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCrKgQ7pCPjda2rHh4qEiWK42PUsqYA5WQLaoDa8%2BRNYwIhAM%2Fu8GxPiCgVaymjF%2BUkG8wwN4IGth%2FKRzW%2BP94%2FuNAHKogECMb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1Igz8ERZvNl3kZZH8spUq3AMFju6Ptqup7DzMJeDwwlIWmHYOl%2B%2F2a60JYtCzpN1mXxhgrO0LkF3hmO0I5xwgujh1RYFtw1dP8tRlv4eE9QtHtl4%2FOoJrP6OtwuLI87PFGz%2B%2BVJtGSYweggi2wt3ITBBEwGvfaF0tnYasA1Jf3TQcAICckD%2FEgiNfvl95x3MLG93ZVhfig1AMRqsHrYmlWfdp%2BVC8GbRkfkDWUTkOuFFO%2F1jgsp7QmFsXNw4dALUP%2F0bVF6ABO2mKjvxzeztxAJSudqJEYF9TKW1jNaMLfWgvUrg1QH7SO2V2ifamAeBH0%2BMvI8rjtM7sSXNU39ng6pNgoGPjFYd1t6TtqwoeugBpOP%2BCLlEGOqWabJ7gQGV0JMxUpV0NjkiNS%2FARedOge%2FNLccvmJnPiZQ86TwUY3fI9E0RqUFiuQArG1VI6YV4jzLzalahDW%2F5HF5qSI4s%2BPRJNYDqm%2F1wrAr7D20%2BCqJ5%2Bz7EzcuiMxn4zMBkbhhP%2BoK5jHHRXYqbvQ4HFs86hu99lv7QvHdgAW0XNBZxIvXKSm3rTUfB8OIi0kGpPWx%2FZeaeKJcDLjye3yCCungWLRjMIreHw9XkMIjDTShMwzKa37Oib35A3XnPomOO4NiwAUBcGQ7gNGoxk6ZqmkzCOuv%2FSBjqkAaOyP9Hz494gBIPBIMGu6lhKd%2BS7rE6LPkSUiZ%2B8463ZYC0Vb85nM%2BBvaBS%2F59T7gDtK1u8IAhR001SKhS%2BNJL0QB%2BvPwzJwtAoi2ic%2BAaLhjDh3cix0fv8nIOUjffMZaucGQ8pjpf5T72ECPIS7fbzxFAoMvnh1FTV4RPq4SrZG%2FjD7zPJHD1ESUVj0IDsRS5YL9HYMHAp8uz2%2BJUDtEWWqQLgq&X-Amz-Signature=caf6fc39a0736eff712df7d771e75f4c187b4fd3f9101598e79aaca1f0d0bf54&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

第一个查询的我们已经是做完了，做完了以后，接下来我们来看一下。在咱们的 service 里面， s t u map 下方是有波浪线红色的，代表它是有问题的。我们之前也说了，这是Mybatis 开发工具的一个问题，使用 eclipse 是不会有这个问题的。如何解决这个问题，其实我们只需要在开发工具里面去做一点设置就可以了。找到 Preference，在这个里面会有一个inspections，在 edit 下方再找到，这里面会有一个 spring core，这个 spring core 其实就是和 spring 相关的。再往下面找。

[image](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/2badd35b-9bc4-4de5-ae88-c745903cebd5/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466V2LHBWV2%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T224615Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCrKgQ7pCPjda2rHh4qEiWK42PUsqYA5WQLaoDa8%2BRNYwIhAM%2Fu8GxPiCgVaymjF%2BUkG8wwN4IGth%2FKRzW%2BP94%2FuNAHKogECMb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1Igz8ERZvNl3kZZH8spUq3AMFju6Ptqup7DzMJeDwwlIWmHYOl%2B%2F2a60JYtCzpN1mXxhgrO0LkF3hmO0I5xwgujh1RYFtw1dP8tRlv4eE9QtHtl4%2FOoJrP6OtwuLI87PFGz%2B%2BVJtGSYweggi2wt3ITBBEwGvfaF0tnYasA1Jf3TQcAICckD%2FEgiNfvl95x3MLG93ZVhfig1AMRqsHrYmlWfdp%2BVC8GbRkfkDWUTkOuFFO%2F1jgsp7QmFsXNw4dALUP%2F0bVF6ABO2mKjvxzeztxAJSudqJEYF9TKW1jNaMLfWgvUrg1QH7SO2V2ifamAeBH0%2BMvI8rjtM7sSXNU39ng6pNgoGPjFYd1t6TtqwoeugBpOP%2BCLlEGOqWabJ7gQGV0JMxUpV0NjkiNS%2FARedOge%2FNLccvmJnPiZQ86TwUY3fI9E0RqUFiuQArG1VI6YV4jzLzalahDW%2F5HF5qSI4s%2BPRJNYDqm%2F1wrAr7D20%2BCqJ5%2Bz7EzcuiMxn4zMBkbhhP%2BoK5jHHRXYqbvQ4HFs86hu99lv7QvHdgAW0XNBZxIvXKSm3rTUfB8OIi0kGpPWx%2FZeaeKJcDLjye3yCCungWLRjMIreHw9XkMIjDTShMwzKa37Oib35A3XnPomOO4NiwAUBcGQ7gNGoxk6ZqmkzCOuv%2FSBjqkAaOyP9Hz494gBIPBIMGu6lhKd%2BS7rE6LPkSUiZ%2B8463ZYC0Vb85nM%2BBvaBS%2F59T7gDtK1u8IAhR001SKhS%2BNJL0QB%2BvPwzJwtAoi2ic%2BAaLhjDh3cix0fv8nIOUjffMZaucGQ8pjpf5T72ECPIS7fbzxFAoMvnh1FTV4RPq4SrZG%2FjD7zPJHD1ESUVj0IDsRS5YL9HYMHAp8uz2%2BJUDtEWWqQLgq&X-Amz-Signature=c7bb7baceca6c50fe722ebda238203ba2792c2bd48e2da17ee955ab6e2c21007&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

在 code 里面有一个 autowearing for bean class，这个其实就是注入的有一个勾，你可以去掉。或者在这边的一个错误级别，你也可以改成其他的，比方我们把勾给去掉，我们直接点击OK，这个时候你会发现下方的红色波浪线就去除了。这一点是需要去注意的，因为我也已经是遇到过有几个同学碰到过这种问题，所以我们在这边可以通过这种方式去掉。随后我们就应该要完善其他的几个方法，分别是保存、修改和删除。我们快速的来编写一下。我们可以把 s t u map 先拷贝一下，由于它是一个保存操作，我们来看一下。


有一个insert，你会发现在这边有很多的一些方法，其中第一个就是我们所需要去使用的是 insert student，其实还有一个是 insert c native。这两者有什么区别？其实我们在之前的文档里面也提过了。 selective 在保存和更新的时候其实都有用到。其实就是针对于它的一个now，如果它某一个属性是空，是不是会覆盖掉我们的一个元数据。是针对有一定的区别。在这里我们可以来一个音色的student，在这边我们 Stu 直接去 new 一下就可以了。 Stu 快速的去创建一下。


s t u，放到这里它就可以去做一个保存了。相应的数据我们是需要去设置的。先 set 一个name，比方来一个Jack，再来一个 s t u，点 set age，来一个 19 岁ID。由于在数据库里面是自增的，所以我们就可以不用去设置了。保存的方法就已经是写好了，下一个是根据 ID 去修改某一个 s t u，在这边也是一样，把 map 拷贝过来一个 up date by 看一下。


在这边我们可以使用这两者其一，当然也可以使用 example 也是没有问题的。根据条件去进行一个更新。它的场景是适用于有多个不同的条件，比方你的一个年龄区间，还有是你的一个ID，在某一个区间之内，都是可以去做到这种批量的更新的。所以在这种情况下，我们可以在这种多条件的情况下可以使用example，否则我们就直接使用根据组件去进行一个更新就可以了。

我们使用 update by 组件，我们把 Stu 直接的拷贝进来， ID 直接我们在这边，我们是需要去设置的。 s t u 点 set ID， ID 传入我们的名称。我们可以比方来一个Lucy，年龄设置为 20 岁。再把 Stu 放进来，这个时候它其实就可以去做一个更新的操作了。


好，下一个是一个删除操作，删除十分简单， map 点有一个delete，这个时候有一个 delete by 组件，把 ID 传进去，它就可以去做一个删除了。最后一个不要忘记这三个我们都还没有加上这个事务，这个事物的传播我们也是要需要去加的。在这里面我们可以使用 request 就可以了。好，我们在这里边都进行一个直接拷贝过来就行了。现在我们的 service 这一层就已经是写完了，随后接下来我们要去完善一下咱们 Ctrl 的控制层，把进行一个拷贝。我们之前也说了，我们要符合它的一个 rest 否规范。我们在这边我们所有的增删改我们统一都使用post，使用 post mapping 就可以了。


比方现在我们要去做一个保存，保存，直接来一个 save s t u，对于保存来讲，它其实在这个里面它不需要传入任何的东西。把删掉，然后直接调用 save 这个方法就可以了。它也不需要做一个return，所以 return 我们放在这里，拉一个 return OK，或者 return 一个200，状态也没有问题。


好，下一个是更新操作，在这边直接写一个 up date s t u，方法名，不要忘记，要统一的去修改传的ID。其实我们在这边是定义传入一个 ID 的值，所以我们也只需要把 Int 值写过来，相应的来一个update，再把 ID 放进来。好，这是更新操作，最后再下一个。这个时候我们来一个delete， delete s，t，u，这样子就 OK 了。


现在我们在控制层写的 3 个方法也是比较简单，他们这几个全部都是 restful web service 这样的一种接口，是可以被外部可以给客户端去调用的。只不过现在我们都是 post post，其实它在浏览器里面是无法访问的，这一点是需要去注意的。

对于我们的一个 rest for web service 这样的一个接口，我们有一点是需要去注意的，接口的一个幂等性。幂等性在后续的课程，会有老师专门开一节课来谈一谈什么是幂等。在这里边我们也可以先说一下，如果我们是保存一个数据到数据库，其实它暂时的，我们可以认为它是不包含幂等性的。因为如果我们多次调用这样的同一个接口，数据库里面可能会有多条记录被保存。


再来看我们的更新和删除更新，其实它是有幂等的，也就是接口被重复的调用多次，它只会根据 ID 去更新某一条记录。也就是不管你执行 100 次还是1万次，这一条记录，它其实一直都会被更新，它不会被影响。此外还有是我们的删除操作，当某一条记录根据 ID 去被删除了以后，第一次是删除了，第二次你再去删。其实这一条数据在数据库里面本身就没有，所以你并不会去删除其他的记录，也就是更新和删除这两个操作。他们其实是有一种幂等性的。对于保存它其实本身是不包含幂等。当然你可以依靠一些相应的代码去来配合着它去实现幂等性也是没有问题的。OK，幂等在后续有一部分的课时，会有专门的老师再来细说一下的。现在我们针对于这 3 个接口，其实我们就已经是写。


