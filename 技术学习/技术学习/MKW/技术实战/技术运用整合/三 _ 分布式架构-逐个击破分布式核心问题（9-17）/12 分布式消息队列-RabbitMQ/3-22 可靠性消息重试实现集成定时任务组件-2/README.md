---
title: 3-22 可靠性消息重试实现集成定时任务组件-2
---

# 3-22 可靠性消息重试实现集成定时任务组件-2

[image](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/baa9ce9a-8dea-44ec-932a-b51235a66880/SCR-20240807-fneh.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZKATTIZC%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T225313Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIGnyYVwZxp3E%2FvbXP2rEt7b9e5f3qGket1dGJWRJzYpnAiEA9SYuo9DH4qFI64iXXvLp%2BbjsiS36HRX%2BeI5JhPDtA4oqiAQIxv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDHXT%2F8kOhp%2FAHN5YeircA2zz%2BxUOUp4QyK%2FoVDw9btrehDQgpQl3rVuJo89pGXXNCktZg0LiQsiMe3oSSkupI6ixANmMFaPcsyd62yik4YkZ3GdWR1kXxlLuFrQO15xakFRhj2RuYYfjI34OCa7lGtoLrayx6PQVvq14dR5mLyRz2v%2F5F3VrnAMGJI90ToMCXg2RusA7USMe2kgXzneb5ZhqG4n1M5fQuWD1lVqHu7gyRuQx%2Fyu3kB5HeYV2f6iPiogp9AEB3r6kRnX84%2BiIu7XjO6a8LOBu0CHkz6fD8ggrA%2FpIlhZhJL%2BOhQAxbRp9%2F%2BAROnTbjyFT6TYVcFlbOeUnJHSxpnKUyvdakG2%2F9X5dqZqPL50EVhJuDM8yTTb2Gy%2FHKrQGX0MXnCv4bEi13ngfHj87CJASCtQ52GN9wxJD5ZPKIJtmGg3Cou9K4Cf9r4JNtshz7X5pXCB%2F%2FOB84rTAM2%2F6WTyZImFOqKQIdD8t949Q8dq9DDicLxF0BWy4q%2BHirmbwhiZo7gvBTnM920gx%2B41XOJqEUzdTGQ5rsR9h8ItDLswTFpUMjoXKSby2SyuZuAk108m2HChfbgMsgbk9bgbC%2FJpNQ32fZjOXez9aln2553klea%2FAsztiTvQLZbLJpk%2F157BYGSz1MIe3%2F9IGOqUBpMFHJONx1iB1qae84i3gFgIvHO9Yb2wxjv%2Bt9SaG9cZ55BhvdVKxeC%2FAscv1f%2FW69DSG0BYbAypxdxtsuhBux9ZEfgIjU%2FdT2%2BPCDSlGCclFZAEAVPb9%2Bmznj6E8Mq%2BkIE3Qb5k3Ixo7y53mpQfPZq%2BOijPyBUHm%2FrAuVchjrvoYWM4tiaIJjHb92Uk%2FjK5c%2BlRB6lhO0POsnIm0fXtTVemjnKOd&X-Amz-Signature=a978e15d040e2f753d643b035b7d48eb8fe233ac57305f77f6a3dbd9c7b400fc&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

[image](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/131366b2-b65c-4dca-afc3-0a99bf8b369e/SCR-20240807-flnf.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZKATTIZC%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T225313Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIGnyYVwZxp3E%2FvbXP2rEt7b9e5f3qGket1dGJWRJzYpnAiEA9SYuo9DH4qFI64iXXvLp%2BbjsiS36HRX%2BeI5JhPDtA4oqiAQIxv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDHXT%2F8kOhp%2FAHN5YeircA2zz%2BxUOUp4QyK%2FoVDw9btrehDQgpQl3rVuJo89pGXXNCktZg0LiQsiMe3oSSkupI6ixANmMFaPcsyd62yik4YkZ3GdWR1kXxlLuFrQO15xakFRhj2RuYYfjI34OCa7lGtoLrayx6PQVvq14dR5mLyRz2v%2F5F3VrnAMGJI90ToMCXg2RusA7USMe2kgXzneb5ZhqG4n1M5fQuWD1lVqHu7gyRuQx%2Fyu3kB5HeYV2f6iPiogp9AEB3r6kRnX84%2BiIu7XjO6a8LOBu0CHkz6fD8ggrA%2FpIlhZhJL%2BOhQAxbRp9%2F%2BAROnTbjyFT6TYVcFlbOeUnJHSxpnKUyvdakG2%2F9X5dqZqPL50EVhJuDM8yTTb2Gy%2FHKrQGX0MXnCv4bEi13ngfHj87CJASCtQ52GN9wxJD5ZPKIJtmGg3Cou9K4Cf9r4JNtshz7X5pXCB%2F%2FOB84rTAM2%2F6WTyZImFOqKQIdD8t949Q8dq9DDicLxF0BWy4q%2BHirmbwhiZo7gvBTnM920gx%2B41XOJqEUzdTGQ5rsR9h8ItDLswTFpUMjoXKSby2SyuZuAk108m2HChfbgMsgbk9bgbC%2FJpNQ32fZjOXez9aln2553klea%2FAsztiTvQLZbLJpk%2F157BYGSz1MIe3%2F9IGOqUBpMFHJONx1iB1qae84i3gFgIvHO9Yb2wxjv%2Bt9SaG9cZ55BhvdVKxeC%2FAscv1f%2FW69DSG0BYbAypxdxtsuhBux9ZEfgIjU%2FdT2%2BPCDSlGCclFZAEAVPb9%2Bmznj6E8Mq%2BkIE3Qb5k3Ixo7y53mpQfPZq%2BOijPyBUHm%2FrAuVchjrvoYWM4tiaIJjHb92Uk%2FjK5c%2BlRB6lhO0POsnIm0fXtTVemjnKOd&X-Amz-Signature=4328a6fd26e3384c7a1d6ea7b102ad1288a54292b33a36353ad49a4b9fc04f08&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

[image](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/e8efd1e9-022b-4d6c-b9eb-19e7e9caa409/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZKATTIZC%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T225313Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIGnyYVwZxp3E%2FvbXP2rEt7b9e5f3qGket1dGJWRJzYpnAiEA9SYuo9DH4qFI64iXXvLp%2BbjsiS36HRX%2BeI5JhPDtA4oqiAQIxv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDHXT%2F8kOhp%2FAHN5YeircA2zz%2BxUOUp4QyK%2FoVDw9btrehDQgpQl3rVuJo89pGXXNCktZg0LiQsiMe3oSSkupI6ixANmMFaPcsyd62yik4YkZ3GdWR1kXxlLuFrQO15xakFRhj2RuYYfjI34OCa7lGtoLrayx6PQVvq14dR5mLyRz2v%2F5F3VrnAMGJI90ToMCXg2RusA7USMe2kgXzneb5ZhqG4n1M5fQuWD1lVqHu7gyRuQx%2Fyu3kB5HeYV2f6iPiogp9AEB3r6kRnX84%2BiIu7XjO6a8LOBu0CHkz6fD8ggrA%2FpIlhZhJL%2BOhQAxbRp9%2F%2BAROnTbjyFT6TYVcFlbOeUnJHSxpnKUyvdakG2%2F9X5dqZqPL50EVhJuDM8yTTb2Gy%2FHKrQGX0MXnCv4bEi13ngfHj87CJASCtQ52GN9wxJD5ZPKIJtmGg3Cou9K4Cf9r4JNtshz7X5pXCB%2F%2FOB84rTAM2%2F6WTyZImFOqKQIdD8t949Q8dq9DDicLxF0BWy4q%2BHirmbwhiZo7gvBTnM920gx%2B41XOJqEUzdTGQ5rsR9h8ItDLswTFpUMjoXKSby2SyuZuAk108m2HChfbgMsgbk9bgbC%2FJpNQ32fZjOXez9aln2553klea%2FAsztiTvQLZbLJpk%2F157BYGSz1MIe3%2F9IGOqUBpMFHJONx1iB1qae84i3gFgIvHO9Yb2wxjv%2Bt9SaG9cZ55BhvdVKxeC%2FAscv1f%2FW69DSG0BYbAypxdxtsuhBux9ZEfgIjU%2FdT2%2BPCDSlGCclFZAEAVPb9%2Bmznj6E8Mq%2BkIE3Qb5k3Ixo7y53mpQfPZq%2BOijPyBUHm%2FrAuVchjrvoYWM4tiaIJjHb92Uk%2FjK5c%2BlRB6lhO0POsnIm0fXtTVemjnKOd&X-Amz-Signature=551bfc2ccf1e33843ccf929029a182ac94f2e84338f6ee9e8ee1e100bd86ff13&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

既然他交给我们 spring 管理了，理论上讲就是 OK 的，那我们现在需要哪些东西？我们需要操作数据库，所以说肯定要用到我们 private message store service，这个 service 肯定得用，因为我们得操作操作数据库去，起码要把这个数据抓出来，需要用到这个service，然后 out where 直接注入进来。


好，还有一个我们要做重新发送，是不是你得有重新发送的一个客户端？我们有一个叫做 Rabbit broker，起码是有它了把它拿进来。嗯，因为 Rabbit broker 里边有帮我们去发送的方法，对不对？它里边有一个什么？具体你要发迅速消息，还是 confirm 消息，还是说可靠性的消息，还是说批量消息，对不对？它里边有这个接口，它的接口下面有具体实现类，就是 Rabbit broker implements，对不对？这就是我们发送的逻辑嘛？OK，就是说首先第一点我们要确定一件事情，就是说我们整个这个定时任务肯定得需要两个这个对象，一个是 message 到service，还有一个是 let it broker，一个用于做抽取数据，还有一个用于做什么呢？重发消息。


好了，那我们来看看这个抽取数据怎么去做吧？我肯定得去找到符合我要求的数据，然后我把它抽取出来，对不对？那我就要用到它这里边的具体的方法了，那我来看一看它这里边具体有什么样的方法？这个 message 到 service 里边有什么？具体有什么方法？我们先把它注释掉，这个先返回，那先在这里也写出来，我们先点进去看一下这个 message 到service，那我们看到了这里边并没有我们想要的就是具体的这个发重发的方法，那怎么办呢？我们来点这个map，看看 map 里有没有，看 map 里有没有，然后你再确认，你看我 map 里边之前已经写好了很多，比如说这叫做 change broker message state，就是改变这个这一条这个 ID 所对应的那个那条记录的这个状态。这个其实是就是消息确认 success 或者 file 的时候会去使用的。然后下面还有一个什么呢？叫做。

Query broker messages this for tomorrow.


是不是就这个方法呢？是不是我觉得这个方法比较像，是吧？给我一个 state 状态，那这个 state 状态肯定是等于三定状态，就是他在待确认的状态，然后我们去看一下对应的这个mapping，你知道了mapping，我们去找到这个SQL，我看这个 SQL 怎么去写的select，然后一堆数据 from 这张表，然后 where 条件就是 state 等于什么呢？等于你给我传进来的state，然后 and 条件 next retry 小于当前时间。


同学们想一想，我的 next retry 肯定比如说我第一次发送的时候，比如说是 9: 01，那我如果是超时一分钟的话，那我下一次 next return 是肯定是 9: 02 了，对不对？所以说如果当我轮询出来，我的 next return 时间已经大于当前时间，就并且这个状态还是三定的状态，那我就认为这个消息是有问题的，我要去做重发，所以说就是这个SQL，那这样的话我们就回过头来就调一下这个 SQL 就好了，就是我的 service 调这个具体这个 map 的这个方法。


好，我们在这里可以再写一个方法，比如说叫做public，这个往上一点叫做public，然后大家返回的肯定是一堆集合，它不可能一个就是符合我条件的一堆的，这个叫做 broke message，然后我们在这里叫做query，或者叫做 fetch come out message for retry 可以。起一个这个名字。然后他只需要给我一个什么呢？他只需要给我一个这个state，对不对？就是你的这个状态是什么？我这里边有一个古 rocker state，是不是有一个 broker state？好，这个 broker state 我传进去就可以了，然后在我这里我叫做 this 点 broker map，点 query for come out，然后直接传进去，它是一个死针类型，那我就 get code 就好了。OK，好，这就可以了。那这个方法直接最后它返回一个list，那我们直接需要 return 一下。


好，这个方法我就写完了，就是用于我们定时任务去重新抽取的一个函数。好，那我们再回到这个 job 里面，很简单，那我们就调这个 service 点fetch，然后 state 就是我们 sending 的状态，就是 broker message state 点什么？ sending 就是这个状态对不对？只要是这个状态的，那它超过 next 宇拽的时间，那肯定是都被我抽取出来了，是不是？那其实在这里我可以先把它变成一个list，其实我要做什么事情？我其实想打印一下具体的参数，我们讲至少是做个log，因为这时候再去return，然后接下来这里边我们加一个s，l，f，o， g 然后我要打印一下是不是让同学们看一下这个到底执没执行。


log 点infer， log 点 infer 我叫抓取数据结合，然后抓取数据集合，数量是多少是不是？那就是 list size 就好了，数量是多少那就是我们的加上我们的list，点size，OK，每次打印这句话就表示我们的数据集合确实被抓取了，是不是？它不是一个这个音FER，我就直接一个大括号替换，然后空格，然后这个里面就打个逗号就行了，就这个大括号被这个的变量所替换了，好了，搞定。


只要是每次说我定时任务能打印出来这句话，就证明起码执行了，OK，然后他会把数据返回给我们的这个process，就是传递到我们的下一个这个实现里面，那么它实现一下，那同学们想一想，就这些数据肯定是需要用定时任务去做重试的，是不是？那这个我们给它起名字叫做 date list，对吧？大家都知道它是一个集合，就是符合我们现在条件，就是需要做重试的一些数据，那我们怎么去做呢？首先我们得挨着牌儿的一个一个的去对这个 date list 去做一些相关工作。那我们就是 for 抑制循环嘛，我们循环这些数据，那每一个数据都是 broker message，我们可以写 broker message，每一条数据我应该对它做一个处理，在这里我们就来看一看。


首先你应该做一个判断，因为我们最大的这个 Max Retry 是多少次？老师在之前已经规定死了，说他最大的重试次数就是 3 次。这个是在我们第一次做可靠性投递方法，然后入库做 insert 的时候已经规定死了的。还记得就是它有一个Max，就相当于我们的 Retry count，这是 next Retry，然后这个 count 那个值默认是0，还记得来点进去就这个 Retry card，它莫是0，那我们如果认为说它超过最大的重试次数，在这里我们就可以想如果是超过 3 次，我就认为什么呢？就不重试了，就失败了。就是说那我在这里边可以定义一个变量哈static，然后 final Int，咱们叫做 Max Retry count Retry 等于3，可以就是说你最大的重复次数就是不能超过 3 次，不让你从事。


那我们第一件事情要做判断吗？我取出来的这个集合它肯定是 sending 状态，但是我不知道它已经重试了多少次了，所以说我从 broker 中点 get 什么呀？ get retry count，我们判断如果它大于等于我们刚才所定义的这个值，那就证明什么呢？就证明你都是大于等于 3 了，然后你还失败了，那这条消息我就不做处理了，那你有什么意思吗？我们可能就比如说进到失败表或者怎么样，那我就直接去打个标，我说 this 点就是我们自己的这个 store service，讲什么呀？fail，就是把整个的这个ID，就整个的这条记录置为 fail 就可以了，就不处理了，对吧？就是已经超过我们最大努力尝试的次数 3 次了。


OK，那如果 else 的情况呢？同学们想一想， else 就是它还小于 3 次，它还可以进行重新尝试吗？比如说他刚从事第一次或者重试第二次，对吧？那这个时候我们是不是也应该做一些处理？然后这块我其实可以去加一个log，比如说 log 点 wonder 做一个预警。


说什么呀？消息重试 Max retry，这个次数对不对？消息重试最终失败，对吧？然后消息ID，消息设置为最终失败，然后消息 ID 是什么？那我们就来写一写消息，消息 ID 是什么啊？打个逗号，然后把这个博客 ID 放到这里来可以，好，这最终失败了。


OK，我们来继续往下看，如果说它小于 3 次，小于 3 次我们是不是还可以重新投递？所以说首先小于 3 次这个变量就起到作用了。这个对象，那他呢？就应该是 list 点，他点什么呢？比如说他要做厨师，是不是就 confime 就可以了？就不用再去做什么了，再去做可靠性投入了，在那里同学们想一想是不是这样，对吧？然后消息从哪来？这消息从哪来？消息？我说全量的消息体都已经保存到 broker message 里边的 get message 里面了，对不对？我就直接 get message 取到它就好了。


然后有同学说老师这里边的那个 message type 是可靠性的，那你这个发到这个肯定算的，这个能行吗？我看一下是不是可靠性的，但是我拿到消息之后我又把它改成config，所以说没问题。所以说他还是终究要是要回 config 的，他不会去走什么呢？不会走那个 relay 克萨的，因为这个是什么？这个是更底层的一个 API 了，我们之前上层的 API 就是根据 message 的 type 去判断到底走哪个，那个是 producer client 里边要做的事情，对不对？像 producer client 里边这是非常顶层的API，就直接暴露给这个开发给用户去使用的，他只要是把 message 里边这个 type 给我填好了，然后我具体调哪个，但是我们刚才底层直接用的就是这个 Rabbit broker 这个API，所以说这个更直接更清晰。


好了，那这样的话就是相当于又重发了，重发假设是说重发他还会做什么事情，他不会再去音色的一条记录了，这是第一点。第二点就是说重发了之后如果确认，那肯定会走这个 confirm 消息，对吧？就是走这个container，重发确认他肯定会把消息走confirm，对不对？回来的时候再次去判断一下这个 ID 到底 o 不OK，就给它更新成success。


如果说直接是发 confime 消息的话，那这句话是不是你压根就没有去做处理？就是你现在做的事情是不是就相当于你去访问了一下数据库，根据 ID 去查一下这个数据库，如果有这个ID，我把它更新成success，对不对？在这里我打个注释，这个很关键，所以说你要做一个区分，就无论是很费用消息还是 react 消息，就是都会去发送消息，以后就说我们的 broker 都会去回调我们现在的这个什么 consume 方法，那 consume 消息虽然说是确认，但是他消息落库吗？他不落库，只有这种 reluctate 消息才落库，所以说理论上来讲像 confirm 消息压根我就不需要去对他做判断，那么 react 消息他每次肯定需要查数据库，就博尔克给我们回送回来 confirm 他的 ACK 到底成功失败，我们肯定要作为更新。


所以说那你可以在这判断说if，如果说他的这个 message type，如果是 renike 的话，然后你再去做这个事情，这就可以了。但是有一点，你在定时任务的时候，你这里不是 resend 了吗？ resend 了你做什么事情呢？你做 resand 的时候做重发，你投递的是这个config，对吧？所以说在这里边就有一个问题了，要么你根据消息判断，要么你重发的时候也要重发，什么呢？也要重发具体的那个可靠性的方法，只不过在这里边你再重发的时候，你判断一下是不是就是在这里边，就是到底是用 confirm 散的，还是用我们的这个可靠性的那个散的？在这里我选择一种。好，我现在用这种叫做 react sand，然后把消息再拿过来。


OK，如果是 react send 会有什么问题？我们点进去看一下，如果是 reset relay send，我只需要在这里点 query 查询我，当然我这个方法可能还没写完，那我们再点进去有 insert 了，肯定有 select by prime key 了，我们来一个 public Int 叫做query，我们就用 message ID 就可以了，对吧？我们就查一下数据库叫做query，你看它这个 Mapper 是怎么去写的？ diss 点Mapper，点 select by primary key，是不是根据 ID 直接给我们返回一个具体的对象？它返回的是一个 broker message，那我们是不是直接可以用它return？这个 broke message？那我们在这里叫做，也叫做 select by message ID 好，就是你自己要写他这个方法就可以了。


然后你回过头来，在我们可靠性投递的时候，就是说在这块时候你第一件事情要先确认一下这条消息到底存不存在吗？你要通过这个 message service 点 select by message ID，先把这个 message ID 先看一下库里有没有对不对？这是你重头，你库里如果返回这个古 rocker message，咱们叫做BM。

好，如果 diff b m 等于那样的话，如果等于空，说明你数据库里没有这个消息，做什么事情？是不是在做映射台？好，然后呢？不管怎么样，就是我做重头肯定再次重发嘛，是不是还是要再次重发？OK，那这个逻辑这样的话才符合我们自己的预期嘛。然后回过头来，我们做完这个事情之后，也就是说我们的定时任务现在一定要做的事情，就是说我们还是要 send 这个relax， send OK，那么接下来这个问题就可以解决了，就是说我们无论是 confirm 还是这个 Relife 这两种消息你肯定都要调这个confirm，然后回SK。


那我们其实就很简单了，我们直接就可以通过这个 message 它的这个类型做一个判断，如果是什么什么样的 message 我就不需要做更新？如果是什么什么样的message，我就强制的要更新。但是小伙伴们，有一点，我这里边只给我传了一个这个 coloration date，还有ACK，还有这个 Cos 错误的时候，我怎么去判断它需不需要做更新？我怎么去区分它是 confirm 消息还是 react 消息？我说其实如果我们能做到，如果当前消息类型，为什么啊？为我们 relax 的消息，我们就去数据库查找 bill 进行更新，对吧？剩下的 config 消息干脆就不需要走。


这句话为什么？因为你本身 confime 消息，你的消息是不落库的，你是不做持久化的。那这个怎么做啊？大家是不是应该能想到就是我们这个 calculation ID，就是我们可以对它做一个拼接嘛？说它到底是什么消息，我是不是知道？那在生成 calculation 它的时候，我们其实可以直接截取出来，在这里我先把它写死，对不对？我先把它写死，它的 type 是什么呢？我就直接先写死，我说直接get， get 2 就直接 get 2，它是一个string，我叫做 message type m e s a g e type，直接我要能找到它，然后去判断if。


如果这个 message type 等于我们 message type 点，我们可靠性的就是 relate 点equals，我们自己传递的这个 message type 的话，我们才去做数据库的更新操作，其他情况不管，对吧？因为其他情况他是什么呀？他是确认消息，他根本消息都不入数据库，那接下来这件事情就简单了，就是我们要在第二个字段里边，我们要通过一个井号的分隔去把消息的类型去传进去，对吧？这是一个井号，那我们来看一看我们在哪里边去发消息的？肯定是在我们的这个 broker implements 里，对吧？其实就找这个客人就可以了，找这客在发客人之前，我们已经对消息的状态对不对？已经都设置了消息的状态，无论是迅速消息，还是说 confime 消息，还是说这个 relax 消息，都会有它了，就是这个 message 里面肯定是有那什么的消息的类型的，那我们直接取出来是吧？然后再生成 calculation date 的时候，我们把它那什么一下就好了，是吧？好，那就是再来一个井号，再来一个百分号 s 就可以了。好，然后把第三个值做一个替换，对不对？第三个值做一个替换，叫 message 点 get message type 搞定，是吧？这就搞定了，这就已经能够实现我们自己的这个可靠性了。


为什么我做了这么这么复杂？这些事情主要就是为了一个什么呀？主要我就是为了，就是当我们只有 relate 消息的时候，我才去更新一下数据库，其他的 confime 我是不更新这个数据库，虽然说你要不这么写，你要不做这件事情也没问题。为什么呢？因为你压根就查不到你是 confime 的消息，它虽然说都有 message ID，但是说它有 message ID 是有 message ID，但是它肯定不落库，对不对？就是做查询的时候干脆就查询不到这个 message ID，因为数据库中没有。


但是为什么一定要这么做？因为每次都多了一次数据库的请求，所以说我们就为了提升我们的这个性能，或者是说减少我们数据库不必要的这个访问，那我们就完全可以加这么一个字段来判断一下分类型。那同理，在我们做消息重试的时候，对吧？我们做的是什么事情？我们做的事情就是重新发一条这个 relax send，只不过在 relax send 的时候我们去判断一下这条消息到底在数据库里有没有，数据库里有的时候我就认为它肯定是重试消息了，我直接调一下重发就好了，没有的话我再去insert。


就这么一个逻辑，很简单，对吧？OK，那回过头来，我们重发消息以后，还有一件事情非常重要，就是你每次重发，是不是你的 try count 都需要去做一个，什么都需要做一个更新，所以说在这里边你肯定得做一个更新的操作。当然这个 service 里边有一个更新方法，我们来看一下这个 service 里面目前还没有更新这个 try count 的这个方法，那我们来看一看这个 map 里面有没有，我们看看 update for try count，看见了就是说你给我一个 message ID，我把它 try count 去做一个更新，这个更新怎么去做？其实你完全可以看一下它的这个mapping，看看怎么去实现的，无非就是加1，我们来看一下对不对？就是我们取到了这个具体它的这个 message ID，然后对 message ID 对应着这条记录里边的 try count，然后对它进行加1，然后更新一下它的更新时间就好了。

OK，这个 SQL 非常简单，所以说既然有这个方法，我在 service 里边可以直接去把这个直接用上 public 叫 y 的，然后叫做update，叫 try cut 所有NT，然后直接就是 dis 点点它，然后传进去就可以了。这个 ID 是外面给我们的，是不是我们直接叫做 broker message ID，这个 time 就我们就 new 一个就可以了，又一个 data 对他好搞定，然后他其实有返回值的话，那你也最好有一个返回值，因此然后我们在最外边，就是在我们刚才这块是不是就可以去使用了？那怎么做？要做更新，每次重发的时候要更新一下，叫做 try count 字段，对吧？这是必须要做的。


update 拆count，然后把 message ID 带过来， message ID 就是他们我 message ID，对吧？既然都用这个麦斯ID，那为什么不生命一个变量呢？要不然每次都开好搞定是不是？OK，那其实呢，我们到现在为止，我们的定时任务重试已经搞定了，这我们的补偿方案已经搞定了，OK，然后我们就差做测试了。

那怎么去做测试呢？其实测试很简单，测试就是说我们自己在新建一个我们的这个 spring boot 工程，然后把我们对应的这个包引进去，然后该配置的配置上，然后再起MQ，然后发消息重试，看看结果就 OK 了。好，那这节课呢？我们先讲到这，下节课我们对重试的逻辑做一个演示，感谢小。

```java
package com.bfxy.rabbit.producer.task;

import com.bfxy.rabbit.producer.broker.RabbitBroker;
import com.bfxy.rabbit.producer.constant.BrokerMessageStatus;
import com.bfxy.rabbit.producer.entity.BrokerMessage;
import com.bfxy.rabbit.producer.service.MessageStoreService;
import com.bfxy.rabbit.task.annotation.ElasticJobConfig;
import com.dangdang.ddframe.job.api.ShardingContext;
import com.dangdang.ddframe.job.api.dataflow.DataflowJob;
import lombok.extern.slf4j.Slf4j;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Component;

import java.util.List;

/**
 * <h1></h1>
 */
@Component
@ElasticJobConfig(
        name = "com.bfxy.rabbit.producer.task.RetryMessageDataflowJob",
        cron = "0/10 * * * * ?",
        description = "可靠性投递消息补偿性任务",
        overwrite = true,
        shardingTotalCount = 1

)
@Slf4j
public class RetryMessageDataflowJob implements DataflowJob<BrokerMessage> {

    @Autowired
    private MessageStoreService messageStoreService;

    @Autowired
    private RabbitBroker rabbitBroker;

    private static final int MAX_RETRY = 3;


    /**
     * 获取待处理数据.
     *
     * @param shardingContext 分片上下文
     * @return 待处理的数据集合
     */
    @Override
    public List<BrokerMessage> fetchData(ShardingContext shardingContext) {
//        messageStoreService
        List<BrokerMessage>  list = messageStoreService.fetchTimeoutMessage4Retry(BrokerMessageStatus.SENDING);
        log.info("-----------------------------@@@@ 抓取数据集合 : {} ---------------------------------", list.size());
        return list;
    }

    /**
     * 处理数据.
     *
     * @param shardingContext 分片上下文
     * @param dataList            待处理数据集合
     */
    @Override
    public void processData(ShardingContext shardingContext, List<BrokerMessage> dataList) {
        dataList.forEach(brokerMessage -> {
            String messageId = brokerMessage.getMessageId();
            if (brokerMessage.getTryCount() >= MAX_RETRY) {
                    this.messageStoreService.failure(messageId);
                    log.warn(" ------消息重试最终失败， 小时自重失败：消息 ID : {}" , messageId);
            } else  {
                // 每次重发的时候要更新一下 tryConut 字段
                this.messageStoreService.updateTryCount(messageId);
                // 重发消息
                this.rabbitBroker.reliantSend(brokerMessage.getMessage());
            }
        });
    }
}
```

```java
/**
 * <h1></h1>
 */
@Service
public class MessageStoreService {

    @Autowired
    private BrokerMessageMapper brokerMessageMapper;

    public BrokerMessage selectByPrimaryKey(String messageId) {
        return this.brokerMessageMapper.selectByPrimaryKey(messageId);
    }

    public int insert(BrokerMessage brokerMessage) {
        return this.brokerMessageMapper.insert(brokerMessage);
    }

    public void success(String messageId) {
        this.brokerMessageMapper.changeBrokerMessageStatus(messageId, BrokerMessageStatus.SEND_OK.getCode(), new Date());
    }


    public void failure(String messageId) {
        this.brokerMessageMapper.changeBrokerMessageStatus(messageId, BrokerMessageStatus.SEND_FAIL.getCode(), new Date());
    }

    public List<BrokerMessage> fetchTimeoutMessage4Retry(BrokerMessageStatus brokerMessageStatus) {
        return this.brokerMessageMapper.queryBrokerMessageStatus4Timeout(brokerMessageStatus.getCode());
    }

    public int updateTryCount(String messageId) {
       return this.brokerMessageMapper.update4TryCount(messageId, new Date());
    }

}
```




