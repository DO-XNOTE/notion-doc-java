---
title: linux 安装 mysql 教程
---

# linux 安装 mysql 教程

## 1. Mac 安装 brew 安装

## 2.Docker安装MySQL

1、下载镜像，注意这里要下载适配了arm架构的镜像源

```markdown
docker pull mysql/mysql-server
```

2、创建容器

```markdown
docker run --name mysql-local -p 3306:3306 -e MYSQL_ROOT_PASSWORD=123456 -d mysql/mysql-server
```

3、进入到docker容器中修改连接权限，否则只能本地连接

```markdown
docker exec -it mysql-local bash
# 进入mysql命令行
mysql -uroot -p123456
# 授权
use mysql;
update user set host = "%" where user='root';
# 刷新权限
flush privileges;
```

4、连接测试（这里使用的是navicat数据库管理工具）

# **3. linux虚拟机安装mysql**

1、下载mysql压缩包[清华mysql镜像下载地址](https://mirrors.tuna.tsinghua.edu.cn/mysql/downloads/MySQL-8.0/)

选择arm版本下载，选择`mysql-8.0.28-1.el7.aarch64.rpm-bundle.tar`

[image](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/279484ee-0ef1-46a0-9ae9-f66d338ee7b1/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466U4BP5GLP%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T234359Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDgm0Bzv9ymEOQIsL2BQtHlKXbKrjFfGmEeh6Xy9P1c%2BgIhAM7S4FRKhuRytU71s3k01ARh5ojnt5U4SawPDcRO2bBwKogECMb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgyVL92%2B6E4ElUxFUXMq3AOKo%2BDoMraNHnua4E8m6qpXneC9QBTLj8L12OCeU1o%2BFVdE5oBm4kCOHm8kVXmRXeIqZPFkEYdxMEib%2Fi16ksoBM8LADKH2nlYPfKyu1NvHeR6njsYMEIuQZp57hJ2txLuZyL89hl2bfr6aHs7hObXaDoFjQSMpWXlItmKTi7kjWzAMMLPPzdwaiZ1w4kcD2ipb8tVwxFdxzVW6eAfYOmo%2FJDxe87CwFmFW%2BDVMQvMEqJxpREgOexaYRZCO4EvOTJtNMrkX74hptVrk0gl6IQIoS98NtmZXLBAu3aID6teOZCF5v1%2FMZl4iykPWrLFK8YBnw0L5VZdFzD3Szst3LYjKO2fsG9f4EX6WoKaKbou9YGbb5Wl4G3k84FzqY3S%2Bfc9m%2FRCYqnlp3xBcrfptQGDRNYt4WQuU7gYwjXBn%2FaUk73CDHCvhjYRq4VIZXwi407hR7Uy3%2BSQH4aSv9pUV8llDRu3lpWNjs5LvPwpOBmnnGQOrWrqp8BYKy0s7WcdsxwHSzstU96CdXxltN6X9frt2g8V%2BEtBESiMnYT9GowbjWdP0Mgm8tun0MTERgGdyVTg5yFjRpNYHNT5KjBK3OVsQnPQBnjzIJgzbDCWzSpsbzI0JrG04KFyPVI90%2FzD8uf%2FSBjqkAWldmX%2FSOjiYkKWpGz8KJI8eQHajTd3251yiGyBNo2RYHZbFf04vJ4AtKR99UZeppdjnphJ8A1L3culERLRjcPNySbZgCXkS5CoqbddH3zE7t2YUuDtO9zu%2FRscyLb7l%2FIahdjL5USw5uk5NhrhYW0M2cFZP6wH%2BLd%2B5bYu8wk5Uxh6aBrsFqvXwU2X0qnexDCKGIdfeEhGrxZnJ5cOYaINZTpvb&X-Amz-Signature=b427e504633b28b8f9a2fa60e935a54ad5bfe42024e01721935f2f1ec6e210f7&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

2、将压缩包上传到linux虚拟机中

```markdown
# 解压 mysql-8.0.28-1.el7.aarch64.rpm-bundle.tar
tar -xvf mysql-8.0.28-1.el7.aarch64.rpm-bundle.tar

#.gz压缩包(不带tar)，用gzip命令即可(-d选项可以解压)
格式：
gzip XXX.gz -d 解压位置

# 注意：如果不指定解压位置，将解压到当前工作文件夹里。

#.tar.gz压缩包，需要使用tar命令的-z和-f选项(解压需要-x)
格式：

tar -zxf XXX.tar.gz -C 解压位置

# 注意：后面的-C是大写C，如果不指定解压位置需要去掉-C，系统会把压缩包中所有文件解压到当前工作文件夹
```

文件上传到linux虚拟机的方式也有两种：
（1）通过scp指令上传，这个指令使用的前提是要开启虚拟机22端口

```java
scp mysql-8.0.28-1.el7.aarch64.rpm-bundle.tar root@192.168.244.17:/var/local
```

（2）通过第三方软件传输，这里推荐一个：[Termius](https://www.macdo.cn/27362.html)

3、解压压缩包

```java
cd /var/local
tar -xvf mysql-8.0.28-1.el7.aarch64.rpm-bundle.tar
```

可以看到解压出一大堆rpm包

4、可以看到这个mysql包的后缀中是有rpm的，所以这个包并不是像我们直接在官网下载的mysql压缩包那样直接安装，还需要我们做一些额外处理

查询虚拟机的mariadb版本，并且将其卸载，防止我们后续安装冲突

```java
rpm -qa | grep mariadb
yum remove mariadb-libs-版本
# 或者直接执行以下卸载指令
rpm -e mariadb-libs --nodeps
```

其中弹出的选择直接选`y`

[image](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/0cd066ba-6fd1-49ad-b302-0a321bf4831b/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466U4BP5GLP%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T234359Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDgm0Bzv9ymEOQIsL2BQtHlKXbKrjFfGmEeh6Xy9P1c%2BgIhAM7S4FRKhuRytU71s3k01ARh5ojnt5U4SawPDcRO2bBwKogECMb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgyVL92%2B6E4ElUxFUXMq3AOKo%2BDoMraNHnua4E8m6qpXneC9QBTLj8L12OCeU1o%2BFVdE5oBm4kCOHm8kVXmRXeIqZPFkEYdxMEib%2Fi16ksoBM8LADKH2nlYPfKyu1NvHeR6njsYMEIuQZp57hJ2txLuZyL89hl2bfr6aHs7hObXaDoFjQSMpWXlItmKTi7kjWzAMMLPPzdwaiZ1w4kcD2ipb8tVwxFdxzVW6eAfYOmo%2FJDxe87CwFmFW%2BDVMQvMEqJxpREgOexaYRZCO4EvOTJtNMrkX74hptVrk0gl6IQIoS98NtmZXLBAu3aID6teOZCF5v1%2FMZl4iykPWrLFK8YBnw0L5VZdFzD3Szst3LYjKO2fsG9f4EX6WoKaKbou9YGbb5Wl4G3k84FzqY3S%2Bfc9m%2FRCYqnlp3xBcrfptQGDRNYt4WQuU7gYwjXBn%2FaUk73CDHCvhjYRq4VIZXwi407hR7Uy3%2BSQH4aSv9pUV8llDRu3lpWNjs5LvPwpOBmnnGQOrWrqp8BYKy0s7WcdsxwHSzstU96CdXxltN6X9frt2g8V%2BEtBESiMnYT9GowbjWdP0Mgm8tun0MTERgGdyVTg5yFjRpNYHNT5KjBK3OVsQnPQBnjzIJgzbDCWzSpsbzI0JrG04KFyPVI90%2FzD8uf%2FSBjqkAWldmX%2FSOjiYkKWpGz8KJI8eQHajTd3251yiGyBNo2RYHZbFf04vJ4AtKR99UZeppdjnphJ8A1L3culERLRjcPNySbZgCXkS5CoqbddH3zE7t2YUuDtO9zu%2FRscyLb7l%2FIahdjL5USw5uk5NhrhYW0M2cFZP6wH%2BLd%2B5bYu8wk5Uxh6aBrsFqvXwU2X0qnexDCKGIdfeEhGrxZnJ5cOYaINZTpvb&X-Amz-Signature=e0ecfcfa5c91a7ec45b73138d37aa0ce4123ec820deaf12a9153ae2794c98544&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

5、接下来按序安装解压出来的包（按照如下顺序安装）

```java
rpm -ivh mysql-community-common-8.0.28-1.el7.aarch64.rpm
rpm -ivh mysql-community-client-plugins-8.0.28-1.el7.aarch64.rpm
rpm -ivh mysql-community-libs-8.0.28-1.el7.aarch64.rpm
rpm -ivh mysql-community-client-8.0.28-1.el7.aarch64.rpm
rpm -ivh mysql-community-icu-data-files-8.0.28-1.el7.aarch64.rpm
rpm -ivh mysql-community-server-8.0.28-1.el7.aarch64.rpm
```

6、初始化数据库

```java
mysqld --initialize --console
```

7、注意，这个方式安装的mysql路径在`/var/lib/mysql`下我们给该目录赋权

```java
chown -R mysql:mysql /var/lib/mysql/
chown -R mysql:mysql /var/log/mysqld.log
```

8、启动mysql

```markdown
systemctl start mysqld
## 设置mysql为开机自启，如不需要可跳过，但是每次启动虚拟机都需要再启动mysql
systemctl enable mysqld
```

查看mysql状态

```markdown
systemctl status mysqld
```

如下为启动成功

[image](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/583b2daf-988b-43ba-8fa3-bf4a35d519ef/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466U4BP5GLP%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T234359Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDgm0Bzv9ymEOQIsL2BQtHlKXbKrjFfGmEeh6Xy9P1c%2BgIhAM7S4FRKhuRytU71s3k01ARh5ojnt5U4SawPDcRO2bBwKogECMb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgyVL92%2B6E4ElUxFUXMq3AOKo%2BDoMraNHnua4E8m6qpXneC9QBTLj8L12OCeU1o%2BFVdE5oBm4kCOHm8kVXmRXeIqZPFkEYdxMEib%2Fi16ksoBM8LADKH2nlYPfKyu1NvHeR6njsYMEIuQZp57hJ2txLuZyL89hl2bfr6aHs7hObXaDoFjQSMpWXlItmKTi7kjWzAMMLPPzdwaiZ1w4kcD2ipb8tVwxFdxzVW6eAfYOmo%2FJDxe87CwFmFW%2BDVMQvMEqJxpREgOexaYRZCO4EvOTJtNMrkX74hptVrk0gl6IQIoS98NtmZXLBAu3aID6teOZCF5v1%2FMZl4iykPWrLFK8YBnw0L5VZdFzD3Szst3LYjKO2fsG9f4EX6WoKaKbou9YGbb5Wl4G3k84FzqY3S%2Bfc9m%2FRCYqnlp3xBcrfptQGDRNYt4WQuU7gYwjXBn%2FaUk73CDHCvhjYRq4VIZXwi407hR7Uy3%2BSQH4aSv9pUV8llDRu3lpWNjs5LvPwpOBmnnGQOrWrqp8BYKy0s7WcdsxwHSzstU96CdXxltN6X9frt2g8V%2BEtBESiMnYT9GowbjWdP0Mgm8tun0MTERgGdyVTg5yFjRpNYHNT5KjBK3OVsQnPQBnjzIJgzbDCWzSpsbzI0JrG04KFyPVI90%2FzD8uf%2FSBjqkAWldmX%2FSOjiYkKWpGz8KJI8eQHajTd3251yiGyBNo2RYHZbFf04vJ4AtKR99UZeppdjnphJ8A1L3culERLRjcPNySbZgCXkS5CoqbddH3zE7t2YUuDtO9zu%2FRscyLb7l%2FIahdjL5USw5uk5NhrhYW0M2cFZP6wH%2BLd%2B5bYu8wk5Uxh6aBrsFqvXwU2X0qnexDCKGIdfeEhGrxZnJ5cOYaINZTpvb&X-Amz-Signature=9948d27878378ee1779765a1c7753c304302aab6716979825b77dd05c18369b7&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

9、查看自动生成的密码

```markdown
cat /var/log/mysqld.log | grep root
```

10、用这个密码登陆mysql （可以直接复制登陆）

[image](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/a262b088-645b-4482-bae5-1965f2250ff0/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466U4BP5GLP%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T234400Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDgm0Bzv9ymEOQIsL2BQtHlKXbKrjFfGmEeh6Xy9P1c%2BgIhAM7S4FRKhuRytU71s3k01ARh5ojnt5U4SawPDcRO2bBwKogECMb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgyVL92%2B6E4ElUxFUXMq3AOKo%2BDoMraNHnua4E8m6qpXneC9QBTLj8L12OCeU1o%2BFVdE5oBm4kCOHm8kVXmRXeIqZPFkEYdxMEib%2Fi16ksoBM8LADKH2nlYPfKyu1NvHeR6njsYMEIuQZp57hJ2txLuZyL89hl2bfr6aHs7hObXaDoFjQSMpWXlItmKTi7kjWzAMMLPPzdwaiZ1w4kcD2ipb8tVwxFdxzVW6eAfYOmo%2FJDxe87CwFmFW%2BDVMQvMEqJxpREgOexaYRZCO4EvOTJtNMrkX74hptVrk0gl6IQIoS98NtmZXLBAu3aID6teOZCF5v1%2FMZl4iykPWrLFK8YBnw0L5VZdFzD3Szst3LYjKO2fsG9f4EX6WoKaKbou9YGbb5Wl4G3k84FzqY3S%2Bfc9m%2FRCYqnlp3xBcrfptQGDRNYt4WQuU7gYwjXBn%2FaUk73CDHCvhjYRq4VIZXwi407hR7Uy3%2BSQH4aSv9pUV8llDRu3lpWNjs5LvPwpOBmnnGQOrWrqp8BYKy0s7WcdsxwHSzstU96CdXxltN6X9frt2g8V%2BEtBESiMnYT9GowbjWdP0Mgm8tun0MTERgGdyVTg5yFjRpNYHNT5KjBK3OVsQnPQBnjzIJgzbDCWzSpsbzI0JrG04KFyPVI90%2FzD8uf%2FSBjqkAWldmX%2FSOjiYkKWpGz8KJI8eQHajTd3251yiGyBNo2RYHZbFf04vJ4AtKR99UZeppdjnphJ8A1L3culERLRjcPNySbZgCXkS5CoqbddH3zE7t2YUuDtO9zu%2FRscyLb7l%2FIahdjL5USw5uk5NhrhYW0M2cFZP6wH%2BLd%2B5bYu8wk5Uxh6aBrsFqvXwU2X0qnexDCKGIdfeEhGrxZnJ5cOYaINZTpvb&X-Amz-Signature=ae61390a84bccd4aa2ac9c232aa747edc21c594c1f673e4c09c644d47069f017&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

11、重置密码

```markdown
alter user 'root'@'localhost' identified by 'guojun12';
```

12、将root账号的连接host设置为全部，否则只能本地连接

```markdown
use mysql;
update user set host = "%" where user='root';
# 刷新权限
flush privileges;
```

13、开通3306端口，否则无法连接到虚拟机的mysql服务

```markdown
firewall-cmd --add-port=3306/tcp --permanent
# 开启后重新加载
firewall-cmd --reload
```

14、大功告成，到连接工具中去测试连接吧。（这里使用的是navicat数据库管理工具）


