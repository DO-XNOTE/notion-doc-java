---
title: 3-10 Seata TCC快速落地（下）
---

# 3-10 Seata TCC快速落地（下）

[image](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/58949825-14c7-4016-bf01-5b9ed29a34e3/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662R4AK5CV%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T231412Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIBcghbe3btvB5GGBRdYX9BrdHSMbpjGYLRgNo39NotkZAiB1h%2F76EHf8fqDH8EGeIIRNOyB6I7MS5ux%2FiTIV8wyJ2SqIBAjG%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMnkgMe72vI8sY2OpTKtwDTV1okeXlsxnqdhtM6OaA5qk4ZSff5KGsn6ygvA2ZT0pNVOYsfz9iNcKwXK6KVF0AUWNXbEBaDngL3zZQwkgpQ50Y6v4T27Dh5UHvCbuYt3U1GPTD9ORXi7Ak%2BTI1BZ%2BvJMwDoyi1LEIibYxGfMrx5NS2M5ifbWvKnUz1IgM42Fv6AdPL54gc82FDn%2BW%2FyXAfHDpDJXYCiR3MIsj6e%2FNJ8pvPXgcmAgQ9w0tUhxmD2P6ry0dHwvf87h6TSytJMZpaRX4E6vKxgVve4zyNWzGFjy6mXRLUd0gNV8zGGJGEKm%2FpXWBCTREfjlspfArJyhiyECGVRSwb17yah4CIfZt%2BdmTJ99zfd6EDxiTgKINDLH5EF55cQuS4RKFIMdYW4V%2BvKynRVtUF6SmnGBRODve233mFGorLSwK6dEroqPet0HqW39i%2FsH7M1Ar0yPj6eqoew0UcmwSkq8g9xkROvP%2FWh%2FueiYuQ1nGW%2BZ%2FLbaSCb%2B0CkxTYJpgv5wEeKG8XzcuFjZdnBUHavrqTdg3i7bDrIf8kr0bteWPLRVsRrEXbMhMYAIWDx2mpoeCs%2B75ZU4YjkwgsYQx7IycqyxMvLyXT7SjifLUWJZ%2FQptij8mGiJ7bqOwB3gsTM1EfTG8Ywsbr%2F0gY6pgEt%2FQyaE9zmoAyOmO%2F5olsw%2Fga03Kz6ZCzPHJyX2pvKiWuPhNbtApvQi3kUANU5p2Di1wnkPDUcXYIbE%2BGxF9NktOerVgGEpNlhssnfVMblvGAhAaGSFPj5y4mANcIFFYrsUfQnSZVJhF4LCzZvaE73TdTEbJNsSbcAcVNMJZVSLqCEB4Ijawg4TGv4U3CNUwaF44KEKOfuABLijGNFx%2Bl764gn%2B630&X-Amz-Signature=9d07ce7e170fea8e76944a61d70560f81236b20d63d07e1160e7e859687b7b91&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

[image](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/a7c83a82-803c-4847-bde8-7a6a36ebb2c0/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662R4AK5CV%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T231412Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIBcghbe3btvB5GGBRdYX9BrdHSMbpjGYLRgNo39NotkZAiB1h%2F76EHf8fqDH8EGeIIRNOyB6I7MS5ux%2FiTIV8wyJ2SqIBAjG%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMnkgMe72vI8sY2OpTKtwDTV1okeXlsxnqdhtM6OaA5qk4ZSff5KGsn6ygvA2ZT0pNVOYsfz9iNcKwXK6KVF0AUWNXbEBaDngL3zZQwkgpQ50Y6v4T27Dh5UHvCbuYt3U1GPTD9ORXi7Ak%2BTI1BZ%2BvJMwDoyi1LEIibYxGfMrx5NS2M5ifbWvKnUz1IgM42Fv6AdPL54gc82FDn%2BW%2FyXAfHDpDJXYCiR3MIsj6e%2FNJ8pvPXgcmAgQ9w0tUhxmD2P6ry0dHwvf87h6TSytJMZpaRX4E6vKxgVve4zyNWzGFjy6mXRLUd0gNV8zGGJGEKm%2FpXWBCTREfjlspfArJyhiyECGVRSwb17yah4CIfZt%2BdmTJ99zfd6EDxiTgKINDLH5EF55cQuS4RKFIMdYW4V%2BvKynRVtUF6SmnGBRODve233mFGorLSwK6dEroqPet0HqW39i%2FsH7M1Ar0yPj6eqoew0UcmwSkq8g9xkROvP%2FWh%2FueiYuQ1nGW%2BZ%2FLbaSCb%2B0CkxTYJpgv5wEeKG8XzcuFjZdnBUHavrqTdg3i7bDrIf8kr0bteWPLRVsRrEXbMhMYAIWDx2mpoeCs%2B75ZU4YjkwgsYQx7IycqyxMvLyXT7SjifLUWJZ%2FQptij8mGiJ7bqOwB3gsTM1EfTG8Ywsbr%2F0gY6pgEt%2FQyaE9zmoAyOmO%2F5olsw%2Fga03Kz6ZCzPHJyX2pvKiWuPhNbtApvQi3kUANU5p2Di1wnkPDUcXYIbE%2BGxF9NktOerVgGEpNlhssnfVMblvGAhAaGSFPj5y4mANcIFFYrsUfQnSZVJhF4LCzZvaE73TdTEbJNsSbcAcVNMJZVSLqCEB4Ijawg4TGv4U3CNUwaF44KEKOfuABLijGNFx%2Bl764gn%2B630&X-Amz-Signature=1448f584afb800e79594702214722421f12a3ed560f26f57ccbc690769abfe7c&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

[image](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/ed1b482a-93ba-47dc-9e1f-9064f8747736/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662R4AK5CV%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T231412Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIBcghbe3btvB5GGBRdYX9BrdHSMbpjGYLRgNo39NotkZAiB1h%2F76EHf8fqDH8EGeIIRNOyB6I7MS5ux%2FiTIV8wyJ2SqIBAjG%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMnkgMe72vI8sY2OpTKtwDTV1okeXlsxnqdhtM6OaA5qk4ZSff5KGsn6ygvA2ZT0pNVOYsfz9iNcKwXK6KVF0AUWNXbEBaDngL3zZQwkgpQ50Y6v4T27Dh5UHvCbuYt3U1GPTD9ORXi7Ak%2BTI1BZ%2BvJMwDoyi1LEIibYxGfMrx5NS2M5ifbWvKnUz1IgM42Fv6AdPL54gc82FDn%2BW%2FyXAfHDpDJXYCiR3MIsj6e%2FNJ8pvPXgcmAgQ9w0tUhxmD2P6ry0dHwvf87h6TSytJMZpaRX4E6vKxgVve4zyNWzGFjy6mXRLUd0gNV8zGGJGEKm%2FpXWBCTREfjlspfArJyhiyECGVRSwb17yah4CIfZt%2BdmTJ99zfd6EDxiTgKINDLH5EF55cQuS4RKFIMdYW4V%2BvKynRVtUF6SmnGBRODve233mFGorLSwK6dEroqPet0HqW39i%2FsH7M1Ar0yPj6eqoew0UcmwSkq8g9xkROvP%2FWh%2FueiYuQ1nGW%2BZ%2FLbaSCb%2B0CkxTYJpgv5wEeKG8XzcuFjZdnBUHavrqTdg3i7bDrIf8kr0bteWPLRVsRrEXbMhMYAIWDx2mpoeCs%2B75ZU4YjkwgsYQx7IycqyxMvLyXT7SjifLUWJZ%2FQptij8mGiJ7bqOwB3gsTM1EfTG8Ywsbr%2F0gY6pgEt%2FQyaE9zmoAyOmO%2F5olsw%2Fga03Kz6ZCzPHJyX2pvKiWuPhNbtApvQi3kUANU5p2Di1wnkPDUcXYIbE%2BGxF9NktOerVgGEpNlhssnfVMblvGAhAaGSFPj5y4mANcIFFYrsUfQnSZVJhF4LCzZvaE73TdTEbJNsSbcAcVNMJZVSLqCEB4Ijawg4TGv4U3CNUwaF44KEKOfuABLijGNFx%2Bl764gn%2B630&X-Amz-Signature=299e3c66fe92435c75b9e2e0e3522e560455e646407cfd654762f4764119e1ae&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

咱们这个分布式事务改造完 restroom service，这里只算是完成了大概 2/ 3。那紧接着我这里要对咱的 employee service 也做一个改造。好，我把这个改造把它放在哪里？我放在这个 employee fan 里面。OK， fan 方法里，我这里另起炉灶 copy 前面的这个 release 方法，给它 copy 一个新的小方法，然后这里 post mapping，我把它添加成咱刚才创建好的 release TCC。OK，与此同时它的这个方法名我也把它写成 release t c c。好，那这样的话份方法就已经改造完成了。


那接下来我们要在这个 employee service 里做一个小的改动，让你当前的服务可以调用我们的分方法去触发一个分布式的事务。咱接下来打开这个 employee service，定位到这个 restore toilet，在这个方法的内容里，我们把这一句给它换掉，同学们看这一句release，OK，在 release 这里我们把它替换成谁呢？替换成 restroom service。咱刚才添加的这个 release TCC 对应的参数依然是record，点 get resource ID。


好嘞，那天衣无缝剩下的最后一个地方就是我们要给它添加一个 global transaction 注解，开启全局事务，在一个全局事务它发生的起点，我们把这个注解给它给添加进去，那给它随便起一个名字就叫 Tolly release 好了，然后 rollback for 碰到什么问题？ rollback exception，OK，好嘞，那看起来咱这个服务已经启动改造完成了，接下来我们直接把它跑起来，看一下我们这个 employee service，非常牛逼的双刀流。


这个占坑方法使用的是 at 方案，释放坑位方法使用的是 TCC 方案，双键合闭。我们把这个应用 employee application 给它跑起来，直接用 ROM 的模式跑就可以了，不用 debug 的模式。OK，稍等片刻，看这边启动成功了之后。

好嘞，我们首先第一步把这些所有的日志该清的给它清掉，这样的话比较方便观察我们接下来的这些调用情况。然后再看一下我当前的坑位， toilet clean 并且available，而且没有被预定好，非常完美。那我们的 employee activity 这里我看一下，好，也都已经是没有当前生效的activity。那咱紧接着直接调出postman，发起一个蹲空调用鞋。OK，蹲空调用成功。


我们看一下，这是咱前面改造的 at 方案，同学们可以看到 resume service 这里 resume application，你看这是 at 方案的 lock commit result face to commit it，这里通篇没有 TCC 三个字，所以它是这个 at 方案。好，我们接下来把这个日志清空。


好嘞，我们启动完成之后，接下来就走到 postman 里，我们把这个 activity ID 从咱刚才调用的蹲坑操作里 46 copy 过来，填到这个起价回工的这个 API 调用，也就是咱刚才的 release TCC。好，点击完之后，我这边直接点击发送。OK，看到这里已经成功返回了，我们接下来去看一下log，同学们看 log 有什么不一样？咱 application log 我们先不管它 application log 不管我们点击到这个 restroom service 这边log，好，同学们，看到 log 的最后两行，这里 phase two committed 不足为奇，但是我们移到前一行看下 TCC results commit，这里就跟 at 不一样，说明它这边执行的是谁。


TCC 的二阶段提交协议，我们去纵观一下整个log，第一行 try release， TCC 进到了踹方法对不对？我们接着往下看，这是 RM 的本地提交， branch 的本地提交好，没问题。走到这里执行到了谁 confirm release 方法OK，那再往下。好，最后他这边宣告 TCC 的二阶段提交完成，这就是整个 TCC 的一个业务流程。


那接下来我们看一下这个数据库当中这个 toilet 的状态，刷新了一下物归原主， clean 1 available 1 reservely OK，没有任何问题。那接下来同学们，我们来试验一个异常的case，咱先去做点坏事，蹲一个坑，蹲完坑再做坏事。好，这里蹲坑完了，对吧？我们走到数据库当中，咱故意把这个蹲坑的操作改一下，去找到最后一条蹲坑记录，你看它这个蹲坑记录的 resource ID 是咱的 toilet ID，对不对？它这里指定的是1，我们把它改一下好不好？咱使点坏，我把它改成 100500 罗汉好了，改成500，然后提交好它的 ID 是47，对吧？我接下来紧接着去调用 47 的起价回工，看一下它会报什么错。在这个看它报错之前，咱先把这个 log 给它清空一下。好，我们点击发送。


等等，点击之前查看一下数据库，看一下我们 tool 的状态。同学们看 clean 是0， available 是0，说明当前已经有人在这里面蹲坑了，对不对？我们回到这个调用，走，发起。OK，看到它这里报了一个异常，我们来到这个 employee service 这里，看一下它这异常报的是什么呀？走到上面，他报的是 tolly not found。谁报的？诶，我们看这是这个 phone 接口报的，也就是说 restroom 这里肯定发生了点事儿。果不其然，你看最终的结果是 branch road bag。那我们这里走到上面去，观察一下它的日志。执行第一步，执行它的 try 方法没错，然后接下来在这里有异常了，对不对？ try 方法爆出了一个 cannot release the restroom，为什么 toilet not found？然后我们穿越一连串的 error 走到最下面，我们看这里，这里 RM 提交失败，然后 branch roll backing，紧接着就走到了咱的这个 cancel release TCC 方法，它执行了这个失败的逻辑，然后到最后 face to road back， OK 我们再来看一下它的数据层面，这个 toilet 刷新一下。


诶，依然这里看到吗？它的这个值依然是我们执行 try 方法之前的值，也就是说我最终的业务回滚实际上是成功的。OK，那这里就是我们 TCC 的三步走的策略方针那不过老师这边诶，也要跟同学们提几个醒。第一个，咱这现在进入了分布式事务的阶段，这些难度、组件间的复杂度，还有你集成的中间件数量肯定和之前相比会有大幅的增长。那么同学们如果有些许的配置失误，或者是跟老师这个样例不一致的地方，或者说你用了不同版本的 Theta 中间页等等，都有可能导致项目启动不起来，这个情况下怎么办？很多同学就是直接到百度搜索对不对？其实际上阿里这家公司你在百度搜索可能搜不到答案，因为一方面它中间件更新的速度非常快，第二方面它不中文档，你很难搜到什么之类的文档。


阿里这家公司开发这些中间件开源项目，他不太讲武德，他不给我们提供这些文档，总是为难我们这些 19 岁的老同志，非常的不讲武。德，那我们这里怎么办？老同志们，老师送大家四个字，好，子伟志，同学们，这里找不到答案，只能自己去动手debug。这个也是锻炼自己源码阅读能力，对自己这个框架理解能力都会更加深一层。那很多时候，对于这些开源项目来说，你启动失败或者运行期抛出一些异常，你实际上根据它的这些 error message，你可以很容易地定位到那个点，答一行断点，然后去跟一下，你就能细心地发现这里边的蛛丝马迹，最终把这个问题解决掉。那这是跟同学们讲的第一点。


第2点，咱在 Theta 集成这里，实际上我这边 demo 的只是一个非常非常简单的案例。咱在实际项目当中你用到TCC，你其实在这个业务层面要对业务的 try 阶段、 confirm 阶段，还有 cancel 界面做更加细致的一个划分。你在 try 阶段你去锁定资源，可不是打一个标这么简单。通常来讲我们是要创建一些独立的业务表，你在业务表里面去加相应的锁记录等等。那因此你要是把这个 TCC 用在金融级项目方上面，你会发现实际上对你的开发成本是一个巨大的提升，你的开发成本基本上可以说它是要大于 double 的，也就是 2 倍的开发成本。所以这就是为什么我不太建议就是一些技术实力比较薄弱的小厂，或者一些小项目，你去上 TCC 这种重量级的方案，那为了这些许的性能提升，但是大大增加了你的维护成本，你的开发成本，这是十分不值得的。


即使要上，你上 at 方案绰绰有余，除非你是那种很大规模，对一些性能要求有极致的公司，你觉得 AD 方案这里并不能满足你的性能需求。你上TCC，或者说你想在这个事物控制方面，你让自己的把控度更强，你想通过业务层面更细粒度地控制你各种事物的提交回滚，在这个过程当中再做出一些业务判断，业务操作，那这里 TCC 才是一个相对来说比较政治正确的选择。OK，那这是跟同学们分享的这几个点，那咱这一节的内容就先到这里结束了，同学们拿到 TCC 的再去把玩消化，把这个视频反复的看两遍，去理解一下其中每一个配置，它的用途要加在哪里。那我们在下一节当中跟同学们再去过一下咱 TCC 这个方案当中的几个坑，这些坑到底它有多坑？同学们，我们下一小节再跟大家揭晓。好，同学们，我们下一小节再见。


