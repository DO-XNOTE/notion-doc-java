---
title: ARM上的linux安装docker
---

# ARM上的linux安装docker

yum erase 【冲突包的包名】 buildan

删除冲突的包



### 正确安装

**下载新的 CentOS-Base.repo 到 /etc/yum.repos.d/**

**centos8（centos8官方源已下线，建议切换centos-vault源）**

wget -O /etc/yum.repos.d/CentOS-Base.repo [https://mirrors.aliyun.com/repo/Centos-vault-8.5.2111.repo](https://mirrors.aliyun.com/repo/Centos-vault-8.5.2111.repo)

或者

curl -o /etc/yum.repos.d/CentOS-Base.repo [https://mirrors.aliyun.com/repo/Centos-vault-8.5.2111.repo](https://mirrors.aliyun.com/repo/Centos-vault-8.5.2111.repo)


**aarch64服务器 离线安装docker操作手册**

## **一. 下载离线安装包**

软件包网址: https://mirrors.aliyun.com/[docker](https://so.csdn.net/so/search?q=docker&spm=1001.2101.3001.7020)-ce/linux/static/stable/aarch64/?spm=a2c6h.25603864.0.0.654c4ccaPxer04

[image](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/c749e3ab-e519-46f5-aee4-1b5426c5f605/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TL7YI2TS%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T234410Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIEANVlbb5op8E4aVTLbQnqOmQyTTNDyupq49HzYUlCNVAiAWcbxd2AZ0rGwCNsLAuOq8QdIo4P0im2KUfYMF9lrU5yqIBAjG%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMd7NbcBimCldm8UNLKtwDfoLbZ0pzLn%2BbdqorPlBbciPwndcNg9o0qf1DTtqCStx1Qub9W8zeF4xN5jKxGsS7C%2FzHJIeXKJn3rw1WYOCjKbd3C9CzF7Rw%2FJWRwd3DALP1aPnNPK80dBeThHuvsnp4XqRSt1poQiQq8QNb238ihbKZnxKoXsnbrdGoq1ElSfHqhsFX7aDYaEiYugAEaPWZC%2B0RsVpUdWlb7EDgmn3kgUp5QpW%2BaOq2shVRksjFU37tBkIlGmlxkus%2B2Sj%2FffBsVmJii6h4qye80nzsu9r%2FWrHaaxt0Lz01DHFDSMiOZBQcaQ%2ByFwc1LFbvsiteccEIQHAGPmVPBjVhxAX0RiQZDMYgL5W%2BX6ezdMo3%2B0OI24u7Dv3P%2FaZKqRhXVLo1D56TC%2Bdo4CEZ3pkYg5tlLQCA4ViH2eZrIt5ERKBl2OVSoJKRy6U6huiMGaJ7o6Dac5Gbqf%2FawI6bGD1eajF%2Bk6CIcRWEX7dMKsfqeknhTPRorEAtW21lT4Ziio%2BTBVj%2BaT%2BDXXkEv0qdvf81dzVj3NQF2w3oJOLvuF8BhomXN4Y6qDM12sG86XNS0Gufm68os9nO9pp5oEen6vegWKKTiScQ2g8T%2BADqyAoOsVrZ51k7G8zP1X31ot1TlYefrsowirr%2F0gY6pgGWVv5h0l9wesC9s2cSpHhF1xH3KiGNLCO%2FTmV7Kcz8xcECkLB%2BbksR9nQWMJ%2FH%2Bql3B%2B6Mk%2BY2ByVS%2BgaqD8esOAOK%2B68Mb%2FOrMAdyXJTYCIW2P8qjgHz20VmRw1KajOcKZDJyGD7Vi8QGI6b3dAImREPQ7KWczn1D0Z7J%2FnyxVYQ%2BJRXvVeor75QRkYxfnJgbTTyLfbrDo%2F5fmDXEY5TmwP9Ll47F&X-Amz-Signature=33f927dfbc3d1c8293ba6476aae2cf0a794b57e6c7dd793f88fb325095ed121b&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

## **二. 把下载好的软件包上传到**[**云服务器**](https://so.csdn.net/so/search?q=%E4%BA%91%E6%9C%8D%E5%8A%A1%E5%99%A8&spm=1001.2101.3001.7020)

利用Xftp7把软件包上传到服务器

## **三. 将docker离线包解压并移动到/usr/bin下**

```java
tar –zxvf docker-20.10.0.tgz
cp docker/* /usr/bin/     /*不是注释!
```

**四. 添加docker配置文件**

```java
vim /etc/systemd/system/docker.service
```

配置文件内容如下

[file](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/93b14884-93fd-4837-a908-3c874843296d/doker%E7%A6%BB%E7%BA%BF%E5%AE%89%E8%A3%85%E9%85%8D%E7%BD%AE%E6%96%87%E4%BB%B6.txt?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TL7YI2TS%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T234410Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIEANVlbb5op8E4aVTLbQnqOmQyTTNDyupq49HzYUlCNVAiAWcbxd2AZ0rGwCNsLAuOq8QdIo4P0im2KUfYMF9lrU5yqIBAjG%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMd7NbcBimCldm8UNLKtwDfoLbZ0pzLn%2BbdqorPlBbciPwndcNg9o0qf1DTtqCStx1Qub9W8zeF4xN5jKxGsS7C%2FzHJIeXKJn3rw1WYOCjKbd3C9CzF7Rw%2FJWRwd3DALP1aPnNPK80dBeThHuvsnp4XqRSt1poQiQq8QNb238ihbKZnxKoXsnbrdGoq1ElSfHqhsFX7aDYaEiYugAEaPWZC%2B0RsVpUdWlb7EDgmn3kgUp5QpW%2BaOq2shVRksjFU37tBkIlGmlxkus%2B2Sj%2FffBsVmJii6h4qye80nzsu9r%2FWrHaaxt0Lz01DHFDSMiOZBQcaQ%2ByFwc1LFbvsiteccEIQHAGPmVPBjVhxAX0RiQZDMYgL5W%2BX6ezdMo3%2B0OI24u7Dv3P%2FaZKqRhXVLo1D56TC%2Bdo4CEZ3pkYg5tlLQCA4ViH2eZrIt5ERKBl2OVSoJKRy6U6huiMGaJ7o6Dac5Gbqf%2FawI6bGD1eajF%2Bk6CIcRWEX7dMKsfqeknhTPRorEAtW21lT4Ziio%2BTBVj%2BaT%2BDXXkEv0qdvf81dzVj3NQF2w3oJOLvuF8BhomXN4Y6qDM12sG86XNS0Gufm68os9nO9pp5oEen6vegWKKTiScQ2g8T%2BADqyAoOsVrZ51k7G8zP1X31ot1TlYefrsowirr%2F0gY6pgGWVv5h0l9wesC9s2cSpHhF1xH3KiGNLCO%2FTmV7Kcz8xcECkLB%2BbksR9nQWMJ%2FH%2Bql3B%2B6Mk%2BY2ByVS%2BgaqD8esOAOK%2B68Mb%2FOrMAdyXJTYCIW2P8qjgHz20VmRw1KajOcKZDJyGD7Vi8QGI6b3dAImREPQ7KWczn1D0Z7J%2FnyxVYQ%2BJRXvVeor75QRkYxfnJgbTTyLfbrDo%2F5fmDXEY5TmwP9Ll47F&X-Amz-Signature=90bcd2769894f2e90b71c5cc06ef3f9fc7355f00f6abb8276ca520a054c766d0&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

如下:

[image](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/b420c3ef-7ec4-40a6-9225-3d426c53c530/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TL7YI2TS%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T234410Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIEANVlbb5op8E4aVTLbQnqOmQyTTNDyupq49HzYUlCNVAiAWcbxd2AZ0rGwCNsLAuOq8QdIo4P0im2KUfYMF9lrU5yqIBAjG%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMd7NbcBimCldm8UNLKtwDfoLbZ0pzLn%2BbdqorPlBbciPwndcNg9o0qf1DTtqCStx1Qub9W8zeF4xN5jKxGsS7C%2FzHJIeXKJn3rw1WYOCjKbd3C9CzF7Rw%2FJWRwd3DALP1aPnNPK80dBeThHuvsnp4XqRSt1poQiQq8QNb238ihbKZnxKoXsnbrdGoq1ElSfHqhsFX7aDYaEiYugAEaPWZC%2B0RsVpUdWlb7EDgmn3kgUp5QpW%2BaOq2shVRksjFU37tBkIlGmlxkus%2B2Sj%2FffBsVmJii6h4qye80nzsu9r%2FWrHaaxt0Lz01DHFDSMiOZBQcaQ%2ByFwc1LFbvsiteccEIQHAGPmVPBjVhxAX0RiQZDMYgL5W%2BX6ezdMo3%2B0OI24u7Dv3P%2FaZKqRhXVLo1D56TC%2Bdo4CEZ3pkYg5tlLQCA4ViH2eZrIt5ERKBl2OVSoJKRy6U6huiMGaJ7o6Dac5Gbqf%2FawI6bGD1eajF%2Bk6CIcRWEX7dMKsfqeknhTPRorEAtW21lT4Ziio%2BTBVj%2BaT%2BDXXkEv0qdvf81dzVj3NQF2w3oJOLvuF8BhomXN4Y6qDM12sG86XNS0Gufm68os9nO9pp5oEen6vegWKKTiScQ2g8T%2BADqyAoOsVrZ51k7G8zP1X31ot1TlYefrsowirr%2F0gY6pgGWVv5h0l9wesC9s2cSpHhF1xH3KiGNLCO%2FTmV7Kcz8xcECkLB%2BbksR9nQWMJ%2FH%2Bql3B%2B6Mk%2BY2ByVS%2BgaqD8esOAOK%2B68Mb%2FOrMAdyXJTYCIW2P8qjgHz20VmRw1KajOcKZDJyGD7Vi8QGI6b3dAImREPQ7KWczn1D0Z7J%2FnyxVYQ%2BJRXvVeor75QRkYxfnJgbTTyLfbrDo%2F5fmDXEY5TmwP9Ll47F&X-Amz-Signature=308f5e317b07ea7593c5b75a7483717d8b3d11d8053ccad69fb0bae07e25e6b5&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

**五. 启动docker**

```java
chmod +x /etc/systemd/system/docker.service	 #增加权限
systemctl daemon-reload		#重新加载配置文件
systemctl start docker		
systemctl enable docker.service
docker ps               #验证docker是否正常启动
```

[image](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/1634d41e-30c0-4461-8ead-ae323c8234ea/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TL7YI2TS%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T234410Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIEANVlbb5op8E4aVTLbQnqOmQyTTNDyupq49HzYUlCNVAiAWcbxd2AZ0rGwCNsLAuOq8QdIo4P0im2KUfYMF9lrU5yqIBAjG%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMd7NbcBimCldm8UNLKtwDfoLbZ0pzLn%2BbdqorPlBbciPwndcNg9o0qf1DTtqCStx1Qub9W8zeF4xN5jKxGsS7C%2FzHJIeXKJn3rw1WYOCjKbd3C9CzF7Rw%2FJWRwd3DALP1aPnNPK80dBeThHuvsnp4XqRSt1poQiQq8QNb238ihbKZnxKoXsnbrdGoq1ElSfHqhsFX7aDYaEiYugAEaPWZC%2B0RsVpUdWlb7EDgmn3kgUp5QpW%2BaOq2shVRksjFU37tBkIlGmlxkus%2B2Sj%2FffBsVmJii6h4qye80nzsu9r%2FWrHaaxt0Lz01DHFDSMiOZBQcaQ%2ByFwc1LFbvsiteccEIQHAGPmVPBjVhxAX0RiQZDMYgL5W%2BX6ezdMo3%2B0OI24u7Dv3P%2FaZKqRhXVLo1D56TC%2Bdo4CEZ3pkYg5tlLQCA4ViH2eZrIt5ERKBl2OVSoJKRy6U6huiMGaJ7o6Dac5Gbqf%2FawI6bGD1eajF%2Bk6CIcRWEX7dMKsfqeknhTPRorEAtW21lT4Ziio%2BTBVj%2BaT%2BDXXkEv0qdvf81dzVj3NQF2w3oJOLvuF8BhomXN4Y6qDM12sG86XNS0Gufm68os9nO9pp5oEen6vegWKKTiScQ2g8T%2BADqyAoOsVrZ51k7G8zP1X31ot1TlYefrsowirr%2F0gY6pgGWVv5h0l9wesC9s2cSpHhF1xH3KiGNLCO%2FTmV7Kcz8xcECkLB%2BbksR9nQWMJ%2FH%2Bql3B%2B6Mk%2BY2ByVS%2BgaqD8esOAOK%2B68Mb%2FOrMAdyXJTYCIW2P8qjgHz20VmRw1KajOcKZDJyGD7Vi8QGI6b3dAImREPQ7KWczn1D0Z7J%2FnyxVYQ%2BJRXvVeor75QRkYxfnJgbTTyLfbrDo%2F5fmDXEY5TmwP9Ll47F&X-Amz-Signature=52dfef1396aafec006ff220767e155e1b81b5fe3f82ac864629f3f41ebea973d&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

成功启动!


docker安装redis：

[https://www.runoob.com/docker/docker-install-redis.html](https://www.runoob.com/docker/docker-install-redis.html)

Docer安装rabbitMQ：

[https://blog.csdn.net/qq_45502336/article/details/118699251](https://blog.csdn.net/qq_45502336/article/details/118699251)




进入Docker中配置其中的Nginx：

进入Docker命令： docker exec -it 镜像ID（比如nginx） bash

安装在dokcer中可以编辑文件的命令：

### **1. ps: command not found**

使用如下命令安装

`apt-get update && apt-get -y install procps`

### **2. **[**vim**](https://so.csdn.net/so/search?q=vim&spm=1001.2101.3001.7020)**: command not found**

使用如下命令安装

`apt-get update && apt-get -y install vim`



**Docker启动已经退出的镜像命令**

查看所有存在的镜像：找到 id

docker ps -a 

使用Docker启动该镜像：

docker start + 镜像id


