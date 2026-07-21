---
title: 设置 jenkins 在 linux 中开机启动
---

# 设置 jenkins 在 linux 中开机启动

**Centos 7 Linux创建Jenkins启动脚本以及开机启动服务—==========(216的 linux上)**

1.启动 jenkins 脚本

```shell
#!/bin/bash
#主要目的用于开机启动服务,不然 启动jenkins.war包没有java -jar的>权限
JAVA_HOME=/usr/local/software/jdk-17.0.5


pid=`ps -ef | grep jenkins.war | grep -v 'grep'| awk '{print $2}'| wc -l`
  if [ "$1" = "start" ];then
  if [ $pid -gt 0 ];then
  echo 'jenkins is running...'
else
  #java启动服务 配置java安装根路径,和启动war包存的根路径
  nohup $JAVA_HOME/bin/java -jar /usr/local/jenkin-home/jenkins.war>jenkins.log --httpPort=8080  2>&1 &
  fi
  elif [ "$1" = "stop" ];then
  exec ps -ef | grep jenkins | grep -v grep | awk '{print $2}'| xargs kill -9
  echo 'jenkins is stop..'
else
  echo "Please input like this:"./jenkins.sh start" or "./jenkins stop""
  fi

```

注意：在写shell脚本时，开头一定要加上#!/bin/bash，否则执行该脚本会报错

根据自己的java安装目录，和jenkins.war包存放目录来修改脚本，我的脚本放在/usr/local/jenkins/目录下

2.让jenkins有可执行权限

```shell
chmod +x /usr/local/jenkin-home/jenkins.sh
```

补充：

启动jenkins

```shell
/usr/local/jenkin-home/jenkins.sh start
```

停止jenkins

```shell
/usr/local/jenkin-home/jenkins.sh stop
```

3.配置开机启动服务
3.1 到 /lib/systemd/system 服务注册目录下创建 jenkins.service

```shell
[Unit]
description=Jenkins
After=network.target
 
[Service]
Type=forking
ExecStart=/usr/local/jenkin-home/jenkins.sh start
ExecReload=
ExecStop=/usr/local/jenkin-home/jenkins.sh stop
PrivateTmp=true
 
[Install]
WantedBy=multi-user.target

```

执行路径根据实际情况进行修改

3.2创建好服务后,执行一下命令刷新配置

```shell
systemctl daemon-reload
```

3.3启动脚本

```shell
systemctl start jenkins.service
```

3.4查看启动脚本状态是否启用成功(失败的话,看错误日志进行修改)

失败时，查看日志：journalctl -xe

```shell


systemctl status jenkins.service
```

[image](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/d38301d4-bdcc-471a-aa80-a0e237c7c45b/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662KGXQNZ5%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T234403Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDqoCCchasYi5nRN3fM1EaJ%2F0BvMs7a%2FDs%2FWRIXWJHXQgIgfCScFJxQTbV%2F5xWkTvlAfiTZZ2f8%2BOdTUX4YVTs1bn0qiAQIxv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDNb9WyyDOo%2FVmO8k8CrcA41qA%2BbjIKSet%2FBQe4oQFfcuWZ8tR3M28Ex5Tq%2BTxZPEMcIMlIxhQYjYEIZ3v3ECneG8CldG7eF2zRFz7U07GhosHAzLTeyXuTYGIDBfT%2BkHXh6TVj1iN44NT9bZPPJGt0j6ymY7PBQScPvftDR1nxMUJe8bxp3noJlCVHCzLJU8QDWr19qvdtZVUsFesJpARdZVkLfydEhZdShAHtGlTbLL%2Fdxj6P24V4zYqDockiaTjOa7ZYZ866El2H5nECjrVgoOKU5mbtCW2j0OWz4JP7zgpwLqRGixcmwaPXS8sCyzgPdmFFUiBFhdCfbyC4w165PUwTgfIpiS1yNN1BkF2SRokNmP9JjeBv%2B3fxu%2BCcNNzNJg3q08WdgrTb3A7D8Dum7Iue1zPyAO1ZoDsZNMTFveixkkP2h%2FfKw1ZY4lHjsbc7MhvYRC8WLXQzhv%2Bi41m7z%2F%2BXfE5vuLlf9hl9DZex74cvu%2F2DtPIZud9gCcuLSsRUcJuyhbMuRUog%2BamRD2fZ4WMmnL24WZjwBM0onVuE%2BRU%2BvHEZ4bxz0loRE7Yjq5kC3Z%2BzSNf5oH8%2BtsoGDvh9VA3zthndji%2FBqJTr5TZ0DjcZVvSQu0MTdYZ2uo%2FMdgi1CxSf%2F%2BHH2xMNeeMOq3%2F9IGOqUB2VwmyhbDOgANHm%2B73YT70IuVrG6rmjq9atuES0USfIGAjKDhtPSPdHKBJOr0jjvTEqnbWkzF07jLwLwSwhv3Np4%2FKFFSdCbQZHOvyHhSBTMHe7aEAclW7QaWXWmoJ3HoZR23GbnYLSNabmCIFnIYxV4pUmAsuWW2a%2Fxl7uKVnHS%2FMjVwlgmgqIgiCmSb9StFPhgFEkuLp87gzQaAvSrenM4507%2Fy&X-Amz-Signature=9cf1bec01fa12783d4dbebda9a99e3994d5d6b656c64cabe81b64abf5dba941f&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

3.5设置开机启动

```shell
systemctl enable jenkins.service
```

3.6查看设置开机启动的服务列表

```shell
systemctl list-units --type=service
```

[image](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/a7cbc533-884b-4f0a-80b4-29cc0769dd40/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662KGXQNZ5%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T234403Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDqoCCchasYi5nRN3fM1EaJ%2F0BvMs7a%2FDs%2FWRIXWJHXQgIgfCScFJxQTbV%2F5xWkTvlAfiTZZ2f8%2BOdTUX4YVTs1bn0qiAQIxv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDNb9WyyDOo%2FVmO8k8CrcA41qA%2BbjIKSet%2FBQe4oQFfcuWZ8tR3M28Ex5Tq%2BTxZPEMcIMlIxhQYjYEIZ3v3ECneG8CldG7eF2zRFz7U07GhosHAzLTeyXuTYGIDBfT%2BkHXh6TVj1iN44NT9bZPPJGt0j6ymY7PBQScPvftDR1nxMUJe8bxp3noJlCVHCzLJU8QDWr19qvdtZVUsFesJpARdZVkLfydEhZdShAHtGlTbLL%2Fdxj6P24V4zYqDockiaTjOa7ZYZ866El2H5nECjrVgoOKU5mbtCW2j0OWz4JP7zgpwLqRGixcmwaPXS8sCyzgPdmFFUiBFhdCfbyC4w165PUwTgfIpiS1yNN1BkF2SRokNmP9JjeBv%2B3fxu%2BCcNNzNJg3q08WdgrTb3A7D8Dum7Iue1zPyAO1ZoDsZNMTFveixkkP2h%2FfKw1ZY4lHjsbc7MhvYRC8WLXQzhv%2Bi41m7z%2F%2BXfE5vuLlf9hl9DZex74cvu%2F2DtPIZud9gCcuLSsRUcJuyhbMuRUog%2BamRD2fZ4WMmnL24WZjwBM0onVuE%2BRU%2BvHEZ4bxz0loRE7Yjq5kC3Z%2BzSNf5oH8%2BtsoGDvh9VA3zthndji%2FBqJTr5TZ0DjcZVvSQu0MTdYZ2uo%2FMdgi1CxSf%2F%2BHH2xMNeeMOq3%2F9IGOqUB2VwmyhbDOgANHm%2B73YT70IuVrG6rmjq9atuES0USfIGAjKDhtPSPdHKBJOr0jjvTEqnbWkzF07jLwLwSwhv3Np4%2FKFFSdCbQZHOvyHhSBTMHe7aEAclW7QaWXWmoJ3HoZR23GbnYLSNabmCIFnIYxV4pUmAsuWW2a%2Fxl7uKVnHS%2FMjVwlgmgqIgiCmSb9StFPhgFEkuLp87gzQaAvSrenM4507%2Fy&X-Amz-Signature=9430c3f338bdc2875419aef589963fd1d7d8fee251fafbba9105edb60dfc4d90&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

3.7停止服务命令

```shell
systemctl stop jenkins.service
```


