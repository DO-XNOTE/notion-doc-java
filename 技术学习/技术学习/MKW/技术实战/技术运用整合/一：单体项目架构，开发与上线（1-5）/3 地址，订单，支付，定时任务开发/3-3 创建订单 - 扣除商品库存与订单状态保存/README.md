---
title: 3-3 创建订单 - 扣除商品库存与订单状态保存
---

# 3-3 创建订单 - 扣除商品库存与订单状态保存

[image](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/0bfa59b5-dd34-4807-8401-7569f61ea8d7/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466Y2YUH4II%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T224705Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDT8BXbZmsbmxJENHy3MDjnhi1mPKLAdDzCByt0i%2FvMYQIgQJwsToDqOXB%2BWXKHbJDmKSKszbTxyBKdlg2K4jcdIgEqiAQIxv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDE3GIscHSkXjt3P%2FhSrcAxvLUnPV0Zw4Dg7xZU4PWdP2T%2BopcMIQIlCaNvUWYFlWo3woJM4yT4gxa4IJwg9gnhecWZG8x%2FKrIzlteB9ekW0i4vug5mli9RNvAfOBer7a%2B4uymrNpY6CWIQfrqute8dtUqZ77r8hO6U3Ar2WtaMbr9VuuXkJ7kf2gl2b2p8ttDQoAy3TmqOxJumIWW3A%2FlFQH8Na4ZYtyV92pMmAH%2F%2Fjm8C5GWM15kQ8DvAzUE3GF2J3CO1U3a0%2BB%2B%2B%2FJvpNgezi5Bjv7N0nBDLqmhVmAwN5FR5WfzfgVsZLt0ypNaVIQYlP0mDXx7rlutom2iZmcBzFHWp8FkLCatngfCKfJnsNBEhr8lWmWVRpLF4Oja7UDOwytdn2gAREghbDHXVDZVRi%2Bsz6blq5KMWI4B0e0LIA9ePboMQUqir7OrhJFBju6C3PW8KYmg%2B2q%2BpS7Reg7mypW8%2B6X%2BKCp61F2lnykuga0UOV5tnCNHXaepKyJd7o%2BKwAoyeF6vn7mIcgyWLWcSkpFYEv4FrMubgpaVWEr0olJYWQcwfspYboPwxy5AvdFwnGLFjfqfz2Xgq%2FlKcGXQREipin9rKo%2BeFtsg79ERcQQp4A5CbQM0joOOkf7sVZsumqXsFDJ4kMVAuzpMO%2B3%2F9IGOqUBk0uiJaX3JkeuhpSNknrK%2BW%2B%2BEVMxRKaarkCLOWqn4al3h6kvkX0ElEOBau4PDOg4wdveoYlfJoxjB9%2BE5Ss6brG4%2FsTjcjq9Elat1T5kGShDHhEa0t2RlB0e%2BxX00EHd084esfxepbKcBvHbmap2m3MRig1y%2FJOviGhlGq9JIlXGz1cpRRvDvX6Jw8CPmek3%2FRNonENNn1W%2BzUqL7ZBj4FCs98HE&X-Amz-Signature=4390c00886146bccc1b2c9d046d6594c708fedad344090767bec9952c3521872&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

前面两节我们是针对了订单基本信息表以及是子订单表做的一个数据的保存。接下来我们要保存一下订单状态表，也就是这张表。这一张表里面所涉及到的一些信息，其实一开始是比较少的，主要在最一开始我们要保存的一个订单状态，就是订单的初始状态，我们是一个等待付款，也就是待付款状态去设置一下。另外它的一个当前订单创建的一个时间也是需要去设置的。最主要的其实就是这两个。所以我们可以先把可以先写一下，先把 order status，把这一个对象我们先给 Mute 出来。

[file](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/28878b08-bcd1-4087-9000-71f135d3f915/OrdersServiceImpl.java?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466Y2YUH4II%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T224705Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDT8BXbZmsbmxJENHy3MDjnhi1mPKLAdDzCByt0i%2FvMYQIgQJwsToDqOXB%2BWXKHbJDmKSKszbTxyBKdlg2K4jcdIgEqiAQIxv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDE3GIscHSkXjt3P%2FhSrcAxvLUnPV0Zw4Dg7xZU4PWdP2T%2BopcMIQIlCaNvUWYFlWo3woJM4yT4gxa4IJwg9gnhecWZG8x%2FKrIzlteB9ekW0i4vug5mli9RNvAfOBer7a%2B4uymrNpY6CWIQfrqute8dtUqZ77r8hO6U3Ar2WtaMbr9VuuXkJ7kf2gl2b2p8ttDQoAy3TmqOxJumIWW3A%2FlFQH8Na4ZYtyV92pMmAH%2F%2Fjm8C5GWM15kQ8DvAzUE3GF2J3CO1U3a0%2BB%2B%2B%2FJvpNgezi5Bjv7N0nBDLqmhVmAwN5FR5WfzfgVsZLt0ypNaVIQYlP0mDXx7rlutom2iZmcBzFHWp8FkLCatngfCKfJnsNBEhr8lWmWVRpLF4Oja7UDOwytdn2gAREghbDHXVDZVRi%2Bsz6blq5KMWI4B0e0LIA9ePboMQUqir7OrhJFBju6C3PW8KYmg%2B2q%2BpS7Reg7mypW8%2B6X%2BKCp61F2lnykuga0UOV5tnCNHXaepKyJd7o%2BKwAoyeF6vn7mIcgyWLWcSkpFYEv4FrMubgpaVWEr0olJYWQcwfspYboPwxy5AvdFwnGLFjfqfz2Xgq%2FlKcGXQREipin9rKo%2BeFtsg79ERcQQp4A5CbQM0joOOkf7sVZsumqXsFDJ4kMVAuzpMO%2B3%2F9IGOqUBk0uiJaX3JkeuhpSNknrK%2BW%2B%2BEVMxRKaarkCLOWqn4al3h6kvkX0ElEOBau4PDOg4wdveoYlfJoxjB9%2BE5Ss6brG4%2FsTjcjq9Elat1T5kGShDHhEa0t2RlB0e%2BxX00EHd084esfxepbKcBvHbmap2m3MRig1y%2FJOviGhlGq9JIlXGz1cpRRvDvX6Jw8CPmek3%2FRNonENNn1W%2BzUqL7ZBj4FCs98HE&X-Amz-Signature=276d12e3c0edeee1d8212f62ef8151090215d06dd8d4a2932f822d41b595c503&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

既然是涉及到了订单状态，所以对象我们在一开始创建的时候，我们就在这边写的更加详细一些，叫做 wait 配 order status，就是等待付款的一个订单状态。好，我们在这里面就可以去塞入相应的值了。首先第一个我们要去设置一下主键订单状态表，它的组件和订单基本信息表的组件其实是同一个组件，所以在这里面直接把 order ID 给塞进去就可以了。随后第二个第二个就是一个状态，有一个 order status。订单状态。在这里其实我也已经是预先写了一个 order status，它会有一个枚举类，预先我也已经是写好了，大家可以直接复制过去使用。在这里面看一下，总共是有 5 个我们所需要去使用到的状态。第一个是等待付款，第二个是用户已经是付款完毕了，处于一个待发货的情况，随后是一个已发货，等待收货。

[image](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/fa6ff88e-1ff0-45b1-8a7f-52a9504d5297/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466Y2YUH4II%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T224705Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDT8BXbZmsbmxJENHy3MDjnhi1mPKLAdDzCByt0i%2FvMYQIgQJwsToDqOXB%2BWXKHbJDmKSKszbTxyBKdlg2K4jcdIgEqiAQIxv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDE3GIscHSkXjt3P%2FhSrcAxvLUnPV0Zw4Dg7xZU4PWdP2T%2BopcMIQIlCaNvUWYFlWo3woJM4yT4gxa4IJwg9gnhecWZG8x%2FKrIzlteB9ekW0i4vug5mli9RNvAfOBer7a%2B4uymrNpY6CWIQfrqute8dtUqZ77r8hO6U3Ar2WtaMbr9VuuXkJ7kf2gl2b2p8ttDQoAy3TmqOxJumIWW3A%2FlFQH8Na4ZYtyV92pMmAH%2F%2Fjm8C5GWM15kQ8DvAzUE3GF2J3CO1U3a0%2BB%2B%2B%2FJvpNgezi5Bjv7N0nBDLqmhVmAwN5FR5WfzfgVsZLt0ypNaVIQYlP0mDXx7rlutom2iZmcBzFHWp8FkLCatngfCKfJnsNBEhr8lWmWVRpLF4Oja7UDOwytdn2gAREghbDHXVDZVRi%2Bsz6blq5KMWI4B0e0LIA9ePboMQUqir7OrhJFBju6C3PW8KYmg%2B2q%2BpS7Reg7mypW8%2B6X%2BKCp61F2lnykuga0UOV5tnCNHXaepKyJd7o%2BKwAoyeF6vn7mIcgyWLWcSkpFYEv4FrMubgpaVWEr0olJYWQcwfspYboPwxy5AvdFwnGLFjfqfz2Xgq%2FlKcGXQREipin9rKo%2BeFtsg79ERcQQp4A5CbQM0joOOkf7sVZsumqXsFDJ4kMVAuzpMO%2B3%2F9IGOqUBk0uiJaX3JkeuhpSNknrK%2BW%2B%2BEVMxRKaarkCLOWqn4al3h6kvkX0ElEOBau4PDOg4wdveoYlfJoxjB9%2BE5Ss6brG4%2FsTjcjq9Elat1T5kGShDHhEa0t2RlB0e%2BxX00EHd084esfxepbKcBvHbmap2m3MRig1y%2FJOviGhlGq9JIlXGz1cpRRvDvX6Jw8CPmek3%2FRNonENNn1W%2BzUqL7ZBj4FCs98HE&X-Amz-Signature=1cc874196f60714b5c96e3dddcc16717fa69e9bf2fdcdb60ec456a263dfa2170&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

再下面是一个交易成功，交易成功和交易关闭，这两个都是订单里面的两个状态。当然如果你的订单流程比较多，比较复杂，订单状态在这里面可以相应的自己去扩展也是没有问题的。在这里面我们在咱们的订单流程里面主要使用到这几个就可以了。好，下一个。在这里我们就应该要来写上一个 wait pay，等待付款。


好，OK，下一个。也就是第三个字段，我们只需要去设置一下它的订单的创建时间，把当前的时间给放进去就可以了。这样子我们只需要 3 个字段就可以了。随后我们应该要去写一下map，来看一下， map 应该现在还没有写，在这里面我们复制一行，写上一个 order status map。好，这样子就有了。以后我们在这个下方去把对象做一个 insert 就行了，把这个放进来。好。OK。


这样子我们涉及到订单相关的三张表，相关的数据，其实我们就已经是做了一个保存音色的。做完这些基本的数据以后，其实在我们的上一节课里面，上一节课我们在这边是做了一个循环循环的，在我们的一个子订单里面去做了一个数据的保存。但是在保存完毕之后，其实有一点我们是需要去注意的。


先来看一下我们的一个数据库表，我们可以找到咱们的一个规格表，这是规格表，在规格表里面可以看到它会有一个库存，当用户的订单创建完毕以后，相应的只要在购物车里面这一件商品所对应的规格，它是放入了。不管是纸件。在这里它的库存应该要减掉。这一步操作我们应该要去做的。所以我们回到代码，在这里也写一个 2 点 4 步骤。在这边我们应该要去扣除库存。写详细一些。在用户提交订单以后，规格表中需要扣除库存。这一步操作是一定要去做的。OK，所以我们在这里去写一下相应的方法。我们在 item service 里面肯定是没有，所以我们在里面去写一下对应的方法。写一个 public void 减少是decrease， item s p c stock 减少。


规格里面的一个库存要传入进来是两个参数，这是实现，我们应该要把这个方法写到接口里面去，写到它的接口。在这里面出现，要传入两个参数，其中一个是规格ID，随后一个用户购买的数量。我们现在还没有整合Redis，所以其实我们现在的 buy CONS 都是唯一，但是没有关系，我们直接把白 COS 可以传入进来就可以了。


这是两个参数，这个就是要在我们库存里面所要去扣除的数量，这个是减少库存。OK，好，我们到这里面去实现一下。方法导入。在这边我们要使用一个事务，涉及到修改，我们会使用到request，好在这里面去写一下。要去减少库存，可能一般会有同学会这么写。


首先可能会做一步操作，比方查询库存，这个库存的数量是要查询出来的。比方现在我们的查询出来以后，假设在这个地方，我们是做了一部数据库的操作，查询出来stock，比方我们就来一个，还剩一两件。第二步要去判断，判断库存是否能够减少到 0 以下，也就是在这边要做一个判断一下， stock 减掉 by comes，如果减到它的值，如果小于 0 了，达到 0 了以下就代表我库存不够。


在这边应该要提醒一下用户，歧视用户，或者直接抛一个异常说我们的库存不够了。即使用户库存不够。这样子的做，可能会有一部分同学想到是去这么做。但是会有一个问题是什么问题？库存对于所有的用户来讲，它其实是属于一种公共的资源，只要是公共的资源，在一个高并发的情况下，有可能在这边库存一直在处理，有可能会达到一个超卖。的确会存在一个超卖的。比方现在我有一个请求，或者是一个线程进入，进入来了以后，比方现在我是一个10，他要去查询库存的时候，直接查出来18，可能我有两三个线程同时查询都是10，查询出来是10。在这里它会有涉及到相应的bycounts，可能是三三和5，这样子加起来总共是11。当它们同时拿到库存是 10 的时候，在这边进行一个判断，会发现没有问题。之后在这边会执行一个数据库的扣库存，扣完之后就是 10- 3 减3，再减5，这个时候会等于-1，这个时候你会发现库存少于 0 了以后，其实会出现一种超卖的情况。在真实的生产环境上，如果你做的不够好，真的是有可能库存会达到负的 100 或者是负的上千。在这种情况下其实就做到了我们数据的一个不一致性。在我们的一个正常的业务逻辑里面，自己公司的库存是不可以少于 0 的，少于 0 了以后，你可能要去进货，要去做其他的方面的处理，所以在我们程序里面是需要去进行控制的。所以这就是一个共享资源所涉及到的数据的一致性。


我们不能够把 stock 库存降低到 0 以下，如何去处理？可能会有同学会说，只要在这个方法的地方加上一个关键字，也就是辛苦nice，针对我们当前这个方法去加一个锁，这样子做其实的确是可以保证我们的一个资源不被多个线程去共享，但是它会有问题。使用它的时候，其实本身它就是一个的线程去进行，直接它的效率性能其实会比较低下，所以这种方式我们不会去使用。它。


还会有另外一个问题，如果现在我们是单体，它的确可以保证这样的一个问题是没有的。但是如果我们在后续把我们的单体发展成一个职群，这个关键字就会不起作用了。因为在我们的集群环境下，它是会有几台服务器，或者几十台、几百台这样子，它的每一个服务器之间，它可能还是会存在于一个资源共享的问题，所以这个是会失效的，所以这个是不会去使用。


当然也有可能会有同学会我们能够在数据库里面，针对于我们当前这张表，把这张表去锁一下。这种情况其实是更加不能够去做了。因为一旦去锁数据库，万一出了问题，数据库的性能会非常非常低下，所以锁数据库也是不可以去做的。OK，这两种方式都是不能去做，我在这边去写一下。


第一个是使用关键字直接复制过来，不推荐使用，集群下无用，性能低下。第二个锁数据库不推荐，这是导致数据库性能低下。除了这两种方式以外，其实还有一种方式是属于在集群和分布式环境下可以去使用的分布式锁。分布式锁的确是可以保证我们的一个数据的一致性。刚刚我们说了，使用关键字在集群下是没有用的。如果我们现在是一个咨询或者分布式的环境下，使用分布式锁可以解决这种问题。


分布式锁其实在后面涉及到 scope 的阶段，应该会有一个分布式的阶段，会专门针对分布式所来进行讲解的。它其实会涉及到一个是 scope 以及是Redis，这两个中间件都是可以做分布式锁的，它会由相应的老师去跟大家去讲解。其实也是在这个地方。我直接以这种假代码来写，比方是有一个lock， 5 跳点， get lock 在这里其实就是枷锁，在执行我们的一个库存业务的之前，加上一把锁在这个地方，如果我们的一个库存扣完以后我们就可以去解锁。在这里是unlock，把锁解开，加锁跟解锁。


OK 其实就是这样的一个通用的有跳。这样子其实就可以保证我们的数据在集群和分布式环境下数据的一致性，绝对是不可能会出现超卖的情况。 OK 相应的我们也说了分布式锁，在后续分布式阶段会有相关的老师跟大家具体去聊一聊，因为会涉及到锁 keeper 以及是 Redis 的。 OK 在我们单体里面，我们现在这些我们都不用，该怎么去做。其实我们可以使用乐观锁的一种情况去做一个设置，也就是我们直接通过 SQL 语句去做一个更新也是没有问题的。如何去做？首先一个我们要去写一下咱们的自定义的思考语句了。自定义的思考语句我们来找一下。我们需要到 map 里面，把这个找一下。找到 itemsmapper custom。把自定义的 map 先写好。以后在这里面我们会做一个执行的语句。先写一下。把这个方法直接写一下。迪克瑞斯斜过来。


degrees item s p c stock 结尾服写一下。在这边我们可以直接去写相关的一个语句就可以了。去 update 一下我们的 items 这张表名，我们来看一下。是这张表。直接把这张表的表名拷贝一下，在买白蒂斯里面的 map 去写。它会没有代码提示，大家可以直接在 SQL 的工具里面去写，写完再复制过来也是可以的。


set 一下，把我们的 stock 去进行一个设置， stock 等于 stock 减掉我们传入的一个参数。传入的一个参数就是等待要去扣除的一个数据，其实就是 by counts，在这边写好取个名字，叫做 Pend in counts，就是等待的一个数值。我们的 stock 要去设置为当前的 stock 数量，减掉一个 icon 就可以了。


随后我们要去加上一个条件，这个条件我们设置为ID，等于这个 ID 其实就是我们的规格ID。规格 ID 也是一个参数，要传进来的，直接写一下，这是我们的规格ID，这是第一个条件。随后还有第二个条件，写一个 and 第二个条件。我们就需要来设置一下stock，其实这样子去做，直接在后面不加任何条件，在这种情况下是肯定会出现超卖的。这是我们可以用乐观锁的一种机制，就可以达到一个这样的效果。


在这里使用一个 stock 并起来， stock 必须要大于等于我们的 pending counts。OK，可以这样子去做，只要我们当前的条件， stock 是大于等于我们传入进来的一个要去扣除的数量，就可以达到我们的一个效果。如果我们执行成功了，对于我们的一个 my bet is 执行的一个语句，它会有一个result。它的一个语句。如果是等于1，我们更新到数据库里面的一个数量，如果是1，就代表我们这一条记录是更新了。如果不是 1 是0，就代表没有更新，没有更新就代表我们条件没有达到，我们是可以抛出一个异常的，但是又由于我们的一个事物，如果在我们的 service 里面抛出一个异常，会被我们的 old service 里面会被接收到。在这里报了一个异常，会导致我们整个事务会失效，相应的数据都会回滚。所以我们在这里面就可以这样子去使用这种乐观锁的机制，就可以去达到我们的效果了。


OK 好，我们在要去写一下他的 name space，在这里面要去写一下。名字，取名也是一样的。 public Int 就是执行返回出来的一个数值，就是更新到数库里面所反映出来的一个数量，要传入一些相应的参数。第一个参数我们定义为来看一下。我们用规格 ID 写在第一个s， p c i、 d string 规格ID。好，我们再传一下第二个参数。第二个参数就是要去扣除的数量。 Penny counts。写到这里，我们传入进来的数量也可以一样。换一行，它是一个 Int 型的Int， Penny 抗死，把这两个传进来就可以了。


OK，这就是我们自定义的一个map。随后在我们的这一块地方，我们就可以具体了。这些注释我就放着，注释我就放着了。在这里我们就可以去使用了。 items 有一个哈斯特。 items map custom。通过这个方法去调用我们刚刚的一个 decrease 点。 decrease 传入参数，一个是辉哥ID，另外一个是Bycounts。OK，在它的前方，我们可以去获得它的一个result，更新数据库的一个数量。判断一下，如果 result 它不等于1，如果 1 代表它是更新成功的，不等于 1 就代表它更新失败。很明显，更新室外，我们可以手动的来一个 throw new，一个 runtime 


excepting。在这里面我们可以加上一个我们自定义的message，比方还有一个订单创建失败，原因就是库存不足。 OK 这样子，如果在这里发生了一个异常，由于我们的service，我们是从 old service 去调用的，相应的有 service 以后，整个事物会回滚的。 OK 好，既然写好了我们的 item service 以后，在我们就可以去完善一下 item service their decrease，把规格 ID 以及是我们的 by counts 传进去，这样子就可以去执行我们的一个扣库存的操作了。 OK 这样子其实我们当前 service 我们就已经是写的几乎是 OK 了，因为它还涉及到一些其他的内容，我们会在后面我们再去完善一下。OK

