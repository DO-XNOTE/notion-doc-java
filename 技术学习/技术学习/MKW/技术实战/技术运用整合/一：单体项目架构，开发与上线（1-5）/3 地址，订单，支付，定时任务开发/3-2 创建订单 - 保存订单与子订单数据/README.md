---
title: 3-2 创建订单 - 保存订单与子订单数据
---

# 3-2 创建订单 - 保存订单与子订单数据

[image](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/d5d111d3-016b-4867-88b3-f086e4d125dc/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VKR4COA4%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T224704Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIGYrHtr2Zyy7fjjeW22Oj2DcDxHoha%2BElM%2Fz3ik7iJJqAiArHc8tsrypvazUGezw03fPejCB3kBhysrYq36vffLFtCqIBAjG%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMb%2Ff%2B8OBmWshqNcKMKtwDvUVxmqEOqLR9A0HY%2F9q858bfwiw7AE7nP3qh8vrD38%2FhjS%2Fg7Uqq6ovbjrarjQY70%2BHtuKTRUfcuoqqlPSYYHphvxf6xnoINZojURx9pDF6HfhRfDpQ%2BQncMOYVWakHS%2BXjXSOpsEnPlc8Ly6Pg7UOFTduAMEplw9wqObsD9nm9Dzq9BzoYBLqMUrAtj0qXuxfxdZXy4BzldczfPZwiMLwvnuy1s%2B9gJzbR%2FJ1sUyNsTCbJcPLWFAMqGoh0QzmG0vR45UWcLVMrnco3socpS51YlzlEvOFsyGyi7dO7znzUVmhpQw4MAUSFJZCBuuAFhxHskNG9%2FSirh6fVOcnHx6DF%2BBxd9e2A6ZQYoeYBPt1p7RX0CZBgp04wv6jEWqg%2BVMUq0WwB%2BvHtoXE97MEGfKJ%2FUUf7JmJBKUFU0joWChId7YbBZpix5i4v1OmCnzddvNr%2FDfo3PRqff6zGnNUkbvfxWchsFNRGyiNgu1vATak1iC%2BYhSqP%2FS2FpSCaPYUUJFR7u71Ll8%2FbuWiPuFt5g7qHXV3HB2eheiRGpJJ6vDIg9FbTtBXBf2kcTj9gvVr2AUR3KGc0YRXL1WkWhpxSvPBYCPOdn67c7iMJxVIiHnxLustLpD8BhT%2Bqkifwwm7r%2F0gY6pgFY3LrGtWUMGWxH3TB58dkIMv7PpluCE8VYMgx%2FKZScBBkn7K7fHPhjDDxsxz9y49SVSLrEQX%2FlLZ%2BE7VDc2a0GBj0IRLfYGiUULuux5qu5WgyD3fCz35Q26Fm%2BH46I%2Fl0e4AAbn%2F6pufTeC%2BeGiphmQh%2BsJJIDZ41g5mRS6q6wPdCGP3oWr07G023Ng5QEraxmkqt4VGXdw5MLQbcNDVOFycmicV3t&X-Amz-Signature=cbb3029d88e4b57525be1dc4f582b28a6ca72d1a01edf394dceea6b8c48b737e&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

上节课我们是填充了一下订单基本信息表里面相关的一些数据，只不过我们有两个价格还没有创进去，因为这两个价格是要让我们的一个s、p、c、i、 d 把去进行一个循环以后获取到真实的一个价格，累加以后再填入到 order 里面去的。所以这节课我们先来子订单，把订单关联的一个子订单表，其实也就是我们之前所说的一个订单商品的关联表，把它称之为是一个子订单也是没有问题的。把这个表我们要去进行一个循环的保存，

[file](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/28878b08-bcd1-4087-9000-71f135d3f915/OrdersServiceImpl.java?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VKR4COA4%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T224704Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIGYrHtr2Zyy7fjjeW22Oj2DcDxHoha%2BElM%2Fz3ik7iJJqAiArHc8tsrypvazUGezw03fPejCB3kBhysrYq36vffLFtCqIBAjG%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMb%2Ff%2B8OBmWshqNcKMKtwDvUVxmqEOqLR9A0HY%2F9q858bfwiw7AE7nP3qh8vrD38%2FhjS%2Fg7Uqq6ovbjrarjQY70%2BHtuKTRUfcuoqqlPSYYHphvxf6xnoINZojURx9pDF6HfhRfDpQ%2BQncMOYVWakHS%2BXjXSOpsEnPlc8Ly6Pg7UOFTduAMEplw9wqObsD9nm9Dzq9BzoYBLqMUrAtj0qXuxfxdZXy4BzldczfPZwiMLwvnuy1s%2B9gJzbR%2FJ1sUyNsTCbJcPLWFAMqGoh0QzmG0vR45UWcLVMrnco3socpS51YlzlEvOFsyGyi7dO7znzUVmhpQw4MAUSFJZCBuuAFhxHskNG9%2FSirh6fVOcnHx6DF%2BBxd9e2A6ZQYoeYBPt1p7RX0CZBgp04wv6jEWqg%2BVMUq0WwB%2BvHtoXE97MEGfKJ%2FUUf7JmJBKUFU0joWChId7YbBZpix5i4v1OmCnzddvNr%2FDfo3PRqff6zGnNUkbvfxWchsFNRGyiNgu1vATak1iC%2BYhSqP%2FS2FpSCaPYUUJFR7u71Ll8%2FbuWiPuFt5g7qHXV3HB2eheiRGpJJ6vDIg9FbTtBXBf2kcTj9gvVr2AUR3KGc0YRXL1WkWhpxSvPBYCPOdn67c7iMJxVIiHnxLustLpD8BhT%2Bqkifwwm7r%2F0gY6pgFY3LrGtWUMGWxH3TB58dkIMv7PpluCE8VYMgx%2FKZScBBkn7K7fHPhjDDxsxz9y49SVSLrEQX%2FlLZ%2BE7VDc2a0GBj0IRLfYGiUULuux5qu5WgyD3fCz35Q26Fm%2BH46I%2Fl0e4AAbn%2F6pufTeC%2BeGiphmQh%2BsJJIDZ41g5mRS6q6wPdCGP3oWr07G023Ng5QEraxmkqt4VGXdw5MLQbcNDVOFycmicV3t&X-Amz-Signature=56630811db6b4e1dd75bf7f12dc412530af46d8b42a362f685dfc5f798a61361&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

保存之前首先一个我们就要把这个规格的 ID 先要把它一个一个的要拿出来。首先它是一个以逗号为间隔的字符串，所以我们要 split 分割一下，写上一个逗号，进行一个分割。 split 以后它就是一个数组了。写一下它是一个 string 类型的 array item，s，p，e， c 规格。它是一个 ID 的a，r， r 其实就是 array 它的一个简称。不要忘记一个冲括号。好在这里面分割了以后，它就是一个数组。


数组我们就要去进行循环了。但是在循环之前，在一开始我们要把两个价格先定义为0，一个是总价格， total amount 等于0。不要忘记所有的单位都是以分为单位的，这是商品原价累计好。再来一个。下，就是一个真实的，具体的价格都是一个需要配amount。具体的价格设置为0，这是优惠后的实际支付价格累计好。随后我们就可以来做一个循环了。循环我们是循环的数组，在数组里面每一项它都是一个string。在这边设置一下，比方我们就取个名字为就叫这个商品的规格 ID 加个冒号，这样子我们就可以拿到数组里面的每一项了，每一项它都是一个字符串行的一个ID。


好拿到 ID 以后，首先第一个我们要根据规格的 ID 去查询一下规格的具体的信息，因为它里面包含了一个价格对吧，所以我们要去写出来。在这里面我们写好相应的步骤，这是第一步。第一步是根据规格 ID 查询规格的具体信息，主要获取价格。好在这里我们就可以去写一下了。


规格我们来看一下商品，打开商品的service，在这里面我们可以去搜一下，看一下有没有查询的相应的方法。可以搜一下，叫做 query s p，这里面没有获得相应的对象，它都是list，所以我们要去自定义一个。到它的接口里面，我们可以去写一下，写一下名字。 public 获得的是一个 item s p e c，它是一个对象，查询的方法叫做 query ITEM s p c。 by ID 根据规格 ID 去查询规格具体的信息。获取的是一个对象，加上注释，根据商品规格 ID 获取规格对象的具体信息。好，我们来到它的实现，把具体的实现去写一下，把这个方法给导入进来，事物加一下，在这边其实也是比较简单，由于 ID 它是一个组件，既然是一个组件我们就可以直接来一个 return 了。写上一个 items s p c Mapper，点select，第一个就是根据这个组件去查询，把 ID 给放起来，就可以拿到相应的信息了。好，现在我们只需要到订单的 service 里面，在这边去写一下，这是 item service，点做一个查询。


item service 看一下，我们在这里没有引入，所以我们要把 service 要引入一下。


好。随后我们回到下面的地方，把 service 写好，根据规格 ID 去查询规格的对象，规格 ID 写进来，这个规格对象我们就可以去在这个地方就可以拿到了。好，OK，好，拿到了以后我们就可以从规格的对象里面去获得相应的信息了。最主要的其实就是两个价格来看一下，一个是 total amount，在这里我们可以去写一下，在这边进行一个累加。我们通过是一个小写，通过在这个对象里面我们就可以去获得。来一个点get。我们在这边应该是获得它的 price 价格，应该是一个Normo，这是一个普通的价格，是进行一个累加的。但是在这边我们应该要乘以一个购买的数量，购买的购物车的数量，其实我们应该要从购物车里面去获得，但是我们的一个前端并没有传这样的一个 by Cos，其实 by Cos 在这里我们应该从后端的购物车里面去获取。


后端的购物车我们是以一种 Redis 的形式存在的，但是 Redis 我们还没有涉及到，所以在这个地方我们的一个 by Com 购物车中的商品数量，我们统一的都写一。等。到后续我们学到了分布式缓存阶段，我们回过头来再把这个地方的 by count 进行一个完善。也可以。所以我们在这里可以在这边先写一下，写一个Todo，整合 Redis 后，商品购买的数量重新从Redis，的购物车中获取。OK。 Todo 我们先写好，所以在这个地方我们可以设定为一个 by counts，直接设置为 1 就可以了。我们写死后面动态了以后，它的数量就可以和前端购物车中的数据保持一致了。OK，好，所以我们把 by Com 直接写到这个地方就可以了。这样子它的一个 total amount 就可以做一个累加了。好， total amount 累加了以后不要忘记它。


还有一个 real pay amount，这是优惠过后的一个总价格，它也是经过了一个累加，从规格的对象里面去获取。 get 有一个discount，这是一个优惠价，优惠价也是乘以一个 by Cos。直接这样子做一个累加。累加了以后，其实这两个数据在我们的牛欧的里面就可以去做一个设置了。


好，下一个。下面我们应该要获得我们商品的一些信息，因为在我们的这一张表里面，其实是也包含了商品的图片，商品的名称。图片和名称我们都分别对应了两张不同的商品的表，所以我们也应该要根据规格的ID，要把相关的信息去获得。所以下一个写好注释。根据规格 ID 获得商品信息以及商品图片。OK。规格 ID 本身在这张本身在对象里面，我们就可以 get 一个 item ID。应该在这里应该是根据商品的 ID 获得商品信息，以及是商品图片。因为我们从商品的规格里面就可以获得一个商品的商品 ID 了。写一下 string item ID，这样子就可以获得。


好，下一个我们就要去获取商品的信息了。商品信息我们来看一下商品的service，它里面有没有一个方法，我们来看一下它，这里面有一个 query item 8 ID，这个方法我们是可以直接去使用，它也是根据商品 ID 它的一个主键去进行查询的，所以我们可以直接在我们的 service 里面去使用的。通过 item service 点 query item by ID，在这里面直接把商品 ID 传入进去，相应的我们的商品信息就可以拿到了。


好，这是一个商品的信息。随后还会有一个商品图片，商品图片在这个里面应该是没有吧。搜一下 query items，有一个 image 图片，它是一个 list 对吧，不符合我们的需求，所以我们要去写一下。 public 写一个方法，在这里我们会使用的是一个直接获得一个商品主要的 UL 的地址就可以了。图片地址。所以图片地址使用的是一个 string query。


item man 是主图 image by ID 传入进来是一个商品的ID。写一下，这是根据商品 ID 获得商品图片的。商品图片主图 u r l 好。 OK service 的抽象方法就写好了。写好以后我们要写一下它的实现。在最后面直接把这个方法给实现一下。这是我们的事物，也要去写，是一个suppose。好在这里面我们还是一样。我们会通过一个以对象的形式去查询它的内容。在这里直接写上一个 items image。先把对象先写好，把直接给 new 出来，在对象里面去放入相应的内容。


首先第一个 set 一下它的ID，这个 ID 是 item ID，这是第一个条件，第二个条件是它的是否是主图，所以它有一个 set is man。我们肯定是需要主图，所以使用 yes or no，点 yes 点type。好。两个条件都有了以后，就可以去做一个查询。 items 有一个 image map，点 select one，把 record 记录给丢进去，就可以去做一个查询了。查询出来我们直接定义为一个result。OK。 result 拿到以后，我们就可以做一个 return 了。在这边我们来判断一下，判断它是不是为空。如果它不为空，我们就直接返回一个result。点 get u l，也就是图片的一个地址，否则我们就直接返回一个空的字符串就可以了。这个方法我们就已经是写好了， OK 吧。


好，回到 order service，在这边我们也写一下。通过 item service 点 get 主图传入的是商品的ID，这样子我们就可以获得一个 u r l。这是一个 e means u r l 定义好这样的一个字符串。好，OK。在这里我们就已经是把一些基本所需要的数据我们都拿到了。拿到了以后，在这边我们应该要把相关的数据保存到数据库，所以我们应该是写一下，这是 2. 3 循环保存子订单数据到数据库。


写一下，这是 order item。搜一下old， order items 装表，取一个名字，叫做 sub order item，叫这个名字。首先第一个我们应该要存上一个组件， set 一下它的ID。组件和我们上面在使用 s i、 d 的时候是一样的。这个东西拷贝一下，贴到这里，名字取一下，叫做sub。 order ID 拿到了以后，直接往 ID 里面一塞就可以了。


好，塞好了之后，下一个我们应该要去 set 一下他的 old ID，它的主订单所关联的一个 ID 归属订单ID。把 order ID 直接拿过来。 order ID 是在我们的一个循环的上方，也是通过 s i d 去生成的，所以拿到了以后直接往这里面一丢就可以。


去设置的。好。再下一个要设置一下商品的ID，商品 ID 在这里。 item ID 拿过来，好设置。OK，设置好了以后，随后我们要去设置一下商品的相关信息，比方我们会有一个商品的名称，商品的名称通过 item 点get，有一个 item name，直接放进去。好，下一个也是商品的。在这里我们就来筛一下商品的图片，图片就这个也 miss URL，直接拿过来，这样子就行了。好，再下一个。下一个我们要 set 一下它的bycounts，我们前面设死的是唯一，所以把 bycounts 直接写过来就行了。


好，再下一个，点set。现在我们就应该要涉及到一个商品的规格了，商品规格，它有一个规格的id，直接把规格 ID 给写过来。再来一个规格的名称，我们是通过获取的规格对象，点 get name，这样子就行了。还有最后一个价格，千万不要忘记它有一个 set price 价格。在这里面其实我们涉及到两个，有一个是 price normal，还有是一个 price discount。对于我们当前来讲，它其实要放入的是一个最终的支付价格，所以应该是一个 price discount，也就是一个优惠价。OK，所以我们只需要在这里把优惠价写上就可以了。好。当我们这些基本的信息都塞入以后，其实我们就可以去做一个保存了。我们可以通过 order item，我们还没有写，我们应该要注入进来，在我们的头部在注意一下。


好，这样子注入 k 注入OK。以后，在循环以后，我们就可以把子订单的数据做一个循环的保存到数据库里面去就 OK 了。 insert 直接把往这里面 1 设置第三，就可以把这条记录直接插入到咱们的数据库里面去了。这就是一个我们的一个循环循环体，循环结束了以后，在这边我们要还是一样，我们要把两个价格，也就是我们所注掉的这两行，我们直接可以放到下方来。放到下面这两个价格，我们就可以去放进去了。


第一个价格是 total amount 累加的，放在是这里。第二个价格是一个 you are pay amount，真实的一个支付的价格。放到这里。放到这里以后，我们的一个订单基本信息表里面这一条记录所涉及到的相关的数据，全部都已经是 OK 了。 OK 了以后和这里是一样，我们要做一个insert，通过 order Mapper 点insert，把这样的一个由 order 给丢进去，这样子这条记录就可以去进行保存了。


OK，现在我们做了两步操作。第一步操作就是把我们的一个子订单的相关数据做了一个循环的保存，随后一个在死订单。循环。数据保存以后，我们主要是拿到了累加的两个价格，这两个价格我们都是放到订单基本表里面。这张基本表保存完毕以后，其实两张表的数据就已经是有了，主要就是这两张表，订单表和订单商品关联表，这两个数据都 OK 了。

