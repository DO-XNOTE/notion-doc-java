---
title: 2-5 mappings新增数据类型与analyze-
---

# 2-5 mappings新增数据类型与analyze-

[image](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/1f02d0dd-6bc0-4d77-8b50-a11fc4ab849a/SCR-20240805-otvr.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VBTZ4JY4%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T225131Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIAzZSoasT3FLdIVjePJy4FyYuaHRDYPiIslZg2alK4LOAiEAwcpQ77XFUWk5WEhWjh%2BkzO14NIrHRNge9QsEg2aHo0UqiAQIxv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDOhicQmzIEA2RLVilyrcA%2Fma5SSOkVRHz1Wacv7iw373SpIMExkKXGUA9AT4PE9N1QTqIEJpyN3L2bjBwytFxBnjrktExTQde9rDp3De0mOTrZbs3sRpwbqXOpUA%2FLvwQ6APZ4TyzremyW8%2Bx9HDEopM4LGEcwOZLt60GnQMfyd9Ze7usRE89P2i%2F0kW4tkp2P5da%2BY88aWZlox%2BXqvh4PFf9VICKC0NaQmDOrs3iKY1YXizLupG0nbEpGQcunNv50SYwx6Pv5gcORLyUPRjvvi0rbEd7Qhf7s5%2BA%2F0q0abWnNx8kuDBUt6EJXUVijzpIBGPPhmaQS0qFRlOyVUKv%2FVxBONhswsebLyfxfq9mCZRJPfScUD1seKG5mAa0eaPS0eSwXXGpOBw0pL2L9NuYEaFoDVJT3ZI3LL8Y%2B19mWqMKxRtxTRGRfwYd2Suq%2B42diJvmG%2Fj6qok467c%2FycEnltmPLgCtwMkMa%2FAp2EunFzxm8I%2FEQJesJimTxIUF92qortsk%2F60XC9CxXMQNLkdwVwTi%2Bf0b2KCygxP9%2BMgF2rh3RCmr83lDuZZbctcHZdpLKlGUpLHxcZxIOMnGN5g0NfEHKa66cvaUV6aGPMrP5xu5X3Hjdhl7G14nkesrOXm3zrMb25Sn2%2F0qrlHMJO4%2F9IGOqUB9cSeGoI0XyawnN9HbWFO%2BoY%2FAJY37sumKWvrk8ZHaziG7tJEYB5QqZVGyRtsKBFa4JVmcL3Sn41k4qLqCZSrGRWn3y8Kq7DljpM6xkQ2Xa%2F4Et3OQFQV9BEWFAR3P4l%2FectLvmzNVDxuJ%2F5VS2hTEZjDPJvhP6bNMJwIOpq6n73fqTBG%2BilXwaTe8HUM68U6L32LQ%2Bjr8y87bwBaLnq2hX4zelCM&X-Amz-Signature=9acdac59f3d1651dc5e91411219824f4ebe4b1db0c689a51d37837fb3cf9250f&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

[image](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/91925a3f-e7b2-48ed-a8aa-9891ff151793/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VBTZ4JY4%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T225131Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIAzZSoasT3FLdIVjePJy4FyYuaHRDYPiIslZg2alK4LOAiEAwcpQ77XFUWk5WEhWjh%2BkzO14NIrHRNge9QsEg2aHo0UqiAQIxv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDOhicQmzIEA2RLVilyrcA%2Fma5SSOkVRHz1Wacv7iw373SpIMExkKXGUA9AT4PE9N1QTqIEJpyN3L2bjBwytFxBnjrktExTQde9rDp3De0mOTrZbs3sRpwbqXOpUA%2FLvwQ6APZ4TyzremyW8%2Bx9HDEopM4LGEcwOZLt60GnQMfyd9Ze7usRE89P2i%2F0kW4tkp2P5da%2BY88aWZlox%2BXqvh4PFf9VICKC0NaQmDOrs3iKY1YXizLupG0nbEpGQcunNv50SYwx6Pv5gcORLyUPRjvvi0rbEd7Qhf7s5%2BA%2F0q0abWnNx8kuDBUt6EJXUVijzpIBGPPhmaQS0qFRlOyVUKv%2FVxBONhswsebLyfxfq9mCZRJPfScUD1seKG5mAa0eaPS0eSwXXGpOBw0pL2L9NuYEaFoDVJT3ZI3LL8Y%2B19mWqMKxRtxTRGRfwYd2Suq%2B42diJvmG%2Fj6qok467c%2FycEnltmPLgCtwMkMa%2FAp2EunFzxm8I%2FEQJesJimTxIUF92qortsk%2F60XC9CxXMQNLkdwVwTi%2Bf0b2KCygxP9%2BMgF2rh3RCmr83lDuZZbctcHZdpLKlGUpLHxcZxIOMnGN5g0NfEHKa66cvaUV6aGPMrP5xu5X3Hjdhl7G14nkesrOXm3zrMb25Sn2%2F0qrlHMJO4%2F9IGOqUB9cSeGoI0XyawnN9HbWFO%2BoY%2FAJY37sumKWvrk8ZHaziG7tJEYB5QqZVGyRtsKBFa4JVmcL3Sn41k4qLqCZSrGRWn3y8Kq7DljpM6xkQ2Xa%2F4Et3OQFQV9BEWFAR3P4l%2FectLvmzNVDxuJ%2F5VS2hTEZjDPJvhP6bNMJwIOpq6n73fqTBG%2BilXwaTe8HUM68U6L32LQ%2Bjr8y87bwBaLnq2hX4zelCM&X-Amz-Signature=3f9bde993f84100337809f589d95bf12ebf8b563b15d3e8163e2cbd843a70723&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

那么当我们创建了一个 mapping 之后，我们也是可以去验证一下上节课所说的。所以我们在 real name 它其实是可以去做一个 index 它是可以去做索引，是可以去做分词去查询的。 Q 的它其实一整段的文字它就是一个单独的查询的内容，它是不会被分的。我们可以来做一个相应的测试还是一样打开 post 面，我们把这个地址拷贝一份，然后来写一下。我们可以去查询去测试一下我们的一个内容，是否可以被做到对应的分词。什么是分词？就是我们在后续会具体的去说。那么在这里我们的分词其实就是把一段内容按照它的词汇一个一个的去进行切分。首先我们先是这里，这里是 get 我们要针对于 index mapping 针对我们的这个索引库去做一个对应的分词一个分析。然后来一个斜杠看一下，使用这个 analyse 这个其实就是分析分词的一个意思。那么随后我们也是也要去为它增加一个 body 使用 Jason 在这里写一下。


那么首先我们要去针对于我们哪一个字段，我们的 sell 的是哪一个？在这里我们使用之前有一个叫做我们看一下，我们设置的时候只设置了一个叫做 real name 也就是 user name 我们先把这个 real name 先拿过来，这个会作为我们的一个分析，随后我们要为他去输入一些相应的内容，也就是为这个 real name 去赋一个值。


比方说我们来一个 IMock is very good 好，随后那么这个是我们的一个文字，其实也就是它的一个属性文本内容。所以它的一个前缀在这里你要写上一个叫做 text 好，随后我们点击 send 来做一个分析。那么在这里你可以看到他能够拿到相应的 token 在这里其实是一个宿主，有一个 M 可有一个意思，还有一个是 very 另外还有是一个 good 总共是有四个单词。那么这四个单词其实也就是我们在分词过后的一个内容，所以我们在这里也能够看得出来，分词其实也就是把这里面的一段内容去做一个对应的分词。Ok 。那么在这里需要注意，我们使用的是一个英文，因为英文的话它是默认支持的。如果说你要把这个改成一个中文的话，可以看一下幕后网非常强大贬值线的。然后你会发现其实他会把我们的这个中文每一个单词每一个字会单独的给拆出来，因为它默认是英文的。标准的一个分词，其实它是识别不了中文的，所以我们后续会去做一个扩展好，然后我们恢复成一个英文就可以了。


这是一个 run 它是可以帮我们做到一个对应的分析，因为我们的 index 学的是 true 随后我们再把它改成一个 user name 随后我们再来做一个 send 发送一下来看一下。这个时候 token 在这里面就只有一项了，它的 token 只有一个，就是 IMock is very good 这一整段的文字。这一段的文本它其实就会把它作为单独的一个 kill 者。这个其实我们就是验证了上一节课中的一个 index true 或者说是一个 force OK 。


好，那么现在我们来看一下，目前其实我们针对于现有的一个映射，我们已经是写好了，但是写好之后能不能去做一个对应的修改，其实它是改不了的。比方说我们把这个 run 改一下改成一个 long 那么这其实也是它其中的一个数据类型，我们尝试的去修改一下，然后点击send ，那么这个时候肯定会报错，因为我们这个来看一下，当前这个其实已经是存在了，因为我们现在什么是这个 put 对吧？ put 是不行的，要去修改，其实应该要使用 post 贬值线的。


那么很明显这边也是不对，因为我们这个是 log 是 get push 和 head 你要去针对于我们现有的一个索引去做对应的修改，而且是针对于 mapping 的话，那么你在这个后方你要去加上一个斜杠下划线，你要去修改什么内容？ mapping 把这个给带过来。那么这是它的一个格式，再点击一个 send 然后他会报一个错。他会说我们当前这个 mapping 映射里面其实我们已经是包含了一个 run name 所以说你是不能够再去把它做一个修改，它是一个 unsupport 就说不支持的。也就是说一旦我们索引中某一项它的一个结构属性已经是收藏了，比方说主要内容已经修了，你是不能够去做修改的，你要修改只能把这整个删除重新去加。


OK ，也就是说前期你是需要去做把它给规划好去设置好的。OK ，当然除了我们已经存在的以外，你是可以去为它增加一些额外的内容。就说我们在这里比方说我们可以去这样子，因为我们的数据类型其实有很多种，所以我们会连带着它的一个数据类型为它去做一个相应的增加。比方说我们来一个 ID 这个 ID 我们就直接 tap 设置为是一个浪。然后这个 index 我们就拿掉，除了 ID 以外，再来为我们这个增加一个 H 年龄，年龄的话我们可以来一个 insins 的话，在我们 ES 中要使用 integer 这个 index 我们也去掉。那么这样子 ID 和 age 我们在之前里面其实并没有这两项的。


现在我们这样子去设置了以后，其实就是增加了额外的两个属性，点击 send 然后这边又报了一个错，说是我们 mapping 这个不正确是这样子，就是说我们要去做一个修改的话，这边的这个 mapping 我们要拿掉。OK ，这个是用于去增加的。因为现在我们之后所以这个 mapping 是不需要了。


OK ，再一次点击 send 然后 OK true 表示成功了。随后回到我们这个 title 插件，刷新一下到我们的这个里面来看一下。这个时候我们的 ID 和 H 就已经新增加了， ID 的话是让 H 是 int 好，随后我们继续除了这些类型以外的话，其实它还会有一些其他的类型。那么我们都在这里可以去加一下。比方说可以再来增加一个尼克尼克，我们这样子，尼克 name 名称我们其实是有了一个是 text 一个是 qword 我们也验证过了，所以就不加了。


我们来一个金额，来一个 money 金额的话我们可以使用 double 那么这是一个浮点对吧，我们来一个money ，再来一个 money 2，除了这个 double 以外，它还会有一个叫做 float 好点击 send 一下，成功之后我们到这里面刷新一下，再来看一下。那么这个时候我们的这个 money 2 money 1 都有，这个 type 也都 OK 然后我们继续来加一个，现在的话我们再来加一个。因为除了像我们的数值类型，除了 long ins 以外，其实它还会有 byte 和 short 我们拿一个 sex 性别的话我们来设置成一个 byte 此外我们可以再来加上一个比方说分数，学生考试的一个分数几个，那么我们就给他可以为他设置了一个 short 远致线的。


好。 OK 随后我们再来刷一下。在这里面我们可以看到这个 sex 和这个 store 就已经是又被我们修改进来了，我们所说的修改就是新增我们的一映射。好，随后我们再来看一下，除了这些类型以外的话，其实它还会有一些像 truefalse 还有一些时间日期的类型，其实也可以去做。比方说我们为这个人去加上一个比方说来一个 is teenager 这个我们可以来设置成是一个不保值。然后我们再来这个人的一个生日 birthday 这边我们可以设置为是一个 date 类型。此外的话其实它还可以去，因为它本身是文档对吧，它是一个 JSON 数据类型。所以对于我们某一个内容某一个属性来讲的话，它其实也是可以去包含一个 object 其实也就是我们的 Jason 的一个数据是可以包含进去的。在这边我们取一下，比方说我们的一些这个人物的人际关系，来一个 relation shop 好，那么就是出了 force 就是使日期，这个是一个对象点击线的。


好OK ，成功我们再来刷新一下。在我们这个索引信息里面，相应的内容全部都会可以看得到。有一个 date 还有是我们的 true force 。另外我们的一个 object 来看一下。在这里。逻辑关系履约新设法菜盘是 object OK 这样子执行就已经是为我们现有存在的某一个索引额外的扩展了一下其他的一些 mapping 的映射。
OK ，同时的话我们也是附带的去讲了一些相应的主要的数据类型。那么这些数据类型其实我们也是来看一下，在文档里面我们也是会提供的这个部分，在这里有一个有这些主要的数据类型。那么这个 string 需要注意，string的话目前我们新版本只是没有了。


在后面提了一下这个数组，就说我们也是可以去设置一个数组的。设置数组的话其实我们它的类型必须要一致，比方说我们数组里面每一项都是字符串，或者说我们每一项都是一个运行，就是说你必须要一致。如果说不一致的话，那么肯定是不能够去设置的，这个也是需要去住的，这个也就是它所支持的一种数组类型。当然数组中去嵌套，再去放入一个一个的 object 肯定也是可以的。


OK ，那么这节课就是我们通过额外的一种扩展的方式，为现有的一个索引去新增加的一些国外的 mapping 词的映射。此外我们也是通过了我们的验证。就是说我们验证了上一节课里面所说的一个 text 就是 Q 的，看一下他们能不能够对进行相应的一个分词。OK ，大家在课后也是可以跟着我们的一个步骤去敲一下，去注意一下它的一些相应的内容。

