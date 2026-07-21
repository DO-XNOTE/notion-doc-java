---
title: 1-8 网络防御-VPN
---

# 1-8 网络防御-VPN

架起需求到落地的桥梁，构建 it 新蓝图。我是张飞扬，上一节我们聊了聊 IDS IPS 入侵的检测和防御。

[image](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/064a890e-2a10-4032-a0ad-e6409f422f3f/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466Z4J2HG4I%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T231031Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIH9JkIzf6OnYwZOAmmsTLleRYpNCYRtmuG0bt1dVfTKUAiEAsBXANpSbMif18AkudNfifcgTfNd4Q6Ih3OSegOuoREoqiAQIxv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDHC1Kzj0nNf7hoWlXircA1%2BARKcKZIpVRZq%2FWVUZeuYo50WaEresZgPA6wzVwLpekYwR92NB7yDxj6A1Ak4kUDFTwq1f5%2BoWDWCdegV4D2G4LMB49VC%2BgM2dhUUS9g9J2ROlQEDfA2fB4%2FojH9Doj9lxlqEPik0r73CRTiMUNz8WKw1VWGBUTqN6S2b857Qfae9XT4QcZyPW7kJoL%2BMj4m40xWmWF8tjPGlgF2Xj7X6AxcELACCI%2ByL5vPBI9VjzXIAY4RWbJ%2FPSm8SCayOo1bzq2vumQNPc8gEWJ4v7Kih42pTrA4x8JUjvA2ig4KvrFDUUmvN8HoopaYdK2c1vuGRY4cnscodurOomGHQmBgNtPPWFIl56vw7GXY4RrxldCyLDV5QE07qQ27tXahwRVG5eZXdRbYAR1LP1roDSTxhkZ5giu8AbHiWQB4KJeJvQqgoGJb2qU6fdmipGyJNuLBy2ln5nI0MFxmHdP%2BleDYPPvs0O3d2UvpDjf4x%2FRmk5VEz3v%2BszFT4KnNLr63QrzVTz%2BVrU8X7RhMHETSWnaMa4G%2F2bEpfoKoOMsZt%2Bo1x9p6PDOUSciYLlNA0KFjPr1LtZ%2BkL6JAt1acv7qHXDKSHKF8MaX4A4v%2F7PEB%2BasngLeISkpGz4sSMsjXx6MKC4%2F9IGOqUBaQOa5qF8QgG%2F9m%2BTRUxPWkiSwmc3OZiamaBlcrpLGT1KXDq1KFWpyl%2FlR0%2F%2FI8NkhFQEzsyFcosLqAJMtk6ItvX8cIvP3PcGYMviYyqyzYOw6Rq41lNHmiSf1BEd5sUmV9THuOyqkrm1LytUg3yvI6IvwgwgrZWBEOU9BtQiYWnLhkF6LgonrAHCfr91LQgmXV9Lqev8GycaUk94ZFyLgXLPA%2F7M&X-Amz-Signature=1a1bac32f68d3b4d966f2f8c4a49459f35d38ff6d56b5061adab9145c4f95b31&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

那这一节我们来聊一聊另外一种网络的防御技术，VPN，通过安全的隧道的加密来实现端到端、点到点的通信安全。好，那讲 VPN 我们要首先讲讲它的应用场景，那相信呢？最近什么新冠期间，很多小伙伴都在家办公，那在家办公你如何去连接办公网络？如何去连接生产开发测试网络呢？

[image](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/74397545-655e-496b-a80a-afd3ff12fb37/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466Z4J2HG4I%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T231031Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIH9JkIzf6OnYwZOAmmsTLleRYpNCYRtmuG0bt1dVfTKUAiEAsBXANpSbMif18AkudNfifcgTfNd4Q6Ih3OSegOuoREoqiAQIxv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDHC1Kzj0nNf7hoWlXircA1%2BARKcKZIpVRZq%2FWVUZeuYo50WaEresZgPA6wzVwLpekYwR92NB7yDxj6A1Ak4kUDFTwq1f5%2BoWDWCdegV4D2G4LMB49VC%2BgM2dhUUS9g9J2ROlQEDfA2fB4%2FojH9Doj9lxlqEPik0r73CRTiMUNz8WKw1VWGBUTqN6S2b857Qfae9XT4QcZyPW7kJoL%2BMj4m40xWmWF8tjPGlgF2Xj7X6AxcELACCI%2ByL5vPBI9VjzXIAY4RWbJ%2FPSm8SCayOo1bzq2vumQNPc8gEWJ4v7Kih42pTrA4x8JUjvA2ig4KvrFDUUmvN8HoopaYdK2c1vuGRY4cnscodurOomGHQmBgNtPPWFIl56vw7GXY4RrxldCyLDV5QE07qQ27tXahwRVG5eZXdRbYAR1LP1roDSTxhkZ5giu8AbHiWQB4KJeJvQqgoGJb2qU6fdmipGyJNuLBy2ln5nI0MFxmHdP%2BleDYPPvs0O3d2UvpDjf4x%2FRmk5VEz3v%2BszFT4KnNLr63QrzVTz%2BVrU8X7RhMHETSWnaMa4G%2F2bEpfoKoOMsZt%2Bo1x9p6PDOUSciYLlNA0KFjPr1LtZ%2BkL6JAt1acv7qHXDKSHKF8MaX4A4v%2F7PEB%2BasngLeISkpGz4sSMsjXx6MKC4%2F9IGOqUBaQOa5qF8QgG%2F9m%2BTRUxPWkiSwmc3OZiamaBlcrpLGT1KXDq1KFWpyl%2FlR0%2F%2FI8NkhFQEzsyFcosLqAJMtk6ItvX8cIvP3PcGYMviYyqyzYOw6Rq41lNHmiSf1BEd5sUmV9THuOyqkrm1LytUg3yvI6IvwgwgrZWBEOU9BtQiYWnLhkF6LgonrAHCfr91LQgmXV9Lqev8GycaUk94ZFyLgXLPA%2F7M&X-Amz-Signature=a091e03823d279fc51c4766c55a2e5ac0913692a01a575eb412fa1e7a9e10350&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

自然是使用 VPN 的全称，其实什么是一个虚拟的私有网络，对吧？ Virtual private network，这个网络给你感觉什么？好像你就连着公司网络，就连着生产中心，完全是独有的，独享了一根链路连过去，但本质上其实你用的是什么互联网，并没有独享，但这种感觉独享哪里来呢？就来自于什么点对点的协议。所以 VPN 套路再多，其实总体思想就一个，就是 p to p 点对点。


那最传统的一种点对点协议叫 p p t p 点对点的隧道协议。它的实现方法就是基于 IP 上面，我们实现一个隧道某一个 IP 地址到另外一个 IP 地址，直接实现一个独有的数据连接，那这个数据连接里面所有的信号采用一些特殊的身份验证技术，不管你是用户名密码，还是用户名口令，还是用户名什么 token 等等，只要这种身份验证在两端形成一个默契，这个时候你的笔记本就可以跟数据中心的某一个跳板机实现一个点对点的隧道连接。


所谓你知我知，这个信令你知道我也知道我们形成一个数据连接，通过传统的加密技术，比如像 SSL 或者是 TLS 一些加密的方式实现整个信道的安全，那这种点对点技术有很大的缺陷，就是只能用在 TCP IP 的 IP 网络上，那到了后面我们会发现什么？很多的远端传输，尤其是城与城之间，比如像上海跟北京跟天津之间，在这种网络中心有些时候走的不是IP，在链路层和网络层，他们走什么真中计系统，所谓真中计落地就叫 ATM 或者叫 X. 25 这种协议相对于 TCP IP 的 IP 层和底层的这个链路层来说，它的传输速率更快，效率更高、浪费更少，所以在城与城之间是一个主流的方法。但是 PPTP 是没法穿越 IP 的，所以一旦碰到这种真踪迹传输就没辙了。那什么样的方法能在这种混编的跨城市通讯当中实现VPN？它就需要 l two t p 在二层形成一个隧道，不管你在二层上面实际上是ATM、 IP 还是 X. 25 等等方式都可以进行轻松应对。


但是这样的方案其实应用也不多，当前最常见的应用是什么？是在四层和三层上面实现VPN，四层 VPN 是特点，就是什么？四层的 VPN 特别安全，特别轻快，所有数据全部加密，不管是采用 SSL 或者是 TLS 加密，而且它的传输效率非常高。但是它有一个缺点，它是四层，这个四层而且选的是什么？是 HTTPS 的四层。所以所有上面的通讯必须要支撑HTTPS，比如像收邮件，比如像打开网页，这些协议是可以支持 4 层 VPN 的。但是如果你要采用远程桌面，跳到一个 Windows 机器去登录生产系统，或者采用 SSH 去登录一个开发测试系统，在这种 VPN 情况下是没法使用的，所以此类 VPI 一般性用于什么？一般性用于大佬们 CU CTU 连接公司网络，做一些非常安全的 VPN 的邮件收发、网页访问，那这个时候他们会单独架设一套 4 层 SS LTLS、四层 VPI 给这些大佬们使用。但我们的工程师、我们的架构师、我们的小伙伴们平时用的最多的是哪种啊？是下面这种最常见的 VPN IP SEC VPN。


这个 VPN 是形成一个什么点对点的三层协议，就是网络层协议，

[image](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/b4b188da-d06b-4fb1-b65b-e9c84ac31dc2/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466Z4J2HG4I%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T231031Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIH9JkIzf6OnYwZOAmmsTLleRYpNCYRtmuG0bt1dVfTKUAiEAsBXANpSbMif18AkudNfifcgTfNd4Q6Ih3OSegOuoREoqiAQIxv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDHC1Kzj0nNf7hoWlXircA1%2BARKcKZIpVRZq%2FWVUZeuYo50WaEresZgPA6wzVwLpekYwR92NB7yDxj6A1Ak4kUDFTwq1f5%2BoWDWCdegV4D2G4LMB49VC%2BgM2dhUUS9g9J2ROlQEDfA2fB4%2FojH9Doj9lxlqEPik0r73CRTiMUNz8WKw1VWGBUTqN6S2b857Qfae9XT4QcZyPW7kJoL%2BMj4m40xWmWF8tjPGlgF2Xj7X6AxcELACCI%2ByL5vPBI9VjzXIAY4RWbJ%2FPSm8SCayOo1bzq2vumQNPc8gEWJ4v7Kih42pTrA4x8JUjvA2ig4KvrFDUUmvN8HoopaYdK2c1vuGRY4cnscodurOomGHQmBgNtPPWFIl56vw7GXY4RrxldCyLDV5QE07qQ27tXahwRVG5eZXdRbYAR1LP1roDSTxhkZ5giu8AbHiWQB4KJeJvQqgoGJb2qU6fdmipGyJNuLBy2ln5nI0MFxmHdP%2BleDYPPvs0O3d2UvpDjf4x%2FRmk5VEz3v%2BszFT4KnNLr63QrzVTz%2BVrU8X7RhMHETSWnaMa4G%2F2bEpfoKoOMsZt%2Bo1x9p6PDOUSciYLlNA0KFjPr1LtZ%2BkL6JAt1acv7qHXDKSHKF8MaX4A4v%2F7PEB%2BasngLeISkpGz4sSMsjXx6MKC4%2F9IGOqUBaQOa5qF8QgG%2F9m%2BTRUxPWkiSwmc3OZiamaBlcrpLGT1KXDq1KFWpyl%2FlR0%2F%2FI8NkhFQEzsyFcosLqAJMtk6ItvX8cIvP3PcGYMviYyqyzYOw6Rq41lNHmiSf1BEd5sUmV9THuOyqkrm1LytUg3yvI6IvwgwgrZWBEOU9BtQiYWnLhkF6LgonrAHCfr91LQgmXV9Lqev8GycaUk94ZFyLgXLPA%2F7M&X-Amz-Signature=300281270447c92f3c6b4556b4cd20cc65160665b5925a32fb7109014c458f41&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

在上面你可以用 SSH 去登录Linux，也可以用 Windows 远程桌面，也可以用什么 MySQL 的协议去什么连接一个数据库，也可以用什么 MQTT 的方法去连接一个物联网做消息队列的传输？什么方法都可以，只要你是基于 IP 以上的所有协议，都可以在这个通道上，这个VPN、 IPC 这个通道上进行传输。


同时这个通道还有两大模式，左边这张图里面就是两大模式，上面那个模式叫 transport mode 传输模式，适合于什么？点到点，平时我们笔记本上装的 VPN 就是这个模式。它只适合于你本笔记本去连什么对端的一个跳板机，然后再连到对方的办公室或者是数据中心。那这种情况下它有一套特殊的连接，这个连接就是两个点之间能够非常安全的进行加密的，有身份验证的传输。


那如果是公司的办公室和公司的数据中心，用的是哪种VPN？应该是左下角的VPN，叫做隧道模式，它会把办公室里面，比如说 1, 000 多台笔记本或者是台式机通过一个特殊的key，这个 key 就是隧道的加密key，进行一个特殊的加密，所有数据走一个互联网，但这个互联网感觉像是走这个专有网络一样，连到了什么生产中心的一个特殊的这个解密机，最后会把数据包发给你，希望发给了各台什么服务器？各台我们的这个开发测试机，那在这个两个 key 服务器之间走的是一套什么隧道模式的？ IB 赛克 VPN 这种模式最常见就是办公网络和生产网络，或者是开发测试中心和我们的生产中心。如果你没有钱租赁一套独有的光纤通道，那很可能就走的是下面这种隧道模式的VPN。


好，这两种模式还分别有两种什么具体的实现手段？所以 IPC VPN 其实说简单也简单，说复杂也复杂，它是 2* 2 = 4 种不同的方式，我们看一下这四种方式该如何真正的落地实现，以它的核心原理好，到了这张图其实有点复杂了，付杨老师不得不拿出我的什么我的红笔来跟大家说说谎话。


好，首先看一看这个名称左边叫什么？叫 a h AH 是什么？ authentication head 身份验证头部的简称。

[image](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/62172e21-d4a7-405e-9d69-43efded8b380/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466Z4J2HG4I%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T231031Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIH9JkIzf6OnYwZOAmmsTLleRYpNCYRtmuG0bt1dVfTKUAiEAsBXANpSbMif18AkudNfifcgTfNd4Q6Ih3OSegOuoREoqiAQIxv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDHC1Kzj0nNf7hoWlXircA1%2BARKcKZIpVRZq%2FWVUZeuYo50WaEresZgPA6wzVwLpekYwR92NB7yDxj6A1Ak4kUDFTwq1f5%2BoWDWCdegV4D2G4LMB49VC%2BgM2dhUUS9g9J2ROlQEDfA2fB4%2FojH9Doj9lxlqEPik0r73CRTiMUNz8WKw1VWGBUTqN6S2b857Qfae9XT4QcZyPW7kJoL%2BMj4m40xWmWF8tjPGlgF2Xj7X6AxcELACCI%2ByL5vPBI9VjzXIAY4RWbJ%2FPSm8SCayOo1bzq2vumQNPc8gEWJ4v7Kih42pTrA4x8JUjvA2ig4KvrFDUUmvN8HoopaYdK2c1vuGRY4cnscodurOomGHQmBgNtPPWFIl56vw7GXY4RrxldCyLDV5QE07qQ27tXahwRVG5eZXdRbYAR1LP1roDSTxhkZ5giu8AbHiWQB4KJeJvQqgoGJb2qU6fdmipGyJNuLBy2ln5nI0MFxmHdP%2BleDYPPvs0O3d2UvpDjf4x%2FRmk5VEz3v%2BszFT4KnNLr63QrzVTz%2BVrU8X7RhMHETSWnaMa4G%2F2bEpfoKoOMsZt%2Bo1x9p6PDOUSciYLlNA0KFjPr1LtZ%2BkL6JAt1acv7qHXDKSHKF8MaX4A4v%2F7PEB%2BasngLeISkpGz4sSMsjXx6MKC4%2F9IGOqUBaQOa5qF8QgG%2F9m%2BTRUxPWkiSwmc3OZiamaBlcrpLGT1KXDq1KFWpyl%2FlR0%2F%2FI8NkhFQEzsyFcosLqAJMtk6ItvX8cIvP3PcGYMviYyqyzYOw6Rq41lNHmiSf1BEd5sUmV9THuOyqkrm1LytUg3yvI6IvwgwgrZWBEOU9BtQiYWnLhkF6LgonrAHCfr91LQgmXV9Lqev8GycaUk94ZFyLgXLPA%2F7M&X-Amz-Signature=46811540551cc992356d677695d82f07fe36203f5287427cc640698cbaff0326&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

这是一种什么？在数据包前面加头部来进行安全通讯的方法。那 ESP 叫什么？叫 ecapsullation security payload 封装有效载荷，所谓封装就是头尾封装，是在数据包的头跟尾加安全字节来进行什么 VTN 传输的好，我们看一看 ah 的图画在左边普通的一个包是不是这样一个数据包？有，前面有个 IP 头部，然后就在什么网络层进行传输了？但是如果我是点到点的 EPN 通讯怎么样？我在数据包前面会加一个绿颜色叫 a h head，这个 head 里面会有数据包的完整验证信息， CIC 验证信息也会有一个额外的数据签名。那前面什么我们在数据的这个安全架构里面聊过的签名方法，在这里就会用到了，签好名以后就防止抵赖，防止这个其他人伪造。同时在签名过程当中它会加一个特殊的什么序列号编码，那这个编码叫什么？防止重放？就前面包子铺的故事，当别人抓到这个包以后，再发给对端的 VPN 服务器，他会发现，嗯，这个序列号用过了，你这是重放攻击，我就会直接拒绝，所以防止重放。


所以 a h 有很多种不同的效果，那加完 ah 以后，最后还是用 IP 包的形式进行封装，然后发送，这就是点对点的什么 ah 形式形成的 IP SEC VPN？那如果你是办公网络和生产网络之间是隧道模式怎么样呢？他就先把你的网络包原封不动的放在那里，然后在外面也加一个 ah head，然后再加一个 IP 头，最终形成一个 IP 的包。


那本质上来看这两个模式，其实大家不用关心下面那个隧道模式，因为平时我们 VPN 是不是都是电脑对电脑或电脑对系统啊？所以这个模式注意看数据包旁边加一个头，这个头里面有各种各样的验证就可以了。好，这就是 a h 模式。那同样道理，我们来聊一聊什么 ESP 模式，就是我们刚刚说的什么所谓封装，就是在数据的前面加上个头，在尾巴上加上个尾巴。同时我们要把什么这里看到没有？封装的本质含义就是加密。我们把数据跟它的尾巴一起加密了，然后最后在最后面再做一些一个数据的签名验证，对吧？哈希，在什么公司要加密？这就是签名。


最终做完签名验证以后，把整个包前面再加个 IP 头部，然后发送出去，这种模式是也是要大家深刻理解的，这个模式其实最常见的VPN，为什么？因为前面的 a h 模式你没有数据加密，也就是说中间传输的所有数据是明文传输，是不是很夸张啊？这个完全不安全，所以大部分的什么IPCC、 VPN 都是采用这种数据加密头尾校验的方式。


如果你感觉这种方式有缺点是有的，它是什么？它不能防止重放攻击，那怎么样呢？你把两个方法组合起来啊？菲亚老师公司的这个 VPN 就是这样的，既是 ah 又是ESP，也就是 IP 地址后面是有 ah 的head， ah header 防止重放，之后再是 ESP 的 header 和加密完的 data 跟 ESP 的尾巴以及最后的 ESP 校验这种最佳安全点对点实现全链路完全封装的。


什么 VPN 是很多公司，特别是什么跟金融跟互联网相关的公司的传统 VPN 套路。但如果你是办公网络，你就可以采用这种 ESP 加上 a p 的组合方式，也就是数据先加 IP 地址，然后用 e s b 进行加密封装。头位封装完以后再加上 ah head，最后再加上一个什么IP，头部形成一个数办公网络到数据中心的完整的封闭式的加密，防止用户什么嗯，重放，防止身份伪造等等的黑客行为。


好，这就是最强大的什么隧道模式的VPN。好，聊完了好几种不同的什么 IP 赛克的实现，我们再回过去想一想，传统的 p to p l to p，再加上 IP second，再加上 4 层的什么SSL，加上 TLS 的VPN，是不是共同构成了我们丰富多彩的 VPN 接入方式啊？嗯，果然不错，这些方式都能有效的防止黑客攻击，充分攻击，对吧？身份的伪造保护我们点到点，端到端的数据安全。好，聊完了数据的传输安全，下一节我们来聊一聊邮件安全怎么样？发一个邮件到对端，保证所有的数据是安全的、加密的、可信的，大家敬请期待。

