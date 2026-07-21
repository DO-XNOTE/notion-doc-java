---
title: 2-17 【Docker技术落地实战】部署微服务-5
---

# 2-17 【Docker技术落地实战】部署微服务-5

[image](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/623bcc37-3265-4e36-97a8-d42bb73057d5/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TWQPKROY%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T225929Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIA8pd2ZTFqSvw40mksumq%2BvaNLhobRbT1WJFgalBibYsAiEA%2BGwjZPkd1bxxhS8pkiyjlf4qoajHnHK5tuO%2Bwn8%2Bl%2FIqiAQIxv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDH5HOK5%2FE%2FfkqQ6bFircA9RqexNqc9%2BhlnTwoOkoZWNf0C%2Fa9W3fKa3nwO21X3oCApseyh6J4srSxQy3ZkFu7Px%2BhJTZB5UffGPF9CUhK9tifXsfdXZ1kC%2BphRPxhSrohEopUm%2BBAnegZ0dc1J2Qe4d3gNl%2BiuJPkdxzt6d7eJ7VugRWhkxNM0Ifn3RzI6rnyZSrwL8APPc4YuLXA9ucsHuYMiZI8kJkBnMZAO52ruR3BdSGVyJXPWRApzHXRMFC7CG9vWEM6xh%2BMlP3meZi5dIVvxU23AQJ%2BJIcgi%2Fw9Fl9nxduHB8Ysgh07zrAdjfmGP%2F%2FV32B0hoUl3e4wGZJohwudMLm22EI62dEjY5OH1lsbx6mUr6SxScz%2F571dgPTMGDgHFT2yP8B%2FDOhDK6qcz%2FsGOtiZ%2BaBgIj3EFhD7HdMS12OoclJ%2B4CyQAzmrdZ817f3CVs7PAiEKWXVLAQVxyYk2tUMRhbOYSVKwXCyarPh4ZjAA%2FGKaxrc8LspXkeNwbL%2FE86AvrI73S1Xgohf5eKW6n5twBFZYcK4gz2RTI55jUS32xjOVuc4Mio6PpKxxRYuuGBNTG4bJKdiQDmFLok2Z1Opv5V%2Fs2PlaNfi0OSBadJGvA6fu5aLExk78RIp%2FUGBcW6p9lSnBHX6MNi6%2F9IGOqUBfz%2FYnufyX5678xbn89xyJRp80T345ppNR8O8ViKbPg%2F6g0eVPs5nHBsO0l2NJOGvSJxucRpqwYYqGGaYPvBkLP3xL2%2BaDxFgBc79rptF5G5f2vg2wXJYem11Gq1TUrZbdpxqxNQqpgTk0YMIW4x94UkqXTypTOTQL7Uh5aWnl4eGyFnWK2rYMPyUESR%2FDKmqlakO94IWF%2BLMT%2B1UTnIHjEmWhGWV&X-Amz-Signature=2bf34672f875d4cd9923b55a477b68bd65630adf5bd15eb7c26747e4a61b1982&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

[image](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/277170e6-bd51-4b92-ae8b-159aa15da036/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TWQPKROY%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T225929Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIA8pd2ZTFqSvw40mksumq%2BvaNLhobRbT1WJFgalBibYsAiEA%2BGwjZPkd1bxxhS8pkiyjlf4qoajHnHK5tuO%2Bwn8%2Bl%2FIqiAQIxv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDH5HOK5%2FE%2FfkqQ6bFircA9RqexNqc9%2BhlnTwoOkoZWNf0C%2Fa9W3fKa3nwO21X3oCApseyh6J4srSxQy3ZkFu7Px%2BhJTZB5UffGPF9CUhK9tifXsfdXZ1kC%2BphRPxhSrohEopUm%2BBAnegZ0dc1J2Qe4d3gNl%2BiuJPkdxzt6d7eJ7VugRWhkxNM0Ifn3RzI6rnyZSrwL8APPc4YuLXA9ucsHuYMiZI8kJkBnMZAO52ruR3BdSGVyJXPWRApzHXRMFC7CG9vWEM6xh%2BMlP3meZi5dIVvxU23AQJ%2BJIcgi%2Fw9Fl9nxduHB8Ysgh07zrAdjfmGP%2F%2FV32B0hoUl3e4wGZJohwudMLm22EI62dEjY5OH1lsbx6mUr6SxScz%2F571dgPTMGDgHFT2yP8B%2FDOhDK6qcz%2FsGOtiZ%2BaBgIj3EFhD7HdMS12OoclJ%2B4CyQAzmrdZ817f3CVs7PAiEKWXVLAQVxyYk2tUMRhbOYSVKwXCyarPh4ZjAA%2FGKaxrc8LspXkeNwbL%2FE86AvrI73S1Xgohf5eKW6n5twBFZYcK4gz2RTI55jUS32xjOVuc4Mio6PpKxxRYuuGBNTG4bJKdiQDmFLok2Z1Opv5V%2Fs2PlaNfi0OSBadJGvA6fu5aLExk78RIp%2FUGBcW6p9lSnBHX6MNi6%2F9IGOqUBfz%2FYnufyX5678xbn89xyJRp80T345ppNR8O8ViKbPg%2F6g0eVPs5nHBsO0l2NJOGvSJxucRpqwYYqGGaYPvBkLP3xL2%2BaDxFgBc79rptF5G5f2vg2wXJYem11Gq1TUrZbdpxqxNQqpgTk0YMIW4x94UkqXTypTOTQL7Uh5aWnl4eGyFnWK2rYMPyUESR%2FDKmqlakO94IWF%2BLMT%2B1UTnIHjEmWhGWV&X-Amz-Signature=525a79ad2cbd318d60b66506a2fb57f5d83864903221c2eb0dcb745b6bf7a260&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

然后我刚刚好像漏了个 demo 以 demo 形式跑。然后我们要跑的是 NGINX 这个 image 这个 image 提前我已经下好，所以会比较快，它也没有下好会稍微有一个下载的过程。


下完以后我们可以用 docker ps NGINX 看一下，你就不叫 NX 叫 my front 他不能直接跟那个名字 PS grip 是不是已经起来了？它是以 NGINX image 形式运行的一个 my front 应用，它是 80 端口。所谓 0.0 就意味着我可以用什么我可以用本地的这个 price IP 来找它。当然它通过 nit 也会什么映射到我们公网地址。所以我们好，我们用公网地址的 8080 来发现它公网地址已经在这个页面。我先看一下照理 gateway 应该已经在这里出现了，给他会出现，但是他可能暴力说他中间有点冲突就无所谓。我们用它的什么巴琳巴琳来访问一下是不是看到了主页出来了，但是好像有些内容好像还不是很完善，是什么原因呢？是因为我们的很多的这个服务，比如说我们的这个什么前面的那个轮盘轮播这一块服务，还有我们的 catalog 目录结构，那些服务器都没有什么在我们的 gateway 上进行指向。
我们可以仔细看一下我们代码，我们 gateway 里面核心代码是 gateway application 底下有个 routing 的 config 的 Java 的这个类。


然后它的这个 routing config 的这个里面会定义我们所谓的 routing 你可以看到它这里定义了什么，有一部分的 user service router 过去 authentication service router 过去 search 也可以 route 但是没有什么没有我们的什么轮播的这些也没有我们整个目录结构，就是整个我们所有 item 的目录结构，只有 item 的细节，没有 item 的目录结构，就导致我们什么主页其实没有什么内容渲染。那我们能做的什么其实主要就是用户登录和登出。我们最近先清一下我们的那个 cookie 清一下 cookie 保持我们这个应用是比较干净的，我重新刷新一下界面这样是一个比较干净的状态。这个时候其实是什么？是你能看到基本的最主页的这个简单框架，就点了慕渴望了能看到它的简单的框架。然后这里是用户未登录的状态，那这个时候我们可以尝试进行登录，我这里应该提前是，有过一些这个基本的数据的，应该是在 SQL 里面已经有一个叫 IMock 123123 我们看一下是不是这样。


有一个 IMock 123123 其实是已经在这个什么已经在我们的这个 C 口语句里面的，如果大家发现还有点问题，没关系，我们可以什么我们可以用登出或者是什么清干净我们的整个这个环境。然后尝试采用注册的方式去注册一个用户，在这里点击注册。我们注册一个叫 imock10 两个用户也是选12312323123。你注册一个，注册完了以后，你 M 会就登进去了。


那这里面其实有几个点是要注意的什么点呢？是因为我在后台的代码这里，其实之前已经做了对一个跨域进行了处理。那就大家记得哪两处做了处理吗？一处是什么？我们刚刚在这个命令行里面看到的，我们什么在这个前台的地方指向它后台。同时我们选择 cookie 是 domain 是新的，没有做额外的 cookie 的大的这个限制。


这是一处。第二处在我们的 gateway 这个配置文件里，我们看一下已经什么有了一个叫 allow orange 这是已经有两处注释，但这两处其实还不够。因为我们实际如果你们在本地操作过程当中还会碰到一个问题，就是我们的 cookie 我们的 cookie 写进去的时候可以看到仔细看 cookie 的时候写进去的时候正常情况下不会是以这个 domain 来写的，因为这是一个公网的域，我们会以容器里面内部的这个地址或者说是服务器之间互 call 的时候的那个我们的服务器的私网地址。所以什么不是云服务器对外的公网地址。


这个导致什么？我们在主页打开的时候用的是什么？是 101013301 三六点四零这个域。但是内部服务器 set 出来的 cookie 的时候就是后台服务器 set 出来 cookie 的时候并不是这里，所以会导致什么我们的 cookie 没法真正 set 出来，也就是用户登录完以后可以跳转到主页，但是这里不会显示你的名字，同时这里不会展示你的头像。


这个问题其实我是之前已经做了一部分代码修正。那在哪里修正这个问题呢？我们要找到我们什么我们的相关 set cookie 的那个地方，大家可以去查找一下。 set cookie 的地方其实是在这里 commonly 然后它的里面的 common 里面有一个叫做我们的基本的一个 utility utility 下有个叫 cookie utilities 我放那整个这个 cookie utilities 里面，我们可以去看一下它有核心的两处地方，一处是叫这里 set cookie 然后它真正调的是这个 do set cookie 那 do set cookie 也有两个实线，一个实线是在这里，最后是以玻璃层 is in code 结尾的。


这种情况下调用的情况下，我们要把这个注释掉，就是我们不要设成 local host 故甚至于我们其实应该是把这个 domain 就不用去拿直接 string domain 就等于它我这已经偷懒，没有把上面注释掉，还是让他去拿一次这个 domain name 然后我这里把它强行替换成什么130136040，也就是改成外网地址。


那真正大家可以在实际操作过程当中，其实不需要这样做的。如果是我们真正有一个什么 D NN server 这个时候你的 DNN server 会用 URL 的形式，而不是用什么用 IPD 的形式。而我们的 uil 其实是跟后网就是内部的应用 URL 跟外部应用 URL 在主域上是一致的。这种情况下，只要你设置的时候是以主域而不是以子域来设置 cookie 的时候，它的域是可以成功的。但是我们这里是没有 DNS 服务器的，也没有是吧，买过一个域名。所以我在这里比较简单粗暴，就直接把 domain name 强行设置成为了外网地址。那同样到了另外一个实现。那另外实现最后是以这个 encode string 结尾的这样一个传参的实现，它也要做相应改动。当它拿完这个 domain name 的时候，或者说你不用去读那个 domain name 你直接把它 set 成什么这样一个公网地址。实际上公网地址以后，这个时候你就在实际过程当中用 cookie set 设置完了以后，重新的什么去把这个 cloud common 没问题倒一下。


然后也把我们相关的两个服务没有 install 一下，一个是什么？一个是我们的 user web 这个服务来去把新的我们的大的胖的夹包里面去引入什么新的我们编译出来的这个 common 的这个小夹包。那同时另外还有一处会用到我们的这个什么我们的这个 cookie set 是我们的 order 的那个类里面，所以我们在 order 的 web 里面也要去什么如法炮制的去 install 一下，把最新的这部分代码给引入到我们的很胖的这个价包里面比较大的这个价包里面。


那之后这个价包是大家 target fully order web Snapshot 点价，然后这时候上传到我们的服务器，上传到我们的服务器我们再去看一下就会成为这样两个加包，一个是这个新的 user web 的加包。另外有一个是我们新的这个福利 order 的加包。那这个时候你就对 user 比较简单， user Docker 然后用什么用这个 IM 然后 my user 这个方法它已经在跑着，建议用杠 IM 杠 F 把它给停掉，因为你要重新去 build 一下。为什么呢？因为你原来的里面的那个什么价包变化了，所以再用什么杠 IMI 删除 image 的形式，把 image 也删干净。


这个时候我们又要重新去新生成一个 Doc phone 那这里我快速的替换一下。就如果大家有之前保存多个 Doc phone ，会在后面替换的时候会相对简单一些。我这里因为只生成了一个 Doc phone 所以这里是相对来说要有重新的替换过程当中的工作。那改成什么 food user web 好改成这个 food use web 好替换完了，这个时候用重新怎么跑一个什么 Docker 的 build 然后类型就是我们的 my user 然后当前这个主目录去 build 一下，build完了以后我们什么我们重新的跑之前类似的命令我们看一下，那命令还在不在 202 来到 12012 的端口映射，然后把 my user 重新再去跑一下，一样道理，my order 也要重新的跑一下。


那跑完以后你再去什么？最好是重新的把我们的什么 service 跟 gateway 重启一下，因为 gateway 是有服务发现的，但是它的时间是有一定长的。那比如我们要很快的生效，建议就是 restart 我们的什么 registry 这样就把我们的什么 urecar 的界面上那些红颜色标识符给刷掉了之后，我们用重新 restart 一下我们的什么我们的这个 get away。这个时候就不需要 get away 在等到它的一定的时间来触发服务发行，而是在它启动的过程当中，强制的重新去发现我们新的什么新的一个起的叫 my user 的容器，跟原来 my user 容器有点不同了。


好刷完以后我们回过去看一下，我们在 ureka 这里看看是不是能够重新的把这些都加载出来。其中既要包含新的 user 包含 gateway gateway 出来了， user 也出来了。那还有一些其他的可能还在加载过程当中，我们看一下应该还有不止这些 config auth ，我们因为其他的 order 什么可能没有起这点 user 跟 gateway 都已经加载完毕，这个时候我们再去尝试一下，那真正就会达到我们的效果。
因为刚刚我在演示过程当中，其实已经把新的这个我们加油包提前准备好了，所以你能看到这里 IMock 然后你看到这里用户名的这个效果已经出现了，其他的这个包括order ，包括我们的这个 cut 功能，大家可以做类似的尝试。关键的几个点，我再重新的去强调一下一个点，就是我们在 


gateway 里面要有服务的映射关系，它才能够暴露。比如像我们的这个轮播，你要真正对外提供服务，你要把这个服务提前准备好，注册在我们什么 eureka 同时在 gateway 上要对外暴露出去，要有一个合适的 route 那这个时候它外面的人访问里面，就不是再用它里面的那个服务器的端口了，而统一用 gateway 的端口 20004 这个端口，然后跟指定的这个 URL 的 route 来指向后台真正提供服务的这个应用。


除此以外的数据库要提前准备，同时要跟我们什么我们应用的这个数据库名用它的 table 的一致。前端后端的调用就是前端一定要找到合理的这个后端的 URL 同时要支持跨域，前端也要支持，后端也要支持。同时后端 set cookie 的时候要 set 对它的域名，这种情况下就能前后端打通。



好，那我们这个 Doc 里面这个 demo 就到此为止。那后面的章节我们会有其他的带一定编排功能的容器平台，就像 cloud foundry 比如像是我们的 masses 比如像我们 kubernetes 那在这个时候我们就会支持什么多个容器对外提供一个服务，然后和服务和服务之间进行调用，而不是只是容器和容器之间进行调用。同时对外提供的时候会有一个更加漂亮的弹性的能力的后台应用。好，这节就到这里结束，那期待大家在后面的内容继续一起来做题目，我们来动脑筋。好，谢谢。


