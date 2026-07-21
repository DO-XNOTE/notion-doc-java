---
title: 1-7 【demo】搭建Client端直连配置中心
---

# 1-7 【demo】搭建Client端直连配置中心

[image](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/797ac3c7-04de-4dd8-8904-c507550eb20a/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QON5YMZT%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T225706Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIG%2B%2BK9500j2WvoG7y18nJw6xDjuULbsIJ8Z4OnHDeRqJAiEAhH4OewqgbKSOAGEexM9mfyLDPybQV1hxyu%2FnRz3bOFgqiAQIxv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDK2mymYsK3yZoTzI3SrcA7IsEWttSpQTtbEyI4Z2vxyh0vbTN%2FzcyDSizN4ZjXqXw51oHezqs6rR3rL0V6ikvZ2MLqQu1VXWawv8zFHAwFciiT0BpMt4dmLhWdaySE2YLkS0vHkS7XpVfIV4mO2RwC4zL%2Bpef3hAj%2BGFPMrOiPiDMkOsimCvvCbFtbNTSM7Qbd1VjImQd4SvW2OhQl9086%2FGfMrnUaBD6%2Bhsv4373QJeG8kuqpRh6OYVYfrEDAzDQwc24vf2afPjrsJkBIozUmPdrC3uAwW6EZWhtneRhjDNwxO6bwofz9quUn%2FJRY5K1U82vCCrXk0yi9koUyW2KvwWI30IpPFeoTNP7Q09tAIE3dn7ZqaeqqAPi2CP1hteNp9Bxgpsxg5EAp8w6TuE5XIaeAKzaLOFxeznQrCuR3w7ujmoa5Eop15aUT8O2EyJqAmOqo1mFQrKmxOBTueNDi0JLM2Wxs2VDE4UbxDcszrlOq88RZLDtWxUdg59Pxq2n1V6kbsvQjj%2BWpz2R0hHZS%2FBn37dDZpUL2d9D1hXtAkcf7Gd2pwdsN8U5WxC%2FKTUBom49BAa7eW2aauCmMDWSWVySoKQsnOao4pSpcdBWA%2F4BbLjgg9u1CAO5rQkPnVXnFqYSWoefE1qvhedMP%2B5%2F9IGOqUBCbHoHZq25wYqvze5UucIiqmsZIah%2FheTmpUFDu5ff%2B1OIxZL5h0lgpM9X%2FAEWYzM9%2FATBZuXPNTWLD9JqFdBKCluXJ4OGTRN7Doq9aivb3VqvbwZKZ0BfbkNu4ehbjQYYb3KtlxJ4Cc8oJH3zByWvByXIMfSI1koOZy9VxPBGdUkrBgD%2FgHK5jm%2FgWn2C%2FGOZ8dHWchfMoGp0nVnDL378tE75qdY&X-Amz-Signature=97608d35afc44f9f94fd4aeef636a5000a873f4d3e30375e21cc8cdbd356fab8&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

[image](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/9aef952d-8d14-4179-bf99-0c56e03d4c8b/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QON5YMZT%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T225706Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIG%2B%2BK9500j2WvoG7y18nJw6xDjuULbsIJ8Z4OnHDeRqJAiEAhH4OewqgbKSOAGEexM9mfyLDPybQV1hxyu%2FnRz3bOFgqiAQIxv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDK2mymYsK3yZoTzI3SrcA7IsEWttSpQTtbEyI4Z2vxyh0vbTN%2FzcyDSizN4ZjXqXw51oHezqs6rR3rL0V6ikvZ2MLqQu1VXWawv8zFHAwFciiT0BpMt4dmLhWdaySE2YLkS0vHkS7XpVfIV4mO2RwC4zL%2Bpef3hAj%2BGFPMrOiPiDMkOsimCvvCbFtbNTSM7Qbd1VjImQd4SvW2OhQl9086%2FGfMrnUaBD6%2Bhsv4373QJeG8kuqpRh6OYVYfrEDAzDQwc24vf2afPjrsJkBIozUmPdrC3uAwW6EZWhtneRhjDNwxO6bwofz9quUn%2FJRY5K1U82vCCrXk0yi9koUyW2KvwWI30IpPFeoTNP7Q09tAIE3dn7ZqaeqqAPi2CP1hteNp9Bxgpsxg5EAp8w6TuE5XIaeAKzaLOFxeznQrCuR3w7ujmoa5Eop15aUT8O2EyJqAmOqo1mFQrKmxOBTueNDi0JLM2Wxs2VDE4UbxDcszrlOq88RZLDtWxUdg59Pxq2n1V6kbsvQjj%2BWpz2R0hHZS%2FBn37dDZpUL2d9D1hXtAkcf7Gd2pwdsN8U5WxC%2FKTUBom49BAa7eW2aauCmMDWSWVySoKQsnOao4pSpcdBWA%2F4BbLjgg9u1CAO5rQkPnVXnFqYSWoefE1qvhedMP%2B5%2F9IGOqUBCbHoHZq25wYqvze5UucIiqmsZIah%2FheTmpUFDu5ff%2B1OIxZL5h0lgpM9X%2FAEWYzM9%2FATBZuXPNTWLD9JqFdBKCluXJ4OGTRN7Doq9aivb3VqvbwZKZ0BfbkNu4ehbjQYYb3KtlxJ4Cc8oJH3zByWvByXIMfSI1koOZy9VxPBGdUkrBgD%2FgHK5jm%2FgWn2C%2FGOZ8dHWchfMoGp0nVnDL378tE75qdY&X-Amz-Signature=51af4d31f8aa46c7cd949275eb61ac2b5d6ba2856504529e61076bcc1f4ea8c0&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

[image](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/b02e641e-6a8c-4ad7-accc-a5f1a9009956/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QON5YMZT%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T225706Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIG%2B%2BK9500j2WvoG7y18nJw6xDjuULbsIJ8Z4OnHDeRqJAiEAhH4OewqgbKSOAGEexM9mfyLDPybQV1hxyu%2FnRz3bOFgqiAQIxv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDK2mymYsK3yZoTzI3SrcA7IsEWttSpQTtbEyI4Z2vxyh0vbTN%2FzcyDSizN4ZjXqXw51oHezqs6rR3rL0V6ikvZ2MLqQu1VXWawv8zFHAwFciiT0BpMt4dmLhWdaySE2YLkS0vHkS7XpVfIV4mO2RwC4zL%2Bpef3hAj%2BGFPMrOiPiDMkOsimCvvCbFtbNTSM7Qbd1VjImQd4SvW2OhQl9086%2FGfMrnUaBD6%2Bhsv4373QJeG8kuqpRh6OYVYfrEDAzDQwc24vf2afPjrsJkBIozUmPdrC3uAwW6EZWhtneRhjDNwxO6bwofz9quUn%2FJRY5K1U82vCCrXk0yi9koUyW2KvwWI30IpPFeoTNP7Q09tAIE3dn7ZqaeqqAPi2CP1hteNp9Bxgpsxg5EAp8w6TuE5XIaeAKzaLOFxeznQrCuR3w7ujmoa5Eop15aUT8O2EyJqAmOqo1mFQrKmxOBTueNDi0JLM2Wxs2VDE4UbxDcszrlOq88RZLDtWxUdg59Pxq2n1V6kbsvQjj%2BWpz2R0hHZS%2FBn37dDZpUL2d9D1hXtAkcf7Gd2pwdsN8U5WxC%2FKTUBom49BAa7eW2aauCmMDWSWVySoKQsnOao4pSpcdBWA%2F4BbLjgg9u1CAO5rQkPnVXnFqYSWoefE1qvhedMP%2B5%2F9IGOqUBCbHoHZq25wYqvze5UucIiqmsZIah%2FheTmpUFDu5ff%2B1OIxZL5h0lgpM9X%2FAEWYzM9%2FATBZuXPNTWLD9JqFdBKCluXJ4OGTRN7Doq9aivb3VqvbwZKZ0BfbkNu4ehbjQYYb3KtlxJ4Cc8oJH3zByWvByXIMfSI1koOZy9VxPBGdUkrBgD%2FgHK5jm%2FgWn2C%2FGOZ8dHWchfMoGp0nVnDL378tE75qdY&X-Amz-Signature=5e651d522d28d77b99ca8b24bfeff4fcb9b5b4e3bc936902596761b88d234982&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

[image](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/f35ec4f4-1117-4ac3-bc2a-cc5602b74e28/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QON5YMZT%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T225706Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIG%2B%2BK9500j2WvoG7y18nJw6xDjuULbsIJ8Z4OnHDeRqJAiEAhH4OewqgbKSOAGEexM9mfyLDPybQV1hxyu%2FnRz3bOFgqiAQIxv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDK2mymYsK3yZoTzI3SrcA7IsEWttSpQTtbEyI4Z2vxyh0vbTN%2FzcyDSizN4ZjXqXw51oHezqs6rR3rL0V6ikvZ2MLqQu1VXWawv8zFHAwFciiT0BpMt4dmLhWdaySE2YLkS0vHkS7XpVfIV4mO2RwC4zL%2Bpef3hAj%2BGFPMrOiPiDMkOsimCvvCbFtbNTSM7Qbd1VjImQd4SvW2OhQl9086%2FGfMrnUaBD6%2Bhsv4373QJeG8kuqpRh6OYVYfrEDAzDQwc24vf2afPjrsJkBIozUmPdrC3uAwW6EZWhtneRhjDNwxO6bwofz9quUn%2FJRY5K1U82vCCrXk0yi9koUyW2KvwWI30IpPFeoTNP7Q09tAIE3dn7ZqaeqqAPi2CP1hteNp9Bxgpsxg5EAp8w6TuE5XIaeAKzaLOFxeznQrCuR3w7ujmoa5Eop15aUT8O2EyJqAmOqo1mFQrKmxOBTueNDi0JLM2Wxs2VDE4UbxDcszrlOq88RZLDtWxUdg59Pxq2n1V6kbsvQjj%2BWpz2R0hHZS%2FBn37dDZpUL2d9D1hXtAkcf7Gd2pwdsN8U5WxC%2FKTUBom49BAa7eW2aauCmMDWSWVySoKQsnOao4pSpcdBWA%2F4BbLjgg9u1CAO5rQkPnVXnFqYSWoefE1qvhedMP%2B5%2F9IGOqUBCbHoHZq25wYqvze5UucIiqmsZIah%2FheTmpUFDu5ff%2B1OIxZL5h0lgpM9X%2FAEWYzM9%2FATBZuXPNTWLD9JqFdBKCluXJ4OGTRN7Doq9aivb3VqvbwZKZ0BfbkNu4ehbjQYYb3KtlxJ4Cc8oJH3zByWvByXIMfSI1koOZy9VxPBGdUkrBgD%2FgHK5jm%2FgWn2C%2FGOZ8dHWchfMoGp0nVnDL378tE75qdY&X-Amz-Signature=616b49f9d9d56f49ce299bf16399552f42b933077e9b22c9d99f380f8164f5a5&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

ello 慕课网的各位同学们，大家好，这一节我来带大家搭建一个最简单的直连式的配置中心服务。本节的主要内容有三个部分，第一部分创建一个新的 module 它的名字叫 config client 然后引入相关的依赖方。 Ok. 第二个部分是配置启动项和启动类。这里的启动项我们将指向前面搭建的 config server 来拉取配置文件。最后一步就是添加一些 service 或者 controller 将 github 中的属性注入到测试用例当中。这里我将使用配置文件注入以及代码中的 annotation 注入两种不同的形式来测试配置属性。

[image](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/db90c89b-7f90-4f0d-a0c6-fff03385d2bc/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QON5YMZT%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T225706Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIG%2B%2BK9500j2WvoG7y18nJw6xDjuULbsIJ8Z4OnHDeRqJAiEAhH4OewqgbKSOAGEexM9mfyLDPybQV1hxyu%2FnRz3bOFgqiAQIxv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDK2mymYsK3yZoTzI3SrcA7IsEWttSpQTtbEyI4Z2vxyh0vbTN%2FzcyDSizN4ZjXqXw51oHezqs6rR3rL0V6ikvZ2MLqQu1VXWawv8zFHAwFciiT0BpMt4dmLhWdaySE2YLkS0vHkS7XpVfIV4mO2RwC4zL%2Bpef3hAj%2BGFPMrOiPiDMkOsimCvvCbFtbNTSM7Qbd1VjImQd4SvW2OhQl9086%2FGfMrnUaBD6%2Bhsv4373QJeG8kuqpRh6OYVYfrEDAzDQwc24vf2afPjrsJkBIozUmPdrC3uAwW6EZWhtneRhjDNwxO6bwofz9quUn%2FJRY5K1U82vCCrXk0yi9koUyW2KvwWI30IpPFeoTNP7Q09tAIE3dn7ZqaeqqAPi2CP1hteNp9Bxgpsxg5EAp8w6TuE5XIaeAKzaLOFxeznQrCuR3w7ujmoa5Eop15aUT8O2EyJqAmOqo1mFQrKmxOBTueNDi0JLM2Wxs2VDE4UbxDcszrlOq88RZLDtWxUdg59Pxq2n1V6kbsvQjj%2BWpz2R0hHZS%2FBn37dDZpUL2d9D1hXtAkcf7Gd2pwdsN8U5WxC%2FKTUBom49BAa7eW2aauCmMDWSWVySoKQsnOao4pSpcdBWA%2F4BbLjgg9u1CAO5rQkPnVXnFqYSWoefE1qvhedMP%2B5%2F9IGOqUBCbHoHZq25wYqvze5UucIiqmsZIah%2FheTmpUFDu5ff%2B1OIxZL5h0lgpM9X%2FAEWYzM9%2FATBZuXPNTWLD9JqFdBKCluXJ4OGTRN7Doq9aivb3VqvbwZKZ0BfbkNu4ehbjQYYb3KtlxJ4Cc8oJH3zByWvByXIMfSI1koOZy9VxPBGdUkrBgD%2FgHK5jm%2FgWn2C%2FGOZ8dHWchfMoGp0nVnDL378tE75qdY&X-Amz-Signature=7d5a56385192ab0c5d835126340792256c85ef31936005447500842c903fbed8&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

OK 咱们说了直连式的配置中心是最简单的结构，它这里只是一个基础版，后面我们会对它进行升级改造。就像我们玩游戏一开始创建的是一个基础版的角色，后面咱将使用 sprint cloud 提供的组件对这个角色进行升级改造，咱就可以把它当做是这个角色进行一转二转。
OK 那具体要使用哪个 spring cloud 的组件对它进行增强呢？这里咱既不剧透也不放彩蛋，大家随着课程慢慢向后学就知道了。 OK 准备好的话咱就开始到 intelligi 里面开工。同学们我慎重考虑了一下，打算换一个口号。有的同学们说每天扣另一小时，健康工作 50 年，这个太浮夸了，我打算换一个务实点的口号，那就是听好了编程使我快乐，996是我的福报，我打算把这个口号先喊上两个章节试试效果。那咱借着这股新口号的号字开始创建。


第一个毛九前面说了它的 artifact 名称叫什么？ config 杠 client 点击下一步 module name 和前面保持一致，然后把它扔到哪个文件夹下 config 文件夹点击 finish 321 true 收起小桌板，这就来添加 dependency 咱前面说了这是一个基础版，那所谓基础版是什么意思这还不简单，基础版的意思就是要啥没啥。那么这里什么 eureka 都不需要了，后面咱还会继续增强的，所以这里只给他最基本的属性就可以了。那比如说我从其他的项目里面 copy 一个属性，就他了。


spring boot the starter web 好，我把这个属性 copy 过来，然后咱是不是还要把 config 的主角给拿过来，它的dependency ，咱这里把它配置上去，group是谁？大家非常熟悉啦。 spring framework.cloudok 那下面的 artifact 叫 spring 杠 cloud 杠 starter 再杠 config 这里跟前面咱们配置的 config server 是不是不同，前面配置的 config 中心，后面还有一个杠 server 那咱这里是应用方，它需要接入到服务中心，所以 dependency 的名称也是不同的，这里大家稍加注意一下，不要配错了。 OK 那它的 packaging 咱也给它指定一个，大家都非常熟悉了。 jar 对不对？就像骑上一批高头骏马 jar 咦好搞定 dependency 完了，接下来自然是要创建一个启动类了，非常简单。


我们创建一个包名，大家心里默念 com.imock.spring cloud 这个启动类，咱随便从一个地方拎过来，但是要给它换一个名字叫 config client application 点击回车，然后清理一下内容，把类的名字在启动脚本中替换掉。那咱把前面的绿帽子都给摘掉，重新戴上咱绿帽子多的是你要戴几顶，而比前面的 config server 少那么一顶，我只需要 spring boot application 就够了，一切从简。好，这里保存一下，接下来还缺少一个 controller 我们要验证配置属性，自然需要一个 controller 了。 OK 我这里新建一个类，它的名字就叫 controller 接下来给他带个绿。


好，新劳工作的controller ，咱就不戴绿帽子了，咱戴一顶高帽子叫 rest controller 在这个 controller 里面，咱提手给它来一个 get 方法，它返回一个 string 这个 string 咱就起名叫 get name 好，他 get 谁的 name 当然是咱在配置文件中配置的 name 啦，我们给它作为一个 get mapping 然后路径也是 name 很多同学给路径起名的时候，非常喜欢用那种给 API 命名的规则叫 get name 实际上在 rest 风格的接口中，咱不要把这个 get 加上去，就直接加 name 就好了，**把动词给省略掉，这才是 rest API 的风格**。


那大家说动词放在哪？动词当然就是 HTTP method 上了。如果你要查询，那就是用 get 如果你要修改，可以用 post put 都可以。那么删除一个对象，就 delete 把这个属性融入到 HTTP method 里面。而在路径上尽量把动词都给去掉。
OK 咱这里说了 get namename 在哪里，name在配置文件里，但是这里要把配置文件中的 name 取为自己所用，天下武功皆为我所用。这里定义一个属性，它就叫 name 然后怎么注入进来这个大家应该都非常熟悉了，通过 value 注入进来，那它的值这里要用一个通配符了，一个什么 dollar 符号，接下来就跟一个 name 那这个属性名称就对应了 properties 文件中的一个 name 属性。好。那么在这个 get 方法中，我们单纯的把它返回回去就行了，非常简单。那咱前面不是还配了另外一个属性吗？叫words。
Okay， see your words.


把这里也给加上名称改为 get wordsok 那咱这里依然把它注入进来，但是这里注入的有那么一点变化喽，什么变化呢？看咱不直接写配置文件中的这个名称 words 而是使用 my words 我想试着把这个 words 从 github 中的配置文件注入到我自己的项目配置文件当中。然后这个 my words 的实际上是引用我自己项目文件中的属性。咱前面不是说过，分别用两种途径注入，上面的这一种是直接从外部的配置文件加载。那下面的这一步是首先把外部的属性注入到自己项目中的配置文件，再从配置文件中加载。两种方式是不同的。


OK 咱的 controller 是不是已经定义好了？接下来该定义谁了呢？配置文件对吗？我看看上一次 config server 使用的哪个配置文件，它使用的是 application.yaml 那咱这里就另辟蹊径配置一个不一样的。那当然还是 YAML 格式了，咱已经跟老年人喜欢使用的 application properties 划清了界限。那我这里配置文件的名称就叫 bootstrap 然后后缀还是 yaml.yml 好，点击回车。
那这里面都有哪些属性需要配置的呢？那在配置之前，同学们还记得上一章老师有没有提过一个小问题，就是研究一下这些配置文件的加载顺序，比如说咱有 application.yaml boot strapyaml 还有 application properties 它们之间谁先谁后给这哥仨排一个座次。
配置文件的第一个属性是谁呢？当然是起名字了。黄蓝盔玉出肚脐。赵锡玉佳明，那这个名字我们就叫它 config got clientok 起好名字以后，咱们接下来先配置其他节点，然后再杀个回马枪回来配置 config 其他的属性都有哪些呢？ Server maha pot. 每次起 port 比起名还难，前面咱是 6 万了，那这里给你起一个61,000。

```java
package com.imooc.springcloud;

import org.springframework.beans.factory.annotation.Value;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RestController;

/**
 * <h1></h1>
 */
@RestController
public class Controller {

    @Value("${name}")
    private String name;

    @Value("${words}")  ) //  把远端的配置属性值获取到之后放到我的配置文件中，再从我的配置文件中获取属性值 words->myWords-使用
    private String words;

    @GetMapping("/name")
    public String getName() {
        return name;
    }

    @GetMapping("/words")
    public String getWords() {
        return name;
    }

}
```


好了，OK接下来在 controller 里咱是不是有一个额外的属性它是 words 对不对？这个 words 要通过咱的配置文件给它注入进来。所以这里声明一个 my wordsokay 它的值从哪里来？它的值就是从 github 的 properties 文件中获取，那这里咱就要把真声放上去，所以 words 才是对应 github 文件中的真实属性。然后 my words 只是我在这个本地配置文件中起的别名。


OK 那这一步配好了，咱是不是接下来要配置 config 的连接字符串了，我们看它的位置在哪儿，在 spring application 下面，紧接着跟一个 cloud 在 cloud 下面，我们再加上 config 咱 YAML 格式的缩进一定要注意，因为很有可能你一不小心缩进错了，那导致配置文件的属性。


这里 config 配置完了以后，咱要配置 URI 记住这不是 URL 而是 URI 那它的地址我们打上来就是 HTTP 冒号 local host ，这个 6 万指谁可不是打麻将里面的 6 万，它指向的是 config server 的端口。 OK 那接下来指定了 URI 以后，我们再指定一个 profile 这个 profile 咱把它写成product 。


那有的同学可能会有个疑惑，假如我们在配置文件中写死了 profile 那难道在生产环境或者是在其他的集成测试环境，我都要保持一份不同的配置文件来指定 profile 吗？其实不是这样的，我们在真正的项目中，这个 profile 不是写死的，而是由外部注入的，是从哪里注入的呢？这里比方说咱可以配置一个操作系统的系统变量，或者在你启动 Tom cat 的时候，给它指定一些属性参数注入进来，这样的话 profile 就跟环境挂钩起来了。

```java
spring:
  application:
    name: config-client
  cloud:
    config:
      uri: http://localhost:60000
      profile: prod
      label: naster


server:
  port: 61000


myWords: ${words}
```


比方说我们在日常测试的机器上，你启动项里面 profile 注入的是 deb 那么你在预发环境上启动项注入的是 it G 或者是 staging 那么你在真正的生产环境下，那这里就直接注入到production。通过这种动态配置的方式，咱就不用在自己的 properties 文件中把 profile 写死了。然后我们的应用服务就可以根据动态传入的这个 profile 去 github 上拉取到正确的文件。


OK profile 指定完了以后，咱们接着给它一个 label 那 label 我们也可以写成 master 也就是每次都从主 master branch 上面获取到属性文件。好，那我们写到这里，似乎所有配置属性都已经准备妥当了。但是老师夜观心想，似乎发现这平静祥和的配置文件背后似有凶兆似有大凶之兆，总之是不吉利的东西。但是一时又说不上来。那咱还是启动项目看如果项目有报错，再回头来看。那接下来咱启动哪些项目呢？我们按顺序，先要把 config server 给它启动起来，我们的依赖很少，所以启动起来应该相当的快。好，这里咱已经启动完成了。那接下来大家睁大双眼看一看启动 config client 的时候会不会有任何的异常。好，点击启动，我们把屏幕放大一点，看到 spring 成功了一半。


接下来看到这行 log 开始读取配置文件的信息了。 fetching config from server okay 读取了很久，夜长梦多，总感觉有事情发生。小心翼翼的往下移看起来。果不其然，看这里报错了，他报了什么错。大家看 error creating being with name controller 我们的 controller 初始化失败。为什么呢？它这里的错误信息下 could not result place holder name in value 那就是我们在 github 上面的这个 name 属性不能被加载进来，这是为什么呢？大家碰到这种问题会怎么样？我敢说 90% 的同学可能要直接百度了，那剩下 10% 的同学中大概有那么百分之一二对自己的技术实力非常有自信，直接点进去 debug 了对不对？实际上在碰到问题的时候，这两种方式并不是最有效的方式。


咱说来得早，不如来得巧，干什么事都要用巧劲。那这里怎么看巧劲那就是 log 了。**大家记着，在开源项目中，尤其是 spring cloud 这种开源项目中，它所有组件的 log 打的一定是非常完备的，我们总能从中查到一些蛛丝马迹**。比如说这里看这一行 log 是不是发现有那么点不对劲，给同学们 5 秒钟的思考时间，大家来找茬。
54321 好，我来揭晓答案啦。这里出问题的地方是 name 咱还记着在 github 中，文件的名称叫什么呢？我们给文件起的名字当中有一部分是 application 咱再到浏览器中回顾一下，这个 application 就是前面的 config consumer 后面的 DEV 是 profile 看起来一切正常。那我们再回到 log 里面。那看这里文件中的 application 是 config consumer 但是咱这里去尝试拉取文件的时候使用的这个 application name 是谁？变成了 config client 为什么？这里就是 sprint cloud config 中的一个默认的机制什么呢？它会使用咱在文件开头声明的这个 name 把它作为 application name 去拉取属性。


那如果你的 spring application name 和远端的配置文件不一样怎么办呢？这种情况很常见，就比如说你在办公室叫 Lucy 叫 Lily 叫 Peter 那你春节回村名字就会变成二狗子狗剩子。所以这种情况怎么办呢？我们有一个办法，就是说当你 application name 和实际文件名称不一致的时候怎么办？给出一个解决方案，在 config 下面声明一个 name 它做什么用呢？它能覆盖掉你 application name 中声明的这个名称。那我们这里给它起名叫 config consumer 好保存一下药到病处，

```java
spring:
  application:
    name: config-client
  cloud:
    config:
      uri: http://localhost:60000  
      name: config-consumer    #  起名叫 config consumer 好保存一下药到病处
      profile: prod
      label: naster


server:
  port: 61000


myWords: ${words}  # words 是github上的属性
```

我们再把这个项目重新启动一下，看看是不是问题就迎刃而解了。
看到 spring 成功一半，这次真的是成功一半了。走到下面。 started 好，项目成功启动。那么接下来的剧情非常简单了，我们怎么样到 postman 里调用一下这个 controller 看它是不是可以成功注入所有的属性。我们转战到 postman 发送一个请求到哪里 61,000 段口号的服务对不对？那我们先看一下这个 name 是不是可以正常获取。点击大家看它的名字是谁保罗是咱给生产环境上配的名字保罗。


OK 看完 name 之后，咱再看一下 words 喊出你的口号 send 这里出现了 god bless you okay 那这里证明咱前面的 name 和 words 属相都可以正常的获取。那讲到这里，咱这章的内容就快要结束了，我来跟大家做一个总结。这一章我们创建了 config client 然后通过两种不同的方式将 github 上的属性注入到了项目中。这两种方式分别是直接使用 value 注入一个 github 上的属性名。第二种方式是将属性名先注入到配置文件，然后再从配置文件中注入到我们的代码里。


除了这部分的知识，咱还看了如何在 bootstrap YAML 中定义 config server 的连接串。并且在某种特殊情况下，假如你的 application name 和远端的文件名称中指定的 application 不一致，这种情况下我们知道怎么办，在 config 下面把这个名称重新覆盖掉就可以了。 OK 那这一节的内容就到这里结束了。下一节我们来看一下 config 组件是如何拉取 github 上的资源文件的。 OK 同学们，那我们下一节再见。





