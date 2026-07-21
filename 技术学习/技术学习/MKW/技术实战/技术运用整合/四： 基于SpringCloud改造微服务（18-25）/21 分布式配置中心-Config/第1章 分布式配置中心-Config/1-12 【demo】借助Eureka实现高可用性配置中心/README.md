---
title: 1-12 【demo】借助Eureka实现高可用性配置中心
---

# 1-12 【demo】借助Eureka实现高可用性配置中心

[image](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/1ebde2d0-35e5-4d85-92e8-ce21b2be9d61/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663KYRCKJ6%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T225710Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIBgiKM%2FEtbebnOyTt53LAL17oEYW918a15xoTYP6pJH1AiEAgPRXafAoFsem5qEQZCDohSvtzOfKjGgNwN21k%2F2B6DAqiAQIxv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDG5triYNP4D%2Fqhol2ircAwchuLB4a6prFU2ENbjUHq%2BM3ciTta9E1fPSuvQDPvCGUtcsHqmoOwHSlTr19MCxqWU11TvuZJXT%2BvvfQSem1Kfmg%2F8twAXCvdOH3YKBSIVBzwfasViDM3K49sAXd7FrlJyzYV2fOsVEFrB82TcnHiCtIlHfId0%2F0MOdoDwGwLtmOBZEBXl%2FfPooiqzX%2FSDCgMPstPdaX4xb4qVTH0sxu22%2FK8GRJwGk26Yj7PuvHex6xrcwp8LoFCGOBurNMq0Qt9X9PeIIvkQaknorRGduUDCIc5wGrmpFtDmO7u9YDqjbVE8%2BLCQ0sRu%2B3A0JV7fxbnQnNV8vfXWXh8sp729KT2LXMrOaa%2FRpDkqW9VAg2xj6ZY95NHFSBH4WH5RspbVFmLBv0ofjPiHnVvc%2FJ1xJlimS2U3KE5x0yHB%2F1kZ70NovF8WcOscWmAKl9V1oPI6AmVSKhEcjJitjv0DupSql5b%2FMT6xVWgFL4WwtLEnsXydnz8%2BiPuI1mZgM5th3rvDj7oJEgWUbnkDVR6%2Fv3nfrv8fEwPs4uQ4GySBB0axKd2KvizBu1js05OIo1p7f6w6A6ylIF4EARrP5Os9zvKoUNDD%2BK1J1rIIZ%2FtbmUxOXWwblYW1wB2xbji8mHCeoML%2B7%2F9IGOqUB1TkxIE8h%2B3EovPrsiAD8NP2OuYsFcm7nnHkeHx7cg6vElfQzj6WWCOsJMkJmGyQE0FMTjSArzKWI0Hc16NfwJZSuBmwACLGJKztIC1qaQFK3N0X9kunMTPYgLdJc%2F%2FAVQpQn0%2F5IRJnDcr2MWDCId6d3zY2eCyq9uGlNteAb7tDIDoTsyA7bAYIyQRQBF5%2FGKd5DSqwNJcfV7AaLEqStifdqxuXT&X-Amz-Signature=8106bfd01d7e3780e070cab33135c6d981bf4cd75774e49da1c534e77cc78625&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

[image](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/42e94e49-3c78-4418-bc3e-90a9be4c2e8c/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663KYRCKJ6%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T225710Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIBgiKM%2FEtbebnOyTt53LAL17oEYW918a15xoTYP6pJH1AiEAgPRXafAoFsem5qEQZCDohSvtzOfKjGgNwN21k%2F2B6DAqiAQIxv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDG5triYNP4D%2Fqhol2ircAwchuLB4a6prFU2ENbjUHq%2BM3ciTta9E1fPSuvQDPvCGUtcsHqmoOwHSlTr19MCxqWU11TvuZJXT%2BvvfQSem1Kfmg%2F8twAXCvdOH3YKBSIVBzwfasViDM3K49sAXd7FrlJyzYV2fOsVEFrB82TcnHiCtIlHfId0%2F0MOdoDwGwLtmOBZEBXl%2FfPooiqzX%2FSDCgMPstPdaX4xb4qVTH0sxu22%2FK8GRJwGk26Yj7PuvHex6xrcwp8LoFCGOBurNMq0Qt9X9PeIIvkQaknorRGduUDCIc5wGrmpFtDmO7u9YDqjbVE8%2BLCQ0sRu%2B3A0JV7fxbnQnNV8vfXWXh8sp729KT2LXMrOaa%2FRpDkqW9VAg2xj6ZY95NHFSBH4WH5RspbVFmLBv0ofjPiHnVvc%2FJ1xJlimS2U3KE5x0yHB%2F1kZ70NovF8WcOscWmAKl9V1oPI6AmVSKhEcjJitjv0DupSql5b%2FMT6xVWgFL4WwtLEnsXydnz8%2BiPuI1mZgM5th3rvDj7oJEgWUbnkDVR6%2Fv3nfrv8fEwPs4uQ4GySBB0axKd2KvizBu1js05OIo1p7f6w6A6ylIF4EARrP5Os9zvKoUNDD%2BK1J1rIIZ%2FtbmUxOXWwblYW1wB2xbji8mHCeoML%2B7%2F9IGOqUB1TkxIE8h%2B3EovPrsiAD8NP2OuYsFcm7nnHkeHx7cg6vElfQzj6WWCOsJMkJmGyQE0FMTjSArzKWI0Hc16NfwJZSuBmwACLGJKztIC1qaQFK3N0X9kunMTPYgLdJc%2F%2FAVQpQn0%2F5IRJnDcr2MWDCId6d3zY2eCyq9uGlNteAb7tDIDoTsyA7bAYIyQRQBF5%2FGKd5DSqwNJcfV7AaLEqStifdqxuXT&X-Amz-Signature=50988de7d52821c4078fc068d2c5c93e3fcbf902d794ce55fb8532ce1cf4efc7&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

[image](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/1afe72e2-c481-4300-b05d-76b5ec0e1fd2/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663KYRCKJ6%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T225710Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIBgiKM%2FEtbebnOyTt53LAL17oEYW918a15xoTYP6pJH1AiEAgPRXafAoFsem5qEQZCDohSvtzOfKjGgNwN21k%2F2B6DAqiAQIxv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDG5triYNP4D%2Fqhol2ircAwchuLB4a6prFU2ENbjUHq%2BM3ciTta9E1fPSuvQDPvCGUtcsHqmoOwHSlTr19MCxqWU11TvuZJXT%2BvvfQSem1Kfmg%2F8twAXCvdOH3YKBSIVBzwfasViDM3K49sAXd7FrlJyzYV2fOsVEFrB82TcnHiCtIlHfId0%2F0MOdoDwGwLtmOBZEBXl%2FfPooiqzX%2FSDCgMPstPdaX4xb4qVTH0sxu22%2FK8GRJwGk26Yj7PuvHex6xrcwp8LoFCGOBurNMq0Qt9X9PeIIvkQaknorRGduUDCIc5wGrmpFtDmO7u9YDqjbVE8%2BLCQ0sRu%2B3A0JV7fxbnQnNV8vfXWXh8sp729KT2LXMrOaa%2FRpDkqW9VAg2xj6ZY95NHFSBH4WH5RspbVFmLBv0ofjPiHnVvc%2FJ1xJlimS2U3KE5x0yHB%2F1kZ70NovF8WcOscWmAKl9V1oPI6AmVSKhEcjJitjv0DupSql5b%2FMT6xVWgFL4WwtLEnsXydnz8%2BiPuI1mZgM5th3rvDj7oJEgWUbnkDVR6%2Fv3nfrv8fEwPs4uQ4GySBB0axKd2KvizBu1js05OIo1p7f6w6A6ylIF4EARrP5Os9zvKoUNDD%2BK1J1rIIZ%2FtbmUxOXWwblYW1wB2xbji8mHCeoML%2B7%2F9IGOqUB1TkxIE8h%2B3EovPrsiAD8NP2OuYsFcm7nnHkeHx7cg6vElfQzj6WWCOsJMkJmGyQE0FMTjSArzKWI0Hc16NfwJZSuBmwACLGJKztIC1qaQFK3N0X9kunMTPYgLdJc%2F%2FAVQpQn0%2F5IRJnDcr2MWDCId6d3zY2eCyq9uGlNteAb7tDIDoTsyA7bAYIyQRQBF5%2FGKd5DSqwNJcfV7AaLEqStifdqxuXT&X-Amz-Signature=490eb49ffbf4cdf8189ef193989367151d7b186997274dde81a6949880342168&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

[image](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/78867f75-cb04-4f32-a39b-ec4baaf0858e/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663KYRCKJ6%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T225710Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIBgiKM%2FEtbebnOyTt53LAL17oEYW918a15xoTYP6pJH1AiEAgPRXafAoFsem5qEQZCDohSvtzOfKjGgNwN21k%2F2B6DAqiAQIxv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDG5triYNP4D%2Fqhol2ircAwchuLB4a6prFU2ENbjUHq%2BM3ciTta9E1fPSuvQDPvCGUtcsHqmoOwHSlTr19MCxqWU11TvuZJXT%2BvvfQSem1Kfmg%2F8twAXCvdOH3YKBSIVBzwfasViDM3K49sAXd7FrlJyzYV2fOsVEFrB82TcnHiCtIlHfId0%2F0MOdoDwGwLtmOBZEBXl%2FfPooiqzX%2FSDCgMPstPdaX4xb4qVTH0sxu22%2FK8GRJwGk26Yj7PuvHex6xrcwp8LoFCGOBurNMq0Qt9X9PeIIvkQaknorRGduUDCIc5wGrmpFtDmO7u9YDqjbVE8%2BLCQ0sRu%2B3A0JV7fxbnQnNV8vfXWXh8sp729KT2LXMrOaa%2FRpDkqW9VAg2xj6ZY95NHFSBH4WH5RspbVFmLBv0ofjPiHnVvc%2FJ1xJlimS2U3KE5x0yHB%2F1kZ70NovF8WcOscWmAKl9V1oPI6AmVSKhEcjJitjv0DupSql5b%2FMT6xVWgFL4WwtLEnsXydnz8%2BiPuI1mZgM5th3rvDj7oJEgWUbnkDVR6%2Fv3nfrv8fEwPs4uQ4GySBB0axKd2KvizBu1js05OIo1p7f6w6A6ylIF4EARrP5Os9zvKoUNDD%2BK1J1rIIZ%2FtbmUxOXWwblYW1wB2xbji8mHCeoML%2B7%2F9IGOqUB1TkxIE8h%2B3EovPrsiAD8NP2OuYsFcm7nnHkeHx7cg6vElfQzj6WWCOsJMkJmGyQE0FMTjSArzKWI0Hc16NfwJZSuBmwACLGJKztIC1qaQFK3N0X9kunMTPYgLdJc%2F%2FAVQpQn0%2F5IRJnDcr2MWDCId6d3zY2eCyq9uGlNteAb7tDIDoTsyA7bAYIyQRQBF5%2FGKd5DSqwNJcfV7AaLEqStifdqxuXT&X-Amz-Signature=8c742171da91d76a1244249b736cd2532dac4382e6890c8c63ced930b43c936d&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

hello 慕课网的各位同学们，大家好，那我前一节吹出去的牛，这一节就要把它实现。咱这一节干什么我们借助 eureka 来实现 config server 的高可用架构。

[image](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/7fceead3-7210-4595-848c-b38f516a47d2/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663KYRCKJ6%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T225710Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIBgiKM%2FEtbebnOyTt53LAL17oEYW918a15xoTYP6pJH1AiEAgPRXafAoFsem5qEQZCDohSvtzOfKjGgNwN21k%2F2B6DAqiAQIxv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDG5triYNP4D%2Fqhol2ircAwchuLB4a6prFU2ENbjUHq%2BM3ciTta9E1fPSuvQDPvCGUtcsHqmoOwHSlTr19MCxqWU11TvuZJXT%2BvvfQSem1Kfmg%2F8twAXCvdOH3YKBSIVBzwfasViDM3K49sAXd7FrlJyzYV2fOsVEFrB82TcnHiCtIlHfId0%2F0MOdoDwGwLtmOBZEBXl%2FfPooiqzX%2FSDCgMPstPdaX4xb4qVTH0sxu22%2FK8GRJwGk26Yj7PuvHex6xrcwp8LoFCGOBurNMq0Qt9X9PeIIvkQaknorRGduUDCIc5wGrmpFtDmO7u9YDqjbVE8%2BLCQ0sRu%2B3A0JV7fxbnQnNV8vfXWXh8sp729KT2LXMrOaa%2FRpDkqW9VAg2xj6ZY95NHFSBH4WH5RspbVFmLBv0ofjPiHnVvc%2FJ1xJlimS2U3KE5x0yHB%2F1kZ70NovF8WcOscWmAKl9V1oPI6AmVSKhEcjJitjv0DupSql5b%2FMT6xVWgFL4WwtLEnsXydnz8%2BiPuI1mZgM5th3rvDj7oJEgWUbnkDVR6%2Fv3nfrv8fEwPs4uQ4GySBB0axKd2KvizBu1js05OIo1p7f6w6A6ylIF4EARrP5Os9zvKoUNDD%2BK1J1rIIZ%2FtbmUxOXWwblYW1wB2xbji8mHCeoML%2B7%2F9IGOqUB1TkxIE8h%2B3EovPrsiAD8NP2OuYsFcm7nnHkeHx7cg6vElfQzj6WWCOsJMkJmGyQE0FMTjSArzKWI0Hc16NfwJZSuBmwACLGJKztIC1qaQFK3N0X9kunMTPYgLdJc%2F%2FAVQpQn0%2F5IRJnDcr2MWDCId6d3zY2eCyq9uGlNteAb7tDIDoTsyA7bAYIyQRQBF5%2FGKd5DSqwNJcfV7AaLEqStifdqxuXT&X-Amz-Signature=4aa691100052bd79f79289ae2475e20c96ed68eb04e1e9e498375cdedeb81fb0&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

这一节的内容不多，主要有两个部分，第一部分是 config server 要向注册中心报道，所以咱要把 eurika 组件集成到 config server 中。这一步完成了以后，接下来咱要让 config client 从注册中心获取 config server 的地址。大家还记得之前咱搭建 config calendar 的时候，是不是写死了一个注册中心的URI 。那这里不能这样做了，咱先要把 eureka 也集成到 config client 中，所以我们要对配置文件进行那么一点小小的改造。 OK 大家如果准备好的话，跟我移步到 intelligi 我们开工编程，使我快乐。


996 是我的福报，咱这里创建一个新的毛九，为什么不在原先上面直接修改，因为咱要和这种单中心的节点划清界限，这样也方便同学们回顾之前学过的内容。我们的 artifact 名称叫 config server 杠 eurika 证明它是一个和 eurika 集成过的 config server 点击 next 毛球 name 和前面保持一致，然后文件夹把它放到 config 下面，点击 finish 321 出来了。


好，现在添加dependency ，咱这里就简化了，直接从前面的应用中把这个 config 的 server 的 dependency copy 过来，然后再添加一个 dependency 就好了。是谁？ eureka 对不对？其他都不需要。咱 eurika 从哪里copy ，随便找一个 eureka 的应用，从这里面把 dependency copy 一下好，再复制回来。


接着给 packaging 指定成价的模式，实际上大家也可以通过哇的模式来启动，但是一般 spring boot 的应用我们还是通过加的方式启动比较好，这样比较标准。 OK 那接下来来一个 main 方法，但是创建 main 方法以前来一个 package 叫 calm.imock.spring cloudok 嫩方法从哪里来，从其他项目里面直接 copy 过来就可以了咱这里方法名称就不变了，直接原样的打过去。Ok.那咱这个方法上面的高帽子是不是要给它多带一顶带谁当然就是注册中心了。


enable discovery client OK 好，这一步完成以后，咱接下来就是配置文件了。那么配置文件我们依然从其他项目中先给他 copy 过来，然后再改吧，改吧就可以了。 application.yaml copy 过来。好， copy 过来以后，咱要对它做一番修改，先改谁把这个 name 要改掉对不对？咱现在分家了，自立门户叫 config server eurekaok 那还有其他的要改的吗？ server 的port ，咱把这个 6 万改成 6 万 E 除了这个以外，我们还要添加 eureka 的地址之前都是用 application.properlist 写的注册地址，然后这里把它是 YAML 的格式重新打一遍 eureka client 再回车，然后打上 service URL 这里有一个比较容易犯错的地方，大家记着这是 service URL 可不是 server URL 。如果你打了 server URL 的话，那么它在启动项目的时候尝试连接注册中心是连不上的，因为它会认为你这个节点没有声明，因为你节点名称给错了。然后 eureka 就会尝试使用默认的配置，也就是 local host 的 87 几的一个端口来尝试访问注册中心，那其实是访问不到的了。
所以这里一定要注意不是 server URL 是 serviceok 再回车，紧接着跟 default zone 然后注册中心的地址要打在这里，咱从其他项目中 copy 一下，大家也有使用 properties 的经验，也有 YAML 的经验同学们觉得哪种方式更加直观简洁一些我个人其实更喜欢是使用 properties 的方式，我觉得 YAML 形式更加适合那种有很多相同前缀的属性在一块的情况。


什么意思，我来打个比方，比如说这里如果你这个除了 default zone 以外，咱还有很多同级的属性。比如这里是一个 A 接下来是一个 B 那么你就会发现通过 YAML 形式配置相当简洁明了对不对？那假如你前面的前缀重复率不高，也就是说你这里是 eureka client 那你下个属性就是 ribbon client 再下个属性是 high strikes client 这时候你就会发现整个 YAML 文件配置会特别长，拉得非常长，几个屏幕都拉不完。但是大家如果用properties ，那就短短几行就可以给它声明出来，所以还是看情况啦。两种配置方式各有利弊，萝卜白菜各有所爱。你喜欢御姐，我喜欢萝莉，大家只要适合自己的就是最好的。不过话说回来，年轻的朋友们用 YAML 的比例好像更高一些。那我们追逐潮流，也用 YAML 了。那咱这里配置文件也配置完了，代码也写完了。


接下来怎么啊？要启动项目来试一下了。那我们先要把 ereca server 给它启动起来，找到 eureka server 的 main 函数，我们这里直接执行。然后等 server 启动起来以后，我们再回到刚才创建的 config server eureka 项目中，直接在闷方法上把它也给启动起来，看他像 URI 卡注册中心注册是否会成功。看到 spring 成功一半往下走，看到一个 started 好，我们的项目已经成功注册了。 OK 那我们到浏览器上看一下。好，我们这里刷新一下。


OK 刷新好以后，大家可以看到这里的 config server eureka 已经注册上去了。好，那接下来咱要配置谁了？咱要让我们的 config client 直接连上我们刚才创建的 config server eureka 看是不是可以拉取到最新的属性。这里总共要改几步，其实只要两步。那咱还记得之前搭建的 config client 它并没有基于 eureka 做服务发现对吧。所以第一步必然是怎么样到 palm 文件中把 eureka 的 dependency 给它加进去。好，我们这里从其他的 eureka 项目中，比如 eureka consumer 项目里，把这个 dependency 先给它 copy 过来。大家 copy 的时候记得要 copy eureka client 这个dependency ，不要靠错了 copy 成 eureka server 那个不起作用的。Ok.那这里把 eureka dependency copy 进去以后，接下来该改哪个代码了？不着急，大家排好队，一个一个来。


接下来改的应该是我们的启动类，那我们找到它的启动类 config client application 好，这里只有一处改动是什么？把 ereca 的服务发现添加上去对吗？ enable discovery client OK 最后一步我们要到配置文件中做一点小修改。好，打开 bootstrap.yaml 这里我们主要改动的部分集中在这一块儿，也就是 string cloud 下面的 config 节点答案。


注意到这个 config 节点当中，我们是通过这个 URI 来拉取配置文件的。从这个后面跟着的 HDD B 路径，它其实是一个写死的 URL 的单节点，它并不是一个注册中心上面拉取到的服务。 okay 咱怎么对它进行改造呢？先把它给注掉，手起刀落，

```java
spring:
  application:
    name: config-client
  cloud:
    config:
      name: config-consumer  # 它能覆盖掉你 application name 中声明的这个名称。那我们这里给它起名叫 config consumer
#      uri: http://localhost:60000
      discovery:
        enabled: true
        service-id: config-server-eureka
      profile: prod
      label: master


server:
  port: 61000


myWords: ${words}  # words 是github上的属性
management:
  security:
    enabled: false
  endpoints:
    web:
      exposure:
        include: "*"
  endpoint:
    health:
      show-details: always
```

把它先拿下，然后在这边添加一个属性叫 discovery 看到这个属性名称，大家应该就能猜到它是跟服务发现有关的。 discovery 添加上去以后，我要先把它打开，让这个服务发现功能生效。这样 config 组件就会通过 eureka 的服务发现尝试着去拉取配置文件。


OK 接下来 config client 如何通过注册中心拉取服务呢？我们这里要把 config server 的 service ID 配置进来，这样的话我们的服务节点就知道从哪一个对应的服务才能获取到正确的配置文件了。 OK 那接下来的 service ID 如何声明？我们先来打上一个节点，它就叫 service 杠 ID 有的同学可能又把这个 service 打成了 server 那么它启动的时候可是会报错的。大家留心一下这个 service ID 是谁呢？那就是 config server 杠 eurekaok 它就是我们在 eureka 注册页面上看到的这个 application name 也就是 service ID 咱配置好了 service ID 以后是不是还缺了一个什么内容啊？咱这不是基于友瑞卡的服务发现吗？友瑞卡在哪？还没有配置好，我们打开小桌板到前面已经配置好的 server eureka 的配置文件当中。把这一段 eureka 相关的配置给它 copy 一下。好，然后回到原先的文件这里见缝插针，把它给随便 copy 到一个空白的地方。我这里插个对，把它放在这里。


OK 那配置文件改完了，代码也写完了，我们接下来就尝试着去启动一下这个项目，看一看能否获得正确的属性。好，我们走到闷函数里，直接把这个项目 run 起来，好看到 spring 成功一半。Ok.这里大家是不是会看到有那么一点点不同，通常咱是先看到 spring 标签，然后才看到有一些 log 说是去尝试着服务注册了。那么咱在这个项目中他是先注册了服务尝试去注册服务，然后再看到了一把 spring 标签乾坤大挪移顺序会变。 OK 再往下我们看到这行 log fetching config from server 那这里配置的这个 IP 地址是从哪获取的？这就是从注册中心上获取到的 IP 地址。 OK 再往下，直到看到最后有一个 started OK 说明这个项目已经启动起来了。你说就启动起来了吗？我不信，那接下来咱去 postman 里实际的去调用一把就知道了，我们来看它的端口是61,000。好，那我走到 postman 里。好，那我发起一个请求，获取 github 上的 words 这个属性发送。 OK 大家看到，这个属性值已经返回回来了。
God bless you and me ok.


搞可用改造完美成功。咱这里实际上只启动了一台 config server 那在真实的生产环境中肯定会起多个 instance 来提供服务的。这一节到这里就快要结束了，我来总结一下我们接着上一节提到的高可用改造方案。在这一节当中，将 eureka 集成到了 config server 以及 config client 当中。那其中最核心的部分，就在 config client 中的 bootstrap YAML 配置文件当中。我们稍加回顾一番，之前是通过 URI 写死的一个服务器端口和地址来访问的。那么这里咱引入了一个新的节点 discovery 然后通过 service ID 来进行访问。

[image](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/2864e3ac-8b8f-4086-af82-4a11d6707c42/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663KYRCKJ6%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T225710Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIBgiKM%2FEtbebnOyTt53LAL17oEYW918a15xoTYP6pJH1AiEAgPRXafAoFsem5qEQZCDohSvtzOfKjGgNwN21k%2F2B6DAqiAQIxv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDG5triYNP4D%2Fqhol2ircAwchuLB4a6prFU2ENbjUHq%2BM3ciTta9E1fPSuvQDPvCGUtcsHqmoOwHSlTr19MCxqWU11TvuZJXT%2BvvfQSem1Kfmg%2F8twAXCvdOH3YKBSIVBzwfasViDM3K49sAXd7FrlJyzYV2fOsVEFrB82TcnHiCtIlHfId0%2F0MOdoDwGwLtmOBZEBXl%2FfPooiqzX%2FSDCgMPstPdaX4xb4qVTH0sxu22%2FK8GRJwGk26Yj7PuvHex6xrcwp8LoFCGOBurNMq0Qt9X9PeIIvkQaknorRGduUDCIc5wGrmpFtDmO7u9YDqjbVE8%2BLCQ0sRu%2B3A0JV7fxbnQnNV8vfXWXh8sp729KT2LXMrOaa%2FRpDkqW9VAg2xj6ZY95NHFSBH4WH5RspbVFmLBv0ofjPiHnVvc%2FJ1xJlimS2U3KE5x0yHB%2F1kZ70NovF8WcOscWmAKl9V1oPI6AmVSKhEcjJitjv0DupSql5b%2FMT6xVWgFL4WwtLEnsXydnz8%2BiPuI1mZgM5th3rvDj7oJEgWUbnkDVR6%2Fv3nfrv8fEwPs4uQ4GySBB0axKd2KvizBu1js05OIo1p7f6w6A6ylIF4EARrP5Os9zvKoUNDD%2BK1J1rIIZ%2FtbmUxOXWwblYW1wB2xbji8mHCeoML%2B7%2F9IGOqUB1TkxIE8h%2B3EovPrsiAD8NP2OuYsFcm7nnHkeHx7cg6vElfQzj6WWCOsJMkJmGyQE0FMTjSArzKWI0Hc16NfwJZSuBmwACLGJKztIC1qaQFK3N0X9kunMTPYgLdJc%2F%2FAVQpQn0%2F5IRJnDcr2MWDCId6d3zY2eCyq9uGlNteAb7tDIDoTsyA7bAYIyQRQBF5%2FGKd5DSqwNJcfV7AaLEqStifdqxuXT&X-Amz-Signature=b7bfc4357ad083e136bf0bd78f76d566c3a9020f4f587c8ca0d1f476982c6c11&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

[image](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/90cb7080-5732-430a-86ae-af89d6a3abae/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663KYRCKJ6%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T225710Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIBgiKM%2FEtbebnOyTt53LAL17oEYW918a15xoTYP6pJH1AiEAgPRXafAoFsem5qEQZCDohSvtzOfKjGgNwN21k%2F2B6DAqiAQIxv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDG5triYNP4D%2Fqhol2ircAwchuLB4a6prFU2ENbjUHq%2BM3ciTta9E1fPSuvQDPvCGUtcsHqmoOwHSlTr19MCxqWU11TvuZJXT%2BvvfQSem1Kfmg%2F8twAXCvdOH3YKBSIVBzwfasViDM3K49sAXd7FrlJyzYV2fOsVEFrB82TcnHiCtIlHfId0%2F0MOdoDwGwLtmOBZEBXl%2FfPooiqzX%2FSDCgMPstPdaX4xb4qVTH0sxu22%2FK8GRJwGk26Yj7PuvHex6xrcwp8LoFCGOBurNMq0Qt9X9PeIIvkQaknorRGduUDCIc5wGrmpFtDmO7u9YDqjbVE8%2BLCQ0sRu%2B3A0JV7fxbnQnNV8vfXWXh8sp729KT2LXMrOaa%2FRpDkqW9VAg2xj6ZY95NHFSBH4WH5RspbVFmLBv0ofjPiHnVvc%2FJ1xJlimS2U3KE5x0yHB%2F1kZ70NovF8WcOscWmAKl9V1oPI6AmVSKhEcjJitjv0DupSql5b%2FMT6xVWgFL4WwtLEnsXydnz8%2BiPuI1mZgM5th3rvDj7oJEgWUbnkDVR6%2Fv3nfrv8fEwPs4uQ4GySBB0axKd2KvizBu1js05OIo1p7f6w6A6ylIF4EARrP5Os9zvKoUNDD%2BK1J1rIIZ%2FtbmUxOXWwblYW1wB2xbji8mHCeoML%2B7%2F9IGOqUB1TkxIE8h%2B3EovPrsiAD8NP2OuYsFcm7nnHkeHx7cg6vElfQzj6WWCOsJMkJmGyQE0FMTjSArzKWI0Hc16NfwJZSuBmwACLGJKztIC1qaQFK3N0X9kunMTPYgLdJc%2F%2FAVQpQn0%2F5IRJnDcr2MWDCId6d3zY2eCyq9uGlNteAb7tDIDoTsyA7bAYIyQRQBF5%2FGKd5DSqwNJcfV7AaLEqStifdqxuXT&X-Amz-Signature=f61a9fc07636c995c4865996cfacc02e160c4b81c37ab7d007f6c746fe92242e&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

好，那么这一节的内容就到这里结束了。下一节我带大家一起展望一下未来，让大家了解一下总线式架构有什么改造方向。听到总线式架构，大家可能不是太明白是什么意思。我这里跟大家举一个例子，比如说你有一个 1000 台服务器的集群，它们都使用了动态属性刷新，按照咱这一章学到的知识，每个机器访问一遍 activated refresh 接口来刷新它的属性攒一台两台。还好说这 1000 台可不是手工就可以完成的，它要使用一种总线式的架构，通过某个服务组件来批量通知到所有需要变更的节点。 OK 好，下集预告到此结束，多的内容我就不剧透了。同学们，我们下一节再见。





