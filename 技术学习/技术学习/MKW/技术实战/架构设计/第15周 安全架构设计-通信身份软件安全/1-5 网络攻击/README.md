---
title: 1-5 网络攻击
---

# 1-5 网络攻击

架起需求到落地的桥梁，构建 it 新蓝图是张飞扬。好，上一节我们聊一聊 CDN 这个土地公，那这节呢？

[image](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/e843130e-1920-4f49-9727-eea60d4df4ed/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466THPFFQFN%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T231029Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIApYD2k3mx%2FQDGI4TAKm%2F7Oa%2F46PRAlf0WyWxx378qoHAiBrbaM7e%2FTHm7MU2u9XgUUDEgIihn7nz%2FcFWYV4j0ratyqIBAjG%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMzKM20yS6syEnGJCiKtwDbO%2B58u7CqluTQolgswKr8Y5eIsnxWq5LGx2ppt46oXNnV3BoTWFP4lbF%2FFNxGKwimbiQQut3K1Fy350i05H2TO5LgW9e3Pr%2BtMAkfflMWuuv85LuAs2VoqazVu52FdoagPKdFm%2FfEau2QC5yD8rKPaYMFqB%2BfTR%2Bx5WXS5lJ142%2FIGPRXa9r%2BiZIKwnyRmct%2FosUniNxbAaqqhLNlwS39KJtoz55PBLpu7vNCj9lF35FDaRVM7KX9U1QuRh%2BM%2FoC47P9bsjqC86bCibcTDMBYEqC84wVuvBIpx15MtJZBzim9emnx1ZN62rIrgqtkYsEHpkb4jgPEkrxhPcrq16rtTdsorjio8qu0kRBaSm0PFtMKojNRswgkLCzeHUpLagC9PizzcNVrdiyz4TFZzjVJmj8OIEslacQWtLQIDC6IkkrR4SWVN2CMSc0mgEfp8WJDjJPBoYcGkFnS%2Fq3SXV7KnD4QX88TA%2F%2FRqY%2B36D1LyeHIbwm%2FfP9ynXEJHR2R0PgxvPVMbw%2BH1quAy%2F6%2FB9ynhdmQ5j42CDbTyYm2DQGKSViacupPYceSCx0JHxGOzOG%2FDjzW0Dd%2FaEOA%2Ftuc4KX9TiCtbTLuF0nzidQ6UQi6SgLxPOYZFMAQN%2BxZyowgbj%2F0gY6pgFhZro%2B5DCKT3jgMeQO6SJgrYTmCq8Mw57H%2FFBjkUD5HpV3qUuUQIHYhCtrTH4DSghW4XEKlLAIqZKPofYF4FFCJDfsBJqTSkF81zp23k8YHXXsrBBJ2w2vzCVYvhm%2BCT9BTPhjUTbrGK9a74cGGElkeHcY1Kz6GM4EGYlOl6MKAkNqZoV0jY8H8u%2F4VYz498sqASQkh3XIAhUY9mgljlwHtiTKrsIH&X-Amz-Signature=fbf60df5e937e9a12cdb7d010a563018f35305b3c9d4d27a36fd6b5831a71d84&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

我们开始来聊一聊攻防两端。首先从网络攻击开始，我们会尝试介绍几款经典的网络层的攻击，第一个就是  DOS Deny of service 拒绝服务攻击。

[image](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/42e4ed28-3d6e-4c85-b467-7c39bf8795c9/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466THPFFQFN%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T231029Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIApYD2k3mx%2FQDGI4TAKm%2F7Oa%2F46PRAlf0WyWxx378qoHAiBrbaM7e%2FTHm7MU2u9XgUUDEgIihn7nz%2FcFWYV4j0ratyqIBAjG%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMzKM20yS6syEnGJCiKtwDbO%2B58u7CqluTQolgswKr8Y5eIsnxWq5LGx2ppt46oXNnV3BoTWFP4lbF%2FFNxGKwimbiQQut3K1Fy350i05H2TO5LgW9e3Pr%2BtMAkfflMWuuv85LuAs2VoqazVu52FdoagPKdFm%2FfEau2QC5yD8rKPaYMFqB%2BfTR%2Bx5WXS5lJ142%2FIGPRXa9r%2BiZIKwnyRmct%2FosUniNxbAaqqhLNlwS39KJtoz55PBLpu7vNCj9lF35FDaRVM7KX9U1QuRh%2BM%2FoC47P9bsjqC86bCibcTDMBYEqC84wVuvBIpx15MtJZBzim9emnx1ZN62rIrgqtkYsEHpkb4jgPEkrxhPcrq16rtTdsorjio8qu0kRBaSm0PFtMKojNRswgkLCzeHUpLagC9PizzcNVrdiyz4TFZzjVJmj8OIEslacQWtLQIDC6IkkrR4SWVN2CMSc0mgEfp8WJDjJPBoYcGkFnS%2Fq3SXV7KnD4QX88TA%2F%2FRqY%2B36D1LyeHIbwm%2FfP9ynXEJHR2R0PgxvPVMbw%2BH1quAy%2F6%2FB9ynhdmQ5j42CDbTyYm2DQGKSViacupPYceSCx0JHxGOzOG%2FDjzW0Dd%2FaEOA%2Ftuc4KX9TiCtbTLuF0nzidQ6UQi6SgLxPOYZFMAQN%2BxZyowgbj%2F0gY6pgFhZro%2B5DCKT3jgMeQO6SJgrYTmCq8Mw57H%2FFBjkUD5HpV3qUuUQIHYhCtrTH4DSghW4XEKlLAIqZKPofYF4FFCJDfsBJqTSkF81zp23k8YHXXsrBBJ2w2vzCVYvhm%2BCT9BTPhjUTbrGK9a74cGGElkeHcY1Kz6GM4EGYlOl6MKAkNqZoV0jY8H8u%2F4VYz498sqASQkh3XIAhUY9mgljlwHtiTKrsIH&X-Amz-Signature=5865735fc841ed7122a231340bbb754ac6d567c7f42aae5e9036a69fbc24adad&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

其实在前面的c、d、 n 我们其实已经聊到了什么？很多的 d DOS，那这 d DOS 呢？其实是 DOS 的衍生，那什么是DOS？ DOS 就是什么让你变成 access denied，也就是让你的整个服务器没法再为用户提供任何的访问服务了，这就是 DOS 攻击的目标，也就是破坏你服务的可用性。


那如何破坏呢？有几种常用手段，一种手段叫机型数据包。那大家都知道 PIN trace root 用的是哪个协议？ ICMP 协议，那这个协议里面有个要求，就是正常的包长度是什么？是一个正常的 int 型 65535 的长度，但是黑客会怎么样？会发一个 65536 的长度来尝试一下，看看你的后台系统是不是能够正常处理越界的这种 ICMP 包。


如果一旦你没法正常处理，它就会用利用这种漏洞，种种的漏洞来破坏你整个服务器的正常运行，导致最后你的服务器被打瘫掉。那除了这种攻击以外，还有一种叫泪滴攻击，也是一种很畸形的爆。我们知道在 TCP 数据的层次，我们很多的时候是进行分片处理的，一个很长的数据包在 TCB 层会分片，分片完了以后在接收层会根据 TCP 的协议重新重组成上层的应用层，数据包在重组过程当中，如果出现一些畸形包，这些包分片的很奇怪，没法重组成功，这个时候我们程序员就会挠头发，对吧？一直挠挠挠，把头发挠光为止，当服务器也在挠头发的时候，很容易把自己挠瘫了。那这也是一种攻击手段，因为一些很奇怪的类型的包，导致你没法把什么分片重组成功。


看看你服务器怎么样对异常进行处理，如果你处理的不合适，会占用大量的内存， CPU 最终会导致整个系统宕机，这是畸形包，那除了畸形包以外，还有一种叫做泛鸿攻击，也有人叫它宏泛攻击，其实都是英文单词 flooding 洪水的简称。那这种攻击方法有好几种具体的实现，比如说通过 TCP 的握手来实现。通常客户端发起握手势，发一个 sync 包，然后服务器端回一个 think 和什么ACK，那最后我们的什么客户端要再回一个ACK？但是黑客是这样的，他是永远只发 think 不回 ACK 的。


所以给服务器的感觉是什么？嗯，不停的有用户来尝试跟我进行 TCP 连接，但是每次连接了一半就中断了，这个时候你不能等他 time out，你不能去等他 time out，因为永远不可能有 time out 发生，因为黑客可能在瞬间就会发起几千万个这种 think 泛红攻击，导致在你 10 秒钟 1 分钟 time out 之前已经把整个服务器的什么整个 TCP 连接的总数给用光了，这个时候你的服务器就崩溃了。所以对于这种很奇特的大量 think 的方法，必须要有一个手段来及时进行防御。


那同样的道理，每台服务器要去查自己的什么自己的 IP 地址的时候是会去发一个 DHCP 的请求，嗯，我们的网关能不能给我分配一个 IP 地址啊？那这一台机器这样发没问题，但如果有成百上千台机器同时要求申请 IP 地址，有可能会把网关给打瘫掉，那一样的道理。


AR P 就是什么？我们的 IP 地址跟 Mac 地址之间的映射？每台物理机其实都是通过 Mac 地址进行沟通的，而不是IP。当你需要去映们 IP 到 Mac 的时候，会发一个 AIP 的包，那这个包不停的发送的时候会导致什么？导致我们的网关没法正常的给出对应的 Mac 地址，因为 Mac 地址的给出的过程当中是会有一些什么广播的，导致整个局域网之间出现广播风暴，最终导致系统或者网络崩溃，那 UDP 的泛红了也很经典。


我们前面已经说过了，直播这种流量型的、实施型的数据通常会用UDP，但是通常服务器端是什么？是向下发送UDP，但是接收 UDP 的能力并不强。也就是说菲亚老师上传视频可能上传一个视频，那服务器端接收一回，然后菲尔老师再上传一个视频也接受一回，对不对？但是如果同时有1万个菲亚老师的同时向慕克网上传视频，很可能把慕克网打瘫掉。


所以 UDP 泛黄就是这样，它不是拉取数据，它是同时向服务器端发送大量的 UDP 请求，大量的数据包通过数据量大，通过带宽大来把什么对端的服务器，不管你是应用服务器还是数据流服务器给压瘫掉，那这种泛红攻击通常还是受限的节点，也就是一个到 10 个节点，当一个黑客能够同时操纵数千个、数万个节点的时候，我们通常给这个黑客一个名称，叫什么？僵尸木手，它控制的所有服务器就是属于僵尸服务器，或者叫它肉肌服务器，那一个黑客怎么会拥有这么多的机器来让它用呢？他要花很多钱，唉，一台服务器一个月可能就是什么，就是几百块钱。如果他要控制几万台服务器，他每个月的开销就是几百万。当然黑客不会这样玩，他怎么玩？它会通过一些这个我们的端口开放的缺点，比如说有的很多的云平台的机器是 22 端口，对，什么0.0.0.0，斜杠零，也就是任何人都可以打开的。还有的人把 doc 蒂姆的这个端口对任何人打开，那我们的这个僵尸木手就会去全网去扫不同的这个云平台，不同的这个机房。


有没有这样的机器，对什么对外打开了一些关键端口，然后去尝试用不同的用户名密码来登录你的服务器，如果发现可以猜出你的用户名密码，它就可以什么成功的捕获你的服务器，捕获完了以后，它也不对你的服务器进行破坏，只不过利用你这台服务器变成它的僵尸或者它的肉肌。
当他掌握了数万个僵尸、数万个肉鸡的时候，他就可以对中国银行、建设银行、农业银行等金融系统等什么核心系统发起总攻了，那这个时候你就会发现有数千台、数万台机器同时采用机型数据包宏泛攻击或者泛红攻击来攻陷一些金融机构，或者攻陷一下慕克网这样一些视频机构，从而进行什么拒绝服务的破坏。


那这就是 DDoS 和 DOS 的攻击手段。好聊完了这种拒绝服务，那大家想一想如何来防御它呢？什么方法最好？当然就是前面说到了土地公 CDN 无处不在，是吧？防微杜渐，然后乱棍打死的土地公了。好，那这是第一种网络攻击手段。那下面我们介绍两种非常类似的攻击手段。


好，飞扬老师时拿出一支笔来给我们说说画画，那这里 DNS 左边，

[image](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/748a0346-4647-4706-affb-a4ce2932651d/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466THPFFQFN%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T231029Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIApYD2k3mx%2FQDGI4TAKm%2F7Oa%2F46PRAlf0WyWxx378qoHAiBrbaM7e%2FTHm7MU2u9XgUUDEgIihn7nz%2FcFWYV4j0ratyqIBAjG%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMzKM20yS6syEnGJCiKtwDbO%2B58u7CqluTQolgswKr8Y5eIsnxWq5LGx2ppt46oXNnV3BoTWFP4lbF%2FFNxGKwimbiQQut3K1Fy350i05H2TO5LgW9e3Pr%2BtMAkfflMWuuv85LuAs2VoqazVu52FdoagPKdFm%2FfEau2QC5yD8rKPaYMFqB%2BfTR%2Bx5WXS5lJ142%2FIGPRXa9r%2BiZIKwnyRmct%2FosUniNxbAaqqhLNlwS39KJtoz55PBLpu7vNCj9lF35FDaRVM7KX9U1QuRh%2BM%2FoC47P9bsjqC86bCibcTDMBYEqC84wVuvBIpx15MtJZBzim9emnx1ZN62rIrgqtkYsEHpkb4jgPEkrxhPcrq16rtTdsorjio8qu0kRBaSm0PFtMKojNRswgkLCzeHUpLagC9PizzcNVrdiyz4TFZzjVJmj8OIEslacQWtLQIDC6IkkrR4SWVN2CMSc0mgEfp8WJDjJPBoYcGkFnS%2Fq3SXV7KnD4QX88TA%2F%2FRqY%2B36D1LyeHIbwm%2FfP9ynXEJHR2R0PgxvPVMbw%2BH1quAy%2F6%2FB9ynhdmQ5j42CDbTyYm2DQGKSViacupPYceSCx0JHxGOzOG%2FDjzW0Dd%2FaEOA%2Ftuc4KX9TiCtbTLuF0nzidQ6UQi6SgLxPOYZFMAQN%2BxZyowgbj%2F0gY6pgFhZro%2B5DCKT3jgMeQO6SJgrYTmCq8Mw57H%2FFBjkUD5HpV3qUuUQIHYhCtrTH4DSghW4XEKlLAIqZKPofYF4FFCJDfsBJqTSkF81zp23k8YHXXsrBBJ2w2vzCVYvhm%2BCT9BTPhjUTbrGK9a74cGGElkeHcY1Kz6GM4EGYlOl6MKAkNqZoV0jY8H8u%2F4VYz498sqASQkh3XIAhUY9mgljlwHtiTKrsIH&X-Amz-Signature=1ca02acc0268694a3a5ebd5c2203ffce88b6ac0a1047825604f92e6f0612c1af&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

我们整个这一大块区域，我们假设是一个我们的教育系统评测机构，那右边是什么？是需要我们访问的这个 i m c . com 的这个服务器，以及是相关的这个 DNS 域名解析。好，这个评测机构要来评测了，目客网，那他怎么评测呢？很简单，这个评测这个教育机构的这个主任，他用他的电脑或者是笔记本尝试去访问，叫 IMC . com 来看一看用户的反馈对不对？那他访问的时候首先会用本地的服务器的叫内部缓存，这样它服饰它的缓存，当找不到缓存的时候，它会是什么？用 etc resolve 点 conf 了等等什么呢？指定的 DS 解析的服务器通工厂一个叫系统或者一个网站，它的 d n s 服务器就是我们前面说到过的什么我们在 d m i z 区的什么千里眼这样一台本地 DNS 服务器，这个 DNS 服务器里面会有大部分的网站的 DNS 地址，[比如像谷歌.com](http://xn--o1qw5snppqpar90k.com/)、百度点Cocom，甚至于像 imooc . com。


如果没有的话，它会为什么去全球的 13 个耕於？比如像谷歌煜的话，就是 8.8. 八、 8.8 这样的知名的耕耘率，去查找 i m mock . com 的具体的一个 IP 地址，如果还是查找不到，他就会去什么. com 他们的顶级域来进行查找，那最终有可能通过什么 s p 的供应商这里，比如像电信、联通移动端的 DNS 服务器这里面就究竟找到了它的这个具体地址，然后发给了幕布克网，那这是一个叫正常情况。


但是如果慕克网这个竞争对手尝试这种抹黑，幕克网怎么办？很简单，在这个我们对应的这个教育系统的这个 DNS 服务器，这个也就是 DMZ 区的这个服务器，这个牵连在这里进行一个小小的破坏，怎么破坏呢？在他的其中的 a 记录，通常 DS 里面很多记录，说什么 SRV 记录、 a 记录、 CNAME 记录等等。


最简单的就是给 AA 记录， a 记录就是什么域名和 IP 地址的对应关系，他把 imock . com，那么就域名对成了一个地址，这个地址什么是一个很烂的网站？这里面骂声一片，这样一个个网站好把它转成这个地理池，这个时候教育局的领导一看，嗯，慕课网不行，学员马失声好多，那该再怎么处理啊？降级，把这个程序员培训机构第一名的名称给拿掉，变成什么？第1万名，对吧？这就是一个降级。嗯，这时候慕克王竞争对手那第二名就很开心了。哈哈，我一举跃，继续。


什么排名第一的网站？那这就是 DNS 投毒。那通常这种投毒对视频机构其实投的还不利。厉害。最厉害的是什么？还是金融机构？如果我们尝试把什么工行、农行、建行的 IP 地地址转成一个什么，转成一个假冒网站，那这个时候当用户或当企业输入他的企业账号、他的用户命令密码的时候，所有这些信息就被假冒号网站获取，取完了以后他可以拿着这个用户命令密码去登录真正的工行、农行、建行，从而提取出其中的，

[image](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/408b68f4-d938-47f1-8082-a7a40d823ca9/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466THPFFQFN%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T231029Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIApYD2k3mx%2FQDGI4TAKm%2F7Oa%2F46PRAlf0WyWxx378qoHAiBrbaM7e%2FTHm7MU2u9XgUUDEgIihn7nz%2FcFWYV4j0ratyqIBAjG%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMzKM20yS6syEnGJCiKtwDbO%2B58u7CqluTQolgswKr8Y5eIsnxWq5LGx2ppt46oXNnV3BoTWFP4lbF%2FFNxGKwimbiQQut3K1Fy350i05H2TO5LgW9e3Pr%2BtMAkfflMWuuv85LuAs2VoqazVu52FdoagPKdFm%2FfEau2QC5yD8rKPaYMFqB%2BfTR%2Bx5WXS5lJ142%2FIGPRXa9r%2BiZIKwnyRmct%2FosUniNxbAaqqhLNlwS39KJtoz55PBLpu7vNCj9lF35FDaRVM7KX9U1QuRh%2BM%2FoC47P9bsjqC86bCibcTDMBYEqC84wVuvBIpx15MtJZBzim9emnx1ZN62rIrgqtkYsEHpkb4jgPEkrxhPcrq16rtTdsorjio8qu0kRBaSm0PFtMKojNRswgkLCzeHUpLagC9PizzcNVrdiyz4TFZzjVJmj8OIEslacQWtLQIDC6IkkrR4SWVN2CMSc0mgEfp8WJDjJPBoYcGkFnS%2Fq3SXV7KnD4QX88TA%2F%2FRqY%2B36D1LyeHIbwm%2FfP9ynXEJHR2R0PgxvPVMbw%2BH1quAy%2F6%2FB9ynhdmQ5j42CDbTyYm2DQGKSViacupPYceSCx0JHxGOzOG%2FDjzW0Dd%2FaEOA%2Ftuc4KX9TiCtbTLuF0nzidQ6UQi6SgLxPOYZFMAQN%2BxZyowgbj%2F0gY6pgFhZro%2B5DCKT3jgMeQO6SJgrYTmCq8Mw57H%2FFBjkUD5HpV3qUuUQIHYhCtrTH4DSghW4XEKlLAIqZKPofYF4FFCJDfsBJqTSkF81zp23k8YHXXsrBBJ2w2vzCVYvhm%2BCT9BTPhjUTbrGK9a74cGGElkeHcY1Kz6GM4EGYlOl6MKAkNqZoV0jY8H8u%2F4VYz498sqASQkh3XIAhUY9mgljlwHtiTKrsIH&X-Amz-Signature=c5803050286ee4328e4abce188f4ab5c477c136b21c16f606cd4f233868b4344&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

比如几千万、几个亿的钱，然后转到个人账单户里面，从而变成一个金融欺诈、金融盗取行为。


那么这就是 DNS 投度的危害性，那和 DNS 投入类似的 DNS 投度危害的是什么？是 URL 和 IPD 之间的对应关系。我们还有另外一种投毒手段，就叫 AR p 投毒。 AR p 大家应该学过 TCPP IP 应该都很熟悉 a AR p 干什么在这局域网内部告诉我们每一台服务器你对应的这个 IP 地址的机器到底在哪里，对吧？每一台机器其实身上不是有 IP 地址的，而是有什么唯一的 Mac 地址作为区分的。假设我们 PCC 1 这台机器要在这个局域网内部找到一台 FTTP 服务器，这个时候我知道有个地址是 10 点 109: 10，但是怎么样找到他呢？怎么找？先在自己的 AIP 缓存里面找有没有他的麦克地址，有的话直接把数据包通过链路子层发给你那个麦克地址。


如果找不到还很简单，我在网关层发起一个叫 AIP 请求群公，发给所有的同一个区域网内的所有节点，请告知是我，你是不是 10 点 10: 10。好好，通红场是什么？那台机器应该回应他吧。但是在那台架机器回应令之前，欺骗者可以尝试先回应我是网关，请发给我，我来告诉你实际内容，然后他偷偷的把一个假的卖那个地址通过缓存注入的方式注入到我们的 AIP 缓存里面，这个时候我们 PCCG 以后再要去访问，我们 10 点 10: 10 就会读它的缓存，然后找到这个欺骗者，然后把他自己的个人照片就发给这个欺骗者了，欺骗者就可以。嗯，很开心的地获取到个人照片、个人账号、个人密码等等为证件，从而干很多的坏事。那这就是 AIP 投的度。


那 AIP 投度通常说是在同一个局域网内部进行投毒，因为是什么 DN 解析时是跨网站的好什么麦克一直在这解析，通常是在局域网的内部执行性的，所以 AAIB 投度通常就是欺诈一个具体的服务器，去欺骗他，去假冒一个他对应要找的这个，比如像 FTP 服务器或其他服务器 GPT 什么本局域网内部的偷渡好。


除了投毒破坏这个 PC 内部的 AR p 缓存以外，我们甚至于可以破坏网关的 AR p 缓存，网关其实也有一个叫 AR p p 的缓存，那这个缓存不会记录什么呢？所有通过网关，如果你要去查找一个机器名叫PCCE，或者是 IPD 叫 10 点 10: 10，或者查到一个 IPDD 叫 10 点 10 点点九九的时候，它会这里记录下来，通常这个地址就是在对应的 Mac 地址是多少，那这个时候当有用户要访问这个 IP 地址时候，会被直接映射到这个欺骗者身上。



所以下面两种偷渡主机器片型可以什么网关机器变形使得危害更大？


当然是网关机器片更大的，当任何和用户在同一个区域网之内想访问 10 点电视或者十点、 10 点点九九的时候，完全可以因为网关的 AI PP 被偷偷入了，而导致所有类似节点都找错了， PCPE 变成了找到叫什么 CC 骗者好好聊完了 AIP 投度跟 DDS 投抖说白了是什么？是一个身份的伪造，对不对？一个是伪造什么？什么？一个 u i l 伪造 i m [库克.com](http://xn--74qq73a.com/)。


另外一个是伪的，造局网内部的一个指定的 IP 地址，比如 10 点 10: 0， 10: 10 这样的伪造，通过这种伪造情形身份的欺诈从而获取到用户的所有的数据。比如你是一个 TSTT 文本，比如你是一个密码数据，比如你是个用户账号，最终就可以实现伪造成就这个用户最终向目标地址、目标服务局、目标银行、目标机构进行什么获利？好，聊完了这个两种网络机器杖，我们来看一看第三种更简单的机器杖。


什么机器杖？重放攻击。好，以包子铺为我们来聊一聊重放攻击。

[image](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/650d0ec4-b5f1-46ba-9dc9-9300303f370b/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466THPFFQFN%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T231029Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIApYD2k3mx%2FQDGI4TAKm%2F7Oa%2F46PRAlf0WyWxx378qoHAiBrbaM7e%2FTHm7MU2u9XgUUDEgIihn7nz%2FcFWYV4j0ratyqIBAjG%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMzKM20yS6syEnGJCiKtwDbO%2B58u7CqluTQolgswKr8Y5eIsnxWq5LGx2ppt46oXNnV3BoTWFP4lbF%2FFNxGKwimbiQQut3K1Fy350i05H2TO5LgW9e3Pr%2BtMAkfflMWuuv85LuAs2VoqazVu52FdoagPKdFm%2FfEau2QC5yD8rKPaYMFqB%2BfTR%2Bx5WXS5lJ142%2FIGPRXa9r%2BiZIKwnyRmct%2FosUniNxbAaqqhLNlwS39KJtoz55PBLpu7vNCj9lF35FDaRVM7KX9U1QuRh%2BM%2FoC47P9bsjqC86bCibcTDMBYEqC84wVuvBIpx15MtJZBzim9emnx1ZN62rIrgqtkYsEHpkb4jgPEkrxhPcrq16rtTdsorjio8qu0kRBaSm0PFtMKojNRswgkLCzeHUpLagC9PizzcNVrdiyz4TFZzjVJmj8OIEslacQWtLQIDC6IkkrR4SWVN2CMSc0mgEfp8WJDjJPBoYcGkFnS%2Fq3SXV7KnD4QX88TA%2F%2FRqY%2B36D1LyeHIbwm%2FfP9ynXEJHR2R0PgxvPVMbw%2BH1quAy%2F6%2FB9ynhdmQ5j42CDbTyYm2DQGKSViacupPYceSCx0JHxGOzOG%2FDjzW0Dd%2FaEOA%2Ftuc4KX9TiCtbTLuF0nzidQ6UQi6SgLxPOYZFMAQN%2BxZyowgbj%2F0gY6pgFhZro%2B5DCKT3jgMeQO6SJgrYTmCq8Mw57H%2FFBjkUD5HpV3qUuUQIHYhCtrTH4DSghW4XEKlLAIqZKPofYF4FFCJDfsBJqTSkF81zp23k8YHXXsrBBJ2w2vzCVYvhm%2BCT9BTPhjUTbrGK9a74cGGElkeHcY1Kz6GM4EGYlOl6MKAkNqZoV0jY8H8u%2F4VYz498sqASQkh3XIAhUY9mgljlwHtiTKrsIH&X-Amz-Signature=1a27854ab8edfdce599e0799fdcbad10ea377ffa0c02025613380a48cb71f2b0&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

那这里我们是小王，他去一个包子铺找了服务员a，付费 5 块钱买了一个包子，一游下去。哇，这包子好香嫩啊，好香甜啊，不错，我要再来一个boss。但他想到了一个投机取巧的方法，他拿这个小票去找了什么包子铺服务员b，结果包子铺服务员 b 还真的免费给他了一个包子哦。嗯，他发现一个漏洞，似乎这个包子铺的 100 个服务员之间是不做沟通的。你怎么样呢？我以后每天买一个包子，然后可以通过不同的服务员那里拿到 100 一个包子。那他把这个消息告诉了小李、小黑、小白，结果这个包子铺一个月之内就打洋关门了。


原因是什么？被吃空了这样一个攻击其实很简单，大家在企业当中有没有碰到过呢？也许大家说，唉，这不难啊，不就是一个交易要让它什么只出现一次吗？那我们有很多套路，我们可以什么把整个绘画或者把整个应用序列化，然后都标记一个序列号，然后对于不同的序列号我们应该怎么样？我们应该能够去重或者幂等的方式来进行回复，那这样呢？不管你是买一次包子还是买两次包子，你拿到的包子跟你买的内容是对应的，不会因为你有多张小票发过来，你就可以拿到多个包子，这种去重这种幂等这种序列化都是一些很好的手段。那其实除了这些手段以外，还可以什么？标注清楚用户的身份，通常利用存放攻击，不是什么普通用户在用，而是什么黑客在用。黑客可以抓到小王、小李、小黑、小白的交易，然后把小王的交易放大 100 倍，把小李的交易放大 100 倍。所以你如果能抓取，到底是。

