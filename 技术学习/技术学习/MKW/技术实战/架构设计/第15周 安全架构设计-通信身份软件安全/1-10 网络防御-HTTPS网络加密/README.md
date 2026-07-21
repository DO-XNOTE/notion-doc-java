---
title: 1-10 网络防御-HTTPS网络加密
---

# 1-10 网络防御-HTTPS网络加密

架起需求到落地的桥梁，构建 it 新蓝图。我是张飞扬，下一个章节我们聊聊 PGP 邮件加密，这个章节，我们来看一看大家更

[image](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/8416c968-3ea4-4b1d-a0ad-61a75446b4c4/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QNGNJOPK%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T231032Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIDPYTAO%2FE9zB9q0wY2sXky9CdNKKe4K0WDt0YWNI%2B%2BA0AiEAm9SeCaXheCDvTuFHkK8gueR4Oq7uIUuJiTwY0d7Q0csqiAQIxv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDPLYpXfrmw526p%2BBmircA3AcQ6xeW0FOAVivM2SjyOk7IrkN%2B%2Brq%2BOrN%2BnrL7RMXGEFT3LPM1M55l%2FqfpUnnE1xF%2BYB5Z8Of9RmedhicoKkt%2FY0snhM5KSlXH3ticcHR5iqjrC58qVR2fW%2FMbkr9CVS4RPz2CtU0Gr1BxRgopyTU0COQ6CeOq1YeO5YiWVSYfYDf0u2K5SaUrf%2FPXjZXHBuW1sbe4M9A3oiHXX72fLW%2BS1Pmep8TiXU%2FpSzwD2ZXi4vpWWvQPLIZGjnU%2Bn3B91aWqAq47BWhd0QmdY1CU84rT2NcT19u0aLPrvyLrQ2UZDsVXdn9hqA5yvjMtRK%2BepH04QfMf4GRNrHvkQmBI1o4bwgvZl3Xi98SoEN99ovIuEC26YV%2Bc7RtXnh5ja%2Bpv1EMXaNWvKy2X5iXGRhxLzDLVfDcHAfaGJvstS14%2FBeVLjEjW0rt5%2Fw8oNKvLbgwQ%2F%2BYBI6jBJdK4LfFYeI%2FzL4MbZe1kLQ3p1a7zLcMDgwPxRcs8QrruzxQJfms1PUJvt%2B0ySrzrHiAV5fOeIcluzqxs31T304JuRyFO9ZpHBJ4azynrC0cpo4siXYyxCuBxCX3jlwC4kasJoVBANYM7%2BZT9hGVko%2F60dQNBIfno464SM%2BUECyn441FDBu1MMO6%2F9IGOqUBMPmlzWAnln1l0Jkls4IZnWsxlqW1MNA1Fsom4R670Oc6NruumHjKP6xuPk9jge%2B8HqG8TNqXagTzMtOnEtVvpM%2BBygdrY4D5vjz2c1O8Iw2XD70IPFA%2Fs3HEcA5YbEiLh0d4vwHbSU2TEbSJozFo7fgPyY%2B2rcmbsmeUd43DkuibYB66yvCh9%2FI89RPGuLwT8qsYa2aldamej8EehyliCnIx9HxW&X-Amz-Signature=6e7f8116621108b5e4bd34c4cd9e2b6557311e31a409705af4c9f80cf0e92d2e&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

耳熟能详的 HTTPS 网络加密。好，那整个章节我通过一张图来跟大家聊网络加密吧。


首先我要拿出一支笔，然后在这里跟大家说一说我们这次要聊的首先是什么？

[image](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/3121dd9e-1369-4a67-b66d-4f30c815a28c/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QNGNJOPK%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T231032Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIDPYTAO%2FE9zB9q0wY2sXky9CdNKKe4K0WDt0YWNI%2B%2BA0AiEAm9SeCaXheCDvTuFHkK8gueR4Oq7uIUuJiTwY0d7Q0csqiAQIxv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDPLYpXfrmw526p%2BBmircA3AcQ6xeW0FOAVivM2SjyOk7IrkN%2B%2Brq%2BOrN%2BnrL7RMXGEFT3LPM1M55l%2FqfpUnnE1xF%2BYB5Z8Of9RmedhicoKkt%2FY0snhM5KSlXH3ticcHR5iqjrC58qVR2fW%2FMbkr9CVS4RPz2CtU0Gr1BxRgopyTU0COQ6CeOq1YeO5YiWVSYfYDf0u2K5SaUrf%2FPXjZXHBuW1sbe4M9A3oiHXX72fLW%2BS1Pmep8TiXU%2FpSzwD2ZXi4vpWWvQPLIZGjnU%2Bn3B91aWqAq47BWhd0QmdY1CU84rT2NcT19u0aLPrvyLrQ2UZDsVXdn9hqA5yvjMtRK%2BepH04QfMf4GRNrHvkQmBI1o4bwgvZl3Xi98SoEN99ovIuEC26YV%2Bc7RtXnh5ja%2Bpv1EMXaNWvKy2X5iXGRhxLzDLVfDcHAfaGJvstS14%2FBeVLjEjW0rt5%2Fw8oNKvLbgwQ%2F%2BYBI6jBJdK4LfFYeI%2FzL4MbZe1kLQ3p1a7zLcMDgwPxRcs8QrruzxQJfms1PUJvt%2B0ySrzrHiAV5fOeIcluzqxs31T304JuRyFO9ZpHBJ4azynrC0cpo4siXYyxCuBxCX3jlwC4kasJoVBANYM7%2BZT9hGVko%2F60dQNBIfno464SM%2BUECyn441FDBu1MMO6%2F9IGOqUBMPmlzWAnln1l0Jkls4IZnWsxlqW1MNA1Fsom4R670Oc6NruumHjKP6xuPk9jge%2B8HqG8TNqXagTzMtOnEtVvpM%2BBygdrY4D5vjz2c1O8Iw2XD70IPFA%2Fs3HEcA5YbEiLh0d4vwHbSU2TEbSJozFo7fgPyY%2B2rcmbsmeUd43DkuibYB66yvCh9%2FI89RPGuLwT8qsYa2aldamej8EehyliCnIx9HxW&X-Amz-Signature=6c4a4d192dbfb6e65117323b25fe5414c72212a51146312fe8c5d19c9bec9086&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

是 SSL 的网络加密。好， SSL 网络加密，那这是什么？这是安全套接词，一个比较传统的 Https 加密方法。那它是怎么来实现的呢？它是什么？一个用户需要去访问一个网站，可能是谷歌，可能是百度，但是你不会把你的数据流直接打到那个网站，而是会什么打到对应的CDN，那这个时候我们就会考虑什么全球有哪几家大的CDN，我们来扳手指了，阿卡马，对吧？Cloudfront，还有 cloud Flare，好，我这里就拿 Cloudflare 在我官网上发布的这样一张 SSL 解释图为例，来跟大家分享一下。


code fly，或者是其他任何的CDN，任何的互联网公司怎么样和我们的用户，和我们的假如客户端来进行 SSL 的握手通讯的，那首先我们的客户端或者我浏览器会什么？会创建一个叫随机码，就是客户的随机码，然后以 hello 的形式发给我们的服务端，那服务端会把这个随机码保留下来，然后会回一个什么服务端的随机码？那这个随机码在回的时候，同时还会告诉我们的客户端我当前主推的公钥是什么？我一张证书里面包含我的主要的公钥，我把证书跟随记码一起发还给我们的用户，也会把这个随机码和这个什么证书保留下来，那这个时候其实我们会有做一个很关键的事情，什么用户要验证这个证书，看看这个证书是不是来自于一些什么 CA 牵出的主链上的一个证书？同时它的有效性是不是还是有效的？是有没有进入什么撤销列表啊？如果没有进入撤销列表，同时是主链签发出来的，可以是主链上的支链签发，也可以是主链本身签发，然后验证一下我们要交流的这个用户实体是不是就是这个证书里面的实体？如果都正确，嗯，那我们就可以信任这张证书。然后怎么样？然后产生第三个随机码啊。


第一个随机码是客户，产生第二个随机码的服务端产生第三个随机码还是由客户端产生，然后把什么，把公钥来加密什么，这个随机码这样的文件就是成为一个加密文件。发给什么？发给我们的服务器，我们的 CDN 厂商，这个时候这个内容即使被什么被黑客所截获也没有关系，因为它没法解出来，只有谁能解出来啊？只有拥有这个私钥的这个 CDN 企业才能够解出其中的内容，当解出其中内容以后，我们的服务端就也有了这样一份，是吧？第三个随机码。


好，第一个随机码，第二个随机码，第三个随机码在客户端完成了，那在服务端也有第一个随机码、第二个随机码和第三个随机码，然后两边同时进行计算，用同样一套规则生成出什么对称密钥，这个对称密钥来自于三个随机秒的综合运算，而它却是什么？不是一个非对称密钥了，这次它是对称密钥了，就是密钥有什么好处？大家还记得吗？运算速度非常快，加解密非常快，所以以后我们在客户和 CDN 之间所有同一 session 的内容全部用什么？用这个对称密钥来进行加密，那这个加密的这个对称密钥如何在进行转达和分发呢？就通过刚刚的什么公钥证书以及对应的公私钥机制来实现，那整个过程当中大家想一想是不是有安全隐患啊？第一个随机数和第二个随机数是在公网传输，是很容易被截获的。


那第三个随机数是什么？通过公司要的离散对数和大数据的质因素分解这样的这个难题来进行保障，那这种保障呢？有时候大家认为还不够，那这时候怎么办呢？有些增强方法，比如迪夫霍尔曼增强，椭圆曲线增强，他们不光有加密，还有通讯协议的增强。通过这些增强，我们可以进一步保护什么密码或者随机数更少的暴露在公网上，还有什么样的增强啊？其实这个协议里面还有一些小小的漏洞，对吧？包含交换的时候握手以及具体的这个数据传输，所以 SSL 发展成1.0、2.0、3.0，到了4.0，它什么举足不前浪，它变成前浪拍死在沙滩上，这个时候出现了 4.0 的替代产品，叫什么？叫 TLS 传输层安全也经历了什么？从 0 到有开始0，1.0，1.1，1.2，那当前最主流的什么？ 1.2 和1.3？这也是我们比较推荐的服务端，尽量采用 1.2 和 1.3 版本来进行沟通，而客户端应该支持 1.2 和 1.4 的通信，那这样情况下我们才能以比较高的安全进行网络的传输。光 1.2 和 1.3 其实还不够。


还有一个情况，什么情况？我们在沟通过程当中似乎没有验证用户，如果你是用户，浏览器也就罢了，因为浏览器可能五花八门。但如果是两个企业和企业之间对团，我的什么，我的是一个服务，你，你也是一个服务。当我要调用你的时候，我既要验证你，你应该也要验证我。这个时候我们就出现了 2.5 步骤一和 2 之后，在 3 之前应该有个2.5，所以 2.5 是什么？是客户端向服务器端发起一个数据，这数据什么共享？一个叫客户端 client 端的什么？我们的证书CC， client 端的certificate，把这个客户端的这个公钥发给服务器端，由服务器端来验证一下我的这个客户端是不是能够跟我通讯，它上面的这个公钥是不是已经过期了？它的这个证书的签发链和它的这个是不是正常啊？所有这些内容验证完了以后，再由服务端或者客户端进行什么第三个随机码的分发，只有当前面两轮 2 和 2.5 全部进行互相验证完以后，这样你们合同的双方才达成一致。


嗯，我信任你，你也信任我，然后不管是服务端还是客户端，随发起的这个什么，最终的这个第三个随机数都会得到什么双方的认可，那这个时候 1233 个随机数才能生成最终的 session key，用这个 key 来做成对称密钥，来进行所有的 HTTP 数据的沟通和安全的保障。


好，这里聊几个概念，一个是SSA，对吧？前浪，一个是TLS，后浪以及 T2S 和 SSI 共同的这种传输协议机制，也就是什么通过公私钥机制来形成握手，最终生成对称密钥，用对称密钥来进行加解密。另外我们还交流了什么？如何让服务器端也进行追加一个验证？客户端的证书是不是什么？是不是可靠？是不是有效？那后面呢？我们会什么？会有一节单独的这个实战章节，来看一下如何用 HTTPS 实现什么双向认证，大家回忆一下在我们的服务网格里是不是有过一个叫 mutual TLS 认证，这其实就是双向的 TLS 的什么 HTPS 安全认证，那个时候是不是很简单的一个配置就能完成所有的功能？那我们用 Java 如何来实现呢？大家敬请期待下一节轻轻松松，简简单单 Java 配置实现双向认证。

