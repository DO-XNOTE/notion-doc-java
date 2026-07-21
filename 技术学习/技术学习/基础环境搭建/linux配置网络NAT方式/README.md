---
title: linux配置网络NAT方式
---

# linux配置网络NAT方式

```markdown
https://zhuanlan.zhihu.com/p/389086678
```


**重启网络：**

**Centos8 不能重启网络报错原因 Failed to restart network.service: Unit network.service not found**

```java
[root@bogon ~]# service network restart
Redirecting to /bin/systemctl restart network.service
Failed to restart network.service: Unit network.service not found
```

**原因是由于 centos8 已经替换了原来的network, 新版的叫：NetworkManager****所以用这个命令就可以重启了 systemctl restart NetworkManager**

```java
[root@bogon sysconfig]#  systemctl status  NetworkManager
● NetworkManager.service - Network Manager
Loaded: loaded (/usr/lib/systemd/system/NetworkManager.service; enabled; ven>
Active: active (running) since Tue 2022-01-04 01:14:16 CST; 1min 43s ago
Docs: man:NetworkManager(8)
Main PID: 11495 (NetworkManager)
Tasks: 3 (limit: 8532)
Memory: 5.2M
CGroup: /system.slice/NetworkManager.service
└─11495 /usr/sbin/NetworkManager --no-daemon
```

***相关整理命令***

```java
systemctl restart NetworkManager			重启网络
systemctl status NetworkManager				查看网络状态
service NetworkManager stop 				关闭NetworkManager
chkconfig NetworkManager off 				禁止开机启动
chkconfig NetworkManager on			 		开机启动
service NetworkManager start 				临时启动
chkconfig NetworkManager off 			 	永久关闭托管工具


**Network和NetworkManager区别**
Network：对网卡的配置,network的制御网络接口配置信息改动后，网络服务必须重新新启动，来激活网络新配置的使得配置生效，这部分操作和从新启动系统时时一样的作用。制御（控制）
是/etc/init.d/network这个文件，可以用这个文件后面加上下面的参数来操作网络服务

NetworkManager：是检测网络、自动连接网络的程序。无论是无线还是有线连接，它都可以令您轻松管理。对于无线网络,网络管理器可以自动切换到最可靠的无线网络。利用网络管理器的程序可以自由切换在
线和离线模式。网络管理器可以优先选择有线网络，支持 VPN。网络管理器最初由 Redhat 公司开发，现在由 GNOME 管理
```



