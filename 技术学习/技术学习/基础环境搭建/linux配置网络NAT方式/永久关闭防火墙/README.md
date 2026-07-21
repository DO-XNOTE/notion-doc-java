---
title: 永久关闭防火墙
---

# 永久关闭防火墙

CentOS-8下的关闭/禁用防火墙

查看状态

```java
systemctl status firewalld.service
```

打开防火墙

```java
systemctl start firewalld.service
```

关闭防火墙

```java
systemctl stop firewalld.service
```

开启防火墙

```java
systemctl enable firewalld.service
```

**禁用防火墙（要永久禁用，先执行关闭stop命令才可以）**

```java
systemctl disable firewalld.service
```


