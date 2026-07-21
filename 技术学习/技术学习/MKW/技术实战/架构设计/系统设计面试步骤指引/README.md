---
title: 系统设计面试步骤指引
---

# 系统设计面试步骤指引

[file](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/5de07ea6-ff6c-4ef2-9364-ff01f9250938/%E7%B3%BB%E7%BB%9F%E8%AE%BE%E8%AE%A1%E9%9D%A2%E8%AF%95%E6%AD%A5%E9%AA%A4%E6%8C%87%E5%BC%95.md?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666DWO5YUW%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T230253Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCooTsf0aUHdw3oiJ9L8u6h5ViVT5D6IbqBCK6kv352VwIgDVXd2f%2Bo6dqo%2FYBo5K4erfpufFySYg5wQK73yOa%2BY%2F8qiAQIxv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDCspsmF57HeaN%2BYqKSrcAy3sRFq%2Bl%2F4G9FK%2Br2cSizZvZrk%2BSv6rucMgjAGXnqldep2SLu1Vk4d2aNbKO6aPDL0y9KVBJzGU%2Bfxzw93wFe3QNr1Vzk7BLBaH1f2PLll9arwYzaMwFVkJL%2F86Wij07W21qrZhdprBTwOJjuA5GJtoI02rG3LDvSxjUyIlgVoYEmqwmv7ZOgYMS2tVqLM0oi18IeOsQnOh8Zjb%2B4a50oJRJDU9DGg1f0TpbnHrNNqTb%2BKwqsvflE%2F7psOCulERewAhqHct8wvd45IvgzDEAwhaff0NnlM%2BTawXBN4EvBKS3COZeS%2FVeR95ZWQ8FgWFH25cARQWRMfLk0nc40VQVI%2Bnb6pe4pPsYMO6PNfV0eOheYDcbqTnOzUauYDQmjzsTrNqhtXOeDgWBYmtY0SKrdu84p6Wodov6nvx6LfPuvNMdvj1tJUZlEk5sU2qUFFyOfrStYzMFzTdTaJNpC%2Fb8F%2Bb5oTZYBAp3eUlhevRTdCRuoiBGBM5k%2BY1X2v32DtEgSzigRU8Orh9tK%2B69AjjiswiATxCKMKV7I%2Fqdb4F0Wy31wWv%2FZSYPUP973%2B3DlPAc6v8uS6STr%2BQvo%2Fxm2K%2B%2FVrxwiEvSOoD%2BRsTsWqr7vzmjOyM5eULOizhNJNuMMG3%2F9IGOqUBWacmn4CE%2FCgNmb%2FQqAfGuKFBEHNVm%2BEup1lCspuwuj3WcztprC7nRe6hhztwJiX25BfG1T5%2FGph7A1FghF%2FcNZTTo4vNHhpqnyCtkL%2FQLy%2FbNHhCz0HTPBAGE46E%2FKx%2BmJbcF4GWrTNRhudHbz%2FPpMln7qut%2BsEkBa9ljD%2FcXDcP0LAM6rz00ysRsy3XhYgCOYOEJmPZB7FCANb%2BFv3RjFqM5QgV&X-Amz-Signature=995f441a9b73d1a5a8611c1772ea941cbd67981dea77a02fcd2f3a65b6c1e74a&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

[file](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/dc5b7236-ef8f-4681-b6a7-b9b724f5feac/README.md?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666DWO5YUW%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T230253Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCooTsf0aUHdw3oiJ9L8u6h5ViVT5D6IbqBCK6kv352VwIgDVXd2f%2Bo6dqo%2FYBo5K4erfpufFySYg5wQK73yOa%2BY%2F8qiAQIxv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDCspsmF57HeaN%2BYqKSrcAy3sRFq%2Bl%2F4G9FK%2Br2cSizZvZrk%2BSv6rucMgjAGXnqldep2SLu1Vk4d2aNbKO6aPDL0y9KVBJzGU%2Bfxzw93wFe3QNr1Vzk7BLBaH1f2PLll9arwYzaMwFVkJL%2F86Wij07W21qrZhdprBTwOJjuA5GJtoI02rG3LDvSxjUyIlgVoYEmqwmv7ZOgYMS2tVqLM0oi18IeOsQnOh8Zjb%2B4a50oJRJDU9DGg1f0TpbnHrNNqTb%2BKwqsvflE%2F7psOCulERewAhqHct8wvd45IvgzDEAwhaff0NnlM%2BTawXBN4EvBKS3COZeS%2FVeR95ZWQ8FgWFH25cARQWRMfLk0nc40VQVI%2Bnb6pe4pPsYMO6PNfV0eOheYDcbqTnOzUauYDQmjzsTrNqhtXOeDgWBYmtY0SKrdu84p6Wodov6nvx6LfPuvNMdvj1tJUZlEk5sU2qUFFyOfrStYzMFzTdTaJNpC%2Fb8F%2Bb5oTZYBAp3eUlhevRTdCRuoiBGBM5k%2BY1X2v32DtEgSzigRU8Orh9tK%2B69AjjiswiATxCKMKV7I%2Fqdb4F0Wy31wWv%2FZSYPUP973%2B3DlPAc6v8uS6STr%2BQvo%2Fxm2K%2B%2FVrxwiEvSOoD%2BRsTsWqr7vzmjOyM5eULOizhNJNuMMG3%2F9IGOqUBWacmn4CE%2FCgNmb%2FQqAfGuKFBEHNVm%2BEup1lCspuwuj3WcztprC7nRe6hhztwJiX25BfG1T5%2FGph7A1FghF%2FcNZTTo4vNHhpqnyCtkL%2FQLy%2FbNHhCz0HTPBAGE46E%2FKx%2BmJbcF4GWrTNRhudHbz%2FPpMln7qut%2BsEkBa9ljD%2FcXDcP0LAM6rz00ysRsy3XhYgCOYOEJmPZB7FCANb%2BFv3RjFqM5QgV&X-Amz-Signature=9fed3fd1ddcd92cb327dd4168f80e4ab3f1882c8361d427a807b5ff5cee829cc&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

很多软件工程师受困于系统设计面试，主要有以下几点原因：

- 开放式的题目，没有固定的套路，没有固定的答案
- 缺乏大规模复杂系统的开发经验
- 缺乏充足的准备
那么，接下来逐步介绍如何解决系统面试中的复杂系统设计问题。

[image](https://cdn.nlark.com/yuque/0/2022/png/640636/1646535721304-a433f227-a50d-4098-bb5b-02323f1695b8.png)

# 理清需求

首先我们必须理清需要解决的问题的详细需求。系统设计问题由于是开放式的，没有唯一确定的答案，如果我们对问题需求理解存在偏差，那么整个面试就很难获得成功。而且面试时间通常只有35-40分钟，因此我们需要把精力集中在重点模块上。

下面让我们看一个实际的例子，假设我们要设计一个类似Twitter的系统，那么首先我们需要弄清楚如下几个问题：

- 是否需要支持用户发推特以及关注其他人
- 是否需要展示用户的活动时间线
- 推特内容是否需要包含照片和视频
- 除了后端，前端是否也需要考虑
- 是否支持用户搜索推特内容
- 是否需要展示热点趋势话题
- 新推特是否需要支持通知
# 接口定义

这一步需要定义出系统中的核心接口。定义出接口能够准确体现系统不同模块的交互，还能review看看我们理解是否和问题需求有偏差。

比如推特系统的相关API定义：

//发推
postTweet(user_id, tweet_data, tweet_location, user_location, timestamp, ...)

//生成用户活动时间线
generateTimeline(user_id, current_time, user_location, ...)

//标记
markTweetFavorite(user_id, tweet_id, timestamp, ...)

# 系统量级规模估计

估计出系统需要支持的量级，在后续进行伸缩性、分片、负载均衡和缓存设计的时候会用到：

- 系统需要支持的业务流量量级（发新推的量级、推特的查看量级等）
- 存储空间大小（是否需要支持照片和视频对存储空间大小评估影响很大）
- 网络带宽
# 定义数据模型

即领域模型定义。通过定义数据模型，明确数据在系统不同模块之间的流向变得清晰，也在后续的数据分片和管理上起到指导作用。我们需要确定出系统中的不同实体、相互之间怎么交互、以及和存储、传输、加密等数据管理设施之间的关系。

比如类Twitter系统可以如下定义数据模型：

- User（UserId、Name、Email、DoB、CreationData、LastLogin）
- Tweet（TweetId、Content、TweetLocation、NumberOfLikes、Timestamp）
- UserFollower（UserId1、UserId2）
- FavoriteTweets（Userid、TweetId1、TimeStamp）
# 概要设计（High-level design）

通过图示画出系统中的核心模块。

类Twitter系统的概要设计图如下。如果流量较大，可能需要考虑采用多台服务器，还需要负载均衡设备。另外还可以考虑读写分离。

[image](https://cdn.nlark.com/yuque/0/2022/png/640636/1646099387503-345aa366-4ee8-41fe-82aa-6b6a5a7b347a.png)

# 详细设计（Detailed design）

对核心模块进行深挖，进行深入讨论。可能会有多种方案，我们需要对多种方案的优缺点进行权衡。

- 数据量级越来越大，如何进行数据的存储？如何将数据分片存储到多台服务器上？
- 大V热点问题如何解决？
- 用户时间线数据查询优化（scan）
- 缓存的使用
# 系统瓶颈分析

讨论系统中可能的瓶颈，并讨论解决方案。

- 是否存在单点问题，单点异常或失败了如何处理
- 是否有足够的数据副本在部分服务器宕机的时候仍然能提供服务
- 服务的性能监控、告警、降级
---

---

---

---

---

---

---

# 大厂系统设计面试真题

## **系统设计面试步骤指引**

[大厂系统设计面试步骤指引](https://github.com/xiajunhust/system-design-interview/blob/main/%E5%A4%A7%E5%8E%82%E7%B3%BB%E7%BB%9F%E8%AE%BE%E8%AE%A1%E9%9D%A2%E8%AF%95%E7%9C%9F%E9%A2%98/%E7%B3%BB%E7%BB%9F%E8%AE%BE%E8%AE%A1%E9%9D%A2%E8%AF%95%E6%AD%A5%E9%AA%A4%E6%8C%87%E5%BC%95.md)

***## *****分布式ID的生成**

常见如交易号等都需要生成分布式唯一ID。  
思路：

- 利用mysql的自增机制。
- 利用开源项目Twitter Snowflake，需要了解下其核心算法实现。
## **类似新浪微博短链接系统设计**

思路：采用发号策略，对应每一个长链接，生成一个唯一的号码，拼接成短连接。  
需要考虑的问题：

- 发号器的设计。小系统可以直接用数据库MySQL的自增。考虑高并发的话可以用如redis做发号器。
- 发号器的高可用。
- 短链接的存储。
## **Instagram的数据存储**

思路：数据分片，主要是分片ID的设计。

## **K-V存储引擎**

思路：可以参考开源的Rocksdb和LevelDB。

## **网络爬虫**

---

致力于分享干货，为每一位计算机CS学子学习道路上带来帮助。

也欢迎大家关注我的公众号「编程学习指南」，***获取更多计算机干货~提供大厂（阿里、字节、美团、快手、网易等）内推、简历修改、面试咨询、毕设咨询等服务***。


