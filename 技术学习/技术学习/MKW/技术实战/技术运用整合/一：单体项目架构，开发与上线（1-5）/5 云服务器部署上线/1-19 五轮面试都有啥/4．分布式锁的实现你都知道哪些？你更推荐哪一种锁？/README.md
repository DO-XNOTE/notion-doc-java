---
title: 4．分布式锁的实现你都知道哪些？你更推荐哪一种锁？
---

# 4．分布式锁的实现你都知道哪些？你更推荐哪一种锁？

对分布式锁的几种常见实现方法我有一些了解:

1. 基于数据库的分布式锁
利用数据库的原子性,可以实现获取和释放锁的操作。比如在MySQL中,可以通过获取一条记录的悲观锁实现。这种方式实现简单,但存在单点问题,数据库故障会导致无法获取锁。
1. 基于Redis的分布式锁
利用Redis的setnx命令,可以实现一个非阻塞的分布式锁。获取锁时SET key value NX EX time,释放锁时DEL key。这种方式可实现自动过期释放锁,避免死锁。但需要考虑锁失效的问题。
1. 基于Zookeeper的分布式锁
Zookeeper提供了一致性的文件系统,可以实现获得锁、释放锁、过期释放锁等操作。但需要单独安装和维护Zookeeper。
1. 基于Etcd的分布式锁
原理与Zookeeper类似,都是利用文件系统的特性实现锁。Etcd相比Zookeeper更轻量级一些。
1. 基于Consul的分布式锁
Consul也提供KV存储,可以基于Consul实现分布式锁,与Zookeeper和Etcd原理类似。
综合来说,我个人更倾向于基于Redis或Etcd实现的分布式锁。相比Zookeeper,Redis和Etcd更轻量级,基于key-value的锁实现也比较简单。同时Redis和Etcd都可以提供过期释放锁的机制,较为安全可靠。

代码

好的,我用Java来给一个使用Redis实现分布式锁的代码示例:

```java
import redis.clients.jedis.Jedis;

public class RedisLock {

  private Jedis jedis;
  private String lockKey;

  public RedisLock(Jedis jedis, String lockKey) {
    this.jedis = jedis;
    this.lockKey = lockKey;
  }

  public boolean acquire() {
    String indentifier = UUID.randomUUID().toString();
    // 设置锁的过期时间,防止死锁
    Long expireTime = System.currentTimeMillis() + 30000;

    // 如果key不存在,返回1,获得锁
    Long result = jedis.setnx(lockKey, indentifier);
    if (result == 1) {
      // 设置过期时间
      jedis.expireAt(lockKey, expireTime);
      return true;
    }

    // 否则重复取锁逻辑
    return false;
  }

  public void release() {
    // 只有锁对应的value值相等才删除锁
    if (jedis.get(lockKey).equals(indentifier)) {
      jedis.del(lockKey);
    }
  }

}

```

主要逻辑是:

1. 生成一个随机标识符
1. 使用SETNX尝试获取锁
1. 设置锁的过期时间,防止死锁
1. 释放锁时判断value值是否相等后再删除
这样可以实现一个非阻塞的分布式锁。



ETCD分布式锁：

Etcd是一个开源的、高可用的分布式键值(key-value)数据库,可以用于共享配置和服务发现。

Etcd实现分布式锁的思路是:

1. 在Etcd上创建一个锁资源的键,值为锁的持有者
1. 通过CAS(Compare And Swap)操作实现对锁资源键的原子获取和释放
一个Java实现Etcd分布式锁的示例代码如下:

```java
import io.etcd.jetcd.Client;
import io.etcd.jetcd.options.PutOption;

public class EtcdLock {

  private Client client;
  private String lockKey = "/lock";

  public EtcdLock(Client client) {
    this.client = client;
  }

  public boolean tryLock(long leaseId) {
    try {
      client.put(lockKey, "locked", PutOption.newBuilder().withLeaseId(leaseId).build()).get();
      return true;
    } catch (Exception ex) {
      return false;
    }
  }

  public void releaseLock(long leaseId) {
    client.delete(lockKey);
    client.revokeLease(leaseId);
  }

}

```

这里主要是:

1. 创建一个路径作为锁资源
1. 尝试以CAS方式写入一个值表示加锁,同时绑定租约
1. 释放锁时删除键并销毁租约
Etcd实现的分布式锁相比Redis更轻量而且可以避免锁不释放的问题。



Consul 实现分布式锁

Consul是一个服务发现和配置工具,与Etcd类似,也可以用来实现分布式锁。

使用Java与Consul实现分布式锁的方式如下:

1. 获取Consul的客户端实例
```java
Consul client = Consul.builder().build(); //构建client实例

```

1. 定义一个锁的key
```java
String lockKey = "my_distributed_lock";

```

1. 使用client的kv操作获取锁
```java
boolean isLocked = client.kvClient().acquireLock(lockKey);

```

1. 获取到锁后执行业务逻辑
1. 释放锁
```java
client.kvClient().releaseLock(lockKey);

```

acquireLock()和releaseLock()使用Consul的sessionId实现锁,相当于一个CAS操作,可以避免不同节点之间的锁冲突。

所以整体实现是一个原子的获取锁->执行业务->释放锁的流程。

相比Etcd,Consul提供了更高级的分布式锁操作,使用更加简单方便。同时Consul也有服务发现、配置管理等功能,可以很好地与微服务结合使用。

