---
title: 1．请详细说明HashMap和HashTable以及CocurrentHashMap的异同？
---

# 1．请详细说明HashMap和HashTable以及CocurrentHashMap的异同？

详细说明HashMap、HashTable和ConcurrentHashMap的异同:

HashMap和HashTable都是基于哈希表的Map接口的实现,主要区别有:

1. HashMap是非线程安全的,HashTable是线程安全的,因为HashTable的主要操作都是synchronized。
1. HashMap允许null作为键和值,而HashTable不允许。
1. HashMap的键值对允许重复,而HashTable的键值对不允许重复。
1. HashMap默认初始容量是16,加载因子是0.75;HashTable默认初始容量是11,加载因子是0.75。
1. HashMap扩容时是容量*2,而HashTable扩容时是容量*2 + 1。
1. HashMap迭代时是fail-fast,而Hashtable迭代时不是fail-fast。
ConcurrentHashMap是线程安全的HashMap,主要分为以下几点:

1. ConcurrentHashMap采用分段锁,每个段是一个类似HashMap的结构,所以其本质也是一个Segment数组。
1. ConcurrentHashMap允许并发读取,理论上不加锁(1.7后加了个volatile)。
1. ConcurrentHashMap的写操作需要加锁,但仅针对该段加锁而不是全表锁。
1. ConcurrentHashMap不允许null作为键和值。
1. ConcurrentHashMap迭代时是fail-safe。
总结来说,HashMap非线程安全;HashTable线程安全但效率低下;ConcurrentHashMap融合了二者的优点,是高效的线程安全Map。


