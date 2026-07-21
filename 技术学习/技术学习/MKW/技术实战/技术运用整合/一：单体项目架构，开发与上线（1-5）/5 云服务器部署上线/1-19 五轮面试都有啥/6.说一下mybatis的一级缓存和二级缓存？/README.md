---
title: 6.说一下mybatis的一级缓存和二级缓存？
---

# 6.说一下mybatis的一级缓存和二级缓存？

对mybatis的缓存机制的理解如下:

1. 一级缓存是SqlSession级别的缓存,在同一个SqlSession内多次执行相同的SQL语句时,第一次执行完毕会将数据库查询结果缓存到SqlSession中,第二次将直接从缓存中获取结果,不需要再次发送SQL到数据库。一级缓存默认开启,通过localCacheScope参数可以控制一级缓存的范围。
1. 二级缓存是mapper级别的缓存,多个SqlSession可以共享二级缓存,二级缓存默认不开启,需要在配置文件中配置
<setting name="cacheEnabled" value="true"/>来开启。二级缓存的作用域由cache-ref属性指定,所有引用了这个cache-ref的mapper都共享这一个缓存。

1. 当进行增删改操作时,会清空SqlSession的一级缓存和当前mapper的二级缓存,以保证缓存数据的一致性。
1. 查询顺序是先查询二级缓存,如果二级缓存没有命中再查询一级缓存,如果一级缓存也没有命中则查询数据库。
1. Mybatis提供FIFO、LRU等缓存替换策略来优化缓存的性能。
所以综上,Mybatis的一级二级缓存可以减少数据库查询次数,提高查询效率。但也需要注意缓存一致性问题,在写操作后可能需要清空缓存。

