---
title: 1-19 ab 使用教程（网站 benchmark 测试工具）
---

# 1-19 ab 使用教程（网站 benchmark 测试工具）

[https://httpd.apache.org/docs/2.4/programs/ab.html](https://httpd.apache.org/docs/2.4/programs/ab.html)

1—19ab使用教程
ab使用教程
ab全称Apache HTTP server benchmarking tool的缩写，是Apache自 带的网站benchmark测试工具。使用非常方便，简约而不简单。
官方网站：https:/httpd.apache.org/docs/2.4/programs/ab.html TIPS


可达到ab相同效果的工具：
wrk: [https://github.com/wg/wrk](https://github.com/wg/wrk) 

wrk2: [https://github.com/giltene/wrk2](https://github.com/giltene/wrk2) 

JMeter: [https://jmeter.apache.org/](https://jmeter.apache.org/) 

Locust: [https://locust.io/](https://locust.io/)
安装 

macOS
系统自带，直接使用即可

Centos 7
运行如下命令即可安装
yum -y install httpd-tools 

Windows
·前往https:/www.apachehaus.com/cgi-bin/download.plx下载 ab 安装包。
.解压，将目录切换到安装包的bin目录，并在终端中执行如下命令即可   ./ab xxxx 

TIPS
由于笔者没有Windows环境，所以此步骤无法亲测。亲们可百度“Windows 安装ab”，参照结果安装即可。资料非常丰富。
使用说明
b是一个命令行工具，使用说明如下：ab -help
Usage: ab     [options]      [http [s]: //]hostname [ port]/path 

Options are:
-n requests                 指定请求多少次 

-c concurrency         指定并发数（指定同时发送几个请求）-t timelimit
测试持续的最长时间，默认无限制，此参数隐含一

-s timeout   每个请求的超时时间，默认30秒-b windowsize
指定TCP收发缓存大小，单位字节-B address
指定在发起连接时绑定的IP地址-p postfile
指定想要POST的文件，需和—T参数配合使用-u putfile
指定想要PUT的文件，需和—T参数配合使用-T content-type
指定POST/PUT文件时的Content-type。默认t -v verbosity
详细模式，打印更多日志
将结果输出到html表格中-i
使用HEAD方式代替GET发起请求-x attributes
插入字符串作为table标签的属性-y attributes
插入字符串作为tr标签的属性-z attributes
插入字符串作为td或th标签的属性-C attribute
添加Cookie,例如Apache=1234;可重复该参数 -H attribute
添加任意的请求头，例如Accept-Encoding:g -A attribute
添加Basic WWW认证信息，用户名和密码之间用：-P attribute
添加Basic Proxy认证信息，用户名和密码之间-X proxy: port
指定代理地址
打印ab的版本信息 -k
使用HTTP的KeepAlive特性 -d
不显示百分比 -S
不显示预估和警告信息-q
默认情况下，如果处理的请求数大于150，ab每处-g
filename
输出结果信息到gnuplot格式的文件中-e
filename
输出结果信息到CSV格式的文件中-r
指定接收到错误信息时不退出程序-h
显示使用说明 -Z
ciphersuite
指定SSL/TLS密码套件-f
protocol
指定SSL/TLS协议(SSL3,TLS1,TLS1.1,TI 

示例
ab -c 100 -n 10000 [http://www.baidu.com/](http://www.baidu.com/) 表示并发100，请求baidu 10000次。
TIPS
[http://www.baidu.com/不能写成http:/www.baidu.com](http://www.baidu.com/%E4%B8%8D%E8%83%BD%E5%86%99%E6%88%90http:/www.baidu.com) 。这是因为http:/www.baidu.com不符合ab要求的[http [s]:/]hostname[:port]/path 格式要求。这是个小坑，需 要注意一下
报表解读
ab -c 10 -n 1000 http: [//www.baidu.com/](notion://www.baidu.com/)
This is ApacheBench, Version 2.3 <$Revision: 1843412 $ Copyright 1996 Adam Twiss, Zeus Technology Ltd, http:// [www.zeustech.net/](http://www.zeustech.net/)
Licensed to The Apache Software Foundation, http: //www. [apache.org/](http://apache.org/)
Benchmarking www. baidu. com (be patient) Completed
100
requests Completed
200
requests Completed
300
requests Completed 400
requests Completed
500
requests Completed 600
requests Completed 700
requests Completed a
800
requests Completed 900
requests Completed 1000 requests
Finished 1000 requests
#展示测试地址所使用的服务器软件及版本Server Software:
BWS/1.1 #测试地址的主机名
Server Hostname:
[www.baidu.com](http://www.baidu.com/) #测试地址的端口
Server Port:
80 #测试地址的路径
Document Path:
/ #测试地址的文档大小
Document Length:
255598 bytes #并发数
Concurrency Level:
10 #测试花费了多久
Time taken for tests:
81.881 seconds #测试总共请求了多少次
Complete requests:
1000 #失败的请求数
Failed requests:
979
(Connect: 0, Receive: 0, Length: 979, Exceptions: 0) #传输的总数据量
Total transferred:
256761473  bytes #HTML文档的总数据量
HTML transferred:
255605512  bytes
#平均每秒的请求数，也叫RPS，该值越大表示服务器吞吐量越大，性能表现越好
Requests per second:
12.21[#/sec](notion://www.notion.so/mean) #请求平均耗时，越小说明响应越快
Time per request:
818.815 [ms] (mean) #服务器平均处理时间，其实是服务器吞吐量的倒数
Time per request:
81.881 [ms] (mean, across all c oncurrent requests)
#每秒获取的数据长度，单位单位：KB/sTransfer rate:
3062.28 [Kbytes/sec] received #连接时间统计信息
Connection Times
(ms) #
最小 平均
中值
最大 min
mean [+/-sd]
median
max #连接时间
Connect:
17
154118.0
135
1416 #处理时间
Processing:
329
661211.2
602
1824 #等待时间
Waiting:
22 160 88.4
143
1089 #总计时间
Total:
391816263.4
731
2521
#请求耗时的统计信息。例如请求经过排序后，50百分位的请求花费了731毫秒；99百分位的请求花费了1942毫秒等
Percentage of the requests served within a certain time (ms )
50%
731 66% 804 75%
873 80%
943 90% 1154 95% 1332 98% 1726 99% 1942 100%
2521(longest request)


[image](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/44da94d4-798f-4afb-9ab1-cb75e99fc611/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RTV5I5Y6%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T230203Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCH0ZtEuB5FNBJshd0v8M%2BGTmK%2BqpSdxJ9okX%2FoxfwqpMCIQDUG8aI1q4LRIvCgLjCrpLwKEWFfBOVi5vBSjuA4SN7niqIBAjG%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMbYNsEgyQ3MwSdlIkKtwDYbVC14EgwNo5ZtbZTtR3PAMuD73hDO3rKp7Pw18zAaj00NrQAizHFs83LEHA%2FxQQsxhLy36KhTfeV1EhbZP1HRBZvuAzEfG0GCrT3cKNDftRzlvGyuidE0cDr%2F4CUVh64Bb%2Fwn33DPbCBz5iGWjuZ9Q418%2Bem4YGJtw%2B998Bz%2FPbKUr%2BMVgqx4Bz4Abaeq0DzmMZk9ft5vBCEV%2Bgmek9wNNbLq4nHRoNTKOnG%2BcotjZintdmqM%2FR4yTMEj3Kogd8IFRw5DumqYQTkCNrL%2BLax2miEPuZvct%2BkDPMMvmVqP2H41wQm5uiEkNYbY9VdRpdgMoPUsysFcT4s77RnsGYPx8E3PaYq4fj4nm9TYR5Mf5%2BoOrTxnVwd8z88lu4yHKRKOTEel9nHFMG8heOIqkqOaFGoO%2FWHAbVDgWbBEX725RIewMUheMHXW6MMxPujtxqGsxjxEdcQE%2BlztCq%2B0lYkhLHFnD1TFQLbhGf1xu90e7OlgW6ZgRAME7c6eXVC9lsnmj283I9vfPBFSzU7iEu0hranRmYCkkA0EGlc8NFijLiGECNRks7egbuWAdGquhVHoO%2BABP8SSbIp8JpEOf%2BsexLTdyAOH2lISGEYiolG21L0Tqe7sEbUxYQB%2BMw%2F7j%2F0gY6pgFfeyalXIjaxPhLnsdb%2BJXmEZJ%2FvwuYd4L5cd5wceozhREr1%2FxSLwwf7LGHhgGCzuXvNX8A%2BAXuC35lYwztgK0y4geKvwQEJngPO3Cb5hiH3K8yDfGI%2Bn9wZdtLE7NJiSmPPYB2yOiBY4FvFFVnqy%2B8A%2FPOVt2KwwwCi%2FgCw0fTfXvd7JYqVq2HEQho6XKcALdLEvAGttUXzXGQ73nRBGqKhjgdl0Ig&X-Amz-Signature=05bb4e050eee02c0b5f91366cdcf70e40ea69cb76250d686ff0e742d6ad43b22&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

[image](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/185d0dd9-63f3-44a8-aacd-f1bd5b651a33/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RTV5I5Y6%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T230203Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCH0ZtEuB5FNBJshd0v8M%2BGTmK%2BqpSdxJ9okX%2FoxfwqpMCIQDUG8aI1q4LRIvCgLjCrpLwKEWFfBOVi5vBSjuA4SN7niqIBAjG%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMbYNsEgyQ3MwSdlIkKtwDYbVC14EgwNo5ZtbZTtR3PAMuD73hDO3rKp7Pw18zAaj00NrQAizHFs83LEHA%2FxQQsxhLy36KhTfeV1EhbZP1HRBZvuAzEfG0GCrT3cKNDftRzlvGyuidE0cDr%2F4CUVh64Bb%2Fwn33DPbCBz5iGWjuZ9Q418%2Bem4YGJtw%2B998Bz%2FPbKUr%2BMVgqx4Bz4Abaeq0DzmMZk9ft5vBCEV%2Bgmek9wNNbLq4nHRoNTKOnG%2BcotjZintdmqM%2FR4yTMEj3Kogd8IFRw5DumqYQTkCNrL%2BLax2miEPuZvct%2BkDPMMvmVqP2H41wQm5uiEkNYbY9VdRpdgMoPUsysFcT4s77RnsGYPx8E3PaYq4fj4nm9TYR5Mf5%2BoOrTxnVwd8z88lu4yHKRKOTEel9nHFMG8heOIqkqOaFGoO%2FWHAbVDgWbBEX725RIewMUheMHXW6MMxPujtxqGsxjxEdcQE%2BlztCq%2B0lYkhLHFnD1TFQLbhGf1xu90e7OlgW6ZgRAME7c6eXVC9lsnmj283I9vfPBFSzU7iEu0hranRmYCkkA0EGlc8NFijLiGECNRks7egbuWAdGquhVHoO%2BABP8SSbIp8JpEOf%2BsexLTdyAOH2lISGEYiolG21L0Tqe7sEbUxYQB%2BMw%2F7j%2F0gY6pgFfeyalXIjaxPhLnsdb%2BJXmEZJ%2FvwuYd4L5cd5wceozhREr1%2FxSLwwf7LGHhgGCzuXvNX8A%2BAXuC35lYwztgK0y4geKvwQEJngPO3Cb5hiH3K8yDfGI%2Bn9wZdtLE7NJiSmPPYB2yOiBY4FvFFVnqy%2B8A%2FPOVt2KwwwCi%2FgCw0fTfXvd7JYqVq2HEQho6XKcALdLEvAGttUXzXGQ73nRBGqKhjgdl0Ig&X-Amz-Signature=4afc4159feeca5d6d7041223cc842091b0e1bb75320b15fdf88adb5dd56ef7f5&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

