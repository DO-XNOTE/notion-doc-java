---
title: 2-1【技术改造】电商系统集成Config-注册中心搭建和配置
---

# 2-1【技术改造】电商系统集成Config-注册中心搭建和配置

[image](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/61b47622-f31d-44ab-af8f-6e8c182eaa5b/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667M5TZR3J%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T225715Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCNK4wNjSd22dpEPTvmKUJHOKkHZDaz36egi0JWPm%2BI8gIgRkl1gIigCl2NKnxNcAyTy7gMvzkBU%2BbGIwpqrHLln2cqiAQIxv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDFOCc7zB6RI8aVOtlyrcA8geZlkgxy0vf74f93GKH5X3lvpfGcIPLyJliVCLodkanmzfmDPQqv9KwgSlxB3FscggyTvLpJFDoe8cwB%2F2HeVo8JJDDZVgkgWK6f07yO4fow%2F48feURJ%2BW3IpER7ElkAyIU6nsxq09oiYTPDBh%2Bm%2BXYtxf4z7z2%2BynFeKd2%2Fs1IGts3W1MfCX%2B%2BeGMndbPgELOz7vfw8P44fB7SYf3N6h55DCpvXtQMiJ3zsC8gdZ0nKMkHVBr7je%2BJRtztwrusdZzqx%2F6EaRv%2Frl66mXoaKkV5QKDxO2BkI23cB8SKWdIsBqgBR7u9HyvulA5HcEhwx84%2FihOsr360Ac2Wd7boq6YnOppIzT1OJQOrbC%2F4RvBeJxJjG44hWkeZQTo%2Fq4jfdeMp8jidMw3mMbIUyIhSlbpnrpxcMWHbEdquLNgxwtbOhRh5Yaq8KrEzSA4vW5hjUDhCqT%2Bp%2F6ncfdIxCg5vp54%2Fspj6cR4eEEinZBP%2FrpH5HMrtq51osE%2BFgDPxQEBf1riwG0rsHwaHPLLezr9aCPOkA3b8hE%2B3ITDr5Sa1xtnbrDd79t8C0vU%2FSB1sCCou9wRXvbbD2ECf4yEuIdq2Rxn2lSC%2B58N%2BbwlghA0gphUZdgHh25jtcHe6q%2BCMM63%2F9IGOqUB6I62f6Dhz6HmeQydYImljOiwXRgoGFKsTBJ8kk%2FkPd2egITsgOPWBc%2FC1Qf0xBl1Tn4hPzg%2Bf732y4TRPXMQxONh1%2FJKMfuo7%2BnYmEIR7fJ9wDUc0BPEe1EeHJEaxm9eoA4UpLfqmnBGNk9hGqWKGaWoaZO86oa0ZmTKfQ7ojC8AxRIamBw%2Fhv%2B7lEOkf4G0y%2F1ge6rFqUsElac3zzfO87DmHehI&X-Amz-Signature=77b2165e2f4fc507a59e07b590481c49f97753a2cad7be49dca9b04b9cc2c947&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

[image](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/b1bb28c0-4f15-4c63-8192-80e2ba1f16ac/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667M5TZR3J%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T225715Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCNK4wNjSd22dpEPTvmKUJHOKkHZDaz36egi0JWPm%2BI8gIgRkl1gIigCl2NKnxNcAyTy7gMvzkBU%2BbGIwpqrHLln2cqiAQIxv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDFOCc7zB6RI8aVOtlyrcA8geZlkgxy0vf74f93GKH5X3lvpfGcIPLyJliVCLodkanmzfmDPQqv9KwgSlxB3FscggyTvLpJFDoe8cwB%2F2HeVo8JJDDZVgkgWK6f07yO4fow%2F48feURJ%2BW3IpER7ElkAyIU6nsxq09oiYTPDBh%2Bm%2BXYtxf4z7z2%2BynFeKd2%2Fs1IGts3W1MfCX%2B%2BeGMndbPgELOz7vfw8P44fB7SYf3N6h55DCpvXtQMiJ3zsC8gdZ0nKMkHVBr7je%2BJRtztwrusdZzqx%2F6EaRv%2Frl66mXoaKkV5QKDxO2BkI23cB8SKWdIsBqgBR7u9HyvulA5HcEhwx84%2FihOsr360Ac2Wd7boq6YnOppIzT1OJQOrbC%2F4RvBeJxJjG44hWkeZQTo%2Fq4jfdeMp8jidMw3mMbIUyIhSlbpnrpxcMWHbEdquLNgxwtbOhRh5Yaq8KrEzSA4vW5hjUDhCqT%2Bp%2F6ncfdIxCg5vp54%2Fspj6cR4eEEinZBP%2FrpH5HMrtq51osE%2BFgDPxQEBf1riwG0rsHwaHPLLezr9aCPOkA3b8hE%2B3ITDr5Sa1xtnbrDd79t8C0vU%2FSB1sCCou9wRXvbbD2ECf4yEuIdq2Rxn2lSC%2B58N%2BbwlghA0gphUZdgHh25jtcHe6q%2BCMM63%2F9IGOqUB6I62f6Dhz6HmeQydYImljOiwXRgoGFKsTBJ8kk%2FkPd2egITsgOPWBc%2FC1Qf0xBl1Tn4hPzg%2Bf732y4TRPXMQxONh1%2FJKMfuo7%2BnYmEIR7fJ9wDUc0BPEe1EeHJEaxm9eoA4UpLfqmnBGNk9hGqWKGaWoaZO86oa0ZmTKfQ7ojC8AxRIamBw%2Fhv%2B7lEOkf4G0y%2F1ge6rFqUsElac3zzfO87DmHehI&X-Amz-Signature=e45935ec3b6cf29e27236b97b0c80e4f8d036010543f1cf9e8fd032db463ef57&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

的各位同学们，大家好，咱又到了电商项目改造的环节了，咱把整个改造的过程分为了三个步骤。第一步是在 platform 下面搭建了 config server 注册中心。紧接着我们要在一个新的 github 地址配置文件。在这一步当中，我们将会把某些微服务里的配置属性移到咱的 github 文件当中。最后一步，我们就挑选其中的一个微服务模块用户中心来集成咱的配置中心。同学们看完这三个步骤以后，就可以依葫芦画瓢把咱的配置中心集成到其他的微服务模块当中。

[image](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/dbf67d10-3562-47ae-98ad-1c5a099fb7bb/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667M5TZR3J%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T225715Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCNK4wNjSd22dpEPTvmKUJHOKkHZDaz36egi0JWPm%2BI8gIgRkl1gIigCl2NKnxNcAyTy7gMvzkBU%2BbGIwpqrHLln2cqiAQIxv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDFOCc7zB6RI8aVOtlyrcA8geZlkgxy0vf74f93GKH5X3lvpfGcIPLyJliVCLodkanmzfmDPQqv9KwgSlxB3FscggyTvLpJFDoe8cwB%2F2HeVo8JJDDZVgkgWK6f07yO4fow%2F48feURJ%2BW3IpER7ElkAyIU6nsxq09oiYTPDBh%2Bm%2BXYtxf4z7z2%2BynFeKd2%2Fs1IGts3W1MfCX%2B%2BeGMndbPgELOz7vfw8P44fB7SYf3N6h55DCpvXtQMiJ3zsC8gdZ0nKMkHVBr7je%2BJRtztwrusdZzqx%2F6EaRv%2Frl66mXoaKkV5QKDxO2BkI23cB8SKWdIsBqgBR7u9HyvulA5HcEhwx84%2FihOsr360Ac2Wd7boq6YnOppIzT1OJQOrbC%2F4RvBeJxJjG44hWkeZQTo%2Fq4jfdeMp8jidMw3mMbIUyIhSlbpnrpxcMWHbEdquLNgxwtbOhRh5Yaq8KrEzSA4vW5hjUDhCqT%2Bp%2F6ncfdIxCg5vp54%2Fspj6cR4eEEinZBP%2FrpH5HMrtq51osE%2BFgDPxQEBf1riwG0rsHwaHPLLezr9aCPOkA3b8hE%2B3ITDr5Sa1xtnbrDd79t8C0vU%2FSB1sCCou9wRXvbbD2ECf4yEuIdq2Rxn2lSC%2B58N%2BbwlghA0gphUZdgHh25jtcHe6q%2BCMM63%2F9IGOqUB6I62f6Dhz6HmeQydYImljOiwXRgoGFKsTBJ8kk%2FkPd2egITsgOPWBc%2FC1Qf0xBl1Tn4hPzg%2Bf732y4TRPXMQxONh1%2FJKMfuo7%2BnYmEIR7fJ9wDUc0BPEe1EeHJEaxm9eoA4UpLfqmnBGNk9hGqWKGaWoaZO86oa0ZmTKfQ7ojC8AxRIamBw%2Fhv%2B7lEOkf4G0y%2F1ge6rFqUsElac3zzfO87DmHehI&X-Amz-Signature=73b56c66d755176b18d83afd10a2a6eac3054e5316a2899660da40195f21f672&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

那我们转场 intelligi 好嘞，小伙伴们咱操练起来，在这个 foodie cloud 当中我们新建一个毛九，那同学们应该对这个步骤都相当熟悉了。好，我们的 artifact 给它起名字叫 conflict server 朴实无华，不花里胡哨把它放在哪个地方呢？放在 platform 文件夹下面。 platform 321 走。你在这里呢，我们要把需要用到的 dependency 给它加进进来来。那咱一键copy 。三二一走。这里面我们看到它有一个 config server 的 dependency 接下来是 eureka client 这是做高可用用的。最后呢还有 accurator 来做它的端点暴露。

```java
        <dependency>
            <groupId>org.springframework.cloud</groupId>
            <artifactId>spring-cloud-config-server</artifactId>
        </dependency>

        <dependency>
            <groupId>org.springframework.cloud</groupId>
            <artifactId>spring-cloud-starter-netflix-eureka-client</artifactId>
        </dependency>
        <dependency>
            <groupId>org.springframework.boot</groupId>
            <artifactId>spring-boot-starter-actuator</artifactId>
        </dependency>
```

那接下来呢我们是不是还缺少一个启动类，因为咱在这个实战环节当中，这些服务都是需要用架的形式来启动的，最终都要部署容器化的。所以我们这里到注册中心上面来抄个作业了，把注册中心的这个 build 节点，我们给它原封不动地 copy 过来说，原封不动当然还是要改一个名字的，这里的启动类我们把它改成 config server application 那接下来我们就要把这个启动类给它创建出来。


那首先咱们先创建一个包名 come.imock 然后在这下面直接 new 一个 config server application 和咱前面这个 build 节点里面的名字保持一致，名字里面多打了一个 E 把它改一下。 OK 那这个类上面的三个注解和咱在 demo 环节中写的是一样的，一个是 springboard application 加上还有一个我们要 enable config server 配置服务器。最后一个我们作为 eurika 的一个服务提供者来连接到 eurika 注册中心里面做高可用。那它的启动方式，我们从注册中心这里把它原封不动地 copy 过来改一下名字就好。


那咱的启动类创建完了之后，我们在 resources 下面要创建相应的配置属性。那咱创建的第一个文件我们是 bootstrap.yaml 

```java
encrypt:
  key: superNewBee
```

大家知道这里面放什么吗？跟咱在前面 demo 环节中一样，我们先把这个 encryption key 给它放进去。那么这里依然采用对称密钥的形式。在前面的随堂 demo 小结中，给同学们留了一个作业，让大家去自己课后研究一下如何使用非对称秘钥。同学们不知道有没有去把这个作业完成。那完成的同学们就把这里的对称密钥换成自己的非对称加密形式，这样的话安全性更高。


那咱这里对称密钥的这个key ，我们把它叫什么呢？话说咱同学们如今的技术水平和刚刚学习这门课的时候，那真是士别三日当刮目相看相当牛逼。所以咱们这个 key 就把它起叫相当牛逼。好了。当然了不是中文，我们要英文说相当牛逼叫 super 牛逼牛逼 super 牛逼超牛逼，发现这里好像少了一个 2 incorrect 同学们要注意不要拼错，否则你在启动的时候，如果 encrypt 拼错了或者少了这个属性，或者你这个属性文件放到了 application YARN 当中，那它将会报一个错误，会告知你这个加密算法不存在，它会报这样一个错误。


那咱的 boot strap 文件已经创建完成了。那么接下来我们就去创建一个 application 文件，新建一个 application.yaml 这里咱主要配置项和前面 demo 当中是一样的，

```java
server:
  port: 20003

spring:
  application:
    name: config-server

  cloud:
    config:
      server:
        # 属性重载
        overrides:
          test: mytest
        git:
          uri: https://github.com/DO-XNOTE/foodie-cloud-config.git
          force-pull: true
          # 将配置文件放到接入服务名称对应的文件夹下面
          search-paths: '{application}'
#          username:
#          password:


eureka:
  client:
    service-url:
      defaultZone: http://peer1:20000/eureka, http://peer2:20001/eureka
#      defaultZone: http://172.16.136.222:20000/eureka/




# 开启所有 actuator-endpoint
management:
  endpoint:
    health:
      show-details: always
  endpoints:
    web:
      exposure:
        include: "*"
  security:
    enabled: false
```

但是额外多出了几项，跟大家讲讲其他的几个新属性。首先我们要把 spring 的 application 给它添加进去。好， spring application name 那这个 name 你叫什么嘞？ config server 名字不起花哨。配置完之后，我们在 application 同层级的这个缩进行上配置 cloud cloud 节点。下面就是咱的 configconfig 这里我先配置服务器的连接信息。那我们适用哪种形式呢？当然是 git 的形式。那同学们如果感兴趣的话，可以也去尝试其他几种配置形式。比如说我们可以不用get ，可以用本地文件的形式，也是可以加载属性的。


好，那我们这里 guitar 它的 URI 是一个公网的地址，那它坐落在美丽的 github 公网湖畔，那是我用慕课网的邮箱创建的一个新的 github 账号。那他这里我也创建了一个新的项目 foodie cloud config 好，我们就在这里面玩耍。那接下来咱给它配置，强制拉取 okay 这里设置成 true 那它的用户名 username 和 password 那我们这里都可以不用设置，因为我也没有设置这两项。


那接下来我们配置一个 search 那咱这里为什么要设置这个属性呢？因为我们经过微服务改造之后，连接到配置中心的服务会多起来。我们不想让这些服务的配置文件全都混杂在这个 git 上面的第一个层级的文件夹下面，我想把它分门别类的管理好。比如说如果你是订单中心过来的，那你的配置就放在订单中心的文件夹下面，用户中心就放在用户中心下面。所以咱的这个 search path 的我给它设置这么一个属性 application 那我就在这个 git 目录下面对应的 application 这个文件名下面去加载你的配置文件。这样的话我们可以更好地管理不同项目的配置文件。


好嘞，那到这里，咱的连接串就已经配置好了。不过咱在这个 server 节点下还可以再搞一点事情，搞什么事情呢？那在有些业务场景下，可能我从远端拉取到的配置并不是我真正想要的，对不对我想把它强制的 override 给它重载掉。那这种情况怎么办？很简单，咱的这个注册中心允许使用 overrides 这样的一个配置项来覆盖你的属性。那比如说我想指定一个叫 test 那这就是你的属性 key 了，那它的值对应的值我可以给它写成 my test 那如果你在配置中心注册了这样的一个属性，那当你去拉取远程服务的时候比如这里postman ，它就会把你拉取到的属性分为两块，第一块是从远端拉取到的，它在 github 上。那另一块就是它上面的这一块，你看它的 name 叫 overrights 那这里所有的 source 节点下的属性都是你在配置中心里重载掉的属性。 OK 那我们再回来。那我这里给同学们加几个注释，方便回顾一下，属性重在这里的这个 search part 它的意思是将配置文件放到哪呢？放到接入方服务名称对应的文件夹下面。


那这里我们就已经配置好了，接下来还要把谁给拿过来呢？ eureka 注册中心是不是没有给它拿过来啊？那我们就去找一个微服务，比如用户模块的微服务，我们把它的 eureka 注册中心给它拿过来 copy 到这里。那除了注册中心以外，我还要把这个配置中心的服务端点给它暴露出来。好，我们这里从其它地方也把它 copy 一下，咱把所有的端点给它拿过来。然后在咱这个配置中心里给它开启。那到这里是不是万事俱备了？好像还差那么一个谁端点对不对，server的这个 pot 端口。好，那咱看一下这个 platform 下面排错4，它是第几个1234。它是第四个，那我给它端口设置成20,003。好，那到这里，咱的整个配置中心就已经完成了。我们可以这里直接走到它的闷函数这里，然后把它跑一下，看它是不是可以启动成功。


好，稍等半炷香的时间，那我们看到这里已经显示 started 了。好，那我们到 postman 里去发起一个模拟的访问。

[image](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/ce0d510b-c64e-478a-93a2-b1024e11e71e/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667M5TZR3J%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T225715Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCNK4wNjSd22dpEPTvmKUJHOKkHZDaz36egi0JWPm%2BI8gIgRkl1gIigCl2NKnxNcAyTy7gMvzkBU%2BbGIwpqrHLln2cqiAQIxv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDFOCc7zB6RI8aVOtlyrcA8geZlkgxy0vf74f93GKH5X3lvpfGcIPLyJliVCLodkanmzfmDPQqv9KwgSlxB3FscggyTvLpJFDoe8cwB%2F2HeVo8JJDDZVgkgWK6f07yO4fow%2F48feURJ%2BW3IpER7ElkAyIU6nsxq09oiYTPDBh%2Bm%2BXYtxf4z7z2%2BynFeKd2%2Fs1IGts3W1MfCX%2B%2BeGMndbPgELOz7vfw8P44fB7SYf3N6h55DCpvXtQMiJ3zsC8gdZ0nKMkHVBr7je%2BJRtztwrusdZzqx%2F6EaRv%2Frl66mXoaKkV5QKDxO2BkI23cB8SKWdIsBqgBR7u9HyvulA5HcEhwx84%2FihOsr360Ac2Wd7boq6YnOppIzT1OJQOrbC%2F4RvBeJxJjG44hWkeZQTo%2Fq4jfdeMp8jidMw3mMbIUyIhSlbpnrpxcMWHbEdquLNgxwtbOhRh5Yaq8KrEzSA4vW5hjUDhCqT%2Bp%2F6ncfdIxCg5vp54%2Fspj6cR4eEEinZBP%2FrpH5HMrtq51osE%2BFgDPxQEBf1riwG0rsHwaHPLLezr9aCPOkA3b8hE%2B3ITDr5Sa1xtnbrDd79t8C0vU%2FSB1sCCou9wRXvbbD2ECf4yEuIdq2Rxn2lSC%2B58N%2BbwlghA0gphUZdgHh25jtcHe6q%2BCMM63%2F9IGOqUB6I62f6Dhz6HmeQydYImljOiwXRgoGFKsTBJ8kk%2FkPd2egITsgOPWBc%2FC1Qf0xBl1Tn4hPzg%2Bf732y4TRPXMQxONh1%2FJKMfuo7%2BnYmEIR7fJ9wDUc0BPEe1EeHJEaxm9eoA4UpLfqmnBGNk9hGqWKGaWoaZO86oa0ZmTKfQ7ojC8AxRIamBw%2Fhv%2B7lEOkf4G0y%2F1ge6rFqUsElac3zzfO87DmHehI&X-Amz-Signature=155911aa7805b4c633c325fb86c8f6dddd5ca624ec392b89eb0e13b0f5634ef9&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

好，我们去拿 fruity 杠 search 这个服务的配置属性，我们点一下。好嘞，看到这里，已经成功拉取到了 github 上面的属性，因为老师在 github 上面已经偷偷摸摸的创建了一个测试文件。

[image](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/b9c099be-b1ac-4dc4-8dc6-315e32d4a251/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667M5TZR3J%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T225715Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCNK4wNjSd22dpEPTvmKUJHOKkHZDaz36egi0JWPm%2BI8gIgRkl1gIigCl2NKnxNcAyTy7gMvzkBU%2BbGIwpqrHLln2cqiAQIxv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDFOCc7zB6RI8aVOtlyrcA8geZlkgxy0vf74f93GKH5X3lvpfGcIPLyJliVCLodkanmzfmDPQqv9KwgSlxB3FscggyTvLpJFDoe8cwB%2F2HeVo8JJDDZVgkgWK6f07yO4fow%2F48feURJ%2BW3IpER7ElkAyIU6nsxq09oiYTPDBh%2Bm%2BXYtxf4z7z2%2BynFeKd2%2Fs1IGts3W1MfCX%2B%2BeGMndbPgELOz7vfw8P44fB7SYf3N6h55DCpvXtQMiJ3zsC8gdZ0nKMkHVBr7je%2BJRtztwrusdZzqx%2F6EaRv%2Frl66mXoaKkV5QKDxO2BkI23cB8SKWdIsBqgBR7u9HyvulA5HcEhwx84%2FihOsr360Ac2Wd7boq6YnOppIzT1OJQOrbC%2F4RvBeJxJjG44hWkeZQTo%2Fq4jfdeMp8jidMw3mMbIUyIhSlbpnrpxcMWHbEdquLNgxwtbOhRh5Yaq8KrEzSA4vW5hjUDhCqT%2Bp%2F6ncfdIxCg5vp54%2Fspj6cR4eEEinZBP%2FrpH5HMrtq51osE%2BFgDPxQEBf1riwG0rsHwaHPLLezr9aCPOkA3b8hE%2B3ITDr5Sa1xtnbrDd79t8C0vU%2FSB1sCCou9wRXvbbD2ECf4yEuIdq2Rxn2lSC%2B58N%2BbwlghA0gphUZdgHh25jtcHe6q%2BCMM63%2F9IGOqUB6I62f6Dhz6HmeQydYImljOiwXRgoGFKsTBJ8kk%2FkPd2egITsgOPWBc%2FC1Qf0xBl1Tn4hPzg%2Bf732y4TRPXMQxONh1%2FJKMfuo7%2BnYmEIR7fJ9wDUc0BPEe1EeHJEaxm9eoA4UpLfqmnBGNk9hGqWKGaWoaZO86oa0ZmTKfQ7ojC8AxRIamBw%2Fhv%2B7lEOkf4G0y%2F1ge6rFqUsElac3zzfO87DmHehI&X-Amz-Signature=30c4f704f0b365d9b1b4fc7bd05c34ddfe9a22fc293ce8f5f4795afb0f535cc9&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

那到这里，咱的整个配置中心的搭建还有测试工作已经做完了。那接下来我们在下一小节里将带同学们去给 user 这一个微服务模块创建对应的属性文件，把它放到咱这边新创建的 foodie cloud config 项目当中。 OK 同学们，那这一节就到这里结束了，我们下一小节再见。




