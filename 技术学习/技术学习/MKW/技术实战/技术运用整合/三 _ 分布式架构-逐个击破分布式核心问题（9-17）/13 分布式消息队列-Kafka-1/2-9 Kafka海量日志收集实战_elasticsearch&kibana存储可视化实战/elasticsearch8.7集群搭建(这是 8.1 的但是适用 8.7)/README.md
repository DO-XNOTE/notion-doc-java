---
title: elasticsearch8.7集群搭建(这是 8.1 的但是适用 8.7)
---

# elasticsearch8.7集群搭建(这是 8.1 的但是适用 8.7)

**ElasticSearch之ES8新特性及集群安装**

```java
文章目录
1. Elasticsearch8 新特性
2. Elasticsearch8安装及使用
2.1 JDK说明
2.2 安装软件
2.2.1 集群规划
2.2.2 安装步骤
2.2.2.1 上传压缩包
2.2.2.2 解压安装包
2.2.2.3 创建Linux新用户/数据文件/证书目录
2.2.2.4 设置通信秘钥
2.2.2.5 生成HTTP证书
2.2.2.6 调整证书位置
2.2.2.7 修改配置文件
2.2.2.8 启动ES
2.2.2.9 访问服务器节点
2.2.2.10 修改其他节点配置
2.2.2.11 依次启动服务节点
2.2.3 问题解决
2.2.3.1 JDK问题
2.2.3.2 SSL认证问题
2.2.3.3 闪退问题
2.2.3.4 忘记密码
2022年2月11日，Elasticsearch 发布了全新的8.0正式版本，新版本中通过改进Elasticsearch的矢量搜索功能、
对现代自然语言处理模型（NLP）的原生支持、不断简化的数据上线过程，以及精简的安全防护体验，在速度、
扩展幅度、相关性和简便性方面迎来了一个全新的时代。

1. Elasticsearch8 新特性
从2019年4月Elasticsearch7.0版本的发布，到2022年2月Elasticsearch8.0版本发布，基于不断优化开发设计理念，Elasticsearch 发布了一系列的小版本。这些小版本在以下方面取得了长足的进步并同时引入一些全新的功能：

减少内存堆使用，完全支持 ARM 架构，引入全新的方式以使用更少的存储空间，从而让每个节点托管更多的数据
降低查询开销，在大规模部署中成效尤为明显
提高日期直方图和搜索聚合的速度，增强了页面缓存的性能，并创建了一个新的pre-filter搜索短语
在 Elasticsearch7.3 和 Elasticsearch7.4 版中，引入了对矢量相似函数的支持
在最新发布的Elasticsearch8.0版本中，也同样增加和完善了很多新的功能

增加对自然语言处理 (NLP) 模型的原生支持，让矢量搜索功能更容易实现，让客户和员工能够使用他们自己的文字和语言来搜索并收到高度相关的结果
直接在Elasticsearch中执行命名实体识别、情感分析、文本分类等，而无需使用额外 的组件或进行编码
Elasticsearch8.0基于Lucene 9.0开发的，那些利用现代NLP的搜索体验，都可以借 助（新增的）对近似最近邻搜索的原生支持，快速且大规模地实现。通过ANN，可以快速并高效地将基于矢量的查询与基于矢量的文档语料库（无论是小语料库、大语料库 还是巨型语料库）进行比较
可以直接在Elasticsearch中使用 PyTorch Machine Learning 模型（如 BERT），并在Elasticsearch 中原生使用这些模型执行推理


2. Elasticsearch8安装及使用
2.1 JDK说明
Elasticsearch8最新版本依赖Java JDK17，所以在安装 ES 软件前，需要下载使用 Java JDK17，但不使用也没关系

Elasticsearch 官方地址：https://www.elastic.co/cn/

Elasticsearch下载地址：https://www.elastic.co/cn/downloads/past-releases#elasticsearch

对于Java开发人员，更熟悉的开发版本应该是 JDK1.8，突然需要升级到 JDK17，其实本身会感觉有点不适应，甚至会有点排斥，担心升级后会对现有的程序代码造成影响。

其实，对于JDK1.8，最新版本的 JDK17 增加了很多的语法特性。对于大多数项目而言，想要利用这些新的特性，是需要修改代码的，但性能除外。

也就是说，升级 JDK 版本，现有代码即使不进行修改，也不会出现兼容问题，但性能会得到极大的提升，并且高吞吐量垃圾回收器比低延迟垃圾回收器更快，更重要的是它可以免费商用。

对于升级版本而言，如果你依然有顾虑，一个好的消息就是可以下载含有适配 JDK的 ES 版本，上面提到的内容基本上就不用考虑。

2.2 安装软件
安装Elasticsearch采用Linux集群配置，准备三台Linux虚拟机，用于安装 Elasticsearch8 集群。

2.2.1 集群规划
启动集群后，每台虚拟机的进程如下：
主机名	linux1	linux2	linux2
进程名	es-node-1	es-node-2	es-node-3

给三台虚拟机搭建Elasticsearch集群，集群中-节点名称依次为：es-node-1，es-node-2，es-node-3

2.2.2 安装步骤
2.2.2.1 上传压缩包
将压缩包elasticsearch-8.1.0-linux-x86_64.tar.gz上传到虚拟机中

2.2.2.2 解压安装包
解压缩文件到自定义路径，本人解压路径为：/opt/module，解压后，软件路径为：/opt/module/elasticsearch-8.1.0
# 切换目录 
cd software 
# 解压缩 
tar -zxvf elasticsearch-8.1.0-linux-x86_64.tar.gz -C /opt/module

解压后的Elasticsearch的目录结构如下:
```

[image](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/ab41668b-5c68-4504-aa1c-52b79fa4199e/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466S7L4F2TO%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T225331Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCICilfZlTmpohzhJxTrVNDlryRcovLtySdOdmFjUEj9BvAiAb4UJiLXEQPbFUK2tgJUlLHJumB8Lbc2BMaggsHstaqCqIBAjI%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMr337Y7St8Cuwm7wbKtwD6WCv3LP6sD0RG%2B5PChSAD9Vl9NSgPUERzWPhafYCZtIL%2BVBPsrBOGKOy3lSwGGCTZYrE0P2cMgQRtYSJHXdUo6NTd%2BBkg1sM%2Fw4YNzqhjGGHJ5o1LTyyXQfg8Bnh4HaZHTB4eZejlIjGl1H7eCAUdZjaRp0TCoD%2Fpf%2BOz3Abz6WwK1GlZM8C%2F3yMR5f0w0xdZ6F%2BaalVABVMyNT%2FKXwEoy%2BgXl2nHQWpc2woUU4GGhBJAjxOJk%2BTvS7lvfCiUM1Sn3kHCQRt2W2PoHpx07Ful7FIdpikGnrZyIeZlzaXoIZ7lEYA1yYn5JzOGqdlZ%2FQCCHVsOjofpbXF1cCJGpL1sEdewjvqw9U3a4WBxGlhfwfB0spGiCk1%2FZpwgClWdUXovO306pDQZlMVVTe8ffacVXcpJZO%2FNtjOJglmQBeVe75Y%2BllzdCocc6weyvBMzI0SOiXxTtiR3dSzykI5gMxMCoC3B%2BVW1VIysc5yASJBxK2LjN3ghdxYddD%2BZq%2By8bMs0IVD4tDvFp4NzwPEjTEa5%2F7ECJc9YkAwm8PwdNbSTdFmK5dVWI2WaNv0WkDRxTQMPT%2BUqtQGsFRkAD7%2FvJ9OV37jbSjBYsfBCcuDsgQ9Tp8DkRWGbdbqsHwKqKYwkvD%2F0gY6pgHCXJYr8Zx7wOpIRfer7yREkC6SqlbkyTI%2FnVxwYGPCA9DwE%2FwW%2FD%2F%2BWXC0s2ljkseVkCO3XQyYxFTLM1q4bO83vpTEo5QJ48pVVTKlWms5BPbu0qnelypsMHnrN%2BWyrLKuXbmkVt5fqqSivnwqL3yLjxUbiEhNlXziZRs38mx%2BR3GL7uvHRIws66krdkF1Brm%2BKYmqjgY0Uqqr39GemNUGyuRybvVT&X-Amz-Signature=6c2e2ed4e0fd742cfbebc804f3527bf091fac61fdcb45952f413c41350c0e09f&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

```java
目录	含义
bin	可执行脚本目录
config	配置目录
jdk	内置 JDK 目录
lib	类库
logs	日志目录
modules	模块目录
plugins	插件目录
注意：当前安装 ES 版本为 8.1.0，自带 JDK，所以当前 Linux 虚拟机节点无需配置 Java 环境

2.2.2.3 创建Linux新用户/数据文件/证书目录
创建Linux新用户es，数据文件，证书目录，并修改Elasticsearch文件拥有者
# 新增 es 用户 
useradd es 

# 为 es 用户设置密码 
passwd es 

# 创建数据文件目录 
mkdir /opt/module/elasticsearch-8.1.0/data 

# 创建证书目录 
mkdir /opt/module/elasticsearch-8.1.0/config/certs 

#切换目录 
cd /opt/module/elasticsearch-8.1.0 

# 修改文件拥有者 
chown -R es:es /opt/module/elasticsearch-8.1.0

2.2.2.4 设置通信秘钥
在第一台服务器节点 es-node-1 设置集群多节点通信密钥
# 切换用户 
su es 

# 签发 ca 证书，过程中需按两次回车键 
bin/elasticsearch-certutil ca 

# 用 ca 证书签发节点证书，过程中需按三次回车键 
bin/elasticsearch-certutil cert --ca elastic-stack-ca.p12 

# 将生成的证书文件移动到 config/certs 目录中
mv elastic-stack-ca.p12 elastic-certificates.p12 config/certs


2.2.2.5 生成HTTP证书
在第一台服务器节点 es-node-1 设置集群多节点 HTTP 证书
# 签发 Https 证书 
bin/elasticsearch-certutil http
每次要求输入时，需要输入的内容
```

[image](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/76e00809-1637-4af5-b13d-9f7ee33aa669/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466S7L4F2TO%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T225331Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCICilfZlTmpohzhJxTrVNDlryRcovLtySdOdmFjUEj9BvAiAb4UJiLXEQPbFUK2tgJUlLHJumB8Lbc2BMaggsHstaqCqIBAjI%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMr337Y7St8Cuwm7wbKtwD6WCv3LP6sD0RG%2B5PChSAD9Vl9NSgPUERzWPhafYCZtIL%2BVBPsrBOGKOy3lSwGGCTZYrE0P2cMgQRtYSJHXdUo6NTd%2BBkg1sM%2Fw4YNzqhjGGHJ5o1LTyyXQfg8Bnh4HaZHTB4eZejlIjGl1H7eCAUdZjaRp0TCoD%2Fpf%2BOz3Abz6WwK1GlZM8C%2F3yMR5f0w0xdZ6F%2BaalVABVMyNT%2FKXwEoy%2BgXl2nHQWpc2woUU4GGhBJAjxOJk%2BTvS7lvfCiUM1Sn3kHCQRt2W2PoHpx07Ful7FIdpikGnrZyIeZlzaXoIZ7lEYA1yYn5JzOGqdlZ%2FQCCHVsOjofpbXF1cCJGpL1sEdewjvqw9U3a4WBxGlhfwfB0spGiCk1%2FZpwgClWdUXovO306pDQZlMVVTe8ffacVXcpJZO%2FNtjOJglmQBeVe75Y%2BllzdCocc6weyvBMzI0SOiXxTtiR3dSzykI5gMxMCoC3B%2BVW1VIysc5yASJBxK2LjN3ghdxYddD%2BZq%2By8bMs0IVD4tDvFp4NzwPEjTEa5%2F7ECJc9YkAwm8PwdNbSTdFmK5dVWI2WaNv0WkDRxTQMPT%2BUqtQGsFRkAD7%2FvJ9OV37jbSjBYsfBCcuDsgQ9Tp8DkRWGbdbqsHwKqKYwkvD%2F0gY6pgHCXJYr8Zx7wOpIRfer7yREkC6SqlbkyTI%2FnVxwYGPCA9DwE%2FwW%2FD%2F%2BWXC0s2ljkseVkCO3XQyYxFTLM1q4bO83vpTEo5QJ48pVVTKlWms5BPbu0qnelypsMHnrN%2BWyrLKuXbmkVt5fqqSivnwqL3yLjxUbiEhNlXziZRs38mx%2BR3GL7uvHRIws66krdkF1Brm%2BKYmqjgY0Uqqr39GemNUGyuRybvVT&X-Amz-Signature=da425dd8e65b5d8eba12b34c5cb8149521ee919f06462cf41bdba3fb1ea7e54a&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

[image](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/3caa2e56-a77f-41a4-b5fb-8c4c428dc6b0/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466S7L4F2TO%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T225331Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCICilfZlTmpohzhJxTrVNDlryRcovLtySdOdmFjUEj9BvAiAb4UJiLXEQPbFUK2tgJUlLHJumB8Lbc2BMaggsHstaqCqIBAjI%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMr337Y7St8Cuwm7wbKtwD6WCv3LP6sD0RG%2B5PChSAD9Vl9NSgPUERzWPhafYCZtIL%2BVBPsrBOGKOy3lSwGGCTZYrE0P2cMgQRtYSJHXdUo6NTd%2BBkg1sM%2Fw4YNzqhjGGHJ5o1LTyyXQfg8Bnh4HaZHTB4eZejlIjGl1H7eCAUdZjaRp0TCoD%2Fpf%2BOz3Abz6WwK1GlZM8C%2F3yMR5f0w0xdZ6F%2BaalVABVMyNT%2FKXwEoy%2BgXl2nHQWpc2woUU4GGhBJAjxOJk%2BTvS7lvfCiUM1Sn3kHCQRt2W2PoHpx07Ful7FIdpikGnrZyIeZlzaXoIZ7lEYA1yYn5JzOGqdlZ%2FQCCHVsOjofpbXF1cCJGpL1sEdewjvqw9U3a4WBxGlhfwfB0spGiCk1%2FZpwgClWdUXovO306pDQZlMVVTe8ffacVXcpJZO%2FNtjOJglmQBeVe75Y%2BllzdCocc6weyvBMzI0SOiXxTtiR3dSzykI5gMxMCoC3B%2BVW1VIysc5yASJBxK2LjN3ghdxYddD%2BZq%2By8bMs0IVD4tDvFp4NzwPEjTEa5%2F7ECJc9YkAwm8PwdNbSTdFmK5dVWI2WaNv0WkDRxTQMPT%2BUqtQGsFRkAD7%2FvJ9OV37jbSjBYsfBCcuDsgQ9Tp8DkRWGbdbqsHwKqKYwkvD%2F0gY6pgHCXJYr8Zx7wOpIRfer7yREkC6SqlbkyTI%2FnVxwYGPCA9DwE%2FwW%2FD%2F%2BWXC0s2ljkseVkCO3XQyYxFTLM1q4bO83vpTEo5QJ48pVVTKlWms5BPbu0qnelypsMHnrN%2BWyrLKuXbmkVt5fqqSivnwqL3yLjxUbiEhNlXziZRs38mx%2BR3GL7uvHRIws66krdkF1Brm%2BKYmqjgY0Uqqr39GemNUGyuRybvVT&X-Amz-Signature=5d7299002440ba7ba98d83e7472e1ab638f7d41df0bed226a4f4ff1b945128b3&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

```java
指定证书路径
```

[image](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/22b65f51-8625-458a-8ef9-7448a74d5600/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466S7L4F2TO%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T225331Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCICilfZlTmpohzhJxTrVNDlryRcovLtySdOdmFjUEj9BvAiAb4UJiLXEQPbFUK2tgJUlLHJumB8Lbc2BMaggsHstaqCqIBAjI%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMr337Y7St8Cuwm7wbKtwD6WCv3LP6sD0RG%2B5PChSAD9Vl9NSgPUERzWPhafYCZtIL%2BVBPsrBOGKOy3lSwGGCTZYrE0P2cMgQRtYSJHXdUo6NTd%2BBkg1sM%2Fw4YNzqhjGGHJ5o1LTyyXQfg8Bnh4HaZHTB4eZejlIjGl1H7eCAUdZjaRp0TCoD%2Fpf%2BOz3Abz6WwK1GlZM8C%2F3yMR5f0w0xdZ6F%2BaalVABVMyNT%2FKXwEoy%2BgXl2nHQWpc2woUU4GGhBJAjxOJk%2BTvS7lvfCiUM1Sn3kHCQRt2W2PoHpx07Ful7FIdpikGnrZyIeZlzaXoIZ7lEYA1yYn5JzOGqdlZ%2FQCCHVsOjofpbXF1cCJGpL1sEdewjvqw9U3a4WBxGlhfwfB0spGiCk1%2FZpwgClWdUXovO306pDQZlMVVTe8ffacVXcpJZO%2FNtjOJglmQBeVe75Y%2BllzdCocc6weyvBMzI0SOiXxTtiR3dSzykI5gMxMCoC3B%2BVW1VIysc5yASJBxK2LjN3ghdxYddD%2BZq%2By8bMs0IVD4tDvFp4NzwPEjTEa5%2F7ECJc9YkAwm8PwdNbSTdFmK5dVWI2WaNv0WkDRxTQMPT%2BUqtQGsFRkAD7%2FvJ9OV37jbSjBYsfBCcuDsgQ9Tp8DkRWGbdbqsHwKqKYwkvD%2F0gY6pgHCXJYr8Zx7wOpIRfer7yREkC6SqlbkyTI%2FnVxwYGPCA9DwE%2FwW%2FD%2F%2BWXC0s2ljkseVkCO3XQyYxFTLM1q4bO83vpTEo5QJ48pVVTKlWms5BPbu0qnelypsMHnrN%2BWyrLKuXbmkVt5fqqSivnwqL3yLjxUbiEhNlXziZRs38mx%2BR3GL7uvHRIws66krdkF1Brm%2BKYmqjgY0Uqqr39GemNUGyuRybvVT&X-Amz-Signature=fa1ba6e149af2b2803f5a4d64197c8b2972821420d7117977158e83f10c23ccd&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

• 无需输入密码

[image](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/ffcfb0a3-a91e-4a25-af63-bc8d355c3fc6/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466S7L4F2TO%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T225331Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCICilfZlTmpohzhJxTrVNDlryRcovLtySdOdmFjUEj9BvAiAb4UJiLXEQPbFUK2tgJUlLHJumB8Lbc2BMaggsHstaqCqIBAjI%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMr337Y7St8Cuwm7wbKtwD6WCv3LP6sD0RG%2B5PChSAD9Vl9NSgPUERzWPhafYCZtIL%2BVBPsrBOGKOy3lSwGGCTZYrE0P2cMgQRtYSJHXdUo6NTd%2BBkg1sM%2Fw4YNzqhjGGHJ5o1LTyyXQfg8Bnh4HaZHTB4eZejlIjGl1H7eCAUdZjaRp0TCoD%2Fpf%2BOz3Abz6WwK1GlZM8C%2F3yMR5f0w0xdZ6F%2BaalVABVMyNT%2FKXwEoy%2BgXl2nHQWpc2woUU4GGhBJAjxOJk%2BTvS7lvfCiUM1Sn3kHCQRt2W2PoHpx07Ful7FIdpikGnrZyIeZlzaXoIZ7lEYA1yYn5JzOGqdlZ%2FQCCHVsOjofpbXF1cCJGpL1sEdewjvqw9U3a4WBxGlhfwfB0spGiCk1%2FZpwgClWdUXovO306pDQZlMVVTe8ffacVXcpJZO%2FNtjOJglmQBeVe75Y%2BllzdCocc6weyvBMzI0SOiXxTtiR3dSzykI5gMxMCoC3B%2BVW1VIysc5yASJBxK2LjN3ghdxYddD%2BZq%2By8bMs0IVD4tDvFp4NzwPEjTEa5%2F7ECJc9YkAwm8PwdNbSTdFmK5dVWI2WaNv0WkDRxTQMPT%2BUqtQGsFRkAD7%2FvJ9OV37jbSjBYsfBCcuDsgQ9Tp8DkRWGbdbqsHwKqKYwkvD%2F0gY6pgHCXJYr8Zx7wOpIRfer7yREkC6SqlbkyTI%2FnVxwYGPCA9DwE%2FwW%2FD%2F%2BWXC0s2ljkseVkCO3XQyYxFTLM1q4bO83vpTEo5QJ48pVVTKlWms5BPbu0qnelypsMHnrN%2BWyrLKuXbmkVt5fqqSivnwqL3yLjxUbiEhNlXziZRs38mx%2BR3GL7uvHRIws66krdkF1Brm%2BKYmqjgY0Uqqr39GemNUGyuRybvVT&X-Amz-Signature=6256f4ad2752db8083e54a5d00f837b51e031c2647d8dd3b3e91f94f8bd1b51f&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

• 设置证书失效时间

[image](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/04c191f5-c387-482d-b8d4-84ae45f9c83c/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466S7L4F2TO%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T225331Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCICilfZlTmpohzhJxTrVNDlryRcovLtySdOdmFjUEj9BvAiAb4UJiLXEQPbFUK2tgJUlLHJumB8Lbc2BMaggsHstaqCqIBAjI%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMr337Y7St8Cuwm7wbKtwD6WCv3LP6sD0RG%2B5PChSAD9Vl9NSgPUERzWPhafYCZtIL%2BVBPsrBOGKOy3lSwGGCTZYrE0P2cMgQRtYSJHXdUo6NTd%2BBkg1sM%2Fw4YNzqhjGGHJ5o1LTyyXQfg8Bnh4HaZHTB4eZejlIjGl1H7eCAUdZjaRp0TCoD%2Fpf%2BOz3Abz6WwK1GlZM8C%2F3yMR5f0w0xdZ6F%2BaalVABVMyNT%2FKXwEoy%2BgXl2nHQWpc2woUU4GGhBJAjxOJk%2BTvS7lvfCiUM1Sn3kHCQRt2W2PoHpx07Ful7FIdpikGnrZyIeZlzaXoIZ7lEYA1yYn5JzOGqdlZ%2FQCCHVsOjofpbXF1cCJGpL1sEdewjvqw9U3a4WBxGlhfwfB0spGiCk1%2FZpwgClWdUXovO306pDQZlMVVTe8ffacVXcpJZO%2FNtjOJglmQBeVe75Y%2BllzdCocc6weyvBMzI0SOiXxTtiR3dSzykI5gMxMCoC3B%2BVW1VIysc5yASJBxK2LjN3ghdxYddD%2BZq%2By8bMs0IVD4tDvFp4NzwPEjTEa5%2F7ECJc9YkAwm8PwdNbSTdFmK5dVWI2WaNv0WkDRxTQMPT%2BUqtQGsFRkAD7%2FvJ9OV37jbSjBYsfBCcuDsgQ9Tp8DkRWGbdbqsHwKqKYwkvD%2F0gY6pgHCXJYr8Zx7wOpIRfer7yREkC6SqlbkyTI%2FnVxwYGPCA9DwE%2FwW%2FD%2F%2BWXC0s2ljkseVkCO3XQyYxFTLM1q4bO83vpTEo5QJ48pVVTKlWms5BPbu0qnelypsMHnrN%2BWyrLKuXbmkVt5fqqSivnwqL3yLjxUbiEhNlXziZRs38mx%2BR3GL7uvHRIws66krdkF1Brm%2BKYmqjgY0Uqqr39GemNUGyuRybvVT&X-Amz-Signature=626452e586a697188500e0a0106109ee07c95ecea994760531c89821cfdefc84&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

• 无需每个节点配置证书

[image](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/cdde54a1-d5c9-4107-a0f3-54fffa011689/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466S7L4F2TO%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T225331Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCICilfZlTmpohzhJxTrVNDlryRcovLtySdOdmFjUEj9BvAiAb4UJiLXEQPbFUK2tgJUlLHJumB8Lbc2BMaggsHstaqCqIBAjI%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMr337Y7St8Cuwm7wbKtwD6WCv3LP6sD0RG%2B5PChSAD9Vl9NSgPUERzWPhafYCZtIL%2BVBPsrBOGKOy3lSwGGCTZYrE0P2cMgQRtYSJHXdUo6NTd%2BBkg1sM%2Fw4YNzqhjGGHJ5o1LTyyXQfg8Bnh4HaZHTB4eZejlIjGl1H7eCAUdZjaRp0TCoD%2Fpf%2BOz3Abz6WwK1GlZM8C%2F3yMR5f0w0xdZ6F%2BaalVABVMyNT%2FKXwEoy%2BgXl2nHQWpc2woUU4GGhBJAjxOJk%2BTvS7lvfCiUM1Sn3kHCQRt2W2PoHpx07Ful7FIdpikGnrZyIeZlzaXoIZ7lEYA1yYn5JzOGqdlZ%2FQCCHVsOjofpbXF1cCJGpL1sEdewjvqw9U3a4WBxGlhfwfB0spGiCk1%2FZpwgClWdUXovO306pDQZlMVVTe8ffacVXcpJZO%2FNtjOJglmQBeVe75Y%2BllzdCocc6weyvBMzI0SOiXxTtiR3dSzykI5gMxMCoC3B%2BVW1VIysc5yASJBxK2LjN3ghdxYddD%2BZq%2By8bMs0IVD4tDvFp4NzwPEjTEa5%2F7ECJc9YkAwm8PwdNbSTdFmK5dVWI2WaNv0WkDRxTQMPT%2BUqtQGsFRkAD7%2FvJ9OV37jbSjBYsfBCcuDsgQ9Tp8DkRWGbdbqsHwKqKYwkvD%2F0gY6pgHCXJYr8Zx7wOpIRfer7yREkC6SqlbkyTI%2FnVxwYGPCA9DwE%2FwW%2FD%2F%2BWXC0s2ljkseVkCO3XQyYxFTLM1q4bO83vpTEo5QJ48pVVTKlWms5BPbu0qnelypsMHnrN%2BWyrLKuXbmkVt5fqqSivnwqL3yLjxUbiEhNlXziZRs38mx%2BR3GL7uvHRIws66krdkF1Brm%2BKYmqjgY0Uqqr39GemNUGyuRybvVT&X-Amz-Signature=7430ff6aade981b8bcc1f6a8d74234a4f4a8e23bf85417feec220e0854e32241&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

• 输出连接到第一个节点的所有主机名称

[image](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/b88d8573-772d-4fdb-b991-bc546e317562/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466S7L4F2TO%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T225331Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCICilfZlTmpohzhJxTrVNDlryRcovLtySdOdmFjUEj9BvAiAb4UJiLXEQPbFUK2tgJUlLHJumB8Lbc2BMaggsHstaqCqIBAjI%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMr337Y7St8Cuwm7wbKtwD6WCv3LP6sD0RG%2B5PChSAD9Vl9NSgPUERzWPhafYCZtIL%2BVBPsrBOGKOy3lSwGGCTZYrE0P2cMgQRtYSJHXdUo6NTd%2BBkg1sM%2Fw4YNzqhjGGHJ5o1LTyyXQfg8Bnh4HaZHTB4eZejlIjGl1H7eCAUdZjaRp0TCoD%2Fpf%2BOz3Abz6WwK1GlZM8C%2F3yMR5f0w0xdZ6F%2BaalVABVMyNT%2FKXwEoy%2BgXl2nHQWpc2woUU4GGhBJAjxOJk%2BTvS7lvfCiUM1Sn3kHCQRt2W2PoHpx07Ful7FIdpikGnrZyIeZlzaXoIZ7lEYA1yYn5JzOGqdlZ%2FQCCHVsOjofpbXF1cCJGpL1sEdewjvqw9U3a4WBxGlhfwfB0spGiCk1%2FZpwgClWdUXovO306pDQZlMVVTe8ffacVXcpJZO%2FNtjOJglmQBeVe75Y%2BllzdCocc6weyvBMzI0SOiXxTtiR3dSzykI5gMxMCoC3B%2BVW1VIysc5yASJBxK2LjN3ghdxYddD%2BZq%2By8bMs0IVD4tDvFp4NzwPEjTEa5%2F7ECJc9YkAwm8PwdNbSTdFmK5dVWI2WaNv0WkDRxTQMPT%2BUqtQGsFRkAD7%2FvJ9OV37jbSjBYsfBCcuDsgQ9Tp8DkRWGbdbqsHwKqKYwkvD%2F0gY6pgHCXJYr8Zx7wOpIRfer7yREkC6SqlbkyTI%2FnVxwYGPCA9DwE%2FwW%2FD%2F%2BWXC0s2ljkseVkCO3XQyYxFTLM1q4bO83vpTEo5QJ48pVVTKlWms5BPbu0qnelypsMHnrN%2BWyrLKuXbmkVt5fqqSivnwqL3yLjxUbiEhNlXziZRs38mx%2BR3GL7uvHRIws66krdkF1Brm%2BKYmqjgY0Uqqr39GemNUGyuRybvVT&X-Amz-Signature=ece38f327e54ef5beb3a33b2bb817e07ea7523031f5dd21f4fcc190c0959803d&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

• 输出连接到第一个节点的所有主机 `IP `地址

[image](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/851963e8-0aa8-496e-ae18-1482dcf7a616/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466S7L4F2TO%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T225331Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCICilfZlTmpohzhJxTrVNDlryRcovLtySdOdmFjUEj9BvAiAb4UJiLXEQPbFUK2tgJUlLHJumB8Lbc2BMaggsHstaqCqIBAjI%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMr337Y7St8Cuwm7wbKtwD6WCv3LP6sD0RG%2B5PChSAD9Vl9NSgPUERzWPhafYCZtIL%2BVBPsrBOGKOy3lSwGGCTZYrE0P2cMgQRtYSJHXdUo6NTd%2BBkg1sM%2Fw4YNzqhjGGHJ5o1LTyyXQfg8Bnh4HaZHTB4eZejlIjGl1H7eCAUdZjaRp0TCoD%2Fpf%2BOz3Abz6WwK1GlZM8C%2F3yMR5f0w0xdZ6F%2BaalVABVMyNT%2FKXwEoy%2BgXl2nHQWpc2woUU4GGhBJAjxOJk%2BTvS7lvfCiUM1Sn3kHCQRt2W2PoHpx07Ful7FIdpikGnrZyIeZlzaXoIZ7lEYA1yYn5JzOGqdlZ%2FQCCHVsOjofpbXF1cCJGpL1sEdewjvqw9U3a4WBxGlhfwfB0spGiCk1%2FZpwgClWdUXovO306pDQZlMVVTe8ffacVXcpJZO%2FNtjOJglmQBeVe75Y%2BllzdCocc6weyvBMzI0SOiXxTtiR3dSzykI5gMxMCoC3B%2BVW1VIysc5yASJBxK2LjN3ghdxYddD%2BZq%2By8bMs0IVD4tDvFp4NzwPEjTEa5%2F7ECJc9YkAwm8PwdNbSTdFmK5dVWI2WaNv0WkDRxTQMPT%2BUqtQGsFRkAD7%2FvJ9OV37jbSjBYsfBCcuDsgQ9Tp8DkRWGbdbqsHwKqKYwkvD%2F0gY6pgHCXJYr8Zx7wOpIRfer7yREkC6SqlbkyTI%2FnVxwYGPCA9DwE%2FwW%2FD%2F%2BWXC0s2ljkseVkCO3XQyYxFTLM1q4bO83vpTEo5QJ48pVVTKlWms5BPbu0qnelypsMHnrN%2BWyrLKuXbmkVt5fqqSivnwqL3yLjxUbiEhNlXziZRs38mx%2BR3GL7uvHRIws66krdkF1Brm%2BKYmqjgY0Uqqr39GemNUGyuRybvVT&X-Amz-Signature=c6a7bbe072aabe50412804be8401a0846e218bff1dd9395f6d461fd86e8f7452&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

• 不改变证书选项配置

[image](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/789bf0ee-8f47-48fa-9e78-2680625c6075/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466S7L4F2TO%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T225331Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCICilfZlTmpohzhJxTrVNDlryRcovLtySdOdmFjUEj9BvAiAb4UJiLXEQPbFUK2tgJUlLHJumB8Lbc2BMaggsHstaqCqIBAjI%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMr337Y7St8Cuwm7wbKtwD6WCv3LP6sD0RG%2B5PChSAD9Vl9NSgPUERzWPhafYCZtIL%2BVBPsrBOGKOy3lSwGGCTZYrE0P2cMgQRtYSJHXdUo6NTd%2BBkg1sM%2Fw4YNzqhjGGHJ5o1LTyyXQfg8Bnh4HaZHTB4eZejlIjGl1H7eCAUdZjaRp0TCoD%2Fpf%2BOz3Abz6WwK1GlZM8C%2F3yMR5f0w0xdZ6F%2BaalVABVMyNT%2FKXwEoy%2BgXl2nHQWpc2woUU4GGhBJAjxOJk%2BTvS7lvfCiUM1Sn3kHCQRt2W2PoHpx07Ful7FIdpikGnrZyIeZlzaXoIZ7lEYA1yYn5JzOGqdlZ%2FQCCHVsOjofpbXF1cCJGpL1sEdewjvqw9U3a4WBxGlhfwfB0spGiCk1%2FZpwgClWdUXovO306pDQZlMVVTe8ffacVXcpJZO%2FNtjOJglmQBeVe75Y%2BllzdCocc6weyvBMzI0SOiXxTtiR3dSzykI5gMxMCoC3B%2BVW1VIysc5yASJBxK2LjN3ghdxYddD%2BZq%2By8bMs0IVD4tDvFp4NzwPEjTEa5%2F7ECJc9YkAwm8PwdNbSTdFmK5dVWI2WaNv0WkDRxTQMPT%2BUqtQGsFRkAD7%2FvJ9OV37jbSjBYsfBCcuDsgQ9Tp8DkRWGbdbqsHwKqKYwkvD%2F0gY6pgHCXJYr8Zx7wOpIRfer7yREkC6SqlbkyTI%2FnVxwYGPCA9DwE%2FwW%2FD%2F%2BWXC0s2ljkseVkCO3XQyYxFTLM1q4bO83vpTEo5QJ48pVVTKlWms5BPbu0qnelypsMHnrN%2BWyrLKuXbmkVt5fqqSivnwqL3yLjxUbiEhNlXziZRs38mx%2BR3GL7uvHRIws66krdkF1Brm%2BKYmqjgY0Uqqr39GemNUGyuRybvVT&X-Amz-Signature=2884ae05bcfb7ba806e7c053b87f9cf1681e66740441a05090dbda856459e24b&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

• 不给证书加密，按键输入两次回车

[image](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/de5509c2-bce8-4857-8c91-a47f90caae79/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466S7L4F2TO%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T225331Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCICilfZlTmpohzhJxTrVNDlryRcovLtySdOdmFjUEj9BvAiAb4UJiLXEQPbFUK2tgJUlLHJumB8Lbc2BMaggsHstaqCqIBAjI%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMr337Y7St8Cuwm7wbKtwD6WCv3LP6sD0RG%2B5PChSAD9Vl9NSgPUERzWPhafYCZtIL%2BVBPsrBOGKOy3lSwGGCTZYrE0P2cMgQRtYSJHXdUo6NTd%2BBkg1sM%2Fw4YNzqhjGGHJ5o1LTyyXQfg8Bnh4HaZHTB4eZejlIjGl1H7eCAUdZjaRp0TCoD%2Fpf%2BOz3Abz6WwK1GlZM8C%2F3yMR5f0w0xdZ6F%2BaalVABVMyNT%2FKXwEoy%2BgXl2nHQWpc2woUU4GGhBJAjxOJk%2BTvS7lvfCiUM1Sn3kHCQRt2W2PoHpx07Ful7FIdpikGnrZyIeZlzaXoIZ7lEYA1yYn5JzOGqdlZ%2FQCCHVsOjofpbXF1cCJGpL1sEdewjvqw9U3a4WBxGlhfwfB0spGiCk1%2FZpwgClWdUXovO306pDQZlMVVTe8ffacVXcpJZO%2FNtjOJglmQBeVe75Y%2BllzdCocc6weyvBMzI0SOiXxTtiR3dSzykI5gMxMCoC3B%2BVW1VIysc5yASJBxK2LjN3ghdxYddD%2BZq%2By8bMs0IVD4tDvFp4NzwPEjTEa5%2F7ECJc9YkAwm8PwdNbSTdFmK5dVWI2WaNv0WkDRxTQMPT%2BUqtQGsFRkAD7%2FvJ9OV37jbSjBYsfBCcuDsgQ9Tp8DkRWGbdbqsHwKqKYwkvD%2F0gY6pgHCXJYr8Zx7wOpIRfer7yREkC6SqlbkyTI%2FnVxwYGPCA9DwE%2FwW%2FD%2F%2BWXC0s2ljkseVkCO3XQyYxFTLM1q4bO83vpTEo5QJ48pVVTKlWms5BPbu0qnelypsMHnrN%2BWyrLKuXbmkVt5fqqSivnwqL3yLjxUbiEhNlXziZRs38mx%2BR3GL7uvHRIws66krdkF1Brm%2BKYmqjgY0Uqqr39GemNUGyuRybvVT&X-Amz-Signature=637af26d6fbb70f1f88bcf260b84aef40ea2a077aef118cd12e82fee438e69b4&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

```java
2.2.2.6 调整证书位置
解压刚生成的zip 包

# 解压文件 
unzip elasticsearch-ssl-http.zip 

# 移动文件 将解压后的证书文件移动到 config/certs 目录中 
mv elasticsearch/http.p12 kibana/elasticsearch-ca.pem config/certs


2.2.2.7 修改配置文件
修改主配置文件：config/elasticsearch.yml


# 设置 ES 集群名称 
cluster.name: es-cluster  

# 设置集群中当前节点名称 
node.name: es-node-1 

# 设置数据，日志文件路径 
path.data: /opt/module/elasticsearch-8.1.0/data 
path.logs: /opt/module/elasticsearch-8.1.0/log 

# 设置网络访问节点 
network.host: 0.0.0.0 

# 设置网络访问端口 
http.port: 9200 


# 安全认证 
xpack.security.enabled: true 
xpack.security.enrollment.enabled: true 
xpack.security.http.ssl: 
 enabled: true 
 keystore.path: /opt/module/elasticsearch-8.1.0/config/certs/http.p12 
 truststore.path: /opt/module/elasticsearch-8.1.0/config/certs/http.p12 
xpack.security.transport.ssl: 
 enabled: true 
 verification_mode: certificate 
 keystore.path: /opt/module/elasticsearch-8.1.0/config/certs/elastic-certificates.p12 
 truststore.path: /opt/module/elasticsearch-8.1.0/config/certs/elastic-certificates.p12 

# 此处需注意，es-node-1 为上面配置的节点名称 
cluster.initial_master_nodes: ["es-node-1"] 

ingest.geoip.downloader.enabled: false 
xpack.security.http.ssl.client_authentication: none

2.2.2.8 启动ES
# 启动 ES 软件 
bin/elasticsearch
第一次成功启动后，会显示密码，请记住，访问时需要。只有第一次才有！！！

```

[image](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/e0ff4f43-ba00-47d0-a927-c3d2542dd461/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466S7L4F2TO%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T225331Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCICilfZlTmpohzhJxTrVNDlryRcovLtySdOdmFjUEj9BvAiAb4UJiLXEQPbFUK2tgJUlLHJumB8Lbc2BMaggsHstaqCqIBAjI%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMr337Y7St8Cuwm7wbKtwD6WCv3LP6sD0RG%2B5PChSAD9Vl9NSgPUERzWPhafYCZtIL%2BVBPsrBOGKOy3lSwGGCTZYrE0P2cMgQRtYSJHXdUo6NTd%2BBkg1sM%2Fw4YNzqhjGGHJ5o1LTyyXQfg8Bnh4HaZHTB4eZejlIjGl1H7eCAUdZjaRp0TCoD%2Fpf%2BOz3Abz6WwK1GlZM8C%2F3yMR5f0w0xdZ6F%2BaalVABVMyNT%2FKXwEoy%2BgXl2nHQWpc2woUU4GGhBJAjxOJk%2BTvS7lvfCiUM1Sn3kHCQRt2W2PoHpx07Ful7FIdpikGnrZyIeZlzaXoIZ7lEYA1yYn5JzOGqdlZ%2FQCCHVsOjofpbXF1cCJGpL1sEdewjvqw9U3a4WBxGlhfwfB0spGiCk1%2FZpwgClWdUXovO306pDQZlMVVTe8ffacVXcpJZO%2FNtjOJglmQBeVe75Y%2BllzdCocc6weyvBMzI0SOiXxTtiR3dSzykI5gMxMCoC3B%2BVW1VIysc5yASJBxK2LjN3ghdxYddD%2BZq%2By8bMs0IVD4tDvFp4NzwPEjTEa5%2F7ECJc9YkAwm8PwdNbSTdFmK5dVWI2WaNv0WkDRxTQMPT%2BUqtQGsFRkAD7%2FvJ9OV37jbSjBYsfBCcuDsgQ9Tp8DkRWGbdbqsHwKqKYwkvD%2F0gY6pgHCXJYr8Zx7wOpIRfer7yREkC6SqlbkyTI%2FnVxwYGPCA9DwE%2FwW%2FD%2F%2BWXC0s2ljkseVkCO3XQyYxFTLM1q4bO83vpTEo5QJ48pVVTKlWms5BPbu0qnelypsMHnrN%2BWyrLKuXbmkVt5fqqSivnwqL3yLjxUbiEhNlXziZRs38mx%2BR3GL7uvHRIws66krdkF1Brm%2BKYmqjgY0Uqqr39GemNUGyuRybvVT&X-Amz-Signature=49060d6872d3dfefaf2eab3702c6f2b28d3841053b2875a3e5f08c623ffe1690&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

```java
注意：

 9300 端口为 Elasticsearch 集群间组件的通信端口

 9200 端口为浏览器访问的http协议RESTful端口
```

### **2.2.2.9 访问服务器节点**

访问服务器节点：`https://虚拟机地址:9200 `。因为配置了安全协议，所以使用 `https `协议进行访问，但由于证书是自己生成的，并不可靠，所以会有安全提示，选择继续即可

[image](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/06234528-fa84-4502-980a-0f615becda94/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466S7L4F2TO%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T225331Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCICilfZlTmpohzhJxTrVNDlryRcovLtySdOdmFjUEj9BvAiAb4UJiLXEQPbFUK2tgJUlLHJumB8Lbc2BMaggsHstaqCqIBAjI%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMr337Y7St8Cuwm7wbKtwD6WCv3LP6sD0RG%2B5PChSAD9Vl9NSgPUERzWPhafYCZtIL%2BVBPsrBOGKOy3lSwGGCTZYrE0P2cMgQRtYSJHXdUo6NTd%2BBkg1sM%2Fw4YNzqhjGGHJ5o1LTyyXQfg8Bnh4HaZHTB4eZejlIjGl1H7eCAUdZjaRp0TCoD%2Fpf%2BOz3Abz6WwK1GlZM8C%2F3yMR5f0w0xdZ6F%2BaalVABVMyNT%2FKXwEoy%2BgXl2nHQWpc2woUU4GGhBJAjxOJk%2BTvS7lvfCiUM1Sn3kHCQRt2W2PoHpx07Ful7FIdpikGnrZyIeZlzaXoIZ7lEYA1yYn5JzOGqdlZ%2FQCCHVsOjofpbXF1cCJGpL1sEdewjvqw9U3a4WBxGlhfwfB0spGiCk1%2FZpwgClWdUXovO306pDQZlMVVTe8ffacVXcpJZO%2FNtjOJglmQBeVe75Y%2BllzdCocc6weyvBMzI0SOiXxTtiR3dSzykI5gMxMCoC3B%2BVW1VIysc5yASJBxK2LjN3ghdxYddD%2BZq%2By8bMs0IVD4tDvFp4NzwPEjTEa5%2F7ECJc9YkAwm8PwdNbSTdFmK5dVWI2WaNv0WkDRxTQMPT%2BUqtQGsFRkAD7%2FvJ9OV37jbSjBYsfBCcuDsgQ9Tp8DkRWGbdbqsHwKqKYwkvD%2F0gY6pgHCXJYr8Zx7wOpIRfer7yREkC6SqlbkyTI%2FnVxwYGPCA9DwE%2FwW%2FD%2F%2BWXC0s2ljkseVkCO3XQyYxFTLM1q4bO83vpTEo5QJ48pVVTKlWms5BPbu0qnelypsMHnrN%2BWyrLKuXbmkVt5fqqSivnwqL3yLjxUbiEhNlXziZRs38mx%2BR3GL7uvHRIws66krdkF1Brm%2BKYmqjgY0Uqqr39GemNUGyuRybvVT&X-Amz-Signature=b1ee575d100cb87f12a9f94dd50b712ca6d37bc5b7cf4e1a79f83325d4b4ccac&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

输入账号，密码登录，即可看到页面会有如下信息

[image](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/74dfc187-e451-4995-a19f-edaf305c36b8/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466S7L4F2TO%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T225331Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCICilfZlTmpohzhJxTrVNDlryRcovLtySdOdmFjUEj9BvAiAb4UJiLXEQPbFUK2tgJUlLHJumB8Lbc2BMaggsHstaqCqIBAjI%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMr337Y7St8Cuwm7wbKtwD6WCv3LP6sD0RG%2B5PChSAD9Vl9NSgPUERzWPhafYCZtIL%2BVBPsrBOGKOy3lSwGGCTZYrE0P2cMgQRtYSJHXdUo6NTd%2BBkg1sM%2Fw4YNzqhjGGHJ5o1LTyyXQfg8Bnh4HaZHTB4eZejlIjGl1H7eCAUdZjaRp0TCoD%2Fpf%2BOz3Abz6WwK1GlZM8C%2F3yMR5f0w0xdZ6F%2BaalVABVMyNT%2FKXwEoy%2BgXl2nHQWpc2woUU4GGhBJAjxOJk%2BTvS7lvfCiUM1Sn3kHCQRt2W2PoHpx07Ful7FIdpikGnrZyIeZlzaXoIZ7lEYA1yYn5JzOGqdlZ%2FQCCHVsOjofpbXF1cCJGpL1sEdewjvqw9U3a4WBxGlhfwfB0spGiCk1%2FZpwgClWdUXovO306pDQZlMVVTe8ffacVXcpJZO%2FNtjOJglmQBeVe75Y%2BllzdCocc6weyvBMzI0SOiXxTtiR3dSzykI5gMxMCoC3B%2BVW1VIysc5yASJBxK2LjN3ghdxYddD%2BZq%2By8bMs0IVD4tDvFp4NzwPEjTEa5%2F7ECJc9YkAwm8PwdNbSTdFmK5dVWI2WaNv0WkDRxTQMPT%2BUqtQGsFRkAD7%2FvJ9OV37jbSjBYsfBCcuDsgQ9Tp8DkRWGbdbqsHwKqKYwkvD%2F0gY6pgHCXJYr8Zx7wOpIRfer7yREkC6SqlbkyTI%2FnVxwYGPCA9DwE%2FwW%2FD%2F%2BWXC0s2ljkseVkCO3XQyYxFTLM1q4bO83vpTEo5QJ48pVVTKlWms5BPbu0qnelypsMHnrN%2BWyrLKuXbmkVt5fqqSivnwqL3yLjxUbiEhNlXziZRs38mx%2BR3GL7uvHRIws66krdkF1Brm%2BKYmqjgY0Uqqr39GemNUGyuRybvVT&X-Amz-Signature=1f9b92b7fccd8eb397449ecd88c60327b65961e3f04c03ba24af03b968c8f235&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

```java
2.2.2.10 修改其他节点配置
修改集群中其他节点的配置文件：config/elasticsearch.yml 。

linux2：证书直接拷贝，其他步骤完全相同，配置文件中修改如下内容即可

# 设置节点名称 
node.name: es-node-2 

linux3：证书直接拷贝，其他步骤完全相同，配置文件中修改如下内容即可
# 设置节点名称 
node.name: es-node-3



2.2.2.11 依次启动服务节点
依次启动集群的三台服务器节点，不要忘记切换用户后再启动


# linux1:后台启动服务 
bin/elasticsearch -d 

# linux2: 后台启动服务 
bin/elasticsearch -d 

# linux3: 后台启动服务 
bin/elasticsearch -d


2.2.3 问题解决
2.2.3.1 JDK问题
Elasticsearch 是使用 Java开发的，Elasticsearch8.1 版本需要 JDK17 及以上版本。

默认安装包中带有 JDK 环境，如果系统配置 ES_JAVA_HOME环境变量，那么会采用系统配置的JDK。如果没有配置该环境变量，Elasticsearch会使用自带捆绑的 JDK，虽然自带的 JDK 是 Elasticsearch软件推荐的 Java 版本，但一般建议使用系统配置的 JDK。

2.2.3.2 SSL认证问题
Windows 环境中出现下面的错误信息，是因为开启了 SSL 认证，可以将SSL认证关闭

```

[image](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/b4f3d49d-e26f-4d3e-8c18-f07e9b78c2fc/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466S7L4F2TO%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T225331Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCICilfZlTmpohzhJxTrVNDlryRcovLtySdOdmFjUEj9BvAiAb4UJiLXEQPbFUK2tgJUlLHJumB8Lbc2BMaggsHstaqCqIBAjI%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMr337Y7St8Cuwm7wbKtwD6WCv3LP6sD0RG%2B5PChSAD9Vl9NSgPUERzWPhafYCZtIL%2BVBPsrBOGKOy3lSwGGCTZYrE0P2cMgQRtYSJHXdUo6NTd%2BBkg1sM%2Fw4YNzqhjGGHJ5o1LTyyXQfg8Bnh4HaZHTB4eZejlIjGl1H7eCAUdZjaRp0TCoD%2Fpf%2BOz3Abz6WwK1GlZM8C%2F3yMR5f0w0xdZ6F%2BaalVABVMyNT%2FKXwEoy%2BgXl2nHQWpc2woUU4GGhBJAjxOJk%2BTvS7lvfCiUM1Sn3kHCQRt2W2PoHpx07Ful7FIdpikGnrZyIeZlzaXoIZ7lEYA1yYn5JzOGqdlZ%2FQCCHVsOjofpbXF1cCJGpL1sEdewjvqw9U3a4WBxGlhfwfB0spGiCk1%2FZpwgClWdUXovO306pDQZlMVVTe8ffacVXcpJZO%2FNtjOJglmQBeVe75Y%2BllzdCocc6weyvBMzI0SOiXxTtiR3dSzykI5gMxMCoC3B%2BVW1VIysc5yASJBxK2LjN3ghdxYddD%2BZq%2By8bMs0IVD4tDvFp4NzwPEjTEa5%2F7ECJc9YkAwm8PwdNbSTdFmK5dVWI2WaNv0WkDRxTQMPT%2BUqtQGsFRkAD7%2FvJ9OV37jbSjBYsfBCcuDsgQ9Tp8DkRWGbdbqsHwKqKYwkvD%2F0gY6pgHCXJYr8Zx7wOpIRfer7yREkC6SqlbkyTI%2FnVxwYGPCA9DwE%2FwW%2FD%2F%2BWXC0s2ljkseVkCO3XQyYxFTLM1q4bO83vpTEo5QJ48pVVTKlWms5BPbu0qnelypsMHnrN%2BWyrLKuXbmkVt5fqqSivnwqL3yLjxUbiEhNlXziZRs38mx%2BR3GL7uvHRIws66krdkF1Brm%2BKYmqjgY0Uqqr39GemNUGyuRybvVT&X-Amz-Signature=64081b3e27a296cbf32616d49eb2fef5a404bfd6ef9894af84134c2845a82833&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

```java
修改 config/elasticsearch.yml 文件，将 enabled 的值修改为 false

xpack.security.http.ssl: 
 enabled: false 
 keystore.path: certs/http.p12


启动成功后，如果访问 localhost:9200 地址后
```

[image](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/ad44bbc9-2fe3-494c-828f-a17a4afe114e/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466S7L4F2TO%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T225331Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCICilfZlTmpohzhJxTrVNDlryRcovLtySdOdmFjUEj9BvAiAb4UJiLXEQPbFUK2tgJUlLHJumB8Lbc2BMaggsHstaqCqIBAjI%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMr337Y7St8Cuwm7wbKtwD6WCv3LP6sD0RG%2B5PChSAD9Vl9NSgPUERzWPhafYCZtIL%2BVBPsrBOGKOy3lSwGGCTZYrE0P2cMgQRtYSJHXdUo6NTd%2BBkg1sM%2Fw4YNzqhjGGHJ5o1LTyyXQfg8Bnh4HaZHTB4eZejlIjGl1H7eCAUdZjaRp0TCoD%2Fpf%2BOz3Abz6WwK1GlZM8C%2F3yMR5f0w0xdZ6F%2BaalVABVMyNT%2FKXwEoy%2BgXl2nHQWpc2woUU4GGhBJAjxOJk%2BTvS7lvfCiUM1Sn3kHCQRt2W2PoHpx07Ful7FIdpikGnrZyIeZlzaXoIZ7lEYA1yYn5JzOGqdlZ%2FQCCHVsOjofpbXF1cCJGpL1sEdewjvqw9U3a4WBxGlhfwfB0spGiCk1%2FZpwgClWdUXovO306pDQZlMVVTe8ffacVXcpJZO%2FNtjOJglmQBeVe75Y%2BllzdCocc6weyvBMzI0SOiXxTtiR3dSzykI5gMxMCoC3B%2BVW1VIysc5yASJBxK2LjN3ghdxYddD%2BZq%2By8bMs0IVD4tDvFp4NzwPEjTEa5%2F7ECJc9YkAwm8PwdNbSTdFmK5dVWI2WaNv0WkDRxTQMPT%2BUqtQGsFRkAD7%2FvJ9OV37jbSjBYsfBCcuDsgQ9Tp8DkRWGbdbqsHwKqKYwkvD%2F0gY6pgHCXJYr8Zx7wOpIRfer7yREkC6SqlbkyTI%2FnVxwYGPCA9DwE%2FwW%2FD%2F%2BWXC0s2ljkseVkCO3XQyYxFTLM1q4bO83vpTEo5QJ48pVVTKlWms5BPbu0qnelypsMHnrN%2BWyrLKuXbmkVt5fqqSivnwqL3yLjxUbiEhNlXziZRs38mx%2BR3GL7uvHRIws66krdkF1Brm%2BKYmqjgY0Uqqr39GemNUGyuRybvVT&X-Amz-Signature=c9a868b25ad4b0d67ec80d39b9f7ab71b5d978b85f4b949db4b0e28423202f6c&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

```java
# ======================== Elasticsearch Configuration =========================
#
# NOTE: Elasticsearch comes with reasonable defaults for most settings.
#       Before you set out to tweak and tune the configuration, make sure you
#       understand what are you trying to accomplish and the consequences.
#
# The primary way of configuring a node is via this file. This template lists
# the most important settings you may want to configure for a production cluster.
#
# Please consult the documentation for further information on configuration options:
# https://www.elastic.co/guide/en/elasticsearch/reference/index.html
#
# ---------------------------------- Cluster -----------------------------------
#
# Use a descriptive name for your cluster:
#


# 集群名称 
cluster.name: elasticsearch-cluster-8.7


#
# ------------------------------------ Node ------------------------------------
#
# Use a descriptive name for the node:

# 集群中每个节点的名称
node.name: es-node-1

# Add custom attributes to the node:
#
#node.attr.rack: r1
#
# ----------------------------------- Paths ------------------------------------
#
# Path to directory where to store the data (separate multiple locations by comma):
#

# 数据存放的目录
path.data: /usr/local/elasticsearch-8.7.0/data


#
# Path to log files:
#

path.logs: /usr/local/elasticsearch-8.7.0/logs


#
# ----------------------------------- Memory -----------------------------------
#
# Lock the memory on startup:
#
#bootstrap.memory_lock: true
#
# Make sure that the heap size is set to about half the memory available
# on the system and that the owner of the process is allowed to use this
# limit.
#
# Elasticsearch performs poorly when the system is swapping the memory.
#
# ---------------------------------- Network -----------------------------------
#
# By default Elasticsearch is only accessible on localhost. Set a different
# address here to expose this node on the network:
#

# 可以被挖补网络访问
network.host: 0.0.0.0
#
# By default Elasticsearch listens for HTTP traffic on the first free port it
# finds starting at 9200. Set a specific HTTP port here:
#
# http 的端口号,这里使用默认 9200
http.port: 9200

#
# For more information, consult the network module documentation.
#
# --------------------------------- Discovery ----------------------------------
#
# Pass an initial list of hosts to perform discovery when this node is started:
# The default list of hosts is ["127.0.0.1", "[::1]"]
#

# 集群地址列表
discovery.seed_hosts: ["192.168.13.213", "192.168.13.214", "192.168.13.215"]



#
# Bootstrap the cluster using an initial set of master-eligible nodes:
#
cluster.initial_master_nodes: ["es-node-1"]

#
# For more information, consult the discovery and cluster formation module documentation.
#
# ---------------------------------- Various -----------------------------------
#
# Allow wildcard deletion of indices:
#
#action.destructive_requires_name: false

# 初始节点 
#discovery.seed_hosts: ["es-node-1"] 

# 安全认证 
xpack.security.enabled:  true   # 设置次属性为 false 登录的时候不需要密码
xpack.security.enrollment.enabled: true 
xpack.security.http.ssl: 
 enabled: true 
 keystore.path: /usr/local/elasticsearch-8.7.0/config/certs/http.p12 
 truststore.path: /usr/local/elasticsearch-8.7.0/config/certs/http.p12 
xpack.security.transport.ssl: 
 enabled: true 
 verification_mode: certificate 
 keystore.path: /usr/local/elasticsearch-8.7.0/config/certs/elastic-certificates.p12 
 truststore.path: /usr/local/elasticsearch-8.7.0/config/certs/elastic-certificates.p12 



ingest.geoip.downloader.enabled: false 
xpack.security.http.ssl.client_authentication: none
```

```java
jvm.option

==================================================================================
################################################################
##
## JVM configuration
##
################################################################
##
## WARNING: DO NOT EDIT THIS FILE. If you want to override the
## JVM options in this file, or set any additional options, you
## should create one or more files in the jvm.options.d
## directory containing your adjustments.
##
## See https://www.elastic.co/guide/en/elasticsearch/reference/8.7/jvm-options.html
## for more information.
##
################################################################



################################################################
## IMPORTANT: JVM heap size
################################################################
##
## The heap size is automatically configured by Elasticsearch
## based on the available memory in your system and the roles
## each node is configured to fulfill. If specifying heap is
## required, it should be done through a file in jvm.options.d,
## which should be named with .options suffix, and the min and
## max should be set to the same value. For example, to set the
## heap to 4 GB, create a new file in the jvm.options.d
## directory containing these lines:

8-9:-Xmx2g
8-9:-Xms2g

## -Xms4g
## -Xmx4g
##
## See https://www.elastic.co/guide/en/elasticsearch/reference/8.7/heap-size.html
## for more information
##
################################################################


################################################################
## Expert settings
################################################################
##
## All settings below here are considered expert settings. Do
## not adjust them unless you understand what you are doing. Do
## not edit them in this file; instead, create a new file in the
## jvm.options.d directory containing your adjustments.
##
################################################################

-XX:+UseG1GC

## JVM temporary directory
-Djava.io.tmpdir=${ES_TMPDIR}

## heap dumps

# generate a heap dump when an allocation from the Java heap fails; heap dumps
# are created in the working directory of the JVM unless an alternative path is
# specified
-XX:+HeapDumpOnOutOfMemoryError

# exit right after heap dump on out of memory error
-XX:+ExitOnOutOfMemoryError

# specify an alternative path for heap dumps; ensure the directory exists and
# has sufficient space
-XX:HeapDumpPath=data

# specify an alternative path for JVM fatal error logs
-XX:ErrorFile=logs/hs_err_pid%p.log

## GC logging
-Xlog:gc*,gc+age=trace,safepoint:file=logs/gc.log:utctime,level,pid,tags:filecount=32,filesize=64m
```

```java
/etc/sysctl.conf

=============================================================
# /etc/security/limits.conf
#
#This file sets the resource limits for the users logged in via PAM.
#It does not affect resource limits of the system services.
#
#Also note that configuration files in /etc/security/limits.d directory,
#which are read in alphabetical order, override the settings in this
#file in case the domain is the same or more specific.
#That means for example that setting a limit for wildcard domain here
#can be overriden with a wildcard setting in a config file in the
#subdirectory, but a user specific setting here can be overriden only
#with a user specific setting in the subdirectory.
#
#Each line describes a limit for a user in the form:

elastic  -  nofile  65535


#
#<domain>        <type>  <item>  <value>
#
#Where:
#<domain> can be:
#        - a user name
#        - a group name, with @group syntax
#        - the wildcard *, for default entry
#        - the wildcard %, can be also used with %group syntax,
#                 for maxlogin limit
#
#<type> can have the two values:
#        - "soft" for enforcing the soft limits
#        - "hard" for enforcing hard limits
#
#<item> can be one of the following:
#        - core - limits the core file size (KB)
#        - data - max data size (KB)
#        - fsize - maximum filesize (KB)
#        - memlock - max locked-in-memory address space (KB)
#        - nofile - max number of open file descriptors
#        - rss - max resident set size (KB)
#        - stack - max stack size (KB)
#        - cpu - max CPU time (MIN)
#        - nproc - max number of processes
#        - as - address space limit (KB)
#        - maxlogins - max number of logins for this user
#        - maxsyslogins - max number of logins on the system
#        - priority - the priority to run user process with
#        - locks - max number of file locks the user can hold
#        - sigpending - max number of pending signals
#        - msgqueue - max memory used by POSIX message queues (bytes)
#        - nice - max nice priority allowed to raise to values: [-20, 19]
#        - rtprio - max realtime priority
#
#<domain>      <type>  <item>         <value>
#

#*               soft    core            0
#*               hard    rss             10000
#@student        hard    nproc           20
#@faculty        soft    nproc           20
#@faculty        hard    nproc           50
#ftp             hard    nproc           0
#@student        -       maxlogins       4

# End of file
```

# 给用户设置密码

[https://blog.csdn.net/weixin_38285720/article/details/123589570](https://blog.csdn.net/weixin_38285720/article/details/123589570)


```java
修改密码需要在es启动,并cd到es的bin目录下执行：

1.重置密码并在控制台显示新密码（密码是自动生成的复杂度较高）

./elasticsearch-reset-password -u 用户名
例：重置 elastic 用户的密码 ./elasticsearch-reset-password -u elastic
```

[image](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/54c65f4e-e4bf-4490-9246-cf0ff3e9c679/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466S7L4F2TO%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T225331Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCICilfZlTmpohzhJxTrVNDlryRcovLtySdOdmFjUEj9BvAiAb4UJiLXEQPbFUK2tgJUlLHJumB8Lbc2BMaggsHstaqCqIBAjI%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMr337Y7St8Cuwm7wbKtwD6WCv3LP6sD0RG%2B5PChSAD9Vl9NSgPUERzWPhafYCZtIL%2BVBPsrBOGKOy3lSwGGCTZYrE0P2cMgQRtYSJHXdUo6NTd%2BBkg1sM%2Fw4YNzqhjGGHJ5o1LTyyXQfg8Bnh4HaZHTB4eZejlIjGl1H7eCAUdZjaRp0TCoD%2Fpf%2BOz3Abz6WwK1GlZM8C%2F3yMR5f0w0xdZ6F%2BaalVABVMyNT%2FKXwEoy%2BgXl2nHQWpc2woUU4GGhBJAjxOJk%2BTvS7lvfCiUM1Sn3kHCQRt2W2PoHpx07Ful7FIdpikGnrZyIeZlzaXoIZ7lEYA1yYn5JzOGqdlZ%2FQCCHVsOjofpbXF1cCJGpL1sEdewjvqw9U3a4WBxGlhfwfB0spGiCk1%2FZpwgClWdUXovO306pDQZlMVVTe8ffacVXcpJZO%2FNtjOJglmQBeVe75Y%2BllzdCocc6weyvBMzI0SOiXxTtiR3dSzykI5gMxMCoC3B%2BVW1VIysc5yASJBxK2LjN3ghdxYddD%2BZq%2By8bMs0IVD4tDvFp4NzwPEjTEa5%2F7ECJc9YkAwm8PwdNbSTdFmK5dVWI2WaNv0WkDRxTQMPT%2BUqtQGsFRkAD7%2FvJ9OV37jbSjBYsfBCcuDsgQ9Tp8DkRWGbdbqsHwKqKYwkvD%2F0gY6pgHCXJYr8Zx7wOpIRfer7yREkC6SqlbkyTI%2FnVxwYGPCA9DwE%2FwW%2FD%2F%2BWXC0s2ljkseVkCO3XQyYxFTLM1q4bO83vpTEo5QJ48pVVTKlWms5BPbu0qnelypsMHnrN%2BWyrLKuXbmkVt5fqqSivnwqL3yLjxUbiEhNlXziZRs38mx%2BR3GL7uvHRIws66krdkF1Brm%2BKYmqjgY0Uqqr39GemNUGyuRybvVT&X-Amz-Signature=5e97e7503ea1f304fa00fb97c735982504e128b8ea36175fa0d05f766328061d&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

```java
2. 给用户修改指定的密码

./elasticsearch-reset-password --username 用户名 -i
例：重置kibana 用户的密码

./elasticsearch-reset-password --username kibana -i

```

[image](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/a260ef19-57e7-40a8-b04f-b34ff361f778/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466S7L4F2TO%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T225331Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCICilfZlTmpohzhJxTrVNDlryRcovLtySdOdmFjUEj9BvAiAb4UJiLXEQPbFUK2tgJUlLHJumB8Lbc2BMaggsHstaqCqIBAjI%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMr337Y7St8Cuwm7wbKtwD6WCv3LP6sD0RG%2B5PChSAD9Vl9NSgPUERzWPhafYCZtIL%2BVBPsrBOGKOy3lSwGGCTZYrE0P2cMgQRtYSJHXdUo6NTd%2BBkg1sM%2Fw4YNzqhjGGHJ5o1LTyyXQfg8Bnh4HaZHTB4eZejlIjGl1H7eCAUdZjaRp0TCoD%2Fpf%2BOz3Abz6WwK1GlZM8C%2F3yMR5f0w0xdZ6F%2BaalVABVMyNT%2FKXwEoy%2BgXl2nHQWpc2woUU4GGhBJAjxOJk%2BTvS7lvfCiUM1Sn3kHCQRt2W2PoHpx07Ful7FIdpikGnrZyIeZlzaXoIZ7lEYA1yYn5JzOGqdlZ%2FQCCHVsOjofpbXF1cCJGpL1sEdewjvqw9U3a4WBxGlhfwfB0spGiCk1%2FZpwgClWdUXovO306pDQZlMVVTe8ffacVXcpJZO%2FNtjOJglmQBeVe75Y%2BllzdCocc6weyvBMzI0SOiXxTtiR3dSzykI5gMxMCoC3B%2BVW1VIysc5yASJBxK2LjN3ghdxYddD%2BZq%2By8bMs0IVD4tDvFp4NzwPEjTEa5%2F7ECJc9YkAwm8PwdNbSTdFmK5dVWI2WaNv0WkDRxTQMPT%2BUqtQGsFRkAD7%2FvJ9OV37jbSjBYsfBCcuDsgQ9Tp8DkRWGbdbqsHwKqKYwkvD%2F0gY6pgHCXJYr8Zx7wOpIRfer7yREkC6SqlbkyTI%2FnVxwYGPCA9DwE%2FwW%2FD%2F%2BWXC0s2ljkseVkCO3XQyYxFTLM1q4bO83vpTEo5QJ48pVVTKlWms5BPbu0qnelypsMHnrN%2BWyrLKuXbmkVt5fqqSivnwqL3yLjxUbiEhNlXziZRs38mx%2BR3GL7uvHRIws66krdkF1Brm%2BKYmqjgY0Uqqr39GemNUGyuRybvVT&X-Amz-Signature=55092898db024cd5ae74f38d373c2203d8872d27c09bcb9b140f7d157a2b5851&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

```java
3.给用户自动生成一个密码

./elasticsearch-reset-password --url "es的实际地址" --username '用户名' -i
例：重置kibana 用户：

bin/elasticsearch-reset-password --url "http://127.0.0.1:9200" --username kibana -i
执行命令之后，输入y 在输入两次密码即可

```

[image](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/dfedc2b9-1332-426f-9f98-e60a139497d4/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466S7L4F2TO%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T225331Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCICilfZlTmpohzhJxTrVNDlryRcovLtySdOdmFjUEj9BvAiAb4UJiLXEQPbFUK2tgJUlLHJumB8Lbc2BMaggsHstaqCqIBAjI%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMr337Y7St8Cuwm7wbKtwD6WCv3LP6sD0RG%2B5PChSAD9Vl9NSgPUERzWPhafYCZtIL%2BVBPsrBOGKOy3lSwGGCTZYrE0P2cMgQRtYSJHXdUo6NTd%2BBkg1sM%2Fw4YNzqhjGGHJ5o1LTyyXQfg8Bnh4HaZHTB4eZejlIjGl1H7eCAUdZjaRp0TCoD%2Fpf%2BOz3Abz6WwK1GlZM8C%2F3yMR5f0w0xdZ6F%2BaalVABVMyNT%2FKXwEoy%2BgXl2nHQWpc2woUU4GGhBJAjxOJk%2BTvS7lvfCiUM1Sn3kHCQRt2W2PoHpx07Ful7FIdpikGnrZyIeZlzaXoIZ7lEYA1yYn5JzOGqdlZ%2FQCCHVsOjofpbXF1cCJGpL1sEdewjvqw9U3a4WBxGlhfwfB0spGiCk1%2FZpwgClWdUXovO306pDQZlMVVTe8ffacVXcpJZO%2FNtjOJglmQBeVe75Y%2BllzdCocc6weyvBMzI0SOiXxTtiR3dSzykI5gMxMCoC3B%2BVW1VIysc5yASJBxK2LjN3ghdxYddD%2BZq%2By8bMs0IVD4tDvFp4NzwPEjTEa5%2F7ECJc9YkAwm8PwdNbSTdFmK5dVWI2WaNv0WkDRxTQMPT%2BUqtQGsFRkAD7%2FvJ9OV37jbSjBYsfBCcuDsgQ9Tp8DkRWGbdbqsHwKqKYwkvD%2F0gY6pgHCXJYr8Zx7wOpIRfer7yREkC6SqlbkyTI%2FnVxwYGPCA9DwE%2FwW%2FD%2F%2BWXC0s2ljkseVkCO3XQyYxFTLM1q4bO83vpTEo5QJ48pVVTKlWms5BPbu0qnelypsMHnrN%2BWyrLKuXbmkVt5fqqSivnwqL3yLjxUbiEhNlXziZRs38mx%2BR3GL7uvHRIws66krdkF1Brm%2BKYmqjgY0Uqqr39GemNUGyuRybvVT&X-Amz-Signature=1290bfe7d322096bfefcdf7a1acaeb1092b8c98172c4f89be706e8d733042df5&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)


