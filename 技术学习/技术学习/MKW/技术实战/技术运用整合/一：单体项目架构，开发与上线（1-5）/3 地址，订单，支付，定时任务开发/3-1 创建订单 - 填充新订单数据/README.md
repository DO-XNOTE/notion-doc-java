---
title: 3-1 创建订单 - 填充新订单数据
---

# 3-1 创建订单 - 填充新订单数据

[image](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/48f117b5-8be1-4b7e-8181-01e9a5a06b5d/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XBO7TLNQ%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T224703Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIEGS%2Fuc6VX9DfyBW4z7DungtCpFUlqiSP83I7MHSM3omAiEA44o%2BlV%2FGJMel7rN5%2BmRImPV0VMdfh4%2BU9Nrj9wLlB%2B8qiAQIxv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDD2bMxHjSetPHCYlpCrcA5GnIX8ycCbbuEqSlZvsSOf%2Fat01dPxYY4WszhHgyuBx1GuWPAezGOMXA96sz%2FMO1SMGjsaoPOezF0nGbaRxH3QGFPTHSI8NbIZ57XD77uVnWlz8ojY4Zd%2BAfpshLSb4qykIDmJXHyE38nTL20MD1pV8eDE%2B2mpE1e%2F2KnXgORdIaTjiQaLNLg0id2JB3Eh5RU5Lp1lsbaqvhFeDaQwsq%2BGoCRCHdxjpcGXo9moO5Y2%2BbMpkFoz%2BMkizdB9GCiLhVSqeMj1lUW1UFO1vEcludLNjHiSeOL6jrQrSk8YHzSNAJBlePH1SHm0dHv%2BueAKEftXHMBDdw%2BuOTmm7t0kQ%2BIkl5UB77R9jL%2FlZIq0yc0fVI7iGKnx3%2BMbN0omB%2B9ZNT2dikgO9jD%2FInjs3xg2xv14Ln5DvCHP6JDQov4XEN8yfg4%2B%2FMYC%2F29CW6x%2FlQ53J%2FAF3uz1%2FMkSX1NjbwdEYidkxWRP1q7FeC7wZIHrWt8btHetjTj8iHhSivqBG5LKa402l7FbuxWPczhmkK0HMR3CjnH%2BPxY1BfZkL09uUtNskIgTIv23%2FU6D2cA1TLtLOEkXczF3U6BbAJpOdH4BTPQ9USVoMFkL7QUomZdY9I5%2BpG7sqdPkd1jJ38y0NMNu3%2F9IGOqUBXHIevJfDDVII6wIDhxNw2jKP2GVgrxWuKaKk4SpsabMTBz5Kl2nDQtCWoowoLmOcQLFqnZCSa1z7wbuRLYYAOQ1Az%2B%2FC8%2BqPxqeC28pqjfQ8YSeFi4OtMRaRJKAQ5eFvQQU3K6sQb%2BaWND%2Fn7Omygr0oXSWYP4D2L%2BSQotrsDe2aSAn3DSi3hm9TZ%2BqVOBZK%2BlghtxBdT%2BjpHM5N4XliSLkUTA2r&X-Amz-Signature=9e962f37ba087caa7056bf6697ee7af70bb983228cac73b00855d5a64a3464c2&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

现在我们很戳了，就可以获得到从前端提交过来的相应的参数。提交过来之后有一个验证，我们是必须要去判断的。也就是 b o 里面我们可以获得的一个支付方式就是 pay method。在这里其实我们必须要去判断一下，如果你不是微信，也不是支付宝，我们肯定要去报一个错的对吧。 return 一个 m 角色results，点 error message 说一下，会说我们支付方式不支持，可以这样子去写吧。


在这里面判断我们会使用到枚举枚举，我预期也已经是创建了，因为它比较简单。

[image](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/d25f32e1-7d79-4f80-aa82-c8fef2fe06e4/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XBO7TLNQ%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T224703Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIEGS%2Fuc6VX9DfyBW4z7DungtCpFUlqiSP83I7MHSM3omAiEA44o%2BlV%2FGJMel7rN5%2BmRImPV0VMdfh4%2BU9Nrj9wLlB%2B8qiAQIxv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDD2bMxHjSetPHCYlpCrcA5GnIX8ycCbbuEqSlZvsSOf%2Fat01dPxYY4WszhHgyuBx1GuWPAezGOMXA96sz%2FMO1SMGjsaoPOezF0nGbaRxH3QGFPTHSI8NbIZ57XD77uVnWlz8ojY4Zd%2BAfpshLSb4qykIDmJXHyE38nTL20MD1pV8eDE%2B2mpE1e%2F2KnXgORdIaTjiQaLNLg0id2JB3Eh5RU5Lp1lsbaqvhFeDaQwsq%2BGoCRCHdxjpcGXo9moO5Y2%2BbMpkFoz%2BMkizdB9GCiLhVSqeMj1lUW1UFO1vEcludLNjHiSeOL6jrQrSk8YHzSNAJBlePH1SHm0dHv%2BueAKEftXHMBDdw%2BuOTmm7t0kQ%2BIkl5UB77R9jL%2FlZIq0yc0fVI7iGKnx3%2BMbN0omB%2B9ZNT2dikgO9jD%2FInjs3xg2xv14Ln5DvCHP6JDQov4XEN8yfg4%2B%2FMYC%2F29CW6x%2FlQ53J%2FAF3uz1%2FMkSX1NjbwdEYidkxWRP1q7FeC7wZIHrWt8btHetjTj8iHhSivqBG5LKa402l7FbuxWPczhmkK0HMR3CjnH%2BPxY1BfZkL09uUtNskIgTIv23%2FU6D2cA1TLtLOEkXczF3U6BbAJpOdH4BTPQ9USVoMFkL7QUomZdY9I5%2BpG7sqdPkd1jJ38y0NMNu3%2F9IGOqUBXHIevJfDDVII6wIDhxNw2jKP2GVgrxWuKaKk4SpsabMTBz5Kl2nDQtCWoowoLmOcQLFqnZCSa1z7wbuRLYYAOQ1Az%2B%2FC8%2BqPxqeC28pqjfQ8YSeFi4OtMRaRJKAQ5eFvQQU3K6sQb%2BaWND%2Fn7Omygr0oXSWYP4D2L%2BSQotrsDe2aSAn3DSi3hm9TZ%2BqVOBZK%2BlghtxBdT%2BjpHM5N4XliSLkUTA2r&X-Amz-Signature=3e9bfc048d49b5c728f54b3fa8559cd106b9cb69738f5f554d79546c8710dbb2&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

它其实就是两个值， pay method 双击来看一下，一个是1，一个是21，对应是微信， 2 对应是支付宝。前后端所对应的值也都是一模一样的。在这里我们就可以直接去写一下 pay method，点微信点 type 是不等于微信，并且它也不等于支付宝，我们就可以报错了，这是阿里配OK，这个错误是必须要去加上的。


随后我们就可以去进行我们的主业务。首先第一个是创建订单，我们是要写到一个 service 里面去的，我们来写一下service，现在其实我们也并没有，所以我们也要去创建一个service。随便挑一个轮播图的写一个 order service，它的实现我们也拷贝一份。

好OK。在这里面我们要去修改相应的代码，首先要去实现的接口改成 order service。在这里会有一个map，我们也使用 o 的map，OK，这是一个通用map，在这里面我们会涉及到一个方法，这个方法我们直接去改掉，主要就是用于去创建order。创建一个订单传入的参数其实就是从我们 Ctrl 里面拿到的 summit order。 Bo 把 Bo 业务对象我们传递到 service 里面来就行了。返回我们在这里直接先写一个 boy 的，因为我们其实我们是有相应的内容要返回的。后面我们可以再去加写个注释，这是用于创建订单相关信息。


好，随后我们在这里把这个方法完善一下，注意应该是一个request。好。OK，基本的 service 我们就框子写好了，

[image](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/5ab4dfa0-fd15-482f-9f03-101fab6af750/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XBO7TLNQ%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T224703Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIEGS%2Fuc6VX9DfyBW4z7DungtCpFUlqiSP83I7MHSM3omAiEA44o%2BlV%2FGJMel7rN5%2BmRImPV0VMdfh4%2BU9Nrj9wLlB%2B8qiAQIxv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDD2bMxHjSetPHCYlpCrcA5GnIX8ycCbbuEqSlZvsSOf%2Fat01dPxYY4WszhHgyuBx1GuWPAezGOMXA96sz%2FMO1SMGjsaoPOezF0nGbaRxH3QGFPTHSI8NbIZ57XD77uVnWlz8ojY4Zd%2BAfpshLSb4qykIDmJXHyE38nTL20MD1pV8eDE%2B2mpE1e%2F2KnXgORdIaTjiQaLNLg0id2JB3Eh5RU5Lp1lsbaqvhFeDaQwsq%2BGoCRCHdxjpcGXo9moO5Y2%2BbMpkFoz%2BMkizdB9GCiLhVSqeMj1lUW1UFO1vEcludLNjHiSeOL6jrQrSk8YHzSNAJBlePH1SHm0dHv%2BueAKEftXHMBDdw%2BuOTmm7t0kQ%2BIkl5UB77R9jL%2FlZIq0yc0fVI7iGKnx3%2BMbN0omB%2B9ZNT2dikgO9jD%2FInjs3xg2xv14Ln5DvCHP6JDQov4XEN8yfg4%2B%2FMYC%2F29CW6x%2FlQ53J%2FAF3uz1%2FMkSX1NjbwdEYidkxWRP1q7FeC7wZIHrWt8btHetjTj8iHhSivqBG5LKa402l7FbuxWPczhmkK0HMR3CjnH%2BPxY1BfZkL09uUtNskIgTIv23%2FU6D2cA1TLtLOEkXczF3U6BbAJpOdH4BTPQ9USVoMFkL7QUomZdY9I5%2BpG7sqdPkd1jJ38y0NMNu3%2F9IGOqUBXHIevJfDDVII6wIDhxNw2jKP2GVgrxWuKaKk4SpsabMTBz5Kl2nDQtCWoowoLmOcQLFqnZCSa1z7wbuRLYYAOQ1Az%2B%2FC8%2BqPxqeC28pqjfQ8YSeFi4OtMRaRJKAQ5eFvQQU3K6sQb%2BaWND%2Fn7Omygr0oXSWYP4D2L%2BSQotrsDe2aSAn3DSi3hm9TZ%2BqVOBZK%2BlghtxBdT%2BjpHM5N4XliSLkUTA2r&X-Amz-Signature=3f78791cdc995cf3bfbb1357c7ef6568d67b03542f446b087d11a3284fed28ab&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

[image](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/c19f8370-b2ab-4bc9-8ad0-f250db9054c2/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XBO7TLNQ%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T224703Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIEGS%2Fuc6VX9DfyBW4z7DungtCpFUlqiSP83I7MHSM3omAiEA44o%2BlV%2FGJMel7rN5%2BmRImPV0VMdfh4%2BU9Nrj9wLlB%2B8qiAQIxv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDD2bMxHjSetPHCYlpCrcA5GnIX8ycCbbuEqSlZvsSOf%2Fat01dPxYY4WszhHgyuBx1GuWPAezGOMXA96sz%2FMO1SMGjsaoPOezF0nGbaRxH3QGFPTHSI8NbIZ57XD77uVnWlz8ojY4Zd%2BAfpshLSb4qykIDmJXHyE38nTL20MD1pV8eDE%2B2mpE1e%2F2KnXgORdIaTjiQaLNLg0id2JB3Eh5RU5Lp1lsbaqvhFeDaQwsq%2BGoCRCHdxjpcGXo9moO5Y2%2BbMpkFoz%2BMkizdB9GCiLhVSqeMj1lUW1UFO1vEcludLNjHiSeOL6jrQrSk8YHzSNAJBlePH1SHm0dHv%2BueAKEftXHMBDdw%2BuOTmm7t0kQ%2BIkl5UB77R9jL%2FlZIq0yc0fVI7iGKnx3%2BMbN0omB%2B9ZNT2dikgO9jD%2FInjs3xg2xv14Ln5DvCHP6JDQov4XEN8yfg4%2B%2FMYC%2F29CW6x%2FlQ53J%2FAF3uz1%2FMkSX1NjbwdEYidkxWRP1q7FeC7wZIHrWt8btHetjTj8iHhSivqBG5LKa402l7FbuxWPczhmkK0HMR3CjnH%2BPxY1BfZkL09uUtNskIgTIv23%2FU6D2cA1TLtLOEkXczF3U6BbAJpOdH4BTPQ9USVoMFkL7QUomZdY9I5%2BpG7sqdPkd1jJ38y0NMNu3%2F9IGOqUBXHIevJfDDVII6wIDhxNw2jKP2GVgrxWuKaKk4SpsabMTBz5Kl2nDQtCWoowoLmOcQLFqnZCSa1z7wbuRLYYAOQ1Az%2B%2FC8%2BqPxqeC28pqjfQ8YSeFi4OtMRaRJKAQ5eFvQQU3K6sQb%2BaWND%2Fn7Omygr0oXSWYP4D2L%2BSQotrsDe2aSAn3DSi3hm9TZ%2BqVOBZK%2BlghtxBdT%2BjpHM5N4XliSLkUTA2r&X-Amz-Signature=5fb93b95a0a69fd818225d9ce5142629f682b326903d960b87273bc1e6941e71&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

这里面具体要去实现的一些内容我们也都要去写。首先第一步我们先把 Bo 里面的信息我们都全部拿出来，定义在外面。第一个是 user ID，取，获取一下。第二个看一下有一个 address ID 也拿出来，好。第三个是get，有一个 item s p c， i d s，我们也要去拿一下，这是规格拼接的 i d s，好。再下一个是 get a method，就是支付方式，好。再来一个，这是一个 in 字形，所以我们要写一下。下一个有一个 get left message，这是用户的备注，拷贝过来好，OK。


这里面所涉及到的五项内容都已经是有了，但是还有一个我们的邮费，其实在我们的订单表里面，我们在之前提到了一个邮费的一个情况，关于邮费，其实在这里会有一个邮费，虽然我们所有的邮费都是0，都是包邮的。但是其实在我们的一个业务里面，其实也应该要把邮费给涉及一下。所以在我们可以写一下我们来一个， Int 邮费，就是 post amount 设置为0，包邮费用设置为0。

[image](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/92b88aec-94d9-4045-bf10-e7475af2f89d/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XBO7TLNQ%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T224703Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIEGS%2Fuc6VX9DfyBW4z7DungtCpFUlqiSP83I7MHSM3omAiEA44o%2BlV%2FGJMel7rN5%2BmRImPV0VMdfh4%2BU9Nrj9wLlB%2B8qiAQIxv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDD2bMxHjSetPHCYlpCrcA5GnIX8ycCbbuEqSlZvsSOf%2Fat01dPxYY4WszhHgyuBx1GuWPAezGOMXA96sz%2FMO1SMGjsaoPOezF0nGbaRxH3QGFPTHSI8NbIZ57XD77uVnWlz8ojY4Zd%2BAfpshLSb4qykIDmJXHyE38nTL20MD1pV8eDE%2B2mpE1e%2F2KnXgORdIaTjiQaLNLg0id2JB3Eh5RU5Lp1lsbaqvhFeDaQwsq%2BGoCRCHdxjpcGXo9moO5Y2%2BbMpkFoz%2BMkizdB9GCiLhVSqeMj1lUW1UFO1vEcludLNjHiSeOL6jrQrSk8YHzSNAJBlePH1SHm0dHv%2BueAKEftXHMBDdw%2BuOTmm7t0kQ%2BIkl5UB77R9jL%2FlZIq0yc0fVI7iGKnx3%2BMbN0omB%2B9ZNT2dikgO9jD%2FInjs3xg2xv14Ln5DvCHP6JDQov4XEN8yfg4%2B%2FMYC%2F29CW6x%2FlQ53J%2FAF3uz1%2FMkSX1NjbwdEYidkxWRP1q7FeC7wZIHrWt8btHetjTj8iHhSivqBG5LKa402l7FbuxWPczhmkK0HMR3CjnH%2BPxY1BfZkL09uUtNskIgTIv23%2FU6D2cA1TLtLOEkXczF3U6BbAJpOdH4BTPQ9USVoMFkL7QUomZdY9I5%2BpG7sqdPkd1jJ38y0NMNu3%2F9IGOqUBXHIevJfDDVII6wIDhxNw2jKP2GVgrxWuKaKk4SpsabMTBz5Kl2nDQtCWoowoLmOcQLFqnZCSa1z7wbuRLYYAOQ1Az%2B%2FC8%2BqPxqeC28pqjfQ8YSeFi4OtMRaRJKAQ5eFvQQU3K6sQb%2BaWND%2Fn7Omygr0oXSWYP4D2L%2BSQotrsDe2aSAn3DSi3hm9TZ%2BqVOBZK%2BlghtxBdT%2BjpHM5N4XliSLkUTA2r&X-Amz-Signature=6350adaa041923d8f27d9c78a65105801c9a742a89c8f82e8d5a9ec1a840960a&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

好，OK，基本的这些参数我们都给它复制到了一个字段了，在下方下面我们要去使用，就没有必要通过 Bo 一个去 get 好。


首先第一个，现在其实我们要去往相应的订单表里面去插入数据了。

[image](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/d76f5692-4bd8-4a21-b115-4fda5e91256d/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XBO7TLNQ%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T224703Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIEGS%2Fuc6VX9DfyBW4z7DungtCpFUlqiSP83I7MHSM3omAiEA44o%2BlV%2FGJMel7rN5%2BmRImPV0VMdfh4%2BU9Nrj9wLlB%2B8qiAQIxv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDD2bMxHjSetPHCYlpCrcA5GnIX8ycCbbuEqSlZvsSOf%2Fat01dPxYY4WszhHgyuBx1GuWPAezGOMXA96sz%2FMO1SMGjsaoPOezF0nGbaRxH3QGFPTHSI8NbIZ57XD77uVnWlz8ojY4Zd%2BAfpshLSb4qykIDmJXHyE38nTL20MD1pV8eDE%2B2mpE1e%2F2KnXgORdIaTjiQaLNLg0id2JB3Eh5RU5Lp1lsbaqvhFeDaQwsq%2BGoCRCHdxjpcGXo9moO5Y2%2BbMpkFoz%2BMkizdB9GCiLhVSqeMj1lUW1UFO1vEcludLNjHiSeOL6jrQrSk8YHzSNAJBlePH1SHm0dHv%2BueAKEftXHMBDdw%2BuOTmm7t0kQ%2BIkl5UB77R9jL%2FlZIq0yc0fVI7iGKnx3%2BMbN0omB%2B9ZNT2dikgO9jD%2FInjs3xg2xv14Ln5DvCHP6JDQov4XEN8yfg4%2B%2FMYC%2F29CW6x%2FlQ53J%2FAF3uz1%2FMkSX1NjbwdEYidkxWRP1q7FeC7wZIHrWt8btHetjTj8iHhSivqBG5LKa402l7FbuxWPczhmkK0HMR3CjnH%2BPxY1BfZkL09uUtNskIgTIv23%2FU6D2cA1TLtLOEkXczF3U6BbAJpOdH4BTPQ9USVoMFkL7QUomZdY9I5%2BpG7sqdPkd1jJ38y0NMNu3%2F9IGOqUBXHIevJfDDVII6wIDhxNw2jKP2GVgrxWuKaKk4SpsabMTBz5Kl2nDQtCWoowoLmOcQLFqnZCSa1z7wbuRLYYAOQ1Az%2B%2FC8%2BqPxqeC28pqjfQ8YSeFi4OtMRaRJKAQ5eFvQQU3K6sQb%2BaWND%2Fn7Omygr0oXSWYP4D2L%2BSQotrsDe2aSAn3DSi3hm9TZ%2BqVOBZK%2BlghtxBdT%2BjpHM5N4XliSLkUTA2r&X-Amz-Signature=0b6d759d27e78c905bb6ba75b74c2af1a332841de758e57d68083ecf524d2366&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

涉及到订单表，其实我们之前也说了，总共是涉及到了 3 张表，一张是订单表主信息表是订单的一个商品表，也就是我们的一个规格，以规格为单位所涉及到的一些商品的信息，以及是具体的价格。如果有多个商品相应的在这张表里面，其实我们应该是一个一对多的关系，在这里面会有多个订单商品和订单进行关联。还有一个是订单状态表，它是一个一对一的关系，只要是有一条订单，它就会有一个订单状态的数据进行插入，所以这些相关的数据我们都应该在创建订单的时候把数据插入到相关的表里面去。OK，好。所以第一个我们应该是新新的订单，新订单数据保存。


第二步我们在这里面可以先把我们所要去做的步骤可以都去写一下。第二步应该是根据 item IDS 循环规格的 ID 保存订单商品信息表。


好。第三步，保存订单状态表OK，好，我们可以先来做第一步新的订单数据的一个保存。首先我们要保存，应该要把 old 给 u 一下， orders 写一下，这是一个 new order。 new 出来。 new 出来了以后，我们第一个所需要去设置的应该是它的组件。组件。其实我们在之前也说了，我们会使用Sid。 Sid 我们在这边写一下，需要把 Sid 给注进来。Sid。随后我们只要在这个地方通过 Sid 点 next short，就可以拿到唯一的 ID 了。


写一下，这是一个 string 类型的 all 的ID，拿到以后直接往这边一插，这样子就 OK 了。好，下一个是订单，通过订单点 set 是一个 user ID， user ID 从这里拿，我们是在 Bo 里面是可以获得到的，所以直接把 user ID 往这里面一塞，希望下一个我们就应该要去设置。来设置一个receive，是收货地址相关的一些内容。收货地址其实我们应该要去做一个查询。在这里其实我们应该要 set 一个 receiver name，再来 set receive a mobile，这是手机号。再来一个 receive 它的地址相应的内容。在这里其实我们应该要在此之前做一个查询，也就是把地址相关的内容给去查出来。


我们可以打开地址的service，我们可以来看一下 address service，在这个类里面我们可以来看一下，可以按 **Ctrl 加 F12** 浏览一下我们的一些方法。在这里面其实会涉及到一个query，但是它没有一个具体的查询。其实我们应该要根据传入的一个地址ID，也就是在我们的 service 里面拿到的一个 address ID。根据 address ID 以及 user ID 去查询一下我们所要去拿到的一个真实的地址对象，对吧。这个地址对象其实在我们当前的 address service 这里面其实没有涉及到，所以我们可以去新创建一个service，我们可以去写一下。在这里面新建一个方法，叫做public，返回的是一个 user address query， user address 传入的两个值，一个是 user ID，一个是 address ID，把它给传进去就行了。加个注释，根据用户 ID 和地址 ID 查询具体的用户地址对象信息。好，随后到他的一个实现里面去把相应的方法去实现一下。先把这个方法我们先把实现生成事务加一下，既然是查询，使用 sports 就可以了。好，我们在这里面就可以去编写相应的方法。其实我们使用通用 map 就可以了，写一下你有一个。先把 user address 给 new 出来，留出来以后把地址 ID 以及是用户 ID 在这里面塞入。以后我们可以直接通过它的通用 map 点 select one 查询一个对象，把 default address 给加入进去就可以了。


default address 可以去改一下，因为之前我们在这里面设置的是一个默认地址，在这边统一的把它改成改一下 reflect rename，把它改成一个， single address，这样子也行。查询出来以后就是一个单独的对象了。好，再把 g s service 关闭。现在在我们的订单里面要去使用，直接在这边我们可以引入一个 service 就行了。这是 address service，把它给注进来。注进来以后，在这个地方我们把一些预备信息在这边都可以去写一下。这是一个 user address address 对象，通过 service 点 query 把 user ID 以及是 address ID 给传进去，这样子我们这个地址相应的信息我们就可以拿到了。拿到以后，随后我们在现在的三项属性里面都可以去塞入相应的值了。


address 点 get 在这里是你第二几个 c 的是用户的姓名，随后再来一个获得他的手机号，再来一个获得他的地址。地址信息应该是一个拼接省市区，把这些内容都拼接一下就可以了。第一个是 get province，加上一个空格，再来 get 一下city，再来一个，把它加上一个空格，这边再是 get 一个 district 区，再拉一个空格， get 一下它的一个detail。


相应的具体的信息内容我们在这里就全部的拼接好了，

[image](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/aa993a85-b282-49ef-8040-ec1941f29c39/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XBO7TLNQ%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T224704Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIEGS%2Fuc6VX9DfyBW4z7DungtCpFUlqiSP83I7MHSM3omAiEA44o%2BlV%2FGJMel7rN5%2BmRImPV0VMdfh4%2BU9Nrj9wLlB%2B8qiAQIxv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDD2bMxHjSetPHCYlpCrcA5GnIX8ycCbbuEqSlZvsSOf%2Fat01dPxYY4WszhHgyuBx1GuWPAezGOMXA96sz%2FMO1SMGjsaoPOezF0nGbaRxH3QGFPTHSI8NbIZ57XD77uVnWlz8ojY4Zd%2BAfpshLSb4qykIDmJXHyE38nTL20MD1pV8eDE%2B2mpE1e%2F2KnXgORdIaTjiQaLNLg0id2JB3Eh5RU5Lp1lsbaqvhFeDaQwsq%2BGoCRCHdxjpcGXo9moO5Y2%2BbMpkFoz%2BMkizdB9GCiLhVSqeMj1lUW1UFO1vEcludLNjHiSeOL6jrQrSk8YHzSNAJBlePH1SHm0dHv%2BueAKEftXHMBDdw%2BuOTmm7t0kQ%2BIkl5UB77R9jL%2FlZIq0yc0fVI7iGKnx3%2BMbN0omB%2B9ZNT2dikgO9jD%2FInjs3xg2xv14Ln5DvCHP6JDQov4XEN8yfg4%2B%2FMYC%2F29CW6x%2FlQ53J%2FAF3uz1%2FMkSX1NjbwdEYidkxWRP1q7FeC7wZIHrWt8btHetjTj8iHhSivqBG5LKa402l7FbuxWPczhmkK0HMR3CjnH%2BPxY1BfZkL09uUtNskIgTIv23%2FU6D2cA1TLtLOEkXczF3U6BbAJpOdH4BTPQ9USVoMFkL7QUomZdY9I5%2BpG7sqdPkd1jJ38y0NMNu3%2F9IGOqUBXHIevJfDDVII6wIDhxNw2jKP2GVgrxWuKaKk4SpsabMTBz5Kl2nDQtCWoowoLmOcQLFqnZCSa1z7wbuRLYYAOQ1Az%2B%2FC8%2BqPxqeC28pqjfQ8YSeFi4OtMRaRJKAQ5eFvQQU3K6sQb%2BaWND%2Fn7Omygr0oXSWYP4D2L%2BSQotrsDe2aSAn3DSi3hm9TZ%2BqVOBZK%2BlghtxBdT%2BjpHM5N4XliSLkUTA2r&X-Amz-Signature=97eea4a374d8541fabb9953c1c2b37a901c585c10ad412fabcaf003d2709af44&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

只不过有点长。没关系，我们在这边做一个换行。OK，这样子格式上看上去就可以舒服一些了。好，这些是订单里面所涉及到的一个地址信息。好，最后下一个， order 点set，现在我们往下面看。我们可以看到有一个 total amount，这是一个价格，这个价格现在我们其实应该要去计算的，所以我们先写好，写了之后我们在直接注释掉，因为我们在后面会去使用的，所以我们直接注释。再来一个 uo 的点set，在这里面还有一个价格，就是 real pay amount，真实的支付的价格，我们也现在是用不到，所以我们也注掉，我们也会在后面再去把相应的一个金额给输进去。好再来一个价格。这个价格是什么？点 set 有一个 post amount，我们之前说过了，它是一个邮费，默认是可以为 0 的。OK，所以我们只要把前面我们在社死的邮费直接写过来就可以了。如果以后大家在做电商的时候，在前端它会有相应的邮费的选择，以后它肯定也会有不同的地区的邮费规则。根据邮费的规则，在数据库后端，在我们的 service 里面可以拿到某一个地区所对应的一个邮费，或者也有可能商品，它的邮费本身设置为死的，它是不可动态的去变化的。在后端拿到相应的邮费以后，在 order 里面直接 set 一个 post 棒子，这样子就可以了。OK，好。这个是订单里面和价格相关的一些。

[file](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/28878b08-bcd1-4087-9000-71f135d3f915/OrdersServiceImpl.java?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XBO7TLNQ%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T224704Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIEGS%2Fuc6VX9DfyBW4z7DungtCpFUlqiSP83I7MHSM3omAiEA44o%2BlV%2FGJMel7rN5%2BmRImPV0VMdfh4%2BU9Nrj9wLlB%2B8qiAQIxv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDD2bMxHjSetPHCYlpCrcA5GnIX8ycCbbuEqSlZvsSOf%2Fat01dPxYY4WszhHgyuBx1GuWPAezGOMXA96sz%2FMO1SMGjsaoPOezF0nGbaRxH3QGFPTHSI8NbIZ57XD77uVnWlz8ojY4Zd%2BAfpshLSb4qykIDmJXHyE38nTL20MD1pV8eDE%2B2mpE1e%2F2KnXgORdIaTjiQaLNLg0id2JB3Eh5RU5Lp1lsbaqvhFeDaQwsq%2BGoCRCHdxjpcGXo9moO5Y2%2BbMpkFoz%2BMkizdB9GCiLhVSqeMj1lUW1UFO1vEcludLNjHiSeOL6jrQrSk8YHzSNAJBlePH1SHm0dHv%2BueAKEftXHMBDdw%2BuOTmm7t0kQ%2BIkl5UB77R9jL%2FlZIq0yc0fVI7iGKnx3%2BMbN0omB%2B9ZNT2dikgO9jD%2FInjs3xg2xv14Ln5DvCHP6JDQov4XEN8yfg4%2B%2FMYC%2F29CW6x%2FlQ53J%2FAF3uz1%2FMkSX1NjbwdEYidkxWRP1q7FeC7wZIHrWt8btHetjTj8iHhSivqBG5LKa402l7FbuxWPczhmkK0HMR3CjnH%2BPxY1BfZkL09uUtNskIgTIv23%2FU6D2cA1TLtLOEkXczF3U6BbAJpOdH4BTPQ9USVoMFkL7QUomZdY9I5%2BpG7sqdPkd1jJ38y0NMNu3%2F9IGOqUBXHIevJfDDVII6wIDhxNw2jKP2GVgrxWuKaKk4SpsabMTBz5Kl2nDQtCWoowoLmOcQLFqnZCSa1z7wbuRLYYAOQ1Az%2B%2FC8%2BqPxqeC28pqjfQ8YSeFi4OtMRaRJKAQ5eFvQQU3K6sQb%2BaWND%2Fn7Omygr0oXSWYP4D2L%2BSQotrsDe2aSAn3DSi3hm9TZ%2BqVOBZK%2BlghtxBdT%2BjpHM5N4XliSLkUTA2r&X-Amz-Signature=cf20d61913ed18dc50c95e0b4789d2ffe1be12dfe0d5c2262fa1e510386f2564&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

最后下一个 order 点set。现在我们还有一个是由用户去进行选择的配method，这是它的支付方式，直接把配 method 我们在前面这里 d 的直接拿过来就行了。好，下一个应该是传入进来的message，就是用户的一个备注 left message，把也给传一下，好，OK。


还有在我们订单里面，它还是会有一些其他的信息，比方它会有一个 is comment，这个是指我们的这笔订单有没有被评价过。刚刚创建的时候肯定是没有评价，所以我们使用 yes or NO 里面的 NO 设置为 0 就可以了。这个是否评价？还有一，这个是非常重要的状态，也是否删除，这是逻辑删除我们之前也说的肯定的。我们要把设置为no，OK，好。最后还有两项，它是一个 create time 和 up 的time，直接把这两个设置为你有 date 当前的一个时间就可以了。 update time 在这里面直接也是你有一个 date 就行了。OK。在这里面其实就是我们现在所设置的一些我们为新的订单里面所设置的一些相应的基本数据，这些基本数据当我们全部都设置完毕以后，随后我们就可以为订单去做一个保存。


但是保存之前其实我们在也了会有两个价格，这两个价格其实我们都要去计算的，并且我们计算都是通过 item s， p c， i d s，这就是一个以商品规格为单位的商品项，我们会以 i d 作为一个数组去循环，循环的以后我们会把它真实的一个价格计算完毕以后，在最后我们再会把价格放到我们的牛欧的里面，我们再去做一个订单的保存。我们会这样子去做的，OK？

```java
@Transactional(propagation = Propagation.REQUIRED)
    @Override
    public OrdersVO createOrder(SubmitOrderBO submitOrderBO) {
        String userId = submitOrderBO.getUserId();
        String addressId = submitOrderBO.getAddressId();
        Integer payMethod = submitOrderBO.getPayMethod();
        String itemSpecIds = submitOrderBO.getItemSpecIds();
        String leftMsg = submitOrderBO.getLeftMsg();

        // 包邮的费用设置成 0
        Integer postAmount = 0;

        String orderId = sid.nextShort();  // 唯一的id

        UserAddress address = addressService.queryUserAddress(userId, addressId);
        // 1:新订单数据的保存
        Orders newOrder = new Orders();
        newOrder.setId(orderId);
        newOrder.setUserId(userId);

        newOrder.setReceiverName(address.getReceiver());
        newOrder.setReceiverMobile(address.getMobile());
        newOrder.setReceiverAddress(address.getProvince() + " " + address.getCity() + " " + address.getDistrict() + " " + address.getDetail());

        newOrder.setPostAmount(postAmount);

        newOrder.setPayMethod(payMethod);
        newOrder.setLeftMsg(leftMsg);

        newOrder.setIsComment(YesOrNo.NO.type);
        newOrder.setIsDelete(YesOrNo.NO.type);

        newOrder.setCreatedTime(new Date());
        newOrder.setUpdatedTime(new Date());

        // 2:循环根据ItemSpecIds保存订单的
        String[] itemSpecIdArr = itemSpecIds.split(",");
        Integer totaolAmount = 0;  // 商品原价累计
        Integer realPayAmount = 0; // 优惠后的知己支付价格累计

        for (String itemSpecId : itemSpecIdArr) {
            // 2.1：根据规格id， 查询规格的具体信息，主要获取价格
            ItemsSpec itemSpec = itemService.queryItemSpecById(itemSpecId);

            // TODO 整合redis后，商品购买的数量重新从redis购物车中获取
            int buyCounts = 1;
            totaolAmount += itemSpec.getPriceNormal() * buyCounts;
            realPayAmount += itemSpec.getPriceDiscount() * buyCounts;

            // 2.2:根据商品id，获得商品的信息以及商品图片
            String itemId = itemSpec.getItemId();
            Items item = itemService.queryItemById(itemId);

            String imgUrl = itemService.queryItemMainImgById(itemId);

            // 2.3:循环保存子订单数据到订单数据库
            String subOrderId = sid.nextShort();

            OrderItems subOrderItem = new OrderItems();
            subOrderItem.setId(subOrderId);
            subOrderItem.setOrderId(orderId);
            subOrderItem.setItemId(itemId);
            subOrderItem.setItemName(item.getItemName());
            subOrderItem.setItemImg(imgUrl);
            subOrderItem.setBuyCounts(buyCounts);
            subOrderItem.setItemSpecId(itemSpecId);
            subOrderItem.setItemSpecName(itemSpec.getName());
            subOrderItem.setPrice(itemSpec.getPriceDiscount());
            orderItemsMapper.insert(subOrderItem);

            // 2.4: 在用户提交订单后，规格表中需要扣除库存
            itemService.decreaseItemSpecStock(itemSpecId, buyCounts);
        }
        newOrder.setTotalAmount(totaolAmount);
        newOrder.setRealPayAmount(realPayAmount);
        ordersMapper.insert(newOrder);

        // 3:保存到订单表
        OrderStatus waitPayOrderStatus = new OrderStatus();
        waitPayOrderStatus.setOrderId(orderId);
        waitPayOrderStatus.setOrderStatus(OrderStatusEnum.WAIT_PAY.type);
        waitPayOrderStatus.setCreatedTime(new Date());
        orderStatusMapper.insert(waitPayOrderStatus);


        // 4:构建商户订单，用于传给支付中心
        MerchantOrdersVO merchantOrdersVO = new MerchantOrdersVO();
        merchantOrdersVO.setMerchantOrderId(orderId);
        merchantOrdersVO.setMerchantUserId(userId);
        merchantOrdersVO.setAmount(realPayAmount + postAmount);
        merchantOrdersVO.setPayMethod(payMethod);

        // 构建自定义订单VO
        OrdersVO ordersVO = new OrdersVO();
        ordersVO.setOrderId(orderId);
        ordersVO.setMerchantOrdersVO(merchantOrdersVO);
        return ordersVO;
    }
```

