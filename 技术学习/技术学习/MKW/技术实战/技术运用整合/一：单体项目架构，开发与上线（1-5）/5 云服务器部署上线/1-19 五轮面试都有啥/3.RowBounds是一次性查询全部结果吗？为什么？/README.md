---
title: 3.RowBounds是一次性查询全部结果吗？为什么？
---

# 3.RowBounds是一次性查询全部结果吗？为什么？

对RowBounds的理解是不完全正确的。RowBounds不是一次性查询全部结果,而是用于分页查询的。

RowBounds允许按照OFFSET和LIMIT进行分页,它包含两个属性:

- offset - 跳过数量,默认值0
- limit - 查询数量,默认值Integer.MAX_VALUE
使用RowBounds进行分页查询时,并不是一次性查询全部结果,而是根据offset和limit指定的数量,每次查询一页的结果。

举例:

```java
int offset = 10; // 跳过10条
int limit = 20; // 查询20条
RowBounds rowBounds = new RowBounds(offset, limit);

List<User> users = userMapper.selectByRowBounds(null, rowBounds);

```

上面代码会跳过前10条,然后取出接下来的20条记录。可以看到并不是一次性查询全部User结果,而是根据分页参数查询一页一页的结果。

所以综上,使用RowBounds进行分页查询时,并不会一次性把全部结果查询出来,这可以减少内存的占用,适合大量数据的场景。需要注意的是其实底层还是查询全部结果,只是在返回结果集时进行了分页。


