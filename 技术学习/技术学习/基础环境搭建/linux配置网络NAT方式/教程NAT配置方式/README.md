---
title: 教程NAT配置方式
---

# 教程NAT配置方式


```markdown

##教程NAT配置方式
Mac环境下 VMware Fusion下的虚拟机 NAT网络配置
VMware Fusion 安装完成后，会在Mac OS中新建两个网卡： 
vmnet1以及vmnet8（在 /Library/Preferences/VMware Fusion 下可以看到），
其中 vmnet1 是Host-only模式， vmnet8是NAT模式。此处仅对网卡vmnet8 进行修改
1 ,修改 /Library/Preferences/VMware\ Fusion/networking
sudo vi /Library/Preferences/VMware\ Fusion/networking
```

[image](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/9fa61fb4-4468-49a2-8e4f-bc9c35c8dcce/v2-04ad9ee18543acadf59e721c8e937aec_720w.jpg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46675HGFQWW%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T234406Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDd5HL1OcvgrhpSFOjkbkXDiiGZzDAUdrSXuLgw0i2GswIhALN5DT3lWeVrr8PZFB9QFqSBqEZVUUH0OM3ni4%2F02ZGvKogECMb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgwjVMCAyM4aDlyiDtkq3AMf7mkxnCMOEUQQ8g0kZfDZLE7D6ryQ0H%2F9vJfipSWgOagWHLfZ4i%2BLhzov2g7fqaN49fSudK18ABlrur5nBTGsyNxc5BzzzgP2SJaWMWuWmuU7PmSjBzFD1K7TQP97XSTChhObnFHiG0hgvHHRVe8uT3MFMy9J%2BReluoMc13zoqyEgNMXYuD2uXB%2Fe3eCzIGYtkZpK9uN9PlVtMtZLt%2BDdfmvm4YH7bpFXJihxeBeK3LP2y6hDy66HUsHV6hJqKfcffeI%2BLt%2BoQpmxv980LYlTDz3pGo9jfmaEy7iaI0BckjLx4qtv5%2BQIPIWYG979S9oEkMVBXFW%2BStcLMicuwAHdM0id4gKOXuzv7Si%2F3IGbbr%2F7QiRXQklPly9Ooi7%2BxwhKoEhLsk1NVPxFgQi7rPinT2Mv%2BA8xi%2FiQZ8bV70JRs7fdsGDF%2FcEIAo9c0e8riAXDk6dw6kBs%2F7Qo%2Fg%2FEdBo%2BmP66r8pv0jiVE%2BnMmL%2B3z5PS7bxj%2BtYjZ2BWcly8GqAkcMQeN5Snj6j3RnkQAfpFNuCky70rtmhaIyt0LK8LuUfbXiitRQHm2RPfdRKByR%2BCMolPVDZDAjXE0w%2FOQbwC6SuiDKHXo%2FHNS%2BrgdLt32p92EuSrtgsjGIJH6DC0uP%2FSBjqkAeLS2jNoAmVm2%2FAk1Il1B879pWttmXpMkoKl7OQ1a%2BBsdkTbKlXan69bSltaaz4fMNUy%2FyVp8caFFgtPIYHeFl%2ByvwxJTZtUWHR0HHfPrwwVK7x%2FF1f8lfgA8UsuGqaLlPpzE7cIDTUf7fT8%2FTHe9lkRuViv9D0VKHrYn0uAgAH7jngraJYF7IMeDmfKEnjW%2FDo%2FdNQcjZfz5QZJ%2B0hYA0Qmv06d&X-Amz-Signature=f2b35fbd2e73ac5b49e343b1e5d8b9f31e93d6a55ee0caaf7512b5d7bb8710e5&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

```java
将 DHCP 设置为 no， 即使用静态IP。 将 SUBNET 修改为自己想用的网段，
此处我填的是 192.168.111.0 网段。 **注意**：只修改 vmnet8 的配置， 
不要修改vmnet1的配置

**2** 修改 /Library/Preferences/VMware\ Fusion/vmnet8/nat.conf
sudo vi /Library/Preferences/VMware\ Fusion/vmnet8/nat.conf
```

[image](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/d617edf9-226c-4ed5-9033-b37c7794f6b3/v2-01aa707c19ebfa895c1b1c9e53814545_720w.jpg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46675HGFQWW%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T234406Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDd5HL1OcvgrhpSFOjkbkXDiiGZzDAUdrSXuLgw0i2GswIhALN5DT3lWeVrr8PZFB9QFqSBqEZVUUH0OM3ni4%2F02ZGvKogECMb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgwjVMCAyM4aDlyiDtkq3AMf7mkxnCMOEUQQ8g0kZfDZLE7D6ryQ0H%2F9vJfipSWgOagWHLfZ4i%2BLhzov2g7fqaN49fSudK18ABlrur5nBTGsyNxc5BzzzgP2SJaWMWuWmuU7PmSjBzFD1K7TQP97XSTChhObnFHiG0hgvHHRVe8uT3MFMy9J%2BReluoMc13zoqyEgNMXYuD2uXB%2Fe3eCzIGYtkZpK9uN9PlVtMtZLt%2BDdfmvm4YH7bpFXJihxeBeK3LP2y6hDy66HUsHV6hJqKfcffeI%2BLt%2BoQpmxv980LYlTDz3pGo9jfmaEy7iaI0BckjLx4qtv5%2BQIPIWYG979S9oEkMVBXFW%2BStcLMicuwAHdM0id4gKOXuzv7Si%2F3IGbbr%2F7QiRXQklPly9Ooi7%2BxwhKoEhLsk1NVPxFgQi7rPinT2Mv%2BA8xi%2FiQZ8bV70JRs7fdsGDF%2FcEIAo9c0e8riAXDk6dw6kBs%2F7Qo%2Fg%2FEdBo%2BmP66r8pv0jiVE%2BnMmL%2B3z5PS7bxj%2BtYjZ2BWcly8GqAkcMQeN5Snj6j3RnkQAfpFNuCky70rtmhaIyt0LK8LuUfbXiitRQHm2RPfdRKByR%2BCMolPVDZDAjXE0w%2FOQbwC6SuiDKHXo%2FHNS%2BrgdLt32p92EuSrtgsjGIJH6DC0uP%2FSBjqkAeLS2jNoAmVm2%2FAk1Il1B879pWttmXpMkoKl7OQ1a%2BBsdkTbKlXan69bSltaaz4fMNUy%2FyVp8caFFgtPIYHeFl%2ByvwxJTZtUWHR0HHfPrwwVK7x%2FF1f8lfgA8UsuGqaLlPpzE7cIDTUf7fT8%2FTHe9lkRuViv9D0VKHrYn0uAgAH7jngraJYF7IMeDmfKEnjW%2FDo%2FdNQcjZfz5QZJ%2B0hYA0Qmv06d&X-Amz-Signature=845c21de4a9e7ef17454fddf841028f40e05b9e1ad66cb49d917939a2eac3f7a&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

```java
设置网关为 192.168.111.2 ， 网关的IP要和上一步中的IP 保持网关一致。

3 配置虚拟机 将虚拟机网络设置为NAT模式,进入虚拟机
su root
vi /etc/sysconfig/network-scripts/ifcfg-eth0
```

配置信息如下:

```java
DEVICE=eth0
TYPE=Ethernet
ONBOOT=yes
NM_CONTROLLED=yes
BOOTPROTO=static
IPADDR=192.168.111.101
GATEWAY=192.168.111.2
NETMASK=255.255.255.0
DNS1=192.168.1.1

--- 配置内容解析
IPADDR=192.168.111.100      //自定义的虚拟机IP， 需与VMware Fusion配置的IP在同一个网段上
GATEWAY=192.168.111.2       //网关。1.2中配置的网关地址
NETMASK=255.255.255.0       //掩码。1.2中配置的掩码
DNS1=192.168.1.1           //Mac本机的DNS地址。 系统偏好设置-> 网络 -> 在左侧选择当前使用的网络，点击右下角的“高级”按钮 -> 切换Tab页，可找到DNS地址。
```

然后重新网络服务

```java
systemctl restart NetworkManager
```


