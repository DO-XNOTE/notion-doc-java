---
title: 2-9 Sentinel整合Apollo配置文件解析与ApolloOpenApiClient创建-2 
---

# 2-9 Sentinel整合Apollo配置文件解析与ApolloOpenApiClient创建-2 

[image](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/303dab9b-960f-4311-8365-a86057452002/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665EVIZYOD%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T225846Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIEruZre9AO08wTJwwRq2VutUmmHaVZ2m0OPsV1Yl00vAAiEAmjcaqMJHqxd91m7Do1VJJlifceDn7j4%2BrTFp9Z5LBa0qiAQIxv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDPi46CcF0xDInAEAGircAwCwbRVF1JoeGWrQRmE%2FYS%2B8ZXNe8C8Z4NP%2B4JzemKr8rXW2aBg2VDya1VKG8VdRCFpYp7sOdqUhfsW5x9eeqbzhGDgaAHW7NxNr3B%2F%2FpjTUHytKSjTDKlXSBIChmApD0%2B9lflqhqQA4pW51LrKU1FIr7IC3RryFs5ZGasIqRVg7cmIGUHkm5F5Z8wlnl35%2FdVh7s%2BtoJl7y%2FeRi%2FWe%2FTYT8hG73HdplVBFt6k%2FfiVDYysCjmMsG7tciakqS%2Bi90k40nJyw25aPxWK0gdAg2CNKUUpEP5Pp6wkd1i8%2BxUeeZEFAqz9ZJ3J0NU%2FmS199oURQFGfSmjhW%2Bll7%2FepnkbPazCxNuPjr3ZEDIrxYec4GZqnNnd0L95ZsC4mLbDE%2BA6pDUE3qQp6FFPWtgJx9vJhMZLOADnAvOgQ2R%2B3ymKZup7Zbbz3TuAhdx3x4QcIMolEm6HP3Y0az5Tq%2FOTOPZGzuNuK3HDnatX3UHsIh1PGs3ftU4QJfgAePBR6yG7SPvNPopYHHVAKg35yqVwWPHFL0rdq1a%2F40%2BLaU%2BngsX4CbFY16fK6Yu8%2FZMRVITrkVfZ71jVyv6O8KUGdqnqpx25BsC0IQHTaYAFhYkfPfrZeHGOM9DQrmqaaTrPMiIMP23%2F9IGOqUB%2F060skZKT1Yqv6bVCfTD0R8MT78DAWZKhTzy2Cq57NmSSCnqfpClQ5mk8s5JRik471sJ%2FXSwahlOU%2FOHIvF30tlkES3pv%2BhkNUwz14zTAplvSNSBmn1%2FsN4uYLawb51acWSPJaJPv6ucmBZoRPumWb90IrWn6mh7t78i8lSPgDvjURYmHxLp5BUpn9YOIjlFnS575EdBxPAc%2BEI%2BaLmmLmPYdcdm&X-Amz-Signature=baba0d53b3e370eb04b4415791377a5576f3d699f4c521cc80ae55fea2da7fad&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

[image](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/4ecfcf64-0c77-4384-aea2-47b9b2684850/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665EVIZYOD%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T225846Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIEruZre9AO08wTJwwRq2VutUmmHaVZ2m0OPsV1Yl00vAAiEAmjcaqMJHqxd91m7Do1VJJlifceDn7j4%2BrTFp9Z5LBa0qiAQIxv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDPi46CcF0xDInAEAGircAwCwbRVF1JoeGWrQRmE%2FYS%2B8ZXNe8C8Z4NP%2B4JzemKr8rXW2aBg2VDya1VKG8VdRCFpYp7sOdqUhfsW5x9eeqbzhGDgaAHW7NxNr3B%2F%2FpjTUHytKSjTDKlXSBIChmApD0%2B9lflqhqQA4pW51LrKU1FIr7IC3RryFs5ZGasIqRVg7cmIGUHkm5F5Z8wlnl35%2FdVh7s%2BtoJl7y%2FeRi%2FWe%2FTYT8hG73HdplVBFt6k%2FfiVDYysCjmMsG7tciakqS%2Bi90k40nJyw25aPxWK0gdAg2CNKUUpEP5Pp6wkd1i8%2BxUeeZEFAqz9ZJ3J0NU%2FmS199oURQFGfSmjhW%2Bll7%2FepnkbPazCxNuPjr3ZEDIrxYec4GZqnNnd0L95ZsC4mLbDE%2BA6pDUE3qQp6FFPWtgJx9vJhMZLOADnAvOgQ2R%2B3ymKZup7Zbbz3TuAhdx3x4QcIMolEm6HP3Y0az5Tq%2FOTOPZGzuNuK3HDnatX3UHsIh1PGs3ftU4QJfgAePBR6yG7SPvNPopYHHVAKg35yqVwWPHFL0rdq1a%2F40%2BLaU%2BngsX4CbFY16fK6Yu8%2FZMRVITrkVfZ71jVyv6O8KUGdqnqpx25BsC0IQHTaYAFhYkfPfrZeHGOM9DQrmqaaTrPMiIMP23%2F9IGOqUB%2F060skZKT1Yqv6bVCfTD0R8MT78DAWZKhTzy2Cq57NmSSCnqfpClQ5mk8s5JRik471sJ%2FXSwahlOU%2FOHIvF30tlkES3pv%2BhkNUwz14zTAplvSNSBmn1%2FsN4uYLawb51acWSPJaJPv6ucmBZoRPumWb90IrWn6mh7t78i8lSPgDvjURYmHxLp5BUpn9YOIjlFnS575EdBxPAc%2BEI%2BaLmmLmPYdcdm&X-Amz-Signature=8bca7672831fd5af7955877d473d5de702e3341a2ea21b141ec44862e597d92b&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

[image](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/d00094f0-e037-4a28-9aa8-aee1005a1659/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665EVIZYOD%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T225846Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIEruZre9AO08wTJwwRq2VutUmmHaVZ2m0OPsV1Yl00vAAiEAmjcaqMJHqxd91m7Do1VJJlifceDn7j4%2BrTFp9Z5LBa0qiAQIxv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDPi46CcF0xDInAEAGircAwCwbRVF1JoeGWrQRmE%2FYS%2B8ZXNe8C8Z4NP%2B4JzemKr8rXW2aBg2VDya1VKG8VdRCFpYp7sOdqUhfsW5x9eeqbzhGDgaAHW7NxNr3B%2F%2FpjTUHytKSjTDKlXSBIChmApD0%2B9lflqhqQA4pW51LrKU1FIr7IC3RryFs5ZGasIqRVg7cmIGUHkm5F5Z8wlnl35%2FdVh7s%2BtoJl7y%2FeRi%2FWe%2FTYT8hG73HdplVBFt6k%2FfiVDYysCjmMsG7tciakqS%2Bi90k40nJyw25aPxWK0gdAg2CNKUUpEP5Pp6wkd1i8%2BxUeeZEFAqz9ZJ3J0NU%2FmS199oURQFGfSmjhW%2Bll7%2FepnkbPazCxNuPjr3ZEDIrxYec4GZqnNnd0L95ZsC4mLbDE%2BA6pDUE3qQp6FFPWtgJx9vJhMZLOADnAvOgQ2R%2B3ymKZup7Zbbz3TuAhdx3x4QcIMolEm6HP3Y0az5Tq%2FOTOPZGzuNuK3HDnatX3UHsIh1PGs3ftU4QJfgAePBR6yG7SPvNPopYHHVAKg35yqVwWPHFL0rdq1a%2F40%2BLaU%2BngsX4CbFY16fK6Yu8%2FZMRVITrkVfZ71jVyv6O8KUGdqnqpx25BsC0IQHTaYAFhYkfPfrZeHGOM9DQrmqaaTrPMiIMP23%2F9IGOqUB%2F060skZKT1Yqv6bVCfTD0R8MT78DAWZKhTzy2Cq57NmSSCnqfpClQ5mk8s5JRik471sJ%2FXSwahlOU%2FOHIvF30tlkES3pv%2BhkNUwz14zTAplvSNSBmn1%2FsN4uYLawb51acWSPJaJPv6ucmBZoRPumWb90IrWn6mh7t78i8lSPgDvjURYmHxLp5BUpn9YOIjlFnS575EdBxPAc%2BEI%2BaLmmLmPYdcdm&X-Amz-Signature=d112ebac20c566c4545040128d4023fe1aa2518e29b4122b8b0d4801e838c8f1&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

做完这个事情其实已经大功告成了一半了。另外的一半我们要创建我们自己的什么？我们自己的 clan 端。这 clan 端做什么事情就是阿波罗的那个第三方 API 它还有一个 clan 端。我们在这里比如说搞一个 util 在这里我们叫做阿波罗，然后叫做 config util 我们就搞一个 util 这个类可以。好，这个 util 类比如说它是一个我们可以听为它是一个 final 的 class 这无所谓了。然后这个里边都有什么内容呢？比如说我们可以指定我们自己想要的一些规则，比如说我们先写一些前缀。 Static final string. 这里边我们说 follow 规则，流控规则， follow 杠 ruler 杠 type type 然后等于什么，follow的规则就是follow ，这个前缀的字符串就叫 follow 然后我们再搞一个降级的就好了，这个叫做 degrade 我们暂且就先要这两种规则。其实这两种也是最主要的，一个是流控，一个是降级。然后这里边其实它还需要一个对应的前缀，这个代码我就不写了，后面跟小伙伴们讲清楚就好了。


我现在在这里我直接粘过来，这什么意思？我们最大化，也就是说这个叫做 follow date ID 叫做 post fixed 就是说我这个东西是怎么做的，我是以一个杠加上这个 ruler 加上这个 type 其实它拼完了这个字符串就是这样的，就是杠 follow 杠 rulers 然后这一边其实还有一些内容。然后这个就是 degrade rules 其实我就是为了拼一些规则，就是做一些前缀，就是这些你可以认为这是一半 key 前面这个星就是另一半 key 整个这个 key 是我以后要持久化到阿波罗中的，我们先不去太关注这个事情。然后我们现在我可以把具体的占位符我们先把它做好。这个占位符我们其实可以直接通过这个东西调用，我在这里代码直接粘过来。比如说 get follow data ID 你给我传进来具体的 App 你看我这是两个占位符，SS第一个占位符就是对应的这个 App name 第二个占位符就对应的后面的后缀。


比如说你这个应用服务叫什么？你这个应用服务我们刚才已经注册的应用服务叫做阿波罗杠 test 对不对？这是我们自己的那个应用服务名称，然后我把它 format 获取这个 ID 它的结果是什么呢？它的结果就是这样的。把这一半看见了吧，就是阿波罗杠 test 杠 follow 杠 rules 就这个是一个关于流控的一个规则的 key 当然这个东西没必要按照跟我保持一致，你自己如果有自己的规则，你可以自己加无所谓的。好。然后这个规则就是阿波罗杠 test 杠 degree 的杠欧勒斯，就是获取规则，这些都是无关紧要的。


来我们看一看，比较重要的就是我们如何去获取我们自己的这个 client 在这里我们搞一个静态的方法，这个静态的方法我们可以这样去写，比如说叫做 public static 然后咱们叫做 gray 的阿波罗，阿波罗 open 1x 好了，那我创建一个阿波罗的 client 我需要哪些参数呢？小伙伴们想一想，其实你现在有的只有一个参数，就是你的应用名字 App name 就是你只知道 App name ，其他的你真的不知道，因为我们之前上节课分析的时候，它只给你了这个 App name 然后其实我们可以搞一个 map 把它这个所有的 client 给它缓存起来，这个是不是也可以呢？我们直接搞一个 concurrent map 可以吧，我说 private static 然后 current 哈希 map 这个 key 存的肯定就是 App name ，value存的是什么存的，就是这个阿波罗他的 client test 还是不行。

OK 我们把这个东西把这个 test 去掉就好了。这是 nuckles 这是我把这个 test 去掉就不生效，我把它先注释掉，就相当于我们现在一定要引这个包保存引这个包它现在才有了。


有了之后，然后我们才能找到这个阿波罗克亚特，我们看一下，你看阿波罗克有了，用它这个集合我们要用一个 key value 把它保存起来。然后我们给它起个名字，这个名字就叫做 client map 好吧，就叫做阿波罗 Open API client map 然后等于六一个 concurrent 希 map 搞定。好，这个 map 有了。当然这个 map 它是 static 的，那我给它也大写，那怎么办？我怎么去创建这个 client 呢？那你就得按照它自己的这个 Open API 的这个写法去做了。


首先比如说假设我去创建的时候，我这个已经在 map 里存在了，那我们来看看，想一想这个写法应该怎么去做。假设说我们先从这个 map 里去 get 就是拿过来一个 App name 我们看一看我们能不能取到对应的什么呢？对应的那个对象能取到，直接返回阿波罗。如果说我能取到，那就直接返回，那就是很很简单，就是如果在这里我简单写，如果这个 map 里已经有就不等于空呗，那我直接 return client 就可以了。 else 的情况就是它等于空，我帮它创建一个。


那当然这个肯定得返回，这个创建一个 client 最终应该返回这个 client 其实它不能是 white 那这样的话怎么办？怎么去创建？很简单，你得去拿到 token 然后去创建对不对？所以说我们知道我们这个 token 从哪去取， token 看见了吗？我们之前保存了好几个集合，它其中有一个叫做 token map 就是它那它是一个静态的 static 我们就直接可以通过类直接点出来。那我们就取，因为它里边创建 client 需要几个比较关键的属性。


第一个就是要有图肯我们找到 token map.get 通过什么？这个 key 是什么？ key 肯定是 App name ，通过 App name 看看能不能取到这个 token 为什么我之前是这么装的，是不是通过 App name 为 key 然后 token 为 value 原因就在这，因为我们要取到 token 拿到我们最关键的 token 然后有了 token 之后，你可以判断说 if 如果 token 不等于空的话，是不是 if stringutils 阿巴奇浪包就可以了。 is not blank 是不是？ is not blank 我们的 token 如果它确实是不为空的话，我们的 client 是不是可以创建了 client 就等于我们的点你有一个 builder 然后点这个 API 就很简单了。


然后直接点位置 portal uil 是不是这个 portal uil 也是很好取，我们通过之前那个 config uil 是不是就可以取到？然后点位置 tokentoken 是什么？ token 就是在这里的这个 token 然后点 build 方法，现在通过这个 build 方法一下子就把这个 client 端 build 出来了。而 client 端 build 出来了之后，所以说我们还要把这个东西 put if set 。然后这个 key 什么 key 肯定是 App namevalue 是什么 value 就是我刚才新创建这个 client 我把它直接放到这里边，然后最后 pretend 我们的 connect 就可以了，现在我的代码基本上就写完了，然后 else 的情况下我就直接 return 空就好了，就是你偷看，如果没有的话就 return 空，然后最多就打一个 error 是不是当前 token 为 nut 根据指定的 App name App name 是什么呢？我们在这里就简单去把它包裹起来 App 内幕，然后逗号，根据指定的 App 内幕找不到对应的图片。


好了以后我们再去修改它的时候就简单了，是不是我们接下来的事情可能就是封装一个 service 然后 service 里面再去获取列表的时候，我们直接去调阿波罗克兰特，然后通过这个我们拿到的这个克兰特去访问阿波罗，去拿到我们想要的信息就好了。好了，那么这节课我们主要是对于我们自己的一些 application 解析制定做了一个讲解。下一个我们开始封装我们具体的 service 感谢小收看。





