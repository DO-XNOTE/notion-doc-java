---
title: 1-13 【原理实战】K8S存储原理实战-2
---

# 1-13 【原理实战】K8S存储原理实战-2

[image](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/58917c21-bd22-4e82-a62b-26ef516c1cff/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466R3SMUUIO%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T225940Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDRZ0ZkFrFd7DpzQLtRMK%2FQ7NDdFF3c4L4YznSUPuWFbgIhAO3IIDryVSvV5PH%2FOYgUqJg2PK3MqrudQxroCcu2ZpVuKogECMb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgzCn%2BWsqE9gC%2B%2FiqOkq3AMxfe2C3UuGmjtTK3c1UdsMQEdNTCqezDPep0QIeLOqtin1N%2BC5eK8oAAl8VPDpmJm87apFrn6lxOQB8o%2FSBoY4T4xX%2Ba4MDQQEQTTjO2s6dyT2afLm5x4CEkYMtui9CdhpsYIlM8tjtL2UvHg50cPz4jaJ9XkQMPnM%2F8l1Xpi%2FcMHvI1iPf%2BOD8FoGYVjTYlGwIJMU3ZNI3KkG5pgTQJdjBGErewl%2BKibNbjloDaE0tlNf8UsPTx2nRoxGG%2BognGqlIWis%2BcVj36BHR%2BIyIpTjab1%2FZJ6tbfsk573%2FTNk%2BDBiTpumI9JpI8NRzMPANyGFrg9Nf4n57Kk3CFfeR2zlLd8OJMcv7uE3JuFpZK5oYrmJewOtyCemQb8GHMAr%2FlmuexgOHAdMfCelVcSBAYIfTL12nKKIvmSmuTUGrtreXarGaVhzFYieHPh9yNucl0bfXJkFmejJSq%2BpQL13bqbEhV%2F0x9QnjWwRe6QWjIRrUdi0HoIhaVqRDOIhJNZNNc%2BtnPOmsCYLTsR4n9W8w6rw2W7oklTYr27BDdzWq0Pi1uwIJNlUo9dlIDl1OYH1oRwHbJCuJ0ZUxp81Bxy0x2vjLNBsnlTs9TNDwEPnkIcURPglUaFlt6ns3v%2FXtQTCVt%2F%2FSBjqkAYMghMkwjFcnkyzTdb30ETY8kha9Lg0PCxfEIjAEWLzY6f4af1w2cdDNFN%2B82B1A0NapJTwGs27qxUapVto1roCrdIfjQmoAHAjawvcsmW5kj7%2Bmp7c1ikzzKfEY3f4XLNezRbLhMxkGFUAMn%2F%2BUeexl6TiuW0s0yt4OfupuhlM8XYaQ6ktHHrDlL5S7swKBHwjwkn0DcrbKYboc%2BFGApS%2F9H2xm&X-Amz-Signature=4d8ed6c0b7cde3056ecde33f138c7048cc16a4ecf387cd40036d2b9f26efff9e&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

[image](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/4e9c205d-fcb0-4fe4-8d55-d06fcf966d8f/SCR-20240726-efol.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466R3SMUUIO%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T225940Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDRZ0ZkFrFd7DpzQLtRMK%2FQ7NDdFF3c4L4YznSUPuWFbgIhAO3IIDryVSvV5PH%2FOYgUqJg2PK3MqrudQxroCcu2ZpVuKogECMb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgzCn%2BWsqE9gC%2B%2FiqOkq3AMxfe2C3UuGmjtTK3c1UdsMQEdNTCqezDPep0QIeLOqtin1N%2BC5eK8oAAl8VPDpmJm87apFrn6lxOQB8o%2FSBoY4T4xX%2Ba4MDQQEQTTjO2s6dyT2afLm5x4CEkYMtui9CdhpsYIlM8tjtL2UvHg50cPz4jaJ9XkQMPnM%2F8l1Xpi%2FcMHvI1iPf%2BOD8FoGYVjTYlGwIJMU3ZNI3KkG5pgTQJdjBGErewl%2BKibNbjloDaE0tlNf8UsPTx2nRoxGG%2BognGqlIWis%2BcVj36BHR%2BIyIpTjab1%2FZJ6tbfsk573%2FTNk%2BDBiTpumI9JpI8NRzMPANyGFrg9Nf4n57Kk3CFfeR2zlLd8OJMcv7uE3JuFpZK5oYrmJewOtyCemQb8GHMAr%2FlmuexgOHAdMfCelVcSBAYIfTL12nKKIvmSmuTUGrtreXarGaVhzFYieHPh9yNucl0bfXJkFmejJSq%2BpQL13bqbEhV%2F0x9QnjWwRe6QWjIRrUdi0HoIhaVqRDOIhJNZNNc%2BtnPOmsCYLTsR4n9W8w6rw2W7oklTYr27BDdzWq0Pi1uwIJNlUo9dlIDl1OYH1oRwHbJCuJ0ZUxp81Bxy0x2vjLNBsnlTs9TNDwEPnkIcURPglUaFlt6ns3v%2FXtQTCVt%2F%2FSBjqkAYMghMkwjFcnkyzTdb30ETY8kha9Lg0PCxfEIjAEWLzY6f4af1w2cdDNFN%2B82B1A0NapJTwGs27qxUapVto1roCrdIfjQmoAHAjawvcsmW5kj7%2Bmp7c1ikzzKfEY3f4XLNezRbLhMxkGFUAMn%2F%2BUeexl6TiuW0s0yt4OfupuhlM8XYaQ6ktHHrDlL5S7swKBHwjwkn0DcrbKYboc%2BFGApS%2F9H2xm&X-Amz-Signature=6f1261743525ef8ff2e1ffad9334bb10e22c147b04cf4689c03e1ae2ec591797&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

[image](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/f79b5545-96fd-497c-a386-d3f3729f0767/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466R3SMUUIO%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T225940Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDRZ0ZkFrFd7DpzQLtRMK%2FQ7NDdFF3c4L4YznSUPuWFbgIhAO3IIDryVSvV5PH%2FOYgUqJg2PK3MqrudQxroCcu2ZpVuKogECMb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgzCn%2BWsqE9gC%2B%2FiqOkq3AMxfe2C3UuGmjtTK3c1UdsMQEdNTCqezDPep0QIeLOqtin1N%2BC5eK8oAAl8VPDpmJm87apFrn6lxOQB8o%2FSBoY4T4xX%2Ba4MDQQEQTTjO2s6dyT2afLm5x4CEkYMtui9CdhpsYIlM8tjtL2UvHg50cPz4jaJ9XkQMPnM%2F8l1Xpi%2FcMHvI1iPf%2BOD8FoGYVjTYlGwIJMU3ZNI3KkG5pgTQJdjBGErewl%2BKibNbjloDaE0tlNf8UsPTx2nRoxGG%2BognGqlIWis%2BcVj36BHR%2BIyIpTjab1%2FZJ6tbfsk573%2FTNk%2BDBiTpumI9JpI8NRzMPANyGFrg9Nf4n57Kk3CFfeR2zlLd8OJMcv7uE3JuFpZK5oYrmJewOtyCemQb8GHMAr%2FlmuexgOHAdMfCelVcSBAYIfTL12nKKIvmSmuTUGrtreXarGaVhzFYieHPh9yNucl0bfXJkFmejJSq%2BpQL13bqbEhV%2F0x9QnjWwRe6QWjIRrUdi0HoIhaVqRDOIhJNZNNc%2BtnPOmsCYLTsR4n9W8w6rw2W7oklTYr27BDdzWq0Pi1uwIJNlUo9dlIDl1OYH1oRwHbJCuJ0ZUxp81Bxy0x2vjLNBsnlTs9TNDwEPnkIcURPglUaFlt6ns3v%2FXtQTCVt%2F%2FSBjqkAYMghMkwjFcnkyzTdb30ETY8kha9Lg0PCxfEIjAEWLzY6f4af1w2cdDNFN%2B82B1A0NapJTwGs27qxUapVto1roCrdIfjQmoAHAjawvcsmW5kj7%2Bmp7c1ikzzKfEY3f4XLNezRbLhMxkGFUAMn%2F%2BUeexl6TiuW0s0yt4OfupuhlM8XYaQ6ktHHrDlL5S7swKBHwjwkn0DcrbKYboc%2BFGApS%2F9H2xm&X-Amz-Signature=f06355e7937b37fa0d38ba02d62d13078c60216fb2135f1d0e01c58ac37dab86&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

[image](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/87949660-17c7-4a5b-abf9-777ddd7a7b84/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466R3SMUUIO%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T225940Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDRZ0ZkFrFd7DpzQLtRMK%2FQ7NDdFF3c4L4YznSUPuWFbgIhAO3IIDryVSvV5PH%2FOYgUqJg2PK3MqrudQxroCcu2ZpVuKogECMb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgzCn%2BWsqE9gC%2B%2FiqOkq3AMxfe2C3UuGmjtTK3c1UdsMQEdNTCqezDPep0QIeLOqtin1N%2BC5eK8oAAl8VPDpmJm87apFrn6lxOQB8o%2FSBoY4T4xX%2Ba4MDQQEQTTjO2s6dyT2afLm5x4CEkYMtui9CdhpsYIlM8tjtL2UvHg50cPz4jaJ9XkQMPnM%2F8l1Xpi%2FcMHvI1iPf%2BOD8FoGYVjTYlGwIJMU3ZNI3KkG5pgTQJdjBGErewl%2BKibNbjloDaE0tlNf8UsPTx2nRoxGG%2BognGqlIWis%2BcVj36BHR%2BIyIpTjab1%2FZJ6tbfsk573%2FTNk%2BDBiTpumI9JpI8NRzMPANyGFrg9Nf4n57Kk3CFfeR2zlLd8OJMcv7uE3JuFpZK5oYrmJewOtyCemQb8GHMAr%2FlmuexgOHAdMfCelVcSBAYIfTL12nKKIvmSmuTUGrtreXarGaVhzFYieHPh9yNucl0bfXJkFmejJSq%2BpQL13bqbEhV%2F0x9QnjWwRe6QWjIRrUdi0HoIhaVqRDOIhJNZNNc%2BtnPOmsCYLTsR4n9W8w6rw2W7oklTYr27BDdzWq0Pi1uwIJNlUo9dlIDl1OYH1oRwHbJCuJ0ZUxp81Bxy0x2vjLNBsnlTs9TNDwEPnkIcURPglUaFlt6ns3v%2FXtQTCVt%2F%2FSBjqkAYMghMkwjFcnkyzTdb30ETY8kha9Lg0PCxfEIjAEWLzY6f4af1w2cdDNFN%2B82B1A0NapJTwGs27qxUapVto1roCrdIfjQmoAHAjawvcsmW5kj7%2Bmp7c1ikzzKfEY3f4XLNezRbLhMxkGFUAMn%2F%2BUeexl6TiuW0s0yt4OfupuhlM8XYaQ6ktHHrDlL5S7swKBHwjwkn0DcrbKYboc%2BFGApS%2F9H2xm&X-Amz-Signature=0f9a1255a04756945e56f23642df5e5c24aa663d86313281783e99868e878753&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

[image](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/0c3cf086-a509-4931-a9de-bc2489721386/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466R3SMUUIO%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T225940Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDRZ0ZkFrFd7DpzQLtRMK%2FQ7NDdFF3c4L4YznSUPuWFbgIhAO3IIDryVSvV5PH%2FOYgUqJg2PK3MqrudQxroCcu2ZpVuKogECMb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgzCn%2BWsqE9gC%2B%2FiqOkq3AMxfe2C3UuGmjtTK3c1UdsMQEdNTCqezDPep0QIeLOqtin1N%2BC5eK8oAAl8VPDpmJm87apFrn6lxOQB8o%2FSBoY4T4xX%2Ba4MDQQEQTTjO2s6dyT2afLm5x4CEkYMtui9CdhpsYIlM8tjtL2UvHg50cPz4jaJ9XkQMPnM%2F8l1Xpi%2FcMHvI1iPf%2BOD8FoGYVjTYlGwIJMU3ZNI3KkG5pgTQJdjBGErewl%2BKibNbjloDaE0tlNf8UsPTx2nRoxGG%2BognGqlIWis%2BcVj36BHR%2BIyIpTjab1%2FZJ6tbfsk573%2FTNk%2BDBiTpumI9JpI8NRzMPANyGFrg9Nf4n57Kk3CFfeR2zlLd8OJMcv7uE3JuFpZK5oYrmJewOtyCemQb8GHMAr%2FlmuexgOHAdMfCelVcSBAYIfTL12nKKIvmSmuTUGrtreXarGaVhzFYieHPh9yNucl0bfXJkFmejJSq%2BpQL13bqbEhV%2F0x9QnjWwRe6QWjIRrUdi0HoIhaVqRDOIhJNZNNc%2BtnPOmsCYLTsR4n9W8w6rw2W7oklTYr27BDdzWq0Pi1uwIJNlUo9dlIDl1OYH1oRwHbJCuJ0ZUxp81Bxy0x2vjLNBsnlTs9TNDwEPnkIcURPglUaFlt6ns3v%2FXtQTCVt%2F%2FSBjqkAYMghMkwjFcnkyzTdb30ETY8kha9Lg0PCxfEIjAEWLzY6f4af1w2cdDNFN%2B82B1A0NapJTwGs27qxUapVto1roCrdIfjQmoAHAjawvcsmW5kj7%2Bmp7c1ikzzKfEY3f4XLNezRbLhMxkGFUAMn%2F%2BUeexl6TiuW0s0yt4OfupuhlM8XYaQ6ktHHrDlL5S7swKBHwjwkn0DcrbKYboc%2BFGApS%2F9H2xm&X-Amz-Signature=5b43e990d5af0625054be0eceba09501617b79e48e0af34983b76d1f622972c2&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

着讲我们的存储刚刚讲过了我们的基本的卷的配置，那这里看看怎么样去配置我们的容器所需要的配置系统 config 怎么样去部署我们的容器所需要的用户名密码的呢？常用的创建方式是这样一种是用什么 kubernetes 直接从这个命令行里面直接输入，就把那些什么用户名密码配置详情信息 care value 直接在命令行里输入，这个是非常少见的一个用法。


那另外一个用法是从一个一个的 file 里面输入，比如你要输入用户名和密码，那你要建一个文件叫 username 的文件，然后里面把它的用户名存进去，然后你要传一个 key value 那 key 叫 pass 我的 value 比如叫1234。你那个时候你要建一个这个文件叫什么叫 pass 我的，然后这个文件里面内容要传1234，这相对来说也是有点麻烦。


那另外还有一个方法是传一个 emv far 这个里面，把一对一对的键值全部提前写在里面。那这是一种方法。那更推荐的方法是什么？还是用羊毛基于羊毛的里面的那个类型叫 secret 类型，然后在里面传一个 data 这样一个字段，把大量的 key value 全部部署在里面。


通过 apply 这个 YAML 可以很方便的把我们的什么不管是我们的 config map 还是我们的 secured 都把它打包进去，然后一起部署到我们的什么容器里面。那这里也要提一下， config map 相当于是键值对的明文配置。但是 secret 跟 config map 其实唯一的区别是什么？是 secret 要求把所有的值用 base 64 给编码一下。虽然不是加密，但至少编码以后，你不能从明文用一眼就看出这个人习惯用哪些密码，对相对来说会好一点。对，我们这次 demo 我会以麻烦一点的 secret 为例，来给大家看一下怎么样 base 64 编码，然后输入到 YAML 里面。


最后 apply 进去以后，在容器是怎么样使用的好吗？具体容器使用的方法其实也有两种，一种是容器把它当成一个卷，就是把这个 secret 当成之前文件系统卷的形式来进行 mount 还有一种是传环境变量，那传环境变量大家其实也可以作为一个小作业去实战一下，我这里就不重点带大家 demo 了。


原因是因为传环境变量它是一个临时性的，也就说在系统启动的时候，就在 POD 创建的时候，它传进去以后，如果你再把那个原来 secret 所在的那些值一些羊毛的那个内容，就是之前创建的这个我们上面创建的这个 secret 羊毛内容进行改动以后重新apply ，这个值不会在我们已经运行的 POD 里生效的，因为只有哪种模式只有左边的这种 volume 模式才可以使得我们只是可以不停的改变。那这个值都会读入到 POD 里面， POD 里面内容值也会更的改变，相对来说这是一个更高级的传递方式。所以我们会 volume 然后以 YAML 创建，以 volume 传递以 secret 就是要 base 64 编码的这个用户为密码。这个例子为例来给大家演示一下。


好，我们切换到这个命令银行界面，请看一下屏幕，那我们就开始创建我们这个 secret 了。那一样的 secret 创建也是需要有一个羊毛发，我们可以写在原来的那个就是我们的 POD 的羊毛发里面也可以新建一个。我们这里推荐是新建一个这个叫 my secret 的 YAML 发。


好，我们进去以后大家一如既往是吧，都很熟了，API version 这是比较简单的，所以写 V one 就可以了。然后 kind secret 第一个字母，kind后面的 secret CS 第一字母大写好，下面选 meta data 然后我们 meta data 里面通常是什么，也就写个 name 就够了对吧。 name 空格，选上我们的 name 叫 my C correct 好就可以了。那后面就是填真正的键值对内容了。那这个键值的内容属于哪个分类呢？属于 data 那个分类，它可以填很多个。那我们其实就假设传两个，一个用户名，一个密码好不好？ username 叫什么叫 aaa 然后 password 叫 bbb 好吧，但是我们其实可以看一下，这里应该传什么是 base 64 的结果。所以我们先保存退出一下，我们先保存它那个反应有点慢。好，出来了，稍等，整个机器是有点卡打下去。那个什么 EC 什么杠 W 什么Q ，都有点不无需要的感觉。


好，我们出来以后，我们假设用户名叫 AA 好，密码叫 bbb echo 杠 NA AA 然后我们要进行一个 base 又是4， base 又是4，用管道符传给 base 64 稍等一下，我打出去的这个字要稍微等一会。看到吗？就是我挨扣一个数字叫 aaa 然后我不代替什么回车，杠 N 比较干净的。然后白色64。好，这个值就是把这个值替换里面的用户名稍等一下。好，那再移动鼠标好移动到位了，然后进行替换。这里要注意是什么？有个空格对吧？然后我们替换刚刚复制的那段内容，然后同样的密码， bbb 要进行一个编码，我们这里还是 wq 退出。然后 echo 一个密码叫 bbb 也是 base 64 编码，我们等那个远端的服务器给我们回显命令行回显。


好了，回显出来了，我们把这个内容也贴到我们的 my secret 里面，替换刚刚的 bbb 好也注意空格，然后替换。替换完了以后保存退出。这样就是我们一段这个 secret 已经好了，我们可以什么库博 CTR 然后用 play 杠 F my secret 去生效这个研发文件，这个 secret 已经创建出来了，我们可以看一下。 get 对吧。


secret get 某个类型，我们这个类型是 secret 有个 default 的 token 是系统默认的，我们不用管。我们看一下 mysecret 类型是我刚刚建了一个什么 opaque 比较透明的一个方式，就是 base 64 编码的这个用户源密码后面是 AA 和 bbb 这个弄完以后我们要用到它对不对？怎么用呢？我们还是以之前我们之前对的 my engines 这个 POD 的羊毛文件为例，我们去修改一下，我们用 volvo 的形式去使用这个 secret 好我们登录到这个就是 VI 进去这个 POD 我们这次不要选什么 volumes 什么 persistent volume claim 好吧，那正常情况其实通常是不是用宏伟密码会映射到一个什么 etc 目录是吧，但是任何目录其实都可以工作的。所以我们这里依然还意识到 my mount 目录不做改动。


那只是我们把底下 volume 的类型给改掉好不好？ volume 类型就改成我们刚刚的什么 secret 的类型，所以在这里就是要全部把它删掉，然后选择 secret 类型。那下面把 secret name 对吧，mysecret输进去。所以如果改成，因为你有点慢了，我们用 DD DD 3 行会快一些。
好，我们再用 insert 模式到这一行的末尾，还有点卡，我们要在这跟 name 平起，就是四个空格这个位置地方输 secret 然后我们这里面输实际的就是 6 个空格以后输实际的 secret ratethe main 就是我们刚刚定义的什么我们刚刚定义的 my secret 对吧，然后我们这边保存一下来看是不是没写错。好， my secret 保存我们重新。因为可以，其实大家可以预想到应该是不会成功对吧，因为我们什么修改了又是卷的模式，但我们还是一如既往，我们尝试一下，看一下能不能我们的 rolling update 这个事好不行对吧，大家可以预见了。然后我们 delete 掉之前的那个什么我们的这个 POD my engines 是吧，我们迭代掉以后重新 apply 对吧，这样它的卷就才能真正的生效。那这个卷其实什么就是个 secret 好，我们库把 CTR get 一下，POD我们看看是不是已经强了，my agency 在 8 秒钟之前已经起来了。那这个时候我们再用之前说的方法，杠 it exact 杠 it 我们登进这个 my engines 然后我们选 being bash 这个方式，我们实际的去看一下是不是把那两个值给传进去了。


好，已经登进去了，我们切到什么？ my mount 这个目录两个文件已经有了对吧？它在这个 mount 进去以后，它的文件名就是 key 值就是 value 我们把这个文件的内容 cat 出来看一下是不是 AA 你可以看一下就是它这个传值的特点是什么？它传进去以后不会自动带什么带一个回车的，我们是把一个实际的一个值不带回车的值就杠 M 前面就是不带回车的值，把它编成 base 64。所以它传进去以后，它的实际的值是在 root 左边的右边是值对吧，右边是我们的那个命令行，这个 PS 1 PS 2 的输出值是这个 aaa 不带回车，这其实也就是我们正常平时实际使用当中要用到的。如果我们程序去读，我们会读出来一个真正的值叫 AA 而不是 AA 斜杠 an 同样道理，让我们看 password 是不是实际值是什么，bbb我们不会读出来一个 bbb 杠斜杠 A 这就是我们正常我们比如说 Java 代码所正常所需要读到的值，现在它的值和 value 全部以文件的形式 mount 进来。


好，我们退出这个，我们尝试去做一个修改。假设我们把密码改成 CCC 我们看一下我们是不是一如既往能够很方便的拿到这个值。那怎么改成 CCC 呢？ echo N 对吧。 CCC 我们写成要 base 64 编码一下，把这个具体值知道我们拿到这个 CCC 的值了对吧，我们去替换什么？我们去替换刚刚的那个 my secret 这个加盟，或者，你用什么 coupa control edit 也可以进行修改。但是平时为了什么落盘为准这种原则我们通常还是以建议说把阳光改掉。那保证你的什么你的本地的静态的落盘的数据和我们动态的这个实际配置是一致的，能通过 apply 的形式来进行修改。库包 CTR 是吧？ apply 杠 F 我们只要 apply 这个 mysecret 就行了。 POD 其实并不需要修改了。


好，稍等一下，有点卡了。
好了，已经生成完成了，我们再登进那个机器看一下，应该是过了几秒钟的时间，它就能够正常的更新进去了。我们重新登录刚刚那个什么 my ending 这个 POD 登进去了，我们再到我们的 my mount 目录进去了。我们看一下还是有两个文件，我们再看一下 password 会怎么样呢？是不是如预期的会修改。还没有修改，那这证明什么时间可能还没有到，我们稍等片刻，我们退出，再稍等片刻，我们看一下 coupe ctl get a secret 看看它的状态是不是更新成功好吗？说什么？他说是 6 分 19 秒之前有这样一个值，似乎还是没有完全更新成功。


我们扩包 CT 2 我们用什么？我们用 describe 来看一下是不是跟我们最后改的那个 y2n 节相关。 describe 不仅可以看 POD 看 deployment 也可以看什么各种各样其他的服务。好包括什么？Secret. describe 基本上靠盲打灰显太慢。 mysecret 好，不是 mysecret 类型是 secret 稍等 secret 好，然后跟上 my secret 对吧，先讲类型再讲具体内容。 describe 还打错了，就是网络当中比较慢的时候就比较的卡顿你看基本上打字这都是错的位置回显跟实际输出值都会互相之间有冲突。


好看到了，你看到什么？他是说 opaque 具体值他不能告诉你对吧，所以你还要到这个实际的登录状态当中去看 annotations 他故意把什么把这两个值给抹掉了。好，我们估计现在时间差不多了，如果成功的话应该已经更新进去。好，我们再登进去看一下。 you apply sorry 没有 change 对吧。刚刚又 apply 的原因什么？是因为我看到其实不是 apply 但是等到回显完毕以后，其实这个命令已经刷到 apply 了。好，我们再看一下等一会。没有变，那就是这个找到合适的命令了，这个整个命令回显什么？确实比较麻烦，因为什么？因为库布内特斯大量的应用软件全部要连公网，连谷歌连那个外网。所以我在那个美国那边找了三台机器，看是不是已经变了。看到没有，它要等一些时间，可能秒级到分钟，级它的值就会变。不是因为我们后面第二次 apply 导致的。因为 apply 根本什么都没有变，只是时间等待一定的时间，它会自动的刷新进去。
好，这个过程其实已经把我们刚刚要说的几个点的介绍了是吧，就是传递的方式用 volume 能够保证你不停的去更新你的那个 secret 是过一阵子以后，它会自动的刷新到我们的这个配置文件里。如果你从 em V 传递，它只是在启动的时候读取以后再也不会改变了。


那创建方法会推荐什么用羊毛的方式进行创建？好大家可以回想一下 config map 跟 secret 是不是跟之前那个 volume 几乎是一样的方法很像那个什么 MTD I 那个方法其实差不多的，我们只要是用不同的类型来实现存储的保存和传递。


config 是一个类型， secret 是个类型是吧，我们的普通的那个什么存储的这种驱动存储的类型，或者说 pbcvpb C 这些都是一些类型。那通过这些类型，很方便的把数据持久化，同时把数据持久化的数据分享给更多的什么服务器，分享给更多的不同的 POD 里面的不同的容器。好，这一块介绍完毕以后，后面我们会进入一个比较深奥的环节，或者说比较拗口的环节。什么用户认证、安全管理这一块。好，大家敬请期待。


