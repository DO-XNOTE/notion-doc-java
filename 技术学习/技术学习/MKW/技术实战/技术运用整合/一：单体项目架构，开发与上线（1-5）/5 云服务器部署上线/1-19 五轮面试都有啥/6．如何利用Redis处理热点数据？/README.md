---
title: 6．如何利用Redis处理热点数据？
---

# 6．如何利用Redis处理热点数据？

[这里有几种方法可以利用Redis来处理热点数据:](/b1287a18fb8c489f80408d87be9507e5)

一：热点数据进行隔离

[image](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/cd3de16f-f527-4a01-b848-b521a3d1b57c/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466W5DM6NNA%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T224819Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIAUzwAx9cgddeUnHHYQRvUnsInm91V5bIg%2BGzimdn76HAiB9DcabirgVbNaUpIZWDToZw4xCTLxvKQmirUHeUjYN5CqIBAjG%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMmZGH1G8FYJE0WnGjKtwDblkZjG2j9OXUZI2Dg8h4E621v%2BMMh0KDCJgDj%2FjgwxMFZV2fZcXmsLnSlbEVLN944BqVdVl%2BiozUCdQmxIOVHUb5U2RlpP4LvcH8IgSrVMZLIi%2BBCRWgMjvln9ei%2BTu60po6aLVal%2B5f7Oz1ZAB9Rzy0o9Xm9a02wviW%2FVFJrijVSHMQVjTtTyDTQ1%2BA2g5oUiPTkrPRxgNip7Q8i0DNTwoMP7a%2Fg7Wi02eBcz5jw3gZj2ZZJSTlMhJ%2BxgJ8oH52nYycrI88SUw%2BCouyeup1cxrByifQqou3ZYJobrpa8TPetBolrvItnkzxNxGedhoG2xL18nmLIYAkC36uofwjmLnI6PjwZhYSHECd%2BE%2BFTaLVGpo5u%2BtIGOY9jFtQmiu2e5EmAHHD0IepGJW7xHSwHctDLQFHdpesxzqy2%2FfbfD4GCK5X%2BNgKRoIykJruDpxaTt3dSbOkH9qPyBhl6%2F5%2FiFYERH0gWm22MlSRGYUYs9KfG%2BZKp044j3LFzmejidAks0HjpEK0IsYsJzudh0NHsxYYk5QTas%2BicuEbXR3SF0x%2FYMzmd4MzrGtohpJseAQONLSilNofwvuD4G%2F%2FEWtjXKNKATL%2BzGWbO%2BJNIoh6%2BWnsEA%2Fj7dHCCFDpPoMwrbr%2F0gY6pgH409RY%2FYhaoR1UetTRGtbvRrkg0nuS4RcjUPq35mcdKIaan79lgrA9Ln57yFr8GhsgA8PHC%2BlPsNoYDOe8AJKjeIzaKgr0NJhuC2dLTRjPdD%2B08q9qhXzimXADa3FoQ6OrNcjuWR8t1pSzYtyP98BDgA01OHDc3hpbQNYnimv%2B9AUV6q%2F8rB55b656YxYmq4bQYjf%2FJRdABK%2BjuLeQydvE6G5DvMkn&X-Amz-Signature=e59ac23a27d80c2978cfb8b55804ec7284af1ce8a190f429cb4d72e128774ef6&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)


[热点散列(Hot Spot Hash)是一种利用散列(Hash)来处理热点数据的技术](/9349fca26b0b4ed6be16277ba15f1c5a)。

主要思路是:

1. 使用多个散列函数(Hash Function)将热点数据映射到不同的存储位置。
1. 读取热点数据时,同时从这些存储位置读取,然后合并。
1. 写入热点数据时,使用多个散列函数将数据映射到不同位置写入。
这样通过散列的手段,可以将对热点数据的读写压力分散到多个存储位置中,避免热点对某一存储位置的过度访问,起到负载均衡的效果。

热点散列常用在缓存系统中,典型的应用就是 Redis 集群使用 CRC16 对 key 进行散列,将热点数据分散在不同的节点中,避免单机压力过大。

相比传统的用 Hash 模拟多个字典的方式,热点散列更加灵活,可以针对热点数据做散列,保证系统的扩展性。除了 Redis 集群,一些 NoSQL 系统也使用了类似热点散列的机制。



1. 使用 Redis 的 HyperLogLog 数据结构对热点数据进行统计和概要存储。HyperLogLog 可以在不存储完整数据的情况下,快速统计出热点数据的基本信息,比如 UV 等。这可以节省存储空间。
1. 将热点数据的访问次数作为 Value,键名作为该数据的 ID,存储到 Redis Sorted Set 中,并根据访问次数做排序。这可以快速找出最热的数据。
1. 使用 Redis 的 Bitmaps, 每个位表示一个数据 ID,通过设置或获取位来记录 ID 是否是热点。Bitmaps 占用空间小,易于统计热点数据总数。
1. 利用 Redis 的发布订阅机制,针对热点数据设置一个频道,数据产生时发布到该频道,应用程序可以订阅该频道获取热点数据。
1. 将热点数据的访问统计结果(比如访问量、次数等数据)存储到 Redis 中,应用从 Redis 获取统计结果,而不是直接统计和计算。可以减小应用压力。

