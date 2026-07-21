---
title: 设置 nexus 在 linux 中开机启动
---

# 设置 nexus 在 linux 中开机启动

在/etc/init.d目录下创建nexus文件

首先转到root用户，然后在这个目录下执行vim nexus命令。

然后把下面这段复制进去，首几行不要漏了。

```markdown
#!/bin/bash    
#chkconfig:2345 20 90    
#description:nexus3    
#processname:nexus3 r   
export JAVA_HOME=/usr/local/jdk  
case $1 in    
        start) su root /usr/local/nexus3/bin/nexus start;;    
        stop) su root /usr/local/nexus3/bin/nexus stop;;    
        status) su root /usr/local/nexus3/bin/nexus status;;    
        restart) su root /usr/local/nexus3/bin/nexus restart;;    
        dump ) su root /usr/local/nexus3/bin/nexus dump ;; 
        console ) su root /usr/local/nexus3/bin/nexus console ;;          
        *) echo "require console | start | stop | restart | status | dump " ;;    
esac
```

# 执行命令

```markdown


chmod 777 /etc/init.d/nexus
chkconfig --add  nexus
systemctl list-unit-files

```

# 验证

```markdown

service nexus start

service nexus stop



登录用户：
#http://192.168.13.218:8081/#user/account
#user： admin
#pass： guojun12
```

