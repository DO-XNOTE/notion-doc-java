---
title: 文章内容
---

# 文章内容

[**智能解析 + Nginx反向代理，自建CDN加速节点**](https://www.xiaoz.me/archives/8775)

## [**智能解析 + Nginx反向代理，自建CDN加速节点**](https://www.xiaoz.me/archives/8775)

买VPS就像“xidu”一样，根本停不下来呀有木有？如果你手里已经有一打VPS，不知道用来干嘛，不妨一起来研究下如何自建CDN，如《[CentOS安装Fikker 缓存，自建CDN加速](https://www.xiaoz.me/archives/8709)》，Fikker非常方便，功能也很强大，不过免费版不支持页面缓存、也不支持HTTP/2，我们也可以用Nginx反向代理实现自建CDN.

### **名词概念**

**智能解析：**域名智能解析是指域名解析服务器根据来访者的IP类型，对同一域名作出相应不同解析。对IP来自电信的访问者，将域名解析到该域名对应IP地址为电信的服务器上。对IP来自网通的访问者，将域名解析到该域名对应IP地址为网通的服务器上。以保证访问者不因网通电信线路瓶颈而造成网速慢。

**反向代理：**反向代理（Reverse Proxy）方式是指以代理服务器来接受internet上的连接请求，然后将请求转发给内部网络上的服务器，并将从服务器上得到的结果返回给internet上请求连接的客户端，此时代理服务器对外就表现为一个反向代理服务器。

**CDN：**CDN的全称是Content Delivery Network，即内容分发网络。其基本思路是尽可能避开互联网上有可能影响数据传输速度和稳定性的瓶颈和环节，使内容传输的更快、更稳定。其目的是使用户可就近取得所需内容，解决 Internet网络拥挤的状况，提高用户访问网站的响应速度。

[image](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/7a80e459-7a2c-45a6-a09c-ba734197b770/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UGSV6YCA%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T231250Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDjUTe3pr1DNpmK2sGuvwaovwE1Qnebld906k3YAx3AIAIhAL%2FgILFUlHA4XotgegPkttRTHkkcE1SOSoHr0u49ZmWDKogECMb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgzKT8YNQ2Maw%2FY5b1wq3AOIjFhQepoJMyMReGfc5P6hfujsO2IKGHTgV85ZYdnn9hOKiu88CwxNB%2Fv1lR3LmN6Fa0DvgXw7CcRzoTGsysYmQn8grtxKplDTe2vrUo36e2g3o6GJPIqbQUStCCcJuhbKXYf3SJMmQu1I49Io7QPHa6FkDp4U%2B%2Bz2kWH3zjuPsUrXF1ABC1bYKMVhr9mJB58RiifBNIG6%2FremL3NnKrSTDxamFQFgqB0XFL5w9NYmwHtuftPadv1UIdlFSCHr7OGx9vn4%2FnHgElLON9ALvvs8GXi7IircQ4YKei1JrzH1GvdvfcLLIpaSj4vBx%2B0WgnZoc%2FeWOAxwuSeasPv1H52sI89rtvfG782g8p0GMyg6OeotzSIjE6iuICDdzMna9ABy9OW9ZG9Tu4qyudopWWuHVee8HCS627De0QId1Tsaj%2B%2BPi%2BsG%2BQsLO5Ud75cwOK%2B3mJDG6CY3MDJypruWW6wu%2B5FhpX74AcJnF5hhWg%2Fsv7Q9BaKlyUoX4JVJv6jm2Gl9Dd0MuhEW0w%2B%2B%2FsYjfmybnyUpRgOuR%2Fx%2FqRNwOI7zUvUtFkV%2FzrEjD315vKy4NEt3r71jmXt9NZPqFGpb7pmnjFfR0NSRJkbRiNpQGI0bgUC%2BdWd7lsdtuawHITC2uv%2FSBjqkAUPsExQBgzqoCyRmv4R%2FLyZnVIPNUptnjD7%2FJz18m7mK0%2FfjR1w%2FCHh%2Fb%2BhwaWwUn%2F9ORIYsdkaq%2FTm3S3zsvQfvZjUKi1qHUqV6QfnkeFcAfGywwb2T43Ut4WiJkOBZjSMXj7%2BNNviCxnB0vXRIwVcxiW%2BYQ%2Fh%2BdC8GhwPDU69aCjPwZh%2BOukzxuQwd7ZsmmCVULuT3uB%2FI%2F2IHxIjlQ1uEncFN&X-Amz-Signature=f3f8cae4519ef12cd37111f52e2999e1265094a4e645564a72ae68e049217a14&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

### **准备工作**

- 智能解析：推荐使用[CloudXNS](https://www.xiaoz.me/archives/6569)或DNSPOD之类的。
- VPS 3台以上，如[野草云香港VPS](https://www.xiaoz.me/archives/8394)
### **安装Nginx**

需要在所有CDN服务器节点安装Nginx，推荐使用[OneinStack](https://oneinstack.com/)或军哥的lnmp.org一键包，如何安装Nginx自行参考脚本官网就行了。

如果您都不想使用，可以试试xiaoz的一键Nginx安装包（适用于Centos 7、Deebian 8），执行下面的命令安装即可。

```plain text
wget https://raw.githubusercontent.com/helloxz/nginx-cdn/master/nginx.sh
chmod +x nginx.sh && ./nginx.sh

```

### **反向代理配置**

反向代理通俗点你把它理解成CDN节点就行了，这里用4台服务器作为解释，

- 源站:192.168.1.100，就是网站数据真实存放的地方
- CDN1:192.168.1.101（电信节点）
- CDN2:192.168.1.102（联通节点）
- CDN3:192.168.1.103（移动节点）
假如我需要对www.xiaoz.me搭建CDN节点，数据放在192.168.1.100，需要先修改hosts指向，告知CDN节点从那里去获取网站数据，也就是回源地址，需要在CDN1/CDN2/CDN3做如下修改：

```plain text
vi /etc/hosts
192.168.1.100   www.xiaoz.me

```

分别在CDN1/CDN2/CDN3下创建nginx配置文件`xiaoz.me.conf`

```plain text
#创建缓存目录
mkdir -p /data/wwwroot/caches/www.xiaoz.me
#设置缓存目录权限
chown -R www:www /data/wwwroot/caches/www.xiaoz.me
#创建xiaoz.me.conf
vi /usr/local/nginx/conf/vhost/xiaoz.me.conf

```

在`xiaoz.me.conf`中添加下面的内容，缓存目录/缓存时间请根据实际情况调整，后面会详细说明各参数含义。

```javascript
proxy_cache_path /data/wwwroot/caches/www.xiaoz.me levels=1:2 keys_zone=xiaoz:50m inactive=30m max_size=50
server {
    listen 80;
    server_name www.xiaoz.me;
    charset utf-8,gbk;
        location / {
        proxy_set_header Accept-Encoding "";
           proxy_pass https://www.xiaoz.me;
           proxy_redirect off;
           proxy_set_header X-Real-IP $remote_addr;
           proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
           proxy_cache xiaoz;
           proxy_cache_valid  200 304  30m;
           proxy_cache_valid  301 24h;
           proxy_cache_valid  500 502 503 504 0s;
           proxy_cache_valid any 1s;
           proxy_cache_min_uses 1;
           expires 12h;
    }
}
```

- `/data/wwwroot/caches/www.xiaoz.me`:为缓存目录
- `levels`:指定该缓存空间有两层hash目录，第一层目录为1个字母，第二层为2个字母。
- `keys_zone=xiaoz:50m`:为缓存空间起个名字，这里取名为“xiaoz”，后面的50m指内存缓存空间
- `inactive=30m`:如果30分钟内该资源没有被访问则删除
- `max_size=50m`:指硬盘缓存大小为50MB
- `proxy_cache_valid`:指定状态码缓存时间，前面写状态码，后面写缓存时间。
最后别忘了重载nginx使配置生效，如果使用的oneinstack直接输入命令：`service nginx reload`，如果是xiaoz一键脚本输入:`/usr/local/nginx/sbin/nginx -s reload`，如果有报错，可以贴出报错信息一起讨论下。

### **智能解析**

假如您上面CDN1/CDN2/CDN3三个CDN节点都配置好了，在CloudXNS后台，将不同的运营商指向不同的节点，使其达到分发和缓存加速效果，如下截图。

[image](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/a2cf164e-d85e-45e6-b0b4-2d288f3c7399/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UGSV6YCA%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T231250Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDjUTe3pr1DNpmK2sGuvwaovwE1Qnebld906k3YAx3AIAIhAL%2FgILFUlHA4XotgegPkttRTHkkcE1SOSoHr0u49ZmWDKogECMb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgzKT8YNQ2Maw%2FY5b1wq3AOIjFhQepoJMyMReGfc5P6hfujsO2IKGHTgV85ZYdnn9hOKiu88CwxNB%2Fv1lR3LmN6Fa0DvgXw7CcRzoTGsysYmQn8grtxKplDTe2vrUo36e2g3o6GJPIqbQUStCCcJuhbKXYf3SJMmQu1I49Io7QPHa6FkDp4U%2B%2Bz2kWH3zjuPsUrXF1ABC1bYKMVhr9mJB58RiifBNIG6%2FremL3NnKrSTDxamFQFgqB0XFL5w9NYmwHtuftPadv1UIdlFSCHr7OGx9vn4%2FnHgElLON9ALvvs8GXi7IircQ4YKei1JrzH1GvdvfcLLIpaSj4vBx%2B0WgnZoc%2FeWOAxwuSeasPv1H52sI89rtvfG782g8p0GMyg6OeotzSIjE6iuICDdzMna9ABy9OW9ZG9Tu4qyudopWWuHVee8HCS627De0QId1Tsaj%2B%2BPi%2BsG%2BQsLO5Ud75cwOK%2B3mJDG6CY3MDJypruWW6wu%2B5FhpX74AcJnF5hhWg%2Fsv7Q9BaKlyUoX4JVJv6jm2Gl9Dd0MuhEW0w%2B%2B%2FsYjfmybnyUpRgOuR%2Fx%2FqRNwOI7zUvUtFkV%2FzrEjD315vKy4NEt3r71jmXt9NZPqFGpb7pmnjFfR0NSRJkbRiNpQGI0bgUC%2BdWd7lsdtuawHITC2uv%2FSBjqkAUPsExQBgzqoCyRmv4R%2FLyZnVIPNUptnjD7%2FJz18m7mK0%2FfjR1w%2FCHh%2Fb%2BhwaWwUn%2F9ORIYsdkaq%2FTm3S3zsvQfvZjUKi1qHUqV6QfnkeFcAfGywwb2T43Ut4WiJkOBZjSMXj7%2BNNviCxnB0vXRIwVcxiW%2BYQ%2Fh%2BdC8GhwPDU69aCjPwZh%2BOukzxuQwd7ZsmmCVULuT3uB%2FI%2F2IHxIjlQ1uEncFN&X-Amz-Signature=b4a14f0b8b7f3c384ba8c89a98442c682e248ccfcdcdd044f3d83f4efceef48a&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

### **其它说明**

解析后可以使用超级ping工具ping.chinaz.com测试各地解析是否生效，也可以本地修改hosts访问测试是否正常，同时分享下小z博客（www.xiaoz.me）的完整CDN配置：

```javascript
proxy_cache_path /data/wwwroot/caches/www.xiaoz.me levels=1:2 keys_zone=xiaoz:50m inactive=30m max_size=50m;
server {
    listen 443 ssl http2;
    ssl_certificate /data/ssl/www.xiaoz.me/www_xiaoz_me.crt;
    ssl_certificate_key /data/ssl/www.xiaoz.me/www_xiaoz_me.key;
    ssl_session_timeout 1d;
    ssl_session_cache builtin:1000 shared:SSL:10m;
    ssl_dhparam /data/ssl/dhparam.pem;

    ssl_protocols TLSv1 TLSv1.1 TLSv1.2;
    ssl_ciphers 'ECDHE-ECDSA-CHACHA20-POLY1305:ECDHE-RSA-CHACHA20-POLY1305:ECDHE-ECDSA-AES128-GCM-SHA256:ECDHE-RSA-AES128-GCM-SHA256:ECDHE-ECDSA-AES256-GCM-SHA384:ECDHE-RSA-AES256-GCM-SHA384:DHE-RSA-AES128-GCM-SHA256:DHE-RSA-AES256-GCM-SHA384:ECDHE-ECDSA-AES128-SHA256:ECDHE-RSA-AES128-SHA256:ECDHE-ECDSA-AES128-SHA:ECDHE-RSA-AES256-SHA384:ECDHE-RSA-AES128-SHA:ECDHE-ECDSA-AES256-SHA384:ECDHE-ECDSA-AES256-SHA:ECDHE-RSA-AES256-SHA:DHE-RSA-AES128-SHA256:DHE-RSA-AES128-SHA:DHE-RSA-AES256-SHA256:DHE-RSA-AES256-SHA:ECDHE-ECDSA-DES-CBC3-SHA:ECDHE-RSA-DES-CBC3-SHA:EDH-RSA-DES-CBC3-SHA:AES128-GCM-SHA256:AES256-GCM-SHA384:AES128-SHA256:AES256-SHA256:AES128-SHA:AES256-SHA:DES-CBC3-SHA:!DSS';
    ssl_prefer_server_ciphers on;

    ssl_stapling on;
    ssl_stapling_verify on;

    server_name www.xiaoz.me;
    access_log /data/wwwlogs/xiaoz.me_nginx.log combined;

    charset utf-8,gbk;
        location / {
        proxy_set_header Accept-Encoding "";
           proxy_pass https://www.xiaoz.me;
           proxy_redirect off;
           proxy_set_header X-Real-IP $remote_addr;
           proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
           proxy_cache xiaoz;
           proxy_cache_valid  200 304  30m;
           proxy_cache_valid  301 24h;
           proxy_cache_valid  500 502 503 504 0s;
           proxy_cache_valid any 1s;
           proxy_cache_min_uses 1;
           expires 12h;
    }
}
server {
    listen 80 default_server;
    return 301 https://$host$request_uri;
}
```

### **总结**

以上教程需要一点linux基础，如果您手里有不少闲置CDN，可以折腾试试，若有任何疑问欢迎留言讨论，原创文章转载请注明。


