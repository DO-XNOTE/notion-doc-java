---
title: 2-4 Kafka海量日志收集实战_filebeat日志收集实战-1
---

# 2-4 Kafka海量日志收集实战_filebeat日志收集实战-1

[image](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/4c13777e-b2ac-488a-8698-9429f7a2c9c7/SCR-20240807-gwft.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665KR4JOM5%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T225326Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCJuP8cI5EMd9HQJsNAbxEJRSBQfTsftNE9oOY33bozTgIgcYDv22%2BSPrqabRvW5VFx5uzWUI2GoDij0UyEASAf99IqiAQIxv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDN7gCAdujohIiEr6uircA7KqJW%2BgvybRqRdGSVjhQNKJb%2BiNsNHnyMQqJZmi0y3jJCJr4CpxUHHQx4wrThUshsk26H51Ri%2Fz55ZBj9e8DKElspC%2FEvbzHTKNJNhBZljNUx5EbjBBQaY9d197ZIZGNhvmIjtPRYCeE0lk9XLIY4HD6%2BEXNyGFgrJpUEe2q2isoPuXkdGmj0jhNCVMaFIKoisiaBtJtl3QeU3QuxWIIdizt0uBVJW%2B5nzoxp1rvLQJXUPYJ4mbevfe%2BgVhrV9waFtFTL5e20Y0xgd8sRwsHcf83UOwITt5ATkC24uRjwMo9Osyc8irtt0tPhHWYdF%2F0F%2FaqZi3ib%2BkEMELd707DyhRBV3URluLzJSr3wlN%2FHRW11e3CH4S5dLxiKoBsuuumDSxCpCivTPxZV33fHifD5Ico7H5PPbF1FxOR7CZHgAcArt2n3oAJcgNY6eEEfAPocQ3mbYsK1H9mNeOsu%2BbRZs5SiV5JbRlzJQPUdpTjGCWBxyqu9RrPO00EKU%2BY%2Fg2Tc0N4%2F3bxaHhXl4c%2FQQf0DyJwqVm1ivj42%2BVF2ssDVnpjYOFBiS01OtYURtPfBYQbSXmkaaW7r3J7hmup8QfuxzTqHkkosWVCO%2BIPV2v5XVrFRvyVCPAbWCLFZvGMLu3%2F9IGOqUBi89N%2FqyoqO0%2BZ3urycpdv0XoEmILfAYc4uiPuWltHHF4UmOmu291%2F163Q9RoU9HUcxCdBpqLv5NRLJusdU2bYS%2BBjX%2F%2BmU%2BsJ2POB7%2BQDoVXYaW3y%2FWr7ZYMjeF%2FfaaT034%2BjwooWK5EEPdSQ5J6gC%2F0YpXRudqOsPEmg2jIWlZSt2RjwhCvD5%2B1UcHxa8%2BKOJnm4cf8vPuKqcfOC31XgUb10h5Z&X-Amz-Signature=b6468f3dbf105429faf59aec5bfed60c788181df3cef4f514d2f742f7d5492e6&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

[image](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/f357b9b5-d8c0-4958-bf63-779b27e14e3b/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665KR4JOM5%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T225326Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCJuP8cI5EMd9HQJsNAbxEJRSBQfTsftNE9oOY33bozTgIgcYDv22%2BSPrqabRvW5VFx5uzWUI2GoDij0UyEASAf99IqiAQIxv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDN7gCAdujohIiEr6uircA7KqJW%2BgvybRqRdGSVjhQNKJb%2BiNsNHnyMQqJZmi0y3jJCJr4CpxUHHQx4wrThUshsk26H51Ri%2Fz55ZBj9e8DKElspC%2FEvbzHTKNJNhBZljNUx5EbjBBQaY9d197ZIZGNhvmIjtPRYCeE0lk9XLIY4HD6%2BEXNyGFgrJpUEe2q2isoPuXkdGmj0jhNCVMaFIKoisiaBtJtl3QeU3QuxWIIdizt0uBVJW%2B5nzoxp1rvLQJXUPYJ4mbevfe%2BgVhrV9waFtFTL5e20Y0xgd8sRwsHcf83UOwITt5ATkC24uRjwMo9Osyc8irtt0tPhHWYdF%2F0F%2FaqZi3ib%2BkEMELd707DyhRBV3URluLzJSr3wlN%2FHRW11e3CH4S5dLxiKoBsuuumDSxCpCivTPxZV33fHifD5Ico7H5PPbF1FxOR7CZHgAcArt2n3oAJcgNY6eEEfAPocQ3mbYsK1H9mNeOsu%2BbRZs5SiV5JbRlzJQPUdpTjGCWBxyqu9RrPO00EKU%2BY%2Fg2Tc0N4%2F3bxaHhXl4c%2FQQf0DyJwqVm1ivj42%2BVF2ssDVnpjYOFBiS01OtYURtPfBYQbSXmkaaW7r3J7hmup8QfuxzTqHkkosWVCO%2BIPV2v5XVrFRvyVCPAbWCLFZvGMLu3%2F9IGOqUBi89N%2FqyoqO0%2BZ3urycpdv0XoEmILfAYc4uiPuWltHHF4UmOmu291%2F163Q9RoU9HUcxCdBpqLv5NRLJusdU2bYS%2BBjX%2F%2BmU%2BsJ2POB7%2BQDoVXYaW3y%2FWr7ZYMjeF%2FfaaT034%2BjwooWK5EEPdSQ5J6gC%2F0YpXRudqOsPEmg2jIWlZSt2RjwhCvD5%2B1UcHxa8%2BKOJnm4cf8vPuKqcfOC31XgUb10h5Z&X-Amz-Signature=c761960625ee7358aba556c68bca2d32ec9fa60e64d83a25f30cee938cc368cc&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

OK，小伙伴们大家好，这节课我们继续往下学习，来学习我们对应的这个日志收集，就是我们海量数据的这么一个实战。那这个对于日收集是一个什么概念？就是说我们上节课已经通过 s l 呼g，就是我们的这个 log 呼 g two 这个组件把日志打到了我们本地的这个 log 文件上，一个是 app log，还有一个是 l log，全量的日志是在 app log 上，那么对应着 warning 级别以上的日志是在 error 点 log 里边。

[file](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/e3e137b3-6a23-4feb-a3d6-3d49968d1501/filebeat.yml?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665KR4JOM5%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T225326Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCJuP8cI5EMd9HQJsNAbxEJRSBQfTsftNE9oOY33bozTgIgcYDv22%2BSPrqabRvW5VFx5uzWUI2GoDij0UyEASAf99IqiAQIxv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDN7gCAdujohIiEr6uircA7KqJW%2BgvybRqRdGSVjhQNKJb%2BiNsNHnyMQqJZmi0y3jJCJr4CpxUHHQx4wrThUshsk26H51Ri%2Fz55ZBj9e8DKElspC%2FEvbzHTKNJNhBZljNUx5EbjBBQaY9d197ZIZGNhvmIjtPRYCeE0lk9XLIY4HD6%2BEXNyGFgrJpUEe2q2isoPuXkdGmj0jhNCVMaFIKoisiaBtJtl3QeU3QuxWIIdizt0uBVJW%2B5nzoxp1rvLQJXUPYJ4mbevfe%2BgVhrV9waFtFTL5e20Y0xgd8sRwsHcf83UOwITt5ATkC24uRjwMo9Osyc8irtt0tPhHWYdF%2F0F%2FaqZi3ib%2BkEMELd707DyhRBV3URluLzJSr3wlN%2FHRW11e3CH4S5dLxiKoBsuuumDSxCpCivTPxZV33fHifD5Ico7H5PPbF1FxOR7CZHgAcArt2n3oAJcgNY6eEEfAPocQ3mbYsK1H9mNeOsu%2BbRZs5SiV5JbRlzJQPUdpTjGCWBxyqu9RrPO00EKU%2BY%2Fg2Tc0N4%2F3bxaHhXl4c%2FQQf0DyJwqVm1ivj42%2BVF2ssDVnpjYOFBiS01OtYURtPfBYQbSXmkaaW7r3J7hmup8QfuxzTqHkkosWVCO%2BIPV2v5XVrFRvyVCPAbWCLFZvGMLu3%2F9IGOqUBi89N%2FqyoqO0%2BZ3urycpdv0XoEmILfAYc4uiPuWltHHF4UmOmu291%2F163Q9RoU9HUcxCdBpqLv5NRLJusdU2bYS%2BBjX%2F%2BmU%2BsJ2POB7%2BQDoVXYaW3y%2FWr7ZYMjeF%2FfaaT034%2BjwooWK5EEPdSQ5J6gC%2F0YpXRudqOsPEmg2jIWlZSt2RjwhCvD5%2B1UcHxa8%2BKOJnm4cf8vPuKqcfOC31XgUb10h5Z&X-Amz-Signature=b2c936f133cd16a8b97afeee6789d88e11d5a6b8a47f52013d277723f2cacd2d&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)


那接下来我们要做的事情就是要把这些数据通过组件，然后收集到某个地方。那比如说我们其实就应该把它收集到我们的这个卡里边，因为前面我们看到那幅图就是说我们本地的应用日志，我要通过 file beat 这个组件，然后把它收集到卡夫卡里，然后对应着卡夫卡的这个producer，那就是我们的 file b 的生产者，生产消息随递到卡中，消费者是谁？消费者就是我们的这个Logstash，那通过 Logstash 把数据过滤，过滤完了之后再 think 到我们对应的 elastic search 上，然后用 Kibana 去做一个展示。

[image](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/71e33056-ee52-42c0-aa5d-26845ba8814c/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665KR4JOM5%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T225326Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCJuP8cI5EMd9HQJsNAbxEJRSBQfTsftNE9oOY33bozTgIgcYDv22%2BSPrqabRvW5VFx5uzWUI2GoDij0UyEASAf99IqiAQIxv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDN7gCAdujohIiEr6uircA7KqJW%2BgvybRqRdGSVjhQNKJb%2BiNsNHnyMQqJZmi0y3jJCJr4CpxUHHQx4wrThUshsk26H51Ri%2Fz55ZBj9e8DKElspC%2FEvbzHTKNJNhBZljNUx5EbjBBQaY9d197ZIZGNhvmIjtPRYCeE0lk9XLIY4HD6%2BEXNyGFgrJpUEe2q2isoPuXkdGmj0jhNCVMaFIKoisiaBtJtl3QeU3QuxWIIdizt0uBVJW%2B5nzoxp1rvLQJXUPYJ4mbevfe%2BgVhrV9waFtFTL5e20Y0xgd8sRwsHcf83UOwITt5ATkC24uRjwMo9Osyc8irtt0tPhHWYdF%2F0F%2FaqZi3ib%2BkEMELd707DyhRBV3URluLzJSr3wlN%2FHRW11e3CH4S5dLxiKoBsuuumDSxCpCivTPxZV33fHifD5Ico7H5PPbF1FxOR7CZHgAcArt2n3oAJcgNY6eEEfAPocQ3mbYsK1H9mNeOsu%2BbRZs5SiV5JbRlzJQPUdpTjGCWBxyqu9RrPO00EKU%2BY%2Fg2Tc0N4%2F3bxaHhXl4c%2FQQf0DyJwqVm1ivj42%2BVF2ssDVnpjYOFBiS01OtYURtPfBYQbSXmkaaW7r3J7hmup8QfuxzTqHkkosWVCO%2BIPV2v5XVrFRvyVCPAbWCLFZvGMLu3%2F9IGOqUBi89N%2FqyoqO0%2BZ3urycpdv0XoEmILfAYc4uiPuWltHHF4UmOmu291%2F163Q9RoU9HUcxCdBpqLv5NRLJusdU2bYS%2BBjX%2F%2BmU%2BsJ2POB7%2BQDoVXYaW3y%2FWr7ZYMjeF%2FfaaT034%2BjwooWK5EEPdSQ5J6gC%2F0YpXRudqOsPEmg2jIWlZSt2RjwhCvD5%2B1UcHxa8%2BKOJnm4cf8vPuKqcfOC31XgUb10h5Z&X-Amz-Signature=ea81a231ee9ce44ce216ae460ed0f1b661f9e8fec1789dee62fe7f4c921ea00d&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

OK，那现在这节课我们就来看一看这个日志如何去收集，那收集呢？首先我们要知道一点，就是对应着我们的 filebeat 其实是一个什么概念？就是说如何去做收集，那对应着我们其实 bits 家族里面有好多好多bits，比如说 filebeat，还有什么 package beat，包括等等一些其他的，比如说像 Heartbeat beat 等等，有好多好多beat，我们到底怎么去选择呢？其实对应着文件的收集，我们一般都会去选 filebeat，在这里老师，卡夫卡所对应的这个 fail b 的版本，我们现在用的是六点零，那就是说我们的 elastic search 用的也是 6. 6 这个版本。


好了，那我们主要对菲尔比特学习哪些内容呢？我们来一点点看。首先第一点就是说如何去做入门安装使用它，然后搞定了它之后，对应着这个 file beat 配置文件应该怎么去做？我们对配置文件做一个讲解，然后接下来怎么去对接我们的卡夫卡，对吧？你们对接卡夫卡这个事情是很重要的，以及我们实际的应用实战结合着去做，那这个就是我们这节课主要讲的内容了，也就是说日志收集。


OK，在这里老师已经准备好了两台服务器， Linux 虚拟机，一个是幺九二点幺六八点幺幺点三幺，还有一个是 51 这个节点，那 51 这个节点通过之前咱们学习知道了，他就是我们的卡斯卡，对吧？那我们现在话不多说，直接帮我们卡夫卡启动起来 u s r local，然后到卡夫卡下面 2. 12 这个版本，到 b 下面去， b 下面有很多脚本文件，我们去执行一下对应的启动卡夫卡的命令，就在这我们要启动卡夫卡的这个server，然后 start 点SH，然后指定对应的这个 config 阅读文件点practice。这样的话我们首先就把卡夫卡提起来了。OK，我们稍微耐心等待一下，看一看，考察启动 GPS 一下，看一下。


目前可能老师启动的节点可能比较多，又开了好多个虚拟机，大家可以看到开了差不多有将近十几个虚拟机，因为我们后面要整个的 elk 这块，我要把它搭建起来。所以说其实小伙伴们你自己想要去学习这课程，你自己是不是对应的这个内存，是不是你应该去要扩大点，我建议最低的配置是16G，当然老师自己的服务器的这个内存是32G。


好了，卡芙莎已经启动起来了，然后我们比如说我想看一下卡不卡，现在到底有哪些topic，还记得哪个命令的老师在这里去按上键去找，其实您可以用什么呢？用 history 对吧？ history 直接就能找到之前历史执行的一些shell。好在这里边这个 long 杠list，我们来看一看我们现在现有的一些topic，首先有一个 app log 杠test，然后还有一个 error log 杠test，还有什么什么其他的直接不用去管，这些是以前的了，那证明我们卡夫卡现在已经起来了。


接下来 31 这个节点 CD 到 USR local 下，然后这里边是老师之前的东西，我们先不用去关注我们 CD 到 software 里边，现在我们就需要着手去安装这个 fail beat，老师已经准备好了这个 fail beat 这个安装包，那我们直接通过这个s， m p d 把它这个传进来就是 file beat。


我们现在采用的是六点零这个版本，包括对应着elk 的一套，比如说你的 log stash 也应该是六点零这个版本，包括你的 elastic search 以及Kibana，最好是要相同版本，当然我不是说必须要相同版本的话，就是最好是相同版本就是最好的了。如果你版本不相同的话，可能会有一些小问题，那这样的话你排查这个问题其实还挺费事的。所以说我建议大家要跟老师的版本统一，那我现在在 31 这个服务器上，我把 file beat 以及这个这两个配置文件我都一次性的 copy 过去，然后把它关掉。


现在的同学们请看，我现在已经有对应着这个 LB 特六点零的这个 card g 这个文件了，然后我如何去安装它？老师在这里已经给你写好了一个文档，就是后面我会把这个项目发给大家，大家就知道了，这里边这个文档就是Docs，这里边有一个 file beat 点TXT，我们就照着这个文档一步步操作，那你就能保证跟老师一致了。首先对于 fail beads 安装，那首先我们要 CD 到 source 链下，对吧？然后把对应的包传上去，然后我们紧接着解压就好了，解压就是踏杠CSVF，然后去把它解压到账大 c u s r local 下即可。


好了，那我们再回车，然后去解压这个菲尔bit，然后 c d 一点点，我们进到这里边，大家可以看到这个文件已经有了，是不是叫做 fail beat 六点零，然后 Linux 杠叉八六杠六四，对吧？好了，那接下来其实你可以给它改个名字，那现在是这样的，是不是我们 MV 它就好了？ MV 它，然后叫做它好搞定。现在呢，我们的名称已经改好了，叫 fail b 乘660。然后接下来我们 CD 到这个 file beat 里边，我们看一看它有什么样的配置好。这首先有一个 fields 点MIML，这个不用去关注，然后这个 fail beat 这个脚本就是我们后面启动 fail b 的时候，你要运行它，然后对应着核心的配置，主要是这个叫做 file beat，点 YML 这个配置文件是一定要去对它进行对应的配置的，这是很重要的。我们先打开看一下它默认的配置里面有哪些。

```java
========================最新版本的 8.7 的 filebeat================配置和之前的不一样了
## filebeat配置文件 
###################### Filebeat Configuration Example #########################
filebeat.inputs:

  - type: filestream
    id: app-collector.log # Unique ID among all inputs, an ID is required.
    enabled: true  # Change to true to enable this input configuration.
    paths:
      ## app-服务名称.log, 为什么写死，防止发生轮转抓取历史数据
      - /usr/local/logs/app-collector.log
        # 定义写入 ES 时的 _type 值
    #document_type: "app-log"
    multiline:
      type: pattern  # pattern: '^\s*(\d{4}|\d{2})\-(\d{2}|[a-zA-Z]{3})\-(\d{2}|\d{4})'   # 指定匹配的表达式（匹配以 2017-11-15 08:04:23:889 时间格式开头的字符串）
      pattern: '^\['                              # 指定匹配的表达式（匹配以 "{ 开头的字符串）
      negate: true                                # 是否匹配到
      match: after                                # 合并到上一行的末尾
      max_lines: 2000                             # 最大的行数
      timeout: 2s                                 # 如果在规定时间没有新的日志事件就不等待后面的日志
    fields:
      logbiz: collector
      logtopic: app-log-collector1   #  按服务划分用作kafka topic
      evn: dev

  - type: filestream
    id: app-collector.log # Unique ID among all inputs, an ID is required.
    enabled: true  # Change to true to enable this input configuration.
    paths:
      - /usr/local/logs/error-collector.log
    #document_type: "error-log"
    multiline:
      type: pattern   # pattern: '^\s*(\d{4}|\d{2})\-(\d{2}|[a-zA-Z]{3})\-(\d{2}|\d{4})'   # 指定匹配的表达式（匹配以 2017-11-15 08:04:23:889 时间格式开头的字符串）
      pattern: '^\['                              # 指定匹配的表达式（匹配以 "{ 开头的字符串）
      negate: true                                # 是否匹配到
      match: after                                # 合并到上一行的末尾
      max_lines: 2000                             # 最大的行数
      timeout: 2s                                 # 如果在规定时间没有新的日志事件就不等待后面的日志
    fields:
      logbiz: collector
      logtopic: error-log-collector1   # 按服务划分用作kafka topic
      evn: dev

output.kafka:
  hosts: ["192.168.13.210:9092", "192.168.13.211:9092", "192.168.13.212:9092"]
  topic: '%{[fields.log_topic]}'
  partition.round_robin:
    reachable_only: true
  required_acks: 1
  compression: gzip
  max_message_bytes: 1000000
logging.to_files: true
```

4 l b 它主要是干什么的？它主要就是提供抓取文件的，然后它这个inputs，比如说我的输入是什么，然后它的 type 是log，然后它的enable，这里面有一些配置项。pass，我要抓取哪些目录下面的点 log 文件，这里面都有对应的配置，并且它里边还可以跟我们的各种各样的组件进行集成，比如说 n g x，就是 n g x 的一些组件，然后它里边还可以跟这个有好多好多，大家可以看一看，关注一下他后面的一个注释。


在这里我就不特别的去跟大家去说这个事儿了，我先把这个退出，然后我们直接去讲干货，我把它来点，那现在呢？其实老师在这个 software 下已经有一个 fail beat 点 YML 了，那我直接把它 MV fail beat 点 y m l 到哪里？到我们 u s r local 下的 l beat 660 下面，OK，把它直接移动 n y o y 的覆盖掉。好，覆盖掉了以后，接下来我去 CD 到 USL local 下面 file beat 660 到他，然后我们 VM l b t 点 m l 现在这里边有好多配置，对不对？这里边的配置那我就一一跟大家去说，那我可能觉得这种配置，嗯，小伙伴们可能看不清，那这样的话我把它呢其实已经 copy 出来了，我们通过这个文档的形式跟大家来说明一下，把它打开。


好，我们来看一看这个 fail beat 老师是怎么去做配置的。那最开始呢？有一个 input type，就是说我这个 input 输入项是干什么的？我是做日志输出的，那你就写一个 log 就可以了。当然这个东西不是说强制，是说非得要写成一个这个log，你写成其他的，你自己的标记也可以，但是我个人建议一定要见名之意。


然后接下来这个 pass 看见了吗？就是你的输入，我的数据源是不是你的 pass 是什么地方？我的 pass 是 USR local 下的 logs 这个文件夹下的 app 杠connector，点log，那这个跟什么比较像？同学们想一想，也就是说我们之前的这个 collect 对应的这个工程，我需要打一个炸包，看见了吗？打一个炸包，打一个炸包之后，它的日志都输出哪？它的日志都输出到，看到这在 logo for 这 two 里边有说明，是不是都输出到这个 logs 这个文件夹下，然后杠 app 杠collection，这个是青岛符号，然后点log，也就是说它输出的这个文件的位置要跟你自己 fail beat 抓取那个地址应该对应上，也就是说现在我们一会儿就需要抓取那个应用服务的这个文件。


OK，然后这个 document type 是什么呢？就是说你可以自定义一种类型，这个写入 e s 的时候可能会需要用到，我们暂时不需要关注。重点来了，下面这个 multi land 这是什么意思？这个 militlan 的意思就是说我要怎么去抓取这个日志里边的数据，那我是以什么开头？我说我是以这个什么以中括号开头的，我认为是一条记录。那同学们还记得吗？我们自己的日志都是什么样子的？我们自己的日志都是以中括号开头的，看见了中括号开头为一条日志一行，对不对？然后中括号开头为一条日志，中括号开头，所以说你就用中括号开头就可以了。


那中括号开头的一条数据就认为是一个日志，那这个是非常简单的一个定义，然后这里面有一个叫做negate，就是否能够匹配到，我是说必须要匹配到处，然后 match 这个 after 老师后面都有对应的注释，对不对？同学们，其实如果你自己自学能力强的话，你看这个书睡，只不过老师在这里跟你详细的说一下， match 就是匹配到，就是合并到上一行的末尾，对不对？就是没有匹配到的这个中括号开头的，那我就把所有东西都合并到上一行的末尾了，上一行的末尾就是什么呢？其实同学们你会发现我们刚才的这个文件里边，比如说我们打 error 的是不是？我们在这里看这个 l 这个 error 的日志，那第二行，你看第二行这里边，你根本匹配不到这个中括号开头的，对不对？因为它是以这个空格开头，换行了是以 a 开头的，那他根本就匹配不到，那怎么办？其实这一行是一条日志，对不对？但是我在抓第二行数据的时候，我发现这不是以中号开头的，那我就把这一行记录合并到上一行，就认为他们两个是一条记录，以此类推，等等看，就是整个的这一串他认为是一条记录，就是做一个合并的工作，这是非要 beat 的一个特殊的功能。


然后接下来往下看，就是有一个叫做 Max line，就是说我认为最大我合并多少行，我这里边说最大 2000 行，也就是说如果你的这个 l 日志，你看我们现在才 50 多行哈，就是说白了才五十几行。如果你这个 l 日志打最大打到 2000 多行，那我就不帮你去再合并了。当然也没有这种极限情况，正常来讲其实 1000 行已经足够了。说白了，其实可以说 1000 行，几百行就已经足够了。 300 行，就你什么样的 l 能达到 300 行的日志呢？这个其实是很少数的，所以说我在这里只是给一个范围说 2000 行已经是最大限制了。然后 time out 在这里就是如果在规定的时间内没有新的日志生成，就是我的 log 日志里边没有新的日志，那我就不等待后面的日志了。那没有新的日志怎么办？难道说我不收集吗？不是的，我还要收集，那我指定它的超时间 time out 是 2 秒钟，就如果说我收集了一条日志，但是这条日志在 2 秒钟之后还没有新的日志的话，那我就不等待了，我就直接一次性的去推出去，就把我收集的日志推到其他的地方。


当然什么地方就是我们的卡斯卡了，这几个都是我们自己，我们 file beat 它规定的一些配置项。然后这个菲尔德斯同学们请看这个 fields 是固定的，但是这个 fields 下面是什么东西？下面的东西是我们自定义的一些 key g a t 有什么用？在这里比如说这个 log b i z，那我们给它起个名字叫做connector，就是我们的应用名称，然后这个叫做 log topic，也就是说什么意思？我们自己收集上来的日志，我们是要放到卡夫卡，那放到卡夫卡在哪呢？是不是你得指定放到卡夫卡的哪一个 topic 上？所以说在这里我就指定我要放到卡夫卡的 APP 杠log，杠 collect 这个 topic 下面就把所有的收集上来，符合这个条件的日志就是从这个文件里抓出来日志，都给它上报到卡夫卡这个里边。


这个 topic 下面，然后这个 EVN 就不说了，就是我们的 environment 开发环境，是不是这是我们的开发环境中写EVA，然后如果是测试环境或者生产环境，你可以对应的有一个p，l、 d 或者是一个 test 等等，然后对应着上面这个东西主要是抓取哪个文件？主要是抓取我们的全量的 app log，对不对？然后接下来再看，还有一个同样也是 type 等于log，然后这是什么？抓取的是 error 点connector，对不对？ error 杠 connect 点log，这是什么文件？那这个就是我们刚才所看到的这个文件嘛？是不是名字都是一样的？就是我们所有的错误的数据，我们也要做一个汇总。


OK，那接下来这个错误的数据也是匹配同样的规则，这都没有去变，然后注意 fields connector，然后这个 topic 变了，叫做 error 杠 log connector，上面这个是什么？叫做 APP 杠 log 杠connect，这个呢？只不过前缀换成 error 了，也是 DV 环境。


OK，那其实对应着上面这些东西就是我们要抓取的数据，要从哪个文件抓取，指定怎么抓取，是多行匹配还是单行匹配？然后是怎么样输出，对不对？怎么样输出？这里面有一个output，就是输出input，其实就输入了，对吧？ output 我们输入到什么地方？很明显我们要把抓取人的数据输出到卡斯卡上，所以说我就写 output 点卡不卡，当然它里边不仅仅是 output 点卡不卡，可以 output 点 elastic search，就是直接可以抓到 e s 上，这是没问题的。


enable 就启动了，然后卡夫卡的地址我们已经之前已经知道了，我们已经启动好了，是不是就是 51 这个节点？好，那就是幺九二点幺六八点，幺幺点五幺九零九二，然后对应的这个 topic 看见了吗？我在这里面用一个取余的这么一个大括号，然后后面加上中括号，这个中括号里面内容其实就能取到这个fields，对应的这个 topic 就是 log 杠 topic 中取到这个里边真实的值。


为什么？我在这里的动态的同学们想一下，因为你自己对于我们现在只是演示一个服务，叫做 collector.jar ，以后可能有千千万万种服务，对不对？所以说这里面我可以写成动态，包括其实这个里面我们可以动态去匹配，这些都是可以的。然后下面有一个叫做partition，哈希等于true，对不对？这是一个分区的一个规则，然后是否这个数据将数据压缩，我说 g z i p 的方式去把这个日志做一个压缩，让它性能更好一些，然后它这个 Max message base 就是最大的字节数是多大，其实这个你可以看是不是这是多少 10 兆。


然后接下来再往下看，就是 request a C k 这个 request a C k 是什么东西？是不是需不需要我们对应它，对它进行一个什么？ a C k 这块还记得吗？它里边有三个值，一个是0，还有一个-1，还有一个是1，分别代表什么含义？是不是大家你一定要回顾一下我们之前所学的卡夫卡 s k，这是生产者端把消息发送到卡夫卡，然后设置为一代表什么意思？给大家 2 秒钟时间思考一下， 1 其实就代表什么呢？只要说 master Kafka 上有一个节点能够存储，就是把数据写到磁盘上，那我就可以去返回 ACK 了。


后因是什么呢？ -1 就相当于说你必须要整个卡夫卡所有的 VPK 的副本都写完才能返回，这个效率是非常低的， 0 是不做任何的这个可靠性的保障。所以说我们去取一个相对来讲稍微靠谱一点的策略，就是等于一对吧。当然如果你想保障可靠性的话，你要设置什么会议也可以。然后最后就是我们的 log 点 to files 等于true，就没什么其他配置了，那这个对应的就是我们的 fail beat 配置。OK，那我们已经把 fail beat 的配置搞定了，之后我把它关掉，接下来的事情我们就可以做什么呢？我们现在其实就可以去做的事情很简单，其实你就可以去启动这个 file beat，因为我的配置已经配置好了，就是我们直接启动这个 fail beat 就可以了。


当然在这之前我们刚才跟小伙伴说了，我们把其他不相关的都关掉，你可以去检查你自己写的这个到底对不对？你自己写的到底对不对？这个配置如果出错了起不来，你是不是还得重新调？你可以用什么 fail beat 杠c，然后这个 fail beat 点 Yam 的 config test，如果它返回的是OK，证明什么呢？你的配置完全没有任何问题，是可以起来的，但现在你可以起来吗？其实现在你起来也无所谓，你可以去做起来，但我现在还不要让他起来，我现在要做几个准备工作。


首先第一点，我要把我自己刚才打的这个包，就是这个connector，这个包我要传到我的这个 Linux 服务器上，然后把它传上去，然后把它起来。同学们能理解我说意思。好，那在这里老师直接把它起来，把它这个传进来，直接拽过来，拽过来之后同学们请看，我这里边就有对应的什么呢？叫做connect，点jar，然后我是不是现在直接可以起来了？我说 jar 杠jar，然后 connector 这个 & (and) 语就是表示什么呢？后台启动嘛，是吧？现在直接把它起来，把这个程序掀起来，他说没有主清单属性。

```java
==============主清单=========================
<build>
        <finalName>collector</finalName>
        <!-- 打包的时候包含 properties.xml -->
        <resources>
            <resource>
                <directory>/src/main/java</directory>
                <includes>
                    <include>**/*.properties</include>
                    <include>**/*.xml</include>
                </includes>
                <!-- 是否替换资源中的属性 -->
                <filtering>true</filtering>
            </resource>
            <resource>
                <directory>/src/main/resources</directory>
            </resource>
        </resources>
        <plugins>
            <plugin>
                <groupId>org.springframework.boot</groupId>
                <artifactId>spring-boot-maven-plugin</artifactId>
                <configuration>
                    <mainClass>com.bfxy.collector.CollectorApplication</mainClass>
                </configuration>
            </plugin>
        </plugins>
    </build>
```

好，那这个遇到一个最头疼的问题，这个问题怎么去解决呢？就是说因为你是一个 spring boot 工程，你的 spring boot 工程如果没有主清单的话，它是起不来的，所以说你要在 Maven 里边加一个主清单的配置，就是在 build 的时候，在这里我们一起来做一下老师，在这里 copy 一下以前的，直接把以前的这个 copy 过来。然后我们一起来看一看这个配置什么意思。


首先这个 final name 就是打包的时候这个应用服务的名称叫什么？我们在这里可以给他起个名字叫做connector，就叫做connect。然后打包的时候能有一些 practice 或者 Xmail 文件，对不对？你可能需要引入，然后在这里就是你自己的主类了，这个就是主情感属性，对吧？我们是什么？我们是在这个包下的application，然后我们把它拿过来，是不是有这个包，你能点进去证明这个主题男属性？你是配置对了。然后接下来我们做的事情就是 Maven clear clean 之后，然后再做一个 its tel，对吧？再做一个重新打包install，然后我们再做一个可练之后，那这里面刷一下，它应该没有了，是吧？没有了 target 下面没有了，然后再去重新做一个 install 打包，打完包之后我们再把它传过去就可以了，咱们稍微耐心等待一下。其实我现在可以去把我之前的这个，因为没有主清单属性，可以把它先删除掉。 RM 杠二 f 我们的 connector 点大把，先删除是不是没有了？然后再重新上传，等着他打包，大家耐心等待一下。




