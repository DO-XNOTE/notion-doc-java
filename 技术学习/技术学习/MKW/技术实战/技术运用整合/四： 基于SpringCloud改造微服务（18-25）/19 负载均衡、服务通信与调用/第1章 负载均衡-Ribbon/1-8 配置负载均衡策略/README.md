---
title: 1-8 配置负载均衡策略
---

# 1-8 配置负载均衡策略

[image](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/d99197ad-575c-426a-9211-7437707d71d5/SCR-20240820-petk.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YW57M3AG%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T225609Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCID9DHYEZHspzwMlf0EJEUvEHMGF0IYOl%2B5AJgjlaXYoMAiEApwEKDpUgUsomsy4RuLIbCVK%2BFhS4unK0AevniNp1KdIqiAQIxv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDIVoSpX2REaH6aN0xyrcAzBHRp9u5rS83YKdPv2hPO4HcVgix9b2RL9gNDZhjQhlFz5rEetuVo9f6Nubhw8YNCJpdywjAP0XsW6rbrv8pymA78EJAXa9MRszGjdObadWZFDtm0%2BBa6opvv5hNlDfm2XYONgjvLUaV4Adpt1n55pzYwPGA%2BqEssAIl03SKvpEgWukdlS2F8YW0giOC8efE6zT7f8j6n4VyAgqIMJlzH420nuCMz2mgK5byxrE2jq5XajSU6IXUrCZOcKH%2BDsPD1jHNYA%2FmKPNHLXqjeqBEJx4Ue%2F391k0apHHlMFprM38u7HOCndTfMHjoXMvSRcxw9mpeq0P7pUICF8GHNGgA4S4Ouod%2FAxtlbrxYAfhiwJqvhXDDyO%2FgLAea%2Fem%2FqxfMq43gbFWpUOg4LkOgaVtUCNlgcLdsAcbEq2DAoYTgTLiTBL%2BkoTvYVyAMIcUapq9AIidrHw19pRyDtK9BLf64ocPsiTud0q59bPOdFJkSbDS7AZ9balYyJsl418ghn42BdX%2BLQKg3AjqAZR8wynsfJWNBKiK%2FgjOwt3fnzyldJf1mbv44HEdXSSbzfNveOR41chnEuysbXe4X5OL9KMiBE54DNLwEWe52y8VX6DJAzHeFbX3%2Fa02dn4KKha%2FMOu5%2F9IGOqUBip92XR9rh62T19LSJIcqrInzS0x9BEMhYtGmRYcPTSb%2BojbeWeLxnAT%2Fvr6mgluoSycOY%2Bnyy2bxaZaylj926X8H7fLnv2es3KfrAM%2BqKRLkDTcme0vQ%2FCZvfYvxy6QTLuvsPDXzQ6CdCMxEJ2jQ7%2FZy6uWt930BH%2BmlmJ%2FmIgr%2BclWHnD%2B%2BI8ca2h%2FnGmQfT0O%2FjTi0u%2FbOzXA2e67UlDniOeQZ&X-Amz-Signature=fbfec811344cf1d089cb94d3b8c4896de430d49781860105401b90b2e5ff3f14&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

[image](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/236a95fc-b6b7-4385-9cea-fc5a71c1c4e8/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YW57M3AG%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T225609Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCID9DHYEZHspzwMlf0EJEUvEHMGF0IYOl%2B5AJgjlaXYoMAiEApwEKDpUgUsomsy4RuLIbCVK%2BFhS4unK0AevniNp1KdIqiAQIxv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDIVoSpX2REaH6aN0xyrcAzBHRp9u5rS83YKdPv2hPO4HcVgix9b2RL9gNDZhjQhlFz5rEetuVo9f6Nubhw8YNCJpdywjAP0XsW6rbrv8pymA78EJAXa9MRszGjdObadWZFDtm0%2BBa6opvv5hNlDfm2XYONgjvLUaV4Adpt1n55pzYwPGA%2BqEssAIl03SKvpEgWukdlS2F8YW0giOC8efE6zT7f8j6n4VyAgqIMJlzH420nuCMz2mgK5byxrE2jq5XajSU6IXUrCZOcKH%2BDsPD1jHNYA%2FmKPNHLXqjeqBEJx4Ue%2F391k0apHHlMFprM38u7HOCndTfMHjoXMvSRcxw9mpeq0P7pUICF8GHNGgA4S4Ouod%2FAxtlbrxYAfhiwJqvhXDDyO%2FgLAea%2Fem%2FqxfMq43gbFWpUOg4LkOgaVtUCNlgcLdsAcbEq2DAoYTgTLiTBL%2BkoTvYVyAMIcUapq9AIidrHw19pRyDtK9BLf64ocPsiTud0q59bPOdFJkSbDS7AZ9balYyJsl418ghn42BdX%2BLQKg3AjqAZR8wynsfJWNBKiK%2FgjOwt3fnzyldJf1mbv44HEdXSSbzfNveOR41chnEuysbXe4X5OL9KMiBE54DNLwEWe52y8VX6DJAzHeFbX3%2Fa02dn4KKha%2FMOu5%2F9IGOqUBip92XR9rh62T19LSJIcqrInzS0x9BEMhYtGmRYcPTSb%2BojbeWeLxnAT%2Fvr6mgluoSycOY%2Bnyy2bxaZaylj926X8H7fLnv2es3KfrAM%2BqKRLkDTcme0vQ%2FCZvfYvxy6QTLuvsPDXzQ6CdCMxEJ2jQ7%2FZy6uWt930BH%2BmlmJ%2FmIgr%2BclWHnD%2B%2BI8ca2h%2FnGmQfT0O%2FjTi0u%2FbOzXA2e67UlDniOeQZ&X-Amz-Signature=029040a09d1183a239a8ceaa6c4ae285140a4032cb517a77057aa79d160d97da&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

[image](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/b60a1ac9-9ee8-42ff-a3e7-7c9767b3c3ee/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YW57M3AG%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T225609Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCID9DHYEZHspzwMlf0EJEUvEHMGF0IYOl%2B5AJgjlaXYoMAiEApwEKDpUgUsomsy4RuLIbCVK%2BFhS4unK0AevniNp1KdIqiAQIxv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDIVoSpX2REaH6aN0xyrcAzBHRp9u5rS83YKdPv2hPO4HcVgix9b2RL9gNDZhjQhlFz5rEetuVo9f6Nubhw8YNCJpdywjAP0XsW6rbrv8pymA78EJAXa9MRszGjdObadWZFDtm0%2BBa6opvv5hNlDfm2XYONgjvLUaV4Adpt1n55pzYwPGA%2BqEssAIl03SKvpEgWukdlS2F8YW0giOC8efE6zT7f8j6n4VyAgqIMJlzH420nuCMz2mgK5byxrE2jq5XajSU6IXUrCZOcKH%2BDsPD1jHNYA%2FmKPNHLXqjeqBEJx4Ue%2F391k0apHHlMFprM38u7HOCndTfMHjoXMvSRcxw9mpeq0P7pUICF8GHNGgA4S4Ouod%2FAxtlbrxYAfhiwJqvhXDDyO%2FgLAea%2Fem%2FqxfMq43gbFWpUOg4LkOgaVtUCNlgcLdsAcbEq2DAoYTgTLiTBL%2BkoTvYVyAMIcUapq9AIidrHw19pRyDtK9BLf64ocPsiTud0q59bPOdFJkSbDS7AZ9balYyJsl418ghn42BdX%2BLQKg3AjqAZR8wynsfJWNBKiK%2FgjOwt3fnzyldJf1mbv44HEdXSSbzfNveOR41chnEuysbXe4X5OL9KMiBE54DNLwEWe52y8VX6DJAzHeFbX3%2Fa02dn4KKha%2FMOu5%2F9IGOqUBip92XR9rh62T19LSJIcqrInzS0x9BEMhYtGmRYcPTSb%2BojbeWeLxnAT%2Fvr6mgluoSycOY%2Bnyy2bxaZaylj926X8H7fLnv2es3KfrAM%2BqKRLkDTcme0vQ%2FCZvfYvxy6QTLuvsPDXzQ6CdCMxEJ2jQ7%2FZy6uWt930BH%2BmlmJ%2FmIgr%2BclWHnD%2B%2BI8ca2h%2FnGmQfT0O%2FjTi0u%2FbOzXA2e67UlDniOeQZ&X-Amz-Signature=5b7195afefbe4aec12955ae1f634f98634f00d640e6c28da951bf7f92c99bbbb&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

hello 慕课网的各位同学们，大家好，这一节我们来学习如何对负载均衡策略进行配置。那本节主要分为两个部分，第一个部分是全局配置，我们将学习如何在整个应用层面配置一个全局负载均衡策略。接下来是为我们指定的一个服务配置负载均衡策略。

[image](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/22a5926c-912e-4a8c-8afc-9c2dc3faee5d/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YW57M3AG%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T225609Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCID9DHYEZHspzwMlf0EJEUvEHMGF0IYOl%2B5AJgjlaXYoMAiEApwEKDpUgUsomsy4RuLIbCVK%2BFhS4unK0AevniNp1KdIqiAQIxv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDIVoSpX2REaH6aN0xyrcAzBHRp9u5rS83YKdPv2hPO4HcVgix9b2RL9gNDZhjQhlFz5rEetuVo9f6Nubhw8YNCJpdywjAP0XsW6rbrv8pymA78EJAXa9MRszGjdObadWZFDtm0%2BBa6opvv5hNlDfm2XYONgjvLUaV4Adpt1n55pzYwPGA%2BqEssAIl03SKvpEgWukdlS2F8YW0giOC8efE6zT7f8j6n4VyAgqIMJlzH420nuCMz2mgK5byxrE2jq5XajSU6IXUrCZOcKH%2BDsPD1jHNYA%2FmKPNHLXqjeqBEJx4Ue%2F391k0apHHlMFprM38u7HOCndTfMHjoXMvSRcxw9mpeq0P7pUICF8GHNGgA4S4Ouod%2FAxtlbrxYAfhiwJqvhXDDyO%2FgLAea%2Fem%2FqxfMq43gbFWpUOg4LkOgaVtUCNlgcLdsAcbEq2DAoYTgTLiTBL%2BkoTvYVyAMIcUapq9AIidrHw19pRyDtK9BLf64ocPsiTud0q59bPOdFJkSbDS7AZ9balYyJsl418ghn42BdX%2BLQKg3AjqAZR8wynsfJWNBKiK%2FgjOwt3fnzyldJf1mbv44HEdXSSbzfNveOR41chnEuysbXe4X5OL9KMiBE54DNLwEWe52y8VX6DJAzHeFbX3%2Fa02dn4KKha%2FMOu5%2F9IGOqUBip92XR9rh62T19LSJIcqrInzS0x9BEMhYtGmRYcPTSb%2BojbeWeLxnAT%2Fvr6mgluoSycOY%2Bnyy2bxaZaylj926X8H7fLnv2es3KfrAM%2BqKRLkDTcme0vQ%2FCZvfYvxy6QTLuvsPDXzQ6CdCMxEJ2jQ7%2FZy6uWt930BH%2BmlmJ%2FmIgr%2BclWHnD%2B%2BI8ca2h%2FnGmQfT0O%2FjTi0u%2FbOzXA2e67UlDniOeQZ&X-Amz-Signature=7706aabeccbd1c09f711c4fb64ab7023429a469aa303618e853f1cbf50860fca&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

 OK 大家看了这两点，应该很容易猜到哪一个优先级更高。我先不剧透。接下来同学通过 demo 中的示例来一起学习。万事俱备，抄几家伙准备开拔，每天 coding 1 小时，健康工作 50 年。同学们，这一节大家将经历一场最为轻松的 demo 为什么这么说呢？因为代码很少。好在 demo 之前我们先要做一些准备工作什么准备工作？来，我们先把尤瑞卡的注册中心给它启动起来。这一节不是要验证负载均衡策略吗？所以我们也要启动多个服务提供者，这样的话才能看出负载均衡有没有生效，对不对我们接下来把 eureka client 启动三个实例。


第一个实例，它的 server port 改成 3 万启动一把，好让他在一旁启动着。我们接下来把这个 server port 改到30,001，再来启动一发好一边呆着去。那我们不管它了，再把 server 炮的改成30,002，我们再启动最后一发三大炮。大家吃过三大炮吗？成都的一个很有特色的小吃在吃之前我还不太敢吃，以为这三大炮是怎么个玩法呢？后来才知道是三个麻团，咚咚咚打到一个板子上发出三声声响，这个叫三大炮。


OK 这三大炮都已经启动好了对不对？接下来我们要做什么呢？我们把 ribbon 启动起来，我们没有指定任何的负载均衡策略，对不对？我们把它启动起来以后，看一看 ribbon 它默认的负载均衡策略是什么？然后我们再有的放矢的改成另外一种负载均衡策略。好， spring 标签成功一半成功启动。那我们这时候打开postman ，这里是调用的 ribbon consumer 这个类，那它调用它什么方法呢？ 


Say hi. 我们主要看什么呢？我们主要看下面这个 response 字比较小，我会给大家同步播报。我们看 response 的其中 this is 后面跟着这个数字，它是什么？它是 eureka client 的 pot 我们来看一看默认的负载均衡是什么。好，第一次调用返回的 port 是30,001，第二次调用返回的 port 是 3 万，第三次调用返回的 pot 是30,002。那接下来我们每次调用发现有没有一个规律，什么规律呢？它这个 POD 永远是30,001，30,002，然后再反复循环，反复循环永远是按照这个顺序，大家知道默认的这种负载循环策略是什么吗？能不能猜到？ round robin roll 对不对？每次轮询一个节点，一个按部就班的往后来调用。那好我们第一步操作先来改全局的负载均衡策略。我们把 round rubbing row 改到什么呢？改到 random row 让它乱序调用，我们来看怎么来改动。


回到页面上，先把负载均衡的应用给它关停，我们这里要动刀子了我要开始变身了。我们先 new 一个方法，你有一个什么方法呢？在这个 configuration 类中的一个方法给它起名叫 ribbon configuration 这是一个类。接着在这个类里面我们要调用一个方法，先把它放大，什么方法呢？ public iro 这是大家第一次见到iro ，对不对？它是什么呢？它是所有负载均衡策略的一个顶级的类，我们给它起名叫 default LB strategy 默认的负载均衡策略，把这个肉引入进来。接下来 return 一个 new random roll 什么都不干。方法上挂一个 bin 这就完事了吗？ no 没有。还有什么，我们叫他 ribbon configuration 是不是就要在这个类上面挂一个 configuration 注解呢？没错，正式这样，我就在 spring 的上下文中创建了一个 random row 那么 raben 在正式启动加载项目的时候，就会使用我声明的这个 row 来替换它默认的 round robin row 好，我们这时候启动来看一下效果，spring标签成功一半。好勒启动起来了。


OK 我们现在回到postman ，我来播报一下它的端口变化，来发起第一次调用它的端口是30,002。第二次调用还是 30,002 看到吗？它没有往后移耶，再调用一次还是30,002。现在又调用了一次，变成了 3 万了。所以说这个 random row 不太靠谱，大家默认还是用 round rubbing row 好，那这里使用 random row 只是为了给大家演示如何来改变负载均衡策略。那这样说明了什么？说明了我们刚才配置的全局负载均衡策略生效了对不对？ OK 那大家记着声明全局负载均衡策略你只用在 


configuration 上下文中声明一个 bin 就好。那大家必须把它加到 configuration 一个类里面吗？可不可以直接在闷方法里面那个类声明当然没问题，我们可以这样做，在当前这个项目的慢方法中所在的这个类直接生命一个 bin 这就好了。


为什么这样可以呢？因为大家看这上面的注解，spring boot application enable eureka client 这些注解里面包含什么呢？我们点进去看一下。这个注解里面包含 spring boot configuration 我们再点进去看。



看到吗？这上面也有个注解叫 configuration 所以说这个注解是一层一层嵌套的。那你在这个类上面加载了这样一个 configuration 所以你在他方法体中声明的 in 是可以被加载进来的。 OK 接下来让我们看一看如何针对一个服务来指定特殊的负载均衡策略。那前面我提到了一个问题，全局的负载均衡策略和针对一个服务的负载均衡策略哪一个优先级更高？哪个同学说全局更高的当然是针对一个服务指定负载均衡策略优先级更高了。那这里有几种针对一个服务配置负载均衡策略的方式呢？甭管它几种，咱先来看第一种，也就是最常见的。



那我们给特定的服务指定负载均衡策略之前，先去怎么样？先去暂时的把刚才配的全局负载均衡策略给它注释掉。 OK 然后再把 ribbon consumer 给关闭，待会我们配置好之后会重启的。好，我们收集小桌板。现在我就来配置一条针对尤瑞卡 client 的负载均衡策略，但它是以什么开头呢？这个配置首先是以 ureka 杠 client 开头，这是什么？这就是服务的 ID service name 对不对？后面跟一个固定的 ribbon 接下来跟一串很拗口很长的属性，名叫 nf load a balancer 接下来是什么？ Role class name. 好，那这一串配置它是一个固定的格式，第一部分永远是 service name 你的服务的名称后面跟 ribbon 在后面跟这个很长的单词。那我们接下来在这里给它配置一个具体的负载进行策略。我们到 configuration 类里面把这个路径给它 copy 回来。我们看这个 random row 把它的路径给借鉴过来。它在这好回去，那用完它了再把它注释掉到这里，把它 copy 过来。 random rowok 那这样我就可以重新再启动 ribbon consumer 我们来看一下这个 role 会不会生效。



好，启动起来了，我们到 postman 里看一下。那我现在来开始方法调用，给大家同步播报接口，第一次调用落在了 3 万这台机器上。第二次调用还是 3 万。那看样子怎么样？这个就是乱序调用了对不对？那说明我们的配置是生效的。好。那大家知道这只是一种配置方式。那还有一种配置方式是什么呢？还有一种配置方式，它跟这个配置文件没有关系，它是通过注解，我们现在去来看一下。
OK 再次回到这个 ribbon configuration 类里面，我们给它配置一个什么注解呢？大家看 ribbon client 这里有很多个注解，大家不要用错了，我们用的是第一个 ribbon client 那点进去看一下它都有什么属性呢？一个 name 和一个 configurationok 那我们第一个先给大家指定一个 namename 是什么？大家能猜到吗？ name 就是我们前面配置的 service ID 对不对？其实这个注解它的作用跟在配置文件里面写上配置是相同的。那所以它也要同步的指定一个 service name 我们这里给它指定 eureka clientok 先把这个 property 给它注释掉接下来是什么？接下来是 configuration 对不对？那它这里面要指定成什么？我们把这个类给 copy 下来，把它的路径 copy 下来。



configuration 里面同样的，它需要指定一个 class 这个 class 是什么？这个 class 就是你需要应用到前面这个服务名称下的负载均衡策略。接下来我们把这个项目启动起来，把它先关停掉，再重新启动一把，看它是不是依然是乱序调用。好， spring 成功一半。走。好嘞好，现在调一把，我来同步播报端口。



第一次调用30,002，第二次调用还是30,002？好赢了。第三次还是 30,002 剩下到了 3 万了。 OK 那说明它还是乱序调用。那我这里再给大家出一个思考题，什么思考题呢？前面我们不是学习了两种配置方式吗？那我想问这两种配置方式哪一种优先级更高来大家知道吗？ OK 那百闻不如一见，我们不妨来做个测试。好了。好，我们现在把这个注解打开，但是它的负载均衡类这个策略我们把它换一下换成什么呢？我们把它换成 roundrobinroll 这两个配置就不同了，对不对？走了不寻常的道路，我们把项目再给它启动起来，大家可以下注哪一个配置优先生效，我赌配置文件，大家说会不会一样？ OK 我们来试一把。


好，现在是第一次调用端口号是 30,002 第二次调用端口号是 3 万，第三次端口号还是 3 万？大家知道了吧，谁赢了？注解胜利对不对是不是注解赢了？ OK 那大家记着你在代码里面配置的这种瑞本 configuration 它的优先级会更高。其实这个机制也有可能跟 property 加载的前后顺序有关。那假设你这个 ribbon client 是后加载的，那是不是就会覆盖掉前面的应用？对不对？


所以项目中很多微小的细微之处都跟什么有关，都跟加载顺序有关。比方说我这里再跟大家抛出一个问题，大家知道这个配置文件有 application.properties 那还有 application.yaml 那大家知道这两个配置文件中哪一个先会被加载，哪一个后会被加载吗？这个同学们需要搞清楚为什么呢？因为你前面加载的一个文件假设需要用到一个属性，而这个属性你不巧正好配置到后加载的那个文件当中。
那这样会怎么样？这在项目启动的时候，那先加载的文件岂不是永远读不到这个属性了？没错，就是这样的。所以我们发现有一些很细微的不容易被察觉的小 bug 正是由于对资源加载文件顺序的不同或者说 spring 对 bin 初始化顺序的不同而导致的。比如说我们经常因为并初始化不同导致 out wire 的失败，或者是拿到了一个空对象。那这就算一个课后小习题了，大家来研究一下 application.problems 和 application.yaml 哪一个加载在线。


我提示，大家最好不要通过百度直接来搜索答案，我们尝试着看一下 springboot 对文件的加载顺序好不好，就锻炼一下大家阅读源代码的能力，也没事自虐一把。那前面我们总共其实介绍了三种不同的配置负载均衡策略的方式，一种是什么？一种是全局负载均衡对不对？另外两种都是针对一个服务配置负载。


均衡。 OK 那我们说了，你这个服务下面。
有不同的接口对不对？那每一个接口它的用途不同，我也想给它配置不同的负载均衡策略。有没有办法呢？这么说就是让大家给方法级别，而不是给一个服务级别来配置负载均衡策略。那给方法配置负载均衡策略怎么办？大家稍安勿躁，这部分的知识，我们把它放到接下来的一个章节进行讨论。在下面一个章节，我们将学习一个叫做 fin 的组件，那他和瑞本是非常好的，两哥俩，他们都有无缝的继承。那不光把这部分知识放到了下一节，我们同时把瑞本的重试也放到了下一节进行讨论。那大家可能会纳闷了，为什么 ribbon 的知识都要放到下一节呢？放到另外一个不同的组件中讨论呢？大家有所不知，当你决定在自己的项目中使用 spring cloud 架构以及尤瑞卡服务治理组件的时候，那基本上 99% 说谦虚一点，10有 89 你会使用 fen 进行服务间的调用。前面我们已经体验了瑞本调用相对于友瑞卡直接调用的简便之处。那么当你使用了 fin 你就会知道原来还有更简单的调用方式，那大家就拭目以待。


好，这一节的内容我们就讲到这里了。下一节我将带大家从源码层面看一看瑞本几种不同的负载均衡策略是怎么来实现的。同学们，我们下期再见。咦还有没有散场的观众朋友吗？恭喜你们，你们等到了彩蛋环节。 OK 那我觉得做一门培训课程不光是要传授知识，更重要的也要传达一些自己的心得、工作中体味道的一些感悟。那我今天就来跟大家稍微聊一聊影响力这个事情。很多做技术的同学真的是一心只读圣贤书，两耳不闻窗外事。咦前面两句好像说反了 never mind 那我打一个比方，一个组里如果有五个程序员，其中四个都是老黄牛，任劳任怨，只干活吃的是草，挤的是奶。那假如第五个同学他并不是那么的任劳任怨，而是怎么样呢？而是在大家每次完成项目的时候，发一封总结性的邮件发给整个公司或者发给他的经理。


那么在经理的印象中，你说谁的影响力更大？大家有可能对这种方式嗤之以鼻，认为它是什么，认为它是拍马屁？如果这个活不是你做的，但是你发出了邮件，这有点像邀功悬赏的意思。很多人不屑于这样干，或者是觉得不好意思，但是这往往真的是扩张自己影响力的事情。


很多同学犯的错误是什么呢？你做了很多的工作，你在背后默默无闻，做了很多的工作，但是没有人知道对不对，这就是自己 sell 自己的一个能力。你要去推销自己的项目，推销自己做了什么，让更多的人怎么样呢？看到你自己的贡献越往上，这个能力越发的重要。


那如果大家真的是像老黄牛一样默默无闻，你只能谁只能期待一个正儿八经，真真正正的伯乐来发现你把你带到聚光灯下。那为何我们不自己走到聚光灯下，自己登上这个舞台，因为真的是千里马常有伯乐部常有能遇到一个非常赏识你能力的上司，是可遇而不可求。很多时候，在大部分情况下，我们都要自己去推销自己，自己去主动的扩张这种影响力。很多同学觉得我程序员听生不善言辞，不善于交际，而且又沉默又内向，其实这是大众给我们这个职业扣上的一顶帽子，我们不要自己往这个套子里面钻当你真正的走到聚光灯下，其实你会发现另外一个自己不可否认，过于内向，过于沉默，确实在职业发展瓶颈上会有那么一点吃亏。


那我们不妨在职业生涯不算太晚的时候，开始重视这个问题，开始有意识的培养这种扩张影响力的能力。这种交际能力，总结性发言、陈词演讲、 presenting 各种各样技术以外的软实力。那随着你的年龄增长，你不再可能在一线中继续承担编码工作，因为国内的情况和国外还是有很大的差距的。我很多国外的同事 50 岁他都可以分散在一线，甚至我之前在一家公司有一位 70 岁的老爷爷，他也是依然在一线写代码。那在国内不可能是这样，你不可能永远沉默的当一个程序员。所以我们更需要这种推销自己的能力，自己主动的走到聚光灯下，勇于表达自己的观点，让更多的人知道你所做出的贡献，不要被害羞，沉默内向。这些词禁锢住自己，不要怕做不好，也不要怕自己做不到。既然我们都能把写代码这么困难的一件事情做这么好，那相信其他事情肯定是不在话下的。


So， please dont be afraid of make a mistake just start to make your voice be heard thats it.
所以也希望大家的努力，在以后能够被更多的人看到，被更多的人赏识。好彩蛋。这里就播放完了，下一节我们再见。

[image](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/68309bca-45fb-470d-a18b-1560f725198a/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YW57M3AG%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T225609Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCID9DHYEZHspzwMlf0EJEUvEHMGF0IYOl%2B5AJgjlaXYoMAiEApwEKDpUgUsomsy4RuLIbCVK%2BFhS4unK0AevniNp1KdIqiAQIxv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDIVoSpX2REaH6aN0xyrcAzBHRp9u5rS83YKdPv2hPO4HcVgix9b2RL9gNDZhjQhlFz5rEetuVo9f6Nubhw8YNCJpdywjAP0XsW6rbrv8pymA78EJAXa9MRszGjdObadWZFDtm0%2BBa6opvv5hNlDfm2XYONgjvLUaV4Adpt1n55pzYwPGA%2BqEssAIl03SKvpEgWukdlS2F8YW0giOC8efE6zT7f8j6n4VyAgqIMJlzH420nuCMz2mgK5byxrE2jq5XajSU6IXUrCZOcKH%2BDsPD1jHNYA%2FmKPNHLXqjeqBEJx4Ue%2F391k0apHHlMFprM38u7HOCndTfMHjoXMvSRcxw9mpeq0P7pUICF8GHNGgA4S4Ouod%2FAxtlbrxYAfhiwJqvhXDDyO%2FgLAea%2Fem%2FqxfMq43gbFWpUOg4LkOgaVtUCNlgcLdsAcbEq2DAoYTgTLiTBL%2BkoTvYVyAMIcUapq9AIidrHw19pRyDtK9BLf64ocPsiTud0q59bPOdFJkSbDS7AZ9balYyJsl418ghn42BdX%2BLQKg3AjqAZR8wynsfJWNBKiK%2FgjOwt3fnzyldJf1mbv44HEdXSSbzfNveOR41chnEuysbXe4X5OL9KMiBE54DNLwEWe52y8VX6DJAzHeFbX3%2Fa02dn4KKha%2FMOu5%2F9IGOqUBip92XR9rh62T19LSJIcqrInzS0x9BEMhYtGmRYcPTSb%2BojbeWeLxnAT%2Fvr6mgluoSycOY%2Bnyy2bxaZaylj926X8H7fLnv2es3KfrAM%2BqKRLkDTcme0vQ%2FCZvfYvxy6QTLuvsPDXzQ6CdCMxEJ2jQ7%2FZy6uWt930BH%2BmlmJ%2FmIgr%2BclWHnD%2B%2BI8ca2h%2FnGmQfT0O%2FjTi0u%2FbOzXA2e67UlDniOeQZ&X-Amz-Signature=8251628ba3c54cf45fadb16bbceb5384f16260e9c59595bda96b9cd6f3a13f5f&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)


