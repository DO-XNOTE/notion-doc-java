---
title: 1-27 【K8S技术落地实战】部署微服务-5
---

# 1-27 【K8S技术落地实战】部署微服务-5

[image](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/c8895aa2-55f3-4cba-86dc-8b101a1fe519/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667CYZECVD%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T225951Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIHm5G57GaSsR1wKvIxTct3iWIrkOXW5S4CrBzrW6NsO0AiB%2Bu3%2BxJmN5IHhnUfcgHwroq5MbvmaUNJqU2YwWzJhcsiqIBAjG%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMFwQtRkpzjAt6rKZ9KtwDDo59Owm0wieq%2FwPMa%2FYGTT1Oq9pPlhxdUrDZ8AnpE2yhb33AXv3pKCbfrZfUAiFBV%2BrtYvqzThPPCdqAMa8jFM8IYWiwmduq0MVouEMmMCXt87XQKpbRYW0eHDc6uESGrB0OT591nxcxm8wN0iCgK5yE90w%2BEH8EbyTH2EtvRULD43N8x%2BcgcEyi6jDscbeCmo6dDKNSuxERIL7brKmLMIjlaIVhhR1vqpvPxb81jqoh0UiiCOFxJXa6a6BEyqWLZAZRq2YFY8Y3lqRFPGe6uIjRzmRHLHluTzaJjJy8NognuA0NmPHbUqZ4gDgPt0skVp%2FRZ7k7ocR33zrQvjuVqmtZG%2FmgDe8HIXhRSkvZF3iKG6bmByOkCqUy8zsJMHE7SW3gsQqPdHKavec4QX6iouINMfwsnjzx9%2FMmVRgDsd9zdOPNHeC4frY%2BnMYok%2BANXsLNulnfEqhAoSy%2BOyyH7gKLPfzejqoJzZzphG0Q8WNIcSqgNF4mmfpcIiknCU2qqN8EQutlKJJX3jlGTcOLogyHzC%2B1sGFUH3k%2FO7gsCl2VMneM05WUZxfCUYqXG4I0J6%2BfMatOdvALIz59v0TRDEs1CeakQnBDUrfoD%2F3cco9hcDxGm4weuvu6LB4wirn%2F0gY6pgHOriQ3GuMYdmj1gdbv16sHgKfQ2qm7fk5jWUxsm3I8C1%2BWraThEQbUOfghgUkR8OD%2B5BqaUXtUcK9Ne5O4tiovDGtvOA%2FxxFzAODiR7RFXphG6FzCImrSklxFkYRLOl%2FRoUpjzsIELP731xcYfp0RV7BHSADPIOFGKp5GshFjeQl%2FRu%2F3Qu2QMSnN3ocbqljIw0iJ8stmoF7b9DcOhTQWeHWWlGt9O&X-Amz-Signature=fc230afdc572f52d636dd274f9491cc314b9e53e7c06b1dbc25dbf41d08baa37&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

[image](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/19d0f7bf-4e0f-4a5d-9c50-e1d0e29bd025/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667CYZECVD%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T225951Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIHm5G57GaSsR1wKvIxTct3iWIrkOXW5S4CrBzrW6NsO0AiB%2Bu3%2BxJmN5IHhnUfcgHwroq5MbvmaUNJqU2YwWzJhcsiqIBAjG%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMFwQtRkpzjAt6rKZ9KtwDDo59Owm0wieq%2FwPMa%2FYGTT1Oq9pPlhxdUrDZ8AnpE2yhb33AXv3pKCbfrZfUAiFBV%2BrtYvqzThPPCdqAMa8jFM8IYWiwmduq0MVouEMmMCXt87XQKpbRYW0eHDc6uESGrB0OT591nxcxm8wN0iCgK5yE90w%2BEH8EbyTH2EtvRULD43N8x%2BcgcEyi6jDscbeCmo6dDKNSuxERIL7brKmLMIjlaIVhhR1vqpvPxb81jqoh0UiiCOFxJXa6a6BEyqWLZAZRq2YFY8Y3lqRFPGe6uIjRzmRHLHluTzaJjJy8NognuA0NmPHbUqZ4gDgPt0skVp%2FRZ7k7ocR33zrQvjuVqmtZG%2FmgDe8HIXhRSkvZF3iKG6bmByOkCqUy8zsJMHE7SW3gsQqPdHKavec4QX6iouINMfwsnjzx9%2FMmVRgDsd9zdOPNHeC4frY%2BnMYok%2BANXsLNulnfEqhAoSy%2BOyyH7gKLPfzejqoJzZzphG0Q8WNIcSqgNF4mmfpcIiknCU2qqN8EQutlKJJX3jlGTcOLogyHzC%2B1sGFUH3k%2FO7gsCl2VMneM05WUZxfCUYqXG4I0J6%2BfMatOdvALIz59v0TRDEs1CeakQnBDUrfoD%2F3cco9hcDxGm4weuvu6LB4wirn%2F0gY6pgHOriQ3GuMYdmj1gdbv16sHgKfQ2qm7fk5jWUxsm3I8C1%2BWraThEQbUOfghgUkR8OD%2B5BqaUXtUcK9Ne5O4tiovDGtvOA%2FxxFzAODiR7RFXphG6FzCImrSklxFkYRLOl%2FRoUpjzsIELP731xcYfp0RV7BHSADPIOFGKp5GshFjeQl%2FRu%2F3Qu2QMSnN3ocbqljIw0iJ8stmoF7b9DcOhTQWeHWWlGt9O&X-Amz-Signature=61df96b515d99a908e21f84b967a1b86cc70de76cc570495f3ea716bcd42e617&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

[image](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/19e2cc15-6eb5-4f50-9a08-8594fb120ddc/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667CYZECVD%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T225951Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIHm5G57GaSsR1wKvIxTct3iWIrkOXW5S4CrBzrW6NsO0AiB%2Bu3%2BxJmN5IHhnUfcgHwroq5MbvmaUNJqU2YwWzJhcsiqIBAjG%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMFwQtRkpzjAt6rKZ9KtwDDo59Owm0wieq%2FwPMa%2FYGTT1Oq9pPlhxdUrDZ8AnpE2yhb33AXv3pKCbfrZfUAiFBV%2BrtYvqzThPPCdqAMa8jFM8IYWiwmduq0MVouEMmMCXt87XQKpbRYW0eHDc6uESGrB0OT591nxcxm8wN0iCgK5yE90w%2BEH8EbyTH2EtvRULD43N8x%2BcgcEyi6jDscbeCmo6dDKNSuxERIL7brKmLMIjlaIVhhR1vqpvPxb81jqoh0UiiCOFxJXa6a6BEyqWLZAZRq2YFY8Y3lqRFPGe6uIjRzmRHLHluTzaJjJy8NognuA0NmPHbUqZ4gDgPt0skVp%2FRZ7k7ocR33zrQvjuVqmtZG%2FmgDe8HIXhRSkvZF3iKG6bmByOkCqUy8zsJMHE7SW3gsQqPdHKavec4QX6iouINMfwsnjzx9%2FMmVRgDsd9zdOPNHeC4frY%2BnMYok%2BANXsLNulnfEqhAoSy%2BOyyH7gKLPfzejqoJzZzphG0Q8WNIcSqgNF4mmfpcIiknCU2qqN8EQutlKJJX3jlGTcOLogyHzC%2B1sGFUH3k%2FO7gsCl2VMneM05WUZxfCUYqXG4I0J6%2BfMatOdvALIz59v0TRDEs1CeakQnBDUrfoD%2F3cco9hcDxGm4weuvu6LB4wirn%2F0gY6pgHOriQ3GuMYdmj1gdbv16sHgKfQ2qm7fk5jWUxsm3I8C1%2BWraThEQbUOfghgUkR8OD%2B5BqaUXtUcK9Ne5O4tiovDGtvOA%2FxxFzAODiR7RFXphG6FzCImrSklxFkYRLOl%2FRoUpjzsIELP731xcYfp0RV7BHSADPIOFGKp5GshFjeQl%2FRu%2F3Qu2QMSnN3ocbqljIw0iJ8stmoF7b9DcOhTQWeHWWlGt9O&X-Amz-Signature=2ff7b0921ae30b0095356e870b337bfc9f450f9c2b6d51eb636695a8f5d5db74&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

[image](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/087415d3-0f9d-46b3-8c52-8c04530a70ea/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667CYZECVD%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T225951Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIHm5G57GaSsR1wKvIxTct3iWIrkOXW5S4CrBzrW6NsO0AiB%2Bu3%2BxJmN5IHhnUfcgHwroq5MbvmaUNJqU2YwWzJhcsiqIBAjG%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMFwQtRkpzjAt6rKZ9KtwDDo59Owm0wieq%2FwPMa%2FYGTT1Oq9pPlhxdUrDZ8AnpE2yhb33AXv3pKCbfrZfUAiFBV%2BrtYvqzThPPCdqAMa8jFM8IYWiwmduq0MVouEMmMCXt87XQKpbRYW0eHDc6uESGrB0OT591nxcxm8wN0iCgK5yE90w%2BEH8EbyTH2EtvRULD43N8x%2BcgcEyi6jDscbeCmo6dDKNSuxERIL7brKmLMIjlaIVhhR1vqpvPxb81jqoh0UiiCOFxJXa6a6BEyqWLZAZRq2YFY8Y3lqRFPGe6uIjRzmRHLHluTzaJjJy8NognuA0NmPHbUqZ4gDgPt0skVp%2FRZ7k7ocR33zrQvjuVqmtZG%2FmgDe8HIXhRSkvZF3iKG6bmByOkCqUy8zsJMHE7SW3gsQqPdHKavec4QX6iouINMfwsnjzx9%2FMmVRgDsd9zdOPNHeC4frY%2BnMYok%2BANXsLNulnfEqhAoSy%2BOyyH7gKLPfzejqoJzZzphG0Q8WNIcSqgNF4mmfpcIiknCU2qqN8EQutlKJJX3jlGTcOLogyHzC%2B1sGFUH3k%2FO7gsCl2VMneM05WUZxfCUYqXG4I0J6%2BfMatOdvALIz59v0TRDEs1CeakQnBDUrfoD%2F3cco9hcDxGm4weuvu6LB4wirn%2F0gY6pgHOriQ3GuMYdmj1gdbv16sHgKfQ2qm7fk5jWUxsm3I8C1%2BWraThEQbUOfghgUkR8OD%2B5BqaUXtUcK9Ne5O4tiovDGtvOA%2FxxFzAODiR7RFXphG6FzCImrSklxFkYRLOl%2FRoUpjzsIELP731xcYfp0RV7BHSADPIOFGKp5GshFjeQl%2FRu%2F3Qu2QMSnN3ocbqljIw0iJ8stmoF7b9DcOhTQWeHWWlGt9O&X-Amz-Signature=75fa5ae994660a96e0feadcee4a7563615142d7256aa5de15f680a24d4c06de3&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

[image](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/1d93af0d-91ac-41d0-a4bd-0f8632303ffa/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667CYZECVD%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T225951Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIHm5G57GaSsR1wKvIxTct3iWIrkOXW5S4CrBzrW6NsO0AiB%2Bu3%2BxJmN5IHhnUfcgHwroq5MbvmaUNJqU2YwWzJhcsiqIBAjG%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMFwQtRkpzjAt6rKZ9KtwDDo59Owm0wieq%2FwPMa%2FYGTT1Oq9pPlhxdUrDZ8AnpE2yhb33AXv3pKCbfrZfUAiFBV%2BrtYvqzThPPCdqAMa8jFM8IYWiwmduq0MVouEMmMCXt87XQKpbRYW0eHDc6uESGrB0OT591nxcxm8wN0iCgK5yE90w%2BEH8EbyTH2EtvRULD43N8x%2BcgcEyi6jDscbeCmo6dDKNSuxERIL7brKmLMIjlaIVhhR1vqpvPxb81jqoh0UiiCOFxJXa6a6BEyqWLZAZRq2YFY8Y3lqRFPGe6uIjRzmRHLHluTzaJjJy8NognuA0NmPHbUqZ4gDgPt0skVp%2FRZ7k7ocR33zrQvjuVqmtZG%2FmgDe8HIXhRSkvZF3iKG6bmByOkCqUy8zsJMHE7SW3gsQqPdHKavec4QX6iouINMfwsnjzx9%2FMmVRgDsd9zdOPNHeC4frY%2BnMYok%2BANXsLNulnfEqhAoSy%2BOyyH7gKLPfzejqoJzZzphG0Q8WNIcSqgNF4mmfpcIiknCU2qqN8EQutlKJJX3jlGTcOLogyHzC%2B1sGFUH3k%2FO7gsCl2VMneM05WUZxfCUYqXG4I0J6%2BfMatOdvALIz59v0TRDEs1CeakQnBDUrfoD%2F3cco9hcDxGm4weuvu6LB4wirn%2F0gY6pgHOriQ3GuMYdmj1gdbv16sHgKfQ2qm7fk5jWUxsm3I8C1%2BWraThEQbUOfghgUkR8OD%2B5BqaUXtUcK9Ne5O4tiovDGtvOA%2FxxFzAODiR7RFXphG6FzCImrSklxFkYRLOl%2FRoUpjzsIELP731xcYfp0RV7BHSADPIOFGKp5GshFjeQl%2FRu%2F3Qu2QMSnN3ocbqljIw0iJ8stmoF7b9DcOhTQWeHWWlGt9O&X-Amz-Signature=3202bbb6e59cfeccc60fdadd335ea566e51cd8992449bee737b47df94cfc5a2e&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)


好，大家看到什么公有云地址出来了，我刚刚做了一个很关键的操作给阿里云充值，因为他在后台其实他会偷偷的帮我建一个 loadbalance 但它要符合 load balance 建立的一个标准，就是有最低资金，因为 load balance 也是后付费，要满足 100 块以上的最低资金，我的刚刚的资金少于 100 块，所以它就戒不成功。所以大家碰到问题，可以点一些这个键，或者找一些常见的超包舒婷的文档。


阿里云上有大量超包舒婷的文档，我刚刚是怎么样调试呢？他在创建楼的 balance 的时候，其实会在这里。服务组件里面有个叫负载均衡组件，我刚刚在负载均衡组件里面来看。我发现负载均衡组件实例里面，原来我有两个实例，但是我人工再去创建一个实例也创建不了，来告知我说钱不够，充值完了以后，直接在这里发现了一个新的实例，就直接创建出来。端口允许的就是 2 万不用再点创建了，因为钱够了，那边的那个命令就能正常执行下去，过一会他就创建出来了。


好，我们再回到我们前面的这个 kubernetes 咨询，也就是说我们刚刚的那个服务后台会自动关联一个阿里云上的实际的 loadbalance 这是它的外网地址。然后我们的服务名称叫 my registry 杠 SVC 看上去都没有问题。打开来看一下，有瑞卡起来了吗？恭喜你起来了。


而且上面注册了个 config server 如预期的它会有两个实例，这两个实例来自于不同的 POD 所以有不同的这个 IP 地址。但端口就是按照规定 config server 应该是20,003，所以你不用去记它，自己自动就注册。如果点这个会有什么结果？这是个内网地址，这个地址只有在 kubernetes 集群里才有效。而我的浏览器并不在 kubernetes 集群里就是打不开的。如果在容器里面就不用再去点它了，因为这是一个内网内部沟通的一种形式。


当你能看到什么，有多少个实例，它的状态如何？好，我们这样的话就很成功的把我们的这个 registry 的友瑞卡给起来了。同时我们把我们两个应用给部署上去了，我们再回过头去看一下这个无状态应用，仔细看一下 config 里面 log 里面什么样的都有两个。 POD 我们进到某一个 POD 里面的一个容器里面，看一下他有很多的输出。而且出错了对不对？出了什么错？我们仔细去看一下他说什么。我要访问一个 config server 叫幺七二点二零点幺五四。但是找不到心跳。所以出错为什么会出这个错大家知道吗？只是因为什么刚刚有 recaserver 是吧？我们在重启和处理一些过程当中，刷新了这个它的 loader balanced IP 地址和它的端口。但是最后它怎么样？ resolving eureka 什么意思？当有日开的服务器真正的把 loader balance 建好以后，从 class ID 转出外网之后，完全成功了。那同样道理，另外一个容器其实也是一样的道理。当中间出现的一些问题以后，最后很成功的进行了注册。


好已经把 my config 注册完了以后，我们再来创建一个下面的应用，就是 my auth 一个来 miles 也是两个实例，作为 authentication 的那个 server 对吧，认证中心 default 然后我们点下一步，选镜像。 am I auth 这个镜像放大，看得更清楚一些。然后下面所有内容都不变，直接点下一步。然后这里面是不是要建服务呢？不需要，因为这是一个内置的应用，也不对外提供服务，所以对外的都走 gateway 好，我们直接再缩小一点，太大了就找不到那个确认了对吧。


好，创建那回去的。咦成功了，我们看看结果怎么样，进到马尔斯里面缩小点才能看下面。买奥斯出错了，为什么呢？他说找不到文件什么之类的出错没关系，我们进到日志里去看一下。好参数不合法， container 跑不起来。参数不合法对吧，就这一报了，我们仔细看一下。


registry VPC 飞扬，mayosslatest我去拉了个什么 latest 有没有？ latest 没有只有 myoss 什么1.0，这个时候它就会有些这个不合理。那如果是说我们正常的一些部署，我们会把当前版本最新的也发一个叫 latest 上去，就是很多不同的应用都会传一个这个我当前版本是多少，然后再打标成 latest 上传一个，防止你要拖 latest 刚刚我就是忘了把版本说清楚，没关系，改，改一改自动就生效，我们看看怎么改。


我们在这里进行一个编辑。 my auth 拉取的时候，好像拉错了我们的 image 我们看看能不能进行直接修改。如果可以修改，我们就修改一下 image 如果不可以，也很容易我们进行一下这个重新创建。这里可以，类型是1.0。好，我们更新一下。所谓更新其实就是应该是一个什么弹性扩缩容的过程，变绿了是不是变绿了？我们点进去看我们不放心。我们点到这个 POD 的容器，在 log 里面去，看起来没起来，先点自动刷新， start application 成功启动。好，我们回到有瑞卡，我们看到了。


起来没有你起来几个实例，fully or service 起来了。两个实例都是 1006 端口不同的 IP 地址，两个不同的容器。一切如预期对吧，我们刚刚什么是一步一坑，带着大家一个排查，一个是什么 service 中间碰到付费问题起不来。另外一个什么我们的这个服务发现之间的网络有问题冲突，这一个是什么？是我们起的时候 image 类型选择好，实际过程当中坑歧是很多的。不要慌。所谓的couplets ，如果你用图形化界面或者你是 coupe control logs 之前学的这些技能完全可以帮助你能够在 


kubernetes 这样一个集群层次就能够展现所有的信息，处理所有的问题，所以并不需要很慌张。
好， my auth 完了以后，我们来个什么 my user ，请 user 也是两个实例，有的底下我们已经吸取教训了，不能乱来，我们要好好的找一个 user 的这个应用，然后要好好的写它的版本号对吧，1.0，其他就不变。点下一步服务，不用创建这个内部应用。


好，我们直接点创建这 deployment 就已经成功了，我们回过去看，是不是有两个对吧，随便点一个进到 log 里面，让它自动刷新。好还在慢慢起。不着急对吧，这个就是它容器的地址，然后这就是它的端口号。好我们把它慢慢起，我们在这里，它又在起了。好，我们有人在这里也刷一刷，看什么时候能刷出来。还在启动是吧，应该是那边先启动这里才能刷出来。好他去找他自己的这个节点的信息，我们不用急的，我们慢慢的 started 就证明成功启动了。


对不对好，我们回过去 eurika 是不是能够刷出来了？ food user service 两个应用和不同 IP 地址同样的端口号已经起来了。好很好。那我们下一步我们下一步再去起几个应用。去起埋 item 用好也起两个，我们那个环境配置有限都起。那么两个可以选个镜像，选个 my item 的镜像好1.0。下一步不用创建什么 service 对吧，都是内部的一些服务。


好嘞，我们再去看一下 my item 的 POD 的容器的 log from pop 自动刷新一下，正在启动是吧？ sprint 图像已经出现，等他 item 提起来是不是拉取还是比较快的？对，因为拉取是什么？是对阿里所以相对比较快上传，虽然你也是在阿里的一台什么我们的云服务器上可能是个服务器，你走的公网地址对不对？给它拉下来跑起来 started 还是蛮快的。


好，我们再来刷新一下是不是 item 也出来了两个容器。很好，我们再做下一个无状态创建 my cut 也是两个实例对吧。下一步选一个什么购物车的 image 就是我们之前做好的上传的点0，然后其他不变。 my cut 也是内部的，所以不用选什么 service 回过来看两个 POD 每个 POD 的容器制看第一个其实也就大概知道啦。


好，正在起一些基本的连数据库的模块忘了点自动刷新了耶，已经起来了，还是蛮快的，是不是越发神速了？ cut 起来了。好的，再去 order 我看看好吧， my old 也给起两个实力，找一个 order 的实例 image 然后 1.0 不用建服务，一路下去创建。好。回到应用列表起来了吗？还在创建中，莫非又出了幺蛾子，刷新一下起来了。好，点进去看看，日志自动刷新。他在慢慢的 loading 一些东西，我往上看看有没有什么 error 似乎没有 error 他在找东西对不对？好应用已经 started 了，是不是？ config auth cut item order user 全都是双实例形式跑起来。


然后 rapid MQ 是单实例也跑着，有人卡也是单实例跑的还缺什么吗？是不是只缺最终对外提供服务的 gateway 了，让 gateway 而引流进来，然后指向不同的比如说 auth cut config item order 然后他们之间再去什么，就通过一些 rabbit MQ ，通过一些这个什么 registry 之间进行沟通，然后再和 my config 这个东西沟通，从而应该是只有 user domain 当前是跟 my config 沟通，然后从而从 git 里面拉一些配置对不对？只有这个 domain 好，那我们就把最后剩余的那个 gateway 就叫 my gate away 。两个实例，我们也当它是什么无状态对吧？相对来说其实它就是一个 S engines 的东西。好去拖，把 gateway 的镜像给找到1.0，这一步是没变化的下一步我们一起去教训了。该见 load balance 就见对不对好怎么建楼的 balance 首先选服务 my gateway service 可以叫什么名字都无所谓。这里选楼的 balance 公网对吧，我们新建一个，该付费就付费了。好，集群模式的 cluster 模式可以跨集群进行 load balance 然后这叫 market way ，这什么无所谓，最关键是什么里面什么端口。


还记得是 20,004 是吧，代码里我们写20,004，然后容器我们也是 20,004 的，这是代码里 20,004 我们希望对外也映射成20,004，后来它就会自动生成一个公网 IP 地址跟这个20,004。好的，我们点创建，这时候还没真创建，只是把配置点完了，我们点真。服务创建完了，我们的应用也部署完了，我们，先看一下这是应用对吧。两个 POD 点任何一个容器里面就有一个容器。好再看日志，我们自动刷新看最新的 discovered client register 然后状态 404 注册成功了，我们来看一下两个容器是不是也出来啦。


platform gateway 两个这是内网地址，真正能够访问的地址在这里，右左边放大服务，也就是 service 也就是什么一个路由展现的形式叫 service 怎么样把路由真正的导流到我们内部的什么 POD 这个容器里面来有两个对外的事情，一个 registry 这个就是什么。我们看 eureka 的图形化界面的这个 gateway 就是我们待会用 postman 来进行实测的，请把此一曲记下来。好复制。我们可以模拟我们用户的 browser 用 postman 然后 call 一些 API 看看能不能 call 通。根据如果有问题，根据报错回过来查看。


postman 我这里有个叫注册，也有个叫登录测试，我们去注册一个我们把 IP 地址替换成当前这个容器的 IP 地址。好。替换好了以后相当于是 gateway 对外的网关地址，就是我们的 service 地址，它会负载均衡到里面某一个台 gateway 然后 gateway 再找到相关的游的 domain 如果它有 auth 的就是 auth domain 把这里既有 authu 的，为什么 head 里面有个 authentication 叫 imock112 好薄蒂里面呢又有飞扬老师的密码，也叫飞扬飞扬。


好不好？我们注册一把，看能不能成功怎么办？成功了对吧，他是先第一次找负载均衡。你先找 service 好，找 service 以后找到那个节点。找那个节点以后他又找那个友瑞卡。有人告诉，到底是哪个节点去 take 你 traffic 然后你还会是吧，用 ribbon 形式决策一下。好像是这个节点更好。那这个节点是 auth auth 验证完了，还又去找尤维卡说。哪个节点来承担 user 的 API 更好？好找这 API user API 靠进去对吧，一路靠跳下来。好。成功了。


成功完了以后，对目看一下，也把这个 UI 换成我们最新的指南。 body 换号以后，pass log in authentication authorizing 都不变。 body body 写错了没关系，先来个错的对不对？ user 是沸扬 body 怎么？发作者不是飞崖，看一下为什么结果艾米亚不正确或者用户名不正确，到底哪个不正确？改一下不就知道了吗？允许好，把这一拿掉再看一下能不能登录成功。


200 登录成功。我的信息都给你们看到了好吧。好，其实没什么信息。好，那我们也就是说模拟我们用户的这个什么阿贾克斯靠已经能成功了。来，我们回过头去看，整个 kubernetes 用了哪些功能？部署了大量的 deployment 里面其实就是 POD 然后我们还有什么使用一些服务的方式？我们没有用高级的 ingress 路由这种方式。因为说我们没有 DNS 买 DNS 所以没有一些很漂亮的 URL 但是我们照样能够对外提供服务的。


那除此以外还有很多很酷炫的功能。我们将在下一节弹性扩缩容给大家看看更加酷炫的那些额外插件库内体词上弹性扩缩容里面， pcf 其实讲的是以图为主，以理论为主，梅瑟斯马拉松是有实战，但没那么精彩，库伯内特斯才是真正能够展现弹琴库索荣根本精髓的内容。大家是不是很期待真正让我们这个应用在我们的这个库目内的集群上面非常弹性自由的发挥起来。


好，这节就到此的结束，希望大家在这一节当中已经学会了所有怎么样用容器来搭建 group quality 之间的网络存储配置，怎么样进行管理，以及怎么样把一个微服务真正的改造成 Doc image 然后发布到我们一个已经准备好的 kubernetes 集群里面。不管是你的 coupe control 命令羊毛文件还是类似于图循环界面的点的方式。


最后以真正以 deployment 和 POD 把应用部署起来，以 service 把我们的什么我们的这个服务提供出来，从而实现我们整个应用能够非常之弹性伸缩的，能够提供外面的 API 响应，甚至于我们能把 engines 服务器也装在我们的 quality 集群上。然后你可以打开页面，滚动我们的轮播盘，访问我们实际的应用，然后真正的进行购物。


好不好？相信大家后面还有更多可以做的东西。基于这个章节，我们可以实战一下，把整个网站完完全全的，包括修改域名，甚至于注册一些 DNS 大家都可以实操。找一个语音平台，不管你是百度、阿里、腾讯或者是自己搭一套基础运营平台，然后在上面把应用完整部署起来。那下一章节的弹性扩缩容力，再跟着大家一起来无限的伸展。好，谢谢大家。


