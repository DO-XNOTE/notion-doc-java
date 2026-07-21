---
title: 2-3【技术改造】电商系统集成Config-用户中心改造
---

# 2-3【技术改造】电商系统集成Config-用户中心改造

[image](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/2ef8f463-9ce9-4c59-85bd-8a4725fa4186/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SRUIFPC6%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T225717Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCICAldkWGdyvDRoaiMFfA9fRSoe3SAy8dF7YRN0nQwkkpAiBLemaB239EEA8fTRCWXtl9v8P9vZHUjWn09z97Fi2YSyqIBAjG%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMdu%2BPTw68NVKob8WfKtwDTtUmJAwcHYOT%2Fm4tTbgTF3XElF1mG2B2NzQJcd9IbrtzRVHomEr6N5W1P843ryXoiltbR40qF23KmY0f34i%2F2wQxmgwU6j11Y1cxOm2Xn6EkzwJs6IqnUOJXksCqi8r8EqoDNv5LBgh8iOyi5kaNBwE2EmeU14k9uinOkC1IVaK%2BUpSWtcmPX3LgHwSPi60yEG%2BBRtVdCQ0r5kNqF1iodj3V6e3yQ8FdoQrlzCVXLmOe3rmT7P3oQopJmD7w8E3lLEFYJT5vAxgwMl9SRf8gZ5TH7oYc8mUPsmiJmXWCFqenV7tH8Q2%2BdSq36%2B0tSf8sMNk7VwibrIM4ZfOzHwgFOC3zcNm6vAWZMYjSbhGicmHSZSAcnSA7iwdT6momfm%2FCUBH7W4mjVYfrjOBv2siCsffl70oMe4wRqTt6Bu8GtGTYUREo0sKYXD37zlFWr8X9fOvDm8T3VYzlNaoe1ZhuN6teBPVDXZwcndpZdATASW%2B2cYeVqrr8aCt8ClKhbUiaYWB%2BgXJ96QK99y9KgicA%2BbyyFTnEYaGnSyU7ye8lAquKNizuqMDwFRKzn8kzNzt7z3R4hH3N3gAYuGllB14BMD5XHLJU3P3Jwza5hGmOc039YlhJXJTUjqOLOZswhbn%2F0gY6pgEl8Edns%2F5pI8IrBN58qF%2BLZuxLa%2BENjfWsG%2FD5LCPe4bhdr7aDHfwk3H5uEDJqIym2sn2lH5ob9x0l6DWVGKcL80X2Ke0%2BDO7Cp%2Fa4mcIZwnmPZQlwprAzcb1WGD4wRq32sjjbuBUkRiiy9fyQscizPfK3ox12WqzcwEvFpsICQvUWkxp7vTHyBTYt%2FVAhihM9MC4rgaLRmlA2VftbkJqF8VwYdk8R&X-Amz-Signature=70b6f4f7ea3c727f84774dab601d948470f3712bafb56ea4b76aec7f33d3334c&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

[image](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/c11b0d67-b2ff-48ad-bf40-1bea6f4bd21a/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SRUIFPC6%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T225717Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCICAldkWGdyvDRoaiMFfA9fRSoe3SAy8dF7YRN0nQwkkpAiBLemaB239EEA8fTRCWXtl9v8P9vZHUjWn09z97Fi2YSyqIBAjG%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMdu%2BPTw68NVKob8WfKtwDTtUmJAwcHYOT%2Fm4tTbgTF3XElF1mG2B2NzQJcd9IbrtzRVHomEr6N5W1P843ryXoiltbR40qF23KmY0f34i%2F2wQxmgwU6j11Y1cxOm2Xn6EkzwJs6IqnUOJXksCqi8r8EqoDNv5LBgh8iOyi5kaNBwE2EmeU14k9uinOkC1IVaK%2BUpSWtcmPX3LgHwSPi60yEG%2BBRtVdCQ0r5kNqF1iodj3V6e3yQ8FdoQrlzCVXLmOe3rmT7P3oQopJmD7w8E3lLEFYJT5vAxgwMl9SRf8gZ5TH7oYc8mUPsmiJmXWCFqenV7tH8Q2%2BdSq36%2B0tSf8sMNk7VwibrIM4ZfOzHwgFOC3zcNm6vAWZMYjSbhGicmHSZSAcnSA7iwdT6momfm%2FCUBH7W4mjVYfrjOBv2siCsffl70oMe4wRqTt6Bu8GtGTYUREo0sKYXD37zlFWr8X9fOvDm8T3VYzlNaoe1ZhuN6teBPVDXZwcndpZdATASW%2B2cYeVqrr8aCt8ClKhbUiaYWB%2BgXJ96QK99y9KgicA%2BbyyFTnEYaGnSyU7ye8lAquKNizuqMDwFRKzn8kzNzt7z3R4hH3N3gAYuGllB14BMD5XHLJU3P3Jwza5hGmOc039YlhJXJTUjqOLOZswhbn%2F0gY6pgEl8Edns%2F5pI8IrBN58qF%2BLZuxLa%2BENjfWsG%2FD5LCPe4bhdr7aDHfwk3H5uEDJqIym2sn2lH5ob9x0l6DWVGKcL80X2Ke0%2BDO7Cp%2Fa4mcIZwnmPZQlwprAzcb1WGD4wRq32sjjbuBUkRiiy9fyQscizPfK3ox12WqzcwEvFpsICQvUWkxp7vTHyBTYt%2FVAhihM9MC4rgaLRmlA2VftbkJqF8VwYdk8R&X-Amz-Signature=3cca48a4e71b9e916527b6867c3b020dccde493314798ca351d7ebabe8b73e00&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

[image](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/7dca9bc1-fbf3-4fe3-ad40-940f69c54155/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SRUIFPC6%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T225717Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCICAldkWGdyvDRoaiMFfA9fRSoe3SAy8dF7YRN0nQwkkpAiBLemaB239EEA8fTRCWXtl9v8P9vZHUjWn09z97Fi2YSyqIBAjG%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMdu%2BPTw68NVKob8WfKtwDTtUmJAwcHYOT%2Fm4tTbgTF3XElF1mG2B2NzQJcd9IbrtzRVHomEr6N5W1P843ryXoiltbR40qF23KmY0f34i%2F2wQxmgwU6j11Y1cxOm2Xn6EkzwJs6IqnUOJXksCqi8r8EqoDNv5LBgh8iOyi5kaNBwE2EmeU14k9uinOkC1IVaK%2BUpSWtcmPX3LgHwSPi60yEG%2BBRtVdCQ0r5kNqF1iodj3V6e3yQ8FdoQrlzCVXLmOe3rmT7P3oQopJmD7w8E3lLEFYJT5vAxgwMl9SRf8gZ5TH7oYc8mUPsmiJmXWCFqenV7tH8Q2%2BdSq36%2B0tSf8sMNk7VwibrIM4ZfOzHwgFOC3zcNm6vAWZMYjSbhGicmHSZSAcnSA7iwdT6momfm%2FCUBH7W4mjVYfrjOBv2siCsffl70oMe4wRqTt6Bu8GtGTYUREo0sKYXD37zlFWr8X9fOvDm8T3VYzlNaoe1ZhuN6teBPVDXZwcndpZdATASW%2B2cYeVqrr8aCt8ClKhbUiaYWB%2BgXJ96QK99y9KgicA%2BbyyFTnEYaGnSyU7ye8lAquKNizuqMDwFRKzn8kzNzt7z3R4hH3N3gAYuGllB14BMD5XHLJU3P3Jwza5hGmOc039YlhJXJTUjqOLOZswhbn%2F0gY6pgEl8Edns%2F5pI8IrBN58qF%2BLZuxLa%2BENjfWsG%2FD5LCPe4bhdr7aDHfwk3H5uEDJqIym2sn2lH5ob9x0l6DWVGKcL80X2Ke0%2BDO7Cp%2Fa4mcIZwnmPZQlwprAzcb1WGD4wRq32sjjbuBUkRiiy9fyQscizPfK3ox12WqzcwEvFpsICQvUWkxp7vTHyBTYt%2FVAhihM9MC4rgaLRmlA2VftbkJqF8VwYdk8R&X-Amz-Signature=69bc4ae1e18987f0ac9daa1a8481f522539ec2c3c5ecf653f9584ec757287685&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

各位同学们，大家好，这一小节里，我们就要把前面两节当中准备好的配置中心以及 github 中设置的配置项集成到咱的用户微服务当中。我们来撸起袖子开干了。第一步自然是要把咱的配置中心把它的依赖项加入到咱这个 pom 当中。我们这里把 config server 它的配置项加入进来是 spring cloud starter 杠 config 因为我们有些配置参数要求启动的时候就已经加载好。所以这一项如果依赖没有加入进来，那项目启动它会报错的。那这里依赖项加入进来之后，我们第二步就是去更改咱项目当中的配置文件。


第一个就是要把咱的配置中心它的服务器地址给它配置进来。我们这里打开用户微服务 user web 当中的 bootstrap YAML 在这个注册中心下面我们把配置中心给它打上，那咱先把自家的牌匾配置中心的牌匾给它挂上去，这叫 config 配置中心。 OK 那接下来它的参数很简单， string 开头，接下来是 cloudcloud 下面专门给 config 这里打个节点。

[image](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/34a911aa-b9b6-4788-a591-20d71d91a51d/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SRUIFPC6%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T225717Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCICAldkWGdyvDRoaiMFfA9fRSoe3SAy8dF7YRN0nQwkkpAiBLemaB239EEA8fTRCWXtl9v8P9vZHUjWn09z97Fi2YSyqIBAjG%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMdu%2BPTw68NVKob8WfKtwDTtUmJAwcHYOT%2Fm4tTbgTF3XElF1mG2B2NzQJcd9IbrtzRVHomEr6N5W1P843ryXoiltbR40qF23KmY0f34i%2F2wQxmgwU6j11Y1cxOm2Xn6EkzwJs6IqnUOJXksCqi8r8EqoDNv5LBgh8iOyi5kaNBwE2EmeU14k9uinOkC1IVaK%2BUpSWtcmPX3LgHwSPi60yEG%2BBRtVdCQ0r5kNqF1iodj3V6e3yQ8FdoQrlzCVXLmOe3rmT7P3oQopJmD7w8E3lLEFYJT5vAxgwMl9SRf8gZ5TH7oYc8mUPsmiJmXWCFqenV7tH8Q2%2BdSq36%2B0tSf8sMNk7VwibrIM4ZfOzHwgFOC3zcNm6vAWZMYjSbhGicmHSZSAcnSA7iwdT6momfm%2FCUBH7W4mjVYfrjOBv2siCsffl70oMe4wRqTt6Bu8GtGTYUREo0sKYXD37zlFWr8X9fOvDm8T3VYzlNaoe1ZhuN6teBPVDXZwcndpZdATASW%2B2cYeVqrr8aCt8ClKhbUiaYWB%2BgXJ96QK99y9KgicA%2BbyyFTnEYaGnSyU7ye8lAquKNizuqMDwFRKzn8kzNzt7z3R4hH3N3gAYuGllB14BMD5XHLJU3P3Jwza5hGmOc039YlhJXJTUjqOLOZswhbn%2F0gY6pgEl8Edns%2F5pI8IrBN58qF%2BLZuxLa%2BENjfWsG%2FD5LCPe4bhdr7aDHfwk3H5uEDJqIym2sn2lH5ob9x0l6DWVGKcL80X2Ke0%2BDO7Cp%2Fa4mcIZwnmPZQlwprAzcb1WGD4wRq32sjjbuBUkRiiy9fyQscizPfK3ox12WqzcwEvFpsICQvUWkxp7vTHyBTYt%2FVAhihM9MC4rgaLRmlA2VftbkJqF8VwYdk8R&X-Amz-Signature=94813323ecf2fa11da02b9ce6fdd3ae828c8820cee5786168971c1594285ee87&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

那这下面有什么呢？第一个就是它的 discovery 因为我们是通过 ereca 服务注册中心来拿到 config server 它的具体地址的。这是咱前面讲到的利用 eureka 做配置中心的高可用化，把这个开关给它打开， enable 等于 true 与此同时，我们还要给出你的 service ID 谁的 service ID 像 config server 的 service ID 好，它的 ID 就叫 config 中间一个横杠 server 那咱接下来指定 profile 是 DEV 以及它的 label 是 master 那这个其实是默认选项，写不写都可以的。

[image](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/8a5a13f0-8e7a-4815-8e47-6e38721ad0bf/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SRUIFPC6%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T225717Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCICAldkWGdyvDRoaiMFfA9fRSoe3SAy8dF7YRN0nQwkkpAiBLemaB239EEA8fTRCWXtl9v8P9vZHUjWn09z97Fi2YSyqIBAjG%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMdu%2BPTw68NVKob8WfKtwDTtUmJAwcHYOT%2Fm4tTbgTF3XElF1mG2B2NzQJcd9IbrtzRVHomEr6N5W1P843ryXoiltbR40qF23KmY0f34i%2F2wQxmgwU6j11Y1cxOm2Xn6EkzwJs6IqnUOJXksCqi8r8EqoDNv5LBgh8iOyi5kaNBwE2EmeU14k9uinOkC1IVaK%2BUpSWtcmPX3LgHwSPi60yEG%2BBRtVdCQ0r5kNqF1iodj3V6e3yQ8FdoQrlzCVXLmOe3rmT7P3oQopJmD7w8E3lLEFYJT5vAxgwMl9SRf8gZ5TH7oYc8mUPsmiJmXWCFqenV7tH8Q2%2BdSq36%2B0tSf8sMNk7VwibrIM4ZfOzHwgFOC3zcNm6vAWZMYjSbhGicmHSZSAcnSA7iwdT6momfm%2FCUBH7W4mjVYfrjOBv2siCsffl70oMe4wRqTt6Bu8GtGTYUREo0sKYXD37zlFWr8X9fOvDm8T3VYzlNaoe1ZhuN6teBPVDXZwcndpZdATASW%2B2cYeVqrr8aCt8ClKhbUiaYWB%2BgXJ96QK99y9KgicA%2BbyyFTnEYaGnSyU7ye8lAquKNizuqMDwFRKzn8kzNzt7z3R4hH3N3gAYuGllB14BMD5XHLJU3P3Jwza5hGmOc039YlhJXJTUjqOLOZswhbn%2F0gY6pgEl8Edns%2F5pI8IrBN58qF%2BLZuxLa%2BENjfWsG%2FD5LCPe4bhdr7aDHfwk3H5uEDJqIym2sn2lH5ob9x0l6DWVGKcL80X2Ke0%2BDO7Cp%2Fa4mcIZwnmPZQlwprAzcb1WGD4wRq32sjjbuBUkRiiy9fyQscizPfK3ox12WqzcwEvFpsICQvUWkxp7vTHyBTYt%2FVAhihM9MC4rgaLRmlA2VftbkJqF8VwYdk8R&X-Amz-Signature=adabec5caaa3832af2cdcaed46a9877b797a766cc98d3d2e495cccb9d06e7b82&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

```java


###################################
#
#
#  Eureka 注册中心
#
#
##################################
eureka:
  client:
    service-url:
      defaultZone: http://peer1:20000/eureka, http://peer2:20001/eureka/
#      defaultZone: http://172.16.136.222:20000/eureka/

###################################
#
#
#  Config 配置中心
#
#
##################################
spring:
  cloud:
    config:
#      name: 名称不一样的话用这个name
      discovery:
        enabled: true
        service-id: config-server
      profile: dev
      # 默认
      label: master
```


那前面我们还讲到过，如果你当前的这个项目，它的 application name 和你在 github 上面存放的文件名不一样。那怎么办呢？这里你可以给出指定的一个 name 那这里你把你自己想要拉取的这个文件的文件名给它写上。 OK 那到这里咱的配置中心的连接字符串这里都已经搞定了。下面让我们转移到配置文件当中。哪一个配置文件呢？ application DEV 好，在这里面我们要把什么替换掉啊？数据库连接字符串和密码这两个我们要把它替换掉。我们先把这个 URL 替换成谁呢？替换成我们在 github 上面配置的 maria db.url 好，这就可以了。那接下来 password 怎么配置呢？ password 我们依然采用同样的方式 mariadb.password 那这里就不用再添加 cipher 这个接头暗号了。咱的配置中心在拉取 github 文件的时候，会自动做这一步解密操作。
好，那到这里咱的 data source 就已经配置完了，

[image](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/b7abf76f-03d8-41ab-8cb4-9461387b9714/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SRUIFPC6%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T225717Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCICAldkWGdyvDRoaiMFfA9fRSoe3SAy8dF7YRN0nQwkkpAiBLemaB239EEA8fTRCWXtl9v8P9vZHUjWn09z97Fi2YSyqIBAjG%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMdu%2BPTw68NVKob8WfKtwDTtUmJAwcHYOT%2Fm4tTbgTF3XElF1mG2B2NzQJcd9IbrtzRVHomEr6N5W1P843ryXoiltbR40qF23KmY0f34i%2F2wQxmgwU6j11Y1cxOm2Xn6EkzwJs6IqnUOJXksCqi8r8EqoDNv5LBgh8iOyi5kaNBwE2EmeU14k9uinOkC1IVaK%2BUpSWtcmPX3LgHwSPi60yEG%2BBRtVdCQ0r5kNqF1iodj3V6e3yQ8FdoQrlzCVXLmOe3rmT7P3oQopJmD7w8E3lLEFYJT5vAxgwMl9SRf8gZ5TH7oYc8mUPsmiJmXWCFqenV7tH8Q2%2BdSq36%2B0tSf8sMNk7VwibrIM4ZfOzHwgFOC3zcNm6vAWZMYjSbhGicmHSZSAcnSA7iwdT6momfm%2FCUBH7W4mjVYfrjOBv2siCsffl70oMe4wRqTt6Bu8GtGTYUREo0sKYXD37zlFWr8X9fOvDm8T3VYzlNaoe1ZhuN6teBPVDXZwcndpZdATASW%2B2cYeVqrr8aCt8ClKhbUiaYWB%2BgXJ96QK99y9KgicA%2BbyyFTnEYaGnSyU7ye8lAquKNizuqMDwFRKzn8kzNzt7z3R4hH3N3gAYuGllB14BMD5XHLJU3P3Jwza5hGmOc039YlhJXJTUjqOLOZswhbn%2F0gY6pgEl8Edns%2F5pI8IrBN58qF%2BLZuxLa%2BENjfWsG%2FD5LCPe4bhdr7aDHfwk3H5uEDJqIym2sn2lH5ob9x0l6DWVGKcL80X2Ke0%2BDO7Cp%2Fa4mcIZwnmPZQlwprAzcb1WGD4wRq32sjjbuBUkRiiy9fyQscizPfK3ox12WqzcwEvFpsICQvUWkxp7vTHyBTYt%2FVAhihM9MC4rgaLRmlA2VftbkJqF8VwYdk8R&X-Amz-Signature=1d28a3218b5bd998df973c85ebace11286e608a8b51538328099aa7b8be25447&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

这是咱在实际项目当中经常用到的一种配置方式。那接下来同学们看一下另外一种配置方式这种配置方式叫什么叫无招胜有招怎么说 activator 端叠，咱是不是把这些配置通通的都放到了咱在 github 当中的 foodie user service YAML 这个配置文件当中去了。你看这些端口都已经在这开放了。



所以我们这里如果引入的时候怎么引入呢？我们还需要像前面一样写一个属性 key 的引用吗？比如说在 always 这里，把前面这一串 key 给它引用进来还用吗？不需要了。同学们，因为咱在这里所要配置的这些属性，它的 key 和你在 github 上面文件中声明的 key 是完全一样的。所以在咱项目启动的时候，它第一步就是去配置中心拉取这些属性，那这些属性自动的就会加载到上下文当中。因为是有一样的 key 所以我们这里可以直接把它删掉，这就叫无招胜有招，我们这里就不用重复配置了。


那上面这几个属性为什么需要这样配置啊？那同学们看这个 key 是不一样的。那如果你把这两个给它拿掉了，那咱 spring boot 就抓瞎了，他不知道该从配置文件中的哪个 key 去找正确的连接串和 passwordok 那这两步配置完了，咱还有一个属性是谁呢？是注册功能的开启和关闭。

[image](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/2411e679-d987-42de-aaec-1e1bbf4fe0fa/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SRUIFPC6%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T225717Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCICAldkWGdyvDRoaiMFfA9fRSoe3SAy8dF7YRN0nQwkkpAiBLemaB239EEA8fTRCWXtl9v8P9vZHUjWn09z97Fi2YSyqIBAjG%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMdu%2BPTw68NVKob8WfKtwDTtUmJAwcHYOT%2Fm4tTbgTF3XElF1mG2B2NzQJcd9IbrtzRVHomEr6N5W1P843ryXoiltbR40qF23KmY0f34i%2F2wQxmgwU6j11Y1cxOm2Xn6EkzwJs6IqnUOJXksCqi8r8EqoDNv5LBgh8iOyi5kaNBwE2EmeU14k9uinOkC1IVaK%2BUpSWtcmPX3LgHwSPi60yEG%2BBRtVdCQ0r5kNqF1iodj3V6e3yQ8FdoQrlzCVXLmOe3rmT7P3oQopJmD7w8E3lLEFYJT5vAxgwMl9SRf8gZ5TH7oYc8mUPsmiJmXWCFqenV7tH8Q2%2BdSq36%2B0tSf8sMNk7VwibrIM4ZfOzHwgFOC3zcNm6vAWZMYjSbhGicmHSZSAcnSA7iwdT6momfm%2FCUBH7W4mjVYfrjOBv2siCsffl70oMe4wRqTt6Bu8GtGTYUREo0sKYXD37zlFWr8X9fOvDm8T3VYzlNaoe1ZhuN6teBPVDXZwcndpZdATASW%2B2cYeVqrr8aCt8ClKhbUiaYWB%2BgXJ96QK99y9KgicA%2BbyyFTnEYaGnSyU7ye8lAquKNizuqMDwFRKzn8kzNzt7z3R4hH3N3gAYuGllB14BMD5XHLJU3P3Jwza5hGmOc039YlhJXJTUjqOLOZswhbn%2F0gY6pgEl8Edns%2F5pI8IrBN58qF%2BLZuxLa%2BENjfWsG%2FD5LCPe4bhdr7aDHfwk3H5uEDJqIym2sn2lH5ob9x0l6DWVGKcL80X2Ke0%2BDO7Cp%2Fa4mcIZwnmPZQlwprAzcb1WGD4wRq32sjjbuBUkRiiy9fyQscizPfK3ox12WqzcwEvFpsICQvUWkxp7vTHyBTYt%2FVAhihM9MC4rgaLRmlA2VftbkJqF8VwYdk8R&X-Amz-Signature=68409a3b3fc108eb19f16a6eb74d8f9561b00020335f044a237d907939199581&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

好，那接下来，我们这里打开 food user web 先在这个顶层目录下面 com.imock.user 这边创建一个专门的配置类。那这个配置类是用来做什么的呢？它专门用来管理这些外部注入的属性。所以我们把它起名叫 user application practice 好创建出来，然后在这里给它添加一些注解。第一个注解 configuration 好给它添加上去。接下来第二个注解我们要把 config 包下面的 RefreshScope 这个注解给它添加进来。因为咱们的注册功能我希望从外部控制它的开启和关闭，它是可以在运行期间不断刷新的。


OK 那好我们这里再给大家加个 long book 的 data 注解。接下来就要把咱外部配置的这个属性给它引入进来。我们声明一个 private 的变量，它的类型是布尔值，然后它的名称我们给它叫 disable registration 那我们这里就通过 value 这一个注解把它给添加进来。那它的 key 还记得是什么吗？ user service.registration.disabled 那把这个注入进来了之后，接下来我们就要找一个地方把它用上，从哪里用呢？咱找到这个 passport controller 然后去找到它的注册 register 这个方法。 OK 在这个方法的第一步，我们就直接的把这个判断条件给它加上。那这个判断条件的开关在哪？在咱刚才配置的 practice 文件里面对不对？所以我们这里把它给引入进来叫 user application properties 引入进来以后就好办了。我这里只用直接判断 if if 谁只用看你的这个注册功能是不是被禁用了。那如果这个值显示的是 true 那我这里要给你返回一段话术。什么话术呢？就是告诉你现在正忙之类的，请稍后再试。好，我们直接把下面这个 return 给它添加上去。这里我要告诉他当前注册用户过多，请稍后再试。

[image](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/2b964687-2abb-4c35-938f-aa35428f595b/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SRUIFPC6%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T225717Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCICAldkWGdyvDRoaiMFfA9fRSoe3SAy8dF7YRN0nQwkkpAiBLemaB239EEA8fTRCWXtl9v8P9vZHUjWn09z97Fi2YSyqIBAjG%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMdu%2BPTw68NVKob8WfKtwDTtUmJAwcHYOT%2Fm4tTbgTF3XElF1mG2B2NzQJcd9IbrtzRVHomEr6N5W1P843ryXoiltbR40qF23KmY0f34i%2F2wQxmgwU6j11Y1cxOm2Xn6EkzwJs6IqnUOJXksCqi8r8EqoDNv5LBgh8iOyi5kaNBwE2EmeU14k9uinOkC1IVaK%2BUpSWtcmPX3LgHwSPi60yEG%2BBRtVdCQ0r5kNqF1iodj3V6e3yQ8FdoQrlzCVXLmOe3rmT7P3oQopJmD7w8E3lLEFYJT5vAxgwMl9SRf8gZ5TH7oYc8mUPsmiJmXWCFqenV7tH8Q2%2BdSq36%2B0tSf8sMNk7VwibrIM4ZfOzHwgFOC3zcNm6vAWZMYjSbhGicmHSZSAcnSA7iwdT6momfm%2FCUBH7W4mjVYfrjOBv2siCsffl70oMe4wRqTt6Bu8GtGTYUREo0sKYXD37zlFWr8X9fOvDm8T3VYzlNaoe1ZhuN6teBPVDXZwcndpZdATASW%2B2cYeVqrr8aCt8ClKhbUiaYWB%2BgXJ96QK99y9KgicA%2BbyyFTnEYaGnSyU7ye8lAquKNizuqMDwFRKzn8kzNzt7z3R4hH3N3gAYuGllB14BMD5XHLJU3P3Jwza5hGmOc039YlhJXJTUjqOLOZswhbn%2F0gY6pgEl8Edns%2F5pI8IrBN58qF%2BLZuxLa%2BENjfWsG%2FD5LCPe4bhdr7aDHfwk3H5uEDJqIym2sn2lH5ob9x0l6DWVGKcL80X2Ke0%2BDO7Cp%2Fa4mcIZwnmPZQlwprAzcb1WGD4wRq32sjjbuBUkRiiy9fyQscizPfK3ox12WqzcwEvFpsICQvUWkxp7vTHyBTYt%2FVAhihM9MC4rgaLRmlA2VftbkJqF8VwYdk8R&X-Amz-Signature=9010075ae8151c0e2362beac5374558fe724bd4c04b02cf6e2bc9bad07db6010&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

然后在上面我们为了方便tracking ，这里可以打一行 log 那打 log 我们就把 sl four G 给它引入进来。好了，在这边打一行 warning 或者是 info 级别的 log info ，叫 user registration request is blocked okay 那如果有的用户打你的客服电话说我被 block 了 100 次，你们怎么还没好？那为了证明他说的是真是假，咱可以把他的这个用户名称给他加入进来。那到这里，咱的这个配置就已经全部完成了。接下来我们把项目给它启动起来，走到 user application 这里。在启动这个用户模块之前，我们要确保 eureka 先启动了，并且你的配置中心也已经启动了。那这时候我们再来启动用户中心。 OK 那稍等半柱香的时间看它这里 log 走到这里，已经开始去从配置中心拉取它的外部属性了。 OK 我们往下看，好到这里很顺利的，这个项目已经启动起来了。那我们为了验证前面的几个配置项都已经生效了，我们先来这样做。首先去看一下这个数据库是不是生效。我们很简单的走到 postman 里，比如说我通过一个 user ID 拿取它的 address 列表。好，点击 sendok 这里已经很快地返回了。那证明数据库的配置已经生效了。


那接下来我们再来看一下咱的 actuator 端点是否都已经暴露出来了。那我们切换到浏览器，然后把咱的用户模块的地址给它打上 local host 10,002 后面跟 activator 端点。好点击回撤。 OK 那同学们看到这里，咱们配置的 actiator 端点已经全部显示出来了，那证明这一段配置也已经生效了。好，接下来最后一个测试是什么？我们要看一下咱的用户注册功能是不是被成功的阻断住了。因为我们在配置属性当中给这个用户注册开关，这里 disabled 给它设置成了 true 也就是处于关闭状态。那我们再把镜头换到 postman 当中，这里也是一个用户注册的请求，我把它发向10,002，它的地址是 register 那我们这里就随便写一个 username 它的值是 1 好了，OK我这里点击发送，点击 send 走。你好，很快返回了注册，返回这么快，肯定不正常。我们看一下这里显示了一个 status 等于500，然后 message 是什么呢？当前注册用户过多，请稍后再试。


OK 那我们三个配置都已经全部生效了。同学们也可以去尝试着把 github 上面的这个用户注册开关，再从关闭状态改成开启状态。改完之后再 push 一条消息，调用 activator 端点的 refresh 把配置文件给它刷新一下，看这个功能是否又会回到正常注册的状态。


OK 同学们，那这一节我们把前面配置的三个属性都成功地集成到了用户微服务模块当中。同学们可以使用相同的方式把剩下的几个微服务模块，订单中心、商品中心、购物车和主搜这些模块通通的改造过来。把这些纷繁复杂的配置项从咱项目中的配置文件放到 github 上面的文件当中，这样咱项目里的配置文件就会从乱糟糟变成了小清新的风格。 OK 同学们，那这一节就到这里结束了，我们在下一章节当中将会去学习配置中心的好搭档 bus 服务。那青山不改，绿水长流。小伙伴们，我们下一章再见。



